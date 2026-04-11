---
name: bulgaria-vat-return
description: Use this skill whenever asked to prepare, review, or create a Bulgaria VAT return (Spravka-deklaratsiya po DDS) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in DDS", "create the return", "Bulgarian VAT", or any request involving Bulgaria VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Bulgaria VAT classification rules, ledger structure, deductibility rules, reverse charge treatment, SAF-T obligations, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Bulgarian VAT-related work.
---

# Bulgaria VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Bulgaria |
| Jurisdiction Code | BG |
| Primary Legislation | Zakon za danak varhu dobavenata stoynost (ZDDS -- VAT Act, as amended) |
| Supporting Legislation | Pravilnik za prilagane na ZDDS (PPZDDS -- Regulations for Application of ZDDS); Tax and Social Security Procedure Code (DOPK); SAF-T Regulation (2025) |
| Tax Authority | Natsionalna agentsiya za prihodite (NRA / NAP -- National Revenue Agency) |
| Filing Portal | https://portal.nra.bg (NRA e-services portal) |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0 |
| Status | validated |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, ledger structure. Tier 2: partial exemption coefficient, mixed-use vehicle apportionment, refund procedures. Tier 3: complex group structures, fiscal representation, special schemes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A certified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and EIK/BULSTAT (company ID) and DDS number** [T1] -- BG + 9/10 digits for EU VIES
2. **VAT registration status** [T1] -- Mandatory registration (turnover > EUR 51,130 in calendar year from 2026; previously BGN 100,000 rolling 12 months), voluntary registration, or non-registered
3. **Filing frequency** [T1] -- ALWAYS monthly in Bulgaria (no quarterly/annual option for VAT returns)
4. **Industry/sector** [T2] -- impacts applicable reduced rates and specific rules (tourism, agriculture)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (koefitsient); reviewer must confirm
6. **SAF-T filing obligation** [T1] -- phased rollout from January 2026 for large enterprises
7. **Excess credit status** [T1] -- Bulgaria has a specific 3-period offset process for VAT credits
8. **Does the business qualify for accelerated refund?** [T1] -- > 30% zero-rated supplies

**If any of items 1-3 are unknown, STOP. Do not classify any transactions.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (danak za nachislyavane -- output VAT / charged tax) or Purchase (danak za prispacane -- input VAT / tax credit)
- Salaries, social contributions (DOO, DZPO, ZO), personal income tax, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** ZDDS Art. 2-12 (taxable transactions), Art. 6 (supply of goods), Art. 9 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Bulgaria (domestic): supplier/customer country is BG
- EU: AT, BE, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else
- **Note:** UK is Non-EU post-Brexit. North Macedonia is Non-EU. Turkey is Non-EU.

### 1c. Determine VAT Rate [T1]

| Rate | Category | Legislation |
|------|----------|-------------|
| 20% | Standard rate -- most goods and services | ZDDS Art. 66(1)(1) |
| 9% | Reduced -- accommodation / hotel services (tourist sector); printed and electronic books and publications; specific baby food and hygiene products | ZDDS Art. 66(2), Annex to Art. 66(2) |
| 0% | Zero-rated -- exports outside EU (Art. 28), intra-EU supplies of goods (Art. 7), international transport (Art. 30-32) | ZDDS Art. 28-37 |
| Exempt with credit | Certain financial intermediation for international clients | ZDDS Art. 46 |
| Exempt without credit | Financial services (Art. 46), insurance (Art. 47), healthcare (Art. 39), education (Art. 41), residential rental first letting (Art. 45), gambling (Art. 48), postal services (Art. 49), land except building plots (Art. 45(1)) | ZDDS Art. 38-50 |

**Note:** The temporary 9% rate on restaurant/catering services and sports facilities expired 31 December 2024 (Art. 66(2) transitional). From 1 January 2025, these are taxed at 20%.

### 1d. Determine Expense Category [T1]
- Capital goods: not specifically defined by threshold in ZDDS; however, immovable property and renovations have a 20-year adjustment period (ZDDS Art. 79(7)), and other goods used for business have a 5-year adjustment (ZDDS Art. 79(3))
- Resale: goods bought to resell
- Overhead/services: everything else
- **Legislation:** ZDDS Art. 79 (adjustment of tax credit)

---

## Step 2: VAT Return and Ledger Structure [T1]

**Legislation:** ZDDS Art. 124-126; PPZDDS.

**Bulgaria is unique in requiring sales and purchase ledgers (dnevnik za pokupkite / dnevnik za prodazhbite) to be submitted with the VAT return.** The return (Spravka-deklaratsiya) summarizes the ledger totals.

### Purchase Ledger (Dnevnik za Pokupkite)

All purchase invoices are recorded with columns for:

