---
name: de-estimated-tax
description: >
  Use this skill whenever asked about German estimated income tax prepayments (Vorauszahlungen) for self-employed individuals, freelancers, or Freiberufler. Trigger on phrases like "Vorauszahlungen", "Einkommensteuer-Vorauszahlung", "estimated tax Germany", "German advance tax", "EStG §37", "quarterly tax Germany", "Finanzamt prepayment", "adjustment of prepayments", "Vorauszahlungsbescheid", or any question about advance income tax obligations under the Einkommensteuergesetz. This skill covers the quarterly payment schedule (10 Mar, 10 Jun, 10 Sep, 10 Dec), assessment basis, minimum thresholds, adjustment requests, late payment surcharges, solidarity surcharge interaction, and payment procedures. ALWAYS read this skill before touching any estimated tax work for Germany.
version: 1.0
jurisdiction: DE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Germany Estimated Tax (Vorauszahlungen) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Germany |
| Jurisdiction Code | DE |
| Primary Legislation | Einkommensteuergesetz (EStG) §37 (advance payment assessment); §37a (special cases); Abgabenordnung (AO) §240 (late payment surcharge) |
| Supporting Legislation | EStG §32a (tax rates); Solidaritaetszuschlaggesetz (SolZG) §1-6 (solidarity surcharge on prepayments); AO §227 (remission); AO §222 (deferral) |
| Tax Authority | Finanzamt (local tax office) |
| Rate Publisher | Bundesministerium der Finanzen (BMF) |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by German Steuerberater |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: payment schedule, minimum thresholds, assessment basis, late payment surcharge, payment procedure. Tier 2: adjustment requests mid-year, solidarity surcharge interaction, church tax prepayments. Tier 3: cross-border income interactions, DTAA credit timing, partnership prepayment allocation. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Steuerberater must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any prepayment figure, you MUST know:

1. **Most recent Einkommensteuer assessment (Steuerbescheid)** [T1] -- the Finanzamt bases prepayments on this
2. **Nature of income** [T1] -- Gewerbebetrieb (trade/business), freiberufliche Taetigkeit (profession), Vermietung (rental), Kapitalertraege (capital income)
3. **Has the client received a Vorauszahlungsbescheid?** [T1] -- the official notice sets the amounts
4. **Current year estimated income** [T2] -- needed if requesting an adjustment
5. **Solidarity surcharge status** [T1] -- since 2021 most individuals are exempt (threshold EUR 18,130 ESt for singles)
6. **Church tax liability** [T1] -- if applicable, church tax prepayments are set alongside ESt
7. **Any wage tax withheld (Lohnsteuer)?** [T1] -- reduces the prepayment base
8. **Trade tax (Gewerbesteuer) credit under EStG §35?** [T2] -- affects net ESt liability

**If the Finanzamt has not issued a Vorauszahlungsbescheid and the client has no prior assessment, no prepayments are due unless voluntarily made.**

---

## Step 1: Determine Prepayment Obligation [T1]

**Legislation:** EStG §37 Abs. 1-3

### Who Must Pay Vorauszahlungen

| Category | Prepayments Required? |
|----------|----------------------|
| Self-employed with prior ESt assessment showing tax due after wage tax credits | YES (Finanzamt issues Vorauszahlungsbescheid) |
| Freelancer (Freiberufler) with prior assessment | YES |
| Employee with ONLY wage income (Lohnsteuer covers all) | NO (no Vorauszahlungsbescheid issued) |
| New business, no prior assessment yet | NO (until first assessment is issued) |
| Prior assessment resulted in zero or refund | Typically NO (Finanzamt may still set if income increase expected) |

### Minimum Thresholds [T1]

| Threshold | Amount |
|-----------|--------|
| Minimum annual prepayment | EUR 400 per calendar year |
| Minimum per instalment | EUR 100 per quarter |

**If the computed annual prepayment is below EUR 400, or any single instalment would be below EUR 100, the Finanzamt will NOT set prepayments.**

---

## Step 2: Payment Schedule [T1]

**Legislation:** EStG §37 Abs. 1

### Due Dates

| Instalment | Due Date | Percentage |
|------------|----------|------------|
| Q1 | 10 March | 25% |
| Q2 | 10 June | 25% |
| Q3 | 10 September | 25% |
| Q4 | 10 December | 25% |

