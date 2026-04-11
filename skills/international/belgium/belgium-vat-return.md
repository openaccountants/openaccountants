---
name: belgium-vat-return
description: Use this skill whenever asked to prepare, review, or create a Belgian VAT return (declaration periodique TVA / periodieke BTW-aangifte) for any client. Trigger on phrases like "prepare VAT return", "do the Belgian VAT", "BTW-aangifte", "declaration TVA Belgique", "periodieke aangifte", or any request involving Belgian VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Belgian VAT classification rules, grid/case mappings (cadre/rooster), deductibility rules, co-contractor reverse charge, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Belgium.
status: deep-research-verified
version: 1.1
---

# Belgium VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Belgium (Belgique / Belgie) |
| Jurisdiction Code | BE |
| Primary Legislation | Code de la TVA / BTW-Wetboek (CTVA / WBTW) |
| Supporting Legislation | Art 44 CTVA (exemptions); Art 45 CTVA (deductibility restrictions); Art 51 CTVA (reverse charge / co-contractor); Art 56bis CTVA (small enterprise scheme); Arrete Royal (KB/AR) nr.1-59 (Royal Decrees) |
| Tax Authority | Service Public Federal Finances / Federale Overheidsdienst Financien (SPF Finances / FOD Financien) |
| Filing Portal | Intervat via MyMINFIN (https://eservices.minfin.fgov.be/intervat) |
| Official Languages | French (FR), Dutch (NL), German (DE) -- all three are official; forms are bilingual FR/NL; German-speaking community uses FR forms |
| Contributor | Deep research verified -- April 2026 |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: grid assignment, co-contractor reverse charge, deductibility blocks, derived calculations, filing deadlines. Tier 2: pro-rata, sector-specific regimes, renovation rate conditions, car deduction percentages above 50%. Tier 3: VAT unit (unite TVA / BTW-eenheid), complex real estate, special agricultural scheme, toll manufacturing. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed accountant (expert-comptable / accountant) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and BTW/TVA number** [T1] -- Format: BE 0XXX.XXX.XXX (enterprise number with "BE" prefix, 10 digits). The enterprise number (numero d'entreprise / ondernemingsnummer) is also the VAT identification number when prefixed with BE. Example: BE 0123.456.789.
2. **VAT regime** [T1] -- Normal (regime normal / normaal stelsel), flat-rate (regime forfaitaire / forfaitair stelsel), small enterprise scheme (regime de la franchise / vrijstellingsregeling), or exempt (Art 44 CTVA).
3. **Filing frequency** [T1] -- Monthly (mandatory if annual turnover > EUR 2,500,000 or certain sectors including energy products, motor vehicles) or quarterly (default for turnover <= EUR 2,500,000). Art 53 CTVA; AR nr. 1, Art 18.
4. **Industry/sector** [T2] -- impacts pro-rata, special schemes (agriculture, real estate, second-hand goods).
5. **Does the business make exempt supplies (Art 44 CTVA)?** [T2] -- If yes, partial deduction (pro-rata / pro rata) required under Art 46 CTVA. Reviewer must confirm rate.
6. **TVA/BTW credit carried forward from prior period** [T1] -- Grid 71 credit balance.
7. **Is the client in the small enterprise scheme (Art 56bis)?** [T1] -- Turnover <= EUR 25,000 excl. VAT.
8. **Does the client use the ET14000 import VAT deferment?** [T1] -- If yes, import VAT reported on return rather than paid at customs.
9. **Language preference for invoicing?** [T1] -- FR, NL, or DE. Impacts mandatory invoice mentions.

For small enterprise clients [T1]: confirm annual turnover <= EUR 25,000 excl. VAT. Art 56bis CTVA.

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Step 1: VAT Return Form Structure (Declaration Periodique / Periodieke Aangifte) [T1]

**Legislation:** Art 53 CTVA; AR nr. 1; Intervat filing instructions.

The Belgian periodic VAT return is structured into seven sections called "cadres" (FR) / "roosters" (NL) / "frames" (EN), numbered I through VII. Each contains numbered grids/cases (cases / vakken). The return is filed electronically via the Intervat portal on MyMINFIN.

### Cadre/Rooster I: Opérations à la sortie / Uitgaande handelingen / Output Transactions

These grids record the taxable base (excluding VAT) of supplies made by the taxable person.

| Grid | FR: Description | NL: Description | EN: Description |
|------|----------------|-----------------|-----------------|
| 00 | Operations soumises a un regime particulier | Handelingen onderworpen aan een bijzondere regeling | Transactions subject to a special regime (margin scheme, travel agents, second-hand goods -- Art 58 CTVA) |
| 01 | Operations soumises au taux de 6% | Handelingen onderworpen aan het tarief van 6% | Supplies and services taxable at 6% |
| 02 | Operations soumises au taux de 12% | Handelingen onderworpen aan het tarief van 12% | Supplies and services taxable at 12% |
| 03 | Operations soumises au taux de 21% | Handelingen onderworpen aan het tarief van 21% | Supplies and services taxable at 21% |

### Cadre/Rooster II: Opérations à la sortie (suite) / Uitgaande handelingen (vervolg) / Output Transactions (continued)

| Grid | FR: Description | NL: Description | EN: Description |
|------|----------------|-----------------|-----------------|
| 44 | Services pour lesquels la TVA est due par le cocontractant (Art 51 §2) | Diensten waarvoor de BTW verschuldigd is door de medecontractant | Services where VAT is due by the co-contractor (reverse charge on services supplied -- domestic and EU) |
| 45 | Livraisons intracommunautaires exemptees et ventes ABC | Vrijgestelde intracommunautaire leveringen en ABC-verkopen | Exempt intra-Community supplies of goods and triangular trade (ABC) |
| 46 | Autres operations exemptees et autres operations effectuees a l'etranger | Andere vrijgestelde handelingen en handelingen verricht in het buitenland | Other exempt operations with right to deduct and operations performed abroad (exports, non-EU services) |
| 47 | Operations exemptees par l'Art 44 effectuees en Belgique | Door Art 44 vrijgestelde handelingen verricht in Belgie | Exempt supplies under Art 44 CTVA performed in Belgium (medical, education, insurance, financial services -- NO right to deduction) |

### Cadre/Rooster III: Notes de credit / Creditnota's / Credit Notes (Output)

| Grid | FR: Description | NL: Description | EN: Description |
|------|----------------|-----------------|-----------------|
| 48 | Notes de credit emises relatives aux operations inscrites en grilles 01, 02 et 03 | Uitgereikte creditnota's met betrekking tot handelingen ingeschreven in roosters 01, 02 en 03 | Credit notes issued relating to supplies in Grids 01, 02, 03 (reduces taxable base at the applicable rate) |
| 49 | Notes de credit emises relatives aux operations inscrites en grilles 44, 45, 46 et 47 | Uitgereikte creditnota's met betrekking tot handelingen ingeschreven in roosters 44, 45, 46 en 47 | Credit notes issued relating to operations in Grids 44, 45, 46, 47 |

### Cadre/Rooster IV: Opérations à l'entrée / Inkomende handelingen / Input Transactions

These grids record the taxable base (excluding VAT) of goods and services acquired.

| Grid | FR: Description | NL: Description | EN: Description |
|------|----------------|-----------------|-----------------|
| 81 | Achats de marchandises commerciales, matieres premieres et matieres auxiliaires | Aankoop van handelsgoederen, grondstoffen en hulpstoffen | Purchases of commercial goods, raw materials and auxiliary materials (goods for resale and production inputs) |
| 82 | Achats de services et biens divers | Aankoop van diensten en diverse goederen | Purchases of services and miscellaneous goods (overheads, utilities, professional fees, rent, insurance premiums for taxable operations) |
| 83 | Achats de biens d'investissement | Aankoop van bedrijfsmiddelen | Purchases of capital/investment goods (assets intended for long-term use in the business) |

### Cadre/Rooster IV (continued): Notes de credit / Creditnota's / Credit Notes (Input)

| Grid | FR: Description | NL: Description | EN: Description |
|------|----------------|-----------------|-----------------|
| 84 | Notes de credit recues relatives aux operations inscrites en grilles 81, 82 et 83 | Ontvangen creditnota's met betrekking tot handelingen ingeschreven in roosters 81, 82 en 83 | Credit notes received relating to purchases in Grids 81, 82, 83 (reduces purchase base) |
| 85 | Notes de credit recues relatives aux operations inscrites en grilles 86 et 88 | Ontvangen creditnota's met betrekking tot handelingen ingeschreven in roosters 86 en 88 | Credit notes received relating to operations in Grids 86, 87, 88 (reduces IC acquisitions and reverse charge base) |

### Cadre/Rooster IV (continued): Intra-Community and Reverse Charge Acquisitions

| Grid | FR: Description | NL: Description | EN: Description |
|------|----------------|-----------------|-----------------|
| 86 | Acquisitions intracommunautaires de biens et operations assimilees | Intracommunautaire verwervingen van goederen en ermee gelijkgestelde handelingen | Intra-Community acquisitions of goods and similar operations (physical goods from EU suppliers) |
| 87 | Autres operations a l'entree avec report de perception | Andere inkomende handelingen met verlegging van heffing | Other input operations with reverse charge (non-EU services, domestic co-contractor construction, import VAT deferment ET14000) |
| 88 | Acquisitions intracommunautaires de services | Intracommunautaire verwervingen van diensten | Intra-Community acquisitions of services (B2B services received from EU suppliers -- Art 21 ss2 CTVA) |

### Cadre/Rooster V: TVA due / Verschuldigde BTW / VAT Due (Output Tax)

| Grid | FR: Description | NL: Description | EN: Description |
|------|----------------|-----------------|-----------------|
| 54 | TVA due sur les operations inscrites en grilles 01, 02 et 03 | Verschuldigde BTW over de handelingen ingeschreven in roosters 01, 02 en 03 | Output VAT on domestic supplies (Grids 01, 02, 03). Calculated: (Grid 01 x 6%) + (Grid 02 x 12%) + (Grid 03 x 21%) |
| 55 | TVA due sur les operations inscrites en grilles 86 et 88 | Verschuldigde BTW over de handelingen ingeschreven in roosters 86 en 88 | VAT due on IC acquisitions of goods (Grid 86) and IC services received (Grid 88). Self-assessed at applicable Belgian rate. |
| 56 | TVA due sur les operations inscrites en grille 87 | Verschuldigde BTW over de handelingen ingeschreven in rooster 87 | VAT due on reverse charge operations (Grid 87): non-EU services, co-contractor construction, import VAT deferment. Self-assessed at applicable Belgian rate. |
| 57 | TVA due en raison des notes de credit recues inscrites en grille 84 | Verschuldigde BTW ingevolge ontvangen creditnota's ingeschreven in rooster 84 | VAT adjustment due to credit notes received (Grid 84). Repayment of previously deducted input VAT. |
| 61 | Diverses regularisations de TVA en faveur de l'Etat | Diverse BTW-regularisaties in het voordeel van de Staat | Various VAT regularisations in favour of the State (corrections, adjustments, revision of capital goods deductions owing to State) |
| 63 | TVA a reverser mentionnee sur les notes de credit emises | Terug te storten BTW vermeld op de uitgereikte creditnota's | VAT to be repaid as shown on credit notes issued (reduces output VAT previously declared) |

### Cadre/Rooster VI: TVA déductible / Aftrekbare BTW / Deductible VAT (Input Tax)

| Grid | FR: Description | NL: Description | EN: Description |
|------|----------------|-----------------|-----------------|
| 59 | TVA deductible | Aftrekbare BTW | Total deductible input VAT. Includes VAT on domestic purchases (Grids 81-83), self-assessed VAT on reverse charge (Grids 55, 56) where deductible, and VAT on imports. Subject to deductibility restrictions (Art 45 CTVA). |
| 62 | Diverses regularisations de TVA en faveur du declarant | Diverse BTW-regularisaties in het voordeel van de aangever | Various VAT regularisations in favour of the declarant (corrections, adjustments, revision of capital goods deductions in favour of declarant) |
| 64 | TVA sur les notes de credit emises relatives aux operations inscrites en grilles 01, 02, 03 | BTW op de uitgereikte creditnota's met betrekking tot handelingen ingeschreven in roosters 01, 02, 03 | VAT on credit notes issued (recovery of output VAT previously charged on sales now credited) |

### Cadre/Rooster VII: Solde / Saldo / Balance

| Grid | FR: Description | NL: Description | EN: Calculation |
|------|----------------|-----------------|-----------------|
| XX | Total TVA due | Totaal verschuldigde BTW | Sum of: Grid 54 + Grid 55 + Grid 56 + Grid 57 + Grid 61 + Grid 63 |
| YY | Total TVA deductible | Totaal aftrekbare BTW | Sum of: Grid 59 + Grid 62 + Grid 64 |
| 71 | TVA a payer a l'Etat | Aan de Staat te betalen BTW | VAT payable to the State: IF XX > YY THEN Grid 71 = XX - YY |
| 72 | Sommes dues par l'Etat | Sommen verschuldigd door de Staat | VAT credit (refund or carry forward): IF YY > XX THEN Grid 72 = YY - XX |
| 91 | Montant total des operations a la sortie (pour info) | Totaalbedrag van de uitgaande handelingen (ter info) | Total output operations for information: Grid 00 + 01 + 02 + 03 + 44 + 45 + 46 + 47 - 48 - 49 |

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]

**Legislation:** Art 2-4 CTVA.

| Transaction | Classification | Action |
|-------------|---------------|--------|
| Sale of goods | Output / TVA due | Grids 00-03 or 44-47 |
| Provision of services | Output / TVA due | Grids 00-03 or 44-47 |
| Purchase of goods | Input / TVA deductible | Grids 81-83 or 86-88 |
| Purchase of services | Input / TVA deductible | Grids 82 or 86-88 |
| Salaries (remunerations / lonen) | OUT OF SCOPE | Never on VAT return |
| Social security (ONSS/RSZ contributions) | OUT OF SCOPE | Never on VAT return |
| Income tax (IPP/PB, ISOC/VenB) | OUT OF SCOPE | Never on VAT return |
| Loan repayments (capital + interest) | OUT OF SCOPE | Never on VAT return |
| Dividends | OUT OF SCOPE | Never on VAT return |
| Bank charges (frais bancaires / bankkosten) | OUT OF SCOPE | Exempt financial services, no VAT |
| Insurance premiums | OUT OF SCOPE | Exempt under Art 44 ss3 2deg CTVA |

### 2b. Determine Counterparty Location [T1]

| Location | Definition | Impact |
|----------|------------|--------|
| Belgium (BE) | Supplier or customer established in Belgium | Normal domestic rules |
| EU | All other EU Member States: AT, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE | Reverse charge / IC rules |
| Non-EU | All others (US, UK, CH, AU, etc.) | Reverse charge / export rules |

**Note:** UK is Non-EU post-Brexit. Switzerland is Non-EU. Northern Ireland has special goods status (XI prefix).

### 2c. Determine Expense Category for Purchases [T1]

| Category | FR Term | NL Term | Grid | Criteria |
|----------|---------|---------|------|----------|
| Commercial goods / raw materials | Marchandises, matieres premieres | Handelsgoederen, grondstoffen | 81 | Goods for resale or production inputs |
| Services and miscellaneous goods | Services et biens divers | Diensten en diverse goederen | 82 | Overheads, professional fees, rent, utilities, repairs, office supplies |
| Capital/investment goods | Biens d'investissement | Bedrijfsmiddelen | 83 | Assets for long-term business use (machinery, vehicles, IT equipment, furniture) |

**Note:** Unlike Malta, Belgium does not have a specific monetary threshold for capital goods classification. Classification follows accounting standards (assets intended for durable use in the business). Art 6 AR nr. 3.

---

## Step 3: Transaction Classification Matrix -- Lookup Tables [T1]

**Legislation:** Art 53 CTVA; AR nr. 1; Intervat instructions.

### Table A: Domestic Sales (Supplier = BE, Customer = BE)

| Supply Type | Rate | Base Grid | VAT Grid | Legal Basis |
|-------------|------|-----------|----------|-------------|
| Standard goods/services | 21% | 03 | 54 | Art 37 ss1 CTVA |
| Reduced-rate goods (margarine, social housing, restaurant food) | 12% | 02 | 54 | Art 37 ss1 CTVA; Table B AR nr. 20 |
| Basic necessities, water, books, hotels, renovation > 10 yrs | 6% | 01 | 54 | Art 37 ss1 CTVA; Table A AR nr. 20 |
| Margin scheme (second-hand, art, antiques) | Special | 00 | 54 | Art 58 ss4 CTVA |
| Exempt without credit (medical, education, finance, insurance) | Exempt | 47 | -- | Art 44 CTVA |
| Construction services to VAT-registered co-contractor | RC | 44 | -- | Art 51 ss2 CTVA; Art 20 AR nr. 1 |

### Table B: Intra-Community Sales (Supplier = BE, Customer = EU)

| Supply Type | Base Grid | VAT Grid | Legal Basis |
|-------------|-----------|----------|-------------|
| IC supply of goods (B2B, goods shipped to other EU state) | 45 | -- | Art 39bis CTVA |
| Triangular trade (ABC -- BE is intermediary) | 45 | -- | Art 25quinquies CTVA |
| B2B services to EU customer (general rule Art 21 ss2) | 44 | -- | Art 21 ss2 CTVA |

### Table C: Non-EU Sales (Supplier = BE, Customer = Non-EU)

| Supply Type | Base Grid | VAT Grid | Legal Basis |
|-------------|-----------|----------|-------------|
| Export of goods | 46 | -- | Art 39 CTVA |
| Services to non-EU customer (general rule) | 46 | -- | Art 21 ss2 CTVA |

### Table D: Domestic Purchases (Supplier = BE, Customer = BE)

| Expense Type | Rate | Base Grid | Input VAT Grid | Legal Basis |
|--------------|------|-----------|----------------|-------------|
| Commercial goods at 21% | 21% | 81 | 59 | Art 45 ss1 CTVA |
| Commercial goods at 6% | 6% | 81 | 59 | Art 45 ss1 CTVA |
| Services/overheads at 21% | 21% | 82 | 59 | Art 45 ss1 CTVA |
| Services/overheads at 6% | 6% | 82 | 59 | Art 45 ss1 CTVA |
| Capital goods at 21% | 21% | 83 | 59 | Art 45 ss1 CTVA |
| Capital goods at 6% | 6% | 83 | 59 | Art 45 ss1 CTVA |
| Blocked category (entertainment, tobacco, etc.) | Any | 82 or 83 | -- (blocked) | Art 45 ss3 CTVA |

### Table E: Intra-Community Purchases (Supplier = EU, Customer = BE)

| Type | Purchase Base Grid | VAT Due Grid | Input VAT Grid | Legal Basis |
|------|-------------------|--------------|----------------|-------------|
| IC acquisition of goods | 86 | 55 | 59 | Art 25ter CTVA; Art 51 ss2 CTVA |
| IC services received (Art 21 ss2 -- B2B general rule) | 88 | 55 | 59 | Art 21 ss2 CTVA; Art 51 ss2 CTVA |

### Table F: Non-EU Purchases (Supplier = Non-EU, Customer = BE)

| Type | Purchase Base Grid | VAT Due Grid | Input VAT Grid | Legal Basis |
|------|-------------------|--------------|----------------|-------------|
| Services from non-EU (reverse charge) | 87 | 56 | 59 | Art 21 ss2 CTVA; Art 51 ss2 CTVA |
| Import VAT deferment (ET14000 licence) | 87 | 56 | 59 | Art 51 ss2 CTVA; AR nr. 7 |
| Import VAT paid at customs (no ET14000) | -- | -- | 59 | Art 45 ss1 CTVA; customs document |

### Table G: Domestic Reverse Charge (Co-contractor -- Supplier = BE, Customer = BE)

| Type | Supplier Grid | Customer Base Grid | Customer VAT Due Grid | Customer Input VAT Grid | Legal Basis |
|------|---------------|-------------------|----------------------|------------------------|-------------|
| Construction / immovable property | 44 | 87 | 56 | 59 | Art 51 ss2 CTVA; Art 20 AR nr. 1 |

### Table H: Credit Notes

| Credit Note Type | Base Grid | VAT Grid | Legal Basis |
|------------------|-----------|----------|-------------|
| CN issued on sales at 6%/12%/21% (Grids 01-03) | 48 | 64 | Art 77 CTVA |
| CN issued on operations in Grids 44-47 | 49 | -- | Art 77 CTVA |
| CN received on domestic purchases (Grids 81-83) | 84 | 57 | Art 77 CTVA |
| CN received on IC/RC acquisitions (Grids 86-88) | 85 | -- | Art 77 CTVA |

---

## Step 4: VAT Rates -- Detailed Supply Classification [T1]

**Legislation:** Art 37-38 CTVA; AR nr. 20 (Tables A, B, C).

### 4a. Standard Rate: 21% [T1]

**Legal Basis:** Art 37 ss1 CTVA. Default rate for all goods and services not explicitly listed in Tables A or B of AR nr. 20.

Applies to (non-exhaustive):
- Professional services (legal, accounting, consulting, IT)
- Telecommunications and electronically supplied services
- New motor vehicles
- Electrical and electronic equipment
- Clothing and footwear
- Furniture (new)
- Alcoholic beverages (including restaurant service of alcohol)
- Construction work on new buildings (first occupation)
- Software licences
- Advertising services
- Rental of movable goods

### 4b. Reduced Rate: 12% [T1]

**Legal Basis:** Art 37 ss1 CTVA; Table B, AR nr. 20.

| Supply | Description | AR nr. 20 Reference |
|--------|-------------|---------------------|
| Restaurant and catering services | Food served in restaurants, cafes, catering (EXCLUDING alcoholic beverages which remain 21%). **NOTE: From 1 March 2026, non-alcoholic beverages served in restaurants/cafes move from 21% to 12%.** | Table B, rubrique XXXIII |
| Margarine | Margarine products | Table B, rubrique I |
| Social housing | Construction, renovation of social housing (conditions apply) | Table B, rubrique X |
| Phytopharmaceutical products | Plant protection products. **NOTE: From 1 March 2026, pesticides/phytopharmaceutical products move from 12% to 21% (standard rate).** | Table B, rubrique II (until 28 February 2026) |
| Combustible materials | Certain solid combustible materials (coal, lignite) | Table B, rubrique V |
| Inner tubes and tyres | For agricultural use | Table B, rubrique IV |
| Pay television | Subscription television services | Table B, rubrique XXXV |

### 4c. Reduced Rate: 6% [T1]

**Legal Basis:** Art 37 ss1 CTVA; Table A, AR nr. 20.

| Supply | Description | AR nr. 20 Reference |
|--------|-------------|---------------------|
| Basic foodstuffs | Food for human consumption (excluding alcohol, restaurant services) | Table A, rubrique I |
| Pharmaceutical products | Medicines, medical devices | Table A, rubrique XXIII |
| Water distribution | Via pipelines | Table A, rubrique XVIII |
| Books and publications | Printed books, newspapers, periodicals; electronic publications (from 2020) | Table A, rubrique XIX |
| Passenger transport | Public transport of persons | Table A, rubrique VI |
| Hotel accommodation | Hotels, guest houses, camping sites (lodging only, not minibar/restaurant). **NOTE: From 1 March 2026, hotel and campsite accommodation moves from 6% to 12% (Table B). Transitional rule: reservations made before 1 March 2026 and paid/invoiced by 30 June 2026 remain at 6%.** | Table A, rubrique XXVIII (until 28 February 2026); Table B from 1 March 2026 |
| Renovation of private dwellings > 10 years | Construction work on dwellings occupied for > 10 years (conditions: dwelling > 10 years old, used as private residence, work invoiced to end consumer) | Table A, rubrique XXXVIII |
| Repair services | Bicycles, shoes, leather goods, clothing, household linen | Table A, rubrique XXVI |
| Agricultural inputs | Seeds, plants, fertilisers, pesticides for agriculture | Table A, rubrique III |
| Social housing | Delivery and construction | Table A, rubrique XXXVI |
| Cultural/sporting events | Entry fees to museums, theatres, concerts, sports events, zoos | Table A, rubrique XXVII |
| Copyrights | Transfer of copyrights by authors, artists, performers | Table A, rubrique XX |
| Demolition and reconstruction | Demolition of old building and reconstruction of dwelling (in 32 cities + nationwide until 2024, extended conditions from 2024) | Table A, rubrique XXXVII |
| Electricity and natural gas | For household use (residential contracts) | Table A, rubrique XXXVIIBIS |
| Heat pumps | For residential property (with energy conditions) | Table A, rubrique XXXVIIIQUATER |
| Intimate hygiene products | Sanitary towels, tampons, menstrual cups | Table A, rubrique XXXVIIIQUINQUIES |
| Defibrillators | External defibrillator maintenance and rental | Table A, rubrique XXXVIIIOCTIES |

### 4d. Zero Rate (0%) -- Exempt with Credit [T1]

**Legal Basis:** Art 39-42 CTVA.

| Supply | Description | Legal Basis |
|--------|-------------|-------------|
| Exports | Goods dispatched or transported outside the EU | Art 39 CTVA |
| Intra-Community supplies | B2B supplies of goods shipped to another EU Member State | Art 39bis CTVA |
| Newspapers (daily/periodic publications) | Certain periodic publications meeting specific criteria | Art 42 ss3 1deg CTVA; Table C AR nr. 20 |
| International transport | Transport of goods in connection with export/import | Art 40 CTVA |
| Supplies to diplomats | Goods and services to diplomatic missions | Art 42 ss1 CTVA |
| Goods under customs suspension | Goods placed under customs warehousing, free zones | Art 40bis CTVA |

### 4e. Exempt without Credit [T1]

**Legal Basis:** Art 44 CTVA. NO input VAT deduction on related costs.

| Supply | Description | Legal Basis |
|--------|-------------|-------------|
| Medical and paramedical services | Doctors, dentists, hospitals, physiotherapists | Art 44 ss1 CTVA |
| Education | Schools, universities, professional training | Art 44 ss2 2deg CTVA |
| Financial services | Banking, credit, securities transactions | Art 44 ss3 5deg-11deg CTVA |
| Insurance | Insurance and reinsurance | Art 44 ss3 4deg CTVA |
| Real estate (sale/rental) | Sale of old buildings (> 2 years), rental of immovable property (with exceptions) | Art 44 ss3 1deg CTVA |
| Sports (non-profit) | Sports services by non-profit organisations | Art 44 ss2 3deg CTVA |
| Cultural services (non-profit) | Libraries, museums operated by public bodies | Art 44 ss2 7deg CTVA |

---

## Step 5: Blocked Input Tax (Non-Deductible VAT) [T1]

**Legislation:** Art 45 CTVA.

### 5a. Completely Blocked Categories

| Category | FR Term | NL Term | Rule | Legal Basis |
|----------|---------|---------|------|-------------|
| Entertainment / reception costs | Frais de reception | Receptiekosten | 0% deductible. VAT on catering for receptions, client entertainment events, cocktail parties, inaugurations is NOT deductible. | Art 45 ss3 3deg CTVA |
| Tobacco products | Tabac | Tabak | 0% deductible. | Art 45 ss3 2deg CTVA |
| Accommodation for personnel/directors | Logement du personnel/dirigeants | Huisvesting van personeel/bestuurders | 0% deductible. Housing provided to staff or directors for private use. Exception: hotel rooms for client-facing business events may be deductible. | Art 45 ss3 4deg CTVA |
| Personal use | Usage prive | Privégebruik | 0% deductible on the private-use portion. | Art 45 ss1 CTVA |
| Gifts exceeding EUR 50 | Cadeaux d'affaires > 50 EUR | Relatiegeschenken > 50 EUR | VAT not deductible if gift value > EUR 50 excl. VAT per recipient per year. Below EUR 50: deductible. | Administrative circular nr. 2 of 1 February 1978; Art 45 ss3 CTVA |

### 5b. Partially Restricted: Motor Vehicles (Voitures / Personenwagens)

**Legal Basis:** Art 45 ss2 CTVA.

VAT on passenger vehicles and related expenses (fuel, maintenance, insurance, parking, car wash, leasing) is deductible only up to the percentage of professional use, with an absolute maximum of 50% for the default case.

**Motor Vehicle VAT Deduction Table:**

| Professional Use % | Maximum VAT Deduction % | Proof Required | Tier |
|-------------------|------------------------|----------------|------|
| Unknown / not proven | 50% | None (default rule) | [T1] |
| Proven <= 50% | Actual % proven | Logbook / trip records | [T2] |
| Proven > 50% (e.g. 70%) | Actual % proven (e.g. 70%) | Logbook / trip records -- reviewer must validate | [T2] |
| 100% professional (delivery van, taxi, driving school) | 100% | Business nature of vehicle -- reviewer must validate | [T2] |
| Light utility vehicles (utilitaires / lichte vrachtwagens) | 100% | Vehicle registration as utility | [T1] |
| Minibuses > 8+1 seats | 100% | Vehicle registration | [T1] |

**Fuel follows the same deduction % as the vehicle itself.** Art 45 ss2 CTVA.

**CO2-based deduction method (alternative for company cars from 2020):** For company cars, the deduction percentage may alternatively be computed using the formula: `120% - (0.5% x CO2 coefficient x CO2 g/km)`. Minimum 50%, maximum 100% for zero-emission vehicles. This is used for corporate income tax (Art 66 CIR) and may be applied for VAT by analogy. [T2] -- reviewer to confirm method used.

### 5c. NOT Blocked (Common Misconception)

| Category | Rule | Notes |
|----------|------|-------|
| Restaurant meals (business) | 100% VAT deductible | Unlike income tax (only 69% deductible for CIT), VAT on business restaurant meals is fully deductible. Restaurant meals are NOT in the Art 45 ss3 exclusion list. |
| Alcohol purchased for resale | 100% VAT deductible | If a bar/restaurant buys alcohol for resale, full deduction applies. |
| Hotel for business travel | 100% VAT deductible | Business hotel stays (not staff housing) are deductible. |

### 5d. Treatment of Non-Deductible VAT [T1]

When VAT is blocked (partially or fully), the non-deductible VAT amount is added to the expense base in Grids 81, 82, or 83. Only the deductible portion appears in Grid 59.

**Example:** Car purchase EUR 25,000 + EUR 5,250 VAT (21%). Professional use 50% (default).
- Grid 83 = EUR 25,000 + EUR 2,625 (non-deductible VAT) = EUR 27,625
- Grid 59 = EUR 2,625 (deductible VAT = 50% of EUR 5,250)

---

## Step 6: Registration and Enterprise Number [T1]

### 6a. Enterprise Number Format

**Legal Basis:** Loi du 16 janvier 2003 / Wet van 16 januari 2003.

| Element | Format | Example |
|---------|--------|---------|
| Enterprise number (numero d'entreprise / ondernemingsnummer) | 0XXX.XXX.XXX (10 digits starting with 0) | 0123.456.789 |
| VAT identification number | BE 0XXX.XXX.XXX (prefix BE + enterprise number) | BE 0123.456.789 |
| VIES format (no dots/spaces) | BE0123456789 | BE0123456789 |

The enterprise number is assigned by the Banque-Carrefour des Entreprises (BCE) / Kruispuntbank van Ondernemingen (KBO). VAT registration is an activation of this number for VAT purposes.

### 6b. Small Enterprise Scheme (Regime de la Franchise / Vrijstellingsregeling) [T1]

**Legal Basis:** Art 56bis CTVA; AR nr. 19.

| Criterion | Rule |
|-----------|------|
| Threshold | Annual turnover <= EUR 25,000 excl. VAT |
| Turnover computation | All taxable supplies that would be subject to VAT if not for the scheme. Excludes: sales of capital goods, exempt operations under Art 44. |
| VAT charged on invoices | NO. Must NOT charge VAT. |
| Invoice mention (mandatory) | FR: "Petite entreprise soumise au regime de la franchise de taxe -- TVA non applicable" / NL: "Kleine onderneming onderworpen aan de vrijstellingsregeling van belasting -- BTW niet toepasselijk" |
| Periodic VAT returns | NOT filed. Small enterprises do not file periodic returns. |
| Input VAT recovery | NOT allowed. No right to deduction. |
| Annual customer listing | MUST file (listing annuelle des clients assujettis / jaarlijkse klantenlisting) by 31 March. |
| Exceeding threshold | Must register for normal regime from the transaction that causes the threshold to be exceeded. Art 56bis ss4 CTVA. |
| Voluntary opt-out | Can opt for normal regime even if below threshold. |
| EU-wide SME scheme | From 1 January 2025, EU Directive 2020/285 allows cross-border small enterprise scheme. Belgium implementation conditions apply. [T3] |

### 6c. Normal Registration

| Criterion | Rule | Legal Basis |
|-----------|------|-------------|
| Mandatory registration | Any person who habitually supplies goods or services in Belgium as an economic activity | Art 50 CTVA |
| No minimum threshold | There is no minimum threshold for mandatory VAT registration (unlike the small enterprise OPTION). Any taxable activity triggers obligation. | Art 50 ss1 CTVA |
| Registration timing | Before the first taxable supply | Art 50 CTVA; AR nr. 10 |
| Filing obligation | Periodic returns via Intervat | Art 53 CTVA |

---

## Step 7: Filing Deadlines and Penalties [T1]

### 7a. Filing Frequency

**Legislation:** Art 53 CTVA; AR nr. 1, Art 18.

| Criterion | Monthly Filing | Quarterly Filing |
|-----------|---------------|-----------------|
| Turnover threshold | > EUR 2,500,000 annual turnover (excl. VAT) | <= EUR 2,500,000 annual turnover (excl. VAT) |
| Mandatory monthly sectors | Energy products (accijnsgoederen), motor vehicles -- regardless of turnover | All other sectors below threshold |
| Voluntary monthly | Any taxpayer may opt for monthly filing | -- |
| Return period | Calendar month | Calendar quarter (Jan-Mar, Apr-Jun, Jul-Sep, Oct-Dec) |

### 7b. Deadlines

| Obligation | FR Term | NL Term | Deadline | Legal Basis |
|------------|---------|---------|----------|-------------|
| Monthly VAT return | Declaration mensuelle | Maandelijkse aangifte | 20th of the month following the return period | Art 53 ss1 CTVA; AR nr. 1, Art 18 ss2 |
| Monthly VAT payment | Paiement mensuel | Maandelijkse betaling | 20th of the month following the return period | AR nr. 1, Art 19 |
| Quarterly VAT return | Declaration trimestrielle | Kwartaalaangifte | 20th of the month following the quarter | AR nr. 1, Art 18 ss2 |
| Quarterly VAT payment | Paiement trimestriel | Kwartaalbetaling | 20th of the month following the quarter | AR nr. 1, Art 19 |
| December advance payment (monthly filers) | Acompte de decembre | Voorschot december | 24 December (advance on December return) | AR nr. 1, Art 19 ss3 |
| Annual customer listing (klantenlisting) | Listing annuelle des clients assujettis | Jaarlijkse klantenlisting van de belastingplichtige afnemers | 31 March of the following year | Art 53quinquies CTVA |
| European Sales Listing (IC listing) | Releve intracommunautaire | Opgave van de intracommunautaire handelingen | Filed with each periodic return (monthly or quarterly) | Art 53sexies CTVA |
| Intrastat declaration | Declaration Intrastat | Intrastat-aangifte | 20th of the following month (if thresholds exceeded) | EU Regulation 2019/2152 |
| Annual accounts filing | Comptes annuels | Jaarrekening | Within 7 months of financial year end (filed with NBB/BNB) | Code des Societes et des Associations |

**Note:** Quarterly deadline is the 20th (not the 25th as previously stated in some older references). Confirmed per AR nr. 1, Art 18 ss2 as amended. However, in practice some quarters have historically had extended deadlines (e.g., Q2 deadline sometimes extended to 10 August). Always verify current administrative tolerances.

### 7c. Penalties

**Legislation:** Art 70-73 CTVA; AR nr. 41 (penalty table / tableau des amendes).

| Infraction | FR Term | Penalty | Legal Basis |
|------------|---------|---------|-------------|
| Late filing of return | Declaration tardive | EUR 100 per month of delay (first infraction); escalating for repeat: EUR 200, EUR 500, EUR 1,000, up to EUR 5,000 per month | AR nr. 41, Table G, Section I |
| Non-filing | Defaut de declaration | EUR 500 to EUR 5,000 per return not filed | AR nr. 41, Table G |
| Late payment | Paiement tardif | Interest at 0.8% per month (9.6% annual) on unpaid VAT -- nalatigheidsinterest | Art 91 CTVA |
| Incorrect return (no fraud) | Declaration inexacte | Proportional fine of 10% of the underpaid VAT (first infraction); escalating | AR nr. 41, Table G, Section III |
| Fraud | Fraude | Fine of 200% of the evaded VAT | Art 70 ss2 CTVA |
| Missing invoice mentions | Mentions manquantes | EUR 50 per invoice (max EUR 500 per infraction) | AR nr. 41, Table F |
| No Intervat registration | -- | Return cannot be filed; additional administrative penalties | Art 53 CTVA |

### 7d. Refund of VAT Credits

| Scenario | Rule | Legal Basis |
|----------|------|-------------|
| Quarterly filer with credit (Grid 72) | Credit carried forward to next period by default. Refund may be requested if credit >= EUR 50 (was EUR 615 before 2023 reform). | Art 76 ss1 CTVA |
| Monthly filer with credit | Refund automatically processed if credit >= EUR 50 and return filed on time. Monthly filers with "restitution mensuelle" authorisation get faster refunds. | Art 76 CTVA; AR nr. 4 |
| Starter refund | New businesses can request monthly refunds for the first 24 months regardless of filing frequency (starters scheme). | AR nr. 4, Art 8bis |

---

## Step 8: Reverse Charge / Co-Contractor (Medecontractant / Cocontractant) [T1]

**Legislation:** Art 51 ss2 CTVA; Art 20 AR nr. 1; Art 21 ss2 CTVA.

### 8a. Intra-Community Reverse Charge

| Situation | Purchase Grid | VAT Due Grid | Input VAT Grid | Notes | Legal Basis |
|-----------|--------------|--------------|----------------|-------|-------------|
| IC acquisition of goods | 86 | 55 | 59 | Self-assess at applicable Belgian rate (6%/12%/21%) | Art 25ter CTVA |
| IC services received (B2B, Art 21 ss2 general rule) | 88 | 55 | 59 | Self-assess at applicable Belgian rate | Art 21 ss2 CTVA |

### 8b. Non-EU Reverse Charge

| Situation | Purchase Grid | VAT Due Grid | Input VAT Grid | Notes | Legal Basis |
|-----------|--------------|--------------|----------------|-------|-------------|
| Services from non-EU supplier | 87 | 56 | 59 | Self-assess at applicable Belgian rate | Art 21 ss2 CTVA |
| Import VAT deferment (ET14000) | 87 | 56 | 59 | Licensed importers defer import VAT to return instead of paying at customs | AR nr. 7, Art 5 |

### 8c. Domestic Reverse Charge -- Co-Contractor Construction

**Legal Basis:** Art 51 ss2 CTVA; Art 20 AR nr. 1.

The co-contractor scheme (medecontractant / cocontractant) applies when ALL of the following conditions are met:

1. **Both parties** are VAT-registered in Belgium and file periodic VAT returns (or are members of a VAT unit filing periodic returns). Art 20 AR nr. 1.
2. **The work** relates to immovable property (travaux immobiliers / werken in onroerende staat): construction, renovation, maintenance, repair, cleaning of buildings. Art 19 ss2 CTVA.
3. **Invoice mention** states: "Autoliquidation -- TVA due par le cocontractant, art. 20 AR nr. 1" / "Verlegging van heffing -- BTW verschuldigd door de medecontractant, art. 20 KB nr. 1"

**Mechanics:**

| Party | Action | Grid |
|-------|--------|------|
| Supplier (contractor) | Issues invoice WITHOUT VAT. Reports net amount in Grid 44. | Grid 44 |
| Customer (principal) | Reports net amount in Grid 87. Self-assesses VAT in Grid 56. Claims deductible portion in Grid 59. | Grids 87, 56, 59 |

**If customer is NOT VAT-registered or does not file periodic returns:** co-contractor scheme does NOT apply. Contractor charges VAT normally (Grid 01/02/03 depending on rate).

### 8d. Other Domestic Reverse Charge Situations

| Situation | Supplier Grid | Customer Grids | Legal Basis |
|-----------|--------------|----------------|-------------|
| Disposal of old buildings with VAT option | 44 | 87 / 56 / 59 | Art 8 CTVA; Art 20 AR nr. 1 |
| Supply of recycled materials | 44 | 87 / 56 / 59 | Art 20bis AR nr. 1 |
| Certain energy supplies (electricity/gas certificates) | 44 | 87 / 56 / 59 | Art 20ter AR nr. 1 |

### 8e. Reverse Charge Exceptions -- NOT Reverse Charge [T1]

| Situation | Treatment | Reason |
|-----------|-----------|--------|
| EU hotel / restaurant / taxi abroad | No Belgian VAT entry; foreign VAT irrecoverable | Local consumption; VAT paid at source in the other EU state |
| EU supplier charged their local VAT > 0% | Not reverse charge; VAT is cost | Supplier correctly applied local VAT; not a B2B RC scenario |
| Out-of-scope payments (wages, dividends, bank charges) | Never reverse charge | Not a supply of goods or services |
| Construction work for private individual (non-VAT registered) | Normal VAT charged by contractor | Co-contractor conditions not met |

---

## Step 9: Pro-Rata (Partial Deduction) [T2]

**Legislation:** Art 46 CTVA; AR nr. 3.

If the taxable person makes BOTH taxable supplies (giving right to deduction) AND exempt supplies under Art 44 (NOT giving right to deduction), input VAT must be apportioned.

### General Pro-Rata Method

```
Pro-rata % = (Turnover with right to deduction / Total turnover) x 100
```

Rounded UP to the next whole number. Art 46 ss2 CTVA.

**Excluded from both numerator and denominator:**
- Sales of capital goods (Art 46 ss2 CTVA)
- Financial and real estate income if ancillary to the main activity
- Subsidies not directly linked to price

### Real Use Method (Affectation Reelle / Werkelijk Gebruik) [T2]

Alternative to general pro-rata. The taxable person allocates each input directly to taxable or exempt activities. Mixed inputs use a specific key. Must be authorised by the VAT administration.

**ALWAYS flag pro-rata for reviewer.** The pro-rata rate must be confirmed by a licensed accountant before applying. Art 46 CTVA; AR nr. 3.

---

## Step 10: Edge Case Registry

These are known Belgium-specific ambiguous situations and their confirmed resolutions.

### EC1 -- Three Official Languages on Invoices and Forms [T1]

**Situation:** Belgium has three official languages (French, Dutch, German). Which language must be used on invoices and VAT returns?
**Resolution:** Invoices must be issued in the language of the region where the supplier is established: French in Wallonia, Dutch in Flanders, either FR or NL in Brussels (bilingual region), German in the German-speaking community. The VAT return form itself is bilingual (FR/NL). The Intervat portal supports FR, NL, and DE. Incorrect language does not invalidate the invoice but may trigger administrative queries.
**Legislation:** Loi du 30 juillet 1963 concernant le regime linguistique / Wet van 30 juli 1963 betreffende de taalregeling in bestuurszaken.

### EC2 -- Co-Contractor Construction: When Conditions Are NOT Met [T1]

**Situation:** Belgian contractor performs renovation on a private individual's home. Individual is not VAT-registered.
**Resolution:** Co-contractor scheme does NOT apply. Contractor charges VAT at the applicable rate (6% if dwelling > 10 years for renovation, 21% for new construction). Reports in Grid 01 or 03 accordingly. Grid 54 for output VAT.
**Legislation:** Art 20 AR nr. 1 -- requires both parties to file periodic returns.

### EC3 -- Belgian Annual Customer Listing (Klantenlisting / Listing Annuelle) [T1]

**Situation:** Client asks whether they need to file a customer listing.
**Resolution:** EVERY Belgian VAT-registered taxable person (including small enterprise scheme) must file an annual listing of Belgian VAT-registered customers to whom they supplied goods or services totalling more than EUR 250 (excl. VAT) during the calendar year. Filed electronically via Intervat by 31 March. Must include customer VAT number, total supplies, and total VAT charged.
**Legislation:** Art 53quinquies CTVA; AR nr. 23.

### EC4 -- Car Deduction Limitation: Default 50% vs Proven Professional Use [T1/T2]

**Situation:** Client purchases a company car. No logbook maintained.
**Resolution:** Default VAT deduction is 50% (Art 45 ss2 CTVA). If the client maintains a logbook proving professional use exceeds 50% (e.g., 75%), the deduction can be increased to the proven percentage (75%). If professional use is below 50%, the deduction is limited to the actual percentage. For a car costing EUR 30,000 + EUR 6,300 VAT (21%):
- No proof: Grid 59 = EUR 3,150 (50%); Grid 83 = EUR 30,000 + EUR 3,150 = EUR 33,150
- Proven 75%: Grid 59 = EUR 4,725 (75%); Grid 83 = EUR 30,000 + EUR 1,575 = EUR 31,575
**Legislation:** Art 45 ss2 CTVA; Circular 36/2015.

### EC5 -- Renovation at 6%: Conditions for Reduced Rate [T2]

**Situation:** Client invoices renovation work on a dwelling. Can 6% be applied?
**Resolution:** The 6% reduced rate for renovation applies ONLY when ALL conditions are met:
1. The dwelling is at least 10 years old (since first occupation).
2. The dwelling is used as a private residence (not purely commercial).
3. The work is invoiced directly to the end consumer (homeowner/tenant), NOT to a VAT-registered business acting as principal.
4. The work constitutes transformation, renovation, improvement, repair, or maintenance of the dwelling (not new construction or complete reconstruction).
5. The contractor states on the invoice that conditions for 6% are met.
If ANY condition fails, the standard 21% rate applies. [T2] -- reviewer to verify conditions.
**Legislation:** Table A, rubrique XXXVIII, AR nr. 20; Circular 2019/C/99.

### EC6 -- E-Commerce and One-Stop Shop (OSS) [T2]

**Situation:** Belgian online retailer sells goods to private consumers across the EU.
**Resolution:** Since 1 July 2021, the EUR 10,000 EU-wide distance sales threshold applies. If total B2C distance sales to all other EU Member States exceed EUR 10,000, VAT must be charged at the destination country's rate. The seller can register for the One-Stop Shop (OSS) via the Belgian Intervat portal to declare and pay VAT for all EU destination countries in a single quarterly return. If below EUR 10,000, Belgian VAT rates apply. OSS return is separate from the periodic Belgian VAT return.
**Legislation:** Art 15 CTVA (as amended by transposition of EU Directive 2017/2455); AR nr. 56.

### EC7 -- EU Hotel / Restaurant Abroad [T1]

**Situation:** Client pays hotel in Germany. Invoice shows German VAT (Mehrwertsteuer/MwSt).
**Resolution:** NOT reverse charge. Foreign VAT was charged and paid at source. No Belgian VAT entry. The expense (including German VAT) is booked as an overhead cost. The German VAT is irrecoverable in Belgium. Recovery is possible only via the EU VAT refund procedure (Directive 2008/9/EC) filed through the Belgian Intervat portal (separate from the periodic return).
**Legislation:** Art 21 ss3 3deg CTVA (place of supply for hotel/restaurant = where property located or where service physically performed).

### EC8 -- SaaS Subscription from US Provider [T1]

**Situation:** US company charges EUR 100/month for software. No VAT on invoice.
**Resolution:** Reverse charge applies. Place of supply for electronically supplied services to a B2B customer is where the customer is established (Belgium). Self-assess Belgian VAT at 21%.
- Grid 87 = EUR 100 (net amount, services category)
- Grid 56 = EUR 21 (output VAT at 21%)
- Grid 59 = EUR 21 (input VAT, fully deductible if taxable person)
- Net VAT effect = zero.
**Legislation:** Art 21 ss2 CTVA; Art 51 ss2 CTVA.

### EC9 -- Intra-Community Supply of Goods [T1]

**Situation:** Client sells goods to a German business. Goods shipped from Belgium to Germany.
**Resolution:** Exempt intra-Community supply. Grid 45 = net amount. No output VAT. Must verify: (1) customer has valid EU VAT number (VIES check), (2) goods are physically transported to Germany, (3) supplier retains proof of transport (CMR, bill of lading). Must file Intra-Community (IC) listing with the periodic return.
**Legislation:** Art 39bis CTVA; Art 53sexies CTVA.

### EC10 -- Credit Notes Issued [T1]

**Situation:** Client issues a credit note to a Belgian customer for goods returned, original sale was at 21%.
**Resolution:** Grid 48 = credit note amount (net). Grid 64 = VAT on credit note (reduces output VAT previously declared). The original Grid 03 and Grid 54 are NOT adjusted -- the credit note is reported separately.
**Legislation:** Art 77 CTVA.

### EC11 -- Triangular Trade (ABC) [T2]

**Situation:** Client (BE) purchases goods from Netherlands (NL) and sells to France (FR). Goods ship directly NL to FR.
**Resolution:** Simplified triangulation under Art 25quinquies CTVA. Client (B, the intermediary) reports in Grid 45 (IC supply to France). Client does NOT self-assess acquisition VAT (Grid 86/55) because goods never enter Belgium. French customer (C) self-assesses French VAT. Invoice must state "Application de l'article 141 de la directive 2006/112/CE -- exoneration TVA / Application of article 141 Directive 2006/112/EC -- VAT exemption". [T2] -- reviewer must confirm all three parties are VAT-registered in different EU Member States.
**Legislation:** Art 25quinquies CTVA; Art 141 Directive 2006/112/EC.

### EC12 -- VAT Unit (Unite TVA / BTW-Eenheid) [T3]

**Situation:** Client is part of a VAT unit (group registration).
**Resolution:** ESCALATE. Internal supplies between members of a VAT unit are outside the scope of VAT. The VAT unit files a single consolidated return. Members file individual "internal" returns (listing per member) that are consolidated into the unit return. Complex rules regarding joint and several liability, internal deduction rights, and reporting obligations.
**Legislation:** Art 4 ss2 CTVA; AR nr. 55.

### EC13 -- Mixed Use Property: Professional and Private [T2]

**Situation:** Self-employed person builds a house that is 30% professional office and 70% private.
**Resolution:** VAT on construction costs is deductible only for the professional-use portion (30%). The 30/70 split must be documented and agreed with the VAT administration. For a construction cost of EUR 200,000 + EUR 42,000 VAT (21%): Grid 59 = EUR 12,600 (30% of EUR 42,000). Grid 83 = EUR 200,000 + EUR 29,400 (non-deductible VAT). Subject to revision period of 15 years for immovable property (Art 48 ss2 CTVA; AR nr. 3, Art 9). [T2] -- reviewer to confirm allocation method.
**Legislation:** Art 45 ss1 CTVA; Art 48 ss2 CTVA; AR nr. 3.

### EC14 -- Import of Physical Goods Without ET14000 [T1]

**Situation:** Client imports goods from China. Pays import VAT at Belgian customs (no ET14000 licence).
**Resolution:** Import VAT is paid to customs and documented on the customs declaration (enkel document / document unique -- SAD). The VAT paid at customs IS recoverable as input VAT. Report in Grid 59 based on the customs document. Do NOT report in Grids 86-88 (those are for IC and reverse charge only). The goods purchase (customs value + duties) goes in Grid 81 or 83 depending on nature.
**Legislation:** Art 45 ss1 CTVA; Art 52 CTVA.

### EC15 -- Restaurant Meal vs Entertainment -- The Belgian Distinction [T1]

**Situation:** Client has a business lunch at a restaurant (EUR 100 + EUR 12 VAT at 12% food + EUR 4.20 VAT at 21% on beverages). Separately, client hosts a reception for 50 clients (EUR 5,000 + EUR 1,050 VAT at 21%).
**Resolution:**
- **Restaurant meal:** VAT IS deductible. Grid 82 = EUR 116.20 (net food + net beverages). Grid 59 = EUR 16.20 (EUR 12 + EUR 4.20). Restaurant meals are NOT in the exclusion list of Art 45 ss3 CTVA.
- **Reception:** VAT is NOT deductible. Grid 82 = EUR 5,000 + EUR 1,050 (non-deductible VAT added to base) = EUR 6,050. Grid 59 = EUR 0 for this expense. Art 45 ss3 3deg CTVA: "frais de reception" are blocked.
**Key distinction:** A business meal at a restaurant (even with clients) is deductible. A reception/event (cocktail party, client entertainment event, inauguration) is NOT deductible. The distinction hinges on whether the event is a "reception" (social gathering) vs a "restaurant meal" (seated meal). [T2] if borderline.
**Legislation:** Art 45 ss3 3deg CTVA; Circular nr. 4 of 17 January 2004.

---

## Step 11: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard domestic purchase, 21% VAT [T1]

**Input:** Belgian supplier, office supplies, gross EUR 242, VAT EUR 42, net EUR 200. Normal regime client.
**Expected output:** Grid 82 = EUR 200. Grid 59 = EUR 42 (deductible). No blocked categories.

### Test 2 -- US software subscription, reverse charge [T1]

**Input:** US provider (no EU establishment), EUR 100/month, no VAT on invoice. Normal regime client.
**Expected output:** Grid 87 = EUR 100. Grid 56 = EUR 21 (21% self-assessed). Grid 59 = EUR 21 (fully deductible). Net VAT = zero.

### Test 3 -- Intra-Community goods acquisition [T1]

**Input:** French supplier ships goods (raw materials) to Belgium, EUR 5,000, no VAT on invoice. Normal regime client.
**Expected output:** Grid 86 = EUR 5,000. Grid 55 = EUR 1,050 (21% self-assessed). Grid 59 = EUR 1,050. Grid 81 = EUR 5,000. Net VAT = zero.

### Test 4 -- IC B2B sale of goods [T1]

**Input:** Client sells goods to German business, EUR 3,000, ships BE to DE. Valid German VAT number verified on VIES.
**Expected output:** Grid 45 = EUR 3,000. No output VAT. IC listing entry for DE customer.

### Test 5 -- Small enterprise client -- purchase [T1]

**Input:** Small enterprise client (Art 56bis, turnover EUR 18,000) purchases office furniture EUR 500 + EUR 105 VAT.
**Expected output:** No VAT return filed. No VAT recovery. Total cost = EUR 605. Grid 59 = NOT applicable.

### Test 6 -- Company car, 50% default deduction [T1]

**Input:** Client purchases passenger car EUR 25,000 + EUR 5,250 VAT (21%). No logbook, no proof of professional use > 50%.
**Expected output:** Grid 83 = EUR 25,000 + EUR 2,625 (non-deductible VAT) = EUR 27,625. Grid 59 = EUR 2,625 (50% of EUR 5,250). Art 45 ss2 CTVA.

### Test 7 -- EU hotel, local consumption [T1]

**Input:** Client pays hotel in Italy, EUR 300 including Italian IVA. Business trip.
**Expected output:** No Belgian VAT entry. Italian VAT irrecoverable on Belgian return. Expense = EUR 300 gross in P&L. Possible recovery via EU VAT refund procedure (separate process).

### Test 8 -- Co-contractor construction [T1]

**Input:** Belgian contractor renovates client's commercial office. Both parties VAT-registered. Contractor invoices EUR 10,000 without VAT (mentions Art 20 AR nr. 1 on invoice).
**Expected output (customer's return):** Grid 87 = EUR 10,000. Grid 56 = EUR 2,100 (21% self-assessed). Grid 59 = EUR 2,100 (fully deductible, commercial property). Net = zero.
**Expected output (contractor's return):** Grid 44 = EUR 10,000. No output VAT.

### Test 9 -- Entertainment / reception costs (blocked) [T1]

**Input:** Client hosts a reception for business clients. Catering invoice: EUR 3,000 + EUR 630 VAT (21%).
**Expected output:** Grid 82 = EUR 3,000 + EUR 630 (non-deductible VAT) = EUR 3,630. Grid 59 = EUR 0. VAT BLOCKED. Art 45 ss3 3deg CTVA.

### Test 10 -- Business restaurant meal (NOT blocked) [T1]

**Input:** Client has a business lunch. Restaurant bill: food EUR 80 + EUR 9.60 VAT (12%), beverages EUR 20 + EUR 4.20 VAT (21%). Total VAT = EUR 13.80.
**Expected output:** Grid 82 = EUR 100 (net food + net beverages). Grid 59 = EUR 13.80. VAT IS deductible. Restaurant meals are not blocked.

### Test 11 -- Renovation at 6% rate [T1]

**Input:** Client (contractor) invoices renovation of a private dwelling built in 2005 (> 10 years old) to the homeowner (private individual). Work = EUR 15,000 + EUR 900 VAT (6%).
**Expected output (contractor's return):** Grid 01 = EUR 15,000. Grid 54 = EUR 900. Customer is private individual so co-contractor does NOT apply.

### Test 12 -- Export to non-EU country [T1]

**Input:** Client exports manufactured goods to United States. Invoice EUR 20,000, no VAT.
**Expected output:** Grid 46 = EUR 20,000. No output VAT. Must retain proof of export (customs export declaration, bill of lading).

### Test 13 -- Credit note received from Belgian supplier [T1]

**Input:** Belgian supplier issues credit note for EUR 500 + EUR 105 VAT (21%) on previously purchased services.
**Expected output:** Grid 84 = EUR 500 (negative adjustment to Grid 82). Grid 57 = EUR 105 (VAT previously deducted must be repaid). Grid 59 reduced by EUR 105 for the period.

### Test 14 -- IC services received from EU (Art 21 ss2) [T1]

**Input:** German consultant provides advisory services to Belgian client. Invoice EUR 2,000, no VAT (reverse charge).
**Expected output:** Grid 88 = EUR 2,000. Grid 55 = EUR 420 (21% self-assessed). Grid 59 = EUR 420 (deductible). Net = zero.

---

## Step 12: Comparison with Malta

| Feature | Belgium (BE) | Malta (MT) |
|---------|-------------|------------|
| **Primary Legislation** | Code de la TVA / BTW-Wetboek (CTVA) | VAT Act Chapter 406, Laws of Malta |
| **Tax Authority** | SPF Finances / FOD Financien | Commissioner for Revenue (CFR) |
| **Filing Portal** | Intervat (MyMINFIN) | CFR VAT Online (cfr.gov.mt) |
| **Standard Rate** | 21% (Art 37 CTVA) | 18% (5th Schedule Cap. 406) |
| **Reduced Rates** | 12%, 6% (AR nr. 20, Tables A & B) | 12%, 7%, 5% (5th Schedule Cap. 406) |
| **Zero Rate** | Exports, IC supplies, certain newspapers (Art 39-42 CTVA) | Exports, certain food, pharmaceuticals (3rd Schedule Cap. 406) |
| **VAT Return Form** | Declaration periodique / Periodieke aangifte -- Grids 00-91 | VAT3 form -- Boxes 1-45 |
| **Return Structure** | 7 cadres/roosters with ~30 grids | Single form with ~45 boxes |
| **Filing Frequency** | Monthly (> EUR 2.5M) or Quarterly (default) | Quarterly (Article 10), Annual (Article 11), Monthly (Article 12) |
| **Filing Deadline** | 20th of month following period | 21st (e-file) or 14th (paper) of month after quarter |
| **Small Enterprise Threshold** | EUR 25,000 (Art 56bis CTVA) | EUR 35,000 (Article 11, Cap. 406) |
| **Small Enterprise Filing** | No periodic returns; annual customer listing | Annual 4-box declaration |
| **Capital Goods Threshold** | No specific monetary threshold (accounting-based) | EUR 1,160 gross (Article 24, Cap. 406) |
| **Capital Goods Revision Period** | 5 years movable, 15 years immovable (Art 48 CTVA; AR nr. 3) | 5 years (Article 24, Cap. 406) |
| **Blocked: Entertainment** | Yes -- Art 45 ss3 3deg CTVA | Yes -- 10th Schedule Item 3(1)(b) |
| **Blocked: Motor Vehicles** | Partial (max 50% default, up to 100% if proven) -- Art 45 ss2 CTVA | Full block -- 10th Schedule Item 3(1)(a)(iv-v), except taxi/delivery |
| **Blocked: Tobacco** | Yes -- Art 45 ss3 2deg CTVA | Yes -- 10th Schedule Item 3(1)(a)(i) |
| **Blocked: Alcohol** | No (fully deductible if business expense) | Yes -- 10th Schedule Item 3(1)(a)(ii) |
| **Blocked: Restaurant Meals** | No (fully deductible for VAT) | No (deductible if not entertainment) |
| **Blocked: Staff Housing** | Yes -- Art 45 ss3 4deg CTVA | Not specifically listed |
| **Reverse Charge -- Construction** | Yes, co-contractor system (Art 20 AR nr. 1) | No specific domestic RC for construction |
| **Reverse Charge -- Grid/Box** | Supplier: Grid 44; Customer: Grids 87/56/59 | EU: Box 9/13; Non-EU: Box 11/15 |
| **IC Listing** | Filed with each periodic return | Filed with each periodic return (quarterly) |
| **Annual Customer Listing** | Mandatory (klantenlisting, by 31 March) | No equivalent annual listing |
| **Languages** | Three official: FR, NL, DE | Two official: Maltese, English |
| **Enterprise Number Format** | BE 0XXX.XXX.XXX (10 digits) | MT + 8 digits |
| **December Advance** | Mandatory for monthly filers (24 Dec) | Not applicable |
| **EU VAT Refund** | Via Intervat (Directive 2008/9/EC) | Via CFR portal |
| **Penalty -- Late Filing** | EUR 100-5,000/month (AR nr. 41) | Administrative penalties per CFR guidelines |
| **Late Payment Interest** | 0.8%/month (9.6%/year) -- Art 91 CTVA | Interest at prescribed rate |
| **OSS (One-Stop Shop)** | Available via Intervat for B2C e-commerce | Available via CFR for B2C e-commerce |

**Key Differences for Cross-Border Practitioners:**

1. **Rate spread:** Belgium's standard rate (21%) is 3 percentage points higher than Malta's (18%). This affects reverse charge calculations significantly.
2. **Vehicle treatment:** Belgium allows partial deduction (up to proven professional use %); Malta blocks entirely (except specific vehicle types like taxi/delivery).
3. **Alcohol:** Belgium allows full VAT deduction on business alcohol purchases; Malta blocks all alcohol under the 10th Schedule.
4. **Co-contractor:** Belgium has a specific domestic reverse charge for construction (medecontractant); Malta does not have an equivalent.
5. **Customer listing:** Belgium requires an annual listing of all Belgian VAT-registered customers (> EUR 250); Malta has no such requirement.
6. **Filing deadline:** Belgium uses the 20th; Malta uses the 21st (e-file) or 14th (paper).
7. **Small enterprise:** Belgium EUR 25,000 vs Malta EUR 35,000 threshold.

---

## PROHIBITIONS [T1]

- NEVER let AI guess grid numbers -- they are 100% deterministic from the transaction facts using the lookup tables above
- NEVER apply small enterprise scheme (Art 56bis CTVA) if turnover > EUR 25,000
- NEVER allow small enterprise clients to recover input VAT or file periodic returns
- NEVER apply reverse charge to out-of-scope categories (salaries, dividends, bank charges, insurance premiums)
- NEVER apply reverse charge to local consumption abroad (EU hotel, restaurant, taxi, conference)
- NEVER allow > 50% vehicle VAT deduction without documented proof of professional use > 50% (Art 45 ss2 CTVA)
- NEVER deduct VAT on entertainment/reception costs (Art 45 ss3 3deg CTVA) -- frais de reception / receptiekosten are always blocked
- NEVER deduct VAT on accommodation for personnel/directors for private use (Art 45 ss3 4deg CTVA)
- NEVER deduct VAT on tobacco (Art 45 ss3 2deg CTVA)
- NEVER confuse co-contractor scheme (domestic construction, Art 20 AR nr. 1) with intra-Community reverse charge (Art 25ter/21 ss2 CTVA) -- they use different grids (87/56 vs 86/55 or 88/55)
- NEVER apply co-contractor reverse charge when the customer is not VAT-registered or does not file periodic returns
- NEVER apply 6% renovation rate without verifying ALL conditions (dwelling > 10 years, private use, invoiced to end consumer)
- NEVER confuse exempt with credit (exports, IC supplies -- Grids 45/46) with exempt without credit (Art 44 -- Grid 47)
- NEVER report import VAT paid at customs in Grids 86-88 -- those are only for IC and reverse charge; import VAT from customs goes directly to Grid 59
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER file a Belgian VAT return on paper -- Intervat electronic filing is mandatory for all periodic filers

---

## Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed accountant (expert-comptable / accountant) must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed accountant (expert-comptable / accountant). Document gap.
```

---

## Step 14: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Do not execute any of these rules. Escalate to licensed accountant.

- **IPP/PB (Impot des personnes physiques / Personenbelasting):** Progressive rates 25%, 30%, 40%, 45%, 50%. Art 130-145 CIR/WIB.
- **ISOC/VenB (Impot des societes / Vennootschapsbelasting):** 25% standard rate; 20% on first EUR 100,000 for qualifying SMEs (Art 215 ss2 CIR/WIB).
- **ONSS/RSZ (social security):** Employer contributions ~25% of gross salary; employee contributions 13.07%. Separate obligation.
- **Precompte professionnel / Bedrijfsvoorheffing:** Withholding tax on salaries. Separate from VAT.
- **Precompte mobilier / Roerende voorheffing:** Withholding on dividends (30%), interest (30%). Art 261-269 CIR/WIB.
- **Restaurant meals for CIT:** Only 69% deductible for income tax purposes (Art 53 8deg CIR/WIB). This is DIFFERENT from VAT where restaurant meals are 100% deductible.

---

## Contribution Notes

Adapted from the Malta VAT Return Skill template. All legislation, grid numbers, thresholds, blocked categories, and edge cases are specific to Belgium. VAT rates verified against PWC Tax Summaries (https://taxsummaries.pwc.com/belgium/corporate/other-taxes): 21% standard, 12% reduced, 6% reduced confirmed.

**A skill may not be published without sign-off from a licensed accountant (expert-comptable / accountant) or tax advisor (conseil fiscal / belastingconsulent) in Belgium.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
