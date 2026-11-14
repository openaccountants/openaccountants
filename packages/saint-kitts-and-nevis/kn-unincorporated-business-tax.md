---
name: kn-unincorporated-business-tax
description: >
  Saint Kitts and Nevis tax on individuals and unincorporated businesses for 2026.
  There is no ordinary personal income tax: s.3(3) of the Income Tax Act takes persons
  other than companies out of the charge for income from 1 May 1980, so wages carry no
  income tax withholding. Self-employed people, sole traders and partnerships not taxed
  as companies pay the Unincorporated Business Tax (Cap. 18.46): 4% on gross takings from
  goods less EC$12,500 a month and from services less EC$2,000 a month (IRD forms use
  EC$37,500 and EC$6,000 a quarter), with quarterly returns and payment by 15 March, 15
  June, 15 September and 15 December. Trigger phrases include St Kitts personal income
  tax, no income tax St Kitts, UBT, unincorporated business tax, self-employed St Kitts.
version: 1.0
jurisdiction: KN
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Kitts and Nevis: individuals and the Unincorporated Business Tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

How individuals and unincorporated businesses are taxed in Saint Kitts and Nevis in 2026: no ordinary personal income tax (Income Tax Act, Cap. 20.22, s.3(3)), and the Unincorporated Business Tax Act, Cap. 18.46 (2017 revision, amended 2014). Amounts are EC$. Employees still bear the Housing and Social Development Levy and social security: [kn-housing-social-development-levy](kn-housing-social-development-levy.md), [kn-social-security-contributions](kn-social-security-contributions.md). Companies: [kn-corporate-income-tax](kn-corporate-income-tax.md).

## Ask the client first

