---
name: armenia-vat
description: Use this skill whenever asked to prepare, review, or create an Armenia VAT return or any VAT filing for an Armenian business. Trigger on phrases like "prepare VAT return", "Armenia VAT", "SRC filing Armenia", "ԱԱՀ", or any request involving Armenia VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Armenia VAT classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Armenia VAT-related work.
---

# Armenia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Armenia |
| Jurisdiction Code | AM |
| Primary Legislation | Tax Code of the Republic of Armenia (2016, as amended) |
| Supporting Legislation | Government Decisions on Tax Administration; EAEU VAT Agreement |
| Tax Authority | State Revenue Committee (SRC) of the Republic of Armenia |
| Filing Portal | https://www.petekamutner.am (SRC E-Filing Portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: standard rate, input-output mapping, return structure. Tier 2: EAEU trade, reverse charge, turnover tax interaction. Tier 3: free economic zones, complex group structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- 8-digit Tax Identification Number
2. **VAT registration status** [T1] -- VAT payer (mandatory/voluntary) or Turnover Tax payer
3. **Tax regime** [T1] -- General (VAT) or Turnover Tax (simplified)
4. **Filing period** [T1] -- monthly (standard for VAT payers)
5. **Industry/sector** [T2] -- impacts exemptions
6. **Does the business make exempt supplies?** [T2] -- apportionment required
7. **Does the business trade with EAEU member states?** [T1] -- Russia, Belarus, Kazakhstan, Kyrgyzstan
8. **Does the business export outside EAEU?** [T1] -- zero-rating
9. **Is the entity in a Free Economic Zone?** [T3] -- special rules
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-4 are unknown, STOP.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, social contributions, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** Tax Code, Chapter 56-60

### 1b. Determine Supply Location [T1]
- Domestic (within Armenia)
- EAEU import/export (Russia, Belarus, Kazakhstan, Kyrgyzstan)
- Non-EAEU import/export
- **Legislation:** Tax Code, Articles 37-42 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 20%
- **Zero-rated:** Exports (outside EAEU and within EAEU with confirmation), international transport
- **Exempt (Article 64):**
  - Financial services (banking, insurance)
  - Educational services (licensed institutions)
  - Medical services and equipment
  - Public transportation
  - Residential rental
  - Agricultural products (certain categories)
  - Government services
  - Religious organizations
  - Postal services (universal)
  - Supply of residential property (first sale)
- **Legislation:** Tax Code, Article 63 (rate); Article 64 (exemptions)

### 1d. Determine Expense Category [T1]
- Capital goods: fixed assets > 1 year useful life
- Trading stock: goods for resale
- Services/overheads: rent, utilities, professional fees

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** Tax Code; SRC prescribed form.

### Monthly VAT Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (TIN, name, period) |
| Part 2 | Taxable supplies at 20% |
| Part 3 | Zero-rated supplies |
| Part 4 | Exempt supplies |
| Part 5 | Total supplies |
| Part 6 | Output VAT (20% of taxable supplies) |
| Part 7 | EAEU import VAT (self-assessed) |
| Part 8 | Reverse charge VAT (non-EAEU services) |
| Part 9 | Total output VAT |
| Part 10 | Input VAT on domestic purchases |
| Part 11 | Input VAT on non-EAEU imports |
| Part 12 | Input VAT on EAEU imports (creditable) |
| Part 13 | Input VAT on reverse charge (creditable) |
| Part 14 | Total input VAT credit |
| Part 15 | Net VAT payable |
| Part 16 | Credit brought forward |
| Part 17 | Net payable or credit |

---

## Step 3: EAEU Trade Rules [T1]

**Legislation:** Treaty on the EAEU; Tax Code, Chapter 61.

### EAEU Member States
- Russia, Belarus, Kazakhstan, Kyrgyzstan

