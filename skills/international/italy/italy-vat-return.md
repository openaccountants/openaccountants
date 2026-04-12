---
name: italy-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Italian VAT return (Liquidazione IVA Periodica / LIPE) for a self-employed individual or small business under the regime ordinario in Italy. Trigger on phrases like "prepare LIPE", "Italian VAT return", "Liquidazione IVA", "IVA italiana", "classify transactions for Italian VAT", or any request involving Italy VAT filing. This skill covers Italy only, regime ordinario (monthly or quarterly LIPE). Regime forfettario, regime dei minimi, split payment, margin schemes, and VAT groups are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Italian VAT work.
version: 2.0
---

# Italy VAT Return Skill (LIPE / Liquidazione IVA Periodica) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Italy (Repubblica Italiana) |
| Standard rate | 22% |
| Reduced rates | 10% (tourism, restaurants, renovation, certain foodstuffs), 5% (certain health/social services, selected food items), 4% (basic foodstuffs, printed books, first-home construction) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods) |
| Return form | LIPE (Comunicazione Liquidazioni Periodiche IVA, quarterly communication); annual Dichiarazione IVA |
| Filing portal | https://www.agenziaentrate.gov.it (Fatture e Corrispettivi / Fisconline) |
| Authority | Agenzia delle Entrate |
| Currency | EUR only |
| Filing frequencies | Monthly (turnover > €800,000 services / €800,000 goods in prior year); Quarterly (below thresholds, with 1% interest surcharge); Annual (Dichiarazione IVA by 30 April) |
| Deadline | LIPE: last day of 2nd month after quarter end (Q1 by 31 May, Q2 by 16 Sept, Q3 by 30 Nov, Q4 by 28 Feb); monthly: 16th of following month for payment |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants contributors |
| Validation date | April 2026 |

**Key LIPE fields (VP section — the fields you will use most):**

| Field | Meaning |
|---|---|
| VP2 | Total taxable transactions (imponibile) |
| VP3 | Total intra-EU acquisitions (imponibile) |
| VP4 | Total output VAT (IVA a debito) |
| VP5 | Total input VAT (IVA a credito) |
| VP6 | VAT payable or credit for the period |
| VP7 | Credit from prior period |
| VP8 | Credit from annual declaration used |
| VP9 | Advance payment (acconto) used |
| VP10 | Intra-EU purchases (acquisti intracomunitari) |
| VP11 | Imports (importazioni) |
| VP12 | Reverse charge purchases (acquisti con inversione contabile) |
| VP14 | Net amount due or credit |

**Registri IVA (VAT registers) — the backbone of Italian VAT:**

| Register | Purpose |
|---|---|
| Registro delle fatture emesse | Sales invoices issued |
| Registro degli acquisti | Purchase invoices received |
| Registro dei corrispettivi | Daily receipts (retail/hospitality) |

**Conservative defaults — Italy-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 22% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Italy |
| Unknown B2B vs B2C status for EU customer | B2C, charge 22% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (Art. 17 c.2 DPR 633/72) |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | €5,000 |
| HIGH tax-delta on a single conservative default | €400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | €10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Italian or international business bank: UniCredit, Intesa Sanpaolo, Banco BPM, Monte dei Paschi di Siena, BPER Banca, Poste Italiane (BancoPosta), Revolut Business, Wise Business, N26 Business, or any other.

**Recommended** — electronic invoices (fatture elettroniche) for the period from SDI (Sistema di Interscambio), purchase invoices for any input VAT claim above €400, the client's Partita IVA in writing (IT + 11 digits).

**Ideal** — complete SDI extract (XML), prior period LIPE, Registri IVA (fatture emesse + acquisti), reconciliation of VP7 credit brought forward.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all → hard stop. If bank statement only without invoices → proceed but record in the reviewer brief: "This LIPE was produced from bank statement alone. The reviewer must verify, before approval, that input VAT claims above €400 are supported by compliant fatture elettroniche received via SDI and that all reverse-charge classifications match the supplier's invoice."

### Italy-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-IT-1 — Regime forfettario.** *Trigger:* client is under the regime forfettario (flat-rate scheme, turnover below €85,000). *Message:* "Regime forfettario taxpayers do not charge IVA on their invoices and cannot recover input IVA. They do not file LIPE or the annual Dichiarazione IVA. This skill covers the regime ordinario only."

