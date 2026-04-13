---
name: belgium-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Belgian VAT return (déclaration périodique TVA / periodieke BTW-aangifte) for a self-employed individual or small business in Belgium. Trigger on phrases like "prepare Belgian VAT return", "Belgian BTW", "déclaration TVA Belgique", "BTW-aangifte", "classify transactions for Belgian VAT", or any request involving Belgium VAT filing. This skill covers Belgium only, standard regime (normal/normal simplifié). Régime forfaitaire, partial exemption, margin scheme, and VAT units are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Belgian VAT work.
version: 2.0
---

# Belgium VAT Return Skill (Déclaration Périodique / Periodieke Aangifte) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Belgium (Koninkrijk België / Royaume de Belgique) |
| Standard rate | 21% |
| Reduced rates | 12% (social housing, restaurant meals including non-alcoholic drinks, certain energy products), 6% (basic foodstuffs, water, books, medicines, hotels, renovation of old residential buildings, passenger transport, cultural events) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods, certain newspapers) |
| Return form | Déclaration périodique à la TVA (grilles/cases 00–91) |
| Filing portal | https://finances.belgium.be (MyMinfin / Intervat) |
| Authority | SPF Finances / FOD Financiën |
| Currency | EUR only |
| Filing frequencies | Monthly (turnover > €2,500,000 or mandatory sectors); Quarterly (below threshold, standard) |
| Deadline | 20th of the month following the period |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants contributors |
| Validation date | April 2026 |

**Key grilles/cases (the boxes you will use most):**

| Grille | Meaning |
|---|---|
| 00 | Sales of goods and services at 0% (non-taxable/exempt with credit) |
| 01 | Sales at 6% (base) |
| 02 | Sales at 12% (base) |
| 03 | Sales at 21% (base) |
| 44 | Intra-EU services received (reverse charge base) |
| 45 | Intra-EU services provided (base) |
| 46 | Intra-EU goods supplied (base, 0%) |
| 47 | Other exempt operations and operations with co-contractor reverse charge |
| 48 | Credit notes issued (negative output) |
| 49 | Credit notes received (negative input) |
| 54 | Output VAT on grilles 01, 02, 03 |
| 55 | Output VAT on intra-EU acquisitions and reverse charge (grilles 86, 88) |
| 56 | Output VAT on co-contractor reverse charge |
| 57 | Output VAT on imports with ET 14 licence |
| 59 | Total output VAT |
| 81 | Purchases of goods, raw materials, consumables (base) |
| 82 | Purchases of services and diverse goods (base) |
| 83 | Purchases of capital goods (investissements, base) |
| 84 | Credit notes received on purchases |
| 85 | Credit notes issued on sales |
| 86 | Intra-EU acquisitions of goods and services (base, linked with grille 55) |
| 87 | Other acquisitions (imports, etc.) |
| 88 | Intra-EU services received (base, linked with grille 55) |
| 59 | Total output VAT (sum of 54+55+56+57) |
| 63 | Total deductible input VAT (voorbelasting / TVA déductible) |
| 71 | Net VAT payable (if 59 > 63) |
| 72 | Net VAT credit (if 63 > 59) |

**Conservative defaults — Belgium-specific values:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 21% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Belgium |
| Unknown B2B vs B2C status for EU customer | B2C, charge 21% |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds:**

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

**Minimum viable** — bank statement for the period. Acceptable from: BNP Paribas Fortis, KBC, Belfius, ING Belgium, CBC, AXA Bank, Argenta, Crelan, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices (especially intra-EU and co-contractor reverse charge), purchase invoices above €400, the client's TVA/BTW number (BE + 10 digits).

**Ideal** — complete invoice register, prior period return, reconciliation of grille 72 credit.

**Refusal policy if minimum is missing — SOFT WARN.** Same as Malta v2.0 template.

### Belgium-specific refusal catalogue

**R-BE-1 — Régime forfaitaire.** *Trigger:* client is under the flat-rate scheme (forfaitaire regeling). *Message:* "Forfaitaire taxpayers have simplified obligations with pre-determined profit margins. This skill covers the normal regime only."

