---
name: ca-fed-cpp-ei
description: >
  Use this skill whenever asked about Canada Pension Plan (CPP) or Employment Insurance (EI) contributions for self-employed individuals. Trigger on phrases like "CPP self-employed", "Schedule 8", "CPP2", "YAMPE", "EI opt-in self-employed", "how much CPP do I pay", "self-employed EI benefits", "CPP contribution calculation", or any question about CPP/EI obligations for a self-employed sole proprietor or single-member entity in Canada. This skill covers CPP1 rates, CPP2 second ceiling, Schedule 8 computation, EI voluntary opt-in, tax treatment (line 22200 deduction and non-refundable credit), age exemptions, overpayment recovery, and edge cases. ALWAYS read this skill before touching any CPP/EI-related work.
version: 2.0
jurisdiction: CA-FED
tax_year: 2025
category: international
depends_on:
  - social-contributions-workflow-base
---

# Canada CPP/EI Self-Employed Skill v2.0

## Section 1 -- Quick reference

Read this whole section before computing anything.

| Field | Value |
|---|---|
| Country | Canada (Federal) |
| Jurisdiction Code | CA-FED |
| Primary Legislation | Canada Pension Plan Act (R.S.C., 1985, c. C-8); Employment Insurance Act (S.C. 1996, c. 23) |
| Supporting Legislation | Income Tax Act (R.S.C., 1985, c. 1 (5th Supp.)) -- line 22200 deduction, Schedule 8, non-refundable credits |
| Tax Authority | Canada Revenue Agency (CRA) |
| Tax Year | 2025 |
| Currency | CAD only |
| Filing Deadline | June 15 (self-employed), but PAYMENT due April 30 |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by Canadian CPA |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: CPP/CPP2 rate calculation, Schedule 8 mechanics, EI opt-in rules, tax treatment. Tier 2: mid-year status changes, partial-year contributions, Quebec QPP interactions. Tier 3: disability pension interactions, international social security agreements. |

**CPP1 thresholds (2025):**

| Item | Amount |
|---|---|
| Year's Maximum Pensionable Earnings (YMPE) | $71,300.00 |
| Year's Basic Exemption | $3,500.00 |
| Maximum contributory earnings (YMPE - exemption) | $67,800.00 |
| Employee rate | 5.95% |
| Self-employed rate (2x employee) | 11.90% |
| Maximum self-employed CPP1 contribution | $8,068.20 |

**CPP2 thresholds (2025):**

| Item | Amount |
|---|---|
| Year's Additional Maximum Pensionable Earnings (YAMPE) | $81,200.00 |
| Maximum additional contributory earnings (YAMPE - YMPE) | $9,900.00 |
| Employee CPP2 rate | 4.00% |
| Self-employed CPP2 rate (2x employee) | 8.00% |
| Maximum self-employed CPP2 contribution | $792.00 |

**EI thresholds (2025, outside Quebec):**

| Item | Amount |
|---|---|
| Maximum insurable earnings (MIE) | $65,700.00 |
| Self-employed premium rate | $1.64 per $100 (employee rate only, no employer portion) |
| Maximum annual premium (self-employed) | $1,077.48 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown province | Ontario (non-Quebec, CPP applies) |
| Unknown CPP pension status | Not receiving pension (contributions required) |
| Unknown EI opt-in status | Not opted in (no EI premiums) |
| Unknown T4 CPP already paid | $0 (full self-employed contribution required) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any CPP or EI figure, you MUST know:

1. Date of birth -- determines whether CPP contributions are required (age 18-70 range)
2. Province of residence -- Quebec residents use QPP, not CPP (this skill does NOT cover QPP)
3. Net self-employment income for the tax year -- CPP is based on current year, not prior year
4. Is the client also employed (T4 income)? -- employee CPP already paid reduces self-employed obligation
5. Has the client opted in to EI? -- EI is voluntary for self-employed
6. Is the client receiving a CPP disability or retirement pension? -- may affect contribution obligations
7. Did the client turn 18 or 70 during the tax year? -- pro-rata calculation required

If province is Quebec, STOP. This skill covers CPP only. QPP has different rates and thresholds.

### Refusal catalogue

**R-CA-CPP-1 -- Quebec resident.** Trigger: client resides in Quebec. Message: "Quebec Pension Plan (QPP) applies instead of CPP. QPP has different rates (6.40% employee / 12.80% self-employed for 2025). This skill does NOT cover QPP. Please escalate to a practitioner with QPP expertise."

