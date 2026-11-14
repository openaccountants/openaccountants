---
name: nt-individual-return
description: >
  Prepare a Northwest Territories individual income-tax workpaper from federal T1
  income, using supported calendar 2026 ordinary bands and the basic personal
  amount. Apply resident, newcomer/emigrant, non-resident and multi-jurisdiction
  scope; keep optional credits, special taxes, the separate refundable NT479,
  monthly child benefit and employee payroll tax distinct. The latest annual
  forms read are expressly the 2025-2026 filing cycle, not final 2026 fields.
version: 2.0
jurisdiction: CA-NT
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: computation
---

# Northwest Territories individual return v2.0

## Scope

Use for an individual's territorial T1 workpaper, including employment and sole-proprietor income. The ordinary resident route uses Northwest Territories residence at year-end. Actual annual CRA instructions also cover a non-resident of Canada with employment income only in this territory or a business permanent establishment only here. A business with permanent establishments in several provinces/territories can require T2203. Corporations and trusts use their own returns. Do not automatically reject all non-residents or apportion every interprovincial move's tax by days. [CRA annual scope and credit restrictions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html).

| Quick reference | Entry |
|---|---|
| Place/currency | Northwest Territories, Canada; CAD |
| Current ordinary estimate | Calendar 2026 territorial marginal bands and basic personal amount |
| Annual forms actually read | 2025 NT428 and NT479, labelled 2025-2026 filing cycle |
| Main legislation | Northwest Territories Income Tax Act, R.S.N.W.T. 1988, c.I-1, as amended; do not substitute Nunavut's separately amended law |
| Administration | CRA administers territorial T1 income tax; GNWT separately administers employee payroll tax |
| Contributor | Open Accountants Community |

The 2026 CRA payroll table supports current ordinary amounts. It is not a final annual NT428, and its rounded payroll constants are not an annual-return engine. Use the actual return-year forms and law for optional claims and final rounding. The official annual-credit catalogue still offers the 2025 edition read here. [2026 T4032NT](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html), [annual credit catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5012-tc.html).

## Ask the client first

1. What tax year, Canadian and territorial residence dates, year-end province/territory, and business permanent-establishment allocations apply?
2. What are reconciled federal taxable income, net income and the business, investment, northern-residents and other deduction workpapers? Obtain the federal return before the territorial calculation.
3. What spouse/dependant net income, ages, marital/custody/support and disability facts support ordinary credits or the cost-of-living supplement? Obtain the other claimant's return/credit use.
4. What CPP/QPP and EI credit bases, pension, donations, medical, tuition/carryforwards/transfers, dividend designations and foreign taxes are supported?
5. Do T691 minimum tax, T1206 split income, T2203 multiple jurisdictions, bankruptcy, death or separate returns apply? Obtain the underlying schedules, not just an estimated effective rate.
6. What actual Indian Act or Inuvialuit Agreement, royalty/resource, investment certificate, political receipt, child-benefit or historic carbon-offset facts require a specific determination? For employees, separate territorial payroll deductions from income-tax withholding and NT479.

## The method, step by step

### Rates, bands and thresholds

| Item | Calendar 2026 amount and conditions | Official source |
|---|---|---|
| First ordinary band | First CAD 53,003 at 5.9% | [CRA 2026 territorial table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html) |
| Second ordinary band | Portion over CAD 53,003 through CAD 106,009 at 8.6% | [CRA 2026 territorial table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html) |
| Third ordinary band | Portion over CAD 106,009 through CAD 172,346 at 12.2% | [CRA 2026 territorial table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html) |
| Top ordinary band | Portion over CAD 172,346 at 14.05% | [CRA 2026 territorial table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html) |
| Basic personal amount | CAD 18,198 ordinary full-year base; the 5.9% value is computed CAD 1,073.68 rounded to cents, before applicable claimant/proration limits | [CRA 2026 basic personal amount](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html) |

