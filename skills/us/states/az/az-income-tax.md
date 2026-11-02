---
name: az-income-tax
description: Use this skill whenever asked about Arizona individual income tax for self-employed individuals or sole proprietors — filing Form 140, AZ estimated tax (Form 140ES), Arizona flat tax rate, Arizona standard deduction, or any query involving Arizona state income tax compliance. Trigger on phrases like "Arizona income tax", "AZ income tax", "Form 140", "Arizona estimated tax", "Arizona self-employed tax", "AZDOR income tax", "Arizona flat tax", or "ARS §43".
jurisdiction: US-AZ
tier: 2
last_updated: 2026-06-12
version: "0.1"
validation_status: ai-drafted-q3
---

# Arizona Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Scope.** This skill covers Arizona individual income tax for self-employed individuals and sole proprietors filing Form 140. It addresses tax computation, deductions, estimated payments, and form mapping.
> **Quality tier.** Q3 — AI-drafted with citations; not independently verified by a licensed professional.

## Section 1: Metadata

| Field | Value |
|---|---|
| Jurisdiction | Arizona, United States |
| Jurisdiction code | US-AZ |
| Tax authority | Arizona Department of Revenue (AZDOR) |
| Filing portal | https://www.aztaxes.gov |
| Legislation citation | Arizona Revised Statutes Title 43 (Taxation of Income) |
| Primary form | Form 140 — Arizona Resident Personal Income Tax |
| Filing deadline | April 15 (follows federal deadline) |
| Version | 0.1 |
| Generated | 2026-05-22 |
| Validation status | AI-drafted — Q3 |

### Sources consulted

1. Arizona Department of Revenue — Individual Income Tax Highlights (2025): https://azdor.gov/forms/individual-income-tax-highlights
2. Arizona Department of Revenue — Individual Estimated Tax Payments: https://azdor.gov/individuals/individual-estimated-tax-payments
3. Arizona Form 140 Instructions (TY 2025): https://azdor.gov/forms/individual
4. Arizona Tax Tables 2025: https://www.taxformcalculator.com/arizona/tax-tables/2025.html

---

## Section 2: Quick reference — rates and thresholds

### Tax rate (TY 2025)

Arizona imposes a **flat income tax rate of 2.5%** on all taxable income, regardless of filing status or income level. This flat rate took effect in tax year 2023.

| Filing status | Rate | Applies to |
|---|---|---|
| All statuses | 2.5% | All Arizona taxable income |

### Standard deduction (TY 2025)

| Filing status | Standard deduction |
|---|---|
| Single | $15,750 |
| Married Filing Jointly | $31,500 |
| Married Filing Separately | $15,750 |
| Head of Household | $23,625 |

Arizona also allows a **Standard Deduction Increase** equal to 34% of qualifying charitable contributions (TY 2025), calculated on page 3 of Form 140.

### Personal exemptions

Arizona does not use personal exemptions in the traditional sense. The standard deduction effectively replaces the exemption for most filers.

---

## Section 3: How this skill works with the federal return

