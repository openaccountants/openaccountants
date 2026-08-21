---
name: cyprus-payroll
description: Use this skill whenever asked about Cyprus payroll processing for employed persons. Trigger on phrases like "Cyprus payroll", "PAYE Cyprus", "TD7", "TD63", "TD59", "TD1 Cyprus", "Social Insurance Cyprus", "GESY", "GHS contribution", "Cyprus payslip", "net salary Cyprus", "tax withholding Cyprus", "employer social cost Cyprus", "Redundancy Fund", "HRDA", "Social Cohesion Fund", "Central Holiday Fund", "insurable earnings ceiling Cyprus", "minimum wage Cyprus", "ERGANI", "50% expat exemption Cyprus", "20% new-resident exemption", "TAX FOR ALL", "TFA", "gross to net Cyprus", "salary calculation Cyprus", or any question about computing employee pay, withholding income tax, or social contributions for Cyprus-based employees. This skill covers PAYE income tax withholding, Social Insurance (employee and employer), General Healthcare System (GHS/GESY), the employer-only Redundancy / HRDA / Social Cohesion / Central Holiday funds, the new-resident 20% and 50% income-tax exemptions, minimum wage, and filing obligations. ALWAYS read this skill before processing any Cyprus payroll.
version: 0.1
jurisdiction: CY
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Christos Thoma
review_status: current
depends_on: - payroll-workflow-base
category: payroll
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus Payroll

## Cyprus Payroll Skill v0.1

> Tier 2 (research-verified). Figures below are drawn primarily from Big-4 guides (PwC, KPMG, Andersen) and the Government of Cyprus Business-in-Cyprus portal because the Cyprus Tax Department (tax.gov.cy) and Social Insurance Services (sid.mlsi.gov.cy) authority PDFs were not directly retrievable at research time. A Cyprus-warranted accountant must confirm against the official 2025 tax card and the Social Insurance Services contribution table before sign-off.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Christos Thoma** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### cyprus-payroll

