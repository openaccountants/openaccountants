---
name: uzbekistan-vat
description: Use this skill whenever asked to prepare, review, or create an Uzbekistan VAT return or any VAT filing for an Uzbek business. Trigger on phrases like "prepare VAT return", "Uzbekistan VAT", "STC filing", "soliq.uz", "НДС Узбекистан", or any request involving Uzbekistan VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Uzbekistan VAT classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Uzbekistan VAT-related work.
---

# Uzbekistan VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Uzbekistan |
| Jurisdiction Code | UZ |
| Primary Legislation | Tax Code of the Republic of Uzbekistan (2020, as amended) |
| Supporting Legislation | Presidential Decrees; Cabinet of Ministers Resolutions on Tax Administration |
| Tax Authority | State Tax Committee (STC) / Davlat soliq qo'mitasi |
| Filing Portal | https://my.soliq.uz (Taxpayer Cabinet) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: standard rate, input-output mapping, return structure. Tier 2: simplified tax regime interaction, free economic zones. Tier 3: transfer pricing, subsoil use, complex holding structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN (INN)** [T1] -- 9-digit Tax Identification Number
2. **VAT registration status** [T1] -- VAT payer (mandatory/voluntary) or Turnover Tax payer
3. **Tax regime** [T1] -- General regime (VAT applicable) or Simplified (turnover tax, no VAT)
4. **Filing period** [T1] -- monthly (standard for VAT payers)
5. **Industry/sector** [T2] -- impacts exemptions
6. **Does the business make exempt supplies?** [T2] -- apportionment required
7. **Does the business import/export goods?** [T1] -- customs VAT / zero-rating
8. **Is the entity in a Free Economic Zone (FEZ)?** [T3] -- special rules
9. **Does the business trade with CIS countries?** [T1] -- impacts import/export treatment
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-4 are unknown, STOP.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, social contributions, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** Tax Code, Chapter 35-39

### 1b. Determine Supply Location [T1]
- Domestic (within Uzbekistan)
- Import (goods/services from outside Uzbekistan)
- Export (goods/services to outside Uzbekistan)
- **Legislation:** Tax Code, Articles 241-245 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 12%
- **Zero-rated:** Exports of goods and services, international transport
- **Exempt (Article 244):**
  - Financial services (banking, insurance)
  - Educational services (licensed institutions)
  - Medical services and pharmaceutical products (listed)
  - Public transportation
  - Residential rental
  - Agricultural products (certain categories)
  - Government services
  - Burial/funeral services
  - Cultural and sports events
  - Goods imported for humanitarian aid
- **Legislation:** Tax Code, Article 258 (rate); Article 244 (exemptions)

### 1d. Determine Expense Category [T1]
- Capital goods: fixed assets > 1 year useful life
- Trading stock: goods for resale
- Services/overheads: rent, utilities, professional fees

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** Tax Code; STC prescribed form.

### VAT Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (TIN, name, period) |
| Part 2 | Taxable turnover at 12% |
| Part 3 | Zero-rated turnover (exports) |
| Part 4 | Exempt turnover |
| Part 5 | Total turnover |
| Part 6 | Output VAT (12% of taxable turnover) |
| Part 7 | Input VAT on domestic purchases |
| Part 8 | Input VAT on imports (paid at customs) |
| Part 9 | Total input VAT credit |
| Part 10 | Net VAT payable |
| Part 11 | Credit brought forward |
| Part 12 | Net payable or credit carried forward |
| Part 13 | Adjustments (credit/debit notes) |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** Tax Code, Articles 266-273.

### Eligibility

1. Business must be on general tax regime (VAT payer) [T1]
2. Purchase must relate to taxable supplies [T1]
3. Valid electronic tax invoice (E-faktura) held [T1]
4. Supplier must be VAT registered [T1]
5. Goods/services received [T1]

### E-Faktura System [T1]

Uzbekistan uses mandatory electronic invoicing (E-faktura) through factura.uz:
- All VAT payers must issue E-faktura for each taxable supply
- Input credit only valid with confirmed E-faktura
- No E-faktura = No input credit
- E-faktura must be issued within 10 days of supply

