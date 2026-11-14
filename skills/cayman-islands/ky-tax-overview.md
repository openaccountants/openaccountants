---
name: ky-tax-overview
description: >
  Overview of Cayman Islands taxation for 2026. There is no income tax, no
  corporate tax, no capital gains tax, no VAT or sales tax, no payroll tax and
  no withholding tax. What exists is import duty (22% on most goods under the
  Customs Tariff Act 2026 Revision), stamp duty on land transfers (7.5%, and
  10% from 1 January 2026 where the price is CI$2 million or more, with
  first-time and second-home reliefs for Caymanians), the 13% tourist
  accommodation tax, mandatory private pensions and health insurance for
  employees, work permit and government registry fees, and economic
  substance reporting. Trigger on Cayman tax, is Cayman tax free, Cayman
  stamp duty, Cayman Islands taxes, moving to Cayman. Built from Cayman
  legislation; not reviewed by an accountant.
version: 1.0
jurisdiction: KY
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: situation-rules
---

# Cayman Islands tax overview

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking how the Cayman Islands taxes people, businesses or property in 2026. Currency: Cayman Islands dollar (CI$); the General Registry converts fees at US$1 = CI$0.82. There is no tax year for income because there is no income tax.

**No direct taxes.** The current legislation list has no income tax, corporate tax, capital gains tax, payroll tax, VAT, sales tax, estate tax or minimum top-up tax Act. There is no tax return to file. Do not compute any of these. An exempted company (or any company in the national interest) can obtain a government undertaking that any future tax on profits, income, gains or appreciation will not apply to it, for up to 30 years (Tax Concessions Act s. 6).

**What exists:** import duty, stamp duty, tourist accommodation tax, government and registry fees, work permit fees, and the employer duties to provide pensions and health insurance.

| Topic | Skill |
|---|---|
| Import duty, accommodation tax, "is there VAT" | `ky-vat-gst` |
| Pensions, health insurance, minimum wage | `ky-payroll-social` |
| Companies: no tax, tax undertaking, economic substance | `ky-corporate-income-tax` |
| Forming an entity, registry fees | `ky-company-formation` |
| Stamp duty on land | This skill |

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| Income, corporate, capital gains, payroll, VAT, estate tax | None | No such Act in the current legislation list (letters searched 14 Nov 2026) | Cayman legislation, current by title: https://legislation.gov.ky/cms/legislation/current/by-title.html |
| Tax undertaking | Up to 30 years from approval | Exempted company or company in the national interest; covers future taxes on profits, income, gains, appreciation, and may cover estate duty and withholding on dividends and interest | Tax Concessions Act (2018 Revision), s. 6: https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0164/1964-0164_2018%20Revision.pdf |
| Stamp duty, conveyance or transfer of land | 7.5% of the consideration | Consideration under CI$2,000,000 | Stamp Duty (Rates of Duty) (No. 2) Regulations 2025, SL 63 of 2025, in force 1 January 2026: https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf |
| Stamp duty, consideration CI$2,000,000 or more | 10% of the consideration | Also applies at the top of each Caymanian relief band | same |
| Caymanian first property, land with a building | Nil to CI$550,000; 3.75% on the excess over CI$550,000 if up to CI$650,000; 7.5% above CI$650,000 and under CI$2 million; 10% from CI$2 million | One Caymanian buyer | Stamp Duty (Rates of Duty) Regulations 2025, SL 3 of 2025, para (10): https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0003/2025-0003_SL%203%20of%202025.pdf |
| Caymanian first property, land without a building | Nil to CI$250,000; 3.75% on the excess over CI$250,000 if up to CI$350,000; 7.5% above | One Caymanian buyer | same |
| Two to ten Caymanian first-time buyers | With a building: nil to CI$600,000, 3.75% on the excess to CI$700,000, then 7.5%; without: nil to CI$450,000, 3.75% on the excess to CI$550,000, then 7.5% | Para (11) | same |
| Caymanian second property | 3.75% of the consideration to CI$600,000 (building) or CI$300,000 (land); 7.5% above | One buyer, para (11A); two to ten buyers CI$700,000 and CI$550,000, para (11B) | same |
| Tourist accommodation tax | 13% of the charges for each tourist | Timeshare owners and their guests: US$10 a room a day instead | Tourist Accommodation (Taxation) Act (2013 Revision), s. 3: https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0168/1964-0168_2013%20Revision.pdf |
| Import duty, most goods | 22% | Customs Tariff Act Schedule; other lines at 0%, 12%, 17%, 27%, 42% or specific rates | Customs Tariff Act (2026 Revision): https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2012/2012-0001/2012-0001_2026%20Revision.pdf |
| Employer pension | At least 5% of earnings to CI$87,000; employee up to 5% | See `ky-payroll-social` | National Pensions Act (2024 Revision), ss. 2 and 47(3): https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1996/1996-0010/1996-0010_2024%20Revision.pdf |