**R-BE-2 — Small enterprise exemption (vrijstellingsregeling / franchise).** *Trigger:* client under the small enterprise exemption (turnover < €25,000). *Message:* "Small enterprise exemption clients do not charge VAT and cannot recover input VAT. They file a special listing only (listing clients), not the periodic return. This skill covers the normal regime."

**R-BE-3 — Partial exemption (pro rata).** *Trigger:* both taxable and exempt supplies, non-de-minimis. *Message:* "You make both taxable and exempt supplies. Input VAT must be apportioned. Please use a comptable-fiscaliste."

**R-BE-4 — Margin scheme (régime de la marge / margeregeling).** *Trigger:* second-hand goods, art, antiques. *Message:* "Margin scheme requires per-item margin computation. Out of scope."

**R-BE-5 — VAT unit (unité TVA / BTW-eenheid).** *Trigger:* client is part of a BTW-eenheid. *Message:* "BTW-eenheden require consolidation. Out of scope."

**R-BE-6 — Fiscal representative.** *Trigger:* non-resident with fiscal representative. *Message:* "Non-resident with fiscal representative — out of scope."

**R-BE-7 — Real estate (TVA immobilière).** *Trigger:* new construction or property. *Message:* "Real estate VAT is complex. Please use a comptable-fiscaliste."

**R-BE-8 — Income tax instead of VAT.** *Trigger:* user asks about IPP/ISOC instead of TVA/BTW. *Message:* "This skill handles Belgian VAT only."

---

## Section 3 — Supplier pattern library (the lookup table)

Match by case-insensitive substring. If none match, fall through to Section 5.

### 3.1 Belgian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BNP PARIBAS FORTIS, FORTIS | EXCLUDE for bank charges | Financial service, exempt |
| KBC, KBC BANK | EXCLUDE for bank charges | Same |
| BELFIUS, DEXIA | EXCLUDE for bank charges | Same |
| ING BELGIQUE, ING BELGIE, ING BE | EXCLUDE for bank charges | Same |
| CBC | EXCLUDE for bank charges | Same |
| ARGENTA, CRELAN | EXCLUDE for bank charges | Same |
| AXA BANK, AGIEAS | EXCLUDE for bank charges | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for separate taxable subscriptions |
| INTERETS, RENTE, INTEREST | EXCLUDE | Interest, out of scope |
| PRET, LENING, EMPRUNT | EXCLUDE | Loan principal, out of scope |

### 3.2 Belgian government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| SPF FINANCES, FOD FINANCIEN | EXCLUDE | Tax payment (TVA, IPP, ISOC) |
| MINFIN, ADMINISTRATION FISCALE | EXCLUDE | Tax payment |
| ONSS, RSZ | EXCLUDE | Social security contributions (ONSS/RSZ) |
| CAISSE D'ASSURANCES SOCIALES, SOCIAAL VERZEKERINGSFONDS | EXCLUDE | Social security for self-employed |
| UCM, ACERTA, PARTENA, LIANTIS, SECUREX, XERIUS | EXCLUDE | Social security funds for self-employed |
| GREFFE, GREFFIER | EXCLUDE | Court fees |
| BCE, KBO, BANQUE CARREFOUR | EXCLUDE | Business register fees |
| PROVINCE, COMMUNE, GEMEENTE | EXCLUDE | Local government fees |

### 3.3 Belgian utilities