1. Finish the federal T1 income/deduction workpaper and reconcile taxable income to line 26000 before NT428. Transaction classification remains in `ca-fed-t2125`; northern deductions require the correct federal eligibility/address workpaper. A valid federal deduction affects the territorial income input; do not deduct it twice. [Actual 2025 NT428 Part A](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-c/5012-c-fill-25e.pdf).
2. Establish resident, qualifying non-resident or T2203 allocation scope. Canadian arrival/departure can restrict specified territorial credits in the same way as corresponding federal amounts. An ordinary interprovincial move does not establish a day-times-final-tax rule. [CRA scope/newcomer/emigrant rules](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html).
3. Apply each ordinary rate only to its slice of taxable income. Maintain continuous boundaries, including cents; do not leave a gap between printed whole-dollar endpoints. Compute the federal and territorial liabilities separately. The worked cases below sum marginal-band products before rounding; final annual form/field rounding must be checked against that year's actual edition. [2026 bands](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html).
4. Build supported ordinary credit bases. The actual annual form includes personal, age, spouse/eligible-dependant/infirm-dependant, CPP/QPP, EI, pension, caregiver, disability, student-loan interest, tuition/education/transfers and medical amounts. Use territorial bases and claimant/transfer/overlap restrictions; these are not necessarily the federal amounts. Calculate donations separately. Do not stop after the basic personal credit on a real return. [Actual 2025 NT428 Parts B-C](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-c/5012-c-fill-25e.pdf), [CRA detailed eligibility](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html).
5. Reconcile special-tax schedules and direct credits in their correct order. Actual 2025 NT428 Part C adds gross ordinary tax and territorial TOSI; subtracts ordinary/dividend credits and minimum-tax carryover with a floor; adds current additional minimum tax; subtracts the territorial foreign credit with a floor; then applies the political credit with a floor. T1206, T691 and T2036 need their own underlying workpapers. Do not substitute a Manitoba or Nunavut field number. [Actual 2025 NT428 Part C](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-c/5012-c-fill-25e.pdf).
6. For actual 2025, the political credit is for qualifying contributions to an Assembly candidate with an official signed receipt. It is non-refundable on NT428, not another NT479 refund. The actual threshold/cap and worksheet belong to that edition; final 2026 fields/amounts are not inferred here. [CRA political instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html).
7. Complete the separate refundable NT479 using adjusted **net** income, not taxable income. Transfer the correct year's territorial tax and refundable credits separately to the federal return. The difference of these components is not a final T1 refund before federal tax, withholding, instalments and other credits. [Actual 2025 NT428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-c/5012-c-fill-25e.pdf), [actual 2025 NT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf).

### Actual 2025-2026 filing cycle: cost-of-living credit

This is the latest actual annual edition read, not a certification of final 2026 optional figures. Establish year-end territorial residence, adjusted income and any T2203 allocation. Begin with federal line 23600, subtract the specified lines 24400/25000 with a floor, then the treaty-exempt foreign income from line 25600 with a floor. A business with outside-territory permanent establishments uses the allocated net income described by CRA. [NT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf), [CRA allocation instruction](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html).

| Actual 2025 NT479 item | Amount and limitation | Official source |
|---|---|---|
| Basic first slice | 2.6% of adjusted net income through CAD 12,000 | [NT479 chart](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf) |
| Basic second slice | CAD 312 plus 1.25% of the portion over CAD 12,000 through CAD 48,000 | [NT479 chart](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf) |
| Basic third slice/cap | CAD 762 plus 1% of the portion over CAD 48,000; maximum CAD 942 at adjusted net income CAD 66,000 or more | [NT479 chart](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf) |
| Supplement | Eligible claimant at least 18 at year-end: floor of CAD 350 for self plus CAD 350 if a spouse/common-law partner exists, minus the applicable basic credits for self and spouse. Only one spouse claims the family supplement; final form maximum CAD 942 | [NT479 supplement and CRA household rule](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf), [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html) |

