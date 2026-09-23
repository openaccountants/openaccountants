---
name: es-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Spanish VAT return (Modelo 303 / IVA autoliquidacion) for a self-employed individual or small business in peninsular Spain or the Balearic Islands. Trigger on phrases like "prepare VAT return", "do the Spanish VAT", "fill in Modelo 303", "IVA", "Modelo 390", or any request involving Spanish VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers peninsular Spain and Balearic Islands only under the regimen general. Canary Islands (IGIC), Ceuta/Melilla (IPSI), regimen simplificado, recargo de equivalencia, RECC cash-basis, VAT groups, and partial exemption (prorrata) are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Spain VAT work.
jurisdiction: ES
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain VAT return: modelo 303 (IVA)

This Guide covers the Spanish VAT self-assessment, modelo 303, for a business taxed under the régimen general in the peninsula and the Balearic Islands. Figures are for tax year 2026. The rates and thresholds come from Ley 37/1992 (LIVA) and its regulation, RD 1624/1992 (RIVA); the box map comes from the modelo 303 approved by Orden HAC/27/2026 and from the Agencia Tributaria's own instructions for the 2026 form. One amount, the investment-goods limit, is printed as a figure only in the Agencia Tributaria's practical VAT manual for the 2025 return, which is the current version of that page; the table that carries it says so. This Guide stands alone: the companion Guides named below add workflow and EU directive detail, but a modelo 303 can be worked from this Guide by itself.

## Spain VAT Return Guide (Modelo 303 / IVA) v2.0

## Section 1: Quick reference

Read this section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1: follow it where you have it, with this Guide supplying the country content and `eu-vat-directive` the EU directive content.

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Spain: peninsula and Balearic Islands |
| Rates | See the rate table below |
| Return form | Modelo 303 (periodic self-assessment); modelo 390 (annual summary) |
| Filing portal | Sede electrónica of the Agencia Tributaria |
| Authority | Agencia Estatal de Administración Tributaria (AEAT) |
| Currency | Euro only |
| Filing frequency | Calendar quarter by default, calendar month in the cases in the deadline table |
| SII obligation | Invoice records supplied through the Sede electrónica (art. 62.6 and art. 69 bis RIVA), compulsory for every monthly filer |
| Companion Guides | `vat-workflow-base` and `eu-vat-directive`, both optional |
| Contributor | OpenAccountants library |
| Checked against the official pages | September 2026 |

**Rates and surcharges**

