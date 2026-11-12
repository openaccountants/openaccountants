"""Source filenames must not become invented MCP names in machine inventories."""

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from skill_dependencies import catalogue  # noqa: E402


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


index_builder = load("identity_index_builder", "build-index.py")
llms_builder = load("identity_llms_builder", "build-llms-full.py")


class IndexSkillIdentityTests(unittest.TestCase):
    def test_same_filename_keeps_distinct_loadable_names(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for country in ("ae", "sa"):
                path = root / f"skills/global/cross-border/eg-{country}/dtt-summary.md"
                path.parent.mkdir(parents=True)
                path.write_text(f"---\nname: eg-{country}-corridor\njurisdiction: EG-{country.upper()}\n---\n\n# Treaty\n")
            for rel, name in (("skills/example/references.md", "references"),
                              ("skills/global/_templates/dtt-template.md", "dtt-template")):
                path = root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f"---\nname: {name}\n---\n\n# Authoring document\n")
            with patch.object(index_builder, "REPO_ROOT", str(root)):
                index = index_builder.build_index()
            corridors = [g for g in index["guides"] if g["slug"] == "dtt-summary"]
            self.assertEqual({g["mcp_slug"] for g in corridors}, {"eg-ae-corridor", "eg-sa-corridor"})
            self.assertEqual(index["counts"]["loadable_skill_names"], 2)
            self.assertTrue(all(g["mcp_slug"] is None for g in index["guides"] if g not in corridors))
            with patch.object(llms_builder, "read_text", return_value=json.dumps(index)):
                text = llms_builder.guide_inventory()
            self.assertIn("- eg-ae-corridor | EG-AE", text)
            self.assertIn("- eg-sa-corridor | EG-SA", text)
            self.assertNotIn("- dtt-summary |", text)
            self.assertNotIn("- dtt-template |", text)
            self.assertNotIn("- references |", text)

    def test_real_index_names_cover_the_source_catalogue_exactly(self):
        _skills, targets, errors = catalogue(ROOT)
        self.assertEqual(errors, [])
        index = index_builder.build_index()
        names = {g["mcp_slug"] for g in index["guides"] if g["mcp_slug"]}
        self.assertEqual(names, set(targets))
        self.assertEqual(index["counts"]["loadable_skill_names"], len(targets))


if __name__ == "__main__":
    unittest.main()
