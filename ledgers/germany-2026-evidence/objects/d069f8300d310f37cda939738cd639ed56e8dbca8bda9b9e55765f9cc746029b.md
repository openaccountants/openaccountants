---
name: de-estimated-tax
description: Use this skill whenever asked about German estimated income tax prepayments (Vorauszahlungen) for self-employed individuals, freelancers, or Freiberufler. Trigger on phrases like "Vorauszahlungen", "Einkommensteuer-Vorauszahlung", "estimated tax Germany", "German advance tax", "EStG 37", "quarterly tax Germany", "Finanzamt prepayment", "adjustment of prepayments", "Vorauszahlungsbescheid", or any question about advance income tax obligations under the Einkommensteuergesetz. Covers the quarterly payment schedule (10 Mar, 10 Jun, 10 Sep, 10 Dec), assessment basis, minimum thresholds, adjustment requests, late payment surcharges, solidarity surcharge interaction, and payment procedures. ALWAYS read this skill before touching any estimated tax work for Germany.
version: 2.0
jurisdiction: DE
tax_year: 2026
last_updated: 2026-09-19
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# German income tax prepayments (Einkommensteuer-Vorauszahlungen)

"Estimated tax" is a US phrase. The German thing is the Einkommensteuer-Vorauszahlung: advance payments of income tax under § 37 EStG, due four times a year. The taxpayer does not work them out. The tax office (Finanzamt) sets them in a prepayment notice (Vorauszahlungsbescheid), and the taxpayer pays the amounts printed on that notice. This Guide is for individuals: freelancers, sole traders, landlords and anyone else whose income tax is not fully collected by withholding. It covers the four due dates, how the tax office sets and changes the amounts, the solidarity surcharge and church tax that ride on them, late payment, interest, and how to apply for a change. Figures are for tax year 2026. The statute figures are read from the consolidated federal law pages. The church tax range is from the finance ministry's tax booklet, 2025 edition. § 37 EStG prints no safe harbour percentage, no annualised instalment method and no penalty for an estimate that turns out too low: what exists is a surcharge on set amounts that are paid late, and interest on the final balance (Section 6).

## Section 1: Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Germany (Federal Republic of Germany) |
| Tax | Income tax prepayments (Einkommensteuer-Vorauszahlungen) |
| Primary legislation | Einkommensteuergesetz (EStG) § 37 |
| Supporting legislation | Abgabenordnung (AO) § 240 (late payment surcharge), § 224 (day of payment), § 233a and § 238 (interest after assessment), § 164 (prepayment notices are always open to change), § 108 (weekends and public holidays); Solidaritätszuschlaggesetz (SolzG) § 1, § 3, § 4; EStG § 36 (crediting and year-end balance), § 51a (church tax prepayments) |
| Authority | Finanzamt (local tax office) |
| Portal | Mein ELSTER (elster.de) |
| Currency | EUR only |
| Payment schedule | Four dates a year: 10 March, 10 June, 10 September, 10 December |
| Who sets the amount | The tax office, by Vorauszahlungsbescheid. The taxpayer does not self-assess |
| Computation basis | The income tax of the last assessment, after crediting withholding taxes. The tax office may adjust it to the tax it expects for the current year |
| Minimum thresholds | See the table in Section 5.2 |
| Grace period | Three days. Not for payments handed over or sent, such as cash or a cheque. See Section 6.1 |
| Contributor | Open Accountants Community |
| Validated by | Pending. Requires sign-off by a German Steuerberater |
| Validation date | Pending |

**Instalment schedule summary**

| Instalment | Due date | Weekday in 2026 |
| --- | --- | --- |
| Q1 | 10 March | Tuesday |
| Q2 | 10 June | Wednesday |
| Q3 | 10 September | Thursday |
| Q4 | 10 December | Thursday |

The four dates are printed in § 37(1) EStG: https://www.gesetze-im-internet.de/estg/__37.html The notice states the amount for each date. § 37 EStG does not print how the yearly amount is split across the four dates, so this Guide states no split. Read the amounts from the notice.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| No Vorauszahlungsbescheid issued | No income tax prepayment is payable until a notice sets it. Do not invent amounts. Advise the client to set money aside |
| New freelancer, no prior assessment | Do not assume there are no prepayments. The tax office sets them from the expected profit stated in the registration questionnaire (Section 8), but only if they reach the two minimums in the Section 5.2 table. If no notice comes, nothing is payable in advance: set money aside |
| Income expected to drop | Pay what the notice says. Apply for a reduction (Herabsetzung) first, and pay less only once a new notice arrives |
| Solidarity surcharge uncertain | Test the year's prepayments against the limits in the Section 5.6 table |
| Church tax status unknown | Ask. The rate depends on the federal state: see the Section 5.7 table |

## Section 2: Required inputs and refusal catalogue

### Required inputs

**Minimum viable:** the Vorauszahlungsbescheid from the Finanzamt, OR the most recent Einkommensteuerbescheid (assessment notice).

**Recommended:** the Steuernummer, the current year's expected income (if an adjustment is needed), wage tax certificates (Lohnsteuerbescheinigung) if the client also has employment income.

**Ideal:** the complete Vorauszahlungsbescheid, the prior year Steuerbescheid, and a BWA (Betriebswirtschaftliche Auswertung) for current year projections. For a new business: the filed registration questionnaire (Fragebogen zur steuerlichen Erfassung).

