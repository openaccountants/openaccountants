---
name: switzerland-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Swiss VAT return (MWST/TVA/IVA Abrechnung), or any request involving Swiss VAT filing, Saldosteuersatz, Bezugsteuer (reverse charge), or import VAT. Trigger on phrases like "prepare Swiss VAT return", "MWST Abrechnung", "Swiss VAT", "Saldosteuersatz", "Bezugsteuer", or any request involving Switzerland VAT obligations. This skill contains the complete Swiss VAT classification rules, form mappings, rate schedules, blocked input tax categories, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Swiss VAT-related work.
---

# Switzerland VAT (MWST/TVA/IVA) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Switzerland (and Liechtenstein customs union) |
| Jurisdiction Code | CH |
| Primary Legislation | Mehrwertsteuergesetz (MWSTG), SR 641.20 (Federal Act on Value Added Tax, 12 June 2009, as amended) |
| Supporting Legislation | Mehrwertsteuerverordnung (MWSTV), SR 641.201; Saldosteuersatzverordnung; ESTV guidelines (Praxisfestlegungen) |
| Tax Authority | Eidgenossische Steuerverwaltung (ESTV) / Administration federale des contributions (AFC) |
| Filing Portal | https://www.estv.admin.ch (ESTV SuisseTax / ePortal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, form box assignment, Bezugsteuer mechanics, derived calculations. Tier 2: Saldosteuersatz election, partial use apportionment, Margenbesteuerung. Tier 3: group taxation (Gruppenbesteuerung), cross-canton complexities, ESTV rulings. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed Swiss tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed adviser and document the gap.

---

## Key Difference from EU VAT Skills

Switzerland is **NOT** a member of the European Union. This has critical consequences:

1. There are NO intra-community acquisitions. All goods from ALL countries (including EU) are imports subject to import VAT at the border (collected by BAZG/OFDF, the Federal Office for Customs and Border Security). [T1]
2. The EU reverse charge mechanism for intra-community goods does NOT apply. [T1]
3. Bezugsteuer (reverse charge / acquisition tax) applies to services received from abroad (Art. 45 MWSTG) and certain other situations. [T1]
4. Liechtenstein is in a customs union with Switzerland and is treated as domestic territory for MWST purposes (Art. 3 let. a MWSTG). [T1]
5. Switzerland has bilateral agreements with the EU but these do not extend VAT harmonisation.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and UID number** [T1] -- CHE-xxx.xxx.xxx MWST (Unternehmens-Identifikationsnummer)
2. **Registration method** [T1] -- Effektive Methode (effective method) or Saldosteuersatz/Pauschalsteuersatz (flat-rate/simplified method)
3. **Applicable Saldosteuersatz(e)** [T2] -- if flat-rate method, which rate(s) approved by ESTV (0.1% to 6.5%, sector-dependent)
4. **VAT period** [T1] -- quarterly (standard) or semi-annual (by election, Art. 35 MWSTG) or monthly (by election)
5. **Industry/sector** [T2] -- impacts Saldosteuersatz eligibility and rate
6. **Does the business make exempt supplies (Art. 21 MWSTG)?** [T2] -- if yes, Vorsteuerabzugskorrektur (input tax correction) required
7. **Does the business receive services from abroad?** [T1] -- triggers Bezugsteuer assessment
8. **Annual turnover** [T1] -- relevant for registration threshold (CHF 100,000)
9. **Does the business export goods or supply services abroad?** [T1] -- zero-rated under Art. 23 MWSTG

**If items 1-2 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (Umsatzsteuer / output VAT) or Purchase (Vorsteuer / input VAT)
- Salaries, social insurance contributions (AHV/IV/EO/ALV), loan repayments, dividends, direct federal/cantonal taxes = OUT OF SCOPE (never on VAT return)
- **Legislation:** Art. 18 MWSTG (taxable supplies)

### 1b. Determine Counterparty Location [T1]
- **Domestic (Inland):** Switzerland + Liechtenstein (Art. 3 let. a MWSTG)
- **Abroad (Ausland):** All other countries, INCLUDING all EU member states
- There is no EU/non-EU distinction for Swiss MWST -- all foreign countries are treated uniformly as "Ausland"

### 1c. Determine VAT Rate [T1]

**Legislation:** Art. 25 MWSTG, as amended by Federal Decree of 25 September 2022 (AHV21 financing).

| Rate | Percentage (from 1 Jan 2024) | Previous (to 31 Dec 2023) | Description | MWSTG Reference |
|------|------------------------------|---------------------------|-------------|-----------------|
| Standard (Normalsatz) | 8.1% | 7.7% | Default rate for all supplies not qualifying for reduced or special rate | Art. 25 al. 1 MWSTG |
| Reduced (Reduzierter Satz) | 2.6% | 2.5% | Food, non-alcoholic beverages, books, newspapers, magazines, medicines, agricultural inputs, menstrual hygiene products (from 2025) | Art. 25 al. 1bis and 2 MWSTG; Annex to Art. 25 |
| Special (Sondersatz) | 3.8% | 3.7% | Accommodation services (Beherbergungsleistungen) | Art. 25 al. 4 MWSTG |

