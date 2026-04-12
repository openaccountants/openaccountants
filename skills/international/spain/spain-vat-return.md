---
name: spain-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Spanish VAT return (Modelo 303 / IVA autoliquidacion) for a self-employed individual or small business in peninsular Spain or the Balearic Islands. Trigger on phrases like "prepare VAT return", "do the Spanish VAT", "fill in Modelo 303", "IVA", "Modelo 390", or any request involving Spanish VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers peninsular Spain and Balearic Islands only under the regimen general. Canary Islands (IGIC), Ceuta/Melilla (IPSI), regimen simplificado, recargo de equivalencia, RECC cash-basis, VAT groups, and partial exemption (prorrata) are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Spain VAT work.
version: 2.0
---

# Spain VAT Return Skill (Modelo 303 / IVA) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Spain (Peninsula + Balearic Islands) |
| Standard rate | 21% (tipo general) |
| Reduced rates | 10% (tipo reducido), 4% (tipo superreducido) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods/services) |
| Return form | Modelo 303 (periodic self-assessment); Modelo 390 (annual summary) |
| Filing portal | Sede Electronica AEAT (sede.agenciatributaria.gob.es) |
| Authority | Agencia Estatal de Administracion Tributaria (AEAT) |
| Currency | EUR only |
| Filing frequencies | Quarterly (standard); Monthly (mandatory for SII-obliged / REDEME registrants / turnover > EUR 6,010,121.04) |
| Deadline | Quarterly: 1st–20th of month after quarter end (April, July, October, January — January deadline is 30th); Monthly: 1st–20th of following month |
| SII obligation | Suministro Inmediato de Informacion (RD 596/2016): real-time invoice reporting within 4 calendar days; mandatory for monthly filers |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Community |
| Validation date | April 2026 |

**Key Modelo 303 casillas (boxes):**

| Casilla | Meaning |
|---|---|
| 01 | Output base — standard rate 21% |
| 02 | Output VAT — standard rate 21% |
| 03 | Output base — reduced rate 10% |
| 04 | Output VAT — reduced rate 10% |
| 05 | Output base — super-reduced rate 4% |
| 06 | Output VAT — super-reduced rate 4% |
| 07 | Output base — recargo de equivalencia (surcharge) |
| 08–14 | Output VAT recargo at various rates |
| 15 | Output base — intra-EU acquisitions of goods |
| 16 | Output VAT on intra-EU acquisitions of goods |
| 17 | Output base — intra-EU acquisitions of services |
| 18 | Output VAT on intra-EU acquisitions of services |
| 19 | Output base — other reverse charge (Art. 84.Uno.2 LIVA) |
| 20 | Output VAT on other reverse charge |
| 21 | Output base — modification of bases and cuotas |
| 22 | Output VAT modification |
| 23 | Output base — recargo modification |
| 24 | Output VAT recargo modification |
| 25 | Total output cuotas (derived) |
| 26 | Total output cuotas inc. recargo (derived) |
| 27 | Total output VAT (derived: sum of output VAT lines) |
| 28 | Input base — domestic purchases (cuotas soportadas en operaciones interiores corrientes) |
| 29 | Input VAT — domestic purchases |
| 30 | Input base — investment goods (bienes de inversion) |
| 31 | Input VAT — investment goods |
| 32 | Input base — intra-EU acquisitions (corrientes) |
| 33 | Input VAT — intra-EU acquisitions |
| 34 | Input base — intra-EU investment goods |
| 35 | Input VAT — intra-EU investment goods |
| 36 | Input base — imports (corrientes) |
| 37 | Input VAT — imports |
| 38 | Input base — imports investment goods |
| 39 | Input VAT — imports investment goods |
| 40 | Rectification of input deductions |
| 41 | Rectification amount |
| 45 | Total input VAT deductible (derived: 29+31+33+35+37+39+41) |
| 46 | Difference (derived: 27 − 45) |
| 59 | Exclusive state-level output base |
| 60 | Exclusive state-level cuotas |
| 61 | Exclusive state-level cuotas devengadas |
| 64 | Result of the periodic self-assessment |
| 65 | Attributable to state administration (for regional split) |
| 66 | Resultado (derived) |
| 67 | Cuotas a compensar de periodos anteriores (credit brought forward) |
| 69 | Resultado de la autoliquidacion (final result: casilla 46 − casilla 67 adjustments) |
| 71 | Result payable or refundable (final line) |

**Conservative defaults — Spain-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 21% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Spain |
| Unknown B2B vs B2C status for EU customer | B2C, charge 21% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery (except vehicles — see 50% presumption in Section 5.11) |
| Unknown SaaS billing entity | Reverse charge from non-EU (casilla 36/37) |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 5,000 |
| HIGH tax-delta on a single conservative default | EUR 300 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | EUR 8,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Spanish or international business bank: CaixaBank, Santander, BBVA, Bankinter, Sabadell, ING Direct, Revolut Business, Wise Business, N26 Business, or any other.

**Recommended** — sales invoices for the period (especially for intra-EU B2B services and zero-rated supplies), purchase invoices (facturas) for any input VAT claim above EUR 300, the client's NIF-IVA in writing (ES + letter/digits).

**Ideal** — complete invoice register (libro registro de facturas emitidas y recibidas), Modelo 303 from prior period showing casilla 67 credit carried forward, SII submission confirmations.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This Modelo 303 was produced from bank statement alone. The reviewer must verify, before approval, that input VAT claims above EUR 300 are supported by compliant facturas and that all reverse-charge classifications match the supplier's invoice."

