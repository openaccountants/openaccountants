---
name: russia-vat
description: Use this skill whenever asked to prepare, review, or advise on a Russian VAT (NDS - Nalog na Dobavlennuyu Stoimost) return or any transaction classification for Russian VAT purposes. Trigger on phrases like "Russian VAT", "NDS", "Russian tax return", "VAT in Russia", "FNS filing", or any request involving Russian VAT obligations. This skill contains the complete Russian VAT classification rules, rate structure, return form mappings, deductibility rules, reverse charge treatment, and filing deadlines required to produce a correct return. NOTE: International sanctions regimes (EU, US, UK, and others) may significantly affect cross-border VAT treatment for Russian entities. Always flag sanctions-related issues as [T2] or [T3]. ALWAYS read this skill before touching any Russian VAT-related work.
---

# Russia VAT (NDS) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Russian Federation |
| Jurisdiction Code | RU |
| Tax Name | NDS (Nalog na Dobavlennuyu Stoimost / VAT) |
| Primary Legislation | Tax Code of the Russian Federation, Part Two, Chapter 21 (Articles 143-178) |
| Supporting Legislation | Government Decree No. 1137 (invoice rules); Federal Law No. 303-FZ (rate changes); Customs Code of the EAEU |
| Tax Authority | Federal Tax Service (FNS / Federalnaya Nalogovaya Sluzhba) |
| Filing Portal | https://lkfl2.nalog.ru (Personal Account); via certified electronic reporting operators |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, standard box assignment, basic reverse charge. Tier 2: sanctions impact, partial exemption, intercompany pricing, EAEU trade. Tier 3: transfer pricing disputes, complex group restructuring, criminal tax liability. |

---

## IMPORTANT: Sanctions Notice [T2]

Russia is subject to extensive international sanctions regimes imposed by the EU, US, UK, and other jurisdictions. These sanctions may affect:

- Cross-border supply chains and the ability to invoice or receive payment
- Import/export VAT treatment where goods are sanctioned
- The availability of reverse charge mechanisms with sanctioned counterparties
- Banking and payment processing for VAT refund claims
- Software and technology services from Western providers

**Any cross-border transaction involving a Russian entity must be flagged for sanctions compliance review before VAT treatment is determined. This is a [T2] minimum -- escalate to [T3] if the practitioner is uncertain about sanctions applicability.**

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and INN (Taxpayer Identification Number)** [T1] -- 10 digits for legal entities, 12 digits for individuals
2. **KPP (Registration Reason Code)** [T1] -- 9 digits, assigned to each branch/subdivision
3. **VAT registration status** [T1] -- General regime (OSNO) taxpayer, simplified regime (USN), or VAT-exempt under Article 145
4. **VAT period** [T1] -- quarterly (standard for all NDS payers)
5. **Industry/sector** [T2] -- impacts reduced rate eligibility and specific exemptions
6. **Does the business make exempt supplies under Article 149?** [T2] -- If yes, separate accounting required; partial deduction rules apply
7. **Does the business engage in cross-border trade?** [T2] -- Impacts EAEU rules, customs VAT, and sanctions screening
8. **Does the business operate in special economic zones?** [T2] -- May affect VAT obligations
9. **Accumulated VAT credits carried forward** [T1] -- from prior periods
10. **Is the business subject to international sanctions?** [T2] -- affects cross-border treatment

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output NDS) or Purchase (input NDS)
- Salaries, social contributions, dividend payments, loan principal repayments, fines/penalties, bank commission on loans = OUT OF SCOPE (never on NDS return)
- **Legislation:** Tax Code Chapter 21, Article 146 (taxable objects)

### 1b. Determine Counterparty Location [T1]
- Russia (domestic): supplier/customer is registered in Russian Federation
- EAEU: Armenia (AM), Belarus (BY), Kazakhstan (KZ), Kyrgyzstan (KG)
- Non-EAEU foreign: all other countries
- **Note:** EAEU members have special VAT rules under the Treaty on the Eurasian Economic Union

### 1c. Determine VAT Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 22% | Standard rate -- most goods and services (increased from 20% effective 1 January 2026 per Federal Law signed 28 November 2025) | Article 164(3) |
| 10% | Reduced rate -- food products (basic foodstuffs), children's goods, medical goods/equipment, periodicals/books (educational) | Article 164(2) |
| 0% | Zero rate -- exports, international transportation, space-related services, diplomatic supplies | Article 164(1) |

