---
name: italy-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Italian VAT return (Liquidazione IVA Periodica / LIPE) for a self-employed individual or small business under the regime ordinario in Italy. Trigger on phrases like "prepare LIPE", "Italian VAT return", "Liquidazione IVA", "IVA italiana", "classify transactions for Italian VAT", or any request involving Italy VAT filing. This skill covers Italy only, regime ordinario (monthly or quarterly LIPE). Regime forfettario, regime dei minimi, split payment, margin schemes, and VAT groups are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Italian VAT work.
version: 2.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italian VAT return: periodic settlement and LIPE (regime ordinario)

How a business under the regime ordinario in Italy classifies transactions, settles IVA monthly or quarterly, pays by F24 and files the quarterly LIPE (Comunicazione delle liquidazioni periodiche IVA). Figures are for tax year 2026. Sources: the Agenzia's VAT rates page (updated 12/12/2020) and VAT payment page (updated 20/09/2024), both current on 22 September 2026; the LIPE model and instructions, the Agenzia's 2024 file, current per its model page; statutes on Normattiva in force on 30 June 2026.

## Italy VAT Return Guide (LIPE / Liquidazione IVA Periodica) v2.1

## Section 1: Quick reference

**Read this section first. Follow the runbook in `vat-workflow-base` Section 1; this Guide gives the Italian content, `eu-vat-directive` the EU content.**

| Field | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/web/guest/iva-regole-generali-aliquote-esenzioni-pagamento/norme-generali-e-aliquote |
| Country | Italy (Repubblica Italiana) | |
| Standard rate | 22% | "In Italia l’aliquota ordinaria Iva è del 22%" |
| Reduced rates | 10% (e.g. electricity, some renovation), 5% (some foods), 4% (e.g. basic food, drinks, agricultural products) | "4% , per esempio per alimentari, bevande e prodotti agricoli" |
| Exports, intra-EU B2B goods | Non imponibile: no IVA charged, right to deduct kept (Section 5.5) | |
| Return forms | LIPE every quarter; annual Dichiarazione IVA | Deadlines in the next table |
| Filing | Online only, directly or through an intermediary | |
| Authority | Agenzia delle Entrate | |
| Currency | EUR only | |
| Companion Guide (Tier 1, workflow) | **vat-workflow-base v0.1+, MUST load** | |
| Companion Guide (Tier 2, EU directive) | **eu-vat-directive v0.1+, MUST load** | |
| Validation date | September 2026 | |

**Frequency, payment and filing deadlines**

| Item | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva |
| Default | Monthly settlement and payment by F24 online, by the 16th of the next month | "Entro il giorno 16 di ciascun mese" |
| Quarterly option: services and self-employed | Prior calendar year volume d'affari not above EUR 500,000 | "500.000 euro, per i lavoratori autonomi e per le imprese" |
| Quarterly option: other activities | Prior calendar year volume d'affari not above EUR 800,000 | "800.000 euro, per le imprese che esercitano altre attività" |
| Quarterly interest | Tax due for each quarter is increased by 1% | "L’imposta dovuta va maggiorata dell’1% a titolo di interessi" |
| Quarterly payment, Q1 to Q3 | By the 16th of the second month after the quarter | |
| Quarterly payment, Q4 | By 16 March of the following year | "va effettuata entro il 16 marzo dell’anno successivo" |
| December acconto | By 27 December, all VAT payers except exempt categories; no 1% interest on it | "categorie esonerate dall’adempimento" |

| Item | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2006-07-04;223~art37!vig=2026-06-30 |
| Payments due from 1 to 20 August (July monthly, Q2 quarterly) | May be made by 20 August without any surcharge | "possono essere effettuati entro il giorno 20 dello stesso mese, senza alcuna maggiorazione" |

| Item | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art21bis!vig=2026-06-30 |
| LIPE, Q1 and Q3 | Last day of the second month after the quarter (31 May, 30 November) | "entro l'ultimo giorno del secondo mese successivo a ogni trimestre" |
| LIPE, Q2 | 30 September | Art. 21-bis(1), as amended |
| LIPE, Q4 | End of February, or inside the annual return filed by end of February | Art. 21-bis(1) D.L. 78/2010 |
| Credit periods | LIPE is filed even when the period shows a credit | Art. 21-bis(3) |
| Exempt from LIPE | Persons not required to file the annual return or to make periodic settlements; also no LIPE for a quarter with nothing to report in quadro VP | Art. 21-bis(3); LIPE instructions |
| Weekend or holiday | A LIPE deadline on a Saturday or holiday moves to the next working day | LIPE instructions |