### EAEU Imports
1. No customs border -- buyer self-assesses VAT at 20%
2. Report output in Part 7 and input credit in Part 12
3. File supplementary EAEU import declaration by 20th of month following import
4. Pay self-assessed VAT by 20th of month following import
5. Net effect: zero for fully taxable businesses

### EAEU Exports
1. Zero-rated
2. Must obtain confirmation from importing country's tax authority
3. If no confirmation within 180 days, standard 20% applies retrospectively [T2]

### Non-EAEU Trade
- Imports: VAT at customs, 20%
- Exports: zero-rated with standard documentation

---

## Step 4: Input Tax Credit Mechanism [T1]

**Legislation:** Tax Code, Articles 68-74.

### Eligibility

1. Business must be VAT registered (general regime) [T1]
2. Purchase must relate to taxable supplies [T1]
3. Valid tax invoice held [T1]
4. Supplier must be VAT registered [T1]
5. Goods/services received [T1]

### Electronic Invoicing [T1]
Armenia uses electronic tax invoices via the SRC portal:
- E-invoices are the standard method
- Input credit validated against SRC database
- Paper invoices accepted but electronic preferred

### Input Tax Apportionment [T2]

```
Creditable Input VAT = Total Input VAT x (Taxable + Zero-rated / Total Supplies)
```
**Flag for reviewer: confirm apportionment.**

---

## Step 5: Deductibility Check

### Blocked Input VAT Credit [T1]

**Legislation:** Tax Code, Article 70.

These have ZERO input VAT credit:

- Motor vehicles for personal use
- Entertainment and representation expenses
- Personal consumption
- Purchases without valid tax invoice
- Purchases from non-registered or turnover tax payers
- Goods/services for exempt supplies
- Alcohol and tobacco (unless production/wholesale)
- Gifts and donations
- Fuel for non-commercial vehicles

Blocked categories OVERRIDE any other rule. Check blocked FIRST.

### Regime-Based Recovery [T1]
- General regime (VAT): input credit allowed
- Turnover tax: NO VAT charged, NO input credit
- Turnover tax rate: 10% on trade (increased from 5% effective 1 January 2025); rates vary by activity (IT/high-tech: 1%)

---

## Step 6: Reverse Charge [T1]

**Legislation:** Tax Code, Article 39.

### When Reverse Charge Applies
- Services from non-resident (non-EAEU) providers
- Non-resident has no PE in Armenia
- Place of supply is Armenia

### Treatment
1. Self-assess output VAT at 20%
2. Report in Part 8
3. Input credit in Part 13 if for taxable supplies
4. Net effect: zero for fully taxable businesses

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > AMD 115 million (~USD 290,000) |
| Voluntary registration | Below threshold |
| Turnover tax eligibility | Below VAT threshold |
| EAEU import reporting | By 20th of following month |
| EAEU export confirmation | Within 180 days |

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| VAT return | Monthly | 20th of the following month |
| VAT payment | Monthly | 20th of the following month |
| EAEU import declaration | Monthly | 20th of month following import |
| EAEU import VAT payment | Monthly | 20th of month following import |
| Annual reconciliation | Annual | With annual profit tax return |

### Fiscal Year [T1]
Armenia fiscal year: 1 January to 31 December (calendar year).

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | AMD 50,000 per return |
| Late payment | 0.04% per day (capped at 365 days) |
| Non-filing | Assessment by SRC + penalties |
| Tax evasion | Criminal prosecution |
| Failure to register | AMD 100,000 + retrospective registration |

---

## Step 9: Derived Calculations [T1]

```
Output VAT             = Domestic taxable x 20%
EAEU Import VAT        = EAEU imports x 20%
Reverse Charge VAT     = Imported services x 20%
Total Output VAT       = Output + EAEU + Reverse Charge
Total Input VAT        = Domestic + Non-EAEU imports + EAEU (creditable) + Reverse Charge (creditable)
Net VAT Payable        = Total Output - Total Input - Credit B/F
If Net < 0             = Credit carried forward or refund
```

---

## Step 10: Excise Tax Interaction [T1]

