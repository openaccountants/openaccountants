import contextlib
import importlib.util
import io
import os
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location(
    "open_coverage_issues", os.path.join(HERE, "..", "scripts", "open-coverage-issues.py"))
oci = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(oci)


ROW = {
    "code": "XX",
    "dir": "skills/international/example",
    "owner": "michael",
    "region": "europe",
    "skills": 2,
    "reviewed": 0,
    "stale": 0,
    "present": ["IT-IND"],
    "missing": ["IT-CORP", "XB"],
    "not_applicable": {},
}


class CoverageIssueWorkflowTest(unittest.TestCase):
    def test_issue_requires_review_gates_and_one_country_batch(self):
        body = oci.body_for(ROW)
        self.assertIn("source preparation do not establish comprehensive coverage", body)
        self.assertIn("checked the full country pack", body)
        self.assertIn("one country PR, not separate PRs for individual Guides", body)
        self.assertIn("GitHub native auto-merge", body)
        self.assertIn("named accountant", body)

    def test_dry_run_does_not_need_github_issue_state(self):
        output = io.StringIO()
        with mock.patch.object(oci, "report", return_value={"rows": [ROW]}), \
                mock.patch.object(oci, "existing_issues", side_effect=AssertionError("GitHub should not be queried")), \
                contextlib.redirect_stdout(output):
            result = oci.main(["--dry-run"])
        self.assertEqual(result, 0)
        self.assertIn("candidate: [XX] Complete the pack", output.getvalue())
        self.assertIn("issue state was not queried", output.getvalue())


if __name__ == "__main__":
    unittest.main()
