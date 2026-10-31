---
name: al-income-tax
description: Use this skill whenever asked about Alabama individual income tax for self-employed individuals or sole proprietors — filing Form 40, AL estimated tax (Form 40-ES), Alabama tax brackets, Alabama deductions, federal income tax deduction on AL return, or any query involving Alabama state income tax compliance. Trigger on phrases like "Alabama income tax", "AL income tax", "Form 40", "Alabama estimated tax", "Alabama self-employed tax", "ADOR income tax", or "Code of Ala. §40-18".
jurisdiction: US-AL
tier: 2
last_updated: 2026-06-12
version: "0.1"
validation_status: ai-drafted-q3
---

# Alabama Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Scope.** This skill covers Alabama individual income tax for self-employed individuals and sole proprietors filing Form 40. It addresses tax computation, deductions, estimated payments, and form mapping.
> **Quality tier.** Q3 — AI-drafted with citations; not independently verified by a licensed professional.

## Section 1: Metadata

| Field | Value |
|---|---|
| Jurisdiction | Alabama, United States |
| Jurisdiction code | US-AL |
| Tax authority | Alabama Department of Revenue (ADOR) |
| Filing portal | https://myalabamataxes.alabama.gov |
| Legislation citation | Code of Alabama §40-18 (Income Tax) |
| Primary form | Form 40 — Alabama Individual Income Tax Return |
| Filing deadline | April 15 (follows federal deadline) |
| Version | 0.1 |
| Generated | 2026-05-22 |
| Validation status | AI-drafted — Q3 |

### Sources consulted

1. Alabama Department of Revenue — Individual Income Tax Rates: https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/
2. Alabama Form 40 Instruction Booklet (TY 2025): https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf
3. Alabama Form 40-ES (Estimated Tax): https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26f40esblk.pdf
4. Code of Alabama §40-18: https://www.legislature.state.al.us/

---

## Section 2: Quick reference — rates and thresholds

### Tax rates (TY 2025)

**Single, Head of Family, and Married Filing Separately:**

| Taxable income | Rate |
|---|---|
| $0 – $500 | 2% |
| $501 – $3,000 | 4% |
| Over $3,000 | 5% |

**Married Filing Jointly:**

| Taxable income | Rate |
|---|---|
| $0 – $1,000 | 2% |
| $1,001 – $6,000 | 4% |
| Over $6,000 | 5% |

### Personal exemptions

| Filing status | Exemption |
|---|---|
| Single | $1,500 |
| Married Filing Jointly | $3,000 |
| Married Filing Separately | $1,500 |
| Head of Family | $3,000 |
| Dependent exemption | $300 per dependent (min, higher amounts per statute) |

### Standard deduction

Alabama does **not** use a fixed standard deduction amount. The allowable standard deduction is determined from the Standard Deduction Chart published by ADOR, which varies by filing status and Alabama Adjusted Gross Income. Taxpayers must consult the chart in the Form 40 instruction booklet.

**Key feature:** Alabama is one of only three states that allows a deduction for **federal income taxes paid** from state taxable income.

---

## Section 3: How this skill works with the federal return

