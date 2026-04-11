---
name: norway-mva
description: Use this skill whenever asked to prepare, review, or create a Norway MVA return (MVA-melding) for any client. Trigger on phrases like "prepare MVA return", "do the MVA", "fill in MVA-melding", "create the return", "Norwegian VAT", "merverdiavgift", or any request involving Norway VAT filing. Also trigger when classifying transactions for MVA purposes from bank statements, invoices, or other source data. This skill contains the complete Norway MVA classification rules, MVA-melding post mappings, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines required to produce a correct return. Norway is NOT an EU member state but IS in the EEA. ALWAYS read this skill before touching any Norway MVA-related work.
---

# Norway MVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Norway (Norge) |
| Jurisdiction Code | NO |
| Primary Legislation | Merverdiavgiftsloven (mval.) -- Lov om merverdiavgift, LOV-2009-06-19-58 |
| Supporting Legislation | Merverdiavgiftsforskriften (fmva.); Skatteforvaltningsloven (sktfvl.); Bokforingsloven |
| Tax Authority | Skatteetaten (Norwegian Tax Administration) |
| Filing Portal | https://www.altinn.no (MVA-melding via Altinn) |
| Currency | Norwegian Krone (NOK) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: post assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial deduction apportionment, sector-specific rules, voluntary registration. Tier 3: complex group registrations (fellesregistrering), transfer of business as going concern, Svalbard supplies. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified accountant (statsautorisert revisor or registrert revisor) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Key Jurisdictional Note: Norway, the EU, and the EEA

**Norway is NOT a member of the European Union.** [T1]

Norway is a member of the European Economic Area (EEA) via the EEA Agreement. This means:

- Norway does NOT participate in the EU VAT system (Council Directive 2006/112/EC does not apply).
- There are NO intra-community acquisitions or intra-community supplies in the EU sense.
- There is NO EU VIES system for Norwegian businesses.
- Goods imported from EU countries are treated as imports, subject to Norwegian import VAT (though customs duties are largely eliminated under the EEA Agreement).
- Services received from abroad (both EU and non-EU) are subject to reverse charge under mval. sections 3-30 and 11-3.
- Norway has its own independent MVA legislation: Merverdiavgiftsloven (mval.).

**Legislation:** mval. section 1-1 (scope); EEA Agreement Article 36 (free movement of services).

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and organisation number** [T1] -- 9-digit Norwegian organisation number (organisasjonsnummer), suffixed with "MVA" if registered. Format: 123 456 789 MVA.
2. **MVA registration status** [T1] -- Registered (mandatory or voluntary) or not registered.
3. **MVA period** [T1] -- Bi-monthly (standard), annual (yearly filing for small businesses under NOK 1,000,000 turnover), or weekly (petroleum sector).
4. **Industry/sector** [T2] -- Impacts deductibility and rate classification (e.g., food retail uses 15%, transport uses 12%).
5. **Does the business make exempt supplies?** [T2] -- If yes, proportional deduction (forholdsmessig fradrag) required under mval. section 8-2. Reviewer must confirm apportionment method.
6. **Does the business operate on Svalbard?** [T1] -- Svalbard is outside the MVA territory (mval. section 1-2). Supplies on Svalbard are zero-rated or outside scope.
7. **Does the business import goods?** [T1] -- Import MVA is now reported on the MVA-melding (not to Customs) for most businesses since 2017.
8. **Excess credit brought forward** [T1] -- Tilgode (credit) from prior period.
9. **Is the business part of a fellesregistrering (joint registration)?** [T3] -- Group VAT registration. Escalate to reviewer.

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

**Legislation:** mval. sections 2-1 (registration obligation), 2-3 (voluntary registration), 15-1 (filing obligation).

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Sale (output MVA / utgaende merverdiavgift) or Purchase (input MVA / inngaende merverdiavgift)
- Salaries, employer contributions (arbeidsgiveravgift), tax payments, loan repayments, dividends, bank charges on exempt financial services = OUT OF SCOPE (never on MVA return)
- **Legislation:** mval. section 1-3 (definitions); section 3-1 (taxable supply of goods and services).

### 1b. Determine Counterparty Location [T1]

- **Norway (domestic):** Supplier/customer located in Norwegian MVA territory (mainland Norway and Norwegian continental shelf, excluding Svalbard and Jan Mayen).
- **Foreign:** ALL countries outside Norway, including EU member states. Norway treats EU and non-EU identically for MVA purposes -- both are "utlandet" (abroad).
- **Svalbard / Jan Mayen:** Outside MVA territory. Treated similarly to export/import. See mval. section 1-2.

**Critical difference from EU states:** There is no distinction between "EU supplier" and "non-EU supplier" in Norwegian MVA law. All foreign suppliers are treated the same way.

**Legislation:** mval. section 1-2 (territorial scope).

### 1c. Determine MVA Rate [T1]

| Rate | Category | Legislation |
|------|----------|-------------|
| 25% | Standard rate (alminnelig sats) -- all goods and services not qualifying for reduced rate or exemption | mval. section 5-1 |
| 15% | Reduced rate (redusert sats) -- foodstuffs (naeringsmidler), excluding alcohol, tobacco, water from waterworks | mval. section 5-2 |
| 12% | Low rate (lav sats) -- domestic passenger transport, hotel/accommodation, cinema tickets, museum/gallery admission, amusement parks, sports events, broadcasting fees | mval. section 5-3, section 5-4, section 5-5 |
| 11.11% | Wild marine resources rate -- sales of wild-caught fish and certain marine resources (effective 1 January 2025) | mval. section 5-2a |
| 0% | Zero-rated (nullsats / fritatt med fradragsrett) -- exports, international transport, supplies to Svalbard/Jan Mayen, certain offshore supplies, electric vehicles (conditions apply; phase-out from 2026) | mval. section 6-1 to 6-39 |
| Exempt | Exempt without credit (unntatt) -- financial services, healthcare, education, real estate sales/rental, cultural services (certain), social services | mval. section 3-2 to 3-20 |

