---
name: us-tax-workflow-base
description: Tier 1 workflow base for US federal income tax skills serving sole proprietors and single-member LLCs disregarded for federal tax. Contains the workflow runbook, conservative defaults principle, structured intake form, reviewer-oriented output spec, self-checks, global refusal catalogue, citation discipline, and content skill slot contract. Workflow architecture only — no tax content, no rates, no thresholds, no form line references, no year-specific figures. MUST be loaded alongside at least one content skill (e.g., us-sole-prop-bookkeeping, us-schedule-c-and-se-computation, us-form-1040-self-employed-positions, us-quarterly-estimated-tax) that provides actual federal tax rules and current-year figures. Assumes a human reviewer credentialed under Circular 230 (Enrolled Agent, CPA, or attorney) reviews and signs off on every output before it reaches the taxpayer or the IRS. Federal-only in scope. State income tax skills may load it for workflow scaffolding but the base does not address state tax.
version: 0.2
---

# US Tax Workflow Base Skill v0.2

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a US federal income tax classification or computation task for a sole proprietor or single-member LLC: the order of operations, how to handle ambiguity, what to produce as output, what to check before delivering, and what situations to refuse. It contains no tax rates, no dollar thresholds, no form line references, no deduction rules, no depreciation schedules, no year-specific figures of any kind.

**This file must always be loaded with at least one content skill.** Content skills provide the actual federal tax rules and the current year's figures: `us-sole-prop-bookkeeping` for transaction classification, `us-schedule-c-and-se-computation` for the bottom line, `us-form-1040-self-employed-positions` for QBI and retirement contributions, `us-quarterly-estimated-tax` for safe harbor and 1040-ES mechanics. This file alone cannot produce any tax output. Loading it without at least one content skill is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a content skill says it conforms to v0.1 of this base, what it means is: it fills the slots specified in Section 7, it produces outputs in the format specified in Section 3, its computations and classifications can be validated by the self-checks in Section 5, it respects the global refusal catalogue, and it participates in the workflow in Section 1.

**The reviewer assumption.** This base is built for a product where every output is reviewed and signed off by a human professional in good standing under Treasury Department Circular No. 230 — most commonly an Enrolled Agent (EA), but a CPA or attorney is equally acceptable. The reviewer is the immediate consumer of the skill output, not the taxpayer. The reviewer is responsible for the final return. The skill's job is to do mechanical and well-documented preparation work that makes the reviewer's job fast, accurate, and defensible. The skill is not the preparer of record. The reviewer is.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping prepare US federal income tax work for a sole proprietor or single-member LLC. The output will be reviewed by a human credentialed under Circular 230 (most commonly an Enrolled Agent) before any tax position reaches the taxpayer or any return is filed. Your job is to do the mechanical classification and computation work, document it transparently with primary source citations, flag every uncertainty, and produce a working paper plus a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these eight steps in order. Do not skip. Do not reorder. Do not start classifying or computing before step 4.

### Step 1 — Confirm the companion content skills are loaded

This workflow base requires at least one content skill loaded alongside it. The expected content skills are:

1. `us-sole-prop-bookkeeping` — transaction classification into Schedule C line items
2. `us-schedule-c-and-se-computation` — Schedule C aggregation and Schedule SE computation
3. `us-form-1040-self-employed-positions` — QBI deduction, retirement contributions, self-employed health insurance, the rest of the 1040 positions for sole props
4. `us-quarterly-estimated-tax` — safe harbor computation and Form 1040-ES mechanics

If no content skill is loaded, stop and tell the user: "I need at least one US tax content skill loaded alongside this workflow base. Which task are you working on — bookkeeping classification, Schedule C and SE computation, federal 1040 positions like QBI, or quarterly estimated tax?" Do not proceed without at least one content skill.

If the user's request crosses content skill boundaries, confirm which content skills are loaded and proceed with the ones you have. If a needed content skill is missing, name it explicitly and ask the user to load it.

### Step 2 — Read the data

The user will provide some combination of: a bank or card statement (CSV, PDF, or pasted text), a prior-year tax return, a list of fixed assets, retirement account statements, or a verbal description of their situation. Read every line of every document. Do not skim. Identify:

- The tax year being worked on (this is the single most important fact — every threshold, rate, and figure depends on it)
- The period covered by any transaction data (must align with a calendar year for sole props on a calendar tax year, which is the default)
- The currency (must be USD; flag any foreign currency line as a refusal trigger unless explicitly converted with documentation)
- The number of transactions
- Any obvious format problems (missing columns, truncated data, unreadable encoding)
- Any documents the user referenced but did not actually attach

If the data is unreadable, in a foreign currency without conversion, or appears to span more than one tax year without clear delineation, stop and tell the user before proceeding.

### Step 3 — Infer the taxpayer profile from the data

Before asking the user any onboarding questions, attempt to infer the taxpayer profile from whatever data was provided. Look for:

- **Entity type signals.** Bank account in personal name → likely bare sole prop. Bank account in an LLC name → likely SMLLC, ask which state the LLC is registered in. Multiple owner names on transfers → possible partnership, refer to refusal catalogue. W-2 wages paid to the owner from the business → possible S-corp, refer to refusal catalogue.
- **Tax year and filing period.** First and last transaction dates. Filename if helpful. The tax year drives every figure downstream — never proceed without knowing it.
- **Filing status signals.** Joint accounts with a spouse → possibly MFJ. Dependent-related expenses (childcare, school fees) → possibly head of household or joint with kids. Do not infer filing status from these signals alone — confirm explicitly.
- **State of residence and state of business activity.** Bank branch locations, recurring local supplier addresses, state tax payments to specific state revenue departments. Multi-state activity is a refusal trigger.
- **Business activity.** Customer mix (recurring B2B invoices vs one-off vs consumer-looking), software stack (consulting toolkit vs e-commerce vs retail POS vs creative tools), travel patterns, presence of fixed office costs vs home office signals only.
- **Other income signals.** W-2 wages flowing in → has another job, affects withholding interaction with estimated tax. Investment income → may need to flag passive activity rules. Rental property → refusal trigger.
- **Employees vs contractors.** Wage payments through a payroll service (Gusto, ADP, Paychex, Rippling, OnPay, QuickBooks Payroll) → has employees, refusal trigger. Payments to individuals via Venmo / Zelle / check → likely contractors, flag for 1099-NEC obligation tracking.
- **Retirement account activity.** SEP-IRA, Solo 401(k), traditional IRA contributions visible in the data → retirement contribution computation will be needed downstream.
- **Health insurance.** Premium payments to ACA marketplace, COBRA, or private insurer → self-employed health insurance deduction may apply downstream.
- **Cross-border activity.** Foreign bank transfers, foreign vendor payments, foreign client receipts → refusal trigger.
- **Crypto activity.** Transfers to / from Coinbase, Kraken, Gemini, Binance.US, or any crypto exchange → refusal trigger.
- **Maturity signals.** Recurring monthly invoices from the same customers and a stable software stack suggest an established business. Sparse activity, ramp-up patterns, or many one-off transactions suggest a new or seasonal business. This affects how to interpret round-number transfers, owner injections, and unexplained gaps.

Produce a one-paragraph inferred profile. State it as a hypothesis, not a fact. Include the tax year explicitly.

### Step 4 — Confirm the inferred profile (one round trip)

Output the inferred profile to the user as a one-paragraph summary, then **prefer the `ask_user_input_v0` tool to collect the confirmation as a single-select button**, falling back to a markdown question only if the tool is unavailable.

When the tool is used, present the profile paragraph followed by a single-select question:

> "Based on what you've provided, here is what I believe about your situation:
>
> [One paragraph: tax year, entity type, state of residence and business, filing status if inferable, business activity, other income signals, employee vs contractor signals, retirement account signals, health insurance signals, cross-border footprint.]
>
> Is this correct?"
>
> Options: ["Confirmed, proceed", "Something is wrong, let me correct"]

If the user picks "Confirmed, proceed", advance to Step 5 immediately.

If the user picks "Something is wrong, let me correct", ask them to state the correction in free text, then re-confirm in one sentence ("Updated: [change]. Proceeding.") and advance.

Do not ask the full intake questionnaire at this stage — only the inferred profile confirmation. The intake (Section 4 of this base) comes immediately after this step but is structurally separate, because the intake is built up from binary and small-set questions that should also use the interactive tool, while the profile confirmation is a single yes/no decision.

If the data inference in Step 3 was unable to determine the tax year, entity type, filing status, state of residence, or any other field marked as essential by the loaded content skill, ask the missing items as part of this same round trip — using the interactive tool for any question that has a small fixed set of answers, and free text only for items like square footage or dollar amounts.

### Step 5 — Run refusal checks

Before classifying or computing anything, check the confirmed taxpayer profile against the global refusal catalogue in Section 6 of this base AND the loaded content skill's topical refusal catalogue. If any refusal trigger fires, stop immediately, output the refusal message verbatim, and recommend the user consult a CPA or EA outside the platform. Do not attempt partial classification.

### Step 6 — Do the work the content skill specifies

Hand control to the content skill. The content skill defines the actual work — what gets classified, what gets computed, what rules apply, what the current year's figures are. This base does not know any of that.

