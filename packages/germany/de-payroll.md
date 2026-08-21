---
name: de-payroll
description: Use this skill whenever asked about German payroll tax (Lohnsteuer) computation for EMPLOYEES. Trigger on phrases like "Lohnsteuer", "Gehaltsabrechnung", "payslip Germany", "Steuerklasse", "Brutto Netto", "Solidaritaetszuschlag on wages", "Kirchensteuer on payroll", "Sozialversicherungsbeitraege employee", "Arbeitnehmeranteil", "Arbeitgeberanteil", "Beitragsbemessungsgrenze", "Lohnabrechnung", "Nettolohn", "payroll withholding Germany", "German wage tax", "Lohnsteuerklasse I II III IV V VI", or any question about computing employee payroll deductions in Germany. Covers Lohnsteuer (income tax withholding), Solidaritatszuschlag, Kirchensteuer, and all four branches of Sozialversicherung (RV, KV, PV, AV) from an employer/employee split perspective. This is SEPARATE from the self-employed income tax skill (de-income-tax.md). ALWAYS read this skill before computing any German employee payroll.
version: 1.0
jurisdiction: DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DE Payroll

## Germany Payroll Tax (Lohnsteuer) -- Employee Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Germany (Bundesrepublik Deutschland) |
| Taxes | Lohnsteuer (LSt) + Solidaritatszuschlag (SolZ) + Kirchensteuer (KiSt, if applicable) |
| Social contributions | Rentenversicherung (RV) + Krankenversicherung (KV) + Pflegeversicherung (PV) + Arbeitslosenversicherung (AV) |
| Currency | EUR only |
| Pay period | Monthly (Monat), Weekly (Woche), Daily (Tag), or Annual (Jahr) |
| Primary legislation | Einkommensteuergesetz (EStG) s38--s42f; Solidaritatszuschlaggesetz (SolZG); SGB IV/V/VI/VII/XI |
| Computation source | BMF Programmablaufplan (PAP) -- official algorithm published annually by the Federal Ministry of Finance |
| Tax engine repos | [MarcelLehmann/Lohnsteuer](https://github.com/MarcelLehmann/Lohnsteuer) (Apache-2.0, generated from BMF PAP XML, covers 2006--2026); [jenner/LstGen](https://github.com/jenner/LstGen) (MIT, PAP code generator for Python/Java/JS/Go/PHP) |
| BMF online calculator | [bmf-steuerrechner.de](https://www.bmf-steuerrechner.de) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a German Steuerberater |
| Validation date | Pending |
| Skill version | 1.0 |

### Grundfreibetrag and Tax Brackets (2025, from BMF PAP September 2025 revision)

**Grundfreibetrag and Tax Brackets table**

| Taxable Income (EUR) | Rate | PAP Zone |
| --- | --- | --- |
| 0 -- 12,096 | 0% | Grundfreibetrag (GFB = 12,096) |
| 12,097 -- 17,443 | 14% -- ~24% | Progressive zone 1 (linear-progressive, formula below) |
| 17,444 -- 68,480 | ~24% -- 42% | Progressive zone 2 (linear-progressive, formula below) |
| 68,481 -- 277,825 | 42% | Proportionalzone (flat) |
| 277,826+ | 45% | Reichensteuer |

**Germany uses the BMF Programmablaufplan (PAP) formula, not simple bracket multiplication. The exact formula is in Section 3.**

### Solidaritatszuschlag (SolZ) on Lohnsteuer

**SolZ table**

| Item | Value |
| --- | --- |
| Rate | 5.5% of Lohnsteuer |
| Freigrenze (single / Stkl I, II, IV, V, VI) | Jahreslohnsteuer up to EUR 19,950 -- no SolZ |
| Freigrenze (married / Stkl III) | Jahreslohnsteuer up to EUR 39,900 -- no SolZ |
| Gleitzone (phase-in) | 11.9% marginal rate on LSt between Freigrenze and full-rate zone |

### Kirchensteuer (KiSt)

**KiSt table**

| Item | Value |
| --- | --- |
| Rate (most Lander) | 9% of Lohnsteuer |
| Rate (Bavaria, Baden-Wurttemberg) | 8% of Lohnsteuer |
| Applied only if | Employee is a registered church member (R > 0 in ELStAM) |
| Bemessungsgrundlage | BK output from PAP (Lohnsteuer after certain adjustments) |

### Steuerklassen (Tax Classes)

**Steuerklassen table**

| Class | Who | Tariff | Key Parameters (2025 PAP) |
| --- | --- | --- | --- |
| I | Single, divorced, widowed | Grundtarif | ANP=1,230; SAP=36; KFB=ZKF x 9,600; KZTAB=1 |
| II | Single parent (Alleinerziehend) | Grundtarif + EFA | ANP=1,230; SAP=36; KFB=ZKF x 9,600; EFA=4,260; KZTAB=1 |
| III | Married, sole earner or higher earner (spouse in V) | Splittingtarif | ANP=1,230; SAP=36; KFB=ZKF x 9,600; KZTAB=2 |
| IV | Married, both earning similar amounts | Grundtarif | ANP=1,230; SAP=36; KFB=ZKF x 4,800; KZTAB=1 |
| V | Married, lower earner (spouse in III) | Special min-tax method | ANP=1,230; SAP=36; KFB=0; special MST5_6 |
| VI | Second or additional employment | No allowances | No ANP, no FVBZ, no KFB |

- **Key abbreviations** — ANP = Arbeitnehmer-Pauschbetrag (employee lump sum EUR 1,230); SAP = Sonderausgaben-Pauschbetrag (EUR 36); KFB = Kinderfreibetrag per child (EUR 9,600 full / EUR 4,800 half); EFA = Entlastungsbetrag fuer Alleinerziehende (EUR 4,260); KZTAB = tariff multiplier (1 = Grundtarif, 2 = Splittingverfahren); ZKF = number of child allowances.  _(Section 1 -- Quick Reference)_

### Social Security Rates (2025)

**Social Security Rates table**

| Branch | German Name | Total Rate | Employee (AN) | Employer (AG) |
| --- | --- | --- | --- | --- |
| Pension | Rentenversicherung (RV) | 18.6% | 9.3% | 9.3% |
| Health | Krankenversicherung (KV) | 14.6% + Zusatzbeitrag | 7.3% + ZB/2 | 7.3% + ZB/2 |
| Care | Pflegeversicherung (PV) | 3.6% base | see table below | see table below |
| Unemployment | Arbeitslosenversicherung (AV) | 2.6% | 1.3% | 1.3% |

- **Average Zusatzbeitrag (ZB) for 2025** — 2.5% (varies by Krankenkasse; Total KV with average ZB = 17.1%)  _(Social Security Rates (2025))_

### Pflegeversicherung Detail (2025)

**Pflegeversicherung Detail table**

| Situation | Employee (AN) | Employer (AG) | Total |
| --- | --- | --- | --- |
| Childless, age 23+ (PVZ=1) | 2.4% | 1.8% | 4.2% |
| 1 child (PVZ=0, PVA=0) | 1.8% | 1.8% | 3.6% |
| 2 children (PVZ=0, PVA=1) | 1.55% | 1.8% | 3.35% |
| 3 children (PVZ=0, PVA=2) | 1.3% | 1.8% | 3.1% |
| 4 children (PVZ=0, PVA=3) | 1.05% | 1.8% | 2.85% |
| 5+ children (PVZ=0, PVA=4) | 0.8% | 1.8% | 2.6% |
| **Sachsen exception** (PVS=1) | +0.5% AN | -0.5% AG | same total |

- **Sachsen PV adjustment** — In Sachsen, the employee pays 0.5% more and the employer pays 0.5% less (Buss- und Bettag adjustment). For childless in Sachsen: AN = 2.9%, AG = 1.3%.  _(Pflegeversicherung Detail (2025))_

### Beitragsbemessungsgrenzen (Contribution Ceilings, 2025)

**Beitragsbemessungsgrenzen table**

| Ceiling | Monthly | Annual | Applies to |
| --- | --- | --- | --- |
| KV/PV-BBG | EUR 5,512.50 | EUR 66,150 | Health + Care insurance |
| RV-BBG (West) | EUR 8,050.00 | EUR 96,600 | Pension insurance |
| RV-BBG (East) | EUR 8,050.00 | EUR 96,600 | Pension insurance (unified since 2025) |
| AV-BBG | EUR 8,050.00 | EUR 96,600 | Unemployment insurance |
| JAEG (Versicherungspflichtgrenze) | EUR 6,150.00 | EUR 73,800 | Threshold above which employees may opt for PKV |

- **Ceiling application rule** — Income above the BBG is not subject to contributions for that branch.  _(Beitragsbemessungsgrenzen (Contribution Ceilings, 2025))_

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown Steuerklasse | Steuerklasse I |
| Unknown church membership | No Kirchensteuer (R=0) |
| Unknown Zusatzbeitrag | Use average 2.5% |
| Unknown number of children | Childless surcharge (PVZ=1) |
| Unknown KRV status | KRV=0 (statutory pension insured) |
| Unknown Sachsen status | PVS=0 (non-Sachsen) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — gross monthly salary (Bruttolohn), Steuerklasse, and pay period (monthly/weekly)  _(Required Inputs)_
- **Recommended** — Zusatzbeitrag of specific Krankenkasse, number and ages of children, church membership, Freibetrag from ELStAM, KRV status, Sachsen residence  _(Required Inputs)_
- **Ideal** — full ELStAM data (electronic wage tax deduction characteristics), employment contract, prior Lohnsteuerbescheinigung  _(Required Inputs)_

### Refusal Catalogue

- **R-DE-P-1 -- Self-employed / Freiberufler** — This skill covers employee payroll (Lohnsteuer). Self-employed persons compute Einkommensteuer, not Lohnsteuer. Use de-income-tax.md.  _(R-DE-P-1)_
- **R-DE-P-2 -- Mini-job (geringfugige Beschaftigung)** — Mini-jobs up to EUR 556/month have flat-rate taxation (2% pauschale Lohnsteuer or individual). Separate rules apply.  _(R-DE-P-2)_
- **R-DE-P-3 -- Cross-border workers (Grenzganger)** — Cross-border employment requires DBA analysis and potentially foreign social security. Escalate to Steuerberater.  _(R-DE-P-3)_
- **R-DE-P-4 -- Board members / Geschaftsfuhrer of GmbH** — Managing directors have special social security rules. Escalate.  _(R-DE-P-4)_
- **R-DE-P-5 -- Short-term employment (kurzfristige Beschaftigung)** — Limited to 70 working days or 3 months per year. Special rules apply.  _(R-DE-P-5)_

## Section 3 -- BMF PAP Tax Formula (UPTAB25)

The following is the exact Einkommensteuer tariff formula from the BMF Programmablaufplan for 2025 (September 2025 revision), as implemented in [MarcelLehmann/Lohnsteuer](https://github.com/MarcelLehmann/Lohnsteuer) `Lohnsteuer2025.java`.

All values are annual. For monthly/weekly/daily payroll, the PAP annualises the pay period amount, computes annual tax, then divides back.

### Formula (§32a EStG, 2025 PAP constants)

- **UPTAB25 tariff formula** — Input: X = zu versteuerndes Einkommen (taxable income) in EUR, whole euros GFB = 12,096 Zone 0 -- Grundfreibetrag: If X < GFB + 1 (i.e., X <= 12,096): ST = 0 Zone 1 -- Progressive zone 1 (14% entry rate): If 12,097 <= X < 17,444: Y = (X - 12,096) / 10,000 RW = Y * 932.30 + 1,400 ST = floor(RW * Y) Zone 2 -- Progressive zone 2: If 17,444 <= X < 68,481: Y = (X - 17,443) / 10,000 RW = Y * 176.64 + 2,397 ST = floor(RW * Y + 1,015.13) Zone 3 -- Proportionalzone (42%): If 68,481 <= X < 277,826: ST = floor(X * 0.42 - 10,911.92) Zone 4 -- Reichensteuer (45%): If X >= 277,826: ST = floor(X * 0.45 - 19,246.67) Final: ST = ST * KZTAB (KZTAB = 2 for Steuerklasse III Splitting; KZTAB = 1 for all others)  _(§32a EStG, 2025 PAP constants; MarcelLehmann/Lohnsteuer Lohnsteuer2025.java)_

### Steuerklasse V/VI Special Method (MST5_6)

- **MST5_6 formula** — UP5_6(ZX): ST1 = UPTAB25(ZX * 1.25) ST2 = UPTAB25(ZX * 0.75) DIFF = (ST1 - ST2) * 2 MIST = floor(ZX * 0.14)    -- minimum tax ST = max(DIFF, MIST)  _(§39b Abs. 2 Satz 7 EStG)_

Steuerklassen V and VI use a different computation per §39b Abs. 2 Satz 7 EStG. Instead of the standard UPTAB25, the PAP computes tax on 1.25x and 0.75x the income, takes the difference, doubles it, and applies a 14% minimum:

The thresholds W1STKL5, W2STKL5, W3STKL5 create additional breakpoints:

**Threshold table**

| Threshold | 2025 Value | Rate above |
| --- | --- | --- |
| W1STKL5 | EUR 13,785 | 42% marginal via comparison check |
| W2STKL5 | EUR 34,240 | 42% flat marginal |
| W3STKL5 | EUR 222,260 | 45% flat marginal |

### Solidaritatszuschlag Formula (MSOLZ)

- **SolZ formula** — SOLZFREI = 19,950 * KZTAB (EUR 19,950 for Grundtarif; EUR 39,900 for Splitting) If JBMG > SOLZFREI: SOLZJ = floor(JBMG * 5.5 / 100, 2 decimals) SOLZMIN = floor((JBMG - SOLZFREI) * 11.9 / 100, 2 decimals) SolZ = min(SOLZJ, SOLZMIN) Else: SolZ = 0 JBMG = Jahresbemessungsgrundlage (annual Lohnsteuer for SolZ assessment, computed from Jahreslohnsteuer after §51a EStG adjustments)  _(MSOLZ, §51a EStG)_
- **Phase-in rate purpose** — The 11.9% phase-in rate ensures the SolZ increases gradually above the Freigrenze rather than jumping to 5.5%.  _(MSOLZ)_

### Vorsorgepauschale (Insurance Deduction in Tax Computation)

The PAP deducts a Vorsorgepauschale from gross income before computing Lohnsteuer. This is an approximation of the employee's social insurance contributions:

- **Vorsorgepauschale (MPARA) formula** — MPARA constants (2025): BBGRV = 96,600 (annual pension ceiling) RVSATZAN = 0.093 (employee pension rate) BBGKVPV = 66,150 (annual health/care ceiling) KVSATZAN = 0.07 + KVZ/200 (employee health rate: 7.0% base + half Zusatzbeitrag) KVSATZAG = 0.07 + 0.0125 (employer health rate for Vorsorgepauschale: 8.25%) PVSATZAN = 0.018 (employee care rate, non-Sachsen; 0.023 Sachsen) PVSATZAG = 0.018 (employer care rate, non-Sachsen; 0.013 Sachsen) VSP1 = min(annual_gross, BBGRV) * RVSATZAN VSP2 = min(annual_gross * 0.12, VHB) VHB = 3,000 (Stkl III) or 1,900 (others) VSP3 = min(annual_gross, BBGKVPV) * (KVSATZAN + PVSATZAN) VSP = max(VSP1 + VSP2, VSP1 + VSP3)  _(MPARA constants (2025))_

## Section 4 -- Social Security Computation (Employer Payroll)

### 4.1 Monthly Payroll Social Security Deductions

- **Assessment base rule** — For each employee, the employer computes contributions on `assessment_base = min(gross_monthly, BBG)`:  _(4.1 Monthly Payroll Social Security Deductions)_

**Monthly Payroll Social Security Deductions table**

| Branch | Rate (AN) | Rate (AG) | BBG monthly | Max AN/month | Max AG/month |
| --- | --- | --- | --- | --- | --- |
| RV (Pension) | 9.30% | 9.30% | EUR 8,050.00 | EUR 748.65 | EUR 748.65 |
| KV (Health) | 7.30%+ZB/2 | 7.30%+ZB/2 | EUR 5,512.50 | varies | varies |
| PV (Care) | varies | 1.80% | EUR 5,512.50 | varies | EUR 99.23 |
| AV (Unemploymt) | 1.30% | 1.30% | EUR 8,050.00 | EUR 104.65 | EUR 104.65 |

- **KV with average ZB detail** — With average ZB = 2.5%: - KV employee: 7.3% + 1.25% = 8.55% of min(gross, 5,512.50) → max EUR 471.32/month - KV employer: 7.3% + 1.25% = 8.55% of min(gross, 5,512.50) → max EUR 471.32/month  _(4.1 Monthly Payroll Social Security Deductions)_

### 4.2 Total Maximum Monthly Deductions (at or above all ceilings)

**Total Maximum Monthly Deductions table**

| Branch | Employee Max | Employer Max | Total Max |
| --- | --- | --- | --- |
| RV | EUR 748.65 | EUR 748.65 | EUR 1,497.30 |
| KV (avg ZB 2.5%) | EUR 471.32 | EUR 471.32 | EUR 942.64 |
| PV (childless) | EUR 132.30 | EUR 99.23 | EUR 231.53 |
| PV (1 child) | EUR 99.23 | EUR 99.23 | EUR 198.45 |
| AV | EUR 104.65 | EUR 104.65 | EUR 209.30 |
| **Total (childless)** | **EUR 1,456.92** | **EUR 1,423.85** | **EUR 2,880.77** |
| **Total (1 child)** | **EUR 1,423.85** | **EUR 1,423.85** | **EUR 2,847.69** |

### 4.3 Employer-Only Contributions (not deducted from employee)

**Employer-Only Contributions table**

| Contribution | Rate | Base |
| --- | --- | --- |
| Umlage U1 (sick pay, <30 employees) | 0.9%--4.1% (varies by Krankenkasse) | Gross up to KV-BBG |
| Umlage U2 (maternity) | 0.19%--0.8% (varies) | Gross up to KV-BBG |
| Insolvenzgeldumlage | 0.06% | Gross up to RV-BBG |
| Berufsgenossenschaft (accident) | varies by industry (0.5%--10%+) | Gross (industry-specific ceiling) |

## Section 5 -- Worked Examples

### Example 1 -- Steuerklasse I, EUR 4,000/month, no church, childless

**Input:** Brutto EUR 4,000/month, Stkl I, R=0, PVZ=1, KVZ=2.50%, KRV=0, PVS=0

**Lohnsteuer computation (annualised):**
- Annual gross = EUR 48,000
- Less ANP (1,230) + SAP (36) + Vorsorgepauschale
- VSP1 = 48,000 x 0.093 = 4,464
- VSP3 = 48,000 x (0.07 + 0.0125 + 0.018 + 0.006) = 48,000 x 0.1065 = 5,112
- VSP = max(4,464 + 1,900, 4,464 + 5,112) = max(6,364, 9,576) = 9,576
- ZVE = 48,000 - 1,230 - 36 - 9,576 = 37,158
- UPTAB25(37,158): Zone 2: Y = (37,158 - 17,443)/10,000 = 1.9715; RW = 1.9715 x 176.64 + 2,397 = 2,745.25; ST = floor(2,745.25 x 1.9715 + 1,015.13) = floor(6,425.96) = 6,425
- Monthly LSt = floor(6,425 x 100 / 12) / 100 = EUR 535.41/month (approximate)

**SolZ:** JBMG = 6,425 < SOLZFREI 19,950 → SolZ = EUR 0

**Social security:**
- RV: 4,000 x 9.3% = EUR 372.00
- KV: 4,000 x 8.55% = EUR 342.00
- PV: 4,000 x 2.4% = EUR 96.00
- AV: 4,000 x 1.3% = EUR 52.00
- Total SV (AN): EUR 862.00

**Approximate net:** 4,000 - 535 - 0 - 0 - 862 = **EUR 2,603/month**

### Example 2 -- Steuerklasse III, EUR 6,000/month, church (Bavaria), 2 children

**Input:** Brutto EUR 6,000/month, Stkl III, R=1 (church, 8% Bayern), ZKF=2.0, PVZ=0, PVA=1, KVZ=2.50%

**Lohnsteuer (annualised):**
- Annual gross = EUR 72,000
- KZTAB = 2 (Splitting)
- KFB = 2.0 x 9,600 = 19,200
- ZVE after deductions and Vorsorgepauschale: computed per PAP
- X = ZVE / 2 (Splitting)
- Apply UPTAB25 to X, then ST = ST x 2
- Result: significantly lower than Stkl I due to Splitting

**Social security (2 children):**
- RV: 6,000 x 9.3% = EUR 558.00 (under RV-BBG)
- KV: 5,512.50 x 8.55% = EUR 471.32 (capped at KV-BBG)
- PV: 5,512.50 x 1.55% = EUR 85.44 (2 children, PVA=1)
- AV: 6,000 x 1.3% = EUR 78.00
- Total SV (AN): EUR 1,192.76

### Example 3 -- Steuerklasse VI (second job), EUR 1,500/month

**Input:** Brutto EUR 1,500/month, Stkl VI, R=0

**Lohnsteuer:** No ANP, no SAP, no KFB, no FVBZ. Higher effective rate since no allowances are applied. MST5_6 method may apply depending on income level.

**Social security:** Normal rates apply. If already at BBG from primary employment, no additional contributions.

## Section 6 -- Payslip Transaction Pattern Library

### 6.1 Payslip Credits (Employee receives)

**Payslip Credits table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| GEHALT, LOHN, ENTGELT | Net salary payment | After all deductions |
| NACHZAHLUNG GEHALT | Salary back-payment | May trigger sonstige Bezuege rules |
| WEIHNACHTSGELD, 13. GEHALT | Christmas bonus | Taxed as sonstiger Bezug |
| URLAUBSGELD | Holiday bonus | Taxed as sonstiger Bezug |
| ABFINDUNG | Severance payment | Fuenftelregelung may apply (§34 EStG) |
| TANTIEME, BONUS, PRAEMIE | Performance bonus | Sonstiger Bezug |
| JUBILAEUM | Anniversary bonus | Sonstiger Bezug |

### 6.2 Employer Deductions (visible on payslip, debited from gross)

**Employer Deductions table**

| Line Item | What It Is | Employee Portion |
| --- | --- | --- |
| LSt / Lohnsteuer | Income tax withholding | 100% employee |
| SolZ / Solidaritatszuschlag | Solidarity surcharge | 100% employee |
| KiSt / Kirchensteuer | Church tax | 100% employee |
| RV-Beitrag AN | Pension contribution | 9.3% of gross (up to BBG) |
| KV-Beitrag AN | Health contribution | 7.3% + ZB/2 of gross (up to BBG) |
| PV-Beitrag AN | Care contribution | see PV table above |
| AV-Beitrag AN | Unemployment contribution | 1.3% of gross (up to BBG) |

## Section 7 -- Key PAP Input Parameters Reference

These are the input parameters to the BMF Programmablaufplan, as defined in the [MarcelLehmann/Lohnsteuer](https://github.com/MarcelLehmann/Lohnsteuer) `Lohnsteuer2025.java` (generated from official BMF PAP XML, Stand: 2025-09-17):

**Key PAP Input Parameters table**  _(MarcelLehmann/Lohnsteuer Lohnsteuer2025.java, Stand: 2025-09-17)_

| Parameter | Type | Description |
| --- | --- | --- |
| RE4 | BigDecimal | Steuerpflichtiger Arbeitslohn for the pay period, in Cent |
| STKL | int | Steuerklasse (1--6) |
| LZZ | int | Pay period: 1=Jahr, 2=Monat, 3=Woche, 4=Tag |
| R | int | Religion (0=none, church membership code otherwise) |
| KRV | int | 0=statutory pension insured, 1=not |
| KVZ | BigDecimal | Zusatzbeitrag in percent (e.g. 2.50) |
| PVS | int | 1=Sachsen (Pflegeversicherung exception) |
| PVZ | int | 1=childless surcharge applies |
| PVA | BigDecimal | Number of Beitragsabschlage (0--4, for children 2--5+) |
| PKV | int | 0=GKV, 1=PKV without employer subsidy, 2=PKV with subsidy |
| PKPV | BigDecimal | Monthly PKV premium in Cent (if PKV) |
| ZKF | BigDecimal | Number of Kinderfreibetrage (one decimal) |
| af | int | 1=Faktorverfahren selected (Stkl IV only) |
| f | double | Factor value (default 1.0) |
| ALTER1 | int | 1=age 64+ at start of calendar year |
| JFREIB | BigDecimal | Annual Freibetrag from ELStAM, in Cent |
| JHINZU | BigDecimal | Annual Hinzurechnungsbetrag from ELStAM, in Cent |

### Key Output Parameters

**Key Output Parameters table**

| Parameter | Description |
| --- | --- |
| LSTLZZ | Lohnsteuer for the pay period, in Cent |
| SOLZLZZ | Solidaritatszuschlag for the pay period, in Cent |
| BK | Bemessungsgrundlage for Kirchensteuer, in Cent |
| STS | Lohnsteuer on sonstige Bezuege, in Cent |
| SOLZS | SolZ on sonstige Bezuege, in Cent |
| BKS | Kirchensteuer Bemessungsgrundlage on sonstige Bezuege, in Cent |
| VKVLZZ | Arbeitgeberzuschuss zur PKV (for employer subsidy computation), in Cent |

## Section 8 -- Sonstige Bezuege (Bonuses, One-Time Payments)

Sonstige Bezuege (bonuses, severance, holiday pay) are taxed separately per §39b Abs. 3 EStG. The PAP:

1. Computes annual Lohnsteuer on regular pay alone (Jahresarbeitslohn)
2. Computes annual Lohnsteuer on regular pay + sonstiger Bezug
3. The difference is the tax on the sonstiger Bezug

This prevents the progressive rate from being distorted by one-time payments.

For Entschadigungen/Abfindungen, the Funftelregelung (§34 EStG) may apply:
- Compute tax on 1/5 of the Abfindung added to regular income
- Multiply the incremental tax by 5
- This smooths the progressive effect

## Section 9 -- Mini-Jobs and Gleitzone (Midijobs)

### Mini-Jobs (Geringfugige Beschaftigung)

**Mini-Jobs table**

| Parameter | Value |
| --- | --- |
| Monthly ceiling | EUR 556 (2025) |
| Employer flat-rate contributions | RV 15%, KV 13%, Pauschalsteuer 2%, U1+U2+Insolvenzumlage |
| Employee contributions | None (unless RV opt-in: employee pays 3.6% RV top-up) |
| No Lohnsteuer | Covered by 2% Pauschalsteuer |

### Midijobs / Uebergangsbereich (Gleitzone)

**Midijobs table**

| Parameter | Value |
| --- | --- |
| Range | EUR 556.01 -- EUR 2,000.00/month |
| Employee contributions | Reduced via gliding scale formula |
| Employer contributions | Full standard rates |
| Lohnsteuer | Normal withholding per Steuerklasse |

## Section 10 -- Test Suite

**Test 1 -- Stkl I, 4,000 brutto, childless, no church.**
Input: STKL=1, RE4=400000 (cents), LZZ=2, R=0, KVZ=2.50, PVZ=1, KRV=0, PKV=0.
Expected: LSTLZZ approximately EUR 535 (monthly Lohnsteuer in cents). SOLZLZZ = 0 (below Freigrenze). BK = 0.
SV deductions: RV=372, KV=342, PV=96, AV=52 = EUR 862/month.

**Test 2 -- Stkl III, 6,000 brutto, 2 children, church 8% (Bayern).**
Input: STKL=3, RE4=600000, LZZ=2, R=1, ZKF=2.0, PVZ=0, PVA=1, KVZ=2.50.
Expected: Significantly lower LSt due to Splitting. KiSt = BK x 8%.
SV: RV=558, KV=471.32, PV=85.44, AV=78 = EUR 1,192.76/month.

**Test 3 -- Stkl V, 2,500 brutto, childless.**
Input: STKL=5, RE4=250000, LZZ=2, PVZ=1, KVZ=2.50.
Expected: Higher LSt than Stkl I due to MST5_6 method with 14% minimum.

**Test 4 -- Above all BBGs, Stkl I, 10,000 brutto.**
Input: STKL=1, RE4=1000000, LZZ=2, PVZ=1.
Expected: RV capped at 748.65, KV capped at 471.32, PV capped at 132.30, AV capped at 104.65.

**Test 5 -- SolZ phase-in.**
Input: Annual LSt = EUR 20,500, single.
Expected: SOLZFREI = 19,950. SOLZJ = 20,500 x 5.5% = 1,127.50. SOLZMIN = (20,500 - 19,950) x 11.9% = 65.45. SolZ = min(1,127.50, 65.45) = EUR 65.45.

**Test 6 -- Validate against BMF online calculator.**
All computations should match [bmf-steuerrechner.de](https://www.bmf-steuerrechner.de) using the same inputs. The MarcelLehmann/Lohnsteuer test suite validates against this API.

## Section 11 -- Interaction with Other German Skills

**Interaction table**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (Lohnsteuer) | **This skill (de-payroll.md)** |
| Self-employed income tax (Einkommensteuer) | de-income-tax.md |
| Self-employed social contributions | de-social-contributions.md |
| Gewerbesteuer (trade tax) | de-trade-tax.md |
| Umsatzsteuer / VAT return | germany-vat-return.md |
| Quarterly estimated tax payments | de-estimated-tax.md |
| ZUGFeRD/XRechnung e-invoicing | [horstoeko/zugferd](https://github.com/horstoeko/zugferd) (MIT, PHP) -- uses VAT category codes S/Z/E/AE/K/G/O with rates 19%/7% standard |

## PROHIBITIONS

- NEVER compute Lohnsteuer using simple bracket percentages -- use the PAP formula (UPTAB25)
- NEVER apply Grundtarif (UPTAB25) directly to Steuerklasse V or VI -- use the MST5_6 method
- NEVER forget the Vorsorgepauschale deduction before computing Lohnsteuer
- NEVER confuse the KV/PV-BBG (EUR 5,512.50/month) with the RV/AV-BBG (EUR 8,050/month)
- NEVER apply the childless PV surcharge to employees with children
- NEVER charge social security contributions above the Beitragsbemessungsgrenze
- NEVER omit the Sachsen PV exception when the employee is in Sachsen
- NEVER treat sonstige Bezuege (bonuses) as regular pay -- use the PAP's separate method
- NEVER assume Kirchensteuer is 9% everywhere -- Bavaria and Baden-Wurttemberg use 8%
- NEVER present payroll computations as definitive -- direct to Steuerberater/Lohnbuchhalter for sign-off

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or Lohnbuchhalter in Germany) before implementation.

The PAP formula and constants are sourced from the [MarcelLehmann/Lohnsteuer](https://github.com/MarcelLehmann/Lohnsteuer) repository (Apache-2.0), which generates code from the official BMF Programmablaufplan XML. The BMF publishes the PAP at [bmf-steuerrechner.de](https://www.bmf-steuerrechner.de).

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
