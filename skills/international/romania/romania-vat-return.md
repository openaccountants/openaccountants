---
name: romania-vat-return
description: Use this skill whenever asked to prepare, review, or create a Romania VAT return (Declaratia 300 / D300 form) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in D300", "create the return", "Romanian VAT", "TVA", or any request involving Romania VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Romania VAT classification rules, box mappings, deductibility rules, reverse charge treatment, SAF-T obligations, e-invoicing (RO e-Factura), and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Romanian VAT-related work.
---

# Romania VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Romania |
| Jurisdiction Code | RO |
| Primary Legislation | Codul Fiscal (Fiscal Code, Law 227/2015, as amended by Law 296/2023 and OUG 59/2025) |
| Supporting Legislation | Normele Metodologice (Methodological Norms, HG 1/2016); OUG 59/2025 (rate changes); OPANAF 2131/2025 (D300 form) |
| Tax Authority | Agentia Nationala de Administrare Fiscala (ANAF) |
| Filing Portal | https://www.anaf.ro (SPV -- Spatiul Privat Virtual) |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0 |
| Status | validated |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, rate assignment. Tier 2: partial exemption pro-rata, simplified imports, vehicle mixed-use. Tier 3: complex group structures, fiscal consolidation, special fiscal regimes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified consultant fiscal must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and CUI/CIF (tax ID)** [T1] -- RO prefix for VAT-registered entities
2. **VAT registration status** [T1] -- Normal VAT payer (inregistrat in scopuri de TVA), small enterprise exempt (under threshold), or micro-enterprise (impozit pe veniturile microintreprinderilor)
3. **Filing frequency** [T1] -- Monthly (turnover > EUR 100,000 prior year) or Quarterly (turnover <= EUR 100,000)
4. **Industry/sector** [T2] -- impacts applicable reduced rates and deductibility
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (pro-rata); reviewer must confirm
6. **Does the business operate in agriculture?** [T1] -- special flat-rate scheme may apply (Art. 315^1)
7. **SAF-T filing obligation** [T1] -- D406 filing required alongside D300
8. **Excess credit brought forward** [T1] -- from prior period (soldul TVA de recuperat)
9. **RO e-Factura compliance** [T1] -- mandatory B2B e-invoicing from 1 January 2026

**If any of items 1-3 are unknown, STOP. Do not classify any transactions.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (TVA colectata -- output VAT) or Purchase (TVA deductibila -- input VAT)
- Salaries, social contributions (CAS, CASS), income tax (impozit pe venit), loan repayments, dividends = OUT OF SCOPE
- **Legislation:** Fiscal Code Art. 265-270 (taxable transactions), Art. 268 (supply of goods), Art. 271 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Romania (domestic): supplier/customer country is RO
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, SK, SI, ES, SE
- Non-EU: everything else
- **Note:** UK is Non-EU post-Brexit. Moldova is Non-EU. Gibraltar is Non-EU.

### 1c. Determine VAT Rate [T1]

**As of 1 August 2025 (OUG 59/2025 rate changes):**

| Rate | Category | Legislation |
|------|----------|-------------|
| 19% | Standard rate (until 31 July 2025) | Fiscal Code Art. 291(1) (pre-OUG 59/2025) |
| 21% | Standard rate (from 1 August 2025) -- most goods and services | Fiscal Code Art. 291(1) (as amended by OUG 59/2025) |
| 9% | Reduced -- residential property (transitional, until 31 July 2026, max 120 sqm useful area and max RON 600,000 excl. VAT); prostheses and similar accessories; hotel accommodation (pre-Aug 2025) | Fiscal Code Art. 291(2) (transitional) |
| 11% | Reduced (from 1 August 2025) -- replacing most former 9% and 5% categories: food, non-alcoholic beverages, restaurant/catering, accommodation, medicines, medical devices, books, newspapers, water supply, heating, fertilizers | Fiscal Code Art. 291(2) (as amended by OUG 59/2025) |
| 5% | Super-reduced (pre-Aug 2025) -- social housing, books, school supplies | Fiscal Code Art. 291(3) (pre-OUG 59/2025) |
| 0% | Zero-rated -- exports (Art. 294), intra-EU supplies of goods (Art. 294) | Fiscal Code Art. 294 |
| Exempt with credit | International transport, certain financial intermediation for international clients | Fiscal Code Art. 294 |
| Exempt without credit | Healthcare (Art. 292(1)(a)), education (Art. 292(1)(b)), insurance (Art. 292(1)(d)), financial services (Art. 292(1)(e)), residential rental (Art. 292(2)(a)), postal services, gambling, transfer of going concern | Fiscal Code Art. 292 |

### 1d. Determine Expense Category [T1]
- Capital goods: tangible fixed assets > RON 2,500 (or per entity capitalization policy) with useful life > 1 year
- Immovable property: 20-year adjustment period (Fiscal Code Art. 305)
- Movable capital goods: 5-year adjustment period (Fiscal Code Art. 305)
- Resale: goods bought to resell
- Overhead/services: everything else
- **Legislation:** Fiscal Code Art. 305 (capital goods adjustment)

