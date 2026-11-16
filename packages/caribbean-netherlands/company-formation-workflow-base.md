---
name: company-formation-workflow-base
description: "Shared 2026 entity-selection and company-formation preparation method: confirm owners/activity and jurisdictions, compare legal/tax forms, sequence identity and registration steps, separate capital from costs, and build a first-year compliance handoff. Includes a bounded UK private-company application. Actual country/entity law, fees, licensing, tax and identity requirements remain necessary; no registrations or filings are performed."
version: 1.1
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-11-14
tax_year: 2026
type: cross-country-method
tier: 2
domain: formation
---

# Company Formation Workflow Base Skill v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a company formation advisory task: the order of operations, how to compare entity types, how to build a registration checklist, how to identify ongoing compliance obligations, what to produce as output, what to check before delivering. It supplies no worldwide entity catalogue, notary fee schedule or tax rate. The bounded UK application illustrates the workflow; other country/entity requirements must come from actually read current official rules.

**This file must always be loaded with a country-specific formation skill** that provides the available entity types, registration authorities, capital requirements, and local compliance rules (e.g., `uk-formation`, `au-formation`, `de-formation`). Without the actual country/entity rules, Claude must not label a comparison, checklist or calendar complete. Safe intake, evidence inventory and a provisional task list can still be prepared, identifying missing rules instead of refusing all useful work or inventing requirements.

**This file is the contract.** When a country formation skill says it conforms to v1.1 of this base, it means: it fills the country slots specified in Section 5, it produces outputs in the format specified in Section 3, its recommendations can be validated by the self-checks in Section 4, and it participates in the workflow in Section 1.

---

## Ask the client first

Read the existing client record and supplied documents first. Confirm proposed legal and operating jurisdictions/activity; founders, beneficial owners and director roles/residence; intended funding, ownership/rights and capital; liability/guarantee needs and investor plans; expected turnover/profit/staff and start date; existing branches/entities, licensing and tax registrations. Use the original detailed nine-point profile below, asking only for missing facts. Do not request passwords, personal verification codes or unnecessary identity documents in the chat.

## The method, step by step

You are helping a business owner or entrepreneur choose an entity type, understand the registration process, and plan for ongoing compliance obligations. The output will be reviewed by a qualified professional (solicitor, accountant, or formation agent) before any filings are made. Your job is to do the structured comparison and produce a clear, actionable checklist plus a reviewer brief that makes the professional's job fast and accurate.

Execute these seven steps in order. Do not skip. Do not reorder. Do not recommend an entity type before step 3. The Step 4 checklist and Step 5 cost schedule may be drafted during those steps; finalise the five-part pack after Step 6. This is preparation, not authority to submit registrations, identity checks or payments.

### Step 1 : Confirm the companion skills are loaded

This workflow base requires a country-specific formation skill providing the entity types, registration authorities, capital requirements, and compliance obligations for the target jurisdiction.

If the companion is missing, search the current available catalogue using known country/entity facts. Ask only for the missing jurisdiction. Continue intake and a provisional source-gap register; hold recommendations or final deadlines/fees that depend on missing rules. Read each companion's actual version/date/approval rather than assuming approval from the author or this base.

If a bookkeeping or tax skill is also loaded for the same jurisdiction, note its presence : the tax treatment comparison in Step 3 can reference the tax skill's rates, and the ongoing compliance calendar in Step 6 can cross-reference the bookkeeping skill's reporting requirements.

### Step 2 : Determine the client situation

The user will describe their situation in free text. Extract and confirm:

