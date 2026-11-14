---
name: cz-tax-overview
description: "Use this skill as the entry point for Czech tax in tax year 2026. It gives the headline figures and points to the skill that holds the detail. Individual income tax at 15% and 23% above CZK 1,762,812 (36 times the 2026 average wage of CZK 48,967), the basic credit of CZK 30,840, corporate income tax at 21%, withholding at 15% or 35%, VAT at 21% and 12% with the CZK 2,000,000 and CZK 2,536,500 registration thresholds, late payment interest (CNB repo plus 8 points, CZK 1,000 floor) and the return deadlines for 2026 (1 April, 3 May and 1 July 2027). Trigger phrases include Czech tax overview, taxes in the Czech Republic, Czech tax rates 2026 and dane v CR. The detail of each tax lives in cz-employee-income-tax, cz-income-tax, cz-corporate-income-tax, czech-republic-vat-return, cz-employee-contributions, cz-social-health, cz-payroll, cz-transfer-pricing and cz-cross-border."
version: 1.0
jurisdiction: CZ
tax_year: 2026
last_updated: 2026-11-14
category: international
type: situation-rules
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Czech Republic: tax overview (2026) v1.0

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team. No accountant has reviewed this skill yet. Figures come from the consolidated laws on e-Sbírka (the official Collection of Laws), financnisprava.gov.cz and cnb.cz, read on 14 November 2026. It is a map, not a full computation: open the linked skill before advising.

## Who this applies to

- **Anyone asking "which Czech tax applies, at what headline rate, and when is it due"** for tax year 2026: individuals (employees, the self-employed, landlords, investors), companies and their advisers. The detailed method for each tax sits in the skill named in the last column of the table below.
- **Tax year.** The calendar year for individuals. Companies use the calendar year or a financial year (Income Taxes Act ("ITA") § 21a).
- **Currency.** Czech koruna (CZK).
- **Authority.** The Financial Administration (Finanční správa) and its tax offices collect income tax and VAT. Social insurance goes to ČSSZ and health insurance to the health insurers.
- **Residence.** Individuals are resident if they have a home in the Czech Republic or stay at least 183 days in the calendar year (ITA § 2(2), (4)). Companies are resident if their seat or place of management is in the Czech Republic (ITA § 17(3)). Residents are taxed on worldwide income, non-residents on Czech-source income only. Detail: [cz-cross-border](cz-cross-border.md).
- **Main laws.** Act No. 586/1992 Coll. on Income Taxes, Act No. 280/2009 Coll., the Tax Code, and Act No. 235/2004 Coll. on VAT.
- **Out of scope here:** the computation of each tax, social and health insurance rates (in [cz-employee-contributions](cz-employee-contributions.md) and [cz-social-health](cz-social-health.md)), payroll withholding ([cz-payroll](cz-payroll.md)) and transfer pricing ([cz-transfer-pricing](cz-transfer-pricing.md)).

## Rates, bands and thresholds

