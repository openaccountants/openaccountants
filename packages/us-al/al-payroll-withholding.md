---
name: al-payroll-withholding
description: >
  Use this skill whenever asked about Alabama payroll withholding for
  tax year 2026: the employee certificate (Form A-4), the quarterly
  return (Form A-1), the monthly return (Form A-6), the annual
  reconciliation (Form A-3 with W-2s), the 5% supplemental rate, the
  electronic filing trigger, penalties, bulk-filer registration (Form
  BF-1), overtime reporting, and nonresident real property withholding.
  Trigger on "Alabama withholding", "Alabama A-1", "Alabama A-6",
  "Alabama A-3", "Alabama A-4", "Alabama bulk filing", "Alabama overtime W-2".
jurisdiction: US-AL
category: payroll
domain: payroll
type: filing-howto
tax_year: 2026
tier: 2
last_updated: 2026-11-13
version: 0.5
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - alabama-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Alabama payroll withholding

> **Source-cited draft.** Built from the ALDOR Withholding Tax Tables and Instructions for Employers and Withholding Agents (revised January 2026), the ALDOR Withholding Bulk Filing page, the ALDOR overtime pages and the nonresident real property withholding page, read 2026-11-13. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Alabama professional.

## Who this applies to

- Every employer or withholding agent paying Alabama wages withholds Alabama income tax using the ALDOR tax tables or the formula in the January 2026 withholding booklet.
- Each employee gives the employer Form A-4, the state exemption certificate; "The federal Form W-4 is not an acceptable substitute." With no Form A-4 on file, the employer withholds using zero exemptions (2026 withholding booklet).
- **Bulk filers:** "accountants or tax filing services who file withholding tax returns and payments on behalf of employers must register with ALDOR as a bulk filer and must utilize their bulk filer registration when filing withholding tax returns on behalf of their clients" (ALDOR Withholding Bulk Filing page, effective April 7, 2008). Registration is on Form BF-1.
- Buyers of Alabama real property from nonresidents withhold under §40-18-86 (ALDOR nonresident withholding page; see `alabama-cross-border`).

## Rates, bands and thresholds