### Spain-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-ES-1 — Canary Islands (IGIC).** *Trigger:* client is located in the Canary Islands or asks about IGIC. *Message:* "The Canary Islands use IGIC (Impuesto General Indirecto Canario), not IVA. This skill covers IVA only (peninsular Spain + Balearic Islands). Please use an Asesor Fiscal familiar with IGIC."

**R-ES-2 — Ceuta or Melilla (IPSI).** *Trigger:* client is in Ceuta or Melilla or asks about IPSI. *Message:* "Ceuta and Melilla use IPSI (Impuesto sobre la Produccion, los Servicios y la Importacion), not IVA. Out of scope for this skill."

**R-ES-3 — Regimen simplificado (simplified modules).** *Trigger:* client files under the regimen simplificado with module-based calculations. *Message:* "The regimen simplificado uses activity-specific modules (modulos) to compute VAT, not actual transaction classification. This skill covers the regimen general only. Please use an Asesor Fiscal for module-based returns."

**R-ES-4 — Recargo de equivalencia.** *Trigger:* client is a retailer subject to recargo de equivalencia. *Message:* "Recargo de equivalencia is a special surcharge regime for retailers (personas fisicas) who sell goods without transformation. Suppliers charge the recargo surcharge (5.2%/1.4%/0.5%) and the retailer has no filing obligation or input VAT recovery. This skill covers the regimen general only."

**R-ES-5 — RECC cash-basis regime.** *Trigger:* client uses the regimen especial de criterio de caja. *Message:* "The RECC regime defers VAT to the payment date rather than the invoice date. This changes the timing of both output and input VAT reporting. This skill assumes the standard accrual basis (devengo). Please use an Asesor Fiscal for RECC returns."

**R-ES-6 — Prorrata de deduccion (partial exemption).** *Trigger:* client makes both taxable and exempt supplies (Art. 20 LIVA) and the exempt proportion is not de minimis. *Message:* "Your business makes both taxable and exempt supplies. Input VAT must be apportioned under the prorrata rules (Art. 102–106 LIVA). This requires the annual definitive prorrata ratio. Please use an Asesor Fiscal to determine the prorrata percentage before input VAT is claimed."

**R-ES-7 — VAT groups (grupos de entidades).** *Trigger:* client is part of a VAT group under Art. 163 quinquies–nonies LIVA. *Message:* "VAT group consolidation is out of scope. Please use an Asesor Fiscal."

**R-ES-8 — Used goods / travel agencies / art margin schemes.** *Trigger:* client deals in second-hand goods, travel agency packages, or art/antiques under margin scheme. *Message:* "Special margin scheme regimes (bienes usados, agencias de viaje, objetos de arte) require transaction-level margin computation. Out of scope."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules — the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Spanish banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| CAIXABANK, LA CAIXA | EXCLUDE for bank charges/fees | Art. 20.Uno.18 LIVA: financial service, exempt |
| SANTANDER, BANCO SANTANDER | EXCLUDE for bank charges/fees | Same |
| BBVA, BANCO BILBAO | EXCLUDE for bank charges/fees | Same |
| BANKINTER | EXCLUDE for bank charges/fees | Same |
| SABADELL, BANCO SABADELL | EXCLUDE for bank charges/fees | Same |
| ING DIRECT, ING BANK | EXCLUDE for bank charges/fees | Same |
| UNICAJA, KUTXABANK, IBERCAJA, ABANCA | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTERESES, INTEREST | EXCLUDE | Interest income/expense, exempt |
| PRESTAMO, HIPOTECA, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Spanish government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| AEAT, AGENCIA TRIBUTARIA, HACIENDA | EXCLUDE | Tax payment, not a supply |
| TGSS, TESORERIA GENERAL DE LA SEGURIDAD SOCIAL | EXCLUDE | Social security contribution |
| SEGURIDAD SOCIAL, SEG. SOCIAL | EXCLUDE | Social security contribution |
| IRPF, RETENCION | EXCLUDE | Income tax withholding payment |
| AYUNTAMIENTO | EXCLUDE | Municipal tax/fee, sovereign act |
| REGISTRO MERCANTIL | EXCLUDE | Registry fee, sovereign act |
| IMPUESTO, IAE, IBI | EXCLUDE | Tax payments |
| TRAFICO, DGT | EXCLUDE | Vehicle registration/fines, sovereign act |

### 3.3 Spanish utilities