### 1d. Determine Expense Category [T1]

- **Operating expenses (driftsutgifter):** General overhead, services, consumables.
- **Capital goods (kapitalvarer):** Property: acquisition cost >= NOK 100,000 excl. MVA (mval. section 9-1(2)(b)). Machinery/equipment: acquisition cost >= NOK 50,000 excl. MVA (mval. section 9-1(2)(a)). Adjustment period: 5 years for movables, 10 years for real property.
- **Goods for resale (varer for videresalg):** Goods purchased to resell without transformation.

**Legislation:** mval. section 9-1 (capital goods scheme / justeringsreglene).

---

## Step 2: MVA-melding Post Assignment [T1]

The Norwegian MVA-melding uses numbered "posts" (codes). Since 2022, the modernised MVA-melding replaced the old RF-0002 form. The new format uses standardised SAF-T codes.

**Legislation:** Skatteforvaltningsforskriften section 8-3; Skatteetaten guidance on MVA-melding.

### Output MVA (Utgaende merverdiavgift) -- Sales

| Post Code | Description | Rate | Use |
|-----------|-------------|------|-----|
| 3 | Domestic sales, standard rate | 25% | All standard-rated domestic sales |
| 31 | Domestic sales, reduced rate (food) | 15% | Sales of foodstuffs |
| 32 | Domestic sales, low rate | 12% | Passenger transport, accommodation, cinema, etc. |
| 33 | Domestic sales, zero-rated | 0% | Zero-rated domestic supplies |
| 5 | Domestic sales, exempt | Exempt | Exempt supplies (no output MVA, no input deduction) |
| 52 | Export of goods and services | 0% | Exports outside Norway |
| 51 | Sales to Svalbard/Jan Mayen | 0% | Supplies to territories outside MVA area |

### Output MVA on Purchases (Reverse Charge / Self-Assessment)

| Post Code | Description | Rate | Use |
|-----------|-------------|------|-----|
| 81 | Purchase of goods from abroad (import) | 25% | Import of physical goods, standard rate |
| 82 | Purchase of goods from abroad (import) | 15% | Import of foodstuffs |
| 83 | Purchase of services from abroad (reverse charge) | 25% | Services received from foreign suppliers |
| 84 | Purchase of goods from abroad, low rate | 12% | Import of goods at low rate |
| 85 | Purchase of services from abroad, low rate | 12% | Services from abroad at low rate |
| 86 | Purchase of emission allowances and gold | 25% | Domestic reverse charge on emissions/gold |
| 87 | Purchase of goods from abroad, zero-rated | 0% | Informational only, no MVA |
| 88 | Purchase of services from abroad, zero-rated | 0% | Informational only, no MVA |
| 89 | Purchase of climate quotas/gold, zero-rated | 0% | Informational only |
| 91 | Purchase of goods from abroad with deduction right | 25% | Import MVA deductible portion (input side) |
| 92 | Purchase of goods from abroad with deduction right | 15% | Import MVA deductible portion, food rate |

### Input MVA (Inngaende merverdiavgift) -- Deductible Purchases

| Post Code | Description | Rate | Use |
|-----------|-------------|------|-----|
| 1 | Input MVA, standard rate (domestic) | 25% | Deductible input on domestic purchases at 25% |
| 11 | Input MVA, reduced rate (domestic) | 15% | Deductible input on domestic food purchases |
| 12 | Input MVA, low rate (domestic) | 12% | Deductible input on domestic purchases at 12% |
| 13 | Input MVA, standard rate (import) | 25% | Deductible input on imported goods at 25% |
| 14 | Input MVA, reduced rate (import) | 15% | Deductible input on imported goods at 15% |
| 15 | Input MVA, low rate (import) | 12% | Deductible input on imported goods at 12% |

### Summary Calculation

```
Total output MVA = Sum of MVA on posts 3, 31, 32, 81, 82, 83, 84, 85, 86
Total input MVA  = Sum of MVA on posts 1, 11, 12, 13, 14, 15
MVA payable      = Total output MVA - Total input MVA
If negative      = Tilgode (refund / credit to be carried forward or refunded)
```

**Legislation:** mval. sections 11-1 (output MVA), 8-1 (input MVA deduction right).

---

## Step 3: Reverse Charge Mechanics [T1]

Norway applies reverse charge (snudd avregning / omvendt avgiftsplikt) in two main scenarios:

### 3a. Services Purchased from Abroad (mval. section 3-30)

When a Norwegian MVA-registered business purchases services from a foreign supplier that would be taxable if supplied in Norway:

1. The Norwegian buyer self-assesses output MVA at the applicable rate (usually 25%).
2. Report the purchase amount in Post 83 (standard rate) or Post 85 (low rate).
3. Claim corresponding input MVA in Post 1 (if fully deductible) at the same rate.
4. Net effect: zero for fully taxable businesses.

**Legislation:** mval. section 3-30 (reverse charge on imported services); section 11-3 (calculation of reverse charge MVA).

### 3b. Import of Goods (mval. sections 3-29, 11-11)

Since 1 January 2017, import MVA on goods is reported on the MVA-melding (not paid to Customs at the border) for businesses registered for MVA:

1. Report the customs value + duty in Post 81 (25%), Post 82 (15%), or Post 84 (12%).
2. Claim input MVA in Post 13 (25%), Post 14 (15%), or Post 15 (12%).
3. Net effect: zero for fully taxable businesses.

**Non-registered importers** still pay import MVA to Customs (Tolletaten).

**Legislation:** mval. section 11-11 (import MVA on MVA-melding); Tolloven (Customs Act).

### 3c. Domestic Reverse Charge (mval. section 11-1(3))

Applies to:
- Emission allowances (klimakvoter) -- Post 86
- Gold sold between dealers -- Post 86

**Legislation:** mval. section 11-1(3) (domestic reverse charge).

### 3d. Exceptions to Reverse Charge [T1]

