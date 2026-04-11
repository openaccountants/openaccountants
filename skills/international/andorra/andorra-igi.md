---
name: andorra-igi
description: Use this skill whenever asked to prepare, review, or advise on an Andorran IGI (Impost General Indirecte / General Indirect Tax) return or any transaction classification for Andorran indirect tax purposes. Trigger on phrases like "Andorra VAT", "Andorra IGI", "Andorran tax", "IGI return", or any request involving Andorran indirect tax obligations. Andorra does NOT have VAT; it has the IGI, a general indirect tax introduced in 2013 at a standard rate of 4.5% -- one of the lowest indirect tax rates in Europe. ALWAYS read this skill before touching any Andorran IGI-related work.
---

# Andorra IGI (General Indirect Tax) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Principality of Andorra |
| Jurisdiction Code | AD |
| Tax Name | IGI (Impost General Indirecte / General Indirect Tax) |
| Primary Legislation | Llei 11/2012, del 21 de juny, de l'Impost General Indirecte (Law 11/2012 on the General Indirect Tax) |
| Supporting Legislation | Reglament de l'IGI (IGI Regulations); Llei 21/2014 (amendments); Llei 3/2019 (amendments) |
| Tax Authority | Department of Taxes and Borders (Departament de Tributs i de Fronteres) |
| Filing Portal | https://www.e-govern.ad (Andorran Government electronic services) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, standard classification, basic input deductions. Tier 2: financial services treatment, cross-border with Spain/France, special regimes. Tier 3: complex structures, international tax treaties. |

---

## IMPORTANT: IGI is NOT VAT [T1]

Andorra's IGI is a general indirect tax conceptually similar to VAT but with key differences:
- **Introduced in 2013** -- Andorra had NO indirect tax before this
- **Very low rate:** 4.5% standard (compared to EU minimum of 15%)
- **NOT harmonized with EU VAT Directive** -- Andorra is not an EU member
- **No customs union** with the EU (unlike Liechtenstein/Switzerland) -- Andorra has its own customs territory
- **Andorra has a customs agreement** with the EU for industrial goods (but not services or agricultural goods)

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and NRT (Numero de Registre Tributari)** [T1] -- tax registration number
2. **IGI registration status** [T1] -- obligatori (mandatory) or voluntari (voluntary) registrant
3. **IGI period** [T1] -- quarterly (standard) or monthly (optional for larger entities)
4. **Industry/sector** [T2] -- impacts rate (financial services, education, medical, etc.)
5. **Does the business make exempt supplies?** [T2] -- proportional deduction rules apply
6. **Does the business trade cross-border?** [T1] -- impacts import treatment (Spain/France borders)
7. **Accumulated IGI credit** [T1] -- from prior periods
8. **Does the business provide financial/banking services?** [T2] -- special IGI treatment

**If any of items 1-3 are unknown, STOP.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output IGI) or Purchase (input IGI)
- Salaries, social security (CASS), dividends, loan repayments = OUT OF SCOPE
- **Legislation:** Law 11/2012, Article 4

### 1b. Determine Counterparty Location [T1]
- Andorra (domestic): supplier/customer in Andorra
- Spain: primary trading partner (direct land border)
- France: second trading partner (direct land border)
- Other foreign: all other countries
- **Note:** Andorra has no direct border with any other country besides Spain and France

### 1c. Determine IGI Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 4.5% | Standard rate -- most goods and services | Article 57 |
| 1% | Reduced rate -- food, water, books, cultural events | Article 57(2) |
| 2.5% | Intermediate reduced rate -- transport, para-pharmaceutical goods | Article 57(3) |
| 0% | Zero rate -- exports, international transport, gold to Andorran financial institutions | Article 58 |
| 9.5% | Increased rate -- banking and financial services | Article 57(4) |
| Exempt | Medical services, educational services, residential rental, insurance, certain financial operations | Article 50 |

### 1d. Rate Categories in Detail [T1]

**Standard Rate -- 4.5%:**
- Most goods and services not covered by other rates
- Professional services (consulting, legal, accounting)
- Telecommunications
- Retail goods (clothing, electronics, household goods)
- Construction services
- Hospitality/hotel services
- Restaurant services

**Reduced Rate -- 1%:**
- Basic food products (bread, milk, eggs, fruits, vegetables, meat, fish)
- Water supply
- Books and periodicals
- Cultural events and activities
- Live theatrical, musical, and dance performances

**Intermediate Reduced Rate -- 2.5%:**
- Passenger transport services
- Para-pharmaceutical products (health supplements, vitamins, cosmetics with therapeutic claims)
- Optical products (glasses, contact lenses)

**Increased Rate -- 9.5%:**
- Banking services (not exempt)
- Financial services (not exempt)
- Investment management
- Financial advisory services