## The base

- **Stamp duty** is charged on the consideration in the conveyance or transfer instrument. The Caymanian reliefs apply only to a Caymanian buying a first or second property in the Islands; a person who bought property before becoming Caymanian does not get the first-property relief on the first purchase as a Caymanian, but may get the second-property relief if that property is the second (para (12)).
- **Import duty** is charged at the tariff line rate (see `ky-vat-gst`).
- **Accommodation tax** is charged on the room charges to tourists, meaning people not ordinarily resident who stay up to six months.

## Deadlines and filing

- Stamp duty is paid on the instrument when it is stamped, before registration.
- Pension contributions are due by the 15th of the following month (`ky-payroll-social`).
- Economic substance: annual notification; report within 12 months after the financial year end (`ky-corporate-income-tax`).
- No income tax or VAT returns exist.

## Penalties and interest

- Economic substance: CI$5,000 plus CI$500 a day for a late report; CI$10,000 for failing the test, CI$100,000 for a second year (`ky-corporate-income-tax`).
- Pension contributions not received by the 15th are delinquent and must be reported to the Director (`ky-payroll-social`).

## Cross-border points

- Moving to Cayman creates no Cayman income tax; the country you leave may still tax you.
- Foreign buyers pay the standard stamp duty (7.5% or 10%); the reliefs are for Caymanians only.
- CRS and FATCA reporting by financial institutions: refer to a specialist.

### Refusal catalogue (kept)

- R-KY-1, income tax: "The Cayman Islands has no income tax. There is no return and nothing to compute."
- R-KY-2, VAT or sales tax: "There is no VAT or sales tax; import duty applies at the border (`ky-vat-gst`)."
- R-KY-3, economic substance detail beyond the figures in `ky-corporate-income-tax`: escalate to a specialist.
- R-KY-4, CRS/FATCA reporting: escalate to a specialist.
- Duty concessions under development agreements, and foreign ownership restrictions on land: refer to a practitioner.

### Prohibitions (kept)

- Never state that the Cayman Islands has income tax, VAT, sales tax or payroll tax.
- Never apply a direct tax computation to a Cayman person or entity.
- Never ignore import duty, economic substance or CRS/FATCA obligations.
- Never present a computation as final without a reviewer.

## Two worked examples that recompute

### Caymanian first-time buyer, house at CI$600,000

```oa-check
name: KY stamp duty Caymanian first home 600000
inputs:
  price: 600000
  nil_band: 550000
steps:
  - duty: (price - nil_band) * 0.0375
expected:
  duty: 1875
```

The first CI$550,000 is free of duty and 3.75% is charged on the CI$50,000 above it: CI$1,875. A non-Caymanian buyer at the same price pays 7.5% of CI$600,000, CI$45,000.

### Decision: agree a price just under CI$2 million?

A non-Caymanian buyer is offered a house at CI$2,000,000 and the seller would take CI$1,990,000.