Refundability does not require positive territorial tax and is not a repayment of the exact payroll tax withheld. The basic credit does not phase out at high income; the supplement tops up a low basic amount under the actual family rule rather than adding a guessed amount on an old income interval. Do not assume the maximum without income/family facts. [NT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf).

### Preserve the separate benefit and special-credit investigations

- **Child benefit:** a separate non-taxable monthly benefit assessed from application/return information and paid with the federal child benefit. It is not an NT428 or NT479 ordinary credit. Check actual family and benefit-period records; do not invent current benefit amounts. [CRA benefits](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html).
- **Carbon offset, EC-NT-2:** CRA records the cost-of-living offset's final payment in April 2025. That ended offset is different from the continuing annual NT479 credit. Do not promise a current quarterly carbon payment based on an old territorial-tax description. Reconcile any historic/late payment to its actual entitlement. [CRA 2025 changes](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html).
- **Risk-capital investment:** retain certificate, investor/issuer, eligible security, issue/acquisition, relationship, holding/disposition and carryover evidence. The old flat 30%, CAD 200,000 lifetime investment/CAD 60,000 credit and unconditional carryback/carryforward statement was not established from current legislation. Do not use it or claim a certificate merely because the old summary lists it. The current investment statute, programme, schedule, rate/class and tax-use limits remain specifically unconfirmed.
- **Resource royalties, EC-NT-3:** reconcile the actual diamond/gold/oil/gas activity, ownership and Mackenzie Valley/resource-agreement workpaper. Do not treat all resource receipts as ordinary sole-proprietor sales without analysis.
- **Inuvialuit/Indian Act, EC-NT-4 and R-NT-4:** obtain the actual recipient, income connection and controlling Agreement/statute. A status, beneficiary or address label does not establish either a blanket exemption or universal taxability. Refer the actual disputed legal issue.
- **Employee payroll tax:** use `nt-payroll-tax` for the separate GNWT levy. Residence affects personal-return eligibility, not the employee-tax work-location test. A personal credit is not a dollar-for-dollar refund of payroll withholding. [GNWT employee explanation](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees).

## Boundary and exception table

| Original code/situation | Response |
|---|---|
| R-NT-1, residence not established | Determine actual year-end residence and any valid non-resident/source-income or T2203 route; do not apply a resident estimate indiscriminately |
| R-NT-2, corporation/trust | Use the correct return; individual employees and sole proprietors are both within this method |
| R-NT-3, part-year residence | Separate arrival/departure credit restrictions from an interprovincial move; obtain the actual allocation, not a days-times-entire-tax shortcut |
| R-NT-4, Indian Act question | Refer actual income, recipient, location connections and controlling provision before deciding exemption |
| EC-NT-1, cost-of-living supplement | Obtain adjusted income, age, spouse's basic credit and the one-family claimant; no assumed maximum or phase-out |
| EC-NT-2, carbon offset | Distinguish historic final payment from continuing annual credit; no future payment promise |
| EC-NT-3, resource royalty | Obtain activity/agreement/ownership classification and refer the contested resource issue |
| EC-NT-4, Inuvialuit beneficiary | Obtain actual legal instrument, recipient and distribution; do not apply an assumed automatic outcome |
| Year unknown | Ask for the year instead of defaulting to an older table |
| Special tax, bankruptcy/death or multiple jurisdictions | Obtain actual federal/territorial schedules and claimant limits before finalising |

## Worked cases

These retain all three original income scenarios. They are ordinary marginal-band workpapers with only the basic personal amount, not complete returns. Final annual field/rounding remains a separate check. No optional 2025 credit is silently carried into 2026.

### Case 1: low income, with a dated refundable comparison

At calendar 2026 taxable income CAD 20,000, gross territorial tax is CAD 1,180 and the rounded basic personal credit is CAD 1,073.68, leaving CAD 106.32 before other/special/refundable items. For the actual 2025 filing-cycle comparison at the same taxable and adjusted net income, the actual basic amount is CAD 17,842, not the old approximate CAD 17,373. A marginal-band workpaper therefore gives CAD 127.32 ordinary tax, and NT479 basic living credit is CAD 412 with no additional supplement for an otherwise eligible single adult. The component difference is minus CAD 284.68, not the invented CAD 1,723.01 refund. [2026 amounts](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html), [actual 2025 basic amount](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-c/5012-c-fill-25e.pdf), [NT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf).

