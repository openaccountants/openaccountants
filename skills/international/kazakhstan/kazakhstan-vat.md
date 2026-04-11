---
name: kazakhstan-vat
description: Use this skill whenever asked to prepare, review, or create a Kazakhstan VAT return (Form 300.00) or any VAT filing for a Kazakh business. Trigger on phrases like "prepare VAT return", "Kazakhstan VAT", "SRC filing", "KGD filing", "Form 300", "НДС", or any request involving Kazakhstan VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Kazakhstan VAT classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Kazakhstan VAT-related work.
---

# Kazakhstan VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Kazakhstan |
| Jurisdiction Code | KZ |
| Primary Legislation | Tax Code of the Republic of Kazakhstan (Code No. 120-VI, 2017, as amended) |
| Supporting Legislation | Rules on VAT Administration; EAEU VAT Agreement |
| Tax Authority | State Revenue Committee (SRC) / KGD under Ministry of Finance |
| Filing Portal | https://cabinet.salyk.kz (Taxpayer's Cabinet) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: standard rate, input-output mapping, Form 300.00 structure. Tier 2: EAEU supplies, special zones, agricultural exemptions. Tier 3: transfer pricing, subsoil use contracts, complex group structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and BIN/IIN** [T1] -- Business Identification Number (12-digit)
2. **VAT registration status** [T1] -- Registered (mandatory or voluntary) or below threshold
3. **Filing period** [T1] -- quarterly (standard)
4. **Industry/sector** [T2] -- impacts exemptions (agriculture, education, healthcare)
5. **Does the business make exempt supplies?** [T2] -- apportionment required
6. **Does the business trade with EAEU member states?** [T1] -- Russia, Belarus, Armenia, Kyrgyzstan
7. **Does the business export outside EAEU?** [T1] -- zero-rating
8. **Is the entity in a Special Economic Zone (SEZ)?** [T3] -- special rules
9. **Is the entity a subsoil user?** [T3] -- special regime
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-3 are unknown, STOP.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, social contributions, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** Tax Code, Articles 369-372

### 1b. Determine Supply Location [T1]
- Domestic (within Kazakhstan)
- EAEU import/export (Russia, Belarus, Armenia, Kyrgyzstan)
- Non-EAEU import/export (rest of world)
- **Legislation:** Tax Code, Articles 378-382 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 12%
- **Zero-rated:** Exports (outside EAEU), international transport, certain financial services
- **Exempt (Article 394):**
  - Financial services (banking, insurance)
  - Educational services (licensed institutions)
  - Medical services
  - Public transportation
  - Residential rental
  - Sale of residential property
  - Agricultural products (certain types)
  - Government services
  - Cultural and sports events (non-commercial)
- **Legislation:** Tax Code, Article 422 (rate); Article 394 (exemptions)

### 1d. Determine Expense Category [T1]
- Capital goods: fixed assets > 1 year useful life
- Trading stock: goods for resale
- Services/overheads: rent, utilities, professional fees

---

## Step 2: Form 300.00 Structure [T1]

**Legislation:** Tax Code; SRC-prescribed Form 300.00.

### VAT Return (Form 300.00) Sections

| Line | Description |
|------|-------------|
| 300.00.001 | Taxable turnover (standard rate 12%) |
| 300.00.002 | Zero-rated turnover (exports) |
| 300.00.003 | Exempt turnover |
| 300.00.004 | Total turnover |
| 300.00.005 | Output VAT (12% on line 001) |
| 300.00.006 | VAT on imports from EAEU (self-assessed) |
| 300.00.007 | Total output VAT (005 + 006) |
| 300.00.008 | Input VAT on domestic purchases |
| 300.00.009 | Input VAT on non-EAEU imports (paid at customs) |
| 300.00.010 | Input VAT on EAEU imports (self-assessed, creditable) |
| 300.00.011 | Total input VAT credit |
| 300.00.012 | Net VAT (output minus input) |
| 300.00.013 | Credit brought forward |
| 300.00.014 | Net payable or credit |

### Appendices to Form 300.00

| Appendix | Purpose |
|----------|---------|
| 300.01 | Domestic sales detail |
| 300.02 | Domestic purchases detail |
| 300.03 | Exports detail |
| 300.04 | Imports from non-EAEU |
| 300.05 | EAEU trade detail |
| 300.06 | Adjustments |

---

## Step 3: EAEU Trade Rules [T1]

**Legislation:** Treaty on the Eurasian Economic Union; Tax Code, Articles 441-456.