- **Purpose of formation.** New business, restructuring, foreign expansion (branch vs. subsidiary), holding structure, or special-purpose vehicle?
- **Number of founders/owners.** Single owner, partners, or multiple shareholders? This eliminates entity types with minimum member requirements.
- **Planned activities.** Some activities require specific entity types or licenses.
- **Liability concerns.** Does the owner want personal liability protection? Primary driver for most decisions.
- **Expected revenue and profit range.** Determines whether corporate administrative burden is justified.
- **Employees.** Hiring immediately or operating solo initially?
- **Funding.** Self-funded, loan, equity/convertible or other investor funding? Establish actual instrument, investor eligibility and transfer/consent rights; external investment does not universally require freely transferable shares.
- **International dimension.** Cross-border operations/assets, non-resident owners/directors, place of management, employees and existing entities? Incorporation jurisdiction alone does not determine tax residence, permanent establishment, withholding, social security or personal residence.
- **Timeline.** When must the entity be operational? Some structures take weeks; others are same-day.

Present the extracted situation to the user:

> "Here is what I understand about your situation:
>
> [One paragraph covering all nine points above.]
>
> Is this correct? If anything is wrong, tell me and I will adjust before I start comparing entity types."

Wait for confirmation.

### Step 3 : Entity type selection

Using the country skill's entity type catalogue, present a structured comparison of the entity types that are compatible with the user's confirmed situation. Filter actual legal eligibility first, recording country rule and confirmed fact. Separately rank commercial suitability. Do not treat a public-company option as legally unavailable merely because the founder is solo, or promise a sole-trader form meets a request for limited liability. Preserve excluded options and reasons in the review record.

For each remaining entity type, compare across the dimensions in Section 2 (the entity comparison framework). Present the comparison as a side-by-side table per the output specification in Section 3.

After the table, provide a recommendation:

> "Based on your situation, [entity type] appears to be the best fit because [one-sentence reason]. The key trade-off is [one-sentence trade-off]. [Entity type 2] would be worth considering if [one-sentence condition]."

The recommendation is advisory : the reviewer and the user make the final decision. State this explicitly.

Wait for the user to confirm the entity type before proceeding to Step 4.

### Step 4 : Registration checklist

For the selected entity type, produce a step-by-step registration checklist using the country skill's registration requirements. For each step:

- What to do (the specific action)
- Where to do it (the authority, website, or office)
- What documents or information are needed
- Estimated time to complete
- Estimated cost (fees payable to the authority)
- Dependencies (which prior steps must be complete first)

The checklist must cover all of the following registration streams (where applicable to the entity type):

1. **Company/business register.** Confirm name/address/email, actual legal form, founders/directors, constitutional documents, capital statement and filing channel; determine identity-verification and beneficial-ownership steps/deadlines separately. Obtain actual acceptance/certificate/company number, not merely an application reference.
2. **Tax authority.** Corporate/income tax registration, obtaining the tax identification number.
3. **VAT / GST registration.** Test the actual country/person/supply/place rules, threshold measurement, non-established or other no-threshold obligations, exemptions and permitted voluntary registration. Near-threshold turnover is only one trigger; company incorporation does not itself prove registration is required or complete.
4. **Social security / employer registration.** If the entity will have employees, register with the relevant social security or labor authority.
5. **Local or municipal registration.** Business license, trade license, or local authority notification if required.
6. **Bank account.** Obtain actual bank eligibility, KYC/beneficial-owner and source-of-funds requirements and, where applicable, capital-deposit evidence. Opening or approval is not guaranteed by incorporation. Do not invent a universal requirement that bank approval precedes every registration.
7. **Professional or activity-specific licenses.** Per the country skill, list the licensing body and requirements.
8. **Data protection registration.** If the jurisdiction requires registration with a data protection authority.

Order the steps in the sequence they should be completed, respecting dependencies. Flag any steps that can be done in parallel.

### Step 5 : Capital requirements and costs

Produce a cost breakdown covering:

**One-time formation costs:**
- Required/subscribed/paid-up capital, premium or permitted non-cash contribution, kept as a funding/liquidity line rather than a consumed formation fee; record unpaid commitment and any deposit/withdrawal restrictions
- Registration fees payable to the company register
- Notary fees (if notarization is required for founding documents)
- Legal fees only from an actual scoped quote or clearly stated client planning assumption, with taxes/disbursements and validity; do not invent a market range
- Accounting setup fees from an actual scoped quote or clearly stated planning assumption; otherwise unknown
- Any mandatory publications (e.g., gazette notices)
- License fees (if applicable)

