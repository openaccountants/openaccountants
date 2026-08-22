from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
import urllib.parse
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check-sync-integrity.py"
sys.path.insert(0, str(SCRIPT_PATH.parent))
SPEC = importlib.util.spec_from_file_location("check_sync_integrity", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
sync_integrity = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = sync_integrity
SPEC.loader.exec_module(sync_integrity)

WORKBOOK_SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "build-verification-workbook.py"
)
WORKBOOK_SPEC = importlib.util.spec_from_file_location(
    "build_verification_workbook", WORKBOOK_SCRIPT_PATH
)
assert WORKBOOK_SPEC is not None and WORKBOOK_SPEC.loader is not None
build_workbook = importlib.util.module_from_spec(WORKBOOK_SPEC)
sys.modules[WORKBOOK_SPEC.name] = build_workbook
WORKBOOK_SPEC.loader.exec_module(build_workbook)


def guide(
    *,
    last_updated: str = "2026-08-06",
    version: str | None = "1.1",
    heading_version: str | None = "1.1",
    body: str = "Reliable body.",
) -> str:
    version_line = f"version: {version}\n" if version is not None else ""
    heading = (
        f"## Synthetic guide v{heading_version}\n\n"
        if heading_version is not None
        else "## Synthetic guide\n\n"
    )
    return (
        "---\n"
        "name: synthetic-guide\n"
        "description: Synthetic guide used only by the sync-integrity test suite.\n"
        "jurisdiction: GLOBAL\n"
        "category: foundation\n"
        "tax_year: 2026\n"
        "tier: 2\n"
        f"last_updated: {last_updated}\n"
        f"{version_line}"
        "---\n\n"
        "# Synthetic guide\n\n"
        f"{heading}"
        f"{body}\n"
    )


def codes(findings: list[object], severity: str | None = None) -> set[str]:
    return {
        finding.code
        for finding in findings
        if severity is None or finding.severity == severity
    }


