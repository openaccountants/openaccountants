---
name: au-super-guarantee
description: >
  Use this skill whenever asked about Australian Superannuation Guarantee (SG) obligations, voluntary super contributions, concessional and non-concessional caps, Division 293 tax, government co-contribution, spouse contribution tax offset, carry-forward rules, or any question about super for sole traders or employers. Trigger on phrases like "how much super do I pay", "SG rate", "super guarantee", "concessional cap", "Division 293", "salary sacrifice super", "personal super contribution deduction", "co-contribution", "BPAY super", "ATO super clearing house", "super fund contribution", or any question about Australian superannuation. Also trigger when classifying bank statement transactions showing super fund payments, BPAY super debits, or ATO Small Business Super Clearing House (SBSCH) payments. ALWAYS read this skill before touching any SG-related work.
version: 2.0
jurisdiction: AU
tax_year: 2024-25
category: international
depends_on:
  - social-contributions-workflow-base
---

# Australia Superannuation Guarantee (SG) -- Sole Trader & Employer Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | Superannuation Guarantee (Administration) Act 1992 (SGAA 1992) |
| Supporting Legislation | SIS Act 1993; ITAA 1997 Div 290-293; Co-contribution Act 2003 |
| Tax Authority | Australian Taxation Office (ATO) |
| Tax Year | 2024-25 (1 July 2024 -- 30 June 2025) |
| Currency | AUD only |
| SG rate (2024-25) | 11.5% (12% from 1 July 2025) |
| Maximum contribution base (quarterly) | $65,070 |
| Concessional cap (2024-25) | $30,000 |
| Non-concessional cap (2024-25) | $120,000 ($360,000 bring-forward) |
| General transfer balance cap | $1,900,000 |
| Division 293 threshold | $250,000 |
| SG quarterly deadlines | 28 Oct, 28 Jan, 28 Apr, 28 Jul |
| Sole trader SG to self | NO obligation -- voluntary only |
| Payday Super | Commences 1 July 2026 |
| Contributor | Open Accountants |
| Validated by | Pending |
| Validation date | April 2026 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown entity structure | Ask -- sole trader vs company affects SG obligation |
| Unknown whether sole trader has employees | Ask -- determines SG requirement |
| Unknown SG rate year | 2024-25 = 11.5%; 2025-26 = 12% |
| Unknown TSB for carry-forward | Assume >= $500,000 (no carry-forward); ask client |
| Unknown s 290-150 notice status | Assume NOT lodged; warn about deadline |
| Unknown contractor vs employee | Flag for reviewer -- multi-factor test |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- entity structure (sole trader / company / trust / partnership), whether client has employees, OTE per quarter (for employers), and voluntary contribution intent (for sole traders).

**Recommended** -- bank statements showing super fund debits, employee roster with OTE, TSB at 30 June prior year, taxable income for Division 293.

**Ideal** -- complete activity statement data, super fund member statements, s 290-150 notice copies, ATO online account showing contribution caps.

### Refusal catalogue

**R-AU-SG-1 -- Defined benefit funds.** *Trigger:* client has a defined benefit fund. *Message:* "Defined benefit fund calculations are actuarially determined and out of scope. Escalate."

**R-AU-SG-2 -- Constitutionally protected funds.** *Trigger:* client has a constitutionally protected state fund. *Message:* "Out of scope. Escalate."

**R-AU-SG-3 -- Family law splits.** *Trigger:* super splitting in divorce. *Message:* "Family law superannuation splits require legal advice. Out of scope."

**R-AU-SG-4 -- SGC penalty computation.** *Trigger:* client has missed SG deadlines and asks about SGC. *Message:* "Super Guarantee Charge computation should be escalated to a qualified practitioner. SGC includes shortfall + 10% nominal interest + $20 per employee per quarter, and is NOT tax-deductible."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to superannuation.

### 3.1 Super fund contributions (employer SG or personal)

