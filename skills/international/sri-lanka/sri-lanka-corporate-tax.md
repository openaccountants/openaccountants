---
name: sri-lanka-corporate-tax
description: "ALWAYS read this skill before touching any Sri Lanka corporate income tax work. Use whenever asked about Sri Lanka company tax for a resident company. Trigger on phrases like \"Sri Lanka corporate tax\", \"Sri Lanka CIT\", \"company tax Sri Lanka\", \"30% corporate rate Sri Lanka\", \"betting and gaming tax Sri Lanka\", \"liquor tobacco tax Sri Lanka\", \"Inland Revenue Act 24 of 2017 company\", or \"year of assessment 2025/26 company\". Covers the Inland Revenue Act No. 24 of 2017 as amended by the Inland Revenue (Amendment) Act No. 02 of 2025 (effective 1 April 2025): the 30% standard rate, the 15% concessionary rate on remitted foreign-currency income/services, and the 45% rate on betting/gaming and liquor/tobacco. Out of scope — personal income tax (separate skill), withholding/AIT (separate skill), SSCL, VAT, banking/insurance/sector special regimes, and group/transfer-pricing matters."
jurisdiction: LK
domain: international
tax_year: 2025
reviewed_by: Lal kumarasiri
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# sri-lanka-corporate-tax

## Sri Lanka — Corporate Income Tax — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com).** Research-grade (tier 2), drafted from official IRD sources for YA 2025/26 — pending sign-off by a Sri Lankan CA / IRD-registered practitioner. Not tax advice.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Sri Lanka |
| Tax | Corporate income tax |
| Currency | LKR |
| Year of assessment | 1 April – 31 March (YA 2025/26) |
| Primary legislation | Inland Revenue Act No. 24 of 2017, as amended by Act No. 02 of 2025 (eff. 1 April 2025) |
| Authority | Inland Revenue Department (IRD) |
| **Standard rate** | **30%** of taxable income (since 1 April 2023) |
| **Concessionary rate** | **15%** on qualifying foreign-currency-source income and services remitted to Sri Lanka through a bank |
| **Higher rate** | **45%** on betting & gaming, and on manufacture/sale or import/sale of any liquor or tobacco product (raised from 40% eff. 1 April 2025) |
| Export of liquor/tobacco | Taxed at the **30%** normal rate (not 45%) |
| Capital gains (investment assets) | 10% (separate from business income) |
| Statement of Estimated Tax (SET) | Filed under s.91; YA 2025/26 due 15 August 2025 |
| Validated by | Pending — Sri Lankan CA / IRD-registered practitioner |
| Skill version | 1.0 |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Sector/rate unclear | Apply 30% standard |
| Forex-remittance concession (15%) claimed | Apply 30% until remittance-through-a-bank evidence confirmed |
| Betting/gaming or liquor/tobacco activity | Apply 45% (flat) unless it is export (then 30%) |
| SME / sector concession asserted | Do NOT apply — not confirmed in this skill; VERIFY against current IRA/IRD |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — audited or draft financial statements (P&L, balance sheet), prior-year return, taxable-income computation, confirmation of (i) sector (standard / betting-gaming / liquor-tobacco / export), (ii) any foreign-currency-remitted income claiming the 15% rate, (iii) WHT/AIT credits.

### Refusal catalogue

- **R-LK-CT-1** — Banking, insurance, and sector special regimes. These carry separate computation rules. Out of scope — escalate.
- **R-LK-CT-2** — SME / concessionary sector rates not in this skill. Any SME or sector-specific concessionary rate must be VERIFIED against the current IRA and IRD guidance — this skill asserts only the 30% standard, 15% remitted-forex, and 45% betting/liquor/tobacco rates.
- **R-LK-CT-3** — Group taxation, transfer pricing, reorganisations. Out of scope — escalate.
- **R-LK-CT-4** — Cross-skill scope. Personal tax → `sri-lanka-income-tax`; WHT/AIT → `sri-lanka-withholding-tax`; SSCL → `sri-lanka-sscl`; VAT → `sri-lanka-vat`.

## Section 3 — Tier 1 rates

### 3.1 Standard rate — 30%

- **Standard corporate income tax rate** — 30% percent (of taxable income, in force since 1 April 2023 (it was 24% from 1 January 2020, and 28% before that). Apply to taxable income computed under the Inland Revenue Act No. 24 of 2017.)  _(Inland Revenue Act No. 24 of 2017)_
- **Standard CIT formula** — Standard CIT = 30% × Taxable income  _(Inland Revenue Act No. 24 of 2017)_

