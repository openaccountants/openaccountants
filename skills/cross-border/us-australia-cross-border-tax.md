---
name: us-australia-cross-border-tax
description: "Comprehensive guide for US-Australia bilateral cross-border tax coordination for US citizens, green card holders, Australian tax residents, and dual-status individuals. Covers the US-Australia Double Tax Convention (1982, as amended by 2001 Protocol), Australian Superannuation classification under US tax law (Foreign Grantor Trust vs Foreign Employee Trust / IRS Forms 3520, 3520-A, 8938, FBAR, and IRC §402(b)), Foreign Tax Credit (FTC Form 1116) vs Foreign Earned Income Exclusion (FEIE Form 2555) optimization, Medicare Levy Exemption for non-residents in Australia, franking credits treatment under US tax rules, and sourcing of income under Article 22."
jurisdiction: INTL
category: cross-border
tax_year: 2025
tax_year_notes: "2025 (US calendar year) / 2024-25 and 2025-26 (AU fiscal years)"
tier: 2
last_updated: 2026-08-21
version: 1.0
depends_on:
  - cross-border-workflow-base
  - au-individual-return
  - us-feie-ftc
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US-Australia Cross-Border Taxation Guide v1.0

> **General reference only.** This skill is general tax and accounting reference material for AI-assisted workflows. It has not been reviewed for any specific taxpayer's residency status, citizenship, superannuation structure, or filing elections. Do not rely on it without review by a qualified CPA/Enrolled Agent (US) and registered Tax Agent (Australia).

---

## What this file is

This skill covers the complex bilateral tax interactions between the **United States (IRS)** and **Australia (ATO)** for individuals living, working, or investing across both jurisdictions.

---

## Section 1 — Scope Statement

### What this skill covers:
- **US Tax Compliance for Expats in Australia**:
  - Worldwide taxation for US citizens and lawful permanent residents (Green Card holders).
  - Australian Superannuation reporting under US rules (IRS Forms 3520, 3520-A, 8938, FinCEN 114 / FBAR).
  - Foreign Earned Income Exclusion (FEIE / Form 2555) vs Foreign Tax Credit (FTC / Form 1116) selection.
  - Sourcing of cross-border compensation, pensions, dividends, and interest under the Double Tax Convention.
- **Australian Tax Compliance for US Connected Persons**:
  - Tax residency determination under ATO rules (resides test, 183-day test, domicile test).
  - Medicare Levy Exemption certificate mechanics for non-entitled foreign residents.
  - Taxation of US-sourced IRA/401(k) distributions, Social Security, and dividends in Australia.

### What this skill does NOT cover:
- Corporate transfer pricing between US and Australian multinationals.
- Complex state-level US tax conformity for non-resident aliens.

---

## Section 2 — Key Bilateral Treaty Provisions & Rates

### US-Australia Double Tax Convention (1982 / 2001 Protocol)

| Treaty Article | Concept | Rule & Statutory Limits |
|---|---|---|
| **Article 10** | **Dividends** | Standard 15% WHT limit; 5% for 10%+ corporate owners; 0% for 80%+ corporate owners (qualified). |
| **Article 11** | **Interest** | Standard 10% maximum withholding tax rate (0% for financial institutions and government bodies). |
| **Article 12** | **Royalties** | Standard 5% maximum withholding tax rate. |
| **Article 18** | **Pensions & Annuities** | Private pensions and annuities taxed exclusively in the country of residence (subject to US saving clause). |
| **Article 19** | **Social Security** | Government pensions / US Social Security taxed exclusively in the paying country (Article 19(2)). |
| **Article 22** | **Double Tax Relief** | Sourcing rules and credit mechanisms allowing foreign tax credits to eliminate double taxation. |

---

## Section 3 — Australian Superannuation Under US Tax Law

Australian superannuation presents unique US classification and reporting challenges:

### 1. Classification Models
- **Foreign Employee Trust (IRC §402(b))**: Employer mandatory SG contributions and earnings are generally taxable annually to highly compensated employees unless exempt; no Form 3520/3520-A required.
- **Foreign Grantor Trust (IRC §§671–679)**: Voluntary / personal contributions make the employee the owner of that portion of the trust, triggering annual **Form 3520** and **Form 3520-A** informational returns.
- **Self-Managed Superannuation Funds (SMSF)**: Treated as foreign grantor trusts, requiring comprehensive 3520/3520-A filing and potential PFIC reporting (Form 8621) for underlying assets.

### 2. Information Reporting Thresholds
- **FinCEN 114 (FBAR)**: Mandatory if aggregate foreign financial accounts (including superannuation balances) exceed **$10,000** at any time during the calendar year.
- **Form 8938 (FATCA)**: Required for expats filing Single/MFS if foreign financial assets exceed **$200,000** at year-end or **$300,000** at any time ($400,000 / $600,000 for MFJ).

---

## Section 4 — Step-by-Step Optimization Workflow

### Step 1 — Tax Year Synchronization
1. Map US calendar year (1 Jan – 31 Dec) against Australian fiscal years (1 Jul – 30 Jun).
2. Split or apportion Australian PAYG withholding summaries and tax liabilities to match the US tax year for Form 1116 accrual calculations.

### Step 2 — FEIE vs FTC Decision
- **High Tax Environment Rule**: Because Australian marginal tax rates (up to 45% + 2% Medicare levy) generally exceed US federal rates, **Foreign Tax Credits (Form 1116)** are typically superior to FEIE (Form 2555).
- Benefits of FTC:
  - Generates excess foreign tax credit carryovers (1 year back, 10 years forward).
  - Preserves eligibility for the US Child Tax Credit (refundable portion) and IRA contributions.

### Step 3 — Australian Medicare Levy Exemption
1. Apply for a **Medicare Entitlement Statement (MES)** from Services Australia confirming the US citizen is not eligible for Medicare.
2. Claim the full exemption on Item M1 of the Australian Individual Tax Return to save the **2.0% Medicare Levy**.

---

## Section 5 — Audit Flash Points

> **AUDIT FLASH POINT 1 — Australian Franking Credits are NOT US Creditable Taxes.** Franking credits (*imputation credits*) represent Australian corporate tax paid by the company, not tax paid directly by the shareholder. They cannot be claimed on US Form 1116, but gross dividends including franking credits may be treated as foreign taxable income.

> **AUDIT FLASH POINT 2 — Penalties for Delinquent Forms 3520 / 3520-A.** Automatic $10,000 or 5% penalties apply for late-filed foreign trust returns under IRC §6677. Ensure streamlined foreign offshore procedures (SFOP) or reasonable cause statements are evaluated if past filings were omitted.

---

## Section 6 — Self-Checks

- [ ] Superannuation balances are included in FinCEN Form 114 (FBAR) and Form 8938.
- [ ] Australian income and foreign taxes paid are converted using official IRS annual exchange rates.
- [ ] Medicare Entitlement Statement (MES) is on file before claiming Australian Medicare levy exemption.
- [ ] FTC carryover schedules are updated and tracked for 10-year expiration windows.

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, or registered Australian Tax Agent) before filing.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