| Pattern | Treatment | Grille | Notes |
|---|---|---|---|
| ENGIE ELECTRABEL, ELECTRABEL | Domestic 21% or 6% | 82/63 (input) | Electricity: 21% standard; gas/electricity may be 6% (temporary energy measures — verify current rate) |
| LUMINUS | Domestic 21% or 6% | 82/63 | Energy |
| TOTALENERGIES BELGIQUE | Domestic 21% | 82/63 | Energy |
| PROXIMUS | Domestic 21% | 82/63 (input) | Telecoms — overhead |
| TELENET | Domestic 21% | 82/63 (input) | Telecoms/cable/broadband |
| ORANGE BELGIQUE, ORANGE BE | Domestic 21% | 82/63 | Mobile telecoms |
| BASE, MOBILE VIKINGS | Domestic 21% | 82/63 | Mobile telecoms |
| SWDE, VIVAQUA | Domestic 6% | 82/63 | Water supply at reduced rate |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| AG INSURANCE, AG | EXCLUDE | Insurance, exempt |
| ETHIAS, AXA BELGIQUE | EXCLUDE | Same |
| P&V, VIVIUM, BALOISE | EXCLUDE | Same |
| ASSURANCE, VERZEKERING | EXCLUDE | All insurance exempt |
| MUTUELLE, MUTUALITEIT | EXCLUDE | Health insurance mutual, exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Grille | Notes |
|---|---|---|---|
| BPOST (standard mail) | EXCLUDE for standard postage | | Universal postal service, exempt |
| BPOST (parcels) | Domestic 21% | 82/63 | Non-universal services taxable |
| DHL EXPRESS BELGIQUE | Domestic 21% | 82/63 | Express courier |
| UPS BELGIUM, TNT BELGIUM | Domestic 21% | 82/63 | Courier |
| MONDIAL RELAY, COLIS PRIVE | Domestic 21% | 82/63 | Parcel delivery |

### 3.6 Transport (Belgium domestic)

| Pattern | Treatment | Grille | Notes |
|---|---|---|---|
| SNCB, NMBS | Domestic 6% | 82/63 (input) | Rail transport at reduced rate |
| STIB, MIVB | Domestic 6% | 82/63 (input) | Brussels public transport |
| TEC | Domestic 6% | 82/63 (input) | Walloon public transport |
| DE LIJN | Domestic 6% | 82/63 (input) | Flemish public transport |
| UBER BE, UBER BELGIUM | Domestic 6% (transport) | 82/63 | Ride-hailing |
| TAXI, TAXI VERTS | Domestic 6% | 82/63 | Local taxi, reduced rate |
| BRUSSELS AIRLINES (domestic/Schengen) | Domestic 21% | 82/63 | Domestic/intra-EU flights at 21% |
| BRUSSELS AIRLINES, RYANAIR (international non-EU) | EXCLUDE / 0% | | International flights exempt |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| COLRUYT, COLRUYT GROUP | Default BLOCK input VAT | Personal provisioning |
| DELHAIZE, AHOLD DELHAIZE | Default BLOCK | Same |
| CARREFOUR BELGIQUE, ALDI, LIDL | Default BLOCK | Same |
| MATCH, PROXY DELHAIZE, SPAR | Default BLOCK | Same |
| RESTAURANT, BRASSERIE, CAFE | Default BLOCK | Entertainment — see Section 5.12 |

### 3.8 SaaS — EU suppliers (reverse charge, grille 88/55 for services, 86/55 for goods)

| Pattern | Billing entity | Grille | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 88/55 + 63 | EU service reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 88/55 + 63 | Same |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 88/55 + 63 | Same |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 88/55 + 63 | Same |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 88/55 + 63 | Same |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 88/55 + 63 | EU reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 88/55 + 63 | Same |
| SLACK | Slack Technologies Ireland Ltd (IE) | 88/55 + 63 | Same |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 88/55 + 63 | EU reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 88/55 + 63 | Same |
| STRIPE (subscription) | Stripe Technology Europe Ltd (IE) | 88/55 + 63 | Transaction fees exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (reverse charge, grille 87/56 area)

| Pattern | Billing entity | Grille | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | 88/55 + 63 | LU → EU reverse charge |
| NOTION | Notion Labs Inc (US) | 87 + 56 + 63 | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 87 + 56 + 63 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 87 + 56 + 63 | Non-EU reverse charge |
| GITHUB (standard) | GitHub Inc (US) | 87 + 56 + 63 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | 87 + 56 + 63 | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | 87 + 56 + 63 | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or IE — check | 87/56 or 88/55 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 87 + 56 + 63 | Non-EU reverse charge |

### 3.10 SaaS — the exception

| Pattern | Treatment | Why |
|---|---|---|
| AWS EMEA SARL | EU reverse charge 88/55 + 63 (LU entity) | If invoice shows Belgian BTW, treat as domestic 21%. |