**Annual ongoing costs:**
- Annual return / confirmation statement filing fee
- Registered office or registered agent fee (if required)
- Actual audit requirement and any available exemption, including entity, group, regulated/public-interest and member-request conditions; auditor fee from a quote, not inferred from a turnover threshold alone
- Annual license renewal fees (if applicable)
- Minimum tax payments (some jurisdictions impose minimum corporate tax regardless of profit)

Present both as a clear cost table per Section 3. Distinguish between mandatory costs (cannot be avoided) and estimated professional fees (which vary by provider). For statutory fees use the actual current official channel/date/currency, applicable tax, concessions and filing frequency. For professional/agent/bank/address services use an actual quote or explicit client-supplied assumption, not a country skill's unsupported market range. Separate sunk fees, refundable deposits, paid capital and ongoing working capital; do not add capital to an expense total or promise it can be withdrawn freely.

### Step 6 : Ongoing compliance obligations

Produce a first-year compliance calendar: for every recurring obligation the new entity will have, list:

- What to file or do
- The authority or body it is filed with
- The frequency (one-off, monthly, quarterly, annual)
- The actual deadline and triggering event, accounting/tax period, channel, weekend/holiday rule and exception; a sample months-after-year-end phrase is not a worldwide rule
- The penalty for late filing (if specified by the country skill)
- Whether a professional is typically required (e.g., statutory audit vs. self-filed returns)

Group obligations by category:

1. **Company law obligations** : annual returns, confirmation statements, filing of accounts, director disclosures, maintaining registers
2. **Tax obligations** : corporate tax returns, estimated tax payments, VAT returns (if registered), payroll tax returns (if employer)
3. **Employment obligations** : payroll reporting, social security returns, workplace pension obligations
4. **Other obligations** : data protection renewals, industry-specific reporting, beneficial ownership registers

