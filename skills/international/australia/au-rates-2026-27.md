---
name: au-rates-2026-27
description: Use this skill whenever you need a current Australian tax rate, threshold, cap or due date for the 2026-27 or 2025-26 income year -- individual brackets, HELP repayment, Medicare levy and surcharge, super guarantee and contribution caps, Division 296, company rates, Div 7A benchmark, FBT, CGT caps and concessions, GST, PAYG instalment uplift, cents-per-km, car limits, penalty units, payroll tax, minimum wage or ASIC fees. Single-page rates card; every figure carries its source. Trigger on "what is the current rate", "2026-27 threshold", "how much is the cap", or any AU figure lookup. Load alongside the topic guide.
version: "1.0"
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 primary; 2025-26 retained for lodgment-season work"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Rates Card 2026-27 (with 2025-26) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Single-page lookup for the figures every other Australian guide relies on. Each row names its primary source. Verified against those sources on 20 August 2026. Deeper rules live in the topic guides named in each section; this card never overrides them.

## Individual income tax

**Resident brackets**

| Taxable income | 2025-26 rate | 2026-27 rate |
| --- | --- | --- |
| $0 -- $18,200 | 0% | 0% |
| $18,201 -- $45,000 | 16% | **15%** |
| $45,001 -- $135,000 | 30% | 30% |
| $135,001 -- $190,000 | 37% | 37% |
| $190,001+ | 45% | 45% |

Tax on full bands: 2025-26 -- $4,288 at $45,000, $31,288 at $135,000, $51,638 at $190,000. 2026-27 -- $4,020 / $31,020 / $51,370. The 15% rate falls to **14% from 1 July 2027**. _(ATO QC 73320; Treasury Laws Amendment (More Cost of Living Relief) Act 2025)_

**Non-residents:** no tax-free threshold; 30% from $0 to $135,000 (2026-27), then resident bands. No Medicare levy.

**Offsets and deductions**

| Item | Value | Source |
| --- | --- | --- |
| LITO | $700 to $37,500; taper 5c/$1 to $45,000; then 1.5c/$1 to nil at $66,667 | ATO Low income tax offset |
| SBITO | 16% of tax on net small business income, cap $1,000, turnover < $5m | ITAA 1997 Subdiv 328-F |
| $1,000 standard WRE deduction | From 1 July 2026 (2026-27 returns). Excludes PSI and business-only earners | Tax Reform No. 1 Act 2026 Sch 4; QC 107405 |
| WFH fixed rate | 70c/hour (2024-25 through 2026-27) | PCG 2023/1 |
| Cents per km | 88c (2025-26); **91c (2026-27)**, cap 5,000 business km | ATO cents-per-km rates |
| Car limit (depreciation) | $69,674 (2025-26); **$69,883 (2026-27)** | ATO car thresholds |

## HELP/study loans (2025-26 onwards: marginal system)

Repayment income = taxable income + reportable fringe benefits + reportable super + exempt foreign income + net investment losses.

| Repayment income (2025-26) | Marginal repayment rate |
| --- | --- |
| Below $67,000 | Nil |
| $67,001 -- $125,000 | 15% of excess over $67,000 |
| $125,001 -- $179,285 | $8,700 + 17% of excess over $125,000 |
| $179,286+ | 10% of repayment income (cap rule) |

One-off 20% debt reduction applied before 1 June 2026 indexation; thresholds index for 2026-27 (confirm current-year bands at ATO study loan repayment thresholds before computing). _(Education and Other Legislation Amendment (VET Fee Protection and Other Measures) Act 2025; ATO QC 103927)_

## Medicare

| Item | 2025-26 | Source |
| --- | --- | --- |
| Levy | 2% of taxable income | MLA 1986 |
| Low-income threshold (single) | $28,011 / shade-in to $35,013 | ATO QC 27031 |
| Low-income threshold (family) | $47,238 + $4,338 per child | ATO QC 27031 |
| SAPTO single | $44,268 / $55,335 | ATO QC 27031 |
| MLS base tier | Single $101,000 / family $202,000 (then 1% / 1.25% / 1.5%) | ATO MLS thresholds |
| PHI rebate (base, under 65) | 24.288% to 31 Mar 2026; 24.118% from 1 Apr 2026 | PHI Circular 12/26 |

2026-27 Medicare low-income thresholds index with CPI; confirm at ATO QC 27031 when lodging 2026-27.

## Superannuation

| Item | 2025-26 | 2026-27 | Source |
| --- | --- | --- | --- |
| SG rate | 12% | 12% (terminal) | ATO SG rates |
| Payment deadline | Quarterly (28th) | **Payday super: fund receipt within 7 business days of each payday from 1 Jul 2026** | payday super law; au-super-guarantee |
| Concessional cap | $30,000 | **$32,500** | ATO contributions caps |
| Non-concessional cap | $120,000 | **$130,000** | ATO contributions caps |
| NCC bring-forward (TSB at prior 30 June) | <$1.76m: $360k/3yr | <$1.84m: $390k/3yr; $1.84--<$1.97m: $260k/2yr; $1.97--<$2.1m: $130k; >=$2.1m: nil | ATO contributions caps |
| General transfer balance cap | $2.0m | **$2.1m** | ATO TBC |
| CGT cap amount | $1,865,000 | **$1,935,000** | ATO key super rates |
| Div 293 threshold | $250,000 (frozen) | $250,000 | ATO Div 293 |
| Div 296 | -- | **First year: extra 15% on earnings share of TSB $3m--$10m; extra 25% above $10m; indexed; realised-earnings basis** | Building a Stronger and Fairer Super System Act 2026 |
| Downsizer | $300,000 from age 55 | $300,000 | ATO downsizer |
| SG maximum contribution base | $62,500/quarter | **$270,830/year (annual basis under payday super)** | ATO Super guarantee page |

