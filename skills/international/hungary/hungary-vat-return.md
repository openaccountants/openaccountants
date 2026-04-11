---
name: hungary-vat-return
description: Use this skill whenever asked to prepare, review, or create a Hungary VAT return (form 2565 / AFA bevallas) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in 2565", "create the return", "Hungarian VAT", "AFA", or any request involving Hungary VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Hungary VAT classification rules, box mappings, deductibility rules, reverse charge treatment, NAV Online Invoice reporting, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Hungarian VAT-related work.
---

# Hungary VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Hungary |
| Jurisdiction Code | HU |
| Primary Legislation | 2007. evi CXXVII. torveny az altalanos forgalmi adorol (VAT Act, Act CXXVII of 2007, as amended) |
| Supporting Legislation | NAV Online Invoice Regulation (Gov. Decree 23/2014); KATA Act (Act XLVIII of 2022); Act CL of 2017 (Tax Procedure Code) |
| Tax Authority | Nemzeti Ado- es Vamhivatal (NAV -- National Tax and Customs Administration) |
| Filing Portal | https://nav.gov.hu (eBEV portal / ANYK system) |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0 |
| Status | validated |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, NAV online invoice obligations. Tier 2: partial exemption pro-rata, mixed-use adjustments, KATA applicability. Tier 3: complex group structures, fiscal representation, VAT grouping. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified adotanacsado must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and adoszam (tax number)** [T1] -- 11 digits (8-digit tax ID + 1-digit VAT code + 2-digit county code); HU prefix for EU VIES
2. **VAT registration status** [T1] -- Normal VAT payer, exempt small enterprise (alanyi mentes, turnover < HUF 18M for 2025, HUF 20M for 2026), or KATA subject
3. **Filing frequency** [T1] -- Monthly (default for first 3 years of registration and net VAT > HUF 1,000,000), Quarterly (net VAT HUF 250K-1M), or Annual (net VAT < HUF 250K, no intra-Community trading)
4. **Industry/sector** [T2] -- impacts applicable reduced rates and specific deductibility rules
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (aranyositas); reviewer must confirm
6. **Does the business use NAV Online Invoice system?** [T1] -- mandatory for all domestic invoices since July 2018
7. **Excess credit brought forward** [T1] -- from prior period (elozo idoszaki visszaigenyelni hagyott ado)
8. **Is the client a KATA taxpayer?** [T1] -- simplified lump-sum regime, limited VAT implications

**If any of items 1-3 are unknown, STOP. Do not classify any transactions.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (fizetendo ado -- output VAT) or Purchase (levonhato ado -- input VAT)
- Salaries, social contributions (TB, SZJA), personal income tax, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** VAT Act Sec. 2-8 (scope of tax), Sec. 9-10 (supply of goods), Sec. 13-16 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Hungary (domestic): supplier/customer country is HU
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else
- **Note:** UK is Non-EU post-Brexit. Gibraltar is Non-EU. Channel Islands are Non-EU.

### 1c. Determine VAT Rate [T1]

| Rate | Category | Legislation |
|------|----------|-------------|
| 27% | Standard rate -- most goods and services (highest in the EU) | VAT Act Sec. 82 |
| 18% | Reduced -- milk, dairy products, flour, bread and bakery, eggs, poultry meat; commercial accommodation services | VAT Act Sec. 82(2), Annex III |
| 5% | Super-reduced -- medicines, medical devices, books, newspapers, periodicals, district heating, live music/theatre performances, internet access, restaurant and catering services (from 2024), certain new residential property (max 150 sqm flat / 300 sqm house) | VAT Act Sec. 82(2), Annex III |
| 0% | Zero-rated -- exports outside EU (Sec. 98), intra-EU supplies of goods (Sec. 89) | VAT Act Sec. 89, 98-99 |
| Exempt with credit | International transport of goods, international passenger transport | VAT Act Sec. 93-97 |
| Exempt without credit | Financial services (Sec. 85-86), insurance (Sec. 85), healthcare (Sec. 85(1)(a)), education (Sec. 85(1)(b)), postal services, residential rental (Sec. 86(1)(j)), gambling | VAT Act Sec. 85-86 |

### 1d. Determine Expense Category [T1]
- Capital goods (targyi eszhoz): tangible assets with net acquisition cost > HUF 200,000 and useful life > 1 year
- Immovable property: 240-month (20-year) adjustment period (VAT Act Sec. 135)
- Movable capital goods: 60-month (5-year) adjustment period (VAT Act Sec. 135)
- Resale: goods bought to resell
- Overhead/services: everything else
- **Legislation:** VAT Act Sec. 135-136 (adjustment of deduction); Act C of 2000 (Accounting Act) Sec. 47-48

---

## Step 2: VAT Return Form Structure (Form 2565) [T1]

**Legislation:** VAT Act Sec. 184; NAV form 2565 (annual form number changes by year, e.g., 2465 for 2024, 2565 for 2025).

### Section A -- Output VAT (Fizetendo Ado)

