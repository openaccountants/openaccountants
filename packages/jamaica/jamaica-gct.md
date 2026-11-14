---
name: jamaica-gct
description: >
  Jamaica General Consumption Tax (GCT) for 2026, for registered taxpayers
  preparing or reviewing the monthly Form 4A standard return. Covers the 15%
  standard rate (from April 2020), 25% on telephone services and instruments, the
  7% residential electricity line, the J$15,000,000 registration threshold from 1
  April 2025, zero-rated exports, exempt supplies, imported services by reverse
  charge, input tax credit rules (50% on entertainment and motor vehicle costs,
  capital goods over 24 months, apportionment above 5% exempt supplies), tax
  invoices, the return due by the last day of the following month and the
  registration penalties. Trigger on Jamaica GCT, Jamaica VAT, Form 4A, GCT return,
  TAJ GCT, GCT registration threshold. Built from Tax Administration Jamaica pages;
  not reviewed by an accountant.
version: 3.0
jurisdiction: JM
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: vat-gst
type: situation-rules
---

# Jamaica General Consumption Tax (GCT) v3.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Persons carrying on a taxable activity in Jamaica in 2026 under the General Consumption Tax Act, administered by Tax Administration Jamaica (TAJ). A taxable activity is the supply of goods and services, including services imported into Jamaica, carried on continuously or regularly, for consideration, whether or not for profit. Amounts are J$.

| Status | Who | Effect |
|---|---|---|
| Registered Taxpayer | Gross value of supplies of J$15,000,000 or more over 12 months (or an average of J$1,250,000 a month for a shorter period), or registered voluntarily | Charges GCT, files Form 4A, claims input tax; receives a Certificate of Registration |
| Registered Person | Below the threshold | Notice of Registration only; may not charge GCT; pays GCT on purchases with no credit |

Mixed activities count exempt supplies in the gross value for the threshold test.

- **In:** standard registered businesses filing Form 4A.
- **Out (refer):** approved tourism activities (Form 4D), general insurance (Form 4E), Special Consumption Tax goods (Form 4C), GCT groups (Form 4H), Special Economic Zone entities, approved farmers or manufacturers claiming relief or deferment. Non-registered persons accounting for imported services or one-off events use Form 4G.

### Refusal catalogue

- **R-JM-1, below the threshold and not registered.** No Form 4A; the person cannot charge GCT.
- **R-JM-2, Special Economic Zone entity.** Escalate; reliefs depend on the licence.
- **R-JM-3, approved farmer, manufacturer or deferment approval.** Confirm the TAJ approval before applying any relief.
- **R-JM-4, tourism activity licensed under the Tourist Board Act.** Form 4D; refer.
- **R-JM-5, general insurance.** Form 4E; refer.

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| Standard rate | 15% | In force from April 2020 (16.5% from June 2012 to March 2020) | TAJ, General Consumption Tax guide, history of the standard rate: https://www.jamaicatax.gov.jm/general-consumption-tax1 |
| Telephone services, telephone instruments and telephone cards | 25% | Specified rate under the Act | same |
| Zero rate | 0% | First Schedule supplies, including exports with a customs certificate of exportation | same |
| Registration threshold | J$15,000,000 gross supplies over 12 months, or J$1,250,000 a month average for a shorter period | Effective 1 April 2025; exempt supplies count in a mixed activity | same |
| Penalty, failure to apply for registration | J$5,000 (individual), J$10,000 (company), plus interest of two and one-half percent (2 ½%) a month on the tax for the unregistered period | Person liable to register as a Registered Taxpayer | same |
| Capital goods, full credit in the period | Consideration of J$100,000 or less, or exports at least 25% of manufactures (or US$416,666.67 equivalent) | Otherwise the credit is spread over 24 months | same |
| Restricted credit | 50% of input tax on restaurant, club and catering services, entertainment, motor vehicle expenses, leasing private motor vehicles, and services from a tourism activity | Business use | same |
| Motor car purchased for the taxable activity | 7% of cost, cost capped at the J$ equivalent of US$35,000, over 24 months | Private motor car | same |
| Other motor vehicle purchased | 14% of cost, over 24 months | Not a private motor car | same |
| Advance GCT at the port | 5% of the value of goods imported for resale by a registered importer | Prepayment of output tax, claimed as input tax; not passed on to customers | same |
| Records | Kept at least 6 years from the end of the taxable period | All registered taxpayers | same |
| Tax invoice | Issued within 7 days of the supply | Supplies to other registered taxpayers | same |
| Return due, Form 4A | On or before the last day of the month after the return period | Standard return | TAJ, GCT forms page: https://www.jamaicatax.gov.jm/general-consumption-tax |
| Return due, payments basis | Within 15 days after the taxable period | Approved payments (cash) basis | TAJ, General Consumption Tax guide: https://www.jamaicatax.gov.jm/general-consumption-tax1 |
| Residential electricity (power supply) | 7% output tax line | Section C2 of Form 4A, by residential customer type | TAJ, Form 4A (revised 3 June 2025): https://www.jamaicatax.gov.jm/documents/10194/18006/GCT+Form+4A+amended+03.06.2025+%28002%29.pdf/b2428c2a-346f-6eeb-0b18-550ec5b60d72 |
| Apportionment trigger | Exempt supplies above 5% of total supplies | Complete Section D1 | same |