| Item | Value | Tax year | Source |
|---|---|---|---|
| Supplemental wages and bonuses | Employers may withhold at 5% | 2026 | [ALDOR withholding booklet, January 2026](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Monthly filing trigger | Monthly returns required if more than $1,000.00 was withheld in either the first or second month of the quarter | 2026 | [ALDOR withholding booklet, January 2026](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Electronic filing trigger | A single withholding payment of $750 or more must be paid and the return filed electronically | 2026 | [ALDOR withholding booklet, January 2026](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Late filing penalty | 10% of the tax due on the return or $50.00, whichever is greater | 2026 | [ALDOR withholding booklet, January 2026](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Late payment penalty | 10% of the tax due (added to the late filing penalty where both apply) | 2026 | [ALDOR withholding booklet, January 2026](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Nonresident real property withholding (§40-18-86) | 3 percent or 4 percent of the purchase price, or on the gain with Form NR-AF2 | 2026 | [ALDOR nonresident withholding page](https://www.revenue.alabama.gov/individual-corporate/nonresidentwh/) |
| Overtime premium deduction for employees (Act 2026-604) | Employees deduct the lesser of the overtime premium or $1,000 on their return, tax years 2026 to 2028; employer shows the premium in W-2 box 12 code TT | 2026 | [ALDOR Overtime Premium Deduction page](https://www.revenue.alabama.gov/individual-corporate/overtime-premium-deduction-act-2026-604/) |

### Regular-wage formula inputs, January 2026 booklet page 7

For annualized gross wages GI, the deduction and exemption settings are specific to **payroll withholding**, not a substitute for the final return's federal-income-tax deduction. Source for every row: January 2026 employer booklet, formula page 7 and the neighboring standard-deduction schedule page 8.

| A-4 setting / input | Annual payroll formula amount | Source |
|---|---|---|
| 0 or S standard deduction | GI at most $25,999: $3,000; GI at least $35,500: $2,500; between: $3,000 less $25 per $500 increment or part above $25,999 | [2026 withholding booklet p.7](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| MS standard deduction | GI at most $12,999: $4,250; GI at least $17,750: $2,500; between: $4,250 less $88 per $250 increment or part above $12,999 | [2026 withholding booklet p.7](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| M standard deduction | GI at most $25,999: $8,500; GI at least $35,500: $5,000; between: $8,500 less $175 per $500 increment or part above $25,999 | [2026 withholding booklet p.7](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| H standard deduction | GI at most $25,999: $5,200; GI at least $35,500: $2,500; between: $5,200 less $135 per $500 increment or part above $25,999 | [2026 withholding booklet p.7](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Federal withholding input | Actual current-period federal income-tax withholding times payroll periods per year; no invented federal rate | [2026 withholding booklet p.7](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Personal exemption | 0 setting: zero; S or MS: $1,500; M or H: $3,000 | [2026 withholding booklet p.7](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Each dependent other than spouse | GI at most $50,000: $1,000; over $50,000 up to $100,000: $500; over $100,000: $300 | [2026 withholding booklet p.7](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Annual tax, 0/S/H/MS | First $500 at 2%, next $2,500 at 4%, excess over $3,000 at 5% | [2026 withholding booklet p.7](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Annual tax, M | First $1,000 at 2%, next $5,000 at 4%, excess over $6,000 at 5% | [2026 withholding booklet p.7](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |

## The taxable base

- Alabama wages are withheld on the ALDOR tables (weekly, bi-weekly, semi-monthly, monthly and quarterly) or by formula; the formula must be used where the employee's dependents or salary exceed the tables (2026 withholding booklet).
- Overtime: the earlier Alabama overtime exemption (Act 2023-421, amended by Act 2024-437) ended on June 30, 2025. Exempt overtime earned January 1 to June 30, 2025 is shown in W-2 box 14 as "EX OT WAGES" and kept out of box 16 (ALDOR Overtime Pay Exemption, Amended page). From 2026 there is no withholding exemption; instead the employee claims the overtime premium deduction on the return, and the employer reports only the premium in box 12 code TT, with total overtime wages in box 16 (ALDOR Overtime Premium Deduction page).
- Bulk files for A-1/A-6 uploaded after January 27, 2024 use the layout with overtime fields; where there is nothing to report, "Zeros should be entered for the 'Number of Employees with Exempt Overtime Wages' and 'Total Amount of Exempt Overtime Wages Paid' and a '1' entered in the 'No Exempt Overtime Wages Paid to Report.'" (ALDOR Withholding Bulk Filing page).

### Regular payroll calculation and submission

1. Collect the employee's signed A-4 setting and dependents, current gross covered wages, payroll frequency and actual federal income-tax withholding. Federal computations remain in `us-form-941-940-payroll`; do not use a hypothetical federal rate.
2. Multiply current-period gross wages by annual payroll periods to get GI. Determine the standard deduction using the table above and booklet schedule. Deduct annualized actual federal withholding, the A-4 personal exemption and qualifying dependent amounts. Compute annual tax on the positive taxable amount using the correct A-4 bracket set; divide by annual payroll periods. The booklet permits formula withholding to round to the nearest dollar; use one consistent permitted method.
3. Reconcile payroll-register withholding to the A-1/A-6 return and the employee annual W-2 amounts. The annual federal **withholding** input in this payroll method differs from the final Form 40 federal **liability** deduction.
4. Use **My Alabama Taxes** to select the employer withholding account and period; complete A-6 if the first/second-month trigger applies, then the quarterly A-1 reconciliation using withholding and payments already made. Submit even a required zero return, retain its acknowledgment, and retain the payment reference separately. Complete A-3 and required wage statements at year end. Exact current screen labels and any unpublished layout revision remain unconfirmed; use the actual form labels rather than guessing screen numbers.
5. Load `al-unemployment-contributions` as the separate UI job whenever the employer has staff. A-4 is the income-tax certificate; it is not the unemployment report. The UI skill owns the wage base, rate, registration and quarterly UI reports.

Source: [January 2026 employer booklet, pp. 1-5 and 7-8](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf). Electronic return/payment cutoff is 4 p.m. on the due date; a Saturday, Sunday or legal-holiday deadline moves to the next business day (p.5).

## Deadlines and filing

| Return | Due | Source |
|---|---|---|
| Form A-1, quarterly return | Last day of the month following the quarter (for example, April 30 for the quarter ended March 31); filed even if no tax was withheld | [ALDOR withholding booklet, January 2026](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Form A-6, monthly return | 15th of the month following the month withheld | [ALDOR withholding booklet, January 2026](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |
| Form A-3, annual reconciliation, with W-2s (and 1099s showing Alabama tax withheld) | Last day of January following the year; 10 or more statements, or anyone who filed and paid electronically, must submit through the ALDOR website; a zero A-3 is still required for an active account with no withholding | [ALDOR withholding booklet, January 2026](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf) |

## Penalties and interest

- Late filing: 10% of the tax due on the return or $50.00, whichever is greater. Late payment: 10% of the tax due. Where both the return and the payment are late, add the two penalties and show them as one figure. Interest runs at the rate for federal tax deficiencies and changes each quarter (2026 withholding booklet).
- Common failure modes: (1) taking a federal W-4 instead of Form A-4; (2) staying quarterly after a month with more than $1,000 withheld; (3) missing the zero A-3 in January for an account with no withholding; (4) still treating 2026 overtime as exempt from withholding; (5) a nonresident property closing with no §40-18-86 withholding or affidavit.

## Cross-border points

- Nonresident employees working in Alabama: Alabama withholding follows the Alabama wages; the booklet's exceptions for out-of-state workers and federally protected categories are on the Not yet confirmed line.
- Nonresident real property sellers: see `alabama-cross-border`.

## Worked examples

Client facts in these examples are hypothetical. Only figures from the tables above are used.

**Example 1: bonus withheld at the supplemental rate**

An employer pays a $4,000 bonus separately from regular wages and uses the 5% supplemental rate:

```oa-check
name: AL supplemental wage withholding at 5 percent
inputs:
  bonus: 4000
  supplemental_rate: 0.05
steps:
  - withheld: bonus * supplemental_rate
expected:
  withheld: 200.00
```

**Example 2: late quarterly return and late payment**

An employer files its Form A-1 late and pays late, with $300 of tax due on the return. The late filing penalty is the greater of 10% or $50; the late payment penalty is 10%; the two are added:

```oa-check
name: AL withholding late filing plus late payment penalty
inputs:
  tax_due: 300
steps:
  - late_filing: max(tax_due * 0.10, 50)
  - late_payment: tax_due * 0.10
  - total_penalty: late_filing + late_payment
expected:
  late_filing: 50.00
  late_payment: 30.00
  total_penalty: 80.00
```

**Example 3: ordinary monthly payroll through the 2026 formula**

A hypothetical employee claims S with one dependent, earns $4,000 per month, and actually has $300 federal income tax withheld that month. GI is $48,000. The standard deduction is $2,500; annual federal withholding $3,600; personal exemption $1,500; dependent amount $1,000. Taxable annualized wages are $39,400. Annual Alabama tax is $1,930, or $160.83 per month before the optional whole-dollar rounding. The $300 is a supplied payroll fact, not a federal-rate computation.

```oa-check
name: AL regular monthly withholding, January 2026 formula
inputs:
  monthly_wages: 4000
  periods: 12
  actual_federal_withholding: 300
steps:
  - gi: monthly_wages * periods
  - annual_federal_withholding: actual_federal_withholding * periods
  - taxable: max(gi - 2500 - annual_federal_withholding - 1500 - 1000, 0)
  - annual_tax: min(taxable, 500) * 0.02 + min(max(taxable - 500, 0), 2500) * 0.04 + max(taxable - 3000, 0) * 0.05
  - monthly_alabama: annual_tax / periods
expected:
  gi: 48000
  taxable: 39400
  annual_tax: 1930
  monthly_alabama: 160.83
```

## Ask the client first

- Does every employee have a signed Form A-4 on file (not a federal W-4)?
- How much was withheld in each month of the quarter: did any month exceed $1,000 (monthly A-6 filing)?
- Are payments of $750 or more being made electronically?
- Is the payroll system reporting the 2026 overtime premium in W-2 box 12 code TT?
- Is a bulk filer registered (Form BF-1) if an accountant files for the employer?
- Any Alabama real property bought from a nonresident?

## Sources

| # | Source | URL | Read on |
|---|---|---|---|
| 1 | ALDOR Withholding Tax Tables and Instructions for Employers and Withholding Agents, revised January 2026, read for Forms A-1, A-6, A-3, A-4, due dates, monthly trigger, e-file trigger, 5% supplemental rate, penalties, page 7 annualization formula and page 8 deduction schedule | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf | 2026-11-13 |
| 2 | ALDOR Withholding Bulk Filing page, read for bulk-filer registration, Form BF-1, A-1/A-6 and A-3 file layouts, 2024 layout change | https://www.revenue.alabama.gov/individual-corporate/withholding-bulk-filing/ | 2026-11-13 |
| 3 | ALDOR Overtime Pay Exemption, Amended page, read for exemption ending June 30, 2025 and W-2 box 14 reporting | https://www.revenue.alabama.gov/individual-corporate/overtime-pay-exemption-amended/ | 2026-11-13 |
| 4 | ALDOR Overtime Premium Deduction (Act 2026-604) page, read for the page as a whole | https://www.revenue.alabama.gov/individual-corporate/overtime-premium-deduction-act-2026-604/ | 2026-11-13 |
| 5 | ALDOR Withholding Requirement on Sales/Transfers of Real Property by Nonresidents (§40-18-86), read for the distinct non-payroll withholding boundary | https://www.revenue.alabama.gov/individual-corporate/nonresidentwh/ | 2026-11-13 |

Not yet confirmed: a line-by-line audit of all wage-table cells (the page 7 regular-wage formula is now read and supplied above); current portal screen labels and any later layout revisions; which nonresident sellers withhold at 3 percent and which at 4 percent; the A-6 rules for withholding on non-wage payments and on nonresident members of pass-through entities; the booklet's exceptions for nonresident employees and whether Alabama has withholding reciprocity with any state (an earlier draft asserted none).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
