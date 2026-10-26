---
name: france-vat-return
description: "French VAT (TVA) for tax year 2026: who must charge it, the franchise en base thresholds (EUR 85,000 and EUR 37,500, with the single EUR 25,000 threshold of the 2025 finance law repealed by loi n° 2025-1044), the 20%, 10%, 5.5% and 2.1% rates, the régime réel normal (monthly or quarterly CA3) and the régime simplifié (annual CA12 with July and December instalments) and their 2026 limits, the CA3 and CA12 lines, self-assessment (autoliquidation) on services and goods bought from abroad, the état récapitulatif and the déclaration européenne de services, the e-invoicing timetable (1 September 2026 and 1 September 2027), deduction restrictions, and penalties and late interest. Trigger on \"prepare CA3\", \"French VAT return\", \"TVA\", \"déclaration de TVA\", \"CA12\", \"franchise en base\", \"autoliquidation\". Out of scope: e-invoicing formats and platforms (france-einvoice), tax audits (fr-tax-audit), income and corporate tax (fr-income-tax, fr-corporate-tax), bookkeeping (france-bookkeeping)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/france-vat-return"
  jurisdiction: "FR"
  tax_year: "2026"
  last_updated: "2026-10-24"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# France: VAT and the VAT return (TVA, CA3 and CA12)

This skill covers French VAT for 2026: who is in and who is out, the rates, the two filing regimes and their limits, how to fill the CA3 and the CA12, self-assessment on cross-border purchases, the EU statements, the e-invoicing timetable, the deduction restrictions, and penalties and interest. Every figure was read on an official French page on 24 October 2026, unless the Sources table says otherwise. Load `vat-workflow-base` for the workflow architecture and `eu-vat-directive` for the EU directive content alongside it.

Two facts about the law itself in 2026:

- **The VAT articles are still in the Code général des impôts (CGI) for all of 2026.** Ordonnance n° 2025-1247 of 17 December 2025 moves them into book II of the Code des impositions sur les biens et services (CIBS). Ordonnance n° 2026-671 of 27 July 2026 put that move back from 1 September 2026 to 1 January 2027, and the old CGI references can still be used until 30 June 2028 (BOFiP, actualité of 7 October 2026). This skill cites the CGI article in force in 2026.
- **The 2026 finance law is loi n° 2026-103 of 19 February 2026.** For VAT it changed rate rules at the edges (waste services and cold networks to 5.5%, forestry work kept at 10%, among others), ended the exclusion of deduction for alcohol advertising from 21 February 2026, and amended the e-invoicing and e-reporting fines (CGI art. 1737 and 1788 D). It did not touch the franchise thresholds or the 20%, 10%, 5.5% and 2.1% rates.

## Who this applies to

