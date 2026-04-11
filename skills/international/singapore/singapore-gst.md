---
name: singapore-gst
description: Use this skill whenever asked to prepare, review, or create a Singapore GST return (GST F5 form) or any GST-related filing for any client. Trigger on phrases like "prepare GST return", "do the GST", "fill in GST F5", "create the return", "Singapore GST", "IRAS filing", or any request involving Singapore GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill contains the complete Singapore GST classification rules, GST F5 box mappings, input tax recovery rules, reverse charge treatment, major exporter schemes, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any GST-related work.
---

# Singapore GST Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Singapore |
| Jurisdiction Code | SG |
| Primary Legislation | Goods and Services Tax Act 1993 (GST Act) |
| Supporting Legislation | GST (General) Regulations; GST (Imports Relief) Order; Fourth Schedule (exempt supplies); Fifth Schedule (international services) |
| Tax Authority | Inland Revenue Authority of Singapore (IRAS) |
| Filing Portal | https://mytax.iras.gov.sg (myTax Portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: box assignment, standard/zero/exempt classification, reverse charge, derived calculations. Tier 2: partial exemption apportionment, industry scheme eligibility, de minimis test. Tier 3: complex group structures, non-standard financial services, transfer pricing GST adjustments. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax practitioner and document the gap.

---

## Section 1: Overview

### 1.1 What is GST? [T1]

Goods and Services Tax (GST) is Singapore's value-added tax, levied on the supply of goods and services in Singapore and on the importation of goods into Singapore. It is a broad-based consumption tax collected at every stage of the supply chain, with businesses acting as collection agents for the Inland Revenue Authority of Singapore (IRAS).

**Legislation:** Goods and Services Tax Act 1993 (Cap. 117A), Section 7 (charge to tax).

### 1.2 Current GST Rate [T1]

| Effective Date | Standard Rate |
|----------------|---------------|
| Before 1 January 2023 | 7% |
| 1 January 2023 to 31 December 2023 | 8% |
| 1 January 2024 onwards | 9% |

The rate increase was announced in Budget 2022 and implemented in two steps:
- First step: 7% to 8% on 1 January 2023 (GST Act, Section 16, as amended by the Goods and Services Tax (Amendment) Act 2022).
- Second step: 8% to 9% on 1 January 2024.

**The current standard rate as of 2024 onwards is 9%.**

### 1.3 Administering Authority [T1]

