---
name: deadline-engine
description: "Builds a sourced filing/payment calendar from confirmed obligations, actual reporting periods and the applicable country rules. Separates tax year from filing year, statutory dates from bank processing cut-offs, filing from payment and confirmed dates from unresolved tasks. Includes bounded UK, Canadian, Singapore and Spanish applications; retains the original country/task register without treating unverified legacy dates or penalties as current guidance."
version: 0.5
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
type: cross-country-method
depends_on:
  - workflow-base
category: intelligence
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tooling
---

# Deadline Engine

## What this file is

**Obligation category:** INTEL (Intelligence / Cross-cutting)
**Functional role:** Calendar generation, deadline tracking, penalty estimation
**Status:** Active

This is an intelligence skill that loads on top of `workflow-base`. Unlike content skills that compute a single obligation, this skill reads the user's full obligation profile and produces a consolidated filing calendar.

**The reviewer is the customer of this output.** The calendar and penalty estimates are working aids for a credentialed reviewer, not direct advice to the taxpayer.

> **Disclaimer.** This skill provides deadline information based on general statutory rules for the jurisdictions listed. Actual deadlines may vary due to weekends, public holidays, individual extensions, agent lodgement schedules, or legislative changes. All dates must be verified by a credentialed professional in the relevant jurisdiction before reliance. OpenAccountants does not guarantee the accuracy of any deadline and accepts no liability for late filings. This is not legal or tax advice.

## Section 1 -- Scope statement

This skill covers:

- **Country/task discovery register:** United States federal/California, Malta, United Kingdom, Germany, Australia, Canada, India, Spain, Netherlands and Singapore. The list is an investigation register, not proof of verified comprehensive calendar coverage. Use ISO country/subdivision codes, for example CA for Canada and US-CA for California.
- **Obligation types:** Income tax, estimated/provisional tax, VAT/GST/BTW, social security contributions
- **Output:** Sorted 12-month calendar, urgency flags, penalty estimates

This skill does NOT cover:

- Corporate, payroll and employer computations; a discovered ECI/company obligation is handed to the company calendar, not silently included in a personal calendar
- Extension requests or amended return deadlines (beyond noting extension availability)
- Sub-national deadlines beyond US-CA (other US states, German Laender, Australian states, etc.)
- Certified local deadlines not actually read from the current authority/notice; retain an unresolved task instead of inventing a date

## Ask the client first

Confirm country/subdivision and tax/entity registrations; tax year and reporting period end; exact obligation/form and filing method; active agent/extension/disaster/deferral status; return and payment history; notices, payment method and relevant time zone. Read existing intake and records before asking again. An absent balance does not prove no filing obligation.

## The method, step by step

### Step 0 -- Read the user's obligation profile

0. **Read obligation profile** : Read the user's jurisdiction and obligation types from one of these sources, in priority order: 1. **Intake manifest** -- the structured output from an intake skill (e.g., `us-ca-freelance-intake`) 2. **Explicit user statement** -- "I'm a freelancer in Malta" or "I file in the UK and Germany" 3. **Prior conversation context** -- jurisdiction identified in an earlier turn If no jurisdiction can be determined, ask: > "Which country (or countries) do you file taxes in? And what types of obligations do you have -- income tax, VAT/GST, estimated tax payments, social security?" Do not proceed until at least one jurisdiction is confirmed.

### Step 1 -- Look up filing deadlines

0. **Look up deadlines:** match each confirmed country, taxpayer type, obligation and period to the actual current official country method/notice. Use Section 3 as a discovery register, not a substitute for the missing source. Record rule URL, read date, tax year, period, filing method, liable person, base deadline, exception/extension conditions and verification status per item. Keep filing, payment, instalment, registration and bank cut-off as distinct tasks. Flag missing coverage; do not claim the register covers every obligation.

### Step 2 -- Generate the calendar