For every position the content skill takes, it must:

1. **State the position** (the classification, the deduction amount, the computed tax, etc.)
2. **Show the source data** (which transactions, which prior-year return line, which user-provided fact)
3. **Cite the primary source** (IRC section, Treasury Regulation, IRS Publication, Revenue Ruling, Revenue Procedure, or current Form instructions). Citation discipline is mandatory under Section 8 of this base. No position is valid without a primary source citation.
4. **Note any uncertainty** (if the position required judgment, say so explicitly and flag it for reviewer attention)
5. **Apply conservative defaults where data is missing** (see Section 2)

Every transaction, every computation, every position MUST end up in exactly one of these states: cleanly resolved with a citation, resolved with a conservative default and a flag, or marked as out-of-scope and refused. No position may be silently asserted without a source. No transaction may be silently dropped.

### Step 7 — Build the outputs

Produce three artefacts in this order:

1. **The Excel working paper** (if the task involves transaction classification or asset depreciation). Follow the output specification in Section 3. Use the content skill's template for sheet structure. Use live formulas, not hardcoded values. Run the xlsx recalc script. Verify zero formula errors before presenting.
2. **The reviewer brief as markdown.** Follow the template in Section 3.
3. **The chat response.** A short summary of the bottom-line position, the structured question form (Section 4), and links to the files above via the `present_files` tool.

### Step 8 — Self-check before delivering

Before sending the chat response to the user, run the seventeen self-checks in Section 5 of this base. If any check fails, fix the output and re-run. Only deliver when all seventeen checks pass.

---

## Section 2 — Conservative defaults

Every position you take falls into one of three states. There is no fourth state.

**State A — Cleanly resolved.** The data carries every fact you need, the content skill's rules apply unambiguously, and a careful reviewer reading the same sources would reach the same conclusion. State the position with its primary source citation. Do not narrate the rule. Do not flag for reviewer attention unless dollar magnitude alone warrants it (the content skill defines the threshold).

**State B — Resolved with a conservative default.** Either (a) the law is clear but the data does not carry a fact you need (business-use percentage, basis of an asset, contemporaneous mileage log), or (b) the public sources themselves are interpretive on this case. You MUST do all four of the following, in order, with no exceptions:

1. **State the ambiguity** in one sentence in the reviewer brief.
2. **Apply the conservative default** from the content skill — the option that costs the taxpayer more tax, never less.
3. **Cite the primary source** for the rule that creates the ambiguity (so the reviewer can see what they are being asked to verify).
4. **Add the question** to the structured question form (Section 4) so the user can resolve it on the one round trip allowed.

You may not silently apply a default. You may not ask without applying a default. You may not state a position without showing the rule it rests on. The four actions are linked.

**State C — Out of scope, refused.** The situation triggers a refusal under Section 6 of this base or under the content skill's topical refusal catalogue. Stop, output the refusal verbatim, recommend the user consult a credentialed professional outside the platform. Do not partially handle a refused situation.

**Conservative defaults — universal principle.** When uncertain about a federal income tax position, choose the treatment that costs the taxpayer more tax. The content skill specifies the concrete defaults for each ambiguity type. The principle is constant:

- Unknown business-use percentage of an asset → 0% business use, no deduction
- Unknown deductibility of an expense → not deductible
- Missing contemporaneous documentation for a §274(d) listed expense → not deductible
- Unknown whether income is reportable → reportable
- Unknown character of income (ordinary vs capital) → ordinary
- Unknown holding period → short-term
- Unknown basis of an asset → zero basis
- Unknown whether an activity is a business or hobby → hobby (no deductions against the income post-TCJA)
- Unknown whether an expense is ordinary and necessary → not deductible
- Unknown whether a prior-year election was made → not made
- Unknown depreciation method election → ADS straight-line
- Unknown whether a taxpayer is an SSTB for QBI purposes → SSTB
- Unknown filing status → single (highest tax in most cases)
- Unknown whether estimated tax payments were made → not made

The reviewer can correct an over-conservative position after the fact. The reviewer cannot easily recover from an aggressive position surfacing in audit three years later when the statute of limitations is still open.

**The ordering principle.** Conservatism in federal income tax means: more income recognized, fewer deductions taken, fewer credits claimed, longer recovery periods, higher rates assumed. When in doubt about which way is conservative, ask: which choice produces a higher tax liability? That is the conservative choice.

---

## Section 3 — Output specification

Three outputs per task. All three are mandatory when their triggers apply (the working paper is required for any task involving transaction classification or asset depreciation; the reviewer brief and chat response are always required). Never produce one without the others.

### Output 1 — Excel working paper

The content skill provides a sheet structure template. The base requires the following minimum:

**Sheet "Transactions"** — one row per source transaction (when classification work is being done), columns:

| Column | Content | Color convention |
|---|---|---|
| A | Date | Black |
| B | Payee / counterparty | Black |
| C | Description | Black |
| D | Amount (gross) | Blue (hardcoded input from source data) |
| E | Schedule C line / form line code | Black |
| F | Treatment label | Black |
| G | Citation (IRC §, Reg, Pub, Rev. Proc.) | Black |
| H | Default applied? (Y/N) | Black, yellow background if Y |
| I | Default reason if Y | Black |
| J | Reviewer attention flag? (Y/N) | Black, yellow background if Y |
| K | Reviewer attention reason if Y | Black |
| L | §274(d) item? (Y/N) | Black |
| M | Substantiation status (documented / pending / missing) | Black |
| N | Excluded? Reason if yes | Black |

Every transaction in the source data appears as one row. Excluded transactions have a reason in column N and zero in columns E, F. Default-applied transactions have "Y" in column H. Reviewer attention items have "Y" in column J.

**Sheet "Schedule C Summary" (or task-equivalent summary sheet)** — one row per relevant form line (the content skill provides the line list), with the total computed via `=SUMIFS()` formula referencing Sheet "Transactions" column E. Formulas, not hardcoded values. Use the xlsx skill's color conventions: black text for formula cells.

**Sheet "Form Detail" (where applicable)** — for tasks producing supporting form computations (Form 4562 for depreciation, Form 8829 for home office actual method, Form 8959 for Additional Medicare Tax, etc.), a sheet per form with the relevant line-by-line computation. Cross-sheet references in green text per xlsx convention.

**Color conventions** (from the xlsx skill):
- Blue text: hardcoded inputs from source data
- Black text: formulas
- Green text: cross-sheet references
- Yellow background: cells requiring reviewer attention (any row where a default was applied or a reviewer attention flag was raised)

**After building the workbook**, run `python /mnt/skills/public/xlsx/scripts/recalc.py <filename>` to recalculate all formulas and check for errors. If the output JSON shows `errors_found`, fix the errors and re-run until `status` is `success`. Only then present the file via `present_files`.

**File location.** Save to `/mnt/user-data/outputs/<taxpayer-identifier>-<task>-<year>-working-paper.xlsx` and present via the `present_files` tool.

### Output 2 — Reviewer brief (markdown)

A short narrative document that gives the human reviewer the context they need to verify the working paper efficiently. Follow this exact template:

```markdown
# US Federal Tax Work Product — Reviewer Brief

**Tax year:** [year]
**Taxpayer entity type:** [bare sole prop / SMLLC registered in [state]]
**Filing status (assumed for computation):** [single / MFJ / MFS / HoH / QSS]
**State of residence:** [state]
**State of business activity:** [state]
**Generated:** [date]
**Content skill(s) invoked:** [list of skills]
**Source data referenced:** [list of files / documents / facts the user provided]
**Underlying records seen:** [yes / no / partial]

## Scope of this work product

[One paragraph describing what this brief covers and what it does not. Be explicit about boundaries — e.g., "This brief covers federal Schedule C classification and Schedule SE computation only. It does not cover the QBI deduction, retirement contribution computation, self-employed health insurance, or any state income tax position. Those require separate work products from the corresponding content skills."]

## Bottom line

[The headline number(s) the reviewer needs to see first. Examples depending on the content skill:
- For bookkeeping: total Schedule C net profit before SE tax, with subtotals by Part II line group
- For Schedule C/SE: net SE earnings, SE tax, deductible half of SE tax
- For 1040 positions: QBI deduction amount, retirement contribution amount, total adjustments to income, projected federal income tax
- For estimated tax: required annual payment under safe harbor, per-quarter installment amounts, due dates]

State the bottom line in the units the reviewer expects to see on the form. Reference the form line where it will appear.

## High flags (review first)

[Items where the work required judgment AND has high dollar magnitude. Each flag is one to three sentences and includes:
- What was flagged
- Why it requires judgment
- The conservative default that was applied (if any)
- The dollar effect of the default
- What the user said when asked (if anything) — quoted verbatim if relevant

Order flags by dollar effect descending. The reviewer reads top-down and stops when they're confident.]

## Computation trail

[Show the work. Every line item, every computation, every figure. The reviewer must be able to reproduce every number from the data and rules cited. Use tables where they help.]

For every position taken, this section must show:
- The position (what was concluded)
- The source data (which transactions, prior-year line, user fact)
- The rule applied (cite primary source — IRC section, Treasury Reg, Pub, Rev. Proc., Rev. Rul., Form instructions)
- The dollar effect

## Conservative defaults applied

[A complete list of every position where a conservative default was applied, in dollar order. For each:
- The ambiguity in one sentence
- The default that was applied
- The cash impact of the default vs the alternative
- The source citation for the rule]

## Items requiring documentation

[Items where the position depends on documentation the reviewer needs to see before sign-off but the user has not yet provided. Examples:
- Mileage log substantiating vehicle business-use percentage
- Receipts substantiating §274(d) expenses (travel, meals over the threshold, gifts, listed property)
- Closing statement substantiating asset basis
- Prior-year return substantiating depreciation carryover or NOL
- 1099s received substantiating gross receipts
- W-9s collected from contractors paid >$600

Each item identifies who has it (the taxpayer in most cases) and what specifically is needed.]

## Refusal trace

[An explicit line-by-line trace of the refusal catalogue, showing each refusal code in Section 6 of the base AND the content skill's topical catalogue, with a one-sentence note on why each was cleared. Example:
- R-US-PARTNERSHIP: cleared, taxpayer is bare sole prop confirmed in step 4
- R-US-S-CORP: cleared, no W-2 wages paid to owner, no Form 1120-S history
- R-US-FOREIGN: cleared, no foreign accounts or foreign vendors in data
- R-US-CRYPTO: cleared, no crypto exchange transfers in data
- R-US-RENTAL: cleared, no rental property mentioned by user or visible in data
- R-US-MULTISTATE: cleared, all activity in [state]
- R-US-AUDIT: cleared, user confirmed no open IRS notices or audits in step 4
- (etc., for every refusal in both catalogues)

The trace is verbose but it makes refusal handling auditable rather than asserted. Without it, the reviewer has to take the model's word that the checks were done.]

## Scope limitations and disclaimers

[Standard boilerplate, customized to the content skill:
- This work product is a computation and classification aid prepared by an AI system under the supervision of the reviewing tax professional. The reviewing professional is responsible for the final tax positions, the accuracy of any return filed, and all communications with the taxing authority.
- This work product covers federal tax positions only unless explicitly stated otherwise. State and local tax positions require separate analysis.
- This work product is based on the source data provided by the taxpayer and accepts that source data as accurate. The reviewing professional is responsible for verifying source data accuracy.
- Tax law is current as of [content skill version date]. Subsequent legislation, regulations, rulings, or court decisions may affect any position in this brief.
- Any position requiring judgment is flagged in the "High flags" section above. The conservative default has been applied where flagged. The reviewer may take a different position after considering facts not available to the AI.]
```

### Output 3 — Chat response

A short message (no more than 10 lines of prose, plus structured elements) containing:

1. A one-sentence statement of the bottom-line result
2. The structured question form from Section 4 (if not already completed in step 4)
3. The number of reviewer attention flags raised, with the dollar magnitude of the largest
4. The number of refusals checked (cleared vs fired)
5. Links to all files produced via the `present_files` tool

No tax content in the chat response itself beyond the headline number. Everything substantive lives in the brief.

---

## Section 4 — The structured question form

Per the conservative defaults rule (Section 2), every ambiguity that drove a conservative default must produce a question. Per the workflow (Section 1), the user gets exactly one round trip to answer questions. The structured question form is how those questions are presented.

**Tool preference:** Whenever a question has a small fixed set of answers (binary yes/no, single-select from 2-4 options, multi-select from a short list, ranking), **prefer the `ask_user_input_v0` tool over markdown text**. The tool renders interactive buttons that are dramatically faster to answer than typing — especially on mobile, where the user is most likely answering. Use markdown text only for free-text answers (square footage, dollar amounts, descriptive details) and for lists that don't fit the tool's constraints. The tool caps at 3 questions per call, so a long intake becomes several tool calls within the same round trip. This is fine and expected.

The intake is split into two tiers because volume matters and refusal-driven questions should come first:

### Tier 1 — Essential to start (ask before any classification or computation)

These questions determine whether the engagement can proceed at all and which content skill rules apply. Ask Tier 1 in Step 4 of the workflow, alongside the inferred profile confirmation. If any answer fires a refusal in Section 6, stop in Step 5 and refuse — do not waste the user's time on Tier 2 questions for an engagement that's about to be refused.

Tier 1 questions are nearly all binary or small single-select, so almost every question uses the interactive tool. Group them by topic into 3-question batches:

**Batch 1 — Tax year and identity**
- Tax year being prepared (single-select if multiple plausible, free text only if no inference possible)
- Entity type: bare sole proprietor / single-member LLC (single-select)
- Filing status: single / MFJ / MFS / HoH / QSS (single-select)

**Batch 2 — Scope and refusal triggers**
- State of residence at year-end (single-select if inferable, free text otherwise)
- Business activity in one sentence (free text or confirm inference)
- Multi-state business activity (Y/N — fires R-US-MULTISTATE if Y)

**Batch 3 — Refusal-trigger sweep (multi-select)**
Single multi-select question: "Tick any that apply to the taxpayer in this tax year:"
- Has employees on payroll (W-2 wages paid by the business)
- Has cryptocurrency activity (any buying, selling, mining, staking, receiving as payment)
- Has rental real estate income or property
- Has investment income beyond simple bank interest and qualified dividends from a single domestic brokerage account
- Has K-1 income from a partnership or S-corporation
- Has foreign bank accounts or foreign income
- Sold a home, business, or major asset during the year
- Got married, divorced, or experienced a death in the family during the year
- Has open IRS notices, audits, or unfiled prior-year returns
- Has any prior-year carryover (NOL, capital loss, charitable, §179, home office, §195 amortization)
- Claimed or is claiming the Employee Retention Credit
- None of the above

Any tick other than "None of the above" potentially fires a refusal in Section 6. The model checks each ticked item against the catalogue and either fires the refusal in Step 5 or, where the catalogue allows nuance (e.g., R-US-INVESTMENT-INCOME has a de minimis exception), asks a follow-up to determine which side of the threshold the situation falls on.

**Batch 4 — Engagement scope (single-select)**
- "Is this engagement scoped to Schedule C and Schedule SE only, or does it include downstream items like the QBI deduction, self-employed health insurance, retirement contribution computation, and quarterly estimated tax?"
- Options: ["Schedule C and SE only", "Full federal sole prop including downstream items", "Schedule C only, SE deferred to companion skill"]

This question determines which downstream content skills should also be loaded. If the user picks an option requiring a content skill that is not currently loaded, the model asks the user to load it before proceeding past Step 5.

### Tier 2 — Essential before delivery (ask after Tier 1 clears refusal checks)

These questions are needed to produce a non-degenerate work product but are not refusal triggers. Ask Tier 2 after Step 5 (refusal checks) clears, before Step 6 (the actual classification or computation work). The content skill specifies the exact Tier 2 questions; the base requires only that they exist and that the interactive tool is preferred where applicable.

Tier 2 questions typically include:
- Home office details (Y/N, square footage, method election)
- Vehicle details (Y/N, mileage log, business miles, total miles, first-year method election)
- Capital purchases over the de minimis threshold
- De minimis safe harbor election (Y/N)
- Contractor 1099-NEC status (W-9 collected Y/N)
- Prior-year return availability and carryovers
- 1099 forms received (for gross receipts cross-check)
- Business gifts, hobby loss history, at-risk status

Many of these are binary yes/no and use the interactive tool. The free-text ones (square footage, mileage, dollar amounts) use markdown.

### Defaults-driven questions (the original Section 4 form)

In addition to the Tier 1 and Tier 2 intake, the conservative defaults discipline (Section 2) generates its own questions during the classification work itself: any time a default is applied, a question is added to the form so the user can confirm or correct on the one round trip. These defaults-driven questions are presented at the end of the work, alongside the deliverables, and follow the same tool-preference rule.

When the volume of defaults-driven questions exceeds 10, group them by category and ask one question per category, not one per transaction. ("The 8 fuel transactions at Shell Oil totalling $X — is the vehicle..." not eight separate questions.)