- **Taxable persons established in France** who supply goods or services in France for consideration. They charge French VAT unless they sit inside the franchise en base or the supply is exempt.
- **The franchise en base (CGI art. 293 B).** A business established in France does not charge VAT, and does not deduct it, while its French turnover stays at or below the thresholds in the rates table. It files no CA3 and no CA12. Its invoices carry the words "TVA non applicable, art. 293 B du code général des impôts". It may opt to charge VAT.
- **The single EUR 25,000 threshold never applied.** The 2025 finance law (loi n° 2025-127, art. 32) set one threshold of EUR 25,000 from 1 March 2025. Loi n° 2025-1044 of 3 November 2025, art. 1, restored the separate thresholds with effect from 1 March 2025 itself. So for 2025 and 2026 the thresholds are the ones in the table below. Any page or skill that prints EUR 25,000 as the French franchise threshold is wrong.
- **Businesses established in another EU state** may use the French franchise if their EU-wide turnover is at or below EUR 100,000 in the previous and the current year and they have notified their own state (CGI art. 293 B bis). A French business that wants to use another state's franchise notifies the French administration and reports quarterly (CGI art. 293 B ter).
- **Régime réel normal.** Monthly CA3, or quarterly where the VAT due each year is below EUR 4,000 (CGI art. 287-2).
- **Régime simplifié (régime simplifié de déclaration).** One annual CA12 plus two instalments (CGI art. 287-3), for businesses inside the turnover band in the table and with VAT due of EUR 15,000 or less for the previous year (CIBS art. L. 162-4, L. 162-5, L. 162-7).
- **Out of this skill:** the overseas departments (their own rates, listed for recognition only; VAT is provisionally not applicable in Guyane and Mayotte), Corsica's special rates beyond the CA3 lines, the margin scheme, property VAT (TVA immobilière), VAT groups (CGI art. 256 C), and non-residents registering through a fiscal representative. Refuse or refer these (see Ask the client first).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate (CGI art. 278) | 20% | 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191854/2026-10-24 |
| Intermediate reduced rate (CGI art. 279): hotels, restaurant meals, passenger transport, most work on dwellings over two years old | 10% | 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/2026-10-24 |
| Reduced rate (CGI art. 278-0 bis): most food, books, energy-efficiency work on dwellings, water; waste services from 1 March 2026 (LF 2026 art. 81) | 5.5% | 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/2026-10-24 |
| Particular rate: reimbursable medicines (CGI art. 281 octies), first performances (art. 281 quater), press (art. 298 septies) | 2.1% | 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191656/2026-10-24 |
| Overseas departments (Guadeloupe, Martinique, Réunion): standard / reduced / particular | 8.5% / 2.1% / 1.75% and 1.05% | 2026 | https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom |
| Corsica, CA3 lines TC, T3, T4, T5 | 13%, 10%, 2.1%, 0.9% | 2026 | https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf |
| Franchise: total turnover, previous calendar year / current year (CGI art. 293 B, I) | EUR 85,000 / EUR 93,500 | 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-24 |
| Franchise: services other than on-site catering and accommodation, previous year / current year | EUR 37,500 / EUR 41,250 | 2026 | same |
| Franchise: lawyers', authors' and performers' regulated work, previous / current year (art. 293 B, I bis) | EUR 50,000 / EUR 55,000 | 2026 | same |
| Franchise: their other activities, previous / current year | EUR 35,000 / EUR 38,500 | 2026 | same |
| Franchise for an EU-established business: EU-wide turnover, previous and current year (art. 293 B bis) | EUR 100,000 | 2026 | same |
| Régime simplifié: previous year turnover, goods, on-site catering, accommodation (CIBS L. 162-4, 1°; amount fixed for 2026 by CIBS art. A. 162-7) | up to EUR 945,000 | 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000049803748/2026-10-24 |
| Régime simplifié: current year ceiling, same activities (CIBS L. 162-5, 1°; A. 162-7) | EUR 1,040,000 | 2026 | same |
| Régime simplifié: previous year turnover, other services incl. furnished lets (CIBS L. 162-4, 2°; A. 162-7) | up to EUR 286,000 | 2026 | same |
| Régime simplifié: current year ceiling, other services (CIBS L. 162-5, 2°; A. 162-7) | EUR 323,000 | 2026 | same |
| Régime simplifié: VAT due for the previous year must not exceed (CIBS L. 162-7) | EUR 15,000 | 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000044598127/2026-10-24 |
| Régime réel normal: quarterly CA3 where annual VAT due is below (CGI art. 287-2) | EUR 4,000 | 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191928/2026-10-24 |
| Régime simplifié instalments: July / December, share of previous year's tax before fixed-asset VAT (CGI art. 287-3) | 55% / 40% | 2026 | same |
| No instalments where previous year's tax (before fixed-asset VAT) is below (CGI art. 287-3) | EUR 1,000 | 2026 | same |
| Instalment change allowed where the real tax differs by at least (CGI art. 287-3) | 10% | 2026 | same |
| First year of a new business: each self-set instalment at least (CGI art. 287-3) | 80% of the half-year's real tax | 2026 | same |
| CA12 credit refundable at year end (frame VII) only where at least | EUR 150 | 2026 | https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf |
| Distance sales of goods and B2C digital services to other EU states stay French below (CA3 notice, line E3) | EUR 10,000 a year | 2026 | https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf |
| Intra-EU acquisitions by a business in the franchise: above this the French buyer self-assesses | EUR 10,000 | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F21746 |
| Invoices with total excluding VAT at or below this need not show the seller's VAT number (that particular only) | EUR 150 | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F31808 |
| Small equipment taken straight to expense, unit value excluding VAT up to (decides line 19 or line 20) | EUR 500 | 2026 | https://bofip.impots.gouv.fr/bofip/2109-PGP.html |
| Fuel: petrol, diesel and E85 in a vehicle excluded from deduction, or a lease the lessee cannot deduct / in any other vehicle | 80% / 100% deductible | from 2022 | https://bofip.impots.gouv.fr/bofip/1194-PGP.html |
| Fuel: LPG and other gaseous petroleum products in an excluded vehicle | 50% deductible | 2026 | same |
| Late interest (CGI art. 1727, III) | 0.20% a month | 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006147309/2026-10-24 |

**How the franchise thresholds bite.** The basic threshold is tested on the previous calendar year: crossing it brings VAT from 1 January of the next year. The higher threshold is tested on the current year: crossing it brings VAT from the day of the overrun itself (CGI art. 293 B, II), so invoices issued that day already carry VAT. In a start-up year, the turnover is scaled up to a full year before the test (service-public F21746).

**Where two official pages disagree.** The impots.gouv.fr page "Les régimes d'imposition à la TVA" (last modified 21 May 2026) still prints EUR 840,000 and EUR 254,000 as the régime simplifié limits. Those are the 2023-2025 values. The law settles it: CIBS art. L. 162-4 sets base amounts of EUR 818,000 and EUR 247,000 for 2020 to 2022 and indexes them on inflation every three years, rounded to the nearest thousand euros, and CIBS art. A. 162-7, as amended by the arrêté of 27 January 2026 (in force from 29 January 2026), fixes the 2026 amounts at EUR 945,000 / 1,040,000 and EUR 286,000 / 323,000. The BOFiP barème of 1 July 2026 and service-public F23566 give the same figures. Use the 2026 values.

