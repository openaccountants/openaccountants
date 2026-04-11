---
name: uk-national-insurance
description: >
  Use this skill whenever asked about UK National Insurance Contributions (NIC) for self-employed individuals. Trigger on phrases like "how much NIC do I pay", "Class 2 contributions", "Class 4 NIC", "national insurance self-employed", "NIC calculation", "state pension qualifying years", "NIC deferment", "voluntary Class 2", or any question about UK NIC obligations for a self-employed client. Also trigger when preparing an SA100 Self Assessment return where NIC is relevant. This skill covers Class 2 voluntary contributions, Class 4 profit-based rates, thresholds, payment schedule, interaction with employment Class 1, deferment, state pension entitlement, and edge cases. ALWAYS read this skill before touching any UK NIC-related work.
version: 1.0
jurisdiction: GB
tax_year: 2025-26
category: international
depends_on:
  - social-contributions-workflow-base
---

# UK National Insurance (Class 2 + Class 4) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | United Kingdom |
| Jurisdiction Code | GB |
| Primary Legislation | Social Security Contributions and Benefits Act 1992 (SSCBA 1992) |
| Supporting Legislation | National Insurance Contributions Act 2015; Finance Act 2024 (Class 2 reform) |
| Tax Authority | HM Revenue & Customs (HMRC) |
| Rate Publisher | HMRC (publishes annual NIC rates confirmation order) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires sign-off by a UK-qualified practitioner |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year Coverage | 2024-25 and 2025-26 |
| Confidence Coverage | Tier 1: rate calculation, thresholds, payment schedule, Class 2 voluntary rule. Tier 2: deferment applications, dual status edge cases, mid-year switches. Tier 3: mariners, share fishermen, volunteer development workers, disability exemptions. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any NIC figure, you MUST know:

1. **Tax year** [T1] -- 2024-25 or 2025-26? Rates differ for Class 2.
2. **Employment status** [T1] -- solely self-employed, or also employed (dual status)?
3. **Net self-employment profits** [T1] -- trading profits after allowable deductions, as reported on SA100/SA103.
4. **Is the client also employed with Class 1 contributions?** [T1] -- affects deferment and maximum NIC cap.
5. **Does the client want to pay voluntary Class 2?** [T1] -- relevant if profits are below the Small Profits Threshold.
6. **State pension record** [T2] -- does the client have gaps in qualifying years?

---

## Step 1: Determine Which Classes Apply [T1]

**Legislation:** SSCBA 1992, Part I

| Class | Who | How |
|-------|-----|-----|
| Class 1 | Employees | Deducted from salary by employer |
| Class 2 | Self-employed (voluntary from 6 April 2024) | Flat weekly rate, paid via Self Assessment or Direct Debit |
| Class 3 | Voluntary (anyone) | To fill gaps in NI record for state pension |
| Class 4 | Self-employed with profits above Lower Profits Limit | Percentage of profits, paid via Self Assessment |

**Self-employed persons are liable for Class 4 NIC on profits above the Lower Profits Limit. Class 2 is voluntary from 6 April 2024 onward.**

---

## Step 2: Class 2 NIC -- Voluntary Contributions [T1]

**Legislation:** SSCBA 1992 s.11; Finance Act 2024

### Key Change: From 6 April 2024, Class 2 NIC is no longer compulsory.

| Item | 2024-25 | 2025-26 |
|------|---------|---------|
| Weekly rate | £3.45 | £3.50 |
| Annual cost (52 weeks) | £179.40 | £182.00 |
| Small Profits Threshold (SPT) | £6,725 | £6,845 |

### How Class 2 Now Works

| Profit Level | Class 2 Treatment |
|-------------|-------------------|
| Profits >= £6,845 (2025-26) | Treated as paid automatically (zero-rate). Client gets NI credit without paying. No action needed. |
| Profits < £6,845 but > £0 | NOT treated as paid. Client must pay voluntarily (£3.50/week) to get a qualifying year for state pension. |
| Zero or negative profits | NOT treated as paid. Client must pay voluntarily to get a qualifying year. |

### Why Pay Voluntary Class 2?

- Class 2 is the cheapest way to build state pension entitlement (£182.00/year vs Class 3 at £17.75/week = £923.00/year in 2025-26).
- Each qualifying year adds approximately 1/35th of the full state pension (£230.25/week in 2025-26).
- A single year of Class 2 contributions (£182.00) buys approximately £342/year in state pension -- an exceptional return.

---

## Step 3: Class 4 NIC -- Profit-Based Contributions [T1]

