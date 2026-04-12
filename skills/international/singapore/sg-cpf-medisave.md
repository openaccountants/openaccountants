---
name: sg-cpf-medisave
description: >
  Use this skill whenever asked about Singapore CPF MediSave contributions for self-employed persons (SEPs). Trigger on phrases like "MediSave contribution", "CPF self-employed", "how much MediSave do I pay", "net trade income CPF", "voluntary CPF contributions", "BHS", "Basic Healthcare Sum", "MediShield Life", or any question about MediSave obligations for a self-employed client in Singapore. This skill covers mandatory MediSave rates by age, contribution caps, voluntary CPF contributions, tax relief, payment deadlines, penalties, and edge cases. ALWAYS read this skill before touching any Singapore CPF/MediSave-related work.
version: 2.0
jurisdiction: SG
tax_year: 2025
category: international
---

# Singapore CPF MediSave Contributions -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

Read this whole section before computing anything.

| Field | Value |
|---|---|
| Country | Singapore |
| Jurisdiction Code | SG |
| Primary Legislation | Central Provident Fund Act (Cap. 36) |
| Supporting Legislation | Income Tax Act (Cap. 134); MediShield Life Scheme Act 2015 |
| Tax Authority | Central Provident Fund Board (CPFB); Inland Revenue Authority of Singapore (IRAS) |
| Tax Year | 2025 (Year of Assessment 2026) |
| Currency | SGD only |
| MediSave Trigger Threshold | NTI > S$6,000 |
| CPF Annual Limit | S$37,740 (2025) |
| Basic Healthcare Sum (BHS) | S$75,500 (2025, for members turning 65 that year) |
| Contributor | Open Accountants |
| Validated By | Pending -- licensed Singapore practitioner sign-off required |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: rate calculation, contribution cap, payment deadline, voluntary CPF relief. Tier 2: dual employment/self-employment, partial year, platform worker exclusions. Tier 3: hardship appeals, contribution refunds, cross-border employment. |

**MediSave rates by age (NTI > S$18,000, full rate):**

| Age as at 1 Jan | MediSave Rate |
|---|---|
| Below 35 | 8.00% of NTI |
| 35 to below 45 | 9.00% of NTI |
| 45 to below 50 | 10.00% of NTI |
| 50 and above | 10.50% of NTI |

**MediSave rates by age (NTI > S$6,000 to S$12,000, lower rate):**

| Age as at 1 Jan | MediSave Rate |
|---|---|
| Below 35 | 4.00% of NTI |
| 35 to below 45 | 4.50% of NTI |
| 45 to below 50 | 5.00% of NTI |
| 50 and above | 5.25% of NTI |

NTI between S$12,001 and S$18,000: graduated rate between lower and full rate. Use CPFB calculator.

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown age | Use highest rate band (50 and above, 10.50%) |
| Unknown NTI tier | Assume NTI > S$18,000 (full rate applies) |
| Unknown CPF headroom | Assume no employee CPF contributions (full Annual Limit available) |
| Unknown BHS status | Assume MediSave Account below BHS |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any MediSave figure, you MUST know:

1. Age as at 1 January of the contribution year -- determines the MediSave contribution rate band
2. Net Trade Income (NTI) for the year -- assessable income from IRAS Form B
3. Is the person a Singapore Citizen or Permanent Resident? -- only SC/PR are obligated
4. Is NTI above S$6,000? -- mandatory MediSave only triggers above this threshold
5. Is the person also an employee with employer CPF contributions? -- affects CPF Annual Limit headroom
6. Has the person received their Notice of Assessment (NOA)? -- MediSave is due 30 days after NOA

If NTI is unknown or the NOA has not been issued, note that MediSave cannot be finalised. Provide estimates only.

### Refusal catalogue

**R-SG-CPF-1 -- Hardship appeal.** Trigger: client asks about reducing or waiving MediSave contributions due to financial hardship. Message: "MediSave contribution hardship appeals are handled directly by CPFB. This skill cannot advise on appeal procedures. Please contact CPFB at 1800-227-1188."

**R-SG-CPF-2 -- Contribution refund.** Trigger: client asks about refunding MediSave contributions already paid. Message: "MediSave contribution refunds are governed by CPFB policy and outside this skill's scope. Please escalate to a licensed Singapore practitioner."

