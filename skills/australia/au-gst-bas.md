---
name: au-gst-bas
description: Australian Business Activity Statement (BAS) — non-GST sections. Covers PAYG withholding (labels W1-W5), PAYG income tax instalments (labels T1-T9), FBT instalments (label F1), and PAYG withholding reconciliation. Complements australia-gst.md which covers GST labels (1A-9).
version: 1.4
jurisdiction: AU
tax_year: 2025
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Ryan Duguid"
reviewed_on: 2026-11-03
tier: 1
domain: vat-gst
---

# Australia BAS: non-GST sections

## Scope

This Guide prepares working papers for individual taxpayers and sole proprietors for the **2025–26 income year (1 July 2025 to 30 June 2026)**. Use the issued statement and notices for the actual reporting period. PAYG withholding, income-tax instalments and FBT instalments can have different cycles.

GST registration, taxable/GST-free/input-taxed supplies, input credits, cash/non-cash attribution and Simpler/full GST reporting belong to [australia-gst.md](australia-gst.md), preserving the original GST-topic destination. The method below covers the complementary non-GST labels. Partnerships, companies, trusts, superannuation funds, WET and LCT are outside this Guide's preparation scope. Fuel tax credit calculations are outside scope: identify any 7C/7D entries before finalising the whole BAS. Check this point with one of our partner accountants.

## Filing requirements and dates

Lodge every required BAS, including a nil BAS when nothing is reportable; pausing trading while retaining GST registration does not remove that requirement. Distinguish quarterly instalment notices: R is PAYG, S is GST and T combines both; those notices require lodgment only when varying the instalment amount. Pay the notified amount when not varying. [ATO instalment notices][NOTICES]; [ATO nil BAS][PAUSED].

For GST, ordinary periods are quarters ending 31 March, 30 June, 30 September and 31 December, unless an election, Commissioner determination or special period applies. Monthly GST applies at turnover of $20 million or more, on direction, or by a valid election; eligible voluntarily registered entities may elect annual reporting. GST turnover alone does not set PAYG-withholding frequency. Use the actual ATO withholding classification: small withholders normally report/pay quarterly and medium withholders monthly; large withholders pay electronically on their separate schedule. Classification includes prior-year withholding, group rules and Commissioner determinations, rather than GST registration status. [GST Act ss 27-5 to 27-15][GST]; [ATO GST cycles][DUE]; [TAA Schedule 1 ss 16-70 to 16-115][TAA1]; [ATO small/medium reporting][CYCLE].

Standard quarterly BAS dates are **28 October** (July–September), **28 February** (October–December), **28 April** (January–March) and **28 July** (April–June). If a date falls on a weekend/public holiday, use the next business day. In this year Q2's nominal 28 February 2026 is a Saturday; check the adjusted actual deadline and any valid relief. Eligible online self-lodgers may get an extra two weeks except Q2; electronic lodgment alone does not give a 25 August deadline. [ATO due dates][DUE].

For Q4 2025–26, **25 August 2026** is the agent-program date for eligible electronic statements, normally generated after the preceding statement was lodged electronically. The program excludes monthly PAYG instalments, consolidated-head PAYG statements, monthly GST cycles (apart from the December concession), R/S/T instalment notices and monthly-withholding-only statements; SAP quarters must align with standard quarters. Paper/first statements may have an earlier date. [ATO agent program][PROGRAM].

## PAYG withholding: W1 to W5

Identify employees/directors, labour-hire workers, voluntary agreements and no-ABN supplies under the applicable withholding provision. Use the tax table and declarations applicable to the **payment date and payment type**. Labour-hire arrangements can require withholding even for an independent contractor with an ABN; apply the more specific withholding provision before no-ABN withholding. [TAA Schedule 1 ss 12-5, 12-35 to 12-60][TAA1]; [ATO labour hire][LABOUR].

For a valid written voluntary agreement with an individual, other compulsory withholding categories take priority. Use the notified CIR if at least 20%; if below 20%, withhold 20% unless the agreement specifies the lower CIR. Without a CIR, use 20%. Exclude GST charged from the withholding base; the supplier's right to charge GST depends on whether the payer is entitled to a full GST credit. [ATO Schedule 10 applicable 1 July 2024 to 30 June 2026][AGREE]; [ATO voluntary-agreement conditions][AGREEMENT].

For no-ABN withholding, first apply s 12-190's enterprise/supply conditions and exceptions. Check supplier/agent ABN documents, non-enterprise payments, total consideration for the whole supply of $75 or less excluding GST, wholly input-taxed supplies, local-government activities, investment-payment exclusions, and a qualifying individual's written hobby/private/domestic statement that you have no reasonable grounds to disbelieve. If withholding is required, withhold **47% of the total payment**, including GST, and report at W4 where that label applies. A missing ABN on the invoice alone does not establish liability. [TAA Schedule 1 s 12-190][TAA1]; [ATO no-ABN instructions][NOABN].