### 3.11 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (subscription) | EU reverse charge 88/55 + 63 | IE entity |
| MOLLIE, ADYEN | Check invoice | Dutch entities — typically via NL entity |
| SUMUP, SQUARE, ZETTLE | Check invoice | If Belgian: domestic 21%; if EU: reverse charge |

### 3.12 Professional services (Belgium)

| Pattern | Treatment | Grille | Notes |
|---|---|---|---|
| COMPTABLE, BOEKHOUDER | Domestic 21% | 82/63 | Always deductible |
| EXPERT COMPTABLE, BEDRIJFSREVISOR | Domestic 21% | 82/63 | Audit/accounting |
| AVOCAT, ADVOCAAT | Domestic 21% | 82/63 | Business legal matters |
| NOTAIRE, NOTARIS | Domestic 21% | 82/63 | Business notarial fees |
| FISCALISTE, BELASTINGCONSULENT | Domestic 21% | 82/63 | Tax adviser |

### 3.13 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ONSS, RSZ | EXCLUDE | Social security employer contributions |
| PRECOMPTE PROFESSIONNEL, BEDRIJFSVOORHEFFING | EXCLUDE | Payroll tax withholding |
| SALAIRE, LOON, WEDDE | EXCLUDE | Wages |
| PENSION, PENSIOEN | EXCLUDE | Pension contributions |
| UCM, ACERTA, PARTENA, SECUREX | EXCLUDE | Self-employed social contributions |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| LOYER COMMERCIAL, HUUR BEDRIJFSPAND | Domestic 21% | Commercial lease with TVA/BTW option |
| LOYER, HUUR (residential) | EXCLUDE | Residential lease exempt |
| PRECOMPTE IMMOBILIER, ONROERENDE VOORHEFFING | EXCLUDE | Property tax |
| CADASTRE, KADASTER | EXCLUDE | Government |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| VIREMENT INTERNE, INTERNE OVERBOEKING | EXCLUDE | Internal movement |
| DIVIDENDE, DIVIDEND | EXCLUDE | Out of scope |
| REMBOURSEMENT PRET, AFLOSSING | EXCLUDE | Loan repayment |
| RETRAIT, GELDOPNAME | TIER 2 — ask | Default exclude |
| APPORT, INBRENG | EXCLUDE | Owner injection |

---

## Section 4 — Worked examples

