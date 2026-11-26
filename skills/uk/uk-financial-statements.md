---
name: uk-financial-statements
description: >
  Use this Guide when preparing or reviewing a UK company’s annual accounts: micro, small and medium size tests, reporting framework selection, statutory statements, year-end adjustments, audit exemption, board approval, Companies House filing, late filing penalties, iXBRL, identity verification and announced April 2028 reforms. Applies at 26 November 2026; technical reporting and special-entity issues requiring further professional judgment are explicitly referred.
version: "2.1"
type: situation-rules
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-26
source_checked: 2026-11-26
depends_on:
  - financial-statements-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-statements
---

# UK Financial Statements

> **Year applicability:** Position at 26 November 2026. Size limits below apply by the **start of the financial year**, not its year-end or the personal tax year. The principal Periodic Review 2024 accounting changes apply to periods beginning on or after 1 January 2026; do not apply them automatically to an earlier-starting period ending in 2026. Future filing announcements are identified separately.

## Scope

Annual accounts working papers for a UK company, loading `financial-statements-workflow-base`. Establish the size regime, reporting framework, audit position, approval and filing obligations separately. Corporation tax computations and CT600 preparation belong to `uk-corporation-tax`; formation belongs to `uk-formation`. Neither a calculation here nor the absence of an audit constitutes professional approval.

### Quick reference

