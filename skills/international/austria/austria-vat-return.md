---
name: austria-vat-return
description: Use this skill whenever asked to prepare, review, or create an Austrian VAT return (Umsatzsteuervoranmeldung / UVA) or annual VAT declaration (Umsatzsteuererklaerung / U1) for any client. Trigger on phrases like "prepare VAT return", "do the Austrian VAT", "fill in UVA", "Umsatzsteuer Oesterreich", "Austrian VAT filing", "Kennzahl mapping", or any request involving Austrian VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Austrian VAT classification rules, UVA Kennzahl mappings, deductibility rules, reverse charge treatment, Fiskal-LKW rules, Differenzbesteuerung, Kleinunternehmerregelung, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Austria.
status: deep-research-verified
version: 1.1
---

# Austria VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Austria |
| Jurisdiction Code | AT |
| Primary Legislation | Umsatzsteuergesetz 1994 (UStG 1994) |
| Supporting Legislation | UStG 1994 §6 (exemptions); §10 (rates); §12 (input tax deduction); §19 (reverse charge); §6(1)(27) (Kleinunternehmerregelung); §21 (filing obligations); §24 (agriculture/forestry flat-rate); Binnenmarktregelung (BMR) for intra-EU |
| Tax Authority | Bundesministerium fuer Finanzen (BMF) / Finanzamt Oesterreich |
| Filing Portal | FinanzOnline (https://finanzonline.bmf.gv.at) |
| VAT Return Form | U30 (Umsatzsteuervoranmeldung / UVA -- monthly/quarterly) |
| Annual Declaration Form | U1 (Umsatzsteuererklaerung -- annual) |
| Contributor | Deep research verified -- April 2026 |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: Kennzahl assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial deduction, sector-specific, Differenzbesteuerung. Tier 3: Organschaft, complex group structures, special agricultural flat-rate scheme. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A Steuerberater must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to Steuerberater and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and UID-Nummer** [T1] -- Format: ATU + 8 digits (e.g., ATU12345678). Required for all VAT-registered entities. Issued by Finanzamt upon registration via FinanzOnline.
2. **VAT registration status** [T1] -- Regelbesteuerung (standard taxation), Kleinunternehmer (small business exempt per §6(1)(27) UStG 1994), or Pauschalierung (flat-rate for agriculture/forestry per §24 UStG 1994).
3. **Soll- or Ist-Versteuerung** [T1] -- Soll-Versteuerung = accrual basis (default); Ist-Versteuerung = cash basis (available if turnover < EUR 700,000 for most businesses; EUR 110,000 for certain freelancers). **Legislation:** §17 UStG 1994.
4. **Filing frequency** [T1] -- Monthly (prior calendar year turnover > EUR 100,000) or quarterly (turnover <= EUR 100,000). **Legislation:** §21(1) UStG 1994.
5. **Industry/sector** [T2] -- impacts partial deduction (e.g., real estate, medical, financial services).
6. **Does the business make exempt supplies (§6 UStG 1994)?** [T2] -- If yes, input tax restriction under §12(3) UStG 1994.
7. **USt credit carried forward from prior period** [T1] -- Gutschrift from previous UVA.
8. **Does the client own or lease motor vehicles?** [T1] -- Determines Vorsteuerabzug blocking rules under §12(2)(2)(b) UStG 1994.
9. **Does the client make construction-sector supplies?** [T1] -- Determines Bauleistungen reverse charge under §19(1a) UStG 1994.

For Kleinunternehmer [T1]: confirm annual gross turnover <= EUR 55,000 (§6(1)(27) UStG 1994, as amended by Progressionsentlastungsgesetz 2025, effective 1 January 2025; threshold increased from prior EUR 35,000 net). One-time tolerance of 10% (to EUR 60,500) allowed -- if exceeded during the year, USt applies from the supply that causes the breach. The EU-wide SME scheme (from 1 January 2025) allows cross-border Kleinunternehmer status, subject to EU-wide EUR 100,000 turnover cap plus domestic threshold.

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration type and basis are confirmed.**

---

## Section 1: VAT Return Form Structure

### 1A. Umsatzsteuervoranmeldung (UVA) -- Form U30 [T1]

**Legislation:** §21 UStG 1994.

The UVA (form U30) is filed monthly or quarterly via FinanzOnline. It contains Kennzahlen (abbreviated Kz) that map to specific transaction types. The form is divided into the following sections:

#### Section I -- Lieferungen, sonstige Leistungen und Eigenverbrauch (Supplies, Services, Own Consumption)

| Kennzahl | German Name | English Translation | What Goes In |
|----------|-------------|---------------------|--------------|
| Kz 000 | Lieferungen und Leistungen zum Normalsteuersatz (20%) | Supplies at standard rate (20%) | Net value of all domestic taxable supplies at 20%. Excludes reverse charge supplies. UStG 1994 §10(1). |
| Kz 001 | Lieferungen und Leistungen zum ermaessigten Steuersatz (10%) | Supplies at reduced rate (10%) | Net value of domestic supplies taxed at 10%: basic foodstuffs, books, newspapers, passenger transport, water supply, pharmaceuticals, accommodation (subject to temporary rules). UStG 1994 §10(2). |
| Kz 006 | Lieferungen und Leistungen zum ermaessigten Steuersatz (13%) | Supplies at intermediate rate (13%) | Net value of domestic supplies at 13%: live animals, plants, firewood, cultural events (theatre, concerts, museums, zoos), wine sold directly by producers (Ab-Hof-Verkauf), domestic flights, swimming pools, athletic events. UStG 1994 §10(3). |
| Kz 007 | Umsaetze zum Steuersatz 19% (Jungholz/Mittelberg) | Supplies at 19% rate (Jungholz/Mittelberg) | Net value of supplies in the exclave municipalities of Jungholz and Mittelberg only. Rare. UStG 1994 §10(4). |
| Kz 009 | Steuerschuld gemaess §11(12) und (14) | Tax liability per §11(12) and (14) | USt amount shown on an invoice that exceeds the correct amount (incorrect higher tax shown). Tax is owed on the invoice amount. UStG 1994 §11(12), §11(14). |
| Kz 021 | Nicht steuerbare sonstige Leistungen gemaess Art 6 Abs 1 BMR | Non-taxable services per Art 6(1) BMR | Net value of B2B services to EU recipients where place of supply is the recipient's country (reverse charge shifts to recipient). Reported for informational/ZM purposes only. |
| Kz 011 | Ausfuhrlieferungen (§6 Abs 1 Z 1 UStG) | Export deliveries | Net value of goods exported to non-EU countries. Zero-rated with input tax credit. UStG 1994 §6(1)(1). |
| Kz 012 | Lohnveredelungen (§6 Abs 1 Z 1 UStG) | Contract processing for export | Net value of contract processing/tolling on goods subsequently exported. UStG 1994 §6(1)(1). |
| Kz 015 | Innergemeinschaftliche Lieferungen von Gegenstaenden | Intra-Community supplies of goods | Net value of goods supplied to VAT-registered businesses in other EU Member States. Zero-rated. Requires valid UID of recipient. Art 6 BMR; UStG 1994 §6(1)(1). |
| Kz 017 | Innergemeinschaftliche Lieferungen (Art 7 BMR) | IC supplies (Art 7 BMR) | Alternative Kz for IC supplies -- the primary Kennzahl used on the U30 form for IC supplies of goods. Art 7 BMR. |
| Kz 016 | Steuerfrei ohne Vorsteuerabzug (Kleinunternehmer) | Tax-exempt without input credit (Kleinunternehmer) | Net value of supplies made by Kleinunternehmer. No USt charged. No Vorsteuer recovery. UStG 1994 §6(1)(27). |
| Kz 020 | Steuerfrei mit Vorsteuerabzug / ohne Vorsteuerabzug | Tax-exempt (various) | Net value of exempt supplies under §6(1) UStG 1994: financial services §6(1)(8), insurance §6(1)(9), medical §6(1)(19), education §6(1)(11), real estate letting §6(1)(16). |
| Kz 022 | Umsaetze, fuer die der Leistungsempfaenger die Steuer schuldet | Supplies where recipient owes tax | Net value of supplies where Austrian supplier invoices without USt because recipient is liable (domestic reverse charge under §19(1a)-(1e)). |

#### Section II -- Innergemeinschaftliche Erwerbe (Intra-Community Acquisitions)

| Kennzahl | German Name | English Translation | What Goes In |
|----------|-------------|---------------------|--------------|
| Kz 070 | Innergemeinschaftliche Erwerbe von Gegenstaenden | IC acquisitions of goods | Net value of goods acquired from other EU Member States. Self-assess output USt at applicable Austrian rate. Art 1 BMR. |
| Kz 071 | Innergemeinschaftliche Erwerbe neuer Fahrzeuge | IC acquisition of new vehicles | Net value of new vehicles acquired from other EU Member States. Special reporting. Art 1 BMR. |
| Kz 072 | Innergemeinschaftliche Erwerbe (steuerfrei, §6 Abs 2) | IC acquisitions (exempt) | Net value of exempt IC acquisitions (rare). Art 6(2) BMR. |
| Kz 073 | Innergemeinschaftliche Erwerbe (ermaessigt 10%) | IC acquisitions at 10% | Net value of IC acquisitions subject to 10% rate. |
| Kz 008 | Innergemeinschaftliche Erwerbe (ermaessigt 13%) | IC acquisitions at 13% | Net value of IC acquisitions subject to 13% rate. |

#### Section III -- Berechnung der Umsatzsteuer (Calculation of Output Tax)

| Kennzahl | German Name | English Translation | What Goes In |
|----------|-------------|---------------------|--------------|
| Kz 065 | Steuerschuld fuer innergemeinschaftliche Erwerbe | Tax on IC acquisitions | Calculated USt on IC acquisitions (Kz 070 x 20%, Kz 073 x 10%, Kz 008 x 13%). Self-assessed. |
| Kz 066 | Steuerschuld gemaess §19(1) zweiter Satz, §19(1a), (1b), (1c), (1d), (1e) | Tax on reverse charge supplies received | Calculated USt on reverse charge supplies received (services from abroad, Bauleistungen, scrap etc.). Self-assessed at applicable Austrian rate. UStG 1994 §19. |
| Kz 082 | Steuerschuld auf Anzahlungen (vorangemeldeter Zeitraum) | Tax on advance payments (prior period) | USt on advance payments received in the current period for which tax point arises. |
| Kz 089 | Davon abziehen: USt auf stornierte Anzahlungen | Deduct: USt on cancelled advance payments | Reduction for advance payments reversed/cancelled. |
| Kz 095 | Gesamtbetrag der Umsatzsteuerschuld | Total output tax liability | Sum of all output USt: (Kz 000 x 20%) + (Kz 001 x 10%) + (Kz 006 x 13%) + (Kz 007 x 19%) + Kz 065 + Kz 066 + Kz 009 + Kz 082 - Kz 089. This is the total tax before input deduction. |

#### Section IV -- Vorsteuer (Input Tax)

| Kennzahl | German Name | English Translation | What Goes In |
|----------|-------------|---------------------|--------------|
| Kz 060 | Gesamtbetrag der Vorsteuer | Total deductible input tax | Sum of all deductible Vorsteuer from domestic purchases. Includes USt on purchases at 20%, 10%, 13%. Excludes blocked categories. UStG 1994 §12(1). |
| Kz 061 | Vorsteuer aus innergemeinschaftlichen Erwerben | Input tax from IC acquisitions | Deductible input USt from IC acquisitions (equals Kz 065 for fully taxable businesses). Mirror of self-assessed output. UStG 1994 §12(1)(2). |
| Kz 083 | Vorsteuer aus §19 Reverse Charge | Input tax from §19 reverse charge | Deductible input USt from reverse charge supplies received (equals Kz 066 for fully taxable businesses). UStG 1994 §12(1)(3). |
| Kz 067 | Berichtigung Vorsteuer (§12(10)-(12)) | Input tax correction (change of use) | Adjustment of input tax for change of use of capital goods. Positive = additional recovery; negative = payback. UStG 1994 §12(10)-(12). |
| Kz 064 | Vorsteuer aus EUSt (Einfuhrumsatzsteuer) | Input tax from import VAT | Deductible import USt paid at customs for goods imported from non-EU countries. UStG 1994 §12(1)(2). |
| Kz 062 | Vorsteuer betreffend Reisekosten | Input tax on travel costs | Deductible Vorsteuer on business travel expenses (domestic only -- foreign travel USt is not recoverable on Austrian UVA). |
| Kz 063 | Sonstige Berichtigungen | Other corrections | Any other Vorsteuer corrections not covered above. |

#### Section V -- Zahllast / Gutschrift (Tax Payable / Credit)

| Kennzahl | German Name | English Translation | What Goes In |
|----------|-------------|---------------------|--------------|
| Kz 095 | Gesamtbetrag der Umsatzsteuerschuld | Total output tax | As calculated above. |
| | Minus: Total Vorsteuer | Minus: Total input tax | Kz 060 + Kz 061 + Kz 083 + Kz 064 + Kz 062 + Kz 063 + Kz 067. |
| Kz 056 | Zahllast (positiv) / Gutschrift (negativ) | Tax payable (positive) / Credit (negative) | Kz 095 minus total Vorsteuer. Positive = pay to Finanzamt. Negative = credit to tax account. |

### 1B. Derived Calculations for UVA [T1]

```
OUTPUT TAX CALCULATION:
  Tax on Kz 000 = Kz 000 * 0.20
  Tax on Kz 001 = Kz 001 * 0.10
  Tax on Kz 006 = Kz 006 * 0.13
  Tax on Kz 007 = Kz 007 * 0.19
  Kz 065       = (Kz 070 * 0.20) + (Kz 073 * 0.10) + (Kz 008 * 0.13)
  Kz 066       = Self-assessed tax on §19 reverse charge base amounts

  Kz 095 = Tax on Kz 000
         + Tax on Kz 001
         + Tax on Kz 006
         + Tax on Kz 007
         + Kz 065
         + Kz 066
         + Kz 009
         + Kz 082
         - Kz 089

INPUT TAX CALCULATION:
  Total Vorsteuer = Kz 060 + Kz 061 + Kz 083 + Kz 064 + Kz 062 + Kz 063 + Kz 067

RESULT:
  Kz 056 = Kz 095 - Total Vorsteuer
  IF Kz 056 > 0 THEN Zahllast (tax payable)
  IF Kz 056 < 0 THEN Gutschrift (credit -- refunded or carried forward)
```

### 1C. Umsatzsteuererklaerung (Annual Declaration) -- Form U1 [T1]

**Legislation:** §21(4) UStG 1994.

The annual Umsatzsteuererklaerung (form U1) is a comprehensive annual reconciliation filed via FinanzOnline. It contains all data from the monthly/quarterly UVAs plus additional annual adjustments:

| Section | Content |
|---------|---------|
| Annual turnover by rate | Total Kz 000, 001, 006, 007 for full year |
| IC supplies | Total Kz 017 for full year |
| Exports | Total Kz 011 for full year |
| Exempt supplies | Total Kz 020 for full year |
| IC acquisitions | Total Kz 070, 071, 073, 008 for full year |
| Reverse charge received | Total §19 amounts for full year |
| Annual output USt | Full year Kz 095 |
| Annual Vorsteuer | Full year total input tax |
| Vorsteuer correction §12(10)-(12) | Annual adjustment for capital goods change of use |
| Pro-rata adjustment §12(4)-(6) | Annual true-up of partial exemption ratio |
| Prepaid UVA amounts | Sum of all Zahllast amounts already paid via UVAs |
| Annual balance | Net payable or refundable after deducting prepaid UVAs |

The U1 is an annual true-up. It corrects any provisional positions taken in the UVAs.

### 1D. Zusammenfassende Meldung (ZM) / Recapitulative Statement [T1]

**Legislation:** Art 21 BMR.

| Field | Detail |
|-------|--------|
| Frequency | Monthly (if IC supplies > EUR 50,000 in any quarter) or quarterly |
| Deadline | End of month following reporting period |
| Content | UID-Nummer of each EU customer, total IC supplies and IC services per customer |
| Filing | Via FinanzOnline |
| Purpose | EU cross-check system (VIES) to verify IC supply/acquisition matching |

---

## Section 2: Transaction Classification Matrix [T1]

**Legislation:** §1 UStG 1994 (taxable transactions); §3 (supplies of goods); §3a (supply of services); §6 (exemptions); §19 (reverse charge).

### 2A. Sales Classification Lookup

| Transaction Type | Counterparty Location | B2B or B2C | VAT Rate | Kennzahl | Notes |
|-----------------|----------------------|------------|----------|----------|-------|
| Domestic sale, standard goods | Austria | Any | 20% | Kz 000 | UStG 1994 §10(1) |
| Domestic sale, basic food | Austria | Any | 10% | Kz 001 | UStG 1994 §10(2) Anlage 1 |
| Domestic sale, books/newspapers | Austria | Any | 10% | Kz 001 | UStG 1994 §10(2) Z 1 |
| Domestic sale, passenger transport | Austria | Any | 10% | Kz 001 | UStG 1994 §10(2) Z 6 |
| Domestic sale, pharmaceutical | Austria | Any | 10% | Kz 001 | UStG 1994 §10(2) Z 4 |
| Domestic sale, water supply | Austria | Any | 10% | Kz 001 | UStG 1994 §10(2) Z 2 |
| Domestic sale, accommodation | Austria | Any | 10% | Kz 001 | UStG 1994 §10(2) Z 3(a) |
| Domestic sale, restaurant/catering | Austria | Any | 10% | Kz 001 | UStG 1994 §10(2) Z 4a (excl. drinks) |
| Domestic sale, wine by farmer (Ab-Hof) | Austria | Any | 13% | Kz 006 | UStG 1994 §10(3) Z 1 |
| Domestic sale, live animals | Austria | Any | 13% | Kz 006 | UStG 1994 §10(3) Z 1 |
| Domestic sale, plants/seeds | Austria | Any | 13% | Kz 006 | UStG 1994 §10(3) Z 1 |
| Domestic sale, firewood | Austria | Any | 13% | Kz 006 | UStG 1994 §10(3) Z 2 |
| Domestic sale, cultural event admission | Austria | Any | 13% | Kz 006 | UStG 1994 §10(3) Z 5 |
| Domestic sale, museum/zoo admission | Austria | Any | 13% | Kz 006 | UStG 1994 §10(3) Z 7 |
| Domestic sale, domestic air travel | Austria | Any | 13% | Kz 006 | UStG 1994 §10(3) Z 6 |
| Domestic sale, swimming pool admission | Austria | Any | 13% | Kz 006 | UStG 1994 §10(3) Z 8 |
| Domestic sale, athletic events | Austria | Any | 13% | Kz 006 | UStG 1994 §10(3) Z 5 |
| Domestic sale, Jungholz/Mittelberg | AT (exclave) | Any | 19% | Kz 007 | UStG 1994 §10(4) |
| IC supply of goods | EU | B2B | 0% | Kz 017 | Art 7 BMR; must verify UID; file ZM |
| B2B service to EU | EU | B2B | 0% | Kz 021 | Art 6(1) BMR; reverse charge at recipient |
| Export of goods | Non-EU | Any | 0% | Kz 011 | UStG 1994 §6(1)(1); customs proof needed |
| Exempt supply (financial) | Austria | Any | Exempt | Kz 020 | UStG 1994 §6(1)(8) |
| Exempt supply (insurance) | Austria | Any | Exempt | Kz 020 | UStG 1994 §6(1)(9) |
| Exempt supply (medical) | Austria | Any | Exempt | Kz 020 | UStG 1994 §6(1)(19) |
| Exempt supply (education) | Austria | Any | Exempt | Kz 020 | UStG 1994 §6(1)(11) |
| Exempt supply (real estate letting) | Austria | Any | Exempt | Kz 020 | UStG 1994 §6(1)(16) |
| Kleinunternehmer supply | Austria | Any | Exempt | Kz 016 | UStG 1994 §6(1)(27) |

### 2B. Purchases Classification Lookup

| Transaction Type | Supplier Location | Category | Kennzahl (Base) | Kennzahl (Input Tax) | Notes |
|-----------------|-------------------|----------|-----------------|---------------------|-------|
| Domestic purchase, standard | Austria | Overhead | -- | Kz 060 | USt shown on invoice at 20%. UStG 1994 §12(1). |
| Domestic purchase, 10% goods | Austria | Overhead | -- | Kz 060 | USt shown on invoice at 10%. |
| Domestic purchase, 13% goods | Austria | Overhead | -- | Kz 060 | USt shown on invoice at 13%. |
| Domestic purchase, capital asset | Austria | Capital | -- | Kz 060 | As overhead but tracked for §12(10)-(12) adjustment. |
| IC acquisition of goods | EU | Any | Kz 070 | Kz 061 | Self-assess Kz 065 (output) and Kz 061 (input). Art 1 BMR. |
| IC acquisition at 10% | EU | Any | Kz 073 | Kz 061 | Self-assess at 10%. |
| IC acquisition at 13% | EU | Any | Kz 008 | Kz 061 | Self-assess at 13%. |
| IC acquisition of new vehicle | EU | Capital | Kz 071 | Kz 061 | Special reporting. |
| Service from EU B2B | EU | Overhead | Kz 057 (base) | Kz 083 | Self-assess Kz 066 (output) and Kz 083 (input). §19(1) UStG 1994. |
| Service from non-EU | Non-EU | Overhead | Kz 057 (base) | Kz 083 | Self-assess Kz 066 (output) and Kz 083 (input). §19(1) UStG 1994. |
| Import of goods (non-EU) | Non-EU | Any | Customs entry | Kz 064 | EUSt paid at border. Recover via Kz 064. |
| Construction subcontractor (Bau) | Austria | Overhead | Kz 057 | Kz 083 | Domestic reverse charge. §19(1a) UStG 1994. |
| Scrap/waste purchase | Austria | Any | Kz 057 | Kz 083 | Domestic reverse charge. §19(1d) UStG 1994. |
| Blocked: entertainment (PKW, Bewirtung) | Any | -- | -- | EUR 0 | No Vorsteuer. §12(2)(2) UStG 1994. |

### 2C. Out-of-Scope Items (NOT on VAT Return) [T1]

| Category | Reason |
|----------|--------|
| Salaries and wages (Loehne/Gehaelter) | Not a supply of goods or services. §1 UStG 1994. |
| Social contributions (SV-Beitraege) | Statutory levy, not a taxable transaction. |
| Income tax payments (ESt/KoeSt) | Tax on income, not on supply. |
| Loan principal repayments | Financial transaction, not supply. |
| Dividends received | Not consideration for a supply. |
| Bank charges and interest | Exempt under §6(1)(8) UStG 1994 -- no input recovery for recipient. |
| Insurance premiums | Exempt under §6(1)(9) UStG 1994 (Versicherungssteuer applies separately). |

---

## Section 3: VAT Rates [T1]

**Legislation:** §10 UStG 1994.

### 3A. Rate Table

| Rate | Name (German) | Name (English) | Legal Basis | Applicable To |
|------|---------------|----------------|-------------|---------------|
| 20% | Normalsteuersatz | Standard rate | §10(1) UStG 1994 | All taxable supplies not qualifying for reduced rate. Default rate. |
| 13% | Ermaessigter Steuersatz (Zwischensteuersatz) | Intermediate reduced rate | §10(3) UStG 1994 | Live animals (not for food prep); plants, seeds, bulbs; firewood and wood chips; cultural event admissions (theatre, concerts, cinema); museum, zoo, botanical garden admissions; domestic air transport; swimming pool admissions; wine sold directly by agricultural producers (Ab-Hof-Verkauf); athletic event admissions; works of art (first supply by artist or importer). |
| 10% | Ermaessigter Steuersatz | Reduced rate | §10(2) UStG 1994 | Basic foodstuffs (Anlage 1 to UStG); books and e-books; newspapers and periodicals; passenger transport (rail, bus, taxi -- not air); water supply; pharmaceutical products; medical devices; accommodation/hotel (Beherbergung); restaurant and catering services (food only, excl. beverages); rental of immovable property where option to tax exercised; waste collection. |
| 19% | Sondersteuersatz Jungholz/Mittelberg | Special rate (exclaves) | §10(4) UStG 1994 | Supplies in the Austrian exclave municipalities of Jungholz (Tirol) and Mittelberg (Vorarlberg) that border Germany. Applies instead of 20% standard rate. Extremely rare. |
| 0% | Steuerbefreiung mit Vorsteuerabzug | Zero-rated (exempt with credit) | §6(1)(1)-(5) UStG 1994 | Export deliveries; IC supplies of goods; IC transport services; certain international transport. Input tax IS deductible. |
| 4.9% | Ermaessigter Steuersatz fuer Grundnahrungsmittel | Super-reduced rate for essential food | §10(1a) UStG 1994 (new, effective 1 July 2026) | Essential foodstuffs as listed in Annex 3 (Anlage 3) to UStG 1994: milk, eggs, bread products, vegetables, and other staple items matching specified Combined Nomenclature (CN) codes. Only products explicitly listed qualify. |
| 0% | Steuerbefreiung fuer Menstruationsprodukte und Verhuetungsmittel | Zero-rated (menstrual products / contraceptives) | §10(5) UStG 1994 (new, effective 2026) | Menstrual products (sanitary pads, tampons, menstrual cups) and contraceptives. EU-aligned zero-rating. |
| Exempt | Steuerbefreiung ohne Vorsteuerabzug | Exempt without credit | §6(1)(6)-(27) UStG 1994 | Financial services §6(1)(8); insurance §6(1)(9); medical §6(1)(19); education §6(1)(11); real estate letting §6(1)(16); Kleinunternehmer §6(1)(27). Input tax is NOT deductible. |

### 3B. Rate Determination Logic [T1]

```
IF supply is in Jungholz or Mittelberg THEN rate = 19%
ELSE IF supply is listed in §10(2) UStG 1994 (Anlage 1) THEN rate = 10%
ELSE IF supply is listed in §10(3) UStG 1994 THEN rate = 13%
ELSE IF supply is export or IC supply THEN rate = 0% (with input credit)
ELSE IF supply is exempt under §6(1)(6)-(27) THEN rate = exempt (no input credit)
ELSE rate = 20% (standard)
```

### 3C. Common Ambiguities [T2]

| Item | Correct Rate | Common Mistake | Note |
|------|-------------|----------------|------|
| Restaurant meal (food) | 10% | 20% | Food component at 10%, but beverages at 20%. Must split. §10(2) Z 4a UStG 1994. |
| Take-away food | 10% | 20% | Reduced rate applies to food regardless of consumption location. §10(2) UStG 1994. |
| Hotel breakfast included in room | 10% | Split 10%/20% | If breakfast is included in room rate, entire amount at 10%. Separate breakfast charge: food 10%, drinks 20%. |
| Wine sold by farmer at vineyard | 13% | 20% | Ab-Hof-Verkauf by agricultural producer. §10(3) Z 1 UStG 1994. |
| Wine sold by retailer/restaurant | 20% | 13% | 13% ONLY for producer's own direct sales. Retail/hospitality = 20%. |
| Domestic flight | 13% | 10% | Air transport within Austria = 13%. Rail/bus = 10%. §10(3) Z 6 UStG 1994. |
| Cinema ticket | 13% | 10% | Film screenings are cultural events at 13%. §10(3) Z 5 UStG 1994. |

---

## Section 4: Blocked Input Tax (Vorsteuerabzug Restrictions) [T1]

**Legislation:** §12(2) UStG 1994; §20 EStG 1988 (by reference).

### 4A. Fully Blocked Categories

| Category | German Term | Rule | Legal Basis | Deductible? |
|----------|-------------|------|-------------|-------------|
| Entertainment / hospitality | Repraesentation / Bewirtung | NOT deductible unless advertising character predominates (> 50% Werbecharakter). Business meals with clients: generally BLOCKED. | §12(2)(2)(a) UStG 1994; §20(1)(3) EStG 1988 | NO (default) |
| Passenger vehicles (PKW) purchase/lease | PKW-Anschaffung/-Leasing | Vorsteuer on purchase, lease, or hire of passenger vehicles (PKW) is fully BLOCKED. This is an Austrian-specific rule stricter than most EU states. | §12(2)(2)(b) UStG 1994 | NO |
| PKW operating costs | PKW-Betriebskosten | Vorsteuer on repairs, maintenance, insurance, parking of PKW is BLOCKED (follows the vehicle block). | §12(2)(2)(b) UStG 1994 | NO |
| PKW fuel | PKW-Treibstoff | Vorsteuer on fuel for PKW is BLOCKED (follows the vehicle block). | §12(2)(2)(b) UStG 1994 | NO |
| Luxury / personal items | Luxusaufwand | Items with predominantly personal character are not deductible. | §12(2)(2)(a) UStG 1994; §20(1)(1) EStG 1988 | NO |
| Exempt supply-related inputs | Vorsteuer bei steuerfreien Umsaetzen | If purchases relate exclusively to exempt outputs (§6(1)(6)-(27)), input tax is not deductible. | §12(3) UStG 1994 | NO |

### 4B. Motor Vehicle Rules -- Detailed [T1]

**Legislation:** §12(2)(2)(b) UStG 1994; Sachbezugswerteverordnung; BMF guidelines.

| Vehicle Classification | German Term | Vorsteuer Deductible? | Conditions |
|-----------------------|-------------|----------------------|------------|
| Passenger car (PKW) | Personenkraftwagen | NO | Fully blocked. No exceptions for business use percentage. §12(2)(2)(b) UStG 1994. |
| Station wagon / Kombi (under 3.5t, PKW-classified) | Kombi (PKW-aehnlich) | NO | If classified as PKW by type approval (Typengenehmigung), blocked. |
| SUV (PKW-classified) | SUV (PKW-Zulassung) | NO | Standard SUVs are PKW. Blocked. |
| Fiskal-LKW | Fiskal-LKW | YES | Vehicles that meet specific criteria to be classified as LKW for tax purposes despite appearing similar to PKW. See EC1 below. §12(2)(2)(b) UStG 1994 exception. |
| Van / LKW (> 3.5t or goods transport) | Lastkraftwagen | YES | Genuine commercial vehicles used for goods transport. Full Vorsteuer recovery. |
| Minibus (> 8+1 seats) | Kleinbus | YES | Buses with more than 8 passenger seats + driver. Full recovery. |
| Zero-emission vehicle (electric/hydrogen) | Emissionsfreies Fahrzeug | YES (capped) | Vorsteuer deductible up to EUR 40,000 gross Anschaffungskosten. Between EUR 40,000-EUR 80,000: proportional reduction. Above EUR 80,000: limited to the EUR 40,000 base equivalent. §12(2)(2)(b) UStG 1994 exception; BMF e-mobility guidelines. |
| Taxi | Taxi | YES | Exception: vehicles used predominantly (> 80%) for taxi services. §12(2)(2)(b) UStG 1994. |
| Driving instruction vehicle | Fahrschulfahrzeug | YES | Exception: vehicles used for driving instruction. §12(2)(2)(b) UStG 1994. |
| Rental stock (car rental business) | Mietwagen (Verleihunternehmen) | YES | Exception: vehicles held as rental inventory by car rental companies. §12(2)(2)(b) UStG 1994. |

### 4C. Zero-Emission Vehicle Graduated Recovery [T1]

**Legislation:** §12(2)(2)(b) UStG 1994; BMF-Erlass zur Vorsteuer bei E-Fahrzeugen.

| Gross Purchase Price (incl. USt) | Vorsteuer Recovery |
|---------------------------------|-------------------|
| Up to EUR 40,000 | 100% of Vorsteuer deductible |
| EUR 40,001 -- EUR 80,000 | Proportional reduction: recovery = (EUR 80,000 - purchase price) / (EUR 80,000 - EUR 40,000) * full Vorsteuer [T2] |
| Above EUR 80,000 | No Vorsteuer deductible (luxury exclusion) |

### 4D. Entertainment (Bewirtung) -- Detailed Rules [T1]

**Legislation:** §12(2)(2)(a) UStG 1994; §20(1)(3) EStG 1988.

| Situation | Vorsteuer Deductible? | Reasoning |
|-----------|----------------------|-----------|
| Client entertainment (dinner, drinks) | NO | Repraesentation. §20(1)(3) EStG. |
| Staff Christmas party (Weihnachtsfeier) | YES (within limits) | Employee benefit, not Repraesentation. Limit EUR 365/employee/year. |
| Event sponsorship with prominent branding | YES (if Werbung > 50%) | Advertising character predominates. §12(2)(2)(a) UStG 1994 exception. [T2] flag for reviewer. |
| Business lunch with no advertising purpose | NO | Pure Bewirtung. Blocked. |
| Product launch with invited media | YES | Advertising/PR event. Werbecharakter predominates. [T2] confirm scope. |

**Key difference vs Germany:** Austria's entertainment blocking is similar in principle to Germany's (§4(5) Nr. 2 EStG DE), but Austria's is an absolute block at the Vorsteuer level via §12(2)(2)(a) UStG 1994 referencing §20(1)(3) EStG. Germany allows 70% income tax deduction for business entertainment but blocks 100% of Vorsteuer. Austria blocks both. The Austrian rule is therefore stricter on income tax deduction but equivalent on Vorsteuer.

### 4E. Pro-Rata Recovery (Partial Exemption) [T2]

**Legislation:** §12(4)-(6) UStG 1994.

If a business makes both taxable and exempt supplies:

```
Recovery % = (Taxable Turnover incl. zero-rated / Total Turnover) * 100
```

Methods:
1. **Gesamtumsatzverfahren** (global turnover method) -- default. §12(4) UStG 1994.
2. **Einzelzuordnung** (direct allocation) -- permitted where costs can be directly attributed to taxable or exempt supplies. §12(5) UStG 1994.

**Flag for reviewer: confirm method and pro-rata percentage. Annual adjustment required in U1.**

---

## Section 5: Registration [T1]

### 5A. Kleinunternehmerregelung (Small Business Exemption)

**Legislation:** §6(1)(27) UStG 1994.

| Parameter | Detail |
|-----------|--------|
| Threshold | Annual gross turnover <= EUR 55,000 (since 1 January 2025; previously EUR 35,000 net. Changed by Progressionsentlastungsgesetz 2025.) |
| One-time tolerance | Up to 10% above threshold (EUR 60,500) in a single year. If exceeded during the year, USt applies from the supply causing the breach; if not exceeded, Kleinunternehmer status retained. |
| UID-Nummer required? | Not required for purely domestic Kleinunternehmer. Required if making/receiving intra-EU supplies/services (must register for UID). |
| Invoice requirements | Must state: "Umsatzsteuerbefreit -- Kleinunternehmer gemaess §6(1)(27) UStG" |
| USt charged? | NO -- Kleinunternehmer does not charge USt on invoices |
| Vorsteuer recovery? | NO -- no input tax deduction |
| UVA filing required? | NO (but must file annual U1 if UID-Nummer held) |
| Opt-in to standard regime | Yes -- by written declaration to Finanzamt. Binding for 5 calendar years minimum (Bindungsfrist). §6(3) UStG 1994. |
| Reverse charge applies? | YES -- §19 overrides Kleinunternehmerregelung. Kleinunternehmer must self-assess and PAY USt on reverse charge supplies received. No Vorsteuer deduction. |
| EU SME scheme (from 2025) | EU-wide Kleinunternehmer status possible in other Member States via FinanzOnline portal, subject to EU-wide EUR 100,000 gross turnover cap plus the domestic threshold of the destination state. Directive 2020/285 implemented from 1 January 2025. [T2] |

### 5B. UID-Nummer Format and Registration

| Field | Detail |
|-------|--------|
| Format | ATU + 8 digits (e.g., ATU12345678) |
| Issuing authority | Finanzamt Oesterreich |
| Registration method | FinanzOnline (https://finanzonline.bmf.gv.at) or paper form (Verf 15) |
| Processing time | Typically 2-4 weeks |
| Verification | VIES system (https://ec.europa.eu/taxation_customs/vies/) |
| When required | When making taxable supplies in Austria; when making/receiving IC supplies; when receiving services from EU businesses (even if Kleinunternehmer). |

### 5C. FinanzOnline Portal

| Function | Detail |
|----------|--------|
| UVA filing | Form U30, monthly or quarterly |
| Annual declaration | Form U1 |
| ZM filing | Zusammenfassende Meldung |
| Tax account | Abgabenkonto -- view balance, payments, credits |
| Authentication | Buergerkarte, Handy-Signatur, or FinanzOnline-Kennung (username/password + TAN) |
| Steuerberater access | Via Vollmacht (power of attorney) registered at Finanzamt |

---

## Section 6: Filing Deadlines [T1]

**Legislation:** §21 UStG 1994; BAO (Bundesabgabenordnung).

### 6A. Regular Filing Deadlines

| Return | Period | Deadline | Method |
|--------|--------|----------|--------|
| Monthly UVA (U30) | Monthly (if prior year turnover > EUR 100,000) | 15th of the 2nd month following the reporting month. E.g., January UVA due 15 March. | FinanzOnline (electronic mandatory). §21(1) UStG 1994. |
| Quarterly UVA (U30) | Quarterly (if prior year turnover <= EUR 100,000) | 15th of the 2nd month following the quarter end. E.g., Q1 (Jan-Mar) UVA due 15 May. | FinanzOnline (electronic mandatory). §21(1) UStG 1994. |
| Annual Umsatzsteuererklaerung (U1) | Calendar year | 30 April of following year (paper) or 30 June of following year (electronic via FinanzOnline). | §134 BAO. |
| Annual U1 with Steuerberater | Calendar year | Extended deadline under Quotenregelung -- typically 30 April of second following year (with Steuerberater quota system). | §134 BAO; BMF Erlass. |
| Zusammenfassende Meldung (ZM) | Monthly or quarterly | End of the month following the reporting period. | Art 21 BMR; FinanzOnline. |
| Exempt from UVA | If annual USt liability < EUR 1,000 | No UVA required, only annual U1. | §21(2) UStG 1994. |

### 6B. Penalties for Late Filing and Payment

| Penalty Type | German Term | Amount / Rate | Legal Basis |
|-------------|-------------|---------------|-------------|
| Late payment surcharge | Saeumniszuschlag | 2% of unpaid tax amount, charged once (on initial default). Additional 1% after 3 months, another 1% after 6 months (total max 4%). | §217 BAO. |
| Late filing penalty | Verspaetungszuschlag | Up to 10% of the assessed tax amount. Discretionary by Finanzamt. | §135 BAO. |
| Estimated assessment | Schaetzung | If no return filed, Finanzamt estimates the tax liability. Often unfavourable. | §184 BAO. |
| Interest on arrears | Anspruchszinsen | 2% above base rate (Basiszinssatz) on income tax / corporate tax differences. Not directly on USt but applies to annual assessment differences. | §205 BAO. |
| Finanzordnungswidrigkeit | Finanzordnungswidrigkeit | Negligent non-filing: fine up to EUR 5,000. | §51 FinStrG. |
| Abgabenhinterziehung | Tax evasion | Intentional evasion: fine up to 200% of evaded tax or imprisonment. | §33 FinStrG. |

### 6C. Example Deadline Calendar (Year 2026)

| Period | Type | Deadline |
|--------|------|----------|
| January 2026 UVA | Monthly | 15 March 2026 |
| February 2026 UVA | Monthly | 15 April 2026 |
| March 2026 UVA | Monthly | 15 May 2026 |
| Q1 2026 UVA | Quarterly | 15 May 2026 |
| April 2026 UVA | Monthly | 15 June 2026 |
| May 2026 UVA | Monthly | 15 July 2026 |
| June 2026 UVA | Monthly | 15 August 2026 |
| Q2 2026 UVA | Quarterly | 15 August 2026 |
| Annual U1 for 2025 (paper) | Annual | 30 April 2026 |
| Annual U1 for 2025 (electronic) | Annual | 30 June 2026 |

---

## Section 7: Reverse Charge (§19 UStG 1994) [T1]

**Legislation:** §19 UStG 1994.

### 7A. Reverse Charge Categories

| Category | Legal Basis | Supplier | Recipient | Kennzahl (Output) | Kennzahl (Input) | Notes |
|----------|-------------|----------|-----------|--------------------|-------------------|-------|
| Services from foreign businesses (B2B) | §19(1) 2. Satz UStG 1994 | EU or non-EU, not established in AT | AT-registered business | Kz 066 | Kz 083 | Base amount in Kz 057. Standard B2B reverse charge. |
| Intra-Community acquisition of goods | Art 1 BMR | EU supplier | AT-registered business | Kz 065 | Kz 061 | Base in Kz 070/073/008. Self-assess at Austrian rate. |
| Construction services (Bauleistungen) | §19(1a) UStG 1994 | AT or foreign subcontractor | AT-registered main contractor providing Bauleistungen | Kz 066 | Kz 083 | Domestic reverse charge. Applies when BOTH parties are in construction sector. Base in Kz 057. |
| Scrap metal and waste | §19(1d) UStG 1994 | Any supplier | AT-registered business | Kz 066 | Kz 083 | Applies to supplies of scrap, waste, and used materials listed in Anlage to §19(1d). Base in Kz 057. |
| Security staff provision (Personalgestellung) | §19(1b) UStG 1994 | Foreign provider | AT-registered business | Kz 066 | Kz 083 | Staff leasing from non-established business. Base in Kz 057. |
| Gas and electricity from foreign suppliers | §19(1) UStG 1994 | EU/non-EU utility | AT-registered business (dealer or large consumer) | Kz 066 | Kz 083 | Supply of gas/electricity where supplier is not established in AT. Base in Kz 057. |
| Transfers of emission allowances | §19(1e) UStG 1994 | Any | AT-registered business | Kz 066 | Kz 083 | CO2 emission certificates (EU ETS). Base in Kz 057. |
| Mobile phones and integrated circuits (threshold) | §19(1d) UStG 1994 | Any | AT-registered business | Kz 066 | Kz 083 | If single invoice amount > EUR 5,000 net. Base in Kz 057. |

### 7B. Reverse Charge Mechanics [T1]

```
Step 1: Identify net amount from supplier invoice (no Austrian USt shown).
Step 2: Determine applicable Austrian VAT rate (usually 20%).
Step 3: Report:
  - Base amount in appropriate acquisition Kz (Kz 070 for IC goods, Kz 057 for services/domestic RC).
  - Self-assess OUTPUT USt in Kz 065 (IC) or Kz 066 (§19).
  - Claim INPUT Vorsteuer in Kz 061 (IC) or Kz 083 (§19).
Step 4: Net effect = zero for fully taxable businesses.
Step 5: For Kleinunternehmer: OUTPUT tax MUST be paid. INPUT tax CANNOT be claimed.
         Net effect = tax cost equal to the USt amount.
```

### 7C. Reverse Charge Exceptions [T1]

| Situation | Reverse Charge? | Reason |
|-----------|----------------|--------|
| Out-of-scope items (salaries, dividends, loan repayments) | NO | Not a supply. §1 UStG 1994. |
| Local consumption abroad (hotel, restaurant, taxi in another country) | NO | VAT paid at source in the other country. Not recoverable on Austrian UVA. |
| EU supplier charged their local VAT on invoice | NO | Supplier already accounted for VAT. Austrian recipient cannot reverse charge. May seek refund via EU VAT Refund Directive (Directive 2008/9/EC). |
| B2C services from EU (not B2B) | Depends | Place of supply rules under §3a UStG 1994 determine. Most B2C services: place of supply = supplier's country. [T2] |
| Kleinunternehmer receiving services from abroad | YES | §19 overrides §6(1)(27). Must register for UID and self-assess. |

---

## Section 8: Edge Cases [T1/T2/T3]

### EC1 -- Fiskal-LKW (Tax Truck Classification for SUVs/Large Vehicles) [T1]

**Situation:** Client purchases a large SUV or pickup truck and wants to claim Vorsteuer, arguing it is a Fiskal-LKW rather than a PKW.
**Resolution:** A Fiskal-LKW is a vehicle that, despite resembling a passenger car, qualifies as an LKW for tax purposes based on the BMF Fiskal-LKW list (published annually). Criteria include: vehicle weight, load area size, number of seats, and ratio of load area to total area. The BMF maintains a definitive list of makes/models classified as Fiskal-LKW. If the vehicle is ON the Fiskal-LKW list: full Vorsteuer deductible. If NOT on the list: treated as PKW and Vorsteuer is BLOCKED. [T2] flag to verify specific vehicle against current BMF Fiskal-LKW list.
**Legislation:** §12(2)(2)(b) UStG 1994; BMF Fiskal-LKW Erlass (updated periodically).
**Key distinction:** This has NO equivalent in Malta -- Malta simply blocks all motor vehicles under 10th Schedule Item 3(1)(a)(iv-v) with no Fiskal-LKW carve-out.

### EC2 -- Differenzbesteuerung (Margin Scheme) [T2]

**Situation:** Client is a second-hand goods dealer (Gebrauchtwarenhaendler) selling used cars, antiques, art, or collector's items.
**Resolution:** Under Differenzbesteuerung (§24a UStG 1994), USt is charged only on the profit margin (Verkaufspreis minus Einkaufspreis), not on the full selling price. The USt is included in the selling price (hidden tax). Invoices must NOT show USt separately. The margin is treated as gross (inclusive of USt). Kz 000 reports only the net margin equivalent. No Vorsteuer recovery on the purchase of the goods. Must note on invoice: "Differenzbesteuerung -- Gebrauchtgegenstaende gemaess §24a UStG."
**Legislation:** §24a UStG 1994.
**Example:** Buy used car for EUR 10,000 (no Vorsteuer). Sell for EUR 12,500. Margin = EUR 2,500 gross. USt = EUR 2,500 / 1.20 * 0.20 = EUR 416.67. Net margin in Kz 000 = EUR 2,083.33.

### EC3 -- Kleinunternehmer Threshold Breach [T1]

**Situation:** Kleinunternehmer's gross turnover exceeds EUR 55,000 during the year.
**Resolution:**
- If gross turnover exceeds EUR 55,000 but stays within the 10% tolerance (EUR 60,500): Kleinunternehmer status is retained for the current year. Invoices for the remainder of the year may still be issued without USt. From the following year, if the tolerance was used, standard taxation applies unless turnover drops below EUR 55,000.
- If gross turnover exceeds EUR 60,500 during the year: USt must be charged from the supply that causes the breach (not retroactively from year start -- this is a change from the pre-2025 rules which applied retroactively). Must file UVAs and charge USt from that point forward.
- Notification to Finanzamt required.
**Legislation:** §6(1)(27) UStG 1994 as amended by Progressionsentlastungsgesetz 2025.

### EC4 -- Tourism and 13% Rate Specifics [T2]

**Situation:** Hotel operator charges for accommodation, food, drinks, spa, and parking.
**Resolution:**
- Accommodation (Beherbergung): 10% (§10(2) Z 3(a) UStG 1994).
- Breakfast included in room: 10% (ancillary to accommodation).
- Restaurant food: 10% (§10(2) Z 4a UStG 1994).
- Beverages at restaurant: 20% (standard rate -- drinks are excluded from reduced rate).
- Spa/wellness: 20% (standard rate -- not a listed reduced-rate service).
- Parking: 20% (standard rate).
- Cultural event ticket sold by hotel: 13% if the hotel is merely selling admission to an external cultural event or operating its own qualifying cultural performance.
**Key point:** Hotels must split invoices by rate. A single "all-inclusive" charge must be allocated to the correct rate components. [T2] flag for correct allocation.
**Legislation:** §10(2), §10(3) UStG 1994.

### EC5 -- Wine from Farmers (Ab-Hof-Verkauf) at 13% [T1]

**Situation:** Agricultural producer (Winzer/Bauer) sells wine directly from the farm or vineyard (Ab-Hof-Verkauf).
**Resolution:** Wine sold directly by the producing farmer is taxed at 13% (§10(3) Z 1 UStG 1994). This applies ONLY to:
- Wine from the farmer's own production.
- Sold at the farm, vineyard, or Buschenschank (farmer's tavern).
- By the agricultural producer themselves (not through a retailer or restaurant).
If the same wine is sold through a retailer, supermarket, or restaurant, the standard rate of 20% applies. The 13% is a producer-direct-sale privilege.
**Legislation:** §10(3) Z 1 UStG 1994.
**Note:** If the farmer operates under the agricultural flat-rate scheme (§24 UStG 1994 Pauschalierung), the farmer charges a flat-rate USt (currently 13%) and does not file UVAs -- the flat rate is considered full settlement. [T3] for flat-rate scheme details.

### EC6 -- EU Hotel / Restaurant Abroad [T1]

**Situation:** Client pays for hotel in Germany or restaurant in Italy. Invoice shows local VAT.
**Resolution:** NOT reverse charge. Foreign VAT was charged and paid at source. No Austrian UVA entry. The foreign VAT is irrecoverable on the Austrian return. Client may seek refund via EU VAT Refund Directive (Directive 2008/9/EC) through FinanzOnline (Vorsteuerverguerungsverfahren), but this is a separate process, not part of the UVA.
**Legislation:** §3a(11) UStG 1994 (place of supply for accommodation/restaurant = where property is located / where service physically performed).

### EC7 -- SaaS Subscription from US Provider [T1]

**Situation:** US company (e.g., AWS, Microsoft Azure), EUR 500/month, no USt on invoice.
**Resolution:** Reverse charge under §19(1) UStG 1994. Self-assess:
- Kz 057 = EUR 500 (base for §19 reverse charge)
- Kz 066 = EUR 100 (output USt at 20%)
- Kz 083 = EUR 100 (input Vorsteuer at 20%)
- Net effect: zero for fully taxable business.
For Kleinunternehmer: Kz 066 = EUR 100 payable. No Kz 083 recovery. Net cost = EUR 100.

### EC8 -- Zero-Emission Vehicle Purchase [T1]

**Situation:** Client purchases Tesla Model 3 for EUR 45,000 gross (incl. USt).
**Resolution:** Zero-emission vehicle exception applies. However, gross price exceeds EUR 40,000 cap:
- Full Vorsteuer on first EUR 40,000 gross: EUR 40,000 / 1.20 * 0.20 = EUR 6,666.67.
- Proportional reduction for EUR 40,001-80,000 band: Deductible Vorsteuer = (80,000 - 45,000) / (80,000 - 40,000) * full Vorsteuer on the excess portion.
- [T2] flag for exact calculation. Use BMF Sachbezugswerte guidelines.
**Legislation:** §12(2)(2)(b) UStG 1994; BMF e-mobility Erlass.

### EC9 -- Construction Reverse Charge (Bauleistungen) [T1]

**Situation:** Austrian subcontractor performs plumbing work for an Austrian general contractor. Both are in the construction business.
**Resolution:** Reverse charge under §19(1a) UStG 1994. Subcontractor invoices WITHOUT USt, noting "Uebergang der Steuerschuld auf den Leistungsempfaenger gemaess §19(1a) UStG". General contractor self-assesses:
- Kz 057 = net invoice amount
- Kz 066 = USt at 20% (output)
- Kz 083 = USt at 20% (input)
- Net = zero for fully taxable contractor.
**Key condition:** BOTH supplier and recipient must provide Bauleistungen. If the recipient is NOT in the construction sector (e.g., a law firm commissioning renovations), §19(1a) does NOT apply -- subcontractor charges USt normally.

### EC10 -- Organschaft (VAT Group) [T3]

**Situation:** Client is part of a VAT group (Organschaft) -- a parent entity (Organtraeger) and one or more subsidiaries (Organgesellschaften) treated as a single taxable person.
**Resolution:** ESCALATE. §2(2)(2) UStG 1994. Internal supplies between Organschaft members are not taxable (Innenumsaetze). Only the Organtraeger files the UVA covering all members. Requires financial, economic, and organisational integration (finanzielle, wirtschaftliche, organisatorische Eingliederung). Complex rules -- do not attempt without Steuerberater.

### EC11 -- Credit Notes (Gutschrift / Stornorechnung) [T1]

**Situation:** Client receives a credit note from a supplier reducing a prior invoice.
**Resolution:** Reduce the original Kennzahl entries. If original purchase was at 20% and Vorsteuer was claimed in Kz 060, the credit note reduces Kz 060 by the credited Vorsteuer amount. Net figures are reported. Do not create separate negative entries in different Kennzahlen. If the credit note relates to a reverse charge transaction, reduce BOTH the output (Kz 065/066) and input (Kz 061/083) sides.
**Legislation:** §16 UStG 1994.

### EC12 -- Intra-Community Supply of Goods with Missing UID [T1]

**Situation:** Client sells goods to an EU business but the recipient's UID-Nummer is not verified or is invalid.
**Resolution:** Cannot zero-rate the supply. Treat as domestic sale at 20% (Kz 000) until valid UID is obtained and verified via VIES. Once verified, correct to Kz 017 (zero-rated IC supply). File corrected UVA if needed. Missing UID = no zero-rating.
**Legislation:** Art 7 BMR; §6(1)(1) UStG 1994.

### EC13 -- Triangulation (Dreiecksgeschaeft) [T2]

**Situation:** Austrian business (B) buys goods from German business (A) and sells to Italian business (C). Goods ship directly from Germany to Italy (A -> C). B never physically handles goods.
**Resolution:** Simplified triangulation under Art 25 BMR. B does not need to register in Italy. B reports:
- IC acquisition from A in Kz 070 (self-assess and reverse out).
- IC supply to C in Kz 017.
- ZM filing with special triangulation marker (code "T" or "D" for Dreiecksgeschaeft).
[T2] flag for reviewer -- confirm all three parties are in different EU Member States and goods move directly from first to last party.
**Legislation:** Art 25 BMR; §19(1) UStG 1994.

### EC14 -- Imports from Non-EU (Physical Goods through Customs) [T1]

**Situation:** Client imports physical goods from China. Customs charges Einfuhrumsatzsteuer (EUSt).
**Resolution:** EUSt paid at customs is recoverable as input tax via Kz 064 (not reverse charge on UVA). The customs declaration (Zollanmeldung) serves as the input tax document. The EUSt amount from the customs assessment is entered in Kz 064.
**Legislation:** §12(1)(2) UStG 1994.

### EC15 -- Real Estate Option to Tax [T2]

**Situation:** Client lets commercial property and opts to charge USt (Option zur Steuerpflicht).
**Resolution:** Rental of immovable property is generally exempt under §6(1)(16) UStG 1994. The landlord may opt to tax the rental (§6(2) UStG 1994) if the tenant uses the property for at least 95% taxable purposes. If option exercised: charge 20% USt on rent. Landlord can then recover Vorsteuer on property costs. If not exercised: exempt, no Vorsteuer recovery. [T2] -- confirm tenant's taxable use percentage.
**Legislation:** §6(1)(16), §6(2) UStG 1994.

---

## Section 9: Test Suite

### Test 1 -- Standard Domestic Purchase, 20% USt [T1]

**Input:** Austrian supplier, office supplies, gross EUR 240, USt EUR 40, net EUR 200. Regelbesteuerung client.
**Expected output:** Kz 060 includes EUR 40 (Vorsteuer deductible). No output Kennzahl entry for this purchase.

### Test 2 -- US Software Subscription, Reverse Charge [T1]

**Input:** US provider (AWS), EUR 100/month, no USt on invoice. Regelbesteuerung client.
**Expected output:**
- Kz 057 = EUR 100 (base)
- Kz 066 = EUR 20 (output USt at 20%)
- Kz 083 = EUR 20 (input Vorsteuer at 20%)
- Net VAT effect = zero.

### Test 3 -- Intra-Community Goods Acquisition [T1]

**Input:** German supplier ships goods to AT, EUR 5,000 net, no USt. Client is Regelbesteuerung.
**Expected output:**
- Kz 070 = EUR 5,000 (IC acquisition base)
- Kz 065 = EUR 1,000 (output USt at 20%)
- Kz 061 = EUR 1,000 (input Vorsteuer at 20%)
- Net VAT effect = zero.
- Report on ZM? No -- ZM is for outgoing IC supplies, not acquisitions.

### Test 4 -- IC Supply of Goods to Italy [T1]

**Input:** Client sells goods to Italian VAT-registered business, EUR 3,000 net. Goods shipped AT to IT. Italian UID verified.
**Expected output:**
- Kz 017 = EUR 3,000
- No output USt.
- File ZM with Italian customer's UID and EUR 3,000.

### Test 5 -- Kleinunternehmer Purchase (No Recovery) [T1]

**Input:** Kleinunternehmer buys office supplies EUR 600 gross (incl. EUR 100 USt at 20%).
**Expected output:** No UVA entry. No Vorsteuer recovery. Gross cost = EUR 600.

### Test 6 -- Diesel Car Purchase (Blocked) [T1]

**Input:** Client purchases diesel Audi A4, EUR 36,000 net + EUR 7,200 USt (20%). Gross EUR 43,200.
**Expected output:**
- Kz 060 does NOT include the EUR 7,200. Vorsteuer BLOCKED under §12(2)(2)(b) UStG 1994.
- Full EUR 43,200 is a non-deductible cost for Vorsteuer purposes.

### Test 7 -- Electric Vehicle Purchase (Partially Deductible) [T1]

**Input:** Client purchases electric vehicle (Tesla Model 3), gross EUR 50,000 (incl. USt). Net EUR 41,666.67, USt EUR 8,333.33.
**Expected output:**
- Zero-emission exception applies.
- Gross price EUR 50,000 is in the EUR 40,001-80,000 proportional band.
- Deductible Vorsteuer = (EUR 80,000 - EUR 50,000) / (EUR 80,000 - EUR 40,000) * EUR 8,333.33 = 75% * EUR 8,333.33 = EUR 6,250.00. [T2] flag for reviewer to verify exact calculation per BMF guidelines.
- Kz 060 includes EUR 6,250.00.

### Test 8 -- Construction Reverse Charge [T1]

**Input:** Austrian plumber (subcontractor) invoices Austrian general contractor EUR 8,000 net, no USt. Both in Bauleistungen. Note on invoice: "Uebergang der Steuerschuld §19(1a)."
**Expected output (for general contractor's UVA):**
- Kz 057 = EUR 8,000 (base)
- Kz 066 = EUR 1,600 (output USt at 20%)
- Kz 083 = EUR 1,600 (input Vorsteuer at 20%)
- Net = zero.

### Test 9 -- EU Hotel (Local Consumption, Not Reverse Charge) [T1]

**Input:** Client stays at hotel in Munich, Germany. Invoice EUR 500 including German USt (7% accommodation rate = EUR 32.71 USt).
**Expected output:** No Austrian UVA entry. German USt is irrecoverable on Austrian return. Total cost = EUR 500 gross. Client may seek refund via EU VAT Refund Directive separately.

### Test 10 -- Kleinunternehmer Receives EU Services (Reverse Charge Applies) [T1]

**Input:** Kleinunternehmer subscribes to Irish SaaS provider, EUR 50/month. No USt on invoice.
**Expected output:**
- §19 reverse charge overrides Kleinunternehmerregelung.
- Kleinunternehmer must self-assess: Kz 066 = EUR 10 (output USt at 20%). MUST PAY.
- No Vorsteuer recovery (Kz 083 = EUR 0 -- Kleinunternehmer cannot claim).
- Net cost to Kleinunternehmer = EUR 50 + EUR 10 = EUR 60.
- Must obtain UID-Nummer for cross-border transactions.

### Test 11 -- Wine Sold by Farmer at 13% [T1]

**Input:** Winzer sells 100 bottles of own wine at Buschenschank, total EUR 1,500 net.
**Expected output:**
- Kz 006 = EUR 1,500
- USt = EUR 1,500 * 13% = EUR 195
- If farmer is on Pauschalierung (§24 UStG 1994): [T3] escalate -- flat-rate scheme, no UVA filing.

### Test 12 -- Scrap Metal Purchase (Domestic Reverse Charge) [T1]

**Input:** Austrian scrap dealer sells EUR 2,000 of scrap metal to Austrian manufacturing company. Invoice without USt, noting §19(1d).
**Expected output (for manufacturing company's UVA):**
- Kz 057 = EUR 2,000 (base)
- Kz 066 = EUR 400 (output USt at 20%)
- Kz 083 = EUR 400 (input Vorsteuer at 20%)
- Net = zero.

---

## Section 10: Comparison with Malta

| Feature | Austria (AT) | Malta (MT) |
|---------|-------------|------------|
| **Primary legislation** | UStG 1994 (Umsatzsteuergesetz) | VAT Act Cap. 406 |
| **Standard rate** | 20% (§10(1) UStG 1994) | 18% |
| **Reduced rates** | 10% and 13% (§10(2)-(3) UStG 1994) | 5%, 7%, 12% |
| **Special rate** | 19% (Jungholz/Mittelberg only) | None |
| **Zero-rating** | Exports, IC supplies (§6(1)(1)-(5)) | Exports (Box 20) |
| **VAT return form** | U30 (UVA) -- Kennzahlen system | VAT3 -- Box system (Box 1-45) |
| **Annual declaration** | U1 (Umsatzsteuererklaerung) | Included in quarterly VAT3 cycle |
| **Small enterprise threshold** | EUR 55,000 gross (Kleinunternehmerregelung, §6(1)(27), from 1 Jan 2025) | EUR 35,000 domestic turnover (Article 11) |
| **Small enterprise scheme** | No USt charged, no Vorsteuer recovery. Opt-in binding for 5 years. | Article 11: simplified 4-box annual declaration. No VAT recovery. |
| **Filing frequency** | Monthly (> EUR 100,000 turnover) or quarterly (< EUR 100,000). §21(1) UStG 1994. | Quarterly (Article 10); Annual (Article 11); Monthly (Article 12). |
| **Filing portal** | FinanzOnline | CFR VAT Online |
| **Filing deadline** | 15th of 2nd month after period (§21(1) UStG 1994) | 21st of month after quarter (e-filing) or 14th (paper) |
| **Motor vehicle Vorsteuer** | Fully BLOCKED for PKW. Exception only for Fiskal-LKW, zero-emission (capped), taxis, driving schools, rental fleet. §12(2)(2)(b) UStG 1994. | Blocked under 10th Schedule Item 3(1)(a)(iv-v). Exception for taxis, delivery, car rental. |
| **Fiskal-LKW concept** | YES -- BMF maintains list of vehicles qualifying as LKW for tax despite PKW appearance. | NO equivalent. |
| **Zero-emission vehicle benefit** | Vorsteuer deductible up to EUR 40,000 gross; proportional reduction EUR 40,000-80,000. | No specific EV benefit. Standard motor vehicle block applies. |
| **Entertainment blocking** | Blocked unless > 50% advertising character. §12(2)(2)(a) UStG 1994. | Blocked under 10th Schedule Item 3(1)(b). |
| **Capital goods threshold** | No specific monetary threshold for UVA treatment, but §12(10)-(12) adjustment applies for capital goods over useful life (5 years movable, 20 years immovable). | EUR 1,160 gross. Below = overhead. Above = Capital Goods Box 30. |
| **Reverse charge (domestic)** | YES: Bauleistungen §19(1a), scrap §19(1d), staff leasing §19(1b), emission certificates §19(1e). | Limited domestic reverse charge. |
| **Reverse charge (cross-border)** | §19(1) for services from abroad; Art 1 BMR for IC acquisitions. | Article 19 (IC acquisitions); Article 20 (services from abroad). |
| **Margin scheme** | Differenzbesteuerung §24a UStG 1994. Tax on margin only. | Not commonly used; follows EU VAT Directive provisions. |
| **Agricultural flat-rate** | Pauschalierung §24 UStG 1994. Flat 13% USt, no UVA filing. | No equivalent scheme. |
| **Penalties (late payment)** | Saeumniszuschlag: 2% initial + up to 2% more. §217 BAO. | Administrative penalty; interest on overdue. |
| **Penalties (late filing)** | Verspaetungszuschlag: up to 10% of assessed tax. §135 BAO. | CFR penalties per VAT Act. |
| **Currency** | EUR | EUR |
| **VAT number format** | ATU + 8 digits (ATU12345678) | MT + 8 digits (MT12345678) |
| **Recapitulative statement** | Zusammenfassende Meldung (ZM) -- Art 21 BMR | EC Sales List / Recapitulative Statement |

### Key Differences Practitioners Must Note

1. **Austria has THREE reduced rates (10%, 13%, 19%) vs Malta's THREE (5%, 7%, 12%).** The mapping is not 1:1. Food is 10% in AT but split across 5%/7% in MT depending on type.
2. **Austria's PKW block is absolute** (no business-use exception for standard cars), whereas Malta's motor vehicle block is similarly absolute but lacks Austria's Fiskal-LKW and zero-emission carve-outs.
3. **Austria has extensive domestic reverse charge** (construction, scrap, emission certificates) which Malta largely lacks.
4. **Austria uses Kennzahl numbers** (Kz 000, 001, 006, etc.) while Malta uses Box numbers (Box 1-45). The classification logic is similar but mapped differently.
5. **Austria's annual return (U1) is separate from UVAs**, while Malta integrates quarterly returns into a single ongoing cycle.
6. **Austria's Kleinunternehmer opt-in is binding for 5 years** (§6(3) UStG 1994); Malta's Article 11 has different transition rules.

---

## Section 11: PROHIBITIONS [T1]

1. **NEVER let AI guess Kennzahl numbers** -- they are 100% deterministic from the transaction facts. Use the lookup tables in Section 2.
2. **NEVER apply Kleinunternehmer exemption if gross turnover > EUR 55,000** (or > EUR 60,500 with one-time 10% tolerance). §6(1)(27) UStG 1994 as amended by Progressionsentlastungsgesetz 2025.
3. **NEVER skip reverse charge for Kleinunternehmer** -- §19 UStG 1994 overrides §6(1)(27). Kleinunternehmer MUST self-assess and pay output USt on reverse charge supplies. No Vorsteuer recovery.
4. **NEVER allow Kleinunternehmer to claim Vorsteuer** -- input tax deduction is denied under §12(3) UStG 1994 for exempt supplies.
5. **NEVER apply reverse charge to out-of-scope categories** (salaries, dividends, loan repayments, social contributions). These are NOT supplies under §1 UStG 1994.
6. **NEVER apply reverse charge to local consumption abroad** (hotel, restaurant, taxi in another country). VAT is paid at source. Not recoverable on Austrian UVA.
7. **NEVER recover Vorsteuer on passenger vehicles (PKW)** -- fully blocked under §12(2)(2)(b) UStG 1994. Only exceptions: Fiskal-LKW (verified against BMF list), zero-emission vehicles (capped at EUR 40,000 gross), taxis, driving schools, rental fleet.
8. **NEVER recover Vorsteuer on entertainment (Bewirtung)** unless advertising character (Werbecharakter) exceeds 50%. §12(2)(2)(a) UStG 1994; §20(1)(3) EStG 1988.
9. **NEVER confuse zero-rated exports (Kz 011/017, input VAT deductible) with exempt supplies (Kz 020, input VAT NOT deductible)**. §6(1)(1)-(5) = with credit. §6(1)(6)-(27) = without credit.
10. **NEVER apply the 13% rate to wine sold through retail or restaurants** -- 13% is exclusively for Ab-Hof-Verkauf by the producing farmer. §10(3) Z 1 UStG 1994.
11. **NEVER apply §19(1a) Bauleistungen reverse charge when the recipient is NOT in the construction sector** -- both parties must provide Bauleistungen.
12. **NEVER zero-rate an IC supply without a verified UID-Nummer** of the recipient. Art 7 BMR.
13. **NEVER compute any number** -- all arithmetic is handled by the deterministic engine, not Claude. Claude classifies and assigns Kennzahlen only.
14. **NEVER file a UVA for a Kleinunternehmer** unless they have opted into Regelbesteuerung or have reverse charge obligations requiring UID registration.
15. **NEVER confuse Soll-Versteuerung (accrual) with Ist-Versteuerung (cash basis)** -- the timing of when USt is owed differs. §17 UStG 1994.

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

## Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Do not execute any of these rules. Escalate to Steuerberater.

- **Einkommensteuer (ESt):** Progressive rates 0% / 20% / 30% / 40% / 48% / 50% / 55%. §33 EStG 1988.
- **Koerperschaftsteuer (KoeSt):** 23% flat rate (from 2024). §22 KStG 1988.
- **Kommunalsteuer:** 3% municipal tax on gross payroll. Kommunalsteuergesetz 1993.
- **Sozialversicherung (SV):** Separate obligation under ASVG/GSVG/BSVG. Not part of VAT return.
- **Dienstgeberbeitrag (DB):** 3.9% employer contribution to Family Burden Equalisation Fund (FLAF).
- **Dienstgeberzuschlag (DZ):** Varies by Bundesland (0.34%-0.42%).

---

## Contribution Notes

Adapted from the Malta VAT Return Skill template (version 1.0, validated March 2026). All legislation references, Kennzahl numbers, thresholds, rates, and blocked categories are specific to Austria and cite UStG 1994. VAT rates confirmed against PWC Tax Summaries (Austria -- Corporate -- Other Taxes) as of April 2026.

**A skill may not be published without sign-off from a Steuerberater or Wirtschaftspruefer in Austria.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