**Rate application rules:** [T1]
- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Normalize to nearest standard rate: 2.6%, 3.8%, or 8.1%
- Boundaries: <= 1% = likely zero-rated; 1.5-3.2% = 2.6%; 3.2-5.5% = 3.8%; >= 6% = 8.1%
- If invoice straddles the 2023/2024 rate change, split by supply date (Leistungsdatum), not invoice date

### 1d. Zero-Rated and Exempt Supplies [T1]

| Category | Treatment | Reference |
|----------|-----------|-----------|
| Exports of goods | Zero-rated (genuinely exempt with credit, "echte Steuerbefreiung") | Art. 23 al. 2 ch. 1 MWSTG |
| Services to recipients abroad (place of supply abroad) | Zero-rated | Art. 23 al. 2 ch. 2 MWSTG |
| International transport | Zero-rated | Art. 23 al. 2 ch. 5-7 MWSTG |
| Healthcare (excluding elective) | Exempt without credit ("unechte Steuerbefreiung") | Art. 21 al. 2 ch. 2-3 MWSTG |
| Education | Exempt without credit | Art. 21 al. 2 ch. 11 MWSTG |
| Financial services (interest, securities trading) | Exempt without credit | Art. 21 al. 2 ch. 19 MWSTG |
| Insurance | Exempt without credit | Art. 21 al. 2 ch. 18 MWSTG |
| Rental of immovable property | Exempt without credit (option to tax available, Art. 22 MWSTG) | Art. 21 al. 2 ch. 21 MWSTG |
| Cultural events (admission) | Exempt without credit | Art. 21 al. 2 ch. 14 MWSTG |

**Critical distinction:** [T1]
- **Echte Steuerbefreiung (Art. 23):** Supply is exempt WITH full input tax recovery. Turnover reported in Ziffer 220.
- **Unechte Steuerbefreiung (Art. 21):** Supply is exempt WITHOUT input tax recovery. Turnover reported in Ziffer 230. Any input tax attributable to these supplies must be corrected (Vorsteuerabzugskorrektur).

---

## Step 2: MWST Abrechnung Form Structure (Effective Method) [T1]

**Legislation:** Art. 35-36 MWSTG; ESTV Abrechnung form (Form 050.1).

The Swiss MWST return uses a "Ziffer" (reference number) system. Below is the complete mapping.

### I. Turnover (Umsatz)

| Ziffer | Description | Classification |
|--------|-------------|----------------|
| 200 | Total consideration (Gesamtbetrag der vereinbarten oder vereinnahmten Entgelte) | Total revenue including exempt |
| 205 | Consideration reported in Ziff. 200 from non-taxable supplies (Art. 21) not opted into | Deduction |
| 210 | Supplies abroad (place of supply abroad, Art. 23 al. 1) | Deduction |
| 220 | Exempt supplies with input tax deduction (exports etc., Art. 23 al. 2) | Deduction |
| 221 | Supplies to beneficiaries under Art. 107 al. 1 lit. b (international organisations) | Deduction (subset of 220) |
| 225 | Transfer of assets under restructuring (Art. 19) | Deduction |
| 230 | Supplies exempt without credit (Art. 21) where option NOT exercised | Deduction |
| 235 | Reduction of consideration (discounts, rebates, losses) | Deduction |
| 280 | Miscellaneous (subsidies, tourist tax, etc.) -- Diverse | Informational |
| 289 | **Total taxable turnover** (= 200 - 205 - 210 - 220 - 225 - 230 - 235) | Calculated |

### II. Tax Calculation (Steuerberechnung)

| Ziffer | Description | Rate |
|--------|-------------|------|
| 302 | Supplies at standard rate | 8.1% |
| 312 | Supplies at reduced rate | 2.6% |
| 342 | Supplies at special rate (accommodation) | 3.8% |
| 382 | **Bezugsteuer (Acquisition tax / reverse charge)** | 8.1% (or applicable rate) |
| 399 | **Total tax payable** (sum of tax on 302 + 312 + 342 + 382) | Calculated |

### III. Input Tax (Vorsteuer)

| Ziffer | Description |
|--------|-------------|
| 400 | Input tax on purchases of materials/services (Vorsteuer auf Material- und Dienstleistungsaufwand) |
| 405 | Input tax on investments and other operating costs (Vorsteuer auf Investitionen und uebrigem Betriebsaufwand) |
| 410 | Eigenverbrauch correction (de-taxation, Art. 31 MWSTG) |
| 415 | Input tax correction: mixed use, change of use (Vorsteuerabzugskorrektur, Art. 30 MWSTG) |
| 420 | Reduction of input tax deduction: flow of funds not consideration (subsidies, etc.) (Art. 33 al. 2 MWSTG) |
| 479 | **Total input tax** (= 400 + 405 + 410 - 415 - 420) | Calculated |

