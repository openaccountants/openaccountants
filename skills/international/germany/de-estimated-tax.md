---
name: de-estimated-tax
description: >
  Use this skill whenever asked about German estimated income tax prepayments (Vorauszahlungen) for self-employed individuals, freelancers, or Freiberufler. Trigger on phrases like "Vorauszahlungen", "Einkommensteuer-Vorauszahlung", "estimated tax Germany", "German advance tax", "EStG 37", "quarterly tax Germany", "Finanzamt prepayment", "adjustment of prepayments", "Vorauszahlungsbescheid", or any question about advance income tax obligations under the Einkommensteuergesetz. Covers the quarterly payment schedule (10 Mar, 10 Jun, 10 Sep, 10 Dec), assessment basis, minimum thresholds, adjustment requests, late payment surcharges, solidarity surcharge interaction, and payment procedures. ALWAYS read this skill before touching any estimated tax work for Germany.
version: 2.0
jurisdiction: DE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Germany Estimated Tax (Vorauszahlungen) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Germany (Federal Republic of Germany) |
| Tax | Income tax prepayments (Einkommensteuer-Vorauszahlungen) |
| Primary legislation | Einkommensteuergesetz (EStG) Paragraph 37 |
| Supporting legislation | Abgabenordnung (AO) Paragraph 240 (late payment surcharge); Solidaritaetszuschlaggesetz (SolZG); AO Paragraph 233a (interest on arrears) |
| Authority | Finanzamt (local tax office) |
| Portal | ELSTER (elster.de) |
| Currency | EUR only |
| Payment schedule | Quarterly: 10 March, 10 June, 10 September, 10 December (equal 25% each) |
| Computation basis | Prior year assessment (Vorauszahlungsbescheid from Finanzamt) |
| Minimum thresholds | EUR 400/year, EUR 100/quarter |
| Grace period | 3 days after due date (Schonfrist) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by German Steuerberater |
| Validation date | Pending |

**Instalment schedule summary:**

| Instalment | Due date | Percentage |
|---|---|---|
| Q1 | 10 March | 25% |
| Q2 | 10 June | 25% |
| Q3 | 10 September | 25% |
| Q4 | 10 December | 25% |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| No Vorauszahlungsbescheid issued | No prepayments due (unless Finanzamt determines otherwise) |
| New freelancer, no prior assessment | No Vorauszahlungen until first assessment issued |
| Income expected to drop | Pay per Bescheid -- apply for Herabsetzung before reducing |
| Solidarity surcharge uncertain | Check EUR 18,130 threshold (singles) |
| Church tax status unknown | Ask -- 8% or 9% of ESt depending on Bundesland |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- the Vorauszahlungsbescheid from the Finanzamt, OR the most recent Einkommensteuerbescheid (assessment notice).

**Recommended** -- the Steuernummer, current year estimated income (if adjustment needed), wage tax certificates (Lohnsteuerbescheinigung) if the client also has employment income.

**Ideal** -- complete Vorauszahlungsbescheid, prior year Steuerbescheid, BWA (Betriebswirtschaftliche Auswertung) for current year projections.

**Refusal policy if minimum is missing -- SOFT WARN.** Without a Vorauszahlungsbescheid or prior assessment, no prepayments are legally due. If the client expects significant income, advise voluntary set-aside.

### Refusal catalogue

**R-DE-ET-1 -- Cross-border income interactions.** Trigger: client has income from multiple countries with DTAA credits affecting prepayments. Message: "Cross-border income and treaty credit timing are outside this skill. Please consult a Steuerberater."

**R-DE-ET-2 -- Partnership prepayment allocation.** Trigger: client asks about Vorauszahlungen for a partnership (Personengesellschaft). Message: "Partnership prepayment allocation is outside this skill."

**R-DE-ET-3 -- Gewerbesteuer computation.** Trigger: client asks about trade tax prepayments. Message: "Gewerbesteuer-Vorauszahlungen are a separate obligation. This skill covers Einkommensteuer only."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as an ESt prepayment.

### 3.1 Finanzamt income tax debits

| Pattern | Treatment | Notes |
|---|---|---|
| FINANZAMT followed by city name | ESt prepayment | Match with Mar/Jun/Sep/Dec timing |
| FA followed by city name | ESt prepayment | Abbreviated form |
| EINKOMMENSTEUER, EST, ESt-VZ | ESt prepayment | Explicit reference |
| VORAUSZAHLUNG, VZ | ESt prepayment | Generic prepayment label |
| LASTSCHRIFT FINANZAMT | ESt prepayment | Direct debit from Finanzamt |

### 3.2 Timing-based identification

| Debit date range | Likely instalment | Confidence |
|---|---|---|
| 8 March -- 15 March | Q1 (10 Mar) | High if payee is Finanzamt |
| 8 June -- 15 June | Q2 (10 Jun) | High |
| 8 September -- 15 September | Q3 (10 Sep) | High |
| 8 December -- 15 December | Q4 (10 Dec) | High |
| 3-day Schonfrist applies | Payment within grace period is on time | |