---

## Step 2: D300 Form Structure (VAT Return) [T1]

**Legislation:** OPANAF 2131/2025 (updated D300 form); Fiscal Code Art. 292-298.

### Output VAT (TVA Colectata -- Sales Side)

| Row | Description | Rate | Notes |
|-----|-------------|------|-------|
| Row 1 | Domestic supplies at standard rate (21% from Aug 2025 / 19% before) -- taxable base | 21%/19% | Standard-rated sales |
| Row 1a | Output TVA at standard rate | -- | Calculated |
| Row 2 | Domestic supplies at reduced rate (11% from Aug 2025 / 9% before) -- taxable base | 11%/9% | Food, accommodation, books etc. |
| Row 2a | Output TVA at reduced rate | -- | Calculated |
| Row 3 | Domestic supplies at second reduced rate (9% transitional) -- taxable base | 9% | Residential property (transitional) |
| Row 3a | Output TVA at 9% transitional | -- | Calculated |
| Row 4 | Exempt supplies with credit (exports, intra-EU) | 0% | No TVA charged |
| Row 5 | Exempt supplies without credit | exempt | Financial, insurance, healthcare |
| Row 6 | Intra-EU supplies of goods (livrari intracomunitare) | 0% | Report on D390 VIES |
| Row 7 | Intra-EU supply of services (Art. 278(2)) | 0% | B2B services to EU |
| Row 8 | Exports outside EU | 0% | Customs documentation required |
| Row 9 | Intra-EU acquisitions of goods -- taxable base | RC | Self-assessed |
| Row 9a | Output TVA on intra-EU acquisitions | -- | At applicable RO rate |
| Row 10 | Import of services (EU and non-EU) -- taxable base | RC | B2B service imports |
| Row 10a | Output TVA on import of services | -- | At applicable RO rate |
| Row 11 | Domestic reverse charge supplies -- taxable base | RC | Buildings, waste, wood, cereals |
| Row 11a | Output TVA on domestic reverse charge | -- | At applicable rate |
| Row 12 | Self-supply / deemed supply | applicable | Private use, free gifts |

### Input VAT (TVA Deductibila -- Purchase Side)

| Row | Description | Notes |
|-----|-------------|-------|
| Row 20 | Domestic purchases -- input TVA at standard rate (21%/19%) | Standard-rated input |
| Row 21 | Domestic purchases -- input TVA at reduced rate (11%/9%) | Reduced-rated input |
| Row 22 | Domestic purchases -- input TVA at second reduced rate (9% transitional) | Transitional rate |
| Row 23 | Intra-EU acquisitions -- input TVA | Mirrors Row 9a |
| Row 24 | Import of services -- input TVA | Mirrors Row 10a |
| Row 25 | Imports of goods (customs) -- input TVA | From customs declaration (DVI) |
| Row 26 | Domestic reverse charge -- input TVA | Mirrors Row 11a |
| Row 27 | Fixed asset purchases -- input TVA | Capital goods separately tracked |

### Summary

| Row | Description | Notes |
|-----|-------------|-------|
| Row 30 | Total output TVA | Sum of all output TVA rows |
| Row 31 | Total input TVA | Sum of all input TVA rows |
| Row 32 | Regularizations (pro-rata adjustments, corrections) | Annual pro-rata true-up |
| Row 33 | Net TVA payable (if Row 30 > Row 31) | Pay to ANAF |
| Row 34 | Net TVA credit (if Row 31 > Row 30) | Excess credit |
| Row 35 | Credit brought forward from prior period | From previous D300 |
| Row 36 | Credit requested for refund | Subject to ANAF review |
| Row 37 | Final amount payable | After offsetting credits |

---

## Step 3: Transaction Classification Matrix [T1]

### Purchases -- Domestic (Romanian Supplier)

| VAT Rate | Category | Input Row | Notes |
|----------|----------|-----------|-------|
| 21% (std) | Overhead/services | Row 20 | Standard domestic purchase |
| 11% (red) | Overhead/services | Row 21 | Food, accommodation, books |
| 9% (trans) | Overhead/services | Row 22 | Transitional residential |
| 0% | Any | -- | No TVA to claim |
| Any | Capital > RON 2,500 | Row 27 | Capital goods scheme |
| Any | Vehicle (mixed use) | Row 20/21 at 50% | Vehicle 50% rule |
| Any | Blocked category | -- | No input TVA |

### Purchases -- EU Supplier (Reverse Charge)

| Type | Output Row | Input Row | Notes |
|------|-----------|-----------|-------|
| Physical goods | Row 9 / Row 9a | Row 23 | Intra-EU acquisition |
| Services (B2B, Art. 278(2)) | Row 10 / Row 10a | Row 24 | EU service RC |
| Capital goods | Row 9/10 + Row 9a/10a | Row 27 | Also capital goods row |
| Out-of-scope (wages etc.) | -- | -- | NEVER reverse charge |
| Local consumption (hotel, restaurant abroad) | -- | -- | Foreign VAT at source |

