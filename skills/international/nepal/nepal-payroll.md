---
name: nepal-payroll
description: Use this skill whenever asked about Nepal payroll processing for employed persons. Trigger on phrases like "Nepal payroll", "PAYE Nepal", "TDS on salary Nepal", "eTDS Nepal", "salary tax Nepal", "SSF contribution", "Social Security Fund Nepal", "provident fund Nepal", "gratuity Nepal", "CIT Nepal", "EPF Nepal", "net pay Nepal", "salary calculation Nepal", "NPR payroll", "Nepalese Rupee payroll", "minimum wage Nepal", "PAN Nepal", "D-01 D-03 Nepal", "female tax credit Nepal", "remote area allowance", "married couple tax Nepal", or any question about computing employee pay, salary withholding, or social security contributions for Nepal-based employees. This skill covers monthly TDS/PAYE salary withholding on progressive resident slabs (single and married-couple), the 1% first-band Social Security Tax and its SSF interaction, retirement-fund and insurance deductions, the female tax credit, the 31% Social Security Fund contribution (20% employer / 11% employee), provident fund and gratuity for non-SSF employers, the minimum wage, filing forms (eTDS, D-01/D-02/D-03) and penalties. Nepal DOES levy a personal income tax (progressive PAYE). ALWAYS read this skill before processing any Nepal payroll.
jurisdiction: NP
domain: payroll
tax_year: 2025
reviewed_by: Ashish Bista
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# nepal-payroll

## Nepal Payroll Skill v0.1

Tier 2 (research-verified). NOT yet signed off by a licensed Nepali chartered accountant or registered auditor. Tax slabs, deductions and non-resident rates are corroborated by PKF T R Upadhya & Co. (PKF Global member firm) Tax Rates booklet FY 2082/83 and the Inland Revenue Department (IRD). SSF figures (31% total, 20%/11% split) are well-corroborated; the SSF scheme-by-scheme sub-split, the SSF salary ceiling, and exact statutory penalty percentages are flagged as RESEARCH GAPS below. Treat every output as an estimate pending professional review.

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Ashish Bista** on 2026-06-06.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Payroll (Salary TDS + SSF)

- **SSF — employee contribution rate** — 11% of basic remuneration (deducted)  _(Contribution Based Social Security Act 2074 (Pioneer Law/HajirHR))_
- **SSF — employer contribution rate** — 20% of basic remuneration  _(Contribution Based Social Security Act 2074)_
- **SSF — total contribution rate** — 31%  _(Pioneer Law; HajirHR)_
- **Employer 20% composition** — PF 10% + Gratuity 8.33% + Additional 1.67%  _(SSF (verify composition))_
- **Employee 11% internal split** — 10% Provident Fund + 1% Medical Insurance Scheme (Medical & Dependent Health Protection Scheme under SSF)  _(SSF Directive 2075)_
- **SSF-liable 'basic remuneration' composition** — Basic Salary + Dearness Allowance (Gross salary excluding overtime/allowances)  _(Labour Act 2074 s. 2 / SSF Act 2074)_
- **Salary income tax withholding** — Withheld monthly per resident-individual slabs (see Income Tax tab)  _(Income Tax Act 2058 Sch.1)_
- **SSF contributor & the 1% SST exemption** — An SSF contributor is exempt from the 1% income-tax SST first-band levy  _(Income Tax Act 2058 (PKF))_
- **Remittance / return due dates** — SSF: Within 15 days of month-end; Salary TDS: Within 25 days of month-end  _(SSF Act 2074 / Income Tax Act 2058)_
- **Maximum Approved Retirement Deduction** — Actual contribution, 1/3rd of assessable income, or NPR 500,000 (whichever is lower)  _(Income Tax Act 2058 s. 63)_
- **Remote Area Allowance Deduction** — Up to NPR 50,000 depending on the remote category (Class A to E)  _(Income Tax Act 2058 Sch. 1)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Federal Democratic Republic of Nepal |
| Currency | Nepalese Rupee (NPR / Rs) |
| Standard pay frequency | Monthly |
| Fiscal / tax year | Mid-July to mid-July (Shrawan 1 -- Ashad end). Current: **FY 2082/83 (2025/26)** |
| Salary tax system | TDS / PAYE -- progressive monthly withholding on annualised salary; reconciled at year-end |
| Tax authority | Inland Revenue Department (IRD), https://ird.gov.np |
| Social security authority | Social Security Fund (SSF), https://www.ssf.gov.np |
| Labour authority | Ministry of Labour, Employment and Social Security (minimum wage via Nepal Gazette) |
| Key legislation | Income Tax Act 2058 (2002); Contribution Based Social Security Act 2074 (2017) and Social Security Regulations 2075; Labour Act 2074 |
| eTDS deadline | Within **25 days** of the end of each Nepali month |
| SSF deadline | Within **25 days** of month-end (extended from 15 days by a July 2025 amendment) — see RESEARCH GAP |
| Validated by | Pending -- requires sign-off by a licensed Nepali chartered accountant / registered auditor |
| Skill version | 0.1 |

