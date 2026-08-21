#!/usr/bin/env python3
"""
Verification utility to test the OpenAccountants MCP server locally.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Add mcp/ to path
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "mcp"))

from openaccountants_mcp import server


def main() -> int:
    print("Testing OpenAccountants MCP Server Initialization...")
    tools = [
        "start",
        "list_skills",
        "get_skill",
        "get_skill_sections",
        "search_skills",
        "submit_feedback",
    ]

    # Test list_skills
    skills_result = server.list_skills(jurisdiction="AU")
    assert "skills" in skills_result, "list_skills must return 'skills'"
    print(f"  [PASS] list_skills(jurisdiction='AU') returned {skills_result['total']} skills")

    # Test start tool
    plan = server.start(intent="taxes", jurisdiction="AU")
    assert plan.get("status") == "ready", "start tool must return ready status"
    print(f"  [PASS] start(intent='taxes', jurisdiction='AU') planned {len(plan.get('skills_to_load', []))} skills")

    # Test search_skills
    search_res = server.search_skills(query="super guarantee", jurisdiction="AU")
    assert search_res.get("total", 0) > 0, "search_skills should find matches for 'super guarantee'"
    print(f"  [PASS] search_skills('super guarantee', 'AU') found {search_res['total']} matches")

    print("\nAll MCP tool verifications passed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
