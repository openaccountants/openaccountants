---
name: ms-paye-employer-withholding
description: "Montserrat employer PAYE withholding for 2026 under section 51 of the Income and Corporation Tax Act, Cap. 17.01, the Income Tax (Employment) Rules and the MCRS tax tables effective January 2024. Covers the table lookup by pay and tax code (rule 4 nearest row against the MCRS \"next higher\" instruction), remitting each month's deductions within the first 15 days of the next month on IRD 03, the 7-day rule on cessation, the January employee certificates (IRD 05) and reconciliation (IRD 06), the late remittance penalty (5% or EC$1,000 in the Act, EC$100 in the MCRS tables, plus 10% interest), and the January to July 2024 over-deduction adjustments. Trigger phrases include Montserrat PAYE, Montserrat tax tables, IRD 03, MCRS employer."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ms-paye-employer-withholding"
  jurisdiction: "MS"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Montserrat employer PAYE withholding

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Tax an employer in Montserrat deducts from emoluments in 2026 under Cap. 17.01 ss.51 and 53, the Income Tax (Employment) Rules (both in the revised edition showing the law at 1 January 2025) and the MCRS 2024 tax tables. Amounts are EC$. The employee's annual tax and the EC$18,000 deduction: [ms-income-tax-individuals](ms-income-tax-individuals.md). Social security deductions: [ms-social-security-contributions](ms-social-security-contributions.md). Payments to nonresidents other than emoluments: [ms-nonresident-withholding](ms-nonresident-withholding.md).

## Ask the client first