**Rate determination from invoice amounts:**
- Calculate: `rate = vat_amount / net_amount * 100`
- Normalize: <= 2% = 0%; 5-15% = 10%; >= 15% = 22%

### 1d. Reduced Rate (10%) -- Specific Categories [T1]

The 10% rate applies to the following under Article 164(2):

**Food products:**
- Meat and meat products (except delicacies: tongue, veal, suckling pig, balyk, etc.)
- Milk and dairy products
- Eggs and egg products
- Sugar, salt, flour, bread, cereals, pasta
- Vegetable oil, margarine
- Vegetables, fruits (domestic production)
- Baby food products
- Diabetic food products
- Fish (live, chilled, frozen -- except delicacy species)
- Seafood (except delicacy species: sturgeon, salmon, lobster, crab)

**Children's goods:**
- Children's clothing and footwear
- Baby beds, mattresses, carriages
- School supplies (notebooks, pens, pencils)
- Diapers
- Toys

**Medical goods:**
- Medicines (included in the Government-approved list)
- Medical devices (included in the Government-approved list)

**Publications:**
- Books and periodicals of educational, scientific, or cultural nature (excluding advertising and erotic content)

### 1e. Exempt Supplies (Article 149) [T1]

The following are exempt from NDS (no output tax, no input tax recovery):
- Medical services (licensed)
- Educational services (licensed, non-commercial)
- Financial services (banking, insurance, securities)
- Residential rental
- Religious articles (produced by religious organizations)
- Burial services
- Passenger transport (urban, suburban)
- Sale of residential property (secondary market)
- Certain cultural/artistic services

### 1f. Determine Expense Category [T1]
- Fixed assets: if acquisition value >= RUB 100,000 and useful life > 12 months (Article 256-257)
- Goods for resale: purchased to resell without transformation
- Raw materials/supplies: consumed in production
- Services/overheads: everything else (rent, utilities, consulting, etc.)

---

## Step 2: NDS Return Form Structure [T1]

**The NDS return (Nalogovaya deklaratsiya po NDS) is filed electronically via certified operators. The declaration consists of 12 sections:**

**Legislation:** Tax Code Article 174; FNS Order No. MMV-7-3/558@

### Section 1 -- Summary (Tax Payable/Refundable)

| Line | Description |
|------|-------------|
| 030 | NDS payable by non-NDS payers who issued invoices with NDS |
| 040 | NDS payable to the budget |
| 050 | NDS refundable from the budget |

### Section 3 -- Calculation of NDS Payable

| Line | Description | Rate |
|------|-------------|------|
| 010 | Taxable sales at 22% -- tax base | 22% |
| 010 (tax) | Output NDS on line 010 | calculated |
| 020 | Taxable sales at 10% -- tax base | 10% |
| 020 (tax) | Output NDS on line 020 | calculated |
| 030 | Sales at calculated rates (22/122 or 10/110) | varies |
| 040 | Output NDS on construction for own consumption | 22% |
| 050 | Output NDS on goods imported (transfer for own use) | varies |
| 070 | Advance payments received -- NDS | calculated |
| 080 | NDS on amounts related to taxable supplies | varies |
| 118 | TOTAL output NDS | sum |
| 120 | Input NDS on acquired goods/services/rights | deductible |
| 130 | Input NDS paid on imports | deductible |
| 150 | NDS paid as tax agent | deductible |
| 160 | NDS on construction for own consumption (deductible) | deductible |
| 170 | NDS on advances to suppliers (deductible) | deductible |
| 180 | NDS paid by tax agent (deductible as buyer) | deductible |
| 190 | TOTAL input NDS deductions | sum |
| 200 | NDS payable (if 118 > 190) | result |
| 210 | NDS refundable (if 190 > 118) | result |

### Section 4 -- Operations Taxed at 0% (Confirmed Exports)

| Line | Description |
|------|-------------|
| 010 | Transaction code |
| 020 | Tax base for confirmed 0% rate |
| 030 | Input NDS deductions related to 0% supplies |
| 040 | NDS previously claimed, now restored |

### Section 5 -- Previously Unconfirmed 0% Rate (Now Confirmed)

### Section 6 -- Unconfirmed 0% Rate Operations

| Line | Description |
|------|-------------|
| 010 | Transaction code |
| 020 | Tax base |
| 030 | NDS at 22% (or 10%) applied to unconfirmed exports |