| Column | Description |
|--------|-------------|
| 1 | Invoice number |
| 2 | Invoice date |
| 3 | Supplier name |
| 4 | Supplier VAT number |
| 5 | Type of document (invoice, credit note, debit note, customs declaration, protocol) |
| 6 | Taxable base at 20% |
| 7 | VAT at 20% |
| 8 | Taxable base at 9% |
| 9 | VAT at 9% |
| 10 | Taxable base at 0% |
| 11 | Exempt purchases |
| 12 | Intra-EU acquisitions (base) |
| 13 | Self-assessed VAT on intra-EU acquisitions |
| 14 | Import VAT from customs |
| 15 | Whether full or partial tax credit is claimed |
| 16 | Non-deductible purchases (blocked categories) |

### Sales Ledger (Dnevnik za Prodazhbite)

All sales invoices are recorded with columns for:

| Column | Description |
|--------|-------------|
| 1 | Invoice number |
| 2 | Invoice date |
| 3 | Customer name |
| 4 | Customer VAT number |
| 5 | Type of document |
| 6 | Taxable base at 20% |
| 7 | VAT at 20% |
| 8 | Taxable base at 9% |
| 9 | VAT at 9% |
| 10 | Taxable base at 0% (exports) |
| 11 | Intra-EU supplies (base) |
| 12 | Exempt supplies |
| 13 | Self-supply / deemed supply |

### VAT Return Summary (Spravka-Deklaratsiya po DDS)

| Cell | Description | Notes |
|------|-------------|-------|
| 01 | Taxable supplies at 20% -- base | Domestic standard-rated sales |
| 02 | VAT at 20% | Output DDS at 20% |
| 03 | Taxable supplies at 9% -- base | Accommodation, books, baby products |
| 04 | VAT at 9% | Output DDS at 9% |
| 05 | Taxable supplies at 0% -- base (exports) | Zero-rated output |
| 06 | Intra-EU supplies of goods -- base | Report on VIES declaration |
| 07 | Exempt supplies without credit | Financial, insurance, healthcare |
| 08 | Self-supply / deemed supply -- base | Private use, free distributions |
| 09 | VAT on self-supply | At applicable rate |
| 10 | Services supplied to EU (Art. 21(2)) | B2B services, place of supply in customer MS |
| 11 | Intra-EU acquisitions -- base | Reverse charge acquisitions |
| 12 | VAT on intra-EU acquisitions (self-assessed) | At applicable BG rate |
| 13 | Received services from EU -- base (reverse charge) | B2B services from EU |
| 14 | VAT on EU services received | Self-assessed |
| 15 | Domestic reverse charge -- base | Waste, grain, emissions |
| 16 | VAT on domestic reverse charge | Self-assessed |
| 17 | Import of goods -- base | From customs declaration |
| 18 | VAT on imports | Paid to customs or self-assessed |
| 19 | Received services from non-EU -- base | B2B services from non-EU |
| 19a | VAT on non-EU services | Self-assessed |
| 20 | Total output VAT | Sum: 02+04+09+12+14+16+18+19a |
| 30 | Full tax credit (input VAT with right to full deduction) | Domestic purchases with full right |
| 31 | Input VAT on intra-EU acquisitions | Mirrors Cell 12 |
| 32 | Input VAT on EU services received | Mirrors Cell 14 |
| 32a | Input VAT on non-EU services received | Mirrors Cell 19a |
| 33 | Partial tax credit (coefficient-adjusted) | For mixed taxable/exempt businesses |
| 34 | Input VAT on imports | Mirrors Cell 18 |
| 40 | Total input VAT | Sum: 30+31+32+32a+33+34 |
| 41 | Annual coefficient adjustment | In December return only |
| 50 | VAT payable (if Cell 20 > Cell 40) | Pay to NRA |
| 60 | VAT credit (if Cell 40 > Cell 20) | 3-period offset process |
| 70 | Credit from prior period | Brought forward |
| 71 | VAT payable after offset | After applying prior credit |
| 80 | Credit to carry forward / apply for refund | After 3-period offset |

---

## Step 3: Transaction Classification Matrix [T1]

### Purchases -- Domestic (Bulgarian Supplier)

| VAT Rate | Category | Input Cell | Notes |
|----------|----------|------------|-------|
| 20% | Overhead/services (full deduction) | Cell 30 | Standard purchase |
| 9% | Overhead/services (full deduction) | Cell 30 | Accommodation, books |
| 0% | Any | -- | No DDS to claim |
| Any | Capital goods | Cell 30 | 5-year / 20-year adjustment |
| Any | Mixed use (partial) | Cell 33 | Coefficient applied |
| Any | Blocked category | -- | No tax credit |

