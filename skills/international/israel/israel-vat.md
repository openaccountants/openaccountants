---
name: israel-vat
description: Use this skill whenever asked to prepare, review, or advise on an Israel VAT (Ma'am / Mas Erech Musaf) return or any Ma'am-related classification. Trigger on phrases like "prepare VAT return", "Israel VAT", "Ma'am", "Mas Erech Musaf", "Osek Murshe", "Osek Patur", or any request involving Israeli VAT obligations. This skill contains the complete Israeli Ma'am classification rules, rate tables, registration categories, filing deadlines, and deductibility rules required to produce a correct return. ALWAYS read this skill before touching any Israel VAT-related work.
---

# Israel VAT (Ma'am / Mas Erech Musaf) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | State of Israel (Medinat Yisrael) |
| Jurisdiction Code | IL |
| Primary Legislation | Chok Mas Erech Musaf, 5736-1975 (VAT Law of 1975) |
| Supporting Legislation | Takanot Mas Erech Musaf (VAT Regulations); Income Tax Ordinance (for Osek Patur thresholds); Customs Ordinance (import VAT) |
| Tax Authority | Rashut HaMisim (Israel Tax Authority -- ITA) |
| Filing Portal | https://www.gov.il/he/departments/israel_tax_authority (Shaam portal) |
| Skill Version | 1.0 |
| Validated By | Deep research verification, April 2026 |
| Confidence Coverage | Tier 1: rate classification, return field assignment, registration categories, deductibility rules. Tier 2: partial exemption, non-profit institutions, Palestinian Authority transactions. Tier 3: complex group structures, Eilat free trade zone, multinational transfer pricing. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax adviser and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and business number (Osek number)** [T1] -- 9-digit business registration number
2. **Registration category** [T1] -- Osek Murshe (licensed/standard dealer), Osek Patur (exempt dealer), Mil'ra (non-profit institution), or Mosad Kespi Finansi (financial institution)
3. **Filing frequency** [T1] -- Monthly (turnover > ILS threshold) or bi-monthly (turnover <= ILS threshold)
4. **Industry/sector** [T2] -- Impacts specific deductibility rules and potential zero-rating
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required
6. **Is the client located in Eilat?** [T3] -- Eilat Free Trade Zone has special VAT-free rules
7. **Does the client transact with Palestinian Authority entities?** [T2] -- Special clearance rules apply
8. **Credit carried forward from prior period** [T1]
9. **Does the client export goods or services?** [T1] -- Zero-rated; refund eligibility
10. **Is the client a Mil'ra (non-profit)?** [T2] -- Different Ma'am treatment and rates apply

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Sale (output Ma'am -- mas etzot) or Purchase (input Ma'am -- mas tsumotkha)
- Salaries (maskoret), social contributions (bituach leumi), tax payments, loan repayments, dividends = OUT OF SCOPE (never on Ma'am return)
- **Legislation:** VAT Law 5736-1975, Section 2 (taxable transactions)

### 1b. Determine Counterparty Location [T1]

- **Domestic (Israel):** Supplier/customer is in Israel (including West Bank settlements for tax purposes) [T2]
- **Palestinian Authority:** Special clearance rules under Paris Protocol [T2]
- **Foreign:** All other countries
- **Eilat:** VAT-free zone; special rules apply [T3]
- **Note:** Israel is NOT an EU/EEA member state. No intra-community supply rules apply.
- **Legislation:** VAT Law 5736-1975, Section 15 (place of supply)

### 1c. Determine Ma'am Rate [T1]

| Rate | Category | Legal Basis |
|------|----------|-------------|
| 18% | Standard rate | VAT Law Section 2; Finance Minister's Order |
| 0% | Zero-rated (exports, tourism services, fruits/vegetables) | VAT Law Section 30 |

**Rate history:**

| Period | Rate |
|--------|------|
| Until 30 September 2015 | 18% |
| 1 October 2015 -- 31 December 2024 | 17% |
| 1 January 2025 onwards | 18% |

**Note:** The rate was reduced from 18% to 17% on 1 October 2015 and restored to 18% on 1 January 2025.

**Legislation:** VAT Law Section 2; Finance Minister's Orders on rate changes

### 1d. Standard Rate (18%) Applies To [T1]

- All goods and services not specifically zero-rated or exempt
- Professional services (legal, accounting, consulting, IT, medical -- private)
- Telecommunications and electronic services
- Construction services
- Motor vehicles
- Electronics, furniture, clothing
- Restaurant and catering services
- Real property transactions (excluding residential rent)
- **Legislation:** VAT Law Section 2

### 1e. Zero-Rated Supplies (Section 30) [T1]

| Category | Legal Basis | Notes |
|----------|-------------|-------|
| Export of goods | Sec 30(a)(1) | Goods must leave Israel, confirmed by customs |
| Tourism services to incoming tourists | Sec 30(a)(2) | Hotels, tours for foreign tourists (specific conditions) [T2] |
| Fruits and vegetables (fresh) | Sec 30(a)(12) | Unprocessed; list maintained by Finance Ministry |
| International transport | Sec 30(a)(3) | Of passengers and goods |
| Services to non-resident (benefit accrues abroad) | Sec 30(a)(5) | B2B services where benefit is outside Israel |
| Supplies to Eilat zone | Sec 30(a)(6) | Goods delivered to Eilat [T3] |
| Diamonds (rough and polished -- inter-dealer) | Sec 30(a)(8) | Diamond industry specific rules |
| Gold (inter-dealer) | Sec 30(a)(9) | Precious metals industry |

**Note:** Zero-rated suppliers can claim full input Ma'am refund
**Legislation:** VAT Law Section 30

### 1f. Exempt Transactions (No Input Recovery) [T1]

| Category | Legal Basis | Notes |
|----------|-------------|-------|
| Residential property rental (dira) | Sec 31(1) | Rental of dwelling for residential use |
| Financial services (partial exemption) | Sec 31(3) | Banks and financial institutions pay profit-based tax (mas revach) instead of standard Ma'am [T2] |
| Sale of going concern | Sec 31(4) | Transfer of business as whole |
| Small transactions by Osek Patur | Sec 31(7) | Below threshold -- exempt without credit |
| Certain insurance transactions | Sec 31(3a) | Life insurance premiums [T2] |

**Note:** Financial institutions (banks, insurance companies) are subject to a special payroll + profit tax (mas revach + mas sachir) in lieu of standard Ma'am on their financial activities. This is unique to Israel.

**Legislation:** VAT Law Section 31

---

## Step 2: Registration Categories

### 2a. Osek Murshe (Licensed Dealer / Standard Registration) [T1]

| Feature | Details |
|---------|---------|
| Who | All businesses above the Osek Patur threshold |
| Threshold | Automatic if turnover exceeds ILS 120,000 per year (2025 threshold) [T2] -- updated annually |
| Obligations | Charge Ma'am on sales, file returns, issue tax invoices (cheshbonit mas) |
| Input recovery | Full input Ma'am recovery on business expenses (subject to deductibility rules) |
| Invoice type | Must issue Tax Invoice (Cheshbonit Mas) showing Ma'am separately |

**Legislation:** VAT Law Section 20, 21, 47

### 2b. Osek Patur (Exempt Dealer) [T1]

| Feature | Details |
|---------|---------|
| Who | Self-employed individuals or sole proprietors below turnover threshold |
| Threshold | Annual turnover <= ILS 120,000 (2025; adjusted annually by Finance Minister) |
| Obligations | Does NOT charge Ma'am on sales; files annual income report only |
| Input recovery | NONE -- cannot claim any input Ma'am |
| Invoice type | Issues receipt (kabala) only, NOT a tax invoice |
| Transition | Must register as Osek Murshe if turnover exceeds threshold |

**Legislation:** VAT Law Section 31(7), Regulations

### 2c. Mil'ra (Non-Profit Institution) [T2]

| Feature | Details |
|---------|---------|
| Who | Recognized non-profit organizations (amutot, public institutions) |
| Obligations | Subject to Ma'am on payroll (salary-based tax) instead of transaction-based Ma'am |
| Rate | Ma'am at reduced employer rate on salaries paid [T2] |
| Input recovery | Limited -- only on goods purchased for resale or certain qualifying activities |
| Complexity | High -- treatment varies by type of activity; mixed treatment common |

**Flag for reviewer:** Mil'ra Ma'am calculations are highly specialized. Always confirm with tax adviser.

**Legislation:** VAT Law Section 1 (definitions), Section 58-63 (Mil'ra provisions)

### 2d. Mosad Kespi Finansi (Financial Institution) [T2]

| Feature | Details |
|---------|---------|
| Who | Banks, insurance companies, provident funds |
| Obligations | Pay Ma'am as profit tax (mas revach) + payroll tax (mas sachir) instead of standard Ma'am |
| Input recovery | Special rules; not standard input deduction |
| Complexity | Very high |

**Flag for reviewer:** Financial institution Ma'am is entirely different from standard Ma'am. Always escalate [T3].

**Legislation:** VAT Law Sections 4, 58-63

---

## Step 3: Ma'am Return Structure

The Ma'am return is filed electronically via the Shaam portal.

### Section A: Output Ma'am [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| A1 | Total taxable sales (standard rate) | Net value of all 18%-rated supplies |
| A2 | Output Ma'am (18%) | = A1 x 18% |
| A3 | Zero-rated sales | Exports, fruits/vegetables, tourism |
| A4 | Exempt sales | Residential rent, financial (for reporting only) |
| A5 | Self-assessed Ma'am on imports of services | Reverse charge on foreign services |
| A6 | Total output Ma'am | = A2 + A5 |

### Section B: Input Ma'am [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| B1 | Input Ma'am on domestic purchases | From tax invoices (cheshbonit mas) |
| B2 | Import Ma'am from customs | From customs assessments (reshimat yevu) |
| B3 | Self-assessed input Ma'am (reverse charge offset) | = A5 (offsetting entry) |
| B4 | Fixed asset purchases -- input Ma'am | Capital goods input Ma'am |
| B5 | Prior period credit carried forward | Yitrat zchut |
| B6 | Adjustments (increase/decrease) | Corrections |
| B7 | Total input Ma'am | = B1 + B2 + B3 + B4 + B5 +/- B6 |

### Section C: Ma'am Payable or Refundable [T1]

```
IF A6 > B7 THEN
    C1 (Ma'am payable / mas le-tashlum) = A6 - B7
    C2 = 0
ELSE
    C1 = 0
    C2 (Ma'am refundable / yitrat zchut) = B7 - A6
END
```

**Legislation:** VAT Law Section 67-72; VAT Regulations

---

## Step 4: Reverse Charge Mechanics [T1]

### 4a. Import of Goods [T1]

- Ma'am on imported physical goods is assessed and collected by Customs (Meckes)
- Importer pays Ma'am at the border via customs declaration (reshimat yevu)
- This import Ma'am is deductible as input Ma'am (Field B2)
- **Do NOT self-assess on the Ma'am return** -- Customs handles assessment
- **Legislation:** VAT Law Section 2(2) (import as taxable transaction), Section 43 (import assessment)

### 4b. Import of Services (Self-Assessment) [T1]

- When an Israeli Osek Murshe receives services from a non-resident with no permanent establishment in Israel:
  1. Self-assess Ma'am at 18% on the service value
  2. Report output Ma'am in Field A5
  3. Deduct same amount as input Ma'am in Field B3
  4. Net effect: zero for fully taxable businesses
- **Legislation:** VAT Law Section 15(b) (reverse charge on imported services)

### 4c. Non-Resident Digital Services [T2]

- Since 2016, non-resident providers of digital services to Israeli consumers must register for Ma'am
- Major platforms (Netflix, Google, etc.) are required to register and collect Ma'am
- When the Israeli business recipient self-assesses, the standard reverse charge applies
- **Flag for reviewer:** Determine if the foreign provider is already registered and charging Ma'am
- **Legislation:** VAT Law Section 15(b); Amendment 54

---

## Step 5: Deductibility Rules

### 5a. General Deduction Right [T1]

- All input Ma'am on goods and services used for taxable business activities by an Osek Murshe is deductible
- Input Ma'am must be documented by a Tax Invoice (Cheshbonit Mas) or customs declaration
- Tax Invoice must contain: supplier name, Osek number, date, description, net amount, Ma'am amount
- Deduction must be claimed within 6 months of the invoice date (extendable to 5 years with Tax Authority approval) [T2]
- **Legislation:** VAT Law Section 38; VAT Regulations on Tax Invoices

### 5b. Non-Deductible Input Ma'am (Blocked Categories) [T1]

The following input Ma'am is BLOCKED and cannot be recovered:

| Category | Legal Basis | Notes |
|----------|-------------|-------|
| Passenger vehicles (rechev prati) | Reg. 14 | Exception: taxi, rental car, driving instruction, vehicles for disabled |
| Entertainment (iruach) | Reg. 15a | Meals, events, hospitality for clients/suppliers |
| Mobile phones | Reg. 18 | 2/3 of input Ma'am blocked (1/3 deductible) [T2] |
| Goods/services for non-business use | Sec 41 | Personal consumption |
| Purchases without proper Tax Invoice | Sec 38 | No cheshbonit mas = no deduction |

### 5c. Vehicle Deductibility Rules [T1]

| Vehicle Type | Input Ma'am Deductible | Notes |
|-------------|----------------------|-------|
| Private passenger car (sedan, SUV) | NO | Blocked -- Regulation 14 |
| Taxi | YES | Business use vehicle |
| Rental car (by rental company) | YES | Business stock |
| Delivery van (marked commercial) | YES | Must be classified as commercial vehicle |
| Truck | YES | Commercial vehicle |
| Motorcycle (for business) | YES | If used for deliveries/business |
| Fuel for blocked vehicle | NO | Follows vehicle classification |
| Fuel for deductible vehicle | YES | Follows vehicle classification |
| Repairs on blocked vehicle | 1/4 deductible | Partial deduction per Reg. 14(b) [T2] |

### 5d. Mobile Phone Rules [T1]

- Input Ma'am on mobile phone purchase: 2/3 blocked, 1/3 deductible
- Input Ma'am on mobile phone bills: 2/3 blocked, 1/3 deductible
- Exception: if the phone is used 100% for business AND the employee has a separate personal phone -- full deduction allowed [T2]
- **Flag for reviewer:** Full deduction claim on mobile requires evidence of separate personal phone
- **Legislation:** VAT Regulations, Regulation 18

### 5e. Partial Exemption (Pro-Rata) [T2]

- If a business makes both taxable and exempt supplies, input Ma'am on overhead must be apportioned
- Pro-rata formula: `Deductible % = (Taxable Supplies / Total Supplies) x 100`
- Must be agreed with the Tax Authority assessor (pakid shuma)
- **Flag for reviewer:** Pro-rata rate must be confirmed with Tax Authority before application
- **Legislation:** VAT Law Section 41; VAT Regulations

### 5f. Real Property Input Ma'am [T2]

- Input Ma'am on construction/purchase of property intended for taxable use: deductible
- Input Ma'am on property intended for residential rental (exempt): NOT deductible
- If property use changes from taxable to exempt (or vice versa) within 10 years: adjustment required
- **Flag for reviewer:** Real property input Ma'am requires careful analysis of intended use
- **Legislation:** VAT Law Section 43; VAT Regulations on real property

---

## Step 6: Invoice and Documentation Requirements

### 6a. Tax Invoice (Cheshbonit Mas) [T1]

| Requirement | Details |
|-------------|---------|
| Who must issue | All Osek Murshe (licensed dealers) |
| Mandatory fields | Supplier name, Osek number, buyer name and Osek number (if B2B), date, sequential number, description of goods/services, quantity, unit price, total before Ma'am, Ma'am amount, total including Ma'am |
| Format | Paper or electronic (both accepted) |
| Storage | 7 years |
| Duplicate | Must be marked "Hetek" (copy) |
| Threshold for buyer details | Must include buyer name and Osek number for invoices > ILS 5,000 |

**Legislation:** VAT Law Section 47; VAT Regulations on invoices

### 6b. Receipt (Kabala) [T1]

| Requirement | Details |
|-------------|---------|
| Who must issue | All dealers (both Osek Murshe and Osek Patur) upon receiving payment |
| When | Within 7 days of receiving payment |
| Content | Date, amount received, payment method |

### 6c. Tax Invoice/Receipt Combined (Cheshbonit Mas / Kabala) [T1]

- Most common document: combines the tax invoice and receipt in one document
- Issued when payment is received at the time of the transaction (e.g., retail)
- **Legislation:** VAT Regulations

### 6d. Debit Note and Credit Note [T1]

- Credit notes (cheshbonit zikui): issued to reduce a previous invoice
- Debit notes: issued to increase a previous invoice
- Must reference the original invoice number
- Reduce/increase the relevant Ma'am fields accordingly
- **Legislation:** VAT Law Section 23a

---

## Step 7: Key Thresholds

| Threshold | Value | Notes |
|-----------|-------|-------|
| Standard Ma'am rate | 18% | Since 1 January 2025 |
| Osek Patur threshold | ILS 120,000 annual turnover | 2025; adjusted annually |
| Tax Invoice buyer detail threshold | ILS 5,000 | Must include buyer details above this |
| Input Ma'am claim deadline | 6 months (standard); 5 years (with approval) | From invoice date |
| Mobile phone deductibility | 1/3 of input Ma'am | 2/3 blocked |
| Vehicle repair (blocked car) | 1/4 of input Ma'am | 3/4 blocked |
| Real property adjustment period | 10 years | Change of use |
| Document retention | 7 years | Tax invoices and records |

---

## Step 8: Filing Deadlines

### Monthly Filers [T1]

| Requirement | Details |
|-------------|---------|
| Who | Turnover above ILS threshold (set by Finance Minister; generally > ILS 1.5M annually) |
| Filing deadline | 15th of the following month |
| Payment deadline | 15th of the following month |
| Method | Electronic via Shaam portal or authorized software |

### Bi-Monthly Filers [T1]

| Requirement | Details |
|-------------|---------|
| Who | Turnover below the monthly threshold |
| Periods | Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct, Nov-Dec |
| Filing deadline | 15th of the month following the bi-monthly period |
| Payment deadline | 15th of the month following the bi-monthly period |

### Osek Patur [T1]

| Requirement | Details |
|-------------|---------|
| Filing | Annual report (doch shnati) only |
| Deadline | By 31 January of the following year |
| No Ma'am return | Osek Patur does not file periodic Ma'am returns |

**Legislation:** VAT Law Section 67-72

### Late Filing and Payment Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing | Fine: up to ILS 5,000 per occurrence |
| Late payment | Interest: linked to CPI index + 4% annual interest (hatzamada + ribit) |
| Failure to issue Tax Invoice | Criminal offense; fine + potential imprisonment |
| Failure to report transaction | Fine + potential assessment with penalties |
| Fraud / evasion | Criminal prosecution; up to 7 years imprisonment |

**Legislation:** VAT Law Sections 94-121 (penalties and offenses)

---

## Step 9: Fruits and Vegetables Zero-Rating [T1]

Israel uniquely zero-rates fresh fruits and vegetables. Key rules:

| Item | Rate | Notes |
|------|------|-------|
| Fresh fruits (unprocessed) | 0% | On the approved list |
| Fresh vegetables (unprocessed) | 0% | On the approved list |
| Fresh herbs | 0% | Included in vegetable list |
| Eggs | 0% | Fresh eggs |
| Frozen fruits/vegetables | 18% | Processing removes zero-rating |
| Canned fruits/vegetables | 18% | Processing removes zero-rating |
| Dried fruits | 18% | Processing removes zero-rating |
| Cut salads (pre-packaged) | 0% | Still considered unprocessed |
| Fresh juices (freshly squeezed) | 18% | Considered processed |
| Nuts | 18% | Not on the zero-rated list |

**Note:** The exact list is maintained by the Finance Ministry and updated periodically. When in doubt, check the current approved list. [T2]

**Legislation:** VAT Law Section 30(a)(12); Finance Minister's Order on zero-rated goods

---

## Step 10: Eilat Free Trade Zone [T3]

- Eilat (Elat) is designated as a VAT-free zone
- Goods sold and consumed in Eilat are exempt from Ma'am
- Services provided and consumed in Eilat are exempt from Ma'am
- Goods transported from Eilat to rest of Israel are subject to Ma'am (treated as import)
- **This is a complex area -- ALWAYS escalate to qualified tax adviser**
- **Legislation:** VAT Law Section 5a-5d (Eilat provisions)

---

## Step 11: Edge Case Registry

### EC1 -- Software subscription from US provider (e.g., AWS, Zoom) [T1]

**Situation:** Israeli Osek Murshe pays for cloud services from a US company, no Ma'am on invoice.
**Resolution:** Self-assess at 18% in Field A5. Deduct in Field B3. Net = zero.
**Legislation:** VAT Law Section 15(b)

### EC2 -- Export of goods [T1]

**Situation:** Israeli manufacturer exports electronics to Germany. Customs documentation obtained.
**Resolution:** Zero-rated under Section 30(a)(1). Report in Field A3. No output Ma'am. Full input recovery.
**Legislation:** VAT Law Section 30(a)(1)

### EC3 -- Sale of fresh fruits and vegetables [T1]

**Situation:** Greengrocer sells fresh tomatoes and cucumbers to customers.
**Resolution:** Zero-rated under Section 30(a)(12). Report in Field A3. No output Ma'am. Input Ma'am on related costs (packaging, transport) is deductible.
**Legislation:** VAT Law Section 30(a)(12)

### EC4 -- Purchase of passenger car [T1]

**Situation:** Osek Murshe purchases a sedan for business use, ILS 200,000 + Ma'am ILS 36,000.
**Resolution:** Input Ma'am of ILS 36,000 is BLOCKED under Regulation 14. Vehicle capitalized at ILS 236,000.
**Legislation:** VAT Regulations, Regulation 14

### EC5 -- Mobile phone purchase [T1]

**Situation:** Business buys a mobile phone for ILS 5,000 + Ma'am ILS 900.
**Resolution:** 1/3 of Ma'am deductible (ILS 300). 2/3 blocked (ILS 600). Field B1 includes ILS 300 only.
**Legislation:** VAT Regulations, Regulation 18

### EC6 -- Residential property rental income [T1]

**Situation:** Osek Murshe rents out an apartment to a tenant for residential use.
**Resolution:** Exempt under Section 31(1). No output Ma'am. Input Ma'am on related expenses (repairs, maintenance) is NOT deductible.
**Legislation:** VAT Law Section 31(1)

### EC7 -- Tourism services to incoming tourists [T2]

**Situation:** Tour operator provides guided tours to foreign tourists visiting Israel.
**Resolution:** Potentially zero-rated under Section 30(a)(2). Specific conditions must be met: tourists must be foreign nationals, service must be tourism-related. Flag for reviewer: confirm qualifying conditions.
**Legislation:** VAT Law Section 30(a)(2)

### EC8 -- Credit notes [T1]

**Situation:** Supplier issues credit note (cheshbonit zikui) for returned goods.
**Resolution:** Reduce output Ma'am fields by the credit note amounts. Credit note must reference original invoice. Buyer reduces input Ma'am accordingly.
**Legislation:** VAT Law Section 23a

### EC9 -- Entertainment expenses [T1]

**Situation:** Company hosts client dinner, Ma'am ILS 1,800 on the invoice.
**Resolution:** Entertainment Ma'am is BLOCKED under Regulation 15a. No input Ma'am recovery. Expense is deductible for income tax (at 80%) but not for Ma'am.
**Legislation:** VAT Regulations, Regulation 15a

### EC10 -- Import of goods [T1]

**Situation:** Israeli retailer imports clothing from China. Customs assessment shows Ma'am ILS 50,000.
**Resolution:** Import Ma'am deductible in Field B2 = ILS 50,000. Do NOT self-assess -- Customs handles.
**Legislation:** VAT Law Section 2(2), 43

### EC11 -- Osek Patur exceeding threshold [T1]

**Situation:** Self-employed person's turnover exceeds ILS 120,000 during the year.
**Resolution:** Must immediately register as Osek Murshe. Start charging Ma'am from the date of transition. Cannot recover input Ma'am from the Osek Patur period.
**Legislation:** VAT Law Section 31(7); Regulations

### EC12 -- Sale of business as going concern [T1]

**Situation:** Osek Murshe sells entire business to a buyer.
**Resolution:** Exempt under Section 31(4). No Ma'am charged on the sale of the business as a whole. Buyer continues with the existing Ma'am obligations.
**Legislation:** VAT Law Section 31(4)

### EC13 -- Vehicle repairs on blocked car [T2]

**Situation:** Company has car repairs done on a private vehicle (blocked under Reg 14), Ma'am ILS 2,000.
**Resolution:** 1/4 of Ma'am deductible (ILS 500). 3/4 blocked (ILS 1,500). Flag for reviewer if vehicle classification is uncertain.
**Legislation:** VAT Regulations, Regulation 14(b)

### EC14 -- Palestinian Authority transactions [T2]

**Situation:** Israeli business sells goods to a buyer in PA-administered territories.
**Resolution:** Complex clearance rules under the Paris Protocol (1994). Ma'am may be charged at Israeli rate and cleared through revenue-sharing mechanism. Flag for reviewer: specific PA transaction rules must be applied.
**Legislation:** Paris Protocol; VAT Law implementation regulations

---

## Step 12: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Qualified tax adviser must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified tax adviser. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard domestic sale at 18%

**Input:** Israeli company sells consulting services, net ILS 100,000, Ma'am ILS 18,000.
**Expected output:** Field A1 = ILS 100,000. Field A2 = ILS 18,000. Output Ma'am reported.

### Test 2 -- Sale of fresh vegetables (zero-rated)

**Input:** Greengrocer sells fresh tomatoes, net ILS 10,000.
**Expected output:** Field A3 = ILS 10,000. No output Ma'am.

### Test 3 -- Export of goods

**Input:** Israeli manufacturer exports goods to the US, net ILS 500,000. Customs documentation obtained.
**Expected output:** Field A3 = ILS 500,000. No output Ma'am. Input Ma'am refundable.

### Test 4 -- Import of services, reverse charge

**Input:** Israeli company receives marketing services from UK agency, GBP 10,000 (approx. ILS 47,000). No Ma'am.
**Expected output:** Field A5 = ILS 8,460 (18% of ILS 47,000). Field B3 = ILS 8,460. Net = zero.

### Test 5 -- Passenger car purchase, blocked

**Input:** Company purchases sedan, ILS 250,000 + Ma'am ILS 45,000.
**Expected output:** Input Ma'am ILS 45,000 BLOCKED. Vehicle capitalized at ILS 295,000.

### Test 6 -- Mobile phone bill

**Input:** Monthly phone bill ILS 300 + Ma'am ILS 54.
**Expected output:** Deductible input Ma'am = ILS 18 (1/3). Blocked = ILS 36 (2/3).

### Test 7 -- Entertainment expense, blocked

**Input:** Client dinner, net ILS 2,000, Ma'am ILS 360.
**Expected output:** Input Ma'am ILS 360 BLOCKED. No Ma'am recovery.

### Test 8 -- Osek Patur transaction

**Input:** Osek Patur freelancer earns ILS 5,000 from a client.
**Expected output:** No Ma'am charged. No return filed for this period. Income reported annually.

---

## PROHIBITIONS [T1]

- NEVER allow input Ma'am deduction on passenger vehicles (unless taxi/rental/disabled)
- NEVER allow any input Ma'am recovery for Osek Patur -- they are exempt without credit
- NEVER charge Ma'am on fresh fruits and vegetables on the approved zero-rated list
- NEVER skip self-assessment on imported services -- reverse charge is mandatory
- NEVER allow full input Ma'am on mobile phones -- 2/3 is blocked
- NEVER allow input Ma'am on entertainment -- fully blocked
- NEVER confuse zero-rated (Section 30, with input recovery) with exempt (Section 31, without recovery)
- NEVER process Eilat transactions without qualified tax adviser -- escalate [T3]
- NEVER confuse the 17% rate (pre-2025) with the current 18% rate
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI
- NEVER process financial institution (Mosad Kespi Finansi) Ma'am -- entirely different system [T3]

---

## Step 14: Advance Payments and Tax Point Rules

### 14a. Tax Point (Meudad Ha'erech) [T1]

| Event | Tax Point | Legal Basis |
|-------|-----------|-------------|
| Supply of goods | Date of delivery or date of invoice, whichever is earlier | Sec 22 |
| Supply of services | Date of completion or date of invoice, whichever is earlier | Sec 23 |
| Advance payment received | Date of receipt | Sec 22(b) |
| Continuous supply | End of each billing period | Sec 24 |
| Import of goods | Date of customs clearance | Sec 26 |
| Rental income | Date rent is due | Sec 24a |

### 14b. Advance Payments [T1]

- When an advance payment is received, Ma'am is triggered immediately
- Tax Invoice/Receipt must be issued within 14 days of receipt
- **Legislation:** VAT Law Section 22(b), 46

---

## Step 15: Special Sector Rules

### 15a. Real Property Transactions [T2]

| Transaction | Ma'am Treatment | Notes |
|-------------|----------------|-------|
| Sale of new residential apartment (by developer) | 18% | Standard rate on sale price |
| Sale of used residential apartment (by individual) | Exempt | Not a business transaction |
| Commercial property sale | 18% | Standard rate |
| Commercial property rental | 18% | Standard rate |
| Residential property rental | Exempt | Section 31(1) |
| Construction services | 18% | Standard rate |
| Real estate agent commission | 18% | Standard rate |

**Flag for reviewer:** Real property transactions may involve additional taxes (betterment tax / hetel hashbacha, purchase tax / mas rechisha). These are outside the scope of Ma'am but relevant to the overall transaction.

### 15b. Digital Economy [T2]

| Scenario | Treatment | Notes |
|----------|-----------|-------|
| Non-resident digital service provider to consumers (B2C) | Must register and charge 18% | Amendment 54 |
| Non-resident B2B digital services | Reverse charge by Israeli recipient | Standard self-assessment |
| Israeli SaaS company selling to foreign B2B | Zero-rated (benefit accrues abroad) | Section 30(a)(5) |
| Israeli app developer selling to foreign consumers | Zero-rated (if benefit abroad) [T2] | Must demonstrate foreign benefit |
| Marketplace facilitator | Platform may be deemed supplier [T2] | Complex rules |

### 15c. Diamond Industry [T3]

- Special rules for the diamond exchange (Bursa Heyahlomim)
- Inter-dealer transactions in rough and polished diamonds may be zero-rated
- Complex documentation requirements
- **ALWAYS escalate to diamond industry tax specialist**
- **Legislation:** VAT Law Section 30(a)(8)-(9)

---

## Step 16: Penalties and Interest Detailed Reference

| Violation | Amount / Rate | Legal Basis |
|-----------|--------------|-------------|
| Late filing | Fine: up to ILS 5,000 per return | Sec 94 |
| Late payment | Linkage differentials (hatzamada) + interest at 4% p.a. | Sec 95 |
| Failure to issue Tax Invoice | Criminal offense: fine + up to 1 year imprisonment | Sec 117 |
| Issuing fictitious Tax Invoice | Criminal offense: fine + up to 5 years imprisonment | Sec 117(b)(5) |
| Failure to report transaction | Fine + estimated assessment with penalties | Sec 94-95 |
| Tax fraud / evasion | Criminal offense: up to 7 years imprisonment | Sec 117(b) |
| Failure to register as Osek Murshe | Fine + retroactive registration + estimated assessments | Sec 94 |
| Claiming input Ma'am without Tax Invoice | Assessment reversal + fine | Sec 95 |
| Osek Patur exceeding threshold without registering | Fine + retroactive Ma'am obligation | Sec 94 |
| CPI-linked interest on unpaid Ma'am | Consumer Price Index linkage + 4% real interest | Sec 95 |

---

## Step 17: Record-Keeping Requirements

### 17a. Books and Records [T1]

| Requirement | Details |
|-------------|---------|
| Accounting records | Must maintain per Income Tax Ordinance and Ma'am Regulations |
| Purchase register | Chronological record of all purchases with Ma'am details |
| Sales register | Chronological record of all sales with Ma'am details |
| Fixed asset register | For capital goods with Ma'am implications |
| Retention period | 7 years from end of the tax year |
| Format | Paper or electronic (both accepted; electronic preferred) |
| Inspection | ITA may inspect at any time during business hours |

**Legislation:** VAT Law Section 69-74; VAT Regulations on record-keeping

---

## Contribution Notes

This skill covers Israeli Ma'am as of April 2026. Israeli tax law is subject to amendment by the Knesset and ministerial orders. All rates and thresholds (especially the Osek Patur threshold and zero-rated goods list) should be verified against the most recent ITA publications before filing. A qualified Israeli tax adviser (yo'etz mas) or CPA (ro'e cheshbon) must validate all T1 rules before this skill is used in production.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
