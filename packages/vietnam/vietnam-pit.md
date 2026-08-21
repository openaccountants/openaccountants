---
name: vietnam-pit
description: Use this skill whenever asked about Vietnam personal income tax (thuế thu nhập cá nhân / TNCN) for resident individuals, self-employed persons, or sole proprietors. Trigger on phrases like "thuế TNCN", "Vietnam income tax", "thuế thu nhập cá nhân", "giảm trừ gia cảnh", "biểu thuế lũy tiến", "progressive tax Vietnam", "personal deduction Vietnam", "dependent deduction Vietnam", "PIT Vietnam", or any question about computing or filing personal income tax in Vietnam. Covers the 2026 five-bracket progressive rate schedule (Luật số 109/2025/QH15), personal and dependent deductions, and filing obligations. ALWAYS read this skill before touching any Vietnam PIT work.
version: 1.0
jurisdiction: VN
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Vietnam Pit

## Vietnam Personal Income Tax (Thuế Thu Nhập Cá Nhân / TNCN) v1.0

## Section 1 — Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Vietnam (Cộng hòa Xã hội chủ nghĩa Việt Nam) |
| Tax | Thuế Thu Nhập Cá Nhân (TNCN — Personal Income Tax / PIT) |
| Currency | VND (Vietnamese Dong / đồng) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Primary legislation | Luật Thuế Thu Nhập Cá Nhân No. 04/2007/QH12 (amended); Luật số 109/2025/QH15 (effective 01/01/2026) |
| Tax authority | Tổng cục Thuế (General Department of Taxation — GDT) |
| Filing portal | etax.gdt.gov.vn / thuedientu.gdt.gov.vn |
| Filing deadline | Annual finalisation: 31 March of following year |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Vietnam-licensed tax agent (đại lý thuế) or CPA |
| Skill version | 1.0 |

## Section 2 — Progressive Tax Brackets (Biểu Thuế Lũy Tiến Từng Phần) — 2026

Effective 01/01/2026, Vietnam moved from a 7-bracket to a **5-bracket** progressive tax system under Luật số 109/2025/QH15.

### Monthly rates (applied to taxable income per month)

**Monthly rates table**  _(Luật số 109/2025/QH15; googlesky/thue-2026 (MIT); thangtd-0050/pit)_

| Bracket | Monthly Taxable Income (VND) | Rate |
| --- | --- | --- |
| 1 | ≤ 10,000,000 | 5% |
| 2 | 10,000,001 – 30,000,000 | 15% |
| 3 | 30,000,001 – 60,000,000 | 25% |
| 4 | 60,000,001 – 100,000,000 | 30% |
| 5 | > 100,000,000 | 35% |

### Annual rates (applied to taxable income per year)

**Annual rates table**  _(Luật số 109/2025/QH15; googlesky/thue-2026 (MIT); thangtd-0050/pit)_

| Bracket | Annual Taxable Income (VND) | Rate |
| --- | --- | --- |
| 1 | ≤ 120,000,000 | 5% |
| 2 | 120,000,001 – 360,000,000 | 15% |
| 3 | 360,000,001 – 720,000,000 | 25% |
| 4 | 720,000,001 – 1,200,000,000 | 30% |
| 5 | > 1,200,000,000 | 35% |

### Quick tax computation table (monthly)

**Quick tax computation table**

| If taxable income/month (VND) | Tax = |
| --- | --- |
| ≤ 10,000,000 | Income × 5% |
| 10,000,001 – 30,000,000 | 500,000 + (Income − 10,000,000) × 15% |
| 30,000,001 – 60,000,000 | 3,500,000 + (Income − 30,000,000) × 25% |
| 60,000,001 – 100,000,000 | 11,000,000 + (Income − 60,000,000) × 30% |
| > 100,000,000 | 23,000,000 + (Income − 100,000,000) × 35% |

## Section 3 — Deductions (Giảm Trừ Gia Cảnh) — 2026

### Personal and dependent deductions

**Personal and dependent deductions table**  _(Luật số 109/2025/QH15; googlesky/thue-2026 (MIT))_

| Deduction | Monthly (VND) | Annual (VND) | Notes |
| --- | --- | --- | --- |
| Personal deduction (giảm trừ bản thân) | 15,500,000 | 186,000,000 | Per taxpayer; automatic |
| Dependent deduction (giảm trừ người phụ thuộc) | 6,200,000 per dependent | 74,400,000 per dependent | Must register dependents with tax authority |

- **Previous values (pre-2026)** — Personal deduction was 11,000,000/month; dependent deduction was 4,400,000/month. The 2026 increase reflects Resolution 954/2020/UBTVQH14's CPI-triggered adjustment mechanism enacted via Luật số 109/2025/QH15.  _(Nghị quyết 954/2020/UBTVQH14; Luật số 109/2025/QH15)_

### Other deductions

**Other deductions table**

