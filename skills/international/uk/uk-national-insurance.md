---
name: uk-national-insurance
description: Use this skill whenever asked about UK National Insurance Contributions (NIC) for self-employed individuals or employers. Trigger on phrases like "how much NIC do I pay", "Class 2 contributions", "Class 4 NIC", "Class 1 employer NIC", "Employer NIC 15%", "Secondary Threshold £5,000", "Employment Allowance £10,500", "April 2026 NIC", "Class 2 abolished", "national insurance self-employed", "NIC calculation", "state pension qualifying years", "NIC deferment", "voluntary Class 2", "HMRC NIC payment", or any question about UK NIC obligations. Also trigger when classifying bank statement transactions showing HMRC NIC debits, Self Assessment NIC payments, or Class 2 direct debits. This skill covers Class 1 (employee and employer), Class 2 (voluntary post-April 2024), Class 4 (profit-based), thresholds, payment schedule, bank statement pattern classification, Employment Allowance, interaction with employment Class 1, deferment, state pension entitlement, and edge cases across three tax years (2024-25, 2025-26, 2026-27). ALWAYS read this skill before touching any UK NIC-related work.
version: 3.0
jurisdiction: GB
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Power
review_status: current
depends_on: - social-contributions-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK National Insurance

## UK National Insurance -- Comprehensive Skill v3.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **James Power** on 2026-06-03.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### National Insurance

- **Weekly rate** — £3.50 (voluntary from 6 April 2024)  _(Finance Act 2024)_
- **Annual cost** — £182.00  _(Calculated)_
- **Small Profits Threshold** — £6,845  _(SSCBA 1992)_
- **Main rate** — 6% on £12,570 – £50,270  _(SSCBA 1992)_
- **Additional rate** — 2% above £50,270  _(SSCBA 1992)_
- **LPL** — £12,570  _(SSCBA 1992)_
- **UPL** — £50,270  _(SSCBA 1992)_

## Section 1 -- Quick reference (3-year comparison)

**Read this whole section before computing or classifying anything.** This skill covers three tax years: the **Prior year (2024-25)**, the **Current year (2025-26)**, and the **Forthcoming year (2026-27)**.

**3-year comparison table**

| Field | 2024-25 (Prior) | 2025-26 (Current) | 2026-27 (Forthcoming) |
| --- | --- | --- | --- |
| **Class 1 employee main rate** | 8% (from 6 Apr 2024; was 10%) | 8% | 8% |
| **Class 1 employee additional rate** | 2% above UEL | 2% | 2% |
| **Class 1 employer rate** | 13.8% | **15%** | 15% |
| **Secondary Threshold (employer)** | £9,100/yr (£175/wk) | **£5,000/yr (£96/wk)** | £5,000/yr |
| **Primary Threshold (employee)** | £12,570/yr | £12,570/yr | £12,570/yr |
| **Upper Earnings Limit (UEL)** | £50,270/yr (£967/wk) | £50,270/yr | £50,270/yr (frozen to 2027-28) |
| **Employment Allowance** | £5,000 | **£10,500** | £10,500 |
| **Class 2 status** | Abolished (voluntary only) | Abolished (voluntary only) | Abolished (voluntary only) |
| **Class 2 voluntary weekly rate** | £3.45 | £3.50 | TBC (Autumn 2026) |
| **Small Profits Threshold (SPT)** | £6,725 | £6,845 | TBC |
| **Class 4 main rate** | 6% (from 6 Apr 2024; was 9%) | 6% | 6% |
| **Class 4 additional rate** | 2% above UPL | 2% | 2% |
| **Class 4 Lower Profits Limit (LPL)** | £12,570 | £12,570 | £12,570 |
| **Class 4 Upper Profits Limit (UPL)** | £50,270 | £50,270 | £50,270 |
| Country | United Kingdom |  |  |
| Primary Legislation | Social Security Contributions and Benefits Act 1992 (SSCBA 1992); National Insurance Contributions (Reduction in Rates) Act 2024; Autumn Budget 2024 (Class 1 employer changes); Autumn Budget 2025 (no change) |  |  |
| Tax Authority | HM Revenue & Customs (HMRC) |  |  |
| Currency | GBP only |  |  |
| Contributor | Open Accountants |  |  |
| Validated by | Verified by James Power on 2026-06-03 |  |  |
| Validation date | Verified by James Power on 2026-06-03 |  |  |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown tax year | Ask -- rates differ materially between 2024-25, 2025-26, and 2026-27 (especially employer NIC) |
| Unknown employment status | Ask -- dual status affects annual maximum cap |
| Unknown profit level | Do not compute -- profits are required |
| Unknown whether client wants voluntary Class 2 | Recommend if profits below SPT and client needs qualifying years |
| Unknown state pension record | Flag for reviewer |
| Unknown age (state pension age) | Ask -- over state pension age = no Class 4 |
| Unknown payroll size for Employer NIC | Ask -- Employment Allowance depends on prior-year secondary Class 1 < £100k and connected-company rules |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable** — tax year, employment status (sole self-employed, employed, employer, or dual), and net self-employment profits (for Class 4) or gross payroll (for Class 1).
- **Recommended** — bank statements showing HMRC Self Assessment / PAYE payments, prior year SA302 tax calculation, P60/P11D from employment, state pension record printout.
- **Ideal** — complete SA100/SA103 return data, FPS submissions for PAYE clients, NI record from gov.uk.

