# How to write a skill: the standard

**This file is the one standard for every skill in this repository.** It applies to every writer, human or AI (Claude, ChatGPT, Codex, Gemini or anything else), and to every accountant who contributes. `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md` and `docs/OWNERS.md` point here. If another document says something different, this file wins; fix the other document in the same PR.

The repository is treated as tax law. Every figure must be traceable to the law that sets it.

Tax is the first domain; [domains.yml](domains.yml) lists the others (financial reporting, audit, bookkeeping, payroll, running a practice, advisory). A skill in another domain follows this standard too, with two changes the file sets: it is dated by its domain's keys instead of `tax_year`, and its official sources are its domain's hosts (an IFRS skill cites ifrs.org by paragraph). Where this page says "tax year" or "the law", read those for that domain.

## What a skill is

A skill is a set of instructions that lets an AI do one tax job correctly, in one place, for one tax year, and shows who stands behind it.

The country or state folder and the declared jurisdiction must agree. For
example, `skills/us/states/id/` is Idaho (`US-ID`), while `ID` is Indonesia.
An explicit path/code mismatch blocks a PR changing that skill, for every
domain and shape, including metadata-only edits. Body-language and currency
heuristics remain advisory: they are clues for review, not proof of identity.

Every part of a skill answers one of four questions. A field that answers none of them does not belong.

| Question | Variables |
|---|---|
| What job? | Country, job, who it covers |
| What is true? | Rules, figures, steps, exceptions, worked examples |
| Still true? | Tax year, date the law was last read, version |
| Who stands behind it? | Written by, checked against the law on, signed by |

"Verified" is three separate facts: who wrote it, whether it was checked against the law and when, and whether a licensed person signed this version. They are kept apart because each can be true without the others. The public label is worked out from them, never typed.