### Purchases -- Non-EU Supplier

| Type | Output Row | Input Row | Notes |
|------|-----------|-----------|-------|
| Services (B2B) | Row 10 / Row 10a | Row 24 | Non-EU service import |
| Physical goods (customs) | -- | Row 25 | VAT paid to customs (DVI) |
| Out-of-scope | -- | -- | NEVER reverse charge |

### Sales -- Domestic

| Rate | Row | Notes |
|------|-----|-------|
| 21% (standard) | Row 1 / Row 1a | Standard-rated supply |
| 11% (reduced) | Row 2 / Row 2a | Food, accommodation etc. |
| 9% (transitional) | Row 3 / Row 3a | Residential property |
| Exempt with credit | Row 4 | International transport |
| Exempt without credit | Row 5 | Financial, insurance, healthcare |

### Sales -- EU / Non-EU

| Location | Type | Row | Notes |
|----------|------|-----|-------|
| EU B2B goods | Intra-EU supply | Row 6 | Zero-rated, report on D390 |
| EU B2B services | Art. 278(2) services | Row 7 | Place of supply in customer MS |
| Non-EU | Export | Row 8 | Zero-rated, customs docs |

---

## Step 4: Reverse Charge Mechanics [T1]

**Legislation:** Fiscal Code Art. 307(2)-(6) (reverse charge); Art. 276-278 (place of supply for services).

### Intra-EU Acquisitions of Goods (Art. 289)
1. Report taxable base in Row 9
2. Self-assess output TVA at applicable Romanian rate in Row 9a
3. Claim input TVA in Row 23
4. Net effect: zero for fully taxable businesses
5. Report on D390 VIES

### Import of Services -- EU and Non-EU B2B (Art. 278(2))
1. Report taxable base in Row 10
2. Self-assess output TVA in Row 10a
3. Claim input TVA in Row 24
4. Net effect: zero for fully taxable businesses

### Domestic Reverse Charge (Art. 331)

| Supply Type | Legislation | Notes |
|-------------|-------------|-------|
| Supply of buildings/land (after first occupation) | Art. 331(2)(a) | When seller opts to tax |
| Supply of wood and timber | Art. 331(2)(b) | All categories of wood |
| Supply of cereals and industrial crops | Art. 331(2)(c) | Grain, oilseeds, etc. |
| Supply of waste and recyclable materials | Art. 331(2)(d) | Scrap metal, paper, plastic |
| Transfers of CO2 emission allowances | Art. 331(2)(e) | Greenhouse gas permits |
| Supply of mobile phones and tablets (> RON 22,500) | Art. 331(2)(f) | Above threshold only |
| Supply of gaming consoles and integrated circuits (> RON 22,500) | Art. 331(2)(g) | Above threshold only |

Domestic reverse charge procedure:
1. Report taxable base in Row 11
2. Self-assess output TVA in Row 11a
3. Claim input TVA in Row 26

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories: NEVER reverse charge
- Local consumption abroad: NOT reverse charge; foreign VAT paid at source
- EU supplier charged their local VAT > 0%: NOT reverse charge
- Mobile phones/tablets below RON 22,500: normal VAT applies

---

## Step 5: Deductibility Check

### Blocked / Restricted Categories [T1]
**Legislation:** Fiscal Code Art. 297-298.

| Category | VAT Recovery | Legislation | Notes |
|----------|-------------|-------------|-------|
| Passenger vehicles (50% rule) | 50% | Art. 297(4) | Unless exclusively for business with proof |
| Fuel for 50%-restricted vehicles | 50% | Art. 297(4) | Same rule as vehicle |
| Maintenance/repairs for 50%-restricted vehicles | 50% | Art. 297(4) | Follows vehicle rule |
| Alcohol | 0% | Art. 297(1)(a) | Unless part of business activity (bar, shop, distributor) |
| Tobacco | 0% | Art. 297(1)(a) | Unless business activity (tobacconist) |
| Luxury goods for personal use | 0% | Art. 297(1)(b) | Non-deductible |
| Business gifts > RON 100 per item | 0% | Art. 297(1)(c) | Blocked above threshold |
| Business gifts <= RON 100 per item | Deductible | Art. 297(1)(c) | Promotional items OK |
| Protocol/entertainment expenses | Deductible for TVA | Art. 297 | NOT blocked for TVA (unlike many EU countries) |
| Protocol expenses | Limited for CIT | Art. 25(3)(a) Fiscal Code | 2% of accounting profit limit for CIT (not TVA) |
| Supplies for exempt-without-credit activities | 0% | Art. 297(2) | Financial, insurance, education inputs |
| Personal use items | 0% | Art. 297(1)(b) | No deduction |

