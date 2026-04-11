---
name: thailand-vat
description: Use this skill whenever asked to prepare, review, or advise on Thailand VAT (Value Added Tax) for any client. Trigger on phrases like "Thai VAT", "Thailand VAT return", "PP.30", "PP.36", "Revenue Code VAT", "Thai output tax", "Thai input tax", or any request involving Thailand VAT filing, classification, or compliance. This skill contains the complete Thailand VAT classification rules, form PP.30 box structure, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Thailand VAT-related work.
---

# Thailand VAT Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Thailand |
| Jurisdiction Code | TH |
| Primary Legislation | Revenue Code, Title IV, Chapter V (Sections 77 -- 90/5) |
| Supporting Legislation | Royal Decree No. 800 (2023, extending 7% rate through 30 Sep 2025); Royal Decree No. 799 B.E. 2568 (2025, extending 7% rate through 30 Sep 2026); Ministerial Regulation No. 189; Revenue Department Notifications |
| Tax Authority | Revenue Department (กรมสรรพากร), Ministry of Finance |
| Filing Portal | https://efiling.rd.go.th (e-Filing) |
| Currency | Thai Baht (THB) |
| Contributor | [Pending -- must be validated by Thai CPA] |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, PP.30 box assignment, blocked input categories, registration threshold. Tier 2: partial input allocation, mixed-use assets, related-party pricing. Tier 3: BOI-promoted enterprise VAT, customs valuation disputes, cross-border digital services. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed Thai tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and Tax Identification Number (TIN)** [T1] -- 13-digit TIN
2. **VAT registration status** [T1] -- VAT registered operator, or non-registered (below threshold or exempt activity)
3. **VAT period** [T1] -- monthly (standard for all VAT registrants)
4. **Industry/sector** [T2] -- impacts whether activity is VAT-liable or exempt under Section 81
5. **Does the business make exempt supplies?** [T2] -- If yes, partial input allocation required (Section 82/3); practitioner must confirm allocation method
6. **Does the business import goods?** [T1] -- impacts customs VAT treatment
7. **Does the business have BOI promotion?** [T3] -- Board of Investment promoted enterprises may have special VAT privileges; escalate
8. **Does the business provide digital services to customers in Thailand from abroad?** [T2] -- e-Service provisions under Section 77/2 amendments
9. **Does the business have branch registrations?** [T1] -- each branch must file separately unless consolidated filing approved
10. **Excess credit carried forward from prior period** [T1] -- from prior PP.30 filing

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Sale of goods or provision of services (output VAT) or Purchase of goods or receipt of services (input VAT)
- Salaries, wages, social security contributions, personal income tax withholding, dividend distributions, loan principal repayments = OUT OF SCOPE (never on VAT return)
- **Legislation:** Revenue Code, Section 77/1 (definition of sale), Section 77/1(10) (definition of service)

### 1b. Determine Counterparty Location [T1]

- Domestic (Thailand): supplier/customer is located in Thailand
- Foreign: supplier/customer is located outside Thailand
- **Note:** For services received from abroad by a VAT-registered person, reverse charge applies under Section 83/6(2)
- For goods imported into Thailand, VAT is collected by Customs at the border under Section 83/8

### 1c. Determine VAT Rate [T1]

**Standard rate: 7%** (temporarily reduced from the statutory 10% rate under Revenue Code Section 80)
- The 7% rate has been extended repeatedly via Royal Decrees. Currently extended through 30 September 2026 (Royal Decree No. 799 B.E. 2568, approved by Cabinet on 9 September 2025). Further extensions are expected but not guaranteed.
- **Legislation:** Revenue Code, Section 80 (statutory 10%); Royal Decree No. 799 B.E. 2568 (2025) (7% extension through 30 Sep 2026)

| Rate | Application |
|------|-------------|
| 7% | Standard rate -- all taxable supplies of goods and services within Thailand |
| 0% | Exports of goods (Section 80/1(1)); services rendered in Thailand and used entirely abroad (Section 80/1(2)); services provided to enterprises in free zones; international transport (Section 80/1(3)-(4)) |
| Exempt | Supplies listed under Section 81 (see classification matrix below) |

### 1d. Determine Expense/Revenue Category [T1]

