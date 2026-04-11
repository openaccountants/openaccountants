---
name: sg-cpf-medisave
description: Use this skill whenever asked about Singapore CPF MediSave contributions for self-employed persons (SEPs). Trigger on phrases like "MediSave contribution", "CPF self-employed", "how much MediSave do I pay", "net trade income CPF", "voluntary CPF contributions", "BHS", "Basic Healthcare Sum", "MediShield Life", or any question about MediSave obligations for a self-employed client in Singapore. This skill covers mandatory MediSave rates by age, contribution caps, voluntary CPF contributions, tax relief, payment deadlines, penalties, and edge cases. ALWAYS read this skill before touching any Singapore CPF/MediSave-related work.
---

# Singapore CPF MediSave Contributions -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Singapore |
| Jurisdiction Code | SG |
| Primary Legislation | Central Provident Fund Act (Cap. 36) |
| Supporting Legislation | Income Tax Act (Cap. 134); MediShield Life Scheme Act 2015 |
| Tax Authority | Central Provident Fund Board (CPFB); Inland Revenue Authority of Singapore (IRAS) |
| Rate Publisher | CPFB (publishes annual MediSave rate tables) |
| Contributor | Open Accountants |
| Validated By | Pending -- licensed Singapore practitioner sign-off required |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate calculation, contribution cap, payment deadline, voluntary CPF relief. Tier 2: dual employment/self-employment, partial year, platform worker exclusions. Tier 3: hardship appeals, contribution refunds, cross-border employment. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Licensed practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any MediSave figure, you MUST know:

1. **Age as at 1 January of the contribution year** [T1] -- determines the MediSave contribution rate band
2. **Net Trade Income (NTI) for the year** [T1] -- assessable income from IRAS Form B (self-employment section)
3. **Is the person a Singapore Citizen or Permanent Resident?** [T1] -- only SC/PR are obligated
4. **Is NTI above S$6,000?** [T1] -- mandatory MediSave only triggers above this threshold
5. **Is the person also an employee with employer CPF contributions?** [T2] -- affects CPF Annual Limit headroom
6. **Has the person received their Notice of Assessment (NOA)?** [T1] -- MediSave is due 30 days after NOA

**If NTI is unknown or the NOA has not been issued, note that MediSave cannot be finalised. Provide estimates only.**

---

## Step 1: Determine Obligation [T1]

**Legislation:** Central Provident Fund Act (Cap. 36), Section 9A

| Condition | Obligation |
|-----------|------------|
| Self-employed person (SEP), SC/PR, NTI > S$6,000 | Mandatory MediSave contribution |
| Self-employed person, NTI <= S$6,000 | No mandatory MediSave (voluntary contributions allowed) |
| SEP who is also an employee | Mandatory MediSave on NTI still applies; total CPF capped at Annual Limit |

**Definition of Self-Employed Person (SEP):** A person who earns trade, business, profession, or vocation income and is not an employee in respect of that income. Includes sole proprietors, freelancers, commission agents, taxi drivers, hawkers, and professionals in private practice.

**Platform workers (from work year 2025):** Net earnings from platform work are excluded from NTI for MediSave computation purposes and are subject to separate CPF rules. [T2] flag if client has platform work income.

---

## Step 2: MediSave Contribution Rates by Age [T1]

**Legislation:** Central Provident Fund Act (Cap. 36); CPFB MediSave Rate Table 2025

MediSave contribution rates are based on age as at 1 January of the contribution year and NTI. There are three income tiers:

### Tier A: NTI > S$18,000 (full rate applies)

| Age as at 1 Jan | MediSave Rate |
|-----------------|---------------|
| Below 35 | 8.00% of NTI |
| 35 to below 45 | 9.00% of NTI |
| 45 to below 50 | 10.00% of NTI |
| 50 and above | 10.50% of NTI |

### Tier B: NTI > S$6,000 to S$12,000 (lower rate applies)

| Age as at 1 Jan | MediSave Rate |
|-----------------|---------------|
| Below 35 | 4.00% of NTI |
| 35 to below 45 | 4.50% of NTI |
| 45 to below 50 | 5.00% of NTI |
| 50 and above | 5.25% of NTI |

### Tier C: NTI > S$12,000 to S$18,000 (graduated rate)

