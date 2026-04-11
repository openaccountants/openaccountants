---
name: kenya-vat
description: Use this skill whenever asked to prepare, review, or create a Kenya VAT return for any client. Trigger on phrases like "prepare VAT return", "Kenya VAT", "KRA return", "file VAT Kenya", "iTax", "eTIMS", "withholding VAT", or any request involving Kenyan VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Kenya VAT classification rules, return structure, withholding VAT mechanics, eTIMS requirements, deductibility rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Kenya VAT-related work.
---

# Kenya VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Kenya |
| Jurisdiction Code | KE |
| Primary Legislation | Value Added Tax Act, 2013 (No. 35 of 2013) |
| Supporting Legislation | VAT Regulations 2017; Tax Procedures Act 2015; Finance Act 2023; Finance Act 2024; Finance Act 2025; East African Community Customs Management Act |
| Tax Authority | Kenya Revenue Authority (KRA) |
| Filing Portal | https://itax.kra.go.ke (iTax) |
| Electronic Invoicing | eTIMS (electronic Tax Invoice Management System) -- mandatory |
| Standard VAT Rate | 16% |
| Currency | Kenya Shilling (KES) |
| Contributor | Open Accounting Skills Registry |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Validated By | Deep research verification, April 2026 |
| Confidence Coverage | Tier 1: classification, withholding VAT, rates, eTIMS, filing. Tier 2: partial exemption, sector-specific, cross-border. Tier 3: complex structures, rulings, appeals. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A CPA or tax advisor must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to CPA/tax advisor and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and KRA PIN** [T1] -- Kenya Revenue Authority Personal Identification Number
2. **VAT registration status** [T1] -- Registered (turnover > KES 5,000,000) or Voluntary
3. **VAT filing period** [T1] -- Monthly (all VAT-registered persons)
4. **Industry/sector** [T2] -- Impacts exempt/zero-rated classification (e.g., agriculture, manufacturing, financial services, EPZ)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial input VAT recovery restrictions apply
6. **Is the business in an Export Processing Zone (EPZ)?** [T1] -- Supplies to EPZ are zero-rated
7. **Is the client an appointed withholding VAT agent?** [T1] -- If yes, must withhold 2% of taxable value
8. **eTIMS compliance status** [T1] -- Must be connected to eTIMS for all invoicing
9. **Excess credit brought forward** [T1] -- From prior period
10. **Does the client import goods or services?** [T1] -- Impacts customs VAT and reverse charge

**Legislation:** VAT Act 2013, Sections 5-8 (registration); Tax Procedures Act 2015, Section 23A (eTIMS).

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, PAYE, NSSF, NHIF, loan repayments, dividends = OUT OF SCOPE (never on VAT return)
- **Legislation:** VAT Act 2013, Section 5 (charge of VAT); Section 2 (definitions)

### 1b. Determine Counterparty Location [T1]
- Kenya (local): supplier/customer within Kenya
- East African Community (EAC): Tanzania, Uganda, Rwanda, Burundi, South Sudan, DRC -- customs union but separate VAT systems
- International: all other countries
- **Legislation:** VAT Act 2013, Section 9 (place of supply); Second Schedule (place of supply for services)

### 1c. Determine VAT Rate [T1]
- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Standard rate: 16%
- Zero rate: 0% (with input VAT recovery)
- Exempt: no VAT charged, no input VAT recovery
- Out of scope: not a supply for VAT purposes
- **Legislation:** VAT Act 2013, Section 5(2) (rate); Second Schedule, Part A (zero-rated); First Schedule (exempt)

### 1d. eTIMS Invoice Status [T1]
- ALL tax invoices must be generated through eTIMS
- Input VAT is ONLY recoverable with a valid eTIMS-generated invoice
- Non-eTIMS invoices do not support input VAT claims
- **Legislation:** Tax Procedures Act 2015, Section 23A; Finance Act 2023

---

## Step 2: VAT Return Form Structure (iTax Form) [T1]

The Kenya VAT return (VAT 3) is filed monthly via iTax. The form captures:

### Section A: Output Tax (Sales)

| Line | Description | Notes |
|------|-------------|-------|
| A1 | Standard rated supplies (16%) | Local taxable sales |
| A2 | Zero-rated supplies (0%) | Exports, EPZ supplies, listed items |
| A3 | Exempt supplies | Per First Schedule |
| A4 | Total supplies | A1 + A2 + A3 |
| A5 | Output VAT | A1 x 16% |

### Section B: Input Tax (Purchases)