| Pattern | Treatment | Notes |
|---|---|---|
| SUPER, SUPERANNUATION | EXCLUDE -- super contribution | Generic super payment |
| AUSTRALIAN SUPER, AUSTSUPER | EXCLUDE -- super contribution | AustralianSuper fund |
| REST, REST SUPER | EXCLUDE -- super contribution | Retail Employees Super |
| HOSTPLUS | EXCLUDE -- super contribution | Hospitality industry fund |
| CBUS, CBUS SUPER | EXCLUDE -- super contribution | Construction industry fund |
| SUNSUPER, AUSTRALIAN RETIREMENT TRUST | EXCLUDE -- super contribution | QLD-based fund (merged) |
| UNISUPER | EXCLUDE -- super contribution | University sector fund |
| HESTA | EXCLUDE -- super contribution | Health sector fund |
| COLONIAL FIRST STATE, CFS | EXCLUDE -- super contribution | Retail fund |
| AMP SUPER, AMP | EXCLUDE -- super contribution | Retail fund |
| MLC SUPER, MLC | EXCLUDE -- super contribution | Retail fund |
| BT SUPER | EXCLUDE -- super contribution | Retail fund |
| SMSF (+ fund name) | EXCLUDE -- super contribution | Self-managed super fund |

### 3.2 BPAY super payments

| Pattern | Treatment | Notes |
|---|---|---|
| BPAY SUPER, BPAY (+ fund name) | EXCLUDE -- super contribution | BPAY is common payment method for super |
| BPAY (biller code matching known super fund) | EXCLUDE -- super contribution | Check BPAY biller code |

### 3.3 ATO Small Business Super Clearing House (SBSCH)

| Pattern | Treatment | Notes |
|---|---|---|
| ATO SUPER, ATO CLEARING HOUSE | EXCLUDE -- super contribution | Small businesses (<20 employees) can pay SG via ATO SBSCH |
| ATO SBSCH | EXCLUDE -- super contribution | Clearing house payment |
| SMALL BUSINESS SUPERANNUATION | EXCLUDE -- super contribution | ATO SBSCH reference |

### 3.4 Super guarantee charge (SGC -- late/missed SG)

| Pattern | Treatment | Notes |
|---|---|---|
| ATO SGC, SUPER GUARANTEE CHARGE | EXCLUDE -- SGC payment | Late SG penalty payment to ATO |

### 3.5 Salary and wages (not super)

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES (outgoing) | Not super | Payroll expense -- SG is separate from wages |
| PAYROLL | Not super | Wages payment |

### 3.6 ATO tax payments (not super)

| Pattern | Treatment | Notes |
|---|---|---|
| ATO IAS, ATO BAS | EXCLUDE -- tax | Activity statement payment (PAYG/GST) |
| ATO INCOME TAX | EXCLUDE -- tax | Not super |

---

## Section 4 -- Worked examples

Six bank statement classifications for a hypothetical Australian sole trader with 2 employees.

### Example 1 -- Quarterly SG payment to employee's super fund

**Input line:**
`28.10.2024 ; AUSTRALIAN SUPER ; DEBIT ; SG Q1 2024-25 EMPLOYEE A ; -2,300.00 ; AUD`

**Reasoning:**
Matches "AUSTRALIAN SUPER" (pattern 3.1). Amount $2,300 = $20,000 OTE x 11.5% SG. This is the Q1 (Jul-Sep) SG contribution for Employee A, paid by the 28 October deadline. Tax-deductible for the employer.

**Classification:** EXCLUDE -- SG contribution for employee. Tax-deductible business expense.

### Example 2 -- Personal voluntary super contribution (sole trader)

**Input line:**
`15.05.2025 ; BPAY HOSTPLUS ; DEBIT ; PERSONAL CONTRIBUTION ; -10,000.00 ; AUD`