- Capital goods: significant assets used in the business (no single statutory threshold like Malta, but depreciation rules in Section 65 bis apply)
- Goods for resale: goods purchased for direct resale
- Raw materials / production inputs: goods consumed in manufacturing
- Services / overheads: everything else
- **Legislation:** Revenue Code, Section 82/5 (input tax on capital goods)

---

## Step 2: VAT Return Form PP.30 Structure [T1]

**Legislation:** Revenue Code, Section 83; Revenue Department Form PP.30 (ภ.พ.30)

The PP.30 is a monthly VAT return. The form structure is as follows:

### Section 1: Output Tax (ภาษีขาย)

| Line | Description | Classification |
|------|-------------|----------------|
| 1.1 | Revenue from sales of goods and services at 7% | Taxable domestic sales |
| 1.2 | Revenue from zero-rated sales (exports, services used abroad) | Zero-rated sales |
| 1.3 | Total revenue (1.1 + 1.2) | Subtotal |
| 1.4 | Output tax (7% of Line 1.1) | Output VAT |

### Section 2: Input Tax (ภาษีซื้อ)

| Line | Description | Classification |
|------|-------------|----------------|
| 2.1 | Purchases of goods and services at 7% (with valid tax invoices) | Taxable domestic purchases |
| 2.2 | Imports (VAT paid at Customs) | Import VAT |
| 2.3 | Total purchases (2.1 + 2.2) | Subtotal |
| 2.4 | Input tax (total of VAT on Lines 2.1 + 2.2) | Input VAT |
| 2.5 | Input tax that cannot be credited (blocked under Section 82/5) | Blocked input |
| 2.6 | Net creditable input tax (2.4 - 2.5) | Net input VAT |

### Section 3: Tax Calculation

| Line | Description | Classification |
|------|-------------|----------------|
| 3.1 | Tax payable (if output tax > net input tax: 1.4 - 2.6) | Tax due |
| 3.2 | Excess credit (if net input tax > output tax: 2.6 - 1.4) | Refund/carry forward |
| 3.3 | Excess credit brought forward from prior period | B/F credit |
| 3.4 | Net tax payable (3.1 - 3.3, if positive) | Payment due |
| 3.5 | Net excess credit to carry forward (3.2 + 3.3, or 3.3 - 3.1 if 3.3 > 3.1) | C/F credit |

### Derived Calculations [T1]

```
Line 1.3 = Line 1.1 + Line 1.2
Line 1.4 = Line 1.1 * 7%
Line 2.3 = Line 2.1 + Line 2.2
Line 2.4 = sum of VAT amounts from Lines 2.1 + 2.2
Line 2.6 = Line 2.4 - Line 2.5

IF Line 1.4 > Line 2.6 THEN
  Line 3.1 = Line 1.4 - Line 2.6
  Line 3.2 = 0
ELSE
  Line 3.1 = 0
  Line 3.2 = Line 2.6 - Line 1.4
END

IF Line 3.1 > 0 THEN
  Line 3.4 = Line 3.1 - Line 3.3 (if positive, else 0)
  Line 3.5 = Line 3.3 - Line 3.1 (if positive, else 0)
ELSE
  Line 3.4 = 0
  Line 3.5 = Line 3.2 + Line 3.3
END
```

---

## Step 3: Supply Classification Matrix [T1]

### Zero-Rated Supplies (0%) -- Section 80/1

| Category | Legislation | Notes |
|----------|-------------|-------|
| Export of goods | Section 80/1(1) | Must have customs export declaration (กศ.101) |
| Services rendered in Thailand, used entirely abroad | Section 80/1(2) | Service must be performed in Thailand, consumed/used outside Thailand |
| International transport of goods | Section 80/1(3) | By aircraft, vessel, or vehicle |
| International transport of passengers | Section 80/1(4) | By aircraft or vessel departing Thailand |
| Sale of goods/services to bonded warehouses | Section 80/1(5) | Duty-free zone supplies |
| Sale of goods/services between bonded warehouses | Section 80/1(6) | Inter-zone transfers |

### Exempt Supplies -- Section 81