### Section 7 -- Exempt Operations (Article 149)

### Section 8 -- Purchase Ledger (Kniga Pokupok) Data

Detailed invoice-by-invoice listing of all purchase invoices (scheta-faktury) claimed as input NDS deductions.

### Section 9 -- Sales Ledger (Kniga Prodazh) Data

Detailed invoice-by-invoice listing of all sales invoices (scheta-faktury) generating output NDS.

### Section 10 -- Intermediary (Agent/Commission) Operations -- Invoices Issued

### Section 11 -- Intermediary Operations -- Invoices Received

### Section 12 -- Invoices Issued by Non-NDS Payers / Exempt Persons

---

## Step 3: Reverse Charge and Tax Agent Mechanisms

### 3a. Tax Agent Obligations (Article 161) [T1]

In the following cases, the Russian buyer must withhold and remit NDS as a tax agent:

| Situation | Tax Agent Duty | Rate |
|-----------|---------------|------|
| Purchase of services from a foreign entity not registered in Russia | Buyer withholds NDS | 22% (or 10%) |
| Lease of federal/municipal property | Tenant withholds NDS | 22/122 |
| Purchase of state/municipal property | Buyer withholds NDS | 22/122 |
| Sale of confiscated property | Seller (agent) withholds NDS | 22/122 |
| Agency for foreign entity (no Russian registration) | Agent withholds NDS | 22/122 |

**Legislation:** Tax Code Article 161

### 3b. Tax Agent -- Foreign Services [T1]

When a Russian entity purchases services from a foreign entity with no Russian tax registration:
1. Determine place of supply under Article 148
2. If place of supply is Russia, buyer must withhold NDS at 22/122 from the payment
3. Withheld NDS is remitted to the budget on the payment date
4. Buyer claims the withheld NDS as input deduction in the same quarter (if entitled)

**Calculated rate formula:** `NDS = Payment Amount * 22 / 122`

### 3c. EAEU Imports [T2]

Goods imported from EAEU member states (Belarus, Kazakhstan, Armenia, Kyrgyzstan):
- NDS is NOT collected at the customs border
- Instead, buyer self-assesses NDS on the imported goods
- Files a separate EAEU import declaration (Statistical form) by the 20th of the month following the month of acceptance
- Pays the NDS by the same deadline
- Claims input NDS deduction after payment and filing

**Legislation:** Treaty on the EAEU, Protocol on Indirect Taxes; Tax Code Article 72 of the EAEU Treaty

### 3d. Non-EAEU Imports [T1]

Goods imported from non-EAEU countries:
- NDS is collected by Russian Customs at the border
- Customs NDS is recoverable as input NDS
- Requires customs declaration (DT) as documentary evidence
- Rate: 22% or 10% depending on goods classification

### 3e. Exports -- Zero Rate Confirmation [T2]

Exports are zero-rated under Article 164(1), but the exporter must confirm the 0% rate by submitting a documentary package to the FNS within 180 calendar days of the customs export declaration:

Required documents:
1. Export contract (or extract)
2. Customs declaration with export stamps
3. Transport/shipping documents with customs stamps
4. Bank statement confirming receipt of payment (if applicable)

**If 180-day deadline is missed:** The export is re-rated at 22% (or 10%). Output NDS must be charged. The exporter may later reclaim the 0% rate by submitting the documents within 3 years.

---

## Step 4: Input NDS Deduction Rules

### 4a. General Conditions for Deduction (Article 171-172) [T1]

Input NDS is deductible if ALL of the following conditions are met:
1. Goods/services are acquired for use in NDS-taxable operations
2. Goods/services are recorded in accounting (accepted on the books)
3. A properly executed invoice (schyot-faktura) is available
4. For imports: customs declaration and payment documents are available

### 4b. Blocked Input NDS (Non-Deductible) [T1]

Input NDS is NOT deductible in the following cases:

| Category | Legislation |
|----------|-------------|
| Goods/services used exclusively for exempt operations (Article 149) | Article 170(2)(1) |
| Goods/services used by non-NDS payers (USN, ENVD, patent) | Article 170(2)(3) |
| Goods/services used for operations outside Russian territory | Article 170(2)(2) |
| Entertainment expenses exceeding 4% of labor costs | Article 264(2) + Article 170 |
| Goods/services acquired with budget subsidies | Article 170(2.1) |
| Free distribution of goods for advertising (if unit cost > RUB 300) | Article 149(3)(25) / Article 170 |

