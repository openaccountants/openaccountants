---
name: ws-income-tax
description: "Samoa personal income tax for 2026: source-cited rules, conditions, filing boundaries and recomputing cases. Not yet approved by an accountant."
jurisdiction: WS
tax_year: 2026
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
category: international
version: 0.2
---

# Samoa Personal Income Tax v0.2

> **General reference only.** This skill supports AI-assisted working papers. It is not approval to file, pay or take a tax position for a particular person. Obtain qualified local review of the facts, applicable law and filing instructions.

## Who this applies to

Ordinary individual and sole-trader income tax in the Independent State of Samoa for 2026. Salary and wage income has a separate final PAYE computation; load [payroll](ws-payroll-social.md). A person’s residence, source and income classification come before the bands. [section 6](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 9](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

Resident if the individual has a home in Samoa during the year; is present for at least 183 days in aggregate in any 12-month period commencing or ending in that tax year; or is a Samoan citizen who is an officer or employee of Government or a statutory authority. Arrival/departure part-year rules apply where preceding/following-year residence differs. The old domicile/permanent-abode formulation was not the Act’s test. [section 6](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

## Rates, bands and thresholds

| Item | Rule or amount | Official source |
|---|---|---|
| First band | WST 0-15,000: 0% income tax (in words on the page: nil). This is an ordinary annual taxable-income band, not an exemption from all gross withholding. | [Schedule 1 paragraphs 1-2](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf) |

| Next band | WST 15,001-25,000: 20% on the slice above WST 15,000. | [Schedule 1 paragraphs 1-2](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf) |

| Top band | Above WST 25,000: 27% on the excess; WST 2,000 tax on the preceding taxable band is derived. | [Schedule 1 paragraphs 1-2](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf) |

| Historical threshold | The Ministry records WST 12,000 rising to WST 15,000 from 1 January 2018; use the current band, not the old amount. | [Company Tax and Small Business Tax](https://revenue.gov.ws/rates/) |

## The base

Taxable income is assessable income less allowable deductions. Residents generally include worldwide income; non-residents include Samoa-source amounts. Exempt income and income separately taxed under the final-tax regimes are excluded. Apply the source rules to employment, business/PE activity, property and payer-based amounts, rather than a bank-account location. [section 13](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 14](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 7](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

Allow only expenditure on revenue account incurred in producing assessable income, and other deductions the Act permits. Private, exempt-income and capital expenditure are not ordinary revenue deductions; employees cannot deduct expenditure against salary/wage income. Capital allowances, losses and special incentives require their own statutory schedules and evidence. [section 18](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 19](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

For nonnegative ordinary taxable income x, compute T(x) = 20% × min(max(x − 15,000, 0), 10,000) + 27% × max(x − 25,000, 0), then apply eligible credits in the statutory order. If there is also salary/wage income w subject to PAYE, the ordinary-income tax is T(x+w) − T(w); do not give the allowance twice or simply credit actual PAYE against T(x+w). [section 9](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [Schedule 1 paragraphs 1-2](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

The Schedule does not deny the ordinary individual bands merely because the individual is non-resident. The old blanket “taxed from the first tala” claim is corrected: classify the payment first. Gross final non-resident withholding is a different regime with its own PE/exempt-income exceptions; load [corporate tax and withholding](ws-corporate-income-tax.md). [section 9](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 10](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [Schedule 1 paragraphs 1-2](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

## Deadlines and filing

The ordinary tax year is the calendar year. File the income tax return within 3 months after year end if liable for income tax or carrying a statutory loss; tax is due on the return’s due date. For the 2026 calendar year this gives 31 March 2027 (derived). IR2 is the sole-trader return. The Ministry currently lists a 2025 IR2 for the 2025-2026 filing cycle; do not relabel it a final 2026 form. [section 2, tax year](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 80](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 82](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [Income Tax Forms, current listing](https://revenue.gov.ws/inland-revenue-services/).

Provisional tax is a prepayment, not extra tax. The statutory starting amount is preceding-year assessed tax after relevant credits, less the specified tax met by withholding; instalments are normally due 31 March, 31 July and 31 October. A Saturday, Sunday or Samoa public holiday moves the due date to the next business day. The third 2026 instalment was due Monday 2 November 2026. Below WST 500, pay the amount on 31 March. New/unassessed businesses must estimate, and a materially lower liability may support a revised estimate. Retain estimates and reconcile payments against final liability. [section 85](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 86](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [Tax Administration Act section 26](https://www.ag.gov.ws/wp-content/uploads/2024/02/Tax-Administration-Act-2012.pdf); [Samoa public holidays calendar](https://mcil.gov.ws/public-holidays-calendar).

## Penalties and interest

| Item | Rule or amount | Official source |
|---|---|---|
| Late return | After 1 month unfiled: WST 300 for a company; WST 100 otherwise. Other missing documents have a separate daily penalty; do not treat that as the return penalty. | [section 48](https://www.ag.gov.ws/wp-content/uploads/2024/02/Tax-Administration-Act-2012.pdf) |

| Late payment | 10% of unpaid tax if still unpaid after 1 month, subject to the statutory extended-date rule; tax excludes penalty. Filing extension alone does not move the payment date. | [section 49](https://www.ag.gov.ws/wp-content/uploads/2024/02/Tax-Administration-Act-2012.pdf); [section 31](https://www.ag.gov.ws/wp-content/uploads/2024/02/Tax-Administration-Act-2012.pdf) |

| Interest | 8.7% prescribed late-payment rate; simple interest from due date to payment, in addition to penalty. Obtain the applicable day-count and account calculation rather than inventing a compounding convention. | [regulation 2, scanned page 2 visually checked](https://revenue.gov.ws/wp-content/uploads/2025/01/Tax-Administration-Late-Payment-Interest-Regulations-2015.pdf); [section 47](https://www.ag.gov.ws/wp-content/uploads/2024/02/Tax-Administration-Act-2012.pdf); [Collection & Enforcement Services FAQ](https://revenue.gov.ws/revenue-faq-2/) |

## Cross-border points

Record the actual home, all travel periods, residence before/after the year and the source of each receipt. Foreign-source exemptions and foreign-tax credits are conditional; this ordinary-income computation does not clear treaty residence, PE attribution, foreign-tax-credit limits, trusts or capital gains. Refer those computations before using a domestic result as the worldwide answer. [section 6](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 7](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 17](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

## Two worked examples that recompute

### Sole trader with ordinary taxable profit

Assume resident, no wages, exemptions, losses or credits, and WST 40,000 of proved taxable profit. The nil band absorbs WST 15,000; the next WST 10,000 gives WST 2,000 and the remaining WST 15,000 gives WST 4,050. Annual income tax is WST 6,050, all results derived.

```oa-check
name: Sole trader with ordinary taxable profit
inputs:
  profit: 40000
steps:
  - middle: min(max(profit - 15000, 0), 10000) * 0.20
  - top: max(profit - 25000, 0) * 0.27
  - tax: middle + top
expected:
  tax: 6050
```

### Business income alongside PAYE wages

Assume WST 20,000 salary/wage income subject to PAYE plus WST 10,000 ordinary taxable business income, with no other adjustments. T(30,000) is WST 3,350 and T(20,000) is WST 1,000, so the tax on business income is WST 2,350, derived. The statutory subtraction uses annual band tax on wages, not actual fortnightly deductions.

```oa-check
name: Business income alongside PAYE wages
inputs:
  wages: 20000
  business: 10000
steps:
  - aggregate: wages + business
  - tax_combined: min(max(aggregate - 15000, 0), 10000) * 0.20 + max(aggregate - 25000, 0) * 0.27
  - tax_wages: min(max(wages - 15000, 0), 10000) * 0.20 + max(wages - 25000, 0) * 0.27
  - business_tax: tax_combined - tax_wages
expected:
  business_tax: 2350
```

## Ask the client first

- Which year, home, travel dates and preceding/following-year residence?
- Which receipts are wages, business, investment, exempt or final-tax income, and where sourced?
- Which expenses, capital assets, losses and credits have supporting records?
- Which provisional payments, withholding certificates, assessments and current return instructions exist?

## Sources

Read on **2026-11-15** for the stated sections. The Attorney General tax consolidations are official texts as at 31 December 2023; current Ministry guidance and the later instruments expressly identified below were checked separately. A recent upload path does not change a document’s printed date.

| Source and scope actually read | URL | Read on |
|---|---|---|
| Read for Schedule 1 paragraphs 1-2; section 10; section 13; section 14; section 17; section 18; section 19; section 6; section 7; section 80; section 82; section 85; section 86; section 9; section 2, tax year | https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf | 2026-11-15 |
| Read for Collection & Enforcement Services FAQ | https://revenue.gov.ws/revenue-faq-2/ | 2026-11-15 |
| Read for Income Tax Forms, current listing | https://revenue.gov.ws/inland-revenue-services/ | 2026-11-15 |
| Read for regulation 2, scanned page 2 visually checked | https://revenue.gov.ws/wp-content/uploads/2025/01/Tax-Administration-Late-Payment-Interest-Regulations-2015.pdf | 2026-11-15 |
| Read for Company Tax and Small Business Tax | https://revenue.gov.ws/rates/ | 2026-11-15 |
| Read for section 31; section 47; section 48; section 49 | https://www.ag.gov.ws/wp-content/uploads/2024/02/Tax-Administration-Act-2012.pdf | 2026-11-15 |
| Read for section 26, non-business-day rule | https://www.ag.gov.ws/wp-content/uploads/2024/02/Tax-Administration-Act-2012.pdf | 2026-11-23 |
| Samoa public holidays calendar, 2026 | https://mcil.gov.ws/public-holidays-calendar | 2026-11-23 |

Not yet confirmed: Final 2026 IR2 and live filing-field mapping; client-specific exemptions, loss/depreciation schedules and foreign-tax-credit/treaty computations. Do not infer an exemption or a non-resident denial of the ordinary bands from the old draft.
