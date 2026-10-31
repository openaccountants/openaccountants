---
name: az-tax-overview
description: 'Use this overview to route 2026 Azerbaijan tax questions to the dedicated individual income, corporate profit, VAT, payroll, social-contribution, transfer-pricing and cross-border skills. It identifies ordinary starting rates, taxpayer types, reporting cycles and the need to separate tax bases and registrations. Trigger on Azerbaijan tax overview, tax system, company tax, entrepreneur tax, salary taxes, VAT, foreign payments and which Azerbaijan skill applies. It does not replace the detailed computation or cover all special schemes. Read the pack README and relevant skill for explicit missing calculations. Checked against the law (tier 2); no accountant has signed it off.'
jurisdiction: AZ
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.1
category: international
---

# Azerbaijan Tax Overview v0.1

> **Checked against the law.** Tax year 2026. Figures independently re-checked against the official sources on 31 October 2026. General reference for working papers; a qualified professional must review the facts and filing position. No accountant has signed this skill off.

## Who this applies to

A routing overview for 2026 Azerbaijan tax working papers. Use it to select the detailed skill, not to finish a return. The State Tax Service administers the Tax Code; separate statutes govern social, medical and unemployment insurance. Individuals, enterprises and non-resident PEs require different residence, source and computation tests under Tax Code arts. 13, 19, 95–105. The pack README declares the incomplete groups and calculations.

## Rates, bands and thresholds

| Starting point | Ordinary amount | Tax year | Official source |
|---|---|---|---|
| Individual entrepreneur profit | 20% | 2026 | [Tax Code art. 101.3](https://e-qanun.az/frameworks/46/f_46948.html) |
| Corporate/PE profit | 20% | 2026 | [Tax Code art. 105.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| VAT | 18% standard | 2026 | [Tax Code art. 173.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| VAT rolling domestic threshold | Above 200,000 taxable operations in 12 months, with separate triggers/weighting | 2026 | [Tax Code art. 155.1–155.1-1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Ordinary simplified tax | 2% of taxable receipts if eligible | 2026 | [Tax Code art. 218–220](https://e-qanun.az/frameworks/46/f_46948.html) |
| Private non-oil salary PIT | 3% / 10% / 14%, progressive monthly schedule | 1 Jan–31 Dec 2026 | [Tax Code art. 101.1-1.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Standard salary PIT | 14% through 2,500; 25% marginal above | 2026 | [Tax Code art. 101.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Ordinary non-PE source-service withholding | 10%, subject to exact source/category/treaty tests | 2026 | [Tax Code art. 125.1.5](https://e-qanun.az/frameworks/46/f_46948.html) |

## The base

Use azerbaijan-income-tax for individuals, including business profit, passive income and ordinary simplified tax. Use az-corporate-income-tax for enterprises and PE profit. Use azerbaijan-payroll for employment PIT/net pay and azerbaijan-social-contributions for distinct employee/employer and self-employed insurance bases. Use azerbaijan-vat for domestic supplies, imports, exports, input credit and reverse charge. Use azerbaijan-transfer-pricing for controlled transactions and azerbaijan-cross-border for source, residence, PE, treaties, foreign-tax credit and CFC screening.

The 2025 private non-oil salary holiday is not the 2026 schedule. The 2026 medical and employer-social bands also differ from the old payroll prose. Low turnover does not by itself establish simplified-tax eligibility; art. 218 contains exclusions and tests. A tax exemption does not by itself exempt social/medical payments or VAT. The detailed skills provide the computational conditions and dates. No accounting-pack formation/optimisation claim overrides the reverified tax skills; those two files remain a separate milestone with recorded conflicts.

## Deadlines and filing

Ordinary annual income/profit returns and settlement are due by 31 March following the tax year (arts. 149.2, 152.1). Advances are due within 15 days after each quarter under art. 151. VAT returns/payments are monthly by the following month's 20th under arts. 177–178. Payroll PIT is monthly by the next month's 20th, but the unified wage report is quarterly by the following month's 20th under art. 150.3. Contributions have their own monthly payment dates, generally the following month's 15th under the insurance statutes. Non-wage withholding has different quarterly dates; use the cross-border skill. File through the State Tax Service's electronic services and check event-triggered returns/registration in the detailed skill.

## Penalties and interest

Under [Tax Code art. 57.1](https://e-qanun.az/frameworks/46/f_46948.html), failure without grounds to submit a required return for a period with taxable or exempt operations or tax objects attracts AZN 40. Under [Tax Code art. 58.1](https://e-qanun.az/frameworks/46/f_46948.html), an understated or evaded tax amount attracts a 50% financial sanction, excluding additional tax assessed by a desk audit; the horizontal-monitoring case in art. 58.1-1 uses 25%. Under [Tax Code art. 59.1–59.2](https://e-qanun.az/frameworks/46/f_46948.html), late tax or advance payments bear 0.1% per overdue day, for at most one year. For additional tax identified by field audit or horizontal monitoring, interest starts on the assessment date under art. 59.2. Apply the facts and procedural exceptions before assessing a sanction.

## Cross-border points

Residents and non-residents do not share the same income scope. Check residence, domestic source, PE and the actual treaty before calculating a tax. VAT reverse charge and contribution coverage are separate. The cross-border skill expressly leaves certain CFC, preferential-jurisdiction and exit-asset calculations incomplete; no general tax-free relocation conclusion is supported.

## Two worked examples that recompute

### Route to ordinary company profit tax

Assume an ordinary enterprise with 300,000 taxable revenue and 200,000 fully deductible costs, no relief, depreciation, losses or credits. Tax is (300,000−200,000) × 20% = 20,000. Continue in the corporate skill for the complete reconciliation (arts. 104, 105).

```oa-check
name: AZ overview ordinary company 2026
inputs:
  revenue: 300000
  deductible_cost: 200000
steps:
  - profit: revenue-deductible_cost
  - tax: profit*0.20
expected:
  profit: 100000
  tax: 20000
```

### Route a VAT-inclusive receipt

An ordinary fully standard-rated receipt of 1,180 includes VAT. VAT-exclusive value is 1,000 and VAT is 180. Continue in the VAT skill for tax point, input credit and return treatment; do not multiply the inclusive price directly by 18% (arts. 161, 173).

```oa-check
name: AZ overview VAT-inclusive receipt 2026
inputs:
  gross: 1180
steps:
  - net: gross/1.18
  - vat: gross-net
expected:
  net: 1000
  vat: 180
```

## Ask the client first

- Is the taxpayer an individual, company, PE or payer acting as tax agent?
- What year/event dates, residence and source facts apply?
- What activities, customer mix, gross amounts, costs and registration/election documents exist?
- Are there employees, foreign counterparties, related parties or ownership changes?
- Which detailed skill applies, and does its stated gap block this calculation?

## Sources

| Source and provisions read | Official URL | Read on |
|---|---|---|
| Tax Code, arts. 13–19, 57–59, 95–105, 125, 149–152, 161, 173, 177–178, 218–220 | https://e-qanun.az/frameworks/46/f_46948.html | 2026-10-31 |
| Social Insurance Law, art. 14.6 | https://frameworks.e-qanun.az/3/f_3813.html | 2026-10-31 |
| Medical Insurance Law, art. 15-11 | https://frameworks.e-qanun.az/0/f_80.html | 2026-10-31 |
| Unemployment Insurance Law, art. 10.3 | https://frameworks.e-qanun.az/36/f_36310.html | 2026-10-31 |

Not yet confirmed: See the domain-specific Not yet confirmed lines and pack partial flags; this overview does not close those gaps.

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