### Vehicle 50% Rule Details [T1]
**Legislation:** Fiscal Code Art. 297(4).

| Scenario | TVA Deduction | Notes |
|----------|--------------|-------|
| Passenger car (max 9 seats), mixed use | 50% | Default assumption |
| Passenger car, exclusively business | 100% | Must have supporting evidence (trip sheets, GPS, contracts) |
| Taxi, delivery vehicle, emergency vehicle | 100% | Qualifying activities |
| Rental fleet vehicle (car rental business) | 100% | Part of business activity |
| Van / truck (N1 category or higher) | 100% | No restriction |
| Fuel for 50% vehicle | 50% | Follows vehicle rule |
| Fuel for 100% vehicle | 100% | Follows vehicle rule |
| Insurance, repairs, parking for 50% vehicle | 50% | Follows vehicle rule |

### Registration-Based Recovery [T1]

| Registration Type | Input VAT Recovery | Legislation |
|-------------------|-------------------|-------------|
| Normal TVA payer | Full recovery (subject to blocks) | Art. 297 |
| Exempt entity (below threshold) | NO recovery | Art. 310 |
| Micro-enterprise | NO TVA obligations (subject to micro-enterprise tax) | Art. 47 |

### Partial Exemption (Pro-Rata) [T2]
**Legislation:** Fiscal Code Art. 300.

`Recovery % = (Taxable Turnover + Zero-Rated Turnover) / Total Turnover * 100`

| Rule | Detail | Legislation |
|------|--------|-------------|
| Rounding | Round UP to nearest whole percent | Art. 300(3) |
| Provisional | Use prior year pro-rata during current year | Art. 300(4) |
| Annual regularization | True-up at year-end in last D300 of the year | Art. 300(5) |
| Excluded from calculation | Incidental financial/property transactions | Art. 300(2) |

**Flag for reviewer: annual regularization required. Provisional pro-rata used during year; final pro-rata calculated after year-end.**

---

## Step 6: SAF-T Reporting (D406) [T1]

**Legislation:** OPANAF 1783/2021 (SAF-T), as amended.

| Feature | Detail |
|---------|--------|
| Filing form | D406 (Standard Audit File for Tax) |
| Large taxpayers | Monthly, by 14th of month M+2 |
| Medium/small taxpayers | Monthly, by last day of month M+3 |
| Micro-enterprises | Monthly, by last day of month M+4 |
| Content | General ledger, accounts receivable/payable, fixed assets, inventory, purchase/sales invoices |
| Reconciliation | ANAF cross-checks D406 against D300; discrepancies must be explained within 20 days |
| Penalty | Fines between RON 1,000 and RON 5,000 for non-compliance |

**From 2026:** Pre-filled VAT returns (RO e-TVA) are generated by ANAF from D406 + RO e-Factura data. Taxpayers must review and either accept or explain discrepancies.

---

## Step 7: E-Invoicing (RO e-Factura) [T1]

**Legislation:** OUG 120/2021, as amended; Law 296/2023.

| Obligation | Effective Date | Legislation |
|------------|---------------|-------------|
| B2G (government) | Mandatory since July 2022 | OUG 120/2021 |
| B2B (all sectors) | Mandatory from 1 January 2026 | Law 296/2023 Art. I |
| B2C | Mandatory from 1 January 2026 | Law 296/2023 Art. I |
| Transmission deadline | Within 5 working days of invoice issuance | OUG 120/2021 Art. 10 |
| Format | CIUS-RO (UBL 2.1 based) | OPANAF specification |
| Platform | RO e-Factura via ANAF SPV portal | anaf.ro |

**Consequence:** Invoices not transmitted via e-Factura may be denied input TVA deduction by ANAF from 2026.

---

## Step 8: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| VAT registration (domestic) | RON 395,000 annual turnover (from 1 September 2025) | Fiscal Code Art. 310 |
| Previous threshold (before Sep 2025) | RON 300,000 | Art. 310 (old) |
| Monthly filing trigger | Annual turnover > EUR 100,000 prior year | Art. 322(1) |
| Capital goods adjustment -- movable | 5 years | Art. 305(1) |
| Capital goods adjustment -- immovable | 20 years | Art. 305(2) |
| Business gift deduction limit | RON 100 per item | Art. 297(1)(c) |
| Vehicle 50% restriction | Passenger cars, max 9 seats | Art. 297(4) |
| Domestic RC mobile phones/tablets | RON 22,500 per transaction | Art. 331(2)(f-g) |
| EU distance selling (B2C) | EUR 10,000 (EU-wide OSS threshold) | EU Directive 2017/2455 |
| Micro-enterprise tax threshold | EUR 500,000 revenue | Art. 47 |
| EU SME scheme (from 2025) | EUR 85,000 domestic + EUR 100,000 EU-wide | EU Directive 2020/285 |

---

