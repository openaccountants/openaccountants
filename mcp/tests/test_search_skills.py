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
        self.assertNotIn("total", response)
        self.assertFalse(response["truncated"])
        self.assertEqual(response["limit"], server.SEARCH_LIMIT)
        self.assertEqual(response["unreadable_skipped"], 0)

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
        self.assertFalse(response["truncated"])


class SearchBoundaryTests(unittest.TestCase):
    """Exactly at the cap. Without this the boundary the change exists to get
    right is unverified: a refactor evaluating the cap before the body-match
    check passes every other test while a 25-match query reports truncated."""

    @staticmethod
    def _reader(non_matching: set[str]):
        def read(slug: str) -> tuple[dict[str, str], str]:
            if slug in non_matching:
                return {"slug": slug}, "# Topic\n\nNothing relevant here.\n"
            return _body(slug)

        return read

    def test_exactly_at_the_limit_is_not_truncated(self) -> None:
        """25 matches, then skills that do not match. The cap must be reached by
        a 26th match, not by the 26th record the loop happens to visit."""
        total = server.SEARCH_LIMIT + 5
        records = {f"skill-{number}": _record(number) for number in range(total)}
        quiet = {f"skill-{number}" for number in range(server.SEARCH_LIMIT, total)}

        with patch.object(server, "_index", return_value=records), patch.object(
            server, "_read_skill", side_effect=self._reader(quiet)
        ):
            response = server.search_skills("searchable phrase")

        self.assertEqual(response["returned"], server.SEARCH_LIMIT)
        self.assertFalse(response["truncated"])
        self.assertNotIn("Narrow the query", response["next_action"])

    def test_one_past_the_limit_is_truncated(self) -> None:
        records = {
            f"skill-{number}": _record(number)
            for number in range(server.SEARCH_LIMIT + 1)
        }

        with patch.object(server, "_index", return_value=records), patch.object(
            server, "_read_skill", side_effect=_body
        ):
            response = server.search_skills("searchable phrase")

        self.assertEqual(response["returned"], server.SEARCH_LIMIT)
        self.assertTrue(response["truncated"])


class UnreadableSkillTests(unittest.TestCase):
    """An unreadable body must be counted, not swallowed."""

    @staticmethod
    def _reader(unreadable: set[str]):
        def read(slug: str) -> tuple[dict[str, str], str]:
            if slug in unreadable:
                raise OSError("file moved after the index snapshot")
            return _body(slug)

        return read

    def test_unreadable_matches_are_reported_not_swallowed(self) -> None:
        """10 skills match, 3 move after the lru_cached _index() snapshot; the
        caller used to be told returned 7 with nothing else said."""
        records = {f"skill-{number}": _record(number) for number in range(10)}
        gone = {"skill-2", "skill-5", "skill-8"}

        with patch.object(server, "_index", return_value=records), patch.object(
            server, "_read_skill", side_effect=self._reader(gone)
        ):
            response = server.search_skills("searchable phrase")

        self.assertEqual(response["returned"], 7)
        self.assertEqual(response["unreadable_skipped"], 3)
        self.assertEqual(sorted(response["unreadable_slugs"]), sorted(gone))
        self.assertIn("may be incomplete", response["next_action"])

    def test_an_unreadable_match_past_the_cap_does_not_claim_completeness(self) -> None:
        """When every match past the cap is unreadable the loop never reaches a
        26th success, so truncated stays false. The skipped count is then the
        only thing standing between the caller and a false 'complete'."""
        records = {
            f"skill-{number}": _record(number)
            for number in range(server.SEARCH_LIMIT + 1)
        }
        gone = {f"skill-{server.SEARCH_LIMIT}"}

        with patch.object(server, "_index", return_value=records), patch.object(
            server, "_read_skill", side_effect=self._reader(gone)
        ):
            response = server.search_skills("searchable phrase")

        self.assertEqual(response["returned"], server.SEARCH_LIMIT)
        self.assertFalse(response["truncated"])
        self.assertEqual(response["unreadable_skipped"], 1)
        self.assertIn("may be incomplete", response["next_action"])


if __name__ == "__main__":
    unittest.main()
