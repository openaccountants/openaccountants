# Automated review of skill PRs

A GitHub workflow reviews every PR that changes `skills/**` or `library/**`, posts one verdict comment, and can fix what it found, up to two rounds. It is line 12 of [skill-template.md](skill-template.md) (an independent second reader), run by Claude through the official [Claude Code GitHub Action](https://github.com/anthropics/claude-code-action) on the founder's Claude subscription. It never approves and never merges: a maintainer still does.

- Workflow: [`.github/workflows/skill-review.yml`](../.github/workflows/skill-review.yml) (its header explains each security choice).
- Playbooks Claude follows, read from main: [`.claude/agents/skill-reviewer.md`](../.claude/agents/skill-reviewer.md) and [`.claude/agents/skill-fixer.md`](../.claude/agents/skill-fixer.md).

## What runs, and when

1. **Gate** (no AI). Runs when a skill PR is opened, reopened, marked ready or pushed to; when someone with write access comments `/review`; or when the workflow is run by hand. It skips drafts, closed PRs, PRs not aimed at `main`, and PRs that change `.github/`, `scripts/`, `.claude/`, a `CLAUDE.md` or an `AGENTS.md` (those stay human-only). It also skips once 25 reviews have run in the UTC day, with a short comment saying so.
2. **Review** (Claude, read-only). Checks figures against official sources (10 spot checks, or a quote check when the PR gives a URL and quote per figure), content lost against main (the 25% rule), worked examples, honest labels, scope (sanctioned countries; Malta and Australia are comment-only) and duplicates. It asks only for objective fixes: a wrong figure, a missing or unofficial or undated source, arithmetic, lost content, a stale tax year, a missing core item. Style and layout are optional notes, never fixes.
   The verdict judges only what the PR changes (its added, changed and removed lines and what they directly feed). Faults in lines the PR does not touch go under "Found on main (not caused by this PR)" and never change the verdict.
3. **Publish** (no AI). Posts the comment, starting `VERDICT: MERGE`, `FIX` or `HOLD`, with a figures table and, for FIX, a numbered list of exact changes. Each file listed under "Found on main" gets one open issue, "Found by review: <path>", labelled `found-by-review`: a new issue the first time, a comment on the same issue after that.
4. **Fix** (Claude, only on FIX). Applies exactly the numbered `[auto]` items to a copy of the PR's files. Nothing else.
5. **Push-fix** (no AI). Checks the edits, commits them as Michael Cutajar (no AI trailer) with each fix named (item, old value, new value, source), and starts a new review.

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
- Malta, Australia or sanctioned-country files;
- a file carrying `reviewed_by` or `tier: 1` (it is held for that accountant);
- adding or changing `reviewed_by`, `reviewed_on`, `verified_by` or `tier`;
- adding an em dash; breaking library JSON.

It never pushes to a fork. For a fork PR, the fixes go on a branch `claude/fix-pr-<n>` in this repository, and the bot comments on the original PR.

It never runs the PR's code. Claude never holds a token that can write; the comment, labels and commit are made by plain shell steps in separate jobs.

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

**The Claude GitHub App does not need to be installed.** The action's docs say the app is used only when no `github_token` is given (it is reached through an OIDC token exchange); this workflow passes each job's own short-lived `GITHUB_TOKEN`, so comments appear as `github-actions[bot]`.

## Known limits

- **CI does not start on a bot commit.** GitHub does not run workflows for commits made with `GITHUB_TOKEN`, so after an automatic fix the required checks (validate, unit-tests, guard-derived-trees, cla) wait. Close and reopen the PR to run them. The re-review itself is started by the bot.
- **Fork PRs get a link, not a PR, by default.** The repository setting "Allow GitHub Actions to create and approve pull requests" is off, so the bot cannot open "Fixes for #<n>". It comments a ready-made link instead; whoever opens that PR starts its review, and the fix rounds carry over. Turning the setting on lets the bot open the PR itself, but it also lets any workflow approve PRs, so it is left off.
- **The daily cap counts every review**, including the re-review after a fix.
- **Reviews use the subscription's limits.** If they run out, the review job fails and the PR gets a HOLD comment saying no verdict came back.
