---
name: vu-payroll-social
description: "Vanuatu payroll, tax year 2026: no income tax withholding on wages; Vanuatu National Provident Fund registration, covered remuneration, 6% employer plus 6% employee from the January 2026 contribution (4% plus 4% before), the VT 3,000 monthly floor, remittance by the end of the next month and the 5% a month surcharge."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vu-payroll-social"
  jurisdiction: "VU"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Vanuatu payroll and social contributions

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to run payroll without professional review.

## Who this applies to

Employers with workers in Vanuatu, and their employees. Vanuatu has no ordinary income tax, so there is no income tax withholding on wages ("Vanuatu does not have an income tax system", Vanuatu Competent Authority AEOI guide). The payroll obligation is the Vanuatu National Provident Fund (VNPF) under the VNPF Act [Cap 189]. An employer with a worker for whom contributions are payable must apply to register with the Board and register its employees in the approved manner (ss 22 to 23A). Check the statutory definition of employee, the Schedule and any exemption before deciding coverage. Self-employed persons can apply for membership.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Contribution rate, January 2026 contribution onwards (payable February 2026) | Employer 6%, employee 6%, total 12% of covered remuneration (s 25(1) to (1A)) | 2026 | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vanuatu_national_provident_fund_consolidated_2026.pdf |
| Contribution rate, to the December 2025 contribution, including arrears for those months | Employer 4%, employee 4%, total 8% | 2025 | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vnpf_act_%5Bcap_189%5D_amended.pdf |
| Monthly floor, per employer | No contribution for a month in which total remuneration from that employer is below VT 3,000 (s 25) | 2026 | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vanuatu_national_provident_fund_consolidated_2026.pdf |
| Earnings cap | None specified in s 25 | 2026 | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vanuatu_national_provident_fund_consolidated_2026.pdf |
| Late payment surcharge | 5% of the unpaid contribution for each month or part of a month; if that comes to less than VT 50, VT 100 is payable (s 26(2)) | 2026 | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vanuatu_national_provident_fund_consolidated_2026.pdf |

The Fund's commencement notice names Act No. 25 of 2025 and Extraordinary Gazette No. 11 of 2025 for the 6% rate.

## The base

Covered remuneration starts from gross cash remuneration before deductions, including bonuses and incentives. Section 1 excludes specified benefits in kind approved in writing under the Employment Act, necessary employment reimbursements, housing allowances, statutory severance and employment gratuities. Test the floor on the total paid by that employer in the month; at VT 3,000 or more, apply the rate to the whole covered remuneration.

## Deadlines and filing

Deduct the employee's share when paying the wage; if the employer fails to deduct, the employer becomes liable for that share (s 25). Remit the month's contributions by the end of the following month in the prescribed form and manner (s 26). Employer guidance: https://www.vnpf.com.vu/employers.html.

## Penalties and interest

Unpaid contributions after the due date attract the s 26(2) surcharge above. The Board may remit it in whole or in part.

## Cross-border points

Coverage of foreign employees, exempt categories and workers sent abroad depends on the statutory definition of employee and the Schedule; this guide does not settle them. No social security agreements were found. For contributions from 1 January 2008 the Fund credits 50% to retirement, 25% to investment and 25% to medi-save (s 30); the Fund's income and withdrawals are exempt (s 46), and an employee's bankruptcy does not stop contributions (s 47).

## Two worked examples that recompute

**1. Employee on VT 150,000 for January 2026, covered, no exemption.** Employer 6% = VT 9,000; employee 6% = VT 9,000 deducted from pay; VT 18,000 remitted by 28 February 2026 (derived).

```oa-check
name: Vanuatu VNPF January 2026
inputs:
  pay: 150000
steps:
  - employer: pay * 0.06
  - employee: pay * 0.06
  - total: employer + employee
expected:
  employer: 9000
  employee: 9000
  total: 18000
```

**2. Arrears for December 2025, VT 150,000 paid late in 2026.** The 2025 rate still applies to that month: 4% each, VT 6,000 employer and VT 6,000 employee (derived). One month late adds the 5% surcharge on VT 12,000, VT 600 (derived).

```oa-check
name: Vanuatu VNPF December 2025 arrears
inputs:
  pay: 150000
steps:
  - employer: pay * 0.04
  - employee: pay * 0.04
  - surcharge_one_month: (employer + employee) * 0.05
expected:
  employer: 6000
  employee: 6000
  surcharge_one_month: 600
```

## Ask the client first

- Is the employer registered with the VNPF, and each employee?
- Monthly remuneration per employee and what it includes (bonuses, housing, benefits in kind)?
- Which contribution month (before or from January 2026)?
- Any foreign, part-time or exempt workers?
- Any unpaid months?

## Sources

| Source | URL | Read on |
|---|---|---|
| VNPF Act [Cap 189], 2026 consolidation, ss 1, 22 to 26, 30, 46, 47 (Read by Ryan Duguid; SHA-256 5b86eaded090ec5d14e862976f48d77553a6a1d66e77270e7fa7e2fe15bdb589; vnpf.com.vu refused scripts on 2026-11-14) | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vanuatu_national_provident_fund_consolidated_2026.pdf | 2026-11-11 |
| VNPF Act [Cap 189], 2021 consolidation, s 25 (Read by Ryan Duguid for the 4% rates) | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vnpf_act_%5Bcap_189%5D_amended.pdf | 2026-11-11 |
| VNPF commencement notice (Read by Ryan Duguid for the January 2026 start) | https://www.vnpf.com.vu/news.html | 2026-11-11 |
| Bill for the VNPF (Amendment) Act 2025, as tabled (Read for the commencement clause; it proposed 7% each, Parliament passed 6%) | https://parliament.gov.vu/images/Bills/Second%20Ordinary%20session%202025/Bill%20for%20the%20Vanuatu%20National%20Provident%20Fund/Bill%20for%20the%20Vanuatu%20National%20Provident%20Fund%20Am%20Act%20No.%20%20of%202025.pdf | 2026-11-14 |
| Vanuatu Competent Authority, AEOI guide v4 (Read for no income tax system) | https://vanuatucustoms.gov.vu/images/Forms/VCA/VU_AEOI_Guide_v4.pdf | 2026-11-14 |

Not yet confirmed: the gazetted Act No. 25 of 2025 itself (the 6% rate rests on the Fund's 2026 consolidation and notice as Ryan Duguid read them; vnpf.com.vu could not be reopened); exempt and cross-border workers; the full rounding rules; registration and remittance procedures.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vu-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vu-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
