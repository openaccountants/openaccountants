---
name: saudi-arabia-vat
description: Use this skill whenever asked to prepare, review, or create a Saudi Arabia VAT return for any client. Trigger on phrases like "prepare VAT return", "Saudi VAT", "ZATCA return", "KSA VAT", "fill in VAT return", "Fatoorah", "e-invoicing Saudi", or any request involving Saudi Arabia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete KSA VAT classification rules, return field mappings, input tax recovery rules, e-invoicing requirements, penalty regime, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Saudi Arabia VAT-related work.
---

# Saudi Arabia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Kingdom of Saudi Arabia (KSA) |
| Jurisdiction Code | SA |
| Primary Legislation | VAT Law (Royal Decree No. A/113, dated 2/11/1438H); VAT Implementing Regulations (Board of Directors Resolution No. 3839, dated 14/12/1438H) |
| Supporting Legislation | E-Invoicing Regulation (issued 4/12/1442H); Excise Tax Law (Royal Decree No. A/86); Unified VAT Agreement for the GCC States; VAT Implementing Regulations amendments (Board Resolution 01-06-24, published 18 April 2025) |
| Tax Authority | Zakat, Tax and Customs Authority (ZATCA / formerly GAZT) |
| Filing Portal | https://zatca.gov.sa (ZATCA portal); Fatoorah e-invoicing platform |
| Contributor | Open Accounting Skills Community |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: field assignment, standard/zero/exempt classification, e-invoicing phases, derived calculations. Tier 2: apportionment, real estate first supply, designated zones, related party transactions. Tier 3: complex GCC customs union matters, oil & gas sector special rules, advanced transfer pricing with VAT implications. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified tax consultant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax consultant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and VAT registration number** [T1] -- 15-digit Tax Identification Number (TIN) starting with 3 and ending with 3
2. **Commercial Registration (CR) number** [T1] -- required for ZATCA registration
3. **Filing frequency** [T1] -- Monthly (annual taxable supplies > SAR 40,000,000) or Quarterly
4. **VAT period** [T1] -- calendar month or calendar quarter
5. **Accounting method** [T1] -- accrual basis (standard) or cash basis (permitted for certain taxpayers)
6. **Industry/sector** [T2] -- impacts treatment (e.g., real estate, oil & gas, financial services, healthcare)
7. **Does the business make exempt supplies?** [T2] -- If yes, apportionment required
8. **E-invoicing phase** [T1] -- Phase 1 (generation) or Phase 2 (integration) -- depends on ZATCA wave rollout
9. **Does the business operate in a designated zone?** [T2] -- special VAT rules apply
10. **Is the business part of a VAT group?** [T2] -- group registration impacts reporting

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and filing frequency are confirmed.**

**Legislation:** VAT Law, Article 50 (registration); VAT Implementing Regulations, Article 8.

---

## Step 1: VAT Rate Structure

### 1a. Standard Rate [T1]

| Rate | Application | Effective Date | Legislation |
|------|-------------|----------------|-------------|
| 15% | Standard rate on all taxable supplies and imports | From 1 July 2020 | VAT Law, Article 2; Royal Decree A/638 |
| 5% | Former standard rate | 1 January 2018 to 30 June 2020 | VAT Law, Article 2 (original) |
| 0% | Zero-rated supplies (exports, international transport, qualifying medicines, investment metals) | From 1 January 2018 | VAT Law, Article 33 |
| Exempt | Financial services (interest-based), residential rental, life insurance premiums | From 1 January 2018 | VAT Law, Article 29 |

**The rate increase from 5% to 15% took effect on 1 July 2020. Transitional rules applied for contracts entered before 11 May 2020.**

### 1b. Zero-Rated Supplies (Complete List) [T1]

| Category | Description | Legislation |
|----------|-------------|-------------|
| Exports of goods | Goods exported outside GCC implementing states, with proof of export | Article 33(1); IR Article 32 |
| Exports of services | Services supplied to non-resident outside KSA (no establishment in KSA, service not related to goods/real estate in KSA) | Article 33(2); IR Article 33 |
| International transport | Transport of goods and passengers internationally, and related services | Article 34; IR Article 34 |
| Qualifying medicines | Medicines and medical equipment listed by SFDA and Ministry of Health | Article 35; IR Article 35 |
| Investment metals | Gold, silver, and platinum of 99% purity or higher, traded for investment purposes | Article 36; IR Article 36 |
| Supplies to diplomats | Supplies to accredited diplomatic missions and international organizations (reciprocity basis) | Article 37; IR Article 37 |
| First supply of residential property | First supply of a residential property within 3 years of completion (government-subsidized housing relief) -- subject to SAR 1,000,000 cap | Article 36(3); Royal Decree A/84 (housing VAT/RETT relief) |

### 1c. Exempt Supplies (Complete List) [T1]

| Category | Description | Legislation |
|----------|-------------|-------------|
| Financial services | Services based on interest or implicit margin (lending, deposits, Islamic finance equivalents) | Article 29(1); IR Article 29 |
| Residential rental | Rental of residential real estate (not hotel/serviced apartments) | Article 30; IR Article 30 |
| Life insurance | Life insurance and reinsurance premiums | Article 29(5); IR Article 29 |
| Local passenger transport | Provision not yet activated -- currently taxable at 15% | Article 31 (reserved) |