### Refusal catalogue

- **R-UK-NIC-1 -- Non-resident or overseas client** — Trigger: client is non-UK resident or has complex international arrangements. Message: "NIC for non-resident or overseas clients involves complex rules under EU/bilateral social security agreements. Escalate to a qualified UK practitioner."  _(R-UK-NIC-1)_
- **R-UK-NIC-2 -- Special categories** — Trigger: client is a mariner, share fisherman, volunteer development worker, or religious minister. Message: "Special NIC provisions apply to this category. Escalate to a qualified practitioner."  _(R-UK-NIC-2)_
- **R-UK-NIC-3 -- Deferment computation** — Trigger: client requests Class 1 deferment across multiple employments. Message: "Class 1 deferment requires HMRC application (form CA72A) and case-specific earnings analysis. Flag for reviewer."  _(R-UK-NIC-3)_
- **R-UK-NIC-4 -- Connected-company Employment Allowance** — Trigger: employer is part of a group of connected companies. Message: "Only one company in a connected group can claim the Employment Allowance. Escalate."  _(R-UK-NIC-4)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to NIC. When a transaction matches a pattern below, apply the treatment directly.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference. NIC payments always EXCLUDE from any VAT classification -- they are statutory personal obligations (Class 2/4) or employer payroll obligations (Class 1 employer).

### 3.1 HMRC Self Assessment payments (include Class 4 + optional Class 2)

**HMRC Self Assessment payments patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HMRC, HM REVENUE, HM REVENUE & CUSTOMS | EXCLUDE -- tax/NIC payment | Self Assessment payments include income tax + Class 4 NIC + voluntary Class 2 |
| HMRC SELF ASSESSMENT | EXCLUDE -- SA payment | Combined tax and NIC |
| HMRC NDDS, HMRC SHIPLEY | EXCLUDE -- SA payment | HMRC processing centres |
| SELF ASSESSMENT, SA PAYMENT | EXCLUDE -- SA payment | Generic SA reference |

### 3.2 Class 2 direct debits (voluntary -- separate from SA)

**Class 2 direct debits patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HMRC NIC, HMRC CLASS 2 | EXCLUDE -- voluntary Class 2 | Monthly or quarterly direct debit for Class 2 |
| NATIONAL INSURANCE, NAT INS | EXCLUDE -- NIC payment | Generic NI reference |
| NIC DIRECT DEBIT, NIC D/D | EXCLUDE -- Class 2 DD | Voluntary Class 2 via direct debit |

### 3.3 HMRC PAYE payments (includes Class 1 employee + employer)

**HMRC PAYE payments patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HMRC PAYE, PAYE NIC, HMRC CUMBERNAULD | EXCLUDE -- PAYE payment | Combined PAYE income tax + Class 1 employee + Class 1 employer + Apprenticeship Levy |
| 1025 (followed by UTR) | EXCLUDE -- SA payment | HMRC Self Assessment payment reference format (1025 + 10-digit UTR) |

