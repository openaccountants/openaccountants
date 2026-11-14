---
name: nh-interest-dividends-note
description: >
  New Hampshire 2026 personal income tax routing: no wage tax, repeal of interest and dividends tax for periods beginning after 2024, historical DP-10 obligations, and the separate business-tax boundary.
jurisdiction: US-NH
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-11-13
version: "0.2"
type: situation-rules
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - nh-bpt-bet
  - us-form-1040-individual-return
---

# New Hampshire interest and dividends repeal, 2026

> **Source-cited draft.** Checked against RSA chapter 77 and the DRA Interest & Dividends Tax FAQs on 2026-11-13. No accountant has reviewed this skill. General reference only; a qualified tax professional must review the facts and any filing. Circular 230 section 10.37: apply the period, residency and business-activity facts before reaching a conclusion.

**Answer first.** For a taxable period beginning in 2026, New Hampshire has no personal wage tax or Interest & Dividends Tax return. The repeal is keyed to the period's **beginning**, not its ending. Business activity, including a sole proprietorship, still needs the separate `nh-bpt-bet` tests.

## Scope

Individuals checking the repeal, prior-period DP-10 obligations and the distinction between personal investment income and business income. This is not a claim that every tax in New Hampshire disappeared. Private-investment capital gains do not create a separate New Hampshire personal capital-gains tax; gains from business assets can enter BPT under [RSA 77-A:1 III(d), VI](https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm). Load `us-form-1040-individual-return` for federal tax and `nh-payroll` for employer UI.

## Ask the client first

1. What are the exact beginning and ending dates of the taxable period?
2. Is the item personal investment income, wages, a business receipt or a gain on a business asset?
3. Is an old DP-10, amended return, assessment or unpaid balance involved?
4. For a pre-repeal period, what are residency dates, joint status and gross interest and dividends?
5. Does the person own a business or an entity with New Hampshire activity?

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or treatment | Official source |
|---|---|---|
| Period begins after December 31, 2024 | RSA chapter 77 repealed; no I&D return or estimates for that period | [DRA I&D FAQs, opening and estimates](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/interest-dividends-tax-frequently-asked-questions) |
| Historical period ending before December 31, 2023 | 5% I&D rate | [DRA I&D FAQs, what is the tax](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/interest-dividends-tax-frequently-asked-questions) |
| Historical period ending on or after December 31, 2023, before the next rate applies | 4% I&D rate | [DRA I&D FAQs](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/interest-dividends-tax-frequently-asked-questions) |
| Historical period ending on or after December 31, 2024, beginning on or before that date | 3% I&D rate; a fiscal period ending in 2025 is not automatically repealed | [DRA I&D FAQs](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/interest-dividends-tax-frequently-asked-questions) |
| Historical resident individual filing test | Gross I&D exceeds USD 2,400 single or USD 4,800 joint; not a 2026 threshold | [DRA I&D FAQs, who must file](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/interest-dividends-tax-frequently-asked-questions) |
| Historical exemptions | USD 2,400 per individual; additional USD 1,200 for age 65+, blindness, or qualifying disabled person unable to work and under 65 | [DRA I&D FAQs, exemptions](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/interest-dividends-tax-frequently-asked-questions) |
| Historical DP-10 deadline | 15th day of fourth month after period ends; calendar 2024 return due April 15, 2025 | [DRA I&D FAQs, when due](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/interest-dividends-tax-frequently-asked-questions) |

1. Compare the beginning date with the repeal. Stop the I&D computation for a period beginning after 2024. Do not apply the old exemption and rate as though the tax were still in force.
2. For an old period, use that period's DP-10 and instructions. The DRA FAQs retain historical rules for part-year residents, entities, grantor trusts, beneficiaries, S-corporation distributions and exemptions. Do not use this short repeal skill to resolve those fact-dependent returns.
3. Preserve unresolved historical returns and balances. Repeal of the charge for new periods does not by itself close a prior-period assessment.
4. Route business receipts, rental activity conducted as a business and gains on business assets to `nh-bpt-bet`. Do not tell a Schedule C filer that self-employment income is free of New Hampshire business tax.
5. No general sales tax is a separate proposition from the repeal. The state's selective meals/rentals, communications, property and transfer taxes are outside this skill; see the README.

## Boundary and exception table

| Facts | Outcome |
|---|---|
| Only 2026 personal interest and dividends | No 2026 DP-10 |
| Fiscal year begins in 2024 and ends in 2025 | Repeal does not apply merely because the ending year is 2025 |
| Historical trust or S-corporation distribution | Read the old-period DP-10 instructions and DRA FAQs; do not assume every distribution was exempt |
| Proprietor or SMLLC with New Hampshire business activity | Separate BPT/BET tests, despite personal-tax repeal |
| Wages earned in another state or resident of another state | That state's filing/withholding rules remain relevant |

## Worked cases

**Case 1, decide whether to file.** A single resident receives USD 10,000 of ordinary personal bank interest, with no additional exemption. For calendar 2024, taxable interest is USD 7,600 and I&D tax is USD 228. For calendar 2026, the same receipts create no DP-10 tax and no DP-10 filing because the period begins after repeal. This compares two periods, not two elective methods.

```oa-check
name: Personal interest before and after repeal
inputs:
  interest: 10000
  historical_exemption: 2400
steps:
  - historical_base: max(interest - historical_exemption, 0)
  - tax_2024: historical_base * 0.03
  - tax_2026: interest * 0
expected:
  historical_base: 7600
  tax_2024: 228
  tax_2026: 0
```

**Case 2, beginning-date boundary.** A hypothetical single fiscal-period filer has USD 20,000 taxable interest after all correctly determined historical exemptions. A period beginning December 1, 2024 and ending November 30, 2025 remains within the old tax: USD 600 at 3%. A period beginning December 1, 2025 and ending November 30, 2026 is repealed: zero. The preparer must establish whether fiscal filing is permitted for the actual taxpayer before applying this illustration.

```oa-check
name: Fiscal period repeal boundary
inputs:
  historical_taxable_interest: 20000
steps:
  - begins_2024: historical_taxable_interest * 0.03
  - begins_2025: historical_taxable_interest * 0
expected:
  begins_2024: 600
  begins_2025: 0
```

## When to refuse or refer

Refer contested residency, pre-repeal trust/entity distributions, penalties and collection notices to a professional who can read the full historical file. Use `nh-bpt-bet` for business taxes and the relevant other-state skill for cross-border wages. A personal-tax repeal does not establish federal exemption.

## Sources

| Source | URL | Read on |
|---|---|---|
| RSA chapter 77. Read for the repeal effective January 1, 2025. | https://gc.nh.gov/rsa/html/V/77/77-mrg.htm | 2026-11-13 |
| DRA I&D FAQs. Read for the beginning-date rule, historic rates, filing thresholds, exemptions, DP-10 due date and old trust/distribution sections. Retrieved with basic Firecrawl after direct web and ordinary browser access were denied. | https://www.revenue.nh.gov/resource-center/frequently-asked-questions/interest-dividends-tax-frequently-asked-questions | 2026-11-13 |
| RSA 77-A:1. Read for the business organization definition and business-asset gains in gross business profits, distinct from private investments. | https://gc.nh.gov/rsa/html/V/77-A/77-A-1.htm | 2026-11-13 |

Not yet confirmed: the old note's historical enactment date of 1923 and its account of House Bill 2 in the 2023 session signed by Governor Chris Sununu are not independently established here; old-period trust, entity and part-year calculations require their historical forms. No accountant has approved this skill.