### Purchases -- EU Supplier (Reverse Charge)

| Type | Output Cell | Input Cell | Notes |
|------|------------|------------|-------|
| Physical goods | Cell 11 / 12 | Cell 31 | Intra-EU acquisition |
| Services (B2B) | Cell 13 / 14 | Cell 32 | EU service RC |
| Out-of-scope (wages etc.) | -- | -- | NEVER reverse charge |
| Local consumption (hotel, restaurant abroad) | -- | -- | Foreign VAT at source |

### Purchases -- Non-EU Supplier

| Type | Output Cell | Input Cell | Notes |
|------|------------|------------|-------|
| Services (B2B) | Cell 19 / 19a | Cell 32a | Non-EU service import |
| Physical goods (customs) | Cell 17 / 18 | Cell 34 | Import via customs declaration |
| Out-of-scope | -- | -- | NEVER reverse charge |

### Sales -- Domestic

| Rate | Cell | Notes |
|------|------|-------|
| 20% | Cell 01 (base), Cell 02 (VAT) | Standard-rated supply |
| 9% | Cell 03 (base), Cell 04 (VAT) | Accommodation, books, baby products |
| 0% | Cell 05 | Exports |
| Exempt without credit | Cell 07 | Financial, insurance, healthcare |

### Sales -- EU / Non-EU

| Location | Type | Cell | Notes |
|----------|------|------|-------|
| EU B2B goods | Intra-EU supply | Cell 06 | Zero-rated, report on VIES |
| EU B2B services | Art. 21(2) services | Cell 10 | Place of supply in customer MS |
| Non-EU | Export | Cell 05 | Zero-rated, customs docs |

---

## Step 4: VAT Credit Offset and Refund Process [T1]

**Legislation:** ZDDS Art. 92.

Bulgaria uses a unique 3-period rolling offset for VAT credits:

| Period | Action | Legislation |
|--------|--------|-------------|
| Period 0 (credit arises) | Credit recorded in Cell 60. Carried forward automatically. | Art. 92(1)(1) |
| Period 1 (next month) | If credit still exists after offsetting output VAT, carried forward. | Art. 92(1)(2) |
| Period 2 (month after) | If credit still exists after offsetting, carried forward. | Art. 92(1)(3) |
| Period 3 (third month) | Remaining credit either: (a) refunded within 30 days, OR (b) offset against other tax liabilities, OR (c) carried forward at taxpayer's choice | Art. 92(1)(4) |

### Accelerated Refund [T1]
**Legislation:** ZDDS Art. 92(3).

| Condition | Refund Timeline |
|-----------|----------------|
| > 30% of taxable supplies are zero-rated (exports/intra-EU) for last 12 months | Within 30 days of filing (no 3-period wait) |
| Public authority / municipality | Within 30 days |
| Other qualifying conditions | As specified by NRA |

### Refund Audit Risk [T2]
- NRA may initiate an audit (revizia) before releasing refund
- Audit can take up to 120 days (or longer with extension)
- Flag for reviewer: if client has pending audit, refund may be delayed

---

## Step 5: Reverse Charge Mechanics [T1]

**Legislation:** ZDDS Art. 82(2) (EU RC), Art. 82(3) (services RC), Art. 163a-163g (domestic RC).

### Intra-EU Acquisitions of Goods (Art. 13)
1. Report base in Cell 11, self-assessed output DDS in Cell 12
2. Claim input DDS in Cell 31
3. Net effect: zero for fully taxable businesses
4. Report on VIES Declaration

### EU Services Received -- B2B (Art. 82(2)(3))
1. Report base in Cell 13, self-assessed output DDS in Cell 14
2. Claim input DDS in Cell 32
3. Net effect: zero

### Non-EU Services Received (Art. 82(2)(3))
1. Report base in Cell 19, self-assessed output DDS in Cell 19a
2. Claim input DDS in Cell 32a
3. Net effect: zero

### Import of Goods from Non-EU (Art. 56)
1. DDS assessed by customs on import declaration (Mitnicheska deklaratsiya)
2. Report in Cell 17 (base) / Cell 18 (customs DDS)
3. Claim in Cell 34 (input DDS)
4. Net effect: zero (if customs DDS is deductible)

### Domestic Reverse Charge (Art. 163a-163g)

| Supply Type | Legislation | Notes |
|-------------|-------------|-------|
| Waste and scrap (metals, paper, glass, plastic) | Art. 163a, Annex 2 | No threshold |
| Grain and industrial crops (certain categories) | Art. 163b | Specified in Annex 2 |
| Emission allowances (CO2) | Art. 163c | Greenhouse gas permits |
| Investment gold | Art. 163d | When seller opts to tax |

