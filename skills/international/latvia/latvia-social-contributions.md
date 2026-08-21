---
name: latvia-social-contributions
description: Use this skill whenever asked about Latvia mandatory state social insurance contributions (VSAOI / valsts sociālās apdrošināšanas obligātās iemaksas) and the social-insurance side of Latvian payroll. Trigger on phrases like "how much social tax do I pay in Latvia", "VSAOI rate", "Latvian social contributions", "employer 23.59% employee 10.50%", "social insurance self-employed Latvia", "solidarity tax Latvia", "minimum mandatory contributions object", "darba devēja ziņojums", "Latvian payroll contributions", "VID social insurance", "VSAA contributions", or any question about Latvian VSAOI obligations for an employee, pensioner, self-employed person, or worker of a foreign employer. Also trigger when classifying bank statement transactions that relate to VID payments, social-tax debits, payroll withholding, or solidarity tax from Swedbank, SEB, Citadele, Luminor, or other Latvian banks. Also trigger when preparing or reconciling the annual income declaration (Gada ienākumu deklarācija / GID) where VSAOI and the EUR 105,300 cap interact with personal income tax. This skill covers VSAOI rates and splits, the EUR 105,300 annual cap, the 25% solidarity tax, the self-employed minimum-object regime and 10% pension contribution, royalty NSIC, non-taxable minimum and allowances, bank-statement classification, deadlines, penalties, and edge cases. ALWAYS read this skill before touching any Latvian social-contribution or payroll work.
version: 0.1
jurisdiction: LV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Latvia Mandatory State Social Insurance Contributions (VSAOI) -- Social Contributions

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Latvia (Republic of Latvia) |
| Primary Legislation | Law on State Social Insurance (Par valsts sociālo apdrošināšanu) |
| Supporting Legislation | Law on Personal Income Tax (Par iedzīvotāju ienākuma nodokli); Solidarity Tax Law (Solidaritātes nodokļa likums); Law on Amendments to the State Social Insurance Law, Official Gazette 19 Dec 2024 (raised cap to EUR 105,300 from 1 Jan 2025) |
| Tax Authority (admin/collection) | State Revenue Service -- Valsts ieņēmumu dienests (VID); portals vid.gov.lv and eds.vid.gov.lv (EDS) |
| Social Insurance Agency (benefits) | State Social Insurance Agency -- Valsts sociālās apdrošināšanas aģentūra (VSAA / SSIA); vsaa.gov.lv |
| Standard total VSAOI rate | 34.09% (employer 23.59% + employee 10.50%) -- unchanged 2024->2025->2026 |
| Pension-age employee VSAOI | 30.02% total (employer 20.77% + employee 9.25%) |
| Worker of non-registered foreign employer | 31.83% combined (paid by the employee) |
| Self-employed VSAOI (general) | 31.07% (29.36% if state pension age) on declared income; minimum object = 12 x minimum monthly wage = EUR 8,880/year (2025) / EUR 9,360/year (2026); plus 10% pension contribution on actual income when income is below the minimum object (PwC / VSAA) |
| Royalty (author's remuneration) NSIC | 10%, payable by the payer for Latvian-resident recipients; special regime 1 Jan 2025 -- 31 Dec 2027 (PwC) |
| Healthcare earmark | 1 percentage point of the 34.09% total VSAOI is allocated to healthcare funding (VSAA) |
| Annual VSAOI cap (max base) | EUR 105,300 per calendar year (2025-2026; raised from EUR 78,100 in 2024) (VSAA / Grant Thornton) |
| Solidarity Tax | 25% (summary-order effective rate) on annual income above the EUR 105,300 cap; reconciled via the annual declaration (PwC / fm.gov.lv) |
| PIT bands | 25.5% up to EUR 105,300; 33% above; +3% surcharge on total annual income above EUR 200,000 (VID / Grant Thornton) |
| Non-taxable minimum | EUR 510/month / EUR 6,120/year (2025) for all employees (fm.gov.lv / Grant Thornton); pensioners EUR 1,000/month / EUR 12,000/year (2025) [2026 figure: RESEARCH GAP -- reviewer to confirm] |
| Minimum monthly wage | EUR 740 (2025), EUR 780 (2026) (Ministry of Welfare / Cabinet Regulations; 2026 increase adopted 19 Nov 2025) |
| Payment / reporting frequency | Monthly employer report; quarterly self-employed report; annual income declaration |
| Currency | EUR only |
| Validated by | Pending -- requires sign-off by a Latvian-qualified tax professional |
| Validation date | Pending |

**Read this whole section before computing or classifying anything.**

**VSAOI rate overview (by status)**

| Status | Total rate | Employer | Employee | Source |
| --- | --- | --- | --- | --- |
| Standard employee (all insurance types) | 34.09% | 23.59% | 10.50% | VID / VSAA |
| Pension-age / pensioner employee | 30.02% | 20.77% | 9.25% | PwC |
| Worker of non-registered foreign employer | 31.83% combined | -- | paid by worker | PwC |
| Self-employed (general) | 31.07% | n/a | n/a | PwC |
| Self-employed, retirement age | 29.36% | n/a | n/a | PwC |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown worker status | Assume standard employee split 23.59% / 10.50% (34.09% total) |
| Unknown age / retirement status | Assume NOT pension-age (use standard 34.09%); confirm before applying 30.02% |
| Unknown whether foreign employer is registered in Latvia | STOP -- ask; the 31.83% combined rate only applies to non-registered foreign employers |
| Income above EUR 105,300 | Continue VSAOI withholding during the year; flag solidarity tax for annual reconciliation |
| Quarterly income below the minimum object | Employer pays 34.09% on the shortfall (employee VSAOI not increased) |
| Unknown non-taxable minimum eligibility | Use EUR 510/month (2025) for standard employees; pensioner EUR 1,000/month (2025). [2026 figure: RESEARCH GAP] |
| Unknown minimum wage year basis | Use EUR 740 (2025) / EUR 780 (2026) |
| Self-employed minimum object year basis | Use 12 x minimum monthly wage = EUR 8,880/year (2025) / EUR 9,360/year (2026); flag for reviewer |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- worker status (employee / pension-age employee / worker of foreign employer / self-employed) and gross income. Without worker status, default to standard employee but flag for confirmation.

**Recommended** -- whether the worker has reached statutory retirement (pension) age, whether any foreign employer is registered in Latvia, annual gross income (to test against the EUR 105,300 cap and the EUR 200,000 surcharge threshold), quarterly income (to test against the minimum object), and non-taxable-minimum eligibility.

**Ideal** -- the employer's report (Darba devēja ziņojums) from EDS, bank statements showing VID debits and net wage credits, prior-year annual income declaration (GID), and the worker's date of birth (for retirement-age determination).

### Refusal catalogue

- **R-LV-VSAOI-1 -- Foreign-employer registration status unknown** — The 31.83% combined rate applies only where the foreign employer is NOT registered in Latvia. If the employer is registered, the standard 34.09% split applies instead. Cannot select the correct rate without confirming the employer's Latvian registration status. (Trigger: worker is paid by a foreign (non-resident) employer and it is unclear whether that employer is registered as an employer in Latvia.)
- **R-LV-VSAOI-2 -- Self-employed rate sub-splits** — The self-employed VSAOI sub-rates (31.07% general, 29.36% at state pension age, 31.83% for a worker of a non-registered foreign employer) come primarily from PwC rather than the VSAA category tables retrieved in research. The 2025 self-employed minimum object is derived as 12 x EUR 740 = EUR 8,880; the VSAA page retrieved cited the 2026 figure (12 x EUR 780 = EUR 9,360). Verify the applicable rate and the 2025 minimum object against current VSAA category tables before computing. Escalate to a Latvian tax professional. [RESEARCH GAP -- reviewer to confirm self-employed sub-splits and 2025 minimum object] (Trigger: computing self-employed VSAOI and the exact rate split is decisive (31.07% general / 29.36% pension age / 31.83% foreign-employer worker).)
- **R-LV-VSAOI-3 -- Solidarity tax allocation / refund timing** — The solidarity tax effective rate is 25% on annual income above EUR 105,300; during the year contributions are paid at the standard 34.09% and reconciled to 25% in summary order via the annual declaration, with the difference refunded (self-employed/employer ST refund for 2026 expected by September 2027). The internal allocation (1 pp healthcare = 0.5% employer + 0.5% employee, 10 pp credited to PIT, remainder to state pensions) is reported by PwC. Escalate to a Latvian tax professional for refund timing in a specific case. (Trigger: client asks how solidarity tax is split or refunded, or seeks to optimise across the cap.)
- **R-LV-VSAOI-4 -- Minimum-object exemptions and special categories** — Minimum-object exemptions are case-specific and depend on the worker's documented status. Do not waive the minimum object without confirming eligibility. Escalate to a Latvian tax professional. (Trigger: worker may be exempt from the minimum-object regime (parental/sick leave, retirement age, student under 24, parent of 3+ children, parent of disabled child, Group III disabled from 2026).)
- **R-LV-VSAOI-5 -- Arrears, interest, and penalty quantification** — Late-payment interest accrues per day under the Law on Taxes and Duties; the exact current rate was not directly confirmed on the consulted pages. Do not quantify arrears or penalties without a VID statement. Escalate to a Latvian tax professional. [RESEARCH GAP -- reviewer to confirm penalty/interest rate] (Trigger: client has unpaid VSAOI/PIT from prior periods.)

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Latvian social contributions and payroll tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. VSAOI, PIT, and solidarity-tax payments always EXCLUDE from any VAT (PVN) return -- they are payroll/statutory obligations, not taxable supplies. VID is the single collection counterparty for both VSAOI and PIT, so reference text matters for sub-classification.

### 3.1 VID payments -- VSAOI and PIT (employer remittances)

**VID payments -- VSAOI and PIT patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VID, VALSTS IENEMUMU DIENESTS | EXCLUDE -- tax/social remittance | Single VID account; check reference for VSAOI vs PIT |
| VSAOI, SOCIALAS APDROSINASANAS | EXCLUDE -- social contribution | Mandatory state social insurance |
| SOCIALA NODOKLIS, SOC TAX | EXCLUDE -- social contribution | Colloquial label for VSAOI |
| VSAA | EXCLUDE -- social insurance agency | Usually benefit-side, but confirm direction |
| IIN, IEDZIVOTAJU IENAKUMA NODOKLIS | EXCLUDE -- personal income tax (PIT) | Withheld PIT, not VSAOI |

### 3.2 VID/VSAOI debits appearing on specific Latvian banks

**VID/VSAOI debits by bank**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| Swedbank | "VID", "VALSTS IENEMUMU DIENESTS", "NODOKLI" | EXCLUDE -- tax/social remittance |
| SEB banka | "VID NODOKLU MAKSAJUMS", "VSAOI" | EXCLUDE -- tax/social remittance |
| Citadele | "VID", "SOCIALAIS NODOKLIS" | EXCLUDE -- tax/social remittance |
| Luminor | "VID", "NODOKLU SAMAKSA" | EXCLUDE -- tax/social remittance |
| Revolut / Wise | Rare -- Latvian VID remittances normally come from local EUR accounts | If present, EXCLUDE |

### 3.3 Solidarity tax and PIT reconciliation (NOT routine VSAOI)

**Solidarity tax and PIT reconciliation patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SOLIDARITATES NODOKLIS, SOLIDARITY | EXCLUDE -- solidarity tax | Only on income above EUR 105,300; annual reconciliation |
| GID, GADA IENAKUMU DEKLARACIJA | EXCLUDE -- annual declaration settlement | PIT/solidarity reconciliation, not monthly VSAOI |
| IIN PIEMAKSA, PIT TOP-UP | EXCLUDE -- income tax balance | Annual PIT balance, not VSAOI |

### 3.4 Salary and payroll (exclude from VSAOI classification)

**Salary and payroll patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALGA, DARBA SAMAKSA (outgoing) | EXCLUDE -- payroll expense | Net wage paid; not a VSAOI remittance |
| ALGA, NETO ALGA (incoming) | EXCLUDE -- employment income received | Net wage received; VSAOI/PIT already withheld at source |

### 3.5 Social benefits received (NOT contributions)

**Social benefits received patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VSAA PENSIJA, PENSIJA | EXCLUDE -- pension income received | Benefit, not a contribution paid |
| SLIMIBAS PABALSTS, BEZDARBNIEKA PABALSTS | EXCLUDE -- sickness/unemployment benefit | Benefit received, not a contribution |
| VECAKU PABALSTS | EXCLUDE -- parental benefit received | Benefit, not a contribution |

## Section 4 -- Worked examples

Six bank statement classifications and computations for a hypothetical Latvian employer and self-employed consultant. All figures in EUR.

### Example 1 -- Standard monthly VSAOI + PIT remittance (Swedbank)

**Input line:**
`17.02.2025 ; VALSTS IENEMUMU DIENESTS ; DEBIT ; VSAOI/IIN 01.2025 ; -1,234.56 ; EUR`

**Reasoning:**
Matches "VALSTS IENEMUMU DIENESTS" (pattern 3.1) with a January 2025 reference, paid by the 17th (general monthly employer-report deadline). This is the employer's monthly remittance of VSAOI (34.09% standard split) plus withheld PIT. Exclude from PVN (VAT). On a EUR 3,000 gross monthly wage: employer VSAOI = 3,000 x 23.59% = EUR 707.70; employee VSAOI = 3,000 x 10.50% = EUR 315.00.

**Classification:** EXCLUDE from PVN -- payroll tax/social remittance to VID.

### Example 2 -- Net wage credit (employee receiving pay)

**Input line:**
`28.02.2025 ; SIA TECH ALGA 02.2025 ; CREDIT ; NETO ALGA ; +2,130.38 ; EUR`

**Reasoning:**
Matches "NETO ALGA" / salary (pattern 3.4). On EUR 3,000 gross, no dependents: employee VSAOI 10.50% = EUR 315.00. The 10.50% employee VSAOI is deductible from gross before PIT (PwC), and the EUR 510 non-taxable minimum (2025) also reduces the base, so PIT base = 3,000 - 315.00 - 510 = EUR 2,175.00; PIT 25.5% x 2,175.00 = EUR 554.62; net = 3,000 - 315.00 - 554.62 = EUR 2,130.38 (illustrative; dependent/disability allowances would further reduce PIT). This credit is net employment income received -- VSAOI and PIT were already withheld at source.

**Classification:** EXCLUDE from PVN. Net employment income received (no further VSAOI by the employee).

### Example 3 -- Pension-age employee remittance

**Input line:**
`17.03.2025 ; VID ; DEBIT ; VSAOI 02.2025 PENSIONARS ; -901.20 ; EUR`

**Reasoning:**
Matches "VID" (pattern 3.1) with a "PENSIONARS" reference indicating a pension-age employee. The pension-age VSAOI rate is 30.02% total (employer 20.77% + employee 9.25%), not the standard 34.09%. On EUR 3,000 gross: employer 20.77% = EUR 623.10; employee 9.25% = EUR 277.50; total EUR 900.60 (rounding to the line). Confirm retirement-age status from date of birth before applying.

**Classification:** EXCLUDE from PVN -- VSAOI remittance at pension-age rate (30.02%).

### Example 4 -- Income above the EUR 105,300 cap (solidarity tax flag)

**Input line:**
`17.12.2025 ; VID ; DEBIT ; VSAOI/IIN 11.2025 ; -4,820.00 ; EUR`

**Reasoning:**
A high earner whose cumulative annual income exceeds EUR 105,300 (the VSAOI cap; VSAA / Grant Thornton). During the year contributions continue at the standard 34.09%, and income above the cap is reconciled to the 25% summary-order solidarity tax via the annual income declaration (GID), with the difference between 34.09% and 25% refunded (PwC / fm.gov.lv). Allocation of the solidarity tax: 1 pp healthcare (0.5% employer + 0.5% employee), 10 pp to PIT, remainder to the state pension scheme (PwC). Do NOT stop VSAOI withholding mid-year on the assumption the cap removes liability -- the mechanism is reconciliation, not in-year exemption. Flag for reviewer to confirm the year-end solidarity-tax computation.

**Classification:** EXCLUDE from PVN -- VSAOI remittance; flag solidarity tax for annual reconciliation.

### Example 5 -- Self-employed below minimum object (10% pension contribution)

**Input line:**
`17.04.2025 ; VID ; DEBIT ; PASNODARBINATA PENSIJA 10% Q1 2025 ; -150.00 ; EUR`

**Reasoning:**
A self-employed person whose income is below the minimum mandatory contribution object (12 x minimum monthly wage = EUR 8,880/year in 2025; PwC / VSAA). Where the self-employed person's income is below the minimum object, an additional 10% VSAOI is payable to pension insurance on actual income (VSAA). On actual quarterly income of EUR 1,500: 10% x 1,500 = EUR 150.00. A self-employed person whose quarterly income is below 3 x minimum wage (EUR 2,220 in 2025) may file a planned-income declaration to VID by the 17th of the first month of the quarter. Confirm the person is not in an exempt category before finalising.

**Classification:** EXCLUDE from PVN -- self-employed 10% pension contribution on actual income below the minimum object.

### Example 6 -- Self-employed quarterly contribution (2025)

**Input line:**
`17.04.2025 ; VID ; DEBIT ; PASNODARBINATA VSAOI Q1 2025 ; -690.00 ; EUR`

**Reasoning:**
Matches "VID" (pattern 3.1) with a "PASNODARBINATA" (self-employed) reference. The self-employed general VSAOI rate is 31.07% (29.36% if at state pension age) on declared income, with a minimum mandatory contribution object of 12 x minimum monthly wage = EUR 8,880/year in 2025 (EUR 9,360 in 2026) (PwC / VSAA). On a quarterly object of EUR 2,220 (one quarter of EUR 8,880): 31.07% x 2,220 = EUR 689.75 ~ EUR 690 to the line. Where actual income is below the minimum object, an additional 10% pension contribution on actual income applies instead. [RESEARCH GAP -- reviewer to confirm self-employed sub-splits and the 2025 minimum object against VSAA category tables]

**Classification:** EXCLUDE from PVN -- self-employed VSAOI.

## Section 5 -- Tier 1 rules

These rules apply when bank statement data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- Standard VSAOI rate and split

- **Standard VSAOI computation formula** — Total VSAOI = gross_income x 34.09% Employer share = gross_income x 23.59% Employee share = gross_income x 10.50%   (withheld from the worker) (Rate unchanged 2024 -> 2025 -> 2026. 1 percentage point of the total is earmarked for healthcare financing.)  _(vid.gov.lv / vsaa.gov.lv)_

### Rule 2 -- Status determines the rate

**Status determines the rate table**  _(VID / VSAA / PwC)_

| Status | Total | Employer | Employee |
| --- | --- | --- | --- |
| Standard employee | 34.09% | 23.59% | 10.50% |
| Pension-age / pensioner employee | 30.02% | 20.77% | 9.25% |
| Worker of non-registered foreign employer | 31.83% combined | -- | worker pays |
| Self-employed (general) | 31.07% | n/a | n/a |
| Self-employed, retirement age | 29.36% | n/a | n/a |

### Rule 3 -- Annual cap and solidarity tax

- **Annual cap and solidarity tax mechanism** — VSAOI applies to gross income up to the EUR 105,300 annual cap for 2025-2026 (raised from EUR 78,100 in 2024). Income above the cap continues to have VSAOI withheld at the standard rate during the year, then is reconciled as a 25% summary-order Solidarity Tax via the annual income declaration, with the difference between 34.09% paid in-year and 25% refunded. Solidarity-tax allocation: 1 pp healthcare (0.5% employer + 0.5% employee), 10 pp to PIT, remainder to the state pension scheme. The same EUR 105,300 figure is also the boundary between the 25.5% and 33% PIT bands.  _(VSAA / Grant Thornton; PwC / fm.gov.lv; VID / Grant Thornton)_

### Rule 4 -- Self-employed minimum mandatory contribution object

- **Self-employed minimum mandatory contribution object** — The self-employed minimum mandatory contribution object is 12 x the minimum monthly wage per year: - 2025: EUR 8,880/year (12 x EUR 740) [the 2025 figure is derived from 12 x EUR 740; the VSAA page retrieved cited the 2026 figure -- RESEARCH GAP, reviewer to confirm the 2025 figure against the regulation in force] - 2026: EUR 9,360/year (12 x EUR 780) Where the self-employed person's actual income is below the minimum object, a 10% VSAOI pension contribution is payable on actual income. A self-employed person whose quarterly income is below 3 x the minimum monthly wage (EUR 2,220 in 2025) may file a planned-income declaration to VID by the 17th of the first month of the quarter.  _(VSAA / PwC; VSAA / CORVUS)_

### Rule 5 -- Minimum-object exemptions

- **Minimum-object exemptions** — Certain categories are exempt from the minimum-object regime (e.g. persons on parental/sick leave, those who have reached state pension age, students in full-time education, and parents of multiple/disabled children). The exact exemption list and conditions were not confirmed from a primary source in this research pass. Do not waive the minimum object without confirming eligibility against current VSAA guidance. [RESEARCH GAP -- reviewer to confirm the precise exemption categories]

### Rule 6 -- Self-employed mechanics

- **Self-employed mechanics** — Self-employed pay 31.07% general VSAOI (29.36% if at state pension age) on declared income, with the minimum object being 12 x the minimum monthly wage per year (EUR 8,880 in 2025 / EUR 9,360 in 2026). Where actual income is below the minimum object, a 10% VSAOI pension contribution is payable on actual income instead.  _(PwC / VSAA)_

### Rule 7 -- Royalty (author's remuneration) NSIC

- **Royalty NSIC** — A 10% national social insurance contribution (NSIC) on royalties (author's remuneration) is payable by the royalty payer for Latvian-resident recipients; the special royalty regime runs 1 Jan 2025 -- 31 Dec 2027. Professional sportspersons have a minimum contribution base of EUR 860 in 2026. [2025 athlete base: RESEARCH GAP -- reviewer to confirm if needed]  _(PwC; VSAA)_

### Rule 8 -- PIT interaction (progressive)

- **PIT interaction** — Personal income tax (IIN): 25.5% on annual income up to EUR 105,300; 33% above EUR 105,300; plus an additional 3% surcharge on total annual income above EUR 200,000 (from 2025, settled via the annual declaration). PIT is withheld monthly by the employer on income above the non-taxable minimum and allowances.  _(vid.gov.lv)_

### Rule 9 -- Non-taxable minimum and allowances (2025)

**Non-taxable minimum and allowances (2025)**

| Allowance | Amount | Source |
| --- | --- | --- |
| Fixed non-taxable minimum (all employees) | EUR 510/month (EUR 6,120/year) | fm.gov.lv / Grant Thornton |
| Pensioner non-taxable minimum | EUR 1,000/month (EUR 12,000/year) | fm.gov.lv / Grant Thornton |
| Per registered dependent | EUR 250/month (EUR 3,000/year), claimable only at the employer holding the wage tax book | fm.gov.lv / VID |

From 2025 a single fixed non-taxable minimum (EUR 510/month) applies to all employees regardless of gross income, replacing the former differentiated minimum (fm.gov.lv / Grant Thornton). Disability and other special allowances exist but were not part of the figures confirmed in this research pass. [RESEARCH GAP -- reviewer to confirm disability/special allowance amounts and 2026 non-taxable minimum]

### Rule 10 -- Minimum monthly wage

- **Minimum monthly wage** — EUR 740 (2025), EUR 780 (2026); the 2026 increase was adopted on 19 Nov 2025. Sets the floor minimum contribution object and the self-employed minimum-object basis (12 x minimum monthly wage).  _(Ministry of Welfare / Cabinet Regulations)_

### Rule 11 -- Reporting and payment schedule

**Reporting and payment schedule**

| Item | Frequency | Deadline | Source |
| --- | --- | --- | --- |
| Employer's report (Darba devēja ziņojums) | Monthly | Report by the 17th of the month following the reporting month; payment by the 23rd; filed via EDS | VID / CORVUS |
| Self-employed quarterly contribution declaration | Quarterly | By the 17th of the first month of the respective quarter (for self-employed whose quarterly income is below 3 x minimum wage) | VSAA / CORVUS |
| Annual income declaration (gada ienākumu deklarācija / GID) | Annual | Filing window 1 March -- 1 July of the following year (extended to 1 April -- 1 July where income exceeds the differentiated minimum / for higher earners) | VID |

(The exact 1 March vs 1 April start varies by income level -- confirm the precise dates with VID for the relevant taxpayer. [RESEARCH GAP])

## Section 6 -- Tier 2 catalogue

When bank statement data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Retirement-age determination

**Trigger:** It is unclear whether the worker has reached statutory retirement (pension) age.

**Issue:** The pension-age rate is 30.02% (employer 20.77% + employee 9.25%) versus the standard 34.09%. Applying the wrong rate over- or under-collects VSAOI.

**Action:** Flag for reviewer. Confirm date of birth against the statutory retirement age before applying the reduced rate.

### T2-2 -- Foreign employer not registered in Latvia

**Trigger:** A Latvian-resident worker is paid by a foreign (non-resident) employer.

**Issue:** Where the foreign employer is NOT registered as an employer in Latvia, a combined 31.83% rate applies and is paid by the worker. Where the employer IS registered, the standard 34.09% split applies. EU/EEA coordination rules may also affect which country's social security applies (A1 certificates).

**Action:** Flag for reviewer. Confirm employer registration status and any A1 / posting arrangement.

### T2-3 -- Income crossing the EUR 105,300 cap mid-year

**Trigger:** Cumulative annual income approaches or exceeds EUR 105,300.

**Issue:** VSAOI continues during the year; income above the cap is reconciled as a 25% summary-order solidarity tax in the GID, with the 34.09%-to-25% difference refunded. The internal allocation (1 pp healthcare = 0.5% employer + 0.5% employee, 10 pp to PIT, remainder to pensions) is reported by PwC.

**Action:** Flag for reviewer. Do not stop in-year VSAOI; schedule the annual solidarity-tax reconciliation and confirm refund timing for the specific case.

### T2-4 -- Self-employed income below the minimum object

**Trigger:** A self-employed person's actual income is below the minimum mandatory contribution object (12 x minimum monthly wage = EUR 8,880 in 2025 / EUR 9,360 in 2026).

**Issue:** Where income is below the minimum object, a 10% VSAOI pension contribution on actual income applies (VSAA), and a planned-income declaration to VID may be required where quarterly income is below 3 x minimum wage (EUR 2,220 in 2025). Some workers may be in exempt categories.

**Action:** Flag for reviewer. Confirm the applicable mechanism and any exemption eligibility before computing.

### T2-5 -- Self-employed rate sub-splits and 2025 minimum object

**Trigger:** Self-employed VSAOI where the exact rate (31.07% / 29.36% / 31.83%) or the 2025 minimum object is decisive.

**Issue:** The self-employed sub-rates come primarily from PwC rather than the VSAA category tables retrieved; the 2025 minimum object (EUR 8,880) is derived as 12 x EUR 740, while the VSAA page retrieved cited the 2026 figure (EUR 9,360).

**Action:** Flag for reviewer. Verify the applicable rate and the 2025 minimum object against current VSAA category tables. [RESEARCH GAP -- reviewer to confirm self-employed sub-splits and 2025 minimum object]

### T2-6 -- 3% surcharge on high total income

**Trigger:** Total annual income above EUR 200,000.

**Issue:** A 3% PIT surcharge applies on total annual income above EUR 200,000, in addition to the two-band 25.5% / 33% PIT (VID / Grant Thornton / fm.gov.lv). This is settled via the annual declaration and interacts with, but is separate from, VSAOI and the 25% solidarity tax.

**Action:** Flag for reviewer. Reconcile the surcharge in the annual income declaration.

## Section 7 -- Excel working paper template

When producing a Latvian VSAOI/payroll computation, structure the working paper as follows:

```
LATVIA VSAOI / PAYROLL COMPUTATION -- WORKING PAPER
Client: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Worker status:                 [Employee / Pension-age / Foreign-employer worker / Self-employed]
  Reached retirement age:        [YES/NO]
  Foreign employer registered:   [YES/NO/N-A]
  Gross monthly income:          EUR [____]
  Cumulative annual income:      EUR [____]
  Quarterly income:              EUR [____]
  Non-taxable minimum eligible:  [Standard / Pensioner / Other]
  Dependents:                    [____]

VSAOI COMPUTATION (monthly)
  Status rate (total):           [34.09% / 30.02% / 31.83% / 31.07% / 29.36%]
  Employer share:                EUR [____]   (rate [23.59% / 20.77% / n-a])
  Employee share:                EUR [____]   (rate [10.50% / 9.25% / n-a])
  Healthcare earmark (1 pp):     EUR [____]

CAP / SOLIDARITY CHECK
  Annual cap (EUR 105,300):      [Below / At / Above]
  Solidarity tax flag (>cap):    [YES/NO]   effective 25% -- reconcile in GID

SELF-EMPLOYED MINIMUM OBJECT CHECK (if self-employed)
  Minimum object (annual):       EUR [8,880 (2025, 12 x 740) / 9,360 (2026, 12 x 780)]
  Actual income vs object:       [Above / Below]
  10% pension on actual income:  EUR [____]   (only if below the object)
  Exemption applies:             [YES/NO -- specify category]

PIT INTERACTION (monthly)
  Non-taxable minimum:           EUR [510 (2025) / 1,000 pensioner; 2026 = RESEARCH GAP]
  Per-dependent allowance:       EUR [250/dependent -- only at wage-tax-book employer]
  Employee VSAOI deducted first: EUR [____]   (10.50% deductible before PIT)
  Taxable base:                  EUR [____]
  PIT 25.5% (<= EUR 105,300):    EUR [____]
  PIT 33% (> EUR 105,300):       EUR [____]
  3% surcharge (> EUR 200,000):  EUR [____]

REPORTING / DEADLINES
  Employer's report due:         [17th of following month; pay by 23rd]
  Self-employed quarterly decl.: [17th of first month of quarter]
  GID due:                       [1 Mar (or 1 Apr) -- 1 Jul of following year]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How VSAOI / PIT remittances appear on Latvian bank statements

**Swedbank:**
- Description: "VALSTS IENEMUMU DIENESTS", "VID", "NODOKLI"
- Timing: Monthly remittance around the 17th (previous month's payroll)
- Amount: Combined VSAOI + PIT to the single VID account

**SEB banka:**
- Description: "VID NODOKLU MAKSAJUMS", "VSAOI", "IIN"
- Timing: Same monthly cycle
- Amount: Combined or split per reference

**Citadele / Luminor:**
- Description: "VID", "SOCIALAIS NODOKLIS", "NODOKLU SAMAKSA"
- Timing: Same monthly cycle

**Key identification tips:**
1. VSAOI/PIT remittances are outgoing (DEBIT) to VID, never credits.
2. VID is a single collection counterparty -- read the reference (VSAOI, IIN, SOLIDARITATES NODOKLIS) to sub-classify.
3. Net wage credits ("NETO ALGA", "ALGA") are income received with VSAOI/PIT already withheld -- do not double-count.
4. Inbound "VSAA PENSIJA", "SLIMIBAS PABALSTS", "VECAKU PABALSTS" are benefits received, not contributions paid.
5. Self-employed VSAOI references often include "PASNODARBINATA"; quarterly timing around the 23rd.
6. Irregular lump sums to VID may be solidarity tax or annual GID settlements -- read the reference and flag if ambiguous.

### Latvian payroll terminology

**Latvian payroll terminology table**

| Latvian term | English |
| --- | --- |
| VSAOI / valsts sociālās apdrošināšanas obligātās iemaksas | Mandatory state social insurance contributions |
| IIN / iedzīvotāju ienākuma nodoklis | Personal income tax (PIT) |
| Solidaritātes nodoklis | Solidarity tax |
| Bruto alga / Neto alga | Gross wage / Net wage |
| Darba devēja ziņojums | Employer's report |
| Ziņas par darba ņēmējiem | Information about employees |
| Gada ienākumu deklarācija (GID) | Annual income declaration |
| Pašnodarbinātais | Self-employed person |
| Neapliekamais minimums | Non-taxable minimum |
| Minimālā mēneša alga | Minimum monthly wage |
| Pensionārs | Pensioner |

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for VID debits** -- identify all outgoing payments matching Section 3 patterns (VID, VSAOI, IIN, SOLIDARITATES NODOKLIS).
2. **Sub-classify by reference** -- separate routine monthly VSAOI/PIT remittances from solidarity tax and annual GID settlements.
3. **Reverse-engineer the VSAOI rate:**
   - If total VSAOI is approximately 34.09% of gross payroll -> standard employees.
   - If approximately 30.02% -> pension-age employee.
   - If approximately 31.83% combined and paid by the individual -> worker of a non-registered foreign employer.
   - If "PASNODARBINATA" references at ~31.07% -> self-employed.
4. **Test against the cap** -- if any worker's cumulative income approaches EUR 105,300, flag solidarity-tax reconciliation.
5. **Flag for reviewer:** "VSAOI classification derived from bank statement amounts only. Worker status, retirement age, foreign-employer registration, and non-taxable-minimum eligibility have not been independently verified. Reviewer must confirm before finalising payroll or the annual declaration."

### VSAOI rate quick table

**VSAOI rate quick table**

| Status | Total | Employer | Employee | Notes |
| --- | --- | --- | --- | --- |
| Standard employee | 34.09% | 23.59% | 10.50% | All insurance types; 1 pp to healthcare |
| Pension-age employee | 30.02% | 20.77% | 9.25% | Reached statutory retirement age |
| Worker of non-registered foreign employer | 31.83% | -- | combined, paid by worker | EU/EEA coordination may override |
| Self-employed (general) | 31.07% | n/a | n/a | + 10% pension on actual income when below the minimum object |
| Self-employed, retirement age | 29.36% | n/a | n/a | minimum object = 12 x min wage/year |

- **Standard employee** — 34.09%  _(All insurance types; 1 pp to healthcare)_
- **Pension-age employee** — 30.02%  _(Reached statutory retirement age)_
- **Worker of non-registered foreign employer** — 31.83%  _(EU/EEA coordination may override)_
- **Self-employed (general)** — 31.07%  _(+ 10% pension on actual income when below the minimum object)_
- **Self-employed, retirement age** — 29.36%  _(minimum object = 12 x min wage/year)_

### Worked computation examples (2025, standard employee, no dependents, EUR)

- **PIT base formula** — PIT base = gross − employee VSAOI (10.50%, deductible before PIT, per PwC) − EUR 510 non-taxable minimum (fm.gov.lv).  _(PwC / fm.gov.lv)_

**Worked computation examples (2025, standard employee, no dependents, EUR)**

| Gross monthly | Employer VSAOI (23.59%) | Employee VSAOI (10.50%) | Non-taxable min | PIT base (25.5%) |
| --- | --- | --- | --- | --- |
| EUR 740 (min wage) | EUR 174.57 | EUR 77.70 | EUR 510 | EUR 152.30 |
| EUR 1,500 | EUR 353.85 | EUR 157.50 | EUR 510 | EUR 832.50 |
| EUR 3,000 | EUR 707.70 | EUR 315.00 | EUR 510 | EUR 2,175.00 |
| EUR 8,775 (= cap/12) | EUR 2,070.02 | EUR 921.38 | EUR 510 | EUR 7,343.62 |

- **Cap and solidarity tax reconciliation** — Cap reached at EUR 105,300/year = EUR 8,775/month; above this, VSAOI continues during the year and the 25% solidarity tax reconciles annually.  _(VSAA / Grant Thornton)_

### Thresholds and figures

**Thresholds and figures**

| Item | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| Annual VSAOI cap (max base) | EUR 105,300 | EUR 105,300 | VSAA / Grant Thornton (was EUR 78,100 in 2024) |
| Solidarity tax threshold | EUR 105,300 (income above cap) | EUR 105,300 | fm.gov.lv / PwC |
| Self-employed minimum mandatory object | EUR 8,880 (12 x 740) [2025 derived -- RESEARCH GAP] | EUR 9,360 (12 x 780) | VSAA / PwC |
| Self-employed quarterly planned-income declaration threshold | EUR 2,220 (3 x 740) | -- (not confirmed) | VSAA / CORVUS |
| Minimum monthly wage | EUR 740 | EUR 780 | Ministry of Welfare / Cabinet Regulations |
| Non-taxable minimum (all employees) | EUR 510/month (EUR 6,120/yr) | RESEARCH GAP | fm.gov.lv / Grant Thornton |
| Pensioner non-taxable minimum | EUR 1,000/month (EUR 12,000/yr) | RESEARCH GAP | fm.gov.lv / Grant Thornton |
| Per-dependent allowance | EUR 250/month (EUR 3,000/yr) | RESEARCH GAP | fm.gov.lv / VID |
| PIT higher-band threshold (33%) | EUR 105,300 | EUR 105,300 | VID / Grant Thornton |
| 3% surcharge threshold | EUR 200,000 | EUR 200,000 | VID / fm.gov.lv |
| Professional athlete minimum base | RESEARCH GAP | EUR 860 | VSAA |
| Micro-enterprise tax (separate regime) | 25% on turnover | 25% on turnover [confirm before relying] | research data (separate regime) |

- **Annual VSAOI cap (max base)** — EUR 105,300  _(VSAA / Grant Thornton (was EUR 78,100 in 2024))_
- **Solidarity tax threshold** — EUR 105,300 (income above cap)  _(fm.gov.lv / PwC)_
- **Self-employed minimum mandatory object** — EUR 8,880 (12 x 740) [2025 derived -- RESEARCH GAP]  _(VSAA / PwC)_
- **Self-employed quarterly planned-income declaration threshold** — EUR 2,220 (3 x 740)  _(VSAA / CORVUS)_
- **Minimum monthly wage** — EUR 740  _(Ministry of Welfare / Cabinet Regulations)_
- **Non-taxable minimum (all employees)** — EUR 510/month (EUR 6,120/yr)  _(fm.gov.lv / Grant Thornton)_
- **Pensioner non-taxable minimum** — EUR 1,000/month (EUR 12,000/yr)  _(fm.gov.lv / Grant Thornton)_
- **Per-dependent allowance** — EUR 250/month (EUR 3,000/yr)  _(fm.gov.lv / VID)_
- **PIT higher-band threshold (33%)** — EUR 105,300  _(VID / Grant Thornton)_
- **3% surcharge threshold** — EUR 200,000  _(VID / fm.gov.lv)_
- **Professional athlete minimum base** — RESEARCH GAP  _(VSAA)_
- **Micro-enterprise tax (separate regime)** — 25% on turnover  _(research data (separate regime))_

### Penalties

**Penalties**

| Penalty | Rate |
| --- | --- |
| Late payment of VSAOI/PIT (nokavējuma nauda) | Late-payment interest accrues per day on overdue VSAOI/PIT; VID applies statutory late-payment charges and may add fines for under-declaration. The exact daily rate was not confirmed from a primary source in this research. [RESEARCH GAP -- reviewer to confirm current daily rate with VID before publishing] |
| Under-declaration / late filing | Additional fines may apply under VID procedures. [RESEARCH GAP -- reviewer to confirm] |

- **Late payment of VSAOI/PIT (nokavējuma nauda)** — Late-payment interest accrues per day on overdue VSAOI/PIT; VID applies statutory late-payment charges and may add fines for under-declaration. The exact daily rate was not confirmed from a primary source in this research. [RESEARCH GAP -- reviewer to confirm current daily rate with VID before publishing]
- **Under-declaration / late filing** — Additional fines may apply under VID procedures. [RESEARCH GAP -- reviewer to confirm]

### Authorities and sources

- **VSAA** -- Valsts sociālās apdrošināšanas aģentūra (State Social Insurance Agency): contribution accounting/distribution. "On contributions" -- https://www.vsaa.gov.lv/en/contributions-0
- **VID** -- Valsts ieņēmumu dienests (State Revenue Service): collection, payroll reporting, PIT and solidarity tax; filed via the Electronic Declaration System (EDS). "Personal Income Tax rates" -- https://www.vid.gov.lv/en/personal-income-tax-rates; portal https://www.vid.gov.lv
- **Finanšu ministrija** (Ministry of Finance): "Changes in taxation and finances from 2025" -- https://www.fm.gov.lv/en/changes-taxation-and-finances-2025; "Solidarity tax" -- https://www.fm.gov.lv/en/solidarity-tax; "Non-taxable minimum and tax allowances" -- https://www.fm.gov.lv/en/non-taxable-minimum-and-tax-allowances
- **Labklājības ministrija** (Ministry of Welfare): minimum wage EUR 740 (2025) / EUR 780 (2026) -- https://www.lm.gov.lv/en/article/minimum-wage-latvia-will-be-780-euros
- **PwC Worldwide Tax Summaries** -- Latvia individual other taxes (social security / solidarity tax) -- https://taxsummaries.pwc.com/latvia/individual/other-taxes
- **Grant Thornton Baltic (Latvia)** -- Key tax rates / changes in Latvia 2025 -- https://www.grantthornton.lv/en/insights/key-tax-rates-in-latvia-2025/
- **KPMG Baltics SIA** -- Tax Card 2025 (Latvia) -- https://assets.kpmg.com/content/dam/kpmg/lv/pdf/Taxcard/Tax_card_Latvia_2025_.pdf

**Legislation:** Law "On State Social Insurance" (Par valsts sociālo apdrošināšanu); Solidarity Tax Law (Solidaritātes nodokļa likums); Law "On Personal Income Tax" (Par iedzīvotāju ienākuma nodokli); Cabinet of Ministers Regulations (minimum monthly wage; annual maximum contribution base).

### Test suite

**Test 1:** Standard employee, EUR 3,000 gross/month. -> Employer VSAOI EUR 707.70 (23.59%); employee VSAOI EUR 315.00 (10.50%); total EUR 1,022.70 (34.09%).

**Test 2:** Pension-age employee, EUR 3,000 gross/month. -> Employer EUR 623.10 (20.77%); employee EUR 277.50 (9.25%); total EUR 900.60 (30.02%).

**Test 3:** Worker of a non-registered foreign employer, EUR 2,000 gross/month. -> Combined VSAOI 31.83% = EUR 636.60, paid by the worker.

**Test 4:** Self-employed (2025), actual income EUR 1,500/quarter (below the EUR 8,880/year minimum object). -> 10% VSAOI pension contribution on actual income = 10% x 1,500 = EUR 150.00; planned-income declaration to VID may be required (quarterly income below EUR 2,220).

**Test 5:** Employee, cumulative 2025 income EUR 120,000. -> VSAOI withheld throughout the year on income up to the EUR 105,300 cap; EUR 14,700 above the cap reconciled at the 25% summary-order solidarity tax via the GID = EUR 3,675.00; the difference between contributions paid at 34.09% during the year and 25% is refunded.

**Test 6:** Self-employed (2025), general rate, contribution object = quarterly slice of the EUR 8,880 minimum object (EUR 2,220). -> 31.07% x 2,220 = EUR 689.75 for the quarter. [RESEARCH GAP -- reviewer to confirm self-employed sub-splits and 2025 minimum object against VSAA]

**Test 7:** Standard employee, EUR 740 gross/month (minimum wage), no dependents. -> Employer EUR 174.57; employee VSAOI EUR 77.70; PIT base = 740 - 77.70 - 510 = EUR 152.30; PIT 25.5% x 152.30 = EUR 38.84.

**Test 8:** High earner, total 2025 income EUR 250,000. -> PIT 25.5% to EUR 105,300, 33% above; additional 3% surcharge on EUR 50,000 (income above EUR 200,000) = EUR 1,500, settled via the GID.

### Prohibitions

- NEVER assume the pension-age rate (30.02%) without confirming the worker has reached statutory retirement age.
- NEVER apply the 31.83% non-registered-foreign-employer rate without confirming the employer is NOT registered in Latvia.
- NEVER stop VSAOI withholding mid-year when income exceeds EUR 105,300 -- the cap is reconciled via solidarity tax, not an in-year exemption.
- NEVER apply the self-employed 10% pension contribution to income ABOVE the minimum object -- it applies on actual income only when income is BELOW the minimum object.
- NEVER waive the minimum object without confirming a documented exemption category.
- NEVER rely on the self-employed sub-rates (31.07% / 29.36% / 31.83%) or the 2025 minimum object (EUR 8,880) without verifying against current VSAA category tables -- these come primarily from PwC in this research pass.
- NEVER quantify late-payment interest or arrears without a VID statement -- the exact current rate is not confirmed here.
- NEVER classify a VID debit as VSAOI when the reference indicates PIT (IIN) or solidarity tax -- read the reference.
- NEVER treat inbound VSAA/pension/benefit credits as contributions paid.
- NEVER present VSAOI, solidarity-tax, or PIT figures as definitive -- always label as estimated and direct the client to their EDS account and VID statement.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