1. **Starting point:** Alabama begins with **federal adjusted gross income** (federal Form 1040, Line 11).
2. **Alabama additions:** Add back any income excluded federally but taxable in Alabama (e.g., certain interest income from other states' obligations).
3. **Alabama subtractions:** Subtract Alabama-exempt income (e.g., Social Security benefits, certain retirement income, interest on U.S. obligations).
4. **Federal income tax deduction:** Deduct federal income taxes actually paid (or accrued) during the tax year. This is a significant benefit unique to Alabama.
5. **Standard deduction or itemized:** Apply the standard deduction (from chart) or Alabama itemized deductions.
6. **Personal exemption:** Subtract the personal exemption amount.
7. **Result:** Alabama taxable income → apply graduated rates.

---

## Section 4: Self-employed specific rules

### Federal conformity
- Alabama generally conforms to federal IRC for computing income, including Schedule C business deductions.
- The QBI deduction (§199A) is a **federal** deduction that reduces federal tax paid, thereby indirectly reducing the Alabama federal tax deduction — but it does not directly affect Alabama taxable income computation.

### SE health insurance deduction
- Alabama follows the federal deduction for self-employed health insurance premiums (above-the-line on federal return), which flows through to AL AGI.

### Retirement contributions
- SEP-IRA and Solo 401(k) contributions reduce federal AGI and therefore reduce Alabama starting income.

### Home office deduction
- Federal home office deduction (simplified or actual) flows through Schedule C and is reflected in federal AGI.

### Estimated tax payments (Form 40-ES)
- **Threshold:** Must pay estimated tax if you expect to owe ≥ $500 after withholding and credits.
- **Safe harbor:** Pay the lesser of 90% of current year tax or 100% of prior year tax.
- **Due dates:** April 15, June 15, September 15, January 15.
- **Payment methods:** Mail (Form 40-ES voucher to P.O. Box 327485, Montgomery, AL 36132-7485) or electronically via My Alabama Taxes portal.

---

## Section 5: Tier 1 rules — deterministic

| # | Rule | Logic |
|---|---|---|
| T1-01 | Apply graduated rates to Alabama taxable income | Use bracket table above based on filing status |
| T1-02 | Subtract personal exemption from AL adjusted income | Fixed amounts by filing status |
| T1-03 | Federal income tax deduction | Deduct actual federal income tax paid (or liability if accrual) from AL gross income |
| T1-04 | Quarterly estimated tax required if expected liability ≥ $500 | Binary threshold |
| T1-05 | Filing requirement | Single: AGI ≥ $4,000; HOF: AGI ≥ $7,700; MFS: AGI ≥ $5,250; MFJ: AGI ≥ $10,500 |
| T1-06 | Social Security benefits not taxed | Always exclude from AL taxable income |

---

## Section 6: Tier 2 rules — requires judgment

| # | Rule | Why judgment needed |
|---|---|---|
| T2-01 | Standard deduction vs. itemized | Taxpayer must compare both methods; chart-based standard deduction varies by income level |
| T2-02 | Federal tax deduction — paid vs. accrued method | Choice of method affects timing and amount |
| T2-03 | Allocation of income for part-year residents | Requires analysis of residency dates and income sourcing |
| T2-04 | Business vs. hobby determination | Same federal analysis, but affects AL Schedule C flow-through |
| T2-05 | Multistate income allocation | If taxpayer has income from other states, credit for taxes paid elsewhere (Schedule CR) |

---

## Section 7: Supplier pattern library

| Pattern on bank/CC statement | Likely meaning |
|---|---|
| `ALABAMA DOR` / `AL DEPT OF REVENUE` | Alabama income tax payment (estimated or balance due) |
| `ADOR TAX PAYMENT` | Alabama Department of Revenue electronic payment |
| `STATE OF AL TAX` | State tax payment |
| `MY ALABAMA TAXES` | Payment via MAT portal |

---

## Section 8: Form mapping

| Computed value | Form 40 line |
|---|---|
| Federal AGI | Line 7 |
| Alabama additions | Line 8 |
| Alabama subtractions | Line 9 |
| Alabama adjusted gross income | Line 10 |
| Itemized or standard deduction | Line 11 |
| Federal income tax deduction | Line 12 |
| Personal exemption | Line 13 |
| Alabama taxable income | Line 14 |
| Tax from tax table / rate schedule | Line 15 |
| Credits | Lines 16–18 |
| Estimated tax payments | Line 23 |
| Balance due / refund | Lines 27–28 |

---

## Section 9: Refusal catalogue

This skill must refuse and recommend professional review when:

| # | Condition |
|---|---|
| R-01 | Taxpayer has multistate business activity requiring apportionment |
| R-02 | Taxpayer is a part-year resident with complex sourcing questions |
| R-03 | Taxpayer has Alabama net operating loss (NOL) carryforward |
| R-04 | Business Privilege Tax (BPT) applicability for entities beyond sole proprietorship |
| R-05 | Taxpayer questions involve Alabama municipal/city income taxes |
| R-06 | Issues involving Alabama credits (Historic Rehabilitation, Growing Alabama, etc.) |
| R-07 | Audit representation or controversy matters |
| R-08 | Any question about tax fraud, evasion, or aggressive positions |

---

## Disclaimer
This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
