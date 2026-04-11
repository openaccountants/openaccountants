---
name: india-gst
description: Use this skill whenever asked to prepare, review, classify, or advise on India's Goods and Services Tax (GST). Trigger on phrases like "GST return", "GSTR-1", "GSTR-3B", "GSTR-9", "file GST", "GST classification", "HSN code", "SAC code", "input tax credit", "ITC", "reverse charge", "e-invoicing", "e-way bill", "composition scheme", "CGST", "SGST", "IGST", "UTGST", "inter-state supply", "intra-state supply", "place of supply", or any request involving Indian indirect tax compliance. This skill contains the complete GST classification rules, return form mappings, ITC eligibility and blocked credit rules, reverse charge treatment, e-invoicing requirements, e-way bill thresholds, composition scheme rules, and filing deadlines required to produce correct GST compliance output. ALWAYS read this skill before touching any India GST-related work.
---

# India GST Compliance Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | India |
| Jurisdiction Code | IN |
| Primary Legislation | Central Goods and Services Tax Act, 2017 (CGST Act) |
| Supporting Legislation | Integrated Goods and Services Tax Act, 2017 (IGST Act); State Goods and Services Tax Acts; CGST Rules, 2017; Place of Supply Rules (Chapter V, IGST Act) |
| Tax Authority | Central Board of Indirect Taxes and Customs (CBIC), Government of India |
| Filing Portal | https://gst.gov.in (GST Common Portal) |
| Contributor | Open Accounting Skills Project |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: rate classification (GST 2.0 slabs: 5%/18%/40%), GSTIN structure, return form selection, basic ITC rules, e-way bill thresholds, e-invoicing rules. Tier 2: place of supply for services, composite vs mixed supply, ITC apportionment, sector-specific exemptions, Health Security Cess on tobacco. Tier 3: anti-profiteering, advance rulings, cross-border digital services, customs valuation. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified Chartered Accountant or GST practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Legal name and GSTIN** [T1] -- 15-digit alphanumeric (format: 2 state code + 10 PAN + entity code + Z + checksum). Example: 27AAPFU0939F1Z5.
2. **Registration type** [T1] -- Regular, Composition, Input Service Distributor (ISD), Non-Resident Taxable Person (NRTP), Casual Taxable Person, TDS/TCS.
3. **State(s) of registration** [T1] -- each state requires separate GSTIN. List all GSTINs if multi-state.
4. **Primary business activity** [T2] -- manufacturer, trader, service provider, mixed. Impacts HSN/SAC classification and composition eligibility.
5. **Annual aggregate turnover (previous year and current year projected)** [T1] -- determines filing frequency (monthly vs quarterly under QRMP), e-invoicing applicability, composition eligibility.
6. **Does the business make inter-state supplies?** [T1] -- composition dealers CANNOT make inter-state supplies.
7. **Does the business make exempt supplies?** [T2] -- impacts ITC reversal under Rule 42/43.
8. **Does the business export?** [T1] -- zero-rated supply; determines if LUT/bond filing needed.
9. **Does the business receive supplies under reverse charge?** [T1] -- Sec 9(3)/9(4) applicability.
10. **E-invoicing applicability** [T1] -- turnover > INR 5 crore triggers mandatory e-invoicing.

**If GSTIN and registration type are unknown, STOP. Do not classify any transactions.**

---

## Step 1: GST Structure -- Dual GST Model

### 1a. Tax Components [T1]

**Legislation:** CGST Act, 2017, Sec 9; IGST Act, 2017, Sec 5; UTGST Act, 2017, Sec 7.

| Supply Type | Tax Components | Collected By |
|-------------|---------------|-------------|
| Intra-state (within same state) | CGST + SGST | Central + State |
| Intra-UT (within Union Territory) | CGST + UTGST | Central + UT |
| Inter-state (different states) | IGST | Central |
| Import of goods | IGST + Customs Duty | Central (Customs) |
| Import of services | IGST (reverse charge) | Recipient |

**Key rule [T1]:** IGST rate = CGST rate + SGST rate. For example, if CGST = 9% and SGST = 9%, then IGST = 18%.

### 1b. GST Rate Structure [T1]

**Legislation:** CGST Act, Sec 9; Notification No. 01/2017-CT(Rate) and amendments; Notification No. 11/2017-CT(Rate) for services. **As restructured by the 56th GST Council (3 Sep 2025), effective 22 Sep 2025 ("GST 2.0").**

**NOTE:** The 56th GST Council abolished the 12% and 28% slabs effective 22 September 2025, replacing them with a simplified two-tier structure (5% and 18%) plus a 40% demerit slab. Items formerly at 12% moved mostly to 5%; items formerly at 28% moved mostly to 18%; specified luxury/sin goods moved to 40%.

| GST Rate | CGST | SGST/UTGST | IGST | Typical Supplies |
|----------|------|------------|------|-----------------|
| 0% (Nil) | 0% | 0% | 0% | Essential foods (fresh milk, cereals, fresh vegetables, fresh fruits), healthcare, education |
| 0% (Zero-rated) | 0% | 0% | 0% | Exports, SEZ supplies (Sec 16 IGST Act) |
| 5% | 2.5% | 2.5% | 5% | Packaged food items, processed food, economy rail/air travel, transport of goods, small restaurants (without ITC), insurance, EVs, medicines |
| 18% | 9% | 9% | 18% | Most goods and services: IT services, telecom, financial services, restaurants in hotels >INR 7,500 tariff, branded garments, cement, automobiles (non-luxury), consumer durables (ACs, washing machines, refrigerators) |
| 40% | 20% | 20% | 40% | Luxury/sin/demerit goods only: aerated drinks, energy drinks, premium motor vehicles (SUVs >4m, >1500cc), online gaming/casinos/betting |

### 1c. Compensation Cess -- ABOLISHED [T1]

**Legislation:** Goods and Services Tax (Compensation to States) Act, 2017. **Abolished by 56th GST Council decisions.**

**IMPORTANT:** The compensation cess regime has been fully wound down:

- **22 Sep 2025:** Compensation cess abolished on all non-tobacco items (motor vehicles, coal, aerated waters, etc.) via CBIC Notification No. 02/2025. These items' effective tax burden was absorbed into the new 18% or 40% slabs.
- **1 Feb 2026:** Compensation cess abolished on tobacco and pan masala products. Replaced by the **Health Security and National Security Cess** under a separate statute, levied on production capacity (pan masala) and specific rates (tobacco/cigarettes).

**Legacy reference (pre-22 Sep 2025):**

