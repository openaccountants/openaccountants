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

    def test_no_comment_shares_the_pr_group(self) -> None:
        """Re-review item 6: every issue_comment run keys on its run id, so no
        comment, /review included, can cancel a review in flight."""
        group = self.doc["concurrency"]["group"]
        self.assertEqual(
            group,
            "skill-review-${{ github.event.pull_request.number || github.event.inputs.pr || github.run_id }}",
        )

    # Item 3.

    def test_caps_fail_closed_and_count_review_and_fix(self) -> None:
        gate = self.doc["jobs"]["gate"]["steps"][0]["run"]
        for job in self.doc["jobs"].values():
            for step in job.get("steps", []):
                self.assertNotRegex(step.get("run", ""), r"for \w+ in \$\(gh ", "a failed API call in a for list is ignored")
        self.assertIn('prt=$(list_runs pull_request_target) || skip', gate)
        self.assertIn('wd=$(list_runs workflow_dispatch) || skip', gate)
        self.assertIn('.name == "review" or .name == "fix"', gate)

    def test_caps_cannot_be_raced_or_spammed(self) -> None:
        """Re-review items 2 and 7: only earlier runs count, an undecided gate
        counts as one, and only pull_request_target and workflow_dispatch runs
        are listed."""
        gate = self.doc["jobs"]["gate"]["steps"][0]["run"]
        self.assertIn('-f event="$1"', gate)
        self.assertIn("NF == 3 && $1 + 0 < me + 0", gate)
        self.assertIn("if $decided == 0 and $n == 0 then 1 else $n end", gate)

    # Final review: the gate's API use is bounded, and maintainers are exempt.
    # These run the gate's real caps block in bash against a fake `gh` that
    # serves the run listings and counts every call.

    _FAKE_GH = """#!/usr/bin/env bash
    echo "$*" >> "$GH_LOG"
    case "$*" in
      *skill-review.yml/runs*event=pull_request_target*) cat "$PRT_FILE" ;;
      *skill-review.yml/runs*event=workflow_dispatch*) cat "$WD_FILE" ;;
      */jobs*) echo "${JOB_N:-1}" ;;
      *collaborators*) echo "${PERM:-none}" ;;
      *) echo "unexpected gh call: $*" >&2; exit 1 ;;
    esac
    """

    def _run_caps(self, event: str, trigger: str, prt: list[tuple[int, str]], wd=(), job_n: int = 1):
        import os
        import shutil
        import subprocess
        import tempfile
        import textwrap

        bash = shutil.which("bash")
        if not bash:
            self.skipTest("bash not available")
        gate = self.doc["jobs"]["gate"]["steps"][0]["run"]
        helpers = gate[: gate.index("# Explain a skip")]
        caps = gate[gate.index("# Caps (pull_request_target runs only)"):]
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            gh = tmp / "gh"
            gh.write_text(textwrap.dedent(self._FAKE_GH), encoding="utf-8")
            gh.chmod(0o755)
            (tmp / "prt").write_text("".join(f"{i} pull_request_target {a}\n" for i, a in prt), encoding="utf-8")
            (tmp / "wd").write_text("".join(f"{i} workflow_dispatch {a}\n" for i, a in wd), encoding="utf-8")
            (tmp / "log").write_text("", encoding="utf-8")
            (tmp / "out").write_text("", encoding="utf-8")
            env = dict(os.environ, PATH=f"{tmp}:{os.environ.get('PATH', '')}", GH_LOG=str(tmp / "log"),
                       PRT_FILE=str(tmp / "prt"), WD_FILE=str(tmp / "wd"), JOB_N=str(job_n),
                       GITHUB_OUTPUT=str(tmp / "out"), GITHUB_STEP_SUMMARY=str(tmp / "summary"), EVENT=event, TRIGGER=trigger, RUN_ID="100000",
                       REPO="o/r", **{k: str(v) for k, v in self.doc["env"].items()})
            proc = subprocess.run([bash, "-c", helpers + caps], env=env, capture_output=True, text=True, timeout=60)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            calls = (tmp / "log").read_text(encoding="utf-8").splitlines()
            out = (tmp / "out").read_text(encoding="utf-8")
        return calls, out, proc.stdout

    @staticmethod
    def _jobs_calls(calls: list[str]) -> int:
        return sum("/jobs" in c for c in calls)

    def test_over_cap_author_is_stopped_from_the_listing_alone(self) -> None:
        spam = [(i, "spammer") for i in range(1, 1001)]
        calls, out, _ = self._run_caps("pull_request_target", "spammer", spam)
        self.assertIn("run=false", out)
        self.assertEqual(self._jobs_calls(calls), 0, "no per-run lookup before the per-author cap")
        self.assertLessEqual(len(calls), 3, calls)

    def test_spam_runs_cost_another_author_a_bounded_number_of_lookups(self) -> None:
        spam = [(i, "spammer") for i in range(1, 1001)]
        calls, out, _ = self._run_caps("pull_request_target", "alice", spam, job_n=0)
        self.assertIn("run=true", out)
        self.assertEqual(self._jobs_calls(calls), int(self.doc["env"]["AUTHOR_CAP"]))

    def test_global_count_stops_at_the_cap(self) -> None:
        runs = [(i, f"user{i}") for i in range(1, 61)]
        calls, out, _ = self._run_caps("pull_request_target", "alice", runs, job_n=1)
        self.assertIn("run=false", out)
        self.assertEqual(self._jobs_calls(calls), int(self.doc["env"]["DAILY_CAP"]))

    def test_lookups_never_exceed_the_ceiling(self) -> None:
        runs = [(i, f"user{i}") for i in range(1, 201)]
        calls, out, _ = self._run_caps("pull_request_target", "alice", runs, job_n=0)
        self.assertIn("run=false", out, "too many runs to count fails closed")
        self.assertEqual(self._jobs_calls(calls), int(self.doc["env"]["MAX_LOOKUPS"]))

    def test_only_earlier_runs_count(self) -> None:
        later = [(200000 + i, "alice") for i in range(10)]
        calls, out, _ = self._run_caps("pull_request_target", "alice", later)
        self.assertIn("run=true", out)
        self.assertEqual(self._jobs_calls(calls), 0)

    def test_maintainer_runs_are_exempt_from_the_caps(self) -> None:
        busy = [(i, f"user{i}") for i in range(1, 61)]
        for event in ("issue_comment", "workflow_dispatch"):
            calls, out, _ = self._run_caps(event, "michael", busy)
            self.assertIn("run=true", out, event)
            self.assertEqual(calls, [], f"{event}: the caps make no API calls")

    def test_reviewed_head_marker_is_the_shell_footer_only(self) -> None:
        """Re-review item 4: the marker is the comment's last line, written by
        shell; the model's text is defused; a skip on an older verdict says so."""
        publish = self.doc["jobs"]["publish"]["steps"][0]["run"]
        self.assertIn("s/[Rr]eviewed[[:space:]]+[Hh]ead/reviewed (quoted) head/g", publish)
        block = publish[publish.index('echo "VERDICT: $verdict"'):publish.index("} > comment.md")]
        self.assertEqual(block.strip().splitlines()[-1].strip(), 'echo "<sub>Reviewed head: \\`$HEAD_SHA\\`</sub>"')
        self.assertLess(publish.index("head -c 60000 body.md"), publish.index("} > comment.md"))
        gate = self.doc["jobs"]["gate"]["steps"][0]["run"]
        self.assertIn('split("\\n") | last', gate)
        self.assertIn('grep -qxF "$marker" markers.txt', gate)
        self.assertIn("was already reviewed earlier on this PR", gate)

    # Item 4.

    def test_gate_is_an_allow_list_and_fails_closed_on_truncated_file_lists(self) -> None:
        gate = self.doc["jobs"]["gate"]["steps"][0]["run"]
        self.assertIn("if grep -vqE '^(skills|library)/' <<<\"$paths\"; then", gate)
        self.assertIn("jq -r .changed_files pr.json", gate)
        self.assertIn('[ "$listed" -lt "$declared" ]', gate)

    def test_fork_path_guards_every_pr_file_before_creating_anything(self) -> None:
        """Re-review item 1: the guard runs over files.tsv (the whole PR) against
        main before any blob, tree, commit or branch, and the fork author is
        the git author of the commit."""
        push = self.doc["jobs"]["push-fix"]["steps"][-1]["run"]
        fork = push[push.index("# Fork PR: never push to the fork"):]
        guard_call = fork.index('guard.py" "$path" "$b" "$a" "$m") || refuse')
        loop_end = fork.index("done < files.tsv")
        self.assertLess(guard_call, loop_end)
        for later in ('s=$(blob "$path")', "git/trees", "git/refs", "gh pr create"):
            self.assertLess(loop_end, fork.index(later), later)
        self.assertIn('"$pr_login" "$pr_id+$pr_login@users.noreply.github.com"', fork)
        self.assertIn('"github-actions[bot]" "41898282+github-actions[bot]@users.noreply.github.com"', fork)
        self.assertNotIn("FIX_AUTHOR", fork)
        self.assertNotIn("Co-authored-by", fork)

    def test_main_is_read_from_git_not_an_api_that_can_fail_open(self) -> None:
        push = self.doc["jobs"]["push-fix"]["steps"][-1]["run"]
        self.assertIn('"+refs/heads/$DEFAULT_BRANCH:refs/oa/main"', push)
        self.assertNotIn("|| : > main.txt", push)
        self.assertIn("grep -q 'HTTP 404'", push)

    def test_fixer_cannot_write_git_metadata(self) -> None:
        """Re-review item 5."""
        stage = self.doc["jobs"]["fix"]["steps"][1]["run"]
        for rule in ('"Write(//**/.git/**)"', '"Write(//**/.gitattributes)"', '"Write(//**/.gitmodules)"',
                     '"Edit(//**/.git/**)"', '"Edit(//**/.gitattributes)"', '"Edit(//**/.gitmodules)"'):
            self.assertIn(rule, stage)
        collect = next(s["run"] for s in self.doc["jobs"]["fix"]["steps"] if s.get("name") == "Collect the edits as a patch")
        self.assertIn('add -u', collect)
        self.assertNotIn("add -A", collect)

    def test_gate_blocks_agent_and_git_config_files(self) -> None:
        gate = self.doc["jobs"]["gate"]["steps"][0]["run"]
        m = re.search(r"if grep -qE '([^']+)' <<<\"\$paths\"; then\n\s*say \"agent or git config file\"", gate)
        self.assertIsNotNone(m)
        blocked = re.compile(m.group(1))
        for path in ("skills/x/.gitattributes", "skills/x/.gitmodules", "skills/x/.git/config",
                     "library/.claude/settings.json", "skills/x/CLAUDE.md", "skills/x/AGENTS.md", "skills/.mcp.json"):
            self.assertTrue(blocked.search(path), path)
        for path in ("skills/germany/de-vat.md", "skills/x/github-notes.md", "library/ireland/figures.json"):
            self.assertIsNone(blocked.search(path), path)

    def test_fork_fix_branch_is_one_commit_on_main(self) -> None:
        push = self.doc["jobs"]["push-fix"]["steps"][-1]["run"]
        self.assertIn('sha=$(commit "$tree" "$main_sha" "$RUNNER_TEMP/forkmsg.txt"', push)
        self.assertIn('base_tree: $base', push)
        self.assertNotIn('refs/heads/$branch" -f sha="$HEAD_SHA"', push)

    def test_models_never_receive_the_scoped_fix_writer(self) -> None:
        writers = [n for n, j in self.doc["jobs"].items() if (j.get("permissions") or {}).get("contents") == "write"]
        self.assertEqual(writers, [])
        holders = [(name, index) for name, job in self.doc["jobs"].items()
                   for index, step in enumerate(job.get("steps", [])) if "DERIVED_BUILD_TOKEN" in str(step)]
        push = self.doc["jobs"]["push-fix"]
        self.assertEqual(holders, [("push-fix", len(push["steps"]) - 1)])
        self.assertEqual(push["environment"], "production")
        self.assertEqual(push["steps"][-1]["env"]["GH_TOKEN"], "${{ secrets.DERIVED_BUILD_TOKEN }}")
        self.assertIn('if [ -z "$GH_TOKEN" ]', push["steps"][-1]["run"])
        self.assertNotIn("gh workflow run", push["steps"][-1]["run"])
        self.assertFalse(self.doc["concurrency"]["cancel-in-progress"])

    def test_summary_separates_a_skipped_review_from_a_verdict(self) -> None:
        gate = self.doc["jobs"]["gate"]["steps"][0]["run"]
        publish = self.doc["jobs"]["publish"]["steps"][0]["run"]
        self.assertIn("AI review: SKIPPED", gate)
        self.assertIn("GITHUB_STEP_SUMMARY", gate)
        self.assertIn("AI review: $verdict", publish)
        self.assertIn('"$HEAD_SHA"; } >> "$GITHUB_STEP_SUMMARY"', publish)

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

    def test_frontmatter_guard_parsing_gaps(self) -> None:
        """Re-review item 3: BOM, duplicate keys, every file type."""
        check = self._guard()
        open_fm = "---\nname: x\njurisdiction: DE\ntier: 2\n---\nrate 19%\n"
        approved = "---\nname: x\njurisdiction: DE\ntier: 1\nreviewed_by: Jane Doe\n---\nrate 19%\n"
        # A new file reads as {} if the BOM hides its frontmatter, and would pass.
        self.assertIsNotNone(check("skills/germany/new.md", None, "\ufeff" + approved), "BOM before the frontmatter")
        self.assertIsNotNone(check("skills/germany/new.md", None, "\n  " + approved), "blank space before the frontmatter")
        self.assertIsNotNone(check("skills/germany/x.md", "\ufeff" + open_fm, "\ufeff" + approved), "BOM on both")
        dup = "---\nname: x\njurisdiction: DE\ntier: 2\nreviewed_by: Jane\nreviewed_by:\n---\nrate\n"
        self.assertIsNotNone(check("skills/germany/x.md", open_fm, dup), "duplicate key")
        dup_case = "---\nname: x\njurisdiction: DE\ntier: 2\nReviewed_By: Jane\nreviewed_by:\n---\nrate\n"
        self.assertIsNotNone(check("skills/germany/x.md", open_fm, dup_case), "duplicate key in another case")
        for path in ("skills/germany/x.MD", "skills/germany/x.markdown", "skills/germany/x.txt"):
            self.assertIsNotNone(check(path, open_fm, approved), path)

    def test_frontmatter_guard_on_whole_pr_files(self) -> None:
        """Re-review item 1: the cases the fork path sends through the guard."""
        check = self._guard()
        new_ok = "---\nname: x\njurisdiction: DE\ntier: 2\n---\nrate 19%\n"
        self.assertIsNone(check("skills/germany/new.md", None, new_ok, None), "a new tier 2 skill")
        for key, line in (("tier 1", "tier: 1"), ("reviewed_by", "tier: 2\nreviewed_by: Jane"),
                          ("license", "tier: 2\nlicense: MIT"), ("approved_by", "tier: 2\napproved_by: Jane"),
                          ("reviewed_on", "tier: 2\nreviewed_on: 2026-11-06"), ("Malta", "tier: 2\njurisdiction: MT")):
            text = new_ok.replace("tier: 2", line)
            self.assertIsNotNone(check("skills/germany/new.md", None, text, None), f"new file with {key}")
        held_main = "---\nname: x\njurisdiction: DE\ntier: 1\nreviewed_by: Jane\n---\nbody\n"
        self.assertIsNotNone(check("skills/germany/x.md", held_main, None, held_main), "deleting an approved file")
        self.assertIsNone(check("skills/germany/x.md", new_ok, None, new_ok), "deleting an open file")
        for folder in ("skills/malta/x.md", "library/australia/figures.json", "skills/Russia/x.md", "skills/iran/x.md"):
            self.assertIsNotNone(check(folder, new_ok, new_ok, new_ok), folder)
        self.assertIsNotNone(check("skills/germany/x.md", new_ok, new_ok, "---\nname: [x\n---\n"), "main unparseable")


if __name__ == "__main__":
    unittest.main()
