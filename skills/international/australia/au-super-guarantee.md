---
name: au-super-guarantee
description: >
  Use this skill whenever asked about Australian Superannuation Guarantee (SG) obligations, voluntary super contributions, concessional and non-concessional caps, Division 293 tax, government co-contribution, spouse contribution tax offset, or carry-forward rules. Trigger on phrases like "how much super do I pay", "SG rate", "super guarantee", "concessional cap", "non-concessional cap", "Division 293", "salary sacrifice super", "personal super contribution deduction", "co-contribution", "spouse super offset", "maximum contribution base", or any question about Australian superannuation obligations for a sole trader or employer. ALWAYS read this skill before touching any SG-related work.
---

# Australia Superannuation Guarantee (SG) -- Sole Trader & Employer Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Australia |
| Jurisdiction Code | AU |
| Primary Legislation | Superannuation Guarantee (Administration) Act 1992 (SGAA 1992) |
| Supporting Legislation | Superannuation Industry (Supervision) Act 1993 (SIS Act); Income Tax Assessment Act 1997 (ITAA 1997) Div 290, Div 291, Div 292, Div 293; Superannuation (Government Co-contribution for Low Income Earners) Act 2003; Income Tax Assessment Act 1936 s 159T (spouse offset) |
| Tax Authority | Australian Taxation Office (ATO) |
| Tax Year | 2024-25 (1 July 2024 -- 30 June 2025) |
| Contributor | Open Accountants |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: SG rate, contribution caps, Division 293, co-contribution, maximum contribution base. Tier 2: carry-forward edge cases, multiple employer scenarios, salary sacrifice interaction. Tier 3: defined benefit funds, constitutionally protected funds, family law splits. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any SG or contribution figure, you MUST know:

1. **Entity structure** [T1] -- sole trader, company, trust, or partnership
2. **Does the client have employees?** [T1] -- determines SG obligation
3. **Is the client a sole trader contributing for themselves?** [T1] -- sole traders have NO SG obligation to themselves
4. **Age of eligible employees** [T1] -- SG applies to all employees regardless of age (from 1 July 2022)
5. **Ordinary time earnings (OTE) per quarter for each employee** [T1] -- SG is calculated on OTE
6. **Total superannuation balance (TSB) at 30 June prior year** [T1] -- affects non-concessional cap and carry-forward eligibility
7. **Income for surcharge purposes** [T1] -- determines Division 293 liability
8. **Does the client hold private health insurance?** [T1] -- relevant to Medicare levy surcharge (separate skill)

---

## Step 1: Determine SG Obligation [T1]

**Legislation:** SGAA 1992 s 12

| Scenario | SG Obligation |
|----------|--------------|
| Employer with employees | YES -- must pay SG on OTE for all eligible employees |
| Sole trader (no employees) | NO SG obligation to themselves. Voluntary contributions only. |
| Sole trader with employees | YES -- must pay SG for employees. NO obligation to themselves. |
| Company director paying themselves a salary | YES -- director is an employee of the company |
| Contractor (employee-like) | May trigger SG -- apply the contractor test (principally for labour) |

**From 1 July 2022, the $450/month earnings threshold was removed.** All employees are eligible for SG regardless of how little they earn.

---

## Step 2: SG Rate [T1]

**Legislation:** SGAA 1992 s 19; Superannuation Guarantee (Administration) Regulations 2018

| Financial Year | SG Rate |
|---------------|---------|
| 2023-24 | 11.0% |
| 2024-25 | 11.5% |
| 2025-26 onwards | 12.0% |

**The SG rate for 2024-25 is 11.5%, NOT 12%.** The 12% rate commences from 1 July 2025.

### Formula

```
SG per quarter = Employee OTE for the quarter x 11.5%
```

**OTE (Ordinary Time Earnings)** includes: salary, wages, commissions, shift loadings, allowances (some), bonuses (if related to ordinary hours), paid leave. OTE excludes: overtime pay, reimbursements, workers compensation payments.

---

## Step 3: Maximum Super Contribution Base [T1]

**Legislation:** SGAA 1992 s 15; Superannuation Guarantee (Administration) Regulations 2018

| Financial Year | Maximum Contribution Base (per quarter) |
|---------------|----------------------------------------|
| 2023-24 | $62,270 |
| 2024-25 | $65,070 |

Employers are NOT required to pay SG on earnings above the maximum contribution base. The cap is per quarter, per employee.

### Formula

```
Maximum SG per quarter = $65,070 x 11.5% = $7,483.05
```

If an employee's OTE exceeds $65,070 in a quarter, the employer's minimum SG obligation is capped at $7,483.05 for that quarter. The employer may voluntarily contribute more.

---

## Step 4: Payment Schedule and Deadlines [T1]

**Legislation:** SGAA 1992 s 33

