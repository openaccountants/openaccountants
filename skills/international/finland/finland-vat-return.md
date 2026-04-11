---
name: finland-vat-return
description: Use this skill whenever asked to prepare, review, or create a Finland VAT return (Arvonlisaveroilmoitus / ALV-ilmoitus) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in ALV", "create the return", "Finnish VAT", "OmaVero", or any request involving Finland VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Finland VAT classification rules, OmaVero field mappings, deductibility rules, reverse charge treatment, construction reverse charge (rakentamispalvelun kaannetty verovelvollisuus), Aland Islands special rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Finnish VAT-related work.
---

# Finland VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Finland (Suomi) |
| Jurisdiction Code | FI |
| Primary Legislation | Arvonlisaverolaki (AVL, VAT Act 1501/1993, as amended by Act 1109/2023, Act 817/2024, and Act 421/2024) |
| Supporting Legislation | Laki oma-aloitteisten verojen verotusmenettelysta (OVML, Act on Assessment Procedure for Self-Assessed Taxes, 768/2016) |
| Tax Authority | Verohallinto (Finnish Tax Administration / Vero Skatt) |
| Filing Portal | https://www.vero.fi/omavero (OmaVero / MyTax) |
| Currency | Euro (EUR) |
| VAT ID Format | FI + 8 digits (Y-tunnus without hyphen; e.g., Y-tunnus 1234567-8 becomes FI12345678) |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 2.1 |
| Status | deep-research-verified |
| Rate Source | PWC Tax Summaries (taxsummaries.pwc.com/finland/corporate/other-taxes), verified April 2026 |
| Confidence Coverage | Tier 1: field assignment, reverse charge, deductibility blocks, rate assignment. Tier 2: partial exemption, construction reverse charge eligibility, mixed-use apportionment. Tier 3: complex group structures, VAT grouping, international shipping/aviation, Aland customs procedures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A KHT/HT auditor or veroasiantuntija must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and Y-tunnus (business ID)** [T1] -- format NNNNNNN-N (7 digits, hyphen, check digit); for EU VIES purposes the FI-prefixed VAT number omits the hyphen: FI + 8 digits. **Legislation:** AVL S 172.
2. **VAT registration status** [T1] -- Registered (arvonlisaverovelvollinen), non-registered (below threshold), or liable for specific activities only. **Legislation:** AVL S 2-6.
3. **Filing frequency** [T1] -- Monthly (liikevaihto > EUR 100,000), Quarterly (EUR 30,001-100,000), or Annual (liikevaihto <= EUR 30,000). **Legislation:** OVML S 2.
4. **Industry/sector** [T2] -- impacts applicable reduced rates and specific rules (e.g., construction, food, transport, publishing). **Legislation:** AVL S 84-85l.
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (AVL S 117); reviewer must confirm pro-rata calculation.
6. **Does the business perform construction services?** [T1] -- determines whether domestic construction reverse charge applies (AVL S 8c).
7. **Does the business operate in or trade with Aland Islands?** [T1] -- Aland is outside EU VAT territory for goods (AVL S 68a). Special import/export treatment.
8. **Excess credit brought forward** [T1] -- Finland refunds excess automatically; no carry-forward by default. Palautettava vero. **Legislation:** AVL S 149.

**If any of items 1-3 are unknown, STOP. Do not classify any transactions.**

---

## Section 1: VAT Return Form Structure -- Arvonlisaveroilmoitus (ALV-ilmoitus)

### 1.1 Filing Method [T1]

The Finnish VAT return (Arvonlisaveroilmoitus) is filed electronically via **OmaVero (MyTax)** at https://www.vero.fi/omavero. Paper filing is not available for standard filers. **Legislation:** AVL S 162; OVML S 18.

OmaVero accepts:
- Manual entry via the web portal
- File upload (CSV/XML in Verohallinto-prescribed format)
- Integration via API (Apitamo / Ilmoitin.fi for accounting software)

### 1.2 Complete Field Reference [T1]

The ALV-ilmoitus consists of the following fields (codes) as prescribed by Verohallinto. Every transaction must map to exactly one output field (if applicable) and one input field (if applicable).

**Legislation:** AVL S 162; Verohallinto decision on reporting obligations.

#### Output VAT Fields (Suoritettava vero -- Tax on Sales)

| Code | Finnish Name | English Description | Rate / Type | AVL Section |
|------|-------------|---------------------|-------------|-------------|
| 301 | Vero kotimaan myynnista 25,5 % -- veron peruste | Tax base of domestic sales at 25.5% | 25.5% base | AVL S 84 |
| 302 | Vero kotimaan myynnista 13,5 % -- veron peruste | Tax base of domestic sales at 13.5% | 13.5% base (was 14% until 31 Dec 2025) | AVL S 85 |
| 303 | Vero kotimaan myynnista 10 % -- veron peruste | Tax base of domestic sales at 10% | 10% base | AVL S 85a |
| 305 | Vero kotimaan myynnista 25,5 % -- veron maara | VAT amount on domestic sales at 25.5% | 25.5% tax | AVL S 84 |
| 306 | Vero kotimaan myynnista 13,5 % -- veron maara | VAT amount on domestic sales at 13.5% | 13.5% tax (was 14% until 31 Dec 2025) | AVL S 85 |
| 318 | Vero kotimaan myynnista 10 % -- veron maara | VAT amount on domestic sales at 10% | 10% tax | AVL S 85a |
| 311 | Tavaroiden myynnit muihin EU-maihin | Intra-EU supply of goods | 0% | AVL S 72b |
| 312 | Palvelujen myynnit muihin EU-maihin | Intra-EU supply of services (B2B) | 0% | AVL S 65-69 |
| 309 | Tavaraostot muista EU-maista -- veron peruste | Intra-EU acquisition of goods -- tax base | RC | AVL S 26a |
| 313 | Palveluostot muista EU-maista -- veron peruste | EU services received (reverse charge) -- tax base | RC | AVL S 9, 65 |
| 319 | Palveluostot EU:n ulkopuolelta -- veron peruste | Import of services from non-EU -- tax base | RC | AVL S 9, 65 |
| 320 | Rakentamispalvelun kaannetty verovelvollisuus -- veron peruste | Construction reverse charge -- tax base | RC | AVL S 8c |
| 310 | Veroton kotimaan myynti | Domestic exempt sales (without credit) | Exempt | AVL S 34-60 |
| 314 | Tavaroiden myynnit EU:n ulkopuolelle (vienti) | Export of goods to non-EU | 0% | AVL S 70 |

#### Input VAT Fields (Vahennettava vero -- Deductible Tax)

| Code | Finnish Name | English Description | Notes | AVL Section |
|------|-------------|---------------------|-------|-------------|
| 307 | Kohdekuukauden vahennettava vero (yhteensa) | Total deductible input VAT for the period | Single aggregate field | AVL S 102-103 |

#### Settlement Fields

| Code | Finnish Name | English Description | Notes |
|------|-------------|---------------------|-------|
| 308 | Suoritettava vero yhteensa | Total output VAT payable | Sum of 305 + 306 + 318 + RC VAT amounts |
| 307 | Vahennettava vero yhteensa | Total deductible input VAT | Single figure |
| 399 | Maksettava vero / Palautukseen oikeuttava vero | Net VAT payable (positive) or refundable (negative) | 308 minus 307 |

### 1.3 Key Structural Feature [T1]

Finland's input VAT is reported as a **SINGLE total figure** (Code 307), NOT broken down by rate, source, or category. This is fundamentally different from jurisdictions like Malta (which has separate input boxes for overheads, capital, resale, EU, non-EU). The single-field approach simplifies the return but requires detailed supporting records. **Legislation:** AVL S 162, 209b.

