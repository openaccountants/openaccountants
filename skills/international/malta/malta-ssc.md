---
name: malta-ssc
description: >
  Use this skill whenever asked about Malta Social Security Contributions (SSC) for self-employed or self-occupied individuals. Trigger on phrases like "how much SSC do I pay", "Class 2 contributions", "social security self-employed", "SSC calculation", "SSC arrears", "do I need to pay SSC", "SSC and income tax", "DSS payment", "Class 2 quarterly debit", or any question about Malta SSC obligations for a self-employed client. Also trigger when classifying bank statement transactions that relate to DSS debits, SSC direct debits, or government social security payments from BOV, HSBC, or other Maltese banks. Also trigger when preparing a TA24 income tax return where SSC deductibility (Box 20) is relevant. This skill covers Class 2 rates, min/max caps, payment schedule, registration, penalties, interaction with income tax, TA22 part-time regime, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any SSC-related work.
version: 2.0
jurisdiction: MT
tax_year: 2026
category: international
depends_on:
  - social-contributions-workflow-base
---

# Malta Social Security Contributions (SSC) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Malta (Republic of Malta) |
| Primary Legislation | Social Security Act, Chapter 318 |
| Supporting Legislation | Income Tax Act Article 14 (SSC deductibility); Income Tax Act Article 4C (TA22 regime) |
| Tax Authority | Department of Social Security (DSS), Malta |
| Rate Publisher | MTCA (publishes annual rate tables) |
| Self-employed rate | 15% of prior year net income (clamped to min/max) |
| SA minimum (2026) | EUR 1,881.36/year (EUR 36.18/week) |
| SC maximum, pre-1962 | EUR 3,825.12/year (EUR 73.56/week) |
| SC maximum, post-1962 | EUR 4,362.28/year (EUR 83.89/week) |
| Payment frequency | Quarterly |
| Payment method | Direct debit or bank transfer to DSS |
| Deadlines | Q1: 30 Apr, Q2: 31 Jul, Q3: 31 Oct, Q4: 31 Jan following year |
| Currency | EUR only |
| Contributor | Michael Cutajar, CPA (Warrant No. 125122), ACCA |
<<<<<<< HEAD
| Validated by | Michael Cutajar |
| Validation date | March 2026 |
=======
| Validated by | Pending — requires sign-off by a Maltese warranted accountant |
| Validation date | Pending |
>>>>>>> 70c2582 (Update accounting project files)

**Class overview:**

| Class | Who | Rate |
|---|---|---|
| Class 1 | Employees | 10% employee + 10% employer |
| Class 1A | Employers (maternity fund) | 0.3% of gross salary |
| Class 2 | Self-employed / Self-occupied | 15% of net income (clamped to min/max) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown birth year | STOP -- do not compute SSC without birth year |
| Unknown employment status | Assume Class 2 applies (self-employed) |
| Unknown prior year net income | Apply SA minimum (EUR 1,881.36) |
| First year or no TA24 filed | SA minimum applies |
| Unknown whether full-time employed | Ask -- do not assume Class 1 exemption |
| Unknown whether DSS debit is SSC or penalty | Classify as SSC; flag for reviewer |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- birth year and employment status. Without birth year, STOP. Do not compute SSC.

**Recommended** -- prior year net self-employment income (from filed TA24), number of years of self-employment, and whether a TA24 has been filed for the prior year.

**Ideal** -- DSS annual statement, bank statements showing quarterly SSC debits, prior year TA24 with Box 20 SSC deduction.

### Refusal catalogue

**R-MT-SSC-1 -- Birth year unknown.** *Trigger:* birth year not provided. *Message:* "Birth year is mandatory for SSC computation. The maximum contribution cap (SC) differs for persons born before vs on/after 1 January 1962. Cannot proceed without this information."

**R-MT-SSC-2 -- SSC arrears computation.** *Trigger:* client has unpaid SSC from prior years. *Message:* "SSC arrears are computed at current rates (not historical rates) for post-1962 clients, with 1% per month penalties compounding indefinitely. Do not attempt to quantify arrears without a DSS statement. Escalate to a warranted accountant immediately."

**R-MT-SSC-3 -- Disability or special exemptions.** *Trigger:* client claims disability exemption, student credited contributions, or pensioner pro-rata reduction. *Message:* "Exemptions and reduced rates for disability, students, and pensioners require case-specific confirmation from DSS. Escalate to a warranted accountant."

