---
name: bc-individual-return
description: >
  Use this skill whenever asked about British Columbia provincial income tax for a self-employed sole proprietor. Trigger on phrases like "BC tax", "BC428", "British Columbia income tax", "BC tax brackets", "BC tax reduction", "BC climate action tax credit", "provincial tax BC", or any question about computing BC provincial tax for a self-employed individual. Covers BC tax brackets, personal credits, BC tax reduction, climate action tax credit, and BC-specific rules. ALWAYS read this skill before touching any BC provincial tax work.
version: 2.0
jurisdiction: CA-BC
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
  - ca-fed-t1-return
---

# British Columbia Provincial Income Tax -- Sole Proprietor Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Canada -- British Columbia |
| Tax | Provincial income tax (BC428) |
| Currency | CAD only |
| Tax year | Calendar year |
| Primary legislation | BC Income Tax Act, RSBC 2002, c. 27 |
| Supporting legislation | Income Tax Act (Canada); BC Budget 2025 |
| Tax authority | CRA on behalf of BC |
| Filing portal | CRA My Account / NETFILE / EFILE |
| Form | BC428 -- British Columbia Tax |
| Filing deadline | June 15 (self-employed); payment due April 30 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- Canadian CPA sign-off required |
| Skill version | 2.0 |

### BC Tax Rates (2025)

| Taxable Income (CAD) | Marginal Rate | Cumulative Tax |
|---|---|---|
| 0 -- 47,937 | 5.06% | 2,426 |
| 47,938 -- 95,875 | 7.70% | 6,117 |
| 95,876 -- 110,076 | 10.50% | 7,608 |
| 110,077 -- 133,664 | 12.29% | 10,508 |
| 133,665 -- 181,232 | 14.70% | 17,500 |
| 181,233 -- 252,752 | 16.80% | 29,515 |
| 252,753+ | 20.50% | 29,515+ |

### Key BC Credits (2025)

| Credit | Amount | Tax Value (x 5.06%) |
|---|---|---|
| Basic personal amount | $12,580 | $636 |
| Spousal amount | $12,580 minus spouse income | up to $636 |

### BC Tax Reduction (Low Income)

Maximum reduction: $521 + $152 per dependant. Reduced by 3.56% of net income. Eliminated at ~$14,635 net income (single).

### Climate Action Tax Credit (Refundable)

$504/individual + $252/spouse + $126/child (annual, paid quarterly by CRA). Reduced by 2% of family income above $41,071.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown province | Do not apply this skill |
| Unknown bracket year | Use 2025 indexed figures |
| Unknown medical/charitable amounts | $0 |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- province of residence on December 31 (must be BC), federal taxable income (T1 line 26000), federal net income (T1 line 23600).

**Recommended** -- marital status, spouse income, dependants, medical expenses, charitable donations.

**Ideal** -- complete T1 data, prior year BC428, disability certificate if applicable.

### Refusal Catalogue

**R-BC-1 -- Not BC resident.** "Province of residence on December 31 is not BC. This skill does not apply."

**R-BC-2 -- Corporations/trusts.** "This skill covers individual sole proprietors only."

**R-BC-3 -- Part-year resident.** "Part-year provincial residency requires specialist analysis. Escalate."

**R-BC-4 -- First Nations exemption.** "Section 87 Indian Act exemptions require specialist analysis. Escalate."

---

## Section 3 -- Transaction Pattern Library

BC provincial tax is computed from federal return data, not directly from bank transactions. The transaction pattern library is in the `ca-fed-t2125` skill. This skill consumes the output of that computation (taxable income, net income) and applies BC rates and credits.

---

## Section 4 -- Worked Examples

### Example 1 -- Low Income, Single

**Input:** Taxable income $25,000. Net income $25,000. Single, no dependants.

**Computation:**
- Gross BC tax: $25,000 x 5.06% = $1,265.00
- BC basic personal credit: $12,580 x 5.06% = $636.55
- BC basic tax: $1,265.00 - $636.55 = $628.45
- BC tax reduction: $521 - (3.56% x $25,000) = $521 - $890 = $0 (eliminated)
- Net BC tax: $628.45

### Example 2 -- Mid-Range Income

**Input:** Taxable income $80,000. Single.

