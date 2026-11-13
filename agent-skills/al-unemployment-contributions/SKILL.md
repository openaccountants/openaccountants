---
name: al-unemployment-contributions
description: "Use this skill whenever asked about Alabama employer unemployment compensation (UC) tax for tax year 2026: the $8,000 taxable wage base, the 2.70% new-employer rate, the 0.20% to 6.80% experience-rated range, the quarterly Contribution and Wage Report and its due dates, and the late-report penalty, administered by the Alabama Department of Labor (adol.alabama.gov). Trigger on \"Alabama UI rate\", \"Alabama SUTA\", \"Alabama unemployment wage base\", \"Alabama UC tax\", \"Alabama employer taxes\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/al-unemployment-contributions"
  jurisdiction: "US-AL"
  tax_year: "2026"
  last_updated: "2026-11-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Alabama unemployment compensation (UC) tax

> **Source-cited draft.** Built from the Alabama Department of Labor (ADOL) Unemployment Compensation Division page and ADOL employer FAQs, read 2026-11-13. No accountant has reviewed it.

## Who this applies to

- Employers covered under Alabama's unemployment compensation law (Ala. Code Title 25), administered by the Alabama Department of Labor (ADOL) Unemployment Compensation Division (ADOL UC Division page). The statutory coverage tests are on the Not yet confirmed line.
- New employers pay the assigned new-account rate until they qualify for experience rating; established employers pay a rate based on their own benefit charges and taxable payroll, modified by the statewide schedule and shared cost (ADOL FAQs).

## Rates, bands and thresholds