### 1.4 Supporting Declarations [T1]

| Declaration | Finnish Name | Frequency | Deadline | AVL Section |
|------------|-------------|-----------|----------|-------------|
| EU Sales List (Recapitulative Statement) | Yhteenvetoilmoitus | Monthly | 12th of M+2 | AVL S 162a |
| Intrastat (arrivals/dispatches) | Intrastat-ilmoitus | Monthly | 10th working day of M+1 | EU Reg 2019/2152 |
| VAT Return | ALV-ilmoitus | Monthly/Quarterly/Annual | See Section 6 | AVL S 162, OVML S 2 |

---

## Section 2: Transaction Classification Matrix

### 2.1 Step 1 -- Determine Transaction Type [T1]

**Legislation:** AVL S 1-4 (taxable activities), S 17-18 (place of supply).

| Transaction Nature | Classification | Action |
|-------------------|---------------|--------|
| Sale of goods/services | Suoritettava vero (output VAT) | Map to output fields |
| Purchase of goods/services | Vahennettava vero (input VAT) | Map to Code 307 |
| Salary / wages (palkka) | OUT OF SCOPE | Never on ALV return |
| Social contributions (TyEL, YEL, SoTu) | OUT OF SCOPE | Never on ALV return |
| Income tax (tulovero) | OUT OF SCOPE | Never on ALV return |
| Loan repayment (lainan lyhennys) | OUT OF SCOPE | Never on ALV return |
| Dividend (osinko) | OUT OF SCOPE | Never on ALV return |
| Bank charges (pankkikulut) | Exempt input (AVL S 41) | No VAT recovery |
| Insurance premiums (vakuutusmaksut) | Exempt input (AVL S 44) | No VAT recovery |
| Grants / subsidies (avustukset) | OUT OF SCOPE (unless consideration for supply) | Review per AVL S 79 |

### 2.2 Step 2 -- Determine Counterparty Location [T1]

**Legislation:** AVL S 63a-69h (place of supply rules).

| Location | Countries | Treatment |
|----------|-----------|-----------|
| Finland (domestic) | FI (mainland) | Normal domestic VAT |
| Aland Islands | Ahvenanmaa | Outside EU VAT for goods; domestic for services (see EC1) |
| EU Member States | AT, BE, BG, HR, CY, CZ, DK, EE, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE | Intra-EU rules |
| Non-EU | All others (incl. UK post-Brexit, NO, CH, US) | Import/export rules |

### 2.3 Step 3 -- Sales Classification Lookup Table [T1]

**Legislation:** AVL S 63a-72h (place of supply), S 70-72h (zero-rating), S 84-85l (rates).

| Sale Type | Counterparty | B2B/B2C | Rate | Output Field (Base) | Output Field (Tax) | AVL Section |
|-----------|-------------|---------|------|---------------------|-------------------|-------------|
| Domestic goods/services (standard) | FI | Any | 25.5% | 301 | 305 | AVL S 84 |
| Domestic food/animal feed sale | FI | Any | 13.5% | 302 | 306 | AVL S 85(1)(1) |
| Domestic restaurant/catering | FI | Any | 13.5% | 302 | 306 | AVL S 85(1)(2) |
| Domestic books (physical/electronic) | FI | Any | 10% | 303 | 318 | AVL S 85a(1)(7) |
| Domestic medicines (prescription) | FI | Any | 10% | 303 | 318 | AVL S 85a(1)(6) |
| Domestic passenger transport | FI | Any | 10% | 303 | 318 | AVL S 85a(1)(1) |
| Domestic accommodation | FI | Any | 10% | 303 | 318 | AVL S 85a(1)(3) |
| Domestic cultural/sporting events | FI | Any | 10% | 303 | 318 | AVL S 85a(1)(4) |
| Domestic newspapers/periodicals | FI | Any | 10% | 303 | 318 | AVL S 85a(1)(8) |
| Domestic minor repair (bicycles, shoes, leather, clothing, linen) | FI | Any | 10% | 303 | 318 | AVL S 85a(1)(5) |
| Domestic exempt (financial, insurance, healthcare, education) | FI | Any | Exempt | 310 | -- | AVL S 34-60 |
| Intra-EU supply of goods | EU | B2B | 0% | 311 | -- | AVL S 72b |
| Intra-EU supply of services | EU | B2B | 0% | 312 | -- | AVL S 65-69 |
| Export of goods to non-EU | Non-EU | Any | 0% | 314 | -- | AVL S 70 |
| Export of services to non-EU | Non-EU | B2B | 0% (outside scope) | 314 | -- | AVL S 65, 69h |

### 2.4 Step 4 -- Purchases Classification Lookup Table [T1]

**Legislation:** AVL S 102-103 (right to deduct), S 8a-8d (reverse charge), S 9 (import of services), S 8c (construction RC).

| Purchase Type | Supplier Location | Treatment | Tax Base Field | Output VAT Included In | Input VAT Field | AVL Section |
|--------------|-------------------|-----------|---------------|----------------------|----------------|-------------|
| Domestic purchase (standard) | FI | Normal | -- | -- | 307 | AVL S 102 |
| Domestic purchase (reduced 13.5%) | FI | Normal | -- | -- | 307 | AVL S 102 |
| Domestic purchase (reduced 10%) | FI | Normal | -- | -- | 307 | AVL S 102 |
| Domestic exempt purchase | FI | No recovery | -- | -- | -- | AVL S 34-60 |
| EU goods acquisition | EU | Reverse charge | 309 | 308 | 307 | AVL S 26a, 8a |
| EU services received (B2B) | EU | Reverse charge | 313 | 308 | 307 | AVL S 9, 65 |
| Non-EU services received | Non-EU | Reverse charge | 319 | 308 | 307 | AVL S 9 |
| Import of goods from non-EU | Non-EU | Self-assessed on return | -- | 308 | 307 | AVL S 86h (from 2018) |
| Construction services (RC applies) | FI | Construction RC | 320 | 308 | 307 | AVL S 8c |
| Construction services (RC does NOT apply) | FI | Normal domestic | -- | -- | 307 | AVL S 102 |
| Goods from Aland to mainland | Aland | Import treatment | -- | 308 | 307 | AVL S 68a, 86h |
| Out-of-scope (salaries, tax, etc.) | Any | NEVER on return | -- | -- | -- | -- |
| Local consumption abroad (hotel/taxi) | EU/Non-EU | NOT reverse charge | -- | -- | -- | Foreign VAT irrecoverable |

---

## Section 3: VAT Rates -- Complete Schedule

### 3.1 Current Rates (as of 1 September 2024) [T1]

**Source verification:** PWC Tax Summaries (taxsummaries.pwc.com/finland/corporate/other-taxes, accessed April 2026) confirms standard rate of 25.5%.

**Legislation:** AVL S 84-85l, as amended by Act 817/2024 (rate increase effective 1 September 2024).