## The taxable base

**What goes on the CA3 (form 3310-CA3-SD, 2026).** Read the line codes off the 2026 form only.

| CA3 line | What goes on it |
|---|---|
| A1 | Taxable sales and services, net |
| A2 | Other taxable operations: disposals of fixed assets, self-supplies, and purchases where the buyer is liable, including construction work received from a subcontractor (CGI art. 283-2 nonies) |
| A3 | Services bought from a supplier not established in France (CGI art. 283-2), EU or non-EU alike |
| A4 | Imports other than petroleum products, net |
| A5 | Exits from a suspensive regime |
| B1 | Petroleum products released for consumption |
| B2 | Intra-EU acquisitions of goods, net |
| B3 | Electricity, gas, heat or cold taxable in France |
| B4 | Goods or services from a taxable person not established in France (CGI art. 283-1) |
| B5 | Corrections on the taxed side, for example credit notes to customers |
| E1 | Exports outside the EU |
| E2 | Other non-taxable operations, including services to a customer established abroad and a subcontractor's construction work under art. 283-2 nonies |
| E3 | Distance sales taxable in another EU state |
| E4 | Imports, non-taxed side |
| F1 | Intra-EU acquisitions not taxable in France (never the counterpart of B2) |
| F2 | Zero-rated intra-EU supplies of goods to a taxable customer |
| F6 | Purchases free of tax (achats en franchise) |
| F8 | Corrections on the non-taxed side |
| 08 / 09 / 9B | Base and tax, mainland: 20% / 5.5% / 10% |
| 10 / 11 | Base and tax, overseas departments: 8.5% / 2.1% |
| T1 to T6 | Overseas particular rates (1.75%, 1.05%), Corsica (13%, 10%, 2.1%, 0.9%), mainland particular rate 2.1% (T6) |
| P1, P2 | Petroleum products, 20% and 13% |
| I1 to I6 | Import VAT by rate: 20%, 10%, 8.5%, 5.5%, 2.1%, 1.05% |
| 15 | VAT previously deducted to be paid back |
| 16 | Total gross VAT due |
| 17 / 18 | Memo lines: of which on intra-EU acquisitions / of which on operations to Monaco |
| 19 | Deductible VAT on fixed assets |
| 20 | Deductible VAT on other goods and services |
| 21 | Other VAT to deduct |
| 22 | Credit carried from line 27 of the previous return |
| 23 | Total deductible VAT |
| 24 / 2E | Memo: of which on imports / on petroleum products |
| 25 / TD | Credit (line 23 less 16) / VAT due (line 16 less 23) |
| 26 | Refund asked for on form 3519 |
| 27 | Credit carried forward, to line 22 of the next return |
| 28 / 29 / 32 | Net VAT due / assimilated taxes from annex 3310 A / total to pay |

Line 18 is a Monaco memo line, not the line for self-assessed EU services. A credit at line 25 does not excuse paying the assimilated taxes at line 29.

**The CA12 (form 3517-S-SD, 2026)** has its own numbering. Lines 5A, 06, 6C and 07 carry the standard, reduced, intermediate and overseas standard rates; line 19 is total gross VAT; line 20 deductions on invoices, 21 the flat-rate deduction, 22 their total; line 23 VAT on fixed assets; line 24 the credit brought in; line 26 total deductible; line 28 VAT due; line 29 credit; line 30 instalments. Line 57 is next year's instalment base: line 16 less lines 11, 12 and 22, which is before VAT on fixed assets. Below EUR 150 a year-end credit is refundable only on a disposal, death or entry into a VAT group; otherwise carry it to next year (line 51) or set it against the next instalment (line 52).

**Self-assessment (autoliquidation).**

- Services bought from a supplier not established in France, EU or not: base on A3, tax in the rate block (08, 09 or 9B), deduction at line 20 (CGI art. 283-2). Net nil for a fully taxable business. If an EU supplier wrongly charged its own VAT, that VAT is not French input VAT: reclaim it in that state.
- Intra-EU acquisitions of goods: base on B2, tax in the rate block and again as a memo at line 17, deduction at line 20 or 19.
- Imports: import VAT is self-assessed on the CA3 (base on A4, tax at I1 to I6, deduction at line 20 or 19 and memo at line 24). The return is pre-filled with customs data: reconcile it with the client's import records.
- Domestic reverse charges: construction subcontracting (art. 283-2 nonies), scrap and waste (283-2 sexies), emission quotas (283-2 septies), electronic communications services (283-2 octies), gas and electricity (283-2 quinquies). Flag these for the reviewer.

**Exempt and zero-rated.** Exports go to E1 with export evidence. Intra-EU supplies of goods go to F2: check the customer's VAT number on VIES before invoicing without VAT, keep transport proof, and file the état récapitulatif. Services to a business customer abroad go to E2. Exempt without credit (CGI art. 261: medical, education, insurance, finance, residential rent): no output VAT and no deduction on the related costs. A mixed business uses the coefficient de déduction (CGI annexe II, art. 206 to 214); refer it to an expert-comptable.

