---
name: in-tax-residency
description: "India individual tax residence: resident, non-resident and resident but not ordinarily resident (RNOR); employment departures, visits, deemed residence, scope of foreign income, return schedules and treaty paperwork. Covers Tax Year 2026-27 under the Income-tax Act, 2025 and the separately labelled 2025-2026 filing cycle under the 1961 Act. Trigger on India 182-day rule, 120-day rule, NRI returning to India, foreign income and RNOR."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/in-tax-residency"
  jurisdiction: "IN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# India individual tax residence v1.1

> **General reference only.** This skill produces a residence working paper for professional review. Residence, treaty entitlement and exchange-control status depend on the client's documents and circumstances.

## Scope

Decide an individual's Indian domestic residence each year, then distinguish resident and ordinarily resident (ROR), resident but not ordinarily resident (RNOR) and non-resident (NR). Apply the scope of taxable income and route the return and treaty paperwork. **Primary period: Tax Year 2026-27, 1 April 2026 to 31 March 2027**, under the Income-tax Act, 2025. The separate **2025-2026 filing cycle**, FY 2025-26 / AY 2026-27, uses the 1961 Act and its return forms. Later assessment or reassessment does not move an earlier year's residence test into the new Act. [2025 Act, ss.3, 5-6](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf); [transition FAQ, Q7-11](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq).

The tests continue across the Acts, including earlier years in the look-backs. Do not restart the residence history when the new Act begins. The answer layer is the residence table below; obtain the inputs before choosing a status.

Companies, HUFs, firms, trusts and other entities are outside this individual's computation. An Indian company or a company with its place of effective management in India is resident under s.6(10); HUF/firm/association control-and-management rules are in s.6(9). Refer those cases rather than applying individual day tests. NRI investment concessions, FEMA bank-account status and the tax computation itself are separate jobs: load the relevant India skill. Currency is INR; 1 lakh means INR 100,000 (unit conversion, derived).

## Ask the client first

- Citizenship and Indian origin; reason for departure or visit; foreign employment contract or ship/crew records where relevant.
- Evidence of India presence for the current year and each of the preceding 10 years, plus the residence status in those years. Use passport/travel records and earlier returns; resolve uncertain arrival/departure days before using a boundary result.
- Total income **other than income from foreign sources**, computed under the Act, and whether the client is liable to tax elsewhere by domicile, residence or similar criteria. Obtain the foreign return/TRC and examine the underlying law; a country having no salary tax does not alone decide the statutory liability test.
- Every Indian and foreign income stream and where first received; any foreign business controlled in India or profession set up in India; foreign accounts, shares, property, insurance and trusts.
- The filing period, business/professional income, earlier return status, active PAN, and whether treaty relief or foreign tax credit is sought. For a treaty claim obtain residence certificates, foreign TIN, home/family/economic ties and the specific treaty text.
- Foreign taxes paid/deducted, evidence, any dispute or refund, and whether a resident needs an Indian TRC for a foreign payer.

## The method, step by step

### Residence tests and thresholds

All current-year figures below are in enacted **s.6 of the 2025 Act**, as amended by Finance Act, 2026. Where the Act prints a number in words, the row says so. Tests are alternatives except where a row expressly requires both conditions.

| Test | Value and complete condition | Official source |
|---|---|---|
| Basic residence | At least 182 India days in the tax year: resident (in words on the page) | [s.6(2)(a)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27) |
| Alternative residence | At least 60 India days in the year **and** at least 365 India days in the preceding 4 years: resident (in words on the page) | [s.6(2)(b)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27) |
| Citizen leaving for foreign employment or as Indian-ship crew | Alternative limb switched off; 182-day basic limb remains (in words on the page). This does not switch off deemed residence | [s.6(3), (7)-(8)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27) |
| Visiting citizen/PIO, qualifying income no more than INR 15 lakh | Alternative limb switched off; basic 182-day test remains (in words on the page) | [s.6(4)-(5)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=28) |
| Visiting citizen/PIO, qualifying income exceeding INR 15 lakh | Alternative limb becomes at least 120 India days **and** at least 365 in preceding 4 years; basic 182-day limb also remains (in words on the page) | [s.6(2), (4)-(5)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=28) |
| Deemed residence | Indian **citizen**, qualifying income exceeding INR 15 lakh, not liable to tax elsewhere by domicile/residence/similar criteria, and not already resident under day tests: deemed resident irrespective of days (income number in words on the page) | [s.6(7)-(8)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=28) |
| Ordinary RNOR history tests | A resident is RNOR if NR in 9 of preceding 10 tax years **or** in India no more than 729 days in preceding 7 tax years (in words on the page) | [s.6(13)(a)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=29) |
| Visitor RNOR | Visiting citizen/PIO described in s.6(5), qualifying income exceeding INR 15 lakh, resident with at least 120 but fewer than 182 India days: RNOR (in words on the page) | [s.6(13)(b)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=29) |
| Deemed-resident RNOR | Citizen deemed resident under s.6(7) is RNOR | [s.6(13)(c)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=29) |

