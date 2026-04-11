---
name: georgia-vat
description: Use this skill whenever asked to prepare, review, or create a Georgia VAT return or any VAT filing for a Georgian business. Trigger on phrases like "prepare VAT return", "Georgia VAT", "RS filing", "Revenue Service Georgia", "Дღმა", or any request involving Georgia VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Georgia VAT classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Georgia VAT-related work.
---

# Georgia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Georgia |
| Jurisdiction Code | GE |
| Primary Legislation | Tax Code of Georgia (as amended) |
| Supporting Legislation | Ministerial Decrees; RS Instructions on VAT |
| Tax Authority | Revenue Service (RS), Ministry of Finance |
| Filing Portal | https://rs.ge (Revenue Service Online Portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | April 2026 (web-verified; practitioner sign-off still pending) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate, input-output mapping, return structure. Tier 2: reverse charge, free industrial zones, partial exemption. Tier 3: virtual zone IT entities, complex international structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- 9 or 11-digit Tax Identification Number
2. **VAT registration status** [T1] -- VAT registered (mandatory/voluntary) or below threshold
3. **Tax regime** [T1] -- Standard, Small Business Status, Micro Business, or Fixed Tax
4. **Filing period** [T1] -- monthly (standard for VAT payers)
5. **Industry/sector** [T2] -- impacts exemptions
6. **Does the business make exempt supplies?** [T2] -- apportionment required
7. **Does the business export goods/services?** [T1] -- zero-rating
8. **Is the entity in a Free Industrial Zone (FIZ)?** [T3] -- special rules
9. **Is the entity a Virtual Zone IT company?** [T3] -- special rules
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-4 are unknown, STOP.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, social contributions, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** Tax Code, Articles 156-160

### 1b. Determine Supply Location [T1]
- Domestic (within Georgia)
- Import (outside Georgia)
- Export (outside Georgia)
- **Legislation:** Tax Code, Articles 166-168 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 18%
- **Zero-rated:** Exports, international transport, supplies to diplomats, supplies to FIZ entities
- **Exempt (Article 168):**
  - Financial services (interest, insurance premiums)
  - Educational services (accredited institutions)
  - Medical services and pharmaceuticals (listed)
  - Residential rental (first supply)
  - Public transportation
  - Agricultural land supply
  - Government services
  - Cultural events (non-commercial)
  - Postal services (universal)
- **Legislation:** Tax Code, Article 164 (rate); Article 168 (exemptions)

### 1d. Determine Expense Category [T1]
- Capital goods: fixed assets > 1 year useful life
- Trading stock: goods for resale
- Services/overheads: rent, utilities, professional fees

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** Tax Code; RS prescribed form.

### Monthly VAT Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (TIN, name, period) |
| Part 2 | Taxable supplies at 18% |
| Part 3 | Zero-rated supplies |
| Part 4 | Exempt supplies |
| Part 5 | Total supplies |
| Part 6 | Output VAT (18% of taxable supplies) |
| Part 7 | Reverse charge VAT (on imported services) |
| Part 8 | Total output VAT |
| Part 9 | Input VAT on domestic purchases |
| Part 10 | Input VAT on imports (paid at customs) |
| Part 11 | Input VAT on reverse charge (creditable) |
| Part 12 | Total input VAT credit |
| Part 13 | Net VAT payable |
| Part 14 | Credit brought forward |
| Part 15 | Net payable or credit |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** Tax Code, Articles 174-178.

### Eligibility

1. Business must be VAT registered [T1]
2. Purchase must relate to taxable supplies [T1]
3. Valid tax invoice held [T1]
4. Supplier must be VAT registered [T1]
5. Goods/services received [T1]

### Electronic Invoicing [T1]
Georgia uses an electronic invoicing system through rs.ge:
- VAT-registered taxpayers issue invoices via the portal
- Input credit validated against the system
- Recommended: always verify invoice in RS system

### Input Tax Apportionment [T2]