| Quarter | Period | SG Due Date |
|---------|--------|-------------|
| Q1 | 1 Jul -- 30 Sep | 28 October |
| Q2 | 1 Oct -- 31 Dec | 28 January |
| Q3 | 1 Jan -- 31 Mar | 28 April |
| Q4 | 1 Apr -- 30 Jun | 28 July |

**Late or missed payments trigger the Super Guarantee Charge (SGC),** which includes the SG shortfall, a nominal interest component (currently 10% per annum), and an administration fee of $20 per employee per quarter. SGC is NOT tax-deductible. Employers must lodge a Super Guarantee Charge Statement with the ATO.

**NOTE: Payday Super commences 1 July 2026.** From that date, SG must be paid on each payday rather than quarterly.

---

## Step 5: Concessional Contributions Cap [T1]

**Legislation:** ITAA 1997 Div 291, Subdiv 291-B

| Financial Year | Concessional Cap |
|---------------|-----------------|
| 2023-24 | $27,500 |
| 2024-25 | $30,000 |

Concessional contributions include:
- Employer SG contributions
- Salary sacrifice contributions
- Personal contributions for which a tax deduction is claimed (s 290-150 notice)

Contributions exceeding the concessional cap are included in the individual's assessable income and taxed at their marginal rate (with a 15% tax offset for tax already paid by the fund).

---

## Step 6: Carry-Forward Unused Concessional Cap [T1]

**Legislation:** ITAA 1997 s 291-20

You can carry forward unused concessional cap amounts from up to **5 previous financial years** if:

1. Your total superannuation balance (TSB) is **less than $500,000** at 30 June of the previous financial year; AND
2. The unused amounts are from 2018-19 or later (carry-forward commenced from that year).

### Example (2024-25)

| Year | Cap | Used | Unused |
|------|-----|------|--------|
| 2019-20 | $25,000 | $15,000 | $10,000 |
| 2020-21 | $25,000 | $25,000 | $0 |
| 2021-22 | $27,500 | $20,000 | $7,500 |
| 2022-23 | $27,500 | $27,500 | $0 |
| 2023-24 | $27,500 | $10,000 | $17,500 |
| **2024-25** | **$30,000** | -- | -- |

**Available cap in 2024-25 = $30,000 + $10,000 + $7,500 + $17,500 = $65,000** (assuming TSB < $500,000 at 30 June 2024). Note: 2019-20 unused amount has now expired (> 5 years ago in 2024-25).

---

## Step 7: Non-Concessional Contributions Cap [T1]

**Legislation:** ITAA 1997 Div 292, Subdiv 292-C

| Financial Year | Non-Concessional Cap | Bring-Forward Cap (3 years) |
|---------------|---------------------|---------------------------|
| 2023-24 | $110,000 | $330,000 |
| 2024-25 | $120,000 | $360,000 |

Non-concessional contributions are after-tax contributions for which no deduction is claimed.

**Total Superannuation Balance (TSB) restrictions:**

| TSB at 30 June 2024 | Non-Concessional Cap 2024-25 |
|---------------------|------------------------------|
| Below $1,660,000 | $360,000 (3-year bring-forward) |
| $1,660,000 -- $1,779,999 | $240,000 (2-year bring-forward) |
| $1,780,000 -- $1,899,999 | $120,000 (no bring-forward) |
| $1,900,000 or more | Nil |

**The general transfer balance cap for 2024-25 is $1,900,000.**

Excess non-concessional contributions attract a tax on the associated earnings at the individual's marginal rate. The individual may elect to release the excess from their super fund.

---

## Step 8: Tax Deductibility of Personal Super Contributions [T1]

**Legislation:** ITAA 1997 Div 290, s 290-150, s 290-170

Sole traders and other self-employed individuals can claim a tax deduction for personal super contributions, subject to:

1. The contribution is made to a complying super fund
2. A valid **Notice of Intent to Claim a Deduction (s 290-170)** is given to the fund AND acknowledged before:
   - Lodging the tax return for that year; OR
   - The end of the following financial year
   -- whichever is earlier
3. The amount does not exceed the concessional contributions cap (including carry-forward if eligible)

**The s 290-150 notice converts a non-concessional contribution into a concessional contribution.** This is the primary mechanism for sole traders to obtain a tax deduction for super.

**WARNING:** If the notice is not lodged before the deadline, the contribution remains non-concessional and NO deduction is available. This is a common and costly error.

---

## Step 9: Division 293 Tax [T1]

**Legislation:** ITAA 1997 Div 293

| Item | Value |
|------|-------|
| Division 293 threshold | $250,000 |
| Division 293 tax rate | 15% |
| Income definition | Taxable income + low tax contributed amounts (concessional contributions) |

Division 293 imposes an additional 15% tax on concessional super contributions for high-income earners, effectively doubling the contributions tax from 15% to 30%.

