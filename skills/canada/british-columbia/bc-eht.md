---
name: bc-eht
description: >
  Calculate, reconcile and prepare British Columbia Employer Health Tax for
  2026, including BC remuneration, permanent establishments, regular and
  charitable employers, qualifying locations, associated-group allocations,
  part-year thresholds, eTaxBC return fields, instalments and final payment.
  Use for BC EHT, BC payroll health tax, the 1 million exemption, 1.5 million
  threshold, charity 4.5 million band and eTaxBC Employer Health Tax returns.
  Read with canada-payroll; Ontario employer health tax uses on-eht.
version: 1.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
category: payroll
domain: payroll
type: computation
---

# British Columbia employer health tax v1.1

## Scope

Prepare a calendar-2026 BC Employer Health Tax (EHT) computation, remuneration reconciliation, instalment schedule and eTaxBC return working paper. Amounts are CAD. The BC Ministry of Finance administers this employer-only tax under the Employer Health Tax Act, SBC 2018, chapter 42. It is separate from CRA payroll deductions, workers' compensation and Ontario EHT. This skill is **Built from the law** and **Not yet approved**. [Act sections 1 and 8](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [current overview](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview).

Use [canada-payroll](../canada-payroll.md) for the payroll run and [on-eht](../ontario/on-eht.md) for Ontario establishments. Do not copy one province's exemption, association test, rate bands or return into the other. This method prepares proposed work; submission, certification, payment and posting require an authorized person's sign-off.

## Ask the client first

1. Which calendar year, legal employer and nine-digit business number? Obtain all CRA payroll-account T4 Summaries and applicable T4/T4A slips, payroll registers, benefits and stock-option records, and the EHT account/assessment history. Confirm authorized eTaxBC access exists; do not ask for passwords in a public working paper.
2. Where did the employer have actual or deemed permanent establishments, and on which dates? For each worker or officeholder, obtain the reporting/attachment facts, paying establishment and relevant former-employment facts. Employee residence or the CRA withholding province alone does not settle BC EHT.
3. What ownership, control, partnership or trust relationships existed on December 31? Obtain the entire associated group's BC remuneration, operational days and signed exemption-allocation agreement, not only the entity's own payroll.
4. Is the employer a statutory charitable or non-profit employer on the relevant year-end or last-BC-establishment date? Obtain legal status and government-entity exclusions. If claiming multiple locations, obtain leases, exclusive-use/occupancy and contiguous-premises facts, and employee attribution records.
5. What was actual 2025 EHT, the reasonable 2026 estimate, instalments already received, prior-year credits and outstanding notices? Was there an amalgamation, acquisition, bankruptcy, cessation or account closure? Obtain the actual event date and instructions.

Missing facts remain open items. Do not default uncertain remuneration into tax, invent an exemption allocation, assume ordinary charity status or create an instalment obligation from a current projection alone.

## The method, step by step

### 1. Determine the employer, BC establishment and employee connection

Apply the BC Act's own definitions and deeming rules. A permanent establishment includes a fixed place of business; section 4 also deems establishments for registered offices, certain employees/agents, owned or leased premises, substantial machinery/equipment and other stated cases. Reporting for work includes in-person attendance or reasonable attachment. Review duties, work location, hiring, supervision, instructions, records and equipment as relevant. [Act sections 1, 4 and 5](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [BC attachment guidance](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration); [permanent establishments](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/permanent-establishment).

For a current employee who reports at a BC establishment at any time in the year, section 3 can include the year's remuneration even where the person also reports elsewhere. The exception is where the commissioner is satisfied that reporting outside BC was for all or substantially all of the year. A worker who reports at no establishment is tested by payment from or through a BC establishment. Former employees have their own last-employment rule. Do not invent a federal Regulation 102 working-days allocation or use residence as the test. [Act sections 1 and 3](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [BC remuneration](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration).

Officeholders, including directors, are within the employee definition; a director's BC residence alone does not determine the EHT allocation. Where a non-resident related employer supplies workers to a BC business, check the complete deemed-employer conditions in section 6. A foreign business is not automatically outside EHT. Hold a disputed establishment, attachment or section-6 conclusion for professional resolution before producing a final liability.

### 2. Reconcile remuneration once, including taxable benefits correctly