- Out-of-scope categories (wages, dividends, bank charges on exempt services): NEVER reverse charge.
- Services consumed locally abroad (hotel, restaurant, taxi abroad): NOT reverse charge -- foreign VAT paid at source is an irrecoverable cost.
- If the foreign supplier has voluntarily registered for Norwegian MVA and charges Norwegian MVA: NOT reverse charge -- treat as domestic purchase.

---

## Step 4: Deductibility Check

### 4a. Blocked Input MVA (Fradragsbegrensninger) [T1]

**Legislation:** mval. section 8-3 (limitations on deduction right); section 8-4 (motor vehicles).

The following categories have FULL BLOCK on input MVA recovery:

| Category | Legislation | Notes |
|----------|-------------|-------|
| Passenger motor vehicles (personkjoretoy) | mval. section 8-4(1) | Includes cars, minibuses with < 10 seats. FULL BLOCK. Exception: taxi, driving school, car rental, funeral vehicles. |
| Entertainment and social events (representasjon) | mval. section 8-3(1)(d) | Restaurant meals for business entertainment, gifts to clients, social events. See 50% rule below for food/drink. |
| Cost of food and drink for employees | mval. section 8-3(1)(e) | Staff meals, canteen costs. NO deduction. |
| Art and antiques | mval. section 8-3(1)(c) | Unless the business is an art dealer. |
| Gifts and free samples | mval. section 8-3(1)(a) | Gifts without consideration. |
| Accommodation for owner/employees (bolig) | mval. section 8-3(1)(b) | Private housing, holiday cabins (hytter). |

### 4b. The 50% Rule for Business Entertainment (Servering) [T1]

**Legislation:** mval. section 8-3(1)(d); fmva. section 8-3-1.

For food and drink (servering) at business meetings where external parties attend and a clear business purpose exists, **50% of input MVA is deductible** -- but ONLY if:
- The meal is in connection with negotiations or meetings with external business contacts.
- The cost is properly documented with names of attendees and business purpose.
- The supply is food/drink (not general entertainment like tickets, shows, etc.).

**If the meal is purely internal (staff only), NO deduction at all under mval. section 8-3(1)(e).**

**If the meal is pure client entertainment without business negotiations, NO deduction under mval. section 8-3(1)(d).**

### 4c. Motor Vehicle Rules (Detailed) [T1]

**Legislation:** mval. section 8-4; fmva. sections 8-4-1 to 8-4-3.

| Vehicle Type | Input MVA Deduction | Condition |
|-------------|-------------------|-----------|
| Passenger car (personbil) | BLOCKED -- 0% | Full block on purchase, lease, and running costs including fuel, repairs, insurance |
| Commercial vehicle (varebil klasse 2) | FULL deduction -- 100% | Must be classified as varebil klasse 2 in vehicle registry. Business use required. |
| Truck (lastebil) | FULL deduction -- 100% | Used in MVA-liable business. |
| Taxi (drosjebil) | FULL deduction -- 100% | Registered as taxi. |
| Driving school vehicle (opplaeringskjoretoy) | FULL deduction -- 100% | Registered for driving instruction. |
| Car rental vehicle (utleiebil) | FULL deduction -- 100% | Owned by licensed car rental business. |
| Minibus >= 10 seats | FULL deduction -- 100% | Passenger transport business. |
| Electric vehicle (elbil) used as passenger car | BLOCKED -- 0% | Same rules as petrol/diesel passenger car for MVA purposes. |
| Fuel for blocked passenger car | BLOCKED -- 0% | Follows vehicle classification. |
| Fuel for deductible commercial vehicle | FULL deduction -- 100% | Follows vehicle classification. |
| Repairs/maintenance on passenger car | BLOCKED -- 0% | Follows vehicle classification. |
| Repairs/maintenance on commercial vehicle | FULL deduction -- 100% | Follows vehicle classification. |

**Critical rule:** The classification of the vehicle determines the deductibility of ALL associated costs (fuel, repairs, insurance, parking). If the vehicle is blocked, ALL costs are blocked. [T1]

**Legislation:** mval. section 8-4(2) (associated costs follow vehicle classification).

### 4d. Proportional Deduction (Forholdsmessig fradrag) [T2]

**Legislation:** mval. section 8-2; fmva. sections 8-2-1 to 8-2-3.

If a business makes both taxable and exempt supplies, input MVA must be apportioned:

```
Recovery % = (Taxable supplies / Total supplies) * 100
```

Round to nearest whole percentage. If taxable portion is >= 95%, full deduction is allowed. If taxable portion is <= 5%, no deduction is allowed.

**Flag for reviewer: apportionment method and ratio must be confirmed by qualified accountant before applying.**

### 4e. Capital Goods Adjustment (Justeringsreglene) [T2]

**Legislation:** mval. sections 9-1 to 9-14.

Capital goods are subject to adjustment of input MVA over:
- **5 years** for machinery/movables (driftsmidler) with acquisition cost >= NOK 50,000 excl. MVA.
- **10 years** for real property (fast eiendom) with acquisition cost >= NOK 100,000 excl. MVA.

If use changes between taxable and exempt activities during the adjustment period, input MVA must be adjusted (up or down) proportionally for each remaining year.

**Flag for reviewer: capital goods adjustment calculations must be confirmed by qualified accountant.**

---

## Step 5: MVA Rates -- Complete Classification Matrix [T1]

### Standard Rate -- 25% (mval. section 5-1)

| Supply | Rate | Notes |
|--------|------|-------|
| General goods | 25% | Default for all goods not otherwise classified |
| General services | 25% | Default for all services not otherwise classified |
| Construction services | 25% | Including materials |
| Professional services (legal, consulting, accounting) | 25% | |
| IT services and software | 25% | Including SaaS |
| Telecommunications | 25% | |
| Electricity and energy | 25% | |
| Clothing and textiles | 25% | |
| Electronics | 25% | |
| Furniture | 25% | |
| Alcohol (served or retail) | 25% | NOT food rate even if consumed with food |
| Tobacco | 25% | NOT food rate |
| Water from waterworks | 25% | Explicitly excluded from food rate per mval. section 5-2 |

### Reduced Rate -- 15% (mval. section 5-2)