| Category | Legislation | Notes |
|----------|-------------|-------|
| Unprocessed agricultural products | Section 81(1)(a) | Includes livestock, crops, fishery products sold by farmers/cooperatives |
| Agricultural inputs | Section 81(1)(b) | Fertilizers, animal feed, pesticides, seeds |
| Newspapers, magazines, textbooks | Section 81(1)(c) | Printed educational/news publications |
| Healthcare / medical services | Section 81(1)(d) | Services of hospitals, clinics (government and private); does not include cosmetic surgery [T2] |
| Educational services | Section 81(1)(e) | Government and private schools under the education law |
| Cultural, religious services | Section 81(1)(f) | Museums, libraries, religious activities |
| Domestic transport | Section 81(1)(g) | Public domestic transport only (not courier/freight) |
| Rental of immovable property | Section 81(1)(h) | Residential and commercial property rental |
| Financial services | Section 81(1)(i) | Interest, credit card services, life insurance premiums (specific financial institution services) |
| Services of government agencies | Section 81(1)(j) | Government services not competing with private sector |
| Goods/services from small operators below THB 1.8M | Section 81/1 | Annual turnover below registration threshold |

### Taxable at 7% -- Everything Else

All supplies of goods and services in Thailand that are not zero-rated under Section 80/1 or exempt under Section 81 are taxable at 7%.

---

## Step 4: Registration Rules [T1]

**Legislation:** Revenue Code, Section 85/1 -- 85/18

| Rule | Detail |
|------|--------|
| Mandatory registration threshold | Annual turnover exceeding THB 1,800,000 from taxable supplies |
| Timing | Must apply for registration within 30 days after turnover exceeds threshold |
| Voluntary registration | Allowed for any business making taxable supplies, even below threshold (Section 85/3) |
| Branch registration | Each branch must be separately registered with the Revenue Department; separate PP.30 unless consolidated filing approved |
| Non-resident e-service providers | Must register if providing electronic services to non-VAT-registered recipients in Thailand exceeding THB 1.8M/year (Section 85/13) |
| Cancellation | May apply to cancel if turnover falls below THB 1.8M for 2 consecutive years, or upon cessation |

### Registration Consequences [T1]

| Status | Input VAT Recovery | Output VAT Obligation |
|--------|--------------------|-----------------------|
| VAT registered | Full recovery on business-related purchases (subject to blocking rules) | Must charge 7% on taxable supplies |
| Not registered (below threshold) | No recovery | No output VAT obligation |
| Exempt activity operator | No recovery | No output VAT obligation |

---

## Step 5: Reverse Charge Mechanics [T1]

**Legislation:** Revenue Code, Section 83/6(2) (services from abroad); Section 83/8 (import of goods)

### Services Received from Abroad [T1]

When a Thai VAT-registered person receives services from a foreign provider who has no business establishment in Thailand:

1. The Thai recipient must self-assess VAT at 7% on the service value
2. File Form PP.36 (ภ.พ.36) and pay the output VAT by the 7th of the following month
3. The same amount may be claimed as input tax credit on the PP.30 for that month (if the service relates to taxable business activities)
4. **Net effect: zero for fully taxable businesses**

**Key difference from other jurisdictions:** Thailand uses a separate form (PP.36) for the output side of the reverse charge, not the main PP.30. The input credit then appears on the PP.30.

### Import of Goods [T1]

- VAT on imported goods is collected by Customs at the border (Section 83/8)
- The customs VAT receipt (ใบเสร็จศุลกากร) serves as the tax invoice for input credit purposes
- Claim input VAT on PP.30 Line 2.2

### Exceptions to Reverse Charge [T1]

- Services received from abroad that are exempt under Section 81: NO reverse charge (e.g., certain financial services)
- Goods imported: NOT reverse charge on PP.36; VAT paid at Customs instead
- Out-of-scope items (salaries, dividends, loan repayments): NEVER reverse charge

---

## Step 6: Blocked Input Tax [T1]

**Legislation:** Revenue Code, Section 82/5; Ministerial Regulation No. 26; Revenue Department Order Paw.86/2542

The following input tax CANNOT be credited, regardless of business purpose:

| Blocked Category | Legislation | Notes |
|------------------|-------------|-------|
| Entertainment expenses | Section 82/5(4); Ministerial Reg. No. 26 | Meals, gifts, recreation for clients or non-employees |
| Passenger vehicles and related expenses | Section 82/5(4); Revenue Dept. Order Paw.86/2542 | Cars seating not more than 10 passengers; includes lease payments, fuel, repairs. Exception: car dealers, car rental businesses, tourist transport businesses |
| Purchases without valid tax invoice | Section 82/5(1) | Tax invoice must comply with Section 86/4 requirements |
| Expenses not related to the business | Section 82/5(3) | Personal use items |
| Input tax on exempt supplies | Section 82/5(6) | Purchases attributable to exempt revenue under Section 81 |
| Purchases from non-VAT-registered suppliers | Section 82/5(1) | No valid tax invoice issued |
| Know-how or goodwill acquired | Section 82/5(4) | Intangible acquisitions in specified categories |

