# Contributing to OpenAccountants

Thanks for your interest in contributing. Here's how it works.

## Who can contribute

Anyone. You don't need to be an accountant to write a skill. You need to know your state's tax code well enough to cite the statutes. Accountants then verify what you wrote.

## How to contribute a skill

### Option 1: Via the website

1. Go to [openaccountants.com/contribute](https://openaccountants.com/contribute)
2. Sign up for an account
3. Use the submission form to upload your skill
4. It goes live immediately as "unverified"

### Option 2: Via GitHub PR

1. Fork this repo
2. Create your skill in the appropriate directory (`skills/federal/`, `skills/california/`, etc.)
3. Follow the [skill template](skill-template.md)
4. Open a PR with a description of what tax forms/schedules the skill covers

## Skill structure

Every skill follows the same structure:

- **Frontmatter** — name, description, version, jurisdiction, tax year, dependencies
- **Scope statement** — what it covers, what it doesn't
- **Filing requirements** — who needs to file, thresholds, deadlines
- **Rates and thresholds** — every number with a statute citation
- **Computation rules** — step-by-step logic Claude can execute
- **Edge cases** — exceptions, elections, safe harbors
- **Self-checks** — verification items for the reviewer
- **Disclaimer** — not tax advice

## Quality standards

- Every dollar amount, percentage, and threshold must have a primary source citation (IRC section, state statute, IRS notice, etc.)
- Computation rules must be mechanical — Claude should be able to follow them step by step
- Scope must be explicit — what's covered and what's deferred to other skills
- The skill must load on top of `us-tax-workflow-base`

## Verification

After you submit, licensed accountants review each section of your skill on [openaccountants.com](https://openaccountants.com). When every section is approved, the skill gets a green "verified" badge. Your name stays on it as the author.

## What you get

- Your name on the skill, linked to your contributor profile
- Public contributor profile showing all your contributions
- Accountant verification — real professionals review your work
- The knowledge that thousands of freelancers are using your skill to understand their taxes