United Kingdom; GBP; Companies House. Normal filing periods are nine months for private companies and six months for public companies, subject to the first-period and altered-period rules below ([CA 2006 s.442](https://www.legislation.gov.uk/ukpga/2006/46/section/442)). A micro or small size result alone does not establish reporting or audit eligibility.

## Ask the client first

Read the available records before asking for missing facts: incorporation and reference dates; actual financial-year start/end; this and preceding years’ turnover, total assets and monthly employee counts; first-year status; group structure and consolidation; public/traded or regulated status; charity status; existing accounting framework; members’ audit notices; prior late filing; leases, customer contracts, development, grants and director loans; proposed filer and software; identity-verification status. Obtain evidence of board approval and the actual signatory. Do not infer consent, eligibility or verification from a company’s size.

## The method, step by step

1. Identify the period and apply the size limits, history and exclusions below.
2. Establish framework eligibility and prepare the complete accounts, distinct from the public filing copy.
3. Reconcile the trial balance, assess the year-end adjustments and settle any referred accounting judgments before completing the accounts.
4. Establish audit entitlement independently; obtain any required audit and board approval.
5. Calculate the filing deadline and deliver the permitted filing copy with required statements and signatory identification. Check acceptance rather than treating transmission as completion.

## Rates, bands and thresholds

For financial years beginning on or after 6 April 2025, satisfy **at least two of the three** applicable limits. Earlier limits are shown solely for earlier-starting years; apply the transitional look-back below when classifying a later year.

| Regime | Turnover ceiling | Total-assets ceiling | Average employees ceiling | Official source |
|---|---|---|---|---|
| Micro | GBP 1,000,000 | GBP 500,000 | 10 | https://www.legislation.gov.uk/ukpga/2006/46/section/384A |
| Small | GBP 15,000,000 | GBP 7,500,000 | 50 | https://www.legislation.gov.uk/ukpga/2006/46/section/382 |
| Medium-sized | GBP 54,000,000 | GBP 27,000,000 | 250 | https://www.legislation.gov.uk/ukpga/2006/46/section/465 |
| Earlier micro | GBP 632,000 | GBP 316,000 | 10 | https://www.legislation.gov.uk/uksi/2024/1303/made |
| Earlier small | GBP 10,200,000 | GBP 5,100,000 | 50 | same |
| Earlier medium-sized | GBP 36,000,000 | GBP 18,000,000 | 250 | same |
| Small group | GBP 15,000,000 net or GBP 18,000,000 gross | GBP 7,500,000 net or GBP 9,000,000 gross | 50 | https://www.legislation.gov.uk/ukpga/2006/46/section/383 |
| Medium-sized group | GBP 54,000,000 net or GBP 64,000,000 gross | GBP 27,000,000 net or GBP 32,000,000 gross | 250 | https://www.legislation.gov.uk/ukpga/2006/46/section/466 |

- **Definitions:** total assets means the aggregate amounts shown as assets, without deducting liabilities. Average employees: count persons under contracts of service in each month, total those counts, divide by months in the year. For a period other than a year, proportionately adjust the turnover limit, not the asset or employee limits ([ss.382, 384A, 465](https://www.legislation.gov.uk/ukpga/2006/46/section/382)).
- **History:** the first financial year stands alone. For small and micro status thereafter, meeting or ceasing to meet the conditions affects qualification only after two consecutive financial years. For medium status, s.465(2) permits current-and-prior conditions, current conditions plus prior qualification, or prior conditions plus prior qualification. A single excess does not automatically make a company large ([s.384A](https://www.legislation.gov.uk/ukpga/2006/46/section/384A), [s.465](https://www.legislation.gov.uk/ukpga/2006/46/section/465)).
- **Transitional look-back:** for years beginning on or after 6 April 2025, treat previous years’ qualification and qualifying conditions as if the new limits had applied then and, for qualification, to preceding years. This also applies to groups; do not simply import last year’s old classification ([SI 2024/1303 regs.2-3](https://www.legislation.gov.uk/uksi/2024/1303/made)).
- **Groups:** parent-company small/medium qualification additionally requires the group to qualify; apply its own history. Aggregate member figures; net eliminates intra-group transactions, gross does not. Either basis may satisfy each relevant requirement. Micro parents need a small group as well as their own micro qualification ([s.383](https://www.legislation.gov.uk/ukpga/2006/46/section/383), [s.466](https://www.legislation.gov.uk/ukpga/2006/46/section/466), [s.384A(8)](https://www.legislation.gov.uk/ukpga/2006/46/section/384A)). Complex aggregation or mismatched subsidiary periods: Check this point with one of our partner accountants.

## Boundary and exception table

| Issue | Rule or required action | Official source |
|---|---|---|
| Small-regime exclusion | Test status at any time in the year. Public companies, specified insurance/banking/e-money/MiFID/UCITS entities, insurance-market activity, Master Trust scheme funders and members of an ineligible group are excluded. An ineligible group is a statutory category, not simply a group above the size limits. A public group member is not, by that fact alone, the complete statutory test. Regulated/group classification: Check this point with one of our partner accountants. | https://www.legislation.gov.uk/ukpga/2006/46/section/384 |
| Additional micro exclusions | Investment undertakings, financial holding undertakings, specified credit/insurance institutions and charities are excluded, as are small-regime-excluded entities. Micro treatment also excludes a parent preparing group accounts and a non-parent whose accounts are consolidated. | https://www.legislation.gov.uk/ukpga/2006/46/section/384B |
| Medium-regime exclusions | Public companies, specified regulated entities, e-money issuers, Master Trust scheme funders and members of an ineligible group cannot claim medium concessions merely by meeting the figures. | https://www.legislation.gov.uk/ukpga/2006/46/section/467 |
| LLPs | The raised limits were also applied to LLPs, but this company workflow does not determine LLP reporting or signing requirements. Check this point with one of our partner accountants. | https://www.legislation.gov.uk/uksi/2024/1303/made |

### Reporting framework and statements

- **Micro:** choosing the micro regime requires FRS 105; an eligible entity may choose another regime instead ([FRC FRS 105](https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-105/)).
- **Small:** FRS 102 Section 1A concerns presentation and disclosure for an eligible entity choosing the small regime; it does not generally replace FRS 102 recognition and measurement. Full FRS 102, adopted IFRS or eligible FRS 101 can be alternatives. **FRS 101** is a reduced-disclosure framework for qualifying individual accounts of subsidiaries/ultimate parents, not automatic relief for every group company. Framework switching, FRS 101 eligibility and exemptions: Check this point with one of our partner accountants. ([FRS 102 paras.1A.1-1A.2](https://www.frc.org.uk/documents/7668/FRS_102_September_2024_tmKYWO6.pdf), [FRC FRS 101](https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-101/)).
- **IFRS:** a parent whose securities are admitted to a UK regulated market at its balance sheet date must use UK-adopted IFRS for group accounts. This is not a universal statement about AIM. Individual-account choices, charity restrictions, group consistency and switching conditions must be checked separately; AIM and specialist/group reporting: Check this point with one of our partner accountants. ([s.395](https://www.legislation.gov.uk/ukpga/2006/46/section/395), [s.403](https://www.legislation.gov.uk/ukpga/2006/46/section/403)).
- **Standards dates:** most Periodic Review 2024 amendments apply to periods beginning on or after 1 January 2026; FRS 102 supplier-finance disclosures in paras.7.20B-C start from 1 January 2025. Early application of the other amendments requires applying them together. Thus a calendar-year entity’s first mandatory principal-change year is the year ending 31 December 2026. The adapted-format amendments have a principal effective date of 1 January 2027, with clarifications affecting the periodic-review amendments; transition, early adoption and format adaptation: Check this point with one of our partner accountants. ([FRS 102 para.1.37](https://www.frc.org.uk/documents/7668/FRS_102_September_2024_tmKYWO6.pdf), [FRC current amendments](https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/)).
- **Prepare versus file:** Companies Act individual accounts comprise a balance sheet and P&L, plus the applicable notes. Public filing concessions do not dispense with preparing the P&L. Directors must be satisfied with a true and fair view. Micro minimum items have a statutory presumption and limited exceptions; additional information is not automatically outside standards requirements ([ss.393, 396](https://www.legislation.gov.uk/ukpga/2006/46/section/396)).
- **Reports:** directors’ report required unless micro; strategic report required unless the s.414B small-company exemption applies. Group report requirements must be considered where group accounts are prepared ([s.415](https://www.legislation.gov.uk/ukpga/2006/46/section/415), [s.414A](https://www.legislation.gov.uk/ukpga/2006/46/section/414A), [s.414B](https://www.legislation.gov.uk/ukpga/2006/46/section/414B)).
- **Equity, comprehensive income and cash flows:** do not use a size-only required/not-required matrix. A small entity’s true-and-fair needs and qualifying-entity exemptions can change the result. Check this point with one of our partner accountants.

### Year-end adjustments and disclosures

Apply the chosen framework; this is not a substitute for its measurement rules. For small Companies Act accounts, [SI 2008/409 Schedule 1](https://www.legislation.gov.uk/uksi/2008/409/schedule/1) provides the following statutory starting points:

| Adjustment | Instruction or professional referral |
|---|---|
| Depreciation | Under the historical-cost rule in para.18, depreciate cost less estimated residual value systematically over a fixed asset’s limited useful economic life. Changes in useful life, residual value or method: Check this point with one of our partner accountants. |
| Accruals and prepayments | Attribute income and charges to the financial year irrespective of cash receipt/payment (para.14); reconcile fees, bonuses, utilities, insurance, rent and licences to their actual periods. |
| Provisions and bad debts | Assess liabilities and diminution in value on a prudent basis (para.13). The particular obligation, recognition and impairment model, including financial-instrument policy choices, must be established; a blanket expected-loss or incurred-loss instruction is unsafe. Check this point with one of our partner accountants. |
| Inventory | Under the historical-cost rules, current assets use purchase/production cost unless net realisable value is lower (paras.23-24). Establish the applicable framework’s cost and impairment rules before measuring stocks. |
| Deferred tax | Recognition, timing differences, exceptions and measurement: Check this point with one of our partner accountants. |
| Holiday pay | Accumulating/non-accumulating entitlement and accrual measurement: Check this point with one of our partner accountants. |
| Leases | Periodic Review 2024 changes FRS 102 lessee accounting. Scope, recognition exemptions, measurement and transition: Check this point with one of our partner accountants. |
| Revenue | Periodic Review 2024 changes revenue accounting in FRS 102 and FRS 105. Contract analysis, timing and transition: Check this point with one of our partner accountants. |
| R&D | Research costs cannot be included as assets under para.3(2); development can be included only consistently with generally accepted accounting principles/practice (para.21), with the specified policy note. The detailed recognition criteria and policy choice: Check this point with one of our partner accountants. |
| Government grants | Model choice, conditions and recognition: Check this point with one of our partner accountants. |
| Director loans | An overdrawn year-end balance alone does not settle tax liability. The tax charge, repayment relief, exemptions and accounts treatment: Check this point with one of our partner accountants. |

The FRC confirms the revenue and FRS 102 lease changes in its [September 2026 reminder](https://www.frc.org.uk/news-and-events/news/2026/09/frc-issues-reminder-of-significant-change-now-effective-in-uk-gaap/). This Guide does not claim a complete read of the accounting standards.

**Formats:** use the applicable statutory format, not the previous Guide’s abbreviated transcription as a complete filing template. For small companies, SI 2008/409 Sch.1 Section B contains balance-sheet formats 1/2 and P&L formats 1/2; micro formats are in Section C. The format notes govern alternative placement of unpaid capital, prepayments and accruals. Abridgement needs all members’ consent for the relevant preceding financial year, and is unavailable to charities (para.1A). Format selection/adaptation and medium/large SI 2008/410 formats: Check this point with one of our partner accountants.

**Notes:** policies, fixed-asset movements, commitments/guarantees/contingencies, related parties, employee numbers, directors’ remuneration, audit fees, financial instruments, deferred tax, share capital and dividends each need a framework- and fact-specific review. Do not treat micro notes as universally absent, or reduced disclosures as eliminating true-and-fair obligations. Check this point with one of our partner accountants.

### Audit, approval and signatures

- Accounts must be audited unless a statutory exemption applies. Small-company exemption under s.477 uses s.382 qualification but is subject to ss.475-479; micro status alone is insufficient. Public companies and the specified regulated/special-register entities in s.478 cannot use **that exemption**. Medium/large/public status does not by itself dispose of every other statutory exemption ([s.475](https://www.legislation.gov.uk/ukpga/2006/46/section/475), [s.477](https://www.legislation.gov.uk/ukpga/2006/46/section/477), [s.478](https://www.legislation.gov.uk/ukpga/2006/46/section/478)).
- **Member demand:** a valid s.476 notice overrides the ordinary small, subsidiary or dormant exemptions. Members must represent at least 10% of nominal issued share capital or of a class, or at least 10% in number if no share capital. Notice cannot precede the year and must arrive no later than one month before its end ([s.476](https://www.legislation.gov.uk/ukpga/2006/46/section/476)).
- **Group member:** s.477 ordinarily requires a small, non-ineligible group. Section 479(3) separately protects a subsidiary dormant throughout its group-membership periods; do not equate an oversized group with an ineligible one ([s.479](https://www.legislation.gov.uk/ukpga/2006/46/section/479)).
- **Subsidiary guarantee:** s.479A is a separate exemption, not merely a parent’s informal promise. UK-established parent, annual unanimous member agreement, statutory guarantee, consolidation, disclosure, filing of specified parent documents and exclusions all need review. Dormant/public-sector exemptions, guarantee documentation, auditor eligibility/registration and the audit itself: Check this point with one of our partner accountants. ([ss.479A-479C](https://www.legislation.gov.uk/ukpga/2006/46/section/479A)).
- **Charities:** England/Wales charity-law audit and its interaction with company law, including the financial-year-end changes from 30 September 2026, SORP and independent examination: Check this point with one of our partner accountants. Do not apply a single UK-wide charity threshold.
- **Approval:** board approves annual accounts; a director signs the balance sheet on its behalf. Place the relevant small/micro statement above the signature. Audit-exemption statements must appear above that signature, acknowledge directors’ responsibilities and confirm no member demand. Never generate a human approval or signature ([s.414](https://www.legislation.gov.uk/ukpga/2006/46/section/414), [s.475](https://www.legislation.gov.uk/ukpga/2006/46/section/475)). Board-approved directors’ and strategic reports are signed by a director or secretary; a directors’ report using small-company relief needs the prominent statement ([s.419](https://www.legislation.gov.uk/ukpga/2006/46/section/419), [s.414D](https://www.legislation.gov.uk/ukpga/2006/46/section/414D)).

## Filing and payment

| Issue | Current rule | Official source |
|---|---|---|
| Ordinary deadline | Nine months after the reference-period end (private); six months (public). Use status immediately before period-end. | https://www.legislation.gov.uk/ukpga/2006/46/section/442 |
| First period over 12 months | Later of nine/six months from incorporation’s first anniversary and three months after period-end. Thus usually 21/18 months from incorporation, not an unconditional first-accounts rule. | same |
| Shortened period | Later of the otherwise applicable deadline and three months from the date of the s.392 notice. | same |
| Discretionary deadline extension | Apply before the existing deadline; extension must be granted and cannot exceed 12 months after reference-period end. | same |
| Altered reference period | Normally no extension beyond 18 months, or another extension less than five years after the earlier extended period ended. Administration, group-alignment and Secretary of State exceptions differ; a previous-period notice is barred after its filing deadline. Check this point with one of our partner accountants. | https://www.legislation.gov.uk/ukpga/2006/46/section/392 |
| Small/micro public copy | Current s.444 permits omitting P&L and directors’ report, with the relevant balance-sheet statements, notes/footnotes and signatory identification. Abridgement also needs the all-member consent statement. This does not mean preparing only a balance sheet. Audited filleted accounts have extra note requirements: Check this point with one of our partner accountants. | https://www.legislation.gov.uk/ukpga/2006/46/section/444 |
| Other companies | Medium companies within s.445 file accounts, strategic report, directors’ report and auditor’s report unless audit exemption is taken. Large, quoted and other special filing duties: Check this point with one of our partner accountants. | https://www.legislation.gov.uk/ukpga/2006/46/section/445 |
| HMRC versus Companies House | HMRC’s combined service closed 31 March 2026. From 1 April use commercial software for ordinary HMRC annual accounts/Company Tax Return filing; paper remains possible for Welsh returns or reasonable excuse. Companies House currently accepts online or paper accounts. CT600, computation, iXBRL scope/exceptions and language-specific filing: Check this point with one of our partner accountants. | https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return |

### Late filing penalties

Civil penalties on the company under [s.453](https://www.legislation.gov.uk/ukpga/2006/46/section/453), measured to delivery complying with s.441. Criminal/default consequences and appeals require separate advice.

| Delay beyond deadline | Private | Public | Official source |
|---|---|---|---|
| Not more than one month | GBP 150 | GBP 750 | https://www.legislation.gov.uk/uksi/2008/497/regulation/4 |
| More than one, not more than three months | GBP 375 | GBP 1,500 | same |
| More than three, not more than six months | GBP 750 | GBP 3,000 | same |
| More than six months | GBP 1,500 | GBP 7,500 | same |

Double the table amount where the previous financial year’s filing requirements were also breached and that year began on or after 6 April 2008. Public amounts are not simply twice private amounts.

### Identity and announced reforms

Identity verification began as a mandatory requirement on 18 November 2025; the existing-director transition covered confirmation statements due between 18 November 2025 and 17 November 2026 ([Companies House, 18 November 2026](https://www.gov.uk/government/news/identity-verification-is-making-the-uks-company-register-more-trustworthy)). Do not tell an overdue director to wait until the next annual accounts filing. Role-specific personal codes, PSC windows including birth-month rules, overseas-company deadlines, ACSP registration, filer permissions, GOV.UK One Login/WebFiling and registered-email/office/lawful-purpose requirements: Check this point with one of our partner accountants.

**April 2028 is an announced future programme, not today’s filing rule.** Companies House’s [23 October 2026 announcement](https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028) says commercial-software iXBRL filing will replace web/paper accounts filing, while non-accounts web services remain. It pauses small/micro P&L-publication reforms and retains abridgement/filleting. It also announces an audit-exemption statement, filing components together and a reference-period-shortening limit. Exact commencement, implementing conditions and future forms: Check this point with one of our partner accountants. Do not present prospective replacement s.444 text as already operative.

## Worked cases

Illustrations, not client data. Original numeric inputs and executable calculations are retained. A met criterion is 1, otherwise 0; the indicator formula assumes non-negative inputs. It calculates size criteria, not statutory eligibility.

**Case 1 (decision, both ways): micro or small?** Original third-year private company: turnover GBP 900,000 and total assets GBP 550,000 in both years; compare average employees 8 and 12, also in both years. Assume each relevant year is a full year beginning on or after 6 April 2025, the company is standalone and none of ss.384/384B’s exclusions applies. Eight employees meets two micro criteria; twelve meets one micro and all three small criteria. The eligible company may elect the micro regime/FRS 105 in the first scenario; the second qualifies for small treatment, with Section 1A an available choice rather than compulsory. Audit entitlement and the filing copy still need separate checks ([s.384A](https://www.legislation.gov.uk/ukpga/2006/46/section/384A), [s.382](https://www.legislation.gov.uk/ukpga/2006/46/section/382)).

```oa-check
name: Micro or small, 8 employees against 12 (limits from 6 April 2025)
inputs:
  turnover: 900000
  balance_sheet: 550000
  employees_a: 8
  employees_b: 12
  micro_turnover: 1000000
  micro_balance: 500000
  micro_employees: 10
  small_turnover: 15000000
  small_balance: 7500000
  small_employees: 50
steps:
  - t_micro: max(0, min(1, floor((micro_turnover - turnover) / micro_turnover) + 1))
  - b_micro: max(0, min(1, floor((micro_balance - balance_sheet) / micro_balance) + 1))
  - e_micro_a: max(0, min(1, floor((micro_employees - employees_a) / micro_employees) + 1))
  - e_micro_b: max(0, min(1, floor((micro_employees - employees_b) / micro_employees) + 1))
  - micro_met_a: t_micro + b_micro + e_micro_a
  - micro_met_b: t_micro + b_micro + e_micro_b
  - is_micro_a: min(1, floor(micro_met_a / 2))
  - is_micro_b: min(1, floor(micro_met_b / 2))
  - t_small: max(0, min(1, floor((small_turnover - turnover) / small_turnover) + 1))
  - b_small: max(0, min(1, floor((small_balance - balance_sheet) / small_balance) + 1))
  - e_small_b: max(0, min(1, floor((small_employees - employees_b) / small_employees) + 1))
  - small_met_b: t_small + b_small + e_small_b
  - is_small_b: min(1, floor(small_met_b / 2))
expected:
  micro_met_a: 2
  micro_met_b: 1
  is_micro_a: 1
  is_micro_b: 0
  small_met_b: 3
  is_small_b: 1
```

**Case 2: late twice running.** Original private company: year ended 31 December 2025; accounts delivered in compliance on 15 January 2027; 2024 accounts also late. Assume an ordinary subsequent reference period and no altered deadline. Nine months gives 30 September 2026; 15 January is more than three but not more than six months late. GBP 750 × 2 = GBP 1,500. The previous year necessarily began after 6 April 2008 ([s.442](https://www.legislation.gov.uk/ukpga/2006/46/section/442), [SI 2008/497 reg.4](https://www.legislation.gov.uk/uksi/2008/497/regulation/4)).

```oa-check
name: Private company penalty, 3 to 6 months late, previous year also late
inputs:
  table_penalty: 750
  previous_year_late: 1
steps:
  - multiplier: 1 + previous_year_late
  - penalty: table_penalty * multiplier
expected:
  multiplier: 2
  penalty: 1500
```

## When to refuse or refer

For any referred topic above: Check this point with one of our partner accountants. Hold the affected conclusion or filing until resolved. This includes disputed size inputs, consolidation and non-small/ineligible groups, specialist regulated entities, charities, AIM, technical standard judgments, audit execution and non-routine filing. Do not fabricate director/member approval, audit evidence, identity status or a signature.

## Completion checklist

- [ ] Period, inputs and history evidenced; size calculation separated from statutory exclusions.
- [ ] Framework, adjustments, statements and disclosures settled; all professional referrals resolved for this engagement.
- [ ] Audit and member demand independently checked; reports, balance-sheet statements and board approval evidenced.
- [ ] Deadline, filing-copy requirements, software/identity authority and acceptance checked.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Sources

Read on 26 November 2026, restricted to the provisions identified here. Legislation XML includes prospective text as well as current provisions; current filing guidance is distinguished from the announced reforms. FRC catalogue pages and selected accessible paragraphs are not a full read of the standards.

| Source | What was read | URL | Read on |
|---|---|---|---|
| CA 2006 s.382 | Limits, history, period adjustment and employee definition | https://www.legislation.gov.uk/ukpga/2006/46/section/382 | 2026-11-26 |
| CA 2006 s.384A | Micro limits, history and parent test | https://www.legislation.gov.uk/ukpga/2006/46/section/384A | 2026-11-26 |
| CA 2006 s.465 | Medium limits and qualification alternatives | https://www.legislation.gov.uk/ukpga/2006/46/section/465 | 2026-11-26 |
| SI 2024/1303 | Regs.2-3, 9-11: applicability, look-back, old/new limits and LLP amendments | https://www.legislation.gov.uk/uksi/2024/1303/made | 2026-11-26 |
| CA 2006 s.383 | Small parent/group conditions and aggregation | https://www.legislation.gov.uk/ukpga/2006/46/section/383 | 2026-11-26 |
| CA 2006 s.466 | Medium parent/group conditions | https://www.legislation.gov.uk/ukpga/2006/46/section/466 | 2026-11-26 |
| CA 2006 s.384 | Small-regime exclusions, distinct from size | https://www.legislation.gov.uk/ukpga/2006/46/section/384 | 2026-11-26 |
| CA 2006 s.384B | Additional micro exclusions including consolidation | https://www.legislation.gov.uk/ukpga/2006/46/section/384B | 2026-11-26 |
| CA 2006 s.467 | Medium-regime exclusions | https://www.legislation.gov.uk/ukpga/2006/46/section/467 | 2026-11-26 |
| FRC FRS 105 catalogue | Optional regime; FRS 105 required when chosen | https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-105/ | 2026-11-26 |
| FRC FRS 102 September 2024 accessible edition | Selected paras.1.37, 1A.1-1A.2, 1A.7A-1A.9; not complete standards review | https://www.frc.org.uk/documents/7668/FRS_102_September_2024_tmKYWO6.pdf | 2026-11-26 |
| FRC FRS 102 catalogue | Adapted-format dates and clarification context | https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/ | 2026-11-26 |
| FRC FRS 101 catalogue | Individual-account framework overview only | https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-101/ | 2026-11-26 |
| FRC September reminder | Revenue and FRS 102 lease changes; implementation resources | https://www.frc.org.uk/news-and-events/news/2026/09/frc-issues-reminder-of-significant-change-now-effective-in-uk-gaap/ | 2026-11-26 |
| CA 2006 ss.395/403 | IFRS choices, compulsory regulated-market group accounts and conditions | https://www.legislation.gov.uk/ukpga/2006/46/section/403 | 2026-11-26 |
| CA 2006 ss.393/396 | True-and-fair duties, micro treatment and statements | https://www.legislation.gov.uk/ukpga/2006/46/section/396 | 2026-11-26 |
| CA 2006 ss.414A/414B/415 | Report duties and exemptions | https://www.legislation.gov.uk/ukpga/2006/46/section/414A | 2026-11-26 |
| SI 2008/409 Sch.1 | Formats/abridgement, accounting principles and selected historical-cost rules | https://www.legislation.gov.uk/uksi/2008/409/schedule/1 | 2026-11-26 |
| CA 2006 ss.475-479 | Audit exemptions, statements, member demand and group conditions | https://www.legislation.gov.uk/ukpga/2006/46/section/475 | 2026-11-26 |
| CA 2006 ss.479A-479C | Read to identify why subsidiary exemption needs a separate review | https://www.legislation.gov.uk/ukpga/2006/46/section/479A | 2026-11-26 |
| CA 2006 ss.414/414D/419 | Board approval and signing requirements | https://www.legislation.gov.uk/ukpga/2006/46/section/414 | 2026-11-26 |
| CA 2006 ss.392/442 | Reference-period and deadline conditions/exceptions | https://www.legislation.gov.uk/ukpga/2006/46/section/442 | 2026-11-26 |
| CA 2006 ss.444/445 | Current public filing duties and relief | https://www.legislation.gov.uk/ukpga/2006/46/section/444 | 2026-11-26 |
| SI 2008/497 reg.4; CA 2006 s.453 | Civil penalty bands, previous-year condition and liability | https://www.legislation.gov.uk/uksi/2008/497/regulation/4 | 2026-11-26 |
| HMRC service closure | Date, software and paper exceptions; separate Companies House filing | https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return | 2026-11-26 |
| Companies House identity update | 18 November 2025 commencement and completed transition period | https://www.gov.uk/government/news/identity-verification-is-making-the-uks-company-register-more-trustworthy | 2026-11-26 |
| Companies House future accounts announcement | Future software filing; P&L pause; other announced reforms | https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028 | 2026-11-26 |

Not yet confirmed for use in this Guide: the individual conclusions listed as professional referrals. They supply no usable exemption, measurement policy or future filing form until resolved.
