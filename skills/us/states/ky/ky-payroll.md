---
name: ky-payroll
description: "Kentucky employer payroll for 2026: state withholding, K-4, MyTaxes K-1/K-3/K-5, KUIP unemployment insurance, rates, base, reporting, reciprocal-state conditions and unresolved local occupational-tax detail."
jurisdiction: US-KY
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
category: state-tax
version: "0.4"
---

# Kentucky withholding and unemployment insurance, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

**Answer first.** Kentucky has separate withholding and employer UI accounts. Use the dated withholding formula and the actual UI rate notice. Federal payroll belongs to `us-form-941-940-payroll`; annual individual return rules belong to `ky-income-tax`.

## Who this applies to

Employers paying Kentucky residents and nonresidents with Kentucky work. Residence, actual work locations, exemption certificates, worker status and the UI coverage test are required inputs, never assumed. This skill covers the ordinary state withholding and contributory UI workflow for 2026. Local occupational taxes remain a disclosed partial below.

For UI, ordinary for-profit liability arises from at least USD 1,500 gross wages in a quarter or a worker in any part of 20 weeks. Agriculture uses USD 20,000 in a quarter or 10 workers in parts of 20 weeks; household employment uses USD 1,000 in a quarter. Successors, prior liable employers, federal/out-of-state liability, government and nonprofit employers have separate tests. [2026 UI manual, pp.5-8](https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf). Do not treat a Form 1099 as proof of contractor status. OUI applies common-law facts; no IRS safe harbour binds it. Corporate officers are generally covered; sole-proprietor family exceptions do not extend to corporations.

## Rates, bands and thresholds