| Item | Rate | Note (the page's own words) |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Standard rate, tipo general (art. 90.Uno LIVA) | 21% | "El Impuesto se exigirá al tipo del 21 por ciento" |
| Reduced rate, tipo reducido (art. 91.Uno LIVA) | 10% | "Se aplicará el tipo del 10 por ciento a las operaciones siguientes" |
| Super-reduced rate (art. 91.Dos LIVA) | 4% | "Se aplicará el tipo del 4 por ciento a las operaciones siguientes" |
| Recargo de equivalencia, standard-rated goods (art. 161.1 LIVA) | 5.2% | "Con carácter general, el 5,2 por ciento" |
| Recargo de equivalencia, reduced-rated goods (art. 161.2 LIVA) | 1.4% | "el 1,4 por ciento" |
| Recargo de equivalencia, super-reduced goods (art. 161.3 LIVA) | 0.5% | "el 0,50 por ciento" |
| Recargo de equivalencia, tobacco (art. 161.4 LIVA) | 1.75% | "Para las entregas de bienes objeto del Impuesto Especial sobre las Labores del Tabaco, el 1,75 por ciento" |
| Flat compensation, farming and fishing scheme (art. 130.Cinco.1 LIVA) | 12% | "El 12 por 100, en las entregas de productos naturales obtenidos en explotaciones agrícolas o forestales" |

No temporary rate is in force for 2026. The rate is the one in force at the tax point (devengo), not at invoicing.

**Filing periods and deadlines**

| Rule | What it says | Provision |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925 |
| Default period | The calendar quarter | art. 71.3 RIVA |
| Monthly period | Turnover of the previous calendar year above EUR 6,010,121.04; a buyer of a business whose combined turnover passed it; anyone in the registro de devolución mensual; holders of fuel tax warehouses and anyone extracting those products from one. A VAT group also files monthly but on modelo 322 and 353, not this form | art. 71.3 and art. 30 RIVA |
| Quarterly deadline | The first twenty calendar days of the month after the quarter | art. 71.4 RIVA |
| Last period of the year | The first thirty calendar days of January | art. 71.4 RIVA |
| Monthly deadline | The first thirty calendar days of the month after the period, and until the last day of February for the January period | art. 71.4 RIVA |
| SII supply deadline, invoices issued | Four calendar days from issue, eight where the customer or a third party issues it, and in both cases before the 16th of the month after the tax point. Saturdays, Sundays and national holidays do not count in the four or eight days | art. 69 bis RIVA |
| SII supply deadline, invoices received | Four calendar days from the accounting entry, and before the 16th of the month after the filing period the invoice is included in. Saturdays, Sundays and national holidays do not count | art. 69 bis RIVA |
| Modelo 349, general rule | Monthly, in the first twenty calendar days of the next month; July may go in August and in the first twenty calendar days of September | art. 81.2.1 RIVA |
| Modelo 349, last period of the year | The first thirty calendar days of January, monthly and quarterly filers alike | art. 81.3 RIVA |
| Modelo 349, quarterly | Only where intra-EU supplies of goods and services were not above EUR 50,000 excluding VAT in the quarter and in each of the four preceding quarters | art. 81.2.2 RIVA |
| Source | modelo 390 deadline | https://www.boe.es/buscar/act.php?id=BOE-A-2009-18472 |
| Modelo 390 | The first thirty calendar days of January following the year of the return | art. 8, Orden EHA/3111/2009 |

These are filing deadlines. Direct debit of the payment closes earlier than the last filing day, and the Sede electrónica states that window for each period.

**Key Modelo 303 casillas (boxes)**

The boxes below are the ones printed on the modelo 303 approved by Orden HAC/27/2026 (Boletín Oficial del Estado of 26 January 2026): page 1 for the régimen general, page 3 for the result. Box numbers in older versions of this Guide, and in most commercial summaries, do not match the form.

**IVA devengado (output side, page 1)**

| Boxes | What goes in them |
| --- | --- |
| Source | box numbers and labels below | https://www.boe.es/boe/dias/2026/01/26/pdfs/BOE-A-2026-1761.pdf |
| 150, 151, 152 | Régimen general, zero-rate row: base, rate, quota |
| 01, 02, 03 | Régimen general, super-reduced row |
| 04, 05, 06 | Régimen general, reduced row |
| 07, 08, 09 | Régimen general, standard row |
| 165 to 167, 153 to 155 | Two further régimen general rate rows; the 2026 instructions assign no rate to either |
| 10, 11 | Adquisiciones intracomunitarias de bienes y servicios: base and quota, goods and services together |
| 12, 13 | Otras operaciones con inversión del sujeto pasivo (art. 84.Uno.2 and 4 LIVA) not belonging in boxes 10 and 11 |
| 14, 15 | Modificación de bases y cuotas |
| 156, 157, 158 | Recargo de equivalencia, tobacco row: base, rate, quota |
| 168, 169, 170 | Recargo, super-reduced row |
| 19, 20, 21 | Recargo, reduced row |
| 22, 23, 24 | Recargo, standard row |
| 16, 17, 18 | A further recargo row; the 2026 instructions assign no rate to it |
| 25, 26 | Modificación de bases y cuotas del recargo de equivalencia |
| 27 | Total cuota devengada (152 + 167 + 03 + 155 + 06 + 09 + 11 + 13 + 15 + 158 + 170 + 18 + 21 + 24 + 26) |
| Source | rate to row mapping above | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html |

**IVA deducible (input side, page 1)**

| Boxes | What goes in them |
| --- | --- |
| Source | box numbers and labels below | https://www.boe.es/boe/dias/2026/01/26/pdfs/BOE-A-2026-1761.pdf |
| 28, 29 | Operaciones interiores corrientes: base and quota |
| 30, 31 | Operaciones interiores con bienes de inversión |
| 32, 33 | Importaciones de bienes corrientes |
| 34, 35 | Importaciones de bienes de inversión |
| 36, 37 | Adquisiciones intracomunitarias de bienes y servicios corrientes |
| 38, 39 | Adquisiciones intracomunitarias de bienes de inversión |
| 40, 41 | Rectificación de deducciones |
| 42 | Compensaciones del régimen especial de la agricultura, ganadería y pesca |
| 43 | Regularización de bienes de inversión |
| 44 | Regularización por el porcentaje definitivo de prorrata (last period of the year, or on ceasing) |
| 45 | Total a deducir (29 + 31 + 33 + 35 + 37 + 39 + 41 + 42 + 43 + 44) |
| 46 | Resultado régimen general (27 - 45) |

Read those six input rows as a decision: an intra-EU acquisition goes in 36 and 37, goods cleared through customs in 32 and 33, and anything else, including a supply located in Spain from a supplier not established here, is an operación interior and goes in 28 and 29. Within each pair, the split is whether the purchase is an investment good, defined in Section 5.10.

The 2026 instructions say only that boxes 28 to 39 hold the deductible base and quota, split between current operations and investment goods. They do not name the row for a reverse charge that is neither an intra-EU acquisition nor an import. This Guide reads it off the three row labels on the form. An accountant should confirm it before relying on it.

**Régimen simplificado, additional information and result (pages 2 and 3)**

| Boxes | What goes in them |
| --- | --- |
| Source | box numbers and labels below | https://www.boe.es/boe/dias/2026/01/26/pdfs/BOE-A-2026-1761.pdf |
| 47 to 58 | Régimen simplificado, the module computation, ending in Resultado régimen simplificado (54 - 57) in box 58. Not covered here, see R-ES-3 |
| 59 | Entregas intracomunitarias de bienes y servicios, exempt |
| 60 | Exportaciones y operaciones asimiladas |
| 120, 122 | Operations not subject by place-of-supply rules; operations subject with reverse charge, reported by the supplier |
| 123, 124 | Operations under the one-stop-shop schemes |
| 62, 63 | Cash-scheme supplies, base and quota, as if the general tax-point rule applied. Only a cash-scheme filer completes them |
| 74, 75 | Purchases affected by the cash scheme, base and input quota, as if the general tax-point rule applied. Completed by any filer who receives invoices from a cash-scheme supplier, not only by cash-scheme filers |
| 76 | Regularización de cuotas art. 80.Cinco.5ª LIVA |
| 64 | Suma de resultados (46 + 58 + 76) |
| 65 | Percentage of the volume of operations in territorio común. The instructions say every taxpayer that does not also file with a foral administration writes 100% here |
| 66 | Atribuible a la Administración del Estado. It equals box 64 unless the taxpayer also files with a foral administration, in which case 66 = 64 x 65 |
| 77 | Import VAT assessed by customs and deferred under art. 74.1 RIVA |
| 110, 78, 87 | Credit from earlier periods: pending, applied now, and left over (110 - 78) |
| 68, 108 | Annual foral regularisation; rectificative return on a difference of administrative criterion |
| 69 | Resultado de la autoliquidación (66 + 77 - 78 + 68 + 108) |
| 70, 109 | Rectificative returns only: the earlier return's result, and refunds already agreed for the period |
| 112 | Payment on account for fuels leaving a depósito distinto del aduanero |
| 71 | Resultado (69 - 70 + 109 - 112) |
| Source | box 65 percentage above | https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html |

Box 71 decides the declaration type: a ingresar where it is positive and the payment is made; con solicitud de devolución where it is negative and a refund is asked for; a compensar where it is negative and no refund is asked for; resultado cero; and sin actividad where no VAT was charged or borne. A refund asked for in a period that is not the last of the year can only be processed if the filer is in the registro de devolución mensual (art. 30 RIVA).

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Standard rate |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Spain |
| Unknown business or consumer status for an EU customer | Consumer, charge the standard rate |
| Unknown business-use share (phone, home office) | No recovery |
| Unknown business use of a passenger vehicle | The statutory presumption in Section 5.11 |
| Unknown supplier billing entity for a service | Reverse charge, output in 12 and 13, input in 28 and 29 |
| Unknown blocked-input status (client entertainment, personal use) | Blocked |
| Unknown whether a transaction is in scope | In scope |

**Red flag thresholds**

The amounts this table once carried were the Guide's own working thresholds. No official page prints them, so they are gone: judge each flag against the size of the return in front of you.

| Flag | Test |
| --- | --- |
| HIGH | A single transaction large enough to change the result of the return on its own |
| HIGH | A conservative default whose tax effect is large next to the period's net VAT |
| MEDIUM | One counterparty making up a large share of output or of input |
| MEDIUM | Several conservative defaults across one return |
| LOW | A net VAT position that is small next to the client's usual periods |

## Section 2: Required inputs and refusal catalogue

### Required inputs

**Minimum viable.** Bank statement for the period in CSV, PDF, or pasted text. It must cover the full period. Any Spanish or international business bank is acceptable: CaixaBank, Santander, BBVA, Bankinter, Sabadell, ING Direct, Revolut Business, Wise Business, N26 Business, or another.

**Recommended.** Sales invoices for the period (above all for intra-EU business-to-business services and exempt supplies), and purchase invoices (facturas) for input VAT claims. A simplified invoice (factura simplificada) may be issued up to the amount in the invoice table below, but it only supports a deduction if it identifies the recipient and shows the VAT quota separately. Get the client's NIF-IVA in writing.

**Invoice limits (RD 1619/2012, Reglamento de facturación)**

| Item | Limit, VAT included | Provision |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696 |
| Simplified invoice, general | EUR 400 | art. 4.1 |
| Simplified invoice, listed retail and consumer sectors (retail sales, home sales, passenger transport, hospitality, hairdressing, dry cleaning and the rest of the list) | EUR 3,000 | art. 4.2 |

Only the holder of the invoice or of the customs document may deduct (art. 97 LIVA). The deduction may be taken in the period in which the quota was borne or in a later one, provided four years have not passed since the right arose (art. 99.Tres LIVA).

**Ideal.** The complete invoice registers (libro registro de facturas expedidas y recibidas), the previous modelo 303 showing the credit carried forward in boxes 110 and 78, and the SII submission confirmations.

**Refusal policy if the minimum is missing: soft warn.** If no bank statement is available at all, hard stop. If there is a bank statement but no invoices, proceed but record in the reviewer brief: "This modelo 303 was produced from a bank statement alone. The reviewer must verify, before approval, that input VAT claims are supported by compliant facturas, including recipient identification and a separate VAT quota on any factura simplificada, and that every reverse-charge classification matches the supplier's invoice."

### Spain-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation.

- **R-ES-1, Canary Islands (IGIC).** Trigger: the client is in the Canary Islands or asks about IGIC. Message: "The Canary Islands use IGIC (Impuesto General Indirecto Canario), not IVA. This Guide covers IVA only, that is peninsular Spain and the Balearic Islands. Please use an Asesor Fiscal familiar with IGIC."
- **R-ES-2, Ceuta or Melilla (IPSI).** Trigger: the client is in Ceuta or Melilla or asks about IPSI. Message: "Ceuta and Melilla use IPSI (Impuesto sobre la Producción, los Servicios y la Importación), not IVA. Out of scope for this Guide."
- **R-ES-3, régimen simplificado (modules).** Trigger: the client files under the régimen simplificado, boxes 47 to 58 of the form. Message: "The régimen simplificado computes VAT from activity modules, not from transaction classification. This Guide covers the régimen general only. Please use an Asesor Fiscal for module-based returns."
- **R-ES-4, recargo de equivalencia.** Trigger: the client is a retailer inside the recargo de equivalencia scheme. Message: "Recargo de equivalencia is a scheme for retailers who are individuals or entities in the IRPF attribution regime and who sell goods without transforming them (art. 148 and 149 LIVA). Their suppliers charge the surcharge in the rate table on top of VAT, and the retailer does not self-assess or deduct VAT on those retail sales (art. 154.Dos LIVA). Note that the retailer must still self-assess intra-EU acquisitions and operations with reverse charge under art. 84.Uno.2 LIVA (art. 154.Uno LIVA). This Guide covers the régimen general only."
- **R-ES-5, RECC cash-basis scheme.** Trigger: the client uses the régimen especial del criterio de caja. Message: "The RECC scheme moves the tax point to the payment date for both output and input VAT, with 31 December of the following year as the backstop, and it has its own boxes 62, 63, 74 and 75. If your client is not in the scheme but buys from a supplier who is, do not refuse: boxes 74 and 75 still have to be completed for those purchases. This Guide assumes the general accrual tax point (devengo). Please use an Asesor Fiscal for RECC returns."
- **R-ES-6, prorrata (partial exemption).** Trigger: the client makes both taxable and exempt supplies (art. 20 LIVA) and the exempt part is not trivial. Message: "Your business makes both taxable and exempt supplies. Input VAT must be apportioned under the prorrata rules (art. 102 to 106 LIVA), and the definitive annual percentage is settled in box 44 of the last return of the year. Please use an Asesor Fiscal to determine the prorrata percentage before input VAT is claimed."
- **R-ES-7, VAT groups (grupos de entidades).** Trigger: the client is in a VAT group under art. 163 quinquies to nonies LIVA. Message: "VAT group consolidation is out of scope, and a group files modelo 322 and modelo 353, not this form. Please use an Asesor Fiscal."
- **R-ES-8, margin schemes.** Trigger: the client deals in second-hand goods, travel agency packages, or art and antiques under a margin scheme. Message: "Margin scheme regimes (bienes usados, agencias de viajes, objetos de arte) need a transaction-level margin computation. Out of scope."

## Section 3: Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. Where a counterparty matches a pattern here, apply the treatment directly and do not consult the Tier 1 rules. Match by case-insensitive substring on the name as it appears in the bank statement; where several patterns match, use the most specific; where none match, fall through to Section 5.

Box shorthand used in the tables: **interior** means boxes 28 and 29 on the input side; **EU-RC** means an intra-EU acquisition, output in boxes 10 and 11 and input in boxes 36 and 37; **RC** means any other reverse charge, output in boxes 12 and 13 and input in boxes 28 and 29. Sales at the standard rate go to boxes 07, 08 and 09.

### 3.1 Spanish banks (fees exempt, exclude)

**Spanish banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CAIXABANK, LA CAIXA, SANTANDER, BBVA, BANCO BILBAO, BANKINTER, SABADELL, ING DIRECT, ING BANK, UNICAJA, KUTXABANK, IBERCAJA, ABANCA | EXCLUDE bank charges and fees | Art. 20.Uno.18 LIVA: financial service, exempt |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE transaction and maintenance fees | Check for a separate taxable subscription invoice |
| INTERESES, INTEREST | EXCLUDE | Interest income or expense, exempt |
| PRESTAMO, HIPOTECA, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Spanish government, regulators, and statutory bodies (exclude entirely)

**Government bodies table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AEAT, AGENCIA TRIBUTARIA, HACIENDA, IMPUESTO, IAE, IBI | EXCLUDE | Tax payment, not a supply |
| TGSS, TESORERIA GENERAL DE LA SEGURIDAD SOCIAL, SEGURIDAD SOCIAL, SEG. SOCIAL | EXCLUDE | Social security contribution |
| IRPF, RETENCION | EXCLUDE | Income tax withholding payment |
| AYUNTAMIENTO, REGISTRO MERCANTIL, TRAFICO, DGT | EXCLUDE | Municipal charge, registry fee, vehicle fines: sovereign acts |

### 3.3 Spanish utilities

**Utilities table**

| Pattern | Treatment | Casilla | Notes |
| --- | --- | --- | --- |
| IBERDROLA, ENDESA, NATURGY, GAS NATURAL, REPSOL (energy bills) | Domestic, standard rate | interior | Electricity, gas and heating, overhead |
| TELEFONICA, MOVISTAR, VODAFONE SPAIN, VODAFONE ES, ORANGE, MASMOVIL, YOIGO, DIGI | Domestic, standard rate | interior | Telecoms, overhead |
| AGUA, CANAL DE ISABEL II, AGUAS | Domestic, reduced rate | interior | Water supply, art. 91.Uno LIVA |

### 3.4 Insurance (exempt, exclude)

**Insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MAPFRE, MUTUA MADRILENA, MUTUALIA, AXA SEGUROS, ALLIANZ, ZURICH, GENERALI, SANTALUCIA, PELAYO | EXCLUDE | Insurance, exempt, art. 20.Uno.16 LIVA |
| SEGURO, POLIZA, PRIMA | EXCLUDE | Insurance premium, exempt |

### 3.5 Post and logistics

**Post and logistics table**

| Pattern | Treatment | Casilla | Notes |
| --- | --- | --- | --- |
| CORREOS, SOCIEDAD ESTATAL CORREOS | EXCLUDE standard postage |  | Universal postal service, exempt |
| CORREOS EXPRESS, SEUR, MRW, NACEX, GLS SPAIN, DHL EXPRESS SPAIN | Domestic, standard rate | interior | Courier and express services are taxable |
| DHL INTERNATIONAL | EU-RC if billed from another member state | EU-RC | Check the invoice for the billing entity |

### 3.6 Transport

**Transport table**

| Pattern | Treatment | Casilla | Notes |
| --- | --- | --- | --- |
| RENFE, METRO, EMT, TMB, TUSSAM | Domestic, reduced rate | interior | Rail and urban passenger transport, art. 91.Uno LIVA |
| CABIFY, UBER SPAIN | Domestic, standard rate | interior | Ride-hailing |
| IBERIA, VUELING, AIR EUROPA (international) | Exempt, exclude |  | International passenger flights, art. 22 LIVA |
| IBERIA, VUELING (domestic) | Domestic, reduced rate | interior | Domestic passenger flights, art. 91.Uno LIVA |
| BLABLACAR | EXCLUDE |  | Cost sharing between individuals, no taxable supply |

### 3.7 Food retail (blocked unless hospitality business)

**Food retail table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MERCADONA, DIA, LIDL, ALDI, CARREFOUR, EL CORTE INGLES (food hall), SUPERMERCADO, ALIMENTACION | Default BLOCK input VAT | Food, drink and tobacco are excluded by art. 96.Uno.3 LIVA unless art. 96.Dos applies, for example a hospitality business reselling them |
| RESTAURANTS, CAFES, BARS (any named) | Default BLOCK | Art. 96.Uno.6 LIVA, see Section 5.12 |

### 3.8 SaaS from EU suppliers (reverse charge, boxes 10 and 11)

A service from a taxable person in another member state is an intra-EU acquisition of services: the customer self-assesses under art. 84.Uno.2 LIVA, and the form puts intra-EU goods and services in the same pair of boxes.

**SaaS EU suppliers table**

| Pattern | Billing entity | Casilla |
| --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | EU-RC |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | EU-RC |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | EU-RC |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | EU-RC |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | EU-RC |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | EU-RC |
| DROPBOX | Dropbox International Unlimited (IE) | EU-RC |
| SLACK | Slack Technologies Ireland Ltd (IE) | EU-RC |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | EU-RC |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | EU-RC |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | EU-RC, transaction fees may be exempt, see 3.11 |
| AWS (standard) | AWS EMEA SARL (LU) | EU-RC, Luxembourg entity, check the invoice; if it shows Spanish IVA treat it as a domestic purchase |

### 3.9 SaaS from non-EU suppliers (reverse charge, boxes 12 and 13)

**SaaS non-EU suppliers table**

| Pattern | Billing entity | Casilla |
| --- | --- | --- |
| NOTION | Notion Labs Inc (US) | RC |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | RC |
| OPENAI, CHATGPT | OpenAI Inc (US) | RC |
| GITHUB (standard plans) | GitHub Inc (US), check for an Irish entity | RC |
| FIGMA | Figma Inc (US) | RC |
| CANVA | Canva Pty Ltd (AU) | RC |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE), check the invoice | RC, or EU-RC |
| TWILIO | Twilio Inc (US) | RC |

