# Automated review of skill PRs

A GitHub workflow can review eligible PRs that change `skills/**` or `library/**`, posts one verdict comment, and can fix what it found, up to two rounds. It is line 12 of [skill-template.md](skill-template.md) (an independent second reader), run by Claude through the official [Claude Code GitHub Action](https://github.com/anthropics/claude-code-action) on the founder's Claude subscription. It never approves and never merges: a maintainer still does.

- Workflow: [`.github/workflows/skill-review.yml`](../.github/workflows/skill-review.yml) (its header explains each security choice).
- Playbooks Claude follows, read from main: [`.claude/agents/skill-reviewer.md`](../.claude/agents/skill-reviewer.md) and [`.claude/agents/skill-fixer.md`](../.claude/agents/skill-fixer.md).

## What runs, and when

1. **Gate** (no AI). Runs when a skill PR is opened, reopened, marked ready or pushed to; when someone with write access comments `/review`; or when the workflow is run by hand. It skips drafts, closed PRs and PRs not aimed at `main`. It reviews a PR only if **every** file it changes is under `skills/` or `library/` (an allow-list); anything else stays human-only, and so does a PR with more files than GitHub can list. Limits, all of which fail closed (if GitHub cannot be read, nothing runs):
   - 25 review and fix runs a day in total (UTC);
   - 5 runs a day per person without write access;
   - one automatic review per commit (reopening a PR does not buy another; `/review` and a manual run can);
   - each run counts only the runs started before it, so a burst of PRs cannot all slip under a limit at once;
   - a `/review` comment from someone without write access starts nothing, and no comment ever cancels a review;
   - runs a maintainer starts (`/review` with write access, or a manual run) skip the daily and per-person limits, so a maintainer can always override; they still run one at a time per PR and stop after two fix rounds;
   - counting costs the bot a fixed, small number of GitHub calls per run however many PRs a spammer opens; if it cannot count within that budget, it stops.
2. **Review** (Claude, read-only, no shell). Main's scripts run first, in plain shell, and their output is staged as files with the PR's files and main's version of each. Claude then checks every figure against official sources, including checking any writer-supplied quotes, content lost against main (the 25% rule), all prose worked examples, honest labels, scope (sanctioned countries; Malta and Australia are comment-only) and duplicates. It asks only for objective fixes: a wrong figure, a missing or unofficial or undated source, arithmetic, lost content, a stale tax year, a missing core item. Style and layout are optional notes, never fixes.
   The verdict judges only what the PR changes (its added, changed and removed lines and what they directly feed). Faults in lines the PR does not touch go under "Found on main (not caused by this PR)" and never change the verdict.
   The reviewer reports figures found versus checked and examples found versus checked per file. It must return HOLD if coverage is incomplete. A green workflow or a MERGE verdict does not establish professional approval; that still belongs to the one accountant for the skill. Mixed-file PRs, skips and exhausted limits need the same complete independent source-review record outside this workflow.
3. **Publish** (no AI). Posts the comment, starting `VERDICT: MERGE`, `FIX` or `HOLD`, with a figures table and, for FIX, a numbered list of exact changes. Each file listed under "Found on main" gets one open issue, "Found by review: <path>", labelled `found-by-review`: a new issue the first time, a comment on the same issue after that.
4. **Fix** (Claude, only on FIX). Applies exactly the numbered `[auto]` items to a copy of the PR's files. Nothing else.
5. **Push-fix** (no AI). Checks the edits and commits them as Michael Cutajar (no AI trailer) with each fix named (item, old value, new value, source). Only its final shell step receives the production environment's existing `DERIVED_BUILD_TOKEN`, a repository-scoped writer. The push starts normal required validation and the next review on the resulting commit. The per-PR queue lets the writer finish before the next review starts. No model receives this writer, and it never merges the skill PR.

| Label | Meaning |
|---|---|
| `review-round-1`, `review-round-2` | An automatic fix round has run on this PR |
| `needs-michael` | The loop stopped: HOLD, two fix rounds used, or a fix it was not allowed to make |
| `found-by-review` | On an issue: faults already on main, found while reviewing a PR (one issue per file) |

## What it can and cannot change

It can change, through the fix job only: files under `skills/` and `library/` that the PR already changes. Edits are text fixes from the numbered list, plus `version` and `last_updated` as CI requires.

It cannot, and the push-fix job refuses a patch that tries:

- files outside `skills/` and `library/`, or files the PR does not change;
- new, deleted or renamed files;
- Malta or Australia files, by folder or by frontmatter `jurisdiction:` (`MT`, `AU`, `MT-...`, `AU-...`, on the PR or on main), and sanctioned-country files;
- a file carrying `reviewed_by` or `tier: 1` (it is held for that accountant);
- changing `reviewed_by`, `reviewed_on`, `verified_by`, `tier`, `jurisdiction` or a platform-written key (`approved_by`, `drafted_by`, `validation_status`, `validated`, `license`), compared by parsing the frontmatter;
- adding an em dash; breaking library JSON.

It never pushes to a fork, and no commit from a fork ever lands on a branch here. For a fork PR, the bot makes branch `claude/fix-pr-<n>`: one new commit on `main` holding the PR's `skills/` and `library/` files with the fixes. The PR's author is the commit's author; the bot is only the committer. Before it creates anything, every file of the PR (not only the fixes) is checked against `main` by the same rules as the fixes, so the branch can never carry Malta, Australia, sanctioned-country or approved files, or new approval and platform keys. It refuses if `main` changed any of those files since the PR branched (the PR needs a rebase first). For a same-repo PR it adds the fix on top of the branch, never on `main`, `test`, the CLA branch, a release or bot branch, or any branch a ruleset protects.

It never runs the PR's code. Claude never holds a token that can write and has no shell; the comment, labels and commit are made by plain shell steps in separate jobs.

**What Claude can see.** It reads only the main checkout and the staged PR folder, and fetches web pages (WebFetch, needed to open official sources). It never sees a secret: the subscription token and the GitHub token are not in any file or tool it can reach, and the GitHub token it runs beside can only read this public repository. WebFetch could still send out anything Claude can read, which is public repository content.

## How to stop it

Disable the workflow: Actions, Skill review, the "..." menu, Disable workflow. Or:

```
gh workflow disable skill-review.yml -R openaccountants/openaccountants
```

`gh workflow enable` turns it back on. Removing the secret also stops it: the gate skips quietly when the secret is missing.

## How to re-run it

- Comment `/review` on the PR (anyone with write access).
- Or run it by hand: `gh workflow run skill-review.yml -R openaccountants/openaccountants -f pr=<number>`.

## Setup: one step for Michael

On a machine where you are signed in to Claude Code with your subscription:

```
claude setup-token
```

Copy the token it prints and add it as a repository secret named `CLAUDE_CODE_OAUTH_TOKEN` (Settings, Secrets and variables, Actions, New repository secret), or:

```
gh secret set CLAUDE_CODE_OAUTH_TOKEN -R openaccountants/openaccountants
```

and paste the token when asked. Until the secret exists the workflow does nothing.

**The Claude GitHub App does not need to be installed.** The action's docs say the app is used only when no `github_token` is given (it is reached through an OIDC token exchange); each model action receives its job's short-lived, read-only `GITHUB_TOKEN`. The final shell writer uses the separate scoped credential, so its comments identify that credential's account.

## Known limits

- **The writer credential is required.** If `DERIVED_BUILD_TOKEN` is missing, no fix is published. A credential whose permissions have lapsed can also prevent publication; repair it rather than substituting `GITHUB_TOKEN` and losing the validation hand-off.
- **Fork fixes stay in this repository.** The scoped writer opens a normal PR for the checked copy when its pull-request permission is available; otherwise it leaves the ready-made link. No write reaches the fork. Repository-wide permission for `GITHUB_TOKEN` to approve PRs is not needed or enabled.
- **The daily cap counts every review and fix run from automatic runs**, including the re-review after a fix; runs a maintainer starts are not limited.
- **The guard reads frontmatter, not body text.** An "Approved by" sentence written into a skill's body is not caught by the push-fix guard; the reviewer playbook catches it (honest labels). Look-alike letters (for example Cyrillic) in a `jurisdiction:` value only matter on a new file, which the reviewer reads; an existing Malta or Australia file is caught through main's copy.
- **Follow-up: network egress.** `step-security/harden-runner` with an egress allow-list was considered for the review and fix jobs. Block mode cannot work for the reviewer, which must open official pages on hundreds of government hosts, and audit mode sends runner telemetry to a third party. It is not added; revisit if a fixed list of official hosts becomes practical (for example from `library/` source hosts).
- **Reviews use the subscription's limits.** If they run out, the review job fails and the PR gets a HOLD comment saying no verdict came back.
