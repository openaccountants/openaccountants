---
name: italy-vat-return
description: "Italian periodic VAT (IVA) for tax year 2026 under the regime ordinario: the 22%, 10%, 5% and 4% rates and what Tabella A puts in each, monthly settlement by the 16th, the quarterly option (EUR 500,000 services and professions, EUR 800,000 other activities) with 1% interest, the LIPE quarterly communication and its VP rows, the annual return window to 30 April, reverse charge (art. 17), split payment for public bodies (extended to 30 June 2029), SdI e-invoicing (forfettari included since 2024) and the esterometro, blocked input VAT, and the penalties after D.Lgs. 87/2024 (25% late payment, ravvedimento, legal interest 1.60%). Trigger on: LIPE, liquidazione IVA, IVA trimestrale, versamento IVA F24, inversione contabile, scissione dei pagamenti, esterometro, ravvedimento IVA. Out of scope: the annual return and December acconto in depth (it-dichiarazione-iva-annuale), invoicing rules (italy-einvoice), the flat-rate regime (it-regime-forfettario), income tax (it-income-tax, it-ires-corporate-tax), payroll (italy-payroll)."
version: 2.1
jurisdiction: IT
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - vat-workflow-base
  - eu-vat-directive
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italian VAT return: periodic settlement, LIPE and payment (regime ordinario), tax year 2026 v2.1

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Italy.

**What this skill does.** It takes an Italian business under the regime ordinario from its invoices and bank lines to a settled VAT period: which rate applies, which VP row each amount goes in, when the tax is paid by F24, when the LIPE is sent, and what a late or wrong payment costs. Figures come from D.P.R. 633/1972 (the VAT decree) and its Tabella A, D.P.R. 100/1998, D.P.R. 542/1999, D.L. 78/2010, D.Lgs. 127/2015, and the penalty decrees D.Lgs. 471/1997 and 472/1997 as reformed by D.Lgs. 87/2024, all read on Normattiva on 24 October 2026, plus Agenzia delle Entrate pages.

**The law moves on 1 January 2027.** The Testo unico IVA (D.Lgs. 10/2026) replaces D.P.R. 633/1972 from 1 January 2027, and new codes for payments and penalties apply from the same date. This skill covers periods up to December 2026; see the pack README.

**Sibling skills.** [it-dichiarazione-iva-annuale](it-dichiarazione-iva-annuale.md) (annual return, December acconto, credits, refunds, pro rata and rettifica). [italy-einvoice](italy-einvoice.md) (SdI, TD document types, invoice penalties). [it-regime-forfettario](it-regime-forfettario.md) (flat-rate regime). [it-income-tax](it-income-tax.md) and [it-irpef-employees](it-irpef-employees.md) (IRPEF), [it-ires-corporate-tax](it-ires-corporate-tax.md) (IRES), [italy-payroll](italy-payroll.md) (payroll), [it-cross-border](it-cross-border.md), [italy-bookkeeping](italy-bookkeeping.md). Load `vat-workflow-base` and `eu-vat-directive` alongside.

## Who this applies to