| Item | Amount and conditions, 2026 | Official source |
| --- | --- | --- |
| Ordinary state wage withholding | Annualize taxable wages, subtract USD 3,360 standard deduction, apply 3.5%, divide by annual pay periods; minimum zero | [DOR formula](https://revenue.ky.gov/Forms/2026%20Withholding%20Formula.pdf) |
| UI taxable wage base | First USD 12,000 per employee per calendar year; report gross wages as well as taxable wages | [OUI wage base](https://ui.ky.gov/Redesign/ResourcePages/TaxableWageBase.aspx) |
| Experience-rated UI | Schedule A, 0.30% to 9.00%; actual reserve-ratio rate from current notice | [OUI schedule](https://ui.ky.gov/Redesign/ResourcePages/TaxRateSchedules.aspx) |
| New nonconstruction UI | At least 2.7% until three years' experience; may be higher under reserve-ratio rules | [2026 manual p.26](https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf) |
| New construction UI | Highest applicable schedule rate; 9% in Schedule A; no lower experience rating until 12 consecutive quarters before computation date | [2026 manual p.26](https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf) |
| SCUF and surcharge | No SCUF in 2026; surcharge 0.00% | [OUI current-year updates](https://ui.ky.gov/); [wage-base page](https://ui.ky.gov/Redesign/ResourcePages/TaxableWageBase.aspx) |

## The base

For withholding, obtain a completed K-4 and apply the wage inclusions/exclusions in the March 2026 booklet, sections I, III and XII. Residents employed by an employer subject to Kentucky jurisdiction are generally covered for in-state and out-of-state services; nonresidents are covered to the extent of Kentucky services unless exempt. Agricultural and household withholding coverage differs from UI coverage. Voluntary pension withholding and nontaxable fringe benefits need their own treatment. Supplemental pay does not acquire an invented separate state rate; process the payment under the dated formula and booklet.

For ordinary periodic pay, multiply by pay periods, subtract the annual deduction and compute the period's tax. Additional withholding or exemptions require the employee certificate. Multiple jobs can use the same deduction in payroll, creating underwithholding on the annual return: review K-4 additional withholding. Do not apply a projected deduction or carry a prior-year rate with a buffer. [Formula](https://revenue.ky.gov/Forms/2026%20Withholding%20Formula.pdf), [booklet sections III and XI](https://revenue.ky.gov/Forms/42A003-March%202026.pdf).

UI uses covered gross remuneration and the remaining calendar-year wage base, not the withholding taxable-wage figure. Track taxable and excess wages per employee. Successor wage-base and reserve transfers require OUI's determination. Wages after the cap still appear in the report. [Manual pp.6, 13-17, successor chapter](https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf).

## Deadlines and filing

1. **Register separately.** Withholding: MyTaxes at `mytaxes.ky.gov`, or Form 10A100; retain the account and assigned frequency. UI: go from [OUI](https://ui.ky.gov/) to Employer Login, create a user, then Employer Registration in KUIP at `employer.ui.ky.gov`. Enter FEIN, entity/ownership, NAICS, first work and wage dates, wages and predecessor data. Retain the KEIN and subjectivity decision. [Booklet I-II](https://revenue.ky.gov/Forms/42A003-March%202026.pdf); [UI manual pp.10-12](https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf).
2. **Set withholding frequency using annual withholding, not average monthly liability.** Under USD 400: annual K-3, due 31 January following year, when assigned. USD 400-1,999: quarterly K-1 for the first three quarters by the last day of the next month, K-3 for the fourth quarter and annual reconciliation by 31 January. USD 2,000-49,999: K-1 first eleven months by the 15th next month, December K-3 by 31 January. USD 50,000 or more: twice monthly, first half by the 25th and second half by the 10th following month; December final period uses K-3. Accumulating USD 100,000 requires payment within one banking day. All frequencies electronically file and pay, absent a granted waiver. Zero returns remain due. [Booklet IV and VIII](https://revenue.ky.gov/Forms/42A003-March%202026.pdf).
3. **Reconcile withholding.** In MyTaxes select the withholding account, correct period and K-1/K-3 form. Reconcile period liability and payments, including every payroll provider, to annual W-2 state totals. Submit and retain acknowledgement and payment evidence. K-3 is also the final period return, not just a standalone reconciliation. Amend using K-1 Amended or K-3 Amended, not an invented K-1X. For wage statements, use the EFW2/Publication 1220 transmitter route or K-5 as appropriate; do not duplicate both. K-5 is under Transactions > File A Form > reconciliation; Calculate then Submit. Statements are due 31 January; the booklet's paper K-5 concession is fewer than 26 statements. Corrected W-2s are paper W-2C. [Booklet V-VIII, XIII](https://revenue.ky.gov/Forms/42A003-March%202026.pdf). Check the final 2026 wage-file specification before upload.
4. **File and pay UI quarterly.** KUIP wage reporting requires employee identity, covered gross wages, taxable and excess wages and employment counts. Verify totals and the assigned rate, submit, then make the payment and retain confirmation. Report even if no wages or no tax. Reports/payments are due the final day of the month after each quarter; closed-office days move the deadline to the next open day. For 2026 this is 30 April, 31 July, 2 November and 1 February 2027. [UI manual pp.14-18](https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf).
5. **Assess a voluntary UI contribution only when eligible.** Calculated experience rating, deficit reserve and no payment in the preceding calendar year are normal prerequisites. Deadline is within 120 days of mailing the annual rate notice or 30 days of a relevant determination, whichever is earlier; special successor deficit payments have a 60-day rule. KUIP Account Maintenance > Make a Voluntary Contribution Payment compares required payment and savings. A construction employer cannot buy out the initial experience-duration restriction. [Manual pp.26-28](https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf).

## Penalties and interest

Withholding late filing and late payment each generally incur 2% per 30 days or part, capped at 20%, minimum USD 10; apply the booklet's conditions and reasonable-cause provisions rather than adding both automatically. DOR's unpaid-tax interest is 9% during 2026, distinct from its 7% base rate. [Booklet X](https://revenue.ky.gov/Forms/42A003-March%202026.pdf); [interest notice](https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-26.aspx).

UI late reports: first late report USD 25 within 30 days or USD 75 later; later late reports in that year USD 125 or USD 175 respectively; annual maximum USD 600. Unpaid UI balances incur 1.5% per month or part. File timely even if unable to pay. [UI manual p.18](https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf). These replace the old unsourced USD 15 per worker/10% formula.

## Cross-border points

K-4 can claim reciprocal-state exemption for Illinois, Indiana, Michigan, West Virginia and Wisconsin; Virginia requires daily commuting; Ohio excludes a direct or indirect 20%-or-more shareholder-employee of an S corporation. The March 2026 booklet lists these qualifications. It also describes Fort Campbell nonresident and military-spouse exemptions. Keep the signed K-4 before stopping withholding. The old file's six-state list omitted Wisconsin and incorrectly routed routine reciprocity through a separate 42A809. [Booklet III](https://revenue.ky.gov/Forms/42A003-March%202026.pdf).

An exemption from Kentucky income-tax withholding does not establish exemption from UI or from a locality's occupational tax. Obtain the work-location records and local determination rather than inventing local rates or treating all taxes as reciprocal. Home-state withholding obligations belong to that state's payroll skill; do not copy Indiana county or Ohio city rates into this file.

## Two worked examples that recompute

**Case 1, periodic withholding and UI cap.** Sarah earns USD 1,500 weekly for 52 periods, no exemption/additional amount. Annual formula: (78,000 - 3,360) x 3.5% / 52 = USD 50.24 rounded per pay. Her UI taxable wages previously paid are USD 11,000; current gross USD 1,500 has only USD 1,000 within the cap. At an assumed notice rate of 2.7%, current employer UI is USD 27. No local amount is included. Beth's USD 2,000 weekly pay would produce USD 67.74; Carla's USD 200,000 annual pay produces USD 6,882.40 annual withholding before period rounding. Mike and Tony can have zero Kentucky state withholding if their Indiana residence and signed K-4 establish reciprocity; their local/Indiana computations remain pending below.

```oa-check
name: Kentucky 2026 weekly wage and UI remaining base
inputs:
  pay: 1500
  periods: 52
  prior_ui: 11000
steps:
  - withholding: round(max(pay * periods - 3360, 0) * 0.035 / periods, 2)
  - ui_wages: min(pay, max(12000 - prior_ui, 0))
  - ui_tax: ui_wages * 0.027
  - beth: round((2000 * 52 - 3360) * 0.035 / 52, 2)
  - carla: (200000 - 3360) * 0.035
expected:
  withholding: 50.24
  ui_wages: 1000
  ui_tax: 27
  beth: 67.74
  carla: 6882.4
```

**Case 2, pay a voluntary contribution or retain the current rate?** An eligible experienced employer has a deficit, no prior-year contribution, and a hypothetical KUIP offer: pay USD 500 to reduce the next year's assigned rate from 2.4% to 2.1%. Estimated taxable payroll is USD 200,000. Without contribution: USD 4,800. With contribution: USD 4,200 plus USD 500 = USD 4,700. Net saving USD 100. Pay only if the actual notice, eligibility and timely KUIP offer support those facts; at USD 100,000 payroll the same offer costs USD 200 more. Rates in this example are possible Schedule A rows, not a promised offer. [Manual pp.27-28](https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf).

```oa-check
name: Kentucky voluntary payment decision both payroll levels
inputs:
  payroll: 200000
  contribution: 500
steps:
  - without: payroll * 0.024
  - with_payment: payroll * 0.021 + contribution
  - net_saving: without - with_payment
  - low_without: 100000 * 0.024
  - low_with: 100000 * 0.021 + contribution
  - low_saving: low_without - low_with
expected:
  without: 4800
  with_payment: 4700
  net_saving: 100
  low_without: 2400
  low_with: 2600
  low_saving: -200
```

## Ask the client first

1. Pay dates/frequency, employee wages and pre-tax items, year-to-date withholding and UI wages?
2. Residence and actual work days in every state/city, signed K-4 and grounds for any exemption?
3. Entity, industry, workers' duties/control, household/agricultural/nonprofit status, first work/pay dates and successor history?
4. Withholding account/frequency, KEIN, actual UI notice and any deficit/voluntary contribution offer?
5. Previous providers, filed returns, payments, wage statements, amendments and notices?
6. Every local occupational-tax registration, locality boundary, rate/cap notice and remote-work record?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR 2026 formula. Read for annualization and deduction, including the printed biweekly arithmetic inconsistency. | https://revenue.ky.gov/Forms/2026%20Withholding%20Formula.pdf | 2026-11-13 |
| DOR March 2026 employer booklet. Read for sections I-XIII: wages, certificates, frequencies, reconciliation, returns, statements and penalties. | https://revenue.ky.gov/Forms/42A003-March%202026.pdf | 2026-11-13 |
| OUI 2026 employer manual. Read for pp.5-8 coverage, pp.10-18 registration/reporting/penalties, pp.26-28 rates and voluntary contributions. | https://ui.ky.gov/Documents/KY-OUI_Employer%20Guide_2026.pdf | 2026-11-13 |
| OUI rate schedules. Read for 2026 Schedule A and all reserve-ratio rows. | https://ui.ky.gov/Redesign/ResourcePages/TaxRateSchedules.aspx | 2026-11-13 |
| OUI wage bases. Read for 2026 base and surcharge. | https://ui.ky.gov/Redesign/ResourcePages/TaxableWageBase.aspx | 2026-11-13 |
| OUI current updates. Read for 2026 SCUF suspension and KUIP employer login. | https://ui.ky.gov/ | 2026-11-13 |

Not yet confirmed: legacy local figures are unconfirmed and must not be used: Louisville 1.45% plus 0.75%, Lexington 2.25%/USD 148,000 plus FCPS 0.50%, Covington 2.45%/USD 160,200, Newport 2.45%, Florence 2%/USD 160,200, Bowling Green 1.85%, Owensboro 1.78%, Boone 0.80%/USD 80,100 plus schools 0.50%, Kenton 0.7097%, Campbell 1.05%, Daviess 0.35%; old Indiana 3%/Clark 2%/Floyd 1.5% and Cincinnati 1.8%; the old 14-day final-pay alternative and liquidated-damages claim; local occupational-tax rates, residency distinctions, wage caps, overlap credits and current forms/deadlines for Louisville/Jefferson County/JCPS, Lexington-Fayette/FCPS, Covington, Newport, Florence, Bowling Green, Owensboro, Boone, Kenton, Campbell and Daviess; local home-working/2021 relief and Northern Kentucky stacking rules; the former OL-3/OL-3E and 220-221 form routing; the former Sarah/Mike/Tony/Beth/Carla local and Indiana/Ohio numerical outputs; local resident credits, alleged school-tax caps and claimed absence of Shelby County tax; the old KRS 341.123 construction presumption/two-prior-Schedule-C test and DOR treatment of SS-8 (OUI's actual common-law test is stated above); wage-law final-pay/vacation/damages under KRS 337.055/337.385; former exemption expiry date; final 2026 W-2 upload specifications. These legacy topics remain unresolved, not exemptions or instructions to use the old figures.
