---
name: italy-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Italian VAT return (Liquidazione IVA Periodica / LIPE) for a self-employed individual or very small business operating under the ordinary VAT regime (regime ordinario) in Italy. Trigger on phrases like "prepare LIPE", "Italian VAT return", "Liquidazione IVA", "classify transactions for Italy", "IVA italiana", "autoliquidazione", "cessione intracomunitaria", "reverse charge Italia", or any request involving Italian VAT filing. This skill covers Italy only and only the regime ordinario. Regime forfettario, regime dei minimi, split payment to public administration, margin schemes, travel agents, agricultural flat rate, the annual Dichiarazione IVA, partial exemption (pro rata), and VAT groups (gruppo IVA) are all in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.2.0 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Italian VAT work.
version: 0.1
---

# Italy VAT Return Skill (LIPE, Regime Ordinario) v0.1

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Italy |
| Return form | LIPE (Liquidazione IVA Periodica) — the periodic VAT settlement |
| Tax | IVA (Imposta sul Valore Aggiunto) — the Italian name for VAT |
| Governing law | D.P.R. 26 ottobre 1972 n. 633 (the Italian VAT law) |
| Authority | Agenzia delle Entrate (national tax authority) |
| Filing portal | Fisconline (individuals) / Entratel (intermediaries) — https://www.agenziaentrate.gov.it |
| Currency | EUR only |
| Standard rate | 22% |
| Reduced rates | 10%, 5%, 4% |
| Filing frequencies | Monthly (turnover > €800,000 services / > €700,000 goods), Quarterly (below those thresholds, by election) |
| Deadline | Monthly: 16th of the second month after the period. Quarterly: 16th of the second month after the quarter, with the fourth quarter LIPE replaced by the annual return (Dichiarazione IVA) filed by 30 April |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.2.0 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |

**Key LIPE fields (the boxes you will use most):**

| Field | Meaning |
|---|---|
| VP1 | Reference period (month or quarter) |
| VP2 | Total taxable operations (output side, excluding reverse charge) |
| VP3 | Total purchases and imports (input side) |
| VP4 | IVA a debito (output VAT, including self-assessed from reverse charge) |
| VP5 | IVA a credito (input VAT deductible) |
| VP6 | IVA dovuta (VAT due = VP4 − VP5) or IVA a credito (credit = VP5 − VP4) |
| VP7 | Previous period credit carried forward |
| VP8 | Periodic settlement result (positive = payable, negative = credit) |
| VP13 | Metodo previsionale / storico (only used for the December LIPE of quarterly filers) |
| VP14 | IVA versata (VAT actually paid) |

**USt-IdNr equivalent — Partita IVA format:** IT + 11 digits (e.g., IT12345678901). The first 7 digits identify the taxpayer, digits 8-10 identify the issuing tax office, digit 11 is a check digit per the Luhn-like algorithm specified in D.M. 23/12/1976.

**Refusal catalogue quick index:** R-IT-1 through R-IT-13 in Section 2.

**Conservative defaults — Italy-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Category | Default | Italian-specific note |
|---|---|---|
| Unknown rate on a sale | 22% | Standard rate, regime ordinario |
| Unknown VAT status of a purchase | Not deductible | Requires invoice compliant with art. 21 D.P.R. 633/72 |
| Unknown counterparty country | Italy domestic | If IBAN starts with anything other than IT or if counterparty name is foreign, re-check |
| Unknown customer status (B2B vs B2C) | B2C with 22% | Applies the conservative customer-side treatment |
| Unknown vehicle business use | 40% deductible | Art. 19-bis1 D.P.R. 633/72 — statutory 40% cap on most mixed-use vehicles (cars, motorcycles, mopeds) regardless of actual business use percentage |
| Unknown business meal (rappresentanza) | Blocked unless documentable business purpose | Art. 19-bis1(h) — entertainment expenses partially deductible, but the skill defaults to blocked |
| Unknown restaurant/bar expense | Blocked by default | Requires identification as either "spesa di rappresentanza" (limited) or "spesa per vitto e alloggio" (generally fully deductible if in business trip context) |
| Gift to customer | Blocked if unit value > €50 | Art. 19-bis1(h) — gift threshold |
| Telephone / mobile | 50% deductible cap | Statutory cap for mobile phones used partly for business |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

- Single transaction HIGH threshold: €5,000
- Tax delta HIGH threshold: €500
- Period total HIGH threshold: €50,000

## Section 2 — Italy-specific refusal catalogue (R-IT-1 through R-IT-13)

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation. Refusal is a safety mechanism.

**R-IT-1 — Regime forfettario.**
*Condition.* The user indicates they operate under the regime forfettario (the Italian flat-rate scheme for small businesses with turnover up to €85,000).
*Reason.* Regime forfettario taxpayers do not charge VAT on their invoices, do not recover input VAT, do not file LIPE returns, and have a completely different tax computation based on activity coefficients. This skill targets the regime ordinario and cannot produce a forfettario return.
*Message.* "You operate under the regime forfettario, which is an entirely different tax regime from the one this skill handles. Regime forfettario taxpayers do not file LIPE returns — instead, they report their turnover annually through the Dichiarazione dei Redditi (Quadro LM) and pay a flat substitutive tax based on their activity coefficient. You need a commercialista familiar with the forfettario regime, or you can handle the simpler annual filing yourself via the Agenzia delle Entrate portal. This skill cannot help with forfettario compliance."

**R-IT-2 — Regime dei minimi (legacy).**
*Condition.* The user indicates they operate under the old regime dei minimi (effective 2008-2015, grandfathered for some taxpayers).
*Message.* "You operate under the legacy regime dei minimi, which has been closed to new entrants since 2015 but grandfathered for some taxpayers. This regime has its own separate rules and this skill does not handle it. You need a commercialista with specific experience in the regime dei minimi."

