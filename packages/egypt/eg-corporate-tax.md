---
name: eg-corporate-tax
description: Use this skill whenever asked about Egyptian corporate income tax for resident companies, branches of foreign companies, and permanent establishments — to compute, review, or explain CIT liability, deductions, losses, thin capitalisation, and filing requirements. Trigger on phrases like "Egypt corporate tax", "Egypt CIT", "Egyptian company tax", "ضريبة دخل الشركات", "شركة مقيمة مصر", "permanent establishment Egypt", or any request to prepare or check an Egyptian corporate tax return. ALWAYS read this skill before touching any Egypt corporate tax work.
version: 0.1
jurisdiction: EG
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt Corporate Income Tax (ضريبة دخل الشركات) Skill

## Egypt Corporate Income Tax (ضريبة دخل الشركات) Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Jurisdiction is required.** Set `jurisdiction: EG` in frontmatter even when the folder path implies it. Sync to openaccountants.com skips files without a resolvable jurisdiction.

This skill covers Egyptian corporate income tax (ضريبة الدخل على الأشخاص الاعتبارية) for **resident companies** (Egyptian joint-stock, LLCs, partnerships), **branches of foreign companies**, and **permanent establishments** of non-residents. The AI must reply in the user's language (English or Arabic / Egyptian Arabic) and may use the native tax terms shown throughout.

> **Currency note:** all figures are in Egyptian Pounds (EGP / ج.م).
> **YMYL — verify before relying.** Egyptian CIT rates, brackets, and deductions were amended in 2024 and 2025 (Laws 5, 6, 7 of 2025). Where this skill says "verify current value," re-confirm against the Egyptian Tax Authority (ETA — eta.gov.eg), PwC Worldwide Tax Summaries (taxsummaries.pwc.com/egypt), or a Big-4 alert before filing.

## What this file is

**This file is a content skill that loads on top of a workflow base** (here: `income-tax-workflow-base`). It provides Egypt-specific CIT rates, deductions, loss rules, thin-cap rules, and filing mechanics.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

## Section 1 — Scope statement

This skill covers:

- CIT rate and brackets for resident companies and PE of non-residents
- Taxable income determination (accounting profit → taxable profit adjustments)
- Allowable and disallowed deductions (Art 23-26, Law 91/2005)
- Thin capitalisation rules (Art 49) and interest deduction limits
- Loss carryforward rules (Art 27) — 5 years, no carryback
- Withholding tax obligations on outbound payments (dividends, interest, royalties, services)
- Advance tax payments (quarterly) and final return filing (Art 55-57)
- ETA e-filing portal requirements and deadlines

This skill does NOT cover:

- Personal income tax for individuals/sole proprietors — see `eg-income-tax`
- VAT — see `egypt-vat`
- Payroll and social insurance — see `eg-payroll` and `eg-social-insurance`
- SME simplified regime (Law 6/2025) — see `eg-sme-tax`
- Transfer pricing documentation — see `eg-transfer-pricing` (planned)
- Free zone / special economic zone regimes — escalate to licensed advisor
- Petroleum/natural gas concession agreements — specialised regime

## Section 2 — Filing requirements

**Filing requirements**  _(Law 91/2005 Art 1, 6, 10, 55, 56, 110, 111; ETA Decree 2024)_

| Item | Rule | Source |
| --- | --- | --- |
| **Who must file** | All resident companies (Egyptian or foreign-owned), branches of foreign companies, and PEs of non-residents deriving Egypt-source income | Law 91/2005 Art 1, 6 |
| **Tax year** | Calendar year (1 Jan – 31 Dec) — companies may apply for a different fiscal year with ETA approval | Law 91/2005 Art 10 |
| **Return form** | Corporate Income Tax Return (إقرار ضريبة دخل الشركات) via ETA portal | ETA Decree 2024 |
| **Filing deadline** | **30 April** of the year following the tax year (or 4 months after fiscal year-end if non-calendar) | Law 91/2005 Art 55 |
| **Payment deadline** | Same as filing deadline — 30 April | Law 91/2005 Art 55 |
| **Advance payments** | 4 quarterly installments: 20 Apr, 20 Jul, 20 Oct, 20 Jan (each 25% of prior year tax or current year estimate) | Law 91/2005 Art 56 |
| **Late filing penalty** | 2% per month or part thereof of tax due, max 20% | Law 91/2005 Art 110 |
| **Late payment interest** | 1.5% per month or part thereof on unpaid tax | Law 91/2005 Art 111 |

