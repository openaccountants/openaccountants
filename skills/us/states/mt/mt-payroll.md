---
name: mt-payroll
description: Compute and report Montana 2026 employee wage withholding and employer unemployment insurance. Covers MW-4, MW-3, TAP, UI eServices, industry new-employer rates and the separate administrative fund tax. Trigger on Montana payroll, MT withholding, UI-5 or Montana UI.
jurisdiction: US-MT
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
version: "1.1"
type: situation-rules
---

# Montana payroll withholding and unemployment insurance, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Montana employers withhold state income tax using the 2026 MW-4 and payroll-period tables, and separately pay UI plus administrative fund tax on each employee's first $47,300 of covered 2026 wages.

## Scope and who this is for

Employers paying wages for services in Montana, including remote work there. This skill owns state wage withholding and UI. Federal FICA, FUTA, deposits and Forms 941/940 remain in `us-form-941-940-payroll`; individual liability is in `mt-income-tax`. Workers compensation, wage/hour law and information-agent mineral royalties are separate jobs.

## Ask the client first

1. Where did each employee physically work, where are they resident, and do reciprocity, reservation, military or short-stay exemptions apply?
2. What does each 2026 MW-4 show for filing status, both-spouses-working, exemptions and extra withholding?
3. What are the payroll frequency, taxable pay and covered wages already paid to each employee this year?
4. What are the Montana UI notice rate/class, industry, new-employer status and any predecessor/successor history?
5. What withholding payment schedule has DOR assigned, what was the lookback withholding, and are TAP and UI eServices accounts active?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| UI annual wage base, each employee | $47,300 | [official text](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf) |
| 2026 Schedule I UI rate, before AFT | 0.00% to 6.12%; use assigned notice | [official text](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf) |
| New employers: agriculture/forestry/hunting/fishing and mining | 1.30% UI plus 0.18% AFT | [official text](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf) |
| New employers: construction and unclassified | 2.00% UI plus 0.18% AFT | [official text](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf) |
| New employers: manufacturing; utilities/transport/warehousing; wholesale; retail; finance/insurance/real estate | 1.00% UI plus 0.18% AFT | [official text](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf) |
| New employers: services | 1.10% UI plus 0.18% AFT | [official text](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf) |
| Eligible UI classes 01 and 02 AFT | 0.13%; all other classes 0.18% | [official text](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf) |
| Monthly MW-4 single/MFS or both-spouses-working table, gross taxable earnings G below $1,342 | $0 | [2026 tables, printed p.17](https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf) |
| Same monthly table, $1,342 <= G < $5,300 | 4.7% x (G - $1,342) | [official text](https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf) |
| Same monthly table, G >= $5,300 | $187 + 5.65% x (G - $5,300) | [official text](https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf) |
| Separate supplemental wages, optional flat method | 5%; aggregation also permitted | [printed p.3](https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf) |
| Withholding lookback: up to $1,199 / $1,200 to $11,999 / at least $12,000 | Annual / monthly / accelerated; new accounts monthly | [official text](https://revenue.mt.gov/taxes/withholding-tax/wage-withholding-returns-and-payments) |

### Register and classify

Register the withholding account in [TAP](https://tap.dor.mt.gov) using FEIN, legal name, mailing details and first Montana work date, or Form GenReg. Register a new UI account through [UI eServices](https://uieservices.mt.gov); the old downloadable UI-1 is no longer offered. Create and verify Okta credentials, then connect them to the UI employer profile. Sources: [official text](https://revenue.mt.gov/taxes/withholding-tax/accounts), [official text](https://uid.dli.mt.gov/forms), [2026 e-filing handbook pp.4-5](https://uid.dli.mt.gov/_docs/eServices/efiling-handbook.pdf).

### Each payroll

Get Form MW-4; a federal W-4 does not replace it. Use the table for the actual payroll frequency and MW-4 status, including the both-spouses-working box. The monthly single schedule above is one executable branch, not a replacement for the other status/frequency tables in [2026 employer instructions pp.10-19](https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf). Compute W = A + B x (G - C); printed p.16 directs rounding **up** to whole dollars. Add requested extra withholding. The source examples sometimes say nearest dollar, but the general formula instruction explicitly says up: use that instruction and reconcile payroll software differences before filing.

For UI, current taxable wages per employee = min(current covered wages, max(47,300 - prior-year-to-date covered wages, 0)). Multiply their sum by the assigned UI rate and separately by the assigned AFT rate. A 0% UI class still has AFT. The new-employer rates above are industry-specific; a negative-reserve employer may be rated as deficit regardless of years in business. Source: [2026 rate explanation pp.1-2](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf).

### Reporting workflow

In UI eServices, choose the account, then **Manage Reports** or **File Now** and the quarter. Answer **Did you pay wages?** A zero-wage quarter still needs a report. Enter worker counts for the pay period containing the 12th of each month, then full SSN, name and total quarterly gross wages for each employee, or import a correctly formatted file. Reconcile gross, excess and taxable totals and both tax components. Click **Next**, then **Submit**; saving a draft is not filing. Retain the confirmation and separately complete payment. Source: [pp.6-10 and payment section pp.17-20](https://uid.dli.mt.gov/_docs/eServices/efiling-handbook.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| North Dakota resident with Montana wages | Reciprocity can exempt the wages; get MW-4 exemption and submit through TAP. |
| Tribal member resident and working on own tribe's reservation | Exemption depends on both residence and work source; split mixed wages. |
| Agricultural labor | Withholding exemption does not itself establish UI exemption. Cannabis employees are not agricultural laborers for withholding. |
| Nonresident working in multiple states, at most 30 Montana days | Special withholding relief has exclusions for construction, athletes, entertainers, certain high earners, event and production workers; apply the full printed p.3 conditions before exempting. |
| Withholding-exempt employee | Submit exempt MW-4 through TAP by the last day of that payroll period; annual renewal by January 31. |
| Owner, contractor, successor or multistate UI worker | Determine coverage/localization separately before applying an employee rate. |

Withholding exceptions and their definitions: [printed pp.2-3 and 6](https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf). UI classification and rate rules: [official text](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf).

## Worked cases

**Case 1.** A single employee with MW-4 line 1a earns $4,000 monthly, with no extra withholding. The printed monthly formula gives ($4,000 - $1,342) x 4.7% = $124.926, rounded up to **$125**. A new services employer pays that employee $48,000 during 2026: UI is $47,300 x 1.10% = $520.30 and AFT $85.14, total $605.44.

```oa-check
name: MT monthly withholding and new service employer 2026
inputs:
  monthly_pay: 4000
  annual_wages: 48000
steps:
- withheld: ceil(max(monthly_pay - 1342, 0) * 0.047)
- ui_base: min(annual_wages, 47300)
- ui: ui_base * 0.011
- aft: ui_base * 0.0018
- employer_total: ui + aft
expected:
  withheld: 125
  ui: 520.3
  aft: 85.14
  employer_total: 605.44
```

**Case 2, a cap decision.** For a new construction employer paying $5,000 this quarter, an employee previously paid $46,000 has $1,300 of taxable wages left: UI plus AFT is $28.34. If previously paid $40,000 instead, all $5,000 remains taxable, costing $109.00. Report the full $5,000 in either branch and let excess wages explain the difference.

```oa-check
name: MT wage cap before and after 2026
inputs:
  quarter_wages: 5000
  prior_high: 46000
  prior_low: 40000
steps:
- taxable_high: min(quarter_wages, max(47300 - prior_high, 0))
- taxable_low: min(quarter_wages, max(47300 - prior_low, 0))
- tax_high: taxable_high * (0.02 + 0.0018)
- tax_low: taxable_low * (0.02 + 0.0018)
expected:
  taxable_high: 1300
  taxable_low: 5000
  tax_high: 28.34
  tax_low: 109
```


## When to refuse or refer

Refer disputed worker status, UI localization, successor transfers, public/nonprofit reimbursing employers, reservation disputes, and an unresolved rate notice. Do not choose a voluntary contribution or exemption without the controlling facts.

## Filing and payment

Withholding: annual schedule pays January 31; monthly pays the following month's 15th; accelerated follows the stated payday schedule (Saturday-Tuesday payroll by following Friday, Wednesday-Friday by following Wednesday). File MW-3 and all Montana W-2s, even those without withholding, plus 1099s with Montana withholding by January 31. DOR moves weekend deadlines to the next business day: 2026 year-end forms are due February 1, 2027. In TAP choose the withholding account, period and reconciliation; reconcile payroll withholding, payments and attached wage forms, submit and retain confirmation. Do not send truncated taxpayer IDs. Amend MW-3 and the affected wage statements if needed. Closure requires final forms within 30 days of cessation. Sources: [official text](https://revenue.mt.gov/taxes/withholding-tax/wage-withholding-returns-and-payments), [official text](https://revenue.mt.gov/taxes/withholding-tax/accounts).

UI: electronic quarterly reports and payment are due the last day of the next month, with next-business-day relief: April 30, July 31, November 2, 2026 and February 1, 2027. Sources: [p.4](https://uid.dli.mt.gov/_docs/eServices/efiling-handbook.pdf). Withholding late payment is 1.5% per month, maximum 15%; 2026 non-individual-tax interest is 10.25% annually, computed daily. The employer instructions specify $50 per missing W-2 (minimum $250), with the stated notice-and-cure rules. UI delinquency can produce a 50% rate increase; the 2026 rate explanation gives January 16, 2026 as the cure cutoff for that year's notice. Sources: [official text](https://revenue.mt.gov/taxes/penalty-and-interest), [printed p.6](https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf), [official text](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf).

## Completion checklist

- Keep separate employee withholding, employer UI, AFT and federal accounts.
- Reconcile wage detail, cap history, rate notice and reporting period.
- Submit returns and payments; retain both confirmations.
- Reconcile MW-3 to W-2s and all deposits.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Montana employer instructions, effective 2026. Read for printed pp.1-8, 16-19: exemptions, formulas, supplemental wages, filing, penalties and rounding. | https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf | 2026-11-13 |
| Montana UI 2026 rate explanation. Read for both pages: wage base, Schedule I, industry rates, AFT and delinquency rate. | https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf | 2026-11-13 |
| Montana UI e-filing handbook, updated September 2026. Read for pp.4-10 and 17-20: deadlines, enrollment, wage entry, submission and payments. | https://uid.dli.mt.gov/_docs/eServices/efiling-handbook.pdf | 2026-11-13 |
| DOR withholding payments and returns. Read for lookback schedule, annual reconciliation and taxpayer ID requirements. | https://revenue.mt.gov/taxes/withholding-tax/wage-withholding-returns-and-payments | 2026-11-13 |
| DOR withholding account registration. Read for registration data and final return after cessation. | https://revenue.mt.gov/taxes/withholding-tax/accounts | 2026-11-13 |
| DLI printable forms. Read for UI-1 replacement by online new-employer registration. | https://uid.dli.mt.gov/forms | 2026-11-13 |
| DOR penalties and interest. Read for 2026 non-individual tax interest and withholding late payment penalty. | https://revenue.mt.gov/taxes/penalty-and-interest | 2026-11-13 |

Not yet confirmed: UI monetary late-report/late-payment penalty calculations and coverage thresholds for domestic, farm, nonprofit and public employers are not confirmed here. The UI rate notice is needed for each employer; this skill does not compute experience-rating assignments.

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.