```
Creditable Input VAT = Total Input VAT x (Taxable + Zero-rated Supplies / Total Supplies)
```
**Flag for reviewer: confirm apportionment.**

---

## Step 4: Deductibility Check

### Blocked Input VAT Credit [T1]

**Legislation:** Tax Code, Article 177.

These have ZERO input VAT credit:

- Motor vehicles for personal use (unless transport/rental business)
- Entertainment and hospitality expenses (representation)
- Personal consumption of owners/directors/employees
- Purchases without valid tax invoice
- Purchases from non-VAT-registered suppliers
- Goods/services for exempt supplies
- Fuel for non-commercial vehicles
- Gifts and donations (unless documented promotional)

Blocked categories OVERRIDE any other rule. Check blocked FIRST.

### Regime-Based Recovery [T1]
- VAT registered (standard): input credit allowed
- Small Business Status: NO VAT obligations (1% turnover tax)
- Micro Business: NO VAT obligations (exempt from VAT)
- Fixed Tax: NO VAT obligations

---

## Step 5: Reverse Charge [T1]

**Legislation:** Tax Code, Article 161.

### When Reverse Charge Applies
- Services received from non-resident providers
- Non-resident has no permanent establishment in Georgia
- Place of supply is Georgia

### Treatment
1. Self-assess output VAT at 18%
2. Report in Part 7 of return
3. Input credit in Part 11 if for taxable supplies
4. Net effect: zero for fully taxable businesses

---

## Step 6: VAT on Imports [T1]

**Legislation:** Tax Code, Article 162; Customs Code.

### Import VAT
- VAT payable at importation
- Calculated on: Customs Value + Customs Duty + Excise
- Rate: 18%
- Paid to Revenue Service / Customs at clearing
- Recoverable as input credit

---

## Step 7: Free Industrial Zone (FIZ) [T3]

**Legislation:** Law on Free Industrial Zones.

FIZ entities enjoy:
- VAT exemption on supplies between FIZ entities
- Zero-rating on supplies from domestic territory to FIZ
- When FIZ goods enter domestic market, import VAT applies

**Do not classify FIZ transactions without reviewing specific regulations. Escalate.**

---

## Step 8: Virtual Zone IT Companies [T3]

**Legislation:** Tax Code, Article 99(2).

Virtual Zone IT companies (registered under the Virtual Zone program) enjoy:
- Profit tax exemption on income from IT services supplied to non-residents
- VAT treatment: exports of IT services are zero-rated
- Domestic IT services: standard 18% VAT applies

**Complex determination. Escalate for confirmation of Virtual Zone status and service classification.**

---

## Step 9: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > GEL 100,000 |
| Voluntary registration | Below threshold |
| Small Business Status | Turnover < GEL 500,000 (1% turnover tax) |
| Micro Business | Income < GEL 30,000 (exempt) |

---

## Step 10: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| VAT return | Monthly | 15th of the following month |
| VAT payment | Monthly | 15th of the following month |
| Annual reconciliation | Annual | With annual profit tax return (1 April) |

### Fiscal Year [T1]
Georgia fiscal year: 1 January to 31 December (calendar year).

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | GEL 200 (first offence); GEL 400 (repeat) |
| Late payment | 0.05% per day of unpaid amount |
| Non-filing | Assessment by RS + penalties |
| Tax evasion | Criminal prosecution |
| Failure to register | GEL 500 + retrospective registration |

---

## Step 11: Derived Calculations [T1]

```
Output VAT             = Taxable supplies x 18%
Reverse Charge VAT     = Imported services x 18%
Total Output VAT       = Output VAT + Reverse Charge VAT
Total Input VAT        = Domestic + Imports + Reverse Charge (creditable)
Net VAT Payable        = Total Output - Total Input - Credit B/F
If Net < 0             = Credit carried forward or refund
```

---

## Step 12: Refund Mechanism [T2]

**Legislation:** Tax Code, Article 179.