**R-IT-2 — Regime dei minimi.** *Trigger:* client is under the legacy regime dei minimi (contribuenti minimi). *Message:* "Regime dei minimi taxpayers have a simplified regime outside the ordinary IVA system. This skill covers the regime ordinario only."

**R-IT-3 — Split payment (scissione dei pagamenti).** *Trigger:* client's customers include Italian public administration bodies subject to split payment under Art. 17-ter DPR 633/72. *Message:* "Split payment (scissione dei pagamenti) for supplies to public administration requires specific treatment where the PA withholds IVA. This is complex and out of scope."

**R-IT-4 — Partial exemption (pro rata).** *Trigger:* client makes both taxable and exempt-without-credit supplies (financial, medical, educational) and the exempt proportion is not de minimis. *Message:* "You make both taxable and exempt supplies. Input IVA must be apportioned under the pro rata rule (Art. 19 and 19-bis DPR 633/72). Please use a commercialista to determine the pro rata."

**R-IT-5 — Margin scheme (regime del margine).** *Trigger:* client deals in second-hand goods, art, antiques, or collectables. *Message:* "Margin scheme transactions require transaction-level margin computation. Out of scope."

**R-IT-6 — VAT group (gruppo IVA).** *Trigger:* client is part of a VAT group under Art. 70-bis to 70-duodecies DPR 633/72. *Message:* "VAT groups require consolidation across the group. Out of scope."

**R-IT-7 — Fiscal representative (rappresentante fiscale).** *Trigger:* non-resident supplier or client with a fiscal representative in Italy. *Message:* "Non-resident registrations with fiscal representatives have specific obligations beyond this skill. Please use a commercialista."

**R-IT-8 — Income tax instead of IVA.** *Trigger:* user asks about annual income tax (IRPEF, IRES, Modello Redditi) instead of IVA. *Message:* "This skill only handles Italian VAT (IVA) returns. For income tax, use a dedicated Italian income tax skill."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules — the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Italian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| UNICREDIT, UNICREDIT SPA | EXCLUDE for bank charges/fees | Financial service, exempt (Art. 10 c.1 n.1 DPR 633/72) |
| INTESA SANPAOLO, INTESA SP | EXCLUDE for bank charges/fees | Same |
| BANCO BPM, BPM | EXCLUDE for bank charges/fees | Same |
| MONTE DEI PASCHI, MPS | EXCLUDE for bank charges/fees | Same |
| BPER BANCA | EXCLUDE for bank charges/fees | Same |
| POSTE ITALIANE, BANCOPOSTA | EXCLUDE for bank charges/fees | Same |
| CREDITO EMILIANO, CREDEM | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTERESSI, INTERESSE | EXCLUDE | Interest income/expense, out of scope |
| MUTUO, PRESTITO, FINANZIAMENTO | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Italian government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| AGENZIA ENTRATE, AGENZIA DELLE ENTRATE | EXCLUDE | Tax payment, not a supply |
| F24, MODELLO F24, PAGAMENTO F24 | EXCLUDE | Tax payment (IVA, IRPEF, INPS, IRAP) via F24 |
| INPS | EXCLUDE | Social security contributions (contributi previdenziali) |
| INAIL | EXCLUDE | Workplace insurance contributions |
| CAMERA DI COMMERCIO, CCIAA | EXCLUDE | Chamber of Commerce fees, government body |
| COMUNE DI, MUNICIPIO | EXCLUDE | Municipal fees/taxes |
| REGIONE, PROVINCIA | EXCLUDE | Regional/provincial government |
| EQUITALIA, AGENZIA RISCOSSIONE | EXCLUDE | Tax collection agency |
| DOGANA, AGENZIA DOGANE | EXCLUDE | Customs (but check for import IVA on C88 equivalent) |

