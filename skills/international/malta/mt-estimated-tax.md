---
name: mt-estimated-tax
description: >
  Use this skill whenever asked about Malta provisional tax (estimated tax) for self-employed or self-occupied individuals. Trigger on phrases like "provisional tax Malta", "estimated tax", "PT instalments", "how much provisional tax do I pay", "20% 30% 50%", "April instalment", "August instalment", "December instalment", "TA24 overpayment", "refund of provisional tax", "Chapter 372", "ITA provisional tax", or any question about Malta's advance income tax payment obligations. Covers the three-instalment schedule (20/30/50), basis of computation (prior year assessment), first-year rules, minimum provisional tax, penalties for late payment, and interaction with the TA24 final assessment. ALWAYS read this skill before touching any Malta provisional tax work.
version: 1.0
jurisdiction: MT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Malta Provisional Tax (PT) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Malta |
| Jurisdiction Code | MT |
| Primary Legislation | Income Tax Act, Chapter 123; Income Tax Management Act, Chapter 372 |
| Supporting Legislation | Provisional Tax Rules (S.L. 372.04); Income Tax Act Article 14 (deductions) |
| Tax Authority | Commissioner for Revenue (CFR), Malta |
| Filing Portal | CFR Online Services (cfr.gov.mt) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Malta-warranted CPA |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | Year of Assessment 2025 (Basis Year 2024) |
| Confidence Coverage | Tier 1: instalment schedule, percentage splits, prior-year basis, penalty rates, TA24 reconciliation. Tier 2: first-year penultimate-year rule, new business minimum PT, refund vs credit election. Tier 3: group companies, partnership PT, non-resident PT obligations. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Warranted accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any provisional tax figure, you MUST know:

1. **Year of assessment** [T1] -- confirm which YA (e.g., YA 2025 = basis year 2024)
2. **Prior year tax assessment (TA24)** [T1] -- the final tax liability from the most recent TA24. This is the basis for PT computation.
3. **Has a prior year TA24 been filed and assessed?** [T1] -- if no prior assessment exists, special rules apply (see Step 3)
4. **Is this the first year of self-employment?** [T2] -- penultimate year rule may apply
5. **Tax credits applied in prior year** [T1] -- PT is based on NET tax payable (after credits)
6. **Any PAYE or withholding tax deducted at source in current year** [T1] -- reduces effective PT obligation
7. **Is the client a new business?** [T2] -- minimum PT rules may apply

**If no prior year tax assessment is available and this is not a first year, STOP. Request the latest TA24 assessment or CFR statement.**

---

## Step 1: Legal Framework [T1]

**Legislation:** Income Tax Management Act, Chapter 372; Provisional Tax Rules (S.L. 372.04)

Provisional tax is an advance payment of income tax, paid in three instalments during the year of assessment. It is based on the tax assessed for the preceding year of assessment (the "basis year" tax).

| Concept | Detail |
|---------|--------|
| Who must pay | Every person chargeable to income tax who is NOT fully covered by PAYE |
| Legal basis | Chapter 372, Article 44 et seq. |
| Computation basis | Tax chargeable for the preceding year of assessment |
| Currency | EUR |

---

## Step 2: Three-Instalment Schedule [T1]

**Legislation:** S.L. 372.04, Rule 3

| Instalment | Percentage | Due Date | Basis |
|------------|-----------|----------|-------|
| 1st | 20% | 30 April | 20% of prior year's tax liability |
| 2nd | 30% | 31 August | 30% of prior year's tax liability |
| 3rd | 50% | 21 December | 50% of prior year's tax liability |

**Total: 100% of the prior year's assessed tax is paid in advance across three instalments.**

### Formula

```
PT_instalment_1 = prior_year_tax × 20%
PT_instalment_2 = prior_year_tax × 30%
PT_instalment_3 = prior_year_tax × 50%
```

Where `prior_year_tax` = the total tax chargeable as per the most recent TA24 assessment, AFTER tax credits, MINUS any tax deducted at source (e.g., Article 12 withholding tax on interest).

### Calculation Examples (YA 2025)

| Prior Year Tax (YA 2024) | 1st (20%, 30 Apr) | 2nd (30%, 31 Aug) | 3rd (50%, 21 Dec) | Total PT |
|--------------------------|-------------------|-------------------|-------------------|----------|
| EUR 5,000 | EUR 1,000 | EUR 1,500 | EUR 2,500 | EUR 5,000 |
| EUR 12,000 | EUR 2,400 | EUR 3,600 | EUR 6,000 | EUR 12,000 |
| EUR 800 | EUR 160 | EUR 240 | EUR 400 | EUR 800 |

---

## Step 3: Special Rules for First Year and New Businesses [T2]

**Legislation:** S.L. 372.04, Rule 5

### First Year of Self-Employment

| Scenario | PT Basis |
|----------|----------|
| First year, no prior TA24 | PT based on the penultimate year's tax (i.e., the tax for the year before the basis year). If no penultimate year assessment exists, minimum PT applies. |
| Second year, first TA24 now available | PT reverts to the standard prior-year basis |

