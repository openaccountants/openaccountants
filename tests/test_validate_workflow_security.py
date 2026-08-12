from __future__ import annotations

import unittest
from pathlib import Path


WORKFLOW = (
    Path(__file__).resolve().parents[1] / ".github" / "workflows" / "validate.yml"
)


class ValidateWorkflowSecurityTests(unittest.TestCase):
    def test_comment_uses_the_minimum_issue_permission(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")

        self.assertIn("      issues: write\n", workflow)
        self.assertNotIn("      pull-requests: write\n", workflow)

    def test_filenames_reach_javascript_through_the_environment(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")

        self.assertIn(
            "GENERATED_FILES_TOUCHED: "
            "${{ steps.guard.outputs.generated_files_touched }}",
            workflow,
        )
        self.assertIn("process.env.GENERATED_FILES_TOUCHED.trim()", workflow)
        self.assertNotIn(
            "`${{ steps.guard.outputs.generated_files_touched }}`",
            workflow,
        )


if __name__ == "__main__":
    unittest.main()
