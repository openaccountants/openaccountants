---
name: uk-national-insurance
description: >
  Use this skill whenever asked about UK National Insurance Contributions (NIC) for self-employed individuals. Trigger on phrases like "how much NIC do I pay", "Class 2 contributions", "Class 4 NIC", "national insurance self-employed", "NIC calculation", "state pension qualifying years", "NIC deferment", "voluntary Class 2", "HMRC NIC payment", or any question about UK NIC obligations for a self-employed client. Also trigger when classifying bank statement transactions showing HMRC NIC debits, Self Assessment NIC payments, or Class 2 direct debits. This skill covers Class 2 voluntary contributions, Class 4 profit-based rates, thresholds, payment schedule, bank statement pattern classification, interaction with employment Class 1, deferment, state pension entitlement, and edge cases. ALWAYS read this skill before touching any UK NIC-related work.
version: 2.0
jurisdiction: GB
tax_year: 2025-26
category: international
depends_on:
  - social-contributions-workflow-base
---

# UK National Insurance (Class 2 + Class 4) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | United Kingdom |
| Primary Legislation | Social Security Contributions and Benefits Act 1992 (SSCBA 1992) |
| Supporting Legislation | National Insurance Contributions Act 2015; Finance Act 2024 (Class 2 reform) |
| Tax Authority | HM Revenue & Customs (HMRC) |
| Tax Year Coverage | 2024-25 and 2025-26 |
| Currency | GBP only |
| Class 2 weekly rate (2025-26) | £3.50 (voluntary from 6 April 2024) |
| Class 2 annual cost (2025-26) | £182.00 |
| Small Profits Threshold (2025-26) | £6,845 |
| Class 4 main rate | 6% on profits between LPL and UPL |
| Class 4 additional rate | 2% on profits above UPL |
| Lower Profits Limit (LPL) | £12,570 |
| Upper Profits Limit (UPL) | £50,270 |
| Payment method | Via Self Assessment (31 Jan / 31 Jul / 31 Jan) |
| Contributor | Open Accountants |
| Validated by | Pending -- requires sign-off by a UK-qualified practitioner |
| Validation date | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown tax year | Ask -- rates differ between 2024-25 and 2025-26 |
| Unknown employment status | Ask -- dual status affects annual maximum cap |
| Unknown profit level | Do not compute -- profits are required |
| Unknown whether client wants voluntary Class 2 | Recommend if profits below SPT and client needs qualifying years |
| Unknown state pension record | Flag for reviewer |
| Unknown age (state pension age) | Ask -- over state pension age = no Class 4 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- tax year, employment status (sole self-employed or dual), and net self-employment profits.

**Recommended** -- bank statements showing HMRC Self Assessment payments, prior year SA302 tax calculation, state pension record printout.

**Ideal** -- complete SA100/SA103 return data, P60 from employment (if dual status), NI record from gov.uk.

### Refusal catalogue

**R-UK-NIC-1 -- Non-resident or overseas client.** *Trigger:* client is non-UK resident or has complex international arrangements. *Message:* "NIC for non-resident or overseas clients involves complex rules under EU/bilateral social security agreements. Escalate to a qualified UK practitioner."

**R-UK-NIC-2 -- Special categories.** *Trigger:* client is a mariner, share fisherman, volunteer development worker, or religious minister. *Message:* "Special NIC provisions apply to this category. Escalate to a qualified practitioner."

**R-UK-NIC-3 -- Deferment computation.** *Trigger:* client requests Class 1 deferment across multiple employments. *Message:* "Class 1 deferment requires HMRC application (form CA72A) and case-specific earnings analysis. Flag for reviewer."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to NIC. When a transaction matches a pattern below, apply the treatment directly.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference. NIC payments always EXCLUDE from any VAT classification -- they are statutory personal obligations.

### 3.1 HMRC Self Assessment payments (include Class 4 + optional Class 2)

| Pattern | Treatment | Notes |
|---|---|---|
| HMRC, HM REVENUE, HM REVENUE & CUSTOMS | EXCLUDE -- tax/NIC payment | Self Assessment payments include income tax + Class 4 NIC + voluntary Class 2 |
| HMRC SELF ASSESSMENT | EXCLUDE -- SA payment | Combined tax and NIC |
| HMRC NDDS, HMRC SHIPLEY | EXCLUDE -- SA payment | HMRC processing centres |
| SELF ASSESSMENT, SA PAYMENT | EXCLUDE -- SA payment | Generic SA reference |

### 3.2 Class 2 direct debits (voluntary -- separate from SA)

