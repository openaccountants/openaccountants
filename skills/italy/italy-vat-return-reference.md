---
name: italy-vat-return-reference
description: Reference sections for italy-vat-return (Two worked examples that recompute, Deadlines and filing, Penalties and interest), moved from the parent skill word for word so each file stays under the size limit. MUST load alongside italy-vat-return.
version: 2.3
jurisdiction: IT
category: international
tax_year: 2026
tax_year_notes: "IVA periods in calendar 2026, read at 5 November 2026, under DPR 633/1972. The Testo unico IVA (D.Lgs. 10/2026), the sanctions Testo unico (D.Lgs. 173/2024) and the Testo unico on compliance and assessment (D.Lgs. 141/2026) apply from 1 January 2027 and are not mapped. Filings made in 2027 for 2026 periods are held on that point."
last_updated: 2026-11-05
tier: 2
depends_on:
  - italy-vat-return
  - vat-workflow-base
  - eu-vat-directive
job: vat-return
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: vat-gst
---

# italy-vat-return: reference sections

Moved word for word from `italy-vat-return`. Load that skill first.

## Two worked examples that recompute

All examples are hypothetical, from a Rome-based self-employed IT consultant in regime ordinario, quarterly, with volume d'affari within EUR 500,000 and no refusal fired. Each `oa-check` is checked by CI. Examples 1 and 2 are the 2 required; Example 2 is the decision. Each rests on the documents shown being held.

### Example 1: quarterly LIPE, Q2 2026

**Input.** Domestic sales EUR 12,000 at 22%. EU B2B service sale EUR 3,500 to a German company with a valid VIES number, completed in the quarter. Laptop EUR 1,307.38 plus IVA EUR 287.62, invoice registered. Google Ireland EUR 850, invoice with no Italian IVA. Notion Labs Inc EUR 14.68, no Italian IVA. Car lease EUR 450 gross at 22%, paid by direct debit, mixed use, client not an agent, vehicle not the object of the activity. VP8 credit from Q1 EUR 300.

```oa-check
name: Italy Q2 2026 LIPE with reverse charge, 40% vehicle and credit
inputs:
  sales_22: 12000
  eu_service_sale: 3500
  laptop_net: 1307.38
  laptop_iva: 287.62
  google_net: 850
  notion_net: 14.68
  lease_gross: 450
  vehicle_share: 40
  vp8: 300
  rate: 22
steps:
  - lease_net: round(lease_gross * 100 / (100 + rate), 2)
  - lease_iva: lease_gross - lease_net
  - lease_deductible: round(pct(lease_iva, vehicle_share), 2)
  - output_sales: pct(sales_22, rate)
  - rc_google: round(pct(google_net, rate), 2)
  - rc_notion: round(pct(notion_net, rate), 2)
  - vp2: sales_22 + eu_service_sale
  - vp3: laptop_net + google_net + notion_net + lease_net
  - vp4: output_sales + rc_google + rc_notion
  - vp5: laptop_iva + rc_google + rc_notion + lease_deductible
  - vp6_col1: max(vp4 - vp5, 0)
  - vp6_col2: max(vp5 - vp4, 0)
  - to_pay_before_interest: max(vp6_col1 - vp6_col2 - vp8, 0)
  - vp12: round(pct(to_pay_before_interest, 1), 2)
  - vp14_col1: max((vp6_col1 + vp12) - (vp6_col2 + vp8), 0)
  - vp14_col2: max((vp6_col2 + vp8) - (vp6_col1 + vp12), 0)
expected:
  lease_net: 368.85
  lease_iva: 81.15
  lease_deductible: 32.46
  vp2: 15500
  vp3: 2540.91
  vp4: 2830.23
  vp5: 510.31
  vp6_col1: 2319.92
  vp6_col2: 0
  to_pay_before_interest: 2019.92
  vp12: 20.20
  vp14_col1: 2040.12
  vp14_col2: 0
```

**Result.** Conditional on this file's held reading of the VP12 base, VP14 col 1 is EUR 2,040.12, payable by F24 by 20 August 2026, with the LIPE by 30 September 2026. The non-deductible EUR 48.69 of the lease is a cost. The EU sale and the Google Ireland purchase fall under Intrastat lists subject to the hold under Related filings, so whether either is listed is held. The 2 foreign purchases need cross-border data unless an art 1(3-bis) exception applies. Another base changes the amount: for scale only, 1% before the VP8 credit gives VP12 of EUR 23.20 and VP14 col 1 of EUR 2,043.12. Confirm the base before relying on either. On this file's reading, had the VP8 credit exceeded the debt, nothing would be payable, VP12 would be nil and col 2 would carry the credit.

### Example 2: monthly or quarterly

**Input.** The consultant's IVA to pay before interest is EUR 6,000, 5,000 and 7,000 for Q1 to Q3, and EUR 4,000 for the Q4 balance in the annual return. Volume d'affari is EUR 300,000 in services. IVA arises evenly across each quarter's months.

```oa-check
name: Italy monthly or quarterly settlement, cost of the option
inputs:
  q1: 6000
  q2: 5000
  q3: 7000
  q4: 4000
  volume: 300000
  services_limit: 500000
steps:
  - headroom: services_limit - volume
  - int_q1: pct(q1, 1)
  - int_q2: pct(q2, 1)
  - int_q3: pct(q3, 1)
  - int_q4: pct(q4, 1)
  - cost_q1_to_q3: int_q1 + int_q2 + int_q3
  - quarterly_cost: cost_q1_to_q3 + int_q4
  - monthly_cost: 0
  - extra_cost_of_quarterly: quarterly_cost - monthly_cost
  - average_months_deferred: (3 + 2 + 1) / 3
  - break_even_percent_a_year: 1 * 12 / average_months_deferred
expected:
  headroom: 200000
  cost_q1_to_q3: 180
  int_q4: 40
  quarterly_cost: 220
  extra_cost_of_quarterly: 220
  average_months_deferred: 2
  break_even_percent_a_year: 6
```

