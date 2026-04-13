---
name: qc-qst-return
description: >
  Use this skill whenever asked about Quebec Sales Tax (QST / TVQ) return preparation for a self-employed sole proprietor or small business. Trigger on phrases like "QST return", "TVQ", "Quebec sales tax", "QST filing", "input tax refund", "ITR", "QST registration", "Revenu Quebec QST", "9.975%", or any question about computing or filing QST. ALWAYS read this skill before touching any QST work.
version: 2.0
jurisdiction: CA-QC
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Quebec Sales Tax (QST) Return -- Sole Proprietor Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Canada -- Quebec |
| Tax | QST (TVQ) at 9.975% -- filed SEPARATELY from federal GST |
| Currency | CAD only |
| Tax year | Calendar year or fiscal year |
| Primary legislation | Act respecting the Quebec Sales Tax (AQST), CQLR c. T-0.1 |
| Supporting legislation | Excise Tax Act (ETA) for GST |
| Tax authority | Revenu Quebec |
| Filing portal | Revenu Quebec My Account (Mon dossier) / ClicSequr |
| Form | VD-403 (QST Return) |
| Filing deadline | Monthly: last day of following month; Quarterly: last day of month after quarter; Annual: 3 months after year-end |
| Contributor | Open Accountants Community |
| Validated by | Pending -- Canadian CPA sign-off required |
| Skill version | 2.0 |

### QST Rate

| Tax | Rate | Since |
|---|---|---|
| QST | 9.975% | January 1, 2013 |

QST is calculated on the price EXCLUDING GST (no tax-on-tax since 2013).

### Small Supplier Threshold

$30,000 (same as GST). If taxable supplies exceed $30,000 in a single quarter or over four consecutive quarters, must register.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown QST registration status | Not registered |
| Unknown supply category | Taxable at 9.975% |
| Unknown business-use % | 0% ITR |
| Unknown meals ITR | 50% (capped) |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- QST registration number, reporting period, total taxable supplies, total QST collected, total QST paid on expenses.

**Recommended** -- supply breakdown (taxable/zero-rated/exempt), sales invoices, purchase invoices with QST numbers.

**Ideal** -- complete bookkeeping, GST return for cross-reference, prior QST returns.

### Refusal Catalogue

**R-QC-QST-1 -- Financial services.** "Exempt -- complex rules. Escalate."

**R-QC-QST-2 -- Real property.** "Real property transactions require specialist analysis. Escalate."

**R-QC-QST-3 -- Non-resident suppliers.** "Specified QST registration rules apply. Escalate."

---

## Section 3 -- Supplier Pattern Library

### 3.1 Output (Sales) Patterns

| Pattern | QST Treatment | Notes |
|---|---|---|
| SERVICE SALE, GOODS SALE | Taxable 9.975% | Standard |
| EXPORT, OUT-OF-PROVINCE | Zero-rated (0%) | No QST; ITRs still claimable |
| BASIC GROCERY, PRESCRIPTION | Zero-rated | Specific items |
| RESIDENTIAL RENT (long-term) | Exempt | No QST; no ITR on inputs |
| FINANCIAL SERVICE | Exempt | No QST |
| PRINTED BOOKS | Zero-rated (QST-specific) | Taxable for GST but zero-rated for QST |
| CHILDREN'S CLOTHING | Zero-rated (QST-specific) | Same |

### 3.2 Input (Purchase) Patterns

| Pattern | ITR Eligible | Notes |
|---|---|---|
| OFFICE SUPPLIES, SOFTWARE | Yes (100%) | Business expense |
| ACCOUNTING, LEGAL | Yes (100%) | Professional fees |
| MEALS, ENTERTAINMENT | Yes (50%) | 50% restriction |
| VEHICLE EXPENSES | Prorate | Business km percentage |
| HOME OFFICE | Prorate | Workspace percentage |
| PERSONAL EXPENSE | No | Never eligible |
| EXEMPT SUPPLY INPUT | No | No ITR for exempt activity inputs |

### 3.3 Self-Assessment Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| AWS, GOOGLE, MICROSOFT (non-QC) | Self-assess QST | Imported services from non-QC suppliers |
| CLOUD SERVICE, SAAS (non-QC) | Self-assess QST | Report on VD-403 line 104 |

---

## Section 4 -- Worked Examples

### Example 1 -- Basic Quarterly Return

**Input:** Taxable supplies $25,000. Zero-rated $2,000. QST paid on expenses $600.