### 3.3 Italian utilities

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| ENEL, ENEL ENERGIA, ENEL SERVIZIO | Domestic 22% | VP5 (input) | Electricity — standard rate overhead |
| ENI, ENI PLENITUDE | Domestic 22% or 10% | VP5 (input) | Gas: check invoice — domestic gas may be 10% (reduced) or 22% |
| EDISON, A2A, IREN, HERA | Domestic 22% | VP5 (input) | Utilities |
| ACEA | Domestic 22% or 10% | VP5 (input) | Water/electricity — water may be 10% |
| TIM, TELECOM ITALIA | Domestic 22% | VP5 (input) | Telecoms — overhead |
| VODAFONE IT, VODAFONE ITALIA | Domestic 22% | VP5 (input) | Telecoms |
| WIND TRE, WINDTRE | Domestic 22% | VP5 (input) | Telecoms |
| FASTWEB | Domestic 22% | VP5 (input) | Internet/telecoms |
| ILIAD | Domestic 22% | VP5 (input) | Mobile telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| GENERALI, ASSICURAZIONI GENERALI | EXCLUDE | Insurance, exempt (Art. 10 c.1 n.2) |
| ALLIANZ, ALLIANZ ITALIA | EXCLUDE | Same |
| UNIPOL, UNIPOLSAI | EXCLUDE | Same |
| AXA ITALIA | EXCLUDE | Same |
| CATTOLICA ASSICURAZIONI, ZURICH | EXCLUDE | Same |
| ASSICURAZIONE, POLIZZA | EXCLUDE | All insurance exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| POSTE ITALIANE (standard mail) | EXCLUDE for standard postage | | Universal postal service, exempt |
| POSTE ITALIANE (parcels, Poste Delivery) | Domestic 22% | VP5 | Non-universal services are taxable |
| SDA EXPRESS, BRT, BARTOLINI | Domestic 22% | VP5 | Express courier, taxable |
| DHL EXPRESS ITALIA | Domestic 22% | VP5 | Express courier |
| GLS ITALY, TNT ITALIA | Domestic 22% | VP5 | Courier |

### 3.6 Transport (Italy domestic)

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| TRENITALIA, ITALO, NTV | Domestic 10% | VP5 (input) | Rail transport at reduced rate |
| ATAC, ATM MILANO, GTT, ANM | Domestic 10% | VP5 (input) | Urban public transport, reduced rate |
| UBER IT, UBER ITALY | Domestic 10% (transport) | VP5 | Ride-hailing, transport reduced rate |
| TAXI, RADIOTAXI | Domestic 10% | VP5 | Local taxi, reduced rate |
| ALITALIA, ITA AIRWAYS (domestic) | Domestic 10% | VP5 | Domestic flights at 10% |
| ITA AIRWAYS, RYANAIR, EASYJET (international) | EXCLUDE / 0% | | International flights exempt |
| AUTOSTRADE, TELEPASS | Domestic 22% | VP5 | Motorway tolls at 22% |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| ESSELUNGA | Default BLOCK input VAT | Personal provisioning. Deductible only if hospitality/catering business. |
| CONAD, COOP, EUROSPIN, LIDL | Default BLOCK | Same |
| CARREFOUR ITALIA, PENNY, MD | Default BLOCK | Same |
| PAM, DESPAR, IPER | Default BLOCK | Same |
| RISTORANTE, TRATTORIA, PIZZERIA, BAR | Default BLOCK | Entertainment — see Section 5.12 |

### 3.8 SaaS — EU suppliers (reverse charge, Art. 17 c.2 / inversione contabile)

These are billed from EU entities (typically Ireland or Luxembourg) and trigger inversione contabile.

| Pattern | Billing entity | Field | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | VP3/VP10 + VP5 | Inversione contabile: output in VP4, input in VP5 |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | VP3/VP10 + VP5 | Inversione contabile |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | VP3/VP10 + VP5 | Inversione contabile |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | VP3/VP10 + VP5 | Inversione contabile |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | VP3/VP10 + VP5 | Inversione contabile |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | VP3/VP10 + VP5 | EU, inversione contabile |
| DROPBOX | Dropbox International Unlimited (IE) | VP3/VP10 + VP5 | Inversione contabile |
| SLACK | Slack Technologies Ireland Ltd (IE) | VP3/VP10 + VP5 | Inversione contabile |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | VP3/VP10 + VP5 | EU, inversione contabile |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | VP3/VP10 + VP5 | Inversione contabile |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | VP3/VP10 + VP5 | Transaction fees may be exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (reverse charge, Art. 17 c.2)