Domestic reverse charge procedure:
1. Report in Cell 15 (base) / Cell 16 (output DDS)
2. Claim in Cell 30 (input DDS)
3. Protocol (protokol) must be issued by buyer within 15 days

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories: NEVER reverse charge
- Local consumption abroad: NOT reverse charge; foreign VAT paid at source
- EU supplier charged local VAT > 0%: NOT reverse charge
- Supplies by EU-established foreign suppliers of installed/assembled goods: NOT domestic RC from 2026

---

## Step 6: Deductibility Check

### Blocked Categories [T1]
**Legislation:** ZDDS Art. 70.

| Category | VAT Recovery | Legislation | Notes |
|----------|-------------|-------------|-------|
| Passenger cars (max 5+1 seats) -- purchase, lease | 0% | Art. 70(1)(4) | Unless taxi, driving school, car dealer, security, courier, emergency |
| Passenger cars (mixed business + private) | 50% | Art. 70(3) (from 2024) | Must be claimed as 50% |
| Running costs of blocked vehicles (fuel, maintenance, insurance) | 0% | Art. 70(1)(5) | Follows vehicle rule |
| Running costs of 50% vehicles | 50% | Art. 70(3) | Follows vehicle rule |
| Entertainment / representation (client hospitality, gifts, events) | 0% | Art. 70(1)(3) | Always blocked |
| Motorcycles (purchase, lease) | 0% | Art. 70(1)(4) | Same restrictions as cars |
| Supplies used for exempt-without-credit activities | 0% | Art. 70(1)(1) | Financial, insurance, education inputs |
| Supplies for non-business (personal) purposes | 0% | Art. 70(1)(2) | No deduction |
| Goods/services for activities outside scope of ZDDS | 0% | Art. 70(1)(1) | Non-economic activities |

### Vehicle Rules (Updated 2024) [T1]
**Legislation:** ZDDS Art. 70(1)(4-5), Art. 70(3), as amended.

| Scenario | Deduction | Evidence Required |
|----------|-----------|-------------------|
| Passenger car (5+1 seats), exclusively business | 100% | Must prove exclusive use (trip sheets, GPS, contracts) [T2] |
| Passenger car (5+1 seats), mixed business + private | 50% | Default assumption for mixed use |
| Passenger car (5+1 seats), primarily private | 0% | No deduction |
| Van / truck (> 5+1 seats or N1 category or higher) | 100% | If for business purposes |
| Taxi / driving school / car dealer vehicle | 100% | Qualifying business activity |
| Courier / delivery vehicle (5+1 seats) | 100% | Must be core business activity |
| Fuel/maintenance for deductible vehicle | Same % as vehicle | Follows vehicle classification |

### Registration-Based Recovery [T1]

| Registration Type | Input VAT Recovery | Legislation |
|-------------------|-------------------|-------------|
| VAT-registered (mandatory or voluntary) | Recovery subject to rules above | ZDDS Art. 69-72 |
| Non-registered | NO recovery | -- |
| Voluntarily registered | Same rights as mandatory | ZDDS Art. 100 |
| Deregistering entity | Must make 20-day correction for inventory on hand | ZDDS Art. 111 |

### Partial Exemption (Koefitsient) [T2]
**Legislation:** ZDDS Art. 73.

If business makes both taxable and exempt supplies:

`Koefitsient = (Taxable + Zero-Rated Supplies) / Total Supplies`

| Rule | Detail | Legislation |
|------|--------|-------------|
| Applied to | Cell 33 (partial tax credit) | Art. 73(2) |
| Rounding | Round UP to nearest whole percent | Art. 73(3) |
| De minimis | If >= 95%, treated as 100% | Art. 73(4) |
| Provisional | Use prior year coefficient during year | Art. 73(5) |
| Annual adjustment | In December return only (Cell 41) | Art. 73(6) |
| Excluded | Incidental financial/property transactions, sale of capital goods | Art. 73(2) |

**Flag for reviewer: provisional coefficient used during year; annual adjustment in December return required.**

---

## Step 7: SAF-T Reporting [T1]

**Legislation:** Amendments to Tax and Social Security Procedure Code (DOPK); NRA SAF-T schema (2025/2026).

### Phased Implementation

| Phase | Start Date | Who |
|-------|-----------|-----|
| Phase 1 | January 2026 | Large enterprises (revenue > BGN 300M or tax/social payments > BGN 3.5M in 2023) |
| Phase 2 | January 2027 | Large enterprises (other criteria) |
| Phase 3 | January 2028 | Medium enterprises |
| Phase 4 | January 2029 | Small enterprises |
| Phase 5 | January 2030 | Micro enterprises |

### Filing Requirements