| Line | Description | Notes |
|------|-------------|-------|
| B1 | Standard rated local purchases (16%) | With valid eTIMS invoice |
| B2 | Imports of goods (customs VAT paid) | With customs entry |
| B3 | Zero-rated purchases | Zero-rated inputs |
| B4 | Exempt purchases | No VAT recovery |
| B5 | Total purchases | B1 + B2 + B3 + B4 |
| B6 | Input VAT claimable | VAT on (B1 + B2), subject to apportionment |

### Section C: Withholding VAT

| Line | Description | Notes |
|------|-------------|-------|
| C1 | VAT withheld at source by customers | 2% of taxable value withheld by appointed agents |
| C2 | Withholding VAT credit certificates | Documentary evidence |

### Section D: Net VAT

| Line | Description | Notes |
|------|-------------|-------|
| D1 | Net VAT payable | A5 - B6 - C1 |
| D2 | Credit carried forward | If D1 is negative |

**Legislation:** VAT Act 2013, Section 21 (returns); KRA iTax filing guidelines.

---

## Step 3: Supply Classification Matrix [T1]

### Zero-Rated Supplies (0% VAT, input tax recoverable) -- Second Schedule, Part A

| Category | Description | Legislation |
|----------|-------------|-------------|
| Exports of goods | Goods physically exported from Kenya | Second Schedule, Part A, Para 1 |
| Exports of taxable services | Services supplied to non-resident for use outside Kenya | Second Schedule, Part A, Para 2 |
| Supplies to EPZ enterprises | Goods and services to licensed EPZ enterprises | Second Schedule, Part A, Para 3 |
| Supplies to privileged persons | Diplomats, UN, international organizations | Second Schedule, Part A, Para 4 |
| Certain agricultural inputs | Seeds, fertilizers, pesticides (gazetted list) | Second Schedule, Part A, Para 5 |
| Taxable goods for direct/exclusive use in geothermal, oil, or mining | Machinery, equipment for extractive industries | Second Schedule, Part A, Para 6 |
| Milk and cream (unprocessed) | Fresh milk and cream | Second Schedule, Part A, Para 7 |
| Transportation of sugarcane | From farm to factory | Second Schedule, Part A, Para 8 |
| Liquefied petroleum gas (LPG) | Including accessories | Second Schedule, Part A, Para 9 |

### Exempt Supplies (no VAT, no input recovery) -- First Schedule

#### Exempt Goods (First Schedule, Part I)

| Category | Description | Legislation |
|----------|-------------|-------------|
| Unprocessed food | Maize, wheat, rice, beans, vegetables, fruits (unprocessed) | First Schedule, Part I, Para 1 |
| Agricultural products (raw) | Unprocessed tea, coffee, raw hides/skins | First Schedule, Part I, Para 2 |
| Pharmaceuticals and medical supplies | Medicines, medical instruments, first aid kits | First Schedule, Part I, Para 3 |
| Sanitary towels and diapers | Feminine hygiene and baby products | First Schedule, Part I, Para 4 |
| Educational materials | Exercise books, textbooks, newspapers | First Schedule, Part I, Para 5 |
| Postage stamps | Kenya Post Corporation stamps | First Schedule, Part I, Para 6 |
| Currency and securities | Banknotes, coins, securities (not goods for collection) | First Schedule, Part I, Para 7 |
| Passenger baggage and personal effects | On entry to Kenya | First Schedule, Part I, Para 8 |

#### Exempt Services (First Schedule, Part II)

| Category | Description | Legislation |
|----------|-------------|-------------|
| Financial services | Banking, insurance (margin-based), securities trading | First Schedule, Part II, Para 1 |
| Educational services | Licensed educational institutions (primary, secondary, tertiary) | First Schedule, Part II, Para 2 |
| Medical and dental services | Registered health practitioners, hospitals, clinics | First Schedule, Part II, Para 3 |
| Residential rent | Rent on residential property used for dwelling | First Schedule, Part II, Para 4 |
| Transportation of passengers | Public service vehicles (PSV), railway passenger transport | First Schedule, Part II, Para 5 |
| Burial and cremation services | Funeral services | First Schedule, Part II, Para 6 |
| Social welfare services | Charitable, religious, welfare organizations | First Schedule, Part II, Para 7 |
| Transfer of business as going concern | TOGC | First Schedule, Part II, Para 8 |

### Out of Scope

| Category | Notes |
|----------|-------|
| Salaries, wages, PAYE | Employment, not a supply |
| NSSF/NHIF contributions | Statutory deductions |
| Dividends | Return on investment |
| Loan repayments (principal) | Financial transaction |
| Government fines/levies | Sovereign functions |

**Legislation:** VAT Act 2013, First Schedule (exempt), Second Schedule (zero-rated).

---

## Step 4: Withholding VAT Mechanism [T1]

### What is Withholding VAT?

