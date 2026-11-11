---
name: italy-vat-return-reference
description: Reference sections for italy-vat-return (Deadlines and filing, Penalties and interest, Cross-border points, Ask the client first, Who this applies to), moved from the parent skill word for word so each file stays under the size limit. MUST load alongside italy-vat-return.
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

## Cross-border points

Place of supply rules are owned by `eu-vat-directive`. The Italian mechanics are below.

- **Services sold to EU businesses.** Art 7-ter places them where the taxable customer is. Invoice without IVA, with the words 'inversione contabile' (art 21(6-bis)(a)), by the 15th of the next month, except art 10 nn 1 to 4 and 9. The legacy 'non imponibile' and 'Art. 196' note are replaced. Confirm the customer is a taxable person: check VIES. OUT-N in VP2. Intrastat: subject to the hold under Related filings.
- **Services sold outside the EU.** Invoice with 'operazione non soggetta' (art 21(6-bis)(b)). OUT-N in VP2. Arts 7-quater and 7-quinquies have exceptions: land, passenger transport, restaurants, short-term hire, culture and sport. Read them where they may apply.
- **Goods sold to EU businesses.** Non imponibile under D.L. 331/1993 art 41(1)(a). Art 41(2-ter) requires the customer's VAT number and the seller's list under art 50(6), or a justified failure. Invoice by the 15th of the next month, with the customer's VAT number (art 46(2)). Art 50(2) lets the office confirm the number. Without those conditions, Needs Input.
- **Exports.** Art 8(1)(a) by or for the seller; (b) by the non-resident buyer within 90 days; (b-bis) travellers and aid within 180 days; (c) purchases without IVA for regular exporters on a dichiarazione d'intento, whose decree was not read: Needs Input.
- **Services bought from abroad.** Reverse charge per Classification rules. An exempt service stays exempt: no tax arises. Art 10 and arts 7 to 7-septies still apply before reverse charge.
- **Goods bought from the EU.** Intra-EU acquisition. A person within art 38(5)(c) needs the EUR 10,000 test. Triangular operations under art 40(2) and art 41 go in VP3 but are Needs Input here.
- **Imports.** See Classification rules. Art 67 defines them.
- **Exempt and small persons abroad.** See R-IT-7 for the EU franchise. Its EU limit is EUR 100,000 and its Italian limit EUR 85,000 or the lower art 1(54) amount (art 70-quaterdecies).

## Ask the client first

Ask for these 6 facts at the start. The workflow base's confirmation step carries them.

1. **Regime and registration:** regime ordinario, forfettario or minimi, with the Partita IVA, the legal form (ditta individuale, SRL or libero professionista), the business activity and any employees.
2. **Period and cadence:** the period, monthly or quarterly (art 7 option or special quarterly), last year's volume d'affari, the credits or small debts carried in (VP7, VP8, VP9) and the acconto.
3. **Sales:** any exempt sales, any supplies to Italian public administration or other art 17-ter bodies, and customers outside Italy (EU or non-EU, B2B or B2C, goods or services).
4. **Purchases:** a registered invoice or customs bill for each claim, any foreign suppliers or art 17(6) sectors, and the entity that bills you.
5. **Vehicles, phones and meals:** whether a vehicle is used only for the business, is the object of the activity or is used by an agent, how fuel and other vehicle costs are paid, the basis for splitting mixed use, and whether meals were for clients or for own or staff business travel.
6. **Special cases:** a VAT group, a margin scheme, a fiscal representative arrangement, or an agricultural or other special regime.

### Completion checks

- Regime and cadence confirmed; every refusal tested, with R-EU-1 to R-EU-11 handled as undefined.
- Period confirmed against 2026 rules; nothing carried into a 2027 period.
- VP lines match the table above, with no legacy VP use.
- VP14 uses the 2 formulas with their floors.
- Every VP5 amount has a document registered under art 25.
- Reverse-charge rows reach VP3, VP4 and VP5.
- Passenger transport, representation and food blocks tested; no 50% telephony rule applied.
- Vehicle share follows art 19-bis.1(c) and (d), with fuel payment proof.
- 1% applied for art 7 quarterlies only, and not on the acconto.
- Related filings flagged.
- Each default disclosed with its alternative.

## Who this applies to

Self-employed individuals and small businesses under the regime ordinario in Italy (Repubblica Italiana), and the reviewers working with them. The tax is the imposta sul valore aggiunto (IVA) under DPR 26 October 1972 n. 633 ('DPR 633'). The authority is the Agenzia delle Entrate. Currency is EUR only.

| Field | Value |
| --- | --- |
| Tax year | IVA periods in calendar 2026, read at 5 November 2026, under DPR 633 |
| Periodic return | Comunicazione Liquidazioni Periodiche IVA (LIPE), section VP, filed each quarter by monthly and quarterly filers alike |
| Annual return | Dichiarazione IVA |
| Payment | Modello F24, online only |
| Portal | Agenzia delle Entrate online services at https://www.agenziaentrate.gov.it: Fatture e Corrispettivi for the LIPE; Fisconline or Entratel for the annual return |
| Companion files | `vat-workflow-base` (workflow) and `eu-vat-directive` (EU directive). Both MUST be loaded. |

