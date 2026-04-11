---
name: azerbaijan-vat
description: Use this skill whenever asked to prepare, review, or create an Azerbaijan VAT return or any VAT filing for an Azerbaijani business. Trigger on phrases like "prepare VAT return", "Azerbaijan VAT", "STM filing", "ƏDV", or any request involving Azerbaijan VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Azerbaijan VAT classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Azerbaijan VAT-related work.
---

# Azerbaijan VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Azerbaijan |
| Jurisdiction Code | AZ |
| Primary Legislation | Tax Code of the Republic of Azerbaijan (2000, as amended) |
| Supporting Legislation | Cabinet of Ministers Decisions; State Tax Service Instructions |
| Tax Authority | State Tax Service under the Ministry of Economy (STM) |
| Filing Portal | https://www.taxes.gov.az (E-taxes portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: standard rate, input-output mapping, return structure. Tier 2: reverse charge, oil/gas sector, simplified tax. Tier 3: PSA contractors, complex international structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN (VOEN)** [T1] -- Tax Identification Number (10-digit)
2. **VAT registration status** [T1] -- VAT registered (mandatory/voluntary) or below threshold
3. **Tax regime** [T1] -- General (VAT) or Simplified Tax
4. **Filing period** [T1] -- monthly (standard for VAT payers)
5. **Industry/sector** [T2] -- impacts exemptions (oil/gas, agriculture)
6. **Does the business make exempt supplies?** [T2] -- apportionment required
7. **Does the business export goods/services?** [T1] -- zero-rating
8. **Is the entity a PSA (Production Sharing Agreement) contractor?** [T3] -- special rules
9. **Is the entity in a Free Economic Zone?** [T3] -- special rules
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-4 are unknown, STOP.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, social insurance, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** Tax Code, Articles 153-159

### 1b. Determine Supply Location [T1]
- Domestic (within Azerbaijan)
- Import (outside Azerbaijan)
- Export (outside Azerbaijan)
- **Legislation:** Tax Code, Articles 168-169 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 18%
- **Zero-rated:** Exports, international transport, supplies to diplomats
- **Exempt (Article 164):**
  - Financial services (banking, insurance)
  - Educational services (state-accredited)
  - Medical services and pharmaceuticals (listed)
  - Public transportation
  - Residential rental
  - Agricultural products (unprocessed, with conditions)
  - Government services
  - Postal services (universal)
  - Religious activities
  - Import of certain goods per Presidential decree
- **Legislation:** Tax Code, Article 163 (rate); Article 164 (exemptions)

### 1d. Determine Expense Category [T1]
- Capital goods: fixed assets > 1 year useful life
- Trading stock: goods for resale
- Services/overheads: rent, utilities, professional fees

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** Tax Code; STM prescribed form.

### Monthly VAT Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (VOEN, name, period) |
| Part 2 | Taxable supplies at 18% |
| Part 3 | Zero-rated supplies |
| Part 4 | Exempt supplies |
| Part 5 | Total supplies |
| Part 6 | Output VAT (18% of taxable supplies) |
| Part 7 | Reverse charge VAT (imported services) |
| Part 8 | Total output VAT |
| Part 9 | Input VAT on domestic purchases |
| Part 10 | Input VAT on imports |
| Part 11 | Input VAT on reverse charge (creditable) |
| Part 12 | Total input VAT credit |
| Part 13 | Net VAT payable |
| Part 14 | Credit brought forward |
| Part 15 | Net payable or credit |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** Tax Code, Articles 175-179.

### Eligibility

1. Business must be VAT registered [T1]
2. Purchase must relate to taxable supplies [T1]
3. Valid electronic tax invoice (E-invoice) held [T1]
4. Supplier must be VAT registered [T1]
5. Goods/services received [T1]

### E-Invoice System [T1]

Azerbaijan uses mandatory electronic invoicing:
- All VAT-registered taxpayers issue E-invoices via taxes.gov.az
- Input credit validated against E-invoice database
- No E-invoice = No input credit