**Reasoning:**
Matches "BPAY" + "HOSTPLUS" (pattern 3.2). Sole trader making a personal super contribution. Whether this is concessional (deductible) depends on whether the s 290-150 notice is lodged and acknowledged. If notice lodged: $10,000 concessional contribution, tax-deductible, taxed at 15% in the fund. If no notice: non-concessional, no deduction.

**Classification:** EXCLUDE -- personal super contribution. Deductibility depends on s 290-150 notice status. Flag: "Has the Notice of Intent to Claim a Deduction been lodged with the fund?"

### Example 3 -- ATO Small Business Clearing House payment

**Input line:**
`27.01.2025 ; ATO SUPER CLEARING HOUSE ; DEBIT ; SG Q2 ALL EMPLOYEES ; -4,600.00 ; AUD`

**Reasoning:**
Matches "ATO SUPER CLEARING HOUSE" (pattern 3.3). Small business paying SG for all employees via the ATO SBSCH. The clearing house distributes to each employee's nominated fund. Q2 (Oct-Dec) payment by 28 January deadline.

**Classification:** EXCLUDE -- SG contributions via SBSCH. Tax-deductible.

### Example 4 -- OTE above maximum contribution base

**Input line:**
`28.04.2025 ; REST SUPER ; DEBIT ; SG Q3 EMPLOYEE B ; -7,483.05 ; AUD`

**Reasoning:**
Matches "REST SUPER" (pattern 3.1). Amount $7,483.05 = $65,070 (max contribution base) x 11.5%. Employee B's OTE for Q3 exceeded $65,070, so SG is capped.

**Classification:** EXCLUDE -- SG contribution (capped at maximum contribution base).

### Example 5 -- Sole trader asking about self-SG

**Input line:**
No super fund debits found for the sole trader's own account.

**Reasoning:**
Sole traders have NO SG obligation to themselves. Drawings are not salary. If the sole trader wants super, they must make voluntary personal contributions.

**Classification:** No SG payment expected for sole trader's own account. Recommend voluntary contribution strategy.

### Example 6 -- ATO tax payment (NOT super)

**Input line:**
`28.10.2024 ; ATO ; DEBIT ; IAS SEP QTR ; -3,500.00 ; AUD`

**Reasoning:**
Matches "ATO" + "IAS" (pattern 3.6). This is an Instalment Activity Statement (PAYG/GST) payment, NOT a super contribution.

**Classification:** EXCLUDE -- tax payment. NOT super.

---

## Section 5 -- Tier 1 rules

### Rule 1 -- SG formula

```
SG per quarter = min(Employee_OTE_for_quarter, $65,070) x 11.5%
```

No $450/month threshold (removed 1 July 2022). All employees eligible.

### Rule 2 -- SG rate

2024-25: 11.5%. 2025-26 onwards: 12%.

### Rule 3 -- Quarterly deadlines

| Quarter | Period | Due |
|---|---|---|
| Q1 | 1 Jul - 30 Sep | 28 October |
| Q2 | 1 Oct - 31 Dec | 28 January |
| Q3 | 1 Jan - 31 Mar | 28 April |
| Q4 | 1 Apr - 30 Jun | 28 July |

Late/missed: triggers Super Guarantee Charge (SGC). SGC is NOT tax-deductible.

### Rule 4 -- Sole traders have NO SG obligation to themselves

Drawings are not salary. Only voluntary contributions. Company directors paying themselves a salary: YES SG applies (director is employee of company).

### Rule 5 -- Concessional contributions cap

$30,000 (2024-25). Includes employer SG + salary sacrifice + personal deductible contributions (with s 290-150 notice). Excess included in assessable income at marginal rate (with 15% offset).

### Rule 6 -- Carry-forward unused concessional cap

Available from 2018-19 onward, up to 5 prior years, IF TSB < $500,000 at 30 June prior year. If TSB >= $500,000: no carry-forward.

### Rule 7 -- Non-concessional cap

