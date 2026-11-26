---
name: vn-payroll-social
description: >
  Vietnam payroll and compulsory insurance for 2026. Use for employer and
  employee social insurance (Law 41/2024/QH15), health insurance and
  unemployment and occupational accident insurance rates, the contribution
  floor, the separate reference-level and regional wage caps, payment deadlines and
  monthly PIT withholding on salaries. Covers employers of Vietnamese and
  foreign staff. Tier 2, not reviewed by an accountant.
version: "2.1"
jurisdiction: VN
tax_year: 2026
tax_year_notes: "Calendar year 2026. The reference level (base salary) rose from VND 2,340,000 to 2,530,000 on 1 July 2026, so the cap changes mid-year."
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Vietnam Payroll and Social Contributions v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers in Vietnam and their employees in 2026. This guide covers social insurance (BHXH) under Law 41/2024/QH15, health insurance (BHYT) under the Health Insurance Law as amended by Law 51/2024/QH15, occupational accident and disease insurance, unemployment insurance (BHTN) under Employment Law 74/2025/QH15 and PIT withholding on pay. See [vietnam-pit](vietnam-pit.md) for the PIT schedule and deductions.

### Refusals and boundaries

- Do not apply the cap for one half of 2026 to the other: the reference level changed on 1 July 2026.
- Check coverage and the applicable wage base separately for each scheme.
- Trade union fee is outside this skill.

## Rates, bands and thresholds

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Employee social insurance (retirement and survivorship fund) | 8% | Law 41/2024 Art. 33(1)(a) | https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/5/468972-1772691642_v1_1772691941_signed.pdf |
| Employer social insurance, sickness and maternity fund | 3% | Art. 34(1)(a) | same |
| Employer social insurance, retirement and survivorship fund | 14% | Art. 34(1)(b) | same |
| Social insurance salary floor and cap | Floor = reference level; cap = 20 times the reference level at the time of payment | Art. 31(1)(đ); while the base salary exists the reference level equals it | same |
| Reference level (base salary) and cap, 1 January to 30 June 2026 | VND 2,340,000 (Decree 73/2024, from 1 July 2024). Cap VND 46,800,000 a month | Cap calculated at 20 times VND 2,340,000 | https://congbao.chinhphu.vn/tai-ve-van-ban-so-73-2024-nd-cp-42169-50685?format=pdf |
| Reference level and cap from 1 July 2026 | VND 2,530,000; cap VND 50,600,000 a month | Decree 161/2026; 20 times 2,530,000 | https://xaydungchinhsach.chinhphu.vn/tu-1-7-nhieu-khoan-tro-cap-bhxh-thay-doi-the-nao-khi-luong-co-so-tang-119260523163024829.htm |
| Health insurance | 4.5% of the social insurance contribution salary, split two thirds employer and one third employee (3% and 1.5%) | Ordinary covered employees, Decree 188/2025 Art. 6(1)(a) | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-188-2025-nd-cp-quy-dinh-moi-ve-doi-tuong-muc-dong-muc-ho-tro-dong-bao-hiem-y-te-119250711175642187.htm |
| Occupational accident and disease insurance | Employer 0.5% of the social insurance contribution salary, or 0.3% with approval | Consolidated Decree 58/2020 Arts. 4–5. The lower rate requires a decision covering the employer and period | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/05-vbhn-bnv.pdf |
| Unemployment insurance | Employee 1% of contribution salary and employer 1% of the participating payroll | Employment Law 74/2025/QH15 and Decree 374/2025 Art. 4, from 1 January 2026 | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/27/cong-bao-so-48-ngay-23-01-46946signed-17694874955991619007433.pdf |
| Unemployment insurance cap | 20 times the applicable regional monthly minimum wage | Employment Law 74/2025 Art. 34(2). Regions I–IV: VND 106.2m, 94.6m, 82.8m and 74m per month respectively | https://congbao.chinhphu.vn/tai-ve-van-ban-so-74-2025-qh15-45562-57700?format=pdf |
| Regional minimum wage 2026, Region I | VND 5,310,000 a month | Decree 293/2025, from 1 January 2026 | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-293-2025-nd-cp-quy-dinh-muc-luong-toi-thieu-doi-voi-nguoi-lao-dong-lam-viec-theo-hop-dong-lao-dong-119251110172808433.htm |
| Region II | VND 4,730,000 | same | same |
| Region III | VND 4,140,000 | same | same |
| Region IV | VND 3,700,000 | same | same |

For an ordinary covered employee with the same contribution salary under all 4 schemes, the employer pays 21.5% at the standard accident insurance rate and the employee pays 10.5%. Calculate each scheme separately when its cap or eligibility differs.