**Refusal policy if minimum is missing: SOFT WARN.** Income tax prepayments are payable in the amounts a notice sets (§ 37(3) sentence 1 EStG), and the tax notice is the basis for collecting a tax claim (§ 218(1) AO, https://www.gesetze-im-internet.de/ao_1977/__218.html), and a late payment surcharge does not start before the tax has been set (§ 240(1) sentence 3 AO). With no notice and no prior assessment, say so and do not invent amounts. If the client expects significant income, advise a voluntary set-aside. A new business should expect a notice based on its registration questionnaire if the expected profit leads to prepayments that reach the Section 5.2 minimums.

### Refusal catalogue

- **R-DE-ET-1: Cross-border income interactions.** Trigger: client has income from several countries with treaty credits that affect prepayments. Message: "Cross-border income and treaty credit timing are outside this Guide. Please consult a Steuerberater."
- **R-DE-ET-2: Partnership prepayment allocation.** Trigger: client asks about Vorauszahlungen for a partnership (Personengesellschaft). Message: "Partnership prepayment allocation is outside this Guide."
- **R-DE-ET-3: Gewerbesteuer computation.** Trigger: client asks about trade tax prepayments. Message: "Gewerbesteuer-Vorauszahlungen are a separate obligation. This Guide covers Einkommensteuer only." See `de-trade-tax`.

## Section 3: Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as an ESt prepayment. The patterns are working conventions, not official formats: no official page prints them.

Payee and timing alone are not proof. Other payments to the same tax office also fall on the 10th: a VAT advance payment is due on the tenth day after each advance return period (§ 18(1) UStG, https://www.gesetze-im-internet.de/ustg_1980/__18.html), and wage tax is remitted by the tenth day after each wage tax period (§ 41a(1) EStG, https://www.gesetze-im-internet.de/estg/__41a.html). Match the reference text, or the amount on the Vorauszahlungsbescheid, before classifying.

### 3.1 Finanzamt income tax debits

**Finanzamt income tax debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| FINANZAMT followed by city name | ESt prepayment, if the reference or amount confirms it | Match with Mar/Jun/Sep/Dec timing and the notice |
| FA followed by city name | ESt prepayment, if the reference or amount confirms it | Abbreviated form |
| EINKOMMENSTEUER, EST, ESt-VZ | ESt prepayment | Explicit reference |
| VORAUSZAHLUNG, VZ | Prepayment. Check which tax | Generic prepayment label. Trade tax and VAT also have prepayments |
| LASTSCHRIFT FINANZAMT | Tax debit. Check which tax | Direct debit by the Finanzamt under a SEPA mandate |

### 3.2 Timing-based identification

**Timing-based identification**

| Debit date range | Likely instalment | Confidence |
| --- | --- | --- |
| 8 March to 15 March | Q1 (10 Mar) | High if payee is Finanzamt and the amount matches the notice |
| 8 June to 15 June | Q2 (10 Jun) | High, same conditions |
| 8 September to 15 September | Q3 (10 Sep) | High, same conditions |
| 8 December to 15 December | Q4 (10 Dec) | High, same conditions |
| Three-day grace (Schonfrist) | A transfer credited up to three days after the due date is late, but no surcharge is charged | Section 6.1 |

### 3.3 Solidarity surcharge and church tax debits

**Solidarity surcharge and church tax debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SOLIDARITAETSZUSCHLAG, SOLZ, SOLI | SolZ prepayment | Paid at the same time as the ESt prepayment (§ 1(4) SolzG) |
| KIRCHENSTEUER, KIST | Church tax prepayment | Paid at the same time as the ESt prepayment (§ 51a(4) EStG, applied under state church tax law) |

### 3.4 Related but NOT ESt prepayments

**Related but NOT ESt prepayments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GEWERBESTEUER, GEWST | EXCLUDE | Trade tax prepayment, a separate obligation. Its dates are 15 February, 15 May, 15 August and 15 November |
| UMSATZSTEUER, UST | EXCLUDE | VAT payment. Self-computed in the advance return, due on the tenth day after the period |
| LOHNSTEUER, LST | EXCLUDE | Wage tax remittance (employer), due by the tenth day after the period |
| SAEUMNISZUSCHLAG | EXCLUDE | Late payment surcharge |
| NACHZAHLUNG | Flag for reviewer | Year-end balance payment, not a prepayment |
| ERSTATTUNG FINANZAMT | Flag for reviewer | Refund from Finanzamt |

The trade tax dates are printed in § 19(1) GewStG, and § 19(3) GewStG has the municipality (Gemeinde) adjust those prepayments: https://www.gesetze-im-internet.de/gewstg/__19.html

### 3.5 Bank transfer references

**Bank transfer references**

| Reference pattern | Treatment | Notes |
| --- | --- | --- |
| Steuernummer + ESt-VZ + quarter/year | ESt prepayment | Reference text often seen on transfers. Not an official format |
| ESt followed by Q1/Q2/Q3/Q4 | ESt prepayment | Quarter-specific |

## Section 4: Worked examples

The examples show the method. They carry no invented amounts: the amounts come from the client's notice, and the rates and limits come from the tables in Sections 5 and 6.

### Example 1: Standard quarterly prepayment

**Standard quarterly prepayment instalments**

| Instalment | Due date | Amount |
| --- | --- | --- |
| Q1 | 10 Mar 2026 | As printed on the notice |
| Q2 | 10 Jun 2026 | As printed on the notice |
| Q3 | 10 Sep 2026 | As printed on the notice |
| Q4 | 10 Dec 2026 | As printed on the notice |

**Input:** a Vorauszahlungsbescheid for 2026 that lists an amount for each of the four dates.

**Output:** report the four amounts and dates exactly as the notice prints them. Do not recompute them.

### Example 2: Below minimum threshold

**Input:** the income tax prepayments worked out for the year come to less than the yearly minimum in the Section 5.2 table.

**Output:** the Finanzamt will NOT set prepayments (§ 37(5) sentence 1 EStG). The same holds when the amount for a single due date is below the per-date minimum: both minimums must be met.

### Example 3: Late payment surcharge

**Input:** the Q2 instalment is due on 10 June 2026. The client pays by bank transfer and the tax office's account is credited on 15 July 2026.

**Computation:** the delay is longer than three days, so the grace rule does not help. Two months of the delay have started by 15 July. Round the unpaid instalment down as the Section 6.1 table says, then apply the rate in that table once for each of the two started months.

### Example 4: Solidarity surcharge check

**Input:** single filer. The income tax prepayments set for 2026 do not exceed the single limit in the Section 5.6 table.

**Computation:** no solidarity surcharge prepayment is due, because the surcharge is charged only if the base exceeds the limit (§ 3(3) SolzG). If the prepayments exceed the limit, the surcharge rate in Section 5.6 applies to the whole base, capped by the mitigation rule in the same section.

### Example 5: Bank statement classification

**Input line:** `10.06.2026 ; LASTSCHRIFT FINANZAMT MUENCHEN ; DEBIT ; ESt-VZ Q2/2026 ; amount ; EUR`

**Classification:** ESt prepayment, Q2 2026. Not a deductible business expense: taxes on income may not be deducted from any type of income or from total income, and the same holds for ancillary charges on them, such as a late payment surcharge (§ 12 number 3 EStG). Church tax paid is the exception that § 12 EStG reserves: it is a special expense under § 10(1) number 4 EStG, except where it was paid as a surcharge on investment income tax or on the income tax under the separate rate of § 32d(1) EStG. https://www.gesetze-im-internet.de/estg/__12.html

## Section 5: Computation rules

### 5.1 How the Finanzamt sets prepayments

- **Who sets them.** The tax office sets the prepayments by prepayment notice (§ 37(3) sentence 1 EStG). Prepayments are made on the income tax the taxpayer is expected to owe for the current year (§ 37(1) EStG). https://www.gesetze-im-internet.de/estg/__37.html
- **Prepayment computation formula.** prepayment_base = income tax from the last assessment minus the withholding taxes credited in that assessment (wage tax, investment income tax). § 37(3) sentence 2 EStG says prepayments are "as a rule" (grundsätzlich) measured by this amount.
- **Adjustment to the current year.** The tax office may adjust the prepayments to the income tax it expects for the year (§ 37(3) sentence 3 EStG). To adjust (anpassen) covers a rise and a cut. For a change to prepayments already set, § 37(5) sentence 2 EStG sets minimums for increases only. The time limit is in Section 5.4.
- **Small deductions are left out.** When the base is worked out, these are ignored if together they do not exceed the small-deductions limit in the Section 5.2 table: church tax paid, childcare costs, the client's own vocational training costs, school fees (§ 10(1) numbers 4, 5, 7 and 9 EStG), the special expenses of § 10(1a) EStG, donations (§ 10b EStG), extraordinary burdens (§ 33 EStG) and the amounts of § 33a EStG. Above the limit they count.
- **Always left out.** The tax reduction under § 34a EStG, and the special expenses deduction under § 10a(1) EStG (§ 37(3) sentences 5 and 6). In the cases of § 31 EStG where child benefit does not fully achieve the required tax relief, the child allowances of § 32(6) EStG and the child benefit to be offset are also left out (§ 37(3) sentence 12).
- **Rental losses on a new building.** A loss from letting a building counts for prepayments only for calendar years that begin after the building was bought or completed. If the building is bought before the calendar year in which it is completed, completion takes the place of purchase (§ 37(3) sentence 9). For another let asset within § 21(1) sentence 1 numbers 1 to 3 EStG the same rule applies, with the start of use by the taxpayer in place of purchase or completion (§ 37(3) sentence 11). This limit does not apply to a building for which special depreciation under § 7b EStG, or the increased deductions of §§ 14a, 14c or 14d of the Berlin promotion law, are claimed (§ 37(3) sentences 8 to 10).

### 5.2 Minimum thresholds

**Minimum thresholds table**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__37.html |
| Minimum total of prepayments in the calendar year. Below it, none are set | EUR 400 | § 37(5) sentence 1 EStG: "mindestens 400 Euro im Kalenderjahr" |
| Minimum for one due date. Both minimums must be met (AND) | EUR 100 | § 37(5) sentence 1 EStG: "und mindestens 100 Euro für einen Vorauszahlungszeitpunkt betragen" |
| Minimum increase for one due date, when prepayments already set are raised under § 37(3) sentences 2 to 5 | EUR 100 | § 37(5) sentence 2 EStG: "für einen Vorauszahlungszeitpunkt auf mindestens 100 Euro" |
| Minimum increase in the case of § 37(4): a later increase (nachträgliche Erhöhung), where the last prepayment for the year is adjusted | EUR 5,000 | § 37(5) sentence 2 EStG: "im Fall des Absatzes 4 auf mindestens 5 000 Euro beläuft" |
| Small-deductions limit: the deductions listed in Section 5.1 are left out if together they do not exceed this | EUR 600 | § 37(3) sentence 4 EStG: "insgesamt 600 Euro nicht übersteigen" |

Below the two minimums in the first two rows, no prepayments are set. The minimums are "at least" tests: a yearly total equal to the minimum is enough. They apply to income tax prepayments only. They do not apply to solidarity surcharge prepayments (§ 1(4) SolzG) or to church tax prepayments (§ 51a(4) EStG). The section prints no minimum for a reduction.

### 5.3 Weekend/holiday rule

- **Weekend/holiday shift rule.** If a deadline ends on a Sunday, a public holiday or a Saturday, it ends at the close of the next working day (§ 108(3) AO). https://www.gesetze-im-internet.de/ao_1977/__108.html In 2026 none of the four dates falls on a weekend (see the schedule in Section 1).

### 5.4 Adjustment window

- **Adjustment window.** The tax office may adjust the prepayments for a year until the end of the 15th calendar month after that year (§ 37(3) sentence 3 EStG). For tax year 2026 that month is March 2028. https://www.gesetze-im-internet.de/estg/__37.html
- **Farmers and foresters.** The period is 23 months if income from farming and forestry is expected to outweigh the other income at the first assessment.
- **Older years.** Longer periods applied, on the taxpayer's application, for the years 2019 to 2024 (§ 52(35d) EStG). That rule names no later year, so 2025 and 2026 follow the normal periods. https://www.gesetze-im-internet.de/estg/__52.html
- **A later increase.** When prepayments are raised after the fact, the last prepayment for the year is adjusted, and the increase is due within one month of the notice (§ 37(4) EStG). The minimum for such an increase is in the Section 5.2 table.

### 5.5 Year-end settlement

- **Year-end settlement formula.** final_tax = income tax assessed on actual income. credited = prepayments paid for the year (§ 36(2) number 1 EStG) plus withholding taxes credited (§ 36(2) number 2 EStG). If credited is more than final_tax: Erstattung (refund). If credited is less than final_tax: Nachzahlung, in the statute Abschlusszahlung (balance due). https://www.gesetze-im-internet.de/estg/__36.html
- **When the balance is due.** Within one month of the assessment notice. The part of the balance that equals prepayments already due but not paid is due at once (§ 36(4) sentence 1 EStG).
- **Refund.** An overpayment is paid out after the assessment notice (§ 36(4) sentence 2 EStG).

### 5.6 Solidarity surcharge on prepayments

Where income tax prepayments are payable, the solidarity surcharge is measured on those prepayments (§ 3(1) number 2 SolzG) and paid at the same time (§ 1(4) SolzG, https://www.gesetze-im-internet.de/solzg_1995/__1.html). It is charged only if the base exceeds the limit below. The pages do not print how this test works for a notice issued part way through a year. Use the test to check the notice, not to replace it: a solidarity surcharge prepayment that the notice sets is payable. The base is reduced first by the income tax under § 32d(3) and (4) EStG, and that part always carries the surcharge.

**Solidarity surcharge limits (2026)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/solzg_1995/__3.html |
| Exemption limit (Freigrenze), single assessment. A limit on the tax, not on income | EUR 20,350 | § 3(3) number 2 SolzG: "in anderen Fällen 20 350 Euro übersteigt" |
| Exemption limit for the splitting cases of § 32a(5) and (6) EStG, such as jointly assessed spouses. Per couple, not per person | EUR 40,700 | § 3(3) number 1 SolzG: "Einkommensteuergesetzes 40 700 Euro" |

These limits first apply for assessment period 2026 (§ 6(27) SolzG, https://www.gesetze-im-internet.de/solzg_1995/__6.html). Older material shows lower limits from earlier years.

**Solidarity surcharge rate and mitigation**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Surcharge rate, on the whole base once the limit is exceeded | 5.5% | § 4 sentence 1 SolzG: "Der Solidaritätszuschlag beträgt 5,5 Prozent der Bemessungsgrundlage" |
| Mitigation: the surcharge is not more than this share of the difference between the base and the limit | 11.9% | § 4 sentence 2 SolzG: "Er beträgt nicht mehr als 11,9 Prozent des Unterschiedsbetrages" |

- **The limit is a cliff with a mitigation zone, not an allowance.** Up to the limit nothing is charged. Just above it the mitigation cap applies. Further up, the full rate applies to the whole base. The official pages print no upper end of the mitigation zone, so this Guide states none.
- **Joint filers threshold rule.** Joint filers use the splitting limit printed in the table. Do not double the single limit by hand.

### 5.7 Church tax on prepayments

Church tax is a surcharge tax (Zuschlagsteuer) measured on the income tax. Its prepayments are paid at the same time as the income tax prepayments (§ 51a(4) EStG), and these federal rules apply to church taxes under state law (§ 51a(6) EStG). https://www.gesetze-im-internet.de/estg/__51a.html

**Church tax rate**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 |
| Church tax for members, charged on the income tax and not on the income | 8% or 9% | Ministry booklet, 2025 edition. Set by each state's church tax rules: "je nach Bundesland 8 oder 9 Prozent" |

## Section 6: Penalties and interest

§ 37 EStG prints no penalty for a prepayment that turns out too low. Two things can cost money: paying a set prepayment late (6.1), and interest on the final balance once the interest-free period has passed (6.3).

### 6.1 Late payment surcharge (Saeumniszuschlag)

**Late payment surcharge elements**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ao_1977/__240.html |
| Surcharge for each started month of the delay, on the overdue tax after rounding down | 1% | § 240(1) AO: "ein Säumniszuschlag von 1 Prozent des abgerundeten rückständigen Steuerbetrags" |
| Rounding: the overdue tax is rounded down to the next amount divisible by this | EUR 50 | § 240(1) AO: "abzurunden ist auf den nächsten durch 50 Euro teilbaren Betrag" |

- **Grace period (Schonfrist).** No surcharge is charged for a delay of up to three days (§ 240(3) AO). The section prints the period in words ("bis zu drei Tagen"). The payment is still late. The grace does not apply to payments under § 224(2) number 1 AO: means of payment (Zahlungsmittel) that are handed over or sent, cheques included.
- **Day of payment.** A bank transfer or a payment into the tax office's account counts as paid on the day the amount is credited to the tax authority, not on the day it is sent. A cheque counts as paid three days after the tax office receives it. Other means of payment handed over or sent, such as cash, count on the day of receipt. Where a SEPA direct debit mandate is in place, a validly made payment counts as made on the due date (§ 224(2) AO speaks of a payment that is 'wirksam geleistet'). https://www.gesetze-im-internet.de/ao_1977/__224.html
- **Not before the tax is set.** The delay does not begin before the tax has been set or declared (§ 240(1) sentence 3 AO). This protection is switched off for solidarity surcharge and church tax prepayments. As long as no notice on them has been issued, they are payable without a separate demand, at the same time as the SET income tax prepayments, and § 240(1) sentence 3 AO does not apply to that extent (§ 1(4) sentences 1 to 3 SolzG, § 51a(4) sentences 1 to 3 EStG).
- **Not on ancillary charges.** No surcharge arises on surcharges, interest and other ancillary charges (§ 240(2) AO).
- **Not interest.** The surcharge is charged per started month. Do not convert it into a yearly rate.

### 6.2 Computation

- **Late payment surcharge computation.** If the payment day under § 224(2) AO is more than three days after the due date (or the payment falls under § 224(2) number 1 AO, such as a cheque, and its payment day is after the due date): rounded_amount = unpaid amount rounded down to the next amount divisible by the rounding step in the 6.1 table. surcharge = rounded_amount x the rate in the 6.1 table x the number of started months of the delay. If the rounded amount is nil, there is no surcharge.

### 6.3 Interest on arrears (Nachzahlungszinsen)

**Interest after assessment (§ 233a AO)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ao_1977/__238.html |
| Interest rate per month in § 233a cases, for interest periods from 1 January 2019 | 0.15% | § 238(1a) AO: "0,15 Prozent für jeden Monat" |
| The same rate per year, as the section itself prints it | 1.8% | § 238(1a) AO: "das heißt 1,8 Prozent für jedes Jahr" |
| Rounding: the amount that bears interest is rounded down, for each tax type, to the next amount divisible by this | EUR 50 | § 238(2) AO: "auf den nächsten durch 50 Euro teilbaren Betrag abgerundet" |

- **Interest on arrears rate.** The rates in the table apply to § 233a AO cases only: interest on the difference an income tax assessment produces, in either direction. Other interest, such as interest on a deferral (§ 234 AO), follows § 238(1) AO, which prints its monthly rate in words ("einhalb Prozent"). Do not mix the two.
- **Interest-free period.** Interest starts 15 months after the end of the calendar year in which the tax arose (§ 233a(2) AO). For tax year 2026 that is 1 April 2028. It ends on the day the assessment takes effect. The start is 23 months where farming and forestry income outweighs the other income. It applies to both underpayments and overpayments. https://www.gesetze-im-internet.de/ao_1977/__233a.html
- **Full months only.** Interest is paid for full months. A started month is left out (§ 238(1) sentence 2 AO). This is the opposite of the late payment surcharge, which counts each started month.
- **Prepayments themselves bear no such interest.** § 233a AO does not apply to the setting of prepayments (§ 233a(1) sentence 2 AO).
- **What bears interest.** The assessed tax, less the withholding taxes credited, less the prepayments SET up to the start of the interest period (§ 233a(3) AO). So prepayments set before that date reduce the amount that bears interest.
- **Voluntary payments.** Interest on arrears is not set, or is waived, so far as the taxpayer made payments before the assessment took effect and the tax office accepted them and credited them against the tax (§ 233a(8) AO).
- **Older years.** For 2019 to 2024 the interest-free period was longer (Art. 97 § 36 EGAO). That rule names no later year. https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html

## Section 7: Requesting adjustments

A prepayment notice is always a tax assessment subject to review (§ 164(1) sentence 2 AO), and the taxpayer may apply at any time to have it cancelled or changed (§ 164(2) sentence 2 AO). https://www.gesetze-im-internet.de/ao_1977/__164.html

### 7.1 Herabsetzung (reduction)

The taxpayer applies to the Finanzamt and explains why the current year's income tax will be lower. Mein ELSTER lists a form named "Antrag auf Anpassung von Vorauszahlungen": https://www.elster.de/eportal/formulare-leistungen/alleformulare/eingvorauszlg Supporting documents (BWA, profit projection) should be attached: the federal founders' portal warns that without up-to-date books a business often cannot give the tax office meaningful records with such an application. https://www.existenzgruendungsportal.de/gruenden-kurz-und-knapp/steuern The adjustment is at the tax office's discretion ("kann", § 37(3) sentence 3 EStG). If it agrees, it issues a new Vorauszahlungsbescheid. Until then the amounts on the current notice stay payable: a notice stays in effect as long as it has not been withdrawn, revoked, otherwise cancelled or settled (§ 124(2) AO, https://www.gesetze-im-internet.de/ao_1977/__124.html).

### 7.2 Heraufsetzung (increase)

The taxpayer may apply for higher prepayments in the same way if income is rising, to avoid a large Nachzahlung. The founders' portal advises founders to use this where needed. An increase is made only if it reaches the minimum increase in the Section 5.2 table. For a later increase (nachträgliche Erhöhung) § 37(4) EStG applies: the last prepayment for the year is adjusted, the higher minimum in the table applies, and the increase is due within one month of the notice.

### 7.3 Risk of reduction

If the reduction is excessive and the assessed tax exceeds the prepayments, the balance is due within one month of the assessment notice (Section 5.5), and Nachzahlungszinsen at the rate in the Section 6.3 table may apply once the 15-month interest-free period has passed. § 37 EStG prints no penalty for a prepayment that turns out too low. The application itself must state the facts truthfully and completely. Whoever gives the tax authorities incorrect or incomplete statements about facts that matter for tax, and so causes tax not to be set, not to be set in full or not to be set in time, commits tax evasion (§ 370(1) number 1 and (4) AO). § 370(4) AO says this also holds where the tax is set subject to review, which every prepayment notice is (§ 164(1) sentence 2 AO). https://www.gesetze-im-internet.de/ao_1977/__370.html This Guide does not judge where a forecast crosses that line: refer to a Steuerberater.

## Section 8: Edge cases

**No Vorauszahlungsbescheid issued.** No income tax prepayment is payable until a notice sets it. The client should set money aside. For a new business see the next case.

**First year of self-employment.** A founder must send the tax office the registration questionnaire (Fragebogen zur steuerlichen Erfassung) within one month of opening the business or starting freelance work (§ 138(1b) and (4) AO, https://www.gesetze-im-internet.de/ao_1977/__138.html). It is filed through Mein ELSTER: https://www.elster.de/eportal/formulare-leistungen/alleformulare/fseeun The questionnaire asks for expected turnover and profit. After processing it, the tax office tells the founder how much to prepay and when. The federal founders' portal says it usually takes two years until the first income tax assessment exists, and that until then the prepayments rest on the questionnaire figures. It warns that if the figures were too low, back payments of income tax for the last two to three years can put the business in serious financial difficulty. https://www.existenzgruendungsportal.de/gruenden-kurz-und-knapp/steuern

**Vorauszahlungsbescheid inflated by a one-off gain.** Apply for a Herabsetzung with evidence that the gain was non-recurring.

**Church member.** Church tax prepayments are set alongside the income tax prepayments and fall on the same dates. The rate depends on the federal state: see Section 5.7.

**Client pays Gewerbesteuer and has the § 35 EStG credit.** § 37(3) EStG lists the items left out of the prepayment base. It names the § 34a reduction. It does not name § 35, so the trade tax credit is not on that list. If the notice ignores the credit, apply for an adjustment. Flag for the Steuerberater.

**Client also has wages or investment income.** The base is the income tax of the last assessment after crediting withholding taxes. Check that the notice reflects all of the client's income types.

**Married couple, joint assessment.** Use the splitting limit for the solidarity surcharge test (Section 5.6).

## Section 9: Self-checks

Before delivering output, verify:

- [ ] Vorauszahlungsbescheid amounts confirmed from the notice, or the output says clearly that no notice was seen
- [ ] The two minimums in the Section 5.2 table checked
- [ ] All four dates identified, with the weekend and public holiday shift
- [ ] Solidarity surcharge limit applied to the right filing status
- [ ] Late payment surcharge worked out with the three-day grace, and the grace not given for payments handed over or sent (cash, cheque)
- [ ] Payment day taken as the day the tax office is credited, not the day the transfer was sent
- [ ] Any adjustment request flagged for the reviewer
- [ ] Church tax prepayment included if applicable
- [ ] Gewerbesteuer § 35 credit considered
- [ ] Year-end settlement formula presented
- [ ] Output labelled as estimated until the Vorauszahlungsbescheid is confirmed

## Section 10: Test suite

### Test 1: Standard quarterly prepayment

**Input:** a Vorauszahlungsbescheid for 2026 with an amount for each date.
**Expected:** the four amounts as printed. Dates: 10 Mar, 10 Jun, 10 Sep, 10 Dec. No recomputed split.

### Test 2: Below minimum threshold

**Input:** the prepayments worked out for the year are below the yearly minimum in Section 5.2.
**Expected:** no prepayments set. The answer names § 37(5) EStG and both minimums.

### Test 3: Late payment surcharge

**Input:** Q2 due 10 Jun 2026. Bank transfer credited 15 Jul 2026.
**Expected:** two started months. Surcharge = rounded-down unpaid amount x the Section 6.1 rate x two. No grace, because the delay is longer than three days.

### Test 4: Solidarity surcharge exempt

**Input:** single filer. The year's income tax prepayments do not exceed the single limit in Section 5.6.
**Expected:** no solidarity surcharge prepayment.

### Test 5: New freelancer

**Input:** registered as Freiberufler in 2026. No prior Steuerbescheid.
**Expected:** the answer does NOT say "no prepayments until the first assessment". It says the tax office sets prepayments from the expected profit in the registration questionnaire, that nothing is payable until a notice arrives, and it advises a set-aside.

### Test 6: Year-end settlement (refund)

**Input:** prepayments paid plus credited withholding taxes exceed the assessed income tax.
**Expected:** Erstattung of the difference, paid out after the assessment notice.

### Test 7: Year-end settlement (balance due)

**Input:** prepayments paid plus credited withholding taxes are less than the assessed income tax.
**Expected:** Nachzahlung of the difference, due within one month of the notice. Any part that equals unpaid due prepayments is due at once. Interest only if the 15-month period has passed.

### Test 8: US-style question

**Input:** "What is the safe harbour to avoid the underpayment penalty in Germany?"
**Expected:** § 37 EStG prints neither. The tax office sets the amounts. For a set amount the costs are the late payment surcharge (Section 6.1) and interest on the final balance (Section 6.3). Untrue facts in a reduction application are a different matter (Section 7.3).

## Prohibitions

- NEVER compute prepayments without checking whether a Vorauszahlungsbescheid has been issued
- NEVER ignore the two minimums in the Section 5.2 table
- NEVER forget the three-day grace period (Schonfrist) when working out late surcharges, and NEVER give it for payments handed over or sent (cash, cheque)
- NEVER apply the solidarity surcharge without checking the exemption limit
- NEVER present prepayment amounts as definitive. The Vorauszahlungsbescheid is authoritative
- NEVER advise reducing prepayments without warning about the Nachzahlungszinsen risk
- NEVER tell a client to pay less than the notice says before a new notice has arrived
- NEVER confuse ESt prepayments with Gewerbesteuer prepayments or with VAT advance payments
- NEVER ignore church tax prepayments for church members
- NEVER describe a German "safe harbour" or "underpayment penalty". Neither exists in § 37 EStG
- NEVER help a client put facts or figures they know to be untrue into a reduction application (§ 370 AO, Section 7.3)

## The method, step by step

1. Get the latest Vorauszahlungsbescheid and the latest Einkommensteuerbescheid. The notice sets the amounts (§ 37(3) sentence 1 EStG). Read the amount for each date from it. https://www.gesetze-im-internet.de/estg/__37.html
2. For a new business with no assessment yet, check that the Fragebogen zur steuerlichen Erfassung was filed through Mein ELSTER within one month of starting (§ 138 AO), and which expected profit it states. The tax office sets the first prepayments from it. https://www.elster.de/eportal/formulare-leistungen/alleformulare/fseeun
3. Diary the four due dates of § 37(1) EStG: 10 March, 10 June, 10 September, 10 December. Move a date that falls on a Saturday, Sunday or public holiday to the next working day (§ 108(3) AO). https://www.gesetze-im-internet.de/ao_1977/__108.html
4. Check the solidarity surcharge and church tax lines on the notice. Test the year's income tax prepayments against the limit for the client's filing status (§ 3(3) SolzG). https://www.gesetze-im-internet.de/solzg_1995/__3.html
5. Compare the income tax expected for the current year with the prepayments set. If they are clearly too high or too low, apply for a change with reasons and figures, using the Mein ELSTER form "Antrag auf Anpassung von Vorauszahlungen" (§ 164(2) sentence 2 AO, § 37(3) sentence 3 EStG). The tax itself is worked out with the tariff in `de-einkommensteuer-freelancer`. https://www.elster.de/eportal/formulare-leistungen/alleformulare/eingvorauszlg
6. Pay so that the tax office is credited by the due date. A transfer counts on the day it is credited. With a SEPA direct debit mandate a validly made payment counts as paid on the due date (§ 224(2) AO). https://www.gesetze-im-internet.de/ao_1977/__224.html
7. If a payment was late, work out the late payment surcharge under § 240 AO (Section 6). https://www.gesetze-im-internet.de/ao_1977/__240.html
8. After the year, check the assessment: prepayments paid are credited (§ 36(2) number 1 EStG), the balance is due within one month (§ 36(4) EStG), and interest under § 233a AO starts 15 months after the year ends. https://www.gesetze-im-internet.de/estg/__36.html

## Ask the client first

- Do you have a current Vorauszahlungsbescheid? What does it set for each date, and for which year?
- Is this your first or second year in business or as a freelancer? What profit did you state in the registration questionnaire?
- Do you expect this year's income to be clearly higher or lower than in the last assessed year, and what evidence is there?
- Do you also have wages or investment income with tax already withheld?
- Are you assessed jointly with a spouse? Are you a member of a church that collects church tax, and in which federal state do you live?
- How do you pay: SEPA direct debit mandate, bank transfer, or a cheque?

## When to refuse or refer

- Cross-border income and treaty credit timing (R-DE-ET-1).
- Prepayments for a partnership, or the split between partners (R-DE-ET-2).
- Trade tax prepayments (§ 19 GewStG): see `de-trade-tax`. VAT advance returns and payments (§ 18 UStG): see `germany-vat-return`.
- Corporations. Corporate tax prepayments follow the income tax rules by reference (§ 31(1) KStG, https://www.gesetze-im-internet.de/kstg_1977/__31.html), but this Guide is written for individuals.
- Working out the expected income tax itself. The tariff is in `de-einkommensteuer-freelancer`.
- A client who cannot pay a prepayment. Deferral (Stundung, § 222 AO, https://www.gesetze-im-internet.de/ao_1977/__222.html) is at the tax office's discretion, is as a rule granted only on application and against security, and carries its own interest. Refer to a Steuerberater.
- A dispute over a prepayment notice beyond a simple application for adjustment.
- Late filing of the annual return. § 37 EStG asks for no return for prepayments, so the late filing surcharge (§ 152 AO) is not part of this Guide.
- The exact church tax rate for a client: it is set by state church tax rules, which are not on the federal pages.
- Clients whose income is mainly from farming and forestry: longer periods apply (Sections 5.4 and 6.3). Refer.

## Sources

- EStG § 37 (income tax prepayments): https://www.gesetze-im-internet.de/estg/__37.html
- EStG § 36 (crediting of prepayments, year-end balance): https://www.gesetze-im-internet.de/estg/__36.html
- EStG § 52(35d) (longer adjustment periods for 2019 to 2024): https://www.gesetze-im-internet.de/estg/__52.html
- EStG § 51a (surcharge taxes, church tax prepayments): https://www.gesetze-im-internet.de/estg/__51a.html
- EStG § 10 (the special expenses named in § 37(3) sentence 4): https://www.gesetze-im-internet.de/estg/__10.html
- EStG § 12 (taxes on income and their ancillary charges are not deductible): https://www.gesetze-im-internet.de/estg/__12.html
- EStG § 41a (wage tax remittance date): https://www.gesetze-im-internet.de/estg/__41a.html
- AO § 108 (weekends and public holidays): https://www.gesetze-im-internet.de/ao_1977/__108.html
- AO § 124 (an administrative act, such as a notice, stays in effect until withdrawn, revoked, otherwise cancelled or settled): https://www.gesetze-im-internet.de/ao_1977/__124.html
- AO § 138 (registration questionnaire, one month): https://www.gesetze-im-internet.de/ao_1977/__138.html
- AO § 164 (prepayment notices are subject to review; application at any time): https://www.gesetze-im-internet.de/ao_1977/__164.html
- AO § 218 (the tax notice is the basis for collecting a tax claim): https://www.gesetze-im-internet.de/ao_1977/__218.html
- AO § 222 and § 234 (deferral and deferral interest): https://www.gesetze-im-internet.de/ao_1977/__222.html and https://www.gesetze-im-internet.de/ao_1977/__234.html
- AO § 224 (day of payment): https://www.gesetze-im-internet.de/ao_1977/__224.html
- AO § 233a and § 238 (interest after assessment): https://www.gesetze-im-internet.de/ao_1977/__233a.html and https://www.gesetze-im-internet.de/ao_1977/__238.html
- AO § 240 (late payment surcharge): https://www.gesetze-im-internet.de/ao_1977/__240.html
- AO § 370 (incorrect statements to the tax authorities): https://www.gesetze-im-internet.de/ao_1977/__370.html
- EGAO Art. 97 § 36 (longer interest-free periods for 2019 to 2024): https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html
- SolzG § 1, § 3, § 4 and § 6 (solidarity surcharge): https://www.gesetze-im-internet.de/solzg_1995/__1.html and https://www.gesetze-im-internet.de/solzg_1995/__3.html and https://www.gesetze-im-internet.de/solzg_1995/__4.html and https://www.gesetze-im-internet.de/solzg_1995/__6.html
- GewStG § 19 (trade tax prepayment dates): https://www.gesetze-im-internet.de/gewstg/__19.html
- UStG § 18 (VAT advance payment date): https://www.gesetze-im-internet.de/ustg_1980/__18.html
- KStG § 31 (corporate tax follows the income tax rules): https://www.gesetze-im-internet.de/kstg_1977/__31.html
- Mein ELSTER, form "Antrag auf Anpassung von Vorauszahlungen": https://www.elster.de/eportal/formulare-leistungen/alleformulare/eingvorauszlg
- Mein ELSTER, "Fragebogen zur steuerlichen Erfassung für Einzelunternehmen": https://www.elster.de/eportal/formulare-leistungen/alleformulare/fseeun
- Federal founders' portal, taxes in brief (questionnaire, first prepayments): https://www.existenzgruendungsportal.de/gruenden-kurz-und-knapp/steuern
- Finance ministry tax booklet "Steuern von A bis Z", 2025 edition (church tax range): https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
