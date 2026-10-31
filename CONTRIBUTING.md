# Contributing to OpenAccountants

Thanks for your interest in contributing. Here's how it works.

## Who can contribute

Anyone. A skill lands as **Checked against the law** (`tier: 2`): built to [the standard](docs/skill-template.md), every figure cited to the law and checked against the statute by an independent review before merge; no accountant has signed it off yet. Older skills not yet rebuilt to the standard are **Sourced from the law** (`tier: 2`): every figure cited to an official source, no accountant sign-off. Drafts are welcome; they are how most of the library started. A skill becomes **accountant-reviewed** (`tier: 1`) only when a licensed accountant whose credential we have checked reviews the whole skill and puts their name on it. Those are the only two tiers; see [docs/QUALITY-TIERS.md](docs/QUALITY-TIERS.md).

To review as an accountant: sign up at [openaccountants.com](https://www.openaccountants.com), finish the [accountant application](https://www.openaccountants.com/onboarding/accountant) with your licence, registration or membership number (provisional and student members of a professional body count, once checked), and set your GitHub username in your profile so we can match your pull requests to you.

Not an accountant? You can still:

- **Draft or fix a skill** from official sources and open a PR. It merges as Checked against the law (`tier: 2`).
- **Report an error** in a skill by opening an issue with the source that shows it.
- **Contribute code** (`mcp/`, `scripts/`, `calculators/`, `.github/`).

There are no fees and no minimum contribution. Contributions of any kind need the [CLA](#contributor-license-agreement-cla).

## The work: complete a pack

[GOAL.md](GOAL.md) sets the target: every jurisdiction with a complete, verified, reviewed tax pack. The work is tracked as one issue per jurisdiction, `[XX] Complete the pack`, on the **Cover the world** milestone, labelled `coverage` plus `owner:<name>` or `owner:open`.

1. Take an issue. Comment `taking` on an `owner:open` issue, or ask the owner in [OWNERS.md](OWNERS.md) for one.
2. Branch `pack/<code>`. Draft the missing domains in the deep-tax shape from [docs/skill-template.md](docs/skill-template.md), with a `## Sources` section and two worked examples that recompute.
3. Run `python3 scripts/validate-guides.py --changed-only` and `python3 scripts/check-examples.py --changed-only`.
4. Open a PR with `Closes #N`. A maintainer listed in [OWNERS.md](OWNERS.md) merges. Nothing counts until merged.

```
gh issue list -R openaccountants/openaccountants -l coverage -l owner:open -m "Cover the world" --state open
```

**Keep it public.** This repository is read by every AI that crawls it. No client names, no prices, no internal plans, no private contact details in any file.

## How to contribute a skill

### Via GitHub PR

Skills are added and changed only through pull requests to this repository.


1. Fork this repo
2. Create your skill in the appropriate **source** directory (`skills/us/federal/`, `skills/us/states/[code]/`, `skills/[country]/`, etc.)
3. Follow the [skill template](docs/skill-template.md)
4. Do **not** run any generator scripts — `index.json`, `llms-full.txt` and `packages/` rebuild in the scheduled platform sync after the source change is ingested
5. Open a PR with a description of what tax forms/schedules the skill covers

> **Important:** edit `skills/**` only. `packages/`, `index.json` and `llms-full.txt` are generated — CI will ask you to revert any changes to them, and the scheduled platform sync regenerates them after confirmed source ingestion. One exception for now: **`packages/us-federal/`** is hand-authored and may be edited directly.

## Repo layout

`skills/` is the editable source; `packages/` is generated from it by `scripts/build-packages.py` (except the hand-authored `packages/us-federal/`); `index.json` at the repo root is the machine-readable inventory of every skill. The one-page canonical answer to "which file do I edit?" is [docs/REPO-LAYOUT.md](docs/REPO-LAYOUT.md).

## Website sync rule

Every skill in `skills/` that should appear on [openaccountants.com](https://www.openaccountants.com) must either:

1. Live in a **recognized country folder** (`skills/<country>/`, `skills/us/federal/`, `skills/us/states/<code>/`), **or**
2. Include **`jurisdiction:` in YAML frontmatter** (e.g. `MT`, `GB`, `US`, `US-CA`, `GLOBAL`, `INTL`)

Skill changes made on openaccountants.com land here through the scheduled sync, committed under the responsible accountant's name. A merged pull request must be ingested and verified in the platform before the next outbound export. The ingestion workflow notifies the platform when configured; a maintainer handles failed notifications and backfills. The exporter must fail closed if its stored Git blob does not match the current source guide. Frontmatter uses `reviewed_by` + `review_status` (the legacy `verified_by` key is being retired automatically). Want your platform edits credited to your GitHub account? Set your GitHub username in your accountant profile on openaccountants.com.

Full details: [docs/WEBSITE-SYNC.md](docs/WEBSITE-SYNC.md)

## Skill structure and frontmatter

**The canonical spec for skill files — required/optional frontmatter keys, formats, the `category` vocabulary, and the body section order — is [docs/skill-template.md](docs/skill-template.md).** Don't restate it; follow it. CI validates required guide schema with `scripts/validate-guides.py` and synchronization metadata with `scripts/check-sync-integrity.py`; citation quality and body structure still require reviewer judgment.

One-line summary: YAML frontmatter (`name`, `description`, `jurisdiction`, `category`, `tax_year`, `tier`, `last_updated`, plus optional keys), then, for a tax skill, the deep-tax shape: who it applies to, rates and thresholds with sources, the base, deadlines, penalties, cross-border points, two worked examples that recompute, the questions to ask the client, and sources with read dates.

All domain skills for a country live in the same directory (e.g., `skills/germany/` contains tax, bookkeeping, payroll, formation, financial statements, transfer pricing, tax optimization, and e-invoicing). The build script detects them by filename suffix and bundles the appropriate workflow base automatically.

## Quality standards

- Follow the ten rules in [docs/skill-template.md](docs/skill-template.md): every amount, percentage, threshold and deadline cited to the law or the tax authority, with the article and a read date; never Big Four firms or blogs; nothing unconfirmed in the skill; one independent review before merge
- Computation rules must be mechanical — the AI should be able to follow them step by step
- Scope must be explicit — what's covered and what's deferred to other skills
- **US skills** load on top of `us-tax-workflow-base` (in `skills/foundation/`)
- **International skills** load on top of `foundation.md` + `intake.md` (generated by `build-packages.py`)
- **Bookkeeping skills** load on top of `bookkeeping-workflow-base` (in `skills/foundation/`)
- **E-invoicing skills** load on top of `einvoice-workflow-base` (in `skills/foundation/`)
- **Payroll skills** load on top of `payroll-workflow-base` (in `skills/foundation/`)
- **Formation skills** load on top of `company-formation-workflow-base` (in `skills/foundation/`)
- **Financial statements skills** load on top of `financial-statements-workflow-base` (in `skills/foundation/`)
- **Transfer pricing skills** load on top of `transfer-pricing-workflow-base` (in `skills/foundation/`)
- **Tax optimization skills** are standalone — no separate workflow base; they follow the universal `workflow-base.md`
- **Crypto tax skills** load on top of `crypto-tax-workflow-base` (in `skills/foundation/`)
- **Cross-border skills** load on top of `cross-border-workflow-base` (in `skills/foundation/`)
- **Vertical skills** (industry-specific) and **integration skills** (platform-specific) are standalone in `skills/reference/verticals/` and `skills/reference/integrations/`
- Citation format: for US, cite IRC sections, state statutes, or IRS notices; for international, cite the relevant tax authority and legislation

## Where to put your files

### Quick reference — common cases

| You're writing… | Put it here | Example |
|-----------------|-------------|---------|
| Country-specific (Malta crypto, UK VAT, Germany payroll) | `skills/[country]/` | `skills/malta/mt-crypto-tax.md` |
| US federal | `skills/us/federal/` | `skills/us/federal/us-crypto-tax.md` |
| US state | `skills/us/states/[code]/` | `skills/us/states/ny/ny-income-tax.md` |
| Global / cross-border (not one country) | `skills/cross-border/` + `jurisdiction:` in frontmatter | `skills/cross-border/oecd-model-treaty-defaults.md` with `jurisdiction: INTL` |
| Industry vertical (developer, e-commerce) | `skills/reference/verticals/` + `jurisdiction: GLOBAL` | `skills/reference/verticals/freelance-developer.md` |
| Platform integration (Stripe, Xero) | `skills/reference/integrations/` + `jurisdiction: GLOBAL` | `skills/reference/integrations/stripe-integration.md` |
| If unsure | Same folder as related skills + **`jurisdiction: XX`** in frontmatter | `jurisdiction: JP`, `MT`, `GLOBAL`, `US`, `US-CA`, etc. |

**Rule:** Folder path is the primary signal. Frontmatter `jurisdiction:` is the backup — use it even when the folder makes it obvious.

### Full directory map

| What you're editing | Source directory |
|---------------------|-----------------|
| US federal skills | `skills/us/federal/` |
| US state skills | `skills/us/states/[two-letter code]/` |
| International country skills (all domains) | `skills/[country-slug]/` |
| Foundation workflow bases | `skills/foundation/` (usually MCP/packages only, not website sync) |
| Cross-border / treaty corridor rules | `skills/cross-border/` (subdirectory `treaty-corridors/` for WHT rates) |
| Industry vertical skills | `skills/reference/verticals/` |
| Platform integration skills | `skills/reference/integrations/` |
| Router | `skills/foundation/global-router.md` |
| Orchestrator files (intake, assembly) | `skills/orchestrator/` |

You never need to run the generators: the scheduled platform sync regenerates every derived tree after your source change has been ingested.

If you add a `references.md` to a country's source directory, it will be included in the generated package automatically.

## Review and merge

Maintainers listed in [OWNERS.md](OWNERS.md) merge. A merged skill without an accountant reviewer is `tier: 2` (Checked against the law). When a licensed accountant reviews it, they set `tier: 1`, `reviewed_by` and `reviewed_on` in a PR of their own, and their name goes on the skill here and on every AI answer that cites it.

## Contributor License Agreement (CLA)

OpenAccountants is a **mixed-licence** project: software is **AGPL-3.0-only** and the skills are under the source-available **OA Guide License**, with a commercial track for both (see [LICENSING.md](LICENSING.md)). The [Contributor License Agreement](CLA.md) lets Glimpse Ltd distribute your contribution under **all** of these tracks. You **retain copyright**; you are granting a license, not handing over ownership.

**GitHub pull requests:** we rely on an **explicit opt-in**. When you open a PR, you must **tick the CLA checkbox** in the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) (and leave it checked on updates to the same PR). That single action is how you record agreement. Maintainers should not merge PRs where the contributor has not confirmed the CLA.

**Website / other channels:** follow whatever acceptance flow that channel provides, or contact **info@openaccountants.com** for a formal signed agreement.

If anything in [CLA.md](CLA.md) is unclear, ask before contributing.

## What you get

- Your name on the skill, linked to your contributor profile
- Public contributor profile showing all your contributions
- Your name, credential and review date on every skill you review, in this repo and in [VERIFIERS.md](VERIFIERS.md)
- The knowledge that thousands of freelancers and small businesses are using your skill to manage their accounting