Use this exact template for the defaults-driven question form (when the interactive tool isn't a fit, or as a fallback):

```markdown
## Questions for the user (one round trip)

Below are questions where the data did not give me a clear answer. I have applied the conservative default for each, but if you can confirm or correct, the reviewer's job becomes faster. **Please answer in one batch — I will not ask again.**

### Group A — High cash impact (please answer first)

1. **[Question]** [Current default applied: X. Alternative if you confirm differently: Y. Estimated tax impact of the swing: $Z.]
2. **[Question]** [Current default: X. Alternative: Y. Impact: $Z.]
[...]

### Group B — Medium cash impact

[...]

### Group C — Low cash impact, but worth confirming

[...]

### Documentation the reviewer will need (you do not need to answer these now, but please collect them for your reviewer)

- [Specific receipt 1]
- [Specific document 2]
- [...]
```

**Rules for the form (apply to both Tier 1, Tier 2, and defaults-driven):**

1. **One round trip per conversation.** Tier 1 and Tier 2 may be presented in separate batches within the round trip, but the user is not asked to come back later for more questions.
2. **Pre-fill with the model's best guess.** Every question states the current default and the alternative. Users correct anchored guesses much more readily than they generate answers from scratch.
3. **Quantify the swing on defaults-driven questions.** Every defaults-driven question includes a rough cash-impact estimate so the user knows which answers actually matter. A $5 impact and a $5,000 impact should not be presented identically.
4. **Separate user-answerable from documentation-required.** Questions only the user can answer go in the question form. Documents the reviewer needs go in a separate list at the bottom — do not pretend the user can produce them verbally.
5. **Maximum 10 defaults-driven questions across all groups.** If more than 10 defaults were applied, group them by category and ask one question per category.
6. **No questions about things the data already answered.** If the data revealed it, do not ask. Step 3 of the workflow exists to prevent this.
7. **Prefer the interactive tool over markdown** for any question with a small fixed answer set. Fall back to markdown only for free text and lists that don't fit the tool.

If you are tempted to add an eleventh defaults-driven question, ask yourself whether the cash impact justifies the user's attention. If not, apply the default and disclose. If yes, drop a lower-impact question to make room.

### Partial answer handling

If the user answers some intake questions and not others, re-ask only the unanswered ones, prioritized by impact on refusal triggers first and then by dollar magnitude. Do not start over. Do not re-ask answered questions. Do not ask all the unanswered ones at once if a Tier 1 refusal-trigger answer would change which Tier 2 questions are needed — re-ask Tier 1 missing items first, then Tier 2 if the engagement is still proceeding.

---

## Section 5 — Self-check before output

Run these seventeen checks against your draft output before sending the chat response. If any fails, fix the output and re-run. Do not deliver work product that fails any check. These checks are deterministic — they catch errors of execution, integrity, discipline, and refusal handling. They are necessary but not sufficient. They are the cheapest reliability gain in the workflow and they must all pass.

### Structural integrity checks (always run first)

**Check 1 — Tax year is stated.** The reviewer brief states the tax year explicitly in the header. Every figure in the brief is for that tax year. Cross-year figures (prior-year tax for safe harbor, prior-year carryovers) are labeled with their year.

**Check 2 — Entity type is stated and in scope.** The reviewer brief states whether the taxpayer is a bare sole prop or an SMLLC, and (if SMLLC) the state of registration. The entity type is one of the in-scope types. If it is anything else, the refusal in Section 6 should have fired in Step 5.

**Check 3 — Filing status is stated.** The reviewer brief states the filing status used for any computation that depends on it (QBI thresholds, additional Medicare tax thresholds, standard deduction). If the content skill made a default assumption because the user did not confirm, the assumption is flagged in the high-flags section.

**Check 4 — Completeness.** If the task involved transaction classification, every transaction in the input source data appears exactly once in the working paper, either classified or excluded with a reason. Count the rows in the input CSV; count the rows in Sheet "Transactions" of the workbook; they must match. If the CSV has 159 lines, Sheet "Transactions" must have 159 data rows. No silent drops.

**Check 5 — Recalc ran successfully.** If a working paper was produced, you ran `python /mnt/skills/public/xlsx/scripts/recalc.py <filename>` against it and the JSON output shows `status: success` with `total_errors: 0`. If recalc was skipped or returned errors, the working paper is not deliverable. Re-run and verify.

### Citation discipline checks

**Check 6 — Every position has a primary source citation.** For every line in the computation trail, the brief cites a primary source: an IRC section, a Treasury Regulation section, a current IRS Publication with publication number, a Revenue Procedure or Revenue Ruling number, or current Form instructions with form number and year. "IRS guidance" or "the regulations" without a section is not acceptable. Spot-check at least five citations chosen at random — they must point to identifiable primary sources.

**Check 7 — Citations are year-appropriate.** Citations to Publications, Revenue Procedures, and Form instructions reference the version applicable to the tax year being prepared, not the version current at the date of preparation. (For example, a 2025 return relies on Pub 334 for 2025, not Pub 334 for 2024.) If the content skill cannot confirm year-appropriateness, the citation includes a footnote.

**Check 8 — No invented citations.** Every citation refers to a source that actually exists. Do not cite a Revenue Procedure number that you are uncertain about. Do not cite a Treasury Reg section without confirming the section exists in the form cited. If you are unsure whether a source exists, cite the IRC section that the regulation interprets and flag for reviewer verification.

### Cross-document consistency checks

**Check 9 — Default disclosure matches working paper.** Every transaction with "Y" in column H of Sheet "Transactions" (default applied) has a corresponding line in the "Conservative defaults applied" section of the reviewer brief. Count them on both sides. They must match exactly. If the working paper has 9 defaults flagged and the brief lists 8, there is one default missing from disclosure.

**Check 10 — Question coverage.** Every ambiguity that drove a default has a corresponding question in the structured form, OR is in the "Documentation the reviewer will need" list, OR is grouped with other transactions of the same category under one question. No ambiguity item is silently absent from all three.

**Check 11 — Bottom line is consistent across documents.** The bottom-line figure in the chat response matches the bottom-line figure in the brief, which matches the supporting working paper if one exists. If they differ, fix the discrepancy before delivering.

### Conservatism, scope, and refusal checks

**Check 12 — Conservative defaults are actually conservative.** For every default applied, the chosen treatment costs the taxpayer more tax than the alternative. The "conservative" label is not used for treatments that happen to favor the taxpayer (those are not defaults, they are positions). If a default would reduce the taxpayer's tax liability, it is misclassified — fix it.

**Check 13 — Scope is respected.** No position in the brief addresses anything outside the federal sole prop scope. State income tax is not computed. Partnership-level positions are not taken. S-corp positions are not taken. Foreign positions are not taken. If the content skill produced any out-of-scope output, strip it before delivery and add a note that the out-of-scope item was refused.

**Check 14 — Refusal sweep with named codes.** The reviewer brief contains an explicit refusal trace listing every refusal R-code from this base's catalogue (Section 6) AND the content skill's catalogue, with a one-sentence note on why each was cleared for this taxpayer. The trace is verbose but it makes the refusal handling auditable rather than asserted. Without it, the reviewer has to take the model's word that the checks were done.

**Check 15 — Reviewer-actionable language.** The brief is written in language a credentialed tax professional can act on without translation. Form line references are present where the content maps to a specific line. Technical terms are used precisely. Layperson-friendly softening is absent. If any section reads like end-user documentation, rewrite it for the reviewer audience.

### Refusal discipline checks (NEW in v0.2)

**Check 16 — Refusal output is verbatim from the catalogue.** If any refusal fired during this engagement, the output text in the brief and in the chat response includes the catalogue text from Section 6 (or from the loaded content skill's topical catalogue) word-for-word, unchanged. The model may add explanation around the verbatim text — identifying which facts triggered the refusal, recommending next steps — but the catalogue text itself appears unchanged. Spot-check any refusal output against the catalogue. If the wording differs, replace with the verbatim text and re-run.

**Check 17 — No invented refusal codes.** Every refusal code that appears in the brief (in the refusal trace, the chat response, or anywhere else in the output) exists in either Section 6 of this base or in a loaded content skill's topical refusal catalogue. The model has not invented a code that does not appear in either. If the model encountered a fact pattern that looked refusable but no code matched, it used R-US-CONTENT-MISMATCH per the meta-rule in Section 6, not a fabricated code. Spot-check the refusal trace against the catalogues.

### Failure handling

If any check fails, fix the output and re-run all seventeen. Do not deliver until all seventeen pass. If a check fails twice in a row on the same item, stop and report the failure to the user explicitly rather than attempting to silently work around it — repeated failure on the same check usually indicates a deeper bug in the position that the model cannot fix on its own. In that case, refuse the position with an explanation and recommend the user consult a credentialed professional.

### Concrete recovery actions per check (NEW in v0.2)

When a self-check fails, do not attempt vague "review and improve" passes. Each check has a specific recovery action:

- **Check 1 fails (tax year missing):** Re-read the source data filename, the first transaction date, and any user statement. If still ambiguous, ask the user explicitly via the interactive tool.
- **Check 2 fails (entity type missing or out of scope):** If missing, ask the user. If out of scope, fire the appropriate refusal from Section 6 (R-US-PARTNERSHIP, R-US-S-CORP, R-US-C-CORP, or R-US-ESTATE-TRUST).
- **Check 3 fails (filing status missing):** Check the inferred profile. If not inferable, the conservative default is single (highest tax in most cases). Apply the default and add a high-impact question to the form.
- **Check 4 fails (completeness — row count mismatch):** Identify the missing transactions by row index. Compare CSV row count to Sheet "Transactions" row count and list the gap explicitly. Each missing transaction is either added with a classification or added with an exclusion reason. No silent drops permitted.
- **Check 5 fails (recalc errors):** Open the recalc JSON output, identify each cell with an error, fix the formula, re-run recalc. If the error persists after a second attempt, replace the formula with a hardcoded computation and add a reviewer attention flag explaining the workaround.
- **Check 6 fails (missing citations):** Identify each position without a citation. Add the citation from the content skill's primary source library. If no primary source is available for the position, demote it to a conservative default and add the question to the form.
- **Check 7 fails (year-inappropriate citation):** Replace the citation with the year-specific version. If the year-specific version doesn't exist or isn't known, footnote the citation with the version uncertainty.
- **Check 8 fails (invented citation):** Replace the invented cite with the IRC section that the regulation interprets, plus a footnote asking the reviewer to verify the specific Treasury Regulation cite.
- **Check 9 fails (default disclosure mismatch):** Count Y flags in column H of Sheet "Transactions" and count entries in the "Conservative defaults applied" section of the brief. Identify which side has more. Add the missing entries.
- **Check 10 fails (question coverage gap):** Identify defaults without corresponding questions. Add the questions to the form, grouped by category if needed to stay under 10.
- **Check 11 fails (bottom-line inconsistency):** Recompute the bottom line from the working paper. Update the brief and chat response to match. The working paper is the source of truth.
- **Check 12 fails (default not actually conservative):** Verify which treatment costs the taxpayer more tax. If the labeled "default" favors the taxpayer, it's a position not a default — relabel and remove from the defaults section. If it's actually conservative, the check passes.
- **Check 13 fails (out-of-scope position):** Strip the out-of-scope position from the brief. Add a note in the scope section that the item was identified but not handled. Refer to the appropriate refusal code or downstream skill.
- **Check 14 fails (refusal trace incomplete):** Regenerate the refusal trace from the catalogues directly. Walk every R-code in Section 6 of this base AND every R-code in the loaded content skills' topical catalogues. Each gets one line: cleared with reason, or fired with reason.
- **Check 15 fails (reviewer-actionable language):** Identify sections written in end-user voice. Rewrite for the reviewer audience. Add form line references where missing.
- **Check 16 fails (refusal not verbatim):** Replace the paraphrased refusal text with the exact catalogue text from Section 6 of this base or from the loaded content skill's topical catalogue. Add explanation around the verbatim text if helpful, but do not modify the verbatim text itself.
- **Check 17 fails (invented refusal code):** Identify the invented code. Replace with R-US-CONTENT-MISMATCH and explain the fact pattern in plain language. If the fact pattern is genuinely covered by an existing code that the model misremembered, replace with the correct existing code.

---

## Section 6 — Global refusal catalogue

These refusals fire at the base layer regardless of which content skill is loaded. They define the outer boundary of the product. If any refusal trigger fires, stop in Step 5 of the workflow and output the refusal verbatim. Do not partially handle a refused situation.

Each refusal has a code (R-US-XXX), a trigger condition, and an output message. The codes are referenced in the refusal trace (Check 14) so that every brief makes its refusal handling auditable.

### The verbatim rule (NEW in v0.2)

**When a refusal fires, output the refusal message text from this catalogue verbatim.** The model may add explanation, context, or recommendations *around* the verbatim text — for example, identifying which specific facts triggered the refusal, or pointing to which sentence in the catalogue applies — but the catalogue text itself must appear unchanged in the output. Paraphrasing, softening, or recombining the catalogue text is a workflow violation. Self-check 16 verifies this.

The verbatim rule exists because the catalogue language has been deliberately chosen to be precise and defensible. A reviewer reading the refusal output should see the same words every time, so they can recognize the refusal pattern at a glance and know exactly what the engagement is being declined for.

### The "no invented codes" meta-rule (NEW in v0.2)

**If a fact pattern looks like it should trigger a refusal but no code in this catalogue matches, do NOT invent a new code.** Instead, do one of the following:

1. If the situation is similar to an existing refusal but the catalogue's trigger language doesn't quite cover it, use the closest existing code and note in the explanation that the fact pattern is adjacent to but not identical to the catalogue trigger.
2. If the situation is genuinely novel and no existing code is close enough, use **R-US-CONTENT-MISMATCH** with an explanation that the engagement involves facts the loaded content skills are not authorized to handle, name what those facts are, and recommend the user consult a credentialed professional.
3. If the model is uncertain whether the fact pattern requires a refusal at all, ask the user a clarifying question rather than refusing prematurely.

The model may NOT invent a refusal code that does not appear in this catalogue or in a loaded content skill's topical catalogue. Inventing codes erodes the auditability of the refusal trace and creates the appearance that the model has access to rules it does not actually have. Self-check 17 verifies this.

### The catalogue

**R-US-PARTNERSHIP — Multi-owner business.**
Trigger: The taxpayer is a partnership, multi-member LLC that has not elected disregarded-entity treatment, joint venture treated as a partnership for tax purposes, or any entity that files Form 1065.
Output: "This product is scoped to single-owner businesses (sole proprietors and single-member LLCs treated as disregarded entities). A multi-owner business files Form 1065 and issues K-1s to its partners, which is outside the scope of this product. Please consult a CPA or Enrolled Agent who handles partnership returns."

**R-US-S-CORP — S-corporation election.**
Trigger: The taxpayer's business has elected S-corporation treatment (Form 2553 filed), files Form 1120-S, pays W-2 wages to the owner, or is described by the user as "incorporated as an S-corp."
Output: "This product is scoped to sole proprietors and single-member LLCs that are disregarded for federal tax purposes. An S-corporation files Form 1120-S, requires reasonable compensation paid to owner-employees through payroll, and has its own set of rules under subchapter S. Please consult a CPA or Enrolled Agent who handles S-corp returns."

**R-US-C-CORP — C-corporation.**
Trigger: The taxpayer's business is incorporated as a C-corporation, files Form 1120, or is described by the user as "incorporated" without S-corp election.
Output: "This product is scoped to sole proprietors and single-member LLCs that are disregarded for federal tax purposes. A C-corporation files Form 1120 and is taxed at the entity level under subchapter C. Please consult a CPA or Enrolled Agent who handles corporate returns."

**R-US-FOREIGN — Foreign income, foreign accounts, or foreign exposure.**
Trigger: Any of: the taxpayer has foreign bank accounts with aggregate balance over $10,000 at any point in the year (FBAR territory); the taxpayer has foreign income from any source; the taxpayer has foreign-domiciled investments or financial assets above the FATCA Form 8938 reporting thresholds; the taxpayer is a US person with foreign business interests; the taxpayer files Form 1040-NR (nonresident); the data shows foreign currency transactions, foreign vendor payments, or foreign client receipts.
Output: "This product is scoped to US-domestic taxpayers with no foreign exposure. Foreign income, foreign accounts, foreign assets, and nonresident filing situations involve FBAR (FinCEN Form 114), FATCA (Form 8938), foreign tax credits, treaty positions, and reporting forms that are outside this product's scope. Please consult a CPA or Enrolled Agent with international tax experience."

**R-US-CRYPTO — Cryptocurrency activity.**
Trigger: The taxpayer has bought, sold, exchanged, mined, staked, received as payment, or otherwise interacted with cryptocurrency or any digital asset during the tax year. The data shows transfers to or from any crypto exchange (Coinbase, Kraken, Gemini, Binance.US, etc.) or any wallet activity.
Output: "This product does not currently handle cryptocurrency or digital asset transactions. Crypto tax reporting involves cost basis tracking across many transactions, character determination (capital vs ordinary), and the digital asset question on Form 1040 that requires careful answering. Please consult a CPA or Enrolled Agent who handles digital asset reporting."

**R-US-RENTAL — Rental real estate.**
Trigger: The taxpayer owns rental property, has rental income reportable on Schedule E, has a short-term rental that may rise to the level of a Schedule C trade or business, or has any real estate held for production of income.
Output: "This product does not currently handle rental real estate. Rental property involves Schedule E (or Schedule C for certain short-term rentals), passive activity loss rules under §469, depreciation and depreciation recapture under §1250, the QBI safe harbor for rentals under Rev. Proc. 2019-38, and basis tracking that is outside this product's scope. Please consult a CPA or Enrolled Agent with rental real estate experience."

**R-US-INVESTMENT-INCOME — Material investment income (NEW in v0.2).**
Trigger: The taxpayer has any of: capital gains or losses requiring Schedule D; brokerage account sales requiring Form 8949; K-1 income from a partnership, S-corporation, estate, or trust; investment income approaching or exceeding the §1411 net investment income tax thresholds ($200,000 single / $250,000 MFJ MAGI); a brokerage account with active trading; mutual fund capital gain distributions other than qualified dividends; bond accrual income; PFIC holdings; investment partnership interests.
**De minimis exception:** Simple bank interest under $1,500 reported on Schedule B Part I from a single domestic checking or savings account, AND/OR qualified dividends under $1,500 from a single domestic brokerage account with no sales during the year, do NOT trigger this refusal. The reviewer can handle these items as part of the personal return without specialized investment tax expertise.
Output: "This product is scoped to taxpayers without material investment income. The taxpayer's investment activity (specify what was disclosed) brings in Schedule B, Schedule D, Form 8949 cost basis reporting, possibly Form 8960 net investment income tax under §1411, and possibly K-1s from pass-through investments — all outside the scope of this product. Please consult a CPA or Enrolled Agent who handles investment taxation alongside Schedule C and Schedule SE work."

**R-US-PRIOR-CARRYOVER — Prior-year carryovers other than NOL (NEW in v0.2).**
Trigger: The taxpayer has any prior-year carryover other than an NOL (which is covered separately by R-US-NOL), including: capital loss carryover under §1212; charitable contribution carryover under §170(d); §179 expense carryover; home office actual-method carryover under §280A(c)(5) (Form 8829 lines 43-44); §195 start-up cost amortization in progress; foreign tax credit carryover; AMT credit carryover; passive activity loss carryover under §469; investment interest expense carryover under §163(d).
Output: "This product is scoped to taxpayers without prior-year carryovers other than ordinary depreciation continuing from prior years. The carryover the taxpayer has (specify which) requires tracking from the prior-year return, application of current-year limitations, and computation of any remaining carryover to next year — all outside this product's scope. Please consult a CPA or Enrolled Agent who can review the prior-year return and properly apply the carryover."

**R-US-ESTATE-TRUST — Fiduciary capacity (NEW in v0.2).**
Trigger: The taxpayer is acting in a fiduciary capacity for an estate or trust (Form 1041), is a beneficiary receiving distributions from an estate or trust (Schedule K-1 from Form 1041), is a personal representative for a deceased taxpayer's final return, or has income reportable on a decedent's Form 1040 in respect of a decedent (IRD).
Output: "This product is scoped to individual taxpayers filing their own Form 1040 for their own active business activity. Fiduciary income tax (Form 1041), beneficiary K-1 income from estates and trusts, and decedent final returns require specialized expertise in fiduciary accounting and the ordering rules under subchapter J. Please consult a CPA, Enrolled Agent, or attorney with estate and trust tax experience."

**R-US-MULTISTATE — Multi-state business activity.**
Trigger: The taxpayer conducted business activity in more than one state during the tax year (including remote work performed from a different state than the business's home state, sales sourced to multiple states, employees in multiple states, or physical presence in multiple states).
Output: "This product is scoped to single-state taxpayers. Multi-state business activity raises questions of nexus, apportionment, sourcing, and credit-for-taxes-paid-to-other-states that vary by state and require state-specific analysis. Please consult a CPA or Enrolled Agent with multi-state experience."

**R-US-AUDIT — Open IRS notices, audit, or collection.**
Trigger: The taxpayer is currently under IRS examination (audit), has open IRS notices that have not been resolved, is in collection (CP504, LT11, LT16, etc.), has an installment agreement under negotiation, or has any unresolved correspondence with the IRS.
Output: "This product does not handle taxpayers with open IRS examinations, notices, or collection matters. Representation in IRS proceedings requires Form 2848 (Power of Attorney) and direct engagement with the IRS that is outside this product's scope. Please consult an Enrolled Agent, CPA, or tax attorney who can represent you before the IRS."

**R-US-PRIOR-UNFILED — Prior-year returns not filed.**
Trigger: The taxpayer has not filed federal income tax returns for one or more prior years that should have been filed.
Output: "This product is scoped to taxpayers who are current on their prior-year filings. Late or unfiled prior-year returns must typically be filed before the current year is addressed. Please consult an Enrolled Agent or CPA who handles back-tax compliance."

**R-US-MAJOR-LIFE-EVENT — Death, divorce, or major liquidity event in the tax year.**
Trigger: The taxpayer experienced any of: death of a spouse during the year (final joint return considerations); divorce or legal separation finalized during the year (filing status, alimony, property settlement); sale of a primary residence (§121 exclusion + recapture interactions); sale or other disposition of a business; receipt of an inheritance with income-in-respect-of-decedent components.
Output: "This product is scoped to taxpayers without major life events in the tax year. Death, divorce, home sale, business sale, and inheritances each carry their own tax rules that materially affect the return and require careful analysis. Please consult a CPA or Enrolled Agent with experience in your specific situation."

**R-US-EMPLOYEES — Business has employees on payroll.**
Trigger: The business pays one or more individuals as employees (W-2), runs payroll through any service, files Form 941 quarterly, files Form 940 annually, or has any state withholding or unemployment tax obligations.
Output: "This product is currently scoped to sole proprietors and SMLLCs without employees. Employer obligations involve quarterly Form 941, annual Form 940 (FUTA), W-2 and W-3 issuance, state withholding, state unemployment tax, and worker classification analysis that are outside this product's current scope. Contractors paid via 1099-NEC are in scope and handled separately. Please consult a CPA or Enrolled Agent who handles payroll-bearing small businesses."

**R-US-NOL — Net operating loss carryforward or carryback.**
Trigger: The taxpayer has a federal net operating loss carryforward from a prior year, or the current year produces an NOL that needs to be tracked for future years.
Output: "This product does not currently handle net operating losses. NOLs involve §172 computation, the 80% taxable income limitation, the post-TCJA elimination of carrybacks (with exceptions), and tracking across multiple years that requires careful documentation. Please consult a CPA or Enrolled Agent who handles NOL situations."

**R-US-ERTC — Employee Retention Tax Credit claims or unwind.**
Trigger: The taxpayer claimed (or is considering claiming) the Employee Retention Credit, has received an ERTC refund, or has received an IRS notice about an ERTC claim under examination.
Output: "This product does not handle ERTC claims or unwinds. The ERTC has been the subject of significant IRS enforcement activity and many claims are being examined or disallowed. Please consult an Enrolled Agent, CPA, or tax attorney who specializes in ERTC matters."

**R-US-REVIEWER-MISSING — Direct-to-taxpayer request without reviewer-in-the-loop (NEW in v0.2).**
Trigger: The user asks the model to address output to the taxpayer directly rather than to a reviewing tax professional, asks the model to "act as if I'm the taxpayer," asks the model to produce taxpayer-friendly output suitable for filing without professional review, or otherwise attempts to remove the reviewer from the loop. The trigger can fire mid-conversation if the user changes the framing after work has started.
Output: "This product is built on a load-bearing assumption: every output is reviewed and signed off by a human professional in good standing under Treasury Department Circular No. 230 — most commonly an Enrolled Agent, but a CPA or attorney is equally acceptable. The reviewer is the immediate consumer of the output, not the taxpayer. The work product is structured for someone who can independently verify positions and take professional responsibility for them. I cannot produce a taxpayer-direct version, even on request, without the reviewer-in-the-loop assumption being satisfied through some other mechanism. If you are working with a credentialed reviewer, I am happy to continue the engagement with the brief addressed to them. If you are a self-employed taxpayer trying to file your own return, please consult a CPA or Enrolled Agent — I am not designed to be the preparer of record."

**R-US-CONTENT-MISMATCH — Loaded content skill cannot serve the request, OR a fact pattern is refusable but no specific code matches.**
Trigger: Any of: the user's request requires a content skill that is not loaded; the loaded content skill explicitly refuses the situation under its topical refusal catalogue; OR the fact pattern looks refusable but no specific R-US or R-{SKILL} code in the loaded catalogues covers it (per the "no invented codes" meta-rule above).
Output: "I need a different content skill loaded to handle this request, OR the fact pattern involves [specify what] which is outside the scope of the currently loaded content skills. The loaded skills are [list]. Please [load skill name OR consult a credentialed tax professional outside the platform]." (If the content skill itself refused, output the content skill's refusal verbatim instead.)

**The catalogue is the floor.** Content skills add to this catalogue with their own topical refusals, numbered R-{SKILL}-N where SKILL is a short skill identifier and N is sequential. The refusal trace in Check 14 lists both base codes and content skill codes in order.

---

## Section 7 — Content skill slot contract

Every content skill loaded alongside this workflow base MUST provide the following. The content skill is incomplete without all of these. This base is incomplete without at least one content skill.

### Mandatory slots

1. **Scope statement.** A one-paragraph description of what tax positions the content skill covers and what it does not. The reviewer brief's scope statement is built from this.

2. **Tax year coverage.** The tax year(s) the content skill is current for. Every figure in the content skill is for a stated tax year. The skill identifies its currency date and the legislation, regulations, and guidance current as of that date.

3. **Year-specific figures table.** All dollar thresholds, rates, percentages, contribution limits, phase-out ranges, indexed figures, and form line references the content skill relies on, listed in one place with their primary source citations. Reviewers and future updaters can find every year-sensitive number in one block.

4. **Primary source library.** A list of every IRC section, Treasury Regulation, IRS Publication, Revenue Procedure, Revenue Ruling, and Form instructions cited by the content skill. Each entry includes the citation and a one-line description of what it governs. This is the source list every position in the brief must cite from.

5. **Position rules.** The actual classification, computation, or treatment rules the content skill applies. For each rule: the trigger condition (when it applies), the rule (what it does), the conservative default if data is missing, the primary source citation, and at least one worked example.

6. **Topical refusal catalogue.** Refusals on top of the base global catalogue, numbered as R-{SKILL}-N. Each refusal has the same structure as the base refusals: code, trigger, output message.

7. **Conservative defaults table.** The content skill's concrete defaults for each ambiguity type the skill handles. This is the table the brief's "Conservative defaults applied" section is built from.

8. **Reviewer attention thresholds.** The dollar thresholds at which a position becomes a reviewer attention flag regardless of certainty (e.g., any single deduction over $X, any single position with tax effect over $Y, any aggregate position over $Z). The content skill defines its own thresholds; the base requires that they exist.

9. **Worked examples.** Minimum 5 fully worked positions drawn from realistic taxpayer situations, each showing input → reasoning with citations → output. These are pattern anchors. Worked examples must be drawn from a hypothetical taxpayer, not from any real test data that will be used to validate the skill — this prevents eval contamination.

10. **Output format extension.** Any additions to the standard reviewer brief template (Section 3) that the content skill needs. The base template is the floor; content skills may add sections, never remove them.

11. **Intake form additions.** The content-skill-specific questions added to the standard intake. These are the questions the content skill needs answered that the base does not already cover.

12. **Self-check additions.** Any content-skill-specific self-checks added to Section 5 of the base. The fifteen base checks are the floor; content skills may add topical checks.

13. **Currency and revision metadata.** The content skill's version number, currency date, and a change log. When tax law changes, the content skill is updated and the version bumps. The base does not change for content updates.

### Optional slots

14. **Supporting working paper specification.** If the content skill produces a working paper (e.g., the bookkeeping skill produces an Excel workbook), the specification of that working paper's structure.

15. **Cross-skill references.** Notes on how the content skill's outputs feed other content skills (e.g., the bookkeeping skill's classified transactions feed the Schedule C/SE skill's aggregation).

16. **Sectoral notes.** Patterns specific to common sole prop business types (consultants, freelance creatives, contractors in the trades, e-commerce sellers, etc.).

If any mandatory slot is missing from a content skill, refuse to proceed and tell the user the content skill is incomplete.

---

## Section 8 — Citation discipline

Citation discipline is mandatory under this base. Every position in every brief must cite a primary source. This section defines what counts as a primary source, what does not, and how citations are formatted. This section has no analog in `vat-workflow-base` because the IRS audit standard makes citation discipline more central to US federal income tax preparation than to European VAT classification — the reviewer signs the return and is exposed to preparer penalties under §6694.

### What counts as a primary source

In descending order of authority:

1. **The Internal Revenue Code (Title 26 USC).** Cite as "IRC §X" or "IRC §X(a)(1)" with subsection and paragraph. Example: "IRC §162(a)" for the ordinary and necessary business expense rule.

2. **Treasury Regulations (26 CFR).** Cite as "Treas. Reg. §1.X-Y" with section and subsection. Example: "Treas. Reg. §1.263(a)-1(f)" for the de minimis safe harbor election. Distinguish final, temporary, and proposed regulations explicitly.

3. **Revenue Rulings.** Cite as "Rev. Rul. YYYY-N." Example: "Rev. Rul. 99-7" for commuting vs business mileage.

4. **Revenue Procedures.** Cite as "Rev. Proc. YYYY-N." Example: "Rev. Proc. 2013-13" for the simplified home office method.

5. **IRS Notices and Announcements.** Cite as "Notice YYYY-N" or "Announcement YYYY-N."

6. **IRS Publications.** Cite as "Pub X (YYYY)" with the publication number and the year of the version cited. Example: "Pub 463 (2025)" for travel, gift, and car expenses. Always cite the year-specific version.

7. **IRS Form Instructions.** Cite as "Form X Instructions (YYYY)." Example: "Schedule C Instructions (2025)."

8. **Court decisions.** Cite as the case name and citation. Example: "Welch v. Helvering, 290 U.S. 111 (1933)" for the ordinary and necessary standard.

### What does NOT count as a primary source

- "The IRS says..." without a citation
- "The regulations require..." without a section
- "Generally accepted practice..."
- A link to a tax preparation software company's blog
- A link to a tax newsletter or commentary
- An LLM's general knowledge of tax rules
- "It is well established that..."

If you cannot cite a primary source for a position, you do not have a position. Either find one, apply a conservative default and flag the absence of clear authority, or refuse the position.

### Citation format in the brief

In the computation trail and elsewhere in the brief, citations appear inline at the end of each position statement. Example:

> Home office deduction (simplified method): $1,500 (300 sq ft × $5). Source: Rev. Proc. 2013-13; Pub 587 (2025); Schedule C Instructions (2025) line 30.

When multiple sources support the same position, list them all. When a position rests on a regulation that interprets a code section, cite both. When a position is supported by guidance that may be year-specific, the year is part of the citation.

### Year-appropriateness

A 2025 return relies on guidance current as of the close of the 2025 tax year. If a regulation, ruling, or publication was modified or superseded during 2025, the brief uses the version applicable to the position being taken on the 2025 return. The content skill's currency date (slot 13 of Section 7) is the reference point.

### Uncertain citations

If you are uncertain whether a specific Revenue Procedure number, Regulation section, or Publication chapter exists in the form you are about to cite, cite the IRC section that the guidance interprets and add a footnote: "[Reviewer: please verify the specific Treasury Regulation cite for this position. The underlying statutory authority is IRC §X.]" This is preferable to inventing a cite that may not exist.

### The point of the discipline

The reviewer signs the return. The reviewer's signature exposes the reviewer to professional liability under Circular 230 and to penalties under §6694 (preparer penalties for understatements). The reviewer needs to be able to verify, in minutes, that every position the AI took rests on a real and current primary source. Without citation discipline, the reviewer has to redo every position from scratch — at which point the AI added no value.

Citation discipline is not about academic rigor. It is about making the reviewer's job possible.

---

## Section 9 — How this workflow base interacts with content skills

This base is one of two or more files that must be loaded together. The division of responsibility:

**This file (us-tax-workflow-base) owns:**
- The workflow runbook (Section 1)
- The conservative defaults principle (Section 2)
- The output specification (Section 3)
- The structured question form template and rules (Section 4)
- The fifteen self-checks (Section 5)
- The global refusal catalogue (Section 6)
- The content skill slot contract (Section 7)
- The citation discipline rule (Section 8)
- The interaction model in this section (Section 9)

**Each content skill owns:**
- Its scope statement
- Its tax year coverage and currency date
- Its year-specific figures (rates, thresholds, dollar limits, indexed figures)
- Its position rules (the actual classification, computation, or treatment logic)
- Its primary source library
- Its topical refusal catalogue (R-{SKILL}-N codes)
- Its conservative defaults table
- Its reviewer attention thresholds
- Its worked examples
- Its intake form additions
- Its self-check additions
- Any supporting working paper specification
- Its version and change log

**Conflict resolution:**

- **If a content skill says X and this base says Y about the same procedural matter:** prefer this base. The base owns workflow architecture.
- **If a content skill states a tax rule and this base is silent on it:** apply the content skill. The content skill owns tax content.
- **If two content skills conflict on a tax position:** the content skill closer to the actual form line owns the position. (E.g., if the bookkeeping skill and the Schedule C/SE skill disagree about whether a transaction goes on Line 22 or Line 27a, the Schedule C/SE skill wins because it owns Schedule C aggregation.)
- **If a content skill's topical refusal fires and a base global refusal also fires:** fire whichever is more specific. Both should appear in the refusal trace.
- **If a content skill omits a mandatory slot in Section 7:** treat the content skill as buggy and refuse to proceed.

A content skill should not redefine the workflow, the output specification, the structured question form, the self-checks, the global refusal catalogue, or the citation discipline. Those are owned by this base. If a content skill redefines them, treat the content skill as buggy and fall back to the base versions.

---

## Section 10 — Reference material

### Validation status

This file is v0.2 of `us-tax-workflow-base`, refactored from v0.1 in April 2026 after a first end-to-end test surfaced refusal-catalogue gaps and intake UX problems. v0.1 was **architecturally derived from `vat-workflow-base` v0.1**, which is in production for the Accora Malta VAT engine and has been validated against real testing with reviewer feedback. The structural patterns — the eight-step workflow, the conservative defaults discipline, the structured question form template, the self-check methodology, the reviewer brief template, the Excel working paper conventions, the refusal trace mechanism, the slot contract framework, the interaction model — are lifted from `vat-workflow-base` with US adaptations where the substantive tax mechanics require it.

v0.2 adds: (1) interactive tool integration via `ask_user_input_v0` for binary and small-set intake questions with markdown fallback for free text; (2) Tier 1 / Tier 2 intake split where Tier 1 covers refusal-trigger sweep and tax-year-essentials before any work begins, and Tier 2 covers details needed only after refusal checks clear; (3) three new global refusals (R-US-INVESTMENT-INCOME with de minimis exception, R-US-PRIOR-CARRYOVER, R-US-ESTATE-TRUST); (4) a verbatim-output rule for refusal text plus a "no invented refusal codes" meta-rule, both enforced by new self-checks 16 and 17; (5) a partial-answer handling pattern; (6) reworked Step 4 confirmation that uses the interactive tool by default.

### What is identical or near-identical to `vat-workflow-base`

- The eight-step workflow runbook structure (Section 1)
- The conservative defaults principle and four-action rule (Section 2)
- The three-output specification with Excel + brief + chat (Section 3)
- The structured question form template with high / medium / low cash impact groups, max 10 questions, and the documentation list (Section 4)
- The Excel sheet structure conventions, color coding, and recalc requirement (Section 3)
- The reviewer brief template structure (Section 3)
- The refusal trace mechanism (Section 6, Check 14)
- The slot contract framework (Section 7)
- The interaction model (Section 9)
- The reference material structure (this section)

### What diverges from `vat-workflow-base`

- **Section 2** drops the "two-tier classification rule" (Tier 1 deterministic supplier-pattern lookup vs Tier 2 ambiguous) because US Schedule C classification does not have an equivalent supplier pattern pre-classifier. The conservative defaults principle is preserved verbatim where possible. The rule is restated as "three states" (cleanly resolved, resolved with default, refused) rather than "two tiers."
- **Step 1** of the workflow asks for content skills (US-specific layer set) rather than a regional + country layer (EU-specific layer set).
- **Step 4** uses the `ask_user_input_v0` interactive tool for the profile confirmation by default, falling back to markdown only if the tool is unavailable. The VAT base does not currently use this tool.
- **Section 3** brief template adds US-specific header fields (filing status, state of residence, content skill invoked) and replaces the VAT-specific reviewer-brief framing with US tax positions while preserving the high-flags / computation-trail / defaults / documentation / refusal-trace structure.
- **Section 4** intake is split into Tier 1 (refusal-trigger sweep + essential identity, asked first) and Tier 2 (details needed only after refusal checks clear). Both tiers prefer the interactive tool over markdown for binary and small-set questions. The defaults-driven question form follows the same tool-preference rule. The VAT base uses a single intake form without tier split.
- **Section 5** self-checks: 17 instead of 14 (VAT base) or 15 (US v0.1). Citation discipline checks (6, 7, 8) are unique to the US base because US federal income tax preparation depends more heavily on primary source citation than European VAT classification does. Refusal discipline checks (16, 17) are unique to the US base, added in v0.2 after the first test surfaced hallucinated refusal codes and paraphrased refusal output. The exclusion-consistency and double-counting checks from the VAT base are folded into the completeness check (Check 4) and the conservative-defaults check (Check 12).
- **Section 6** is a global refusal catalogue (in the VAT base, refusals are delegated to the country layer; here, the base owns the global refusals because there is no "country layer" — the US is one country). Section 6 also contains the "verbatim rule" and the "no invented codes" meta-rule, both unique to the US base and added in v0.2.
- **Section 7** slot contract is restructured around content skills rather than country skills. There is no "country layer" in the US base; instead there are multiple content skills covering different parts of the federal sole prop tax picture.
- **Section 8** (citation discipline) is entirely new — no analog in the VAT base. It exists because the IRS audit standard demands it and because LLM citation hallucination is a real risk that needs an explicit mitigation.

### Origin

Architecturally lifted from `vat-workflow-base` v0.1. Content adapted for US federal income tax for sole proprietors and single-member LLCs disregarded for federal tax. The two bases share architectural DNA but are independent files — updating one does not automatically update the other. If the workflow runbook, the conservative defaults principle, or the structured question form pattern is improved in either base, the other base should be reviewed for the same improvement.

### Known gaps

1. The seventeen self-checks are deterministic but not exhaustive. They catch errors of execution, integrity, discipline, and refusal handling, not errors of conceptual understanding of substantive tax law. They are the foundation of the eval loop, not its only component.
2. The defaults-driven question form's 10-question maximum is a heuristic inherited from the VAT base, not a measured optimum for US tax intake.
3. The refusal catalogue grew in v0.2 (added R-US-INVESTMENT-INCOME, R-US-PRIOR-CARRYOVER, R-US-ESTATE-TRUST) but may still need additions as content skills are built and edge cases surface. Particular candidates for v0.3: gambling income, royalty income from passive sources, household employer situations, ministerial income, ESPP/RSU/ISO equity compensation, gig-economy 1099-K with personal-use commingling.
4. The reviewer attention threshold mechanism is delegated to content skills without a base-level minimum. May need a base floor (e.g., "any position over $5,000 is automatically flagged regardless of certainty") in v0.3.
5. The citation discipline section assumes the model can produce accurate primary source citations. This is a real risk — LLMs are known to hallucinate cites. The Section 8 instruction to flag uncertain cites and fall back to statutory authority is the mitigation, but the eval loop will need to specifically test cite accuracy.
6. No guidance yet on how content skills should handle the post-OBBBA TCJA-permanence transition. May need a transition note in v0.3.
7. The base is currently silent on how to handle a taxpayer who is in scope for some content skills but not others (e.g., a sole prop with rental property — refused for the rental piece but in scope for the Schedule C piece). Current behavior: refuse the whole engagement. May want a more nuanced approach in v0.3.
8. The R-US-CRYPTO refusal is currently a hard refusal with no de minimis exception. A single documented ETH sale on Coinbase with clean basis from a single purchase refuses the whole engagement. The conservative position is correct given the product's narrow scope, but v0.3 should reconsider whether the reviewer can handle the personal-side disposition separately while the skill stack handles Schedule C and SE.
9. The R-US-INVESTMENT-INCOME de minimis exception added in v0.2 ($1,500 simple bank interest from a single domestic account, OR $1,500 qualified dividends from a single domestic brokerage with no sales) is based on the Schedule B reporting threshold, not on testing data. May need calibration after real usage.
10. The "no invented refusal codes" meta-rule depends on the model's discipline. Self-check 17 verifies it after the fact, but does not prevent it during composition. v0.3 should consider whether the meta-rule needs additional reinforcement, possibly by listing the catalogue codes inline at the start of the refusal trace.
11. The base inherits the cautious-confirmation step (Step 4) cost of one round trip from the VAT base. v0.2 made this cheaper by using the interactive tool, but it is still a round trip. If MVP testing shows users dropping off at this step, consider an opt-out for clearly unambiguous profiles.
12. The Tier 1 / Tier 2 intake split added in v0.2 has not been tested end-to-end. The first end-to-end test in v0.1 dumped the full intake as a single markdown wall and the user answered 7 of 22 questions before giving up. v0.2 should perform better but this is unverified.

### Change log

- **v0.2 (April 2026):** Refactor after first end-to-end test. (1) Added interactive tool integration via `ask_user_input_v0` for binary and small-set questions in Step 4 confirmation and Section 4 intake, with markdown fallback. (2) Split Section 4 intake into Tier 1 (refusal-trigger sweep, asked first) and Tier 2 (details after refusal checks clear). (3) Added three global refusals: R-US-INVESTMENT-INCOME with de minimis exception, R-US-PRIOR-CARRYOVER, R-US-ESTATE-TRUST. (4) Added the verbatim-output rule and the "no invented refusal codes" meta-rule to Section 6, both enforced by new self-checks 16 and 17. Updated R-US-CONTENT-MISMATCH to absorb the meta-rule fallback case. (5) Added a partial-answer handling pattern to Section 4. (6) Updated Step 8, Section 5 intro, and failure handling to reference 17 self-checks instead of 15.
- **v0.1 (April 2026):** Initial draft. Architecturally lifted from `vat-workflow-base` v0.1 with US adaptations. Built to support content skills `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, `us-form-1040-self-employed-positions`, and `us-quarterly-estimated-tax`.

### Self-check (v0.2 of this document, not the runtime self-check in Section 5)

1. Workflow at top of file: yes (Section 1).
2. Imperatives not descriptions: yes throughout.
3. Output specification mandates Excel + reviewer brief + chat response: yes (Section 3).
4. Structured question form is a literal template: yes (Section 4) — both Tier 1/Tier 2 intake structure and the defaults-driven form template.
5. Self-check before output: yes (Section 5, seventeen checks).
6. No tax content, no rates, no thresholds, no form line references, no year-specific figures: verified.
7. Content skill slots tightened: yes (Section 7, 13 mandatory + 3 optional).
8. Inferred-profile-first ordering: yes (Step 3 before Step 4 confirmation).
9. Loading model explicit: yes (Section 9).
10. Global refusal catalogue at base layer: yes (Section 6 owns global refusals; Section 7 slot 6 requires content skills to define topical refusals).
11. Citation discipline as a first-class section: yes (Section 8).
12. Year-agnostic: verified — no year-specific figures anywhere except example "2025" used to illustrate citation format.
13. Federal-only: verified — file does not address state tax.
14. Reviewer assumed throughout: yes — every output specification, every refusal, every self-check assumes a credentialed reviewer reads the output before it reaches the taxpayer.
15. Reference material at bottom: yes (Section 10).
16. Architectural lineage to `vat-workflow-base` documented: yes (this section).
17. Interactive tool preference documented for both Step 4 and Section 4 intake: yes (added in v0.2).
18. Verbatim refusal rule and "no invented codes" meta-rule documented: yes (Section 6 introduction, added in v0.2).
19. New refusals R-US-INVESTMENT-INCOME, R-US-PRIOR-CARRYOVER, R-US-ESTATE-TRUST present in Section 6: yes (added in v0.2).
20. New self-checks 16 and 17 present in Section 5: yes (added in v0.2).
21. All counts updated from "fifteen" to "seventeen" throughout (Step 8, Section 5 intro, failure handling, document self-check): yes (verified in v0.2).

## End of US Tax Workflow Base Skill v0.1

This base is incomplete without at least one content skill loaded alongside it. If you are reading this without any content skill loaded, ask the user which task they are working on (bookkeeping classification, Schedule C and SE computation, federal 1040 positions like QBI, or quarterly estimated tax) and refuse to proceed until the appropriate content skill is loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