| Rate | Percentage | Finnish Term | Supplies Covered | AVL Section |
|------|-----------|-------------|-----------------|-------------|
| Standard | **25.5%** | Yleinen verokanta | All taxable supplies not qualifying for reduced rate or zero rate | AVL S 84 |
| Reduced I | **13.5%** | Alennettu verokanta (13,5 %) | Food and animal feed (elintarvikkeet ja rehut); restaurant and catering services (ravintola- ja ateriapalvelut); passenger transport; accommodation; cultural and sports events; medicines (prescription). Reduced from 14% to 13.5% effective 1 January 2026. | AVL S 85(1)(1-2) |
| Reduced II | **10%** | Alennettu verokanta (10 %) | Books (kirjat, incl. e-books); newspapers and periodicals (sanoma- ja aikakauslehdet); medicines (laakkeet, prescription); passenger transport (henkilokuljetukset); accommodation (majoituspalvelut); admission to cultural and sporting events (kulttuuri- ja urheilutapahtumien paasynmaksut); minor repairs (bicycles, shoes, leather, clothing, linen) | AVL S 85a(1)(1-8) |
| Zero | **0%** | Nollaverokanta | Exports of goods (vienti, AVL S 70); intra-EU supplies of goods (yhteisonmyynti, AVL S 72b); international transport services (AVL S 71); vessels and aircraft for international traffic (AVL S 70(1)(6-7)) | AVL S 70-72h |
| Exempt (no credit) | **N/A** | Verovapaa (ilman vahennysoikeutta) | Financial services (AVL S 41-42); insurance (AVL S 44); healthcare (AVL S 34-36); education (AVL S 39-40); real estate transfers (AVL S 27-28); residential rental (AVL S 27) | AVL S 34-60 |

### 3.2 Rate Change History [T1]

**Legislation:** Act 817/2024 (standard rate increase); historical Acts.

| Effective Date | Standard | Reduced I | Reduced II | Legislation |
|---------------|----------|-----------|------------|-------------|
| 1 Jan 2026 -- present | **25.5%** | **13.5%** | 10% | Act 817/2024 (standard); Act on reduced rate reduction (2025) |
| 1 Sep 2024 -- 31 Dec 2025 | **25.5%** | 14% | 10% | Act 817/2024 |
| 1 Jan 2013 -- 31 Aug 2024 | 24% | 14% | 10% | Act 1202/2011 |
| 1 Jul 2010 -- 31 Dec 2012 | 23% | 13% | 9% | Act 1780/2009 |
| 1 Oct 2009 -- 30 Jun 2010 | 22% | 12% | 8% | Act 907/2009 |

### 3.3 Rate Transition Rules [T1]

**The September 2024 rate change from 24% to 25.5% requires careful handling.** **Legislation:** Act 817/2024, transitional provisions.

| Scenario | Rate to Apply | Rationale |
|----------|--------------|-----------|
| Supply completed before 1 Sep 2024 | 24% | Old rate applies to completed supplies |
| Supply completed on/after 1 Sep 2024 | 25.5% | New rate applies |
| Advance payment received before 1 Sep 2024, supply completed after | 24% on advance portion, 25.5% on remainder | AVL S 15(1) -- tax point is earlier of delivery or payment |
| Continuous supply spanning the change date | Apportion by delivery/performance date | Each portion uses the rate in force when performed |
| Credit note for pre-change supply issued after 1 Sep 2024 | 24% | Original rate follows original supply |
| Subscription starting before, ending after 1 Sep 2024 | Apportion pro rata | Split by days pre/post 1 Sep 2024 |

**The decisive factor is when the supply is performed (tavaran toimitus / palvelun suoritus), NOT the invoice date or payment date.** **Legislation:** AVL S 15-16.

### 3.4 Enacted Rate Change -- 1 January 2026 [T1]

The reduced rate I decreased from 14% to 13.5% effective 1 January 2026. This is now enacted law. All transactions with a tax point on or after 1 January 2026 use the 13.5% rate. Advance payments received before 1 January 2026 remain at 14%.

**Broadcasting services** previously at 10% have been reclassified to the 13.5% rate from 1 January 2026.

---

## Section 4: Blocked Input VAT (Vahennyskelvottomuus)

### 4.1 Fully Blocked Categories [T1]

**Legislation:** AVL S 114 (general deduction restrictions).

| Category | Finnish Term | VAT Recovery | Income Tax Deductibility | Key Distinction | AVL Section |
|----------|-------------|-------------|------------------------|----------------|-------------|
| **Entertainment / representation** | Edustusmenot | **0% -- FULLY BLOCKED** | 50% deductible for income tax (EVL S 8(1)(8)) | **CRITICAL: 50% income tax deduction does NOT extend to VAT. VAT is 100% irrecoverable.** | AVL S 114(1)(4) |
| **Residential property** (purchase, construction, renovation for non-taxable use) | Asuntojen hankinta | **0%** | N/A | Unless voluntary registration for taxable letting (AVL S 30) | AVL S 114(1)(1) |
| **Private / personal use** | Yksityiskaytto | **0%** | N/A | Must exclude from deduction entirely | AVL S 114(1)(4), 117 |
| **Gifts to clients / third parties** | Lahjat | **0%** | Limited deduction (EVL S 8(1)(8)) | Unless minor-value promotional items (vahatarvoinen mainoslahja, max ~EUR 50) | AVL S 114(1)(4) |

### 4.2 Motor Vehicles -- Special Rules [T1]

**Legislation:** AVL S 114(1)(5) (passenger car restriction); AVL S 114a (exceptions).

| Vehicle Type | VAT Recovery | Condition | AVL Section |
|-------------|-------------|-----------|-------------|
| Passenger car (henkiloauto) -- general | **0% -- BLOCKED** | Private or mixed business/personal use | AVL S 114(1)(5) |
| Passenger car -- taxi (taksi) | **100%** | Used exclusively in taxi operations | AVL S 114a(1) |
| Passenger car -- driving school (autokoulu) | **100%** | Used exclusively for driving instruction | AVL S 114a(2) |
| Passenger car -- car rental (autovuokraamo) | **100%** | Vehicle is rental stock | AVL S 114a(3) |
| Passenger car -- sale stock (automyynti) | **100%** | Vehicle is inventory for resale | AVL S 114a |
| Van / truck (pakettiauto / kuorma-auto) | **100%** | Used for business; not subject to passenger car restriction | AVL S 102 |
| Fuel for blocked vehicle | **0% -- BLOCKED** | Follows vehicle treatment | AVL S 114(1)(5) |
| Fuel for non-blocked vehicle (van/truck/taxi) | **100%** | Follows vehicle treatment | AVL S 102 |
| Leasing of passenger car | **0% -- BLOCKED** | Same restriction as purchase | AVL S 114(1)(5) |

**CRITICAL DISTINCTION from Malta:** In Malta, motor vehicle VAT is also blocked (10th Schedule Item 3(1)(a)(iv-v)), but Malta applies this to virtually all passenger cars. Finland similarly blocks passenger cars but provides explicit statutory exceptions for taxi, driving school, and car rental businesses (AVL S 114a).

### 4.3 Fully Deductible Categories (Notable) [T1]

**Unlike many EU countries, Finland does NOT block input VAT on the following (subject to business use requirement):**

| Category | VAT Recovery | Condition | AVL Section |
|----------|-------------|-----------|-------------|
| Business accommodation / hotel (majoitus) | **100%** | Must be for business travel | AVL S 102, 85a |
| Staff meals provided by employer (henkilokunnan ruokailu) | **100%** (if business purpose) | Not entertainment; internal staff function | AVL S 102 |
| Parking (pysakointi) | **100%** | Business purpose | AVL S 102 |
| Work clothing (tyovaatteet) | **100%** | Necessary for work | AVL S 102 |
| Van / delivery vehicle (pakettiauto) | **100%** | Business use | AVL S 102 |

### 4.4 Mixed Use -- Apportionment [T2]

**Legislation:** AVL S 117 (apportionment).