class GuideComparisonTests(unittest.TestCase):
    path = "skills/foundation/synthetic-guide.md"

    def compare(self, before: str, after: str, mode: str = "audit"):
        return sync_integrity.compare_existing_guides(self.path, before, after, mode)

    def test_last_updated_regression_fails(self) -> None:
        findings = self.compare(
            guide(last_updated="2026-08-06"),
            guide(last_updated="2026-07-13", body="Stale body."),
        )
        self.assertIn("date-regression", codes(findings, "error"))

    def test_numeric_version_regression_fails_even_with_newer_date(self) -> None:
        findings = self.compare(
            guide(last_updated="2026-08-06", version="1.2", heading_version="1.2"),
            guide(
                last_updated="2026-08-07",
                version="1.1",
                heading_version="1.1",
                body="Changed body.",
            ),
        )
        self.assertIn("version-regression", codes(findings, "error"))

    def test_incident_shape_detects_heading_split_and_uncertainty(self) -> None:
        findings = self.compare(
            guide(body="W5 = W2 + W3 + W4."),
            guide(
                last_updated="2026-07-13",
                version="1.1",
                heading_version="1.0",
                body="W5 = W2 + W4. _(unsure)_",
            ),
        )
        self.assertTrue(
            {
                "date-regression",
                "heading-version-regression",
                "version-mismatch",
            }.issubset(codes(findings, "error"))
        )
        self.assertIn("uncertainty-increase", codes(findings, "warning"))

    def test_forward_dated_and_versioned_edit_passes(self) -> None:
        findings = self.compare(
            guide(),
            guide(
                last_updated="2026-08-07",
                version="1.2",
                heading_version="1.2",
                body="Improved body.",
            ),
        )
        self.assertEqual([], findings)

    def test_same_day_unversioned_edit_warns_in_audit_mode(self) -> None:
        findings = self.compare(guide(), guide(body="Same-day edit."), mode="audit")
        self.assertIn("unversioned-body-change", codes(findings, "warning"))
        self.assertNotIn("unversioned-body-change", codes(findings, "error"))

    def test_same_day_unversioned_edit_fails_in_strict_audit(self) -> None:
        findings = sync_integrity.compare_existing_guides(
            self.path,
            guide(),
            guide(body="Unversioned main-branch rewrite."),
            "audit",
            strict_metadata=True,
        )
        self.assertIn("unversioned-body-change", codes(findings, "error"))

    def test_same_day_unversioned_edit_fails_in_sync_mode(self) -> None:
        findings = self.compare(guide(), guide(body="Same-day export."), mode="sync")
        self.assertIn("unversioned-body-change", codes(findings, "error"))

    def test_line_endings_and_trailing_whitespace_are_ignored(self) -> None:
        before = guide(body="First line.\nSecond line.")
        after = before.replace("First line.", "First line.   ").replace("\n", "\r\n")
        self.assertEqual([], self.compare(before, after))

    def test_frontmatter_key_reordering_only_passes(self) -> None:
        before = guide()
        after = before.replace(
            "jurisdiction: GLOBAL\ncategory: foundation\n",
            "category: foundation\njurisdiction: GLOBAL\n",
        )
        self.assertEqual([], self.compare(before, after))

    def test_optional_missing_version_does_not_crash(self) -> None:
        findings = self.compare(
            guide(version=None, heading_version=None),
            guide(
                last_updated="2026-08-07",
                version=None,
                heading_version=None,
                body="Updated body.",
            ),
        )
        self.assertEqual([], findings)

    def test_invalid_yaml_fails_before_metadata_comparison(self) -> None:
        malformed = guide().replace(
            "category: foundation\n",
            "category: foundation\ndepends_on: - workflow-base\n",
        )
        findings = self.compare(guide(), malformed)
        self.assertIn("invalid-candidate", codes(findings, "error"))

    def test_invalid_legacy_base_can_be_repaired(self) -> None:
        malformed = guide().replace(
            "category: foundation\n",
            "category: foundation\ndepends_on: - workflow-base\n",
        )
        repaired = guide().replace(
            "category: foundation\n",
            "category: foundation\ndepends_on:\n  - workflow-base\n",
        )
        findings = self.compare(malformed, repaired)
        self.assertEqual(set(), codes(findings, "error"))
        self.assertIn("frontmatter-repaired", codes(findings, "notice"))

    def test_yaml_boolean_jurisdiction_fails_closed(self) -> None:
        malformed = guide().replace("jurisdiction: GLOBAL", "jurisdiction: NO")
        findings = self.compare(guide(), malformed)
        self.assertIn("invalid-candidate", codes(findings, "error"))

    def test_existing_version_cannot_be_removed(self) -> None:
        findings = self.compare(
            guide(),
            guide(
                last_updated="2026-08-07",
                version=None,
                heading_version=None,
                body="Updated body.",
            ),
        )
        self.assertIn("version-removed", codes(findings, "error"))

    def test_non_numeric_version_warns_but_uses_date_guard(self) -> None:
        findings = self.compare(
            guide(version="release-one", heading_version=None),
            guide(
                last_updated="2026-08-07",
                version="release-two",
                heading_version=None,
                body="Updated body.",
            ),
        )
        self.assertEqual(set(), codes(findings, "error"))
        self.assertIn("version-unordered", codes(findings, "warning"))

    def test_numeric_version_cannot_become_non_numeric(self) -> None:
        findings = self.compare(
            guide(version="2.0", heading_version="2.0"),
            guide(
                last_updated="2026-08-07",
                version="release-two",
                heading_version=None,
                body="Updated body.",
            ),
            mode="sync",
        )
        self.assertIn("version-became-unordered", codes(findings, "error"))

    def test_new_guide_heading_must_match_frontmatter_version(self) -> None:
        findings = sync_integrity.validate_new_guide(
            self.path,
            guide(version="2.0", heading_version="1.0"),
        )
        self.assertIn("version-mismatch", codes(findings, "error"))

    def test_new_guide_version_must_be_numeric_when_present(self) -> None:
        findings = sync_integrity.validate_new_guide(
            self.path,
            guide(version="release-one", heading_version=None),
        )
        self.assertIn("version-unordered", codes(findings, "error"))