### 3.4 Student loan and other SA components (NOT NIC)

**Student loan and other SA components patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STUDENT LOAN, SLC | EXCLUDE -- student loan repayment | Not NIC -- see uk-student-loan-repayment skill |
| HMRC (large combined payment) | EXCLUDE -- combined SA | May include income tax + Class 4 + Class 2 + student loan; cannot split from bank statement alone |

### 3.5 Employer Class 1 (payroll context)

**Employer Class 1 payroll context patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES (incoming credit) | Not self-employed NIC | Employment income -- Class 1 deducted at source by employer |
| EMPLOYER NIC | Employer's Class 1 obligation | 13.8% (2024-25) or 15% (2025-26 / 2026-27) on earnings above ST |

## Section 4 -- Worked examples

### Example 1 -- Self Assessment balancing payment (combined tax + NIC)

**Input line:**
`31.01.2027 ; HMRC SELF ASSESSMENT ; DEBIT ; SA BALANCING PAYMENT ; -4,200.00 ; GBP`

**Reasoning:** Matches "HMRC SELF ASSESSMENT" (pattern 3.1). This is the 31 January balancing payment for tax year 2025-26. Includes income tax, Class 4 NIC, and possibly Class 2 voluntary. Cannot split NIC from income tax on the bank statement alone. Exclude from VAT. The SA302 tax calculation will show the NIC breakdown.

**Classification:** EXCLUDE -- SA payment (combined tax and NIC). Request SA302 to determine NIC component.

### Example 2 -- Payment on account (31 July)

**Input line:**
`31.07.2026 ; HMRC NDDS ; DEBIT ; PAYMENT ON ACCOUNT ; -2,100.00 ; GBP`

**Reasoning:** Matches "HMRC NDDS" (pattern 3.1). This is the second payment on account for 2025-26, due 31 July 2026. Includes 50% of prior year Class 4 liability and income tax. Exclude from VAT.

**Classification:** EXCLUDE -- SA payment on account.

### Example 3 -- Voluntary Class 2 direct debit

**Input line:**
`15.03.2026 ; HMRC NIC ; DEBIT ; CLASS 2 NIC MAR ; -15.17 ; GBP`

**Reasoning:** Matches "HMRC NIC" (pattern 3.2). Amount approximately £3.50/week x 4.33 weeks = £15.17 monthly. Voluntary Class 2 payment via direct debit. Client has profits below SPT and is paying voluntarily for state pension qualifying years.

**Classification:** EXCLUDE -- voluntary Class 2 NIC. Not deductible from profits (Class 2 is not a trading expense).

### Example 4 -- Employment salary credit (not NIC)

**Input line:**
`28.02.2026 ; ACME LTD SALARY ; CREDIT ; FEB SALARY ; +3,200.00 ; GBP`

**Reasoning:** This is employment income received. Class 1 NIC has already been deducted by the employer at source. This is NOT a self-employment NIC payment.

**Classification:** NOT NIC -- employment income. Class 1 deducted at source.

### Example 5 -- Large SA payment (combined with student loan)

**Input line:**
`31.01.2027 ; HM REVENUE & CUSTOMS ; DEBIT ; SELF ASSESSMENT ; -8,500.00 ; GBP`

**Reasoning:** Matches "HM REVENUE & CUSTOMS" (pattern 3.1). Large SA payment that likely combines income tax + Class 4 NIC + possibly Class 2 + student loan repayment. Cannot split components from bank statement. Need SA302 for breakdown.

**Classification:** EXCLUDE -- combined SA payment. Request SA302 for NIC/tax/student loan split.

### Example 6 -- HMRC refund (overpayment)

**Input line:**
`15.04.2027 ; HMRC ; CREDIT ; SA REPAYMENT ; +650.00 ; GBP`

**Reasoning:** This is a CREDIT from HMRC -- a repayment of overpaid SA (may include overpaid NIC). Exclude from VAT.