## The base

1. Start from the monthly job salary, salary allowances and other regular, stable contractual amounts (Law 41/2024 Art. 31(1) and Decree 158/2025 Art. 7). Apply the social insurance floor under Art. 31 separately from the applicable employment minimum wage under Decree 293/2025 Arts. 3–4.
2. For the ordinary employee, cap the social, health and occupational accident insurance salary at 20 times the reference level (VND 46.8m through June, VND 50.6m from July). Apply the separate regional wage cap to unemployment insurance.
3. Apply the rates above to each scheme's contribution salary.
4. Deduct compulsory employee insurance contributions when calculating a resident employee's taxable salary (see [vietnam-pit](vietnam-pit.md)).
5. Withhold resident PIT on the progressive schedule for employment contracts of at least 3 months. For shorter contracts or qualifying payments without a contract, check the separate 10% withholding rule, payment threshold and declaration exception. Withhold 20% on a non-resident's taxable pay for work in Vietnam.

## Deadlines and filing

| Item | Deadline | Source |
| --- | --- | --- |
| Employer social insurance, monthly method | Last day of the following month | Law 41/2024 Art. 34(4)(a) |
| Employer social insurance, eligible 3 or 6 month cycle | Last day of the month after the cycle | Law 41/2024 Arts. 33(1)(b) and 34(4)(b), for eligible output or piece-rate workers in agriculture, forestry, fisheries and salt production |
| PIT withholding return, monthly filers | 20th day of the following month | Decree 252/2026 via the Government portal |
| PIT withholding return, quarterly filers | Last day of the first month of the next quarter | same |
| Employer PIT finalisation for employees | Last day of the 3rd month after year end | same |

## Penalties and interest

Late tax payment carries interest of 0.03% per day (Law 108/2025/QH15 Art. 16(2)(a)). Late or evaded compulsory social or unemployment insurance attracts 0.03% per day on the unpaid amount under Law 41/2024 Arts. 40–41. Determine any separate fine from the offence, its timing and the applicable penalty provision.

## Cross-border points

- Foreign employees on a fixed-term contract of at least 12 months with a Vietnamese employer generally join compulsory social and health insurance. Check the exceptions for intra-company transfers, statutory retirement age at signing and applicable treaties under Social Insurance Law Art. 2(2) and Health Insurance Law Art. 12(1)(c).
- Foreign employees are outside compulsory unemployment insurance under Employment Law Arts. 2 and 31. Check the employer's separate duty to pay a contribution equivalent with wages under Labour Code Art. 168(3).
- Non-resident PIT is 20% of taxable remuneration for work in Vietnam, regardless of where it is paid. Resident deductions do not apply.

## Two worked examples that recompute

### Example 1: employee on VND 30 million a month, August 2026

A Vietnamese employee covered by all 4 schemes earns VND 30 million in insurable pay, below all applicable caps. At the standard accident insurance rate, the employer pays VND 30 million × 21.5% = VND 6.45 million. The employee pays VND 30 million × 10.5% = VND 3.15 million.

```oa-check
name: VN 2026 payroll contributions below the cap
inputs:
  salary: 30000000
steps:
  - employer: salary * (0.03 + 0.14 + 0.005 + 0.03 + 0.01)
  - employee: salary * (0.08 + 0.015 + 0.01)
expected:
  employer: 6450000
  employee: 3150000
```

### Example 2: manager on VND 80 million a month, March against July 2026: does the cap change?

Assume a Vietnamese manager in Region I covered by all 4 schemes at the standard accident insurance rate. The social, health and accident insurance cap rises from VND 46.8m in March to VND 50.6m in July. With the unemployment cap at VND 106.2m, each party pays VND 800,000 of unemployment insurance in both months. The employee total rises from VND 5,246,000 to VND 5,607,000, an increase of VND 361,000. The employer total rises from VND 10,394,000 to VND 11,173,000, an increase of VND 779,000.