| Item | Rate or amount (2026) | Official source | Detail skill |
|---|---|---|---|
| Individual income tax | 15% on the part of the base up to 36 times the average wage; 23% on the part above | [ITA § 16(1)](https://e-sbirka.gov.cz/sb/1992/586/2026-08-01) | [cz-employee-income-tax](cz-employee-income-tax.md), [cz-income-tax](cz-income-tax.md) |
| Average wage for tax purposes | CZK 48,967 (general assessment base for 2024 of CZK 46,278 times the coefficient 1.0581, rounded up to whole CZK; ITA § 21g(2) uses the social insurance figure under Act 589/1992 § 23b(4)) | [Government Regulation 365/2025 § 1](https://e-sbirka.gov.cz/sb/2025/365) | cz-income-tax |
| 23% threshold | CZK 1,762,812 a year (36 times CZK 48,967) | [ITA § 16(1)](https://e-sbirka.gov.cz/sb/1992/586/2026-08-01) | cz-employee-income-tax |
| Basic taxpayer credit | CZK 30,840 a year | [ITA § 35ba(1)(a)](https://e-sbirka.gov.cz/sb/1992/586/2026-08-01) | cz-employee-income-tax |
| Corporate income tax | 21% on the base reduced by deductions and rounded down to whole thousands of CZK (5% basic investment funds, 0% pension funds) | [ITA § 21(1) to (3)](https://e-sbirka.gov.cz/sb/1992/586/2026-08-01) | [cz-corporate-income-tax](cz-corporate-income-tax.md) |
| Withholding on payments to non-residents | 15%; 35% to residents of states outside the EU and EEA with no treaty, tax information exchange agreement or multilateral information exchange convention in force | [ITA § 36(1)](https://e-sbirka.gov.cz/sb/1992/586/2026-08-01) | cz-cross-border |
| VAT rates | 21% standard; 12% reduced | [VAT Act § 47(1)](https://e-sbirka.gov.cz/sb/2004/235/2026-01-01) | [czech-republic-vat-return](czech-republic-vat-return.md) |
| VAT registration (established business) | turnover over CZK 2,000,000 in a calendar year: VAT payer from 1 January of the next year; over CZK 2,536,500 in the year: payer from the day after | [VAT Act § 6(1), (2)](https://e-sbirka.gov.cz/sb/2004/235/2026-01-01) | czech-republic-vat-return |
| Late payment interest on tax | the Civil Code default rate: CNB repo rate on the first day of the calendar half-year plus 8 points | [Tax Code § 252(4), § 251a(5)](https://e-sbirka.gov.cz/sb/2009/280/2026-01-01); [Government Regulation 351/2013 § 2(1)](https://e-sbirka.gov.cz/sb/2013/351) | cz-corporate-income-tax |
| CNB repo rate on 1 January 2026 and the interest rate it gives | 3.50% (in force from 9 May 2025), so 11.50% a year for days from 1 January to 30 June 2026 | [CNB repo history](https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt) | same |
| CNB repo rate on 1 July 2026 and the interest rate it gives | 3.75% (in force from 19 June 2026), so 11.75% a year for days from 1 July to 31 December 2026 | [CNB repo history](https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt) | same |
| Interest floor | interest is not charged if, for one tax, one tax office and one tax period, it does not exceed CZK 1,000 in total | [Tax Code § 251a(2)](https://e-sbirka.gov.cz/sb/2009/280/2026-01-01) | same |

## The base

- **Individuals.** Income is grouped into five heads (employment, business, capital, rental, other), each with its own base; the 15% and 23% rates apply to the total base after non-taxable parts, then credits such as the basic credit reduce the tax. Method: [cz-employee-income-tax](cz-employee-income-tax.md) for employees, [cz-income-tax](cz-income-tax.md) for the self-employed and other income.
- **Companies.** The base starts from the accounting profit, adjusted for non-deductible items and tax depreciation, less losses and deductions, then rounded down to whole thousands of CZK before the 21% rate (ITA § 21(1)). Method: [cz-corporate-income-tax](cz-corporate-income-tax.md).
- **VAT.** Charged on taxable supplies in the Czech Republic once the business is a VAT payer; input VAT is deducted. Method: [czech-republic-vat-return](czech-republic-vat-return.md).

## Deadlines and filing

Individual and corporate income tax returns follow the same rule. The return is due within 3 months after the end of the tax period. It is 4 months if filed electronically after the 3-month date, and 6 months if a tax adviser files after the 3-month date or the accounts must be audited (Tax Code § 136(1), (2)). A deadline on a Saturday, Sunday or public holiday moves to the next working day (Tax Code § 33(4)). The tax is due on the last day for filing (Tax Code § 135(3)).

For the calendar year 2026:

- paper or electronic: **1 April 2027**;
- electronic, after 1 April: **3 May 2027**, because 1 May 2027 is a Saturday and a public holiday;
- tax adviser files after 1 April, or the accounts must be audited: **1 July 2027**.

Statutory audit: for accounting periods that start on or after 1 January 2026, small companies no longer have to be audited under the Accounting Act. Act No. 316/2025 Coll. repealed Accounting Act § 20(1)(c) and (d), so only large and medium accounting units, and units a special law names, must be audited (Accounting Act § 20(1); Act 316/2025, Art. I point 12, Art. II point 1, Art. VII). A small company without a tax adviser therefore files its 2026 return by 1 April 2027, or by 3 May 2027 electronically; it gets 1 July 2027 only if a tax adviser files. Detail: [cz-corporate-income-tax](cz-corporate-income-tax.md) and [cz-company-formation](cz-company-formation.md).

For the 2025 return the Financial Administration gave 1 April, 4 May and 1 July 2026 ([Finanční správa](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace)). The 2027 dates are counted the same way.

VAT returns, control statements and EC sales lists have monthly or quarterly 25-day deadlines: see [czech-republic-vat-return](czech-republic-vat-return.md).

## Penalties and interest

- **Late payment interest** runs from the fourth day after the original due date to the day of payment (Tax Code § 252(2)(a)), at the rate in the table, for each day at the rate of the half-year that day falls in (Tax Code § 251a(5)). It is not charged at all if it stays at or under CZK 1,000 for one tax, one office and one period (§ 251a(2)).
- **Late filing and control statement fines** are in the detail skills (the late filing surcharge under Tax Code § 250 in [cz-corporate-income-tax](cz-corporate-income-tax.md) and [cz-income-tax](cz-income-tax.md); VAT control statement fines under VAT Act § 101h in [czech-republic-vat-return](czech-republic-vat-return.md)).
- **Watch for 2027:** the CNB raised the repo rate to 4.00% from 6 November 2026, so unless it changes again before 1 January 2027, interest for the first half of 2027 will be 12.00%. Recheck the CNB history before computing 2027 days.

## Cross-border points

- Non-residents are taxed on Czech-source income only; withholding at 15% (35% for listed non-cooperative states) under ITA § 36(1), reduced by a treaty where one applies. Method and treaty steps: [cz-cross-border](cz-cross-border.md).
- Related-party pricing: [cz-transfer-pricing](cz-transfer-pricing.md).
- EU supplies, reverse charge and EC sales lists: [czech-republic-vat-return](czech-republic-vat-return.md).

## Two worked examples that recompute

### 1. Employee with a 2026 base of CZK 2,000,000

The base is above the CZK 1,762,812 threshold. 15% on CZK 1,762,812 is CZK 264,421.80; 23% on the CZK 237,188 above it is CZK 54,553.24; tax before credits CZK 318,975.04. The basic credit of CZK 30,840 leaves CZK 288,135.04 before rounding and before any other credit. Payroll detail (monthly advances, the 3-times-average-wage advance threshold) is in [cz-payroll](cz-payroll.md).

```oa-check
name: Czech employee, 2026 base CZK 2,000,000
inputs:
  base: 2000000
  threshold: 1762812
  credit: 30840
steps:
  - band_15: min(base, threshold) * 0.15
  - band_23: max(base - threshold, 0) * 0.23
  - tax_before_credit: band_15 + band_23
  - tax_after_credit: tax_before_credit - credit
expected:
  band_15: 264421.80
  band_23: 54553.24
  tax_before_credit: 318975.04
  tax_after_credit: 288135.04
```

### 2. Decision: is late payment interest charged? Company tax paid 30 days or 10 days late (first half of 2026)

A company's base is CZK 1,234,567, rounded down to CZK 1,234,000; tax at 21% is CZK 259,140. If it pays 30 days after the due date, interest runs from the fourth day, so for 27 days at 11.50%: CZK 2,204.46. That is over CZK 1,000, so the tax office charges it. If it pays 10 days late, interest runs for 7 days: CZK 571.53, under CZK 1,000, so nothing is charged. The figure that decides is the CZK 1,000 floor in Tax Code § 251a(2).

```oa-check
name: Late payment interest, 30 days versus 10 days late, H1 2026
inputs:
  base_rounded: 1234000
  cit_rate: 0.21
  rate: 0.115
  days_late_a: 30
  days_late_b: 10
  floor: 1000
steps:
  - tax: base_rounded * cit_rate
  - interest_a: tax * rate * (days_late_a - 3) / 365
  - interest_b: tax * rate * (days_late_b - 3) / 365
  - over_floor_a: interest_a - floor
  - over_floor_b: interest_b - floor
expected:
  tax: 259140.00
  interest_a: 2204.46
  interest_b: 571.53
  over_floor_a: 1204.46
  over_floor_b: -428.47
```

## Ask the client first

1. Individual or company, and for a company the accounting period (calendar or financial year).
2. Czech tax residence (home or 183 days; seat or place of management).
3. The kinds of income (employment, business, rental, capital, other) and the expected 2026 base, to see whether the 23% band applies.
4. Turnover in the Czech Republic in 2025 and so far in 2026, for VAT registration.
5. Whether a tax adviser will file, and whether the accounts must be audited, for the return deadline.
6. Any payment made late, and by how many days, for interest.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 586/1992 Coll., Income Taxes Act, version in force from 1 August 2026. Read for §§ 2, 16(1) (15% and 23% bands), 17(3), 21(1) to (3) (21% rate, rounding to thousands), 21a, 21g, 35ba(1)(a) (CZK 30,840) and 36(1) (15% and 35% withholding) | https://e-sbirka.gov.cz/sb/1992/586/2026-08-01 | 2026-11-14 |
| Government Regulation No. 365/2025 Coll. Read for the 2024 general assessment base of CZK 46,278 and the coefficient 1.0581 | https://e-sbirka.gov.cz/sb/2025/365 | 2026-11-14 |
| Act No. 280/2009 Coll., Tax Code, version in force from 1 January 2026. Read for §§ 33(4), 135(3), 136(1) and (2) (3, 4 and 6 month deadlines), 251a(2) (CZK 1,000 floor), 251a(5) and 252(2) and (4) (interest start and rate) | https://e-sbirka.gov.cz/sb/2009/280/2026-01-01 | 2026-11-14 |
| Act No. 235/2004 Coll., VAT Act, version in force from 1 January 2026. Read for § 6(1) and (2) (CZK 2,000,000 and CZK 2,536,500) and § 47(1) (21% and 12%) | https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 | 2026-11-14 |
| Act No. 563/1991 Coll., Accounting Act, version in force from 1 January 2026. Read for § 20(1) (audit duty only for large and medium units and units named by a special law) | https://e-sbirka.gov.cz/sb/1991/563/2026-01-01 | 2026-11-14 |
| Act No. 316/2025 Coll., amending the Accounting Act. Read for Art. I point 12, Art. II point 1 and Art. VII (repeal of the small-company audit duty from periods starting 1 January 2026) | https://e-sbirka.gov.cz/sb/2025/316 | 2026-11-14 |
| Government Regulation No. 351/2013 Coll. Read for § 2(1) (default interest equals the CNB repo rate for the first day of the half-year plus 8 percentage points) | https://e-sbirka.gov.cz/sb/2013/351 | 2026-11-14 |
| Czech National Bank, two-week repo rate history. Read for the 3.50% rate from 9 May 2025, 3.75% from 19 June 2026 and 4.00% from 6 November 2026 | https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt | 2026-11-14 |
| Finanční správa, Daň z příjmů fyzických osob, obecné informace. Read for the 2025 return dates (1 April, 4 May and 1 July 2026) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace | 2026-11-14 |

Not yet confirmed: the Financial Administration had not published the filing dates for 2026 returns; 1 April, 3 May and 1 July 2027 are counted from Tax Code §§ 33(4) and 136. The interest rate for 2027 days depends on the CNB repo rate on 1 January 2027.