### IV. Result

| Ziffer | Description |
|--------|-------------|
| 500 | Amount payable to ESTV (if 399 > 479) |
| 510 | Credit in favour of taxable person (if 479 > 399) |

### V. Other Flows of Funds

| Ziffer | Description |
|--------|-------------|
| 900 | Subsidies, tourist taxes, financial contributions from public entities |
| 910 | Donations, dividends, damages, etc. |

---

## Step 3: Bezugsteuer (Acquisition Tax / Reverse Charge) [T1]

**Legislation:** Art. 45-49 MWSTG.

Bezugsteuer is Switzerland's equivalent of the EU reverse charge. It applies when:

1. **Services received from a business with its registered office abroad** (Art. 45 al. 1 let. a MWSTG) [T1]
2. **Import of goods exempt from import VAT** in certain situations [T2]
3. **Goods acquired from non-registered suppliers in Switzerland** under specific conditions [T2]

### Bezugsteuer Mechanics [T1]

1. Identify the service/supply received from abroad where the place of supply is Switzerland
2. Self-assess MWST at the applicable rate (normally 8.1%) on the consideration paid
3. Report the tax amount in **Ziffer 382** (output side)
4. Claim input tax deduction in **Ziffer 400 or 405** (input side) -- subject to normal deduction rules
5. Net effect: zero for fully taxable businesses; partial impact for businesses with exempt supplies

### Bezugsteuer Threshold [T1]

Bezugsteuer is due when the total of services received from abroad in a calendar year exceeds **CHF 10,000** (Art. 45 al. 1 let. a MWSTG). Below this threshold, no Bezugsteuer is owed.

**IMPORTANT:** This CHF 10,000 threshold is an annual cumulative total, not per-transaction. Once breached, Bezugsteuer applies to ALL such services for the year, including those received before the threshold was exceeded. [T1]

### When Bezugsteuer Does NOT Apply [T1]

- Supplier has a Swiss VAT registration and charges MWST on the invoice
- Supply is exempt under Art. 21 MWSTG
- Services where the place of supply is NOT Switzerland under Art. 8 MWSTG
- Physical goods imported through customs (import VAT handled by BAZG, not Bezugsteuer)
- Out-of-scope items (wages, dividends, loan interest)

---

## Step 4: Import VAT (Einfuhrsteuer) [T1]

**Legislation:** Art. 50-64 MWSTG; Zollgesetz (ZG), SR 631.0.

Unlike EU member states, Switzerland levies import VAT on ALL goods entering the country, including from EU states.

### Import VAT Mechanics [T1]

| Step | Description |
|------|-------------|
| 1 | Goods arrive at Swiss border (or Liechtenstein border) |
| 2 | BAZG (Bundesamt fuer Zoll und Grenzsicherheit) assesses import VAT on customs value |
| 3 | Import VAT is paid to BAZG (not ESTV) -- either by importer or customs broker |
| 4 | BAZG issues Veranlagungsverfuegung (customs assessment decision) |
| 5 | Import VAT paid is recoverable as input tax in Ziffer 400 or 405 on the MWST return |

### Import VAT Rates [T1]

Same rates as domestic supplies:
- 8.1% standard
- 2.6% reduced (food, medicines, books etc.)
- Certain goods are exempt from import VAT (Art. 53 MWSTG): e.g., personal effects, small consignments under CHF 5 value

### Import VAT Recovery [T1]

- Recoverable for registered businesses, subject to same input tax deduction rules as domestic purchases
- Must be supported by the Veranlagungsverfuegung (customs document) -- not the commercial invoice alone
- Claim in the period the Veranlagungsverfuegung is issued

---

## Step 5: Saldosteuersatz Method (Flat-Rate Method) [T2]

**Legislation:** Art. 37 MWSTG; Saldosteuersatzverordnung.

### Overview

The Saldosteuersatz (SSS) method is a simplified filing method for small businesses. Instead of tracking actual input tax, the business applies an approved flat rate to gross turnover.

### Eligibility [T2]

| Criterion | Threshold |
|-----------|-----------|
| Annual domestic turnover | <= CHF 5,005,000 |
| Annual tax liability (at effective method) | <= CHF 103,000 |
| No group taxation (Gruppenbesteuerung) | Must not be part of a VAT group |

### How It Works [T1 if rate is known, T2 for rate determination]

1. ESTV assigns one or two Saldosteuersaetze based on the business's activities (rates range from 0.1% to 6.5%)
2. Tax payable = Gross revenue (including MWST) x Saldosteuersatz
3. No separate input tax deduction is claimed -- it is deemed included in the flat rate
4. No Bezugsteuer self-assessment for services under CHF 10,000/year from abroad
5. Bezugsteuer still applies above CHF 10,000 threshold
6. Import VAT is still paid at the border and is NOT recoverable under SSS method

