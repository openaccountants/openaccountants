from __future__ import annotations

import unittest
from unittest.mock import patch

from openaccountants_mcp import server


def _record(number: int, jurisdiction: str = "AU") -> dict[str, str]:
    return {
        "slug": f"skill-{number}",
        "title": f"Skill {number}",
        "jurisdiction": jurisdiction,
    }


def _body(slug: str) -> tuple[dict[str, str], str]:
    return {"slug": slug}, "# Topic\n\nA searchable phrase appears here."


class SearchSkillsTests(unittest.TestCase):
    def test_reports_exact_total_when_complete(self) -> None:
        records = {f"skill-{number}": _record(number) for number in range(3)}

        with patch.object(server, "_index", return_value=records), patch.object(
            server, "_read_skill", side_effect=_body
        ):
            response = server.search_skills("searchable phrase")

        self.assertEqual(response["returned"], 3)
        self.assertEqual(response["total"], 3)
        self.assertFalse(response["truncated"])
        self.assertEqual(response["limit"], server.SEARCH_LIMIT)

    def test_stops_after_one_match_beyond_limit(self) -> None:
        records = {
            f"skill-{number}": _record(number)
            for number in range(server.SEARCH_LIMIT + 10)
        }

        with patch.object(server, "_index", return_value=records), patch.object(
            server, "_read_skill", side_effect=_body
        ) as read_skill:
            response = server.search_skills("searchable phrase")

        self.assertEqual(response["returned"], server.SEARCH_LIMIT)
        self.assertEqual(len(response["results"]), server.SEARCH_LIMIT)
        self.assertEqual(response["total"], server.SEARCH_LIMIT)
        self.assertTrue(response["truncated"])
        self.assertEqual(read_skill.call_count, server.SEARCH_LIMIT + 1)
        self.assertIn("Narrow the query", response["next_action"])

    def test_non_matching_jurisdictions_do_not_trigger_truncation(self) -> None:
        records = {
            **{f"au-{number}": _record(number, "AU") for number in range(2)},
            **{
                f"gb-{number}": {
                    **_record(number, "GB"),
                    "slug": f"gb-skill-{number}",
                }
                for number in range(server.SEARCH_LIMIT + 5)
            },
        }

        with patch.object(server, "_index", return_value=records), patch.object(
            server, "_read_skill", side_effect=_body
        ):
            response = server.search_skills("searchable phrase", jurisdiction="AU")

        self.assertEqual(response["returned"], 2)
        self.assertEqual(response["total"], 2)
        self.assertFalse(response["truncated"])


if __name__ == "__main__":
    unittest.main()
