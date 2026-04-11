---
name: cyprus-vat-return
description: Use this skill whenever asked to prepare, review, or create a Cyprus VAT return (VAT4 form) for any client. Trigger on phrases like "prepare Cyprus VAT return", "do the Cyprus VAT", "fill in VAT4", "create the return", "Cyprus VAT filing", or any request involving Cyprus VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data for Cyprus-registered entities. This skill contains the complete Cyprus VAT classification rules, box mappings, deductibility rules, reverse charge treatment, capital goods rules, partial exemption, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Cyprus VAT-related work.
---

# Cyprus VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Cyprus |
| Jurisdiction Code | CY |
| Primary Legislation | Value Added Tax Law N.95(I)/2000, as amended (Harmonisation with EU VAT Directive 2006/112/EC) |
| Supporting Legislation | Fifth Schedule (reduced rates); Sixth Schedule (zero-rated supplies); Seventh Schedule (exempt supplies); Eighth Schedule (immovable property); Ninth Schedule (special schemes); Section 11B (domestic reverse charge -- construction); Section 11C (gas/electricity/emissions); Section 11D (telecommunications); Section 11E (gold) |
| Tax Authority | Cyprus Tax Department, Ministry of Finance |
| Filing Portal | https://taxisnet.mof.gov.cy (TAXISnet) / TAX FOR ALL (TFA) portal |
| Contributor | Pending -- requires licensed CY practitioner |
| Validated By | Deep research verification, April 2026 |
| Validation Date | Pending |
| Skill Version | 1.0 (Draft -- awaiting practitioner sign-off) |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial exemption pro-rata, immovable property classification, TOMS/margin scheme, ship management. Tier 3: complex group structures, cross-border property, non-standard supplies. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed accountant and document the gap.

---

## SECTION 1: VAT Return Form Structure (Form VAT4)

**Legislation:** VAT Law N.95(I)/2000, Section 14; Cyprus Tax Department Official VAT4 Form.

The Cyprus VAT return (Form VAT4) is filed electronically via the TAXISnet portal. Unlike Malta's VAT3 (which has 45+ boxes with separate boxes per rate), Cyprus uses a consolidated structure with fewer boxes. All amounts are in EUR with two decimal places. The form is divided into tax boxes (VAT amounts) and value boxes (net amounts excluding VAT).

### Group A: Output Tax (VAT Due)

| Box | Description | What Goes In | Derived? |
|-----|-------------|--------------|----------|
| Box 1 | VAT due on sales and other outputs | Total output VAT on all local taxable supplies at all rates (19%, 9%, 5%, 3%) + VAT on deemed supplies + self-assessed output VAT on domestic reverse charge (construction Art. 11B, gold Art. 11E, telecoms Art. 11D, gas/electricity Art. 11C) | No |
| Box 2 | VAT due on acquisitions from EU Member States | Self-assessed output VAT at applicable CY rate on intra-EU acquisitions of goods (Section 11) AND services received from EU suppliers under reverse charge (Section 11A) + self-assessed VAT on services received from non-EU suppliers (Section 11A) | No |
| Box 3 | Total VAT due (output) | Sum of Box 1 + Box 2 | **Yes** |

### Group B: Input Tax (VAT Recoverable)

| Box | Description | What Goes In | Derived? |
|-----|-------------|--------------|----------|
| Box 4 | VAT reclaimed on purchases and other inputs | Total deductible input VAT on local purchases + input VAT self-assessed on EU acquisitions (reverse charge input side) + input VAT self-assessed on non-EU services (reverse charge input side) + import VAT paid to Customs (from C88/SAD) + input VAT on domestic reverse charge (construction, gold, telecoms, gas/electricity) | No |

### Group C: Net VAT Position

| Box | Description | What Goes In | Derived? |
|-----|-------------|--------------|----------|
| Box 5 | Net VAT payable or refundable | Box 3 minus Box 4. Positive = tax payable. Negative = credit (carry forward or claim refund). | **Yes** |

### Group D: Value Boxes (Net Amounts, Excluding VAT)

| Box | Description | What Goes In | Derived? |
|-----|-------------|--------------|----------|
| Box 6 | Total value of sales and all other outputs (excl. VAT) | Net value of ALL sales: taxable (all rates), zero-rated, and exempt. Includes deemed supplies. | No |
| Box 7 | Total value of purchases and all inputs (excl. VAT) | Net value of ALL purchases: local taxable, EU acquisitions, imports, services from abroad, out-of-scope items. | No |

### Group E: EU Acquisitions and Dispatches (Supplementary Value Boxes)

| Box | Description | What Goes In | Derived? |
|-----|-------------|--------------|----------|
| Box 8A | Total value of intra-EU supplies of goods | Net value of goods supplied to VAT-registered businesses in other EU Member States (zero-rated B2B supplies with transport proof) | No |
| Box 8B | Total value of services supplied to other EU Member States | Net value of B2B services where place of supply shifts to customer's EU Member State under the general rule (Section 5) | No |
| Box 9 | Total value of zero-rated output transactions | Net value of zero-rated sales NOT included in Box 8A or 8B: exports outside EU, zero-rated local supplies (Sixth Schedule items) | No |
| Box 10 | Sales outside scope of CY VAT with right of input deduction | Net value of out-of-scope supplies that still preserve the right to deduct input VAT (e.g., B2B services to non-EU where place of supply is outside CY) | No |
| Box 11A | Total value of goods acquired from EU Member States | Net value of goods (plus related ancillary costs: freight, insurance) acquired from VAT-registered EU suppliers | No |
| Box 11B | Total value of services received from other EU Member States | Net value of B2B services received from EU suppliers where reverse charge applies (Section 11A) | No |

### Derived Calculations [T1]

```
Box 3  = Box 1 + Box 2
Box 5  = Box 3 - Box 4

If Box 5 > 0:  Tax payable to Cyprus Tax Department (due by filing deadline)
If Box 5 < 0:  Credit -- carry forward to next period or submit refund claim
If Box 5 = 0:  Nil return (still must be filed)
```

**Note:** Boxes 6 through 11B are VALUE boxes (net amounts excluding VAT). They do not participate in the tax calculation but are required for control, reconciliation, risk assessment, and VIES cross-matching by the Tax Department.

---

## SECTION 2: Transaction Classification Matrix

### Step 2a: Determine Transaction Type [T1]

**Legislation:** VAT Law N.95(I)/2000, Section 3 (taxable supplies), Section 5 (place of supply).

- Sale (output VAT) or Purchase (input VAT)
- Salaries, contractor payments (employment), income tax payments, loan repayments, dividends, bank charges, Social Insurance contributions, GHS contributions = OUT OF SCOPE (never on VAT return)

### Step 2b: Determine Counterparty Location [T1]

- Cyprus (local): supplier/customer country is CY
- EU Member States: AT, BE, BG, HR, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else (US, UK, AU, CH, etc.)
- **Note:** UK is Non-EU post-Brexit. Northern Cyprus (TRNC) is treated as outside EU VAT territory. Gibraltar is Non-EU. Channel Islands are Non-EU.

### Step 2c: Determine VAT Rate [T1]

**Legislation:** VAT Law N.95(I)/2000, Fifth Schedule, Sixth Schedule.

- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Normalize to nearest standard rate: 0%, 3%, 5%, 9%, 19%
- Boundaries: <= 1% = 0%; 1-4% = 3%; 4-7% = 5%; 7-14% = 9%; >= 14% = 19%

### Step 2d: Determine Expense Category [T1]

**Legislation:** VAT Law N.95(I)/2000, Section 20 (capital goods adjustment).