The rate is graduated between the Tier B and Tier A rates. The contribution is calculated using the formula on CPFB's rate table or calculator. In practice, use the CPFB Self-Employed MediSave Contribution Calculator for exact figures in this band.

### Important Notes

- The contribution is calculated on the **full NTI**, not just the portion above S$6,000.
- The contribution is subject to the **CPF Annual Limit** (see Step 3).
- The contribution is also subject to the **Basic Healthcare Sum** (BHS) cap on the MediSave Account balance.
- **Use the official CPFB calculator** for NTI between S$12,001 and S$18,000 -- the graduated formula is complex.

---

## Step 3: Contribution Caps [T1]

**Legislation:** Central Provident Fund Act (Cap. 36); CPFB Annual Limit and BHS announcements

### CPF Annual Limit

| Year | CPF Annual Limit |
|------|-----------------|
| 2025 | S$37,740 |

The CPF Annual Limit is the maximum total CPF contributions (mandatory + voluntary, employer + employee + self-employed) that can be made in a calendar year. This applies across ALL CPF accounts (Ordinary, Special, MediSave).

**If the person is also an employee:** The mandatory employer + employee CPF contributions count toward the S$37,740 limit. MediSave contributions as an SEP are on top, but total CPF must not exceed the Annual Limit.

### Basic Healthcare Sum (BHS)

| Year | BHS (for members turning 65 in that year) |
|------|------------------------------------------|
| 2025 | S$75,500 |

- The BHS is the cap on the MediSave Account (MA) balance. Once the MA reaches the BHS, no further MediSave contributions are required.
- For members below 65, the BHS is adjusted yearly. For members who have turned 65, the BHS is fixed for life at their cohort's amount.
- The BHS is NOT a minimum -- members with less than the BHS are not required to top up.
- If mandatory MediSave would push the MA above the BHS, the excess is allocated to the Special Account (SA) first, then Ordinary Account (OA), subject to the CPF Annual Limit.

---

## Step 4: Net Trade Income Computation [T1]

**Legislation:** Income Tax Act (Cap. 134); CPFB guidelines

### Formula
```
Net Trade Income (NTI) = Gross Trade Income - Allowable Business Expenses - Capital Allowances
```

| Component | Detail |
|-----------|--------|
| Source | Assessable income reported in IRAS Form B (Trade, Business, Profession or Vocation section) |
| Gross trade income | Revenue from self-employment activities |
| Allowable deductions | Business expenses wholly and exclusively incurred in the production of income |
| Capital allowances | As per Income Tax Act provisions |
| Losses | If NTI is negative or <= S$6,000, no mandatory MediSave is due |

**NTI is determined by IRAS after assessment. The MediSave contribution is computed on the assessed NTI, not self-reported estimates.**

---

## Step 5: Payment Schedule and Deadline [T1]

**Legislation:** Central Provident Fund Act (Cap. 36), Section 9A

| Item | Detail |
|------|--------|
| Trigger | IRAS issues Notice of Assessment (NOA) for the Year of Assessment |
| Deadline | **30 days from the date of the NOA** |
| Payment method | GIRO (recommended), PayNow, AXS, internet banking, or at CPF Service Centres |
| Instalment plan | Available upon request to CPFB -- typically up to 12 monthly instalments |

**The MediSave payment deadline is the same as the income tax payment deadline -- 30 days from NOA.**

CPFB will send a MediSave contribution notice separately from the IRAS NOA. Both must be paid within 30 days.

---

## Step 6: Penalties for Non-Contribution [T1]

**Legislation:** Central Provident Fund Act (Cap. 36), Sections 9A and 61

| Penalty | Detail |
|---------|--------|
| Late payment interest | 1.5% per month (18% per annum) on outstanding MediSave contributions |
| Enforcement | CPFB may issue a demand notice, followed by legal proceedings |
| Court action | CPFB can recover unpaid contributions through the courts |
| Criminal liability | Failure to contribute is an offence; conviction can result in a fine of up to S$5,000 |
| Travel restriction | CPFB may request the Controller of Immigration to prevent the SEP from leaving Singapore until contributions are paid |

**WARNING:** Unlike income tax penalties, MediSave late payment interest at 1.5% per month (18% p.a.) is severe and compounds. Advise clients to pay on time or apply for instalment plans before the deadline.

---

## Step 7: Voluntary CPF Contributions [T1]

**Legislation:** Central Provident Fund Act (Cap. 36); Income Tax Act (Cap. 134)