### 3.10 SaaS, the exception (not reverse charge)

**SaaS exception table**

| Pattern | Treatment | Why |
| --- | --- | --- |
| AMAZON ES, AMAZON.ES (marketplace) | Domestic, standard rate, interior | Amazon Spain retail, a domestic supply with IVA on the invoice |

### 3.11 Payment processors

**Payment processors table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees), PAYPAL (transaction fees), REDSYS, SERVIRED | EXCLUDE (exempt) | Payment and card processing, exempt financial services |
| STRIPE (monthly subscription) | EU-RC | Irish entity, separate from the transaction fees |
| SUMUP, SQUARE, ZETTLE | Check the invoice | Spanish entity: domestic, standard rate. Entity in another member state: EU-RC |

### 3.12 Professional services (Spain)

**Professional services table**

| Pattern | Treatment | Casilla | Notes |
| --- | --- | --- | --- |
| NOTARIO, NOTARIA, ASESOR, ASESORIA, GESTORIA, ABOGADO, BUFETE, DESPACHO, COLEGIO PROFESIONAL | Domestic, standard rate | interior | Deductible where there is a business purpose |
| REGISTRO MERCANTIL | EXCLUDE |  | Government registry fee |

### 3.13 Payroll and social security (exclude entirely)

**Payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NOMINA, SALARIO, SUELDO | EXCLUDE | Wages, outside the scope of VAT |
| TGSS, SEGURIDAD SOCIAL, AUTONOMO, RETA, CUOTA AUTONOMO | EXCLUDE | Statutory social security payments |
| IRPF, RETENCION, MODELO 111, MODELO 190 | EXCLUDE | IRPF withholding payment |