**Key distinction:** Zero-rated supplies allow full input tax recovery. Exempt supplies do NOT allow input tax recovery on related inputs.

### 1d. Out-of-Scope Supplies [T1]

| Category | Description | Legislation |
|----------|-------------|-------------|
| Salary/wages | Employment income -- not a supply | Article 2 (definition of supply) |
| Government sovereign activities | Activities conducted by government in a sovereign capacity | Article 10; IR Article 9 |
| Dividends | Distribution of profits -- not consideration for a supply | General principles |
| Transfer within same legal entity | Not a supply between persons | Article 2 |
| Intra-GCC (implementing state to implementing state) | Treated under GCC customs union transitional rules | Unified Agreement, transitional provisions |

---

## Step 2: VAT Return Form -- Field Mapping

### 2a. VAT Return Structure (Complete) [T1]

The Saudi VAT return is filed electronically via the ZATCA portal. The return is divided into sections:

**Legislation:** VAT Law, Article 59 (returns); VAT Implementing Regulations, Article 59.

#### Section 1: Standard Rated Sales

| Field | Description |
|-------|-------------|
| Field 1 | Sales subject to standard rate (15%) -- VAT-exclusive amount |
| Field 2 | VAT amount on standard rated sales (Field 1 x 15%) |

#### Section 2: Sales to GCC Countries (Implementing States)

| Field | Description |
|-------|-------------|
| Field 3 | Sales to customers in GCC implementing states -- VAT-exclusive amount |
| Field 4 | VAT amount on GCC sales |

#### Section 3: Zero-Rated Sales

| Field | Description |
|-------|-------------|
| Field 5 | Zero-rated domestic sales -- VAT-exclusive amount |
| Field 6 | Exports -- VAT-exclusive amount |

#### Section 4: Exempt Sales

| Field | Description |
|-------|-------------|
| Field 7 | Exempt sales -- VAT-exclusive amount |

#### Section 5: Standard Rated Purchases

| Field | Description |
|-------|-------------|
| Field 8 | Purchases subject to standard rate (15%) -- VAT-exclusive amount |
| Field 9 | VAT on standard rated purchases (Field 8 x 15%) |

#### Section 6: Imports Subject to VAT (Reverse Charge)

| Field | Description |
|-------|-------------|
| Field 10 | Imports subject to VAT paid at Customs -- VAT-exclusive amount |
| Field 11 | VAT paid at Customs |

#### Section 7: Imports Subject to VAT (Accounted for via Reverse Charge Mechanism)

| Field | Description |
|-------|-------------|
| Field 12 | Imports accounted for through reverse charge -- VAT-exclusive amount |
| Field 13 | VAT on reverse charge imports (Field 12 x 15%) |

#### Section 8: Purchases Subject to Zero Rate

| Field | Description |
|-------|-------------|
| Field 14 | Zero-rated purchases -- VAT-exclusive amount |

#### Section 9: Exempt Purchases

| Field | Description |
|-------|-------------|
| Field 15 | Exempt purchases -- VAT-exclusive amount |

#### Section 10: Adjustments and Corrections

| Field | Description |
|-------|-------------|
| Field 16 | Adjustments to output VAT (credit notes issued, corrections to previous periods) |
| Field 17 | Adjustments to input VAT (credit notes received, corrections to previous periods) |

#### Section 11: Total VAT Due

| Field | Description |
|-------|-------------|
| Field 18 | Total output VAT: Field 2 + Field 4 + Field 13 + Field 16 |
| Field 19 | Total input VAT: Field 9 + Field 11 + Field 17 |
| Field 20 | Net VAT due: Field 18 - Field 19 |

### 2b. Derived Calculations [T1]

```
Field 2  = Field 1 x 15%
Field 4  = Field 3 x 15%
Field 9  = Field 8 x 15%
Field 13 = Field 12 x 15%

Field 18 = Field 2 + Field 4 + Field 13 + Field 16
Field 19 = Field 9 + Field 11 + Field 17

IF Field 18 > Field 19 THEN
    Field 20 = Field 18 - Field 19    -- Net VAT payable
ELSE
    Field 20 = Field 18 - Field 19    -- Net VAT refundable (negative value)
END
```

---

## Step 3: Transaction Classification Rules

### 3a. Determine Transaction Type [T1]

- Sale/revenue (output VAT) or Purchase/expense (input VAT)
- Salaries, wages, government levies, zakat, loan repayments, dividends = OUT OF SCOPE (never on VAT return)

**Legislation:** VAT Law, Article 2 (definition of taxable supply), Article 9 (supply of goods and services).

### 3b. Determine Counterparty Location [T1]

| Location | Classification |
|----------|---------------|
| Saudi Arabia (domestic) | Local supply, standard 15% or zero-rated or exempt |
| GCC implementing state | GCC rules (currently only UAE, Bahrain -- others not yet implementing) |
| GCC non-implementing state | Treated as export (zero-rated if export conditions met) |
| Outside GCC | Export (zero-rated if conditions met) or import (reverse charge/customs) |

**GCC implementing states (as at 2026):** UAE (1 Jan 2018, 5%), Bahrain (1 Jan 2019, increased to 10% on 1 Jan 2022), Oman (16 April 2021, 5%). Kuwait and Qatar have not yet implemented VAT.

### 3c. Sales Classification [T1]