For small/medium withholders, reconcile the required labels to payroll records, tax tables, STP and any ATO pre-fill. STP does **not** give them a blanket W1 exemption. Verify and correct pre-filled amounts; payroll/software records remain the primary source. [ATO withholding labels][W]; [ATO pre-fill][PREFILL].

- **W1:** total gross salary, wages and other covered payments, including covered payments with nil tax withheld. Exclude salary sacrifice, employer super contributions, no-ABN supply payments and other W1 exclusions in the instructions.
- **W2:** tax withheld from payments shown at W1.
- **W4:** tax withheld because an ABN was not quoted.
- **W3:** other withholding, excluding amounts already in W2/W4.
- **W5 = W2 + W3 + W4**, excluding W1. Transfer W5 to summary label 4, or the withholding-only form's label 9 where there is no summary.

These are [ATO label definitions][W]. A large withholder completes only W1 if not reporting through STP; if reporting through STP it also omits W1. Large withholders do not complete W2–W5 or summary label 4 and pay electronically under their separate schedule. Other tax roles still require their own reporting.

A small employer with **19 or fewer payees** can choose quarterly STP reporting for closely held payees; other arm's-length payees remain reportable on or before payday. The concession does not cancel BAS reporting/payment. [ATO STP checklist][CLOSE].

## PAYG income-tax instalments

Automatic entry for individuals requires **all three**: latest-return instalment income at least **$4,000**, latest-assessment tax payable at least **$1,000**, and estimated/notional tax at least **$500**. A new business can request voluntary entry. Liability follows the Commissioner's written instalment-rate notice; payments start when the ATO sends the activity statement/notice, not automatically on a fixed first-business anniversary. [ATO entry][ENTRY]; [TAA Schedule 1 s 45-15][TAA2].

Use the offered method and actual notice. GDP adjustment belongs to the instalment-amount calculation, not an automatic increase to T2. The original **2024–25 6%** row is historical; for an ordinary 1 July 2025–30 June 2026 year the factor is **4%**. For SAP years commencing 1 January, February or March 2025 the ATO retains 6%; years starting from 1 April 2025 use 4%. Do not invent a GDP increase after repeated variations. [ATO historical factor][GDP24]; [ATO 2025–26 factor][GDP25]; [TAA Schedule 1 ss 45-400 and 45-405][TAA2].

### Amount method

Use T7 as notified unless varying. For a standard four-quarter payer, count quarters **from the first quarter for which liable**. Estimate full-year tax at T8. The cumulative shares are 25%, 50%, 75% and 100%, less earlier instalment liabilities, adding back earlier credit entitlements as required by s 45-410. Enter the varied result at T9, reason at T4 and payable amount at 5A. For a nil/negative result put zero at T9/5A; a qualifying negative result may be claimed as a **positive** credit at 5B. Two-instalment, annual or other cycles need their own ATO instructions; do not apply the four-quarter formula to them. [ATO amount variation][VARY]; [TAA Schedule 1 ss 45-410 to 45-420][TAA2].

**Original case:** at the third standard quarterly instalment, annual estimated tax **$8,000**, earlier instalments **$3,000**, no earlier credits: $8,000 × 75% = **$6,000**, less $3,000 = **$3,000** current instalment. Dividing $8,000 by two remaining quarters would give $4,000 and is incorrect.

```oa-check
name: Original third-quarter PAYG amount variation
inputs:
  annual_tax: 8000
  previous_instalments: 3000
  previous_credits: 0
steps:
  - cumulative_target: annual_tax * 0.75
  - current_instalment: cumulative_target - previous_instalments + previous_credits
  - rejected_remaining_quarters: annual_tax / 2
expected:
  cumulative_target: 6000
  current_instalment: 3000
  rejected_remaining_quarters: 4000
```

```oa-check
name: Original case cumulative-payment reconciliation
inputs:
  annual_tax: 8000
  earlier_instalments: 3000
  current_instalment: 3000
steps:
  - payments_to_date: earlier_instalments + current_instalment
  - target: annual_tax * 0.75
  - difference: payments_to_date - target
expected:
  payments_to_date: 6000
  target: 6000
  difference: 0
```

### Rate method