| Deduction | Amount | Notes |
| --- | --- | --- |
| Compulsory social insurance (BHXH) | 8% of salary | Employee's share — deducted before PIT |
| Compulsory health insurance (BHYT) | 1.5% of salary | Employee's share — deducted before PIT |
| Unemployment insurance (BHTN) | 1% of salary | Employee's share — deducted before PIT |
| Voluntary pension fund | Up to 1,000,000/month | If contributing to qualified fund |
| Charitable contributions | Actual amount | Donations to approved organisations only |

### Taxable income formula

- **Taxable Income formula** — Taxable Income = Gross Income − Compulsory insurance (BHXH + BHYT + BHTN) − Personal deduction (15,500,000/month) − Dependent deductions (6,200,000 × number of registered dependents/month) − Other allowable deductions

## Section 4 — Resident vs Non-Resident

**Resident vs Non-Resident table**

| Status | Definition | Tax treatment |
| --- | --- | --- |
| Tax resident | Present in Vietnam ≥ 183 days in a calendar year OR 12 consecutive months; OR has a regular abode in Vietnam | Worldwide income; progressive rates (Section 2) |
| Non-resident | Does not meet resident criteria | Vietnam-sourced income only; flat 20% on employment income |

## Section 5 — Income Categories (Các Khoản Thu Nhập Chịu Thuế)

**Income Categories table**

| Category | Rate | Notes |
| --- | --- | --- |
| Employment income (tiền lương, tiền công) | Progressive 5-bracket (Section 2) | Main category for salaried individuals |
| Business income (kinh doanh) | Progressive 5-bracket OR deemed rates | Self-employed / sole proprietors |
| Capital gains (chuyển nhượng vốn) | 20% on gains | Or 0.1% of transfer value for listed securities |
| Securities transfer | 0.1% of sale proceeds | Regardless of gain/loss |
| Real estate transfer (chuyển nhượng bất động sản) | 2% of transfer price | No deduction of cost basis |
| Royalties, franchises | 5% above VND 10,000,000 per contract |  |
| Lottery / prizes (trúng thưởng) | 10% above VND 10,000,000 |  |
| Inheritance / gifts | 10% above VND 10,000,000 |  |

### Deemed tax rates for business income (self-employed individuals)

**Deemed tax rates table**

| Business activity | Revenue tax rate |
| --- | --- |
| Distribution / supply of goods | 0.5% |
| Services, construction (excl. materials) | 2% |
| Manufacturing, transport, services with goods | 1.5% |
| Other business activities | 1% |

- **Small business PIT exemption** — Self-employed individuals with revenue < VND 100,000,000/year are exempt from PIT on business income.

## Section 6 — Filing and Payment

### Withholding (Khấu Trừ Tại Nguồn)

- **Employer withholding deadlines** — Employers withhold PIT monthly from employee salaries and remit to GDT by the 20th of the following month (monthly filers) or 30th of the month following the quarter (quarterly filers).

### Annual finalisation (Quyết Toán Thuế)

**Annual finalisation table**

| Who | Deadline | Notes |
| --- | --- | --- |
| Employers (on behalf of employees) | 31 March of following year | File form 05/QTT-TNCN |
| Individuals self-filing | 31 March of following year | File form 02/QTT-TNCN |
| Individuals with single employer, no additional income | May authorise employer to finalise | No separate filing needed |

### When individual must self-file

- Has income from 2+ sources and total additional tax > VND 100,000
- Receives income not subject to withholding
- Foreign-sourced income (residents only)
- Wishes to claim dependent deductions not registered with employer

## Section 7 — Worked Examples

### Example 1 — Single employee, no dependents

**Facts:** Monthly gross salary VND 40,000,000. No dependents.

**Computation:**
```
Gross salary:                       40,000,000
Less: BHXH (8%):                    -3,200,000
Less: BHYT (1.5%):                    -600,000
Less: BHTN (1%):                      -400,000
Less: Personal deduction:          -15,500,000
                                   -----------
Taxable income:                     20,300,000

Tax:
  First 10,000,000 × 5%  =            500,000
  Next 10,300,000 × 15%  =          1,545,000
                                   -----------
Total PIT/month:                     2,045,000
```

### Example 2 — Employee with 2 dependents

**Facts:** Monthly gross salary VND 60,000,000. Two registered dependents.

**Computation:**
```
Gross salary:                       60,000,000
Less: BHXH (8%):                    -4,800,000
Less: BHYT (1.5%):                    -900,000
Less: BHTN (1%):                      -600,000
Less: Personal deduction:          -15,500,000
Less: Dependent deductions (2×):   -12,400,000
                                   -----------
Taxable income:                     25,800,000

Tax:
  First 10,000,000 × 5%  =            500,000
  Next 15,800,000 × 15%  =          2,370,000
                                   -----------
Total PIT/month:                     2,870,000
```

### Example 3 — High income earner

**Facts:** Monthly gross salary VND 150,000,000. One dependent.

