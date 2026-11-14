---
name: nv-payroll
description: "Nevada payroll and unemployment insurance, 2026, tax year 2026: applicability, state computations, exceptions, registration, returns, payment and source-backed worked cases."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nv-payroll"
  jurisdiction: "US-NV"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Nevada payroll and unemployment insurance, 2026

## Scope

Nevada 2026 employer unemployment insurance (UI) and Career Enhancement Program (CEP). Nevada imposes no state individual income-tax withholding; workers may still have federal or another state's obligations. Federal payroll calculations stay in `us-form-941-940-payroll`. Employer MBT and its Commerce credit are computed only in `nv-commerce-and-mbt`.

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.

## Ask the client first

1. FEIN, legal entity, start/acquisition date, ESD account and liability notice?
2. Employees, officers/owners, contractors and Nevada/multistate work locations?
3. Gross wages/tips, employee calendar-year wage history and recognized predecessor wages?
4. Actual 2026 UI/CEP rate notice and prior filings/payments?
5. Household, agricultural, nonprofit, government or other special coverage?
6. No-payroll/closure dates and separate Department MBT registration?

## The method, step by step

1. **Register with ESD** through NUI Employer Self-Service within 30 days after ordinary liability begins at $225 wages in a quarter. Special coverage tests differ. Keep the employer liability notice and assigned account; ESD registration automatically sets up MBT at the Department of Taxation, which uses a separate account. [Official source](https://detr.nv.gov/content/media/Employer_Handbook_Published_9_2023.pdf); [Official source](https://tax.nv.gov/faqs/modified-business-tax-faqs/).
2. **Determine covered wages and location.** Do not replace state worker-status rules with a 1099 label. For multistate work, use localization, then base/direction/residence rules; refer uncertain coverage and acquisitions before transferring experience or wage history. Employer UI/CEP is not employee income-tax withholding. [Official source](https://detr.nv.gov/content/media/Employer_Handbook_Published_9_2023.pdf); [Official source](https://detr.nv.gov/Page/NUI_View_Quarterly_Reporting_Info).
3. **Cap each worker's 2026 UI wages at $43,700**, after recognized earlier-year wages. Report gross wages even when above the cap. The dated 2026 notice supersedes 2025's $41,800. [Official source](https://detr.nv.gov/content/media/Contributions_Newsletter_December_2025.pdf); [Official source](https://www.nevadaworkforce.com/_docs/EDS_Wage-Benefit/MWB-2024.PDF).
4. **Apply the assigned UI and CEP rates.** New employer UI is 2.95%; CEP adds 0.05%, normally 3.00% combined. Experience UI ranges 0.25%-5.4%; CEP does not apply at 5.4%. Download the 2026 notice in ESS; do not choose a rate from the range. MBT has no corresponding per-worker cap. [Official source](https://detr.nv.gov/Page/NUI_View_Quarterly_Reporting_Info); [Official source](https://detr.nv.gov/content/media/Contributions_Newsletter_December_2025.pdf).

### Rates, bases and dates

| Item | Amount or rule | Official source |
| --- | --- | --- |
| 2026 UI wage base | $43,700 per covered employee/calendar year | [Official source](https://detr.nv.gov/content/media/Contributions_Newsletter_December_2025.pdf) |
| New employer UI | 2.95% | [Official source](https://detr.nv.gov/Page/NUI_View_Quarterly_Reporting_Info) |
| CEP | 0.05%; not charged at 5.4% UI rate | [Official source](https://detr.nv.gov/Page/NUI_View_Quarterly_Reporting_Info) |
| Experience UI range | 0.25%-5.4%; use assigned 2026 notice | [Official source](https://detr.nv.gov/Page/NUI_View_Quarterly_Reporting_Info) |
| Ordinary registration | $225 quarterly wages; within 30 days of subjectivity | [Official source](https://detr.nv.gov/content/media/Employer_Handbook_Published_9_2023.pdf) |
| 2026 quarter report/payment dates | April 30, July 31, November 2, 2026; February 1, 2027 | [Official source](https://detr.nv.gov/Page/NUI_View_Quarterly_Reporting_Info) |

## Worked cases

**Case 1:** A new employer pays $5,000 after $42,000 earlier 2026 wages. Only $1,700 is taxable; UI $50.15 andCEP $0.85, total $51. Report all $5,000 gross wages.

```oa-check
name: NV new employer remaining cap
inputs:
  prior: 42000
  current: 5000
steps:
- taxable: min(current, max(43700 - prior, 0))
- ui: taxable * 0.0295
- cep: taxable * 0.0005
- total: ui + cep
expected:
  taxable: 1700
  ui: 50.15
  cep: 0.85
  total: 51
```

**Case 2:** At $10,000 taxable wages, a 5.4% assigned employer owes $540 UIand no CEP. A new employer instead owes $295 UI+$5 CEP=$300. The lower amount cannot be selected unless the rate notice assigns it.

```oa-check
name: NV maximum UI CEP decision
inputs:
  wages: 10000
steps:
- maximum_ui: wages * 0.054
- maximum_cep: wages * 0
- new_ui: wages * 0.0295
- new_cep: wages * 0.0005
- new_total: new_ui + new_cep
expected:
  maximum_ui: 540
  maximum_cep: 0
  new_ui: 295
  new_cep: 5
  new_total: 300
```

## When to refuse or refer

Refer employee status, special coverage, multistate work, successor experience/wages and contested rates. Do not use the UI cap for MBT or treat no Nevada income tax as exemption from employer taxes.

## Filing and payment

File Contribution and Wage Reports electronically in NUI ESS each quarter, including zero payroll, unless ESD approves a waiver. Due last day of month after quarter, end adjusted for holidays/weekends; 2026 actual dates are in the table. Pay electronically when required by the state and save confirmations. Notify ESD on closure/sale and complete reporting through last payroll; ESD then alerts Taxation to close MBT. Keep per-worker base/rate reconciliation and notices. [Official source](https://detr.nv.gov/Page/NUI_View_Quarterly_Reporting_Info); [Official source](https://detr.nv.gov/content/media/Contributions_Newsletter_December_2025.pdf).

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| DETR 2026 newsletter. Read for 2026 base, rate notices, electronic reporting and closure. | https://detr.nv.gov/content/media/Contributions_Newsletter_December_2025.pdf | 2026-11-13 |
| DETR quarterly reporting. Read for UI/CEP rates, gross wages, zero returns and 2026 calendar. | https://detr.nv.gov/Page/NUI_View_Quarterly_Reporting_Info | 2026-11-13 |
| DETR employer handbook. Read for ordinary registration threshold and timing, special coverage and status. | https://detr.nv.gov/content/media/Employer_Handbook_Published_9_2023.pdf | 2026-11-13 |
| State 2026 wage-base determination. Read for NRS 612.545 annual wage calculation; scanned source cross-checked toDETR. | https://www.nevadaworkforce.com/_docs/EDS_Wage-Benefit/MWB-2024.PDF | 2026-11-13 |
| DOR MBT FAQ. Read for ESDregistration creates separate MBT account. | https://tax.nv.gov/faqs/modified-business-tax-faqs/ | 2026-11-13 |

Not yet confirmed: individual experience rate without the 2026 notice, special worker/household/agricultural/nonprofit coverage and successor transfers. Late-interest/penalty disputes require current ESD assessment instructions; this skill supplies no invented charge.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nv-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nv-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