TAJ's guide still prints 16.5% in its older narrative paragraphs; its rate history table gives 15% from April 2020, which is the rate applied here.

## The base

### Supplies and value

- **Value of a supply** for money is the consideration excluding GCT; for part-money consideration or a connected-person buyer, open market value; with no consideration, the cost to the registered taxpayer.
- **Imports of goods**: GCT is collected by Customs on the customs value plus duty, additional stamp duty and Special Consumption Tax. A non-registered commercial importer bears an uplift instead of advance GCT; no importer bears both.
- **Imported services**: a registered taxpayer self-assesses (reverse charge) on Form 4A lines 20 and 21, and may claim the input tax at line 35 if the service is for taxable supplies.
- **Exports** are zero-rated when the customs export documents are held.
- **Exempt supplies** (Third Schedule): no GCT charged and no input credit on related purchases.
- **Time of supply** (invoice basis): the earliest of invoice, delivery or payment. The payments basis is available on written approval for general insurance, professional services, telephone service and commercial rental.
- **Own use**: goods given away, taken for personal use or diverted to an exempt activity are output tax; prepare a tax invoice marked "Own Use".

### Tax invoice contents

The words "Tax Invoice"; date; serial number; supplier name, address and GCT registration number; buyer name and address; quantity and description; consideration; rate and amount of tax; total including GCT. One tax invoice per supply; a replacement is marked "COPY". Credit and debit notes adjust output or input tax.

### Form 4A, line by line (revision of 3 June 2025)

| Lines | Content |
|---|---|
| 6 | Total supplies for the period, excluding imported services |
| 7, 8, 9, 10 | Exempt, export and other zero-rated supplies, and their total |
| 11 | Taxable supplies at a positive rate (6 minus 10) |
| 12, 13 | Supplies to tax withholding entities (TWEs) at the standard rate, and GCT |
| 14, 15 | Supplies to other entities at the standard rate, and GCT |
| 16 to 19 | Supplies at other rates (Section C1, and C2 power supply), to TWEs and others |
| 20, 21 | Imported services and GCT on them |
| 22, 23 | GCT deferred; GCT on goods for exempt activities, personal use and other adjustments |
| 24 | Total output tax (13, 15, 17, 19, 21, 22, 23) |
| 25 to 28 | Purchases and expenses that qualify for credit: imported goods, local purchases, local expenses |
| 29 | GCT on local purchases and expenses that qualify |
| 30 to 32 | GCT paid or deferred on imports that qualifies |
| 33 | GCT on capital goods, if not in 32 |
| 34 | GCT withheld by TWEs (claim only on an e-filed return) |
| 35 | GCT on imported services that qualifies |
| 36, 37 | Adjustments; total input tax (29, 32, 33, 34, 35, 36) |
| 38 | GCT payable or creditable (24 minus 37) |
| 39, 40 | Balance brought forward; total payable or creditable |
| 41, 42, 43 | JPS subsidy line; GCT paid this period; refund or credit choice if 38 is negative |

Where exempt supplies exceed 5% of total supplies, Section D1 apportions input tax by the taxable share. Do not take a credit for a refund requested but not yet received.

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 15% |
| Unknown GCT status of a purchase | No credit |
| Unknown counterparty country | Domestic |
| Unknown business-use share | No credit |
| Entertainment, restaurant, motor vehicle running cost | 50% credit at most |