| Item | Former Cess Rate | Current Status |
|------|-----------|----------------|
| Pan masala | 60% | Replaced by Health Security Cess (from 1 Feb 2026) |
| Tobacco / cigarettes | 12-36% + specific rate | Replaced by Health Security Cess (from 1 Feb 2026) |
| Aerated waters | 12% | Abolished 22 Sep 2025; item now in 40% slab |
| Motor vehicles (above 1200cc petrol / 1500cc diesel) | 15-22% | Abolished 22 Sep 2025; item now in 18% slab |
| Coal, lignite, peat | INR 400 per tonne | Abolished 22 Sep 2025 |
| Motor vehicles (SUVs >4m, >1500cc, ground clearance >170mm) | 22% | Abolished 22 Sep 2025; item now in 40% slab |

**Note [T1]:** Do NOT apply compensation cess to any invoice dated on or after 22 Sep 2025 (non-tobacco) or 1 Feb 2026 (tobacco/pan masala). For tobacco items between 22 Sep 2025 and 31 Jan 2026, the old compensation cess still applied.

### 1d. HSN / SAC Classification [T1]

**Legislation:** CGST Rules, Rule 46 (tax invoice); Notification No. 78/2020-CT.

| Annual Turnover | HSN Digits Required |
|-----------------|-------------------|
| Up to INR 5 crore | 4-digit HSN on B2B invoices |
| Above INR 5 crore | 6-digit HSN on all invoices |

- **HSN** (Harmonized System of Nomenclature): for goods. Based on World Customs Organization classification.
- **SAC** (Services Accounting Code): for services. Starts with 99xxxx.
- HSN/SAC must appear on every tax invoice. Incorrect HSN/SAC = incorrect return = potential demand notice.

---

## Step 2: Registration Rules

### 2a. Registration Thresholds [T1]

**Legislation:** CGST Act, Sec 22; Notification No. 10/2019-CT.

| Category | Threshold |
|----------|-----------|
| Goods supplier (general states) | INR 40 lakh (INR 4 million) aggregate turnover |
| Goods supplier (special category states*) | INR 20 lakh (INR 2 million) |
| Service provider (all states) | INR 20 lakh (INR 2 million) |
| Service provider (special category states*) | INR 10 lakh (INR 1 million) |

*Special category states: Manipur, Mizoram, Nagaland, Tripura, Meghalaya, Arunachal Pradesh, Sikkim, Uttarakhand, Himachal Pradesh (Puducherry and Telangana opted out).

**Compulsory registration regardless of turnover (Sec 24) [T1]:**
- Inter-state suppliers (with exceptions for handcraft/specified services)
- Casual taxable persons
- Non-resident taxable persons
- Persons making supplies under reverse charge
- E-commerce operators and suppliers through e-commerce
- TDS/TCS deductors
- Input Service Distributors
- Agents of suppliers

### 2b. GSTIN Format [T1]

15-character alphanumeric:

```
Position:  1-2    3-12        13   14  15
Content:   State  PAN Number  Entity  Z  Checksum
           Code                Code

Example:   27     AAPFU0939F   1    Z   5
           (MH)   (PAN)       (1st) (default) (check digit)
```

| State Code | State | State Code | State |
|-----------|-------|-----------|-------|
| 01 | Jammu & Kashmir | 20 | Jharkhand |
| 02 | Himachal Pradesh | 21 | Odisha |
| 03 | Punjab | 22 | Chhattisgarh |
| 04 | Chandigarh | 23 | Madhya Pradesh |
| 05 | Uttarakhand | 24 | Gujarat |
| 06 | Haryana | 25 | Daman & Diu* |
| 07 | Delhi | 26 | Dadra & Nagar Haveli* |
| 08 | Rajasthan | 27 | Maharashtra |
| 09 | Uttar Pradesh | 29 | Karnataka |
| 10 | Bihar | 30 | Goa |
| 11 | Sikkim | 32 | Kerala |
| 12 | Arunachal Pradesh | 33 | Tamil Nadu |
| 13 | Nagaland | 34 | Puducherry |
| 14 | Manipur | 35 | Andaman & Nicobar |
| 15 | Mizoram | 36 | Telangana |
| 16 | Tripura | 37 | Andhra Pradesh |
| 17 | Meghalaya | 38 | Ladakh |
| 18 | Assam | 97 | Other Territory |
| 19 | West Bengal | | |

*26 now covers merged Dadra & Nagar Haveli and Daman & Diu.

### 2c. Composition Scheme [T1]

**Legislation:** CGST Act, Sec 10; Notification No. 02/2019-CT(Rate).

| Parameter | Rule |
|-----------|------|
| Eligibility (goods) | Aggregate turnover <= INR 1.5 crore (INR 75 lakh in special category states) |
| Eligibility (services) | Aggregate turnover <= INR 50 lakh |
| Tax rate (manufacturer) | 1% (0.5% CGST + 0.5% SGST) |
| Tax rate (restaurant) | 5% (2.5% CGST + 2.5% SGST) |
| Tax rate (other suppliers) | 1% (0.5% CGST + 0.5% SGST) |
| Tax rate (service providers under Notification 02/2019) | 6% (3% CGST + 3% SGST) |
| ITC entitlement | NO -- cannot claim any input tax credit |
| Inter-state supply | NOT ALLOWED -- composition dealers cannot make inter-state supplies |
| E-commerce supply | NOT ALLOWED |
| Return form | GSTR-4 (annual) + CMP-08 (quarterly challan) |
| Invoice | Cannot collect tax on invoice; must mention "composition taxable person" |

---

## Step 3: GST Return Forms and Filing

### 3a. Return Form Matrix [T1]

**Legislation:** CGST Act, Sec 37-44; CGST Rules, Rule 59-80.