| Supply | Rate | Notes |
|--------|------|-------|
| Foodstuffs (naeringsmidler) | 15% | All food for human consumption |
| Non-alcoholic beverages | 15% | Juice, soft drinks, coffee, tea |
| Takeaway food | 15% | Food sold for takeaway; note: restaurant dining is also 15% |
| Restaurant food (not alcohol) | 15% | The food component of a restaurant bill |
| Catering services (food component) | 15% | Food portion only; service portion may be 25% if separately invoiced |
| Animal feed | 15% | Feed for food-producing animals |
| Water and sewage services | 15% | From 1 July 2025 per mval. section 5-2 amendment |

**From 1 July 2025:** Water and sewage services are included in the 15% rate per mval. section 5-2 amendment.

**Exclusions from 15% rate:** Alcohol, tobacco, medicines/pharmaceuticals, dietary supplements classified as medicine.

### Wild Marine Resources Rate -- 11.11% (mval. section 5-2a, effective 1 January 2025)

| Supply | Rate | Notes |
|--------|------|-------|
| Wild-caught fish (fresh, chilled, frozen) | 11.11% | Wild marine resources only |
| Other wild marine resources | 11.11% | As specified by mval. section 5-2a |

**Note:** This rate applies specifically to sales of wild-caught marine resources. Farmed fish (e.g., salmon from aquaculture) remains at 15% as a foodstuff.

### Low Rate -- 12% (mval. section 5-3, 5-4, 5-5)

| Supply | Rate | Legislation |
|--------|------|-------------|
| Domestic passenger transport | 12% | mval. section 5-3 |
| Domestic ferry transport of vehicles | 12% | mval. section 5-3 |
| Hotel/accommodation (overnatting) | 12% | mval. section 5-5 |
| Cinema tickets | 12% | mval. section 5-4 |
| Museum admission | 12% | mval. section 5-4 |
| Gallery admission | 12% | mval. section 5-4 |
| Amusement park admission | 12% | mval. section 5-4 |
| Sports event admission | 12% | mval. section 5-4 |
| Broadcasting licence (NRK-lisens) | 12% | mval. section 5-4 (historical; NRK licence abolished 2020, replaced by tax) |
| Camping and cabin rental | 12% | mval. section 5-5 |
| Ski lift tickets | 12% | mval. section 5-4 (amusement/activity) |

### Zero-Rated -- 0% with Deduction Right (mval. chapter 6)

| Supply | Legislation | Notes |
|--------|-------------|-------|
| Export of goods | mval. section 6-21 | Goods shipped out of Norway |
| Export of services | mval. section 6-22 | Services supplied to foreign recipients and consumed abroad |
| International transport | mval. section 6-28 | Transport of goods/passengers across Norwegian border |
| Supplies to Svalbard/Jan Mayen | mval. section 6-24 | Treated as export |
| Supplies to Norwegian continental shelf | mval. section 6-32 | Petroleum-related supplies |
| Sale of newspapers (print) | mval. section 6-1 | Physical newspapers |
| Sale of electronic news services | mval. section 6-2 | Digital newspapers/news, from 2016 |
| Sale of books (print and e-books) | mval. section 6-3 | From 2019 for e-books |
| Electric vehicles | mval. section 6-7 | Phase-out: from 1 Jan 2026 MVA applies on purchase price exceeding NOK 300,000; from 2027 exceeding NOK 150,000; full phase-out 2028 [T2] confirm current thresholds |

### Exempt Without Credit (Unntatt -- mval. chapter 3)

| Supply | Legislation | Notes |
|--------|-------------|-------|
| Financial services | mval. section 3-6 | Banking, insurance, securities trading |
| Healthcare services | mval. section 3-2 | Medical, dental, physiotherapy |
| Education services | mval. section 3-5 | Schools, universities, courses |
| Real estate rental/sale | mval. section 3-11 | With option for voluntary registration (mval. section 2-3) |
| Social services | mval. section 3-4 | Care services, kindergartens |
| Cultural services (certain) | mval. section 3-7 | Performing arts, concerts (artist fees) |
| Lottery/gambling | mval. section 3-14 | |
| Funeral services | mval. section 3-15 | |

---

## Step 6: Registration Rules

### 6a. Mandatory Registration (mval. section 2-1) [T1]

A business MUST register for MVA when:
- Taxable turnover (omsetning) exceeds **NOK 50,000** in a 12-month period.
- The 12-month period is rolling, not calendar year.

**Legislation:** mval. section 2-1(1).

### 6b. Special Thresholds [T1]

| Entity Type | Threshold | Legislation |
|------------|-----------|-------------|
| Standard business | NOK 50,000 | mval. section 2-1(1) |
| Charitable/non-profit organisations (veldedige organisasjoner) | NOK 140,000 | mval. section 2-1(1) second sentence |

### 6c. Voluntary Registration (mval. section 2-3) [T2]

Businesses below the threshold or making exempt supplies may voluntarily register in certain cases:
- **Property rental to MVA-registered tenants:** mval. section 2-3(1) -- landlord can opt to charge MVA on commercial rent to recover input MVA on property costs.
- **Forestry and agriculture:** mval. section 2-3(3).
- **Foreign businesses with no place of business in Norway:** mval. section 2-3(5) -- via tax representative (avgiftsrepresentant).

**Flag for reviewer: voluntary registration decisions have significant commercial implications. Confirm with qualified accountant.**

### 6d. VOEC Scheme (VAT on E-Commerce) [T1]

**Legislation:** mval. section 14-4 to 14-7; fmva. chapter 14.

Non-resident suppliers selling the following B2C to Norwegian consumers must register under the simplified VOEC scheme:
- Electronic services (e-tjenester)
- Remotely deliverable services
- Low-value goods (goods with value <= NOK 3,000 per consignment)

VOEC registration:
- No Norwegian tax representative required.
- Quarterly MVA filing.
- No right to deduct Norwegian input MVA.
- Report output MVA at the applicable rate (25%, 15%, or 12%).

