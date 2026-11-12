"""A source must not publish an unresolvable parent or ambiguous name."""

from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from skill_dependencies import add_package_dependencies, catalogue  # noqa: E402


def content(name, body="Guidance.", jurisdiction="XX", dependencies=()):
    deps = "depends_on:\n" + "".join(f"  - {d}\n" for d in dependencies) if dependencies else ""
    return f"---\nname: {name}\njurisdiction: {jurisdiction}\n{deps}---\n\n# {name}\n\n{body}\n"


class SkillDependenciesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
        return target

    def test_missing_dependency_fails_even_when_child_did_not_change(self):
        self.write("skills/example/child.md", content("child", dependencies=["removed-parent"]))
        _skills, _targets, errors = catalogue(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("skills/example/child.md", errors[0])
        self.assertIn("removed-parent", errors[0])

    def test_filename_is_not_enough_the_mcp_loads_the_declared_name(self):
        self.write("skills/example/parent.md", content("other-name"))
        self.write("skills/example/child.md", content("child", dependencies=["parent"]))
        self.assertTrue(catalogue(self.root)[2])

    def test_same_name_with_different_guidance_is_an_error(self):
        self.write("skills/a/tax.md", content("tax", "A"))
        self.write("skills/b/tax.md", content("tax", "B"))
        self.assertIn("ambiguous skill name `tax`", catalogue(self.root)[2][0])

    def test_same_body_different_country_is_still_ambiguous(self):
        self.write("skills/a/tax.md", content("tax", jurisdiction="GA"))
        self.write("skills/b/tax.md", content("tax", jurisdiction="US-GA"))
        self.assertTrue(catalogue(self.root)[2])

    def test_same_body_same_place_collapses_without_losing_a_dependency(self):
        text = content("parent")
        self.write("skills/a/parent.md", text)
        self.write("skills/b/parent.md", text)
        self.write("skills/a/child.md", content("child", dependencies=["parent"]))
        self.assertEqual(catalogue(self.root)[2], [])

    def test_hand_authored_federal_precedence_matches_the_mcp(self):
        self.write("skills/us/federal/federal.md", content("federal", "Generated", "US"))
        manual = self.write("packages/us-federal/federal.md", content("federal", "Manual", "US"))
        _skills, targets, errors = catalogue(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(targets["federal"].path, manual)

    def test_documentation_is_not_a_loadable_parent(self):
        self.write("skills/example/references.md", content("references"))
        self.write("skills/example/child.md", content("child", dependencies=["references"]))
        self.assertTrue(catalogue(self.root)[2])

    def test_another_country_cannot_hide_a_collision_behind_federal_precedence(self):
        self.write("skills/gabon/federal.md", content("federal", "Other country", "GA"))
        self.write("packages/us-federal/federal.md", content("federal", "Manual", "US"))
        self.assertTrue(catalogue(self.root)[2])

    def test_malformed_dependency_type_fails(self):
        self.write("skills/example/child.md", content("child").replace("jurisdiction: XX", "jurisdiction: XX\ndepends_on: parent"))
        self.assertIn("must be a YAML list", catalogue(self.root)[2][0])

    def test_package_contains_transitive_dependencies_and_keeps_source_bytes(self):
        child = self.write("skills/example/child.md", content("child", dependencies=["parent"]))
        parent = self.write("skills/global/methods/parent.md", content("parent", dependencies=["base"]))
        base = self.write("skills/global/methods/base.md", content("base"))
        package = self.root / "packages/example"
        package.mkdir(parents=True)
        (package / "child.md").write_bytes(child.read_bytes())
        files = ["child.md"]
        add_package_dependencies(package, files, catalogue(self.root)[1])
        self.assertEqual(files, ["child.md", "parent.md", "base.md"])
        self.assertEqual((package / "parent.md").read_bytes(), parent.read_bytes())
        self.assertEqual((package / "base.md").read_bytes(), base.read_bytes())

    def test_dependency_does_not_overwrite_an_occupied_filename(self):
        self.write("skills/example/child.md", content("child", dependencies=["parent"]))
        self.write("skills/global/methods/parent.md", content("parent"))
        package = self.root / "packages/example"
        package.mkdir(parents=True)
        (package / "child.md").write_text(content("child", dependencies=["parent"]))
        (package / "parent.md").write_text(content("other-name", "Do not overwrite"))
        with self.assertRaisesRegex(ValueError, "overwrite"):
            add_package_dependencies(package, ["child.md", "parent.md"], catalogue(self.root)[1])
        self.assertIn("Do not overwrite", (package / "parent.md").read_text())

    def test_current_source_graph_has_no_missing_or_ambiguous_names(self):
        _skills, _targets, errors = catalogue(ROOT)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