The starting definition is payments, benefits and allowances included, or deemed included, in employment income under federal Income Tax Act sections 5, 6 or 7, including the corresponding non-resident rule. It is not simply cash wages, a T4 province field or an unadjusted T4 total. [BC Act sections 1 and 2](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [official inclusions and exclusions](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration).

| Payment or adjustment | Treatment to establish | Official source |
|---|---|---|
| Salary, wages, bonuses, commissions, taxable allowances, vacation and employer-paid tips | Include taxable employment remuneration in the applicable payment/deemed-payment year; establish BC connection separately | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration |
| Group life insurance, taxable stock options, employer RRSP contributions, EPSP/employee trust amounts | Apply actual taxable/deemed amount and timing; no general life-insurance monetary exemption. Do not add benefits already counted in T4 income again. | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration |
| Private health services plan, registered pension, SUB, deferred profit sharing and retirement compensation arrangements | Apply the stated exclusion for the employer contribution/premium and classify any separate taxable payment correctly | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration |
| Retiring allowances/severances, pension/annuity/superannuation to a retired employee, death benefits and dividends | Exclude the properly classified amount; an RRSP rollover is not a condition for excluding a retiring allowance. Separate ordinary wages, vacation and payment in lieu of notice from an actual retiring allowance. | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration |
| Expense reimbursement or non-taxable allowance | Establish the underlying facts and federal tax treatment. A label such as allowance or reimbursement is not enough. | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration |
| Plan contribution already included as remuneration | Do not count it again when later allocated/paid; reconcile the timing under section 2 | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration |
| First Nations/reserve or other disputed statutory exclusion | Obtain the specific status, business, work and situs facts and applicable official exclusion; do not infer it solely from identity or address | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration |

For the ordinary employer return, reconcile all T4 Summary line-14 amounts under the same business number to EHT line 100. Deduct qualifying non-BC remuneration at line 110; line 120 is the subtotal. Add only BC remuneration not already included in that total, for example eligible T4A/other-slip amounts, at line 130. Line 190 is line 120 plus line 130. Preserve a worker/payment-level bridge from payroll and slips to these adjustments. A stock-option benefit already in the line-14 total is not added again. [Official return instructions, Step 2](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay/filing-employers).

### 3. Select the correct employer schedule and calendar year

Determine charitable/non-profit status and associated-group status before applying the ordinary table. Use the group or location method below where required. The following ordinary rates apply for 2024 onward, including 2026, to a full-year unassociated regular employer.

| Ordinary BC remuneration R | Annual EHT rate and amount | Authority and official source |
|---|---|---|
| R at most 1,000,000 | Zero | Act section 10: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview |
| R greater than 1,000,000 and at most 1,500,000 | 5.85% x (R minus 1,000,000) | Act section 11: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview |
| R greater than 1,500,000 | 1.95% x all R; no 1,000,000 deduction | Act section 8: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview |

The 5.85% is the rate on the excess within the notch, not the effective rate on all remuneration. At R of 1,500,000, EHT is 29,250 and the effective rate is **1.95%**. The old 2.925% effective-rate statement was wrong. Cents above a boundary must not be lost by writing the next band as beginning at 1,000,001.

If the employer has a BC establishment for only part of 2026, let D be the number of days with at least one BC establishment. Under section 12, prorate **both** the exemption E = 1,000,000 x D/365 and upper threshold U = 1,500,000 x D/365. Apply zero through E, 5.85% of R minus E through U, and 1.95% of all R above U. Do not prorate payroll itself again or give the full exemption to a new successor. Keep the exact working precision and reconcile to the portal's calculated fields. [Act section 12](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [part-year guidance](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview).

### 4. Apply the associated-employer rules and actual allocation

For 2026, test association on **December 31**, using federal section 256 as modified by BC Act sections 13-16. The BC rules extend to individuals, partnerships and trusts; federal elections or exclusions cannot simply be imported. Charitable/non-profit employers are excluded from ordinary group sharing, but links through a charity can still connect two ordinary employers. Anti-avoidance rules can also deem association. [Act sections 13-16 and 53](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [group guidance](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-associated-employers).

Combine BC remuneration for the associated employers and establish group BC-establishment days. For a full-year group:

| Group BC remuneration G | Entity calculation | Official source |
|---|---|---|
| G at most 1,000,000 | No tax under section 17 | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-associated-employers |
| G greater than 1,000,000 and at most 1,500,000 | If section 18 conditions are met, each member pays 5.85% of its remuneration above its valid allocated exemption, or zero if it is within that exemption | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-associated-employers |
| G greater than 1,500,000 | Each member pays 1.95% of its own full BC remuneration; the group does not keep the exemption | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-associated-employers |

Where every member is part-year, section 17/18 uses the days on which **at least one** member had a BC establishment to prorate the group exemption and upper threshold. An individual member's allocation is also limited by its own establishment-day maximum. Allocate no more than the group maximum and no more than each member's statutory maximum. Preserve every member's agreed share and verify the totals.

Section 18's notch relief is conditional on the allocation-agreement requirements. Guidance implements the annual filing through the **Association Summary** and says to retain the written allocation agreement for request rather than attach it to the annual return. Keep that evidence and satisfy the commissioner's required process. Do not replace these steps with a supposed Schedule B or an invented ministerial zero-allocation decision. Nor treat missing agreement as permission to charge 5.85% from dollar one: section 18 relief and section 8's baseline rate are distinct. Resolve an incomplete allocation before finalizing the return. [Act section 18](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [retained agreement](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-associated-employers); [Association Summary instructions](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay/filing-associated-employers).

### 5. Apply the charitable/non-profit schedule and location tests

A qualifying employer is a registered charity or an organization described in federal Income Tax Act paragraphs 149(1)(e), (g), (i), (j), (k) or (l), subject to BC Act exclusions including the government reporting entity. Do not reduce non-profit eligibility to paragraph (l) alone. Status is tested on the last day of the year or applicable last BC-establishment day. [Act sections 1, 19 and 24](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042).

For an eligible employer outside the multiple-qualifying-location division, apply sections 20-22. Where there are at least two qualifying locations, apply sections 23-30 and sum the location liabilities. A qualifying location requires the exclusive right to occupy premises, sole use/occupancy by the employer and the Act's treatment of contiguous premises. Merely having separate addresses or an employee at a place does not establish separate exemptions. Attribute each worker under section 25: primarily reporting location for multiple-location workers, or a reasonable location allocation for a worker reporting nowhere, ensuring all BC remuneration is attributed. Do not freely split one employee's pay to create exemptions.

| Full-year eligible employer, or qualifying location under the multiple-location method | EHT rate and amount | Official source |
|---|---|---|
| R at most 1,500,000 | Zero | Act sections 20/27: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |
| R greater than 1,500,000 and at most 4,500,000 | 2.925% x (R minus 1,500,000) | Act sections 21/28: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |
| R greater than 4,500,000 | 1.95% x all R | Act sections 8/29: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |

Under sections 22/30, prorate the 1,500,000 and 4,500,000 thresholds for part-year BC establishment using the prescribed employer BC-establishment days/365. Do not automatically use each location's opening date as a separate proration rule. For multiple locations, sum their resulting tax; do not apply the ordinary 1,000,000 exemption as well. Obtain a ruling where exclusive occupancy, location grouping or attribution is disputed.

**Zero tax is not always no return.** A multiple-qualifying-location charity with aggregate BC remuneration above 1,500,000, or the section-30 prorated amount, has the separate registration/return obligation under sections 31/32 even if each location owes zero. The three-location example below deliberately preserves that distinction.

### 6. Determine actual instalments and the final balance

The trigger is **2025 EHT greater than 2,925** for 2026 instalments. The Act does not create that obligation merely because the 2026 projection exceeds 2,925. Once triggered, there are three instalments, each at least 25% of the lesser of actual preceding-year tax and reasonably estimated current-year tax. The remaining balance is due with the annual return. An estimate that understates both actual current and prior liabilities can cause deficiency interest. Reconcile payments already made before changing the estimate midyear. [Act sections 41 and 62](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [Regulation section 3](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/268_2018); [payment guidance](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay).

| 2026 ordinary obligation | Date | Official source |
|---|---|---|
| First, second and third instalments, if required | June 15, September 15 and December 15, 2026 | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay |
| Registration if this is the first required year | December 31, 2026; apply the separate charity condition too | Act section 31: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview |
| Annual 2026 return and remaining payment | March 31, 2027 | Act sections 32/42: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview |
| Deadline falling on weekend or BC statutory holiday | Next business day under official filing/payment guidance | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay |

These ordinary 2026 dates are weekdays. March 31 is the final balance, not a fourth equal instalment. Use eTaxBC or the stated bank/financial-institution method, the correct EHT account and actual received/payment evidence. A CRA payroll remittance does not discharge BC EHT.

### 7. Prepare, approve, file and reconcile the return

Determine the registration/return requirement under sections 31/32 rather than assuming that registration itself proves current tax is payable. Prepare eTaxBC registration when required; arrange authorized account access separately. The law requires electronic returns under section 38; there is no verified charity paper-return exception. [Act sections 31/32/38](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042).

For an ordinary unassociated employer, use the official eTaxBC steps in this order. The associated method adds the Association Summary; use the relevant charity workflow where that division applies. [Ordinary return instructions](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay/filing-employers); [associated return instructions](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay/filing-associated-employers).

1. In the authorized account, select **Employer Health Tax**, then **File Return** for the correct period. Check the default period/due date, amalgamation predecessor/successor, December-31 association, final-year and BC-establishment declarations.
2. Reconcile BC remuneration at lines 100, 110, 120, 130 and 190 as in Method 2. Do not enter an assumed tax province or add already-included benefits.
3. Check ordinary exemption-eligibility fields: line 200 days, line 202 upper threshold, line 203 BC remuneration, line 204 exemption limit and line 205 available exemption. For a group, enter all required members, business numbers, remuneration, days and agreed shares in the Association Summary; compare both individual and group maxima.
4. Reconcile line 300 remuneration, line 310 applied exemption, line 320 taxable remuneration, line 700 rate and line 770 tax. Check the selected branch before relying on portal arithmetic.
5. Reconcile line 840 instalments received, line 842 prior-year overpayment, line 844 subtotal and line 846 tax due or overpaid. Investigate a missing payment/credit instead of manually deducting it twice. Select permitted carryforward/refund treatment for an overpayment.
6. Give the complete working paper and unresolved items to the authorized person before certification/submission. Certification identifies the signer's first name, last name and position and requires acceptance of the displayed statement. After authorized submission, retain the confirmation number and filed return; arrange the separately authorized payment and retain its reference/receipt.
7. Compare the Notice of Assessment with the calculation, account and general ledger. Record any explanation or correction. Preserve an amendment trail and use the actual voluntary-disclosure/waiver/objection route where relevant; do not silently alter an already filed return.

EHT is an employer expense, not an extra employee deduction. Reconcile the tax expense/payable, instalment payments and final balance in the accounts; propose journals/imports for human approval. Official BC guidance states business-income deductibility. Use the employer's applicable income-tax return and accounting policy; do not invent a Canadian corporate-return skill slug or post to a read-only ledger. [BC overview](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview); [canada-bookkeeping](../canada-bookkeeping.md).

## Boundary and exception table

| Situation | Required treatment | Official source |
|---|---|---|
| Uncertain employee, taxable benefit, option timing or former-employee amount | Resolve classification/timing before final computation; no automatically taxable default | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration |
| Foreign/remote work or disputed BC establishment | Apply BC attachment, deemed establishment/employer and all-substantially-all exception; obtain resolution where disputed | Act sections 1-6: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration |
| Uncertain ownership, charity status or location eligibility | Obtain evidence; do not manufacture either relief or an inflated liability from missing facts | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-associated-employers |
| Association arranged to reduce EHT | Check specific section 16(3)(d) and general section 53 anti-avoidance, not the old section-32 reference | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |
| Bankruptcy, last BC establishment ceases, insolvency or winding up | Check sections 33-40 special returns, notices and distribution certificate; ordinary March 31 may not apply | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |
| Amalgamation, acquisition or successor | Identify the predecessor/successor and dates; prorated/new-employer treatment and ministry instructions need the actual transaction, not an assumed reused exemption | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay/filing-employers ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay |
| Audit, reassessment, objection or disputed coverage | Preserve notice dates and refer the disputed matter to an appropriately experienced practitioner; do not treat this ordinary computation as a resolved appeal | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay ; https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |
| Old increased-employment credit in the Act | Part 2.1 refers to 2020 base/qualifying periods and a December 31, 2021 application deadline; it is not a 2026 payroll credit | Act sections 30.01/30.06: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |

## Worked cases

### Case 1. Ordinary full-year boundaries and effective rate

Assume an unassociated regular employer with a full-year BC establishment and an already reconciled remuneration base. The charity and part-year methods do not apply. Sources: [Act sections 8-12](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042) and [ordinary formulas](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview).

```oa-check
name: 2026 BC regular employer exemption and notch boundaries
inputs:
  exempt: 1000000
  middle: 1200000
  upper: 1500000
  above: 1500000.01
steps:
  - zero: max(0, exempt - 1000000) * 0.0585
  - middle_tax: round((middle - 1000000) * 0.0585, 2)
  - upper_tax: round((upper - 1000000) * 0.0585, 2)
  - upper_effective_percent: upper_tax / upper * 100
  - above_tax: round(above * 0.0195, 2)
expected:
  zero: 0
  middle_tax: 11700
  upper_tax: 29250
  upper_effective_percent: 1.95
  above_tax: 29250.00
```

### Case 2. Vancouver employer, two-million base, instalments and final balance

The original example is preserved for 2026. All T4 Summary totals under one business number are 2,250,000, including a taxable 150,000 stock-option benefit already counted once. Qualifying non-BC remuneration is 250,000; no additional BC amount is missing from the summaries. The reconciled BC base is 2,000,000. The employer is ordinary, unassociated and full-year. Actual 2025 EHT is 9,750; it chooses the prior-year basis with no credits/refunds. Its three 2026 instalments and March 31, 2027 balance are separate. [Return reconciliation](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay/filing-employers); [instalment rules](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay).

```oa-check
name: 2026 Vancouver payroll EHT and prior-year instalment reconciliation
inputs:
  t4_total: 2250000
  outside_bc: 250000
  additional_bc: 0
  prior_tax: 9750
steps:
  - bc_base: t4_total - outside_bc + additional_bc
  - annual_tax: round(bc_base * 0.0195, 2)
  - instalment: round(prior_tax * 0.25, 2)
  - three_instalments: instalment * 3
  - final_balance: annual_tax - three_instalments
expected:
  bc_base: 2000000
  annual_tax: 39000
  instalment: 2437.50
  three_instalments: 7312.50
  final_balance: 31687.50
```

### Case 3. Charity locations: zero tax still requires filing

Assume actual statutory charity status, full-year BC establishment, three proven qualifying locations and remuneration attributed under section 25: 700,000, 700,000 and 600,000. All three location liabilities are zero. Aggregate remuneration is 2,000,000, so sections 31/32 still require registration and the annual return. A separate eligible single-location charity with 4,000,000 pays 73,125; at 4,500,000 it pays 87,750; above that threshold the full-base branch applies. These are not ordinary-employer calculations. [Act sections 19-32](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042).

```oa-check
name: 2026 BC charity location tax and aggregate remuneration
inputs:
  a: 700000
  b: 700000
  c: 600000
  single: 4000000
  upper: 4500000
  above: 5000000
steps:
  - aggregate: a + b + c
  - location_total_tax: max(0, a - 1500000) * 0.02925 + max(0, b - 1500000) * 0.02925 + max(0, c - 1500000) * 0.02925
  - single_tax: round((single - 1500000) * 0.02925, 2)
  - upper_tax: round((upper - 1500000) * 0.02925, 2)
  - above_tax: round(above * 0.0195, 2)
expected:
  aggregate: 2000000
  location_total_tax: 0
  single_tax: 73125
  upper_tax: 87750
  above_tax: 97500
```

### Case 4. Associated group with a valid allocation

Two ordinary full-year employers, associated on December 31, have BC remuneration of 800,000 and 400,000. The group is in the notch. A valid agreement allocates 700,000 and 300,000, within all statutory limits. Each files its own return and completes the Association Summary. A missing agreement or a group above 1,500,000 would require a different analysis. [Act sections 17-18](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [group guidance](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-associated-employers).

```oa-check
name: 2026 BC associated employers valid shared exemption
inputs:
  a_pay: 800000
  b_pay: 400000
  a_share: 700000
  b_share: 300000
steps:
  - group_pay: a_pay + b_pay
  - allocated: a_share + b_share
  - a_tax: round(max(0, a_pay - a_share) * 0.0585, 2)
  - b_tax: round(max(0, b_pay - b_share) * 0.0585, 2)
  - group_tax: a_tax + b_tax
expected:
  group_pay: 1200000
  allocated: 1000000
  a_tax: 5850
  b_tax: 5850
  group_tax: 11700
```

### Case 5. Part-year ordinary employer: prorate both thresholds

An ordinary unassociated employer first has a BC establishment on October 20, 2026 and keeps it through December 31: 73 days. Actual BC remuneration is 250,000. The prorated exemption is 200,000 and upper threshold 300,000, placing it in the notch rather than exempt under the full-year million. [Act section 12](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042).

```oa-check
name: 2026 BC ordinary employer 73-day establishment
inputs:
  days: 73
  bc_pay: 250000
steps:
  - exemption: 1000000 * days / 365
  - upper: 1500000 * days / 365
  - tax: round((bc_pay - exemption) * 0.0585, 2)
expected:
  exemption: 200000
  upper: 300000
  tax: 2925
```

### Case 6. Late-return penalty is based on unpaid tax, with separate repeat conditions

For an ordinary section-54 late return, assume tax unpaid at the original due date is 10,000 and the earlier filing/assessment endpoint leaves three whole months. The penalty is 800, not a greater-of-100 rule. For a separate section-55 case, assume all three statutory conditions are established: the original late return, failure to comply with the later filing demand and a section-54 penalty in one of the preceding three calendar years. On the same base and three whole months, its enhanced formula gives 1,600. Interest is separate; this example does not apply the repeat formula merely because a previous return was late. [Act sections 54-55](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042).

```oa-check
name: 2026 BC ordinary and qualifying repeated late-return penalty
inputs:
  unpaid: 10000
  whole_months: 3
steps:
  - ordinary: round(unpaid * 0.05 + unpaid * 0.01 * min(whole_months, 12), 2)
  - qualifying_repeat: round(unpaid * 0.10 + unpaid * 0.02 * min(whole_months, 20), 2)
expected:
  ordinary: 800
  qualifying_repeat: 1600
```

## Filing and payment

Apply Method 7 and the actual year/account. Keep a checklist for tax liability, separate registration/return duty, instalment trigger, each payment and final return. A multiple-location charity can owe no tax and still have to file. An ordinary employer with no statutory return obligation may follow guidance recommending a nil return to keep an account active where future liability is expected; that recommendation is not a universal statutory obligation for every registered employer. Account closure and loss of the last BC establishment are different events. [Act sections 31-38](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042); [nil/final-return guidance](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay).

| Special event or consequence | Rule and conditions | Official source |
|---|---|---|
| Bankruptcy | If the ordinary return rule applies, return for the pre-bankruptcy portion within 90 days; trustee appointment also has its own notice/distribution requirements | Act sections 33, 35, 39 and 40: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |
| Employer ceases to have a BC establishment | Applicable final return within 90 days of cessation, rather than automatically next March 31 | Act section 34: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay |
| Ordinary late return | Section 54: 5% of tax unpaid at the due date plus 1% of that amount for each whole month, capped at 12 months, ending at the earlier of filing/assessment. No general 100 minimum in this formula. | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |
| Repeat late return | Section 55: 10% plus 2% per whole month up to 20 only if its late-return, later demand-failure and prior-three-year penalty conditions all apply | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |
| Missing required information | Section 56 has a separate 100-per-failure rule; do not import it as the minimum ordinary late-return penalty | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 |
| Underpaid instalment | Interest uses the statutory actual-current/prior comparison and deficiency period, not a guessed flat penalty | Act section 62: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay |
| Tax/penalty interest | Use the actual prescribed rate for each relevant period. Interest is calculated daily and compounded monthly, not compounded daily. Review the specific section-67 full-payment-after-notice rule where applicable. | Act sections 63-67: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 ; Regulation section 2: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/268_2018 |

Do not attach a universal late-filing penalty solely because registration was late. Quantify the actual return/payment failure and keep the notice and payment dates. Waiver, voluntary disclosure, amendment, reassessment and objection require the facts and official process for that case. The ordinary examples do not settle a dispute or override a notice.

## When to refuse or refer

Do not give a final liability where necessary facts or authority remain unresolved: disputed BC attachment/establishment, non-arm's-length foreign supply, stock-option timing, reserve exclusions, charity/location eligibility, association/avoidance, successor treatment or the actual relief/demand conditions. State the missing issue and the effect on the computation. Route a substantive dispute, audit or appeal to an appropriately experienced practitioner. Ordinary part-year/association rules above remain usable when their required facts are established; do not replace them with arbitrary conservative defaults.

For historical work, select the historical year before any formula. EHT started January 1, 2019; MSP premiums were halved from January 1, 2018 and eliminated January 1, 2020, leaving a 2019 overlap. The regular-employer exemption increased to 1,000,000 from 2024, with a 5.85% notch. Through 2023, the ordinary exemption was 500,000 and the notch was 2.925% of excess up to the 1,500,000 upper threshold; above it, 1.95% of full remuneration. Do not label either old rate as a 2026 method. [Historical EHT overview](https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/employer-health-tax-overview-for-2023-and-prior-years); [official MSP transition](https://news.gov.bc.ca/releases/2018FIN0005-000238); [2018 Budget speech](https://bcbudget.gov.bc.ca/2018/aria/budget-speech.htm).

## Sources

Read on **2026-11-13**. The Act and Regulation were downloaded and relevant operative sections read locally; the downloaded consolidations are current to November 10, 2026. Some ministry pages returned 502 or closed the direct connection; their official indexed text was read for the identified sections below. A failed fetch alone is not evidence of a rule. Quotes and old-topic destinations are in the country audit ledger.

| Source | What was read | Read date |
|---|---|---|
| https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042 | Read for act sections 1-30, 31-42, 53-56, 62-68 and historical-credit definitions/application limit; downloaded operative text, current November 10,2026 | 2026-11-13 |
| https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/268_2018 | Read for regulation sections 2-3: monthly compounding and prescribed instalment trigger; current November 10,2026 | 2026-11-13 |
| https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview | Read for official indexed ordinary 2024-onward formulas, days/365, business deductibility and 2026 dates; direct fetch failed | 2026-11-13 |
| https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/determining-remuneration | Read for official indexed taxable remuneration, inclusions/exclusions, stock-option treatment and payment timing; direct fetch failed | 2026-11-13 |
| https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration | Read for opened current BC remuneration/reporting/attachment and residence distinction, with official indexed full text | 2026-11-13 |
| https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-remuneration/permanent-establishment | Read for official indexed fixed/deemed establishment definitions, read with actual Act section 4 | 2026-11-13 |
| https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay/filing-employers | Read for official indexed declarations, lines 100-846, certification and confirmation instructions | 2026-11-13 |
| https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-associated-employers | Read for official indexed association modifications, proration, agreement retention, individual returns and anti-avoidance | 2026-11-13 |
| https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay/filing-associated-employers | Read for official indexed Association Summary, member shares/days and certification; direct fetch failed | 2026-11-13 |
| https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/eht-file-pay | Read for official indexed prior-year trigger, three instalments/estimate changes, nil/final returns, next-business-day rule, payment and assessment | 2026-11-13 |
| https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview/employer-health-tax-overview-for-2023-and-prior-years | Read for official indexed pre-2024 exemption/notch/full-base and start date | 2026-11-13 |
| https://news.gov.bc.ca/releases/2018FIN0005-000238 | Read for opened 2018 official news backgrounder: 2018 half-premiums, 2019 EHT and 2020 MSP abolition | 2026-11-13 |
| https://bcbudget.gov.bc.ca/2018/aria/budget-speech.htm | Read for opened historical Budget 2018 MSP section, not treated as current tax legislation | 2026-11-13 |

**Not yet confirmed:** the live authenticated 2026 eTaxBC interface was not inspected and may change field presentation; use its current declarations and the official instructions. No current professional approval is claimed. Disputed worker/location/association status, exact assessment interest and complex acquisition/insolvency facts require the actual records and current authority process. Failed standalone charity/registration/form-page attempts are not treated as source reads; the rules stated here rest on the opened Act or identified actual guidance.