When an asset or expense is used for both taxable and exempt/private purposes:
- Directly attributable to taxable: **100% deductible**
- Directly attributable to exempt/private: **0% deductible**
- Mixed / general overhead: Pro-rata based on taxable turnover / total turnover

**Flag for reviewer:** Confirm pro-rata calculation. Annual adjustment may apply for immovable property (AVL S 119-121, 10-year adjustment).

### 4.5 Partial Exemption [T2]

**Legislation:** AVL S 117.

If business makes both taxable and exempt-without-credit supplies:

```
Recovery % = (Taxable Turnover / Total Turnover) * 100
```

Rounded up to nearest whole number. **Legislation:** AVL S 117(2).

- Costs directly attributable to taxable activities: 100% deductible
- Costs directly attributable to exempt activities: 0% deductible
- General overhead: apply pro-rata percentage

**Flag for reviewer: confirm pro-rata calculation before filing.**

---

## Section 5: Registration

### 5.1 Mandatory Registration [T1]

**Legislation:** AVL S 2-3, as amended by Act 421/2024.

| Criterion | Threshold | Notes | AVL Section |
|-----------|-----------|-------|-------------|
| Domestic turnover exceeds threshold | **EUR 15,000** per calendar year | Increased from EUR 10,000 by Act 421/2024 (effective 1 January 2025) | AVL S 3 |
| Intra-EU distance selling to Finland (B2C) | **EUR 10,000** (EU-wide OSS threshold) | Or EUR 0 if OSS opted | EU Dir 2006/112 Art 59c |
| Reverse charge liability | **No threshold** | Any amount triggers reporting obligation | AVL S 8a-9 |
| Import of goods | **No threshold** | Self-assessed on return since 2018 | AVL S 86h |

### 5.2 Voluntary Registration [T1]

**Legislation:** AVL S 12.

Businesses below the EUR 15,000 threshold may voluntarily register. Once registered, all normal VAT obligations apply including the right to deduct input VAT.

### 5.3 Y-tunnus and FI VAT Number Format [T1]

**Legislation:** AVL S 172; Yritys- ja yhteisotietolaki (Business Information Act 244/2001).

| Format | Structure | Example | Usage |
|--------|-----------|---------|-------|
| Y-tunnus (national) | NNNNNNN-N (7 digits, hyphen, check digit) | 1234567-8 | Domestic use, tax filings |
| FI VAT number (EU VIES) | FI + 8 digits (no hyphen) | FI12345678 | Intra-EU trade, EU Sales List |

### 5.4 Small Business Relief (Alarajahuojennus) -- ABOLISHED [T1]

**Legislation:** AVL S 149a -- REPEALED by Act 421/2024, effective 1 January 2025.

The graduated small business relief (alarajahuojennus) that previously allowed partial VAT relief for businesses with turnover between EUR 10,000 and EUR 30,000 has been **abolished** from 1 January 2025. This was replaced by the higher registration threshold of EUR 15,000.

**PROHIBITION:** NEVER apply alarajahuojennus for periods from 1 January 2025 onward.

### 5.5 Registration Threshold -- Comparison [T1]

| Jurisdiction | Registration Threshold | Legislation |
|-------------|----------------------|-------------|
| Finland | EUR 15,000 (from 1 Jan 2025; was EUR 10,000) | AVL S 3 |
| Malta | EUR 35,000 (Article 11 exemption) | VAT Act Cap. 406, Art 11 |
| EU Small Business Scheme (2025) | EUR 85,000 domestic / EUR 100,000 EU-wide (new EU scheme) | EU Dir 2020/285 |

---

## Section 6: Filing Deadlines (Ilmoitus- ja maksuaikataulut)

### 6.1 Filing Frequency and Deadlines [T1]

**Legislation:** OVML S 2-3; Verohallinto decision on filing periods.

| Frequency | Turnover Criterion | Period | Filing Deadline | Payment Deadline | AVL / OVML Section |
|-----------|-------------------|--------|----------------|-----------------|-------------------|
| Monthly (kuukausittain) | > EUR 100,000 | Calendar month | **12th of M+2** (e.g., January return due 12 March) | Same as filing deadline | OVML S 2(1) |
| Quarterly (neljännesvuosittain) | EUR 30,001 -- EUR 100,000 | Calendar quarter | **12th of 2nd month after quarter end** (e.g., Q1 Jan-Mar due 12 May) | Same as filing deadline | OVML S 2(2) |
| Annual (vuosittain) | <= EUR 30,000 | Calendar year | **End of February following the tax year** | Same as filing deadline | OVML S 2(3) |

**Key Feature:** Finland has an unusually late monthly deadline (12th of the second month following), giving businesses significantly more time than most EU countries. **Legislation:** OVML S 2(1).

### 6.2 Deadline Adjustments [T1]

**Legislation:** OVML S 3; Laki saadettyjen maaraaikain laskemisesta (Act on Calculation of Prescribed Time Limits, 150/1930).

If the filing/payment deadline falls on a Saturday, Sunday, or Finnish public holiday, it moves to the **next business day**.

Finnish public holidays (pyhapaivia):
- Uudenvuodenpaiva (1 January), Loppiainen (6 January), Pitkaaperjantai (Good Friday), Toinen paasiaispaiva (Easter Monday), Vappu (1 May), Helatorstai (Ascension Day), Juhannuspaiva (Midsummer Day -- Saturday nearest 24 June), Itsenaisyyspaiva (6 December), Joulupaiva (25 December), Tapaninpaiva (26 December).

**VAT return deadlines CANNOT be extended.** **Legislation:** OVML S 3.

### 6.3 Penalties for Late Filing and Payment [T1]

**Legislation:** OVML S 35-37 (myohastymismaksu), S 38-40 (veronkorotus).

| Penalty Type | Finnish Term | Amount / Rate | Condition | OVML Section |
|-------------|-------------|--------------|-----------|-------------|
| Late filing surcharge | Myohastymismaksu | EUR 3 per day, up to max EUR 135 per return | Return filed after deadline | OVML S 35 |
| Tax increase (negligence) | Veronkorotus | 10% of additional tax, minimum EUR 75 | Errors, omissions, or negligence | OVML S 38 |
| Tax increase (gross negligence / intent) | Veronkorotus (torkea) | Up to 50% of additional tax | Intentional underreporting | OVML S 39 |
| Late payment interest | Viivastyskorko | Reference rate + 7 percentage points (currently ~11% p.a.) | Tax paid after due date | Korkolaki (Interest Act 633/1982) S 4 |
| Maximum late filing penalty | Myohastymismaksu enimmaismäärä | EUR 15,000 | Per assessment decision | OVML S 37 |

### 6.4 Correction of Errors [T1]

**Legislation:** OVML S 16-17.

- Errors in a filed return can be corrected by submitting a replacement return via OmaVero
- Correction period: **3 years** from the original filing deadline (OVML S 16)
- Corrections in the taxpayer's favour: must be made by submitting a corrected return
- Corrections increasing tax: must be made promptly; myohastymismaksu may apply

---

## Section 7: Reverse Charge Mechanics (Kaannetty verovelvollisuus)

### 7.1 Intra-EU Acquisitions of Goods [T1]

**Legislation:** AVL S 26a-26f (intra-EU acquisitions), S 8a (reverse charge).

| Step | Action | Field |
|------|--------|-------|
| 1 | Report acquisition value (net) | Code 309 |
| 2 | Calculate output VAT at applicable Finnish rate | Included in Code 308 |
| 3 | Claim input VAT (if fully deductible) | Code 307 |
| 4 | Net effect for fully taxable business | Zero |

