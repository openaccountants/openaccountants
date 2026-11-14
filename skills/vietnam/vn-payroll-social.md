---
name: vn-payroll-social
description: >
  Vietnam payroll and compulsory insurance for 2026. Use for employer and
  employee social insurance (Law 41/2024/QH15), health insurance and
  unemployment insurance rates, the contribution floor and the 20 times
  reference-level cap (VND 46.8 million to 30 June 2026, 50.6 million from
  1 July 2026), the 2026 regional minimum wages, payment deadlines, and
  monthly PIT withholding on salaries. Covers employers of Vietnamese and
  foreign staff. Tier 2, not reviewed by an accountant.
version: "2.0"
jurisdiction: VN
tax_year: 2026
tax_year_notes: "Calendar year 2026. The reference level (base salary) rose from VND 2,340,000 to 2,530,000 on 1 July 2026, so the cap changes mid-year."
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Vietnam Payroll and Social Contributions v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers in Vietnam and their employees in 2026: compulsory social insurance (BHXH) under Law 41/2024/QH15 (in force 1 July 2025), health insurance (BHYT) and unemployment insurance (BHTN) under the Employment Law 74/2025/QH15 (in force 1 January 2026), plus PIT withholding on pay. Foreign employees with qualifying contracts are within compulsory social insurance with limited exceptions (Law 41/2024 Art. 2(2)); confirm each case. The PIT schedule and deductions are owned by [vietnam-pit](vietnam-pit.md).

### Refusals and boundaries

- Do not apply the cap for one half of 2026 to the other: the reference level changed on 1 July 2026.
- Occupational accident and disease insurance, the unemployment insurance cap and foreign workers' unemployment insurance position are on the "Not yet confirmed" line; compute them only from the official text.
- Trade union fee is outside this skill.

## Rates, bands and thresholds

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Employee social insurance (retirement and survivorship fund) | 8% | Law 41/2024 Art. 33(1)(a) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/5/468972-1772691642_v1_1772691941_signed.pdf |
| Employer social insurance, sickness and maternity fund | 3% | Art. 34(1)(a) | same |
| Employer social insurance, retirement and survivorship fund | 14% | Art. 34(1)(b) | same |
| Social insurance salary floor and cap | Floor = reference level; cap = 20 times the reference level at the time of payment | Art. 31(1)(đ); while the base salary exists the reference level equals it | same |
| Reference level (base salary) and cap, 1 January to 30 June 2026 | VND 2,340,000 (Decree 73/2024, from 1 July 2024); cap VND 46,800,000 a month | Cap computed: 20 times 2,340,000 | Nghe An provincial portal on Decree 73/2024: https://hcc.nghean.gov.vn/tin-tong-hop/chinh-phu-quy-dinh-muc-luong-co-so-va-che-do-tien-thuong-moi-voi-can-bo-cong-chuc-vien-chuc-luc-luong-vu-trang-1429.html |
| Reference level and cap from 1 July 2026 | VND 2,530,000; cap VND 50,600,000 a month | Decree 161/2026; 20 times 2,530,000 | https://xaydungchinhsach.chinhphu.vn/tu-1-7-nhieu-khoan-tro-cap-bhxh-thay-doi-the-nao-khi-luong-co-so-tang-119260523163024829.htm |
| Health insurance | 4.5% of the social insurance salary: employer two thirds, employee one third (3% and 1.5%, computed from the 4.5%) | Decree 188/2025 | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-188-2025-nd-cp-quy-dinh-moi-ve-doi-tuong-muc-dong-muc-ho-tro-dong-bao-hiem-y-te-119250711175642187.htm |
| Unemployment insurance | Employee up to 1% of monthly pay; employer up to 1% of the payroll of participating staff | Employment Law 74/2025/QH15, from 1 January 2026; the 1% in practice is set by Decree 374/2025 | https://xaydungchinhsach.chinhphu.vn/quy-dinh-muc-dong-bao-hiem-that-nghiep-119250711175950882.htm |
| Regional minimum wage 2026, Region I | VND 5,310,000 a month | Decree 293/2025, from 1 January 2026 | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-293-2025-nd-cp-quy-dinh-muc-luong-toi-thieu-doi-voi-nguoi-lao-dong-lam-viec-theo-hop-dong-lao-dong-119251110172808433.htm |
| Region II | VND 4,730,000 | same | same |
| Region III | VND 4,140,000 | same | same |
| Region IV | VND 3,700,000 | same | same |