### Minimum Provisional Tax (New Business)

Where there is no prior or penultimate year assessment, the CFR may set a minimum provisional tax amount. This is determined administratively and may vary. [T2] -- confirm the minimum amount with CFR or client's prior correspondence.

**Flag for reviewer whenever first-year or new-business PT is being computed.**

---

## Step 4: Payment and Filing [T1]

**Legislation:** S.L. 372.04

| Requirement | Detail |
|-------------|--------|
| Payment method | Online via CFR portal, bank transfer, or cheque |
| PT notification | CFR issues PT notices with instalment amounts |
| Self-assessment | If no PT notice received, taxpayer must still compute and pay |
| Rounding | Round each instalment to nearest cent |

### Important: PT is a PAYMENT, not a separate return.

There is no separate "PT return" to file. The taxpayer simply pays the instalment amounts by the due dates. The final reconciliation happens on the TA24.

---

## Step 5: Interaction with TA24 Final Assessment [T1]

**Legislation:** Income Tax Act, Chapter 123; Chapter 372, Article 46

| Scenario | Treatment |
|----------|-----------|
| PT paid = Final tax | No further payment or refund |
| PT paid < Final tax | Balance due with TA24 (by 30 June of year following YA) |
| PT paid > Final tax | Overpayment: taxpayer may request a refund or credit against next year's PT |

### Reconciliation Formula

```
balance_due = final_tax_liability - total_PT_paid - WHT_at_source
if balance_due > 0: additional payment required with TA24
if balance_due < 0: refund or credit
```

### Refund vs Credit

| Option | Detail |
|--------|--------|
| Refund | Taxpayer submits written request to CFR. Processing may take 6-12 months. |
| Credit | Overpayment is automatically set off against next year's PT (faster, more common) |

**[T2] If the overpayment is substantial (e.g., >EUR 2,000), flag for reviewer to advise client on refund vs credit strategy.**

---

## Step 6: Penalties for Late Payment [T1]

**Legislation:** Chapter 372, Article 49; Income Tax Act, Article 50

| Penalty | Rate |
|---------|------|
| Late payment interest | 0.75% per month (9% per annum) on the unpaid instalment |
| Maximum interest | No statutory cap -- accrues until paid |
| Additional penalty | CFR may impose an additional 10% penalty on amounts outstanding after the final due date |
| Prosecution | Persistent non-payment may result in enforcement action |

### Interest Computation

```
interest = unpaid_amount × 0.75% × months_overdue
```

Interest runs from the due date of each instalment, not from the end of the year.

**WARNING:** Interest accrues per instalment. A missed April instalment accrues interest for 8+ months by December, compounding the cost significantly.

---

## Step 7: Adjusting Provisional Tax [T2]

**Legislation:** S.L. 372.04, Rule 6

If the taxpayer expects current year income to be significantly lower than the prior year:

| Option | Detail |
|--------|--------|
| Application to reduce | Taxpayer may apply in writing to CFR to reduce PT instalments |
| Basis | Must provide evidence (e.g., reduced contracts, cessation of activity) |
| Risk | If actual tax exceeds reduced PT, interest and penalties may apply on the shortfall |
| Timing | Application should be made before the relevant instalment due date |

**[T2] Always flag for reviewer before advising a client to reduce PT. Incorrect reduction exposes the client to penalties.**

---

## Step 8: Edge Case Registry

### EC1 -- No prior year TA24 assessment available [T2]
**Situation:** Client has been self-employed for 3 years but has never filed a TA24.
**Resolution:** CFR may issue estimated assessments. PT should be based on the latest CFR-issued assessment (even if estimated). If no assessment exists at all, SA minimum or CFR-determined amount applies. [T2] flag for reviewer -- client needs to regularise filing history urgently.

### EC2 -- Prior year resulted in zero tax (below personal allowance) [T1]
**Situation:** Client's prior year income was below the personal allowance threshold. Tax liability = EUR 0.
**Resolution:** PT = EUR 0. No instalments required. However, if current year income is expected to exceed the threshold, voluntary PT payments are prudent to avoid a large balancing payment.

### EC3 -- Client switches from employment to self-employment mid-year [T2]
**Situation:** Client was PAYE-employed until June, then started freelancing in July.
**Resolution:** First year of self-employment. Penultimate-year rule applies for PT. PAYE already deducted covers the employment portion. PT applies only to the self-employment income. [T2] flag for reviewer to confirm split-year treatment.

### EC4 -- Provisional tax on rental income [T1]
**Situation:** Client has self-employment income AND rental income. Rental income is subject to 15% final withholding tax.
**Resolution:** Rental income taxed at 15% final WHT is NOT included in the PT computation. PT applies only to income subject to progressive rates and not already covered by final WHT.