- Capital goods (immovable): land, buildings, major construction -- adjustment period 10 years
- Capital goods (movable): equipment, vehicles, machinery -- adjustment period 5 years
- Resale: goods bought to literally resell (not inputs consumed in delivering a service)
- Overhead/services: everything else

### Complete Transaction-to-Box Assignment Matrix [T1]

#### Sales -- Local (Cyprus Customer)

| Rate | Box 1 (Output VAT) | Box 6 (Value) | Box 9 | Notes |
|------|---------------------|---------------|-------|-------|
| 19% | Output VAT at 19% | Net amount | -- | Standard rate |
| 9% | Output VAT at 9% | Net amount | -- | Accommodation, restaurants |
| 5% | Output VAT at 5% | Net amount | -- | Foodstuffs, pharma, qualifying property |
| 3% | Output VAT at 3% | Net amount | -- | Books, waste services |
| 0% (zero-rated) | -- | Net amount | Net amount | Exports, Sixth Schedule items |
| Exempt | -- | Net amount | -- | Seventh Schedule; no VAT, no Box 9 |

#### Sales -- EU Customer (B2B)

| Type | Box 1 | Box 6 | Box 8A | Box 8B | Box 9 | Notes |
|------|-------|-------|--------|--------|-------|-------|
| Goods to EU VAT-registered | -- | Net amount | Net amount | -- | -- | Zero-rated; customer reverses; VIES required |
| Services to EU VAT-registered (B2B general rule) | -- | Net amount | -- | Net amount | -- | Place of supply = customer country; VIES required |
| Services to EU non-VAT-registered (B2C) | Output VAT at CY rate | Net amount | -- | -- | -- | CY VAT applies unless OSS/IOSS used |

#### Sales -- Non-EU Customer

| Type | Box 1 | Box 6 | Box 9 | Box 10 | Notes |
|------|-------|-------|-------|--------|-------|
| Goods exported | -- | Net amount | Net amount | -- | Zero-rated; transport/customs proof required |
| Services B2B (general rule) | -- | Net amount | -- | Net amount | Outside scope; input deduction right preserved |
| Services B2C (CY place of supply) | Output VAT at CY rate | Net amount | -- | -- | CY VAT applies |

#### Purchases -- Local (Cyprus Supplier)

| Rate | Box 4 (Input VAT) | Box 7 (Value) | Notes |
|------|-------------------|---------------|-------|
| 19% | VAT amount (if deductible) | Net amount | Standard. Check blocked categories first. |
| 9% | VAT amount (if deductible) | Net amount | Accommodation, restaurants |
| 5% | VAT amount (if deductible) | Net amount | Foodstuffs, pharma |
| 3% | VAT amount (if deductible) | Net amount | Books, waste services |
| 0% | -- | Net amount | No input VAT to claim |
| Exempt | -- | Net amount | No input VAT |

#### Purchases -- EU Supplier (Reverse Charge)

| Type | Box 2 (Output) | Box 4 (Input) | Box 7 (Value) | Box 11A/11B | Notes |
|------|----------------|---------------|---------------|-------------|-------|
| Goods from EU | VAT at 19% | VAT at 19% (if deductible) | Net amount | Box 11A | Both sides of reverse charge. Section 11. |
| Services from EU (B2B general rule) | VAT at 19% | VAT at 19% (if deductible) | Net amount | Box 11B | Both sides of reverse charge. Section 11A. |
| Capital goods from EU | VAT at 19% | VAT at 19% (if deductible) | Net amount | Box 11A | Same as goods; capital goods adjustment applies. |
| Local consumption (hotel, restaurant, taxi abroad) | -- | -- | Gross amount | -- | Foreign VAT paid at source. NOT reverse charge. |
| Out-of-scope (wages, dividends) | -- | -- | -- | -- | NEVER reverse charge. |

#### Purchases -- Non-EU Supplier

| Type | Box 2 (Output) | Box 4 (Input) | Box 7 (Value) | Notes |
|------|----------------|---------------|---------------|-------|
| Services from non-EU (B2B) | VAT at 19% | VAT at 19% (if deductible) | Net amount | Reverse charge. Section 11A. |
| Physical goods import | -- | Import VAT from C88/SAD | Net amount | VAT paid to Customs, recoverable via Box 4. Section 17. |
| Local consumption abroad | -- | -- | Gross amount | Foreign VAT paid at source. NOT reverse charge. |
| Out-of-scope | -- | -- | -- | NEVER reverse charge. |

#### Domestic Reverse Charge -- Construction (Section 11B) [T1]

| Type | Box 1 (Output) | Box 4 (Input) | Box 6 | Box 7 | Notes |
|------|----------------|---------------|-------|-------|-------|
| Construction services received (recipient is VAT-registered) | VAT at 19% | VAT at 19% (if deductible) | -- | Net amount | Supplier invoices without VAT. Recipient self-accounts. Goes in Box 1, NOT Box 2. |

#### Domestic Reverse Charge -- Other Sectors [T1]

| Type | Section | Box 1 (Output) | Box 4 (Input) | Notes |
|------|---------|----------------|---------------|-------|
| Emissions allowances | 11C | VAT at 19% | VAT at 19% (if deductible) | Domestic reverse charge |
| Gas/electricity via distribution networks | 11C | VAT at 19% | VAT at 19% (if deductible) | Domestic reverse charge |
| Telecommunications services | 11D | VAT at 19% | VAT at 19% (if deductible) | Domestic reverse charge |
| Gold and gold material (> 325/1000 fineness) | 11E | VAT at 19% | VAT at 19% (if deductible) | Domestic reverse charge |
| Mobile phones and integrated circuit devices | 11B(2) | VAT at 19% | VAT at 19% (if deductible) | Domestic reverse charge; value > EUR 4,000 per invoice |

---

## SECTION 3: VAT Rates

**Legislation:** VAT Law N.95(I)/2000, Fifth Schedule (reduced rates), Sixth Schedule (zero-rated supplies), Seventh Schedule (exempt supplies).

### Standard Rate: 19% [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 19% | All goods and services not covered by reduced, zero, or exempt categories | VAT Law N.95(I)/2000, Section 18(a) |

### Reduced Rate: 9% [T1]

| Category | Detail | Legislation |
|----------|--------|-------------|
| Accommodation | Hotels, motels, holiday apartments, holiday villages, tourist residences, camping sites, furnished holiday dwellings | Fifth Schedule, Part II, Table A |
| Restaurant and catering services | Food and beverages for on-premises or off-premises consumption; excludes alcoholic beverages when sold separately | Fifth Schedule, Part II, Table A |
| Local passenger transport | Bus, taxi, and other licensed local passenger transport within Cyprus | Fifth Schedule, Part II, Table A |
| Old people's/care home supplies | Supplies by care homes for the elderly | Fifth Schedule, Part II, Table A |

### Reduced Rate: 5% [T1]

| Category | Detail | Legislation |
|----------|--------|-------------|
| Foodstuffs (non-zero-rated) | Processed food, frozen foods, canned goods, prepared meals (not served in restaurants) | Fifth Schedule, Part II, Table B |
| Pharmaceutical products | Medicines for human therapeutic/prophylactic use | Fifth Schedule, Part II, Table B |
| Books and newspapers (non-3%) | Printed matter not qualifying for 3% rate | Fifth Schedule, Part II, Table B |
| Medical aids/devices | Wheelchairs, prostheses, hearing aids, spectacles, contact lenses | Fifth Schedule, Part II, Table B |
| Children's car seats | Safety seats for child passengers | Fifth Schedule, Part II, Table B |
| Renovation of private dwellings | Renovation/repair of used private residences (3+ years old), subject to conditions; labour component only | Fifth Schedule, Part II, Table B |
| New residential property (primary residence) | First 130 m2 of primary/permanent residence; value up to EUR 350,000; total transaction up to EUR 475,000; natural person buyer; 10-year residence commitment | Fifth Schedule, Part II, Table B; Eighth Schedule |
| Liquefied petroleum gas (LPG) in cylinders | LPG sold in cylinders for domestic use | Fifth Schedule, Part II, Table B |
| Cut flowers and plants for decorative use | Fresh cut flowers and ornamental plants | Fifth Schedule, Part II, Table B |

