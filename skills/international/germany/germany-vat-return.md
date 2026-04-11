---
name: germany-vat-return
description: Use this skill whenever asked to prepare, review, or create a German VAT return (Umsatzsteuer-Voranmeldung / USt-VA) or annual VAT declaration (Umsatzsteuererklaerung) for any client. Trigger on phrases like "prepare VAT return", "do the German VAT", "fill in USt-VA", "create the return", "Umsatzsteuer", "Vorsteuer", or any request involving German VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete German VAT classification rules, Kennzahl mappings, deductibility rules, reverse charge treatment, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Germany.
status: awaiting-validation
version: 1.0-draft
---

# Germany VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Germany (Federal Republic of Germany) |
| Jurisdiction Code | DE |
| Primary Legislation | Umsatzsteuergesetz (UStG) -- German Value Added Tax Act |
| Supporting Legislation | UStDV (Umsatzsteuer-Durchfuehrungsverordnung -- implementing regulation); AO (Abgabenordnung -- General Tax Code); EStG (Einkommensteuergesetz -- Income Tax Act, for cross-references) |
| Tax Authority | Finanzamt (local tax office), overseen by Bundeszentralamt fuer Steuern (BZSt) |
| Filing Portal | ELSTER (https://www.elster.de) |
| Contributor | DRAFT -- awaiting practitioner validation |
| Validated By | AWAITING VALIDATION -- must be validated by a Steuerberater (licensed tax advisor) in Germany |
| Validation Date | Pending |
| Skill Version | 1.0-draft |
| Confidence Coverage | Tier 1: Kennzahl assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial deduction for mixed-use, sector-specific rules, Differenzbesteuerung. Tier 3: Organschaft, complex group structures, special schemes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A Steuerberater must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to Steuerberater and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and Steuernummer / USt-IdNr** [T1] -- USt-IdNr format: DE + 9 digits (e.g. DE123456789). Steuernummer is the local tax number assigned by the Finanzamt.
2. **VAT registration status** [T1] -- Regelbesteuerung (standard), Kleinunternehmer (ss19 UStG), or Ist-Versteuerung (cash basis under ss20 UStG)
3. **Filing frequency** [T1] -- Monthly (prior year VAT liability > EUR 9,000), quarterly (EUR 2,000-9,000), or exempt from advance returns (< EUR 2,000). Source: ss18(2) UStG; thresholds verified against PWC Tax Summaries.
4. **Industry/sector** [T2] -- impacts partial deduction rules and ss13b applicability (e.g., construction sector)
5. **Does the business make exempt supplies (ss4 UStG)?** [T2] -- If yes, ss15(2) input tax restriction applies; Steuerberater must confirm pro-rata
6. **Does the business trade goods for resale?** [T1] -- impacts classification of purchases
7. **VAT credit carried forward from prior period** [T1] -- relevant for Kz 62
8. **Soll- or Ist-Versteuerung?** [T1] -- Soll = accrual basis (default); Ist = cash basis (turnover <= EUR 600,000, ss20 UStG)
9. **Dauerfristverlaengerung granted?** [T1] -- if yes, filing deadline extended by 1 month; Sondervorauszahlung applies
10. **Does the client hold a ss13b Freistellungsbescheinigung?** [T1] -- relevant for construction reverse charge

For Kleinunternehmer [T1]: confirm prior year turnover was <= EUR 25,000 AND current year turnover will not exceed EUR 100,000. Source: ss19(1) UStG (as amended from 1 January 2025 by Wachstumschancengesetz / JStG 2024).

**If items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## SECTION 1: VAT Return Form Structure (USt-VA)

### 1.1 Form Identification [T1]

| Field | Value |
|-------|-------|
| Official Name | Umsatzsteuer-Voranmeldung (USt-VA) |
| English Name | Advance VAT Return |
| Filing Method | Electronic filing via ELSTER (https://www.elster.de) only; paper filing not accepted |
| Legal Basis | ss18(1) UStG |
| Annual Declaration | Umsatzsteuererklaerung (USt-E), filed annually, ss18(3) UStG |

### 1.2 Kennzahl Directory -- Grouped by Category [T1]

**Legislation:** ss18 UStG; BMF official form guidance for USt-VA.

**Note on Kennzahl mechanics:** For most output tax lines, the taxpayer enters the NET (tax base) amount only. The tax amount is computed automatically by ELSTER by applying the relevant rate. For input tax lines, the taxpayer enters the TAX amount. Exceptions are noted below.

#### Group A: Taxable Domestic Supplies (Steuerpflichtige Umsaetze)

| Kz | German Name | English Name | What Goes In | Rate | Entry |
|----|-------------|--------------|--------------|------|-------|
| 81 | Steuerpflichtige Umsaetze zum Steuersatz von 19% | Taxable supplies at 19% | Net amount of all domestic sales at standard rate | 19% | Net (tax auto-calculated) |
| 86 | Steuerpflichtige Umsaetze zum Steuersatz von 7% | Taxable supplies at 7% | Net amount of all domestic sales at reduced rate | 7% | Net (tax auto-calculated) |
| 35 | Umsaetze zu anderen Steuersaetzen | Supplies at other tax rates | Net amount of supplies at rates other than 19%/7% (rare; e.g. forestry 5.5%) | Other | Net |
| 36 | -- (tax for Kz 35) | Tax on other-rate supplies | Tax amount corresponding to Kz 35 | -- | Tax amount |

#### Group B: Tax-Free Supplies with Input Tax Deduction (Steuerfreie Umsaetze mit Vorsteuerabzug)

| Kz | German Name | English Name | What Goes In |
|----|-------------|--------------|--------------|
| 41 | Innergemeinschaftliche Lieferungen (ss4 Nr.1b) | Intra-Community supplies of goods | Net amount of B2B goods sold to VAT-registered EU customers, shipped from DE to another EU state. Zero-rated. Requires valid USt-IdNr of customer. |
| 44 | Innergemeinschaftliche Lieferungen -- neue Fahrzeuge an Abnehmer ohne USt-IdNr | IC supplies of new vehicles to buyers without VAT ID | Net amount of new vehicle sales to non-VAT-registered EU buyers |
| 49 | Innergemeinschaftliche Lieferungen -- neue Fahrzeuge ausserhalb eines Unternehmens | IC supplies of new vehicles outside a business | Net amount of new vehicles sold by non-business sellers to EU buyers |
| 43 | Ausfuhrlieferungen | Export supplies (non-EU) | Net amount of goods exported outside the EU. Zero-rated under ss4 Nr.1a + ss6 UStG. Requires proof of export (customs documentation). |
| 45 | Uebrige steuerfreie Umsaetze mit Vorsteuerabzug | Other tax-free supplies with input tax deduction | Net amount of other zero-rated supplies (e.g. services to non-EU B2B under ss3a(2), cross-border transport, certain financial services to non-EU) |

#### Group C: Tax-Free Supplies without Input Tax Deduction (Steuerfreie Umsaetze ohne Vorsteuerabzug)

| Kz | German Name | English Name | What Goes In |
|----|-------------|--------------|--------------|
| 48 | Steuerfreie Umsaetze ohne Vorsteuerabzug | Tax-free supplies without input tax deduction | Net amount of exempt supplies under ss4 Nr.8-29 UStG (financial services, insurance, healthcare, education, property rental, etc.). Input VAT on related purchases is NOT recoverable under ss15(2). |

#### Group D: Intra-Community Acquisitions (Innergemeinschaftliche Erwerbe)

| Kz | German Name | English Name | What Goes In | Rate | Entry |
|----|-------------|--------------|--------------|------|-------|
| 89 | Steuerpflichtige innergemeinschaftliche Erwerbe zum Steuersatz von 19% | Taxable IC acquisitions at 19% | Net amount of goods acquired from EU suppliers at standard rate | 19% | Net (tax auto-calculated) |
| 93 | Steuerpflichtige innergemeinschaftliche Erwerbe zum Steuersatz von 7% | Taxable IC acquisitions at 7% | Net amount of goods acquired from EU suppliers at reduced rate | 7% | Net (tax auto-calculated) |
| 95 | Steuerpflichtige innergemeinschaftliche Erwerbe zu anderen Steuersaetzen | Taxable IC acquisitions at other rates | Net amount of IC acquisitions at non-standard rates | Other | Net |
| 98 | -- (tax for Kz 95) | Tax on other-rate IC acquisitions | Tax amount corresponding to Kz 95 | -- | Tax amount |
| 94 | Steuerfreie innergemeinschaftliche Erwerbe | Tax-free IC acquisitions | IC acquisitions that are exempt (e.g. certain exempt supplies) | 0% | Net |
| 46 | Innergemeinschaftliche Erwerbe neuer Fahrzeuge | IC acquisitions of new vehicles | By non-VAT-registered buyers (ss1a UStG) | 19% | Net (tax auto-calculated) |

#### Group E: Reverse Charge -- Recipient is Tax Debtor (ss13b UStG)

| Kz | German Name | English Name | What Goes In | Entry |
|----|-------------|--------------|--------------|-------|
| 46 | Leistungen eines im Ausland ansaessigen Unternehmers (ss13b(1)) | Supplies by foreign-based businesses | Net amount of services/goods received from businesses not established in Germany where reverse charge applies | Net (tax auto-calculated at applicable rate) |
| 47 | -- (tax for Kz 46) | Tax on ss13b(1) supplies | Output VAT self-assessed on Kz 46 supplies | Tax amount |
| 73 | Lieferungen sicherungsuebereigneter Gegenstaende und Umsaetze (ss13b(2) Nr.2) | Supplies of collateral-assigned goods | Net amount | Net |
| 74 | -- (tax for Kz 73) | Tax on Kz 73 | Tax amount | Tax |
| 84 | Andere Leistungen (ss13b(2) Nr.1, 2, 4-12) | Other supplies under ss13b(2) | Net amount of construction services (Bauleistungen), building cleaning, scrap metal, telecommunications, gas/electricity, etc. | Net (tax auto-calculated) |
| 85 | -- (tax for Kz 84) | Tax on Kz 84 | Output VAT self-assessed | Tax amount |

**Note on Kz 46 vs Kz 84:** Kz 46/47 is used for supplies from foreign-based businesses (ss13b(1)). Kz 84/85 is used for domestic reverse charge scenarios under ss13b(2), including construction services, building cleaning, scrap metal, gas/electricity, mobile phones, and other specified categories.

#### Group F: Supplementary Information (Ergaenzende Angaben)

| Kz | German Name | English Name | What Goes In |
|----|-------------|--------------|--------------|
| 42 | Lieferungen des ersten Abnehmers bei innergemeinschaftlichen Dreiecksgeschaeften | Supplies by first buyer in IC triangular transactions | Net amount of supplies in triangular transaction where German business is the intermediate buyer |
| 60 | Steuerpflichtige Umsaetze fuer die der Leistungsempfaenger die Steuer schuldet | Taxable supplies where recipient owes the tax | Net amount of supplies made where the CUSTOMER is the reverse charge debtor (seller side reporting) |
| 21 | Nicht steuerbare sonstige Leistungen (ss18b S.1 Nr.2) | Non-taxable other services | Net amount of B2B services supplied to EU customers where place of supply is the recipient's country |

#### Group G: Input Tax (Vorsteuerbetraege)

| Kz | German Name | English Name | What Goes In | Entry |
|----|-------------|--------------|--------------|-------|
| 66 | Vorsteuerbetraege aus Rechnungen von anderen Unternehmern | Input tax from invoices of other businesses | VAT amount from domestic purchase invoices (standard input tax deduction under ss15(1) Nr.1 UStG) | Tax amount |
| 61 | Vorsteuerbetraege aus innergemeinschaftlichem Erwerb | Input tax from IC acquisitions | VAT amount self-assessed on intra-Community acquisitions (mirrors the output in Kz 89/93 group) | Tax amount |
| 67 | Vorsteuerbetraege aus Leistungen i.S.d. ss13b (Empfaenger als Steuerschuldner) | Input tax from ss13b reverse charge supplies | VAT amount self-assessed as input on reverse charge supplies (mirrors output in Kz 46/47 and Kz 84/85) | Tax amount |
| 63 | Vorsteuerbetraege aus der Inanspruchnahme von Sondervorauszahlung | Input tax from Sondervorauszahlung deduction | Deduction of the 1/11 Sondervorauszahlung in the last Voranmeldung of the calendar year (December or Q4) | Tax amount |
| 59 | Vorsteuerbetraege berichtigt (ss15a UStG) | Input tax corrections under ss15a | Adjustments for change of use of capital goods (Vorsteuerberichtigung) | Tax amount (+/-) |
| 64 | Vorsteuerbetraege aus Steuer nach ss13a(1) Nr.6 UStG | Input tax from ss13a(1) Nr.6 | Input VAT from supplies by farmers under Durchschnittssatzbesteuerung (flat-rate farmers) | Tax amount |

#### Group H: Derived / Summary Fields

| Kz | German Name | English Name | Calculation |
|----|-------------|--------------|-------------|
| 65 | Verbleibende Umsatzsteuer-Vorauszahlung / Ueberschuss | Remaining advance payment / excess | Total output tax minus total input tax. Positive = payment due. Negative = refund claim. |
| 39 | Anrechenbare Sondervorauszahlung fuer Dauerfristverlaengerung | Creditable Sondervorauszahlung | The 1/11 prepayment credited in the final period of the year |
| 83 | Umsatzsteuer (total) | Total output tax | Sum of all output VAT lines (from Groups A, D, E) |

### 1.3 Derived Calculation Formulas [T1]

```
Total Output Tax (Kz 83) =
    (Kz 81 * 0.19) + (Kz 86 * 0.07) + Kz 36
  + (Kz 89 * 0.19) + (Kz 93 * 0.07) + Kz 98
  + Kz 47 + Kz 85 + Kz 74

Total Input Tax =
    Kz 66 + Kz 61 + Kz 67 + Kz 63 + Kz 59 + Kz 64

Advance Payment / Refund (Kz 83 result) =
    Total Output Tax - Total Input Tax

Final Period Adjustment:
    Kz 65 = Advance Payment - Kz 39 (Sondervorauszahlung credit)

If Kz 65 > 0: VAT payable (Zahllast)
If Kz 65 < 0: VAT refund claim (Erstattungsanspruch)
```

### 1.4 Annual Declaration (Umsatzsteuererklaerung) [T1]

| Field | Value |
|-------|-------|
| Official Name | Umsatzsteuererklaerung (USt-E) |
| Legal Basis | ss18(3) UStG |
| Filing Deadline | 31 July of the following year (without Steuerberater); extended to end of February of the second following year (with Steuerberater) |
| Purpose | Reconciles all advance returns for the calendar year; serves as the definitive annual VAT assessment |
| Differences from USt-VA | Contains additional fields for annual adjustments: ss15a capital goods corrections, partial exemption annual adjustment, Kleinunternehmer declaration, and final reconciliation of all periodic returns against actual annual figures |
| Filing Method | Electronic via ELSTER only |

**Key difference:** The USt-E includes fields not present on the USt-VA, such as detailed breakdowns of exempt supply categories, ss15a multi-year capital goods adjustments, and the annual pro-rata calculation for partially exempt businesses.

---

## SECTION 2: Transaction Classification Matrix [T1]

### 2.1 Sales Classification

#### Sales of Goods

| Counterparty Location | VAT Status of Customer | Rate | Kz (Net) | Kz (Tax) | Reverse Charge? | Reporting |
|----------------------|----------------------|------|----------|----------|-----------------|-----------|
| Domestic (DE) | Any | 19% | 81 | auto-calc | No | -- |
| Domestic (DE) | Any | 7% | 86 | auto-calc | No | -- |
| Domestic (DE) | Any | Exempt | 48 | -- | No | -- |
| EU B2B | VAT-registered | 0% | 41 | -- | No (customer self-assesses) | ZM + Intrastat (if > threshold) |
| EU B2C | Non-registered | 19%/7% | 81/86 | auto-calc | No | Unless OSS applies |
| EU B2C (distance sales > EUR 10,000 EU-wide) | Non-registered | Destination rate | OSS | OSS | No | OSS return in destination state |
| EU (new vehicles) | Non-registered | 0% | 44 | -- | No | ZM |
| Non-EU (export) | Any | 0% | 43 | -- | No | Customs export documentation required |

#### Sales of Services

| Counterparty Location | VAT Status | Rate | Kz (Net) | Kz (Tax) | Reverse Charge? | Reporting |
|----------------------|------------|------|----------|----------|-----------------|-----------|
| Domestic (DE) | Any | 19% | 81 | auto-calc | No | -- |
| Domestic (DE) | Any | 7% | 86 | auto-calc | No | -- |
| Domestic (DE) | Any | Exempt | 48 | -- | No | -- |
| EU B2B (ss3a(2) general rule) | VAT-registered | 0% | 21 | -- | No (customer self-assesses) | ZM |
| EU B2C (ss3a(1) general rule) | Non-registered | 19% | 81 | auto-calc | No | Unless special rules apply |
| Non-EU B2B (ss3a(2)) | Any | 0% | 45 | -- | No | -- |
| Non-EU B2C | Non-registered | 19% | 81 | auto-calc | No | Unless place of supply is abroad |

### 2.2 Purchases Classification

#### Purchases of Goods

| Counterparty Location | Type | Rate | Kz (Net/Base) | Kz (Output Tax) | Kz (Input Tax) | Reverse Charge? | Reporting |
|----------------------|------|------|---------------|-----------------|----------------|-----------------|-----------|
| Domestic (DE) | Standard | 19% | -- | -- | 66 (enter tax amt) | No | -- |
| Domestic (DE) | Reduced | 7% | -- | -- | 66 (enter tax amt) | No | -- |
| EU B2B (IC acquisition) | Standard | 19% | 89 | auto-calc (19%) | 61 | Yes (self-assess) | Intrastat (if > threshold) |
| EU B2B (IC acquisition) | Reduced | 7% | 93 | auto-calc (7%) | 61 | Yes (self-assess) | Intrastat (if > threshold) |
| Non-EU (import) | Standard | 19% | -- | -- | 62 [T2] | No (EUSt paid at customs) | Customs C77/C78 document |

**Non-EU goods imports:** Import VAT (Einfuhrumsatzsteuer / EUSt) is paid to customs at the border. It is recovered as input tax via Kz 62 on the USt-VA using the customs assessment notice (Einfuhrabgabenbescheid). [T2] -- Steuerberater should confirm the correct Kennzahl as this has changed over time; some periods use Kz 66 with customs documents as supporting evidence.

#### Purchases of Services

| Counterparty Location | Type | Rate | Kz (Net/Base) | Kz (Output Tax) | Kz (Input Tax) | Reverse Charge? | Reporting |
|----------------------|------|------|---------------|-----------------|----------------|-----------------|-----------|
| Domestic (DE) | Standard | 19% | -- | -- | 66 | No | -- |
| Domestic (DE) | Reduced | 7% | -- | -- | 66 | No | -- |
| Domestic (DE) | ss13b construction | 19% | 84 | 85 | 67 | Yes | -- |
| Domestic (DE) | ss13b building cleaning | 19% | 84 | 85 | 67 | Yes | -- |
| EU B2B (ss13b(1)) | Standard | 19% | 46 | 47 | 67 | Yes | -- |
| EU B2B (ss13b(1)) | Reduced | 7% | 46 | 47 | 67 | Yes | -- |
| Non-EU B2B (ss13b(1)) | Standard | 19% | 46 | 47 | 67 | Yes | -- |
| Non-EU B2B (ss13b(1)) | Reduced | 7% | 46 | 47 | 67 | Yes | -- |
| Local consumption abroad (hotel/restaurant/taxi) | Foreign VAT | -- | -- | -- | -- | No | Not on DE return |

### 2.3 Reverse Charge Summary -- Both Sides [T1]

For every reverse charge transaction, the USt-VA must show BOTH the output side (tax liability) and the input side (deduction). For fully taxable businesses, the net effect is zero.

| Scenario | Output Side (Kz Net / Kz Tax) | Input Side (Kz) | Net Effect |
|----------|------------------------------|-----------------|------------|
| IC acquisition of goods 19% | 89 / auto-calc | 61 | Zero |
| IC acquisition of goods 7% | 93 / auto-calc | 61 | Zero |
| Services from foreign business (ss13b(1)) | 46 / 47 | 67 | Zero |
| Domestic construction reverse charge (ss13b(2) Nr.4) | 84 / 85 | 67 | Zero |
| Domestic building cleaning (ss13b(2) Nr.5a) | 84 / 85 | 67 | Zero |
| Scrap metal / gold (ss13b(2) Nr.7) | 84 / 85 | 67 | Zero |
| Mobile phones > EUR 5,000 (ss13b(2) Nr.10) | 84 / 85 | 67 | Zero |
| Gas/electricity from foreign supplier (ss13b(2) Nr.5) | 84 / 85 | 67 | Zero |

---

## SECTION 3: VAT Rates [T1]

**Legislation:** ss12 UStG.

### 3.1 Standard Rate: 19%

| Field | Value |
|-------|-------|
| Rate | 19% |
| Legal Basis | ss12(1) UStG |
| Applies To | All taxable supplies of goods and services not qualifying for reduced, zero, or exempt treatment |
| Effective | Since 1 January 2007 (increased from 16%) |

### 3.2 Reduced Rate: 7%

| Field | Value |
|-------|-------|
| Rate | 7% |
| Legal Basis | ss12(2) UStG |

**Categories qualifying for 7% (from ss12(2) Nr.1-14 UStG and Anlage 2):**

| Category | Description | Legal Basis |
|----------|-------------|-------------|
| Foodstuffs | Most food and drink products for human consumption (excluding restaurant services, alcoholic beverages, luxury food) | ss12(2) Nr.1, Anlage 2 Nr.1-31 |
| Animal feed | Feed for livestock and pets | ss12(2) Nr.1, Anlage 2 |
| Books and newspapers | Printed books, newspapers, periodicals, and e-books/e-periodicals (since 2020) | ss12(2) Nr.14 |
| Water supply | Supply of water by mains or tanker | ss12(2) Nr.1, Anlage 2 Nr.34 |
| Plants and flowers | Live plants, cut flowers, seeds | ss12(2) Nr.1, Anlage 2 Nr.7 |
| Firewood | Wood for fuel purposes | ss12(2) Nr.1, Anlage 2 |
| Medical devices | Certain prosthetics and orthopaedic goods | ss12(2) Nr.1, Anlage 2 Nr.51-52 |
| Cultural events | Admission to theatres, concerts, museums, zoos | ss12(2) Nr.7a |
| Passenger transport (short distance) | Local public transport (Nahverkehr, <= 50 km) | ss12(2) Nr.10 |
| Agricultural products | Certain raw agricultural outputs | ss12(2) Nr.1, Anlage 2 |
| Artwork | Supplies by the artist themselves (Urheberrechte) | ss12(2) Nr.7c [T2] |
| Accommodation | Short-term letting of accommodation (Beherbergung) since 2010 (excluding ancillary services like breakfast, parking, Wi-Fi at standard rate) | ss12(2) Nr.11 |
| Dental technicians | Supplies by dental technicians | ss12(2) Nr.6 |

### 3.3 Zero Rate: 0% for Photovoltaic Installations

| Field | Value |
|-------|-------|
| Rate | 0% |
| Legal Basis | ss12(3) UStG |
| Effective | Since 1 January 2023 |
| Applies To | Supply and installation of photovoltaic (solar) systems and essential components (inverters, battery storage) on or near residential buildings and public/community-use buildings, where the installed capacity does not exceed 30 kWp |
| Input Tax | Supplier charges 0% VAT. Purchaser pays no VAT. Supplier retains input tax deduction rights. |
| Condition | Installation must be on or near a dwelling or a building used for activities serving the public good (Gemeinwohl) |

### 3.4 Other Zero-Rated Supplies (Not ss12(3))

These are tax-free with input deduction under ss4 Nr.1-7 UStG, NOT a "0% rate" under ss12:

| Category | Legal Basis |
|----------|-------------|
| Intra-Community supplies of goods (B2B, shipped to another EU state) | ss4 Nr.1b + ss6a UStG |
| Exports to non-EU countries | ss4 Nr.1a + ss6 UStG |
| International transport services | ss4 Nr.3 UStG |
| Supplies to NATO forces | ss4 Nr.7a UStG |
| Cross-border goods transport (certain) | ss4 Nr.3 UStG |

### 3.5 Exempt Supplies (No Input Tax Deduction) -- ss4 Nr.8-29 UStG

| Category | Legal Basis |
|----------|-------------|
| Financial services (banking, lending, securities) | ss4 Nr.8 UStG |
| Insurance and reinsurance | ss4 Nr.10 UStG |
| Letting of immovable property (long-term) | ss4 Nr.12 UStG (option to tax under ss9 possible for B2B) |
| Healthcare and medical services | ss4 Nr.14 UStG |
| Education and training (state-recognised) | ss4 Nr.21-22 UStG |
| Social welfare services | ss4 Nr.16-18 UStG |
| Postal services (universal service obligation) | ss4 Nr.11b UStG |

### 3.6 Temporary Rate Changes (Historical Reference)

| Period | Standard Rate | Reduced Rate | Reason |
|--------|--------------|--------------|--------|
| 1 Jul 2020 -- 31 Dec 2020 | 16% | 5% | COVID-19 economic stimulus |
| 1 Jan 2021 onwards | 19% | 7% | Return to normal rates |
| Restaurant/catering food | 19% (reverted 1 Jan 2024) | 7% (temporary) | COVID measure extended then expired |

---

## SECTION 4: Blocked Input Tax (Non-Deductible Categories) [T1]

**Legislation:** ss15(1a) UStG; ss15(2) UStG; cross-references to ss4(5) EStG.

### 4.1 Blocked Categories Table

| Category | VAT Recovery Rule | Income Tax Rule | Legal Basis |
|----------|------------------|-----------------|-------------|
| **Entertainment/Bewirtungskosten** | **100% VAT RECOVERABLE** (if properly documented) | Only 70% of net deductible for income tax (30% disallowed) | ss15(1) Nr.1 UStG (VAT); ss4(5) Nr.2 EStG (income tax) |
| Business gifts > EUR 50 net per person per year | VAT NOT deductible | Not deductible for income tax either | ss15(1a) Nr.1 UStG; ss4(5) Nr.1 EStG |
| Hunting, fishing, yachts, guest houses, similar luxury | VAT NOT deductible | Not deductible | ss15(1a) Nr.1 UStG; ss4(5) Nr.1-4 EStG |
| Travel expenses -- private portion | VAT NOT deductible on private portion | Private portion not deductible | ss15(1) UStG |
| Motor vehicles -- private use portion | VAT on private use NOT deductible; must split by actual use or apply 1% rule / Fahrtenbuch | Private use taxed via 1% rule or Fahrtenbuch | ss15(1) UStG; ss6(1) Nr.4 EStG |
| Private use (Eigenverbrauch / unentgeltliche Wertabgabe) | Must charge output VAT on deemed supply | Treated as deemed withdrawal | ss3(1b), ss3(9a) UStG |
| Exempt supply-related purchases | VAT NOT deductible per ss15(2) | N/A | ss15(2) Nr.1 UStG |
| Input tax where no proper invoice exists | VAT NOT deductible | N/A | ss15(1) Nr.1 UStG (invoice requirement) |

### 4.2 CRITICAL: Entertainment (Bewirtung) VAT is Fully Recoverable [T1]

**This is a commonly misunderstood rule.** Unlike Malta and Ireland where entertainment VAT is blocked, in Germany:

- **VAT on business entertainment IS 100% recoverable** under ss15(1) Nr.1 UStG, provided:
  - A proper VAT invoice exists (maschinell erstellte Rechnung from the restaurant)
  - The back of the receipt documents: date, names of attendees, business purpose, and the host's signature
  - The entertainment has a concrete business reason (Bewirtung aus geschaeftlichem Anlass)

- **The 30% disallowance is ONLY an income tax rule** under ss4(5) Nr.2 EStG. It does NOT affect VAT recovery.

- Example: Business dinner EUR 200 net + EUR 38 VAT (19%). Kz 66 = EUR 38 (full VAT recovery). For income tax: only EUR 140 (70% of EUR 200) is deductible as a business expense.

### 4.3 Motor Vehicle Rules [T2]

| Method | Description | VAT Impact |
|--------|-------------|------------|
| **Fahrtenbuch** (logbook) | Actual business vs private km recorded daily | VAT deductible only on business-use percentage. Private portion: output VAT due as unentgeltliche Wertabgabe under ss3(9a) UStG. |
| **1% Regelung** | Private use deemed at 1% of gross list price per month for income tax | For VAT: private use portion triggers output VAT on deemed supply (ss3(9a) UStG). The VAT base is the actual costs attributable to private use, NOT the 1% figure. |
| **Business vehicle, no private use** | Vehicle used 100% for business (rare, must be proven) | 100% VAT recoverable. No output VAT adjustment. |

**Flag for reviewer:** The VAT treatment of private motor vehicle use is complex. The 1% income tax rule does NOT directly determine the VAT adjustment. Steuerberater must confirm the correct VAT base for the deemed supply. [T2]

### 4.4 Partial Deduction (ss15(4) UStG) [T2]

If a business makes both taxable and exempt supplies:

```
Recovery % = (Taxable Turnover / Total Turnover) * 100
```

- Must be calculated annually and reconciled in the Umsatzsteuererklaerung
- Advance returns use the prior year's pro-rata or an estimated ratio
- ss15(4) allows either a turnover-based split or an "other reasonable method" (sachgerechte Schaetzung)
- **Flag for reviewer: pro-rata must be confirmed by Steuerberater. Annual adjustment is mandatory.**

---

## SECTION 5: Registration [T1]

### 5.1 General Rule -- No Turnover Threshold for Standard Registration

| Field | Value |
|-------|-------|
| Rule | ALL commercial activity triggers a VAT obligation in Germany, unless the Kleinunternehmerregelung (ss19 UStG) is elected |
| Legal Basis | ss1(1), ss2(1) UStG |
| Registration Process | Submit Fragebogen zur steuerlichen Erfassung (Tax Registration Questionnaire) via ELSTER within one month of commencing business |
| USt-IdNr Format | DE + 9 digits (e.g. DE123456789) |
| USt-IdNr Issuing Authority | Bundeszentralamt fuer Steuern (BZSt), applied for via ELSTER or Form USt 1 TI |
| Steuernummer | Assigned by the local Finanzamt; used for domestic filings |

### 5.2 Kleinunternehmerregelung (ss19 UStG) [T1]

| Field | Value |
|-------|-------|
| Legal Basis | ss19(1) UStG (as amended from 1 January 2025) |
| Prior Year Threshold | Turnover (Umsatz) in the preceding calendar year <= EUR 25,000 |
| Current Year Threshold | Turnover in the current calendar year will not exceed EUR 100,000 |
| Effect | No VAT charged on invoices. No input tax (Vorsteuer) recovery. Must include notice on invoices: "Kein Ausweis von Umsatzsteuer aufgrund der Anwendung der Kleinunternehmerregelung gemaess ss19 UStG" |
| USt-VA Filing | Not required (exempt from advance returns) |
| Annual Declaration | MUST file annual Umsatzsteuererklaerung |
| Reverse Charge | ss13b reverse charge obligations STILL APPLY. Kleinunternehmer must self-assess VAT on EU/non-EU services received. |
| Option to Waive | Can voluntarily opt for standard taxation (Regelbesteuerung) under ss19(2) UStG. Binding for 5 calendar years. |

**From 2025:** An EU-wide Kleinunternehmer scheme allows small businesses to apply the exemption in other EU member states, subject to an EU-wide turnover ceiling of EUR 100,000 and individual member state thresholds. [T2] -- Details of cross-border application to be confirmed by Steuerberater.

### 5.3 Threshold Breach Mid-Year [T1]

If a Kleinunternehmer exceeds EUR 100,000 turnover during the current year:
- Kleinunternehmer status is **lost immediately** from the transaction that causes the breach (as of 2025 amendment)
- All subsequent supplies must be invoiced with VAT
- VAT registration obligations and advance return filing begin immediately
- Prior supplies in the year that were below the threshold remain VAT-free

---

## SECTION 6: Filing Deadlines and Penalties [T1]

### 6.1 Filing Deadlines

| Return Type | Period | Deadline | Legal Basis |
|-------------|--------|----------|-------------|
| Monthly USt-VA | Monthly | 10th of the following month | ss18(1) UStG |
| Quarterly USt-VA | Quarterly | 10th of the month after quarter end (10 Apr, 10 Jul, 10 Oct, 10 Jan) | ss18(2) UStG |
| Annual Umsatzsteuererklaerung (without Steuerberater) | Annual | 31 July of the following year | ss149(2) AO |
| Annual Umsatzsteuererklaerung (with Steuerberater) | Annual | End of February of the second following year (e.g. 28 Feb 2028 for tax year 2026) | ss149(3) AO |
| Zusammenfassende Meldung (ZM / EC Sales List) | Monthly (or quarterly if IC supplies < EUR 50,000) | 25th of the following month | ss18a UStG |
| Intrastat Declaration | Monthly | 10th working day of the following month | EU Regulation 2019/2152 |

### 6.2 Filing Frequency Thresholds [T1]

| Prior Year VAT Liability | Filing Frequency | Legal Basis |
|-------------------------|------------------|-------------|
| > EUR 9,000 | Monthly | ss18(2) UStG |
| EUR 2,000 -- EUR 9,000 | Quarterly | ss18(2) UStG |
| < EUR 2,000 | Exempt from advance returns (annual only) | ss18(2) UStG |
| First year + following year of new business | Monthly (mandatory) | ss18(2) S.4 UStG |

**Source for EUR 9,000 / EUR 2,000 thresholds:** Verified against PWC Tax Summaries Germany (https://taxsummaries.pwc.com/germany/corporate/other-taxes), accessed April 2026. [T2] -- These thresholds may have been updated by recent legislation; a Steuerberater should confirm they apply to the current filing period.

### 6.3 Dauerfristverlaengerung (Permanent Filing Extension) [T1]

| Field | Value |
|-------|-------|
| Legal Basis | ss46-48 UStDV |
| Effect | Extends the USt-VA filing deadline by ONE month |
| Condition | Must pay a Sondervorauszahlung (special advance payment) of 1/11 of the prior year's total VAT liability by 10 February |
| Application | Filed via ELSTER; once granted, applies until revoked |
| Year-End Credit | The Sondervorauszahlung is credited back in the last Voranmeldung of the year (Kz 39) |

### 6.4 Penalties [T1]

| Penalty Type | Amount | Legal Basis |
|-------------|--------|-------------|
| Verspaetungszuschlag (late filing surcharge) | 0.25% of the assessed tax per started month of delay, minimum EUR 25 per month | ss152 AO |
| Saeumniszuschlag (late payment surcharge) | 1% of the outstanding tax per started month of delay | ss240 AO |
| Zinsen (interest on late assessment) | 0.15% per month (1.8% per year) for periods after 15 months following the end of the tax year | ss233a, ss238 AO |
| Estimated assessment (Schaetzungsbescheid) | Finanzamt estimates tax liability if returns not filed; typically unfavourable | ss162 AO |
| Zwangsgeld (coercive fine) | Up to EUR 25,000 per instance to enforce filing | ss328-329 AO |
| Steuerhinterziehung (tax evasion) | Criminal offence; fines and/or imprisonment up to 5 years (up to 10 years in serious cases) | ss370 AO |

---

## SECTION 7: Reverse Charge Rules (ss13b UStG) [T1]

### 7.1 Complete ss13b Catalogue

| Provision | Category | German Name | Description | Kz (Base) | Kz (Output Tax) | Kz (Input Tax) |
|-----------|----------|-------------|-------------|-----------|-----------------|----------------|
| ss13b(1) | Foreign business supplies | Leistungen auslaendischer Unternehmer | ALL taxable supplies (goods and services) by businesses not established in Germany to German VAT-registered businesses | 46 | 47 | 67 |
| ss13b(2) Nr.1 | Work supplies / construction-related | Werklieferungen/sonstige Leistungen eines im Ausland ansaessigen Unternehmers | Supplies of work (Werklieferungen) and certain services by foreign businesses | 46 | 47 | 67 |
| ss13b(2) Nr.4 | Construction services (Bauleistungen) | Bauleistungen | Construction work, renovation, repair, demolition -- applies when BOTH supplier and recipient are construction businesses (Bauleistungen an Bauleistende) | 84 | 85 | 67 |
| ss13b(2) Nr.5 | Gas and electricity | Lieferungen von Gas/Elektrizitaet | Supply of gas and electricity by foreign suppliers through the German grid | 84 | 85 | 67 |
| ss13b(2) Nr.5a [T2] | Building cleaning services | Gebaeudereinigungsleistungen | Building cleaning services where both parties are in the cleaning industry | 84 | 85 | 67 |
| ss13b(2) Nr.6 | Telecommunications | Telekommunikationsdienstleistungen | Telecommunications services by foreign providers [T2] -- scope and applicability to be confirmed | 84 | 85 | 67 |
| ss13b(2) Nr.7 | Gold and scrap metal | Lieferungen von Gold / Schrott und Altmetallen | Supplies of investment gold, scrap metal, and used materials | 84 | 85 | 67 |
| ss13b(2) Nr.8 | Industrial emissions allowances | CO2-Emissionszertifikate | Transfer of greenhouse gas emission allowances | 84 | 85 | 67 |
| ss13b(2) Nr.9 [T2] | Mobile phones and circuit boards | Mobilfunkgeraete, Tablet-Computer, Spielekonsolen, integrierte Schaltkreise | When the invoice amount for these goods exceeds EUR 5,000 net | 84 | 85 | 67 |
| ss13b(2) Nr.10 | Precious metals and base metals | Edelmetalle und unedle Metalle | Supplies of precious metals (except gold under Nr.7) and certain base metals | 84 | 85 | 67 |
| ss13b(2) Nr.11 [T2] | Tablet computers and game consoles | (included in Nr.9 above in some legislative versions) | See Nr.9 -- scope varies by legislative version | 84 | 85 | 67 |

### 7.2 Intra-Community Acquisitions (ss1a UStG) [T1]

| Field | Value |
|-------|-------|
| Legal Basis | ss1a UStG |
| Trigger | B2B purchase of goods shipped from another EU state to Germany |
| Kz (Base) | 89 (19%) or 93 (7%) |
| Kz (Output Tax) | Auto-calculated |
| Kz (Input Tax) | 61 |
| Net Effect | Zero for fully taxable businesses |
| Additional Reporting | Intrastat (if shipment value exceeds threshold -- EUR 800,000 arrivals or EUR 500,000 dispatches per year) [T2] |

### 7.3 Import of Goods (Einfuhrumsatzsteuer -- EUSt) [T1]

| Field | Value |
|-------|-------|
| Legal Basis | ss1(1) Nr.4, ss11, ss21 UStG |
| Trigger | Physical goods imported from non-EU countries into Germany |
| VAT Rate | 19% (or 7% for reduced-rate goods) on customs value plus duties |
| Payment | Paid to Zoll (customs authority) at import, NOT self-assessed on the USt-VA |
| Recovery | Recoverable as input tax via Kz 62 [T2] (or Kz 66 with customs document as evidence -- to be confirmed by Steuerberater) |
| Document Required | Einfuhrabgabenbescheid (customs duty assessment) or C77/C78 customs entry |

### 7.4 Exceptions to Reverse Charge [T1]

| Situation | Treatment |
|-----------|-----------|
| Out-of-scope categories (wages, dividends, bank charges, loan repayments) | NEVER reverse charge |
| Local consumption abroad (hotel, restaurant, taxi, conference in another country) | NOT reverse charge; foreign VAT paid at source; not on German return |
| Kleinunternehmer receiving ss13b supplies | Reverse charge STILL APPLIES; ss13b overrides ss19 |
| Supplies from EU businesses where supplier charged local VAT | NOT reverse charge; foreign VAT is embedded in expense |
| B2C supplies from foreign businesses (where supplier should have registered in DE) | Generally not ss13b; supplier should register and charge German VAT |

---

## SECTION 8: Edge Cases [T1/T2]

### EC1 -- Entertainment (Bewirtung): VAT Fully Deductible [T1]

**Situation:** Client entertains business partners at a restaurant. Bill: EUR 200 net + EUR 38 VAT (19%).
**Resolution:** VAT is 100% deductible. Kz 66 = EUR 38. For income tax purposes, only 70% of the net (EUR 140) is deductible. The 30% disallowance is an income tax rule (ss4(5) Nr.2 EStG), NOT a VAT rule. Invoice must document: restaurant name, date, attendees (including from own company), business purpose. The annotation must be on the reverse of the original receipt.
**Legislation:** ss15(1) Nr.1 UStG (full VAT deduction); ss4(5) Nr.2 EStG (70% income tax limit only).

### EC2 -- Private Use of Business Car (1% Regelung vs Fahrtenbuch) [T2]

**Situation:** Client uses a company car 60% for business, 40% privately.
**Resolution:** Input VAT on purchase/lease/fuel is recoverable only to the extent of business use. The private use portion triggers a deemed supply (unentgeltliche Wertabgabe) under ss3(9a) UStG, and output VAT must be charged on the private use portion. The VAT base for the deemed supply is the actual costs, NOT the 1% income tax amount.
**Flag for reviewer:** Confirm usage split method (Fahrtenbuch vs estimated). Confirm VAT base for deemed supply.
**Legislation:** ss15(1) UStG; ss3(9a) UStG; ss10(4) Nr.2 UStG.

### EC3 -- Intra-Community Supply: Proof Requirements [T1]

**Situation:** Client sells goods to a French business, ships DE to FR, invoices at 0%.
**Resolution:** Tax-free IC supply under ss4 Nr.1b + ss6a UStG. Report net in Kz 41. Also report in ZM (Zusammenfassende Meldung). Required proof (Gelangensbestaetigung or alternative under ss17a-17c UStDV):
- Gelangensbestaetigung (arrival confirmation) signed by the customer, OR
- CMR/bill of lading + customer confirmation, OR
- Tracking/shipment confirmation from the carrier
**Without valid proof, zero-rating is denied and 19% VAT must be charged retroactively.**
**Legislation:** ss4 Nr.1b, ss6a UStG; ss17a-17c UStDV.

### EC4 -- Reverse Charge Construction (ss13b Bauleistungen) [T1]

**Situation:** German subcontractor provides plumbing installation to a German general contractor.
**Resolution:** Reverse charge applies under ss13b(2) Nr.4 ONLY if the recipient (general contractor) itself provides construction services as part of its business (is a "Bauleistender"). The subcontractor invoices without VAT. General contractor self-assesses: Kz 84 (base), Kz 85 (output VAT 19%), Kz 67 (input VAT). Both parties must be in the construction trade.
**If the recipient is NOT a construction business** (e.g., a law firm having its office renovated), reverse charge does NOT apply. The subcontractor charges normal VAT.
**Legislation:** ss13b(2) Nr.4, ss13b(5) S.2 UStG; BMF letter of 10 Aug 2004.

### EC5 -- Kleinunternehmer Threshold Breach Mid-Year [T1]

**Situation:** Kleinunternehmer client has EUR 90,000 turnover by October and expects to exceed EUR 100,000.
**Resolution:** From 2025, if the EUR 100,000 current-year threshold is exceeded, Kleinunternehmer status is lost immediately from the supply that causes the breach. The client must:
1. Begin charging VAT on all subsequent invoices
2. Register for standard VAT (if not already registered)
3. File USt-VA for the remaining periods
4. Can now recover input VAT on purchases from the date status was lost
**Legislation:** ss19(1) UStG (as amended 2025).

### EC6 -- Photovoltaic Installations at 0% [T1]

**Situation:** Homeowner buys and installs a 10 kWp solar system on their house for EUR 15,000.
**Resolution:** 0% VAT under ss12(3) UStG (since 1 Jan 2023). The installer invoices at 0%. No VAT charged to the homeowner. The installer retains full input tax deduction rights on their own purchases. The system must be on or near a dwelling (or public benefit building) and not exceed 30 kWp.
**Legislation:** ss12(3) UStG.

### EC7 -- Differenzbesteuerung (Margin Scheme) [T2]

**Situation:** Used car dealer purchases a car from a private individual for EUR 8,000 and sells it for EUR 10,000.
**Resolution:** Under the margin scheme (ss25a UStG), VAT is calculated only on the margin (EUR 2,000), not the full selling price. VAT = EUR 2,000 / 1.19 * 0.19 = EUR 319.33 (VAT is included in the margin). The dealer reports in Kz 81 but only the margin-based amount. The purchase from a private individual has no input VAT.
**Conditions:** Only applies to used goods, works of art, collectors' items, and antiques purchased from non-VAT-registered sellers (private individuals, Kleinunternehmer, or other margin scheme dealers).
**Flag for reviewer:** Confirm eligibility. Confirm margin calculation.
**Legislation:** ss25a UStG.

### EC8 -- Ist-Versteuerung (Cash Basis) Timing [T1]

**Situation:** Client is approved for Ist-Versteuerung (cash basis, turnover <= EUR 600,000). Client issues an invoice for EUR 10,000 + EUR 1,900 VAT in December but receives payment in January.
**Resolution:** Under Ist-Versteuerung, output VAT is due when payment is received, not when the invoice is issued. The EUR 1,900 output VAT goes in the January USt-VA, not December. Input tax deduction for the client's own purchases remains on the invoice date (ss15 UStG is always accrual-based for input tax).
**Legislation:** ss20 UStG (cash basis option); ss13(1) Nr.1a UStG (accrual default); ss15(1) UStG (input tax timing).

### EC9 -- Import VAT (Einfuhrumsatzsteuer) Recovery [T2]

**Situation:** Client imports goods from China. Customs charges EUR 3,800 EUSt (19% on customs value of EUR 20,000).
**Resolution:** The EUSt is paid at the border to the Zollamt (customs office). It is recoverable as input tax on the USt-VA. The client needs the Einfuhrabgabenbescheid (customs assessment notice) as documentation. Report the recoverable EUSt in Kz 62 (or Kz 66 -- confirm with Steuerberater which Kennzahl is current).
**Flag for reviewer:** Confirm the correct Kz for EUSt recovery in the current filing period.
**Legislation:** ss15(1) Nr.2 UStG; ss21 UStG.

### EC10 -- Credit Notes: Gutschrift vs Stornorechnung [T1]

**Situation:** Client needs to issue a correction for an incorrect invoice.
**Resolution:** German tax law distinguishes:
- **Gutschrift (ss14 UStG):** A credit note issued by the RECIPIENT (buyer) to themselves, acting as an invoice on behalf of the supplier. This is a form of self-billing. It creates output tax liability for the supplier.
- **Stornorechnung / Rechnungskorrektur:** A correction invoice issued by the SUPPLIER to cancel or amend a previous invoice. This is the typical "credit note" in common parlance.
- For VAT purposes, both reduce the original Kz entries. A Stornorechnung in period 2 that corrects a period 1 invoice: adjust the relevant Kz in period 2 by the negative amounts.
**Legislation:** ss14(2) S.2 UStG (Gutschrift); ss14c, ss17 UStG (corrections).

### EC11 -- EU Hotel / Restaurant / Taxi Booked Abroad [T1]

**Situation:** Client pays for a hotel in France via credit card. Invoice shows French VAT.
**Resolution:** NOT reverse charge. French VAT was charged and paid at source. This is local consumption in France. No entry on the German USt-VA. The French VAT is an irrecoverable cost (unless the client applies for a VAT refund under the EU VAT Refund Directive 2008/9/EC via the BZSt portal -- separate process, not part of the USt-VA).
**Legislation:** ss3a(3) Nr.1 UStG (place of supply for accommodation/restaurant = where property is located / where physically performed).

### EC12 -- Organschaft (VAT Group) [T3]

**Situation:** Client is part of a VAT group (Organschaft) with parent and subsidiaries.
**Resolution:** ESCALATE. Under ss2(2) Nr.2 UStG, an Organschaft creates a single taxable entity for VAT purposes. Internal supplies between group members are non-taxable (Innenumsaetze). The controlling entity (Organtraeger) files a single USt-VA for the entire group. Complex conditions apply (financial, economic, and organisational integration). Do NOT classify without Steuerberater guidance.
**Legislation:** ss2(2) Nr.2 UStG.

### EC13 -- SaaS Subscription from US Provider [T1]

**Situation:** Monthly charge from a US company (e.g. AWS, Notion, Slack), no VAT shown on invoice.
**Resolution:** Reverse charge applies under ss13b(1). Place of supply is Germany under ss3a(2) UStG (B2B general rule: recipient's location). Self-assess: Kz 46 = net amount (base), Kz 47 = output VAT at 19%, Kz 67 = input VAT at 19%. Net effect zero for fully taxable business.
**Legislation:** ss13b(1) UStG; ss3a(2) UStG.

### EC14 -- Business Gift Exceeding EUR 50 [T1]

**Situation:** Client gives a bottle of wine worth EUR 80 net to a business partner.
**Resolution:** Input VAT is BLOCKED under ss15(1a) Nr.1 UStG (cross-referencing ss4(5) Nr.1 EStG). The EUR 50 threshold is per recipient per calendar year. If total gifts to one recipient exceed EUR 50 net in a year, ALL VAT on gifts to that recipient is blocked (not just the excess). Kz 66 = EUR 0.
**Legislation:** ss15(1a) Nr.1 UStG; ss4(5) Nr.1 EStG.

---

## SECTION 9: Test Suite

### Test 1 -- Standard Domestic Purchase at 19% [T1]

**Input:** German supplier, office supplies, gross EUR 238, VAT EUR 38, net EUR 200. Standard-registered (Regelbesteuerung) client.
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 66 | EUR 38 | Input tax deductible |
Full recovery. No restrictions.

### Test 2 -- Reduced Rate Purchase at 7% [T1]

**Input:** German supplier, books for office library, gross EUR 107, VAT EUR 7, net EUR 100. Standard-registered client.
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 66 | EUR 7 | Input tax deductible (reduced rate) |
Full recovery.

### Test 3 -- Reverse Charge from EU Service Provider [T1]

**Input:** Irish law firm provides legal advice to German client. Invoice EUR 5,000, no VAT charged. Both are VAT-registered businesses.
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 46 | EUR 5,000 | Base amount (services from foreign business, ss13b(1)) |
| 47 | EUR 950 | Output VAT self-assessed (19%) |
| 67 | EUR 950 | Input VAT deductible |
Net VAT effect = zero.

### Test 4 -- Reverse Charge from Non-EU Service Provider [T1]

**Input:** US company (AWS) charges EUR 1,000 for cloud services. No VAT on invoice. Standard-registered German client.
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 46 | EUR 1,000 | Base amount (ss13b(1)) |
| 47 | EUR 190 | Output VAT self-assessed (19%) |
| 67 | EUR 190 | Input VAT deductible |
Net VAT effect = zero.

### Test 5 -- Intra-Community Goods Acquisition (EU Purchase) [T1]

**Input:** French supplier ships goods to Germany. Invoice EUR 5,000, no VAT. Client is standard-registered. Goods subject to 19%.
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 89 | EUR 5,000 | IC acquisition base (19%) |
| (auto) | EUR 950 | Output VAT auto-calculated |
| 61 | EUR 950 | Input VAT on IC acquisition |
Net VAT effect = zero.

### Test 6 -- Intra-Community Goods Supply (Zero-Rated EU Sale) [T1]

**Input:** German client sells goods worth EUR 3,000 to an Italian VAT-registered business. Goods shipped from DE to IT. Italian customer USt-IdNr verified.
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 41 | EUR 3,000 | IC supply (tax-free with input deduction) |
No output VAT. Must also file ZM (Zusammenfassende Meldung) showing the Italian customer's VAT ID and net amount.

### Test 7 -- Export to Non-EU [T1]

**Input:** German client exports machinery worth EUR 50,000 to a customer in the USA. Customs export documentation obtained.
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 43 | EUR 50,000 | Export supply (tax-free with input deduction) |
No output VAT. Customs export proof required.

### Test 8 -- Blocked Input: Private Use Portion of Car [T2]

**Input:** Standard-registered client purchases a company car for EUR 40,000 net + EUR 7,600 VAT. Fahrtenbuch shows 70% business, 30% private use.
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 66 | EUR 7,600 | Full input VAT initially claimed |
Private use portion (30%) triggers a deemed supply. Output VAT on private use must be reported:
| Kz | Amount | Description |
|----|--------|-------------|
| 81 or other | Based on actual private-use costs | Output VAT on deemed supply (ss3(9a) UStG) |
**Flag for reviewer:** Confirm private use percentage and correct Kz for deemed supply output. The output VAT base is the actual costs attributable to private use, not 30% of the purchase price.

### Test 9 -- ss13b Construction Reverse Charge [T1]

**Input:** German subcontractor (plumber) invoices EUR 10,000 for plumbing work on a building site. No VAT charged. Recipient is a German construction company (Bauleistender).
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 84 | EUR 10,000 | Base (ss13b(2) Nr.4 construction services) |
| 85 | EUR 1,900 | Output VAT self-assessed (19%) |
| 67 | EUR 1,900 | Input VAT deductible |
Net VAT effect = zero.

### Test 10 -- Kleinunternehmer Scenario [T1]

**Input:** Kleinunternehmer client (ss19 UStG) purchases office chair for EUR 500 gross. Prior year turnover EUR 20,000, current year projected EUR 40,000.
**Expected Output:**
No USt-VA entry. No input tax recovery. EUR 500 is the full expense.
Kleinunternehmer does not file advance returns and cannot recover Vorsteuer.

### Test 11 -- Entertainment (Bewirtung) Full VAT Recovery [T1]

**Input:** Standard-registered client hosts business dinner. Restaurant bill: EUR 300 net + EUR 57 VAT (19%). Properly documented (attendees, business purpose on back of receipt).
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 66 | EUR 57 | Input VAT -- FULLY recoverable |
For income tax: only EUR 210 (70% of EUR 300) deductible as business expense. The 30% block is income tax only, not VAT.

### Test 12 -- Exempt Supply (Healthcare) [T1]

**Input:** Doctor provides medical services to patients. Monthly revenue EUR 15,000. All services exempt under ss4 Nr.14 UStG.
**Expected Output:**
| Kz | Amount | Description |
|----|--------|-------------|
| 48 | EUR 15,000 | Exempt supplies without input tax deduction |
No output VAT. Input VAT on related purchases is NOT recoverable under ss15(2) Nr.1 UStG.

### Test 13 -- Photovoltaic System at 0% [T1]

**Input:** Homeowner purchases and has installed a 10 kWp solar system for EUR 12,000 from a VAT-registered installer.
**Expected Output (from installer's perspective):**
| Kz | Amount | Description |
|----|--------|-------------|
| 81 or 86 | EUR 0 | Not applicable -- 0% rate |
| Special Kz for 0% PV [T2] | EUR 12,000 | Supply at 0% under ss12(3) UStG |
**Flag for reviewer:** Confirm the exact Kz for 0% PV supplies. The supply is taxable at 0%, NOT exempt. The installer retains full input tax deduction rights.

### Test 14 -- EU Hotel (Local Consumption Exception) [T1]

**Input:** Standard-registered client pays for a hotel in Spain. EUR 400 including Spanish VAT EUR 36.
**Expected Output:**
No German VAT return entry. Expense is EUR 400 gross including irrecoverable Spanish VAT. Not reverse charge. Client may apply for refund via EU VAT Refund Directive (separate process).

---

## SECTION 10: Comparison with Malta

| Feature | Germany (DE) | Malta (MT) |
|---------|-------------|------------|
| **Primary Legislation** | UStG (Umsatzsteuergesetz) | VAT Act Chapter 406 |
| **Standard Rate** | 19% | 18% |
| **Reduced Rates** | 7% (food, books, accommodation, local transport, etc.) | 7% (accommodation), 5% (electricity, certain cultural), 12% (certain) |
| **Zero Rate** | 0% for photovoltaic systems (ss12(3)); tax-free exports/IC supplies with input deduction | 0% for exports and certain food/pharmaceutical items |
| **Small Business Exemption** | Kleinunternehmer ss19: EUR 25,000 prior year / EUR 100,000 current year | Article 11: EUR 35,000 domestic turnover |
| **Small Business VAT Recovery** | No (Kleinunternehmer cannot recover Vorsteuer) | No (Article 11 cannot recover input VAT) |
| **Return Form** | USt-VA (Umsatzsteuer-Voranmeldung) | VAT3 |
| **Box/Field System** | Kennzahl (Kz) numbers | Box numbers |
| **Filing Portal** | ELSTER | CFR Online (cfr.gov.mt) |
| **Filing Frequency** | Monthly (>EUR 9,000), Quarterly (EUR 2,000-9,000), Annual (<EUR 2,000) | Quarterly (Article 10), Annual (Article 11), Monthly (Article 12) |
| **Filing Deadline** | 10th of following month/quarter | 21st (e-filing) / 14th (paper) of month after quarter |
| **Filing Extension** | Dauerfristverlaengerung: +1 month (requires 1/11 Sondervorauszahlung) | No equivalent automatic extension |
| **Entertainment VAT** | **FULLY RECOVERABLE** (100% VAT deduction; 30% income tax block only) | **BLOCKED** (10th Schedule Item 3(1)(b); 0% recovery) |
| **Motor Vehicle VAT** | Deductible for business-use portion; private use triggers deemed supply | **BLOCKED** (10th Schedule; exception for taxis, driving schools, etc.) |
| **Capital Goods Threshold** | No single threshold; ss15a adjustment for assets > EUR 1,000 net over 5 years (10 years for immovable property) [T2] | EUR 1,160 gross (Article 24) |
| **Reverse Charge (Domestic)** | Extensive ss13b catalogue (construction, cleaning, scrap, telecoms, etc.) | Limited domestic reverse charge |
| **Reverse Charge (EU Services)** | ss13b(1): Kz 46/47/67 | Article 20: Box 9a/13a/Box 3/6 |
| **Reverse Charge (Non-EU Services)** | ss13b(1): Kz 46/47/67 | Article 20: Box 11/15/Box 4/7 |
| **Import VAT** | EUSt paid at customs; recovered via USt-VA | Paid at customs (C88); recovered via VAT3 |
| **EC Sales List** | Zusammenfassende Meldung (ZM), monthly (or quarterly if <EUR 50,000) | Recapitulative Statement, quarterly |
| **Intrastat** | Arrivals >EUR 800,000 / Dispatches >EUR 500,000 [T2] | Lower thresholds (smaller economy) |
| **Late Filing Penalty** | 0.25% per month, min EUR 25 (ss152 AO) | Penalties under VAT Act |
| **Late Payment** | 1% per started month (ss240 AO) | Interest on late payment |
| **Partial Exemption** | ss15(4) UStG -- turnover-based or sachgerechte Schaetzung | Article 22(4) -- turnover-based pro-rata |
| **Annual Declaration** | Umsatzsteuererklaerung -- reconciles all advance returns | N/A for Article 10 (quarterly is final); Article 11 files annual declaration |
| **Blocked Categories** | Narrower: gifts >EUR 50, luxury (hunting/yachts), exempt-related. Entertainment NOT blocked. | Broader: entertainment, motor vehicles, tobacco, alcohol, art, pleasure craft, personal use |
| **Margin Scheme** | ss25a UStG (Differenzbesteuerung) | Margin scheme available |
| **VAT Groups** | Organschaft (ss2(2) Nr.2 UStG) -- complex | Limited VAT grouping provisions |
| **Cash Basis Option** | Ist-Versteuerung (ss20 UStG) if turnover <= EUR 600,000 | Not a standard option |

---

## PROHIBITIONS [T1]

1. NEVER let AI guess Kennzahl numbers -- they are 100% deterministic from the facts established in the classification steps
2. NEVER apply Kleinunternehmer exemption if either threshold is exceeded (EUR 25,000 prior year OR EUR 100,000 current year)
3. NEVER skip reverse charge for Kleinunternehmer on ss13b supplies -- reverse charge overrides ss19
4. NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges, loan repayments, social contributions)
5. NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi in another country)
6. NEVER confuse zero-rated exports/IC supplies (input VAT deductible, Kz 41/43/45) with exempt supplies (input VAT NOT deductible, Kz 48)
7. NEVER allow Kleinunternehmer to claim input tax recovery
8. NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
9. NEVER apply ss13b(2) Nr.4 construction reverse charge when the recipient is not itself a construction business
10. NEVER treat the 30% entertainment (Bewirtung) income tax disallowance as a VAT rule -- entertainment VAT is fully recoverable in Germany
11. NEVER file a USt-VA on paper -- electronic filing via ELSTER is mandatory
12. NEVER apply Differenzbesteuerung (margin scheme) to goods purchased from VAT-registered businesses who charged VAT on the full amount
13. NEVER report import VAT (EUSt) as a reverse charge -- it is paid at customs and recovered as input tax, not self-assessed on the USt-VA
14. NEVER confuse Gutschrift (self-billing by buyer) with Stornorechnung (correction by seller) -- they have different legal meanings in German tax law

---

## Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Do not execute any of these rules. Escalate to Steuerberater.

| Tax | Rate | Notes |
|-----|------|-------|
| Einkommensteuer (income tax) | Progressive 0%-45% | Plus 5.5% Solidaritaetszuschlag on tax amount |
| Koerperschaftsteuer (corporate tax) | 15% flat | Plus 5.5% Soli = 15.825% effective |
| Gewerbesteuer (trade tax) | Varies by municipality | Typically 7-17% effective (Hebesatz varies) |
| Kirchensteuer (church tax) | 8-9% of income tax | Only for church members |
| Sozialversicherung (social insurance) | Employer + employee contributions | Separate obligation, out of scope |

---

## Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Steuerberater must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to Steuerberater. Document gap.
```

---

## Contribution Notes

This skill was developed using:
- UStG (Umsatzsteuergesetz) as primary legislation source
- PWC Tax Summaries Germany (https://taxsummaries.pwc.com/germany/corporate/other-taxes) for verification of rates and thresholds
- Malta VAT Return Skill as structural template

**Filing thresholds (EUR 9,000 monthly / EUR 2,000 quarterly relief) and Kleinunternehmer thresholds (EUR 25,000 / EUR 100,000) were verified against PWC Tax Summaries as of April 2026.** The EUR 9,000 / EUR 2,000 thresholds differ from older references that cite EUR 7,500 / EUR 1,000; the PWC source reflects current law. [T2] -- A Steuerberater should confirm these thresholds apply to the specific filing periods in question.

**A skill may not be published without sign-off from a Steuerberater (licensed tax advisor) in Germany.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