### 3.3 Solidarity surcharge and church tax debits

| Pattern | Treatment | Notes |
|---|---|---|
| SOLIDARITAETSZUSCHLAG, SOLZ, SOLI | SolZ prepayment | Accompanies ESt, same dates |
| KIRCHENSTEUER, KIST | Church tax prepayment | Accompanies ESt, same dates |

### 3.4 Related but NOT ESt prepayments

| Pattern | Treatment | Notes |
|---|---|---|
| GEWERBESTEUER, GEWST | EXCLUDE | Trade tax prepayment -- separate obligation |
| UMSATZSTEUER, UST | EXCLUDE | VAT payment |
| LOHNSTEUER, LST | EXCLUDE | Wage tax remittance (employer) |
| SAEMNISZUSCHLAG | EXCLUDE | Late payment surcharge |
| NACHZAHLUNG | Flag for reviewer | Year-end balance payment, not a prepayment |
| ERSTATTUNG FINANZAMT | Flag for reviewer | Refund from Finanzamt |

### 3.5 Bank transfer references

| Reference pattern | Treatment | Notes |
|---|---|---|
| Steuernummer + ESt-VZ + quarter/year | ESt prepayment | Standard Kassenzeichen format |
| ESt followed by Q1/Q2/Q3/Q4 | ESt prepayment | Quarter-specific |

---

## Section 4 -- Worked examples

### Example 1 -- Standard quarterly prepayment

**Input:** Vorauszahlungsbescheid sets annual prepayment at EUR 4,000.

| Instalment | Due date | Amount |
|---|---|---|
| Q1 | 10 Mar 2025 | EUR 1,000 |
| Q2 | 10 Jun 2025 | EUR 1,000 |
| Q3 | 10 Sep 2025 | EUR 1,000 |
| Q4 | 10 Dec 2025 | EUR 1,000 |

### Example 2 -- Below minimum threshold

**Input:** Computed annual prepayment = EUR 350.

**Output:** Below EUR 400 annual minimum. Finanzamt will NOT set prepayments.

### Example 3 -- Late payment surcharge

**Input:** Q2 instalment EUR 1,500 due 10 June. Grace period ends 13 June. Payment made 15 July.

**Computation:** Months late = 2 (June and July both commenced). Surcharge = EUR 1,500 x 1% x 2 = EUR 30.

### Example 4 -- Solidarity surcharge check

**Input:** Annual ESt prepayment = EUR 16,000 (EUR 4,000/quarter). Single filer.

**Computation:** ESt EUR 16,000 < EUR 18,130 threshold. SolZ = 0% (fully exempt).

### Example 5 -- Bank statement classification

**Input line:** `10.06.2025 ; LASTSCHRIFT FINANZAMT MUENCHEN ; DEBIT ; ESt-VZ Q2/2025 ; -2,500.00 ; EUR`

**Classification:** ESt prepayment, Q2 2025. Not a deductible business expense -- tax payment.

---

## Section 5 -- Computation rules

### 5.1 How the Finanzamt sets prepayments

```
prior_year_ESt = income tax from last assessment
minus_wage_tax = Lohnsteuer withheld
minus_KapESt = Kapitalertragsteuer withheld
minus_credits = other credits (foreign tax credits etc.)
prepayment_base = prior_year_ESt - wage_tax - KapESt - credits
annual_prepayment = prepayment_base (rounded down to nearest EUR divisible by 4)
quarterly_instalment = annual_prepayment / 4
```

The Finanzamt may adjust upward or downward based on expected income changes.

### 5.2 Minimum thresholds

| Threshold | Amount |
|---|---|
| Minimum annual prepayment | EUR 400 |
| Minimum per instalment | EUR 100 |

Below these thresholds, no prepayments are set.

### 5.3 Weekend/holiday rule

If the 10th falls on a Saturday, Sunday, or public holiday, the due date shifts to the next business day (AO Paragraph 108 Abs. 3).

### 5.4 Adjustment window

The Finanzamt may adjust prepayments until the 15th month after the end of the calendar year. For tax year 2025: adjustments possible until 31 March 2027.

### 5.5 Year-end settlement

```
final_tax = ESt on actual income
total_prepaid = sum of all Vorauszahlungen
if total_prepaid > final_tax: Erstattung (refund)
if total_prepaid < final_tax: Nachzahlung (balance due)
```

### 5.6 Solidarity surcharge on prepayments

| ESt threshold (singles) | Solidarity surcharge |
|---|---|
| ESt <= EUR 18,130 | 0% (fully exempt) |
| EUR 18,130 < ESt <= EUR 33,761 | Sliding scale (Milderungszone) |
| ESt > EUR 33,761 | 5.5% of ESt |

Joint filers: thresholds doubled.

---

## Section 6 -- Penalties and interest

### 6.1 Late payment surcharge (Saeumniszuschlag)