**Result.** Quarterly costs EUR 220 a year more than monthly: EUR 180 on Q1 to Q3 plus EUR 40 on Q4. On Q1 to Q3, 1% buys a payment on average 2 months later. On interest alone, choose monthly if the client's own cost of money is below about 6% a year simple, and quarterly if above it. Any bookkeeping saving is a separate judgement. The month counts are 3, 2 and 1 for the 3 months of a quarter and move slightly with the August date. Q4 is left out of the break-even because the acconto changes its timing. Monthly has no option step. Quarterly is open only because EUR 300,000 is within EUR 500,000; above that it closes. The option is communicated in the first annual return after the choice, takes effect from the year chosen and lasts until revoked unless the limit is exceeded.

### Example 3: amount not above EUR 100

**Input.** A monthly filer has VP14 col 1 of EUR 85 for January 2026 and VP6 col 1 of EUR 1,000 for February, with no credits.

```oa-check
name: Italy EUR 100 carry in a monthly settlement
inputs:
  january_vp14: 85
  february_vp6: 1000
  limit: 100
steps:
  - over_limit: min(ceil(max(january_vp14 - limit, 0)), 1)
  - january_paid: january_vp14 * over_limit
  - february_vp7: january_vp14 - january_paid
  - february_vp14: february_vp6 + february_vp7
expected:
  over_limit: 0
  january_paid: 0
  february_vp7: 85
  february_vp14: 1085
```

**Result.** Nothing is paid by 16 February. February's VP7 is EUR 85 and EUR 1,085 is paid by 16 March 2026. A carry still open at the end must be paid by 16 December 2026. The carry itself needs the amount to be EUR 100 or less: at EUR 100.01 the whole amount is paid.

### Example 4: vehicle costs

**Input.** Lease IVA EUR 81.15 and fuel IVA EUR 22 paid by card, on a car in the business. Cases: mixed use; exclusive business use proved, or the client is an agent; fuel paid in cash.

```oa-check
name: Italy art 19-bis.1 vehicle and fuel deduction cases
inputs:
  lease_iva: 81.15
  fuel_iva: 22
  share_mixed: 40
  share_full: 100
steps:
  - mixed_lease: round(pct(lease_iva, share_mixed), 2)
  - mixed_fuel: round(pct(fuel_iva, share_mixed), 2)
  - mixed_total: mixed_lease + mixed_fuel
  - full_total: pct(lease_iva, share_full) + pct(fuel_iva, share_full)
  - difference: full_total - mixed_total
  - cash_fuel_case: mixed_lease + 0
expected:
  mixed_lease: 32.46
  mixed_fuel: 8.80
  mixed_total: 41.26
  full_total: 103.15
  difference: 61.89
  cash_fuel_case: 32.46
```

**Result.** Mixed use: EUR 41.26 in VP5. Exclusive use proved, or an agent or commercial representative: EUR 103.15. What decides it is the art 19-bis.1(c) test, not the legacy list of taxi, driving school and rental. The EUR 61.89 is the IVA at stake to disclose. Fuel in cash: no fuel deduction, EUR 32.46 only. The legacy said an IT consultant has 40%, which still holds on these facts.

### Transaction patterns

From the same hypothetical account, Q2 2026. Each tests both cases.