### Input Tax Apportionment [T2]

```
Creditable Input VAT = Total Input VAT x (Taxable + Zero-rated / Total Supplies)
```
**Flag for reviewer: confirm apportionment.**

---

## Step 4: Deductibility Check

### Blocked Input VAT Credit [T1]

**Legislation:** Tax Code, Article 175.

These have ZERO input VAT credit:

- Motor vehicles for personal use (unless transport/rental business)
- Entertainment and representation expenses
- Personal consumption of owners/directors/employees
- Purchases without valid E-invoice
- Purchases from non-VAT-registered or simplified tax payers
- Goods/services for exempt supplies
- Alcohol and tobacco (unless production/wholesale)
- Gifts and donations
- Fuel for non-commercial vehicles

Blocked categories OVERRIDE any other rule. Check blocked FIRST.

### Regime-Based Recovery [T1]
- General regime (VAT registered): input credit allowed
- Simplified tax: NO VAT charged, NO input credit
- Simplified tax rate: 2% (Baku), 4% (regions) on gross revenue

---

## Step 5: Reverse Charge [T1]

**Legislation:** Tax Code, Article 169.

### When Reverse Charge Applies
- Services from non-resident providers
- Non-resident has no permanent establishment in Azerbaijan
- Place of supply is Azerbaijan

### Treatment
1. Self-assess output VAT at 18%
2. Report in Part 7
3. Input credit in Part 11 if for taxable supplies
4. Withhold and remit VAT to tax authority

---

## Step 6: VAT on Imports [T1]

**Legislation:** Tax Code, Article 171; Customs Code.

### Import VAT
- VAT payable at importation
- Calculated on: Customs Value + Customs Duty + Excise
- Rate: 18%
- Paid to State Customs Committee
- Recoverable as input credit

---

## Step 7: Oil and Gas Sector [T3]

**Legislation:** Tax Code, Part XII; individual PSAs.

PSA (Production Sharing Agreement) contractors:
- May be exempt from VAT under PSA terms
- Subcontractors may have different VAT treatment
- Foreign employees under PSA may have different obligations

**Do not classify PSA-related transactions. Escalate.**

---

## Step 8: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > AZN 200,000 |
| Voluntary registration | Below threshold |
| Simplified tax eligibility | Below VAT threshold |
| E-invoice mandatory | All VAT-registered taxpayers |

---

## Step 9: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| VAT return | Monthly | 20th of the following month |
| VAT payment | Monthly | 20th of the following month |
| Annual reconciliation | Annual | With annual profit tax return (31 March) |

### Fiscal Year [T1]
Azerbaijan fiscal year: 1 January to 31 December (calendar year).

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | AZN 200 (first offence); AZN 500 (repeat) |
| Late payment | 0.05% per day of unpaid amount |
| Non-filing | Assessment by STM + penalties |
| Tax evasion | Criminal prosecution |
| Failure to register | AZN 1,000 + retrospective registration |

---

## Step 10: Derived Calculations [T1]

```
Output VAT             = Domestic taxable x 18%
Reverse Charge VAT     = Imported services x 18%
Total Output VAT       = Output + Reverse Charge
Total Input VAT        = Domestic + Imports + Reverse Charge (creditable)
Net VAT Payable        = Total Output - Total Input - Credit B/F
If Net < 0             = Credit carried forward or refund
```

---

## Step 11: Excise Tax Interaction [T1]

**Legislation:** Tax Code, Chapter 10 (Excise Tax).

| Category | Typical Rate |
|----------|-------------|
| Tobacco / cigarettes | AZN per 1000 units |
| Alcohol / spirits | AZN per liter |
| Beer | AZN per liter |
| Petroleum products | AZN per ton |
| Motor vehicles (imported, luxury) | 10% - 20% |

Excise calculated BEFORE VAT. VAT at 18% on (value + excise).

---

## Step 12: Refund Mechanism [T2]

