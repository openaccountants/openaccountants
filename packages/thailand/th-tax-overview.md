---
name: th-tax-overview
description: "Thailand 2026 tax overview: taxpayer and period identification, domestic residence and income-source tests, PIT/CIT/VAT/payroll filing routes, foreign-income tracing and handoff to the separate top-up-tax method."
jurisdiction: TH
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
category: international
version: 1.0
---

# Thailand tax overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

**2026 answer layer:** identify the person, income source, period and tax before choosing a computation. Thailand uses THB and the Revenue Department administers the Revenue Code. Individuals use a calendar tax year; an ordinary company's accounting period normally spans 12 months with statutory exceptions. A transfer into a Thai bank account is neither automatically taxable income nor proof of an exemption.

## Rates, bands and thresholds

| Question | Answer and required conditions | Official source and method home |
|---|---|---|
| Individual period | Calendar year; establish when the income was earned and received | [Revenue Code §39](https://www.rd.go.th/5937.html); [PIT](thailand-pit.md) |
| Individual residence | Presence aggregating at least 180 days in the tax year; treaty residence is a separate test | [Revenue Code §41](https://www.rd.go.th/5937.html); [PIT](thailand-pit.md) |
| Ordinary individual tax | Progressive rates reach 35%, with a first-slice exemption and allowance conditions; do not apply the top rate to all income | [Income Tax Schedule](https://www.rd.go.th/5938.html); [PIT bands and base](thailand-pit.md) |
| Company period and ordinary rate | Normally 12 months; 20% of ordinary taxable net profit; qualifying SME and special regimes differ | [Revenue Code §§65-67](https://www.rd.go.th/english/37764.html) and [Income Tax Schedule](https://www.rd.go.th/5938.html); [CIT](th-corporate-income-tax.md) |
| VAT exists | Current ordinary combined rate is 7%; taxable, exempt and zero-rated supplies must be separated, and the reduction is period-bound | [Revenue Department VAT §4](https://www.rd.go.th/english/6043.html) and [Royal Decree 807](https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/dc807.pdf); [VAT](thailand-vat.md) |
| Annual individual filing | Statutory last day of March following the year; electronic extensions need the actual filing-year notice | [Revenue Code §§56 and 57 quater](https://www.rd.go.th/5937.html); [PIT filing](thailand-pit.md) |
| Annual company filing | Within 150 days after the accounting-period end, independently of accounts approval | [Revenue Code §§68-69](https://www.rd.go.th/english/37764.html); [CIT filing](th-corporate-income-tax.md) |

## The base

1. **Identify the taxpayer.** For an individual, distinguish residence, domestic-source income and foreign-source income. For a company, distinguish Thai incorporation, a foreign company's Thai business and non-resident income subject to gross withholding. Legal form and activity determine the route, not the bank description.
2. **Identify the period and evidence.** Match income, deductions and credits to the relevant tax year or company period; retain the original BE/CE dates. Reconcile bank movements with contracts, invoices, payslips, asset records and withholding certificates. Transfers, loans, capital contributions and gifts need their own facts.
3. **Compute in the substantive home.** Use [PIT](thailand-pit.md) for the progressive base, deductions and personal filing; [CIT](th-corporate-income-tax.md) for tax-adjusted profit; [VAT](thailand-vat.md) for transactions and input-credit conditions; [payroll](th-payroll-social.md) for employer withholding and social security; [formation](th-company-formation.md) for entity/registration decisions. The [references catalogue](references.md) offers software leads, not law.
4. **Keep top-up tax separate.** The existing [top-up tax skill](th-top-up-tax.md) handles the large-MNE group test, period and notification/GIR/return workflow. The old overview's approximate 15% headline is not a substitute for a GloBE computation or proof every Thai company is in scope. This overview does not create a new verification of the unchanged sibling.

## Deadlines and filing

Select the form and actual period through the [Revenue Department filing-service index](https://www.rd.go.th/rdeservice/63813.html). Individuals distinguish salary-only PND.91, broader PND.90 and applicable half-year PND.94; companies distinguish PND.50, PND.51 and foreign-payee PND.54; monthly VAT uses PP.30 and applicable imported-service payments use PP.36. Payroll withholding is a separate PND.1/annual-summary stream. Each substantive skill states its statutory deadline and the evidence needed before claiming an extension.

Before submission, a preparer reconciles the computation, attachments and payment credits; an authorised filer checks taxpayer, period, return type and generated amount, then retains acknowledgement and proof of payment. This pack supplies reference and working papers; no authenticated portal submission is represented as tested here.

## Penalties and interest

No country-wide generic penalty applies to every tax. Load the relevant method, identify filing versus payment versus understatement, read the applicable penalty provision and current remission or extension, and keep tax, surcharge and fine separate. Escalate an unresolved assessment rather than selecting a convenient headline amount.

## Cross-border points

Domestic-source employment, business, an employer's Thai business or Thai property can be taxable even when paid abroad. Foreign-source income requires tracing the year earned, residence then and the amount/year brought into Thailand. The [Revenue Department foreign-income guide, printed pages 3-4](https://www.rd.go.th/fileadmin/user_upload/porphor/GuideTaxFromAbroad_TH.pdf) explains residence in the income year and taxation in the remittance year; [Order P.162/2566](https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/dn162A.pdf) excludes income arising before the stated commencement date from that interpretation. Capital and old savings are not automatically income, and transfers of mixed funds require a trace. Treaty relief and foreign tax credits require the relevant treaty, income category and tax evidence; do not net foreign taxes against Thai tax without applying the limitation.

## Two worked examples that recompute

**Residence decision.** Hypothetical stays of 90, 60 and 30 days total 180 and reach the domestic residence threshold. Removing 1 day produces 179 and does not reach it. This decides the domestic presence test only; it neither proves treaty residence nor makes every remittance taxable.

```oa-check
name: Thailand domestic residence presence decision
inputs:
  stay_a: 90
  stay_b: 60
  stay_c: 30
  shorter_stay_c: 29
steps:
  - full_total: stay_a + stay_b + stay_c
  - short_total: stay_a + stay_b + shorter_stay_c
  - full_margin: full_total - 180
  - short_margin: short_total - 180
expected:
  full_total: 180
  short_total: 179
  full_margin: 0
  short_margin: -1
```

**Mixed remittance evidence.** Assume THB 500,000 transferred comprises THB 200,000 of documented loan principal, THB 100,000 of documented pre-2024 savings and THB 200,000 of identified assessable foreign income arising while resident after that boundary. The income amount for further PIT/treaty analysis is THB 200,000, not the gross transfer. If the tracing fails, the subtraction is not allowed merely because the taxpayer calls the funds savings.

```oa-check
name: Thailand remittance tracing working paper
inputs:
  transfer: 500000
  documented_loan_principal: 200000
  documented_old_savings: 100000
steps:
  - income_to_analyse: transfer - documented_loan_principal - documented_old_savings
expected:
  income_to_analyse: 200000
```

## Ask the client first

- Individual, Thai entity, foreign branch or non-resident payee, and the actual activity?
- Income year/company period, residence days and treaty residence evidence?
- Where was work done, business carried on or property situated?
- Which funds were earned when, and when/how much was remitted?
- Registration, employees, turnover and any incentive or special regime?
- Filed returns, credits, tax notices and forthcoming deadlines?

## Sources

| Source and actual reading scope | URL | Read on |
|---|---|---|
| Thai Revenue Code (Read for §§39-41, 50, 56-57 quater for calendar year, source, residence and filing) | https://www.rd.go.th/5937.html | 2026-11-16 |
| Income Tax Schedule (Read for ordinary individual top rate and company net-profit rate) | https://www.rd.go.th/5938.html | 2026-11-16 |
| Revenue Code corporate provisions (Read for §§65-70 for company periods, scope and filing) | https://www.rd.go.th/english/37764.html | 2026-11-16 |
| Revenue Department VAT explanation (Read for §§1 and 4 for taxable-person and ordinary/zero-rate scope) | https://www.rd.go.th/english/6043.html | 2026-11-16 |
| Royal Decree 807 B.E. 2569 (Read for all 3 rendered pages, especially §§2-3 and substituted Decree 646 §4) | https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/dc807.pdf | 2026-11-16 |
| Revenue Department foreign-income credit guide, November 2025 (Read for printed pages 3-4, including residence in the income year, remittance year and treaty-credit boundaries) | https://www.rd.go.th/fileadmin/user_upload/porphor/GuideTaxFromAbroad_TH.pdf | 2026-11-16 |
| Order P.162/2566 (Read for whole operative single-page order amending P.161/2566) | https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/dn162A.pdf | 2026-11-16 |
| Revenue Department filing-service index (Read for forms and portal routes; no authenticated submission) | https://www.rd.go.th/rdeservice/63813.html | 2026-11-16 |

Not yet confirmed: 2026 annual PND.90/91 final forms and filing-year electronic deadline extensions; taxpayer-specific treaties, special exemptions and any later change to foreign-income remittance treatment. The former approximate top-up-tax 15% statement is routed to the unchanged substantive sibling rather than treated as a universal company tax.
