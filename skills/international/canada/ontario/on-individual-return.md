---
name: on-individual-return
description: >
  Use this skill whenever asked about Ontario provincial income tax for a self-employed sole proprietor. Trigger on phrases like "Ontario tax", "ON428", "Ontario income tax", "Ontario surtax", "Ontario Health Premium", "OHP", "OEPTC", "Ontario trillium", "provincial tax Ontario", or any question about computing Ontario provincial tax. ALWAYS read this skill before touching any Ontario provincial tax work.
version: 2.0
jurisdiction: CA-ON
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
  - ca-fed-t1-return
---

# Ontario Provincial Income Tax -- Sole Proprietor Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Canada -- Ontario |
| Tax | Provincial income tax (ON428) + Ontario Health Premium + Ontario surtax |
| Currency | CAD only |
| Tax year | Calendar year |
| Primary legislation | Taxation Act, 2007, S.O. 2007, c. 11, Sch. A |
| Tax authority | CRA on behalf of Ontario |
| Filing portal | CRA My Account / NETFILE / EFILE |
| Form | ON428 -- Ontario Tax; ON479 (Credits); ON-BEN (Trillium) |
| Filing deadline | June 15 (self-employed); payment due April 30 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- Canadian CPA sign-off required |
| Skill version | 2.0 |

### Ontario Tax Rates (2025)

| Taxable Income (CAD) | Rate | Cumulative Tax |
|---|---|---|
| 0 -- 52,886 | 5.05% | 2,671 |
| 52,887 -- 105,775 | 9.15% | 7,510 |
| 105,776 -- 150,000 | 11.16% | 12,447 |
| 150,001 -- 220,000 | 12.16% | 20,959 |
| 220,001+ | 13.16% | 20,959+ |

### Ontario Surtax

20% on basic tax exceeding $5,315 + 36% on basic tax exceeding $6,802. Thresholds NOT indexed.

### Ontario Health Premium (OHP)

| Taxable Income | OHP |
|---|---|
| 0 -- 20,000 | $0 |
| 20,001 -- 25,000 | 6% of excess over $20,000 (max $300) |
| 25,001 -- 36,000 | $300 |
| 36,001 -- 48,000 | Step increases to $600 |
| 48,601 -- 72,000 | $600 |
| 72,601 -- 200,000 | $750 |
| 200,601+ | $900 (maximum) |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown province | Do not apply this skill |
| Unknown bracket year | 2025 indexed figures |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- province of residence on Dec 31 (must be Ontario), federal taxable income (T1 line 26000), federal net income.

**Recommended** -- marital status, spouse income, children, property tax/rent paid, municipality.

**Ideal** -- complete T1 data, prior ON428, disability certificate.

### Refusal Catalogue

**R-ON-1 -- Not Ontario resident.** "Province is not Ontario on December 31."

**R-ON-2 -- Corporations/trusts.** "Individual sole proprietors only."

**R-ON-3 -- Part-year resident.** "Escalate."

**R-ON-4 -- First Nations exemption.** "Escalate."

---

## Section 3 -- Transaction Pattern Library

Ontario tax is computed from federal return data. Transaction classification is in `ca-fed-t2125`.

---

## Section 4 -- Worked Examples

### Example 1 -- Low Income

**Input:** Taxable income $18,000. Single.

**Computation:**
- Gross Ontario tax: $18,000 x 5.05% = $909.00
- Basic personal credit: $11,865 x 5.05% = $599.18
- Basic tax: $309.82. Surtax: $0. OHP: $0.
- Ontario tax: $309.82

### Example 2 -- Mid-Range

**Input:** Taxable income $75,000. Single.

**Computation:**
- $52,886 at 5.05% + $22,114 at 9.15% = $4,694.17
- Credit: $599.18. Basic tax: $4,094.99. Surtax: $0. OHP: $750.
- Ontario tax: $4,844.99

### Example 3 -- High Income, Surtax

**Input:** Taxable income $200,000. Single.

**Computation:**
- Gross tax through brackets: $18,525.59
- Credit: $599.18. Basic tax: $17,926.41
- Surtax 1: 20% x ($17,926.41 - $5,315) = $2,522.28
- Surtax 2: 36% x ($17,926.41 - $6,802) = $4,004.79
- OHP: $750
- Ontario tax: $17,926.41 + $6,527.07 + $750 = $25,203.48

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Ontario Tax Computation

Taxable income -> 5 brackets -> gross tax -> minus non-refundable credits at 5.05% -> basic tax -> plus surtax -> plus OHP.

### 5.2 Ontario Surtax

Surtax = 20% x max(0, basic_tax - $5,315) + 36% x max(0, basic_tax - $6,802). Thresholds frozen (not indexed).

### 5.3 OHP

Based on taxable income (not net income). Maximum $900. NOT reduced by credits.

### 5.4 Credits at 5.05%

Basic personal: $11,865. Spousal: $11,865 minus partner income. Age (65+): $5,590.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Ontario Trillium Benefit

OEPTC: max $1,194 (non-senior). OSTC: $360/person. NOEC: $180 (Northern Ontario only). All reduced by income. Paid by CRA. Flag for reviewer.

### 6.2 CARE Credit

Refundable childcare credit, percentage depends on family income. Flag if client has childcare expenses.

### 6.3 Multiple Provinces

If multi-province allocation required (T2203), flag for reviewer.

---

## Section 7 -- Excel Working Paper Template

```
ONTARIO PROVINCIAL TAX -- Working Paper (2025)

A. INCOME
  A1. Taxable income (T1 line 26000)               ___________

B. ONTARIO TAX
  B1. Gross Ontario tax (5 brackets)                ___________
  B2. Ontario non-refundable credits (x 5.05%)      ___________
  B3. Ontario basic tax (B1 - B2, min 0)            ___________
  B4. Ontario surtax                                ___________
  B5. Ontario tax before OHP (B3 + B4)              ___________
  B6. Ontario Health Premium                        ___________
  B7. Ontario tax payable (B5 + B6)                 ___________

REVIEWER FLAGS:
  [ ] Province confirmed as Ontario?
  [ ] Surtax computed on basic tax (after credits)?
  [ ] OHP NOT reduced by credits?
  [ ] 2025 indexed thresholds used?
```

---

## Section 8 -- Bank Statement Reading Guide

Ontario tax is not computed from bank statements directly. See `ca-fed-t2125`.

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- ONTARIO PROVINCIAL TAX
1. Province of residence on December 31?
2. Federal taxable income?
3. Federal net income?
4. Marital status and spouse income?
5. Number of children?
6. Property tax or rent paid?
7. Northern Ontario resident?
8. Medical expenses, charitable donations?
9. Disability status?
10. Childcare expenses?
```

---

## Section 10 -- Reference Material

| Topic | Reference |
|---|---|
| Ontario brackets | Taxation Act, 2007, s. 3 |
| Surtax | Taxation Act, 2007, s. 3(2) |
| OHP | Taxation Act, 2007, s. 3(5) |
| Non-refundable credits | Taxation Act, 2007, s. 8+ |
| OTB / OEPTC | Taxation Act, 2007, Part IV |
| Dividend tax credits | Taxation Act, 2007, s. 19 |

---

## PROHIBITIONS

- NEVER apply this skill if province is not Ontario on December 31
- NEVER reduce the OHP by tax credits
- NEVER forget the surtax -- it dramatically increases effective rates
- NEVER compute tax for corporations, partnerships, or trusts
- NEVER use prior-year bracket amounts
- NEVER combine with another provincial skill
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
