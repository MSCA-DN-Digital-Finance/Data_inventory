#!/usr/bin/env python3
"""Apply a reviewed website JSON proposal to a canonical CSV. Dry-run by default."""
import argparse
import csv
import json
import os
import shutil
from pathlib import Path
import tempfile
from build_site import ROOT, FILES, inventory


def apply_proposal(path, write=False):
    proposal = json.loads(Path(path).read_text())
    kind, action, record = proposal['kind'], proposal['action'], proposal['record']
    if kind not in FILES or action not in ('add', 'update') or not isinstance(record, dict):
        raise ValueError('Expected kind source/dataset, action add/update and a record object')
    target = ROOT / 'data' / FILES[kind]
    with target.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fields, rows = reader.fieldnames, list(reader)
    unknown = set(record) - set(fields)
    # The website uses collection for both types; datasets retain legacy availability.
    if kind == 'dataset' and 'collection' in unknown:
        record['availability'] = record.pop('collection') or record.get('access_notes', '')
        unknown.remove('collection')
    if unknown:
        raise ValueError(f'Unknown fields: {sorted(unknown)}')
    if not all(isinstance(v, str) for v in record.values()):
        raise ValueError('All record fields must be strings')
    # Keep the legacy README summaries useful for website-originated changes.
    if kind == 'source' and 'access_category' in record:
        record['access'] = {'public': 'Public', 'request': 'Request access', 'institutional': 'Private - institutional licence', 'restricted': 'Private - restricted', 'unknown': 'Not documented'}.get(record['access_category'], '')
    if kind == 'dataset' and 'quality_notes' in record:
        record['clean'] = record['quality_notes']
    matches = [i for i, r in enumerate(rows) if r['id'] == record.get('id')]
    if action == 'add':
        if matches:
            raise ValueError('ID already exists; use an update proposal')
        rows.append({f: record.get(f, '') for f in fields})
    else:
        if len(matches) != 1:
            raise ValueError('Update requires an existing ID')
        rows[matches[0]].update(record)
    # Validate in an isolated copy so dry-runs and failed proposals never touch live CSVs.
    with tempfile.TemporaryDirectory() as staging:
        staging_root = Path(staging)
        shutil.copytree(ROOT / 'data', staging_root / 'data')
        staged_target = staging_root / 'data' / FILES[kind]
        with staged_target.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        inventory(staging_root)
        if write:
            # Write on the target filesystem, then replace the CSV atomically.
            with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as f:
                tmp = Path(f.name)
                f.write(staged_target.read_bytes())
            try:
                os.replace(tmp, target)
            finally:
                tmp.unlink(missing_ok=True)
    print(f"{'Applied' if write else 'Valid dry run for'} {action}: {kind}/{record['id']}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('proposal', type=Path)
    parser.add_argument('--write', action='store_true', help='Write the validated change; otherwise dry-run')
    args = parser.parse_args()
    apply_proposal(args.proposal, args.write)