**Legislation:** Tax Code, Article 179.

### Refund Eligibility
- Excess credits accumulated for 3+ months
- Exporters with persistent credit positions
- Entities ceasing business

### Process
1. Apply via taxes.gov.az
2. Tax audit likely
3. Processing: 45 days (may take longer)

---

## PROHIBITIONS [T1]

- NEVER allow simplified tax entities to claim input VAT credit or charge VAT
- NEVER classify exempt supplies as zero-rated
- NEVER accept input credit without valid E-invoice
- NEVER apply input credit on blocked categories
- NEVER classify PSA contractor transactions without specialist review
- NEVER file return without reconciling E-invoice records
- NEVER ignore reverse charge on imported services
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 13: Edge Case Registry

### EC1 -- PSA subcontractor VAT [T3]
**Situation:** Subcontractor provides services to a PSA contractor.
**Resolution:** May be VAT exempt under PSA terms. Do not classify. Escalate to review specific PSA.

### EC2 -- Reverse charge on digital services [T2]
**Situation:** Azerbaijani company subscribes to cloud software from US provider.
**Resolution:** Reverse charge at 18%. Self-assess output VAT. Input credit if for taxable supplies. Flag for reviewer.

### EC3 -- Simplified tax entity selling to VAT entity [T1]
**Situation:** Simplified tax supplier sells goods to VAT-registered buyer.
**Resolution:** No VAT on the invoice (simplified tax entity does not charge VAT). Buyer gets no input credit. Full cost as expense for buyer.

### EC4 -- Credit notes [T1]
**Situation:** Price adjustment, credit note issued.
**Resolution:** Supplier reduces output VAT. Buyer reduces input credit. Both adjust in period of correction via corrective E-invoice.

### EC5 -- Agricultural producer exemption [T2]
**Situation:** Farmer sells unprocessed agricultural products.
**Resolution:** May be exempt under Article 164. If voluntarily VAT registered, standard rules apply. Flag for reviewer.

### EC6 -- Import for re-export (temporary import) [T2]
**Situation:** Goods imported temporarily for exhibition, then re-exported.
**Resolution:** May qualify for customs suspension/temporary import regime with no VAT. If goods remain, full import VAT applies. Flag for reviewer.

### EC7 -- Construction services [T1]
**Situation:** Construction company bills in stages.
**Resolution:** VAT at 18% on each billing. Input credit on materials per E-invoice.

### EC8 -- Foreign currency transactions [T1]
**Situation:** Invoice in USD or EUR.
**Resolution:** Convert to AZN at Central Bank rate on date of supply. All VAT in AZN.

---

## Step 14: Reviewer Escalation Protocol

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

## Step 15: Test Suite

### Test 1 -- Standard local sale at 18%
**Input:** Domestic sale, net AZN 50,000, VAT AZN 9,000. VAT registered.
**Expected output:** Part 2: AZN 50,000. Part 6: Output VAT AZN 9,000.

### Test 2 -- Local purchase with input credit
**Input:** Purchase from registered supplier, net AZN 20,000, VAT AZN 3,600. Valid E-invoice.
**Expected output:** Part 9: Input VAT AZN 3,600. Full credit.

### Test 3 -- Export (zero-rated)
**Input:** Export of petrochemicals, FOB AZN 200,000. Documentation complete.
**Expected output:** Part 3: AZN 200,000 at 0%. Full input credit recovery.

### Test 4 -- Import with customs VAT
**Input:** Import of equipment, customs value AZN 100,000. Duty AZN 15,000. VAT at 18% on AZN 115,000 = AZN 20,700.
**Expected output:** Part 10: Input VAT AZN 20,700. Credit allowed.

### Test 5 -- Blocked input: entertainment
**Input:** Client entertainment, AZN 2,000, VAT AZN 360.
**Expected output:** Input VAT AZN 0 (BLOCKED).