```oa-check
name: VN 2026 payroll cap before and after 1 July
inputs:
  salary: 80000000
  cap_h1: 46800000
  cap_h2: 50600000
  ui_cap: 106200000
steps:
  - si_mar: min(salary, cap_h1) * 0.08
  - hi_mar: min(salary, cap_h1) * 0.015
  - si_jul: min(salary, cap_h2) * 0.08
  - hi_jul: min(salary, cap_h2) * 0.015
  - ui: min(salary, ui_cap) * 0.01
  - employee_mar: si_mar + hi_mar + ui
  - employee_jul: si_jul + hi_jul + ui
  - employer_mar: min(salary, cap_h1) * (0.17 + 0.03 + 0.005) + ui
  - employer_jul: min(salary, cap_h2) * (0.17 + 0.03 + 0.005) + ui
  - employee_increase: employee_jul - employee_mar
  - employer_increase: employer_jul - employer_mar
expected:
  si_mar: 3744000
  hi_mar: 702000
  si_jul: 4048000
  hi_jul: 759000
  ui: 800000
  employee_mar: 5246000
  employee_jul: 5607000
  employer_mar: 10394000
  employer_jul: 11173000
  employee_increase: 361000
  employer_increase: 779000
```

## Ask the client first

1. Monthly contract salary and regular allowances, by month.
2. Nationality, contract type and length, and any secondment or totalisation agreement.
3. Workplace region (I to IV) for the minimum wage floor and unemployment insurance cap.
4. Whether the employee is resident for PIT and how many dependants are registered.
5. Payment cycle and eligibility for any 3 or 6 month cycle.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Decree 73/2024 Art. 3, base salary from 1 July 2024 | https://congbao.chinhphu.vn/tai-ve-van-ban-so-73-2024-nd-cp-42169-50685?format=pdf | 2026-11-26 |
| Read for the consolidated Social Insurance Law 41/2024/QH15 (VBHN 19/VBHN-VPQH, February 2026): Art. 31 contribution salary floor and cap, Art. 32 rates, Art. 33 employee 8%, Art. 34 employer 3% and 14% and payment deadlines | https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/5/468972-1772691642_v1_1772691941_signed.pdf | 2026-11-14 |
| Read for the base salary rise to VND 2,530,000 from 1 July 2026 (Decree 161/2026) and the cap of 50,600,000 | https://xaydungchinhsach.chinhphu.vn/tu-1-7-nhieu-khoan-tro-cap-bhxh-thay-doi-the-nao-khi-luong-co-so-tang-119260523163024829.htm | 2026-11-14 |
| Read for Decree 188/2025 health insurance rate of 4.5%, two thirds employer and one third employee | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-188-2025-nd-cp-quy-dinh-moi-ve-doi-tuong-muc-dong-muc-ho-tro-dong-bao-hiem-y-te-119250711175642187.htm | 2026-11-14 |
| Read for the Employment Law unemployment insurance rates (up to 1% each) | https://xaydungchinhsach.chinhphu.vn/quy-dinh-muc-dong-bao-hiem-that-nghiep-119250711175950882.htm | 2026-11-14 |
| Read for Decree 293/2025 regional minimum wages from 1 January 2026 | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-293-2025-nd-cp-quy-dinh-muc-luong-toi-thieu-doi-voi-nguoi-lao-dong-lam-viec-theo-hop-dong-lao-dong-119251110172808433.htm | 2026-11-14 |
| Read for the Decree 252/2026 withholding return deadlines | https://xaydungchinhsach.chinhphu.vn/quy-dinh-thoi-han-nop-ho-so-khai-thue-119260703120801722.htm | 2026-11-14 |
| Read for Law 108/2025/QH15 Art. 16(2)(a) late payment interest | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf | 2026-11-14 |
| Law 51/2024/QH15, employee health insurance coverage | https://congbao.chinhphu.vn/tai-ve-van-ban-so-51-2024-qh15-43559-53646?format=pdf | 2026-11-26 |
| Consolidated Decree 58/2020 Arts. 4–5, occupational accident and disease insurance rates | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/05-vbhn-bnv.pdf | 2026-11-26 |
| Employment Law 74/2025 Arts. 2 and 31–34, unemployment insurance coverage and wage cap | https://congbao.chinhphu.vn/tai-ve-van-ban-so-74-2025-qh15-45562-57700?format=pdf | 2026-11-26 |
| Decree 374/2025 Art. 4, unemployment insurance rates | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/27/cong-bao-so-48-ngay-23-01-46946signed-17694874955991619007433.pdf | 2026-11-26 |
| Decree 253/2026 Art. 50, PIT withholding from 1 July 2026 | https://xaydungchinhsach.chinhphu.vn/quy-dinh-moi-ve-khau-tru-thue-thu-nhap-ca-nhan-119260703150410707.htm | 2026-11-26 |
| Finance Ministry consolidation 02/VBHN-BTC Art. 25, earlier PIT withholding rules | https://congbao.chinhphu.vn/tai-ve-van-ban-so-02-vbhn-btc-41029-48282?format=pdf | 2026-11-26 |

Not yet confirmed: a case-specific social insurance fine or treaty exemption without the facts of the offence or assignment.
