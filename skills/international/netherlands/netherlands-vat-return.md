---
name: netherlands-vat-return
description: Use this skill whenever asked to prepare, review, or create a Netherlands VAT return (OB aangifte / btw-aangifte) or KOR declaration for any client. Trigger on phrases like "prepare VAT return", "do the BTW", "fill in OB aangifte", "create the return", "Dutch VAT", "Netherlands VAT", "KOR declaration", or any request involving Netherlands VAT filing. Also trigger when classifying transactions for BTW purposes from bank statements, invoices, or other source data. This skill contains the complete Netherlands BTW classification rules, box mappings (rubrieken), BUA blocked deductions, reverse charge treatment (verleggingsregeling), margin scheme (margeregeling), private use corrections (privegebruik), and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Netherlands VAT-related work.
---

# Netherlands VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Netherlands |
| Jurisdiction Code | NL |
| Primary Legislation | Wet op de omzetbelasting 1968 (Wet OB 1968 / Dutch VAT Act) |
| Supporting Legislation | Uitvoeringsbesluit omzetbelasting 1968 (Implementation Decree); Besluit Uitsluiting Aftrek omzetbelasting 1968 (BUA); Uitvoeringsbeschikking omzetbelasting 1968 |
| Tax Authority | Belastingdienst (Dutch Tax and Customs Administration) |
| Filing Portal | https://www.belastingdienst.nl (Mijn Belastingdienst Zakelijk) |
| Contributor | [Awaiting contributor -- must be a Dutch belastingadviseur or AA/RA accountant] |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 2.1 |
| Confidence Coverage | Tier 1: rubriek assignment, reverse charge, BUA blocks, derived calculations, KOR eligibility. Tier 2: partial exemption pro-rata, sector-specific deductibility, margin scheme elections, Article 23 deferral. Tier 3: complex group structures, fiscal unity (fiscale eenheid), real estate VAT option (optie belaste verhuur). |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A registered belastingadviseur must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to belastingadviseur and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and BTW-identificatienummer (btw-id)** [T1] -- Format: NL + 9 digits + B + 2-digit suffix (e.g., NL123456789B01)
2. **KVK number** [T1] -- Kamer van Koophandel registration number (8 digits)
3. **VAT registration type** [T1] -- Standard (reguliere ondernemer), KOR (Kleineondernemersregeling), or Fiscal Unity (fiscale eenheid)
4. **Filing frequency** [T1] -- Monthly (maandelijks), quarterly (per kwartaal), or annual (jaarlijks) -- assigned by Belastingdienst
5. **Industry/sector** [T2] -- Impacts BUA corrections and domestic reverse charge (e.g., hospitality, construction, staffing)
6. **Does the business make exempt supplies (vrijgestelde prestaties)?** [T2] -- If yes, partial attribution required (pro-rata rate needed; reviewer must confirm rate)
7. **Does the business trade in second-hand goods?** [T2] -- Impacts margin scheme (margeregeling) election
8. **Does the business have an Article 23 permit (vergunning)?** [T1] -- Import VAT deferral
9. **Does the business provide company cars to employees?** [T1] -- Impacts private use correction (privegebruik correctie)
10. **BUA correction amount from prior year** [T1] -- For reference in year-end correction

For KOR clients [T1]: also confirm turnover was below EUR 20,000 in both the current and prior calendar year.

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until registration type and filing frequency are confirmed.**

---

## SECTION 1: VAT Return Form Structure (OB Aangifte / Aangifte Omzetbelasting) [T1]