### 3.14 Property and rent

**Property and rent table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALQUILER, RENTA (commercial, with IVA) | Domestic, standard rate, interior | Commercial lease where the landlord charges IVA |
| ALQUILER, RENTA (residential, no IVA) | EXCLUDE | Residential lease, exempt, art. 20.Uno.23 LIVA |
| COMUNIDAD DE PROPIETARIOS | EXCLUDE | Building community charges |
| HIPOTECA | EXCLUDE | Mortgage payment, financial service |

### 3.15 Internal transfers and exclusions

**Internal transfers table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRASPASO, TRANSFERENCIA PROPIA | EXCLUDE | Internal movement |
| DIVIDENDO, AMORTIZACION PRESTAMO | EXCLUDE | Dividend and loan repayment, out of scope |
| REINTEGRO, CAJERO, ATM | TIER 2, ask | Default exclude, ask what the cash was spent on |
| BIZUM (personal) | EXCLUDE | Personal transfers through Bizum |

## Section 4: Worked examples

Six worked classifications from a made-up bank statement of a Spain-based self-employed software consultant (autónomo). The amounts are illustrative, not figures from an official page.

### Example 1: Non-EU SaaS reverse charge (Notion)

03.04.2026 ; NOTION LABS INC ; CARGO ; monthly subscription ; 14.68 euros

Notion Labs Inc is a US entity (Section 3.9) and there is no IVA on the invoice. A service from a supplier not established in the Union makes the customer the taxable person under art. 84.Uno.2 LIVA. It is not an intra-EU acquisition, so output goes in boxes 12 and 13 and input in boxes 28 and 29 as an operación interior. Net effect zero for a fully taxable business.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Boxes (input) | Boxes (output) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.08 | standard | 28 and 29 | 12 and 13 | N | none | none |

### Example 2: EU service, reverse charge (Google Ads)

10.04.2026 ; GOOGLE IRELAND LIMITED ; CARGO ; Google Ads abril 2026 ; -850.00

Google Ireland Limited is established in another member state, so this is an intra-EU acquisition of services: output in boxes 10 and 11, input in boxes 36 and 37, net cash effect zero. It is reported on modelo 349 as an intra-EU acquisition of services, because art. 79.1.4 RIVA puts on the recapitulative declaration the services supplied from elsewhere in the Union on which the Spanish customer is the taxable person.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Boxes (input) | Boxes (output) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 178.50 | standard | 36 and 37 | 10 and 11 | N | none | none |

### Example 3: Entertainment, no deduction right

15.04.2026 ; RESTAURANTE BOTIN MADRID ; CARGO ; cena de negocios ; -180.00

Art. 96.Uno.6 LIVA excludes travel, hotel and restaurant services from deduction unless the amount is a deductible expense for income tax or corporate tax. Art. 96.Uno.5 separately excludes, in any proportion, anything meant as hospitality for clients, employees or third parties, with only the two exceptions in its own letters a and b. Default: block, and flag it, because the reviewer must settle the income-tax deductibility first.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Boxes | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | RESTAURANTE BOTIN | -180.00 | -180.00 | 0 | none | none | Y | Q1 | "Client entertainment: blocked, conservative" |

### Example 4: Investment goods (bienes de inversion)

18.04.2026 ; APPLE STORE PASEO DE GRACIA ; CARGO ; MacBook Pro 16 ; -2,999.00

Gross 2,999 euros, net 2,478.51 euros. A good is an investment good when it is normally meant to be used for more than a year as an instrument of work, and it is not one when its value is below the limit in Section 5.10. Both readings here are below that limit, so the purchase goes to boxes 28 and 29, not to boxes 30 and 31. If accessories on the same invoice push the value over, reclassify. The official page says "valor" without saying whether VAT is included, so where the two readings differ, ask the reviewer.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Boxes | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | APPLE STORE | -2,999.00 | -2,478.51 | -520.49 | standard | 28 and 29 | N | none | none |

### Example 5: EU B2B service sale (inbound receipt)

22.04.2026 ; KREBS CONSULTING GMBH ; ABONO ; factura ES-2026-018 consultoria IT marzo ; +4,200.00

An incoming 4,200 euros from a German company for IT consulting. For services to a business customer the place of supply is the customer's country (art. 69.Uno.1 LIVA), so nothing is taxed in Spain and nothing goes in the output rate rows. The client invoices with no Spanish IVA and a note that the customer self-assesses. The amount goes in box 59 and on modelo 349. Confirm the customer's German VAT number is valid and that the invoice shows no Spanish IVA.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Boxes | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22.04.2026 | KREBS CONSULTING GMBH | +4,200.00 | +4,200.00 | 0 | exempt | 59 and modelo 349 | Y | Q2 (HIGH) | "Verify the German VAT number" |

### Example 6: Vehicle costs, 50% presumption

28.04.2026 ; REPSOL ESTACION DE SERVICIO ; CARGO ; gasoleo A ; -85.00

Art. 95.Tres.2 LIVA presumes a passenger car, trailer, moped or motorcycle is used in the business in the proportion in Section 5.11, and art. 95.Cuatro extends that proportion to fuel, spare parts and running costs. The presumption can be displaced either way on evidence. Default: apply the statutory proportion.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Boxes | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28.04.2026 | REPSOL | -85.00 | -70.25 | -7.38 | standard, half recovered | 28 and 29 | Y | Q3 | "Vehicle fuel: statutory presumption applied" |

## Section 5: Tier 1 classification rules (compressed)

Each rule gives the legal source and the box mapping. Apply it silently where the data is unambiguous. The rates are in the rate table in Section 1.