**R-SG-CPF-3 -- Cross-border employment.** Trigger: client asks about CPF obligations while working across Singapore and another jurisdiction simultaneously. Message: "Cross-border CPF obligations require case-specific analysis. Please escalate to a licensed Singapore practitioner."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement entries related to CPF/MediSave. Match by case-insensitive substring on the counterparty name or transaction description.

### 3.1 CPF Board payments (mandatory MediSave)

| Pattern | Treatment | Notes |
|---|---|---|
| CPFB, CPF BOARD, CENTRAL PROVIDENT FUND | MEDISAVE PAYMENT | Mandatory MediSave contribution -- verify against NOA amount |
| GIRO CPF, GIRO-CPF | MEDISAVE PAYMENT (GIRO) | Auto-debit for MediSave contribution |
| CPF VOLUNTARY, CPF TOP-UP | VOLUNTARY CPF CONTRIBUTION | Voluntary contribution to OA/SA/MA -- tax-deductible |

### 3.2 IRAS-related (triggers MediSave obligation)

| Pattern | Treatment | Notes |
|---|---|---|
| IRAS, INLAND REVENUE | INCOME TAX PAYMENT | Separate from MediSave; but NOA triggers MediSave deadline |
| IRAS NOA, NOTICE OF ASSESSMENT | DEADLINE TRIGGER | MediSave due 30 days from this date |

### 3.3 MediShield Life premium deductions

| Pattern | Treatment | Notes |
|---|---|---|
| MEDISHIELD, MEDISHIELD LIFE | EXCLUDE from MediSave computation | Premium deducted from MediSave Account balance, not a separate contribution |
| INTEGRATED SHIELD, AIA HEALTHSHIELD, PRUDENTIAL PRUSHIELD | EXCLUDE | Private insurer on top of MediShield Life -- paid from MA |

### 3.4 Platform worker CPF (separate from traditional MediSave)

| Pattern | Treatment | Notes |
|---|---|---|
| GRAB, DELIVEROO, GOJEK, FOODPANDA | FLAG FOR REVIEW | From work year 2025, platform worker income excluded from NTI for MediSave; separate CPF rules apply |

---

## Section 4 -- MediSave computation rules

### 4.1 Determine obligation (Tier 1)

Legislation: Central Provident Fund Act (Cap. 36), Section 9A

| Condition | Obligation |
|---|---|
| SEP, SC/PR, NTI > S$6,000 | Mandatory MediSave contribution |
| SEP, NTI <= S$6,000 | No mandatory MediSave (voluntary allowed) |
| SEP who is also an employee | Mandatory MediSave on NTI still applies; total CPF capped at Annual Limit |

Definition of SEP: a person who earns trade, business, profession, or vocation income and is not an employee in respect of that income. Includes sole proprietors, freelancers, commission agents, taxi drivers, hawkers, and professionals.

Platform workers (from work year 2025): net earnings from platform work are excluded from NTI for MediSave computation and subject to separate CPF rules. Flag if client has platform work income.

### 4.2 NTI computation (Tier 1)

```
Net Trade Income (NTI) = Gross Trade Income - Allowable Business Expenses - Capital Allowances
```

Source: assessable income reported in IRAS Form B. NTI is determined by IRAS after assessment. MediSave is computed on assessed NTI, not self-reported estimates.

### 4.3 Rate application (Tier 1 / Tier 2 for graduated band)

For NTI > S$18,000: apply full rate per age band.
For NTI > S$6,000 to S$12,000: apply lower rate per age band.
For NTI > S$12,000 to S$18,000: use CPFB Self-Employed MediSave Contribution Calculator. Do not interpolate manually.

The contribution is calculated on the full NTI, not just the portion above S$6,000.

### 4.4 Contribution caps (Tier 1)

CPF Annual Limit of S$37,740 is the maximum total CPF contributions in a calendar year (mandatory + voluntary, employer + employee + self-employed).

If also an employee: mandatory employer + employee CPF count toward the limit. MediSave on top, but total cannot exceed Annual Limit.