**R-CA-CPP-2 -- Disability pension interaction.** Trigger: client receives a CPP disability pension and asks about contribution obligations or benefit impacts. Message: "CPP disability pension interactions with self-employment contributions are complex and outside this skill's scope. Please escalate to a licensed Canadian CPA."

**R-CA-CPP-3 -- International social security agreement.** Trigger: client asks about CPP credits under a bilateral social security agreement. Message: "International social security agreements require case-specific analysis. Please escalate to a licensed Canadian CPA familiar with treaty provisions."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement entries related to CPP and EI. Match by case-insensitive substring on the counterparty name or transaction description.

### 3.1 CRA payments (CPP/EI embedded in T1 balance owing)

| Pattern | Treatment | Notes |
|---|---|---|
| CRA, CANADA REVENUE AGENCY | T1 PAYMENT COMPONENT | Self-employed CPP/EI are not paid separately; rolled into T1 balance owing (line 42100) |
| RECEIVER GENERAL, REC GEN CANADA | T1 PAYMENT COMPONENT | Same as CRA -- instalment or balance owing payment |
| CRA INSTALMENT, QUARTERLY INSTALMENT | INSTALMENT PAYMENT | If net tax owing exceeds $3,000 in current AND prior years, quarterly instalments required (March 15, June 15, September 15, December 15) |
| CRA REFUND, TAX REFUND CRA | T1 REFUND | May include CPP overpayment refund (line 44800) |

### 3.2 EI-related payments (if opted in)

| Pattern | Treatment | Notes |
|---|---|---|
| SERVICE CANADA, ESDC | EI BENEFIT or REGISTRATION | Employment Insurance benefit payment or opt-in registration |
| EI MATERNITY, EI PARENTAL, EI SICKNESS | EI BENEFIT RECEIPT | Special benefits available to opted-in self-employed |

### 3.3 Provincial pension (Quebec -- refusal trigger)

| Pattern | Treatment | Notes |
|---|---|---|
| RRQ, RETRAITE QUEBEC, QPP | REFUSAL TRIGGER | Quebec Pension Plan -- fire R-CA-CPP-1 |

---

## Section 4 -- CPP eligibility and computation rules

### 4.1 CPP eligibility (Tier 1)

Legislation: Canada Pension Plan Act, s. 10

| Condition | CPP Obligation |
|---|---|
| Age 18 to 69 (inclusive) with net self-employment earnings > $3,500 | MUST contribute |
| Age 70 or older | EXEMPT -- no CPP contributions required |
| Under age 18 | EXEMPT -- no CPP contributions required |
| Receiving CPP retirement pension and age 60-64 | MUST contribute (mandatory since 2012) |
| Receiving CPP retirement pension and age 65-69 | MAY elect to stop contributing (file Form CPT30) |
| Receiving CPP disability pension | EXEMPT -- do not contribute |
| Net self-employment earnings <= $3,500 (basic exemption) | No CPP payable (earnings below floor) |

### 4.2 CPP1 computation (Tier 1)

```
pensionable_earnings = min(net_self_employment_income, $71,300) - $3,500
pensionable_earnings = max(pensionable_earnings, 0)
cpp1 = pensionable_earnings x 11.90%
cpp1 = min(cpp1, $8,068.20)
```

### 4.3 CPP2 computation (Tier 1)

Legislation: Canada Pension Plan Act (as amended by Bill C-97, 2024)

```
cpp2_earnings = min(net_self_employment_income, $81,200) - $71,300
cpp2_earnings = max(cpp2_earnings, 0)
cpp2 = cpp2_earnings x 8.00%
cpp2 = min(cpp2, $792.00)
```

### 4.4 Schedule 8 computation (Tier 1)

| Line | Description | Computation |
|---|---|---|
| Line 1 | Total CPP pensionable employment income (from T4 slips) | Sum of Box 26 from all T4s |
| Line 2 | CPP contributions deducted (from T4 slips) | Sum of Box 16 from all T4s |
| Line 3 | Net self-employment earnings | From line 12200 of T1 |
| Line 4 | Total pensionable earnings | Line 1 + Line 3 |
| Line 5 | Basic exemption | $3,500 (or pro-rated if partial year) |
| Line 6 | Maximum contributory earnings | min(Line 4, YMPE) - Line 5 |
| Line 7 | CPP contributions on self-employment | (Line 6 x 11.90%) - Line 2 |
| Line 8 | CPP2 additional contributions | Per Step 4.3 above |
| Line 9 | Total contributions payable | Line 7 + Line 8 |

Key rule: If the client also has T4 employment income with CPP already deducted, the employee CPP contributions (Line 2) are subtracted from the total obligation. If T4 CPP contributions already cover the maximum, self-employed CPP = $0.