| Pattern | Treatment | Notes |
|---|---|---|
| HMRC NIC, HMRC CLASS 2 | EXCLUDE -- voluntary Class 2 | Monthly or quarterly direct debit for Class 2 |
| NATIONAL INSURANCE, NAT INS | EXCLUDE -- NIC payment | Generic NI reference |
| NIC DIRECT DEBIT, NIC D/D | EXCLUDE -- Class 2 DD | Voluntary Class 2 via direct debit |

### 3.3 HMRC payments via bank transfer

| Pattern | Treatment | Notes |
|---|---|---|
| HMRC CUMBERNAULD | EXCLUDE -- SA/NIC payment | HMRC Accounts Office reference |
| 1025 (followed by UTR) | EXCLUDE -- SA payment | HMRC Self Assessment payment reference format (1025 + 10-digit UTR) |

### 3.4 Student loan and other SA components (NOT NIC)

| Pattern | Treatment | Notes |
|---|---|---|
| STUDENT LOAN, SLC | EXCLUDE -- student loan repayment | Not NIC -- see uk-student-loan-repayment skill |
| HMRC (large combined payment) | EXCLUDE -- combined SA | May include income tax + Class 4 + Class 2 + student loan; cannot split from bank statement alone |

### 3.5 Employer Class 1 (payroll -- not self-employed NIC)

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES (incoming credit) | Not NIC | Employment income -- Class 1 deducted at source by employer |
| EMPLOYER NIC | Not self-employed NIC | Employer's Class 1 obligation, not the client's self-employed NIC |

---

## Section 4 -- Worked examples

Six bank statement classifications showing NIC-related transactions for a hypothetical UK self-employed software consultant.

### Example 1 -- Self Assessment balancing payment (combined tax + NIC)

**Input line:**
`31.01.2027 ; HMRC SELF ASSESSMENT ; DEBIT ; SA BALANCING PAYMENT ; -4,200.00 ; GBP`

**Reasoning:**
Matches "HMRC SELF ASSESSMENT" (pattern 3.1). This is the 31 January balancing payment for tax year 2025-26. Includes income tax, Class 4 NIC, and possibly Class 2 voluntary. Cannot split NIC from income tax on the bank statement alone. Exclude from VAT. The SA302 tax calculation will show the NIC breakdown.

**Classification:** EXCLUDE -- SA payment (combined tax and NIC). Request SA302 to determine NIC component.

### Example 2 -- Payment on account (31 July)

**Input line:**
`31.07.2026 ; HMRC NDDS ; DEBIT ; PAYMENT ON ACCOUNT ; -2,100.00 ; GBP`

**Reasoning:**
Matches "HMRC NDDS" (pattern 3.1). This is the second payment on account for 2025-26, due 31 July 2026. Includes 50% of prior year Class 4 liability and income tax. Exclude from VAT.

**Classification:** EXCLUDE -- SA payment on account.

### Example 3 -- Voluntary Class 2 direct debit

**Input line:**
`15.03.2026 ; HMRC NIC ; DEBIT ; CLASS 2 NIC MAR ; -15.17 ; GBP`

**Reasoning:**
Matches "HMRC NIC" (pattern 3.2). Amount approximately £3.50/week x 4.33 weeks = £15.17 monthly. This is a voluntary Class 2 payment via direct debit. Client has profits below SPT and is paying voluntarily for state pension qualifying years.

**Classification:** EXCLUDE -- voluntary Class 2 NIC. Not deductible from profits (Class 2 is not a trading expense).

### Example 4 -- Employment salary credit (not NIC)

**Input line:**
`28.02.2026 ; ACME LTD SALARY ; CREDIT ; FEB SALARY ; +3,200.00 ; GBP`

**Reasoning:**
This is employment income received. Class 1 NIC has already been deducted by the employer at source. This is NOT a self-employment NIC payment. Do not classify as NIC.

**Classification:** NOT NIC -- employment income. Class 1 deducted at source.

### Example 5 -- Large SA payment (combined with student loan)

**Input line:**
`31.01.2027 ; HM REVENUE & CUSTOMS ; DEBIT ; SELF ASSESSMENT ; -8,500.00 ; GBP`

**Reasoning:**
Matches "HM REVENUE & CUSTOMS" (pattern 3.1). Large SA payment that likely combines income tax + Class 4 NIC + possibly Class 2 + student loan repayment. Cannot split components from bank statement. Need SA302 for breakdown.

**Classification:** EXCLUDE -- combined SA payment. Request SA302 for NIC/tax/student loan split.