1. Choose the correct Act and year. Count actual presence and evidence the totals; do not mix calendar years with the Indian tax year.
2. Apply the basic residence limb, then the alternative limb with the applicable departure/visitor substitution. If neither applies, test deemed residence separately for citizens.
3. For a resident, test all RNOR routes. If none applies, the status is ROR. A person is not NR simply because foreign income is exempt.
4. Apply the income-scope table below. Identify first receipt, accrual, deemed accrual and India-controlled activities, then route the return.
5. Keep a residence memorandum with every year's days, historic residence, qualifying income computation, statutory limb, foreign-tax-liability evidence, treaty position and unresolved fact.

**Qualifying income is not simply Indian-source cash receipts.** Section 6(14) defines foreign-source income as income accruing/arising outside India, excluding income from a business controlled in or a profession set up in India, and excluding income deemed to accrue/arise in India. Compute total income other than that defined foreign income. Exactly the threshold does not satisfy an **exceeds** test. [s.6(14)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=29).

**The visitor FAQ wording is not a separate legal uncertainty.** It says more than the basic day threshold; the enacted basic limb includes equality for every individual. Apply the Act. The 2025-2026 filing-cycle return's residence panel also includes the basic limb without adding a look-back condition to it. The visitor and leaver ticks elsewhere in that panel do not override the statute. [Act s.6](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27); [AY return Part A-GEN](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-04/Notification%20No.46_2026.pdf#page=2).

For eligible Indian-citizen crew of a foreign-bound ship, do not use an ordinary travel-day assumption: rule 8 excludes the qualifying voyage period evidenced by joining/signing-off entries in the Continuous Discharge Certificate. The voyage must meet the rule's India/foreign-port and international carriage conditions. [Notified Rules, rule 8](https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf#page=3).

### Scope of taxable income

| Income | ROR | RNOR | NR | Official source |
|---|---|---|---|---|
| Received/deemed received in India; or accruing/arising/deemed accruing/arising in India | Included | Included | Included | [s.5(1)-(2)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27) |
| Foreign accrual from India-controlled business or India-set-up profession, not received in India | Included | Included | Not included merely by this foreign accrual, subject to deemed Indian accrual | [s.5(1)(c), (2)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27) |
| Other foreign accrual, not received/deemed received or accruing/deemed accruing in India | Included | Excluded | Excluded | [s.5](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27) |

These are inclusion boundaries, subject to any specific exemption and treaty. Foreign salary, rent, interest, dividends and gains each require their own source/receipt analysis. Recording a foreign accrual in an Indian balance sheet does not itself make it received in India; the same income is not included again just because it is later received after inclusion on accrual. Do not equate remitting existing foreign capital with first receipt of income. [s.5(3)-(4)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27).

### Return consequences: 2025-2026 filing cycle only

The following are FY 2025-26 / AY 2026-27 form requirements; they are not a prediction of final Tax Year 2026-27 return fields.