- **PIT band 1 — tax-free threshold (2025)** — 0% on chargeable income EUR 0 – 19,500  _(Cyprus Tax Department; PwC Worldwide Tax Summaries (reviewed 18 May 2026); Income Tax Law N.118(I)/2002)_
- **PIT band 2 — marginal rate (2025)** — 20% on chargeable income EUR 19,501 – 28,000  _(Cyprus Tax Department; PwC Worldwide Tax Summaries (reviewed 18 May 2026))_
- **PIT band 3 — marginal rate (2025)** — 25% on chargeable income EUR 28,001 – 36,300  _(Cyprus Tax Department; PwC Worldwide Tax Summaries (reviewed 18 May 2026))_
- **PIT band 4 — marginal rate (2025)** — 30% on chargeable income EUR 36,301 – 60,000  _(Cyprus Tax Department; PwC Worldwide Tax Summaries (reviewed 18 May 2026))_
- **PIT band 5 — top marginal rate (2025)** — 35% on chargeable income above EUR 60,000  _(Cyprus Tax Department; PwC Worldwide Tax Summaries (reviewed 18 May 2026))_
- **Cumulative tax at top of band 2 (EUR 28,000) — 2025** — EUR 1,700.00  _(Cyprus Tax Department; PwC)_
- **Cumulative tax at top of band 3 (EUR 36,300) — 2025** — EUR 3,775.00  _(Cyprus Tax Department; PwC)_
- **Cumulative tax at top of band 4 (EUR 60,000) — 2025** — EUR 10,885.00  _(Cyprus Tax Department; PwC)_
- **PIT band 1 — tax-free threshold (2026 reform)** — 0% on chargeable income EUR 0 – 22,000  _(Tax Reform Laws approved by Parliament 22 Dec 2025; ITR World Tax)_
- **PIT band 2 — marginal rate (2026 reform)** — 20% on chargeable income EUR 22,001 – 32,000  _(Tax Reform Laws approved by Parliament 22 Dec 2025; ITR World Tax)_
- **PIT band 3 — marginal rate (2026 reform)** — 25% on chargeable income EUR 32,001 – 42,000  _(Tax Reform Laws approved by Parliament 22 Dec 2025; ITR World Tax)_
- **PIT band 4 — marginal rate (2026 reform)** — 30% on chargeable income EUR 42,001 – 72,000  _(Tax Reform Laws approved by Parliament 22 Dec 2025; ITR World Tax)_
- **PIT band 5 — top marginal rate (2026 reform)** — 35% on chargeable income above EUR 72,000  _(Tax Reform Laws approved by Parliament 22 Dec 2025; ITR World Tax)_
- **Cumulative tax at top of band 2 (EUR 32,000) — 2026** — EUR 2,000.00  _(Tax Reform Laws approved by Parliament 22 Dec 2025; ITR World Tax)_
- **Cumulative tax at top of band 3 (EUR 42,000) — 2026** — EUR 4,500.00  _(Tax Reform Laws approved by Parliament 22 Dec 2025; ITR World Tax)_
- **Cumulative tax at top of band 4 (EUR 72,000) — 2026** — EUR 13,500.00  _(Tax Reform Laws approved by Parliament 22 Dec 2025; ITR World Tax)_
- **Employee Social Insurance (SI) contribution rate** — 8.8%  _(PwC; Andersen Cyprus; fixed since 1 Jan 2024 for 5 years)_
- **Employee GHS/GESY contribution rate** — 2.65%  _(PwC; gesy.org.cy)_
- **Total employee contribution rate (SI + GHS, below both ceilings)** — 11.45%  _(PwC; Andersen; gesy.org.cy)_
- **Maximum insurable earnings — annual (2025)** — EUR 66,612  _(KPMG Cyprus; Social Insurance Services)_
- **Maximum insurable earnings — monthly (2025)** — EUR 5,551  _(KPMG Cyprus; Social Insurance Services)_
- **Maximum insurable earnings — weekly (2025)** — EUR 1,281  _(KPMG Cyprus; Social Insurance Services)_
- **Maximum insurable earnings — annual (2024, prior year for reference)** — EUR 62,868  _(KPMG Cyprus; Social Insurance Services)_
- **Maximum insurable earnings — monthly (2024, prior year for reference)** — EUR 5,239  _(KPMG Cyprus; Social Insurance Services)_
- **Maximum insurable earnings — weekly (2024, prior year for reference)** — EUR 1,209  _(KPMG Cyprus; Social Insurance Services)_
- **GHS / GESY employee contribution ceiling — annual** — EUR 180,000 (all income sources combined)  _(PwC; gesy.org.cy)_
- **Employer Social Insurance (SI) contribution rate** — 8.8%  _(PwC; Andersen)_
- **Employer Redundancy Fund contribution rate** — 1.2% of insurable earnings, capped at EUR 66,612/yr  _(businessincyprus.gov.cy; Andersen)_
- **Employer HRDA (Human Resource Development Fund) contribution rate** — 0.5% of insurable earnings, capped at EUR 66,612/yr  _(businessincyprus.gov.cy; Andersen)_
- **Employer GHS/GESY contribution rate** — 2.90% of emoluments, capped at EUR 180,000/yr  _(PwC; gesy.org.cy)_
- **Employer subtotal (SI + Redundancy + HRDA + GHS, capped/standard funds)** — 13.40%  _(businessincyprus.gov.cy; Andersen)_
- **Employer Social Cohesion Fund contribution rate** — 2.0% of total/actual emoluments — NO ceiling  _(businessincyprus.gov.cy; Andersen)_
- **Employer total load below insurable earnings ceiling (excl. Central Holiday Fund)** — 15.40%  _(businessincyprus.gov.cy; Andersen)_
- **Employer Central Holiday Fund contribution rate (conditional — non-exempt employers only)** — 8.0% of emoluments  _(businessincyprus.gov.cy)_
- **Self-employed Social Insurance contribution rate** — 16.6% of notional/deemed insurable earnings by occupational category  _(Andersen; KPMG; cyprustaxlife (effective 1 Jan 2024))_
- **Self-employed GHS/GESY contribution rate** — 4.00% of earnings, capped at EUR 180,000/yr (max ~EUR 7,200/yr)  _(PwC; gesy.org.cy)_
- **GHS/GESY rate for pensioners / rent, interest, dividend earners** — 2.65% of income, capped at EUR 180,000/yr (max EUR 4,770/yr)  _(PwC; gesy.org.cy)_
- **GHS / GESY annual ceiling (all contributor types)** — EUR 180,000/yr  _(PwC; gesy.org.cy)_
- **Minimum wage — first 6 months of employment (2025)** — EUR 900/month (gross)  _(Cyprus Government; in force since 1 Jan 2024)_
- **Minimum wage — after 6 months continuous employment (2025)** — EUR 1,000/month (gross)  _(Cyprus Government; in force since 1 Jan 2024)_
- **Minimum wage — first 6 months of employment (2026)** — EUR 979/month (gross)  _(Cyprus Mail (Dec 2025); amending decree announced 22/23 Dec 2025)_
- **Minimum wage — after 6 months continuous employment (2026)** — EUR 1,088/month (gross)  _(Cyprus Mail (Dec 2025); amending decree announced 22/23 Dec 2025)_
- **20% new-resident exemption — Art. 8(21A) — relief amount** — Lower of 20% of remuneration or EUR 8,550/year  _(Income Tax Law N.118(I)/2002 Art. 8(21A); Harneys; PwC)_
- **20% new-resident exemption — Art. 8(21A) — first-employment eligibility date** — First employment in Cyprus commencing after 26 Jul 2022  _(Income Tax Law N.118(I)/2002 Art. 8(21A); Harneys)_
- **20% new-resident exemption — Art. 8(21A) — prior non-residency requirement** — Not Cyprus-resident for the 3 prior consecutive tax years  _(Income Tax Law N.118(I)/2002 Art. 8(21A); Harneys)_
- **20% new-resident exemption — Art. 8(21A) — duration** — Up to 7 years  _(Income Tax Law N.118(I)/2002 Art. 8(21A); Harneys)_
- **50% new-resident exemption — Art. 8(23A) — relief amount** — 50% of remuneration  _(Income Tax Law N.118(I)/2002 Art. 8(23A); Harneys; PwC)_
- **50% new-resident exemption — Art. 8(23A) — minimum salary threshold** — Annual remuneration must exceed EUR 55,000  _(Income Tax Law N.118(I)/2002 Art. 8(23A); Harneys)_
- **50% new-resident exemption — Art. 8(23A) — first-employment eligibility date** — First employment in Cyprus from 1 Jan 2022  _(Income Tax Law N.118(I)/2002 Art. 8(23A); Harneys)_
- **50% new-resident exemption — Art. 8(23A) — prior non-residency requirement** — Not Cyprus-resident for 15 consecutive years prior  _(Income Tax Law N.118(I)/2002 Art. 8(23A); Harneys)_
- **50% new-resident exemption — Art. 8(23A) — duration** — 17 consecutive years  _(Income Tax Law N.118(I)/2002 Art. 8(23A); Harneys)_
- **Monthly TD7 — mandatory start date** — From 1 Jan 2025  _(IBCCS Tax; businessincyprus.gov.cy)_
- **Monthly TD7 — exclusive TFA filing requirement start date** — From 22 Aug 2025 must be filed and paid exclusively through TAX FOR ALL (TFA)  _(IBCCS Tax; Tax Department)_
- **Monthly TD7 — payment due date (from Jan 2026)** — End of the month following the payroll month  _(businessincyprus.gov.cy)_
- **TD7 transitional deadline — Jan–Nov 2025 returns** — Due 31 Dec 2025  _(IBCCS Tax; businessincyprus.gov.cy)_
- **TD7 transitional deadline — Dec 2025 return** — Due 31 Jan 2026  _(IBCCS Tax; businessincyprus.gov.cy)_
- **TD1 personal income tax return — annual deadline** — 31 July of the year following the tax year (electronically via TFA)  _(Cyprus Tax Department)_
- **ERGANI hire-notification deadline** — No later than one day before commencement of employment  _(ergani.mlsi.gov.cy)_
- **Employer registration form** — Form YKA 01-001 — before first hire  _(Social Insurance Services)_
- **Employee TIN mandatory on TD7** — Mandatory on every monthly and annual TD7 from tax year 2025, regardless of income level  _(Cyprus Tax Department)_
- **Personal income tax filing threshold (TD1)** — Gross annual income exceeds EUR 19,500 (2025)  _(PwC; Cyprus Tax Department)_
- **Late payment interest rate on overdue tax/contributions** — 3.50% per annum for amounts due from 1 January 2026 (2025: 5.50%; 2024: 5.00%).  _(https://www.mof.gov.cy/mof/tax/taxdep.nsf/page26_en/page26_en?opendocument=)_
- **PAYE computation method — SI and GHS deductibility** — Employee SI (8.8%) and GHS (2.65%) contributions are deductible before computing the PAYE income-tax base  _(PwC)_
- **SI/GHS coverage — de minimis threshold** — Applies from the first euro of employment income; no de minimis  _(Social Insurance Services)_
- **Social Cohesion Fund — ceiling** — NO ceiling — computed on total actual emoluments  _(businessincyprus.gov.cy; Andersen)_
- **Tax year** — Calendar year: 1 January – 31 December  _(Cyprus Tax Department)_
- **2026 PIT reform — Parliament approval date** — 22 Dec 2025  _(ITR World Tax)_
- **Maximum insurable earnings — annual (2026)** — EUR 68,904  _(KPMG Cyprus; Social Insurance Services; PwC Worldwide Tax Summaries)_
- **Maximum insurable earnings — monthly (2026)** — EUR 5,742  _(KPMG Cyprus; Social Insurance Services; PwC Worldwide Tax Summaries)_
- **Maximum insurable earnings — weekly (2026)** — EUR 1,325  _(KPMG Cyprus; Social Insurance Services; PwC Worldwide Tax Summaries)_

### Tax rates

- **Maximum insurable earnings — annual (2026)** — EUR 68,904  _(KPMG Cyprus; Social Insurance Services; PwC Worldwide Tax Summaries)_
- **Maximum insurable earnings — monthly (2026)** — EUR 5,742  _(KPMG Cyprus; Social Insurance Services; PwC Worldwide Tax Summaries)_
- **Maximum insurable earnings — weekly (2026)** — EUR 1,325  _(KPMG Cyprus; Social Insurance Services; PwC Worldwide Tax Summaries)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Cyprus (Republic of Cyprus) |
| Currency | EUR only |
| Standard pay frequency | Monthly (most common); weekly permitted |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | PAYE -- cumulative monthly withholding on projected annual chargeable income (Income Tax Law N.118(I)/2002) |
| Tax authority | Cyprus Tax Department (Τμήμα Φορολογίας) |
| Social security authority | Social Insurance Services (Υπηρεσίες Κοινωνικών Ασφαλίσεων), Ministry of Labour and Social Insurance |
| Health system authority | Health Insurance Organisation -- General Healthcare System (GHS / GESY) |
| Hire-notification system | ERGANI (ergani.mlsi.gov.cy) |
| Key legislation | Income Tax Law N.118(I)/2002 (PAYE; Art. 8(21A) 20% and Art. 8(23A) 50% exemptions); Social Insurance Law N.59(I)/2010; GHS Law N.89(I)/2001; Termination of Employment Law (Redundancy Fund); Human Resource Development Law (HRDA); Social Cohesion Fund provisions |
| Filing portal | TAX FOR ALL (TFA) -- tax.gov.cy / taxportal.mof.gov.cy |
| Validated by | Pending -- requires sign-off by a Cyprus-warranted accountant |
| Skill version | 0.1 |

## Section 2 -- Income Tax Withholding (PAYE)

The employer withholds income tax monthly under PAYE on a **cumulative basis**: it projects the employee's annual chargeable income, applies the progressive brackets, and spreads the resulting tax evenly across pay periods, adjusting month-by-month. The employee declares allowances and exemptions on **form TD59** at the start of each tax year (or on hiring); the employer issues an annual **TD63 emoluments certificate** after year-end (Income Tax Law N.118(I)/2002; PwC Worldwide Tax Summaries, reviewed 18 May 2026).

There are **no FS4-style status categories** in Cyprus — the same progressive scale applies to every individual regardless of marital status. The 0% band IS the personal allowance; there is no separate married/parent scale.

### Income Tax Rate Table -- 2025 (applies to PAYE for pay periods in calendar 2025)

**Income Tax Rate Table -- 2025**  _(Cyprus Tax Department; PwC Worldwide Tax Summaries (reviewed 18 May 2026))_

| Chargeable Income (EUR) | Marginal Rate | Tax on Band (EUR) | Cumulative Tax at Top of Band (EUR) |
| --- | --- | --- | --- |
| 0 -- 19,500 | 0% | 0 | 0 |
| 19,501 -- 28,000 | 20% | 1,700.00 | 1,700.00 |
| 28,001 -- 36,300 | 25% | 2,075.00 | 3,775.00 |
| 36,301 -- 60,000 | 30% | 7,110.00 | 10,885.00 |
| 60,001 + | 35% | -- | (10,885 + 35% of excess over 60,000) |

Source: Cyprus Tax Department; PwC Worldwide Tax Summaries (reviewed 18 May 2026). Cumulative figures recomputed: 8,500 × 20% = 1,700; 8,300 × 25% = 2,075 (→ 3,775); 23,700 × 30% = 7,110 (→ 10,885).

### Income Tax Rate Table -- 2026 reform (use ONLY for pay periods from 1 Jan 2026)

**Income Tax Rate Table -- 2026 reform**  _(Tax Reform Laws approved by Parliament 22 Dec 2025, effective 1 Jan 2026 (ITR World Tax))_

| Chargeable Income (EUR) | Marginal Rate | Tax on Band (EUR) | Cumulative Tax at Top of Band (EUR) |
| --- | --- | --- | --- |
| 0 -- 22,000 | 0% | 0 | 0 |
| 22,001 -- 32,000 | 20% | 2,000.00 | 2,000.00 |
| 32,001 -- 42,000 | 25% | 2,500.00 | 4,500.00 |
| 42,001 -- 72,000 | 30% | 9,000.00 | 13,500.00 |
| 72,001 + | 35% | -- | (13,500 + 35% of excess over 72,000) |

Source: Tax Reform Laws approved by Parliament 22 Dec 2025, effective 1 Jan 2026 (ITR World Tax). Cumulative recomputed: 10,000 × 20% = 2,000; 10,000 × 25% = 2,500 (→ 4,500); 30,000 × 30% = 9,000 (→ 13,500). **[RESEARCH GAP — reviewer to confirm]** the final published law text for any conditions on the new 2026 family/household reliefs.

### PAYE Computation Method

- **PAYE computation steps** — 1. Project annual chargeable income = annual gross emoluments **minus** deductible employee Social Insurance (8.8%) **minus** deductible employee GHS (2.65%) **minus** any documented new-resident exemption (20% or 50%, see Section 6). 2. Apply the progressive bracket table for the relevant year to that projected chargeable income to get projected annual tax. 3. Divide by the number of pay periods (12 monthly), then adjust cumulatively each period for variations in pay.  _(Income Tax Law N.118(I)/2002)_
- **Deductibility of employee SI and GHS** — Employee SI and GHS contributions ARE deductible before computing the income-tax base  _(PwC; conservative default applied throughout this skill)_

## Section 3 -- Social Contributions -- Employee Deductions

Employee deductions are **Social Insurance 8.8%** + **GHS 2.65%**, each subject to its own ceiling, computed before PAYE.

### Employee Contribution Rates (2025)

**Employee Contribution Rates (2025)**  _(Social Insurance Fund 8.8% fixed since 1 Jan 2024 for 5 years (PwC; Andersen Cyprus); 2025 maximum insurable earnings figures (KPMG Cyprus; Social Insurance Services); GHS employee 2.65% (PwC; gesy.org.cy))_

| Contribution | Rate | Base | Annual Ceiling (EUR) | Monthly Ceiling (EUR) | Weekly Ceiling (EUR) |
| --- | --- | --- | --- | --- | --- |
| Social Insurance Fund (employee) | 8.8% | Insurable earnings | 66,612 | 5,551 | 1,281 |
| General Healthcare System (GHS/GESY) (employee) | 2.65% | Emoluments | 180,000 (all income sources combined) | -- | -- |
| **Total employee contributions (below both ceilings)** | **11.45%** | -- | -- | -- | -- |

Sources: Social Insurance Fund 8.8% fixed since 1 Jan 2024 for 5 years (PwC; Andersen Cyprus). 2025 maximum insurable earnings 66,612/yr (5,551/mo, 1,281/wk), up from 62,868/5,239/1,209 in 2024 (KPMG Cyprus; Social Insurance Services). GHS employee 2.65% capped at 180,000/yr (PwC; gesy.org.cy). Total recomputed: 8.8% + 2.65% = 11.45%. **Plus PAYE income tax on top.**

Note the SI ceiling (66,612) and the GHS ceiling (180,000) differ. For an employee below both ceilings the deductions are a flat 11.45% of gross; above 66,612 the SI portion stops growing while GHS continues up to 180,000.

## Section 4 -- Social Contributions -- Employer Contributions

Employers pay matching Social Insurance and GHS plus three (or four) employer-only funds. Note the **Social Cohesion Fund has NO ceiling** — it is computed on total actual emoluments, not the insurable-earnings cap.

### Employer Contribution Rates (2025)

**Employer Contribution Rates (2025)**  _(businessincyprus.gov.cy; Andersen; PwC; gesy.org.cy)_

| Contribution | Rate | Base | Ceiling (EUR) | Who |
| --- | --- | --- | --- | --- |
| Social Insurance Fund | 8.8% | Insurable earnings | 66,612/yr (5,551/mo, 1,281/wk) | Employer |
| Redundancy Fund | 1.2% | Insurable earnings | 66,612/yr | Employer only |
| Human Resource Development Fund (HRDA) | 0.5% | Insurable earnings | 66,612/yr | Employer only |
| General Healthcare System (GHS/GESY) | 2.90% | Emoluments | 180,000/yr | Employer |
| **Subtotal (capped/standard funds)** | **13.40%** | -- | -- | -- |
| Social Cohesion Fund | 2.0% | **Total / actual emoluments — NO CAP** | None | Employer only |
| **Total employer load (below insurable ceiling)** | **15.40%** | -- | -- | -- |
| Central Holiday Fund (conditional) | 8.0% | Emoluments | Applies only where employer is NOT exempt | Employer only |

Sources: SI 8.8% employer (PwC; Andersen). Redundancy 1.2% + HRDA 0.5% on insurable earnings capped at 66,612 (businessincyprus.gov.cy; Andersen). GHS employer 2.90% capped at 180,000 (PwC; gesy.org.cy). Social Cohesion 2.0% on total actual earnings with no ceiling (businessincyprus.gov.cy; Andersen). Central Holiday Fund 8.0% applies only where the employer does not operate its own approved annual-leave scheme — common in tourism/construction/seasonal sectors (businessincyprus.gov.cy).

**Arithmetic check (employer column):** 8.8 + 1.2 + 0.5 + 2.90 = 13.40 (capped/standard subtotal); + 2.0 (uncapped Social Cohesion) = **15.40%** total load below the insurable-earnings ceiling, excluding the conditional 8.0% Central Holiday Fund.

> The GHS employer rate is occasionally quoted as 2.90%/3.00% in secondary listings; 2.90% is the consistent figure used here. **[RESEARCH GAP — reviewer to confirm]** against gesy.org.cy.

### Combined Employer + Employee Snapshot (below all ceilings)

**Combined Employer + Employee Snapshot**

| Party | Components | Rate of gross |
| --- | --- | --- |
| Employee | SI 8.8% + GHS 2.65% | 11.45% (+ PAYE) |
| Employer (capped funds) | SI 8.8% + Redundancy 1.2% + HRDA 0.5% + GHS 2.90% | 13.40% |
| Employer (uncapped) | Social Cohesion 2.0% | 2.0% |
| Employer total | -- | 15.40% (+ 8.0% Central Holiday Fund if not exempt) |

### Self-Employed (for cross-reference only — not payroll)

**Self-Employed rates**  _(Andersen; KPMG; cyprustaxlife)_

| Contribution | Rate | Base | Ceiling |
| --- | --- | --- | --- |
| Social Insurance (self-employed) | 16.6% | Notional/deemed insurable earnings by occupational category | 66,612/yr (2025) |
| GHS (self-employed) | 4.00% | Earnings | 180,000/yr (max ~7,200/yr) |
| GHS (pensioners / rent, interest, dividend earners) | 2.65% | Income | 180,000/yr (max 4,770/yr) |

Source: self-employed SI rose from 15.6% to 16.6% on 1 Jan 2024, assessed quarterly on deemed earnings (Andersen; KPMG; cyprustaxlife). PwC's page still showed 15.6% at research time; 16.6% is used here per the more recent corroborating sources. **[RESEARCH GAP — reviewer to confirm]** the deemed-income table per occupational category for any self-employed computation. Self-employed contributions are NOT processed through this employer-payroll skill — see a Cyprus self-employed SSC skill.

## Section 5 -- Minimum Wage and Hiring Mechanics

### National Minimum Wage

**National Minimum Wage**  _(Cyprus Mail)_

| Period | First 6 months (EUR/month) | After 6 months continuous employment (EUR/month) |
| --- | --- | --- |
| 2025 (in force since 1 Jan 2024) | 900 | 1,000 |
| 2026 (from 1 Jan 2026) | 979 | 1,088 |

Sources: 2025 minimum wage EUR 1,000/EUR 900 (in force since 1 Jan 2024); 2026 increase to EUR 1,088/EUR 979 announced 22/23 Dec 2025 per amending decree (Cyprus Mail). Minimum wage is full-time gross.

### Hiring and Registration

**Hiring and Registration**

| Step | Detail | Authority |
| --- | --- | --- |
| Employer registration | Register in the Register of Employers (form **YKA 01-001**) before first hire; obtain employer registration number | Social Insurance Services |
| Hire notification | Notify each new hire electronically via **ERGANI** no later than one day before commencement | ergani.mlsi.gov.cy |
| Employee TIN | Mandatory on every monthly and annual TD7 from tax year 2025, regardless of income level | Cyprus Tax Department |

- **No minimum employee count or wage threshold** — There is no minimum employee count or wage threshold for employer SI registration, and SI/GHS coverage applies from the first euro of employment income (no de minimis).

## Section 6 -- New-Resident Income-Tax Exemptions

Cyprus offers two mutually relevant employment-income exemptions. Apply them ONLY when eligibility is documented (residence history + first-employment date + salary threshold).

### 20% Exemption -- Art. 8(21A)

**20% Exemption -- Art. 8(21A)**  _(Income Tax Law N.118(I)/2002 Art. 8(21A))_

| Element | Detail |
| --- | --- |
| Relief | Lower of **20% of remuneration** or **EUR 8,550/year** |
| Eligibility | First employment in Cyprus commencing **after 26 Jul 2022**; individual not Cyprus-resident for the **3 prior consecutive tax years** |
| Duration | Up to **7 years** |

### 50% Exemption -- Art. 8(23A)

**50% Exemption -- Art. 8(23A)**  _(Income Tax Law N.118(I)/2002 Art. 8(23A))_

| Element | Detail |
| --- | --- |
| Relief | **50% of remuneration** |
| Salary threshold | Annual remuneration must exceed **EUR 55,000** |
| Eligibility | First employment in Cyprus from **1 Jan 2022**; not Cyprus-resident for **15 consecutive years** prior |
| Duration | **17 consecutive years** |

Sources: Income Tax Law Art. 8(21A) and Art. 8(23A) (Harneys; PwC). The exemption reduces only the **income-tax (PAYE) base** — it does NOT reduce the Social Insurance or GHS contribution base (those are computed on full emoluments, subject to their own ceilings).

## Section 7 -- Conservative Defaults

When inputs are missing or ambiguous, apply these defaults and flag for the accountant:

1. **Year-correct brackets.** Use the 2025 brackets (0/20/25/30/35% at 19,500 / 28,000 / 36,300 / 60,000) for any pay period in calendar 2025; switch to the 2026 reform brackets (0/20/25/30/35% at 22,000 / 32,000 / 42,000 / 72,000) only for pay periods from 1 Jan 2026 onward.
2. **Employer social cost.** Apply ~15.40% of insurable earnings up to EUR 66,612 (8.8% SI + 1.2% Redundancy + 0.5% HRDA + 2.90% GHS) **plus** 2.0% Social Cohesion on uncapped total earnings; add 8.0% Central Holiday Fund **only** if the employer is not exempt from the statutory annual-leave scheme.
3. **Employee deductions first.** Deduct employee 8.8% SI (capped at 66,612) + 2.65% GHS (capped at 180,000) before computing the taxable PAYE base; both are income-tax deductible.
4. **No exemption unless documented.** Do NOT apply the 20% or 50% new-resident exemption unless the employee's eligibility (residence history + salary threshold + first-employment date) is documented.
5. **Monthly TFA filing.** Assume the employer files monthly TD7 via TAX FOR ALL and remits PAYE + SI + GHS by the end of the month following the payroll month.
6. **No Central Holiday Fund by default.** Treat the 8.0% Central Holiday Fund as NOT applicable unless the engagement confirms the employer is non-exempt (does not run its own approved annual-leave scheme).

## Section 8 -- Required Inputs + Refusal Catalogue

### Required Inputs (refuse to finalise a payroll run without these)

**Required Inputs**

| Input | Why needed |
| --- | --- |
| Pay period and pay date (and calendar year) | Determines whether 2025 or 2026 brackets/ceilings apply |
| Gross emoluments for the period (and annualised) | Base for PAYE projection and all contributions |
| TD59 declaration of allowances/exemptions | Determines the correct PAYE base |
| Employee TIN | Mandatory on TD7 from tax year 2025 |
| Employee SI registration number | Required for SI/GHS reporting |
| Year-to-date gross + PAYE + SI + GHS already withheld | Cumulative PAYE adjustment |
| Whether employer operates its own approved annual-leave scheme | Determines Central Holiday Fund 8.0% applicability |
| New-resident exemption eligibility evidence (if claimed) | Required before applying 20%/50% exemption |

### Refusal Catalogue (stop and ask, do not guess)

- **No TD59 / no confirmation of exemptions** — Refuse; PAYE base is undeterminable.
- **No employee TIN** — Refuse to file TD7; TIN is mandatory from tax year 2025.
- **Exemption claimed without documentation** — Refuse to apply the 20%/50% exemption; default to no exemption.
- **Pay date year unknown** — Refuse; cannot choose 2025 vs 2026 brackets.
- **Central Holiday Fund status unknown** — Flag and exclude the 8.0% by default; do not silently include or exclude without noting it.
- **Self-employed engagement** — Out of scope for this employer-payroll skill; redirect to a Cyprus self-employed SSC skill.

## Section 9 -- Transaction / Payment Pattern Library

Deterministic classification of Cyprus bank-statement lines. Greek and English descriptors both appear.

### Salary Credits (employee side)

**Salary Credits (employee side)**

| Pattern (statement text) | Classification |
| --- | --- |
| MISTHOS, ΜΙΣΘΟΣ, SALARY, PAYROLL | Net salary payment |
| EMPLOYER [name] TRANSFER, WAGES | Net salary payment |
| BONUS, 13TH SALARY, ΔΩΡΟ (gift/13th) | Bonus / 13th-salary payment (taxable) |
| SI REFUND, GESY REFUND | Contribution adjustment — not income |

### Employer Debits (employer side)

**Employer Debits (employer side)**

| Pattern (statement text) | Classification |
| --- | --- |
| TAX DEPARTMENT TD7, TFA PAYMENT, PAYE | PAYE income tax remittance (via TFA) |
| ΚΟΙΝΩΝΙΚΕΣ ΑΣΦΑΛΙΣΕΙΣ, SOCIAL INSURANCE, SIS | Social Insurance + employer-only funds remittance |
| GESY, GHS CONTRIBUTION, ΓΕΣΥ | General Healthcare System remittance |
| REDUNDANCY FUND, HRDA, COHESION FUND | Employer-only fund remittance (usually bundled with SI) |
| CENTRAL HOLIDAY FUND, ΚΕΝΤΡΙΚΟ ΤΑΜΕΙΟ ΑΔΕΙΩΝ | Central Holiday Fund levy (only if non-exempt) |
| NET WAGES, SALARY RUN, PAYROLL BATCH | Salary disbursement to employees |

> Cyprus SI, Redundancy, HRDA and Social Cohesion are typically remitted together to Social Insurance Services; PAYE and (often) GHS are remitted via the Tax Department / TFA. Confirm the actual split with the employer's payment records.

## Section 10 -- Worked Examples

All examples use 2025 brackets and 2025 ceilings unless stated. Figures recomputed end-to-end; rounding to the cent.

### Example 1 -- Standard monthly employee, EUR 2,500/month (annual EUR 30,000)

**Example 1 -- Standard monthly employee, EUR 2,500/month (annual EUR 30,000)**

| Step | Amount (EUR) |
| --- | --- |
| Annual gross emoluments | 30,000.00 |
| Employee SI 8.8% (below 66,612 cap) | 2,640.00 |
| Employee GHS 2.65% | 795.00 |
| Chargeable income (PAYE base) = 30,000 − 2,640 − 795 | 26,565.00 |
| PAYE: 0% to 19,500 = 0; (26,565 − 19,500) × 20% = 7,065 × 20% | 1,413.00 |
| **Net annual** = 30,000 − 2,640 − 795 − 1,413 | **25,152.00** |
| **Net monthly** = 25,152 / 12 | **2,096.00** |

Employer cost: SI 8.8% (2,640) + Redundancy 1.2% (360) + HRDA 0.5% (150) + GHS 2.90% (870) + Social Cohesion 2.0% (600) = **4,620.00/yr**; total employer outlay = 30,000 + 4,620 = **34,620.00/yr** (no Central Holiday Fund assumed).

### Example 2 -- High earner above the SI ceiling, EUR 90,000/year

**Example 2 -- High earner above the SI ceiling, EUR 90,000/year**

| Step | Amount (EUR) |
| --- | --- |
| Annual gross emoluments | 90,000.00 |
| Employee SI 8.8% capped at 66,612 → 66,612 × 8.8% | 5,861.86 |
| Employee GHS 2.65% (below 180,000 cap) | 2,385.00 |
| Chargeable income = 90,000 − 5,861.86 − 2,385 | 81,753.14 |
| PAYE: 10,885 (cumulative to 60,000) + (81,753.14 − 60,000) × 35% = 10,885 + 21,753.14 × 35% (7,613.60) | 18,498.60 |
| **Net annual** = 90,000 − 5,861.86 − 2,385 − 18,498.60 | **63,254.54** |
| **Net monthly** | **5,271.21** |

Employer cost: SI 5,861.86 (capped) + Redundancy 799.34 (66,612 × 1.2%) + HRDA 333.06 (66,612 × 0.5%) + GHS 2,610.00 (90,000 × 2.90%) + Social Cohesion 1,800.00 (90,000 × 2.0%, uncapped) = **11,404.26/yr**; total employer outlay = 90,000 + 11,404.26 = **101,404.26/yr**.

Note how Redundancy/HRDA/SI are frozen at the 66,612 ceiling while GHS and Social Cohesion keep rising with full pay.

### Example 3 -- Minimum-wage employee (after 6 months), EUR 1,000/month (annual EUR 12,000)

**Example 3 -- Minimum-wage employee (after 6 months), EUR 1,000/month (annual EUR 12,000)**

| Step | Amount (EUR) |
| --- | --- |
| Annual gross emoluments | 12,000.00 |
| Employee SI 8.8% | 1,056.00 |
| Employee GHS 2.65% | 318.00 |
| Chargeable income = 12,000 − 1,056 − 318 | 10,626.00 |
| PAYE (10,626 < 19,500, all in 0% band) | 0.00 |
| **Net annual** = 12,000 − 1,056 − 318 − 0 | **10,626.00** |
| **Net monthly** | **885.50** |

Below the EUR 19,500 tax-free band, no PAYE is due; SI + GHS are still mandatory from the first euro.

### Example 4 -- Eligible 50% expat exemption (Art. 8(23A)), EUR 120,000/year

Assume documented eligibility: first employment in Cyprus from 1 Jan 2022, annual remuneration > EUR 55,000, not Cyprus-resident for 15 prior years.

**Example 4 -- Eligible 50% expat exemption (Art. 8(23A)), EUR 120,000/year**

| Step | Amount (EUR) |
| --- | --- |
| Annual gross emoluments | 120,000.00 |
| 50% exemption (income-tax only) | 60,000.00 |
| Taxable emoluments after exemption | 60,000.00 |
| Employee SI 8.8% capped at 66,612 → 66,612 × 8.8% (on full insurable earnings, NOT reduced by exemption) | 5,861.86 |
| Employee GHS 2.65% on full emoluments (120,000, below 180,000 cap) | 3,180.00 |
| PAYE base = 60,000 (taxable emoluments) − 5,861.86 SI − 3,180.00 GHS | 50,958.14 |
| PAYE: 3,775 (cumulative to 36,300) + (50,958.14 − 36,300) × 30% = 3,775 + 14,658.14 × 30% (4,397.44) | 8,172.44 |
| **Net annual** = 120,000 − 5,861.86 − 3,180.00 − 8,172.44 | **102,785.70** |
| **Net monthly** | **8,565.48** |

Key point: the 50% exemption cuts the income-tax base in half but does NOT reduce SI (still capped at 66,612) or GHS (still on full emoluments).

### Example 5 -- Social Cohesion Fund has no ceiling, EUR 80,000/year

**Example 5 -- Social Cohesion Fund has no ceiling, EUR 80,000/year**

| Fund | Base used | Amount (EUR) |
| --- | --- | --- |
| Employer SI 8.8% | min(80,000, 66,612) = 66,612 | 5,861.86 |
| Employer Redundancy 1.2% | 66,612 | 799.34 |
| Employer HRDA 0.5% | 66,612 | 333.06 |
| Employer GHS 2.90% | 80,000 (below 180,000) | 2,320.00 |
| Social Cohesion 2.0% | **80,000 (uncapped)** | 1,600.00 |
| **Total employer funds** | -- | **10,914.26** |

This illustrates the asymmetry: SI/Redundancy/HRDA freeze at 66,612 while Social Cohesion (2.0% × 80,000 = 1,600) is charged on the full salary.

## Section 11 -- Tier 1 Rules (deterministic — apply directly)

- **PAYE withholding basis** — PAYE is withheld monthly on a cumulative basis on projected annual chargeable income  _(Income Tax Law N.118(I)/2002; PwC)_

**2025 PIT brackets**  _(Cyprus Tax Department; PwC, reviewed 18 May 2026)_

| Band | Rate |
| --- | --- |
| to 19,500 | 0% |
| 19,501–28,000 | 20% |
| 28,001–36,300 | 25% |
| 36,301–60,000 | 30% |
| above 60,000 | 35% |

**2026 reform brackets (pay periods from 1 Jan 2026)**  _(Parliament approved 22 Dec 2025; ITR World Tax)_

| Band | Rate |
| --- | --- |
| to 22,000 | 0% |
| 22,001–32,000 | 20% |
| 32,001–42,000 | 25% |
| 42,001–72,000 | 30% |
| above 72,000 | 35% |

- **Employee deductions SI + GHS** — SI 8.8% + GHS 2.65% = 11.45%, each capped separately (SI at 66,612; GHS at 180,000), plus PAYE  _(PwC; Andersen; gesy.org.cy)_
- **2025 maximum insurable earnings** — EUR 66,612/yr, EUR 5,551/mo, EUR 1,281/wk — caps SI, Redundancy and HRDA  _(KPMG Cyprus; Social Insurance Services)_
- **Employer load below the insurable ceiling** — SI 8.8% + Redundancy 1.2% + HRDA 0.5% + GHS 2.90% = 13.40%, plus Social Cohesion 2.0% on uncapped total earnings = 15.40%  _(businessincyprus.gov.cy; Andersen)_
- **Social Cohesion Fund basis** — Social Cohesion Fund 2.0% is computed on TOTAL actual earnings with NO ceiling  _(businessincyprus.gov.cy; Andersen)_
- **Deductibility of SI/GHS before PAYE base** — Employee SI and GHS contributions are deductible before computing the PAYE income-tax base  _(PwC; conservative default)_
- **SI/GHS coverage from first euro** — SI/GHS coverage applies from the first euro of employment income; no de minimis  _(Social Insurance Services)_
- **Employer registration requirement** — Employer must register with Social Insurance Services (form YKA 01-001) before the first hire and notify each new hire via ERGANI at least one day before commencement.
- **Employee TIN mandatory on TD7** — Employee TIN is mandatory on every monthly and annual TD7 from tax year 2025 regardless of income level  _(Cyprus Tax Department)_
- **Monthly TD7 mandatory and TFA filing** — Monthly TD7 is mandatory from 1 Jan 2025 and from 22 Aug 2025 must be filed and paid exclusively through TAX FOR ALL (TFA)  _(IBCCS Tax; Tax Department)_
- **2026 TD7 filing timing** — From Jan 2026, each month's TD7 and the related PAYE/SI/GHS payment are due by the end of the following month  _(businessincyprus.gov.cy)_
- **Minimum wage 2025** — EUR 1,000/month after 6 months' continuous employment, EUR 900/month for the first 6 months (in force since 1 Jan 2024)

## Section 12 -- Tier 2 Catalogue (reviewer judgement required)

These require professional judgement — flag for the Cyprus-warranted accountant rather than auto-deciding:

**Tier 2 Catalogue**

| Topic | Judgement call |
| --- | --- |
| Central Holiday Fund 8.0% | Whether the employer is exempt (runs its own approved annual-leave scheme) — common in seasonal/tourism/construction; affects total employer cost materially. |
| New-resident exemption choice | Whether the 20% (Art. 8(21A)) or 50% (Art. 8(23A)) exemption applies, and which is more favourable given salary and residence history; interaction and election rules. |
| Self-employed deemed earnings | The notional/deemed insurable-earnings category for any self-employed person assessed at 16.6% SI. **[RESEARCH GAP — reviewer to confirm]** the per-occupation table. |
| Benefits in kind | Treatment and valuation of non-cash benefits in the PAYE base. **[RESEARCH GAP — reviewer to confirm]** current BIK rules. |
| 13th-salary / bonus timing | Whether and how a 13th salary or contractual bonus is spread for cumulative PAYE. |
| Late-payment interest rate | The annual public-interest rate (3.50% p.a. from 1 Jan 2026; 2025: 5.50%; 2024: 5.00%) for the year in question. **[RESEARCH GAP — reviewer to confirm]** the current Minister-of-Finance rate. |
| 2026 family/household reliefs | New reliefs under the 2026 reform. **[RESEARCH GAP — reviewer to confirm]** the final law text and any conditions. |

## Section 13 -- Excel Working Paper Template

Recommended columns for a monthly Cyprus payroll working paper (one row per employee):

**Excel Working Paper Template columns**

| Column | Formula / source |
| --- | --- |
| A. Employee name | input |
| B. Employee TIN | input (mandatory for TD7) |
| C. SI registration number | input |
| D. Pay date / period | input (drives 2025 vs 2026 rules) |
| E. Monthly gross emoluments | input |
| F. Annualised gross | = E × 12 |
| G. New-resident exemption (if documented) | = lower of 20% × F or 8,550 (Art. 8(21A)) OR 50% × F (Art. 8(23A)); else 0 |
| H. Employee SI 8.8% | = MIN(F, 66,612) × 8.8% |
| I. Employee GHS 2.65% | = MIN(F, 180,000) × 2.65% |
| J. Annual PAYE base | = F − G − H − I |
| K. Annual PAYE | = bracket function on J (2025 or 2026 table) |
| L. Monthly PAYE | = K / 12 (cumulative-adjusted) |
| M. Monthly net pay | = E − (H/12) − (I/12) − L |
| N. Employer SI 8.8% | = MIN(F, 66,612) × 8.8% |
| O. Employer Redundancy 1.2% | = MIN(F, 66,612) × 1.2% |
| P. Employer HRDA 0.5% | = MIN(F, 66,612) × 0.5% |
| Q. Employer GHS 2.90% | = MIN(F, 180,000) × 2.90% |
| R. Social Cohesion 2.0% | = F × 2.0% (NO cap) |
| S. Central Holiday Fund 8.0% (if non-exempt) | = F × 8.0% else 0 |
| T. Total employer cost | = F + N + O + P + Q + R + S |

Build the bracket function (column K) as a nested IF or a lookup against the correct year's table from Section 2. Always recompute cumulative tax from the band table — do not hard-code per-employee tax.

## Section 14 -- Cyprus Payslip / Statement Reading Guide

Cyprus payslips and bank statements mix Greek and English. Common terms:

**Payslip term glossary**

| Term (Greek / English) | Meaning |
| --- | --- |
| Μισθός / Misthos / Salary | Gross or net salary |
| Κοινωνικές Ασφαλίσεις / Social Insurance / SIS | Social Insurance contribution (8.8% employee / 8.8% employer) |
| ΓΕΣΥ / GESY / GHS | General Healthcare System contribution (2.65% employee / 2.90% employer) |
| Ταμείο Πλεονασμού / Redundancy Fund | Employer-only 1.2% |
| ΑνΑΔ / HRDA | Human Resource Development Fund, employer-only 0.5% |
| Ταμείο Κοινωνικής Συνοχής / Social Cohesion Fund | Employer-only 2.0%, uncapped |
| Κεντρικό Ταμείο Αδειών / Central Holiday Fund | Conditional employer 8.0% |
| Φόρος Εισοδήματος / PAYE / Income Tax | Income tax withheld |
| Ασφαλιστέες αποδοχές / Insurable earnings | Capped base (66,612/yr in 2025) |
| Δωρόσημο / 13th salary / Bonus | Annual bonus (taxable) |

## Section 15 -- Onboarding Fallback

If you cannot establish enough to compute payroll, gather in this order and stop where blocked:

1. **Calendar year + pay date** — selects 2025 vs 2026 brackets and ceilings.
2. **Gross monthly emoluments** + whether any 13th salary/bonus applies.
3. **TD59 declaration** — allowances and any new-resident exemption claim.
4. **Employee TIN + SI registration number** — required to file.
5. **Year-to-date gross, PAYE, SI, GHS already withheld** — for cumulative adjustment.
6. **Employer Central Holiday Fund status** — exempt or not.
7. **Exemption evidence** — only if 20%/50% is claimed.

If the engagement turns out to be a self-employed person, stop: this employer-payroll skill does not cover self-employed SI (16.6% on deemed earnings) or GHS (4.00%).

## Section 16 -- Filing Obligations (Forms)

**Filing Obligations (Forms)**

| Form | Purpose | Deadline |
| --- | --- | --- |
| **TD7 (ΤΦ7) — Employer's Return for Withheld Tax and Contributions** | Monthly employer return of PAYE income tax, Social Insurance and GHS withheld for all employees; filed exclusively via TAX FOR ALL (TFA) | Monthly TD7 mandatory from 1 Jan 2025. From Jan 2026 each month's return and payment due by end of the following month. Transitional: Jan–Nov 2025 returns due 31 Dec 2025; Dec 2025 return due 31 Jan 2026 (IBCCS Tax; businessincyprus.gov.cy) |
| **TD63 — Emoluments Certificate** | Annual certificate the employer issues to each employee showing emoluments, tax withheld, and SI/GHS contributions | Provided to employees after year-end (feeds the employee's TD1) |
| **TD59 — Declaration of allowances/exemptions** | Employee declares claimed allowances/exemptions so the employer can calculate correct monthly PAYE | Start of each tax year / on hiring |
| **TD1 — Personal income tax return** | Employee's annual income tax return | 31 July of the year following the tax year (electronically via TFA) |
| **YKA 01-001 — Employer registration** | Register employer in the Register of Employers with Social Insurance Services; obtain employer registration number | Before first hire |

### Key Thresholds

**Key Thresholds**

| Threshold | Value | Source |
| --- | --- | --- |
| Personal income tax filing threshold | Personal return (TD1) generally required where gross annual income exceeds EUR 19,500 (2025) | PwC; Cyprus Tax Department |
| Social Insurance employer registration | Required before hiring any employee — no minimum employee count or wage threshold | Social Insurance Services |
| GHS / SI employee coverage | Applies from the first euro of employment income; no de minimis | gesy.org.cy; Social Insurance Services |
| Employee TIN requirement | Mandatory on all monthly and annual TD7 returns from tax year 2025, regardless of income level | Cyprus Tax Department |

### Penalties

**Penalties**

| Penalty | Detail | Source |
| --- | --- | --- |
| Late payment of tax/contributions | Interest at 3.50% per annum for amounts due from 1 January 2026 (2025: 5.50%; 2024: 5.00%) plus monetary penalties. **[RESEARCH GAP — reviewer to confirm]** current rate. | Tax Department |
| Late submission of TD7 / failure to withhold | Administrative penalties for late or non-submission of employer returns and for failure to remit withheld PAYE/contributions via TFA; exact amounts vary. **[RESEARCH GAP — reviewer to confirm]** current schedule. | Tax Department |
| Late Social Insurance contributions | Additional charge / surcharge on overdue SI, Redundancy, HRDA and Social Cohesion contributions. **[RESEARCH GAP — reviewer to confirm]** current surcharge. | Social Insurance Services |

## Section 17 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (PAYE + SI + GHS + employer funds) | **This skill (cyprus-payroll.md)** |
| Self-employed income tax / SI (16.6%) / GHS (4.00%) | cyprus self-employed / income-tax skill |
| Cyprus VAT returns | cyprus-vat-return skill |
| Cyprus bookkeeping | cyprus-bookkeeping skill |
| Employer corporate tax | cyprus-corporate-tax skill |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages, employer SI, Redundancy, HRDA, GHS, Social Cohesion (and Central Holiday Fund if any) are expenses; PAYE and employee SI/GHS are liabilities until remitted via TFA / to Social Insurance Services.
- **Payroll → Income Tax:** The TD63 emoluments certificate feeds the employee's TD1 personal return (due 31 July following year).
- **Payroll → Social Insurance:** Contributions paid through payroll count toward the employee's SI pension entitlement.

## Section 18 -- Reference Material

**Reference Material**

| Item | Value | Source |
| --- | --- | --- |
| 2025 PIT brackets | 0/20/25/30/35% at 19,500 / 28,000 / 36,300 / 60,000 | Cyprus Tax Department; PwC (reviewed 18 May 2026) |
| 2026 PIT brackets | 0/20/25/30/35% at 22,000 / 32,000 / 42,000 / 72,000 | Parliament 22 Dec 2025; ITR World Tax |
| Social Insurance | 8.8% employee + 8.8% employer; 16.6% self-employed | PwC; Andersen |
| 2025 max insurable earnings | EUR 66,612/yr; 5,551/mo; 1,281/wk | KPMG Cyprus; Social Insurance Services |
| GHS/GESY | 2.65% employee; 2.90% employer; 4.00% self-employed; cap 180,000/yr | PwC; gesy.org.cy |
| Redundancy Fund | 1.2% employer, capped at 66,612 | businessincyprus.gov.cy; Andersen |
| HRDA Fund | 0.5% employer, capped at 66,612 | businessincyprus.gov.cy; Andersen |
| Social Cohesion Fund | 2.0% employer, NO cap | businessincyprus.gov.cy; Andersen |
| Central Holiday Fund | 8.0% employer, only if non-exempt | businessincyprus.gov.cy |
| Minimum wage 2025 | EUR 1,000/mo (after 6 months); EUR 900/mo (first 6 months) | in force since 1 Jan 2024 |
| Minimum wage 2026 | EUR 1,088/mo (after 6 months); EUR 979/mo (first 6 months) | Cyprus Mail (Dec 2025) |
| 20% exemption | lower of 20% or EUR 8,550/yr; first employment after 26 Jul 2022; 3 prior non-resident years; up to 7 years | Income Tax Law Art. 8(21A); Harneys |
| 50% exemption | 50% where remuneration > EUR 55,000; first employment from 1 Jan 2022; 15 prior non-resident years; 17 years | Income Tax Law Art. 8(23A); Harneys |

### Sources

1. PwC Worldwide Tax Summaries — Cyprus Individual: Taxes on personal income (reviewed 18 May 2026) — https://taxsummaries.pwc.com/cyprus/individual/taxes-on-personal-income
2. PwC Worldwide Tax Summaries — Cyprus Individual: Other taxes (Social Insurance, GHS, funds) — https://taxsummaries.pwc.com/cyprus/individual/other-taxes
3. KPMG Cyprus — Amendment to the maximum amount of insurable earnings for 2025 — https://kpmg.com/cy/en/home/insights/2025/01/amendment-to-the-maximum-amount-of-insurable-earnings-for-2025.html
4. Andersen Cyprus — Social Insurance Contributions for the Year 2025 — https://gr.andersen.com/news/cyprus-news-social-insurance-contributions-for-the-year-2025/
5. Government of Cyprus (Business in Cyprus) — Social Insurance Registration and Contributions — https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/
6. IBCCS TAX — Cyprus Monthly TD7 PAYE Declarations via Tax For All (TFA): Deadlines & Key Rules — https://ibccs.tax/blog/cyprus-monthly-td7-%CF%84%CF%867-tf7-paye-tfa/
7. Harneys — Cyprus clarifies the 50% (Art. 8(23A)) and 20% (Art. 8(21A)) income-tax exemptions — https://www.harneys.com/our-blogs/regulatory/cyprus-clarifies-the-50-per-cent-income-tax-exemption-for-employment-exercised-in-cyprus/
8. Cyprus Mail — Labour Minister announces increase of monthly minimum wage to EUR 1,088 — https://cyprus-mail.com/2025/12/23/labour-minister-announces-increase-of-monthly-minimum-wage-to-1088-euro
9. ITR World Tax — Cyprus Tax Reform updates effective from 2026 (new PIT brackets) — https://www.itrworldtax.com/NewsAndAnalysis/cyprus-tax-reform-updates-effective-from-2026/Index/2225
10. Cyprus Tax Life (citing gesy.org.cy) — Cyprus GHS/GESY contribution rates and cap — https://www.cyprustaxlife.com/learn/ghs-cyprus

### Research Caveats (read before relying on figures)

- Confidence is **high** for the core 2025 payroll mechanics; most figures are corroborated by two or more Big-4 / official sources.
- The official Cyprus Tax Department (tax.gov.cy) and Social Insurance Services (sid.mlsi.gov.cy) PDFs were not directly retrievable at research time; figures are from Big-4 guides and the Business-in-Cyprus portal. **Confirm against the official 2025 tax card and Social Insurance Services contribution table.**
- Self-employed SI is stated at 16.6% (Andersen/KPMG/cyprustaxlife) although PwC's page still listed 15.6%.
- GHS employer rate 2.90% vs occasionally-quoted 3.00% — 2.90% used here; confirm against gesy.org.cy.
- Central Holiday Fund 8.0% applies only to non-exempt employers; treat as conditional, not universal.
- Exact monetary penalty amounts and the annual public-interest rate are **[RESEARCH GAP — reviewer to confirm]**.
- 2026 reform brackets are Parliament-approved (22 Dec 2025) and effective 1 Jan 2026; verify the final published law text for new family/household reliefs.

## Section 19 -- Test Suite

Each test recomputed end-to-end; expected values reconcile to the cent (2025 brackets/ceilings).

**Tax-free band.** Annual gross EUR 18,000. SI 8.8% = 1,584.00; GHS 2.65% = 477.00; PAYE base = 15,939.00 (< 19,500) → **PAYE = 0.00**.

**First-bracket employee.** Annual gross EUR 30,000. SI = 2,640.00; GHS = 795.00; base = 26,565.00; PAYE = (26,565 − 19,500) × 20% = **1,413.00**; net annual = **25,152.00**.

**SI ceiling bite.** Annual gross EUR 90,000. Employee SI = MIN(90,000, 66,612) × 8.8% = **5,861.86** (NOT 7,920); GHS = **2,385.00**.

**Top-bracket PAYE.** Base EUR 81,753.14 → 10,885 + (81,753.14 − 60,000) × 35% = 10,885 + 7,613.60 = **18,498.60**.

**Employer load below ceiling.** Annual gross EUR 30,000 → 8.8% + 1.2% + 0.5% + 2.90% + 2.0% = 15.40% × 30,000 = **4,620.00** total employer funds.

**Social Cohesion uncapped.** Annual gross EUR 80,000 → Social Cohesion = 80,000 × 2.0% = **1,600.00** (full salary, not capped at 66,612).

**Redundancy/HRDA capped.** Annual gross EUR 90,000 → Redundancy = 66,612 × 1.2% = **799.34**; HRDA = 66,612 × 0.5% = **333.06**.

**50% expat exemption.** Gross EUR 120,000, eligible Art. 8(23A) → taxable emoluments = 60,000; SI = 5,861.86 (capped, unreduced); GHS = 3,180.00 (full emoluments); PAYE base = 50,958.14; PAYE = 3,775 + (50,958.14 − 36,300) × 30% = **8,172.44**.

**Combined employee rate.** Below both ceilings, employee SI + GHS = 8.8% + 2.65% = **11.45%** of gross (before PAYE).

**Minimum wage net.** Annual gross EUR 12,000 (EUR 1,000/mo after 6 months) → SI 1,056.00 + GHS 318.00, PAYE 0.00 → net annual **10,626.00**, net monthly **885.50**.

**2026 bracket switch.** A pay period dated 15 Jan 2026 uses the 2026 table (0% to 22,000), NOT the 2025 table — a EUR 21,000 chargeable income yields **PAYE 0.00** in 2026 vs 300.00 (1,500 × 20%) in 2025.

**TIN refusal.** Employee with no TIN → refuse to file TD7 (TIN mandatory from tax year 2025).

## PROHIBITIONS

- **TD59 declaration required** — NEVER process payroll without a TD59 declaration of allowances/exemptions from the employee.
- **TD7 without TIN** — NEVER file a TD7 without the employee's TIN — it is mandatory from tax year 2025.
- **New-resident exemption documentation** — NEVER apply the 20% or 50% new-resident exemption without documented eligibility (residence history + first-employment date + salary threshold).
- **SI/GHS base not reduced by income-tax exemption** — NEVER reduce the Social Insurance or GHS base by the income-tax exemption — exemptions reduce only the PAYE base.
- **Social Cohesion Fund uncapped** — NEVER cap the Social Cohesion Fund at the insurable-earnings ceiling — it is 2.0% on TOTAL actual earnings, no cap.
- **Redundancy/HRDA/SI ceiling** — NEVER apply Redundancy, HRDA or Social Insurance above the EUR 66,612 (2025) insurable-earnings ceiling.
- **Central Holiday Fund default exclusion** — NEVER include the 8.0% Central Holiday Fund by default — apply only when the employer is confirmed non-exempt.
- **Bracket year matching** — NEVER use the 2025 brackets for a 2026 pay period (or vice versa).
- **TD7 deadline via TAX FOR ALL** — NEVER miss the monthly TD7 deadline via TAX FOR ALL — penalties and interest apply.
- **Estimated labeling requirement** — NEVER present payroll computations as definitive — always label as estimated and direct to a Cyprus-warranted accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a warranted accountant in Cyprus) before implementation.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