The old file said the employer total is 21.5% including 0.5% occupational accident insurance and gave a 20-times cap of 46.8 million for the whole year. The social, health and unemployment shares above total 21% for the employer and 10.5% for the employee; the 0.5% is not confirmed here, and the cap is 50.6 million from 1 July 2026.

## The base

1. Contribution salary: the monthly salary, salary allowances and other regular, stable amounts agreed in the contract (Law 41/2024 Art. 31(1)). It may not be below the regional minimum wage for the simplest job, nor below the reference level.
2. Cap the salary at 20 times the reference level for the month (46.8 million to June, 50.6 million from July 2026).
3. Employee: 8% social plus 1.5% health plus 1% unemployment. Employer: 17% social (3% plus 14%) plus 3% health plus 1% unemployment.
4. Employee contributions reduce PIT taxable income (see [vietnam-pit](vietnam-pit.md)).
5. Withhold PIT monthly on the five-band schedule for residents, or 20% flat for non-residents.

## Deadlines and filing

| Item | Deadline | Source |
| --- | --- | --- |
| Employer social insurance, monthly method | Last day of the following month | Law 41/2024 Art. 34(4)(a) |
| Employer social insurance, 3 or 6 monthly method | Last day of the month after the cycle | Law 41/2024 Art. 34(4)(b) |
| PIT withholding return, monthly filers | 20th day of the following month | Decree 252/2026 via the Government portal |
| PIT withholding return, quarterly filers | Last day of the first month of the next quarter | same |
| Employer PIT finalisation for employees | Last day of the 3rd month after year end | same |

## Penalties and interest

Late tax payment carries interest of 0.03% per day (Law 108/2025/QH15 Art. 16(2)(a)). Late or evaded social insurance is handled under Law 41/2024 Art. 35 and following; the interest and fine figures were not read (see "Not yet confirmed").

## Cross-border points

- Foreign employees with labour contracts are generally within compulsory social insurance; exceptions (for example intra-company transferees, those at retirement age) must be checked against Law 41/2024 Art. 2(2) and its decree.
- Totalisation agreements may exempt seconded staff; the agreement text decides.
- A non-resident employee's PIT is 20% of gross pay for work in Vietnam, with no deductions.

## Two worked examples that recompute

### Example 1: employee on VND 30 million a month, August 2026

Below the 50.6 million cap. Employer: 30 million times 21% = 6.3 million. Employee: 30 million times 10.5% = 3.15 million.

```oa-check
name: VN 2026 payroll contributions below the cap
inputs:
  salary: 30000000
steps:
  - employer: salary * (0.03 + 0.14 + 0.03 + 0.01)
  - employee: salary * (0.08 + 0.015 + 0.01)
expected:
  employer: 6300000
  employee: 3150000
```

### Example 2: manager on VND 80 million a month, March against July 2026: does the cap change?

Social and health insurance stop at the cap. March: cap 46.8 million, employee social 3.744 million and health 0.702 million. July: cap 50.6 million, employee social 4.048 million and health 0.759 million. Each month from July costs the employee 0.361 million more and the employer, at 20% on the same base, 0.76 million more. Unemployment insurance is left out: its cap is not confirmed.