**Computation:**
- QST collected: $25,000 x 9.975% = $2,493.75
- ITRs: $600
- Net QST: $2,493.75 - $600 = $1,893.75 owing

### Example 2 -- Refund Position (Exporter)

**Input:** Taxable supplies $5,000. Zero-rated (exports) $40,000. QST on expenses $1,500.

**Computation:**
- QST collected: $5,000 x 9.975% = $498.75
- ITRs: $1,500 (zero-rated still qualifies)
- Net QST: $498.75 - $1,500 = -$1,001.25 (refund)

### Example 3 -- Meals ITR

**Input:** Business meals $2,000. QST paid $199.50.

**Computation:**
- ITR: $199.50 x 50% = $99.75

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 QST Base

QST applies to the sale price EXCLUDING GST. Selling price $100 -> GST $5 -> QST $9.98 (9.975% of $100, NOT $105).

### 5.2 ITR Eligibility

Must be for commercial activities. Must have documentation with supplier's QST number. Claim within 4 years. Mixed-use: 90%+ = claim 100%; 10% or less = claim 0%; between = actual %.

### 5.3 VD-403 Structure

Line 101: QST collected. Line 104: adjustments. Line 106: ITRs. Line 111: net QST. Line 114: net owing or refund.

### 5.4 Filing Frequency

Over $6M: monthly. $1.5M-$6M: quarterly. Under $1.5M: annual (can elect more frequent).

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Quick Method

Available if annual taxable supplies <= $400,000. Services: 3.4% of QST-included revenue. Goods: 6.6%. 1% credit on first $30,000. Flag for reviewer.

### 6.2 Place of Supply

QST applies to supplies made in Quebec. Goods: where delivered. Services: where recipient located. Flag for cross-border/interprovincial.

### 6.3 Bad Debts

Recover QST on uncollectable invoices via VD-403 line 107. Flag for reviewer.

### 6.4 Self-Assessment on Imported Services

QST must be self-assessed on taxable services from non-resident suppliers. Common for SaaS subscriptions.

---

## Section 7 -- Excel Working Paper Template

```
QUEBEC QST RETURN -- Working Paper

A. OUTPUT
  A1. Taxable supplies                              ___________
  A2. QST collected (A1 x 9.975%)                   ___________
  A3. Adjustments (self-assessments)                 ___________
  A4. Total QST (A2 + A3)                           ___________

B. INPUT
  B1. ITRs on business expenses                     ___________
  B2. ITR adjustments                               ___________
  B3. Net ITRs (B1 - B2)                            ___________

C. NET QST
  C1. A4 - B3                                       ___________
  C2. Instalments paid                              ___________
  C3. Net owing / (refund)                          ___________

REVIEWER FLAGS:
  [ ] QST rate 9.975% used (not 10%, not HST)?
  [ ] QST base excludes GST?
  [ ] Separate from GST return?
  [ ] Meals ITR at 50%?
  [ ] Self-assessment on imported services?
```

---

## Section 8 -- Bank Statement Reading Guide

| Bank | Format | Key Fields |
|---|---|---|
| Desjardins | CSV | Date, Description, Withdrawal, Deposit |
| RBC, TD, BMO, Scotiabank | CSV, PDF | Date, Description, Debit, Credit, Balance |
| National Bank | CSV | Date, Description, Amount |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- QUEBEC QST
1. QST registration number?
2. GST registration number?
3. Filing frequency (monthly/quarterly/annual)?
4. Reporting period dates?
5. Total taxable supplies in period?
6. Zero-rated and exempt supplies?
7. Total QST collected?
8. QST paid on business expenses?
9. Out-of-province or out-of-country sales?
10. Using quick method?
```

---

## Section 10 -- Reference Material

| Topic | Reference |
|---|---|
| QST rate | AQST, s. 16 |
| Registration | AQST, s. 407+ |
| ITRs | AQST, s. 199+ |
| Small supplier | AQST, s. 148 |
| Quick method | AQST, s. 433.1+ |
| Filing deadlines | AQST, s. 468+ |
| Zero-rated (books, children's) | AQST specific schedules |

---

## PROHIBITIONS

- NEVER combine QST and GST into a single return
- NEVER calculate QST on a GST-included price
- NEVER claim ITRs for personal expenses
- NEVER claim ITRs for exempt supply inputs
- NEVER claim more than 50% ITR on meals
- NEVER apply HST rates to Quebec
- NEVER use GST quick method rates for QST
- NEVER ignore self-assessment on imported services
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