| Element | Rule |
|---|---|
| Rate | 1% per commenced month of outstanding amount |
| Grace period | 3 days after due date (Schonfrist) -- AO Paragraph 240 Abs. 3 |
| Base | Unpaid amount rounded down to nearest EUR 50 |
| Minimum | EUR 0 if rounded amount is below EUR 50 |

### 6.2 Computation

```
if payment_date > due_date + 3_days:
    months_late = number of commenced months from due_date
    surcharge = floor(unpaid_amount / 50) * 50 * 1% * months_late
```

### 6.3 Interest on arrears (Nachzahlungszinsen)

Rate: 0.15% per month (1.8% per year). Interest-free period: 15 months after end of tax year. Applies to both underpayments and overpayments.

---

## Section 7 -- Requesting adjustments

### 7.1 Herabsetzung (reduction)

Taxpayer writes to the Finanzamt (letter or ELSTER message) explaining why current-year income will be lower. Supporting documents (BWA, profit projection) should be attached. Finanzamt issues a new Vorauszahlungsbescheid.

### 7.2 Heraufsetzung (increase)

Taxpayer may voluntarily increase prepayments if income is rising, to avoid a large Nachzahlung.

### 7.3 Risk of reduction

If the reduction is excessive and actual tax exceeds prepayments significantly, Nachzahlungszinsen of 0.15% per month may apply after the 15-month interest-free period.

---

## Section 8 -- Edge cases

**EC1 -- New freelancer, no prior assessment.** No Vorauszahlungsbescheid issued. No prepayments due until the first Steuerbescheid. Client should voluntarily set aside estimated tax.

**EC2 -- Prior year included large one-off capital gain.** Vorauszahlungsbescheid inflated. Request Herabsetzung with evidence the gain was non-recurring.

**EC3 -- Church tax prepayments.** Member of evangelisch or katholisch church: 8% or 9% of ESt depending on Bundesland. Set alongside ESt in the same Vorauszahlungsbescheid, same dates.

**EC4 -- Gewerbesteuer interaction.** Client pays Gewerbesteuer and claims EStG Paragraph 35 credit. Finanzamt should account for the credit when setting ESt prepayments. If not, request adjustment. Flag for Steuerberater.

**EC5 -- Multiple income sources.** Prepayments are set on the net ESt after all source-specific deductions. Verify the Vorauszahlungsbescheid reflects all income types.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Vorauszahlungsbescheid amount confirmed or estimated correctly
- [ ] Minimum thresholds (EUR 400/year, EUR 100/quarter) checked
- [ ] All four quarterly dates identified with weekend/holiday adjustments
- [ ] Solidarity surcharge threshold applied correctly
- [ ] Late payment surcharge computed with 3-day grace period
- [ ] Any adjustment request flagged for reviewer
- [ ] Church tax prepayment included if applicable
- [ ] Gewerbesteuer Paragraph 35 credit considered
- [ ] Year-end settlement formula presented
- [ ] Output labelled as estimated until Vorauszahlungsbescheid confirmed

---

## Section 10 -- Test suite

### Test 1 -- Standard quarterly prepayment
**Input:** Annual prepayment per Bescheid = EUR 4,000.
**Expected:** Q1-Q4 = EUR 1,000 each. Dates: 10 Mar, 10 Jun, 10 Sep, 10 Dec.

### Test 2 -- Below minimum threshold
**Input:** Computed annual prepayment = EUR 350.
**Expected:** Below EUR 400 minimum. No prepayments set.

### Test 3 -- Late payment surcharge
**Input:** Q2 EUR 1,500 due 10 Jun. Paid 15 Jul. Grace period ends 13 Jun.
**Expected:** 2 commenced months. Surcharge = EUR 1,500 x 1% x 2 = EUR 30.

### Test 4 -- Solidarity surcharge exempt
**Input:** Annual ESt = EUR 16,000. Single filer.
**Expected:** Below EUR 18,130. SolZ = 0%.

### Test 5 -- New freelancer
**Input:** Registered as Freiberufler 2025. No prior Steuerbescheid.
**Expected:** No Vorauszahlungen due. Advise voluntary set-aside.

### Test 6 -- Year-end settlement (refund)
**Input:** Total prepaid = EUR 8,000. Final ESt = EUR 6,500.
**Expected:** Erstattung = EUR 1,500.

### Test 7 -- Year-end settlement (balance due)
**Input:** Total prepaid = EUR 8,000. Final ESt = EUR 11,000.
**Expected:** Nachzahlung = EUR 3,000.

---

## Prohibitions

- NEVER compute prepayments without checking whether a Vorauszahlungsbescheid has been issued
- NEVER ignore the EUR 400/EUR 100 minimum thresholds
- NEVER forget the 3-day grace period (Schonfrist) when computing late surcharges
- NEVER apply solidarity surcharge without checking the exemption threshold
- NEVER present prepayment amounts as definitive -- the Vorauszahlungsbescheid is authoritative
- NEVER advise reducing prepayments without warning about Nachzahlungszinsen risk
- NEVER confuse ESt prepayments with Gewerbesteuer prepayments
- NEVER ignore church tax prepayments for church members

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
