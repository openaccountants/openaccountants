---
name: kz-corporate-income-tax
description: "Kazakhstan 2026 corporate income tax: sector rates, documented base, losses, advances, annual filing and non-resident payments."
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax

version: 0.1
type: computation
category: international
---

# Kazakhstan corporate income tax v0.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Resident legal entities and non-residents carrying on business through a Kazakhstan permanent establishment. Confirm special-regime status first: income taxed under the simplified declaration does not also enter the ordinary CIT declaration (arts. 233–234 and 359). This file covers the ordinary computation, with specialist sectors and cross-border payments identified separately.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| Ordinary taxable income | 20% (art. 357(2)(5)) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Own agricultural/aquaculture production, processing and sale by qualifying producers | 3%; qualifying agricultural cooperative other activity 6% (art. 357(2)(1)–(2)) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Qualifying social-sector organisations, excluding art. 330 organisations | 5% during 2026; 10% from 2027 (art. 357(2)(3)) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Banking except qualifying business lending; casino, slot-machine hall, totalisator and bookmaker activity | 25% (art. 357(2)(4)); classify income separately | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Non-resident PE net income after CIT | 15% additional net-income tax, subject to applicable treaty relief (arts. 357(1)(4), 689) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Ordinary business loss | Carry forward sequentially through the following 10 tax periods; special exceptions in art. 339 (figure in words on the page) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| CIT advance-payment size exception | Adjusted annual income in the period preceding the previous period no more than 600,000 МРП of that historical year; not the current-year МРП (art. 348) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Art. 236 computes aggregate annual income minus exclusions, plus/minus income adjustments, minus allowable deductions, plus/minus deduction adjustments. Apply taxable-income reductions and eligible losses before tax; reconcile accounting profit to tax. Document business purpose, capital/revenue distinction, disallowed items and loss origin. Art. 339 does not carry forward losses of a bank subsidiary acquiring its parent’s doubtful/bad assets; special CFC and reorganisation cases require their own analysis.

Advance payments are not determined by an undefined “large taxpayer” label. Art. 348 also provides status-specific exceptions, including qualifying new entities for the registration and following period, with reorganisation exceptions. Digital-asset taxpayers cannot rely on the listed advance-payment exceptions. Calculate the actual schedule under arts. 349–350 if liable. Purchases from simplified-regime suppliers need the art. 286(16) deduction restriction considered; do not infer deductibility from an invoice alone.

## Deadlines and filing

Ordinary annual CIT declaration: by 31 March following the reporting year (art. 359). Final payment: within 10 calendar days after the filing deadline, with credit for advances already paid (art. 347). Use the current electronic CIT declaration and relevant appendices in the taxpayer cabinet, reconcile the tax base, advances and losses, retain acceptance and payment reference. Special CFC supplemental and liquidation deadlines are different; refer rather than reusing the ordinary date.

## Penalties and interest

Determine administrative filing/understatement penalties and late-payment interest separately. No numeric sanction is supplied without the operative current provision and taxpayer category.

## Cross-border points

Under art. 682, non-resident source withholding is generally 20%, with dividends/capital gains/royalties generally 15%; loan/debt-security interest is 10%. Qualifying direct or indirect ownership of at least 25% permits dividend rates of 5% through 230,000 МРП and 15% on the excess (ownership figure in words on the page). Other interest is not automatically the loan-interest rate. A recipient in a preferential-tax state is subject to 20%. Apply treaty relief only after checking entitlement and residence documentation under arts. 698 and 702–706. PE net-income tax is separate from source withholding; treaty reduction is not automatic.

## Two worked examples that recompute

Case 1: hypothetical ordinary income KZT 50,000,000 less allowable deductions KZT 30,000,000 and available ordinary loss KZT 5,000,000 gives tax KZT 3,000,000.

```oa-check
name: Ordinary CIT with eligible loss
inputs:
  income: 50000000
  deductions: 30000000
  loss: 5000000
steps:
  - base: max(income - deductions - loss, 0)
  - tax: base * 0.20
expected:
  base: 15000000
  tax: 3000000
```

Case 2: for identical hypothetical KZT 10,000,000 taxable income, qualifying own agricultural production gives KZT 300,000, while an ordinary trading activity gives KZT 2,000,000. The decision turns on the activity and producer conditions, not the company name.

```oa-check
name: Activity classification decides CIT rate
inputs:
  base: 10000000
steps:
  - producer_tax: base * 0.03
  - ordinary_tax: base * 0.20
  - difference: ordinary_tax - producer_tax
expected:
  producer_tax: 300000
  ordinary_tax: 2000000
  difference: 1700000
```

## Ask the client first

- Legal form, residence, PE and tax regime?
- Activities and separately attributable income, including banking/agriculture/social sector/digital assets?
- Reconciled income, documented deductions and loss history?
- Historical annual income for advance-payment status and payments made?
- Foreign recipients, payment type, ownership, beneficial entitlement and treaty documents?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 233–236, 286(16), 339, 347–350, 357, 359, 682, 689 and treaty documentation provisions | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |

Not yet confirmed: Detailed banking allocation, sector qualification, CFC/reorganisation computations, specific treaty rates, current declaration boxes and numeric penalties. The old agricultural 10% and blanket non-resident interest 15% are not current instructions.