Nepal levies a progressive personal income tax on resident natural persons, collected by the employer as monthly TDS (PAYE) and reconciled annually. The slab thresholds depend on whether the employee elects **single** or **married-couple** status. (Source: PKF FY 2082/83 booklet p.2, https://pkf.trunco.com.np/files/publications/1748841198_Tax%20Rates%202082-83_Final_250601_213028.pdf)

## Section 2 -- Income Tax (TDS / PAYE) Withholding

The employer annualises the employee's taxable salary, applies the progressive slab table, divides by 12, and withholds monthly TDS. **The slabs are identical for FY 2081/82 and FY 2082/83** (confirmed side-by-side in PKF FY 2082/83 booklet p.2).

### Residency test

- **Resident** — Present in Nepal for 183 days or more in a 365-day period, or whose normal place of abode is Nepal. Residents are taxed on the progressive slabs below.  _(Income Tax Act 2058; PKF FY 2082/83 booklet.)_
- **Non-resident** — Anyone else; taxed at a flat rate on Nepal-source income (see Section 4).  _(Income Tax Act 2058; PKF FY 2082/83 booklet.)_

### Resident slabs — SINGLE individual (FY 2082/83, also FY 2081/82)

**Resident slabs — SINGLE individual (FY 2082/83, also FY 2081/82)**  _(PKF FY 2082/83 booklet p.2)_

| Taxable income (NPR) | Marginal rate | Tax on slice (NPR) | Cumulative tax at top of band (NPR) |
| --- | --- | --- | --- |
| First 500,000 | 1% (Social Security Tax) | 5,000 | 5,000 |
| Next 200,000 (500,001 -- 700,000) | 10% | 20,000 | 25,000 |
| Next 300,000 (700,001 -- 1,000,000) | 20% | 60,000 | 85,000 |
| Next 1,000,000 (1,000,001 -- 2,000,000) | 30% | 300,000 | 385,000 |
| Next 3,000,000 (2,000,001 -- 5,000,000) | 36% | 1,080,000 | 1,465,000 |
| Above 5,000,000 | 39% | -- | -- |

500,000×1% = 5,000; +200,000×10% = 25,000; +300,000×20% = 85,000; +1,000,000×30% = 385,000; +3,000,000×36% = 1,465,000. All reconcile to the cumulative column.

- **Top two rates surcharge structure** — 36% = 30% + 20% surcharge; 39% = 30% + 30% surcharge  _(PKF FY 2082/83 booklet p.2)_

### Resident slabs — MARRIED couple (electing couple status)

**Resident slabs — MARRIED couple (electing couple status)**  _(PKF FY 2082/83 booklet p.2)_

| Taxable income (NPR) | Marginal rate | Tax on slice (NPR) | Cumulative tax at top of band (NPR) |
| --- | --- | --- | --- |
| First 600,000 | 1% (Social Security Tax) | 6,000 | 6,000 |
| Next 200,000 (600,001 -- 800,000) | 10% | 20,000 | 26,000 |
| Next 300,000 (800,001 -- 1,100,000) | 20% | 60,000 | 86,000 |
| Next 900,000 (1,100,001 -- 2,000,000) | 30% | 270,000 | 356,000 |
| Next 3,000,000 (2,000,001 -- 5,000,000) | 36% | 1,080,000 | 1,436,000 |
| Above 5,000,000 | 39% | -- | -- |

600,000×1% = 6,000; +200,000×10% = 26,000; +300,000×20% = 86,000; +900,000×30% = 356,000; +3,000,000×36% = 1,436,000. All reconcile.

the couple's first band is Rs 600,000 (vs Rs 500,000 for single), so the 30% band runs from 1,100,001 to 2,000,000 = a 900,000 slice (not 1,000,000). (Source: PKF FY 2082/83 booklet p.2.)

### The 1% first-band "Social Security Tax"

- **1% first-band Social Security Tax** — The 1% on the first band is a Social Security Tax deposited to a separate revenue account (code 11211). It is NOT levied if the taxpayer is: a sole proprietor, or on pension income, or contributing to the Social Security Fund (SSF). For SSF-enrolled employees the first-band rate is effectively 0% — the 1% is replaced by the SSF contribution.  _(PKF FY 2082/83 booklet p.2 footnotes)_
- **Practical rule for employees** — if the employer is SSF-registered and the employee is enrolled, drop the 1% on the first band; otherwise apply the 1%.  _(PKF FY 2082/83 booklet p.2 footnotes)_

## Section 3 -- Key Deductions and Credits Affecting Withholding

**Deductions**  _(PKF FY 2082/83 booklet pp.2--3)_

| Item | Limit |
| --- | --- |
| Retirement fund contribution deduction | Lower of 1/3 of taxable income, **NPR 500,000**, or actual contribution (EPF 2019 / CIT 2047 / SSF 2074 / Retirement Fund Act 2075 funds only) |
| Life insurance premium | Lower of actual or **NPR 40,000** |
| Medical (health) insurance | Lower of actual or **NPR 20,000** |
| Private building insurance | Lower of actual or **NPR 5,000** |
| Remote Area Allowance | Up to **NPR 50,000** (Area A 50,000 / B 40,000 / C 30,000 / D 20,000 / E 10,000) |
| Pension income (additional) | 25% of first-band amount or actual pension, whichever lower |
| Incapacitated person (additional) | 50% of first-band amount or actual, whichever lower |
| Foreign diplomatic mission staff of Nepal | Only **25%** of foreign allowances included in income |

**Credits**  _(PKF FY 2082/83 booklet pp.2--3)_

| Credit | Amount |
| --- | --- |
| Female Tax Credit | **10% credit on the tax liability** for a female natural person whose **only** income is remuneration |
| Medical Tax Credit | At least the lower of NPR 1,500, 15% of medical expenses (plus carry-forward), or actual liability |

## Section 4 -- Non-Resident Rates

**Non-Resident Rates**  _(PKF FY 2082/83 booklet p.3)_

| Transaction | Rate |
| --- | --- |
| Normal transactions / employment income | **25%** flat |
| Shipping / air transport / telecom, postage, satellite, optical fibre | **5%** |
| Shipping / air transport / telecom **within Nepal territory** | **2%** |
| Repatriation of profit by Foreign Permanent Establishment | **5%** |

- **No slab/credit benefit** — Non-residents receive no slab benefit and no female/medical credits on employment income.  _(PKF FY 2082/83 booklet p.3)_

## Section 5 -- Social Security Fund (SSF) Contributions

Governed by the Contribution Based Social Security Act 2074 (2017) and Social Security Regulations 2075, administered by the SSF.

### Contribution rates (of basic salary)

**Contribution rates (of basic salary)**

| Component | Total | Employer | Employee |
| --- | --- | --- | --- |
| Social Security Fund | **31%** | **20%** | **11%** |

Employer 20% + Employee 11% = 31% total. Reconciles.

- **Employee 11% deducted from pay** — Employee 11% is deducted from pay.  _(Social Security Act 2074; SSF, https://www.ssf.gov.np)_
- **Employer 20% is added cost** — Employer 20% is an employer cost on top of gross.  _(Social Security Act 2074; SSF, https://www.ssf.gov.np)_
- **Basic salary under SSF** — "Basic salary" under the SSF scheme is conventionally basic + dearness allowance; many employers define basic as a fixed portion of gross.  _(Social Security Act 2074; SSF, https://www.ssf.gov.np; Lockton, https://global.lockton.com/us/en/news-insights/nepal-introduces-mandatory-social-security-contribution.)_

### The four protection schemes

The 31% funds four schemes: (1) Medical treatment, health & maternity; (2) Accident & disability; (3) Dependent family (survivor) protection; (4) Old-age protection (pension or lump sum).

[RESEARCH GAP — reviewer to confirm against ssf.gov.np scheme circulars.] Two conflicting breakdowns appear in secondary legal summaries (e.g. medical ~1% vs ~3.22%; old-age ~28.33% vs ~26.11%). The 31% total and the 20% / 11% split are authoritative; the internal allocation is not. Do not rely on a per-scheme split for payroll — only the aggregate 31% drives the cash deduction.

### SSF salary ceiling

Multiple secondary sources report the SSF maximum monthly contributory salary ceiling raised from NPR 300,000 to NPR 350,000/month effective FY 2082/83 (2025/26). [RESEARCH GAP — could not be confirmed directly from ssf.gov.np; reviewer to verify before applying a cap.] (Source: secondary — lawsagar.com, kumarijob.com SSF guides.)

## Section 6 -- Provident Fund and Gratuity (non-SSF employers)

For employers not under SSF, the Labour Act 2074 baseline applies:

**Provident Fund and Gratuity table**  _(Labour Act 2074)_

| Item | Employee | Employer |
| --- | --- | --- |
| Provident Fund | 10% of basic | 10% of basic |
| Gratuity | -- | 8.33% of basic |

- **SSF subsumption** — Under SSF these are subsumed into the 20% employer / 11% employee SSF contribution. Most private employers have migrated to SSF, which is mandatory (see Section 7).  _(Labour Act 2074)_

## Section 7 -- Registration Thresholds

- **PAN (Permanent Account Number)** — Employers and all persons with taxable income must register for PAN at the local Inland Revenue Office. PAN must be quoted on tax documents.  _(Income Tax Act 2058; infinitynp.com income-tax guide.)_
- **SSF registration threshold** — SSF registration is mandatory for ALL private-sector employers with one or more employees — no minimum-size threshold (Section 5, Social Security Act 2074). Employers list the establishment, then enrol employees within 3 months of the employer's listing.  _(Social Security Act 2074; Lockton, https://global.lockton.com/us/en/news-insights/nepal-introduces-mandatory-social-security-contribution.)_

## Section 8 -- Filing, Forms and Deadlines

### Monthly TDS / eTDS (IRD)

**Monthly TDS / eTDS (IRD)**  _(unionnepal.com TDS guide, https://www.unionnepal.com/tds-in-nepal; estartupnepal.com.)_

| Item | Detail |
| --- | --- |
| Frequency | Monthly (per Nepali calendar month) |
| Deadline | Deposit TDS **and** file the eTDS return **within 25 days** of month-end (e.g. Shrawan TDS due by Bhadra 25) |
| Channel | IRD eTDS system (mandatory for all withholding agents) |

### Monthly SSF contribution

**Monthly SSF contribution**  _(secondary — lawsagar.com SSF employer guide.)_

| Item | Detail |
| --- | --- |
| Frequency | Monthly |
| Deadline | **Within 25 days** of month-end (extended from 15 days by a July 2025 amendment) — **[RESEARCH GAP — corroborate against SSF/Gazette primary source]** |
| Channel | SSF online system |

### Annual income tax return

**Annual income tax return**  _(taxconsultantnepal.com; IRD D-01 form https://ird.gov.np/public/pdf/53922457.pdf; PKF FY 2082/83 booklet p.3; estartupnepal.com.)_

| Item | Detail |
| --- | --- |
| Deadline | Within **3 months** of fiscal year-end → **Ashoj end (~mid-October)** (e.g. FY 2081/82 extended to 25 Ashoj 2082); a further 3-month extension to Poush end (~mid-January) may be granted on application |
| Forms | **D-01** (self-assessment / presumptive small taxpayer); **D-02**; **D-03** (companies and firms with turnover over Rs 10m / Rs 1 crore) |
| Employee filing | Not required if the **only** income is remuneration fully withheld at source — **except** a natural person with **taxable income over NPR 4,000,000** must file under Section 96 |

## Section 9 -- Penalties

### TDS / income tax (Income Tax Act 2058)

**TDS / income tax (Income Tax Act 2058)**  _(unionnepal.com; estartupnepal.com.)_

| Trigger | Penalty |
| --- | --- |
| Late eTDS return filing | NPR 100 per day, capped at NPR 5,000; plus 2.5% per annum for failing to file even after depositing |
| Late deposit of deducted TDS | Interest **15% per annum** plus **1.5% per month** on the outstanding amount |

[RESEARCH GAP — exact statutory percentages from secondary sources only; cross-check against the current Income Tax Act 2058 / IRD circular.] (Source: unionnepal.com; estartupnepal.com.)

### SSF non-compliance (Social Security Act 2074)

**SSF non-compliance (Social Security Act 2074)**  _(Social Security Act 2074; secondary legal guides — lawsagar.com, medhacorplaw.com.)_

| Trigger | Penalty |
| --- | --- |
| Late / non-deposit of contribution | Fine equal to **double (2×)** the unpaid contribution |
| Outstanding contribution | Interest **10% per annum** |
| Continued default | Prosecution and possible business-license suspension |

## Section 10 -- Minimum Wage

Set by the Ministry of Labour, Employment and Social Security; published in the Nepal Gazette 21 July 2025, effective from the start of FY 2082/83 (17 July 2025). A +13% increase from the previous NPR 17,300 (set 2023).

**Minimum wage table**  _(wageindicator.org, https://wageindicator.org/work/minimum-wage/updates/2025/minimum-wage-increased-in-nepal-from-17-july-2025-july-22-2025/; business-humanrights.org.)_

| Basis | Amount (NPR) |
| --- | --- |
| Monthly minimum | **19,550** = basic 12,170 + dearness allowance 7,380 |
| Daily wage | **754** |
| Hourly wage | **101** (part-time hourly: 107) |
| Tea estate workers (monthly) | **13,893** |

basic 12,170 + dearness 7,380 = 19,550. Reconciles.

## Section 11 -- Conservative Defaults

**Conservative defaults table**

| Unknown | Conservative default | Why |
| --- | --- | --- |
| Residency status | Treat as **resident** ONLY if ≥183-day presence / abode is evidenced; otherwise flag — do not silently assume | Non-resident employment income is a flat 25% with no slabs or credits |
| Single vs married election | **Single** until couple status is documented | The couple thresholds are more generous; defaulting to single avoids understating tax |
| SSF enrolment | If unconfirmed, **apply the 1% first-band Social Security Tax** | The 1% drops only when SSF contributions are actually made |
| First-band 1% for SSF-enrolled employee | **0%** (1% replaced by SSF) | Reflects the statutory carve-out |
| Female tax credit | **Do not apply** unless the employee is female AND has remuneration-only income | The 10% credit is conditional on remuneration-only income |
| Deductions (insurance, retirement) | **Zero** until documented with limits | Over-claiming deductions understates tax |
| SSF basic salary | Use documented basic (+ dearness); do not assume gross = basic | Over-stating basic over-charges contributions |
| SSF ceiling | Apply the ceiling only if confirmed (RESEARCH GAP) | The NPR 350,000 ceiling is unverified |
| Pay frequency | Monthly | Standard in Nepal |

## Section 12 -- Required Inputs and Refusal Catalogue

### Required inputs

1. Annualised gross taxable salary (NPR) and the month being processed.
2. Residency status (or days present in Nepal this fiscal year).
3. Single vs married-couple election.
4. Whether the employer is SSF-registered and the employee enrolled (drives the 1% first-band carve-out and the 31% split).
5. Basic salary (+ dearness allowance) for SSF / PF computation.
6. Eligible deductions (retirement fund, life/health/building insurance, remote-area, pension/incapacity) with evidence.
7. Whether the employee is female with remuneration-only income (female tax credit).

### Refusal catalogue — STOP and ask, do not guess

**Refusal catalogue table**

| Situation | Action |
| --- | --- |
| Residency unknown and presence days not provided | Refuse to finalise; ask for days present / abode status |
| Single/married election unknown | Default to **single** and flag; do not apply couple thresholds without an election |
| SSF status unknown | Flag; do not drop the 1% first band without confirmed SSF enrolment |
| Female tax credit requested without remuneration-only confirmation | Refuse; the credit is conditional |
| Deductions claimed without evidence or above statutory limits | Cap at the limit or refuse; request evidence |
| Request to apply an SSF salary ceiling | Flag the ceiling as a RESEARCH GAP before relying on it |
| Request to skip SSF "because employer is small" | Refuse — SSF applies at ≥1 employee, no threshold |
| Request to use a per-scheme SSF split for the cash deduction | Refuse — only the aggregate 31% (20%/11%) is authoritative |

## Section 13 -- Transaction / Payment Pattern Library

Deterministic classification for Nepali bank statement lines (Devanagari / Nepali terms shown alongside common English / transliterated forms).

### Salary credits (to the employee)

**Salary credits table**

| Pattern on statement | Nepali term | Classification |
| --- | --- | --- |
| TALAB, SALARY, PAYROLL | तलब (talab = salary) | Net salary payment |
| EMPLOYER [name] TRANSFER, WAGES | -- | Net salary payment |
| BONUS, BHATTA | बोनस / भत्ता (bhatta = allowance) | Bonus / allowance (taxable, in TDS base) |
| OT, OVERTIME, ADHIK SAMAYA | अधिक समय | Overtime pay |
| MAHANGI BHATTA | महंगी भत्ता | Dearness allowance |

### Employer debits (to the authorities)

**Employer debits table**

| Pattern on statement | Classification |
| --- | --- |
| IRD, TDS, eTDS, AYAKAR | TDS / income-tax remittance to IRD (due within 25 days) |
| SSF, SAMAJIK SURAKSHYA KOSH | SSF contribution remittance (due within 25 days) |
| EPF, PROVIDENT FUND, SANCHAYA KOSH | Provident fund remittance (non-SSF employers) |
| CIT, NAGARIK LAGANI KOSH | Citizen Investment Trust remittance |
| NET WAGES, SALARY RUN, PAYROLL | Net salary disbursement to employees |

"AYAKAR" (आयकर) means income tax; "SAMAJIK SURAKSHYA" means social security. Any IRD debit referencing salary tax = monthly TDS remittance.

## Section 14 -- Worked Examples

All examples use the FY 2082/83 resident slabs. Currency NPR. Arithmetic is recomputed end-to-end. "Annual" figures are the taxable income for the fiscal year; monthly TDS = annual tax ÷ 12.

### Example A -- SSF-enrolled single employee, taxable income 800,000

Single, SSF-enrolled (so first band is **0%**, not 1%), no deductions.

- Band 1 (first 500,000): SSF-enrolled → **0%** → 0.
- Band 2 (500,001--700,000): 200,000 × 10% = 20,000.
- Band 3 (700,001--800,000): 100,000 × 20% = 20,000.
- **Annual income tax = 0 + 20,000 + 20,000 = 40,000.**
- Monthly TDS = 40,000 ÷ 12 = **3,333.33**.

### Example B -- Non-SSF single employee, taxable income 800,000

Same income, but employer is **not** SSF-registered (so the 1% first band **applies**).

- Band 1: 500,000 × 1% = 5,000.
- Band 2: 200,000 × 10% = 20,000.
- Band 3: 100,000 × 20% = 20,000.
- **Annual income tax = 5,000 + 20,000 + 20,000 = 45,000.**
- Monthly TDS = 45,000 ÷ 12 = **3,750**.
- *Cross-check vs Example A:* the only difference is the 1% on the first band = +5,000. Reconciles.

### Example C -- Married couple, SSF-enrolled, taxable income 1,500,000

Married election, SSF-enrolled (first band 0%), no deductions.

- Band 1 (first 600,000): SSF → 0%.
- Band 2 (600,001--800,000): 200,000 × 10% = 20,000.
- Band 3 (800,001--1,100,000): 300,000 × 20% = 60,000.
- Band 4 (1,100,001--1,500,000): 400,000 × 30% = 120,000.
- **Annual income tax = 0 + 20,000 + 60,000 + 120,000 = 200,000.**
- Monthly TDS = 200,000 ÷ 12 = **16,666.67**.

### Example D -- Female single employee, remuneration-only, taxable income 1,000,000 (with female tax credit)

Single, SSF-enrolled (first band 0%), female with remuneration-only income → **10% tax credit**.

- Band 1: 0% (SSF).
- Band 2: 200,000 × 10% = 20,000.
- Band 3: 300,000 × 20% = 60,000.
- Tax before credit = 0 + 20,000 + 60,000 = **80,000**.
- Female tax credit = 10% × 80,000 = 8,000.
- **Annual income tax = 80,000 − 8,000 = 72,000.**
- Monthly TDS = 72,000 ÷ 12 = **6,000**.

### Example E -- Monthly SSF contribution, basic salary 40,000/month

Employer SSF-registered; basic salary (incl. dearness) NPR 40,000/month.

- Employee SSF = 40,000 × 11% = **4,400** (deducted from pay).
- Employer SSF = 40,000 × 20% = **8,000** (employer cost).
- Total SSF = 40,000 × 31% = **12,400**. (4,400 + 8,000 = 12,400 ✓.)
- If this employee's annual taxable income is 800,000 single, TDS per Example A = 3,333.33/month.
- **Monthly net pay (illustrative) = monthly gross − TDS − employee SSF.** With monthly gross 60,000: 60,000 − 3,333.33 − 4,400 = **52,266.67**.
- (Ceiling check: 40,000 basic is below any reported SSF ceiling, so no cap applies.)

### Example F -- Non-resident employee, employment income 1,200,000

Non-resident; flat 25% on Nepal-source employment income, no slabs, no credits.

- **Annual income tax = 1,200,000 × 25% = 300,000.**
- Monthly TDS = 300,000 ÷ 12 = **25,000**.
- SSF still applies if employed by a Nepali establishment: on basic 40,000/month, employee SSF = 4,400, employer SSF = 8,000.

## Section 15 -- Tier 1 Rules (deterministic — always apply)

- **Tier 1 rules** — 1. Resident salary tax is progressive marginal — apply each slice at its own rate (single or married-couple table). 2. The 1% first band is levied unless the employee contributes to the SSF (then 0%) — also waived for sole proprietors and pension income. 3. Married-couple thresholds apply only on a confirmed couple election; otherwise use the single table. 4. SSF = 31% of basic salary: 20% employer + 11% employee. Employee 11% is deducted; employer 20% is an added cost. 5. SSF is mandatory at ≥1 employee — no size threshold. 6. Female tax credit = 10% of the tax liability, only for a female with remuneration-only income. 7. Deductions are capped: retirement fund (lower of 1/3 income / 500,000 / actual), life insurance 40,000, health insurance 20,000, building insurance 5,000, remote-area up to 50,000. 8. Non-resident employment income is a flat 25%, no slabs or credits. 9. eTDS and SSF are due within 25 days of the Nepali month-end. 10. A natural person with taxable income over NPR 4,000,000 must file an annual return (Section 96), even on remuneration-only income.

## Section 16 -- Tier 2 Catalogue (reviewer judgement required)

These require a licensed Nepali chartered accountant's / registered auditor's judgement — do not finalise unilaterally:

- Whether an expatriate is resident under the abode test vs the 183-day count.
- The exact per-scheme SSF allocation of the 31% (RESEARCH GAP — Section 5).
- Whether and at what level an SSF salary ceiling applies (RESEARCH GAP — Section 5).
- The precise composition of "basic salary" for SSF where pay is structured into multiple allowances.
- Eligibility and quantum of the remote-area allowance (Area A--E).
- Treatment of pension / incapacity additional deductions.
- Application of a tax treaty to a non-resident from a treaty country.
- Whether a fund qualifies as an approved retirement fund (EPF / CIT / SSF / Retirement Fund Act 2075).
- Exact statutory penalty / interest percentages (RESEARCH GAP — Section 9).

## Section 17 -- Excel Working Paper Template

A minimal annual payroll working paper. One row per employee; monthly TDS = annual tax ÷ 12.

**Working paper columns**

| Col | Field | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Residency (R/NR) | input |
| C | Status (S/M) | input (R only) |
| D | SSF enrolled? (Y/N) | input |
| E | Annual taxable income (NPR) | input |
| F | First-band rate | `=IF(D="Y",0%,1%)` |
| G | Annual income tax (before credit) | progressive table on E using C and F (see formula below) |
| H | Female remuneration-only? (Y/N) | input |
| I | Female tax credit | `=IF(H="Y", G*10%, 0)` |
| J | Annual income tax (after credit) | `=G-I` (NR: `=E*25%`) |
| K | Monthly TDS | `=J/12` |
| L | Monthly basic salary (SSF base) | input |
| M | Employee SSF (11%) | `=IF(D="Y", L*11%, 0)` |
| N | Employer SSF (20%) | `=IF(D="Y", L*20%, 0)` |
| O | Monthly gross | input |
| P | Monthly net pay | `=O-K-M` |
| Q | Total monthly employer cost | `=O+N` |

- **Annual income tax formula (col G, SINGLE)** — =IF(E<=500000, E*F, IF(E<=700000, 500000*F + (E-500000)*10%, IF(E<=1000000, 500000*F + 20000 + (E-700000)*20%, IF(E<=2000000, 500000*F + 80000 + (E-1000000)*30%, IF(E<=5000000, 500000*F + 380000 + (E-2000000)*36%, 500000*F + 1460000 + (E-5000000)*39%)))))

For MARRIED, substitute the 600,000 / 800,000 / 1,100,000 / 2,000,000 / 5,000,000 breakpoints and the 6,000-based cumulative constants from Section 2. The cumulative constants 80,000 / 380,000 etc. assume the 1% first band; when F=0 the first-band amount is 0 and the cumulative constants reduce by the first-band tax — recompute per Section 2.

## Section 18 -- Bank Statement / Terminology Reading Guide

**Terminology guide**

| Term (Devanagari / transliterated) | Meaning |
| --- | --- |
| तलब (talab) | Salary |
| भत्ता (bhatta) | Allowance |
| महंगी भत्ता (mahangi bhatta) | Dearness allowance |
| बोनस (bonus) | Bonus |
| अधिक समय (adhik samaya) | Overtime |
| आयकर (ayakar) | Income tax (TDS) |
| सामाजिक सुरक्षा कोष (samajik surakshya kosh) | Social Security Fund (SSF) |
| सञ्चय कोष (sanchaya kosh) | Provident Fund (EPF) |
| नागरिक लगानी कोष (nagarik lagani kosh) | Citizen Investment Trust (CIT) |
| स्थायी लेखा नम्बर (PAN) | Permanent Account Number |

Statements are in NPR. An IRD debit referencing "ayakar" / "TDS" = monthly salary-tax remittance (due within 25 days).
- An SSF debit = social-security remittance (due within 25 days).
- An EPF / sanchaya kosh debit indicates a non-SSF provident-fund employer — confirm which scheme governs payroll.

## Section 19 -- Onboarding Fallback

If you lack a complete payroll setup for a new client:

1. Confirm PAN registration (IRD) and SSF registration (or EPF/CIT for non-SSF employers) exist.
2. Collect each employee's residency status, single/married election, and SSF enrolment status.
3. Confirm basic salary (+ dearness) for SSF / PF, and collect evidence for any deductions (retirement, insurance, remote-area).
4. Confirm whether any employee is female with remuneration-only income (female tax credit).
5. If any of the above is missing, produce an estimate only, label it clearly, list the assumptions (and flag every RESEARCH GAP relied on), and route to a licensed Nepali chartered accountant before filing.

### Reference tables (all figures cited inline above)

**Reference tables (all figures cited inline above)**  _(PKF FY 2082/83 booklet; Social Security Act 2074; SSF; Lockton; Labour Act 2074; Nepal Gazette 21 Jul 2025; wageindicator.org; unionnepal.com; estartupnepal.com; lawsagar.com; taxconsultantnepal.com; IRD)_

| Item | Value | Source |
| --- | --- | --- |
| Single 1% first-band ceiling | NPR 500,000 | PKF FY 2082/83 booklet p.2 |
| Married 1% first-band ceiling | NPR 600,000 | PKF FY 2082/83 booklet p.2 |
| Top marginal rate | 39% over NPR 5,000,000 | PKF FY 2082/83 booklet p.2 |
| 1% first-band carve-out | 0% if SSF-enrolled / sole prop / pension | PKF FY 2082/83 booklet p.2 |
| Retirement fund deduction cap | lower of 1/3 income / 500,000 / actual | PKF FY 2082/83 booklet p.2 |
| Life / health / building insurance caps | 40,000 / 20,000 / 5,000 | PKF FY 2082/83 booklet pp.2--3 |
| Remote-area allowance | up to 50,000 (A--E) | PKF FY 2082/83 booklet p.3 |
| Female tax credit | 10% of tax liability (remuneration-only) | PKF FY 2082/83 booklet p.3 |
| Non-resident employment income | 25% flat | PKF FY 2082/83 booklet p.3 |
| SSF total / employer / employee | 31% / 20% / 11% | Social Security Act 2074; SSF; Lockton |
| SSF per-scheme split | [RESEARCH GAP — verify with SSF] | secondary (conflicting) |
| SSF salary ceiling | NPR 350,000/mo [RESEARCH GAP — verify with SSF] | secondary |
| Provident Fund (non-SSF) | 10% + 10% of basic | Labour Act 2074 |
| Gratuity (non-SSF) | 8.33% of basic | Labour Act 2074 |
| Monthly minimum wage | NPR 19,550 (basic 12,170 + dearness 7,380) | Nepal Gazette 21 Jul 2025; wageindicator.org |
| eTDS deadline | within 25 days of month-end | unionnepal.com; estartupnepal.com |
| SSF deadline | within 25 days [RESEARCH GAP — corroborate] | secondary (lawsagar.com) |
| Annual return deadline | Ashoj end (~mid-Oct) | taxconsultantnepal.com; IRD |
| Mandatory return threshold | taxable income over NPR 4,000,000 | PKF FY 2082/83 booklet p.3 (Sec. 96) |
| TDS late-filing penalty | NPR 100/day, cap 5,000 + 2.5% p.a. [RESEARCH GAP] | unionnepal.com |
| TDS late-deposit interest | 15% p.a. + 1.5%/month [RESEARCH GAP] | unionnepal.com |
| SSF late penalty | 2× unpaid + 10% p.a. interest | Social Security Act 2074 (secondary) |

- **Single 1% first-band ceiling** — NPR 500,000  _(PKF FY 2082/83 booklet p.2)_
- **Married 1% first-band ceiling** — NPR 600,000  _(PKF FY 2082/83 booklet p.2)_
- **Top marginal rate** — 39% over NPR 5,000,000  _(PKF FY 2082/83 booklet p.2)_
- **1% first-band carve-out** — 0% if SSF-enrolled / sole prop / pension  _(PKF FY 2082/83 booklet p.2)_
- **Retirement fund deduction cap** — lower of 1/3 income / 500,000 / actual  _(PKF FY 2082/83 booklet p.2)_
- **Life / health / building insurance caps** — 40,000 / 20,000 / 5,000  _(PKF FY 2082/83 booklet pp.2--3)_
- **Remote-area allowance** — up to 50,000 (A--E)  _(PKF FY 2082/83 booklet p.3)_
- **Female tax credit** — 10% of tax liability (remuneration-only)  _(PKF FY 2082/83 booklet p.3)_
- **Non-resident employment income** — 25% flat  _(PKF FY 2082/83 booklet p.3)_
- **SSF total / employer / employee** — 31% / 20% / 11%  _(Social Security Act 2074; SSF; Lockton)_
- **SSF per-scheme split** — [RESEARCH GAP — verify with SSF]  _(secondary (conflicting))_
- **SSF salary ceiling** — NPR 350,000/mo [RESEARCH GAP — verify with SSF]  _(secondary)_
- **Provident Fund (non-SSF)** — 10% + 10% of basic  _(Labour Act 2074)_
- **Gratuity (non-SSF)** — 8.33% of basic  _(Labour Act 2074)_
- **Monthly minimum wage** — NPR 19,550 (basic 12,170 + dearness 7,380)  _(Nepal Gazette 21 Jul 2025; wageindicator.org)_
- **eTDS deadline** — within 25 days of month-end  _(unionnepal.com; estartupnepal.com)_
- **SSF deadline** — within 25 days [RESEARCH GAP — corroborate]  _(secondary (lawsagar.com))_
- **Annual return deadline** — Ashoj end (~mid-Oct)  _(taxconsultantnepal.com; IRD)_
- **Mandatory return threshold** — taxable income over NPR 4,000,000  _(PKF FY 2082/83 booklet p.3 (Sec. 96))_
- **TDS late-filing penalty** — NPR 100/day, cap 5,000 + 2.5% p.a. [RESEARCH GAP]  _(unionnepal.com)_
- **TDS late-deposit interest** — 15% p.a. + 1.5%/month [RESEARCH GAP]  _(unionnepal.com)_
- **SSF late penalty** — 2× unpaid + 10% p.a. interest  _(Social Security Act 2074 (secondary))_

### Test Suite (recompute and assert)

1. **Single, SSF-enrolled, taxable 800,000 → annual tax = 40,000** (0 + 20,000 + 20,000). ✓
2. **Single, non-SSF, taxable 800,000 → annual tax = 45,000** (5,000 + 20,000 + 20,000). ✓ The 1% first band adds exactly 5,000 vs Test 1.
3. **Married, SSF-enrolled, taxable 1,500,000 → annual tax = 200,000** (0 + 20,000 + 60,000 + 120,000). ✓
4. **Female single, SSF, taxable 1,000,000 → tax before credit 80,000; credit 8,000; after = 72,000.** ✓
5. **Cumulative tax (single, 1% band) at 2,000,000 = 385,000** (5,000 + 20,000 + 60,000 + 300,000). ✓
6. **Cumulative tax (married, 1% band) at 2,000,000 = 356,000** (6,000 + 20,000 + 60,000 + 270,000). ✓
7. **SSF on basic 40,000 → employee 4,400 (11%), employer 8,000 (20%), total 12,400 (31%).** ✓
8. **Non-resident employment 1,200,000 → tax = 300,000 (flat 25%).** ✓
9. **SSF effective rates: employer 20%, employee 11%, total 31% of basic.** ✓
10. **Minimum wage 19,550 = basic 12,170 + dearness 7,380.** ✓

## PROHIBITIONS

- **Married-couple thresholds default** — NEVER apply the married-couple thresholds without a confirmed couple election — default to single.  _(PROHIBITIONS section)_
- **1% first-band SSF drop condition** — NEVER drop the 1% first-band Social Security Tax unless the employee actually contributes to the SSF (or is a sole proprietor / on pension income).  _(PROHIBITIONS section)_
- **Non-resident flat rate enforcement** — NEVER apply resident slabs or credits to a non-resident — non-resident employment income is a flat 25%.  _(PROHIBITIONS section)_
- **SSF applies regardless of employer size** — NEVER skip SSF because an employer is small — it applies at ≥1 employee, no threshold.  _(PROHIBITIONS section)_
- **Employer SSF contribution required** — NEVER deduct only 11% as 'the SSF' and forget the 20% employer contribution on top.  _(PROHIBITIONS section)_
- **Female tax credit eligibility** — NEVER claim the female tax credit unless the employee is female with remuneration-only income.  _(PROHIBITIONS section)_
- **Deduction caps enforcement** — NEVER exceed the statutory deduction caps (retirement / insurance / remote-area).  _(PROHIBITIONS section)_
- **SSF salary ceiling / scheme split flag** — NEVER rely on the unverified SSF salary ceiling or a per-scheme SSF split without flagging the RESEARCH GAP and confirming with the SSF.  _(PROHIBITIONS section)_
- **25-day deadline enforcement** — NEVER miss the 25-day eTDS or SSF deadlines — penalties and interest apply.  _(PROHIBITIONS section)_
- **Estimated output labeling** — NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Nepali chartered accountant / registered auditor.  _(PROHIBITIONS section)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed chartered accountant or registered auditor in Nepal) before implementation.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