## Section 3 — Rates and thresholds

**Rates and thresholds**  _(Law 91/2005 Art 40, 40 bis, 40 ter, 18 bis, 18 ter; Law 5/2025; Law 6/2025 Art 3)_

| Item | Amount / Rate | Source |
| --- | --- | --- |
| **Standard CIT rate** | **22.5%** | Law 91/2005 Art 40, as amended by Law 5/2025 |
| **Reduced rate — SMEs (turnover ≤ EGP 20m)** | **10%** on first EGP 1m, **20%** on excess — *or* opt into Law 6/2025 turnover regime (see `eg-sme-tax`) | Law 6/2025 Art 3, Law 5/2025 |
| **Reduced rate — listed companies (EGX)** | **20%** (conditional on ≥30% free float, continuous listing) | Law 5/2025 |
| **Petroleum / gas companies** | 40.55% (special concession agreements) | Law 91/2005 Art 40 bis |
| **Suez Canal Authority** | 40.55% | Law 91/2005 Art 40 bis |
| **Branches of foreign banks** | 20% on Egypt-source income | Law 91/2005 Art 40 ter |
| **Dividends received from Egyptian resident company** | **Exempt** (participation exemption — ≥10% holding, ≥1 year) | Law 91/2005 Art 18 bis |
| **Capital gains on listed shares (EGX)** | Exempt if held ≥1 year; otherwise 10% | Law 91/2005 Art 18 ter, Law 5/2025 |

## Section 4 — Computation rules

### Step 1 — Start from accounting profit (net profit per financial statements)

- **Start from accounting profit** — Egyptian GAAP / IFRS net profit before tax → **accounting profit**  _(Section 4 Step 1)_

### Step 2 — Add back disallowed expenses (Art 23-26, Law 91/2005)

**Add back disallowed expenses**  _(Art 23-26, Law 91/2005)_

| Disallowed item | Rule | Source |
| --- | --- | --- |
| **Provisions** (bad debts, obsolescence, warranties, etc.) | Not deductible unless specifically allowed | Art 23(1) |
| **Entertainment / hospitality** | Not deductible | Art 23(2) |
| **Fines, penalties, late fees** (to government or private) | Not deductible | Art 23(3) |
| **Donations** > 5% of taxable income before donations | Excess not deductible | Art 23(4) |
| **Reserves** (general, contingency) | Not deductible | Art 23(5) |
| **Personal expenses** of owners/partners | Not deductible | Art 23(6) |
| **Income tax / CIT paid** | Not deductible | Art 23(7) |
| **Interest expense exceeding thin-cap limit** | See Section 5 | Art 49 |
| **Royalty / technical service fees to related non-resident** without TP documentation | Disallowed | Art 26, TP regulations |
| **Depreciation exceeding tax rates** | Excess not deductible (see tax depreciation below) | Art 24 |

### Step 3 — Allow additional tax deductions

**Allow additional tax deductions**  _(Art 24, 25, 25 bis, 27; ETA Decree 2006; Law 5/2025 Art 12, 13)_

| Item | Rule | Source |
| --- | --- | --- |
| **Tax depreciation** | Straight-line per ETA schedules (buildings 5%, machinery 10-20%, vehicles 20%, computers 33.33%, intangibles 10%) | Art 24, ETA Decree 2006 |
| **Start-up expenses** | Deductible over 5 years (20% per year) | Art 25 |
| **R&D expenditure** | 150% super-deduction (qualifying R&D per ETA criteria) | Law 5/2025 Art 12 |
| **Employee training costs** | 100% deductible (approved programs) | Law 5/2025 Art 13 |
| **Bad debts written off** | Deductible if proven uncollectible, ETA notified | Art 25 bis |
| **Losses carried forward** | Up to 5 years (see Section 6) | Art 27 |

### Step 4 — Apply thin capitalisation limit (Art 49)

