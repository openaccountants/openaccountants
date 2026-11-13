---
name: al-payroll-withholding
description: "Use this skill whenever asked about Alabama payroll withholding for tax year 2026: the employee certificate (Form A-4), the quarterly return (Form A-1), the monthly return (Form A-6), the annual reconciliation (Form A-3 with W-2s), the 5% supplemental rate, the electronic filing trigger, penalties, bulk-filer registration (Form BF-1), overtime reporting, and nonresident real property withholding. Trigger on \"Alabama withholding\", \"Alabama A-1\", \"Alabama A-6\", \"Alabama A-3\", \"Alabama A-4\", \"Alabama bulk filing\", \"Alabama overtime W-2\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/al-payroll-withholding"
  jurisdiction: "US-AL"
  tax_year: "2026"
  last_updated: "2026-11-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
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

## The taxable base

- Alabama wages are withheld on the ALDOR tables (weekly, bi-weekly, semi-monthly, monthly and quarterly) or by formula; the formula must be used where the employee's dependents or salary exceed the tables (2026 withholding booklet).
- Overtime: the earlier Alabama overtime exemption (Act 2023-421, amended by Act 2024-437) ended on June 30, 2025. Exempt overtime earned January 1 to June 30, 2025 is shown in W-2 box 14 as "EX OT WAGES" and kept out of box 16 (ALDOR Overtime Pay Exemption, Amended page). From 2026 there is no withholding exemption; instead the employee claims the overtime premium deduction on the return, and the employer reports only the premium in box 12 code TT, with total overtime wages in box 16 (ALDOR Overtime Premium Deduction page).
- Bulk files for A-1/A-6 uploaded after January 27, 2024 use the layout with overtime fields; where there is nothing to report, "Zeros should be entered for the 'Number of Employees with Exempt Overtime Wages' and 'Total Amount of Exempt Overtime Wages Paid' and a '1' entered in the 'No Exempt Overtime Wages Paid to Report.'" (ALDOR Withholding Bulk Filing page).

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
| 1 | ALDOR Withholding Tax Tables and Instructions for Employers and Withholding Agents, revised January 2026, read for Forms A-1, A-6, A-3, A-4, due dates, monthly trigger, e-file trigger, 5% supplemental rate, penalties | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf | 2026-11-13 |
| 2 | ALDOR Withholding Bulk Filing page, read for bulk-filer registration, Form BF-1, A-1/A-6 and A-3 file layouts, 2024 layout change | https://revenue.alabama.gov/taxes-fees/withholding/ | 2026-11-13 |
| 3 | ALDOR Overtime Pay Exemption, Amended page (exemption ended June 30, 2025; W-2 box 14 reporting) | https://www.revenue.alabama.gov/individual-corporate/overtime-pay-exemption-amended/ | 2026-11-13 |
| 4 | ALDOR Overtime Premium Deduction (Act 2026-604) page, read for the page as a whole | https://www.revenue.alabama.gov/individual-corporate/overtime-premium-deduction-act-2026-604/ | 2026-11-13 |
| 5 | ALDOR Withholding Requirement on Sales/Transfers of Real Property by Nonresidents (§40-18-86) | https://www.revenue.alabama.gov/individual-corporate/nonresidentwh/ | 2026-11-13 |

Not yet confirmed: the 2026 withholding table amounts and formula constants (the booklet holds them but they were not tied out line by line); which nonresident sellers withhold at 3 percent and which at 4 percent; the A-6 rules for withholding on non-wage payments and on nonresident members of pass-through entities; the booklet's exceptions for nonresident employees and whether Alabama has withholding reciprocity with any state (an earlier draft asserted none).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `al-payroll-withholding` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/al-payroll-withholding. If neither is available, confirm every figure against the official source pages cited above before relying on it.
