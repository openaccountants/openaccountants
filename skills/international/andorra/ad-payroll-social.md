---
name: andorra-payroll
description: Use this skill whenever asked about Andorra payroll processing for employed persons. Trigger on phrases like "Andorra payroll", "CASS contributions", "IRPF withholding Andorra", "employee CASS", "employer CASS", "retencions Andorra", "CASS-0031", "salari Andorra", "net salary Andorra", "gross to net Andorra", "withholding tax Andorra", "Andorra social security", "retenidor Andorra", "DTF withholding", "IRNR Andorra", "non-resident tax Andorra", "minimum wage Andorra", "salari mínim Andorra", or any question about computing employee pay, withholding tax, or social security contributions for Andorra-based employees. This skill covers IRPF employment income withholding, CASS contributions (employee and employer), non-resident income tax (IRNR), minimum wage, mandatory registration obligations, payslip requirements, and filing obligations. ALWAYS read this skill before processing any Andorra payroll.
jurisdiction: AD
domain: payroll
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# andorra-payroll

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Principality of Andorra (Principat d'Andorra) |
| Currency | EUR only |
| Standard pay frequency | Monthly (most common) |
| Tax year | Calendar year (1 January -- 31 December) |
| Income tax system | IRPF (Impost sobre la Renda de les Persones Físiques) -- progressive withholding by employer |
| Tax authority | Departament de Tributs i de Fronteres (DTF) |
| Social security authority | CASS (Caixa Andorrana de Seguretat Social) |
| Key legislation | Llei 5/2014 (IRPF); Decret 596/2023 (IRPF regulation); Llei 17/2008 (CASS framework); Decret 4/2025 (minimum wage 2025); Decret 16/2025 (average salary 2025) |
| Filing portal | e-tramits.ad (IRPF); cass.ad (CASS) |
| Official language | Catalan |
| Validated by | Pending -- requires sign-off by a qualified Andorran tax adviser (assessor fiscal) |
| Skill version | 0.1 |

## Section 2 -- Income Tax Withholding (IRPF)

Employers must register as a **retenidor** (withholding agent) with the DTF and withhold IRPF monthly from employees' gross wages as a payment on account of the employee's final annual IRPF liability. The DTF operates an automatic regularisation system: employees with only employment income generally do not need to file a full annual return if withholding has been correctly applied. *(Source: Govern d'Andorra IRPF FAQs; Rivermate guide)*

### 2.1 Statutory IRPF Rate Structure (Annual General Base)

- **Statutory rate structure overview** — The statutory structure has a 0% band up to €24,000 and a 10% marginal rate above €40,000. A bonification (tax relief) of up to €800 reduces the effective rate on the €24,001--€40,000 slice to approximately 5%.  _(Llei 5/2014; e-tramits.ad IRPF portal)_

**Statutory IRPF Rate Table**  _(Llei 5/2014; Assessors Associats)_

| Annual Taxable Income | Marginal Rate | Note |
| --- | --- | --- |
| €0 -- €24,000 | 0% | General personal minimum exemption |
| €24,001 -- €40,000 | ~5% effective | 10% statutory rate with bonification up to €800 reducing effective rate |
| Above €40,000 | 10% | *(Source: Llei 5/2014; Assessors Associats)* |

**Important:** The 5% effective rate is not a literal bracket -- it results from a bonification mechanism. The statutory marginal rate is 10% throughout the taxable base; the bonification creates the stepped effective rate in practice.

### 2.2 Employer Withholding Rate Table (Retencions)

- **Withholding rate maximum cap** — The actual withholding rates applied by employers to annual gross salary are graduated and significantly lower than the marginal statutory rates. The maximum withholding rate is 7%, even though the statutory marginal rate reaches 10%; the gap is reconciled at the annual IRPF filing.  _(Assessors Associats; Andorra Difusió report on 7% maximum withholding cap)_

**Employer Withholding Rate Table**  _(Assessors Associats; Andorra Difusió report on 7% maximum withholding cap)_

| Annual Gross Salary | Withholding Rate |
| --- | --- |
| €0 -- €27,000 | 0% |
| €27,001 -- €30,000 | 0.5% |
| €30,001 -- €40,000 | 1% |
| €40,001 -- €50,000 | 2% |
| €50,001 -- €60,000 | 3% |
| €60,001 -- €70,000 | 4% |
| €70,001 -- €80,000 | 4.5% |
| €80,001 -- €90,000 | 5% |
| €90,001 -- €100,000 | 5.5% |
| €100,001 -- €120,000 | 6% |
| €120,001 -- €150,000 | 6.5% |
| Above €150,000 | 7% (maximum) |

- **Monthly withholding computation** — Monthly withholding = (Annual gross salary × Withholding rate) ÷ 12  _(Assessors Associats)_

The DTF determines the applicable withholding percentage for each employee taking into account that employee's personal deductions (children, ascendants, mortgage relief). The table above represents the standard rates before personal deduction adjustments. Employees may request a higher withholding rate via Form 317.

### 2.3 IRPF Deductions Affecting Tax Base

**IRPF Deductions Table**  _(aaa.ad 2025 tax return guide; Bloomberg Tax IRPF 2025 filing announcement)_

| Deduction | Annual Amount |
| --- | --- |
| General personal minimum (exemption) | €24,000 |
| Per qualifying dependent child (<25 yrs, living with taxpayer, income ≤ minimum wage) | €1,000 |
| Supplemental for dependent child in higher education | €300 additional |
| Per qualifying ascendant (>65 yrs, living with taxpayer, income <€12,000) or descendant <25 | €750 |
| Primary residence mortgage: 50% of annual mortgage payments, capped | €5,000/taxpayer/year |
| Affordable rental housing investment: 50%, capped | €5,000/taxpayer/year |

### 2.4 Savings / Investment Income (Base de l'Estalvi)

**Savings/Investment Income Table**  _(Elysium Consulting / Invicoandorra)_

| Income Type | Rate |
| --- | --- |
| First €3,000 savings/investment income per year | 0% (exempt) |
| Savings/investment income above €3,000 | 10% flat |
| Dividends from Andorran entities (corporate tax already paid) | Fully exempt |
| Foreign dividends | 10% (unless treaty relief applies) |

### 2.5 Capital Gains -- Special Exemptions

- Shares with ≤25% stake: exempt
- Any asset held ≥10 years: exempt
- Real estate capital gains: generally exempt if held ≥10 years

## Section 3 -- Non-Resident Income Tax (IRNR)

Employers are responsible for deducting and remitting IRNR on behalf of non-resident employees working in Andorra. *(Source: Govern.ad IRNR page)*

**IRNR Table**  _(Govern.ad IRNR page; Myexpatexperts tax calendar; Remotepeople)_

| Item | Detail |
| --- | --- |
| Rate | 10% flat on Andorran-source employment income |
| Base | Gross employment income exercised in Andorra |
| Dividends / interest paid to non-residents | Generally not subject to IRNR |
| Filing frequency | Quarterly |
| Quarterly deadlines | January, April, July, October (end of each quarter) |
| Treaty relief | May apply for residents of Spain, France, Portugal, Luxembourg, Liechtenstein, Malta, Cyprus, Hungary, San Marino, UAE |

## Section 4 -- CASS Social Security Contributions

### 4.1 Governing Framework

- **CASS governing framework** — CASS (Caixa Andorrana de Seguretat Social) is the public social security body established under Llei 17/2008. The 2025 reference average global salary was set at €2,560.99/month by Decret 16/2025 (29 January 2025).  _(CASS official site; Elysium Consulting 2025 CASS guide)_

### 4.2 Contribution Rates -- Standard Salaried Employees (2025)

**Standard Contribution Rates Table**  _(CASS official page cass.ad/cotitzacions-recarrecs-sancions; Elysium Consulting)_

| Branch | Employee | Employer | Total |
| --- | --- | --- | --- |
| General Branch (health, maternity/paternity, temporary disability, death/orphan benefits) | 3.0% | 7.0% | 10.0% |
| Retirement Branch (retirement, widow/widower, survivor pensions) | 3.5% | 8.5% | 12.0% |
| **TOTAL** | **6.5%** | **15.5%** | **22.0%** |

**Special case -- employee already drawing a retirement pension**  _(CASS official page cass.ad/cotitzacions-recarrecs-sancions; Elysium Consulting)_

| Branch | Employee | Employer | Total |
| --- | --- | --- | --- |
| General Branch only | 3.0% | 7.0% | 10.0% |
| Retirement Branch | Not applicable | Not applicable | -- |
| **TOTAL** | **3.0%** | **7.0%** | **10.0%** |

### 4.3 Occupational Accident Coverage

- **Occupational accident coverage** — There is no separate employer occupational risk premium. Occupational accidents and diseases are covered within the General Branch. The standard 15.5% employer contribution subsumes this coverage.  _(Elysium Consulting CASS 2025 guide)_

### 4.4 Contribution Base

- **Included in contribution base** — Regular salary, supplements, bonuses, benefits-in-kind (housing, meals, company car), indemnities.
- **Excluded from contribution base** — Tips, company liberalities, meal/travel expense reimbursements, employer contributions to supplementary (occupational) pension plans.
- **CASS contribution ceiling (self-employed, 2025)** — €3,520.36/month (137.5% of the average monthly salary)  _(CASS official pages; Elysium Consulting)_

**Ceiling (plafó):** A formal government-set contribution ceiling exists under Llei 17/2008. The exact 2025 ceiling for salaried employees is **[RESEARCH GAP -- reviewer to confirm: contact CASS directly or check latest BOPA decree]**. For self-employed workers the 2025 ceiling is €3,520.36/month (137.5% of the average monthly salary). *(Source: CASS official pages; Elysium Consulting)*

**Floor:** No explicit contribution floor for salaried workers confirmed in public sources. **[RESEARCH GAP -- reviewer to confirm with CASS]**

## Section 5 -- Minimum Wage (Salari Mínim Interprofessional)

**Minimum Wage 2025 Table**  _(Summit Advisors; Auge Legal & Fiscal)_

| Metric | 2025 Figure |
| --- | --- |
| Hourly rate | €8.35 |
| Monthly rate (40-hour week) | €1,447.33 |
| Annual rate (×12) | €17,367.96 |
| Effective date | 1 January 2025 |
| Increase vs. 2024 | +5.2% |
| Legal instrument | Decret 4/2025 |

- **2026 minimum wage (for reference)** — €8.80/hour and €1,525.33/month effective 1 January 2026  _(Playroll)_

## Section 6 -- Conservative Defaults

**Conservative Defaults Table**

| Parameter | Conservative Default | Basis |
| --- | --- | --- |
| IRPF withholding rate | Per withholding table based on annual gross salary; 0% if annual gross ≤€27,000 | Decret 596/2023; Assessors Associats |
| Employee CASS | 6.5% of gross salary | CASS official; Llei 17/2008 |
| Employer CASS | 15.5% of gross salary | CASS official; Llei 17/2008 |
| CASS contribution ceiling (salaried) | [RESEARCH GAP -- apply contributions on full gross until ceiling confirmed with CASS] |  |
| Tax residency status | Resident (apply IRPF rates) | Only override if non-residency is confirmed |
| Personal deductions | None (standard: no adjustments) | Deductions require employee declaration |
| Pay frequency | Monthly | Standard Andorran practice |
| Currency | EUR | Only currency used in Andorra |

## Section 7 -- Required Inputs

Before computing Andorra payroll, you MUST have:

1. **Employee tax residency status** -- resident (IRPF) or non-resident (IRNR)
2. **Annual gross salary** -- to determine correct withholding rate band
3. **Monthly gross salary** -- for computation of monthly amounts
4. **CASS registration status** -- confirm both employer and employee are registered
5. **Personal deduction declarations** -- children, ascendants, mortgage if applicable (affects DTF-determined withholding rate)
6. **Pension-drawing status** -- if employee is already receiving a retirement pension, different CASS rates apply
7. **Employment start date** -- for pro-rating partial months

### Refusal Catalogue

- **Unknown residency status** — Cannot determine whether IRPF or IRNR applies
- **Salary in non-EUR currency** — Andorra uses EUR exclusively; flag if any other currency is mentioned
- **Double-taxation treaty claim** — Treaty benefit cannot be applied without knowing employee's country of tax residence and the specific treaty provisions -- direct to qualified adviser
- **CASS ceiling uncertainty** — If salary may exceed the (unconfirmed) CASS ceiling, output must be flagged as potentially overstated and marked [RESEARCH GAP]
- **Benefits-in-kind valuation** — Housing, vehicles, and meal benefits require valuation -- do not guess
- **Termination payments** — Indemnification amounts under Andorran labour law require legal advice before payroll treatment can be determined

## Section 8 -- Transaction and Payment Pattern Library

This section enables recognition and classification of Andorra-specific payroll entries on bank statements and in accounting records.

### 8.1 Employee Bank Statement Patterns (Salary Credits)

**Employee Bank Statement Patterns Table**

| Pattern Observed | Classification |
| --- | --- |
| NOMINA, SALARI, SUELDO | Net salary payment (credit to employee) |
| PAGAMENT NOMINA [employer name] | Net salary payment |
| TRANSFERENCIA NOMINA | Net salary payment |
| BONUS, PRIMA, GRATIFICACIÓ | Discretionary bonus or one-off payment |
| LIQUIDACIÓ, INDEMNITZACIÓ | Termination payment -- requires separate tax/CASS analysis |
| PAGA EXTRA | Extra salary payment (if contractual 13th/14th month exists) |
| DIETES, DESPLAÇAMENT | Per diems / travel reimbursement -- generally not subject to CASS/IRPF if genuine expense reimbursement |

### 8.2 Employer Bank Statement Patterns (Payroll Debits)

**Employer Bank Statement Patterns Table**

| Pattern Observed | Classification |
| --- | --- |
| CASS-0031, COTITZACIO CASS | Monthly CASS contribution payment (employer + employee shares) |
| CASS [employer number] | CASS remittance |
| DTF IRPF, RETENCIO IRPF, TRIBUTS | IRPF withholding remittance to DTF |
| DTF IRNR, RETENCIO IRNR | IRNR withholding remittance (non-resident employees) |
| PAGAMENT NOMINES, TRANSFERENCIES NOMINA | Bulk salary disbursement to employees |
| SEGURETAT SOCIAL, COTITZACIONS | Social security contributions (CASS) |

### 8.3 CASS-0031 Form Classification

- **CASS-0031 form** — The CASS-0031 form ("Full de declaració de cotitzacions i retencions IRPF/IRNR") is a combined monthly declaration covering both CASS contributions and IRPF/IRNR withholdings. A single monthly payment/declaration to CASS covers both obligations for most employers.  _(CASS-0031 form page cass.ad/tramits/cass-0031)_

### 9.1 CASS Monthly Declaration (CASS-0031)

**CASS Monthly Declaration Table**  _(CASS official CASS-0031 page; CASS contributions page)_

| Item | Detail |
| --- | --- |
| Form | CASS-0031 "Full de declaració de cotitzacions i retencions IRPF/IRNR" |
| Frequency | Monthly |
| Deadline | 1st--15th of the month following the salary payment period |
| Content | Employer CASS (15.5%), employee CASS (6.5%), IRPF/IRNR withholdings |
| Who pays | Employer remits both shares (deducts employee 6.5% from wages, adds employer 15.5%) |
| Portal | cass.ad |

### 9.2 IRPF Withholding Forms (Filed with DTF)

**IRPF Withholding Forms Table**  _(e-tramits.ad IRPF forms page; Govern.ad forms)_

| Form | Purpose |
| --- | --- |
| Form 310 | Self-assessment of withholdings on employment income NOT subject to CASS (e.g., some border-worker income) |
| Form 312 | Self-assessment of withholdings on employment income subject to CASS obligations |
| Form 312-A | Additional or late withholding self-assessments |
| Form 315 | Communication of withholding data to individual employee |
| Form 316 | Notification of changes in withholding amount |
| Form 317 | Employee request for higher withholding percentage |
| Form 311 | Annual withholding summary (non-CASS employment income) |
| Form 311-A | Annex to Form 311 |
| Form 340 | Self-assessment of withholdings on investment/movable capital income |
| Form 341 | Annual summary of capital income withholdings |

Because CASS-0031 already captures the monthly IRPF remittance for most salaried employees (combined CASS + IRPF declaration), Forms 310/312 may apply primarily for out-of-CASS situations. **[RESEARCH GAP -- reviewer to confirm the exact interaction between CASS-0031 and the separate DTF forms for a typical Andorran employer]**

### 9.3 IRPF Withholding Payment Frequency and Deadlines

**IRPF Withholding Payment Frequency Table**  _(Govern.ad IRPF consultation; multiple secondary sources consistently citing "20 days" deadline)_

| Item | Detail |
| --- | --- |
| Frequency | Monthly or quarterly, depending on employer size and total withholding volume |
| Deadline | Within the first 20 days of the month following the withholding period |
| Quarterly periods | April, July, October, January |
| Annual employer summary deadline | [RESEARCH GAP -- described as end of February/March by secondary sources; verify exact date with DTF] |

### 9.4 Annual IRPF Return (Employee-Level -- Form 300)

**Annual IRPF Return Table**  _(e-tramits.ad IRPF portal; Bloomberg Tax; WIT Andorra)_

| Item | Detail |
| --- | --- |
| Who must file | Residents with: income from economic activity; OR gross employment/property income ≥€24,000; OR unwithheld savings income ≥€3,000; OR any capital gain/loss |
| Filing window | 1 April -- 30 September of the year following the income year |
| For 2025 income | 1 April 2026 -- 30 September 2026 |
| Method | Online (MIL credentials or electronic certificate) or in-person with prior appointment |
| Main form | Form 300 (with annexes 300-A through 300-E) |

### 9.5 Employer Registration Requirements

**Employer Registration Requirements Table**  _(Elysium Consulting CASS 2025; Playroll EOR guide; e-tramits.ad IRPF portal)_

| Registration | Timing | Authority |
| --- | --- | --- |
| CASS employer registration (obtain employer number) | Before employee's first day of work | CASS (cass.ad) |
| New hire notification to CASS | Within 5 days of hire | CASS |
| DTF retenidor (withholding agent) registration | Before paying any employment income subject to withholding | DTF (Baixada del Molí, 26, Andorra la Vella; +376 885 005; impostos@govern.ad) |
| Andorran Company Registry (Registre de Comerç) | Before employing staff | Registre de Comerç |

### 10.1 CASS Late Payment Surcharges

**CASS Late Payment Surcharges Table**  _(Effective from 1 July 2022 reform; CASS official contributions page)_

| Lateness | Surcharge |
| --- | --- |
| Up to 1 month late | 5% of unpaid amount |
| 1 -- 6 months late | 10% of unpaid amount |
| More than 6 months late | 20% of unpaid amount |

- **Serious CASS infractions** — Serious CASS infractions (administrative sanctions -- range 501--20,000 jubilation points): - Filing declarations more than 3 months late - Intentionally falsifying contribution data - Withholding employee contributions without remitting them to CASS

### 10.2 IRPF Penalties

Specific penalty percentages for IRPF late filing or late withholding remittance are **[RESEARCH GAP -- not confirmed in reviewed sources; consult DTF directly for the sanction schedule under Llei 5/2014 and Decret 596/2023]**.

### 10.3 Minimum Wage Violation Fines

- **Minimum wage violation fines** — Fines: €500 -- €10,000 per violation.  _(Playroll EOR guide)_

## Section 11 -- Worked Examples

### Example 1 -- Minimum Wage Employee (Resident, No Personal Deductions)

**Example 1 table**  _(Decret 4/2025)_

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | Per Decret 4/2025 | €1,447.33 |
| Employee CASS (6.5%) | 1,447.33 × 6.5% | −€94.08 |
| IRPF withholding (0%) | Annual gross €17,368 < €27,000 threshold → 0% | €0.00 |
| **Net pay to employee** | 1,447.33 − 94.08 | **€1,353.25** |
| Employer CASS (15.5%) | 1,447.33 × 15.5% | €224.34 |
| **Total employer cost** | 1,447.33 + 224.34 | **€1,671.67** |

**Profile:** Resident employee, single, no dependants, annual gross = €17,367.96 (minimum wage 2025: €1,447.33/month). *(Source: Decret 4/2025)*

### Example 2 -- Mid-Range Salary (Resident, No Personal Deductions)

**Example 2 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 50,000 ÷ 12 | €4,166.67 |
| Employee CASS (6.5%) | 4,166.67 × 6.5% | −€270.83 |
| IRPF withholding (2%) | Annual €40,001--€50,000 band → 2%; (50,000 × 2%) ÷ 12 | −€83.33 |
| **Net pay to employee** | 4,166.67 − 270.83 − 83.33 | **€3,812.51** |
| Employer CASS (15.5%) | 4,166.67 × 15.5% | €645.83 |
| **Total employer cost** | 4,166.67 + 645.83 | **€4,812.50** |

**Profile:** Resident employee, annual gross = €50,000. Monthly gross = €4,166.67.

### Example 3 -- Higher Salary (Resident, No Personal Deductions)

**Example 3 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 80,000 ÷ 12 | €6,666.67 |
| Employee CASS (6.5%) | 6,666.67 × 6.5% | −€433.33 |
| IRPF withholding (4.5%) | Annual €70,001--€80,000 band → 4.5%; (80,000 × 4.5%) ÷ 12 | −€300.00 |
| **Net pay to employee** | 6,666.67 − 433.33 − 300.00 | **€5,933.34** |
| Employer CASS (15.5%) | 6,666.67 × 15.5% | €1,033.33 |
| **Total employer cost** | 6,666.67 + 1,033.33 | **€7,700.00** |

**Profile:** Resident employee, annual gross = €80,000. Monthly gross = €6,666.67.

### Example 4 -- Lower-Mid Salary at Band Boundary (Resident, No Personal Deductions)

**Example 4 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 30,000 ÷ 12 | €2,500.00 |
| Employee CASS (6.5%) | 2,500.00 × 6.5% | −€162.50 |
| IRPF withholding (0.5%) | Annual €27,001--€30,000 band → 0.5%; (30,000 × 0.5%) ÷ 12 | −€12.50 |
| **Net pay to employee** | 2,500.00 − 162.50 − 12.50 | **€2,325.00** |
| Employer CASS (15.5%) | 2,500.00 × 15.5% | €387.50 |
| **Total employer cost** | 2,500.00 + 387.50 | **€2,887.50** |

**Profile:** Resident employee, annual gross = €30,000. Monthly gross = €2,500.00.

### Example 5 -- Non-Resident Employee

**Example 5 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 36,000 ÷ 12 | €3,000.00 |
| Employee CASS (6.5%) | 3,000.00 × 6.5% | −€195.00 |
| IRNR withholding (10% flat) | 3,000.00 × 10% | −€300.00 |
| **Net pay to employee** | 3,000.00 − 195.00 − 300.00 | **€2,505.00** |
| Employer CASS (15.5%) | 3,000.00 × 15.5% | €465.00 |
| **Total employer cost** | 3,000.00 + 465.00 | **€3,465.00** |

**Profile:** Non-resident employee, annual gross from Andorran employment = €36,000. Monthly gross = €3,000.00. No treaty relief (no confirmed treaty with country of residence).

**Note:** IRNR is filed quarterly (January, April, July, October). The employer remits the deducted IRNR to the DTF each quarter.

### Example 6 -- Employee Already Drawing Retirement Pension (Resident)

**Example 6 table**

| Item | Calculation | Monthly Amount |
| --- | --- | --- |
| Gross salary | 24,000 ÷ 12 | €2,000.00 |
| Employee CASS -- General Branch only (3.0%) | 2,000.00 × 3.0% | −€60.00 |
| IRPF withholding (0%) | Annual gross €24,000 ≤ €27,000 threshold → 0% | €0.00 |
| **Net pay to employee** | 2,000.00 − 60.00 | **€1,940.00** |
| Employer CASS -- General Branch only (7.0%) | 2,000.00 × 7.0% | €140.00 |
| **Total employer cost** | 2,000.00 + 140.00 | **€2,140.00** |

**Profile:** Resident employee who is also receiving a CASS retirement pension, annual gross = €24,000. Monthly gross = €2,000.00.

## Section 12 -- Tier 1 Rules (Always Apply)

These rules have no exceptions in standard Andorran payroll. Violating any of them constitutes a processing error.

- **Register with CASS before first hire** — Employers must obtain a CASS employer number before the employee's first working day. New hires must be individually registered within 5 days of hire.  _(Llei 17/2008)_
- **Register as retenidor with DTF before paying wages** — The DTF registration as withholding agent is mandatory before any employment income is paid.  _(Llei 5/2014)_
- **Always deduct employee CASS at 6.5%** — For standard employees, 6.5% of gross salary is deducted from employee wages and remitted to CASS with the employer's 15.5% share via CASS-0031. Exception: employees drawing a retirement pension pay 3.0% (general branch only).
- **Always add employer CASS at 15.5%** — Employer must contribute 15.5% of the employee's gross salary. This is an employer cost over and above the gross salary. Exception: employees drawing a retirement pension -- employer pays 7.0% only.
- **File CASS-0031 monthly by the 15th** — The combined CASS contribution and IRPF/IRNR withholding declaration must be submitted to CASS by the 15th of the month following the salary period. Late payment triggers surcharges starting at 5%.
- **Never pay below the minimum wage** — For 2025: €8.35/hour or €1,447.33/month for a standard 40-hour week.  _(Decret 4/2025)_
- **Apply IRPF or IRNR -- never both** — Resident employees are subject to IRPF withholding (per the graduated table). Non-resident employees are subject to IRNR at 10% flat. Determine residency status before computing any withholding.
- **Maximum IRPF withholding rate is 7%** — Even for very high earners, the employer withholding rate is capped at 7% (per Andorra Difusió / Assessors Associats). The gap between withheld and final statutory liability is settled via the annual IRPF return.  _(Andorra Difusió / Assessors Associats)_
- **All amounts in EUR** — Andorra has no domestic currency; all payroll must be computed and paid in EUR.

## Section 13 -- Tier 2 Catalogue (Reviewer Judgement Required)

These items involve judgement, incomplete research data, or complexity that requires a qualified Andorran adviser to resolve before finalising payroll.

**Tier 2 Catalogue Table**

| Situation | Issue | Action Required |
| --- | --- | --- |
| Employee claims personal deductions (children, ascendants, mortgage) | Deductions affect DTF-determined withholding rate; standard table above does not reflect these | Obtain signed employee declaration; submit deduction data to DTF to get adjusted withholding rate |
| Salary exceeds possible CASS ceiling | Exact 2025 CASS contribution ceiling for salaried employees not confirmed in any reviewed public source | Contact CASS directly or check latest BOPA decree before computing on salaries that may be near the ceiling |
| Double-taxation treaty relief claim | Employee is resident in Spain, France, Portugal, Luxembourg, Liechtenstein, Malta, Cyprus, Hungary, San Marino, or UAE | Review specific treaty provisions; do not apply treaty relief without written professional advice |
| Benefits-in-kind (housing, vehicle, meals) | Must be included in CASS contribution base; IRPF valuation rules apply | Obtain market-value assessment; apply per DTF/CASS guidance on benefit valuation |
| Termination/indemnification payments | May be partially or fully exempt from IRPF; CASS treatment depends on nature of payment | Consult Andorran labour and tax adviser before processing |
| Self-employed / mixed-employment status | IRPF applies to employment income; economic activity income has separate rules | Do not commingle in payroll computation; separate income streams require separate IRPF declarations |
| CASS contribution floor for salaried workers | Floor not confirmed in public sources reviewed | Verify with CASS |
| Annual IRPF employer summary deadline | Secondary sources cite "end of February/March" -- exact date not confirmed | Verify exact deadline with DTF before processing year-end reconciliation |
| IRPF penalty schedule | Specific penalty amounts/percentages not published in reviewed sources | Consult DTF or Llei 5/2014 sanction provisions directly |
| CASS-0031 vs. separate DTF forms interaction | Precise workflow for simultaneous CASS and DTF filing needs local practitioner confirmation | Confirm with DTF and a local assessor fiscal before first payroll run |

## Section 14 -- Excel Working Paper Template

Use the following structure when building a monthly payroll working paper. All values in EUR.

```
ANDORRA PAYROLL WORKING PAPER
Month / Year: [MONTH YYYY]
Employer CASS Number: [____________]
DTF Retenidor Number: [____________]

COLUMN HEADERS:
A  Employee Name
B  Employment Type (Resident / Non-Resident / Pension-drawing)
C  Gross Monthly Salary (EUR)
D  Annual Gross (=C×12 or actual annual if variable)
E  Withholding Rate (from Section 2.2 table, or 10% IRNR if non-resident)
F  Monthly IRPF/IRNR Withholding (=D×E/12)
G  Employee CASS Rate (6.5% standard; 3.0% if pension-drawing)
H  Employee CASS Deduction (=C×G)
I  Net Pay to Employee (=C−F−H)
J  Employer CASS Rate (15.5% standard; 7.0% if pension-drawing)
K  Employer CASS Contribution (=C×J)
L  Total Employer Cost (=C+K)
M  Notes (treaty claim, deductions applied, CASS ceiling reached, etc.)

TOTALS ROW:
Sum Column C  = Total Gross Payroll
Sum Column F  = Total IRPF/IRNR to remit to DTF (or via CASS-0031)
Sum Column H  = Total Employee CASS (remitted via CASS-0031)
Sum Column K  = Total Employer CASS (remitted via CASS-0031)
Sum Column I  = Total Net Wages (bank transfer to employees)
Sum Column L  = Total Employer Payroll Cost

RECONCILIATION CHECK:
Total Gross (ΣC) = Total Net (ΣI) + Total Employee CASS (ΣH) + Total IRPF/IRNR (ΣF) ✓
Total CASS-0031 Remittance = Total Employee CASS (ΣH) + Total Employer CASS (ΣK)

FILING DEADLINES THIS MONTH:
[ ] CASS-0031 submitted by 15th of following month (CASS)
[ ] IRPF withholding remitted within 20 days of period end (DTF, if separate from CASS-0031)
[ ] IRNR quarterly filing due? (January/April/July/October if non-resident employees)
```

## Section 15 -- Bank Statement / Terminology Reading Guide

### Andorran Payroll Terms (Catalan)

**Andorran Payroll Terms Table**

| Catalan Term | English Equivalent |
| --- | --- |
| Impost sobre la Renda de les Persones Físiques (IRPF) | Personal income tax |
| Impost sobre la Renda dels No-Residents (IRNR) | Non-resident income tax |
| Caixa Andorrana de Seguretat Social (CASS) | Andorran Social Security Fund |
| Departament de Tributs i de Fronteres (DTF) | Department of Taxes and Borders (tax authority) |
| Retenidor | Withholding agent (employer in payroll context) |
| Retencions | Withholdings (tax withheld from salary) |
| Cotitzacions | Contributions (social security contributions to CASS) |
| Salari brut | Gross salary |
| Salari net | Net salary |
| Nòmina | Payslip / payroll |
| Branca general | General branch (CASS health/disability coverage) |
| Branca de jubilació | Retirement branch (CASS pension coverage) |
| Plafó de cotització | Contribution ceiling (CASS cap) |
| Salari mínim interprofessional | National minimum wage |
| Declaració de cotitzacions | Contributions declaration (CASS-0031) |
| Bonificació | Bonification / tax relief |
| Base imposable | Taxable base |
| Base de l'estalvi | Savings income base |

### Typical Payslip Line Items (Andorra)

**Typical Payslip Line Items Table**

| Payslip Line | Meaning |
| --- | --- |
| Salari base / Sou base | Base salary |
| Complements salarials | Salary supplements (seniority, technical, etc.) |
| Cotització CASS (treballador) | Employee CASS contribution deducted |
| Retenció IRPF / Retenció IRNR | Income tax withholding deducted |
| Total percepcions | Total gross earnings |
| Total deduccions | Total deductions |
| Líquid a percebre | Net pay (take-home amount) |

## Section 16 -- Onboarding Fallback

If you are asked to process Andorra payroll and any of the following conditions apply, stop and request clarification before computing:

1. **Residency status unknown:** Ask whether the employee is an Andorran tax resident. IRPF rates and IRNR rates differ substantially.

2. **Salary figures missing:** Both monthly gross and annual gross are needed to identify the correct IRPF withholding rate band.

3. **CASS registration not confirmed:** Ask whether the employer is registered with CASS and whether the employee has been individually registered. If not, payroll cannot legally begin.

4. **Pension-drawing status unknown:** If the employee is of retirement age, ask whether they are already drawing a CASS pension, as this halves the CASS rate.

5. **Treaty claim indicated:** If the employee mentions being resident in Spain, France, or any of the other treaty countries, pause and direct to a qualified adviser before applying any exemption.

6. **Benefit-in-kind components:** If housing, vehicle, or meals are part of the package, flag that these must be valued and included in the CASS base before net pay can be computed.

**Default response when blocked:**
> "I need [missing item] before I can compute an accurate Andorra payroll. Andorra's IRPF withholding rates vary significantly by salary band and residency status, and CASS registration must be confirmed before the first payroll run. Please provide [specific item] or consult a qualified Andorran assessor fiscal."

## Section 17 -- Reference Material

### Key Legislation

**Key Legislation Table**

| Instrument | Subject |
| --- | --- |
| Llei 5/2014 | Personal income tax (IRPF) -- principal act |
| Decret 596/2023 (29 December 2023) | IRPF Regulation -- current withholding rules |
| Llei 17/2008, 3 October | Social security (CASS framework) |
| Decret 16/2025 (29 January 2025) | Sets average global monthly salary at €2,560.99/month |
| Decret 4/2025 | Minimum wage 2025 (+5.2% to €8.35/hour) |

### Official Sources

**Official Sources Table**

| Source | URL |
| --- | --- |
| CASS contributions and surcharges | cass.ad/cotitzacions-recarrecs-sancions |
| CASS-0031 combined declaration form | cass.ad/tramits/cass-0031 |
| e-tramits IRPF portal | e-tramits.ad/tramits/ca/declaracio-de-limpost-sobre-la-renda-de-les-persones-fisiques-irpf/p/tr-irpf |
| e-tramits IRPF forms | e-tramits.ad/tramits/ca/impostos/irpf/formularis |
| Govern.ad IRPF FAQs | govern.ad/ca/l/4194272 |
| Govern.ad IRNR | govern.ad/ca/tematiques/impostos-taxes-i-duana/impostos-en-andorra/impost-sobre-la-renda-dels-no-residents-fiscals-a-andorra |
| Summit Advisors -- minimum wage 2025 | summitadvisors.ad/en/blog/2025-01-31-new-minimum-wage-in-andorra-for-2025-5-2-increase |
| Elysium Consulting -- CASS 2025 | elysiumconsultingfirm.com/en/publications/the-cass-in-andorra-contributions-coverage-and-key-facts-for-2025 |
| Assessors Associats -- withholding table | assessors-associats.com/la-declaracio-dirpf-a-andorra/ |
| Bloomberg Tax -- IRPF 2025 filing | news.bloombergtax.com/daily-tax-report-international/andorra-tax-agency-announces-2025-individual-income-tax-return-filing-deadline-releases-filing-guidance |
| WIT Andorra -- IRPF 2025 guide | wit.ad/en/irpf-andorra-2025-guide-deadlines-and-how-to-file-it/ |

### Double Taxation Treaties (as of 2025)

Andorra has concluded income tax treaties with: Spain, France, Portugal, Luxembourg, Liechtenstein, Malta, Cyprus, Hungary, San Marino, and UAE. *(Source: Remotepeople)*

## Section 18 -- Test Suite

All computations below were verified arithmetically before inclusion. Run these to validate any implementation of this skill.

**Test 1:** Employee, annual gross €20,000, resident, no deductions.
- Annual gross €20,000 < €27,000 → Withholding rate 0%
- Monthly gross: 20,000 ÷ 12 = €1,666.67
- Monthly IRPF: €0.00
- Employee CASS: 1,666.67 × 6.5% = €108.33
- Net pay: 1,666.67 − 0.00 − 108.33 = **€1,558.34**
- Employer CASS: 1,666.67 × 15.5% = €258.33
- Total employer cost: 1,666.67 + 258.33 = **€1,925.00**

**Test 2:** Employee, annual gross €35,000, resident, no deductions.
- Annual gross €35,000 falls in €30,001--€40,000 band → Withholding rate 1%
- Monthly gross: 35,000 ÷ 12 = €2,916.67
- Monthly IRPF: (35,000 × 1%) ÷ 12 = 350.00 ÷ 12 = **€29.17**
- Employee CASS: 2,916.67 × 6.5% = **€189.58**
- Net pay: 2,916.67 − 29.17 − 189.58 = **€2,697.92**
- Employer CASS: 2,916.67 × 15.5% = **€452.08**
- Total employer cost: 2,916.67 + 452.08 = **€3,368.75**
- Reconciliation: 2,697.92 + 29.17 + 189.58 = 2,916.67 ✓

**Test 3:** Employee, annual gross €60,000, resident, no deductions.
- Annual gross €60,000 falls in €50,001--€60,000 band → Withholding rate 3%
- Monthly gross: 60,000 ÷ 12 = €5,000.00
- Monthly IRPF: (60,000 × 3%) ÷ 12 = 1,800 ÷ 12 = **€150.00**
- Employee CASS: 5,000.00 × 6.5% = **€325.00**
- Net pay: 5,000.00 − 150.00 − 325.00 = **€4,525.00**
- Employer CASS: 5,000.00 × 15.5% = **€775.00**
- Total employer cost: 5,000.00 + 775.00 = **€5,775.00**
- Reconciliation: 4,525.00 + 150.00 + 325.00 = 5,000.00 ✓

**Test 4:** Non-resident employee, annual gross €48,000.
- Monthly gross: 48,000 ÷ 12 = €4,000.00
- IRNR (10% flat): 4,000.00 × 10% = **€400.00**
- Employee CASS: 4,000.00 × 6.5% = **€260.00**
- Net pay: 4,000.00 − 400.00 − 260.00 = **€3,340.00**
- Employer CASS: 4,000.00 × 15.5% = **€620.00**
- Total employer cost: 4,000.00 + 620.00 = **€4,620.00**
- Reconciliation: 3,340.00 + 400.00 + 260.00 = 4,000.00 ✓

**Test 5:** Pension-drawing employee, annual gross €18,000, resident.
- Monthly gross: 18,000 ÷ 12 = €1,500.00
- Annual gross €18,000 < €27,000 → IRPF withholding rate 0%
- Employee CASS (general branch only, 3.0%): 1,500.00 × 3.0% = **€45.00**
- Net pay: 1,500.00 − 0.00 − 45.00 = **€1,455.00**
- Employer CASS (general branch only, 7.0%): 1,500.00 × 7.0% = **€105.00**
- Total employer cost: 1,500.00 + 105.00 = **€1,605.00**
- Reconciliation: 1,455.00 + 0.00 + 45.00 = 1,500.00 ✓

**Test 6:** Employee, annual gross €160,000, resident (above maximum withholding band).
- Annual gross €160,000 > €150,000 → Withholding rate 7% (maximum)
- Monthly gross: 160,000 ÷ 12 = €13,333.33
- Monthly IRPF: (160,000 × 7%) ÷ 12 = 11,200 ÷ 12 = **€933.33**
- Employee CASS: 13,333.33 × 6.5% = **€866.67** [NOTE: subject to CASS ceiling -- see Section 4.4 RESEARCH GAP]
- Net pay (before ceiling adjustment): 13,333.33 − 933.33 − 866.67 = **€11,533.33**
- Employer CASS: 13,333.33 × 15.5% = **€2,066.67** [NOTE: subject to CASS ceiling]
- Total employer cost (before ceiling adjustment): 13,333.33 + 2,066.67 = **€15,400.00**
- Reconciliation: 11,533.33 + 933.33 + 866.67 = 13,333.33 ✓

## PROHIBITIONS

- **Residency determination required** — NEVER process Andorra payroll without confirming the employee's tax residency status (resident → IRPF; non-resident → IRNR; never apply both)  _(PROHIBITIONS)_
- **Employer CASS mandatory** — NEVER omit employer CASS (15.5%) -- it is a mandatory employer cost above and beyond gross salary  _(PROHIBITIONS)_
- **Employee CASS mandatory** — NEVER omit employee CASS (6.5%) deduction from net pay  _(PROHIBITIONS)_
- **IRPF withholding cap** — NEVER apply IRPF withholding rate above 7% even if the statutory marginal rate is 10% -- the cap is 7% at source; balance settles at annual filing  _(PROHIBITIONS)_
- **Personal deductions require signed declaration** — NEVER assume an employee's personal deductions without a signed declaration -- use the standard withholding table and flag that deductions may adjust the rate  _(PROHIBITIONS)_
- **Registration confirmation before payroll** — NEVER commence payroll before CASS employer registration and DTF retenidor registration are confirmed  _(PROHIBITIONS)_
- **CASS-0031 deadline** — NEVER miss the CASS-0031 monthly deadline (15th of following month) -- late surcharges begin at 5%  _(PROHIBITIONS)_
- **Minimum wage compliance** — NEVER pay below the statutory minimum wage: €8.35/hour or €1,447.33/month (2025, Decret 4/2025)  _(PROHIBITIONS; Decret 4/2025)_
- **Treaty relief requires opinion** — NEVER apply treaty relief without a written professional opinion confirming eligibility and the specific treaty provisions  _(PROHIBITIONS)_
- **CASS ceiling research gap flag** — NEVER compute CASS contributions on a high-salary employee without flagging the unconfirmed CASS contribution ceiling (RESEARCH GAP -- Section 4.4)  _(PROHIBITIONS)_
- **Computations not definitive** — NEVER present payroll computations as definitive -- always label as estimated and direct to a qualified Andorran assessor fiscal for review  _(PROHIBITIONS)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a qualified Andorran assessor fiscal) before implementation.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