Appointed withholding VAT agents deduct 2% of the taxable value (NOT 2% of the VAT) from payments to suppliers and remit it to KRA on behalf of the supplier.

**Key distinction:** In Kenya, withholding VAT is 2% of the TAXABLE VALUE (the net amount before VAT), NOT 2% of the VAT itself.

### Who Must Withhold VAT? [T1]

| Agent Category | Description | Legislation |
|----------------|-------------|-------------|
| Government ministries, departments, agencies | National and county government bodies | KRA Gazette Notice |
| Appointed large taxpayers | As designated by Commissioner via Gazette Notice | Tax Procedures Act 2015, Section 16A |
| Specific companies | As individually gazetted by KRA | KRA Gazette Notices |

### How Withholding VAT Works [T1]

1. Supplier issues eTIMS invoice including 16% VAT
2. Appointed agent calculates 2% of the taxable value (net amount)
3. Agent deducts the 2% from the VAT portion of the payment
4. Agent remits the 2% to KRA by 20th of following month
5. Agent issues withholding VAT certificate to supplier
6. Supplier claims the withheld amount as credit on their VAT return (Section C1)

### Example [T1]

```
Invoice:
  Taxable value (net):              KES 100,000
  VAT at 16%:                       KES  16,000
  Gross:                            KES 116,000

Withholding:
  2% of taxable value:              KES   2,000
  Agent pays supplier:              KES 114,000
  Agent remits to KRA:              KES   2,000

Supplier's VAT return:
  Output VAT (A5):                  KES  16,000
  Withholding VAT credit (C1):      KES   2,000
  Net output after withholding:     KES  14,000
```

### Important Rules [T1]

- Withholding is 2% of the TAXABLE VALUE, not 2% of the VAT amount
- The full 16% VAT is still shown on the invoice
- The supplier claims the withheld amount as a credit
- The agent must issue a withholding VAT certificate within 10 working days

**Legislation:** VAT Act 2013, Section 17A (withholding VAT); Tax Procedures Act 2015, Section 16A; KRA Gazette Notices.

---

## Step 5: eTIMS (Electronic Tax Invoice Management System) [T1]

### Mandatory Requirements

| Requirement | Detail | Legislation |
|-------------|--------|-------------|
| Who must comply | ALL VAT-registered persons and any person issued a PIN | Finance Act 2023; Tax Procedures Act, Section 23A |
| When effective | Phased rollout from August 2023; fully mandatory from January 2024 | KRA Notice |
| What it covers | ALL sales invoices, credit notes, debit notes | Section 23A |
| Connection options | eTIMS Lite (mobile), eTIMS Online (web), eTIMS Integration (ERP/API) | KRA eTIMS guidelines |
| Invoice validation | Each invoice gets a unique QR code and control unit number from KRA | Section 23A |

### Impact on Input VAT Recovery [T1]

| Invoice Type | Input VAT Recovery |
|--------------|-------------------|
| eTIMS-generated invoice with valid QR code | Yes -- input VAT recoverable |
| Non-eTIMS invoice (supplier not on eTIMS) | No -- input VAT NOT recoverable |
| eTIMS-generated but buyer's PIN not captured | May be challenged by KRA on audit |
| Credit note via eTIMS | Adjusts original invoice; recovery adjusted accordingly |

### Penalties for Non-Compliance [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Not issuing eTIMS invoice | KES 1,000,000 or imprisonment up to 3 years or both | Tax Procedures Act, Section 86 |
| Issuing invoice not through eTIMS | Equal to the tax evaded + criminal penalty | Section 86 |
| Tampering with eTIMS data | Criminal offence | Section 86 |

**Legislation:** Tax Procedures Act 2015, Section 23A; Finance Act 2023.

---

## Step 6: Reverse Charge on Imported Services [T1]

### When Reverse Charge Applies

A Kenyan VAT-registered business that receives taxable services from a non-resident supplier must account for VAT at 16% on the value of the services (reverse charge / self-accounting).

**Legislation:** VAT Act 2013, Section 10 (imported services); Section 5(4).

### Reverse Charge Steps

1. Determine the value of services received from the non-resident
2. Convert to KES at the exchange rate on the date of supply
3. Calculate VAT at 16%
4. Report as output VAT in Section A5
5. If used for taxable supplies, claim as input VAT in Section B6
6. Net effect: zero for fully taxable businesses

### Exceptions [T1]
- Out-of-scope categories: NEVER reverse charge
- Services consumed outside Kenya: no Kenya VAT
- Non-resident supplier registered for VAT in Kenya: supplier charges directly
- Exempt services from non-residents: no VAT (e.g., financial services margin)

### Digital Services Tax / VAT on Digital Marketplace [T2]