| Line | Description | Rate | Notes |
|------|-------------|------|-------|
| 01 | Domestic supplies at 27% -- taxable base | 27% | Standard-rated domestic sales |
| 02 | Output VAT at 27% | -- | Calculated: Line 01 x 27% |
| 03 | Domestic supplies at 18% -- taxable base | 18% | Accommodation, specified foodstuffs |
| 04 | Output VAT at 18% | -- | Calculated: Line 03 x 18% |
| 05 | Domestic supplies at 5% -- taxable base | 5% | Medicines, books, restaurant, new housing |
| 06 | Output VAT at 5% | -- | Calculated: Line 05 x 5% |
| 07 | Intra-EU acquisition of goods -- taxable base | RC | Reverse charge self-assessment |
| 08 | Output VAT on intra-EU acquisition | -- | Self-assessed at applicable HU rate |
| 09 | Received services from EU (Sec. 37(1)) -- taxable base | RC | B2B services from EU |
| 10 | Output VAT on received EU services | -- | Self-assessed at applicable HU rate |
| 11 | Import of services from non-EU -- taxable base | RC | B2B services from non-EU |
| 12 | Output VAT on import of services | -- | Self-assessed at applicable HU rate |
| 13 | Domestic reverse charge received -- taxable base | RC | Construction, waste, grain etc. |
| 14 | Output VAT on domestic reverse charge | -- | Self-assessed at applicable rate |
| 15 | Import of goods (self-assessment, if applicable) -- base | RC | Customs self-assessment |
| 16 | Output VAT on import of goods | -- | Self-assessed |
| 17 | Exempt supplies with credit (exports, intra-EU supply of goods) | 0% | Zero-rated output |
| 18 | Exempt supplies without credit | exempt | Financial, insurance, healthcare etc. |
| 19 | Supply of new means of transport to EU non-taxable person | 0% | Special intra-EU rule |
| 20 | Self-supply / deemed supply (Sec. 11-12) | applicable | Private use, free gifts |

### Section B -- Input VAT (Levonhato Ado)

| Line | Description | Notes |
|------|-------------|-------|
| 30 | Input VAT on domestic purchases | All domestic input at all rates |
| 31 | Input VAT on intra-EU acquisitions of goods | Mirrors Line 08 (if deductible) |
| 32 | Input VAT on EU services received | Mirrors Line 10 |
| 33 | Input VAT on non-EU services received | Mirrors Line 12 |
| 34 | Input VAT on domestic reverse charge | Mirrors Line 14 |
| 35 | Input VAT on imports of goods | From customs documents or self-assessment |
| 36 | Input VAT on fixed assets (targyi eszhoz) | Capital goods input VAT |
| 37 | Proportional deduction (aranyositas) adjustments | Sec. 123 partial exemption |
| 38 | Capital goods adjustment (Sec. 135-136) | Annual correction for capital goods |

### Section C -- Settlement

| Line | Description | Notes |
|------|-------------|-------|
| 50 | Total output VAT | Sum of Lines 02+04+06+08+10+12+14+16 |
| 51 | Total input VAT | Sum of Lines 30+31+32+33+34+35+36+37+38 |
| 52 | Net VAT payable (if Line 50 > Line 51) | Pay to NAV |
| 53 | Net VAT credit (if Line 51 > Line 50) | Excess credit |
| 54 | Credit brought forward from prior period | From previous return |
| 55 | Credit requested for refund | Minimum HUF 1,000 for refund |
| 56 | Final amount payable / carry forward | After offsetting credits |

---

## Step 3: Transaction Classification Matrix [T1]

### Purchases -- Domestic (Hungarian Supplier)

| VAT Rate | Category | Output Line | Input Line | Notes |
|----------|----------|-------------|------------|-------|
| 27% | Overhead/services | -- | 30 | Standard domestic purchase |
| 18% | Overhead/services | -- | 30 | Accommodation, specified food |
| 5% | Overhead/services | -- | 30 | Medicines, books, catering |
| 0% | Any | -- | -- | No entry (no VAT to claim) |
| 27% | Resale | -- | 30 | Goods for resale |
| Any | Capital > HUF 200,000 net | -- | 36 | Capital goods scheme applies |
| Any | Blocked category | -- | -- | No input VAT (Sec. 124-125) |

### Purchases -- EU Supplier (Reverse Charge)

| Type | Output Lines | Input Line | Notes |
|------|-------------|------------|-------|
| Physical goods | 07 / 08 | 31 | Intra-EU acquisition |
| Services (B2B, Sec. 37(1)) | 09 / 10 | 32 | EU service reverse charge |
| Capital goods | 07 / 08 or 09 / 10 | 36 | Also capital goods line |
| Out-of-scope (wages etc.) | -- | -- | NEVER reverse charge |
| Local consumption (hotel, restaurant abroad) | -- | -- | Foreign VAT at source, not RC |

### Purchases -- Non-EU Supplier (Reverse Charge)

| Type | Output Lines | Input Line | Notes |
|------|-------------|------------|-------|
| Services (B2B) | 11 / 12 | 33 | Non-EU service import |
| Physical goods (customs) | 15 / 16 | 35 | Import via customs declaration |
| Out-of-scope | -- | -- | NEVER reverse charge |

### Sales -- Domestic

