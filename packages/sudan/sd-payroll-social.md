---
name: sd-payroll-social
description: Use this skill whenever asked about Sudanese payroll, social insurance contributions (NSIF), employer withholding obligations, PAYE remittance, and employee/employer contribution rates. Trigger on phrases like "Sudan payroll", "Sudan social insurance", "NSIF contribution", "Sudan employer taxes", "ضمان اجتماعي السودان", "Sudan PAYE", or any request to compute or review Sudanese payroll deductions. ALWAYS read this skill before touching any Sudan payroll or social insurance work.
version: 0.1
jurisdiction: SD
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sudan Payroll & Social Contributions Skill v0.1

## Sudan Payroll & Social Contributions Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Currency note:** All figures are in Sudanese Pounds (SDG — ج.س). Exchange rate reference: US$1.00 = SDG 47 (SSA 2019 data — verify current rate). Sudan has undergone multiple currency redenominations; verify current SDG values before filing.

## Section 1 — Scope statement

This skill covers:

- National Social Insurance Fund (NSIF) contribution rates for employers and employees
- Employment income tax (PAYE) withholding mechanics
- Monthly remittance deadlines for both PAYE and NSIF
- Sickness, maternity, and work injury benefits framework
- Severance pay (unemployment) rules under the labor code
- Self-employed and voluntary social insurance contributions
- Record-keeping and compliance requirements

This skill does NOT cover:

- Personal income tax computation (brackets, allowances) — see `sd-income-tax`
- Corporate income tax — see `sd-corporate-income-tax`
- VAT — see `sd-vat-gst`
- Company formation — see `sd-company-formation`

## Section 2 — Social insurance framework

### Regulatory framework

**Regulatory framework**  _(SSA Social Security Worldwide; ILO Social Protection)_

| Item | Detail | Source |
| --- | --- | --- |
| **First laws** | 1919 (pensions ordinance); 1974 (social insurance) | SSA Social Security Worldwide |
| **Current law** | 2016 (social insurance) — consolidating prior legislation | SSA Social Security Worldwide |
| **Administering body** | National Pensions and Social Insurance Fund (NPSIF / NSIF) | SSA; ILO Social Protection |
| **Supervising ministry** | Ministry of Insurance and Social Development | SSA Social Security Worldwide |
| **Program type** | Social insurance system (old age, disability, survivors, sickness, maternity, work injury) | SSA Social Security Worldwide |

### Coverage

- Public- and private-sector employees
- Self-employed persons (voluntary)
- Citizens of Sudan working abroad (voluntary coverage)
- **Exclusions:** Household workers, family labor, home-based workers, farmers, foresters, unpaid apprentices
- Special systems for judges and military/police personnel

**AUDIT FLASH POINT:** Excluded categories (household workers, agricultural labor) are commonly miss-classified. Verify actual job classification against the NSIF exclusion list before computing contributions.

## Section 3 — Contribution rates and thresholds

### Old Age, Disability, and Survivors (pension)

**Old Age, Disability, and Survivors (pension) contribution rates**  _(SSA Social Security Worldwide — Sudan; NSIF regulations)_

| Contributor | Rate | Source |
| --- | --- | --- |
| **Employer** | **17%** of gross monthly payroll (including cost-of-living, travel, and accommodation allowances) | SSA Social Security Worldwide — Sudan |
| **Employee** | **8%** of gross monthly earnings (including cost-of-living, travel, and accommodation allowances) | SSA Social Security Worldwide — Sudan |
| **Self-employed** | **25%** of monthly declared earnings (also finances work injury benefits) | SSA Social Security Worldwide — Sudan |
| **Voluntarily insured (Sudanese working abroad)** | **23%** of declared earnings | SSA Social Security Worldwide — Sudan |
| **Total (employer + employee, standard)** | **25%** of gross salary | NSIF regulations; confirmed by SSA |

### Contribution wage base

**Contribution wage base**  _(SSA Social Security Worldwide (2019 data — verify current))_

| Item | Amount (SDG) | Source |
| --- | --- | --- |
| **Minimum monthly earnings for contribution** | SDG 1,500 | SSA Social Security Worldwide (2019 data — verify current) |
| **Maximum monthly earnings for contribution** | SDG 20,000 | SSA Social Security Worldwide (2019 data — verify current) |

