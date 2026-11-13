"""A source hold must survive old packages, aliases and cached catalogues."""

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from openaccountants_mcp import server
from openaccountants_mcp.eligibility import publication_holds


def document(name, status="", dependencies=()):
    dep = "depends_on:\n" + "".join(f"  - {d}\n" for d in dependencies) if dependencies else ""
    hold = f"status: {status}\n" if status else ""
    return f"---\nname: {name}\njurisdiction: XX\n{hold}{dep}---\n\n# {name}\n\nRule body.\n"


class PublicationHoldTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.patch = patch.object(server, "PACKAGES_DIR", self.root)
        self.patch.start()
        server._index.cache_clear()
        self.addCleanup(self.temp.cleanup)
        self.addCleanup(self.patch.stop)
        self.addCleanup(server._index.cache_clear)

    def write(self, name, status="", dependencies=(), folder="xx"):
        path = self.root / folder / f"{name}.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text(document(name, status, dependencies))
        return path

    def test_held_file_cannot_list_load_search_or_return_sections(self):
        self.write("held", "needs_sources")
        self.write("safe")
        self.assertEqual([r["slug"] for r in server.list_skills()["skills"]], ["safe"])
        self.assertEqual([r["slug"] for r in server.search_skills("Rule")["results"]], ["safe"])
        for read in (server.get_skill, server.get_skill_sections):
            with self.assertRaisesRegex(server.ToolInputError, "held from publication"):
                read("held")
        self.assertIn("Rule body", server.get_skill("safe")["markdown"])

    def test_transitive_required_companion_is_held_without_replacement(self):
        self.write("held", "needs_sources")
        self.write("child", dependencies=["held"])
        self.write("grandchild", dependencies=["child"])
        self.write("safe")
        self.assertEqual(set(server._index()), {"safe"})
        for name in ("child", "grandchild"):
            with self.assertRaisesRegex(server.ToolInputError, "required companion unavailable"):
                server.get_skill(name)

    def test_new_hold_after_cache_removes_parent_from_list_and_blocks_read(self):
        path = self.write("parent")
        self.write("child", dependencies=["parent"])
        self.assertIn("child", server._index())
        path.write_text(document("parent", "needs_sources"))
        self.assertEqual(server.list_skills()["total"], 0)
        with self.assertRaisesRegex(server.ToolInputError, "required companion.*unavailable"):
            server.get_skill("child")
        with self.assertRaisesRegex(server.ToolInputError, "held from publication"):
            server.get_skill("parent")

    def test_identical_active_alias_cannot_erase_held_copy(self):
        self.write("alias", folder="aa")
        self.write("alias", "needs_sources", folder="zz")
        self.assertNotIn("alias", server._index())
        with self.assertRaisesRegex(server.ToolInputError, "needs_sources"):
            server.get_skill("alias")

    def test_hold_added_to_unselected_alias_after_cache_still_blocks(self):
        self.write("alias", folder="aa")
        path = self.write("alias", folder="zz")
        self.assertIn("alias", server._index())
        path.write_text(document("alias", "needs_sources"))
        self.assertNotIn("alias", server._index())
        with self.assertRaisesRegex(server.ToolInputError, "needs_sources"):
            server.get_skill("alias")

    def test_standards_are_not_held_for_non_tax_dates_or_missing_approval(self):
        self.write("ifrs-standard")
        self.assertEqual(publication_holds({"ifrs-standard": {
            "domain": "financial-reporting", "standard": "IFRS", "tier": 2,
        }}), {})
        self.assertIn("Rule body", server.get_skill("ifrs-standard")["markdown"])

    def test_missing_required_companion_is_explicitly_unavailable(self):
        self.write("child", dependencies=["absent"])
        with self.assertRaisesRegex(server.ToolInputError, "required companion unavailable: absent"):
            server.get_skill("child")


if __name__ == "__main__":
    unittest.main()
