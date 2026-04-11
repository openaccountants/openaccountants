---
name: illinois-sales-tax
description: Use this skill whenever asked about Illinois sales and use tax, Retailers' Occupation Tax (ROT), Illinois use tax, Service Occupation Tax, IDOR filings, Illinois exemptions, Illinois nexus, or any request involving Illinois state sales and use tax compliance. Trigger on phrases like "Illinois sales tax", "IL sales tax", "ROT", "Retailers Occupation Tax", "IDOR", "ST-1", "Illinois exemption certificate", or any request involving Illinois sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Illinois sales tax work.
---

# Illinois Sales and Use Tax Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Illinois, United States |
| Jurisdiction Code | US-IL |
| Tax Type | Retailers' Occupation Tax (ROT), Use Tax, Service Occupation Tax (SOT), Service Use Tax |
| Primary Legislation | 35 ILCS 120 (Retailers' Occupation Tax Act); 35 ILCS 105 (Use Tax Act); 35 ILCS 115 (Service Use Tax Act); 35 ILCS 110 (Service Occupation Tax Act) |
| Key Statutes | 35 ILCS 120/1 et seq.; 35 ILCS 105/1 et seq. |
| Tax Authority | Illinois Department of Revenue (IDOR) |
| Filing Portal | https://mytax.illinois.gov |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires Illinois CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate structure, ROT/Use Tax mechanics, basic taxability, filing mechanics, nexus thresholds. Tier 2: service tax classification, multi-tax interaction, home rule taxes. Tier 3: audit defense, complex multi-tax situations, IDOR private letter rulings. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before performing any Illinois sales tax work, collect the following from the client:

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What is your Illinois Certificate of Registration number? | Required for filing; confirms registration with IDOR. [T1] |
| 2 | What is your assigned filing frequency (monthly, quarterly, annual)? | Determines return due dates. [T1] |
| 3 | What type of nexus do you have in Illinois (physical, economic, both)? | Economic nexus: $100,000 revenue OR 200 transactions (OR test). [T1] |
| 4 | Do you sell through any marketplace facilitators (Amazon, eBay, Etsy, etc.)? | Marketplace facilitators collect tax on facilitated sales; seller must track separately. [T1] |
| 5 | Do you provide services that involve transferring tangible personal property? | Service Occupation Tax (SOT) applies to TPP transferred incident to service. [T1] |
| 6 | Are you located in a home rule municipality? | Home rule municipalities can impose significant additional taxes. [T2] |
| 7 | Do you sell food, drugs, or medical appliances? | These are taxed at a reduced 1% state rate (NOT exempt). [T1] |
| 8 | Do you sell software or SaaS products? | Downloaded software is taxable; purely cloud-based SaaS is NOT taxable. [T1] |

---

## Step 1: Tax Rate Structure [T1]

### 1.1 Illinois Four-Tax System [T1]

| Tax | Statute | Imposed On | Collected From |
|-----|---------|-----------|----------------|
| Retailers' Occupation Tax (ROT) | 35 ILCS 120 | Retailers on gross receipts from sales of TPP | Retailers pass to customers [T1] |
| Use Tax | 35 ILCS 105 | Purchasers on use of TPP purchased from out-of-state | Purchasers (or collected by retailer) [T1] |
| Service Occupation Tax (SOT) | 35 ILCS 110 | Service providers who transfer TPP incident to service | Service providers pass to customers [T1] |
| Service Use Tax | 35 ILCS 115 | Purchasers of services involving TPP transfer | Purchasers [T1] |

### 1.2 State Rates [T1]

| Rate Category | State Rate | Items |
|--------------|-----------|-------|
| General merchandise | **6.25%** | Most tangible personal property [T1] |
| Qualifying food and drugs | **1.00%** | Grocery food, drugs, medical appliances [T1] |

**Critical:** Illinois taxes grocery food and drugs at a reduced 1% state rate rather than exempting them entirely. This is unusual among states. [T1]

**Legislation:** 35 ILCS 120/2-10.

### 1.3 Local Taxes [T1/T2]

| Tax Component | Rate Range | Notes |
|--------------|-----------|-------|
| State ROT | 6.25% (or 1%) | Base rate [T1] |
| County RTA (Regional Transportation Authority) | 0.75% -- 1.25% | Chicago metro area [T1] |
| County/city general | 0.25% -- 1.75% | Varies [T1] |
| Home rule municipal | 0% -- 3.75%+ | Home rule municipalities can impose additional [T2] |
| Special districts | Varies | Water reclamation, park, etc. [T1] |

**Combined maximum rates can exceed 10%** in parts of Chicago and Cook County. [T1]

### 1.4 Key Combined Rates [T1]

| Jurisdiction | General Merch Rate | Qualifying Food Rate |
|-------------|-------------------|---------------------|
| Chicago (Cook County) | ~10.25% | ~2.00% (1% state + local food taxes) |
| Springfield | ~9.00% | Varies |
| Suburban Cook County | ~9.00-10.25% | Varies |
| Downstate counties | ~6.25-8.75% | Varies |

### 1.5 Sourcing Rules [T1/T2]

| Scenario | Rate Applied |
|----------|-------------|
| Intrastate sales | Generally origin-based (seller's location rate) [T1] |
| Remote (out-of-state) sellers | Destination-based (buyer's location rate) [T1] |
| Home rule taxes | May have different sourcing rules [T2] |

**Legislation:** 35 ILCS 120/2-12.

---

## Step 2: Transaction Classification Rules [T1/T2]

### 2.1 Tangible Personal Property (TPP) [T1]

All sales of TPP at retail are taxable (ROT on gross receipts, passed to customer). 35 ILCS 120/2. Includes: electronics, appliances, furniture, equipment, vehicles, clothing and footwear (**NO clothing exemption** -- fully taxable at 6.25%), building materials, jewelry, sporting goods, office supplies. [T1]

### 2.2 Food, Drugs, and Medical Appliances -- Reduced Rate [T1]

| Category | State Rate | Citation |
|----------|-----------|----------|
| Qualifying food (grocery food for human consumption, off-premises) | **1%** | 35 ILCS 120/2-10 [T1] |
| Prescription and nonprescription drugs | **1%** | 35 ILCS 120/2-10 [T1] |
| Medical appliances (prescribed) | **1%** | 35 ILCS 120/2-10 [T1] |

**Food that does NOT qualify for the reduced rate (taxed at 6.25%):**

| Item | Rate | Tier |
|------|------|------|
| Prepared food (heated, served with utensils) | 6.25% | [T1] |
| Candy (no flour, contains sugar/sweetener as primary ingredient) | 6.25% | [T1] |
| Soft drinks | 6.25% | [T1] |
| Alcoholic beverages | 6.25% | [T1] |
| Food from restaurants (unless to-go and not heated) | 6.25% | [T2] |

**Legislation:** 35 ILCS 120/2-10; 86 Ill. Admin. Code 130.310.

### 2.3 Services [T1]

Illinois does NOT generally tax services. The Service Occupation Tax (SOT) applies only when a service provider transfers TPP as part of a service transaction (the TPP component is taxed, not the service itself). 35 ILCS 110. [T1]

| Situation | SOT Applies? | Notes |
|----------|-------------|-------|
| Auto mechanic installs new parts | Yes (on parts) | Parts are TPP transferred incident to service [T1] |
| Attorney provides legal advice | No | No TPP transferred [T1] |
| Web designer delivers a website | No (generally) | Intangible -- no TPP [T1] |
| Contractor installs flooring | Yes (on materials) | Materials are TPP [T1] |
| Hair salon sells shampoo | Yes (on shampoo) | TPP sold at retail [T1] |

### 2.4 SOT Calculation Methods [T1]

| Method | Calculation | When to Use |
|--------|------------|-------------|
| Cost price method | Tax on the cost of materials/parts transferred | When materials are a significant component [T1] |
| Service provider election | Tax on 50% of entire bill | Optional if service and materials are inseparable [T1] |
| Separately stated | Tax on the materials/parts amount only | When charges are broken out on the invoice [T1] |

**Legislation:** 35 ILCS 110/3; 86 Ill. Admin. Code 140.101.

### 2.5 SaaS and Digital Goods [T1/T2]

| Product | Taxable? | Notes |
|---------|----------|-------|
| Canned software (physical media) | **TAXABLE** | TPP at 6.25% [T1] |
| Canned software (electronic download) | **TAXABLE** | 86 Ill. Admin. Code 130.1935 [T1] |
| Custom software (any delivery) | **EXEMPT** | Not TPP; treated as a service [T1] |
| SaaS (cloud-hosted, no download) | **NOT TAXABLE** | IDOR General Information Letter ST 15-0015 [T1] |
| Digital music, movies, books (download) | **TAXABLE** | Treated as TPP if delivered with permanent right [T1] |
| Streaming (no download/no possession) | **NOT TAXABLE** | No transfer of TPP [T1] |

**Important:** Illinois distinguishes between software that is downloaded (taxable as TPP) and software that is accessed remotely without download (SaaS -- not taxable). [T1]

**Legislation:** 86 Ill. Admin. Code 130.1935; IDOR General Information Letters.

### 2.6 Clothing [T1]

Clothing is **fully taxable** at the standard 6.25% state rate (plus local). No clothing exemption in Illinois. [T1]

---

## Step 3: Return Form Structure [T1]

### 3.1 Filing Forms

| Form | Name | Use |
|------|------|-----|
| ST-1 | Sales and Use Tax and E911 Surcharge Return | Primary return (covers all four taxes) [T1] |
| ST-2 | Multiple Site Form | Businesses with multiple locations [T1] |
| ST-1-X | Amended return | Corrections [T1] |
| RUT-25 | Use Tax Return | Individual purchasers [T1] |

### 3.2 ST-1 Line Mapping [T1]

| Line | Content |
|------|---------|
| Line 1 | Gross receipts from sales of general merchandise (6.25% items) [T1] |
| Line 2 | Gross receipts from sales of qualifying food, drugs, and medical appliances (1% items) [T1] |
| Line 5 | Service providers -- cost price of TPP transferred [T1] |
| Use tax section | For purchasers reporting use tax [T1] |

### 3.3 Use Tax Reporting [T1]

| Filer Type | Reporting Method |
|-----------|-----------------|
| Registered retailers | Report on Form ST-1 [T1] |
| Individuals | Form IL-1040 (Schedule ST) [T1] |
| Businesses not registered | Form RUT-25 (Use Tax Return) [T1] |

### 3.4 Use Tax Rules [T1]

| Rule | Detail |
|------|--------|
| When use tax applies | TPP from out-of-state retailer without IL tax; TPP purchased tax-free diverted to taxable use; TPP brought into IL for use/storage/consumption [T1] |
| Rates | General merchandise: 6.25%; Qualifying food/drugs/medical: 1% (plus local) [T1] |
| Credit for tax paid to other states | Credit allowed under 35 ILCS 105/3-55 [T1] |

---

## Step 4: Deductibility / Exemptions [T1/T2]

### 4.1 Common Exemptions

| Exemption | Statute | Notes | Tier |
|-----------|---------|-------|------|
| Food for human consumption (REDUCED RATE 1%) | 35 ILCS 120/2-10 | NOT exempt, but reduced rate | [T1] |
| Drugs (Rx and OTC) (REDUCED RATE 1%) | 35 ILCS 120/2-10 | NOT exempt, but reduced rate | [T1] |
| Medical appliances (REDUCED RATE 1%) | 35 ILCS 120/2-10 | NOT exempt, but reduced rate | [T1] |
| Farm equipment and chemicals | 35 ILCS 120/2-5(2) | Used in agriculture | [T1] |
| Manufacturing machinery/equipment | 35 ILCS 120/2-5(14) | Used primarily in manufacturing | [T1] |
| Resale | 35 ILCS 120/2-5(39) | Goods purchased for resale | [T1] |
| Interstate commerce | 35 ILCS 120/2-5(1) | Goods shipped out of state | [T1] |
| Federal/state government | 35 ILCS 120/2-5(11)(12) | Government purchases | [T1] |
| Gasoline (separate motor fuel tax) | 35 ILCS 120/2-5(5) | Subject to motor fuel tax instead | [T1] |
| Newspapers/magazines | 35 ILCS 120/2-5(6) | Qualifying publications | [T1] |
| Pollution control equipment | 35 ILCS 120/2-5(16) | Environmental compliance | [T1] |
| Rolling stock (railroad, airline) | 35 ILCS 120/2-5(19) | Interstate transportation | [T1] |

### 4.2 Manufacturing Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Scope | Machinery and equipment used primarily (over 50%) in manufacturing/assembling TPP for wholesale or retail sale/lease [T1] |
| Includes | Production machinery, tools, dies, replacement parts [T1] |
| Excludes | Office equipment, vehicles, administrative equipment [T1] |
| Authority | 35 ILCS 120/2-5(14) |

### 4.3 Resale Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Form | CRT-61 (Certificate of Resale) or blanket Certificate of Resale [T1] |
| Multi-state accepted | MTC Uniform Sales Tax Certificate accepted [T1] |
| SST Certificate | NOT accepted -- IL is not an SST member [T1] |

### 4.4 Nonprofit Exemptions [T2]

| Parameter | Detail |
|-----------|--------|
| Certificate | Illinois Exemption Identification Number (E-number) from IDOR [T2] |
| Application | Form STAX-1 (Application for Sales Tax Exemption) [T2] |
| Scope | Covers purchases by the organization [T2] |
| Not automatic | Specific types of charitable, educational, and religious organizations [T2] |

### 4.5 Exemption Certificates [T1]

| Certificate | Form | Purpose |
|------------|------|---------|
| Resale | CRT-61 | Purchases for resale [T1] |
| Various exemptions | ST-587 | Manufacturing, agriculture, and other exemptions (check appropriate box) [T1] |
| Government | CRT-63 | Government entity purchases [T1] |

---

## Step 5: Key Thresholds [T1]

### 5.1 Economic Nexus Threshold [T1]

| Parameter | Value |
|-----------|-------|
| Revenue threshold | $100,000 in cumulative gross receipts from sales of TPP to IL purchasers [T1] |
| Transaction threshold | 200 or more separate transactions for sale of TPP to IL purchasers [T1] |
| Test type | **OR test** -- either threshold triggers nexus [T1] |
| Measurement period | Preceding 12-month period [T1] |
| Effective date | October 1, 2018 [T1] |
| Marketplace exclusion | Marketplace-facilitated sales excluded from seller's threshold [T1] |
| Authority | 35 ILCS 105/2 |

### 5.2 Registration Requirements [T1]

| Requirement | Detail |
|------------|--------|
| Who must register | Any retailer making sales of TPP at retail in IL (35 ILCS 120/2a) [T1] |
| Out-of-state retailers | Register as retailer maintaining a place of business or as remote retailer [T1] |
| Portal | MyTax Illinois (https://mytax.illinois.gov) [T1] |
| Form | REG-1 (Illinois Business Registration Application) [T1] |

### 5.3 Marketplace Facilitator Rules [T1]

| Rule | Detail |
|------|--------|
| Effective date | January 1, 2020 [T1] |
| Facilitator treated as | Retailers for ROT/Use Tax purposes [T1] |
| Seller relief | Sellers relieved of collection obligation for facilitated sales [T1] |
| Facilitator liability | Liable for uncollected tax on marketplace sales [T1] |
| Authority | 35 ILCS 120/2(a-10); 35 ILCS 105/2(a-10) |

---

## Step 6: Filing Deadlines and Penalties [T1]

### 6.1 Filing Frequency

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Monthly | Annual tax liability > $20,000 | 20th of the following month [T1] |
| Quarterly | Annual tax liability $500-$20,000 | Last day of the month following the quarter [T1] |
| Annual | Annual tax liability < $500 | January 31 [T1] |

### 6.2 Quarterly Due Dates [T1]

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | January 1 -- March 31 | April 30 |
| Q2 | April 1 -- June 30 | July 31 |
| Q3 | July 1 -- September 30 | October 31 |
| Q4 | October 1 -- December 31 | January 31 |

**Legislation:** 35 ILCS 120/3.

### 6.3 Electronic Filing [T1]

| Rule | Detail |
|------|--------|
| Mandatory e-filing | Taxpayers with annual ROT/Use Tax liability of $20,000+ [T1] |
| Platform | MyTax Illinois [T1] |

### 6.4 Vendor Discount [T1]

| Parameter | Value |
|-----------|-------|
| Rate | 1.75% of tax due [T1] |
| Maximum | $1,000 per return [T1] |
| Note | Verify current rate -- temporarily reduced and capped [T2] |
| Authority | 35 ILCS 120/3 |

### 6.5 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing | 2% per month (max 25%) | 35 ILCS 735/3-3 [T1] |
| Late payment | 2% per month (max 25%) | 35 ILCS 735/3-3 [T1] |
| Negligence | 20% of deficiency | 35 ILCS 735/3-5 [T1] |
| Fraud | 50% of deficiency | 35 ILCS 735/3-6 [T1] |
| Interest | Federal short-term rate + 2% | 35 ILCS 735/3-2 [T1] |

### 6.6 Record Retention [T1]

| Parameter | Value |
|-----------|-------|
| Retention period | Minimum 4 years from the date of the return or the date it was due, whichever is later [T1] |
| Authority | 35 ILCS 735/3-7 |

### 6.7 Statute of Limitations [T1]

| Scenario | Limitation Period |
|----------|------------------|
| Standard assessment | 3.5 years from filing [T1] |
| No return filed | No limitation [T1] |
| Fraud | No limitation [T1] |

### 6.8 Audit Considerations [T2]

| Factor | Detail |
|--------|--------|
| Audit types | Desk and field audits [T1] |
| Common issues | Improper use of 1% food/drug rate, failure to collect SOT on parts, missing exemption certificates [T2] |
| Frequent audit point | Candy/food distinction (flour vs. no flour) [T1] |

---

## Step 7: Illinois-Specific Rules [T1/T2]

### 7.1 Four-Tax System Interaction [T1]

**Scenario A: Standard retail sale of a product**
- The RETAILER owes ROT (35 ILCS 120) on gross receipts. [T1]
- The retailer passes this cost to the buyer. [T1]
- If the buyer is from out of state and the retailer does not collect, the BUYER owes Use Tax (35 ILCS 105). [T1]

**Scenario B: Service provider transfers TPP as part of a service**
- The SERVICE PROVIDER owes SOT (35 ILCS 110) on the cost price of TPP transferred. [T1]
- If the buyer purchases a service from an out-of-state provider involving TPP, the BUYER owes Service Use Tax (35 ILCS 115). [T1]

### 7.2 Home Rule Taxes [T2]

Illinois home rule municipalities have broad authority to impose additional taxes beyond the standard state and local rates. These may include: home rule ROT, home rule service occupation tax, home rule use tax, and special taxes on specific items (e.g., restaurant meals, amusement, liquor). Each home rule municipality has its own ordinances. Flag for reviewer -- must research the specific municipality's tax ordinances. [T2]

**Legislation:** Illinois Constitution Art. VII, Sec. 6; 65 ILCS 5/8-11-1.

### 7.3 Chicago Amusement Tax on Streaming ("Netflix Tax") [T1]

The City of Chicago imposes a 9% amusement tax on streaming services (commonly called the "Netflix tax"). This is a separate municipal tax, not the state ROT. Cook County may impose its own amusement tax. These local taxes are separate from state sales tax and have their own filing requirements. [T1] for awareness; [T3] for filing mechanics.

### 7.4 Candy vs. Food Classification [T1]

Under Illinois law, "candy" is defined as a preparation of sugar, honey, or other sweetener combined with chocolate, fruits, nuts, or other ingredients in the form of bars, drops, or pieces, that does NOT contain flour. Items containing flour as an ingredient are classified as FOOD (1% rate), not candy (6.25% rate). [T1]

**Example:** Granola bars with flour = 1% rate. Pure chocolate bar without flour = 6.25% rate. [T1]

**Legislation:** 35 ILCS 120/2-10; 86 Ill. Admin. Code 130.310.

### 7.5 Detailed Taxability Matrix [T1]

| Category | State Rate | Local Additional? | Key Statute |
|----------|-----------|-------------------|-------------|
| General TPP | 6.25% | Yes (varies) | 35 ILCS 120/2-10 |
| Grocery food (qualifying) | 1% | Yes (reduced local) | 35 ILCS 120/2-10 |
| Drugs (Rx and OTC) | 1% | Yes (reduced local) | 35 ILCS 120/2-10 |
| Medical appliances | 1% | Yes (reduced local) | 35 ILCS 120/2-10 |
| Prepared food (hot, utensils) | 6.25% | Yes (full local) | 35 ILCS 120/2-10 |
| Candy (no flour, sugar primary) | 6.25% | Yes (full local) | 35 ILCS 120/2-10 |
| Soft drinks | 6.25% | Yes (full local) | 35 ILCS 120/2-10 |
| Clothing (all items) | 6.25% | Yes | No exemption |
| Canned software (download) | 6.25% | Yes | 86 Ill. Admin. Code 130.1935 |
| Custom software | Exempt | N/A | Service, not TPP |
| SaaS (cloud, no download) | Not taxable | N/A | IDOR Gen. Info. Letter ST 15-0015 |
| Manufacturing equipment | Exempt | N/A | 35 ILCS 120/2-5(14) |
| Farm equipment | Exempt | N/A | 35 ILCS 120/2-5(2) |
| Resale purchases | Exempt | N/A | 35 ILCS 120/2-5(39) |
| Interstate shipments | Exempt | N/A | 35 ILCS 120/2-5(1) |
| SOT (parts in service) | 6.25% or 1% | Yes | 35 ILCS 110/3 |
| Gasoline/fuel | Separate tax | Motor fuel tax | 35 ILCS 120/2-5(5) |
| Newspapers/magazines | Exempt | N/A | 35 ILCS 120/2-5(6) |
| Pollution control equipment | Exempt | N/A | 35 ILCS 120/2-5(16) |

---

## PROHIBITIONS [T1]

- **NEVER** say Illinois exempts grocery food -- it taxes food at a REDUCED 1% rate, not exempt. [T1]
- **NEVER** forget that Illinois has FOUR separate taxes (ROT, Use Tax, SOT, Service Use Tax) that function together. [T1]
- **NEVER** apply a clothing exemption in Illinois -- clothing is fully taxable at 6.25%. [T1]
- **NEVER** assume all services are taxable -- SOT applies only to the TPP component of service transactions. [T1]
- **NEVER** treat SaaS as taxable if the product is purely cloud-based with no download component. [T1]
- **NEVER** confuse the candy definition -- items containing flour are FOOD (1%), not candy (6.25%). [T1]
- **NEVER** ignore home rule taxes -- home rule municipalities can impose significant additional taxes. [T2]
- **NEVER** use destination-based sourcing for intrastate Illinois sales -- Illinois is origin-based for intrastate. [T1]
- **NEVER** accept the SST Certificate in Illinois -- IL is not an SST member. [T1]
- **NEVER** overlook the Chicago amusement tax on streaming services -- it is separate from state sales tax. [T1]

---

## Edge Case Registry [T1/T2]

### EC1 -- Grocery Food at Reduced Rate vs. Prepared Food at Full Rate [T1]

**Situation:** A grocery store has a deli counter that sells both prepared foods (hot sandwiches) and cold grocery items.

**Resolution:** Cold grocery items are taxed at the 1% reduced rate. Hot prepared food and food sold with utensils is taxed at the full 6.25% rate (plus local). Each item must be classified separately. If the transaction mixes items at different rates, the register must apply the correct rate to each item. 35 ILCS 120/2-10.

### EC2 -- Service Occupation Tax -- Auto Repair [T1]

**Situation:** An auto mechanic charges $500 for repair labor and $300 for parts to fix a car.

**Resolution:** The Service Occupation Tax applies to the parts ($300) at 6.25% (plus local). The labor ($500) is NOT taxable. If the charges are separately stated, only the parts are taxed. If not separately stated, the entire $800 may be subject to SOT. 35 ILCS 110/3.

### EC3 -- Home Rule Taxes [T2]

**Situation:** A business operates in a home rule municipality that imposes additional local sales taxes.

**Resolution:** Illinois home rule municipalities have broad authority to impose additional taxes beyond the standard state and local rates. These may include: home rule ROT, home rule service occupation tax, home rule use tax, and special taxes on specific items. Each home rule municipality has its own ordinances. Flag for reviewer -- must research the specific municipality's tax ordinances.

**Legislation:** Illinois Constitution Art. VII, Sec. 6; 65 ILCS 5/8-11-1.

### EC4 -- Cook County "Netflix Tax" [T1]

**Situation:** A Chicago resident subscribes to Netflix and other streaming services.

**Resolution:** The City of Chicago imposes a 9% amusement tax on streaming services. This is a separate municipal tax, not the state ROT. Additionally, Cook County may impose its own amusement tax. These local taxes are separate from state sales tax and have their own filing requirements. [T1] for awareness; [T3] for filing mechanics.

### EC5 -- Candy vs. Food Classification [T1]

**Situation:** A store sells chocolate bars, granola bars with chocolate chips, and sugar-free mints.

**Resolution:** Under Illinois law, "candy" does NOT contain flour. Items containing flour are classified as FOOD (1% rate), not candy (6.25% rate). Granola bars with flour = 1% rate. Pure chocolate bar without flour = 6.25% rate. 35 ILCS 120/2-10; 86 Ill. Admin. Code 130.310.

### EC6 -- Vehicle Use Tax [T1]

**Situation:** Individual purchases a used vehicle from a private party.

**Resolution:** Illinois imposes a Vehicle Use Tax at the time of title transfer. The rate is generally 6.25% of the purchase price (or fair market value, whichever is higher), paid to the Secretary of State. This is a separate mechanism from the standard ROT. County and municipal taxes may also apply.

### EC7 -- SaaS vs. Downloaded Software Distinction [T1]

**Situation:** A business uses software that is partly cloud-based and partly downloaded to the local computer.

**Resolution:** If the software involves a download or installation on the user's computer, it is taxable as TPP at 6.25%. If purely accessed through a web browser with no download, it is NOT taxable. For hybrid products, taxability depends on whether the primary function requires a download. Flag for reviewer if the product has both components. [T2]

### EC8 -- Qualified Solid Waste Energy Facilities [T2]

**Situation:** A waste-to-energy facility purchases equipment.

**Resolution:** Equipment used in qualified solid waste energy facilities may qualify for exemption under 35 ILCS 120/2-5(16). Requires analysis of whether the facility and equipment meet statutory requirements. Flag for reviewer.

### EC9 -- Marketplace Seller with Direct Sales [T1]

**Situation:** A seller makes sales through Amazon (marketplace) and through their own website to Illinois customers.

**Resolution:** Amazon collects and remits tax on marketplace sales. The seller must independently collect and remit tax on direct website sales. The seller must track both channels separately and report accordingly on Form ST-1.

### EC10 -- Enterprise Zone Incentives [T2]

**Situation:** A business operating in a designated Illinois Enterprise Zone purchases building materials for a qualified project.

**Resolution:** Businesses in designated Enterprise Zones may qualify for a sales tax exemption on building materials used in qualified construction projects. Requires certification from the local zone administrator and the applicable exemption certificate. Flag for reviewer -- specific requirements vary by zone.

**Legislation:** 20 ILCS 655 (Illinois Enterprise Zone Act); 35 ILCS 120/5k.

---

## Test Suite

### Test 1 -- General Merchandise Sale in Chicago [T1]

**Input:** Retailer in Chicago sells a $500 laptop. Combined rate: 10.25%.
**Expected output:** Tax = $51.25. Total = $551.25.

### Test 2 -- Grocery Food at Reduced Rate [T1]

**Input:** Customer buys $100 of grocery food (bread, milk, eggs) in Chicago. Qualifying food combined rate: ~2.00% (1% state + local food taxes).
**Expected output:** Tax = $2.00 (approximate -- exact local rate varies). Food taxed at reduced rate, NOT exempt.

### Test 3 -- Prepared Food at Full Rate [T1]

**Input:** Customer buys a $15 hot sandwich from a deli in Springfield. Combined rate: ~9.00%.
**Expected output:** Tax = $1.35. Prepared food taxed at full general merchandise rate.

### Test 4 -- SaaS Not Taxable [T1]

**Input:** Illinois business subscribes to a cloud-based CRM (SaaS). $200/month. No download, browser-only access.
**Expected output:** Not taxable. SaaS without download is not TPP in Illinois. No ROT/Use Tax applies.

### Test 5 -- Economic Nexus -- Revenue [T1]

**Input:** Out-of-state seller has $110,000 in IL sales and 50 transactions in the past 12 months.
**Expected output:** Seller HAS economic nexus. Revenue ($110,000) exceeds $100,000 threshold. Transaction count is irrelevant (OR test).

### Test 6 -- Economic Nexus -- Transactions [T1]

**Input:** Out-of-state seller has $50,000 in IL sales but 250 transactions in the past 12 months.
**Expected output:** Seller HAS economic nexus. Transaction count (250) exceeds 200 threshold. Revenue is irrelevant (OR test).

### Test 7 -- Auto Repair SOT [T1]

**Input:** Auto mechanic charges $400 labor + $200 parts. Parts taxed at 8.25% combined local rate. Charges separately stated.
**Expected output:** Tax on parts = $16.50 ($200 x 8.25%). Tax on labor = $0. Total tax = $16.50.

### Test 8 -- Candy vs. Food [T1]

**Input:** Customer buys: (a) chocolate bar (no flour) for $3, (b) granola bar (contains flour) for $3. Both in Chicago.
**Expected output:** Chocolate bar taxed at ~10.25% (general merchandise rate) = $0.31. Granola bar taxed at ~2.00% (food rate) = $0.06. Different rates because granola bar contains flour and qualifies as food, not candy.

### Test 9 -- Vendor Discount [T1]

**Input:** Retailer files ST-1 on time with $5,000 in ROT due.
**Expected output:** Vendor discount = 1.75% of $5,000 = $87.50 (within $1,000 cap). Net remittance = $4,912.50.

### Test 10 -- Use Tax on Out-of-State Purchase [T1]

**Input:** Illinois business purchases $2,000 of office supplies from an Oregon retailer. No tax collected. Business located in Springfield (combined rate ~9.00%).
**Expected output:** Use tax = $180.00 ($2,000 x 9.00%). Report on ST-1 or IL-1040.

---

## Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed CPA, EA, or tax attorney must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax professional. Document gap.
```

---

## Contribution Notes

| Resource | URL / Contact |
|----------|---------------|
| IDOR Main | https://www2.illinois.gov/rev |
| MyTax Illinois (Online Filing) | https://mytax.illinois.gov |
| Rate Lookup | https://tax.illinois.gov/questionsandanswers/tax-rate-finder.html |
| Phone | 1-800-732-8866 |
| Registration | Online via MyTax Illinois |
| Tax Publications | https://tax.illinois.gov/publications.html |
| Regulations (86 Ill. Admin. Code) | https://www.ilga.gov/commission/jcar/admincode/086/08600130sections.html |
| General Information Letters | https://tax.illinois.gov/research/legalinformation.html |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