```oa-check
name: KY stamp duty either side of 2m, 2026
inputs:
  price_low: 1990000
  price_high: 2000000
steps:
  - duty_low: price_low * 0.075
  - duty_high: price_high * 0.10
  - total_low: price_low + duty_low
  - total_high: price_high + duty_high
  - saving: total_high - total_low
expected:
  duty_low: 149250
  duty_high: 200000
  saving: 60750
```

From 1 January 2026 the 10% rate applies to the whole consideration once it reaches CI$2 million, so a CI$10,000 lower price saves CI$60,750 in total. The price must be the real consideration; an artificial split is a matter for the Stamp Duty Act and a practitioner.

### Working paper (kept, compact)

```
CAYMAN ISLANDS, 2026
A. Import duties: value for duty; tariff line and rate; duty (ky-vat-gst)
B. Employment: payroll; pension 5% + 5% to CI$87,000; health insurance premium (employer recovers at most 50%); work permit fees
C. Entity: registry fee; economic substance notification and report
D. Property: consideration; buyer status (Caymanian first or second property, others); stamp duty
Reviewer flags: economic substance in scope? work permits current? pensions paid by the 15th?
```

### Bank statement reading (kept)

| Bank | Format |
|---|---|
| Cayman National, Butterfield | PDF, CSV |
| CIBC FirstCaribbean | CSV |

## Ask the client first

1. What is the question about: employment, imports, an entity, property, a hotel or rental?
2. For property: price, land with or without a building, and is the buyer Caymanian and is it a first or second property?
3. Employees in Cayman: how many, Caymanian or on work permits, how long employed?
4. Entity type (exempted company, ordinary company, partnership, fund) and does it carry on a relevant activity for economic substance?
5. Any imports, and their tariff headings?

## Sources

| Source | URL | Read on |
|---|---|---|
| Cayman legislation, current by title (letters C, D, H, I, M, N, S, T): read to confirm there is no income, corporate, VAT or minimum top-up tax Act and to find the current revisions | https://legislation.gov.ky/cms/legislation/current/by-title.html | 2026-11-14 |
| Tax Concessions Act (2018 Revision): read for s. 6, the tax undertaking and its 30-year limit | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0164/1964-0164_2018%20Revision.pdf | 2026-11-14 |
| Stamp Duty (Rates of Duty) Regulations 2025, SL 3 of 2025: read for the 7.5% rate and the Caymanian first and second property reliefs | https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0003/2025-0003_SL%203%20of%202025.pdf | 2026-11-14 |
| Stamp Duty (Rates of Duty) (No. 2) Regulations 2025, SL 63 of 2025: read for the 10% rate at CI$2 million or more from 1 January 2026 | https://legislation.gov.ky/cms/images/LEGISLATION/SUBORDINATE/2025/2025-0063/2025-0063_SL%2063%20of%202025.pdf | 2026-11-14 |
| Tourist Accommodation (Taxation) Act (2013 Revision): read for the 13% tax and the timeshare US$10 rule | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0168/1964-0168_2013%20Revision.pdf | 2026-11-14 |
| Customs Tariff Act (2026 Revision, revised as at 31 December 2025): read for the tariff rates, 22% on most lines | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2012/2012-0001/2012-0001_2026%20Revision.pdf | 2026-11-14 |
| National Pensions Act (2024 Revision): read for the 5% contributions and the CI$87,000 maximum | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1996/1996-0010/1996-0010_2024%20Revision.pdf | 2026-11-14 |

Not yet confirmed: stamp duty on mortgages, leases and share transfers of land holding companies; the old "Tax Undertaking Certificate up to 50 years for companies, 30 for individuals" (the Act read gives up to 30 years for companies; nothing on individuals); the old KYD to USD peg wording (only the Registry's US$1 = CI$0.82 conversion was read); work permit fee amounts; the old entity fee ranges (exempted company CI$850 to 3,000, ELP CI$750 to 2,500, regulated fund CI$3,000 to 4,000).