### Input Tax Apportionment [T2]

```
Creditable Input VAT = Total Input VAT x (Taxable Turnover / Total Turnover)
```
**Flag for reviewer: confirm apportionment.**

---

## Step 4: Deductibility Check

### Blocked Input VAT Credit [T1]

**Legislation:** Tax Code, Article 268.

These have ZERO input VAT credit:

- Motor vehicles for personal use
- Entertainment expenses
- Personal consumption
- Purchases without valid E-faktura
- Purchases from non-VAT-registered suppliers or turnover tax payers
- Goods/services for exempt supplies
- Alcohol and tobacco (unless production/wholesale)
- Gifts and donations
- Representation expenses beyond statutory limits

Blocked categories OVERRIDE any other rule. Check blocked FIRST.

### Regime-Based Recovery [T1]
- General regime (VAT payer): input credit allowed
- Simplified regime (turnover tax): NO input credit, NO VAT charged on sales
- Turnover tax rate: 4% (most activities)

---

## Step 5: VAT on Imports [T1]

**Legislation:** Tax Code, Article 259; Customs Code.

### Import VAT
- VAT payable at importation
- Calculated on: Customs Value + Customs Duty + Excise (if applicable)
- Rate: 12%
- Paid to State Customs Committee at time of clearing
- Recoverable as input credit if for taxable supplies

### CIS Country Imports
- Similar to standard imports but may have simplified customs procedures
- VAT still applies at 12% on import value

---

## Step 6: Excise Tax Interaction [T1]

**Legislation:** Tax Code, Chapter 40 (Excise Tax).

| Category | Typical Rate |
|----------|-------------|
| Tobacco products | Specific rates per unit |
| Alcohol / spirits | Specific rates per liter |
| Beer | Specific rates per liter |
| Petroleum products | Specific rates per ton |
| Motor vehicles | 5% - 30% (depending on engine) |

Excise calculated BEFORE VAT. VAT at 12% applies on (value + excise).

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > UZS 1 billion (~USD 80,000) |
| Voluntary registration | Below threshold but may register |
| Turnover tax (simplified) | Below VAT threshold or voluntary choice for eligible entities |
| E-faktura mandatory | All VAT payers |

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| VAT return | Monthly (standard); Quarterly for certain taxpayers | By the 20th of the month following the reporting period |
| VAT payment | Same as return | Same deadline as return |
| Annual reconciliation | Annual | With annual tax return |
| E-faktura issuance | Per transaction | Within 10 days of supply |

### Fiscal Year [T1]
Uzbekistan fiscal year: 1 January to 31 December (calendar year).

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | 1% of tax per day (max 10%) |
| Late payment | 0.04% per day of unpaid amount (refinancing rate-based) |
| Non-filing | Assessment by STC + penalties |
| Failure to issue E-faktura | Administrative fine |
| Tax evasion | Criminal prosecution |

---

## Step 9: Derived Calculations [T1]

```
Output VAT             = Taxable turnover x 12%
Total Input VAT        = Domestic input VAT + Import VAT
Net VAT Payable        = Output VAT - Total Input VAT - Credit B/F
If Net < 0             = Credit carried forward or refund
Total Payable          = Net VAT + Penalties (if any)
```

---

## Step 10: Reverse Charge on Imported Services [T1]

**Legislation:** Tax Code, Article 243.

### When Reverse Charge Applies
- Services from non-resident providers
- Non-resident has no permanent establishment in Uzbekistan
- Place of supply is Uzbekistan

### Treatment
1. Self-assess output VAT at 12%
2. Withhold and remit VAT on behalf of non-resident
3. Input credit allowed if service relates to taxable supplies

---

## PROHIBITIONS [T1]

- NEVER allow turnover tax payers to claim input VAT credit or charge VAT
- NEVER classify exempt supplies as zero-rated
- NEVER accept input credit without valid E-faktura
- NEVER apply input credit on blocked categories
- NEVER confuse general regime (VAT) with simplified regime (turnover tax)
- NEVER file return without reconciling E-faktura records
- NEVER ignore excise when calculating VAT base
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- Turnover tax payer receives invoice with VAT [T1]
**Situation:** Entity on simplified (turnover tax) regime receives an invoice with 12% VAT charged.
**Resolution:** Turnover tax payer cannot claim input credit. VAT charged becomes part of the cost. No VAT return filed. Only turnover tax return.