**AUDIT FLASH POINT:** The SDG 1,500 minimum and SDG 20,000 maximum figures are from 2019 SSA data. Sudan's currency redenominations and inflation mean these thresholds have likely changed. Verify current NSIF circular before computing.

### Sickness and Maternity

**Sickness and Maternity contribution rates**  _(SSA; National Health Insurance Fund; Labor code 1997)_

| Contributor | Rate | Source |
| --- | --- | --- |
| **Employee (medical insurance)** | 4% of gross earnings | SSA; National Health Insurance Fund |
| **Employer (medical insurance)** | 6% of gross payroll | SSA; National Health Insurance Fund |
| **Employer (cash benefits)** | 100% of cost (employer liability system) | SSA; Labor code 1997 |

### Work Injury

**Work Injury contribution rates**  _(SSA Social Security Worldwide)_

| Contributor | Rate | Source |
| --- | --- | --- |
| **Employee** | 0% (none) | SSA Social Security Worldwide |
| **Employer** | Included in the 17% pension contribution (employer contributions also finance work injury) | SSA Social Security Worldwide |
| **Self-employed** | Included in the 25% contribution | SSA Social Security Worldwide |

## Section 4 — PAYE withholding

### Employment income tax (PAYE)

**Employment income tax (PAYE)**  _(Income Tax Act 1986; tax.gov.sd; Britacom)_

| Item | Rule | Source |
| --- | --- | --- |
| **Mechanism** | Employer withholds income tax at progressive rates from salaries | Income Tax Act 1986; tax.gov.sd |
| **Remittance deadline** | On or before the **15th of the month following deduction** | Income Tax Act 1986; tax.gov.sd |
| **Progressive rates** | 5% – 15% (resident); 20% (non-resident, fringe benefits) | Income Tax Act 1986; see `sd-income-tax` |
| **Personal allowance** | SDG 3,000 (verify current value) | Income Tax Act 1986; Britacom |

### Employer monthly payroll obligations

**Employer monthly payroll obligations**  _(Income Tax Act 1986; NSIF; NHIF)_

| Obligation | Rate | Remittance deadline |
| --- | --- | --- |
| PAYE income tax withholding | Progressive 5%-15% of employee gross salary | 15th of following month |
| NSIF employer pension contribution | 17% of gross monthly payroll | Monthly (verify exact date) |
| NSIF employee pension contribution (withheld) | 8% of gross monthly earnings | Monthly (verify exact date) |
| Health insurance (employer) | 6% of gross payroll | Monthly (verify exact date) |
| Health insurance (employee, withheld) | 4% of gross earnings | Monthly (verify exact date) |

**Total employer cost above gross salary:** 17% (pension) + 6% (health) = **23%** of gross payroll

**Total employee deductions:** 8% (pension) + 4% (health) + PAYE (5%-15%) = **17%-27%** of gross earnings

### NSIF contribution remittance

Employers must register with the NSIF, deduct employee contributions from wages, and remit both employer and employee shares **monthly**. Failure to remit or register can result in penalties and legal consequences.

**AUDIT FLASH POINT:** NSIF remittance deadline is monthly but the exact date (15th vs end-of-month) should be confirmed against current NSIF regulations. Some sources reference monthly without specifying a date.

## Section 5 — Benefit calculations

### Old-age pension

**Old-age pension**  _(SSA)_

| Item | Rule | Source |
| --- | --- | --- |
| **Retirement age** | 65 (normal); reduced for arduous work | SSA |
| **Early pension** | Age 50 with at least 20 years of contributions (any age if involuntarily unemployed due to economic factors) | SSA |
| **Minimum contributions** | 20 years for old-age pension | SSA |
| **Pension formula** | 2% of average monthly earnings (last 3 years) for every 12 months of contributions | SSA |
| **Minimum pension** | 40% of average monthly earnings (last 3 years) | SSA |
| **Maximum pension** | 83.33% of average monthly earnings (last 3 years) | SSA |
| **Early pension reduction** | -15% if aged 50-54; -10% if aged 55-59 | SSA |