| Type | Field 1/2 | Field 3/4 | Field 5/6 | Field 7 | Notes |
|------|-----------|-----------|-----------|---------|-------|
| Standard domestic sale | Yes | -- | -- | -- | 15% VAT |
| Sale to GCC implementing state customer | -- | Yes | -- | -- | 15% VAT (transitional) |
| Zero-rated domestic sale | -- | -- | Field 5 | -- | No VAT |
| Export outside GCC | -- | -- | Field 6 | -- | No VAT, proof of export required |
| Exempt sale | -- | -- | -- | Yes | No VAT, no input recovery |

### 3d. Purchases Classification [T1]

| Type | Field | Notes |
|------|-------|-------|
| Standard domestic purchase | Field 8/9 | 15% VAT, input recoverable (subject to rules) |
| Import cleared at Customs | Field 10/11 | VAT paid to Customs, recoverable as input |
| Import via reverse charge (services, intangibles) | Field 12/13 | Self-assess output AND claim input (net zero for fully taxable) |
| Zero-rated purchase | Field 14 | No VAT content |
| Exempt purchase | Field 15 | No input VAT recovery |

---

## Step 4: Input Tax Recovery Rules

### 4a. General Entitlement [T1]

A taxable person may deduct input VAT on goods and services acquired for the purpose of making taxable supplies (standard-rated or zero-rated).

**Legislation:** VAT Law, Article 46 (input tax deduction); IR Article 46.

**Requirements:**
1. The person must be registered for VAT
2. The goods/services must be for making taxable supplies
3. A valid tax invoice must be held (or Customs declaration for imports)
4. The input VAT must have been correctly charged

### 4b. Blocked Input Tax Categories [T1]

The following categories are specifically blocked from input tax recovery:

| Category | Legislation |
|----------|-------------|
| Motor vehicles (purchase, lease, running costs) -- unless the vehicle is essential to the business (e.g., taxi, delivery, car rental, transportation business) | IR Article 49(3) |
| Entertainment, hospitality, and recreation expenses for employees or non-business purposes | IR Article 49(4) |
| Services for personal benefit of employees (housing, childcare) unless legally required | IR Article 49(5) |
| Goods and services acquired for making exempt supplies | Article 46(1) |

### 4c. Apportionment for Mixed Supplies [T2]

If a taxable person makes both taxable and exempt supplies, input VAT must be apportioned:

**Step 1 -- Direct attribution:**
- Input VAT directly attributable to taxable supplies: fully recoverable
- Input VAT directly attributable to exempt supplies: not recoverable

**Step 2 -- Residual input VAT (overheads):**
```
Recovery % = (Value of taxable supplies / Total value of all supplies) x 100
```

**Annual adjustment:** Required at end of calendar year based on actual ratios for the year.

**Legislation:** VAT Law, Article 50; IR Article 50.

**Flag for reviewer: apportionment ratio must be confirmed by qualified tax consultant before applying.**

### 4d. Capital Assets Scheme [T2]

For capital assets with input VAT exceeding SAR 250,000:
- Adjustment period: 5 years for movable assets, 10 years for immovable property (real estate)
- Annual comparison of actual use vs initial claim
- Adjustment = (1/5 or 1/10) x Full input VAT x (Current year % taxable use - Initial % taxable use)

**Legislation:** VAT Implementing Regulations, Article 51.

---

## Step 5: Reverse Charge Mechanics

### 5a. When Reverse Charge Applies [T1]

The reverse charge mechanism applies when:
1. A non-resident person who is not registered for VAT in KSA makes a taxable supply to a registered person in KSA
2. The supply is of services, intangibles, or goods in certain circumstances

**Legislation:** VAT Law, Article 47 (reverse charge); IR Article 47.

### 5b. Reverse Charge Treatment [T1]

For qualifying imports via reverse charge:
1. Report the VAT-exclusive value in Field 12
2. Self-assess output VAT at 15% in Field 13
3. Claim input VAT (if entitled) in Field 19 (via Field 9 or aggregated)
4. Net effect: zero for fully taxable businesses

**Both sides must be shown on the return.**

### 5c. Exceptions to Reverse Charge [T1]

| Situation | Treatment |
|-----------|-----------|
| Non-resident supplier IS registered for VAT in KSA | Normal supply, not reverse charge |
| Import of physical goods cleared at Customs | VAT collected at border (Field 10/11), not reverse charge |
| Supply by non-resident to non-registered person | Non-resident must register and charge VAT |

---

## Step 6: E-Invoicing (Fatoorah) Requirements

### 6a. Overview [T1]

Saudi Arabia has implemented mandatory e-invoicing in two phases under the E-Invoicing Regulation issued by ZATCA.

**Legislation:** E-Invoicing Regulation (Resolution dated 4/12/1442H, 4 December 2020).

### 6b. Phase 1 -- Generation Phase [T1]

| Item | Detail |
|------|--------|
| Effective date | 4 December 2021 |
| Requirement | All VAT-registered taxpayers must generate, store, and share electronic invoices and electronic notes using compliant e-invoicing solutions |
| Format | XML or PDF/A-3 with embedded XML |
| Prohibitions | Handwritten invoices prohibited; unstructured electronic invoices prohibited |
| QR code | Required on simplified (B2C) invoices; optional on standard (B2B) invoices in Phase 1 |
| Storage | E-invoices must be stored for minimum 6 years |

### 6c. Phase 2 -- Integration Phase [T1]