**Deduction restrictions.**

| Cost | Treatment | Source |
|---|---|---|
| Vehicles designed to carry people or for mixed use, their parts and upkeep | Not deductible. The test is how the vehicle was designed, judged at purchase or lease, not how it is used | https://bofip.impots.gouv.fr/bofip/1192-PGP.html |
| Exceptions to the vehicle exclusion | Vehicles bought for resale new; taxis, VTC and public passenger transport used exclusively for it; driving schools; hearses used exclusively by undertakers; vehicle hire businesses; vehicles with more than eight seats besides the driver carrying staff; horse transport vehicles from 2024; ski-domain all-terrain vehicles; aircraft for paid air services; racing sailboats. Each needs exclusive use | same |
| Fuel | Shares in the rates table. Electric charging is not on the fuel list: ordinary rules apply once the vehicle's own exclusion is settled | https://bofip.impots.gouv.fr/bofip/1194-PGP.html |
| Housing directors or staff free of charge | Not deductible, including buying or renting the premises; apportion by headcount where third parties are housed too | https://bofip.impots.gouv.fr/bofip/1190-PGP.html |
| Gifts and goods given away | Not deductible, except goods of very low value (amount fixed by CGI annexe IV, art. 28-00 A; not printed here, see Sources) | https://bofip.impots.gouv.fr/bofip/1196-PGP.html |
| Private use by owners, directors or staff | Not deductible | https://bofip.impots.gouv.fr/bofip/1194-PGP.html |
| Restaurant meals | Not excluded by name. Deductible only where incurred for the business, with the purpose and guests documented | CGI annexe II, art. 206 |
| Advertising for alcoholic drinks | Deductible under the ordinary rules from 21 February 2026 (CGI art. 273 septies E, LF 2026 art. 91) | https://bofip.impots.gouv.fr/bofip/15011-PGP.html |
| Fixed assets | Line 19, not line 20. Adjusted over five years (movable) or twenty years (immovable) if use changes. The EUR 500 small-equipment tolerance decides asset or expense | https://bofip.impots.gouv.fr/bofip/2109-PGP.html |

**Conservative defaults when facts are missing.** Unknown rate on a sale: 20%. Unknown VAT status of a purchase: not deductible. Unknown counterparty country: France. Unknown B2B or B2C status of an EU customer: consumer, charge French VAT. Unknown business-use share (car, phone, home office): no recovery. Unknown SaaS billing entity: line A3 self-assessment. Unknown whether a cost is blocked: blocked. Unknown whether in scope: in scope.

**Supplier and bank-line patterns (pre-classifier).** Match the counterparty name on the bank statement, most specific first; if nothing matches, apply the rules above.