| Feature | Detail |
|---------|--------|
| Monthly SAF-T file | By 14th of following month (same as VAT return) |
| Annual fixed asset file | By 28 February following year |
| Grace period | 6-month grace period after go-live (no penalties) |
| Format | OECD SAF-T standard, adapted for Bulgaria |
| Content | General ledger, AR/AP, fixed assets, inventory, invoices |

---

## Step 8: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | EUR 51,130 calendar year turnover (from 2026) | ZDDS Art. 96(1) |
| Previous threshold | BGN 100,000 rolling 12 months (until 2025) | ZDDS Art. 96(1) (old) |
| Registration period | Calendar year (from 2026) | ZDDS Art. 96(1) |
| Registration application deadline | 7 days after exceeding threshold (from 2026) | ZDDS Art. 96(1) |
| Filing frequency | ALWAYS monthly (no quarterly/annual option) | ZDDS Art. 125(5) |
| Filing and payment deadline | 14th of following month | ZDDS Art. 125(5) |
| Accelerated refund | > 30% zero-rated supplies in last 12 months | ZDDS Art. 92(3) |
| VAT credit offset period | 3 months rolling | ZDDS Art. 92(1) |
| Mixed-use vehicle deduction | 50% | ZDDS Art. 70(3) |
| Capital goods -- immovable | 20-year adjustment | ZDDS Art. 79(7) |
| Capital goods -- movable | 5-year adjustment | ZDDS Art. 79(3) |
| EU distance selling (B2C) | EUR 10,000 (EU-wide OSS threshold) | EU Directive 2017/2455 |
| EU SME scheme (from 2025) | EUR 85,000 domestic + EUR 100,000 EU-wide | EU Directive 2020/285 |

---

## Step 9: VAT Registration [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| VAT number format | BG + 9 or 10 digits | ZDDS Art. 94 |
| Mandatory registration | Turnover > EUR 51,130 in calendar year (from 2026) | ZDDS Art. 96(1) |
| Registration deadline | 7 days after exceeding threshold (from 2026) | ZDDS Art. 96(1) |
| Voluntary registration | May register at any time | ZDDS Art. 100 |
| Group registration | Not available in Bulgaria | -- |
| Deregistration | If turnover stays below threshold for 12 months | ZDDS Art. 108 |
| Deregistration inventory correction | Must correct (charge DDS on) remaining inventory within 20 days | ZDDS Art. 111 |
| Fiscal representative | Required for non-EU businesses without Bulgarian establishment | ZDDS Art. 133 |

---

## Step 10: Filing Deadlines and Penalties

### Filing Deadlines [T1]

| Filing | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| VAT return (Spravka-deklaratsiya) | Monthly | 14th of following month | ZDDS Art. 125(5) |
| Purchase Ledger (Dnevnik za Pokupkite) | Monthly (with return) | 14th of following month | ZDDS Art. 124(4) |
| Sales Ledger (Dnevnik za Prodazhbite) | Monthly (with return) | 14th of following month | ZDDS Art. 124(4) |
| VIES Declaration | Monthly | 14th of following month | ZDDS Art. 125(2) |
| Intrastat | Monthly | 14th of following month | NSI regulation |
| SAF-T (Phase 1+) | Monthly | 14th of following month | DOPK amendment |
| DDS payment | Monthly | 14th of following month | ZDDS Art. 89 |

**Note:** If the 14th falls on a weekend or public holiday, the deadline moves to the next business day.

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of VAT return | BGN 500 per return (first offense); BGN 1,000+ (repeat) | ZDDS Art. 178 |
| Late payment of DDS | Late interest at basic interest rate of BNB + 10% p.a. | DOPK Art. 175(1) |
| Failure to register for VAT | BGN 500 - BGN 5,000 + back-assessment of DDS | ZDDS Art. 178a |
| Failure to submit ledgers with return | BGN 500 per ledger (first); BGN 1,000+ (repeat) | ZDDS Art. 179 |
| Failure to issue invoice | BGN 500 - BGN 2,000 per invoice | ZDDS Art. 180 |
| Issuing invoice with incorrect data | BGN 100 - BGN 500 per invoice | ZDDS Art. 180a |
| Non-compliance with VIES declaration | BGN 500 - BGN 10,000 | ZDDS Art. 181 |
| Tax evasion (criminal) | Criminal liability under Penal Code | Penal Code Art. 255-258 |

---

## Step 11: Edge Case Registry

### EC1 -- Hotel in another EU country [T1]
**Situation:** Bulgarian DDS payer pays for hotel in Greece. Invoice shows Greek 13% VAT.
**Resolution:** NOT reverse charge. Greek VAT charged at source. No Bulgarian DDS entries. Greek VAT is irrecoverable cost.
**Legislation:** ZDDS Art. 21(4)(b) -- place of supply for accommodation is where property is located.