Non-resident digital service providers supplying to Kenyan consumers must register for VAT in Kenya and charge 16% VAT. This applies to:
- App stores, streaming services, online advertising
- Cloud/SaaS services to consumers
- Digital marketplace operators

**Flag for reviewer:** Enforcement of non-resident digital VAT registration is evolving. Confirm current KRA compliance status.

**Legislation:** VAT Act 2013, Section 5(7) (digital marketplace supplies); Finance Act 2020.

---

## Step 7: Input Tax Recovery Rules

### General Rule [T1]

Input VAT is recoverable if the purchase is used to make taxable supplies (standard-rated or zero-rated) AND supported by a valid eTIMS invoice.

**Legislation:** VAT Act 2013, Section 17 (input tax deduction).

### Conditions for Recovery [T1]

| Condition | Detail | Legislation |
|-----------|--------|-------------|
| Valid eTIMS invoice | Must have QR code and control unit number | Section 17(2); Section 23A |
| Business purpose | Must be for making taxable supplies | Section 17(1) |
| Within claim period | Must be claimed within 6 months of invoice date | Section 17(5) |
| Not blocked | Must not be on the blocked list | Third Schedule |

### Blocked Input Tax (Third Schedule) [T1]

The following categories have ZERO VAT recovery:

| Category | Description | Legislation |
|----------|-------------|-------------|
| Entertainment | Hospitality, entertainment of non-employees | Third Schedule, Para 1 |
| Motor vehicles (passenger) | Private motor vehicles with seating capacity < 13 | Third Schedule, Para 2 |
| Fuel for blocked vehicles | Fuel for private passenger vehicles | Third Schedule, Para 2 |
| Club subscriptions | Social, sporting, recreational club memberships | Third Schedule, Para 3 |

### Motor Vehicle Exceptions [T2]

Input VAT on motor vehicles IS recoverable if:
- Vehicle is stock in trade (car dealer)
- Vehicle used exclusively for taxable business (taxi, tour operator, driving school)
- Vehicle used for hire/rental business
- Minibus with capacity of 13+ passengers

**Flag for reviewer:** Must confirm exclusive business use.

### Partial Exemption (Mixed Supplies) [T2]

If a business makes both taxable and exempt supplies:
```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```

The Finance Act 2024 removed the previous 90:10 rule (which allowed full recovery if taxable supplies were 90%+). Now proportional apportionment applies regardless of ratio.

**Flag for reviewer:** Pro-rata must be confirmed by CPA. Annual adjustment may be required.

**Legislation:** VAT Act 2013, Section 17(6) (apportionment); Finance Act 2024 amendments.

---

## Step 8: VAT Rates Summary Table [T1]

| Rate | Application | Input Recovery |
|------|-------------|----------------|
| 16% (standard) | All taxable supplies not zero-rated or exempt | Yes (with eTIMS invoice) |
| 0% (zero-rated) | Exports, EPZ supplies, certain agricultural inputs, LPG, milk | Yes |
| Exempt | Unprocessed food, medical, education, financial, residential rent, transport | No |
| Out of scope | Salaries, NSSF/NHIF, dividends, government fines | N/A |

**Legislation:** VAT Act 2013, Sections 5, First Schedule, Second Schedule.

---

## Step 9: Registration Thresholds [T1]

| Threshold | Amount | Legislation |
|-----------|--------|-------------|
| Mandatory registration | KES 5,000,000 (taxable supplies in 12 months or expected next 12 months) | VAT Act 2013, Section 5(1) |
| Voluntary registration | Below KES 5,000,000 but making taxable supplies | Section 5(3) |
| Non-resident registration | Must register if making taxable supplies in Kenya (especially digital services) | Section 5(7) |
| Deregistration | Taxable turnover falls below KES 5,000,000; or cessation of business | Section 8 |
| Turnover calculation | Excludes capital asset sales | Section 5(2) |

**Legislation:** VAT Act 2013, Sections 5-8.

---

## Step 10: Filing Deadlines and Penalties [T1]

### Filing Frequency

| Requirement | Detail |
|-------------|--------|
| Filing period | Monthly (all VAT-registered persons) |
| Filing deadline | 20th day of the month following the tax period |
| Payment deadline | Same as filing deadline (20th of following month) |
| Filing method | Electronic via iTax portal |
| Nil returns | Must file even if no transactions (nil return) |

### Monthly Calendar

| Tax Period | Filing/Payment Deadline |
|------------|------------------------|
| January | 20 February |
| February | 20 March |
| March | 20 April |
| April | 20 May |
| May | 20 June |
| June | 20 July |
| July | 20 August |
| August | 20 September |
| September | 20 October |
| October | 20 November |
| November | 20 December |
| December | 20 January |

