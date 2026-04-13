---
name: qc-individual-return
description: >
  Use this skill whenever asked about Quebec provincial income tax (TP-1) for a self-employed sole proprietor. Trigger on phrases like "Quebec tax", "TP-1", "Quebec income tax", "QPP", "QPIP", "Revenu Quebec", "QHSF", "health services fund", "solidarity tax credit", "Quebec abatement", or any question about computing Quebec provincial tax. ALWAYS read this skill before touching any Quebec provincial tax work.
version: 2.0
jurisdiction: CA-QC
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
  - ca-fed-t1-return
---

# Quebec TP-1 Provincial Income Tax -- Sole Proprietor Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Canada -- Quebec |
| Tax | Quebec provincial income tax (TP-1) + QPP + QPIP + QHSF |
| Currency | CAD only |
| Tax year | Calendar year |
| Primary legislation | Taxation Act (Quebec), CQLR c. I-3 |
| Supporting legislation | QPP Act; QPIP Act; ITA (Canada) |
| Tax authority | Revenu Quebec (provincial); CRA (federal) |
| Filing portal | Revenu Quebec My Account (ImpotNet) |
| Form | TP-1 + Schedule E (QPP) + Schedule F (QPIP) + TP-80 (self-employment) |
| Filing deadline | June 15 (self-employed); payment due April 30 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- Canadian CPA sign-off required |
| Skill version | 2.0 |

**CRITICAL: Quebec files a SEPARATE provincial return (TP-1) with Revenu Quebec, not through CRA.**

### Quebec Tax Rates (2025)

| Taxable Income (CAD) | Rate |
|---|---|
| 0 -- 53,255 | 14% |
| 53,256 -- 106,495 | 19% |
| 106,496 -- 129,590 | 24% |
| 129,591+ | 25.75% |

### QPP Self-Employed (2025)

| Item | Value |
|---|---|
| QPP rate (double) | 12.80% (vs CPP 11.90%) |
| QPP2 rate (double) | 8.00% |
| Max QPP contribution | $8,678.40 |
| Max QPP2 contribution | $792.00 |

### QPIP Self-Employed (2025)

| Item | Value |
|---|---|
| Rate | 0.878% |
| Max insurable earnings | $98,000 |
| Max premium | $860.44 |

### QHSF Self-Employed

0% below $16,780. Graduated to 1% at $59,885. 1% above $59,885.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown province | Do not apply this skill |
| Unknown parts familiales | 1 part (single) |
| Unknown QHSF income | Apply graduated formula |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- province on Dec 31 (must be Quebec), net self-employment income, marital status.

**Recommended** -- QPP from employment (RL-1), rent/property tax paid, family situation.

**Ideal** -- complete TP-80, prior TP-1, RL slips.

### Refusal Catalogue

**R-QC-1 -- Not Quebec resident.** "Province is not Quebec on December 31."

**R-QC-2 -- Corporations.** "Corporate entities file separate Quebec returns."

**R-QC-3 -- Part-year resident.** "Escalate."

---

## Section 3 -- Transaction Pattern Library

Quebec income tax is computed from TP-80 (Quebec equivalent of T2125). Transaction classification follows the same patterns as `ca-fed-t2125`. Quebec taxable income may differ from federal due to Quebec-specific rules.

---

## Section 4 -- Worked Examples

### Example 1 -- Low Income

**Input:** Quebec taxable income $30,000. Self-employment $30,000. Single.

**Computation:**
- Quebec tax: $30,000 x 14% = $4,200. Credit: $18,056 x 14% = $2,527.84. Net tax: $1,672.16
- QPP: ($30,000 - $3,500) x 12.80% = $3,392.00
- QPIP: $30,000 x 0.878% = $263.40
- QHSF: ~$92 (graduated formula)
- Total: ~$5,419.58

### Example 2 -- Mid-Range

**Input:** Quebec taxable income $80,000. Single.

**Computation:**
- Tax: $53,255 x 14% + $26,745 x 19% = $12,537.25. Credit: $2,527.84. Net: $10,009.41
- QPP: max $8,678.40. QPP2: $696.00. QPIP: $702.40. QHSF: $800.
- Total: ~$20,886.21

### Example 3 -- High Income

**Input:** Quebec taxable income $200,000. Single.