### EC2 -- SaaS subscription from US provider [T1]
**Situation:** Monthly charge from US company (e.g., AWS, Google), no VAT on invoice.
**Resolution:** Import of services. Report in Cell 19 (base) / Cell 19a (output DDS at 20%) / Cell 32a (input DDS). Net effect zero.
**Legislation:** ZDDS Art. 21(2) -- place of supply for B2B services is customer's establishment.

### EC3 -- Intra-EU goods acquisition [T1]
**Situation:** Bulgarian company buys goods from German supplier at 0% with DE VAT number.
**Resolution:** Cell 11 (base) / Cell 12 (output DDS at 20%) / Cell 31 (input DDS). Net zero. VIES declaration.
**Legislation:** ZDDS Art. 13 -- intra-EU acquisition.

### EC4 -- Passenger car, mixed use (50%) [T1]
**Situation:** Company buys passenger car BGN 40,000 + BGN 8,000 DDS. Used for business and private.
**Resolution:** 50% deduction. Cell 30 += BGN 4,000. Remaining BGN 4,000 is cost.
**Legislation:** ZDDS Art. 70(3).

### EC5 -- Passenger car, exclusively for business [T2]
**Situation:** Courier company buys delivery car (5+1 seats). BGN 30,000 + BGN 6,000 DDS. Used exclusively for deliveries.
**Resolution:** Flag for reviewer: courier/delivery qualifies for full deduction if exclusive business use can be demonstrated. If confirmed, Cell 30 += BGN 6,000.
**Legislation:** ZDDS Art. 70(1)(4) exception.

### EC6 -- Entertainment dinner (blocked) [T1]
**Situation:** Business dinner with clients. BGN 300 + BGN 60 DDS.
**Resolution:** Input DDS BLOCKED. Full BGN 360 is cost. Entertainment/representation never deductible.
**Legislation:** ZDDS Art. 70(1)(3).

### EC7 -- EU B2B service sale [T1]
**Situation:** Bulgarian company provides IT consulting to Romanian client (B2B).
**Resolution:** Report in Cell 10 (services to EU). No output DDS. Customer reverse charges in Romania. VIES declaration.
**Legislation:** ZDDS Art. 21(2) -- place of supply in customer's MS.

### EC8 -- Restaurant meal at 20% (post-2025) [T1]
**Situation:** Business lunch at Bulgarian restaurant. BGN 50 + BGN 10 DDS (20%).
**Resolution:** If entertainment/representation (client dining): BLOCKED. If ordinary working meal (not client entertainment): Cell 30 += BGN 10 (deductible as overhead). Classification matters -- flag if ambiguous [T2].
**Legislation:** ZDDS Art. 70(1)(3) for entertainment; Art. 69 for business overhead.

### EC9 -- VAT credit offset (3-period process) [T1]
**Situation:** Company has BGN 5,000 DDS credit in January. February and March have net payable < credit.
**Resolution:** January: Cell 60 = BGN 5,000 credit. February: offset against February's output; remaining carried forward. March: offset again. April (3rd period): remaining credit eligible for refund within 30 days.
**Legislation:** ZDDS Art. 92(1).

### EC10 -- Export of goods (accelerated refund) [T1]
**Situation:** Company is primarily an exporter. > 30% of supplies are zero-rated in last 12 months. Has BGN 20,000 credit.
**Resolution:** Qualifies for accelerated refund within 30 days without waiting for 3-period offset.
**Legislation:** ZDDS Art. 92(3).

### EC11 -- Domestic reverse charge (waste/scrap) [T1]
**Situation:** Bulgarian company sells scrap metal to another Bulgarian company. Both DDS registered.
**Resolution:** Seller invoices without DDS (domestic RC). Buyer issues protocol (protokol) within 15 days. Buyer: Cell 15 (base) / Cell 16 (output DDS 20%) / Cell 30 (input DDS). Net zero.
**Legislation:** ZDDS Art. 163a.

### EC12 -- Credit note [T1]
**Situation:** Supplier issues credit note reducing an earlier invoice.
**Resolution:** Reduce original cell values. Record in purchase ledger as negative entry. Report in the period the credit note is issued.
**Legislation:** ZDDS Art. 115 (credit notes).

### EC13 -- Deregistration inventory correction [T1]
**Situation:** Company deregisters from VAT. Has inventory of goods on hand.
**Resolution:** Must issue a protocol charging DDS on the tax base of remaining inventory, assets, and goods within 20 days of deregistration. This is a deemed supply.
**Legislation:** ZDDS Art. 111.