### 5.1 Standard rate 21% (Art. 90 LIVA)

- **Standard rate default.** The default for any taxable supply unless a reduced rate, an exemption or a reverse charge applies. Sales go to boxes 07, 08 and 09; purchases to boxes 28 and 29. _(Art. 90 LIVA)_

### 5.2 Reduced rate 10% (Art. 91.Uno LIVA)

- **Reduced rate.** Art. 91.Uno LIVA lists it: food and drink outside the super-reduced list, water, passenger transport, hotels, restaurant and catering, the first transfer of new housing, qualifying home renovation, certain medical equipment. Sales go to boxes 04, 05 and 06; purchases to boxes 28 and 29, which are not split by rate. _(Art. 91.Uno LIVA)_

### 5.3 Super-reduced rate 4% (Art. 91.Dos LIVA)

- **Super-reduced rate.** Art. 91.Dos LIVA lists it: plain bread and bread dough, bread flour, milk, cheese, eggs, natural fruit, vegetables, pulses, tubers and cereals, olive oil, books, newspapers and magazines, medicines for human use, certain disability aids and social housing. Olive oil has been in this list since 1 January 2025. Sales go to boxes 01, 02 and 03; purchases to boxes 28 and 29. _(Art. 91.Dos LIVA)_

### 5.4 Zero rate and exempt with credit

- **Exports and intra-EU supplies.** Exports outside the Union are exempt with a right of deduction (art. 21 LIVA) and go in box 60, together with sendings to the Canary Islands, Ceuta and Melilla. Intra-EU supplies of goods (art. 25 LIVA) and intra-EU services to a business customer (art. 69 LIVA) go in box 59 and on modelo 349. The form's zero-rate row (boxes 150, 151 and 152) is a different thing from these exemptions. _(Art. 21, 25 and 69 LIVA)_

### 5.5 Exempt without credit (Art. 20 LIVA)

- **Exempt without credit.** Medical services, education, insurance, financial services, the universal postal service, residential letting, social welfare. No output VAT and no deduction of the input VAT behind them. If they are more than trivial, R-ES-6 fires. _(Art. 20 LIVA)_

### 5.6 Local standard purchases

- **Local purchases.** Input VAT on a compliant factura from a Spanish supplier is deductible where the purchase is used in the taxable activity, subject to 5.12 and to the investment-goods split in 5.10. Boxes 28 and 29, or 30 and 31. Only the holder of the invoice may deduct (art. 97 LIVA), and the deduction must be taken within four years of the right arising (art. 99.Tres LIVA).

### 5.7 Reverse charge: intra-EU services received (Art. 84.Uno.2 LIVA)

- **EU services.** A service from a supplier established in another member state, invoiced without VAT and with a reverse-charge note, is an intra-EU acquisition of services: output in boxes 10 and 11, input in boxes 36 and 37, net effect zero. The form puts intra-EU goods and services in the same pair. If the supplier charged its own national VAT, that is not a reverse charge: it is foreign VAT, not deductible here, and only the cross-border refund procedure recovers it. _(Art. 84.Uno.2 LIVA)_

### 5.8 Reverse charge: intra-EU goods received (Art. 13 LIVA)

- **EU goods.** An intra-EU acquisition of goods: output in boxes 10 and 11, input in boxes 36 and 37, or 38 and 39 for investment goods. _(Art. 13 LIVA)_

### 5.9 Reverse charge: non-EU services and imports

- **Non-EU services and imports.** A service from a supplier outside the Union is still a reverse charge under art. 84.Uno.2 LIVA but not an intra-EU acquisition: output in boxes 12 and 13, input in boxes 28 and 29 as an operación interior. Imported goods are different: import VAT is assessed by customs on the DUA and deducted in boxes 32 and 33, or 34 and 35 for investment goods. A monthly filer who elected the deferral by census declaration in the November before the year may declare the customs-assessed import VAT in box 77 instead of paying it at the border (art. 74.1 RIVA). Without that election box 77 stays empty. _(Art. 84.Uno.2 LIVA)_

### 5.10 Investment goods: bienes de inversion (Art. 108 to 110 LIVA)

- **Bienes de inversión.** A tangible good normally meant to be used for more than a year as an instrument of work (art. 108.Uno LIVA). Art. 108.Dos excludes spare parts, repair work, packaging, work clothing, and any good whose acquisition value is below the amount below. They go in boxes 30 and 31 (domestic), 34 and 35 (imports) or 38 and 39 (intra-EU). The deduction is regularised over the four calendar years after acquisition, or the nine years after it for land and buildings, and only where a year's definitive percentage differs from the original by more than ten points (art. 107 LIVA).

**Investment goods limit**