BHS of S$75,500 caps the MediSave Account balance. Once MA reaches BHS, excess flows to SA first, then OA. The SEP does not get an exemption from contributing -- the contribution is still computed, but overflow is redirected.

---

## Section 5 -- Payment schedule and penalties

### 5.1 Payment deadline (Tier 1)

| Item | Detail |
|---|---|
| Trigger | IRAS issues Notice of Assessment (NOA) |
| Deadline | 30 days from the date of the NOA |
| Payment methods | GIRO (recommended), PayNow, AXS, internet banking, CPF Service Centres |
| Instalment plan | Available upon request to CPFB -- typically up to 12 monthly instalments |

The MediSave payment deadline is the same as the income tax payment deadline -- 30 days from NOA.

### 5.2 Penalties for non-contribution (Tier 1)

| Penalty | Detail |
|---|---|
| Late payment interest | 1.5% per month (18% per annum) on outstanding contributions |
| Enforcement | CPFB may issue demand notice, followed by legal proceedings |
| Court action | CPFB can recover through courts |
| Criminal liability | Fine up to S$5,000 |
| Travel restriction | CPFB may request Controller of Immigration to prevent departure |

WARNING: MediSave late payment interest at 1.5% per month (18% p.a.) is severe. Advise clients to pay on time or apply for instalment plans before the deadline.

---

## Section 6 -- Voluntary CPF contributions and tax relief

### 6.1 Voluntary contributions (Tier 1)

Legislation: Central Provident Fund Act (Cap. 36); Income Tax Act (Cap. 134)

SEPs may make voluntary contributions to OA + SA + MA in addition to mandatory MediSave. Voluntary contributions are allocated across OA, SA, and MA according to the same age-based allocation ratios as employees.

### 6.2 Tax relief (Tier 1)

| Item | Detail |
|---|---|
| Relief type | CPF Relief for Self-Employed (Section 39 ITA) |
| Maximum relief | Lower of: (a) 37% of NTI, (b) CPF Annual Limit of S$37,740, or (c) actual contributions |
| Mandatory MediSave | Fully deductible as CPF relief (no separate cap) |
| Voluntary contributions | Deductible up to cap above, AFTER mandatory MediSave is accounted for |
| Overall personal relief cap | S$80,000 total across ALL personal reliefs |
| Condition | No CPF relief if NTI is zero or negative |

CPF relief is automatically included in the tax return based on data from CPFB to IRAS. Contributions must be made by 31 December to qualify for that YA.

### 6.3 MediShield Life interaction (Tier 1)

MediShield Life is a mandatory basic health insurance plan for all SC/PR. Premiums are payable from the MediSave Account. The SEP must ensure sufficient MediSave balance to cover premiums. Integrated Shield Plans (private) can also be paid from MediSave up to Additional Withdrawal Limits.

---

## Section 7 -- Edge case registry

### EC1 -- SEP with NTI exactly S$6,000 (Tier 1)
Situation: Client's assessed NTI is exactly S$6,000.
Resolution: No mandatory MediSave contribution. Threshold is "more than S$6,000", not "S$6,000 or more". Voluntary contributions are still permitted.

### EC2 -- SEP who is also an employee (Tier 2)
Situation: Client works part-time as an employee and also has self-employment income.
Resolution: Mandatory MediSave on NTI still applies. Total CPF (employer + employee + SEP MediSave + voluntary) cannot exceed Annual Limit of S$37,740. Flag for reviewer to verify total CPF headroom.

### EC3 -- NTI in graduated band (S$12,001 to S$18,000) (Tier 1)
Situation: Client's NTI falls in the graduated rate band.
Resolution: Use the CPFB Self-Employed MediSave Contribution Calculator. Do not interpolate manually.

### EC4 -- MediSave Account already at BHS (Tier 1)
Situation: Client's MediSave Account balance has reached the BHS.
Resolution: Mandatory MediSave contributions are still computed on NTI, but contributions in excess of BHS flow to SA first, then OA. The SEP does not get an exemption.

### EC5 -- First year of self-employment, NOA not yet issued (Tier 1)
Situation: Client started self-employment mid-year and has not yet received an NOA.
Resolution: MediSave is only due after IRAS issues the NOA. No advance payment required. Advise client to set aside estimated MediSave for cash flow planning.