### 7.2 EU Services Received -- B2B General Rule [T1]

**Legislation:** AVL S 9 (reverse charge), S 65 (B2B place of supply).

| Step | Action | Field |
|------|--------|-------|
| 1 | Report service value (net) | Code 313 |
| 2 | Calculate output VAT at 25.5% (or applicable rate) | Included in Code 308 |
| 3 | Claim input VAT | Code 307 |
| 4 | Net effect for fully taxable business | Zero |

### 7.3 Import of Services from Non-EU [T1]

**Legislation:** AVL S 9 (reverse charge for services from abroad).

| Step | Action | Field |
|------|--------|-------|
| 1 | Report service value (net) | Code 319 |
| 2 | Calculate output VAT at 25.5% (or applicable rate) | Included in Code 308 |
| 3 | Claim input VAT | Code 307 |
| 4 | Net effect for fully taxable business | Zero |

### 7.4 Domestic Construction Reverse Charge (Rakentamispalvelun kaannetty verovelvollisuus) [T1]

**Legislation:** AVL S 8c (construction reverse charge -- enacted 2011).

**This is a FINLAND-SPECIFIC domestic reverse charge for construction services.**

#### Conditions -- ALL must be met:

| Condition | Requirement | AVL Section |
|-----------|------------|-------------|
| Supplier | Provides construction services (rakentamispalvelut): building, renovation, repair, demolition, earthworks, installation | AVL S 8c(1) |
| Buyer | Is a business that **regularly** provides construction services (either as main activity or on a regular/continuing basis) | AVL S 8c(1) |
| Both parties | VAT-registered in Finland | AVL S 8c |
| Service type | Must be construction services as defined in AVL S 31(3)(1) | AVL S 31(3)(1) |

#### Mechanics:

| Step | Action | Field |
|------|--------|-------|
| 1 | Subcontractor invoices WITHOUT VAT (noting "AVL 8c kaannetty verovelvollisuus") | -- |
| 2 | Buyer reports tax base | Code 320 |
| 3 | Buyer calculates output VAT at 25.5% | Included in Code 308 |
| 4 | Buyer claims input VAT | Code 307 |
| 5 | Net effect for fully taxable buyer | Zero |

#### When Construction RC Does NOT Apply [T1]:

| Scenario | Treatment | Rationale |
|----------|-----------|-----------|
| Buyer is NOT in the construction industry (e.g., office company hiring builder for renovation) | Normal VAT -- builder charges 25.5% | Buyer does not "regularly provide" construction services (AVL S 8c) |
| Service is not construction (e.g., architectural design, engineering consulting) | Normal VAT | Not within AVL S 31(3)(1) definition |
| Supplier is non-Finnish EU company | Intra-EU reverse charge (Code 313), not construction RC | AVL S 9 takes precedence |
| Supply of construction materials only (without installation) | Normal VAT on goods sale | Not a construction service |

### 7.5 Import of Goods from Non-EU (Self-Assessment on Return) [T1]

**Legislation:** AVL S 86h (enacted 1 January 2018 -- moved import VAT from customs to VAT return).

Since 1 January 2018, VAT on imports of goods is **declared and deducted on the VAT return**, NOT paid at customs. This applies to VAT-registered businesses.

| Step | Action | Field |
|------|--------|-------|
| 1 | Customs issues import decision with VAT amount | -- |
| 2 | Report import VAT as output VAT | Included in Code 308 |
| 3 | Claim import VAT as input VAT | Code 307 |
| 4 | Net effect for fully taxable business | Zero |

### 7.6 Reverse Charge Exceptions [T1]

**Legislation:** AVL S 8a-9, 65-69h.

| Scenario | Treatment | Rationale |
|----------|-----------|-----------|
| Out-of-scope categories (salaries, dividends, etc.) | NEVER reverse charge | Not a supply of goods/services |
| Local consumption abroad (hotel, restaurant, taxi) | NOT reverse charge; foreign VAT paid at source | Place of supply is abroad; foreign VAT irrecoverable |
| EU supplier charged local VAT > 0% | NOT reverse charge; foreign VAT is cost | Supplier applied their domestic rate |
| B2C services from EU (general rule) | NOT reverse charge (unless specific exception) | Place of supply for B2C is supplier's country (AVL S 66) |
| Small value consignments under EUR 150 (goods from non-EU to consumers) | Import VAT at customs (IOSS scheme) | Different regime for B2C imports |

---

## Section 8: Edge Cases (Finland-Specific)

### EC1 -- Aland Islands -- Goods Movement [T1]

**Situation:** Finnish mainland company receives goods from an Aland Islands supplier.
**Resolution:** Aland Islands (Ahvenanmaa) are **outside the EU VAT territory** for goods per Protocol 2 of Finland's EU Accession Treaty. Goods moving between Aland and mainland Finland (or other EU countries) are treated as **imports/exports** for VAT purposes. Import VAT treatment on the VAT return applies. Services between Aland and mainland are treated as domestic.
**Legislation:** AVL S 68a; Protocol 2 to Finland's EU Accession Treaty.
**Tag:** [T1]

### EC2 -- Entertainment Expenses: VAT vs. Income Tax Asymmetry [T1]

**Situation:** Business pays EUR 500 + EUR 67.50 VAT (13.5%) for a client entertainment dinner. The accountant notes that entertainment is 50% deductible for income tax purposes.
**Resolution:** The 50% income tax deductibility of entertainment expenses (edustusmenot, per EVL S 8(1)(8)) is COMPLETELY IRRELEVANT for VAT. Entertainment VAT is **FULLY BLOCKED** -- 0% recovery. The EUR 67.50 VAT is an irrecoverable cost. Do NOT be misled by the income tax treatment.
**Legislation:** AVL S 114(1)(4) (full VAT block); EVL S 8(1)(8) (50% income tax deduction -- separate regime).
**Tag:** [T1]

### EC3 -- Rate Increase to 25.5% -- Transitional Invoice [T1]

**Situation:** A Finnish company received an advance payment of EUR 10,000 in August 2024 (before 1 Sep 2024) for a project completed in October 2024. Total contract value EUR 25,000.
**Resolution:** The advance of EUR 10,000 is taxed at the **old rate of 24%** (tax point created at payment). The remaining EUR 15,000 is taxed at the **new rate of 25.5%** (tax point at completion). Two separate output VAT entries may be needed if spanning the transition.
**Legislation:** AVL S 15(1) (tax point); Act 817/2024 transitional provisions.
**Tag:** [T1]

### EC4 -- Construction Reverse Charge: Buyer is a Construction Company [T1]

**Situation:** A construction company (paaurakoitsija, regularly provides construction services) hires a subcontractor for plumbing work. Invoice EUR 50,000.
**Resolution:** Domestic construction RC applies. Subcontractor invoices WITHOUT VAT, noting "AVL 8c kaannetty verovelvollisuus". Buyer: Code 320 = EUR 50,000. Output VAT EUR 12,750 (25.5%) in Code 308. Input VAT EUR 12,750 in Code 307. Net zero.
**Legislation:** AVL S 8c.
**Tag:** [T1]

### EC5 -- Construction Work: Buyer is NOT a Construction Company [T1]

**Situation:** An IT company hires a builder for office renovation. EUR 30,000.
**Resolution:** Construction reverse charge does NOT apply because the buyer (IT company) does not "regularly provide construction services". Builder charges normal 25.5% VAT (EUR 7,650). IT company claims input VAT in Code 307 (if business use).
**Legislation:** AVL S 8c (condition on buyer not met).
**Tag:** [T1]