**R-MT-SSC-4 -- Group pension arrangements.** *Trigger:* client asks about group pension or occupational scheme interaction with SSC. *Message:* "Group pension arrangements and their interaction with statutory SSC are outside the scope of this skill. Escalate to a warranted accountant."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to social security. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. SSC payments always EXCLUDE from any VAT return or revenue/expense classification -- they are statutory personal obligations, not business supplies.

### 3.1 DSS quarterly debits (Class 2 self-employed)

| Pattern | Treatment | Notes |
|---|---|---|
| DSS, DEPARTMENT OF SOCIAL SECURITY | EXCLUDE -- SSC payment | Quarterly Class 2 direct debit or bank transfer |
| SOCIAL SECURITY, SOC SEC | EXCLUDE -- SSC payment | Same |
| SSC, S.S.C. | EXCLUDE -- SSC payment | Abbreviated reference |
| CLASS 2, CLASS TWO | EXCLUDE -- SSC payment | Explicit class reference |
| KONTRIBUZZJONI SOCJALI | EXCLUDE -- SSC payment | Maltese-language reference |

### 3.2 DSS debits appearing on specific Maltese banks

| Bank | Typical debit description | Treatment |
|---|---|---|
| BOV (Bank of Valletta) | "DSS DIRECT DEBIT" or "DEPT OF SOCIAL SECURITY" | EXCLUDE -- SSC |
| HSBC Malta | "DEPARTMENT OF SOCIAL SECURITY" or "DSS D/D" | EXCLUDE -- SSC |
| APS Bank | "DSS" or "SOC SECURITY CONTRIB" | EXCLUDE -- SSC |
| Lombard Bank | "SOCIAL SECURITY" | EXCLUDE -- SSC |
| Revolut / Wise | Rare -- DSS debits typically come from local Maltese accounts | If present, EXCLUDE |

### 3.3 Income tax payments (NOT SSC -- do not confuse)

| Pattern | Treatment | Notes |
|---|---|---|
| CFR, COMMISSIONER FOR REVENUE | EXCLUDE -- income tax, not SSC | Tax payment, not social security |
| INLAND REVENUE, IRD | EXCLUDE -- income tax | Same |
| FSS, FINAL SETTLEMENT SYSTEM | EXCLUDE -- employer PAYE/FSS | Not Class 2 SSC |
| PAYE, PAYER TAX | EXCLUDE -- employer withholding | Not Class 2 SSC |

### 3.4 Salary and payroll (exclude from SSC classification)

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, PAGA, WAGES (outgoing) | EXCLUDE -- payroll expense | Not an SSC payment |
| SALARY, PAGA (incoming) | EXCLUDE -- employment income received | Not an SSC payment |

### 3.5 Pension payments (received -- not SSC contributions)

| Pattern | Treatment | Notes |
|---|---|---|
| DSS PENSION, PENSJONI | EXCLUDE -- pension income received | Not a contribution payment |
| OLD AGE PENSION | EXCLUDE -- pension income | Not a contribution |

---

## Section 4 -- Worked examples

Six bank statement classifications showing SSC-related transactions from a hypothetical self-employed Maltese IT consultant.

### Example 1 -- Standard quarterly SSC debit (BOV)

**Input line:**
`30.04.2026 ; DEPT OF SOCIAL SECURITY ; DEBIT ; Q1 2026 CLASS 2 ; -470.34 ; EUR`

**Reasoning:**
Matches "DEPT OF SOCIAL SECURITY" (pattern 3.1). Amount EUR 470.34 = SA minimum quarterly (EUR 1,881.36 / 4). This is the Q1 2026 Class 2 contribution. Exclude from VAT classification. Record as SSC expense deductible in Box 20 of TA24.

**Classification:** EXCLUDE -- SSC payment. Deductible in TA24 Box 20.

### Example 2 -- Mid-range SSC quarterly debit (HSBC)

**Input line:**
`31.07.2026 ; DSS D/D ; DEBIT ; SOCIAL SECURITY CONTRIBUTION ; -750.00 ; EUR`

**Reasoning:**
Matches "DSS D/D" (pattern 3.2, HSBC). Amount EUR 750.00 = quarterly payment for SB category (EUR 3,000 annual / 4 = EUR 750). Implies prior year net income of EUR 20,000 (15% x EUR 20,000 = EUR 3,000). Exclude from VAT.

**Classification:** EXCLUDE -- SSC payment. Deductible in TA24 Box 20.

### Example 3 -- CFR tax payment (NOT SSC)