**R-IT-3 — Split payment (scissione dei pagamenti).**
*Condition.* The user makes supplies to Italian public administration (PA), listed companies on the FTSE MIB, or other entities subject to split payment under art. 17-ter D.P.R. 633/72.
*Reason.* Split payment is a unique Italian mechanism where the customer (public administration or listed company) pays the net amount to the supplier and the VAT directly to the Erario. The supplier issues an invoice with VAT shown but does not receive the VAT. The accounting treatment, the LIPE reporting, and the cash flow implications are all non-standard.
*Message.* "Some of your customers appear to be public administration entities or listed companies subject to split payment (scissione dei pagamenti) under art. 17-ter D.P.R. 633/72. Split payment has specialized rules about how VAT is invoiced, reported, and paid that this skill does not handle. You need a commercialista with public-administration billing experience."

**R-IT-4 — E-invoicing non-compliance (Sistema di Interscambio).**
*Condition.* The user indicates they are not operating via the Sistema di Interscambio (SdI) for electronic invoicing, or the bank statement shows business activity that would require SdI compliance but no corresponding SdI infrastructure is mentioned.
*Reason.* Since 1 January 2019, electronic invoicing via SdI is mandatory for almost all B2B and B2G transactions, and since 1 July 2022 extended to regime forfettario taxpayers with turnover > €25,000, and since 1 January 2024 extended to all regime forfettario taxpayers regardless of turnover. A business that is not SdI-compliant is either operating illegally or the profile inference has misidentified the business. Either way, this skill cannot proceed until SdI compliance is confirmed.
*Message.* "Since 2019, Italian businesses are required to issue invoices through the Sistema di Interscambio (SdI) for B2B and B2G transactions. If you are not currently using SdI or an accredited intermediary (commercialista, software provider), you cannot legally issue invoices and this skill cannot prepare a LIPE for you. You need to set up SdI access through your commercialista or a certified e-invoicing provider before any VAT return can be filed. This is not optional — it is a legal requirement. Contact the Agenzia delle Entrate or a commercialista to get set up."

**R-IT-5 — Partial exemption (pro rata).**
*Condition.* The user makes both taxable and exempt supplies (esenti under art. 10 D.P.R. 633/72) that are not de minimis.
*Reason.* Italian partial exemption uses the pro-rata method under art. 19-bis D.P.R. 633/72, with different calculation rules from the directive's default. Sector-specific rules apply.
*Message.* "Your business makes both taxable and exempt supplies (operazioni esenti), which requires pro-rata calculation of deductible input VAT under art. 19-bis D.P.R. 633/72. The pro-rata calculation is complex, sector-specific, and requires annual adjustment. This skill cannot handle pro-rata. You need a commercialista to set up the pro-rata methodology before filing LIPE returns."

**R-IT-6 — Margin schemes (regime del margine).**
*Condition.* The user resells second-hand goods, art, or collectors' items under the margin scheme.
*Message.* "Your business involves the resale of second-hand goods, works of art, or collectors' items under the regime del margine (art. 36-40 D.L. 41/1995). This scheme requires item-by-item margin tracking that cannot be derived from a bank statement. You need a commercialista familiar with the margin scheme."

**R-IT-7 — Travel agents (regime agenzie di viaggio).**
*Condition.* The user operates a travel agency reselling travel and accommodation under art. 74-ter D.P.R. 633/72.
*Message.* "Your business is subject to the regime agenzie di viaggio under art. 74-ter, which has specialized VAT rules quite different from standard IVA. This skill cannot handle the travel agents margin scheme."

**R-IT-8 — Agricultural flat rate (regime speciale agricoltura).**
*Condition.* The user operates under the agricultural flat-rate scheme (art. 34 D.P.R. 633/72).
*Message.* "You operate under the regime speciale agricoltura, which has its own input VAT recovery mechanics based on compensation percentages rather than actual input VAT. This skill cannot handle the agricultural flat rate. You need a commercialista with agricultural sector experience."

**R-IT-9 — VAT group (gruppo IVA).**
*Condition.* The user is part of a gruppo IVA under art. 70-bis ff. D.P.R. 633/72.
*Message.* "Your business is part of a gruppo IVA (Italian VAT group), where multiple related entities are treated as a single taxable person for IVA purposes. The group return is prepared by the representing entity and involves intra-group transaction handling that this skill does not support. You need the group representative's commercialista."

**R-IT-10 — Annual VAT return (Dichiarazione IVA).**
*Condition.* The user asks for help with the annual Dichiarazione IVA rather than a periodic LIPE.
*Reason.* The annual Dichiarazione IVA is a substantially more complex filing than the LIPE, with reconciliation of all periodic settlements, multiple quadri (VE, VF, VG, VH, VJ, VL, VX, etc.), and integration with the corporate income tax return. v0.1 of this skill handles only the LIPE.
*Message.* "The annual Dichiarazione IVA is more complex than the periodic LIPE and requires reconciliation of all periods plus integration with your overall tax position. This skill version (v0.1) handles only the periodic LIPE. For the annual Dichiarazione IVA, you need a commercialista or a more complete version of this skill. The annual return is due by 30 April of the year following the tax year."

**R-IT-11 — Construction reverse charge (reverse charge edilizia).**
*Condition.* The user is a construction subcontractor or contractor subject to the internal reverse charge under art. 17, c. 6, lett. a) D.P.R. 633/72.
*Message.* "You operate in the construction sector with reverse charge obligations between contractor and subcontractor. The Italian construction reverse charge has strict conditions about when it applies, how invoices must be issued, and how it interacts with split payment when the final customer is public administration. This skill does not handle construction reverse charge. You need a commercialista with construction sector experience."