| Rate | Line | Notes |
|------|------|-------|
| 27% | 01 (base), 02 (VAT) | Standard-rated supply |
| 18% | 03 (base), 04 (VAT) | Accommodation, specified food |
| 5% | 05 (base), 06 (VAT) | Medicines, books, restaurant, new housing |
| 0% (exempt with credit) | 17 | International transport |
| Exempt without credit | 18 | Financial, insurance, education, healthcare |

### Sales -- EU / Non-EU

| Location | Type | Line | Notes |
|----------|------|------|-------|
| EU B2B goods | Intra-EU supply | 17 | Zero-rated, report on Recapitulative Statement |
| EU B2B services | Sec. 37(1) services | 17 | Place of supply in customer MS |
| Non-EU | Export | 17 | Zero-rated export |

---

## Step 4: NAV Online Invoice System [T1]

**Legislation:** Gov. Decree 23/2014 (XI.3.); VAT Act Sec. 175/A-B.

### Mandatory Real-Time Reporting

ALL invoices issued by Hungarian VAT-registered taxpayers must be reported to NAV electronically in real time, regardless of:
- Invoice amount (no threshold since July 2020)
- Whether the buyer is VAT-registered or not (B2B and B2C)
- Whether the transaction is domestic, EU, or non-EU

### Reporting Deadlines

| Type | Deadline | Legislation |
|------|----------|-------------|
| Invoices with VAT >= HUF 100,000 | Immediately (real-time via API) | Gov. Decree 23/2014 Sec. 9 |
| Invoices with VAT < HUF 100,000 | Within 4 calendar days | Gov. Decree 23/2014 Sec. 10 |
| Invoices with zero VAT | Within 4 calendar days | Gov. Decree 23/2014 Sec. 10 |
| Credit notes / modifications | Same rules as original invoice | Gov. Decree 23/2014 Sec. 11 |
| Self-billing invoices | Same rules | Gov. Decree 23/2014 Sec. 10 |

### Key Rules [T1]
- Invoice must be reported BEFORE the VAT return filing deadline
- NAV may deny input VAT deduction if the invoice is not in its system (VAT Act Sec. 120(1))
- XML format based on NAV's Online Invoice schema (currently v3.0)
- Energy sector: mandatory full e-invoicing from July 2025 (Gov. Decree 2024)
- Penalty for non-reporting: up to HUF 500,000 per invoice (Tax Procedure Code Sec. 230)

---

## Step 5: Reverse Charge Mechanics [T1]

**Legislation:** VAT Act Sec. 139-142 (domestic RC), Sec. 91 (intra-EU), Sec. 47 (import of services).

### Intra-EU Acquisitions of Goods (Sec. 91)
1. Report taxable base in Line 07 and output VAT in Line 08
2. Claim input VAT in Line 31
3. Net effect: zero for fully taxable businesses
4. Report on Recapitulative Statement (A60)

### EU Services Received -- B2B (Sec. 37(1))
1. Report in Line 09 (base) / Line 10 (output VAT)
2. Claim in Line 32
3. Net effect: zero
4. Report on Recapitulative Statement (A60)

### Non-EU Services Received (Sec. 47)
1. Report in Line 11 (base) / Line 12 (output VAT)
2. Claim in Line 33
3. Net effect: zero

### Domestic Reverse Charge (Sec. 142)

| Supply Type | Legislation | Threshold |
|-------------|-------------|-----------|
| Waste and scrap (metals, paper, glass, plastic) | Sec. 142(1)(a), Annex 4 | No threshold |
| Construction and assembly services | Sec. 142(1)(b) | No threshold |
| Staff leasing for construction | Sec. 142(1)(c) | No threshold |
| Certain agricultural products (grain, oilseed, sunflower) | Sec. 142(8) | HUF 100,000 per transaction |
| Sale of immovable property (when seller opts to tax under Sec. 88) | Sec. 142(1)(e) | No threshold |
| Sale of new immovable property by non-established person | Sec. 142(1)(f) | No threshold |
| Greenhouse gas emission allowances | Sec. 142(1)(g) | No threshold |
| Steel products (semi-finished) | Sec. 142(1)(d) | No threshold |

Domestic reverse charge procedure:
1. Report in Line 13 (base) / Line 14 (output VAT)
2. Claim in Line 34
3. Net effect: zero

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories (wages, bank charges, dividends): NEVER reverse charge
- Local consumption abroad (hotel, restaurant, taxi, conference): NOT reverse charge; foreign VAT paid at source
- EU supplier charged their local VAT > 0%: NOT reverse charge; foreign VAT is part of expense
- Agricultural products below HUF 100,000 per transaction: normal VAT applies (not domestic RC)

---

## Step 6: Deductibility Check

### Blocked Categories (VAT Act Sec. 124-125) [T1]