**Computation:**
- Tax through all 4 brackets: $41,244.68. Credit: $2,527.84. Net: $38,716.84
- QPP: $8,678.40. QPP2: $792.00. QPIP: $860.44. QHSF: $2,000.
- Total: ~$51,047.68

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Separate Provincial Return

Quebec is the only province that administers its own income tax. TP-1 filed with Revenu Quebec; T1 filed with CRA (with 16.5% Quebec abatement on federal tax).

### 5.2 QPP vs CPP

Quebec residents always contribute to QPP, never CPP. QPP rate: 12.80% (higher than CPP 11.90%). Half deductible, half credited.

### 5.3 QPIP

Replaces EI maternity/parental benefits in Quebec. Self-employed rate: 0.878%. Fully deductible from Quebec income.

### 5.4 QHSF

Self-employed pay directly on TP-1. Graduated from 0% to 1% between $16,780 and $59,885. Flat 1% above $59,885.

### 5.5 Quebec Abatement

16.5% abatement on federal basic tax (on federal T1, line 44000).

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Solidarity Tax Credit

QST component $360/adult + housing $756 + Northern village $2,005. Reduced by 3% of family income above $40,060. Flag for reviewer.

### 6.2 Work Premium

Refundable credit based on work income. Varies by family status. Flag for reviewer.

### 6.3 Quebec vs Federal Income Differences

Quebec taxable income may differ from federal. Always compute independently. Flag for reviewer.

### 6.4 QPP vs CPP Interaction

If client has both QPP and CPP contributions in the same year (employment outside Quebec), adjustments needed. Flag.

---

## Section 7 -- Excel Working Paper Template

```
QUEBEC TP-1 -- Working Paper (2025)

A. INCOME
  A1. Quebec taxable income (TP-1 line 299)         ___________
  A2. Net self-employment income                     ___________

B. QUEBEC TAX
  B1. Gross Quebec tax (4 brackets)                  ___________
  B2. Quebec non-refundable credits (x 14%)          ___________
  B3. Net Quebec tax (B1 - B2, min 0)                ___________

C. SOCIAL CONTRIBUTIONS
  C1. QPP (Schedule E)                               ___________
  C2. QPP2                                           ___________
  C3. QPIP (Schedule F)                              ___________
  C4. QHSF (line 448)                               ___________

D. TOTAL QUEBEC OBLIGATIONS
  D1. B3 + C1 + C2 + C3 + C4                        ___________

REVIEWER FLAGS:
  [ ] Province confirmed as Quebec?
  [ ] QPP rates used (NOT CPP)?
  [ ] Quebec income computed independently?
  [ ] QHSF graduated formula applied?
  [ ] Quebec abatement noted on federal?
```

---

## Section 8 -- Bank Statement Reading Guide

Quebec tax is computed from TP-80 data. Bank statement classification follows `ca-fed-t2125` patterns. Quebec-specific banks: Desjardins (CSV: Date, Description, Withdrawal, Deposit).

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- QUEBEC TP-1
1. Province of residence on December 31?
2. Net self-employment income?
3. Marital status and spouse income?
4. Number of dependant children?
5. QPP contributions from employment (RL-1)?
6. QPIP premiums from employment?
7. Rent paid or property tax paid?
8. Municipal address (for solidarity credit)?
9. Medical expenses, charitable donations?
10. Prior year avis de cotisation (TP-1)?
```

---

## Section 10 -- Reference Material

| Topic | Reference |
|---|---|
| Quebec brackets | Taxation Act (Quebec), s. 750 |
| Non-refundable credits | Taxation Act (Quebec), s. 752+ |
| QPP | Act respecting the QPP, s. 50+ |
| QPIP | Act respecting parental insurance |
| QHSF | Act respecting RAMQ, s. 34 |
| Quebec abatement | ITA (Canada), s. 120(2) |
| Solidarity credit | Taxation Act (Quebec), s. 1029.8.116.12+ |

---

## PROHIBITIONS

- NEVER apply this skill if province is not Quebec on December 31
- NEVER use CPP rates for Quebec residents -- always QPP
- NEVER copy federal taxable income to Quebec without verification
- NEVER forget the QHSF contribution
- NEVER forget the Quebec abatement on the federal return
- NEVER combine with another provincial skill
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