| Item | Amount | Note (the page's own words) |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2025/capitulo-05-deducciones-devoluciones/deducciones/regularizacion-deducciones-bienes-inversion/concepto-bienes-inversion.html |
| Value below which a good is not an investment good (art. 108.Dos.5 LIVA) | EUR 3,005.06 | "Cualquier otro bien de valor inferior a 3.005,06 euros" |

The law still writes this limit in pesetas, so the euro figure comes from the Agencia Tributaria manual page for the 2025 return, the current version of that page.

### 5.11 Vehicle deduction: 50% presumption (Art. 95.Tres.2 LIVA)

- **Vehicles.** Passenger cars and their trailers, mopeds and motorcycles are presumed used in the business in the proportion below, and the same proportion carries to their fuel, spare parts, servicing, parking and tolls (art. 95.Cuatro LIVA). Six uses carry the full proportion: mixed vehicles carrying goods, carrying passengers for payment, driving and flying schools, manufacturers' tests and demonstrations, commercial travellers and agents, and security services. The figure must be corrected later if real use differs, and the taxpayer proves use by any means admitted in law: the return itself and the accounting entry are not enough (art. 95.Tres.3 and 4 LIVA).

**Vehicle presumption**

| Case | Presumed business use | Note (the page's own words) |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Passenger cars, trailers, mopeds and motorcycles | 50% | "se presumirán afectados al desarrollo de la actividad empresarial o profesional en la proporción del 50 por 100" |
| The six listed uses | 100% | "los vehículos que se relacionan a continuación se presumirán afectados al desarrollo de la actividad empresarial o profesional en la proporción del 100 por 100" |

### 5.12 Restricted input VAT (Art. 96 LIVA)

- **Excluded categories.** Art. 96.Uno LIVA excludes from deduction in any proportion, with their accessories: jewellery and objects of gold or platinum (96.Uno.1); food, drink and tobacco (96.Uno.3); shows and recreational services (96.Uno.4); goods and services meant as hospitality for clients, employees or third parties (96.Uno.5); and travel, hotel and restaurant services unless the amount is deductible for income tax or corporate tax (96.Uno.6). Number 2 of the list was repealed. Art. 96.Dos puts back goods of exclusively industrial, commercial, agricultural, clinical or scientific use, and goods and services bought for resale by a business that does that for a living. Free samples and low-value advertising objects are not hospitality, but art. 7.4 LIVA stops treating an advertising object as low-value once the total to one recipient in a calendar year passes the amount below.

**Advertising objects**

| Item | Amount | Note (the page's own words) |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Total to one recipient in a calendar year, above which the free-supply treatment stops (art. 7.4 LIVA) | EUR 200 | "objetos publicitarios cuando el coste total de los suministros a un mismo destinatario durante el año natural exceda de 200 euros" |

### 5.13 SII: Suministro Inmediato de Informacion (RD 596/2016)

- **SII.** Anyone whose period is the calendar month must keep the VAT registers through the Sede electrónica by supplying the invoice records electronically (art. 62.6 RIVA); anyone else may opt in (art. 68 bis RIVA). The supply deadlines are in the deadline table in Section 1. Where the client is inside the SII, note in the reviewer brief that the return must agree with the records supplied, because the Agencia Tributaria builds its draft from them.

### 5.14 Modelo 390: annual summary

- **Modelo 390.** An annual informative return summarising the year's modelo 303 filings; its deadline is in the deadline table in Section 1. The 2026 instructions exonerate two groups: quarterly filers taxed only in territorio común whose only activities are the simplified regime or letting urban property, and anyone keeping the registers through the Sede electrónica. Both instead complete the extra data block on page 4 of the last modelo 303 of the year. Neither exoneration applies where there is no duty to file that last return.

### 5.15 Modelo 349: recapitulative declaration

- **Modelo 349.** Declares intra-EU supplies of goods, intra-EU services supplied and intra-EU acquisitions. Monthly as a general rule, quarterly only under the test in the deadline table in Section 1. It must agree with boxes 10, 11 and 59 of the modelo 303 filings for the same period.

## Section 6: Tier 2 catalogue (compressed)

For each ambiguity: the pattern, why the bank statement is not enough, the conservative default, and the question to ask.

### 6.1 Fuel and vehicle costs

Repsol, Cepsa, BP, Shell, Galp, fuel receipts. The vehicle type and the business use are unknown. Default: the statutory proportion in Section 5.11. Ask: "Is this fuel for a passenger car, for a vehicle in one of the six listed uses, or for private use?"

### 6.2 Restaurants and entertainment

Any named restaurant, bar or cafeteria. Deductibility for income tax is unknown and art. 96.Uno.6 LIVA hangs on it. Default: block. Ask: "Is this meal a deductible expense in your income tax accounts, and who was it with?"

### 6.3 Ambiguous SaaS billing entities

Google, Microsoft, Adobe, Meta, Slack, Zoom, LinkedIn, Apple, Amazon, Dropbox, Atlassian, Stripe where the legal entity is not visible. The same brand bills from another member state (boxes 10 and 11), from outside the Union (boxes 12 and 13) or from Spain with IVA on the invoice. Default: reverse charge, boxes 12 and 13 out, 28 and 29 in. Ask: "Please send the latest invoice, I need the legal entity name and its country."

### 6.4 Round-number incoming transfers from owner-named counterparties

A large round credit from a name matching the client's. Default: exclude as an owner injection. Ask: "Is this transfer a customer payment, your own funds, or a loan?"

### 6.5 Incoming transfers from individual names (not owner)

Default: domestic sale to a consumer at the standard rate, boxes 07, 08 and 09. Ask: "Was it a sale? Business or consumer? Which country?"

### 6.6 Incoming transfers from foreign counterparties

Foreign IBAN or foreign currency. Default: domestic sale at the standard rate. Ask: "Business with a VAT number or consumer, goods or services, which country?"

### 6.7 Large one-off purchases (potential bienes de inversion)

A single invoice near the limit in Section 5.10, or labelled "ordenador", "equipo", "maquinaria". Default: compare the value with that limit; below it, boxes 28 and 29; at or above it and meant to last more than a year, boxes 30 and 31. Ask: "Please confirm the invoice total and whether the item will be used for more than a year."

### 6.8 Mixed-use phone, internet, home office

Movistar, Vodafone, Orange personal lines, home electricity. Default: no recovery where the business share is not declared. Ask: "Is this a dedicated business line or mixed use? What business percentage?"

### 6.9 Outgoing transfers to individuals

Default: exclude as drawings. Ask: "Was this a contractor with a factura, salary, a refund, or a personal transfer?"

### 6.10 Cash withdrawals

ATM, cajero, reintegro. Default: exclude as a personal drawing. Ask: "What was the cash used for, and is there a factura?"

### 6.11 Rent payments

A monthly "alquiler" or "renta" to a landlord. Default: no recovery, assuming a residential letting exempt under art. 20.Uno.23 LIVA. Ask: "Is this a commercial property, and does the landlord charge IVA on the rent?"

### 6.12 Foreign hotel and accommodation (non-Spain)

Default: no input VAT on this return. Foreign VAT is claimed, if at all, through the cross-border refund procedure. Ask: "Was this a business trip?"

### 6.13 Amazon purchases

Amazon.es, Amazon EU SARL. Amazon sells as Amazon Spain (domestic, IVA on the invoice), as a Luxembourg entity (intra-EU acquisition) or as a marketplace for a third-party seller. Default: domestic at the standard rate for Amazon.es retail. Ask: "Was this bought from Amazon itself or from a third-party seller? Please check the factura."

### 6.14 IRPF withholding on professional invoices

An incoming payment smaller than the invoice by exactly one of the professional withholding rates in Section 8. The payer withheld IRPF. Default: gross the payment back up to the invoice amount, because the VAT base is the full fee before withholding. Ask: "Please confirm the invoice amount before the retención."

### 6.15 Platform sales (Amazon, eBay, Wallapop, Etsy)

Platform settlements. Default: for Spain-only sales, the gross goes in boxes 07, 08 and 09 at the standard rate, and the platform's fee is a separate reverse charge. If the client sells to consumers in other member states above the distance-sales threshold in Section 9.10, the one-stop-shop refusal R-EU-5 fires. Ask: "Do you sell to buyers outside Spain? What were the total cross-border sales for the year?"

## Section 7: Excel working paper template (Spain-specific)

The base specification is in `vat-workflow-base` Section 3. This is the Spain-specific overlay.

### Sheet "Transactions"

Columns A to L per the base. Column H (box code) accepts only box codes from the box map in Section 1. Leave it blank for excluded transactions. For a reverse charge, enter the output box and the input box separated by a slash, for example 12/28.

### Sheet "Casilla Summary"

One row per box: column A the box number, column B the description, column C the value from a formula. The rate columns of the form (151, 166, 02, 154, 05, 08) hold the rate itself, not an amount. Mandatory rows:

~~~
Output:
| 01 | Base, super-reduced | =SUMIFS(Transactions!E:E, Transactions!H:H, "01") |
| 03 | Quota, super-reduced | =C[01_row]*super_reduced_rate |
| 04 | Base, reduced | =SUMIFS(Transactions!E:E, Transactions!H:H, "04") |
| 06 | Quota, reduced | =C[04_row]*reduced_rate |
| 07 | Base, standard | =SUMIFS(Transactions!E:E, Transactions!H:H, "07") |
| 09 | Quota, standard | =C[07_row]*standard_rate |
| 10 | Base, intra-EU acquisitions of goods and services | =SUMIFS(Transactions!E:E, Transactions!H:H, "10") |
| 11 | Quota, intra-EU acquisitions | =C[10_row]*standard_rate |
| 12 | Base, other reverse charge | =SUMIFS(Transactions!E:E, Transactions!H:H, "12") |
| 13 | Quota, other reverse charge | =C[12_row]*standard_rate |
| 152 | Quota, zero-rate row (150 to 152) | =SUMIFS on the VAT column, because this box carries no fixed rate |
| 167 | Quota, further rate row (165 to 167) | =SUMIFS on the VAT column, because this box carries no fixed rate |
| 155 | Quota, further rate row (153 to 155) | =SUMIFS on the VAT column, because this box carries no fixed rate |
| 158 | Quota, recargo de equivalencia, tobacco row (156 to 158) | =SUMIFS on the VAT column, because this box carries no fixed rate |
| 170 | Quota, recargo de equivalencia, super-reduced row (168 to 170) | =SUMIFS on the VAT column, because this box carries no fixed rate |
| 27 | Total cuota devengada | =SUM(C[152],C[167],C[03],C[155],C[06],C[09],C[11],C[13],C[15],C[158],C[170],C[18],C[21],C[24],C[26]) |

Input:
| 28 | Base, operaciones interiores corrientes | =SUMIFS(Transactions!E:E, Transactions!H:H, "28") |
| 29 | Quota, operaciones interiores corrientes | =SUMIFS on the VAT column, because the input side mixes rates |
| 30 | Base, interiores bienes de inversion | =SUMIFS(Transactions!E:E, Transactions!H:H, "30") |
| 31 | Quota, interiores bienes de inversion | =SUMIFS on the VAT column |
| 32 | Base, imports corrientes | =SUMIFS(Transactions!E:E, Transactions!H:H, "32") |
| 33 | Quota, imports corrientes | =SUMIFS on the VAT column |
| 36 | Base, intra-EU acquisitions corrientes | =SUMIFS(Transactions!E:E, Transactions!H:H, "36") |
| 37 | Quota, intra-EU acquisitions corrientes | =C[36_row]*standard_rate |
| 45 | Total a deducir | =SUM(C[29],C[31],C[33],C[35],C[37],C[39],C[41],C[42],C[43],C[44]) | ~~~

Name the rate cells (standard_rate, reduced_rate, super_reduced_rate) on a settings sheet and take the values from the rate table in Section 1, so one edit changes the whole workbook.

### Sheet "Return Form"

~~~
Box 27 = total cuota devengada
Box 45 = total a deducir
Box 46 = 27 - 45          (resultado régimen general)
Box 64 = 46 + 58 + 76     (suma de resultados)
Box 66 = 64               (or 64 x 65 where the taxpayer also files with a foral administration)
Box 78 = credit from earlier periods applied now
Box 69 = 66 + 77 - 78 + 68 + 108
Box 71 = 69 - 70 + 109 - 112

Box 71 positive  -> payable (ingreso)
Box 71 negative  -> a compensar, or a refund request, which outside the last
                    period of the year needs entry in the registro de devolución mensual
~~~

### Color and formatting conventions

Per the spreadsheet conventions: blue for hardcoded values from the bank statement, black for formulas, green for cross-sheet references, a yellow background on any row where Default? is "Y".

### Mandatory recalc step

After building the workbook, run:

~~~bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/spain-vat-period-working-paper.xlsx
~~~

## Section 8: Spanish bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Spain-specific patterns.

**Extracto bancario format conventions.** Spanish bank statements vary by institution but share common fields:

- **CaixaBank:** CSV or Excel export from CaixaBankNow. Fecha (date DD/MM/YYYY), Concepto, Importe (negative for debits), Saldo. The concepto often carries the beneficiary name after a dash.
- **Santander:** export from Santander One. Fecha Valor, Fecha Operacion, Concepto, Importe, Saldo. "ADEUDO" for debits, "ABONO" for credits.
- **BBVA:** export from the app or web. Fecha, Concepto, Movimiento (Cargo or Abono), Importe, Disponible.
- **Bankinter:** Fecha, Descripcion, Debe, Haber, Saldo.
- **Revolut, Wise, N26:** ISO dates (YYYY-MM-DD), English headers, amount in euro with a sign.

**Key Spanish-language terms in bank descriptions**

| Term | Meaning |
| --- | --- |
| Concepto | Description or reference |
| Beneficiario | Payee |
| Ordenante | Payer, on an incoming item |
| Cargo, Adeudo | Debit |
| Abono, Ingreso | Credit |
| Transferencia | Transfer |
| Domiciliacion, Recibo | Direct debit, bill payment |
| Bizum | Spanish instant payment |
| Reintegro, Cajero | Cash withdrawal, ATM |
| Comision | Bank fee |
| Nomina | Salary payment |
| Cuota autonomo | Self-employed social security payment |

**Internal transfers and exclusions.** Own-account transfers between the client's accounts, labelled "traspaso", "transferencia propia" or "movimiento entre cuentas". Always exclude.

**Self-employed draws.** An autónomo cannot pay themselves wages, so a transfer to a personal account is a drawing. Exclude.

**IRPF retenciones.** A business client paying a professional withholds IRPF, so the bank shows the net. The VAT base is the full fee before the withholding, so always gross it back up. The rates that produce the mismatch are below.

**IRPF withholding rates on a professional invoice**

| Case | Rate | Provision |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Professional invoice, general rate | 15% | art. 95.1 Reglamento IRPF |
| Professional starting the activity, in that year and the two following, provided no professional activity was carried on in the year before it started | 7% | art. 95.1 Reglamento IRPF |

**Refunds and reversals.** Identify by "devolucion", "anulacion" or "abono por devolucion". Book as a negative in the same box as the original, or, where the base itself changes, in boxes 14 and 15.

**Foreign currency transactions.** Convert to euro at the rate on the date of the tax point and note the rate used in column L.

**Bizum transactions.** Business Bizum shows merchant names, personal Bizum shows individual names. Default: exclude personal Bizum unless the client confirms it was a customer payment.

## Section 9: Onboarding fallback (only when inference fails)

The workflow in `vat-workflow-base` Section 1 says to infer the client profile from the data first and confirm in Step 4. This questionnaire is the fallback.

### 9.1 Entity type and trading name

Inference: "autónomo" or a personal name means a sole trader; "SL", "SA" or "SLU" means a company. Fallback: "Are you an autónomo or a company?"

### 9.2 VAT regime

Inference: asking for a modelo 303 means the régimen general. A mention of módulos fires R-ES-3, and a retailer buying with a surcharge on the invoice fires R-ES-4. Fallback: "Are you in the régimen general, the régimen simplificado, or recargo de equivalencia?"

### 9.3 NIF-IVA

Inference: sometimes visible in EU customer payment descriptions. Fallback: "What is your NIF-IVA, and are you listed in the VIES register?"

### 9.4 Filing period

Inference: the first and last transaction dates, and whether the client is inside the SII. Fallback: "Which period? 1T, 2T, 3T, 4T, or a month?"

### 9.5 Industry and sector

Inference: the counterparty mix and the invoice descriptions. Fallback: "In one sentence, what does the business do?"

### 9.6 Employees

Inference: outgoing TGSS, nómina or IRPF items. Fallback: "Do you have employees?"

### 9.7 Exempt supplies

Inference: medical, financial or educational income. Fallback: "Do you make any IVA-exempt sales?" If yes and not trivial, R-ES-6 fires.

### 9.8 SII obligation

Inference: a monthly period, or turnover above the monthly-filing amount in the deadline table in Section 1. Fallback: "Are you inside the SII, or in the registro de devolución mensual?"

### 9.9 Credit brought forward (boxes 110 and 78)

Not inferable from one period. Always ask: "Do you have IVA credit carried forward from earlier periods, and how much of it is still unapplied?"

### 9.10 Cross-border customers

Inference: foreign IBANs on incoming payments. Fallback: "Do you have customers outside Spain? Are they businesses or consumers, and in which countries?" Distance sales of goods and electronic services to consumers in other member states are taxed there once the threshold below is passed.

**Cross-border thresholds and scheme limits (Ley 37/1992)**

| Item | Amount | Provision |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Distance sales of goods and electronic, broadcasting and telecommunications services to consumers, one combined EU-wide threshold | EUR 10,000 | art. 73.Uno |
| Intra-EU acquisitions by farmers in the special scheme, businesses making only exempt supplies, and non-business legal persons: threshold above which the acquisitions are taxed here | EUR 10,000 | art. 14.Dos |
| Cash accounting scheme: turnover of the previous calendar year up to which it may be chosen | EUR 2,000,000 | art. 163 decies.Uno |
| Simplified regime: gross income of the previous year, other than farming, above which it cannot be used | EUR 150,000 | art. 122.Dos.2 |

## The method, step by step

1. **Fix the period and the regime.** Quarter or month is decided by art. 71.3 RIVA, and the monthly cases are listed in the deadline table in Section 1 ([RIVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925)). A monthly period also means the VAT registers must be kept through the Sede electrónica (art. 62.6 RIVA). Check whether any refusal in Section 2 fires before doing anything else.
2. **Classify every transaction against Ley 37/1992.** Rate, exemption, place of supply and reverse charge all come from the law, not from the bank narrative ([Ley 37/1992](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740)). Use the supplier library in Section 3 first, the Tier 1 rules in Section 5 next, and the Tier 2 defaults in Section 6 only where the data cannot answer the question.
3. **Fill the output side of the modelo 303.** Put each rate band in its own row of boxes, intra-EU acquisitions of goods and services in boxes 10 and 11, every other reverse charge in boxes 12 and 13, and base or quota changes in boxes 14 and 15. Box 27 is the total ([the form, Orden HAC/27/2026](https://www.boe.es/boe/dias/2026/01/26/pdfs/BOE-A-2026-1761.pdf)).
4. **Fill the input side.** Split the deductible quotas between operaciones interiores, imports and intra-EU acquisitions, and within each between corrientes and bienes de inversión, then add the rectifications and regularisations. Box 45 is the total and box 46 is the difference ([the form, Orden HAC/27/2026](https://www.boe.es/boe/dias/2026/01/26/pdfs/BOE-A-2026-1761.pdf)).
5. **Work the result, then file and pay electronically.** Apply the credit from earlier periods in box 78, read the result in box 71, and choose the declaration type the instructions define: a ingresar, a compensar, con solicitud de devolución, resultado cero, or sin actividad ([modelo 303 instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html)). A refund asked for before the last period of the year needs entry in the registro de devolución mensual (art. 30 RIVA).
6. **File the companion returns.** Modelo 349 for intra-EU supplies and services on the period in art. 81.2 RIVA, and modelo 390 for the year unless the client is exonerated ([Orden EHA/3111/2009](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18472)). Keep the SII records in step with the return, because the Agencia Tributaria builds its draft from them.

## Ask the client first

- Where is the business established, and does it trade in the Canary Islands, Ceuta or Melilla? A different tax applies there and this Guide does not cover it.
- Which regime are you in: régimen general, simplificado, recargo de equivalencia, criterio de caja, or a VAT group? Each one changes the form or takes you out of it.
- Is your period the quarter or the month, and are you in the SII or in the registro de devolución mensual? That decides the deadline and whether a refund can be asked for now.
- Do you make any exempt supplies without a right of deduction? If you do, the input VAT has to be apportioned before anything is claimed.
- How much credit from earlier periods is still unapplied? It goes in box 110, and only the part you apply now goes in box 78.
- For each foreign supplier and customer: which legal entity, in which country, and does the invoice show VAT? That decides between an intra-EU acquisition, another reverse charge, an import and a domestic purchase.

## When to refuse or refer

- The client is in the Canary Islands, Ceuta or Melilla, or asks about IGIC or IPSI (R-ES-1, R-ES-2).
- The client is in the régimen simplificado, in recargo de equivalencia, in the criterio de caja scheme, or in a VAT group (R-ES-3 to R-ES-5, R-ES-7).
- The client makes exempt supplies without a right of deduction, so a prorrata is needed (R-ES-6).
- The client uses a margin scheme for second-hand goods, travel packages or works of art (R-ES-8).
- The figures here would be used for a foral territory return (Araba, Bizkaia, Gipuzkoa or Navarra) or a return split between administrations. Those returns follow their own rules, and boxes 65, 66 and 68 assume a split this Guide does not compute.
- There is no invoice behind a claimed deduction, or the invoice is in someone else's name: art. 97 LIVA does not allow the deduction, whatever the bank statement shows.
- The question is about an autonomous community tax, income tax or social security rather than IVA.

## Section 10: Reference material

### Validation status

This is the v2.0 structure, refreshed in September 2026 against the official pages listed below. The box map was rebuilt from the modelo 303 approved by Orden HAC/27/2026 and from the 2026 instructions, and the rates and thresholds from Ley 37/1992 and RD 1624/1992. No accountant has yet attested this Guide.

### Sources

**Primary legislation:**
1. Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido (LIVA): art. 7, 13, 14, 20, 21, 22, 25, 69, 73, 84, 90, 91, 95, 96, 97, 99, 102 to 110, 122, 130, 148, 149, 154, 161, 163 decies
2. Real Decreto 1624/1992 (RIVA): art. 30, 62, 68 bis, 69 bis, 71, 74, 81
3. Real Decreto 1619/2012, invoicing rules: art. 4

**AEAT and ministerial sources:**
4. Orden HAC/27/2026, which approves the current modelo 303 form
5. Modelo 303 instructions for 2026, Agencia Tributaria
6. Orden EHA/3111/2009, modelo 390
7. Agencia Tributaria practical VAT manual, investment goods

**EU directive (through the companion Guide):**
8. Council Directive 2006/112/EC and Council Implementing Regulation 282/2011, in `eu-vat-directive`

### Known gaps

1. The supplier pattern library covers common Spanish and international counterparties, not every regional supplier, and a billing entity can change without notice.
2. The worked examples are for a software consultant. Hospitality, retail, construction and farming need their own examples.
3. The instructions do not say in so many words which input row takes the deductible side of a reverse charge that is not an intra-EU acquisition or an import. This Guide reads the box labels and uses operaciones interiores, boxes 28 and 29.
4. The investment-goods limit is printed as a figure only on the Agencia Tributaria manual page, because the law still states it in pesetas, and neither page says whether the value is measured with VAT or without.
5. Prorrata is refused outright. A later version could handle the general prorrata and box 44.
6. IGIC and IPSI are refused. They need their own Guides.
7. The form carries three rate rows the 2026 instructions assign to no rate (boxes 165 to 167, 153 to 155, and the recargo row 16 to 18). Do not guess what belongs in them.

### Change log

- **September 2026 refresh:** the whole box map was rebuilt from the form and the 2026 instructions; the earlier map was wrong in almost every line. Deadlines, the modelo 349 period test, the recargo rates including tobacco, the art. 96 exclusion list, the vehicle presumption and the investment-goods limit were re-sourced. Invented working thresholds were removed.
- **v2.0 (April 2026):** structure adopted, supplier library, worked examples, Tier 1 and Tier 2 catalogues, Excel template, bank statement guide, onboarding fallback.

### Self-check (v2.0)

1. Quick reference with the box map and conservative defaults: yes, Section 1.
2. Supplier library as literal lookup tables: yes, Section 3.
3. Worked examples: yes, Section 4.
4. Tier 1 rules: yes, Section 5.
5. Tier 2 catalogue: yes, Section 6.
6. Excel template with a recalc step: yes, Section 7.
7. Onboarding as a fallback: yes, Section 9.
8. All eight Spain-specific refusals: yes, Section 2.
9. Reference material at the bottom: yes, Section 10.
10. Vehicle presumption explicit: yes, Section 5.11 and Example 6.
11. Entertainment block explicit: yes, Section 5.12 and Example 3.
12. SII obligation documented: yes, Section 5.13.
13. IRPF withholding gross-up documented: yes, Section 6.14 and Section 8.
14. Reverse charge in both directions: yes, Examples 1 and 2, Sections 5.7 to 5.9.
15. Canary Islands, Ceuta and Melilla refusals: yes, R-ES-1 and R-ES-2.

## End of Spain VAT Return Guide v2.0

This Guide is self-contained for a régimen general modelo 303. The companion Guides `vat-workflow-base` and `eu-vat-directive` add the general workflow and the EU directive background, and are worth loading alongside it, but they are not required to work the return.

## Sources

- Ley 37/1992 del Impuesto sobre el Valor Añadido, consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- Real Decreto 1624/1992, Reglamento del IVA, consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925
- Real Decreto 1619/2012, invoicing rules, consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
- Orden HAC/27/2026, which approves the modelo 303 in force: https://www.boe.es/boe/dias/2026/01/26/pdfs/BOE-A-2026-1761.pdf
- Modelo 303 instructions for 2026, Agencia Tributaria: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
- Orden EHA/3111/2009, modelo 390, consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-2009-18472
- Reglamento del IRPF, RD 439/2007, professional withholding rates: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
- Agencia Tributaria, concept of investment goods: https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2025/capitulo-05-deducciones-devoluciones/deducciones/regularizacion-deducciones-bienes-inversion/concepto-bienes-inversion.html

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as an Asesor Fiscal, Economista, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