### Penalties

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing | KES 10,000 or 5% of tax due, whichever is higher, per month | Tax Procedures Act, Section 83 |
| Late payment | 1% per month of the unpaid tax (simple interest) | Tax Procedures Act, Section 89 |
| Late payment interest | 1% per month on outstanding tax | Section 89 |
| Failure to register | KES 100,000 or imprisonment up to 2 years or both | Section 85 |
| Failure to issue eTIMS invoice | KES 1,000,000 or imprisonment up to 3 years or both | Section 86 |
| Incorrect return (negligence) | 75% of tax underpaid | Section 83(5) |
| Incorrect return (fraud) | 200% of tax evaded + criminal prosecution | Section 97 |
| Failure to keep records | KES 100,000 per year of default | Section 84 |

**Legislation:** Tax Procedures Act 2015, Sections 83-97.

---

## Step 11: Tax Invoice Requirements (via eTIMS) [T1]

All tax invoices must be generated through eTIMS. The following fields are mandatory:

| Field | Requirement | Legislation |
|-------|-------------|-------------|
| eTIMS QR code | System-generated unique identifier | Section 23A |
| eTIMS control unit number | Unique device/connection identifier | Section 23A |
| Supplier name, PIN | As registered with KRA | VAT Act, Section 15 |
| Customer name, PIN | For B2B (mandatory for input claims) | Section 15 |
| Invoice number | Sequential via eTIMS | Section 15 |
| Date of invoice | Date generated | Section 15 |
| Description of goods/services | Sufficient detail | Section 15 |
| Quantity and unit price | For goods | Section 15 |
| VAT rate | 16%, 0%, or Exempt | Section 15 |
| VAT amount | In KES | Section 15 |
| Total amount | Inclusive of VAT | Section 15 |
| HSN/tax code | Harmonized System Nomenclature code for goods | eTIMS requirement |

**Legislation:** VAT Act 2013, Section 15; Tax Procedures Act 2015, Section 23A.

---

## Step 12: Specific Sector Rules

### Agriculture [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Unprocessed agricultural produce | Exempt | First Schedule, Part I |
| Processed food (packaged, branded) | Standard rated (16%) | Section 5 |
| Agricultural inputs (seeds, fertilizer, pesticides) | Zero-rated (gazetted list) | Second Schedule, Part A |
| Agricultural equipment | Standard rated (16%) unless gazetted | Section 5 |
| Flowers for export | Zero-rated (export) | Second Schedule, Part A |
| Tea for domestic consumption | Exempt (Finance Act 2024) | First Schedule amendment |

### Financial Services [T2]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Interest income (margin-based) | Exempt | First Schedule, Part II, Para 1 |
| Bank fees and commissions (explicit) | Standard rated (16%) | Section 5 |
| Insurance premiums (general) | Exempt | First Schedule, Part II, Para 1 |
| Insurance brokerage fees | Standard rated (16%) | Section 5 |
| Securities trading | Exempt | First Schedule, Part II, Para 1 |
| Mobile money transfer fees (Mpesa) | Exempt (financial services) | First Schedule, Part II, Para 1 |

**Flag for reviewer:** Classification of fintech and mobile money services is evolving. Confirm current KRA position.

### Manufacturing [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Manufactured goods | Standard rated (16%) | Section 5 |
| Exports of manufactured goods | Zero-rated | Second Schedule, Part A |
| Supplies to EPZ enterprises | Zero-rated | Second Schedule, Part A, Para 3 |
| Raw materials (imported) | Standard rated (16%) at customs | Section 5 |

### Real Estate [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Commercial property (sale) | Standard rated (16%) | Section 5 |
| Commercial rent | Standard rated (16%) | Section 5 |
| Residential rent | Exempt | First Schedule, Part II, Para 4 |
| Construction services | Standard rated (16%) | Section 5 |
| Sale of residential property | Standard rated (16%) | Section 5 |

### Tourism and Hospitality [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Hotel accommodation | Standard rated (16%) | Section 5 |
| Tour operations | Standard rated (16%) | Section 5 |
| Restaurant/catering | Standard rated (16%) | Section 5 |
| Park/conservancy fees | Standard rated (16%) | Section 5 |

### Digital Economy [T2]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Digital marketplace supplies (B2C to Kenya) | Standard rated (16%) -- non-resident must register | Section 5(7) |
| SaaS/cloud services (B2B) | Reverse charge at 16% | Section 10 |
| Online advertising | Standard rated (16%) | Section 5 |
| E-commerce sales of physical goods | Standard rated (16%) | Section 5 |

---

## Step 13: Record Keeping Requirements [T1]