### EAEU Member States
- Russia
- Belarus
- Armenia
- Kyrgyzstan

### EAEU Imports (goods from EAEU countries)
1. NO customs declaration required (no customs border within EAEU)
2. Buyer self-assesses VAT at 12% on the import value
3. Report in Form 300.00 line 006 (output) and line 010 (input credit)
4. File supplementary Form 328.00 (statement on imported goods) by 20th of month following import
5. Pay self-assessed VAT by 20th of month following import
6. Net effect: zero for fully taxable businesses

### EAEU Exports
1. Zero-rated (0%) -- no output VAT
2. Must file Form 328.00 with confirmation from importing country's tax authority
3. Full input credit recovery on related purchases
4. If confirmation not received within 180 days, standard 12% applies retrospectively [T2]

### Non-EAEU Imports
- VAT paid at customs (standard import procedure)
- Calculated on: Customs Value + Customs Duty
- Rate: 12%
- Recoverable as input credit

### Non-EAEU Exports
- Zero-rated
- Standard export documentation required

---

## Step 4: Input Tax Credit Mechanism [T1]

**Legislation:** Tax Code, Articles 400-411.

### Eligibility

1. Business must be VAT registered [T1]
2. Purchase must relate to taxable supplies [T1]
3. Valid tax invoice (ESF -- electronic счет-фактура) held [T1]
4. Supplier must be VAT registered [T1]
5. ESF must be issued within 15 calendar days of supply [T1]

### Electronic Invoice (ESF) System [T1]

Kazakhstan uses a mandatory electronic invoice system (ESF -- Электронный счет-фактура):
- All VAT-registered taxpayers must issue ESF for each taxable supply
- ESF is issued through the IS ESF portal (esf.gov.kz)
- Input credit is only valid with a confirmed ESF
- No ESF = No input credit

### Input Tax Apportionment [T2]

If making both taxable and exempt supplies:
```
Creditable Input VAT = Total Input VAT x (Taxable Turnover / Total Turnover)
```
**Flag for reviewer: confirm apportionment.**

---

## Step 5: Deductibility Check

### Blocked Input VAT Credit [T1]

**Legislation:** Tax Code, Article 402.

These have ZERO input VAT credit:

- Motor vehicles for personal use (unless transport/rental business)
- Entertainment expenses
- Personal consumption of owners/directors/employees
- Purchases without valid ESF
- Purchases from non-registered suppliers
- Goods/services for exempt supplies
- Alcohol and tobacco (unless production/wholesale)
- Gifts and donations
- Fuel for non-commercial vehicles

Blocked categories OVERRIDE any other rule. Check blocked FIRST.

---

## Step 6: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > 20,000 MCI (Monthly Calculation Index) |
| MCI value (2025) | KZT 3,932 (updated annually) |
| Registration threshold (2025) | ~KZT 78,640,000 (~USD 175,000) |
| Voluntary registration | Below threshold |
| ESF mandatory | All VAT-registered taxpayers |
| EAEU import reporting | Form 328.00 by 20th of following month |

---

## Step 7: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| VAT return (Form 300.00) | Quarterly | 15th of second month after quarter end |
| VAT payment | Quarterly | 25th of second month after quarter end |
| EAEU import form (328.00) | Monthly | 20th of month following import |
| EAEU import VAT payment | Monthly | 20th of month following import |
| ESF issuance | Per transaction | Within 15 calendar days of supply |

### Quarterly Periods

| Quarter | Period | Return Due | Payment Due |
|---------|--------|-----------|-------------|
| Q1 | Jan - Mar | 15 May | 25 May |
| Q2 | Apr - Jun | 15 August | 25 August |
| Q3 | Jul - Sep | 15 November | 25 November |
| Q4 | Oct - Dec | 15 February | 25 February |

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | Warning (first offence) + fine for repeat |
| Late payment | 1.25x refinancing rate of National Bank per day |
| Non-filing | Assessment + administrative fine |
| Failure to issue ESF | Administrative fine per instance |
| Tax evasion | Criminal prosecution |

---

## Step 8: Derived Calculations [T1]

```
Output VAT             = Domestic taxable turnover x 12%
EAEU Import VAT        = Value of EAEU imports x 12%
Total Output VAT       = Output VAT + EAEU Import VAT
Input VAT              = Domestic input VAT + Non-EAEU import VAT + EAEU import VAT (creditable)
Net VAT Payable        = Total Output VAT - Total Input VAT - Credit B/F
If Net < 0             = Credit carried forward or refund
```