### EC2 -- Reverse charge on digital services [T2]
**Situation:** Uzbek company subscribes to international SaaS platform.
**Resolution:** Reverse charge at 12%. Self-assess and remit. Input credit if for taxable supplies. Non-resident may also have separate registration obligation. Flag for reviewer.

### EC3 -- Free Economic Zone entity [T3]
**Situation:** Entity operates in a Free Economic Zone (FEZ).
**Resolution:** FEZ entities may have VAT exemptions on certain operations. Rules vary by FEZ. Escalate to review the specific FEZ decree.

### EC4 -- Credit notes / E-faktura corrections [T1]
**Situation:** Price adjustment after original supply.
**Resolution:** Issue corrective E-faktura through factura.uz. Adjust output/input VAT in the period of correction. Report in Part 13.

### EC5 -- Agricultural producer VAT treatment [T2]
**Situation:** Agricultural enterprise sells unprocessed products.
**Resolution:** May qualify for exemption. However, if voluntarily VAT registered, standard rules apply. Flag for reviewer: evaluate exemption vs. registration benefit.

### EC6 -- Construction contract progress billing [T1]
**Situation:** Construction company bills client in stages.
**Resolution:** VAT at 12% on each progress billing. Issue E-faktura for each billing. Input credit on materials and subcontractors per E-faktura.

### EC7 -- Multi-currency transactions [T1]
**Situation:** Invoice in USD.
**Resolution:** Convert to UZS at Central Bank rate on date of supply. All VAT in UZS.

### EC8 -- Donation of goods [T1]
**Situation:** Company donates goods to charity.
**Resolution:** Deemed supply for VAT purposes. Output VAT due on fair market value. Input credit on donated goods may be reversed. Exception: donations to approved institutions per Presidential decree.

---

## Step 12: Reviewer Escalation Protocol

