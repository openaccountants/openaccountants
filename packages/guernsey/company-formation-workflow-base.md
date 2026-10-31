---
name: company-formation-workflow-base
description: Universal company formation and entity selection workflow base that defines the entity comparison, registration checklist, and ongoing compliance runbook for all jurisdictions. Contains no jurisdiction-specific content — no entity type names, no registration fees, no filing portals. This skill MUST be loaded alongside a country-specific formation skill that provides the entity types, registration authorities, and local requirements. This skill alone cannot produce any output.
version: 1.0
category: foundation
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# Company Formation Workflow Base Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a company formation advisory task: the order of operations, how to compare entity types, how to build a registration checklist, how to identify ongoing compliance obligations, what to produce as output, what to check before delivering. It contains no entity type names, no registration fees, no share capital requirements, no filing portals, no notary fee schedules, no specific tax rates.

**This file must always be loaded with a country-specific formation skill** that provides the available entity types, registration authorities, capital requirements, and local compliance rules (e.g., `uk-formation`, `au-formation`, `de-formation`). This file alone cannot produce an entity comparison, a registration checklist, or a compliance calendar. Loading it without a companion is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a country formation skill says it conforms to v1.0 of this base, it means: it fills the country slots specified in Section 5, it produces outputs in the format specified in Section 3, its recommendations can be validated by the self-checks in Section 4, and it participates in the workflow in Section 1.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping a business owner or entrepreneur choose an entity type, understand the registration process, and plan for ongoing compliance obligations. The output will be reviewed by a qualified professional (solicitor, accountant, or formation agent) before any filings are made. Your job is to do the structured comparison and produce a clear, actionable checklist plus a reviewer brief that makes the professional's job fast and accurate.

Execute these seven steps in order. Do not skip. Do not reorder. Do not recommend an entity type before step 3. Do not build any output files before step 6.

### Step 1 — Confirm the companion skills are loaded

This workflow base requires a country-specific formation skill providing the entity types, registration authorities, capital requirements, and compliance obligations for the target jurisdiction.

If no country-specific skill is loaded, stop and tell the user: "I need a country-specific company formation skill loaded alongside this workflow base. Which jurisdiction are you forming the entity in?" Do not proceed without it.

If a bookkeeping or tax skill is also loaded for the same jurisdiction, note its presence — the tax treatment comparison in Step 3 can reference the tax skill's rates, and the ongoing compliance calendar in Step 6 can cross-reference the bookkeeping skill's reporting requirements.

### Step 2 — Determine the client situation

The user will describe their situation in free text. Extract and confirm:

- **Purpose of formation.** New business, restructuring, foreign expansion (branch vs. subsidiary), holding structure, or special-purpose vehicle?
- **Number of founders/owners.** Single owner, partners, or multiple shareholders? This eliminates entity types with minimum member requirements.
- **Planned activities.** Some activities require specific entity types or licenses.
- **Liability concerns.** Does the owner want personal liability protection? Primary driver for most decisions.
- **Expected revenue and profit range.** Determines whether corporate administrative burden is justified.
- **Employees.** Hiring immediately or operating solo initially?
- **Funding.** Self-funded, bank loan, or external investors? External investment typically requires transferable shares.
- **International dimension.** Cross-border operations, foreign assets, or non-resident owners?
- **Timeline.** When must the entity be operational? Some structures take weeks; others are same-day.

Present the extracted situation to the user:

> "Here is what I understand about your situation:
>
> [One paragraph covering all nine points above.]
>
> Is this correct? If anything is wrong, tell me and I will adjust before I start comparing entity types."

Wait for confirmation.

### Step 3 — Entity type selection

Using the country skill's entity type catalogue, present a structured comparison of the entity types that are compatible with the user's confirmed situation. Eliminate obviously unsuitable types first (e.g., do not present a public limited company to a solo founder with no external investors; do not present a sole trader to someone explicitly seeking liability protection).

