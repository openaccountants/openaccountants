---
name: bd-payroll
description: "Bangladesh 2026 salary tax withholding workflow: annual estimate, current individual relief, average-rate deduction, in-year corrections and remittance evidence, with employer fund duties kept separate."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bd-payroll"
  jurisdiction: "BD"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bangladesh salary withholding v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Employers paying Bangladesh employment income. Covers the salary-tax estimate/deduction working paper, not every payroll labour-law entitlement. A solo proprietor without staff has no employee payroll merely by making drawings.

## Ask the client first

- Employee residence/citizenship, period and taxpayer category.
- Annual salary, benefits, bonuses and other relevant employment details.
- Verified eligible investments/reliefs and prior/current source deductions.
- Pay dates, treasury challans, withholding-return status and fund obligations.

## The method, step by step

### Withholding rate

| Item | Rate and conditions | Official source |
|---|---|---|
| Employment-income payment | Average tax rate on estimated annual employment income; adjust current-year shortfall/excess as allowed | Income Tax Act section 86: https://bdlaws.minlaw.gov.bd/act-1429/section-51916.html |

1. Estimate annual employment income and applicable tax using [PIT](bangladesh-pit.md), including current aggregate salary relief, bands, rebate conditions and minimum tax. Do not reuse the old basic threshold or separate salary-component exemptions.
2. Section 86 requires deduction at payment at the average tax rate on estimated employment income. Keep the annual estimate, applicable base and pay-period calculation together; do not apply the highest marginal band to all salary (https://bdlaws.minlaw.gov.bd/act-1429/section-51916.html).
3. Reforecast for bonus, benefit, joiner/leaver or corrected evidence. Section 86(4) permits an in-year increase/decrease for a deduction shortfall/excess. A statutory reduced/no-deduction certificate is a separate mechanism; do not simply stop withholding on an employee's assertion.
4. Record salary expense, employee withholding payable, net salary and any separate employee PF deduction. Use [payroll/social](bd-payroll-social.md) for mandatory PF/Progoti, WPPF and gratuity conditions; use [social contributions](bd-social-contributions.md) for voluntary individual choices. Do not infer that all employer benefits are voluntary.
5. Deposit deducted tax by e-challan under Rule 9 of the current Withholding Tax Rules, 2026, SRO 273 dated 5 July 2026, deemed effective from 1 July 2026. It replaces the June SRO 210. Keep the employee allocation and treasury evidence; use the exact calendar below, not a uniform fortnight estimate (https://www.dpp.gov.bd/upload_file/gazettes/62247_76058.pdf).
6. Give the reviewer the annual estimate, deduction history, in-year corrections, deposit evidence and unresolved reporting items. A payroll calculation is not proof that withholding was remitted or the required return was filed.

### Deposits, certificates and withholding returns

| Deduction/collection timing | Treasury deposit deadline | Official source |
|---|---|---|
| July through May | Within 2 weeks after the deduction/collection month ends | Current Rules 9, printed page 20719: https://www.dpp.gov.bd/upload_file/gazettes/62247_76058.pdf |
| June 1-20 | Within 7 days following deduction/collection | same |
| Other June days, except the final working day | Following day | same |
| Final working day of June | Same day | same |

Rule 10 uses Schedule 1 for an employment-income withholding certificate where the pay is not government salary; Schedule 2 covers other deductions and Schedule 3 collections. Attach the deposited e-challan. Give the certificate within 2 weeks of the following month or at the time suitable to settle the recipient's tax liability under Rule 10(5). The alternative records described in Rule 10(6) do not substitute for the employment certificate because Rule 10(7) excludes salary withholding from that provision. Keep the salary, benefits, TIN, deduction, estimate/relief and challan particulars specified in Schedule 1 (https://www.dpp.gov.bd/upload_file/gazettes/62247_76058.pdf, printed pages 20719-20721).

Section 177 requires a **quarterly** withholding return from its listed payers. The list includes companies excluding government ministries, divisions, directorates, inspectorates and MPO educational institutions; firms; AOPs; private hospitals, clinics and diagnostic centres; PPPs; e-commerce/online marketplaces and hotels, resorts, motels, restaurants, convention centres, community centres and transport agencies with annual turnover over BDT 10,000,000 (1 crore, in words on the page); non-farmer tobacco-product producers; and individuals with annual business turnover over BDT 100,000,000 (10 crore, in words on the page). Apply the complete entity/activity conditions, rather than assuming every employer is automatically included (https://bdlaws.minlaw.gov.bd/act-1429/section-52007.html).

| Reporting quarter | Return due | Official source |
|---|---|---|
| July-September | 25 October | Section 177(3): https://bdlaws.minlaw.gov.bd/act-1429/section-52007.html |
| October-December | 25 January | same |
| January-March | 25 April | same |
| April-June | 25 July | same |

If a listed return date is a weekly or government holiday, file on the next working day. Rule 13 prescribes Schedule 4; section 177 also requires the appropriate Deputy Commissioner jurisdiction, prescribed schedules/documents and signature/verification, with Board power to prescribe electronic filing. Reconcile quarterly return totals to payroll and other covered payments, deductions, deposits and certificates. Confirm the actual e-TDS fields before submission; quarterly reporting does not extend a Rule 9 deposit deadline.

## Worked cases

### Ordinary employee annual estimate

Illustrative general-category resident annual salary 600,000 and no other relevant amounts. Under the PIT salary exclusion, employment income after exclusion is 400,000 and ordinary band tax is 0; an automatic positive deduction merely because gross pay exceeds the threshold would be wrong. No special income/minimum-tax regime is assumed. Figures are derived from the PIT provisions.

```oa-check
name: Annual salary after current aggregate relief
inputs:
  annual_salary: 600000
steps:
  - exclusion: min(annual_salary / 3, 500000)
  - ordinary_income: annual_salary - exclusion
  - band_tax: min(max(ordinary_income - 400000, 0), 300000) * 0.10
expected:
  exclusion: 200000
  ordinary_income: 400000
  band_tax: 0
```

### Edge: in-year under-deduction correction

A reviewed revised annual withholding estimate is 36,000; 20,000 has already been deducted and 4 equal remaining pay periods are assumed. Remaining deduction is 16,000, or 4,000 per period. The annual estimate is an input established from the employee's facts, not a tax rate invented here.

```oa-check
name: Salary withholding shortfall spread over remaining equal periods
inputs:
  annual_estimate: 36000
  already_deducted: 20000
  remaining_periods: 4
steps:
  - remaining: annual_estimate - already_deducted
  - per_period: remaining / remaining_periods
expected:
  remaining: 16000
  per_period: 4000
```

## When to refuse or refer

Refer foreign/non-resident employees, disputed employment status, unsupported relief, leaver/negative-adjustment treatment and unresolved filing/deposit rules. Never mark payroll tax paid without treasury evidence or assume drawings are wages.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for salary average-rate deduction, in-year adjustment and reduced/no-deduction certificate conditions, section 86 | https://bdlaws.minlaw.gov.bd/act-1429/section-51916.html | 2026-11-14 |
| Read for salary cap amendment, Sixth Schedule paragraph 27 | https://bdlaws.minlaw.gov.bd/act-1718/section-59129.html | 2026-11-14 |
| Read for ordinary individual bands and thresholds, Finance Act schedule 2 | https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf | 2026-11-14 |
| Read for investment rebate formula and qualifications section 78 | https://bdlaws.minlaw.gov.bd/act-1429/section-51908.html | 2026-11-14 |
| Read visually for current Rules 9-14, deposit calendar, certificates, Schedule 1 and replacement of June rules; printed pages 20719-20722 | https://www.dpp.gov.bd/upload_file/gazettes/62247_76058.pdf | 2026-11-14 |
| Read for complete current section 177 payer classes, quarterly dates, holiday exception, documents and electronic-filing power | https://bdlaws.minlaw.gov.bd/act-1429/section-52007.html | 2026-11-14 |

Not yet confirmed: Live e-TDS portal fields, any case-specific later Board filing direction or extension, and taxpayer-specific foreign/non-resident employment adjustments. The sourced deposit and quarterly-return rules above replace the old approximate remittance/monthly-return wording.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bd-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bd-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