### Refund Eligibility
- Excess input credit accumulated for 3+ consecutive months
- Exporters with persistent credit positions
- Automatic refund for "Gold List" taxpayers (low-risk, compliant)

### Process
1. Apply via rs.ge portal
2. RS may audit
3. Processing: 30-45 days (Gold List: faster)
4. Refund via bank transfer

---

## PROHIBITIONS [T1]

- NEVER allow unregistered or Small Business/Micro Business entities to claim input VAT credit
- NEVER classify exempt supplies as zero-rated
- NEVER accept input credit without valid tax invoice
- NEVER apply input credit on blocked categories
- NEVER assume FIZ or Virtual Zone treatment without verification
- NEVER file return without reconciling invoice records
- NEVER ignore reverse charge on imported services
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 13: Edge Case Registry

### EC1 -- Virtual Zone IT company domestic sales [T3]
**Situation:** Virtual Zone IT company provides services to a Georgian client.
**Resolution:** Domestic sales subject to standard 18% VAT. Only exports to non-residents benefit from profit tax exemption. VAT still applies domestically. Escalate to confirm Virtual Zone application.

### EC2 -- Reverse charge on digital services [T2]
**Situation:** Georgian company subscribes to cloud software from US provider.
**Resolution:** Reverse charge at 18%. Self-assess output VAT. Claim input credit if for taxable supplies. Flag for reviewer.

### EC3 -- FIZ to domestic supply [T1]
**Situation:** FIZ entity sells goods to a domestic (non-FIZ) buyer.
**Resolution:** Goods leaving FIZ to domestic market are treated as imports. Import VAT at 18% applies. Buyer pays import VAT, which is creditable.

### EC4 -- Credit notes [T1]
**Situation:** Price adjustment, credit note issued.
**Resolution:** Supplier reduces output VAT. Buyer reduces input credit. Both adjust in period of correction.

### EC5 -- Wine industry exemption [T2]
**Situation:** Small winery sells wine domestically.
**Resolution:** Wine is subject to standard 18% VAT. Excise tax also applies. No special VAT exemption for wine. Flag for reviewer: confirm excise rates.

### EC6 -- Construction services progress billing [T1]
**Situation:** Construction company bills in stages.
**Resolution:** VAT at 18% on each progress billing. Issue tax invoice for each stage. Input credit on materials per invoice.

### EC7 -- Tourism services [T1]
**Situation:** Tour operator provides package tours to foreign tourists.
**Resolution:** Export of services: zero-rated if tourists are non-residents and service consumed outside or during transit. Domestic tourism services to residents: 18%.

### EC8 -- Small Business Status entity crossing threshold [T2]
**Situation:** Entity on Small Business Status (1% turnover) crosses GEL 100,000 threshold.
**Resolution:** Must register for VAT. Transition from 1% turnover tax to standard 18% VAT regime. Flag for reviewer: confirm transition timing and retrospective obligations.

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
**Input:** Domestic sale, net GEL 10,000, VAT GEL 1,800. VAT registered.
**Expected output:** Part 2: GEL 10,000. Part 6: Output VAT GEL 1,800.

### Test 2 -- Local purchase with input credit
**Input:** Purchase from registered supplier, net GEL 5,000, VAT GEL 900. Valid invoice.
**Expected output:** Part 9: Input VAT GEL 900. Full credit.

### Test 3 -- Export (zero-rated)
**Input:** Export of wine, FOB GEL 50,000. Documentation complete.
**Expected output:** Part 3: GEL 50,000 at 0%. Full input credit recovery.

### Test 4 -- Import with customs VAT
**Input:** Import of materials, customs value GEL 20,000. Duty GEL 2,000. VAT at 18% on GEL 22,000 = GEL 3,960.
**Expected output:** Part 10: Input VAT GEL 3,960. Credit allowed.

### Test 5 -- Blocked input: entertainment
**Input:** Business dinner, GEL 1,000, VAT GEL 180.
**Expected output:** Input VAT GEL 0 (BLOCKED).