## Companies

| Item | Value | Source |
| --- | --- | --- |
| BRE rate | 25% (turnover < $50m AND <= 80% BREPI) | ITRA 1986 ss 23AA-23AB |
| Standard rate | 30% | ITRA 1986 |
| Franking | At 25%: credit = distribution / 3. At 30%: x 3/7 | au-company-tax |
| Loss carry-back | ENDED (2019-20 to 2022-23 claim years only) | former Div 160 |
| Div 7A benchmark | 8.37% (2025-26); **8.77% (2026-27)** | ATO Div 7A rates |
| PAYG GDP uplift | 4% (2025-26); **5% (2026-27)** | ATO GDP adjustment |
| Amendment period (SMB) | 4 years for 2024-25+ assessments | ATO amendment periods |

## FBT (year ending 31 March 2027)

| Item | Value | Source |
| --- | --- | --- |
| Rate | 47% | FBTAA 1986 |
| Type 1 / Type 2 gross-up | 2.0802 / 1.8868 | ATO FBT rates |
| RFBA trigger | > $2,000 taxable value; report x 1.8868 | ATO RFBA |
| EV exemption | Battery/hydrogen cars only; PHEVs out from 1 Apr 2025 (grandfathering); wind-back announced from 1 Apr 2027, not law | au-fbt Rule 5 |
| EV home-charging shortcut | 5.47c/km (FBT year from 1 Apr 2026) | PCG 2024/2 |
| Record-keeping exemption base | $10,962 (FBT 2026-27) | au-fbt Rule 12 |

## CGT

| Item | Value | Source |
| --- | --- | --- |
| Discount | 50% individuals/trusts (assets 12+ months); one-third super funds; nil companies | ITAA 1997 Div 115 |
| **Reform from 1 Jul 2027** | Gains accruing from 1 Jul 2027: indexation + 30% minimum rate replaces the 50% discount (individuals/trusts/partnerships); deemed re-acquisition 30 Jun 2027 | Tax Reform No. 1 Act 2026; au-capital-gains |
| FRCGW | 15%, no threshold, contracts from 1 Jan 2025; clearance certificate mandatory for resident vendors | TLA (2024 Tax and Other Measures No. 1) Act 2024; QC 26663 |
| Div 152 gateways | $2m CGT SBE turnover / $6m MNAV | au-small-business-cgt |
| Retirement exemption | $500,000 lifetime | Subdiv 152-D |

## GST and indirect

| Item | Value | Source |
| --- | --- | --- |
| Rate / registration | 10% / $75,000 ($150,000 NFP; $1 taxi-rideshare) | GST Act |
| Instant asset write-off | $20,000 per asset (turnover < $10m) legislated to 30 Jun 2026; permanence from 1 Jul 2026 announced, confirm enactment | ATO QC 103578 |
| Penalty unit | $330 (7 Nov 2024 -- 30 Jun 2026); **$364 from 1 Jul 2026** | ATO QC 71196 |
| GIC | **Not deductible from 1 Jul 2025** (SIC likewise) | Tax Incentives and Integrity Act 2025; QC 73746 |

## Employers

| Item | Value | Source |
| --- | --- | --- |
| National minimum wage | **$26.44/hr, $1,004.90/wk from 1 Jul 2026** ($24.95 / $948.10 prior) | FWC AWR 2025-26 |
| Payroll tax NSW | 5.45%, $1.2m threshold | Revenue NSW |
| Payroll tax VIC | 4.85% (regional 1.2125%), $1.0m; surcharges >$10m | SRO Vic |
| Payroll tax QLD | 4.75% <=$6.5m / 4.95% above; $1.3m deduction phasing to $10.4m | QRO |
| Other states | WA 5.5%/$1m; SA 0-4.95%/$1.5m; TAS 4%+6.1%/$1.25m; ACT 6.85%/$2m; NT 5.5%/$1.5m | state revenue offices |
| ASIC annual review (Pty Ltd) | **$342 from 1 Jul 2026** ($329 prior); registration $636; SMSF special purpose $70 | ASIC fee indexation |

## Maintenance rule

This card is the single place indexed figures live outside their topic guides. When any figure above changes: update the topic guide first, then this card in the same PR, and advance both `last_updated` fields. Rows sourced to a topic guide (au-fbt, au-company-tax) must never disagree with that guide; where they do, the topic guide wins and this card is the bug.

## Provenance

All figures verified 20 August 2026 directly against: ato.gov.au rate pages (QC 73320, 27031, 71196, 73746, 103578, 103927, contributions caps, key super rates, car thresholds, Div 7A rates, GDP adjustment), Department of Health PHI Circular 12/26, Revenue NSW / SRO Vic / QRO current-rates pages, FWC Annual Wage Review 2025-26 decision, ASIC fee indexation page (1 July 2026), and the amending Acts named inline.

<!-- openaccountants-cta-block -->

## Talk to a verified accountant

This guide covers the mechanical rules. For anything touching judgement -- residency, structuring, disputes, amounts that matter -- speak to a verified accountant on Open Accountants.

- Browse verified professionals: https://www.openaccountants.com
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or accounting advice. Verify current rates and rules against primary sources before acting. Figures and thresholds change; the tax year stated in the front matter governs.