T1 is gross business/investment instalment income, excluding GST, salary/wages subject to PAYG withholding and capital gains for these individuals. Include ordinary business income even if tax was withheld for non-quotation of TFN/ABN; apply special partnership/trust and farm-management-deposit rules when relevant. Use T2 as shown (which can reflect an earlier variation); a new varied rate goes at T3 with reason at T4. **T11 = T1 × applicable rate**, using T3 when newly varied, otherwise T2; transfer T11 to 5A. A rate reduction may also permit a 5B credit for earlier quarters under the ATO instructions. [ATO instalment income][INCOME]; [ATO rate-method labels][INSTAL]; [TAA Schedule 1 ss 45-110, 45-120 and 45-215][TAA2].

Variation must be lodged by the instalment due date and before the year's tax return. A rate variation below **85% of the benchmark instalment rate** can trigger GIC under s 45-230; for an amount variation s 45-232 compares the estimate with **85% of benchmark tax** and uses the statutory acceptable-versus-actual instalment calculation. These are different tests. Keep and review the full-year estimate. This Guide does not calculate the interest charge. [ATO variations][VARY]; [TAA Schedule 1 ss 45-230 to 45-240][TAA2].

### Stopping instalments

Automatic individual exit includes notional tax **below $500**; this is not a standalone right to stop paying yourself. Request exit when no longer earning business/investment income, subject to the ATO exclusions: bankruptcy with a Part IX debt agreement/Part X personal-insolvency agreement, and specified low-debt/refund cases that become debts over $500 when instalments are included. In linked myGov use **Tax > Manage > Tax registrations > Cancel**, available only when eligible; an agent or the ATO can also take a request. Liability for further instalments ceases on withdrawal of the rate, rather than merely sending a request. [ATO exit instructions][STOP]; [TAA Schedule 1 s 45-90][TAA2].

## FBT instalments: F1 to F4, 6A and 6B

FBT uses its own year, **1 April to 31 March**. The ATO's ordinary quarterly-instalment instructions apply where prior-year FBT payable was **$3,000 or more**. Use the actual notified obligation: the statutory notional amount can reflect the latest assessed year, no-assessment/nil cases, a Commissioner determination or an accepted estimate; it is not invariably last year's final liability. The correct authority is FBTAA ss 102, 110–112A and 136(1), rather than TAA PAYG provisions or FBTAA s 149. [FBTAA][FBTLAW]; [ATO instalment instructions][FBT].

- **Unvaried:** use the notified F1 and copy it to 6A. An unchanged ordinary base gives a quarter of the annual notional amount, but do not overwrite a different notified amount.
- **Varied:** estimate annual FBT at F2, calculate F3 and enter the variation reason at F4. Use cumulative percentages 25%, 50%, 75%, 100% for quarters ending June, September, December and March respectively. Subtract previous instalments less previous credits. A positive result goes at F3 and 6A; for zero/negative results enter zero at F3/6A. A qualifying negative result may be claimed at 6B as a positive credit. Do not report a varied amount at F1.
- Review the estimate carefully: FBT's variation-shortfall test uses **90%**, distinct from PAYG's 85% tests. This Guide does not compute the FBT interest/penalty outcome.

Follow [ATO F1/F2/F3/F4/6A/6B instructions][FBT] and [FBTAA ss 111–112B][FBTLAW]. An estimate below the instalment threshold does not itself cancel an existing quarterly obligation.

The annual FBT return reconciles the year's instalments against actual liability. The ordinary return/payment date is **21 May**; generally **25 June** only where an agent lodges electronically and the employer was on the agent's FBT client list by **21 May**. Check extensions and next-business-day adjustments. Lodge all required FBT-year activity statements, including March, before the annual FBT return. [ATO annual FBT instructions][FBTDUE].

## Whole-statement reconciliation and penalties

Combine only applicable payment/credit labels on the issued statement. For the ordinary combined form, payment labels include 1A, 4, 5A and 6A; credits include 1B, 5B and 6B. Include other applicable statement amounts, including supported fuel-credit entries, before calculating the statement's payment/refund total. Exclude separately paid large-withholder amounts; never add the annual estimate T8 as a tax payment or add W1 to withheld tax. Reconcile with the GST working paper and ATO account. [ATO withholding labels][W]; [ATO PAYG labels][INSTAL]; [ATO FBT labels][FBT].

A required return/statement not given in approved form by its due date may attract FTL penalties. The base is **one penalty unit per 28 days or part**, up to **five base units**. Apply the statutory medium/large/significant-global-entity multipliers when relevant; five units is not a universal maximum. The unit value is the value at the start of each relevant 28-day period. A registered-agent safe harbour may apply where all relevant information was supplied in time and the failure did not result from the agent's recklessness or intentional disregard. The Commissioner may remit all or part of the penalty. [TAA Schedule 1 ss 286-75, 286-80 and 298-20][TAA2].