### Example 6 -- HMRC refund (overpayment)

**Input line:**
`15.04.2027 ; HMRC ; CREDIT ; SA REPAYMENT ; +650.00 ; GBP`

**Reasoning:**
This is a CREDIT from HMRC -- a repayment of overpaid SA (may include overpaid NIC). Exclude from VAT. The SA302 will show the breakdown.

**Classification:** EXCLUDE -- SA refund. Not taxable income. Request SA302 for breakdown.

---

## Section 5 -- Tier 1 rules

### Rule 1 -- Class 4 formula (2025-26)

```
Class 4 NIC = (min(profits, £50,270) - £12,570) x 6% + max(profits - £50,270, 0) x 2%
```

If profits <= £12,570, Class 4 = £0.

### Rule 2 -- Class 2 is voluntary from 6 April 2024

Self-employed with profits >= SPT (£6,845 in 2025-26) are treated as paid automatically (zero-rate credit). No action needed. Profits < SPT: must pay voluntarily (£3.50/week) to get a qualifying year.

### Rule 3 -- Class 4 is based on CURRENT year profits

Unlike Malta SSC, UK Class 4 NIC is calculated on the same year's profits as reported on the SA return.

### Rule 4 -- Payment schedule (via Self Assessment)

| Payment | Due Date | What |
|---|---|---|
| First payment on account | 31 January during tax year | 50% of prior year Class 4 liability |
| Second payment on account | 31 July after tax year end | 50% of prior year Class 4 liability |
| Balancing payment | 31 January following tax year end | Remaining Class 4 (and Class 2 if voluntary) |

### Rule 5 -- Employed AND self-employed

Class 1 continues on employment income. Class 4 due on self-employment profits above LPL. Both apply simultaneously. Annual maximum cap checked by HMRC automatically.

### Rule 6 -- Over state pension age

No Class 4 liability. No Class 2 needed. Must still file SA return for income tax.

### Rule 7 -- Multiple self-employments

Profits from all self-employments are aggregated for Class 4.

### Rule 8 -- Losses

Zero or negative profits: no Class 4. Voluntary Class 2 may still be paid for state pension.

### Rule 9 -- State pension qualifying years

35 qualifying years for full new state pension (£230.25/week in 2025-26). 10 years minimum. Class 2 is the cheapest way to build years (£182/year vs Class 3 at £923/year).

### Rule 10 -- NIC is NOT tax-deductible

Class 2 and Class 4 NIC are NOT deductible business expenses. They are personal statutory obligations.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Deferment (multiple employments)

**Trigger:** Client has two employments and expects combined Class 1 to exceed annual maximum.
**Action:** Flag for reviewer. Client may apply on form CA72A to defer Class 1 in secondary employment.

### T2-2 -- First year with overlap relief / basis period

**Trigger:** Client started trading mid-year; basis period allocation unclear under 2024-25 reform.
**Action:** Flag for reviewer to confirm basis period allocation for Class 4.

### T2-3 -- Backfilling NI gaps for state pension

**Trigger:** Client wants to pay voluntary contributions for prior years.
**Action:** Can go back up to 6 years. Class 2 if eligible as self-employed in those years; otherwise Class 3. Flag for reviewer to check NI record.

### T2-4 -- Examiners, moderators, foster carers

**Trigger:** Employment status is ambiguous.
**Action:** Flag for reviewer. Check contract terms for employment vs self-employment.

### T2-5 -- Non-resident with UK self-employment

**Trigger:** Client is non-UK resident but has UK self-employment profits.
**Action:** Escalate -- complex NIC rules for non-residents.

---

## Section 7 -- Excel working paper template

```
UK NATIONAL INSURANCE COMPUTATION -- WORKING PAPER
Client: [name]
Tax Year: [2024-25 / 2025-26]
Prepared: [date]

INPUT DATA
  Employment status:              [Self-employed only / Employed + self-employed]
  Net trading profits (SA103):    GBP [____]
  Over state pension age:         [YES/NO]
  Voluntary Class 2 elected:      [YES/NO]

CLASS 4 COMPUTATION
  Profits:                        GBP [____]
  Less LPL:                       GBP 12,570
  Main rate band (LPL to UPL):   GBP [____] x 6% = GBP [____]
  Additional rate (above UPL):    GBP [____] x 2% = GBP [____]
  Total Class 4:                  GBP [____]

CLASS 2 (VOLUNTARY)
  Profits vs SPT (GBP 6,845):    [Above / Below]
  Treated as paid automatically:  [YES/NO]
  Voluntary payment:              GBP [0.00 / 182.00]

TOTAL NIC
  Class 4:                        GBP [____]
  Class 2 voluntary:              GBP [____]
  Total:                          GBP [____]

PAYMENT SCHEDULE
  1st POA (31 Jan during year):   GBP [____]
  2nd POA (31 Jul after year):    GBP [____]
  Balancing (31 Jan after year):  GBP [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]
```