When a [T2] situation is identified:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list possible treatments]
Recommended: [most likely correct]
Action Required: Qualified accountant must confirm before filing.
```

When a [T3] situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Refer to qualified accountant. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard local sale at 12%
**Input:** Domestic sale, net UZS 100,000,000, VAT UZS 12,000,000. General regime.
**Expected output:** Part 2: UZS 100,000,000. Part 6: Output VAT UZS 12,000,000.

### Test 2 -- Local purchase with input credit
**Input:** Purchase from VAT-registered supplier, net UZS 50,000,000, VAT UZS 6,000,000. Valid E-faktura.
**Expected output:** Part 7: Input VAT UZS 6,000,000. Full credit.

### Test 3 -- Import with customs VAT
**Input:** Import of equipment, customs value UZS 200,000,000. Duty UZS 20,000,000. VAT at 12% on UZS 220,000,000 = UZS 26,400,000.
**Expected output:** Part 8: Input VAT UZS 26,400,000. Credit allowed.

### Test 4 -- Export (zero-rated)
**Input:** Export of cotton yarn, FOB UZS 500,000,000. Documentation complete.
**Expected output:** Part 3: UZS 500,000,000 at 0%. Full input credit recovery.

### Test 5 -- Blocked input: entertainment
**Input:** Client dinner, UZS 5,000,000, VAT UZS 600,000.
**Expected output:** Input VAT UZS 0 (BLOCKED).

### Test 6 -- Turnover tax payer, no VAT
**Input:** Small shop on simplified regime, monthly turnover UZS 80,000,000.
**Expected output:** Turnover tax = 4% x UZS 80,000,000 = UZS 3,200,000. No VAT return. No input credit.

### Test 7 -- Reverse charge on foreign services
**Input:** Uzbek company pays USD 10,000 (UZS 128,000,000) to Russian IT firm.
**Expected output:** Self-assess output VAT: UZS 15,360,000 (12%). Input credit: UZS 15,360,000 (if taxable). Net: zero.

### Test 8 -- No E-faktura
**Input:** Purchase UZS 30,000,000, VAT UZS 3,600,000. No E-faktura issued.
**Expected output:** Input VAT UZS 0. No credit.

---

## Step 14: Invoice Requirements [T1]

**Legislation:** Tax Code; E-faktura Regulations.

### E-Faktura System Details
1. Mandatory for all VAT payers via factura.uz
2. E-faktura must be issued within 10 days of supply
3. Buyer confirms receipt electronically
4. Input credit only valid with confirmed E-faktura
5. Corrective E-faktura for adjustments

### Mandatory Contents
1. Supplier's name, address, TIN (INN)
2. Buyer's name and TIN
3. Date of issue
4. E-faktura number (system-generated)
5. Description of goods/services with TNVED code
6. Quantity and unit price
7. VAT rate (12%) and VAT amount
8. Total amount including VAT
9. Digital signature

---

## Step 15: Record Keeping [T1]

**Legislation:** Tax Code, Chapter 12.

### Mandatory Records (retain for 5 years)
1. All E-faktura records (digital, via factura.uz)
2. Purchase and sales journals
3. Import/export documentation
4. Bank statements and payment records
5. General ledger, journals, trial balance
6. Stock/inventory records
7. Fixed asset register
8. Payroll records (separate)
9. CIS trade documentation (if applicable)

---

## Step 16: Specific Sector Rules

### Cotton and Textile [T1]
- Raw cotton: may be exempt at farm level
- Cotton processing: VAT at 12%
- Textile export: zero-rated
- Input credit on processing machinery allowed

### Construction [T1]
- Construction services: VAT at 12%
- Progress billing: VAT on each milestone
- Input credit on materials per E-faktura

### Agriculture [T2]
- Agricultural producers may qualify for exemption
- Unprocessed products: often exempt
- Processed agricultural products: VAT at 12%
- **Flag for reviewer: verify exemption eligibility**

### IT and Digital Services [T2]
- IT companies may have incentives under IT Park regime
- Software development exports: zero-rated
- Domestic IT services: VAT at 12%
- **Flag for reviewer: confirm IT Park status**

---

## Step 17: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | Fine + retrospective registration |
| Late filing | 1% per day of tax (max 10%) |
| Late payment | 0.04% per day |
| Failure to issue E-faktura | Administrative fine per STC |
| Fraudulent declaration | Up to 200% of understated tax |
| Failure to maintain records | Administrative fine |
| Tax evasion | Criminal prosecution |
| Under-declaration | Additional tax + 50% penalty |

---

## Step 18: Audit and Appeals [T2]

### Audit Process
1. STC may audit within **5 years** of filing
2. Desk audits and field audits
3. Risk-based selection using E-faktura analytics
4. E-faktura mismatches trigger automatic flags

### Appeals
1. File objection with STC within **30 days**
2. Appeal to court within **30 days** of STC decision

**Escalate any audit situation to qualified practitioner.**

---

## Step 19: Currency and Reporting [T1]

- All VAT returns filed in UZS (Uzbekistani som)
- Foreign currency transactions: Central Bank of Uzbekistan rate on date of supply
- Import transactions: customs exchange rate at date of declaration
- Dual-currency contracts: convert each billing to UZS

---

## Step 20: Transitional Rules for Regime Changes [T2]

**Legislation:** Tax Code, transitional provisions.

### Turnover Tax to VAT Transition
- When entity crosses the VAT threshold, must register within 10 days
- Transition date: first day of month following threshold breach
- Inventory on hand at transition: VAT applies on subsequent sale
- No input credit on pre-transition purchases
- **Flag for reviewer: confirm transition timing and inventory treatment**

### VAT to Turnover Tax Transition
- If turnover drops below threshold, entity may apply to deregister
- Must reverse input credit on unsold inventory and capital goods
- STC approval required for deregistration

---

## Contribution Notes

This skill must be validated by a qualified auditor or tax consultant practicing in Uzbekistan before use in production.

**A skill may not be published without sign-off from a qualified practitioner in Uzbekistan.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