For each remaining entity type, compare across the dimensions in Section 2 (the entity comparison framework). Present the comparison as a side-by-side table per the output specification in Section 3.

After the table, provide a recommendation:

> "Based on your situation, [entity type] appears to be the best fit because [one-sentence reason]. The key trade-off is [one-sentence trade-off]. [Entity type 2] would be worth considering if [one-sentence condition]."

The recommendation is advisory — the reviewer and the user make the final decision. State this explicitly.

Wait for the user to confirm the entity type before proceeding to Step 4.

### Step 4 — Registration checklist

For the selected entity type, produce a step-by-step registration checklist using the country skill's registration requirements. For each step:

- What to do (the specific action)
- Where to do it (the authority, website, or office)
- What documents or information are needed
- Estimated time to complete
- Estimated cost (fees payable to the authority)
- Dependencies (which prior steps must be complete first)

The checklist must cover all of the following registration streams (where applicable to the entity type):

1. **Company register / business register.** Name reservation, founding documents, registration filing, obtaining the company number.
2. **Tax authority.** Corporate/income tax registration, obtaining the tax identification number.
3. **VAT / GST registration.** Mandatory (above threshold), voluntary, or not applicable. Flag if expected revenue is near the threshold.
4. **Social security / employer registration.** If the entity will have employees, register with the relevant social security or labor authority.
5. **Local or municipal registration.** Business license, trade license, or local authority notification if required.
6. **Bank account.** Opening a business bank account. Note typical document requirements.
7. **Professional or activity-specific licenses.** Per the country skill, list the licensing body and requirements.
8. **Data protection registration.** If the jurisdiction requires registration with a data protection authority.

Order the steps in the sequence they should be completed, respecting dependencies. Flag any steps that can be done in parallel.

### Step 5 — Capital requirements and costs

Produce a cost breakdown covering:

**One-time formation costs:**
- Minimum share capital or equity requirement (if any) per the country skill
- Registration fees payable to the company register
- Notary fees (if notarization is required for founding documents)
- Legal fees (estimated range for standard formation)
- Accounting setup fees (estimated range)
- Any mandatory publications (e.g., gazette notices)
- License fees (if applicable)

**Annual ongoing costs:**
- Annual return / confirmation statement filing fee
- Registered office or registered agent fee (if required)
- Statutory audit fees (if the entity exceeds audit thresholds or audit is mandatory)
- Annual license renewal fees (if applicable)
- Minimum tax payments (some jurisdictions impose minimum corporate tax regardless of profit)

Present both as a clear cost table per Section 3. Distinguish between mandatory costs (cannot be avoided) and estimated professional fees (which vary by provider). Where the country skill provides fee ranges, use them. Where it provides fixed statutory fees, state the exact amount.

### Step 6 — Ongoing compliance obligations

Produce a first-year compliance calendar: for every recurring obligation the new entity will have, list:

- What to file or do
- The authority or body it is filed with
- The frequency (one-off, monthly, quarterly, annual)
- The deadline (absolute date or rule-based, e.g., "within 9 months of year-end")
- The penalty for late filing (if specified by the country skill)
- Whether a professional is typically required (e.g., statutory audit vs. self-filed returns)

Group obligations by category:

1. **Company law obligations** — annual returns, confirmation statements, filing of accounts, director disclosures, maintaining registers
2. **Tax obligations** — corporate tax returns, estimated tax payments, VAT returns (if registered), payroll tax returns (if employer)
3. **Employment obligations** — payroll reporting, social security returns, workplace pension obligations
4. **Other obligations** — data protection renewals, industry-specific reporting, beneficial ownership registers

For the first year specifically, note any one-off obligations that only apply in the formation year (e.g., first accounts period may be longer than 12 months, initial registration filings with specific bodies).

### Step 7 — Produce outputs and deliver

Produce the five output artefacts specified in Section 3. Run the self-checks in Section 4 against all outputs. If any check fails, fix and re-run. Only present outputs to the user when all checks pass.