### What this file is

This is the return workflow file for Italy (`job: vat-return`), a country slot file for `vat-workflow-base`, which owns the workflow, output specification, question form and self-checks. `eu-vat-directive` owns the EU directive content. Read this file in full before classifying anything. Its status is Tier 2, pending review. No statement here has been approved by an accountant.

`eu-vat-directive` as loaded has no refusal catalogue. The legacy file cited 'R-EU-1 through R-EU-12' from it, but only R-EU-12 is defined, in `vat-workflow-base`. R-EU-1 to R-EU-11 are undefined in the files read. Do not invent them. If another file cites one, return Needs Input naming the missing contract, as Step 5 of the base requires. The legacy use of R-EU-5 for cross-border consumer sales is replaced by R-IT-9 below.

Every classification is a working paper for reviewer checking. Input IVA needs an invoice or customs bill registered under art 25; treat all credits as provisional until that is checked.

### The 2027 change

No Testo unico governs 2026 periods. These 3 consolidations are enacted and apply from 1 January 2027:

| Text | Applies from | Effect read |
| --- | --- | --- |
| Testo unico IVA, D.Lgs. 19 January 2026 n. 10, in force 31 January 2026 | 1 January 2027 (art 171) | Art 170 repeals from that date DPR 633 arts 1 to 17, 17-ter to 27, 30, 30-bis, 30-ter, 32, 34 to 36-bis, 38 to 39, 40-bis to 40-sexies, 62, 67 to 74-octies, 76, 77, 78, 80 to 94 and Tabelle A, B and C. It also repeals L. 405/1990 art 6, D.L. 331/1993 arts 36(5), (6), (19-bis), 37 to 52, 53(1) to (4), 56, 57(2), 58, 60 and 66(9-bis), (21), parts of D.L. 41/1995, D.Lgs. 127/2015 arts 1, 2 (most) and 4, and L. 190/2014 art 1(667). |
| Testo unico delle sanzioni, D.Lgs. 173/2024 Allegato | 1 January 2027 (art 102) | Normattiva prints the D.Lgs. 471/1997 articles read as in force to 31 December 2026 |
| Testo unico adempimenti e accertamento, D.Lgs. 5 August 2026 n. 141 | 1 January 2027 (art 368) | Art 367(1)(d) repeals DPR 633 arts 40, 51 to 54-bis, 54-bis.1(1), (2) and (5), 54-ter to 57, 60, 60-bis, 63 to 66-bis and 75 |

Article numbers below are the 2026 numbers. Do not carry them into 2027 periods. D.L. 78/2010 art 21-bis (LIPE) and L. 405/1990 art 6 (acconto) also print 'al 31-12-2026'. This file has not mapped their replacements, and filings made in 2027 for 2026 periods (Q4 LIPE, the annual return, the Q4 payment, the December 2026 monthly payment) are held on which text governs them. Apart from the rows marked held, the 2026 rules are stated as they stand at 5 November 2026.

### Refusals and boundaries

These are the country refusals for `vat-workflow-base`. If a trigger fires, stop, output the message verbatim and end, as Step 5 of the base requires. There is no partial classification. R-EU-12 applies as the base states it.