| Item | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art8!vig=2026-06-30 |
| Annual Dichiarazione IVA | Filed online between 1 February and 30 April of the next year | Art. 8(1) D.P.R. 322/1998 |

**LIPE rows (quadro VP), as the Agenzia's instructions define them**

| Row | Meaning | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/5986193/IVA+period_2024.pdf/04990f53-edc9-048a-c953-49592ebea05f |
| VP1 | Month or quarter (quarterly filers enter "5" for the fourth quarter) | |
| VP2 | Total sales (operazioni attive) net of IVA: taxable, non-taxable, exempt, and out-of-scope sales under arts. 7 to 7-septies that need an invoice; also the base of sales where the buyer owes the IVA | "Totale operazioni attive (al netto dell’IVA)" |
| VP3 | Total purchases net of IVA: domestic, intra-EU and imports (customs documents), including non-deductible ones | "Totale operazioni passive (al netto dell’IVA)" |
| VP4 | IVA esigibile (output VAT), including reverse-charge IVA the buyer owes | |
| VP5 | IVA detratta (input VAT deducted), including reverse-charge IVA when deductible | |
| VP6 | VP4 minus VP5: column 1 IVA due, column 2 credit | |
| VP7 | Debt from the previous period not paid because not above EUR 100 | "Debito periodo precedente non superiore a 100 euro" |
| VP8 | Credit from the previous settlement of the same calendar year | |
| VP9 | Credit from the prior year's annual return used in this period | |
| VP10 | F24 "elementi identificativi" payments for first domestic sales of cars | |
| VP11 | Special tax credits used against the payment | |
| VP12 | Interest due by quarterly filers, at the 1% rate; not filled for Q4 | |
| VP13 | Acconto due, with method code (1 historical, 2 forecast, 3 actual, 4 special sectors); none if below EUR 103.29 | "inferiore a euro 103,29" |
| VP14 | IVA to pay (column 1) or credit (column 2): (VP6 col. 1 + VP7 + VP12) minus (VP6 col. 2 + VP8 + VP9 + VP10 + VP11 + VP13 col. 2); not filled by quarterly filers for Q4 | |

**Registri IVA (VAT registers)**

| Register | Purpose |
| --- | --- |
| Registro delle fatture emesse | Sales invoices issued |
| Registro degli acquisti | Purchase invoices received |
| Registro dei corrispettivi | Daily receipts (retail/hospitality) |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Standard rate |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Italy |
| Unknown B2B vs B2C status for EU customer | B2C, charge Italian IVA |
| Unknown business-use proportion (vehicle, phone, home office) | No recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (art. 17(2) D.P.R. 633/1972) |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds.** Flag large transactions, large default effects, a dominant counterparty, many defaults, and a large net position. No official page sets amounts; the firm chooses.

## Section 2: Required inputs and refusal catalogue

### Required inputs

**Minimum viable.** A bank statement covering the full period (CSV, PDF or pasted text), from any bank.

**Recommended.** The period's fatture elettroniche from the SdI, purchase invoices for material input VAT claims, and the client's Partita IVA (IT plus 11 digits).

**Ideal.** Full SdI XML extract, prior LIPE, Registri IVA, and a VP8/VP9 credit reconciliation.

**Refusal policy if minimum is missing: SOFT WARN.** No bank statement: hard stop. Statement without invoices: proceed, but flag that material input IVA claims and reverse-charge lines need checking against the SdI invoices before approval.

### Italy-specific refusal catalogue

| Refusal | Trigger | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- |
| R-IT-1 | Client is under the regime forfettario. Entry needs prior-year revenue or fees, annualised, not above EUR 85,000; revenue above EUR 100,000 during the year ends the regime that same year, with IVA due from the sale that crosses it | "non superiori a 85.000 euro"; "se però si va oltre i 100.000 euro di ricavi/compensi, non è più applicabile dallo stesso anno" |

- **R-IT-1**: "This Guide covers the regime ordinario only. Forfettari charge no IVA and recover none. If revenue crossed the upper limit above during the year, the regime ended: refer." _(On top of the EU-wide refusals R-EU-1 to R-EU-12 in eu-vat-directive Section 13.)_
- **R-IT-2**: regime dei minimi. "Outside the ordinary IVA system; regime ordinario only."
- **R-IT-3**: supplies to public bodies under split payment (art. 17-ter D.P.R. 633/1972). "The buyer pays the IVA; out of scope."
- **R-IT-4**: taxable and exempt-without-credit supplies with a material exempt share. "Pro rata under arts. 19 and 19-bis D.P.R. 633/1972; use a commercialista."
- **R-IT-5**: second-hand goods, art, antiques, collectables. "Margin scheme; out of scope."
- **R-IT-6**: VAT group (arts. 70-bis to 70-duodecies D.P.R. 633/1972). "Out of scope."
- **R-IT-7**: non-resident with a fiscal representative in Italy. "Use a commercialista."
- **R-IT-8**: income tax (IRPEF, IRES, Modello Redditi). "This Guide handles IVA only."