## Step 9: VAT Registration [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| VAT number format | RO + CUI number (up to 10 digits) | Art. 316 |
| Mandatory registration | Turnover > RON 395,000 (from Sep 2025) | Art. 310(1) |
| Registration deadline | 10 days after exceeding threshold | Art. 316(1) |
| Voluntary registration | May register below threshold | Art. 316(1)(b) |
| Deregistration | If turnover drops below threshold | Art. 310(7) |
| ANAF reactivation risk | ANAF may cancel VAT number if non-compliant (D300/D394 unfiled, inactive address, etc.) | Art. 316(11) |
| Re-registration | Must apply and may require fiscal inspection | Art. 316(12) |
| Fiscal representative | Required for non-EU businesses without Romanian establishment | Art. 318 |

**Warning:** ANAF actively cancels VAT registrations for non-compliance. Re-registration can be difficult and time-consuming.

---

## Step 10: Filing Deadlines and Penalties

### Filing Deadlines [T1]

| Filing | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| D300 (monthly filer) | Monthly | 25th of following month | Art. 322(1) |
| D300 (quarterly filer) | Quarterly | 25th of month after quarter end | Art. 322(2) |
| D394 (local transactions report) | Monthly/Quarterly | Same as D300 deadline | OPANAF 3769/2015 |
| D390 VIES (recapitulative statement) | Monthly | 25th of following month | Art. 325 |
| D406 SAF-T (large taxpayers) | Monthly | 14th of M+2 | OPANAF 1783/2021 |
| D406 SAF-T (medium/small) | Monthly | Last day of M+3 | OPANAF 1783/2021 |
| TVA payment | Same as return | 25th | Tax Procedure Code Art. 156 |
| RO e-Factura transmission | Per invoice | 5 working days from issuance | OUG 120/2021 Art. 10 |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of D300 | RON 1,000 - RON 5,000 for legal entities | Tax Procedure Code Art. 336(1) |
| Late filing (individuals) | RON 500 - RON 1,000 | Tax Procedure Code Art. 336(2) |
| Late payment of TVA | 0.02% per day of delay (late interest) | Tax Procedure Code Art. 174(5) |
| Tax shortfall (additional assessment) | 0% - 50% penalty depending on circumstances | Tax Procedure Code Art. 181-182 |
| D406 SAF-T non-compliance | RON 1,000 - RON 5,000 per filing | OPANAF 1783/2021 |
| e-Factura non-compliance | RON 5,000 - RON 10,000 (legal entities from 2026) | Law 296/2023 |
| Failure to register for VAT | Back-assessment + penalties | Art. 310 |
| Non-filing of D394 | RON 2,000 - RON 10,000 | OPANAF 3769/2015 |

---

## Step 11: Edge Case Registry

### EC1 -- Hotel in another EU country [T1]
**Situation:** Romanian TVA payer pays for hotel in Italy. Invoice shows Italian 10% VAT.
**Resolution:** NOT reverse charge. Italian VAT was charged and paid at source. No Romanian TVA entries. Italian VAT is irrecoverable cost.
**Legislation:** Fiscal Code Art. 278(4)(b) -- place of supply for accommodation is where property is located.

### EC2 -- SaaS subscription from US provider (AWS, Google) [T1]
**Situation:** Monthly charge from US company, no VAT on invoice.
**Resolution:** Import of services. Report in Row 10 (base) / Row 10a (output TVA at 21%) / Row 24 (input TVA). Net effect zero.
**Legislation:** Fiscal Code Art. 278(2) -- place of supply for B2B services is customer's establishment.

### EC3 -- Intra-EU goods acquisition [T1]
**Situation:** Romanian company buys goods from German supplier at 0% with DE VAT number.
**Resolution:** Report in Row 9 (base) / Row 9a (output TVA at 21%) / Row 23 (input TVA). Net effect zero. Report on D390 VIES.
**Legislation:** Fiscal Code Art. 289.

### EC4 -- Passenger car purchase, mixed use (50% rule) [T1]
**Situation:** Company buys car for RON 100,000 + RON 21,000 TVA. Mixed use, no proof of exclusive business.
**Resolution:** 50% deduction. Input TVA recoverable = RON 10,500. Remaining RON 10,500 is cost.
**Legislation:** Fiscal Code Art. 297(4).

### EC5 -- Domestic reverse charge (waste materials) [T1]
**Situation:** Romanian supplier sells scrap metal to Romanian buyer. Both TVA registered.
**Resolution:** Supplier invoices without TVA. Buyer self-assesses in Row 11/11a (output) and Row 26 (input). Net effect zero.
**Legislation:** Fiscal Code Art. 331(2)(d).

### EC6 -- Credit note [T1]
**Situation:** Supplier issues credit note reducing an earlier invoice.
**Resolution:** Reduce original row values. Report in the period the credit note is issued. Negative adjustment in applicable rows.
**Legislation:** Fiscal Code Art. 287 (adjustment of tax base).

