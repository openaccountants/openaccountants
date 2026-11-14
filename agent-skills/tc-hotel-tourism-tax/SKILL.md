---
name: tc-hotel-tourism-tax
description: "Turks and Caicos hotel, restaurant and tourism tax for 2026, the Islands' main consumption tax in place of VAT. Covers the 12% rate on accommodation, vacation rentals, designated restaurants and bars and prescribed tourism services, registration 30 days before trading, designation criteria, the USD 4,000 monthly exemption for independent tourism providers on application, the 21st-of-the-month due date, the 20% penalty and 1.5% monthly interest, nil returns, records, automated remittance forms, and the other sales-type taxes (communications, financial services, insurance premium, vehicle hire). Trigger phrases include Turks and Caicos hotel tax, HRTT, TCI tourism tax, TCI VAT."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/tc-hotel-tourism-tax"
  jurisdiction: "TC"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Turks and Caicos hotel and tourism tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Businesses in the Turks and Caicos Islands that supply accommodation (hotels, resorts, villa and condo owners, vacation rentals), meals and drinks at hotel bars and restaurants or designated restaurants and bars, and prescribed tourism services, under the Hotel, Restaurant and Tourism Taxation Ordinance, administered by the Revenue Department (Inland Revenue Department, Ministry of Finance). Amounts are US dollars.