### Test 6 -- Reverse charge on foreign services
**Input:** Georgian company pays USD 3,000 (GEL 8,100) to UK consulting firm.
**Expected output:** Part 7: GEL 1,458 (18% output). Part 11: GEL 1,458 (input credit). Net: zero.

### Test 7 -- Small Business crossing threshold
**Input:** Entity on 1% turnover tax, annual turnover reaches GEL 110,000.
**Expected output:** Must register for VAT. Transition to 18% VAT regime. Future sales subject to VAT.

### Test 8 -- FIZ goods entering domestic market
**Input:** FIZ entity sells goods GEL 30,000 to domestic buyer.
**Expected output:** Treated as import. Buyer pays import VAT: GEL 5,400 (18%). Buyer claims input credit.

---

## Step 16: Invoice Requirements [T1]

**Legislation:** Tax Code; RS e-Invoice Regulations.

### Electronic Invoicing via rs.ge
1. All VAT-registered taxpayers issue invoices through rs.ge portal
2. Electronic invoices automatically registered in RS database
3. Input credit validated against system records
4. Paper invoices accepted but electronic strongly preferred

### Mandatory Contents
1. Supplier's name, address, TIN
2. Buyer's name and TIN
3. Date of issue
4. Invoice number (system-assigned or sequential)
5. Description of goods/services
6. Quantity and unit price
7. VAT rate (18%) and VAT amount
8. Total amount including VAT

---

## Step 17: Record Keeping [T1]

**Legislation:** Tax Code, Chapter 5.

### Mandatory Records (retain for 6 years)
1. All electronic invoices (via rs.ge)
2. Purchase and sales journals
3. Import/export documentation
4. Bank statements
5. General ledger, journals, trial balance
6. Stock records
7. Fixed asset register
8. Payroll records (separate)

---

## Step 18: Specific Sector Rules

### Wine and Spirits [T2]
- Wine production: VAT at 18% on domestic sales
- Wine export: zero-rated (significant sector for Georgia)
- Excise tax on wine: separate calculation
- Input credit on grapes, equipment, barrels allowed
- **Flag for reviewer: confirm excise rates for specific beverages**

### Tourism and Hospitality [T1]
- Hotel accommodation: VAT at 18%
- Restaurant services: VAT at 18%
- Tour packages for non-residents: zero-rated (export of services)
- Domestic tourism: VAT at 18%
- Input credit on hotel supplies allowed

### IT and Technology [T3]
- Virtual Zone IT companies: special regime
- IT service exports to non-residents: zero-rated
- Domestic IT services: VAT at 18%
- **Escalate Virtual Zone classification questions**

### Construction and Real Estate [T2]
- Construction services: VAT at 18%
- Sale of new buildings: VAT at 18%
- Sale of existing buildings: may be exempt (second-hand)
- Residential rental: exempt
- Commercial rental: VAT at 18%
- **Flag for reviewer: new vs existing building distinction**

---

## Step 19: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | GEL 500 |
| Late filing | GEL 200 (first) / GEL 400 (repeat) |
| Late payment | 0.05% per day |
| Failure to issue invoice | GEL 200 per instance |
| Fraudulent declaration | Up to 200% of understated tax |
| Failure to maintain records | GEL 200 |
| Tax evasion | Criminal prosecution |
| Under-declaration | Additional tax + penalty |

---

## Step 20: Audit and Appeals [T2]

### Audit Process
1. RS may audit within **3 years** of filing (6 years for fraud)
2. Risk-based selection
3. "Gold List" taxpayers face less frequent audits

### Appeals
1. File objection with RS within **30 days**
2. Appeal to court within **20 days** of RS decision

**Escalate any audit situation to qualified practitioner.**

---

## Contribution Notes

This skill must be validated by a qualified auditor or tax consultant practicing in Georgia before use in production.

**A skill may not be published without sign-off from a qualified practitioner in Georgia.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