```oa-check
name: VN 2026 payroll cap before and after 1 July
inputs:
  salary: 80000000
  cap_h1: 46800000
  cap_h2: 50600000
steps:
  - si_mar: min(salary, cap_h1) * 0.08
  - hi_mar: min(salary, cap_h1) * 0.015
  - si_jul: min(salary, cap_h2) * 0.08
  - hi_jul: min(salary, cap_h2) * 0.015
  - employee_increase: (si_jul + hi_jul) - (si_mar + hi_mar)
  - employer_increase: (min(salary, cap_h2) - min(salary, cap_h1)) * (0.17 + 0.03)
expected:
  si_mar: 3744000
  hi_mar: 702000
  si_jul: 4048000
  hi_jul: 759000
  employee_increase: 361000
  employer_increase: 760000
```

## Ask the client first

1. Monthly contract salary and regular allowances, by month.
2. Nationality, contract type and length, and any secondment or totalisation agreement.
3. Workplace region (I to IV) for the minimum wage floor.
4. Whether the employee is resident for PIT and how many dependants are registered.
5. Whether the employer pays monthly or on a 3 or 6 month cycle.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Nghe An provincial government portal: read for Decree 73/2024, base salary 2.340.000 dong a month from 1 July 2024 | https://hcc.nghean.gov.vn/tin-tong-hop/chinh-phu-quy-dinh-muc-luong-co-so-va-che-do-tien-thuong-moi-voi-can-bo-cong-chuc-vien-chuc-luc-luong-vu-trang-1429.html | 2026-11-14 |
| Read for the consolidated Social Insurance Law 41/2024/QH15 (VBHN 19/VBHN-VPQH, February 2026): Art. 31 contribution salary floor and cap, Art. 32 rates, Art. 33 employee 8%, Art. 34 employer 3% and 14% and payment deadlines | https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/5/468972-1772691642_v1_1772691941_signed.pdf | 2026-11-14 |
| Read for the base salary rise to VND 2,530,000 from 1 July 2026 (Decree 161/2026) and the cap of 50,600,000 | https://xaydungchinhsach.chinhphu.vn/tu-1-7-nhieu-khoan-tro-cap-bhxh-thay-doi-the-nao-khi-luong-co-so-tang-119260523163024829.htm | 2026-11-14 |
| Read for Decree 188/2025 health insurance rate of 4.5%, two thirds employer and one third employee | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-188-2025-nd-cp-quy-dinh-moi-ve-doi-tuong-muc-dong-muc-ho-tro-dong-bao-hiem-y-te-119250711175642187.htm | 2026-11-14 |
| Read for the Employment Law unemployment insurance rates (up to 1% each) | https://xaydungchinhsach.chinhphu.vn/quy-dinh-muc-dong-bao-hiem-that-nghiep-119250711175950882.htm | 2026-11-14 |
| Read for Decree 293/2025 regional minimum wages from 1 January 2026 | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-293-2025-nd-cp-quy-dinh-muc-luong-toi-thieu-doi-voi-nguoi-lao-dong-lam-viec-theo-hop-dong-lao-dong-119251110172808433.htm | 2026-11-14 |
| Read for the Decree 252/2026 withholding return deadlines | https://xaydungchinhsach.chinhphu.vn/quy-dinh-thoi-han-nop-ho-so-khai-thue-119260703120801722.htm | 2026-11-14 |
| Read for Law 108/2025/QH15 Art. 16(2)(a) late payment interest | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf | 2026-11-14 |

Not yet confirmed: occupational accident and disease insurance rate (old file 0.5%; Law on Occupational Safety and Health and its decree not read); unemployment insurance salary cap (old file 20 times the Region I minimum wage, 106.2 million) and the Decree 374/2025 rate as applied; whether foreign employees are within unemployment insurance in 2026; social insurance late payment interest and fines; the exceptions for foreign employees in Law 41/2024 Art. 2(2) and its decree (baohiemxahoi.gov.vn did not open from a script on 14 November 2026).