### SSS Form Differences [T1]

The SSS Abrechnung (Form 050.3) is simpler:
- Report gross turnover by Saldosteuersatz
- Multiply by approved rate
- No input tax section
- Still report exports (zero-rated) separately

**PROHIBITION:** A business using SSS method CANNOT claim input tax deductions. If client is on SSS, do NOT populate Ziffer 400/405. [T1]

---

## Step 6: Deductibility Check

### Blocked Input Tax (Vorsteuerabzugsausschluesse) [T1]

**Legislation:** Art. 33 MWSTG.

Unlike Malta's extensive 10th Schedule, Switzerland has a narrower set of blocked categories:

| Category | Blocked? | Reference |
|----------|----------|-----------|
| Private use / non-business use | Blocked (proportional) | Art. 30 MWSTG |
| Supplies used for exempt (Art. 21) outputs | Blocked (unless option to tax exercised under Art. 22) | Art. 29 al. 1 / Art. 30 MWSTG |
| Subsidised activities (non-consideration funding) | Reduction required | Art. 33 al. 2 MWSTG |
| Entertainment | **NOT specifically blocked** (deductible if business purpose) | No equivalent to Malta 10th Schedule |
| Motor vehicles (business use) | **NOT specifically blocked** (deductible if business use; private portion must be corrected) | Art. 30 MWSTG |
| Food and drink for staff | Deductible if business purpose | -- |

**Key difference from Malta and EU:** Switzerland does NOT have a blanket entertainment block. Business entertainment expenses are deductible for MWST purposes if they serve a business purpose. Private use must be corrected (Eigenverbrauch). [T1]

### Eigenverbrauch (Deemed Supply / Private Use) [T1]

**Legislation:** Art. 31 MWSTG.

If business assets are used for non-business purposes (private use), or if the business ceases to be taxable:
- A deemed supply (Eigenverbrauch) is triggered
- MWST must be accounted for on the fair value
- Reported as a correction in Ziffer 410 (if de-taxing) or as an adjustment

### Mixed Use Correction [T2]

**Legislation:** Art. 30 MWSTG.

If an asset or expense is used for both taxable and exempt (or private) purposes:
- Input tax must be apportioned
- Methods: actual use, turnover-based pro-rata, or other appropriate method approved by ESTV
- Correction reported in Ziffer 415
- **Flag for reviewer:** apportionment method must be confirmed by licensed adviser

---

## Step 7: Registration Rules

**Legislation:** Art. 10-14 MWSTG.

| Criterion | Threshold / Rule |
|-----------|-----------------|
| Mandatory registration | Domestic turnover exceeds CHF 100,000 per calendar year (Art. 10 al. 2 let. a MWSTG) |
| Voluntary registration | Any amount (Art. 14 MWSTG) -- useful for input tax recovery |
| Foreign businesses | Must register if supplying goods/services in Switzerland with no reverse charge applicable (Art. 10 al. 2 let. b MWSTG) |
| Small business exemption (Befreiung) | Turnover <= CHF 100,000: may opt not to register (Art. 10 al. 2) |
| Non-profit / public entities | Mandatory if turnover from taxable supplies > CHF 150,000 (Art. 10 al. 2 let. c MWSTG) |
| Group taxation | Available under Art. 13 MWSTG; closely connected entities can form a VAT group [T3] |
| Liechtenstein entities | Same rules; Liechtenstein is domestic territory |

### De-registration [T1]

- If turnover drops below CHF 100,000, the business may request de-registration
- Must settle Eigenverbrauch on remaining assets
- Cannot de-register retroactively if Bezugsteuer obligations exist

---

## Step 8: Filing Deadlines and Penalties

### Filing Periods [T1]

**Legislation:** Art. 35 MWSTG.

| Period | Frequency | Quarters |
|--------|-----------|----------|
| Standard | Quarterly | Q1: Jan-Mar, Q2: Apr-Jun, Q3: Jul-Sep, Q4: Oct-Dec |
| Election: semi-annual | Semi-annual | H1: Jan-Jun, H2: Jul-Dec |
| Election: monthly | Monthly | Each calendar month |

### Deadlines [T1]

| Period Type | Deadline |
|-------------|----------|
| Quarterly | 60 days after end of quarter (e.g., Q1 due 30 May) |
| Semi-annual | 60 days after end of half-year |
| Monthly | 60 days after end of month |

**Note:** These are 60 calendar days from period end, not business days. If the 60th day falls on a weekend or public holiday, the deadline is the next business day.

### Penalties [T1]

**Legislation:** Art. 86-88 MWSTG; Art. 96 MWSTG (criminal provisions).