Write a short closing chat response:

- The recommended entity type and the one-sentence reason
- One sentence on what each output contains
- The single most important next step for the user
- An invitation to revise: "If your situation changes or you want to explore a different entity type, tell me and I'll regenerate the comparison."

---

## Section 2 — Entity comparison framework

When comparing entity types in Step 3, evaluate each type across these dimensions. The country skill provides the values; this section provides the framework.

### Liability protection

- **Full protection.** The owner's personal assets are separate from the business. Liability is limited to the owner's investment in the business. (Typical of: limited companies, corporations.)
- **Partial protection.** Some partners have limited liability; at least one has unlimited liability. (Typical of: limited partnerships.)
- **No protection.** The owner is personally liable for all business debts. (Typical of: sole traders, general partnerships.)

Note: liability protection can be pierced in fraud or certain statutory circumstances. State the general position; do not overstate the protection.

### Tax treatment

- **Separate entity taxation.** The business is taxed as a separate legal person. Profits are taxed at the corporate rate; distributions to owners are taxed again (potential double taxation). (Typical of: limited companies, corporations.)
- **Pass-through taxation.** The business's income flows through to the owner's personal tax return. No separate entity tax, but the owner pays personal tax on all business profits. (Typical of: sole traders, partnerships, LLCs in some jurisdictions.)
- **Hybrid or elective.** The entity can choose its tax treatment. (Typical of: US LLCs, some European forms.)

The country skill specifies which entity types fall into which category and the applicable rates. Reference the tax skill if loaded.

### Administrative burden

Rate as low, medium, or high based on the country skill's assessment:

- **Low.** Minimal filing requirements, no mandatory audit, simple accounts. (Typical of: sole traders.)
- **Medium.** Annual return and accounts filing, basic bookkeeping requirements, but no mandatory audit below a threshold. (Typical of: small limited companies.)
- **High.** Mandatory audit, detailed annual accounts, board resolutions, shareholder meetings, extensive disclosure. (Typical of: large companies, public companies.)

### Capital requirements

- Minimum share capital or equity requirement
- Whether the capital must be paid up on formation or can be called over time
- Whether non-cash contributions are permitted (and whether they require valuation)

### Transferability

- How ownership interests are transferred (share transfer, assignment of partnership interest, sale of business as a whole)
- Whether transfer requires consent of other owners
- Whether the entity can issue new ownership interests to raise capital
- Implications for succession planning

### Number of owners

- Minimum and maximum number of owners permitted
- Whether a single person can form and own the entity
- Requirements for directors, officers, or managing partners separate from owners

---

## Section 3 — Output specification

Five outputs per formation advisory engagement. All five are mandatory. Never produce one without the others.

### Output 1 — Entity comparison table

Side-by-side comparison of the entity types suitable for the user's situation:

| Dimension | [Entity Type 1] | [Entity Type 2] | [Entity Type 3] |
|---|---|---|---|
| Liability protection | [value] | [value] | [value] |
| Tax treatment | [value] | [value] | [value] |
| Administrative burden | [value] | [value] | [value] |
| Minimum capital | [value] | [value] | [value] |
| Transferability | [value] | [value] | [value] |
| Min/max owners | [value] | [value] | [value] |
| Formation time | [value] | [value] | [value] |
| Formation cost (est.) | [value] | [value] | [value] |
| Annual cost (est.) | [value] | [value] | [value] |

Include only entity types that passed the initial filter in Step 3. Do not pad the table with obviously unsuitable options.

### Output 2 — Registration step-by-step checklist

Numbered list with sub-items, per Step 4's structure. Each step includes the action, authority, documents needed, estimated time, estimated cost, and dependencies. Steps are sequenced in order of execution. Parallel steps are marked.

### Output 3 — Cost breakdown

Two tables:

**Table A — One-time formation costs:**

