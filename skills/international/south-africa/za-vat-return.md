---
name: za-vat-return
description: Use this skill whenever asked about South African VAT returns for self-employed individuals or small businesses. Trigger on phrases like "South Africa VAT", "VAT201", "SARS VAT", "15% VAT", "eFiling VAT", "zero-rated SA", "VAT vendor", or any question about VAT filing, computation, or registration for vendors in South Africa. Covers the 15% standard rate, zero-rated and exempt supplies, R1M registration threshold, VAT201 return, and bimonthly filing via SARS eFiling. ALWAYS read this skill before touching any South African VAT work.
---

# South Africa VAT Return (VAT201) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | South Africa |
| Jurisdiction Code | ZA |
| Primary Legislation | Value-Added Tax Act 89 of 1991 (VAT Act) |
| Supporting Legislation | Tax Administration Act 28 of 2011 (TAA); SARS interpretation notes and binding general rulings |
| Tax Authority | South African Revenue Service (SARS) |
| Filing Portal | SARS eFiling (efiling.sars.gov.za) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a South African registered tax practitioner |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: rate application, registration threshold, VAT201 computation, filing deadlines. Tier 2: mixed supplies, deemed supplies, second-hand goods input tax. Tier 3: cross-border services, customs VAT, VAT grouping, large-value complex transactions. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before preparing any VAT return, you MUST know:

1. **VAT registration status** [T1] -- registered vendor; VAT number
2. **Filing category** [T1] -- Category A (bimonthly), B (monthly), C (six-monthly), D (annual), E (bimonthly aligned to tax year)
3. **Accounting basis** [T1] -- invoice basis or payments basis
4. **Nature of supplies** [T1] -- standard-rated (15%), zero-rated (0%), or exempt
5. **Input tax on purchases** [T1] -- with valid tax invoices
6. **Whether making imported services** [T2] -- reverse charge may apply

**If the client's taxable supplies have not exceeded R1,000,000 in any 12-month period and they are not voluntarily registered, STOP. No VAT obligations.**

---

## Step 1: Registration [T1]

**Legislation:** VAT Act, s 23

| Rule | Detail |
|------|--------|
| Compulsory registration | Taxable supplies exceed or expected to exceed **R1,000,000** in any 12-month period |
| Voluntary registration | Taxable supplies exceed R50,000 in any 12-month period (lower threshold for voluntary) |
| Effective date | From the first day of the month following when registration is required |
| VAT number | Issued by SARS upon approval |

---

## Step 2: Rates and Supply Classification [T1]

**Legislation:** VAT Act, s 7 (standard rate), s 11 (zero-rated), s 12 (exempt)

### VAT Rate [T1]

| Rate | Application |
|------|------------|
| **15%** | Standard rate on all taxable supplies (effective 1 April 2018) |
| **0%** | Zero-rated supplies (Schedule of zero-rated supplies) |
| **Exempt** | Exempt supplies (s 12 list) |

### Zero-Rated Supplies (0%) [T1]

| Category | Examples |
|----------|---------|
| Exports | Goods exported from SA; services to non-residents consumed outside SA |
| Basic foodstuffs | Brown bread, maize meal, samp, mealie rice, dried beans, lentils, pilchards, milk powder, rice, vegetables, fruit, eggs, vegetable oil, milk |
| Petrol/diesel | Fuel levy applies instead |
| International transport | Air and sea transport |
| Agricultural inputs | Certain farming inputs |
| Municipal property rates | Rates charged by municipalities |

### Exempt Supplies [T1]

| Category | Examples |
|----------|---------|
| Financial services | Interest, life insurance, unit trust management |
| Residential rental | Rental of residential dwelling |
| Public transport | Minibus taxi, municipal bus |
| Educational services | By registered educational institutions |
| Childcare | Creches and after-school care |

---

## Step 3: Tax Invoice Requirements [T1]

**Legislation:** VAT Act, s 20

### Full Tax Invoice (supplies > R5,000) [T1]

| Element | Required |
|---------|---------|
| Words "Tax Invoice" | Yes |
| Supplier name, address, VAT number | Yes |
| Recipient name, address, VAT number | Yes |
| Serial number and date | Yes |
| Description of goods/services | Yes |
| Quantity/volume | Yes |
| Value excluding VAT | Yes |
| VAT rate and VAT amount | Yes |
| Total including VAT | Yes |