0. **Generate calendar:** anchor to the actual local date/time, label the tax period separately from filing year, and generate each confirmed event in the next 12 months plus any unresolved/overdue tasks. Add calendar months as calendar months, not a fixed number of days. Apply only the actual obligation's weekend/holiday rule and recognised holiday calendar. UK VAT must reach HMRC by the stated deadline even on a weekend; CRA GST/HST and individual instalments allow the next business day. Do not move every Saturday backwards or every Sunday forwards. Keep the legal deadline unchanged when only a bank processing cut-off requires earlier action. Sort confirmed dates and show unresolved items separately with their missing evidence. [HMRC VAT](https://www.gov.uk/submit-vat-return), [HMRC payment processing](https://www.gov.uk/pay-self-assessment-tax-bill/overview), [CRA GST/HST](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html), [CRA instalments](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html).

### Step 3 -- Flag approaching deadlines

0. **Flag deadlines:** compute whole local calendar days remaining to the legally adjusted deadline. The urgency thresholds below are this workflow's planning policy, not statutory periods or permission to delay. Today is urgent, not overdue until the applicable deadline time has passed. An unknown deadline gets no fabricated countdown. For an overdue item run Step 4 eligibility checks; do not automatically invent a penalty.

**Urgency flag table**  _(Section 3 -- Master Deadline Table (urgency flag table))_

| Days remaining | Flag | Label |
| --- | --- | --- |
| > 30 days | -- | On track |
| 8--30 days | AMBER | Approaching |
| 0--7 days | RED | Urgent |
| Past due | RED | OVERDUE |

### Step 4 -- Calculate penalties for late filing

0. **Calculate penalties:** establish the applicable tax/form, period, failure type, original/effective deadline, actual filing/payment dates, unpaid-tax base at each stage, partial-month/day rule, overlapping charges, prior penalties/demand notices, caps, relief/appeal and interest rates for each dated segment. Load the current official penalty rule, recompute and show each step. A T2 label cannot make a stale summary usable. With missing rules/facts report the unresolved exposure and required evidence, without a numeric bill. Separate penalty, interest, collection charges and cash already paid; never automatically compound a penalty or apply a filing penalty merely because a payment was late.

## Section 3 -- Country/task register and bounded verified rules

The register retains all original obligation topics and form clues. It grants no filing extension, payment deferral or penalty rate. Form names are discovery clues, not confirmation of applicability. In particular, Malta TA24 is a rental-income route, not the ordinary sole-trader return, and Singapore ECI is a company task. The verified applications after the register govern only their stated facts; all other old shortcuts are explicitly held under Sources.

### 3.1 United States -- Federal

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| Federal income tax (filing + payment) | 1040 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Estimated tax -- Q1 | 1040-ES | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Estimated tax -- Q2 | 1040-ES | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Estimated tax -- Q3 | 1040-ES | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Estimated tax -- Q4 | 1040-ES | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.2 United States -- California

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| CA individual income tax | 540 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| CA SMLLC annual tax | 568 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| CA estimated tax | 540-ES | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.3 Malta

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| Ordinary sole-trader income tax return; keep TA24 as a separate rental-income investigation | Self-assessment return, not TA24 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| VAT return | Periodic return (CFR) | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Social security contributions (Class 2) | SSC | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Provisional tax -- 1st instalment | PT | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Provisional tax -- 2nd instalment | PT | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Provisional tax -- 3rd instalment | PT | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.4 United Kingdom

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| Self Assessment (online) | SA100 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Self Assessment (paper) | SA100 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Payment on Account -- 1st | POA | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Payment on Account -- 2nd | POA | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Balancing payment | SA100 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| VAT return | VAT100 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.5 Germany

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| Income tax return | ESt (Einkommensteuererklaerung) | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| VAT return (advance) | UStVA (Umsatzsteuer-Voranmeldung) | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| VAT annual return | UStE | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Estimated tax -- Q1 | Vorauszahlung | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Estimated tax -- Q2 | Vorauszahlung | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Estimated tax -- Q3 | Vorauszahlung | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Estimated tax -- Q4 | Vorauszahlung | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.6 Australia

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| Income tax return (self-lodged) | ITR | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Income tax return (tax agent) | ITR | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| BAS -- GST (quarterly) | BAS | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| PAYG instalments | BAS/IAS | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.7 Canada

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| Individual income tax (filing) | T1 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Individual income tax (payment) | T1 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| GST/HST return | GST34 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Instalments -- Q1 | -- | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Instalments -- Q2 | -- | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Instalments -- Q3 | -- | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Instalments -- Q4 | -- | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.8 India

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| Income tax return (no audit) | ITR-3 or ITR-4 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Income tax return (audit required) | ITR-3 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Advance tax -- Q1 | Challan 280 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Advance tax -- Q2 | Challan 280 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Advance tax -- Q3 | Challan 280 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Advance tax -- Q4 | Challan 280 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| GST return | GSTR-3B | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| GST annual return | GSTR-9 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.9 Spain

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| IRPF (income tax) | Modelo 100 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| IVA (VAT) -- Q1 | Modelo 303 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| IVA (VAT) -- Q2 | Modelo 303 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| IVA (VAT) -- Q3 | Modelo 303 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| IVA (VAT) -- Q4 | Modelo 303 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Pago fraccionado -- Q1 | Modelo 130 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Pago fraccionado -- Q2 | Modelo 130 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Pago fraccionado -- Q3 | Modelo 130 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Pago fraccionado -- Q4 | Modelo 130 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| RETA (social security) | Cuota | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.10 Netherlands

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| Income tax return | IB (Inkomstenbelasting) | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| BTW (VAT) return | Aangifte omzetbelasting | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Voorlopige aanslag (provisional assessment) | -- | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### 3.11 Singapore