**This scheme is for non-resident suppliers only. Norwegian businesses use standard registration.**

### 6e. Tax Representative (Avgiftsrepresentant) [T1]

**Legislation:** mval. section 2-1(6); fmva. section 2-1-1.

Foreign businesses registered for Norwegian MVA that do not have a place of business in Norway must appoint a Norwegian tax representative (avgiftsrepresentant) who is jointly liable for the MVA. EEA-based businesses may be exempt from the representative requirement since 2021.

---

## Step 7: Filing Deadlines and Penalties

### 7a. Filing Periods [T1]

| Period Type | Who | Period Months | Legislation |
|------------|-----|---------------|-------------|
| Bi-monthly (standard) | Most businesses | Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct, Nov-Dec | mval. section 15-1; sktfvl. section 8-3 |
| Annual (arlig) | Businesses with turnover < NOK 1,000,000 | Jan-Dec | sktfvl. section 8-3(4) |
| Weekly | Petroleum sector (certain) | Weekly | sktfvl. section 8-3 |

### 7b. Filing Deadlines [T1]

| Period Type | Deadline | Notes |
|------------|----------|-------|
| Bi-monthly | 1 month + 10 days after period end | E.g., Jan-Feb period due 10 April; Mar-Apr period due 10 June |
| Bi-monthly (3rd period, May-Jun) | 31 August | Extended summer deadline |
| Annual | 10 March following year | Annual filers |

**Specific bi-monthly deadlines:**

| Period | Months | Deadline |
|--------|--------|----------|
| 1st termin | January -- February | 10 April |
| 2nd termin | March -- April | 10 June |
| 3rd termin | May -- June | 31 August (extended) |
| 4th termin | July -- August | 10 October |
| 5th termin | September -- October | 10 December |
| 6th termin | November -- December | 10 February (following year) |

**Legislation:** sktfvl. section 8-3; skatteforvaltningsforskriften section 8-3-10.

### 7c. Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing (forsinket levering) | Tvangsmulkt (coercive fine): NOK 524 per day (2025 rate), up to a maximum. Starts after a reminder is sent. | sktfvl. section 14-1 |
| Late payment (forsinket betaling) | Forsinkelsesrente (late payment interest) at a rate set by Finansdepartementet (currently ~10.75% annually). | Forsinkelsesrenteloven |
| Incorrect return (uriktig oppgave) | Tilleggsskatt (additional tax): 20% of the underpaid MVA as standard rate; 40% for gross negligence; 60% for intentional evasion. | sktfvl. section 14-3 to 14-6 |
| Failure to register | Etterberegning (reassessment) of MVA for the entire unregistered period + tilleggsskatt. | sktfvl. section 12-1 |

### 7d. Refund Processing [T1]

- If the MVA-melding shows tilgode (credit), Skatteetaten normally refunds within 3 weeks of filing.
- Skatteetaten may withhold refund pending review (kontroll). Common triggers: large refunds, first filing, unusual patterns.
- Annual filers receive refund after 10 March deadline processing.

**Legislation:** sktfvl. section 9-3 (refund of excess input MVA).

---

## Step 8: MVA-melding Structure (Modernised Format from 2022) [T1]

The modernised MVA-melding is filed electronically via Altinn in SAF-T XML format. The key data points are:

### Output MVA Section

| Post | Description | Base (NOK) | Rate | MVA Amount |
|------|-------------|-----------|------|------------|
| 3 | Domestic sales, standard | Net turnover | 25% | Calculated |
| 31 | Domestic sales, food | Net turnover | 15% | Calculated |
| 32 | Domestic sales, low rate | Net turnover | 12% | Calculated |
| 33 | Domestic sales, zero-rated | Net turnover | 0% | 0 |
| 5 | Exempt sales | Net turnover | N/A | N/A |
| 51 | Sales to Svalbard/Jan Mayen | Net turnover | 0% | 0 |
| 52 | Export | Net turnover | 0% | 0 |
| 6 | Withdrawal (uttak) standard | Net value | 25% | Calculated |
| 81 | Import of goods, standard | Customs value | 25% | Calculated |
| 82 | Import of goods, food | Customs value | 15% | Calculated |
| 83 | Services from abroad, standard | Net value | 25% | Calculated |
| 84 | Import of goods, low rate | Customs value | 12% | Calculated |
| 85 | Services from abroad, low rate | Net value | 12% | Calculated |
| 86 | Domestic reverse charge (emissions/gold) | Net value | 25% | Calculated |

### Input MVA Section

| Post | Description | MVA Amount |
|------|-------------|------------|
| 1 | Domestic purchases, standard (25%) | Deductible MVA |
| 11 | Domestic purchases, food (15%) | Deductible MVA |
| 12 | Domestic purchases, low rate (12%) | Deductible MVA |
| 13 | Import of goods, standard (25%) | Deductible MVA |
| 14 | Import of goods, food (15%) | Deductible MVA |
| 15 | Import of goods, low rate (12%) | Deductible MVA |

### Summary

```
Total output MVA = MVA on posts 3 + 31 + 32 + 6 + 81 + 82 + 83 + 84 + 85 + 86
Total input MVA  = Posts 1 + 11 + 12 + 13 + 14 + 15
MVA to pay       = Total output MVA - Total input MVA
If negative      = Tilgode (refund)
```

**Legislation:** sktfvl. section 8-3; Skatteetaten technical specification for MVA-melding.

---

## Step 9: Comparison with EU VAT System

Since Norway is often confused with EU countries, this section clarifies key differences. [T1]