**Computation:**
- First $47,937 at 5.06% = $2,425.61
- $32,063 at 7.70% = $2,468.85
- Gross BC tax: $4,894.46
- Credit: $636.55
- Net BC tax: $4,257.91

### Example 3 -- High Income, Top Bracket

**Input:** Taxable income $300,000. Married, spouse income $0.

**Computation:**
- Tax through $252,752 = $29,515
- $47,248 at 20.50% = $9,685.84
- Gross BC tax: $39,200.84
- Credits: basic $636.55 + spousal $636.55 = $1,273.10
- Net BC tax: $37,927.74

### Example 4 -- Below Basic Personal Amount

**Input:** Taxable income $10,000.

**Computation:**
- Gross BC tax: $506.00
- Credit: $636.55
- Net BC tax: $0

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 BC Tax Computation

Start with taxable income from T1 line 26000. Apply 7 BC marginal rates. Subtract non-refundable credits at 5.06%. Apply BC tax reduction if applicable.

### 5.2 BC Tax Reduction

**Legislation:** BC ITA, s. 4.62

Maximum $521 + $152/dependant. Credit percentage: 3.56% of net income. Reduction = maximum - credit percentage. Cannot go below zero.

### 5.3 Political Contribution Credit

First $100 at 75%, $100.01-$550 at 50% + $75, $550.01-$1,150 at 33.33% + $300. Maximum $500.

### 5.4 Dividend Tax Credits

Eligible dividends: 12.0% of grossed-up amount. Non-eligible: 1.96%.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Multiple Provinces of Self-Employment

If business income earned in multiple provinces, T2203 may be required. Flag for reviewer.

### 6.2 BC Renter's Tax Credit

Up to $400/year for tenants under income threshold. Cannot claim both renter credit and home office deduction for same space. Flag for reviewer.

### 6.3 BC Home Renovation Tax Credit for Seniors

10% of eligible expenses (max $10,000) for 65+ individuals. Flag for reviewer.

---

## Section 7 -- Excel Working Paper Template

```
BC PROVINCIAL TAX -- Working Paper (2025)

A. INCOME
  A1. Taxable income (T1 line 26000)               ___________
  A2. Net income (T1 line 23600)                    ___________

B. BC TAX COMPUTATION
  B1. Gross BC tax (7 brackets)                     ___________
  B2. BC non-refundable credits (x 5.06%)           ___________
  B3. BC basic tax (B1 - B2, min 0)                 ___________
  B4. BC tax reduction                              ___________
  B5. Net BC tax (B3 - B4, min 0)                   ___________
  B6. BC dividend tax credits                       ___________
  B7. BC political contribution credit              ___________
  B8. BC tax payable                                ___________

REVIEWER FLAGS:
  [ ] Province confirmed as BC on Dec 31?
  [ ] 2025 indexed thresholds used?
  [ ] Part-year / multi-province flagged?
```

---

## Section 8 -- Bank Statement Reading Guide

BC provincial tax is not computed from bank statements directly. See `ca-fed-t2125` for bank statement classification. BC428 consumes the federal return output.

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- BC PROVINCIAL TAX
1. Province of residence on December 31?
2. Federal taxable income (T1 line 26000)?
3. Federal net income (T1 line 23600)?
4. Marital status and spouse net income?
5. Number of dependants?
6. Medical expenses claimed federally?
7. Charitable donations claimed federally?
8. BC political contributions?
9. Disability certificate (T2201)?
10. Do you rent your residence in BC?
```

---

## Section 10 -- Reference Material

| Topic | Reference |
|---|---|
| BC tax brackets | BC ITA, s. 4.1 |
| Non-refundable credits | BC ITA, s. 4.3 et seq. |
| BC tax reduction | BC ITA, s. 4.62 |
| Political contribution credit | BC ITA, s. 4.73 |
| Climate action tax credit | BC ITA, s. 8.1 |
| Dividend tax credits | BC ITA, s. 4.69 |

---

## PROHIBITIONS

- NEVER apply this skill if province is not BC on December 31
- NEVER compute tax for corporations, partnerships, or trusts
- NEVER guess at First Nations exemption amounts
- NEVER use prior-year bracket amounts
- NEVER combine this with another provincial skill for the same year
- NEVER claim expired credits
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