## Section 3: Supplier pattern library (the lookup table)

Deterministic pre-classifier: match by case-insensitive substring on the counterparty name; the most specific pattern wins; else use Section 5. Patterns are OpenAccountants' own list, not an official source; treatments follow Section 5. Shorthand: domestic purchase = VP3 (net) + VP5 (deductible IVA); reverse charge = VP3 (net) + IVA in VP4, and in VP5 only if deductible, never in VP2; sale = VP2 + VP4. EXCLUDE means no IVA to claim: an exempt or non-taxable purchase with a fattura in the registro degli acquisti still counts in VP3; a bank line with no fattura (F24, wages, transfers) stays out.

### 3.1 Italian banks (fees exempt: exclude)

_(art. 10(1) n. 1 D.P.R. 633/1972)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UNICREDIT, INTESA SANPAOLO, BANCO BPM, MONTE DEI PASCHI (MPS), BPER BANCA, POSTE ITALIANE/BANCOPOSTA, CREDEM | EXCLUDE bank charges/fees | Financial service, exempt |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscription invoices |
| INTERESSI; MUTUO, PRESTITO, FINANZIAMENTO | EXCLUDE | Interest; loan principal |

### 3.2 Italian government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AGENZIA ENTRATE; F24, PAGAMENTO F24; EQUITALIA, AGENZIA RISCOSSIONE | EXCLUDE | Tax payments and collection |
| INPS, INAIL | EXCLUDE | Contributions |
| CAMERA DI COMMERCIO, CCIAA; COMUNE DI; REGIONE, PROVINCIA | EXCLUDE | Public fees and local taxes |
| DOGANA, AGENZIA DOGANE | EXCLUDE the payment line | The customs document (bolletta doganale) value, net of IVA, goes to VP3; its IVA, if deductible, to VP5 |

### 3.3 Italian utilities

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ENEL, ENI PLENITUDE, EDISON, A2A, IREN, HERA, ACEA | Domestic, rate from the invoice | Electricity, gas, water: may be reduced rate |
| TIM, VODAFONE ITALIA, WINDTRE, FASTWEB, ILIAD | Domestic standard | Telecoms: business share only (Section 5.12) |

### 3.4 Insurance (exempt: exclude)

_(art. 10(1) n. 2)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GENERALI, ALLIANZ, UNIPOLSAI, AXA ITALIA, CATTOLICA, ZURICH, ASSICURAZIONE, POLIZZA | EXCLUDE | Insurance, exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Notes |
| --- | --- | --- |
| POSTE ITALIANE (standard mail) | EXCLUDE | Universal postal service, exempt |
| POSTE DELIVERY (parcels), SDA, BRT, DHL EXPRESS, GLS, TNT | Domestic standard | Courier services are taxable |

### 3.6 Transport (Italy domestic)

IVA on passenger transport is not deductible unless transport is the business's own activity (art. 19-bis.1(1)(e), Section 5.12). Net to VP3; nothing to VP5.

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRENITALIA, ITALO, ATAC, ATM MILANO, GTT, ANM, UBER, TAXI, ITA AIRWAYS (domestic) | BLOCK input IVA | Passenger transport |
| ITA AIRWAYS, RYANAIR, EASYJET (international) | EXCLUDE | No Italian IVA to recover |
| AUTOSTRADE, TELEPASS | Same deduction share as the vehicle | Follows the vehicle share (art. 19-bis.1(1)(d)) |

### 3.7 Food retail (blocked unless hospitality business)

_(art. 19-bis.1(1)(f) and (h))_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ESSELUNGA, CONAD, COOP, EUROSPIN, LIDL, CARREFOUR, PENNY, MD, PAM, DESPAR, IPER | Default BLOCK | Not deductible unless the business's own activity |
| RISTORANTE, TRATTORIA, PIZZERIA, BAR | Default BLOCK | See Section 5.12 |

### 3.8 SaaS: EU suppliers (reverse charge, Art. 17 c.2 / inversione contabile)

The buyer integrates the invoice and sends a TD17 document to the SdI (see `italy-einvoice`).

| Pattern | Billing entity | Treatment |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META/FACEBOOK ADS, LINKEDIN, DROPBOX, SLACK, ZOOM | Irish entities (IE) | Reverse charge, VP3 + VP4/VP5 |
| SPOTIFY TECHNOLOGY; ATLASSIAN | Spotify AB (SE); Atlassian Network Services BV (NL) | Reverse charge |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | Reverse charge; transaction fees see 3.11 |