| Pattern | Treatment | Casilla | Notes |
|---|---|---|---|
| IBERDROLA | Domestic 21% | 28/29 | Electricity — overhead |
| ENDESA, NATURGY, GAS NATURAL | Domestic 21% | 28/29 | Electricity/gas — overhead |
| REPSOL (energy bills) | Domestic 21% | 28/29 | Energy/heating — overhead |
| TELEFONICA, MOVISTAR | Domestic 21% | 28/29 | Telecoms — overhead |
| VODAFONE SPAIN, VODAFONE ES | Domestic 21% | 28/29 | Telecoms — overhead |
| ORANGE, MASMOVIL, YOIGO, DIGI | Domestic 21% | 28/29 | Telecoms — overhead |
| AGUA, CANAL DE ISABEL II, AGUAS | Domestic 10% | 28/29 | Water supply — reduced rate |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MAPFRE, MUTUA MADRILENA, MUTUALIA | EXCLUDE | Insurance, exempt Art. 20.Uno.16 LIVA |
| AXA SEGUROS, ALLIANZ, ZURICH | EXCLUDE | Same |
| GENERALI, SANTALUCIA, PELAYO | EXCLUDE | Same |
| SEGURO, POLIZA, PRIMA | EXCLUDE | Insurance premium, exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Casilla | Notes |
|---|---|---|---|
| CORREOS, SOCIEDAD ESTATAL CORREOS | EXCLUDE for standard postage | | Universal postal service, exempt |
| CORREOS EXPRESS | Domestic 21% | 28/29 | Express/courier is taxable |
| SEUR, MRW, NACEX, GLS SPAIN | Domestic 21% | 28/29 | Courier services, taxable |
| DHL EXPRESS SPAIN | Domestic 21% | 28/29 | Express courier |
| DHL INTERNATIONAL | EU reverse charge (DE entity) | 32/33 | Check invoice — European billing entity |

### 3.6 Transport

| Pattern | Treatment | Casilla | Notes |
|---|---|---|---|
| RENFE | Domestic 10% | 28/29 | Passenger rail — reduced rate (Art. 91 LIVA) |
| METRO, EMT, TMB, TUSSAM | EXCLUDE or 10% | | Public urban transport — reduced rate |
| CABIFY | Domestic 21% | 28/29 | Ride-hailing platform fee |
| UBER SPAIN | Domestic 21% | 28/29 | Ride-hailing |
| IBERIA, VUELING, AIR EUROPA (international) | EXCLUDE / 0% | | International flights exempt Art. 22 LIVA |
| IBERIA, VUELING (domestic) | Domestic 10% | | Domestic passenger flights — reduced rate |
| BLABLACAR | EXCLUDE | | Peer-to-peer, no VAT supply |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| MERCADONA, DIA, LIDL, ALDI, CARREFOUR | Default BLOCK input VAT | Personal provisioning. Deductible only if hospitality/catering. Rate mix: 4% staples, 10% prepared food, 21% non-food |
| EL CORTE INGLES (food hall) | Default BLOCK | Same |
| SUPERMERCADO, ALIMENTACION | Default BLOCK | Same |
| RESTAURANTS, CAFES, BARS (any named) | Default BLOCK | Entertainment — see Section 5.12 |

### 3.8 SaaS — EU suppliers (reverse charge, casilla 17/18)

These are billed from EU entities (typically Ireland or Luxembourg) and trigger inversion del sujeto pasivo (reverse charge) under Art. 84.Uno.2 LIVA for services.

| Pattern | Billing entity | Casilla | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 17/18 + 32/33 | Reverse charge services |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 17/18 + 32/33 | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 17/18 + 32/33 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 17/18 + 32/33 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 17/18 + 32/33 | Reverse charge |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 17/18 + 32/33 | EU, reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 17/18 + 32/33 | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | 17/18 + 32/33 | Reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 17/18 + 32/33 | EU, reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 17/18 + 32/33 | Reverse charge |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | 17/18 + 32/33 | Transaction fees may be exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (reverse charge, casilla 19/20 + 36/37)

| Pattern | Billing entity | Casilla | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | 17/18 + 32/33 | LU entity = EU reverse charge |
| NOTION | Notion Labs Inc (US) | 19/20 + 36/37 | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 19/20 + 36/37 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 19/20 + 36/37 | Non-EU reverse charge |
| GITHUB (standard plans) | GitHub Inc (US) | 19/20 + 36/37 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | 19/20 + 36/37 | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | 19/20 + 36/37 | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE) — check invoice | 19/20 or 17/18 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 19/20 + 36/37 | Non-EU reverse charge |

### 3.10 SaaS — the exception (NOT reverse charge)

| Pattern | Treatment | Why |
|---|---|---|
| AWS EMEA SARL | EU reverse charge casilla 17/18 + 32/33 (Luxembourg entity) | Standard EU reverse charge. If invoice shows Spanish IVA charged, treat as domestic 21%. |
| AMAZON ES, AMAZON.ES (marketplace) | Domestic 21% | Amazon Spain retail — domestic supply with IVA on invoice |

### 3.11 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (monthly subscription) | EU reverse charge casilla 17/18 + 32/33 | Stripe IE entity — separate from transaction fees |
| REDSYS, SERVIRED | EXCLUDE (exempt) | Card processing, exempt financial service |
| SUMUP, SQUARE, ZETTLE | Check invoice | If Spanish entity: domestic 21%; if IE/EU entity: reverse charge |

### 3.12 Professional services (Spain)

| Pattern | Treatment | Casilla | Notes |
|---|---|---|---|
| NOTARIO, NOTARIA | Domestic 21% | 28/29 | Notary fees, deductible if business purpose |
| ASESOR, ASESORIA, GESTORIA | Domestic 21% | 28/29 | Tax advisor/accountant, always deductible |
| ABOGADO, BUFETE, DESPACHO | Domestic 21% | 28/29 | Legal services, deductible if business purpose |
| REGISTRO MERCANTIL | EXCLUDE | | Government registry fee |
| COLEGIO PROFESIONAL | Domestic 21% | 28/29 | Professional body membership |