### Passenger Vehicle Blocking Rule -- Detail [T1]

**Legislation:** Revenue Dept. Order Paw.86/2542

- Applies to sedans, SUVs, pickup trucks with cap, and similar vehicles seating up to 10 persons
- **Blocked:** purchase/lease cost, fuel, maintenance, insurance, parking for such vehicles
- **Exceptions (input tax IS recoverable):**
  - Car dealers (buying/selling cars as inventory)
  - Car rental operators (vehicles rented to customers)
  - Tourism/transport operators licensed to carry tourists
- Single-cab pickup trucks and trucks designed for goods carriage: NOT blocked
- If client claims vehicle is for excepted use, [T2] flag for practitioner confirmation

---

## Step 7: Tax Invoice Requirements [T1]

**Legislation:** Revenue Code, Section 86/4

A valid tax invoice (ใบกำกับภาษี) must contain:

1. The words "Tax Invoice" or "ใบกำกับภาษี" prominently displayed
2. Name, address, and TIN of the issuer (seller)
3. Name, address, and TIN of the recipient (buyer) -- for invoices exceeding THB 1,000 [T1]
4. Sequential invoice number
5. Description of goods or services, quantity, and unit price
6. VAT amount stated separately
7. Date of issue
8. Branch number of issuer (Head Office = 00000, branches numbered sequentially)

### Abbreviated Tax Invoice [T1]

- Permitted for retail sales under Section 86/6 for operators approved by the Revenue Department
- Does not require buyer's name, address, or TIN
- Approved via application; commonly used by department stores, convenience stores, gas stations

### Credit Notes and Debit Notes [T1]

**Legislation:** Revenue Code, Sections 86/9 -- 86/10

- **Credit note:** issued when the taxable base decreases after the tax invoice was issued (returns, discounts, price adjustments)
- **Debit note:** issued when the taxable base increases after the tax invoice was issued
- Must reference the original tax invoice number and date
- Adjustments reflected in the PP.30 for the month the credit/debit note is issued

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Revenue Code, Sections 83, 83/6, 89, 89/1

### Filing Deadlines

| Form | Period | Deadline | Notes |
|------|--------|----------|-------|
| PP.30 (ภ.พ.30) | Monthly | 15th of the following month (paper); 23rd of the following month (e-filing) | Main VAT return |
| PP.36 (ภ.พ.36) | Per transaction | 7th of the month following payment | Reverse charge on services from abroad |

### Penalties for Late Filing [T1]

| Offence | Penalty | Legislation |
|---------|---------|-------------|
| Late filing of PP.30 | Surcharge: 1.5% per month on unpaid tax (Section 89/1) | Section 89/1 |
| Late payment of VAT | Surcharge: 1.5% per month on unpaid tax, capped at amount of tax | Section 89/1 |
| Failure to file | Fine: up to THB 5,000 (Section 90/1) plus surcharge | Section 90/1, 89/1 |
| Understating output tax | Penalty: 1x the understated tax amount (Section 89(3)) | Section 89(3) |
| Overstating input tax | Penalty: 1x the overstated credit (Section 89(4)) | Section 89(4) |
| Fraudulent intent | Penalty: 2x the tax amount (Section 89(7)) plus criminal prosecution | Section 89(7) |
| Failure to register | Fine: up to THB 10,000 (Section 90/2(1)) | Section 90/2(1) |
| Failure to issue tax invoice | Fine: up to THB 5,000 (Section 90/2(3)) | Section 90/2(3) |
| Issuing false tax invoice | Criminal penalty: 2-7 years imprisonment (Section 90/4(3)) | Section 90/4(3) |

### Surcharge Calculation [T1]

```
Surcharge = Unpaid Tax * 1.5% * Number of months (or fraction of month) late
Maximum surcharge = amount of tax due
```

If filed within 7 days of deadline and tax is paid: reduced penalty of THB 300 for PP.30.

