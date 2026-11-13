"""One publication hold policy governs packages and both usable inventories."""

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from skill_dependencies import publication_catalogue  # noqa: E402


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


index = load("hold_index", "build-index.py")
agents = load("hold_agents", "build-agent-skills.py")
packages = load("hold_packages", "build-packages.py")


def document(name, status="", dependencies=(), extra=""):
    dep = "depends_on:\n" + "".join(f"  - {d}\n" for d in dependencies) if dependencies else ""
    hold = f"status: {status}\n" if status else ""
    return f"---\nname: {name}\njurisdiction: XX\n{hold}{dep}{extra}---\n\n# {name}\n\nRule body.\n"


class BuilderHoldTests(unittest.TestCase):
    def test_hold_closure_excludes_usable_outputs_and_preserves_sources(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            src = root / "skills/example"
            src.mkdir(parents=True)
            texts = {
                "held": document("held", "needs_sources"),
                "child": document("child", dependencies=["held"]),
                "grandchild": document("grandchild", dependencies=["child"]),
                "standard": document("standard", extra="domain: financial-reporting\nstandard: IFRS\n"),
            }
            for name, text in texts.items():
                (src / f"{name}.md").write_text(text)
            _all, targets, held, errors = publication_catalogue(root)
            self.assertEqual(errors, [])
            self.assertEqual(set(held), {"held", "child", "grandchild"})
            self.assertEqual(set(targets), {"standard"})
            with patch.object(index, "REPO_ROOT", str(root)):
                result = index.build_index()
            self.assertEqual({g["mcp_slug"] for g in result["guides"]}, {"standard"})
            self.assertEqual(result["counts"]["held_skill_names"], 3)
            with patch.object(agents, "REPO_ROOT", root), \
                 patch.object(agents, "iter_source_files", return_value=sorted(src.glob("*.md"))), \
                 patch.object(agents, "OUT_DIR", root / "agent-skills"), \
                 patch.object(agents, "PLUGIN_SKILLS_DIR", root / "plugin"):
                self.assertEqual(agents.build({"XX"}, False), 0)
            generated = json.loads((root / "agent-skills/index.json").read_text())
            self.assertEqual([s["name"] for s in generated["skills"]], ["standard"])
            self.assertEqual({h["name"] for h in generated["publication_holds"]}, set(held))
            bundle = root / "packages/example"
            bundle.mkdir(parents=True)
            for name, text in texts.items():
                (bundle / f"{name}.md").write_text(text)
            files = [f"{name}.md" for name in texts]
            with patch.object(packages, "dependency_targets", return_value=targets):
                packages.include_dependencies(str(bundle), files)
            self.assertEqual(files, ["standard.md"])
            self.assertEqual({p.name for p in bundle.iterdir()}, {"standard.md"})
            for name, text in texts.items():
                self.assertEqual((src / f"{name}.md").read_text(), text)

    def test_direct_conversion_cannot_strip_source_hold(self):
        with self.assertRaisesRegex(ValueError, "Cannot convert held skill"):
            agents.skill_md("held", {"status": "needs_sources"}, "Rule body")

    def test_index_refuses_malformed_or_ambiguous_source_catalogue(self):
        for problem in ("malformed", "ambiguous"):
            with self.subTest(problem=problem), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                source = root / "skills/example"
                source.mkdir(parents=True)
                if problem == "malformed":
                    (source / "bad.md").write_text(document("bad", extra="depends_on: not-a-list\n"))
                else:
                    (source / "first.md").write_text(document("same"))
                    (source / "second.md").write_text(document("same").replace("Rule body.", "Different guidance."))
                with patch.object(index, "REPO_ROOT", str(root)):
                    with self.assertRaisesRegex(ValueError, "Invalid source catalogue"):
                        index.build_index()

    def test_actual_held_source_files_are_held_without_dependents(self):
        _skills, targets, held, errors = publication_catalogue(ROOT)
        self.assertEqual(errors, [])
        names = {"fl-sales-tax", "wi-payroll"}
        for name in names:
            self.assertEqual(held[name], "status: needs_sources")
            self.assertNotIn(name, targets)
        self.assertIn("workflow-base", targets)
        self.assertTrue(any(json.loads(s.context).get("domain") == "financial-reporting" for s in targets.values()))


if __name__ == "__main__":
    unittest.main()
