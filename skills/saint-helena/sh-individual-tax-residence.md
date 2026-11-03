---
name: sh-individual-tax-residence
description: >
  Saint Helena island individual tax residence for tax year 2026 (1 April 2026 to 31 March 2027). Covers the three section 2 tests (more than 90 days with a normal abode, more than 183 days, a contract of at least 183 days), arrival and departure, the one-tenth travel discretion, the source rule, and where the official leaflet conflicts with the statute. Use for residence, days on island or part-year allowance questions on St Helena. Does not apply to Ascension or Tristan da Cunha.
version: 0.3
jurisdiction: SH
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Saint Helena island: individual tax residence v0.3

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. It covers Saint Helena island only, not Ascension or Tristan da Cunha, which have separate laws.

## Who this applies to

Individuals asking whether they are resident for income tax on Saint Helena island. Ascension and Tristan da Cunha have separate laws, as the [legislation introduction](https://www.sainthelena.gov.sh/st-helena/government/legislation/laws-of-st-helena/) explains. The SH code does not extend this skill to those islands. Tax residence does not establish immigration status (Tax Guide 12).

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Normal abode route | Normal place of abode in Saint Helena and present for more than 90 days of the tax year (s.2) | 2026 | https://www.sainthelena.gov.sh/documents/Income-Tax-Ord-Updated-011021 |
| Physical presence route | Present for periods exceeding in aggregate 183 days in the tax year (s.2) | 2026 | same |
| Employment contract route | Present in the year fulfilling a contract of employment exercised in Saint Helena specified to be of not less than 183 days (s.2) | 2026 | same |
| Travel discretion | Commissioner may disregard up to one tenth of the relevant days if presence resulted only from infrequent travel opportunities (s.2 first proviso) | 2026 | same |
| Monthly allowance | 1/12 of £7,000 for each month resident, or each month receiving Saint Helena employment income if non-resident (s.10(3)) | 2026 | same |

## The base

Meeting one route is sufficient. The boundaries differ: exactly 90 days does not meet the first, exactly 183 days does not meet the second, and a contract of exactly 183 days meets the duration part of the third, though the other conditions still apply. Do not decide non-residence because one test fails.

Arrival and departure: a person resident this year but not last year is resident only from the first day present. A person resident this year but not next year is resident only to the last day present. A final conclusion can depend on an adjacent year.

The travel discretion is not an automatic adjustment. Keep evidence and any determination with the calculation.

Residence does not replace the source test. Section 8 charges income in or from Saint Helena. Employment exercised on the island is within scope even if paid overseas, and income of a resident from service on certain vessels is included (s.2). Do not reduce this to a rule that overseas-paid income is exempt.

## Deadlines and filing

There is no separate residence filing. Residence feeds the allowance and the return.

1. Build a day count for 1 April to 31 March.
2. Test each route, then the adjacent years.
3. Employees: declare the expected duration if not ordinarily or only temporarily resident (Regulation 6(4)), and on starting or ceasing employment (Regulation 6(3)).
4. If a boundary turns on the travel discretion, ask the Commissioner at the Income Tax Office before filing.
5. Enter the months resident on the [personal return](sh-personal-income-tax.md).

Suggested evidence: travel ledger, accommodation and normal-abode facts, signed employment contract, actual place of work, previous and following year residence, and any Commissioner direction.

## Penalties and interest

Residence has no penalty of its own. A wrong claim in a return falls under s.68: 75% if knowing or reckless, 20% otherwise.

## Cross-border points

The official Tax Guides conflict with the statute at two points. Guide 1 states the normal-abode test as at least 90 days, and Guides 1 and 12 say non-residents receive no personal allowance. The statute says more than 90 days, and s.10(3)(b) gives non-resident employees a monthly allowance. The statute wins; resolve a boundary case with the office before filing. Treaty tie-breakers: see [cross-border points](sh-cross-border.md).

## Two worked examples that recompute

Example 1: the most the Commissioner may disregard against the 183-day count.

```oa-check
name: Travel discretion ceiling
inputs:
  days: 183
  share: 0.1
steps:
  - ceiling: days * share
expected:
  ceiling: 18.30
```

Example 2: resident six months of the year.

```oa-check
name: Part-year allowance
inputs:
  allowance: 7000
  months: 6
steps:
  - part: allowance * months / 12
expected:
  part: 3500.00
```


## Ask the client first

- Days present in this tax year and the two adjacent years?
- Normal place of abode?
- Contract length, and where the work is done?
- Any travel disruption, and any Commissioner direction?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Ordinance 2012 and Income Tax Regulations 2012, consolidation authoritative at 1 October 2021, read for the sections and regulations cited | https://www.sainthelena.gov.sh/documents/Income-Tax-Ord-Updated-011021 | 2026-11-01 |
| Tax Guide 1, Residency in St Helena, read for the residence tests and allowance | https://www.sainthelena.gov.sh/documents/Tax-Guide-No.-1-Residency-in-St-Helena | 2026-11-01 |
| Tax Guide 12, Questions on Taxes and Allowances (April 2024), read in full | https://www.sainthelena.gov.sh/documents/Tax-Guide-No.-12-Questions-on-Taxes-Allowances-on-St-Helena | 2026-11-01 |
| Laws of St Helena index, read in full | https://www.sainthelena.gov.sh/st-helena/government/legislation/laws-of-st-helena/ | 2026-11-01 |

Not yet confirmed: Any instrument after the 1 October 2021 consolidation: the Laws index, press pages and 2026 Income Tax Office page show no enacted change to these rates, and a full Gazette audit was not done. How part months count toward the 1/12 allowance. How days of arrival and departure are counted.

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