| Requirement | Detail | Legislation |
|-------------|--------|-------------|
| Retention period | 5 years from end of tax period | Tax Procedures Act, Section 23 |
| Language | English or Kiswahili | Section 23 |
| Format | Paper or electronic; eTIMS records stored centrally by KRA | Section 23 |
| Records required | eTIMS invoices, credit notes, import entries, bank statements, accounting records | Section 23 |
| Backup | eTIMS records stored by KRA serve as backup; but maintain own copies | KRA guidance |

**Legislation:** Tax Procedures Act 2015, Section 23.

---

## Step 14: Derived Calculations [T1]

```
A4 = A1 + A2 + A3
A5 = A1 * 16%
B5 = B1 + B2 + B3 + B4
B6 = (B1 + B2) * 16%, subject to apportionment and blocked list
D1 = A5 - B6 - C1

IF D1 > 0 THEN
  VAT payable = D1
ELSE
  Credit carried forward = |D1|
  (May apply for refund per Section 17(4))
END
```

**Legislation:** VAT Act 2013, Section 21.

---

## Step 15: Refund Mechanism [T1]

| Scenario | Treatment | Legislation |
|----------|-----------|-------------|
| Excess input VAT | Carry forward (default) or request refund after 12 months (reduced from 24 months by Finance Act 2025) | VAT Act, Section 17(4); Finance Act 2025 |
| Refund processing | KRA has 90 days from application | Tax Procedures Act, Section 47 |
| Exporters | May apply for refund each period if export sales > 50% | Section 17(4)(b) |
| Diplomatic refunds | Direct refund on application | Section 18 |
| Refund offset | Refund may be offset against other VAT liabilities (Finance Act 2025) | Finance Act 2025 amendment |

**Legislation:** VAT Act 2013, Section 17(4); Tax Procedures Act 2015, Section 47; Finance Act 2025.

---

## Step 16: Capital Goods and Adjustments [T2]

Kenya does not have a formal multi-year capital goods scheme comparable to the EU. However:

- Input VAT on capital assets is claimed in full at time of purchase
- If the asset is subsequently used for exempt supplies, an adjustment may be required
- If a VAT-registered person deregisters, output VAT is due on capital assets still held

**Flag for reviewer:** Confirm treatment of capital assets with CPA when use changes.

**Legislation:** VAT Act 2013, Sections 17 and 12 (deemed supply on deregistration).

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT classification -- it is deterministic from the legislation
- NEVER allow input VAT recovery without a valid eTIMS invoice
- NEVER charge VAT on exempt supplies (unprocessed food, medical, education, residential rent)
- NEVER apply reverse charge to out-of-scope categories (salaries, NSSF, dividends)
- NEVER confuse zero-rated (input VAT recoverable) with exempt (input VAT NOT recoverable)
- NEVER apply input tax recovery on blocked categories (entertainment, private motor vehicles, club subscriptions)
- NEVER ignore withholding VAT obligations if the client is an appointed agent
- NEVER confuse withholding VAT rate (2% of taxable value) with VAT rate (16%)
- NEVER file a return without accounting for VAT withheld at source (Section C1)
- NEVER apply the old 90:10 apportionment rule (removed by Finance Act 2024)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER accept a non-eTIMS invoice for input VAT recovery purposes
- NEVER overlook the 6-month time limit for claiming input VAT
- NEVER classify Mpesa/mobile money transfer fees as taxable (they are exempt financial services)

---

## Step 17: Edge Case Registry

### EC1 -- Non-eTIMS supplier invoice [T1]
**Situation:** Client receives invoice from a supplier who is not connected to eTIMS. Invoice has no QR code.
**Resolution:** Input VAT is NOT recoverable. The expense is recorded gross (inclusive of any purported VAT). Client should request the supplier to connect to eTIMS and re-issue. No VAT claim until valid eTIMS invoice is received.
**Legislation:** Tax Procedures Act 2015, Section 23A.

### EC2 -- Withholding VAT calculation [T1]
**Situation:** Appointed agent pays supplier KES 500,000 + KES 80,000 VAT = KES 580,000.
**Resolution:** Withholding = 2% x KES 500,000 (taxable value) = KES 10,000. Agent pays supplier KES 570,000 (KES 580,000 - KES 10,000). Agent remits KES 10,000 to KRA.
**Legislation:** VAT Act 2013, Section 17A.

### EC3 -- Export of flowers (zero-rated) [T1]
**Situation:** Flower farm exports roses to Netherlands. Invoice KES 2,000,000.
**Resolution:** Zero-rated. Report in A2. Must have customs export declaration, airway bill, and phytosanitary certificate. Input VAT on farm inputs is recoverable.
**Legislation:** VAT Act 2013, Second Schedule, Part A.