### EC14 -- Hotel accommodation at 9% [T1]
**Situation:** Business trip, hotel in Bulgaria. BGN 200 + BGN 18 DDS (9%). Business purpose.
**Resolution:** Cell 30 += BGN 18. Deductible as business overhead (not entertainment).
**Legislation:** ZDDS Art. 66(2); Art. 69.

---

## Step 12: VAT Rates -- Detailed Supply Classification [T1]

### 20% Standard Rate (ZDDS Art. 66(1)(1))

| Supply Category | Examples |
|----------------|----------|
| General goods | Electronics, furniture, clothing, household items, motor vehicles |
| Professional services | Legal, accounting, consulting, IT, advertising |
| Telecommunications | Mobile, fixed-line, internet |
| Alcohol | Beer, wine, spirits |
| Tobacco | Cigarettes, cigars |
| Construction and materials | Building services, cement, steel, timber |
| Energy | Electricity, gas, fuel |
| Restaurant/catering (from 2025) | Dine-in, takeaway (temporary 9% expired 31 Dec 2024) |
| Sports facilities (from 2025) | Gym, fitness, swimming (temporary 9% expired 31 Dec 2024) |

### 9% Reduced Rate (ZDDS Art. 66(2))

| Supply Category | Specific Items |
|----------------|----------------|
| Accommodation / hotel services | Hotel rooms, guesthouses, camping (tourist sector) |
| Books and publications | Printed and electronic books, newspapers, periodicals |
| Baby food | Infant formula, baby cereals |
| Baby hygiene products | Diapers, baby wipes, baby care products |

---

## Step 13: Comparison with Malta

| Feature | Bulgaria (BG) | Malta (MT) |
|---------|--------------|------------|
| Standard rate | 20% | 18% |
| Reduced rates | 9% (accommodation, books, baby products) | 12%, 7%, 5% |
| Return form | Spravka-deklaratsiya (~80 cells) + ledgers | VAT3 (45 boxes) |
| Ledger submission | Mandatory with every return | Not required with return |
| Filing frequency | Always monthly (no quarterly/annual) | Quarterly (Art. 10), Annual (Art. 11) |
| Filing deadline | 14th of following month | 21st of month after quarter (e-filing) |
| Payment deadline | 14th of following month | Same as filing |
| Small enterprise threshold | BGN 100,000 (~EUR 51,130) | EUR 35,000 |
| Capital goods movable | 5-year adjustment (no value threshold) | > EUR 1,160 gross |
| Capital goods immovable | 20-year adjustment | No specific adjustment period |
| Blocked: passenger cars | Yes (5+1 seats; 50% mixed-use rule from 2024) | Yes (10th Schedule) |
| Blocked: entertainment | Yes (fully blocked, Art. 70(1)(3)) | Yes (10th Schedule Item 3(1)(b)) |
| Domestic reverse charge | Waste, grain, emissions, investment gold | No domestic reverse charge |
| VAT credit refund | 3-period rolling offset (unique to BG) | Direct carry forward / refund |
| Accelerated refund | > 30% zero-rated -> 30-day refund | No accelerated mechanism |
| SAF-T | Phased from 2026 | No SAF-T |
| Coefficient de minimis | >= 95% treated as 100% | No de minimis |
| Currency | BGN (Bulgarian Lev, fixed 1.95583:1 EUR) | EUR |

---

## Step 14: Derived Box Calculations [T1]

```
Cell 20 = Cell 02 + Cell 04 + Cell 09 + Cell 12 + Cell 14 + Cell 16 + Cell 18 + Cell 19a
Cell 40 = Cell 30 + Cell 31 + Cell 32 + Cell 32a + Cell 33 + Cell 34

IF Cell 20 > Cell 40 THEN
  Cell 50 = Cell 20 - Cell 40  -- VAT Payable
  Cell 60 = 0
ELSE
  Cell 50 = 0
  Cell 60 = Cell 40 - Cell 20  -- VAT Credit
END

Cell 71 = Cell 50 - Cell 70  -- Payable after offset of prior credit
IF Cell 71 < 0 THEN
  Cell 80 = ABS(Cell 71)  -- Credit to carry forward or refund
END
```

---