### Reduced Rate: 3% [T1]

| Category | Detail | Legislation |
|----------|--------|-------------|
| Books, newspapers, magazines | Paper and electronic publications (not primarily advertising material) | Fifth Schedule, Part II, Table C |
| Street cleaning, waste collection | Municipal waste collection, street cleaning, refuse disposal services | Fifth Schedule, Part II, Table C |
| Sewage treatment | Sewage collection and treatment services | Fifth Schedule, Part II, Table C |
| First performance of theatrical/musical/dance events | Entrance fees to a first public performance of a theatrical, musical, or dance event in Cyprus | Fifth Schedule, Part II, Table C |
| Goods for citizens with special needs | Assistive devices and aids for persons with disabilities | Fifth Schedule, Part II, Table C |

### Zero-Rated Supplies: 0% [T1]

**Legislation:** VAT Law N.95(I)/2000, Sixth Schedule.

| Category | Detail | Legislation |
|----------|--------|-------------|
| Exports outside the EU | Goods exported to non-EU countries with customs/transport proof | Sixth Schedule, Item 1 |
| Intra-EU B2B supplies of goods | Goods dispatched to VAT-registered persons in other EU Member States (valid VIES number + transport proof) | Sixth Schedule, Item 2; Section 10 |
| International transport | Transport of passengers and goods to/from destinations outside Cyprus | Sixth Schedule, Item 3 |
| Supplies to qualifying aircraft/vessels | Fuel, provisions, and equipment for qualifying international sea-going vessels and aircraft | Sixth Schedule, Item 4 |
| Temporary zero-rate (to 31 December 2026) | Baby milk, infant diapers, adult diapers, women's hygiene products, fresh/chilled (not frozen) vegetables, fresh fruits (Decree 337/2025) | Decree 337/2025 |

### Exempt Supplies (No VAT, No Input Credit) [T1]

**Legislation:** VAT Law N.95(I)/2000, Seventh Schedule.

| Category | Detail | Legislation |
|----------|--------|-------------|
| Postal services | Universal postal services by the national postal provider | Seventh Schedule, Item 1 |
| Financial services | Banking, credit, financial guarantees, securities dealing, fund management (option to tax available for B2B) | Seventh Schedule, Item 2 |
| Insurance and reinsurance | All insurance and reinsurance services, including brokerage/agency | Seventh Schedule, Item 3 |
| Letting of immovable property (residential) | Long-term residential letting; short-term (< 3 months) is taxable at 9% | Seventh Schedule, Item 4 |
| Medical and dental services | Services by registered/licensed medical or dental practitioners | Seventh Schedule, Item 5 |
| Education and training | Education by eligible public/private educational institutions; vocational training by approved bodies | Seventh Schedule, Item 6 |
| Cultural services by public bodies/non-profits | Admission to museums, galleries, cultural events organised by non-profit bodies | Seventh Schedule, Item 7 |
| Betting, lotteries, gambling | All forms of betting, gambling, lottery services | Seventh Schedule, Item 8 |
| Supply of non-building land | Agricultural or non-building land not intended for construction | Seventh Schedule, Item 9 |
| Sale of used buildings (after 5 years) | Buildings sold more than 5 years after completion, unless seller has opted to tax | Seventh Schedule, Item 10 |

---

## SECTION 4: Blocked Input Tax

**Legislation:** VAT Law N.95(I)/2000, Section 20.

### Blocked Categories Table [T1]

| Category | Rule | Exception | Legislation |
|----------|------|-----------|-------------|
| Entertainment of non-employees | Input VAT on entertaining non-employees (clients, suppliers, prospects) is FULLY BLOCKED | Entertainment of own employees (staff events, Christmas party) IS deductible | Section 20(2)(a) |
| Private motor vehicles (saloon cars) | Input VAT on purchase, import, hire, or leasing of private motor cars is BLOCKED | (1) Cars held for resale by motor dealers; (2) Driving instruction vehicles; (3) Taxi/hire cars as business activity; (4) Demonstrably 100% business-use vehicles [T2 -- reviewer must confirm]; (5) Running expenses (fuel, servicing, repairs) for qualifying business vehicles ARE deductible | Section 20(2)(b) |
| Personal/non-business use | Input VAT on goods or services used for personal, non-business purposes is FULLY BLOCKED | Mixed-use: business portion may be claimed if evidenced with records [T2] | Section 20(2)(c) |
| Goods/services for exempt supplies | Input VAT relating SOLELY to exempt supplies cannot be recovered | Partial exemption calculation applies if mixed taxable/exempt supplies (Section 20(3)) | Section 20(2)(d) |
| Yachts and pleasure craft | Input VAT on purchase/import of yachts and pleasure boats for private use is BLOCKED | Yachts used for commercial charter business or for resale by dealers are exceptions [T2 -- reviewer must confirm commercial use] | Section 20(2)(b) |

### Blocking Hierarchy [T1]

```
1. Check BLOCKED CATEGORIES first
2. If blocked -> Input VAT = ZERO, regardless of registration or partial exemption
3. If NOT blocked -> Check registration status
4. If registered -> Check partial exemption
5. If fully taxable -> Full recovery
6. If mixed taxable/exempt -> Apply pro-rata (Section 20(3))
```

**Blocked categories OVERRIDE partial exemption. Always check blocked FIRST.**

---

## SECTION 5: Registration

**Legislation:** VAT Law N.95(I)/2000, Sections 6-10.

### Registration Thresholds [T1]

| Threshold | Value | Trigger | Legislation |
|-----------|-------|---------|-------------|
| Compulsory registration | EUR 15,600 | Taxable turnover in preceding 12 months exceeds threshold | Section 6(1) |
| Anticipated registration | EUR 15,600 | Reasonable grounds to expect turnover will exceed threshold within next 30 days | Section 6(2) |
| EU goods acquisition | EUR 10,251.61 | Value of intra-EU acquisitions exceeds threshold in calendar year | Section 10 |
| EU services received (B2B) | EUR 15,600 | Services from abroad subject to reverse charge, if total taxable supplies (including deemed supplies) exceed threshold | Section 6 |
| Distance selling (EU-wide) | EUR 10,000 | EU-wide threshold for B2C distance sales of goods/digital services to other EU Member States (triggers OSS/IOSS registration) | EU Regulation 2019/1995 |
| Non-established taxable person | No threshold | Any taxable supply in Cyprus by a person not established in CY triggers immediate registration | Section 6(4) |

### Voluntary Registration [T1]

**Legislation:** VAT Law N.95(I)/2000, Section 7.

- Any person carrying on economic activity may register voluntarily, even if below the EUR 15,600 threshold.
- Once voluntarily registered, subject to all VAT obligations (filing, charging, record-keeping).
- Cannot deregister voluntarily for at least 2 years (unless activity ceases).

### VAT Number Format [T1]