**Each instalment is exactly one-quarter of the annual prepayment amount set in the Vorauszahlungsbescheid.**

### Weekend/Holiday Rule

If the 10th falls on a Saturday, Sunday, or public holiday, the due date shifts to the next business day (AO §108 Abs. 3).

### Example: Annual Prepayment Set at EUR 4,000

| Instalment | Due Date | Amount |
|------------|----------|--------|
| Q1 | 10 Mar 2025 | EUR 1,000 |
| Q2 | 10 Jun 2025 | EUR 1,000 |
| Q3 | 10 Sep 2025 | EUR 1,000 |
| Q4 | 10 Dec 2025 | EUR 1,000 |

---

## Step 3: Assessment Basis [T1]

**Legislation:** EStG §37 Abs. 3

### How the Finanzamt Calculates Prepayments

```
prior_year_ESt = income tax from last assessment
minus_wage_tax = Lohnsteuer already withheld
minus_KapESt   = Kapitalertragsteuer withheld (if applicable)
minus_credits  = any other credits (e.g., Anrechnung ausl. Steuern)
prepayment_base = prior_year_ESt - wage_tax - KapESt - credits
annual_prepayment = prepayment_base (rounded down to nearest EUR divisible by 4)
quarterly_instalment = annual_prepayment / 4
```

**The Finanzamt may adjust upward or downward if it expects the current year income to differ materially from the prior year.**

### Adjustment Window [T1]

The Finanzamt may adjust prepayments until the 15th month after the end of the calendar year (EStG §37 Abs. 3 Satz 3). For tax year 2025, adjustments are possible until 31 March 2027.

---

## Step 4: Requesting an Adjustment (Herabsetzung / Heraufsetzung) [T2]

**Legislation:** EStG §37 Abs. 3 Satz 4; AO §163

### When to Request a Reduction

| Trigger | Action |
|---------|--------|
| Income dropped significantly from prior year | File informal application (formloser Antrag) with Finanzamt |
| Large one-time income in prior year inflated the assessment | Request adjustment with explanation |
| New deductions (e.g., children, Vorsorgeaufwendungen) | Provide documentation with request |

### How to Apply

1. Write to the Finanzamt (letter or ELSTER message)
2. Explain why current-year income will differ from the assessment basis
3. Provide supporting documents (e.g., BWA, current profit projection)
4. The Finanzamt issues a new Vorauszahlungsbescheid

**WARNING:** If the reduction is excessive and actual tax exceeds prepayments significantly, Nachzahlungszinsen (interest on arrears under AO §233a) of 0.15% per month (1.8% per year, effective from 1 January 2019 onward under BVerfG ruling) may apply.

---

## Step 5: Late Payment Surcharge [T1]

**Legislation:** AO §240

### Saeumniszuschlag (Late Payment Surcharge)

| Element | Rule |
|---------|------|
| Rate | 1% per commenced month of the outstanding amount |
| Grace period | 3 days after the due date (Schonfrist) -- AO §240 Abs. 3 |
| Base | The unpaid instalment amount (rounded down to nearest EUR 50) |
| Minimum | EUR 0 if rounded amount is below EUR 50 |

### Computation

```
if payment_date > due_date + 3_days:
    months_late = number of commenced months from due_date
    surcharge = floor(unpaid_amount / 50) * 50 * 1% * months_late
```

### Example

| Item | Amount |
|------|--------|
| Instalment due 10 Jun 2025 | EUR 1,500 |
| Grace period ends | 13 Jun 2025 |
| Payment made | 15 Jul 2025 |
| Months late | 2 (Jun and Jul are both commenced months) |
| Rounded base | EUR 1,500 (already divisible by 50) |
| Surcharge | EUR 1,500 x 1% x 2 = EUR 30 |

---

## Step 6: Solidarity Surcharge on Prepayments [T1]

**Legislation:** SolZG §4

### Current Rules (2021 Onward)

| ESt Threshold (Singles) | Solidarity Surcharge |
|------------------------|---------------------|
| ESt <= EUR 18,130 | 0% (fully exempt) |
| EUR 18,130 < ESt <= EUR 33,761 | Sliding scale (Milderungszone) |
| ESt > EUR 33,761 | 5.5% of ESt |