| Item | Detail |
|------|--------|
| Effective date | Rolling waves starting 1 January 2023 |
| Wave 1 | Taxpayers with annual revenue > SAR 3,000,000,000 (from 1 January 2023) |
| Wave 2 | Taxpayers with annual revenue > SAR 500,000,000 (from 1 July 2023) |
| Subsequent waves | Revenue thresholds progressively lowered; ZATCA notifies taxpayers at least 6 months before their go-live date. As at April 2026: Wave 22 (revenue > SAR 1M, deadline 31 Dec 2025), Wave 23 (revenue > SAR 750K, deadline 31 Mar 2026), Wave 24 (revenue > SAR 375K, deadline 30 Jun 2026). Revenue reference years: 2022, 2023, or 2024. |
| Requirement | E-invoices must be reported to and validated by ZATCA platform (FATOORA) in near-real-time for standard invoices; within 24 hours for simplified invoices |
| UUID | Each invoice assigned a unique identifier by ZATCA |
| Cryptographic stamp | ZATCA applies a cryptographic stamp to validated invoices |
| QR code | Mandatory on ALL invoices (B2B and B2C) in Phase 2 |

### 6d. QR Code Requirements [T1]

The QR code on invoices must encode (at minimum):

| Field | Description |
|-------|-------------|
| 1 | Seller's name |
| 2 | Seller's VAT registration number |
| 3 | Invoice date and time (timestamp) |
| 4 | Invoice total (including VAT) |
| 5 | VAT amount |

For Phase 2, additional fields are required including the cryptographic hash and digital signature.

### 6e. Invoice Types [T1]

| Type | Usage | Requirements |
|------|-------|-------------|
| Standard (tax) invoice | B2B transactions and exports | Full details: buyer/seller info, line items, VAT breakdown, sequential numbering |
| Simplified (tax) invoice | B2C transactions under SAR 1,000 | Reduced requirements: seller info, QR code, total with VAT |

### 6f. Credit Notes and Debit Notes [T1]

Credit notes and debit notes must also be issued electronically and reference the original invoice. They follow the same e-invoicing requirements as the original invoice type.

**Legislation:** VAT Implementing Regulations, Article 54 (credit notes); E-Invoicing Regulation.

---

## Step 7: Registration Rules

### 7a. Registration Thresholds [T1]

| Type | Threshold | Legislation |
|------|-----------|-------------|
| Mandatory registration | Annual taxable supplies (including imports subject to reverse charge) exceed SAR 375,000 | VAT Law, Article 50(1); IR Article 7 |
| Voluntary registration | Annual taxable supplies (or eligible expenses) exceed SAR 187,500 | VAT Law, Article 50(3); IR Article 8 |
| Non-resident mandatory registration | Any taxable supplies in KSA (no threshold) | VAT Law, Article 50(2) |
| Group registration | Two or more related legal persons may register as a single taxable person | VAT Law, Article 51; IR Article 10 |

### 7b. Deregistration [T1]

| Type | Condition | Legislation |
|------|-----------|-------------|
| Mandatory deregistration | Taxable supplies fall below SAR 187,500 for 12 consecutive months | IR Article 13 |
| Voluntary deregistration | After minimum 12 months of registration, if taxable supplies below SAR 375,000 | IR Article 13 |

---

## Step 8: Filing Frequency and Deadlines

### 8a. Filing Periods [T1]

| Frequency | Eligibility | Legislation |
|-----------|-------------|-------------|
| Monthly | Annual taxable supplies exceed SAR 40,000,000 | VAT Law, Article 59(2) |
| Quarterly | Annual taxable supplies of SAR 40,000,000 or less | VAT Law, Article 59(2) |

### 8b. Quarterly Periods [T1]

| Quarter | Period |
|---------|--------|
| Q1 | 1 January - 31 March |
| Q2 | 1 April - 30 June |
| Q3 | 1 July - 30 September |
| Q4 | 1 October - 31 December |

### 8c. Due Dates [T1]

| Item | Due Date | Legislation |
|------|----------|-------------|
| VAT return filing | Last day of the month following the end of the tax period | VAT Law, Article 60 |
| VAT payment | Last day of the month following the end of the tax period (same as filing) | VAT Law, Article 60 |

**Example:** For Q1 (Jan-Mar), the return and payment are due by 30 April.
**Example:** For the month of January (monthly filer), the return and payment are due by 28/29 February.

---

## Step 9: Penalties

### 9a. Penalty Schedule [T1]

| Offence | Penalty | Legislation |
|---------|---------|-------------|
| Late registration | SAR 10,000 | VAT Law, Article 62 |
| Late filing of VAT return | 5% to 25% of unpaid VAT for the period | VAT Law, Article 62; IR Article 62 |
| Late payment of VAT | 5% of unpaid VAT for each month (or part month) of delay | VAT Law, Article 62 |
| Failure to issue tax invoice / e-invoice | SAR 5,000 to SAR 50,000 per invoice | VAT Law, Article 62; E-Invoicing Regulation |
| Incorrect VAT return (unintentional) | 50% of the difference between correct and filed tax | VAT Law, Article 62 |
| Tax evasion | 25% to 200% of evaded tax + potential criminal penalties | VAT Law, Article 62 |
| Failure to maintain records | SAR 50,000 per instance | VAT Law, Article 62 |
| Failure to submit information to ZATCA | SAR 1,000 per item (up to SAR 100,000) | VAT Law, Article 62 |
| E-invoicing non-compliance | Warning for first offence, then SAR 1,000 per invoice, escalating | E-Invoicing Regulation penalties |