```oa-check
name: NWT low-income ordinary 2026 and dated 2025 living credit
inputs:
  taxable_income: 20000
  adjusted_net_income_2025: 20000
steps:
  - gross: taxable_income * 0.059
  - basic_credit_2026: round(18198 * 0.059, 2)
  - ordinary_2026: max(0, gross - basic_credit_2026)
  - basic_credit_2025: round(17842 * 0.059, 2)
  - ordinary_2025_estimate: max(0, gross - basic_credit_2025)
  - living_basic_2025: 312 + (adjusted_net_income_2025 - 12000) * 0.0125
  - single_supplement_2025: max(0, 350 - living_basic_2025)
  - component_difference_2025: ordinary_2025_estimate - living_basic_2025 - single_supplement_2025
expected:
  gross: 1180
  basic_credit_2026: 1073.68
  ordinary_2026: 106.32
  basic_credit_2025: 1052.68
  ordinary_2025_estimate: 127.32
  living_basic_2025: 412
  single_supplement_2025: 0
  component_difference_2025: -284.68
```

### Case 2: mid-range income is not a guessed refund

At calendar 2026 taxable income CAD 80,000, sum the first and second marginal-band products, then round gross ordinary tax to CAD 5,448.92. Subtract the rounded basic-only credit for CAD 4,375.24 before other items. For actual 2025 adjusted income at the same level, the living credit is capped at CAD 942; it is not CAD 1,878 plus an invented supplementary credit. The separate payroll example in `nt-payroll-tax` shows why this is not a full refund of payroll withholding. [2026 bands/basic amount](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html), [actual NT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf).

```oa-check
name: NWT 2026 middle ordinary bands before optional credits
inputs:
  taxable_income: 80000
steps:
  - first_slice: 53003 * 0.059
  - second_slice: (taxable_income - 53003) * 0.086
  - gross: round(first_slice + second_slice, 2)
  - basic_credit: round(18198 * 0.059, 2)
  - ordinary: max(0, gross - basic_credit)
expected:
  first_slice: 3127.177
  second_slice: 2321.742
  gross: 5448.92
  basic_credit: 1073.68
  ordinary: 4375.24
```

### Case 3: high income does not phase out the living basic credit

At calendar 2026 taxable income CAD 250,000, the four marginal slices give rounded gross CAD 26,689.19 and basic-only ordinary tax CAD 25,615.51. For a separate actual 2025 NT479 workpaper at adjusted net income CAD 250,000 and otherwise valid residence, the basic credit still reaches its cap; the old “fully phased out” claim is false. This is not permission to carry that annual amount into a final 2026 return. [2026 ordinary amounts](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html), [NT479 high-income instruction](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf).

```oa-check
name: NWT 2026 high-income marginal portions
inputs:
  taxable_income: 250000
steps:
  - band1: 53003 * 0.059
  - band2: (106009 - 53003) * 0.086
  - band3: (172346 - 106009) * 0.122
  - band4: (taxable_income - 172346) * 0.1405
  - gross: round(band1 + band2 + band3 + band4, 2)
  - basic_credit: round(18198 * 0.059, 2)
  - ordinary: max(0, gross - basic_credit)
expected:
  band1: 3127.177
  band2: 4558.516
  band3: 8093.114
  band4: 10910.387
  gross: 26689.19
  basic_credit: 1073.68
  ordinary: 25615.51
```

## When to refuse or refer

Do not finalise with an unknown year, unresolved residence, unreconciled federal income or an unsupported material claim. Complete the supported ordinary work and identify the exact missing determination. Refer actual non-resident/treaty, Agreement/Indigenous, royalty, investment, AMT/TOSI, bankruptcy/death and disputed allocation cases with their documents. Do not invent a maximum, prior-year fallback, no-credit default or completed filing.

