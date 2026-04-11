---
name: ie-preliminary-tax
description: Use this skill whenever asked about Irish Preliminary Tax for self-employed individuals. Trigger on phrases like "preliminary tax Ireland", "Form 11", "self-assessed tax Ireland", "October 31 deadline", "ROS filing", "100% rule preliminary tax", "90% rule Ireland", or any question about estimated tax payment obligations for a self-employed client in Ireland. Covers the 100%/90% prior-year/current-year rules, payment deadlines, and surcharges. ALWAYS read this skill before touching any Ireland preliminary tax work.
---

# Ireland Preliminary Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Ireland |
| Jurisdiction Code | IE |
| Primary Legislation | TCA 1997, Part 41A (Self-Assessment), ss. 952-959 |
| Supporting Legislation | TCA 1997, s.1084 (surcharges); Finance Acts |
| Tax Authority | Revenue Commissioners (Revenue) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Irish Chartered Accountant or CTA |
| Validation Date | Pending |
| Skill Version | 1.0 |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

Before computing, you MUST know:

1. **Income type** [T1] -- self-employment (Case I/II), rental (Case V), investment, or mixed?
2. **Prior-year final tax liability** [T1] -- the total tax paid/due for the prior year
3. **Estimated current-year income** [T1] -- needed for the 90% rule
4. **Filing method** [T1] -- paper filing or ROS (Revenue Online Service)?
5. **Is this the first year of self-assessment?** [T1] -- special rules for first year
6. **CGT (Capital Gains Tax) obligations?** [T1] -- CGT preliminary tax has different rules

**If prior-year liability is unknown, STOP. The 100% rule requires knowing the prior-year figure.**

---

## Step 1: The Two Safe Harbour Rules [T1]

**Legislation:** TCA 1997, s.959AN

A self-assessed taxpayer meets their preliminary tax obligation if they pay **at least** one of:

| Rule | Amount | When to Use |
|------|--------|-------------|
| **100% of prior-year liability** | 100% of the final tax liability for the preceding year | Safe and simple -- no estimation needed |
| **90% of current-year liability** | 90% of the final tax liability for the current year | If current year will be significantly lower than prior year |

### Which Rule to Choose?

- **100% rule** is the **safe default**. No estimation risk. Revenue cannot impose interest even if current-year liability is much higher.
- **90% rule** requires accurate estimation. If the estimate is wrong and less than 90% is paid, interest accrues.
- For **prior-year liability <= EUR 200 (de minimis)**: no preliminary tax obligation.

### Additional Safe Harbour: 105% Rule

For very large prior-year liabilities, a **105% of pre-prior-year liability** option may apply:

| Rule | Amount |
|------|--------|
| 105% of pre-prior-year | 105% of the final tax liability for the year BEFORE the prior year |

This applies only if paying via direct debit in equal monthly instalments.

---

## Step 2: What Constitutes "Tax Liability" [T1]

**Legislation:** TCA 1997, s.959A

The preliminary tax covers ALL of:

| Component | Description |
|-----------|-------------|
| Income tax | At 20%/40% rates |
| USC (Universal Social Charge) | At applicable USC rates (0.5%/2%/4%/8%) |
| PRSI (Class S) | 4% on all self-employment income (no upper limit) |
| CGT (if applicable) | Capital gains tax (33%) -- separate payment dates |

**Preliminary tax = income tax + USC + PRSI combined.**

---

## Step 3: Computation Steps [T1]

### Step 3.1 -- Determine prior-year final liability

```
prior_year_liability = income_tax + USC + PRSI (from prior-year assessment)
```

### Step 3.2 -- Option A: 100% of prior year

```
preliminary_tax_100 = prior_year_liability × 100%
```

### Step 3.3 -- Option B: 90% of current year (estimated)

```
current_year_estimated_liability = estimated_income_tax + estimated_USC + estimated_PRSI
preliminary_tax_90 = current_year_estimated_liability × 90%
```

### Step 3.4 -- Choose the lower option (or the safer 100% rule)

```
preliminary_tax = min(preliminary_tax_100, preliminary_tax_90)
# OR simply pay preliminary_tax_100 for safety
```

### Step 3.5 -- Credit prior payments

```
net_preliminary_due = preliminary_tax - any_PAYE_credits - any_withholding_tax
```

---

## Step 4: Payment Deadlines [T1]

**Legislation:** TCA 1997, s.959AN, s.959AO

### Paper Filing