### EC6 -- SaaS Subscription from US Provider [T1]

**Situation:** Finnish company pays EUR 100/month to a US SaaS provider. No VAT on invoice.
**Resolution:** Import of services from non-EU. Report in Code 319 = EUR 100 (base). Output VAT EUR 25.50 (25.5%) included in Code 308. Input VAT EUR 25.50 in Code 307. Net zero.
**Legislation:** AVL S 9 (reverse charge on non-EU services); AVL S 65 (B2B place of supply).
**Tag:** [T1]

### EC7 -- Hotel in Another EU Country [T1]

**Situation:** Finnish company employee stays at hotel in Estonia. Invoice shows Estonian 22% VAT.
**Resolution:** NOT reverse charge. Estonian VAT was charged at source (place of supply for accommodation is where property is located -- AVL S 67). No Finnish VAT entries. Estonian VAT is an irrecoverable cost.
**Legislation:** AVL S 67 (immovable property place of supply).
**Tag:** [T1]

### EC8 -- Hotel in Finland (Business Trip) [T1]

**Situation:** Employee stays at Finnish hotel. EUR 120 + EUR 12 VAT (10%).
**Resolution:** Input VAT of EUR 12 is **FULLY deductible** (Finland allows hotel VAT deduction for business travel, unlike many EU countries where accommodation VAT is restricted). Code 307 += EUR 12.
**Legislation:** AVL S 102 (general right to deduct); AVL S 85a(1)(3) (10% rate for accommodation).
**Tag:** [T1]

### EC9 -- Passenger Car Purchase: General Business Use [T1]

**Situation:** Company buys a passenger car (henkiloauto) for EUR 40,000 + EUR 10,200 VAT (25.5%). Used by the managing director for business and personal travel.
**Resolution:** Input VAT is **BLOCKED**. Passenger car VAT is not deductible under AVL S 114(1)(5) unless the car is used exclusively in taxi, driving school, or car rental operations. The EUR 10,200 VAT is an irrecoverable cost forming part of the asset's acquisition value.
**Legislation:** AVL S 114(1)(5).
**Tag:** [T1]

### EC10 -- Passenger Car Purchase: Taxi Operator [T1]

**Situation:** Licensed taxi operator purchases a vehicle for EUR 35,000 + EUR 8,925 VAT (25.5%). Used exclusively for taxi services.
**Resolution:** Full input VAT deduction. EUR 8,925 goes to Code 307. Exception to passenger car block applies.
**Legislation:** AVL S 114a(1) (taxi exception).
**Tag:** [T1]

### EC11 -- Goods from Aland to EU Country (Not Mainland Finland) [T2]

**Situation:** Aland-based company sells goods to a customer in Germany.
**Resolution:** Treated as an export from Aland (outside EU VAT territory). Zero-rated in Aland. The German customer must report as an import. Finnish mainland VAT rules do not apply to the Aland seller directly. **Flag for reviewer:** Confirm Aland customs and excise procedures.
**Legislation:** AVL S 68a; Protocol 2.
**Tag:** [T2]

### EC12 -- EU B2B Service Sale [T1]

**Situation:** Finnish company provides IT consulting to a Swedish client (B2B).
**Resolution:** Code 312 (base amount). No output VAT charged. Swedish customer reverse charges in Sweden. Finnish company must file EU Sales List (Yhteenvetoilmoitus).
**Legislation:** AVL S 65 (B2B place of supply in customer country); AVL S 162a (EU Sales List).
**Tag:** [T1]

### EC13 -- Import of Goods from Non-EU (Self-Assessed) [T1]

**Situation:** Finnish company imports goods from China. Customs value EUR 20,000, customs duty EUR 1,000. VAT base = EUR 21,000 (customs value + duty).
**Resolution:** Since 2018, import VAT is declared on the VAT return. Output VAT EUR 5,355 (25.5% of EUR 21,000) in Code 308. Input VAT EUR 5,355 in Code 307. Net zero. The VAT base for imports includes customs duties and transport costs to Finland.
**Legislation:** AVL S 86h, 88 (import VAT base).
**Tag:** [T1]

### EC14 -- Credit Note for Pre-Rate-Change Supply [T1]

**Situation:** In November 2024, a Finnish supplier issues a credit note for EUR 2,000 relating to a supply made in July 2024 (before the rate change).
**Resolution:** The credit note must use the **original rate of 24%**, not the current 25.5%. Output VAT reduction: EUR 480 (24%). The period of the credit note entry is November 2024.
**Legislation:** AVL S 78 (credit notes); Act 817/2024 transitional provisions.
**Tag:** [T1]

### EC15 -- Abolished Small Business Relief -- Claim Attempt [T1]

**Situation:** A small business with EUR 12,000 turnover in 2025 asks to claim alarajahuojennus (graduated small business relief).
**Resolution:** **REFUSED.** Alarajahuojennus was abolished from 1 January 2025 by Act 421/2024. The business may be below the new EUR 15,000 registration threshold and could deregister, but if registered, full VAT obligations apply with no graduated relief.
**Legislation:** AVL S 149a (repealed); Act 421/2024.
**Tag:** [T1]

### EC16 -- VAT Grouping (Verovelvollisuusryhma) [T3]

**Situation:** A financial institution wishes to form a VAT group with its subsidiaries.
**Resolution:** **ESCALATE.** VAT grouping in Finland is available only for financial and insurance sector entities (AVL S 13a-13c). Complex rules on scope, eligibility, and internal supply treatment. Refer to qualified adviser.
**Legislation:** AVL S 13a-13c.
**Tag:** [T3]

---

## Section 9: Test Suite

### Test 1 -- Standard Domestic Purchase, 25.5% VAT [T1]

**Input:** Finnish supplier, office equipment, EUR 1,000 net + EUR 255 VAT. Client is VAT-registered.
**Expected output:** Code 307 += EUR 255. Fully deductible. No output field entries for this purchase.
**Legislation:** AVL S 84 (rate), S 102 (deduction right).

### Test 2 -- Import of Services from US (SaaS) [T1]

**Input:** US supplier, monthly fee EUR 50, no VAT. Client is VAT-registered.
**Expected output:** Code 319 = EUR 50. Output VAT EUR 12.75 (25.5%) included in Code 308. Code 307 += EUR 12.75. Net = zero.
**Legislation:** AVL S 9 (RC), S 65 (place of supply), S 84 (rate).

### Test 3 -- Intra-EU Goods Acquisition [T1]

**Input:** Swedish supplier, goods EUR 5,000 at 0% with SE VAT number.
**Expected output:** Code 309 = EUR 5,000. Output VAT EUR 1,275 (25.5%) included in Code 308. Code 307 += EUR 1,275. Net = zero. EU Sales List entry for the Swedish supplier.
**Legislation:** AVL S 26a (acquisition), S 8a (RC), S 84 (rate).

### Test 4 -- Entertainment Dinner (BLOCKED) [T1]

**Input:** Client entertainment dinner EUR 150 + EUR 20.25 VAT (13.5%). Client is VAT-registered.
**Expected output:** Code 307 += EUR 0. **BLOCKED.** Full EUR 170.25 is cost. Despite 50% income tax deductibility, VAT recovery is zero.
**Legislation:** AVL S 114(1)(4) (block); EVL S 8(1)(8) (income tax -- irrelevant for VAT).

### Test 5 -- Construction Reverse Charge (Buyer is Construction Company) [T1]