class GitBackedIntegrityTests(unittest.TestCase):
    path = "skills/foundation/synthetic-guide.md"

    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.repo = Path(self.tempdir.name)
        self.git("init", "--initial-branch=main")
        self.git("config", "user.name", "Synthetic Accountant")
        self.git("config", "user.email", "accountant@example.test")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "commit.gpgsign", "false")
        candidate = self.repo / self.path
        candidate.parent.mkdir(parents=True)
        candidate.write_text(guide(), encoding="utf-8", newline="\n")
        self.git("add", self.path)
        self.git("commit", "-m", "add synthetic guide")
        self.base = self.git("rev-parse", "HEAD").strip()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def git(self, *args: str) -> str:
        result = subprocess.run(
            ["git", *args],
            cwd=self.repo,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout

    def write_candidate(self, content: str) -> None:
        (self.repo / self.path).write_text(content, encoding="utf-8", newline="\n")

    def test_matching_blob_provenance_allows_forward_render(self) -> None:
        self.write_candidate(
            guide(
                last_updated="2026-08-07",
                version="1.2",
                heading_version="1.2",
                body="Platform edit attributed to an accountant.",
            )
        )
        expected_blob = sync_integrity.revision_blob(self.repo, self.base, self.path)
        provenance = {
            self.path: {"expected_repo_blob": expected_blob, "content_revision": 2}
        }
        findings, count = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "sync", provenance
        )
        self.assertEqual(1, count)
        self.assertEqual(set(), codes(findings, "error"))

    def test_stale_blob_provenance_fails_closed(self) -> None:
        self.write_candidate(
            guide(
                last_updated="2026-08-07",
                version="1.2",
                heading_version="1.2",
                body="Conflicting platform edit.",
            )
        )
        provenance = {
            self.path: {"expected_repo_blob": "0" * 40, "content_revision": 2}
        }
        findings, _ = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "sync", provenance
        )
        self.assertIn("cas-conflict", codes(findings, "error"))

    def test_sync_preflight_rejects_malformed_yaml_before_publication(self) -> None:
        malformed = guide(
            last_updated="2026-08-07",
            version="1.2",
            heading_version="1.2",
            body="Platform edit with malformed metadata.",
        ).replace(
            "category: foundation\n",
            "category: foundation\ndepends_on: - workflow-base\n",
        )
        self.write_candidate(malformed)
        expected_blob = sync_integrity.revision_blob(self.repo, self.base, self.path)
        provenance = {
            self.path: {"expected_repo_blob": expected_blob, "content_revision": 2}
        }

        findings, count = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "sync", provenance
        )

        self.assertEqual(1, count)
        self.assertIn("invalid-candidate", codes(findings, "error"))

    def test_missing_provenance_fails_closed(self) -> None:
        self.write_candidate(
            guide(
                last_updated="2026-08-07",
                version="1.2",
                heading_version="1.2",
                body="Unprovenanced platform edit.",
            )
        )
        findings, _ = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "sync", {}
        )
        self.assertIn("missing-provenance", codes(findings, "error"))

    def test_new_guide_requires_null_blob_and_valid_revision(self) -> None:
        new_path = "skills/foundation/new-synthetic-guide.md"
        candidate = self.repo / new_path
        candidate.write_text(
            guide(
                last_updated="2026-08-07",
                version="1.0",
                heading_version="1.0",
                body="New guide.",
            ),
            encoding="utf-8",
            newline="\n",
        )
        provenance = {
            new_path: {"expected_repo_blob": None, "content_revision": 1}
        }
        findings, count = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "sync", provenance
        )
        self.assertEqual(1, count)
        self.assertEqual(set(), codes(findings, "error"))

    def test_invalid_content_revision_fails(self) -> None:
        self.write_candidate(
            guide(
                last_updated="2026-08-07",
                version="1.2",
                heading_version="1.2",
                body="Platform edit.",
            )
        )
        expected_blob = sync_integrity.revision_blob(self.repo, self.base, self.path)
        provenance = {
            self.path: {"expected_repo_blob": expected_blob, "content_revision": "2"}
        }
        findings, _ = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "sync", provenance
        )
        self.assertIn("invalid-content-revision", codes(findings, "error"))

    def test_no_op_provenance_always_validates_content_revision(self) -> None:
        expected_blob = sync_integrity.revision_blob(self.repo, self.base, self.path)
        for invalid in (None, "2", True, -1):
            with self.subTest(content_revision=invalid):
                entry = {"expected_repo_blob": expected_blob}
                if invalid is not None:
                    entry["content_revision"] = invalid
                findings, count = sync_integrity.run_integrity_check(
                    self.repo,
                    self.base,
                    None,
                    "sync",
                    {self.path: entry},
                )
                self.assertEqual(0, count)
                self.assertIn("invalid-content-revision", codes(findings, "error"))

    def test_idempotent_no_op_can_repair_stale_sync_state(self) -> None:
        provenance = {
            self.path: {"expected_repo_blob": "0" * 40, "content_revision": 2}
        }
        findings, count = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "sync", provenance
        )
        self.assertEqual(0, count)
        self.assertEqual(set(), codes(findings, "error"))
        self.assertIn("idempotent-state-repair", codes(findings, "notice"))

    def test_idempotent_repair_hashes_filtered_crlf_blob(self) -> None:
        self.git("config", "core.autocrlf", "true")
        candidate = self.repo / self.path
        content = candidate.read_text(encoding="utf-8")
        candidate.write_bytes(content.replace("\n", "\r\n").encode("utf-8"))
        provenance = {
            self.path: {"expected_repo_blob": "0" * 40, "content_revision": 2}
        }
        findings, count = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "sync", provenance
        )
        self.assertEqual(0, count)
        self.assertEqual(set(), codes(findings, "error"))
        self.assertIn("idempotent-state-repair", codes(findings, "notice"))

    def test_aggregate_bot_cannot_rewrite_existing_source(self) -> None:
        self.git("config", "user.name", "openaccountants-sync[bot]")
        self.git("config", "user.email", "sync@openaccountants.com")
        self.write_candidate(
            guide(
                last_updated="2026-07-13",
                version="1.1",
                heading_version="1.0",
                body="Stale body. _(unsure)_",
            )
        )
        self.git("add", self.path)
        self.git("commit", "-m", "stale aggregate export")
        head = self.git("rev-parse", "HEAD").strip()

        findings, count = sync_integrity.run_integrity_check(
            self.repo, self.base, head, "audit"
        )
        self.assertEqual(1, count)
        self.assertIn("aggregate-bot-source-write", codes(findings, "error"))
        self.assertIn("date-regression", codes(findings, "error"))

    def test_human_authored_unversioned_main_rewrite_fails_strict_audit(self) -> None:
        self.write_candidate(guide(body="Unversioned main rewrite."))
        self.git("add", self.path)
        self.git("commit", "-m", "rewrite without metadata")
        head = self.git("rev-parse", "HEAD").strip()

        findings, count = sync_integrity.run_integrity_check(
            self.repo,
            self.base,
            head,
            "audit",
            strict_metadata=True,
        )
        self.assertEqual(1, count)
        self.assertIn("unversioned-body-change", codes(findings, "error"))

    def test_non_guide_markdown_edit_is_ignored(self) -> None:
        readme_path = "skills/foundation/README.md"
        candidate = self.repo / readme_path
        candidate.write_text("# Foundation docs\n", encoding="utf-8", newline="\n")
        self.git("add", readme_path)
        self.git("commit", "-m", "add foundation docs")
        docs_base = self.git("rev-parse", "HEAD").strip()
        self.git("config", "user.name", "openaccountants-sync[bot]")
        self.git("config", "user.email", "sync@openaccountants.com")
        candidate.write_text(
            "# Foundation docs\n\nMore explanation.\n",
            encoding="utf-8",
            newline="\n",
        )
        self.git("add", readme_path)
        self.git("commit", "-m", "clarify foundation docs")
        head = self.git("rev-parse", "HEAD").strip()

        findings, count = sync_integrity.run_integrity_check(
            self.repo, docs_base, head, "audit", strict_metadata=True
        )
        self.assertEqual(0, count)
        self.assertEqual([], findings)

    def test_source_deletion_requires_human_review(self) -> None:
        (self.repo / self.path).unlink()
        findings, count = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "audit"
        )
        self.assertEqual(1, count)
        self.assertIn("source-removal-needs-review", codes(findings, "warning"))

        strict_findings, _ = sync_integrity.run_integrity_check(
            self.repo, self.base, None, "audit", strict_metadata=True
        )
        self.assertIn("source-removal-needs-review", codes(strict_findings, "error"))

    def test_source_rename_fails_strict_main_audit(self) -> None:
        renamed = "skills/foundation/renamed-synthetic-guide.md"
        self.git("mv", self.path, renamed)
        findings, count = sync_integrity.run_integrity_check(
            self.repo,
            self.base,
            None,
            "audit",
            strict_metadata=True,
        )
        self.assertEqual(1, count)
        self.assertIn("source-removal-needs-review", codes(findings, "error"))

    def test_merge_base_excludes_unrelated_main_only_changes(self) -> None:
        self.git("checkout", "-b", "feature")
        self.write_candidate(
            guide(
                last_updated="2026-08-07",
                version="1.2",
                heading_version="1.2",
                body="Feature edit.",
            )
        )
        self.git("add", self.path)
        self.git("commit", "-m", "edit guide on feature")
        feature_head = self.git("rev-parse", "HEAD").strip()

        self.git("checkout", "main")
        main_only_path = self.repo / "skills" / "foundation" / "main-only-guide.md"
        main_only_path.write_text(
            guide(version="1.0", heading_version="1.0", body="Main-only guide."),
            encoding="utf-8",
            newline="\n",
        )
        self.git("add", "skills/foundation/main-only-guide.md")
        self.git("commit", "-m", "add unrelated guide on main")
        current_main = self.git("rev-parse", "HEAD").strip()
        merge_base = self.git("merge-base", current_main, feature_head).strip()

        findings, count = sync_integrity.run_integrity_check(
            self.repo, merge_base, feature_head, "audit"
        )
        self.assertEqual(1, count)
        self.assertEqual(set(), codes(findings, "error"))

    def test_cli_provenance_shape_is_json_serializable(self) -> None:
        expected_blob = sync_integrity.revision_blob(self.repo, self.base, self.path)
        payload = {
            self.path: {"expected_repo_blob": expected_blob, "content_revision": 1}
        }
        self.assertEqual(payload, json.loads(json.dumps(payload)))


