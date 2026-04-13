---
name: bvi-tax
description: >
  Use this skill whenever asked about British Virgin Islands (BVI) taxation, payroll tax, or the absence of income tax and VAT. Trigger on phrases like "BVI tax", "British Virgin Islands tax", "BVI VAT", "BVI payroll tax", or any request involving BVI tax compliance. BVI does NOT have income tax, capital gains tax, or VAT. The primary tax is payroll tax. ALWAYS read this skill before handling any BVI tax work.
version: 2.0
jurisdiction: VG
tax_year: 2025
category: international
---

# British Virgin Islands (BVI) Tax Compliance Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | British Virgin Islands (BVI) |
| Tax | Payroll tax (primary), customs duties, property tax, social security, NHI |
| Currency | USD |
| Tax year | Calendar year |
| Primary legislation | Payroll Taxes Act, 2004 (as amended); Customs Management and Duties Act |
| Supporting legislation | BVI Business Companies Act, 2004; Economic Substance Act, 2018 |
| Tax authority | Inland Revenue Department (IRD) |
| Filing portal | https://www.bvi.gov.vg/departments/inland-revenue-department |
| Filing deadline | Payroll tax monthly by 15th; annual reconciliation March 31 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a licensed BVI practitioner |
| Skill version | 2.0 |

### Tax Landscape

| Tax Type | Status |
|---|---|
| Income Tax (personal/corporate) | None |
| Capital Gains Tax | None |
| VAT / Sales Tax | None |
| Withholding Tax | None |
| Payroll Tax | Yes |
| Customs Duties | Yes |
| Property Tax | Yes |
| Social Security (SSB) | Yes -- 9% total (4.5% each) |
| National Health Insurance (NHI) | Yes -- 7.5% total (3.75% each) |

### Payroll Tax Rates

**Class 1** (<=7 employees, payroll <=USD 150,000, revenue <=USD 300,000): Employer 2% + Employee 8% = 10%.

**Class 2** (all others): Employer 6% + Employee 8% = 14%.

Employee exemption: first USD 10,000 annual remuneration exempt.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown employer class | Class 2 |
| Unknown duty rate | General merchandise |
| Unknown economic substance | Assume relevant activity applies |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- payroll records, employee count, employer classification.

**Recommended** -- remuneration breakdown by employee, BVI BC registration, prior returns.

**Ideal** -- complete payroll export, economic substance filings, customs records.

### Refusal Catalogue

**R-VG-1 -- Income tax.** "BVI has no income tax."

**R-VG-2 -- VAT/sales tax.** "BVI has no VAT or sales tax."

**R-VG-3 -- Economic substance detail.** "Escalate to specialist."

**R-VG-4 -- CRS/FATCA compliance.** "Escalate to specialist."

---

## Section 3 -- Compliance Pattern Library

### 3.1 Employer Payment Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES, BONUS, COMMISSION | Payroll tax base | Include in taxable remuneration |
| BENEFITS IN KIND | Payroll tax base | Include |
| CONTRACTOR (independent) | Not payroll tax | Verify independence |
| SSB CONTRIBUTION | Social security | 4.5% employer + 4.5% employee |
| NHI CONTRIBUTION | Health insurance | 3.75% + 3.75% |

### 3.2 Customs Duty Categories

| Category | Rate |
|---|---|
| General merchandise | 5% -- 20% |
| Food/essential goods | Lower or exempt |
| Motor vehicles | 20% + environmental levy |
| Building materials | 5% -- 10% |

### 3.3 BVI BC Annual Fees

| Authorized Shares | Annual Fee (USD) |
|---|---|
| Up to 50,000 (no par) | 450 |
| 50,001+ | 1,200 |

---

## Section 4 -- Worked Examples

### Example 1 -- Payroll Tax (Class 2)

**Input:** Monthly payroll USD 50,000, 10 employees.

**Computation:** Employer payroll tax: 6% x USD 50,000 = USD 3,000/month. Employee: 8% on remuneration above USD 10,000 annual exemption. Plus SSB 4.5% each + NHI 3.75% each.

### Example 2 -- BVI BC Annual Obligations

**Input:** BVI BC with 10,000 no-par shares, no employees.

**Classification:** Annual fee USD 450. No income tax. No payroll tax. Economic substance filing if conducting relevant activities.

### Example 3 -- Import Duty

**Input:** Office equipment USD 10,000.

**Computation:** Duty ~15%: USD 1,500. No VAT. No sales tax.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 No Income Tax / No VAT

No personal/corporate income tax, no capital gains tax, no VAT/sales tax, no withholding tax, no estate tax.

### 5.2 Payroll Tax Filing

Monthly by 15th. Annual reconciliation March 31. Late filing: USD 50/day. Late payment: 1.5%/month.

### 5.3 Social Security and NHI

SSB: 4.5% employer + 4.5% employee. NHI: 3.75% + 3.75%.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Payroll Tax Exemptions

Small business concessions may apply. Flag for practitioner.

### 6.2 Economic Substance

Entities conducting relevant activities must demonstrate adequate substance in BVI. Flag for specialist.

### 6.3 Stamp Duty

Real estate: 4% buyer + 4% seller. Belonger concessions may apply.

---

## Section 7 -- Excel Working Paper Template

```
BVI TAX -- Working Paper

A. PAYROLL TAX
  A1. Total remuneration          ___________
  A2. Employer class              ___________
  A3. Employer payroll tax        ___________
  A4. Employee payroll tax        ___________

B. SOCIAL SECURITY & NHI
  B1. SSB employer (4.5%)         ___________
  B2. NHI employer (3.75%)        ___________

C. BVI BC FEES
  C1. Annual government fee       ___________

REVIEWER FLAGS:
  [ ] Employer classification confirmed?
  [ ] Employee exemption applied?
  [ ] Economic substance filing required?
```

---

## Section 8 -- Bank Statement Reading Guide

| Bank | Format | Key Fields |
|---|---|---|
| VP Bank, First Caribbean | PDF, CSV | Date, Description, Debit, Credit, Balance |
| Scotiabank BVI | CSV | Date, Narrative, Amount |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- BVI TAX
1. Do you have employees in BVI?
2. How many employees?
3. Total payroll?
4. Employer class (1 or 2)?
5. Do you import goods?
6. BVI Business Company held?
7. Relevant activities for economic substance?
8. Non-Belonger employees (work permits)?
9. Property in BVI?
10. Prior returns available?
```

---

## Section 10 -- Reference Material

| Topic | Reference |
|---|---|
| Payroll tax | Payroll Taxes Act, 2004 |
| Customs | Customs Management and Duties Act |
| BVI BCs | BVI Business Companies Act, 2004 |
| Economic substance | Economic Substance Act, 2018 |
| Social security | Social Security Act |
| Health insurance | National Health Insurance Act |

---

## PROHIBITIONS

- NEVER state BVI has income tax -- it does not
- NEVER state BVI has VAT or sales tax -- it does not
- NEVER apply income tax or VAT calculations to BVI transactions
- NEVER ignore payroll tax obligations
- NEVER confuse government fees with taxes
- NEVER ignore economic substance requirements
- NEVER ignore SSB and NHI contributions
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