| Component | Format |
|-----------|--------|
| Country prefix | CY |
| Numeric digits | 8 digits |
| Check letter | 1 alphabetic character |
| Full format | CY12345678X |
| VIES validation | Must be validated via VIES before zero-rating intra-EU supplies |

### Registration Process [T1]

- Registration via TAXISnet portal (https://taxisnet.mof.gov.cy) or the TAX FOR ALL (TFA) portal.
- Application form TD2001.
- Required documents: certificate of incorporation/registration, ID of directors/partners, proof of economic activity.
- Tax Department assigns the quarterly group (A, B, or C) upon registration.

---

## SECTION 6: Filing Deadlines and Penalties

**Legislation:** VAT Law N.95(I)/2000, Sections 14, 45, 46, 47.

### Filing Frequency and Deadlines [T1]

| Period Type | Frequency | Deadline | Legislation |
|-------------|-----------|----------|-------------|
| Standard | Quarterly | 10th day of the second month following the end of the quarter | Section 14(1) |
| Special arrangement | Monthly | By agreement with Tax Commissioner; 10th of second month after period end | Section 14(2) |
| VIES (Recapitulative Statement) | Monthly | 15th of the month following the reporting period | Section 14(4) |
| Intrastat | Monthly (if above threshold) | 10th working day of the following month | Customs regulations |

### Quarterly Groups [T1]

The Cyprus Tax Department assigns businesses to one of three quarterly groups based on activity type:

| Group | Activity Type | Q1 | Q2 | Q3 | Q4 | Q1 Filing Deadline |
|-------|--------------|----|----|----|----|-------------------|
| Group A | Retailers | Jan-Mar | Apr-Jun | Jul-Sep | Oct-Dec | 10 May |
| Group B | Industry/Manufacturing | Feb-Apr | May-Jul | Aug-Oct | Nov-Jan | 10 June |
| Group C | Services/Professions | Mar-May | Jun-Aug | Sep-Nov | Dec-Feb | 10 July |

**The Tax Department assigns the group at registration. The client MUST know their assigned group. If unknown, STOP and confirm before filing.**

### Late Filing Penalties [T1]

**Legislation:** VAT Law N.95(I)/2000, Section 45.

| Offence | Penalty | Legislation |
|---------|---------|-------------|
| Late submission of VAT return | EUR 51 per return | Section 45(1)(a) |
| Late submission of VIES declaration | EUR 50 per missed monthly declaration | Section 45(1)(b) |
| Failure to register when required | EUR 85 per month of delay | Section 45(2) |
| VIES correction after 1-month window | EUR 15 per correction | Section 45(1)(c) |
| Failure to issue tax invoice | EUR 205 per invoice | Section 45(3) |
| Non-compliance with reverse charge (filing) | EUR 200 per VAT return, maximum EUR 4,000 per period | Section 45(4) |
| Incorrect VAT return (negligence) | Up to EUR 4,000 per return | Section 46 |
| Fraudulent VAT return | Criminal prosecution; fine up to EUR 34,172 and/or imprisonment up to 3 years | Section 47 |

### Late Payment Interest [T1]

**Legislation:** VAT Law N.95(I)/2000, Section 45(5).

| Item | Detail |
|------|--------|
| Interest rate | 1.75% per quarter on outstanding VAT balance (i.e., approximately 7% per annum, compounding quarterly) |
| Accrual start | Day after the filing/payment deadline |
| Applies to | Tax payable (Box 5 positive) not remitted by deadline |
| Payment methods | Direct debit, bank transfer, online payment via TFA portal |

### Refund Timeline [T1]

**Legislation:** VAT Law N.95(I)/2000, Section 20(5).

| Scenario | Timeline |
|----------|----------|
| Standard refund | Within 4 months of claim submission |
| If investigation required | Extended to 8 months total |
| Interest on late refund | Payable by Tax Department if refund delayed beyond statutory period |
| Refund blocked if | Taxpayer has outstanding income tax returns unfiled |
| Claim time limit | Refund claim must be submitted within 6 years of the relevant period |

---

## SECTION 7: Reverse Charge

**Legislation:** VAT Law N.95(I)/2000, Section 11 (intra-EU acquisitions of goods), Section 11A (services from abroad), Section 11B (domestic -- construction), Section 11C (gas/electricity/emissions), Section 11D (telecommunications), Section 11E (gold).

### Intra-EU Acquisitions of Goods (Section 11) [T1]

| Step | Action | Box |
|------|--------|-----|
| 1 | EU supplier invoices at 0% (intra-EU supply) | -- |
| 2 | CY recipient self-assesses output VAT at 19% | Box 2 |
| 3 | CY recipient claims input VAT at 19% (if deductible) | Box 4 |
| 4 | Report net value of goods | Box 7, Box 11A |
| Net effect | Zero for fully taxable businesses | -- |

### Services Received from Abroad -- B2B General Rule (Section 11A) [T1]

Applies to services received from BOTH EU and non-EU suppliers under the B2B general place-of-supply rule.

| Step | Action | Box |
|------|--------|-----|
| 1 | Foreign supplier invoices without CY VAT | -- |
| 2 | CY recipient self-assesses output VAT at 19% | Box 2 |
| 3 | CY recipient claims input VAT at 19% (if deductible) | Box 4 |
| 4 | Report net value | Box 7; Box 11B (EU services only) |
| Net effect | Zero for fully taxable businesses | -- |

### Import of Physical Goods from Non-EU (Section 17) [T1]

| Step | Action | Box |
|------|--------|-----|
| 1 | Goods arrive at CY customs | -- |
| 2 | Import VAT assessed and paid to Customs (C88/SAD document) | -- |
| 3 | Recoverable import VAT entered in Box 4 from C88 | Box 4 |
| 4 | Net value of goods | Box 7 |
| Note | This is NOT reverse charge -- VAT is paid to Customs at the border, not self-assessed on the return. | -- |

### Domestic Reverse Charge -- Construction (Section 11B) [T1]

| Step | Action | Box |
|------|--------|-----|
| 1 | CY contractor provides construction/repair/maintenance/demolition services | -- |
| 2 | Contractor invoices WITHOUT VAT | -- |
| 3 | Recipient self-assesses output VAT at 19% | **Box 1** (NOT Box 2) |
| 4 | Recipient claims input VAT at 19% (if deductible) | Box 4 |
| 5 | Report net value | Box 7 |
| Scope | Applies to all construction services regardless of supplier's VAT status | -- |
| Net effect | Zero for fully taxable businesses | -- |

### Domestic Reverse Charge -- Other Sectors [T1]

| Sector | Section | Box (Output) | Box (Input) | Notes |
|--------|---------|-------------|-------------|-------|
| Emissions allowances | 11C | Box 1 | Box 4 | EU ETS carbon credits |
| Gas/electricity via distribution networks | 11C | Box 1 | Box 4 | Only supplies through networks |
| Telecommunications services | 11D | Box 1 | Box 4 | Between taxable persons |
| Gold (> 325/1000 fineness) | 11E | Box 1 | Box 4 | Investment gold and gold material |
| Mobile phones / integrated circuit devices | 11B(2) | Box 1 | Box 4 | Invoice value > EUR 4,000 |

### Exceptions to Reverse Charge [T1]

| Situation | Treatment | Reason |
|-----------|-----------|--------|
| Out-of-scope categories (wages, bank charges, dividends, loan repayments) | NEVER reverse charge | Not a supply of goods or services |
| Local consumption abroad (hotel, restaurant, taxi, conference, car rental in another country) | NOT reverse charge | Foreign VAT paid at source; irrecoverable cost |
| EU supplier charged their local VAT > 0% | NOT reverse charge | Foreign VAT is part of the expense; irrecoverable |
| B2C services from abroad (place of supply remains in supplier's country) | NOT reverse charge | Supplier accounts for VAT in their own jurisdiction |

---

## SECTION 8: Edge Cases

### EC1 -- EU hotel / restaurant / taxi booked abroad (e.g., Greece) [T1]

**Situation:** CY-registered client pays for a hotel in Greece via credit card. Invoice shows Greek VAT at 13% or 24%.
**Resolution:** NOT reverse charge. Foreign VAT was charged and paid at source. Treat as overhead expense in Box 7 (gross amount). No entry in Box 2 or Box 4. Greek VAT is an irrecoverable cost embedded in the expense. This is especially common for Cyprus-Greece travel given shared language and close business ties.
**Legislation:** VAT Law N.95(I)/2000, Section 11A -- local consumption exclusion.

### EC2 -- Subscription software from non-EU provider (Google, AWS, Notion) [T1]

**Situation:** Monthly charge from a US company, no VAT shown on invoice. B2B service.
**Resolution:** Reverse charge applies. Box 2 = VAT at 19% on net amount (output). Box 4 = VAT at 19% (input, if deductible). Box 7 = net amount. Net VAT effect = zero for fully taxable business.
**Legislation:** VAT Law N.95(I)/2000, Section 11A (services received from outside Cyprus).

### EC3 -- Cross-border services between Cyprus and Greece [T1]

**Situation:** CY company provides consulting services to a Greek company (B2B). Both are VAT-registered.
**Resolution:** Place of supply is Greece (customer's country) under the general B2B rule. CY supplier invoices at 0%, does NOT charge CY VAT. Report net amount in Box 6 and Box 8B. No Box 1 entry. Greek customer self-accounts for Greek VAT. CY supplier must file VIES declaration by the 15th of the following month. Confirm Greek customer's VAT number via VIES before invoicing.
**Legislation:** VAT Law N.95(I)/2000, Section 5 (place of supply of services).

### EC4 -- Property transactions -- sale of new building [T2]

**Situation:** Developer sells a newly constructed apartment in Limassol.
**Resolution:** Taxable supply at 19% standard rate. If buyer is a natural person acquiring a primary/permanent residence and all conditions are met (area up to 190 m2, 5% on first 130 m2, value up to EUR 350,000, transaction up to EUR 475,000, 10-year residence commitment), the reduced 5% rate applies to the eligible portion. Output VAT in Box 1, net value in Box 6. Developer can recover related input VAT on construction costs. Flag for reviewer: verify ALL reduced rate conditions; verify property is within the 5-year new building window; check for 2026 amendments effective 1 September 2026 (Regulations 102/2026 and 103/2026).
**Legislation:** VAT Law N.95(I)/2000, Fifth Schedule, Eighth Schedule.

### EC5 -- Ship management companies [T2]

**Situation:** Cyprus ship management company provides technical and crew management services for vessels under third-party flags.
**Resolution:** Ship management services related to qualifying sea-going vessels engaged in international navigation are zero-rated under the Sixth Schedule. The company can recover input VAT on related expenses in full. However, if the company also provides services unrelated to qualifying vessels (e.g., office administration for the shipowner), those services may be standard-rated or subject to the B2B place-of-supply rule. Flag for reviewer: (1) confirm vessel qualifies as international sea-going; (2) confirm services are directly related to the vessel's operation; (3) if mixed supplies exist, partial attribution may be required.
**Legislation:** VAT Law N.95(I)/2000, Sixth Schedule, Item 4 (supplies related to qualifying vessels); Section 5 (place of supply).

### EC6 -- Holding companies and partial exemption [T2]

**Situation:** CY holding company receives dividends and also provides management services to subsidiaries.
**Resolution:** Dividends are outside the scope of VAT (not a supply). Management services to subsidiaries are taxable supplies (standard-rated if subsidiary is in CY; reverse charge if subsidiary is in another EU state or non-EU). Input VAT recovery depends on the nature of supplies: (1) if the company makes only taxable supplies (management fees), full recovery; (2) if the company is a pure holding company with no taxable supplies, no recovery; (3) if mixed, partial exemption applies (Section 20(3)). Flag for reviewer: holding company VAT treatment is complex; confirm the exact nature of supplies and the appropriate partial exemption method.
**Legislation:** VAT Law N.95(I)/2000, Section 20(3) (partial exemption); CJEU case law on holding companies.

### EC7 -- Import of yachts/boats [T2]

**Situation:** CY company or individual imports a yacht from a non-EU country (e.g., Turkey, UK).
**Resolution:** Import VAT at 19% is payable to Cyprus Customs upon importation (C88/SAD document). If the yacht is for private/personal use, the import VAT is a final cost and NOT recoverable. If the yacht is for commercial charter business (demonstrable commercial use), the import VAT may be recoverable via Box 4, subject to proof of commercial activity. If the yacht enters CY temporarily under Temporary Admission procedures, VAT may be suspended. Flag for reviewer: (1) confirm commercial vs. private use; (2) check Temporary Admission eligibility; (3) verify customs valuation is correct.
**Legislation:** VAT Law N.95(I)/2000, Section 17 (importation); Section 20(2)(b) (blocked -- pleasure craft for private use).

### EC8 -- Tourism sector reduced rates (hotel + restaurant composite supply) [T2]

**Situation:** Hotel in Paphos charges a single rate for a package including accommodation and half-board meals.
**Resolution:** Both accommodation and restaurant/catering services are subject to the 9% reduced rate. A composite supply where the principal component is accommodation and the ancillary component is catering may be treated as a single supply at 9%. However, if the hotel separately itemises the components, each component is taxed at its applicable rate (both 9% in this case). If the hotel also provides spa services, conference facilities, or other standard-rated services, those must be separately identified and taxed at 19%. Flag for reviewer: confirm whether the package constitutes a single composite supply or multiple distinct supplies.
**Legislation:** VAT Law N.95(I)/2000, Fifth Schedule, Part II, Table A.

### EC9 -- Construction reverse charge -- subcontractor chain [T1]

**Situation:** Main contractor hires a subcontractor who hires a sub-subcontractor for construction work. All are CY VAT-registered.
**Resolution:** Domestic reverse charge under Section 11B applies at EACH level of the chain. Sub-subcontractor invoices subcontractor without VAT (subcontractor self-accounts in Box 1/Box 4). Subcontractor invoices main contractor without VAT (main contractor self-accounts in Box 1/Box 4). Main contractor invoices the end client: if the end client is VAT-registered, reverse charge continues; if the end client is a non-taxable person (private individual), the main contractor charges VAT normally at 19% in Box 1.
**Legislation:** VAT Law N.95(I)/2000, Section 11B.

### EC10 -- Goods via Northern Cyprus territory [T1]

**Situation:** CY company receives goods that transit through the TRNC-controlled area (e.g., goods arriving at Famagusta port then transported to the Republic).
**Resolution:** The TRNC is treated as outside the EU VAT territory. Goods entering the Republic of Cyprus from the TRNC-controlled area are treated as imports for VAT purposes. Import VAT is assessed at the crossing/checkpoint by Cyprus Customs. The import VAT paid is recoverable via Box 4 (if the business is registered and the goods are for taxable activity). Net value goes in Box 7. This is NOT an intra-EU acquisition (not Box 11A).
**Legislation:** Protocol No. 10 to the Act of Accession 2003; VAT Law N.95(I)/2000, Section 17.

### EC11 -- Bad debt relief [T2]

**Situation:** CY-registered supplier issued a tax invoice and accounted for output VAT, but the customer has not paid and the debt is irrecoverable.
**Resolution:** Cyprus allows bad debt relief subject to conditions: (1) the supply must have been taxable and VAT accounted for; (2) the debt must be proven to be irrecoverable (written off in accounts, legal action taken or demonstrably uneconomic); (3) at least 12 months must have elapsed since the due date of payment; (4) the supplier must have notified the Tax Department. The adjustment reduces Box 1 (output VAT) in the period when relief is claimed. Flag for reviewer: confirm all conditions are met; documentation of write-off and notification to Tax Department required.
**Legislation:** VAT Law N.95(I)/2000, Section 21.

### EC12 -- Capital goods scheme for immovable property [T2]

**Situation:** Company acquired a commercial building with full input VAT recovery 4 years ago. Now the building is being used for exempt letting.
**Resolution:** The capital goods adjustment period for immovable property is 10 years. A change in use from taxable to exempt (or vice versa) triggers an annual adjustment for the remaining years. In each remaining year, 1/10th of the original input VAT must be repaid (or recovered) proportionally. If the building was acquired for EUR 500,000 + EUR 95,000 VAT and use changes in year 5, the adjustment for years 5-10 (6 years) = 6/10 x EUR 95,000 = EUR 57,000 to repay. Flag for reviewer: confirm exact date of acquisition, date of change in use, and whether any prior adjustments were made.
**Legislation:** VAT Law N.95(I)/2000, Section 20(4) (capital goods adjustment -- immovable: 10 years).

### EC13 -- Motor vehicle running expenses vs. purchase [T1]

**Situation:** Client has a private saloon car used partly for business.
**Resolution:** Purchase/lease VAT on the car itself is BLOCKED (Section 20(2)(b)). However, running expenses (fuel, repairs, servicing, insurance) are treated separately. If the car is used for business purposes (and the car is not itself a blocked purchase -- e.g., the car was acquired before VAT registration or was acquired VAT-free), the business portion of running expenses is deductible. If the car purchase VAT was blocked, running expenses for that car are also typically blocked unless the car is demonstrably used for a qualifying purpose (taxi, hire, delivery). Flag for reviewer if mixed personal/business use.
**Legislation:** VAT Law N.95(I)/2000, Section 20(2)(b), Section 20(2)(c).

### EC14 -- Credit notes [T1]

**Situation:** Client receives a credit note from a supplier, or issues one to a customer.
**Resolution:** Reverse the original entry. If the original purchase was in Box 4 / Box 7, the credit note reduces Box 4 / Box 7. If the original sale was in Box 1 / Box 6, the credit note reduces Box 1 / Box 6. Net figures are reported. Do not create a separate negative entry in a different box.
**Legislation:** VAT Law N.95(I)/2000, Section 22 (adjustments).

### EC15 -- Director fees [T1]

**Situation:** Individual receives director fees from a CY company.
**Resolution:** Director services by a natural person acting in a dependent capacity (i.e., as an employee/officer of the company) are outside the scope of VAT. Not a taxable supply. Do not include on VAT return. If the director acts in an independent capacity through their own company, the supply of management services IS taxable. [T2] flag if independence status is unclear.
**Legislation:** VAT Law N.95(I)/2000, Section 3 (definition of taxable person and economic activity).

---

## SECTION 9: Test Suite

### Test 1 -- Standard local purchase, 19% VAT, overhead [T1]

**Input:** CY supplier, office supplies, gross EUR 238, VAT EUR 38, net EUR 200. Standard-registered client, fully taxable.
**Expected output:** Box 4 = EUR 38 (input VAT). Box 7 = EUR 200 (net value). Input VAT recoverable in full.

### Test 2 -- Non-EU software subscription, reverse charge [T1]

**Input:** US supplier (Notion), monthly fee EUR 20, no VAT on invoice. Standard-registered client, fully taxable.
**Expected output:** Box 2 = EUR 3.80 (19% output VAT). Box 4 = EUR 3.80 (19% input VAT). Box 7 = EUR 20. Net VAT effect = zero.

### Test 3 -- EU acquisition of goods, reverse charge [T1]

**Input:** German supplier ships goods to Cyprus, invoice EUR 1,000 at 0% (intra-EU supply). Standard-registered client, fully taxable.
**Expected output:** Box 2 = EUR 190 (19% output). Box 4 = EUR 190 (19% input). Box 7 = EUR 1,000. Box 11A = EUR 1,000. Net VAT = zero.

### Test 4 -- EU B2B service sale, zero rated [T1]

**Input:** CY-registered client invoices Italian company EUR 500 for consulting, 0% VAT. Italian customer is VAT registered (verified via VIES).
**Expected output:** Box 6 = EUR 500. Box 8B = EUR 500. No output VAT in Box 1. VIES declaration required by 15th of following month.

### Test 5 -- Motor vehicle, blocked [T1]

**Input:** Standard-registered client purchases a private saloon car, EUR 25,000 net + VAT EUR 4,750 (19%).
**Expected output:** Box 4 = EUR 0 (BLOCKED). Box 7 = EUR 25,000. No input VAT recovery. 10th Schedule blocked category.

### Test 6 -- EU hotel, local consumption exception [T1]

**Input:** Standard-registered client pays for hotel in France, EUR 300 including French VAT.
**Expected output:** No Box 2 or Box 4 entry. Box 7 = EUR 300 (gross). Not reverse charge. French VAT is irrecoverable.

### Test 7 -- Construction reverse charge, domestic (Section 11B) [T1]

**Input:** CY contractor provides building repair services, EUR 5,000 net, invoiced without VAT. Standard-registered recipient, fully taxable.
**Expected output:** Box 1 = EUR 950 (output VAT at 19%). Box 4 = EUR 950 (input VAT). Box 7 = EUR 5,000. Net VAT = zero. Note: Box 1, NOT Box 2.

### Test 8 -- Local sale at 9% (restaurant) [T1]

**Input:** CY-registered restaurant charges customer EUR 109 (EUR 100 net + EUR 9 VAT at 9%).
**Expected output:** Box 1 = EUR 9 (output VAT). Box 6 = EUR 100 (net value).

### Test 9 -- Export outside EU [T1]

**Input:** CY company exports goods to the United States, invoice EUR 2,000, 0% VAT. Transport/customs documentation available.
**Expected output:** Box 6 = EUR 2,000. Box 9 = EUR 2,000. No Box 1 entry. Zero-rated export.

### Test 10 -- Entertainment expense, blocked [T1]

**Input:** Standard-registered client takes a prospective client to dinner, EUR 119 (EUR 100 net + EUR 19 VAT at 19%).
**Expected output:** Box 4 = EUR 0 (BLOCKED -- entertainment of non-employees). Box 7 = EUR 100. No input VAT recovery.

### Test 11 -- EU services received from Greek supplier, reverse charge [T1]

**Input:** Greek law firm provides legal advice to CY company, invoice EUR 2,000, no CY VAT charged. B2B service, general rule applies.
**Expected output:** Box 2 = EUR 380 (19% output). Box 4 = EUR 380 (19% input). Box 7 = EUR 2,000. Box 11B = EUR 2,000. Net VAT = zero.

### Test 12 -- Partially exempt business, local purchase [T2]

**Input:** CY company making 70% taxable and 30% exempt supplies. Purchases general overhead: office rent EUR 1,000 net + EUR 190 VAT (19%). Not attributable to either taxable or exempt supplies exclusively.
**Expected output:** Box 4 = EUR 133 (EUR 190 x 70% pro-rata). Box 7 = EUR 1,000. Flag for reviewer: confirm pro-rata rate of 70% and that the standard method applies.

### Test 13 -- Import of goods from non-EU (customs entry) [T1]

**Input:** CY company imports equipment from China. Customs value EUR 10,000. Import VAT assessed by Customs = EUR 1,900. C88/SAD document received.
**Expected output:** Box 4 = EUR 1,900 (import VAT from C88). Box 7 = EUR 10,000. NOT reverse charge -- VAT was paid to Customs.

---

## SECTION 10: Comparison with Malta

Cyprus and Malta share the same standard VAT rate (19%) and have very similar VAT systems as small EU island Member States. Both transposed the EU VAT Directive 2006/112/EC. This section highlights the key similarities and differences to assist practitioners working across both jurisdictions.

### Rate Comparison [T1]

| Feature | Cyprus | Malta | Notes |
|---------|--------|-------|-------|
| Standard rate | 19% | 18% | **KEY DIFFERENCE.** CY is 19%, MT is 18%. Despite both being commonly described as "19%", Malta's standard rate is actually 18%. |
| Reduced rate 1 | 9% (accommodation, restaurants) | 7% (accommodation) | CY groups accommodation + restaurants at 9%; MT has 7% for accommodation only |
| Reduced rate 2 | 5% (foodstuffs, pharma, property) | 5% (electricity, medical, confectionery) | Both have 5% but for different categories |
| Reduced rate 3 | 3% (books, waste, events) | -- | CY has a super-reduced 3% rate; MT does not |
| Additional reduced | -- | 12% (certain goods) | MT has a 12% rate; CY does not |
| Zero rate | Exports, intra-EU B2B, international transport | Exports, intra-EU B2B, international transport, food items | Similar scope; MT zero-rates more food items |

### VAT Return Structure Comparison [T1]

| Feature | Cyprus (VAT4) | Malta (VAT3) | Notes |
|---------|---------------|--------------|-------|
| Total boxes | 13 boxes (Box 1-11B) | 45+ boxes | CY is consolidated; MT separates by rate |
| Output tax boxes | Box 1 (all rates combined) + Box 2 (EU/non-EU reverse charge) | Separate boxes per rate (Box 23, 23a, 23b, 24) | CY aggregates all output VAT into one box |
| Input tax boxes | Box 4 (all inputs combined) | Separate boxes by category and rate (Box 34-38) | CY aggregates all input VAT into one box |
| EU boxes | Box 8A, 8B, 11A, 11B | Box 1, 9, 9a, 10 | Both track EU supplies/acquisitions; different numbering |
| Capital goods box | No separate box (included in Box 4) | Box 30 (separate) | MT has a dedicated capital goods input box |
| Resale box | No separate box | Box 27, 28, 29 | MT separates resale purchases; CY does not |

### Registration Comparison [T1]

| Feature | Cyprus | Malta | Notes |
|---------|--------|-------|-------|
| Compulsory threshold | EUR 15,600 | EUR 35,000 (Article 11) / EUR 20,000 (Article 10) | CY threshold is significantly lower |
| Small enterprise scheme | Below EUR 15,600 (no registration required) | Article 11 (simplified annual declaration) | CY has no equivalent of Malta's Article 11 annual declaration |
| VAT number format | CY + 8 digits + 1 letter | MT + 8 digits | CY has a trailing check letter; MT does not |
| Registration types | Standard only | Article 10, Article 11, Article 12 | MT has three registration types; CY has one standard type |

### Filing Comparison [T1]

| Feature | Cyprus | Malta | Notes |
|---------|--------|-------|-------|
| Filing frequency | Quarterly (3 groups) | Quarterly (Article 10); Annual (Article 11) | Both quarterly for standard; CY has staggered groups |
| Filing deadline | 10th of 2nd month after quarter end | 21st of month after quarter end (e-filing) | CY allows more time but from different base |
| Late filing penalty | EUR 51 per return | EUR 20 per return | CY penalty is higher |
| Late payment interest | 1.75% per quarter (~7% p.a.) | 0.54% per month (~6.5% p.a.) | Similar effective annual rates |
| VIES filing | Monthly, nil returns required | Monthly, nil returns required | Same obligation |
| E-filing | Mandatory (TAXISnet) | Mandatory (CFR portal) | Both mandate electronic filing |

### Blocked Input Tax Comparison [T1]

| Category | Cyprus | Malta | Notes |
|----------|--------|-------|-------|
| Entertainment | Blocked (non-employees) | Blocked (10th Schedule Item 3(1)(b)) | Same rule in both |
| Motor vehicles | Blocked (private cars) | Blocked (10th Schedule Item 3(1)(a)(iv-v)) | Same exceptions (taxi, hire, resale) |
| Personal use | Blocked | Blocked (10th Schedule Item 3(1)(c)) | Same |
| Tobacco | Not specifically listed | Blocked (10th Schedule Item 3(1)(a)(i)) | MT specifically blocks; CY treats under general rules |
| Alcohol | Not specifically listed | Blocked (10th Schedule Item 3(1)(a)(ii)) | MT specifically blocks; CY treats under general rules |
| Art/antiques | Not specifically listed | Blocked (10th Schedule Item 3(1)(a)(iii)) | MT specifically blocks |
| Pleasure craft | Blocked (private use) | Blocked (10th Schedule Item 3(1)(a)(iv)) | Same |

### Reverse Charge Comparison [T1]

| Feature | Cyprus | Malta | Notes |
|---------|--------|-------|-------|
| EU acquisitions | Box 2 (output) / Box 4 (input) | Box 3,6 (output) / Box 13,13a (input) | Both apply reverse charge; different box mapping |
| Non-EU services | Box 2 (output) / Box 4 (input) | Box 4,7 (output) / Box 15 (input) | Same treatment, different boxes |
| Domestic construction | Yes (Section 11B) | No domestic reverse charge | **KEY DIFFERENCE.** CY has domestic reverse charge for construction; MT does not |
| Domestic gold/telecoms | Yes (Sections 11D, 11E) | No | CY has broader domestic reverse charge |
| Physical goods import | Customs (C88), NOT reverse charge | Customs (C88), NOT reverse charge | Same -- both collect import VAT at border |

### Capital Goods Comparison [T1]

| Feature | Cyprus | Malta | Notes |
|---------|--------|-------|-------|
| Immovable property adjustment | 10 years | 20 years (proposed) | Different adjustment periods |
| Movable property adjustment | 5 years | 5 years (if >= EUR 1,160) | Same for movable; CY has no minimum threshold specified for movable |
| MT capital goods threshold | N/A | EUR 1,160 gross | MT has a specific threshold; CY does not specify a comparable minimum |

### Key Differences Summary

1. **Standard rate:** CY 19% vs MT 18% -- practitioners must not assume they are the same.
2. **CY has a 3% super-reduced rate** that MT does not have.
3. **MT has a 12% reduced rate** that CY does not have.
4. **CY has domestic reverse charge for construction** (Section 11B); MT does not.
5. **CY registration threshold (EUR 15,600) is much lower** than MT's Article 11 threshold (EUR 35,000).
6. **CY VAT return is consolidated** (13 boxes); MT's VAT3 is granular (45+ boxes with per-rate breakdown).
7. **CY has no equivalent of Malta's Article 11** simplified annual declaration for small enterprises.
8. **CY has quarterly groups** (A/B/C based on activity); MT quarters are uniform calendar quarters.
9. **CY VAT number includes a trailing letter**; MT does not.
10. **CY immovable property capital goods adjustment is 10 years**; MT is up to 20 years.

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT boxes -- box assignment is 100% deterministic from transaction facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges, loan repayments, Social Insurance)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi in another country)
- NEVER allow input VAT recovery on entertainment of non-employees
- NEVER allow input VAT recovery on private motor vehicle purchase/hire (unless qualifying exception applies and reviewer confirms)
- NEVER allow input VAT recovery on yachts/pleasure craft for private use
- NEVER allow input VAT recovery for businesses below the registration threshold / not VAT-registered
- NEVER confuse zero-rated (input VAT deductible) with exempt without credit (input VAT NOT deductible)
- NEVER apply reverse charge when EU supplier charged local VAT > 0%
- NEVER report domestic construction reverse charge in Box 2 -- it goes in Box 1 (domestic output)
- NEVER report domestic gold/telecoms/gas reverse charge in Box 2 -- it goes in Box 1
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER file a VAT return without confirming the client's quarterly group assignment (A, B, or C)
- NEVER omit a nil VIES return -- Cyprus requires submission even with zero intra-EU supplies
- NEVER apply the 5% reduced rate on residential property without verifying ALL eligibility conditions
- NEVER treat Northern Cyprus (TRNC) as EU territory for VAT purposes
- NEVER assume CY and MT have the same standard rate -- CY is 19%, MT is 18%
- NEVER classify imports of physical goods as reverse charge -- import VAT is paid to Customs (C88/SAD)

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and VAT number** [T1] -- CY + 8 digits + 1 letter (e.g., CY12345678X)
2. **VAT registration status** [T1] -- Standard registration, below threshold (not registered), or non-established taxable person
3. **VAT period and quarterly group** [T1] -- Group A (retailers), Group B (industry), or Group C (services). Which quarter is being filed?
4. **Industry/sector** [T2] -- Impacts quarterly group assignment, deductibility, and special rules (construction triggers Section 11B awareness; shipping triggers Sixth Schedule awareness; tourism triggers reduced rate awareness)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial exemption calculation required (pro-rata rate needed; reviewer must confirm rate and method -- standard or special)
6. **Does the business trade goods for resale?** [T1] -- Impacts input classification
7. **Credit balance brought forward** [T1] -- From prior period (negative Box 5 carried forward)
8. **Does the client deal in immovable property?** [T2] -- Triggers Eighth Schedule rules, 5% primary residence conditions, capital goods adjustment
9. **Does the client operate as a tour operator or travel agent?** [T2] -- Triggers TOMS (Ninth Schedule)
10. **Does the client manage ships or own yachts?** [T2] -- Triggers Sixth Schedule (zero-rating for qualifying vessels) and Section 20(2)(b) (blocked pleasure craft)

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration status, quarterly group, and period are confirmed.**

---

## Special Schemes [T2]

### Tour Operators' Margin Scheme (TOMS)

**Legislation:** VAT Law N.95(I)/2000, Ninth Schedule.

| Aspect | Rule |
|--------|------|
| Who | Tour operators, travel agents, online booking platforms selling travel packages |
| Scope | Package holidays, accommodation, transport, and ancillary services bought and resold as a package |
| VAT base | Margin = selling price minus cost of bought-in services |
| VAT rate | 19% on the margin |
| Place of supply | Where the tour operator is established (Cyprus) |
| Input VAT | No input VAT recovery on bought-in travel services (margin already accounts for this) |
| Reporting | Report margin-based VAT in Box 1; net margin in Box 6 |

**Flag for reviewer:** TOMS is complex. Confirm applicability and calculation with licensed accountant before filing.

### Margin Scheme for Second-Hand Goods

**Legislation:** VAT Law N.95(I)/2000, Ninth Schedule.

| Aspect | Rule |
|--------|------|
| Who | Taxable dealers in second-hand goods, works of art, collectors' items, antiques |
| Scope | Items purchased without VAT (from private individuals, exempt persons, or other margin scheme dealers) |
| VAT base | Margin = selling price minus purchase price |
| VAT rate | 19% on the margin |
| Optional | Use of the scheme is optional per item |
| Record-keeping | Stock book with purchase/sales details, stock numbers, margin calculations |

---

## Partial Exemption [T2]

**Legislation:** VAT Law N.95(I)/2000, Section 20(3).

If business makes both taxable and exempt supplies:

### Standard Method (Pro-Rata)

```
Recovery % = (Value of Taxable Supplies / Value of Total Supplies) * 100
```

Round up to the next whole percentage point.

### De Minimis Rule

Where non-deductible input tax is less than 50% of total input tax AND less than approximately EUR 171 (CYP 100 equivalent) per month on average, input tax is fully deductible.

### Special Method

Businesses may apply to the Tax Department for an individual methodology suited to their operations. Written permission must be obtained in advance.

### Annual Adjustment

Businesses must perform an annual adjustment based on actual figures for the full year, comparing against provisional quarterly calculations. This is done in the first return following the end of the tax year.

**Flag for reviewer: pro-rata calculation and annual adjustment must be confirmed by licensed accountant before filing.**

---

## Key Thresholds Reference Table [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Compulsory VAT registration | EUR 15,600 in any rolling 12 months | Section 6, VAT Law N.95(I)/2000 |
| Anticipated threshold (next 30 days) | EUR 15,600 | Section 6 |
| EU goods acquisition trigger | EUR 10,251.61 in calendar year | Section 10 |
| EU distance selling (B2C) | EUR 10,000 EU-wide | EU Regulation 2019/1995 |
| Capital goods adjustment -- immovable property | 10-year adjustment period | Section 20(4) |
| Capital goods adjustment -- movable property | 5-year adjustment period | Section 20(4) |
| New building classification | Within 5 years of completion | Eighth Schedule |
| Reduced 5% VAT on primary residence | First 130 m2; total area max 190 m2; value max EUR 350,000; transaction max EUR 475,000 | Fifth Schedule |
| Domestic reverse charge -- mobile phones/ICD | Invoice value > EUR 4,000 | Section 11B(2) |
| Intrastat arrivals (2026) | EUR 380,000 | Customs regulations |
| Intrastat dispatches (2026) | EUR 75,000 | Customs regulations |
| Intrastat detailed arrivals (2026) | EUR 2,700,000 | Customs regulations |
| Intrastat detailed dispatches (2026) | EUR 5,800,000 | Customs regulations |

---

## Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Do not execute any of these rules. Escalate to licensed accountant.

- **Corporate income tax rate:** 12.5% (one of the lowest in the EU; increased to 15% from 2026 under Pillar Two for qualifying entities)
- **Special Defence Contribution (SDC):** Applies to dividends (17%), interest (30%), and rental income (3%) for CY tax residents domiciled in CY
- **General Healthcare System (GHS) contributions:** Various rates on employment income, emoluments, pensions, dividends, interest, rental income
- **Social Insurance Contributions:** Separate obligation. Out of scope of this skill.
- **Capital Gains Tax:** 20% on gains from disposal of immovable property situated in Cyprus. Not a VAT matter.
- **Transfer fees:** Land Registry fees on property transfers. Not a VAT matter.
- **Tonnage tax:** Cyprus tonnage tax system for qualifying shipping companies. Not a VAT matter.

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
Action Required: Licensed accountant must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed accountant. Document gap.
```

---

## Contribution Notes

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all box numbers with the equivalent boxes on your jurisdiction's VAT return form.
3. Replace VAT rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace the capital goods thresholds and adjustment periods with your jurisdiction's equivalents.
5. Replace the registration threshold (EUR 15,600) with your jurisdiction's equivalent.
6. Replace the EU country list with the list relevant to your jurisdiction's trading bloc, if applicable.
7. Replace the blocked categories with your jurisdiction's equivalent non-deductible categories.
8. Have a licensed or warranted accountant in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
