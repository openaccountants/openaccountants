---
name: us-form-941-940-payroll
description: Compute US federal employer payroll taxes for 2026 and prepare Forms 941, 940, W-2 and W-3. Covers FICA wage bases, Additional Medicare withholding, monthly and semiweekly deposits, FUTA credit reductions, wage exclusions, Form W-4, corrections and penalties, with historical 2025 cases kept separate.
version: "3.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# US federal employer payroll: Forms 941, 940, W-2 and W-3, tax year 2026

For ordinary covered employees in 2026, each side pays Social Security at 6.2% up to USD 184,500 and Medicare at 1.45% without a cap. Withhold a further employee-only 0.9% on this employer's Medicare wages above USD 200,000. Determine the deposit schedule before computing the return; filing a return does not replace a required deposit. [IRS Pub. 15 (2026), Social Security/Medicare withholding and section 11](https://www.irs.gov/publications/p15).

## Scope and who this is for

US businesses paying covered W-2 employees in 2026. This is federal payroll guidance; the historical cases below retain their stated years. For Circular 230 purposes, outputs are general guidance based on the stated assumptions; obtain professional review before filing.

Route state/local withholding, SUTA, disability and paid leave to `us-state-payroll-matrix`; new hires to `us-state-new-hire-reporting-matrix`; contractors/classification to `us-1099-nec-issuance`; family employment to `us-hiring-your-children-and-accountable-plans`; sole-proprietor SE tax to `us-schedule-c-and-se-computation`; S corporation salary to `us-s-corp-election-decision`; research-credit eligibility/election to `us-r-and-d-section-174-and-41`; individual deductions to `us-form-1040-individual-return`; collections to `us-irs-collections-and-controversy`. Use `us-tax-workflow-base`, `us-federal-return-assembly` and `us-quarterly-estimated-tax` for their separate workflows.

## Ask the client first