1. Pay frequency (weekly, fortnightly, half-monthly, monthly) and pay for the period, including benefits such as free board and lodging.
2. The employee's tax code from the IRD 01 declaration, certified by the Comptroller where in doubt.
3. Any bonus or retroactive pay (refer to Inland Revenue before paying).
4. Is the business ceasing, or is an employee leaving (IRD 04)?
5. Any remittance already late?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Table lookup, rule 4(1) | Deduct the amount in the employee's code column opposite the pay row that is the same as or the nearest to the emoluments due | [Cap. 17.01, Income Tax (Employment) Rules, rr.3 and 4](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=60) |
| Exact tie, rule 4(2) | Pay exactly between two rows: use the larger row | same |
| Out-of-table cases, rule 4(1) proviso | Pay period not in the tables, pay above the last row, or allowances above the tables: the Comptroller determines the deduction | same |
| MCRS table instruction | "Where the pay is between two amounts, use the next higher figure" (conflicts with rule 4(1)) | [MCRS 2024 tax tables, instructions](https://mcrs.ms/wp-content/uploads/2024/08/2024-Tax-Tables.pdf#page=5) |
| Remittance, rule 11 | Previous month's deductions to the Accountant General within the first 15 days of each month, with the return (IRD 03) | [Cap. 17.01, Income Tax (Employment) Rules, rr.11 to 19](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=63) |
| Business ceasing, rule 12 | Pay within 7 days | same |
| Late remittance, s.51(3) | Greater of 5% of the amount not remitted or EC$1,000, plus the amount and interest at 10% a year | [Cap. 17.01, s.51](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=45) |
| Late remittance, MCRS tables | Greater of 5% or EC$100, plus interest at 10% a year (conflicts with s.51(3)) | [MCRS 2024 tax tables, instructions](https://mcrs.ms/wp-content/uploads/2024/08/2024-Tax-Tables.pdf#page=5) |
| 2024 over-deductions | Tables revised only in August 2024; employers adjust January to July 2024 overpayments by the absolute deadline of 31 December 2024 | [MCRS 2024 notice](https://mcrs.ms/paye-adjustment-2024/) |

### Steps

1. **Pay for the period:** salary plus taxable benefits (MCRS example: free board and lodging).
2. **Code:** take the code from the employee's declaration (rule 3); if in doubt, have the Comptroller certify it before paying.
3. **Look up** the deduction in the table for the pay frequency, the code column and the pay row (rule 4). For half-monthly pay the MCRS method doubles the pay, reads the monthly table and halves the tax.
4. **Hold** the deductions in trust (s.51(7)); the employee gets credit for them (s.51(13)).
5. **Remit** within the first 15 days of the next month with IRD 03; keep payment particulars and records (rules 18 and 19).
6. **Year end:** give each employee an annual certificate (IRD 05) in January and send the Comptroller's copies and the reconciliation (IRD 06) (rule 14 prints 1 January for the Comptroller's copies).

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Monthly pay of 2,010, code 180M | Rule 4(1) nearest row is 2,000, which prints 25; the MCRS example uses the next higher row 2,025, which prints 26. Resolve with MCRS before choosing; both are documented lookups, not an established deduction | [Rules, r.4](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=60); [MCRS monthly 180M table](https://mcrs.ms/wp-content/uploads/2024/08/2024-Tax-Tables.pdf#page=9) |
| Bonus or retroactive payment | Refer to Inland Revenue before paying (MCRS tables, item 7) | [MCRS 2024 tax tables](https://mcrs.ms/wp-content/uploads/2024/08/2024-Tax-Tables.pdf#page=5) |
| Which penalty applies | s.51(3) prints EC$1,000 minimum; MCRS prints EC$100. Cap. 17.26 has its own penalty and interest rules and its s.4(2) gives the revenue law precedence where they conflict. Verify before computing | [Cap. 17.01, s.51](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=45); [Cap. 17.26](https://www.gov.ms/wp-content/uploads/2026/02/17.26-Tax-Administration-Act.pdf) |
| Historical 2024 claim after 31 December 2024 | SRO 37/2024 limits relief to the overpayment caused by Act 20's changes in January to July 2024; check the remaining route, and note the notice speaks of income year 2024 while the Act speaks of the year of assessment | [SRO 37/2024](https://www.gov.ms/wp-content/uploads/2024/10/SRO-No.-37-of-2014-Income-and-Corporation-Tax-Individual-Exemption-Order.pdf); [MCRS 2024 notice](https://mcrs.ms/paye-adjustment-2024/) |
| Employee leaves | IRD 04 ceasing form; rule 14 certificate obligations | [MCRS forms](https://mcrs.ms/ird-forms/) |

## Worked cases

### Case 1: late remittance of EC$4,000 under each rule

An employer remits EC$4,000 of deductions late. Under s.51(3) the penalty is the greater of 5% (200) and 1,000, so 1,000. Under the MCRS table wording it is the greater of 200 and 100, so 200. One year's interest at 10% is 400 under both.

```oa-check
name: Montserrat PAYE late remittance penalty on 4,000, Act vs MCRS
inputs:
  amount: 4000
steps:
  - pct_part: amount * 0.05
  - penalty_act: max(pct_part, 1000)
  - penalty_mcrs: max(pct_part, 100)
  - interest_year: amount * 0.10
expected:
  pct_part: 200
  penalty_act: 1000
  penalty_mcrs: 200
  interest_year: 400
```

### Case 2 (decision): which table row for monthly pay of EC$2,010?

The nearest row under rule 4(1) is 2,000 (10 away; 2,025 is 15 away), giving 25 at code 180M. The MCRS next-higher instruction gives 2,025 and 26. Over 12 months the difference is 12. Follow the rule and record the MCRS conflict, or ask MCRS in writing which one it accepts.

```oa-check
name: Montserrat PAYE nearest row vs next higher, monthly 2,010 at 180M
inputs:
  pay: 2010
  row_low: 2000
  row_high: 2025
  tax_low: 25
  tax_high: 26
steps:
  - gap_low: pay - row_low
  - gap_high: row_high - pay
  - year_difference: (tax_high - tax_low) * 12
expected:
  gap_low: 10
  gap_high: 15
  year_difference: 12
```

## When to refuse or refer

- Out-of-table cases under the rule 4(1) proviso: the Comptroller determines the deduction.
- Bonuses and retroactive pay.
- Penalty computations until the s.51(3) and MCRS conflict is resolved.
- Any period where newer tables may exist.

## Filing and payment

1. Register as an employer (IRD 02); collect each employee's declaration (IRD 01).
2. Each month: deduct by the table and remit within the first 15 days of the next month with IRD 03.
3. On cessation of the business: remit within 7 days.
4. In January: IRD 05 certificate to each employee; Comptroller's copies and the IRD 06 reconciliation.

## Completion checklist

- Code certified; pay includes benefits.
- Row chosen and the rule followed recorded.
- Remitted by the 15th; certificates issued in January.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income and Corporation Tax Act Cap. 17.01, revised to 1 January 2025: read for s.51 (deduction, trust, 5% or EC$1,000 penalty and 10% interest, credit), s.53 and the Income Tax (Employment) Rules rr.3, 4, 11, 12, 14, 18 and 19 | https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf | 2026-11-14 |
| MCRS 2024 tax tables (effective January 2024): read for the instructions (next higher row, examples A and B, bonuses, the 15th, 5% or EC$100 and 10%) and the monthly table rows 2,000 and 2,025 at 180M | https://mcrs.ms/wp-content/uploads/2024/08/2024-Tax-Tables.pdf | 2026-11-14 |
| MCRS IRD forms page: read for IRD 01 to 06 | https://mcrs.ms/ird-forms/ | 2026-11-14 |
| MCRS public notice for the private sector (2024 adjustments): read for the August 2024 tables and the 31 December 2024 deadline | https://mcrs.ms/paye-adjustment-2024/ | 2026-11-14 |
| SRO 37/2024, Income and Corporation Tax (Individual Exemption) Order: read for the limit on January to July 2024 relief | https://www.gov.ms/wp-content/uploads/2024/10/SRO-No.-37-of-2014-Income-and-Corporation-Tax-Individual-Exemption-Order.pdf | 2026-11-11 |
| Tax Administration Act Cap. 17.26: read for s.4(2) precedence and its separate penalty and interest provisions | https://www.gov.ms/wp-content/uploads/2026/02/17.26-Tax-Administration-Act.pdf | 2026-11-14 |

Not yet confirmed: tables for 2025 or 2026 (none found); which row rule MCRS applies; which late remittance penalty applies; the operative date for the Comptroller's year-end copies; SRO 37/2024 was read by Ryan Duguid on 2026-11-11 and not re-opened here.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ms-paye-employer-withholding` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ms-paye-employer-withholding. If neither is available, confirm every figure against the official source pages cited above before relying on it.