**R-IT-12 — Import via postponed accounting.**
*Condition.* The user imports goods from outside the EU and uses postponed accounting.
*Reason.* Italy operates a partial postponed accounting regime for imports (reverse charge for certain goods via the importer's VAT identification), with specific rules that differ from other EU member states.
*Message.* "Your business imports goods from outside the EU and appears to use postponed accounting (reverse charge all'importazione). The Italian rules around which imports qualify for postponed accounting vs cash payment at the border are complex and fact-specific. This skill cannot reliably distinguish between the two treatments from a bank statement alone. You need a commercialista with import/export experience, or you need to provide the actual customs documents (bolle doganali) rather than just the bank statement."

**R-IT-13 — Cash accounting election (IVA per cassa).**
*Condition.* The user operates under the IVA per cassa regime (cash accounting for VAT) under art. 32-bis D.L. 83/2012.
*Reason.* Under IVA per cassa, output VAT becomes due when the customer pays (not when the invoice is issued) and input VAT is recoverable when the supplier is paid (not when the invoice is received). This shifts the entire classification from accrual to cash basis and the bank statement becomes the primary data source in a way it is not under ordinary regime. The LIPE reporting is also different.
*Message.* "You operate under the IVA per cassa regime, where VAT follows cash movements rather than invoice dates. This is a substantially different basis of accounting and this skill version (v0.1) assumes the ordinary accrual basis. For IVA per cassa returns, you need a commercialista familiar with the regime or a later version of this skill."

## Section 3 — Italian supplier pattern library (literal lookup table)

When you encounter these counterparties, apply the treatment indicated. Do not second-guess the table. The table is derived from public corporate disclosures and Italian tax authority guidance as of v0.1; reviewer must confirm for high-value transactions.

### 3.1 — Italian telecommunications

| Supplier | Typical IBAN / context | Treatment |
|---|---|---|
| TIM S.p.A. (Telecom Italia) | IT IBAN | Domestic 22% business line — mobile mixed-use defaults to 50% cap under art. 19-bis1(g); fixed line "ufficio" in description → 100% business recovery at 22% |
| Vodafone Italia S.p.A. | IT IBAN | Same as TIM |
| WindTre S.p.A. | IT IBAN | Same as TIM |
| Fastweb S.p.A. | IT IBAN | Same as TIM; note Fastweb is owned by Swisscom but bills from Italy |
| Iliad Italia S.p.A. | IT IBAN | Same as TIM — low-cost mobile operator with Italian VAT registration |

### 3.2 — Italian energy, water, and utilities

| Supplier | Treatment |
|---|---|
| Enel Energia S.p.A. | Domestic 22% electricity — but note Enel offers multiple rate classes, residential invoices are 10% reduced rate, business invoices are 22% |
| ENI Gas e Luce | Domestic gas supply — 10% reduced rate for residential, 22% for non-residential |
| A2A S.p.A. (Milan utility) | Domestic 22% for business, 10% for residential |
| Hera S.p.A. (Emilia-Romagna utility) | Same structure as A2A |
| ACEA S.p.A. (Rome utility) | Same structure |
| Iren S.p.A. (Liguria/Piemonte utility) | Same structure |

### 3.3 — Italian banks and financial services

| Supplier | Treatment |
|---|---|
| Intesa Sanpaolo | Bank fees — exempt under art. 10 D.P.R. 633/72 (EU Article 135). Excluded from LIPE as esenti. No input VAT to recover. |
| UniCredit S.p.A. | Same as Intesa |
| Banca Nazionale del Lavoro (BNL) | Same |
| Banco BPM S.p.A. | Same |
| Mediobanca, Monte dei Paschi, Credem, Banca Popolare di Sondrio, etc. | Same — all Italian banks follow the art. 10 exemption for their core banking services |
| Poste Italiane — BancoPosta services | Same — banking services exempt |

### 3.4 — Italian insurance

| Supplier | Treatment |
|---|---|
| Generali Italia S.p.A. | Insurance premiums — exempt art. 10 D.P.R. 633/72 (EU Article 135). Excluded from LIPE. No input VAT. |
| Allianz S.p.A. | Same |
| AXA Assicurazioni | Same |
| UnipolSai | Same |
| Reale Mutua | Same |

### 3.5 — Italian tax authority and statutory bodies

| Supplier / Counterparty | Treatment |
|---|---|
| Agenzia delle Entrate (tax payments) | Excluded — tax authority payment, not a supply. Flag for reviewer if unusual amount. |
| INPS (Istituto Nazionale della Previdenza Sociale) | Excluded — statutory social security contributions, outside VAT scope |
| INAIL (workplace accident insurance) | Excluded — statutory insurance, outside VAT scope |
| Equitalia / Agenzia delle Entrate-Riscossione | Excluded — tax collection agency |
| Camera di Commercio (Chamber of Commerce) — diritto annuale | Excluded — statutory contribution to a public-law body, NOT subject to VAT. Do NOT claim input VAT on Camera di Commercio annual fees regardless of invoice format. |
| Ordini professionali (professional orders — Ordine dei Dottori Commercialisti, Ordine degli Avvocati, etc.) — annual dues | Excluded — statutory contribution to a public-law professional order, outside VAT scope |
| Comune (municipal taxes — IMU, TARI, TASI) | Excluded — local taxes, outside VAT scope |

### 3.6 — Italian postal service

| Supplier | Treatment |
|---|---|
| Poste Italiane — universal postal service (francobolli, raccomandate ordinarie) | Exempt under art. 10 D.P.R. 633/72 universal service exemption. No VAT, no input VAT. |
| Poste Italiane — courier services (Poste Delivery, SDA) | Domestic 22% standard rate — competitive courier services are NOT part of the universal service exemption |
| BRT (Bartolini) | Domestic 22% |
| GLS Italy | Domestic 22% |
| DHL Express (Italia) | Domestic 22% if billed via DHL Italy; if billed from DE via DHL International, EU reverse charge autoliquidazione |
| TNT (now FedEx) | Similar — check billing entity on invoice |

### 3.7 — Italian public transport and rail

| Supplier | Treatment |
|---|---|
| Trenitalia (Frecciarossa, Frecciargento, Frecciabianca, Intercity, Regionale) | Domestic 10% reduced rate under Tabella A Parte III (passenger transport) |
| Italo - Nuovo Trasporto Viaggiatori | Same 10% |
| ATM (Azienda Trasporti Milanesi) — Milan metro/bus | 10% reduced rate — public transport |
| ATAC S.p.A. (Rome metro/bus) | Same 10% |
| ANM (Napoli) | Same 10% |
| Autostrade per l'Italia — toll charges | Domestic 22% — road tolls, fully deductible if business use |
| ENAV / Italian airport charges (via airline invoice) | Generally embedded in airline ticket; see 3.8 |

### 3.8 — Airlines and air transport

| Supplier | Treatment |
|---|---|
| ITA Airways (Italia Trasporto Aereo) | International flights exempt under art. 9 D.P.R. 633/72; domestic Italian flights 10% reduced rate |
| Ryanair | International — exempt art. 9; domestic — 10% but Ryanair billing entity is often Irish, check invoice |
| easyJet | Similar — check billing entity (Swiss, UK, or Italian sub) |
| Alitalia (legacy, ceased operations October 2021) | n/a, but may appear in historical statements — same treatment as ITA |
| Lufthansa / Air France / KLM for flights departing from Italy | Generally billed from the home country; place of supply rules for passenger transport apply — Italian portion potentially taxable, foreign portion generally exempt |

### 3.9 — Italian hotels, restaurants, and hospitality

| Category | Treatment |
|---|---|
| Italian hotels (business travel) | 10% reduced rate on accommodation; 22% on ancillary services (minibar, spa, parking). For LIPE purposes apply conservative 10% on full gross unless invoice breaks out ancillaries. Input VAT recoverable if the trip is documented business purpose. |
| Italian restaurants (business meal / "trasferta") | 10% reduced rate on food and non-alcoholic beverages. Input VAT recoverable at 75% for "spese di rappresentanza" (entertainment) if documented; 100% for "vitto e alloggio during transferte" (business trip meals) if documented. Default for unclear cases: blocked. |
| Bar / caffetteria | 10% — but often unclear business purpose; default to blocked for single-transaction bar receipts. |
| Italian Airbnb bookings | Via Airbnb Ireland UAC — EU reverse charge on the service fee. The accommodation itself is typically billed by the Italian host (if VAT-registered) or outside VAT (if below registration threshold). Check the invoice. |

### 3.10 — Italian supermarkets and food retail

| Supplier | Treatment |
|---|---|
| Esselunga | Mixed — food is 4%/10% reduced rates, non-food household items 22%. Default to blocked for single-transaction supermarket purchases (assume private provisioning) unless clear business purpose in description. |
| Conad, Coop, Carrefour Italia, Lidl Italia, Eurospin, PAM | Same treatment as Esselunga — default blocked |
| Metro Italia Cash & Carry | Mixed food/non-food, but Metro is a business-to-business wholesaler so the presumption shifts slightly toward business purpose; still default blocked without specific description |

### 3.11 — Fuel stations

| Supplier | Treatment |
|---|---|
| Eni Station, Agip, Q8, IP, Esso Italia, Tamoil | Domestic 22% on fuel. BUT vehicle input VAT is capped at 40% under art. 19-bis1(c) D.P.R. 633/72 for cars, motorcycles, and mopeds regardless of actual business use, unless the vehicle is exclusively used for business and this is documented. Default to 40% deductible. Trucks and commercial vehicles (autocarri) get 100% deduction if used 100% business. |

### 3.12 — Universal SaaS suppliers (EU reverse charge — autoliquidazione)

These are the same universal patterns that appear in Germany and other EU countries. The treatment is EU reverse charge (autoliquidazione under art. 17, c. 2 D.P.R. 633/72): the supplier does not charge IVA, the user self-accounts for 22% output IVA (reported in VP4 on the LIPE) and simultaneously claims 22% input IVA (reported in VP5 on the LIPE), net cash effect zero.

| Supplier | Billing entity | Treatment |
|---|---|---|
| Google Ireland Ltd | IE IBAN | EU autoliquidazione 22% — Google Ads, Google Workspace, Google Cloud (EMEA) |
| Microsoft Ireland Operations | IE IBAN | EU autoliquidazione 22% — Microsoft 365, Azure, GitHub Enterprise |
| Adobe Systems Software Ireland | IE IBAN | EU autoliquidazione 22% — Creative Cloud, Acrobat |
| LinkedIn Ireland Unlimited | IE IBAN | EU autoliquidazione 22% |
| Meta Platforms Ireland | IE IBAN | EU autoliquidazione 22% — Facebook Ads, Instagram Ads |
| Slack Technologies Ireland | IE IBAN | EU autoliquidazione 22% |
| Dropbox International | IE IBAN | EU autoliquidazione 22% |
| Atlassian Pty (Ireland) | IE IBAN | EU autoliquidazione 22% — Jira, Confluence |
| Stripe Payments Europe | IE IBAN | EU autoliquidazione 22% — Stripe platform fees |
| Uber BV | NL IBAN | EU autoliquidazione 22% — Uber ride bookings and Uber for Business |
| Zoom Video Communications | US entity billing EU | Non-EU reverse charge art. 17 c. 2 — autoliquidazione 22% |
| Fiverr International | Israeli entity | Non-EU reverse charge art. 17 c. 2 — autoliquidazione 22% |

### 3.13 — AWS (the branch-billing exception)

AWS EMEA SARL bills most EU customers through local branches with local VAT registration. For Italian customers, the billing entity may be "AWS EMEA SARL Italy Branch" or similar, with an Italian partita IVA and 22% IVA charged on the invoice. **If the IBAN is Italian and the invoice shows Italian IVA, treat as domestic 22% (not as reverse charge).** If the IBAN is Luxembourg and the invoice shows no VAT with a reverse-charge note, treat as EU autoliquidazione. This is the same exception structure as the German AWS case and it is the most common misclassification trap in Italian SaaS billing. Always check the invoice rather than defaulting to one treatment or the other.

### 3.14 — Apple and consumer-tier app stores

| Supplier | Treatment |
|---|---|
| Apple Distribution International (Ireland) — Apple One, iCloud+, App Store | Check billing entity on invoice. Apple One Premier and consumer subscriptions billed on a personal Apple ID are typically personal expenses — default to excluded. Apple Business Essentials billed on a business account with partita IVA is a B2B service — EU autoliquidazione 22%. The default for ambiguous Apple One lines is excluded as personal. |
| Google Play Store consumer purchases | Similar — default excluded as personal unless clearly business (e.g., business Google account with partita IVA) |

### 3.15 — Anthropic and AI services

| Supplier | Treatment |
|---|---|
| Anthropic PBC — Claude Pro (individual tier) | Consumer-tier on personal email → default excluded as personal |
| Anthropic PBC — Claude Team / Claude Enterprise | Business tier with partita IVA on invoice → non-EU reverse charge art. 17 c. 2, autoliquidazione 22% |
| OpenAI LLC — ChatGPT Plus (individual) | Default excluded as personal |
| OpenAI LLC — ChatGPT Team / Enterprise | Non-EU reverse charge autoliquidazione 22% |

### 3.16 — Amazon (intra-Community acquisitions and local billing)

| Pattern | Treatment |
|---|---|
| Amazon.it marketplace sale billed by an Italian seller | Domestic 22% (or reduced rate for books etc.), check invoice |
| Amazon Business EU SARL with LU IBAN | Intra-Community acquisition of goods — report in VP4/VP5 as acquisto intracomunitario with self-assessed 22% |
| Amazon Web Services (see 3.13) | See AWS branch exception |
| Amazon consumer purchases on .it with an IT IBAN | Depends on the seller — if the invoice shows an Italian partita IVA it's domestic; if it shows an LU partita IVA it's an intra-Community acquisition |

## Section 4 — Worked examples

The worked examples below use a hypothetical client: **Marco Bianchi, architect in Milan (studio di architettura), operating as a ditta individuale in regime ordinario, USt-IdNr IT01234567890, Studio in Via Torino 45 Milano, VP filings quarterly.** This client does NOT correspond to any test fixture used to validate this skill — the examples are drawn from a fictional profile to avoid eval contamination.

### Example 1 — The AWS branch exception

Bank line: `AWS EMEA SARL IT BRANCH -640.00 EUR "AWS compute charges Q1"`. IBAN on payment: IT.

**Wrong treatment:** Kz 46 EU reverse charge under autoliquidazione. This is the default assumption for "AWS EMEA SARL" because the parent entity is Luxembourg.

**Right treatment:** Domestic 22% — the IT branch designation in the counterparty field and the Italian IBAN together indicate that AWS is billing from its Italian branch with an Italian partita IVA. The invoice will show Italian IVA charged. Treat as a normal domestic purchase with VP5 input VAT recovery of (640 / 1.22 × 0.22) = €115.41.

**Reviewer note:** Confirm by inspecting the actual AWS invoice for the period. The bank statement alone is not sufficient to confirm branch billing.

### Example 2 — The Apple One consumer trap

Bank line: `APPLE DISTRIBUTION INTL -14.99 EUR "APPLE ONE PREMIER m.bianchi@gmail.com"`.

**Wrong treatment:** Kz 46 EU reverse charge at 22%, recover €2.70 input VAT.

**Right treatment:** Excluded as personal expense. The description contains "m.bianchi@gmail.com" — a personal Gmail address, not a business domain. Apple One Premier is a consumer bundle (iCloud+, Music, TV+, Arcade, Fitness+) and is almost never legitimately a business expense for a one-person architectural practice. Default to excluded. If the user specifically confirms business use, reclassify as autoliquidazione — but the default is excluded and the reviewer brief should flag the need for confirmation.

### Example 3 — Rappresentanza vs vitto e alloggio

Bank line: `RISTORANTE DA GIOVANNI MILANO -187.50 EUR "cena cliente"`.

**First question:** is this "spese di rappresentanza" (entertainment, art. 19-bis1(h), 75% deductible with documentation) or "vitto e alloggio durante trasferta" (business trip meals, 100% deductible with documentation)?

The description says "cena cliente" (client dinner) in Milan. Marco is based in Milan — this is not a trasferta (out-of-town trip), so it falls under rappresentanza, not vitto e alloggio. Apply 75% deductibility if (and only if) the user can produce a "giustificativo" showing the attendees, the business purpose, and the date. Without documentation, default to blocked.

For LIPE purposes, the input VAT at 10% (restaurants are reduced rate) on €187.50 is €17.05. At 75% deductibility: €12.79 recovered. Default treatment: blocked, €0 recovered, flag for Q3 question on the reviewer form asking whether documentation exists.

### Example 4 — Intra-Community supply of services to a French B2B customer

Bank line: `ARCHITECTES ASSOCIES PARIS +4,500.00 EUR "Consulting architettonico progetto Lyon"`. IBAN: FR.

**Treatment:** This is a B2B supply of services to a VAT-registered EU customer under art. 44 of the directive (place of supply = customer's country). Italian treatment: the supply is "non soggetto" (not subject to Italian IVA) per art. 7-ter D.P.R. 633/72 and the invoice is issued without IVA. For LIPE purposes, the amount appears in VP2 as a non-taxable output (operazione non imponibile) but carries no output VAT.

**Additional requirement:** this triggers a separate Esterometro filing (or Fattura Elettronica Estero via SdI, depending on the period — the rules changed effective 1 July 2022). Flag in the reviewer brief — the skill does NOT generate the Esterometro, but the obligation must be noted.

**Conditions to verify:** the French customer's TVA number must be valid on VIES at the time of supply; the invoice must include both VAT numbers and the note "operazione non soggetta art. 7-ter D.P.R. 633/72". If the VIES check was not performed, the supply reclassifies to domestic 22% with €990 of output IVA — cash swing of nearly €1,000 on this single line. Q1 question on the reviewer form: "did you verify ARCHITECTES ASSOCIES PARIS on VIES before invoicing?"

### Example 5 — Fuel station with 40% cap

Bank line: `ENI STATION VIA MILANO 12 -85.00 EUR`.

**Treatment:** Fuel for a non-commercial vehicle (presumed car, as Marco is an architect without a van or truck). Under art. 19-bis1(c) D.P.R. 633/72, input VAT on cars and fuel for cars is capped at 40% regardless of actual business use, unless the vehicle is exclusively business and this is documented (rare for a sole practitioner).

- Gross: €85.00
- Net: 85 / 1.22 = €69.67
- Full input VAT at 22%: €15.33
- Recoverable at 40% cap: €6.13

For LIPE: VP5 input VAT recovery = €6.13. The remaining €9.20 of input VAT is blocked.

**Trucks and commercial vehicles:** if the bank description indicates a commercial vehicle (autocarro, furgone, van), the 40% cap does not apply and the full €15.33 is recoverable. The skill's bank statement reading guide (Section 8) lists the Italian terms to look for.

### Example 6 — Camera di Commercio annual fee

Bank line: `CCIAA MILANO -120.00 EUR "diritto annuale 2026"`.

**Wrong treatment:** Assume an invoice was issued with 22% IVA and claim €21.64 input VAT.

**Right treatment:** Excluded. The Camera di Commercio is a public-law body and the "diritto annuale" is a statutory contribution under L. 580/1993, NOT consideration for a taxable supply. No IVA is charged on the annual fee. There is no input VAT to recover. Mark the line as excluded with reason "Camera di Commercio statutory contribution, outside VAT scope." Do NOT claim €21.64 of input VAT.

**This is the Italian equivalent of the German IHK error** that surfaced in the German skill's rerun analysis. Camera di Commercio dues, ordini professionali dues, and similar statutory contributions to public-law bodies never carry VAT and the skill must not invent it.

## Section 5 — Tier 1 deterministic rules (compressed)

These are the rules applied silently by the classifier when the data unambiguously resolves the treatment. They do not trigger Tier 2 questions.

**5.1 — Domestic B2B sale to an Italian partita IVA customer.** 22% standard, or reduced rate per Tabella A if the goods/services qualify. Report in VP2 (net) and VP4 (output VAT). No reverse charge unless specifically covered by a national extension (construction, scrap metal, electronics above thresholds).

**5.2 — Domestic B2C sale.** Same rates. Same reporting. Different invoice requirements (scontrino elettronico or invoice per customer request).

**5.3 — Intra-Community supply of goods to an EU VAT-registered customer.** Non imponibile under art. 41 D.L. 331/1993. Report in VP2 but with no output VAT. Triggers Esterometro filing. Conditions: customer VAT verified on VIES, goods physically transported out of Italy, proof of transport retained, invoice shows both partite IVA and the "operazione non imponibile art. 41" note. If any condition fails, reclassify as domestic 22%.

**5.4 — B2B service to a VAT-registered EU customer.** Non soggetto under art. 7-ter — place of supply is the customer's country. Report in VP2 as a non-taxable output. Triggers Esterometro.

**5.5 — B2B service to a non-EU customer.** Non soggetto under art. 7-ter. No IVA. No Esterometro (non-EU customers are outside the esterometro regime for services — but the Esterometro rules for non-EU transactions have changed multiple times, note for reviewer).

**5.6 — Purchase from EU supplier (goods).** Intra-Community acquisition under art. 38 D.L. 331/1993. Self-assess 22% output IVA in VP4 and claim 22% input IVA in VP5 (net cash zero unless partial exemption or blocked input). Requires invoice from EU supplier with both partite IVA.

**5.7 — Purchase of services from EU supplier (reverse charge — autoliquidazione).** Under art. 17 c. 2 D.P.R. 633/72 and art. 44 of the directive. Self-assess 22% in VP4, claim 22% in VP5. Net zero. The Irish/Luxembourg SaaS stack (Google, Microsoft, Adobe, Slack, Dropbox, etc.) is the dominant case.

**5.8 — Purchase from non-EU supplier (services).** Reverse charge under art. 17 c. 2. Same mechanics as EU reverse charge — self-assess 22%, claim 22%, net zero. Zoom, Fiverr, US-based consultants, Anthropic business tier all fall here.

**5.9 — Import of goods from outside the EU.** Cash payment at the border through customs agent (spedizioniere) unless the user has elected postponed accounting (reverse charge all'importazione, a refusal trigger for v0.1 — see R-IT-12). Cash payment treatment: the customs document (bolletta doganale) is the invoice equivalent, and the IVA paid at import is recoverable as input VAT in the period of payment.

**5.10 — Exempt-without-credit supplies.** Sales of banking/insurance/healthcare/education/residential letting services are esenti under art. 10 D.P.R. 633/72 — non-taxable sales, no output VAT, no input VAT on related costs. If the user's business makes any esenti supplies above de minimis, fire R-IT-5 (partial exemption).

**5.11 — Mixed-use vehicle fuel and maintenance.** 40% cap applies by default (art. 19-bis1(c)). Do not ask for actual business use percentage unless the user volunteers it.

**5.12 — Business gifts above €50 per recipient per year.** Blocked under art. 19-bis1(h) — same principle as Germany but different threshold (Italy €50, Germany €50 — happen to match).

**5.13 — Business meals and entertainment.** Default blocked unless documented as "vitto e alloggio in trasferta" (100%) or "spesa di rappresentanza" (75% with formal documentation). The 75% vs 100% distinction depends on whether the user was away from their normal place of work.

## Section 6 — Italy-specific Tier 2 ambiguity catalogue

Applied after the EU-wide T2-EU catalogue in `eu-vat-directive` Section 12. Each entry: pattern / why the data can't answer / question / default.

**T2-IT-1 — Rappresentanza vs trasferta.** *Pattern:* restaurant/hotel line in a city that may or may not be the user's base of operations. *Why:* bank line doesn't indicate trasferta. *Question:* "Was this meal/hotel during a business trip away from your office, or was it entertainment at or near your office location?" *Default:* blocked.

**T2-IT-2 — Vehicle category.** *Pattern:* fuel or vehicle expense on an unspecified vehicle. *Why:* bank line doesn't distinguish autoveicolo from autocarro. *Question:* "Is the vehicle a passenger car (autoveicolo, deduction capped at 40%) or a commercial vehicle (autocarro, deduction up to 100%)?" *Default:* 40% cap.

**T2-IT-3 — Telephone/mobile mixed use.** *Pattern:* mobile phone invoice. *Why:* bank line doesn't indicate business-only use. *Question:* "Is this a pure business line or mixed personal/business?" *Default:* 50% cap under art. 19-bis1(g).

**T2-IT-4 — Esenti income detection.** *Pattern:* incoming payment with a description suggesting exempt activity (interest, rental from residential property, insurance commission). *Why:* bank line doesn't classify as esente vs imponibile. *Question:* "Does your business earn any interest income, residential rent, insurance commission, or other art. 10 exempt supplies?" *Default:* if yes, fire R-IT-5 (partial exemption); if no, treat as taxable at 22%.

**T2-IT-5 — SdI compliance.** *Pattern:* the bank statement shows B2B activity but the skill has not established that the user is operating via SdI. *Why:* SdI compliance is not directly visible on the bank statement. *Question:* "Are all your sales invoices issued through the Sistema di Interscambio (SdI), either directly or via a commercialista/software provider?" *Default:* if the user says no or unclear, fire R-IT-4 (e-invoicing non-compliance).

**T2-IT-6 — Split payment customer.** *Pattern:* incoming payment from an entity with "S.p.A." or "Comune di" or "Ministero" or "Regione" in the counterparty name. *Why:* the PA/listed-company status is not on the bank line. *Question:* "Is this customer a public administration entity, a listed company, or otherwise subject to split payment under art. 17-ter?" *Default:* if yes, fire R-IT-3 (split payment).

**T2-IT-7 — LIPE period mismatch.** *Pattern:* the bank statement period doesn't align with a standard monthly or quarterly LIPE boundary. *Why:* the user may be on an unusual filing cadence. *Question:* "Are you on monthly or quarterly LIPE filing?" *Default:* quarterly (the more common case for small businesses).

## Section 7 — Excel working paper template (Italy-specific overlay)

The base specification is in `vat-workflow-base` Section 3. This section provides the Italy-specific overlay.

**Sheet 1 — "Transactions".** 12 columns: Date, Counterparty, Description, Gross (EUR), Net (EUR), IVA (EUR), Rate, LIPE field, Treatment, Default? (Y/N), Q-Ref, Excluded reason.

**Sheet 2 — "LIPE Summary".** Aggregates by LIPE field:

| Field | Description | Formula |
|---|---|---|
| VP2 | Totale operazioni attive (imponibili) | `=SUMIFS(Transactions!E:E,Transactions!H:H,"VP2")` |
| VP3 | Totale operazioni passive | `=SUMIFS(Transactions!E:E,Transactions!H:H,"VP3")` |
| VP4 | IVA a debito | `=SUMIFS(Transactions!F:F,Transactions!H:H,"VP4")` |
| VP5 | IVA a credito | `=SUMIFS(Transactions!F:F,Transactions!H:H,"VP5")` |
| VP6 | IVA dovuta / credito | `=VP4-VP5` |
| VP8 | Risultato periodo | `=VP6-VP7` |

**Sheet 3 — "Return Form".** Lays out the LIPE form with the final values drawn from the LIPE Summary sheet.

**Color conventions:** yellow highlight on every row with Default? = Y. No other colors.

**Mandatory recalc step:** `python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/italy-vat-<period>-working-paper.xlsx` after writing. Verify `status: success, total_errors: 0` before proceeding.

## Section 8 — Italian bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Section 1 Step 6, plus these Italy-specific patterns.

**CSV format conventions.** Italian business banks export in several formats. Common columns: Data Contabile, Data Valuta, Descrizione, Importo, Valuta, Causale, Beneficiario/Ordinante, IBAN Controparte. Date format: DD/MM/YYYY. Decimal separator: comma (1.234,56 EUR means one thousand two hundred thirty-four euros and fifty-six cents). Currency indicator: EUR or € symbol.

**Common causali (bank transaction codes)** that help with classification:
- BON = bonifico (wire transfer)
- ADD = addebito diretto (direct debit)
- POS = point-of-sale card payment
- PRE = prelievo (withdrawal)
- SDD = SEPA Direct Debit
- VER = versamento (deposit)
- COM = commissioni (fees — usually bank fees, exempt art. 10)
- STI = stipendio (salary payment — excluded as payroll)
- F24 = tax payment via the F24 form (excluded as tax authority payment)

**Internal transfers and exclusions.** Giroconto (internal transfer between own accounts), prelievo (cash withdrawal), versamento contanti (cash deposit), rimborso spese (expense reimbursement), stipendio, TFR (end-of-service allowance), interessi attivi/passivi (interest — exempt), F24 (tax payment), INPS/INAIL (statutory contributions). None of these are VAT events.

**Italian supplier name abbreviations.** Italian banks often truncate or abbreviate counterparty names in ways that obscure the actual entity. Common patterns:
- "TIM SpA" / "T.I.M. S.P.A." / "TELECOM ITALIA" — all the same entity
- "INTESA SP" / "INTESA SANP" — Intesa Sanpaolo
- "ENEL EN" / "ENEL ENERGIA" — Enel Energia S.p.A.
- "AGE ENTRATE" / "AG.ENTRATE" / "AGENZIA ENTRATE" — Agenzia delle Entrate

**Partita IVA and codice fiscale in descriptions.** Italian bank descriptions sometimes include the counterparty's partita IVA (11 digits starting with IT) or codice fiscale (16 alphanumeric characters for individuals, 11 digits for companies — same as partita IVA). These are useful for verifying counterparty identity and should be captured in the Transactions sheet where available.

## Section 9 — Onboarding (fallback only — use after Step 3 of the workflow base)

The workflow in `vat-workflow-base` Section 1 mandates inferring the client profile from the data first (Step 3) and only confirming with the user in Step 4. The questions below are a *fallback* — ask only the questions the data could not answer at all.

**Q1. Regime check.** "Are you in the regime ordinario (standard VAT), regime forfettario (flat-rate small business), or another special regime?" Only the regime ordinario is supported by this skill — forfettario fires R-IT-1.

**Q2. LIPE frequency.** "Are you on monthly or quarterly LIPE filing?" If turnover > €800,000 (services) or > €700,000 (goods), monthly is mandatory.

**Q3. SdI compliance.** "Are all your sales invoices issued through the Sistema di Interscambio (SdI)?" If no, fire R-IT-4.

**Q4. Partial exemption check.** "Does your business earn any exempt income (interest, insurance commission, residential rent, medical/educational services)?" If yes, fire R-IT-5.

**Q5. Split payment customer check.** "Do you have any customers that are public administration, listed companies, or otherwise subject to split payment?" If yes, fire R-IT-3.

**Q6. Construction sector check.** "Do you work as a contractor or subcontractor in the construction sector?" If yes, fire R-IT-11.

**Q7. Vehicle use.** "Do you have a vehicle used for the business? Is it a passenger car (40% cap) or a commercial vehicle (autocarro, up to 100%)?"

**Q8. Esterometro awareness.** "Are you aware of the Esterometro / fattura elettronica estero obligation for cross-border transactions? Do you file it separately?" This is not a question whose answer changes the LIPE, but it affects what goes in the reviewer brief.

## Section 10 — Reference material

### Validation status

This is v0.1 of `italy-vat-return`. Drafted in April 2026 from public sources (D.P.R. 633/1972, Agenzia delle Entrate published guidance, EU directive content from `eu-vat-directive` v0.1) with no practitioner validation. The supplier pattern library, the refusal catalogue, the Tier 1 rules, and the worked examples are all derived from the same sources and should be treated as v0.1 — not practitioner-validated, not tested against a real Italian bank statement, likely to contain errors that only a local commercialista would catch.

**Specific known limitations:**

1. The LIPE field mapping (VP2, VP3, VP4, VP5) is simplified relative to the actual LIPE form, which has more granular fields for specific transaction types. v0.1 covers the most common cases; edge cases may need manual adjustment.
2. The Esterometro / fattura elettronica estero rules have changed multiple times between 2019 and 2023 and v0.1 describes them in general terms. The skill flags the obligation but does not generate the Esterometro filing.
3. The regime forfettario is in the refusal catalogue — v0.1 does not attempt to handle it even though it is the most common Italian regime for small businesses. This is deliberate: forfettario is structurally different from the regime ordinario and would require a separate skill.
4. The split payment and construction reverse charge regimes are in the refusal catalogue for the same reason — they are different enough from standard IVA classification to warrant their own dedicated skills.
5. The annual Dichiarazione IVA is not supported — v0.1 covers only the periodic LIPE. The annual return requires integration with the income tax return and multi-period reconciliation.
6. The IVA per cassa regime is in the refusal catalogue.

### Sources

1. D.P.R. 26 ottobre 1972 n. 633 (the Italian VAT law, the "Decreto IVA"): https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633
2. D.L. 30 agosto 1993 n. 331 (intra-Community VAT): https://www.normattiva.it
3. Agenzia delle Entrate — Area Tematica IVA: https://www.agenziaentrate.gov.it/portale/web/guest/schede/comunicazioni/liquidazioni-periodiche-iva
4. Agenzia delle Entrate — guide pratiche on specific topics (fatturazione elettronica, esterometro, split payment, regime forfettario)
5. EU Directive 2006/112/EC via `eu-vat-directive` v0.1
6. Ministero dell'Economia e delle Finanze circolari and risoluzioni
7. D.Lgs. 127/2015 (electronic invoicing and Sistema di Interscambio)

### Change log

- **v0.1 (April 2026):** Initial draft following the germany-vat-return v0.3.1 architecture. Three-tier model: loads on top of vat-workflow-base v0.2.0 and eu-vat-directive v0.1. Covers regime ordinario periodic LIPE only. Forfettario, split payment, construction reverse charge, margin schemes, travel agents, agricultural flat rate, partial exemption, VAT groups, annual Dichiarazione IVA, and IVA per cassa are all in the refusal catalogue. Supplier pattern library has roughly 50 entries across 16 sub-categories. Six worked examples from a hypothetical Milan architect. Not practitioner-validated.

### Self-check (v0.1 of this document)

1. Quick reference at top: yes (Section 1).
2. Refusal catalogue distinct from EU-wide: yes (13 R-IT refusals in Section 2, on top of R-EU-1 through R-EU-12).
3. Supplier library as literal lookup table: yes (Section 3, 16 sub-tables).
4. Worked examples drawn from a hypothetical non-test client: yes (Milan architect, Section 4).
5. Tier 1 rules compressed: yes (Section 5, thirteen rules).
6. Tier 2 catalogue distinct from EU-wide: yes (seven T2-IT entries in Section 6).
7. Excel template specification with mandatory recalc: yes (Section 7).
8. Italian bank statement reading guide: yes (Section 8).
9. Onboarding as fallback only: yes (Section 9).
10. Reference material at bottom: yes (Section 10).
11. AWS branch exception explicit: yes (Section 3.13 and Example 1).
12. Apple consumer trap explicit: yes (Section 3.14 and Example 2).
13. Camera di Commercio zero-VAT explicit: yes (Section 3.5 and Example 6).
14. Rappresentanza vs trasferta distinction explicit: yes (Section 5.13 and Example 3).
15. Vehicle 40% cap explicit: yes (Section 3.11, Section 5.11, and Example 5).

## End of Italy VAT Return Skill v0.1

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` v0.2.0 or later (Tier 1, workflow architecture) AND `eu-vat-directive` v0.1 or later (Tier 2, EU directive content). Do not attempt to produce a LIPE without all three files loaded.

**Practitioner review note:** this skill has not been reviewed by an Italian commercialista. Before this skill is used for any real return, it should be reviewed line-by-line by a practitioner with experience in the Italian regime ordinario and periodic LIPE filings. The refusal catalogue, in particular, may be over- or under-inclusive relative to real Italian practice.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