### Abridged Tax Invoice (supplies R50 -- R5,000) [T1]

Reduced information required -- supplier details, date, description, and total including VAT (with VAT rate shown).

### No invoice required for supplies under R50.

---

## Step 4: VAT201 Return Computation [T1]

**Legislation:** VAT Act, s 16, 28

| Field | Description | How to Populate |
|-------|-------------|-----------------|
| 1 | Standard-rated supplies | Total value of supplies at 15% (VAT exclusive) |
| 1A | VAT on standard-rated supplies | Field 1 x 15% |
| 2 | Zero-rated supplies | Total value of 0% supplies |
| 3 | Exempt supplies | Total exempt supplies |
| 4 | Total supplies | 1 + 2 + 3 |
| 5 | Capital goods purchased (standard-rated) | VAT-exclusive value of capital goods |
| 5A | VAT on capital goods | Field 5 x 15% |
| 6 | Other goods/services purchased | VAT-exclusive value |
| 6A | VAT on other purchases | Field 6 x 15% |
| 7 | Total input tax | 5A + 6A + adjustments |
| 8 | Output tax (1A) less input tax (7) | 1A - 7 |
| 9 | VAT payable / (refundable) | Field 8 (positive = payable; negative = refund) |

---

## Step 5: Filing Frequency and Deadlines [T1]

**Legislation:** VAT Act, s 27

### Filing Categories [T1]

| Category | Frequency | Who |
|----------|-----------|-----|
| A | Every 2 months (bimonthly) | Default for most vendors |
| B | Monthly | Taxable supplies > R30M per year |
| C | Every 6 months | Farming enterprises (by approval) |
| D | Every 12 months | Small vendors (by approval) |
| E | Every 2 months (aligned to tax year end) | Certain vendors by arrangement |

### Bimonthly Periods (Category A) [T1]

| Period | Months | Return Due |
|--------|--------|-----------|
| 1 | March -- April | Last business day of May |
| 2 | May -- June | Last business day of July |
| 3 | July -- August | Last business day of September |
| 4 | September -- October | Last business day of November |
| 5 | November -- December | Last business day of January |
| 6 | January -- February | Last business day of March |

### Filing Deadline [T1]

| Method | Deadline |
|--------|----------|
| eFiling | Last business day of the month following the period end |
| Manual (branch) | 25th of the month following period end |

---

## Step 6: Payments Basis [T1]

**Legislation:** VAT Act, s 15

| Rule | Detail |
|------|--------|
| Eligibility | Taxable supplies < R2,500,000 in any 12-month period |
| How it works | Account for VAT when payment is made or received (not when invoice is issued) |
| Advantage | Cash flow benefit -- no VAT owed until cash is received |
| Application | Must apply to SARS to use payments basis |

---

## Step 7: Input Tax on Second-Hand Goods [T2]

**Legislation:** VAT Act, s 1 (definition), s 16(3)(a)(ii)

| Rule | Detail |
|------|--------|
| What | A registered vendor can claim notional input tax on second-hand goods purchased from a non-vendor |
| Calculation | Tax fraction (15/115) x consideration paid |
| Documentation | Requires a declaration from the seller and proof of payment |
| Limit | Cannot exceed the lesser of: consideration paid or open market value |

[T2] Flag for reviewer -- notional input tax claims require careful documentation.

---

## Step 8: Penalties and Interest [T1]

**Legislation:** TAA, Chapter 15

| Offence | Penalty |
|---------|---------|
| Late filing | Fixed amount penalty (based on assessed loss or taxable income, escalating scale) |
| Late payment | 10% of the amount outstanding |
| Interest on underpayment | Prescribed rate (approximately prime rate) compounding monthly |
| Understatement | 10-200% depending on behavior (substantial understatement, gross negligence, fraud) |
| Non-registration | Penalties under TAA |

---

## Step 9: Edge Case Registry