| Category | VAT Recovery | Legislation | Notes |
|----------|-------------|-------------|-------|
| Passenger cars (purchase, lease, maintenance) | 0% | Sec. 124(1)(d) | Exception: taxi, driving school, car rental, vehicles > 9 seats |
| Motorcycles (purchase, lease, maintenance) | 0% | Sec. 124(1)(d) | Same exceptions as cars |
| Fuel for blocked vehicles (petrol, diesel, LPG) | 0% | Sec. 124(1)(d) | Follows vehicle rule |
| Parking for blocked vehicles | 0% | Sec. 124(1)(d) | Follows vehicle rule |
| Food and beverages (own consumption / staff meals) | 0% | Sec. 124(1)(a) | Exception: hospitality sector providing meals to guests [T2] |
| Entertainment and representation (client hospitality, gifts, events) | 0% | Sec. 124(1)(a) | Always blocked, no exceptions |
| Residential property (purchase and renovation) | 0% | Sec. 124(1)(c) | Exception: developer for taxable resale, taxable letting |
| Pleasure craft (yachts, sailboats) | 0% | Sec. 124(1)(d) | Exception: charter/rental business |
| Tobacco products | 0% | Sec. 124(1)(a) | Unless business activity (tobacconist) |
| Goods/services for exempt-without-credit activities | 0% | Sec. 120(2) | Financial services, insurance, education, healthcare inputs |
| Goods/services for non-business (personal) purposes | 0% | Sec. 120(1) | No deduction for private use |

### Important Exceptions [T2]
- Food/beverages provided to staff as part of employment benefits: partially deductible in certain conditions. Flag for reviewer.
- Vehicles used exclusively and demonstrably for business (with logbook compliant with NAV requirements): may claim deduction. Flag for reviewer to verify log compliance (VAT Act Sec. 124(4)).
- Hotel accommodation for business travel within Hungary: deductible at 18% rate if invoice properly issued.

### Registration-Based Recovery [T1]

| Registration Type | Input VAT Recovery | Legislation |
|-------------------|-------------------|-------------|
| Normal VAT payer | Full recovery (subject to blocks) | VAT Act Sec. 120 |
| Alanyi mentes (exempt small enterprise) | NO recovery | VAT Act Sec. 187 |
| KATA taxpayer (VAT-exempt) | NO recovery | KATA Act Sec. 4 |
| KATA taxpayer (VAT-registered) | Full recovery if registered | VAT Act Sec. 120 + KATA Act |

### Partial Exemption -- Aranyositas (Sec. 123) [T2]

**Legislation:** VAT Act Sec. 123.

If business makes both taxable and exempt-without-credit supplies:

`Recovery % = (Taxable Turnover / Total Turnover) * 100`

| Rule | Detail | Legislation |
|------|--------|-------------|
| Rounding | Round UP to nearest whole percent | Sec. 123(3) |
| De minimis | If >= 98%, treated as 100% | Sec. 123(4) |
| Provisional | Use prior year ratio during current year | Sec. 123(5) |
| Annual adjustment | True-up at year-end on annual return | Sec. 123(6) |
| Excluded from calculation | Incidental financial/property transactions | Sec. 123(2) |

**Flag for reviewer: provisional ratio used during year; annual adjustment required. Warranted accountant must confirm rate before filing.**

---

## Step 7: KATA (Small Taxpayer Lump-Sum Tax) [T2]

**Legislation:** Act XLVIII of 2022 on the Itemized Tax of Small-Taxpayer Enterprises.

| Feature | Detail |
|---------|--------|
| Eligibility | Sole proprietors and single-member private entrepreneurs |
| Revenue limit | HUF 18 million per year |
| Tax rate | HUF 50,000/month flat tax (covers income tax + social contributions) |
| VAT status | KATA subjects may be VAT-registered or exempt (alanyi mentes); if exempt, no VAT return required |
| Invoice restriction | Cannot issue invoices > HUF 3 million to a single partner per year |
| Related party limitation | Receipts from related parties are limited |
| Breach consequence | If revenue exceeds HUF 18M, must exit KATA and register for standard taxes |

**Note:** KATA is an income tax simplification. VAT obligations are separate -- a KATA subject who is also VAT-registered must file VAT returns normally.

---

## Step 8: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Small enterprise VAT exemption (alanyi mentes) | HUF 18,000,000 for 2025; HUF 20,000,000 for 2026; rising to HUF 24,000,000 by 2028 | VAT Act Sec. 188 |
| EU SME scheme (from 2025) | EUR 85,000 domestic + EUR 100,000 EU-wide | EU Directive 2020/285 |
| Monthly filing trigger | Net VAT liability > HUF 1,000,000 OR first 2 years of registration | VAT Act Sec. 184(2) |
| Quarterly filing | Net VAT between HUF 250,000 and HUF 1,000,000 | VAT Act Sec. 184(3) |
| Annual filing | Net VAT < HUF 250,000, no intra-Community trading | VAT Act Sec. 184(4) |
| NAV Online Invoice (real-time) | All invoices (no amount threshold for reporting) | Gov. Decree 23/2014 |
| NAV Online Invoice (immediate) | VAT >= HUF 100,000 per invoice | Gov. Decree 23/2014 Sec. 9 |
| Capital goods -- movable | > HUF 200,000 net (5-year adjustment) | VAT Act Sec. 135(1) |
| Capital goods -- immovable | Any value (20-year adjustment period) | VAT Act Sec. 135(2) |
| KATA revenue cap | HUF 18,000,000 | KATA Act Sec. 4 |
| Domestic RC agricultural threshold | HUF 100,000 per transaction | VAT Act Sec. 142(8) |
| EU distance selling (B2C) | EUR 10,000 (EU-wide OSS threshold) | EU Directive 2017/2455 |
| Refund minimum | HUF 1,000 | Tax Procedure Code Sec. 65 |