| Violation | Consequence |
|-----------|-------------|
| Late filing | Reminder from ESTV; if no filing, estimation assessment (Ermessenseinschaetzung) |
| Late payment | Default interest (Verzugszins) at 4.0% p.a. (Art. 87 MWSTG) |
| Tax evasion (intent) | Fine up to CHF 400,000 or 3x the tax evaded (Art. 96 MWSTG) |
| Tax fraud (falsification) | Imprisonment up to 3 years or fine (Art. 98 MWSTG) |
| Failure to register | Back-assessment of tax + default interest |

### Annual Reconciliation (Finalisierung) [T1]

**Legislation:** Art. 72 MWSTG.

- Within 180 days of the end of the financial year, the taxable person must reconcile the MWST returns with the annual financial statements
- If discrepancies exist, a correction (Korrekturabrechnung) must be filed
- This is a MANDATORY annual process, not optional

---

## Step 9: Derived Calculations [T1]

```
Ziffer 289 = Ziffer 200 - 205 - 210 - 220 - 225 - 230 - 235

Ziffer 399 = Tax on Ziffer 302 (at 8.1%)
           + Tax on Ziffer 312 (at 2.6%)
           + Tax on Ziffer 342 (at 3.8%)
           + Ziffer 382

Ziffer 479 = Ziffer 400 + 405 + 410 - 415 - 420

IF Ziffer 399 > Ziffer 479 THEN
  Ziffer 500 = Ziffer 399 - Ziffer 479   -- Amount payable to ESTV
  Ziffer 510 = 0
ELSE
  Ziffer 500 = 0
  Ziffer 510 = Ziffer 479 - Ziffer 399   -- Credit (refund)
END
```

---

## Step 10: Classification Matrix [T1]

### Purchases -- Domestic (Switzerland + Liechtenstein)

| VAT Rate | Category | Ziffer (Net) | Ziffer (Tax) |
|----------|----------|--------------|--------------|
| 8.1% | Materials/services | -- | 400 |
| 2.6% | Materials/services | -- | 400 |
| 3.8% | Materials/services (accommodation) | -- | 400 |
| 8.1% | Investments/operating costs | -- | 405 |
| 2.6% | Investments/operating costs | -- | 405 |
| 0% | Exempt supply | -- | No recovery |

**Note:** Swiss MWST returns do not itemise purchases by rate in the way Malta does. Input tax is simply totalled into Ziffer 400 (materials/services) or Ziffer 405 (investments/other operating costs). The rate distinction matters for verification but not for form placement.

### Purchases -- Foreign Supplier (Services, Bezugsteuer)

| Type | Bezugsteuer Ziffer | Input Tax Ziffer | Condition |
|------|-------------------|-----------------|-----------|
| Services from abroad (>= CHF 10,000 cumulative/year) | 382 | 400 or 405 | Place of supply is CH |
| Services from abroad (< CHF 10,000/year) | None | None | Below threshold |
| Physical goods imported | N/A (import VAT via BAZG) | 400 or 405 | Veranlagungsverfuegung required |

### Sales -- Domestic

| Rate | Ziffer (Net) | Tax Calculated On |
|------|--------------|-------------------|
| 8.1% | 302 | Net amount x 8.1% |
| 2.6% | 312 | Net amount x 2.6% |
| 3.8% | 342 | Net amount x 3.8% |

### Sales -- Abroad

| Type | Ziffer | Notes |
|------|--------|-------|
| Exports (Art. 23 al. 2) | 220 | Deducted from Ziffer 200; input tax fully recoverable |
| Place of supply abroad (Art. 23 al. 1) | 210 | Deducted from Ziffer 200 |
| Exempt without credit (Art. 21) | 230 | Deducted from Ziffer 200; NO input tax recovery |

---

## Step 11: Edge Case Registry

### EC1 -- Software subscription from US provider (e.g., Microsoft 365, AWS) [T1]
**Situation:** Swiss business pays monthly subscription to a US SaaS provider. No MWST on invoice.
**Resolution:** Bezugsteuer applies IF annual total of all foreign services >= CHF 10,000. Self-assess at 8.1% in Ziffer 382. Claim input tax in Ziffer 400. Net effect zero for fully taxable business.
**Legislation:** Art. 45 al. 1 let. a MWSTG.

### EC2 -- Import of physical goods from Germany [T1]
**Situation:** Swiss business orders machinery from a German supplier. Goods cross the border.
**Resolution:** This is NOT an intra-community acquisition (Switzerland is not in the EU). Import VAT is assessed and paid at customs (BAZG). Recover import VAT in Ziffer 400/405 based on Veranlagungsverfuegung. Do NOT use Bezugsteuer (Ziffer 382).
**Legislation:** Art. 50-52 MWSTG.

### EC3 -- Hotel stay in Switzerland billed to foreign client [T1]
**Situation:** Foreign client stays at a Swiss hotel. Hotel invoices at 3.8%.
**Resolution:** Accommodation in Switzerland is subject to the special rate of 3.8%. Report in Ziffer 342 (output). The fact that the customer is foreign does not change the rate -- place of supply for accommodation is where the property is located.
**Legislation:** Art. 25 al. 4 MWSTG; Art. 8 al. 2 let. a MWSTG.