**Non-EU SaaS.** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`. Invoice from a US entity with no IVA: autofattura under art 17(2) and art 21(5). IN-RC: VP3 EUR 14.68, VP4 and VP5 EUR 3.23. Net zero for a fully taxable client. The legacy 'VP4 (via VP12)' is wrong. Use the art 13(4) exchange rate, not the bank's, if they differ.

**EU service.** `10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`. Invoice from an IE entity with no IVA: integrate and register under art 17(2) and D.L. 331/1993 arts 46 and 47. IN-RC: VP3 EUR 850, VP4 and VP5 EUR 187. Both sides appear. Invoice showing Italian IVA: IN-D for the tax shown.

**Restaurant.** `15.04.2026 ; RISTORANTE DA MARIO ROMA ; DEBIT ; Business dinner ; -220.00 ; EUR`. Needs Input, with the restaurant question. Client dinner that is representation: blocked under (h), IN-N. Staff or own business travel with a fattura elettronica registered under art 25: IN-D at the 10% rate shown (item 121): EUR 220 x 10/110 = EUR 20 in VP5, net EUR 200 in VP3, subject to the hold on (f). A scontrino only: no VP5. The legacy Q1 question is kept.

**Capital goods.** `18.04.2026 ; DELL ITALIA SRL ; DEBIT ; Invoice DEL2026-0041 Laptop XPS 15 ; -1,595.00 ; EUR`. EUR 1,595 / 1.22 = EUR 1,307.38 net, above EUR 516.46. Registered invoice: IN-D, VP3 EUR 1,307.38, VP5 EUR 287.62. Flag for the registro dei beni ammortizzabili and for art 19-bis.2.

**EU B2B service sale.** `22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice IT-2026-018 IT consultancy March ; +3,500.00 ; EUR`. German customer's USt-IdNr valid on VIES, invoice with 'inversione contabile': OUT-N, VP2 EUR 3,500, no IVA, Intrastat list subject to the hold under Related filings. The narrative says March: art 6(6) places the sale when the work is completed, or on earlier payment, so this pattern treats it as completed in April, in the Q2 VP2. If it was completed in March, it belongs in the Q1 VP2. Confirm the date. Number not verified: Needs Input (HIGH). The legacy 'non imponibile' field note is replaced.

**Motor vehicle.** `28.04.2026 ; LEASYS SPA ; DEBIT ; Lease payment Fiat 500X ; -450.00 ; EUR`. EUR 368.85 net and EUR 81.15 IVA. Default in Conservative defaults once the facts there are known: 40%, EUR 32.46 in VP5, VP3 EUR 368.85. The block on lease is art 19-bis.1(d), by reference to (c). The question stays: 'Vehicle: 40% IVA deductible unless used only for the business. Is that so, is the vehicle the object of your activity, or are you an agent?'

**Taxi.** `05.05.2026 ; RADIOTAXI ROMA ; DEBIT ; Corsa ; -18.00 ; EUR`. Urban: exempt under art 10(1)(14), no IVA. Otherwise blocked under (e). No VP5 either way.

**Fuel.** `12.05.2026 ; Q8 ; DEBIT ; Carburante ; -122.00 ; EUR`. Invoice and card payment, 40% vehicle: EUR 100 net, EUR 22 IVA, EUR 8.80 in VP5. Bank line alone: Needs Input.

## Deadlines and filing

Dates are for 2026 periods. A date on a Saturday or holiday moves to the next working day (D.Lgs. 241/1997 art 18(1) for payments; the LIPE instructions for the LIPE). Payments due from 1 to 20 August may be made by 20 August without surcharge (D.L. 223/2006 art 37(11-bis), added by D.L. 16/2012 art 3-quater).

| Item | Rule | 2026 periods |
| --- | --- | --- |
| Monthly settlement and payment | By the 16th of the following month (DPR 100/1998 art 1(1)) | 16 May falls on a Saturday: Monday 18 May 2026. 16 August falls in the August window: 20 August 2026. December 2026: 16 January 2027 is a Saturday, so Monday 18 January 2027 on the current text. Held for 2027. |
| Quarterly payment, Q1 to Q3 | By the 16th of the second month after the quarter (DPR 542/1999 art 7(1)(a)) | Q1: Monday 18 May 2026 (16 May is a Saturday). Q2: 20 August 2026. Q3: 16 November 2026. |
| Quarterly payment, Q4 | With the annual balance: 16 March, or the DPR 435/2001 art 17(1) date with 0.40% for each month or part (art 7(1)(b)) | 16 March 2027 on the current text. Held for 2027. |
| Special quarterlies | Fuel distributors, hauliers for third parties, public service operators under art 74(4) and health professions: no 1% interest, Q4 by 16 February of the next year (art 73(1)(e), art 74(4); Agenzia). Subfornitori under art 74(5): quarterly payment, no interest. | Q4: 16 February 2027 on the current text. Held for 2027. |
| LIPE | Last day of the second month after each quarter (D.L. 78/2010 art 21-bis(1)). Q2 is by 30 September: the legacy 16 September was wrong. Q4 may instead go in an annual return filed by the end of February. | Q1: 31 May is a Sunday, so Monday 1 June 2026. Q2: 30 September 2026. Q3: 30 November 2026. Q4: 28 February 2027 is a Sunday, so Monday 1 March 2027 on the current text. Held for 2027. |
| Acconto | By 27 December (L. 405/1990 art 6(2)) | 27 December 2026 is a Sunday: Monday 28 December 2026 |
| Annual return | 1 February to 30 April of the next year (DPR 322/1998 art 8(1)) | 2025 return: 1 February to 30 April 2026. 2026 return: same dates on the current text. Held for 2027. |
| Annual balance | By 16 March, or in equal instalments with the last by 16 December at 0.33% a month, or deferred to 30 June with 0.40% for each month or part after 16 March, then to 30 July with 0.40% on the 30 June sum (annual instructions; D.Lgs. 241/1997 art 20 and ris. 73/E 2017 as cited there) | For 2025: 16 March 2026 |
| Intrastat | By the 25th of the month after the reference period (D.L. 331/1993 art 50(6-bis)) to the Agenzia delle dogane e dei monopoli | Monthly or quarterly period is set by a decree not read |
| Cross-border data | D.Lgs. 127/2015 art 1(3-bis), through SDI for operations from 1 July 2022: sales to persons not established in Italy within the issue dates for the invoice or receipt; purchases from them by the 15th of the month after receipt of the document or the operation | Exceptions are under Related filings |

**Who files the LIPE.** Every taxpayer who settles periodically, even in credit. Not those with no annual return duty or periodic settlement duty, if that stays so all year (art 21-bis(3)). One communication per period (art 21-bis(4)): monthly filers fill one module per month inside the quarterly filing, and quarterly filers one module.

**Who files the annual return.** Those with IVA activity. These cases, read in the instructions, do not: those who made only art 10 exempt operations (unless they had art 19-bis.2 adjustments, intra-EU operations or reverse-charge purchases), forfettari for a whole year, art 34(6) farmers, art 74(6) entertainment non-optants, and sole traders who only rented their business. The instructions list is not reproduced in full: read it before relying on an exclusion.

### Filing the LIPE

1. Build the VP lines from the working paper and have the reviewer approve them. This workflow does not file or pay.
2. Prepare the file to the Agenzia's xml specification (provvedimento of 21 March 2018), with control software, or use the web interface.
3. Sign in to Fatture e Corrispettivi at https://www.agenziaentrate.gov.it, or use another Agenzia channel. The taxpayer or an intermediary sends it, telematically only.
4. Collect the receipt from the reserved area or Fatture e Corrispettivi. If rejected, retransmit within 5 days of the notice: the filing then counts as timely (circ. 195/1999).
5. Pay VP14 col 1 by F24 online by the payment date above, not the LIPE date. Quarterly filers add the 1% and use codes 6031 to 6033. Monthly filers use 6001 to 6012.
6. To correct, send a new LIPE before the annual return. After that, correct in the annual return (ris. 104/E 2017).

**Annual return.** File directly through Entratel or Fisconline, or by an intermediary. Late by up to 90 days: valid, with penalties. Later: treated as omitted, though it can be a title for collection (DPR 322/1998 art 2(7), applied by art 8). Volume d'affari is line VE50. Refund claims are in VX4.

### Registration

- Start: declaration within 30 days of starting a business, art or profession, or setting up a stable organisation in Italy, on approved models, online or in person (art 35(1), (6)). The text read sets no turnover floor. The Agenzia assigns the Partita IVA.
- Contents: identity, activity, places, website and internet provider for e-commerce (art 35(2)).
- Intra-EU operations: state the intention in the declaration (art 35(2)(e-bis)). This enters the taxpayer in the VIES database at once. A taxpayer filing no list for 4 consecutive quarters is presumed to have stopped, and the Agenzia removes it after notice (art 35(7-bis)).
- Changes and cessation: within 30 days (art 35(3)); a fiscal domicile transfer takes effect from the 60th day. Cessation runs from the end of liquidation (art 35(4)).
- Expected turnover: a starter who expects a volume d'affari that brings special duties or calculation rules states it in the declaration and follows the rules for that volume (art 35(5)).
- Non-residents: direct identification under art 35-ter before operations begin, or a fiscal representative under art 17(3), jointly liable. R-IT-7.

### Credits and refunds

A year-end credit carries to the next year, or is refunded in the art 30 cases: (a) mainly lower-rate sales, counting art 17 and art 17-ter sales; (b) art 8, 8-bis and 9 operations above 25% of all operations; (c) tax on buying or importing depreciable goods and on goods and services for studies and research, for that tax only; (d) mainly art 7 to 7-septies non-territorial operations; (e) art 17(3) non-residents; and cessation, with no minimum. Outside those, where the year and the 2 prior years each show a credit, a refund is open up to the lower credit of the 2 prior years, even under EUR 2,582.28. Art 38-bis(1): refund within 3 months of the return, with 2% interest a year from the 90th day after filing, leaving out the time from notice of a document request to delivery of the documents where that time exceeds 15 days. Quarterly refunds are in art 38-bis(2). Offset in F24 follows the rates table. Visto rules for offset are in the annual instructions.

## Penalties and interest

D.Lgs. 471/1997 as amended by D.Lgs. 87/2024, which applies to violations from 1 September 2024 (art 5(1)). Earlier violations keep the earlier text, which was not read. The legacy file covered only the quarterly interest.

| Violation | Penalty | Source |
| --- | --- | --- |
| Quarterly interest | 1% on amounts to pay. The legacy 'net IVA payable for the quarter' and 'approximate' are replaced: the base is the amount to pay. | DPR 542/1999 art 7(3) |
| LIPE omitted, incomplete or untrue | EUR 500 to 2,000; halved if filed or corrected within 15 days of the due date | Art 11(2-ter) |
| Annual return omitted | 120% of the tax, minimum EUR 250 | Art 5(1) |
| Annual return omitted, only operations with no tax due, or other art 5(3) case with no debt | EUR 250 to 2,000 | Art 5(3) |
| Annual return filed over 90 days late, within the art 57 period and before formal knowledge of any check | Art 13(1) sanction tripled on the tax due. No tax due: the EUR 250 minimum. | Art 5(1-bis) |
| Same lateness and timing, for a person within art 5(3) with no tax due | EUR 150 to 1,000 | Art 5(3) |
| Annual return faithless | 70% of the additional tax due or the difference in credit used, minimum EUR 150. Outside art 5(4-bis) cases, reduced by a third where the additional tax or the reduced deductible or refundable credit is under 3% of the tax or credit declared and under EUR 30,000. Art 5(4-bis): increased by half to double for false invoices or documents, non-existent operations, artifice or deception, or simulated or fraudulent conduct; a customer who used invoices for subjectively non-existent operations is caught only if taking part in the fraud is proved. Art 5(4.1): on an integrative return filed within the art 57 time and before formal knowledge of an audit, the art 13(1) penalty doubled on the tax due, or the art 5(4) minimum if no tax is due. | Art 5(4), (4.1), (4-bis), (4-ter) |
| Late payment | 25% of the unpaid amount. Within 90 days: half. Within 15 days: one fifteenth of the halved amount per day. | Art 13(1) |
| Undue credit used | Non spettante: 25% of the credit offset, also where a required administrative step, not on pain of forfeiture, is missed and not cured in time. Cured by the income tax return date for the year of the breach, or within a year if there is no return, the penalty on a missed instrumental step is EUR 250. Inesistente: 70%, increased by half to double under art 13(5-bis) for credits within D.Lgs. 74/2000 art 1(1)(g-quater)(2), which was not read. | Art 13(4-bis), (4-ter), (5), (5-bis) |
| Refund without basis | 25% | Art 5(5) |
| Registration declaration | EUR 500 to 2,000; one fifth of the minimum if regularised within 30 days of the invite | Art 5(6) |
| Invoice or registration failure on taxable operations | 70% of the tax, minimum EUR 300; EUR 250 to 2,000 if it did not affect the settlement | Art 6(1), (4) |
| Same by the supplier, for non imponibile, exempt, non-taxed or reverse-charge operations | 5% of the amount, minimum EUR 300; EUR 250 to 2,000 if it does not count even for income | Art 6(2), (4) |
| No receipt or transport document, or one understated | 150% of the tax on the amount undocumented, minimum EUR 300 | Art 6(3), (4) |
| Daily receipts data under art 2 D.Lgs. 127/2015 | 70%, minimum EUR 300 in the art 6(4) cases | Art 6(2-bis), (4) |
| Undue deduction | 70% of the deduction. Tax wrongly charged at too high a rate, or on exempt, non imponibile or non-taxed operations, and paid by the supplier: customer EUR 250 to 10,000, deduction kept only for the tax actually due, and not in fraud or abuse of rights. These penalties do not apply if the breach produced a faithless return punished under art 5(4). | Art 6(6) |
| Customer without a regular invoice | 70%, minimum EUR 250, unless reported through Agenzia tools within 90 days | Art 6(8) |
| Reverse charge omitted | EUR 500 to 10,000. Not in the accounts: 5% of the taxable amount, minimum EUR 1,000. | Art 6(9-bis) |
| Tax wrongly charged where reverse charge applied | EUR 250 to 10,000, with deduction kept and the customer not paying again | Art 6(9-bis.1) |
| Reverse charge on non-taxable operations | Debt and deduction both struck out on assessment; see art 6(9-bis.3) | Art 6(9-bis.3) |
| Exports | 50% where goods do not leave in time; same for art 41 goods not arriving in 90 days; neither applies if, in the next 30 days, the invoice is regularised and the tax paid. 70% for a missing dichiarazione d'intento. | Art 7(1), (3) |
| Books and records | EUR 1,000 to 8,000, with the art 9(3) reductions and doubling | Art 9(1), (3) |
| Return not on the model, or with missing or inexact data | EUR 250 to 2,000 | Art 8(1) |
| The violations art 11(1) lists | EUR 250 to 2,000 | Art 11(1) |
| Cross-border data omitted or wrong | For operations from 1 July 2022: EUR 2 per invoice, maximum EUR 400 a month; halved, maximum EUR 200 a month, if sent or corrected within 15 days of the D.Lgs. 127/2015 art 1(3-bis) due dates. The combined violations rule in D.Lgs. 472/1997 art 12 does not apply. | Art 11(2-quater) |
| Daily receipts data omitted, late, incomplete or untrue | Where the tax was not affected: EUR 100 per transmission, maximum EUR 1,000 a quarter. D.Lgs. 472/1997 art 12 does not apply. The same applies to the electronic payment duties in D.Lgs. 127/2015 art 2(3), except where recorded electronic payment operations and accepted electronic payments differ by not more than 5% (added by D.Lgs. 148/2026 art 33(1)(a); art 33(1)(b) adds the same exception to art 12(2)). | Art 11(2-quinquies) |
| Intrastat | EUR 500 to 1,000 per list, halved if filed within 30 days of the request. None if the data are completed or corrected, even on request. | Art 11(4) |
| Accessory sanctions | Sanction above EUR 50,000: 3 to 6 months. Above EUR 100,000: up to 12 months. Art 12(1-bis) halves the limits for the persons it names. | Art 12(1), (1-bis) |

**Ravvedimento, D.Lgs. 472/1997 art 13.** The penalty is reduced if the taxpayer corrects, paying the tax due and interest at the legal rate at the same time (art 13(2)). For Agenzia taxes the bar is notice of a liquidation or assessment act, as art 13(1-ter) states. Limbs: (a) unpaid tax or acconto, 1/10 of the minimum within 30 days; (a-bis) 1/9 within 90 days of the error, or of the due date of the return it is in; (b) 1/8 by the due date of the return for the year of the violation; (b-bis) 1/7 after that date; (b-ter) 1/6, (b-quater) 1/5 and (b-quinquies) 1/4 after a schema d'atto or a constatazione, on the terms each limb sets; (c) 1/10 of the minimum for an omitted return filed up to 90 days late. The legal interest rate was not read. Art 12 of that decree on combined violations excludes payment violations.

## Sources

Read on means the date read for this conversion. Limits follow each source. Normattiva is the official Italian law database. Articles were read in the text in force at retrieval; those marked 'retained' were read from an earlier phase's copy.

| Source | URL | Read on |
| --- | --- | --- |
| DPR 633 art 1, scope. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art1!vig= | 2026-11-05 |
| DPR 633 art 2, supplies of goods. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art2!vig= | 2026-11-05 |
| DPR 633 art 3, supplies of services. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art3!vig= | 2026-11-05 |
| DPR 633 art 4, business activity. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art4!vig= | 2026-11-05 |
| DPR 633 art 5, arts and professions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art5!vig= | 2026-11-05 |
| DPR 633 art 6, tax point. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art6!vig= | 2026-11-05 |
| DPR 633 art 7, definitions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7!vig= | 2026-11-05 |
| DPR 633 art 7-bis, place of goods. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7bis!vig= | 2026-11-05 |
| DPR 633 art 7-ter, place of services. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7ter!vig= | 2026-11-05 |
| DPR 633 art 7-quater, service exceptions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7quater!vig= | 2026-11-05 |
| DPR 633 art 7-quinquies, culture and sport. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7quinquies!vig= | 2026-11-05 |
| DPR 633 art 7-sexies, B2C exceptions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7sexies!vig= | 2026-11-05 |
| DPR 633 art 7-septies, non-EU consumers. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7septies!vig= | 2026-11-05 |
| DPR 633 art 8, exports. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art8!vig= | 2026-11-05 |
| DPR 633 art 8-bis, operations treated as exports. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art8bis!vig= | 2026-11-05 |
| DPR 633 art 9, international services. Read in part: the paragraphs this file cites. Limbs 1 to 5 read. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art9!vig= | 2026-11-05 |
| DPR 633 art 10, exemptions. Read in part: the paragraphs this file cites. Numbers 1, 2, 8, 8-bis, 8-ter, 14, 15, 16, 18, 19, 20, 21 and 27-ter. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art10!vig= | 2026-11-05 |
| DPR 633 art 13, base. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art13!vig= | 2026-11-05 |
| DPR 633 art 15, exclusions from the base. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art15!vig= | 2026-11-05 |
| DPR 633 art 16, rates. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art16!vig= | 2026-11-05 |
| DPR 633 art 17, debtor and reverse charge. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art17!vig= | 2026-11-05 |
| DPR 633 art 17-ter, split payment. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art17ter!vig= | 2026-11-05 |
| DPR 633 art 18, rivalsa. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art18!vig= | 2026-11-05 |
| DPR 633 art 19, deduction. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19!vig= | 2026-11-05 |
| DPR 633 art 19-bis, deduction percentage. Read in full. The URN returned art 19-bis.1, so this was opened from the act page; the URL is the act. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633!vig= | 2026-11-05 |
| DPR 633 art 19-bis.1, limits on deduction. Read in part: the paragraphs this file cites. Letters (a) to (i) and their notes. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19bis.1!vig= | 2026-11-05 |
| DPR 633 art 19-bis.2, adjustment. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19bis.2!vig= | 2026-11-05 |
| DPR 633 art 21, invoices. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art21!vig= | 2026-11-05 |
| DPR 633 art 21-bis, simplified invoice. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art21bis!vig= | 2026-11-05 |
| DPR 633 art 22, invoice on request. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art22!vig= | 2026-11-05 |
| DPR 633 art 23, sales register. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art23!vig= | 2026-11-05 |
| DPR 633 art 24, receipts register. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art24!vig= | 2026-11-05 |
| DPR 633 art 25, purchase register. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art25!vig= | 2026-11-05 |
| DPR 633 art 26, variations. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art26!vig= | 2026-11-05 |
| DPR 633 art 27, monthly settlement. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art27!vig= | 2026-11-05 |
| DPR 633 art 30, year-end credit. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art30!vig= | 2026-11-05 |
| DPR 633 art 33. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art33!vig= | 2026-11-05 |
| DPR 633 art 34, farming. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art34!vig= | 2026-11-05 |
| DPR 633 art 35, registration. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art35!vig= | 2026-11-05 |
| DPR 633 art 35-ter, direct identification. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art35ter!vig= | 2026-11-05 |
| DPR 633 art 36, separate activities. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art36!vig= | 2026-11-05 |
| DPR 633 art 38-bis, refunds. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art38bis!vig= | 2026-11-05 |
| DPR 633 art 67, imports. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art67!vig= | 2026-11-05 |
| DPR 633 art 70, import tax. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art70!vig= | 2026-11-05 |
| DPR 633 art 70-bis, VAT group. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art70bis!vig= | 2026-11-05 |
| DPR 633 art 70-terdecies, EU franchise. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art70terdecies!vig= | 2026-11-05 |
| DPR 633 art 70-quaterdecies, EU franchise conditions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art70quaterdecies!vig= | 2026-11-05 |
| DPR 633 art 74, special sectors. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art74!vig= | 2026-11-05 |
| DPR 633 art 74-sexies, special scheme. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art74sexies!vig= | 2026-11-05 |
| DPR 633 Tabella A. Read in part: the paragraphs this file cites. Parts II, II-bis and III, for the items named; opened from the act page, so the URL is the act. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633!vig= | 2026-11-05 |
| D.L. 331/1993 art 38, intra-EU acquisitions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art38!vig= | 2026-11-05 |
| D.L. 331/1993 art 40, place. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art40!vig= | 2026-11-05 |
| D.L. 331/1993 art 41, intra-EU supplies. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art41!vig= | 2026-11-05 |
| D.L. 331/1993 art 46, invoices. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art46!vig= | 2026-11-05 |
| D.L. 331/1993 art 47, registration. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art47!vig= | 2026-11-05 |
| D.L. 331/1993 art 50, lists. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art50!vig= | 2026-11-05 |
| D.L. 41/1995 art 36, margin scheme. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1995-02-23;41~art36!vig= | 2026-11-05 |
| D.L. 78/2010 art 21-bis, LIPE. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art21bis!vig= | 2026-11-05 |
| D.L. 98/2011 art 27, regime di vantaggio. Read in part: the paragraphs this file cites. Repeal note. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-07-06;98~art27!vig= | 2026-11-05 |
| D.L. 16/2012 art 3-quater, August date. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-03-02;16~art3quater!vig= | 2026-11-05 |
| D.Lgs. 127/2015 art 1, e-invoices and cross-border data. Read in part: the paragraphs this file cites. Commi 3, 3-bis and 6. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig= | 2026-11-05 |
| D.Lgs. 127/2015 art 2, daily receipts. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art2!vig= | 2026-11-05 |
| DPR 100/1998 art 1, monthly settlement. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-03-23;100~art1!vig= | 2026-11-05 |
| DPR 542/1999 art 6, annual balance. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1999-12-14;542~art6!vig= | 2026-11-05 |
| DPR 542/1999 art 7, quarterly option. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1999-12-14;542~art7!vig= | 2026-11-05 |
| DPR 322/1998 art 8, annual return. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art8!vig= | 2026-11-05 |
| DPR 600/1973 art 18, simplified accounts. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art18!vig= | 2026-11-05 |
| L. 405/1990 art 6, acconto. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-12-29;405~art6!vig= | 2026-11-05 |
| L. 488/1999 art 7, renovation. Read in part: the paragraphs this file cites. Comma 1(b). | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-23;488~art7!vig= | 2026-11-05 |
| L. 191/2009 art 2, comma 11. Read in part: the paragraphs this file cites. Comma 11 only. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2009-12-23;191~art2!vig= | 2026-11-05 |
| TUIR art 102, depreciation. Read in part: the paragraphs this file cites. Comma 5. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art102!vig= | 2026-11-05 |
| D.Lgs. 241/1997 art 17, offset. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art17!vig= | 2026-11-05 |
| D.Lgs. 241/1997 art 18, due dates. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art18!vig= | 2026-11-05 |
| D.Lgs. 241/1997 art 19, payment. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art19!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 7, export penalties. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art7!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 8, return content. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art8!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 9, records. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art9!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 11, other violations. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 12, accessory sanctions. Read in part: the paragraphs this file cites. Commi 1, 1-bis and 2. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art12!vig= | 2026-11-05 |
| D.Lgs. 472/1997 art 12, combined violations. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art12!vig= | 2026-11-05 |
| D.Lgs. 148/2026, act page. Read in part: the paragraphs this file cites. Header and in-force date. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 12, deduction limit. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art12!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 33. Read in full. Other articles of the decree not read. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art33!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 34. Read in part: the paragraphs this file cites. Searched for an application clause. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art34!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 35. Read in part: the paragraphs this file cites. Searched for an application clause. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art35!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 36. Read in part: the paragraphs this file cites. Searched for an application clause. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art36!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 37. Read in part: the paragraphs this file cites. Searched for an application clause. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art37!vig= | 2026-11-05 |
| D.Lgs. 10/2026, Testo unico IVA, decree page. Read in part: the paragraphs this file cites. Header and in-force date. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10!vig= | 2026-11-05 |
| Testo unico IVA art 1. Read in part: the paragraphs this file cites. Read to confirm the text; the Testo unico is not mapped. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art1!vig= | 2026-11-05 |
| Testo unico IVA art 169. Read in part: the paragraphs this file cites. Read to confirm the text; the Testo unico is not mapped. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art169!vig= | 2026-11-05 |
| Testo unico IVA art 170, repeals. Read in full. Not mapped article by article to 2026 provisions. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art170!vig= | 2026-11-05 |
| Testo unico IVA art 171, application. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art171!vig= | 2026-11-05 |
| D.Lgs. 173/2024 Allegato art 102, application. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig= | 2026-11-05 |
| D.Lgs. 141/2026, decree page. Read in part: the paragraphs this file cites. Header and in-force date. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-05;141!vig= | 2026-11-05 |
| D.Lgs. 141/2026 Allegato art 367, repeals. Read in part: the paragraphs this file cites. Comma 1(d). | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-05;141:1~art367!vig= | 2026-11-05 |
| D.Lgs. 141/2026 Allegato art 368, application. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-05;141:1~art368!vig= | 2026-11-05 |
| Agenzia, Come pagare l'IVA. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva-imprese | 2026-11-05 |
| Agenzia, F24 IVA periodica. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24ivap10/come-e-quando-si-versa | 2026-11-05 |
| Agenzia, Norme generali e aliquote. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/iva-regole-generali-aliquote-esenzioni-pagamento/norme-generali-e-aliquote-imprese | 2026-11-05 |
| Agenzia, LIPE: che cos'e. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/infogen_comunicaz_liquidaz_per_iva | 2026-11-05 |
| Agenzia, LIPE FAQ. Read in part: the paragraphs this file cites. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/faq-liquidaz-iva | 2026-11-05 |
| Agenzia, LIPE model and instructions page. Read in full. Links to the file edition used. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/modello-e-istruzioni-_comunicaz-liquidaz-per-iva | 2026-11-05 |
| Agenzia, LIPE norms page. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/normativa-e-prassi-comunicazione-delle-liquidazioni-periodiche-iva | 2026-11-05 |
| Agenzia, LIPE transmission page. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/modalita_trasmissione_liquidaz_per_iva | 2026-11-05 |
| Agenzia, LIPE model and instructions, file edition 2024. Read in part: the paragraphs this file cites. General instructions and lines VP1 to VP14; local text extract. The form page links this edition. | https://www.agenziaentrate.gov.it/portale/documents/20143/5986193/IVA+period_2024.pdf/04990f53-edc9-048a-c953-49592ebea05f?t=1742281742832 | 2026-11-05 |
| Agenzia, LIPE model and instructions, file edition 2023. Read in part: the paragraphs this file cites. Compared with the 2024 edition; local text extract. | https://www.agenziaentrate.gov.it/portale/documents/20143/289118/IVA+periodica_2023.pdf/8828af2c-ef09-69e9-d259-6ac3d189ddc6 | 2026-11-05 |
| Agenzia provvedimento 73203 of 4 April 2018, payment means for fuel and lubricants. Read in full. Administrative statement; local text extract. | https://www.agenziaentrate.gov.it/portale/documents/20143/296703/Provvedimento+04042018+mezzi+pagamento_PROVVEDIMENTO+N_73203+DEL+04-04-2018.pdf/e0e18c4f-b1e5-dfd9-8196-2cac72e65717 | 2026-11-05 |
| Agenzia circ. 8/E of 30 April 2018, fuel sales and payment. Read in part: the paragraphs this file cites. Introduction and the passages on payment means; searched for other art 19-bis.1(d) costs, none named; local text extract. | https://www.agenziaentrate.gov.it/portale/documents/20143/297557/Circolare+n+8+del+30+04+2018_Circolare_N_8_30042018.pdf/7972d001-311b-31f0-f4a0-f7cb1f75090c | 2026-11-05 |
| Agenzia, Dichiarazione IVA 2026 instructions. Read in part: the paragraphs this file cites. Sections on filing, payment, VL, VE, VJ and VX lines and refunds; local text extract. | https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711 | 2026-11-05 |
| MEF note on the split payment extension. Read in full. Press note, reporting a decision whose Official Journal text was not obtained. | https://www.finanze.gov.it/it/archivi/notizie/dettaglio-notizie/Pubblicata-la-decisione-di-proroga-dello-Split-Payment-00001 | 2026-11-05 |
| D.Lgs. 471/1997 art 5, return penalties. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art5!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 6, documents and deduction. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art6!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 13, payment. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig= | 2026-11-05 |
| D.Lgs. 472/1997 art 13, ravvedimento. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig= | 2026-11-05 |
| D.Lgs. 87/2024 art 5, application. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-06-14;87~art5!vig= | 2026-11-05 |
| DPR 322/1998 art 2, comma 7. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig= | 2026-11-05 |
| L. 207/2024 art 1, commi 57 to 63. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig= | 2026-11-05 |
| L. 190/2014 art 1, regime forfettario. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig= | 2026-11-05 |
| DPR 435/2001 art 17, payment dates. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2001-12-07;435~art17!vig= | 2026-11-05 |

Cited only as they appear in a text above, and not read on their own: DPR 633 art 73(1)(e), in art 74; c.c. art 2359, L. 196/2009 and D.L. 84/2025, in art 17-ter and its notes; D.L. 95/2025 and D.Lgs. 186/2025, in the DPR 633 amendment notes; L. 217/1983 and L. 457/1978, in Tabella A; D.L. 112/2008 and L. 244/2007, in the art 19-bis.1 notes; L. 205/2017 art 1(922) and (923), in the 2018 provvedimento and circ. 8/E 2018; D.L. 155/1993, in the note to L. 405/1990 art 6; D.L. 223/2006, in D.L. 16/2012 art 3-quater; D.Lgs. 74/2000 art 1, in D.Lgs. 471/1997 art 13; D.L. 262/2006, circ. 195/1999 and ris. 104/E 2017, in the LIPE instructions; L. 388/2000 art 34 and ris. 73/E 2017, in the annual instructions; the provvedimento of 21 March 2018, on the Agenzia LIPE pages.

Not yet confirmed: which text governs the Q4 2026 LIPE, Q4 payment, December 2026 monthly payment, annual return and acconto rules for filings made in 2027, and the Testo unico numbering for 2027 periods, including the replacement for D.L. 78/2010 art 21-bis; the transition for deduction rights that arose before D.Lgs. 148/2026 art 12 took effect, and any application clause in articles of that decree not read; the amending act that puts EUR 500,000 and EUR 800,000 into DPR 542/1999 art 7, which prints lire, and the same for the euro amounts of lire 5 million in art 30 and 1 million lire in art 19-bis.2(5); the conflict between L. 190/2014 art 1(58)(e-bis) and (60) on payment dates; the Official Journal text of Decision (EU) 2026/1728, where EUR-Lex returned a bot challenge and the MEF note was used instead, and the 2015 ministerial decree on split payment mechanics; the current EU derogation for the 40% vehicle limit; whether the art 19-bis.1(d) payment sentence reaches costs other than fuel and lubricants; Tabella B letter (f), which takes some vehicles outside the 40% rule; the 2008 ministerial decree defining representation costs; the reach of art 19-bis.1(f) over restaurant service; the legacy statement that import IVA can be deferred to the LIPE since 2022, which no text read supports; L. 244/2007 art 1(18) on renovation; the legal interest rate; the VP12 base and any interest on a carried quarterly amount; the F24 code 6099 in a sibling guide, where the Agenzia code page returned 404; the Intrastat periodicity decree and the art 50(6) provvedimento, including whether a service purchase is listed; the D.L. 746/1983 dichiarazione d'intento rules; the LIPE treatment of the L. 207/2024 art 1(59) logistics option; the reach of D.Lgs. 74/2000 art 1(1)(g-quater)(2); the volume d'affari definition in art 20, which was not read, with line VE50 used; the R-EU-1 to R-EU-11 catalogue; every legacy billing entity, the ABI causale codes and the bank column layouts; the format of the Partita IVA as 'IT + 11 digits'; and the penalty text before the D.Lgs. 87/2024 amendments, for older violations.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.3 | 2026-11-05 | Converted to the upstream template. Tax year moved to 2026 with the 2027 Testo unico boundary stated. Replaced the VP table and field mappings; corrected the Q2 LIPE date, VP14 formula, 0% label, EU services label, spices rate, taxi, flights, telephony, representation, vehicle tests, EUR 516.46 role and processor fees. Added penalties, registration, refunds, split payment persons, the forfettario conflict, D.Lgs. 148/2026 deduction limit, R-IT-9 and Needs Input defaults. Moved onboarding to intake only. |
| 2.2 | November 2026 | Legacy: quarterly limit for services corrected to EUR 500,000. |
| 2.1 | April 2026 | Legacy: full rewrite to the Malta v2.1 structure, 10 sections, country-specific supplier pattern library. |
| 1.0 | | Legacy: initial skill. |

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` and `eu-vat-directive`.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista, revisore legale, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