**Legislation:** Tax Code, Chapter 51 (Excise Tax).

| Category | Typical Rate |
|----------|-------------|
| Tobacco | AMD per unit (specific) |
| Alcohol / spirits | AMD per liter |
| Beer | AMD per liter |
| Fuel | AMD per liter |
| Motor vehicles (imported, luxury) | Variable |

Excise calculated BEFORE VAT. VAT at 20% on (value + excise).

---

## PROHIBITIONS [T1]

- NEVER allow turnover tax payers to claim input VAT credit or charge VAT
- NEVER classify exempt supplies as zero-rated
- NEVER accept input credit without valid tax invoice
- NEVER apply input credit on blocked categories
- NEVER treat EAEU imports like non-EAEU imports
- NEVER ignore the 180-day rule for EAEU export confirmation
- NEVER file return without reconciling records
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- EAEU export, no confirmation within 180 days [T2]
**Situation:** Goods exported to Russia, no confirmation from Russian tax authority.
**Resolution:** Zero-rating revoked. Standard 20% VAT applies retrospectively. Amend return. Flag for reviewer.

### EC2 -- Reverse charge on digital services [T2]
**Situation:** Armenian company subscribes to international SaaS.
**Resolution:** Reverse charge at 20%. Self-assess output VAT. Input credit if for taxable supplies. Flag for reviewer.

### EC3 -- Turnover tax payer receiving VAT invoice [T1]
**Situation:** Turnover tax entity receives purchase invoice with 20% VAT.
**Resolution:** Cannot claim input credit. VAT becomes part of cost. No VAT return filed.

### EC4 -- Credit notes [T1]
**Situation:** Price adjustment, credit note issued.
**Resolution:** Supplier reduces output VAT. Buyer reduces input credit. Both adjust in period of correction.

### EC5 -- IT company exports [T2]
**Situation:** Armenian IT company provides software development to US client.
**Resolution:** Export of services: zero-rated. Full input credit recovery. Documentation: contract, payment evidence, no physical presence requirement. Flag for reviewer: confirm place of supply rules.

### EC6 -- Construction services [T1]
**Situation:** Construction company bills in stages.
**Resolution:** VAT at 20% on each progress billing. Input credit on materials per invoice.

### EC7 -- Mixed EAEU and non-EAEU trade [T1]
**Situation:** Entity exports to both Russia (EAEU) and Turkey (non-EAEU).
**Resolution:** Both are zero-rated but different documentation. EAEU: Form 328 equivalent + confirmation. Non-EAEU: customs declaration + transport docs. Separate reporting in return.

### EC8 -- Donation of goods to charity [T2]
**Situation:** Company donates goods.
**Resolution:** May be treated as deemed supply with output VAT. Exception for approved charitable organizations. Flag for reviewer: confirm charitable status.

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

### Test 1 -- Standard local sale at 20%
**Input:** Domestic sale, net AMD 5,000,000, VAT AMD 1,000,000. VAT registered.
**Expected output:** Part 2: AMD 5,000,000. Part 6: Output VAT AMD 1,000,000.

### Test 2 -- Local purchase with input credit
**Input:** Purchase from registered supplier, net AMD 2,000,000, VAT AMD 400,000. Valid invoice.
**Expected output:** Part 10: Input VAT AMD 400,000. Full credit.

### Test 3 -- EAEU import (from Russia)
**Input:** Goods from Russia, value AMD 3,000,000.
**Expected output:** Part 7: AMD 600,000 (output). Part 12: AMD 600,000 (input credit). Net: zero.

### Test 4 -- Non-EAEU export (zero-rated)
**Input:** Export IT services to US client, AMD 10,000,000.
**Expected output:** Part 3: AMD 10,000,000 at 0%. Full input credit recovery.

### Test 5 -- Blocked input: entertainment
**Input:** Client entertainment, AMD 500,000, VAT AMD 100,000.
**Expected output:** Input VAT AMD 0 (BLOCKED).