### 4.5 Tax treatment of self-employed CPP (Tier 1)

Legislation: Income Tax Act, s. 60(e), s. 118.7

CPP1 split: Employer-equivalent half (50%) is a deduction from net income (line 22200). Employee-equivalent half (50%) is a non-refundable tax credit (line 30800, 15% federal credit).

CPP2 split: Employer-equivalent half (50%) is a deduction from net income (line 22215). Employee-equivalent half (50%) is a non-refundable tax credit (line 30800, 15% federal credit).

The deduction is more valuable at higher marginal rates. The credit is worth a flat 15% regardless of income.

### 4.6 EI for self-employed (Tier 1)

Legislation: Employment Insurance Act, Part VII.1, s. 152.07-152.21

EI is voluntary for self-employed. To opt in, register with Service Canada. 12-month waiting period before claiming benefits. Once benefits are claimed, cannot opt out. Self-employed EI covers SPECIAL BENEFITS ONLY (maternity, parental, sickness, compassionate care, family caregiver). It does NOT cover regular unemployment benefits.

```
ei_premium = min(net_self_employment_income, $65,700) x 1.64%
ei_premium = min(ei_premium, $1,077.48)
```

EI premiums are claimed as a non-refundable tax credit on line 31200 (15% federal credit).

---

## Section 5 -- Age exemptions and pro-rata rules

Legislation: Canada Pension Plan Act, s. 12, s. 13

| Age Event | CPP Treatment | EI Treatment |
|---|---|---|
| Turn 18 during the year | Contribute from month after 18th birthday | No age restriction |
| Age 18-69 all year | Full year contributions | Full year EI (if opted in) |
| Turn 70 during the year | Contribute up to and including month of 70th birthday | No age restriction |
| Age 70+ at start of year | NO CPP contributions | EI still available (if opted in) |
| Under 18 all year | NO CPP contributions | No age restriction |

Pro-rata basic exemption when turning 18 or 70 during the year:

```
pro_rata_exemption = ($3,500 / 12) x number_of_contributory_months
```

---

## Section 6 -- Overpayment recovery and filing

### 6.1 Overpayment recovery (Tier 1)

Legislation: Income Tax Act, s. 118.7

| Overpayment Type | How Recovered |
|---|---|
| CPP overpayment (employee contributions from T4s exceed maximum) | Claimed on line 44800 of T1 as refundable credit |
| CPP2 overpayment | Claimed on line 44801 of T1 as refundable credit |
| EI overpayment (multiple T4s) | Claimed on line 45000 of T1 as refundable credit |

### 6.2 Payment and filing (Tier 1)

| Requirement | Detail |
|---|---|
| How CPP is paid | Added to balance owing on T1 return (line 42100) |
| Filing deadline | June 15 (self-employed), but PAYMENT due April 30 |
| Instalment requirements | If net tax owing exceeds $3,000 ($1,800 in Quebec) in current year AND either of the two prior years |
| Instalment dates | March 15, June 15, September 15, December 15 |
| Interest on late payment | Prescribed rate set quarterly by CRA, compounded daily |

CPP and EI are NOT paid separately by self-employed individuals. They are calculated on Schedule 8 and rolled into the T1 balance owing.

---

## Section 7 -- Edge case registry

### EC1 -- Client turns 70 mid-year (Tier 1)
Situation: Client's 70th birthday is in July 2025.
Resolution: CPP contributions required January through July (7 months). Pro-rate the basic exemption: ($3,500 / 12) x 7 = $2,041.67. Schedule 8 handles the pro-rata calculation.

### EC2 -- Client receiving CPP retirement pension, age 65-69 (Tier 2)
Situation: Client started CPP retirement pension at 65 and continues to be self-employed.
Resolution: Contributions are optional for ages 65-69 if receiving CPP retirement. Client must file Form CPT30 to elect to stop contributing. If no CPT30 filed, contributions are required. Flag for reviewer -- confirm pension status and whether CPT30 has been filed.

### EC3 -- Quebec resident (Tier 3)
Situation: Client resides in Quebec.
Resolution: QPP applies instead of CPP. QPP has different rates (6.40% employee / 12.80% self-employed for 2025). This skill does NOT cover QPP. Escalate to practitioner with QPP expertise.

### EC4 -- Self-employed EI opt-in within first 12 months (Tier 1)
Situation: Client opted in to EI in August 2025, wants to claim maternity benefits in January 2026.
Resolution: 12-month waiting period applies. Client cannot claim benefits until August 2026. Premiums are still due for August-December 2025.