**Input:** Subcontractor invoices construction company EUR 30,000 (no VAT, citing AVL S 8c). Buyer regularly provides construction services.
**Expected output:** Code 320 = EUR 30,000. Output VAT EUR 7,650 (25.5%) in Code 308. Code 307 += EUR 7,650. Net = zero.
**Legislation:** AVL S 8c.

### Test 6 -- EU B2B Service Sale [T1]

**Input:** Finnish company invoices Danish client EUR 2,000 for consulting. B2B. Danish client is VAT-registered.
**Expected output:** Code 312 = EUR 2,000. No output VAT. EU Sales List (Yhteenvetoilmoitus) required.
**Legislation:** AVL S 65 (place of supply), S 162a (EU Sales List).

### Test 7 -- Hotel in Finland (Deductible) [T1]

**Input:** Business hotel EUR 100 + EUR 10 VAT (10%). Client is VAT-registered.
**Expected output:** Code 307 += EUR 10. Fully deductible.
**Legislation:** AVL S 85a(1)(3) (rate), S 102 (deduction right).

### Test 8 -- Import of Goods (Self-Assessed on Return) [T1]

**Input:** US supplier, goods EUR 8,000. Customs duty EUR 400. Transport to Finland EUR 200. VAT base = EUR 8,600. Import declared on VAT return.
**Expected output:** Output VAT EUR 2,193 (25.5% of EUR 8,600) in Code 308. Code 307 += EUR 2,193. Net = zero.
**Legislation:** AVL S 86h (self-assessment), S 88 (VAT base for imports).

### Test 9 -- Passenger Car Purchase (Blocked) [T1]

**Input:** Passenger car EUR 30,000 + EUR 7,650 VAT (25.5%). General business use (not taxi/driving school/rental). Client is VAT-registered.
**Expected output:** Code 307 += EUR 0. **BLOCKED** under AVL S 114(1)(5). EUR 37,650 is total cost of the asset.
**Legislation:** AVL S 114(1)(5).

### Test 10 -- Rate Transition: Advance Payment Spanning 1 Sep 2024 [T1]

**Input:** Advance payment of EUR 5,000 received 15 Aug 2024. Remaining EUR 15,000 invoiced when project completed 20 Oct 2024. Total EUR 20,000.
**Expected output:** August 2024: Code 301 (24% base) = EUR 5,000, Code 305 = EUR 1,200 (24%). October 2024: Code 301 (25.5% base) = EUR 15,000, Code 305 = EUR 3,825 (25.5%). Two separate entries at different rates.
**Legislation:** AVL S 15(1) (tax point); Act 817/2024 transitional provisions.

### Test 11 -- Goods from Aland Islands to Mainland [T1]

**Input:** Finnish mainland company purchases goods EUR 3,000 from Aland Islands supplier.
**Expected output:** Import treatment. Output VAT EUR 765 (25.5%) in Code 308. Code 307 += EUR 765. Net = zero. Treat as import despite both parties being in Finland.
**Legislation:** AVL S 68a; Protocol 2.

### Test 12 -- Abolished Alarajahuojennus for 2025 Period [T1]

**Input:** Small business, turnover EUR 12,000 in 2025, VAT-registered. Asks for alarajahuojennus.
**Expected output:** **REFUSED.** Relief abolished from 1 January 2025. No graduated relief. Full VAT obligations apply. Business may consider deregistering (below EUR 15,000 threshold).
**Legislation:** AVL S 149a (repealed by Act 421/2024).

---

## Section 10: Comparison with Malta VAT System

### 10.1 Structural Comparison [T1]

| Feature | Finland (FI) | Malta (MT) |
|---------|-------------|------------|
| **Primary legislation** | Arvonlisaverolaki (AVL) 1501/1993 | VAT Act Chapter 406 |
| **Tax authority** | Verohallinto (Finnish Tax Administration) | Commissioner for Revenue (CFR) |
| **Filing portal** | OmaVero (online only) | cfr.gov.mt (online or paper) |
| **Return form** | ALV-ilmoitus (single-page, code-based) | VAT3 (multi-box form with 45+ boxes) |
| **Standard rate** | **25.5%** (from 1 Sep 2024) | **18%** |
| **Reduced rates** | 13.5% (from 1 Jan 2026; was 14%), 10% | 12%, 7%, 5% |
| **Zero rate** | Exports, intra-EU supplies | Exports, intra-EU supplies, certain food |
| **Registration threshold** | EUR 15,000 (from 1 Jan 2025) | EUR 35,000 (Article 11 exemption) |
| **Small business relief** | Abolished (alarajahuojennus repealed 2025) | Article 11 annual declaration (simplified) |
| **Input VAT structure** | **Single field** (Code 307 -- one total) | **Multiple boxes** (34-38 by category/rate) |
| **Capital goods scheme** | 10-year adjustment for immovable property only | EUR 1,160 gross threshold, covers all assets |
| **Filing frequency** | Monthly / Quarterly / Annual | Quarterly (Art 10) / Annual (Art 11) / Monthly (Art 12) |
| **Monthly filing deadline** | 12th of M+2 (very generous) | 15th of M+1 (Art 12) or 21st of Q+1 (Art 10) |
| **Import VAT** | Self-assessed on VAT return (since 2018) | Paid at customs (C88 document) |
| **Construction RC** | Yes (AVL S 8c -- buyer must be construction industry) | No domestic reverse charge |
| **VAT grouping** | Limited to financial/insurance sector (AVL S 13a) | Available more broadly |

### 10.2 Deductibility Comparison [T1]

| Expense Category | Finland Recovery | Malta Recovery | Notes |
|-----------------|-----------------|----------------|-------|
| Entertainment (edustusmenot) | **0% -- FULLY BLOCKED** (AVL S 114(1)(4)) | **0% -- BLOCKED** (10th Sch Item 3(1)(b)) | Both block; Finland has the income tax 50% trap |
| Motor vehicles (passenger cars) | **0% -- BLOCKED** with exceptions (taxi, driving school, rental) (AVL S 114(1)(5), 114a) | **0% -- BLOCKED** with exceptions (taxi, delivery, rental) (10th Sch Item 3(1)(a)(iv-v)) | Similar approach; different exception lists |
| Hotel / accommodation | **100% deductible** (AVL S 102) | **100% deductible** | Both allow; unusual in EU |
| Fuel (business vehicle) | **100% if vehicle not blocked** (AVL S 102) | **100% if vehicle not blocked** | Follows vehicle status |
| Alcohol | **100% deductible** (if not entertainment) | **0% -- BLOCKED** (10th Sch Item 3(1)(a)(ii)) | **KEY DIFFERENCE**: Finland does not block alcohol per se (only entertainment); Malta blocks all alcohol |
| Tobacco | **100% deductible** (if business stock) | **0% -- BLOCKED** (10th Sch Item 3(1)(a)(i)) | **KEY DIFFERENCE**: Finland does not block tobacco per se; Malta blocks all tobacco |

### 10.3 Filing Process Comparison [T1]

| Aspect | Finland | Malta |
|--------|---------|-------|
| Submission method | OmaVero electronic only | cfr.gov.mt electronic or paper |
| Payment method | Bank transfer via OmaVero reference | Bank transfer or CFR portal |
| Automatic refund | Yes -- excess input VAT refunded automatically | Must apply; offset against future periods |
| Correction method | Replacement return via OmaVero (3-year window) | Corrective return via cfr.gov.mt |
| EU Sales List | Monthly, same deadline as VAT return | Quarterly with VAT3 |

---

## Section 11: PROHIBITIONS [T1]

These are absolute rules that must NEVER be violated. Each is tagged [T1] -- deterministic, no exceptions.