| Feature | EU VAT (Directive 2006/112/EC) | Norway MVA (mval.) |
|---------|-------------------------------|-------------------|
| Legal basis | EU VAT Directive, transposed into national law | Independent national legislation (mval.) |
| Standard rate range | 15% minimum, varies by country (17-27%) | Fixed at 25% (mval. section 5-1) |
| Intra-community supplies | Zero-rated with VIES reporting | Does not exist; EU is "abroad" |
| Intra-community acquisitions | Self-assessed by buyer; reported on VAT return | Does not exist; treated as import |
| VIES / EC Sales List | Required for cross-border B2B | Not applicable |
| Import VAT reporting | Varies; some countries postponed accounting | On MVA-melding since 2017 for registered businesses |
| Reverse charge on services | Article 196 of Directive; B2B services from abroad | mval. section 3-30; all foreign services |
| OSS/IOSS schemes | One-Stop-Shop for B2C cross-border | Not applicable; VOEC is independent Norwegian scheme |
| Fiscal representative | Varies by country | Required for non-EEA businesses (mval. section 2-1(6)) |
| Group registration | Varies | Fellesregistrering (mval. section 2-2(3)) |
| Filing frequency | Varies (monthly, quarterly, annual) | Bi-monthly standard; annual for small businesses |
| Filing portal | Country-specific | Altinn (altinn.no) |
| Capital goods adjustment | Directive Article 184-192 | mval. sections 9-1 to 9-14; 5yr movables, 10yr property |

**Key practical implication:** When a Norwegian business trades with an EU business, BOTH sides treat it as an export/import. The EU business does NOT report it as an intra-community transaction.

---

## Step 10: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- Hotel stay in another country (business trip) [T1]

**Situation:** Norwegian MVA-registered business pays for a hotel in Sweden. Invoice shows Swedish moms (12%).
**Resolution:** NOT reverse charge. The accommodation was consumed in Sweden. Swedish VAT was charged and paid at source. Treat as an operating expense at gross amount. The Swedish VAT is an irrecoverable cost. No entry on the Norwegian MVA-melding.
**Legislation:** mval. section 3-30 applies only to services that would be taxable in Norway if supplied here; place of supply for hotel is where the property is located.

### EC2 -- SaaS subscription from US provider (e.g., Notion, Slack) [T1]

**Situation:** Monthly subscription to a US-based SaaS platform. No MVA on invoice.
**Resolution:** Reverse charge applies. The service is an electronic service consumed in Norway. Report in Post 83 (output, 25%) and claim in Post 1 (input, 25%). Net effect: zero for fully taxable business.
**Legislation:** mval. section 3-30 (imported services); section 11-3(1).

### EC3 -- Purchase of foodstuffs from Swedish supplier (physical goods) [T1]

**Situation:** Restaurant in Norway imports food ingredients from Sweden. No Norwegian MVA on invoice.
**Resolution:** This is an import of goods. Report in Post 82 (output at 15% food rate) and claim in Post 14 (input at 15%). Net effect: zero. Note: may also require customs declaration depending on product type.
**Legislation:** mval. section 3-29 (import of goods); section 5-2 (food rate).

### EC4 -- Passenger car purchase or lease [T1]

**Situation:** Business purchases a car classified as "personbil" for employee use.
**Resolution:** Input MVA is FULLY BLOCKED under mval. section 8-4(1). The 25% MVA is a cost. This applies to purchase, lease payments, fuel, repairs, insurance, and parking. No deduction in Post 1 or any other input post. Report gross cost as operating expense.
**Legislation:** mval. section 8-4(1) (passenger vehicles); section 8-4(2) (associated costs).

### EC5 -- Commercial vehicle (varebil klasse 2) [T1]

**Situation:** Business purchases a van classified as "varebil klasse 2" in the vehicle registry.
**Resolution:** Input MVA is FULLY DEDUCTIBLE. Report MVA in Post 1 (25%). All associated costs (fuel, repairs, insurance) also deductible. The vehicle must be registered as varebil klasse 2 -- check vehicle registration certificate (vognkort).
**Legislation:** mval. section 8-4(1) -- exception for commercial vehicles.

### EC6 -- Business entertainment at restaurant with client [T1]

**Situation:** Lunch meeting with a client to discuss a contract. Restaurant bill NOK 2,000 + NOK 300 MVA (15% food rate).
**Resolution:** 50% of input MVA is deductible = NOK 150. Must document: names of attendees, company names, business purpose. Report NOK 150 in Post 11 (input MVA at 15%). The remaining NOK 150 is a blocked cost.
**Legislation:** mval. section 8-3(1)(d); fmva. section 8-3-1.

### EC7 -- Svalbard supply [T1]

**Situation:** Norwegian mainland business sells goods to a customer on Svalbard.
**Resolution:** Zero-rated. Svalbard is outside the MVA territory. Report in Post 51 (sales to Svalbard/Jan Mayen). No output MVA. Full input MVA deduction on related costs is maintained (same as export).
**Legislation:** mval. section 1-2 (territorial scope); section 6-24 (zero-rating for Svalbard).

### EC8 -- Credit note received from supplier [T1]

**Situation:** Supplier issues a credit note for returned goods or price adjustment.
**Resolution:** Reverse the original entry. If original purchase was in Post 1 at 25%, reduce Post 1 by the MVA on the credit note. Report negative amount in the same post. Do not create entries in different posts.
**Legislation:** mval. section 18-3 (adjustment of incorrectly charged MVA).

### EC9 -- Freelancer providing services to foreign client [T1]

**Situation:** Norwegian freelancer invoices a German company for consulting services.
**Resolution:** Zero-rated export of services. Report in Post 52 (export). No output MVA. The freelancer maintains full input MVA deduction rights on business costs. The German buyer will reverse charge in their German VAT return.
**Legislation:** mval. section 6-22 (export of services); section 6-22(1) (B2B services to recipient abroad).

### EC10 -- Voluntary registration for commercial property rental [T2]

**Situation:** Landlord rents office space to MVA-registered tenants. Rental income is normally exempt (mval. section 3-11).
**Resolution:** Landlord can apply for frivillig registrering (voluntary registration) under mval. section 2-3(1). Once registered, landlord charges 25% MVA on rent and can deduct input MVA on property costs (construction, maintenance, utilities). Tenants must be MVA-registered, or the specific rental area must be used in MVA-liable activity. Partial deduction applies if some tenants are not MVA-registered.
**Flag for reviewer: voluntary registration assessment requires detailed review of tenant mix and lease terms.**
**Legislation:** mval. section 2-3(1) (voluntary registration for property rental).

