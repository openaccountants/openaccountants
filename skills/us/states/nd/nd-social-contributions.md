---
name: nd-social-contributions
description: >-
  Use when an employer needs the North Dakota answer (2025 figures) on state-level
  social contributions: North Dakota has no employee-side social
  contribution, no state disability insurance and no paid-family-leave
  payroll tax -- the only state-level social contribution is the
  employer-only unemployment insurance tax administered by Job Service ND
  under N.D.C.C. Ch. 52-8 (quarterly Form SFN 41263 via UI EASY, new
  employer rates 1.02% non-construction / 6.09% construction on the
  2025 $45,100 taxable wage base). Trigger on North Dakota UI tax, ND
  SUTA, new employer rate, Job Service ND, SFN 41263, UI EASY.
  Source-cited draft; 2026 wage base and rates need confirmation.
jurisdiction: US-ND
type: decision
category: payroll
tax_year: 2025
tax_year_notes: Covers the 2025-2026 period using the 2025 unemployment wage base and rates; the 2026 wage base and rate schedule were not confirmed on 2026-11-13 (Job Service North Dakota pages returned 403 to an automated read).
tier: 2
verified_by: pending
last_updated: 2026-11-13
version: 0.4
---

# North Dakota social contributions (employer-only UI; no employee-side levy)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