1. **NEVER let AI guess ALV field assignment** -- it is 100% deterministic from transaction facts. **Legislation:** AVL S 162.
2. **NEVER claim input VAT on entertainment or representation expenses (edustusmenot)** -- FULLY BLOCKED regardless of income tax treatment. **Legislation:** AVL S 114(1)(4). [T1]
3. **NEVER apply the old 24% rate to supplies made on or after 1 September 2024** -- standard rate is 25.5%. **Legislation:** Act 817/2024. [T1]
4. **NEVER apply construction reverse charge (AVL S 8c) when the buyer is NOT in the construction industry** -- the buyer must regularly provide construction services. **Legislation:** AVL S 8c. [T1]
5. **NEVER apply reverse charge to out-of-scope categories** (salaries, dividends, loan repayments, income tax payments). [T1]
6. **NEVER apply reverse charge to local consumption services abroad** (hotel, restaurant, taxi booked in another country) -- foreign VAT was paid at source and is irrecoverable. [T1]
7. **NEVER allow non-registered entities to claim input VAT.** **Legislation:** AVL S 102. [T1]
8. **NEVER apply the abolished small business relief (alarajahuojennus)** for periods from 1 January 2025 onward. **Legislation:** AVL S 149a (repealed by Act 421/2024). [T1]
9. **NEVER treat Aland Islands as domestic for goods movements** -- import/export VAT treatment required. **Legislation:** AVL S 68a; Protocol 2 to EU Accession Treaty. [T1]
10. **NEVER compute any number** -- all arithmetic is handled by the deterministic engine, not the AI. [T1]
11. **NEVER apply VAT deduction to passenger car purchases/leases** unless the car is used exclusively for taxi, driving school, or car rental operations. **Legislation:** AVL S 114(1)(5), 114a. [T1]
12. **NEVER confuse the 50% income tax deductibility of entertainment with VAT deductibility** -- they are separate regimes; VAT is always 0%. **Legislation:** AVL S 114(1)(4) vs. EVL S 8(1)(8). [T1]
13. **NEVER apply a proposed/pending rate change until it is enacted into law** -- verify legislative status before using any future rate. [T1]
14. **NEVER reverse charge when an EU supplier has charged their local VAT on the invoice** -- foreign VAT is embedded in the cost; no Finnish VAT entries. [T1]
15. **NEVER apply the EUR 15,000 registration threshold retroactively** to periods before 1 January 2025 (prior threshold was EUR 10,000). **Legislation:** AVL S 3; Act 421/2024. [T1]

---

## Section 12: Reviewer Escalation Protocol

### 12.1 Tier 2 Flag Template [T2]

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Legislation: [AVL section(s)]
Action Required: KHT/HT auditor or veroasiantuntija must confirm before filing.
```

### 12.2 Tier 3 Escalation Template [T3]

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Legislation: [AVL section(s) if known]
Action Required: Do not classify. Refer to qualified adviser. Document gap.
```

---

## Section 13: Capital Goods Adjustment (Kiinteiston tarkistusmenettely)

### 13.1 Immovable Property Adjustment [T2]

**Legislation:** AVL S 119-121.

Finland applies a capital goods adjustment scheme **only for immovable property** (kiinteisto):

| Parameter | Value | AVL Section |
|-----------|-------|-------------|
| Adjustment period | **10 years** (new construction or major renovation) | AVL S 121 |
| Starting point | Year of completion or acquisition | AVL S 121(1) |
| Trigger | Change in use between taxable and exempt, or change in pro-rata percentage | AVL S 119 |
| Minimum adjustment | If change in deduction entitlement > 10 percentage points | AVL S 121e |
| Annual adjustment | 1/10 of original VAT per year for remaining adjustment period | AVL S 121a |

**Note:** Unlike Malta, Finland does NOT have a general capital goods scheme for movable property (no EUR 1,160 or similar threshold). Movable assets are fully deducted at purchase with no subsequent adjustment obligation. [T1] **Legislation:** AVL S 102.

**Flag for reviewer [T2]:** If immovable property changes use during the 10-year adjustment period, confirm annual adjustment calculation.

---

## Section 14: Special Sectors and Rate Application

### 14.1 Food and Restaurant Services -- 13.5% Rate [T1]

**Legislation:** AVL S 85(1)(1-2). Rate reduced from 14% to 13.5% effective 1 January 2026.

| Supply | Rate | Field (Base) | Field (Tax) | Notes |
|--------|------|-------------|-------------|-------|
| Food for human consumption (elintarvikkeet) | 13.5% | 302 | 306 | Excludes live animals, water supply |
| Animal feed (rehut) | 13.5% | 302 | 306 | Feed for food-producing and pet animals |
| Restaurant and catering services (ravintola- ja ateriapalvelut) | 13.5% | 302 | 306 | Excludes alcoholic beverages served at standard rate |
| Alcoholic beverages in restaurant | **25.5%** | 301 | 305 | Even when served with food |
| Takeaway food | 13.5% | 302 | 306 | Same as restaurant |

### 14.2 Books, Publications, and Media -- 10% Rate [T1]

**Legislation:** AVL S 85a(1)(7-8).

| Supply | Rate | Notes |
|--------|------|-------|
| Physical books | 10% | Printed books |
| E-books | 10% | Electronic books (from 2019) |
| Audiobooks | 10% | Digital audio publications |
| Newspapers (sanomalehtdet) | 10% | Physical and electronic subscriptions |
| Periodicals (aikakauslehdet) | 10% | Physical and electronic subscriptions |

### 14.3 Healthcare and Medicines [T1]

**Legislation:** AVL S 34-36 (healthcare exemption), S 85a(1)(6) (medicines 10%).

| Supply | Rate | Notes |
|--------|------|-------|
| Healthcare services (terveydenhuoltopalvelut) | **Exempt** | No VAT; no input credit |
| Prescription medicines (reseptilaakkeet) | **10%** | Sold by pharmacies |
| Non-prescription medicines (itsehoitolaakkeet) | **10%** | OTC medicines |
| Medical devices | **25.5%** | Standard rate unless specifically listed |

### 14.4 Transport and Accommodation [T1]

**Legislation:** AVL S 85a(1)(1, 3).

| Supply | Rate | Notes |
|--------|------|-------|
| Passenger transport (henkilokuljetukset) | **10%** | Bus, train, taxi, domestic flights |
| Accommodation (majoituspalvelut) | **10%** | Hotels, hostels, short-term rental |
| Freight transport | **25.5%** | Standard rate |
| International passenger transport | **0%** | Zero-rated (AVL S 71) |

---

## Contribution Notes

This skill was fully rewritten based on publicly available information about Finland's VAT system as of April 2026. Key Finland-specific features covered include:

- The September 2024 standard rate increase from 24% to 25.5% (Act 817/2024)
- The increase of the registration threshold to EUR 15,000 (Act 421/2024)
- The abolition of the small business relief (alarajahuojennus) from 2025
- The Aland Islands' special status outside EU VAT territory for goods
- The entertainment expense trap (0% VAT despite 50% income tax deduction)
- The construction-specific domestic reverse charge (AVL S 8c)
- The passenger car VAT block with statutory exceptions for taxi/driving school/rental
- The single input VAT field (Code 307)
- The self-assessment of import VAT on the return (since 2018)
- The generous filing deadline (12th of M+2)

Rate data was verified against PWC Tax Summaries (taxsummaries.pwc.com/finland/corporate/other-taxes).

This skill requires validation by a qualified Finnish KHT or HT auditor, or veroasiantuntija before use.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