**Classification:** EXCLUDE -- SA refund. Not taxable income. Request SA302 for breakdown.

### Example 7 -- Employer NIC impact: 2024-25 vs 2025-26 (side-by-side)

**Scenario:** A small employer pays one employee a gross salary of **£35,000** per year. Show the employer Class 1 NIC cost in 2024-25 (13.8% / ST £9,100) versus 2025-26 (15% / ST £5,000), and net of Employment Allowance.

**Employer NIC comparison table**

| Component | 2024-25 (Prior) | 2025-26 (Current) |
| --- | --- | --- |
| Gross salary | £35,000.00 | £35,000.00 |
| Secondary Threshold (ST) | £9,100 | £5,000 |
| Earnings above ST | £25,900 | £30,000 |
| Employer NIC rate | 13.8% | 15% |
| **Gross employer NIC** | **£3,574.20** | **£4,500.00** |
| Employment Allowance offset (single-director companies excluded) | up to £5,000 | up to £10,500 |
| **Employer NIC after Employment Allowance** (if eligible) | **£0** (£3,574.20 fully absorbed) | **£0** (£4,500.00 fully absorbed) |
| **Employer NIC if NOT eligible for EA** | **£3,574.20** | **£4,500.00** |

**Real-world impact:**
- For an **ineligible** employer (e.g. single-director company with no other employees on payroll, or a connected-company group that already claimed elsewhere), the cost rises by **£925.80 (+25.9%)** for a £35k employee from 2024-25 to 2025-26 -- driven by both the rate increase (13.8% -> 15%) and the ST reduction (£9,100 -> £5,000).
- For an **eligible** small employer, the doubled Employment Allowance (£5,000 -> £10,500) absorbs the full increase and may shield additional headcount.
- Worked check, 2025-26: (£35,000 - £5,000) x 15% = £30,000 x 0.15 = £4,500.00 ✓.
- Worked check, 2024-25: (£35,000 - £9,100) x 13.8% = £25,900 x 0.138 = £3,574.20 ✓.