### Red flags for review

| Flag | Level |
|---|---|
| Single transaction over J$500,000, or a single default moving tax by over J$50,000 | High |
| One counterparty over 40% of output or input, or more than 4 defaults used | Medium |
| Net GCT position over J$1,000,000 | Low |

### Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| NCB, SCOTIABANK, JMMB, SAGICOR BANK, FIRST GLOBAL, CIBC FIRSTCARIBBEAN | Fees: check the invoice for GCT; interest: no GCT | Financial services exemption to confirm per Third Schedule |
| TAJ, TAX ADMINISTRATION JAMAICA, NIS, NHT, EDUCATION TAX | Exclude | Tax and statutory payments |
| JAMAICA CUSTOMS | Duty excluded; GCT on the import entry to line 30, advance GCT also creditable | Keep the entry |
| JPS (electricity) | Commercial supply at 15%; residential power at 7% is the supplier's line | Check the bill |
| NWC (water) | Check the bill | |
| FLOW, DIGICEL | Telephone at 25%; check internet lines on the bill | Credit if a business line |
| SAGICOR LIFE, GUARDIAN LIFE | Exclude | Life insurance |
| GENERAL INSURANCE, ADVANTAGE GENERAL | GCT on general insurance per the insurer's invoice | Insurer files Form 4E |
| GOOGLE, MICROSOFT, ADOBE, META, ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI (non-resident) | Imported service: lines 20 and 21 at 15%, credit at line 35 | Net nil if fully taxable |
| HI-LO, MEGAMART, PRICESMART, LOSHUSAN | No credit by default | Personal provisioning |
| RESTAURANT, CATERING, CLUB | 50% credit at most | Business purpose needed |
| PETCOM, RUBIS, TOTAL, SHELL (fuel) | Check the invoice; petroleum carries Special Consumption Tax | Motor vehicle expense: 50% credit at most |
| OWN TRANSFER, SALARY, WAGES, PAYE | Exclude | |

Bank statements: NCB and Scotiabank CSV or PDF, DD/MM/YYYY, J$; own-account transfers excluded.

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | Apply on Form GCT-1 (with a TRN branch extension) | When the threshold is reached, or voluntarily |
| 2 | Receive a Certificate of Registration (above threshold) or Notice of Registration (below) | After TAJ approves |
| 3 | Issue tax invoices | Within 7 days of each supply |
| 4 | File Form 4A online through the TAJ portal and pay line 42 | By the last day of the following month (15 days for the payments basis) |
| 5 | If line 38 is negative, tick refund or credit at line 43 | With the return |

Online filing is required to claim GCT withheld by TWEs (line 34).

## Penalties and interest

- Failure to apply for registration: J$5,000 (individual) or J$10,000 (company), plus 2.5% a month interest on the tax for the period unregistered.
- Late return and late payment: TAJ's guide has a "Penalty, Surcharge and Interest" section whose figures were not reached in the text read; see Not yet confirmed.

## Cross-border points

- Imported services: self-assess on lines 20 and 21 if registered; a non-registered person uses Form 4G.
- Imported goods: GCT at Customs, plus 5% advance GCT for registered importers of goods for resale (not on petroleum, capital goods, deferred goods, telephone instruments, exempt goods, raw foodstuff, goods with productive input relief, or goods imported by non-registered persons).
- Exports: zero-rated with customs export evidence.
- Non-resident digital suppliers: registration duties not confirmed (see Not yet confirmed).

## Two worked examples that recompute

### Example 1: Monthly Form 4A with an imported service

Standard-rated sales J$2,000,000 net to non-TWE customers (line 14, GCT J$300,000). A cloud subscription from a non-resident, J$300,000 (lines 20 and 21, GCT J$45,000). Local input GCT that qualifies J$180,000 (line 29). Imported service credit J$45,000 (line 35). Output J$345,000, input J$225,000, payable J$120,000 by the last day of the next month.

```oa-check
name: JM GCT 2026 Form 4A, standard sales and imported service
inputs:
  sales: 2000000
  imported_services: 300000
  local_input_gct: 180000
steps:
  - line15: sales * 0.15
  - line21: imported_services * 0.15
  - line24: line15 + line21
  - line37: local_input_gct + line21
  - line38: line24 - line37
expected:
  line15: 300000
  line21: 45000
  line24: 345000
  line37: 225000
  line38: 120000
```

