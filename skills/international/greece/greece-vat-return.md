---
name: greece-vat-return
description: Use this skill whenever asked to prepare, review, or create a Greece VAT return (Periodiki Dilosi FPA / Periodikhh Dhlwsh FPA) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in the FPA return", "Greek VAT", "FPA", "myAADE", "TAXISnet", or any request involving Greece VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Greece VAT classification rules, form field mappings, deductibility rules, reverse charge treatment, myDATA e-invoicing obligations, Aegean island reduced rates, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Greek VAT-related work.
---

# Greece VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Greece (Elliniki Dimokratia) |
| Jurisdiction Code | GR (EL for VIES purposes) |
| Primary Legislation | N.2859/2000 -- Kodikas Forou Prostithemenis Axias (Kodikos FPA / VAT Code), as amended |
| Amending Legislation | N.4172/2013; N.4714/2020; N.4916/2022; N.5073/2023 |
| Procedural Legislation | N.4174/2013 -- Kodikas Forologikis Diadikasias (Tax Procedure Code, KFD) |
| myDATA Legislation | POL 1138/2020; A.1138/2020 (myDATA platform); A.1052/2023 (mandatory B2B e-invoicing) |
| Tax Authority | Aneksartiti Archi Dimosion Esodon (AADE -- Independent Authority for Public Revenue) |
| Filing Portal | https://www.aade.gr -- myTAXISnet / myAADE portal |
| Form Name | Periodiki Dilosi FPA (Periodic VAT Declaration) -- commonly called "F2" |
| Annual Summary | Ekkatharistiki Dilosi FPA (Annual VAT Summary Declaration) |
| Contributor | Auto-generated -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Status | awaiting-validation |
| Confidence Coverage | Tier 1: form field assignment, reverse charge, deductibility blocks, myDATA classification, rate determination. Tier 2: partial exemption pro-rata, island reduced rates, mixed-use apportionment, tourism sector specifics. Tier 3: complex group structures, shipping/maritime VAT, special schemes (farmers Art. 41, travel agents Art. 43). |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. The engine computes; the AI classifies.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A logistis-forotechnikos (certified accountant-tax consultant) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and AFM (Arithmos Forologikou Mitroou -- tax identification number)** [T1] -- 9 digits; EL prefix for EU VIES purposes. N.2859/2000, Art. 36.
2. **DOY (Diefthynsi Oikonomikon Ypiresioon -- tax office)** [T1] -- the local tax office the entity is registered with.
3. **VAT registration status** [T1] -- Normal regime, small business exemption (Art. 39), or special scheme (farmers Art. 41, travel agents Art. 43, used goods Art. 45). N.2859/2000, Art. 36.
4. **Filing frequency** [T1] -- Monthly (double-entry bookkeeping / diplografika vivlia) or Quarterly (single-entry bookkeeping / aplografika vivlia). N.2859/2000, Art. 38; N.4174/2013, Art. 6.
5. **Industry/sector** [T2] -- impacts applicable reduced rates, island eligibility, and deductibility. Flag for reviewer.
6. **Does the business make exempt-without-credit supplies?** [T2] -- If yes, partial attribution required (analogia ekptwsis / pro-rata). N.2859/2000, Art. 31. Reviewer must confirm.
7. **Is the business located on or supplying to eligible Aegean islands?** [T2] -- reduced rates apply per N.2859/2000, Art. 21(4). Reviewer must confirm island eligibility.
8. **myDATA classification codes** [T1] -- income/expense type codes required for all documents. POL 1138/2020.
9. **Excess credit brought forward (pistotiko ypoloipo)** [T1] -- from prior period. N.2859/2000, Art. 38.
10. **Does the business engage in shipping, maritime transport, or ship supply?** [T3] -- special exemption regime. Escalate.

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until these are confirmed.**

---

## Section 1: VAT Return Form Structure -- Periodiki Dilosi FPA