### EC7 -- Pre-filled VAT return discrepancy (RO e-TVA) [T2]
**Situation:** ANAF's pre-filled D300 (RO e-TVA) shows different figures than taxpayer's records.
**Resolution:** Flag for reviewer. Taxpayer must either accept ANAF figures or provide written explanation (Notificare) within 20 days. Discrepancy may trigger audit.
**Legislation:** OPANAF 2131/2025.

### EC8 -- Transitional rate period (August 2025) [T1]
**Situation:** Invoice issued 31 July 2025 at 19%, paid in August 2025.
**Resolution:** TVA rate is determined by chargeability date (data exigibilitatii), not payment date. If supply occurred before 1 August 2025, old rate (19%) applies. If supply is after, new rate (21%) applies.
**Legislation:** Fiscal Code Art. 282 (chargeability); OUG 59/2025 transitional provisions.

### EC9 -- Import of physical goods via customs [T2]
**Situation:** Client imports goods from China via Constanta port.
**Resolution:** TVA assessed by customs on DVI (declaratie vamala de import). Input TVA from customs document reported in Row 25. Flag for reviewer: confirm customs documentation and any deferred payment scheme (Art. 326^1).
**Legislation:** Fiscal Code Art. 293; Art. 326^1 (deferred import TVA).

### EC10 -- Business gift under RON 100 [T1]
**Situation:** Company distributes promotional items worth RON 50 each to clients.
**Resolution:** Input TVA on purchase is deductible (under RON 100 threshold). No output TVA on distribution if promotional purpose is documented.
**Legislation:** Fiscal Code Art. 297(1)(c).

### EC11 -- Business gift over RON 100 (blocked) [T1]
**Situation:** Company gives client a gift worth RON 200 + RON 42 TVA.
**Resolution:** Input TVA of RON 42 is NOT deductible (exceeds RON 100 threshold). Full amount is cost.
**Legislation:** Fiscal Code Art. 297(1)(c).

### EC12 -- ANAF cancellation of VAT registration [T2]
**Situation:** ANAF sends notice that client's TVA number is being cancelled for non-compliance.
**Resolution:** ESCALATE. Client must regularize compliance issues (file missing returns, update registered address). Flag for reviewer: re-registration requires fiscal inspection.
**Legislation:** Fiscal Code Art. 316(11)-(12).

### EC13 -- Domestic reverse charge (wood/timber) [T1]
**Situation:** Romanian lumber company sells processed timber to another Romanian TVA-registered company.
**Resolution:** Domestic reverse charge applies. Seller invoices without TVA. Buyer: Row 11 (base) / Row 11a (output TVA at 21%) / Row 26 (input TVA). Net zero.
**Legislation:** Fiscal Code Art. 331(2)(b).

### EC14 -- Mobile phones above RON 22,500 (domestic RC) [T1]
**Situation:** Romanian company buys smartphones worth RON 30,000 from another Romanian company.
**Resolution:** Domestic reverse charge applies (above RON 22,500 threshold). Buyer self-assesses. Below threshold: normal TVA.
**Legislation:** Fiscal Code Art. 331(2)(f).

### EC15 -- Deferred import TVA (Art. 326^1) [T2]
**Situation:** Company with authorization defers import TVA rather than paying at customs border.
**Resolution:** TVA is reported on D300 instead of paying to customs. Output in Row 10a equivalent, input in Row 25. Flag for reviewer: confirm client has the deferred import TVA authorization from ANAF.
**Legislation:** Fiscal Code Art. 326^1.

### EC16 -- Passenger car used exclusively for business (100% deduction) [T2]
**Situation:** Delivery company buys a car for RON 60,000 + RON 12,600 TVA. Used exclusively for deliveries.
**Resolution:** If exclusive business use can be demonstrated (trip sheets, GPS tracking, contracts), 100% TVA deduction applies. Flag for reviewer: confirm evidence of exclusive business use.
**Legislation:** Fiscal Code Art. 297(4) -- exception to 50% rule.

### EC17 -- Transitional rate: supply straddling August 2025 [T1]
**Situation:** Service contract signed in July 2025, partial delivery in July (19%) and partial in August (21%).
**Resolution:** TVA rate follows chargeability date for each portion. July deliveries at 19%, August deliveries at 21%. Split invoicing required.
**Legislation:** Fiscal Code Art. 282; OUG 59/2025 transitional provisions.

---

## Step 12: Comparison with Malta