### 9b. Voluntary Disclosure [T1]

Taxpayers may submit a voluntary disclosure for errors in previously filed returns:
- If error results in VAT difference of SAR 5,000 or less: correct in next return
- If error results in VAT difference of more than SAR 5,000: submit voluntary disclosure form via ZATCA portal
- Reduced penalties may apply for voluntary disclosure before ZATCA audit

**Legislation:** VAT Implementing Regulations, Article 63.

---

## Step 10: Key Thresholds Lookup Table

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory registration | SAR 375,000 annual taxable supplies | Article 50(1) |
| Voluntary registration | SAR 187,500 annual taxable supplies/expenses | Article 50(3) |
| Monthly filing | SAR 40,000,000 annual taxable supplies | Article 59(2) |
| Voluntary disclosure (correction in next return) | SAR 5,000 or less VAT difference | IR Article 63 |
| Simplified invoice threshold | SAR 1,000 (transaction value) | IR Article 53(7) |
| Capital asset adjustment (movable) | Input VAT > SAR 250,000, 5-year period | IR Article 51 |
| Capital asset adjustment (immovable) | Input VAT > SAR 250,000, 10-year period | IR Article 51 |
| Record retention | 6 years minimum | VAT Law, Article 64 |
| Housing VAT/RETT relief cap | SAR 1,000,000 (first residential property) | Royal Decree A/84 |
| Late registration penalty | SAR 10,000 fixed | Article 62 |

---

## Step 11: Real Estate Rules

### 11a. Commercial Real Estate [T1]

| Transaction | Treatment | Rate | Legislation |
|-------------|-----------|------|-------------|
| Sale of commercial property | Taxable supply | 15% | Article 9 (standard supply) |
| Lease of commercial property | Taxable supply | 15% | Article 9 |
| Sale of bare commercial land | Taxable supply | 15% | Article 9 |

### 11b. Residential Real Estate [T2]

| Transaction | Treatment | Rate | Legislation |
|-------------|-----------|------|-------------|
| First supply of residential property (within 3 years) | Zero-rated (up to SAR 1,000,000) | 0% | Article 36(3); Royal Decree A/84 housing relief |
| First supply above SAR 1,000,000 | 15% on amount exceeding the cap | 15% on excess | Housing relief rules |
| Subsequent supply of residential property | Exempt | Exempt | Article 30 |
| Lease of residential property | Exempt | Exempt | Article 30 |
| Sale of residential land (bare) | Exempt from VAT; subject to RETT at 5% | Exempt (VAT) | Real Estate Transaction Tax Law |

**Flag for reviewer: "first supply" determination and the SAR 1,000,000 cap calculation require careful analysis. Confirm whether the supply qualifies.**

### 11c. Real Estate Transaction Tax (RETT) [T1]

From 4 October 2020, real estate transactions exempt from VAT are subject to RETT at 5% of the transaction value. RETT replaced the previous 15% VAT on real estate dispositions that are now exempt.

**Legislation:** Real Estate Transaction Tax Law (Royal Decree A/84).

---

## Step 12: Designated Zones

### 12a. Overview [T2]

Certain areas in KSA are designated as "Qualifying Economic Zones" or "Designated Zones" where specific VAT rules apply:

| Rule | Description | Legislation |
|------|-------------|-------------|
| Goods within designated zone | Movement of goods within a designated zone is not treated as a supply | IR Article 39 |
| Goods between designated zones | Transfer of goods between qualifying designated zones may be outside scope of VAT | IR Article 39 |
| Goods from designated zone to KSA mainland | Treated as an import into KSA; VAT applies | IR Article 39 |
| Services in designated zone | Standard VAT rules apply to services (no special treatment) | IR Article 39 |

**Flag for reviewer: confirm whether the specific zone qualifies under ZATCA's designated zone rules. Not all free zones automatically qualify.**

---

## Step 12A: Recent Changes (April 2025 Amendments and Penalty Amnesty)

### 12Aa. April 2025 VAT Implementing Regulations Amendments [T2]

On 18 April 2025, ZATCA published Board Resolution No. 01-06-24, amending the VAT Implementing Regulations. Key changes:

| Change | Effective Date | Detail |
|--------|---------------|--------|
| VAT grouping (Article 10, Para 1) | 15 October 2025 | Updated rules for related entities forming VAT groups |
| Deemed supplier for electronic marketplaces (Article 47, Para 3) | 1 January 2026 | Digital platforms facilitating sales by non-resident or unregistered suppliers become liable for VAT collection. The platform is treated as having acquired and supplied the goods/services on its own account. Exceptions apply where the non-resident supplier is explicitly the principal supplier and the platform does not set terms, determine consideration, collect payment, handle complaints, or offer promotions. |
| Transfer of economic activity | Various | Updated rules on going-concern transfers |
| Special/designated zones | Various | Revised treatment for supplies to or within special zones |
| Tourist VAT refunds | Various | Updated designated person provisions for administering tourist refunds |

**Flag for reviewer: businesses operating digital platforms or electronic marketplaces must assess deemed supplier obligations before 1 January 2026.**

**Legislation:** Board Resolution No. 01-06-24; PWC Tax Alert May 2025; KPMG Tax Flash April 2025.

### 12Ab. Penalty Waiver / Amnesty Initiative [T1]