| Pattern | Treatment |
|---|---|
| Bank fees and interest (BNP, Société Générale, Crédit Agricole, LCL, BPCE, Caisse d'Épargne, La Banque Postale, CIC, Crédit Mutuel; fee lines of Qonto, Revolut, Wise, N26); INTERETS, AGIOS; PRET, EMPRUNT | Exclude (exempt financial services or out of scope). Check for separate taxable subscription invoices from neobanks |
| DGFIP, TRESOR PUBLIC, IMPOTS.GOUV, URSSAF, CPAM, SSI, France Travail, CIPAV, CNAV, GREFFE, CFE, CVAE, PREFECTURE, INPI, CCI, CMA | Exclude: taxes, social charges, sovereign or registry fees |
| SALAIRE, PAIE, MUTUELLE (employee), DIVIDENDE, APPORT, VIREMENT INTERNE | Exclude: outside VAT |
| EDF, TotalEnergies, Orange, Free, SFR, Bouygues Telecom, OVHcloud | Domestic 20%, line 20. Gas (Engie) and water (Veolia, Suez): read the invoice for the rate |
| AXA, MAIF, MACIF, MATMUT, MAAF, Groupama, Generali, AG2R, Malakoff Humanis | Exclude: insurance is exempt |
| La Poste standard mail | Exclude (universal service). Colissimo, Chronopost, DHL Express France, Mondial Relay: 20%. UPS, TNT, FedEx: check whether billed from France or abroad (A3) |
| SNCF, Ouigo, RATP, taxis, G7, Bolt, Heetch, Uber rides, Air France domestic | 10%, line 20. International flights: exclude. Motorway tolls (Vinci, Sanef, APRR): 20% |
| Supermarkets (Carrefour, Auchan, Leclerc, Lidl, Monoprix, etc.) and restaurants | Default block unless a catering business or a documented business meal |
| Google, Microsoft, Adobe, Meta, LinkedIn, Spotify, Dropbox, Slack, Atlassian, Zoom (EU billing entities); Notion, OpenAI, Anthropic, Figma, Canva, Twilio, GitHub, HubSpot (non-EU or check); AWS EMEA SARL | A3 plus line 20 (self-assessment). If the invoice shows French TVA actually charged, treat as a domestic 20% purchase |
| Stripe, PayPal transaction fees | Exclude (exempt payment services). Stripe subscription: A3 plus 20. SumUp, Square, Zettle: by billing entity |
| Expert-comptable, avocat, notaire (business), commissaire aux comptes, architecte | Domestic 20%, line 20 |
| LOYER COMMERCIAL, SCI with TVA invoiced | 20% only where the landlord opted for VAT. Residential rent and TAXE FONCIERE: exclude |
| RETRAIT DAB, cash | Ask; default exclude as drawings |

Bank-statement reading: French exports are usually semicolon-separated with DD/MM/YYYY dates (Qonto and Revolut use ISO dates). VIR is a transfer, CB a card payment, PRLV a direct debit, CHQ a cheque, REM a cheque deposit, TIP an interbank payment. Refunds (remboursement, annulation, avoir) go as negatives on the original line; a customer credit note is a B5 correction, a non-taxed correction F8. Convert foreign currency at the transaction-date rate and keep the evidence. An IBAN prefix shows the bank's country, not the customer's VAT status: check VIES.

**Questions to raise when a line is ambiguous.** Fuel and vehicle costs (was the vehicle designed for people or goods, and which fuel?); restaurants (who was present and why?); SaaS (legal entity, country, any French TVA charged?); round transfers from the owner's name (sale, capital or loan?); incoming money from individuals or foreign accounts (sale? business or consumer? which country?); large one-off purchases near EUR 500 (asset or expense?); mixed-use phone or home costs (business share?); outgoing transfers to individuals (contractor with invoice, wages, refund or private?); foreign hotels (foreign VAT is not French input VAT; a refund may be claimed in that state); Airbnb income (furnished letting falls in the services band); construction subcontractors (domestic reverse charge?); platform sales on Amazon, Etsy or eBay (cross-border consumer sales above EUR 10,000 go through the OSS, refuse here under `eu-vat-directive` R-EU-5).

**Invoices.** Every mandatory particular applies at any amount; the EUR 150 rule only waives the seller's VAT number. Reverse-charge invoices say "Auto-liquidation". From 1 September 2026 (large companies and ETI) and 1 September 2027 (SMEs and micro-enterprises), invoices add four new particulars: the customer's SIREN, the delivery address if different, whether the invoice is for goods, services or both, and "Option pour le paiement de la taxe d'après les débits" where that option was made (service-public F31808).

**Working paper.** Follow `vat-workflow-base` Section 3. In the Transactions sheet the line-code column accepts only 2026 CA3 codes, blank for excluded lines, and "A3/20" style for self-assessed lines. The Line Summary sheet sums A1, E1, E2, E3, F2, A3, A4, B2, B4, then the rate block 08, 09, 9B, I1 to I6, line 16, memo 17, lines 19, 20, 22, 23, memo 24, then 25 or TD, 26, 27, 28 and 32. If line 23 exceeds line 16, line 25 is the credit and line 27 = 25 less 26 carries to the next return; otherwise TD = 16 less 23. Shade any row resting on a conservative default and recalculate the workbook before handing it over.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| CA3, régime réel normal | Monthly, between the 15th and the 24th of the following month. The exact day depends on the department (Paris, 92, 93 and 94 apart), the category of business and the SIREN or the first letter of the name, and is shown in the espace professionnel. Never state a single date | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 ; https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 |
| CA3, quarterly option | Where annual VAT due is below EUR 4,000 (CGI art. 287-2) | Légifrance art. 287 |
| CA12, régime simplifié | Annual, by the second working day after 1 May for a calendar year; within three months of the year end otherwise | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 |
| Régime simplifié instalments | July (55%) and December (40%); balance with the CA12. Off-calendar years: return filed January to May of N gives instalments July and December N; June to October gives December N and July N+1; November or December gives July and December N+1 | CGI art. 287-3 ; F23566 |
| Régime simplifié moved to monthly CA3 | VAT due for the previous year above EUR 15,000 (art. 287-3 bis); or the business makes intra-EU acquisitions, imports or exits from a suspensive regime (art. 287-3 ter, from 1 January 2025; quarterly if under EUR 4,000) | Légifrance art. 287 |
| Change of regime | Crossing the previous-year band or the EUR 15,000 limit: régime réel normal from 1 January of the following year (F23566). Crossing a current-year ceiling ends the régime simplifié during the year (CIBS L. 162-5); refer for the exact date and returns | F23566 ; CIBS L. 162-5 |
| Cessation or sale of the business | Final return within 30 days; 60 days under the régime simplifié (CGI art. 287-4) | Légifrance art. 287 |
| État récapitulatif des clients (intra-EU supplies of goods) and déclaration européenne de services (B2B services taxed in the customer's EU state) | Within ten working days after the month the VAT became due, filed with customs on pro.douane.gouv.fr (CGI art. 289 B) | CA3 notice 3310-NOT-CA3-SD, 2026 |
| Payment | With the return, online from the espace professionnel on impots.gouv.fr | F23566 |
| E-invoicing: receiving | From 1 September 2026 every business established in France must be able to receive e-invoices through an approved platform (plateforme agréée) | CGI art. 289 bis ; LFR 2022 art. 26, III, as rewritten by LF 2024 art. 91 ; impots.gouv.fr FAQ |
| E-invoicing and e-reporting: issuing | From 1 September 2026 for large companies, ETI and VAT groups; from 1 September 2027 for SMEs and micro-enterprises (size under LME art. 51 and decree 2008-1354, art. 3) | same ; BOFiP BOI-TVA-DECLA-20-30-50 (30 September 2026) |

Formats, platforms, e-reporting frequencies and the payment-data rules are in `france-einvoice`.

## Penalties and interest

| Failure | Charge | Source |
|---|---|---|
| Late payment of tax | Interest of 0.20% a month, from the first day of the month after the due month to the last day of the month of payment (CGI art. 1727, III and IV) | Légifrance art. 1727 |
| Late return, no formal notice, or filed within 30 days of a notice | 10% of the tax due on the return (CGI art. 1728, 1, a) | Légifrance art. 1728 |
| Return still missing 30 days after a formal notice | 40% (art. 1728, 1, b) | same |
| Hidden activity discovered | 80% (art. 1728, 1, c) | same |
| Errors or omissions: deliberate failure / abuse of law or fraudulent schemes | 40% / 80% (CGI art. 1729) | Légifrance art. 1729 |
| Late payment where art. 1728 does not apply | 5% surcharge (CGI art. 1731) | Légifrance art. 1731 |
| Self-assessed tax that would have been deductible but was left off the return | Fine of 5% of the deductible amount (CGI art. 1788 A, 4) | Légifrance art. 1788 A |
| État récapitulatif filed late | EUR 750; EUR 1,500 if still missing 30 days after notice; EUR 15 per error, capped at EUR 1,500 (art. 1788 A, 1 and 2) | same |
| Invoice errors or omissions | EUR 15 per error, capped at a quarter of the invoice amount (CGI art. 1737, II) | Légifrance art. 1737 |
| Invoice not issued electronically when required | EUR 50 per invoice, capped at EUR 15,000 a year (art. 1737, III, as amended by LF 2026) | same |
| No approved platform for receiving e-invoices | Formal notice to comply within three months; then EUR 500; then EUR 1,000 after a second three-month notice, and EUR 1,000 again for each further three months the failure persists (CGI art. 1737, IV bis) | Légifrance art. 1737 |
| E-reporting not transmitted | EUR 500 per transmission, capped at EUR 15,000 a year (CGI art. 1788 D, I and II, as amended by LF 2026) | Légifrance art. 1788 D |
| First-offence relief | The invoice fines in art. 1737, II and III do not apply to a first offence in the current year and the three previous years when it is put right spontaneously or within 30 days of the administration's first request (art. 1737, V) | Légifrance art. 1737 |

Example of the interest rule: a CA3 for March 2026 showing EUR 4,000 due, filed and paid in June without any notice, bears the 10% majoration (EUR 400) and interest for May and June, 2 × 0.20% × 4,000 = EUR 16. Audit procedure, the reductions for voluntary correction and the taxpayer's rights are in `fr-tax-audit`.

## Cross-border points

- **B2B services sold to EU customers:** place of supply is the customer's state (CGI art. 259-1°). Invoice without French VAT, mark "Auto-liquidation", put the amount on E2, check the customer's number on VIES, and file the déclaration européenne de services.
- **Goods sold to EU businesses:** zero-rated on F2 with VIES check and transport proof; état récapitulatif within ten working days after the month.
- **Distance sales and B2C digital services to other EU states:** French VAT while the EU-wide total stays at or below EUR 10,000 a year; above it, or on option, the destination state's VAT applies and the OSS is used. That is outside this skill (`eu-vat-directive`, R-EU-5); such sales sit on E3.
- **Purchases from abroad:** self-assess as set out in The taxable base (A3, B2, A4, B4).
- **Non-established businesses selling in France:** where a French taxable customer buys, the customer is liable under art. 283-1 and 283-2 in the cases those articles name. A non-EU business that must register may need a fiscal representative: refer.
- **The EU franchise:** an EU business with EU-wide turnover up to EUR 100,000 can use the French franchise after notifying its own state (art. 293 B bis); a French business crossing EUR 100,000 of EU-wide turnover while using another state's franchise must tell the French administration within 15 working days (art. 293 B ter).
- **Monaco:** tax on operations to Monaco is shown at memo line 18 of the CA3.
- Income tax on cross-border activity is in `fr-cross-border` and `fr-corporate-tax`.

## Worked examples

**Example 1: monthly CA3 for a Paris consultancy (régime réel normal).** In April 2026 the company sells EUR 50,000 of consulting at 20%, and its in-house café sells EUR 8,000 of food and soft drinks for consumption on the premises at 10% (CGI art. 279, m; alcoholic drinks would be 20%). It buys Google Ads from Google Ireland for EUR 850 (no VAT on the invoice), other French purchases of EUR 12,000 plus 20% VAT, and a server for EUR 1,500 plus 20% VAT that it records as a fixed asset. Sales: A1 is 58,000; line 08 base 50,000 and tax 10,000; line 9B base 8,000 and tax 800. Google Ads: A3 is 850, tax 170 joins line 08, and the same 170 is deducted at line 20. Deductions: line 20 is 2,400 plus 170, line 19 is 300. Line 16 is 10,970, line 23 is 2,870, so TD and line 28 are 8,100.

```oa-check
name: France CA3 April 2026, consultancy and café with an EU service self-assessed
inputs:
  sales_20: 50000
  sales_10: 8000
  eu_service_a3: 850
  domestic_purchases_net: 12000
  fixed_asset_net: 1500
steps:
  - tax_08: sales_20 * 0.20 + eu_service_a3 * 0.20
  - tax_9b: sales_10 * 0.10
  - line_16: tax_08 + tax_9b
  - line_19: fixed_asset_net * 0.20
  - line_20: domestic_purchases_net * 0.20 + eu_service_a3 * 0.20
  - line_23: line_19 + line_20
  - vat_due: line_16 - line_23
expected:
  line_16: 10970.00
  line_23: 2870.00
  vat_due: 8100.00
```

**Example 2: régime simplifié, instalments and the fixed-asset edge.** A shop on the régime simplifié had tax of EUR 9,000 for 2025 before the VAT on fixed assets. Its 2026 instalments are 55% in July (4,950) and 40% in December (3,600). On the 2026 CA12 its gross VAT is EUR 18,000, deductions on other goods and services EUR 6,500, and VAT on fixed assets EUR 1,200. Net VAT for 2026 is 10,300, so the balance due with the CA12 by the second working day after 1 May 2027 is 10,300 less 8,550, or 1,750. The edge: next year's instalment base (line 57) is struck before the fixed-asset VAT, so it is 18,000 less 6,500, or 11,500, not 10,300. The 2027 instalments are 6,325 in July and 4,600 in December.

```oa-check
name: France CA12 2026, instalments, balance and next year's base
inputs:
  prior_year_base: 9000
  gross_vat: 18000
  deduction_other: 6500
  deduction_fixed_assets: 1200
steps:
  - july_2026: prior_year_base * 0.55
  - december_2026: prior_year_base * 0.40
  - net_vat_2026: gross_vat - deduction_other - deduction_fixed_assets
  - balance_may_2027: net_vat_2026 - july_2026 - december_2026
  - base_2027: gross_vat - deduction_other
  - july_2027: base_2027 * 0.55
  - december_2027: base_2027 * 0.40
expected:
  july_2026: 4950.00
  december_2026: 3600.00
  balance_may_2027: 1750.00
  july_2027: 6325.00
  december_2027: 4600.00
```

## Ask the client first

- Which regime are you in, and what were last year's turnover (by activity: goods and catering, or services) and last year's VAT due? Both numbers decide the regime.
- What filing date does your espace professionnel show for the CA3? It depends on department, category and SIREN.
- Do you sell outside France? For each customer: business or consumer, goods or services, which country. That decides E1, E2, E3, F2 and the EU statements.
- Do you buy goods from other EU states or import? Under the régime simplifié that alone forces monthly CA3 returns from 2025.
- Any credit at line 27 of your last return, any exempt income, any construction subcontracting, any company cars (designed to carry people or goods)?
- Refuse or refer: a business inside the franchise that has not opted; partial exemption above de minimis; margin scheme; property VAT; VAT groups; fiscal representatives; overseas departments; anyone wanting income tax (use `fr-income-tax` or `fr-personal-income-tax`); any refusal in `eu-vat-directive` R-EU-1 to R-EU-12.

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI art. 293 B, 293 B bis, 293 B ter (franchise; LF 2025 art. 32 and loi n° 2025-1044 art. 1) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162567/2026-10-24 | 2026-10-24 |
| CGI art. 287 (returns, instalments, monthly triggers) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191928/2026-10-24 | 2026-10-24 |
| CIBS art. L. 162-4 to L. 162-8 (régime simplifié conditions; L. 162-4 indexation rule) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000044598127/2026-10-24 | 2026-10-24 |
| CIBS art. A. 162-7 (régime simplifié amounts for 2026, arrêté of 27 January 2026) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000049803748/2026-10-24 | 2026-10-24 |
| BOFiP BOI-BAREME-000036-20260701 (régime simplifié limits for 2026) | https://bofip.impots.gouv.fr/bofip/9368-PGP.html/identifiant=BOI-BAREME-000036-20260701 | 2026-10-24 |
| CGI art. 278 (20%) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191854/2026-10-24 | 2026-10-24 |
| CGI art. 278-0 bis (5.5%) and 279 (10%) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191654/2026-10-24 | 2026-10-24 |
| CGI art. 281 quater and 281 octies (2.1%) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191656/2026-10-24 | 2026-10-24 |
| CGI art. 298 septies (press, 2.1% and 1.05%) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179663/2026-10-24 | 2026-10-24 |
| CGI art. 289 B (état récapitulatif) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191662/2026-10-24 | 2026-10-24 |
| CGI art. 289 bis (e-invoicing, amended by LF 2026 art. 123) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006191855/2026-10-24 | 2026-10-24 |
| Loi n° 2023-1322 (LF 2024), art. 91, rewriting LFR 2022 art. 26, III (e-invoicing dates) | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048727345 | 2026-10-24 |
| CGI art. 1727 (late interest) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006147309/2026-10-24 | 2026-10-24 |
| CGI art. 1728 (late filing, amended by LF 2026 art. 126) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179995/2026-10-24 | 2026-10-24 |
| CGI art. 1729 (inaccuracies) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006179987/2026-10-24 | 2026-10-24 |
| CGI art. 1731 (5% late payment) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006163002/2026-10-24 | 2026-10-24 |
| CGI art. 1737 (invoice fines) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006163056/2026-10-24 | 2026-10-24 |
| CGI art. 1788 A and 1788 D (statements, self-assessment, e-reporting fines) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000006162921/2026-10-24 | 2026-10-24 |
| BOFiP actualité 7 October 2026: CIBS recodification moved to 1 January 2027; LF 2026 VAT measures | https://bofip.impots.gouv.fr/bofip/15140-PGP.html | 2026-10-24 |
| BOFiP actualité 17 June 2026: alcohol advertising deduction (LF 2026 art. 91) | https://bofip.impots.gouv.fr/bofip/15011-PGP.html | 2026-10-24 |
| BOFiP BOI-TVA-DECLA-20-30-50 (e-reporting dates) | https://bofip.impots.gouv.fr/bofip/13897-PGP.html | 2026-10-24 |
| BOFiP: vehicles; fuel; accommodation; gifts; small equipment | https://bofip.impots.gouv.fr/bofip/1192-PGP.html ; https://bofip.impots.gouv.fr/bofip/1194-PGP.html ; https://bofip.impots.gouv.fr/bofip/1190-PGP.html ; https://bofip.impots.gouv.fr/bofip/1196-PGP.html ; https://bofip.impots.gouv.fr/bofip/2109-PGP.html | 2026-10-24 |
| Service-public: franchise en base (checked 1 January 2026) | https://entreprendre.service-public.gouv.fr/vosdroits/F21746 | 2026-10-24 |
| Service-public: déclarer et payer la TVA (checked 21 February 2026) | https://entreprendre.service-public.gouv.fr/vosdroits/F23566 | 2026-10-24 |
| Service-public: invoice particulars (checked 11 August 2026) | https://entreprendre.service-public.gouv.fr/vosdroits/F31808 | 2026-10-24 |
| CA3 form 3310-CA3-SD 2026 (impots.gouv.fr in maintenance; Internet Archive copy of 10 May 2026) | https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf | 2026-10-24 |
| CA3 notice 3310-NOT-CA3-SD 2026 (Internet Archive copy of 16 October 2026) | https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf | 2026-10-24 |
| CA12 form 3517-S-SD 2026 (Internet Archive copy of 12 January 2026) | https://www.impots.gouv.fr/sites/default/files/formulaires/3517-s-sd/2026/3517-s-sd_5291.pdf | 2026-10-24 |
| impots.gouv.fr: CA3 filing dates (Internet Archive copy of 29 September 2026) | https://www.impots.gouv.fr/le-regime-reel-normal-dates-limites-de-transmission-des-ca3 | 2026-10-24 |
| impots.gouv.fr: e-invoicing start dates, modified 16 January 2026 (Internet Archive copy of 25 June 2026) | https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation | 2026-10-24 |
| impots.gouv.fr: overseas department rates (Internet Archive copy of 18 May 2026) | https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom | 2026-10-24 |
| impots.gouv.fr: VAT regimes, modified 21 May 2026, still showing 2023-2025 limits (Internet Archive copy of 29 September 2026) | https://www.impots.gouv.fr/professionnel/les-regimes-dimposition-la-tva | 2026-10-24 |

Not yet confirmed: the amount of the very-low-value gift exception (CGI annexe IV, art. 28-00 A, not re-read); the CA12 completion notice 3517-S-NOT-SD 2026 (no copy reachable; CA12 lines taken from the form and the earlier read of the notice); the reference date for measuring a business's size for the e-invoicing timetable (LFR 2022 art. 26, III and its decree, not re-read); the consolidated text of LFR 2022 art. 26, III after LF 2025 and LF 2026 (the dates were checked against the LF 2024 text, BOFiP of 30 September 2026 and service-public F31808); the exact date a business leaves the régime simplifié after crossing a current-year ceiling under CIBS L. 162-5 and its implementing decree; the full lists of goods and services under the 10% and 5.5% rates after LF 2026 (only the article headings and the BOFiP summary were read); Corsican rate rules beyond the CA3 lines; the restaurant-meal treatment rests on CGI annexe II art. 206, not re-read today.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `france-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/france-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
