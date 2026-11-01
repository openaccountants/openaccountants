---
name: sc-transfer-pricing
description: "Seychelles transfer pricing for tax year 2026: the arm's length rule in Business Tax Act section 54, the Related Party Dealings Schedule, documentation triggers of SR 1,000,000 turnover, 10% of turnover and SR 50,000,000, the EUR 100 million masterfile, the 21-day production rule, record keeping and additional tax. Use for Seychelles related party schedule, RPD, TP documentation threshold or masterfile. Source-based; no accountant has signed it."
jurisdiction: SC
category: transfer-pricing
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Seychelles Transfer Pricing v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

A person in a controlled arrangement under Business Tax Act s 54, meaning dealings between associates. The first RPD year was 2024.

## Rates, bands and thresholds

| Item | Amount or rule | Tax year | Official URL |
|---|---|---|---|
| RPD Schedule | Any person in a controlled arrangement, with the business tax return | 2026 | https://src.gov.sc/seychelles-tax-system/ |
| TP documentation | Annual turnover above SR 1,000,000 | 2026 | same |
| Additional documentation | Controlled arrangements above 10% of turnover, or above SR 50,000,000 | 2026 | same |
| Masterfile | MNE group consolidated turnover above EUR 100 million | 2026 | same |
| Production | Within 21 days of the Commissioner General asking | 2026 | https://src.gov.sc/wp-content/uploads/2023/11/SI-73-2023-Business-Tax-Transfer-Pricing-Documentation-Regulations-2023.pdf |
| Failure to complete RPD Schedule, no reasonable cause | (a) SR 5,000 if not furnished under regs 3(1) and 3(2); and (b) SR 75,000 plus SR 2,500 a week or part week | 2026 | https://src.gov.sc/wp-content/uploads/2023/11/SI-74-2023-Business-Tax-Related-Party-Dealings-Regulations-2023.pdf |
| False or misleading RPD information, knowingly | 5% of annual turnover | 2026 | same |
| Failure to keep records | At least SR 10,000 small, SR 50,000 medium, SR 100,000 large | 2026 | same |

No 2026 amendment to this rate was found on the SRC legislation list read on 1 Nov 2026, so 2026 rests on the instruments below staying in force.

## The base

Conditions must match what independent parties would agree. SRC uses the most appropriate method or a combination, weighing strengths and weaknesses, the facts, and reliable data ([Ruling 2015-3](https://src.gov.sc/wp-content/uploads/2025/04/Transfer-Pricing-Ruling.pdf)).

## Deadlines and filing

RPD Schedule: with the return, by 31 March, unless a substituted or transitional year applies. Documentation is held and given only on request. Keep records for seven years after the period ([S.I. 74 of 2023](https://src.gov.sc/wp-content/uploads/2023/11/SI-74-2023-Business-Tax-Related-Party-Dealings-Regulations-2023.pdf)). Download the [RPD Schedule](https://src.gov.sc/wp-content/uploads/2024/07/RPD-Schedule_final.xlsx) and attach it to the Schedule 3 return where that return applies.

## Penalties and interest

See the table. Section 42 of the Revenue Administration Act does not apply to the RPD Schedule (reg 5(2)).

## Cross-border points

Country-by-Country Reporting exists under S.I. 25 of 2019; that scan was not read, so its thresholds are not stated here.

## Two worked examples that recompute

Turnover SR 30,000,000, controlled arrangements SR 4,000,000: 13.33%, above 10%, so additional documentation is needed.

```oa-check
name: Controlled share of turnover
inputs:
  controlled: 4000000
  turnover: 30000000
steps:
  - share: round(controlled / turnover * 100, 2)
expected:
  share: 13.33
```

Decision: can the group stay out of additional documentation? At SR 2,500,000 the share is 8.33%, under 10% and under SR 50,000,000, so only basic documentation applies. A false schedule at this turnover costs SR 1,500,000.

```oa-check
name: Below the test, and false-schedule exposure
inputs:
  controlled: 2500000
  turnover: 30000000
steps:
  - share: round(controlled / turnover * 100, 2)
  - exposure: turnover * 0.05
expected:
  exposure: 1500000
```

## Ask the client first

- Who are the associates and what are the dealings?
- Annual turnover and value of controlled arrangements?
- Group consolidated turnover?
- Calendar or substituted tax year?

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for the figures cited: SRC Tax System page, whole page read | https://src.gov.sc/seychelles-tax-system/ | 2026-11-01 |
| Read for the figures cited: S.I. 73 of 2023, commencement and documentation regs | https://src.gov.sc/wp-content/uploads/2023/11/SI-73-2023-Business-Tax-Transfer-Pricing-Documentation-Regulations-2023.pdf | 2026-11-01 |
| Read for the figures cited: S.I. 74 of 2023, regs 4 to 7 | https://src.gov.sc/wp-content/uploads/2023/11/SI-74-2023-Business-Tax-Related-Party-Dealings-Regulations-2023.pdf | 2026-11-01 |
| Read for the figures cited: SRC Public Ruling 2015-3, transfer pricing | https://src.gov.sc/wp-content/uploads/2025/04/Transfer-Pricing-Ruling.pdf | 2026-11-01 |
| Read for the figures cited: SRC Public Ruling 2025-1, read by OCR | https://src.gov.sc/wp-content/uploads/2025/04/Public-Ruling-BTR_final_02.04.2025.pdf | 2026-11-01 |

Not yet confirmed: how limbs (a) and (b) of reg 5(1) of S.I. 74 of 2023 fit together, as the text joins them with "and"; Country-by-Country Reporting thresholds; size definitions.

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