| Item | Amount | Notes |
|---|---|---|
| [Registration fee] | [amount] | [statutory / estimated] |
| ... | | |
| **Total one-time costs** | **[amount]** | |

**Table B — Annual ongoing costs:**

| Item | Amount | Frequency | Notes |
|---|---|---|---|
| [Annual return fee] | [amount] | Annual | [statutory / estimated] |
| ... | | | |
| **Total annual costs** | **[amount]** | | |

Distinguish statutory fees (fixed, known) from professional fees (estimated ranges).

### Output 4 — First-year compliance calendar

Chronological list of all filings and obligations in the first 12-18 months after formation:

| Date / Deadline | Obligation | Authority | Penalty if late | Professional needed? |
|---|---|---|---|---|
| [Formation + X days] | [obligation] | [authority] | [penalty] | [Yes/No] |
| ... | | | | |

Include both one-off formation-year obligations and the first occurrence of each recurring obligation.

### Output 5 — Reviewer brief

```markdown
# [Country] Company Formation — Reviewer Brief
**Client situation:** [one-sentence summary]
**Recommended entity type:** [type]
**Generated:** [date]

## Summary
- Entity types compared: [count]
- Recommended: [type] — [one-sentence reason]
- Alternative: [type] — [one-sentence condition under which this is better]
- Estimated total formation cost: [amount range]
- Estimated annual ongoing cost: [amount range]
- Key first-year deadlines: [count]

## Recommendation rationale
[Two to three sentences: why this entity type fits the client's stated
situation, what the primary trade-off is, and what circumstance would
change the recommendation.]

## Assumptions made
[For each assumption about the client's situation that affected the
recommendation: the assumption, what it affects, and what changes if
the assumption is wrong.]

## Items the reviewer should verify
[Specific items: whether the client qualifies for the recommended entity
type, whether any planned activities require additional licenses, whether
non-resident ownership creates complications, whether the capital
requirements are achievable. Not generic "verify everything."]

## Risks and caveats
[Numbered list: specific risks the client should be aware of. Personal
guarantee requirements, director liability exposures, ongoing filing
obligations that carry penalties, audit thresholds that may be
triggered by growth.]
```

---

## Section 4 — Self-checks (run before delivering output)

Run these ten checks against all outputs. If any fails, fix and re-run. Do not deliver until all pass.

### Completeness

**Check 1 — All entity types covered.** Every entity type from the country skill's catalogue that is compatible with the user's situation appears in the comparison table. No eligible type is silently omitted.

**Check 2 — All comparison dimensions populated.** Every cell in the entity comparison table has a value. No dimension is left blank for any entity type.

**Check 3 — Registration checklist covers all streams.** The registration checklist addresses every applicable registration stream from Step 4 (company register, tax authority, VAT, employer registration, local registration, bank account, licenses, data protection). Streams that do not apply to the selected entity type are explicitly noted as not applicable with a reason.

**Check 4 — Cost breakdown includes all mandatory fees.** Every statutory fee from the country skill's fee schedule appears in the cost breakdown. No mandatory cost is omitted. Estimated professional fees are clearly labelled as estimates.

### Consistency

**Check 5 — Recommendation matches comparison.** The recommended entity type in the reviewer brief is one of the types in the comparison table, and the stated reason is consistent with the comparison data. If the comparison shows Entity A has lower cost and lower administrative burden than Entity B, the recommendation should not favor Entity B without an explicit reason.

**Check 6 — Calendar matches checklist.** Every filing obligation mentioned in the registration checklist appears in the compliance calendar with a specific deadline. Every recurring obligation from Step 6 appears. No obligation exists in one output but not the other.

**Check 7 — Costs are consistent.** Formation costs in the cost breakdown match the costs mentioned in the registration checklist. Annual costs in the cost breakdown match the ongoing obligations in the compliance calendar. No amount appears in one output at a different figure than another.

### Accuracy