$120,000 (2024-25). Bring-forward: $360,000 (3 years) if TSB < $1,660,000. TSB >= $1,900,000: nil cap.

### Rule 8 -- s 290-150 notice (personal contribution deduction)

Must lodge Notice of Intent to Claim a Deduction with the super fund AND receive acknowledgement BEFORE the earlier of: lodging the tax return, or end of following financial year. If not lodged: contribution stays non-concessional, NO deduction.

### Rule 9 -- Division 293 (additional 15% for high earners)

```
Div 293 income = taxable income + concessional contributions
If > $250,000: Div 293 tax = 15% x lesser of (concessional contributions, excess over $250,000)
```

### Rule 10 -- Government co-contribution

Max $500. Income < $60,400. Matching rate: 50c per $1 of non-concessional contribution (max $1,000 contributed). Reduces above $45,400. Automatic upon tax return lodgement.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Contractor vs employee for SG

**Trigger:** Client engages a contractor who may be principally for labour (SGAA s 12(3)).
**Issue:** Multi-factor test required. SG may be triggered.
**Action:** Flag for reviewer.

### T2-2 -- Multiple employers exceeding concessional cap

**Trigger:** Individual has two employers both paying SG. Combined may exceed $30,000.
**Issue:** Neither employer at fault. Individual bears excess contributions tax.
**Action:** Flag for reviewer to assess salary sacrifice adjustment.

### T2-3 -- Over-75 contributions

**Trigger:** Client aged 75+ wants to make voluntary contributions.
**Issue:** Work test applies (40 hours in 30 consecutive days). Mandated employer SG has no age limit.
**Action:** Flag for reviewer.

### T2-4 -- Carry-forward with borderline TSB

**Trigger:** TSB close to $500,000 threshold.
**Issue:** Carry-forward availability depends on exact TSB at 30 June.
**Action:** Flag for reviewer to confirm TSB.

### T2-5 -- s 290-150 notice deadline approaching

**Trigger:** Client made personal contributions but has not lodged notice.
**Issue:** Missing the deadline is irreversible -- contribution stays non-concessional.
**Action:** Urgent flag. Confirm notice status before lodging return.

---

## Section 7 -- Excel working paper template

```
AUSTRALIA SUPERANNUATION -- WORKING PAPER
Client: [name]
Financial Year: [2024-25]
Prepared: [date]

ENTITY AND STRUCTURE
  Entity type:                    [Sole trader / Company / Trust / Partnership]
  Has employees:                  [YES/NO]
  Sole trader contributing for self: [YES/NO -- voluntary only]

EMPLOYER SG (PER EMPLOYEE PER QUARTER)
  Employee name:                  [____]
  OTE for quarter:                AUD [____]
  Capped OTE (max $65,070):       AUD [____]
  SG rate:                        11.5%
  SG contribution:                AUD [____]
  Due date:                       [____]
  Paid on time:                   [YES/NO]

PERSONAL CONTRIBUTIONS (SOLE TRADER)
  Personal contribution:          AUD [____]
  s 290-150 notice lodged:        [YES/NO]
  Acknowledged by fund:           [YES/NO]
  Classification:                 [Concessional / Non-concessional]
  Tax deduction claimed:          AUD [____]

CONTRIBUTION CAP CHECK
  Concessional cap:               AUD 30,000
  Total concessional contributions: AUD [____]
  Carry-forward available:        AUD [____]
  Remaining cap:                  AUD [____]
  Non-concessional cap:           AUD [____]
  Total non-concessional:         AUD [____]

DIVISION 293
  Taxable income:                 AUD [____]
  Concessional contributions:     AUD [____]
  Div 293 income:                 AUD [____]
  Div 293 tax (if applicable):    AUD [____]

REVIEWER FLAGS
  [List any Tier 2 flags]
```

---

## Section 8 -- Bank statement reading guide

### How super payments appear on Australian bank statements