**Legislation:** Wet OB 1968; Belastingdienst OB aangifte toelichting (explanatory notes).
**Filing method:** Filed electronically via Mijn Belastingdienst Zakelijk portal (https://www.belastingdienst.nl).

The Dutch VAT return (aangifte omzetbelasting) is divided into 5 sections with 17 rubrieken (fields). Each rubriek that reports taxable supplies has two columns: turnover (omzet, excl. VAT) and VAT amount (omzetbelasting).

### Section 1: Prestaties binnenland (Domestic Supplies)

| Rubriek | Dutch Name | English Translation | What Transactions Go Here | Columns |
|---------|-----------|---------------------|---------------------------|---------|
| **1a** | Leveringen/diensten belast met hoog tarief | Supplies/services taxed at standard rate | All domestic sales of goods and services subject to 21% VAT. Includes margin scheme VAT at 21%. | Turnover + VAT |
| **1b** | Leveringen/diensten belast met laag tarief | Supplies/services taxed at reduced rate | All domestic sales of goods and services subject to 9% VAT (Tabel I categories: food, water, medicines, books, newspapers, hairdressing, minor repairs, cultural/sports events, camping). Includes margin scheme VAT at 9%. | Turnover + VAT |
| **1c** | Leveringen/diensten belast met overige tarieven | Supplies/services taxed at other rates | Domestic sales at any rate other than 21% or 9%. Currently rarely used; exists for transitional provisions or future rate changes. | Turnover + VAT |
| **1d** | Privegebruik | Private use | Annual correction for private use of business goods/services. Reported only in the last VAT return of the calendar year. Includes company car private use correction (2.7% of catalogue value or alternative). | Turnover + VAT |
| **1e** | Leveringen/diensten belast met 0% of niet bij u belast | Supplies/services at 0% or not taxed by you | Zero-rated domestic supplies, exempt supplies (vrijgesteld), and domestic supplies where VAT is reverse-charged to the customer (supplier reports here with "btw verlegd"). | Turnover only |

### Section 2: Verleggingsregelingen binnenland (Domestic Reverse Charge)

| Rubriek | Dutch Name | English Translation | What Transactions Go Here | Columns |
|---------|-----------|---------------------|---------------------------|---------|
| **2a** | Leveringen/diensten waarbij de omzetbelasting naar u is verlegd | Supplies/services where VAT has been reverse-charged to you | As the RECIPIENT: domestic purchases where the supplier applied the verleggingsregeling (construction, staffing in construction, scrap metal, mobile phones/chips >= EUR 10,000, emission rights). You self-assess VAT here. | Turnover + VAT |

### Section 3: Prestaties naar het buitenland (Supplies to Foreign Countries)

| Rubriek | Dutch Name | English Translation | What Transactions Go Here | Columns |
|---------|-----------|---------------------|---------------------------|---------|
| **3a** | Leveringen naar landen buiten de EU (uitvoer) | Supplies to countries outside the EU (exports) | Exports of goods to non-EU countries. Requires proof of export (customs declaration, CMR, bill of lading). Also: certain services to non-EU recipients where place of supply is outside EU. | Turnover only |
| **3b** | Leveringen naar/diensten in landen binnen de EU | Supplies to/services in EU countries | Intra-EU supplies of goods to VAT-registered businesses in other EU member states (intracommunautaire leveringen). Also: B2B services where place of supply is in another EU member state (Article 6 reverse charge). Must verify customer btw-id via VIES. Must match ICP declaration. | Turnover only |
| **3c** | Installatie/afstandsverkopen binnen de EU | Installation/distance sales within the EU | Installation supplies where goods are assembled/installed in another EU member state. Distance sales to consumers in other EU member states (if OSS is not used). | Turnover only |

### Section 4: Prestaties vanuit het buitenland (Supplies from Foreign Countries)

| Rubriek | Dutch Name | English Translation | What Transactions Go Here | Columns |
|---------|-----------|---------------------|---------------------------|---------|
| **4a** | Leveringen/diensten uit landen buiten de EU | Supplies/services from countries outside the EU | Services received from non-EU suppliers (reverse charge -- self-assess NL VAT). Also: imports of goods with Article 23 permit (import VAT deferral). | Turnover + VAT |
| **4b** | Leveringen/diensten uit landen binnen de EU | Supplies/services from EU countries | Intra-EU acquisitions of goods (intracommunautaire verwervingen). Also: B2B services received from EU suppliers where place of supply is NL (reverse charge). Self-assess NL VAT. | Turnover + VAT |

### Section 5: Berekening (Calculation)

| Rubriek | Dutch Name | English Translation | Calculation / What Goes Here |
|---------|-----------|---------------------|------------------------------|
| **5a** | Verschuldigde omzetbelasting (subtotaal) | Output VAT payable (subtotal) | Sum of ALL VAT amounts from: 1a + 1b + 1c + 1d + 2a + 4a + 4b |
| **5b** | Voorbelasting | Input VAT (deductible) | Total deductible input VAT from: purchase invoices (NL suppliers), self-assessed VAT on reverse charge (matching 2a, 4a, 4b where deductible), import VAT from customs declarations (non-Art 23), MINUS BUA corrections and partial exemption adjustments |
| **5c** | Subtotaal | Subtotal | 5a minus 5b. Positive = VAT payable. Negative = VAT refundable. |
| **5d** | Vermindering volgens de kleineondernemersregeling | KOR deduction | Old KOR scheme only (pre-2020). Current KOR participants do not file returns at all. For legacy cases only. |
| **5e** | Schatting vorige aangifte(n) | Estimate from previous return(s) | Only used when authorized by Belastingdienst to file estimated returns. Correction of prior estimate. |
| **5f** | Schatting deze aangifte | Estimate for this return | Only used when authorized by Belastingdienst to file estimated returns. |
| **5g** | Totaal | Total payable/refundable | **5g = 5c - 5d - 5e + 5f**. Positive = amount to pay. Negative = amount refundable. This is the final amount. |

### Derived Calculation Summary [T1]

```
Box 5a = VAT(1a) + VAT(1b) + VAT(1c) + VAT(1d) + VAT(2a) + VAT(4a) + VAT(4b)

Box 5b = Total deductible input VAT from purchase invoices
       + Self-assessed VAT from 2a (if deductible)
       + Self-assessed VAT from 4a (if deductible)
       + Self-assessed VAT from 4b (if deductible)
       + Import VAT from customs declarations (non-Art 23, if deductible)
       - BUA corrections (last return of year only)
       - Partial exemption adjustments (if applicable)

Box 5c = Box 5a - Box 5b

Box 5d = KOR deduction (old scheme; normally EUR 0)

Box 5e = Prior period estimate correction (normally EUR 0)

Box 5f = Current period estimate (normally EUR 0)

Box 5g = Box 5c - Box 5d - Box 5e + Box 5f
         Positive = PAY to Belastingdienst
         Negative = REFUND from Belastingdienst
```

**Note:** Rubrieken 3a, 3b, and 3c are informational only (turnover, no VAT column feeds into 5a). They provide data for the ICP declaration and export verification but do not affect the VAT payable/refundable calculation.

---

## SECTION 2: Transaction Classification Matrix [T1]

**Legislation:** Wet OB 1968, Articles 1-6 (taxable supplies, place of supply), Article 9 (rates), Article 12 (domestic reverse charge), Article 17b (intra-EU acquisitions), Article 23 (import deferral).

### 2a. Determine Transaction Type [T1]

- Sale (output VAT / verschuldigde btw) or Purchase (input VAT / voorbelasting)
- Salaries, pension contributions, income tax payments, loan repayments, dividends, bank charges = OUT OF SCOPE (never on VAT return)
- **Legislation:** Wet OB 1968, Articles 1-4 (definition of taxable supply)

### 2b. Determine Counterparty Location [T1]

- Netherlands (domestic / binnenland): supplier/customer is NL
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else (US, UK, AU, CH, NO, etc.)
- **Note:** UK is Non-EU post-Brexit. Norway and Switzerland are Non-EU. Canary Islands, Ceuta, Melilla, Mount Athos, Aland Islands are Non-EU for VAT purposes.

### 2c. Determine VAT Rate [T1]

- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Normalize to nearest standard rate: 0%, 9%, 21%
- Boundaries: <= 1% = 0%; 1-15% = 9%; >= 15% = 21%
- **Legislation:** Wet OB 1968, Article 9; Tabel I; Tabel II

### 2d. Determine Supply Type [T1]

- Goods (goederen): tangible, movable property
- Services (diensten): everything that is not a supply of goods
- Immovable property: [T3] -- complex rules, always escalate
- **Legislation:** Wet OB 1968, Articles 3 (goods) and 4 (services)

### Purchases -- Domestic (NL Supplier)

| Scenario | Reverse Charge? | Output Rubriek | Input Rubriek | Notes |
|----------|----------------|----------------|---------------|-------|
| Standard purchase at 21% | No | -- | 5b (VAT from invoice) | Normal deduction |
| Reduced rate purchase at 9% | No | -- | 5b (VAT from invoice) | Normal deduction |
| Construction subcontractor ("btw verlegd") | Yes (domestic) | 2a (turnover + self-assessed VAT) | 5b (same VAT if deductible) | Art. 12(4) Wet OB |
| Staffing in construction ("btw verlegd") | Yes (domestic) | 2a (turnover + self-assessed VAT) | 5b (same VAT if deductible) | Art. 12(4) Wet OB |
| Scrap metal / waste ("btw verlegd") | Yes (domestic) | 2a (turnover + self-assessed VAT) | 5b (same VAT if deductible) | Art. 12(3) Wet OB |
| Mobile phones/chips >= EUR 10,000 invoice ("btw verlegd") | Yes (domestic) | 2a (turnover + self-assessed VAT) | 5b (same VAT if deductible) | Art. 12(3) Wet OB |
| Emission rights (CO2) ("btw verlegd") | Yes (domestic) | 2a (turnover + self-assessed VAT) | 5b (same VAT if deductible) | Art. 12(3) Wet OB |
| Real estate with option to tax ("btw verlegd") | Yes (domestic) | 2a (turnover + self-assessed VAT) | 5b (same VAT if deductible) | Art. 12(4) Wet OB |
| Zero-rated or exempt purchase | No | -- | -- | No VAT to recover |

### Purchases -- EU Supplier

| Scenario | Reverse Charge? | Output Rubriek | Input Rubriek | Notes |
|----------|----------------|----------------|---------------|-------|
| Goods from EU (intracommunautaire verwerving) | Yes (cross-border) | 4b (turnover + self-assessed VAT at NL rate) | 5b (same VAT if deductible) | Art. 17b Wet OB |
| B2B services from EU (place of supply NL) | Yes (cross-border) | 4b (turnover + self-assessed VAT at NL rate) | 5b (same VAT if deductible) | Art. 6(1) Wet OB |
| Local consumption abroad (hotel, restaurant, taxi) | No | -- | -- | Foreign VAT paid at source; not recoverable via NL return |
| EU supplier charged their local VAT > 0% | No | -- | -- | Not reverse charge; seek refund via 8th Directive if applicable |

### Purchases -- Non-EU Supplier

| Scenario | Reverse Charge? | Output Rubriek | Input Rubriek | Notes |
|----------|----------------|----------------|---------------|-------|
| Services from non-EU (reverse charge) | Yes (cross-border) | 4a (turnover + self-assessed VAT at NL rate) | 5b (same VAT if deductible) | Art. 6(1) Wet OB |
| Goods import -- WITH Article 23 permit | Yes (import deferral) | 4a (customs value + duties + self-assessed VAT) | 5b (same VAT if deductible) | Art. 23 Wet OB |
| Goods import -- WITHOUT Article 23 permit | No (VAT paid at customs) | -- | 5b (VAT from customs declaration if deductible) | Art. 18 Wet OB |
| Local consumption abroad | No | -- | -- | Foreign VAT paid at source |

### Sales -- Domestic

| Scenario | Output Rubriek | VAT Rate | Notes |
|----------|---------------|----------|-------|
| Sale of goods/services at standard rate | 1a (turnover + VAT) | 21% | Art. 9(1) Wet OB |
| Sale of goods/services at reduced rate | 1b (turnover + VAT) | 9% | Tabel I Wet OB |
| Sale at other rate | 1c (turnover + VAT) | Other | Rarely used |
| Zero-rated supply | 1e (turnover only) | 0% | Tabel II Wet OB |
| Exempt supply (vrijgesteld) | 1e (turnover only) | N/A | Art. 11 Wet OB; no input VAT recovery |
| Supply with domestic reverse charge to customer | 1e (turnover only) | N/A | Supplier invoices "btw verlegd" |
| Private use correction (year-end) | 1d (turnover + VAT) | 21% or 9% | Art. 4(2) Wet OB; last return only |

### Sales -- EU

| Scenario | Output Rubriek | Notes |
|----------|---------------|-------|
| Intra-EU supply of goods (valid btw-id, proof of transport) | 3b (turnover only) | Art. 9(2)(b) Wet OB; Tabel II post a6; must verify via VIES; must report on ICP |
| Intra-EU B2B services (place of supply in customer's MS) | 3b (turnover only) | Art. 6(1) Wet OB; customer applies reverse charge |
| Installation/distance sales in EU | 3c (turnover only) | Art. 5a Wet OB; or OSS if applicable |
| B2C services (place of supply NL) | 1a or 1b (turnover + NL VAT) | NL VAT applies; consider OSS for B2C digital services |

### Sales -- Non-EU

| Scenario | Output Rubriek | Notes |
|----------|---------------|-------|
| Export of goods (with proof of export) | 3a (turnover only) | Zero-rated; Tabel II Wet OB |
| B2B services to non-EU (place of supply outside NL) | 3a or 1e (turnover only) | Depends on place of supply rules; Art. 6 Wet OB |
| B2C services (place of supply NL) | 1a or 1b (turnover + NL VAT) | NL VAT applies |

---

## SECTION 3: VAT Rates [T1]

**Legislation:** Wet OB 1968, Article 9 (rates); Tabel I (reduced rate); Tabel II (zero rate); Article 11 (exemptions).

### Standard Rate: 21% (Algemeen tarief)

**Legal basis:** Wet OB 1968, Article 9(1).

Applies to all supplies of goods and services that are not zero-rated, reduced-rated, or exempt.

### Reduced Rate: 9% (Verlaagd tarief)

**Legal basis:** Wet OB 1968, Article 9(2)(a); Tabel I.

| Category | Examples | Tabel I Reference |
|----------|----------|-------------------|
| Food and non-alcoholic beverages | Groceries, food products, restaurant meals (food component at 9%; alcoholic drinks at 21%). Note: the 2026 accommodation rate increase to 21% does NOT affect restaurant food, which remains at 9%. | Tabel I, post a1 |
| Water | Tap water supply | Tabel I, post a2 |
| Medicines | Pharmaceutical products for human use | Tabel I, post a3 |
| Medical aids | Prostheses, hearing aids, orthopaedic shoes | Tabel I, post a4 |
| Books, newspapers, magazines | Physical and digital (e-publications from 2020) | Tabel I, post a29/a30 |
| Passenger transport | Bus, train, taxi, domestic flights | Tabel I, post b9 |
| Hairdressing | Hairdressing services | Tabel I, post b14 |
| Minor repairs | Repair of bicycles, shoes, leather goods, clothing, household linen | Tabel I, post b15 |
| Cultural and recreational services | Museums, theatre, cinema, concerts, zoos, amusement parks, circuses | Tabel I, post b14 |
| Sports | Providing sports facilities (non-profit and commercial) | Tabel I, post b3 |
| Camping accommodation | Campsite pitches and tent/caravan rental on campsites | Tabel I, post b11 |
| Lending of books | Library lending services | Tabel I, post b12 |
| Agricultural inputs | Seeds, bulbs, plants for food production | Tabel I, post a8 |
| Energy-saving insulation | Insulation materials and installation for private dwellings (labour component) | Tabel I, post b20 |

**2026 rate change:** As of 1 January 2026, accommodation (hotels, B&Bs, holiday homes, hostels, furnished mobile homes, platform rentals) moved from 9% to 21%. Exception: camping accommodation remains at 9%. [T1]

**2025 rate change:** As of 1 January 2025, certain agricultural goods (cereals not for food, seedlings, livestock feed, straw, flax, wool) moved from 9% to 21%. [T1]

### Zero Rate: 0% (Nultarief)

**Legal basis:** Wet OB 1968, Article 9(2)(b); Tabel II.

| Category | Condition | Tabel II Reference |
|----------|-----------|-------------------|
| Exports to non-EU | Proof of export required (customs declaration, CMR, bill of lading) | Tabel II, post a1 |
| Intra-EU B2B supply of goods | Valid btw-id of customer verified via VIES; proof of transport | Tabel II, post a6 |
| International transport | Transport of goods/persons across NL border | Tabel II, post b1 |
| Seagoing vessels | Supply, repair, maintenance of seagoing vessels | Tabel II, post a3 |
| Aircraft for international use | Supply, repair, maintenance of aircraft used by airlines operating international routes | Tabel II, post a4 |
| Gold to central banks | Supply of gold to De Nederlandsche Bank or other central banks | Tabel II, post a7 |
| Solar panels on dwellings | Supply and installation of solar panels on or near private dwellings | Tabel II (since 1 Jan 2023) |

**Key distinction:** Zero-rated supplies allow FULL input VAT recovery. This differs fundamentally from exempt supplies where input VAT is NOT recoverable.

### Exempt: No VAT (Vrijgesteld)

**Legal basis:** Wet OB 1968, Article 11.

| Category | Examples | Article 11 Reference |
|----------|----------|---------------------|
| Healthcare | Doctors, dentists, physiotherapists, psychologists, midwives (BIG-registered professions) | Art. 11(1)(g) |
| Education | Schools, universities, accredited vocational training (not unaccredited commercial training) | Art. 11(1)(o) |
| Financial services | Banking, credit, payment services, securities trading | Art. 11(1)(i) |
| Insurance | Insurance and reinsurance transactions | Art. 11(1)(j) |
| Immovable property letting | Residential rental (no option to tax); commercial letting (exempt unless lessor and lessee opt into VAT jointly) | Art. 11(1)(b) |
| Postal services | Universal postal services by designated operator (PostNL universal service) | Art. 11(1)(l) |
| Social/cultural services | Childcare, elderly care, social welfare organizations | Art. 11(1)(f) |
| Non-profit sports | Sports services by non-profit organizations to members | Art. 11(1)(e) |
| Gambling | Games of chance, lotteries | Art. 11(1)(p) |
| Funeral services | Undertaker services | Art. 11(1)(h) |
| Composers/writers (collective management) | Collective management of copyrights | Art. 11(1)(q) |
| Transfer of going concern | Transfer of a business as a going concern (no VAT, no effect) | Art. 37d |

**Businesses making ONLY exempt supplies are not required to register for VAT and cannot recover input VAT.**

---

## SECTION 4: Blocked Input Tax (BUA) [T1]

**Legislation:** Besluit Uitsluiting Aftrek omzetbelasting 1968 (BUA), based on Wet OB 1968, Article 15(6) and Article 16.

The BUA excludes input VAT recovery on goods and services with a consumptive (private/personal) character. The correction is calculated per beneficiary per calendar year.

### BUA Blocked Categories

| Category | Rule | Threshold | BUA Article |
|----------|------|-----------|-------------|
| Business gifts to relations (relatiegeschenken) | VAT blocked if total gifts to ONE recipient exceed EUR 227/year (excl. VAT) | EUR 227 per recipient per year | BUA Art. 1(1)(b) |
| Staff provisions (personeelsvoorzieningen) | VAT blocked if total provisions to ONE employee exceed EUR 227/year (excl. VAT) | EUR 227 per employee per year | BUA Art. 1(1)(a) |
| Business entertaining / food and drink | VAT blocked on food, drink, tobacco provided to non-employees at business events if total exceeds EUR 227 per person per year | EUR 227 per recipient per year | BUA Art. 1(1)(b) |
| Company outings / staff parties | VAT blocked if total per employee exceeds EUR 227/year | EUR 227 per employee per year | BUA Art. 1(1)(a) |
| Staff canteen (bedrijfskantine) | Exception: VAT on canteen food IS deductible if employer charges employees a fee covering at least the cost of food/ingredients (zakelijke vergoeding). If provided free or below cost, BUA applies. | EUR 227 combined with other staff provisions | BUA Art. 1(2) |

### Critical BUA Rules [T1]

1. **All-or-nothing rule:** If the EUR 227 threshold is exceeded for a recipient/employee, ALL VAT on those provisions for that person for the ENTIRE year is blocked -- not just the excess above EUR 227.
2. **Annual test:** The EUR 227 threshold is tested per calendar year, not per VAT period.
3. **Correction timing:** BUA corrections are processed in the LAST VAT return of the calendar year (December return or Q4 return). Report as a reduction of rubriek 5b.
4. **Mixed provisions:** All staff provisions (gifts, parties, canteen, outings) are aggregated per employee when testing the EUR 227 threshold.

### Private Use Correction (Privegebruik) [T1]

**Legislation:** Wet OB 1968, Article 4(2); Uitvoeringsbesluit OB 1968.

At year-end, businesses must correct for private use of business goods. This is reported in **rubriek 1d** of the last VAT return of the calendar year.

| Item | Correction Method | Legislation |
|------|-------------------|-------------|
| **Company car (auto van de zaak)** | Default: **2.7% of catalogue price** (incl. VAT and BPM, excl. accessories added later) per year. The 2.7% represents the deemed VAT correction for private use. | Art. 4(2) Wet OB; Besluit uitsluiting aftrek |
| Company car -- reduced correction | Alternative: **1.5% of catalogue price** if the business can demonstrate limited private use (500-1000 km private per year) via a complete km registration (rittenregistratie) | Art. 4(2) Wet OB |
| Company car -- no correction | If private use is <= 500 km/year AND a complete km registration proves this, no correction is required | Art. 4(2) Wet OB |
| Company car -- employer pays fuel only | If the car is the employee's own but the employer pays for fuel: correct based on actual private km ratio from km registration | BUA Art. 1 |
| **Business premises with private use** | Correct based on actual private use proportion (e.g., m2 basis for home office in business property) | Art. 4(2) Wet OB |
| **Other business assets used privately** | Correct based on actual private use proportion | Art. 4(2) Wet OB |

**Motor vehicles -- Netherlands-specific:** There is NO general block on input VAT for motor vehicles in the Netherlands (unlike Malta and some other EU countries). A business MAY deduct ALL input VAT on a company car when purchased. However, the private use correction (2.7% of catalogue value) must be applied annually if the car is used for private purposes (> 500 km/year). This is fundamentally different from countries that block car VAT entirely.

### Registration-Based Recovery [T1]

| Registration Type | Input VAT Recovery | Notes |
|-------------------|-------------------|-------|
| Standard registration | Full recovery (subject to BUA and partial exemption) | Normal rules apply |
| KOR participant | NO recovery at all | Cannot file returns; VAT on costs is a cost |
| Fiscal unity (fiscale eenheid) | Recovery at group level | [T3] -- complex; escalate |

### Partial Exemption (Pro-Rata / Evenredige Toerekening) [T2]

**Legislation:** Wet OB 1968, Article 15(2); Uitvoeringsbesluit OB 1968, Articles 11-14.

If a business makes both taxable and exempt supplies:

```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```

Two methods available:

| Method | Description | When Used |
|--------|-------------|-----------|
| Pro-rata (omzet-methode) | Based on turnover ratio of taxable to total supplies | Default method |
| Actual use (werkelijk gebruik) | Based on actual allocation of costs to taxable/exempt activities | Optional; may be required by Belastingdienst if pro-rata produces distorted result |

**Flag for reviewer: pro-rata calculation must be confirmed by a belastingadviseur before applying. Year-end adjustment (herziening) is mandatory. Herzieningsperiode is 4 years for movable goods, 9 years for immovable property (Art. 13 Uitvoeringsbesluit OB).**

---

## SECTION 5: Registration [T1]

**Legislation:** Wet OB 1968, Article 7 (definition of entrepreneur); Article 25 (KOR).

### General Registration Rule

There is **NO general turnover threshold** for Dutch VAT registration. Every entrepreneur (ondernemer) performing economic activities must register for VAT, regardless of turnover level.

**Legislation:** Wet OB 1968, Article 7(1) -- "Ondernemer is ieder die een bedrijf zelfstandig uitoefent."

### How to Register

1. Register the business at KVK (Kamer van Koophandel)
2. KVK forwards registration data to the Belastingdienst automatically
3. Belastingdienst issues a BTW-identificatienummer (btw-id)
4. Filing frequency (monthly/quarterly/annual) is assigned by the Belastingdienst based on expected VAT liability

### BTW-nummer Format [T1]

| Element | Format | Example |
|---------|--------|---------|
| Country prefix | NL | NL |
| 9 digits | Numeric | 123456789 |
| Separator | B | B |
| 2-digit suffix | Numeric (01-99; suffix distinguishes entities at same fiscal number) | 01 |
| **Full format** | NL + 9 digits + B + 2 digits | NL123456789B01 |

**Note:** The btw-id is different from the RSIN/fiscaal nummer used for income/corporate tax purposes. Since 1 January 2020, sole traders (eenmanszaken) received new btw-ids that no longer contain the BSN (citizen service number) for privacy reasons.

### KOR -- Kleineondernemersregeling (Small Business Scheme) [T1]

**Legislation:** Wet OB 1968, Article 25 (new KOR, in effect from 1 January 2020).

#### Eligibility

| Criterion | Requirement |
|-----------|-------------|
| Annual turnover | < EUR 20,000 per calendar year (all activities combined) |
| Prior year | Turnover must also have been < EUR 20,000 in the prior calendar year |
| Entity types eligible | Sole traders (eenmanszaak), partnerships (VOF, maatschap), BVs, stichtingen, other legal entities |
| NOT eligible | Businesses making exclusively exempt supplies; businesses in a fiscal unity |

#### Effect of KOR Participation [T1]

| Aspect | Rule |
|--------|------|
| VAT on invoices | Do NOT charge VAT; invoices must indicate KOR applies |
| VAT returns | Do NOT file periodic VAT returns |
| Input VAT | CANNOT recover input VAT on any costs or investments |
| Intra-EU supplies | CANNOT apply zero rate for intra-EU supplies; cannot issue "btw verlegd" invoices |
| Intra-EU acquisitions | If intra-EU acquisitions exceed EUR 10,000/year, must register for intra-EU acquisition VAT separately |
| Administration | Simplified; must still keep records of turnover |

#### KOR Exit and Re-entry [T1]

| Event | Rule |
|-------|------|
| Voluntary exit | Can exit KOR at any time (3-year lock-in abolished from 2025) |
| Re-entry after exit | Cannot re-enter for remainder of exit year plus the entire following calendar year |
| Automatic exit (threshold breach) | If turnover exceeds EUR 20,000 during a year, KOR ceases from the FIRST supply that causes the threshold breach. VAT must be charged from that supply onwards. |
| Consequences of automatic exit | Must start filing VAT returns; can recover input VAT from the date KOR ceases; cannot re-enter until conditions met |

#### EU-KOR (from 2025) [T2]

**Legislation:** EU Directive 2020/285; implemented via amendment to Wet OB 1968.

| Criterion | Rule |
|-----------|------|
| Total EU-wide turnover | < EUR 100,000/year across all EU member states |
| Domestic turnover | Must also be below the domestic KOR threshold (EUR 20,000) |
| Application | Must register via Belastingdienst for cross-border application |
| Effect | Can apply exemption in other EU member states where domestic thresholds are met |

**Flag for reviewer: EU-KOR is a new scheme from 2025. Implementation details and practical application should be confirmed with a belastingadviseur.**

---

## SECTION 6: Filing Deadlines and Penalties [T1]

**Legislation:** Wet OB 1968, Article 14 (filing); Algemene wet inzake rijksbelastingen (AWR) Articles 67a-67f (penalties); Invorderingswet 1990 (collection and interest).

### Filing Frequency and Deadlines

| Frequency | Period | Filing & Payment Deadline | Legislation |
|-----------|--------|---------------------------|-------------|
| Monthly (maandelijks) | Calendar month | Last business day of the month following the period end (e.g., January return due by last business day of February) | Art. 14 Wet OB |
| Quarterly (per kwartaal) | Calendar quarter | Last business day of the month following quarter end (Q1: last business day of April; Q2: last business day of July; Q3: last business day of October; Q4: last business day of January following year) | Art. 14 Wet OB |
| Annual (jaarlijks) | Calendar year | 31 March of the following year | Art. 14 Wet OB |

**Critical filing rules:**

1. Filing and payment must BOTH be completed by the deadline. The payment must be **received** by the Belastingdienst, not merely sent.
2. Returns can only be submitted from the **24th day** of the last month of the reporting period. Returns submitted before this date are automatically rejected.
3. Monthly filing is mandatory if quarterly VAT payable typically exceeds EUR 15,000.
4. The Belastingdienst assigns the filing frequency; the entrepreneur cannot freely choose.

### Penalties [T1]

**Legislation:** AWR Articles 67a-67f; Besluit Bestuurlijke Boeten Belastingdienst (BBBB).

| Violation | Penalty | Legal Basis |
|-----------|---------|-------------|
| Late filing (verzuimboete voor niet-tijdig aangifte) | EUR 68 per late return (2024/2025 amount; indexed periodically). Escalates with repeated offenses up to EUR 1,377. | AWR Art. 67a |
| Late payment (verzuimboete voor niet-tijdig betalen) | 3% of the unpaid amount, minimum EUR 50, maximum EUR 5,514 | AWR Art. 67c |
| Failure to file (niet doen van aangifte) | Estimated assessment (ambtshalve aanslag) issued by Belastingdienst + penalty | AWR Art. 67a(2) |
| Deliberate error (vergrijpboete) | 25% to 100% of the underpaid tax, depending on severity and intent | AWR Art. 67f |
| Late payment interest (invorderingsrente) | 4% per annum (wettelijke rente; rate is set by government and may change) | Invorderingswet 1990, Art. 28 |
| Interest on tax assessment (belastingrente) | Currently 7.5% per annum for VAT (2024; rate is set annually by ministerial decree) [T2] | AWR Art. 30f |

### Suppletie (Supplementary Return / Correction of Prior Periods) [T1]

**Legislation:** AWR Article 10a; Belastingdienst guidance on suppletie-aangifte.

| Situation | Action Required |
|-----------|----------------|
| Error discovered, difference >= EUR 1,000 | Must file a separate suppletie-aangifte (supplementary return) via the Belastingdienst portal. Cannot correct via the next regular return. |
| Error discovered, difference < EUR 1,000 | May correct in the next regular periodic return |
| Voluntary disclosure | Filing a suppletie-aangifte voluntarily (before the Belastingdienst contacts you) generally prevents a vergrijpboete (deliberate error penalty) |
| Deadline for suppletie | Should be filed as soon as error is discovered; no specific statutory deadline, but filing before the Belastingdienst initiates an audit is strongly recommended |

### ICP Declaration (Opgaaf Intracommunautaire Prestaties) [T1]

| Frequency | Trigger | Deadline |
|-----------|---------|----------|
| Quarterly | Default for most businesses | Last business day of month following quarter end |
| Monthly | Intra-EU goods supplies > EUR 50,000 in any quarter (or any of the preceding 4 quarters) | Last business day of month following reporting month |

**The ICP total must equal rubriek 3b of the VAT return for the same period.**

### CBS Intrastat Reporting [T2]

| Aspect | Detail |
|--------|--------|
| Threshold | No fixed threshold since 2023. CBS selects businesses based on VAT return data (rubrieken 3b and 4b). |
| Notification | CBS sends a letter when the business is selected. |
| Frequency | Monthly (standard). Annual possible for arrivals EUR 0.8-5M or dispatches EUR 1-5M. |
| Deadline | 10th working day of following month. |

---

## SECTION 7: Reverse Charge Rules (Verleggingsregeling) [T1]

**Legislation:** Wet OB 1968, Articles 12(2)-(4) (domestic reverse charge), Article 17b (intra-EU acquisitions), Article 6 (place of supply for services), Article 23 (import deferral).

### 7a. Cross-Border Reverse Charge [T1]

For EU and non-EU purchases where the supplier does not charge Dutch VAT:

| Step | Action | Rubriek |
|------|--------|---------|
| 1 | Report turnover in the acquisition rubriek | 4a (non-EU) or 4b (EU) |
| 2 | Self-assess output VAT at the applicable Dutch rate (21% or 9%) | VAT column of 4a or 4b |
| 3 | Claim input VAT for the same amount (if fully deductible) | 5b |
| 4 | Net effect for fully taxable businesses | Zero |

**The VAT return must show BOTH sides (output and input) for reverse charge. This is mandatory even though the net effect is zero.**

### 7b. Domestic Reverse Charge (Verleggingsregeling binnenland) [T1]

**Legislation:** Wet OB 1968, Article 12(2)-(4); Besluit verleggingsregeling bouw.

The Netherlands applies mandatory domestic reverse charge in the following situations:

| Sector / Category | Condition | Supplier Rubriek | Customer Rubriek | Legislation |
|--------------------|-----------|-----------------|-----------------|-------------|
| **Construction (bouw)** | Subcontracting of construction work: building, demolition, renovation, installation, earthwork, shipbuilding | 1e (turnover only, "btw verlegd") | 2a (turnover + self-assessed VAT) + 5b (input) | Art. 12(4) Wet OB |
| **Staffing in construction** | Temporary labor provided for construction, shipbuilding, cleaning of buildings under construction | 1e (turnover only, "btw verlegd") | 2a (turnover + self-assessed VAT) + 5b (input) | Art. 12(4) Wet OB |
| **Scrap metal and waste** | B2B sales of scrap metal, demolition waste, reclaimed materials | 1e (turnover only, "btw verlegd") | 2a (turnover + self-assessed VAT) + 5b (input) | Art. 12(3) Wet OB |
| **Mobile phones and computer chips** | Invoice total for these specific products >= EUR 10,000 | 1e (turnover only, "btw verlegd") | 2a (turnover + self-assessed VAT) + 5b (input) | Art. 12(3) Wet OB |
| **Emission rights (CO2)** | All B2B transfers of emission allowances | 1e (turnover only, "btw verlegd") | 2a (turnover + self-assessed VAT) + 5b (input) | Art. 12(3) Wet OB |
| **Real estate (certain transfers)** | Transfer of immovable property where the option to tax is exercised (optie belaste levering) | 1e (turnover only, "btw verlegd") | 2a (turnover + self-assessed VAT) + 5b (input) | Art. 12(4) Wet OB |
| **Gold (semi-finished)** | Supplies of gold material with purity >= 325/1000 | 1e (turnover only, "btw verlegd") | 2a (turnover + self-assessed VAT) + 5b (input) | Art. 12(3) Wet OB |

### 7c. Article 23 Import Licence (Vergunning Article 23) [T1]

**Legislation:** Wet OB 1968, Article 23.

| Aspect | Detail |
|--------|--------|
| What it does | Allows holders to defer import VAT from the customs declaration to their periodic VAT return, instead of paying VAT at the border |
| Cash flow benefit | No upfront VAT payment at customs; VAT is reported and simultaneously claimed on the VAT return |
| How it works | Import reported in rubriek 4a (customs value + duties as turnover, self-assessed import VAT). Claim same VAT in 5b. Net effect = zero for fully taxable businesses. |
| Eligibility | Business must be established in NL (or have a fiscal representative); must regularly import from non-EU; requires application to Belastingdienst |
| Foreign entrepreneurs | Must appoint a fiscal representative (fiscaal vertegenwoordiger) who is jointly liable for the VAT |

**The Netherlands is notable in the EU for the widespread availability and use of this import deferral scheme.**

### 7d. Ketenaansprakelijkheid (Chain Liability in Construction) [T2]

**Legislation:** Wet OB 1968, Article 35; Invorderingswet 1990, Articles 34-35.

In the construction sector, the main contractor can be held liable for unpaid VAT by subcontractors down the chain. To mitigate this risk:

| Protection Measure | Description |
|--------------------|-------------|
| G-account (geblokkeerde rekening) | Subcontractor opens a blocked bank account; main contractor pays the VAT portion into this account; Belastingdienst can only collect from the G-account |
| Verklaring betalingsgedrag | Certificate of good tax payment behaviour issued by Belastingdienst; confirms subcontractor is up to date with tax obligations |
| Direct deposit to Belastingdienst | Main contractor pays VAT portion directly to Belastingdienst on behalf of subcontractor |

**Flag for reviewer: chain liability assessment requires specialist knowledge. Escalate if client is a main contractor with subcontractors in construction.**

### 7e. Exceptions to Reverse Charge [T1]

- Out-of-scope payments (wages, bank charges, dividends, etc.): NEVER reverse charge
- Local consumption abroad (hotel, restaurant, taxi, conference in another country): NOT reverse charge; foreign VAT paid at source
- EU supplier charged their local VAT > 0%: NOT reverse charge; foreign VAT is part of expense (refund via EU 8th Directive procedure)
- B2C services where place of supply is not NL: NOT reverse charge
- Mobile phones/chips invoice total below EUR 10,000: NOT domestic reverse charge (normal VAT applies)

---

## SECTION 8: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- Article 23 Import Licence (Vergunning) [T1]

**Situation:** Dutch entrepreneur with Article 23 permit imports electronics from China. Goods arrive at Rotterdam port.
**Resolution:** Instead of paying VAT at customs, report on VAT return: rubriek 4a (customs value + import duties as turnover, self-assessed import VAT at 21%). Claim same amount in rubriek 5b. Net cash effect = zero. The customs declaration must reference the Article 23 permit number. Without the permit, VAT would be payable at customs (recoverable via 5b from customs document).
**Legislation:** Wet OB 1968, Article 23.

### EC2 -- Private Use Correction for Company Car (2.7% of Catalogue Value) [T1]

**Situation:** Employee has a company car with catalogue price EUR 45,000 (incl. VAT and BPM). No km registration is maintained. Year-end correction needed.
**Resolution:** Apply default correction: 2.7% x EUR 45,000 = EUR 1,215. This amount is the deemed turnover for private use. VAT = EUR 1,215 x 21/121 = EUR 211.03 (rounded). Report EUR 1,215 as turnover and EUR 211.03 as VAT in rubriek 1d of the LAST return of the calendar year. If > 500 km private use but < 1,000 km with km registration, 1.5% applies instead. If <= 500 km private with km registration, no correction.
**Legislation:** Wet OB 1968, Article 4(2); Besluit uitsluiting aftrek omzetbelasting.

### EC3 -- BUA Entertainment Threshold (EUR 227 per Person) [T1]

**Situation:** Client entertains business relations with dinners throughout the year. Total entertainment per relation: EUR 250 (excl. VAT). VAT on entertainment: EUR 52.50 per relation at 21%.
**Resolution:** EUR 250 > EUR 227 threshold. ALL VAT on entertainment for those recipients is blocked for the entire year -- not just the excess above EUR 227. Process BUA correction in the last VAT return of the calendar year by reducing rubriek 5b by the total blocked VAT.
**Legislation:** BUA 1968, Article 1(1)(b).

### EC4 -- KOR Threshold Breach [T1]

**Situation:** KOR-registered entrepreneur has turnover of EUR 18,500 in January-October. In November, a new contract will bring total turnover to EUR 22,000.
**Resolution:** KOR ceases from the FIRST supply that causes turnover to exceed EUR 20,000. The entrepreneur must charge VAT from that specific supply onwards, begin filing VAT returns, and can recover input VAT from that date. All supplies before the threshold breach remain KOR-treated (no VAT). The entrepreneur must notify the Belastingdienst. Cannot re-enter KOR until the remainder of the exit year plus the entire following calendar year have passed.
**Legislation:** Wet OB 1968, Article 25(3).

### EC5 -- Margin Scheme (Margeregeling) for Second-Hand Goods [T2]

**Situation:** A second-hand furniture dealer buys a table from a private individual for EUR 200 and sells it for EUR 350 (incl. VAT).
**Resolution:** Margin scheme applies because the goods were purchased without VAT from a non-VAT-registered person. Profit margin = EUR 350 - EUR 200 = EUR 150. VAT = EUR 150 x 21/121 = EUR 26.03. Report in rubriek 1a: turnover = EUR 150 - EUR 26.03 = EUR 123.97, VAT = EUR 26.03. Invoice must state "margeregeling" or "margin scheme" and must NOT show VAT separately. If sold at a loss (negative margin), report EUR 0 VAT -- no negative VAT refund on margin goods.
**Legislation:** Wet OB 1968, Articles 28b-28i.
**Flag for reviewer:** Election between individual method and globalisation method must be confirmed. Method chosen must be applied consistently.

### EC6 -- Fiscal Unity (Fiscale Eenheid) [T3]

**Situation:** Three related BVs (parent + two subsidiaries) are closely bound financially, economically, and organisationally. They want to form a fiscal unity for VAT.
**Resolution:** ESCALATE. Fiscal unity (fiscale eenheid) means the entities are treated as a single taxable person. Internal supplies between members are outside the scope of VAT. One combined VAT return is filed. All members are jointly and severally liable for the VAT debts. Application must be made to the Belastingdienst. Complex implications for partial exemption, BUA corrections, and group restructuring.
**Legislation:** Wet OB 1968, Article 7(4).

### EC7 -- Real Estate: Option to Tax (Optie Belaste Levering/Verhuur) [T3]

**Situation:** Commercial property owner wants to charge VAT on the rental of office space to a VAT-registered tenant.
**Resolution:** ESCALATE. By default, letting of immovable property is exempt (Art. 11(1)(b)). However, lessor and lessee can jointly opt to tax the rental if the tenant uses the property for at least 90% VATable activities (the "90% test"). If option is exercised, VAT is charged on rent and the lessor can recover input VAT on the property. The option must be documented in writing. For sale of new immovable property (< 2 years after first use), VAT applies mandatorily. For sale of existing immovable property, transfer tax (overdrachtsbelasting) at 10.4% applies unless option to tax is exercised.
**Legislation:** Wet OB 1968, Article 11(1)(b)(5); Uitvoeringsbesluit OB, Article 6a.

### EC8 -- Correction of Prior Period Errors via Suppletieverklaring [T1]

**Situation:** Accountant discovers in June that a March VAT return understated output VAT by EUR 3,000.
**Resolution:** EUR 3,000 > EUR 1,000 threshold. Must file a separate suppletie-aangifte via the Belastingdienst portal. Cannot correct in the next regular return. If the difference were < EUR 1,000, it could be included in the next regular return. Voluntary disclosure before Belastingdienst contact generally prevents vergrijpboete (up to 100% penalty).
**Legislation:** AWR Article 10a; Belastingdienst policy.

### EC9 -- Self-Supply Rules for New Construction [T2]

**Situation:** A property developer builds a new apartment building using own staff and materials. The building will be used for exempt (residential) letting.
**Resolution:** Self-supply rules apply. When a business constructs immovable property and uses it for exempt purposes, the business must self-assess VAT on the cost of construction at the point the property is taken into use (integratieheffing was abolished in 2014, but similar corrections apply via herzieningsregeling). Input VAT deducted during construction must be corrected over the herzieningsperiode (9 years for immovable property). Year-end adjustment compares actual taxable use vs. initial deduction.
**Legislation:** Wet OB 1968, Article 15(4); Uitvoeringsbesluit OB, Articles 11-14.
**Flag for reviewer:** Complex calculation requiring specialist real estate VAT knowledge.

### EC10 -- Cross-Border B2C Digital Services (OSS) [T2]

**Situation:** Dutch online business sells digital services (streaming subscriptions) to consumers in France, Germany, and Spain. Total B2C digital sales to other EU countries exceed EUR 10,000/year.
**Resolution:** Place of supply is in the customer's country (Art. 6h Wet OB). Options: (1) Register for VAT in each customer's country and charge local VAT, or (2) Use the One-Stop Shop (OSS) scheme via the Belastingdienst portal. Under OSS, the business files a single quarterly OSS return covering all EU B2C digital/telecom/broadcasting sales, applying each country's local VAT rate. Payment is made to the Belastingdienst, which distributes to other member states. Below the EUR 10,000 threshold, NL VAT may apply instead.
**Legislation:** Wet OB 1968, Article 6h; Article 28s (OSS).
**Flag for reviewer:** OSS registration and rate selection per country require confirmation.

### EC11 -- EU Hotel / Restaurant / Taxi Booked Abroad [T1]

**Situation:** Dutch entrepreneur pays for a hotel in France. Invoice shows French VAT at 10%.
**Resolution:** NOT reverse charge. French VAT was charged and paid at source. Treat as overhead expense. No Dutch VAT rubrieken affected. French VAT is irrecoverable on the NL return. May be refundable via the EU 8th Directive VAT refund procedure (application to French tax authority via Dutch Belastingdienst portal, deadline: 30 September of following year).
**Legislation:** Wet OB 1968, Article 6 (place of supply rules for services).

### EC12 -- Software Subscription from Non-EU Provider (e.g., Google, AWS) [T1]

**Situation:** Monthly charge from a US company, no VAT on invoice. Client is standard-registered.
**Resolution:** Reverse charge applies. Rubriek 4a: report net amount as turnover, self-assess VAT at 21%. Rubriek 5b: claim same VAT as input (if fully deductible). Net effect = zero for fully taxable business.
**Legislation:** Wet OB 1968, Article 6(2)(d) -- B2B services from outside EU; place of supply is where the recipient is established.

### EC13 -- Construction Subcontractor Invoice (Verleggingsregeling Bouw) [T1]

**Situation:** Subcontractor invoices EUR 15,000 for renovation work. Invoice states "btw verlegd."
**Resolution:** Domestic reverse charge. Customer (main contractor) reports in rubriek 2a: EUR 15,000 turnover + EUR 3,150 self-assessed VAT (21%). Claims EUR 3,150 in rubriek 5b (if deductible). Subcontractor reports EUR 15,000 in rubriek 1e (turnover only, no VAT).
**Legislation:** Wet OB 1968, Article 12(4); Besluit verleggingsregeling bouw.

### EC14 -- Accommodation Post-2026 [T1]

**Situation:** Hotel in Amsterdam charges for overnight stay in 2026.
**Resolution:** 21% VAT applies (changed from 9% on 1 January 2026). Report in rubriek 1a. Exception: camping accommodation remains at 9% (rubriek 1b).
**Legislation:** Wet OB 1968, Tabel I (as amended 1 January 2026).

### EC15 -- EU Supplier Charges Local VAT on Invoice [T1]

**Situation:** French supplier charges 20% French VAT on consulting services provided to a Dutch entrepreneur (B2B).
**Resolution:** This is NOT a reverse charge situation (supplier charged VAT). Do NOT self-assess in rubriek 4b. The French VAT is a cost. The supply SHOULD have been reverse-charged (B2B services). Advise client to request a corrected invoice from the French supplier showing 0% VAT with "VAT reverse charge" notation. If corrected, then apply normal reverse charge via rubriek 4b. If not corrected, the French VAT may be refundable via 8th Directive.
**Legislation:** Wet OB 1968, Article 6(1) (place of supply).

### EC16 -- Credit Notes [T1]

**Situation:** Client receives a credit note from a supplier for a previously invoiced and reported transaction.
**Resolution:** Reverse the original entry. If original input VAT was in rubriek 5b, reduce 5b by the credit note VAT. If original was output in rubriek 1a, reduce 1a by the credit note amount. Report net figures per period.
**Legislation:** Wet OB 1968, Article 29.

### EC17 -- Import of Goods Without Article 23 Permit [T2]

**Situation:** Client imports electronics from China. No Article 23 permit. Customs charges VAT at the border.
**Resolution:** VAT is paid at customs (appears on customs declaration / invoer-aangifte). This VAT IS recoverable as input VAT -- include in rubriek 5b using the customs declaration as the source document. Flag for reviewer: confirm customs document is available and amounts match.
**Legislation:** Wet OB 1968, Article 18; Article 15(1)(b).

---

## SECTION 9: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard Domestic Purchase, 21% VAT [T1]

**Input:** NL supplier, office supplies, gross EUR 242, VAT EUR 42, net EUR 200. Standard-registered client. Not a BUA category.
**Expected output:** Rubriek 5b += EUR 42. No output rubrieken affected. Input VAT recoverable in full.

### Test 2 -- Non-EU Software Subscription, Reverse Charge [T1]

**Input:** US supplier (AWS), monthly fee EUR 100, no VAT on invoice. Standard-registered client.
**Expected output:** Rubriek 4a: turnover EUR 100, VAT EUR 21 (21%). Rubriek 5b += EUR 21. Net VAT effect = zero.

### Test 3 -- EU Goods Acquisition, Reverse Charge [T1]

**Input:** German supplier ships machinery to NL, EUR 5,000, no VAT on invoice (intracommunautaire levering). Standard-registered client.
**Expected output:** Rubriek 4b: turnover EUR 5,000, VAT EUR 1,050 (21%). Rubriek 5b += EUR 1,050. Net VAT effect = zero. Client should verify German supplier's btw-id via VIES.

### Test 4 -- Intra-EU Sale of Goods, Zero-Rated [T1]

**Input:** Standard-registered NL client sells goods to Belgian company (valid BE btw-id), EUR 3,000. Goods shipped to Belgium with CMR documentation.
**Expected output:** Rubriek 3b = EUR 3,000. No VAT charged. Must report on ICP declaration.

### Test 5 -- KOR Client, Any Purchase [T1]

**Input:** KOR-registered client purchases materials for EUR 500 incl. EUR 87 VAT (21%).
**Expected output:** No VAT return filed. No input VAT recovery. The EUR 87 VAT is a cost absorbed by the business.

### Test 6 -- Construction Reverse Charge (Domestic) [T1]

**Input:** Subcontractor invoices EUR 10,000 for brickwork, states "btw verlegd." Standard-registered client (main contractor).
**Expected output:** Rubriek 2a: turnover EUR 10,000, VAT EUR 2,100 (21%). Rubriek 5b += EUR 2,100. Subcontractor reports EUR 10,000 in rubriek 1e.

### Test 7 -- EU Hotel, Local Consumption Exception [T1]

**Input:** Standard-registered client pays EUR 300 for hotel in Italy including EUR 30 Italian VAT (10%).
**Expected output:** No Dutch VAT return entry. Expense is EUR 300 gross including irrecoverable Italian VAT. Not reverse charge. Italian VAT may be refundable via 8th Directive procedure.

### Test 8 -- BUA Correction, Business Gifts Exceeding Threshold [T1]

**Input:** Client gave gifts totalling EUR 300 (excl. VAT) per recipient to 20 business relations during the year. VAT on gifts: EUR 63 per recipient (21%). Total VAT: EUR 1,260.
**Expected output:** EUR 300 > EUR 227 threshold. ALL gift VAT is blocked (not just excess). In last return of year: reduce rubriek 5b by EUR 1,260.

### Test 9 -- Private Use Company Car, No km Registration [T1]

**Input:** Company car, catalogue price EUR 40,000 (incl. VAT and BPM). No km records kept. Year-end correction.
**Expected output:** Rubriek 1d: 2.7% x EUR 40,000 = EUR 1,080 (turnover). VAT = EUR 1,080 x 21/121 = EUR 187.60 (rounded). Report EUR 1,080 as turnover and EUR 187.60 as VAT in rubriek 1d of last return of year.

### Test 10 -- Export to Non-EU Country [T1]

**Input:** Standard-registered NL client exports goods to United States, EUR 8,000. Proof of export (customs declaration) available.
**Expected output:** Rubriek 3a = EUR 8,000. Zero-rated. No VAT. Input VAT on costs related to this export is fully recoverable.

### Test 11 -- Domestic Sale at Reduced Rate (9%) [T1]

**Input:** NL bookshop sells books to a customer, net EUR 500, VAT EUR 45 (9%).
**Expected output:** Rubriek 1b: turnover EUR 500, VAT EUR 45.

### Test 12 -- Margin Scheme Sale [T2]

**Input:** Second-hand goods dealer bought item from private person for EUR 400. Sells for EUR 600 (incl. VAT). Uses individual method.
**Expected output:** Profit margin = EUR 600 - EUR 400 = EUR 200. VAT = EUR 200 x 21/121 = EUR 34.71. Report in rubriek 1a: turnover = EUR 165.29, VAT = EUR 34.71. Invoice must state "margeregeling."

### Test 13 -- Article 23 Import [T1]

**Input:** Standard-registered NL client with Article 23 permit imports goods from US. Customs value + duties = EUR 20,000.
**Expected output:** Rubriek 4a: turnover EUR 20,000, VAT EUR 4,200 (21%). Rubriek 5b += EUR 4,200. Net effect = zero. No cash payment at customs.

### Test 14 -- Suppletie Required [T1]

**Input:** Accountant discovers EUR 2,500 underpayment in a prior VAT return.
**Expected output:** EUR 2,500 > EUR 1,000 threshold. Cannot correct in next regular return. Must file separate suppletie-aangifte via Belastingdienst portal.

---

## SECTION 10: Comparison with Malta

This section highlights key differences between Netherlands and Malta VAT systems for practitioners working across both jurisdictions.

| Feature | Netherlands (NL) | Malta (MT) |
|---------|-------------------|------------|
| **Primary legislation** | Wet OB 1968 | VAT Act Chapter 406 |
| **Tax authority** | Belastingdienst | Commissioner for Revenue (CFR) |
| **Standard rate** | 21% | 18% |
| **Reduced rates** | 9% (single reduced rate) | 5%, 7%, 12% (three reduced rates) |
| **VAT return form** | OB aangifte (17 rubrieken across 5 sections) | VAT3 (45 boxes across multiple sections) |
| **Filing frequency** | Monthly, quarterly, or annual (Belastingdienst assigns) | Quarterly (Article 10), annual (Article 11), monthly (Article 12) |
| **Filing deadline** | Last business day of month following period | 21st of month following quarter (e-filing); 14th (paper) |
| **Small business scheme** | KOR: EUR 20,000 turnover; full exemption, no filing, no input recovery | Article 11: EUR 35,000 turnover; simplified annual declaration, no input recovery |
| **Registration threshold** | None (all entrepreneurs must register, then may elect KOR) | None for Article 10; EUR 35,000 for Article 11; EUR 10,000 for EU goods acquisition (Article 12) |
| **BTW-id format** | NL + 9 digits + B + 2 digits (e.g., NL123456789B01) | MT + 8 digits (e.g., MT12345678) |
| **Capital goods scheme threshold** | Herzieningsregeling: 4 years movable, 9 years immovable (no monetary threshold for entry) | EUR 1,160 gross per item |
| **Blocked input VAT** | BUA: EUR 227/person/year threshold (all-or-nothing); no general block on motor vehicles | 10th Schedule: entertainment, motor vehicles, tobacco, alcohol, art/antiques, pleasure craft, personal use (absolute block) |
| **Motor vehicles** | Full input VAT deduction allowed; annual private use correction (2.7% of catalogue value) | Input VAT BLOCKED entirely (10th Schedule); exceptions for taxi, delivery, car rental |
| **Import VAT deferral** | Article 23 permit: defer to VAT return (widely used) | No equivalent; VAT paid at customs (C88 document) |
| **Domestic reverse charge** | Extensive: construction, staffing, scrap, mobile phones/chips >= EUR 10,000, emissions, gold, real estate | Limited; not widely applied domestically |
| **Fiscal unity** | Available (Art. 7(4)): related entities treated as one taxpayer; internal supplies outside scope | Not available under Malta VAT law |
| **Margin scheme** | Available (Art. 28b-28i): individual or globalisation method | Available but less commonly used |
| **Suppletie (correction)** | Separate suppletie-aangifte if error >= EUR 1,000; < EUR 1,000 in next return | Correction via amended return |
| **Late filing penalty** | EUR 68 per late return (escalating) | EUR 20 per day late (capped) |
| **Deliberate error penalty** | Vergrijpboete: 25%-100% of underpaid tax | Up to 150% of tax evaded |
| **Real estate option to tax** | Joint election by lessor + lessee; 90% test for tenant's taxable use | Limited option to tax |
| **ICP declaration** | Separate filing matching rubriek 3b; quarterly or monthly | Recapitulative statement; quarterly |
| **Place of supply (B2B services)** | Customer's country (standard B2B rule) | Customer's country (standard B2B rule) |
| **Exempt supplies** | Art. 11: healthcare, education, financial, insurance, postal, immovable property letting, gambling, funeral, social/cultural | Similar categories; medical, education, financial, insurance |

### Key Practitioner Warnings When Switching Between NL and MT

1. **Motor vehicles:** NL allows full deduction with annual correction; MT blocks entirely. Do NOT apply MT's block in NL or vice versa.
2. **Blocked categories:** NL uses EUR 227 threshold (BUA); MT has absolute blocks (10th Schedule). The approaches are fundamentally different.
3. **Number of reduced rates:** NL has one (9%); MT has three (5%, 7%, 12%). Different lookup logic required.
4. **Capital goods:** NL uses a time-based revision period (herzieningsregeling); MT uses a monetary threshold (EUR 1,160).
5. **Import VAT:** NL's Article 23 deferral has no equivalent in MT. NL businesses expect zero cash outflow on imports; MT businesses pay at customs.
6. **Form structure:** NL's 17 rubrieken are simpler than MT's 45 boxes. Do not attempt to map NL rubrieken 1:1 onto MT boxes.
7. **Domestic reverse charge:** NL applies it extensively (construction, scrap, phones, etc.); MT has very limited domestic reverse charge.

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT rubrieken -- they are 100% deterministic from facts
- NEVER report intra-EU supplies (rubriek 3b) without verifying the customer's btw-id via VIES
- NEVER apply reverse charge to out-of-scope categories (wages, bank charges, dividends, loan repayments, income tax payments)
- NEVER apply reverse charge when EU supplier charged their local VAT > 0%
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi in another country)
- NEVER allow KOR participants to claim input VAT
- NEVER allow KOR participants to charge VAT on invoices
- NEVER allow KOR participants to file periodic VAT returns
- NEVER apply the margin scheme to goods where input VAT was previously deducted by the seller
- NEVER report BUA corrections in a period other than the LAST return of the calendar year
- NEVER report private use corrections (rubriek 1d) in a period other than the LAST return of the calendar year
- NEVER file a return before the 24th of the last month of the reporting period
- NEVER confuse exempt without credit (vrijgesteld, no input VAT recovery) with zero-rated (nultarief, full input VAT recovery)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER apply domestic reverse charge for mobile phones/chips if the invoice total for that product category is below EUR 10,000
- NEVER apply the 2.7% private use correction to a car with <= 500 km private use per year (if proven by km registration)
- NEVER apply NL motor vehicle rules using Malta's 10th Schedule block -- NL allows full deduction with annual correction
- NEVER include rubrieken 3a, 3b, or 3c VAT amounts in the calculation of rubriek 5a (they are turnover-only, informational)
- NEVER file a suppletie correction >= EUR 1,000 via the next regular return -- a separate suppletie-aangifte is required

---

## Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Belastingadviseur must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to belastingadviseur. Document gap.
```

---

## Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax or corporate tax. The following is reference information only. Do not execute any of these rules. Escalate to belastingadviseur.

- **Inkomstenbelasting (IB):** Personal income tax for self-employed (Box 1: work and home; Box 2: substantial interest; Box 3: savings and investments). Progressive rates.
- **Vennootschapsbelasting (Vpb):** Corporate income tax. Rates: 19% on first EUR 200,000, 25.8% above (2024). Separate filing.
- **Loonheffingen:** Payroll taxes (income tax, social insurance premiums, healthcare insurance contribution). Separate filing obligation.
- **Dividendbelasting:** 15% withholding on dividend distributions. Separate filing.
- **Overdrachtsbelasting:** Transfer tax on immovable property (10.4% general; 2% for primary residences under EUR 510,000 for buyers under 35). Separate from VAT.

---

## Contribution Notes

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all rubriek numbers with the equivalent boxes on your jurisdiction's VAT return form.
3. Replace VAT rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace the BUA thresholds (EUR 227) with your jurisdiction's equivalent blocked deduction rules.
5. Replace the KOR thresholds (EUR 20,000) with your jurisdiction's equivalent small enterprise scheme.
6. Replace the EU country list with the list relevant to your jurisdiction's trading bloc, if applicable.
7. Replace the domestic reverse charge sectors with your jurisdiction's equivalent.
8. Have a registered tax adviser (belastingadviseur) or equivalent in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a registered practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