Collect the original quarterly Form 941 line 12 amounts for July 2024–June 2025; any Form 944 filing in 2024–2025; any next-day liability in 2025–2026; payroll registers by payment date; year-to-date totals and predecessor/provider changes; each deduction's plan documents and employee eligibility; S corporation ownership; fringe benefits and sick pay; employee work states and state UI payment dates; tips, occupations and FLSA overtime; current W-4s; deposit confirmations and prior notices. Obtain the actual original and corrected returns before recommending corrections.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 rule and conditions | Official source |
| --- | --- | --- |
| Social Security | 6.2% employee and 6.2% employer; combined 12.4%; wages plus tips capped at USD 184,500 per employee for this employer | [Pub. 15, Social Security/Medicare withholding](https://www.irs.gov/publications/p15) |
| Medicare | 1.45% each side, combined 2.9%; all covered wages, no cap | [Pub. 15, Social Security/Medicare withholding](https://www.irs.gov/publications/p15) |
| Additional Medicare withholding | 0.9% employee only on Medicare wages above USD 200,000 from this employer during the calendar year, starting with the excess in the crossing pay period | [Pub. 15, Social Security/Medicare withholding](https://www.irs.gov/publications/p15) |
| Supplemental wages | Optional 22% only when separately identified and regular-wage income tax was withheld in the current or immediately preceding calendar year; otherwise use the applicable aggregate method. Mandatory 37% on annual supplemental wages above USD 1 million, counting businesses under common control | [Pub. 15, section 7](https://www.irs.gov/publications/p15) |
| FUTA | Employer only; 6.0% on first USD 7,000 per employee. Up to 5.4% credit; 0.6% after full credit only if state UI was paid in full, on time, on the same wages and no credit reduction applies | [Pub. 15, section 14](https://www.irs.gov/publications/p15) |
| Final credit reduction | California 1.5%; U.S. Virgin Islands zero after repayment. Derived California rate with otherwise full credit: 0.6% + 1.5% = 2.1% | [DOL final 2026 determination, note and state rows](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx) |

### 1. Set and operate the deposit schedule

Use the four original Form 941 line 12 amounts from **1 July 2024 through 30 June 2025**. Form 941-X adjustments do not change the lookback. USD 50,000 or less means monthly; more means semiweekly. A 2026 Form 941 filer that filed Form 944 in 2024 or 2025 uses calendar 2024 instead; Forms 943/944/945 use the second preceding calendar year. Before a new business starts or is acquired, lookback liabilities count as zero: normally monthly for the first year for Form 941, first two years for Forms 943/944/945, subject to the next-day rule. [Pub. 15, section 11, Table 1](https://www.irs.gov/publications/p15).

- Monthly: wages paid during a month are deposited by the next month's 15th.
- Semiweekly: Wednesday–Friday paydays deposit by the following Wednesday; Saturday–Tuesday paydays by the following Friday. Attach Schedule B to Form 941. Separate deposits are required if paydays in one deposit period fall in different quarters: the original 30 September and 2 October 2026 example requires two deposits, both due 7 October.
- Liability follows the date wages are paid, not accrued or earned. Schedule B records liability dates, never deposit dates, and must total line 12. A new back-pay payment belongs to its payment period; correcting a previously reported amount is a separate question.
- At **USD 100,000 or more accumulated in one deposit period**, deposit by the next business day. Test before nonrefundable credits. Stop accumulation at the end of that day and restart the next day; do not combine different deposit periods. A monthly depositor becomes semiweekly the next day for the rest of that year and the next. Thus the original USD 95,000 Tuesday / USD 10,000 Wednesday semiweekly example does not trigger next-day payment: they belong to different periods, due Friday and the following Wednesday respectively.
- Weekend or District of Columbia legal-holiday deposit deadlines roll to the next business day. Semiweekly depositors have at least three business days after the deposit period; other statewide holidays do not postpone deposits.

Source for each deposit rule: [Pub. 15, section 11](https://www.irs.gov/publications/p15).

**Payment with return:** a timely Form 941 may include payment in full if current **or** prior quarter line 12 is below USD 2,500 and there was no current-quarter next-day obligation. If relying on the prior quarter and current line 12 reaches USD 100,000, still supply the liability record required by line 16. The separate accuracy-of-deposits concession requires a shortfall no greater than the larger of USD 100 or 2% and timely makeup: monthly filers by the return due date (deposit or pay with return); semiweekly filers deposit by the earlier of the return due date and the first Wednesday/Friday on or after the next month's 15th. [Pub. 15, section 11](https://www.irs.gov/publications/p15); [Form 941 instructions, line 16](https://www.irs.gov/instructions/i941).

**Electronic deposits:** EFT may use EFTPS, IRS Direct Pay or the IRS business tax account. EFTPS accepts same-day payments of USD 1 million or less submitted **before 3 p.m. Eastern on a business day**; larger payments must be submitted by **8 p.m. Eastern the preceding day**. Third-party cutoffs may differ. A same-day bank wire is another option, subject to the bank's arrangements and cutoff. Keep the EFT Trace Number. [Pub. 15, section 11, How To Deposit](https://www.irs.gov/publications/p15).

### 2. Compute wages and withholding

Use the employee's valid W-4 and the applicable [2026 Pub. 15-T tables](https://www.irs.gov/publications/p15t). A prior valid W-4 remains effective; for a new/re-hired employee in 2026 with no completed W-4, use Single/Married filing separately with no Steps 2–4 entries. A replacement takes effect no later than the start of the first payroll period ending on or after the 30th day after receipt, subject to IRS lock-in/invalid-form/exemption exceptions. Step 4(c) permits additional withholding. For a nonstandard request to replace the form with a fixed dollar or percentage instruction: **Check this point with one of our partner accountants.** [Pub. 15, section 9](https://www.irs.gov/publications/p15).

The 2026 W-4's five steps cover identity/status, multiple jobs/spouse, dependents/credits, other income/deductions/extra withholding, and signature. The simple Step 3 instruction for income up to USD 200,000 (USD 400,000 joint) uses USD 2,200 per qualifying child under 17 and USD 500 per other dependent; eligibility and SSN conditions remain in the form instructions. Use the Step 4(b) worksheet, including its tips/overtime/car-loan entries where applicable. A 2026 exemption needs both no 2025 federal income tax liability and none expected for 2026, the exemption checkbox and a signed form; renew by **16 February 2027**. On expiry use Single/Married filing separately with no Steps 2–4 entries, with no refund of tax correctly withheld before a new exemption. [2026 Form W-4 and instructions](https://www.irs.gov/pub/irs-pdf/fw4.pdf); [Pub. 15, section 9](https://www.irs.gov/publications/p15).

For each pay date, compute income tax withholding, both halves of capped Social Security and uncapped Medicare, and employee Additional Medicare. Their sum is the ordinary liability before adjustments/credits. Explain each wage-base difference:

| Payment/deduction | Federal payroll treatment | Source |
| --- | --- | --- |
| Traditional elective retirement deferrals | Generally excluded from income-tax wages within applicable plan limits, but included in FICA and FUTA wages; includes the original 401(k), 403(b) salary reduction and governmental 457(b) topics | [Pub. 15, section 15, retirement chart](https://www.irs.gov/publications/p15) |
| Designated Roth deferrals | Included in income-tax, Social Security and Medicare wages; the retirement salary deferral is not a FUTA exclusion | [W-2 instructions, designated Roth contributions](https://www.irs.gov/instructions/iw2w3); [Pub. 15, section 15](https://www.irs.gov/publications/p15) |
| Qualified cafeteria health premiums | A written plan is necessary, but does not alone establish an exclusion: check qualified benefits, eligibility and nondiscrimination. Do not apply an ordinary employee's cafeteria exclusion to a more-than-2% S corporation shareholder | [Pub. 15-B, Cafeteria Plans and exclusion chart](https://www.irs.gov/publications/p15b) |
| HSA | Eligible employer contributions within the statutory limits can be excluded from withholding, FICA and FUTA when reasonably believed excludable, including outside a cafeteria plan. Employee salary reductions require a qualifying cafeteria plan; after-tax employee funding does not reduce payroll wages. Partners and more-than-2% S corporation shareholders need separate treatment | [Pub. 15-B, HSAs](https://www.irs.gov/publications/p15b); [W-2 instructions, HSA](https://www.irs.gov/instructions/iw2w3) |

For the original dependent-care, adoption, transportation fringe, group-term life (including active/former employee and codes C/M/N), nonqualified deferred compensation/vesting, section 409A, and unusual benefit cases: **Check this point with one of our partner accountants.** Determine exclusions and corrections from the actual plan and employee facts; do not use the former unconditional wage-base table.

**Tips and overtime:** for 2026, code TP reports cash tips reported to the employer; enter Treasury Tipped Occupation Code(s) in box 14b. Code TT reports only qualified FLSA section 7 overtime compensation above the regular rate (the premium, not all overtime pay). They remain generally subject to income tax withholding and FICA; the employee's individual deduction does not itself create a payroll exclusion. Tips of at least USD 20 per month are generally subject to FICA. Box 14a is Other, with labeled information such as state disability or union dues. [2026 W-2 instructions, TP/TT and boxes 14a–14b](https://www.irs.gov/instructions/iw2w3). For Form 8027 allocation, allocated tips/box 8 and a section 3121(q) notice, obtain a specialist's computation rather than applying a blanket percentage: **Check this point with one of our partner accountants.**

### 3. Complete Form 941 (March 2026 revision)

| Lines | Entry | Source |
| --- | --- | --- |
| 1–4 | Count payroll employees for the period including March/June/September/December 12 (excluding the categories in the instructions); line 2 uses W-2 box 1 wages; line 3 income tax withheld; line 4 only if no wages subject to FICA | [941 instructions, lines 1–4](https://www.irs.gov/instructions/i941) |
| 5a–5e | Social Security wages on 5a and reported tips on 5b, within the combined employee annual cap; multiply by 0.124. Medicare wages/tips on 5c × 0.029. Wages/tips subject to Additional Medicare withholding on 5d × 0.009. Include reported tips even if employee tax could not be withheld; 5e totals column 2 | [941 instructions, lines 5a–5e](https://www.irs.gov/instructions/i941) |
| 5f | Tax from the IRS section 3121(q) Notice and Demand; liability arises on the notice date and follows the deposit schedule | [941 instructions, line 5f](https://www.irs.gov/instructions/i941) |
| 6–10 | Line 6 = 3 + 5e + 5f; 7 fractions of cents; 8 sick pay; 9 negative uncollected employee FICA on tips/former-employee group-term life; combine 6–9 on 10 | [941 form](https://www.irs.gov/pub/irs-pdf/f941.pdf); [941 instructions, lines 7–10](https://www.irs.gov/instructions/i941) |
| 11–12 | Attach Form 8974 for research credit on 11; first employer Social Security, up to USD 250,000 per quarter, then employer Medicare, remaining credit carried forward. Line 12 = 10 − 11, not below zero | [941 instructions, research credit and lines 11–12](https://www.irs.gov/instructions/i941) |
| 13–15e | 13 deposits and applicable prior overpayments, including credits from adjustment forms; 14 balance when 12 exceeds 13; **15a** overpayment, 15b choice, 15c–15e refund bank details | [941 form](https://www.irs.gov/pub/irs-pdf/f941.pdf) |
| 16 and Parts 3–5 | Use the de minimis box only under its full conditions above; otherwise monthly liabilities or Schedule B. Complete closure/seasonal information as applicable, designee and signature | [941 form](https://www.irs.gov/pub/irs-pdf/f941.pdf); [941 instructions, line 16](https://www.irs.gov/instructions/i941) |

File every quarter after the initial wage quarter, including zero quarters, unless the seasonal/final-return exception applies. File electronically through an authorized provider or to the applicable IRS paper address; retain the accepted return and deposit reconciliation. Do not file a second original for a correction. **Form 941-X is separate from Form 941**. Correction deadlines, employee repayment/consent, income-tax/Additional Medicare restrictions and COVID-era claims depend on the error and year: **Check this point with one of our partner accountants.** [941 instructions](https://www.irs.gov/instructions/i941).

### 4. Form 940 and FUTA

The general FUTA test for 2026 is wages of at least USD 1,500 in any quarter of 2025 or 2026, **or** an employee for part of a day in at least 20 different weeks in either year. Household/farm tests differ and are referred below. Compute covered wages per employee, applying the annual base, credit conditions and applicable state's reduction. For multiple states, use one Form 940 and Schedule A; use wages subject to each state's unemployment law rather than assuming the work location alone decides the credit. If state UI excludes a FUTA-taxed payment, the net rate can exceed 0.6% even outside a credit-reduction state. [Pub. 15, section 14](https://www.irs.gov/publications/p15); [940 instructions, lines 1–2 and credit adjustments](https://www.irs.gov/instructions/i940).

Carry a quarter's liability forward when it is USD 500 or less; when accumulated liability exceeds USD 500, deposit by the last day of the following month. Include credit reduction as a **fourth-quarter liability**; an amount above USD 500 must be deposited, not merely paid with the return. If fourth-quarter liability plus carryforward is USD 500 or less, deposit or pay with timely Form 940. Corrections use Form 940 marked Amended, with corrected amounts and an explanation, not a Form 940-X. [Pub. 15, section 14](https://www.irs.gov/publications/p15); [940 instructions, amended returns](https://www.irs.gov/instructions/i940).

### 5. W-2, W-3 and reconciliation

Prepare W-2 for any employee with income tax/FICA withheld, or for whom withholding would have been required under the instruction's no-exemption/legacy-allowance test; also for at least USD 2,000 wages even without withholding. The small-wage threshold does not excuse an ordinary employee's FICA reporting. Boxes 1/2 are income-tax wages/withholding, 3 excludes Social Security tips (box 7), **boxes 3 + 7** cannot exceed USD 184,500, 4 is employee Social Security, 5 Medicare wages and 6 employee Medicare plus Additional Medicare. [2026 W-2 instructions](https://www.irs.gov/instructions/iw2w3).

E-file when the aggregate of covered information returns reaches **10**, including additional W-2s for extra codes; corrected returns are counted separately under their own rule. W-2c must be e-filed if the original was required to be e-filed; paper originals correctly filed on paper are corrected on paper. SSA Business Services Online generates W-3/W-3c totals automatically; paper filings use the transmittal. Furnish corrected employee copies as well. For Form 8508 hardship waivers and extension applications (including the nonautomatic Form 8809 SSA extension and a separate employee-furnishing extension): **Check this point with one of our partner accountants.** [W-2 instructions, e-filing and corrections](https://www.irs.gov/instructions/iw2w3).

For the original box 12 code catalog (A/B/C/D/E/F/G/H/J/K/L/M/N/P/Q/R/S/T/V/W/Y/Z/AA/BB/DD/EE/FF/GG/HH/II), extra-code forms and special reporting: consult the current code-specific instructions. In particular, code Y is not a blanket mandatory entry. For code TA and Trump-account program eligibility, contribution limits, dependent accounts and effective date: **Check this point with one of our partner accountants.** Do not infer exclusion merely from a code. [W-2 instructions, box 12](https://www.irs.gov/instructions/iw2w3). Codes TP/TT are covered above. State/local boxes 15–20 require the separate state workflow.

Reconcile the four Forms 941 to W-3: box 1 to line 2, box 2 to line 3, Social Security wages/tips to lines 5a/5b column 1, Medicare wages to 5c column 1. Ordinary employee Social Security equals half the 5a/5b column 2 taxes; ordinary employee Medicare equals half 5c column 2 plus all 5d column 2. Document sick pay, uncollected taxes and other adjustments before relying on those simple tax equalities. Payment-year wages are not moved by the deposit date. A discrepancy notice needs an actual reconciliation; no universal response period is assumed. [Pub. 15, section 12, reconciliation](https://www.irs.gov/publications/p15); [W-2 instructions, boxes 1–7](https://www.irs.gov/instructions/iw2w3).

### 6. Penalties and red flags

| Deposit failure | Rate, subject to applicable exceptions | Source |
| --- | --- | --- |
| Deposited 1–5 calendar days late | 2% | [Pub. 15, section 11](https://www.irs.gov/publications/p15) |
| Deposited 6–15 days late | 5% | [Pub. 15, section 11](https://www.irs.gov/publications/p15) |
| Deposited 16+ days late before notice escalation, or improperly paid directly/with return | 10% | [Pub. 15, section 11](https://www.irs.gov/publications/p15) |
| Still unpaid more than 10 days after the first IRS notice, or on receipt of immediate notice and demand, whichever earlier | 15% | [Pub. 15, section 11](https://www.irs.gov/publications/p15) |

Compute each deposit separately using calendar days. Deposits generally apply to the most recent liability within the quarter. Reasonable cause without willful neglect can prevent the deposit penalty. Inadvertent first-quarter/changed-frequency relief also requires a timely return and the section 7430 net-worth/size conditions. Obtain advice for an actual relief application, allocation designation, first-time abatement or appeal: **Check this point with one of our partner accountants.** [Pub. 15, section 11](https://www.irs.gov/publications/p15).

Late filing generally costs 5% of unpaid tax per month or part month, up to 25%; late payment generally costs 0.5% per month, up to 25%. For overlapping months the filing penalty is reduced by the payment penalty; reasonable-cause exceptions apply. Responsible persons who willfully fail to collect, account for or pay trust taxes can face the 100% trust fund recovery penalty. For an actual assessment, accelerated/default rates, minimums or personal liability: **Check this point with one of our partner accountants.** [Pub. 15, sections 11–12](https://www.irs.gov/publications/p15).

For W-2 filings due after 31 December 2026, ordinary late/correction penalties per form are USD 60 when correctly filed within 30 days, USD 130 thereafter through 1 August, and USD 340 after that or not filed. Annual caps, small-business caps and exceptions apply. Separate failure-to-furnish penalties and intentional disregard require their own analysis: **Check this point with one of our partner accountants.** [W-2 instructions, Penalties](https://www.irs.gov/instructions/iw2w3).

Investigate a lost year-to-date balance after a provider change, off-cycle bonus or negative adjustment, combined EINs, a prior-year cap left in the system, 5a wages above 5c, tax instead of wages on 5d, Schedule B not totaling line 12, missing TP/TT/14b, unexplained boxes 1/3/5 differences, or California FUTA without credit reduction. These are investigation prompts, not proof of an error; compare actual coverage, payment dates and adjustments.

## Worked cases

**Case 1, a decision: monthly or semiweekly depositor for 2026?** Harbor Supply LLC files Form 941. As originally filed, line 12 was USD 11,800 for Q3 2024, USD 12,600 for Q4 2024, USD 13,100 for Q1 2025 and USD 13,400 for Q2 2025. In January 2026 its bookkeeper filed a Form 941-X reducing Q4 2024 by USD 1,500, and proposes to treat the company as a monthly depositor because the corrected total is USD 49,400.

The lookback total uses the amounts originally reported: USD 50,900, which is more than USD 50,000, so Harbor Supply is a **semiweekly depositor for all of 2026** and must attach Schedule B to each Form 941. The Form 941-X does not change this (Pub. 15 (2026), section 11, "Adjustments and the lookback rule"). On Friday 6 March 2026 it pays wages of USD 21,000 (all under the wage bases) and withholds USD 2,730 of income tax. FICA on both sides is USD 21,000 x 15.3% = USD 3,213, so the pay-date liability is USD 5,943, due by **Wednesday 11 March 2026**. If paid on 15 April 2026, it is 35 days late; assuming no earlier notice escalation or relief, the 10% failure-to-deposit penalty is USD 594.30 on this deposit. Recommend: semiweekly schedule, Schedule B, and set the payroll system to deposit on the Wednesday and Friday cycle.

```oa-check
name: Lookback rule, monthly or semiweekly for 2026, and one Friday deposit
inputs:
  q3_2024: 11800
  q4_2024: 12600
  q1_2025: 13100
  q2_2025: 13400
  form_941x_change: -1500
  wages: 21000
  income_tax_withheld: 2730
steps:
  - lookback_total: q3_2024 + q4_2024 + q1_2025 + q2_2025
  - corrected_total_not_used: lookback_total + form_941x_change
  - semiweekly: clamp(ceil((lookback_total - 50000) / 1000000), 0, 1)
  - fica_both_halves: wages * 0.153
  - deposit: income_tax_withheld + fica_both_halves
  - penalty_if_paid_monthly: deposit * 0.10
expected:
  lookback_total: 50900.00
  corrected_total_not_used: 49400.00
  semiweekly: 1
  fica_both_halves: 3213.00
  deposit: 5943.00
  penalty_if_paid_monthly: 594.30
```

**Case 2, an executive crossing the wage base and the Additional Medicare trigger.** Northwind Analytics Inc. pays its CEO USD 25,000 on the last day of each month in 2026 (USD 300,000 for the year, no pre-tax deductions).

- **Social Security:** cumulative wages are USD 175,000 after July. August's USD 25,000 is taxed only on USD 9,500 (to reach USD 184,500): employee tax USD 589 that month, then nothing for September to December. Box 3 is USD 184,500 and box 4 is USD 11,439.
- **Additional Medicare:** cumulative wages reach exactly USD 200,000 at the end of August (not "in excess of"). From the September payroll, 0.9% is withheld on every dollar: USD 225 a month, USD 900 for the year on USD 100,000.
- **Box 5** is USD 300,000; **box 6** is USD 4,350 (1.45%) + USD 900 = USD 5,250.
- **Q3 Form 941, this employee only:** line 5a column 1 USD 34,500 (July 25,000 + August 9,500) x 0.124 = USD 4,278; line 5c column 1 USD 75,000 x 0.029 = USD 2,175; line 5d column 1 USD 25,000 x 0.009 = USD 225.

Common errors: box 3 at USD 300,000 (no cap), or at USD 200,000 (confusing the wage base with the Additional Medicare trigger), or using the 2025 base of USD 176,100.

```oa-check
name: Wage base crossover and Additional Medicare withholding, USD 300,000 salary (2026)
inputs:
  annual_wages: 300000
  wages_through_july: 175000
  wage_base: 184500
  addl_trigger: 200000
  q3_medicare_wages: 75000
  september_wages: 25000
steps:
  - august_ss_wages: wage_base - wages_through_july
  - august_employee_ss: august_ss_wages * 0.062
  - box_3: min(annual_wages, wage_base)
  - box_4: box_3 * 0.062
  - additional_medicare: max(annual_wages - addl_trigger, 0) * 0.009
  - box_6: annual_wages * 0.0145 + additional_medicare
  - q3_line_5a_wages: 25000 + august_ss_wages
  - q3_line_5a_tax: q3_line_5a_wages * 0.124
  - q3_line_5c_tax: q3_medicare_wages * 0.029
  - q3_line_5d_tax: september_wages * 0.009
expected:
  august_ss_wages: 9500.00
  august_employee_ss: 589.00
  box_3: 184500.00
  box_4: 11439.00
  additional_medicare: 900.00
  box_6: 5250.00
  q3_line_5a_wages: 34500.00
  q3_line_5a_tax: 4278.00
  q3_line_5c_tax: 2175.00
  q3_line_5d_tax: 225.00
```

**Case 3, FUTA in California, the 2026 credit reduction state.** Pacific Grove Cafe LLC pays wages only in California and pays its state unemployment tax in full and on time. Its 12 employees each earn more than USD 7,000 in 2026, half of the FUTA wages in Q1 and half in Q2.

FUTA wages: 12 x USD 7,000 = USD 84,000. Gross FUTA at 6.0% is USD 5,040; the 5.4% credit is USD 4,536; net at 0.6% is USD 504. Schedule A: USD 84,000 x 0.015 = USD 1,260 of credit reduction. Total 2026 FUTA: USD 1,764, which is USD 147 per employee. Deposits: Q1 USD 252 (USD 500 or less, carry forward); Q2 cumulative USD 504 (over USD 500), deposit by **31 July 2026**; Q3 nil; the USD 1,260 credit reduction is a fourth-quarter liability, over USD 500, so it is deposited by **1 February 2027** (31 January 2027 is a Sunday). Form 940 with Schedule A is due 1 February 2027, or 10 February 2027 if every FUTA deposit was made on time.

```oa-check
name: Form 940 with the 2026 California credit reduction, 12 employees
inputs:
  employees: 12
  futa_base: 7000
  ca_reduction: 0.015
steps:
  - futa_wages: employees * futa_base
  - gross_futa: futa_wages * 0.06
  - state_credit: futa_wages * 0.054
  - net_futa: gross_futa - state_credit
  - credit_reduction: futa_wages * ca_reduction
  - total_futa: net_futa + credit_reduction
  - per_employee: total_futa / employees
  - q1_liability: futa_wages / 2 * 0.006
expected:
  futa_wages: 84000.00
  gross_futa: 5040.00
  state_credit: 4536.00
  net_futa: 504.00
  credit_reduction: 1260.00
  total_futa: 1764.00
  per_employee: 147.00
  q1_liability: 252.00
```

**Case 4, a small employer's Q2 2026 Form 941.** Acme Coffee Roasters LLC (three employees, monthly depositor) paid Q2 2026 gross wages of USD 46,200, with USD 2,200 of traditional 401(k) deferrals, USD 2,000 of section 125 health premiums under a written plan, and USD 5,960 of income tax withheld. Assume all three qualify for these exclusions, are not more-than-2% S corporation shareholders, nobody is near the wage base or Additional Medicare trigger, and there are no other adjustments or credits. Line 2: USD 46,200 - 2,200 - 2,000 = USD 42,000. Lines 5a and 5c column 1: USD 46,200 - 2,000 = USD 44,200 (the 401(k) stays in FICA wages). Line 5a column 2: USD 5,480.80; line 5c column 2: USD 1,281.80; line 5e: USD 6,762.60; lines 6, 10 and 12: USD 12,722.60. Deposits: April wages by 15 May 2026, May by 15 June 2026, June by 15 July 2026. Form 941 due 31 July 2026, or 10 August 2026 if every deposit was on time.


```oa-check
name: Acme Q2 2026 ordinary employees with qualified deductions
inputs:
  gross: 46200
  traditional_401k: 2200
  health: 2000
  withholding: 5960
steps:
  - line_2: gross - traditional_401k - health
  - fica_wages: gross - health
  - line_5a_tax: fica_wages * 0.124
  - line_5c_tax: fica_wages * 0.029
  - line_5e: line_5a_tax + line_5c_tax
  - line_12: withholding + line_5e
expected:
  line_2: 42000
  fica_wages: 44200
  line_5a_tax: 5480.80
  line_5c_tax: 1281.80
  line_5e: 6762.60
  line_12: 12722.60
```

### Historical 2025 cases: original inputs and years

**Original Acme case, 2025 Q2 (old 12.1).** Acme Coffee Roasters LLC was a single-member LLC taxed as an S corporation. Alice, owner-employee: gross wages USD 25,000, traditional 401(k) USD 1,500, health premium USD 1,200, income tax withheld USD 4,200. Bob, shift lead: USD 14,000 / USD 700 / USD 800 / USD 1,400 respectively. Carla, barista: USD 7,200 / zero / zero / USD 360. Totals remain USD 46,200 / USD 2,200 / USD 2,000 / USD 5,960. The old arithmetic—USD 42,000 income-tax wages, USD 44,200 FICA wages, USD 5,480.80 combined Social Security, USD 1,281.80 combined Medicare, USD 6,762.60 total FICA and USD 12,722.60 total tax—requires exclusions not established for Alice. These are **non-usable filing totals for the owner scenario**. **Check this point with one of our partner accountants.** The original monthly-depositor assumption used July 2023–June 2024 lookback below USD 50,000; the original approximately USD 4,240 per month was an estimate, not an exact payroll allocation. The 2025 monthly deposit dates were 15 May, 16 June and 15 July; Q2 filing was 31 July or 11 August with timely full deposits. [Pub. 15-B, cafeteria/S corporation conditions](https://www.irs.gov/publications/p15b); [2025 Pub. 15, sections 11–12 and Calendar](https://www.irs.gov/pub/irs-prior/p15--2025.pdf).

**Original TechCo case, 2025 (old 12.2).** TechCo Inc. had eight employees; Carol, CEO, earned USD 300,000 paid USD 25,000 monthly, and the other employees earned below USD 176,100. After USD 175,000 through July, August Social Security wages are USD 1,100 and employee tax USD 68.20; annual employee Social Security is USD 10,918.20. Q3 Social Security wages are USD 26,100, combined tax USD 3,236.40; Medicare wages USD 75,000, combined tax USD 2,175; Additional Medicare wages USD 25,000, tax USD 225. Cumulative wages reach exactly USD 200,000 in August; Additional Medicare starts with September's USD 25,000, USD 225 each month through December, USD 900 for the year. W-2 boxes 1/3/4/5/6 are USD 300,000 / USD 176,100 / USD 10,918.20 / USD 300,000 / USD 5,250. Do not apply the 2026 base to this 2025 case. [2025 Pub. 15, wage base and Social Security/Medicare withholding](https://www.irs.gov/pub/irs-prior/p15--2025.pdf).

**Original BeachCo case, 2025 (old 12.3).** BeachCo LLC had 12 California employees, each earning above USD 7,000; total FUTA wages USD 84,000, USD 42,000 in each of Q1 and Q2. Assuming full timely state credit before reduction: gross FUTA USD 5,040, credit USD 4,536, base tax USD 504. The old heading mixed a 2024 reduction with 2025 facts. For **2025**, California's 1.2% gives USD 1,008 reduction, USD 1,512 total and USD 126 per employee. Q1 USD 252 carries; cumulative USD 504 is deposited by 31 July 2025. The USD 1,008 reduction is a fourth-quarter deposit due **2 February 2026**, not a balance merely paid with the return. Form 940 is due that day or 10 February with full timely deposits. The original 2024 illustration using 0.9% produced USD 756 reduction, USD 1,260 total and USD 105 each; that arithmetic does not determine the 2025 rate. [DOL final 2025 determination](https://www.govinfo.gov/content/pkg/FR-2026-01-12/html/2026-00342.htm); [2025 Pub. 15, section 14](https://www.irs.gov/pub/irs-prior/p15--2025.pdf); [Form 940 instructions, 2025 deadline](https://www.irs.gov/instructions/i940).

**Original TechCo reconciliation, 2025 (old 12.4).** Illustrative annual wages USD 1,800,000, income tax withheld USD 360,000, Social Security wages USD 1,408,800 for eight employees. The original link to Carol at USD 300,000 and seven employees below the base cannot produce those totals. The 6 July correction explicitly used a separate Carol wage assumption of **USD 567,300**, with the other seven totaling USD 1,232,700. Under that corrected assumption and no other adjustments: combined Social Security USD 174,691.20, employee box 4 USD 87,345.60; regular Medicare USD 52,200, employee regular Medicare USD 26,100; Additional Medicare USD 3,305.70 on USD 367,300; combined Medicare/Additional USD 55,505.70 and box 6 USD 29,405.70. The earlier USD 53,100 / USD 27,000 / USD 54,000 / USD 27,900 figures were incorrect or belonged to the incompatible USD 900 Additional Medicare assumption. Keep the original facts for diagnosis; do not combine the two Carol scenarios. [2025 Pub. 15, Social Security/Medicare](https://www.irs.gov/pub/irs-prior/p15--2025.pdf).

```oa-check
name: Historical 2025 Carol and separate corrected reconciliation
inputs:
  base_2025: 176100
  carol_original: 300000
  monthly: 25000
  july_ytd: 175000
  all_wages: 1800000
  ss_wages: 1408800
  carol_reconciliation: 567300
steps:
  - august_ss: base_2025 - july_ytd
  - august_ss_tax: august_ss * 0.062
  - annual_ss: base_2025 * 0.062
  - q3_ss: monthly + august_ss
  - q3_ss_tax: q3_ss * 0.124
  - original_additional: (carol_original - 200000) * 0.009
  - original_box_6: carol_original * 0.0145 + original_additional
  - other_seven_wages: all_wages - carol_reconciliation
  - reconciled_ss: ss_wages * 0.124
  - reconciled_box_4: reconciled_ss / 2
  - regular_medicare: all_wages * 0.029
  - reconciliation_additional: (carol_reconciliation - 200000) * 0.009
  - combined_medicare: regular_medicare + reconciliation_additional
  - reconciled_box_6: regular_medicare / 2 + reconciliation_additional
expected:
  august_ss: 1100
  august_ss_tax: 68.20
  annual_ss: 10918.20
  q3_ss: 26100
  q3_ss_tax: 3236.40
  original_additional: 900
  original_box_6: 5250
  other_seven_wages: 1232700
  reconciled_ss: 174691.20
  reconciled_box_4: 87345.60
  regular_medicare: 52200
  reconciliation_additional: 3305.70
  combined_medicare: 55505.70
  reconciled_box_6: 29405.70
```

```oa-check
name: Historical BeachCo 2025 and original 2024 arithmetic
inputs:
  employees: 12
  futa_base: 7000
  reduction_2025: 0.012
  illustration_2024: 0.009
steps:
  - wages: employees * futa_base
  - gross: wages * 0.06
  - state_credit: wages * 0.054
  - base_tax: gross - state_credit
  - reduction: wages * reduction_2025
  - total_2025: base_tax + reduction
  - each_2025: total_2025 / employees
  - q1_liability: wages / 2 * 0.006
  - old_illustration_reduction: wages * illustration_2024
  - old_illustration_total: base_tax + old_illustration_reduction
  - old_illustration_each: old_illustration_total / employees
expected:
  wages: 84000
  gross: 5040
  state_credit: 4536
  base_tax: 504
  reduction: 1008
  total_2025: 1512
  each_2025: 126
  q1_liability: 252
  old_illustration_reduction: 756
  old_illustration_total: 1260
  old_illustration_each: 105
```

## When to refuse or refer

Each item retains an original boundary topic. For each specialist determination: **Check this point with one of our partner accountants.**

- R-PR-STATE: state/local withholding, SUTA, disability and paid leave use the state workflow above.
- R-PR-AGG: section 3504 agents, PEO/CPEO, aggregate returns and Schedule R.
- R-PR-TERR: territories; do not reuse the obsolete Form 941-SS/944-SS route.
- R-PR-NRA: nonresident aliens, totalization, Forms 1042/8233.
- R-PR-HH: household employment and Schedule H; farmworkers/Form 943, election workers and Form 944 eligibility/conversion have separate conditions, not the ordinary business tests here.
- R-PR-TFRP: collections, Letter 1153, personal liability, penalty relief and appeals.
- R-PR-CLASS: common-law classification, statutory employees/nonemployees, section 530, VCSP/Form 8952 and FLSA economic-realities analysis. Do not infer tax classification from a wage-and-hour result.
- R-PR-NQDC: section 409A and special FICA/FUTA timing for deferred compensation; successor acquisitions, common paymasters and Rev. Proc. 2004-53 W-4/return procedures require separate analysis too.
- R-PR-RAIL: railroad, clergy, church, government and section 218 coverage.
- R-PR-OLDSICK: historical COVID credits and correction limits.
- R-PR-ACA: ACA Forms 1094-C/1095-C, Form 5500 and multi-employer pensions; garnishments are outside this federal tax computation.
- Nonpayroll withholding/Form 945, including pensions, gambling and backup withholding: keep separate from Form 941 deposits and use the applicable instructions.
- Historical 2024 state-credit-reduction lists, including the old Connecticut uncertainty: do not apply another year's list; obtain the applicable final determination.

Unrelated employers generally each apply their own Social Security wage base; an employee's excess-withholding credit does not refund the employer share. The employer's Additional Medicare trigger ignores filing status/other jobs, while the employee reconciles on Form 8959 using the applicable threshold: joint USD 250,000, separate USD 125,000, single/head of household/qualifying surviving spouse USD 200,000, with positive self-employment income combined as applicable. Thus the original single employee with two USD 150,000 jobs and no other adjustments has no employer Additional Medicare withholding but USD 900 liability. A joint employee may have withholding above USD 200,000 despite combined income below USD 250,000 and recover excess through the individual return. [Pub. 15, Social Security/Medicare](https://www.irs.gov/publications/p15); [26 USC 6413(c)](https://uscode.house.gov/us/usc/t26/s6413/); [Form 8959 instructions](https://www.irs.gov/instructions/i8959).

## Filing and payment

| Return | Ordinary 2026 filing date; timely-full-deposit extension where applicable | Source |
| --- | --- | --- |
| Form 941 Q1 / Q2 / Q3 / Q4 | 30 April / 31 July / 2 November 2026 / 1 February 2027; extensions 11 May / 10 August / 10 November 2026 / 10 February 2027 | [941 instructions, When Must You File](https://www.irs.gov/instructions/i941) |
| Form 940 | 1 February 2027; 10 February if all FUTA deposits timely and full | [IRS Topic 759, When to file](https://www.irs.gov/taxtopics/tc759) |
| W-2 employee copies and SSA W-2/W-3 | 1 February 2027 | [2026 W-2 instructions, When to file/furnish](https://www.irs.gov/instructions/iw2w3) |
| FUTA deposits, when accumulated liability exceeds the threshold above | 30 April / 31 July / 2 November 2026 / 1 February 2027 | [Pub. 15, section 14, Table 4](https://www.irs.gov/publications/p15) |

Weekend/holiday rollovers are included. The 2025 Form 940 instructions support continuing procedures, not 2026 state rates or a claimed read of a final 2026 form. Use the applicable-year return when filing.

## Completion checklist

Reconcile employee/year-to-date coverage, plans and deductions; check lookback/next-day classification; compare each liability with its deposit receipt; total Schedule B to line 12; reconcile annual wages/taxes to W-3; check TP/TT/14b and e-filing; document exceptions and referrals before providing filing figures. Retain accepted returns and payment confirmations.

## Sources

These completed reads are reused for the same operative 2026 rules (and expressly labeled 2025 cases). Their applicability was checked on 27 November 2026 against the unchanged period, original Guide and surviving exact-quote ledger. The dates below are the original read dates, not claims of new full reads.

| Official source and portions read | URL | Original read on |
| --- | --- | --- |
| Read for Pub. 15 sections 7, 9 and 11–14 and the section 15 retirement/wage chart: supplemental wages, W-4 administration, deposit periods/reset, electronic methods/cutoffs, exceptions, penalties, reconciliation and FUTA | https://www.irs.gov/publications/p15 | 2026-11-26; business-day passage checked 2026-11-27 |
| Read for Form 941 March 2026 lines 1–16, refund fields 15a–15e, research credit and quarterly filing conditions | https://www.irs.gov/pub/irs-pdf/f941.pdf ; https://www.irs.gov/instructions/i941 | 2026-11-26 |
| Read for W-2/W-3 reporting threshold, boxes 1–7, retirement/HSA, TP/TT/TA, boxes 14a–14b, e-filing/corrections, deadlines and penalties | https://www.irs.gov/instructions/iw2w3 | 2026-11-26; code Y passage checked 2026-11-27 |
| Read for Pub. 15-B cafeteria-plan definition, eligible employees/nondiscrimination, HSA exclusions and S corporation restrictions | https://www.irs.gov/publications/p15b | 2026-11-26 |
| Read for 2026 W-4 steps, Step 3 income/qualification conditions, deductions worksheet and exemption/renewal | https://www.irs.gov/pub/irs-pdf/fw4.pdf | 2026-11-26 |
| Read for final 2026 DOL workbook note and California/Virgin Islands rows, updated 10 November | https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx | 2026-11-26 |
| Read for 2025 Form 940 instructions: annual deadline, multistate credit scope, amended returns and fourth-quarter reduction deposits | https://www.irs.gov/instructions/i940 | 2026-11-26 |
| Read for IRS Topic 759 continuing annual filing date, extension and quarterly deposits | https://www.irs.gov/taxtopics/tc759 | 2026-11-26 |
| Read for Pub. 15-T 2026 table scope, W-4 and withholding methods | https://www.irs.gov/publications/p15t | 2026-11-26 |
| Read for historical 2025 Pub. 15 wage base, Social Security/Medicare, deposit/filing/Calendar and FUTA; Schedule A mechanics and final DOL California reduction | https://www.irs.gov/pub/irs-prior/p15--2025.pdf ; https://www.irs.gov/pub/irs-prior/f940sa--2025.pdf ; https://www.govinfo.gov/content/pkg/FR-2026-01-12/html/2026-00342.htm | 2026-11-26 |
| Reused completed reads for independent-employer wage base, employee excess credit and Form 8959 status/SE aggregation (claims SC-18–20); same operative conditions | https://uscode.house.gov/us/usc/t26/s6413/ ; https://www.irs.gov/instructions/i8959 | 2026-11-26 (reused) |

Not yet confirmed: no usable conclusion is supplied for expressly referred specialist cases, the historical owner-exclusion assumption, incompatible historical reconciliation facts, or final 2026 Form 940 line numbering. **Check this point with one of our partner accountants.** Resolve a referred issue before using its filing output. Redundant historical/permanence commentary, repeated rate/checklist text and broad provenance lists were removed; the material original topics and numeric case inputs remain or have an explicit referral.