### 3.9 SaaS: non-EU suppliers (reverse charge, Art. 17 c.2)

The buyer issues a self-invoice (autofattura) and sends a TD17 document to the SdI.

| Pattern | Billing entity | Treatment |
| --- | --- | --- |
| NOTION, ANTHROPIC, OPENAI, FIGMA, TWILIO | US entities | Reverse charge, VP3 + VP4/VP5 |
| CANVA | Canva Pty Ltd (AU) | Reverse charge |
| GITHUB, HUBSPOT | US or IE entity, check the invoice | Reverse charge either way; follows the entity |
| AWS | AWS EMEA SARL (LU), check | EU reverse charge |

### 3.10 SaaS: the exception (NOT reverse charge)

| Pattern | Treatment | Why |
| --- | --- | --- |
| AWS EMEA SARL | EU reverse charge (Luxembourg entity) | If the invoice shows Italian IVA, treat as a domestic purchase |

### 3.11 Payment processors

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE, PAYPAL (transaction fees) | EXCLUDE (exempt) | Exempt financial service |
| SUMUP, SQUARE, ZETTLE, NEXI, SATISPAY | Check invoice | Italian entity: domestic, fees may be exempt; EU entity: reverse charge |

### 3.12 Professional services (Italy)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| COMMERCIALISTA, AVVOCATO, NOTAIO, CONSULENTE DEL LAVORO, ARCHITETTO, INGEGNERE, GEOMETRA | Domestic standard | Deductible when for the business |
| REGISTRO IMPRESE | EXCLUDE | Registry fee |

### 3.13 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INPS, INAIL, STIPENDIO, BUSTA PAGA, TFR, CASSA PREVIDENZA, ENPAM, CNPADC | EXCLUDE | Wages, severance and contributions are outside IVA |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AFFITTO COMMERCIALE, LOCAZIONE COMMERCIALE | Domestic standard | Where the landlord charges IVA |
| AFFITTO, LOCAZIONE (residential) | EXCLUDE | IVA on residential buildings is not deductible (art. 19-bis.1(1)(i)) |
| IMU, TASI | EXCLUDE | Property tax |
| CONDOMINIO | Check | Only if IVA is invoiced |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GIROCONTO, BONIFICO INTERNO, TRASFERIMENTO TRA CONTI | EXCLUDE | Own-account transfer |
| DIVIDENDO, RATA MUTUO, RIMBORSO PRESTITO, APPORTO PERSONALE, VERSAMENTO SOCIO | EXCLUDE | Dividends, loans, owner money |
| PRELIEVO BANCOMAT, PRELIEVO CONTANTI | TIER 2, ask | Default exclude |

## Section 4: Worked examples

Six cases for a self-employed IT consultant. Amounts are illustrative.

### Example 1: Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; 16.00 US dollars ; 14.68 euro`

**Reasoning:**
US supplier, no IVA on the invoice. The client self-assesses under art. 17(2) D.P.R. 633/1972 with an autofattura (TD17). Net in VP3; IVA in VP4 and VP5; net effect zero.

**Output table** _(none)_

| Date | Counterparty | Gross | Net | VAT | Rate | Field (input) | Field (output) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.23 | 22% | VP3 + VP5 | VP4 | N | none | none |

### Example 2: EU service, inversione contabile (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`

**Reasoning:**
Irish supplier: EU reverse charge on a service. The client integrates the invoice (TD17). Net in VP3; IVA in VP4 and VP5.

**Output table** _(none)_

| Date | Counterparty | Gross | Net | VAT | Rate | Field (input) | Field (output) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 187.00 | 22% | VP3 + VP5 | VP4 | N | none | none |

### Example 3: Business dinner (spese di rappresentanza)

**Input line:**
`15.04.2026 ; RISTORANTE DA MARIO ROMA ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
A client dinner is entertainment (spesa di rappresentanza): IVA not deductible (art. 19-bis.1(1)(h) D.P.R. 633/1972). A business-trip meal is not entertainment: deductible with a fattura (D.L. 112/2008 removed the old restaurant ban). VP3 takes the net-of-IVA amount even when not deductible. Default: block and ask.

**Output table** _("Restaurant: client entertainment or a meal on a business trip? Do you have a fattura?")_

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | RISTORANTE DA MARIO ROMA | -220.00 | net on the fattura | IVA on the fattura | rate on the fattura | VP3 (net of IVA) only; IVA not deductible | Y | Q1 | "Client entertainment or business-trip meal? Fattura?" |

### Example 4: Capital goods (bene strumentale)

**Input line:**
`18.04.2026 ; DELL ITALIA SRL ; DEBIT ; Invoice DEL2026-0041 Laptop XPS-15 ; -1,595.00 ; EUR`

**Reasoning:**
Input IVA is deductible (VP5) like any business purchase; the LIPE has no capital goods row. For income tax, a unit cost above the Section 5.11 limit for the client's income type means depreciation: flag it for the registro dei beni ammortizzabili.

**Output table** _(none)_

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | DELL ITALIA SRL | -1,595.00 | -1,307.38 | -287.62 | 22% | VP3 + VP5 | N | none | none |

### Example 5: EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice IT-2026-018 IT consultancy March ; +3,500.00 ; EUR`