### Test 6 -- Reverse charge on foreign services
**Input:** Azerbaijani company pays GBP 5,000 (AZN 10,000) to UK consulting firm.
**Expected output:** Part 7: AZN 1,800 (18% output). Part 11: AZN 1,800 (input credit). Net: zero.

### Test 7 -- Simplified tax entity
**Input:** Small retailer in Baku, simplified tax, monthly revenue AZN 30,000.
**Expected output:** Simplified tax = 2% x AZN 30,000 = AZN 600. No VAT return. No input credit.

### Test 8 -- No E-invoice
**Input:** Purchase AZN 10,000, VAT AZN 1,800. No E-invoice issued.
**Expected output:** Input VAT AZN 0. No credit without E-invoice.

---

## Step 16: Invoice Requirements [T1]

**Legislation:** Tax Code; E-Invoice Regulations.

### E-Invoice System Details
1. Mandatory electronic invoicing via taxes.gov.az
2. All VAT-registered entities must issue E-invoices
3. Input credit validated against E-invoice database
4. Corrective E-invoices for adjustments
5. No E-invoice = No input credit (strictly enforced)

### Mandatory Contents
1. Supplier's name, address, VOEN (TIN)
2. Buyer's name and VOEN
3. Date of issue
4. E-invoice number (system-generated)
5. Description of goods/services
6. Quantity and unit price
7. VAT rate (18%) and VAT amount
8. Total amount including VAT
9. Electronic signature

---

## Step 17: Record Keeping [T1]

**Legislation:** Tax Code, Chapter 3.

### Mandatory Records (retain for 5 years)
1. All E-invoice records (digital)
2. Purchase and sales journals
3. Import/export documentation
4. Bank statements
5. General ledger, journals, trial balance
6. Stock records
7. Fixed asset register
8. Payroll records (separate)
9. PSA-related documentation (if applicable)

---

## Step 18: Specific Sector Rules

### Oil and Gas [T3]
- PSA contractors: special VAT regime per agreement
- Subcontractors: may be VAT exempt under PSA umbrella
- Equipment imports: potential duty/VAT relief under PSA
- **Always escalate oil/gas questions**

### Agriculture [T2]
- Unprocessed agricultural products: may be exempt
- Processed food: VAT at 18%
- Agricultural equipment: VAT at 18% (input credit allowed)
- **Flag for reviewer: verify exemption eligibility**

### Construction [T1]
- Construction services: VAT at 18%
- Progress billing: VAT on each stage
- Input credit on materials per E-invoice

### Tourism and Hospitality [T1]
- Hotel accommodation: VAT at 18%
- Restaurant services: VAT at 18%
- Tour services for non-residents: may be zero-rated (export)
- Input credit on hotel supplies allowed

### IT and Technology [T2]
- IT services: VAT at 18%
- Software exports: zero-rated
- IT Park entities may have incentives
- **Flag for reviewer: confirm IT Park status**

---

## Step 19: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | AZN 1,000 |
| Late filing | AZN 200 (first) / AZN 500 (repeat) |
| Late payment | 0.05% per day |
| Failure to issue E-invoice | AZN 500 per instance |
| Fraudulent declaration | Up to 200% of understated tax |
| Failure to maintain records | AZN 500 |
| Tax evasion | Criminal prosecution |
| Under-declaration | Additional tax + penalty |
| Non-compliance with E-invoice | AZN 200 per instance |

---

## Step 20: Audit and Appeals [T2]

### Audit Process
1. STM may audit within **3 years** of filing (6 years for fraud)
2. Desk audits and field audits
3. E-invoice data analytics for risk-based selection
4. PSA entities: audited per agreement terms

### Appeals
1. File objection with STM within **30 days**
2. Appeal to court within **20 days** of STM decision

**Escalate any audit situation to qualified practitioner.**

---

## Contribution Notes

This skill must be validated by a qualified auditor or tax consultant practicing in Azerbaijan before use in production.

**A skill may not be published without sign-off from a qualified practitioner in Azerbaijan.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
