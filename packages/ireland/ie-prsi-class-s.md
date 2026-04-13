---
name: ie-prsi-class-s
description: Use this skill whenever asked about Irish PRSI Class S contributions for self-employed individuals. Trigger on phrases like "PRSI self-employed", "Class S contributions", "how much PRSI do I pay", "PRSI calculation Ireland", "self-employed social insurance Ireland", "PRSI threshold", or any question about PRSI obligations for a self-employed client in Ireland. This skill covers Class S rates, minimum contribution, income threshold, payment schedule, interaction with income tax, and edge cases. ALWAYS read this skill before touching any Irish PRSI Class S work.
version: 2.0
---

# Ireland PRSI Class S -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Ireland |
| Authority | Department of Social Protection (DSP); Revenue Commissioners (collection) |
| Primary legislation | Social Welfare Consolidation Act 2005 (as amended) |
| Supporting legislation | Finance Act (annual); Social Welfare Acts (annual amendments) |
| 2025 blended rate | 4.125% (9/12 x 4.1% + 3/12 x 4.2%) |
| 2026 blended rate | 4.2375% (9/12 x 4.2% + 3/12 x 4.35%) |
| Income threshold | EUR 5,000 from all sources (all-or-nothing) |
| Minimum contribution | EUR 650 (2025/2026) |
| Upper earnings limit | None -- no cap |
| Payment method | Self-assessment via Form 11 (Revenue) |
| Preliminary tax deadline | 31 October (mid-November for ROS e-filers) |
| Currency | EUR only |
| Contributor | Open Accountants |
| Validated by | Pending -- licensed Irish practitioner sign-off required |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any PRSI Class S figure, you MUST obtain:

1. **Tax year** -- rates change annually and mid-year (1 October)
2. **Total income from all sources** -- PRSI Class S is levied on aggregate income, not just self-employment
3. **Is income from all sources below EUR 5,000?** -- if yes, no PRSI liability
4. **Does the client have any PAYE employment?** -- may already pay Class A
5. **Age** -- PRSI is not payable once the client reaches age 66
6. **Is the client a proprietary director?** -- 15%+ shareholding pays Class S

**If tax year is unknown, STOP. Do not compute PRSI.**

### Refusal catalogue

**R-IE-PRSI-1 -- EU/EEA cross-border worker.** Trigger: client is self-employed in Ireland but resident in another EU/EEA state. Message: "EU Regulation 883/2004 governs which state collects social insurance. Escalate -- do not advise without specialist cross-border guidance."

### Prohibitions

- NEVER compute PRSI without confirming the tax year -- rates change annually and mid-year
- NEVER tell a client they owe no PRSI without checking the EUR 5,000 threshold from ALL sources
- NEVER apply a single rate (4.1% or 4.2%) to an annual return -- use the blended rate
- NEVER treat a proprietary director as Class A -- they are Class S regardless of salary arrangements
- NEVER state that PRSI is deductible for income tax -- it is NOT
- NEVER pro-rate the EUR 5,000 threshold for partial years -- it is an annual threshold
- NEVER conflate USC and PRSI -- they are separate charges

---

## Section 3 -- Liability determination

**Legislation:** Social Welfare Consolidation Act 2005, Part II

| Condition | PRSI liability |
|---|---|
| Total income from all sources >= EUR 5,000 | Class S applies |
| Total income from all sources < EUR 5,000 | No PRSI liability |
| Client aged 66 or over | No PRSI liability |
| Client already paying Class A as PAYE employee | See dual status rules |

"Total income from all sources" includes self-employment income, rental income, investment income, and any other assessable income. The EUR 5,000 threshold is all-or-nothing: if income is EUR 5,001, PRSI applies to the FULL EUR 5,001.

---

## Section 4 -- Rates, formula, and dual status

### Rate schedule

| Period | Rate |
|---|---|
| 1 Jan 2025 -- 30 Sep 2025 | 4.1% |
| 1 Oct 2025 -- 31 Dec 2025 | 4.2% |
| 1 Jan 2026 -- 30 Sep 2026 | 4.2% |
| 1 Oct 2026 -- 31 Dec 2026 | 4.35% |

### Formula

```
PRSI = max(total_income x blended_rate, minimum_contribution)
```

### Dual status -- PAYE employment + self-employment

| Scenario | PRSI treatment |
|---|---|
| PAYE (Class A) + self-employment >= EUR 5,000 | Class A on employment + Class S on non-PAYE income |
| PAYE (Class A) + self-employment < EUR 5,000 | Class A only |
| Proprietary director (15%+ shareholding) | Class S on all income |

Class A and Class S can both apply simultaneously to the same individual on different income streams.