---

## Step 9: Filing Deadlines and Penalties

### Filing Deadlines [T1]

| Filing | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| Monthly VAT return | Monthly | 20th of following month | VAT Act Sec. 184(2) |
| Quarterly VAT return | Quarterly | 20th of month after quarter end | VAT Act Sec. 184(3) |
| Annual VAT return | Annual | 15 February of following year | VAT Act Sec. 184(4) |
| EU Recapitulative Statement (A60) | Monthly | 20th of following month | VAT Act Sec. 4/A |
| VAT payment | Same as return | 20th of following month/quarter | Tax Procedure Code Sec. 49 |
| NAV Online Invoice | Real-time | Within 4 days (or immediate for >= HUF 100K VAT) | Gov. Decree 23/2014 |
| Intrastat | Monthly | 15th of following month | KSH regulation |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of VAT return | Up to HUF 500,000 (self-assessment penalty) | Tax Procedure Code Sec. 220 |
| Late payment of VAT | Late interest at central bank base rate + 5% p.a. | Tax Procedure Code Sec. 208 |
| Tax shortfall (negligence) | 50% of shortfall amount | Tax Procedure Code Sec. 215(1) |
| Tax shortfall (fraud / concealment) | 200% of shortfall amount | Tax Procedure Code Sec. 215(2) |
| NAV Online Invoice non-reporting | Up to HUF 500,000 per invoice | Tax Procedure Code Sec. 230 |
| Repeated NAV non-reporting | Up to HUF 1,000,000 per invoice (doubled) | Tax Procedure Code Sec. 230 |
| Failure to register for VAT | Up to HUF 500,000 + back-assessment | Tax Procedure Code Sec. 221 |
| Recapitulative Statement late/missing | Up to HUF 500,000 | Tax Procedure Code Sec. 220 |

---

## Step 10: VAT Registration [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| VAT number format | HU + 8 digits (for VIES); full adoszam is 11 digits | VAT Act Sec. 173 |
| Mandatory registration | Anyone making taxable supplies in Hungary | VAT Act Sec. 173 |
| Small enterprise exemption | Turnover < HUF 18,000,000 for 2025; HUF 20,000,000 for 2026 (alanyi mentes) | VAT Act Sec. 188 |
| Voluntary registration | May register even below threshold | VAT Act Sec. 173 |
| Group registration | Related entities may form VAT group (Sec. 8) | VAT Act Sec. 8 |
| EU acquirer registration | If acquiring goods from EU above threshold | VAT Act Sec. 173 |
| Deregistration | If turnover stays below threshold for 2 consecutive years | VAT Act Sec. 189 |
| Fiscal representative | Required for non-EU businesses without Hungarian establishment | VAT Act Sec. 174 |

---

## Step 11: Edge Case Registry

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]
**Situation:** Hungarian VAT payer pays for hotel in Germany. Invoice shows German 7% VAT.
**Resolution:** NOT reverse charge. German VAT charged at source. No Hungarian VAT entries. German VAT is irrecoverable cost embedded in the expense.
**Legislation:** VAT Act Sec. 46 -- place of supply for accommodation is where the property is located.

### EC2 -- SaaS subscription from US provider (Google, AWS, Notion) [T1]
**Situation:** Monthly charge from US company, no VAT on invoice.
**Resolution:** Import of services. Report in Line 11 (base) / Line 12 (output VAT at 27%) / Line 33 (input VAT at 27%). Net effect zero for fully taxable business.
**Legislation:** VAT Act Sec. 37(1) and Sec. 47 -- place of supply is customer's establishment.

### EC3 -- Intra-EU goods acquisition [T1]
**Situation:** Hungarian company buys goods from Austrian supplier at 0% with AT VAT number.
**Resolution:** Report in Line 07 (base) / Line 08 (output VAT at 27%) / Line 31 (input VAT at 27%). Net zero. Report on Recapitulative Statement (A60).
**Legislation:** VAT Act Sec. 91 -- intra-EU acquisition is taxable in Hungary.

### EC4 -- Company car purchase (blocked) [T1]
**Situation:** Company buys passenger car for HUF 10,000,000 + HUF 2,700,000 VAT.
**Resolution:** Input VAT of HUF 2,700,000 is BLOCKED under Sec. 124(1)(d). No deduction. Full HUF 12,700,000 is cost. Exception only for taxis, driving schools, car rental businesses, vehicles with > 9 seats.
**Legislation:** VAT Act Sec. 124(1)(d).

### EC5 -- Client entertainment dinner [T1]
**Situation:** Business dinner with clients. HUF 80,000 + HUF 21,600 VAT (27%).
**Resolution:** Input VAT BLOCKED. Full HUF 101,600 is cost. Entertainment/representation is never deductible.
**Legislation:** VAT Act Sec. 124(1)(a).