**Input line:**
`30.06.2026 ; COMMISSIONER FOR REVENUE ; DEBIT ; PT 2026 ; -1,200.00 ; EUR`

**Reasoning:**
Matches "COMMISSIONER FOR REVENUE" (pattern 3.3). This is a provisional tax payment, NOT an SSC payment. Do not classify as social security. Exclude from VAT. Not deductible as SSC in Box 20 -- this is income tax.

**Classification:** EXCLUDE -- income tax payment. NOT SSC.

### Example 4 -- Salary outgoing (employer payroll, not SSC)

**Input line:**
`28.04.2026 ; JOHN DOE SALARY APR ; DEBIT ; PAGA ; -1,800.00 ; EUR`

**Reasoning:**
Matches "PAGA" / salary pattern (3.4). This is a wage payment to an employee, not an SSC contribution. Class 1 employer contributions may also appear separately but are payroll costs, not the client's Class 2 SSC.

**Classification:** EXCLUDE -- payroll expense. NOT the client's Class 2 SSC.

### Example 5 -- Pension income received (not a contribution)

**Input line:**
`05.05.2026 ; DSS PENSION ; CREDIT ; OLD AGE PENSION MAY ; +680.00 ; EUR`

**Reasoning:**
Matches "DSS PENSION" (pattern 3.5). This is a pension benefit RECEIVED, not a contribution paid. Do not confuse inbound DSS credits with outbound SSC debits. Exclude from VAT. This is taxable income on the TA24, not a Box 20 deduction.

**Classification:** EXCLUDE from VAT. Taxable income (not an SSC deduction).

### Example 6 -- Ambiguous DSS debit (penalty or arrears)

**Input line:**
`15.09.2026 ; DEPARTMENT OF SOCIAL SECURITY ; DEBIT ; ARREARS PAYMENT ; -2,400.00 ; EUR`

**Reasoning:**
Matches "DEPARTMENT OF SOCIAL SECURITY" (pattern 3.1) but the amount is irregular and reference says "ARREARS PAYMENT." This could include penalties (1% per month) compounded on top of unpaid contributions. Cannot separate principal from penalty without a DSS statement. Flag for reviewer.

**Classification:** EXCLUDE from VAT. Flag for reviewer -- request DSS breakdown to split contribution principal (deductible in TA24 Box 20) from penalty (not deductible).

---

## Section 5 -- Tier 1 rules

These rules apply when bank statement data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- SSC formula

```
SSC = clamp(prior_year_net_income x 15%, SA_minimum, SC_maximum)
```

Where:
- SA minimum = EUR 1,881.36/year
- SC maximum (pre-1962) = EUR 3,825.12/year
- SC maximum (post-1962) = EUR 4,362.28/year

### Rule 2 -- Birth year determines ONLY the SC maximum

Born before 1 January 1962: SC maximum = EUR 3,825.12. Born on or after 1 January 1962: SC maximum = EUR 4,362.28. Birth year does NOT affect SA minimum or the 15% SB rate.

### Rule 3 -- SSC is based on PRIOR year net income

2026 SSC = based on 2025 net income from filed TA24. Not current year estimates.

### Rule 4 -- First year or no TA24 filed = SA minimum

First year of self-employment: SA minimum applies as a legislative provision, not just a default. No prior year TA24 filed: SA minimum applies until DSS assessment is made.

### Rule 5 -- Minimum always applies

Even at zero income, the SA minimum (EUR 1,881.36) is due once registered. There is no zero-SSC outcome.

### Rule 6 -- Full-time employed (Class 1) exempts from Class 2

If the client is a full-time employee paying Class 1 NIC, no Class 2 is due on side income. Class 1 covers everything.

### Rule 7 -- SSC is deductible in TA24 Box 20

SSC paid in Year X is deducted from income in Year X's TA24 (Box 20). This reduces taxable income before tax rate application.

### Rule 8 -- Payment schedule

| Quarter | Period | Due Date |
|---|---|---|
| Q1 | Jan -- Mar | 30 April |
| Q2 | Apr -- Jun | 31 July |
| Q3 | Jul -- Sep | 31 October |
| Q4 | Oct -- Dec | 31 January (following year) |

### Rule 9 -- Registration threshold

Self-employment income above EUR 910/year triggers SSC registration obligation. Below EUR 910 may be exempt but should still register.

### Rule 10 -- Maternity fund (Class 1A) does NOT apply to self-employed

Class 1A (0.3% of gross salary) is employer-only. Do not include in Class 2 calculations.