### 3.13 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| NOMINA, SALARIO, SUELDO | EXCLUDE | Wages — outside VAT scope |
| TGSS, SEGURIDAD SOCIAL | EXCLUDE | Statutory SSC payment |
| IRPF, RETENCION, MOD 111, MOD 190 | EXCLUDE | IRPF withholding payment |
| AUTONOMO, RETA, CUOTA AUTONOMO | EXCLUDE | Self-employed social security quota |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| ALQUILER, RENTA (commercial, with IVA) | Domestic 21% | Commercial lease where landlord charges IVA |
| ALQUILER, RENTA (residential, no IVA) | EXCLUDE | Residential lease exempt Art. 20.Uno.23 LIVA |
| COMUNIDAD DE PROPIETARIOS | EXCLUDE | Building community fees — not a taxable supply |
| HIPOTECA | EXCLUDE | Mortgage payment, financial service |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRASPASO, TRANSFERENCIA PROPIA | EXCLUDE | Internal movement |
| DIVIDENDO | EXCLUDE | Dividend payment, out of scope |
| AMORTIZACION PRESTAMO | EXCLUDE | Loan repayment, out of scope |
| REINTEGRO, CAJERO, ATM | TIER 2 — ask | Default exclude; ask what cash was spent on |
| BIZUM (personal) | EXCLUDE | Personal transfers via Bizum |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Spain-based self-employed software consultant (autonomo). They illustrate the trickiest cases.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; CARGO ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.9). No IVA on the invoice. This is a service received from a non-EU supplier. Art. 84.Uno.2 LIVA triggers inversion del sujeto pasivo. Both sides of the reverse charge must be reported: output IVA in casilla 19/20, input IVA in casilla 36/37. Net effect zero for a fully taxable registrant.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Casilla (input) | Casilla (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.08 | 21% | 36/37 | 19/20 | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; CARGO ; Google Ads abril 2026 ; -850.00 ; EUR`

**Reasoning:**
Google Ireland Limited is an IE entity — standard EU reverse charge for services. Casilla 17 for the output base, casilla 18 for output IVA, casilla 32 for input base, casilla 33 for input IVA. Net cash effect zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Casilla (input) | Casilla (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 178.50 | 21% | 32/33 | 17/18 | N | — | — |

### Example 3 — Entertainment, no deduction right

**Input line:**
`15.04.2026 ; RESTAURANTE BOTIN MADRID ; CARGO ; Cena de negocios ; -180.00 ; EUR`

**Reasoning:**
Restaurant transaction. Under Spanish rules, entertainment and client meals (atenciones a clientes) are deductible for income tax purposes (IRPF) up to 1% of net turnover but the IVA deductibility is restricted: Art. 96.Uno.5 LIVA limits input IVA recovery on entertainment to expenses that are "strictly necessary" for business activity and can be justified. The conservative default is to block recovery. Flag for reviewer.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Casilla | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANTE BOTIN | -180.00 | -180.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked (conservative)" |

### Example 4 — Investment goods (bienes de inversion)

**Input line:**
`18.04.2026 ; APPLE STORE PASEO DE GRACIA ; CARGO ; MacBook Pro 16 ; -2,999.00 ; EUR`

**Reasoning:**
Gross amount is EUR 2,999. Investment goods threshold in Spain: assets with useful life > 1 year and acquisition cost > EUR 3,005.06 (historical threshold). At EUR 2,999 this falls just below the bienes de inversion threshold, so it goes to casilla 28/29 (current domestic inputs), not casilla 30/31. However, if the total including accessories exceeds the threshold, reclassify. Conservative: treat as ordinary input.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Casilla | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | APPLE STORE | -2,999.00 | -2,478.51 | -520.49 | 21% | 28/29 | N | — | — |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; KREBS CONSULTING GMBH ; ABONO ; Factura ES-2026-018 consultoria IT marzo ; +4,200.00 ; EUR`

**Reasoning:**
Incoming EUR 4,200 from a German company. Client provides IT consulting services. B2B place of supply for services is the customer's country (Germany) under Art. 69.Uno.1 LIVA (general rule). Client invoices at 0% with a note that the customer self-assesses. Not reported in casilla 01–06 (those are domestic). Reported in Modelo 303 informative section (casilla 59 for operations with EU) and in the recapitulative declaration Modelo 349. Confirm: (a) customer has a valid DE VAT number verified on VIES; (b) the invoice shows no Spanish IVA.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Casilla | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | KREBS CONSULTING GMBH | +4,200.00 | +4,200.00 | 0 | 0% | 59 (informative) | Y | Q2 (HIGH) | "Verify DE USt-IdNr on VIES" |

### Example 6 — Vehicle costs, 50% presumption

**Input line:**
`28.04.2026 ; REPSOL ESTACION DE SERVICIO ; CARGO ; Gasoleo A ; -85.00 ; EUR`

**Reasoning:**
Fuel purchase. In Spain, vehicle expenses have a special rule: Art. 95.Tres.2 LIVA creates a rebuttable presumption of 50% business use for passenger vehicles. This means 50% of input IVA is deductible by default (unlike Malta where vehicles are fully blocked). The 50% can be increased if the taxpayer proves higher business use, or reduced if AEAT proves lower. Conservative default: 50% recovery.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Casilla | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | REPSOL | -85.00 | -70.25 | -7.38 | 21% (50%) | 28/29 | Y | Q3 | "Vehicle fuel: 50% presumption applied" |

---

## Section 5 — Tier 1 classification rules (compressed)

Each rule states the legal source and the casilla mapping. Apply silently if the data is unambiguous. For full doctrinal context, see the source citations in Section 10.

### 5.1 Standard rate 21% (Art. 90 LIVA)

Default rate for any taxable supply unless a reduced rate, zero rate, or exemption applies. Sales → casilla 01/02. Purchases → casilla 28/29.

### 5.2 Reduced rate 10% (Art. 91.Uno LIVA)

Applies to: food and beverages (excluding alcohol and tobacco), water supply, passenger transport (rail, bus, taxi, domestic air), hotel accommodation, restaurant and catering services, spectacles and cinema, housing (first transfer of new housing), medical devices, agricultural inputs. Sales → casilla 03/04. Purchases → casilla 28/29 (input base is aggregated).

### 5.3 Super-reduced rate 4% (Art. 91.Dos LIVA)

Applies to: bread, milk, eggs, fruit, vegetables, cereals, cheese, books, newspapers, periodicals, pharmaceutical products for human use, vehicles for disabled persons, social housing (VPO), prosthetics and implants. Sales → casilla 05/06. Purchases → casilla 28/29.

### 5.4 Zero rate and exempt with credit

Exports outside EU → exempt with right of deduction (Art. 21 LIVA), reported in casilla 60 informative. Intra-EU B2B supplies of goods → exempt with right of deduction (Art. 25 LIVA), reported in Modelo 349. Intra-EU B2B services → place of supply is customer's country (Art. 69 LIVA), reported in Modelo 349.

### 5.5 Exempt without credit (Art. 20 LIVA)

Medical services, education, insurance, financial services, postal universal service, residential lettings, social welfare. These supplies are excluded from the return — no output VAT, no input VAT deduction on related costs. If significant → R-ES-6 prorrata refusal fires.

### 5.6 Local standard purchases

Input VAT on a compliant factura from a Spanish supplier is deductible for purchases used in taxable business activity. Subject to blocked-input rules (5.12) and bienes de inversion threshold (5.9). Map to casilla 28/29 (corrientes) or 30/31 (bienes de inversion).

### 5.7 Reverse charge — intra-EU services received (Art. 84.Uno.2 LIVA)

When the client receives a service from an EU supplier and the supplier invoices at 0% with a reverse-charge note: output base → casilla 17, output IVA → casilla 18, input base → casilla 32, input IVA → casilla 33. Net effect zero. If the EU supplier charged their local VAT (e.g. Irish 23%), that is NOT reverse charge — treat as irrecoverable foreign VAT.

### 5.8 Reverse charge — intra-EU goods received (Art. 13 LIVA)

Physical goods from an EU supplier: output base → casilla 15, output IVA → casilla 16, input base → casilla 32, input IVA → casilla 33.

### 5.9 Reverse charge — non-EU services and imports

Services from non-EU → Art. 84.Uno.2 LIVA: output base → casilla 19, output IVA → casilla 20, input base → casilla 36, input IVA → casilla 37. Physical goods imports: import IVA is paid at customs (DUA) and recovered via casilla 36/37.

### 5.10 Investment goods — bienes de inversion (Art. 108–110 LIVA)

Assets with useful life > 1 year and net acquisition cost > EUR 3,005.06: casilla 30/31 (domestic), casilla 34/35 (intra-EU), casilla 38/39 (imports). Subject to a 4-year adjustment period (9 years for immovable property). If gross < threshold → casilla 28/29 (ordinary input).

### 5.11 Vehicle deduction — 50% presumption (Art. 95.Tres.2 LIVA)

Passenger vehicles (turismos) and related expenses (fuel, maintenance, insurance premiums for the vehicle itself — but insurance is exempt anyway): rebuttable presumption of 50% business use. Apply 50% input IVA recovery by default. Vehicles used exclusively for: taxi/VTC, driving school, commercial transport, or traveling sales → 100% deduction. The 50% presumption does NOT apply to vans (furgonetas), trucks, or motorbikes used for delivery.

### 5.12 Restricted input VAT (Art. 96 LIVA)

The following categories have restricted or no VAT recovery:
- Jewellery, precious stones, and furs (Art. 96.Uno.1)
- Food, drink, and tobacco (Art. 96.Uno.2) — unless hospitality/catering business
- Spectacles and entertainment (Art. 96.Uno.3) — for client entertainment
- Services related to the above (Art. 96.Uno.4)
- Gifts and samples above EUR 200 per recipient per year (Art. 96.Uno.5) — IVA deductible below threshold

Unlike Malta, Spain does NOT have a hard block on entertainment. The IVA on business meals CAN be deductible if the expense is strictly necessary and directly related to the business activity. However, the conservative default is to block — the burden of proof is on the taxpayer.

### 5.13 SII — Suministro Inmediato de Informacion (RD 596/2016)

SII-obliged entities must report invoices to AEAT within 4 calendar days of issue (sales) or accounting date (purchases). SII is mandatory for monthly filers. If client is SII-obliged, note in the reviewer brief that invoice data must match the SII submissions.

### 5.14 Modelo 390 — annual summary

Modelo 390 is an annual informative declaration summarizing all periodic Modelo 303 filings. Due by 30 January following the tax year. SII-obliged entities are exempt from filing Modelo 390 (since 2017).

### 5.15 Modelo 349 — recapitulative declaration

Quarterly (or monthly if intra-EU operations exceed EUR 50,000 in any quarter): declares all intra-EU supplies and acquisitions. Must reconcile with casillas 15–18 and informative casilla 59.

---

## Section 6 — Tier 2 catalogue (compressed)

For each ambiguity type: pattern, why the bank statement is insufficient, conservative default, question for the structured form.

### 6.1 Fuel and vehicle costs

*Pattern:* Repsol, Cepsa, BP, Shell, Galp, fuel receipts. *Why insufficient:* vehicle type and business-use proportion unknown. *Default:* 50% recovery for passenger vehicles (Art. 95.Tres.2 LIVA presumption). *Question:* "Is this fuel for a passenger car (50% presumption), a commercial vehicle (100%), or personal use (0%)?"

### 6.2 Restaurants and entertainment

*Pattern:* any named restaurant, bar, cafeteria. *Why insufficient:* business necessity unclear. *Default:* block. *Question:* "Was this a business meal strictly necessary for the activity? (Note: conservative default is to block — reviewer must confirm deductibility under Art. 96 LIVA.)"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, Adobe, Meta, Slack, Zoom, LinkedIn, Apple, Amazon, Dropbox, Atlassian, Stripe where the legal entity is not visible. *Why insufficient:* same brand can bill from Ireland (EU reverse charge casilla 17/18), US (non-EU reverse charge casilla 19/20), or Spain (domestic 21%). *Default:* non-EU reverse charge casilla 19/20 + 36/37. *Question:* "Could you check the most recent invoice? I need the legal entity name and country."

### 6.4 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit from a name matching the client's name. *Default:* exclude as owner injection. *Question:* "The EUR X transfer from [name] — is this a customer payment, your own funds, or a loan?"

### 6.5 Incoming transfers from individual names (not owner)

*Pattern:* incoming from private-looking counterparties. *Default:* domestic B2C sale at 21%, casilla 01/02. *Question:* "Was it a sale? Business or consumer? Country?"

### 6.6 Incoming transfers from foreign counterparties

*Pattern:* foreign IBAN or foreign currency. *Default:* domestic 21%. *Question:* "B2B with VAT number, B2C, goods or services, which country?"

### 6.7 Large one-off purchases (potential bienes de inversion)

*Pattern:* single invoice EUR 2,500–3,500 range or labelled "ordenador", "equipo", "maquinaria". *Default:* if net > EUR 3,005.06 → casilla 30/31; if net <= EUR 3,005.06 → casilla 28/29. *Question:* "Confirm the total invoice amount including IVA."

### 6.8 Mixed-use phone, internet, home office

*Pattern:* Movistar, Vodafone, Orange personal lines; home electricity. *Default:* 0% if mixed without declared %. *Question:* "Is this a dedicated business line or mixed-use? What business percentage?"

### 6.9 Outgoing transfers to individuals

*Pattern:* outgoing to private-looking names. *Default:* exclude as drawings. *Question:* "Was this a contractor (with factura), salary, refund, or personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* ATM, cajero, reintegro. *Default:* exclude as personal drawing. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* monthly "alquiler", "renta" to a landlord name. *Default:* no IVA recovery (residential assumption). *Question:* "Is this a commercial property? Does the landlord charge IVA on the rent?"

### 6.12 Foreign hotel and accommodation (non-Spain)

*Pattern:* hotel abroad. *Default:* exclude from input IVA. *Question:* "Was this a business trip?" (For IRPF, the expense may still be deductible.)

### 6.13 Amazon purchases

*Pattern:* Amazon.es, Amazon EU SARL. *Why insufficient:* Amazon can sell as Amazon Spain (domestic 21%), Amazon EU SARL Luxembourg (EU reverse charge), or third-party marketplace seller. *Default:* domestic 21% for Amazon.es retail. *Question:* "Was this purchased from Amazon directly or a third-party seller? Check the factura."

### 6.14 IRPF withholding on professional invoices

*Pattern:* incoming payment that is less than the invoiced amount by exactly 15% or 7%. *Why insufficient:* the payer withheld IRPF retencion. *Default:* gross up the payment to the full invoice amount for IVA base calculation. *Question:* "Confirm the invoice amount before IRPF retention."

### 6.15 Platform sales (Amazon, eBay, Wallapop, Etsy)

*Pattern:* incoming from platform settlements. *Default:* if selling to EU consumers across multiple countries above EUR 10,000, R-EU-5 OSS refusal fires. For Spain-only: treat gross as casilla 01/02 base at 21%; platform fees as separate reverse charge casilla 17/18 (IE entity). *Question:* "Do you sell to buyers outside Spain? Total EU cross-border sales for the year?"

---

## Section 7 — Excel working paper template (Spain-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Spain-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Casilla code") accepts only valid Modelo 303 casilla codes from Section 1 of this skill. Use blank for excluded transactions. For reverse-charge transactions, enter both the output casilla (e.g. 17) and the input casilla (e.g. 32) separated by a slash in column H.

### Sheet "Casilla Summary"

One row per casilla. Column A is the casilla number, column B is the description, column C is the value computed via formula. Mandatory rows:

```
Output:
| 01 | Output base 21% | =SUMIFS(Transactions!E:E, Transactions!H:H, "01") |
| 02 | Output IVA 21% | =Casilla_Summary!C[01_row]*0.21 |
| 03 | Output base 10% | =SUMIFS(Transactions!E:E, Transactions!H:H, "03") |
| 04 | Output IVA 10% | =Casilla_Summary!C[03_row]*0.10 |
| 05 | Output base 4% | =SUMIFS(Transactions!E:E, Transactions!H:H, "05") |
| 06 | Output IVA 4% | =Casilla_Summary!C[05_row]*0.05 |
| 15 | Output base intra-EU goods | =SUMIFS(Transactions!E:E, Transactions!H:H, "15") |
| 16 | Output IVA intra-EU goods | =C[15_row]*0.21 |
| 17 | Output base intra-EU services | =SUMIFS(Transactions!E:E, Transactions!H:H, "17") |
| 18 | Output IVA intra-EU services | =C[17_row]*0.21 |
| 19 | Output base non-EU reverse charge | =SUMIFS(Transactions!E:E, Transactions!H:H, "19") |
| 20 | Output IVA non-EU reverse charge | =C[19_row]*0.21 |
| 27 | Total output IVA | =SUM(C[02],C[04],C[06],C[16],C[18],C[20]) |

Input:
| 28 | Input base domestic current | =SUMIFS(Transactions!E:E, Transactions!H:H, "28") |
| 29 | Input IVA domestic current | =variable rate — use SUMIFS on VAT column |
| 30 | Input base investment goods | =SUMIFS(Transactions!E:E, Transactions!H:H, "30") |
| 31 | Input IVA investment goods | =C[30_row]*0.21 |
| 32 | Input base intra-EU current | =SUMIFS(Transactions!E:E, Transactions!H:H, "32") |
| 33 | Input IVA intra-EU current | =C[32_row]*0.21 |
| 36 | Input base imports/non-EU | =SUMIFS(Transactions!E:E, Transactions!H:H, "36") |
| 37 | Input IVA imports/non-EU | =C[36_row]*0.21 |
| 45 | Total input IVA | =SUM(C[29],C[31],C[33],C[35],C[37],C[39],C[41]) |
```

### Sheet "Return Form"

Final Modelo 303-ready figures:

```
Casilla 27 = Total output IVA
Casilla 45 = Total input IVA deductible

Casilla 46 = Casilla 27 - Casilla 45   [difference]
Casilla 67 = Credit brought forward from prior period
Casilla 69 = Casilla 46 - Casilla 67   [final result]

Positive Casilla 69 → payable to AEAT (ingreso)
Negative Casilla 69 → credit to carry forward (a compensar) or request refund (devolucion, only in Q4 annual or REDEME monthly)
```

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values from the bank statement, black for formulas, green for cross-sheet references, yellow background for any row where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/spain-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Spanish bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Spain-specific patterns.

**Extracto bancario format conventions.** Spanish bank statements (extractos bancarios) vary by institution but share common fields:

- **CaixaBank:** CSV/Excel export from CaixaBankNow. Columns: Fecha (date DD/MM/YYYY), Concepto (description), Importe (amount, negative for debits), Saldo (balance). The concepto field often includes the beneficiary name after a dash.
- **Santander:** Online export from Santander One. Columns: Fecha Valor, Fecha Operacion, Concepto, Importe, Saldo. Uses "ADEUDO" for debits, "ABONO" for credits.
- **BBVA:** Export from BBVA app/web. Columns: Fecha, Concepto, Movimiento (Cargo/Abono), Importe, Disponible. "Cargo" = debit, "Abono" = credit.
- **Bankinter:** Columns: Fecha, Descripcion, Debe (debit), Haber (credit), Saldo.
- **Revolut/Wise/N26:** ISO date format (YYYY-MM-DD), English column headers, amount in EUR with sign.

**Key Spanish-language terms in bank descriptions:**

| Term | Meaning |
|---|---|
| Concepto | Description/reference |
| Beneficiario | Payee |
| Ordenante | Payer (on incoming) |
| Cargo / Adeudo | Debit |
| Abono / Ingreso | Credit |
| Transferencia | Transfer |
| Domiciliacion / Recibo | Direct debit / bill payment |
| Bizum | Spanish instant payment (like Venmo) |
| Reintegro / Cajero | Cash withdrawal / ATM |
| Comision | Bank fee/commission |
| Nomina | Salary payment |
| Cuota autonomo | Self-employed social security payment |

**Internal transfers and exclusions.** Own-account transfers between the client's CaixaBank, Santander, BBVA, Revolut accounts. Labelled "traspaso", "transferencia propia", "movimiento entre cuentas". Always exclude.

**Self-employed (autonomo) draws.** A self-employed person (autonomo/persona fisica) cannot pay themselves wages — any transfer to a personal account is a drawing. Exclude.

**IRPF retenciones.** Incoming payments from business clients may be net of 15% IRPF retention (or 7% for new autonomos in first 3 years). The bank statement shows the net amount received. The IVA base is the full invoice amount before retention. Always gross up.

**Refunds and reversals.** Identify by "devolucion", "anulacion", "abono por devolucion". Book as a negative in the same casilla as the original transaction.

**Foreign currency transactions.** Convert to EUR at the transaction date rate. Use the ECB reference rate. Note the rate in column L (Notes).

**Bizum transactions.** Bizum is Spain's peer-to-peer instant payment. Business Bizum (Bizum Comercios) shows merchant names. Personal Bizum shows individual names. Default: exclude personal Bizum as non-business unless client confirms it was a customer payment.

---

## Section 9 — Onboarding fallback (only when inference fails)

The workflow in `vat-workflow-base` Section 1 mandates inferring the client profile from the data first and only confirming in Step 4. The questionnaire below is a fallback.

### 9.1 Entity type and trading name
*Inference rule:* "autonomo" or personal name = sole trader; "SL", "SA", "SLU" = company. *Fallback:* "Are you an autonomo (persona fisica) or a company (SL/SA)?"

### 9.2 VAT regime
*Inference rule:* if asking for Modelo 303, they are regimen general. If they mention modulos or modules, R-ES-3 fires. *Fallback:* "Are you in the regimen general, regimen simplificado, or recargo de equivalencia?"

### 9.3 NIF-IVA
*Inference rule:* sometimes visible in EU customer payment descriptions. *Fallback:* "What is your NIF-IVA? (ES + 9 characters)"

### 9.4 Filing period
*Inference rule:* first and last transaction dates. Standard is quarterly. *Fallback:* "Which quarter? 1T (Jan–Mar), 2T (Apr–Jun), 3T (Jul–Sep), or 4T (Oct–Dec)?"

### 9.5 Industry and sector
*Inference rule:* counterparty mix, invoice descriptions. *Fallback:* "In one sentence, what does the business do?"

### 9.6 Employees
*Inference rule:* TGSS/nomina/IRPF outgoing. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Inference rule:* medical/financial/educational income. *Fallback:* "Do you make any IVA-exempt sales?" *If yes and non-de-minimis → R-ES-6 fires.*

### 9.8 SII obligation
*Inference rule:* monthly filing frequency, turnover > EUR 6M. *Fallback:* "Are you registered in SII or REDEME?"

### 9.9 Credit brought forward (casilla 67)
*Not inferable from a single period. Always ask.* "Do you have IVA credit carried forward from the previous period (casilla 67 of prior Modelo 303)?"

### 9.10 Cross-border customers
*Inference rule:* foreign IBANs on incoming payments. *Fallback:* "Do you have customers outside Spain? EU or non-EU? Businesses or consumers?"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the three-tier Accora architecture (vat-workflow-base + eu-vat-directive + country skill). The Spain-specific content (casilla mappings, rates, thresholds, blocked categories, SII requirements) is based on LIVA and RIVA as of April 2026.

### Sources

**Primary legislation:**
1. Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Anadido (LIVA) — Art. 3, 4, 11, 13–16, 20, 21–25, 69, 84, 90, 91, 92–96, 102–106, 108–110, 148–163
2. Real Decreto 1624/1992, de 29 de diciembre (RIVA — Reglamento del IVA) — Art. 30 (filing frequency)
3. Real Decreto 596/2016 (SII — Suministro Inmediato de Informacion)

**AEAT guidance:**
4. Modelo 303 form and completion instructions — sede.agenciatributaria.gob.es
5. Modelo 390 annual summary instructions
6. Modelo 349 recapitulative declaration instructions
7. AEAT guidance on inversion del sujeto pasivo (reverse charge)
8. AEAT guidance on bienes de inversion (investment goods)

**EU directive (loaded via companion skill):**
9. Council Directive 2006/112/EC (Principal VAT Directive) — implemented via eu-vat-directive companion skill
10. Council Implementing Regulation 282/2011

**Other:**
11. VIES validation — https://ec.europa.eu/taxation_customs/vies/
12. ECB euro reference rates — https://www.ecb.europa.eu/stats/eurofxref/

### Known gaps

1. The supplier pattern library covers common Spanish and international counterparties but not every regional supplier.
2. Worked examples are for a software consultant. Hospitality, retail, construction, and agricultural sectors need v2.1 examples.
3. The 50% vehicle presumption (Art. 95.Tres.2) is well-established but AEAT may challenge it — flag for reviewer if vehicle costs are significant.
4. The bienes de inversion threshold (EUR 3,005.06 net) is the historical amount. Verify annually.
5. Prorrata calculation (Art. 102–106) is refused entirely — a future version should add basic prorrata support.
6. IGIC/IPSI for Canary Islands/Ceuta/Melilla is refused — separate skills needed.
7. The entertainment deduction rule (Art. 96) is fact-sensitive — the conservative block is appropriate but a reviewer may unlock it.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with three-tier Accora architecture. 10-section Malta v2.0 structure adopted. Supplier pattern library restructured as literal lookup tables (Section 3). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template added (Section 7). Bank statement guide with extracto bancario formats added (Section 8). Onboarding moved to fallback (Section 9).
- **v2.1-verified (April 2026):** Previous version with inline tier tags. Superseded by this rewrite.

### Self-check (v2.0)

1. Quick reference at top with casilla table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples (hypothetical autonomo IT consultant): yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 15 rules).
5. Tier 2 catalogue compressed with inference rules: yes (Section 6, 15 items).
6. Excel template with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only, inference rules first: yes (Section 9, 10 items).
8. All 8 Spain-specific refusals present: yes (Section 2, R-ES-1 through R-ES-8).
9. Reference material at bottom: yes (Section 10).
10. Vehicle 50% presumption explicit: yes (Section 5.11 + Example 6).
11. Entertainment conservative block explicit: yes (Section 5.12 + Example 3).
12. SII obligation documented: yes (Section 5.13).
13. IRPF retention grossing-up documented: yes (Section 6.14 + Section 8).
14. Reverse charge both directions (EU + non-EU) explicit: yes (Examples 1–2 + Section 5.7–5.9).
15. Canary Islands/Ceuta/Melilla refusal explicit: yes (R-ES-1, R-ES-2).

## End of Spain VAT Return Skill v2.0

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture) AND `eu-vat-directive` v0.1 or later (Tier 2, EU directive content). Do not attempt to produce a Modelo 303 without all three files loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an Asesor Fiscal, Economista, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
