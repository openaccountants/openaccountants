"""The Hermes plugin bundle (plugins/openaccountants-hermes/) must be a valid portable
Agent Plugins v1 package: plugin.json and mcp.json parse, and every skills/<slug>/SKILL.md
carries frontmatter the Hermes loader accepts (name matches the folder, description present).
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "plugins" / "openaccountants-hermes"


class HermesBundleTests(unittest.TestCase):
    def test_plugin_json_is_agent_plugins_v1(self) -> None:
        data = json.loads((BUNDLE / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(
            data["$schema"], "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
        )
        self.assertEqual(data["name"], "openaccountants")
        self.assertIsInstance(data.get("description"), str)
        self.assertTrue(data.get("description"))

    def test_mcp_json_declares_the_connector(self) -> None:
        data = json.loads((BUNDLE / "mcp.json").read_text(encoding="utf-8"))
        self.assertEqual(
            data["$schema"], "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
        )
        server = data["mcpServers"]["openaccountants"]
        self.assertEqual(server["type"], "streamable-http")
        self.assertEqual(server["url"], "https://www.openaccountants.com/api/mcp")

    def test_skills_mirror_agent_skills(self) -> None:
        bundle_slugs = {
            p.parent.name for p in (BUNDLE / "skills").glob("*/SKILL.md")
        }
        agent_slugs = {
            p.parent.name for p in (ROOT / "agent-skills").glob("*/SKILL.md")
        }
        self.assertTrue(bundle_slugs, "the bundle ships no skills")
        self.assertEqual(bundle_slugs, agent_slugs)

    def test_every_skill_frontmatter_matches_its_folder(self) -> None:
        for skill_md in (BUNDLE / "skills").glob("*/SKILL.md"):
            text = skill_md.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), f"{skill_md} has no frontmatter")
            end = text.index("\n---\n", 3)
            fm = text[3:end]
            self.assertIn(
                f"\nname: {skill_md.parent.name}\n", fm + "\n",
                f"{skill_md} frontmatter name does not match its folder",
            )
            self.assertIn("description:", fm, f"{skill_md} has no description")


if __name__ == "__main__":
    unittest.main()