### 3.2 Concessionary rate — 15% (remitted foreign currency)

- **Concessionary rate on remitted foreign-currency income/services** — 15% percent (applies to qualifying foreign-currency-source income and services remitted to Sri Lanka through a bank. Require evidence of the foreign-currency source and the banking-channel remittance before applying.)

### 3.3 Higher rate — 45% (betting/gaming, liquor, tobacco)

- **Higher rate on betting/gaming and liquor/tobacco** — 45% percent (applies to income from a business consisting of: betting and gaming; or manufacture and sale, or import and sale, of any liquor or tobacco product. Raised from 40% effective 1 April 2025 (Act No. 02 of 2025). The same 45% flat rate applies to individuals carrying on such business income.)  _(Act No. 02 of 2025)_
- **Export of liquor/tobacco products** — 30% percent (The export of liquor or tobacco products is taxed at the 30% normal rate, not 45%.)

## Section 4 — Tier 2

- **Capital gains.** Gains on the realisation of investment assets are taxed at a flat **10%** (resident and non-resident). Company-specific characterisation (business asset vs investment asset) — VERIFY with the practitioner.
- **Losses, depreciation, allowances.** Computed under the IRA (Second/Fourth Schedules) — detailed loss carry-forward and capital-allowance rules are NOT asserted here; VERIFY against the IRA.
- **SSCL interaction.** SSCL (2.5% on liable turnover) is a separate levy — see `sri-lanka-sscl`.

- **Capital gains on realisation of investment assets** — 10% percent (flat rate for resident and non-resident; separate from business income. Company-specific characterisation (business asset vs investment asset) — VERIFY with the practitioner.)

## Section 5 — Worked examples

### 5.1 Standard company

Taxable income LKR 50,000,000 → CIT = 30% × 50,000,000 = **LKR 15,000,000**.

### 5.2 Liquor manufacturer (domestic)

Taxable income LKR 50,000,000 from domestic liquor manufacture/sale → CIT = 45% × 50,000,000 = **LKR 22,500,000**. (If the same income were from **export** of the product, the rate would be 30%.)

### 5.3 IT services exporter, forex remitted through a bank

Qualifying remitted foreign-currency services income LKR 50,000,000 → CIT = 15% × 50,000,000 = **LKR 7,500,000**, provided the banking-channel remittance is evidenced.

## Section 6 — Filing

- **Year of assessment:** 1 April – 31 March.
- **Statement of Estimated Tax Payable (SET):** under IRA s.91; YA 2025/26 due **15 August 2025**.
- **Annual return + payment / quarterly instalment dates:** VERIFY against the current IRD calendar (not asserted here).

- **Statement of Estimated Tax Payable (SET) due date** — 15 August 2025 (YA 2025/26, filed under IRA s.91)  _(IRA s.91)_

## Section 7 — Conservative defaults

**Conservative defaults table**

| Item | Default |
| --- | --- |
| Rate uncertain | 30% standard |
| 15% forex concession | Apply only with banking-remittance evidence |
| Betting/gaming/liquor/tobacco | 45% (flat) unless export (30%) |
| SME / other concession | Not applied — VERIFY |
| Any figure flagged VERIFY | Flag for reviewer; do not finalise |

## Section 8 — Sources

1. IRD YA 2025/26 tax chart — https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx
2. IRD Notice PN/IT/2025-01 (26.03.2025) — https://www.ird.gov.lk/en/Lists/Latest%20News%20%20Notices/Attachments/666/PN_IT_2025-01_26032025_E.pdf
3. Consolidated Inland Revenue Act No. 24 of 2017 (to 2025 changes) — https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf

**Known gaps / VERIFY:** SME / sector concessionary rates; loss carry-forward and capital-allowance detail; company capital-gains characterisation; annual-return and instalment dates.

## Prohibitions

- NEVER apply the 24% or 28% historical rate to YA 2025/26 — the standard rate is 30%.
- NEVER apply the 15% concession without banking-channel forex-remittance evidence.
- NEVER use the old 40% rate for betting/gaming/liquor/tobacco for periods from 1 April 2025 — it is 45%.
- NEVER assert an SME/sector concession this skill flags as VERIFY.
- NEVER file or instruct filing — produce a working paper for practitioner review.

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Sri Lankan professional (CA / IRD-registered tax practitioner) before filing or acting upon. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. To speak with one of the licensed accountants who verifies skills for your jurisdiction — **no liability until both parties sign an engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**
