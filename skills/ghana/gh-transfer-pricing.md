---
name: gh-transfer-pricing
description: >
  Use this skill for Ghana transfer pricing compliance in tax year 2026 under the Transfer Pricing Regulations, 2020 (L.I. 2412) and Income Tax Act, 2015 (Act 896) as amended. It covers who is in a controlled relationship, the 25% control test, arm's length pricing, the methods, contemporaneous documentation, Master and Local files, the transfer pricing return due four months after year end, the Country-by-Country Report due twelve months after the reporting year, adjustments and penalties. Trigger on "Ghana transfer pricing", "related party Ghana", "TP return GRA", "controlled relationship", "Master file Ghana", "CbC Ghana". Rates are in gh-corporate-income-tax and withholding is in gh-cross-border.
version: 0.1
jurisdiction: GH
category: transfer-pricing
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana Transfer Pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Law: Act 896 s.31 (arm's length standard) and s.128 as replaced by Act 1094; Transfer Pricing Regulations, 2020 (L.I. 2412). The GRA page still names L.I. 2188; the GRA guidance list names L.I. 2412, which is followed here.

## Who this applies to

Any person with an arrangement with a person in a controlled relationship. Persons are controlled where they are an individual and a relative; partners in one partnership; an entity and its associate; settlor, trustee and beneficiary; or one acts on the direction of the other. Control means 25% or more of voting power or rights to income or capital, directly or through interposed entities ([Act 1094 s.11](https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf)).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Control | 25% or more | Voting power, income or capital | 2026 | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf |
| Transfer pricing return | 4 months after each basis period | Controlled arrangements (reg 11) | 2026 | https://gra.gov.gh/wp-content/uploads/2023/12/Transfer-Pricing-Regulations-2020-LI-24121-_231207_142107.pdf |
| Contemporaneous documentation | Filed electronically 4 months after each basis period | Master file and Local file (reg 12) | 2026 | same |
| Country-by-Country Report | 12 months after the last day of the reporting year | Ghana-resident Ultimate Parent, or Constituent Entity meeting reg 13(2) (regs 11, 13) | 2026 | same |
| Country-by-Country group size | GHS 2.9 billion | A group below this consolidated revenue in the preceding fiscal year is excluded (reg 17) | 2026 | same |
| Documentation exemption | USD 200,000, in cedi | Arrangement at or below this value is exempt from reg 12(1) documentation, not from the return; arrangements can be aggregated if designed for avoidance (reg 14) | 2026 | same |
| Low value-adding intra-group services | Mark-up up to 3% on cost | Treated as arm's length on cost-plus; election to skip documentation on the mark-up within 30 days (reg 14) | 2026 | same |
| Interest on adjustment | 125% of the Bank of Ghana policy rate, compounded monthly | Adjustment is an adjusted assessment (reg 16; Act 915 s.71) | 2026 | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf |

## The base

1. List every arrangement with a controlled person: goods, services, financing, IP, transfers of functions.
2. Analyse functions, assets and risks.
3. Pick the method under the First Schedule of L.I. 2412.
4. Compare with independent parties, and use the safe harbour ranges in the Second Schedule where they apply.
5. Adjust taxable income so that the price is arm's length (Act 896 s.31). GRA may also re-characterise an arrangement, including debt as equity (s.31(5)). An arm's length price is what unrelated, independent parties would agree ([GRA](https://gra.gov.gh/domestic-tax/transfer-pricing/)).

## Deadlines and filing

1. Prepare the Master file and Local file during the year. They must exist for each year of assessment.
2. Complete the [Transfer Pricing Return form](https://gra.gov.gh/wp-content/uploads/2022/06/Transfer-Pricing-Return-Form.pdf): identity, relationship, group structure, consolidated revenue, arrangements, business activities.
3. Send the return and an electronic copy of the documents by 30 April 2027 for a December year end.
4. A paid preparer signs the return (Act 915 s.29).
5. In a group, confirm by year end which entity files the Country-by-Country Report.

## Penalties and interest

Regulation 16 applies Act 915 on failing to file, keeping documents, under-payment, interest and offences. Late return: GHS 500 plus GHS 10 a day. No documents: 75% of the tax for the period if deliberate; otherwise the lesser of that and GHS 250, monthly ([Act 915 ss 72, 73](https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf)).

## Cross-border points

Payments to related non-residents also carry withholding: see [gh-cross-border](gh-cross-border.md). Thin capitalisation, 3 to 1, is in [gh-corporate-income-tax](gh-corporate-income-tax.md).

## Two worked examples that recompute

**Example 1: adjustment.** A Ghana distributor pays its parent GHS 2,000,000. The arm's length price is GHS 1,700,000. GRA adjusts income by 300,000. Extra tax at 25% is GHS 75,000.

```oa-check
name: Adjustment on 300,000
inputs:
  paid: 2000000
  arm: 1700000
steps:
  - adjustment: paid - arm
  - tax: adjustment * 0.25
expected:
  tax: 75000.00
```

**Example 2: is this holder in a controlled relationship?** A foreign investor holds 24% of votes and 30% of income rights. Rights to income reach 25%, so yes. Filing is required even though votes fall short.

```oa-check
name: Control test on the higher of votes or income rights
inputs:
  votes: 24
  income: 30
steps:
  - highest: max(votes, income)
  - gap: highest - 25
expected:
  highest: 30.00
  gap: 5.00
```

## Ask the client first

1. Group chart and ownership percentages.
2. Every related-party flow in the year, by type and value.
3. Year end.
4. Group consolidated revenue, for the Country-by-Country test.
5. Existing Master and Local files.

## Sources

| Source | URL | Read on |
|---|---|---|
| Transfer Pricing Regulations, 2020 (L.I. 2412); regs 11 to 14, 16, 17 read | https://gra.gov.gh/wp-content/uploads/2023/12/Transfer-Pricing-Regulations-2020-LI-24121-_231207_142107.pdf | 2026-11-01 |
| Income Tax Act, 2015 (Act 896), OCR of scan; s.31 read | https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf | 2026-11-01 |
| Income Tax (Amendment) Act, 2023 (Act 1094), whole act | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf | 2026-11-01 |
| GRA, Transfer Pricing page (still names the repealed L.I. 2188), page read in full | https://gra.gov.gh/domestic-tax/transfer-pricing/ | 2026-11-01 |
| GRA, Transfer Pricing Return form, headings read | https://gra.gov.gh/wp-content/uploads/2022/06/Transfer-Pricing-Return-Form.pdf | 2026-11-01 |
| Revenue Administration Act, 2016 (Act 915); ss 27 to 30, 46, 47, 70 to 73 read | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf | 2026-11-01 |

Not yet confirmed: (1) Whether the GHS 2.9 billion figure has changed since 2020. (2) Second Schedule safe harbour ranges were not read in detail. (3) Any exemption from the return itself for small transactions; reg 14 covers documentation only.

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