---

## Step 9: Reverse Charge on Services [T1]

**Legislation:** Tax Code, Articles 373, 441.

### When Reverse Charge Applies
- Services received from non-resident providers
- Non-resident has no permanent establishment in Kazakhstan
- Place of supply is Kazakhstan

### Treatment
1. Self-assess output VAT at 12% on service value
2. Report in Form 300.00
3. Input credit allowed if service relates to taxable supplies
4. Withhold and remit the reverse charge VAT

---

## PROHIBITIONS [T1]

- NEVER allow unregistered entities to claim input VAT credit
- NEVER classify exempt supplies as zero-rated
- NEVER accept input credit without valid ESF
- NEVER apply input credit on blocked categories
- NEVER treat EAEU imports like non-EAEU imports -- different procedures
- NEVER ignore the 180-day rule for EAEU export zero-rating confirmation
- NEVER file Form 300.00 without reconciling ESF records
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 10: Edge Case Registry

### EC1 -- EAEU import without Form 328.00 [T1]
**Situation:** Goods received from Russia but Form 328.00 not filed by 20th of following month.
**Resolution:** Late filing penalties apply. Self-assessed VAT still due. File Form 328.00 immediately with penalties.

### EC2 -- EAEU export, no confirmation within 180 days [T2]
**Situation:** Goods exported to Belarus, but importing country's tax authority has not confirmed receipt.
**Resolution:** Zero-rating revoked. Standard 12% VAT applies retrospectively. Must amend Form 300.00 for the original period. Flag for reviewer: consider requesting extension or contacting counterpart.
**Legislation:** Tax Code, Article 449.

### EC3 -- Reverse charge on digital services [T2]
**Situation:** Kazakh company subscribes to cloud software from US provider.
**Resolution:** Reverse charge at 12%. Self-assess output VAT. Claim input credit if for taxable supplies. Non-resident provider may also have separate registration obligation for B2C digital services.

### EC4 -- SEZ entity supplies [T3]
**Situation:** Entity operating in Special Economic Zone sells goods locally.
**Resolution:** SEZ entities may have preferential VAT treatment. When goods leave SEZ for domestic consumption, VAT may apply. Escalate to review SEZ agreement.

### EC5 -- Agricultural producer exemption [T2]
**Situation:** Agricultural producer sells unprocessed products.
**Resolution:** May qualify for VAT exemption under Article 394. However, voluntary registration is possible to recover input credit on farming inputs. Flag for reviewer: evaluate whether exemption or registration is more beneficial.

### EC6 -- Multi-currency transactions [T1]
**Situation:** Invoice in USD or RUB.
**Resolution:** Convert to KZT at National Bank of Kazakhstan rate on date of supply. All VAT calculations in KZT.

### EC7 -- Credit notes / adjustments [T1]
**Situation:** Price adjustment after original supply.
**Resolution:** Issue corrective ESF. Adjust output/input VAT in the period of correction. Report in Appendix 300.06.

### EC8 -- Subsoil user VAT [T3]
**Situation:** Oil company operating under subsoil use contract.
**Resolution:** Special VAT regime may apply under the contract. Stability provisions may override general tax code. Escalate.

---

## Step 11: Reviewer Escalation Protocol

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

## Step 12: Test Suite

### Test 1 -- Standard local sale at 12%
**Input:** Domestic sale of goods, net KZT 1,000,000, VAT KZT 120,000. Registered.
**Expected output:** Line 001: KZT 1,000,000. Line 005: Output VAT KZT 120,000.

### Test 2 -- Local purchase with input credit
**Input:** Purchase from registered supplier, net KZT 500,000, VAT KZT 60,000. Valid ESF held.
**Expected output:** Line 008: Input VAT KZT 60,000. Full credit.

### Test 3 -- EAEU import (from Russia)
**Input:** Import of goods from Russia, value KZT 2,000,000.
**Expected output:** Self-assess: Line 006: KZT 240,000 (output). Line 010: KZT 240,000 (input credit). File Form 328.00. Net: zero.

### Test 4 -- Non-EAEU export (zero-rated)
**Input:** Export to Turkey, FOB KZT 5,000,000. Documentation complete.
**Expected output:** Line 002: KZT 5,000,000 at 0%. Full input credit recovery.

### Test 5 -- Blocked input: entertainment
**Input:** Business dinner, KZT 100,000, VAT KZT 12,000.
**Expected output:** Input VAT KZT 0 (BLOCKED).