### Disability pension

- 50% of average monthly earnings (last 3 years before disability) OR 2% per 12 months of contributions, whichever is greater
- Maximum: 83.33% of average monthly earnings
- No minimum qualifying period

### Survivor pension

- Spouse: 30% of deceased's pension (50% if orphan/parent eligible; 75% if no orphan/parent but other survivors; 100% if no other survivors)
- Orphan: 40% split equally (split among eligible orphans)
- Parents: 30% (50% if widow/orphan eligible)
- Maximum combined survivor pension: 100% of deceased's pension

### Death grant

- Lump sum of **4x average monthly earnings** (last 3 years before death) if insured at time of death
- **2 months** of pension if deceased was a pensioner

### Sickness benefit (employer liability)

- First 3 months: 100% of last monthly earnings
- Next 3 months: 50%
- Up to 3 additional months: 25%
- Thereafter: unpaid sick leave

### Maternity benefit (employer liability)

- 100% of last monthly earnings for **8 weeks** (must have at least 6 months employment)

### Severance pay (unemployment, labor code 1997)

**Severance pay (unemployment, labor code 1997)**  _(Labor code 1997)_

| Years of service | Severance |
| --- | --- |
| 3 – 9 years | 1 month's basic earnings per year |
| 10 – 14 years | 1.5 months' basic earnings per year |
| 15+ years | 1.75 months' basic earnings per year |
| Maximum | 36 months of basic monthly earnings |

## Section 6 — Worked examples

### Example 1 — Standard employee payroll

**Example 1 — Standard employee payroll (Gross monthly salary SDG 25,000)**

| Item | Amount (SDG) | Rate |
| --- | --- | --- |
| Gross salary | 25,000 | — |
| NSIF employee pension (8%) | -2,000 | 8% |
| Health insurance employee (4%) | -1,000 | 4% |
| PAYE (estimate at ~12% effective) | -3,000 | ~12% (verify bracket) |
| **Net pay** | **19,000** | — |
|  |  |  |
| Employer NSIF (17%) | +4,250 | 17% |
| Employer health insurance (6%) | +1,500 | 6% |
| **Total employer cost** | **30,750** | — |

*Flag: PAYE estimate requires confirmed bracket schedule. NSIF wage base capped at SDG 20,000 may reduce the actual contribution base — verify current cap.*

### Example 2 — NSIF contribution with wage cap

**Example 2 — NSIF contribution with wage cap (Gross monthly salary SDG 35,000)**

| Item | Amount (SDG) | Calculation |
| --- | --- | --- |
| NSIF employer contribution | 3,400 | 20,000 x 17% |
| NSIF employee contribution | 1,600 | 20,000 x 8% |
| Excess salary (35,000 - 20,000) | 15,000 | No NSIF contribution |
| PAYE on full salary | Computed on 35,000 | No wage cap for PAYE |

### Example 3 — Self-employed social insurance

**Scenario:** Self-employed person declaring monthly earnings of SDG 18,000.

- Monthly NSIF contribution: 18,000 x 25% = **SDG 4,500**
- This covers pension, disability, survivors, AND work injury
- Minimum contribution base: SDG 1,500 (verify current)
- Maximum contribution base: SDG 20,000 (verify current)

### Example 4 — Severance calculation

**Scenario:** Employee with 12 years of service, basic monthly salary SDG 20,000.

- Years 3-9 (7 years): 7 x 20,000 = SDG 140,000
- Years 10-12 (3 years): 3 x 1.5 x 20,000 = SDG 90,000
- Total severance: SDG 230,000

## Section 7 — Record-keeping and compliance

### Employer record requirements

**Employer record requirements**

| Record type | Retention |
| --- | --- |
| Individual employee records (name, ID, contract date, salary, deductions, contributions) | 5-7 years minimum |
| Monthly payroll registers | 5-7 years |
| Tax withholding documentation | 5-7 years |
| Social contribution records (NSIF + health insurance) | 5-7 years |
| Supporting documents (employment contracts, ID documents, authorization letters) | Duration of employment + 5-7 years |

### Registration requirements