| Point | ROR | RNOR | NR | Official source |
|---|---|---|---|---|
| ITR form | ITR-1/4 only if otherwise eligible, including foreign-item exclusions | ITR-2 without business; ITR-3 with business/profession | ITR-2 without business; ITR-3 with business/profession | [ITR-1 eligibility and foreign-item exclusions](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1); [NR forms](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-0); [ITR-4 eligibility](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs) |
| Schedule FA | Foreign legal/beneficial ownership or beneficiary interests must be examined; covers holdings at any time in relevant calendar year ending 31 December | Not required | Not required | [FA/FSI guide, sections 2 and 5](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/Step%20by%20Step%20Guide%20FA%20FSI.pdf); [AY 2026-27 Schedule FA, PDF p.27](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-04/Notification%20No.46_2026.pdf#page=27) |
| FSI and TR | Report taxable foreign income and eligible relief | Apply to taxable foreign income and eligible relief as a resident | Not applicable | [ITR-2 rules 442-455](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT__e-Filing_ITR%202_Validation%20Rules_AY%202026-27_V1.0.pdf#page=30) |
| Resident rebate | Subject to its income/regime limits | Subject to its income/regime limits | Not available | [ITR-2 rules 533-535](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT__e-Filing_ITR%202_Validation%20Rules_AY%202026-27_V1.0.pdf#page=36) |
| Treaty rate fields | The utility restricts the specified rate fields; credit via FSI/TR remains a separate issue | Same utility limitation; do not treat as a blanket denial of treaties | TRC and Form 10F requirements apply | [ITR-3 rule 37](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/CBDT_e-filing_ITR-3_Validation%20Rules_V1.0_AY%2026-27.pdf#page=6); [ITR-2 category D item 21](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT__e-Filing_ITR%202_Validation%20Rules_AY%202026-27_V1.0.pdf#page=51) |

Record foreign assets even while deciding whether Schedule FA is required. For an NR return, enter jurisdiction of residence and foreign TIN; citizen/PIO panels also ask for current and prior-year India presence. [Notified return, Part A-GEN](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-04/Notification%20No.46_2026.pdf#page=2). See [return assembly](in-return-assembly.md) and [income tax](india-income-tax.md) for filing requirements, belated-return routes, fees and interest; residential status alone does not decide that a return is unnecessary.

### Treaty residence and documentation

Domestic residence and treaty residence are separate conclusions. Dual residence requires the **specific treaty's residence article**, its current protocols and the facts concerning home, personal/economic ties, habitual abode and citizenship. Do not apply a generic tie-breaker order without the operative treaty. A treaty outcome does not erase the domestic residence working or automatically settle every return schedule. Refer disputed dual-status years, competent-authority/mutual-agreement work and unclear foreign tax liability.

| Period/job | Procedure | Official source |
|---|---|---|
| Tax Year 2026-27, NR claiming treaty relief in India | Obtain foreign TRC and foreign TIN; file Form 41 under s.159 and rule 75 | [Form 41 manual](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form41-UM) |
| 2025-2026 filing cycle, NR claiming preferable treaty rate | Form 10F and TRC; the return validation treats the TRC flag as No if the form is absent | [ITR-2 category D item 21](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT__e-Filing_ITR%202_Validation%20Rules_AY%202026-27_V1.0.pdf#page=51) |
| Tax Year 2026-27, Indian resident seeking Indian TRC | Apply in Form 42 to the Assessing Officer under s.159(1)-(2); if satisfied, officer issues Form 43 | [Form 42 manual](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form42-UM) |
| Tax Year 2026-27, resident claiming foreign credit | Form 44 under rule 76, with evidence; foreign tax refunds/disputes need the rule's separate procedure | [Notified Rules, rule 76](https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf#page=54); [official Forms 44/45 guidance](https://www.incometaxindia.gov.in/documents/d/guest/fn-44) |
| 2025-2026 filing cycle, resident foreign credit | Form 67 and FSI/TR under the old Act; do not substitute the new form or assume an obsolete manual's deadline controls | [FA/FSI guide](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/Step%20by%20Step%20Guide%20FA%20FSI.pdf); [dual-residence/credit skill](in-cross-border-india-dual-resident-treaty.md) |

**Form 41 workflow.** Login > e-File > Income Tax Forms > File Income Tax Forms > Forms as per Income Tax Act 2025 > choose Form 41 and tax year. Complete applicant particulars, residential information and declaration; preview and e-verify; retain transaction ID and acknowledgement. PAN users use EVC/DSC as applicable. A nonresident without PAN who is not required to have one uses the separate NR ID category and email/mobile OTPs. The foreign certificate and TIN are prerequisites. Select the old-Act tab for the earlier period's forms. [Manual](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form41-UM).

**Form 42 workflow.** Registered user with active PAN: choose the new-Act forms tab, form and tax year; complete applicant, TRC details, attachments and verification; preview, e-verify and retain acknowledgement. The address must be for the year for which the certificate is sought. Application is not itself a granted certificate. The earlier form was Form 10FA; obtain the applicable old-Act procedure for earlier years. [Manual](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form42-UM); [official form mapping, p.2](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/Navigator%201.pdf).

### Earlier-period section map

| Topic | 2025-2026 filing cycle, 1961 Act | Tax Year 2026-27, 2025 Act | Official source |
|---|---|---|---|
| Basic residence | s.6(1)(a), (c), Explanation 1 | s.6(2)-(6) | [Residence FAQ, Q1-3](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq) |
| Deemed residence | s.6(1A) | s.6(7)-(8) | [Residence FAQ, Q4](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq) |
| RNOR, including visitor/deemed routes | s.6(6)(a), (c), (d) | s.6(13)(a)-(c) | [Old return residence panel](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-04/Notification%20No.46_2026.pdf#page=2); [new Act s.6](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=29) |
| Earlier-year assessments/reassessments | Earlier Act retained | Savings s.536 | [Residence FAQ, Q7-11](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq) |

The old visitor/deemed rules began with FY 2020-21 / AY 2021-22; do not back-apply them to earlier disputes. [NR page](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-0). Earlier years and concessional NRI regimes require their own research.

## Boundary and exception table

| Boundary | Decision | Official source |
|---|---|---|
| Exactly 182 days | Resident under basic limb; departure/visit does not undo it (in words on the page) | [s.6(2)-(5)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27) |
| Under 182 days | Test alternative limb and exceptions, then deemed residence; not automatically NR | [s.6](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=27) |
| Exactly INR 15 lakh qualifying income | Neither high-income visitor substitution nor deemed-residence income condition is met (in words on the page) | [s.6(5), (7)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=28) |
| Visitor alternative limb | Both 120 current days and 365 prior days needed; if resident with fewer than 182 current days, RNOR (in words on the page) | [s.6(5), (13)(b)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=28) |
| PIO without Indian citizenship | Can use visitor rules; cannot be deemed resident under citizen-only rule | [s.6(4), (7)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=28) |
| RNOR historic days | 729 or fewer qualifies; 730 does not qualify on this limb (730 derived); another RNOR limb can still qualify | [s.6(13)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=29) |
| Returning NRI | No fixed RNOR grace period; recalculate all historic tests annually | [s.6(13)](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf#page=29) |

## Worked cases

All presence and income amounts below are illustrative assumed facts. Calculations test the relevant boundary; legal classification follows the method, not a tax-rate computation.

**Returning NRI.** A citizen nonresident throughout the preceding 10 years returns on 1 July 2026 and stays: July-March is 274 days. Resident under the basic limb; RNOR by residence history. In Tax Year 2027-28 the prior history still contains 9 NR years, so RNOR continues. In Tax Year 2028-29 only 8 remain: assumed prior visits of 100 days plus 274 plus the intervening leap-year presence of 366 total 740, exceeding 729. With no other RNOR route, the person is ROR then. Foreign bank interest first received abroad is outside RNOR scope; Pune rent remains included. Foreign income first received in India or from an India-controlled business requires the exception analysis. AY return-schedule rules must not be projected uncritically onto future forms.

```oa-check
name: Returning NRI presence and later RNOR boundary
inputs:
  july_to_december: 184
  january_to_march: 90
  earlier_visits: 100
  intervening_leap_year: 366
steps:
  return_year_days: july_to_december + january_to_march
  basic_test_margin: return_year_days - 182
  later_seven_year_days: earlier_visits + return_year_days + intervening_leap_year
  excess_over_RNOR_limit: later_seven_year_days - 729
expected:
  return_year_days: 274
  basic_test_margin: 92
  later_seven_year_days: 740
  excess_over_RNOR_limit: 11
```

**Visiting PIO, decision both ways.** British citizen of Indian origin, UK-tax-liable, qualifying income INR 2,200,000, prior 4-year presence 400 days. A 130-day visit meets both substituted conditions and gives RNOR; a 110-day visit fails and gives NR. Not an Indian citizen, so no deemed-residence fallback. UK-India treaty residence needs its own text and facts. A UK salary first received abroad, without India source/control conditions, is excluded for either result.

```oa-check
name: Visitor 130 days versus 110 days
inputs:
  income: 2200000
  long_visit: 130
  short_visit: 110
  prior_days: 400
steps:
  income_above_threshold: income - 1500000
  long_margin: long_visit - 120
  short_margin: short_visit - 120
  prior_margin: prior_days - 365
expected:
  income_above_threshold: 700000
  long_margin: 10
  short_margin: -10
  prior_margin: 35
```

**Citizen not liable elsewhere.** Assume an Indian citizen is not liable to tax anywhere else by domicile/residence/similar criteria, has qualifying income INR 1,800,000 and only 45 India days. Assume the remaining day-test facts also fail. The citizen is deemed resident and RNOR. Exactly INR 1,500,000 instead fails the deemed-residence income threshold; on the assumed facts the citizen is NR. Do not infer the liability premise just from living in a no-salary-tax country.

```oa-check
name: Deemed-residence income boundary
inputs:
  qualifying_income: 1800000
  boundary_income: 1500000
steps:
  excess: qualifying_income - 1500000
  boundary_excess: boundary_income - 1500000
expected:
  excess: 300000
  boundary_excess: 0
```

**Employment departure.** Citizen previously resident for many years, assumed no RNOR route. The period 1 April to 30 September 2026 has 183 days: departure for Singapore employment after that presence leaves the person resident/ROR. Even 182 India days remains resident; 181 days fails the basic limb and the employment exception disables the alternative limb. Separately check deemed residence and reliable travel-day treatment. In the resident outcome, foreign salary is within worldwide scope with any eligible foreign credit under the correct year's rules. The 2026-27 new-Act procedure uses Form 44, not the older Form 67.

```oa-check
name: Employment departure boundary
inputs:
  april_to_september: 183
steps:
  basic_test_margin: april_to_september - 182
  earlier_presence: april_to_september - 2
  earlier_margin: earlier_presence - 182
expected:
  basic_test_margin: 1
  earlier_presence: 181
  earlier_margin: -1
```

## When to refuse or refer

- Uncertain travel records, arrival/departure treatment or crew voyages near a day threshold. Do not provide a status from guessed days.
- Dual domestic residence, unclear foreign liability to tax, treaty tie-breaker disputes, competent-authority or mutual-agreement matters.
- Large foreign receipts or structures where source, first receipt, control of a business, setting up a profession or deemed accrual is uncertain. The statutory RNOR rule is confirmed; its application to the client's receipt still needs evidence.
- Company, HUF, firm or trust residence; NRI investment concession, FEMA/banking residence, or disputed years before the labelled filing cycle.
- Foreign credit for disputed/refunded tax, alternate minimum tax, late statements, updated returns or unavailable documents. Use the credit skill; do not improvise a due date.

## Filing and payment

Keep the old-Act filing cycle distinct from the current tax year. Choose the correct Act/year on forms and e-Pay Tax. This skill determines residence and documentation; [income tax](india-income-tax.md), [return assembly](in-return-assembly.md) and [foreign credit](in-cross-border-india-dual-resident-treaty.md) own return timing, tax, interest and statement deadlines.

The transition FAQ describes July 2027 as the ordinary next filing period for Tax Year 2026-27; it does not establish every taxpayer's final form, due date or later extension. The FAQ mentions **31 July 2026 or 31 August 2026** for non-audit AY 2026-27 returns. Those exact historical windows from the old version are preserved here as the FAQ's wording, not as a verified category-specific due date or current filing calendar. Check the applicable statutory category and dated notification in the return workflow. [Returns transition FAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq).

## Completion checklist

- [ ] Year/Act and citizenship/PIO status recorded; departure/visit/crew facts evidenced.
- [ ] Current and historic days reconciled; all resident and RNOR limbs tested separately.
- [ ] Qualifying income and foreign tax liability evidenced, including equality boundaries.
- [ ] Indian source, first receipt and foreign business/profession control considered for every income item.
- [ ] Correct-year return/schedules and treaty/credit forms selected; TRC obtained where required.
- [ ] Residence memorandum and acknowledgement evidence retained; unresolved factual or treaty questions referred.

## Sources

| Official source | Read for | Read on |
|---|---|---|
| [2025 Act, amended by Finance Act 2026](https://www.incometaxindia.gov.in/documents/d/guest/income_tax_act_2025_as_amended_by_fa_act_2026-pdf) | Read for ss.3, 5-6, PDF pp.26-29: year, receipt/source scope, all individual residence and RNOR tests, exceptions and definitions | 2026-11-14 |
| [Notified Rules 2026](https://www.incometaxindia.gov.in/documents/d/guest/en-notified-it-rules-2026-20-03-2026-pdf) | Read for rule 8, PDF pp.3-4, crew voyage exclusion; rule 76, PDF pp.54-55, foreign-credit form and evidence | 2026-11-14 |
| [Residence transition FAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq) | Read for Q1-11: continued residence tests, company boundary, old/new-Act and look-back transition; statute controls visitor equality wording | 2026-11-14 |
| [NR AY 2026-27 page](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-0) | Read for residence introduction, visitor/deemed rules and ITR-2/3 routing; labelled 2025-2026 filing cycle | 2026-11-14 |
| [Notified AY 2026-27 ITR-2](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-04/Notification%20No.46_2026.pdf) | Read for Part A-GEN residence panels, PDF pp.2-3, including NR country/TIN and historic presence; Schedule FA, PDF p.27, calendar year ending 31 December 2025 | 2026-11-14 |
| [ITR-2 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT__e-Filing_ITR%202_Validation%20Rules_AY%202026-27_V1.0.pdf) | Read for rules 442-455, 533-535 and category D item 21: FSI/TR, resident rebate boundary, treaty paperwork | 2026-11-14 |
| [FA/FSI/TR official guide](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/Step%20by%20Step%20Guide%20FA%20FSI.pdf) | Read for sections 2-5: correct forms, taxable foreign income, credit, FA ownership and calendar-year scope, NR/RNOR exclusion | 2026-11-14 |
| [Salaried individual return routing](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) | Read for AY 2026-27 ITR-1 resident-other-than-RNOR condition and exclusions for foreign assets, signing authority and income; no unrelated figures adopted | 2026-11-14 |
| [ITR-4 FAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs) | Read for Q1-2 eligibility and RNOR/NR exclusions for the 2025-2026 filing cycle | 2026-11-14 |
| [ITR-3 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/CBDT_e-filing_ITR-3_Validation%20Rules_V1.0_AY%2026-27.pdf) | Read for rule 37: utility restriction on specified treaty-rate fields, not a general denial of foreign tax credit | 2026-11-14 |
| [Form 41 manual](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form41-UM) | Read for overview, prerequisites, panels, year selection, PAN/NR-ID verification and acknowledgement | 2026-11-14 |
| [Form 42 manual](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form42-UM) | Read for Indian TRC application, officer-issued certificate, year/address and verification workflow | 2026-11-14 |
| [Forms 44/45 official guidance](https://www.incometaxindia.gov.in/documents/d/guest/fn-44) | Read for full guidance, pp.1-5: new-Act foreign-credit forms, documents, deadlines, accountant verification and disputes | 2026-11-14 |
| [Official form mapping](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-06/Navigator%201.pdf) | Read for p.2: old Form 10F to Form 41 and Form 10FA to Form 42 | 2026-11-14 |
| [Returns transition FAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq) | Read for separate earlier-Act return and next-year filing cycle; not treated as a complete live deadline calendar | 2026-11-14 |

Not yet confirmed: general arrival/departure-day counting beyond the specific crew rule; any particular treaty's tie-breaker or its effect on the client's return schedules; final current-year return fields and later deadline extensions. The old section-map entries for the NRI investment-income regime (old ss.115D-115H/new ss.213-217), NRE interest exemption (old s.10(4)(ii)/new Schedule IV), and precise old-Act TRC application/information section mapping were not reverified in this residence job and remain outside usable guidance here. The earlier generic treaty tie-breaker ordering and any fixed returning-NRI RNOR window are not confirmed instructions. Earlier-period Form 67 timing belongs to the credit skill and requires the amended rule, rather than the stale manual deadline.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `in-tax-residency` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/in-tax-residency. If neither is available, confirm every figure against the official source pages cited above before relying on it.