**Reasoning:**
B2B service to a German business, supplied in Germany (art. 7-ter D.P.R. 633/1972): not subject to Italian IVA (non soggetta, N2.1), not "non imponibile". The invoice is still required, marked "inversione contabile" (art. 21(6-bis)), and goes in VP2. Check the VAT number on VIES.

**Output table** _("Verify German USt-IdNr on VIES")_

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | n/a | VP2 (non soggetta) | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6: Motor vehicle, partial recovery

**Input line:**
`28.04.2026 ; LEASYS SPA ; DEBIT ; Lease payment Fiat 500X ; -450.00 ; EUR`

**Reasoning:**
Vehicles not used exclusively for the business take the Section 5.12 share (art. 19-bis.1(1)(c)); full rules apply if it is the business's own activity (taxi, driving school, rental) or for agenti e rappresentanti di commercio. IT consultant: reduced share.

**Output table** _("Vehicle: partial IVA deduction. Core business vehicle, or are you a commercial agent?")_

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28.04.2026 | LEASYS SPA | -450.00 | -368.85 | -81.15 (x 40% = -32.46 deductible) | 22% | VP3 + VP5 (partial) | Y | Q3 | "Vehicle: partial deduction. Core business vehicle or agent?" |

## Section 5: Tier 1 classification rules (compressed)

### 5.1 Standard rate 22% (art. 16 D.P.R. 633/1972)

- Default for any supply not listed in Table A.

### 5.2 Reduced rate 10% (Table A, Part III, D.P.R. 633/1972)

- E.g. electricity supply (table below); other goods and services: read the invoice and Table A, Part III.

### 5.3 Reduced rate 5% (Table A, Part II-bis)

- A narrow list, e.g. some foods.

### 5.4 Super-reduced rate 4% (Table A, Part II)

- E.g. food, drinks and agricultural products. Sales at any rate: VP2/VP4; purchases: VP3/VP5.

| Rate | Examples on the Agenzia page | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/web/guest/iva-regole-generali-aliquote-esenzioni-pagamento/norme-generali-e-aliquote |
| 22% | Ordinary rate | "In Italia l’aliquota ordinaria Iva è del 22%" |
| 10% | E.g. electricity supply | "10% , per esempio per la fornitura di energia elettrica" |
| 5% | E.g. some foods | "5% , per esempio per alcuni alimenti" |
| 4% | E.g. food, drinks, agricultural products | "4% , per esempio per alimentari, bevande e prodotti agricoli" |

### 5.5 Zero rate and exempt with credit (non imponibile)

- Exports outside the EU (art. 8 D.P.R. 633/1972, export evidence needed, nature code N3.1). Intra-EU B2B supplies of goods (art. 41 D.L. 331/1993, VIES check, N3.2). B2B services to EU businesses are not "non imponibile" but out of scope (non soggette, art. 7-ter, N2.1). All three go in VP2.

### 5.6 Exempt without credit (esente art. 10)

- Medical, education, insurance, financial, residential rent, universal postal service. No deduction on related costs; if significant, R-IT-4.

### 5.7 Local standard purchases

- IVA on a compliant fattura for taxable business use is deductible, subject to 5.12. Net to VP3, IVA to VP5.

### 5.8 Inversione contabile: EU services received (Art. 17 c.2 + Art. 7-ter)

- No IVA on the invoice; the client integrates it (TD17). Net to VP3; IVA to VP4 and VP5.

### 5.9 Inversione contabile: EU goods received

- Intra-EU acquisition; the client integrates the supplier invoice (TD18). Net to VP3; IVA to VP4 and VP5.

### 5.10 Inversione contabile: non-EU services and imports

- **Non-EU services**: autofattura (TD17). Net to VP3; IVA to VP4 and VP5.
- **Imports of goods**: customs IVA on the bolletta doganale; net to VP3, deductible IVA to VP5. No general LIPE deferral was found on an official page.

### 5.11 Capital goods (beni strumentali)