- **R-IT-1, regime forfettario.** Trigger: the client applies the regime forfettario under L. 190/2014 art 1(54) to (89), or entered or left it in the year in which the adjustment under art 1(61) to (63) falls. The trigger is the regime, not turnover: the legacy 'turnover below EUR 85,000' states only one entry condition. Message: 'Regime forfettario taxpayers do not charge IVA on their domestic invoices and cannot deduct input IVA. They do not file LIPE, or the annual Dichiarazione IVA for a whole year in the regime, but they can still owe IVA on reverse-charge purchases and intra-EU acquisitions. This skill covers the regime ordinario only.'
- **R-IT-2, regime dei minimi.** Trigger: the client is under the legacy regime dei minimi (contribuenti minimi), the regime di vantaggio of D.L. 98/2011 art 27. L. 190/2014 art 1(85) repealed it, and art 1(88) lets those in it at the end of 2014 continue only for the rest of the five-year period and in any case until age 35. Message: 'Regime dei minimi taxpayers have a simplified regime outside the ordinary IVA system. This skill covers the regime ordinario only.'
- **R-IT-3, split payment.** Trigger: the sales in the period include a supply to a person within DPR 633 art 17-ter(1) or (1-bis), where that person is not itself the debtor of the tax, outside (1-quinquies) and (1-sexies). The persons are listed under Split payment below. The legacy trigger named public administration bodies only. Message: 'Split payment (scissione dei pagamenti) applies to this customer, who pays the IVA to the Treasury instead of to the supplier (Art. 17-ter DPR 633/72). This is complex and out of scope. Please use a commercialista.'
- **R-IT-4, pro rata.** Trigger: the client makes both operations with a right of deduction and exempt operations that count in the art 19-bis percentage. The legacy 'not de minimis' test has no source: the statute has no floor. Exempt operations under art 10 nn 1 to 9 that are not the client's own activity, or that are accessory to taxable operations, do not count (art 19-bis(2)), so interest of that kind alone does not fire this; tax on goods and services used only for them stays non-deductible. Message: 'You make both taxable and exempt supplies. Input IVA must be apportioned under the pro rata rule (Art. 19 and 19-bis DPR 633/72). Please use a commercialista to determine the pro rata.'
- **R-IT-5, margin scheme.** Trigger: the client deals in second-hand goods, art, antiques or collectables and applies, or may apply, the regime of D.L. 41/1995 art 36. Message: 'Margin scheme transactions require transaction-level margin computation. Out of scope.'
- **R-IT-6, VAT group.** Trigger: the client is part of a VAT group under Art. 70-bis to 70-duodecies DPR 633/72, or of a group IVA settlement, for which the LIPE instructions set separate rules. Message: 'VAT groups require consolidation across the group. Out of scope.'
- **R-IT-7, non-resident.** Trigger: a non-resident supplier or client with a fiscal representative in Italy (art 17(3)) or identified directly (art 35-ter), or a taxpayer established in another member state using the franchise under arts 70-terdecies and 70-quaterdecies. Message: 'Non-resident registrations with fiscal representatives have specific obligations beyond this skill. Please use a commercialista.'
- **R-IT-8, income tax.** Trigger: the user asks about annual income tax (IRPEF, IRES, Modello Redditi) instead of IVA. Message: 'This skill only handles Italian VAT (IVA) returns. For income tax, use a dedicated Italian income tax skill.' The sibling is `it-income-tax`.
- **R-IT-9, cross-border consumer sales.** Trigger: the client makes intra-EU distance sales of goods or the art 7-octies(3)(b) services to consumers in other member states, and any of the conditions under Sales to EU consumers is not shown to hold; or the client uses the art 74-sexies special scheme or an import scheme. Message: 'These cross-border consumer sales may be taxable in the customer's Member State or reportable through a special scheme. This workflow does not prepare those returns. Please use a commercialista.'

**Special regimes not covered.** Agricultural producers (art 34), the sectors of art 74 and travel agents (art 74-ter) are not worked through in this file. Return Needs Input for them.

**Forfettario interaction.** The conditions and income tax effects belong to `it-income-tax`. For IVA, L. 190/2014 art 1 as read in the text in force from 12 August 2026 says: revenue or fees in the prior year, annualised, not above EUR 85,000, summed across ATECO codes (54, 55); no rivalsa of IVA on national operations (58(a)); no deduction (58 and 59); exempt from paying IVA and from the DPR 633 duties, except numbering and keeping purchase invoices and customs bills, certifying receipts and keeping documents (59). The regime ends the next year if the conditions fail, and in the same year if revenue exceeds EUR 100,000, with IVA due from the operation that takes it over the limit (71). An entrant or leaver adjusts (61 to 63), so R-IT-1 fires. For operations where the taxpayer is the debtor, it issues or completes the invoice (60) and pays. Comma 60 says by the 16th of the following month; comma 58(e-bis) says by the 16th of the second month after each calendar quarter for art 17 purchases, including intra-EU ones. That conflict is held. A forfettario supplier's invoice carries no IVA, so a regime ordinario buyer has nothing for VP5.

### Required inputs

| Level | Items | Policy |
| --- | --- | --- |
| Minimum viable | Bank statement for the period in CSV, PDF or pasted text, covering the full period, from any Italian or international business bank: UniCredit, Intesa Sanpaolo, Banco BPM, Monte dei Paschi di Siena, BPER Banca, Poste Italiane (BancoPosta), Revolut Business, Wise Business, N26 Business or any other | Hard stop if no bank statement is available |
| Recommended | Electronic invoices (fatture elettroniche) for the period from SDI (Sistema di Interscambio), purchase invoices, and the client's Partita IVA in writing. The legacy format is IT + 11 digits. | SOFT WARN |
| Ideal | Complete SDI extract (XML), prior period LIPE, Registri IVA (fatture emesse and acquisti), reconciliation of the VP8 and VP9 credits brought forward | SOFT WARN |

If only a bank statement is held, proceed and record in the reviewer brief: 'This LIPE was produced from bank statement alone. The reviewer must verify, before approval, that every input IVA claim is supported by a compliant invoice or customs bill registered under art 25, starting with claims above EUR 400, and that all reverse-charge classifications match the supplier's invoice.' EUR 400 is a working setting: the rule needs a document at any amount.

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