Self-employed persons may make voluntary contributions to their CPF accounts (OA + SA + MA) in addition to mandatory MediSave.

### Allocation of Voluntary Contributions

Voluntary contributions are allocated across OA, SA, and MA according to the same age-based allocation ratios that apply to employees. The allocation depends on the contributor's age.

### Tax Relief on Voluntary CPF Contributions

| Item | Detail |
|------|--------|
| Relief type | CPF Relief for Self-Employed (Section 39 of the Income Tax Act) |
| Maximum relief | Lower of: (a) 37% of NTI, (b) CPF Annual Limit of S$37,740, or (c) actual voluntary contributions made |
| Mandatory MediSave | Fully deductible as CPF relief (no separate cap) |
| Voluntary contributions | Deductible up to the cap above, AFTER mandatory MediSave is accounted for |
| Overall personal relief cap | S$80,000 total across ALL personal reliefs in a Year of Assessment |
| Condition | No CPF relief if NTI is zero or negative for the Year of Assessment |

### How to Claim

CPF relief is automatically included in the income tax return based on data transmitted from CPFB to IRAS. The SEP does not need to manually claim in most cases. Contributions must be made by 31 December of the relevant year to qualify for that Year of Assessment.

---

## Step 8: MediShield Life Interaction [T1]

**Legislation:** MediShield Life Scheme Act 2015

| Item | Detail |
|------|--------|
| What is MediShield Life? | A mandatory basic health insurance plan that covers all Singapore Citizens and Permanent Residents for life |
| Premium payment | MediShield Life premiums are payable from the MediSave Account |
| Interaction with MediSave | MediSave contributions fund the MA, which in turn pays MediShield Life premiums automatically |
| Premium subsidies | Available for lower- and middle-income households |
| Additional coverage | SEPs may purchase Integrated Shield Plans (private insurers) on top of MediShield Life, with premiums also payable from MediSave up to Additional Withdrawal Limits |

**MediShield Life premiums are NOT a separate obligation -- they are deducted from the MediSave Account balance. However, the SEP must ensure sufficient MediSave balance to cover premiums.**

---

## Step 9: Key Rules Summary [T1]

1. **MediSave is mandatory for SEPs with NTI > S$6,000.** There is no opt-out.
2. **Contribution is based on assessed NTI**, not estimated or declared income.
3. **Payment is due 30 days from NOA** -- same deadline as income tax.
4. **Age determines the rate.** Age is measured as at 1 January of the contribution year.
5. **CPF Annual Limit of S$37,740 is the absolute ceiling** for all CPF contributions in a year.
6. **BHS caps the MediSave Account balance**, not the contribution itself -- overflow goes to SA/OA.
7. **Voluntary CPF contributions are tax-deductible** up to 37% of NTI or S$37,740, whichever is lower.
8. **Platform worker income is excluded from NTI** for MediSave purposes from work year 2025 onward.

---

## Step 10: Edge Case Registry

### EC1 -- SEP with NTI exactly S$6,000 [T1]
**Situation:** Client's assessed NTI is exactly S$6,000.
**Resolution:** No mandatory MediSave contribution. The threshold is "more than S$6,000", not "S$6,000 or more". Voluntary contributions are still permitted.

### EC2 -- SEP who is also an employee [T2]
**Situation:** Client works part-time as an employee (employer pays CPF) and also has self-employment income.
**Resolution:** Mandatory MediSave on NTI still applies. However, total CPF (employer + employee + SEP MediSave + any voluntary) cannot exceed the Annual Limit of S$37,740. [T2] flag for reviewer to verify total CPF headroom.

### EC3 -- NTI in graduated band (S$12,001 to S$18,000) [T1]
**Situation:** Client's NTI falls in the graduated rate band.
**Resolution:** Use the CPFB Self-Employed MediSave Contribution Calculator. Do not interpolate manually -- the graduated formula is prescribed by CPFB.

### EC4 -- MediSave Account already at BHS [T1]
**Situation:** Client's MediSave Account balance has reached the BHS.
**Resolution:** Mandatory MediSave contributions are still computed on NTI, but contributions in excess of BHS flow to SA first, then OA. The SEP does not get an exemption from contributing.

### EC5 -- First year of self-employment, NOA not yet issued [T1]
**Situation:** Client started self-employment mid-year and has not yet received an NOA.
**Resolution:** MediSave is only due after IRAS issues the NOA. No advance payment is required. Advise client to set aside estimated MediSave for cash flow planning.

