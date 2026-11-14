---
name: yt-individual-return
description: >
  Prepare a Yukon individual territorial return workpaper using current ordinary bands, the supported income-tested federal basic amount, actual claimant credits and separate settlement-land tax-sharing, refundable credits, utility benefits, resource and historic carbon investigations. Latest actual annual forms read are the 2025-2026 filing cycle.
version: 2.0
jurisdiction: CA-YT
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Yukon individual return v2.0

## Scope

Prepare the territorial part of an individual's Canadian return, including employment and sole-proprietor income. Use supported calendar 2026 ordinary bands, a supported federal basic personal amount and the actual claimant's credit workpapers. The annual forms actually read are expressly the **2025-2026 filing cycle**, not final 2026 return fields. CRA administers the return for Yukon. Corporations and trusts use their own returns. [CRA annual scope](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [2026 amounts](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html).

| Quick reference | Entry |
|---|---|
| Place/currency | Yukon, Canada; CAD |
| Main law | Income Tax Act, R.S.Y. 2002, c.118, as amended; current section numbers below are from the consolidation read, including the separately read 2025 amendment |
| Ordinary individual return | YT428; separate refundable YT479; actual applicable settlement-land tax-sharing form YT432 |
| Contributor | Open Accountants Community |
| Federal business classification | `ca-fed-t2125`; reconcile its result through the federal T1 before territorial tax |
| Full return and settlement | `ca-fed-t1-return`, `ca-return-assembly`, `ca-fed-instalments` |

The ordinary resident route uses year-end Yukon residence. Actual annual CRA instructions also cover the qualifying non-resident with employment income only in Yukon or business income from a permanent establishment only here. A business with permanent establishments in several provinces/territories can require T2203. Do not equate a Canadian newcomer/emigrant with an ordinary move between provinces, or multiply the entire territorial liability by days of local residence. [CRA scope and multi-jurisdiction instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html).

## Ask the client first

1. Obtain the actual tax year, Canadian and territorial residence dates, year-end address and any business permanent-establishment allocation. For death, departure, bankruptcy or separate returns obtain their actual schedules.
2. Obtain reconciled federal taxable income, net income and deductions, the basic personal amount actually supported on the federal workpaper, and employment versus self-employment facts. Higher income can reduce that amount even when taxable income alone looks similar.
3. Obtain marital status, support/custody, spouse/dependant income and age, disability approvals, tuition/transfer/carryforward, CPP/QPP, EI, pension, medical, donation and dividend/foreign-tax records. Do not use the basic personal credit as the entire real return.
4. For settlement-land tax sharing, obtain the actual land/address and residence date, named First Nation and applicable enacted income-tax law and sharing agreement. Citizenship/status and an employer's address do not by themselves settle the result. Keep any actual Indian Act exemption determination separate.
5. Obtain investment certificates and acquisition/disposal/carryover records, fitness receipts/child eligibility, R&D workpapers, fertility receipts and insured-person facts, political receipts, utility-grant and historic carbon statements. Ask about mining/placer royalties and any claimed exploration or flow-through incentive before accepting a credit.
6. What filing/payment authority has the preparer? Obtain prior returns, assessments, instalments, withholding and actual receipts; a prepared return or proposed payment is not an accepted filing or settled liability.

## The method, step by step

### Rates, bands and thresholds

| Item | Supported calendar 2026 amount | Official source |
|---|---|---|
| First ordinary slice | First CAD 58,523 at 6.4% | [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html), [Yukon](https://yukon.ca/yukon-income-tax) |
| Second ordinary slice | Portion over CAD 58,523 through CAD 117,045 at 9% | [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html), [Yukon](https://yukon.ca/yukon-income-tax) |
| Third ordinary slice | Portion over CAD 117,045 through CAD 181,440 at 10.9% | [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html), [Yukon](https://yukon.ca/yukon-income-tax) |
| Fourth ordinary slice | Portion over CAD 181,440 through CAD 500,000 at 12.8% | [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html), [Yukon](https://yukon.ca/yukon-income-tax) |
| Top ordinary slice | Portion over CAD 500,000 at 15% | [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html), [Yukon](https://yukon.ca/yukon-income-tax) |
| Basic personal amount | Maximum CAD 16,452 and minimum CAD 14,829; use the actual income-tested federal amount and claimant restrictions, not the maximum for everyone | [CRA basic amounts](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html), [Yukon](https://yukon.ca/yukon-income-tax), [Act s. 6](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf) |

1. Finish the federal income/deduction workpaper and reconcile taxable income to T1 line 26000. A valid northern, business or other federal deduction can affect this base; do not deduct it again on the territorial calculation. `ca-fed-t2125` owns transaction classification. [Actual YT428 Part A](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf).
2. Establish the actual resident, qualifying non-resident or T2203 route. For arrival/departure, apply the proper corresponding federal/territorial credit restrictions. Do not default unknown residence to Yukon or unknown year to an older table. [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html).
3. Apply each marginal rate only to its slice of taxable income, with continuous boundaries including cents. The current table is a payroll publication, not proof that whole-dollar payroll constants equal final annual rounding. The cases sum the marginal products and round gross tax to cents; final annual field rounding remains a separate check. [Current territorial table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html).
4. Build the supported ordinary credit bases. Yukon follows the specified federal bases and claimant conditions, applying its own percentage/conversion rules; do not take every federal tax credit dollar directly. The actual annual form includes personal, spouse/dependant, age, CPP/QPP, EI, pension, disability/caregiver, tuition/student-loan, adoption/arts, medical and donation work. Donation portions have their own rates. [Act s. 6](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [actual 2025 YT428 Parts B-C](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf), [CRA detailed restrictions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html).
5. On the actual 2025 form, Part C combines gross ordinary tax and territorial TOSI, subtracts ordinary/dividend/minimum-tax-carry credits with a floor, adds additional minimum tax, subtracts foreign tax with a floor, then applies business investment, First Nation and political credits in that printed order. The latest annual fields are not automatically the 2026 fields. [Actual YT428 Part C](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf).
6. Obtain T1206, T691 and foreign-tax workpapers where relevant. The 2025 amendment applies from 2025, using a territorial/federal additional-minimum-tax ratio and a **transitional minimum-tax carryover split by origin year** before 2032. Do not replace that with the old annual form's single printed carryover percentage on every future return. [2025 amending Act ss.2,6](https://laws.yukon.ca/cms/images/LEGISLATION/AMENDING/2025/2025-0006A/2025-0006A.pdf).
7. Complete the separate refundable YT479 and any required YT432, then reconcile the whole federal return, withholding, instalments, benefits and other credits. An ordinary territorial estimate is not a final T1 refund or a complete First Nation tax result. [Actual YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf), [YT432](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf).

### Yukon-specific claims and benefits

- **First Nation tax sharing:** `yt-tax-credits` preserves the complete land/agreement/form investigation. The legislation's credit is for an eligible individual based on the statutory tax-otherwise-payable definition, prescribed percentage and applicable agreement; the actual form also accounts for a transfer of tax. It is not an automatic nil-tax outcome for all status Indians, not limited to citizens earning wages on that land, and not a percentage of the federal abatement substituted for territorial tax. Some consolidation passages show alternative application-period definitions involving other credits; read the applicable commencement and form before finalising the base. [Act s. 12 and application notes](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [regulation](https://laws.yukon.ca/cms/images/LEGISLATION/SUBORDINATE/1999/1999-0184/1999-0184.pdf), [actual YT432](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf).
- **Children's fitness:** the actual annual edition is refundable on YT479, not a non-refundable YT428 credit. Obtain child age/disability, eligible activity/receipts, reimbursement and shared-claim evidence. `yt-tax-credits` owns the detailed expense and disability supplement conditions. [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [actual YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf).
- **Business investment:** an individual investor can have a certified qualifying security credit; it is not mainly a corporate claimant credit. The actual YT428 applies it before First Nation and political credits. Keep eligibility, eligible security, certificate, acquisition/disposal, carryovers, tax-use and deadline evidence. [Act s. 13](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [actual YT428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf).
- **Pioneer Utility Grant:** a separate government application and payment, not a refundable T1 credit flowing through YT428/YT479. The current government page describes age, residence, prior-year income and annual application conditions. Retain its own decision/payment records. Do not put a guessed utility-grant amount on a tax credit form. [Current programme and 2026 application](https://yukon.ca/en/pioneer-utility-grant).
- **Carbon, EC-YT-1:** CRA states that the final individual Yukon carbon price rebate payment was April 2025, and no business rebate applies to a business year ending on or after April 1, 2025. The actual 2025 YT479 still has historical carbon fields. These do not establish a current quarterly federal rebate for Yukon or a continuing 2026 entitlement. Reconcile any historical/late payment to its own period. [CRA changes](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [actual form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf).
- **Mining and placer royalties, EC-YT-3:** obtain the activity, mineral/claim rights, royalty documents, expenditure stage and any flow-through renunciation. The old current mineral credit was not established: a historical official budget describes a time-limited refundable programme, contradicting the old unqualified non-refundable claim. Keep the legal/programme investigation, not an assumed rate or automatic federal-credit stacking. [Historical budget only](https://open.yukon.ca/information/6e6c5d07-2fa4-4841-b743-96a50e3174e6/resource/8ae49b62-3145-3892-8053-c3d5843486af/download/fin-2006-07-budget-address.pdf), [current measures, not proof of every historical entitlement](https://yukon.ca/yukon-income-tax).
- **R&D, fertility and political claims:** preserve their own underlying evidence, deadlines and refundable/non-refundable treatment in `yt-tax-credits`; do not skip them because the ordinary tax has already reached zero. [Act ss.11,15](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [fertility amendment](https://laws.yukon.ca/cms/images/LEGISLATION/AMENDING/2025/2025-0006A/2025-0006A.pdf), [actual YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf).

## Boundary and exception table

| Original code/default or fact | Response |
|---|---|
| R-YT-1, not a year-end resident | Check actual non-resident source-income or T2203 eligibility before refusing all Yukon work; do not apply the resident estimate to unsupported facts |
| R-YT-2, corporation/trust | Use the correct return. Individual employees as well as sole proprietors can use the personal method |
| R-YT-3, part-year residence | Distinguish a domestic move, arrival/departure and multi-jurisdiction business; no universal days-times-tax apportionment |
| R-YT-4, status/settlement land | Obtain the actual exemption or enacted First Nation law and sharing agreement, land and residence facts; no automatic nil-tax conclusion |
| Unknown jurisdiction/year | Ask for the actual year and residence evidence; no older-table fallback |
| EC-YT-1, carbon | Historical final payment and old fields are separate from a present entitlement |
| EC-YT-2, certified investment | Obtain issuer/security/certificate, investor, acquisition/holding/disposal, current/carry credit, tax and deadline evidence |
| EC-YT-3, mining/placer | Preserve resource/royalty and incentive investigation, refer the unsupported legal classification |
| Death, bankruptcy, TOSI/AMT, foreign tax or special returns | Obtain the proper schedules and claimant limits before finalising |

## Worked cases

All four original fact patterns remain. The first three now use current ordinary 2026 bands with a **supplied, independently supported federal basic amount** and no other credits; they are not complete tax returns. No optional prior-cycle figure is silently carried into 2026.

### Case 1: low income

A single full-year resident has taxable and net income CAD 20,000 and a supported federal basic personal amount CAD 16,452. Gross Yukon tax is CAD 1,280; rounded basic credit CAD 1,052.93; basic-only ordinary tax CAD 227.07 before other claims. [Current rates/basic range](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html).

```oa-check
name: Yukon 2026 low-income ordinary estimate
inputs:
  taxable_income: 20000
  supported_basic_amount: 16452
steps:
  - gross: taxable_income * 0.064
  - basic_credit: round(supported_basic_amount * 0.064, 2)
  - ordinary: max(0, gross - basic_credit)
expected:
  gross: 1280
  basic_credit: 1052.93
  ordinary: 227.07
```

### Case 2: middle income

At taxable/net income CAD 90,000 with the same supported maximum basic amount, sum the marginal slices: CAD 3,745.472 plus CAD 2,832.93 gives rounded gross CAD 6,578.40, leaving CAD 5,525.47 before other items. This replaces the old-year estimate without applying a single rate to all income. [Current bands](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html).

```oa-check
name: Yukon 2026 middle-income slices
inputs:
  taxable_income: 90000
  supported_basic_amount: 16452
steps:
  - first: 58523 * 0.064
  - second: (taxable_income - 58523) * 0.09
  - gross: round(first + second, 2)
  - basic_credit: round(supported_basic_amount * 0.064, 2)
  - ordinary: max(0, gross - basic_credit)
expected:
  first: 3745.472
  second: 2832.93
  gross: 6578.4
  basic_credit: 1052.93
  ordinary: 5525.47
```

### Case 3: high income, not the maximum basic amount

A single full-year resident has taxable/net income CAD 600,000 and a supported federal basic amount CAD 14,829. The five slices total gross CAD 71,807.19 rounded; basic credit CAD 949.06; ordinary balance CAD 70,858.13 before special taxes or other claims. Reusing the maximum basic amount at this income is wrong. The supplied amount does not certify an intermediate-income phase-down engine or final annual rounding. [2026 bands and minimum/maximum](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html), [basic-amount linkage](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf).

```oa-check
name: Yukon 2026 high-income marginal calculation
inputs:
  taxable_income: 600000
  supported_basic_amount: 14829
steps:
  - band1: 58523 * 0.064
  - band2: (117045 - 58523) * 0.09
  - band3: (181440 - 117045) * 0.109
  - band4: (500000 - 181440) * 0.128
  - band5: (taxable_income - 500000) * 0.15
  - gross: round(band1 + band2 + band3 + band4 + band5, 2)
  - basic_credit: round(supported_basic_amount * 0.064, 2)
  - ordinary: max(0, gross - basic_credit)
expected:
  band1: 3745.472
  band2: 5266.98
  band3: 7019.055
  band4: 40775.68
  band5: 15000
  gross: 71807.19
  basic_credit: 949.06
  ordinary: 70858.13
```

### Case 4: the original settlement-land employee facts

Retain the original employee's Indian Act status, residence on settlement land of a Yukon First Nation with a Final Agreement income-tax law, and CAD 80,000 employment income earned there. These facts **do not establish** that all income is exempt or territorial tax is nil. First obtain the actual Indian Act/Agreement exemption determination and reconcile whether the income is included in federal taxable income at all. Separately test the enacted First Nation law, applicable sharing agreement, land/residence and YT432 requirements. A credit offsetting part of transferred tax does not cancel the First Nation tax itself. Refer that specific legal result with the documents; complete only the supported ordinary workpaper. [Act s. 12](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [actual YT432 instructions](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf).

## When to refuse or refer

Do not finalise with an unknown year, unreconciled federal income/basic amount, unresolved residence or unsupported material credit. Refer the actual settlement-land/exemption, resource, foreign-tax, investment, AMT/TOSI, death/bankruptcy or allocation issue. Continue the supported ordinary work instead of silently assuming the highest tax, zero credit, old year or nil liability.

## Filing and payment

For calendar 2026, the ordinary individual filing and payment date is 30 April 2027. Qualifying self-employed filing is 15 June 2027 without extending payment, subject to actual statutory exceptions. Use the federal return/assembly owners for the complete filing, instalment, late-filing and interest work. [CRA dates for calendar 2026](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html).

Use the correct year's CRA-certified NETFILE software, an authorised EFILE preparer or required paper route. My Account provides account/assessment access; it is not an interchangeable return-preparation form. Actual 2025 YT428 transfers final tax to T1 line 42800, YT479 transfers its refundable total to line 47900, and the actual YT432 has separate tax-transfer/abatement fields. Do not use a historic carbon Schedule 14 automatically for 2026. [Actual CRA annual instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [YT428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf), [YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf), [YT432](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf).

## Completion checklist

- Actual year, residence/source-income and any T2203 route documented.
- Federal income/deductions and the income-tested basic amount reconciled.
- Current ordinary bands, continuous slices and applicable credit bases used.
- All original income cases and R-YT/EC-YT investigations retained with corrected boundaries.
- Fitness refundability, investment order, separate utility grant and ended carbon correctly distinguished.
- Actual First Nation transfer/exemption result documented; no universal citizen-only or nil-tax shortcut.
- Optional claims, special taxes and correct annual edition/rounding completed or specifically unresolved.
- Final T1 settlement, authorised transmission, accepted acknowledgement, assessment and payment evidence retained separately from the estimate.

## Sources

| Source actually read and scope | Official URL | Read on |
|---|---|---|
| Read for 2026 territorial marginal table and basic amount range; a payroll publication, not final annual field rounding | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032yt-jan/t4032yt-january-general-information.html | 2026-11-14 |
| Read for current government ordinary amounts and incentive/benefit summaries, checking statutory conflicts separately | https://yukon.ca/yukon-income-tax | 2026-11-14 |
| Read for bounded individual rate/credit provisions, First Nation s. 12/application notes, investment s. 13, corporate/M&P and R&D provisions; not a claim of reading every enforcement section or resolving every commencement | https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf | 2026-11-14 |
| Read for all operative 2025 amending provisions, additional-minimum-tax/carryover transition, fertility and commencement | https://laws.yukon.ca/cms/images/LEGISLATION/AMENDING/2025/2025-0006A/2025-0006A.pdf | 2026-11-14 |
| Read for actual 2025 annual claimant, newcomer/non-resident, ordinary-credit, investment, fitness, fertility and carbon-change instructions | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html | 2026-11-14 |
| Read for actual 2025 YT428, three pages, including ordinary credits, special-tax and investment/First Nation/political order | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf | 2026-11-14 |
| Read for actual 2025 YT479, entire refundable-credit and transfer page | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf | 2026-11-14 |
| Read for actual 2025 YT432, entire settlement-land instructions and separate transfer/abatement fields; some percentage fields were not readable in this edition's text | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf | 2026-11-14 |
| Read for prescribed First Nation percentage and historical cross-reference; application of the correct tax base remains separate | https://laws.yukon.ca/cms/images/LEGISLATION/SUBORDINATE/1999/1999-0184/1999-0184.pdf | 2026-11-14 |
| Read for separate Pioneer Utility Grant 2026 eligibility/application/income overview; no application submitted or decision assumed | https://yukon.ca/en/pioneer-utility-grant | 2026-11-14 |
| Read for historical 2006 budget's time-limited mineral credit statement only, not proof of current entitlement or repeal | https://open.yukon.ca/information/6e6c5d07-2fa4-4841-b743-96a50e3174e6/resource/8ae49b62-3145-3892-8053-c3d5843486af/download/fin-2006-07-budget-address.pdf | 2026-11-14 |
| Read for CRA calendar-2026 filing/payment dates in 2027 | https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html | 2026-11-14 |

Not yet confirmed: final 2026 YT428/YT479/YT432, optional indexed credit amounts, exact annual fields and rounding; a complete intermediate-income basic-amount engine; the applicable commencement of the alternative s. 12 tax-base definitions and every refundable-credit interaction, and the federal percentage not readable in actual YT432 text. No First Nation credit is finalised without that determination. Current mineral incentive entitlement/rate/refundability/carryover and specific royalty/Indian Act/Agreement outcomes remain unsupported. Actual claimant, investment certificate, special-tax and allocation workpapers remain required. Latest annual editions read above are the 2025-2026 filing cycle, not final 2026 editions.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (a Canadian CPA familiar with Yukon territorial tax) before filing.