### EC5 -- Net self-employment loss (Tier 1)
Situation: Client has a net self-employment loss (negative income).
Resolution: No CPP contributions are payable on a loss. Pensionable earnings = $0. Unlike Malta SSC, there is NO minimum CPP contribution.

### EC6 -- Religious exemption (Tier 2)
Situation: Client is a member of a religious group that has an approved exemption from CPP.
Resolution: Form CPT17 must have been filed and approved. Flag for reviewer -- confirm exemption status with CRA before excluding CPP.

### EC7 -- Non-resident self-employed in Canada (Tier 2)
Situation: Client is a non-resident of Canada earning self-employment income from Canadian sources.
Resolution: CPP may still apply if the work is performed in Canada, regardless of residence. Flag for reviewer -- confirm whether the Canada-source self-employment triggers CPP obligations.

### EC8 -- EI opt-out after opting in but before claiming (Tier 1)
Situation: Client opted in to EI for self-employed in 2024, has not claimed benefits, wants to opt out.
Resolution: Client may opt out by December 31 of the current year if NO benefits have been claimed. Premiums paid for the opt-in year are refundable. Once any benefit has been claimed, the client cannot opt out.

---

## Section 8 -- Reviewer escalation protocol

When a Tier 2 situation is identified:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Licensed Canadian CPA must confirm before advising client.
```

When a Tier 3 situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed Canadian CPA. Document gap.
```

---

## Section 9 -- Test suite

### Test 1 -- Standard self-employed, mid-range income
Input: Born 1985, Ontario resident, net self-employment income $50,000, no T4 income, no EI opt-in.
Expected output: CPP1 = ($50,000 - $3,500) x 11.90% = $5,533.50. CPP2 = $0 (below YMPE). EI = $0 (not opted in). Line 22200 deduction = $2,766.75. Line 30800 credit base = $2,766.75.

### Test 2 -- High-income, both ceilings hit
Input: Born 1978, Alberta resident, net self-employment income $120,000, no T4 income.
Expected output: CPP1 = $8,068.20 (capped). CPP2 = $792.00 (capped). Total CPP = $8,860.20. Line 22200 deduction = $4,430.10. Line 30800 credit base = $4,430.10.

### Test 3 -- Income between YMPE and YAMPE
Input: Born 1990, BC resident, net self-employment income $75,000, no T4 income.
Expected output: CPP1 = $8,068.20 (capped at YMPE). CPP2 = ($75,000 - $71,300) x 8.00% = $296.00. Total CPP = $8,364.20.

### Test 4 -- Below basic exemption
Input: Born 1992, Ontario resident, net self-employment income $2,500.
Expected output: CPP = $0.00 (below $3,500 basic exemption). No Schedule 8 contribution.

### Test 5 -- Self-employed with T4 employment income
Input: Born 1988, Ontario, T4 pensionable earnings $45,000, T4 CPP deducted $2,468.25, net self-employment income $40,000.
Expected output: Combined pensionable earnings exceed YMPE. Self-employed CPP on Schedule 8 = $8,068.20 - $2,468.25 (employee) - $2,468.25 (deemed employer) = $3,131.70.

### Test 6 -- EI opt-in calculation
Input: Opted-in self-employed, Ontario, net self-employment income $50,000.
Expected output: EI premium = $50,000 x 1.64% = $820.00. Below maximum of $1,077.48.

### Test 7 -- Age 72, self-employed
Input: Born 1953, net self-employment income $80,000.
Expected output: CPP = $0.00 (age 70+ exemption). No Schedule 8 required for CPP.

### Test 8 -- Net loss
Input: Born 1985, net self-employment loss of ($5,000).
Expected output: CPP = $0.00. No minimum contribution. No Schedule 8 obligation.

---

## Section 10 -- Prohibitions and disclaimer

### Prohibitions

- NEVER compute CPP for Quebec residents -- QPP applies, not CPP
- NEVER tell a self-employed client they must pay EI -- it is voluntary
- NEVER forget to split CPP into deduction (line 22200) and credit (line 30800) -- both halves must be claimed
- NEVER apply CPP to a client aged 70 or over at the start of the year
- NEVER ignore T4 CPP already deducted when computing self-employed CPP on Schedule 8
- NEVER present CPP2 as optional -- it is mandatory for earnings above YMPE
- NEVER combine CPP and EI into a single figure without showing the breakdown
- NEVER advise on QPP rates using CPP figures -- they are different
- NEVER state that self-employed EI covers regular (unemployment) benefits -- it covers special benefits only
- NEVER compute figures without confirming the tax year -- rates change annually

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