**Non-usable historical details:** earlier versions covered 2024–25 (1 July 2024 to 30 June 2025), used a $10 million GST cycle boundary, quoted a flat $313 penalty unit for 2024–25, described GIC as a 90-day-bank-bill rate plus 7%, and added a GIC deduction statement from 1 July 2025. Do not use those historical lines to determine a current cycle, period-specific penalty or GIC/deduction outcome. The former 1 January 2022 STP reference also does not establish an exemption from W1/W2. The current methods above govern ordinary reporting; for a historical interest/deduction/penalty calculation: Check this point with one of our partner accountants.

## Review before filing

- Match the taxpayer, actual period, offered method, classification, notices and deadline.
- Reconcile payroll/STP/pre-fill, T1 income, T7 or T3/T4/T11, F1 or F2/F3/F4, credits and the GST working paper.
- Retain the estimate and source records; identify unresolved entries and obtain professional review before filing.

## Sources

Read dates below record actual relied-upon text reads, including indexed ATO source text where direct requests returned HTTP 403. The 22 November report is reused for unchanged scope and source-read applicability; its missing exact quotations were supplied on 27 November. Historical statutory compilations are used for the original year; current notices still control the taxpayer's filing.

[W]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding "Read 2026-11-27"
[CYCLE]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/paying-and-reporting-payg-withholding-amounts-for-small-and-medium-withholders "Read 2026-11-27"
[TAA1]: https://www.legislation.gov.au/C1953A00001/2025-07-01/2025-07-01/text/original/epub/OEBPS/document_1/document_1.html "Read 2026-11-27"
[TAA2]: https://www.legislation.gov.au/C1953A00001/2025-07-01/2025-07-01/text/original/epub/OEBPS/document_2/document_2.html "Read 2026-11-27"
[GST]: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html "Read 2026-11-27"
[DUE]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas "Read 2026-11-27"
[PROGRAM]: https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-by-obligation-type/activity-statements "Read 2026-11-27"
[NOTICES]: https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/your-practice/managing-electronic-activity-statements-and-instalment-notices "Read 2026-11-27"
[NOABN]: https://www.ato.gov.au/forms-and-instructions/statement-by-supplier-not-quoting-an-abn "Read 2026-11-27"
[AGREE]: https://www.ato.gov.au/api/public/content/0-19524f95-212e-4bdf-b439-abc0b39dcc98 "Read 2026-11-27"
[AGREEMENT]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/payments-under-a-voluntary-agreement "Read 2026-11-27"
[LABOUR]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/labour-hire-firms-and-their-workers "Read 2026-11-27"
[ENTRY]: https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/starting-payg-instalments "Read 2026-11-27"
[VARY]: https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments "Read 2026-11-27"
[INSTAL]: https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement "Read 2026-11-27"
[INCOME]: https://www.ato.gov.au/Business/PAYG-instalments/Calculate-your-PAYG-instalments/Instalment-income/ "Read 2026-11-27"
[GDP24]: https://softwaredevelopers.ato.gov.au/gdp-adjustment-2024-25-gst-and-payg-instalments "Read 2026-11-27"
[GDP25]: https://softwaredevelopers.ato.gov.au/gdp-adjustment-2025-26-gst-and-payg-instalments "Read 2026-11-27"
[FBT]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/fringe-benefits-tax-fbt-instalment "Read 2026-11-27"
[FBTLAW]: https://www.legislation.gov.au/C2004A03280/2025-02-15/2025-02-15/text/original/epub/OEBPS/document_2/document_2.html "Read 2026-11-27"
[FBTDUE]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/fbt-registration-lodgment-payment-and-reporting/lodging-your-fbt-return-and-paying "Read 2026-11-27"
[PREFILL]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/stp-and-activity-statements/ato-payg-withholding-pre-fill-for-activity-statements "Read 2026-11-27"
[CLOSE]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/start-reporting/stp-checklists "Read 2026-11-27"
[STOP]: https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/stopping-payg-instalments "Read 2026-11-27"
[PAUSED]: https://www.ato.gov.au/api/public/content/0-49df3169-15a8-4445-a4b8-28464c117790 "Read 2026-11-27"

Not yet confirmed: no taxpayer payroll, ATO notice, lodged return or real account was supplied. Fuel-credit computations and the historical GIC/deduction/flat-dollar penalty outcomes identified above are non-usable holds. Check this point with one of our partner accountants.

## Disclaimer

This Guide and its outputs are informational working papers and do not constitute tax, legal or financial advice. Obtain qualified professional review before filing or acting.

> Contributed by Ryan Duguid.