**Legislation:** SSCBA 1992 s.15

### Rates

| Band | 2024-25 | 2025-26 |
|------|---------|---------|
| Profits below Lower Profits Limit (LPL) | 0% | 0% |
| Profits between LPL and Upper Profits Limit (UPL) | 6% | 6% |
| Profits above UPL | 2% | 2% |

### Thresholds

| Threshold | 2024-25 | 2025-26 |
|-----------|---------|---------|
| Lower Profits Limit (LPL) | £12,570 | £12,570 |
| Upper Profits Limit (UPL) | £50,270 | £50,270 |

### Formula

```
Class 4 NIC = (min(profits, UPL) - LPL) x 6%  +  max(profits - UPL, 0) x 2%
```

Where profits = net trading profits from self-employment after allowable deductions.

### Calculation Examples (2025-26)

| Net Profits | Class 4 NIC | Breakdown |
|-------------|-------------|-----------|
| £10,000 | £0.00 | Below LPL -- no Class 4 due |
| £12,570 | £0.00 | At LPL -- no Class 4 due |
| £20,000 | £445.80 | (£20,000 - £12,570) x 6% |
| £35,000 | £1,345.80 | (£35,000 - £12,570) x 6% |
| £50,270 | £2,262.00 | (£50,270 - £12,570) x 6% |
| £60,000 | £2,456.60 | (£50,270 - £12,570) x 6% + (£60,000 - £50,270) x 2% |
| £100,000 | £3,256.60 | (£50,270 - £12,570) x 6% + (£100,000 - £50,270) x 2% |

---

## Step 4: Payment Schedule [T1]

**Legislation:** Taxes Management Act 1970; HMRC Self Assessment rules

Class 4 NIC is collected through Self Assessment alongside income tax.

| Payment | Due Date | What |
|---------|----------|------|
| First payment on account | 31 January during tax year | 50% of prior year Class 4 liability |
| Second payment on account | 31 July after tax year end | 50% of prior year Class 4 liability |
| Balancing payment | 31 January following tax year end | Any remaining Class 4 (and Class 2 if paying voluntarily) |

**Class 2 voluntary contributions** can be paid:
- Through Self Assessment (added to balancing payment)
- By Direct Debit (monthly or quarterly to HMRC)
- By bank transfer

**Example timeline for 2025-26 tax year (6 April 2025 to 5 April 2026):**
- 31 January 2026: First payment on account
- 31 July 2026: Second payment on account
- 31 January 2027: Balancing payment (final settlement)

---

## Step 5: Interaction with Employment Class 1 (Dual Status) [T1]

**Legislation:** SSCBA 1992; Social Security (Contributions) Regulations 2001

| Scenario | Class 1 | Class 2 | Class 4 |
|----------|---------|---------|---------|
| Employed only | Yes (via payroll) | No | No |
| Self-employed only | No | Voluntary | Yes (if profits > LPL) |
| Employed AND self-employed | Yes (via payroll) | Voluntary (if desired) | Yes (if profits > LPL) |

**Unlike Malta, being employed does NOT exempt the client from Class 4. Both Class 1 and Class 4 are due on their respective income streams.**

### Maximum NIC Cap (Annual Maximum)

There is an annual maximum on total NIC. If combined Class 1 and Class 4 contributions would exceed the maximum, the excess Class 4 is reduced. HMRC calculates this automatically through Self Assessment.

The maximum is: 53 x weekly Class 1 main primary threshold rate + Class 4 main rate on (UPL - LPL).

---

## Step 6: Deferment Applications [T2]

**Legislation:** Social Security (Contributions) Regulations 2001, Reg 90-100

| Situation | Can Defer? | How |
|-----------|-----------|-----|
| Two or more employments (Class 1 + Class 1) | Yes -- defer Class 1 in secondary employment | Apply on form CA72A to HMRC |
| Employed + self-employed (Class 1 + Class 4) | No deferment needed | HMRC calculates annual maximum automatically via SA |
| Class 4 alone | Cannot be deferred | N/A |

**Deferment of Class 1 only:** If the client has two employments and expects combined Class 1 to exceed the annual maximum, they can apply to defer Class 1 in one employment. In the deferred employment, they pay only 2% (not the main rate).

**[T2] flag for reviewer whenever a client has multiple employments and requests deferment. Confirm earnings estimates before applying.**

---

## Step 7: State Pension Qualifying Years [T1]

**Legislation:** Pensions Act 2014