### Example 2: Must input tax be apportioned? Exempt share 10% or 4%

Total supplies J$10,000,000. Input GCT J$350,000, of which J$50,000 relates only to taxable supplies and J$300,000 is common. Case A: exempt supplies J$1,000,000 (10%, above 5%): Section D1 applies, common GCT allowed at 90%, credit J$320,000. Case B: exempt supplies J$400,000 (4%): no apportionment on Form 4A, credit J$350,000. The 5% test is worth J$30,000.

```oa-check
name: JM GCT 2026 apportionment above or below 5% exempt
inputs:
  total_supplies: 10000000
  exempt_a: 1000000
  direct_gct: 50000
  common_gct: 300000
steps:
  - taxable_share_a: (total_supplies - exempt_a) / total_supplies
  - credit_a: direct_gct + common_gct * taxable_share_a
  - credit_b: direct_gct + common_gct
  - difference: credit_b - credit_a
expected:
  taxable_share_a: 0.9
  credit_a: 320000
  credit_b: 350000
  difference: 30000
```

### Short cases kept from the earlier version (corrected)

- Sale to ABC Jamaica Ltd, J$575,000 GCT-inclusive: net J$500,000, GCT J$75,000 (lines 14 and 15).
- Export to a US buyer, J$500,000: line 8, zero-rated, full input credit.
- Restaurant bill J$23,000 including GCT J$3,000: credit at most J$1,500 (50%), not blocked as the earlier version said.
- Sedan J$5,000,000 bought for the business: 7% of cost (cost capped at the US$35,000 equivalent) over 24 months, not blocked as the earlier version said.
- Digicel phone service J$12,500: net J$10,000, GCT J$2,500 at 25%; credit if a business line.

## Ask the client first

1. Are you a Registered Taxpayer (Certificate) or a Registered Person (Notice)? What is your TRN and filing period?
2. Total supplies in the last 12 months, split into standard-rated, other rates, zero-rated, exports and exempt.
3. Do you sell to tax withholding entities, and have you received GCT withheld certificates?
4. Imported goods (customs entries) and imported services from non-residents in the period.
5. Capital goods, motor vehicles, entertainment and restaurant costs in the period.
6. Any credit brought forward (line 39) or refund requested and not yet received?

## Sources

| Source | URL | Read on |
|---|---|---|
| TAJ, General Consumption Tax guide: read for the threshold (effective 1 April 2025), registration statuses and penalty, the rate history, the 25% telephone rate, value of supply, imports and advance GCT, tax invoice contents, records, input tax credit rules (capital goods, 50% items, motor vehicles), accounting bases and the payments-basis deadline | https://www.jamaicatax.gov.jm/general-consumption-tax1 | 2026-11-14 |
| TAJ, General Consumption Tax forms page: read for the Form 4A to 4H descriptions and the due date on or before the last day of the following month | https://www.jamaicatax.gov.jm/general-consumption-tax | 2026-11-14 |
| TAJ, Form 4A, GCT standard return (revised 3 June 2025): read in full for lines 6 to 43, Section C2 power supply at 7% and the 5% apportionment trigger | https://www.jamaicatax.gov.jm/documents/10194/18006/GCT+Form+4A+amended+03.06.2025+%28002%29.pdf/b2428c2a-346f-6eeb-0b18-550ec5b60d72 | 2026-11-14 |

Not yet confirmed: the GCT withholding rate applied by tax withholding entities (the earlier version said two-thirds of the GCT, about 10% of value); late-filing and late-payment penalties, surcharge and interest on GCT returns; the tourism rate (TAJ's older text says 10%); whether the 50% restricted credits and the 7% and 14% motor vehicle rules in TAJ's guide (written when the rate was 16.5%) are unchanged in the current Act; the full First Schedule zero-rated list and Third Schedule exempt list (the earlier version listed basic foods, medical and dental services, education, financial services, life insurance, residential rental, public transport, domestic water and electricity under thresholds, and petroleum); registration duties for non-resident digital service suppliers; the earlier version's section numbers of the Act (ss. 4A, 16(2), 17, 19A, 20), which could not be checked because the Act on laws.moj.gov.jm returned an error (503); the bi-monthly filing option for small taxpayers named in the earlier version.
