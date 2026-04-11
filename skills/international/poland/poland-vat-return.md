---
name: poland-vat-return
description: Use this skill whenever asked to prepare, review, or create a Poland VAT return (JPK_V7M/JPK_V7K declaration) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in JPK", "create the return", "Polish VAT", or any request involving Poland VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Poland VAT classification rules, JPK_V7 field mappings, deductibility rules, reverse charge treatment, split payment mechanism (MPP), GTU reporting codes, white list verification, capital goods thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Polish VAT-related work.
---

# Poland VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Poland (Rzeczpospolita Polska) |
| Jurisdiction Code | PL |
| Primary Legislation | Ustawa z dnia 11 marca 2004 r. o podatku od towarow i uslug (ustawa o VAT) -- Journal of Laws 2004 No. 54 item 535, as amended |
| Supporting Legislation | Ordynacja podatkowa (Tax Ordinance); Kodeks karny skarbowy (KKS -- Fiscal Penal Code); Rozporzadzenie Ministra Finansow w sprawie JPK_V7M/JPK_V7K; Annex 15 to ustawa o VAT (split payment goods/services) |
| Tax Authority | Krajowa Administracja Skarbowa (KAS -- National Revenue Administration) |
| Filing Portal | e-Urzad Skarbowy (https://e-urzadskarbowy.podatki.gov.pl) and https://www.podatki.gov.pl |
| Contributor | Auto-generated -- requires validation by doradca podatkowy |
| Validated By | Deep research verification, April 2026 |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Status | awaiting-validation |
| Confidence Coverage | Tier 1: JPK_V7 field assignment, reverse charge, deductibility blocks, split payment rules, GTU codes, white list. Tier 2: partial exemption pro-rata (proporcja/prewspolczynnik), mixed-use vehicle apportionment, KSeF transition issues. Tier 3: complex group structures (grupa VAT), tax grouping, special economic zones, transfer pricing adjustments on VAT. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. The engine computes; the AI classifies.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A doradca podatkowy (licensed tax adviser) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and NIP (Numer Identyfikacji Podatkowej)** [T1] -- For EU VIES purposes the format is PL + 10 digits (e.g., PL1234567890). Domestically, the NIP is 10 digits without the PL prefix. **ustawa o VAT, Art. 96 ust. 1.**
2. **VAT registration status** [T1] -- Active VAT payer (czynny podatnik VAT), VAT-exempt (podatnik zwolniony), or not registered. **ustawa o VAT, Art. 96.**
3. **Filing frequency** [T1] -- Monthly (JPK_V7M) or Quarterly (JPK_V7K). Quarterly filing is available only to entities qualifying as "maly podatnik" (small taxpayer -- annual revenue up to PLN 2,000,000 equivalent in EUR) and not in their first 12 months of VAT registration. **ustawa o VAT, Art. 99 ust. 2-3.**
4. **Industry/sector** [T2] -- Impacts deductibility (e.g., hospitality, automotive, construction) and GTU code requirements.
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (proporcja under Art. 90 or prewspolczynnik under Art. 86 ust. 2a). Reviewer must confirm rate. **ustawa o VAT, Art. 90, Art. 86 ust. 2a.**
6. **Does the business trade goods/services listed in Annex 15?** [T1] -- Impacts mandatory split payment (mechanizm podzielonej platnosci / MPP). **ustawa o VAT, Art. 108a.**
7. **Does the business use passenger vehicles for mixed purposes?** [T1] -- 50% VAT deduction limit applies. **ustawa o VAT, Art. 86a.**
8. **Does the business claim 100% vehicle VAT (full business use)?** [T2] -- Requires vehicle usage log (ewidencja przebiegu pojazdu) with GPS tracking, declaration to tax office on VAT-26 form, and defined vehicle usage rules. Reviewer must verify compliance. **ustawa o VAT, Art. 86a ust. 4-12.**
9. **Excess credit brought forward** [T1] -- From prior period (field P_51 in JPK_V7).
10. **Is the entity part of a VAT group (grupa VAT)?** [T3] -- If yes, escalate. Group VAT has separate rules. **ustawa o VAT, Art. 15a.**

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: VAT Return Form Structure -- JPK_V7M / JPK_V7K

### 1a. Overview [T1]

**Legislation:** ustawa o VAT, Art. 99; Art. 109 ust. 3; Rozporzadzenie Ministra Finansow w sprawie szczegolowego zakresu danych zawartych w deklaracjach podatkowych i w ewidencji w zakresie podatku od towarow i uslug.

Poland uses a **merged declaration and SAF-T file** called JPK_V7. There are two variants:

| Variant | Filer Type | Contents | Filing Frequency |
|---------|-----------|----------|-----------------|
| **JPK_V7M** | Monthly filer | Deklaracja (declaration) + Ewidencja (records) every month | Monthly -- by 25th of following month |
| **JPK_V7K** | Quarterly filer (maly podatnik) | Ewidencja (records) monthly + Deklaracja (declaration) quarterly (in month 3 of quarter) | Records monthly; declaration quarterly |

The file is submitted electronically via **e-Urzad Skarbowy** (https://e-urzadskarbowy.podatki.gov.pl). Paper filing is NOT permitted.

### 1b. JPK_V7 Structure -- Deklaracja (Declaration Part) [T1]

The Deklaracja section contains aggregate tax figures. Fields use the **P_** prefix in the XML schema.

#### Output VAT Fields (Podatek Nalezny -- Sales Side)

| Field | Description | Rate / Type | ustawa o VAT Reference |
|-------|-------------|-------------|----------------------|
| P_10 | Taxable base -- Intra-EU supply of goods (WDT) | 0% | Art. 13 ust. 1, Art. 42 |
| P_11 | Taxable base -- Export of goods to non-EU | 0% | Art. 2 pkt 8, Art. 41 ust. 4-9 |
| P_12 | Taxable base -- Supply of services where buyer is liable (EU/non-EU B2B) | n/a (no PL VAT) | Art. 28b |
| P_13 | Taxable base -- Domestic supply at 23% | 23% | Art. 41 ust. 1 |
| P_14 | Output VAT at 23% (tax on P_13) | -- | Art. 41 ust. 1 |
| P_15 | Taxable base -- Domestic supply at 8% | 8% | Art. 41 ust. 2 |
| P_16 | Output VAT at 8% (tax on P_15) | -- | Art. 41 ust. 2 |
| P_17 | Taxable base -- Domestic supply at 5% | 5% | Art. 41 ust. 2a |
| P_18 | Output VAT at 5% (tax on P_17) | -- | Art. 41 ust. 2a |
| P_19 | Taxable base -- Domestic supply at 0% | 0% | Art. 41 ust. 3-3e |
| P_20 | Taxable base -- Exempt supplies (without right to deduct) | exempt | Art. 43 |
| P_21 | Taxable base -- Intra-EU acquisition of goods (WNT) | RC | Art. 20 ust. 5, Art. 9 |
| P_22 | Output VAT on intra-EU acquisition (self-assessed) | -- | Art. 20 ust. 5 |
| P_23 | Taxable base -- Import of goods (simplified procedure Art. 33a or procedure 42/63) | RC | Art. 33a |
| P_24 | Output VAT on import of goods (self-assessed) | -- | Art. 33a |
| P_25 | Taxable base -- Import of services (Art. 28b) | RC | Art. 28b |
| P_26 | Output VAT on import of services (self-assessed) | -- | Art. 28b |
| P_27 | Taxable base -- Domestic supply where buyer is liable (Art. 17(1) pkt 7-8) | RC | Art. 17 ust. 1 pkt 7-8 |
| P_28 | Output VAT on domestic reverse charge (self-assessed) | -- | Art. 17 ust. 1 pkt 7-8 |
| P_37 | **Total output VAT** | sum | -- |
| P_38 | Total output VAT (= P_37, carried forward) | sum | -- |

#### Input VAT Fields (Podatek Naliczony -- Purchase Side)

| Field | Description | ustawa o VAT Reference |
|-------|-------------|----------------------|
| P_40 | Input VAT on intra-EU acquisitions (WNT) | Art. 86 ust. 2 pkt 4 |
| P_41 | Input VAT on import of goods (from customs document SAD/C88 or Art. 33a) | Art. 86 ust. 2 pkt 2 |
| P_42 | Input VAT on import of services | Art. 86 ust. 2 pkt 4 |
| P_43 | Input VAT on domestic purchases (general) | Art. 86 ust. 2 pkt 1 |
| P_44 | Input VAT on domestic reverse charge purchases | Art. 86 ust. 2 pkt 4 |
| P_45 | Input VAT on fixed asset purchases (srodki trwale) | Art. 86 ust. 2 pkt 1 |
| P_46 | Correction of input VAT from prior periods | Art. 89b, Art. 91 |
| P_48 | **Total input VAT** | sum |

#### Summary / Settlement Fields

| Field | Description | ustawa o VAT Reference |
|-------|-------------|----------------------|
| P_49 | Excess of input VAT over output VAT (credit) | Art. 87 |
| P_50 | VAT payable to tax office | Art. 103 |
| P_51 | Excess from prior period brought forward | Art. 87 ust. 1 |
| P_52 | Excess including prior period amounts | Art. 87 |
| P_53 | Amount of excess to carry forward to next period | Art. 87 ust. 1 |
| P_54 | Amount of excess requested for refund | Art. 87 ust. 1-2 |
| P_55 | Refund to bank account in 60 days | Art. 87 ust. 2 |
| P_56 | Refund to bank account in 25 days (accelerated) | Art. 87 ust. 6 |
| P_57 | Refund to VAT account in 25 days | Art. 87 ust. 6a |
| P_60 | Refund to bank account in 40 days | Art. 87 ust. 2 |
| P_62 | **Final amount payable or credit** | -- |

### 1c. JPK_V7 Structure -- Ewidencja (Records Part) [T1]

The Ewidencja section contains **transaction-level detail** for every invoice/document. It is split into:

- **SprzedazWiersz** (sales records) -- each sales invoice with amounts, GTU codes, transaction type markers
- **ZakupWiersz** (purchase records) -- each purchase invoice with amounts, document type

Key attributes on sales records:

| Attribute | Description |
|-----------|-------------|
| KodKrajuNadaniaTIN | Country code of buyer's tax ID |
| NrKontrahenta | Buyer's tax ID (NIP or EU VAT number) |
| NazwaKontrahenta | Buyer's name |
| DowodSprzedazy | Invoice number |
| DataWystawienia | Invoice issue date |
| DataSprzedazy | Supply date |
| TypDokumentu | Document type (FP, RO, WEW) |
| GTU_01 through GTU_13 | Goods/services type codes (see Step 6) |
| SW | Delivery of goods as mail order (Art. 23) |
| EE | Supply of telecommunications/electronic services (Art. 28k) |
| TP | Related party transaction (Art. 32 ust. 2 pkt 1) |
| TT_WNT | Intra-EU triangulation (WNT) |
| TT_D | Second-in-line supply in triangulation |
| MR_T | Margin scheme for tourism |
| MR_UZ | Margin scheme for second-hand goods |
| I_42 | Import procedure 42 |
| I_63 | Import procedure 63 |
| B_SPV | Transfer of single-purpose voucher |
| B_SPV_DOSTAWA | Supply against single-purpose voucher |
| B_MPV_PROWIZJA | Multi-purpose voucher services |
| MPP | Split payment mechanism applies |

Key attributes on purchase records:

| Attribute | Description |
|-----------|-------------|
| NrDostawcy | Supplier's NIP / tax ID |
| NazwaDostawcy | Supplier's name |
| DowodZakupu | Invoice / document number |
| DataZakupu | Purchase date |
| DataWplywu | Date invoice received |
| DokumentZakupu | Document type (MK, VAT_RR, WEW) |
| IMP | Import of goods |
| MPP | Split payment mechanism applies |

---

## Step 2: Transaction Classification Matrix [T1]

### 2a. Determine Transaction Type [T1]

**Legislation:** ustawa o VAT, Art. 5 ust. 1 (taxable activities), Art. 7 (supply of goods), Art. 8 (supply of services).

| Transaction | Classification | VAT Treatment |
|------------|---------------|---------------|
| Sale of goods/services | Output VAT (podatek nalezny) | Report in sales fields (P_10 through P_28) |
| Purchase of goods/services | Input VAT (podatek naliczony) | Report in purchase fields (P_40 through P_46) |
| Salaries / wages (wynagrodzenia) | OUT OF SCOPE | Never on VAT return |
| Social contributions (ZUS) | OUT OF SCOPE | Never on VAT return |
| Income tax payments (CIT/PIT) | OUT OF SCOPE | Never on VAT return |
| Loan repayments | OUT OF SCOPE | Never on VAT return |
| Dividend payments | OUT OF SCOPE | Never on VAT return |
| Bank charges (prowizje bankowe) | EXEMPT | No input VAT (Art. 43 ust. 1 pkt 38-41) |
| Insurance premiums | EXEMPT | No input VAT (Art. 43 ust. 1 pkt 37) |

### 2b. Counterparty Location Matrix [T1]

**Legislation:** ustawa o VAT, Art. 22-28 (place of supply rules).

| Counterparty Location | Code | Treatment (Sales) | Treatment (Purchases) |
|----------------------|------|-------------------|----------------------|
| Poland (PL) | DOMESTIC | Standard output VAT at applicable rate | Standard input VAT recovery (subject to blocks) |
| EU Member State | EU | WDT (goods, P_10) or B2B services (P_12) at 0% | WNT reverse charge (goods, P_21/P_22/P_40) or import of services RC (P_25/P_26/P_42) |
| Non-EU country | NON-EU | Export (goods, P_11) at 0% or B2B services (P_12) | Import of goods via customs (P_23/P_24/P_41) or import of services RC (P_25/P_26/P_42) |

EU Member States (post-Brexit): AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PT, RO, SK, SI, ES, SE.

**Note:** UK, CH, NO, US, and all others are Non-EU. **ustawa o VAT, Art. 2 pkt 2-4.**

### 2c. VAT Rate Determination Matrix [T1]

**Legislation:** ustawa o VAT, Art. 41.

Calculate from invoice amounts: `rate = vat_amount / net_amount * 100`

| Calculated Rate | Standard Rate | JPK_V7 Base Field | JPK_V7 Tax Field |
|----------------|---------------|-------------------|-----------------|
| 22-24% | **23%** | P_13 | P_14 |
| 7-9% | **8%** | P_15 | P_16 |
| 4-6% | **5%** | P_17 | P_18 |
| 0% (with right to deduct) | **0%** | P_19 | -- |
| 0% (exempt, no right to deduct) | **exempt** | P_20 | -- |

### 2d. Sales Classification Lookup Table [T1]

| Sale Type | Counterparty | B2B/B2C | Base Field | Tax Field | GTU Required? |
|-----------|-------------|---------|------------|-----------|--------------|
| Domestic goods/services 23% | PL | Any | P_13 | P_14 | Yes, if applicable |
| Domestic goods/services 8% | PL | Any | P_15 | P_16 | Yes, if applicable |
| Domestic goods/services 5% | PL | Any | P_17 | P_18 | Yes, if applicable |
| Domestic goods/services 0% | PL | Any | P_19 | -- | Yes, if applicable |
| Exempt supply | PL | Any | P_20 | -- | No |
| Intra-EU supply of goods (WDT) | EU | B2B | P_10 | -- | No |
| Export of goods | NON-EU | Any | P_11 | -- | No |
| B2B services (place of supply = buyer) | EU/NON-EU | B2B | P_12 | -- | Yes, if applicable |

### 2e. Purchase Classification Lookup Table [T1]

| Purchase Type | Supplier Location | Input VAT Field | Also Creates Output? | Output Base | Output Tax |
|--------------|------------------|----------------|---------------------|-------------|-----------|
| Domestic purchase (general) | PL | P_43 | No | -- | -- |
| Domestic purchase (fixed asset) | PL | P_45 | No | -- | -- |
| Intra-EU acquisition of goods (WNT) | EU | P_40 | Yes (RC) | P_21 | P_22 |
| Import of services (Art. 28b) | EU or NON-EU | P_42 | Yes (RC) | P_25 | P_26 |
| Import of goods (customs / Art. 33a) | NON-EU | P_41 | Yes (if Art. 33a) | P_23 | P_24 |
| Domestic reverse charge (Art. 17(1) pkt 7-8) | PL (non-established supplier) | P_44 | Yes (RC) | P_27 | P_28 |

### 2f. Expense Category Matrix [T1]

**Legislation:** ustawa o VAT, Art. 91 (adjustment periods for capital goods).

| Category | Criteria | Input VAT Field | Adjustment Period |
|----------|---------|----------------|------------------|
| Fixed assets (srodki trwale) | Net value > PLN 15,000 | P_45 | 5 years (movable), 10 years (immovable) |
| Fixed assets (srodki trwale) | Net value <= PLN 15,000 | P_43 | No multi-year adjustment |
| Goods for resale (towary handlowe) | Goods bought to resell | P_43 | None |
| Overhead / services | Everything else | P_43 | None |

---

## Step 3: VAT Rates -- Detailed Breakdown

### 3a. Standard Rate: 23% [T1]

**Legislation:** ustawa o VAT, Art. 41 ust. 1.

Applies to all supplies of goods and services not covered by a reduced rate, zero rate, or exemption.

| Supply Category | Rate | Legislation |
|----------------|------|-------------|
| General merchandise | 23% | Art. 41 ust. 1 |
| Professional services (legal, consulting, accounting) | 23% | Art. 41 ust. 1 |
| Electronics and IT equipment | 23% | Art. 41 ust. 1 |
| Motor vehicles and parts | 23% | Art. 41 ust. 1 |
| Furniture and household goods | 23% | Art. 41 ust. 1 |
| Clothing and footwear | 23% | Art. 41 ust. 1 |
| Telecommunications services | 23% | Art. 41 ust. 1 |
| Construction materials | 23% | Art. 41 ust. 1 |
| Restaurant and catering services (alcohol portion) | 23% | Art. 41 ust. 1 |
| Commercial property rental | 23% | Art. 41 ust. 1 |
| Advertising and marketing services | 23% | Art. 41 ust. 1 |

### 3b. Reduced Rate: 8% [T1]

**Legislation:** ustawa o VAT, Art. 41 ust. 2; Annex 3 to ustawa o VAT.

| Supply Category | Rate | Legislation |
|----------------|------|-------------|
| Construction and renovation of residential buildings (budownictwo objete spolecznym programem mieszkaniowym) | 8% | Art. 41 ust. 12-12c |
| Certain foodstuffs (processed foods, spices, tea, coffee) | 8% | Art. 41 ust. 2, Annex 3 |
| Passenger transport services (bus, train, taxi) | 8% | Art. 41 ust. 2, Annex 3 poz. 155-163 |
| Restaurant and catering services (excluding alcohol) | 8% | Art. 41 ust. 2, Annex 3 poz. 56 |
| Hotel and accommodation services | 8% | Art. 41 ust. 2, Annex 3 poz. 163 |
| Pharmaceutical products and medical devices | 8% | Art. 41 ust. 2, Annex 3 poz. 82-93 |
| Sanitary and hygiene products | 8% | Art. 41 ust. 2, Annex 3 |
| Cut flowers and plants | 8% | Art. 41 ust. 2, Annex 3 |
| Firewood | 8% | Art. 41 ust. 2, Annex 3 |
| Cleaning services for residential buildings | 8% | Art. 41 ust. 2, Annex 3 |

### 3c. Reduced Rate: 5% [T1]

**Legislation:** ustawa o VAT, Art. 41 ust. 2a; Annex 10 to ustawa o VAT.

| Supply Category | Rate | Legislation |
|----------------|------|-------------|
| Basic foodstuffs -- bread and bakery products | 5% | Art. 41 ust. 2a, Annex 10 |
| Basic foodstuffs -- dairy products (milk, cheese, butter, yogurt) | 5% | Art. 41 ust. 2a, Annex 10 |
| Basic foodstuffs -- meat and meat products | 5% | Art. 41 ust. 2a, Annex 10 |
| Basic foodstuffs -- fish and seafood | 5% | Art. 41 ust. 2a, Annex 10 |
| Basic foodstuffs -- fruit and vegetables (fresh and frozen) | 5% | Art. 41 ust. 2a, Annex 10 |
| Basic foodstuffs -- cereals, flour, groats | 5% | Art. 41 ust. 2a, Annex 10 |
| Basic foodstuffs -- oils and fats (olive oil, sunflower oil) | 5% | Art. 41 ust. 2a, Annex 10 |
| Basic foodstuffs -- sugar | 5% | Art. 41 ust. 2a, Annex 10 |
| Books and e-books (printed and electronic) | 5% | Art. 41 ust. 2a, Annex 10 |
| Periodicals (newspapers, magazines -- printed and electronic) | 5% | Art. 41 ust. 2a, Annex 10 |
| Musical scores | 5% | Art. 41 ust. 2a, Annex 10 |

### 3d. Zero Rate: 0% (With Right to Deduct Input VAT) [T1]

**Legislation:** ustawa o VAT, Art. 41 ust. 3-3e; Art. 42; Art. 83.

| Supply Category | Rate | Conditions | Legislation |
|----------------|------|-----------|-------------|
| Export of goods | 0% | Goods physically leave EU; customs export declaration (IE599) | Art. 41 ust. 4-9 |
| Intra-EU supply of goods (WDT) | 0% | Buyer has valid EU VAT number; goods transported to another MS; WDT conditions met | Art. 42 |
| International transport of goods | 0% | Transport crosses EU border | Art. 83 ust. 1 pkt 23 |
| International transport of passengers | 0% | Cross-border routes | Art. 83 ust. 1 pkt 23 |
| Services directly connected with exported goods | 0% | Related to export transaction | Art. 83 ust. 1 pkt 21 |
| Supply of goods for ships in international traffic | 0% | Maritime supplies | Art. 83 ust. 1 pkt 1-3 |
| Supply of goods for aircraft in international traffic | 0% | Aviation supplies | Art. 83 ust. 1 pkt 5-6 |

### 3e. Exempt Supplies (Without Right to Deduct) [T1]

**Legislation:** ustawa o VAT, Art. 43.

| Supply Category | Legislation |
|----------------|-------------|
| Financial services (banking, lending, credit) | Art. 43 ust. 1 pkt 38-41 |
| Insurance and reinsurance services | Art. 43 ust. 1 pkt 37 |
| Healthcare and medical services | Art. 43 ust. 1 pkt 18-19a |
| Education and training (accredited institutions) | Art. 43 ust. 1 pkt 26-29 |
| Residential property rental (for housing purposes) | Art. 43 ust. 1 pkt 36 |
| Postal services (universal service provider) | Art. 43 ust. 1 pkt 17 |
| Gambling and lottery services | Art. 43 ust. 1 pkt 15 |
| Cultural services (museums, libraries, public cultural institutions) | Art. 43 ust. 1 pkt 33 |
| Social welfare services | Art. 43 ust. 1 pkt 22-24 |
| Supply of buildings/land (after first occupation, unless option to tax exercised) | Art. 43 ust. 1 pkt 10-10a |

---

## Step 4: Blocked Input Tax (Non-Deductible Input VAT) [T1]

### 4a. Blocked Categories -- Full Block [T1]

**Legislation:** ustawa o VAT, Art. 88.

| Blocked Category | VAT Recovery | Legislation | Notes |
|-----------------|-------------|-------------|-------|
| Accommodation services (uslugi noclegowe) | **0% recovery** | Art. 88 ust. 1 pkt 4 lit. c | Exception: purchased for resale (e.g., travel agent) |
| Catering services (uslugi gastronomiczne) | **0% recovery** | Art. 88 ust. 1 pkt 4 lit. b | Exception: catering for employees on business premises [T2] |
| Purchases not related to taxable activity | **0% recovery** | Art. 88 ust. 1 pkt 1-2 (via Art. 86 ust. 1) | Private use, non-business purpose |
| Invoices from non-existent entities / fictitious invoices | **0% recovery** | Art. 88 ust. 3a pkt 1 | "Puste faktury" -- empty invoices |
| Invoices documenting activities that did not occur | **0% recovery** | Art. 88 ust. 3a pkt 4 | Fraud prevention |
| Invoices with incorrect amounts | **0% recovery** (on excess) | Art. 88 ust. 3a pkt 4 | Only the incorrect excess is blocked |

### 4b. Motor Vehicles -- 50% Limitation [T1]

**Legislation:** ustawa o VAT, Art. 86a; EU Council Implementing Decision 2019/2138 (extending Poland's derogation).

This is a critical Poland-specific rule. The 50% limitation applies to ALL costs related to passenger vehicles used for mixed (business + private) purposes.

| Expense Type | Mixed Use (Default) | 100% Business Use (Declared) | Legislation |
|-------------|--------------------|-----------------------------|-------------|
| Purchase of passenger vehicle | **50% VAT deduction** | 100% VAT deduction | Art. 86a ust. 1 pkt 1 |
| Lease / rental of passenger vehicle | **50% VAT deduction** | 100% VAT deduction | Art. 86a ust. 1 pkt 2 |
| Fuel (petrol, diesel, LPG, electricity for EV) | **50% VAT deduction** | 100% VAT deduction | Art. 86a ust. 1 pkt 3, Art. 86a ust. 2 pkt 3 |
| Repairs and maintenance | **50% VAT deduction** | 100% VAT deduction | Art. 86a ust. 1 pkt 2 |
| Parking | **50% VAT deduction** | 100% VAT deduction | Art. 86a ust. 1 pkt 2 |
| Car wash | **50% VAT deduction** | 100% VAT deduction | Art. 86a ust. 1 pkt 2 |
| Motorway tolls | **50% VAT deduction** | 100% VAT deduction | Art. 86a ust. 1 pkt 2 |
| Insurance (if VAT-bearing, rare) | **50% VAT deduction** | 100% VAT deduction | Art. 86a ust. 1 pkt 2 |

**To claim 100% deduction (full business use), ALL of these conditions must be met:**
1. Vehicle must be used EXCLUSIVELY for business activity (Art. 86a ust. 4 pkt 1)
2. Entity must maintain a vehicle usage log (ewidencja przebiegu pojazdu) with GPS tracking (Art. 86a ust. 4 pkt 1, ust. 6-7)
3. Entity must file form **VAT-26** with the tax office within 25 days of incurring the first expense (Art. 86a ust. 12)
4. Entity must establish internal vehicle usage rules (regulamin) (Art. 86a ust. 4 pkt 1)
5. The log must include: date, starting mileage, ending mileage, route description, purpose of trip, driver identity (Art. 86a ust. 7)

**Vehicles exempt from the 50% limitation (always 100%):** [T1]
- Vehicles with gross vehicle weight > 3.5 tonnes (Art. 86a ust. 3 pkt 1 lit. a)
- Vehicles with N1 homologation (cargo van) meeting technical criteria (Art. 86a ust. 3 pkt 1 lit. b, with confirmation from okregowa stacja kontroli pojazdow)
- Vehicles constructed for special purposes (Art. 86a ust. 3 pkt 1 lit. c): cranes, concrete mixers, etc.

**If 100% business use is claimed, [T2] flag for reviewer to verify GPS log, VAT-26 filing, and compliance with all conditions.**

### 4c. Entertainment and Representation [T1]

**Legislation:** ustawa o VAT, Art. 86 ust. 1 (general deduction right), Art. 88 (blocks).

**Important Poland-specific distinction:** Unlike Malta, Poland does NOT have a general VAT block on entertainment/representation expenses. Input VAT on business entertainment IS deductible for VAT purposes, provided the expense is connected to taxable business activity (Art. 86 ust. 1).

| Expense | VAT Deductible? | Note |
|---------|-----------------|------|
| Business dinner with client | **YES** (100%) | Connected to business activity. CIT deductibility limited to 70% -- but this is income tax, not VAT. |
| Team building event | **YES** (100%) | Business overhead. |
| Conference / seminar | **YES** (100%) | Business overhead. |
| Gifts to clients > PLN 100 net | **YES** (100%) for VAT, BUT output VAT due on free-of-charge supply | Art. 7 ust. 2 -- deemed supply if input VAT was deducted. If gift <= PLN 100 net, no deemed supply (Art. 7 ust. 3-4). |

### 4d. Partial Exemption (Proporcja / Prewspolczynnik) [T2]

**Legislation:** ustawa o VAT, Art. 90 (proporcja), Art. 86 ust. 2a-2h (prewspolczynnik).

If the business makes BOTH taxable and exempt supplies:

**Proporcja (Art. 90):**
```
Recovery % = (Taxable Supplies / (Taxable Supplies + Exempt Supplies)) * 100
```
- Rounded up to nearest whole percent (Art. 90 ust. 4)
- If ratio >= 98%, treat as 100% (Art. 90 ust. 10 pkt 1)
- If ratio <= 2%, treat as 0% (Art. 90 ust. 10 pkt 2)
- Preliminary ratio based on prior year; annual adjustment required (Art. 91)

**Prewspolczynnik (Art. 86 ust. 2a):**
Applies when goods/services are used for BOTH business activity AND non-business activity (e.g., municipalities, public institutions). This is a pre-proportional allocation BEFORE proporcja.

**Flag for reviewer: both proporcja and prewspolczynnik calculations must be confirmed by doradca podatkowy before filing. Annual adjustment is mandatory under Art. 91.**

---

## Step 5: Registration Rules [T1]

### 5a. Mandatory Registration

**Legislation:** ustawa o VAT, Art. 113.

| Rule | Threshold | Legislation |
|------|----------|-------------|
| **Small business exemption threshold (zwolnienie podmiotowe)** | PLN 200,000 annual turnover (applicable through 2025) | Art. 113 ust. 1 |
| **Increased threshold (from 2026)** | PLN 240,000 annual turnover | Art. 113 ust. 1 (as amended) |
| **Mid-year breach** | Registration mandatory from the transaction that caused the breach | Art. 113 ust. 5 |
| **Certain activities -- no exemption available** | Must register regardless of turnover | Art. 113 ust. 13 |

Activities that CANNOT use the small business exemption (Art. 113 ust. 13):
- Legal services (Art. 113 ust. 13 pkt 2 lit. a)
- Consulting / advisory services (Art. 113 ust. 13 pkt 2 lit. b)
- Jewellery trade (Art. 113 ust. 13 pkt 1 lit. d)
- Debt collection and factoring (Art. 113 ust. 13 pkt 1 lit. f)
- Supply of new means of transport (Art. 113 ust. 13 pkt 1 lit. b)
- Supply of buildings/land (unless exempt) (Art. 113 ust. 13 pkt 1 lit. c)
- Distance selling from Poland (Art. 113 ust. 13 pkt 1 lit. a)
- Electronic services to EU consumers (Art. 113 ust. 13 pkt 1 lit. e-f)

### 5b. NIP Format [T1]

| Context | Format | Example |
|---------|--------|---------|
| Domestic | 10 digits (XXX-XXX-XX-XX or XXXXXXXXXX) | 123-456-78-90 |
| EU VIES | PL + 10 digits | PL1234567890 |

**ustawa o VAT, Art. 96 ust. 4 -- registration certificate issued by naczelnik urzadu skarbowego.**

### 5c. VAT-Exempt Entities [T1]

**Legislation:** ustawa o VAT, Art. 113.

- Entities below the threshold may opt for exemption (zwolnienie podmiotowe)
- They CANNOT recover input VAT (Art. 86 ust. 1 -- no right to deduct without taxable supplies)
- They must issue invoices marked "zwolniony" or "zw" (exempt)
- If threshold is exceeded mid-year, entity becomes VAT-liable from the overshooting transaction
- Voluntary registration is possible at any time (Art. 113 ust. 4)

---

## Step 6: Filing Deadlines and Penalties

### 6a. Filing Deadlines [T1]

**Legislation:** ustawa o VAT, Art. 99, Art. 103.

| Filing Obligation | Period | Deadline | Legislation |
|-------------------|--------|----------|-------------|
| JPK_V7M (monthly filer) | Monthly | **25th of the month following the reporting month** | Art. 99 ust. 1 |
| JPK_V7K -- Ewidencja only (months 1-2 of quarter) | Monthly | **25th of the month following the reporting month** | Art. 99 ust. 3 |
| JPK_V7K -- Deklaracja + Ewidencja (month 3 of quarter) | Quarterly | **25th of the month following the quarter end** | Art. 99 ust. 3 |
| VAT payment (monthly) | Monthly | **25th of the month following the reporting month** | Art. 103 ust. 1 |
| VAT payment (quarterly) | Quarterly | **25th of the month following the quarter end** | Art. 103 ust. 2 |
| EU summary statement (VAT-UE / informacja podsumowujaca) | Monthly | **25th of the month following the reporting month** | Art. 100 ust. 3 |
| Intrastat declarations | Monthly | **10th of the month following the reporting month** | Separate legislation |
| VAT refund -- standard | -- | **60 days from filing** | Art. 87 ust. 2 |
| VAT refund -- accelerated | -- | **25 days from filing** (conditions apply) | Art. 87 ust. 6 |
| VAT refund -- to VAT account | -- | **25 days from filing** | Art. 87 ust. 6a |
| VAT refund -- 40-day | -- | **40 days from filing** (electronic invoices via KSeF) | Art. 87 ust. 2 |

**If the 25th falls on a weekend or public holiday, the deadline moves to the next business day (Ordynacja podatkowa, Art. 12 par. 5).**

### 6b. KSeF E-Invoicing [T1]

**Legislation:** ustawa o VAT, Art. 106na-106ne (KSeF provisions).

| Milestone | Date | Scope |
|-----------|------|-------|
| KSeF mandatory -- large taxpayers (turnover > PLN 200 million) | **1 February 2026** | All domestic B2B invoices must be issued via KSeF |
| KSeF mandatory -- all other VAT taxpayers | **1 April 2026** | All domestic B2B invoices must be issued via KSeF |
| KSeF invoice number in JPK_V7 | **From mandatory date** | KSeF reference number must be included in Ewidencja records |

### 6c. Penalties (Kodeks Karny Skarbowy -- KKS) [T1]

**Legislation:** Kodeks karny skarbowy (KKS); ustawa o VAT, Art. 112b.

| Offence | Penalty | Legislation |
|---------|---------|-------------|
| Late filing of JPK_V7 | Fine (kara grzywny) up to 720 stawek dziennych; for minor offences (wykroczenie skarbowe), fine up to PLN 67,200 (2026) | KKS Art. 56 par. 1-4 |
| Non-filing of JPK_V7 | Fine (kara grzywny) up to 720 stawek dziennych or imprisonment up to 2 years | KKS Art. 54 par. 1 |
| Late payment of VAT | Statutory interest (odsetki za zwloke) -- rate set by Minister of Finance (currently ~14.5% p.a.) | Ordynacja podatkowa, Art. 53-56 |
| Incorrect JPK_V7 (understatement of tax or overstatement of credit) | 30% surcharge on the amount of understated tax or overstated credit (sankcja VAT) | Art. 112b ust. 1 |
| Incorrect JPK_V7 (related to fraud / fictitious invoices) | 100% surcharge | Art. 112b ust. 2 |
| Failure to use mandatory split payment | 30% surcharge on the VAT amount not paid via MPP | Art. 108a ust. 7 (via Art. 112b) |
| Failure to mark invoice with "mechanizm podzielonej platnosci" | Penalty up to 30% of VAT on the invoice | Art. 106e ust. 1 pkt 18a, Art. 112b |
| Failure to verify white list before payment > PLN 15,000 | Joint and several liability for supplier's VAT debt; CIT non-deductibility of expense | Art. 117ba Ordynacja podatkowa |
| Errors in JPK_V7 not corrected within 14 days of notification | Fine (kara grzywny) | KKS Art. 80 |

### 6d. Voluntary Correction (Czynny Zal) [T2]

**Legislation:** KKS, Art. 16.

A taxpayer who files a corrected JPK_V7 BEFORE the tax authority initiates proceedings and pays the outstanding tax with interest is not subject to fiscal penalties. This is known as "czynny zal" (active remorse). Flag for reviewer to confirm conditions are met.

---

## Step 7: Reverse Charge Mechanics

### 7a. B2B Services from Abroad (Art. 28b) [T1]

**Legislation:** ustawa o VAT, Art. 17 ust. 1 pkt 4; Art. 28b.

When a Polish VAT payer receives services from a supplier not established in Poland (EU or non-EU), and the place of supply is Poland under Art. 28b (B2B general rule):

1. Report net amount in **P_25** (taxable base for import of services)
2. Self-assess output VAT at the applicable Polish rate in **P_26**
3. Claim input VAT in **P_42** (if entitled to deduction)
4. Net effect: **zero** for fully taxable businesses

### 7b. Intra-EU Acquisitions of Goods (WNT) [T1]

**Legislation:** ustawa o VAT, Art. 9 ust. 1; Art. 17 ust. 1 pkt 3; Art. 20 ust. 5.

When a Polish VAT payer acquires goods from another EU Member State:

1. Report net amount in **P_21** (taxable base for WNT)
2. Self-assess output VAT at the applicable Polish rate in **P_22**
3. Claim input VAT in **P_40**
4. Net effect: **zero** for fully taxable businesses
5. Also report on **VAT-UE** (EU summary statement)

**Late reporting rule (Art. 86 ust. 10b pkt 2):** If the WNT is not reported within 3 months of the tax obligation arising, the taxpayer must reduce input VAT in P_40 (output VAT in P_22 remains). Input VAT can be reclaimed once the WNT is properly reported.

### 7c. Import of Goods from Non-EU [T1]

**Legislation:** ustawa o VAT, Art. 33; Art. 33a.

Two procedures:

| Procedure | Treatment | JPK_V7 Fields |
|-----------|----------|---------------|
| **Standard import** (VAT paid to customs) | VAT paid on customs document (SAD/C88). Input VAT claimed in JPK_V7. | P_41 only (input VAT from customs document) |
| **Simplified import (Art. 33a)** | Self-assessment in JPK_V7 (no payment to customs). Requires AEO status or customs guarantee. | P_23 (base) / P_24 (output VAT) / P_41 (input VAT) |

### 7d. Domestic Reverse Charge (Art. 17 ust. 1 pkt 7-8) [T1]

**Legislation:** ustawa o VAT, Art. 17 ust. 1 pkt 7-8.

Applies when the supplier is **not established in Poland** but supplies goods/services in Poland (and the buyer is a Polish VAT payer):

1. Report net amount in **P_27**
2. Self-assess output VAT in **P_28**
3. Claim input VAT in **P_44**
4. Net effect: **zero** for fully taxable businesses

**Important note:** The previous domestic reverse charge for construction services (Art. 17 ust. 1 pkt 8 -- Annex 14) was **largely replaced by the mandatory split payment mechanism (MPP) from 1 November 2019**. Domestic transactions between Polish-established entities no longer use reverse charge; instead, MPP applies for Annex 15 goods/services.

### 7e. Exceptions to Reverse Charge [T1]

| Situation | Treatment | Reason |
|-----------|----------|--------|
| Out-of-scope items (wages, dividends, loan repayments) | NEVER reverse charge | Not a supply of goods/services |
| Local consumption abroad (hotel/restaurant/taxi in another country) | NOT reverse charge | VAT charged and paid at source in the other country; irrecoverable foreign VAT |
| EU supplier charged their local VAT > 0% | NOT reverse charge | Supplier applied their domestic VAT; this is not a Polish transaction |
| B2C services where place of supply is abroad | NOT reverse charge | Not a Polish supply |

---

## Step 8: Split Payment Mechanism (Mechanizm Podzielonej Platnosci / MPP)

### 8a. Overview [T1]

**Legislation:** ustawa o VAT, Art. 108a-108d; Annex 15 to ustawa o VAT.

The split payment mechanism (MPP) is Poland's primary anti-fraud tool for high-risk goods and services. It **replaced the previous domestic reverse charge** for construction and certain other services from 1 November 2019.

### 8b. Mandatory MPP Conditions [T1]

MPP is **mandatory** when ALL three conditions are simultaneously met:

| Condition | Threshold | Legislation |
|-----------|----------|-------------|
| 1. Transaction is B2B (between VAT payers) | Both parties are active VAT payers | Art. 108a ust. 1a |
| 2. Invoice gross amount exceeds PLN 15,000 | Single invoice, gross (with VAT) | Art. 108a ust. 1a pkt 1 |
| 3. Invoice includes at least ONE item from Annex 15 | See Annex 15 categories below | Art. 108a ust. 1a pkt 2 |

**All three must be TRUE simultaneously. If any one is FALSE, MPP is voluntary (but still permitted).**

### 8c. Annex 15 Categories (Key Items) [T1]

**Legislation:** ustawa o VAT, Annex 15 (Zalacznik nr 15).

| Category | Examples | Annex 15 Reference |
|----------|---------|-------------------|
| Steel and iron products | Bars, rods, pipes, sheets, wire | Poz. 1-27 |
| Non-ferrous metals | Copper, aluminium, zinc, lead products | Poz. 28-33 |
| Waste and scrap | Ferrous and non-ferrous scrap, waste paper, waste glass | Poz. 34-36 |
| Fuels | Petrol, diesel, heating oil, LPG, natural gas | Poz. 37-42 |
| Plastics | Plastic raw materials and semi-finished products | Poz. 43-46 |
| Electronics | Processors, hard drives, smartphones, tablets, laptops, game consoles, TV sets | Poz. 47-62 |
| Motor vehicle parts | Car parts, engine components, accessories | Poz. 63-68 |
| Precious metals | Gold, silver, platinum (in unwrought form) | Poz. 69-72 |
| Coal and coke | Hard coal, lignite, coke | Poz. 73-77 |
| Construction services | General construction, specialised construction trades (subcontractor or general contractor) | Poz. 78-95 |
| Cleaning and security services | Building cleaning, guard/protection services | Poz. 96-100 |
| Personnel outsourcing | Temporary staffing, labour hire | Poz. 101-106 |
| IT services | Hardware maintenance, software licensing (selected) | Poz. 107-115 |
| Emission allowances | CO2 emission permits | Poz. 116-120 |

### 8d. How Split Payment Works [T1]

**Legislation:** ustawa o VAT, Art. 108a ust. 2.

1. Buyer initiates a **split payment message** through their bank
2. Bank splits the payment automatically:
   - **Net amount** goes to seller's current account (rachunek biezacy)
   - **VAT amount** goes to seller's dedicated VAT account (rachunek VAT)
3. Seller's **VAT account** has restricted use:
   - Pay VAT to the tax office
   - Pay VAT portion of purchase invoices (to another entity's VAT account)
   - Transfer between own VAT accounts
   - Pay ZUS social contributions (from 1 November 2019)
   - Pay income tax (CIT/PIT) (from 1 November 2019)
   - Release funds to current account with tax office approval (Art. 108b)

### 8e. Invoice Annotation [T1]

**Legislation:** ustawa o VAT, Art. 106e ust. 1 pkt 18a.

When mandatory MPP applies, the invoice **MUST** bear the annotation:

**"mechanizm podzielonej platnosci"**

This annotation must appear on the invoice. Failure to include it triggers penalties under Art. 106e ust. 12-13.

### 8f. MPP Consequences of Non-Compliance [T1]

| Party | Violation | Consequence | Legislation |
|-------|----------|-------------|-------------|
| Buyer | Fails to use MPP when mandatory | 30% surcharge on VAT amount not paid via MPP | Art. 108a ust. 7 |
| Seller | Fails to annotate invoice with "mechanizm podzielonej platnosci" | 30% surcharge on VAT amount on the invoice | Art. 106e ust. 12 |
| Buyer | Uses MPP voluntarily (even when not mandatory) | Benefit: protection from joint liability for supplier's VAT; protection from 30% sanction; reduced interest rate on late VAT payment | Art. 108a ust. 5-6 |

---

## Step 9: White List Verification (Biala Lista Podatnikow VAT) [T1]

### 9a. Overview [T1]

**Legislation:** ustawa o VAT, Art. 96b; Ordynacja podatkowa, Art. 117ba.

The "biala lista" (white list) is the electronic register of VAT taxpayers maintained by the head of KAS. It includes registered bank accounts of VAT payers.

### 9b. Verification Obligation [T1]

| Rule | Threshold | Legislation |
|------|----------|-------------|
| Before making any B2B payment exceeding PLN 15,000, the buyer MUST verify that the seller's bank account is on the white list | PLN 15,000 gross | Art. 96b, Art. 117ba Ordynacja podatkowa |
| If payment is made to an account NOT on the white list | Buyer has joint and several liability for seller's VAT + CIT non-deductibility of the expense | Art. 117ba par. 1 |
| Safe harbour: notify tax office within 7 days | Buyer can avoid liability by reporting the payment to the wrong account within 7 days (ZAW-NR form) | Art. 117ba par. 3 |

### 9c. White List Lookup [T1]

The white list can be checked at: https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka

Verify by NIP, REGON, or bank account number. The result confirms:
- Whether the entity is registered as an active VAT payer
- Whether the entity has been removed from the register
- The entity's registered bank accounts

---

## Step 10: GTU Codes (Goods/Services Type Codes) [T1]

### 10a. Overview [T1]

**Legislation:** Rozporzadzenie Ministra Finansow, Inwestycji i Rozwoju z dnia 15 pazdziernika 2019 r. (as amended); JPK_V7 schema.

Sales records in the Ewidencja section of JPK_V7 must include GTU codes when the supply involves certain categories of goods or services. GTU codes are **mandatory markers** -- omission is a reporting error subject to penalties.

### 10b. GTU Code Lookup Table [T1]

| GTU Code | Category | Key Items / Examples | ustawa o VAT / PKWiU Reference |
|----------|----------|---------------------|-------------------------------|
| **GTU_01** | Alcohol | Alcoholic beverages -- beer, wine, spirits, ethyl alcohol | CN 2203-2208 |
| **GTU_02** | Fuel and lubricants | Petrol, diesel, aviation fuel, lubricating oils | CN 2710, 2711 |
| **GTU_03** | Heating oil | Heating oil not qualifying as fuel | CN 2710 19 |
| **GTU_04** | Tobacco | Cigarettes, cigars, smoking tobacco, e-liquids | CN 2401-2403 |
| **GTU_05** | Waste and scrap | Ferrous/non-ferrous scrap, waste paper, waste glass, rubber waste | PKWiU 38.11, 38.32 |
| **GTU_06** | Electronic devices | Processors, smartphones, tablets, laptops, game consoles, cameras, monitors, printers | CN 8471, 8517, 8528 |
| **GTU_07** | Vehicles and parts | Motor vehicles, trailers, car parts, motorcycles | CN 8701-8711 |
| **GTU_08** | Precious metals and gemstones | Gold, silver, platinum (unwrought); diamonds, rubies, sapphires | CN 7106-7112, 7102 |
| **GTU_09** | Medicines and medical devices | Pharmaceutical products, medical devices, surgical instruments | CN 3001-3006 |
| **GTU_10** | Buildings and land | Supply of buildings, structures, land (developed and undeveloped) | PKWiU 41-43 |
| **GTU_11** | Emission allowances | Greenhouse gas emission permits (CO2) | ustawa o VAT Art. 8 ust. 2 pkt 1 (in connection with EU ETS) |
| **GTU_12** | Intangible services | Consulting, advisory, legal, accounting, auditing, management, marketing, IT, training, HR, engineering, scientific research services | PKWiU 62-74 (selected) |
| **GTU_13** | Transport and warehouse management | Freight transport, warehousing, courier services | PKWiU 49-53 (selected) |

### 10c. GTU Application Rules [T1]

| Rule | Detail |
|------|--------|
| GTU codes apply to **sales records only** | Purchase records do not require GTU codes |
| Multiple GTU codes can apply to one invoice | If an invoice covers both electronics and transport, mark both GTU_06 and GTU_13 |
| GTU codes do NOT apply to: | Simplified invoices (faktura uproszczona), internal documents (WEW), cash register receipts (RO) -- unless they are "recognized" as invoices |
| GTU_12 is the most common and most frequently missed | ANY consulting, legal, accounting, IT, marketing, management, training, or HR service triggers GTU_12 |
| Omission of required GTU code | Tax office will send a demand to correct within 14 days; failure = fine under KKS Art. 80 |

---

## Step 11: Edge Case Registry

### EC1 -- Hotel in another EU country [T1]
**Situation:** Polish VAT payer pays for hotel in Germany. Invoice shows German 19% VAT.
**Resolution:** NOT reverse charge. German VAT was charged and paid at source. No Polish VAT entries. German VAT is an irrecoverable cost embedded in the expense. No P_ fields affected.
**Legislation:** ustawa o VAT, Art. 28e (place of supply for immovable property services is where the property is located -- Germany).

### EC2 -- SaaS subscription from US provider (e.g., AWS, Google, Notion) [T1]
**Situation:** Monthly charge from US company, no VAT on invoice. Polish VAT payer.
**Resolution:** Import of services under Art. 28b. Report in P_25 (base) / P_26 (output VAT at 23%) / P_42 (input VAT at 23%). Net VAT effect: zero for fully taxable entity. Mark as GTU_12 if service is consulting/IT-related (on purchase side, GTU not applicable -- on sales side of the US entity, not relevant in Poland).
**Legislation:** ustawa o VAT, Art. 17 ust. 1 pkt 4, Art. 28b.

### EC3 -- Intra-EU goods acquisition from Italy [T1]
**Situation:** Polish company buys goods from Italian supplier. Invoice at 0% with IT VAT number (intra-EU supply).
**Resolution:** WNT -- intra-EU acquisition. Report in P_21 (base) / P_22 (output VAT at 23%) / P_40 (input VAT at 23%). Net effect: zero. Also report on VAT-UE. If goods are Annex 15 items and value > PLN 15,000, MPP applies on payment.
**Legislation:** ustawa o VAT, Art. 9 ust. 1, Art. 20 ust. 5.

### EC4 -- Passenger car purchase, mixed use (no GPS log) [T1]
**Situation:** Company buys a car for PLN 120,000 net + PLN 27,600 VAT (23%). Car used for business and private. No GPS log maintained. No VAT-26 filed.
**Resolution:** 50% VAT deduction. Input VAT recoverable = PLN 13,800. Report PLN 13,800 in P_43 (and P_45 if treated as fixed asset). Remaining PLN 13,800 is non-deductible cost (becomes part of the asset's tax base for CIT depreciation).
**Legislation:** ustawa o VAT, Art. 86a ust. 1-2.

### EC5 -- Invoice exceeds PLN 15,000 with Annex 15 goods -- mandatory MPP [T1]
**Situation:** Polish supplier invoices PLN 25,000 gross for steel products (Annex 15, poz. 1-27). Both parties are active VAT payers.
**Resolution:** Mandatory split payment. Buyer MUST pay via MPP. Invoice MUST bear annotation "mechanizm podzielonej platnosci". Failure by buyer = 30% surcharge on VAT. Normal VAT reporting: input VAT in P_43. Mark MPP = "1" in purchase record.
**Legislation:** ustawa o VAT, Art. 108a ust. 1a, Art. 106e ust. 1 pkt 18a.

### EC6 -- Credit note received (faktura korygujaca) [T1]
**Situation:** Supplier issues credit note reducing an earlier invoice. The credit note relates to a price reduction.
**Resolution:** Buyer reduces input VAT in the period the credit note is received (or when the conditions for correction are met -- for the supplier, confirmation of receipt is required under Art. 29a ust. 13). Reduce the original P_ field values accordingly. If the original was in P_43, reduce P_43 by the VAT on the credit note.
**Legislation:** ustawa o VAT, Art. 29a ust. 13-16 (supplier side), Art. 86 ust. 19a (buyer side).

### EC7 -- EU B2B service sale (consulting to German client) [T1]
**Situation:** Polish company provides IT consulting to a German business (B2B). German client has valid DE VAT number.
**Resolution:** Place of supply is Germany (Art. 28b). Report net amount in P_12. No output VAT charged. Customer self-assesses in Germany. Include in VAT-UE (informacja podsumowujaca). Mark GTU_12 on sales record (intangible services -- consulting/IT).
**Legislation:** ustawa o VAT, Art. 28b, Art. 100 ust. 1 pkt 4.

### EC8 -- Import of physical goods from China (standard customs procedure) [T2]
**Situation:** Client imports goods from China. VAT assessed by customs on SAD/C88 document.
**Resolution:** Import VAT paid at customs. Report input VAT in P_41 (from customs document). If using simplified procedure (Art. 33a), also report in P_23 (base) / P_24 (output VAT). Flag for reviewer: confirm customs documentation, confirm AEO status if Art. 33a claimed.
**Legislation:** ustawa o VAT, Art. 33, Art. 33a.

### EC9 -- Business entertainment dinner with clients [T1]
**Situation:** Polish company pays for business dinner with clients at a Polish restaurant. Invoice shows PLN 1,000 net + PLN 80 VAT (8% restaurant rate).
**Resolution:** Input VAT IS deductible in Poland (unlike Malta where entertainment is blocked). Report PLN 80 in P_43. Note: for CIT purposes, representation costs may be limited to 70% deductibility -- but this is NOT a VAT issue. Full VAT recovery for VAT purposes.
**Legislation:** ustawa o VAT, Art. 86 ust. 1 (general deduction right). No block in Art. 88 for entertainment.

### EC10 -- Fuel for mixed-use passenger car [T1]
**Situation:** Employee fills up company car used for business and private. Fuel invoice: PLN 500 net + PLN 115 VAT (23%).
**Resolution:** 50% input VAT deduction. Recoverable VAT = PLN 57.50. Report PLN 57.50 in P_43. The 50% rule for fuel follows the same Art. 86a logic as the vehicle itself.
**Legislation:** ustawa o VAT, Art. 86a ust. 1, ust. 2 pkt 3.

### EC11 -- White list payment violation [T1]
**Situation:** Company pays PLN 30,000 to a supplier's bank account that is NOT on the white list (biala lista).
**Resolution:** The buyer faces two consequences: (1) joint and several liability for the supplier's unpaid VAT, and (2) the expense is non-deductible for CIT. Safe harbour: file ZAW-NR form with the tax office within 7 days of payment to avoid liability. VAT on the purchase is still deductible for VAT purposes (white list affects CIT, not VAT input deduction), but the risk of joint VAT liability remains.
**Legislation:** Ordynacja podatkowa, Art. 117ba; ustawa o CIT, Art. 15d.

### EC12 -- Full business use vehicle with GPS tracking [T2]
**Situation:** Company purchases a delivery car (passenger vehicle, not N1) for PLN 80,000 net + PLN 18,400 VAT. Company maintains GPS tracking log, filed VAT-26 within 25 days, has internal vehicle usage rules.
**Resolution:** 100% VAT deduction claimed (PLN 18,400). Report full amount in P_43/P_45. However, [T2] flag: reviewer must verify GPS log completeness, VAT-26 filing confirmation, and that no private use has occurred. Any private use (even occasional) invalidates the 100% claim retroactively.
**Legislation:** ustawa o VAT, Art. 86a ust. 3-12.

### EC13 -- Quarterly filer (JPK_V7K), first month of quarter [T1]
**Situation:** Entity is a maly podatnik filing JPK_V7K. It is January (month 1 of Q1).
**Resolution:** Submit Ewidencja (records) only for January. The Deklaracja (declaration) part is submitted together with March's filing (month 3 of Q1). The Ewidencja for January is still due by 25 February.
**Legislation:** ustawa o VAT, Art. 99 ust. 3.

### EC14 -- Gift to client exceeding PLN 100 net [T1]
**Situation:** Company gives a gift basket worth PLN 300 net + PLN 69 VAT to a client. Input VAT was deducted on purchase.
**Resolution:** Input VAT (PLN 69) IS deductible. However, since the gift value exceeds PLN 100 net and input VAT was deducted, the gift is a deemed supply (nieodplatne przekazanie towarow). Output VAT must be charged at 23% on the market value (PLN 300 * 23% = PLN 69) and reported in P_13/P_14.
**Legislation:** ustawa o VAT, Art. 7 ust. 2 (deemed supply), Art. 7 ust. 3-4 (PLN 100 threshold for gifts).

### EC15 -- Construction services with MPP annotation [T1]
**Situation:** Polish construction subcontractor invoices PLN 50,000 gross for construction work (Annex 15) to a general contractor. Both are Polish VAT payers.
**Resolution:** Before November 2019, this would have been domestic reverse charge. Now it is a standard supply WITH mandatory split payment (MPP). Subcontractor charges 23% VAT normally. Invoice must include "mechanizm podzielonej platnosci" annotation. Buyer pays via MPP (net to current account, VAT to VAT account). Report input VAT in P_43.
**Legislation:** ustawa o VAT, Art. 108a ust. 1a (MPP replaced domestic RC for construction from 1 Nov 2019).

### EC16 -- Passenger car purchase for taxi company [T1]
**Situation:** Licensed taxi company purchases a passenger car for PLN 100,000 net + PLN 23,000 VAT. Car will be used exclusively as a taxi.
**Resolution:** 100% VAT deduction. Taxi operators are exempt from the 50% limitation provided the vehicle is used exclusively for licensed taxi services and the company meets the GPS/log requirements. Report PLN 23,000 in P_43/P_45.
**Legislation:** ustawa o VAT, Art. 86a ust. 3 pkt 1 (vehicles used exclusively for business) -- taxi use qualifies with proper documentation.

### EC17 -- Late reporting of intra-EU acquisition (WNT beyond 3 months) [T1]
**Situation:** Polish company received goods from a French supplier in January but only discovered the invoice in June (5 months later).
**Resolution:** Output VAT (P_22) must be reported in the period the tax obligation arose (January). Input VAT (P_40) can only be claimed in the current period (June) AFTER the output side is corrected. The 3-month window for simultaneous reporting has passed, so corrections must be filed. Output VAT correction for January; input VAT in the current June filing.
**Legislation:** ustawa o VAT, Art. 86 ust. 10b pkt 2 lit. b, Art. 86 ust. 10i.

---

## Step 12: Test Suite

### Test 1 -- Standard domestic purchase, 23% VAT [T1]
**Input:** Polish supplier, office supplies, gross PLN 1,230, VAT PLN 230, net PLN 1,000. Active VAT payer. Not Annex 15. Invoice < PLN 15,000.
**Expected output:** P_43 += PLN 230. Input VAT recoverable in full. No MPP required. No GTU code on purchase record.

### Test 2 -- Import of services from US (SaaS subscription) [T1]
**Input:** US supplier (Notion), monthly fee USD 20 (~PLN 86 net), no VAT on invoice. Active VAT payer. Service is software/IT.
**Expected output:** P_25 = PLN 86, P_26 = PLN 19.78 (23%), P_42 = PLN 19.78. Net VAT effect = zero. Purchase record has no GTU (purchase side).

### Test 3 -- Intra-EU goods acquisition (WNT) [T1]
**Input:** German supplier, machinery parts EUR 5,000 (~PLN 21,500 at assumed rate), invoice at 0% with valid DE VAT number. Active VAT payer.
**Expected output:** P_21 = PLN 21,500, P_22 = PLN 4,945 (23%), P_40 = PLN 4,945. Net = zero. Reported on VAT-UE. If machinery parts are Annex 15 items (e.g., steel), and gross > PLN 15,000, MPP applies on payment.

### Test 4 -- Mixed-use passenger car purchase (no GPS log) [T1]
**Input:** Dealer invoice PLN 100,000 net + PLN 23,000 VAT. Car for mixed use (no GPS log, no VAT-26 filed). Fixed asset.
**Expected output:** P_43 += PLN 11,500 (50%). P_45 += PLN 11,500. Remaining PLN 11,500 is non-deductible (added to CIT depreciation base). 50% rule applies under Art. 86a.

### Test 5 -- Mandatory split payment invoice (Annex 15 goods) [T1]
**Input:** Polish supplier invoices PLN 25,000 gross for steel products (Annex 15). B2B transaction. Both parties active VAT payers.
**Expected output:** Payment must use MPP. Invoice must bear "mechanizm podzielonej platnosci". Normal VAT reporting: VAT on purchase in P_43. MPP = "1" on purchase record. Buyer verifies supplier on white list before payment.

### Test 6 -- Accommodation service at Polish hotel [T1]
**Input:** Polish hotel invoice PLN 500 net + PLN 40 VAT (8%). Business trip by employee.
**Expected output:** P_43 += PLN 0. VAT is **BLOCKED** under Art. 88 ust. 1 pkt 4 lit. c. No input VAT recovery. Full PLN 540 is a cost. Exception only if hotel services are purchased for resale (e.g., travel agent).

### Test 7 -- EU B2B service export (consulting) [T1]
**Input:** Polish company invoices French client EUR 2,000 for management consulting. B2B. French client has valid FR VAT number.
**Expected output:** P_12 = PLN equivalent of EUR 2,000. No output VAT. Reported on VAT-UE. Sales record marked with GTU_12 (consulting = intangible services).

### Test 8 -- Quarterly filer (JPK_V7K), months 1 and 2 of quarter [T1]
**Input:** JPK_V7K filer, month 1 of quarter (January).
**Expected output:** Submit Ewidencja (records) only for January, by 25 February. Deklaracja (declaration) submitted with month 3 (March), by 25 April.

### Test 9 -- Fuel for mixed-use car [T1]
**Input:** Fuel invoice PLN 400 net + PLN 92 VAT (23%). Car is mixed-use (no GPS log). Active VAT payer.
**Expected output:** P_43 += PLN 46 (50% of PLN 92). Remaining PLN 46 is non-deductible. 50% rule under Art. 86a applies to fuel for mixed-use vehicles.

### Test 10 -- White list verification before payment [T1]
**Input:** Purchase invoice PLN 30,000 gross from Polish supplier. Buyer checks white list -- supplier's bank account IS on the list.
**Expected output:** Payment proceeds normally. VAT in P_43. No joint liability risk. If supplier's account were NOT on the list, buyer should use MPP voluntarily (for VAT protection) and file ZAW-NR within 7 days.

### Test 11 -- Gift to client, net value PLN 80 (below PLN 100 threshold) [T1]
**Input:** Company buys gift worth PLN 80 net + PLN 18.40 VAT (23%). Gives to client. Input VAT was deducted.
**Expected output:** P_43 += PLN 18.40 (input VAT deductible). No deemed supply because value <= PLN 100 net (Art. 7 ust. 3-4). No output VAT required.

### Test 12 -- Gift to client, net value PLN 300 (above PLN 100 threshold) [T1]
**Input:** Company buys gift worth PLN 300 net + PLN 69 VAT (23%). Gives to client. Input VAT was deducted.
**Expected output:** P_43 += PLN 69 (input VAT deductible). BUT: deemed supply under Art. 7 ust. 2. Output VAT due: P_13 += PLN 300 (base), P_14 += PLN 69 (output VAT). Net cost of gift includes the output VAT effectively making the gift VAT-neutral.

### Test 13 -- Construction subcontractor invoice with MPP [T1]
**Input:** Polish subcontractor invoices PLN 50,000 gross (PLN 40,650 net + PLN 9,350 VAT at 23%) for construction work (Annex 15). Both parties are Polish VAT payers.
**Expected output:** Standard supply (NOT reverse charge -- domestic RC for construction was replaced by MPP). Invoice must include "mechanizm podzielonej platnosci". Buyer pays via MPP. P_43 += PLN 9,350. MPP = "1" on purchase record.

---

## Step 13: Comparison with Malta

### 13a. Structural Comparison [T1]

| Feature | Poland | Malta |
|---------|--------|-------|
| **Return form** | JPK_V7M (monthly) / JPK_V7K (quarterly) -- merged declaration + SAF-T | VAT3 (quarterly) / Article 11 declaration (annual) |
| **Filing method** | Electronic only (e-Urzad Skarbowy) | Electronic (CFR portal) or paper |
| **Standard VAT rate** | 23% (ustawa o VAT, Art. 41 ust. 1) | 18% (VAT Act Cap. 406) |
| **Reduced rates** | 8%, 5% (Art. 41 ust. 2, 2a) | 7%, 5%, 12% (5th Schedule) |
| **Zero rate** | 0% -- exports, intra-EU supplies (Art. 41 ust. 3) | 0% -- exports, intra-EU supplies |
| **Registration threshold** | PLN 200,000 (~EUR 46,000) / PLN 240,000 from 2026 (Art. 113) | EUR 35,000 (Article 11) |
| **NIP/VAT number format** | PL + 10 digits | MT + 8 digits |
| **Filing deadline** | 25th of following month (monthly); 25th after quarter end (quarterly) | 21st after quarter end (e-filing); 14th (paper) |
| **Capital goods threshold** | PLN 15,000 net for multi-year adjustment (Art. 91) | EUR 1,160 gross (Article 24) |
| **Capital goods adjustment** | 5 years (movable), 10 years (immovable) (Art. 91) | 5 years (Article 24) |
| **Currency** | PLN (Polish zloty) | EUR (Euro) |
| **Tax authority** | KAS (Krajowa Administracja Skarbowa) | CFR (Commissioner for Revenue) |

### 13b. Deductibility Comparison [T1]

| Expense Category | Poland | Malta |
|-----------------|--------|-------|
| **Entertainment / representation** | **DEDUCTIBLE** for VAT (Art. 86 ust. 1; no block in Art. 88) | **BLOCKED** (10th Schedule Item 3(1)(b)) |
| **Motor vehicles (passenger cars)** | **50% deductible** (mixed use, Art. 86a); 100% with GPS log and VAT-26 | **BLOCKED** (10th Schedule Item 3(1)(a)(iv-v)); exception: taxi, car rental |
| **Fuel (for mixed-use car)** | **50% deductible** (Art. 86a ust. 2 pkt 3) | **BLOCKED** if vehicle is blocked (10th Schedule) |
| **Accommodation** | **BLOCKED** (Art. 88 ust. 1 pkt 4 lit. c) | Not specifically blocked (deductible if business-related) |
| **Catering** | **BLOCKED** (Art. 88 ust. 1 pkt 4 lit. b) | Not specifically blocked (follows entertainment rule) |
| **Tobacco** | Not specifically blocked for VAT (but excise duty applies) | **BLOCKED** (10th Schedule Item 3(1)(a)(i)) |
| **Alcohol** | Not specifically blocked for VAT (subject to excise) | **BLOCKED** (10th Schedule Item 3(1)(a)(ii)) |
| **Art/antiques** | Not specifically blocked | **BLOCKED** (10th Schedule Item 3(1)(a)(iii)) |

### 13c. Mechanism Comparison [T1]

| Mechanism | Poland | Malta |
|-----------|--------|-------|
| **Split payment** | YES -- mandatory for Annex 15 goods/services > PLN 15,000 (Art. 108a) | NO -- no split payment mechanism |
| **White list** | YES -- must verify supplier's bank account for payments > PLN 15,000 (Art. 96b) | NO -- no white list requirement |
| **GTU codes** | YES -- 13 codes (GTU_01 to GTU_13) on sales records | NO -- no equivalent reporting codes |
| **SAF-T** | YES -- integrated into JPK_V7 (merged with VAT return) | NO -- separate filing if requested |
| **KSeF e-invoicing** | YES -- mandatory from Feb/Apr 2026 (Art. 106na) | NO -- no mandatory e-invoicing system |
| **Domestic reverse charge** | Limited -- largely replaced by MPP (Art. 17 ust. 1 pkt 7-8, only for non-established suppliers) | N/A -- Malta follows standard EU rules |
| **Partial exemption** | Proporcja (Art. 90) + Prewspolczynnik (Art. 86 ust. 2a) | Pro-rata (Article 22(4)) |
| **Refund timeline** | 60 days standard; 25 days accelerated; 40 days with KSeF | 21 days from filing (quarterly) |
| **Quarterly filing** | Only for maly podatnik (< PLN 2 million revenue, not first year) | Standard for Article 10 |

### 13d. Key Differences for Practitioners [T2]

| Area | Practical Impact |
|------|-----------------|
| **Entertainment VAT** | Poland allows full input VAT on entertainment; Malta blocks it entirely. A dinner with clients is VAT-deductible in PL but not in MT. |
| **Vehicle costs** | Poland permits 50% VAT recovery on passenger cars by default (100% with GPS); Malta blocks vehicle VAT entirely (except taxis/rental). |
| **Accommodation** | Reversed from entertainment: Poland BLOCKS hotel VAT; Malta does NOT have a specific block on accommodation. |
| **Compliance burden** | Poland has significantly higher compliance requirements: MPP, white list, GTU codes, KSeF. Malta has simpler reporting. |
| **Filing frequency** | Poland requires monthly SAF-T reporting even for quarterly declarants; Malta quarterly filers only submit quarterly. |

---

## Step 14: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Doradca podatkowy must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to doradca podatkowy. Document gap.
```

---

## PROHIBITIONS [T1]

These are absolute rules. Violation of any prohibition is a critical error.

1. **NEVER** let AI guess JPK_V7 field assignment -- it is deterministic from transaction facts. **ustawa o VAT, Art. 99, Art. 109.**
2. **NEVER** ignore mandatory split payment (MPP) when all three conditions are met (B2B + > PLN 15,000 + Annex 15). **ustawa o VAT, Art. 108a.**
3. **NEVER** claim 100% VAT on passenger cars without verifying GPS log (ewidencja przebiegu pojazdu), VAT-26 filing, and internal vehicle usage rules. **ustawa o VAT, Art. 86a ust. 4-12.**
4. **NEVER** claim input VAT on accommodation services (blocked under Art. 88 ust. 1 pkt 4 lit. c) unless purchased for resale. **ustawa o VAT, Art. 88.**
5. **NEVER** claim input VAT on catering services (blocked under Art. 88 ust. 1 pkt 4 lit. b). **ustawa o VAT, Art. 88.**
6. **NEVER** apply reverse charge to out-of-scope categories (wages, dividends, loan repayments, ZUS contributions). **ustawa o VAT, Art. 5.**
7. **NEVER** apply reverse charge to local consumption services abroad (hotel, restaurant, taxi in another country). **ustawa o VAT, Art. 28e, Art. 28i.**
8. **NEVER** allow VAT-exempt entities (podatnik zwolniony) to claim input VAT. **ustawa o VAT, Art. 86 ust. 1.**
9. **NEVER** omit GTU codes on sales of goods/services listed in the GTU table. **Rozporzadzenie Ministra Finansow (JPK_V7 schema).**
10. **NEVER** skip white list verification before making B2B payments exceeding PLN 15,000. **Ordynacja podatkowa, Art. 117ba.**
11. **NEVER** apply domestic reverse charge to transactions between Polish-established entities for Annex 15 goods/services -- use MPP instead (since 1 November 2019). **ustawa o VAT, Art. 108a.**
12. **NEVER** skip KSeF e-invoicing for domestic B2B invoices after the applicable mandatory date (Feb/Apr 2026). **ustawa o VAT, Art. 106na.**
13. **NEVER** compute any number -- all arithmetic is handled by the deterministic engine, not the AI. The AI classifies; the engine calculates.
14. **NEVER** report input VAT on intra-EU acquisitions (WNT) if more than 3 months have passed since the tax obligation arose without first correcting the output VAT side. **ustawa o VAT, Art. 86 ust. 10b pkt 2.**
15. **NEVER** pay invoices > PLN 15,000 to bank accounts not on the white list without filing ZAW-NR within 7 days. **Ordynacja podatkowa, Art. 117ba par. 3.**

---

## Contribution Notes

This skill was generated based on publicly available information about Poland's VAT system as of April 2026. It requires validation by a warranted Polish tax adviser (doradca podatkowy) before it may be used for actual filing. All T1 rules must be verified against current legislation. Edge cases should be expanded based on practitioner experience.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**

Key sources consulted:
- Ustawa z dnia 11 marca 2004 r. o podatku od towarow i uslug (Dz.U. 2004 Nr 54, poz. 535, as amended)
- Kodeks karny skarbowy (Dz.U. 1999 Nr 83, poz. 930, as amended)
- Ordynacja podatkowa (Dz.U. 1997 Nr 137, poz. 926, as amended)
- Rozporzadzenie Ministra Finansow w sprawie JPK_V7M/JPK_V7K
- PWC Tax Summaries -- Poland Corporate Other Taxes (https://taxsummaries.pwc.com/poland/corporate/other-taxes)
- KAS official guidance on split payment, white list, and GTU codes


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