**Computation:**
```
Gross salary:                      150,000,000
Less: BHXH (8%, capped at 36×base): -2,984,000  (cap applies: 8% × 37,300,000)
Less: BHYT (1.5%, capped):            -559,500
Less: BHTN (1%, capped):              -373,000
Less: Personal deduction:          -15,500,000
Less: Dependent deduction (1×):     -6,200,000
                                   -----------
Taxable income (approx):          124,383,500

Tax:
  First 10,000,000 × 5%   =           500,000
  Next 20,000,000 × 15%   =         3,000,000
  Next 30,000,000 × 25%   =         7,500,000
  Next 40,000,000 × 30%   =        12,000,000
  Remaining 24,383,500 × 35% =      8,534,225
                                   -----------
Total PIT/month:                    31,534,225
```

## Section 8 — Conservative Defaults

**Conservative Defaults table**

| Situation | Default Assumption |
| --- | --- |
| Unknown residency status | Treat as resident (progressive rates — higher tax) |
| Unknown number of dependents | Zero dependents (no deduction) |
| Dependent registration unclear | Do not claim deduction |
| Income category unclear | Employment income (progressive rates) |
| Insurance contribution cap unclear | Apply cap at statutory maximum |
| Allowance taxability unclear | Taxable (include in gross income) |
| Business vs employment income unclear | Employment income |

## Section 9 — Red Flag Thresholds

**Red Flag Thresholds table**

| Threshold | Value |
| --- | --- |
| HIGH single month tax discrepancy | VND 10,000,000 |
| HIGH annual under-withholding | VND 50,000,000 |
| MEDIUM unreported income source | Any additional source > VND 2,000,000/month |
| MEDIUM dependent claim without registration | Any amount |
| LOW rounding difference | VND 100,000 |

## Section 10 — Penalties

**Penalties table**

| Offence | Penalty |
| --- | --- |
| Late filing (quyết toán) | VND 2,000,000 – 25,000,000 |
| Late payment | 0.03% per day of unpaid tax |
| Under-declaration (underpayment) | 20% of underpaid amount |
| Tax evasion | 1× – 3× evaded tax + criminal liability |
| Failure to register dependents | Deduction denied + back-tax + interest |

## Section 11 — Exempt Income (Thu Nhập Miễn Thuế)

**Exempt Income table**

| Item | Notes |
| --- | --- |
| Real estate transfer between spouses, parents/children, siblings | Exempt |
| Inheritance/gift between immediate family | Exempt |
| Salary from night shift / dangerous work allowances | Per statutory schedule |
| One-off relocation allowance | Per statutory limits |
| Life insurance proceeds | Exempt |
| Severance pay per labour code | Exempt (up to statutory amount) |
| Interest on bank deposits | Exempt (5% withholding applies separately) |
| Scholarships | Exempt |

## Section 12 — Reference Material

### Key legislation

**Key legislation table**

| Topic | Reference |
| --- | --- |
| PIT Law | Luật Thuế TNCN No. 04/2007/QH12 (amended 2012, 2014) |
| 2026 bracket reform | Luật số 109/2025/QH15 (effective 01/01/2026) |
| Implementation decree | Nghị định 65/2013/NĐ-CP (as amended) |
| Circular guidance | Thông tư 111/2013/TT-BTC (as amended) |
| Deduction adjustment mechanism | Nghị quyết 954/2020/UBTVQH14 |
| Tax administration | Luật Quản lý Thuế No. 38/2019/QH14 |
| Social insurance | Luật BHXH No. 58/2014/QH13 |

### Open-source references

**Open-source references table**

| Repository | License | Scope |
| --- | --- | --- |
| [googlesky/thue-2026](https://github.com/googlesky/thue-2026) | MIT | 2026 PIT brackets and deduction amounts |
| [thangtd-0050/pit](https://github.com/thangtd-0050/pit) | Open source | Vietnam PIT calculator implementation |

### Known gaps

- Foreign tax credit computation for residents with overseas income — escalate
- Transfer pricing adjustments for related-party business income — escalate
- Expatriate tax equalisation — escalate
- Stock option / equity compensation — escalate
- Crypto / digital asset income — uncertain; escalate

### Self-check before finalisation

- [ ] Correct bracket schedule applied (2026 five-bracket system)?
- [ ] Personal deduction at VND 15,500,000/month?
- [ ] Each dependent deduction at VND 6,200,000/month with registration confirmed?
- [ ] Compulsory insurance deducted before applying brackets?
- [ ] Insurance contribution caps applied correctly?
- [ ] All income sources identified and categorised?
- [ ] Withholding reconciled against annual liability?
- [ ] Filing deadline (31 March) noted?

## Section 13 — Changelog

**Changelog table**

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | May 2026 | Initial release with 2026 five-bracket system per Luật số 109/2025/QH15 |

## Prohibitions

- **Prohibitions list** — NEVER apply the old 7-bracket schedule for tax year 2026 onwards; NEVER claim dependent deduction without confirmed registration; NEVER ignore compulsory insurance deductions when computing taxable income; NEVER apply resident rates to a confirmed non-resident; NEVER present calculations as definitive — direct to a licensed Vietnamese tax agent (đại lý thuế)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