- Ordinary IVA deduction (VP5), no LIPE row. Matters for the annual return and the rettifica della detrazione (art. 19-bis2). Income tax: unit cost up to the limit below may be expensed in the year.

| Item | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art102!vig=2026-06-30 |
| Full deduction in the year, business income (reddito d'impresa, TUIR art. 102(5)) | Unit cost not above EUR 516.46 | "non è superiore a 516,46 euro" |

| Item | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30 |
| Full deduction in the year, professionals (lavoro autonomo, TUIR art. 54-quinquies(1)) | Unit cost not above EUR 516.40 | "il cui costo unitario non sia superiore a euro 516,40" |

### 5.12 Blocked input IVA (art. 19-bis.1 D.P.R. 633/1972)

| Item | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19bis.1!vig=2026-06-30 |
| Road vehicles not used exclusively for the business (lett. c) | 40% deductible | "nella misura del 40 per cento"; covers road vehicles up to 3,500 kg with up to eight seats besides the driver |
| Exceptions (lett. c) | Full rules apply when the vehicle is the business's own activity, or for commercial agents and representatives | |
| Fuel, repairs, maintenance, road transit (lett. d) | Same share as the vehicle; fuel must be paid by card or other traceable means | |
| Passenger transport (lett. e) | Not deductible, unless transport is the business's own activity | |
| Food and drink (lett. f) | Not deductible, unless the business's own activity or canteen supply | |
| Entertainment, spese di rappresentanza (lett. h) | Not deductible, except goods costing no more than fifty euro each | "non superiore ad euro cinquanta" |
| Residential buildings (lett. i) | Purchase, rent, upkeep not deductible, except for builders of such buildings | |

- **Telephone and internet**: no fixed share; lett. g was repealed by L. 244/2007. Deduct the business share only (art. 19).
- **Hotels, business-trip meals**: deductible with a fattura. **Personal items**: not deductible.

### 5.13 Quarterly interest surcharge

- Quarterly filers add the interest in the Section 1 payment table to Q1 to Q3 tax due, in VP12; for Q4 it is paid with the annual balance. Monthly filers do not (art. 7 D.P.R. 542/1999).

### 5.14 Sales: local domestic (any rate)

- Charge the applicable rate from the table in 5.4. All via fattura elettronica through the SdI.

### 5.15 Sales: cross-border B2C

| Item | Rule | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art41!vig=2026-06-30 |
| EU-wide threshold for distance sales of goods (and B2C telecom, broadcasting and electronic services) | Above EUR 10,000 in the prior or current year, IVA of the customer's country applies | "anno solare precedente 10.000 euro" |

- Above the threshold in the table, R-EU-5 (OSS) refuses. Below it, Italian IVA at the applicable rate.

## Section 6: Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

- ENI, Q8, IP, ESSO, SHELL: share depends on the vehicle (Section 5.12) and needs traceable payment. Default: the reduced share. Ask: "Core business vehicle, commercial agent, or a standard car?"

### 6.2 Restaurants and entertainment

- Client entertainment is blocked; a business-trip meal is deductible with a fattura. Default: block. Ask: "Who was at the meal and why? Fattura?"

### 6.3 Ambiguous SaaS billing entities

- Default non-EU reverse charge. Ask: "Legal entity name and country on the invoice?"

### 6.4 Round-number incoming transfers from owner-named counterparties

- Default exclude as owner injection. Ask: "Customer payment, own money, or loan?"

### 6.5 Incoming transfers from individual names (not owner)

- Default domestic B2C sale at the standard rate. Ask: "Was it a sale?"

### 6.6 Incoming transfers from foreign counterparties

- Default domestic sale at the standard rate. Ask: "B2B or B2C, goods or services, which country?"

### 6.7 Large one-off purchases (potential beni strumentali)

- IVA unchanged; income tax limit in the Section 5.11 table. Ask: "Unit cost on the invoice?"

### 6.8 Mixed-use phone, internet

- No recovery until the business share is known (Section 5.12). Ask: "Business line or mixed? What share is business?"

### 6.9 Outgoing transfers to individuals

- Default exclude as drawings. Ask: "Contractor, wages, refund, or personal?"

### 6.10 Cash withdrawals

- Default exclude. Ask: "What was the cash used for?"

### 6.11 Rent payments

- Default no IVA (residential). Ask: "Commercial or residential? Does the landlord charge IVA?"

### 6.12 Foreign hotel and accommodation

- Exclude; foreign VAT is not Italian IVA.

### 6.13 Airbnb income

- [T2] flag. Ask: "Short-term tourist rental? Cedolare secca?"

### 6.14 Domestic reverse charge (construction, cleaning)

- Construction subcontracting, building cleaning and energy fall under art. 17(6) D.P.R. 633/1972 (TD16). [T2] flag.

### 6.15 Platform sales

- EU B2C sales above the Section 5.15 threshold: R-EU-5. Otherwise domestic sales; platform fees as EU reverse charge.

## Section 7: Excel working paper template (Italy-specific)

The base specification is in `vat-workflow-base` Section 3. This is the Italian overlay.

### Sheet "Transactions"

Columns A to L per the base. Column H ("Field code") takes the VP row codes from Section 1. For reverse-charge lines, enter VP3 and VP4/VP5.

### Sheet "Field Summary"

**Field Summary mandatory rows**

| Row | Meaning | Formula |
| --- | --- | --- |
| VP2 | Total sales, net | =SUMIFS(Transactions!E:E, ..., "VP2") |
| VP3 | Total purchases, net | =SUMIFS(Transactions!E:E, ..., "VP3") |
| VP4 | IVA esigibile | =SUM(output IVA incl. reverse charge) |
| VP5 | IVA detratta | =SUM(deductible IVA incl. reverse charge) |
| VP6 | IVA due or credit | =VP4-VP5 (column 1 if positive, column 2 if negative) |
| VP7 | Unpaid small debt from previous period | (manual entry) |
| VP8 | Credit from previous period, same year | (manual entry) |
| VP9 | Credit from prior year's annual return used | (manual entry) |
| VP12 | Quarterly interest (Q1 to Q3 only) | =net due x the rate in the payment table |
| VP13 | Acconto (December or Q4) | (manual entry) |
| VP14 | IVA to pay or credit | =(VP6c1+VP7+VP12)-(VP6c2+VP8+VP9+VP10+VP11+VP13c2) |

### Sheet "Return Form"

- **LIPE-ready figures formula**: VP6 column 2 if VP5 > VP4, else column 1; VP14 as above; quarterly filers leave VP12 and VP14 empty for Q4.

### Mandatory recalc step

~~~
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/italy-vat-PERIOD-working-paper.xlsx
~~~

## Section 8: Italian bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Italian patterns.

**CSV format conventions.** DD/MM/YYYY dates; columns Data, Descrizione/Causale, Dare (debit), Avere (credit), Saldo.

**Italian language variants.** Affitto (rent), stipendio (salary), interessi (interest), bonifico (transfer), contributi (contributions), rimborso (refund), versamento (deposit), prelievo (withdrawal).

**ABI causale codes.** Banks show interbank causale codes on some lines (e.g. 27 for a bank transfer, 48 for a credit card, 05 for a direct debit, 26 for a cheque). Banking-association codes, not a tax source; unchecked here.

**Internal transfers and exclusions.** Giroconto is an internal transfer. Always exclude.

**F24 payments.** Tax payments appear as "PAGAMENTO F24" or with tax codes (6001 to 6012 for monthly IVA, 6031 to 6034 for quarterly IVA). Always exclude. The codes are unchecked; confirm them in the Agenzia's codici tributo list.

**Fattura elettronica (SdI).** B2B and B2C invoices between Italian parties are electronic via the SdI since 2019 (see `italy-einvoice`). Prefer an SdI extract over the bank statement for invoice detail.

**Foreign currency transactions.** Convert to EUR at the ECB rate or bank statement rate.

**IBAN country prefix.** IT is Italy. IE, LU, NL, FR, DE are EU. US, GB, AU, CH are non-EU.

## Section 9: Onboarding fallback (only when inference fails)

### 9.1 Entity type

- SRL, SPA, SAS: company; ditta individuale: sole trader; libero professionista: freelancer. Ask if unclear.

### 9.2 VAT regime

- Filing LIPE implies regime ordinario. Ask: "Regime ordinario or forfettario?"

### 9.3 Partita IVA

- From invoices. Ask: "Your Partita IVA? (IT plus 11 digits)"

### 9.4 Filing period and frequency

- From the statement dates. Ask: "Which period? Monthly or quarterly?"

### 9.5 Industry and sector

- From the counterparty mix. Ask: "What does the business do?"

### 9.6 Employees

- INPS outgoing. Ask: "Do you have employees?"

### 9.7 Exempt supplies

- Medical, financial or educational income. If yes, R-IT-4 refuses.

### 9.8 Credit carried forward

- Always ask: "IVA credit from the previous period (VP8) or last year's return (VP9)?"

### 9.9 Cross-border customers

- Foreign IBANs. Ask: "EU or non-EU? B2B or B2C?"

### 9.10 Public administration customers

- PA-sounding payers. If yes, R-IT-3 (split payment) refuses.

## The method, step by step

1. **Check the regime and frequency.** Regime ordinario only (forfettario limits in the Section 2 table). Monthly by default; quarterly only if last year's volume d'affari met the limits on the [Agenzia's payment page](https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva).
2. **Classify each transaction** with Sections 3, 5 and 6, applying the deduction limits of [art. 19-bis.1 D.P.R. 633/1972](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19bis.1!vig=2026-06-30). Reverse-charge purchases need TD16 to TD19 documents at the SdI (`italy-einvoice`).
3. **Settle the period.** Fill VP2 to VP14 as the [LIPE instructions](https://www.agenziaentrate.gov.it/portale/documents/20143/5986193/IVA+period_2024.pdf/04990f53-edc9-048a-c953-49592ebea05f) define them. Quarterly filers add the interest in VP12 for Q1 to Q3.
4. **Pay by F24 online** on the dates in the Section 1 payment table (same Agenzia page as step 1).
5. **File the LIPE** each quarter by the deadlines in [art. 21-bis D.L. 78/2010](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art21bis!vig=2026-06-30). Correct errors with a replacement LIPE before filing the annual return, or in the annual return after that (LIPE instructions, step 3).
6. **File the annual Dichiarazione IVA** between 1 February and 30 April ([art. 8 D.P.R. 322/1998](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art8!vig=2026-06-30)).

**Penalties**

| Violation | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig=2026-06-30 |
| LIPE omitted, incomplete or wrong (art. 11(2-ter) D.Lgs. 471/1997) | EUR 500 to EUR 2,000; halved if sent or corrected within fifteen days of the deadline | "da euro 500 a euro 2.000" |

| Violation | Penalty | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-06-30 |
| Periodic IVA paid late or short (art. 13(1)) | Twenty-five per cent of the unpaid amount (in words in the law); halved if paid within ninety days; smaller within fifteen days; ravvedimento operoso reduces it further | "pari al venticinque" |

Invoicing penalties (art. 6 D.Lgs. 471/1997) are in `italy-einvoice`.

## Ask the client first

- Are you under the regime ordinario, or forfettario or minimi? (Section 2.)
- Monthly or quarterly settlement, and what was last year's volume d'affari? (Frequency table.)
- Do you make any exempt sales, or sell to public administration (split payment)? Either can take the file out of scope.
- Do you sell to or buy from businesses or consumers in other EU countries or outside the EU?
- Do you use a car for the business, is it your core activity, or are you a commercial agent?
- Do you have IVA credit from the previous period or from last year's annual return?

## When to refuse or refer

- Regime forfettario, regime dei minimi, split payment, pro rata, margin schemes, VAT groups, fiscal representatives (R-IT-1 to R-IT-7).
- EU B2C distance sales above the threshold in Section 5.15 (OSS).
- Domestic reverse charge sectors (art. 17(6)) beyond a single flagged line.
- Adjustments of deduction on capital goods (art. 19-bis2), VAT credit refunds and the annual return itself.
- Penalties, ravvedimento operoso and tax notices.
- Any question on income tax (R-IT-8).

## Section 10: Reference material

### Validation status

v2.1, refreshed in September 2026 against the pages in Sources. No accountant has reviewed it.

### Sources

See Sources at the end. EU law comes via `eu-vat-directive`.

### Known gaps

1. The supplier library does not cover every Italian SME.
2. Split payment and domestic reverse charge are flagged, not computed.
3. The LIPE model and instructions are the Agenzia's 2024 edition, the one its model page links in September 2026.
4. Restaurant IVA depends on who ate and why; the Guide flags but cannot check.
5. F24 tax codes and ABI causale codes are not checked against an official page.

### Change log

- **v2.1 (September 2026):** LIPE rows, quarterly limits, Q2 deadline, transport, entertainment, telephone, toll deductions and B2B EU services corrected.
- **v2.0 (April 2026):** Rewrite to the Malta v2.0 structure.
- **v1.0:** Initial version.

### Self-check (v2.0)

All ten sections present; LIPE rows follow the Agenzia's instructions; vehicle, entertainment, interest and reverse-charge rules are in Sections 4 and 5.

## End of Italy VAT Return Guide v2.1

This Guide is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.

## Sources

- https://www.agenziaentrate.gov.it/portale/web/guest/iva-regole-generali-aliquote-esenzioni-pagamento/norme-generali-e-aliquote
- https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva
- https://www.agenziaentrate.gov.it/portale/documents/20143/5986193/IVA+period_2024.pdf/04990f53-edc9-048a-c953-49592ebea05f
- https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020-
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art21bis!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art8!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19bis.1!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art41!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art102!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2006-07-04;223~art37!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-06-30

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista, revisore legale, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