### EC6 -- Domestic reverse charge (construction) [T1]
**Situation:** Hungarian subcontractor provides construction services to Hungarian VAT payer. HUF 5,000,000.
**Resolution:** Supplier invoices without VAT. Buyer: Line 13 (base HUF 5M) / Line 14 (output VAT HUF 1,350,000 at 27%) / Line 34 (input VAT HUF 1,350,000). Net zero.
**Legislation:** VAT Act Sec. 142(1)(b).

### EC7 -- EU B2B service sale (consulting) [T1]
**Situation:** Hungarian company provides consulting to Austrian client (B2B).
**Resolution:** Report in Line 17 (exempt with credit). No output VAT. Customer reverse charges in Austria. Report on Recapitulative Statement (A60).
**Legislation:** VAT Act Sec. 37(1) -- place of supply is customer's establishment.

### EC8 -- NAV Online Invoice not reported in time [T1]
**Situation:** Invoice issued but not reported to NAV Online Invoice system within 4-day deadline.
**Resolution:** Buyer's right to deduct input VAT may be denied by NAV. Penalty up to HUF 500,000 per invoice. Ensure all invoices are reported before VAT return filing.
**Legislation:** Gov. Decree 23/2014 Sec. 10; Tax Procedure Code Sec. 230.

### EC9 -- Exempt small enterprise exceeds threshold [T1]
**Situation:** Alanyi mentes business exceeds the applicable threshold (HUF 18,000,000 for 2025; HUF 20,000,000 for 2026).
**Resolution:** Must register as normal VAT payer from the transaction that caused the breach. Must charge VAT on ALL supplies from that point forward. Can claim input VAT from registration date. Prior period exempt income is not retrospectively taxed.
**Legislation:** VAT Act Sec. 189(1).

### EC10 -- Restaurant/catering at 5% (input VAT blocked) [T1]
**Situation:** Business pays for restaurant meal in Hungary. Invoice shows 5% VAT.
**Resolution:** Input VAT is BLOCKED (food and beverages for own consumption under Sec. 124(1)(a)). Despite the reduced rate, no deduction. Full amount is cost.
**Legislation:** VAT Act Sec. 124(1)(a).

### EC11 -- Agricultural products above HUF 100,000 [T1]
**Situation:** Hungarian farmer sells grain worth HUF 250,000 to a Hungarian VAT-registered buyer.
**Resolution:** Domestic reverse charge applies (Sec. 142(8)). Buyer self-assesses output VAT and claims input VAT. Seller invoices without VAT.
**Legislation:** VAT Act Sec. 142(8).

### EC12 -- Agricultural products below HUF 100,000 [T1]
**Situation:** Hungarian farmer sells grain worth HUF 80,000 to a Hungarian buyer.
**Resolution:** Domestic reverse charge does NOT apply (below HUF 100,000 threshold). Normal VAT applies. Seller charges VAT.
**Legislation:** VAT Act Sec. 142(8) -- threshold not met.

### EC13 -- Credit notes [T1]
**Situation:** Client receives a credit note from a supplier.
**Resolution:** Reverse the original entry. If original was in Line 30, credit note reduces Line 30 by the credit note VAT amount. Net figures reported.
**Legislation:** VAT Act Sec. 77-78 (correction of tax base).

### EC14 -- Import of physical goods via customs [T2]
**Situation:** Client imports goods from China through Budapest.
**Resolution:** VAT on physical goods imports is collected by customs (NAV customs division) at the border. Import VAT appears on the customs declaration (VAM import document). This is recoverable input VAT in Line 35 but must be entered from the customs document. Flag for reviewer: confirm client has the customs document and amount matches.
**Legislation:** VAT Act Sec. 93-95, Sec. 120.

### EC15 -- Fuel for business vehicle with logbook [T2]
**Situation:** Client purchases fuel for a delivery van with a properly maintained logbook proving 100% business use.
**Resolution:** If vehicle is not a passenger car (e.g., N1 category van), fuel VAT is fully deductible in Line 30. If vehicle is a passenger car but has a compliant logbook, flag for reviewer: VAT Act Sec. 124(4) exception may apply.
**Legislation:** VAT Act Sec. 124(1)(d) and Sec. 124(4).

### EC16 -- Mixed invoice from EU supplier (goods + services) [T1]
**Situation:** EU supplier invoice covers both physical goods and installation services.
**Resolution:** Split by line item. Physical goods go to Line 07/08/31. Services go to Line 09/10/32. If line items are not broken out, [T2] flag for reviewer to confirm split with client.
**Legislation:** VAT Act Sec. 91 (goods) and Sec. 37(1) (services).

### EC17 -- Emission allowance purchase (domestic reverse charge) [T1]
**Situation:** Hungarian company buys CO2 emission allowances from another Hungarian company.
**Resolution:** Domestic reverse charge applies. Buyer: Line 13 (base) / Line 14 (output VAT 27%) / Line 34 (input VAT). Net zero. Seller invoices without VAT.
**Legislation:** VAT Act Sec. 142(1)(g).