### EC6 -- SEP turning 55 during the year (Tier 2)
Situation: Client turns 55 during the contribution year.
Resolution: Age for MediSave rate purposes is measured as at 1 January. The rate does not change mid-year. Voluntary CPF allocation ratios may shift. Flag for reviewer.

### EC7 -- Foreign-sourced self-employment income (Tier 2)
Situation: Client earns self-employment income from overseas sources.
Resolution: MediSave is based on NTI as assessed by IRAS. If income is taxable in Singapore and included in Form B, it forms part of NTI. Flag for reviewer.

### EC8 -- Platform worker with mixed income (Tier 2)
Situation: Client earns from both platform work and traditional self-employment.
Resolution: From work year 2025, net platform work earnings excluded from NTI for MediSave. Only traditional self-employment income triggers mandatory MediSave. Flag for reviewer.

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
Action Required: Licensed Singapore practitioner must confirm before advising client.
```

When a Tier 3 situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed practitioner. Document gap.
```

---

## Section 9 -- Test suite

### Test 1 -- Standard SEP, age 30, NTI above S$18,000
Input: Age 30 (as at 1 Jan 2025), NTI = S$50,000.
Expected output: Rate = 8.00%. MediSave = S$4,000.00. Below CPF Annual Limit. No cap issue.

### Test 2 -- SEP, age 40, NTI above S$18,000
Input: Age 40 (as at 1 Jan 2025), NTI = S$80,000.
Expected output: Rate = 9.00%. MediSave = S$7,200.00. Below CPF Annual Limit. No cap issue.

### Test 3 -- SEP, age 48, NTI above S$18,000
Input: Age 48 (as at 1 Jan 2025), NTI = S$60,000.
Expected output: Rate = 10.00%. MediSave = S$6,000.00. Below CPF Annual Limit. No cap issue.

### Test 4 -- SEP, age 55, NTI above S$18,000
Input: Age 55 (as at 1 Jan 2025), NTI = S$40,000.
Expected output: Rate = 10.50%. MediSave = S$4,200.00. Below CPF Annual Limit. No cap issue.

### Test 5 -- NTI exactly S$6,000
Input: Age 30, NTI = S$6,000.
Expected output: No mandatory MediSave. Threshold is "more than S$6,000".

### Test 6 -- NTI in Tier B (S$6,001 to S$12,000)
Input: Age 30, NTI = S$10,000.
Expected output: Rate = 4.00%. MediSave = S$400.00.

### Test 7 -- NTI in graduated band
Input: Age 30, NTI = S$15,000.
Expected output: Use CPFB calculator. Rate is between 4.00% and 8.00% (graduated). Do not compute manually.

### Test 8 -- Voluntary CPF tax relief
Input: Age 35, NTI = S$100,000. Mandatory MediSave = S$9,000 (9%). Voluntary CPF contribution = S$30,000.
Expected output: Total CPF = S$39,000. Exceeds Annual Limit of S$37,740. Cap at S$37,740. Tax relief = S$37,000 (37% of NTI). Actual relief limited to S$37,740 (lower of 37% NTI and Annual Limit). Maximum additional voluntary = S$28,740.

---

## Section 10 -- Prohibitions and disclaimer

### Prohibitions

- NEVER compute MediSave without knowing the client's age as at 1 January of the contribution year
- NEVER use estimated income for final MediSave computation -- MediSave is based on IRAS-assessed NTI
- NEVER tell a client they owe no MediSave without confirming NTI is S$6,000 or below
- NEVER manually interpolate the graduated rate band (S$12,001 to S$18,000) -- use the CPFB calculator
- NEVER advise that MediSave is optional once NTI exceeds S$6,000 -- it is mandatory
- NEVER ignore the CPF Annual Limit when computing total CPF contributions
- NEVER conflate BHS (MediSave Account balance cap) with CPF Annual Limit (contribution cap)
- NEVER include platform worker income in NTI for MediSave from work year 2025 onward without review
- NEVER present MediSave figures as definitive -- always label as estimated and direct client to their CPFB contribution notice
- NEVER advise on MediSave penalties without escalating to a licensed practitioner

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