### EC6 -- SEP turning 55 during the year [T2]
**Situation:** Client turns 55 during the contribution year, which triggers CPF allocation changes.
**Resolution:** Age for MediSave rate purposes is measured as at 1 January. The rate does not change mid-year. However, voluntary CPF allocation ratios may shift. [T2] flag for reviewer.

### EC7 -- Foreign-sourced self-employment income [T2]
**Situation:** Client earns self-employment income from overseas sources.
**Resolution:** MediSave is based on NTI as assessed by IRAS. If the income is taxable in Singapore and included in Form B, it forms part of NTI. If not assessable, it does not trigger MediSave. [T2] flag for reviewer to confirm IRAS treatment.

### EC8 -- Platform worker with mixed income [T2]
**Situation:** Client earns income from both platform work and traditional self-employment.
**Resolution:** From work year 2025, net earnings from platform work are excluded from NTI for MediSave computation. Only traditional self-employment income triggers mandatory MediSave. [T2] flag for reviewer to confirm income classification.

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

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

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed practitioner. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Standard SEP, age 30, NTI above S$18,000
**Input:** Age 30 (as at 1 Jan 2025), NTI = S$50,000.
**Expected output:** Rate = 8.00%. MediSave = S$4,000.00. Below CPF Annual Limit. No cap issue.

### Test 2 -- SEP, age 40, NTI above S$18,000
**Input:** Age 40 (as at 1 Jan 2025), NTI = S$80,000.
**Expected output:** Rate = 9.00%. MediSave = S$7,200.00. Below CPF Annual Limit. No cap issue.

### Test 3 -- SEP, age 48, NTI above S$18,000
**Input:** Age 48 (as at 1 Jan 2025), NTI = S$60,000.
**Expected output:** Rate = 10.00%. MediSave = S$6,000.00. Below CPF Annual Limit. No cap issue.

### Test 4 -- SEP, age 55, NTI above S$18,000
**Input:** Age 55 (as at 1 Jan 2025), NTI = S$40,000.
**Expected output:** Rate = 10.50%. MediSave = S$4,200.00. Below CPF Annual Limit. No cap issue.

### Test 5 -- NTI exactly S$6,000
**Input:** Age 30, NTI = S$6,000.
**Expected output:** No mandatory MediSave. Threshold is "more than S$6,000".

### Test 6 -- NTI in Tier B (S$6,001 to S$12,000)
**Input:** Age 30, NTI = S$10,000.
**Expected output:** Rate = 4.00%. MediSave = S$400.00.

### Test 7 -- NTI in graduated band
**Input:** Age 30, NTI = S$15,000.
**Expected output:** Use CPFB calculator. Rate is between 4.00% and 8.00% (graduated). Do not compute manually.

### Test 8 -- Voluntary CPF tax relief
**Input:** Age 35, NTI = S$100,000. Mandatory MediSave = S$9,000 (9%). Voluntary CPF contribution = S$30,000.
**Expected output:** Total CPF = S$39,000. Exceeds Annual Limit of S$37,740. Cap at S$37,740. Tax relief = S$37,000 (37% of S$100,000). But actual relief limited to S$37,740 (lower of 37% NTI and Annual Limit). Mandatory MediSave S$9,000 is included in this cap. Maximum additional voluntary = S$28,740.

---

## PROHIBITIONS

- NEVER compute MediSave without knowing the client's age as at 1 January of the contribution year
- NEVER use estimated income for final MediSave computation -- MediSave is based on IRAS-assessed NTI
- NEVER tell a client they owe no MediSave without confirming NTI is S$6,000 or below
- NEVER manually interpolate the graduated rate band (S$12,001 to S$18,000) -- use the CPFB calculator
- NEVER advise that MediSave is optional once NTI exceeds S$6,000 -- it is mandatory
- NEVER ignore the CPF Annual Limit when computing total CPF contributions
- NEVER conflate BHS (MediSave Account balance cap) with CPF Annual Limit (contribution cap)
- NEVER include platform worker income in NTI for MediSave from work year 2025 onward without [T2] review
- NEVER present MediSave figures as definitive -- always label as estimated and direct client to their CPFB contribution notice for confirmation
- NEVER advise on MediSave penalties without escalating to a licensed practitioner

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