ZATCA's penalty cancellation and fine exemption initiative has been extended to **30 June 2026** (per Minister of Finance decision, effective 1 January 2026). The initiative covers:

- Late registration penalties (all tax systems)
- Late filing penalties (all tax systems)
- Late payment penalties
- VAT return correction penalties
- E-invoicing field inspection violation fines

**Requirements:** Taxpayer must be registered, submit all required returns, and pay the full principal tax liability. The initiative covers VAT, Excise Tax, RETT, WHT, and CIT.

**Legislation:** ZATCA penalty waiver initiative; Minister of Finance decision (December 2025 extension).

---

## Step 13: PROHIBITIONS [T1]

- NEVER let AI guess VAT classification -- it is deterministic from facts and legislation
- NEVER claim input tax on blocked categories (motor vehicles for private use, entertainment for non-business purposes)
- NEVER claim input tax on expenses related to exempt supplies without apportionment
- NEVER treat residential rental as taxable -- it is EXEMPT
- NEVER treat lease of commercial property as exempt -- it is TAXABLE at 15%
- NEVER issue non-electronic invoices -- all invoices must be e-invoices since 4 December 2021
- NEVER zero-rate a domestic supply without specific legislation supporting the zero-rating
- NEVER confuse zero-rated (input tax claimable) with exempt (input tax NOT claimable)
- NEVER file a return using GST-inclusive figures -- Saudi VAT returns use VAT-EXCLUSIVE amounts for the base
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER apply former 5% rate to supplies made after 1 July 2020 (subject to transitional rules for pre-existing contracts)
- NEVER ignore the SAR 5,000 voluntary disclosure threshold -- errors above this amount require a separate disclosure
- NEVER treat a sale of residential property as exempt if it is the first supply within 3 years -- it may be zero-rated
- NEVER assume all free zones are designated zones -- each must be specifically designated by ZATCA

---

## Step 14: Edge Case Registry

### EC1 -- Real Estate: First Supply vs Subsequent Supply [T2]

**Situation:** Developer sells a new apartment to a buyer. The building was completed 2 years ago and this is the first sale.
**Resolution:** This is a "first supply" of residential real estate within 3 years of completion. Zero-rated up to SAR 1,000,000 of the purchase price. VAT at 15% applies on any amount exceeding SAR 1,000,000. Buyer must be a Saudi citizen purchasing their first home for the government relief to apply.
**Legislation:** VAT Law, Article 36(3); Housing VAT relief program (Ministry of Housing/ZATCA).
**Flag for reviewer:** Confirm first-supply status and eligibility for housing relief.

### EC2 -- Designated Zone: Goods Transfer to Mainland [T1]

**Situation:** Company in a designated zone sells goods to a customer on the KSA mainland. Goods are shipped from the designated zone.
**Resolution:** Treated as an import into KSA. VAT at 15% applies. The goods are treated as if imported from outside KSA. Buyer accounts for VAT (at customs or via reverse charge mechanism depending on arrangement).
**Legislation:** VAT Implementing Regulations, Article 39.

### EC3 -- E-Invoicing: Phase 2 Non-Compliance [T1]

**Situation:** A taxpayer in Phase 2 wave issues invoices without connecting to ZATCA's FATOORA platform for validation.
**Resolution:** Non-compliant. Invoices without ZATCA validation are not valid tax invoices. Buyer cannot claim input tax based on non-validated invoices. Seller faces penalties (warning for first offence, then SAR 1,000+ per invoice).
**Legislation:** E-Invoicing Regulation; ZATCA penalties schedule.

### EC4 -- Oil and Gas Sector [T3]

**Situation:** Oil company makes supplies under a government concession arrangement.
**Resolution:** ESCALATE. The oil and gas sector has special rules regarding government concessions, deemed supplies, and the treatment of crude oil transfers. These rules are complex and require specialized knowledge.
**Legislation:** VAT Implementing Regulations, various sector-specific provisions.
**Action:** Refer to specialized oil & gas tax consultant.

### EC5 -- Related Party Transactions [T2]

**Situation:** Company sells goods to a related company at below-market value. Both are registered for VAT.
**Resolution:** ZATCA may adjust the value to open market value for VAT purposes under the related party rules. If the recipient cannot claim full input tax, ZATCA will deem the supply at market value. If both parties are fully taxable, no adjustment (net effect zero).
**Legislation:** VAT Law, Article 26 (related party supplies); IR Article 26.
**Flag for reviewer:** Confirm related party status and whether both parties are fully taxable.

### EC6 -- GCC Customs Union: Goods Moving Between KSA and UAE [T2]

**Situation:** KSA registered company sells goods to UAE registered company. Goods are physically shipped from KSA to UAE.
**Resolution:** Under the transitional GCC rules (until full GCC electronic services system is implemented), the export from KSA is zero-rated if proof of export is obtained. The UAE customer accounts for import VAT in UAE. Standard export documentation required.
**Legislation:** Unified VAT Agreement for GCC States; transitional provisions.
**Flag for reviewer:** GCC transitional rules are evolving. Confirm current treatment with latest ZATCA guidance.

### EC7 -- Tourist Refund Scheme [T1]

**Situation:** Tourist purchases goods in KSA and requests a VAT refund on departure.
**Resolution:** Saudi Arabia launched a VAT refund scheme for tourists. Eligible tourists can claim refunds on purchases from participating retailers. The refund is processed through an approved operator (Planet). Minimum purchase amount and conditions apply.
**Legislation:** ZATCA tourist refund scheme regulations.