| Pattern | Billing entity | Field | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | VP3/VP10 + VP5 | LU entity → EU inversione contabile |
| NOTION | Notion Labs Inc (US) | VP11/VP12 + VP5 | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | VP11/VP12 + VP5 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | VP11/VP12 + VP5 | Non-EU reverse charge |
| GITHUB (standard plans) | GitHub Inc (US) | VP11/VP12 + VP5 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | VP11/VP12 + VP5 | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | VP11/VP12 + VP5 | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE) — check | VP11/VP12 or VP3/VP10 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | VP11/VP12 + VP5 | Non-EU reverse charge |

### 3.10 SaaS — the exception (NOT reverse charge)

| Pattern | Treatment | Why |
|---|---|---|
| AWS EMEA SARL | EU inversione contabile VP3/VP10 + VP5 (Luxembourg entity) | Standard EU reverse charge applies. If invoice shows Italian IVA charged, treat as domestic 22%. |

### 3.11 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (monthly subscription) | EU inversione contabile VP3/VP10 + VP5 | Stripe IE entity |
| SUMUP, SQUARE, ZETTLE | Check invoice | If Italian entity: domestic 22%; if IE/EU entity: inversione contabile |
| NEXI, SATISPAY | Check invoice | Italian payment processor — fees may be exempt or taxable |

### 3.12 Professional services (Italy)

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| COMMERCIALISTA, STUDIO COMMERCIALE | Domestic 22% | VP5 | Always deductible |
| AVVOCATO, STUDIO LEGALE | Domestic 22% | VP5 | Deductible if business legal matter |
| NOTAIO, STUDIO NOTARILE | Domestic 22% | VP5 | Notarial fees on business transactions |
| CONSULENTE DEL LAVORO | Domestic 22% | VP5 | Payroll consultant, deductible |
| ARCHITETTO, INGEGNERE, GEOMETRA | Domestic 22% | VP5 | Professional services |
| REGISTRO IMPRESE | EXCLUDE | Company registry fee, government body |