**Note:** The 9.5% rate on financial services is unusual -- most countries exempt financial services from indirect tax. Andorra taxes them at a higher-than-standard rate.

### 1e. Exempt Supplies (Article 50) [T1]

The following are exempt from IGI:
- Medical and health services (licensed)
- Educational services (accredited institutions)
- Insurance services (premiums)
- Residential property rental (long-term)
- Sale of stamps and fiscal marks at face value
- Certain intra-group financial operations
- Social welfare services
- Burial services

### 1f. Determine Expense Category [T1]
- Fixed assets: per Andorran accounting standards, useful life > 12 months
- Goods for resale: purchased for direct resale
- Raw materials: consumed in production
- Services/overheads: everything else

---

## Step 2: IGI Return Form Structure [T1]

**The IGI return (Declaracio de l'IGI) is filed quarterly via the Government electronic portal.**

### Part I -- Output IGI (Supplies)

| Box | Description | Rate |
|-----|-------------|------|
| A1 | Supplies at 4.5% -- tax base | 4.5% |
| A2 | Output IGI at 4.5% | calculated |
| A3 | Supplies at 1% -- tax base | 1% |
| A4 | Output IGI at 1% | calculated |
| A5 | Supplies at 2.5% -- tax base | 2.5% |
| A6 | Output IGI at 2.5% | calculated |
| A7 | Supplies at 9.5% -- tax base | 9.5% |
| A8 | Output IGI at 9.5% | calculated |
| A9 | Zero-rated supplies (exports) | 0% |
| A10 | Exempt supplies | - |
| A11 | Self-assessed IGI on imports of services (reverse charge) | varies |
| A12 | Output IGI on reverse charge | calculated |
| A13 | Total output IGI (A2 + A4 + A6 + A8 + A12) | sum |

### Part II -- Input IGI (Purchases)

| Box | Description |
|-----|-------------|
| B1 | Domestic purchases |
| B2 | Input IGI on domestic purchases |
| B3 | Imports of goods |
| B4 | IGI paid on imports |
| B5 | Fixed asset acquisitions |
| B6 | Input IGI on fixed assets |
| B7 | Input IGI on reverse charge (deductible) |
| B8 | Adjustments |
| B9 | Total input IGI (B2 + B4 + B6 + B7 + B8) |

### Part III -- Settlement

| Box | Description |
|-----|-------------|
| C1 | IGI payable (if A13 > B9) |
| C2 | IGI credit (if B9 > A13) |
| C3 | Credit from prior period |
| C4 | Credit for refund |
| C5 | Net IGI payable |

---

## Step 3: Reverse Charge and Import Mechanisms

### 3a. Services from Non-Residents [T1]

When an Andorran entity purchases services from a non-resident:
- If place of supply is Andorra, buyer self-assesses IGI at the applicable rate
- Report in Box A11/A12 (output) and Box B7 (input deduction)
- Net effect: zero for fully taxable businesses

### 3b. Imports of Goods [T1]

Goods imported into Andorra (primarily from Spain and France):
- IGI collected by Andorran Customs (Departament de Tributs i de Fronteres) at the border
- Rate depends on goods classification (1%, 2.5%, 4.5%, or 9.5%)
- Tax base: customs value + import duties
- Customs IGI is recoverable as input IGI
- **Important:** Andorra has land borders only with Spain and France; all goods enter through these two border crossings

### 3c. Exports [T1]

Exports of goods from Andorra:
- Zero-rated under Article 58
- Customs export declaration required
- Related input IGI fully deductible

### 3d. EU Customs Agreement [T2]

Andorra has a customs agreement with the EU (Decision 90/680/EEC):
- Covers industrial goods (HS Chapters 25-97)
- Does NOT cover agricultural products (HS Chapters 1-24)
- Industrial goods traded between Andorra and the EU benefit from reduced/zero customs duties
- Agricultural goods imported into Andorra are subject to full customs duties and IGI

**Flag for reviewer: classification of goods under the customs agreement requires specialist analysis for borderline products.**

---

## Step 4: Input IGI Deduction Rules

### 4a. General Conditions [T1]

Input IGI is deductible if:
1. Goods/services acquired for taxable operations
2. Valid invoice (factura) available
3. Goods/services recorded in accounting
4. For imports: customs documentation available

### 4b. Blocked Input IGI (Non-Deductible) [T1]

| Category | Legislation |
|----------|-------------|
| Goods/services for exempt operations | Article 60 |
| Passenger vehicles for personal use | Article 60 |
| Entertainment and hospitality expenses | Article 60 |
| Personal consumption of employees/directors | Article 60 |
| Without valid invoice | Article 59 |
| Jewelry, art, and luxury items for personal use | Article 60 |
| Tobacco products | Article 60 |

### 4c. Proportional Deduction [T2]

For mixed taxable/exempt operations:

```
Deductible % = (Taxable + Zero-rated) / Total supplies * 100
```

Annual adjustment required. Flag for reviewer.

---

## Step 5: Derived Calculations [T1]

```
Total Output IGI (A13) = A2 + A4 + A6 + A8 + A12

Total Input IGI (B9) = B2 + B4 + B6 + B7 + B8

IF A13 > B9 THEN
    C1 = A13 - B9 (IGI payable)
    C2 = 0
ELSE
    C1 = 0
    C2 = B9 - A13 (IGI credit)
END

C5 = C1 - C3
IF C5 < 0 THEN C5 = 0; excess = credit
```

---

## Step 6: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory IGI registration | Annual turnover > EUR 40,000 | Article 78 |
| Voluntary registration | Below threshold | Article 78 |
| Quarterly filing | Standard for all registrants | Article 85 |
| IGI refund | Credit accumulated for 4+ quarters | Article 66 |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| IGI return (quarterly) | Quarterly | Last day of the month following the quarter end | Article 85 |
| IGI payment | Quarterly | Last day of the month following the quarter end | Article 85 |
| Import IGI | Per import | At customs clearance | Customs law |
| Annual summary | Annual | March 31 following year | Article 85 |

**Quarter dates:**
- Q1 (Jan-Mar): filing/payment by April 30
- Q2 (Apr-Jun): filing/payment by July 31
- Q3 (Jul-Sep): filing/payment by October 31
- Q4 (Oct-Dec): filing/payment by January 31

---

## Step 8: Andorra-Specific Context [T2]

### Economy and Tax Context
- Andorra's economy is heavily tourism-dependent (skiing, duty-free shopping)
- The low IGI rate (4.5%) is part of Andorra's positioning as a low-tax jurisdiction
- Before 2013, Andorra had NO indirect tax at all
- Andorra also introduced corporate income tax (IS) in 2012 and personal income tax (IRPF) in 2015
- These reforms were part of Andorra's commitment to international tax transparency (OECD standards)

### Currency
- Andorra uses the Euro (EUR) despite not being an EU member (no formal monetary agreement until 2011, but Euro used de facto since its introduction)

### Customs Operations
- All goods enter Andorra through either the Spanish (southern) or French (northern) border
- Andorra's customs authority handles all import IGI collection
- Travelers benefit from personal allowances when exporting goods (tourism/duty-free context)

---

## Step 9: Edge Case Registry

### EC1 -- Purchase of services from Spanish provider [T1]

**Situation:** Andorran company engages a Spanish consulting firm. No Andorran registration.
**Resolution:** Reverse charge at 4.5%. Box A11 = net amount, Box A12 = IGI at 4.5%, Box B7 = deductible IGI. Net zero.

### EC2 -- Import of food products from France [T1]

**Situation:** Andorran supermarket imports food from France.
**Resolution:** Agricultural products are NOT covered by the EU customs agreement. Full customs duties apply. IGI at 1% (reduced rate for food). Import IGI = (customs value + duties) * 1%.

### EC3 -- Banking services at 9.5% [T1]

**Situation:** Andorran bank charges fees for account management.
**Resolution:** Banking services at 9.5% (increased rate). Box A7 = net, Box A8 = IGI at 9.5%. This is an unusual feature of Andorran IGI.

### EC4 -- Export of goods (duty-free retail context) [T2]

**Situation:** Andorran retailer sells goods to tourists who export them.
**Resolution:** Retail sales to tourists within Andorra are domestic supplies subject to IGI. Tourists may claim IGI refund on goods exported in their luggage, subject to minimum purchase thresholds and documentation (tax-free shopping). Flag for reviewer: verify tourist refund scheme procedures and current thresholds.

### EC5 -- Mixed taxable and exempt operations [T2]

**Situation:** An entity provides both taxable consulting (4.5%) and exempt medical services.
**Resolution:** Proportional deduction required. Direct attribution first. Mixed costs split by pro-rata formula. Flag for reviewer.

### EC6 -- Import of industrial goods from EU (customs agreement) [T1]

**Situation:** Andorran company imports machinery from Germany.
**Resolution:** Industrial goods (HS Chapters 25-97) benefit from the EU customs agreement: no customs duties. However, IGI at 4.5% still applies on import. Import IGI = customs value * 4.5%. Deductible as input IGI.

### EC7 -- Cultural event at 1% [T1]

**Situation:** Organization charges admission to a theater performance.
**Resolution:** Cultural events at 1% reduced rate. Box A3 = net, Box A4 = IGI at 1%.

### EC8 -- Real property sale [T2]

**Situation:** Company sells commercial premises.
**Resolution:** Sale of real property may be subject to IGI at 4.5% or may be subject to the Impost sobre les Transmissions Patrimonials (property transfer tax) instead. Flag for reviewer: determine which tax applies.

---

## PROHIBITIONS [T1]

- NEVER let AI guess IGI treatment -- deterministic from facts
- NEVER apply input IGI without valid invoice
- NEVER allow non-registered entities to claim input IGI
- NEVER apply 0% without customs documentation
- NEVER ignore reverse charge on non-resident services
- NEVER confuse IGI rates -- 4.5% standard, 1% reduced, 2.5% intermediate, 9.5% increased
- NEVER apply EU VAT rules to Andorra -- Andorra is NOT in the EU
- NEVER assume the EU customs agreement covers agricultural products (it does not)
- NEVER allow input IGI on entertainment, passenger vehicles, or personal items
- NEVER compute any number -- handled by deterministic engine

---

## Step 10: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

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

## Step 11: Test Suite

### Test 1 -- Standard domestic sale at 4.5%

**Input:** Andorran company sells consulting services. Net EUR 20,000. IGI at 4.5%.
**Expected output:** Box A1 = EUR 20,000. Box A2 = EUR 900.

### Test 2 -- Sale of food at 1%

**Input:** Andorran shop sells bread and milk. Net EUR 5,000. IGI at 1%.
**Expected output:** Box A3 = EUR 5,000. Box A4 = EUR 50.

### Test 3 -- Banking service at 9.5%

**Input:** Andorran bank charges account management fees. Net EUR 10,000. IGI at 9.5%.
**Expected output:** Box A7 = EUR 10,000. Box A8 = EUR 950.

### Test 4 -- Import from Spain (industrial goods)

**Input:** Import machinery from Spain. Customs value EUR 30,000. No customs duty (EU agreement).
**Expected output:** Import IGI = EUR 30,000 * 4.5% = EUR 1,350. Box B3 = EUR 30,000. Box B4 = EUR 1,350. Deductible.

### Test 5 -- Import of food from France

**Input:** Import cheese from France. Customs value EUR 8,000. Customs duty EUR 400.
**Expected output:** IGI base = EUR 8,400. Import IGI = EUR 8,400 * 1% = EUR 84. Box B3 = EUR 8,400. Box B4 = EUR 84. Deductible.

### Test 6 -- Reverse charge on Spanish services

**Input:** Andorran company engages Spanish law firm. EUR 5,000. No AD registration.
**Expected output:** Box A11 = EUR 5,000. Box A12 = EUR 225 (4.5%). Box B7 = EUR 225. Net zero.

### Test 7 -- Export of goods

**Input:** Andorran company exports products to UK. EUR 12,000. Customs declaration.
**Expected output:** Box A9 = EUR 12,000. IGI = 0%. Input IGI deductible.

### Test 8 -- Blocked entertainment

**Input:** Client dinner. Gross EUR 1,045 including IGI EUR 45.
**Expected output:** Input IGI EUR 45 NOT deductible. Blocked.

---

## Contribution Notes

This skill requires validation by a licensed Andorran tax practitioner. Key areas:

1. Current IGI rate categories (subject to legislative updates)
2. EU customs agreement product classification
3. Tourist IGI refund scheme procedures
4. Financial services IGI treatment nuances
5. Real property tax overlap (IGI vs. ITP)

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**

---

## Step 12: Penalties and Interest [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of IGI return | EUR 50-300 per return per month of delay | Law 11/2012 |
| Late payment of IGI | Interest at legal rate (currently ~3.5% annual) accruing daily | Law 11/2012 |
| Understatement of IGI | 50-150% of understated amount | Law 11/2012 |
| Failure to register | Back-assessment + EUR 300-3,000 | Law 11/2012 |
| Failure to issue invoice | EUR 150-600 per instance | Law 11/2012 |
| Repeat offenders | Enhanced penalties, potential business suspension | Law 11/2012 |

---

## Step 13: Record Keeping Requirements [T1]

IGI payers must maintain records for a minimum of 6 years:

| Record | Requirement |
|--------|-------------|
| Invoices (issued and received) | Sequential, chronological |
| Purchase and sales ledgers | Full IGI breakdowns |
| Import/export customs documents | Originals |
| IGI returns (filed copies) | With government confirmation |
| Contracts | For significant transactions |
| Bank statements | Payment trail |
| Cash register records (if B2C) | Daily summaries |

---

## Step 14: Place of Supply Rules [T1]

| Service Type | Place of Supply |
|-------------|----------------|
| B2B general services | Where recipient is established |
| B2C general services | Where supplier is established |
| Immovable property | Where property is located |
| Transport | Where transport takes place |
| Cultural/sporting events | Where event takes place |
| Restaurant/catering | Where performed |
| Electronic services (B2C) | Where recipient is established |


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