### 4c. Partial Deduction (Separate Accounting) [T2]

If a business makes both taxable and exempt supplies:
- Must maintain separate accounting of input NDS
- Input NDS on goods/services used exclusively for taxable operations: fully deductible
- Input NDS on goods/services used exclusively for exempt operations: not deductible (included in cost)
- Input NDS on mixed-use goods/services: split proportionally

**Proportion formula:**
```
Deductible % = (Taxable revenue for quarter / Total revenue for quarter) * 100
```

**5% rule:** If exempt operations constitute 5% or less of total expenses for the quarter, the taxpayer may deduct ALL input NDS without separate accounting (Article 170(4)).

**Flag for reviewer: proportional split must be confirmed by qualified practitioner.**

### 4d. NDS on Advances [T1]

**Advances received (seller):**
- Output NDS must be charged on advance payments received: `NDS = Advance * 22/122`
- When goods/services are shipped, advance NDS is reversed and NDS is charged on the full supply
- Legislation: Article 167(1)(2)

**Advances paid (buyer):**
- Buyer MAY claim input NDS on advance payments to suppliers
- Requires advance invoice (schyot-faktura na avans) from supplier
- When goods/services are received, advance NDS deduction is reversed and replaced by standard deduction
- Legislation: Article 171(12), Article 172(9)

---

## Step 5: Derived Calculations [T1]

```
Total Output NDS (Section 3, line 118) =
    NDS on sales at 22% (line 010 tax)
  + NDS on sales at 10% (line 020 tax)
  + NDS at calculated rates (line 030 tax)
  + NDS on own-consumption construction (line 040)
  + NDS on advance payments received (line 070)
  + Other output NDS (line 080)

Total Input NDS Deductions (Section 3, line 190) =
    Input NDS on purchases (line 120)
  + Input NDS on imports (line 130)
  + NDS paid as tax agent (line 150)
  + NDS on own-consumption construction deductible (line 160)
  + NDS on advances paid (line 170)
  + Tax agent NDS deductible as buyer (line 180)

IF line 118 > line 190 THEN
    Line 200 = line 118 - line 190  (NDS payable)
    Line 210 = 0
ELSE
    Line 200 = 0
    Line 210 = line 190 - line 118  (NDS refundable)
END

Section 1, Line 040 = Line 200 (payable)
Section 1, Line 050 = Line 210 (refundable)
```

---

## Step 6: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| VAT exemption (Article 145) | Revenue <= RUB 2,000,000 for prior 3 consecutive months | Article 145 |
| Fixed asset classification | >= RUB 100,000 acquisition cost, > 12 months useful life | Article 256-257 |
| Export 0% confirmation deadline | 180 calendar days from customs export declaration | Article 165(9) |
| Advertising materials (free distribution exempt) | Unit cost <= RUB 300 | Article 149(3)(25) |
| 5% rule for separate accounting | Exempt expenses <= 5% of total expenses | Article 170(4) |
| Electronic invoice mandatory | All NDS payers (since 2014) | Article 169(1) |
| USN revenue threshold (exemption from NDS) | RUB 20,000,000 (2026); RUB 15,000,000 (2027); RUB 10,000,000 (from 2028) -- phased reduction | Article 145 / transitional provisions |
| USN revenue threshold (no NDS -- general USN eligibility) | RUB 265,800,000 (indexed annually) | Article 346.12 |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| NDS return (electronic) | Quarterly | 25th of the month following the quarter end | Article 174(5) |
| NDS payment (installment 1/3) | Quarterly | 28th of the month following the quarter end | Article 174(1) |
| NDS payment (installment 2/3) | Quarterly | 28th of the second month following quarter end | Article 174(1) |
| NDS payment (installment 3/3) | Quarterly | 28th of the third month following quarter end | Article 174(1) |
| EAEU import declaration | Monthly | 20th of the month following month of acceptance | EAEU Treaty Protocol |
| EAEU import NDS payment | Monthly | 20th of the month following month of acceptance | EAEU Treaty Protocol |
| Tax agent NDS (foreign services) | Per payment | Date of payment to foreign supplier | Article 174(4) |
| Export 0% documentary package | Per shipment | 180 days from customs declaration | Article 165(9) |

**NDS is paid in three equal installments** over the three months following the reporting quarter. Example: Q1 (Jan-Mar) NDS is paid 1/3 on April 28, 1/3 on May 28, 1/3 on June 28.