### Formula

```
Div 293 income = taxable income + low tax contributed amounts
If Div 293 income > $250,000:
  Div 293 tax = 15% x LESSER OF:
    (a) low tax contributed amounts; OR
    (b) Div 293 income - $250,000
```

### Example

| Item | Amount |
|------|--------|
| Taxable income | $240,000 |
| Concessional contributions | $30,000 |
| Div 293 income | $270,000 |
| Excess over $250,000 | $20,000 |
| Div 293 tax = 15% x $20,000 | $3,000 |

The ATO issues a Division 293 assessment after the individual's tax return is processed. The individual can choose to pay from personal funds or release from their super fund.

---

## Step 10: Government Co-Contribution [T1]

**Legislation:** Superannuation (Government Co-contribution for Low Income Earners) Act 2003

| Item | 2024-25 |
|------|---------|
| Maximum co-contribution | $500 |
| Lower income threshold | $45,400 |
| Higher income threshold | $60,400 |
| Matching rate | 50 cents per $1 of personal non-concessional contribution |
| Maximum personal contribution to receive full co-contribution | $1,000 |

### Eligibility

- Total income is less than $60,400
- At least 10% of total income is from employment or carrying on a business
- Made personal non-concessional contributions during the year
- Under 71 years old at end of financial year
- Not held a temporary visa at any time during the year (unless New Zealand citizen or it was a prescribed visa)
- Lodged a tax return for the year

### Reduction formula

```
If income > $45,400:
  Maximum co-contribution reduces by 3.333 cents for every $1 above $45,400
  Co-contribution = $500 - ((income - $45,400) x 0.03333)
```

The ATO calculates and pays the co-contribution automatically upon lodgement of the tax return. No application required.

---

## Step 11: Low Income Super Tax Offset (LISTO) [T1]

**Legislation:** ITAA 1997 s 292-467

| Item | Value |
|------|-------|
| Adjusted taxable income threshold | $37,000 or less |
| LISTO amount | 15% of concessional contributions |
| Maximum LISTO | $500 |

The LISTO effectively refunds the 15% contributions tax paid by the super fund on concessional contributions for low-income earners. The ATO pays the LISTO directly into the individual's super fund.

---

## Step 12: Spouse Contribution Tax Offset [T1]

**Legislation:** ITAA 1936 s 159T; ITAA 1997 s 290-230

| Item | Value |
|------|-------|
| Maximum tax offset | $540 |
| Offset rate | 18% |
| Maximum eligible contribution | $3,000 |
| Spouse income threshold (full offset) | $37,000 or less |
| Spouse income threshold (nil offset) | $40,000 or more |

### Formula

```
Offset = 18% x LESSER OF:
  (a) $3,000; OR
  (b) $3,000 - (spouse income - $37,000)
  -- where "spouse income" = assessable income + RESC + RFBA (excl FHSS released amounts)
```

### Conditions

- The contribution is non-concessional (after-tax) to the spouse's super fund
- Both are Australian residents when the contribution is made
- The couple are not living separately and apart on a permanent basis
- The spouse has not exceeded their non-concessional contributions cap
- The spouse's TSB is less than $1,900,000 at 30 June of the prior year

---

## Step 13: Sole Trader -- Voluntary Super Contributions [T1]

**Legislation:** SGAA 1992 s 12; ITAA 1997 Div 290

A sole trader has **NO SG obligation to themselves.** Any super contribution is voluntary.

| Strategy | Tax Treatment |
|----------|--------------|
| Personal contribution with s 290-150 notice | Concessional -- deductible, taxed at 15% in the fund (up to concessional cap) |
| Personal contribution without s 290-150 notice | Non-concessional -- not deductible, not taxed in the fund (up to non-concessional cap) |
| Contribution to spouse's fund | Non-concessional for the spouse -- may qualify for spouse contribution tax offset |

**Sole trader planning note:** A sole trader should consider making personal super contributions and claiming a deduction under s 290-150 to reduce taxable income. This is the equivalent of an employer's SG contribution.

---

## Step 14: Edge Case Registry

### EC1 -- Sole trader thinks they must pay SG to themselves [T1]
**Situation:** Sole trader asks how much SG they owe on their own drawings.
**Resolution:** Sole traders have NO SG obligation to themselves. Drawings are not salary. Only voluntary contributions apply. If the client has employees, SG applies to those employees only.

### EC2 -- Exceeding the concessional cap [T1]
**Situation:** Employer SG + salary sacrifice + personal deductible contributions exceed $30,000.
**Resolution:** Excess concessional contributions are included in assessable income and taxed at the individual's marginal rate. A 15% tax offset applies for contributions tax already paid by the fund. The excess also counts towards the non-concessional cap unless the individual elects to release from super.