### EC4 -- Business entertainment (client dinner) [T1]
**Situation:** Swiss business takes clients to dinner. Restaurant invoice shows 8.1% MWST.
**Resolution:** MWST on business entertainment IS recoverable in Switzerland (unlike Malta). Claim in Ziffer 400. No blocked category applies. However, if any private element exists, the private portion must be excluded (Eigenverbrauch correction in Ziffer 415).
**Legislation:** Art. 28 MWSTG (general input tax deduction right); no equivalent to Malta 10th Schedule block.

### EC5 -- Motor vehicle purchase for business [T2]
**Situation:** Business purchases a car for CHF 45,000 + CHF 3,645 MWST.
**Resolution:** Input tax on motor vehicles IS recoverable in Switzerland if used for business purposes. Claim in Ziffer 405. However, if the vehicle is also used privately (e.g., by a director), private use must be corrected. ESTV provides deemed private use percentages (typically 9.6% of purchase price per year for luxury vehicles, or actual logbook method). Flag for reviewer: confirm private use percentage.
**Legislation:** Art. 28, Art. 31 MWSTG; ESTV Praxisfestlegung on Privatanteil.

### EC6 -- Transitional rate change (invoice straddles 2023/2024) [T1]
**Situation:** Service performed in December 2023, invoiced in January 2024.
**Resolution:** The applicable rate is determined by the date of supply (Leistungsdatum), not the invoice date. December 2023 services = 7.7%. January 2024 services = 8.1%. If a single invoice covers both periods, the invoice must split the amounts by rate period.
**Legislation:** Art. 115a MWSTG (transitional provisions for rate changes).

### EC7 -- Liechtenstein supplier [T1]
**Situation:** Swiss business receives invoice from a Liechtenstein company with MWST charged.
**Resolution:** Treat as domestic supply. Liechtenstein is part of the Swiss MWST territory. Recover input tax normally in Ziffer 400/405. Do NOT treat as import or apply Bezugsteuer.
**Legislation:** Art. 3 let. a MWSTG.

### EC8 -- Exempt supplies with option to tax (Immobilien) [T2]
**Situation:** Client rents out commercial property. Rental is normally exempt (Art. 21 al. 2 ch. 21).
**Resolution:** The client may exercise the option to tax (Art. 22 MWSTG), charging MWST on rent. This allows input tax recovery on property-related costs. Flag for reviewer: option must be explicitly exercised with ESTV and noted on invoices. Once opted, applies for at least one year.
**Legislation:** Art. 22 MWSTG.

### EC9 -- Small consignment import (< CHF 5 import VAT) [T1]
**Situation:** Business imports a small item from abroad; import VAT would be less than CHF 5.
**Resolution:** No import VAT is collected by BAZG if the tax amount is less than CHF 5 (Art. 53 al. 1 let. d MWSTG, currently goods up to approximately CHF 62 at 8.1%). No Veranlagungsverfuegung issued. No input tax to claim.
**Legislation:** Art. 53 al. 1 let. d MWSTG.

### EC10 -- Freelancer under CHF 100,000 turnover, voluntary registration [T2]
**Situation:** IT freelancer earns CHF 80,000/year, wants to register voluntarily to reclaim input tax on equipment purchases.
**Resolution:** Voluntary registration is permitted under Art. 14 MWSTG. Once registered, ALL supplies become taxable (must charge MWST). Cannot cherry-pick. Must file returns and comply with all obligations. Flag for reviewer: cost-benefit analysis should be discussed -- registration is beneficial if input tax on costs exceeds the administrative burden.
**Legislation:** Art. 14 MWSTG.

### EC11 -- Bezugsteuer on intercompany management fees from foreign parent [T1]
**Situation:** Swiss subsidiary receives management services from its German parent company, invoiced at EUR 50,000/year.
**Resolution:** Bezugsteuer applies (services from abroad, place of supply is Switzerland, exceeds CHF 10,000). Self-assess at 8.1% in Ziffer 382. Claim input tax in Ziffer 400. The intercompany nature does not change the treatment unless a VAT group exists (Swiss VAT groups cannot include foreign entities).
**Legislation:** Art. 45 MWSTG; Art. 13 MWSTG (group taxation limited to domestic entities).

### EC12 -- Credit notes [T1]
**Situation:** Supplier issues a credit note reducing a previous invoice.
**Resolution:** Reduce the turnover/input tax in the period the credit note is issued. For the supplier: reduce Ziffer 302/312/342 accordingly. For the recipient: reduce Ziffer 400/405. Report in Ziffer 235 if shown as a global discount/reduction.
**Legislation:** Art. 44 MWSTG.

---

## Step 12: EU Comparison Table

