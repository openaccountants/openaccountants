---
name: trinidad-vat
description: >
  Trinidad and Tobago Value Added Tax for 2026, for registered persons preparing
  or reviewing VAT returns. Covers the 12.5% standard rate, zero-rating and the
  exempt services in Schedule 1 of the VAT Act, the TT$600,000 registration
  threshold (from 1 January 2023), tax periods of two months, the return due
  within 25 days after the period, the 8% penalty and 2% a month interest on late
  payment, refund interest, tax invoice contents, time of supply, reverse charge
  on imported services and record keeping for six years. Trigger on Trinidad VAT,
  T&T VAT, VAT return Trinidad, BIR VAT, 12.5% VAT Trinidad. Built from the VAT
  Act and IRD pages; not reviewed by an accountant.
version: 1.0
jurisdiction: TT
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: vat-gst
type: situation-rules
---

# Trinidad and Tobago VAT v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Persons carrying on a business in Trinidad and Tobago and making commercial supplies in 2026, under the Value Added Tax Act, Chap. 75:06, administered by the Board of Inland Revenue (IRD). Amounts are TT$.

- **In:** registered persons (sole proprietors, partnerships, companies) filing periodic VAT returns.
- **Out (refer):** upstream petroleum contracts and production sharing contracts, VAT bonds and remissions, duty-free concession imports, sale of a going concern.

Before classifying anything, know: the BIR file number and VAT registration number, the tax period, the sector (energy, financial services, manufacturing), whether exempt supplies are made, imports, and any credit brought forward. If registration and period are unknown, stop.

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| Standard rate | 12.5% | Goods and services not zero-rated or exempt | IRD, VAT page: https://www.ird.gov.tt/VAT |
| Registration threshold | Commercial supplies over TT$600,000 in any 12-month period, or expected to exceed it | From 1 January 2023; register by applying with Forms A, B or C | same |
| Below-threshold test in the Act | Not required to register where supplies in the past 12 months and the next 12 months are not more than six hundred thousand dollars | VAT Act s. 19 as consolidated | VAT Act, Chap. 75:06 (IRD 2024 consolidation): https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.06-Value-Added-Tax-Act--2024.pdf |
| Tax period | Two months (category B), or one month then two months (category A), or periods the Board sets (category C) | The Board may move a person between categories | same |
| Return due | Within 25 days after the end of the tax period | s. 31(2); IRD says by the 25th day of the following month | same |
| Late payment | Penalty of 8% of the amount outstanding plus interest of 2% a month or part month | s. 54(1); the Board may reduce or waive | same |
| Late refund | Interest of 1% a month or part month after six months | Refund not paid within six months of the later of the due date and the filing date | same |
| Records | Six years, or three years from filing, whichever is later | In English, in TT currency, at the principal place of business | IRD, VAT page: https://www.ird.gov.tt/VAT |
| Exempt services | Medical, dental, hospital, optical and paramedical services; bus and taxi services; approved education; real estate brokerage; residential rental; hotel stays over 30 days; public postal services; betting and lotteries; financial services | Schedule 1 | VAT Act, Chap. 75:06: https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.06-Value-Added-Tax-Act--2024.pdf |

## The base

### Supplies

- **Value of a supply** at arm's length is the consideration excluding VAT; between associated persons, and for barter, open market value.
- **Time of supply** is the earliest of the invoice date, the payment date, and the date the goods are made available or the services supplied.
- **Zero-rated** supplies (Schedule 2) carry 0% with input credit; exports are zero-rated. IRD publishes a list of zero-rated food items.
- **Exempt** supplies (Schedule 1) carry no VAT and no input credit.
- **Out of scope**: salaries, PAYE, NIS, health surcharge, loan repayments, dividends.

### Tax invoice (IRD)

The words "Tax Invoice"; serial number and date; supplier name, address and VAT registration number; recipient name and address; full description; VAT-exclusive figure; VAT; total value. Invoices are not attached to the return but must be produced on request.

### Input tax

- Registered persons making taxable supplies recover input tax on business purchases and imports; non-registered persons and persons making only exempt supplies recover none.
- Mixed taxable and exempt supplies: directly attributable input tax follows the supply; common input tax is apportioned by the taxable share (flag for review).
- Imported services: self-assess 12.5% and claim the input tax if used for taxable supplies (net nil for a fully taxable business).
- Restrictions on motor cars, entertainment and club subscriptions given by the earlier version: see Not yet confirmed; treat as no credit until checked.

### Classification by sector (kept from the earlier version, to review)

