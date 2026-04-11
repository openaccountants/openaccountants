---
name: jp-estimated-tax
description: >
  Use this skill whenever asked about Japanese estimated tax prepayments (yotei nozei / 予定納税) for self-employed individuals, freelancers, or sole proprietors. Trigger on phrases like "予定納税", "yotei nozei", "estimated tax Japan", "Japanese advance tax", "予定納税基準額", "reduction application", "予定納税額の減額申請", or any question about advance income tax obligations under the Income Tax Act (所得税法). This skill covers the two-instalment schedule (July and November), the JPY 150,000 threshold, reduction applications, penalties for non-payment, and payment procedures. ALWAYS read this skill before touching any estimated tax work for Japan.
version: 1.0
jurisdiction: JP
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Japan Estimated Tax (予定納税 / Yotei Nozei) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Japan |
| Jurisdiction Code | JP |
| Primary Legislation | Income Tax Act (所得税法), Arts. 104-108 (予定納税 obligation and computation); Art. 120 (final return); Art. 2-1-8 (definitions) |
| Supporting Legislation | National Tax General Act (国税通則法), Arts. 60-63 (delinquent tax/penalties); Income Tax Act Art. 111 (reduction application / 減額申請) |
| Tax Authority | National Tax Agency (国税庁 / NTA) |
| Rate Publisher | NTA |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by Japanese zeirishi (税理士) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: instalment schedule, JPY 150,000 threshold, payment procedure, basic penalty calculation. Tier 2: reduction application, disaster relief provisions, blue return interaction. Tier 3: cross-border income, treaty credits, non-resident estimated tax. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Zeirishi must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any yotei nozei figure, you MUST know:

1. **Prior year income tax from final return (確定申告)** [T1] -- specifically the 予定納税基準額 (yotei nozei kijun-gaku / baseline amount)
2. **Nature of income** [T1] -- business income (事業所得), professional income, real estate income, etc.
3. **Withholding tax (源泉徴収) already deducted** [T1] -- reduces final tax but does not directly reduce yotei nozei
4. **Current year income trend** [T2] -- needed if applying for reduction
5. **Blue return (青色申告) status** [T1] -- affects deductions but not yotei nozei schedule
6. **Any disaster or special circumstances?** [T2] -- may qualify for reduction or deferral

**If the 予定納税基準額 is less than JPY 150,000, no yotei nozei is required.**

---

## Step 1: Determine Yotei Nozei Obligation [T1]

**Legislation:** Income Tax Act, Art. 104

### The Baseline Amount (予定納税基準額)

The baseline is calculated from the prior year's final return. It is the income tax on income from recurring sources (excluding capital gains from asset sales, retirement income, timber income, and one-off income), minus withholding tax credits on those recurring sources.

```
baseline_amount = prior_year_tax_on_recurring_income - withholding_on_recurring_income
if baseline_amount >= 150,000:
    yotei_nozei_required = YES
else:
    yotei_nozei_required = NO
```

### Who Must Pay

| Category | Yotei Nozei Required? |
|----------|----------------------|
| Self-employed with baseline >= JPY 150,000 | YES |
| Freelancer with baseline >= JPY 150,000 | YES |
| Real estate income earner with baseline >= JPY 150,000 | YES |
| Salary earner with no other income (withholding covers all) | NO |
| Any person with baseline < JPY 150,000 | NO |
| First year of activity, no prior return | NO |

---

## Step 2: Instalment Schedule [T1]

**Legislation:** Income Tax Act, Arts. 104, 107

### Payment Schedule

| Instalment | Due Date | Amount |
|------------|----------|--------|
| 1st (第1期) | 1-31 July | 1/3 of baseline amount |
| 2nd (第2期) | 1-30 November | 1/3 of baseline amount |
| Final (確定申告) | 16 Feb - 15 Mar (next year) | Remaining balance (actual tax - yotei nozei paid) |

**Each instalment is exactly one-third of the 予定納税基準額.**

### Example: Baseline Amount = JPY 600,000

| Instalment | Period | Amount |
|------------|--------|--------|
| 1st instalment | July 2025 | JPY 200,000 |
| 2nd instalment | November 2025 | JPY 200,000 |
| Final return | Feb-Mar 2026 | Actual tax - JPY 400,000 (may be refund or balance due) |

---

## Step 3: Reduction Application (減額申請) [T2]

**Legislation:** Income Tax Act, Art. 111

### When to Apply for Reduction

| Trigger | Action |
|---------|--------|
| Current year income significantly lower than prior year | File 予定納税額の減額申請書 |
| Business closed or suspended during the year | File reduction application |
| Disaster, illness, or other extraordinary circumstances | File reduction application |
| Significant increase in deductions (e.g., new dependents) | File reduction application |

### Application Deadlines

| Instalment | Application Deadline |
|------------|---------------------|
| 1st instalment (July) reduction | By 15 July |
| 2nd instalment (November) reduction | By 15 November |

### Application Process