### EC11 -- Mixed-use asset (partly business, partly private) [T2]

**Situation:** Business purchases equipment used 60% for taxable business and 40% for private/exempt use.
**Resolution:** Only 60% of input MVA is deductible. Apply proportional deduction under mval. section 8-2. If the asset qualifies as a capital good (>= NOK 50,000), the justeringsreglene (adjustment rules) apply over the 5-year period if usage changes.
**Flag for reviewer: confirm usage split and whether capital goods adjustment applies.**
**Legislation:** mval. section 8-2 (proportional deduction); section 9-1 (capital goods adjustment).

### EC12 -- Foreign supplier charges Norwegian MVA [T1]

**Situation:** A Swedish supplier invoices a Norwegian business and charges 25% Norwegian MVA.
**Resolution:** If the Swedish supplier is registered for Norwegian MVA (standard or voluntary registration), treat as a domestic purchase. Report input MVA in Post 1. Do NOT apply reverse charge. Verify the supplier's Norwegian MVA number is valid on Skatteetaten's register.
**Legislation:** mval. section 2-1 (registration); domestic supply rules apply if supplier is NO-registered.

### EC13 -- Withdrawal for private use (uttak) [T1]

**Situation:** Business owner takes inventory goods for personal use.
**Resolution:** Self-assess output MVA on the market value of the goods. Report in Post 6 (withdrawal at applicable rate). This is treated as a deemed sale.
**Legislation:** mval. section 3-21 (withdrawal of goods); section 3-22 (withdrawal of services).

### EC14 -- Digital services sold B2C to Norwegian consumers by foreign supplier [T1]