### EC1 -- Imported services (reverse charge) [T2]
**Situation:** SA-based freelancer purchases cloud software from US provider.
**Resolution:** If the foreign supplier is not VAT-registered in SA and the service is consumed in SA, the recipient must account for VAT under s 7(1)(c) (imported services). Output tax = 15% of the consideration. May claim corresponding input tax if the service is for making taxable supplies (net effect zero). [T2] Flag for reviewer.

### EC2 -- Mixed supplies (taxable and exempt) [T2]
**Situation:** Business provides both taxable consulting and exempt financial services.
**Resolution:** Input tax must be apportioned. Directly attributable input follows its supply. Residual input is apportioned using a fair and reasonable method (typically revenue-based ratio). [T2] Flag for reviewer on apportionment method.

### EC3 -- Bad debts [T1]
**Situation:** Vendor issued invoice, accounted for output VAT on invoice basis, but debtor has not paid for over 12 months.
**Resolution:** May claim input tax deduction (bad debt relief) under s 22(1) if the debt is written off and has been outstanding for at least 12 months. Calculated as tax fraction (15/115) of the debt written off.

### EC4 -- Change from payments to invoice basis [T2]
**Situation:** Business grows and exceeds R2,500,000 turnover threshold.
**Resolution:** Must switch to invoice basis. Transitional adjustments required for invoices issued but not yet paid, and payments received in advance. [T2] Significant complexity -- flag for tax practitioner.

### EC5 -- Voluntary registration below R1M [T1]
**Situation:** Freelancer with R200,000 turnover wants to register voluntarily.
**Resolution:** Permitted if taxable supplies exceed R50,000. Can register and claim input tax on business purchases. Must charge 15% to all customers and file returns on schedule.

### EC6 -- Zero-rated vs exempt confusion [T1]
**Situation:** Client thinks exempt supplies allow input tax claims.
**Resolution:** INCORRECT. Zero-rated = taxable at 0% (input tax claimable). Exempt = NOT taxable (NO input tax claimable). Critical distinction.

---

## Step 10: Test Suite

### Test 1 -- Standard bimonthly return
**Input:** Standard-rated supplies R500,000. Purchases R200,000 (all standard-rated, valid invoices).
**Expected output:**
- Output VAT: R500,000 x 15% = R75,000
- Input VAT: R200,000 x 15% = R30,000
- VAT payable: R75,000 - R30,000 = R45,000

### Test 2 -- Refund position (exporter)
**Input:** Zero-rated exports R800,000. Purchases R300,000 (standard-rated).
**Expected output:**
- Output VAT: R0
- Input VAT: R300,000 x 15% = R45,000
- Refund: R45,000

### Test 3 -- Mixed supplies (apportionment)
**Input:** Taxable supplies R600,000, exempt supplies R400,000. Total input VAT R90,000 (none directly attributable).
**Expected output:**
- Taxable ratio: 600,000 / 1,000,000 = 60%
- Claimable input: R90,000 x 60% = R54,000
- Output VAT: R600,000 x 15% = R90,000
- VAT payable: R90,000 - R54,000 = R36,000

### Test 4 -- Second-hand goods purchase
**Input:** Vendor buys used equipment from non-vendor for R50,000 (no VAT charged).
**Expected output:**
- Notional input tax: R50,000 x 15/115 = R6,521.74
- Claimable as input tax on VAT201

### Test 5 -- Bad debt relief
**Input:** Invoice for R23,000 (incl. VAT) written off after 14 months.
**Expected output:**
- Bad debt relief: R23,000 x 15/115 = R3,000
- Claimed as input tax deduction on current period return

---

## PROHIBITIONS

- NEVER claim input tax on exempt supplies -- only taxable (including zero-rated) supplies qualify
- NEVER charge VAT if not registered as a vendor
- NEVER use a rate other than 15% for standard-rated supplies
- NEVER confuse zero-rated (input tax claimable) with exempt (input tax NOT claimable)
- NEVER claim input tax without a valid tax invoice (for supplies over R50)
- NEVER ignore the bimonthly filing deadline -- penalties apply from the first day late
- NEVER apply payments basis without SARS approval
- NEVER claim notional input on second-hand goods without proper documentation and declarations
- NEVER present calculations as definitive -- always label as estimated and direct client to a SARS-registered tax practitioner

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, chartered accountant (CA(SA)), or equivalent licensed practitioner in South Africa) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
