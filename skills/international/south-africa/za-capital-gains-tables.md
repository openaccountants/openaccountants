---
name: za-capital-gains-tables
description: >
  Year-keyed South African capital gains tax rate tables for natural persons, covering five years of assessment (2023 to 2027). Contains the annual exclusion, the increased exclusion in the year of death, the primary residence exclusion and the inclusion rate for individuals, together with the tax-free savings account annual and lifetime contribution limits and the excess contribution penalty rate. Use for any South African CGT exclusion or inclusion rate lookup, primary residence disposal, deceased estate, or tax-free savings account limit question, current or prior year.
jurisdiction: ZA
category: international
tax_year: 2023
tax_year_notes: "2022/23 to 2026/27 — SARS years of assessment 2023 to 2027"
tier: 2
last_updated: 2026-09-02
version: 0.1
depends_on:
  - foundation
verified_by: pending
---

# South Africa — Capital Gains Tax Rate Tables (natural persons)

Year-keyed CGT exclusions and inclusion rates for **natural persons**, years of
assessment 2023 to 2027, plus the tax-free savings account limits. Data only: this
file does not compute a gain and does not set out base cost determination.

> **Verification status — checked 2 September 2026.**
>
> Confirmed against SARS, figure by figure:
>
> - **Annual exclusion, year-of-death exclusion and primary residence exclusion for
>   YoA 2027** — R50,000 / R440,000 / R3,000,000
> - **Maximum effective rate for individuals and special trusts, YoA 2027** — 18%
>
> **Still to confirm** — carried from the same reconciled source, but not
> independently re-checked:
>
> - The same four CGT figures for **YoA 2023 to 2026**
> - The **tax-free savings account** limits and penalty rate, all five years

## How South African years of assessment are labelled

SARS numbers a year of assessment by the calendar year in which it **ends**. The tax
year runs 1 March to the last day of February. So the year of assessment ending
28 February 2027 is **YoA 2027**, and it is the year commonly written "2026/27".

| Year of assessment | Commonly written | Period |
| --- | --- | --- |
| 2023 | 2022/23 | 1 March 2022 – 28 February 2023 |
| 2024 | 2023/24 | 1 March 2023 – 29 February 2024 |
| 2025 | 2024/25 | 1 March 2024 – 28 February 2025 |
| 2026 | 2025/26 | 1 March 2025 – 28 February 2026 |
| 2027 | 2026/27 | 1 March 2026 – 28 February 2027 |

Getting this wrong by one year is the single most common error in South African rate
lookups. Every table below is keyed by **year of assessment**.


## Section 1 — Scope

This file covers, for each year of assessment 2023-2027:

- Annual exclusion (Eighth Schedule para 5)
- Annual exclusion in the year of death (Eighth Schedule para 5(2))
- Primary residence exclusion (Eighth Schedule para 45)
- Inclusion rate for natural persons (s 26A read with Eighth Schedule para 10)
- Tax-free savings account annual and lifetime limits and penalty rate (s 12T)

Not covered here: inclusion rates for companies and trusts; base cost rules;
the small business asset exclusion under s 10(1)(zJ); roll-overs; or any
computation rule.

---

## Section 2 — CGT exclusions and inclusion rate (natural persons)

| YoA | Annual exclusion | Annual exclusion (year of death) | Primary residence exclusion | Inclusion rate |
| --- | --- | --- | --- | --- |
| 2023 (2022/23) | R40,000 | R300,000 | R2,000,000 | 40% |
| 2024 (2023/24) | R40,000 | R300,000 | R2,000,000 | 40% |
| 2025 (2024/25) | R40,000 | R300,000 | R2,000,000 | 40% |
| 2026 (2025/26) | R40,000 | R300,000 | R2,000,000 | 40% |
| 2027 (2026/27) | R50,000 | R440,000 | R3,000,000 | 40% |

_Source: Income Tax Act 58 of 1962 s 26A; Eighth Schedule paras 5, 10 and 45. YoA 2027 confirmed against SARS, Capital Gains Tax (CGT) rate tables dated 25 February 2026: <https://www.sars.gov.za/tax-rates/income-tax/capital-gains-tax-cgt/>, 2026-09-02. Earlier years not re-checked._

**Effective rate.** The inclusion rate is 40% in every year in this file, so the
maximum effective CGT rate for a natural person is 40% of the top marginal rate of
45%, being 18%.

---

## Section 3 — Tax-free savings accounts

| YoA | Annual contribution limit | Lifetime contribution limit | Penalty on excess |
| --- | --- | --- | --- |
| 2023 (2022/23) | R36,000 | R500,000 | 40% |
| 2024 (2023/24) | R36,000 | R500,000 | 40% |
| 2025 (2024/25) | R36,000 | R500,000 | 40% |
| 2026 (2025/26) | R36,000 | R500,000 | 40% |
| 2027 (2026/27) | R46,000 | R500,000 | 40% |

_Source: Income Tax Act 58 of 1962 s 12T._

---

## Section 4 — Edge cases and traps

- **The YoA 2027 increases are easy to miss.** The annual exclusion, the death
  exclusion and the primary residence exclusion all increased with effect from
  1 March 2026. A guide still quoting the prior figures for YoA 2027 is wrong, and
  the error is most dangerous inside a home-office warning, where the superseded
  annual exclusion understates the relief available on a tainted portion.
- **The primary residence exclusion applies to the first portion of the GAIN**, not
  the first portion of the proceeds.
- **Home-office tainting.** Where part of a residence is used for trade, the primary
  residence exclusion does not apply to the tainted portion, which falls back on the
  annual exclusion only. Use the annual exclusion **for the year of disposal**.
- **The lifetime TFSA limit has not moved** while the annual limit has. Do not infer
  one from the other.
- **The death exclusion replaces the annual exclusion** in the year of death; the two
  are not cumulative.

## Section 5 — Self-checks

1. **Year of disposal.** The exclusion is the one for the year of assessment in which
   disposal occurred, not the year of assessment in which the return is filed.
2. **Death exclusion is larger than the annual exclusion** in every year. If it is
   not, the two have been transposed.
3. **Inclusion rate is for natural persons only.** Companies and trusts differ and
   are out of scope here.

---

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in South Africa.
