---
name: uk-australia-cross-border-tax
description: "Comprehensive guide for UK-Australia bilateral cross-border taxation for individuals, expats, and dual residents. Covers the UK-Australia Double Taxation Convention (2003), Qualifying Recognised Overseas Pension Schemes (QROPS) transfers and the 25% Overseas Transfer Charge (OTC) under UK Finance Act rules, UK Statutory Residence Test (SRT) split-year treatment vs Australian tax residency (resides and 183-day tests), UK Non-Resident Capital Gains Tax (NRCGT) on UK real estate, Australian Capital Gains Tax (CGT) Main Residence Exemption rules for non-residents, and double taxation relief mechanisms under Article 22."
jurisdiction: INTL
category: cross-border
tax_year: 2025
tax_year_notes: "2025-26 (UK fiscal year 6 Apr - 5 Apr) / 2024-25 and 2025-26 (AU fiscal years 1 Jul - 30 Jun)"
tier: 2
last_updated: 2026-08-21
version: 1.0
depends_on:
  - cross-border-workflow-base
  - au-individual-return
  - uk-income-tax-sa100
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK-Australia Cross-Border Taxation Guide v1.0

> **General reference only.** This skill is general tax and accounting reference material for AI-assisted workflows. It has not been reviewed for any specific taxpayer's residency status, domicile, pension transfer path, or property holdings. Do not rely on it without review by a CTA/chartered accountant (UK) and registered Tax Agent (Australia).

---

## What this file is

This skill covers the bilateral tax interactions between the **United Kingdom (HMRC)** and **Australia (ATO)** for individuals relocating, working remotely, owning property, or transferring retirement funds between both nations.

---

## Section 1 — Scope Statement

### What this skill covers:
- **UK-Australia Double Taxation Convention (2003)** provisions and maximum withholding rates.
- **Pension Transfers (QROPS)**: Moving UK defined contribution / defined benefit pensions to Australian superannuation funds, QROPS registration conditions, and avoidance of the 25% Overseas Transfer Charge (OTC).
- **Tax Residency Coordination**:
  - UK Statutory Residence Test (SRT), split-year treatment (Cases 1–8).
  - Australian tax residency tests (Resides, Domicile, 183-Day, Superannuation).
  - Treaty tie-breaker rules under Article 4.
- **Cross-Border Capital Gains**:
  - UK Non-Resident CGT (NRCGT) on UK residential/commercial property.
  - Australian CGT market value cost base uplift upon tax entry into Australia (ITAA 1997 s 855-45).
  - Australian CGT deemed disposal upon tax departure (s 104-160).

### What this skill does NOT cover:
- Corporate transfer pricing and diverted profits tax (DPT).
- UK Inheritance Tax (IHT) planning for non-domiciled individuals following UK non-dom regime abolition.

---

## Section 2 — Key Bilateral Treaty Provisions & Rates

### UK-Australia Double Taxation Convention (2003)

| Treaty Article | Concept | Rule & Statutory Ceiling |
|---|---|---|
| **Article 10** | **Dividends** | Maximum 15% withholding rate; 0% or 5% for corporate shareholders. (Note: UK does not levy domestic dividend WHT; AU franked dividends are 0% WHT). |
| **Article 11** | **Interest** | Standard 10% maximum withholding tax rate (0% for financial institutions / government). |
| **Article 12** | **Royalties** | Standard 5% maximum withholding tax rate. |
| **Article 17** | **Pensions** | Private pensions and annuities are taxable exclusively in the individual's country of tax residence. |
| **Article 18** | **Government Service** | Government pensions and remuneration are generally taxable only in the paying state. |
| **Article 22** | **Elimination of Double Taxation** | Provides foreign tax credit relief in both jurisdictions for doubly taxed income. |

---

## Section 3 — UK Pension Transfers to Australia (QROPS)

Transferring a UK registered pension scheme to an Australian super fund requires adherence to strict HMRC and ATO rules:

### 1. Requirements for QROPS Transfer
- The Australian superannuation fund must be an HMRC-notified **QROPS**. Under current UK regulations, Australian retail/industry super funds generally do not qualify due to the condition of release for severe financial hardship under age 55; transfers typically require a **Self-Managed Super Fund (SMSF)** whose trust deed restricts access strictly to members aged **55 and over**.
- Transfer is subject to the **Australian Non-Concessional Contributions (NCC) Cap** ($120,000/year or up to $360,000 using the 3-year bring-forward rule).

### 2. Overseas Transfer Charge (OTC)
- A **25% Overseas Transfer Charge** applies under UK Finance Act 2004 s 244A unless an exemption applies:
  - Exemption: The member is an Australian tax resident at the time of the transfer and the receiving QROPS is established in Australia.
  - If the member changes tax residency to another country within 5 full UK tax years of the transfer, the 25% OTC is clawed back.

### 3. Australian Applicable Fund Earnings (AFE)
- Under **ITAA 1997 s 305-70**, growth in the UK pension value between the date the individual became an Australian tax resident and the transfer date (*Applicable Fund Earnings*) is taxable in Australia at marginal tax rates (or elective 15% super fund rate if transferred directly into the fund).

---

## Section 4 — Step-by-Step Residency Coordination Workflow

### Step 1 — Tax Year Alignment
- **UK Tax Year**: 6 April to 5 April.
- **Australian Tax Year**: 1 July to 30 June.
- Cross-border filings require time-apportioning UK payslips (P60/P45) to Australian fiscal years and vice versa.

### Step 2 — Statutory Residence Test (SRT) & Split-Year Evaluation
1. Determine if the departing UK taxpayer qualifies for split-year treatment (e.g. Case 1: Starting full-time work abroad, or Case 3: Ceasing UK home).
2. Establish exact UK overseas part and UK resident part dates.

### Step 3 — Australian Cost Base Reset
1. Upon becoming an Australian tax resident, establish market value valuations for all worldwide assets (excluding taxable Australian property) under **s 855-45 ITAA 1997**.
2. This establishes the new Australian CGT cost base and eliminates tax on gains accrued prior to Australian residency.

---

## Section 5 — Audit Flash Points

> **AUDIT FLASH POINT 1 — Loss of Australian CGT Main Residence Exemption for Foreign Residents.** Australian law denies the CGT Main Residence Exemption to non-residents who sell Australian residential property while living in the UK, unless they satisfy the strict 6-year "life events" test.

> **AUDIT FLASH POINT 2 — Australian 6-Month Pension Transfer Window.** Transferring a UK pension within **6 months** of becoming an Australian tax resident eliminates the Australian tax on Applicable Fund Earnings (AFE) entirely, as fund earnings during that 6-month window are treated as zero under s 305-75(2).

---

## Section 6 — Self-Checks

- [ ] QROPS SMSF trust deed contains the strict age-55 restriction rule to prevent HMRC disqualification.
- [ ] Transfer amount is within the Australian non-concessional contributions (NCC) cap limits.
- [ ] Market valuations are documented at the exact date of residency transition for CGT cost base rebasing.
- [ ] Foreign tax credit claims on UK SA100 and Australian Tax Returns cite Article 22 of the 2003 Convention.

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified UK Chartered Tax Adviser / Accountant and a registered Australian Tax Agent before filing.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