**Electronic filing is mandatory** for all NDS payers. Paper returns are not accepted (except for tax agents who are not NDS payers themselves, under specific conditions).

---

## Step 8: Invoice (Schyot-Faktura) Requirements [T1]

A valid schyot-faktura must contain (Article 169(5)):

| Field | Requirement |
|-------|------------|
| Sequential number and date | Mandatory |
| Seller name, address, INN/KPP | Mandatory |
| Buyer name, address, INN/KPP | Mandatory |
| Shipper and consignee (if different) | Mandatory for goods |
| Payment document reference (if advance) | Mandatory for advance invoices |
| Description of goods/services | Mandatory |
| Unit of measurement | Mandatory (OKEI code) |
| Quantity | Mandatory |
| Price per unit (excl. NDS) | Mandatory |
| Total amount (excl. NDS) | Mandatory |
| Excise amount (if applicable) | Mandatory |
| NDS rate | Mandatory (22%, 10%, 0%, or "bez NDS") |
| NDS amount | Mandatory |
| Total amount (incl. NDS) | Mandatory |
| Country of origin and customs declaration number | Mandatory for imported goods |
| Currency code | Mandatory |

**Invalid invoices result in denial of input NDS deduction.**

**Corrective invoices (ispravitelny schyot-faktura):** Issued to correct errors in original invoices.

**Adjustment invoices (korrektirovochny schyot-faktura):** Issued when the price or quantity changes after the original supply (Article 169(5.2)).

---

## Step 9: Edge Case Registry

### EC1 -- Purchase of services from a US software company (SaaS) [T2]

**Situation:** Russian company subscribes to a US-based SaaS platform. No NDS on the invoice.
**Resolution:** Since 2019, foreign providers of electronic services to Russian consumers (B2C) must register and pay NDS themselves. For B2B: the Russian buyer acts as tax agent and withholds NDS at 22/122. However, **sanctions may prevent payment processing** to certain US companies. Flag for reviewer: confirm (a) whether the US provider has registered for NDS in Russia under the "Google tax" rules, (b) whether sanctions affect the payment, (c) tax agent obligations.
**Legislation:** Article 161, Article 174.2

### EC2 -- Export of goods with missed 180-day deadline [T1]

**Situation:** Company exported goods but failed to collect confirmation documents within 180 days.
**Resolution:** The export must be treated as a domestic sale at 22% (or 10%). Output NDS is charged on the export value as of the date of shipment. The company may subsequently submit documents within the 3-year statute of limitations and reclaim the 0% rate and receive a refund.
**Legislation:** Article 165(9), Article 164(1)

### EC3 -- Advance payment received from customer [T1]

**Situation:** Company receives RUB 1,200,000 advance payment for future delivery.
**Resolution:** Output NDS on advance = RUB 1,200,000 * 22/122 = RUB 216,393 (rounded). Issue advance schyot-faktura. When goods are shipped, reverse the advance NDS and charge NDS on the full shipment amount. Section 3 line 070 for advance NDS; line 170 for reversal.
**Legislation:** Article 167(1)(2), Article 154(1)

### EC4 -- Import from Belarus (EAEU) [T2]

**Situation:** Russian company imports goods from Belarus.
**Resolution:** NDS is NOT collected at the customs border (no customs border within EAEU). Buyer self-assesses NDS on the import value. Files a separate statistical declaration by the 20th of the following month. Pays NDS by the same date. Claims input deduction after payment and filing. Rate depends on goods (20% or 10%).
**Legislation:** EAEU Treaty Protocol on Indirect Taxes, Article 72

### EC5 -- Mixed taxable and exempt operations [T2]

**Situation:** A company provides both taxable consulting services and exempt educational services.
**Resolution:** Separate accounting is mandatory. Input NDS on costs directly attributable to taxable operations is fully deductible. Input NDS on costs directly attributable to exempt operations is not deductible (added to cost). Mixed costs are split proportionally based on revenue. Check the 5% rule: if exempt expenses are <= 5% of total quarterly expenses, all input NDS may be deducted.
**Legislation:** Article 170(4), Article 149

### EC6 -- Free distribution of promotional goods [T1]