---

## Section 8 -- Bank statement reading guide

### How NIC payments appear on UK bank statements

**Self Assessment payments (combined tax + NIC):**
- Description: "HMRC SELF ASSESSMENT", "HM REVENUE & CUSTOMS", "HMRC NDDS", "HMRC SHIPLEY"
- Timing: 31 January (1st POA + balancing), 31 July (2nd POA)
- Amount: Combined income tax + Class 4 + optional Class 2 + student loan
- Cannot split NIC from tax on bank statement -- need SA302

**Voluntary Class 2 direct debit:**
- Description: "HMRC NIC", "HMRC CLASS 2", "NIC D/D"
- Timing: Monthly (around 15th) or quarterly
- Amount: Approximately £15/month or £45/quarter (£3.50/week)

**HMRC refunds:**
- Description: "HMRC", "SA REPAYMENT"
- Direction: CREDIT (incoming)
- May include NIC overpayment component

**Key identification tips:**
1. Most self-employed NIC is embedded within SA payments -- you cannot isolate it from the bank statement
2. Only voluntary Class 2 via direct debit appears as a separate NIC-labelled transaction
3. The SA302 tax calculation is the authoritative source for the NIC breakdown
4. Payments on account are based on prior year -- actual NIC may differ

---

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Scan for HMRC debits** -- identify all outgoing payments matching Section 3 patterns
2. **Identify SA payment dates** -- 31 Jan and 31 Jul payments are SA payments on account
3. **Flag combined nature:** "HMRC Self Assessment payments include income tax, Class 4 NIC, optional Class 2, and student loan repayments combined. The bank statement alone cannot isolate the NIC component. Please provide the SA302 tax calculation or the SA100 return for breakdown."
4. **Identify separate Class 2 DD** -- small monthly debits (~£15) labelled "HMRC NIC" are voluntary Class 2

---

## Section 10 -- Reference material

### Rates comparison (2024-25 vs 2025-26)

| Item | 2024-25 | 2025-26 |
|---|---|---|
| Class 2 weekly rate | £3.45 | £3.50 |
| Class 2 annual | £179.40 | £182.00 |
| SPT | £6,725 | £6,845 |
| Class 4 main rate | 6% | 6% |
| Class 4 additional rate | 2% | 2% |
| LPL | £12,570 | £12,570 |
| UPL | £50,270 | £50,270 |

### Test suite

**Test 1:** 2025-26, self-employed only, profits £30,000. -> Class 4 = £1,045.80. Class 2 treated as paid. Total = £1,045.80.

**Test 2:** 2025-26, self-employed only, profits £80,000. -> Class 4 = £2,856.60. Total = £2,856.60.

**Test 3:** 2025-26, profits £10,000. -> Class 4 = £0. Profits > SPT, Class 2 treated as paid. Total = £0.

**Test 4:** 2025-26, profits £5,000, voluntary Class 2. -> Class 4 = £0. Class 2 = £182.00. Total = £182.00.

**Test 5:** 2025-26, profits -£3,000, voluntary Class 2. -> Class 4 = £0. Class 2 = £182.00. Total = £182.00.

**Test 6:** 2025-26, employed (£45,000 salary, Class 1 via payroll) + self-employed profits £20,000. -> Class 4 = £445.80. Annual max checked by HMRC.

**Test 7:** 2025-26, age 69, profits £40,000. -> Class 4 = £0 (over state pension age). Total = £0.

**Test 8:** 2024-25, profits £30,000. -> Class 4 = £1,045.80. Class 2 treated as paid (profits > SPT £6,725).

### Prohibitions

- NEVER compute Class 4 without confirming the tax year
- NEVER tell a client they must pay Class 2 -- it is voluntary since 6 April 2024
- NEVER tell a client with profits below SPT that they automatically get a qualifying year
- NEVER apply Class 4 rates to employment income
- NEVER ignore the annual maximum NIC cap for dual-status clients
- NEVER advise on deferment without confirming all employment income sources
- NEVER present NIC figures as definitive for dual-status clients
- NEVER assume Class 2 is treated as paid for clients with profits below SPT
- NEVER advise on NIC for non-resident clients without escalating

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