| Item | Treatment |
|---|---|
| Interest, foreign exchange, lending, life insurance, securities | Exempt (financial services, Schedule 1 item 10) |
| Bank fees and commissions closely related to intermediation | Check whether within the financial services definition |
| Residential rental | Exempt; commercial rental 12.5% |
| Hotel accommodation | Exempt only for stays over 30 days |
| Construction services and materials | 12.5% |
| Exports, including LNG and petrochemical exports | 0% |
| Services to energy companies | 12.5% |
| CARICOM imports and services | Same as any import: VAT at customs, reverse charge on services |
| Credit notes | Reduce output tax in the period |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 12.5% |
| Unknown VAT status of a purchase | No credit |
| Unknown business-use share | No credit |
| Motor car, entertainment, club subscription | No credit until reviewed |

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | Apply for registration (Form AOI 002 and Forms A, B or C) with ID, BIR numbers and evidence of trading | When supplies exceed or are expected to exceed TT$600,000 |
| 2 | Display the VAT Registration Certificate; issue tax invoices | From registration |
| 3 | File the VAT return for each tax period (two months for most) through e-Tax, signed | Within 25 days after the period (Jan-Feb period by 25 March) |
| 4 | Pay the VAT due with the return | Same date |
| 5 | Deregister (Forms VAT 13 or 14) and return the certificate when no longer liable | On cessation |

## Penalties and interest

- Late payment: 8% penalty plus 2% a month (s. 54). Failure to furnish a return lets the Board assess (s. 39). Offences under the Act carry fines up to TT$30,000 and imprisonment for two years for the most serious offences.

## Cross-border points

- Imports: VAT at customs, creditable for registered persons.
- Imported services: reverse charge at 12.5%.
- Exports of goods and services consumed abroad: zero-rated with evidence; place of supply rules decide digital services (flag for review).

## Two worked examples that recompute

### Example 1: Two-month return, late by two months

Standard-rated sales TT$800,000 give output VAT TT$100,000; input VAT TT$40,000; VAT due TT$60,000. Paid two months late: penalty 8% = TT$4,800, interest 2% x 2 = TT$2,400, total TT$67,200.

```oa-check
name: TT VAT 2026 bimonthly return paid two months late
inputs:
  sales: 800000
  input_vat: 40000
  months_late: 2
steps:
  - output_vat: sales * 0.125
  - vat_due: output_vat - input_vat
  - penalty: vat_due * 0.08
  - interest: vat_due * 0.02 * months_late
  - total: vat_due + penalty + interest
expected:
  output_vat: 100000
  vat_due: 60000
  penalty: 4800
  interest: 2400
  total: 67200
```

### Example 2: Register or not? Supplies TT$550,000 or TT$650,000 in 12 months

TT$550,000 is TT$50,000 under the TT$600,000 threshold: no duty to register if the next 12 months will also stay under. TT$650,000 is TT$50,000 over: registration is required. Monthly averages are TT$45,833.33 and TT$54,166.67 against TT$50,000.

```oa-check
name: TT VAT 2026 registration threshold both ways
inputs:
  threshold: 600000
  low: 550000
  high: 650000
steps:
  - gap_low: threshold - low
  - excess_high: high - threshold
  - monthly_low: round(low / 12, 2)
  - monthly_high: round(high / 12, 2)
expected:
  gap_low: 50000
  excess_high: 50000
  monthly_low: 45833.33
  monthly_high: 54166.67
```

### Short cases kept from the earlier version

- Local office furniture TT$11,250 including VAT TT$1,250: input credit TT$1,250.
- Export to Barbados TT$50,000: zero-rated; inputs recoverable.
- UK legal advice TT$45,000, no VAT charged: self-assess TT$5,625 and claim TT$5,625; net nil.
- Life insurance premiums TT$200,000: exempt; related inputs not recoverable.
- 80% taxable, 20% exempt, common VAT TT$10,000: recover TT$8,000 (flag for review).

## Ask the client first

1. BIR and VAT registration numbers, tax period category and the period being filed.
2. Sales split: standard-rated, zero-rated (exports, listed food), exempt.
3. Imports (customs entries) and imported services.
4. Any exempt supplies, and purchases used for both.
5. Motor cars, entertainment, club costs in the period.
6. Credit brought forward, or refunds outstanding.

## Sources

| Source | URL | Read on |
|---|---|---|
| IRD, Value Added Tax page: read for the 12.5% rate, the TT$600,000 threshold from 1 January 2023, registration documents, records, tax invoice contents, value and time of supply and the 25th-day return date | https://www.ird.gov.tt/VAT | 2026-11-14 |
| VAT Act, Chap. 75:06 (IRD 2024 consolidation): read for the registration test, tax periods, s. 31 returns, s. 39 assessments, s. 54 penalty and interest, refund interest and Schedule 1 | https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.06-Value-Added-Tax-Act--2024.pdf | 2026-11-14 |
| Ministry of Finance, Budget Statement FY2026: read for VAT measures (review of the VAT system, VAT on luxury electric cars over TT$400,000 CIF) | https://www.finance.gov.tt/wp-content/uploads/2025/10/Budget-Statement-FY-2026-2.pdf | 2026-11-14 |

Not yet confirmed: the input tax restrictions on motor cars, entertainment and club subscriptions and their exceptions (earlier version); the full Schedule 2 zero-rated list (earlier version: basic food, agricultural inputs, prescription drugs, crude oil and gas upstream, books and newspapers, piped water); the earlier version's return box numbers 1 to 16 (no form read); the earlier version's late filing penalty of TT$100 a day and records fine of TT$10,000; whether FY2026 budget VAT proposals were enacted; the refund processing time.