**Situation:** A US company sells streaming subscriptions to Norwegian private consumers.
**Resolution:** The US company must register under the VOEC scheme and charge 25% Norwegian MVA. The Norwegian consumer pays the MVA-inclusive price. The VOEC-registered supplier files quarterly MVA returns via the simplified portal. No input MVA deduction is available under VOEC.
**Legislation:** mval. section 14-4 to 14-7 (VOEC scheme).

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Qualified accountant (statsautorisert/registrert revisor) must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified accountant. Document gap.
```

---

## Step 12: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard domestic purchase, 25% MVA [T1]

**Input:** Norwegian supplier, office furniture, gross NOK 12,500, MVA NOK 2,500, net NOK 10,000, not resale, registered business.
**Expected output:** Post 1 = NOK 2,500 (input MVA). Full deduction.

### Test 2 -- Import of goods from China, standard rate [T1]

**Input:** Chinese supplier, electronics components, customs value NOK 50,000 (including duty), no MVA on invoice.
**Expected output:** Post 81 base = NOK 50,000, MVA = NOK 12,500 (25%). Post 13 = NOK 12,500 (input MVA). Net effect = zero.

### Test 3 -- Reverse charge on imported service (SaaS) [T1]

**Input:** US supplier (AWS), monthly cloud hosting NOK 8,000, no MVA on invoice.
**Expected output:** Post 83 base = NOK 8,000, MVA = NOK 2,000 (25%). Post 1 = NOK 2,000 (input MVA). Net effect = zero.

### Test 4 -- Food purchase by restaurant, domestic supplier [T1]

**Input:** Norwegian food wholesaler, ingredients, gross NOK 11,500, MVA NOK 1,500 (15%), net NOK 10,000.
**Expected output:** Post 11 = NOK 1,500 (input MVA at 15%). Full deduction.

### Test 5 -- Domestic passenger transport sale [T1]

**Input:** Bus company sells tickets, net revenue NOK 100,000, MVA at 12%.
**Expected output:** Post 32 base = NOK 100,000, MVA = NOK 12,000 (12% output MVA).

### Test 6 -- Export of goods [T1]

**Input:** Norwegian manufacturer ships goods to UK customer, invoice NOK 500,000, no MVA charged.
**Expected output:** Post 52 = NOK 500,000 (export, zero-rated). No output MVA. Full input MVA deduction maintained on related costs.

### Test 7 -- Passenger car purchase, blocked [T1]

**Input:** Business purchases a Toyota Corolla (personbil), NOK 400,000 + MVA NOK 100,000 (25%).
**Expected output:** Post 1 = NOK 0. MVA BLOCKED. Total cost to business = NOK 500,000 gross. No deduction.

### Test 8 -- Commercial vehicle purchase, deductible [T1]

**Input:** Business purchases a Ford Transit (varebil klasse 2), NOK 350,000 + MVA NOK 87,500 (25%).
**Expected output:** Post 1 = NOK 87,500 (input MVA). Full deduction. Capital goods scheme applies (>= NOK 50,000).

### Test 9 -- Business entertainment, 50% deductible [T1]

**Input:** Lunch with client, restaurant in Oslo, NOK 3,000 + MVA NOK 450 (15%), external client present, business purpose documented.
**Expected output:** Post 11 = NOK 225 (50% of NOK 450). Remaining NOK 225 is blocked cost.

### Test 10 -- Sale to Svalbard [T1]

**Input:** Norwegian mainland business sells equipment to Svalbard-based customer, NOK 200,000.
**Expected output:** Post 51 = NOK 200,000 (zero-rated). No output MVA. Input MVA on related costs fully deductible.

### Test 11 -- Voluntary property registration, mixed tenants [T2]

**Input:** Landlord voluntarily registered. Building has 3 floors: 2 floors rented to MVA-registered businesses, 1 floor rented to a non-MVA-registered medical clinic (exempt).
**Expected output:** Output MVA charged on 2/3 of rental income (floors to MVA-registered tenants). Input MVA on building costs deductible at 2/3 (proportional). Medical clinic floor: no MVA on rent, no input deduction on that portion.
**Flag:** Reviewer must confirm apportionment method (floor area, revenue, or other).

### Test 12 -- Credit note reversal [T1]

**Input:** Supplier issues credit note for NOK 5,000 + MVA NOK 1,250 (25%) on previously reported purchase.
**Expected output:** Post 1 reduced by NOK 1,250 (negative adjustment to input MVA).

### Test 13 -- Withdrawal for private use [T1]

**Input:** Business owner takes inventory (retail goods) worth NOK 4,000 (net) for personal use.
**Expected output:** Post 6 base = NOK 4,000, MVA = NOK 1,000 (25% output MVA on deemed supply).

---

## PROHIBITIONS [T1]

- NEVER let AI guess MVA post assignment -- it is 100% deterministic from facts.
- NEVER treat Norway as an EU member state. Norway is EEA, NOT EU. There are NO intra-community supplies or acquisitions.
- NEVER apply EU VIES reporting rules to Norwegian businesses.
- NEVER allow input MVA deduction on passenger vehicles (personkjoretoy) unless the vehicle falls within an explicit exception (taxi, driving school, car rental, funeral).
- NEVER allow full deduction on business entertainment -- maximum 50% for qualifying meals, 0% for all other entertainment.
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges on exempt services).
- NEVER apply reverse charge when the foreign supplier has charged Norwegian MVA (verify their Norwegian registration).
- NEVER report supplies to/from Svalbard as domestic supplies -- Svalbard is outside MVA territory.
- NEVER allow VOEC-registered businesses to deduct input MVA -- VOEC is output-only.
- NEVER confuse zero-rated (fritatt med fradragsrett -- input deduction preserved) with exempt (unntatt -- no input deduction).
- NEVER file an annual return for a business with turnover >= NOK 1,000,000 -- they must file bi-monthly.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.
- NEVER classify water from waterworks at the 15% food rate for periods before 1 July 2025 -- it was 25% previously.
- NEVER allow input MVA deduction for a non-registered business -- only MVA-registered businesses can deduct.
- NEVER ignore the capital goods adjustment rules (justeringsreglene) when an asset's use changes between taxable and exempt activities during the adjustment period.

---

## Step 13: Common Norwegian MVA Terminology

| Norwegian Term | English Equivalent | Notes |
|---------------|-------------------|-------|
| Merverdiavgift (MVA) | Value Added Tax (VAT) | Norwegian name for VAT |
| Merverdiavgiftsloven (mval.) | VAT Act | Primary legislation |
| Utgaende merverdiavgift | Output VAT | MVA charged on sales |
| Inngaende merverdiavgift | Input VAT | MVA paid on purchases |
| Omsetning | Turnover / Supply | Taxable supply of goods/services |
| Avgiftspliktig | Taxable / Liable to MVA | Subject to MVA |
| Unntatt | Exempt | Not subject to MVA, no input deduction |
| Fritatt (med fradragsrett) | Zero-rated (with deduction right) | 0% rate but input deduction maintained |
| Snudd avregning | Reverse charge | Buyer self-assesses MVA |
| Tilgode | Credit / Refund | Excess input MVA |
| Termin | Period | Filing period |
| Grunnlag | Base / Taxable amount | Net amount before MVA |
| Fradrag | Deduction | Right to deduct input MVA |
| Justeringsreglene | Adjustment rules | Capital goods scheme |
| Fellesregistrering | Joint/Group registration | Multiple entities as one MVA subject |
| Frivillig registrering | Voluntary registration | Optional MVA registration |
| Avgiftsrepresentant | Tax representative | Required for non-EEA foreign businesses |
| Naeringsmidler | Foodstuffs | Goods qualifying for 15% rate |
| Personkjoretoy | Passenger vehicle | Input MVA blocked |
| Varebil klasse 2 | Commercial vehicle class 2 | Input MVA deductible |
| Uttak | Withdrawal / Deemed supply | Self-supply for private use |
| Tvangsmulkt | Coercive fine | Penalty for late filing |
| Tilleggsskatt | Additional tax / Penalty tax | Penalty for incorrect return |
| Skatteetaten | Tax Administration | Authority administering MVA |
| Altinn | Altinn portal | Electronic filing portal |
| Tolletaten | Customs Administration | Handles customs duties (not MVA for registered businesses) |
| Klimakvoter | Emission allowances | Subject to domestic reverse charge |

---

## Step 14: Annual Cycle Summary [T1]

| Month | Action |
|-------|--------|
| February 10 | File 6th termin MVA-melding (Nov-Dec of previous year) |
| March 10 | File annual MVA-melding (annual filers) |
| April 10 | File 1st termin MVA-melding (Jan-Feb) |
| June 10 | File 2nd termin MVA-melding (Mar-Apr) |
| August 31 | File 3rd termin MVA-melding (May-Jun) -- extended summer deadline |
| October 10 | File 4th termin MVA-melding (Jul-Aug) |
| December 10 | File 5th termin MVA-melding (Sep-Oct) |

---

## 2025-2026 Changes Summary

| Change | Details | Effective |
|--------|---------|-----------|
| 11.11% rate for wild marine resources | New reduced rate for sales of wild-caught fish and certain marine resources | 1 January 2025 |
| Water and sewage services at 15% | Supply of water and sewage services moved from 25% to 15% reduced rate | 1 July 2025 |
| Electric vehicle MVA phase-out begins | MVA applies on purchase price exceeding NOK 300,000 | 1 January 2026 |
| Electric vehicle MVA threshold reduction | MVA applies on purchase price exceeding NOK 150,000 | 1 January 2027 |
| Electric vehicle full MVA | Zero-rating fully abolished | 1 January 2028 |

**Note:** Standard rate (25%), food rate (15%), and low rate (12%) are unchanged for 2025 and 2026.

---

## Contribution Notes (For Adaptation to Other Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all post numbers with the equivalent codes on your jurisdiction's VAT return form.
3. Replace MVA rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace capital goods thresholds (NOK 50,000 movables / NOK 100,000 property) with your jurisdiction's equivalents.
5. Replace the registration threshold (NOK 50,000) with your jurisdiction's equivalent.
6. Determine whether your jurisdiction is EU, EEA, or neither, and adjust cross-border rules accordingly.
7. Replace the blocked categories with your jurisdiction's equivalent non-deductible categories.
8. Have a qualified accountant in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