| Requirement | Detail |
|-------------|--------|
| Full new state pension | 35 qualifying years |
| Minimum state pension | 10 qualifying years |
| Full amount (2025-26) | £230.25 per week (£11,973 per year) |
| Proportional | Years between 10 and 35 give proportional amount |

### How Self-Employed Build Qualifying Years

| Profit Level | Qualifying Year? |
|-------------|-----------------|
| Profits >= SPT (£6,845 in 2025-26) | Yes -- automatic credit (Class 2 treated as paid) |
| Profits < SPT, voluntary Class 2 paid | Yes -- voluntary payment secures the year |
| Profits < SPT, no voluntary Class 2 paid | No -- gap in NI record |

### Filling Gaps

- Voluntary Class 2 (if eligible as self-employed): £3.50/week (2025-26)
- Voluntary Class 3 (anyone): £17.75/week (2025-26)
- Can usually go back up to 6 years to fill gaps
- Check NI record at gov.uk/check-national-insurance-record

---

## Step 8: Key Rules [T1]

1. **Class 4 is based on CURRENT year profits.** Unlike Malta SSC, UK Class 4 NIC is calculated on the same year's profits as reported on the Self Assessment return.
2. **Class 2 is voluntary from 6 April 2024.** Self-employed with profits above the SPT are automatically credited.
3. **Net profits = turnover minus allowable business expenses** as computed on form SA103 (self-employment supplementary pages).
4. **Losses:** If net profits are zero or negative, no Class 4 is due. Voluntary Class 2 may still be paid for state pension purposes.
5. **Multiple self-employments:** Profits from all self-employments are aggregated for Class 4 purposes.

---

## Step 9: Penalties [T1]

**Legislation:** Taxes Management Act 1970; Finance Act 2009

| Penalty | Detail |
|---------|--------|
| Late filing (SA return) | £100 initial, escalating to daily penalties after 3 months |
| Late payment | Interest charged from due date at HMRC's prevailing rate |
| Failure to notify chargeability | Up to 100% of tax/NIC due (behaviour-dependent) |
| Deliberate underpayment | Up to 100% of NIC due (may be reduced for disclosure) |

**Class 4 NIC penalties are the same as income tax penalties -- they are collected through the same Self Assessment regime.**

---

## Step 10: Exemptions and Special Cases [T2]

| Category | Treatment |
|----------|-----------|
| Under 16 | No Class 2 or Class 4 liability |
| Over state pension age | No Class 4 liability. No Class 2 needed for pension. |
| Examiners / moderators | May be treated as employed -- check contract terms |
| Foster carers | Qualifying care relief may reduce profits below thresholds |
| Religious ministers | Special Class 2 provisions may apply |
| Persons abroad | Complex rules -- see HMRC guidance on NIC for non-residents |

**[T2] flag for reviewer whenever any of these categories applies.**

---

## Step 11: Edge Case Registry

### EC1 -- Mid-year switch from employment to self-employment [T1]
**Situation:** Client was employed until September 2025, then became self-employed from October 2025.
**Resolution:** Class 1 stops when employment ends. Class 4 applies on self-employment profits from October onward (first accounting period). Voluntary Class 2 can be paid for the self-employment period. The annual maximum NIC cap applies if Class 1 contributions were also paid in the year.

### EC2 -- Profits exactly at the Lower Profits Limit [T1]
**Situation:** Client's net trading profits are exactly £12,570.
**Resolution:** No Class 4 NIC due. The LPL is the point at which the 6% rate begins -- profits AT the LPL produce zero liability. Class 2 treated as paid (profits > SPT).

### EC3 -- Zero or negative profits (loss year) [T1]
**Situation:** Client had a trading loss. Net profits are negative.
**Resolution:** No Class 4 due. Client may still pay voluntary Class 2 (£182.00 for 2025-26) to secure a state pension qualifying year.

### EC4 -- Employed and self-employed simultaneously [T1]
**Situation:** Client earns £40,000 employment income (Class 1 via payroll) and £25,000 self-employment profits.
**Resolution:** Class 1 continues on employment income. Class 4 due on self-employment profits above £12,570. Annual maximum applies -- HMRC adjusts automatically. Voluntary Class 2 is not needed if employment income provides qualifying year via Class 1.

### EC5 -- Multiple self-employments [T1]
**Situation:** Client has two sole trader businesses, one earning £8,000 and another earning £15,000.
**Resolution:** Aggregate profits (£23,000) for Class 4 purposes. Class 4 = (£23,000 - £12,570) x 6% = £625.80. File on single SA return.