---

## Section 6 -- Tier 2 catalogue

When bank statement data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Dual status ambiguity (employed but also director)

**Trigger:** Client is a full-time employee but also a director of their own company drawing a director's fee.

**Issue:** Director fees from a company where the client is NOT a full-time employee may trigger Class 2. If the client is a full-time employee of the same or another company with Class 1 already paid, Class 2 is not due.

**Action:** Flag for reviewer. Confirm employment contract status and hours before advising.

### T2-2 -- TA22 client with multiple part-time income sources

**Trigger:** Client has two part-time self-employment activities, neither with full-time employment.

**Issue:** TA22 requires no full-time employment. If both activities are part-time and no full-time employment exists, Class 2 applies. Unclear whether one activity tips into full-time equivalence.

**Action:** Flag for reviewer.

### T2-3 -- Returning self-employed (previously stopped, now restarting)

**Trigger:** Client was self-employed before, stopped for several years, now restarting.

**Issue:** SA minimum does NOT automatically apply to returners. SA applies only to genuine first-timers. If no prior year TA24 for self-employment exists, SA applies until assessment.

**Action:** Flag for reviewer to confirm with DSS.

### T2-4 -- SSC arrears from prior years

**Trigger:** Client has unpaid SSC from previous years.

**Issue:** DSS can recover up to 5 years. Arrears are calculated at current rates (not historical rates) for post-1962 clients. 1% per month penalty compounds indefinitely.

**Action:** Do not attempt to quantify arrears without a DSS statement. Escalate to warranted accountant immediately.

### T2-5 -- Mid-year switch from employment to self-employment

**Trigger:** Client was employed until mid-year, then became self-employed.

**Issue:** Class 1 stops when employment ends. Class 2 starts when self-employment begins. First-year SA minimum applies for the self-employment period. Quarterly SSC payments due from the relevant quarter onward.

**Action:** Flag for reviewer to confirm start date and pro-rata application.

### T2-6 -- Students, pensioners, and disability exemptions

**Trigger:** Client may qualify for credited contributions, pro-rata reduced rate, or exemption.

**Issue:** These categories require case-specific DSS confirmation.

**Action:** Flag for reviewer. Do not apply exemptions without DSS confirmation.

---

## Section 7 -- Excel working paper template

When producing an SSC computation, structure the working paper as follows:

```
MALTA SSC COMPUTATION -- WORKING PAPER
Client: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Birth year:                    [____]
  Born on/after 1 Jan 1962:     [YES/NO]
  Employment status:             [Self-occupied / Self-employed / Dual]
  First year of self-employment: [YES/NO]
  Prior year net income (TA24):  EUR [____]
  TA24 filed for prior year:     [YES/NO]

COMPUTATION
  Rate:                          15%
  Gross SSC (15% x net income):  EUR [____]
  SA minimum:                    EUR 1,881.36
  SC maximum (pre/post-1962):    EUR [3,825.12 / 4,362.28]
  Annual SSC (clamped):          EUR [____]
  Quarterly SSC:                 EUR [____]
  Category applied:              [SA / SB / SC]

PAYMENT SCHEDULE
  Q1 (due 30 Apr):              EUR [____]
  Q2 (due 31 Jul):              EUR [____]
  Q3 (due 31 Oct):              EUR [____]
  Q4 (due 31 Jan):              EUR [____]

TA24 INTERACTION
  SSC paid in [year]:           EUR [____]
  Entered in TA24 Box 20:       EUR [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their tax impact]
```

---

## Section 8 -- Bank statement reading guide

### How SSC debits appear on Maltese bank statements

**BOV (Bank of Valletta):**
- Description: "DSS DIRECT DEBIT" or "DEPT OF SOCIAL SECURITY" or "DEPARTMENT OF SOCIAL SECURITY"
- Timing: End of month following quarter (30 Apr, 31 Jul, 31 Oct, 31 Jan)
- Amount: Quarterly figure (annual / 4)

**HSBC Malta:**
- Description: "DSS D/D" or "DEPARTMENT OF SOCIAL SECURITY" or "SOC SEC CONTRIB"
- Timing: Same quarterly cycle
- Amount: Quarterly figure

**APS Bank:**
- Description: "DSS" or "SOC SECURITY CONTRIB" or "SOCIAL SECURITY"
- Timing: Same quarterly cycle