### Test 6 -- Reverse charge on foreign services
**Input:** Armenian company pays EUR 2,000 (AMD 840,000) to French consulting firm.
**Expected output:** Part 8: AMD 168,000 (20% output). Part 13: AMD 168,000 (input credit). Net: zero.

### Test 7 -- Turnover tax payer
**Input:** Small shop on turnover tax, monthly sales AMD 8,000,000.
**Expected output:** Turnover tax = 10% x AMD 8,000,000 = AMD 800,000. No VAT return. No input credit.

### Test 8 -- EAEU export pending confirmation
**Input:** Export to Kazakhstan AMD 5,000,000. 170 days elapsed, no confirmation.
**Expected output:** Currently zero-rated. If no confirmation by day 180, 20% applies retrospectively = AMD 1,000,000.

---

## Step 14: Invoice Requirements [T1]

**Legislation:** Tax Code; SRC e-Invoice Regulations.

### Electronic Invoicing
1. Electronic tax invoices via SRC portal (petekamutner.am)
2. Input credit validated against SRC database
3. E-invoices increasingly mandatory for B2B transactions
4. Paper invoices accepted for certain smaller transactions

### Mandatory Contents
1. Supplier's name, address, TIN
2. Buyer's name and TIN
3. Date of issue
4. Invoice number
5. Description of goods/services
6. Quantity and unit price
7. VAT rate (20%) and VAT amount
8. Total amount including VAT

---

## Step 15: Record Keeping [T1]

**Legislation:** Tax Code, Chapter 15.

### Mandatory Records (retain for 6 years)
1. All tax invoices (electronic and paper)
2. Purchase and sales journals
3. EAEU import/export documentation
4. Non-EAEU customs declarations
5. Bank statements
6. General ledger, journals, trial balance
7. Stock records
8. Fixed asset register

---

## Step 16: Specific Sector Rules

### IT and Technology [T2]
- Software development exports: zero-rated
- Domestic IT services: VAT at 20%
- Armenia has growing IT sector with potential incentives
- **Flag for reviewer: confirm any sector-specific incentives**

### Mining [T3]
- Mining companies: standard VAT rules apply unless under special agreement
- Mineral exports: zero-rated
- Equipment imports: VAT at customs (creditable)
- **Escalate complex mining structures**

### Agriculture [T2]
- Unprocessed agricultural products: may be exempt
- Processed food: VAT at 20%
- Agricultural cooperatives may have simplified treatment
- **Flag for reviewer: verify exemption eligibility**

### Tourism and Hospitality [T1]
- Hotel accommodation: VAT at 20%
- Restaurant services: VAT at 20%
- Tour services for non-residents: zero-rated (export)
- Input credit on hotel supplies allowed

### Construction [T1]
- Construction services: VAT at 20%
- Progress billing: VAT on each milestone
- Input credit on materials allowed

---

## Step 17: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | AMD 100,000 |
| Late filing | AMD 50,000 per return |
| Late payment | 0.04% per day (max 365 days) |
| Failure to issue invoice | AMD 50,000 per instance |
| Fraudulent declaration | Up to 200% of understated tax |
| Failure to maintain records | AMD 50,000 |
| Tax evasion | Criminal prosecution |
| Under-declaration | Additional tax + penalty |
| Non-filing of EAEU declaration | AMD 50,000 + interest |

---

## Step 18: Audit and Appeals [T2]

### Audit Process
1. SRC may audit within **3 years** of filing (6 years for fraud)
2. Desk audits and field audits
3. EAEU trade triggers cross-border verification
4. Risk-based selection

### Appeals
1. File objection with SRC within **30 days**
2. Appeal to Administrative Court within **30 days**

**Escalate any audit situation to qualified practitioner.**

---

## Contribution Notes

This skill must be validated by a qualified auditor or tax consultant practicing in Armenia before use in production.

**A skill may not be published without sign-off from a qualified practitioner in Armenia.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