### 3.13 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| INPS, CONTRIBUTI INPS | EXCLUDE | Social security contributions |
| INAIL, PREMIO INAIL | EXCLUDE | Workplace insurance |
| STIPENDIO, SALARIO, BUSTA PAGA | EXCLUDE | Wages — outside IVA scope |
| TFR, TRATTAMENTO FINE RAPPORTO | EXCLUDE | Severance fund, out of scope |
| CASSA PREVIDENZA, ENPAM, CNPADC | EXCLUDE | Professional pension fund |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| AFFITTO COMMERCIALE, LOCAZIONE COMMERCIALE | Domestic 22% | Commercial lease where landlord opted to charge IVA |
| AFFITTO, LOCAZIONE (residential, no IVA) | EXCLUDE | Residential lease exempt |
| IMU, TASI | EXCLUDE | Property tax, not a supply |
| CONDOMINIO | EXCLUDE or Domestic 22% | Building management — check if IVA invoiced |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| GIROCONTO, BONIFICO INTERNO | EXCLUDE | Internal movement |
| TRASFERIMENTO TRA CONTI | EXCLUDE | Own-account transfer |
| DIVIDENDO | EXCLUDE | Dividend payment, out of scope |
| RATA MUTUO, RIMBORSO PRESTITO | EXCLUDE | Loan repayment, out of scope |
| PRELIEVO BANCOMAT, PRELIEVO CONTANTI | TIER 2 — ask | Default exclude; ask what cash was spent on |
| APPORTO PERSONALE, VERSAMENTO SOCIO | EXCLUDE | Owner injection |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of an Italy-based self-employed IT consultant (regime ordinario). They illustrate the trickiest cases.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.9). No IVA on the invoice. This is a service received from a non-EU supplier. The Italian client must self-assess IVA (inversione contabile / autofattura) under Art. 17 c.2 DPR 633/72. The client issues an autofattura, records output IVA in VP4 and input IVA in VP5. Net effect zero for a fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field (input) | Field (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.23 | 22% | VP5 | VP4 (via VP12) | N | — | — |

### Example 2 — EU service, inversione contabile (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`

**Reasoning:**
Google Ireland Limited is an IE entity — standard EU inversione contabile. Google Ads is a service. Output IVA in VP4, input IVA in VP5. Net → VP3/VP10. Both sides must appear. Net effect zero for a fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field (input) | Field (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 187.00 | 22% | VP5 | VP4 (via VP3) | N | — | — |

### Example 3 — Entertainment, partially recoverable in Italy

**Input line:**
`15.04.2026 ; RISTORANTE DA MARIO ROMA ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant transaction. In Italy, business entertainment (spese di rappresentanza) has complex deductibility rules. For IVA purposes, restaurant meals are deductible if they qualify as business expenses under Art. 19 DPR 633/72 and are properly documented with a fattura (not just a scontrino/receipt). The IVA deduction was restored by D.L. 112/2008, but personal meals remain blocked. Default: block, flag for reviewer. If confirmed as documented business expense with fattura → deductible at 10% (restaurant rate).

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RISTORANTE DA MARIO ROMA | -220.00 | -220.00 | 0 | — | — | Y | Q1 | "Restaurant: do you have a fattura (not scontrino)? Confirm business purpose." |

### Example 4 — Capital goods (bene strumentale)

**Input line:**
`18.04.2026 ; DELL ITALIA SRL ; DEBIT ; Invoice DEL2026-0041 Laptop XPS 15 ; -1,595.00 ; EUR`

**Reasoning:**
The gross amount is €1,595. In Italy, assets with a useful life beyond one year and value above €516.46 (net of IVA) are capitalised as beni strumentali. €1,595 / 1.22 = €1,307.38 > €516.46. This is a capital goods purchase. Input IVA is deductible (VP5) as for any business purchase. The distinction matters for income tax depreciation, not for IVA recovery — but flag it for proper registro dei beni ammortizzabili entry.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DELL ITALIA SRL | -1,595.00 | -1,307.38 | -287.62 | 22% | VP5 | N | — | — |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice IT-2026-018 IT consultancy March ; +3,500.00 ; EUR`

**Reasoning:**
Incoming €3,500 from a German company. B2B services: place of supply is the customer's country (Germany) under Art. 7-ter DPR 633/72 / Art. 44 VAT Directive. The client invoices without IVA with notation "Inversione contabile — Art. 196 Direttiva 2006/112/CE". Report as non-taxable (operazione non imponibile). Confirm: (a) customer is VAT-registered — verify German USt-IdNr on VIES; (b) invoice is correctly issued.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | n/a | VP2 (non-imp.) | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, partial recovery

**Input line:**
`28.04.2026 ; LEASYS SPA ; DEBIT ; Lease payment Fiat 500X ; -450.00 ; EUR`

**Reasoning:**
Car lease payment. In Italy, IVA on passenger vehicles is deductible at 40% if the vehicle is used for business (Art. 19-bis1 lett. c DPR 633/72). This is a partial deduction (not a full block as in Malta). The 40% is a legal presumption of business use. Full 100% deduction only applies to taxis, driving schools, car rental, and vehicles forming the core business asset. For an IT consultant: 40% deductible.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | LEASYS SPA | -450.00 | -368.85 | -81.15 (x 40% = -32.46 deductible) | 22% | VP5 (partial) | Y | Q3 | "Vehicle: 40% IVA deductible. Is this a core business vehicle (taxi/rental)?" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 22% (Art. 16 c.1 DPR 633/72)

Default rate. Sales → VP2/VP4. Purchases → VP5.

### 5.2 Reduced rate 10% (Table A, Part III, DPR 633/72)

Applies to: restaurants, hotels, renovation of residential buildings, certain food products (meat, fish, certain processed foods), passenger transport, cultural events. Sales → VP2/VP4. Purchases → VP5.

### 5.3 Reduced rate 5% (Table A, Part II-bis)

Applies to: certain health and social services, selected food items (herbs, spices), basilico, oregano. Very narrow. Sales → VP2/VP4. Purchases → VP5.

### 5.4 Super-reduced rate 4% (Table A, Part II)

Applies to: basic foodstuffs (bread, milk, olive oil, fresh fruit/vegetables), printed books and newspapers, first-home construction materials, medical devices for disabled persons. Sales → VP2/VP4. Purchases → VP5.

### 5.5 Zero rate and exempt with credit (non imponibile)

Exports outside EU → Art. 8 DPR 633/72 (non imponibile, requires export evidence). Intra-EU B2B supplies of goods → Art. 41 D.L. 331/93 (non imponibile, requires VIES verification). Intra-EU B2B services → Art. 7-ter (non imponibile, customer country rule).

### 5.6 Exempt without credit (esente Art. 10)

Medical services, education, insurance, financial services, residential rent, postal universal service. No output IVA, no input IVA deduction on related costs. If significant → **R-IT-4 refuses**.

### 5.7 Local standard purchases

Input IVA on a compliant fattura from an Italian supplier is deductible for purchases used in taxable business activity. Subject to blocked-input rules (5.12). Map to VP5.

### 5.8 Inversione contabile — EU services received (Art. 17 c.2 + Art. 7-ter)

EU supplier invoices at 0% with reverse-charge note: client issues autofattura or integrazione della fattura. Output IVA → VP4, input IVA → VP5. Net → VP3/VP10. Net effect zero for fully taxable client.

### 5.9 Inversione contabile — EU goods received

Physical goods from EU: integration of supplier invoice. Output IVA → VP4, input IVA → VP5. Net → VP3/VP10.

### 5.10 Inversione contabile — non-EU services and imports

Non-EU services: autofattura required. Output IVA and input IVA both self-assessed. → VP12/VP11 + VP4/VP5. Goods imports: since 2022, IVA on imports can be deferred to the LIPE (pre-liquidazione doganale).

### 5.11 Capital goods (beni strumentali)

Assets > €516.46 net: capitalize for income tax depreciation (registro beni ammortizzabili). For IVA purposes, input deduction follows the same rules as other purchases (VP5) — there is no separate IVA line for capital goods on the LIPE. The distinction matters for the annual Dichiarazione IVA and for the 5-year adjustment period (rettifica della detrazione, Art. 19-bis2).

### 5.12 Blocked input IVA (Art. 19-bis1 DPR 633/72)

- Motor vehicles (autovetture): 40% deductible (legal presumption). 100% for taxis, driving schools, car rental, vehicles as core business tools.
- Fuel (carburante): 40% deductible for vehicles at 40%; 100% for fully deductible vehicles. Must be paid via traceable means (no cash).
- Entertainment (spese di rappresentanza): IVA deductible if proper fattura obtained and expense is proportionate to business. Meals and accommodation deductible with fattura since D.L. 112/2008.
- Accommodation (alberghi): IVA deductible since D.L. 112/2008 if documented with fattura and for business.
- Personal use items: not deductible.
- Phone/telecoms: 50% deductible (Art. 19-bis1 lett. d) — overridable if exclusively business.
- Gifts: IVA deductible only if unit cost ≤ €50.

### 5.13 Quarterly interest surcharge

Quarterly filers must add 1% interest on the net IVA payable for the quarter (Art. 7 DPR 542/99). This interest goes on the LIPE as an additional amount. Monthly filers do not pay this surcharge.

### 5.14 Sales — local domestic (any rate)

Charge 22%, 10%, 5%, or 4% as applicable. All via fattura elettronica through SDI.

### 5.15 Sales — cross-border B2C

Goods to EU consumers above €10,000 EU-wide threshold → **R-EU-5 (OSS refusal)**. Below threshold → Italian IVA at applicable rate.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* ENI, Q8, IP, ESSO, SHELL, fuel receipts. *Why insufficient:* 40% vs 100% deduction depends on vehicle type. *Default:* 40% recovery. *Question:* "Is this a core business vehicle (taxi/rental) or a standard company car?"

### 6.2 Restaurants and entertainment

*Pattern:* any named ristorante, trattoria, pizzeria, bar. *Why insufficient:* IVA on meals is deductible only with a fattura (not scontrino). *Default:* block. *Question:* "Do you have a fattura elettronica (not just a scontrino) for this meal? Was it a business expense?"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, Adobe, Meta, etc. *Default:* non-EU reverse charge (VP11/VP12 + VP5). *Question:* "Could you check the invoice? I need the legal entity name and country."

### 6.4 Round-number incoming transfers from owner-named counterparties

*Default:* exclude as owner injection. *Question:* "The €X transfer from [name] — customer payment, own money, or loan?"

### 6.5 Incoming transfers from individual names (not owner)

*Default:* domestic B2C sale at 22%. *Question:* "Was it a sale? Business or consumer?"

### 6.6 Incoming transfers from foreign counterparties

*Default:* domestic 22%. *Question:* "B2B with Partita IVA, B2C, goods or services, which country?"

### 6.7 Large one-off purchases (potential beni strumentali)

*Pattern:* near €516.46 threshold. *Default:* if net > €516.46 → capital goods. *Question:* "Confirm total invoice amount."

### 6.8 Mixed-use phone, internet

*Pattern:* TIM, Vodafone, WindTre personal lines. *Default:* 50% deductible (Art. 19-bis1 lett. d). *Question:* "Is this a dedicated business line or mixed-use?"

### 6.9 Outgoing transfers to individuals

*Default:* exclude as drawings. *Question:* "Contractor payment, wages, refund, or personal?"

### 6.10 Cash withdrawals

*Pattern:* prelievo bancomat, prelievo contanti. *Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* affitto, locazione, canone. *Default:* no IVA (residential default). *Question:* "Commercial or residential? Does the landlord charge IVA?"

### 6.12 Foreign hotel and accommodation

*Default:* exclude from input IVA. *Question:* "Business trip?" (Income tax deduction possible.)

### 6.13 Airbnb income

*Default:* [T2] flag. *Question:* "Short-term tourist rental? Duration? Cedolare secca applied?"

### 6.14 Domestic reverse charge (construction, cleaning)

*Pattern:* payments to subcontractors in construction and cleaning sectors. *Why insufficient:* Italy has broad domestic reverse charge (Art. 17 c.6 DPR 633/72) for construction subcontracting, building cleaning, and energy sector. *Default:* [T2] flag. *Question:* "Is this a domestic reverse charge sector (construction/cleaning)?"

### 6.15 Platform sales

*Default:* if selling EU cross-border above €10,000 → R-EU-5. Otherwise: domestic 22% for sales; platform fees as EU inversione contabile. *Question:* "Do you sell to buyers outside Italy?"

---

## Section 7 — Excel working paper template (Italy-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Italy-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Field code") accepts VP field codes from Section 1 of this skill. For inversione contabile transactions, enter both input and output fields separated by a slash.

### Sheet "Field Summary"

One row per VP field. Mandatory rows:

```
| VP2 | Total taxable operations | =SUMIFS(Transactions!E:E, ...) |
| VP3 | Intra-EU acquisitions | =SUMIFS(Transactions!E:E, ..., "VP3") |
| VP4 | Total output IVA | =SUM(output VAT on all taxable and RC lines) |
| VP5 | Total input IVA | =SUM(input VAT on all deductible lines) |
| VP6 | Net IVA for period | =VP4-VP5 |
| VP7 | Credit from prior period | (manual entry) |
| VP10 | Intra-EU purchases | =VP3 |
| VP11 | Imports | =SUMIFS(..., "VP11") |
| VP12 | Reverse charge purchases | =SUMIFS(..., "VP12") |
| VP14 | Net amount due/credit | =VP6-VP7-VP8-VP9 |
```

### Sheet "Return Form"

Final LIPE-ready figures.

```
IF VP5 > VP4:
  VP6 = credit (credito)
  VP14 = credit after adjustments
ELSE:
  VP6 = payable (debito)
  VP14 = net payable + 1% interest (if quarterly)
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/italy-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Italian bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Italy-specific patterns.

**CSV format conventions.** Italian banks typically export in CSV or Excel with DD/MM/YYYY dates. Common columns: Data, Descrizione/Causale, Dare (debit), Avere (credit), Saldo. UniCredit and Intesa exports include ABI causale codes (e.g., 27 = bonifico, 48 = carta di credito).

**Italian language variants.** Affitto (rent), stipendio (salary), interessi (interest), bonifico (transfer), contributi (contributions), fattura (invoice), rimborso (refund), versamento (deposit), prelievo (withdrawal). Treat as English equivalents.

**ABI causale codes.** 27 = bank transfer (bonifico), 48 = credit card, 05 = direct debit (RID/SDD), 26 = cheque. The code helps classify.

**Internal transfers and exclusions.** Giroconto = internal transfer. Always exclude.

**F24 payments.** Tax payments via F24 (modello F24) appear as "PAGAMENTO F24" or with specific tax codes (6001-6012 for monthly IVA, 6031-6034 for quarterly IVA). Always exclude.

**Fattura elettronica (SDI).** Since 2019, all B2B invoices in Italy must be electronic via SDI. If the client has an SDI extract, it provides the most reliable data source for IVA classification — prefer over bank statement for invoice details.

**Foreign currency transactions.** Convert to EUR at the ECB rate or bank statement rate.

**IBAN country prefix.** IT = Italy. IE, LU, NL, FR, DE = EU. US, GB, AU, CH = non-EU.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference rule:* SRL, SPA, SAS = company; ditta individuale = sole trader; libero professionista = freelance professional. *Fallback:* "Ditta individuale, SRL, or libero professionista?"

### 9.2 VAT regime
*Inference rule:* if filing LIPE, they are regime ordinario. *Fallback:* "Are you under regime ordinario or regime forfettario?"

### 9.3 Partita IVA
*Inference rule:* IT-format P.IVA on invoices. *Fallback:* "What is your Partita IVA? (IT + 11 digits)"

### 9.4 Filing period and frequency
*Inference rule:* date range on statement. *Fallback:* "Which period? Monthly or quarterly filer?"

### 9.5 Industry and sector
*Inference rule:* counterparty mix. *Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* INPS outgoing. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Inference rule:* medical/financial/educational income. *Fallback:* "Do you make any exempt sales?" *If yes → R-IT-4 refuses.*

### 9.8 Credit carried forward
*Inference rule:* not inferable. Always ask. *Question:* "Do you have IVA credit from the prior period? (VP7)"

### 9.9 Cross-border customers
*Inference rule:* foreign IBANs. *Fallback:* "Customers outside Italy? EU or non-EU? B2B or B2C?"

### 9.10 Public administration customers
*Inference rule:* payments from PA-sounding entities. *Conditional fallback:* "Do you supply to Italian public administration?" *If yes → R-IT-3 (split payment) refuses.*

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, written in April 2026 to align with the three-tier Accora architecture.

### Sources

**Primary legislation:**
1. DPR 633/72 (Decreto IVA) — the core Italian VAT law
2. D.L. 331/93 — intra-EU transactions
3. DPR 542/99 — quarterly filing and interest surcharge

**Agenzia delle Entrate guidance:**
4. LIPE form and completion instructions — https://www.agenziaentrate.gov.it
5. Fatturazione elettronica guidance
6. Circular letters on reverse charge and domestic inversione contabile

**EU directive:**
7. Council Directive 2006/112/EC — via eu-vat-directive companion skill
8. Council Implementing Regulation 282/2011

**Other:**
9. VIES validation — https://ec.europa.eu/taxation_customs/vies/
10. ECB euro reference rates

### Known gaps

1. Supplier pattern library does not cover every Italian SME.
2. Split payment (scissione dei pagamenti) for PA customers is out of scope — R-IT-3 refuses.
3. Domestic reverse charge (Art. 17 c.6) is flagged T2 only.
4. Capital goods threshold (€516.46 net) is per current guidance — verify annually.
5. Motor vehicle 40% presumption may change — verify annually.
6. Restaurant IVA deductibility requires fattura (not scontrino) — skill flags but cannot verify document type.
7. Quarterly 1% interest surcharge calculation is approximate.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. 10 sections. Country-specific supplier pattern library.
- **v1.0:** Initial skill.

### Self-check (v2.0)

1. Quick reference at top: yes (Section 1).
2. Supplier library: yes (Section 3, 15 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules: yes (Section 5, 15 rules).
5. Tier 2 catalogue: yes (Section 6, 15 items).
6. Excel template: yes (Section 7).
7. Onboarding fallback: yes (Section 9, 10 items).
8. All 8 Italy-specific refusals: yes (Section 2).
9. Reference material: yes (Section 10).
10. Motor vehicle 40% partial deduction (key Italy difference): yes (Section 5.12 + Example 6).
11. Restaurant fattura requirement: yes (Section 5.12 + Example 3).
12. Fattura elettronica / SDI requirement: yes (Section 8).
13. Quarterly 1% interest surcharge: yes (Section 5.13).
14. Non-EU SaaS autofattura: yes (Example 1).
15. Domestic reverse charge flagged: yes (Section 6.14).

## End of Italy VAT Return Skill v2.0

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` v0.1 or later AND `eu-vat-directive` v0.1 or later.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista, revisore legale, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
