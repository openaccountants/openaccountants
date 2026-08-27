---
name: ma-income-tax
description: Use this skill whenever asked about Massachusetts individual income tax. Trigger on phrases like "Massachusetts income tax", "MA income tax", "Form 1", "Mass DOR", "M.G.L. c. 62", "millionaire's tax", "MA surtax". Massachusetts has a flat 5% rate plus a 4% surtax on income over ~$1M (inflation-adjusted). ALWAYS load us-tax-workflow-base first.
version: "0.1"
jurisdiction: US-MA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Income Tax

## Massachusetts Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Massachusetts Form 1 (Resident Income Tax Return) for sole proprietors and single-member LLCs. It addresses the flat 5% income tax, the 4% millionaire's surtax, and Massachusetts-specific income classifications. It does NOT cover nonresident/part-year returns (Form 1-NR/PY), corporate excise (Form 355), or trust/estate returns (Form 2).

> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Section 1: Metadata

**Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Massachusetts (US-MA) |
| Tax authority | [Massachusetts Department of Revenue (DOR)](https://www.mass.gov/orgs/massachusetts-department-of-revenue) |
| Filing portal | [MassTaxConnect](https://mtc.dor.state.ma.us/) |
| Legislation | M.G.L. Chapter 62 — Taxation of Incomes |
| Primary form | Form 1 (Massachusetts Resident Income Tax Return) |
| Filing deadline | April 15, 2027 (for tax year 2026) |
| Version | 0.1 |
| Date | May 22, 2026 |
| Validation status | AI-drafted — Q3 |

### Sources consulted

1. Massachusetts DOR — Tax Rates: <https://www.mass.gov/service-details/tax-rates>
2. Massachusetts DOR — Personal Income Tax for Residents: <https://www.mass.gov/guides/personal-income-tax-for-residents>
3. Massachusetts DOR — 4% Surtax on Taxable Income: <https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000>
4. M.G.L. c. 62, §§ 4, 5, 5A
5. Article 44 of the Massachusetts Constitution (as amended by 2022 ballot question — "Fair Share Amendment")

## Section 2: Quick reference — rates and thresholds

### Income tax rates

**Income tax rates**

| Income type | Rate | Source |
| --- | --- | --- |
| Part A income (interest, dividends, capital gains from non-MA obligations) | 5.00% | M.G.L. c. 62, § 4(a) |
| Part B income (wages, salaries, self-employment, most other income) | 5.00% | M.G.L. c. 62, § 4(b) |
| Part C income (short-term capital gains) | 8.50% (subject to 50% deduction, effective rate ~12%) | M.G.L. c. 62, § 4(c) |
| Long-term capital gains | 5.00% | M.G.L. c. 62, § 4(b) |

### Millionaire's surtax (4% additional tax)

**Millionaire's surtax thresholds**

| Tax year | Surtax threshold | Source |
| --- | --- | --- |
| 2023 | $1,000,000 | Article 44 |
| 2024 | $1,053,750 | Inflation-adjusted |
| 2025 | $1,083,150 | Inflation-adjusted |
| 2026 | TBD (inflation-adjusted, typically announced late in preceding year) | M.G.L. c. 62, § 5A |

- **Surtax application** — The 4% surtax applies only to the portion of taxable income exceeding the threshold. For a taxpayer with $1,100,000 in TY2025 taxable income, the surtax applies to $16,850 ($1,100,000 − $1,083,150).  _(M.G.L. c. 62, § 5A)_

### Deductions and exemptions

Massachusetts does **not** use a standard deduction in the federal sense. Instead, it provides:

**Deductions and exemptions table**

| Item | Amount (TY2025) | Source |
| --- | --- | --- |
| Personal exemption — Single | $4,400 | M.G.L. c. 62, § 3(B)(a) |
| Personal exemption — Head of Household | $6,800 | M.G.L. c. 62, § 3(B)(b)(2) |
| Personal exemption — MFJ | $8,800 | M.G.L. c. 62, § 3(B)(b)(1) |
| Dependent deduction | $1,000 per dependent | M.G.L. c. 62, § 3(B)(a)(3) |
| Rental deduction | 50% of rent paid, max $3,000 | M.G.L. c. 62, § 3(B)(a)(9) |

### Filing threshold

- **Filing threshold** — $8,000 of Massachusetts gross income USD (Everyone whose Massachusetts gross income is $8,000 or more must file.)

## Section 3: How this skill works with the federal return

### Starting point

- **Income classification system** — Massachusetts uses its own income classification system rather than starting directly from federal AGI. However, the computation references federal Form 1040 amounts extensively. Massachusetts income is divided into three parts: - **Part A:** Interest, dividends, and net capital gains on non-Massachusetts obligations - **Part B:** Wages, salaries, self-employment income, pensions, annuities, and most other income - **Part C:** Short-term capital gains and gains on collectibles

### Key differences from federal

**Key differences from federal table**

| Item | Massachusetts treatment | Source |
| --- | --- | --- |
| No standard deduction | MA uses personal exemptions and specific deductions instead | M.G.L. c. 62, § 3 |
| Social Security | Fully exempt | M.G.L. c. 62, § 2(a)(2)(E) |
| Interest from MA obligations | Exempt | M.G.L. c. 62, § 2 |
| Interest from other states | Taxable (add back any federal exclusions) | M.G.L. c. 62, § 2 |
| Short-term capital gains | Taxed at 8.50% (not the standard 5%) | M.G.L. c. 62, § 4(c) |

### Resulting computation

- **Computation order** — Compute Part A, Part B, and Part C income separately → subtract applicable deductions and exemptions → apply the appropriate rate to each part → sum = Massachusetts gross tax → minus credits → plus 4% surtax if applicable.

## Section 4: Self-employed specific rules

### Estimated tax payments

- **Estimated tax payment obligation** — Self-employed individuals must make quarterly estimated tax payments if they expect to owe $400 or more.

**Estimated tax payment due dates**

| Voucher | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

Use Form 1-ES for estimated payments.

### Self-employment health insurance

- **Self-employment health insurance** — Massachusetts generally follows federal treatment — the deduction is taken as a Part B deduction.

### Retirement contributions (SEP, SIMPLE, Solo 401(k))

- **Retirement contributions** — Massachusetts generally follows federal treatment — these deductions reduce Part B income.

### Home office deduction

- **Home office deduction** — Massachusetts follows the federal home office deduction as part of Schedule C.

### QBI deduction (Section 199A)

- **QBI deduction disallowed** — Massachusetts does not allow the federal QBI deduction. Massachusetts has its own income computation that does not incorporate the QBI deduction.

### Health insurance mandate

- **Health insurance mandate** — Massachusetts has an individual health insurance mandate (separate from the ACA). Failure to maintain minimum creditable coverage may result in a penalty assessed on Form 1 (Schedule HC). This is relevant for self-employed individuals who must obtain their own coverage.

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule | Description |
| --- | --- |
| R-1 | Apply 5% to Part A and Part B income. Apply 8.50% to Part C (short-term capital gains). |
| R-2 | Apply the 4% surtax on total taxable income exceeding the inflation-adjusted threshold ($1,083,150 for TY2025). |
| R-3 | Social Security is fully exempt. |
| R-4 | Interest from U.S. obligations is exempt. |
| R-5 | Interest from Massachusetts municipal bonds is exempt; interest from other states' bonds is taxable. |
| R-6 | Massachusetts does NOT have a standard deduction — use the personal exemption system. |
| R-7 | Long-term capital gains are taxed at 5%, NOT the short-term rate. |
| R-8 | Massachusetts has NO local/county income taxes. Only the state tax applies. |
| R-9 | Filing threshold: $8,000 of MA gross income. |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule | Description |
| --- | --- |
| J-1 | Classify income correctly among Part A, Part B, and Part C — misclassification changes the rate. |
| J-2 | Determine whether the taxpayer's total income approaches the surtax threshold and whether income timing strategies are appropriate. |
| J-3 | Evaluate Massachusetts deductions vs. federal deductions (they differ significantly). |
| J-4 | Assess the health insurance mandate penalty when the taxpayer had gaps in coverage (Schedule HC). |
| J-5 | Determine credit for taxes paid to other states for multi-state income. |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern | Massachusetts treatment |
| --- | --- |
| Freelance income (Schedule C) | Part B income. Taxed at 5%. |
| Rental income (Schedule E) | Part B income. Taxed at 5%. |
| Short-term capital gains | Part C income. Taxed at 8.50%. |
| Long-term capital gains | Part B income. Taxed at 5%. |
| Interest / dividends | Part A income. Taxed at 5%. MA and U.S. obligations exempt. |
| Social Security | Fully exempt. |
| Pension / retirement | Part B income. Taxed at 5%. |

## Section 8: Form mapping

**Form 1 line mapping table**

| Form 1 line | Description | Source |
| --- | --- | --- |
| Lines 1–4 | Part A income (interest, dividends) | M.G.L. c. 62, § 2 |
| Lines 5–10 | Part A deductions and exemptions | M.G.L. c. 62, § 3 |
| Line 10 | Part A taxable income | Computed |
| Lines 11–14 | Part B income (wages, self-employment, pensions) | M.G.L. c. 62, § 2 |
| Lines 15–20 | Part B deductions and exemptions | M.G.L. c. 62, § 3 |
| Line 20 | Part B taxable income | Computed |
| Line 21 | Part C income (short-term capital gains) | M.G.L. c. 62, § 2 |
| Line 23 | Total 5% income tax (Part A + Part B at 5%) | Computed |
| Line 24 | 8.50% tax on Part C | Computed |
| Line 25 | Total income tax before credits | Sum |
| Line 28 | Credits | Various |
| Line 29 | 4% surtax (if applicable) | M.G.L. c. 62, § 5A |
| Lines 34–39 | Payments, withholding, estimated payments | Various |
| Line 43 | Balance due or refund | Computed |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Code | Situation | Action |
| --- | --- | --- |
| REF-MA-01 | Taxpayer is a nonresident or part-year resident | Refuse; requires Form 1-NR/PY. |
| REF-MA-02 | Taxpayer has complex Part A / Part B / Part C classification issues | Flag for reviewer. |
| REF-MA-03 | Taxpayer's income exceeds the surtax threshold and involves timing strategies | Flag for reviewer — surtax cliff analysis needed. |
| REF-MA-04 | Taxpayer claims complex credits (e.g., Brownfields, Life Sciences, Film) | Flag for reviewer. |
| REF-MA-05 | Taxpayer has Schedule HC penalty issues (gaps in health insurance coverage) | Flag for reviewer — penalty computation is complex. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