### EC4 -- Residential vs. commercial rent [T1]
**Situation:** Landlord rents property to a business. The property is a converted house used as an office.
**Resolution:** If the property is used for commercial purposes (office), the rent is standard rated at 16% regardless of the building's original design. Residential rent exemption applies only to property used as a dwelling.
**Legislation:** VAT Act 2013, First Schedule, Part II, Para 4.

### EC5 -- Mpesa transaction charges [T1]
**Situation:** Client pays Mpesa transfer fees of KES 50 per transaction.
**Resolution:** Mpesa fees are exempt financial services (mobile money transfer). No VAT is charged on the fee. No input VAT to claim.
**Legislation:** First Schedule, Part II, Para 1 (financial services exemption).

### EC6 -- Import of services from non-resident [T1]
**Situation:** Kenyan company receives legal services from a UK law firm. Invoice GBP 5,000.
**Resolution:** Reverse charge. Convert to KES. Self-assess 16% output VAT and claim input VAT (if used for taxable supplies). Net effect zero. Must have documentation of the service and proof of payment.
**Legislation:** VAT Act 2013, Section 10.

### EC7 -- Supply to EPZ enterprise [T1]
**Situation:** Local supplier sells raw materials to an EPZ-licensed manufacturer.
**Resolution:** Zero-rated. Must obtain EPZ certificate from the buyer. Report in A2. Input VAT on the supplier's purchases is recoverable.
**Legislation:** Second Schedule, Part A, Para 3.

### EC8 -- Motor vehicle for tour operator [T2]
**Situation:** Safari tour company buys a Land Cruiser for game drives. KES 12,000,000 + KES 1,920,000 VAT.
**Resolution:** Input VAT MAY be recoverable if the vehicle is used exclusively for licensed tour operations. Flag for reviewer: confirm exclusive business use and vehicle registration as commercial/tourism.
**Legislation:** Third Schedule (exception for tourism vehicles).

### EC9 -- Credit note via eTIMS [T1]
**Situation:** Client issues credit note for KES 200,000 + KES 32,000 VAT on a previous sale.
**Resolution:** Credit note MUST be issued through eTIMS, referencing the original eTIMS invoice. Reduces A1 by KES 200,000 and A5 by KES 32,000.
**Legislation:** Tax Procedures Act 2015, Section 23A; VAT Act 2013, Section 16.

### EC10 -- Late input VAT claim (> 6 months) [T1]
**Situation:** Client discovers an eTIMS invoice from 8 months ago with unclaimed input VAT.
**Resolution:** Input VAT CANNOT be claimed. The 6-month time limit has expired. The VAT is an irrecoverable cost.
**Legislation:** VAT Act 2013, Section 17(5).

### EC11 -- Transfer of business as going concern (TOGC) [T1]
**Situation:** Client sells their entire business to another VAT-registered person.
**Resolution:** Exempt supply (TOGC). No output VAT charged. Report in A3. No clawback of input VAT previously claimed on the business assets (provided buyer continues taxable activity).
**Legislation:** First Schedule, Part II, Para 8.

### EC12 -- VAT on imported goods at port [T1]
**Situation:** Company imports machinery from China through Mombasa port. Customs assesses 16% VAT.
**Resolution:** VAT paid at customs is recoverable input tax. Report in B2. Retain the customs entry (Form C63) and payment receipt.
**Legislation:** VAT Act 2013, Section 17(1)(b).

### EC13 -- Tea for domestic consumption [T1]
**Situation:** Tea packer sells processed tea (branded tea bags) for local market.
**Resolution:** Exempt (as of Finance Act 2024 amendment). No output VAT. Input VAT on processing costs NOT recoverable.
**Legislation:** First Schedule amendment by Finance Act 2024.

---

## Step 18: EU VAT Comparison [T1]

| Feature | Kenya | EU (Directive 2006/112/EC) |
|---------|-------|---------------------------|
| Standard rate | 16% | 15-27% (varies) |
| Registration threshold | KES 5,000,000 (~EUR 35,000) | Varies (EUR 0 to EUR 85,000) |
| Reverse charge (import of services) | Yes (Section 10) | Yes (Article 196) |
| Withholding VAT | Yes (2% of taxable value) | Rare |
| Electronic invoicing | Mandatory (eTIMS) | Varies (mandatory in some states) |
| Filing frequency | Monthly | Varies |
| Cash vs. accrual basis | Accrual (invoice basis) | Varies |
| Capital goods adjustment | No formal scheme | Yes (5/10/20 years) |
| Bad debt relief | Not formally provided | Yes (varies) |
| Group registration | Not formally provided | Yes (Article 11) |
| Tourist refund scheme | No | Yes (Article 170) |
| Input claim time limit | 6 months | Varies (usually 3-4 years) |
| Zero-rated basic food | No (exempt instead) | Some states (0% or reduced) |
| Digital services (non-resident) | Must register | OSS/IOSS system |