**Check 8 — No jurisdiction-specific content from this base.** Verify that all entity type names, fee amounts, filing deadlines, authority names, and legal requirements come from the country skill, not from this workflow base. This base provides the framework; the country skill provides the content. If any specific amount or name appears that is not sourced from the country skill, it is an error.

**Check 9 — Entity types correctly eliminated.** Every entity type excluded from the comparison table was excluded for a valid reason based on the user's confirmed situation. If a sole trader is excluded because the user requested liability protection, that is valid. If a partnership is excluded for no stated reason, that is an error.

**Check 10 — Tier 2/3 disclosure complete.** Every assumption or user-answered question that affected the recommendation is documented in the reviewer brief. No assumption is silently embedded in the outputs without disclosure.

### Failure handling

If any check fails, fix the output and re-run all ten. Do not deliver until all pass. If a check fails twice in a row on the same item, stop and report the failure to the user.

---

## Section 5 — Country skill contract

Every country-specific formation skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Entity type catalogue** — complete list of available entity types. For each: legal name (local language and English), governing legislation, min/max owners, liability treatment, tax treatment, minimum capital, audit requirements, and typical formation time.
2. **Registration authorities** — for each stream (company register, tax, VAT, employer, local licenses): authority name, website, and registration process summary.
3. **Fee schedule** — statutory formation fees (registration, name reservation, notary, gazette publication) and annual fees (annual return, registered office, audit thresholds).
4. **Founding document requirements** — required documents per entity type, notarization requirements, availability of standard templates.
5. **Capital rules** — minimum share capital per entity type, paid-up requirements, non-cash contribution rules and valuation requirements.
6. **Ongoing compliance obligations** — for each entity type: recurring filings (annual return, accounts, tax, payroll, VAT), filing body, frequency, deadline, and late-filing penalty.
7. **Director and officer requirements** — minimum directors, residency requirements, company secretary, disqualification rules.
8. **Beneficial ownership registration** — register availability, filing requirements, and deadline.
9. **VAT/GST registration threshold** — mandatory threshold and voluntary registration option.
10. **Audit thresholds** — criteria (revenue, balance sheet, employees) for mandatory statutory audit.

### Optional slots

11. **Industry-specific entity types** — special-purpose vehicles, professional corporations, cooperative societies, or other entity types specific to certain activities.
12. **Foreign owner considerations** — additional requirements or restrictions for entities with non-resident owners or directors, including apostille requirements, local representative requirements, and tax treaty implications.
13. **Integration notes** — how the formation skill interacts with the country's bookkeeping, tax, or payroll skills if loaded simultaneously.

---

## Section 6 — Reference material

### Validation status

This file is v1.0 of `company-formation-workflow-base`, drafted as part of the Open Accountants skill architecture in May 2026. It follows the structural pattern established by `bookkeeping-workflow-base` v1.0.

### Design decisions

1. **Advisory, not filing.** This workflow produces a comparison and checklist for professional review. It does not file anything — formation filings are high-stakes and often require identity verification that an AI cannot perform.

2. **Three-step confirmation.** Three user checkpoints (situation, entity type, final delivery) prevent wasted work from misunderstood situations.

3. **First-year calendar, not perpetual.** Covers 12-18 months — the critical period. Ongoing calendars are the domain of bookkeeping and tax skills.

4. **Cost ranges, not quotes.** Professional fees are ranges; statutory fees are exact amounts. The distinction is always explicit.

### Known gaps

1. Cross-border formation is acknowledged in Step 2 but not deeply specified.
2. Group structures (parent-subsidiary, holding companies) are not covered.
3. Post-formation share issuance, transfers, and restructuring are not in scope.
4. IP holding structures and TP implications are not addressed (see transfer-pricing-workflow-base).
5. Regulatory licensing detail is delegated entirely to the country skill.

### Change log

- **v1.0 (May 2026):** Initial release. Establishes the universal company formation workflow, entity comparison framework, five-output specification, 10 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
