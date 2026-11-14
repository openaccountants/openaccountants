---
name: za-capital-gains-tables
description: >
  Year-keyed South African capital gains tax tables for natural persons, for the years of assessment 2023 to 2027, with the current year being the 2027 year of assessment (1 March 2026 to 28 February 2027, written 2026/27). Holds the annual exclusion, the exclusion in the year of death, the primary residence exclusion, the small business asset exclusion and its market value limit, the maximum effective CGT rates by type of taxpayer, and the tax-free investment annual and lifetime limits with the 40% charge on excess contributions, each row linked to the SARS page it was read on. Use for any South African CGT exclusion or effective rate lookup, primary residence disposal, deceased estate, small business disposal at 55 or older, or tax-free savings account limit question, current or prior year.
version: 1.0
jurisdiction: ZA
tax_year: 2026
tax_year_notes: "2026-27, the 2027 year of assessment (1 March 2026 to 28 February 2027); prior years 2023 to 2026 kept for disposals in those years"
last_updated: 2026-11-14
depends_on:
  - workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: rates-card
---

# South Africa: capital gains tax tables for natural persons, years of assessment 2023 to 2027

Year-keyed CGT exclusions and effective rates for **natural persons and special trusts**, plus the tax-free investment limits. Data only: this file does not compute a gain and does not set out base cost rules (see `za-capital-gains`). An accountant-approved file with the same job exists: `capital-gains-tax-rate-tables-2023-to-2027`. Where the two ever differ, the SARS page linked on the row decides.

**Current year:** the 2027 year of assessment, 1 March 2026 to 28 February 2027 (commonly written 2026/27).

## How South African years of assessment are labelled

SARS numbers a year of assessment by the calendar year in which it **ends**; the tax year runs 1 March to the last day of February. The year ending 28 February 2027 is **YoA 2027**, commonly written "2026/27". Getting this wrong by one year is the most common error in South African rate lookups.

| Year of assessment | Commonly written | Period |
| --- | --- | --- |
| 2023 | 2022/23 | 1 March 2022 to 28 February 2023 |
| 2024 | 2023/24 | 1 March 2023 to 29 February 2024 |
| 2025 | 2024/25 | 1 March 2024 to 28 February 2025 |
| 2026 | 2025/26 | 1 March 2025 to 28 February 2026 |
| 2027 | 2026/27 | 1 March 2026 to 28 February 2027 |

## Scope

For each year of assessment 2023 to 2027: the annual exclusion (Eighth Schedule para 5(1)); the exclusion in the year of death (para 5(2)); the primary residence exclusion (para 45); the small business asset exclusion for individuals aged 55 or older (para 57); the maximum effective CGT rates; the tax-free investment limits (s 12T).

Not covered: base cost; roll-overs; the inclusion rate computation for companies and trusts beyond the effective rate; any computation rule.

## Rates, bands and thresholds

### Exclusions for natural persons

| YoA | Annual exclusion | Exclusion in the year of death (replaces the annual exclusion) | Primary residence exclusion (gain or loss) | Source |
| --- | --- | --- | --- | --- |
| 2027 (2026/27) | R50,000 | R440,000 | R3,000,000 | https://www.sars.gov.za/tax-rates/income-tax/capital-gains-tax-cgt/ |
| 2026 (2025/26) | R40,000 | R300,000 | R2,000,000 | https://www.sars.gov.za/budget-tax-guide-21-may-2025/ |
| 2025 (2024/25) | R40,000 | R300,000 | R2,000,000 | https://www.sars.gov.za/wp-content/uploads/Budget-tax-guide-2024-_.pdf |
| 2024 (2023/24) | R40,000 | R300,000 | R2,000,000 | https://www.sars.gov.za/budget-2023-tax-guide/ |
| 2023 (2022/23) | R40,000 | R300,000 | R2,000,000 | https://www.sars.gov.za/budget-tax-guide-2022/ |

### Small business asset exclusion (individuals at least 55 years old)

| YoA | Exclusion of capital gains | Market value limit of the small business | Source |
| --- | --- | --- | --- |
| 2027 (2026/27) | R2,700,000 | R15,000,000 | https://www.sars.gov.za/tax-rates/income-tax/capital-gains-tax-cgt/ |
| 2026 (2025/26) | R1,800,000 | R10,000,000 | https://www.sars.gov.za/budget-tax-guide-21-may-2025/ |
| 2025 (2024/25) | R1,800,000 | R10,000,000 | https://www.sars.gov.za/wp-content/uploads/Budget-tax-guide-2024-_.pdf |
| 2024 (2023/24) | R1,800,000 | R10,000,000 | https://www.sars.gov.za/budget-2023-tax-guide/ |
| 2023 (2022/23) | R1,800,000 | R10,000,000 | https://www.sars.gov.za/budget-tax-guide-2022/ |

### Maximum effective CGT rates

| Type of taxpayer | 2027 | 2026 | 2025 | 2024 | 2023 | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Individuals and special trusts | 18% | 18% | 18% | 18% | 18% | https://www.sars.gov.za/tax-rates/income-tax/capital-gains-tax-cgt/ |
| Companies | 21.6% | 21.6% | 21.6% | 21.6% | 21.6% | same |
| Other trusts | 36% | 36% | 36% | 36% | 36% | same |

The 18% for individuals is the 40% inclusion rate (para 10) applied to the 45% top marginal rate. SARS publishes the effective rate on this page, not the inclusion rate.

### Tax-free investments (s 12T)

| YoA | Annual contribution limit | Lifetime contribution limit | Charge on excess (normal tax) | Source |
| --- | --- | --- | --- | --- |
| 2027 (2026/27) | R46,000 | R500,000 | 40% of the excess | https://www.sars.gov.za/types-of-tax/personal-income-tax/tax-free-investments/ |
| 2021 to 2026 (2020/21 to 2025/26) | R36,000 | R500,000 | 40% of the excess | same |