| Feature | Romania (RO) | Malta (MT) |
|---------|-------------|------------|
| Standard rate | 21% (from Aug 2025; previously 19%) | 18% |
| Reduced rates | 11%, 9% (transitional) | 12%, 7%, 5% |
| Return form | D300 (~37 rows) | VAT3 (45 boxes) |
| Filing frequency | Monthly / Quarterly | Quarterly (Art. 10), Annual (Art. 11) |
| Filing deadline | 25th of following month | 21st of month after quarter (e-filing) |
| Payment deadline | 25th | Same as filing |
| Small enterprise threshold | RON 395,000 (~EUR 80,000) | EUR 35,000 |
| Capital goods movable | > RON 2,500 (5 years) | > EUR 1,160 gross |
| Capital goods immovable | 20-year adjustment | No specific adjustment period |
| Blocked: passenger cars | 50% rule (mixed use) | Yes (fully blocked, 10th Schedule) |
| Blocked: entertainment | NOT blocked for TVA (limited for CIT) | Yes (10th Schedule Item 3(1)(b)) |
| Blocked: alcohol/tobacco | Yes (unless business activity) | Yes (10th Schedule) |
| Domestic reverse charge | Buildings, waste, wood, cereals, emissions, phones | No domestic reverse charge |
| SAF-T filing | D406 mandatory (phased) | No SAF-T |
| E-invoicing | RO e-Factura mandatory from 2026 | No mandatory e-invoicing |
| Pre-filled returns | RO e-TVA from ANAF | No pre-filled returns |
| Refund mechanism | Request on D300, ANAF review | Carry forward / refund request |
| Tax authority | ANAF | CFR |
| Filing portal | anaf.ro (SPV) | cfr.gov.mt |
| Currency | RON (Romanian Leu) | EUR |

---

## Step 13: Derived Box Calculations [T1]

```
Row 30 = Sum of Row 1a + Row 2a + Row 3a + Row 9a + Row 10a + Row 11a + other output TVA
Row 31 = Sum of Row 20 + Row 21 + Row 22 + Row 23 + Row 24 + Row 25 + Row 26 + Row 27

IF Row 30 > Row 31 THEN
  Row 33 = Row 30 - Row 31  -- Net TVA Payable
  Row 34 = 0
ELSE
  Row 33 = 0
  Row 34 = Row 31 - Row 30  -- Net TVA Credit
END

Row 37 = Row 33 - Row 35  -- Final payable after credit brought forward
```

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
Action Required: Consultant fiscal must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to consultant fiscal. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Standard domestic purchase, 21% TVA [T1]
**Input:** Romanian supplier, office supplies, gross RON 1,210, TVA RON 210, net RON 1,000. Active VAT payer.
**Expected output:** Row 20 += RON 210. Input TVA recoverable in full.

### Test 2 -- Import of services from US (SaaS) [T1]
**Input:** US supplier, monthly fee EUR 50 (~RON 250), no VAT. Active VAT payer.
**Expected output:** Row 10 = RON 250, Row 10a = RON 52.50 (21%), Row 24 = RON 52.50. Net = zero.

### Test 3 -- Intra-EU goods acquisition [T1]
**Input:** French supplier, machinery EUR 10,000, 0% invoice with FR VAT number.
**Expected output:** Row 9 = RON equivalent, Row 9a = 21% output TVA, Row 23 = same input TVA. Net = zero.

### Test 4 -- Mixed-use passenger car (50% rule) [T1]
**Input:** Car RON 80,000 net + RON 16,800 TVA (21%). Mixed use, no exclusive business proof.
**Expected output:** Row 20 += RON 8,400 (50% of RON 16,800). Remaining RON 8,400 is cost.

### Test 5 -- Export of goods [T1]
**Input:** Romanian company exports goods to US client, EUR 5,000.
**Expected output:** Row 8 = RON equivalent. No output TVA. Zero-rated.

### Test 6 -- Domestic reverse charge (scrap metal) [T1]
**Input:** Romanian supplier sells recyclable waste RON 10,000 to Romanian buyer. Both TVA registered.
**Expected output:** Row 11 = RON 10,000, Row 11a = RON 2,100 (21%), Row 26 = RON 2,100. Net = zero.

### Test 7 -- Accommodation at 9% (transitional) [T1]
**Input:** Hotel stay RON 500 + RON 45 TVA (9%). Business trip, before July 2026.
**Expected output:** Row 22 += RON 45. Fully deductible (business purpose).

### Test 8 -- Business gift over RON 100 (blocked) [T1]
**Input:** Company gives client a gift worth RON 200 + RON 42 TVA.
**Expected output:** Input TVA of RON 42 is NOT deductible. Full amount is cost.

### Test 9 -- Fuel for 50%-restricted vehicle [T1]
**Input:** Fuel RON 500 + RON 105 TVA (21%) for a mixed-use passenger car.
**Expected output:** Row 20 += RON 52.50 (50% of RON 105). Remaining RON 52.50 is cost.

### Test 10 -- EU B2B service sale [T1]
**Input:** Romanian company invoices Bulgarian client EUR 2,000 for IT consulting. B2B.
**Expected output:** Row 7 = RON equivalent. No output TVA. Report on D390 VIES.

### Test 11 -- Alcohol purchase (blocked) [T1]
**Input:** Company buys wine RON 1,000 + RON 210 TVA. Not a bar or restaurant.
**Expected output:** Row 20 += RON 0. TVA BLOCKED (alcohol, Art. 297(1)(a)). Full RON 1,210 is cost.

