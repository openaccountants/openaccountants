---
name: ms-payroll
description: "Mississippi 2026 employer wage withholding and unemployment:Form 89-350, annualized4% computation, filing/reconciliation,14000 UI wage base and assigned rates with training contribution boundary."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ms-payroll"
  jurisdiction: "US-MS"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Mississippi payroll withholding and unemployment insurance, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Use Mississippi's2026 annualized payroll formula and employee Form 89-350 for state withholding. UI uses a separate$14,000 annual wage base and MDES assigned rate, including any applicable training contribution. [2026 payroll flowchart](https://www.dor.ms.gov/sites/default/files/business/Computer%20Payroll%20Flowchart%20-%20updated%208-13-25.pdf); [MDES employer FAQ](https://www.mdes.ms.gov/employer-faqs/).

## Scope

Ordinary wage-withholding employers and covered contributing UI employers. State withholding and UI have different liability/localization rules; obtain both account determinations. Federal payroll figures belong to `us-form-941-940-payroll`. Public/nonprofit reimbursement, agriculture/domestic exceptions, acquisitions and multistate work require review.

## Ask the client first

1. Entity, first wage dates, work/residence locations, worker classification and acquired/predecessor business?
2. DOR withholding account/assigned frequency, MDES liability and2026 rate notice including training contribution?
3. Employee Form 89-350 status/exemption, spouse employment/allocation, additional withholding and payroll frequency?
4. State taxable pay, supplemental payments, prior-year/current-year wages and per-worker year-to-date UI wages?
5. Quarterly payroll/payments, W-2/annual reconciliation, amendments and final wage/closure dates?

## The method, step by step

