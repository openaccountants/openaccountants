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
        raise unittest.SkipTest("PyYAML not installed")
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


if __name__ == "__main__":
    unittest.main()