Amounts received in or accrued on a tax-free investment are exempt from income tax, dividends tax and CGT.

### Edge cases and traps

- **The YoA 2027 increases are easy to miss.** The annual exclusion, the death exclusion, the primary residence exclusion and the small business exclusion all rose from 1 March 2026. A skill quoting the prior figures for YoA 2027 is wrong, and the error is most dangerous inside a home-office warning, where the old annual exclusion understates the relief on a tainted portion.
- **The primary residence exclusion applies to the first part of the GAIN**, not of the proceeds.
- **Home-office tainting.** Where part of a residence is used for trade, the primary residence exclusion does not reach the trade portion, which falls back on the annual exclusion only. Use the annual exclusion **for the year of disposal**.
- **The lifetime tax-free limit has not moved** while the annual limit has. Do not infer one from the other.
- **The death exclusion replaces the annual exclusion** in the year of death; the two are not added.
- **A short year of assessment.** TLAA 5 of 2026 amended the para 5(1) proviso: where a year of assessment is shorter than 12 months, the annual exclusions for years ending in one 1 March to end-February period must not exceed R40,000 in aggregate (the Act's own figure; how it sits with the R50,000 annual exclusion for 2027 is listed under Not yet confirmed).

### Self-checks

1. **Year of disposal.** The exclusion is the one for the year of assessment in which the disposal happened, not the year the return is filed.
2. **Death exclusion is larger than the annual exclusion** in every year. If not, the two are transposed.
3. **The effective rates are maxima**, reached only at the top marginal rate for individuals.

### Worked example: home sold in YoA 2027 with a home-office portion

A natural person sells a primary residence in October 2026 for a capital gain of R3,400,000. 10% of the house was used for trade for the whole holding period, so R340,000 of the gain is the trade portion and R3,060,000 the residence portion.

- Residence portion R3,060,000 less the primary residence exclusion R3,000,000 leaves R60,000.
- Add the trade portion R340,000: R400,000.
- Less the 2027 annual exclusion R50,000 (no other disposals): net capital gain R350,000.
- Taxable capital gain at the 40% inclusion rate: **R140,000**, added to taxable income.

```oa-check
name: YoA 2027 home sale, gain R3,400,000, 10% trade use
inputs:
  gain: 3400000
  trade_share: 0.10
  primary_residence_exclusion: 3000000
  annual_exclusion: 50000
  inclusion_rate: 0.40
steps:
  - trade_part: gain * trade_share
  - residence_part: gain - trade_part
  - residence_after_exclusion: max(residence_part - primary_residence_exclusion, 0)
  - net_gain: residence_after_exclusion + trade_part - annual_exclusion
  - taxable_capital_gain: net_gain * inclusion_rate
expected:
  trade_part: 340000.00
  residence_after_exclusion: 60000.00
  net_gain: 350000.00
  taxable_capital_gain: 140000.00
```

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| SARS, Capital Gains Tax (CGT) rate page (updated 26 February 2026): read for the 2027 exclusions (R3,000,000 primary residence, R50,000 annual, R440,000 year of death, R2.7 million small business with R15 million limit) and the effective rates 2022 to 2027 | https://www.sars.gov.za/tax-rates/income-tax/capital-gains-tax-cgt/ | 2026-11-14 |
| SARS, Budget Tax Guide 21 May 2025 (1 March 2025 to 28 February 2026): read for the YoA 2026 CGT exclusions and small business exclusion | https://www.sars.gov.za/budget-tax-guide-21-may-2025/ | 2026-11-14 |
| SARS, Budget Tax Guide 2024 (1 March 2024 to 28 February 2025): read for the YoA 2025 CGT exclusions | https://www.sars.gov.za/wp-content/uploads/Budget-tax-guide-2024-_.pdf | 2026-11-14 |
| SARS, Budget 2023 Tax Guide (1 March 2023 to 29 February 2024): read for the YoA 2024 CGT exclusions | https://www.sars.gov.za/budget-2023-tax-guide/ | 2026-11-14 |
| SARS, Budget Tax Guide 2022 (1 March 2022 to 28 February 2023): read for the YoA 2023 CGT exclusions | https://www.sars.gov.za/budget-tax-guide-2022/ | 2026-11-14 |
| SARS, Tax Free Investments page: read for the annual limits by year (R36,000 for 2021 to 2026, R46,000 from 2027), the R500,000 lifetime limit and the 40% charge | https://www.sars.gov.za/types-of-tax/personal-income-tax/tax-free-investments/ | 2026-11-14 |
| SARS, Budget Tax Guide 2026: read for the R46,000 tax-free limit and the 2026/27 CGT exclusions (cross-check) | https://www.sars.gov.za/budget-tax-guide-2026-online-version-for-printing/ | 2026-11-14 |
| Taxation Laws Amendment Act 5 of 2026 (GG 54448, 1 April 2026): read for section 32 (paragraph 5(1) proviso, short years of assessment) | https://www.sars.gov.za/legal-lprim-aa-2026-03-taxation-laws-amendment-act-5-of-2026-gg-54448-1-april-2026/ | 2026-11-14 |

Not yet confirmed: the 40% inclusion rate in para 10 (SARS rate pages publish only the 18% effective rate; the Act text did not open by script). How the R40,000 aggregate in the amended para 5(1) proviso (TLAA 5 of 2026 s 32) relates to the R50,000 annual exclusion for 2027: the amending Act prints R40,000, which may be a figure carried from before the increase; read the consolidated para 5 before applying it to a short year.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in South Africa.

> Contributed by Brandon Iverach.