| Obligation | Deadline |
|------------|----------|
| Preliminary tax for current year | **31 October** of the current year |
| Income tax return (Form 11) for prior year | **31 October** of the following year |
| Balance of tax for prior year | **31 October** of the following year |

### ROS (Revenue Online Service) Filing

| Obligation | Deadline |
|------------|----------|
| Preliminary tax for current year | **Mid-November** (typically 14-16 November) -- extended deadline |
| Income tax return (Form 11) for prior year | **Mid-November** of the following year |
| Balance of tax for prior year | **Mid-November** of the following year |

**The ROS extended deadline is usually 2 weeks after 31 October. The exact date is published annually by Revenue.**

### Key Dates Example (Tax Year 2025)

| Event | Paper Deadline | ROS Deadline |
|-------|---------------|-------------|
| Pay 2025 preliminary tax | 31 Oct 2025 | ~14 Nov 2025 |
| File 2024 Form 11 | 31 Oct 2025 | ~14 Nov 2025 |
| Pay 2024 balance of tax | 31 Oct 2025 | ~14 Nov 2025 |
| Pay 2026 preliminary tax | 31 Oct 2026 | ~14 Nov 2026 |
| File 2025 Form 11 | 31 Oct 2026 | ~14 Nov 2026 |

---

## Step 5: Consequences of Underpayment [T1]

**Legislation:** TCA 1997, s.1080

### Interest on Late/Insufficient Payment

| Period | Daily Rate | Approximate Annual Rate |
|--------|-----------|------------------------|
| From due date | 0.0219% per day | ~8% per annum |

Interest runs from the due date to the date of actual payment.

### Surcharge for Late Filing

**Legislation:** TCA 1997, s.1084

| Delay | Surcharge |
|-------|-----------|
| Filed within 2 months of deadline | 5% of tax due (max EUR 12,695) |
| Filed more than 2 months late | 10% of tax due (max EUR 63,485) |

**The surcharge applies to the RETURN filing, not the payment. Even if payment is on time, a late return triggers the surcharge.**

---

## Step 6: First Year of Self-Assessment [T1]

**Legislation:** TCA 1997, s.959AN(3)

| Situation | Preliminary Tax Rule |
|-----------|---------------------|
| First year of self-assessment (no prior-year liability) | Pay 90% of estimated current-year liability |
| Transitioning from PAYE-only to self-assessment | 100% rule based on prior-year self-assessed component only |

In the first year, the 100% rule is not available (no prior-year self-assessed liability exists). The taxpayer must estimate and pay 90%.

---

## Step 7: CGT Preliminary Tax [T1]

**Legislation:** TCA 1997, s.31

CGT has separate payment dates from income tax preliminary tax:

| Disposal Period | Payment Deadline |
|----------------|-----------------|
| 1 January -- 30 November | 15 December of the same year |
| 1 December -- 31 December | 31 January of the following year |

**CGT preliminary tax is NOT part of the 31 October / mid-November payment. It has its own schedule.**

---

## Step 8: PRSI Class S [T1]

**Legislation:** Social Welfare Acts

| Parameter | Value |
|-----------|-------|
| Rate | 4% |
| Minimum annual contribution | EUR 500 (even if 4% of income is less) |
| Applied to | All self-employment income without upper limit |
| Exemption | Income below EUR 5,000 -- no PRSI due |

PRSI is included in the preliminary tax payment and collected through self-assessment.

---

## Step 9: Edge Case Registry

### EC1 -- Prior-year liability under EUR 200 [T1]
**Situation:** Client's prior-year total liability was EUR 150.
**Resolution:** No preliminary tax obligation. The de minimis threshold means no payment is required for the current year under the 100% rule. However, the client must still file the return on time.

### EC2 -- Income dropped significantly [T1]
**Situation:** Client earned EUR 80,000 last year (liability EUR 25,000) but expects only EUR 20,000 this year.
**Resolution:** Client can use the 90% rule: estimate current-year liability (approx EUR 3,000) and pay 90% = EUR 2,700. This saves cash flow vs the 100% rule (EUR 25,000). Risk: if estimate is too low, interest applies on the shortfall.

### EC3 -- First year of self-employment [T1]
**Situation:** Client started freelancing in April 2025, previously PAYE only.
**Resolution:** No prior-year self-assessed liability. Must estimate 2025 self-employment income and pay 90% of estimated liability by 31 Oct 2025. Any PAYE credits from employment reduce the amount due.

### EC4 -- ROS vs paper deadline confusion [T1]
**Situation:** Client files on paper but thought they had the ROS extended deadline.
**Resolution:** Paper deadline is strictly 31 October. The ~2-week extension ONLY applies to ROS filers who both file AND pay through ROS. Client is late if payment arrives after 31 October.