**Reviewer flag:** Confirm Employment Allowance eligibility (employer's secondary Class 1 in the prior tax year was below £100,000, not a single-director-only company, and not the connected company in a group that already claims).

### Example 8 -- Self-employed Class 4 across 3 years (same £30,000 profit)

**Class 4 across 3 years table**

| Year | Profits | Class 4 calc | Class 4 NIC |
| --- | --- | --- | --- |
| 2024-25 | £30,000 | (£30,000 - £12,570) x 6% | £1,045.80 |
| 2025-26 | £30,000 | (£30,000 - £12,570) x 6% | £1,045.80 |
| 2026-27 | £30,000 | (£30,000 - £12,570) x 6% | £1,045.80 |

Class 4 rates and thresholds are unchanged across all three years. Class 2 treated as paid (profits > SPT) in all years -- no voluntary payment needed.

## Section 5 -- Tier 1 rules (per year)

### Rule 1 -- Class 1 employee formula (all three years -- unchanged)

- **Class 1 employee formula** — Class 1 (employee) = max(0, min(earnings, UEL) - PT) x 8% + max(earnings - UEL, 0) x 2% PT = £12,570/yr, UEL = £50,270/yr (frozen through 2027-28)  _(Rule 1)_

### Rule 2 -- Class 1 employer formula (rate and threshold CHANGE in 2025-26)

- **Class 1 employer formula by year** — 2024-25: Employer NIC = max(0, earnings - £9,100) x 13.8% 2025-26: Employer NIC = max(0, earnings - £5,000) x 15% 2026-27: Employer NIC = max(0, earnings - £5,000) x 15%    (unchanged from 2025-26)  _(Rule 2)_
- **Employment Allowance cap by year** — Reduce by Employment Allowance (capped at the lesser of secondary Class 1 due in year and the allowance): 2024-25: up to £5,000; 2025-26: up to £10,500; 2026-27: up to £10,500  _(Rule 2)_

### Rule 3 -- Class 2 abolished from 6 April 2024

- **Class 2 treatment for all three years** — For all three years (2024-25, 2025-26, 2026-27): self-employed with profits >= SPT are treated as paid automatically (zero-rate credit). No action needed. Profits < SPT: may pay voluntarily (£3.45/wk in 2024-25; £3.50/wk in 2025-26; TBC for 2026-27) to get a qualifying year.  _(Rule 3)_

### Rule 4 -- Class 4 formula (unchanged across all three years)

- **Class 4 NIC formula** — Class 4 NIC = (min(profits, £50,270) - £12,570) x 6% + max(profits - £50,270, 0) x 2%  _(Rule 4)_
- **Class 4 zero threshold and rate change history** — If profits <= £12,570, Class 4 = £0. Rates were reduced from 9% to 6% from 6 April 2024 and have not changed since.  _(Rule 4)_

### Rule 5 -- Class 4 is based on CURRENT year profits

- **Basis of Class 4 calc** — Unlike Malta SSC, UK Class 4 NIC is calculated on the same year's profits as reported on the SA return.  _(Rule 5)_

### Rule 6 -- Payment schedule (via Self Assessment)

**Payment schedule table**  _(Rule 6)_

| Payment | Due Date | What |
| --- | --- | --- |
| First payment on account | 31 January during tax year | 50% of prior year Class 4 liability |
| Second payment on account | 31 July after tax year end | 50% of prior year Class 4 liability |
| Balancing payment | 31 January following tax year end | Remaining Class 4 (and Class 2 if voluntary) |

### Rule 7 -- Employed AND self-employed

- **Dual status rule** — Class 1 continues on employment income. Class 4 due on self-employment profits above LPL. Both apply simultaneously. Annual maximum cap checked by HMRC automatically.  _(Rule 7)_

### Rule 8 -- Over state pension age

- **Over state pension age rule** — No Class 4 liability. No Class 2 needed. Must still file SA return for income tax. Employees over state pension age also stop paying Class 1 employee (but employer Class 1 continues).  _(Rule 8)_

### Rule 9 -- Multiple self-employments

- **Aggregation rule** — Profits from all self-employments are aggregated for Class 4.  _(Rule 9)_

### Rule 10 -- Losses

- **Losses rule** — Zero or negative profits: no Class 4. Voluntary Class 2 may still be paid for state pension.  _(Rule 10)_

### Rule 11 -- State pension qualifying years

- **State pension qualifying years rule** — 35 qualifying years for full new state pension (£230.25/week in 2025-26). 10 years minimum. Class 2 is the cheapest way to build years (~£182/year vs Class 3 at £923/year).  _(Rule 11)_

### Rule 12 -- NIC is NOT tax-deductible (personal)

- **Deductibility rule** — Class 2 and Class 4 NIC are NOT deductible business expenses for the individual. They are personal statutory obligations. Employer Class 1 NIC, by contrast, IS a deductible business expense in the company's accounts.  _(Rule 12)_

## Section 6 -- Tier 2 catalogue

### T2-1 -- Deferment (multiple employments)

- **T2-1** — Trigger: Client has two employments and expects combined Class 1 to exceed annual maximum. Action: Flag for reviewer. Client may apply on form CA72A to defer Class 1 in secondary employment.  _(T2-1)_

### T2-2 -- First year with overlap relief / basis period

- **T2-2** — Trigger: Client started trading mid-year; basis period allocation unclear under 2024-25 reform. Action: Flag for reviewer to confirm basis period allocation for Class 4.  _(T2-2)_

### T2-3 -- Backfilling NI gaps for state pension

- **T2-3** — Trigger: Client wants to pay voluntary contributions for prior years. Action: Can go back up to 6 years. Class 2 if eligible as self-employed in those years; otherwise Class 3. Flag for reviewer to check NI record.  _(T2-3)_

### T2-4 -- Examiners, moderators, foster carers

- **T2-4** — Trigger: Employment status is ambiguous. Action: Flag for reviewer. Check contract terms for employment vs self-employment.  _(T2-4)_

### T2-5 -- Non-resident with UK self-employment

- **T2-5** — Trigger: Client is non-UK resident but has UK self-employment profits. Action: Escalate -- complex NIC rules for non-residents.  _(T2-5)_

### T2-6 -- Employment Allowance eligibility

- **T2-6** — Trigger: Employer payroll client; need to confirm EA can be claimed. Action: Confirm (a) prior-year secondary Class 1 < £100,000, (b) not a single-director-only company (sole director with no other employees), (c) for a connected-company group, only one company claims. Flag for reviewer if any criterion is uncertain.  _(T2-6)_

### T2-7 -- Director on annual earnings basis

- **T2-7** — Trigger: Director's earnings calculated on cumulative annual basis rather than per pay period. Action: Flag for reviewer -- different rules apply for directors' NIC computation.  _(T2-7)_

## Section 7 -- Excel working paper template

UK NATIONAL INSURANCE COMPUTATION -- WORKING PAPER
Client: [name]
Tax Year: [2024-25 / 2025-26 / 2026-27]
Prepared: [date]

INPUT DATA
  Employment status:              [Self-employed only / Employed + self-employed / Employer]
  Net trading profits (SA103):    GBP [____]
  Gross payroll (if employer):    GBP [____]
  Over state pension age:         [YES/NO]
  Voluntary Class 2 elected:      [YES/NO]
  Employment Allowance eligible:  [YES/NO]

CLASS 1 EMPLOYER COMPUTATION (if applicable)
  Year:                           [2024-25 / 2025-26 / 2026-27]
  Secondary Threshold:            [£9,100 / £5,000 / £5,000]
  Rate:                           [13.8% / 15% / 15%]
  Employer NIC:                   GBP [____]
  Less Employment Allowance:      GBP [____] (max £5,000 / £10,500 / £10,500)
  Net Employer NIC:               GBP [____]

CLASS 4 COMPUTATION
  Profits:                        GBP [____]
  Less LPL:                       GBP 12,570
  Main rate band (LPL to UPL):   GBP [____] x 6% = GBP [____]
  Additional rate (above UPL):    GBP [____] x 2% = GBP [____]
  Total Class 4:                  GBP [____]

CLASS 2 (VOLUNTARY)
  Profits vs SPT:                 [Above / Below]
  Treated as paid automatically:  [YES/NO]
  Voluntary payment:              GBP [____]

TOTAL NIC
  Class 1 employer (net of EA):   GBP [____]
  Class 4:                        GBP [____]
  Class 2 voluntary:              GBP [____]
  Total:                          GBP [____]

PAYMENT SCHEDULE
  1st POA (31 Jan during year):   GBP [____]
  2nd POA (31 Jul after year):    GBP [____]
  Balancing (31 Jan after year):  GBP [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]

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
- Amount: Approximately £15/month or £45/quarter (£3.45-3.50/week)

**Employer PAYE/NIC payments:**
- Description: "HMRC PAYE", "HMRC CUMBERNAULD", "PAYE NIC"
- Timing: Monthly (around 22nd) or quarterly for small employers
- Amount: Combined PAYE income tax + Class 1 employee + Class 1 employer + Apprenticeship Levy

**HMRC refunds:**
- Description: "HMRC", "SA REPAYMENT"
- Direction: CREDIT (incoming)
- May include NIC overpayment component

**Key identification tips:**
1. Most self-employed NIC is embedded within SA payments -- you cannot isolate it from the bank statement
2. Only voluntary Class 2 via direct debit appears as a separate NIC-labelled transaction
3. The SA302 tax calculation is the authoritative source for the NIC breakdown
4. Employer NIC is embedded inside the combined monthly PAYE remittance

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Scan for HMRC debits** -- identify all outgoing payments matching Section 3 patterns
2. **Identify SA payment dates** -- 31 Jan and 31 Jul payments are SA payments on account
3. **Identify PAYE payment dates** -- 22nd of each month for employers
4. **Flag combined nature:** "HMRC Self Assessment payments include income tax, Class 4 NIC, optional Class 2, and student loan repayments combined. The bank statement alone cannot isolate the NIC component. Please provide the SA302 tax calculation or the SA100 return for breakdown."
5. **Identify separate Class 2 DD** -- small monthly debits (~£15) labelled "HMRC NIC" are voluntary Class 2

## Section 10 -- Reference material

### Full 3-year rate table

**Full 3-year rate table**

| Item | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| **Class 1 employee main** | 8% | 8% | 8% |
| **Class 1 employee additional** | 2% | 2% | 2% |
| **Class 1 employer rate** | 13.8% | **15%** | 15% |
| **Secondary Threshold** | £9,100 | **£5,000** | £5,000 |
| **Primary Threshold** | £12,570 | £12,570 | £12,570 |
| **Upper Earnings Limit** | £50,270 | £50,270 | £50,270 |
| **Employment Allowance** | £5,000 | **£10,500** | £10,500 |
| **Class 2 weekly rate (voluntary)** | £3.45 | £3.50 | TBC |
| **Class 2 annual (voluntary)** | £179.40 | £182.00 | TBC |
| **SPT** | £6,725 | £6,845 | TBC |
| **Class 4 main rate** | 6% | 6% | 6% |
| **Class 4 additional rate** | 2% | 2% | 2% |
| **LPL** | £12,570 | £12,570 | £12,570 |
| **UPL** | £50,270 | £50,270 | £50,270 |

### Test suite

**Test 1:** 2025-26, self-employed only, profits £30,000. -> Class 4 = £1,045.80. Class 2 treated as paid. Total = £1,045.80.

**Test 2:** 2025-26, self-employed only, profits £80,000. -> Class 4 = £2,856.60. Total = £2,856.60.

**Test 3:** 2025-26, profits £10,000. -> Class 4 = £0. Profits > SPT, Class 2 treated as paid. Total = £0.

**Test 4:** 2025-26, profits £5,000, voluntary Class 2. -> Class 4 = £0. Class 2 = £182.00. Total = £182.00.

**Test 5:** 2025-26, profits -£3,000, voluntary Class 2. -> Class 4 = £0. Class 2 = £182.00. Total = £182.00.

**Test 6:** 2025-26, employed (£45,000 salary, Class 1 via payroll) + self-employed profits £20,000. -> Class 4 = £445.80. Annual max checked by HMRC.

**Test 7:** 2025-26, age 69, profits £40,000. -> Class 4 = £0 (over state pension age). Total = £0.

**Test 8:** 2024-25, profits £30,000. -> Class 4 = £1,045.80. Class 2 treated as paid (profits > SPT £6,725).

**Test 9:** 2024-25, employer, employee salary £35,000, EA-ineligible. -> Employer NIC = (£35,000 - £9,100) x 13.8% = £3,574.20.

**Test 10:** 2025-26, employer, employee salary £35,000, EA-ineligible. -> Employer NIC = (£35,000 - £5,000) x 15% = £4,500.00. Year-on-year increase: £925.80 (+25.9%).

**Test 11:** 2026-27, employer, employee salary £35,000, EA-ineligible. -> Employer NIC = (£35,000 - £5,000) x 15% = £4,500.00 (unchanged from 2025-26).

**Test 12:** 2025-26, employer, two employees £25k + £25k, EA-eligible. -> Gross employer NIC = 2 x (£25,000 - £5,000) x 15% = £6,000. After EA (£10,500): £0 employer NIC payable.

### Prohibitions

- NEVER compute NIC without confirming the tax year (Class 1 employer rates and ST changed significantly in April 2025)
- NEVER tell a client they must pay Class 2 -- it is voluntary since 6 April 2024
- NEVER tell a client with profits below SPT that they automatically get a qualifying year
- NEVER apply Class 4 rates to employment income
- NEVER ignore the annual maximum NIC cap for dual-status clients
- NEVER advise on deferment without confirming all employment income sources
- NEVER present NIC figures as definitive for dual-status clients
- NEVER assume Class 2 is treated as paid for clients with profits below SPT
- NEVER advise on NIC for non-resident clients without escalating
- NEVER apply 13.8% / £9,100 to 2025-26 or 2026-27 employer payroll (rate is 15% / £5,000)
- NEVER apply the £5,000 Employment Allowance to 2025-26 or 2026-27 (it doubled to £10,500)
- NEVER allow Employment Allowance for a single-director-only company or for more than one company in a connected group

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