Six fully worked classifications from a hypothetical Belgium-based self-employed IT consultant.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
Notion Labs Inc is US (Section 3.9). Non-EU reverse charge. Client self-assesses: output VAT on grille 56, input VAT on grille 63. Base on grille 87. Net effect zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Grille (input) | Grille (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.08 | 21% | 63 | 56 (base 87) | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`

**Reasoning:**
IE entity — EU service reverse charge. Base on grille 88, output VAT on grille 55, input VAT on grille 63. Net zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Grille (input) | Grille (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 178.50 | 21% | 63 | 55 (base 88) | N | — | — |

### Example 3 — Entertainment, treatment in Belgium

**Input line:**
`15.04.2026 ; COMME CHEZ SOI BRUXELLES ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant transaction. In Belgium, the TVA on restaurant meals at 12% is deductible if the meal has a business purpose and is properly documented (names, business reason). However, frais de réception (entertainment of external guests) at 50% deductible for income tax but fully deductible for VAT if documented. Personal meals: blocked. Default: block, flag for reviewer.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Grille | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | COMME CHEZ SOI BRUXELLES | -220.00 | -220.00 | 0 | — | — | Y | Q1 | "Restaurant: TVA deductible if business purpose. Confirm and provide names." |

### Example 4 — Capital goods (investissement)

**Input line:**
`18.04.2026 ; DELL BELGIQUE SA ; DEBIT ; Laptop XPS 15 ; -1,595.00 ; EUR`

**Reasoning:**
Capital goods in Belgium go to grille 83 (investissements / investeringen). There is no explicit minimum threshold for capitalisation for TVA purposes, but assets used for more than one year are typically treated as capital goods. Input VAT on grille 63. Subject to herzieningsregeling (5 years movable, 15 years immovable).

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Grille | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DELL BELGIQUE SA | -1,595.00 | -1,318.18 | -276.82 | 21% | 83/63 | N | — | — |

### Example 5 — EU B2B service sale

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice BE-2026-018 IT consultancy ; +3,500.00 ; EUR`

**Reasoning:**
B2B services to Germany — place of supply is customer's country. Report on grille 45 (services intracommunautaires fournis). No output VAT. Verify German USt-IdNr on VIES.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Grille | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | 45 | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, partial recovery

**Input line:**
`28.04.2026 ; ARVAL BELGIUM ; DEBIT ; Lease payment BMW 3 Series ; -650.00 ; EUR`

**Reasoning:**
Car lease. In Belgium, TVA on cars is deductible based on professional use, capped at a maximum of 50% (Art. 45 §2 CTVA). The default professional use percentage can be calculated using the formula: (distance domicile-travail x 2 x 200 working days + private km) / total km. For mixed-use vehicles, the 50% cap applies. Default: 50% deductible (most common for self-employed).

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Grille | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | ARVAL BELGIUM | -650.00 | -537.19 | -112.81 (x 50% = -56.40 deductible) | 21% | 82/63 (partial) | Y | Q3 | "Vehicle: max 50% TVA deductible. Confirm professional use %." |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 21% (Art. 37 §1 CTVA)

Default rate. Sales → grille 03/54. Purchases → grille 81 or 82 or 83 / grille 63.

### 5.2 Reduced rate 12% (Table B, Annex to AR no. 20)

Restaurant meals (food + non-alcoholic drinks), social housing, certain energy products (margarine). Sales → grille 02/54. Purchases → grille 81 or 82 / 63.

### 5.3 Reduced rate 6% (Table A, Annex to AR no. 20)

Basic foodstuffs, water supply, books, medicines, hotels, renovation of old residential buildings (>10 years), passenger transport, cultural events (concerts, theatre, museums), social housing rehabilitation. Sales → grille 01/54. Purchases → grille 81 or 82 / 63.

### 5.4 Zero rate

Exports → grille 00 (with export evidence). Intra-EU goods → grille 46 (with VIES). Intra-EU B2B services → grille 45.

### 5.5 Exempt without credit (Art. 44 CTVA)

Medical, education, insurance, financial services, residential rent, postal universal service. If significant → **R-BE-3 refuses**.

### 5.6 Local purchases

Input VAT on compliant invoice. Goods → grille 81, services → grille 82, capital goods → grille 83. Input VAT → grille 63.

### 5.7 Co-contractor reverse charge (medecontractant / cocontractant)

Belgium has a domestic co-contractor reverse charge for construction work (Art. 20 AR no. 1), real estate transactions, and certain other sectors. The customer self-assesses VAT. Base → grille 87, output VAT → grille 56, input → grille 63. Invoices must mention "TVA due par le cocontractant" or "BTW verlegd".

### 5.8 Reverse charge — EU services (Art. 21 §2 CTVA)

EU service: base → grille 88, output VAT → grille 55, input → grille 63. Net zero.

### 5.9 Reverse charge — EU goods (intracommunautaire verwervingen)

EU goods: base → grille 86, output VAT → grille 55, input → grille 63.

### 5.10 Reverse charge — non-EU

Non-EU services/goods: base → grille 87, output VAT → grille 56, input → grille 63. If goods import with ET 14 licence → base grille 87, output → grille 57.

### 5.11 Capital goods (investissements)

Assets used for >1 year → grille 83. Subject to herzieningstermijn (5 years movable, 15 years immovable). No explicit minimum value threshold for TVA capitalisation.

### 5.12 Blocked/restricted input VAT

- Motor vehicles: max 50% deductible (Art. 45 §2 CTVA). Professional use formula or lump sum.
- Fuel: follows vehicle deduction percentage (max 50%).
- Restaurant meals: TVA deductible if business purpose documented. Alcohol excluded.
- Entertainment/reception (frais de réception): TVA fully deductible for VAT purposes (unlike 50% income tax deduction). BUT personal entertainment blocked.
- Gifts: TVA deductible if unit value ≤ €50 (excluding VAT) per occasion.
- Tobacco: not deductible.
- Hotel accommodation for staff: not deductible. For clients/third parties: deductible.

### 5.13 Co-contractor reverse charge (construction detail)

For registered construction contractors: when a registered contractor provides construction services to another registered contractor, the customer self-assesses. The supplier invoices without VAT and mentions "BTW verlegd — medecontractant" or "Autoliquidation — Art. 20 AR n° 1". This is uniquely Belgian — not found in all EU member states.

### 5.14 Sales — local domestic

Charge 21%, 12%, or 6%. Map to grille 01/02/03 + 54.

### 5.15 Sales — cross-border B2C

Above €10,000 EU-wide → **R-EU-5 OSS refusal fires**.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* TOTAL, SHELL, Q8, TEXACO. *Default:* 50% deductible (vehicle cap). *Question:* "What is the professional use percentage?"

### 6.2 Restaurants and entertainment

*Pattern:* restaurant, brasserie, café. *Default:* block. *Question:* "Business meal? Names and purpose? Note: alcohol VAT never deductible."

### 6.3 Ambiguous SaaS billing entities

*Default:* non-EU reverse charge (87/56/63). *Question:* "Check invoice for legal entity."

### 6.4 Round-number owner transfers

*Default:* exclude. *Question:* "Customer payment, own money, or loan?"

### 6.5 Incoming from individuals

*Default:* domestic B2C 21%. *Question:* "Sale? Business or consumer?"

### 6.6 Foreign counterparty incoming

*Default:* domestic 21%. *Question:* "B2B with VAT number, B2C, goods or services, country?"

### 6.7 Large one-off purchases

*Default:* grille 83 if capital good. *Question:* "Confirm invoice amount."

### 6.8 Mixed-use phone, internet

*Default:* 0%. *Question:* "Dedicated business or mixed?"

### 6.9 Outgoing to individuals

*Default:* exclude. *Question:* "Contractor, wages, refund, or personal?"

### 6.10 Cash withdrawals

*Default:* exclude. *Question:* "What was cash used for?"

### 6.11 Rent

*Default:* no VAT (residential). *Question:* "Commercial with TVA option?"

### 6.12 Foreign hotel

*Default:* exclude from input. *Question:* "Business trip?"

### 6.13 Airbnb income

*Default:* [T2] flag. *Question:* "Duration? Tourist accommodation?"

### 6.14 Co-contractor construction reverse charge

*Pattern:* construction companies, entrepreneurs. *Default:* [T2] flag. *Question:* "Is this construction work subject to co-contractor reverse charge (medecontractant)?"

### 6.15 Platform sales

*Default:* if EU cross-border above €10,000 → R-EU-5. Otherwise: domestic 21%. *Question:* "Sell outside Belgium?"

---

## Section 7 — Excel working paper template (Belgium-specific)

The base specification is in `vat-workflow-base` Section 3.

### Sheet "Transactions"

Column H accepts grille codes from Section 1.

### Sheet "Grille Summary"

```
| 01 | Sales 6% base | =SUMIFS(...) |
| 02 | Sales 12% base | =SUMIFS(...) |
| 03 | Sales 21% base | =SUMIFS(...) |
| 45 | Intra-EU services provided | =SUMIFS(...) |
| 46 | Intra-EU goods supplied | =SUMIFS(...) |
| 54 | Output VAT on domestic sales | =01*0.06 + 02*0.12 + 03*0.21 |
| 55 | Output VAT on EU reverse charge | =(86+88)*0.21 |
| 56 | Output VAT on non-EU/co-contractor | =87*0.21 |
| 59 | Total output VAT | =54+55+56+57 |
| 81 | Purchases goods base | =SUMIFS(...) |
| 82 | Purchases services base | =SUMIFS(...) |
| 83 | Capital goods base | =SUMIFS(...) |
| 86 | EU goods acquired base | =SUMIFS(...) |
| 88 | EU services received base | =SUMIFS(...) |
| 87 | Other acquisitions base | =SUMIFS(...) |
| 63 | Total deductible input VAT | =SUM(input VAT) |
| 71 | Net payable | =MAX(0, 59-63) |
| 72 | Net credit | =MAX(0, 63-59) |
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/belgium-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Belgian bank statement reading guide

**CSV format conventions.** Belgian banks export CSV with semicolons and DD/MM/YYYY. Common columns: Datum/Date, Omschrijving/Description, Bedrag/Montant, Saldo/Solde. KBC uses structured export; Belfius and BNP Paribas Fortis use similar formats.

**Bilingual descriptions.** Belgium has three official languages (Dutch, French, German). Bank statements may use: loyer/huur (rent), salaire/loon (salary), intérêts/rente (interest), virement/overschrijving (transfer), cotisations/bijdragen (contributions).

**Internal transfers.** "Virement interne", "interne overboeking". Exclude.

**SPF Finances payments.** Tax payments appear as "SPF FINANCES", "FOD FINANCIEN", or with structured communications (+++XXX/XXXX/XXXXX+++). Always exclude.

**Structured communication.** Belgian payments often use structured communication (+++XXX/XXXX/XXXXX+++). This is a reference number, not a classification indicator.

**Foreign currency.** Convert to EUR at ECB rate.

**IBAN prefix.** BE = Belgium. NL, FR, DE, LU = EU. US, GB = non-EU.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type
*Inference rule:* SPRL/BVBA = old company form; SRL/BV = new company form; personne physique/eenmanszaak = sole trader. *Fallback:* "SRL/BV, SA/NV, or sole trader (indépendant/zelfstandige)?"

### 9.2 VAT regime
*Fallback:* "Standard regime, franchise (small enterprise exemption), or forfaitaire?"

### 9.3 TVA/BTW number
*Fallback:* "Your Belgian TVA/BTW number? (BE + 10 digits)"

### 9.4 Filing period
*Fallback:* "Which month or quarter?"

### 9.5 Industry
*Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* ONSS/RSZ outgoing. *Fallback:* "Employees?"

### 9.7 Exempt supplies
*Fallback:* "Any exempt sales?" *If yes → R-BE-3.*

### 9.8 Credit carried forward
*Always ask.* "TVA/BTW credit from prior period? (Grille 72)"

### 9.9 Cross-border customers
*Fallback:* "Customers outside Belgium? EU/non-EU? B2B/B2C?"

### 9.10 Construction sector
*Conditional:* "Are you in construction? (Co-contractor reverse charge may apply.)"

---

## Section 10 — Reference material

### Sources

1. Code de la TVA (CTVA) / BTW-Wetboek — https://finances.belgium.be
2. Arrêtés royaux d'exécution (AR no. 1, no. 20, etc.)
3. Table A (6%) and Table B (12%) — Annexes to AR no. 20
4. SPF Finances / FOD Financiën guidance on periodic returns
5. Council Directive 2006/112/EC — via eu-vat-directive companion
6. VIES — https://ec.europa.eu/taxation_customs/vies/

### Known gaps

1. Bilingual descriptions not exhaustively mapped.
2. Co-contractor construction reverse charge flagged T2 only.
3. ET 14 import licence details not covered.
4. Vehicle deduction percentage formula simplified to 50% cap.
5. Temporary reduced rates (energy measures) require annual verification.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure.
- **v1.0/1.1:** Initial skill.

### Self-check (v2.0)

1. Quick reference: yes. 2. Supplier library (15): yes. 3. Worked examples (6): yes. 4. Tier 1 (15): yes. 5. Tier 2 (15): yes. 6. Excel template: yes. 7. Onboarding (10): yes. 8. 8 refusals: yes. 9. Reference material: yes. 10. Vehicle 50% cap: yes. 11. Co-contractor reverse charge: yes. 12. Restaurant 12% rate: yes. 13. Grille system: yes. 14. Bilingual considerations: yes. 15. Non-EU SaaS 87/56: yes.

## End of Belgium VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a comptable-fiscaliste, bedrijfsrevisor, or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