## Filing and payment

For calendar 2026, the ordinary individual filing/payment date is 30 April 2027. Qualifying self-employed filing is 15 June 2027 without extending payment, subject to the actual statutory exceptions. Use `ca-fed-t1-return`, `ca-return-assembly` and `ca-fed-instalments` for the full return, penalty/payment and instalment work. [CRA deadlines naming 2027 dates](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html).

Use the correct year's CRA-certified NETFILE software, an authorised EFILE preparer or the required paper return. MyAccount is an account/assessment access route, not an interchangeable tax-preparation form. Actual 2025 NT428 is completed after federal steps 1-5, and its final tax goes to T1 line 42800; NT479 goes separately to line 47900. NT(S2) transfers specified spouse amounts, not the whole territorial tax computation. Preserve actual tuition/transfer schedules and required paper attachments. [CRA annual instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html), [NT428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-c/5012-c-fill-25e.pdf), [NT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf).

Retain the prepared return, source and review workpaper, authority to transmit, accepted filing acknowledgement, notice of assessment, withholding/instalment reconciliation and settlement evidence. Preparing or exporting a return is not an accepted filing or payment. This method does not sign in, register, transmit or pay for the taxpayer.

## Completion checklist

- Actual year/residence and any source-income/T2203 route documented.
- Federal taxable/net income reconciled; valid northern/business deductions not duplicated.
- Current ordinary bands and territorial credit bases used; no whole-income top-rate shortcut.
- Optional claimant, transfer, medical/donation and special-tax workpapers completed where applicable.
- Adjusted net income distinguished from taxable income, and NT479 refundability/household supplement handled correctly.
- Political, investment, monthly benefit, ended carbon offset and employee payroll tax kept separate.
- All original R-NT and EC-NT investigation jobs retained or explicitly unresolved.
- Actual annual editions and final-rounding gaps labelled; no older fallback presented as current.
- Final T1 settlement and accepted filing/payment evidence kept separate from the territorial estimate.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| Read for CRA 2026 T4032NT territorial bands, indexing and basic amount; payroll-purpose limitation retained | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nt-jan/t4032nt-january-general-information.html | 2026-11-14 |
| Read for Actual 2025 NT428, all three pages: income/ordinary-credit categories, personal amount, special-tax order, political credit and final tax handoff | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-c/5012-c-fill-25e.pdf | 2026-11-14 |
| Read for Actual 2025 NT479, entire one-page adjusted-income, basic three-slice formula, family supplement, cap and refundable handoff | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf | 2026-11-14 |
| Read for CRA actual 2025 territorial eligibility, non-resident/newcomer rules, ordinary-credit/transfer instructions, ended carbon offset, political, monthly child-benefit and T2203 jobs | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html | 2026-11-14 |
| Read for Annual credit catalogue identifying the available 2025 edition; not evidence of a final 2026 annual form | https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5012-tc.html | 2026-11-14 |
| Read for GNWT employee payroll-tax explanation, separate incidence, work-location scope and T4 distinction; detailed payroll method owns its law | https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees | 2026-11-14 |
| Read for CRA factsheet read for 2027 filing/payment dates for calendar 2026; URL year not mistaken for the return year | https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html | 2026-11-14 |

Not yet confirmed: final 2026 NT428/NT479, optional credit amounts, annual field references and rounding; the complete current investment statute/programme, eligible certificate/class, exact rate/caps/carryover/holding/recapture and federal interactions. The old 30% and lifetime CAD 200,000 investment/CAD 60,000 credit are not established usable figures. Actual northern address/eligibility, Agreement/Indian Act/resource result, special taxes and multi-jurisdiction allocations need their own supported workpapers. The annual edition above is explicitly the latest 2025-2026 filing cycle read, not a claim that every 2026 optional credit was published.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Canadian CPA familiar with NWT territorial tax before filing.