| Form | Description | Who Files | Frequency | Due Date |
|------|-------------|-----------|-----------|----------|
| GSTR-1 | Outward supplies (sales) | Regular taxpayers | Monthly (turnover > INR 5 crore) or Quarterly (QRMP) | 11th of following month (monthly) / 13th of month after quarter (quarterly) |
| GSTR-3B | Summary return + tax payment | Regular taxpayers | Monthly or Quarterly (QRMP) | 20th of following month (monthly) / 22nd-24th of month after quarter (quarterly, by state) |
| GSTR-2A | Auto-populated inward supplies | Auto-generated (read-only) | -- | -- |
| GSTR-2B | Auto-drafted ITC statement | Auto-generated (read-only) | Monthly | -- |
| GSTR-4 | Composition return | Composition taxpayers | Annual | 30th April following FY |
| CMP-08 | Composition challan | Composition taxpayers | Quarterly | 18th of month after quarter |
| GSTR-5 | Return for NRTPs | Non-resident taxable persons | Monthly | 20th of following month |
| GSTR-6 | ISD return | Input Service Distributors | Monthly | 13th of following month |
| GSTR-7 | TDS return | TDS deductors | Monthly | 10th of following month |
| GSTR-8 | TCS return | E-commerce operators | Monthly | 10th of following month |
| GSTR-9 | Annual return | Regular taxpayers (turnover > INR 2 crore) | Annual | 31st December following FY |
| GSTR-9C | Reconciliation statement | Taxpayers with turnover > INR 5 crore | Annual (self-certified) | 31st December following FY |
| GSTR-10 | Final return | Cancelled registrations | One-time | Within 3 months of cancellation |
| GSTR-11 | UIN return | Entities with UIN (embassies etc) | Monthly | 28th of month following quarter |
| ITC-04 | Job work return | Principals sending goods for job work | Annual / Half-yearly | Varies by turnover |

### 3b. QRMP Scheme (Quarterly Return Monthly Payment) [T1]

**Legislation:** CGST Rule 61A; Notification No. 84/2020-CT.

| Parameter | Rule |
|-----------|------|
| Eligibility | Aggregate turnover <= INR 5 crore in preceding FY |
| Returns | GSTR-1 quarterly; GSTR-3B quarterly |
| Tax payment | Monthly via PMT-06 (by 25th of following month) |
| Invoice Furnishing Facility (IFF) | Optional upload of B2B invoices in months 1 and 2 of quarter (max INR 50 lakh per month) |
| Tax computation methods | Fixed Sum Method (35% of previous quarter) or Self-Assessment Method |

### 3c. GSTR-3B Table Mapping [T1]

**Legislation:** CGST Rules, Rule 61; GSTR-3B format per Notification No. 34/2017-CT.

| Table | Description | What to Report |
|-------|-------------|---------------|
| 3.1(a) | Outward taxable supplies (other than zero-rated, nil-rated, exempted) | All taxable sales + tax collected |
| 3.1(b) | Outward taxable supplies (zero-rated) | Exports + SEZ supplies |
| 3.1(c) | Other outward supplies (nil-rated, exempted) | Nil-rated + exempt supplies |
| 3.1(d) | Inward supplies (liable to reverse charge) | RCM purchases |
| 3.1(e) | Non-GST outward supplies | Petroleum, alcohol, etc. |
| 3.2 | Inter-state supplies to unregistered persons, composition taxpayers, UIN holders | B2C inter-state + composition + UIN |
| 4(A) | ITC Available | Import, RCM, ISD, other ITC |
| 4(B) | ITC Reversed | Rule 42/43 reversals, others |
| 4(C) | Net ITC Available | 4(A) minus 4(B) |
| 4(D) | Ineligible ITC | As per Sec 17(5) |
| 5.1 | Interest and late fee payable | Auto-computed |
| 6.1 | Tax payment | IGST, CGST, SGST, Cess -- cash + ITC utilization |

### 3d. ITC Utilization Order [T1]

**Legislation:** CGST Act, Sec 49(5); Circular No. 98/17/2019-GST.

ITC must be utilized in this mandatory order:

```
IGST Credit --> First against IGST liability
            --> Then against CGST liability
            --> Then against SGST/UTGST liability

CGST Credit --> First against CGST liability
            --> Then against IGST liability
            --> CANNOT be used against SGST/UTGST

SGST Credit --> First against SGST liability
            --> Then against IGST liability
            --> CANNOT be used against CGST
```

**Rule [T1]:** IGST credit must be fully exhausted before CGST or SGST credit can be used against IGST liability.

---

## Step 4: Input Tax Credit (ITC) Rules

### 4a. Conditions for Claiming ITC [T1]

**Legislation:** CGST Act, Sec 16(2).

ALL four conditions must be met:

1. **Possession of tax invoice** or debit note or prescribed document.
2. **Receipt of goods or services.** For goods, can be received by agent on behalf of recipient.
3. **Tax has been actually paid** to the government by the supplier (reflected in GSTR-2B).
4. **Recipient has filed GSTR-3B** (return must be furnished).

**Time limit for claiming ITC [T1]:** Earlier of:
- 30th November of the year following the financial year to which the invoice pertains, OR
- Date of filing annual return (GSTR-9) for that financial year.

**Legislation:** CGST Act, Sec 16(4).

### 4b. ITC Matching and GSTR-2B [T1]

**Legislation:** CGST Act, Sec 16(2)(aa); Rule 36(4).