class VerificationWorkbookQueryTests(unittest.TestCase):
    base_args = ["--verifier", "Test Verifier", "--output", "test.xlsx"]

    def test_repository_inventory_matches_validated_selector_grammar(self) -> None:
        index_path = Path(__file__).resolve().parents[1] / "index.json"
        guides = json.loads(index_path.read_text(encoding="utf-8"))["guides"]

        for slug in {guide["slug"] for guide in guides}:
            self.assertEqual(slug, build_workbook.validate_skill_slug(slug))
        for jurisdiction in {
            guide["jurisdiction"] for guide in guides if guide.get("jurisdiction")
        }:
            self.assertEqual(
                jurisdiction,
                build_workbook.validate_jurisdiction(jurisdiction),
            )

    def test_valid_selectors_include_grouped_and_multi_part_jurisdictions(self) -> None:
        self.assertEqual(
            ["us-1099-k-and-payment-processors", "ifrs15-revenue"],
            build_workbook.parse_slug_list(
                "us-1099-k-and-payment-processors, ifrs15-revenue"
            ),
        )
        for jurisdiction in ("US-NY-NYC", "EU-27", "EU/EEA/CH/UK", "GLOBAL", "general"):
            self.assertEqual(
                jurisdiction,
                build_workbook.validate_jurisdiction(jurisdiction),
            )

    def test_hostile_or_malformed_slug_components_fail_before_query_build(self) -> None:
        for slug in (
            "valid&select=*",
            "valid#fragment",
            "valid+slug",
            "valid slug",
            'valid"slug',
            "valid,slug",
            "valid/slug",
        ):
            with self.subTest(slug=slug), self.assertRaises(ValueError):
                build_workbook.skills_query_path(slugs=[slug])

        for slug_list in ("", "valid,", ",valid", "valid,,other"):
            with self.subTest(slug_list=slug_list), self.assertRaises(ValueError):
                build_workbook.parse_slug_list(slug_list)

    def test_hostile_jurisdictions_fail_before_query_build(self) -> None:
        for jurisdiction in (
            "US-ND&select=*",
            "US#fragment",
            "US+CA",
            "US CA",
            "US,CA",
            '"US"',
            "General",
        ):
            with self.subTest(jurisdiction=jurisdiction), self.assertRaises(ValueError):
                build_workbook.skills_query_path(jurisdiction=jurisdiction)

    def test_selectors_are_mutually_exclusive_and_required(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            build_workbook.parse_arguments(self.base_args)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            build_workbook.parse_arguments(
                [
                    "--slugs",
                    "ifrs15-revenue",
                    "--jurisdiction",
                    "US-ND",
                    *self.base_args,
                ]
            )

    def test_postgrest_filters_are_percent_encoded_as_single_values(self) -> None:
        path = build_workbook.skills_query_path(
            slugs=["ifrs15-revenue", "us-1099-k-and-payment-processors"]
        )
        self.assertIn("%28%22ifrs15-revenue%22%2C%22us-1099", path)
        query = urllib.parse.parse_qs(urllib.parse.urlsplit(path).query)
        self.assertEqual(
            ['in.("ifrs15-revenue","us-1099-k-and-payment-processors")'],
            query["slug"],
        )
        self.assertEqual(["eq.true"], query["is_published"])
        self.assertEqual([build_workbook.SKILL_COLUMNS], query["select"])

        grouped = build_workbook.skills_query_path(jurisdiction="EU/EEA/CH/UK")
        self.assertIn("EU%2FEEA%2FCH%2FUK", grouped)
        self.assertEqual(
            ["eq.EU/EEA/CH/UK"],
            urllib.parse.parse_qs(urllib.parse.urlsplit(grouped).query)["jurisdiction"],
        )

    def test_database_values_cannot_add_query_parameters(self) -> None:
        path = build_workbook.rest_query_path(
            "skill_versions",
            skill_id="eq.id&select=*#fragment +space",
            is_current="eq.true",
            select="markdown_content,version",
            limit="1",
        )
        query = urllib.parse.parse_qs(urllib.parse.urlsplit(path).query)
        self.assertEqual(
            {
                "skill_id": ["eq.id&select=*#fragment +space"],
                "is_current": ["eq.true"],
                "select": ["markdown_content,version"],
                "limit": ["1"],
            },
            query,
        )
        self.assertIn("%26select%3D%2A%23fragment%20%2Bspace", path)


if __name__ == "__main__":
    unittest.main()
