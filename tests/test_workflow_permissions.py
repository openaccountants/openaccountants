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

    # Security review of PR #1267, item 1 and item 6.

    def _claude_steps(self):
        for name, job in self.doc["jobs"].items():
            for step in job.get("steps", []):
                if step.get("uses", "").startswith(CLAUDE_ACTION):
                    yield name, step

    @staticmethod
    def _tool_list(claude_args: str, flag: str) -> list[str]:
        m = re.search(rf'--{flag}\s+"([^"]*)"', claude_args)
        return [t.strip() for t in m.group(1).split(",")] if m else []

    def test_no_job_that_runs_claude_has_a_shell(self) -> None:
        for name, step in self._claude_steps():
            args = step["with"]["claude_args"]
            allowed = self._tool_list(args, "allowedTools")
            self.assertTrue(allowed, f"job {name!r} has no --allowedTools list")
            self.assertEqual([t for t in allowed if t.startswith("Bash")], [], f"job {name!r} allows Bash")
            self.assertIn("Bash", self._tool_list(args, "disallowedTools"), f"job {name!r} must disallow Bash")

    def test_claude_reads_only_the_checkout_and_the_staged_pr(self) -> None:
        for name, step in self._claude_steps():
            allowed = self._tool_list(step["with"]["claude_args"], "allowedTools")
            for bare in ("Read", "Grep", "Glob", "Edit", "Write"):
                self.assertNotIn(bare, allowed, f"job {name!r} allows {bare} everywhere")
            reads = [t for t in allowed if t.startswith("Read(")]
            self.assertEqual(
                sorted(reads),
                sorted(["Read(/${{ github.workspace }}/**)", "Read(/${{ runner.temp }}/oa-review/**)"]),
                f"job {name!r} reads outside the checkout and the staged PR",
            )
            for tool in allowed:
                if tool.startswith(("Edit(", "Write(")):
                    self.assertRegex(tool, r"/oa-review/tree/(skills|library)/\*\*\)$", f"job {name!r}: {tool}")

    def test_checks_run_before_claude_in_the_review_job(self) -> None:
        steps = self.doc["jobs"]["review"]["steps"]
        names = [s.get("name", s.get("uses", "")) for s in steps]
        checks = names.index("Mechanical checks (main's scripts, PR files as data)")
        claude = next(i for i, s in enumerate(steps) if s.get("uses", "").startswith(CLAUDE_ACTION))
        self.assertLess(checks, claude)
        self.assertIn('"$D/base"', steps[names.index("Stage the PR as data")]["run"])

    # Item 2.

    def test_only_writers_review_comments_share_the_pr_group(self) -> None:
        group = self.doc["concurrency"]["group"]
        self.assertIn("github.event.comment.author_association", group)
        self.assertIn('["OWNER","MEMBER","COLLABORATOR"]', group)
        self.assertTrue(group.rstrip("} ").endswith("github.run_id"), "other comments must fall back to the run id")

    # Item 3.

    def test_caps_fail_closed_and_count_review_and_fix(self) -> None:
        gate = self.doc["jobs"]["gate"]["steps"][0]["run"]
        for job in self.doc["jobs"].values():
            for step in job.get("steps", []):
                self.assertNotRegex(step.get("run", ""), r"for \w+ in \$\(gh ", "a failed API call in a for list is ignored")
        self.assertRegex(gate, r'runs=\$\(gh api [^)]*\)[^\n]*\n?[^\n]*\|\| skip', "listing today's runs must stop the gate on failure")
        self.assertIn('.name == "review" or .name == "fix"', gate)
        self.assertIn("AUTHOR_CAP", gate)
        self.assertIn("Reviewed head: \\`$head_sha\\`", gate)
        self.assertIn("Reviewed head: \\`$HEAD_SHA\\`", self.doc["jobs"]["publish"]["steps"][0]["run"])

    # Item 4.

    def test_gate_is_an_allow_list_and_fails_closed_on_truncated_file_lists(self) -> None:
        gate = self.doc["jobs"]["gate"]["steps"][0]["run"]
        self.assertIn("if grep -vqE '^(skills|library)/' <<<\"$paths\"; then", gate)
        self.assertIn("jq -r .changed_files pr.json", gate)
        self.assertIn('[ "$listed" -lt "$declared" ]', gate)

    def test_fork_fix_branch_is_one_commit_on_main(self) -> None:
        push = self.doc["jobs"]["push-fix"]["steps"][-1]["run"]
        self.assertIn('sha=$(commit "$tree" "$main_sha"', push)
        self.assertIn('base_tree: $base', push)
        self.assertNotIn('refs/heads/$branch" -f sha="$HEAD_SHA"', push)

    def test_only_push_fix_can_write_contents(self) -> None:
        writers = [n for n, j in self.doc["jobs"].items() if (j.get("permissions") or {}).get("contents") == "write"]
        self.assertEqual(writers, ["push-fix"])

    def test_oauth_secret_reaches_only_the_gate_check_and_claude(self) -> None:
        for name, job in self.doc["jobs"].items():
            for step in job.get("steps", []):
                if "CLAUDE_CODE_OAUTH_TOKEN" not in str(step):
                    continue
                if step.get("uses", "").startswith(CLAUDE_ACTION):
                    continue
                self.assertEqual(name, "gate")
                self.assertEqual(step["env"]["HAS_TOKEN"], "${{ secrets.CLAUDE_CODE_OAUTH_TOKEN != '' }}")

    # Item 5 and item 9: the frontmatter guard in push-fix, run on real cases.

    def _guard(self):
        push = self.doc["jobs"]["push-fix"]["steps"][-1]["run"]
        m = re.search(r"<<'PY'\n(.*?)\nPY\n", push, re.S)
        self.assertIsNotNone(m, "guard.py heredoc not found in push-fix")
        namespace: dict = {"__name__": "guard"}
        exec(compile(m.group(1), "guard.py", "exec"), namespace)  # noqa: S102 - our own workflow text
        return namespace["check"]

    def test_frontmatter_guard(self) -> None:
        check = self._guard()

        def skill(fm: str, body: str = "rate 19%", nl: str = "\n") -> str:
            return nl.join(["---", *fm.strip().splitlines(), "---", body, ""])

        open_fm = "name: x\njurisdiction: DE\ntier: 2"
        before = skill(open_fm)
        self.assertIsNone(check("skills/germany/x.md", before, skill(open_fm, "rate 21%")))
        self.assertIsNone(check("library/germany/figures.json", "{}", '{"a": 1}'))
        refused = {
            "Malta by jurisdiction": (skill("name: x\njurisdiction: MT\ntier: 2"), ""),
            "Malta region, lower case": (skill("name: x\njurisdiction: mt-gozo\ntier: 2"), ""),
            "Australia state, quoted key": (skill('name: x\n"jurisdiction": "AU-NSW"\ntier: 2'), ""),
            "Malta only on main": (before, skill("name: x\njurisdiction: MT\ntier: 2")),
            "reviewed_by": (skill("name: x\njurisdiction: DE\ntier: 2\nreviewed_by: Jane Doe"), ""),
            "quoted reviewed_by": (skill("name: x\njurisdiction: DE\n'reviewed_by': Jane Doe"), ""),
            "tier 1 as a string": (skill('name: x\njurisdiction: DE\ntier: "1"'), ""),
            "CRLF frontmatter": (skill("name: x\njurisdiction: DE\nreviewed_by: Jane", nl="\r\n"), ""),
        }
        for label, (pr_head, main) in refused.items():
            after = pr_head.replace("19%", "21%")
            self.assertIsNotNone(check("skills/x/x.md", pr_head, after, main), label)
        changes = {
            "tier": "name: x\njurisdiction: DE\ntier: 3",
            "jurisdiction": "name: x\njurisdiction: FR\ntier: 2",
            "license": open_fm + "\nlicense: MIT",
            "approved_by": open_fm + "\napproved_by: Someone",
            "reviewed_on": open_fm + "\nreviewed_on: 2026-11-06",
        }
        for key, fm in changes.items():
            self.assertIsNotNone(check("skills/germany/x.md", before, skill(fm)), f"changing {key}")
        self.assertIsNotNone(check("skills/germany/x.md", before, "---\nname: [unclosed\n---\n"), "unparseable")
        self.assertIsNone(check("skills/austria/x.md", skill("name: x\njurisdiction: AT\ntier: 2"),
                                skill("name: x\njurisdiction: AT\ntier: 2", "rate 21%")), "AT is not AU")


if __name__ == "__main__":
    unittest.main()