---

## Section 5 -- Key rules and coverage

**Legislation:** Social Welfare Consolidation Act 2005

1. PRSI Class S is based on CURRENT year income via self-assessment
2. No upper earnings limit -- applies to ALL income above threshold with no cap
3. Minimum contribution of EUR 650 applies whenever income >= EUR 5,000 but calculated PRSI < EUR 650
4. PRSI is NOT deductible for income tax purposes
5. Class S covers: pension, widow/widower's pension, guardian's payment, maternity/paternity/parent's benefit, treatment benefit (from 2025)

---

## Section 6 -- Payment schedule and registration

### Payment schedule

| Event | Deadline |
|---|---|
| Preliminary tax (including PRSI) | 31 October (mid-November for ROS e-filers) |
| Final return and balance | 31 October following year (mid-November for ROS) |

PRSI Class S is collected by Revenue through the self-assessment system (Form 11). It is NOT paid separately to DSP.

### Voluntary contributions

Former Class S contributors who have ceased self-employment may pay voluntary contributions at EUR 500/year (flat rate, 2025/2026) to maintain pension entitlement. Must apply within 60 months of last compulsory contribution. Confirm contribution record with DSP before advising.

### Registration

Register with Revenue Commissioners (Form TR1 for individuals) within 30 days of commencing self-employment.

---

## Section 7 -- Interaction with USC and income tax

| Question | Answer |
|---|---|
| Is PRSI deductible for income tax? | NO |
| Is PRSI part of USC? | NO -- entirely separate charges |
| Are income tax credits applied against PRSI? | NO |

PRSI, USC, and income tax are three independent charges computed separately on different bases with different rules.

---

## Section 8 -- Edge case registry

### EC1 -- Income exactly EUR 5,000
**Situation:** Client's total income from all sources is exactly EUR 5,000.
**Resolution:** PRSI applies. Calculated = EUR 206.25 (2025). Minimum EUR 650 applies. Client pays EUR 650.

### EC2 -- Income EUR 4,999
**Situation:** Client's total income is EUR 4,999.
**Resolution:** No PRSI liability. Threshold not met.

### EC3 -- Mid-year commencement
**Situation:** Client started self-employment in July 2025.
**Resolution:** PRSI based on total income for the full tax year, not pro-rated. If total >= EUR 5,000, Class S applies on full income.

### EC4 -- Proprietary director receiving only salary
**Situation:** Proprietary director (15%+ shareholding) receiving PAYE salary but no dividends.
**Resolution:** Class S, not Class A, regardless of how they draw income. Employer does NOT deduct Class A PRSI. Flag for reviewer to confirm shareholding.

### EC5 -- Client turning 66 mid-year
**Situation:** Client reaches age 66 in August 2025.
**Resolution:** PRSI ceases from the contribution week in which client turns 66. Income after that date not subject to PRSI.

### EC6 -- Rental income only, no trade
**Situation:** Client has EUR 30,000 rental income, no trade.
**Resolution:** Class S applies to rental income if total income >= EUR 5,000.

### EC7 -- Rate transition year
**Situation:** Client asks which rate applies for 2025.
**Resolution:** Blended rate 4.125% for the annual return. Do not apply 4.1% or 4.2% separately.

---

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

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

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified practitioner. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard self-employed, mid-range income (2025)
**Input:** Total income EUR 50,000, age 45, no PAYE.
**Expected output:** PRSI = EUR 50,000 x 4.125% = EUR 2,062.50.

### Test 2 -- Below threshold
**Input:** Total income EUR 4,500, age 35.
**Expected output:** PRSI = EUR 0.

### Test 3 -- Minimum contribution applies
**Input:** Total income EUR 10,000, age 40.
**Expected output:** Calculated = EUR 412.50. Below minimum. PRSI = EUR 650.

### Test 4 -- Aged 66+
**Input:** Total income EUR 80,000, age 67.
**Expected output:** PRSI = EUR 0.

### Test 5 -- Dual Class A and Class S
**Input:** PAYE EUR 60,000 (Class A at source) + self-employment EUR 25,000, age 50.
**Expected output:** Class S on EUR 25,000: EUR 1,031.25.

### Test 6 -- Exactly at threshold
**Input:** Total income EUR 5,000, age 30.
**Expected output:** PRSI = EUR 650 (minimum applies).

### Test 7 -- 2026 rate
**Input:** Total income EUR 80,000, age 42, tax year 2026.
**Expected output:** PRSI = EUR 80,000 x 4.2375% = EUR 3,390.00.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CTA, AITI, or equivalent licensed practitioner in Ireland) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