1. **Starting point:** Arizona begins with **federal adjusted gross income** (federal Form 1040, Line 11).
2. **Arizona additions:** Add back amounts deducted federally but not recognized by Arizona (e.g., other states' municipal bond interest).
3. **Arizona subtractions:** Subtract Arizona-exempt income (e.g., Social Security benefits, U.S. government interest, Arizona-specific exclusions).
4. **Arizona AGI:** Federal AGI ± additions/subtractions.
5. **Deductions:** Subtract standard deduction or Arizona itemized deductions.
6. **Result:** Arizona taxable income × 2.5% = tax liability.

---

## Section 4: Self-employed specific rules

### Federal conformity
- Arizona generally conforms to the Internal Revenue Code as of a specific date (rolling conformity with some exceptions).
- Schedule C business income and deductions flow through federal AGI into Arizona's computation.

### QBI deduction (§199A)
- The federal QBI deduction reduces federal taxable income but does **not** directly apply to Arizona's computation since Arizona starts from federal AGI (above the line).
- However, Arizona allows its own subtraction for certain small business income (check current year instructions).

### SE health insurance deduction
- Flows through federal AGI (above-the-line deduction) and is automatically reflected in Arizona's starting point.

### Retirement contributions
- SEP-IRA and Solo 401(k) contributions reduce federal AGI and therefore reduce Arizona starting income.

### Home office deduction
- Federal home office deduction (simplified or actual) flows through Schedule C and is reflected in federal AGI.

### Estimated tax payments (Form 140ES)

- **Required if:** Your Arizona gross income exceeds $75,000 (single/MFS/HOH) or $150,000 (MFJ) for the current or prior year.
- **Safe harbor:** Total estimated payments + withholding must equal the lesser of 90% of current year tax or 100% of prior year tax.
- **Due dates:** April 15, June 15, September 15, January 15.
- **Payment methods:** Online via AZTaxes.gov or mail Form 140ES to AZDOR.
- **Small business variant:** Form 140ES-SBI for those electing the small business income tax.

---

## Section 5: Tier 1 rules — deterministic

| # | Rule | Logic |
|---|---|---|
| T1-01 | Apply 2.5% flat rate to Arizona taxable income | Single rate × taxable income |
| T1-02 | Standard deduction by filing status | Fixed amounts: $15,750 / $31,500 / $23,625 |
| T1-03 | Social Security benefits fully exempt | Subtract from AZ computation |
| T1-04 | U.S. government bond interest exempt | Subtract from AZ income |
| T1-05 | Estimated tax threshold | Gross income > $75,000 (single) or $150,000 (MFJ) |
| T1-06 | Standard deduction increase | Add 34% of qualifying charitable contributions |

---

## Section 6: Tier 2 rules — requires judgment

| # | Rule | Why judgment needed |
|---|---|---|
| T2-01 | Standard deduction vs. itemized | Taxpayer must compare both methods |
| T2-02 | IRC conformity date issues | Some federal provisions may not be adopted; requires checking current conformity |
| T2-03 | Part-year resident allocation | Requires apportionment of income to AZ residency period |
| T2-04 | Small Business Income Tax election | Taxpayer may elect to pay 2.5% separately on business income — requires evaluation of benefit |
| T2-05 | Credit for taxes paid to other states | Requires analysis of multistate income sourcing (Form 309) |
| T2-06 | Charitable contribution substantiation | Standard deduction increase requires documentation of qualified contributions |

---

## Section 7: Supplier pattern library

| Pattern on bank/CC statement | Likely meaning |
|---|---|
| `AZ DEPT OF REVENUE` / `AZDOR` | Arizona income tax payment (estimated or balance due) |
| `AZTAXES.GOV` | Electronic payment via AZTaxes portal |
| `STATE OF AZ TAX` | State tax payment |
| `ARIZONA DOR` | Department of Revenue payment |

---

## Section 8: Form mapping

| Computed value | Form 140 line |
|---|---|
| Federal AGI | Line 12 |
| Arizona additions | Line 13 |
| Arizona subtractions | Line 15 |
| Arizona adjusted gross income | Line 16 |
| Standard or itemized deduction | Line 18 |
| Arizona taxable income | Line 19 |
| Tax (2.5% × Line 19) | Line 20 |
| Credits | Lines 21–30 |
| Estimated payments + withholding | Lines 40–43 |
| Balance due / refund | Lines 52–56 |

---

## Section 9: Refusal catalogue

This skill must refuse and recommend professional review when:

| # | Condition |
|---|---|
| R-01 | Taxpayer has multistate business activity requiring apportionment |
| R-02 | Taxpayer is a part-year resident (Form 140PY) with complex sourcing |
| R-03 | Taxpayer is considering the Small Business Income Tax election and needs cost-benefit analysis |
| R-04 | Issues involving Arizona tax credits (solar, research, qualified facilities, etc.) |
| R-05 | Taxpayer has Arizona net operating loss carryforward |
| R-06 | Questions about TPT (Transaction Privilege Tax) nexus or classification |
| R-07 | Audit representation or controversy matters |
| R-08 | Any question about tax fraud, evasion, or aggressive positions |

---

## Disclaimer
This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