### EC6 -- Client over state pension age [T1]
**Situation:** Client is 68 and still self-employed with profits of £30,000.
**Resolution:** No Class 4 liability (exempt once past state pension age). No Class 2 needed. Must still file SA return for income tax purposes.

### EC7 -- First year of self-employment with overlap relief [T2]
**Situation:** Client started trading on 1 July 2025. First accounting period does not align with tax year.
**Resolution:** Basis period reform (from 2024-25) means profits are taxed on a tax-year basis. Class 4 applies to the profits allocated to the tax year under the new rules. [T2] flag for reviewer to confirm basis period allocation.

### EC8 -- Client wants to backfill NI gaps for state pension [T2]
**Situation:** Client has 5 years of NI gaps and wants to pay voluntary contributions.
**Resolution:** Can pay Class 2 (if eligible as self-employed in those years) or Class 3 going back up to 6 years. Class 2 is significantly cheaper. [T2] flag -- reviewer should check client's NI record and confirm which years can still be filled and which class applies.

---

## Step 12: Reviewer Escalation Protocol

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

## Step 13: Test Suite

### Test 1 -- Standard self-employed, mid-range profits
**Input:** Tax year 2025-26. Self-employed only. Net profits £30,000.
**Expected output:** Class 4 = (£30,000 - £12,570) x 6% = £1,045.80. Class 2 treated as paid (profits > SPT). No voluntary Class 2 payment needed. Total NIC = £1,045.80.

### Test 2 -- High-income self-employed
**Input:** Tax year 2025-26. Self-employed only. Net profits £80,000.
**Expected output:** Class 4 = (£50,270 - £12,570) x 6% + (£80,000 - £50,270) x 2% = £2,262.00 + £594.60 = £2,856.60. Total NIC = £2,856.60.

### Test 3 -- Below Lower Profits Limit
**Input:** Tax year 2025-26. Self-employed only. Net profits £10,000.
**Expected output:** Class 4 = £0 (below LPL). Profits above SPT so Class 2 treated as paid. Total NIC = £0 (unless voluntary Class 2 chosen, but not needed as profits > SPT).

### Test 4 -- Below Small Profits Threshold, pays voluntary Class 2
**Input:** Tax year 2025-26. Self-employed only. Net profits £5,000. Client elects voluntary Class 2.
**Expected output:** Class 4 = £0 (below LPL). Voluntary Class 2 = £182.00 (52 x £3.50). Total NIC = £182.00.

### Test 5 -- Loss year, voluntary Class 2 for state pension
**Input:** Tax year 2025-26. Self-employed only. Net profits -£3,000. Client wants to maintain NI record.
**Expected output:** Class 4 = £0. Voluntary Class 2 = £182.00. Total NIC = £182.00.

### Test 6 -- Employed and self-employed
**Input:** Tax year 2025-26. Employed (Class 1 paid via payroll on £45,000 salary). Also self-employed with net profits £20,000.
**Expected output:** Class 4 = (£20,000 - £12,570) x 6% = £445.80. Class 1 paid separately via payroll. Annual maximum cap checked by HMRC. Voluntary Class 2 not needed (Class 1 from employment provides qualifying year).

### Test 7 -- Over state pension age
**Input:** Tax year 2025-26. Client age 69. Net profits £40,000.
**Expected output:** Class 4 = £0 (exempt -- over state pension age). Class 2 not needed. Total NIC = £0.

### Test 8 -- 2024-25 tax year comparison
**Input:** Tax year 2024-25. Self-employed only. Net profits £30,000.
**Expected output:** Class 4 = (£30,000 - £12,570) x 6% = £1,045.80. Class 2 treated as paid (profits > SPT of £6,725). Voluntary Class 2 rate would be £3.45/week if elected. Total NIC = £1,045.80.

---

## PROHIBITIONS

- NEVER compute Class 4 NIC without confirming the tax year -- thresholds and rates vary by year
- NEVER tell a client they must pay Class 2 -- it has been voluntary since 6 April 2024
- NEVER tell a client with profits below the SPT that they automatically get a qualifying year -- they must pay voluntary Class 2 to secure it
- NEVER apply Class 4 rates to employment income -- Class 4 applies only to self-employment profits
- NEVER ignore the annual maximum NIC cap for clients who are both employed and self-employed
- NEVER advise on deferment without confirming all employment income sources and expected NIC totals
- NEVER present NIC figures as definitive for dual-status clients -- the annual maximum requires HMRC's Self Assessment calculation
- NEVER assume Class 2 is treated as paid for clients with profits below the SPT
- NEVER advise on NIC for non-resident or overseas clients without escalating to [T3] -- complex rules apply

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