- **In scope.** Sole traders, professionals and companies with a Partita IVA under the regime ordinario that make taxable supplies in Italy (D.P.R. 633/1972 art. 1). They settle VAT monthly by default (D.P.R. 100/1998 art. 1) or quarterly by option (D.P.R. 542/1999 art. 7), and send the LIPE every quarter (D.L. 78/2010 art. 21-bis).
- **Forfettari: no VAT charged, but e-invoicing applies.** Individuals in the regime forfettario (prior-year revenue or fees, annualised, up to EUR 85,000; the regime ends in the same year once revenue passes EUR 100,000) charge no VAT on domestic sales and are exempt from paying VAT and from most VAT duties (L. 190/2014 art. 1 commi 54, 58, 59, 71). They still pay VAT on reverse-charge purchases, including intra-EU ones, by the 16th of the second month after each calendar quarter, with no deduction (comma 58(e-bis), text in force on 24 October 2026). They do not file a LIPE (D.L. 78/2010 art. 21-bis(3)). Use [it-regime-forfettario](it-regime-forfettario.md).
- **Not in this skill (refer).** Regime dei minimi; pro rata for mixed taxable and exempt activity (art. 19(5), see the annual skill); margin scheme for second-hand goods, art and collectables (D.L. 41/1995 art. 36); VAT groups (arts. 70-bis to 70-duodecies); a non-resident acting through a fiscal representative; agriculture special regime (art. 34); EU B2C sales above the EUR 10,000 threshold (OSS, see `eu-vat-directive`); income tax questions.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 22% | 2026 | D.P.R. 633/1972 art. 16(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art16!vig=2026-10-24 |
| Reduced rates | 4% (Tabella A Part II), 5% (Part II-bis), 10% (Part III) | 2026 | D.P.R. 633/1972 art. 16(2), same URL |
| 4%: what falls in it | Fresh milk; butter and cheese; vegetables, fruit, pulses; bread, pasta, crackers; olive oil; newspapers, books and periodicals; a first home bought under the registry-tax "prima casa" conditions (not cadastral A1, A8, A9); orthopaedic and prosthetic aids, wheelchairs; canteen meals in workplaces and schools | 2026 | Tabella A Part II nn. 3-8, 13, 15, 18, 21, 30-31, 37, 41-quater, https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633:1~allA!vig=2026-10-24 |
| 5%: what falls in it | Social-cooperative health, education and care services to listed groups; fresh basil, rosemary, sage, oregano; urban passenger transport by water; fresh truffles; winter-sport and mountaineering courses; live horses not for food sold up to the end of the year after birth; works of art, antiques and collectables (when the margin scheme is not used) | 2026 | Tabella A Part II-bis nn. 1, 1-bis, 1-ter, 1-quater, 1-septies, 1-octies, 1-novies, same URL |
| 10%: what falls in it (main items) | Domestic electricity, and electricity and gas for manufacturing, farming and extraction businesses; medicines; hotel and other accommodation; food and drink served (restaurants, bars, vending machines); passenger transport (except Part II-bis and exempt transport); non-luxury new homes sold by builders outside the prima casa conditions | 2026 | Tabella A Part III nn. 103, 114, 120, 121, 127-novies, 127-undecies, same URL |
| Monthly settlement and payment | VAT due for the month paid by the 16th of the next month; December by 16 January | 2026 | D.P.R. 100/1998 art. 1(1) and (4), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-03-23;100~art1!vig=2026-10-24 |
| Small debt carried forward | A period's VAT up to EUR 100 is paid with the next period (monthly: by 16 December at the latest; quarterly: by 16 November) | 2026 | D.P.R. 100/1998 art. 1(4); D.P.R. 542/1999 art. 7(1)(a) |
| Quarterly option: limits | Prior calendar year volume d'affari up to EUR 500,000 (services and professions) or EUR 800,000 (other activities) | 2026 | D.P.R. 542/1999 art. 7(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art7!vig=2026-10-24; limits tied to the simplified-accounts limits by L. 183/2011 art. 14(11), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2011-11-12;183~art14!vig=2026-10-24, set in D.P.R. 600/1973 art. 18(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art18!vig=2026-10-24 |
| Quarterly payment dates | Q1 to Q3 by the 16th of the second month after the quarter (16 May, 16 August, 16 November); Q4 with the annual balance by 16 March | 2026 | D.P.R. 542/1999 art. 7(1)(a) and (b); Agenzia, "Come pagare l'Iva", https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva |
| Quarterly interest | 1% added to each quarterly payment | 2026 | D.P.R. 542/1999 art. 7(3) |
| August payments | Payments due 1 to 20 August may be made by 20 August with no surcharge | 2026 | D.L. 223/2006 art. 37(11-bis), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2006-07-04;223~art37!vig=2026-10-24 |
| Weekend or holiday | A payment or filing due on a Saturday or holiday is on time on the next working day | 2026 | D.L. 70/2011 art. 7(2)(l), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-05-13;70~art7!vig=2026-10-24 |
| LIPE deadlines | Last day of the second month after the quarter (31 May, 30 November); Q2 by 30 September; Q4 by end of February, or inside the annual return filed by end of February | 2026 | D.L. 78/2010 art. 21-bis(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art21bis!vig=2026-10-24 |
| Annual VAT return | Filed 1 February to 30 April of the next year | VAT year 2026, filed 2027 | D.P.R. 322/1998 art. 8(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art8!vig=2026-10-24 |
| Car and motor-vehicle VAT | 40% deductible when not used only for the business | 2026 | D.P.R. 633/1972 art. 19-bis.1(1)(c), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art19bis.1!vig=2026-10-24 |
| Entertainment gifts | VAT deductible only on goods costing up to EUR 50 each | 2026 | D.P.R. 633/1972 art. 19-bis.1(1)(h), same URL |
| EU distance sales and B2C e-services | Italian VAT stays on them while the yearly total stays at or below EUR 10,000 | 2026 | D.L. 331/1993 art. 41(1)(b), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art41!vig=2026-10-24 |
| Esterometro exemption | Purchases of non-Italian-situs goods and services up to EUR 5,000 per operation are not reported | 2026 | D.Lgs. 127/2015 art. 1(3-bis), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig=2026-10-24 |
| Late payment penalty | 25% of the unpaid tax; 12.5% if paid within 90 days; within 15 days, one fifteenth of 12.5% per day late | Violations from 1 September 2024 | D.Lgs. 471/1997 art. 13(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-24 |
| Legal interest rate (ravvedimento) | 1.60% a year, from 1 January 2026 | 2026 | D.M. 10 December 2025, GU n. 289 of 13 December 2025, https://www.gazzettaufficiale.it/eli/id/2025/12/13/25A06705/sg |
| Income tax limit for small assets (pointer) | Unit cost up to EUR 516.46 (business income) or EUR 516.40 (professionals) expensed in the year | 2026 | TUIR art. 102(5), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art102!vig=2026-10-24; TUIR art. 54-quinquies(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=2026-10-24 |

## The taxable base

**The periodic settlement.** For each month (or quarter) the business takes the VAT that became chargeable on its sales and subtracts the VAT on purchases it deducts in that period (D.P.R. 100/1998 art. 1(1)). VAT on purchase invoices received and recorded by the 15th of the next month can be deducted in the month of the operation, except for invoices for the previous year (same article). Quarterly filers may record sales invoices by the end of the month after the quarter (D.P.R. 542/1999 art. 7(3-bis)).

**The LIPE rows (quadro VP).** As defined in the Agenzia's LIPE instructions (2024 edition, the current one on its model page):

| Row | What goes in |
|---|---|
| VP1 | Month or quarter (quarterly filers enter 5 for the fourth quarter) |
| VP2 | Sales net of VAT: taxable, non-taxable, exempt, and out-of-scope sales under arts. 7 to 7-septies that need an invoice; also sales where the buyer owes the VAT |
| VP3 | Purchases net of VAT: domestic, intra-EU and imports, including non-deductible ones |
| VP4 | Output VAT, including reverse-charge VAT the business owes as buyer |
| VP5 | Input VAT deducted, including reverse-charge VAT when deductible |
| VP6 | VP4 minus VP5: column 1 due, column 2 credit |
| VP7 | Previous period's debt not paid because not above EUR 100 |
| VP8 | Credit from the previous period of the same year |
| VP9 | Credit from last year's annual return used in this period |
| VP10 | F24 payments for first domestic sales of EU cars |
| VP11 | Special tax credits used against the payment |
| VP12 | Quarterly filers' 1% interest; not filled for Q4 |
| VP13 | December acconto, with method code; not paid if under EUR 103.29 |
| VP14 | VAT to pay (col. 1) or credit (col. 2): (VP6 col. 1 + VP7 + VP12) minus (VP6 col. 2 + VP8 + VP9 + VP10 + VP11 + VP13); not filled by quarterly filers for Q4 |

**Which kind of supply.** Taxable at a rate from the table above. Non-taxable with right to deduct (non imponibile): exports (art. 8, nature code N3.1) and intra-EU B2B supplies of goods (D.L. 331/1993 art. 41, N3.2, check VIES). Out of scope (non soggette): B2B services to a business established elsewhere, since the general rule taxes B2B services where the customer is established (art. 7-ter(1)(a), N2.1); the invoice is still issued, marked "inversione contabile", by the 15th of the next month for EU customers (art. 21(4)(c) and (6-bis)). Exempt without deduction (art. 10): medical, education, insurance, financial services, residential letting, universal postal service. All three kinds go in VP2.

**Reverse charge (inversione contabile, art. 17).**
- *From foreign suppliers (art. 17(2)).* Goods and services supplied in Italy by non-residents to Italian businesses: the buyer owes the VAT. EU service invoices are integrated (TD17), EU goods (TD18); non-EU services need a self-invoice (TD17). Net to VP3, VAT to VP4 and, if deductible, VP5.
- *Domestic (art. 17(5) and (6)).* The Italian buyer owes the VAT on: construction subcontracting to builders (6)(a); cleaning, demolition, installation and completion services on buildings (6)(a-ter); sales of buildings where the seller opts to tax (6)(a-bis); mobile phones (6)(b); game consoles, tablets, laptops and chips before installation (6)(c); emission allowances and gas and electricity certificates (6)(d-bis), (d-ter); gas and electricity sold to a reseller (6)(d-quater); gold material and semi-finished gold of 325 thousandths or more, and investment gold taxed by option (art. 17(5)); scrap metals, waste paper, rags, glass, plastic and recovered pallets (art. 74(7) and (8)). Document type TD16. Letter (6)(a-quinquies) for logistics and goods-handling services only takes effect once the EU Council authorises it (L. 207/2024 art. 1(58)).

**Split payment (scissione dei pagamenti, art. 17-ter).** On sales to public administrations, public economic bodies, foundations at least 70% publicly funded, and companies controlled by or at least 70% owned by public bodies, the supplier invoices the VAT but the buyer pays it straight to the Treasury. Listed (FTSE MIB) companies left the scheme on 1 July 2025 (D.L. 84/2025 art. 10). It does not apply to services whose fees bear income tax withholding, such as professionals' fees (art. 17-ter(1-sexies)). The rule applies until the EU authorisation ends (art. 17-ter(1-ter)); Council Implementing Decision (EU) 2026/1728 extended that authorisation to 30 June 2029, with effect from 1 July 2026. The supplier ends up with VAT credits; refunds of those credits are dealt with first (Decision recital 7, and see the annual skill).

**Blocked or limited input VAT (art. 19-bis.1).**

| Cost | Treatment |
|---|---|
| Road motor vehicles not used only for the business (lett. c) | 40% of the VAT. Full deduction if the vehicle is the business's own activity (taxi, rental, driving school) or for commercial agents |
| Fuel, repairs, tolls for those vehicles (lett. d) | Same share as the vehicle; fuel paid by traceable means |
| Passenger transport (lett. e) | Not deductible unless transport is the business's own activity |
| Food and drink (lett. f) | Not deductible unless the business's own activity or canteen supply. A business-trip meal or hotel with an invoice is deductible |
| Entertainment, spese di rappresentanza (lett. h) | Not deductible, except goods costing up to EUR 50 each |
| Residential buildings (lett. i) | Purchase, rent and upkeep not deductible, except for builders of such buildings |
| Phone and internet | No fixed share (lett. g repealed by L. 244/2007): deduct the business share only (art. 19) |

**Capital goods.** Input VAT is deducted in VP5 like any purchase; there is no LIPE row for them. Later changes of use are adjusted under art. 19-bis2 (annual skill). For income tax the small-asset limits in the rates table decide whether to expense or depreciate.

**Classifying bank lines (OpenAccountants' own working list, not an official source).** Shorthand: domestic purchase = VP3 + VP5; reverse charge = VP3 + VP4 (+ VP5 if deductible); sale = VP2 + VP4. "Exclude" means no VAT line; an exempt purchase with an invoice still counts in VP3.

| Counterparty pattern | Default treatment |
|---|---|
| Bank fees, interest, loans (UniCredit, Intesa Sanpaolo, BPM, MPS, BPER, Poste/BancoPosta, Credem; Revolut, Wise, N26 fee lines) | Exclude: exempt financial services (art. 10(1) n. 1) |
| Agenzia Entrate, F24, Agenzia Riscossione, INPS, INAIL, Camera di Commercio, Comune, Regione | Exclude: taxes, contributions, public fees |
| Dogana / customs | Exclude the payment line; the customs bill (bolletta doganale) value goes to VP3 and its deductible VAT to VP5 |
| Utilities (Enel, Eni Plenitude, Edison, A2A, Iren, Hera, Acea) | Domestic purchase at the rate on the invoice (may be 10%) |
| Telecoms (TIM, Vodafone, WindTre, Fastweb, Iliad) | Domestic 22%, business share only |
| Insurance (Generali, Allianz, UnipolSai, AXA, Zurich) | Exclude: exempt (art. 10(1) n. 2) |
| Poste Italiane standard mail | Exclude: exempt universal service. Couriers (SDA, BRT, DHL, GLS, TNT): domestic 22% |
| Trains, buses, taxis, Uber, domestic flights | Net to VP3, VAT blocked (lett. e); international flights excluded |
| Autostrade, Telepass | Same share as the vehicle |
| Supermarkets, restaurants, bars | Blocked by default; ask whether it was a business-trip meal with an invoice |
| Google, Microsoft, Adobe, Meta, LinkedIn, Dropbox, Slack, Zoom (Irish entities); Spotify (SE); Atlassian (NL); AWS EMEA (LU); Stripe subscriptions (IE) | EU reverse charge, TD17. If the invoice shows Italian VAT, treat as domestic |
| Notion, Anthropic, OpenAI, Figma, Twilio (US); Canva (AU); GitHub, HubSpot (check entity) | Non-EU reverse charge, self-invoice TD17 |
| Stripe and PayPal transaction fees | Exclude: exempt financial services. SumUp, Nexi, Satispay: check the invoice |
| Commercialista, avvocato, notaio, consulente del lavoro, architetto | Domestic 22% |
| Wages, TFR, professional pension funds (ENPAM, CNPADC) | Exclude |
| Commercial rent with VAT | Domestic 22%. Residential rent, IMU: exclude |
| Own transfers (giroconto), dividends, owner money, loan repayments | Exclude |
| Cash withdrawals | Exclude; ask what the cash paid for |

**Conservative defaults when facts are missing.** Unknown sale rate: 22%. Unknown purchase status: not deductible. Unknown counterparty country: Italy. Unknown EU customer status: B2C with Italian VAT. Unknown business-use share: no recovery. Unknown SaaS billing entity: non-EU reverse charge. Unknown entertainment or personal use: blocked. Unknown scope: in scope.

**Working paper.** Use the `vat-workflow-base` workbook with VP codes in the field column, a summary sheet that sums VP2 to VP5 and applies the VP14 formula above, and a recalculation step before handing it over. Large or unusual items are flagged by the firm's own limits; no official page sets them.

## Deadlines and filing

- **Registration and invoices.** A Partita IVA is opened before starting. Invoices between Italian parties are electronic through the SdI only, including those of forfettari and minimi since 1 January 2024 (from 1 July 2022 if their prior-year revenue exceeded EUR 25,000) (D.Lgs. 127/2015 art. 1(3); D.L. 36/2022 art. 18(2) and (3), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2022-04-30;36~art18!vig=2026-10-24). An invoice is issued within 12 days of the operation; a deferred invoice for the month's deliveries by the 15th of the next month (art. 21(4)). Details in [italy-einvoice](italy-einvoice.md).
- **Esterometro.** Sales to and purchases from parties not established in Italy are reported to the SdI in XML: sales within the invoice deadlines, purchases by the 15th of the month after receiving the document or making the operation. Not reported: operations with a customs bill, ones already invoiced through the SdI, and purchases up to EUR 5,000 each that are not Italian-situs (D.Lgs. 127/2015 art. 1(3-bis)).
- **Monthly filers.** Settle and pay by F24 online by the 16th of the next month (D.P.R. 100/1998 art. 1). Payments due 1 to 20 August may be made by 20 August.
- **Quarterly filers.** Settle and pay with 1% interest by 16 May, 16 August (by 20 August under the August rule), 16 November; Q4 goes into the annual return and is paid by 16 March 2027 (D.P.R. 542/1999 art. 7).
- **LIPE.** Sent online for every quarter, also when the period ends in credit: Q1 2026 by 1 June 2026 (31 May was a Sunday), Q2 by 30 September 2026, Q3 by 30 November 2026, Q4 by 1 March 2027 or inside an annual return filed by then (D.L. 78/2010 art. 21-bis). Monthly filers send one LIPE per quarter with one module per month (LIPE instructions). Errors are corrected with a replacement LIPE before the annual return, or in the annual return.
- **December acconto.** Due 27 December (28 December 2026, as the 27th is a Sunday); computation in [it-dichiarazione-iva-annuale](it-dichiarazione-iva-annuale.md).
- **Annual return.** 1 February to 30 April 2027 for VAT year 2026 (D.P.R. 322/1998 art. 8(1)).
- **Registers.** Sales invoices (art. 23), purchases (art. 25), and daily receipts for retail (art. 24).

## Penalties and interest

The penalty figures below apply to violations from 1 September 2024 (D.Lgs. 87/2024 art. 5(1)).

| Violation | Penalty | Source |
|---|---|---|
| VAT paid late or short (monthly, quarterly, acconto, balance) | 25% of the unpaid amount; 12.5% if paid within 90 days; within 15 days, 12.5% divided by 15 for each day late | D.Lgs. 471/1997 art. 13(1) |
| Credit offset that was not due (non spettante) | 25% of the credit used | D.Lgs. 471/1997 art. 13(4-bis) |
| LIPE omitted, incomplete or wrong | EUR 500 to 2,000; halved if sent or corrected within 15 days of the deadline | D.Lgs. 471/1997 art. 11(2-ter), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig=2026-10-24 |
| Esterometro data omitted or wrong | EUR 2 per invoice, at most EUR 1,000 per quarter; halved (max EUR 500) if sent or corrected within 15 days | D.Lgs. 471/1997 art. 11(2-quater) |
| Taxable sale not invoiced or recorded, or VAT understated | 70% of the VAT; EUR 250 to 2,000 when the tax settlement was not affected | D.Lgs. 471/1997 art. 6(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art6!vig=2026-10-24 |
| Non-taxable, exempt or reverse-charge sale not invoiced or recorded | 5% of the amount; EUR 250 to 2,000 if it does not affect income either | D.Lgs. 471/1997 art. 6(2) |
| VAT deducted that was not deductible | 70% of the deduction | D.Lgs. 471/1997 art. 6(6) |
| Buyer receives no invoice or an irregular one and does not report it within 90 days | 70% of the VAT, minimum EUR 250 | D.Lgs. 471/1997 art. 6(8) |
| Buyer omits the reverse-charge entries | EUR 500 to 10,000; 5% of the base, minimum EUR 1,000, if the operation is not in the books. If the supplier charged VAT by mistake, EUR 250 to 10,000 and the buyer keeps the deduction | D.Lgs. 471/1997 art. 6(9-bis) and (9-bis.1) |

**Ravvedimento operoso (D.Lgs. 472/1997 art. 13, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-10-24).** Before an assessment is notified, the business can pay the tax, the reduced penalty and interest together. The penalty falls to: one tenth of the minimum for a missed payment made within 30 days (lett. a); one ninth within 90 days (a-bis); one eighth by the deadline of the return for the year of the violation (b); one seventh after that (b-bis); one sixth, one fifth or one quarter after a tax audit report or a draft assessment (b-ter to b-quinquies). Interest runs at the legal rate, day by day (art. 13(2)): 1.60% for 2026.

**Quarterly interest is not a penalty.** The 1% on quarterly payments is the price of the option (D.P.R. 542/1999 art. 7(3)); late quarterly payments carry both.

## Cross-border points

- **Services bought from abroad.** B2B services are taxed where the Italian buyer is established (art. 7-ter(1)(a)); the buyer self-assesses under art. 17(2) and reports through the SdI (TD17), which also covers the esterometro.
- **Services sold abroad.** B2B to a business established elsewhere: not subject to Italian VAT (N2.1), invoice by the 15th of the next month for EU customers, VIES check, intra-EU listing (Intrastat) for EU services.
- **Goods.** Intra-EU B2B sales are non-taxable (D.L. 331/1993 art. 41, N3.2) and intra-EU purchases are self-assessed (TD18). Exports are non-taxable (art. 8, N3.1). Import VAT is paid at customs and deducted from the customs bill.
- **B2C to other EU countries.** Up to EUR 10,000 a year of distance sales and e-services, Italian VAT applies; above it, the customer's country's VAT applies, normally through OSS (D.L. 331/1993 art. 41(1)(b); `eu-vat-directive`).
- **Non-residents.** A foreign business supplying Italian businesses usually leaves the VAT to the buyer (art. 17(2)). One that must register uses direct identification or a fiscal representative: refer.
- **Forfettari abroad.** They apply the normal place-of-supply rules to cross-border services and pay reverse-charge VAT on purchases themselves (L. 190/2014 art. 1(58)(d) and (e-bis)).

## Worked examples

**Example 1: quarterly filer, Q2 2026.** A software consultancy (services) had a 2025 volume d'affari of EUR 300,000, below the EUR 500,000 limit, and opted for quarterly settlement. In April to June 2026 it invoices EUR 60,000 at 22% to Italian clients and EUR 20,000 of consulting to a German company (out of scope under art. 7-ter, N2.1, still in VP2). It buys EUR 2,000 of software from a US company (self-invoice TD17: VAT 440 in VP4 and VP5), EUR 10,000 of Italian services at 22% (VAT 2,200) and leases a car used for business and private trips for EUR 3,000 plus 22% VAT of 660, of which 40% (264) is deductible. VP2 = 80,000; VP3 = 15,000; VP4 = 13,200 + 440 = 13,640; VP5 = 440 + 2,200 + 264 = 2,904; VP6 = 10,736. The 1% interest is 107.36 (VP12), so VP14 = 10,843.36. The 16 August deadline is a Sunday inside the August window, so the F24 is due by Thursday 20 August 2026. The Q2 LIPE is due 30 September 2026.

```oa-check
name: Italy quarterly settlement Q2 2026 with reverse charge and car limit
inputs:
  sales_it_22: 60000
  services_to_eu_b2b: 20000
  software_us: 2000
  purchases_it_22: 10000
  car_lease: 3000
steps:
  - vp2: sales_it_22 + services_to_eu_b2b
  - vp3: software_us + purchases_it_22 + car_lease
  - reverse_charge_vat: software_us * 0.22
  - vp4: sales_it_22 * 0.22 + reverse_charge_vat
  - car_vat_deductible: car_lease * 0.22 * 0.40
  - vp5: reverse_charge_vat + purchases_it_22 * 0.22 + car_vat_deductible
  - vp6: vp4 - vp5
  - vp12_interest: vp6 * 0.01
  - vp14: vp6 + vp12_interest
expected:
  vp2: 80000
  vp3: 15000
  vp4: 13640
  car_vat_deductible: 264
  vp5: 2904
  vp6: 10736
  vp12_interest: 107.36
  vp14: 10843.36
```

**Example 2: monthly filer pays September 2026 VAT ten days late.** A retailer files monthly. Its September 2026 settlement shows EUR 8,000 due by Friday 16 October 2026. It pays on Monday 26 October, ten days late, before any audit, and uses ravvedimento. The base penalty is 25%; paid within 90 days it is halved to 12.5%; paid within 15 days it is 12.5% divided by 15 for each of the 10 days (D.Lgs. 471/1997 art. 13(1)). Ravvedimento within 30 days cuts that to one tenth (D.Lgs. 472/1997 art. 13(1)(a)): 8,000 x 12.5% x 10/15 / 10 = 66.67. Interest at the legal rate of 1.60% for 10 days: 8,000 x 1.60% x 10/365 = 3.51. The F24 carries 8,070.18 in total: tax, penalty and interest, each under its own code.

```oa-check
name: Italy monthly VAT paid 10 days late with ravvedimento (2026)
inputs:
  vat_due: 8000
  days_late: 10
  legal_rate: 0.016
steps:
  - base_penalty: vat_due * 0.25
  - within_90_days: base_penalty / 2
  - within_15_days: within_90_days * days_late / 15
  - ravvedimento_penalty: round(within_15_days / 10, 2)
  - interest: round(vat_due * legal_rate * days_late / 365, 2)
  - total_f24: vat_due + ravvedimento_penalty + interest
expected:
  base_penalty: 2000
  within_90_days: 1000
  ravvedimento_penalty: 66.67
  interest: 3.51
  total_f24: 8070.18
```

## Ask the client first

- Regime ordinario, forfettario or minimi? If forfettario, what were 2025 revenues and have 2026 revenues passed EUR 100,000? (Whether VAT is charged at all.)
- Monthly or quarterly, and what was the 2025 volume d'affari, split between services and other activities? (Frequency, 1% interest.)
- Do you sell to public bodies or publicly controlled companies, or make exempt sales? (Split payment; pro rata, refer.)
- Who are your foreign customers and suppliers, by legal entity and country, B2B or B2C? (Reverse charge, esterometro, OSS.)
- Do you work in construction, cleaning or installation on buildings, or sell phones, laptops or energy to resellers? (Domestic reverse charge.)
- Do you have VAT credit from the previous period (VP8) or last year's return (VP9), any car, entertainment or phone costs, and any late payments in 2026? (Deductions, ravvedimento.)

## Sources

| Source | URL | Read on |
|---|---|---|
| D.P.R. 633/1972 art. 1 (scope) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art1!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 633/1972 art. 7-ter (B2B place of supply of services) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art7ter!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 633/1972 art. 16 (rates) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art16!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 633/1972 Tabella A (Parts II, II-bis, III) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633:1~allA!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 633/1972 art. 17 (reverse charge) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art17!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 633/1972 art. 17-ter (split payment) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art17ter!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 633/1972 art. 19-bis.1 (deduction limits) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art19bis.1!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 633/1972 art. 74 (scrap reverse charge) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art74!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 633/1972 art. 21 (invoices, timing) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art21!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 100/1998 art. 1 (monthly settlement, EUR 100 carry) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-03-23;100~art1!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 542/1999 art. 7 (quarterly option, 1% interest) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1999-10-14;542~art7!vig=2026-10-24 | 2026-10-24 |
| L. 183/2011 art. 14(11) (quarterly limits = simplified-accounts limits) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2011-11-12;183~art14!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 600/1973 art. 18(1) (EUR 500,000 / 800,000) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art18!vig=2026-10-24 | 2026-10-24 |
| D.L. 78/2010 art. 21-bis (LIPE) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art21bis!vig=2026-10-24 | 2026-10-24 |
| D.L. 223/2006 art. 37(11-bis) (August payments) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2006-07-04;223~art37!vig=2026-10-24 | 2026-10-24 |
| D.L. 70/2011 art. 7(2)(l) (weekend and holiday deadlines) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-05-13;70~art7!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 322/1998 art. 8 (annual return window) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art8!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 127/2015 art. 1 (SdI e-invoicing, esterometro) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig=2026-10-24 | 2026-10-24 |
| D.L. 36/2022 art. 18 (e-invoicing for forfettari) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2022-04-30;36~art18!vig=2026-10-24 | 2026-10-24 |
| L. 190/2014 art. 1 commi 54-89 (regime forfettario, VAT effects) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-10-24 | 2026-10-24 |
| D.L. 331/1993 art. 41 (intra-EU supplies, EUR 10,000) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art41!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 471/1997 art. 6 (invoicing and reverse-charge penalties) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art6!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 471/1997 art. 11 (LIPE and esterometro penalties) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 471/1997 art. 13 (late payment, as amended by D.Lgs. 87/2024) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 472/1997 art. 13 (ravvedimento) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-10-24 | 2026-10-24 |
| TUIR arts. 102(5) and 54-quinquies(1) (small-asset limits) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art102!vig=2026-10-24 and https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=2026-10-24 | 2026-10-24 |
| D.M. 10 December 2025, legal interest 1.60% from 1 January 2026 (GU n. 289, 13 December 2025) | https://www.gazzettaufficiale.it/eli/id/2025/12/13/25A06705/sg | 2026-10-24 |
| Council Implementing Decision (EU) 2026/1728 (split payment to 30 June 2029) | https://eur-lex.europa.eu/eli/dec_impl/2026/1728/oj/eng | 2026-10-24 |
| Agenzia delle Entrate, "Come pagare l'Iva" | https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva | 2026-10-24 |
| Agenzia delle Entrate, LIPE instructions (2024 edition, VP rows) | https://www.agenziaentrate.gov.it/portale/documents/20143/5986193/IVA+period_2024.pdf/04990f53-edc9-048a-c953-49592ebea05f | 2026-10-24 |

Not yet confirmed: whether the EU Council has authorised the logistics reverse charge in art. 17(6)(a-quinquies), so it is not treated as in force; the full lists of Tabella A Parts II and III beyond the items named (home renovation at 10% under L. 488/1999 art. 7 was not read); the date the 5% rate for works of art (Part II-bis n. 1-novies) took effect; how a split-payment sale fills VP2 and VP4 (not checked in the LIPE instructions); the start date of L. 190/2014 art. 1(58)(e-bis) (quarterly payment of forfettari reverse-charge VAT; comma 60 still speaks of the 16th of the following month); the Intrastat thresholds and deadlines for services; F24 tax codes (6001 to 6012 monthly, 6031 to 6034 quarterly, and the ravvedimento penalty and interest codes) and ABI bank causale codes, carried from the old version unchecked; whether a 2026 or 2027 LIPE model replaces the 2024 instructions; the bank-statement reading notes and supplier entities in the classification list are OpenAccountants' working list, not law.

> Contributed by OpenAccountants.

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
