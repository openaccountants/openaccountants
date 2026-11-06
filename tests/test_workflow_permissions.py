"""Regression tests for CI workflow hardening.

Both properties here were live defects:

* `validate.yml` declared no `permissions:` block, so every job inherited the
  repository default token scope.
* The contributor-comment step interpolated `steps.guard.outputs.*` — built from
  filenames in the pull request's own diff — directly into an
  `actions/github-script` body, where a crafted filename would be evaluated as
  JavaScript.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = REPO_ROOT / ".github" / "workflows"
VALIDATE = WORKFLOWS / "validate.yml"


def _load(path: Path) -> dict:
    try:
        import yaml
    except ImportError:  # pragma: no cover - exercised only without PyYAML
        raise unittest.SkipTest("PyYAML not installed") from None
    return yaml.safe_load(path.read_text(encoding="utf-8"))


class WorkflowPermissionTests(unittest.TestCase):
    def test_validate_workflow_declares_least_privilege_default(self) -> None:
        doc = _load(VALIDATE)
        self.assertEqual(
            doc.get("permissions"),
            {"contents": "read"},
            "validate.yml must declare a read-only default token scope",
        )

    def test_only_the_commenting_job_can_write(self) -> None:
        doc = _load(VALIDATE)
        for name, job in doc["jobs"].items():
            perms = job.get("permissions")
            if name == "guard-derived-trees":
                self.assertEqual(perms, {"contents": "read", "issues": "write"})
            else:
                self.assertIsNone(
                    perms,
                    f"job {name!r} should inherit the read-only default, got {perms!r}",
                )

    def test_no_workflow_interpolates_untrusted_input_into_a_script_body(self) -> None:
        """`script:` blocks must read from env, never from ${{ ... }} directly."""
        offenders: list[str] = []
        for wf in sorted(WORKFLOWS.glob("*.yml")):
            lines = wf.read_text(encoding="utf-8").splitlines()
            in_script = False
            indent = 0
            for lineno, line in enumerate(lines, 1):
                stripped = line.strip()
                if re.match(r"^script:\s*[|>]", stripped):
                    in_script = True
                    indent = len(line) - len(line.lstrip())
                    continue
                if in_script:
                    if stripped and (len(line) - len(line.lstrip())) <= indent:
                        in_script = False
                    elif "${{" in line:
                        offenders.append(f"{wf.name}:{lineno}: {stripped}")
        self.assertEqual(
            offenders,
            [],
            "pass values through `env:` instead of interpolating them into `script:`:\n"
            + "\n".join(offenders),
        )


SKILL_REVIEW = WORKFLOWS / "skill-review.yml"
CLAUDE_ACTION = "anthropics/claude-code-action@"


class SkillReviewWorkflowTests(unittest.TestCase):
    """skill-review.yml runs Claude on untrusted PRs with this repo's secrets.

    These pin the properties docs/AUTOMATED-REVIEW.md promises: Claude never
    holds a write token, PR code is never checked out, every action is pinned,
    and no workflow value is spliced into a shell script.
    """

    def setUp(self) -> None:
        self.doc = _load(SKILL_REVIEW)
        self.text = SKILL_REVIEW.read_text(encoding="utf-8")

    def test_no_default_permissions(self) -> None:
        self.assertEqual(self.doc.get("permissions"), {})

    def test_jobs_that_run_claude_cannot_write(self) -> None:
        claude_jobs = 0
        for name, job in self.doc["jobs"].items():
            uses = [step.get("uses", "") for step in job.get("steps", [])]
            if not any(u.startswith(CLAUDE_ACTION) for u in uses):
                continue
            claude_jobs += 1
            perms = job.get("permissions") or {}
            writes = {k: v for k, v in perms.items() if v != "read"}
            self.assertEqual(writes, {}, f"job {name!r} runs Claude with write access: {writes}")
        self.assertEqual(claude_jobs, 2, "expected the review and fix jobs to run Claude")

    def test_every_action_is_pinned_to_a_commit(self) -> None:
        for line in self.text.splitlines():
            m = re.search(r"uses:\s*([^\s#]+)", line)
            if m:
                self.assertRegex(m.group(1), r"@[0-9a-f]{40}$", f"not pinned by SHA: {line.strip()}")

    def test_never_checks_out_the_pr_head(self) -> None:
        for name, job in self.doc["jobs"].items():
            for step in job.get("steps", []):
                if step.get("uses", "").startswith("actions/checkout@"):
                    ref = str((step.get("with") or {}).get("ref", ""))
                    self.assertNotIn("head", ref, f"job {name!r} checks out {ref!r}")

    def test_run_blocks_take_values_from_env_only(self) -> None:
        for name, job in self.doc["jobs"].items():
            for step in job.get("steps", []):
                self.assertNotIn(
                    "${{",
                    step.get("run", ""),
                    f"job {name!r}: pass values through env, not ${{{{ }}}} in run",
                )


if __name__ == "__main__":
    unittest.main()