### EC8 -- Profit Margin Scheme [T2]

**Situation:** Dealer in secondhand goods (e.g., used cars) wants to account for VAT only on the profit margin rather than the full selling price.
**Resolution:** The KSA VAT law includes a profit margin scheme for eligible goods. VAT is calculated on the difference between the purchase price and the selling price (margin). The dealer must maintain records of both prices. Not all goods qualify.
**Legislation:** VAT Implementing Regulations, Article 44 (profit margin scheme).
**Flag for reviewer:** Confirm eligibility for profit margin scheme.

### EC9 -- Deemed Supplies [T1]

**Situation:** Registered person transfers business assets for non-business purposes (e.g., personal use), or provides free goods/services to employees above de minimis thresholds.
**Resolution:** Treated as a deemed supply. Output VAT at 15% must be accounted for on the open market value of the goods/services. This applies to gifts of goods valued above SAR 200 per recipient per year.
**Legislation:** VAT Law, Article 14 (deemed supplies); IR Article 14.

### EC10 -- Credit Notes and Adjustments [T1]

**Situation:** Registered person issues a credit note to a customer for a price reduction or returned goods.
**Resolution:** Reduce Field 1 (or appropriate sales field) by the credit note amount. Output VAT is reduced accordingly. Credit notes must be e-invoiced with reference to the original invoice. Enter the net adjustment in Field 16 if correcting a prior period.
**Legislation:** VAT Implementing Regulations, Article 54 (credit notes).

### EC11 -- Government Entities as Taxable Persons [T2]

**Situation:** A government entity undertakes commercial activities (e.g., leasing commercial property, providing commercial services) alongside its sovereign functions.
**Resolution:** Government entities are taxable persons for their commercial (non-sovereign) activities. They must register for VAT if their taxable commercial supplies exceed SAR 375,000. Sovereign activities remain outside the scope of VAT.
**Legislation:** VAT Law, Article 10 (government entities); IR Article 9.
**Flag for reviewer:** Determine which activities are commercial vs. sovereign.

### EC12 -- Pre-1 July 2020 Contracts (Transitional Rules) [T1]

**Situation:** A contract was signed before 11 May 2020 at 5% VAT. Supplies continued after 1 July 2020.
**Resolution:** Supplies made after 1 July 2020 under contracts entered before 11 May 2020 may continue at 5% until 30 June 2021 (or contract renewal/amendment date, whichever is earlier). After 30 June 2021, all supplies are at 15% regardless of contract date.
**Legislation:** Transitional provisions under Royal Decree A/638; ZATCA guidelines on transitional rules.

---

## Step 15: Comparison with EU VAT

| Feature | Saudi Arabia VAT | EU VAT (Standard) |
|---------|------------------|--------------------|
| Rate structure | Single rate: 15% (plus zero and exempt) | Multiple rates per member state (standard, reduced, super-reduced, zero) |
| Rate history | 5% (2018-2020), 15% (2020-present) | Varies by state, generally stable |
| Return basis | VAT-exclusive amounts | VAT-exclusive amounts (most states) |
| E-invoicing | Mandatory (Phase 1 generation, Phase 2 integration with ZATCA) | Varies by state (mandatory in Italy, France upcoming, voluntary in most) |
| QR code | Mandatory on all invoices (Phase 2) | Generally not required (some states for B2C) |
| Reverse charge | On imports of services from non-registered non-residents | On intra-EU B2B services and specific domestic supplies |
| Registration threshold | SAR 375,000 (~EUR 93,000) mandatory | Varies by state (EUR 0 to EUR 85,000) |
| Capital goods adjustment | 5 years (movable), 10 years (immovable); only if input VAT > SAR 250,000 | 5 years (movable), 10-20 years (immovable); varies by state |
| Profit margin scheme | Available for eligible secondhand goods | Available (margin scheme for travel agents, auctioneers, secondhand goods) |
| Real estate | First supply zero-rated (up to SAR 1,000,000 cap), subsequent exempt, commercial taxable | Varies by state; generally new buildings taxable, used buildings exempt (option to tax) |
| Tourist refunds | Available via approved operators | Available via global blue/planet etc. |
| Group registration | Available for related entities | Available in most member states |
| GCC customs union | Transitional rules between implementing states | Full single market with intra-community rules |
| Filing frequency | Monthly (>SAR 40M) or quarterly | Monthly (most states) or quarterly |
| Penalty for late filing | 5%-25% of unpaid tax | Varies by state |
| Fiscal representative | Required for non-resident without establishment | Required in many states for non-EU businesses |

---