GST is administered by the **Inland Revenue Authority of Singapore (IRAS)**. All returns are filed electronically via the **myTax Portal** (https://mytax.iras.gov.sg). Paper filing is not available for GST returns.

### 1.4 GST Registration Number Format [T1]

Singapore GST registration numbers follow the format:
- For locally incorporated companies: same as the Unique Entity Number (UEN), e.g., `200312345A`
- Suffixed with a GST identifier in some contexts: `M9-1234567-8` (older format) or UEN-based
- Businesses must display their GST registration number on all tax invoices

**Legislation:** GST Act, Section 25 (registration number); GST (General) Regulations, Regulation 11 (tax invoices).

### 1.5 Types of Supplies [T1]

Under the GST Act, supplies are classified into four categories:

| Category | GST Treatment | Input Tax Claimable? | Examples |
|----------|--------------|---------------------|----------|
| Standard-rated | 9% GST charged | Yes | Most local goods and services |
| Zero-rated | 0% GST charged | Yes | Exports of goods, international services |
| Exempt | No GST charged | No | Financial services (Fourth Schedule), residential property sale/rental, investment precious metals |
| Out-of-scope | No GST charged | No (not a supply) | Private transactions, transfer of going concern (TOGC), third-country sales |

**Legislation:** GST Act, Section 7 (taxable supplies); Section 16 (rate); Section 22 (zero-rating); Fourth Schedule (exempt supplies).

---

## Section 2: GST F5 Return Form Structure

### 2.1 Overview of GST F5 [T1]

The GST F5 is the standard quarterly GST return filed by all GST-registered persons in Singapore. It reports all supplies made, output tax due, input tax claimed, and adjustments for the accounting period.

**Filed via:** myTax Portal (https://mytax.iras.gov.sg)
**Frequency:** Quarterly (standard); Monthly (by special arrangement with IRAS)
**Due date:** One month after the end of the prescribed accounting period

**Legislation:** GST Act, Section 20 (returns); GST (General) Regulations, Regulation 46.

### 2.2 Box-by-Box Breakdown [T1]

#### Supply Boxes (Output Side)

| Box | Description | Classification | Notes |
|-----|-------------|----------------|-------|
| **Box 1** | Total value of standard-rated supplies | Standard-rated (9%) | All local supplies subject to GST at the standard rate. Include the value before GST. Also include deemed supplies, self-supplies, and the value of reverse charge supplies where applicable. |
| **Box 2** | Total value of zero-rated supplies | Zero-rated (0%) | Exports of goods (Section 21) and prescribed international services (Section 21(3), Fifth Schedule). Report the full value of the supply. |
| **Box 3** | Total value of exempt supplies | Exempt | Supplies listed in the Fourth Schedule: prescribed financial services, sale/lease of residential property, supply of digital payment tokens, import/local supply of investment precious metals. |

#### Supply Totals

| Box | Description | Calculation |
|-----|-------------|-------------|
| **Box 4** | Total value of supplies | Box 1 + Box 2 + Box 3 (automatically calculated during e-filing) |

**Note on out-of-scope supplies:** Out-of-scope supplies (private transactions, transfer of going concern, government grants, third-country supplies, dividends, salary payments) are NOT reported in any supply box. They are excluded from the GST F5 return. IRAS may request information on out-of-scope supplies separately during audits.

#### Purchases Box

| Box | Description | Notes |
|-----|-------------|-------|
| **Box 5** | Total value of taxable purchases | All purchases on which GST was incurred (standard-rated local purchases plus imports). Report value before GST. This is an informational field for IRAS cross-checking. |

#### Tax Boxes

| Box | Description | Classification | Notes |
|-----|-------------|----------------|-------|
| **Box 6** | Output tax due | Output GST | GST due on standard-rated supplies (Box 1 x 9%). Also includes output tax on reverse charge supplies, customer accounting supplies, IGDS deferred import GST, and any adjustments increasing output tax. |
| **Box 7** | Input tax and refunds claimed | Input GST | Total input tax claimable on business purchases, subject to input tax recovery rules (Section 20). Include tourist refund scheme amounts, bad debt relief, and pre-registration input tax claims where applicable. |

#### Net GST

| Box | Description | Calculation | Notes |
|-----|-------------|-------------|-------|
| **Box 8** | Net GST to be paid to / (refunded by) IRAS | Box 6 minus Box 7 | Positive = tax payable; Negative = refund claimable. |

#### Reporting Boxes (Schemes and Supplementary Information)

| Box | Description | Notes |
|-----|-------------|-------|
| **Box 9** | Total value of goods imported under MES / Approved 3rd Party Logistics Company Scheme / other approved import GST suspension schemes | Report CIF value of goods imported under import GST suspension schemes. |
| **Box 10** | Did you claim for GST you had refunded to tourists? | Yes/No indicator. Applies only to independent retailers and central refund agencies operating the Tourist Refund Scheme (TRS). |
| **Box 11** | Did you make any bad debt relief claims and/or refund claims for reverse charge transactions? | Yes/No indicator. Select "Yes" if claiming bad debt relief or reverse charge refunds in the period. |
| **Box 12** | Did you make any pre-registration claims? | Yes/No indicator. Select "Yes" if this is the first return and you are claiming input tax incurred before GST registration. |
| **Box 13** | Revenue | Gross sales, income, or turnover reflecting the primary business income for the accounting period. This is an informational field. |
| **Box 14** | Did you import services and/or low-value goods subject to GST under reverse charge? | Value of imported services (from 1 Jan 2020) and low-value goods (from 1 Jan 2023) subject to reverse charge under Section 14(2). Output tax on these supplies is included in Box 6. |
| **Box 15** | Did you operate an electronic marketplace to supply remote services subject to GST on behalf of third-party suppliers? | For electronic marketplace operators accounting for GST on remote services supplied on behalf of third-party suppliers. |
| **Box 16** | Did you operate as a redeliverer, or an electronic marketplace to supply imported low-value goods subject to GST on behalf of third-party suppliers? | For redeliverers and electronic marketplace operators supplying imported low-value goods on behalf of third parties. |
| **Box 17** | Did you make your own supply of imported low-value goods that is subject to GST? | For suppliers of their own imported low-value goods subject to GST. Not required if you are not a supplier of low-value goods. |

#### Import GST Deferment Scheme (IGDS) Boxes

These boxes are only available to businesses approved under the IGDS.

| Box | Description | Notes |
|-----|-------------|-------|
| **Box 18** | Net GST per Box 8 above | Carries forward the value from Box 8. |
| **Box 19** | Add: Deferred import GST payable | Import GST deferred from the point of import to the GST return. |
| **Box 20** | Total tax to be paid to IRAS | Box 18 + Box 19. This is the total amount payable. |
| **Box 21** | Total value of goods imported under this scheme | CIF value of goods for which import GST payment has been deferred to the GST return. |

### 2.3 Relationship Between Boxes [T1]

```
Box 4  = Box 1 + Box 2 + Box 3
Box 8  = Box 6 - Box 7

For IGDS-approved businesses:
Box 20 = Box 18 (= Box 8) + Box 19

Box 6 includes:
  - Standard-rated output tax (Box 1 x 9%)
  - Output tax on reverse charge supplies (Box 14 value x 9%)
  - Output tax on IGDS imports (Box 21 x applicable rate, via Box 19)
  - Customer accounting output tax (if applicable)
  - All adjustments increasing output tax

Box 7 includes:
  - Input tax on local taxable purchases
  - Input tax on reverse charge (equals output tax if fully taxable)
  - Input tax on IGDS imports (if claimable)
  - Bad debt relief (if Box 11 = Yes)
  - Pre-registration input tax claims (if Box 12 = Yes)
  - Tourist refund scheme refunds (if Box 10 = Yes)
  - All adjustments decreasing output tax
```

### 2.4 GST F7 -- Errors in Previous Returns [T2]

If errors are discovered in previously filed GST F5 returns, they must be corrected via:
- **GST F7 form** (for voluntary disclosure of errors), or
- **Amended GST F5** (for the current period, if error qualifies for current-period adjustment under the administrative concession)

Administrative concession for current-period adjustment:
- Error is not due to fraud or willful neglect
- Net GST error does not exceed SGD 1,500 per accounting period
- Errors are corrected in the next return filed

**Legislation:** GST Act, Section 47 (voluntary disclosure); IRAS e-Tax Guide "GST: Voluntary Disclosure of Errors."

---

## Section 3: Transaction Classification

### 3.1 Classification Decision Tree [T1]

For every transaction, follow this sequence:

```
1. Is it a SUPPLY for GST purposes? (Section 7)
   NO  --> Out of scope (no entry on GST F5)
   YES --> Continue

2. Is it made IN SINGAPORE? (Sections 13-14, place of supply rules)
   NO  --> Potentially zero-rated or out-of-scope
   YES --> Continue

3. Is it EXEMPT? (Fourth Schedule)
   YES --> Box 3
   NO  --> Continue

4. Is it ZERO-RATED? (Section 21, 22; Fifth Schedule)
   YES --> Box 2
   NO  --> Standard-rated, Box 1 at 9%
```

### 3.2 Standard-Rated Supplies (9%) [T1]

All supplies of goods and services made in Singapore that are not exempt or zero-rated are subject to GST at 9%.

**Common examples:**
- Sale of goods in Singapore
- Provision of local services (consultancy, legal, accounting, IT, etc.)
- Lease of commercial property
- Commission and fee income
- Deemed supplies (e.g., gifts exceeding SGD 200, private use of business assets)
- Self-supplies under Sections 10A and 27A

**Legislation:** GST Act, Section 7(1) (charge), Section 16 (rate of 9%).

### 3.3 Zero-Rated Supplies (0%) [T1]

Zero-rated supplies are taxable supplies charged at 0%. The supplier can still claim input tax on related purchases.

#### 3.3a Export of Goods (Section 21) [T1]

Goods are zero-rated when exported from Singapore, provided:
- Goods are physically shipped out of Singapore within the prescribed timeframe
- Exporter retains prescribed export documentation (bill of lading, airway bill, export permit)
- For hand-carried exports: Hand-Carried Exports Scheme (HCES) documentation applies

**Legislation:** GST Act, Section 21(1)-(2); GST (General) Regulations, Regulation 31-35.

#### 3.3b International Services (Section 21(3), Fifth Schedule) [T1]

Services are zero-rated if they fall under one of the prescribed categories in the Fifth Schedule:

| Para | Service Type | Conditions |
|------|-------------|------------|
| 1 | Services supplied under a contract with an overseas person | Service is not performed on goods situated in Singapore at the time; no direct benefit to a person in Singapore other than the overseas person |
| 2 | Services directly in connection with land or goods outside Singapore | Land/goods must be outside Singapore |
| 3 | Services of arranging for international transport | Arranging transport of passengers or goods to/from Singapore |
| 4 | International transport of goods or passengers | Actual carriage of goods/passengers entering or leaving Singapore |
| 5 | Services supplied to overseas persons and directly in connection with goods for export | Goods must be exported within prescribed period |
| 6 | Services (repair, maintenance, broking) of ships/aircraft used for international travel | Ship/aircraft must be used for international transport |
| 7-10 | Various prescribed international services | Specific conditions per paragraph |

**Key condition for Para 1 zero-rating:** The "belonging" status of the customer. The customer must "belong" outside Singapore (Section 15(2)). A person belongs outside Singapore if:
- Not registered for GST in Singapore, AND
- Has no business establishment or fixed establishment in Singapore, AND
- Usual place of residence is outside Singapore

**Legislation:** GST Act, Section 21(3); Fifth Schedule.

#### 3.3c Zero-Rating Lookup Table [T1]

| Transaction | Zero-Rated? | Box | Conditions |
|-------------|-------------|-----|------------|
| Export of goods by sea/air | Yes | Box 2 | Export documents retained |
| International freight services | Yes | Box 2 | Transport to/from Singapore |
| Consultancy to overseas client (no SG benefit) | Yes | Box 2 | Para 1, client belongs overseas |
| IT services to overseas company (no SG use) | Yes | Box 2 | Para 1, client belongs overseas |
| Repair of ship used internationally | Yes | Box 2 | Para 6 conditions met |
| Sale of goods delivered locally in Singapore | No | Box 1 | Even if buyer is overseas person |
| Services performed on goods in Singapore (goods stay in SG) | No | Box 1 | Fails Para 1 exclusion |
| Training delivered in Singapore to overseas delegates | No | Box 1 | Service physically performed in SG with direct benefit in SG |

### 3.4 Exempt Supplies (Fourth Schedule) [T1]

No GST is charged on exempt supplies. Input tax directly attributable to exempt supplies is **not claimable**.

#### Fourth Schedule Categories:

| Category | Description | Legislation |
|----------|-------------|-------------|
| **Financial services** | Provision, transfer, or dealing in prescribed financial products: interest on loans, exchange of currency, issue/transfer of securities, life insurance premiums, operation of bank accounts | Fourth Schedule, Part I |
| **Residential property** | Sale or lease of any residential property (including HDB flats, condominiums, landed residential). Short-term accommodation (serviced apartments, hotels) is NOT exempt -- it is standard-rated. | Fourth Schedule, Part II |
| **Investment precious metals (IPM)** | Import and local supply of gold, silver, and platinum bars/coins meeting prescribed purity standards (99.5% gold, 99.9% silver, 99.95% platinum) | Fourth Schedule, Part III; GST (Imports Relief) (Amendment No. 2) Order |
| **Digital payment tokens** | Supply of digital payment tokens (e.g., Bitcoin, Ether) as a form of payment is exempt. Utility tokens and NFTs may not qualify. | Fourth Schedule, Part IV (from 1 Jan 2020) |

**Legislation:** GST Act, Fourth Schedule.

### 3.5 Out-of-Scope Supplies [T1]

Out-of-scope transactions are not supplies for GST purposes. No GST is charged and no input tax credit arises.

| Transaction Type | Classification | Notes |
|-----------------|----------------|-------|
| Private/personal transactions | Out-of-scope | Not in the course or furtherance of business |
| Transfer of a going concern (TOGC) | Out-of-scope | Transfer of a business as a whole (Section 10(1)(b)) |
| Government grants/subsidies | Out-of-scope | Not consideration for a supply |
| Third-country sales | Out-of-scope | Goods sold from overseas to overseas, never entering SG |
| Dividends | Out-of-scope | Not consideration for a supply |
| Salary/wage payments | Out-of-scope | Employment, not a supply of services |
| Loan repayments (principal) | Out-of-scope | Not a supply |
| Directors' fees (from employment) | Out-of-scope | Employment relationship |
| Donations (without benefits given) | Out-of-scope | No supply made |
| Statutory penalties/fines | Out-of-scope | Not consideration for a supply |

**Legislation:** GST Act, Section 7 (supply must be in the course or furtherance of business); Section 10 (TOGC).

---

## Section 4: GST Rates -- Detailed Reference

### 4.1 Rate Table [T1]

| Rate | Category | Applicable To |
|------|----------|--------------|
| **9%** | Standard | All taxable supplies not qualifying for zero-rating or exemption |
| **0%** | Zero-rated | Exports of goods (s.21); International services meeting Fifth Schedule conditions (s.21(3)); Supply of stores/fuel for international ships/aircraft |
| **Exempt** | Fourth Schedule | Prescribed financial services; Residential property (sale/lease); Investment precious metals; Digital payment tokens |

### 4.2 Transitional Rate Rules [T1]

For the rate change from 8% to 9% (1 January 2024), the following transitional rules applied:

| Scenario | Rate |
|----------|------|
| Supply made before 1 Jan 2024, payment received before 1 Jan 2024 | 8% |
| Supply made before 1 Jan 2024, payment received on/after 1 Jan 2024 | 8% |
| Supply made on/after 1 Jan 2024 | 9% |
| Supply spanning the rate change (e.g., 12-month lease) | Apportioned: 8% for period before 1 Jan 2024; 9% for period on/after 1 Jan 2024 |
| Payment received before 1 Jan 2024 for supply on/after 1 Jan 2024 | 8% on the payment amount (election available) |
| Invoice issued before 1 Jan 2024 for supply on/after 1 Jan 2024 | 8% on the invoiced amount (election available) |

**Legislation:** GST (Amendment) Act 2022; IRAS e-Tax Guide "GST: Rate Change (2024)".

### 4.3 Calculating GST from Gross Amounts [T1]

```
GST-exclusive price x 1.09 = GST-inclusive price
GST amount = GST-inclusive price x (9/109)
Net amount = GST-inclusive price x (100/109)
```

For prior periods:
```
8% period: GST = inclusive x (8/108); Net = inclusive x (100/108)
7% period: GST = inclusive x (7/107); Net = inclusive x (100/107)
```

---

## Section 5: Input Tax Recovery

### 5.1 General Principle [T1]

A GST-registered person may claim input tax on goods and services acquired for the purpose of making taxable supplies (standard-rated or zero-rated), subject to the conditions in Section 20 of the GST Act.

**Conditions for claiming input tax [T1]:**
1. The claimant is GST-registered at the time of the claim
2. The goods or services are for business purposes
3. The goods or services are used or intended to be used for making taxable supplies
4. The claimant holds a valid tax invoice (or import permit for imports)
5. The input tax is not a "blocked" category (Regulation 26/27 of GST (General) Regulations)
6. The claim is made within 5 years from the due date for the return relating to the relevant prescribed accounting period

**Legislation:** GST Act, Section 20; GST (General) Regulations, Regulation 26-29.

### 5.2 Blocked Input Tax [T1]

The following categories of input tax are **permanently blocked** and may NEVER be claimed, regardless of business purpose:

| Blocked Category | Regulation | Exception |
|-----------------|------------|-----------|
| **Motor car expenses** -- purchase, hire, import of motor cars and related running expenses (petrol, maintenance, parking, ERP) | Reg 26(1) | Taxis, private hire cars used exclusively for chauffeured transport, motor dealers' stock-in-trade, driving schools |
| **Club membership fees** -- country club, golf club, recreation club subscriptions | Reg 27(1)(a) | None |
| **Medical expenses** -- employee medical, dental, health insurance | Reg 27(1)(b) | Medical expenses required under the Work Injury Compensation Act, Employment Act, or similar statutory obligation |
| **Family benefits** -- benefits provided to family members of employees or directors | Reg 27(1)(c) | None |
| **Costs of non-business transactions** -- expenses not related to making taxable supplies | Reg 26(2) | None |

**Key distinction:** A "motor car" is defined as a motor vehicle with a maximum laden weight not exceeding 3,000 kg, constructed or adapted for the carriage of not more than 7 passengers (excluding the driver). This means:
- Vans, lorries, trucks (>3,000 kg or goods vehicles): NOT blocked
- Motorcycles: NOT blocked
- Buses (>7 passengers): NOT blocked

**Legislation:** GST (General) Regulations, Regulations 26-27.

### 5.3 Directly Attributable Method [T1]

Input tax must first be categorized by attribution:

```
Step 1: Identify input tax DIRECTLY ATTRIBUTABLE to:
  (a) Taxable supplies --> Fully claimable
  (b) Exempt supplies  --> NOT claimable
  (c) Non-business use --> NOT claimable

Step 2: Remaining input tax is RESIDUAL (not directly attributable).
  Apply apportionment formula to residual input tax.
```

### 5.4 Apportionment of Residual Input Tax [T2]

For businesses making both taxable and exempt supplies, residual input tax is apportioned using a formula approved by the Comptroller:

**Standard formula:**
```
Claimable residual input tax = Residual input tax x (Value of taxable supplies / Total value of all supplies)
```

**Alternative methods** (require Comptroller approval):
- Transaction count method
- Floor area method
- Sectoral method
- Any other method that produces a fair and reasonable result

**The apportionment method must be applied consistently and is subject to annual adjustment.**

**Legislation:** GST Act, Section 20(4); GST (General) Regulations, Regulation 29.

### 5.5 De Minimis Rule for Exempt Input Tax [T1]

A partially exempt business may claim ALL of its input tax (including the portion attributable to exempt supplies) if the exempt input tax satisfies BOTH conditions of the de minimis test:

| Condition | Threshold |
|-----------|-----------|
| Total exempt input tax | Does not exceed **SGD 5,000** per quarter |
| Proportion of exempt input tax | Does not exceed **5%** of total input tax |

**Both conditions must be met simultaneously.** If either threshold is breached, the business must apportion its input tax and may not claim the exempt portion.

**Legislation:** GST (General) Regulations, Regulation 29A.

### 5.6 Longer Period Adjustment [T2]

Regardless of whether the de minimis test is passed in each quarter, a longer-period adjustment is required at the end of a longer period (usually a financial year):
- Re-apply the de minimis test using annual figures
- If the annual de minimis test is not met, repay the exempt input tax previously claimed in individual quarters
- If the annual de minimis test is met but quarterly tests were failed, claim back the exempt input tax not claimed in individual quarters

**Legislation:** GST (General) Regulations, Regulation 29A(4).

### 5.7 Pre-Registration Input Tax Claims [T2]

GST-registered persons may claim input tax incurred before registration, subject to conditions:

| Item | Time Limit | Conditions |
|------|-----------|------------|
| Goods on hand at registration | Purchased within 3 years before registration | Still on hand at date of registration; not fully consumed |
| Services | Supplied within 6 months before registration | Must relate to business activities after registration |
| Property (capital goods) | Purchased within 3 years before registration | Still held at registration; used for making taxable supplies |

**Legislation:** GST (General) Regulations, Regulation 40.

---

## Section 6: GST Registration

### 6.1 Mandatory Registration [T1]

A person must register for GST if:

| Test | Threshold | Measurement Period | Legislation |
|------|-----------|-------------------|-------------|
| **Retrospective test** | Taxable turnover exceeds **SGD 1,000,000** | Past 12 months (any rolling 12-month period ending at the end of any calendar quarter) | GST Act, Section 25(1)(a), First Schedule, Para 1(1)(a) |
| **Prospective test** | Taxable turnover is expected to exceed **SGD 1,000,000** | Next 12 months | GST Act, Section 25(1)(a), First Schedule, Para 1(1)(b) |

**Taxable turnover** includes standard-rated and zero-rated supplies. It excludes exempt and out-of-scope supplies.

**Timeline for registration:**
- Apply within 30 days of the liability to register arising
- Registration takes effect from the date determined by the Comptroller (usually the first day of the month following the 30-day period)

### 6.1a Registration Grace Period (from 1 July 2025) [T1]

From 1 July 2025, businesses that become liable to register for GST on a prospective basis (i.e., they reasonably forecast crossing the SGD 1,000,000 threshold in the next 12 months) are given a **two-month grace period** before the effective date of registration. This extends the previous one-month period.

**Key rules:**
- The obligation to **apply** for GST registration within 30 days of the forecast still applies
- However, the effective date of registration is now **two months** from the date of the forecast (previously one month)
- This gives businesses more time to prepare systems, pricing, and processes before they must start charging GST

**Legislation:** GST (General) (Amendment No. 2) Regulations 2025, gazetted 30 June 2025.

### 6.2 Voluntary Registration [T1]

Businesses below the SGD 1,000,000 threshold may register voluntarily, subject to conditions:

| Condition | Requirement |
|-----------|-------------|
| Must remain registered | Minimum 2 years |
| Must comply with GST obligations | File returns, charge GST, keep records |
| Must implement e-invoicing | From 1 November 2025, new voluntary registrants (companies registering within 6 months of incorporation) must use InvoiceNow; from 1 April 2026, all new voluntary registrants must use InvoiceNow |
| Must make taxable supplies | Or intend to make taxable supplies |

**Legislation:** GST Act, First Schedule, Para 1(3)-(4).

### 6.3 Overseas Vendor Registration (OVR) [T1]

Non-resident suppliers must register for GST under the OVR regime if they make B2C supplies of:
- **Remote services** (digital services, electronically supplied services) to non-GST-registered customers in Singapore
- **Low-value goods** (goods valued at or below SGD 400, imported by air or post) to non-GST-registered customers in Singapore (from 1 Jan 2023)

**OVR registration thresholds:**
- Global turnover exceeds SGD 1,000,000, AND
- B2C supplies of remote services and/or low-value goods to Singapore customers exceed SGD 100,000

**OVR-registered vendors:**
- Must charge and account for GST at 9% on B2C supplies
- Cannot claim input tax (unless they opt for full GST registration)
- File quarterly returns via myTax Portal

**Legislation:** GST Act, Section 25(2A)-(2B); First Schedule, Para 1A.

### 6.4 Electronic Marketplace Operator Registration [T1]

An electronic marketplace operator is treated as the supplier and must register for GST if:
- It operates an electronic marketplace through which B2C supplies of remote services or low-value goods are made
- The marketplace operator meets the OVR registration thresholds

The marketplace operator accounts for GST on behalf of the underlying suppliers.

**Legislation:** GST Act, Section 33C (deemed supply by marketplace operator).

### 6.5 GST Group Registration [T2]

Two or more GST-registered entities may apply for group registration if:
- Each entity is a body corporate
- One entity controls the others, or they are under common control (>50% voting rights)
- All entities are established or have a fixed establishment in Singapore

**Effects of group registration:**
- Intra-group supplies are disregarded for GST purposes
- The representative member files a single GST return for the group
- All members are jointly and severally liable for GST obligations

**Legislation:** GST Act, First Schedule, Para 5.

### 6.6 Deregistration [T1]

Voluntary deregistration may be requested if:
- Taxable turnover has fallen below SGD 1,000,000 (for compulsorily registered persons)
- At least 2 years have passed since voluntary registration
- Business has permanently ceased

On deregistration, output GST may be due on remaining stock and assets (deemed supply).

**Legislation:** GST Act, First Schedule, Para 7-9.

---

## Section 7: Filing Deadlines and Penalties

### 7.1 Prescribed Accounting Periods [T1]

| Frequency | Standard | Notes |
|-----------|----------|-------|
| **Quarterly** | Default for all GST-registered persons | Calendar quarters: Jan-Mar, Apr-Jun, Jul-Sep, Oct-Dec |
| **Monthly** | By application to the Comptroller | Typically approved for businesses that regularly receive GST refunds (e.g., major exporters) |
| **Six-monthly** | Rare, by special approval | Only for specific cases |

Businesses may apply to use non-calendar quarter periods (e.g., financial year quarters) with Comptroller approval.

### 7.2 Filing and Payment Deadlines [T1]

| Obligation | Deadline |
|------------|----------|
| Filing of GST F5 return | **One month** after the end of the prescribed accounting period |
| Payment of net GST payable | **One month** after the end of the prescribed accounting period (same as filing deadline) |
| GIRO payment | Deducted on the 15th of the month following the filing deadline |

**Examples (quarterly filer, calendar quarters):**

| Quarter | Period | Filing/Payment Deadline |
|---------|--------|------------------------|
| Q1 | 1 Jan -- 31 Mar | 30 April |
| Q2 | 1 Apr -- 30 Jun | 31 July |
| Q3 | 1 Jul -- 30 Sep | 31 October |
| Q4 | 1 Oct -- 31 Dec | 31 January (next year) |

### 7.3 Late Filing Penalties [T1]

| Penalty | Amount |
|---------|--------|
| Late filing of GST return | **SGD 200** per month (or part thereof) that the return is outstanding, up to a maximum of SGD 10,000 |
| Failure to file | IRAS may issue an estimated assessment (Section 45) with penalties |

### 7.4 Late Payment Penalties [T1]

| Penalty | Rate |
|---------|------|
| Initial late payment penalty | **5%** of outstanding tax |
| Additional penalty | **2% per month** on the unpaid tax (including the 5% penalty), imposed on the 60th day after the due date and every subsequent month |
| Maximum total penalty | **50%** of the outstanding tax |

**Legislation:** GST Act, Section 47 (penalties); GST (General) Regulations.

### 7.5 Interest on Overpayment [T1]

IRAS pays interest on GST refunds that are delayed beyond the prescribed processing time (generally 30 business days from receipt of a complete and accurate return).

---

## Section 8: Reverse Charge Mechanism

### 8.1 Overview [T1]

The reverse charge mechanism requires a GST-registered person in Singapore to account for GST on services and low-value goods procured from overseas suppliers, as if the recipient were the supplier.

**Effective dates:**
- Imported services: **1 January 2020**
- Low-value goods (goods valued at SGD 400 or below): **1 January 2023**

**Legislation:** GST Act, Section 14(2) (reverse charge on imported services); Section 14(2A) (reverse charge on low-value goods).

### 8.2 When Reverse Charge Applies [T1]

Reverse charge applies when **ALL** of the following conditions are met:

| Condition | Requirement |
|-----------|-------------|
| Recipient | Is GST-registered in Singapore |
| Supplier | Belongs outside Singapore (Section 15) |
| Supply | Is a supply of services or low-value goods |
| Recipient's input tax recovery | Recipient is NOT entitled to full input tax credit (i.e., the business makes exempt supplies or has non-business activities) |

**Important:** If the recipient is entitled to full input tax credit (i.e., makes only taxable supplies), the reverse charge still technically applies but has zero net effect (output tax = input tax claimed). IRAS provides an administrative concession: fully taxable businesses need not account for reverse charge if they would be entitled to claim back all the input tax.

### 8.3 Reverse Charge Mechanics on GST F5 [T1]

When reverse charge applies:

```
Step 1: Determine the value of imported services / low-value goods
Step 2: Calculate GST at 9% on that value
Step 3: Report on GST F5:
  - Box 1: Include the value of reverse charge supplies
  - Box 6: Include the output tax (value x 9%)
  - Box 7: Include the input tax claim (value x 9%), subject to input tax recovery rules
  - Box 14: Report the value of reverse charge supplies (imported services and/or LVG)
  - Box 5: Include in taxable purchases
```

**Net effect for partially exempt businesses:**
- Output tax in Box 6 is fully accounted for
- Input tax in Box 7 is reduced by the proportion attributable to exempt supplies
- Result: net GST cost equal to the irrecoverable portion

### 8.4 Supplies Subject to Reverse Charge [T1]

| Supply Type | Subject to RC? | Notes |
|-------------|---------------|-------|
| Consultancy from overseas firm | Yes | Service from non-SG supplier |
| Software subscription (SaaS) from US | Yes | Remote service |
| Cloud hosting from overseas | Yes | Remote service |
| Legal advice from UK law firm | Yes | Service from non-SG supplier |
| Importation of physical goods (>SGD 400) | No | GST collected by Singapore Customs at import |
| Low-value goods ordered online (<=SGD 400) | Yes | From 1 Jan 2023 |
| Services consumed overseas (e.g., hotel abroad) | No | Place of supply outside Singapore |
| Intra-company cross-charges from overseas HQ | Yes | If treated as supplies for GST purposes |
| Royalty/licence fees to overseas licensor | Yes | Service from non-SG supplier |

### 8.5 Exclusions from Reverse Charge [T1]

The following are NOT subject to reverse charge:
- Services that would be exempt under the Fourth Schedule if made locally (e.g., financial services)
- Services that would be zero-rated under Section 21(3) if made locally
- Services consumed entirely outside Singapore
- Goods imported through normal customs channels with import GST paid at the border (>SGD 400)
- Services received by a fully taxable business (administrative concession -- no net GST impact)

**Legislation:** GST Act, Section 14(2); IRAS e-Tax Guide "GST: Taxing imported services by way of reverse charge."

---

## Section 9: Major Industry and Import Schemes

### 9.1 Major Exporter Scheme (MES) [T2]

**Purpose:** Relieves cash flow burden for businesses that export substantially.

**Benefits:**
- Import GST on non-dutiable goods is suspended (not payable at the point of import)
- Import GST on dutiable goods remains payable to Singapore Customs

**Eligibility criteria:**
- Zero-rated supplies must exceed 50% of total taxable supplies for a past 12-month period, OR
- Output tax payable is less than SGD 200 per month on average for the past 12 months
- Good compliance track record with IRAS

**GST F5 reporting:**
- Box 9: Value of goods imported under MES
- No entry in Box 6 for suspended import GST
- Input tax on imports is effectively built into Box 7 through the scheme

**Legislation:** GST Act, Section 27; GST (General) Regulations, Regulation 51.

### 9.2 Import GST Deferment Scheme (IGDS) [T2]

**Purpose:** Allows approved businesses to defer import GST from the point of import to the GST return.

**Benefits:**
- Import GST is not paid at the point of import to Singapore Customs
- Instead, import GST is accounted for in the GST F5 return:
  - Output tax (Box 6): import GST due
  - Input tax (Box 7): import GST claimable (subject to input tax recovery rules)
- Net cash flow benefit: GST is deferred by 1-2 months

**Eligibility:**
- Annual import value exceeds SGD 100 million, OR
- Approved Assisted Self-Help Kit (ASK) result
- Good compliance track record

**GST F5 reporting:**
- Box 21: CIF value of goods imported under IGDS
- Box 19: Deferred import GST payable
- Box 6: Include the deferred import GST as output tax (also reflected in Box 19)
- Box 7: Include the deferred import GST as input tax (if claimable)

**Legislation:** GST Act, Section 27A; IRAS e-Tax Guide "GST: Import GST Deferment Scheme."

### 9.3 Approved Third Party Logistics (3PL) Company Scheme [T2]

**Purpose:** Allows approved 3PL providers to import and supply goods belonging to overseas persons without charging GST.

**Benefits:**
- Goods belonging to overseas principals stored in the 3PL company's warehouse
- Import GST suspended when goods are imported under the scheme
- Supplies of goods from the 3PL warehouse to local GST-registered customers are zero-rated (subject to conditions)

**Legislation:** GST Act, Section 33(3); IRAS e-Tax Guide "GST: Approved Third Party Logistics Company Scheme."

### 9.4 Approved Contract Manufacturer and Trader (ACMT) Scheme [T2]

**Purpose:** Reduces GST costs for contract manufacturers processing goods belonging to overseas principals.

**Benefits:**
- Goods belonging to overseas persons imported by the ACMT are not subject to import GST
- Deemed supply provisions under Section 10(2) are suspended for goods belonging to the overseas person

**Legislation:** GST Act, Section 33(4); IRAS e-Tax Guide "GST: Approved Contract Manufacturer and Trader Scheme."

### 9.5 Hand-Carried Exports Scheme (HCES) [T1]

**Purpose:** Allows zero-rating for goods physically hand-carried out of Singapore by overseas customers.

**Requirements:**
- Customer must be a person who belongs outside Singapore
- Goods must be hand-carried out of Singapore at the point of sale (same day)
- Supplier must retain prescribed documentation:
  - Customer's passport (copy)
  - Boarding pass or ticket (copy)
  - HCES form endorsed by customer
- Minimum value: no minimum, but scheme is typically used for high-value goods

**GST F5 reporting:**
- Box 2: Include in zero-rated supplies

**Legislation:** GST (General) Regulations, Regulation 35A; IRAS e-Tax Guide "GST: Hand-Carried Exports Scheme."

### 9.6 Tourist Refund Scheme (TRS) [T1]

**Purpose:** Allows tourists to claim a refund of GST paid on goods purchased in Singapore and carried out in their personal luggage.

**Key features:**
- Operated by Global Tax Free (the appointed central refund agency) and approved retailers
- Tourist must spend at least SGD 100 (including GST) at a single retailer on the same day
- Tourist must depart Singapore within 2 months of purchase
- Refund is processed at the airport via electronic Tourist Refund Scheme (eTRS) kiosks

**Impact on GST-registered retailers:**
- Retailer charges GST at 9% at point of sale (Box 1, Box 6)
- Refund is processed between the tourist and the central refund agency
- Retailer may claim input tax credit for the refund amount via Box 7

**Legislation:** GST Act, Section 25A; GST (Tourist Refund Scheme) Regulations.

### 9.7 Approved Marine Customer Scheme [T2]

**Purpose:** Allows approved marine customers to import goods with GST suspended for use in qualifying ships.

### 9.8 Zero GST Warehouse Scheme [T2]

**Purpose:** Allows goods to be stored in, and supplied between, approved warehouses without payment of import GST or output GST, provided goods remain within the scheme.

**Legislation:** GST Act, Section 33B.

---

## Section 10: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- Reverse Charge on Imported Services (Partially Exempt Business) [T1]

**Situation:** A Singapore GST-registered financial institution (making both taxable and exempt supplies) engages a UK consulting firm for strategic advisory services. The UK firm invoices GBP 50,000 with no GST.

**Resolution:** Reverse charge applies. The financial institution must:
1. Account for output tax at 9% on the SGD equivalent of GBP 50,000 (Box 6, Box 14)
2. Claim input tax at 9% subject to input tax recovery ratio (Box 7)
3. If the institution's input tax recovery rate is 40%, only 40% of the reverse charge input tax is claimable
4. Net cost: 60% of the reverse charge GST (SGD equivalent x 9% x 60%)

**Legislation:** GST Act, Section 14(2).

### EC2 -- Low-Value Goods Regime (Online Purchases) [T1]

**Situation:** A GST-registered company purchases office supplies worth SGD 300 from an overseas online marketplace. The goods are shipped by air to Singapore.

**Resolution:**
- If the marketplace operator is OVR-registered: GST is charged by the marketplace operator at the point of sale. The recipient claims input tax from the marketplace operator's tax invoice.
- If the supplier is NOT OVR-registered: Reverse charge applies (from 1 Jan 2023). Report value in Box 1 and Box 14; account for output tax in Box 6; claim input tax in Box 7.
- If the goods value exceeds SGD 400: Normal import GST applies at Customs.

**Legislation:** GST Act, Section 14(2A); Section 33C (marketplace operator rules).

### EC3 -- OVR Obligations for SaaS Provider [T1]

**Situation:** A US-based SaaS company provides subscriptions to Singapore consumers (B2C). Annual B2C revenue from Singapore customers is SGD 150,000. Global turnover is USD 5 million.

**Resolution:** The SaaS company must register under OVR because:
- Global turnover > SGD 1,000,000
- B2C Singapore supplies > SGD 100,000
The SaaS company must charge and remit GST at 9% on B2C supplies to Singapore non-registered customers.

**Legislation:** GST Act, First Schedule, Para 1A.

### EC4 -- Customer Accounting for Prescribed Goods [T1]

**Situation:** A GST-registered mobile phone wholesaler sells SGD 15,000 worth of mobile phones to another GST-registered retailer.

**Resolution:** Customer accounting applies. The supplier:
- Does NOT charge GST on the invoice
- Issues an invoice stating "Customer Accounting Supply -- Customer to account for GST"
- Reports the supply value in Box 1 but NOT the GST in Box 6

The customer:
- Accounts for output tax on the purchase in Box 6
- Claims input tax in Box 7 (subject to input tax recovery rules)

**Prescribed goods (from 1 Jan 2019):** Mobile phones, memory cards, off-the-shelf software.
**Threshold:** Total value of prescribed goods in a single invoice exceeds SGD 10,000.

**Legislation:** GST Act, Section 20A; Eleventh Schedule.

### EC5 -- De Minimis Exempt Input Tax Test [T1]

**Situation:** A GST-registered company provides mostly taxable supplies but also earns a small amount of exempt interest income from bank deposits. Quarterly exempt input tax is SGD 3,000, and total input tax is SGD 80,000.

**Resolution:** Apply de minimis test:
- Exempt input tax: SGD 3,000 (< SGD 5,000 threshold) -- PASS
- Proportion: SGD 3,000 / SGD 80,000 = 3.75% (< 5% threshold) -- PASS
- Both conditions met: the company may claim ALL input tax (including the SGD 3,000 attributable to exempt supplies)

If either condition fails (e.g., exempt input tax is SGD 6,000), the exempt input tax is NOT claimable.

**Legislation:** GST (General) Regulations, Regulation 29A.

### EC6 -- GST Group Registration -- Intra-Group Supplies [T2]

**Situation:** Company A and Company B are in the same GST group. Company A provides management services to Company B for SGD 200,000.

**Resolution:** Intra-group supplies are disregarded for GST purposes. No GST is charged, no entry on the GST return for this transaction. The representative member files a single consolidated return.

**Caution:** If Company B is partially exempt, the group's overall input tax recovery may be affected. Flag for reviewer.

**Legislation:** GST Act, First Schedule, Para 5.

### EC7 -- Real Estate Developer -- Exempt and Taxable Supplies [T2]

**Situation:** A property developer builds a mixed development with residential units (exempt) and commercial units (standard-rated).

**Resolution:** Input tax on construction costs must be apportioned:
- Costs directly attributable to commercial units: fully claimable
- Costs directly attributable to residential units: NOT claimable
- Common costs (e.g., shared infrastructure): apportioned using an approved method (floor area, value, or other reasonable basis)

Developer must apply for special apportionment approval if standard formula produces an unreasonable result.

**Legislation:** GST Act, Section 20(4); IRAS e-Tax Guide "GST: Partial Exemption and Input Tax Recovery."

### EC8 -- Electronic Marketplace Operator Rules [T1]

**Situation:** An overseas marketplace (e.g., Amazon) facilitates sales of low-value goods from overseas suppliers to Singapore consumers.

**Resolution:** The marketplace operator is deemed to be the supplier and must:
- Register under OVR (if thresholds met)
- Charge GST at 9% on B2C supplies of low-value goods
- File GST returns and remit GST to IRAS
- The underlying supplier does NOT charge GST on these supplies (the marketplace operator does)

**Legislation:** GST Act, Section 33C.

### EC9 -- Tourist Refund Scheme Edge Case [T1]

**Situation:** A tourist purchases a luxury watch (SGD 20,000 + SGD 1,800 GST) from an eTRS-registered retailer. The tourist departs Singapore 3 months after purchase.

**Resolution:** The tourist is NOT eligible for a refund because departure was more than 2 months after purchase. The retailer retains the GST collected as normal output tax. No adjustment required.

**Legislation:** GST (Tourist Refund Scheme) Regulations, Regulation 4(1)(b).

### EC10 -- Transfer Pricing Adjustments [T3]

**Situation:** IRAS adjusts the transfer price of intercompany services between a Singapore subsidiary and its overseas parent. The adjusted value is higher than the original invoiced amount.

**Resolution:** Escalate to qualified tax practitioner. The transfer pricing adjustment may create additional output tax liability on the deemed supply value. Complex interaction between GST Act and transfer pricing provisions. This is outside the scope of automated classification.

**Legislation:** GST Act, Section 17(3) (open market value for supplies between related parties); IRAS e-Tax Guide "Transfer Pricing Guidelines."

### EC11 -- Bad Debt Relief [T1]

**Situation:** A GST-registered supplier has charged GST on an invoice but has not received payment after 12 months. The debt has been written off in the supplier's books.

**Resolution:** The supplier may claim bad debt relief (reduce output tax) if:
- At least 12 months have passed since the supply
- The debt has been written off in the books
- The supplier has made reasonable efforts to collect the debt
- Claim is made within 5 years

Report the bad debt relief as a reduction in Box 6 (output tax) and include the claim in Box 7. Mark Box 11 as "Yes".

If the debt is subsequently recovered, the supplier must repay the bad debt relief by including the amount in Box 6 (output tax).

**Legislation:** GST Act, Section 19(6)-(9); GST (General) Regulations, Regulation 38.

### EC12 -- Free Zone Transactions [T1]

**Situation:** Goods are stored in a Free Trade Zone (FTZ) in Singapore and sold to another party within the FTZ, without the goods leaving the FTZ.

**Resolution:** The supply is treated as a local supply subject to GST at 9% (not zero-rated) unless the goods are subsequently exported. The FTZ status does not automatically confer zero-rating.

**Exception:** If the buyer is an overseas person and the goods are to be exported from the FTZ, zero-rating may apply under Section 21(6) with prescribed export documentation.

**Legislation:** GST Act, Section 21(6); IRAS e-Tax Guide "GST: Guide on Exports."

### EC13 -- Deemed Supply of Business Assets Put to Private Use [T1]

**Situation:** A director of a GST-registered company uses a company laptop (costing SGD 3,000) exclusively for personal purposes for 6 months.

**Resolution:** A deemed supply arises under Section 10(4). Output GST must be accounted for on the open market value of the private use. If the asset was originally purchased with input tax claimed, the deemed supply ensures GST is ultimately borne on private consumption.

**Legislation:** GST Act, Section 10(4) (deemed supply on private use of business assets).

### EC14 -- Gifts and Samples Exceeding SGD 200 [T1]

**Situation:** A company gives a gift basket worth SGD 500 (excluding GST) to a client.

**Resolution:** Gifts with an open market value exceeding SGD 200 (excluding GST) per gift are deemed supplies. Output GST must be accounted for at 9% on the SGD 500 value.

Gifts worth SGD 200 or less (excluding GST) are NOT deemed supplies -- no output GST required.

**Industrial samples** given free for business purposes are generally not deemed supplies, regardless of value.

**Legislation:** GST Act, Section 10(3); GST (General) Regulations, Regulation 3.

---

## Section 11: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard Local Sale, 9% GST [T1]

**Input:** GST-registered Singapore company sells consulting services to a local client. Invoice: SGD 10,000 + SGD 900 GST = SGD 10,900 total.
**Expected output:**
- Box 1 = SGD 10,000
- Box 6 = SGD 900 (output tax)
- No input tax entry (this is a sale)

### Test 2 -- Zero-Rated Export of Goods [T1]

**Input:** GST-registered exporter ships goods worth SGD 50,000 FOB to a buyer in Japan. Bill of lading and export permit retained.
**Expected output:**
- Box 2 = SGD 50,000
- Box 6 = SGD 0 (zero-rated)
- Input tax on related purchases is claimable in Box 7

### Test 3 -- Exempt Financial Services [T1]

**Input:** A bank earns SGD 500,000 in interest income from loans to local borrowers during the quarter.
**Expected output:**
- Box 3 = SGD 500,000
- Box 6 = SGD 0 (exempt, no GST charged)
- Input tax attributable to this exempt supply is NOT claimable

### Test 4 -- Reverse Charge on Imported Services [T1]

**Input:** GST-registered partially exempt company engages an Australian marketing firm for SGD 100,000. No GST on invoice. Company's input tax recovery rate is 70%.
**Expected output:**
- Box 1 = SGD 100,000 (include in standard-rated supplies)
- Box 6 = SGD 9,000 (output tax at 9%)
- Box 7 = SGD 6,300 (input tax: SGD 9,000 x 70% recovery)
- Box 14 = SGD 100,000
- Box 5 = SGD 100,000 (include in taxable purchases)
- Net GST cost = SGD 2,700

### Test 5 -- Blocked Input Tax (Motor Car) [T1]

**Input:** GST-registered company purchases a BMW sedan for SGD 150,000 + SGD 13,500 GST.
**Expected output:**
- Box 5 = SGD 150,000
- Box 7 = SGD 0 (input tax BLOCKED -- motor car)
- The SGD 13,500 GST is an irrecoverable cost

### Test 6 -- De Minimis Test Pass [T1]

**Input:** Company has total input tax of SGD 100,000 for the quarter. Exempt input tax (attributable to interest income from bank deposits) is SGD 4,000.
**Expected output:**
- Test 1: SGD 4,000 < SGD 5,000 -- PASS
- Test 2: SGD 4,000 / SGD 100,000 = 4% < 5% -- PASS
- Both conditions met: claim ALL SGD 100,000 input tax in Box 7

### Test 7 -- De Minimis Test Fail [T1]

**Input:** Company has total input tax of SGD 50,000 for the quarter. Exempt input tax is SGD 4,000.
**Expected output:**
- Test 1: SGD 4,000 < SGD 5,000 -- PASS
- Test 2: SGD 4,000 / SGD 50,000 = 8% > 5% -- FAIL
- De minimis NOT met: must apportion. Claimable input tax = SGD 50,000 - SGD 4,000 = SGD 46,000 in Box 7

### Test 8 -- Customer Accounting (Prescribed Goods) [T1]

**Input:** GST-registered wholesaler sells SGD 12,000 of mobile phones to a GST-registered retailer. Single invoice.
**Expected output (wholesaler):**
- Box 1 = SGD 12,000
- Box 6 = SGD 0 (customer accounts for GST)

**Expected output (retailer/customer):**
- Box 6 = SGD 1,080 (output tax at 9% on SGD 12,000)
- Box 7 = SGD 1,080 (input tax, fully claimable if fully taxable)
- Box 5 = SGD 12,000

### Test 9 -- Low-Value Goods via OVR Marketplace [T1]

**Input:** GST-registered company purchases stationery worth SGD 200 from an OVR-registered overseas marketplace. GST of SGD 18 is charged by the marketplace.
**Expected output:**
- Box 5 = SGD 200
- Box 7 = SGD 18 (input tax claimed from marketplace's tax invoice)
- No reverse charge required (GST already charged by OVR marketplace)

### Test 10 -- Hand-Carried Exports Scheme [T1]

**Input:** Tourist purchases a handbag worth SGD 5,000 + SGD 450 GST from an eTRS retailer. Tourist departs same day with HCES documentation.
**Expected output:**
- Box 2 = SGD 5,000 (zero-rated supply under HCES)
- Box 6 = SGD 0 (zero-rated)

### Test 11 -- Gift Exceeding SGD 200 (Deemed Supply) [T1]

**Input:** Company gives a corporate gift worth SGD 350 (ex-GST) to a client. Gift is from stock purchased with input tax claimed.
**Expected output:**
- Box 1 = SGD 350 (deemed supply)
- Box 6 = SGD 31.50 (output tax at 9%)

### Test 12 -- International Services Zero-Rating (Para 1) [T1]

**Input:** Singapore law firm provides legal advisory services to a UK company. The UK company is not GST-registered in Singapore and has no establishment in Singapore. Fee: SGD 80,000. No direct benefit to any person in Singapore.
**Expected output:**
- Box 2 = SGD 80,000 (zero-rated international service, Fifth Schedule Para 1)
- Box 6 = SGD 0
- Input tax on related expenses is claimable in Box 7

### Test 13 -- Residential Property Sale (Exempt) [T1]

**Input:** GST-registered property developer sells a residential condominium unit for SGD 2,000,000.
**Expected output:**
- Box 3 = SGD 2,000,000
- Box 6 = SGD 0 (exempt supply)
- Input tax directly attributable to the residential unit is NOT claimable
- Must check de minimis test for residual input tax

---

## Section 12: Comparison with EU VAT

### 12.1 Key Structural Differences [T1]

| Feature | Singapore GST | EU VAT (Directive 2006/112/EC) |
|---------|--------------|-------------------------------|
| **Tax name** | Goods and Services Tax (GST) | Value Added Tax (VAT) |
| **Standard rate** | 9% (single rate) | Varies by member state: 17% (Luxembourg) to 27% (Hungary) |
| **Reduced rates** | None -- Singapore has a single standard rate | Multiple reduced rates per member state (5%, 6%, 9%, 10%, 12%, 13%, etc.) |
| **Super-reduced / parking rates** | Not applicable | Some member states (e.g., France 2.1%, Spain 4%) |
| **Zero-rating** | Exports of goods, international services only | Varies -- UK (pre-Brexit) had extensive zero-rating; most EU states have limited zero-rating |
| **Registration threshold** | SGD 1,000,000 (~EUR 700,000) | Varies: EUR 0 (Spain) to EUR 85,000 (France) |
| **Filing frequency** | Quarterly (default), monthly (by approval) | Varies: monthly, quarterly, or annually depending on member state and turnover |
| **Intra-community rules** | Not applicable (Singapore is not part of a multi-state bloc) | Extensive intra-community acquisition/supply rules |
| **Reverse charge** | On imported services (from 2020), low-value goods (from 2023) | On cross-border B2B services (default since 2010); specific goods (construction, metals) by member state |
| **Place of supply (services)** | Primarily based on where the supplier belongs; extensive zero-rating for international services | General rule: where customer belongs (B2B); where supplier belongs (B2C), with numerous exceptions |
| **Invoice requirements** | Tax invoice required for all taxable supplies; electronic invoicing increasingly mandatory | Full VAT invoice required for B2B; simplified invoice below thresholds; e-invoicing mandates vary by state |
| **Group registration** | Available for corporate groups under common control | Available in most member states; rules vary |
| **Bad debt relief** | Available after 12 months, debt written off | Available in most states; conditions vary (6-24 months) |
| **Tourist refund** | eTRS at airport (minimum SGD 100 purchase) | VAT refund for non-EU tourists; rules and minimums vary by state |
| **Capital goods scheme** | No multi-year capital goods adjustment scheme (unlike EU) | Required: 5-year adjustment for movable assets; 10-20 years for immovable |
| **Import GST deferment** | Available under IGDS for approved businesses | Available in many EU states (postponed accounting) |

### 12.2 Key Similarities [T1]

| Feature | Singapore GST | EU VAT |
|---------|--------------|--------|
| Multi-stage tax | Yes -- collected at every stage of supply chain | Yes |
| Input-output mechanism | Output tax less input tax = net payable/refundable | Same |
| Invoice-based system | Tax invoices required | VAT invoices required |
| Exemptions for financial services | Yes (Fourth Schedule) | Yes (Article 135, Directive 2006/112/EC) |
| Exemptions for residential property | Yes (sale and lease) | Varies -- most states exempt residential letting |
| Reverse charge for imported services | Yes (from 2020) | Yes (Article 196) |
| Blocked input tax categories | Yes (motor cars, clubs, medical, family benefits) | Yes -- varies by state (entertainment, cars, etc.) |
| Voluntary registration | Available below threshold | Available in most states |
| Electronic filing | Mandatory | Mandatory in most states |

### 12.3 Practical Differences for Multinational Businesses [T2]

| Scenario | Singapore Treatment | EU Treatment |
|----------|-------------------|--------------|
| Cross-border sale of goods within a trading bloc | Not applicable -- Singapore is a single jurisdiction | Intra-community supply (zero-rated) + intra-community acquisition (self-assessed) |
| Digital services to overseas consumers | OVR for B2C to Singapore consumers; zero-rated for B2C outside Singapore | OSS (One-Stop Shop) for B2C to EU consumers; each member state's VAT rate |
| Importing goods from overseas | Import GST at Customs (or IGDS/MES deferment) | Import VAT at Customs (or postponed accounting in some states) |
| Multi-country group structure | Single GST return per Singapore entity or GST group | Separate VAT return per member state where registered |

---

## Section 13: PROHIBITIONS [T1]

These are absolute rules. Violating any prohibition produces an incorrect return.

1. **NEVER** let AI guess GST box assignment -- it is deterministic from the classification rules in this skill.

2. **NEVER** claim input tax on blocked categories (motor cars, club memberships, medical expenses, family benefits) regardless of business purpose, unless a specific statutory exception applies (Regulation 26-27).

3. **NEVER** apply reverse charge when the overseas supplier has already charged Singapore GST (e.g., OVR-registered supplier).

4. **NEVER** zero-rate a supply of services without verifying the "belonging" status of the customer under Section 15 and the specific conditions of the applicable Fifth Schedule paragraph.

5. **NEVER** zero-rate goods that are not physically exported from Singapore. Local delivery to an overseas person does not qualify for zero-rating.

6. **NEVER** treat a sale or lease of residential property as a taxable supply. Residential property is always exempt (Fourth Schedule, Part II).

7. **NEVER** treat a sale or lease of commercial property as an exempt supply. Commercial property is standard-rated at 9%.

8. **NEVER** apply the de minimis rule without checking BOTH conditions (SGD 5,000 absolute threshold AND 5% proportional threshold). Both must be met simultaneously.

9. **NEVER** allow input tax claims without a valid tax invoice or import permit. The claim must be supported by documentation (Regulation 25).

10. **NEVER** ignore the reverse charge on imported services for a partially exempt business. The administrative concession for fully taxable businesses does NOT extend to partially exempt businesses.

11. **NEVER** treat out-of-scope items (salaries, dividends, loan principal, statutory fines) as taxable supplies. These are not supplies under the GST Act.

12. **NEVER** confuse zero-rated supplies (input tax IS claimable) with exempt supplies (input tax is NOT claimable). These have opposite input tax consequences.

13. **NEVER** apply customer accounting to goods that are not prescribed (currently: mobile phones, memory cards, off-the-shelf software) or to invoices below the SGD 10,000 threshold.

14. **NEVER** file a paper GST return. GST F5 must be filed electronically via myTax Portal.

15. **NEVER** compute any number -- all arithmetic is handled by the deterministic engine, not Claude. Claude classifies and assigns; the engine calculates.

---

## Step 14: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Qualified tax practitioner must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified tax practitioner. Document gap.
```

---

## Step 15: Record-Keeping Requirements [T1]

GST-registered persons must maintain records for **at least 5 years** from the end of the prescribed accounting period. Required records include:

| Record Type | Details |
|-------------|---------|
| Tax invoices (issued and received) | All tax invoices, including simplified tax invoices |
| Credit and debit notes | All credit/debit notes issued or received |
| Import permits and export documents | Customs permits, bills of lading, airway bills |
| Contracts and agreements | For supplies of goods and services |
| Bank statements and payment records | Supporting transaction evidence |
| GST account | Summary of output and input tax for each period |
| Business and accounting records | General ledger, journals, trial balance |

**Legislation:** GST Act, Section 43; GST (General) Regulations, Regulation 53.

---

## Step 16: E-Invoicing Requirements [T1]

From 1 April 2025, Singapore is progressively mandating the InvoiceNow standard for GST-registered businesses:

| Phase | Effective Date | Scope |
|-------|---------------|-------|
| Phase 1a | 1 November 2025 | Companies that voluntarily register for GST within 6 months of incorporation |
| Phase 1b | 1 April 2026 | All new voluntary GST registrants (regardless of incorporation date or business structure) |
| Phase 2a | 1 April 2028 | All new compulsory GST registrants and existing GST-registered businesses with annual supplies of SGD 200,000 or less |
| Phase 2b | 1 April 2029 | Existing GST-registered businesses with annual supplies of SGD 1,000,000 or less |
| Phase 2c | 1 April 2030 | Existing GST-registered businesses with annual supplies of SGD 4,000,000 or less |
| Phase 3 | 1 April 2031 | All remaining GST-registered businesses (annual supplies exceeding SGD 4,000,000) |

InvoiceNow uses the Peppol e-invoicing framework. Businesses must transmit invoice data to IRAS in the prescribed format via an approved Access Point.

**Legislation:** IRAS e-Tax Guide "InvoiceNow for GST-Registered Businesses."

---

## Step 17: Common Adjustments on GST F5

### 17.1 Change of Use Adjustments [T2]

When assets or services originally acquired for a taxable purpose are subsequently used for an exempt or non-business purpose (or vice versa), a change-of-use adjustment is required:

| Direction | GST Treatment |
|-----------|--------------|
| Taxable --> Exempt/Non-business | Output tax due (deemed supply). Include adjustment in Box 6. |
| Exempt/Non-business --> Taxable | Input tax claimable. Include adjustment in Box 7. |

**Legislation:** GST Act, Section 10(4)-(5); GST (General) Regulations, Regulation 30-31.

### 17.2 Credit Notes and Debit Notes [T1]

| Document | Effect on Output Tax | Effect on Input Tax |
|----------|---------------------|-------------------|
| Credit note issued (to customer) | Decreases output tax (reduce Box 6) | N/A |
| Debit note issued (to customer) | Increases output tax (increase Box 6) | N/A |
| Credit note received (from supplier) | N/A | Decreases input tax (Box 7 reduced) |
| Debit note received (from supplier) | N/A | Increases input tax (Box 7) |

**Legislation:** GST Act, Section 18; GST (General) Regulations, Regulation 12-13.

### 17.3 Exchange Rate Rules [T1]

For transactions denominated in foreign currencies:
- Convert to SGD using the exchange rate at the **time of supply**
- Acceptable rates: prevailing selling rate published by the Monetary Authority of Singapore (MAS), or a consistent rate from a reliable source (e.g., bank rate, Bloomberg, Reuters)
- The rate must be applied consistently

**Legislation:** GST (General) Regulations, Regulation 14.

---

## Step 18: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and GST registration number** [T1] -- UEN format or older M-format
2. **GST registration status** [T1] -- Registered, not registered, OVR-registered
3. **Accounting period** [T1] -- Quarterly (which quarters?), monthly, or other
4. **Industry/sector** [T2] -- Impacts scheme eligibility (MES, IGDS, ACMT), place of supply rules, and input tax recovery
5. **Does the business make exempt supplies?** [T2] -- If yes, partial exemption applies (input tax apportionment required; confirm recovery rate with reviewer)
6. **Does the business have import activities?** [T2] -- If yes, check eligibility for import GST suspension/deferment schemes
7. **Does the business make international supplies?** [T1] -- If yes, verify zero-rating conditions for each category of international supply
8. **Net GST payable/refundable brought forward** [T1] -- From prior period
9. **Payment method** [T1] -- GIRO or other
10. **Does the business supply prescribed goods (mobile phones, memory cards, off-the-shelf software)?** [T1] -- If yes, customer accounting may apply

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Contribution Notes (For Other Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all GST F5 box numbers (Boxes 1-21) with the equivalent boxes on your jurisdiction's GST/VAT return form.
3. Replace GST rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace the registration threshold (SGD 1,000,000) with your jurisdiction's equivalent.
5. Replace blocked input tax categories with your jurisdiction's equivalent.
6. Replace the de minimis thresholds (SGD 5,000 / 5%) with your jurisdiction's equivalent.
7. Replace international service zero-rating provisions with your jurisdiction's equivalent.
8. Replace scheme references (MES, IGDS, ACMT, HCES) with your jurisdiction's equivalent trade facilitation schemes.
9. Have a qualified tax practitioner in your jurisdiction validate every T1 rule before publishing.
10. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
11. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
