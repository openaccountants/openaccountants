"""Generated inventory and packages remove endorsements without changing sources."""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


index = load('index_public_test', 'build-index.py')
packages = load('packages_public_test', 'build-packages.py')
llms = load('llms_public_test', 'build-llms-full.py')

GUIDE = '''---
name: sample
jurisdiction: MT
category: international
tax_year: 2026
tier: 1
reviewed_by: Reviewer CPA
authored_by: Actual Author
---
# Sample
**Reviewed by:** Reviewer CPA
15% in 2026 [official source](https://example.gov/tax).
The records must be verified by the Commissioner.
'''


class PublicGeneratorTests(unittest.TestCase):
    def test_index_and_inventory_preserve_coverage_and_author_without_endorsement(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'skills/sample.md'
            path.parent.mkdir()
            path.write_text(GUIDE)
            with mock.patch.object(index, 'REPO_ROOT', tmp):
                result = index.build_index()
            self.assertEqual(result['counts'], {'guides': 1, 'jurisdictions': 1})
            self.assertEqual(result['schema_version'], 2)
            self.assertEqual(result['guides'][0]['authored_by'], 'Actual Author')
            self.assertEqual(result['guides'][0]['tax_year'], '2026')
            self.assertNotIn('Reviewer CPA', json.dumps(result))
            self.assertNotIn('tier', result['guides'][0])
            with mock.patch.object(llms, 'read_text', return_value=json.dumps(result)):
                inventory = llms.guide_inventory()
            self.assertIn('tax year 2026 | author Actual Author', inventory)
            self.assertNotIn('reviewed', inventory)

    def test_package_copy_retains_rules_and_does_not_edit_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp) / 'src.md', Path(tmp) / 'dst.md'
            src.write_text(GUIDE)
            packages.copy_public_guide(src, dst)
            result = dst.read_text()
            self.assertEqual(src.read_text(), GUIDE)
            self.assertNotIn('Reviewer CPA', result)
            self.assertNotIn('tier:', result)
            self.assertIn('authored_by: Actual Author', result)
            self.assertIn('15% in 2026 [official source](https://example.gov/tax).', result)
            self.assertIn('The records must be verified by the Commissioner.', result)