---

## Step 19: Test Suite

### Test 1 -- Standard local sale, 16% VAT
**Input:** Kenyan company sells IT services to local client. Net KES 500,000. VAT KES 80,000. eTIMS invoice issued.
**Expected output:** A1 = KES 500,000. A5 = KES 80,000.

### Test 2 -- Withholding VAT by government agency
**Input:** Company sells office furniture to county government. Net KES 1,000,000. VAT KES 160,000. Government is appointed withholding agent.
**Expected output:** A1 = KES 1,000,000. A5 = KES 160,000. C1 = KES 20,000 (2% of KES 1,000,000). Net from customer = KES 1,140,000.

### Test 3 -- Export of goods (zero-rated)
**Input:** Company exports coffee to Germany. Invoice KES 3,000,000. Export documentation complete.
**Expected output:** A2 = KES 3,000,000. A5 = KES 0. Input VAT on related purchases recoverable.

### Test 4 -- Exempt supply: residential rent
**Input:** Landlord receives KES 150,000/month residential rent.
**Expected output:** A3 = KES 150,000. No output VAT. Input VAT on property maintenance NOT recoverable.

### Test 5 -- Non-eTIMS invoice: blocked input
**Input:** Client receives invoice for KES 50,000 + KES 8,000 VAT from supplier not on eTIMS.
**Expected output:** B1 = KES 50,000. B6 does NOT include KES 8,000. Input VAT NOT recoverable (no eTIMS).

### Test 6 -- Reverse charge on imported services
**Input:** Kenyan company receives cloud hosting from AWS (US). USD 2,000 (~KES 310,000). No Kenya VAT on invoice.
**Expected output:** Output VAT = KES 49,600 (16%) in A5. Input VAT = KES 49,600 in B6. Net = zero.

### Test 7 -- Blocked motor vehicle
**Input:** Company buys sedan for MD. KES 4,000,000 + KES 640,000 VAT. eTIMS invoice received.
**Expected output:** B1 = KES 4,000,000. B6 does NOT include KES 640,000. VAT BLOCKED (private vehicle).

### Test 8 -- Supply to EPZ (zero-rated)
**Input:** Local supplier sells raw materials to EPZ enterprise. KES 2,000,000. EPZ certificate obtained.
**Expected output:** A2 = KES 2,000,000. A5 = KES 0. Zero-rated.

### Test 9 -- Late filing penalty
**Input:** Monthly return for February 2026 due 20 March 2026. Filed 25 March 2026. Tax payable KES 200,000.
**Expected output:** Late filing penalty: higher of KES 10,000 or 5% x KES 200,000 = KES 10,000. Late payment: 1% x KES 200,000 = KES 2,000. Total penalty = KES 12,000.

### Test 10 -- Partial exemption (mixed supplies)
**Input:** Company makes 75% taxable, 25% exempt supplies. Office rent KES 300,000 + KES 48,000 VAT. eTIMS invoice.
**Expected output:** B1 = KES 300,000. B6 includes KES 36,000 (75% of KES 48,000). Recovery restricted.

### Test 11 -- Expired input VAT claim
**Input:** Client finds eTIMS invoice from 7 months ago. Input VAT KES 15,000 unclaimed.
**Expected output:** Input VAT NOT recoverable. 6-month time limit expired. Record as irrecoverable cost.

### Test 12 -- Credit note via eTIMS
**Input:** Client issues credit note for KES 100,000 + KES 16,000 VAT via eTIMS.
**Expected output:** A1 reduced by KES 100,000. A5 reduced by KES 16,000. Credit note references original eTIMS invoice.

### Test 13 -- Unprocessed food (exempt)
**Input:** Supermarket buys raw vegetables from farmer. KES 200,000. No VAT charged.
**Expected output:** B4 = KES 200,000. Exempt. No VAT.

---

## Step 20: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: CPA or tax advisor must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to CPA or tax advisor. Document gap.
```

---

## Contribution Notes

If you are adapting this skill for another jurisdiction, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all return line items with your jurisdiction's VAT return structure.
3. Replace VAT rates with your jurisdiction's rates.
4. Replace the exempt/zero-rated lists with your jurisdiction's lists.
5. Replace the withholding VAT mechanism if applicable.
6. Replace eTIMS requirements with your jurisdiction's electronic invoicing requirements (if any).
7. Have a CPA in your jurisdiction validate every T1 rule before publishing.
8. Add your own edge cases for known ambiguous situations.
9. Run all test suite cases against your jurisdiction's rules.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