| Feature | Switzerland (MWST) | EU (Common System Directive 2006/112/EC) |
|---------|-------------------|------------------------------------------|
| Standard rate | 8.1% | 15% minimum; most states 19-27% |
| Reduced rates | 2.6% + 3.8% special | Varies; typically 2+ reduced rates |
| Registration threshold | CHF 100,000 (~EUR 103,000) | Varies: EUR 0 to EUR 85,000 |
| Intra-community supplies | N/A (not in EU) | Zero-rated B2B with reporting |
| Import VAT on EU goods | Yes, at border | No (intra-community acquisition instead) |
| Reverse charge on services | Bezugsteuer (Art. 45) with CHF 10,000 threshold | Art. 196 Directive -- no threshold |
| Flat-rate scheme | Saldosteuersatz (Art. 37) | Various national schemes |
| Filing frequency | Quarterly (default) | Varies by state |
| Filing deadline | 60 days after period end | Varies; typically 20-30 days |
| Annual reconciliation | Mandatory (180 days after FY end) | Not universally required |
| Entertainment deduction | Fully deductible (no block) | Varies; many states block |
| Motor vehicle deduction | Deductible (private use correction) | Many states block or restrict |
| VAT group | Domestic entities only (Art. 13) | Available in most states |
| Digital services to consumers | MWST registration required for foreign suppliers > CHF 100,000 | OSS/IOSS schemes |

---

## Step 13: Filing Checklist [T1]

Before submitting the MWST Abrechnung, verify:

- [ ] All invoices issued in the period are included in turnover (Ziffer 200)
- [ ] Export evidence (customs declarations, proof of dispatch) supports Ziffer 220 amounts
- [ ] Bezugsteuer has been assessed on all foreign services if annual total >= CHF 10,000
- [ ] Import VAT claims are supported by Veranlagungsverfuegungen from BAZG
- [ ] Input tax split correctly between Ziffer 400 (materials/services) and Ziffer 405 (investments)
- [ ] Eigenverbrauch corrections applied for private use of business assets
- [ ] Corrections for exempt supply attribution entered in Ziffer 415
- [ ] Rate applied matches the date of supply, not invoice date (critical around rate changes)
- [ ] Annual reconciliation (Finalisierung) filed within 180 days of FY end
- [ ] All amounts in CHF (foreign currency converted at time of supply or average rate per ESTV guidance)

---

## PROHIBITIONS [T1]

- NEVER treat Switzerland as an EU member state -- it is NOT in the EU
- NEVER apply intra-community acquisition rules to Swiss imports -- ALL goods imports go through BAZG customs
- NEVER apply Bezugsteuer to physical goods imports (use import VAT via BAZG instead)
- NEVER ignore the CHF 10,000 annual threshold for Bezugsteuer on services from abroad
- NEVER allow input tax deduction for a Saldosteuersatz client -- flat-rate method precludes Vorsteuerabzug
- NEVER apply old rates (7.7%/2.5%/3.7%) to supplies made on or after 1 January 2024
- NEVER treat Liechtenstein as a foreign country for MWST purposes -- it is domestic territory
- NEVER file without performing the annual Finalisierung reconciliation
- NEVER assume entertainment expenses are blocked -- Switzerland does NOT block business entertainment for MWST
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER let AI guess Ziffer assignment -- it must be deterministic from the classification facts
- NEVER claim import VAT without a Veranlagungsverfuegung (customs assessment document)

---

## Step 14: Test Suite

### Test 1 -- Standard domestic purchase, 8.1% MWST [T1]
**Input:** Swiss supplier, office furniture, gross CHF 1,081, MWST CHF 81, net CHF 1,000. Effective method. Fully taxable business.
**Expected output:** Ziffer 405 (input tax) += CHF 81. Classified as investment/operating cost.

### Test 2 -- Reduced rate domestic sale [T1]
**Input:** Swiss bakery sells bread. Net CHF 500, MWST CHF 13 (2.6%).
**Expected output:** Ziffer 200 += CHF 513 (gross), Ziffer 312 += CHF 500 (net at reduced rate). Tax on 312 = CHF 13.

### Test 3 -- Bezugsteuer on foreign services [T1]
**Input:** Swiss consulting firm receives legal advice from a UK law firm, GBP 8,000 (~CHF 9,200). Total foreign services for the year already CHF 5,000. Cumulative now CHF 14,200 (> CHF 10,000 threshold).
**Expected output:** Bezugsteuer triggered. Ziffer 382 = CHF 14,200 x 8.1% = CHF 1,150.20 (on full year amount including prior). Ziffer 400 += CHF 1,150.20. Net effect zero. Flag: retrospective assessment on the first CHF 5,000 that was below threshold.

### Test 4 -- Import of goods from Germany [T1]
**Input:** Swiss manufacturer imports raw materials from Germany, invoice EUR 10,000 (~CHF 9,700). BAZG issues Veranlagungsverfuegung: import VAT CHF 785.70 (8.1%).
**Expected output:** Import VAT CHF 785.70 recoverable in Ziffer 400. NO Bezugsteuer entry. NO Ziffer 382.