**For joint filers (Zusammenveranlagung), the thresholds are doubled.**

The Finanzamt includes SolZ prepayments in the Vorauszahlungsbescheid alongside ESt prepayments. They share the same due dates.

---

## Step 7: Payment Procedure [T1]

### Payment Methods

| Method | Details |
|--------|---------|
| SEPA Lastschriftmandat (direct debit) | Recommended -- set up with Finanzamt to avoid late surcharges |
| Bank transfer | Transfer to the Finanzamt's bank account with Kassenzeichen as reference |
| ELSTER | Online payment via the ELSTER portal |
| Cash | At the Finanzamt cash desk (limited availability) |

### Key Payment Details

| Field | Value |
|-------|-------|
| Reference | Steuernummer + Vorauszahlungszeitraum (e.g., "ESt-VZ Q2/2025") |
| Recipient | Zustaendiges Finanzamt |
| IBAN | Listed on the Vorauszahlungsbescheid |

**Always retain proof of payment. For bank transfers, the Buchungsdatum (posting date) counts, not the Ueberweisungsdatum (transfer initiation date).**

---

## Step 8: Interaction with Annual Return [T1]

**Legislation:** EStG §36 Abs. 2

### Year-End Settlement

```
final_tax = ESt on actual income for the year
total_prepaid = sum of all Vorauszahlungen paid
if total_prepaid > final_tax:
    refund = total_prepaid - final_tax  # Erstattung
else:
    balance_due = final_tax - total_prepaid  # Nachzahlung
```

### Interest on Arrears (Nachzahlungszinsen) [T2]

**Legislation:** AO §233a

| Element | Rule |
|---------|------|
| Rate | 0.15% per month (1.8% per year) -- effective from 1 Jan 2019 |
| Karenzzeit (interest-free period) | 15 months after end of the tax year (for 2025: interest starts 1 Apr 2027) |
| Applies to | Both underpayments (Nachzahlung) and overpayments (Erstattung) |

---

## Step 9: Edge Cases

### EC1 -- New freelancer, no prior assessment [T1]
**Situation:** Client registered as Freiberufler in 2025, no prior Steuerbescheid.
**Resolution:** No Vorauszahlungen due until the first assessment is issued. Client should set aside estimated tax voluntarily.

### EC2 -- Prior year included large one-off capital gain [T2]
**Situation:** Vorauszahlungsbescheid is inflated due to a one-time capital gain.
**Resolution:** Request Herabsetzung with evidence that the gain was non-recurring.

### EC3 -- Church tax prepayments [T1]
**Situation:** Client is a member of a church (evangelisch or katholisch).
**Resolution:** Church tax prepayments (8% or 9% of ESt depending on Bundesland) are set alongside ESt in the same Vorauszahlungsbescheid with the same quarterly dates.

### EC4 -- Gewerbesteuer interaction [T2]
**Situation:** Client pays Gewerbesteuer and claims the EStG §35 credit.
**Resolution:** The Finanzamt should account for the §35 credit when setting ESt prepayments. If not, request adjustment. [T2] flag -- Steuerberater should confirm credit calculation.

---

## Self-Checks

Before delivering output, verify:

- [ ] Vorauszahlungsbescheid amount confirmed or estimated correctly
- [ ] Minimum thresholds (EUR 400/year, EUR 100/quarter) checked
- [ ] All four quarterly dates identified with weekend/holiday adjustments
- [ ] Solidarity surcharge threshold applied correctly
- [ ] Late payment surcharge computed with 3-day grace period
- [ ] Any adjustment request flagged as [T2]

---

## PROHIBITIONS

- NEVER compute prepayments without checking whether a Vorauszahlungsbescheid has been issued
- NEVER ignore the EUR 400/EUR 100 minimum thresholds
- NEVER forget the 3-day grace period (Schonfrist) when computing late surcharges
- NEVER apply solidarity surcharge without checking the exemption threshold
- NEVER present prepayment amounts as definitive -- the Vorauszahlungsbescheid from the Finanzamt is authoritative
- NEVER advise reducing prepayments without warning about potential Nachzahlungszinsen

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