## Step 15: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Certified accountant must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to certified accountant. Document gap.
```

---

## Step 16: Test Suite

### Test 1 -- Standard domestic purchase, 20% DDS [T1]
**Input:** Bulgarian supplier, office supplies, BGN 1,000 net + BGN 200 DDS. VAT-registered, fully taxable.
**Expected output:** Cell 30 += BGN 200. Fully deductible.

### Test 2 -- Import of services from US (SaaS) [T1]
**Input:** US supplier, monthly fee EUR 20 (~BGN 39), no VAT. VAT-registered.
**Expected output:** Cell 19 = BGN 39, Cell 19a = BGN 7.80 (20%), Cell 32a = BGN 7.80. Net = zero.

### Test 3 -- Intra-EU goods acquisition [T1]
**Input:** German supplier, goods EUR 5,000 at 0% with DE VAT number.
**Expected output:** Cell 11 = BGN equivalent, Cell 12 = 20% output DDS, Cell 31 = same input DDS. Net = zero.

### Test 4 -- Passenger car, mixed use (50%) [T1]
**Input:** Car BGN 30,000 + BGN 6,000 DDS. Mixed business/private use.
**Expected output:** Cell 30 += BGN 3,000 (50%). Remaining BGN 3,000 is cost.

### Test 5 -- Entertainment (blocked) [T1]
**Input:** Client dinner BGN 200 + BGN 40 DDS (20%).
**Expected output:** Cell 30 += BGN 0. BLOCKED. Full BGN 240 is cost.

### Test 6 -- Export of goods [T1]
**Input:** Bulgarian company exports to US client. BGN 50,000.
**Expected output:** Cell 05 = BGN 50,000. No output DDS. Zero-rated.

### Test 7 -- Hotel accommodation at 9% [T1]
**Input:** Hotel stay BGN 300 + BGN 27 DDS (9%). Business trip.
**Expected output:** Cell 30 += BGN 27. Deductible (business purpose, not entertainment).

### Test 8 -- VAT credit offset process (3 periods) [T1]
**Input:** January credit BGN 10,000. February net payable BGN 3,000. March net payable BGN 2,000. April net payable BGN 1,000.
**Expected output:** Jan: Cell 60 = BGN 10,000. Feb: offset 3,000, carry 7,000. Mar: offset 2,000, carry 5,000. Apr (period 3): offset 1,000, remaining 4,000 eligible for refund.

### Test 9 -- Domestic reverse charge (scrap) [T1]
**Input:** Bulgarian company sells scrap metal BGN 5,000 to another BG company. Both registered.
**Expected output:** Buyer: Cell 15 = BGN 5,000, Cell 16 = BGN 1,000 (20%), Cell 30 += BGN 1,000. Net = zero. Protocol issued.

### Test 10 -- EU B2B service sale [T1]
**Input:** Bulgarian company invoices Romanian client EUR 2,000 for IT consulting. B2B.
**Expected output:** Cell 10 = BGN equivalent. No output DDS. VIES declaration. Customer RC in Romania.

### Test 11 -- Non-registered entity purchase [T1]
**Input:** Non-registered entity buys supplies BGN 500 + BGN 100 DDS.
**Expected output:** No recovery. Full BGN 600 is cost. No VAT return filed.

### Test 12 -- Restaurant meal (working meal, not entertainment) [T1]
**Input:** Solo business lunch BGN 30 + BGN 6 DDS (20%). No clients present.
**Expected output:** Cell 30 += BGN 6. Deductible as business overhead (not entertainment/representation).

---

## Step 17: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Escalate to qualified adviser.

- **Corporate income tax:** 10% flat rate on adjusted profit (ZKPO)
- **Dividend tax:** 5% withholding (ZKPO Art. 194)
- **Personal income tax:** 10% flat rate (ZDDFL)
- **Social contributions (DOO):** employer ~13.72%, employee ~14.12% (varies by risk category)
- **Health insurance (ZO):** employer 4.8%, employee 3.2%
- **Local taxes:** Property tax, vehicle tax (administered by municipalities)

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT box assignment -- it is deterministic from transaction facts
- NEVER claim input DDS on passenger cars (5+1 seats) unless a proven exception or 50% mixed-use rule applies (Art. 70(1)(4), Art. 70(3))
- NEVER claim input DDS on entertainment or representation expenses (Art. 70(1)(3))
- NEVER omit the purchase/sales ledgers when filing the VAT return (Art. 124-126)
- NEVER skip the 3-period credit offset process -- do not assume immediate refund (Art. 92)
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi)
- NEVER apply the expired 9% rate to restaurant/catering or sports facilities (now 20% from 2025)
- NEVER allow non-registered entities to claim input DDS
- NEVER forget to issue protocol (protokol) for domestic reverse charge within 15 days
- NEVER omit VIES declaration for intra-EU supplies
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Contribution Notes

This skill covers Bulgaria's VAT system based on the ZDDS (VAT Act) as amended. Key distinctive features include: mandatory monthly filing for all VAT payers, the purchase/sales ledger submission requirement, the 3-period VAT credit offset process, the 50% mixed-use vehicle rule (from 2024), the SAF-T phased rollout from 2026, the expiration of temporary 9% reduced rates on restaurant/catering and sports (from 2025), and the protocol requirement for domestic reverse charge. Validation by a qualified Bulgarian certified accountant (diplomiran eksperten schetovoditel) is required before production use.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
