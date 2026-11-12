#!/usr/bin/env python3
"""Validate the canonical CSV files and build a dependency-free GitHub Pages site."""
import csv
import html
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {'public', 'request', 'institutional', 'restricted', 'unknown'}
FILES = {'source': 'data-sources.csv', 'dataset': 'datasets.csv'}


def validate_url(value):
    return not value or (urlsplit(value).scheme in ('http', 'https') and bool(urlsplit(value).netloc))


def read_records(kind, root=None):
    path = (root or ROOT) / 'data' / FILES[kind]
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        if not fields or len(fields) != len(set(fields)):
            raise ValueError(f'{path}: missing or duplicate columns')
        rows = list(reader)
    seen = set()
    for line, row in enumerate(rows, 2):
        if None in row or any(v is None for v in row.values()):
            raise ValueError(f'{path}:{line}: row does not match CSV header')
        for key in row:
            row[key] = row[key].strip()
        label = row.get('name' if kind == 'source' else 'dataset_name')
        if not label or not row.get('short_description') or not row.get('subjects'):
            raise ValueError(f'{path}:{line}: name, description and subjects are required')
        rid = row.get('id', '')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', rid) or rid in seen:
            raise ValueError(f'{path}:{line}: invalid or duplicate id {rid!r}')
        seen.add(rid)
        if row.get('access_category') not in CATEGORIES or not row.get('access_notes'):
            raise ValueError(f'{path}:{line}: access category and notes are required')
        for key in ('link', 'documentation_url'):
            if not validate_url(row.get(key, '')):
                raise ValueError(f'{path}:{line}: {key} must be an HTTP(S) URL')
        if row.get('last_reviewed'):
            from datetime import date
            date.fromisoformat(row['last_reviewed'])
    return rows


def inventory(root=None):
    sources, datasets = read_records('source', root), read_records('dataset', root)
    source_ids = {r['id'] for r in sources}
    for row in datasets:
        refs = set(filter(None, row.get('source_ids', '').split(';')))
        if refs - source_ids:
            raise ValueError(f"{row['id']}: unknown source IDs: {refs - source_ids}")
    return {'sources': sources, 'datasets': datasets}


def build():
    data = inventory()
    out = ROOT / '_site'
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ROOT / 'site', out, ignore=shutil.ignore_patterns('config.json'))
    config = json.loads((ROOT / 'site/config.json').read_text())
    payload = json.dumps({**data, 'config': config}, ensure_ascii=False).replace('<', '\\u003c')
    fallback = ''.join(f'<li><a href="{html.escape(r.get("link") or config["repository"], quote=True)}">{html.escape(r.get("name") or r["dataset_name"])}</a> — {html.escape(r["access_notes"])}</li>' for r in data['sources'] + data['datasets'])
    for page in out.glob('*.html'):
        page.write_text(page.read_text().replace('<!-- INVENTORY_DATA -->', f'<script type="application/json" id="inventory-data">{payload}</script>').replace('<!-- FALLBACK -->', fallback), encoding='utf-8')
    shutil.copytree(ROOT / 'data', out / 'data')
    (out / 'data/inventory.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    shutil.copy2(ROOT / 'logo-nobackground-5000.png', out / 'assets/digital-logo.png')
    shutil.copy2(ROOT / 'EU-logo(2).png', out / 'assets/eu-funded.png')
    (out / '.nojekyll').touch()
    print(f"Built {len(data['sources'])} sources and {len(data['datasets'])} datasets → {out}")

if __name__ == '__main__':
    build()