1. **Employer NSIF registration:** Register with the National Social Insurance Fund before commencing employment
2. **Tax registration:** Register with the Sudan Taxation Chamber for income tax withholding
3. **Health insurance:** Register with the National Health Insurance Fund (NHIF)
4. **Labor office:** Register with the Ministry of Labor

### Penalties for non-compliance

- Late payment penalties: percentage-based on unpaid amounts plus interest
- Administrative fines: for late filing, incomplete returns, missing documentation
- Legal consequences: potential criminal prosecution for serious violations or repeated non-compliance
- Operational restrictions: license suspension or business closure for severe violations
- Back payment requirements: employer remains liable for unpaid contributions + accumulated penalties

## Section 8 — Audit flash points

1. **Wage base cap:** The SDG 20,000 maximum contribution base (2019 figure) likely no longer reflects current SDG values due to inflation and redenomination. Verify current NSIF circular.
2. **"Gross salary" definition:** Includes cost-of-living, travel, and accommodation allowances — not just basic salary. This materially affects contribution amounts.
3. **Excluded worker categories:** Household workers, agricultural laborers, and family labor are excluded from NSIF. Misclassification is a common audit finding.
4. **NSIF vs NHIF:** Pension contributions go to NSIF (National Pensions and Social Insurance Fund); health insurance contributions go to NHIF (National Health Insurance Fund). Do not confuse the two.
5. **Employer liability for cash sickness/maternity:** The employer pays cash sickness and maternity benefits directly — this is above the NSIF contribution rate, not part of it.
6. **Confusion with South Sudan:** Some sources congregate Sudan and South Sudan (which became independent in 2011). Verify all rates apply to Sudan (Khartoum), not South Sudan (Juba).

## Section 9 — Self-checks

Before delivering output, verify:

- [ ] Employer and employee NSIF rates correctly stated (17% / 8%)
- [ ] Wage base min/max (SDG 1,500 / 20,000) verified against current NSIF circular
- [ ] "Gross salary" includes allowances (cost-of-living, travel, accommodation)
- [ ] PAYE progressive rates applied correctly (5%-15% resident, 20% non-resident)
- [ ] PAYE remittance deadline (15th of following month) stated
- [ ] NSIF and NHIF contributions distinguished correctly
- [ ] Health insurance rates (4% employee / 6% employer) applied
- [ ] Excluded worker categories checked
- [ ] Severance calculation uses correct tier (1x / 1.5x / 1.75x per service band)
- [ ] Record retention period (5-7 years) communicated

## Section 10 — Reference material

**Reference material**  _(Section 10 — Reference material)_

| Resource | Reference |
| --- | --- |
| Sudan Taxation Chamber — Income Tax | https://tax.gov.sd/en/income-tax-2/ |
| SSA Social Security Worldwide — Sudan | https://www.ssa.gov/policy/docs/progdesc/ssptw/2018-2019/africa/sudan.html |
| ILO Social Protection — Sudan | https://www.social-protection.org/gimi/ShowCountryProfile.action?iso=SD |
| National Health Insurance Fund (NHIF) Sudan | http://www.nhif.gov.sd/ |
| Britacom tax profile — Sudan | https://www.britacom.org/zt/BRPolicies/Sudan/ |
| Africarrieres — Employer Taxes Sudan | https://africarrieres.com/sudan/en/guide/employeur-entreprise/employer-taxes |

## PROHIBITIONS

- Do NOT confuse Sudan (Khartoum) with South Sudan (Juba) — separate jurisdictions with different tax systems since 2011.
- Do NOT apply NSIF contribution rates without verifying the current wage base cap — the SDG 20,000 figure is from 2019 and likely outdated.
- Do NOT compute employer total cost without including both NSIF (17%) and NHIF (6%).
- Do NOT omit employer liability for cash sickness/maternity benefits (separate from contribution rates).
- Do NOT present payroll figures as final without flagging "verify current value" for SDG thresholds.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

**Sources:** Social Insurance Act 2016 (Sudan); SSA Social Security Programs Throughout the World — Sudan 2019; Income Tax Act 1986; ILO Social Protection; Britacom; Africarrieres.

> Contributed by Ahmed Hassan.

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