**Strict on shape, local on content.** The fields, the blocks and the checks are the same in all jurisdictions. Only the values change: figures, portals, forms, sources, language. Where a job does not exist in a jurisdiction, the pack README says so, with the reason. Federal systems (the US, Canada, Spain's foral regions) add one field, not a different shape.

**Countries we do not cover.** No skill, library or evidence file for a country under broad embargo (Russia, Belarus, Cuba, Iran, North Korea, Syria) or under a UN Security Council sanctions regime (Afghanistan, Central African Republic, DR Congo, Haiti, Iraq, Lebanon, Libya, Somalia, South Sudan, Sudan and Guinea-Bissau). The list, its codes and folders live in [`scripts/data/sanctioned.yml`](../scripts/data/sanctioned.yml); `scripts/validate-guides.py` fails a PR that adds or edits a file in their folders or with their `jurisdiction:` code. Venezuela is also excluded by Michael's coverage decision of 12 November 2026. Other countries under US or EU sanctions only, with no UN Security Council regime (such as Myanmar), stay covered unless listed in that file.

The frontmatter below is what the platform reads today. A smaller field list follows these four questions and moves with the server, in one planned change.

## What a perfect skill does

A perfect skill makes a frontier model give the right answer, with its conditions, cited to the law, and never a confident wrong one, for one job in one country.

Each of the twelve lines below is in the standard because a measurement says so. Each line carries its **Evidence** (the test or reading that justifies it) and its **Check** (the function in `scripts/skill_checks.py` that tests it, or "reviewer" when only a human reading the law can). The checks run from `scripts/validate-guides.py`: the fixed core blocks changed content in every domain, while full-corpus scans warn on the backlog. New files must also meet their declared shape; an edit cannot break a shape check it previously passed. Existing shape gaps remain warnings unless this change adds a new source defect. A metadata-only approval does not inherit old body defects. Where a line is marked **unmeasured**, it is reasoning, not a result, and the weekly loop owes it a test.

## The fixed core and the seven shapes

**Strict on the core, flexible on the body.** There is one perfect result and several perfect shapes. The result is the line above. The shape that gets there depends on the job: a rates question, a "how do I file" question and a "should I" question need different things in the skill.

**The fixed core.** Every skill, whatever its shape, carries:

1. The job and the place: country (and state or province), the job, who it covers (lines 6 and 7).
2. The tax year, current (line 1).
3. Every figure with its official URL on the row and a read date in `## Sources` (lines 1 and 2).
4. The conditions next to each figure (line 3).
5. Who stands behind it, honestly (line 11).
6. An answer layer at the top: the key figures and the facts to ask before anything else. In the plugin's usage logs (60 days to 6 Nov 2026, not public), the sections models most often asked for by name were a quick-reference section and a required-inputs section. **Unmeasured** as an effect on answers, and not yet checked by a script: the shape tests owe it a result.

**The body follows one of seven shapes.** Declare it with `type:` in the frontmatter. The checks then test the body against its own shape (`SKILL_TYPES` in `scripts/skill_checks.py`); a skill with no `type:` is checked as before.

| `type:` | The job | What the body must hold | Worked examples | Closest skill today (not yet checked to this shape) |
|---|---|---|---|---|
| `situation-rules` | "Does this apply to me, and how": the rule applied to a set of facts | Who is in and out, the rule, conditions, an exception table, the facts to ask | 2 | `nl-corporate-tax` |
| `filing-howto` | Register, file, pay | The steps in the order the filer meets them: portal, form, box or field, what happens after (line 4) | 1 | `uk-vat-return` |
| `computation` | Work out the figure | Inputs, the computation in order, the form lines it lands on | 2, recomputing | `us-schedule-c-and-se-computation` |
| `decision` | "Which should I" | The options side by side, the figure that decides, a worked decision both ways | 2, one a decision | `us-s-corp-election-decision` |
| `rates-card` | Figures for one country and year | The rates tables, every row linked; no method needed | 1 | `au-rates-2026-27` |
| `cross-country-method` | One topic across several countries | One method, then a section per country with its values | 1 | `global-home-office` |
| `router` | Which skills to load, in what order | The routing steps, what is out of scope, the handoff | 0, or 1 if it carries rates, deadlines or worked cases | `cross-border-tax-router` |

`situation-rules`, `filing-howto`, `computation` and `decision` keep either canonical heading set (line 7). A `router` that carries rates, deadlines or worked cases is doing a tax skill's job and needs one worked example, so declaring a shape cannot dodge line 9. `python3 scripts/check-examples.py --require` uses that same declared shape; a routing-only `router` does not need a dummy calculation because its filename names a tax. An undeclared legacy tax skill still needs at least one example in that command. `rates-card` needs `## Rates, bands and thresholds` and `## Sources`; `cross-country-method` needs `## The method, step by step` and `## Sources`; `router` needs `## The method, step by step`, `## When to refuse or refer` and `## Sources`.

- **Evidence:** a study of 6 Nov 2026: all 2,376 skill files on main (public), plus 60 days of plugin usage and 60 real questions read by hand (usage logs, not public). In that sample about 60% of questions were a person's situation and about 15% a figure; the rest were developers building on the data, return preparation, or too vague to place. The scoreboard of 30 Oct 2026 scored figure questions 100% and condition questions 95% with our skills, decisions 56% and how-tos 21%: the gaps are the content a shape needs (steps, decision cases), not the layout. 1,370 skills (58%) use neither canonical heading set, including most of the 44 most-used; the single most-used skill in the logs (`global-home-office`) is a cross-country method, a shape the earlier standard did not have.
- **Unmeasured:** that each shape beats the others for its own questions. The next step is a question set by shape, a baseline, then two skills per shape rewritten and re-run; a shape stays only if `right` rises and confident-wrong does not.
- **Check:** `check_type_declared` (p, required for a new skill, advisory on legacy gaps) for the key; checks c, d and e read the declared shape.

## How to read a source

Every figure comes from the official page, actually opened by the writer. Memory and secondary summaries do not count.

1. **Route, in order:** a direct fetch of the official page; then a real browser; then a dated archive copy, marked as archived in the Sources table.
2. **Quote it:** each figure carries the exact wording from the page, the link and the read date.
3. **Read the neighbouring sections:** caps, exceptions and definitions often sit elsewhere in the same law. A Kansas example used the right federal unemployment tax rate and missed the wage base in another section.
4. **Respect blocks:** an ordinary browser visit is fine. Never solve a CAPTCHA or disguise a request. If a page will not open, leave the unverified figure out of usable guidance and record the missing confirmation under `## Sources`; never guess it.

## The twelve lines

### 1. Every figure comes from the official page, for the current tax year, cited to the article

Every rate, threshold, deadline and penalty comes from the law itself (gazette or law register) or the tax authority's own pages, fetched by you, for the tax year the skill covers. Cite the act and article on the row ("ZKPO art. 20"). The statute wins over an authority page that disagrees with it; follow the law, cite it, note the outdated page. Never cite PwC, KPMG, Deloitte, EY, taxsummaries, blogs, law-firm notes or another AI; a secondary source may help you find the law, it is never the citation. `tax_year` is the current year; when a law changes mid-year, give both periods with their dates. The `## Sources` table carries the date each page was read.

- **Evidence:** the 50 most used old skills had 2,318 figures checked on 16 and 17 Oct 2026: 58.5% right, 34.1% wrong or stale, none clean. Rewrites to this standard (DE, GB, NL, MT) came out at about 99%. In the shape test of 31 Oct 2026, two of the three confident-wrong answers came from a stale figure (a 1040 Free File limit of USD 89,000 against USD 95,000 in the law) and from a skill still on tax year 2025; a 2025 skill answers 2026 questions wrong even when the model reads all of it.
- **Read dates:** a read date means the page was opened and read, by you, on that day. A server answering is not a read. Where a page failed, the row says so and is not dated as read. Where only part of a long document was read, the row says which part. A row tagged with a tax year links a page for that year, and the page itself names it.
- **Check:** `check_tax_year_current` (a), `check_sources_read_dates` (b), `check_read_date_evidence` (k, warns on a future date, a date resting on a status code, or six or more rows on one day that do not say what was read) and `check_year_matches_link` (o, warns when the URL names an earlier year than the row; it reads the URL, not the page). Whether the figure matches the law: reviewer (line 12).

### 2. The official URL sits on the rates row itself

Every row of the rates table carries the URL of the official text it comes from. A row may say `same` to inherit the row above. A figure whose source could not be opened is left out of the rates table and usable guidance, and listed on the `Not yet confirmed:` line under `## Sources`. An `unverified` mark identifies a legacy evidence gap; it does not make that row acceptable guidance. The Sources table at the end is not enough on its own: `search_rules` and partial fetches return rows without it, so a figure with no URL on its row reaches the model with no citation.

- **Evidence:** year-boundary test: a skill that points at the law plus a live fetch answered 4 of 5; stored facts with no link, 0 of 5. Citations to an official source 76% with the skill against 20% without (4 Aug 2026). The section-demand read of 31 Oct 2026 (453 loads in 28 days, 6.4% with any section held back) showed `get_skill` almost always sends the Sources table, so the row URL is for the other read paths, not for `get_skill`.
- **Host and column:** the URL is the page that holds the row's figure, on the site of the authority the row names, in the column the header says. Citing a secondary host or a neighbour's domain in a one-country skill warns.
- **Check:** `check_rates_rows_sourced` (c), `check_sources_columns` (l) and `check_source_hosts` (m) report the backlog as warnings. In every domain, newly added or edited rate rows without a source URL, including rows marked unverified, and newly added or edited citations to a barred secondary host block the PR. Unchanged legacy defects remain warnings. Unknown tax-authority hosts and inferred library matches remain advisory. Active non-tax domains use their explicit official-source host rules in domains.yml for new citations. A skill whose shape has no rates table (`filing-howto`, `decision`, `cross-country-method`, `router`) passes c when it has none; any rates table it does carry is checked.

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

A merge is the same rule with two files. A PR that deletes a skill names it and lists every item the loser held in two tables in the PR body: `## Moved` (item, from, to, source URL) and `## Not moved` (item, why). "No content lost" is not a list.

- **Evidence:** 39 rules lost in 11 rewrites before the rule; 431 restored in 49 PRs since (count to 31 Oct 2026).
- **Check:** reviewer (the "Removed and why:" list and the "Lost content restored: N" comment). No script tests this yet.

### 6. One skill per country and job, named in the pack README; no duplicates

One job in one country has one skill. The pack `README.md` names it under `covered_by` when the slug does not say the domain. A second skill for the same cell is retired with an alias, not kept beside the first. Folder, `jurisdiction:` and body name one place: `ID` is Indonesia, Idaho is `US-ID`, and a state file never carries another country's currency or tax authority.

- **Evidence:** the scoreboard set itself carried pairs: `malta-vat-return` with `mt-vat3-quarterly-return-malta`, `germany-vat-return` with `de-vat-annual-and-special-schemes`. Routing to the right skill was 64% to 70% (30 Oct 2026). The shape test of 31 Oct 2026 put the cost of routing at about 7 points: the same skill pasted in scored 50% (Claude) and 40% (GPT); the live arm, where the model picks the skill, 43% on both. In the wild, `netherlands-vat-return` and `nl-vat-return` were both being loaded (16 and 13 loads in 28 days).
- **Check:** `scripts/build-register.py`, `duplicate` column: two or more slugs in one (country, domain) cell that `covered_by` does not name. `scripts/validate-guides.py` fails a PR that adds or renames a skill when another skill in that jurisdiction has the same job, unless the PR deletes that skill; a different job in an occupied cell only warns. A skill may declare `job:` (a short kebab id such as `30-percent-ruling`); otherwise the job comes from the slug without its country, year and numeric suffix (`scripts/job_identity.py`). `skills/DUPLICATES.md` lists the existing groups. `check_jurisdiction_body` (n) warns when folder, frontmatter or body disagree.

### 7. The headings are one of the two canonical sets, verbatim, in order

This line applies to the `situation-rules`, `filing-howto`, `computation` and `decision` shapes and to any skill with no `type:`; the other three shapes have their own short sets (see "The fixed core and the seven shapes"). Every such tax skill (IT-IND, IT-CORP, VAT, SC, PR, TP, XB) uses one of two heading sets, with every heading present and in this order, so an AI reading any two jurisdictions finds the same things in the same places. A numbering prefix ("## 1.") is tolerated; a source link in brackets after the heading text is tolerated; nothing else is. A skill does not mix the two sets.

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
## Sources
```

In the method set, six writer-owned headings are required (Scope, which may read "Scope and who this is for"; Ask the client first; The method, step by step; Worked cases; When to refuse or refer; Sources) and three are optional (Boundary and exception table; Filing and payment; Completion checklist). The rates, base and deadline material lives under "The method, step by step" as sub-headings, each carrying its source link in the heading text, which is why a bracketed link after a heading is tolerated. What each set holds: residence and scope (who is in, who is out); the rates table with item, amount, tax year and official URL per row; what is taxed, what is deductible or exempt, how losses work; registration, returns, payments, instalments, form, portal, box; late filing, late payment, under-declaration figures; non-residents, treaties, withholding, exit rules that touch this domain; the worked examples (line 9); the facts to ask (line 10); the sources table (line 1). The platform adds its own closing CTA; a writer never adds a CTA heading. The website admits at most 112,640 UTF-8 bytes per skill. When a file needs splitting, preserve every topic, source and example in a base and a distinct companion job, link them explicitly and record the content map for independent review.

- **Evidence:** shape test, 31 Oct 2026, 30 questions, two models: cutting a fifth of the text changed nothing on Claude (50% right either way) and cost GPT 7 points; the rewritten skills beat their pre-September versions by 16 points on Claude (56% against 40%) and 8 on GPT, and cut confident-wrong from 20% to 0% (Claude). Split by set on the same run: reference set 54% right, 0% confident-wrong (10 skills); method set 50%, 6% (8 skills); skills on neither set 28%, 11% (9 skills, the US, Australia and Canada ones). The two sets are within noise of each other; being on neither is what costs. Section demand, 31 Oct 2026: 6.4% of loads had any section held back, so the earlier inline-budget rule (core sections under a character budget) measured nothing and is dropped. Picking one set for everything is a decision for after the loop has measured both on a full Monday run.
- **Check:** `check_canonical_headings` (d), which accepts either full set, or the short set of a `rates-card`, `cross-country-method` or `router`. The two older spellings it still accepts in the reference set ("The taxable base", "Worked examples") go once the backlog is rewritten.

### 8. One figure, one home

A figure that belongs to another skill in the pack is linked, not restated. If a sibling skill owns the small-business threshold, link to it; do not copy the number.

- **Evidence:** 10 of 12 indexed US 2026 facts differed across skills (the FEIE cap had four values in six skills), 31 Oct 2026 reading.
- **Check:** `scripts/detect-contradictions.py`, a warning, not a gate.

### 9. Two worked examples that recompute, one of them a decision

One simple case, one with an edge case. The number follows the shape: two for `situation-rules`, `computation` and `decision`, one for `filing-howto`, `cross-country-method` and `rates-card`, none for `router` unless it carries rates, deadlines or worked cases. Each has the prose walk-through for the reader and, under it, an `oa-check` block that CI recomputes with `scripts/check-examples.py`. Where the topic invites a "which should I" question (sole trader or company, cash or accrual, register for OSS or not, monthly or quarterly), one of the two cases is that decision, worked both ways to the figure that decides it.

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
- **Check:** `check_two_oa_checks` (e) for the number of blocks the shape needs (two when no `type:` is declared); `python3 scripts/check-examples.py --require` for the arithmetic. Whether one case is a decision: reviewer.

### 10. "Ask the client first" lists the three to six facts that change the answer

The section names the facts the AI must have before it computes (residence, turnover, entity type, year of registration, whichever switch the rates and deadlines above). It is how the AI asks instead of guessing. **Unmeasured:** no test has yet varied this section; it stays because the reasoning is sound and gets a test in the loop.

- **Evidence:** none yet. The heading's presence is covered by line 7.
- **Check:** reviewer.

### 11. Tier and name are honest and bound to the version

A skill has one label with two states. `tier: 2` shows **Built from the law**, with source links and the last check date where those exist. `tier: 1` adds **Approved by [name]**: an accountant with an approved account on openaccountants.com stands behind the whole skill. An accountant who writes and publishes it as their own professional work is also its approver. They set `reviewed_by` (their own name), `reviewed_on` (the actual approval date) and `tier: 1` in the publishing PR. No second accountant or separate approval PR is required. A maintenance assignment, old credit line or AI commit under a person's Git identity does not establish professional publication of that version. Licence numbers stay private.

A body change or a change to source-owned identity, description, category, dependency, period, place, domain or shape metadata requires the accountant to approve that version or the approval to be removed. Credit-only changes do not silently create or renew professional approval. Who wrote or edited a skill remains in the Git history; a commit author's name alone is not professional approval.

- **Evidence:** the fidelity exam of Aug 2026 (31 items, three models) found invented attribution the top error (31 of 44). The 17 wrong figures in wave 1 (Oct 2026) all sat in two US skills carrying the accountant-signed label; the label never tracked accuracy.
- **Check:** `check_tier_honest` (g): `reviewed_by` implies `tier: 1` and `tier: 1` implies `reviewed_by`; `check_reviewed_on` (j): a signed skill names the real, non-future date it was signed; a missing, impossible or future date blocks an approval-only PR too. That `reviewed_on` moved with the content: reviewer.

### 12. An independent second reader before merge

For a new skill or substantive content change, someone other than the writer (a person or a separate AI agent with no shared context) re-reads the cited law, checks every figure in each changed skill, recomputes every worked example required by its shape, fixes what is wrong, and posts a PR comment with three parts: figures checked (a count), fixes made with sources, items still not confirmed. Only then does the PR merge. A maintenance PR that changes only a title, description, dependency name or credit records the exact unchanged body and checks that the metadata matches it; it cannot claim new legal verification. A change to the country, covered period, domain, shape or interpretation needs the full source review. This source check can be done by a separate AI reviewer. It is distinct from the accountant author's own professional approval, recorded in the same PR under line 11. Without that approval, the skill remains **Not yet approved** (`tier: 2`).

- **Evidence:** not one first draft was clean in any wave since September 2026. Reviewer records on 266 merged PRs (22 to 31 Oct 2026) count about 12,234 figures checked.
- **Check:** reviewer; the PR comment pattern is the record. Scripts do not test it. The automated reviewer must state its full figure inventory and checked count; sampling or an incomplete run cannot stand in for this record. Skipped or mixed-file PRs need the same independent source-review record from another person or AI agent; one professional accountant per skill remains enough.

## Writing rules that sit under the twelve

- **When a site blocks scripts,** open it in a normal browser tab and read it there. Never solve a CAPTCHA or human check. If a site refuses every connection, use an Internet Archive (web.archive.org) copy captured in the current year and say so in the Sources table.
- **Nothing unconfirmed goes in.** If you cannot confirm a figure or rule from an official source, leave it out and list it on the "Not yet confirmed:" line at the end of `## Sources`. Check: `check_not_yet_confirmed` (i).
- **No em dash** anywhere in the writer's text. Check: `check_no_em_dash` (h), advisory. The platform-stamped `openaccountants-cta-block` is not yours and is not counted.
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
- Remove a named approver only when the content they approved has changed (line 11).
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
| `description` | At least 40 characters; aim for 80-150 words | What it covers, entity types, jurisdiction, tax year, plus trigger phrases the AI should match |
| `jurisdiction` | ISO code | `MT`, `GB`, `DE`, `US`, `US-CA`, `GLOBAL`, `INTL`, `EU-27`. Required even when the folder path implies it. Quote `"NO"` because YAML 1.1 otherwise reads Norway's code as boolean `false` |
| `category` | one of the vocabulary below | Domain the skill covers |
| `tax_year` | **bare integer**, e.g. `2026` | The **coverage start year**, and the current year (line 1). Ranges, fiscal calendars, and qualifiers ("2025-26", "YA 2026", "2567 (2024)") go in `tax_year_notes` and the body text, never here. CI errors on anything that is not an integer 2015-2035 |
| `tier` | `1` or `2` | `1` adds **Approved by [name]**; `2` has no professional approval. Both show **Built from the law** (line 11). These are the only two tiers |
| `last_updated` | `YYYY-MM-DD` | Date the content was last checked/edited. It must never move backwards |

## Optional keys

| Key | Format | Notes |
|-----|--------|-------|
| `tax_year_notes` | quoted string | The human-readable tax-year label when a bare year can't express it: `"2025-26"`, `"FY 2026-27 (AY 2027-28)"`. For a non-current `tax_year`, it must name an adjacent-year period that starts in that year and includes the current year, such as `2025-26`; an arbitrary note, provenance date or reference to another year cannot exempt stale figures. The platform does not store this key, so the daily export drops it when it re-renders a skill. Put the year label in the body text too, such as a "Tax year" row in the quick-reference table, so it survives |
| `verified_by` | legacy | Do not add to new skills. The platform is retiring it; accountant review uses `reviewed_by` and `reviewed_on` (line 11) |
| `reviewed_by` | `Name` | The approving accountant's name, matching their openaccountants.com account. Set only by them, with `reviewed_on` (`YYYY-MM-DD`) and `tier: 1`. No licence number in the file |
| `status` | `needs_sources` | Set when a tax skill cites no official source yet. The site keeps it off the site and out of the AI plugin until sources are added and this line is removed. CI requires it on an edited tax skill with no source link |
| `type` | one of `situation-rules`, `filing-howto`, `computation`, `decision`, `rates-card`, `cross-country-method`, `router` | The skill's shape ("The fixed core and the seven shapes"). The checks test the body against it. Required for a new skill; existing missing labels remain backlog warnings. The declared shape determines the examples and headings |
| `domain` | an id from [domains.yml](domains.yml) | What the skill is about: `tax`, `financial-reporting`, `audit-assurance`, `bookkeeping`, `payroll`, `practice-management`, `advisory`. It picks how the skill is dated (check a) and which hosts are official (check m). Tax, no domain, and the values the website already writes keep every rule on this page. A value not in the file warns: propose it there |
| `standard`, `effective_date` | quoted string; `YYYY-MM-DD` | Instead of `tax_year`, for `financial-reporting` and `audit-assurance`: the standard as its setter names it, and the date from which the version described applies. Repeat both in the body, since the export may drop keys it does not store |
| `checked_on` | `YYYY-MM-DD` | Instead of `tax_year`, for the other non-tax domains: the day the content was last checked against its official sources |
| `depends_on` | YAML list of slugs | Workflow base or country skill this loads on top of |
| `version` | numeric dotted value, e.g. `0.1` | Content version, bumped on substantive change. Keep any body-heading version in step |

## Platform-written keys

The daily export from openaccountants.com (see [WEBSITE-SYNC.md](WEBSITE-SYNC.md)) writes these keys when it renders a skill. Do not add or edit them in a PR: the platform owns their values and rewrites them on the next export. Leave them in place when you edit a skill that already carries them. None of them is a quality state; `tier` with `reviewed_by` is the only quality field. `review_status`, `authored_by` and `trust_label` were removed on 3 Nov 2026 (one label: Built from the law, plus Approved by). `scripts/validate-guides.py` ignores keys it does not know, so a key outside this document is undefined, not validated.

| Key | Values seen | Notes |
|-----|-------------|-------|
| `license` | `AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)` | Written verbatim by the export. [LICENSING.md](../LICENSING.md) is the licence reference |

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
tier: 2                    # 1 = Approved by the named accountant | 2 = Not yet approved
last_updated: 2026-10-31   # YYYY-MM-DD
version: 0.1
depends_on:
  - [workflow-base-or-country-skill]
---
```

The body opens with `# [Skill Name] v0.1` and this notice, then the nine sections of line 7:

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## General template (accounting packs only)

Bookkeeping, e-invoicing, financial statements and tax optimisation skills (`category` in `bookkeeping`, `invoicing`, `financial-statements`, `tax-optimization`) keep this general shape and belong to the Accounting packs milestone. The twelve lines still apply where they fit (sources, read dates, conditions, no loss on rewrite, honest tier, second reader); The fixed-core admission rules apply in every domain. Existing general-template shape gaps remain warnings until improved; a new skill declares the appropriate one of the seven shapes above. **Tax skills use the applicable headings in line 7, not this legacy template.**

1. **What this file is.** The workflow base it loads on top of (`us-tax-workflow-base`, `crypto-tax-workflow-base`, `bookkeeping-workflow-base`); what it computes, where it fits in the pipeline, what it does not cover; the tax year it is current for. The reviewer is the customer of the output: the skill produces working papers and a brief, not a return.
2. **Scope statement.** What forms, entity types and line items are covered, and what is out of scope with the skill that handles it.
3. **Filing requirements.** Who must file, thresholds, deadlines, with the statute or section cited.
4. **Rates and thresholds.** A table: item, amount, source, with an official URL per row.
5. **Computation rules.** Step-by-step, written so the AI can execute it mechanically, each step with its citation.
6. **Edge cases and special rules.** Exceptions, elections, safe harbours, each with a citation.
7. **Self-checks.** Inputs trace to source documents; rates match the tax year; computation follows the steps; edge cases checked; output matches the base skill spec.
8. **Sources.** The same `## Sources` table with read dates and the "Not yet confirmed:" line.
9. **Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