### EC18 -- New residential property sale at 5% [T2]
**Situation:** Developer sells a new flat (120 sqm) to a private buyer.
**Resolution:** 5% VAT applies if the property meets the size criteria (max 150 sqm for flats, max 300 sqm for houses) and it is the first sale after construction or substantial renovation. Flag for reviewer: confirm size, first occupation status, and that the developer is VAT registered.
**Legislation:** VAT Act Sec. 82(2), Annex III, Item 159/C.

---

## Step 12: Comparison with Malta

| Feature | Hungary (HU) | Malta (MT) |
|---------|--------------|------------|
| Standard rate | 27% (highest in EU) | 18% |
| Reduced rates | 18%, 5% | 12%, 7%, 5% |
| Return form | Form 2565 (56 lines) | VAT3 (45 boxes) |
| Filing frequency | Monthly / Quarterly / Annual | Quarterly (Art. 10), Annual (Art. 11) |
| Filing deadline | 20th of following month | 21st of month after quarter (e-filing) |
| Payment deadline | Same as filing | Same as filing |
| Small enterprise threshold | HUF 12,000,000 (~EUR 31,000) | EUR 35,000 |
| Capital goods movable | > HUF 200,000 net (5 years) | > EUR 1,160 gross (no adjustment) |
| Capital goods immovable | 20-year adjustment | No specific adjustment period |
| Blocked: passenger cars | Yes (purchase, lease, fuel, parking) | Yes (10th Schedule Item 3(1)(a)(iv-v)) |
| Blocked: entertainment | Yes (fully blocked) | Yes (10th Schedule Item 3(1)(b)) |
| Blocked: food/beverages | Yes (own consumption) | No (not specifically blocked) |
| Domestic reverse charge | Construction, waste, grain, emission allowances, steel | No domestic reverse charge |
| Online invoice reporting | NAV Online Invoice (real-time, all invoices) | No real-time invoice reporting |
| Partial exemption threshold | 98% = treated as 100% | No de minimis |
| Refund mechanism | Direct refund if credit on return | Carry forward / refund request |
| Tax authority | NAV (national) | CFR (Commissioner for Revenue) |
| Filing portal | eBEV / ANYK | cfr.gov.mt |
| Currency | HUF (Hungarian Forint) | EUR |

---

## Step 13: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Adotanacsado must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to adotanacsado. Document gap.
```

---

## Step 14: Test Suite

### Test 1 -- Standard domestic purchase, 27% VAT [T1]
**Input:** Hungarian supplier, office supplies, HUF 100,000 net + HUF 27,000 VAT. Normal VAT payer, no exempt activities.
**Expected output:** Line 30 += HUF 27,000. Fully deductible.

### Test 2 -- Import of services from US (SaaS) [T1]
**Input:** US supplier, monthly fee EUR 20 (~HUF 7,800), no VAT. Normal VAT payer.
**Expected output:** Line 11 = HUF 7,800, Line 12 = HUF 2,106 (27%), Line 33 = HUF 2,106. Net = zero.

### Test 3 -- Passenger car blocked [T1]
**Input:** Company buys passenger car HUF 8,000,000 + HUF 2,160,000 VAT. Mixed use, no logbook.
**Expected output:** Line 30 += HUF 0. VAT BLOCKED under Sec. 124(1)(d). Full HUF 10,160,000 is cost.

### Test 4 -- EU B2B service sale [T1]
**Input:** Hungarian company invoices Czech client EUR 1,000 for consulting. B2B.
**Expected output:** Line 17 = HUF equivalent. No output VAT. Report on Recapitulative Statement (A60).

### Test 5 -- Domestic reverse charge (construction) [T1]
**Input:** Hungarian subcontractor, construction work HUF 2,000,000. Both parties VAT payers.
**Expected output:** Buyer: Line 13 = HUF 2,000,000, Line 14 = HUF 540,000 (27%), Line 34 = HUF 540,000. Net = zero.

### Test 6 -- Entertainment (blocked) [T1]
**Input:** Client dinner HUF 50,000 + HUF 13,500 VAT (27%).
**Expected output:** Line 30 += HUF 0. VAT BLOCKED under Sec. 124(1)(a). Full HUF 63,500 is cost.

### Test 7 -- Intra-EU goods acquisition [T1]
**Input:** German supplier, goods EUR 3,000 at 0% with DE VAT number.
**Expected output:** Line 07 = HUF equivalent, Line 08 = HUF equivalent x 27% output VAT, Line 31 = same input VAT. Net = zero.

### Test 8 -- Alanyi mentes (exempt small enterprise) purchase [T1]
**Input:** Exempt small enterprise buys supplies HUF 200,000 + HUF 54,000 VAT.
**Expected output:** No input VAT recovery. Full HUF 254,000 is cost. No VAT return required.

### Test 9 -- Domestic reverse charge (agricultural products above HUF 100K) [T1]
**Input:** Hungarian farmer sells grain HUF 300,000 to VAT-registered buyer.
**Expected output:** Buyer: Line 13 = HUF 300,000, Line 14 = HUF 81,000 (27%), Line 34 = HUF 81,000. Net = zero.

### Test 10 -- Restaurant meal at 5% (blocked) [T1]
**Input:** Business lunch in Hungary. HUF 20,000 + HUF 1,000 VAT (5%). Own consumption.
**Expected output:** Line 30 += HUF 0. VAT BLOCKED (food/beverages own consumption). Full HUF 21,000 is cost.

### Test 11 -- Capital goods (movable, > HUF 200,000) [T1]
**Input:** Hungarian supplier, laptop HUF 400,000 net + HUF 108,000 VAT (27%). Normal VAT payer.
**Expected output:** Line 36 = HUF 108,000. Capital goods scheme applies (5-year adjustment).

### Test 12 -- EU hotel (local consumption, not reverse charge) [T1]
**Input:** Hungarian VAT payer pays for hotel in France EUR 200 including French VAT EUR 20.
**Expected output:** No VAT return entry. Expense is EUR 200 gross including irrecoverable French VAT. Not reverse charge.

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT box assignment -- it is deterministic from transaction facts
- NEVER claim input VAT on passenger cars, motorcycles, or their running costs (fuel, parking, maintenance) unless a proven exception applies (Sec. 124(1)(d))
- NEVER claim input VAT on food, beverages, or entertainment/representation (Sec. 124(1)(a))
- NEVER claim input VAT on residential property (purchase or renovation) unless for taxable activity (Sec. 124(1)(c))
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi)
- NEVER allow exempt small enterprises (alanyi mentes) to claim input VAT
- NEVER file VAT return for KATA subjects who are also VAT-exempt
- NEVER issue invoices without NAV Online reporting -- VAT deduction may be denied (Sec. 120(1))
- NEVER apply domestic reverse charge to agricultural products below HUF 100,000 (Sec. 142(8))
- NEVER apply old rates without checking the date-specific rate tables
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 15: Derived Box Calculations [T1]

```
Line 50 = Line 02 + Line 04 + Line 06 + Line 08 + Line 10 + Line 12 + Line 14 + Line 16
Line 51 = Line 30 + Line 31 + Line 32 + Line 33 + Line 34 + Line 35 + Line 36 + Line 37 + Line 38