The Islands have no VAT, no general sales tax and no income tax. The Revenue Department administers five sales-type taxes, on tourism, financial services, telecommunications, insurance premiums and vehicle hire, plus business licences ([Revenue streams](https://gov.tc/revenue/streams)). This skill owns the hotel and tourism tax and lists the others.

Prescribed tourism services include tour operator and tourist guide services, camping and caravan sites, camping equipment rental, watersports and watersports or beach equipment rental, sports fishing, sightseeing excursions (including by aircraft or helicopter), non-motorised land and air transport equipment rental, and parasailing, parachuting and zip lining ([Hotel and tourism tax](https://www.gov.tc/revenue/htt)).

## Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Hotel and tourism tax | 12% on accommodation, vacation rentals, designated meals and drinks and prescribed tourism services | [Hotel and tourism tax](https://www.gov.tc/revenue/htt) |
| Exemption threshold, independent tourism service providers | Turnover below USD 4,000 a month, on written application with sufficient evidence; all providers are first registered to collect | same |
| Late payment penalty | 20% of the tax overdue, immediately after the 21st | same |
| Late payment interest | 1.5% a month of the tax while it remains outstanding | same |
| Communications tax (telecom companies, internet service providers) | 12% | [Revenue streams](https://gov.tc/revenue/streams) |
| Domestic financial services sales tax (financial institutions, money transfer operators, on financial services fees) | 12% | same |
| Insurance premium sales tax (domestic business except life and health) | 2.5% | same |
| Vehicle hire stamp duty (motor vehicle and scooter rental) | 12% | same |
| Business licence | Varies | same |

## The base

- Tax is charged on the charge for the taxable supply. If a price is stated as including the 12% tax and nothing else, the tax is 12/112 of it; applying 12% to an inclusive price overstates the tax.
- Bars and restaurants attached to a hotel are registered at once. Other bars and restaurants may be designated by the Department on size, location, seating capacity, monthly or annual turnover, or whether the customers are largely tourists.
- A business licence alone does not make a supply taxable or exempt; check registration, designation and any written exemption, and keep the effective date with the records.

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Register | 30 days before operations begin, on the HRTT registration form; registrants get an advisory session | [Hotel and tourism tax](https://www.gov.tc/revenue/htt) |
| File and pay | On or before the 21st of each month for the month before, with the remittance form for the period | same |
| Weekend or holiday | Pay on the last working day before the weekend or holiday | [Revenue FAQ](https://www.gov.tc/revenue/faqs) |
| Remittance forms | Generated and emailed automatically since 1 August 2026; keep contact details current with the Department | [IRD notice](https://www.gov.tc/revenue/news/inland-revenue-department-introduces-automated-monthly-remittance-forms) |
| Seasonal closure | File a nil return and give written notice of the closure period | [Hotel and tourism tax](https://www.gov.tc/revenue/htt) |
| Changes | Notify the Department of any change to registration details | same |

## Penalties and interest

Missing the 21st brings an immediate 20% penalty on the overdue tax and interest of 1.5% a month on the tax for as long as it is unpaid ([Hotel and tourism tax](https://www.gov.tc/revenue/htt)). Tax is self-assessed and returns are subject to audit.

## Cross-border points

- A non-resident owner letting a villa or condo is a taxpayer like any other accommodation provider.
- Online booking platforms: who collects and remits for a platform booking is not confirmed here; the owner remains registered.
- The Revenue Department's list of taxes has no income tax, so the rental profit itself is not taxed in the Islands; the owner's home country may tax it.

## Two worked examples that recompute

### Example 1: a price that includes the tax

A guest pays USD 1,120 for a room, stated to include the 12% hotel tax and nothing else. The base is 1,120 / 1.12 = 1,000 and the tax 120. Applying 12% to 1,120 would give 134.40, overstating the tax by 14.40.

```oa-check
name: TCI hotel tax extracted from a tax-inclusive price
inputs:
  inclusive: 1120
  rate: 0.12
steps:
  - base: inclusive / (1 + rate)
  - tax: inclusive - base
  - wrong_tax: inclusive * rate
  - overstatement: wrong_tax - tax
expected:
  base: 1000
  tax: 120
  wrong_tax: 134.40
  overstatement: 14.40
```

### Example 2 (decision): pay on time or two months late

A villa owner owes USD 5,000 for October, due 21 November. Paid on time the cost is 5,000. Paid two months late it is 5,000 plus the 20% penalty (1,000) plus 1.5% interest for two months (150), total 6,150. Borrowing to pay on time is cheaper unless the loan costs more than 1,150 on 5,000 over two months.

```oa-check
name: TCI hotel tax paid on time against two months late
inputs:
  tax: 5000
  months_late: 2
steps:
  - penalty: tax * 0.20
  - interest: tax * 0.015 * months_late
  - late_total: tax + penalty + interest
  - cost_of_delay: late_total - tax
expected:
  penalty: 1000
  interest: 150
  late_total: 6150
  cost_of_delay: 1150
```

## Ask the client first

1. What exactly is supplied: rooms, a villa, meals and drinks, a tour or another listed service?
2. Is the business registered for the tax, designated, or exempt in writing, and from when?
3. Are prices quoted before or including the tax?
4. Monthly turnover (for the USD 4,000 independent provider exemption).
5. Is the business seasonal, and were nil returns filed for closed months?

## Sources

| Source | URL | Read on |
|---|---|---|
| Revenue Department, hotel and tourism tax page: read for the 12% rate, taxable services, registration, designation, the USD 4,000 exemption, the 21st, the penalty and interest, nil returns and the seven-year record rule | https://www.gov.tc/revenue/htt | 2026-11-14 |
| Revenue Department, major revenue streams: read for the five sales-type taxes and their rates | https://gov.tc/revenue/streams | 2026-11-14 |
| Revenue Department, FAQ: read for the weekend and holiday rule and the five-year record statement | https://www.gov.tc/revenue/faqs | 2026-11-14 |
| IRD notice on automated monthly remittance forms: read for the start on 1 August 2026 | https://www.gov.tc/revenue/news/inland-revenue-department-introduces-automated-monthly-remittance-forms | 2026-11-14 |

Not yet confirmed: the record-keeping period (the tax page says seven years, the FAQ five; keep seven); whether interest compounds (the example treats 1.5% a month as simple, on the tax); the text of the Hotel, Restaurant and Tourism Taxation Ordinance itself (not opened; the Revenue homepage link to it opened a business licence consultation) and the Hotel, Restaurant, Tourism (Taxation) (Exemption) Regulations 2024 (LN 13 and 18 of 2024, listed by the Attorney General's Chambers, not opened); how platform bookings are handled.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `tc-hotel-tourism-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/tc-hotel-tourism-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