1. **Register each system.** Obtain DOR withholding account through TAP. MDES ordinary coverage includes$1,500 wages in a quarter or one worker in 20different weeks, with acquisition/voluntary and special domestic/agricultural routes. Retain the determination rather than treating every contractor as outside UI. [2026 withholding instructions §§2-5](https://www.dor.ms.gov/sites/default/files/tax-forms/business/89700251revised1.13.2026.pdf); [MDES liability requirements](https://mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/liability-requirements/).
2. **Identify wages and certificate.** Resident/nonresident wages for Mississippi work generally require withholding; resident work elsewhere has the other-state-withholding exception described in the booklet. Obtain Form 89-350; federal certificate information is insufficient. If missing, use zero exemption under the instructions, not a guessed personal exemption. [2026 instructions §§4-8,12](https://www.dor.ms.gov/sites/default/files/tax-forms/business/89700251revised1.13.2026.pdf).
3. **Compute ordinary payroll.** Annualize pay by periodsN. TI=annualized pay - Form 89-350 exemption - annual payroll standard deduction. Use$2,300 for single and married-both-employed, $3,400 Head of Family and$4,600 married-one-employed. Annual tax=max(0,TI-10000)x0.04; divide by N and round to whole dollars as the flowchart directs, then account for agreed additional withholding. N is52weekly,26biweekly,24semimonthly,12monthly,1annual; daily/miscellaneous260requires the stated days worked handling. Supplemental wages have separate aggregation instructions. [2026 flowchart, entire page](https://www.dor.ms.gov/sites/default/files/business/Computer%20Payroll%20Flowchart%20-%20updated%208-13-25.pdf); [2026 §§9,13](https://www.dor.ms.gov/sites/default/files/tax-forms/business/89700251revised1.13.2026.pdf).
4. **Compute UI separately.** For a covered worker, quarter taxable wages=min(current covered wages,max(0,14000-earlier-year UI taxable wages)). Apply the full assigned rate and retain all reportable wages even after the cap. Published startup base rates are1% first liability year,1.1% second and1.2% third/subsequent until modified rate eligibility; these **exclude any applicable Workforce Investment and Training contribution**. Do not quote them as the complete2026 total without the notice. MDES pages differ on the experience-rate minimum; use the actual assigned notice and Sources gap. [MDES rate/wage-base FAQ](https://www.mdes.ms.gov/employer-faqs/); [MDES rate page](https://mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/unemployment-tax-rates).
5. **Reconcile and report.** Match state wages and withholding to each DOR return/payment and annual89-140/W-2. Match UI covered/taxable wages and rate to MDES quarterly report/payment. MDES permits corrected quarters using UI-3B; DOR corrections use the affected amended return. File final returns/closure requests where obligations end and preserve acknowledgments. [2026 instructions §§14-18 and calendar](https://www.dor.ms.gov/sites/default/files/tax-forms/business/89700251revised1.13.2026.pdf); [MDES reporting/corrections FAQ](https://www.mdes.ms.gov/employer-faqs/).

### Rates, bands and thresholds

| 2026 item | Amount or rule | Authority |
| --- | --- | --- |
| Ordinary annualized withholding | 0% first $10,000 of taxable amount;4% excess | [2026 computer payroll flowchart](https://www.dor.ms.gov/sites/default/files/business/Computer%20Payroll%20Flowchart%20-%20updated%208-13-25.pdf) |
| Payroll deduction | $2,300 single/both-employed;$3,400 Head of Family;$4,600 one-employed married | [2026 flowchart status branches](https://www.dor.ms.gov/sites/default/files/business/Computer%20Payroll%20Flowchart%20-%20updated%208-13-25.pdf) |
| UI annual taxable wage base | $14,000 per covered employee | [MDES wage-base FAQ](https://www.mdes.ms.gov/employer-faqs/) |
| Startup base rates | 1%,1.1%,1.2% by liability year; training contribution may add | [MDES startup paragraphs](https://mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/unemployment-tax-rates) |
| Ordinary UI liability | $1,500 quarterly wages or worker in 20 different weeks | [MDES regular employment rule](https://mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/liability-requirements/) |

## Worked cases

### Weekly single payroll

A worker has valid$6,000 exemption on 89-350, single status and $1,000 weekly taxable pay. Annual pay=$52,000; subtract$6,000 and$2,300, leaving$43,700. Annual tax = $1,348; divided by 52=$25.9231, rounded to$26 withholding. This is the formula method, not a claim about an arbitrary wage-table midpoint.

```oa-check
name: MS weekly formula method 2026
inputs:
  weekly_pay: 1000
  exemption: 6000
steps:
  - annual_taxable: weekly_pay * 52 - exemption - 2300
  - annual_tax: max(0, annual_taxable - 10000) * 0.04
  - pay_withholding: round(annual_tax / 52)
expected:
  annual_taxable: 43700
  annual_tax: 1348
  pay_withholding: 26
```

### UI cap with an explicitly assumed full rate

A covered worker has $13,000 earlier-year UI taxable wages and earns$4,000 this quarter. Remaining taxable wages are$1,000. Assume its actual full assigned notice rate is1.20%, solely for this example; UI is$12. Do not substitute the startup base rate without checking training contribution or successor/experience assignment.

```oa-check
name: MS UI annual wage cap
inputs:
  prior_taxable: 13000
  quarter_wages: 4000
  assumed_full_rate: 0.012
steps:
  - taxable: min(quarter_wages, max(0, 14000 - prior_taxable))
  - contribution: taxable * assumed_full_rate
expected:
  taxable: 1000
  contribution: 12
```

## When to refuse or refer

Refer employee status, multistate localization, acquisitions, special coverage and reimbursement, missing UI notice/training contribution and unusual wages. DOR assigns withholding filing frequency; do not make up a dollar threshold or apply a withholding rate to UI.

## Filing and payment

DOR assigns monthly or quarterly reporting and requires a return for every assigned period, including no-tax periods. Its2026 calendar gives returns/remittance by the15th after the month or quarter, moved for weekends/state holidays. Annual W-2/89-140 filing and employee statements are due January31 under the booklet; the10-or-more electronic mandate and1099calendar must be checked for the actual filing population. Amend errors through TAP or the authorized paper form and mark the final return on closure. [2026 §§14-18 and p.38 calendar](https://www.dor.ms.gov/sites/default/files/tax-forms/business/89700251revised1.13.2026.pdf).

MDES quarterly wages and taxes are due April30, July31, October31 and January31 following each quarter, next business day if weekend/holiday. An active account still files a zero report. Register for its online system, file/pay and retain proof; a report acknowledgment alone is not payment. [MDES quarterly calendar](https://mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/quarterly-report-and-tax-due-dates/); [MDES employer FAQ](https://www.mdes.ms.gov/employer-faqs/).

## Completion checklist

Confirm two accounts and liability, save89-350 and assigned rate, reproduce the 2026 formula and annual UI cap, reconcile separate filing/payment calendars, file annual statements and resolve prior-period corrections with evidence.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| 2026 computer payroll accounting flowchart; read for for entire status/exemption/period/rounding branches and4% formula. | https://www.dor.ms.gov/sites/default/files/business/Computer%20Payroll%20Flowchart%20-%20updated%208-13-25.pdf | 2026-11-13 |
| 89-700 revised January13,2026; read for for instructions §§1-18, certificate and p.38 employer calendar; wage-table ranges not copied as independent figures. | https://www.dor.ms.gov/sites/default/files/tax-forms/business/89700251revised1.13.2026.pdf | 2026-11-13 |
| MDES liability requirements; read for for regular, domestic/agricultural, acquisition and voluntary routes. | https://mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/liability-requirements/ | 2026-11-13 |
| MDES employer FAQ; read for for registration, liability, rates/base, quarterly reporting/zero returns, corrections and closure. | https://www.mdes.ms.gov/employer-faqs/ | 2026-11-13 |
| MDES unemployment rates; read for for startup base rates, training-contribution caveat, modified-rate definition and range. | https://mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/unemployment-tax-rates | 2026-11-13 |
| MDES quarterly report/tax dates; read for for all four dates, weekend rule and online registration. | https://mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/quarterly-report-and-tax-due-dates/ | 2026-11-13 |
| MDES law/regulation compilation dated2024; read for for71-5-353 startup-rate and71-5-361 surrounding experience provisions; dated legal background, not a2026 total-rate notice. | https://www.mdes.ms.gov/media/456617/mdes_lawsandregulation_web_02152024.pdf | 2026-11-13 |

Not yet confirmed: the applicable 2026 Workforce Investment and Training contribution and complete assigned UI rate. MDES employerFAQ gives a0.2% experience minimum while its rates page gives0%; neither is silently selected as the 2026 minimum. Specialized UI coverage/localization and current annual electronic file specifications need confirmation for affected facts. Startup base rates are not a substitute for the rate notice.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ms-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ms-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
