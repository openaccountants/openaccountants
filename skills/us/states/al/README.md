---
jurisdiction: US-AL
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  SC: al-unemployment-contributions
  PR: al-payroll-withholding
---

# Alabama (US-AL) pack

Jurisdiction: Alabama, United States. Tax year 2026. Pack drafted 2026-10-27, corrected 2026-10-28 to tie every retained figure to an archived primary source (tier 2).

Alabama taxes corporations at a flat 6.5% of net income with a deduction for federal income
tax paid, on single-sales-factor apportionment for tax years beginning on or after 2021-01-01.
The same Department of Revenue administers withholding (A-1/A-6/A-3 bulk filing) and the sales tax;
unemployment contributions run through the Department of Labor (adol.alabama.gov). There is
no standalone transfer-pricing statute: related-party economics are policed through combined
reporting and the single-sales-factor apportionment. Individuals pay a graduated income tax
(see `al-income-tax`).

## applicable

- `IT-IND` -- individual income tax -- present: `al-income-tax.md`, `alabama-income-tax.md`
- `IT-CORP` -- corporate income tax (6.5%, federal-tax deduction) -- present: `al-corporate-income-tax.md`
- `VAT` -- sales & use tax -- present: `al-sales-tax.md`, `alabama-sales-tax.md`
- `SC` -- social contributions (employer UI contributions, Dept. of Labor) -- present: `al-unemployment-contributions.md`
- `PR` -- payroll withholding (A-1/A-6/A-3, bulk filing) -- present: `al-payroll-withholding.md`
- `TP` -- transfer pricing / combined reporting / unitary group -- present: `al-transfer-pricing.md`
- `XB` -- cross-border / nexus / non-resident corporations -- present: `al-cross-border.md`

## not_applicable

- none -- Alabama has income, corporate, sales, payroll, and social-contribution regimes; all
  pilot domains apply.

## Source status

All figures retained in the pack's skills are tied to archived primary sources (raw copies +
sidecar JSON in the evidence pack sources/ directory), read 2026-10-27/28:

- ALDOR Corporate Income Tax page (revenue.alabama.gov, 200): 6.5% rate, federal-income-tax
  deduction, single sales factor from TYB 2021-01-01, statutory authority §§40-18-1 to 40-18-59
  and 40-18-160 to 40-18-176, franchise-tax authority §§40-27-1 to 40-27-6, Amendment 662 rate
  history.
- ALDOR Individual Income Tax page (200): rate schedules, Amendments 25/61/225, minimum
  exemptions, filing AGI thresholds.
- ALDOR individual income tax rate FAQ (200): 2%/4%/5% brackets by filing status.
- 2025 Form 40 booklet PDF, 25f40bk (200, text layer extracted): filing thresholds, personal and
  dependent exemptions, standard-deduction charts, deadlines, automatic extension, penalties,
  estimated tax, ABLE deduction, criminal liability.
- ALDOR Sales Tax authority page (200): 4% general rate, 2% food, 1.5% manufacturing/farm
  machinery, 2% automotive, 3% vending food, local rates .10%–5%, self-administration split.
- ALDOR Sales and Use Tax Incentives page (200): rate differentials and Code-section-cited
  exemptions.
- ALDOR food-rate reduction notice, Act 2023-554 (200): 4%→3% (Sep 1, 2023) →2% (Sep 1, 2024),
  SNAP food definition, local food rates.
- ALDOR remote-seller FAQ (200): $250,000 economic-nexus threshold, collection from
  October 1, 2018, threshold computation.
- ALDOR Withholding Bulk Filing page (200): bulk-filer registration (Form BF-1), A-1/A-6 and
  A-3 layouts, the 2024-01-27 A-1/A-6 layout change with overtime-exemption fields.
- ADOL Unemployment Compensation Division page (200): division and employer services.

Not yet confirmed (carried on each skill's Not yet confirmed line, not in skill bodies):
franchise-tax rates and form due dates (form PDFs 404'd this run); UI wage base and 2026
experience-rate range (not extractable from the ADOL pages); Code of Alabama section text
(legislative mirror not retrievable from this host).

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | al-income-tax, alabama-income-tax | figures tied to archived sources |
| IT-CORP, corporate income tax | al-corporate-income-tax | figures tied to archived sources |
| VAT / GST / sales tax | al-sales-tax, alabama-sales-tax | figures tied to archived sources |
| SC, social contributions | al-unemployment-contributions | administration confirmed; all UI figures unconfirmed |
| PR, payroll withholding | al-payroll-withholding | bulk-filing mechanics confirmed; form dates unconfirmed |
| TP, transfer pricing | al-transfer-pricing | apportionment confirmed; §40-18-50 text unconfirmed |
| XB, cross-border | al-cross-border | confirmed where archived |

## Official sources

- ALDOR Corporate Income Tax: https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ (read 2026-10-27)
- ALDOR Individual Income Tax: https://revenue.alabama.gov/taxes-fees/individual-income-tax/ (read 2026-10-28)
- ALDOR individual income tax rate FAQ: https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/ (read 2026-10-28)
- 2025 Form 40 booklet (25f40bk): https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf (read 2026-10-28)
- ALDOR Sales Tax: https://www.revenue.alabama.gov/tax-types/sales-tax/ (read 2026-10-28)
- ALDOR Sales and Use Tax Incentives: https://revenue.alabama.gov/taxes-fees/sales-use-tax/ (read 2026-10-28)
- ALDOR food-rate notice (Act 2023-554): https://www.revenue.alabama.gov/notice-state-sales-and-use-tax-rate-reduced-on-food-beginning-september-1-2023/ (read 2026-10-28)
- ALDOR remote-seller FAQ: https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/ (read 2026-10-28)
- ALDOR Withholding Bulk Filing: https://revenue.alabama.gov/taxes-fees/withholding/ (read 2026-10-27)
- Alabama Department of Labor, UC Division: https://adol.alabama.gov/divisions/unemployment-compensation/ (read 2026-10-28)