| Task to retain | Original form/discovery clue, confirm applicability | Evidence required before scheduling |
|---|---|---|
| Income tax return | Form B | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| GST return | GST F5 | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |
| Estimated chargeable income | ECI | Establish the actual period, filing/payment distinction, current due date and exception from the country method/notice |

### Verified calendar applications, current rules read 14 November 2026

| Obligation and bounded period | Rule and conditions | Official source |
|---|---|---|
| UK ordinary Self Assessment, 2025-2026 tax year | Paper received 31 October 2026; online 31 January 2027. The late-registration notice can give a different filing date without moving the ordinary payment date. Specialist pension/non-resident-company and partnership exceptions need their actual rule | [HMRC deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines) |
| UK Self Assessment payments | Ordinary balancing payment and first payment on account 31 January; second payment on account 31 July. Test actual payment-on-account liability and reduction before scheduling an amount | [HMRC payment](https://www.gov.uk/pay-self-assessment-tax-bill/overview) |
| UK ordinary online VAT | Usually one calendar month and 7 days after the assigned accounting period; filing/payment still due by that deadline on weekends/holidays. Actual annual-accounting/other special scheme and payment clearance need their own rule | [HMRC VAT](https://www.gov.uk/submit-vat-return) |
| Canada personal return, 2025 tax year filed in 2026 | Ordinary filing and balance payment 30 April 2026; qualifying self-employed taxpayer/spouse filing 15 June 2026, without moving payment. Confirm tax-shelter, death and other exceptions before using the later filing date | [CRA dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) |
| Canada individual instalments, 2026 | For most liable individuals: 15 March, June, September and December, next business day for a recognised weekend/holiday. Farmers/fishers can have a December-only date; death can remove later instalments. Liability is a separate test, not a universal threshold from this table | [CRA instalments](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) |
| Canada GST/HST | Monthly/quarterly filing and payment one month after period. Most annual filers: three months after year end. Qualifying calendar-year sole proprietor with business income: payment 30 April, filing 15 June. Listed-financial-institution and election exceptions need their own rule; recognised weekends/holidays move to next business day | [CRA GST/HST](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) |
| Malta return identification and Article 10 sole-proprietor VAT online concession | Ordinary sole-trader return is a self-assessment return; TA24 is rental income. The VAT guidance gives qualifying online sole proprietors an additional 7 days from the 15th day. Confirm the actual assigned period and concession eligibility; do not treat every VAT return as a calendar quarter plus 45 days | [MTCA tax cycle](https://mtca.gov.mt/personal-tax/self-employed/tax-return-cycle), [VAT cycle](https://mtca.gov.mt/personal-tax/self-employed/vat-return-cycle) |
| Singapore GST | Return/payment one month after actual accounting period; accepted GIRO has a separate deduction date and weekend rule for that deduction. Confirm the acknowledgement instead of moving the filing deadline to the debit date | [IRAS GST](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/gst-filing-due-dates-and-requests-for-extension) |
| Spain Modelo 303, 2026 instructions | Quarterly general window: days 1 to 20 in April/July/October; fourth quarter days 1 to 30 January. Monthly window and January exception differ. Confirm the dated annual calendar, holidays and earlier direct-debit cut-off before assigning a concrete date | [AEAT instructions, filing-period section](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html) |

**Extensions are evidence, not assumptions.** Preserve extension/amendment discovery and the exclusions above. For an in-scope IRAS GST request, the page distinguishes accepted reasons, request timing and actual approval; a request does not itself move the deadline or necessarily defer payment. Reconcile original and extended dates to the approved notice. [IRAS extensions](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/gst-filing-due-dates-and-requests-for-extension).

## Section 4 -- Penalty method and verified bounded applications

Never generate a monetary charge from the unsourced historical summaries. Keep investigations for US failure-to-file/pay/estimated-tax interest, California filing/payment/collection costs, Malta filing/payment/VAT, Germany filing/payment surcharges, Australia FTL multipliers and GIC, Canada ordinary/repeated filing and instalments, India filing fee/advance interest, Spain voluntary versus enforced collection, Netherlands default penalties/interest and Singapore filing/payment charges. The full original topics and numeric shortcuts are inventoried as unresolved under Sources, so none disappear silently.

| Tax and eligibility | Current bounded rule | Official source |
|---|---|---|
| UK Self Assessment late return | Initial GBP 100; after three months GBP 10/day up to GBP 900; after six months further greater of 5% tax due or GBP 300; after twelve months another greater of 5% or GBP 300. Keep later/serious-case and appeal checks in the actual country method | [HMRC SA penalties](https://www.gov.uk/self-assessment-tax-returns/penalties) |
| UK Self Assessment unpaid tax | 5% of unpaid tax at 30 days, six months and twelve months, plus separately computed interest. Establish the unpaid amount at each trigger; do not add tax already cleared | [HMRC SA penalties](https://www.gov.uk/self-assessment-tax-returns/penalties) |
| Canada personal 2025 return, ordinary late filing with balance owing | 5% of balance owing plus 1% per full late month, maximum twelve monthly increments | [CRA personal penalties](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html) |
| Canada personal 2025 return, qualifying repeated late filing | 10% plus 2% per full late month, maximum twenty monthly increments, only when the prior-year penalty and demand-to-file conditions apply. Do not escalate merely because a return was late before | [CRA personal penalties](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html) |

Interest, instalment penalties, relief, different taxes/forms and future filing cycles require their dated official rules. No interest rate is hard-coded here. Preserve proof of notices and requests without submitting anything or advising a waiver is guaranteed.

## Section 5 -- Output format

Present the calendar in this structure:

### Part A -- Filing calendar (next 12 months)

**Filing calendar table (Part A)**  _(Part A -- Filing calendar (next 12 months))_

| # | Date | Days | Urgency | Jurisdiction | Obligation | Form | Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Confirmed legal date | Computed locally | Policy flag | Confirmed country | Filing task and period | Actual form | File, retain acceptance |
| 2 | Separate confirmed date | Computed locally | Policy flag | Confirmed country | Payment task and period | Actual payment reference | Allow actual bank clearance time |
| ... |  |  |  |  |  |  |  |

### Part B -- Overdue items (if any)

List confirmed overdue obligations, filing/payment status and dated evidence. Show a recomputed penalty only where facts and current rule permit; list unresolved penalty/interest separately, not as zero.

### Part C -- Reviewer notes

- Confirmed filing method and facts; do not silently assume online filing or agent/extension eligibility
- Items requiring reviewer confirmation
- Suggestions for extension filings

## Section 6 -- Self-checks

Before delivering output, verify:

- [ ] User's jurisdiction is confirmed, not assumed
- [ ] Every confirmed obligation is included; missing/unsupported coverage is named, not described as a complete country calendar
- [ ] Dates are correct for the current calendar year
- [ ] Actual obligation-specific weekend/holiday rule and bank processing cut-off applied separately
- [ ] Urgency flags match the days-remaining calculation
- [ ] Penalty/interest eligibility, dated inputs, caps and overlapping charges checked; no amount invented from a T2 flag
- [ ] No filing advice is given without reviewer qualification
- [ ] Calendar is sorted chronologically
- [ ] Output uses the format from Section 5

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## When to refuse or refer

Do not invent a deadline or penalty when jurisdiction, period, taxpayer class, return method or current rule is unknown. Keep the task visible as unresolved. Obtain the actual extension/deferral/disaster notice instead of assuming relief. Suspected evasion, an assessment dispute or a missed statutory remedy needs the appropriate specialist. Never represent a draft calendar as a filing, payment or accepted extension, and never submit a form/payment without the user's actual authorised procedure.

## Worked cases

**UK VAT calendar and urgency, 14 November 2026.** Assume the assigned ordinary accounting period ended 31 October 2026 and no special scheme. One calendar month ends 30 November; seven further days gives 7 December 2026. With 23 calendar days remaining, this method's planning label is AMBER. Keep filing, cleared payment and any earlier bank action separate. A statutory weekend date would not automatically move. The ordinal inputs below represent the stated dates and are arithmetic aids, not tax figures. [HMRC VAT](https://www.gov.uk/submit-vat-return).

```oa-check
name: UK VAT month-plus-days calendar, not a fixed forty-day offset
inputs:
  today_ordinal: 739934
  period_end_ordinal: 739920
  next_calendar_month_end_ordinal: 739950
  extra_days: 7
steps:
  - due_ordinal: next_calendar_month_end_ordinal + extra_days
  - days_remaining: due_ordinal - today_ordinal
  - preparation_buffer_after_seven_day_internal_target: max(days_remaining - 7, 0)
expected:
  due_ordinal: 739957
  days_remaining: 23
  preparation_buffer_after_seven_day_internal_target: 16
```

**Canada ordinary versus repeated late filing, 2025 return filed in the 2026 cycle.** Assume CAD 10,000 balance, three complete late months and no other charge/relief. Ordinary filing penalty is CAD 500 + CAD 300 = CAD 800. If the actual prior-penalty AND demand conditions are proved, the repeated formula gives CAD 1,000 + CAD 600 = CAD 1,600 instead, not in addition to CAD 800. Filing lateness and payment interest remain distinct. [CRA penalty conditions](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html).

```oa-check
name: Canada repeat-penalty conditions select a formula, not two cumulative penalties
inputs:
  balance_owing: 10000
  full_months_late: 3
  ordinary_initial: 0.05
  ordinary_monthly: 0.01
  repeated_initial: 0.10
  repeated_monthly: 0.02
steps:
  - ordinary: balance_owing * (ordinary_initial + min(full_months_late, 12) * ordinary_monthly)
  - repeated_if_conditions_met: balance_owing * (repeated_initial + min(full_months_late, 20) * repeated_monthly)
  - increase_from_proved_repeat_conditions: repeated_if_conditions_met - ordinary
expected:
  ordinary: 800
  repeated_if_conditions_met: 1600
  increase_from_proved_repeat_conditions: 800
```

## Sources

| Official source | What was read for | Read on |
|---|---|---|
| https://www.gov.uk/self-assessment-tax-returns/deadlines | Read for 2025-2026 filing cycle, paper/online dates, late-registration and specialist-return exceptions | 2026-11-14 |
| https://www.gov.uk/pay-self-assessment-tax-bill/overview | Read for payment dates, receipt versus instruction, payment-method lead times and weekend bank cut-off | 2026-11-14 |
| https://www.gov.uk/submit-vat-return | Read for assigned periods, ordinary calendar-month-plus-days deadline and fixed weekend/holiday deadline | 2026-11-14 |
| https://www.gov.uk/self-assessment-tax-returns/penalties | Read for ordinary filing stages, unpaid-tax stages, separate interest and appeal; not all linked specialist penalty legislation | 2026-11-14 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | Read for 2025 personal return's 2026 filing/payment distinction; 2026 tax-year final-return dates are not certified by this page | 2026-11-14 |
| https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html | Read for filing/payment periods, sole-proprietor and listed-financial-institution exceptions and next-business-day rule | 2026-11-14 |
| https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html | Read for 2026 ordinary instalments, farmer/fisher/death exceptions and weekend rule; eligibility threshold is not certified from this page | 2026-11-14 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html | Read for 2025 return ordinary/repeated penalty conditions, daily interest and changing prescribed rates | 2026-11-14 |
| https://mtca.gov.mt/personal-tax/self-employed/tax-return-cycle ; https://mtca.gov.mt/personal-tax/self-employed/vat-return-cycle | Read for actual ordinary-return identification, rental-income menu distinction and qualified online VAT concession, not all Maltese due dates/penalties | 2026-11-14 |
| https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/gst-filing-due-dates-and-requests-for-extension | Read for period-based deadlines, GIRO distinction, actual extension reasons/request/approval and nil returns, not income-tax/ECI deadlines | 2026-11-14 |
| https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html | Read for the 2026 instructions' submission channels, quarterly/monthly windows and January exception; not the full annual holiday/direct-debit calendar | 2026-11-14 |

Not yet confirmed: current US federal/California, German, Australian, Indian, Dutch and other unverified deadlines/penalties in the original register; Malta annual, provisional-tax, Class 2 dates and penalties; UK payment-on-account bases and specialist penalties; Canada instalment eligibility/interest rates and final 2026-return dates; Singapore personal/ECI and tax-specific penalty conditions; Spain non-VAT and current direct-debit/holiday calendar. ATO pages returned 403 in normal access, so Australian dates and penalties are not freshly certified here. The register remains, but the historical shortcuts below must not be used to schedule or charge a client until the actual official country rule is read. In particular, TA24 is not Malta's ordinary self-employed return, a universal Saturday move is wrong, the Australian December BAS exception cannot be omitted, and one filing date cannot cover every Canadian individual/GST filer. Unsupported numeric summaries have been removed from usable guidance, not silently treated as current.

### Retired shortcuts and what remains to verify

Every original obligation/form remains in the country/task register. The original unsourced date and penalty summaries are no longer executable defaults. Their exact old text and the old-to-new map are retained in the batch audit evidence, so the independent reader can assess every correction and unresolved item.

- US federal: ordinary income filing/payment and Form 4868, each estimated instalment and filing/payment/underpayment penalties. Confirm actual tax-year dates, relief notices, minimum penalty for that filing year and interaction; do not infer compound-daily estimated-tax penalties.
- California: personal filing/extension and estimated instalment dates/weights, LLC annual tax versus return/form and due date, filing versus payment/collection charges. A Form 568 return is not itself the annual-tax payment instruction.
- Malta: ordinary return versus rental TA24, actual VAT period/online concession, Class 2 and provisional instalments/benchmark, tax/VAT filing and payment penalties. The original generic quarterly Class 2 and calendar-quarter-only VAT schedules are not certified.
- Germany: actual advised/unadvised filing year, any transition extension, current advance-VAT frequency thresholds, annual VAT and assessed instalments; filing/payment surcharge bases, grace and exclusions. Historic turnover thresholds are not current merely because the return title is unchanged.
- Australia: self-lodged versus taxpayer-specific agent return dates, quarterly BAS/PAYG and the December-quarter exception, concessions, current FTL penalty unit/multiplier and dated GIC. Normal source access was blocked, so a country skill link cannot certify those figures as freshly read.
- Canada: ordinary versus self-employed filing, separate balance date, all GST filer categories, instalment eligibility and exceptions, repeated-penalty demand/prior-year conditions and separate interest. The bounded 2025-return rules above are not confirmation of final 2026-return dates.
- India: actual audit/non-audit return and form, advance-tax cumulative instalments, GST monthly/quarterly and annual-return eligibility, current filing-fee/income thresholds and advance-interest provisions. The old two-tier post-December fee and automatic GSTR-9 turnover shortcut are unconfirmed, not defaults.
- Spain: IRPF campaign/debit dates, each Modelo 303/130 period, RETA collection, voluntary regularisation versus enforced-collection surcharges and interest. The official VAT window above does not verify unrelated tax/payment penalties.
- Netherlands: taxpayer's income-tax invitation/extension, BTW filing/cleared payment and assessed provisional instalments; current default penalties and tax-specific interest period. The old 2025 interest figure is not adopted as current.
- Singapore: personal filing channel/year, actual GST period/GIRO and extension, separate company ECI task; income-tax versus GST filing/payment penalties and outstanding-tax triggers. The old immediate-filing-penalty shorthand is not a universal rule.