IF Line 50 > Line 51 THEN
  Line 52 = Line 50 - Line 51  -- Net VAT Payable
  Line 53 = 0
ELSE
  Line 52 = 0
  Line 53 = Line 51 - Line 50  -- Net VAT Credit
END

Line 56 = Line 52 - Line 54  -- Final payable after credit brought forward
IF Line 56 < 0 THEN
  -- Excess credit, may request refund (Line 55) if >= HUF 1,000
  -- Otherwise carry forward to next period
END
```

---

## Step 16: VAT Rates -- Detailed Supply Classification [T1]

### 27% Standard Rate (VAT Act Sec. 82)

| Supply Category | Examples |
|----------------|----------|
| General goods | Electronics, furniture, clothing, household items |
| General services | Professional services, consulting, advertising, IT support |
| Telecommunications | Mobile/internet (unless internet access at 5%) |
| Alcohol | Beer, wine, spirits |
| Tobacco | Cigarettes, cigars, rolling tobacco |
| Motor vehicles | Cars, motorcycles, parts, accessories |
| Construction materials | Cement, steel, timber, fixtures |
| Energy | Electricity, gas (unless district heating at 5%) |

### 18% Reduced Rate (VAT Act Sec. 82(2), Annex III)

| Supply Category | Specific Items |
|----------------|----------------|
| Dairy products | Fresh milk, yogurt, cheese, butter, cream |
| Bakery and grain | Bread, flour, pasta, cereal products |
| Eggs and poultry | Fresh eggs, poultry meat |
| Accommodation | Hotel rooms, guesthouse, Airbnb (commercial) |

### 5% Super-Reduced Rate (VAT Act Sec. 82(2), Annex III)

| Supply Category | Specific Items |
|----------------|----------------|
| Medicines | Prescription and OTC pharmaceutical products |
| Medical devices | Hearing aids, prosthetics, wheelchairs |
| Books and publications | Printed and electronic books, newspapers, periodicals |
| Live performances | Theatre, concerts, opera, ballet |
| District heating | Central heating supply |
| Internet access | Broadband and mobile internet services |
| Restaurant/catering | Dine-in and takeaway food services (from 2024) |
| New residential property | Flats up to 150 sqm, houses up to 300 sqm (conditions apply) |

---

## Step 17: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Escalate to qualified adviser.

- **Corporate income tax (TAO):** 9% flat rate on adjusted profit (Act LXXXI of 1996)
- **Local business tax (IPA):** up to 2% on net revenue, levied by municipality
- **Social contributions:** employer 13% social contribution tax (SZOCHO); employee 18.5% (10% pension + 7% health + 1.5% labor market)
- **Personal income tax (SZJA):** 15% flat rate
- **KATA:** HUF 50,000/month flat tax for eligible sole proprietors
- **Dividend tax:** 15% SZJA on dividends paid to individuals

---

## Contribution Notes

This skill covers Hungary's VAT system based on Act CXXVII of 2007 as amended. Hungary has the highest standard VAT rate in the EU at 27%. Key distinctive features include: the NAV Online Invoice real-time reporting obligation, extensive blocked deduction categories (vehicles, food, entertainment, residential property), domestic reverse charge for construction/waste/grain, and the KATA simplified regime. Validation by a qualified Hungarian adotanacsado is required before production use.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
