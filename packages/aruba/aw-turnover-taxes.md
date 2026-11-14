---
name: aw-turnover-taxes
description: "Aruba turnover taxes BBO, BAVP and BAZV for tax year 2026. Covers who owes them, the combined 7% rate (BBO 2.5%, BAVP 1.5%, BAZV 3%) on the total compensation, place of supply, exemptions, the cash basis and the optional invoice basis, the small-entrepreneur relief for sole traders up to Afl. 50,000 and what happens on crossing it, BBO at the border on imports since 1 August 2023 and its deduction, the reverse charge and registration for foreign suppliers of services, the monthly return and payment by the 15th, and collection costs. Trigger phrases include Aruba BBO, BAVP, BAZV, Aruba turnover tax, Aruba sales tax, kleine ondernemer Aruba, BBO na frontera."
version: "1.0"
jurisdiction: AW
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Aruba turnover taxes: BBO, BAVP and BAZV v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar year 2026. Authority: Departamento di Impuesto (DIMP); imports through the Departamento di Aduana. Amounts in Aruban florins (Afl.). The three taxes share one base and one return; DIMP calls them together "BBO" ([DIMP, U bent kleine ondernemer](https://www.impuesto.aw/u-bent-kleine-ondernemer)).

## Who this applies to

- **Every entrepreneur** owes BBO, BAVP and BAZV on turnover from supplying goods and services. They are self-assessed: you report all taxable and exempt turnover on the return and pay ([DIMP, BBO](https://www.impuesto.aw/bbo); [DIMP, Bestemmingsheffing AZV](https://www.impuesto.aw/bestemmingsheffing-azv)).
- **Importers**, including private persons, pay BBO at the border on imported goods ([DIMP, BBO na frontera](https://www.impuesto.aw/bbo-na-frontera)).
- **Small sole traders** with annual turnover of Afl. 50,000 or less are relieved from filing and paying ([DIMP, U bent kleine ondernemer](https://www.impuesto.aw/u-bent-kleine-ondernemer)).
- **Foreign suppliers** of services taxed in Aruba must register or appoint a fiscal representative; for B2B services the reverse charge applies ([DIMP, Belastingplan 2023](https://www.impuesto.aw/belastingplan_2023)).
- Not covered: tourist levy, special accommodation tax, gaming licence tax, import duties and excises.

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| BBO | 2.5% | From 1 January 2023 (was 1.5%) | 2026 | [DIMP, Hoeveel BBO en BAVP moet u betalen](https://www.impuesto.aw/hoeveel-bbo-en-bavp-moet-u-betalen) |
| BAVP | 1.5% | From 1 July 2018 | 2026 | same |
| BAZV | 3% | From 1 July 2018 | 2026 | same |
| Combined | 7% | On the total compensation | 2026 | same |
| At the border | 4% BBO/BAVP plus 3% BAZV, total 7% | On the customs value, from 1 August 2023 | 2026 | [DIMP, BBO na frontera](https://www.impuesto.aw/bbo-na-frontera) |
| Small entrepreneur (KOR) threshold | Afl. 50,000 annual turnover or less | Sole traders only | 2026 | [DIMP, U bent kleine ondernemer](https://www.impuesto.aw/u-bent-kleine-ondernemer) |
| USD conversion rate | Afl. 1.79 per USD | Used by DIMP | 2026 | [DIMP, Hoeveel BBO en BAVP moet u betalen](https://www.impuesto.aw/hoeveel-bbo-en-bavp-moet-u-betalen) |
| Reminder cost on an unpaid assessment | Afl. 10 | | 2026 | [DIMP, U betaalt deels niet of niet op tijd](https://www.impuesto.aw/u-betaalt-deels-niet-of-niet-op-tijd) |

## The base

1. **Compensation:** the total amount charged to the customer, including extra costs, plus anything the customer pays above the invoice; payments in kind at their value. Tips received by employees are outside the base; a service charge billed by the business is inside it. Pass-through items paid in the customer's name and for their account are outside (a notary's registry and stamp duties) ([DIMP, Hoeveel BBO en BAVP moet u betalen](https://www.impuesto.aw/hoeveel-bbo-en-bavp-moet-u-betalen)).
2. **Supplies of goods** include sales, hire purchase, building and delivering real estate, supplying and installing goods, and taking goods for private use ([DIMP, Waarover berekent u BBO](https://www.impuesto.aw/waarover-berekent-u-bbo)).
3. **Place of supply:** goods located in Aruba are supplied in Aruba, including sales to foreign customers. A business established in Aruba supplies its services in Aruba, except some services for foreign customers (such as those on foreign real estate) and services physically done abroad (real estate work, cultural, artistic and educational activities, loading and unloading) (same page). Telecommunications, broadcasting and electronic services are supplied where the customer lives or is established ([DIMP, Belastingplan 2023](https://www.impuesto.aw/belastingplan_2023)).
4. **Exempt goods** include: real estate on which transfer tax was paid; fuel for aircraft and ships in international transport, armed forces and water and power producers; prescription medicines; medical aids; water and electricity; goods to customers established outside Aruba ([DIMP, Wanneer krijgt u vrijstelling](https://www.impuesto.aw/wanneer-krijgt-u-vrijstelling)).
5. **Exempt services** include: hotel rooms and apartments on which tourist levy is due; gaming on which gaming licence tax is due; international passenger or goods transport; public education; certain banking and insurance; letting homes used as a main residence; interest received. Further education, medical and social care bodies are designated by ministerial regulation (same page).
6. **Timing:** cash basis by default (due when payment is received); invoice basis on request (due on the invoice date, or when the invoice should have been issued). On the invoice basis, a bad debt can be reclaimed by letter if you show the amount will not be received ([DIMP, Wanneer moet u aangifte doen en betalen](https://www.impuesto.aw/wanneer-moet-u-aangifte-doen-en-betalen)).
7. **No VAT-style credit:** a registered entrepreneur deducts only the BBO paid at the border on imported trading goods (goods for resale) ([DIMP, U bent kleine ondernemer](https://www.impuesto.aw/u-bent-kleine-ondernemer)).

### Small entrepreneur relief

- A sole trader with annual turnover of Afl. 50,000 or less is relieved by law from filing and paying, is not registered and files no returns. A company does not qualify ([DIMP, U bent kleine ondernemer](https://www.impuesto.aw/u-bent-kleine-ondernemer)).
- Crossing the threshold during the year: register immediately; file and pay from the month of crossing, on the amount above the threshold, for the rest of that year and all later years ([DIMP, Belastingplan 2023](https://www.impuesto.aw/belastingplan_2023)).
- Imports: a small entrepreneur still pays BBO at the border and cannot deduct it. Voluntary registration gives the deduction on imported trading goods, but brings monthly returns and cannot be reversed ([DIMP, U bent kleine ondernemer](https://www.impuesto.aw/u-bent-kleine-ondernemer)).

## Deadlines and filing

- Monthly period. File and pay by the 15th of the next month, or the first working day after if the 15th is a Saturday, Sunday or holiday. File even with no activity or only exempt turnover; if the whole year is exempt or inactive, all 12 returns may be filed at once ([DIMP, Wanneer moet u aangifte doen en betalen](https://www.impuesto.aw/wanneer-moet-u-aangifte-doen-en-betalen)).
- Returns open in BOi early in the month: September 2026 returns opened 2 October and were due 15 October 2026 ([DIMP, Kalender oktober 2026](https://www.impuesto.aw/kalender-digitale-aangifte-oktober-2026)).
- At the border, the importer or broker pays with the customs declaration in ASYCUDAWorld; the importer's persoonsnummer must be on the declaration to support the deduction ([DIMP, BBO na frontera](https://www.impuesto.aw/bbo-na-frontera)).

## Penalties and interest

Late or missing returns or payments can bring an additional assessment with a penalty; unpaid assessments carry collection costs (reminder Afl. 10, writ at least Afl. 25) and collection interest ([DIMP, U betaalt deels niet of niet op tijd](https://www.impuesto.aw/u-betaalt-deels-niet-of-niet-op-tijd)). The BBO penalty amounts are not on the pages read.

## Cross-border points

- B2B services from foreign suppliers not established in Aruba (real estate services, transport, cultural and similar activities, loading and unloading, work on movable goods, telecom, broadcasting and electronic services): reverse charge, the Aruban business pays ([DIMP, Belastingplan 2023](https://www.impuesto.aw/belastingplan_2023)).
- B2C electronic and similar services by foreign suppliers: the foreign supplier owes the tax and must register, or appoint a fiscal representative and notify the Inspector with a copy of the mandate (same page).
- Exports of goods to customers outside Aruba are exempt ([DIMP, Wanneer krijgt u vrijstelling](https://www.impuesto.aw/wanneer-krijgt-u-vrijstelling)).
- An importer with an exemption from import duties or excise under the LIUD is also exempt from BBO at the border ([DIMP, BBO na frontera](https://www.impuesto.aw/bbo-na-frontera)).

## Two worked examples that recompute

**Case 1: monthly return on Afl. 100,000 of taxable receipts, with imports.** BBO 2.5% = 2,500, BAVP 1.5% = 1,500, BAZV 3% = 3,000, total 7,000. The business paid border BBO of 7% on trading goods with a customs value of 33,000 (2,310, DIMP's own car example amount) and deducts it: net payable 4,690 by the 15th of the next month.

```oa-check
name: Aruba BBO, BAVP and BAZV monthly return
inputs:
  receipts: 100000
  import_customs_value: 33000
steps:
  - bbo: receipts * 0.025
  - bavp: receipts * 0.015
  - bazv: receipts * 0.03
  - total_output: bbo + bavp + bazv
  - border_paid: import_customs_value * 0.07
  - net_payable: total_output - border_paid
expected:
  bbo: 2500.00
  bavp: 1500.00
  bazv: 3000.00
  total_output: 7000.00
  border_paid: 2310.00
  net_payable: 4690.00
```

**Case 2: decision, a small sole trader registers voluntarily or not.** Annual turnover 45,000; imported trading goods with a customs value of 20,000 carry border BBO of 1,400. Stay relieved: total tax cost 1,400 (the border tax, not deductible). Register: 7% of 45,000 = 3,150 on the returns, less the 1,400 deduction = 1,750 payable, a total cost of 3,150. Staying relieved is cheaper by 1,750, and registration cannot be undone. Registering only pays if the business would cross Afl. 50,000 anyway.

```oa-check
name: Voluntary BBO registration for a small sole trader
inputs:
  turnover: 45000
  import_value: 20000
steps:
  - border_tax: import_value * 0.07
  - cost_relieved: border_tax
  - payable_registered: turnover * 0.07 - border_tax
  - cost_registered: border_tax + payable_registered
  - extra_cost_if_registered: cost_registered - cost_relieved
expected:
  border_tax: 1400.00
  payable_registered: 1750.00
  cost_registered: 3150.00
  extra_cost_if_registered: 1750.00
```

## Ask the client first

1. Sole trader or company? Annual turnover in 2025 and so far in 2026.
2. Cash or invoice basis?
3. What is supplied, and to whom (exempt items, foreign customers, hotel rooms under tourist levy)?
4. Imports of trading goods, with customs values and the persoonsnummer on the declarations?
5. Services bought from foreign suppliers (reverse charge)?

## Sources

| Source | URL | Read on |
|---|---|---|
| DIMP, Hoeveel BBO en BAVP moet u betalen: read for the base, the rate timeline to 7% and the USD rate | https://www.impuesto.aw/hoeveel-bbo-en-bavp-moet-u-betalen | 2026-11-14 |
| DIMP, BBO: read for who owes BBO and self-assessment | https://www.impuesto.aw/bbo | 2026-11-14 |
| DIMP, Bestemmingsheffing AZV: read for who owes BAZV | https://www.impuesto.aw/bestemmingsheffing-azv | 2026-11-14 |
| DIMP, Waarover berekent u BBO: read for supplies of goods, services and place of supply | https://www.impuesto.aw/waarover-berekent-u-bbo | 2026-11-14 |
| DIMP, Wanneer krijgt u vrijstelling: read for exempt goods and services | https://www.impuesto.aw/wanneer-krijgt-u-vrijstelling | 2026-11-14 |
| DIMP, Wanneer moet u aangifte doen en betalen (BBO): read for the monthly period, the 15th, cash and invoice basis and bad debts | https://www.impuesto.aw/wanneer-moet-u-aangifte-doen-en-betalen | 2026-11-14 |
| DIMP, U bent kleine ondernemer: read for the Afl. 50,000 relief, imports and voluntary registration | https://www.impuesto.aw/u-bent-kleine-ondernemer | 2026-11-14 |
| DIMP, Belastingplan 2023: read for the 2023 rate rise, threshold crossing, electronic services, reverse charge and fiscal representative | https://www.impuesto.aw/belastingplan_2023 | 2026-11-14 |
| DIMP, BBO na frontera: read for border BBO, the customs value base, the car example and exemptions | https://www.impuesto.aw/bbo-na-frontera | 2026-11-14 |
| DIMP, Kalender digitale aangifte oktober 2026: read for the September 2026 dates | https://www.impuesto.aw/kalender-digitale-aangifte-oktober-2026 | 2026-11-14 |
| DIMP, U betaalt deels niet of niet op tijd: read for collection costs and interest | https://www.impuesto.aw/u-betaalt-deels-niet-of-niet-op-tijd | 2026-11-14 |

Not yet confirmed: BBO penalty amounts; the collection interest rate; the ministerial list of exempt education, medical and social care bodies; whether the small-entrepreneur test uses the current or prior year's turnover (the page says "jaarlijkse bedrijfsomzet").