**Key identification tips:**
1. SSC debits are always outgoing (DEBIT), never credits
2. They recur quarterly with consistent amounts (unless the client changed income bracket)
3. The amount should be divisible by 4 from a round annual figure, OR exactly EUR 470.34 (SA minimum quarterly)
4. Do not confuse with CFR/Inland Revenue debits (income tax) or FSS debits (employer PAYE)
5. Arrears payments may appear as irregular lump sums with "ARREARS" in the reference

---

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for DSS debits** -- identify all outgoing payments matching Section 3 patterns
2. **Sum annual SSC paid** -- total all DSS debits in the year
3. **Reverse-engineer the category:**
   - If total approximately EUR 1,881.36 -> SA minimum (income <= EUR 12,543.72 or first year)
   - If total between EUR 1,881.36 and EUR 3,825.12 -> SB (15% rate band)
   - If total approximately EUR 3,825.12 -> SC pre-1962 maximum
   - If total approximately EUR 4,362.28 -> SC post-1962 maximum
4. **Flag for reviewer:** "SSC classification derived from bank statement amounts only. Birth year and prior year income have not been independently verified. Reviewer must confirm before filing TA24 with Box 20 deduction."

---

## Section 10 -- Reference material

### Calculation examples (2026)

| Prior Year Net Income | Birth Year | Category | Annual SSC | Quarterly |
|---|---|---|---|---|
| EUR 8,000 | 1990 | SA | EUR 1,881.36 | EUR 470.34 |
| EUR 0 | 1990 | SA | EUR 1,881.36 | EUR 470.34 |
| EUR 20,000 | 1990 | SB | EUR 3,000.00 | EUR 750.00 |
| EUR 20,000 | 1955 | SB | EUR 3,000.00 | EUR 750.00 |
| EUR 50,000 | 1990 | SC (post-1962) | EUR 4,362.28 | EUR 1,090.57 |
| EUR 50,000 | 1955 | SC (pre-1962) | EUR 3,825.12 | EUR 956.28 |

### Self-occupied vs Self-employed

- Self-occupied: trades, businesses, professions (accountant, plumber, shop owner). Entitled to pension + short-term benefits (sickness, injury, maternity).
- Self-employed: income from rents, investments, capital gains. Entitled to pension only.
- Both pay the same 15% Class 2 rate with the same min/max caps.

### Penalties

| Penalty | Rate |
|---|---|
| Late payment | 1% per month on outstanding amount |
| Non-registration | All unpaid contributions + penalties |
| Arrears lookback | DSS can claim up to 5 years of unpaid SSC |
| Arrears rate (post-1962) | Calculated at CURRENT rates, not rates when originally due |

### Test suite

**Test 1:** Born 1985, prior year net income EUR 20,000, not first year. -> SB. Annual = EUR 3,000.00. Quarterly = EUR 750.00.

**Test 2:** Born 1958, prior year net income EUR 60,000, not first year. -> SC (pre-1962). Annual = EUR 3,825.12. Quarterly = EUR 956.28.

**Test 3:** Born 1975, prior year net income EUR 60,000, not first year. -> SC (post-1962). Annual = EUR 4,362.28. Quarterly = EUR 1,090.57.

**Test 4:** Born 1990, prior year net income EUR 5,000, not first year. -> SA. Annual = EUR 1,881.36. Quarterly = EUR 470.34.

**Test 5:** Born 1988, first year, no prior TA24. -> SA (first year). Annual = EUR 1,881.36. Quarterly = EUR 470.34.

**Test 6:** Full-time employee paying Class 1, side income EUR 8,000. -> NO Class 2 due. Class 1 covers all.

**Test 7:** Born 1992, registered self-employed, net income EUR 0. -> SA. Annual = EUR 1,881.36.

**Test 8:** Client paid EUR 3,000 SSC in 2025, preparing 2025 TA24. -> EUR 3,000 in Box 20.

### Prohibitions

- NEVER compute SSC without knowing the client's birth year
- NEVER use current year income -- SSC is always based on PRIOR year net income
- NEVER tell a client they owe zero SSC because their income is low -- minimum always applies once registered
- NEVER apply SA minimum to a returning self-employed without reviewer confirmation
- NEVER advise on SSC arrears without a DSS statement -- do not estimate
- NEVER conflate Class 1 and Class 2 -- they are entirely separate obligations
- NEVER include maternity fund (Class 1A) in Class 2 calculations
- NEVER present SSC figures as definitive -- always label as estimated and direct client to their DSS statement
- NEVER compute SSC penalties without escalating to a warranted accountant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
