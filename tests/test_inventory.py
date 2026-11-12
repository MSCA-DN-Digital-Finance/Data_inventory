import csv
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import build_site
import import_proposal


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'data').mkdir()
        for kind, filename in build_site.FILES.items():
            (self.root / 'data' / filename).write_bytes((build_site.ROOT / 'data' / filename).read_bytes())
        self.builder = patch.object(build_site, 'ROOT', self.root)
        self.importer = patch.object(import_proposal, 'ROOT', self.root)
        self.builder.start()
        self.importer.start()
        self.addCleanup(self.builder.stop)
        self.addCleanup(self.importer.stop)
        self.addCleanup(self.tmp.cleanup)

    def proposal(self, **changes):
        record = dict(build_site.inventory()['datasets'][0])
        record.update(changes)
        path = self.root / 'proposal.json'
        path.write_text(json.dumps({'kind':'dataset', 'action':'update', 'record':record}))
        return path

    def test_dry_run_preserves_csv(self):
        target = self.root / 'data/datasets.csv'
        before = target.read_bytes()
        import_proposal.apply_proposal(self.proposal(quality_notes='Updated notes, with commas\nand a newline'))
        self.assertEqual(target.read_bytes(), before)

    def test_apply_preserves_multiline_and_other_records(self):
        before = build_site.inventory()
        import_proposal.apply_proposal(self.proposal(quality_notes='Updated notes, with commas\nand a newline'), True)
        after = build_site.inventory()
        self.assertEqual(after['datasets'][0]['quality_notes'], 'Updated notes, with commas\nand a newline')
        self.assertEqual(after['datasets'][1:], before['datasets'][1:])
        self.assertEqual(after['sources'], before['sources'])

    def test_invalid_reference_restores_csv(self):
        target = self.root / 'data/datasets.csv'
        before = target.read_bytes()
        with self.assertRaises(ValueError):
            import_proposal.apply_proposal(self.proposal(source_ids='does-not-exist'), True)
        self.assertEqual(target.read_bytes(), before)

    def test_unsafe_url_rejected(self):
        with self.assertRaises(ValueError):
            import_proposal.apply_proposal(self.proposal(link='javascript:alert(1)'), True)

    def test_duplicate_id_rejected(self):
        path = self.proposal()
        p = json.loads(path.read_text()); p['action'] = 'add'; path.write_text(json.dumps(p))
        with self.assertRaises(ValueError):
            import_proposal.apply_proposal(path, True)

    def test_add_source_from_website_fields(self):
        record = {'id': 'test-provider', 'name': 'Test provider', 'short_description': 'A new source', 'subjects': 'finance', 'access_category': 'public', 'access_notes': 'Download via public website', 'link': 'https://example.org'}
        path = self.root / 'new.json'
        path.write_text(json.dumps({'kind': 'source', 'action': 'add', 'record': record}))
        import_proposal.apply_proposal(path, True)
        source = build_site.inventory()['sources'][-1]
        self.assertEqual(source['id'], 'test-provider')
        self.assertEqual(source['access'], 'Public')

    def test_clear_dataset_source_relationship(self):
        import_proposal.apply_proposal(self.proposal(source_ids=''), True)
        self.assertEqual(build_site.inventory()['datasets'][0]['source_ids'], '')

    def test_website_dataset_delivery_mapping(self):
        path = self.proposal()
        p = json.loads(path.read_text()); del p['record']['availability']; p['record']['collection']='Download via provider'
        path.write_text(json.dumps(p))
        import_proposal.apply_proposal(path, True)
        self.assertEqual(build_site.inventory()['datasets'][0]['availability'], 'Download via provider')

if __name__ == '__main__':
    unittest.main()