**Direct fund payments:**
- Description: Fund name (e.g., "AUSTRALIAN SUPER", "HOSTPLUS", "REST SUPER")
- Timing: Quarterly (by 28th of month after quarter end) or more frequently
- Amount: SG amount per employee or personal contribution amount

**BPAY payments:**
- Description: "BPAY" + biller name or code
- Timing: Any time
- Amount: SG or personal contribution

**ATO Super Clearing House:**
- Description: "ATO SUPER", "ATO CLEARING HOUSE", "SBSCH"
- Timing: Quarterly
- Amount: Combined SG for all employees

**Key identification tips:**
1. Super fund names are the most reliable identifier
2. BPAY to a super fund shows biller code -- cross-reference with fund
3. ATO SBSCH is a single payment covering all employees
4. Sole trader personal contributions look like any other fund payment -- context required
5. SGC payments go to ATO, not to the fund
6. Payday Super (from 1 July 2026) will change timing to each payday

---

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Scan for super fund debits** -- match against fund names in Section 3
2. **Identify SG vs personal contributions** -- quarterly amounts aligned with deadlines = likely SG; ad hoc amounts = likely personal
3. **Check for ATO SBSCH** -- indicates employer using clearing house
4. **Sum quarterly SG payments** -- compare against expected OTE x 11.5% to verify completeness
5. **Flag:** "Super contribution classification derived from bank statement patterns. Employee OTE, s 290-150 notice status, and TSB have not been independently verified. Reviewer must confirm before tax return lodgement."

---

## Section 10 -- Reference material

### Key rates and thresholds (2024-25)

| Item | Value |
|---|---|
| SG rate | 11.5% |
| Max contribution base (quarterly) | $65,070 |
| Maximum SG per quarter | $7,483.05 |
| Concessional cap | $30,000 |
| Non-concessional cap | $120,000 |
| Bring-forward (3 years) | $360,000 |
| Div 293 threshold | $250,000 |
| Co-contribution max | $500 |
| Co-contribution lower threshold | $45,400 |
| Co-contribution upper threshold | $60,400 |
| LISTO threshold | $37,000 |
| Spouse offset max | $540 |
| Transfer balance cap | $1,900,000 |

### LISTO (Low Income Super Tax Offset)

Adjusted taxable income <= $37,000: 15% of concessional contributions, max $500. Paid directly into super fund by ATO.

### Spouse contribution tax offset

Max $540 (18% of $3,000). Full offset if spouse income <= $37,000. Nil if spouse income >= $40,000.

### Test suite

**Test 1:** Employee OTE $20,000/quarter, 2024-25. -> SG = $2,300.

**Test 2:** Employee OTE $80,000/quarter. -> SG = $7,483.05 (capped).

**Test 3:** Sole trader contributes $25,000, lodges s 290-150. TSB $200,000. -> $25,000 concessional. Deduction $25,000. Within cap.

**Test 4:** Taxable income $260,000, concessional $30,000. -> Div 293 income $290,000. Div 293 tax = 15% x $30,000 = $4,500.

**Test 5:** TSB $400,000. Unused cap: $5,000 (2021-22) + $10,000 (2022-23) + $15,000 (2023-24). -> Available cap = $60,000.

**Test 6:** Income $50,000, non-concessional $1,000. -> Co-contribution = $346.68.

**Test 7:** $5,000 to spouse's fund, spouse income $36,000. -> Offset = $540.

**Test 8:** Sole trader asks about SG to self. -> $0. No obligation. Advise voluntary contributions.

### Prohibitions

- NEVER tell a sole trader they must pay SG to themselves
- NEVER apply 12% rate to 2024-25 (rate is 11.5%)
- NEVER ignore maximum contribution base ($65,070/quarter)
- NEVER allow deduction claim without confirmed s 290-150 notice
- NEVER apply carry-forward if TSB >= $500,000
- NEVER present figures as definitive
- NEVER compute SGC penalties without escalating
- NEVER advise on defined benefit or constitutionally protected funds

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