Every employer liable for North Dakota unemployment insurance: any person or entity paying wages in North Dakota that meets the coverage tests of N.D.C.C. Ch. 52-8 (Employment Security). North Dakota is an **employer-only** state for social contributions -- there is no state-level employee payroll contribution of any kind. Reimbursement-base governmental and certain nonprofit employers elect reimbursement instead of contribution financing (Job Service ND employer's guide).

### 2. Core rules and rates

- **No employee-side social contribution.** No state disability insurance (contrast NY), no paid-family-leave payroll tax (contrast NY, WA), no state retirement contribution. FICA/FUTA are federal and outside this skill. _(N.D.C.C. Ch. 52-8; corroborated by absence of any employee payroll levy in the ND Tax Commissioner materials, read 2026-10-25)_
- **UI taxable wage base.** The base "is determined yearly and equals 70% of the calculated statewide average annual payroll" -- Job Service ND, "Determination of Taxable Wage Base," verified 2026-10-25 (US-ND-dr-jsnd-learn-about-taxes.txt). The **2025 base is $45,100** (US-ND-dr-jsnd-uitaxrates2025.pdf: "2025 Taxable Wage Base is $45,100"); the **2026 base is $46,600** (US-ND-dr-jsnd-uitaxrates2026.pdf: "2026 Taxable Wage Base is $46,600").
- **New employer rates.** Per the JSND rate schedules: 2025 -- non-construction **1.03%** (positive balance) / **6.09%** (negative balance), construction **9.69%** (US-ND-dr-jsnd-uitaxrates2025.pdf); 2026 -- non-construction **1.00%** / **6.07%**, construction **9.67%** (US-ND-dr-jsnd-uitaxrates2026.pdf). _(jobsnd.com "Learn About Taxes" confirms new-employer classification mechanics, verified 2026-10-25)_
- **Experience rating.** Rates are re-determined each calendar year based on the employer's history as of the preceding June 30; an employer remains a "new employer" until liable for the period ending the prior June 30 (typically 3 full fiscal years). _(jobsnd.com/unemployment-business-tax/learn-about-taxes, verified 2026-10-25)_
- **Rate range for experience-rated employers:** 2025 schedules run **0.08% (positive-balance minimum) to 9.69% (negative-balance maximum)** (US-ND-dr-jsnd-uitaxrates2025.pdf rate tables). Statutory floor: "The positive employer minimum rate in the first rate schedule of the table of rate schedules is one-hundredth of one percent" (US-ND-dr-nd-t52c04.pdf, § 52-04-05(5)(b)).

### 3. Base and adjustments

- Base: each employee's wages up to the calendar-year taxable wage base. Wages follow the Ch. 52-8 definition (remuneration for personal services; exclusions per statute).
- Contributions are computed per employee: taxable wages × assigned rate. No employee withholding, no employee W-2 Box 14 state social line (contrast NY PFL/SDI).
- Voluntary contribution account (VCA) and reimbursement options exist for eligible employers (US-ND-jsnd4036.pdf, "VOLUNTARY CONTRIBUTIONS": "Employers may make voluntary contributions to their Unemployment Insurance" accounts; reimbursement option per US-ND-dr-jsnd-learn-about-taxes.txt).

### 4. Deadlines

- **Quarterly Form SFN 41263** (Employer's Contribution and Wage Report): due the **last day of the month following the calendar quarter** (Apr 30, Jul 31, Oct 31, Jan 31). Mandatory electronic filing via **UI EASY** for all employers. _(existing `nd-payroll` skill, corroborated by jobsnd.com "File Reports" hub, verified 2026-10-25)_
- Annual rate notices issue in November/December for the following calendar year (existing `nd-payroll` skill; protest window per notice).
- New-employer liability begins with the first quarter in which the coverage test is met; register via Job Service ND.

### 5. Penalties and interest

- Late quarterly reports/contributions: "Contributions unpaid when due must bear interest at the rate of one and one-half percent per month or fraction thereof from due date"; failure to file a contribution and wage report carries "a penalty equal to five percent of the contributions due for each month or part of a month," first-month minimum $25 (subsequent reports $100), capped at 20% of contributions and $500 per report (US-ND-dr-nd-t52c04.pdf, § 52-04-11).
- Fraudulent reporting and misclassification (employee vs independent contractor) carry separate Ch. 52-8 sanctions; construction project risk protection rules apply to contractors (jobsnd.com "Comply with Construction Project Risk Protection," verified 2026-10-25).

### 6. Cross-border and federal overlay

- Multi-state employers: ND UI applies to services performed in ND; reciprocal-state wage rules do not affect UI (UI follows the work-location/coverage tests, not income-tax reciprocity).
- Federal FUTA credit reduction interacts with the state UI system; ND's credit-reduction status each year: check the DOL list (federal skill).
- No state PFL/SDI means no interaction with the federal FMLA beyond unpaid-leave protection.

### 7. Worked examples

**Example 1 -- two new non-construction employees, 2025 base.** New employer (non-construction), rate 1.02%, 2025 taxable wage base $45,100, two employees each earning over the base.

```oa-check
name: nd ui new employer two employees
inputs:
  base: 45100
  employees: 2
  rate: 0.0102
steps:
  - tax: base * employees * rate
expected:
  tax: 920.04
```

**Example 2 -- new construction employer.** Same base, construction new-employer rate 6.09%, one employee over the base.

```oa-check
name: nd ui new construction employer
inputs:
  base: 45100
  rate: 0.0609
steps:
  - tax: base * rate
expected:
  tax: 2746.59
```

(2026 figures will differ once Job Service ND publishes the 2026 base and schedules -- recompute before relying.)

### 8. Ask the client first

1. Is the employer construction or non-construction? (Different new-employer rate and project risk-protection rules.)
2. Are workers correctly classified as employees for Ch. 52-8? (Misclassification is the top ND UI audit issue.)
3. Reimbursement or contribution financing -- which election is on file?
4. Multi-state: are ND wages being reported to another state's UI system by mistake?
5. Has the 2026 rate notice been reviewed and, if wrong, protested within the notice window?

### 9. Sources

- Job Service ND -- Learn About Taxes (taxable wage base formula, new-employer and experience-rating mechanics): <https://www.jobsnd.com/unemployment-business-tax/learn-about-taxes> -- 200 with text, 2026-10-25.
- Job Service ND -- site root and unemployment-business-tax hub (file reports, employer's guide, construction risk protection): <https://www.jobsnd.com/> -- 200, 2026-10-25.
- Existing `nd-payroll` skill (2025 wage base $45,100; SFN 41263 mechanics; new-employer rates) -- read 2026-10-25; the 2025 base and rates are now archived as US-ND-dr-jsnd-uitaxrates2025.pdf.
- N.D.C.C. Ch. 52-04 (rate determination; penalties and interest): archived as US-ND-dr-nd-t52c04.pdf. Full Ch. 52-8 text: see the "Not yet confirmed:" paragraph below -- ndlegis.nd.gov DNS failure on 2026-10-25.
- 2026 ND UI taxable wage base and rate schedules: archived as US-ND-dr-jsnd-uitaxrates2026.pdf ($46,600 base; new-employer and experience-rate tables).

<!-- openaccountants-cta-block -->

---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at the OpenAccountants network.

- Use it in your AI: 
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min

## Who this applies to

No figures stated in this section.

## Rates, bands and thresholds

No figures stated in this section.

## The taxable base

No figures stated in this section.

## Deadlines and filing

No figures stated in this section.

## Penalties and interest

No figures stated in this section.

## Cross-border points

No figures stated in this section.

## Worked examples

No figures stated in this section.

## Ask the client first

No figures stated in this section.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| US-ND-dr-nd-booklet2024.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2024-iit/2024-individual-income-tax-booklet.pdf | 2026-10-28 |
| US-ND-dr-nd-withholding-2025.pdf | https://www.tax.nd.gov/sites/www/files/documents/misc-discuss-folder/Final_2025%20Income%20Tax%20Withholding%20Rates%20%20Instructions.pdf | 2026-10-28 |
| US-ND-dr-ndwr.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf | 2026-10-28 |
| US-ND-dr-nd-walsh-county-notice-2026.pdf | https://www.tax.nd.gov/sites/www/files/documents/forms/business/sales-use/local-jurisdiction-rates/2026-jurisdiction/notice-to-walsh-county-permit-holders.pdf | 2026-10-28 |
| US-ND-dr-t57c51-1.pdf | https://ndlegis.gov/cencode/t57c51-1.pdf | 2026-10-28 |
| US-ND-dr-usc26-1.txt | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1&num=0&edition=prelim | 2026-10-28 |
| US-ND-dr-ndcc-57-39-2.pdf | https://ndlegis.gov/cencode/t57c39-2.pdf | 2026-10-28 |
| US-ND-tap.html | https://tap.tax.nd.gov/?Check=1 | 2026-10-28 |

Not yet confirmed: figures in this skill lack archived line-citations.
- Full N.D.C.C. Ch. 52-8 employer-financing text beyond Ch. 52-04 (archived as US-ND-dr-nd-t52c04.pdf) remains unarchived.
- Historical 2023 UI rate range 0.08%--9.97% appears in US-ND-dr-nd-ui-databook.pdf but predates the archived 2024--2026 schedules.


| Source | URL | Read on |
| --- | --- | --- |
| (see "Not yet confirmed:" paragraph) | -- | 2026-10-28 |

No figures stated in this section.

## Talk to a verified accountant

No figures stated in this section.
