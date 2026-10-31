# How to write a skill: the standard

**This file is the one standard for every skill in this repository.** It applies to every writer, human or AI (Claude, ChatGPT, Codex, Gemini or anything else), and to every accountant who contributes. `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md` and `OWNERS.md` point here. If another document says something different, this file wins; fix the other document in the same PR.

The repository is treated as tax law. Every figure must be traceable to the law that sets it.

## What a skill is

A skill is a set of instructions that lets an AI do one tax job correctly, in one place, for one tax year, and shows who stands behind it.

Every part of a skill answers one of four questions. A field that answers none of them does not belong.

| Question | Variables |
|---|---|
| What job? | Country, job, who it covers |
| What is true? | Rules, figures, steps, exceptions, worked examples |
| Still true? | Tax year, date the law was last read, version |
| Who stands behind it? | Written by, checked against the law on, signed by |

"Verified" is three separate facts: who wrote it, whether it was checked against the law and when, and whether a licensed person signed this version. They are kept apart because each can be true without the others. The public label is worked out from them, never typed.

**Strict on shape, local on content.** The fields, the blocks and the checks are the same in all jurisdictions. Only the values change: figures, portals, forms, sources, language. Where a job does not exist in a jurisdiction, the pack README says so, with the reason. Federal systems (the US, Canada, Spain's foral regions) add one field, not a different shape.

The frontmatter below is what the platform reads today. A smaller field list follows these four questions and moves with the server, in one planned change.

## What a perfect skill does

A perfect skill makes a frontier model give the right answer, with its conditions, cited to the law, and never a confident wrong one, for one job in one country.

Each of the twelve lines below is in the standard because a measurement says so. Each line carries its **Evidence** (the test or reading that justifies it) and its **Check** (the function in `scripts/skill_checks.py` that tests it, or "reviewer" when only a human reading the law can). The checks run from `scripts/validate-guides.py`: an error on a PR for a tax skill, a warning on the backlog. Where a line is marked **unmeasured**, it is reasoning, not a result, and the weekly loop owes it a test.

## The twelve lines

### 1. Every figure comes from the official page, for the current tax year, cited to the article

Every rate, threshold, deadline and penalty comes from the law itself (gazette or law register) or the tax authority's own pages, fetched by you, for the tax year the skill covers. Cite the act and article on the row ("ZKPO art. 20"). The statute wins over an authority page that disagrees with it; follow the law, cite it, note the outdated page. Never cite PwC, KPMG, Deloitte, EY, taxsummaries, blogs, law-firm notes or another AI; a secondary source may help you find the law, it is never the citation. `tax_year` is the current year; when a law changes mid-year, give both periods with their dates. The `## Sources` table carries the date each page was read.

- **Evidence:** the 50 most used old skills had 2,318 figures checked on 16 and 17 Oct 2026: 58.5% right, 34.1% wrong or stale, none clean. Rewrites to this standard (DE, GB, NL, MT) came out at about 99%. In the shape test of 31 Oct 2026, two of the three confident-wrong answers came from a stale figure (a 1040 Free File limit of USD 89,000 against USD 95,000 in the law) and from a skill still on tax year 2025; a 2025 skill answers 2026 questions wrong even when the model reads all of it.
- **Check:** `check_tax_year_current` (a) and `check_sources_read_dates` (b). Whether the figure matches the law: reviewer (line 12).

### 2. The official URL sits on the rates row itself

Every row of the rates table carries the URL of the official text it comes from. A row may say `same` to inherit the row above. The Sources table at the end is not enough on its own: `search_rules` and partial fetches return rows without it, so a figure with no URL on its row reaches the model with no citation.

- **Evidence:** year-boundary test: a skill that points at the law plus a live fetch answered 4 of 5; stored facts with no link, 0 of 5. Citations to an official source 76% with the skill against 20% without (4 Aug 2026). The section-demand read of 31 Oct 2026 (453 loads in 28 days, 6.4% with any section held back) showed `get_skill` almost always sends the Sources table, so the row URL is for the other read paths, not for `get_skill`.
- **Check:** `check_rates_rows_sourced` (c).

### 3. Every rule states its conditions next to the figure

A figure without its conditions is wrong for someone. Write who it applies to, from when, and what switches it off, in the same row or sentence as the figure. A condition you cannot source goes on the "Not yet confirmed:" line at the end of `## Sources`, never into the body.

- **Evidence:** every wave since September 2026 found wrong figures rare; the misses were dropped conditions, scope and direction. In the shape test of 31 Oct 2026 the model got every condition question right (100%, 0% confident wrong) when the skill carried the conditions.
- **Check:** `check_not_yet_confirmed` (i) for the line's presence; the conditions themselves: reviewer (line 12).

### 4. For the job covered, the steps are complete: inputs, order, portal, form, box, what happens next

A how-to section names the portal (where you log in), the form, and the box or field numbers, in the order the filer meets them, then what happens after submission (confirmation, payment reference, deadline for the payment). Nothing is left as "file the return".

- **Evidence:** scoreboard baseline, 30 Oct 2026 (50 real questions, two models): how-to questions right 21% with our skill against 38% with web search, while figures and multilingual questions were 100% in every tool arm. Shape test, 31 Oct 2026: how-tos at the closed-book floor (8%) with the whole skill in front of the model; web search 38%. The misses were missing steps, not layout.
- **Check:** reviewer. The scoreboard's how-to percentage is the number this line has to move.

### 5. A rewrite never loses a rule

Every rule, rate, threshold, deadline, exemption, taxpayer group and edge case the old version covered is carried into the new one (checked against the law) or listed on the "Not yet confirmed:" line. Only boilerplate, duplicates and content with no official source may go. If the new file is more than 25% shorter, the PR lists every cut under "Removed and why:", and the independent review compares old against new and records "Lost content restored: N". A rewrite that shrinks more than 25% without that record does not merge.

- **Evidence:** 39 rules lost in 11 rewrites before the rule; 431 restored in 49 PRs since (count to 31 Oct 2026).
- **Check:** reviewer (the "Removed and why:" list and the "Lost content restored: N" comment). No script tests this yet.

### 6. One skill per country and job, named in the pack README; no duplicates

One job in one country has one skill. The pack `README.md` names it under `covered_by` when the slug does not say the domain. A second skill for the same cell is retired with an alias, not kept beside the first.

- **Evidence:** the scoreboard set itself carried pairs: `malta-vat-return` with `mt-vat3-quarterly-return-malta`, `germany-vat-return` with `de-vat-annual-and-special-schemes`. Routing to the right skill was 64% to 70% (30 Oct 2026). The shape test of 31 Oct 2026 put the cost of routing at about 7 points: the same skill pasted in scored 50% (Claude) and 40% (GPT); the live arm, where the model picks the skill, 43% on both. In the wild, `netherlands-vat-return` and `nl-vat-return` were both being loaded (16 and 13 loads in 28 days).
- **Check:** `scripts/build-register.py`, `duplicate` column: two or more slugs in one (country, domain) cell that `covered_by` does not name. `scripts/validate-guides.py` fails a PR that adds or renames a skill when another skill in that jurisdiction has the same job, unless the PR deletes that skill; a different job in an occupied cell only warns. A skill may declare `job:` (a short kebab id such as `30-percent-ruling`); otherwise the job comes from the slug without its country, year and numeric suffix (`scripts/job_identity.py`). `skills/DUPLICATES.md` lists the existing groups.

### 7. The headings are one of the two canonical sets, verbatim, in order

Every tax skill (IT-IND, IT-CORP, VAT, SC, PR, TP, XB) uses one of two heading sets, with every heading present and in this order, so an AI reading any two jurisdictions finds the same things in the same places. A numbering prefix ("## 1.") is tolerated; a source link in brackets after the heading text is tolerated; nothing else is. A skill does not mix the two sets.

The reference set (about 440 skills, the September waves):

```
## Who this applies to
## Rates, bands and thresholds
## The base
## Deadlines and filing
## Penalties and interest
## Cross-border points
## Two worked examples that recompute
## Ask the client first
## Sources
```

The method set (about 250 skills, the October waves):

```
## Scope
## Ask the client first
## The method, step by step
## Boundary and exception table
## Worked cases
## When to refuse or refer
## Filing and payment
## Completion checklist
## (the standard closing block)
```

In the method set, six headings are required (Scope, which may read "Scope and who this is for"; Ask the client first; The method, step by step; Worked cases; When to refuse or refer; the standard closing block) and three are optional (Boundary and exception table; Filing and payment; Completion checklist). The rates, base and deadline material lives under "The method, step by step" as sub-headings, each carrying its source link in the heading text, which is why a bracketed link after a heading is tolerated. What each set holds: residence and scope (who is in, who is out); the rates table with item, amount, tax year and official URL per row; what is taxed, what is deductible or exempt, how losses work; registration, returns, payments, instalments, form, portal, box; late filing, late payment, under-declaration figures; non-residents, treaties, withholding, exit rules that touch this domain; the worked examples (line 9); the facts to ask (line 10); the sources table (line 1). There is no length rule: the model reads the whole skill.

- **Evidence:** shape test, 31 Oct 2026, 30 questions, two models: cutting a fifth of the text changed nothing on Claude (50% right either way) and cost GPT 7 points; the rewritten skills beat their pre-September versions by 16 points on Claude (56% against 40%) and 8 on GPT, and cut confident-wrong from 20% to 0% (Claude). Split by set on the same run: reference set 54% right, 0% confident-wrong (10 skills); method set 50%, 6% (8 skills); skills on neither set 28%, 11% (9 skills, the US, Australia and Canada ones). The two sets are within noise of each other; being on neither is what costs. Section demand, 31 Oct 2026: 6.4% of loads had any section held back, so the earlier inline-budget rule (core sections under a character budget) measured nothing and is dropped. Picking one set for everything is a decision for after the loop has measured both on a full Monday run.
- **Check:** `check_canonical_headings` (d), which accepts either full set. The two older spellings it still accepts in the reference set ("The taxable base", "Worked examples") go once the backlog is rewritten.

### 8. One figure, one home

A figure that belongs to another skill in the pack is linked, not restated. If a sibling skill owns the small-business threshold, link to it; do not copy the number.

- **Evidence:** 10 of 12 indexed US 2026 facts differed across skills (the FEIE cap had four values in six skills), 31 Oct 2026 reading.
- **Check:** `scripts/detect-contradictions.py`, a warning, not a gate.

### 9. Two worked examples that recompute, one of them a decision

One simple case, one with an edge case. Each has the prose walk-through for the reader and, under it, an `oa-check` block that CI recomputes with `scripts/check-examples.py`. Where the topic invites a "which should I" question (sole trader or company, cash or accrual, register for OSS or not, monthly or quarterly), one of the two cases is that decision, worked both ways to the figure that decides it.

```oa-check
name: Sole trader, profit EUR 40,000 (2026 bands)
inputs:
  profit: 40000
steps:
  - band_15: (min(profit, 14500) - 9100) * 0.15
  - band_25: (min(profit, 19500) - 14500) * 0.25
  - band_35: (profit - 19500) * 0.35
  - tax: band_15 + band_25 + band_35
expected:
  tax: 9235.00
```

Arithmetic only: inputs, named steps, `+ - * /`, and `min max abs round floor ceil pct clamp`. Decimal maths; a value matches within `tolerance` (default 0.01). A wrong expected value fails the PR.

- **Evidence:** arithmetic was right in every benchmark answer where the skill carried a recomputing example (baseline 30 Oct 2026). Decision questions sat between floor and ceiling in the shape test of 31 Oct 2026 (31% right with the skill, 13% closed book, 56% web): the worked cases did not cover the "which should I" questions people ask.
- **Check:** `check_two_oa_checks` (e) for the two blocks; `python3 scripts/check-examples.py --require` for the arithmetic. Whether one case is a decision: reviewer.

### 10. "Ask the client first" lists the three to six facts that change the answer

The section names the facts the AI must have before it computes (residence, turnover, entity type, year of registration, whichever switch the rates and deadlines above). It is how the AI asks instead of guessing. **Unmeasured:** no test has yet varied this section; it stays because the reasoning is sound and gets a test in the loop.

- **Evidence:** none yet. The heading's presence is covered by line 7.
- **Check:** reviewer.

### 11. Tier and name are honest and bound to the version

`tier: 2` means **Checked against the law** (built to this standard and independently reviewed before merge) or **Sourced from the law** (an older skill not yet rebuilt). `tier: 1` means a licensed accountant reviewed the whole skill and set `reviewed_by` and `reviewed_on`; no one else sets these keys. A content change after the review drops the name and the skill returns to `tier: 2` until it is reviewed again. Where no accountant signs, the byline is the team's: `trust_label: Built by Michael Cutajar and the OpenAccountants team`.

- **Evidence:** the fidelity exam of Aug 2026 (31 items, three models) found invented attribution the top error (31 of 44). The 17 wrong figures in wave 1 (Oct 2026) all sat in two US skills carrying the accountant-signed label; the label never tracked accuracy.
- **Check:** `check_tier_honest` (g): `reviewed_by` implies `tier: 1` and `tier: 1` implies `reviewed_by`; `check_reviewed_on` (j): a signed skill names the date it was signed. That `reviewed_on` moved with the content: reviewer.

### 12. An independent second reader before merge

Someone other than the writer (a person or a separate AI agent with no shared context) re-reads the cited law, checks every figure, recomputes both examples, fixes what is wrong, and posts a PR comment with three parts: figures checked (a count), fixes made with sources, items still not confirmed. Only then does the PR merge, as **Checked against the law** (`tier: 2`).

- **Evidence:** not one first draft was clean in any wave since September 2026. Reviewer records on 266 merged PRs (22 to 31 Oct 2026) count about 12,234 figures checked.
- **Check:** reviewer; the PR comment pattern is the record. Scripts do not test it.

## Writing rules that sit under the twelve

- **When a site blocks scripts,** open it in a normal browser tab and read it there. Never solve a CAPTCHA or human check. If a site refuses every connection, use an Internet Archive (web.archive.org) copy captured in the current year and say so in the Sources table.
- **Nothing unconfirmed goes in.** If you cannot confirm a figure or rule from an official source, leave it out and list it on the "Not yet confirmed:" line at the end of `## Sources`. Check: `check_not_yet_confirmed` (i).
- **No em dash** anywhere in the writer's text. Check: `check_no_em_dash` (h). The platform-stamped `openaccountants-cta-block` is not yours and is not counted.
- **Sources live in the body**, in the `## Sources` table, not in a frontmatter key, because the platform export re-renders frontmatter and drops keys it does not store:

  ```markdown
  ## Sources

  | Source | URL | Read on |
  |---|---|---|
  | Income Tax Act, Cap. 123, art. 56 | https://legislation.mt/eli/cap/123/eng | 2026-10-22 |
  | MTCA, 2026 tax rates | https://mtca.gov.mt/... | 2026-10-22 |

  Not yet confirmed: ...
  ```

## Updating an existing skill

- Rewrite in place; keep the slug.
- `version` and `last_updated` only go up. Set `version` one step above main's, and keep any version in the body heading the same (CI `compare` fails otherwise). Check: `check_version_numeric` (f).
- Keep a team byline or `trust_label` as it is. Remove a named outside reviewer only when the content they reviewed has changed (line 11).
- Fix contradictions you find in sibling skills in their own PR, not as a bonus edit (line 8).

## Pack README

Each jurisdiction folder has a `README.md` (see [pack-readme-template.md](pack-readme-template.md)). A domain whose skills still carry an old tax year, or leave out a group of taxpayers or a core computation most clients need, gets a `partial:` entry with the reason in double quotes. Remove the entry only when the gap is closed. Niche regimes, special VAT schemes and treaty-rate tables are named out of scope in the README; they do not make a domain partial. `covered_by` names the one skill for a domain when the slug does not say it (line 6).

## Checks before you open a PR

```
python3 scripts/skill_checks.py <skill.md>
python3 scripts/check-examples.py --require <skill.md>
python3 scripts/validate-guides.py --no-index-check
python3 scripts/coverage-report.py --json
```

Edit `skills/**` only. Never edit `packages/`, `index.json` or `llms-full.txt`, and do not add or edit the platform-written keys listed below or the `openaccountants-cta-block`.

# Frontmatter spec

**This section is THE frontmatter spec for every skill file in this repo.** Other docs (`CLAUDE.md`, `CONTRIBUTING.md`) link here rather than restating it. CI enforces it: `scripts/validate-guides.py` hard-fails on malformed frontmatter, a missing `name`/`description`, a non-integer `tax_year`, a missing or invalid `tier` (must be 1 or 2), a missing or malformed `last_updated` (YYYY-MM-DD), and a missing `jurisdiction` (except in a small allowlist of jurisdiction-agnostic directories, where it warns).

## Required keys

| Key | Format | Notes |
|-----|--------|-------|
| `name` | slug, `[country-or-topic]-[domain]` | e.g. `malta-income-tax` |
| `description` | 80-150 words | What it covers, entity types, jurisdiction, tax year, plus trigger phrases the AI should match |
| `jurisdiction` | ISO code | `MT`, `GB`, `DE`, `US`, `US-CA`, `GLOBAL`, `INTL`, `EU-27`. Required even when the folder path implies it. Quote `"NO"` because YAML 1.1 otherwise reads Norway's code as boolean `false` |
| `category` | one of the vocabulary below | Domain the skill covers |
| `tax_year` | **bare integer**, e.g. `2026` | The **coverage start year**, and the current year (line 1). Ranges, fiscal calendars, and qualifiers ("2025-26", "YA 2026", "2567 (2024)") go in `tax_year_notes` and the body text, never here. CI errors on anything that is not an integer 2015-2035 |
| `tier` | `1` or `2` | `1` = **accountant-reviewed** (a named licensed accountant fully reviewed and signed off); `2` = **Checked against the law** or **Sourced from the law** (line 11). These are the only two tiers |
| `last_updated` | `YYYY-MM-DD` | Date the content was last checked/edited. It must never move backwards |

## Optional keys

| Key | Format | Notes |
|-----|--------|-------|
| `tax_year_notes` | quoted string | The human-readable tax-year label when a bare year can't express it: `"2025-26"`, `"FY 2026-27 (AY 2027-28)"`. Its presence is what lets `check_tax_year_current` accept a `tax_year` other than the current year. The platform does not store this key, so the daily export drops it when it re-renders a skill. Put the year label in the body text too, such as a "Tax year" row in the quick-reference table, so it survives |
| `verified_by` | legacy | Do not add to new skills. The platform is retiring it; accountant review uses `reviewed_by` and `reviewed_on` (line 11) |
| `reviewed_by` | `Name, Credential` | Set only by a licensed accountant who reviewed the whole skill, with `reviewed_on` (`YYYY-MM-DD`) and `tier: 1` |
| `depends_on` | YAML list of slugs | Workflow base or country skill this loads on top of |
| `version` | numeric dotted value, e.g. `0.1` | Content version, bumped on substantive change. Keep any body-heading version in step |

## Platform-written keys

The daily export from openaccountants.com (see [WEBSITE-SYNC.md](WEBSITE-SYNC.md)) writes these keys when it renders a skill. Do not add or edit them in a PR: the platform owns their values and rewrites them on the next export. Leave them in place when you edit a skill that already carries them. None of them is a quality state; `tier` remains the only quality field, and `review_status` records where the accountant review stands. `scripts/validate-guides.py` ignores keys it does not know, so a key outside this document is undefined, not validated.

| Key | Values seen | Notes |
|-----|-------------|-------|
| `review_status` | `current` or `pending_review` | Whether the current text carries a professional review. A substantive edit sets the skill back to `pending_review` until it is reviewed again |
| `license` | `AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)` | Written verbatim by the export. [LICENSING.md](../LICENSING.md) is the licence reference |
| `authored_by` | `OpenAccountants team` | Present when the platform team, not a named accountant or GitHub contributor, authored the current revision |
| `trust_label` | `Built by Michael Cutajar and the OpenAccountants team` | The team byline where no accountant signs (line 11). Display attribution for the website, not a review claim |

The export has also written `drafted_by`, `approved_by`, `validation_status` and `validated` on some skills (`grep -rl "^drafted_by:" skills/` lists them). Treat them the same way: leave them alone and do not add them to new files.

## Sync integrity rules

`last_updated` and a numeric `version` are monotonic content metadata: an edit must not decrease either value. A substantive body change should advance the date, the version, or both, and a heading such as `v1.1` must agree with the frontmatter version.

These values are not synchronization tokens. The platform exporter must still compare its stored Git blob hash with the current repository blob before it rewrites an existing `skills/**` file. See [WEBSITE-SYNC.md](WEBSITE-SYNC.md) for the fail-closed compare-and-swap contract and pre-push command.

## Category vocabulary (the real one)

This is the vocabulary actually in use across the repo's skills (by count), not an aspirational list. Use these for new files:

| Category | What it means | Approx. usage |
|----------|---------------|---------------|
| `international` | Country-level tax computation (income tax, VAT, SSC) | ~757 |
| `foundation` | Universal workflow base (domain-agnostic) | ~198 |
| `orchestrator` | Router / intake / assembly files | ~110 |
| `federal` | US federal tax | ~104 |
| `payroll` | Withholding, social security, payslips | ~82 |
| `tax-optimization` | Legal tax reduction strategies, timing, deductions | ~64 |
| `cross-border` | Multi-jurisdiction coordination, treaties, WHT | ~54 |
| `transfer-pricing` | TP documentation, arm's length, CbCR | ~43 |
| `state-tax` | US state tax | ~40 |
| `formation` | Entity types, registration, compliance | ~39 |
| `financial-statements` | Annual accounts, reporting, audit | ~39 |
| `bookkeeping` | Chart of accounts, P&L, balance sheet | ~39 |
| `invoicing` | E-invoicing format, validation, transmission | ~30 |
| `crypto` | Cryptocurrency and digital asset taxation | ~30 |
| `vertical` | Industry-specific accounting patterns | ~28 |
| `integration` | Platform export formats, column mappings | ~20 |

Legacy synonyms still present in older files, not for new files: `federal-tax` (use `federal`), `state` / `us-states` (use `state-tax`), `financial-reporting` (use `financial-statements`), plus stragglers `template`, `pattern(s)`, `intelligence`.

## Frontmatter example

```yaml
---
name: [country-or-topic]-[domain]
description: >
  [One paragraph: what this skill covers, entity types, jurisdiction, tax year.
  Include trigger phrases the AI should match. Be specific about scope.]
jurisdiction: XX           # REQUIRED: MT, GB, DE, US, US-CA, GLOBAL, INTL, EU-27, etc.
category: international    # see the category vocabulary above
tax_year: 2026             # bare integer = the current year the figures apply to
tax_year_notes: "2026-27"  # optional; the export drops it, so repeat the label in the body
tier: 2                    # 1 = accountant-reviewed | 2 = checked against the law / sourced from the law
last_updated: 2026-10-31   # YYYY-MM-DD
version: 0.1
depends_on:
  - [workflow-base-or-country-skill]
---
```

The body opens with `# [Skill Name] v0.1` and this notice, then the nine sections of line 7:

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## General template (accounting packs only)

Bookkeeping, e-invoicing, financial statements and tax optimisation skills (`category` in `bookkeeping`, `invoicing`, `financial-statements`, `tax-optimization`) keep this general shape and belong to the Accounting packs milestone. The twelve lines still apply where they fit (sources, read dates, conditions, no loss on rewrite, honest tier, second reader); `skill_checks.py` runs on them but `validate-guides.py` treats a failure as a warning, never an error. **Tax skills use the nine sections of line 7, not this.**

1. **What this file is.** The workflow base it loads on top of (`us-tax-workflow-base`, `crypto-tax-workflow-base`, `bookkeeping-workflow-base`); what it computes, where it fits in the pipeline, what it does not cover; the tax year it is current for. The reviewer is the customer of the output: the skill produces working papers and a brief, not a return.
2. **Scope statement.** What forms, entity types and line items are covered, and what is out of scope with the skill that handles it.
3. **Filing requirements.** Who must file, thresholds, deadlines, with the statute or section cited.
4. **Rates and thresholds.** A table: item, amount, source, with an official URL per row.
5. **Computation rules.** Step-by-step, written so the AI can execute it mechanically, each step with its citation.
6. **Edge cases and special rules.** Exceptions, elections, safe harbours, each with a citation.
7. **Self-checks.** Inputs trace to source documents; rates match the tax year; computation follows the steps; edge cases checked; output matches the base skill spec.
8. **Sources.** The same `## Sources` table with read dates and the "Not yet confirmed:" line.
9. **Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