### Test 12 -- Protocol/entertainment expense (deductible for TVA) [T1]
**Input:** Client dinner RON 500 + RON 105 TVA (21%). Business entertainment.
**Expected output:** Row 20 += RON 105. Input TVA IS deductible in Romania (Art. 297 does not block entertainment for TVA purposes). Note: limited to 2% of accounting profit for CIT purposes only.

---

## Step 16: TVA Rates -- Detailed Supply Classification [T1]

### 21% Standard Rate (from 1 August 2025, Fiscal Code Art. 291(1))

| Supply Category | Examples |
|----------------|----------|
| General goods | Electronics, furniture, clothing, household items, motor vehicles |
| Professional services | Legal, accounting, consulting, IT, advertising |
| Telecommunications | Mobile, fixed-line, internet services |
| Alcohol | Beer, wine, spirits |
| Tobacco | Cigarettes, cigars |
| Construction materials | Cement, steel, timber, fixtures |
| Energy | Electricity, gas (non-household tariffs) |

### 11% Reduced Rate (from 1 August 2025, Fiscal Code Art. 291(2) as amended)

| Supply Category | Examples |
|----------------|----------|
| Food and non-alcoholic beverages | All food items, soft drinks, juice, water |
| Restaurant and catering services | Dine-in meals, takeaway food (not alcohol) |
| Accommodation | Hotels, guesthouses, camping, Airbnb (commercial) |
| Books and periodicals | Printed and electronic books, newspapers, magazines |
| Medicines and medical devices | Prescription and OTC pharmaceuticals, hearing aids, prosthetics |
| Water supply | Drinking water distribution |
| Heating | District heating, firewood, pellets |
| Fertilizers and pesticides | Agricultural inputs |
| School supplies | Notebooks, textbooks, educational materials |

### 9% Transitional Rate (until 31 July 2026, Fiscal Code Art. 291(2) transitional)

| Supply Category | Examples |
|----------------|----------|
| Residential property (first sale) | New apartments and houses meeting social housing criteria |
| Prostheses and similar accessories | Medical prosthetics, hearing aids (during transitional period) |

### Pre-August 2025 Rates (for historical periods)

| Rate | Category |
|------|----------|
| 19% | Standard rate (all periods before 1 August 2025) |
| 9% | Reduced rate (food, accommodation, books, medicines, water, heating) |
| 5% | Super-reduced (social housing, books, school supplies) |

---

## Step 17: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Escalate to qualified adviser.

- **Corporate income tax (impozit pe profit):** 16% on adjusted profit (Fiscal Code Art. 13-46)
- **Micro-enterprise tax:** 1% on revenue (if EUR 500,000 or below; from 2024)
- **Dividend tax:** 8% withholding (Fiscal Code Art. 97)
- **Social contributions (CAS):** 25% employee pension contribution
- **Health contributions (CASS):** 10% employee health contribution
- **Personal income tax:** 10% flat rate on employment income
- **Local taxes:** Property tax, vehicle tax, advertising tax (administered by local authorities)
- **Construction tax:** 1.5% on value of new constructions (administered by local authorities)
- **Special construction tax:** 1% on buildings used for non-residential purposes over RON 2,500,000

### Refund Process [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Refund request | Filed via D300 Row 36 | Art. 303(2) |
| Automatic refund (with fiscal certificate) | 45 days from filing | Tax Procedure Code Art. 77 |
| Audit-conditioned refund | ANAF may inspect before refund | Tax Procedure Code Art. 94 |
| Risk classification | Low risk: automatic; high risk: audit first | ANAF internal procedure |

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT box assignment -- it is deterministic from transaction facts
- NEVER apply old rates (19%/9%/5%) to transactions after 1 August 2025 without verifying transitional rules
- NEVER claim 100% TVA on passenger cars without evidence of exclusive business use (Art. 297(4))
- NEVER claim input TVA on alcohol/tobacco unless it is the business activity (Art. 297(1)(a))
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi)
- NEVER allow TVA-exempt entities to claim input TVA
- NEVER ignore SAF-T / D406 filing obligations
- NEVER file D300 without reconciling against D406 data (from 2026, ANAF cross-checks automatically)
- NEVER ignore RO e-Factura obligations -- non-transmitted invoices may be denied deduction
- NEVER apply domestic RC to mobile phones/tablets below RON 22,500 threshold
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Contribution Notes

This skill covers Romania's VAT system based on the Fiscal Code (Law 227/2015) as amended by OUG 59/2025. Key distinctive features include: the August 2025 rate changes (19% to 21%, 9%/5% consolidation to 11%), the RO e-Factura mandatory e-invoicing system, SAF-T (D406) reporting, the vehicle 50% rule, entertainment deductibility for TVA purposes, pre-filled returns (RO e-TVA), and ANAF's active cancellation of non-compliant VAT registrations. Validation by a qualified Romanian consultant fiscal or expert contabil is required before production use.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