1. Is the person an employee only, or carrying on a business (sole trader, partnership)?
2. Is the business a company registered under the Companies Act, or a partnership taxed as a company (both outside UBT)?
3. Monthly gross takings from goods and from services, kept separate, with VAT excluded.
4. Any client money received as a representative (only the own commission, fee or mark-up counts)?
5. Has the business elected to compute under the Income Tax Act (s.5(5) to (8))?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Personal income tax, Income Tax Act s.3(3) | None: s.3 does not apply to income accruing on or after 1st May, 1980 to any person other than a company | [Income Tax Act, Cap. 20.22, ss.3 and 68 to 71](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf) |
| UBT rate, ss.3 to 5 | Four per centum of the goods tax base and four per centum of the services tax base | [Unincorporated Business Tax Act, Cap. 18.46, s.5](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_46-Unincorporated-Business-Tax-Act.pdf) |
| Goods allowance, s.5(2)(a) | Monthly gross takings from goods reduced (not below zero) by twelve thousand five hundred dollars | same |
| Services allowance, s.5(2)(b) | Monthly gross takings from services reduced (not below zero) by two thousand dollars | same |
| IRD guide and UBT-01 form | Quarterly exemption of $37,500.00 for goods and $6,000.00 for services | [IRD UBT guide](https://www.sknird.com/wp-content/uploads/2020/05/200701012021.pdf); [UBT-01, p.2](https://www.sknird.com/wp-content/uploads/2024/02/UBT-Return-Updated-3.0.pdf) |
| Return and payment, s.7 (Act 6 of 2014) | Quarterly, on or before the 15th day of March, June, September and December | [Cap. 18.46, ss.7 and 8](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_46-Unincorporated-Business-Tax-Act.pdf) |

### The base

- **Who pays.** Anyone carrying on business in the Federation other than a company registered under the Companies Act or a partnership treated as a company and liable under the Income Tax Act. Employment is not a business.
- **Gross takings.** Cash and accrued receipts; exclude VAT properly accounted for and client money received as a representative (include the own commission, fee or mark-up). Use VAT time-of-supply and value rules, including the hypothetical timing for someone not registered for VAT. Keep goods and services apart.
- **Election.** Section 5(5) to (8) allows one election to compute under the Income Tax Act instead.
- **Quarters (IRD guide).** December to February (due 15 March), March to May (15 June), June to August (15 September), September to November (15 December); a deadline on a weekend or holiday moves to the next business day.

### Steps

1. **Check status:** company or partnership taxed as one is out.
2. **Each month:** goods takings less 12,500 and services takings less 2,000, each floored at zero.
3. **Quarter:** add the three months for each base; 4% of each.
4. **File and pay** the UBT-01 return through SMARTS by the 15th.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Wages | No income tax withholding: the old ss.68 to 71 employer machinery applies to emoluments assessable to income tax, which ordinary wages are not | [Cap. 20.22, ss.3 and 68 to 71](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf) |
| Monthly floors in the Act against quarterly allowances on IRD forms | Different results when takings are uneven; confirm the accepted method with IRD (see Case 2) | [Cap. 18.46, s.5(2)](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_46-Unincorporated-Business-Tax-Act.pdf); [IRD guide](https://www.sknird.com/wp-content/uploads/2020/05/200701012021.pdf) |
| COVID relief line on UBT-01 | Still printed; confirm whether any relief authority applies to the period | [UBT-01](https://www.sknird.com/wp-content/uploads/2024/02/UBT-Return-Updated-3.0.pdf) |
| September to November 2026 | Due 15 December 2026 (IRD calendar) | [IRD tax calendar](https://www.sknird.com/tax-calendar/) |
| Payments to non-residents | 15% withholding: [kn-nonresident-withholding](kn-nonresident-withholding.md) | [Cap. 20.22, s.36](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf) |

## Worked cases

### Case 1: a shop's quarter

Goods takings of 20,000, 15,000 and 10,000 in the three months. Monthly bases: 7,500, 2,500 and 0; total 10,000; UBT 400.

```oa-check
name: St Kitts UBT goods quarter 20,000, 15,000, 10,000
inputs:
  m1: 20000
  m2: 15000
  m3: 10000
steps:
  - base: max(m1 - 12500, 0) + max(m2 - 12500, 0) + max(m3 - 12500, 0)
  - ubt: base * 0.04
expected:
  base: 10000
  ubt: 400
```

### Case 2 (decision): monthly floors or the quarterly allowance?

A consultant's services takings are 0, 0 and 9,000. The Act's monthly floors give (9,000 - 2,000) x 4% = 280. The IRD form's quarterly 6,000 gives (9,000 - 6,000) x 4% = 120. The gap is 160. Filing on the form's method follows IRD's own return; record the statutory reading and ask IRD which it accepts if the gap matters.

```oa-check
name: St Kitts UBT services 0, 0, 9,000, monthly vs quarterly
inputs:
  m3: 9000
steps:
  - monthly_method: max(m3 - 2000, 0) * 0.04
  - quarterly_method: max(m3 - 6000, 0) * 0.04
  - gap: monthly_method - quarterly_method
expected:
  monthly_method: 280
  quarterly_method: 120
  gap: 160
```

## When to refuse or refer

- The s.5(5) election to use the Income Tax Act.
- Representative receipts and mixed goods and services businesses.
- Non-ordinary payments to individuals (s.37 deductible payments to residents).

## Filing and payment

1. Register for UBT with IRD.
2. File UBT-01 and pay through SMARTS by 15 March, 15 June, 15 September and 15 December.

## Completion checklist

- Business status checked; goods and services kept apart.
- Allowances applied; method recorded.
- Quarterly return by the 15th.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act Cap. 20.22 (2017 revision): read for s.3(3) (1 May 1980 exclusion) and ss.36, 37 and 68 to 71 | https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf | 2026-11-14 |
| Unincorporated Business Tax Act Cap. 18.46 (2017 revision): read for ss.3 to 8 (4%, EC$12,500, EC$2,000, quarterly returns) | https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_46-Unincorporated-Business-Tax-Act.pdf | 2026-11-14 |
| IRD UBT guide: read for the quarterly allowances of $37,500.00 and $6,000.00, quarter mapping and weekend rule | https://www.sknird.com/wp-content/uploads/2020/05/200701012021.pdf | 2026-11-14 |
| IRD UBT-01 return: read for the allowance lines and the COVID relief line | https://www.sknird.com/wp-content/uploads/2024/02/UBT-Return-Updated-3.0.pdf | 2026-11-11 |
| IRD tax calendar: read for 15 December 2026 | https://www.sknird.com/tax-calendar/ | 2026-11-11 |

Not yet confirmed: which allowance method IRD accepts; any relief authority for the COVID line; UBT-01 and the calendar were read by Ryan Duguid on 2026-11-11 and not re-opened here.
