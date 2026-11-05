"""The Hermes plugin bundle (plugins/openaccountants-hermes/) must be a valid portable
Agent Plugins v1 package: plugin.json and mcp.json parse, and the bundle ships no
skills. Every enabled plugin skill adds a row to the skills index on every turn, so
the full library lives in agent-skills/ and installs per jurisdiction via install.sh
instead of registering as plugin skills.
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

    def test_bundle_ships_no_plugin_skills(self) -> None:
        # 2,000+ plugin-skill rows cost tens of thousands of tokens per turn.
        # The library installs per jurisdiction from agent-skills/ instead.
        skills = BUNDLE / "skills"
        self.assertFalse(
            skills.exists() and any(skills.glob("*/SKILL.md")),
            "the Hermes bundle must not register the full skill library as plugin skills",
        )

    def test_agent_skills_tree_is_the_install_path(self) -> None:
        # The skills-hub tap the README points users at must exist and be browsable.
        self.assertTrue((ROOT / "agent-skills" / "index.json").exists())
        self.assertTrue((ROOT / "agent-skills" / "install.sh").exists())


if __name__ == "__main__":
    unittest.main()