### Test 5 -- Export of goods [T1]
**Input:** Swiss watchmaker exports watches to Japan, invoice CHF 50,000. Customs export declaration available.
**Expected output:** Ziffer 200 += CHF 50,000. Ziffer 220 += CHF 50,000 (deduction for exempt with credit). No output tax. Full input tax recovery on related purchases.

### Test 6 -- Saldosteuersatz client [T1]
**Input:** Hairdresser using SSS method, approved rate 5.1%. Quarterly gross revenue CHF 30,000.
**Expected output:** Tax payable = CHF 30,000 x 5.1% = CHF 1,530. No input tax section. No Ziffer 400/405.

### Test 7 -- Motor vehicle with private use [T2]
**Input:** Director purchases car for business, CHF 50,000 + MWST CHF 4,050. Estimated 20% private use.
**Expected output:** Ziffer 405 += CHF 4,050 (full input tax claimed). Ziffer 415 += CHF 810 (20% private use correction = CHF 4,050 x 20%). Net input tax recovery = CHF 3,240. Flag for reviewer: confirm private use percentage.

### Test 8 -- Business entertainment dinner [T1]
**Input:** Client dinner at Zurich restaurant, CHF 540 gross, MWST CHF 40.40 (8.1%), net CHF 499.60. 100% business purpose, no private element.
**Expected output:** Ziffer 400 += CHF 40.40. Fully deductible. No entertainment block in Switzerland.

### Test 9 -- Exempt supply (financial services) [T1]
**Input:** Swiss bank earns interest income CHF 200,000 and advisory fee income CHF 100,000 (taxable). Interest is exempt under Art. 21 al. 2 ch. 19.
**Expected output:** Ziffer 200 += CHF 300,000 (total). Ziffer 230 += CHF 200,000 (exempt without credit). Ziffer 302 += CHF 100,000 (advisory at 8.1%). Input tax must be apportioned -- only 1/3 recoverable (Ziffer 415 correction required). [T2 for apportionment method]

### Test 10 -- Liechtenstein supplier [T1]
**Input:** Swiss company receives IT services from Vaduz-based company, invoice CHF 5,000 + CHF 405 MWST.
**Expected output:** Treated as DOMESTIC purchase. Ziffer 400 += CHF 405. No Bezugsteuer. No import procedure.

### Test 11 -- Below Bezugsteuer threshold [T1]
**Input:** Small Swiss business receives only one foreign service all year: EUR 3,000 (~CHF 2,900) from an Italian designer. No other foreign services.
**Expected output:** Below CHF 10,000 annual threshold. No Bezugsteuer. No Ziffer 382 entry. No input tax claim on this item.

### Test 12 -- Rate transition invoice [T1]
**Input:** Consulting services: 15 hours in December 2023 at CHF 200/hr = CHF 3,000, and 10 hours in January 2024 at CHF 200/hr = CHF 2,000. Single invoice issued January 2024.
**Expected output:** December 2023 portion: CHF 3,000 at 7.7% = CHF 231 tax. January 2024 portion: CHF 2,000 at 8.1% = CHF 162 tax. Invoice must split the two rates. Report in respective period returns.

---

## Step 15: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed Swiss tax adviser must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Swiss tax adviser. Document gap.
```

---

## Upcoming Rate Changes (Planned)

**Delayed VAT rate increase (originally planned for 2026, now expected 2028):**

| Rate | Current (from 1 Jan 2024) | Planned (expected 2028) |
|------|---------------------------|-------------------------|
| Standard | 8.1% | 8.8% |
| Reduced | 2.6% | 2.8% |
| Accommodation | 3.8% | 4.2% |

These increases are linked to AHV (pension) financing. The original target date of 1 January 2026 has been delayed. Monitor Federal Council announcements for the confirmed effective date.

**2025 exemption changes:**
- Menstrual hygiene products moved from standard rate (8.1%) to reduced rate (2.6%)
- New VAT exemptions for: outpatient/day clinics for medical treatments, care coordination services, private home care providers, travel agency services

---

## Contribution Notes

This skill covers Switzerland (and Liechtenstein by extension). It does NOT cover:

1. **Group taxation (Gruppenbesteuerung)** under Art. 13 MWSTG -- [T3], requires specialist analysis
2. **Margenbesteuerung** (margin scheme for second-hand goods, Art. 24a MWSTG) -- [T3]
3. **Real estate transactions** beyond basic option-to-tax -- [T3]
4. **Cross-border e-commerce** platform rules (Art. 20a MWSTG, effective 2025) -- [T3]
5. **Cantonal/municipal taxes** -- these are NOT VAT; entirely separate system
6. **Withholding tax (Verrechnungssteuer)** -- federal tax on dividends/interest, not related to MWST

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