### Test 6 -- Reverse charge on foreign services
**Input:** Kazakh company pays USD 5,000 (KZT 2,400,000) to German consulting firm.
**Expected output:** Self-assess output VAT: KZT 288,000 (12%). Input credit: KZT 288,000 (if taxable). Net: zero.

### Test 7 -- No ESF, no credit
**Input:** Purchase KZT 300,000, VAT KZT 36,000. Supplier did not issue ESF.
**Expected output:** Input VAT KZT 0. No credit without ESF.

### Test 8 -- EAEU export, confirmation pending
**Input:** Export to Kyrgyzstan KZT 3,000,000. 150 days elapsed, no confirmation yet.
**Expected output:** Currently zero-rated. If no confirmation by day 180, must retrospectively apply 12% = KZT 360,000.

---

## Step 13: Invoice Requirements [T1]

**Legislation:** Tax Code; ESF Regulations.

### ESF (Electronic Invoice) System Details
1. Mandatory for all VAT-registered taxpayers via esf.gov.kz
2. ESF must be issued within 15 calendar days of supply
3. Buyer confirms receipt electronically
4. Input credit only valid with confirmed ESF
5. Corrective ESF for adjustments (not cancellation + reissue)
6. ESF contains digital signature

### Mandatory Contents of ESF
1. Supplier's name, address, BIN/IIN
2. Buyer's name and BIN/IIN
3. Date of issue
4. ESF number (system-generated)
5. Description of goods/services with TNVED code
6. Quantity and unit price
7. VAT rate (12%) and VAT amount
8. Total amount including VAT
9. Origin of goods (for EAEU tracking)
10. Contract reference (if applicable)

---

## Step 14: Record Keeping [T1]

**Legislation:** Tax Code, Chapter 4.

### Mandatory Records (retain for 5 years)
1. All ESF records (digital, via esf.gov.kz)
2. Purchase and sales journals
3. EAEU trade documentation (Form 328.00, confirmations)
4. Non-EAEU customs declarations
5. Bank statements and payment records
6. General ledger, journals, trial balance
7. Stock/inventory records
8. Fixed asset register
9. Payroll records (separate)
10. Transfer pricing documentation (if applicable)

---

## Step 15: Specific Sector Rules

### Oil and Gas / Mining [T3]
- Subsoil users may operate under Stability Contracts
- Special VAT regime per contract terms
- Equipment imports during exploration: potential VAT relief
- **Always escalate subsoil user questions**

### Agriculture [T2]
- Agricultural producers may qualify for VAT exemption
- Unprocessed agricultural products: often exempt
- Processed products: VAT at 12%
- Agricultural cooperatives: special regime possible
- **Flag for reviewer: verify exemption eligibility**

### Construction [T1]
- Construction services: VAT at 12%
- Progress billing: VAT on each milestone
- Input credit on materials per ESF
- Government contracts: standard VAT applies

### IT and Technology [T2]
- IT companies in Astana Hub may have VAT incentives
- Software exports: zero-rated
- Domestic IT services: VAT at 12%
- **Flag for reviewer: confirm Astana Hub status**

### Financial Services [T1]
- Banking services (interest): exempt
- Insurance premiums: exempt
- Advisory and consulting by financial firms: VAT at 12%
- Banks: input credit apportionment required

---

## Step 16: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | Warning (first) + fine (repeat) |
| Late filing | Warning + administrative fine per SRC |
| Late payment | 1.25x refinancing rate per day |
| Failure to issue ESF | Administrative fine per instance |
| Fraudulent declaration | Up to 200% of understated tax |
| Failure to file Form 328.00 | Administrative fine |
| Tax evasion | Criminal prosecution |
| Under-declaration | Additional tax + penalty |
| Late EAEU VAT payment | Interest at refinancing rate |

---

## Step 17: Audit and Appeals [T2]

### Audit Process
1. SRC may audit within **5 years** of filing
2. Desk audits, field audits, thematic audits
3. ESF data analytics for risk-based selection
4. EAEU trade triggers cross-border verification with partner states
5. Subsoil users: audited per contract terms

### Appeals
1. File objection with SRC within **30 working days**
2. Appeal to court within **30 working days** of SRC decision

**Escalate any audit situation to qualified practitioner.**

---

## Contribution Notes

This skill must be validated by a qualified auditor or tax consultant practicing in Kazakhstan before use in production. All T1 rules must be verified against the current Tax Code and SRC instructions.

**A skill may not be published without sign-off from a qualified practitioner in Kazakhstan.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