**Situation:** Company distributes branded merchandise to clients at no charge.
**Resolution:** If unit cost of each item <= RUB 300, the transfer is exempt from NDS under Article 149(3)(25). If unit cost > RUB 300, output NDS must be charged on the market value. Input NDS on the merchandise is deductible only if the transfer is NDS-taxable (i.e., cost > RUB 300).
**Legislation:** Article 146(1)(2), Article 149(3)(25)

### EC7 -- Construction for own consumption [T1]

**Situation:** Company builds a warehouse using its own workforce and materials.
**Resolution:** Construction for own consumption (khozyaystvennym sposobom) triggers output NDS at 22% on the cost of construction at quarter-end (Section 3, line 040). The same NDS is immediately deductible as input NDS (line 160), resulting in a net zero effect for fully taxable businesses. The tax base is the actual cost of construction (materials + labor + overheads).
**Legislation:** Article 146(1)(3), Article 159(2), Article 171(6)

### EC8 -- VAT refund claim triggering desk audit (kameral'naya proverka) [T2]

**Situation:** Company files an NDS return claiming a refund (line 050 populated).
**Resolution:** FNS will automatically conduct a desk audit (kameral'naya proverka) within 2 months (may be extended to 3 months). During the audit, FNS cross-references all invoices in Sections 8-9 against counterparties' returns. Discrepancies trigger additional information requests. Flag for reviewer: ensure all schyot-faktury are correct and counterparties have reported matching data. Consider whether an accelerated refund procedure (zayavitel'ny poryadok) is available under Article 176.1 (requires bank guarantee or history of large tax payments).
**Legislation:** Article 176, Article 88

### EC9 -- Digital services "Google Tax" [T2]

**Situation:** Foreign company provides digital services to Russian customers.
**Resolution:** Since January 2019, foreign providers of electronic/digital services must register with FNS and pay NDS at 22% (previously 20%, raised from 1 January 2026) on B2C supplies (Article 174.2). For B2B supplies, the Russian buyer acts as tax agent. If the foreign provider has registered and charges Russian NDS, the Russian buyer should NOT also withhold as tax agent. Flag for reviewer: verify whether the foreign provider is on the FNS registry of registered foreign digital service providers.
**Legislation:** Article 174.2, FNS Registry

### EC10 -- Sanctions-affected cross-border transaction [T2]

**Situation:** Russian company attempts to purchase goods/services from an EU supplier subject to EU sanctions.
**Resolution:** The VAT/NDS treatment cannot be determined independently of sanctions compliance. The transaction itself may be prohibited. Even if the transaction proceeds, banking restrictions may prevent payment and thus prevent tax agent obligations from being fulfilled. **Escalate to legal counsel for sanctions review before determining NDS treatment.** Do not classify until sanctions clearance is obtained.
**Legislation:** EU Regulations 833/2014 (as amended), US Executive Orders, UK Sanctions Regulations

---

## Step 10: Special Regimes and Exemptions [T2]

### USN (Simplified Tax System)
- USN payers are NOT NDS payers (Article 346.11)
- Exception: NDS on imports (customs and EAEU) must still be paid
- Exception: NDS as tax agent must still be withheld
- If a USN payer issues an invoice with NDS, they must remit that NDS to the budget (but cannot claim input deductions)
- Revenue threshold for USN eligibility: RUB 265,800,000 (indexed; check current year)

### Article 145 Exemption
- Available to taxpayers with revenue <= RUB 2,000,000 for 3 consecutive preceding calendar months
- Must notify FNS; exemption lasts 12 months (can be extended)
- Does not apply to excisable goods
- NDS on imports must still be paid
- Cannot claim input NDS during exemption period

### ENVD / Patent System
- ENVD was abolished from January 1, 2021
- Patent system (PSN) payers are not NDS payers (same exceptions as USN)

---

## Step 11: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Qualified tax practitioner must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified practitioner. Document gap.
```

---

## PROHIBITIONS [T1]

- NEVER let AI guess NDS treatment -- classification is deterministic from facts and legislation
- NEVER apply input NDS deduction without a valid schyot-faktura (invoice)
- NEVER allow USN/Patent payers to claim input NDS deductions
- NEVER apply 0% rate to exports without confirmed documentary evidence within 180 days
- NEVER ignore tax agent obligations on purchases from foreign entities
- NEVER classify sanctions-affected transactions without legal review [T2]
- NEVER confuse EAEU imports (self-assessed, no customs) with non-EAEU imports (customs-collected)
- NEVER apply the 5% rule without calculating actual exempt expenses as a percentage of total expenses
- NEVER accept paper NDS returns -- electronic filing is mandatory
- NEVER omit advance NDS when advance payments are received
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 12: Test Suite

### Test 1 -- Standard domestic sale at 22%

**Input:** Russian company sells consulting services to Russian client. Net amount RUB 500,000. NDS at 22%.
**Expected output:** Section 3 line 010: tax base = RUB 500,000. Output NDS = RUB 110,000. Section 9 entry with schyot-faktura details.

**Note:** Prior to 1 January 2026, the standard rate was 20% and output NDS would have been RUB 100,000. All test cases below use the 22% rate effective from 2026.

### Test 2 -- Purchase with input NDS deduction

**Input:** Russian company purchases office supplies from Russian supplier. Gross RUB 122,000 including NDS RUB 22,000, net RUB 100,000. Valid schyot-faktura received. Goods recorded in accounting.
**Expected output:** Section 3 line 120: input NDS = RUB 22,000. Section 8 entry with schyot-faktura details. Fully deductible.

### Test 3 -- Tax agent on foreign services

**Input:** Russian company pays USD 10,000 (equivalent RUB 900,000) to a UK consulting firm with no Russian registration. Services consumed in Russia.
**Expected output:** Tax agent NDS = RUB 900,000 * 22/122 = RUB 162,295 (rounded). Withhold and remit on payment date. Section 3 line 150: deductible NDS = RUB 162,295 (if entitled). Net effect zero for fully taxable business.

### Test 4 -- Export with confirmed 0% rate

**Input:** Russian company exports machinery to Turkey. Invoice value RUB 3,000,000. All documentary evidence submitted within 180 days.
**Expected output:** Section 4: tax base = RUB 3,000,000. NDS rate = 0%. Related input NDS deductions claimed in Section 4 line 030.

### Test 5 -- Sale of food products at 10%

**Input:** Russian company sells flour and bread products. Net amount RUB 200,000. NDS at 10%.
**Expected output:** Section 3 line 020: tax base = RUB 200,000. Output NDS = RUB 20,000.

### Test 6 -- Advance payment received

**Input:** Russian company receives advance of RUB 600,000 from customer for future delivery.
**Expected output:** Advance NDS = RUB 600,000 * 22/122 = RUB 108,197 (rounded). Section 3 line 070 = RUB 108,197. Advance schyot-faktura issued.

### Test 7 -- EAEU import from Kazakhstan

**Input:** Russian company imports raw materials from Kazakhstan. Value RUB 1,000,000. Goods accepted on March 15.
**Expected output:** Self-assessed NDS = RUB 1,000,000 * 22% = RUB 220,000. EAEU import declaration filed by April 20. NDS paid by April 20. Input NDS of RUB 220,000 claimed after payment and filing. [T2] -- confirm goods classification and rate.

### Test 8 -- USN payer issues invoice with NDS

**Input:** USN payer issues an invoice to customer showing NDS of RUB 50,000. Not registered as NDS payer.
**Expected output:** USN payer must remit RUB 50,000 to the budget. Section 12 entry. NO input NDS deduction available. Report in Section 1 line 030.

---

## 2026 Tax Reforms

| Change | Details | Effective |
|--------|---------|-----------|
| Standard NDS rate increase | 20% to 22% | 1 January 2026 |
| Reduced rate (10%) | Unchanged -- food, children's goods, medicines, educational publications | N/A |
| USN VAT exemption threshold | Reduced to RUB 20,000,000 (from RUB 60,000,000); further reductions: RUB 15M (2027), RUB 10M (2028) | 1 January 2026 |
| Banking VAT exemptions | Certain banking services (acquiring, processing, payment services) now subject to 22% NDS | 1 January 2026 |
| Software exemption | VAT exemption for rights to Russian software retained | Retained |
| SME transition support | Moratorium on penalties for SMEs newly subject to VAT under simplified regime | 2026 |

---

## Contribution Notes

This skill requires validation by a licensed Russian tax practitioner (nalogovyy konsul'tant or auditor). Given the rapidly evolving sanctions environment and frequent legislative changes, **this skill should be re-validated at least annually.**

Key areas requiring local expertise:
1. Current sanctions applicability and their NDS impact
2. Updated USN thresholds and special regime parameters
3. FNS administrative practices and audit triggers
4. EAEU protocol amendments
5. Digital services registry (Article 174.2) updates

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