### EC5 -- Capital gain in August [T1]
**Situation:** Client sold an investment property in August with a EUR 50,000 gain.
**Resolution:** CGT = EUR 50,000 x 33% = EUR 16,500. Due by 15 December (disposal in Jan-Nov period). This is SEPARATE from the 31 Oct preliminary tax payment for income tax/USC/PRSI.

### EC6 -- PAYE employee with rental income [T1]
**Situation:** Client is a PAYE employee with EUR 12,000 rental income.
**Resolution:** Preliminary tax applies to the rental income (Case V). 100% rule: pay prior-year Case V liability. PAYE credits from employment offset some of the income tax. PRSI Class S applies if total self-assessed income > EUR 5,000.

### EC7 -- Direct debit instalments (105% rule) [T2]
**Situation:** Client wants to spread preliminary tax payments monthly via direct debit.
**Resolution:** Revenue offers a direct debit option. The 105% of pre-prior-year rule applies. Payments are spread evenly across the year. [T2] -- confirm current direct debit arrangement with Revenue.

### EC8 -- Surcharge risk on late return [T1]
**Situation:** Client pays preliminary tax on time but files Form 11 two weeks late.
**Resolution:** Payment is on time -- no interest. But the return is late: 5% surcharge on tax due (up to EUR 12,695) applies. The surcharge is triggered by the return, not the payment.

---

## Step 10: Test Suite

### Test 1 -- Standard 100% rule
**Input:** Prior-year final liability EUR 15,000 (income tax EUR 9,000 + USC EUR 3,500 + PRSI EUR 2,500). Current year expected similar.
**Expected output:** Preliminary tax = EUR 15,000 (100% of prior year). Due 31 Oct (paper) or ~14 Nov (ROS).

### Test 2 -- 90% rule, income drop
**Input:** Prior-year liability EUR 30,000. Current year estimated liability EUR 10,000.
**Expected output:** 90% rule: EUR 10,000 x 90% = EUR 9,000. Saves EUR 21,000 vs 100% rule. Risk flag: if actual liability exceeds EUR 10,000, interest applies.

### Test 3 -- First year, no prior liability
**Input:** First year of self-employment. Estimated income EUR 60,000. Estimated tax: income tax EUR 11,000 + USC EUR 2,400 + PRSI EUR 2,400 = EUR 15,800.
**Expected output:** 90% rule (only option). Preliminary tax = EUR 15,800 x 90% = EUR 14,220.

### Test 4 -- De minimis (prior year < EUR 200)
**Input:** Prior-year self-assessed liability EUR 120.
**Expected output:** No preliminary tax obligation. Still must file Form 11.

### Test 5 -- CGT separate payment
**Input:** Income preliminary tax EUR 12,000 (due 31 Oct). CGT on June disposal EUR 8,250.
**Expected output:** Income preliminary: EUR 12,000 due 31 Oct. CGT: EUR 8,250 due 15 Dec. Two separate payments.

### Test 6 -- Late return surcharge
**Input:** Tax due EUR 20,000. Return filed 6 weeks late (within 2 months).
**Expected output:** Surcharge = 5% x EUR 20,000 = EUR 1,000. Plus interest on any late payment at 0.0219%/day.

### Test 7 -- PAYE + self-employment
**Input:** PAYE salary EUR 50,000 (PAYE deducted at source). Self-employment income EUR 25,000. Prior year self-assessed component liability EUR 8,000.
**Expected output:** Preliminary tax = EUR 8,000 (100% of prior-year self-assessed portion). PAYE employment tax handled by employer.

---

## PROHIBITIONS

- NEVER tell a client the 100% rule requires estimating current-year income -- it does NOT, it uses prior-year final liability only
- NEVER confuse the paper deadline (31 Oct) with the ROS deadline (~mid-Nov)
- NEVER include CGT in the 31 October preliminary tax payment -- CGT has its own separate dates
- NEVER forget USC and PRSI when computing "tax liability" -- preliminary tax covers all three
- NEVER ignore the surcharge for late filing -- it applies even if payment is on time
- NEVER apply the 105% rule without confirming the client is on a direct debit arrangement
- NEVER tell a first-year self-employed person to use the 100% rule -- they must use the 90% rule
- NEVER ignore the EUR 200 de minimis threshold -- below this, no preliminary tax is required
- NEVER present preliminary tax amounts as final tax -- the balance (positive or negative) is settled with the Form 11

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