- ITC can only be claimed if invoice appears in GSTR-2B (auto-generated from supplier's GSTR-1).
- ITC cannot exceed the amount reflected in GSTR-2B.
- If supplier has not uploaded invoice, recipient CANNOT claim ITC even if goods/services received and payment made.

### 4c. Blocked Credits -- Section 17(5) [T1]

**Legislation:** CGST Act, Sec 17(5).

ITC is NOT available on the following, regardless of business use:

| Blocked Category | Section | Notes |
|-----------------|---------|-------|
| Motor vehicles and conveyances | 17(5)(a) | Exception: (i) further supply of vehicles, (ii) transportation of passengers, (iii) training of driving, (iv) transportation of goods |
| Food and beverages, outdoor catering, beauty treatment, health services, cosmetic/plastic surgery | 17(5)(b) | Exception: where such supply is an inward supply used for making outward taxable supply of the same category, or as an element of a taxable composite/mixed supply |
| Membership of club, health and fitness centre | 17(5)(c) | No exceptions |
| Rent-a-cab, life insurance, health insurance | 17(5)(d) | Exception: (i) government mandated provision to employees, (ii) used for making taxable supply of same category |
| Travel benefits to employees on vacation (LTC/LTA) | 17(5)(e) | No exceptions |
| Works contract for construction of immovable property (other than plant & machinery) | 17(5)(f) | Exception: where it is an input service for further supply of works contract |
| Construction of immovable property on own account (other than plant & machinery) | 17(5)(d) | Even if used for business, ITC blocked. Note: some practitioners cite this as 17(5)(c)/(d) -- verify against current statute |
| Goods/services for personal consumption | 17(5)(g) | No exceptions |
| Goods lost, stolen, destroyed, written off, disposed of by way of gift or free samples | 17(5)(h) | ITC must be reversed |
| Tax paid under composition scheme | Sec 10(4) | Composition taxpayers cannot claim any ITC |
| Tax paid under Sec 74 (fraud cases), Sec 129 (detention), Sec 130 (confiscation) | 17(5)(i) | No exceptions |

### 4d. ITC Reversal Rules [T1]

**Legislation:** CGST Rules, Rule 42 (inputs/input services) and Rule 43 (capital goods).

**Rule 42 -- Proportional reversal for inputs and input services:**
When inputs/input services are used partly for taxable and partly for exempt supplies:

```
ITC attributable to exempt supplies = (Exempt turnover / Total turnover) x Common Credit
```

This amount must be reversed. Reversal calculated monthly, annual reconciliation in GSTR-9.

**Rule 43 -- Capital goods reversal:**
Proportional ITC on capital goods used for both taxable and exempt supplies. 5-year useful life assumed. Monthly reversal = Total ITC / 60 months x (exempt turnover / total turnover).

**Sec 16(2) reversal for non-payment [T1]:**
If recipient does not pay supplier within 180 days of invoice date, ITC claimed must be reversed. ITC can be re-claimed upon payment.

### 4e. ITC on Imports [T1]

**Legislation:** CGST Act, Sec 16; Customs Tariff Act (for BCD); IGST Act, Sec 5(1).

- IGST paid on imports of goods (through Customs) is available as ITC.
- Basic Customs Duty (BCD) is NOT available as ITC.
- Social Welfare Surcharge on Customs is NOT available as ITC.
- IGST on import of services (under reverse charge) is available as ITC.

---

## Step 5: Reverse Charge Mechanism (RCM)

### 5a. Specified Goods/Services under RCM [T1]

**Legislation:** CGST Act, Sec 9(3); Notification No. 13/2017-CT(Rate).

| Supply | Supplier | Recipient (liable to pay GST) |
|--------|----------|------------------------------|
| Services by Goods Transport Agency (GTA) | GTA | Any factory, registered society, partnership firm, body corporate, registered person |
| Legal services by advocate | Advocate/firm of advocates | Any business entity |
| Services by arbitral tribunal | Arbitral tribunal | Any business entity |
| Sponsorship services | Any person | Body corporate or partnership firm |
| Services by government/local authority | Government | Any business entity |
| Director's services (not as employee) | Director | Company or body corporate |
| Insurance agent services | Insurance agent | Insurance company |
| Recovery agent services | Recovery agent | Banking company/NBFC |
| Services by author/music composer/artist | Author etc. | Publisher, music company, producer |
| Renting of motor vehicle (if supplier doesn't charge GST @12%) | Any person other than body corporate | Any body corporate |
| Security services | Any person other than body corporate | Registered person in same line of business |

### 5b. Import of Services -- Automatic RCM [T1]

**Legislation:** IGST Act, Sec 5(3).

Any import of services where the supplier is located outside India and the recipient is located in India -- GST must be paid by recipient under reverse charge. No threshold.

### 5c. RCM Mechanics [T1]

1. Recipient self-assesses GST at applicable rate.
2. Pays via cash ledger ONLY (ITC cannot be used to discharge RCM liability).
3. Reports in GSTR-3B Table 3.1(d).
4. ITC on RCM payment available in same period (if conditions of Sec 16 met).
5. Net effect: cash-neutral if recipient entitled to full ITC.

---

## Step 6: Place of Supply Rules

### 6a. Place of Supply for Goods [T1]

**Legislation:** IGST Act, Sec 10.

| Scenario | Place of Supply |
|----------|----------------|
| Goods involving movement | Location where movement terminates (delivery location) |
| Goods without movement | Location of goods at time of delivery |
| Goods via bill-to / ship-to | Principal place of business of third party receiving goods |
| Goods on approval / sale or return | Place where goods are when they are assented to |
| Import of goods | Location of the importer |
| Export of goods | Location outside India |

### 6b. Place of Supply for Services [T2]

**Legislation:** IGST Act, Sec 12 (B2B), Sec 13 (cross-border).

| Service Type | B2B (Sec 12) | B2C (Sec 12) | Cross-border (Sec 13) |
|-------------|-------------|-------------|----------------------|
| General rule | Location of recipient | Location of recipient (if address on record), else location of supplier | Location of recipient |
| Immovable property related | Location of property | Location of property | Location of property |
| Restaurant/catering/personal grooming/fitness | Where services performed | Where services performed | Where services performed |
| Training and performance appraisal | Location of recipient | Where services performed | Location of recipient |
| Transportation of goods | Location of recipient | Location where goods handed over | Location of recipient |
| Passenger transportation | Place of embarkation | Place of embarkation | Place of embarkation |
| Events and exhibitions (admission) | Place of event | Place of event | Place of event |
| OIDAR (Online Information Database Access/Retrieval) | Location of recipient | Location of recipient | Location of recipient |
| Banking/financial services | Location of recipient | Location of recipient | Location of recipient |
| Insurance | Location of recipient | Location of recipient on record | Location of recipient |
| Telecom services | Location of recipient | Billing address / SIM location | Location of recipient |
| Advertising to government/non-taxable online recipient | Where addressed to | Where addressed to | -- |

**Flag [T2]:** Place of supply for services is frequently disputed. If supply involves multiple states or cross-border elements, flag for practitioner review.

---

## Step 7: Zero-Rated Supplies and Exports

### 7a. Definition [T1]

**Legislation:** IGST Act, Sec 16.

Zero-rated supplies means any of:
- **Export of goods or services**, or
- **Supply to a Special Economic Zone (SEZ) developer or SEZ unit**

### 7b. Two Options for Exporters [T1]

**Legislation:** IGST Act, Sec 16(3); CGST Rules, Rule 96/96A.

| Option | Mechanism | Refund |
|--------|-----------|--------|
| Export with payment of IGST | Charge IGST on invoice, claim refund of IGST paid | Automatic refund via shipping bill (Rule 96) |
| Export under LUT/Bond (without payment of tax) | File Letter of Undertaking (LUT) on portal, supply at 0% | Claim refund of accumulated ITC (Rule 89) |

**LUT eligibility [T1]:** Any registered person who has not been prosecuted for tax evasion exceeding INR 250 lakh. Filed annually on GST portal (Form GST RFD-11).

### 7c. SEZ Supplies [T1]

**Legislation:** IGST Act, Sec 16(1)(b); SEZ Act, 2005.

- Treated as zero-rated supplies.
- Same two options as exports (with IGST or under LUT).
- Endorsed by SEZ authority (requires proper documentation).
- Supplier must obtain endorsement from SEZ officer on invoices.

---

## Step 8: E-Invoicing

### 8a. Applicability Thresholds [T1]

**Legislation:** CGST Rule 48(4); Notification No. 13/2020-CT and amendments.

| Effective Date | Turnover Threshold |
|---------------|-------------------|
| 01 Oct 2020 | > INR 500 crore |
| 01 Jan 2021 | > INR 100 crore |
| 01 Apr 2021 | > INR 50 crore |
| 01 Apr 2022 | > INR 20 crore |
| 01 Oct 2022 | > INR 10 crore |
| 01 Aug 2023 | > INR 5 crore |

**Turnover is aggregate turnover in any preceding financial year from 2017-18 onwards.**

### 8a-ii. 30-Day Reporting Rule [T1]

**Legislation:** GSTN Advisory dated 5 Nov 2024; effective 1 Apr 2025.

From 1 April 2025, taxpayers with AATO >= INR 10 crore must report e-invoices to the IRP within **30 days** of the invoice date. If an e-invoice (invoice, credit note, or debit note) is reported beyond the 30-day window, the IRP will reject the IRN generation request.

| Effective Date | Applicability |
|---------------|---------------|
| 1 Nov 2023 | AATO >= INR 100 crore (original rule) |
| 1 Apr 2025 | AATO >= INR 10 crore (threshold lowered) |

### 8a-iii. Multi-Factor Authentication [T1]

From 1 April 2025, multi-factor authentication (MFA) is mandatory for all taxpayers accessing the GST portal, including for e-invoice and e-way bill generation.

### 8b. E-Invoice Mechanics [T1]

1. Generate invoice in accounting/ERP system.
2. Upload JSON to Invoice Registration Portal (IRP) at `einvoice1.gst.gov.in`.
3. IRP validates, generates **IRN** (Invoice Reference Number -- 64-character hash).
4. IRP returns signed JSON with IRN + QR code.
5. IRN + QR code must appear on printed/emailed invoice.
6. E-invoice data auto-populates GSTR-1 and e-way bill (Part A).

### 8c. Exemptions from E-Invoicing [T1]

- Banks, insurance companies, NBFCs
- SEZ units (for supplies to DTA only)
- Government departments
- Local authorities
- Persons registered under Sec 14 of IGST Act (OIDAR suppliers)

---

## Step 9: E-Way Bill

### 9a. When Required [T1]

**Legislation:** CGST Rules, Rule 138.

| Condition | E-Way Bill Required |
|-----------|-------------------|
| Movement of goods, consignment value > INR 50,000 | YES |
| Movement of goods, consignment value <= INR 50,000 | NO (unless intra-state movement in states with lower threshold) |
| Handicraft goods, inter-state by exempt person | YES, even if < INR 50,000 |
| Job work -- inter-state movement | YES, even if < INR 50,000 |

### 9b. E-Way Bill Details [T1]

| Field | Rule |
|-------|------|
| Validity (within state, up to 200 km) | 1 day |
| Validity (every additional 200 km) | +1 day |
| Validity (over-dimensional cargo, up to 20 km) | 1 day, +1 day per 20 km |
| Generation | By consignor (supplier) or consignee (recipient) or transporter |
| Portal | https://ewaybillgst.gov.in |
| Cancellation | Within 24 hours (if goods not in transit) |
| Extension | Before expiry, with reasons |

### 9c. Exempt from E-Way Bill [T1]

- Goods transported by non-motorized conveyance
- Goods transported from port/airport/land customs to customs warehouse
- Transit cargo to/from Nepal or Bhutan
- Kerosene oil sold under PDS
- Postal baggage
- Natural or cultured pearls, precious stones, currency
- Used personal and household effects
- Coral, unworked

---

## Step 10: Composite and Mixed Supplies

### 10a. Definitions [T1]

**Legislation:** CGST Act, Sec 2(30) (composite supply), Sec 2(74) (mixed supply).

| Type | Definition | Tax Treatment |
|------|-----------|---------------|
| Composite supply | Two or more supplies naturally bundled, supplied in conjunction, where one is principal supply | Taxed at rate of the PRINCIPAL supply |
| Mixed supply | Two or more supplies which are NOT naturally bundled but supplied together for a single price | Taxed at rate of the supply attracting HIGHEST rate |

### 10b. Examples [T2]

| Scenario | Classification | Rate Applied |
|----------|---------------|-------------|
| Hotel room + breakfast (included in tariff) | Composite -- room is principal | Rate of accommodation |
| Gift hamper: chocolates (18%) + dry fruits (5%) + crockery (18%) | Mixed supply | 18% (highest rate) |
| Works contract (goods + services for immovable property) | Composite supply of services | 18% (Sec 2(119)) |
| Annual maintenance contract (spare parts + service) | Composite -- service is principal | 18% |
| Bundled telecom + handset offer at one price | Mixed supply (not naturally bundled) | 18% (handset rate, if higher) |

**Flag [T2]:** Composite vs mixed determination is fact-specific and frequently litigated. Flag for practitioner if classification is ambiguous.

---

## Step 11: Key Thresholds Summary

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Registration (goods, general) | INR 40 lakh | Sec 22 |
| Registration (goods, special states) | INR 20 lakh | Sec 22 |
| Registration (services, general) | INR 20 lakh | Sec 22 |
| Registration (services, special states) | INR 10 lakh | Sec 22 |
| Composition (goods) | INR 1.5 crore | Sec 10 |
| Composition (services) | INR 50 lakh | Notification 02/2019-CT(Rate) |
| E-invoicing | INR 5 crore aggregate turnover (any FY from 2017-18) | Rule 48(4) |
| E-way bill | INR 50,000 consignment value | Rule 138 |
| QRMP eligibility | INR 5 crore | Rule 61A |
| GSTR-9 annual return mandatory | INR 2 crore | Sec 44 |
| GSTR-9C reconciliation mandatory | INR 5 crore | Sec 44 |
| Non-payment ITC reversal | 180 days | Sec 16(2) |
| Time limit for ITC claim | 30 Nov of following FY or date of GSTR-9, whichever earlier | Sec 16(4) |

---

## Step 12: Penalties and Interest

### 12a. Late Filing [T1]

**Legislation:** CGST Act, Sec 47.

| Return | Late Fee |
|--------|----------|
| GSTR-3B (with tax liability) | INR 50/day (INR 25 CGST + INR 25 SGST), max INR 10,000 per return |
| GSTR-3B (nil return) | INR 20/day (INR 10 CGST + INR 10 SGST), max INR 500 per return |
| GSTR-1 | INR 50/day (INR 25 CGST + INR 25 SGST), max INR 10,000 |
| GSTR-9 | INR 200/day (INR 100 CGST + INR 100 SGST), max 0.5% of turnover |
| GSTR-4 (composition) | INR 50/day (INR 25 CGST + INR 25 SGST), max INR 10,000 |

### 12b. Interest on Late Payment [T1]

**Legislation:** CGST Act, Sec 50.

| Situation | Interest Rate |
|-----------|-------------|
| Late payment of tax (on net cash liability) | 18% per annum |
| Undue/excess ITC claimed and utilized | 24% per annum |

### 12c. Penalties for Non-Compliance [T1]

**Legislation:** CGST Act, Sec 122-138.

| Offence | Penalty |
|---------|---------|
| Failure to register | Higher of INR 10,000 or tax evaded |
| Incorrect invoice / without invoice | Higher of INR 10,000 or tax evaded |
| Fraud / suppression / misstatement | 100% of tax due (Sec 74) |
| Non-fraud short payment | 10% of tax due or INR 10,000, whichever higher (Sec 73) |
| E-way bill violation | INR 10,000 or tax evaded, whichever greater + detention of goods/vehicle |

---

## PROHIBITIONS [T1]

- NEVER allow ITC on blocked credits under Sec 17(5) -- these are absolute blocks regardless of business use.
- NEVER allow composition dealers to claim ITC, make inter-state supplies, or supply through e-commerce.
- NEVER apply intra-state rates (CGST+SGST) to inter-state supplies, or vice versa.
- NEVER let AI guess HSN/SAC codes -- classification must be verified against the HSN/SAC master.
- NEVER allow ITC claims that do not appear in GSTR-2B.
- NEVER discharge RCM liability using ITC -- must be paid via electronic cash ledger only.
- NEVER allow ITC to be claimed beyond the time limit (30 Nov of following FY).
- NEVER classify a mixed supply as composite to achieve a lower rate.
- NEVER ignore the ITC utilization order (IGST must be exhausted first).
- NEVER allow e-invoicing-applicable businesses to issue invoices without IRN/QR code.
- NEVER assume export status without LUT filing or IGST payment proof.
- NEVER ignore state-specific e-way bill thresholds (some states have lower thresholds than INR 50,000).
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Step 13: Edge Case Registry

### EC1 -- Inter-state vs intra-state determination for bill-to/ship-to [T2]

**Situation:** Supplier in Maharashtra bills a buyer in Delhi, but goods are shipped directly to a factory in Gujarat.
**Resolution:** Place of supply = Gujarat (location where movement terminates, per Sec 10(1)(b) IGST Act). Since supplier is in Maharashtra and place of supply is Gujarat, this is inter-state (IGST). But the bill-to party is in Delhi. The IGST invoice is issued to the Delhi entity. The Delhi entity can claim ITC if registered in Gujarat via its Gujarat GSTIN. Flag for practitioner to confirm three-party documentation.
**Legislation:** IGST Act, Sec 10(1)(b); Circular No. 35/09/2018-GST.

### EC2 -- Place of supply for OIDAR services to non-registered person [T2]

**Situation:** Foreign company (e.g., Netflix, AWS) supplies OIDAR services to an Indian consumer (B2C, unregistered).
**Resolution:** Place of supply = location of recipient (India). If supplier is foreign, supplier must register under Simplified Registration Scheme (Sec 14 IGST Act) and collect/remit IGST at 18%. If B2B and recipient is registered, reverse charge applies instead.
**Legislation:** IGST Act, Sec 13(12), Sec 14.

### EC3 -- ITC reversal on non-payment within 180 days [T1]

**Situation:** Recipient claimed ITC on purchase in April 2025, has not paid supplier by September 2025 (180 days elapsed).
**Resolution:** ITC claimed on that invoice must be added to output tax liability in the return for the period in which 180 days expire. Interest at 18% applies from date of ITC claim to date of reversal. ITC may be re-claimed in the period when payment is eventually made.
**Legislation:** CGST Act, Sec 16(2), proviso; CGST Rules, Rule 37.

### EC4 -- Reverse charge on services from directors [T1]

**Situation:** Company pays sitting fees / consultancy fees to a non-employee director.
**Resolution:** RCM applies. Company must self-assess GST at 18% on director fees (if director provides services in individual capacity, not as employee). Report in GSTR-3B Table 3.1(d). ITC claimable if otherwise eligible. If director is a full-time employee on company's payroll, GST does not apply (employer-employee relationship, Schedule III).
**Legislation:** Notification 13/2017-CT(Rate), Sl. No. 6; Circular No. 140/10/2020-GST.

### EC5 -- SEZ supply vs DTA supply from same entity [T2]

**Situation:** Supplier makes supplies to both SEZ units and Domestic Tariff Area (DTA) customers from same GSTIN.
**Resolution:** SEZ supplies are zero-rated under Sec 16 IGST Act. DTA supplies are taxable at applicable rate. Supplier must maintain separate accounts/invoices. ITC on inputs used for SEZ supplies is fully recoverable. No reversal required under Rule 42 for zero-rated supplies (they are not exempt supplies). However, if supplier opts to supply without payment of tax (LUT), ITC accumulates and refund must be claimed under Rule 89.
**Legislation:** IGST Act, Sec 16; CGST Rules, Rule 89.

### EC6 -- Export with payment of IGST -- refund stuck [T2]

**Situation:** Exporter charged IGST on export invoices, shipping bill filed, but refund not processed within 60 days.
**Resolution:** Common reasons: mismatch between GSTR-1 and shipping bill data (invoice number, port code, shipping bill number), IGST amount mismatch, incomplete bank realization certificate. Exporter should check ICEGATE for status, reconcile GSTR-1 with shipping bill, and file manual refund claim (RFD-01) if automatic route fails. Interest at 6% due to exporter after 60 days of shipping (Sec 56).
**Legislation:** IGST Act, Sec 16(3); CGST Act, Sec 54, 56.

### EC7 -- Job work: goods sent but not returned within prescribed time [T1]

**Situation:** Principal sends goods to job worker. Job worker has not returned goods within 1 year (inputs) or 3 years (capital goods).
**Resolution:** The supply of goods to job worker is deemed a supply on the day the time limit expires. Principal must pay GST on the value of goods sent. ITC already claimed must be reversed. If goods are subsequently returned, no mechanism exists to reverse the deemed supply.
**Legislation:** CGST Act, Sec 143(1); Proviso to Sec 143(1).

### EC8 -- Composite supply vs mixed supply -- restaurant + takeaway [T2]

**Situation:** Restaurant supplies food for dine-in (restaurant service, 5% without ITC) and also sells packaged/branded takeaway items (goods at 12% or 18%).
**Resolution:** Dine-in is restaurant service at 5% (if opted, without ITC). Packaged/branded items sold separately are goods and taxed at their HSN rate. If billed together as a single supply, determine if naturally bundled (composite) or not (mixed). Typically, a clearly distinct packaged product (e.g., bottled sauce with brand label) is a separate supply, not naturally bundled with restaurant service. Flag for practitioner.
**Legislation:** CGST Act, Sec 2(30), 2(74); Circular No. 164/20/2021-GST.

### EC9 -- ITC on motor vehicles -- exceptions [T1]

**Situation:** Transport company purchases trucks for goods transportation.
**Resolution:** ITC on trucks used for transportation of goods is NOT blocked. Sec 17(5)(a) blocks motor vehicles and conveyances EXCEPT when used for: (i) further supply of such vehicles, (ii) transportation of passengers, (iii) imparting training on driving, (iv) transportation of goods. Trucks for goods transport fall under exception (iv). Full ITC available.
**Legislation:** CGST Act, Sec 17(5)(a)(ii), exception (iv).

### EC10 -- GST on advance payments for services [T1]

**Situation:** Client receives advance payment for services to be provided next quarter.
**Resolution:** Time of supply for services = earlier of: (a) date of invoice (if within 30 days of service), or (b) date of receipt of payment. If advance is received, GST is payable at the time of receipt. However, for registered persons with turnover up to INR 1.5 crore, the requirement to pay GST on advances for services was removed (Notification 66/2017-CT). For goods, GST on advances was removed for all registered persons (Notification 66/2017-CT as amended).
**Legislation:** CGST Act, Sec 13(2); Notification 66/2017-CT.

### EC11 -- Credit notes and GST impact [T1]

**Situation:** Supplier issues credit note for deficient services 4 months after original invoice.
**Resolution:** Supplier declares credit note in GSTR-1 of the period in which credit note is issued. Reduces output tax liability. Recipient must reverse ITC to the extent of the credit note (auto-reflected in GSTR-2B). Time limit: credit note must be issued before 30 November of following FY or date of GSTR-9, whichever earlier.
**Legislation:** CGST Act, Sec 34; CGST Rules, Rule 53.

### EC12 -- Works contract for plant and machinery vs immovable property [T2]

**Situation:** Company hires contractor for construction of a factory building with attached plant and machinery.
**Resolution:** Works contract for construction of immovable property (other than plant and machinery) -- ITC BLOCKED under Sec 17(5)(c). Works contract for plant and machinery -- ITC AVAILABLE. "Plant and machinery" means apparatus, equipment, and machinery fixed to earth by foundation or structural support, BUT excludes land, building, or civil structures. Demarcation between building and plant is contentious. Flag for practitioner to review based on facts.
**Legislation:** CGST Act, Sec 17(5)(c), Explanation to Sec 17(5).

### EC13 -- Supplies to government -- TDS under GST [T1]

**Situation:** Supplier provides services to a government department, contract value > INR 2.5 lakh.
**Resolution:** Government department / establishment / local authority / PSUs must deduct TDS at 2% (1% CGST + 1% SGST for intra-state, or 2% IGST for inter-state) on payments exceeding INR 2.5 lakh. TDS deducted is reflected in recipient's (supplier's) electronic cash ledger and can be used for tax payment. Deductor files GSTR-7 monthly.
**Legislation:** CGST Act, Sec 51; Notification No. 33/2017-CT.

### EC14 -- Deemed exports (supply within India but treated as export for refund) [T2]

**Situation:** Supplier supplies goods to an EOU (Export Oriented Unit) or against Advance Authorization.
**Resolution:** Deemed exports under Sec 147 of CGST Act. Goods are supplied within India but treated as exports for refund purposes. Refund of tax paid or ITC accumulated is available to either supplier or recipient (as per prior agreement). Notification 48/2017-CT specifies categories: supply against Advance Authorization, supply to EOU, supply to EPCG holder.
**Legislation:** CGST Act, Sec 147; Notification 48/2017-CT; Rule 89(4).

---

## Step 14: Comparison with EU VAT

| Feature | India GST | EU VAT |
|---------|----------|--------|
| Structure | Dual (CGST+SGST or IGST) | Single VAT per member state |
| Rates | 0%, 5%, 18%, 40% (since 22 Sep 2025; formerly also 12% and 28% + cess) | Standard (varies 17-27%), reduced rates vary by country |
| Registration threshold | INR 20-40 lakh (approx EUR 2,200-4,400) | Varies by country (e.g., EUR 35,000 in Malta) |
| Return frequency | Monthly/Quarterly | Monthly/Quarterly (varies by country) |
| Reverse charge (domestic) | Yes, for specified services | Limited (mainly for construction in some countries) |
| Reverse charge (imports) | Yes, for services; goods via Customs | Yes, for intra-EU acquisitions and imported services |
| E-invoicing | Mandatory above INR 5 crore | Varies -- mandatory in Italy, being rolled out across EU (ViDA) |
| E-way bill | Mandatory for goods > INR 50,000 | No EU-wide equivalent (transport documents vary) |
| Input matching | ITC locked to supplier's GSTR-1 upload (GSTR-2B) | No real-time matching in most EU states (except Hungary/Italy) |
| Blocked credits | Extensive list (Sec 17(5)) | Varies by country (typically entertainment, cars) |
| Composition/flat rate | Yes, for small taxpayers | Flat-rate scheme for farmers in some countries |
| Compensation cess | Abolished (22 Sep 2025 for non-tobacco; 1 Feb 2026 for tobacco). Replaced by Health Security Cess on tobacco/pan masala | No equivalent (excise duties separate) |
| Digital service taxation | OIDAR provisions under IGST | OSS/IOSS for B2C digital services |
| Place of supply rules | Chapter V, IGST Act (detailed) | EU VAT Directive Art. 44-59 |
| Invoice requirements | HSN/SAC mandatory, IRN for e-invoicing | Sequential numbering, VAT ID, varied rules |
| Refund mechanism | Automatic (shipping bill) + manual (RFD-01) | Varies by country (8th/13th Directive for non-residents) |

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
Action Required: Qualified GST practitioner or Chartered Accountant must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified GST practitioner. Document gap.
```

---

## Step 16: Out of Scope [T3]

The following are NOT covered by this skill. Escalate to practitioner:

- **Customs duty** -- BCD, safeguard duty, anti-dumping duty, social welfare surcharge.
- **Income tax / TDS** -- withholding tax on payments is separate from GST.
- **Anti-profiteering complaints** -- National Anti-Profiteering Authority proceedings.
- **GST litigation and appeals** -- Appellate Tribunal (GSTAT) proceedings.
- **Transitional credit** -- TRAN-1/TRAN-2 issues (legacy Cenvat/VAT credit migration).
- **Valuation disputes** -- Sec 15 valuation rules for related party transactions, pure agent, subsidies.
- **Cross-charge and ISD** -- intra-entity cross-charges for common services across GSTINs.
- **GST audit** -- Sec 65/66 special audit or departmental audit proceedings.
- **E-commerce operator obligations** -- TCS, compliance requirements for marketplace models.

---

## Step 17: Test Suite

### Test 1 -- Standard intra-state sale at 18%
**Input:** Supplier in Maharashtra sells IT services to buyer in Maharashtra. Invoice value INR 1,00,000 + GST.
**Expected output:** CGST 9% = INR 9,000. SGST 9% = INR 9,000. Total invoice = INR 1,18,000. Report in GSTR-1 as B2B supply. Buyer claims ITC of INR 18,000 (INR 9,000 CGST + INR 9,000 SGST) if reflected in GSTR-2B.

### Test 2 -- Inter-state sale at 18%
**Input:** Supplier in Tamil Nadu sells goods to buyer in Karnataka. Invoice value INR 5,00,000 + GST.
**Expected output:** IGST 18% = INR 90,000. Total invoice = INR 5,90,000. Report in GSTR-1 as B2B supply. Buyer claims ITC of INR 90,000 IGST.

### Test 3 -- Import of services, reverse charge
**Input:** Indian company receives consulting services from a US firm. Value USD 10,000 (INR 8,30,000). No GST on foreign invoice.
**Expected output:** Recipient pays IGST 18% = INR 1,49,400 under RCM via cash ledger. Reports in GSTR-3B Table 3.1(d). Claims ITC of INR 1,49,400 in Table 4(A)(3) if conditions met. Net effect = zero (cash-neutral).

### Test 4 -- Blocked credit: motor vehicle (personal car)
**Input:** Company purchases car for director's personal use. Invoice INR 15,00,000 + GST 18% = INR 2,70,000 (post-22 Sep 2025; no compensation cess).
**Expected output:** ITC BLOCKED under Sec 17(5)(a). Zero ITC available. Total cost to company = INR 17,70,000 including non-recoverable GST. (Note: luxury/premium vehicles above 1500cc or SUVs may attract 40% GST instead.)

### Test 5 -- Composition dealer quarterly challan
**Input:** Composition dealer (trader) with turnover INR 80 lakh in quarter. Tax rate 1%.
**Expected output:** CMP-08 liability: 0.5% CGST = INR 40,000 + 0.5% SGST = INR 40,000 = INR 80,000. No ITC claim. No inter-state supply allowed.

### Test 6 -- Export under LUT
**Input:** Exporter in Gujarat ships goods to UAE buyer. FOB value INR 25,00,000. LUT filed for current FY.
**Expected output:** Invoice at 0% (zero-rated). No IGST charged. Report in GSTR-1 as export. Claim refund of accumulated ITC via RFD-01. Shipping bill and Bill of Lading required as proof.

### Test 7 -- E-invoicing required
**Input:** Company with aggregate turnover INR 12 crore (previous FY) issues B2B invoice.
**Expected output:** E-invoice MANDATORY. Invoice must be uploaded to IRP, IRN obtained, QR code printed on invoice. Non-compliance = invoice deemed invalid, ITC blocked for recipient.

### Test 8 -- E-way bill for goods movement
**Input:** Supplier in Delhi transports goods worth INR 75,000 to buyer in Haryana (distance 80 km).
**Expected output:** E-way bill REQUIRED (value > INR 50,000). Validity = 1 day (distance < 200 km). Inter-state movement, IGST applies.

### Test 9 -- ITC reversal for exempt supplies (Rule 42)
**Input:** Business makes taxable supplies of INR 70 lakh and exempt supplies of INR 30 lakh. Common ITC for the month = INR 1,80,000.
**Expected output:** ITC attributable to exempt supplies = (30/100) x 1,80,000 = INR 54,000. This must be reversed (added to output liability). Net ITC claimable = INR 1,26,000. Annual reconciliation required in GSTR-9.

### Test 10 -- Credit note reducing output liability
**Input:** Supplier issues credit note for INR 50,000 + IGST INR 9,000 (original inter-state supply at 18%). Credit note issued within time limit.
**Expected output:** Supplier: reduces GSTR-1 output by INR 50,000, reduces IGST output by INR 9,000. Recipient: must reverse ITC of INR 9,000 in the period credit note appears in GSTR-2B.

### Test 11 -- GTA services under RCM
**Input:** Manufacturing company receives goods transport service from a GTA. Freight INR 50,000. GTA has not opted to pay GST under forward charge.
**Expected output:** RCM applies. Recipient pays GST 5% (CGST 2.5% + SGST 2.5% if intra-state) = INR 2,500 via cash ledger. ITC of INR 2,500 claimable if used for taxable outward supplies. Alternative: 12% rate if GTA opts for ITC.

### Test 12 -- Mixed supply classification
**Input:** Retailer sells a Diwali gift hamper containing sweets (5%), dry fruits (5%), a silver coin (3%), and a decorative box (18%) for a single price of INR 5,000.
**Expected output:** Mixed supply. Not naturally bundled. Tax at highest rate = 18%. IGST/CGST+SGST at 18% on INR 5,000 = INR 900. HSN of the item attracting highest rate to be used. (Note: silver coin retains the special 3% rate for precious metals.)

---

## Contribution Notes

If you are adapting this skill for another jurisdiction:

1. Replace all legislation references with equivalent national legislation.
2. Replace return forms with your jurisdiction's equivalent forms.
3. Replace GST rates with your jurisdiction's rates.
4. Replace registration thresholds with local equivalents.
5. Replace blocked credit categories with your jurisdiction's non-deductible categories.
6. Replace GSTIN format with your jurisdiction's taxpayer identification format.
7. Have a qualified practitioner in your jurisdiction validate every T1 rule before publishing.
8. Add jurisdiction-specific edge cases.
9. Run all test suite cases against your jurisdiction's rules.
10. Update the EU VAT comparison table for your jurisdiction.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