---

## Step 9: Partial Input Tax Allocation [T2]

**Legislation:** Revenue Code, Section 82/6; Ministerial Regulation No. 29

When a business makes both taxable and exempt supplies, input tax must be allocated:

### Allocation Method [T2]

1. **Direct allocation:** Input tax directly attributable to taxable supplies is fully creditable. Input tax directly attributable to exempt supplies is fully blocked.
2. **Pro-rata allocation:** For shared/common expenses, apply the formula:

```
Creditable Input Tax = Total Common Input Tax * (Taxable Revenue / Total Revenue)
```

3. The pro-rata is calculated on a **yearly basis** using annual revenue figures.
4. Monthly PP.30 filings use an **estimated** pro-rata based on prior year. Annual adjustment is made in the December PP.30 (or final month of accounting period).

**Flag for practitioner: pro-rata calculation and allocation method must be confirmed before applying. The Revenue Department may challenge the allocation methodology.**

---

## Step 10: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| VAT registration | THB 1,800,000 annual turnover | Section 85/1 |
| Tax invoice -- buyer details required | THB 1,000 per transaction | Section 86/4 |
| Abbreviated tax invoice eligibility | Retail operators approved by Revenue Dept. | Section 86/6 |
| Non-resident e-service registration | THB 1,800,000 annual revenue from Thai non-VAT-registered recipients | Section 85/13 |
| Withholding tax on service payments | Varies by service type (1-5%); separate from VAT | Section 50 (reference only) |

---

## Step 11: Withholding Tax Interaction [T1]

**Legislation:** Revenue Code, Sections 3 tre, 50, 69 bis

This is NOT a VAT issue but frequently confused with VAT:

- When a company pays for services, it must withhold income tax (typically 3% for services) and remit via Form PND.53
- Withholding tax is calculated on the **net amount before VAT**, not on the VAT-inclusive amount
- The VAT amount is paid in full to the supplier; withholding applies only to the service fee
- **Do NOT net withholding tax against VAT. They are separate obligations.**

Example: Service fee THB 100,000 + VAT THB 7,000 = total THB 107,000. Pay supplier THB 104,000 (THB 107,000 - THB 3,000 WHT). Remit THB 3,000 WHT via PND.53. Claim THB 7,000 input VAT on PP.30.

---

## Step 12: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- Foreign software subscription (e.g., Microsoft 365, AWS) [T1]

**Situation:** Thai company subscribes to cloud services from a US provider. No VAT on invoice.
**Resolution:** Reverse charge applies under Section 83/6(2). File PP.36 by the 7th of the following month, self-assessing 7% VAT on the service fee. Claim the same amount as input tax on the PP.30 for that month (Line 2.1). Net effect zero for fully taxable business.
**Legislation:** Revenue Code, Section 83/6(2).

### EC2 -- Employee entertainment vs. client entertainment [T1]

**Situation:** Company hosts a dinner. Some attendees are employees, some are clients.
**Resolution:** Entertainment of clients/non-employees: input tax BLOCKED under Section 82/5(4) and Ministerial Regulation No. 26. Entertainment of employees only (year-end party, training event): input tax IS creditable as a staff welfare expense. Mixed event: entire input tax is blocked unless the employee-only portion can be separately invoiced. [T2] if separation is claimed -- flag for practitioner.
**Legislation:** Section 82/5(4); Ministerial Regulation No. 26.

### EC3 -- Company car -- sedan vs. pickup truck [T1]

**Situation:** Company purchases a vehicle. Is input VAT recoverable?
**Resolution:** Sedan/SUV (10 seats or fewer): input tax BLOCKED. Single-cab pickup truck (designed for goods carriage): input tax RECOVERABLE. Double-cab pickup with passenger cap: BLOCKED. If vehicle type is ambiguous, [T2] flag for practitioner to verify vehicle registration classification.
**Legislation:** Revenue Dept. Order Paw.86/2542.

### EC4 -- Rental of office space [T1]

**Situation:** Company pays office rent to a landlord.
**Resolution:** Rental of immovable property is EXEMPT under Section 81(1)(h). No VAT is charged by the landlord, no input tax to claim. However, if the landlord bundles services (cleaning, security, utilities) in a separate "service charge" and is VAT-registered, that service charge portion IS subject to VAT and input tax is creditable.
**Legislation:** Revenue Code, Section 81(1)(h).