| Item | 2026 amount | Source |
|---|---|---|
| Taxable wage base | First $8,000 paid by the employer to each worker in the calendar year | [ADOL FAQ: What is the taxable wage base?](https://adol.alabama.gov/faq/what-is-the-taxable-wage-base/) |
| New-employer rate | 2.70% on the first $8,000 of wages for each employee | [ADOL FAQ: What is the new account rate?](https://adol.alabama.gov/faq/what-is-the-new-account-rate/) |
| Experience-rated range | 0.20% to 6.80%, inclusive of the 0.06% Employment Security Enhancement Assessment (ESA), depending on which of four rate schedules is in effect, plus any shared cost | [ADOL FAQ: experience rating](https://adol.alabama.gov/faq/may-an-employer-earn-a-tax-rate-based-upon-its-record-of-unemployment-experience/) |
| Employment Security Enhancement Assessment | 0.06%, carved out of the schedule rate (all rates except 5.40% are reduced by 0.06% ESA) | [ADOL FAQ: how the annual rate is calculated](https://adol.alabama.gov/faq/how-is-my-annual-tax-rate-calculated-if-the-rate-is-based-on-experience/) |
| Late report penalty | $25 or 10% of taxes owed, whichever is greater (quarters from 1996) | [ADOL FAQ: penalty for late reports](https://adol.alabama.gov/faq/what-is-the-penalty-rate-for-late-reports/) |

## The taxable base

- The wage base is per employee per calendar year: tax stops once an employee's wages from the employer pass $8,000 (ADOL FAQ).
- Experience rating uses the three most recent complete fiscal years (July 1 to June 30) of benefit charges and taxable payroll; the benefit ratio (charges divided by taxable payroll) is read against the Tax Rate Table in §25-4-54(f) under the schedule (A to D) set each year from the trust fund balance, and shared cost is added (ADOL FAQ).
- A successor that acquires a liable employer's business takes over the predecessor's experience (ADOL FAQ).

## Deadlines and filing

- Quarterly Contribution and Wage Reports are due the last day of the month following the quarter: January 31, April 30, July 31 and October 31 (ADOL FAQ).
- The annual Tax Rate Notice (Form UC-216) is downloaded through ADOL's eGov service; employers on the 2.70% initial rate get a notice once an individual rate is set (ADOL FAQ).

## Penalties and interest

- Late Contribution and Wage Reports: $25 or 10% of the taxes owed, whichever is greater (ADOL FAQ). Interest provisions are on the Not yet confirmed line.
- Common failure modes: (1) computing tax on total wages instead of the first $8,000 per employee; (2) a new employer budgeting below 2.70% before its first rate notice; (3) ignoring shared cost when checking the rate notice.

## Cross-border points

- Multi-state employers register in Alabama for employees whose work is localised in Alabama; the wage base applies per employee per state (localisation rules on the Not yet confirmed line).

## Worked examples

Client facts in these examples are hypothetical. Only figures from the table above are used.

**Example 1: new employer, one employee earning $30,000**

Only the first $8,000 is taxable, at the 2.70% new-account rate:

```oa-check
name: AL UC tax, new employer, one employee
inputs:
  annual_wages: 30000
  wage_base: 8000
  new_employer_rate: 0.027
steps:
  - taxable_wages: min(annual_wages, wage_base)
  - uc_tax: taxable_wages * new_employer_rate
expected:
  taxable_wages: 8000.00
  uc_tax: 216.00
```

**Example 2: late quarterly report**

A Contribution and Wage Report showing $180 of tax is filed late. The penalty is the greater of $25 or 10% of the tax owed:

```oa-check
name: AL UC late report penalty
inputs:
  tax_owed: 180
steps:
  - penalty: max(25, tax_owed * 0.10)
expected:
  penalty: 25.00
```

## Ask the client first

- Is the business newly liable (2.70%) or does it have an ADOL Tax Rate Notice for 2026? What rate, schedule and shared cost does the notice show?
- Are wages capped at $8,000 per employee per year in the payroll system?
- Were all four quarterly Contribution and Wage Reports filed by the last day of the following month?
- Did the business acquire another employer's operations (predecessor experience transfers)?

## Sources

| # | Source | URL | Read on |
|---|---|---|---|
| 1 | ADOL Unemployment Compensation Division page, read for the page as a whole | https://adol.alabama.gov/divisions/unemployment-compensation/ | 2026-11-13 |
| 2 | ADOL FAQ: What is the taxable wage base?, read for $8,000 | https://adol.alabama.gov/faq/what-is-the-taxable-wage-base/ | 2026-11-13 |
| 3 | ADOL FAQ: What is the new account rate?, read for 2.70% | https://adol.alabama.gov/faq/what-is-the-new-account-rate/ | 2026-11-13 |
| 4 | ADOL FAQ: May an employer earn a tax rate based upon its record of unemployment experience?, read for 0.20% to 6.80% incl. 0.06% ESA | https://adol.alabama.gov/faq/may-an-employer-earn-a-tax-rate-based-upon-its-record-of-unemployment-experience/ | 2026-11-13 |
| 5 | ADOL FAQ: How is my annual tax rate calculated?, read for three fiscal years, schedules A to D, shared cost, ESA | https://adol.alabama.gov/faq/how-is-my-annual-tax-rate-calculated-if-the-rate-is-based-on-experience/ | 2026-11-13 |
| 6 | ADOL FAQ: When is the last day I can file my Quarterly Contribution and Wage Report?, read for the page as a whole | https://adol.alabama.gov/faq/when-is-the-last-day-i-can-file-my-quarterly-contribution-and-wage-report-and-not-be-late/ | 2026-11-13 |
| 7 | ADOL FAQ: What is the penalty rate for late reports?, read for the page as a whole | https://adol.alabama.gov/faq/what-is-the-penalty-rate-for-late-reports/ | 2026-11-13 |
| 8 | ADOL FAQ: How do I get my new tax rate notice?, read for the page as a whole | https://adol.alabama.gov/faq/how-do-i-get-my-new-tax-rate-notice/ | 2026-11-13 |

Not yet confirmed: the rate schedule (A to D) and shared cost in force for 2026; whether employees contribute anything (an earlier draft said the tax is employer-only, without a source); the coverage tests in Title 25; the interest rate on late UC tax; the FUTA credit-reduction status for Alabama; the localisation rules for multi-state employees; the quarterly report form number (an earlier draft carried "Form A-4", which is in fact ALDOR's employee withholding certificate); the workers' compensation employee threshold; whether Alabama has any state disability or paid-leave payroll contribution (an earlier draft asserted none).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `al-unemployment-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/al-unemployment-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