- **Debt-to-equity ratio limit** — 4:1 (total interest-bearing debt to equity) ratio  _(Art 49)_
- **Thin capitalisation rules** — - Interest on debt exceeding 4:1 is **non-deductible** - "Equity" = paid-up capital + reserves + retained earnings - treasury shares - Applies to **related-party loans** (direct/indirect ≥25% ownership) and **third-party loans guaranteed by related party** - **Safe harbour**: If actual debt:equity ≤ 4:1, all interest deductible (subject to arm's length rate test)  _(Art 49)_

> **AUDIT FLASH POINT** — Thin cap is a top ETA audit focus. TP documentation (master file + local file) mandatory for related-party loans > EGP 8m.

### Step 5 — Compute taxable income

- **Taxable income** — Taxable income = Accounting profit + Disallowed add-backs - Allowable tax deductions - Losses brought forward (max 5 years)  _(Section 4 Step 5)_

### Step 6 — Apply CIT rate

- **Apply CIT rate** — - Standard: **22.5%** on taxable income - SME reduced brackets: 10% on first EGP 1m, 20% on excess (if eligible and not opted into turnover regime) - Listed: 20% (if conditions met)  _(Section 4 Step 6)_

### Step 7 — Compute advance tax credit

- **Compute advance tax credit** — Credit quarterly advance payments made during the year against final liability.  _(Section 4 Step 7)_

## Section 5 — Edge cases and special rules

### Loss carryforward (Art 27)

- **Loss carryforward** — - **5 years** forward, **no carryback** - Loss must be declared in the return for the loss year - Change of ownership >50% → loss carryforward **forfeited** (anti-avoidance)  _(Art 27)_

### Withholding tax on outbound payments (resident payer → non-resident)

**Withholding tax on outbound payments (resident payer → non-resident)**  _(Law 91/2005 Art 56)_

| Payment type | Rate (non-treaty) | Treaty reduction | Source |
| --- | --- | --- | --- |
| Dividends | **10%** | Often 5% (DTT) | Law 91/2005 Art 56 |
| Interest | **20%** | Often 10% (DTT) | Law 91/2005 Art 56 |
| Royalties | **20%** | Often 10% (DTT) | Law 91/2005 Art 56 |
| Technical / management / consulting fees | **20%** | Often 10-15% (DTT) | Law 91/2005 Art 56 |
| Rental (movable/immovable) | **20%** | Per DTT | Law 91/2005 Art 56 |

> **Key DTT partners**: UAE (5% div/int/roy), Saudi Arabia (5% div, 10% int/roy), UK (5% div, 10% int/roy), USA (5% div, 15% int/roy), Netherlands (0% div ≥10%, 10% int/roy), France (5% div, 10% int/roy).

### Transfer pricing (Arts 49, 49 bis, ETA Decree 2018)

- **Transfer pricing** — - **Arm's length principle** — OECD Guidelines apply - **Documentation threshold**: Related-party transactions > EGP 8m/year → master file + local file - **CbCR**: MNE groups with consolidated revenue ≥ EGP 3bn (≈ EUR 750m) — Country-by-Country Report - **APA program**: Available via ETA (bilateral/multilateral)  _(Arts 49, 49 bis, ETA Decree 2018)_

### Free zones / special economic zones

- **Free zones / special economic zones** — - **New investment** in qualifying free zones: **0% CIT** for 10-20 years (Law 83/2002, Law 173/2018) - Conditions: export ≥80% of production, minimum capital, ETA approval - **Existing mainland companies** moving to free zone — escalate (anti-avoidance rules apply)  _(Law 83/2002, Law 173/2018)_

### Real estate / construction

- **Real estate / construction** — - **Real estate tax** (Law 196/2008) separate from CIT — not deductible for CIT - **Construction contracts** — percentage-of-completion mandatory for CIT (Art 21)  _(Law 196/2008, Art 21)_

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] Accounting profit ties to audited/reviewed financial statements
- [ ] All disallowed add-backs from Section 4 Step 2 captured
- [ ] Tax depreciation uses ETA prescribed rates (not accounting rates)
- [ ] Thin cap debt:equity ratio computed correctly (4:1 limit)
- [ ] Related-party loan interest tested at arm's length rate
- [ ] Loss carryforward ≤ 5 years, no ownership change >50%
- [ ] WHT applied on all outbound payments to non-residents
- [ ] DTT benefits claimed only with valid Tax Residency Certificate
- [ ] Advance payments (4 quarters) credited correctly
- [ ] Filing deadline 30 April (or 4 months post fiscal year-end)
- [ ] ETA e-filing portal used (eta.gov.eg)

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, Egyptian licensed tax accountant — محاسب قانوني, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ahmed Hassan.

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