### EC5 -- Overpayment carried forward but client wants refund instead [T2]
**Situation:** Client has EUR 3,000 overpayment from YA 2024. CFR has credited it against YA 2025 PT. Client wants cash refund.
**Resolution:** Client must submit written request to CFR to reverse the credit and process a refund. Processing time is 6-12 months. [T2] flag for reviewer -- advise on cash flow implications.

### EC6 -- Client ceases self-employment mid-year [T2]
**Situation:** Client closes business in May. 1st PT instalment already paid. 2nd and 3rd not yet due.
**Resolution:** Client should apply to CFR to cancel remaining PT instalments. Final TA24 for the cessation year will reconcile actual liability. Overpaid PT will be refunded or credited. [T2] flag for reviewer.

### EC7 -- PT notice amount differs from client's own calculation [T1]
**Situation:** CFR PT notice states EUR 6,000 total; client calculates EUR 5,200 based on TA24.
**Resolution:** The CFR notice prevails unless the client appeals. Differences typically arise from CFR adjustments to the prior year assessment. Client should pay the CFR-stated amount and query the discrepancy separately. Paying less than the notice amount triggers penalties on the shortfall.

### EC8 -- Client has both Maltese and foreign source income [T2]
**Situation:** Client earns EUR 30,000 from Malta and EUR 20,000 from abroad (double taxation relief claimed).
**Resolution:** PT is based on the NET tax from the prior TA24 (which already factors in DTR). If DTR reduced prior year tax to EUR 3,000, PT = EUR 3,000. [T2] flag for reviewer to confirm DTR will be similarly available in the current year.

### EC9 -- Late filing of prior year TA24 means PT basis is uncertain [T2]
**Situation:** Prior year TA24 not yet filed when April PT instalment is due.
**Resolution:** Use the LATEST available assessed year as the basis. If YA 2024 TA24 is not filed, use YA 2023 assessment. File the overdue TA24 as soon as possible. CFR may issue revised PT notices once the TA24 is processed. [T2] flag for reviewer.

---

## Step 9: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Warranted accountant must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to warranted accountant. Document gap.
```

---

## Step 10: Test Suite

### Test 1 -- Standard three-instalment computation
**Input:** Prior year TA24 tax liability = EUR 9,000.
**Expected output:** 1st instalment (30 Apr) = EUR 1,800. 2nd instalment (31 Aug) = EUR 2,700. 3rd instalment (21 Dec) = EUR 4,500. Total PT = EUR 9,000.

### Test 2 -- Zero prior year tax
**Input:** Prior year TA24 tax liability = EUR 0 (income below personal allowance).
**Expected output:** PT = EUR 0. No instalments due. Flag: advise client to consider voluntary payments if current year income is expected to exceed threshold.

### Test 3 -- Reconciliation with final assessment (underpayment)
**Input:** Total PT paid = EUR 8,000. Final TA24 tax liability = EUR 11,500.
**Expected output:** Balance due = EUR 3,500. Due with TA24 filing (by 30 June following YA).

### Test 4 -- Reconciliation with final assessment (overpayment)
**Input:** Total PT paid = EUR 10,000. Final TA24 tax liability = EUR 7,200.
**Expected output:** Overpayment = EUR 2,800. Client may request refund or credit against next year's PT.

### Test 5 -- Late payment penalty calculation
**Input:** 1st instalment of EUR 1,800 due 30 April. Paid 15 July (2.5 months late).
**Expected output:** Interest = EUR 1,800 x 0.75% x 3 months (rounded up) = EUR 40.50. Flag: additional 10% penalty may apply at CFR discretion.

### Test 6 -- First year, no prior assessment
**Input:** First year of self-employment. No prior TA24 or penultimate year assessment.
**Expected output:** [T2] flag for reviewer. Minimum PT amount per CFR administrative determination applies. Request CFR PT notice or prior correspondence.

### Test 7 -- Rental income excluded from PT basis
**Input:** Prior year TA24: EUR 3,000 tax on self-employment income + EUR 1,500 tax on rental income (15% final WHT). Total tax = EUR 4,500.
**Expected output:** PT based on EUR 3,000 only (rental income excluded as already covered by final WHT). 1st = EUR 600, 2nd = EUR 900, 3rd = EUR 1,500.

---

## PROHIBITIONS

- NEVER compute PT without the prior year TA24 tax liability (or a CFR PT notice)
- NEVER use current year estimated income as the basis -- PT is always based on PRIOR year assessment
- NEVER advise a client to skip PT payments because they expect lower income -- they must apply to CFR for a reduction
- NEVER ignore the instalment split (20/30/50) -- do not divide by three equally
- NEVER combine income subject to final WHT (e.g., 15% rental WHT) into the PT basis
- NEVER present PT figures as definitive if no CFR notice has been received -- label as estimated
- NEVER advise on PT penalty disputes without escalating to a warranted accountant
- NEVER assume first-year clients owe no PT -- minimum amounts may apply
- NEVER tell a client that overpayment is automatically refunded -- they must apply or accept credit

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