1. Complete the 予定納税額の減額申請書 (Application for Reduction of Estimated Tax)
2. Attach a statement showing estimated income and tax for the current year through 30 June (for 1st instalment) or 31 October (for 2nd instalment)
3. Submit to the jurisdictional tax office (所轄税務署)
4. The tax office reviews and issues approval or denial

**WARNING:** The application must include a reasonable estimate. If the NTA determines the estimate was unreasonably low, penalties may apply.

---

## Step 4: Penalties for Non-Payment [T1]

**Legislation:** National Tax General Act (国税通則法), Arts. 60, 63

### Delinquent Tax (延滞税 / Entaizei)

| Period | Rate (2025) |
|--------|-------------|
| First 2 months from due date | 2.4% per annum (tokureizei rate, reviewed annually) |
| After 2 months | 8.7% per annum (standard entaizei rate) |

### Computation

```
if payment_date > due_date:
    days_late = payment_date - due_date
    if days_late <= 60:
        penalty = unpaid_amount x 2.4% x days_late / 365
    else:
        penalty_first_60 = unpaid_amount x 2.4% x 60 / 365
        penalty_remaining = unpaid_amount x 8.7% x (days_late - 60) / 365
        penalty = penalty_first_60 + penalty_remaining
```

### No Penalty Surcharge (加算税)

**Yotei nozei is not subject to additional penalty surcharges (加算税) because it is a prepayment, not a return-based assessment.** Delinquent tax (延滞税) is the only consequence of late payment.

---

## Step 5: Payment Procedure [T1]

### Payment Methods

| Method | Details |
|--------|---------|
| e-Tax (電子納税) | Online payment via e-Tax system |
| Direct debit (振替納税) | Pre-registered bank account -- automatic deduction (typically about 1 month after due date) |
| Bank counter (金融機関窓口) | Pay at any bank or post office with 納付書 (payment slip) |
| Convenience store | For amounts up to JPY 300,000 with barcode payment slip |
| Credit card | Via the 国税クレジットカードお支払サイト (with processing fee) |
| QR code / smartphone | Pay via Pay-easy or smartphone payment apps |

### Payment Slip Details

| Field | Value |
|-------|-------|
| Tax type | 申告所得税及復興特別所得税 (Income Tax and Special Reconstruction Tax) |
| Tax year | 2025 (令和7年分) |
| Type | 予定 (estimated) |
| Amount | Per instalment |

**If using 振替納税 (direct debit), the actual deduction date is typically around late July for the 1st instalment and late December for the 2nd instalment. No penalty applies for the delay between the official due date and the debit date.**

---

## Step 6: Interaction with Final Return [T1]

**Legislation:** Income Tax Act, Art. 120

```
actual_tax = income_tax_on_2025_final_return + special_reconstruction_tax
total_yotei_nozei_paid = 1st_instalment + 2nd_instalment
if actual_tax > total_yotei_nozei_paid:
    balance_due = actual_tax - total_yotei_nozei_paid  # pay with final return
else:
    refund = total_yotei_nozei_paid - actual_tax  # claimed on final return
```

**Overpayment of yotei nozei results in a refund processed through the final return.**

---

## Step 7: Edge Cases

### EC1 -- First year of business [T1]
**Situation:** Client started freelance business in 2025, no prior year return.
**Resolution:** No yotei nozei obligation. Tax is settled entirely through the final return in Feb-Mar 2026.

### EC2 -- Prior year included large one-off capital gain [T1]
**Situation:** Baseline amount is inflated by one-off capital gain.
**Resolution:** Capital gains from asset sales are excluded from the baseline calculation. The 予定納税基準額 should already exclude them. If incorrectly included, contact the tax office for correction.

### EC3 -- Income dropped significantly mid-year [T2]
**Situation:** Client's business income dropped 50% compared to prior year.
**Resolution:** File 減額申請 by 15 July (for 1st instalment) or 15 November (for 2nd instalment). [T2] flag -- zeirishi should prepare the estimate.

### EC4 -- Disaster relief [T2]
**Situation:** Client affected by natural disaster.
**Resolution:** Special deferral or reduction provisions may apply under the Disaster Tax Relief Act (災害減免法). [T2] flag -- consult zeirishi.

---

## Self-Checks

Before delivering output, verify:

- [ ] 予定納税基準額 confirmed from prior year return
- [ ] JPY 150,000 threshold checked
- [ ] Instalments correctly calculated as 1/3 each
- [ ] Reduction application deadlines identified if applicable
- [ ] Delinquent tax rates current for the applicable year
- [ ] Payment method appropriate for the amount

---

## PROHIBITIONS

- NEVER compute yotei nozei without confirming the 予定納税基準額
- NEVER include capital gains, retirement, or one-off income in the baseline calculation
- NEVER forget that each instalment is 1/3 (not 1/2) of the baseline
- NEVER advise filing a reduction application without [T2] flag for zeirishi review
- NEVER apply penalty surcharge (加算税) to yotei nozei -- only delinquent tax (延滞税) applies
- NEVER present yotei nozei amounts as definitive -- advise client to confirm with their zeirishi

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a zeirishi or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