## Step 16: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed Saudi tax consultant must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Saudi tax consultant. Document gap.
```

---

## Step 17: Test Suite

### Test 1 -- Standard Domestic Sale at 15% [T1]

**Input:** KSA registered company sells goods to KSA customer. Invoice: SAR 10,000 + SAR 1,500 VAT = SAR 11,500 total. Standard rated.
**Expected output:** Field 1 = SAR 10,000. Field 2 = SAR 1,500. No other sales fields affected.

### Test 2 -- Export Sale (Zero-Rated) [T1]

**Input:** KSA registered company exports goods to a customer in India. Invoice: SAR 50,000 (zero-rated). Proof of export obtained.
**Expected output:** Field 6 = SAR 50,000. No VAT. Fields 1-4 and 7 = no entry for this transaction.

### Test 3 -- Standard Domestic Purchase with Input Recovery [T1]

**Input:** KSA registered company (fully taxable) purchases office equipment from local supplier. Invoice: SAR 5,000 + SAR 750 VAT = SAR 5,750 total.
**Expected output:** Field 8 = SAR 5,000. Field 9 = SAR 750. Full input recovery.

### Test 4 -- Import of Services via Reverse Charge [T1]

**Input:** KSA registered company (fully taxable) purchases consulting services from a UK firm not registered in KSA. Invoice: SAR 20,000 (no VAT charged).
**Expected output:** Field 12 = SAR 20,000. Field 13 = SAR 3,000 (output VAT at 15%). Input VAT claim = SAR 3,000 (included in Field 19). Net effect = zero.

### Test 5 -- Exempt Sale: Residential Rental [T1]

**Input:** KSA registered property company earns SAR 8,000/month from residential rental.
**Expected output:** Field 7 = SAR 8,000. No output VAT. Input tax on expenses related to residential rental: NOT claimable.

### Test 6 -- Blocked Input Tax: Employee Entertainment [T1]

**Input:** KSA registered company hosts a staff party. Catering bill SAR 15,000 + SAR 2,250 VAT.
**Expected output:** Field 8 = SAR 15,000. Field 9 = SAR 0 (VAT BLOCKED -- entertainment for employees). Input tax NOT recoverable. The SAR 2,250 is a cost to the business.

### Test 7 -- First Supply of Residential Property (Zero-Rated) [T2]

**Input:** Developer sells new apartment (completed 1 year ago, first sale) to eligible Saudi citizen. Price: SAR 1,100,000.
**Expected output:** First SAR 1,000,000 is zero-rated (Field 5 = SAR 1,000,000). Remaining SAR 100,000 is taxable at 15% (Field 1 = SAR 100,000, Field 2 = SAR 15,000). Flag for reviewer: confirm first supply status and buyer eligibility.

### Test 8 -- Goods Imported at Customs [T1]

**Input:** KSA registered company imports machinery from Germany. Customs value: SAR 100,000. VAT of SAR 15,000 paid at border.
**Expected output:** Field 10 = SAR 100,000. Field 11 = SAR 15,000. Input VAT of SAR 15,000 recoverable (fully taxable business).

### Test 9 -- Related Party Transaction Below Market Value [T2]

**Input:** Company A (registered) sells goods to Company B (registered, related party). Invoice: SAR 10,000. Open market value: SAR 25,000. Both companies are fully taxable.
**Expected output:** Since both parties are fully taxable, no adjustment required by ZATCA (net effect is zero). Field 1 = SAR 10,000. Field 2 = SAR 1,500. Flag for reviewer: confirm both parties' fully taxable status.

### Test 10 -- Voluntary Disclosure: Error Above SAR 5,000 [T1]

**Input:** Company discovers it underreported output VAT by SAR 8,000 in a previous period.
**Expected output:** Since the VAT difference exceeds SAR 5,000, a separate voluntary disclosure must be filed via ZATCA portal. Cannot simply correct in the next return. Field 16 adjustment in a future return is NOT sufficient.

### Test 11 -- Credit Note Issued [T1]

**Input:** KSA registered company issues credit note to customer for SAR 2,000 + SAR 300 VAT for returned goods. Original sale was in the same period.
**Expected output:** Reduce Field 1 by SAR 2,000. Reduce Field 2 by SAR 300. Net sales for the period are reduced accordingly. If correcting a prior period, use Field 16 = -SAR 300.

### Test 12 -- Deemed Supply: Business Asset for Personal Use [T1]

**Input:** Registered person takes company laptop (original cost SAR 4,000) for personal use. Market value at time of transfer: SAR 2,500.
**Expected output:** Deemed supply at market value. Field 1 = SAR 2,500. Field 2 = SAR 375 (15% VAT on deemed supply value). Output VAT must be accounted for.

---

## Step 18: Out of Scope -- Zakat and Income Tax (Reference Only) [T3]

This skill does not compute Zakat or Corporate Income Tax. The following is reference information only. Escalate to qualified consultant.

- **Zakat:** 2.5% on Zakat base (net assets) for Saudi/GCC-owned entities
- **Corporate Income Tax (CIT):** 20% on adjusted profit for non-Saudi/non-GCC shareholders
- **Withholding Tax (WHT):** 5%-20% on payments to non-residents (royalties, technical services, rent, etc.)
- **Real Estate Transaction Tax (RETT):** 5% on real estate transactions (separate from VAT)
- **Excise Tax:** 50%-100% on tobacco, soft drinks, energy drinks, sweetened beverages

---

## Contribution Notes

If you are adapting this skill for another jurisdiction:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all field numbers with the equivalent fields on your jurisdiction's VAT return form.
3. Replace VAT rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace all SAR thresholds with your jurisdiction's equivalents in local currency.
5. Replace the e-invoicing requirements with your jurisdiction's electronic invoicing rules.
6. Replace blocked categories with your jurisdiction's equivalent non-deductible categories.
7. Have a qualified tax consultant in your jurisdiction validate every T1 rule before publishing.
8. Add your own edge cases to the Edge Case Registry.
9. Run all test suite cases against your jurisdiction's rules.
10. Update the comparison table to reflect differences from your jurisdiction's perspective.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