### EC5 -- Goods destroyed or lost before sale [T2]

**Situation:** Inventory is damaged/destroyed by flood, fire, or theft. Input VAT was previously claimed.
**Resolution:** If goods are lost/destroyed through force majeure and the operator notifies the Revenue Department within 15 days of the event, no output VAT adjustment is required (Section 77/1(8)(e)). If goods are lost through negligence or no notification, the operator must treat the loss as a deemed sale and account for output VAT on the fair market value. Flag for practitioner: confirm whether the loss qualifies as force majeure and whether notification was timely.
**Legislation:** Revenue Code, Section 77/1(8)(d)-(e); Revenue Department Notification.

### EC6 -- Free samples and promotional goods [T1]

**Situation:** Company gives away products as free samples.
**Resolution:** Distribution of goods for free is a deemed sale under Section 77/1(8)(d). Output VAT must be assessed at 7% of the market value. The input tax on the goods given away is creditable (not blocked) as it relates to a business promotional activity.
**Legislation:** Revenue Code, Section 77/1(8)(d); Section 79/3(1).

### EC7 -- Bad debt relief [T2]

**Situation:** Customer fails to pay an invoice. Output VAT was already accounted for.
**Resolution:** Bad debt VAT relief is available under Section 82/11 if: (a) the debt has been outstanding for at least 6 months; (b) the operator has taken legal action or written off the debt under the accounting standards; (c) the amount is less than THB 500,000 or legal action has been pursued for amounts exceeding THB 500,000. Issue a credit note per Section 86/10 and reduce output tax in the month the credit note is issued. Flag for practitioner: confirm all conditions are met before claiming relief.
**Legislation:** Revenue Code, Section 82/11; Ministerial Regulation No. 186.

### EC8 -- Sale of business as a going concern [T3]

**Situation:** An entire business is sold, including assets, inventory, and goodwill.
**Resolution:** Transfer of an entire business to a new operator may be outside the scope of VAT under certain conditions per Revenue Department rulings. However, individual asset transfers within the deal may still be subject to VAT. This is highly fact-specific. ESCALATE to practitioner. Do not classify.
**Legislation:** Revenue Department Rulings (case-specific).

### EC9 -- Deposit invoices and advance payments [T1]

**Situation:** Customer pays a deposit before goods are delivered or services are completed.
**Resolution:** VAT point (tax point) arises at the earlier of: (a) delivery of goods / completion of services, (b) issuance of the tax invoice, (c) receipt of payment (Section 78). Therefore, receiving a deposit triggers the VAT point. Issue a tax invoice and account for output VAT in the month the deposit is received.
**Legislation:** Revenue Code, Section 78.

### EC10 -- E-commerce platform seller [T2]

**Situation:** Small seller on Shopee/Lazada exceeds THB 1.8M turnover.
**Resolution:** Must register for VAT within 30 days of exceeding the threshold. Must issue tax invoices for all subsequent sales. Platform fees charged by Shopee/Lazada (with VAT) are creditable input tax. Flag for practitioner: confirm whether the platform has been collecting VAT on behalf of the seller under any marketplace facilitator arrangements, which could create double-taxation issues.
**Legislation:** Revenue Code, Section 85/1; Revenue Department guidelines on e-commerce.

---

## Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed Thai tax practitioner must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Thai tax practitioner. Document gap.
```

---

## Step 14: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard domestic sale at 7%

**Input:** Thai VAT-registered company sells goods to Thai customer, net THB 500,000.
**Expected output:** PP.30 Line 1.1 = THB 500,000. Line 1.4 (output tax) = THB 35,000. Tax invoice issued for THB 535,000.

### Test 2 -- Export sale, zero-rated

**Input:** Thai company exports goods to Japan. FOB value THB 1,000,000. Customs export declaration obtained.
**Expected output:** PP.30 Line 1.2 = THB 1,000,000. Line 1.4 = THB 0 (no output tax on zero-rated). Input tax on production costs fully recoverable.

### Test 3 -- Domestic purchase, standard 7%

**Input:** Thai company purchases office supplies from VAT-registered supplier. Net THB 50,000, VAT THB 3,500. Valid tax invoice obtained.
**Expected output:** PP.30 Line 2.1 = THB 50,000. Line 2.4 includes THB 3,500 input tax. Fully creditable (not blocked).

### Test 4 -- Reverse charge on foreign service (PP.36)

**Input:** Thai company pays USD 10,000 (~THB 350,000) to a US law firm for legal advisory. No Thai VAT on invoice.
**Expected output:** File PP.36 by 7th of following month. Self-assess output VAT = THB 350,000 * 7% = THB 24,500. Claim THB 24,500 as input tax on PP.30 Line 2.1. Net effect = zero.

### Test 5 -- Client entertainment, blocked input

**Input:** Thai company hosts dinner for clients. Restaurant bill THB 21,400 (net THB 20,000, VAT THB 1,400). Valid tax invoice obtained.
**Expected output:** PP.30 Line 2.5 = THB 1,400 (blocked input under Section 82/5(4)). Line 2.6 reduced by THB 1,400. No input credit. Expense is THB 21,400 gross cost.

### Test 6 -- Purchase of sedan (blocked vehicle)

**Input:** Thai company purchases a Toyota Camry sedan for THB 1,284,000 (net THB 1,200,000, VAT THB 84,000).
**Expected output:** PP.30 Line 2.5 = THB 84,000 (blocked input). No input credit. Full THB 1,284,000 is cost of the asset.

### Test 7 -- Import of goods (Customs VAT)

**Input:** Thai company imports machinery from Germany. CIF value THB 2,000,000. Customs duty THB 100,000. VAT paid at Customs = 7% of (THB 2,000,000 + THB 100,000) = THB 147,000.
**Expected output:** PP.30 Line 2.2 = THB 2,100,000 (CIF + duty). Line 2.4 includes THB 147,000. Input credit = THB 147,000 (assuming fully taxable business).

### Test 8 -- Non-registered small operator, below threshold

**Input:** Freelancer earns THB 1,500,000/year from services. Not VAT registered.
**Expected output:** No PP.30 filing required. No output VAT charged. No input VAT recovery. Exempt under Section 81/1 (below THB 1.8M). Income subject to personal income tax only.

### Test 9 -- Exempt rental income with separate service charge

**Input:** Landlord (VAT-registered for other activities) rents office to tenant. Monthly rent THB 100,000 (exempt). Monthly service charge THB 20,000 + VAT THB 1,400 (taxable).
**Expected output:** Rent THB 100,000 is exempt -- no output VAT. Service charge THB 20,000 goes to PP.30 Line 1.1. Output tax THB 1,400 in Line 1.4. Tenant claims THB 1,400 input tax.

### Test 10 -- Free samples (deemed sale)

**Input:** Company distributes 500 product samples, market value THB 200 each. Total market value THB 100,000.
**Expected output:** Deemed sale under Section 77/1(8)(d). PP.30 Line 1.1 = THB 100,000. Output tax = THB 7,000. Input tax on the goods distributed is creditable.

---

## PROHIBITIONS [T1]

- NEVER let AI guess PP.30 line items -- they are deterministic from facts
- NEVER apply input tax credit without a valid tax invoice per Section 86/4
- NEVER credit input tax on blocked categories (entertainment, passenger vehicles, personal use)
- NEVER omit PP.36 filing for reverse charge on foreign services -- it is a separate obligation from PP.30
- NEVER confuse zero-rated (0%, input tax recoverable) with exempt (no VAT, input tax NOT recoverable)
- NEVER apply 10% rate -- the current effective rate is 7% unless a Royal Decree extension is not renewed
- NEVER combine branch filings unless consolidated filing has been approved by the Revenue Department
- NEVER confuse withholding tax (income tax) with VAT -- they are separate obligations, separate forms, separate deadlines
- NEVER classify property rental as taxable -- it is exempt under Section 81(1)(h); only service charges are taxable
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER file PP.30 without reconciling to the purchase and sales tax invoice registers (รายงานภาษีซื้อ / รายงานภาษีขาย)

---

## Contribution Notes

This skill requires validation by a licensed Thai tax practitioner (ผู้สอบบัญชีภาษีอากร or สอบบัญชีรับอนุญาต) before production use. All T1 rules are based on the Revenue Code as of early 2026 and Revenue Department published guidance. The 7% rate has been confirmed extended through 30 September 2026 (Royal Decree No. 799). Tax practitioners should verify against current Royal Decrees for the applicable VAT rate period.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