### EC3 -- Carry-forward with TSB at or above $500,000 [T1]
**Situation:** Client wants to use carry-forward unused concessional cap but TSB is $520,000 at 30 June 2024.
**Resolution:** Carry-forward is NOT available. The concessional cap is $30,000 only. No prior year unused amounts can be accessed.

### EC4 -- Contractor vs employee for SG purposes [T2]
**Situation:** Client engages a contractor who works exclusively for them, uses client's tools, and is paid hourly.
**Resolution:** The contract may be principally for the labour of the individual (SGAA s 12(3)), triggering SG obligations. [T2] flag for reviewer -- the multi-factor test requires analysis of the specific arrangement.

### EC5 -- Multiple employers contributing SG [T2]
**Situation:** Individual has two employers both paying SG. Combined concessional contributions may exceed the cap.
**Resolution:** Neither employer is at fault -- each must pay SG on their employee's OTE. The individual bears the excess concessional contributions tax. [T2] flag for reviewer to assess whether salary sacrifice should be adjusted.

### EC6 -- Over-75 contributions [T2]
**Situation:** Client is 76 years old and wants to make super contributions.
**Resolution:** From 1 July 2022, the work test was removed for contributions by those under 75. For those 75 and over, voluntary contributions require meeting the work test (40 hours in 30 consecutive days). Mandated employer contributions (SG) have no age limit. [T2] flag for reviewer.

### EC7 -- s 290-150 notice lodged late [T1]
**Situation:** Client made personal super contributions but forgot to lodge the notice of intent before the earlier of lodging the return or end of the following year.
**Resolution:** The contribution cannot be converted to concessional. It remains non-concessional. No deduction is available. This is irreversible.

---

## Step 15: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified practitioner must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified practitioner. Document gap.
```

---

## Step 16: Test Suite

### Test 1 -- Standard SG calculation
**Input:** Employee OTE $20,000 for the quarter. 2024-25 year.
**Expected output:** SG = $20,000 x 11.5% = $2,300.00.

### Test 2 -- OTE above maximum contribution base
**Input:** Employee OTE $80,000 for the quarter. 2024-25 year.
**Expected output:** SG = $65,070 x 11.5% = $7,483.05 (capped at maximum contribution base).

### Test 3 -- Sole trader voluntary contribution with deduction
**Input:** Sole trader contributes $25,000 personal super, lodges s 290-150 notice. No other concessional contributions. TSB $200,000.
**Expected output:** $25,000 concessional contribution. Tax deduction of $25,000. Within $30,000 cap. Fund pays 15% contributions tax ($3,750).

### Test 4 -- Division 293 calculation
**Input:** Taxable income $260,000. Concessional contributions $30,000.
**Expected output:** Div 293 income = $290,000. Excess = $40,000. Div 293 tax = 15% x $30,000 = $4,500 (lesser of concessional contributions $30,000 and excess $40,000).

### Test 5 -- Carry-forward unused cap
**Input:** TSB $400,000 at 30 June 2024. Unused concessional amounts: $5,000 (2021-22), $10,000 (2022-23), $15,000 (2023-24).
**Expected output:** Available cap = $30,000 + $5,000 + $10,000 + $15,000 = $60,000 (TSB < $500,000, all within 5-year window).

### Test 6 -- Government co-contribution
**Input:** Total income $50,000. Personal non-concessional contribution $1,000. Age 35.
**Expected output:** Co-contribution = $500 - (($50,000 - $45,400) x 0.03333) = $500 - $153.32 = $346.68 (rounded).

### Test 7 -- Spouse contribution tax offset
**Input:** Contributed $5,000 to spouse's super fund. Spouse assessable income $36,000.
**Expected output:** Offset = 18% x $3,000 = $540 (capped at $3,000 eligible amount; spouse income below $37,000).

### Test 8 -- Sole trader asks about SG for themselves
**Input:** Sole trader, no employees, asks "how much SG do I owe?"
**Expected output:** $0. Sole traders have no SG obligation to themselves. Advise on voluntary contribution options.

---

## PROHIBITIONS

- NEVER tell a sole trader they must pay SG to themselves -- sole traders have no SG obligation on their own income
- NEVER apply the 12% rate to the 2024-25 year -- the rate is 11.5% (12% starts 1 July 2025)
- NEVER ignore the maximum contribution base -- SG is capped at $65,070 per quarter per employee
- NEVER allow a client to claim a deduction for personal super contributions without confirming the s 290-150 notice has been lodged
- NEVER apply carry-forward unused concessional cap if TSB is $500,000 or more
- NEVER present super figures as definitive -- always label as estimated and direct client to their super fund and ATO records for confirmation
- NEVER compute SGC penalties without escalating to a qualified practitioner
- NEVER advise on defined benefit or constitutionally protected fund matters -- [T3] escalate

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