**Legislation:** N.2859/2000, Art. 38; AADE Form F2.
**Filing method:** Exclusively electronic via TAXISnet / myAADE portal (https://www.aade.gr). [T1]

The Periodiki Dilosi FPA (Periodic VAT Declaration) is the form used for monthly or quarterly VAT reporting. It is divided into three main sections plus supporting schedules.

### 1.1 Form Header Fields [T1]

| Field (Greek) | Field (English) | Description |
|---------------|-----------------|-------------|
| AFM | Tax ID Number | 9-digit taxpayer identification number. N.2859/2000, Art. 36. |
| DOY | Tax Office | The competent local tax office. |
| Eponymia / Eponimo | Entity Name / Surname | Legal name of the entity or individual. |
| Forologiki Periodos | Tax Period | Month or quarter being reported. |
| Eidos Dilosis | Declaration Type | Normal (kanonikh), Corrective (tropopoiitikh), or Nil (midenikhh). |
| Imerominia Ypovolis | Submission Date | Date of electronic submission via TAXISnet. |
| Diplografika / Aplografika | Double-Entry / Single-Entry | Bookkeeping method -- determines filing frequency. N.4174/2013, Art. 6. |

### 1.2 Section A -- Output VAT (FPA Ekroon) [T1]

**Legislation:** N.2859/2000, Art. 19-20 (chargeable event and chargeability), Art. 21 (rates).

| Code | Description (Greek) | Description (English) | Rate |
|------|--------------------|-----------------------|------|
| 301 | Forologitea axia ekroon 24% | Taxable base of supplies at 24% | 24% |
| 302 | FPA ekroon 24% | Output VAT at 24% | -- |
| 303 | Forologitea axia ekroon 13% | Taxable base of supplies at 13% | 13% |
| 304 | FPA ekroon 13% | Output VAT at 13% | -- |
| 305 | Forologitea axia ekroon 6% | Taxable base of supplies at 6% | 6% |
| 306 | FPA ekroon 6% | Output VAT at 6% | -- |
| 307 | Forologitea axia ekroon 17% (nisia) | Taxable base at 17% (island rate) | 17% |
| 308 | FPA ekroon 17% | Output VAT at 17% (island) | -- |
| 309 | Forologitea axia ekroon 9% (nisia) | Taxable base at 9% (island rate) | 9% |
| 310 | FPA ekroon 9% | Output VAT at 9% (island) | -- |
| 311 | Endokoinotikes paradoseis agathon | Intra-EU supplies of goods | 0% |
| 312 | Exagoges agathon | Exports of goods | 0% |
| 313 | Parochi ypiresion entos EE (B2B) | EU B2B service supplies (Art. 14(2)(a)) | 0% |
| 321 | Apallassomenes aney dikaiomatos ekptwsis | Exempt supplies without right of deduction | Exempt |
| 322 | Apallassomenes me dikaiwma ekptwsis | Exempt supplies with right of deduction | 0% |
| 331 | Endokoinotikes apoktiseis agathon -- axia | Intra-EU acquisition of goods -- base | RC |
| 332 | FPA endokoinotikon apoktiseon | Output VAT on intra-EU acquisition | -- |
| 333 | Lipsi ypiresion apo EE (Art. 14(2)(a)) -- axia | EU services received -- base | RC |
| 334 | FPA lipsis ypiresion apo EE | Output VAT on EU services received | -- |
| 335 | Eisagogi ypiresion apo trites chores -- axia | Import of services from non-EU -- base | RC |
| 336 | FPA eisagogis ypiresion apo trites chores | Output VAT on non-EU services | -- |
| 341 | Esoteriki antistrofi epivarynsi -- axia | Domestic reverse charge -- base | RC |
| 342 | FPA esoterikis antistrofis epivarynsis | Output VAT on domestic reverse charge | -- |

### 1.3 Section B -- Input VAT (FPA Eisroon) [T1]

**Legislation:** N.2859/2000, Art. 30 (right of deduction), Art. 30(4) (blocked categories).

| Code | Description (Greek) | Description (English) |
|------|--------------------|-----------------------|
| 361 | FPA eisroon esoterikon agoron 24% | Input VAT on domestic purchases at 24% |
| 362 | FPA eisroon esoterikon agoron 13% | Input VAT on domestic purchases at 13% |
| 363 | FPA eisroon esoterikon agoron 6% | Input VAT on domestic purchases at 6% |
| 364 | FPA eisroon esoterikon agoron 17% (nisia) | Input VAT on domestic purchases at 17% (island) |
| 365 | FPA eisroon esoterikon agoron 9% (nisia) | Input VAT on domestic purchases at 9% (island) |
| 366 | FPA eisroon esoterikon agoron 4% (nisia) | Input VAT on domestic purchases at 4% (island) |
| 371 | FPA endokoinotikon apoktiseon agathon | Input VAT on intra-EU acquisitions of goods |
| 372 | FPA lipsis ypiresion apo EE | Input VAT on EU services received |
| 373 | FPA eisagogis ypiresion apo trites chores | Input VAT on non-EU services received |
| 374 | FPA esoterikis antistrofis epivarynsis | Input VAT on domestic reverse charge |
| 381 | FPA eisagogon (teloneio) | Input VAT on imports (customs) |
| 382 | FPA pagion | Input VAT on fixed assets / capital goods |
| 383 | Diakanorismos analogias ekptwsis | Proportional deduction adjustment (pro-rata) |

### 1.4 Section C -- Settlement (Ekkathariasi) [T1]

**Legislation:** N.2859/2000, Art. 38.

| Code | Description (Greek) | Description (English) |
|------|--------------------|-----------------------|
| 401 | Synolo FPA ekroon | Total output VAT |
| 402 | Synolo FPA eisroon | Total input VAT |
| 411 | Chreostiko ypoloipo (poso pliromi) | Net VAT payable (if output > input) |
| 412 | Pistotiko ypoloipo | Net VAT credit (if input > output) |
| 501 | Pistotiko ypoloipo prohgoumenis periodou | Credit brought forward from prior period |
| 502 | Pistotiko ypoloipo pros synepsifismo | Credit requested for offset to next period |
| 503 | Pistotiko ypoloipo pros epistrofi | Credit requested for refund |
| 511 | Teliko poso pliromi | Final amount payable |
| 512 | Katavoli se doseis | Payment in instalments (up to 2 monthly instalments) |

### 1.5 Supporting Schedules [T1]

| Schedule | Description | Legislation |
|----------|-------------|-------------|
| Anakefalaiotikos Pinakas (VIES) | Recapitulative statement for intra-EU transactions | N.2859/2000, Art. 36(5); Reg. (EU) 904/2010 |
| Intrastat | Statistical declaration for physical EU goods movements | Reg. (EC) 638/2004 |
| myDATA Synopsi | Summary of documents transmitted to myDATA platform | POL 1138/2020 |

---

## Section 2: Transaction Classification Matrix

### 2.1 Master Classification Lookup Table [T1]

**Legislation:** N.2859/2000, Art. 2-4 (taxable transactions), Art. 11-14 (place of supply), Art. 35 (reverse charge).

| Transaction Type | Counterparty | Type | Output Code | Input Code | Rate | VIES | myDATA Type | Tier |
|-----------------|-------------|------|-------------|------------|------|------|-------------|------|
| Domestic sale of goods | GR | Sale | 301/302 | -- | 24% | No | 1.1 | [T1] |
| Domestic sale of food/catering | GR | Sale | 303/304 | -- | 13% | No | 1.1 | [T1] |
| Domestic sale of medicines | GR | Sale | 305/306 | -- | 6% | No | 1.1 | [T1] |
| Domestic sale -- island 17% | GR (island) | Sale | 307/308 | -- | 17% | No | 1.1 | [T2] |
| Domestic sale -- island 9% | GR (island) | Sale | 309/310 | -- | 9% | No | 1.1 | [T2] |
| Intra-EU supply of goods | EU | Sale | 311 | -- | 0% | Yes | 2.1 | [T1] |
| Export of goods | Non-EU | Sale | 312 | -- | 0% | No | 2.2 | [T1] |
| EU B2B service supply | EU | Sale | 313 | -- | 0% | Yes | 2.1 | [T1] |
| Exempt supply (no credit) | Any | Sale | 321 | -- | Exempt | No | 1.3 | [T1] |
| Exempt supply (with credit) | Any | Sale | 322 | -- | 0% | No | 1.4 | [T1] |
| Domestic purchase -- overhead 24% | GR | Purchase | -- | 361 | 24% | No | 14.1 | [T1] |
| Domestic purchase -- overhead 13% | GR | Purchase | -- | 362 | 13% | No | 14.1 | [T1] |
| Domestic purchase -- overhead 6% | GR | Purchase | -- | 363 | 6% | No | 14.1 | [T1] |
| Domestic purchase -- island 17% | GR (island) | Purchase | -- | 364 | 17% | No | 14.1 | [T2] |
| Domestic purchase -- island 9% | GR (island) | Purchase | -- | 365 | 9% | No | 14.1 | [T2] |
| Domestic purchase -- island 4% | GR (island) | Purchase | -- | 366 | 4% | No | 14.1 | [T2] |
| Domestic purchase -- capital goods | GR | Purchase | -- | 382 | Applicable | No | 14.1 | [T1] |
| Intra-EU acquisition of goods | EU | Purchase | 331/332 | 371 | RC 24% | Yes | 14.2 | [T1] |
| EU services received (B2B) | EU | Purchase | 333/334 | 372 | RC 24% | No | 14.4 | [T1] |
| Non-EU services received | Non-EU | Purchase | 335/336 | 373 | RC 24% | No | 14.5 | [T1] |
| Domestic reverse charge received | GR | Purchase | 341/342 | 374 | RC 24% | No | 14.1 | [T1] |
| Import of goods (customs) | Non-EU | Purchase | -- | 381 | Customs | No | 14.3 | [T2] |

### 2.2 Out-of-Scope Items -- NEVER on VAT Return [T1]

**Legislation:** N.2859/2000, Art. 2 (scope of VAT).

| Item | Reason |
|------|--------|
| Salaries and wages (misthoi) | Employment relationship, not supply of goods/services |
| Social contributions (EFKA eisphores) | Statutory obligation, not supply |
| Income tax (foros eisodimatos) | Tax, not supply |
| Loan principal repayments | Financial transaction, not supply |
| Dividends (merismata) | Return on capital, not supply |
| Share capital contributions | Capital, not supply |
| Bank charges (trapezikes promitheies) | Exempt financial service -- no input VAT recovery |
| Fines and penalties (prostima) | Penalty, not supply |
| Internal transfers between own accounts | Not a transaction |

### 2.3 Counterparty Location Lookup [T1]

| Location | Countries | Classification |
|----------|-----------|---------------|
| Domestic | GR / EL | Greece |
| EU Member States | AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE | EU |
| Non-EU | US, UK, CH, NO, AU, CN, JP, and all others | Third countries |

**Note:** UK is Non-EU post-Brexit (1 January 2021). Northern Ireland follows EU goods rules under the Windsor Framework but is Non-EU for services. [T2]

---

## Section 3: VAT Rates

### 3.1 Mainland Rates (Ipirotiki Ellada) [T1]

**Legislation:** N.2859/2000, Art. 21(1); Annex III (Parartima III) to N.2859/2000.
**Verified against:** PwC Tax Summaries -- Greece Corporate -- Other Taxes (2025/2026).

| Rate | Percentage | Applies To | Legislative Basis |
|------|-----------|------------|-------------------|
| Standard | **24%** | All goods and services not listed in reduced-rate annexes | N.2859/2000, Art. 21(1)(a) |
| Reduced | **13%** | See Table 3.2 below | N.2859/2000, Art. 21(1)(b); Annex III, Part A |
| Super-reduced | **6%** | See Table 3.3 below | N.2859/2000, Art. 21(1)(c); Annex III, Part B |
| Zero-rated | **0%** | Exports (Art. 24); intra-EU supplies (Art. 28); international transport | N.2859/2000, Art. 24, Art. 28 |
| Exempt with credit | **0%** (deduction allowed) | International passenger/goods transport; ship supply | N.2859/2000, Art. 27 |
| Exempt without credit | **N/A** | Financial services, insurance, healthcare, education, postal, residential letting, gambling | N.2859/2000, Art. 22 |

### 3.2 Reduced Rate (13%) -- Detailed Categories [T1]

**Legislation:** N.2859/2000, Art. 21(1)(b); Annex III, Part A.

| Category | Examples | Notes |
|----------|---------|-------|
| Food and non-alcoholic beverages | Fresh food, oil, coffee, sugars, confectionery | Excludes alcoholic beverages (24%) |
| Catering and restaurant services | Restaurant meals, takeaway food | Alcoholic beverages served separately at 24% |
| Hotel accommodation | Hotels, pensions, furnished apartments | Short-term letting < 1 year |
| Water supply | Municipal water distribution | N.2859/2000, Annex III, Part A |
| Energy -- natural gas, district heating | Gas and heating supply | Distinct from electricity (see 6% below) |
| Passenger transport | Taxis, buses, ferries, trains | Domestic routes |
| Agricultural inputs | Seeds, fertilizers, animal feed, pesticides | For agricultural use |
| Medical devices | Hearing aids, orthopaedic devices, wheelchairs | CN codes per Annex III |
| Infant and child products | Diapers, car seats, baby nutrition | N.4916/2022 amendment |
| Fitness centres and dance schools | Gym memberships, dance lessons | Added by N.4714/2020 |
| Zoo and botanical garden admission | Entry tickets | N.2859/2000, Annex III |
| Imported artwork | Sculptures, paintings by living artists | CN codes 9701-9703 |

### 3.3 Super-Reduced Rate (6%) -- Detailed Categories [T1]

**Legislation:** N.2859/2000, Art. 21(1)(c); Annex III, Part B.

| Category | Examples | CN Codes / Notes |
|----------|---------|-----------------|
| Medicines | Pharmaceutical products for human use | CN 3003, 3004. N.2859/2000, Annex III, Part B |
| Vaccines | Human vaccines | CN 3002. N.2859/2000, Annex III, Part B |
| Books | Physical books, e-books, audiobooks | N.2859/2000, Annex III, Part B; N.4714/2020 |
| Newspapers | Daily and periodic press | Physical and electronic. N.2859/2000, Annex III, Part B |
| Magazines and periodicals | Weekly, monthly publications | N.2859/2000, Annex III, Part B |
| Theatre and concert tickets | Performing arts admission | N.2859/2000, Annex III, Part B |
| Cinema tickets | Film screenings | N.2859/2000, Annex III, Part B |
| Electricity | Electricity supply | N.5073/2023 (moved from 13% to 6%) |
| Prepared animal food | Pet food, livestock feed preparations | CN 2309. N.2859/2000, Annex III, Part B |

### 3.4 Aegean Island Reduced Rates [T2]

**Legislation:** N.2859/2000, Art. 21(4); POL 1150/2001 (island list); Presidential Decree.

Specific islands in the Aegean Sea benefit from a **30% discount** on all three VAT rates. This discount is applied by reducing each rate by 30% and rounding to the nearest whole number.

| Rate Type | Mainland Rate | Island Rate (30% reduction) | Calculation |
|-----------|-------------|---------------------------|-------------|
| Standard | 24% | **17%** | 24% x 0.70 = 16.8% -> 17% |
| Reduced | 13% | **9%** | 13% x 0.70 = 9.1% -> 9% |
| Super-reduced | 6% | **4%** | 6% x 0.70 = 4.2% -> 4% |

### 3.5 Eligible Aegean Islands [T2]

**Legislation:** N.2859/2000, Art. 21(4); POL 1150/2001 as amended.

| Island Group | Specific Islands (indicative) | Notes |
|-------------|------------------------------|-------|
| Dodecanese | Kos, Rhodes, Kalymnos, Karpathos, Leros, Patmos, Symi, Tilos, Nisyros, Astypalaia, Kasos, Lipsi, Halki, Megisti | Except Rhodes and Kos which may have different treatment for certain supplies -- confirm per current legislation |
| North Aegean | Lesvos, Chios, Samos, Ikaria, Limnos, Agios Efstratios | N.2859/2000, Art. 21(4) |
| Cyclades | Mykonos, Santorini, Paros, Naxos, Andros, Tinos, Syros, Milos, Ios, Amorgos, Serifos, Sifnos, Kea, Kythnos, Folegandros, Sikinos, Anafi, Kimolos, Antiparos | Subject to periodic review |
| Saronic Gulf | Certain smaller islands | Confirm eligibility per current POL circular |
| Sporades | Skiathos, Skopelos, Alonissos, Skyros | Confirm per current legislation |
| Eastern Aegean | Samothraki, Thasos | Confirm per current legislation |

**CRITICAL RULES for island rates** [T2]:

| Rule | Detail | Legislation |
|------|--------|-------------|
| Goods delivered AND consumed on island | Rate applies | N.2859/2000, Art. 21(4) |
| Services rendered on island | Rate applies | N.2859/2000, Art. 21(4) |
| New buildings (construction) | Island rate does NOT apply -- mainland rate | POL 1150/2001 |
| Motor vehicles, boats, aircraft | Island rate does NOT apply -- mainland rate | N.2859/2000, Art. 21(4)(b) |
| Services deliverable remotely (consulting, IT) | Island rate does NOT apply -- mainland rate | POL 1150/2001 |
| Goods shipped FROM island to mainland | Mainland rate at destination | N.2859/2000, Art. 21(4) |

**Flag for reviewer: ALWAYS confirm (a) the specific island is on the eligible list per current legislation, (b) the supply qualifies for the reduction, and (c) no recent legislative change has modified eligibility.** [T2]

---

## Section 4: Blocked Input Tax (Ми Ekpiptomenos FPA)

### 4.1 Categories with Zero VAT Recovery [T1]

**Legislation:** N.2859/2000, Art. 30(4).

Blocked categories have ZERO VAT recovery regardless of business use, partial exemption status, or any other factor. Check blocked categories FIRST, before any other deductibility analysis.

| Category | VAT Recovery | Legislative Basis | Exceptions |
|----------|-------------|-------------------|------------|
| Passenger cars (purchase, lease, hire) | **0%** | N.2859/2000, Art. 30(4)(a) | Taxis (Art. 30(4)(a) proviso); car rental businesses; driving schools; vehicles for resale by dealers |
| Fuel for passenger cars | **0%** | N.2859/2000, Art. 30(4)(a) | Same exceptions as vehicle itself |
| Maintenance, repair, insurance of passenger cars | **0%** | N.2859/2000, Art. 30(4)(a) | Same exceptions as vehicle itself |
| Motorcycles over 50cc (purchase, lease) | **0%** | N.2859/2000, Art. 30(4)(a) | Courier/delivery businesses; motorcycle dealers |
| Fuel for blocked motorcycles | **0%** | N.2859/2000, Art. 30(4)(a) | Same as motorcycle |
| Entertainment and hospitality (philoxenia, diaskhedasi) | **0%** | N.2859/2000, Art. 30(4)(b) | Hospitality sector businesses (hotels, restaurants) for their own trade supplies |
| Tobacco products | **0%** | N.2859/2000, Art. 30(4)(c) | Tobacco dealers/retailers for resale stock only |
| Yachts and pleasure boats (skaph anapsikhis) | **0%** | N.2859/2000, Art. 30(4)(d) | Commercial charter companies; boat dealers for resale |
| Residential property (purchase, renovation) | **0%** | N.2859/2000, Art. 22(1)(kb); Art. 30(4) | Unless opting to tax (Art. 22 waiver for new buildings within 5 years) |
| Swimming pools, sports facilities (personal) | **0%** | N.2859/2000, Art. 30(4)(b) | Commercial sports facilities open to public |
| Personal use items | **0%** | N.2859/2000, Art. 30(4)(e) | None -- personal use is always blocked |

### 4.2 Fully Deductible Categories (Subject to Business Use) [T1]

**Legislation:** N.2859/2000, Art. 30(1)-(3).

| Category | Deductibility | Notes |
|----------|-------------|-------|
| Office supplies and stationery | 100% | Must be for business use |
| Professional services (logistikes, nomikes ypiresies) | 100% | Accounting, legal, consulting |
| Telecommunications (tilephonia, internet) | 100% | If exclusively business; mixed use requires apportionment [T2] |
| Utilities (ilektrismos, nero, fysiko aerio) | 100% | Business premises only |
| Commercial vehicles -- vans (fortion < 3.5t) | 100% | N.2859/2000, Art. 30(4)(a) -- not blocked |
| Commercial vehicles -- trucks (fortion > 3.5t) | 100% | N.2859/2000, Art. 30(4)(a) -- not blocked |
| Fuel for commercial vehicles | 100% | Follows vehicle deductibility |
| Business travel -- transport (air, train, ferry) | 100% | Not entertainment |
| Business travel -- accommodation | 100% | Not entertainment; must be for business traveller |
| Professional training and conferences | 100% | Directly related to business activity |
| Rent of business premises | 100% | Commercial lease; residential blocked |
| IT equipment and software | 100% | Business use; capital goods rules if > EUR 1,500 net |
| Raw materials and stock for production | 100% | Directly attributable to taxable supplies |
| Advertising and marketing services | 100% | N.2859/2000, Art. 30(1) |

### 4.3 Registration-Based Recovery [T1]

**Legislation:** N.2859/2000, Art. 30; Art. 39 (small business); Art. 41 (farmers).

| Registration Type | Input VAT Recovery | Notes |
|------------------|-------------------|-------|
| Normal VAT payer (kanoniko kathestos) | Full recovery (subject to blocked categories and pro-rata) | N.2859/2000, Art. 30(1) |
| Small business exempt (Art. 39) | **NO recovery** | Exempt from charging and recovering VAT |
| Farmers -- flat-rate scheme (Art. 41) | **NO recovery** | Flat-rate compensation instead (currently 6% for agricultural products) |
| Farmers -- normal regime (opted in) | Full recovery | Must maintain full books |
| Travel agents (Art. 43) | Margin scheme | VAT on margin only; no input recovery on bought-in travel components |

### 4.4 Partial Exemption -- Analogia Ekptwsis (Pro-Rata) [T2]

**Legislation:** N.2859/2000, Art. 31.

If the business makes both taxable and exempt-without-credit supplies, a proportional deduction applies:

```
Recovery % = (Taxable Turnover + Zero-Rated Turnover + Exempt-with-Credit Turnover)
             / Total Turnover * 100
```

| Rule | Detail | Legislation |
|------|--------|-------------|
| Rounding | Round UP to nearest whole percent | N.2859/2000, Art. 31(1) |
| Provisional rate | Use prior year's rate during the year | N.2859/2000, Art. 31(2) |
| Annual adjustment | Final calculation on Ekkatharistiki Dilosi | N.2859/2000, Art. 31(3) |
| Directly attributable costs | Fully deductible if related to taxable supplies; non-deductible if related to exempt | N.2859/2000, Art. 31(1) |
| Overhead costs | Apply pro-rata percentage | N.2859/2000, Art. 31(1) |
| Blocked categories | OVERRIDE pro-rata -- always 0% | N.2859/2000, Art. 30(4) |
| Adjustment entry | Code 383 on Periodiki Dilosi | N.2859/2000, Art. 31 |

**Flag for reviewer: pro-rata calculation must be confirmed by logistis-forotechnikos before filing. Annual adjustment is mandatory.** [T2]

### 4.5 Capital Goods Adjustment (Diakanonismos Pagion) [T1]

**Legislation:** N.2859/2000, Art. 33.

| Asset Type | Adjustment Period | Threshold | Notes |
|-----------|------------------|-----------|-------|
| Immovable property (akinita) | 10 years | No minimum | Annual recalculation for change in taxable use |
| Movable capital goods (kinita pagia) | 5 years | > EUR 1,500 net | Annual recalculation |
| Services capitalised | 5 years | > EUR 1,500 net | If capitalised as asset |

---

## Section 5: Registration Rules (Eggraphi sto Mitroo FPA)

### 5.1 General Registration Obligation [T1]

**Legislation:** N.2859/2000, Art. 36; N.4174/2013, Art. 10.

| Rule | Detail | Legislation |
|------|--------|-------------|
| General threshold | **No threshold** -- ANY person carrying out taxable economic activity must register | N.2859/2000, Art. 36(1) |
| Commencement | Registration BEFORE first taxable supply | N.2859/2000, Art. 36(1) |
| AFM format | 9 digits; EL prefix for VIES | N.2859/2000, Art. 36(1) |
| Non-established persons | Must register if making taxable supplies in Greece (unless reverse charge applies) | N.2859/2000, Art. 36(1a) |
| Fiscal representative | Required for non-EU persons making supplies in Greece | N.2859/2000, Art. 36(4) |

### 5.2 Small Business Exemption (Mikres Epicheiriseis) [T1]

**Legislation:** N.2859/2000, Art. 39.

| Rule | Detail | Legislation |
|------|--------|-------------|
| Threshold | Annual gross receipts <= **EUR 10,000** | N.2859/2000, Art. 39(1) |
| Effect | Exempt from charging VAT on supplies | N.2859/2000, Art. 39(1) |
| Input VAT | **NO recovery** | N.2859/2000, Art. 39(4) |
| Invoicing | Must issue invoices marked "Apallagi apo FPA -- Art. 39 N.2859/2000" | N.2859/2000, Art. 39(3) |
| Opt-in | May voluntarily register for normal regime | N.2859/2000, Art. 39(5) |
| Cross-border | EU intra-Community acquisitions > EUR 10,000 require registration | N.2859/2000, Art. 11(2) |
| Review | Threshold reviewed annually; exceeding triggers mandatory normal registration | N.2859/2000, Art. 39(2) |

### 5.3 Special Schemes [T2]

| Scheme | Legislation | Key Feature | Tier |
|--------|-------------|-------------|------|
| Flat-rate farmers (agrotes eidikoy kathestwtos) | N.2859/2000, Art. 41 | No VAT charged; flat-rate compensation (6%) from buyers | [T2] |
| Travel agents (taxidiotika grapia) | N.2859/2000, Art. 43 | Margin scheme; VAT on profit margin only | [T2] |
| Used goods, art, antiques | N.2859/2000, Art. 45 | Margin scheme | [T2] |
| Investment gold | N.2859/2000, Art. 47 | Exempt with option to tax | [T2] |
| OSS / IOSS (distance selling B2C) | N.2859/2000, Art. 47a; EU Reg. | EUR 10,000 EU-wide threshold | [T2] |

---

## Section 6: Filing Deadlines and Penalties

### 6.1 Filing Frequency Determination [T1]

**Legislation:** N.2859/2000, Art. 38(1)-(2); N.4174/2013, Art. 6.

| Bookkeeping Method | Filing Frequency | Legislation |
|-------------------|-----------------|-------------|
| Double-entry (diplografika vivlia) | **Monthly** | N.2859/2000, Art. 38(1) |
| Single-entry (aplografika vivlia) | **Quarterly** | N.2859/2000, Art. 38(2) |
| New businesses (first 24 months) | Follow bookkeeping method | N.2859/2000, Art. 38 |
| Non-established taxable persons | Monthly (after initial period may switch to quarterly) | N.2859/2000, Art. 38 |

### 6.2 Filing Deadlines Table [T1]

**Legislation:** N.2859/2000, Art. 38; N.4174/2013, Art. 18.

| Filing | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| Monthly Periodiki Dilosi FPA | Calendar month | **Last business day of the following month** | N.2859/2000, Art. 38(1) |
| Quarterly Periodiki Dilosi FPA | Calendar quarter (Jan-Mar, Apr-Jun, Jul-Sep, Oct-Dec) | **Last business day of the month following the quarter end** | N.2859/2000, Art. 38(2) |
| Ekkatharistiki Dilosi FPA (Annual Summary) | Calendar year | **Deadline per AADE announcement (typically April-May)** | N.2859/2000, Art. 38(3) |
| VIES (Anakefalaiotikos Pinakas) | Calendar month | **26th of the following month** | N.2859/2000, Art. 36(5) |
| Intrastat declaration | Calendar month | **26th of the following month** | Reg. (EC) 638/2004 |
| VAT payment -- full | Same as return | **Same as return filing deadline** | N.2859/2000, Art. 38 |
| VAT payment -- 2 instalments | Monthly/Quarterly | 1st: with return; 2nd: last day of next month | N.2859/2000, Art. 38(5) |
| myDATA income classification | Per transaction | **By 20th of month after issuance** | A.1138/2020, Art. 4 |
| myDATA expense classification | Per transaction | **By 20th of month after receipt** | A.1138/2020, Art. 5 |
| Corrective declaration (tropopoiitiki) | Any prior period | **Before AADE audit notification** | N.4174/2013, Art. 19 |

**Note:** If a deadline falls on a Saturday, Sunday, or public holiday (argia), it moves to the next business day (ergasimi imera). [T1] N.4174/2013, Art. 7.

### 6.3 Quarterly Periods [T1]

| Quarter | Months | Deadline |
|---------|--------|----------|
| Q1 | January -- March | Last business day of April |
| Q2 | April -- June | Last business day of July |
| Q3 | July -- September | Last business day of October |
| Q4 | October -- December | Last business day of January (following year) |

### 6.4 Penalties (Prostima) and Interest (Tokoi) [T1]

**Legislation:** N.4174/2013, Art. 53-59 (Tax Procedure Code penalties).

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of return | EUR 100 per return (up to EUR 500 per year for recurring) | N.4174/2013, Art. 54(1) |
| Failure to file | EUR 250 per return; increases for repeated non-compliance | N.4174/2013, Art. 54(2) |
| Inaccurate return (underdeclared output or overclaimed input) | 10% of additional tax due (if self-corrected); 50% if discovered by AADE | N.4174/2013, Art. 58(1) |
| Late payment of VAT | Interest at 0.73% per month (8.76% annual) on outstanding balance | N.4174/2013, Art. 53(1) |
| Failure to issue invoice (mi ekdosi parastikou) | EUR 2,500 per instance (minimum); 40% of VAT on undocumented supply | N.4174/2013, Art. 55(1) |
| Failure to transmit to myDATA | EUR 100 per document (B2B); EUR 100 per summary (B2C) | A.1138/2020; POL 1025/2022 |
| Issuance of inaccurate invoice | EUR 500 per instance (minimum) | N.4174/2013, Art. 55(2) |
| Failure to register for VAT | EUR 2,500 plus back-assessment of all VAT due | N.4174/2013, Art. 54(5) |

### 6.5 Corrective Declarations [T1]

**Legislation:** N.4174/2013, Art. 19.

| Scenario | Treatment | Penalty Reduction |
|----------|-----------|-------------------|
| Self-correction before audit notification | File tropopoiitiki dilosi | Reduced penalty: 10% surcharge instead of 50% |
| Self-correction after audit notification | May still file but higher penalty | No reduction |
| AADE-initiated correction | Assessment by AADE | Full 50% surcharge plus interest |

---

## Section 7: Reverse Charge Mechanics (Antistrofi Epivarynsi)

### 7.1 Reverse Charge Decision Table [T1]

**Legislation:** N.2859/2000, Art. 11-14 (place of supply), Art. 35 (reverse charge), Art. 14(2)(a) (general rule for B2B services).

| Scenario | Reverse Charge? | Output Code | Input Code | Net Effect | Legislation |
|----------|----------------|-------------|------------|------------|-------------|
| Intra-EU acquisition of goods | YES | 331/332 | 371 | Zero (if fully taxable) | N.2859/2000, Art. 11(1); Art. 35(1)(a) |
| EU B2B services received (Art. 14(2)(a)) | YES | 333/334 | 372 | Zero (if fully taxable) | N.2859/2000, Art. 14(2)(a); Art. 35(1)(b) |
| Non-EU services received (B2B) | YES | 335/336 | 373 | Zero (if fully taxable) | N.2859/2000, Art. 14(2)(a); Art. 35(1)(c) |
| Domestic -- construction services (Art. 35(1)(h)) | YES | 341/342 | 374 | Zero (if fully taxable) | N.2859/2000, Art. 35(1)(h); POL 1135/2014 |
| Domestic -- supply of immovable property (option to tax) | YES | 341/342 | 374 | Zero (if fully taxable) | N.2859/2000, Art. 35(1)(d) |
| Domestic -- investment gold | YES | 341/342 | 374 | Zero (if fully taxable) | N.2859/2000, Art. 35(1)(e); Art. 47 |
| Domestic -- scrap metal / waste materials | YES | 341/342 | 374 | Zero (if fully taxable) | N.2859/2000, Art. 35(1)(f); POL 1103/2015 |
| Domestic -- emission allowances (CO2) | YES | 341/342 | 374 | Zero (if fully taxable) | N.2859/2000, Art. 35(1)(g) |
| Supply from non-established person to GR VAT payer | YES | 341/342 | 374 | Zero (if fully taxable) | N.2859/2000, Art. 35(1)(c) |
| Out-of-scope categories (wages, etc.) | **NO** -- NEVER | -- | -- | -- | N.2859/2000, Art. 2 |
| Local consumption abroad (hotel, restaurant, taxi) | **NO** | -- | -- | Foreign VAT irrecoverable | N.2859/2000, Art. 14(2)(b) |
| EU supplier charged their local VAT > 0% | **NO** | -- | -- | Foreign VAT embedded in cost | N.2859/2000, Art. 35 |

### 7.2 Construction Sector Reverse Charge [T1]

**Legislation:** N.2859/2000, Art. 35(1)(h); POL 1135/2014.

| Rule | Detail |
|------|--------|
| Scope | Construction works, including subcontracted construction, renovation, repair, demolition |
| Who applies | The recipient (contractor or property owner) who is a VAT-registered person |
| Supplier treatment | Issues invoice without VAT, noting "Antistrofi epivarynsi -- Art. 35(1)(h) N.2859/2000" |
| Recipient treatment | Self-assesses output VAT (Code 341/342) and claims input VAT (Code 374) |
| Exceptions | Does NOT apply if recipient is a private individual (B2C); standard VAT applies instead |
| myDATA | Supplier: income type 1.5 (self-billing reverse charge); Recipient: expense type 14.1 with RC marker |

### 7.3 Reverse Charge for Non-Established Persons [T1]

**Legislation:** N.2859/2000, Art. 35(1)(c).

| Rule | Detail |
|------|--------|
| Trigger | Non-established (non-GR) person makes taxable supply in Greece to a GR VAT payer |
| Effect | Greek recipient self-assesses VAT via reverse charge |
| Exception | If the non-established person has a Greek VAT registration and charges Greek VAT, reverse charge does NOT apply |
| B2C supplies | Non-established person must register in Greece and charge Greek VAT directly |

---

## Section 8: myDATA Platform and E-Invoicing

### 8.1 myDATA Overview [T1]

**Legislation:** POL 1138/2020; A.1138/2020; A.1052/2023.

myDATA (my Digital Accounting and Tax Application) is AADE's platform for real-time digital transmission of all income and expense documents. All Greek VAT-registered entities must transmit transaction summaries.

### 8.2 myDATA Income/Expense Classification Table [T1]

| Code | Type | Use | Legislation |
|------|------|-----|-------------|
| 1.1 | Timologio polisis (Sales invoice) | Domestic B2B sales | POL 1138/2020, Art. 3 |
| 1.2 | Timologio parochis ypiresion (Service invoice) | Domestic service sales | POL 1138/2020, Art. 3 |
| 1.3 | Pistotico timologio (Credit note) | Returns, discounts | POL 1138/2020, Art. 3 |
| 1.4 | Symvolayo (Contract-based income) | Long-term contracts | POL 1138/2020, Art. 3 |
| 1.5 | Aftotymoligia (Self-billing) | Reverse charge self-billing | POL 1138/2020, Art. 3 |
| 2.1 | Timologio endokoinotikis paradosis (Intra-EU supply) | EU goods sales | POL 1138/2020, Art. 3 |
| 2.2 | Timologio exagogis (Export invoice) | Non-EU goods sales | POL 1138/2020, Art. 3 |
| 11.1-11.5 | Eggrafes autoparadosis / RC entries | Acquisition self-assessment | POL 1138/2020, Art. 5 |
| 14.1 | Timologio agoron (Purchase invoice) | Domestic purchases | POL 1138/2020, Art. 5 |
| 14.2 | Endokoinotiki apoktisi (Intra-EU acquisition) | EU goods received | POL 1138/2020, Art. 5 |
| 14.3 | Eisagogi (Import) | Non-EU goods | POL 1138/2020, Art. 5 |
| 14.4 | Lipsi ypiresion apo EE (EU services received) | EU services | POL 1138/2020, Art. 5 |
| 14.5 | Lipsi ypiresion apo trites chores (Non-EU services) | Non-EU services | POL 1138/2020, Art. 5 |

### 8.3 Mandatory B2B E-Invoicing Timeline [T1]

**Legislation:** A.1052/2023; AADE announcements.

| Phase | Start Date | Scope | Notes |
|-------|-----------|-------|-------|
| Phase 0 | 1 September 2025 | B2G contracts (public procurement) | Government suppliers |
| Phase 1 | 2 March 2026 | Businesses with 2023 revenue > EUR 1,000,000 | Large enterprises |
| Phase 2 | 1 October 2026 | All remaining businesses | Universal B2B e-invoicing |

**Consequence:** After the applicable mandatory date, invoices NOT issued through an approved e-invoicing provider connected to myDATA may not be accepted for input VAT deduction by the recipient. [T1] A.1052/2023, Art. 6.

### 8.4 myDATA Transmission Methods [T1]

| Method | Description | Legislation |
|--------|-------------|-------------|
| ERP direct integration | Business ERP transmits XML to AADE API | A.1138/2020 |
| Certified e-invoicing provider (PAP) | Third-party provider transmits on behalf of business | A.1052/2023 |
| AADE free tool (timologio) | AADE's free invoicing platform for small businesses | A.1138/2020 |
| Manual entry via myAADE portal | Manual data entry for low-volume businesses | A.1138/2020 |

---

## Section 9: Edge Case Registry

### EC1 -- Hotel in another EU country [T1]

**Situation:** Greek VAT payer pays for a hotel in France. Invoice shows French 10% TVA.
**Resolution:** NOT reverse charge. French VAT was charged at source (local consumption). No Greek VAT entries. French VAT is an irrecoverable cost embedded in the expense amount.
**Legislation:** N.2859/2000, Art. 14(2)(b) -- immovable property rule; place of supply is where the property is located.
**myDATA:** No myDATA transmission required for foreign VAT-only expenses.

### EC2 -- SaaS subscription from US provider [T1]

**Situation:** Monthly charge from US company (e.g., AWS, Notion), no VAT on invoice.
**Resolution:** Import of services from non-EU. Reverse charge applies.
- Code 335 = base amount
- Code 336 = output VAT at 24%
- Code 373 = input VAT at 24%
- Net effect: zero for fully taxable business.
**Legislation:** N.2859/2000, Art. 14(2)(a) (place of supply = recipient); Art. 35(1)(c).
**myDATA:** Expense Type 14.5.

### EC3 -- Intra-EU goods acquisition from Germany [T1]

**Situation:** Greek company buys goods from German supplier. Invoice at 0% with DE VAT number.
**Resolution:** Intra-EU acquisition. Reverse charge applies.
- Code 331 = base amount
- Code 332 = output VAT at 24%
- Code 371 = input VAT at 24%
- Net effect: zero. VIES filing required.
**Legislation:** N.2859/2000, Art. 11(1); Art. 35(1)(a).
**myDATA:** Expense Type 14.2.

### EC4 -- Passenger car purchase (blocked) [T1]

**Situation:** Company buys passenger car EUR 20,000 + EUR 4,800 VAT (24%).
**Resolution:** Input VAT **BLOCKED**. No deduction in Code 361 or any other input code. Full EUR 24,800 is a cost.
**Exception:** Only deductible if business is a taxi operator, car rental company, driving school, or car dealer (resale).
**Legislation:** N.2859/2000, Art. 30(4)(a).
**myDATA:** Expense Type 14.1; mark as non-deductible.

### EC5 -- Client entertainment dinner (blocked) [T1]

**Situation:** Business dinner with clients at restaurant. EUR 200 + EUR 26 VAT (13%).
**Resolution:** Input VAT **BLOCKED** under entertainment/hospitality. Full EUR 226 is a cost. No input VAT recovery.
**Legislation:** N.2859/2000, Art. 30(4)(b).
**myDATA:** Expense Type 14.1; mark as non-deductible.

### EC6 -- EU B2B service sale (consulting to Italy) [T1]

**Situation:** Greek company provides engineering consulting services to Italian B2B client.
**Resolution:** Place of supply is Italy (recipient's country). Report in Code 313. No Greek output VAT. Italian customer reverse charges in Italy. VIES filing required.
**Legislation:** N.2859/2000, Art. 14(2)(a); Art. 28(a).
**myDATA:** Income Type 2.1.

### EC7 -- Restaurant on Mykonos (Aegean island rate) [T2]

**Situation:** Restaurant on Mykonos serves meals. Mainland catering rate would be 13%.
**Resolution:** Mykonos is an eligible Aegean island. Island reduced rate of **9%** applies (13% x 0.70 = 9.1% -> 9%). Report in Code 309 (base) / Code 310 (output VAT at 9%).
**Flag for reviewer:** Confirm (a) Mykonos remains on the eligible island list, (b) supply is food/beverage consumed on the island.
**Legislation:** N.2859/2000, Art. 21(4); POL 1150/2001.
**myDATA:** Income Type 1.1; rate 9%.

### EC8 -- Credit note from supplier [T1]

**Situation:** Supplier issues pistotico timologio (credit note) for EUR 500 relating to a prior 24% purchase.
**Resolution:** Reduce Code 361 by EUR 120 (the VAT on the credited amount). Reduce the base in the relevant purchase tracking. myDATA classification must be updated with a Type 1.3 entry.
**Legislation:** N.2859/2000, Art. 19(5); POL 1138/2020.
**myDATA:** Income Type 1.3 (credit note).

### EC9 -- Physical goods import from China via Piraeus [T2]

**Situation:** Client imports goods from China through Piraeus port customs.
**Resolution:** VAT is assessed by Greek customs on the import declaration (DETE / eniaio diakoinotiko eggrafo). The VAT appears on the customs document. Input VAT from customs is claimed in Code 381.
**Flag for reviewer:** Confirm the customs documentation (DETE) is complete and amounts match. Customs value includes CIF (cost, insurance, freight) plus customs duty.
**Legislation:** N.2859/2000, Art. 17 (importation); Art. 20 (taxable amount on import).
**myDATA:** Expense Type 14.3.

### EC10 -- Flat-rate farmer selling agricultural products [T2]

**Situation:** Farmer under flat-rate scheme (Art. 41) sells olive oil to a processor.
**Resolution:** Farmer does NOT charge VAT. Buyer issues self-billing document (aftotymoligio) and pays flat-rate compensation of **6%** on the purchase price. Buyer deducts the 6% compensation as input VAT equivalent.
**Flag for reviewer:** Confirm farmer is registered under Art. 41 and flat-rate compensation percentage is current.
**Legislation:** N.2859/2000, Art. 41.
**myDATA:** Buyer: Expense Type 14.1 with flat-rate marker.

### EC11 -- myDATA transmission failure [T1]

**Situation:** Business issued an invoice but failed to transmit to myDATA within the required timeframe.
**Resolution:** Late transmission incurs penalty of EUR 100 per document (B2B) or EUR 100 per summary (B2C). The invoice is still valid but the penalty applies. After the mandatory e-invoicing date (Phase 1/2), failure may result in the recipient being unable to deduct input VAT.
**Legislation:** A.1138/2020; POL 1025/2022; A.1052/2023, Art. 6.

### EC12 -- Commercial vehicle (van) purchase -- deductible [T1]

**Situation:** Company buys a delivery van (< 3.5 tonnes) for EUR 15,000 + EUR 3,600 VAT (24%).
**Resolution:** Input VAT is **FULLY DEDUCTIBLE** -- commercial vehicles are NOT blocked. Report VAT in Code 382 (fixed asset if > EUR 1,500 net) or Code 361 (if below threshold, unlikely for a van). 5-year capital goods adjustment applies.
**Legislation:** N.2859/2000, Art. 30(4)(a) -- blocking applies only to passenger cars (epivathga), not commercial (forthga). Art. 33 (capital goods adjustment).

### EC13 -- Shipping company supplying fuel to vessels [T3]

**Situation:** Shipping company supplies bunker fuel to ocean-going vessels.
**Resolution:** **ESCALATE.** Maritime/shipping VAT involves complex exemptions under N.2859/2000, Art. 27(1)(a) (supply of vessels used for commercial navigation). Ship supply is exempt with credit. Requires specialist maritime tax knowledge.
**Legislation:** N.2859/2000, Art. 27(1)(a)-(c).
**Flag:** T3 -- refer to specialist logistis-forotechnikos with maritime experience.

### EC14 -- Construction subcontractor invoice (domestic reverse charge) [T1]

**Situation:** Subcontractor issues invoice for EUR 10,000 construction works to a VAT-registered contractor, noting "Antistrofi epivarynsi -- Art. 35(1)(h)".
**Resolution:** Domestic reverse charge applies. Contractor reports:
- Code 341 = EUR 10,000 (base)
- Code 342 = EUR 2,400 (output VAT at 24%)
- Code 374 = EUR 2,400 (input VAT)
- Net effect: zero.
**Legislation:** N.2859/2000, Art. 35(1)(h); POL 1135/2014.
**myDATA:** Expense Type 14.1 with reverse charge marker.

### EC15 -- Short-term holiday rental (Airbnb-style) on island [T2]

**Situation:** Property owner on Santorini rents furnished apartment short-term via booking platform.
**Resolution:** Short-term rental (< 1 year) is a taxable supply. Hotel accommodation rate applies: **9%** on Santorini (island reduced rate: 13% x 0.70 = 9%). Report in Code 309/310. If owner is below EUR 10,000 threshold, Art. 39 exemption may apply. Platform may withhold/remit VAT under OSS.
**Flag for reviewer:** Confirm island eligibility, rental duration, registration status, and whether platform is remitting VAT via OSS.
**Legislation:** N.2859/2000, Art. 21(4); Art. 39; Art. 47a (OSS).

### EC16 -- Scrap metal sale (domestic reverse charge) [T1]

**Situation:** Manufacturer sells scrap metal to a recycler. Both are Greek VAT-registered.
**Resolution:** Domestic reverse charge applies for scrap metal / waste materials.
- Seller issues invoice without VAT, noting "Antistrofi epivarynsi -- Art. 35(1)(f)"
- Buyer reports: Code 341/342 (output) and Code 374 (input)
**Legislation:** N.2859/2000, Art. 35(1)(f); POL 1103/2015.

### EC17 -- Mixed-use telecommunications expense [T2]

**Situation:** Business mobile phone bill -- 60% business, 40% personal use.
**Resolution:** Only the business portion (60%) of input VAT is deductible. The personal portion (40%) is blocked under N.2859/2000, Art. 30(4)(e).
**Flag for reviewer:** Confirm the business/personal apportionment percentage. AADE may challenge aggressive splits.
**Legislation:** N.2859/2000, Art. 30(4)(e); Art. 30(1).

### EC18 -- Sale of new building within 5 years of construction [T2]

**Situation:** Developer sells newly constructed apartment within 5 years of completion.
**Resolution:** Sale of new building within 5 years is subject to VAT at 24% (not exempt). After 5 years, the sale is exempt without credit unless the seller opts to apply VAT. This is one of the few cases where immovable property sale is taxable.
**Flag for reviewer:** Confirm the 5-year window and whether the seller has opted to tax.
**Legislation:** N.2859/2000, Art. 6(2)(b); Art. 22(1)(kb).

---

## Section 10: Comparison with Malta VAT

### 10.1 Structural Comparison [T1]

| Feature | Greece | Malta | Key Difference |
|---------|--------|-------|----------------|
| **Primary legislation** | N.2859/2000 (Kodikas FPA) | VAT Act Chapter 406 | Different statutory frameworks |
| **Tax authority** | AADE | Commissioner for Revenue (CFR) | AADE is independent authority; CFR is government body |
| **Filing portal** | myTAXISnet / myAADE | cfr.gov.mt (VAT Online) | Both electronic-only for standard filers |
| **Standard rate** | **24%** | **18%** | Greece 6 points higher |
| **Reduced rate(s)** | 13% and 6% | 12%, 7%, and 5% | Greece has two tiers; Malta has three |
| **Island/geographic rates** | YES -- 17%, 9%, 4% on Aegean islands | NO geographic variation | Unique to Greece |
| **Return form** | Periodiki Dilosi FPA (F2) | VAT3 | Different box numbering systems |
| **Filing frequency** | Monthly (double-entry) / Quarterly (single-entry) | Quarterly (standard) / Monthly (Art. 12) / Annual (Art. 11) | Greece links to bookkeeping method; Malta links to registration type |
| **Small enterprise threshold** | EUR 10,000 (Art. 39) | EUR 35,000 (Art. 11) | Malta has much higher threshold |
| **Registration threshold** | No general threshold -- all activity requires registration | Article 10 mandatory above EUR 35,000; Article 12 for certain EU activities | Greece more strict |
| **Capital goods threshold** | EUR 1,500 net | EUR 1,160 gross | Different valuation basis (net vs. gross) |
| **Capital goods adjustment -- immovable** | 10 years | 10 years | Same |
| **Capital goods adjustment -- movable** | 5 years | 5 years | Same |
| **E-invoicing** | myDATA mandatory (phased 2025-2026) | Not yet mandatory | Greece ahead on e-invoicing |
| **Domestic reverse charge** | Extensive: construction, scrap, gold, emissions, property | Limited: not widely applied domestically | Greece has broader domestic RC |

### 10.2 Rate Comparison Table [T1]

| Category | Greece Rate | Malta Rate | Notes |
|----------|-----------|-----------|-------|
| General goods/services | 24% | 18% | Standard rate |
| Hotel accommodation | 13% (9% on islands) | 7% | Malta significantly lower |
| Restaurant/catering | 13% (9% on islands) | 18% | Greece lower for food |
| Medicines | 6% (4% on islands) | 0% | Malta zero-rates medicines |
| Books | 6% (4% on islands) | 5% | Similar |
| Electricity | 6% (4% on islands) | 5% | Similar |
| Financial services | Exempt | Exempt | Same |
| Insurance | Exempt | Exempt | Same |
| Healthcare | Exempt | Exempt | Same |

### 10.3 Blocked Categories Comparison [T1]

| Category | Greece (N.2859/2000, Art. 30(4)) | Malta (10th Schedule) | Difference |
|----------|--------------------------------|----------------------|------------|
| Passenger cars | Blocked | Blocked | Same |
| Fuel for passenger cars | Blocked | Blocked (follows vehicle) | Same |
| Entertainment | Blocked | Blocked | Same treatment; Greece: Art. 30(4)(b); Malta: Item 3(1)(b) |
| Tobacco | Blocked | Blocked | Same |
| Alcohol | Not specifically blocked (24% rate) | Blocked | Malta blocks; Greece does not specifically |
| Art/antiques | Not specifically blocked | Blocked | Malta blocks; Greece does not |
| Yachts/pleasure craft | Blocked | Blocked | Same |
| Personal use | Blocked | Blocked | Same |

### 10.4 Process Comparison [T1]

| Process Step | Greece | Malta |
|-------------|--------|-------|
| Classify transaction type | Same logic: sale/purchase/out-of-scope | Same |
| Determine counterparty location | Same: domestic/EU/non-EU | Same |
| Apply rate | More complex (3 mainland + 3 island rates) | Simpler (4 rates, no geographic variation) |
| Check blocked categories | Similar list with some differences | Similar |
| Apply reverse charge | Same EU/non-EU logic; broader domestic RC | Same EU/non-EU logic; minimal domestic RC |
| Assign form codes | F2 codes (301-512) | VAT3 boxes (1-45) |
| E-invoicing | myDATA mandatory | Not mandatory |
| File return | Monthly/Quarterly via myAADE | Quarterly via cfr.gov.mt |

---

## Section 11: PROHIBITIONS [T1]

These prohibitions are absolute. No exception. No reviewer override. Violation of any prohibition is a critical error.

1. **NEVER** let AI guess VAT form code assignment -- it is 100% deterministic from transaction facts. N.2859/2000, Art. 38.
2. **NEVER** claim input VAT on passenger cars, motorcycles (>50cc), or their running costs (fuel, maintenance, insurance) unless a proven exception applies (taxi, car rental, driving school, dealer resale). N.2859/2000, Art. 30(4)(a).
3. **NEVER** claim input VAT on entertainment, hospitality, or tobacco unless the business is in the hospitality trade and the expense is for its own trade supplies. N.2859/2000, Art. 30(4)(b)-(c).
4. **NEVER** apply island reduced rates (17%/9%/4%) without confirming: (a) the specific island is on the eligible list per current legislation, (b) the supply type qualifies for the reduction, (c) no recent legislative change has modified eligibility. N.2859/2000, Art. 21(4).
5. **NEVER** apply reverse charge to out-of-scope categories (salaries, social contributions, income tax, loan repayments, dividends, fines). N.2859/2000, Art. 2.
6. **NEVER** apply reverse charge when the EU supplier has charged their local VAT (> 0%) on the invoice. The foreign VAT is embedded in the cost. N.2859/2000, Art. 35.
7. **NEVER** apply reverse charge to local consumption services abroad (hotel, restaurant, taxi, conference in another country). N.2859/2000, Art. 14(2)(b).
8. **NEVER** allow Art. 39 (small business exempt) entities to claim input VAT. N.2859/2000, Art. 39(4).
9. **NEVER** allow flat-rate farmers (Art. 41) to claim input VAT -- they receive flat-rate compensation instead. N.2859/2000, Art. 41.
10. **NEVER** confuse zero-rated (Code 311/312/313/322 -- input VAT IS deductible) with exempt-without-credit (Code 321 -- input VAT is NOT deductible). N.2859/2000, Art. 22 vs. Art. 24-28.
11. **NEVER** ignore myDATA classification obligations -- all income and expense documents must be transmitted. POL 1138/2020; A.1052/2023.
12. **NEVER** issue invoices without myDATA transmission after the applicable mandatory e-invoicing date (Phase 0/1/2). A.1052/2023, Art. 6.
13. **NEVER** compute any number -- all arithmetic is handled by the deterministic engine, not the AI. The AI classifies; the engine calculates.
14. **NEVER** file a return for a period where the client's AFM, registration status, or filing frequency is unknown or unconfirmed.
15. **NEVER** apply the construction reverse charge (Art. 35(1)(h)) to B2C supplies -- standard VAT applies when the recipient is a private individual. POL 1135/2014.
16. **NEVER** treat shipping/maritime VAT without specialist escalation (T3). N.2859/2000, Art. 27.

---

## Section 12: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard domestic purchase, 24% VAT [T1]

**Input:** Greek supplier, office equipment, EUR 1,000 net + EUR 240 VAT. Normal VAT payer, mainland.
**Expected output:** Code 361 += EUR 240. Fully deductible. myDATA Expense Type 14.1.
**Legislation:** N.2859/2000, Art. 30(1).

### Test 2 -- Import of services from US (SaaS subscription) [T1]

**Input:** US supplier (AWS), monthly fee EUR 50, no VAT on invoice. Normal VAT payer.
**Expected output:** Code 335 = EUR 50 (base), Code 336 = EUR 12 (24%), Code 373 = EUR 12 (input). Net = zero. myDATA Expense Type 14.5.
**Legislation:** N.2859/2000, Art. 14(2)(a); Art. 35(1)(c).

### Test 3 -- Intra-EU goods acquisition from Germany [T1]

**Input:** German supplier, goods EUR 5,000 at 0% with DE VAT number. Normal VAT payer.
**Expected output:** Code 331 = EUR 5,000 (base), Code 332 = EUR 1,200 (24%), Code 371 = EUR 1,200 (input). Net = zero. VIES filing required. myDATA Expense Type 14.2.
**Legislation:** N.2859/2000, Art. 11(1); Art. 35(1)(a).

### Test 4 -- Passenger car purchase (blocked) [T1]

**Input:** Car EUR 15,000 + EUR 3,600 VAT (24%). Mixed use. Not a taxi/rental company.
**Expected output:** Code 361 += EUR 0. VAT **BLOCKED**. Full EUR 18,600 is cost.
**Legislation:** N.2859/2000, Art. 30(4)(a).

### Test 5 -- EU B2B service sale (consulting to France) [T1]

**Input:** Greek company invoices French B2B client EUR 3,000 for consulting. French client is VAT-registered.
**Expected output:** Code 313 = EUR 3,000. No output VAT. VIES filing required. myDATA Income Type 2.1.
**Legislation:** N.2859/2000, Art. 14(2)(a); Art. 28(a).

### Test 6 -- Restaurant meal at 13% (non-entertainment, mainland) [T1]

**Input:** Business lunch for employee, EUR 100 net + EUR 13 VAT (13%). Not client entertainment. Mainland.
**Expected output:** Code 362 += EUR 13. Deductible (ordinary business meal for employee, not client entertainment/hospitality).
**Legislation:** N.2859/2000, Art. 30(1); not blocked under Art. 30(4)(b) because not entertainment.

### Test 7 -- Client entertainment dinner (blocked) [T1]

**Input:** Dinner entertaining clients, EUR 300 net + EUR 39 VAT (13%). Mainland.
**Expected output:** Code 362 += EUR 0. VAT **BLOCKED**. Full EUR 339 is cost.
**Legislation:** N.2859/2000, Art. 30(4)(b).

### Test 8 -- Export of goods to USA [T1]

**Input:** Greek company exports textiles to US client, EUR 10,000.
**Expected output:** Code 312 = EUR 10,000. No output VAT. Zero-rated with credit (input VAT on related purchases is deductible). myDATA Income Type 2.2.
**Legislation:** N.2859/2000, Art. 24(1).

### Test 9 -- Aegean island sale at 17% [T2]

**Input:** Retailer on Lesvos sells electronics (standard-rated) for EUR 500 net. Lesvos is an eligible island.
**Expected output:** Code 307 = EUR 500 (base), Code 308 = EUR 85 (17%). Reviewer must confirm Lesvos eligibility.
**Legislation:** N.2859/2000, Art. 21(4); POL 1150/2001.

### Test 10 -- Domestic construction reverse charge [T1]

**Input:** Subcontractor invoices EUR 8,000 for building renovation to VAT-registered contractor. Invoice notes Art. 35(1)(h).
**Expected output:** Code 341 = EUR 8,000 (base), Code 342 = EUR 1,920 (24%), Code 374 = EUR 1,920 (input). Net = zero. myDATA Expense Type 14.1 with RC marker.
**Legislation:** N.2859/2000, Art. 35(1)(h); POL 1135/2014.

### Test 11 -- EU hotel (local consumption, NOT reverse charge) [T1]

**Input:** Greek VAT payer stays at hotel in Italy. Invoice shows EUR 300 with Italian 10% IVA of EUR 27.27.
**Expected output:** No Greek VAT return entry. Full EUR 300 is cost including irrecoverable foreign VAT. NOT reverse charge.
**Legislation:** N.2859/2000, Art. 14(2)(b).

### Test 12 -- Pharmacy selling medicines at 6% [T1]

**Input:** Pharmacy on mainland sells prescription medicines EUR 200 net.
**Expected output:** Code 305 = EUR 200 (base), Code 306 = EUR 12 (6%). myDATA Income Type 1.1.
**Legislation:** N.2859/2000, Art. 21(1)(c); Annex III, Part B.

### Test 13 -- Fuel for blocked passenger car [T1]

**Input:** EUR 80 net + EUR 19.20 VAT (24%) for petrol. Vehicle is a passenger car (not taxi/rental).
**Expected output:** Code 361 += EUR 0. VAT **BLOCKED**. Fuel follows the vehicle blocking rule.
**Legislation:** N.2859/2000, Art. 30(4)(a).

### Test 14 -- Fuel for commercial van (deductible) [T1]

**Input:** EUR 80 net + EUR 19.20 VAT (24%) for diesel. Vehicle is a delivery van (forthgo < 3.5t).
**Expected output:** Code 361 += EUR 19.20. Fully deductible. Commercial vehicle fuel is not blocked.
**Legislation:** N.2859/2000, Art. 30(1); Art. 30(4)(a) does not apply to commercial vehicles.

---

## Reviewer Escalation Protocol

### Tier 2 Escalation Format [T2]

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous or requires confirmation]
Options: [list the possible treatments with legislation references]
Recommended: [which treatment is most likely correct and why]
Action Required: Logistis-forotechnikos must confirm before filing.
Legislation: [relevant N.2859/2000 article or POL circular]
```

### Tier 3 Escalation Format [T3]

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified logistis-forotechnikos with specialist expertise. Document the gap.
Legislation: [relevant N.2859/2000 article if known]
```

---

## Contribution Notes

This skill was written based on publicly available information about Greece's VAT system under N.2859/2000 (Kodikas FPA) as amended, N.4174/2013 (Tax Procedure Code), and supporting POL circulars and AADE decisions. Greece-specific features covered include:

- Aegean island reduced rates (17%/9%/4%) under Art. 21(4)
- Mandatory myDATA electronic books and e-invoicing under POL 1138/2020 and A.1052/2023
- Extensive domestic reverse charge provisions (construction, scrap metal, emissions, investment gold) under Art. 35
- Shipping and maritime exemptions under Art. 27 (T3 escalation)
- Tourism sector reduced rates (hotel 13%/9%, catering 13%/9%)
- Flat-rate farmer scheme under Art. 41
- Construction reverse charge under Art. 35(1)(h) and POL 1135/2014

VAT rates verified against PwC Tax Summaries (Greece -- Corporate -- Other Taxes, 2025/2026 edition): standard 24%, reduced 13%, super-reduced 6%, island rates at 30% discount (17%/9%/4%).

**This skill requires validation by a qualified Greek logistis-forotechnikos before use in production.**

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