For the first year distinguish incorporation, trading commencement, accounting reference period and tax accounting periods. Accounts may cover a longer period while a tax return may not, creating separate returns/payment dates. Also track initial identity/beneficial-owner and other one-off filings. Use actual deadlines and approved extensions, not the same anniversary for every task. [UK first accounts and tax returns](https://www.gov.uk/first-company-accounts-and-return).

### Step 7 : Produce outputs and deliver

Produce the five output artefacts specified in Section 3. Run the self-checks in Section 4 against all outputs. If any check fails, fix and re-run. Only describe the pack as ready when all applicable checks pass. An exception draft can show unresolved facts/sources and exact failed checks without pretending it is complete. No incorporation, tax registration, bank application, identity declaration or payment is submitted by delivering this pack.

Write a short closing chat response:

- The recommended entity type and the one-sentence reason
- One sentence on what each output contains
- The single most important next step for the user
- An invitation to revise: "If your situation changes or you want to explore a different entity type, tell me and I'll regenerate the comparison."

---

## Section 2 : Entity comparison framework

When comparing entity types in Step 3, evaluate each type across these dimensions. The country skill provides the values; this section provides the framework.

### Liability protection

- **Limited-liability form.** Establish the actual entity's legal separation, share/guarantee commitment including unpaid capital and any personal guarantee, director/statutory or misconduct exposure. Do not call it full personal-asset protection. For example, UK share terms can leave unpaid obligations; director responsibility remains even when an accountant handles filings. [UK shares](https://www.gov.uk/limited-company-formation/shareholders), [director duties](https://www.gov.uk/running-a-limited-company).
- **Mixed/conditional liability.** Identify each general/limited/managing partner's actual liability, management conditions and guarantees under the country/entity law; do not apply one partner's protection to every owner.
- **Unlimited-liability form.** Confirm the actual proprietor/partner exposure and joint/several rules, rather than assuming a trading name creates legal separation or every debt category has identical enforcement.

Note: liability protection can be pierced in fraud or certain statutory circumstances. State the general position; do not overstate the protection.

### Tax treatment

- **Separate entity taxation.** Establish corporate tax base/rates, exemptions/credits and owner-level salary/distribution/capital treatment. A separate legal person does not by itself prove every profit/distribution is taxed twice; test actual residence, relief and election conditions.
- **Transparent/pass-through treatment.** Establish the actual tax classification for each tax/jurisdiction and partner/owner, income allocation, return/payment/withholding and other entity-level charges. Transparency for one income tax does not establish no separate tax, VAT, payroll or filing obligation.
- **Hybrid/elective treatment.** Confirm available election, eligible owners, timing/consent, default classification, consequences and cross-country mismatch; no worldwide right to choose a preferred tax result.

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

## Section 3 : Output specification

For a complete formation comparison/checklist engagement provide the five linked outputs below, or identify which are incomplete and why. A narrower diagnostic request can return its requested working paper without claiming a full formation pack.

### Output 1 : Entity comparison table

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

### Output 2 : Registration step-by-step checklist

Numbered list with sub-items, per Step 4's structure. Each step includes the action, authority, documents needed, estimated time, estimated cost, and dependencies. Steps are sequenced in order of execution. Parallel steps are marked.

### Output 3 : Cost breakdown

Two tables:

**Table A : One-time formation costs:**

| Item | Confirmed cost and evidence | Notes |
|---|---|---|
| [Registration fee] | [amount] | [statutory / estimated] |
| ... | | |
| **Total one-time costs** | **[amount]** | |

**Table B : Annual ongoing costs:**

| Item | Confirmed cost and evidence | Frequency | Notes |
|---|---|---|---|
| [Annual return fee] | [amount] | Annual | [statutory / estimated] |
| ... | | | |
| **Total annual costs** | **[amount]** | | |

Every statutory-fee row carries its actual official URL, read date and channel; every professional-fee row names the actual quote/source and its scope, tax and validity. An unknown figure stays unknown and is excluded from any claimed complete total. Present capital/deposits in a separate funding schedule, without relabelling them as costs.

### Output 4 : First-year compliance calendar

Chronological list for the initial 12 to 18 month planning window, also retaining every first-cycle deadline beyond that window, with its actual date/trigger and an out-of-window flag. A later first accounts deadline must not disappear:

| Date / Deadline | Obligation | Authority | Penalty if late | Professional needed? |
|---|---|---|---|---|
| [Formation + X days] | [obligation] | [authority] | [penalty] | [Yes/No] |
| ... | | | | |

Include both one-off formation-year obligations and the first occurrence of each recurring obligation.

### Output 5 : Reviewer brief

```markdown
# [Country] Company Formation : Reviewer Brief
**Client situation:** [one-sentence summary]
**Recommended entity type:** [type]
**Generated:** [date]

## Summary
- Entity types compared: [count]
- Recommended: [type] : [one-sentence reason]
- Alternative: [type] : [one-sentence condition under which this is better]
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

## Section 4 : Self-checks (run before delivering output)

Run all ten applicable checks. Fix failures before claiming a ready pack; an exception draft retains exact unresolved checks, missing evidence and consequences.

### Completeness

**Check 1 : All entity types covered.** Every entity type from the country skill's catalogue that is compatible with the user's situation appears in the comparison table. No eligible type is silently omitted.

**Check 2: All comparison dimensions addressed.** Give each actual sourced value, an explicit not-applicable reason, or an unresolved fact/source with its consequence. Never invent a value to fill a blank or rank an unknown as zero.

**Check 3 : Registration checklist covers all streams.** The registration checklist addresses every applicable registration stream from Step 4 (company register, tax authority, VAT, employer registration, local registration, bank account, licenses, data protection). Streams that do not apply to the selected entity type are explicitly noted as not applicable with a reason.

**Check 4 : Cost breakdown includes all mandatory fees.** Every statutory fee from the country skill's fee schedule appears in the cost breakdown. No mandatory cost is omitted. Estimated professional fees are clearly labelled as estimates.

### Consistency

**Check 5 : Recommendation matches comparison.** The recommended entity type in the reviewer brief is one of the types in the comparison table, and the stated reason is consistent with the comparison data. If the comparison shows Entity A has lower cost and lower administrative burden than Entity B, the recommendation should not favor Entity B without an explicit reason.

**Check 6: Calendar matches checklist.** Every obligation appears with its actually sourced trigger/deadline or an explicit unresolved-date status. Distinguish filing, payment, identity and bank processing dates, first versus later periods and approved extensions. No omission is hidden by a complete-looking calendar.

**Check 7 : Costs are consistent.** Formation costs in the cost breakdown match the costs mentioned in the registration checklist. Annual costs in the cost breakdown match the ongoing obligations in the compliance calendar. No amount appears in one output at a different figure than another.

### Accuracy

**Check 8: Actual source and scope.** Verify every entity rule, fee, authority, deadline and tax/identity condition from an actually read current official source, whether reached through the country method or the bounded application below. Never turn an example, historical fee or method author into country-wide coverage or professional approval. Keep the actual rule date and country/entity scope.

**Check 9 : Entity types correctly eliminated.** Every entity type excluded from the comparison table was excluded for a valid reason based on the user's confirmed situation. If a sole trader is excluded because the user requested liability protection, that is valid. If a partnership is excluded for no stated reason, that is an error.

**Check 10 : Tier 2/3 disclosure complete.** Every assumption or user-answered question that affected the recommendation is documented in the reviewer brief. No assumption is silently embedded in the outputs without disclosure.

### Failure handling

If a check fails, fix and rerun all ten. If the same item fails twice, stop finalisation and report the exact failure/evidence gap, retaining the exception draft. Never fill a missing fee/deadline with an invented value.

---

## Section 5 : Country skill contract

Every country-specific formation skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Entity type catalogue** : complete list of available entity types. For each: legal name (local language and English), governing legislation, min/max owners, liability treatment, tax treatment, minimum capital, audit requirements, and typical formation time.
2. **Registration authorities** : for each stream (company register, tax, VAT, employer, local licenses): authority name, website, and registration process summary.
3. **Fee schedule** : statutory formation fees (registration, name reservation, notary, gazette publication) and annual fees (annual return, registered office, audit thresholds).
4. **Founding document requirements** : required documents per entity type, notarization requirements, availability of standard templates.
5. **Capital rules** : minimum share capital per entity type, paid-up requirements, non-cash contribution rules and valuation requirements.
6. **Ongoing compliance obligations** : for each entity type: recurring filings (annual return, accounts, tax, payroll, VAT), filing body, frequency, deadline, and late-filing penalty.
7. **Director and officer requirements** : minimum directors, residency requirements, company secretary, disqualification rules.
8. **Beneficial ownership registration** : register availability, filing requirements, and deadline.
9. **VAT/GST registration** : actual turnover/supply/person/location tests, mandatory no-threshold cases, exclusions, permitted voluntary route, period/effective date and confirmation evidence.
10. **Audit eligibility** : actual country/entity/group/period size tests plus regulated/public-interest, member-demand and other mandatory-audit overrides or exemption conditions; meeting one size number alone proves nothing.

### Optional slots

11. **Industry-specific entity types** : special-purpose vehicles, professional corporations, cooperative societies, or other entity types specific to certain activities.
12. **Foreign owner considerations** : additional requirements or restrictions for entities with non-resident owners or directors, including apostille requirements, local representative requirements, and tax treaty implications.
13. **Integration notes** : how the formation skill interacts with the country's bookkeeping, tax, or payroll skills if loaded simultaneously.

---

## Section 6 : Reference material

### Validation status

This file is v1.1 of `company-formation-workflow-base`, updated in November 2026 from the original draft as part of the Open Accountants skill architecture in May 2026. It follows the structural pattern established by `bookkeeping-workflow-base` v1.0.

### Design decisions

1. **Advisory, not filing.** This workflow produces a comparison and checklist for professional review. It does not file anything : formation filings are high-stakes and often require identity verification that an AI cannot perform.

2. **Three-step confirmation.** Three user checkpoints (situation, entity type, final delivery) prevent wasted work from misunderstood situations.

3. **First-cycle calendar, not perpetual.** Use a 12 to 18 month planning window plus every later first-cycle filing/payment deadline. Hand off ongoing calendars to the country bookkeeping and tax methods without losing a first obligation.

4. **Cost ranges, not quotes.** Professional fees require an actual scoped quote or explicit client assumption; statutory fees require a current official channel/date. Unknowns stay unknown, and capital/deposits remain separate funding.

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


## Bounded UK private-company application, read 14 November 2026

For the Companies House private-company online route, identify the legal form, registered office/email, directors, shareholders/guarantors, constitutional documents and people with significant control. Do not treat a simple share-percentage clue as the complete beneficial-control test. The certificate proves legal incorporation, not a licence for every proposed activity or bank approval. Ordinary online registration costs **GBP 100** on the page read; timing is an estimate, not a guarantee. [Official registration service](https://www.gov.uk/limited-company-formation/register-your-company).

New-company registration asks for each director's personal identity code. PSC identity/code reporting is a separate role-specific requirement; being both director and PSC does not mean one role's submission completes both. Check the actual role/appointment and deadline, and have the person or authorised provider complete the official identity process. Do not ask them to paste personal codes into an AI output or public repository. [Companies House role-specific identity guidance](https://www.gov.uk/guidance/when-you-need-to-verify-your-identity-for-companies-house).

For an ordinary UK private-company case within the cited overview, first Companies House accounts and subsequent accounts have different triggers; Corporation Tax payment and return filing are separate again. The first accounts can exceed a tax accounting period, so obtain actual trading commencement and split return/payment tasks where required. Large-company instalments and other exceptions require the country corporate-tax method; this paragraph does not certify their payment date. [Accounts/return overview](https://www.gov.uk/prepare-file-annual-accounts-for-limited-company), [first-period distinction](https://www.gov.uk/first-company-accounts-and-return).

| Confirmed example item | Rule within stated UK scope | Official source |
|---|---|---|
| Ordinary private-company online registration | GBP 100, channel/date-specific fee, not a universal formation budget | [Companies House registration](https://www.gov.uk/limited-company-formation/register-your-company) |
| Private-company first and subsequent accounts | First accounts generally 21 months after incorporation; later accounts 9 months after financial year end. Establish actual period/extension and entity exceptions | [Official accounts overview](https://www.gov.uk/prepare-file-annual-accounts-for-limited-company) |
| Ordinary non-instalment Corporation Tax case and return | Overview payment rule 9 months plus 1 day after tax accounting period, return 12 months after that period. Actual instalment/other exceptions require their own method | [Official accounts/tax overview](https://www.gov.uk/prepare-file-annual-accounts-for-limited-company) |

## Worked cases

**Capital is funding, not a formation expense.** Assume the selected UK online route is applicable, paid share capital is GBP 5,000, the actual government fee is GBP 100 and an actual agreed professional quote is GBP 300 with no further tax/disbursements in this example. Consumed formation cash is GBP 400; gross funding paid in is GBP 5,000; remaining liquidity is GBP 4,600. It is wrong to call GBP 5,400 formation expense. Capital availability, banking, accounting recognition and tax deduction remain separate questions. Only the government fee is a statutory figure; capital/quote are assumed facts. [Companies House fee](https://www.gov.uk/limited-company-formation/register-your-company).

```oa-check
name: Separate paid capital from formation costs and remaining liquidity
inputs:
  paid_share_capital: 5000
  actual_online_registration_fee: 100
  agreed_professional_fee: 300
steps:
  - formation_cash_cost: actual_online_registration_fee + agreed_professional_fee
  - company_liquidity_after_fees: paid_share_capital - formation_cash_cost
  - amount_overstated_if_capital_added_to_cost: paid_share_capital
expected:
  formation_cash_cost: 400
  company_liquidity_after_fees: 4600
  amount_overstated_if_capital_added_to_cost: 5000
```

**Long first accounts require a period split.** Assume an actual first accounts period has twelve complete months plus one further month of trading and the UK Corporation Tax maximum accounting-period condition applies. One thirteen-month Corporation Tax return is not valid merely because the accounts cover thirteen months; prepare the twelve-month and residual-period tasks with separately established payment/filing dates. These illustrative month counts are assumed case facts, not an election to lengthen a tax period. [HMRC first accounts and returns](https://www.gov.uk/first-company-accounts-and-return).

```oa-check
name: First accounts span is not automatically one Corporation Tax period
inputs:
  months_in_first_accounts: 13
  maximum_months_in_tax_period: 12
steps:
  - first_period_months: min(months_in_first_accounts, maximum_months_in_tax_period)
  - residual_period_months: max(months_in_first_accounts - first_period_months, 0)
  - reconstructed_accounts_months: first_period_months + residual_period_months
expected:
  first_period_months: 12
  residual_period_months: 1
  reconstructed_accounts_months: 13
```

## When to refuse or refer

Hold final recommendation/filing readiness when legal form, beneficial control, identity, ownership rights, mandatory licensing, funding legitimacy or actual country rule is unresolved. Foreign/group/residence/PE and restructuring questions need the relevant specialist method instead of tax savings inferred from the registration address. Do not impersonate an applicant, attest identity, guarantee bank approval, supply invented fee ranges, or submit a registration/payment through this preparation method. Preserve the usable comparison and exact unresolved questions.

## Sources

| Official source | What was actually read for | Read on |
|---|---|---|
| https://www.gov.uk/limited-company-formation/register-your-company | Read for registration prerequisites, actual online fee/channel, certificate, tax-registration interaction and identity-code requirement; no all-country fee/time claim | 2026-11-14 |
| https://www.gov.uk/limited-company-formation/shareholders | Read for UK private-shareholder scope, share/guarantee distinction, capital/rights and unpaid-share liability; the page's low-value share example is not a universal minimum | 2026-11-14 |
| https://www.gov.uk/running-a-limited-company | Read for directors' continuing responsibilities despite professional assistance and required records/filings | 2026-11-14 |
| https://www.gov.uk/guidance/when-you-need-to-verify-your-identity-for-companies-house | Read for director, PSC and authorised-agent role requirements and actual role-specific reporting periods; no single blanket identity deadline adopted | 2026-11-14 |
| https://www.gov.uk/prepare-file-annual-accounts-for-limited-company | Read for private-company first/later accounts versus ordinary tax-payment/return overview; actual special-case/instalment conditions must come from the company tax method | 2026-11-14 |
| https://www.gov.uk/first-company-accounts-and-return | Read for first accounts spanning more than one tax accounting period, actual trading-start distinction and separate payment tasks; not every linked special case | 2026-11-14 |

Not yet confirmed: every non-UK jurisdiction/entity's actual eligibility, liability, capital/paid-up and non-cash rules, foreign-owner/director limits, tax classification/elections/residence/PE, registration/beneficial-control/identity requirements, VAT/payroll triggers, licensing, data-protection fees, audit exemptions and reporting dates. Also obtain UK activity-specific permissions, full PSC control tests, actual special-case accounts/Corporation Tax dates and exact client identity-role deadlines. Professional fee ranges, formation turnaround, bank approval, tax deductions and permission to withdraw capital are not certified by incorporation or by this method. The original worldwide no-output refusal, full-liability-protection label, threshold-only registration and treating share capital as a formation cost have been corrected; all comparison dimensions, registration streams, five outputs, ten checks and country slots remain.
