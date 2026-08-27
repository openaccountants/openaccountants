---
name: id-payroll-pph21
description: Use this skill whenever asked to calculate, review, or advise on Indonesian payroll — PPh 21 (income tax withholding), BPJS Kesehatan (health insurance), BPJS Ketenagakerjaan (JHT, JP, JKK, JKM employment social security), biaya jabatan, or PTKP thresholds. Trigger on phrases like "PPh 21", "PPh Pasal 21", "pajak penghasilan", "BPJS", "gaji Indonesia", "payroll Indonesia", "potong pajak karyawan", "TER PPh 21", "PTKP", or any Indonesia employment income tax / social security request. ALWAYS read this skill before touching any Indonesia payroll or PPh 21 work.
version: 1.0
jurisdiction: ID
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: RILIA PUTRI
review_status: current
depends_on:
  - foundation
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ID Payroll Pph21

## Indonesia Payroll — PPh 21 & BPJS Contributions Skill v1.1

> **2025 changes summary (v1.1 refresh):** PPh 21 monthly withholding continues under the TER system (PP 58/2023, PMK 168/2023 — Categories A/B/C by PTKP, year-end reconciliation under Article 17 brackets). From **1 July 2024**, Indonesian-citizen employees use their **16-digit NIK as NPWP**; foreign-national employees keep the 15-digit NPWP. From **1 January 2025**, all PPh 21 filings — monthly **SPT Masa PPh 21 / e-Bupot Unifikasi** and the **1721-A1 / 1721-A2** annual slips — flow through **Coretax DJP** (the legacy DJP Online e-Bupot 21/26 desktop app is being retired). See `id-einvoice-coretax` for the Coretax workflow.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **RILIA PUTRI** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Payroll PPh 21 and BPJS

- **0 – IDR 60,000,000 bracket** — 5% — max IDR 3,000,000  _(UU HPP Art. 17(1)(a))_
- **60m – 250m bracket** — 15% — max IDR 28,500,000  _(UU HPP Art. 17(1)(a))_
- **250m – 500m bracket** — 25% — max IDR 62,500,000  _(UU HPP Art. 17(1)(a))_
- **500m – 5bn bracket** — 30% — max IDR 1,350,000,000  _(UU HPP Art. 17(1)(a))_
- **Above 5,000,000,000** — 35%  _(UU HPP Art. 17(1)(a))_
- **No-NPWP surcharge** — 20% additional on calculated PPh 21  _(UU PPh Art. 21(5a); PMK 168/2023)_
- **Biaya Jabatan rate** — 5% of gross employment income  _(UU PPh Art. 21)_
- **Biaya Jabatan monthly cap** — Maximum IDR 500,000/month  _(PMK-168/2023)_
- **Biaya Jabatan annual cap** — Maximum IDR 6,000,000/year  _(PMK-168/2023)_
- **Biaya Jabatan applies to** — Permanent employees (Pegawai Tetap)  _(PMK 168/2023 Art. 3 & Art. 10)_
- **BPJS Kesehatan employer rate** — 4% of gross monthly salary  _(Perpres 64/2020)_
- **BPJS Kesehatan employee rate** — 1% of gross monthly salary  _(Perpres 64/2020)_
- **BPJS Kesehatan total** — 5%  _(Perpres 64/2020)_
- **BPJS Kesehatan max wage basis** — IDR 12,000,000/month  _(Perpres 64/2020)_
- **BPJS Kesehatan extra dependants (>5 family)** — Additional 1% per extra dependent  _(Perpres 64/2020)_
- **JHT employer rate** — 3.7% of wage  _(PP 46/2015)_
- **JHT employee rate** — 2.0% of wage  _(PP 46/2015)_
- **JHT total** — 5.7% total contribution  _(PP 46/2015)_
- **JP employer rate** — 2.00%  _(PP 45/2015)_
- **JP employee rate** — 1.00%  _(PP 45/2015)_
- **JP total** — 3.00%  _(PP 45/2015)_
- **JP wage cap (Mar 2025)** — IDR 10,547,400/month  _(BPJS TK 2025 regulation)_
- **JKK Grade 1 (very low risk)** — 0.10% of monthly wage  _(PP 44/2015 jo. PP 49/2023 Art. 16A(1)(a))_
- **JKK Grade 2 (low risk)** — 0.40% of monthly wage  _(PP 44/2015 jo. PP 49/2023 Art. 16A(1)(b))_
- **JKK Grade 3 (medium risk)** — 0.75% of monthly wage  _(PP 44/2015 jo. PP 49/2023 Art. 16A(1)(b))_
- **JKK Grade 4 (high risk)** — 1.13% of monthly wage  _(PP 44/2015 jo. PP 49/2023 Art. 16A(1)(d))_
- **JKK Grade 5 (very high risk)** — 1.60% of monthly wage  _(PP 44/2015 jo. PP 49/2023 Art. 16A(1)€)_
- **JKM employer rate** — 0.20% of monthly wage  _(PP 44/2015 jo. PP 49/2023 Art. 18A)_
- **JKP rate** — 0.46% — funded by govt + JKK/JKM surplus reallocation  _(PP 37/2021; PP 49/2023)_
- **JKP impact on payroll** — No additional employer/employee deduction  _(PP 37/2021; PP 49/2023)_
- **TER effective from** — 1 January 2024  _(PP 58/2023; PMK 168/2023)_
- **TER Category A** — Category A generally applies to taxpayers with PTKP status TK/0, TK/1, K/0 under prevailing TER provisions.  _(PP 58/202, PMK 168/PMK.010/2023. Full TER monthly rate tables for all categories provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'TER Monthly')_
- **TER Category B** — Category B generally applies to PTKP status TK/2, TK/3, K/1, K/2.  _(PP 58/2023; PMK 168/PMK.010/2023. Full TER monthly rate tables for all categories provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'TER Monthly')_
- **TER Category C** — Category C generally applies to PTKP status K/3.  _(PP 58/2023 ; PMK 168/PMK.010/2023. Full TER monthly rate tables for all categories provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'TER Monthly')_
- **Cat A: 0% threshold** — IDR 0 – 5,400,000/month  _(PP 58/2023 ; PMK 168/PMK.010/2023.)_
- **Cat B: 0% threshold** — IDR 0 – 6,200,000/month  _(PP 58/2023 ; PMK 168/PMK.010/2023.)_
- **Cat C: 0% threshold** — IDR 0 – 6,600,000/month  _(PP 58/2023 ; PMK 168/PMK.010/2023.)_
- **Cat A: top rate** — 34% (over IDR 1,400,000,000/month)  _(PP 58/2023 Annex; PMK 168/PMK.010/2023. See full bracket table in attachment TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'TER Monthly'.)_
- **December reconciliation** — December PPh 21 calculation generally reconciles annual tax under Article 17 rates against cumulative Jan–Nov withholding using TER methodology.  _(PP 58/2023; PMK 168/PMK.010/2023.)_
- **Monthly e-Bupot PPh 21/26** — Generally due by the 20th of the following month through the applicable DJP electronic tax administration system (Coretax/e-Bupot)  _(UU KUP Art. 3(3); PMK 81/2024 as amended by PMK 1/2026 |; note: UU KUP as amended by UU HPP No. 7/2021.)_
- **Annual SPT filing** — 31 March (individual)  _(UU KUP Art. 3(3)(b))_
- **1721-A1 certificate** — Issued annually or on termination  _(PMK 168/2023 Art. 23)_

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Indonesia (Republik Indonesia) |
| Tax | PPh 21 — Pajak Penghasilan Pasal 21 (Employment Income Tax Withholding) |
| Currency | IDR (Indonesian Rupiah / Rp) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Current tax year | 2025 |
| Tax authority | Direktorat Jenderal Pajak (DJP) — Directorate General of Taxes |
| Return forms | SPT Tahunan PPh Orang Pribadi (1770/1770S/1770SS) |
| Monthly withholding | E-Bupot PPh 21/26 via DJP Online |
| Filing deadline | 31 March (annual); 20th of following month (monthly E-Bupot) |
| Governing law | UU PPh No. 36/2008, as amended by UU HPP No. 7/2021; PP 58/2023; PMK 168/2023 |
| Source credit | `steevenz/id-payroll-calculator` (MIT) + `KejawenLab/PPH21` (MIT) + DJP / official regulations |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a qualified Indonesian tax consultant |
| Skill version | 1.0 |

## Section 2 — PPh 21 progressive tax brackets (Tarif Pasal 17 UU HPP)

Tax is computed on **Penghasilan Kena Pajak (PKP)** — taxable income after deductions and PTKP.

These brackets are from UU HPP No. 7/2021, effective from 1 January 2022 onward. They are permanent and unchanged through 2025/2026.

**PPh 21 progressive tax brackets**

| Annual PKP (IDR) | Rate | Max tax in bracket |
| --- | --- | --- |
| 0 – 60,000,000 | 5% | 3,000,000 |
| 60,000,001 – 250,000,000 | 15% | 28,500,000 |
| 250,000,001 – 500,000,000 | 25% | 62,500,000 |
| 500,000,001 – 5,000,000,000 | 30% | 1,350,000,000 |
| Over 5,000,000,000 | 35% | — |

> **Note:** The `steevenz/id-payroll-calculator` and `KejawenLab/PPH21` repos use the older pre-HPP brackets (first bracket 0–50M, no 35% bracket). The brackets above reflect the current law.

- **No-NPWP surcharge** — Employees without an NPWP (tax ID number) are subject to an additional 20% surcharge on the calculated PPh 21 liability  _(per `steevenz/id-payroll-calculator` `Pph21.php`)_

## Section 3 — PTKP (Penghasilan Tidak Kena Pajak / Non-Taxable Income)

PTKP is deducted from annual net income before applying the progressive brackets. Amounts are per PMK 101/PMK.010/2016, unchanged through 2025.

**PTKP status table**

| Status code | Description | Annual PTKP (IDR) |
| --- | --- | --- |
| TK/0 | Single, no dependents | 54,000,000 |
| TK/1 | Single, 1 dependent | 58,500,000 |
| TK/2 | Single, 2 dependents | 63,000,000 |
| TK/3 | Single, 3 dependents | 67,500,000 |
| K/0 | Married, no dependents | 58,500,000 |
| K/1 | Married, 1 dependent | 63,000,000 |
| K/2 | Married, 2 dependents | 67,500,000 |
| K/3 | Married, 3 dependents | 72,000,000 |

- **Additional rules** — Maximum 3 dependents (tanggungan) are recognized; If wife's income is combined (penghasilan digabung), add an additional IDR 54,000,000

Source: `steevenz/id-payroll-calculator` → `State.php` → `$listOfPTKP` array.

## Section 4 — Biaya Jabatan (Position Deduction)

**Biaya Jabatan parameters**

| Parameter | Value |
| --- | --- |
| Rate | 5% of annual gross income |
| Monthly maximum | IDR 500,000 |
| Annual maximum | IDR 6,000,000 |
| Applies to | Permanent employees (pegawai tetap) only |

- **Exemption for minimum wage earners** — Employees earning at or below the province minimum wage are exempt from biaya jabatan (per `steevenz/id-payroll-calculator` logic).

Source: UU DJP No. PER-32/PJ/2015 Pasal 21 ayat 3; `PayrollCalculator.php`.

## Section 5 — BPJS Kesehatan (Health Insurance)

**BPJS Kesehatan contribution table**

| Component | Rate | Paid by |
| --- | --- | --- |
| Employer contribution | 4% of gross monthly salary | Employer |
| Employee contribution | 1% of gross monthly salary | Employee (payroll deduction) |
| **Total** | **5%** |  |

**BPJS Kesehatan parameters**

| Parameter | Value |
| --- | --- |
| Maximum wage basis | IDR 12,000,000/month |
| Additional dependents | If employee has > 5 family dependents, additional 1% deduction per extra dependent |

Source: `steevenz/id-payroll-calculator` → `PayrollCalculator.php` (employer 4%, employee 1%).

## Section 6 — BPJS Ketenagakerjaan (Employment Social Security)

### 6a — JHT (Jaminan Hari Tua / Old-Age Savings)

**JHT contribution table**

| Component | Rate | Paid by |
| --- | --- | --- |
| Employer contribution | 3.70% of gross monthly salary | Employer |
| Employee contribution | 2.00% of gross monthly salary | Employee (payroll deduction) |
| **Total** | **5.70%** |  |

Source: `steevenz/id-payroll-calculator` → `PayrollCalculator.php`.

### 6b — JP (Jaminan Pensiun / Pension Insurance)

**JP contribution table**

| Component | Rate | Paid by |
| --- | --- | --- |
| Employer contribution | 2.00% of gross monthly salary | Employer |
| Employee contribution | 1.00% of gross monthly salary | Employee (payroll deduction) |
| **Total** | **3.00%** |  |

**JP parameters**

| Parameter | Value |
| --- | --- |
| Maximum wage basis | IDR 10,547,400/month (effective 1 March 2025) |

- **JP contribution cap example** — When salary exceeds the wage ceiling, contributions are calculated on the ceiling amount, not actual salary. Example: for salary IDR 15,000,000, employer JP = 2% × 10,547,400 = IDR 210,948; employee JP = 1% × 10,547,400 = IDR 105,474.

Source: `steevenz/id-payroll-calculator` → `PayrollCalculator.php` (cap logic at `7000000` in repo, now updated to IDR 10,547,400 per BPJS Ketenagakerjaan 2025 regulation).

### 6c — JKK (Jaminan Kecelakaan Kerja / Work Accident Insurance)

- **Payer and rate basis** — Paid entirely by the employer. Rate depends on the company's industry risk grade.

**JKK risk grade table**

| Risk grade | Industry type | Rate |
| --- | --- | --- |
| Grade 1 | Very low risk (e.g. financial services, offices) | 0.24% |
| Grade 2 | Low risk (e.g. retail, hospitality) | 0.54% |
| Grade 3 | Medium risk (e.g. manufacturing, light industry) | 0.89% |
| Grade 4 | High risk (e.g. transportation, heavy industry) | 1.27% |
| Grade 5 | Very high risk (e.g. mining, construction) | 1.74% |

Source: `steevenz/id-payroll-calculator` → `State.php` → `$listOfJKKRiskGradePercentage` array.

### 6d — JKM (Jaminan Kematian / Death Insurance)

**JKM contribution table**

| Component | Rate | Paid by |
| --- | --- | --- |
| Employer contribution | 0.30% of gross monthly salary | Employer |
| Employee contribution | — | — |
| **Total** | **0.30%** |  |

Source: `steevenz/id-payroll-calculator` → `PayrollCalculator.php`.

### 6e — JKP (Jaminan Kehilangan Pekerjaan / Job Loss Insurance)

**JKP contribution table**

| Component | Rate | Paid by |
| --- | --- | --- |
| Contribution | 0.46% | Government + reallocation from JKK/JKM surplus |

- **JKP funding and impact** — JKP was introduced by PP 37/2021 (effective February 2022). The 0.46% is funded jointly: 0.22% from employer contribution reallocated from JKK/JKM, 0.14% from government, and 0.10% from reallocation of BPJS Ketenagakerjaan surplus. **No additional payroll deduction for employer or employee.** This program is listed for completeness but does not change the payroll calculation.

## Section 7 — Summary of all payroll contributions

**Summary of all payroll contributions**

| Program | Employer | Employee | Total |
| --- | --- | --- | --- |
| BPJS Kesehatan | 4.00% | 1.00% | 5.00% |
| JHT | 3.70% | 2.00% | 5.70% |
| JP (capped at IDR 10,547,400) | 2.00% | 1.00% | 3.00% |
| JKK (varies by risk grade) | 0.24%–1.74% | — | 0.24%–1.74% |
| JKM | 0.30% | — | 0.30% |
| **Total (using JKK grade 2)** | **10.54%** | **4.00%** | **14.54%** |

## Section 8 — TER (Tarif Efektif Rata-rata / Average Effective Rate)

- **TER scheme applicability** — Since 1 January 2024, monthly PPh 21 withholding for permanent employees uses the TER scheme (PP 58/2023, PMK 168/2023) instead of the old cumulative method.  _(PP 58/2023, PMK 168/2023)_
- **How TER works** — 1. Months January–November: PPh 21 = Gross Monthly Income × TER rate 2. December (or final month of employment): recalculate full-year liability using progressive brackets (Section 2), then subtract all TER withheld in months 1–11

### TER category assignment

**TER category assignment**

| TER Category | PTKP Status |
| --- | --- |
| A | TK/0, TK/1, K/0 |
| B | TK/2, TK/3, K/1, K/2 |
| C | K/3 |

### TER Category A — selected rates (common salary ranges)

**TER Category A — selected rates (common salary ranges)**

| Monthly gross income (IDR) | TER rate |
| --- | --- |
| 0 – 5,400,000 | 0% |
| 5,400,001 – 5,650,000 | 0.25% |
| 5,650,001 – 5,950,000 | 0.50% |
| 5,950,001 – 6,300,000 | 0.75% |
| 6,300,001 – 6,750,000 | 1.00% |
| 6,750,001 – 7,500,000 | 1.25% |
| 7,500,001 – 8,550,000 | 1.50% |
| 8,550,001 – 9,650,000 | 1.75% |
| 9,650,001 – 10,050,000 | 2.00% |
| 10,050,001 – 10,350,000 | 2.25% |
| 10,350,001 – 10,700,000 | 2.50% |
| 10,700,001 – 11,050,000 | 3.00% |
| 11,050,001 – 11,600,000 | 3.50% |
| 11,600,001 – 12,500,000 | 4.00% |
| 12,500,001 – 13,750,000 | 5.00% |
| 13,750,001 – 15,100,000 | 6.00% |
| 15,100,001 – 16,950,000 | 7.00% |
| 16,950,001 – 19,750,000 | 8.00% |
| 19,750,001 – 24,150,000 | 9.00% |
| 24,150,001 – 26,450,000 | 10.00% |
| 26,450,001 – 28,000,000 | 11.00% |
| 28,000,001 – 30,050,000 | 12.00% |
| 30,050,001 – 32,400,000 | 13.00% |
| 32,400,001 – 35,400,000 | 14.00% |
| 35,400,001 – 39,100,000 | 15.00% |
| 39,100,001 – 43,850,000 | 16.00% |
| 43,850,001 – 47,800,000 | 17.00% |
| 47,800,001 – 51,400,000 | 18.00% |
| 51,400,001 – 56,300,000 | 19.00% |
| 56,300,001 – 62,200,000 | 20.00% |
| 62,200,001 – 68,600,000 | 21.00% |
| 68,600,001 – 77,500,000 | 22.00% |
| 77,500,001 – 89,000,000 | 23.00% |
| 89,000,001 – 103,000,000 | 24.00% |
| 103,000,001 – 125,000,000 | 25.00% |
| 125,000,001 – 157,000,000 | 26.00% |
| 157,000,001 – 206,000,000 | 27.00% |
| 206,000,001 – 337,000,000 | 28.00% |
| 337,000,001 – 454,000,000 | 29.00% |
| 454,000,001 – 550,000,000 | 30.00% |
| 550,000,001 – 695,000,000 | 31.00% |
| 695,000,001 – 910,000,000 | 32.00% |
| 910,000,001 – 1,400,000,000 | 33.00% |
| Over 1,400,000,000 | 34.00% |

### TER Category B — selected rates (common salary ranges)

**TER Category B — selected rates (common salary ranges)**

| Monthly gross income (IDR) | TER rate |
| --- | --- |
| 0 – 6,200,000 | 0% |
| 6,200,001 – 6,500,000 | 0.25% |
| 6,500,001 – 6,850,000 | 0.50% |
| 6,850,001 – 7,300,000 | 0.75% |
| 7,300,001 – 9,200,000 | 1.00% |
| 9,200,001 – 10,750,000 | 1.50% |
| 10,750,001 – 11,250,000 | 2.00% |
| 11,250,001 – 11,600,000 | 2.50% |
| 11,600,001 – 12,600,000 | 3.00% |
| 12,600,001 – 13,600,000 | 4.00% |
| 13,600,001 – 14,950,000 | 5.00% |
| 14,950,001 – 16,400,000 | 6.00% |
| 16,400,001 – 18,450,000 | 7.00% |
| 18,450,001 – 21,850,000 | 8.00% |
| 21,850,001 – 26,000,000 | 9.00% |
| 26,000,001 – 27,700,000 | 10.00% |
| Over 27,700,000 | 11%–34% (see PP 58/2023 Annex) |

### TER Category C — selected rates (common salary ranges)

**TER Category C — selected rates (common salary ranges)**

| Monthly gross income (IDR) | TER rate |
| --- | --- |
| 0 – 6,600,000 | 0% |
| 6,600,001 – 6,950,000 | 0.25% |
| 6,950,001 – 7,350,000 | 0.50% |
| 7,350,001 – 7,800,000 | 0.75% |
| 7,800,001 – 8,850,000 | 1.00% |
| 8,850,001 – 9,800,000 | 1.25% |
| 9,800,001 – 10,950,000 | 1.50% |
| 10,950,001 – 11,200,000 | 1.75% |
| 11,200,001 – 12,050,000 | 2.00% |
| 12,050,001 – 12,950,000 | 3.00% |
| 12,950,001 – 14,150,000 | 4.00% |
| 14,150,001 – 15,550,000 | 5.00% |
| 15,550,001 – 17,050,000 | 6.00% |
| 17,050,001 – 19,500,000 | 7.00% |
| 19,500,001 – 22,700,000 | 8.00% |
| 22,700,001 – 26,600,000 | 9.00% |
| 26,600,001 – 28,100,000 | 10.00% |
| Over 28,100,000 | 11%–34% (see PP 58/2023 Annex) |

### TER Harian (Daily Rate) — for non-permanent employees

**TER Harian (Daily Rate) — for non-permanent employees**

| Daily gross income (IDR) | TER rate |
| --- | --- |
| ≤ 450,000 | 0% |
| 450,001 – 2,500,000 | 0.50% |
| > 2,500,000 | Use 50% × gross × progressive rates (Pasal 17) |

## Section 9 — Annual PPh 21 computation method (December recalculation)

- **December recalculation steps** — Step 1:  Gross annual income (gaji + tunjangan tetap + overtime + bonus + THR) Step 2:  − Biaya jabatan (5%, max IDR 6,000,000/year) Step 3:  − Iuran pensiun (employee JP contribution, if applicable) Step 4:  = Penghasilan Neto (net income) Step 5:  − PTKP (based on marital/dependent status) Step 6:  = PKP (Penghasilan Kena Pajak / taxable income) Step 7:  Apply progressive brackets (Section 2) → PPh 21 terutang (annual liability) Step 8:  − TER amounts withheld Jan–Nov Step 9:  = PPh 21 for December (or refund if negative)

## Section 10 — Worked example: monthly payroll calculation

Scenario: Permanent employee (pegawai tetap), single with no dependents (TK/0), has NPWP. Monthly base salary IDR 10,000,000. Company risk grade 2 (low). No overtime, no bonuses this month.

### A — Monthly gross earnings

**A — Monthly gross earnings**

| Component | Amount (IDR) |
| --- | --- |
| Base salary (gaji pokok) | 10,000,000 |
| Fixed allowances (tunjangan tetap) | 0 |
| **Monthly gross** | **10,000,000** |

### B — Employer BPJS contributions (company cost, not deducted from employee)

**B — Employer BPJS contributions (company cost, not deducted from employee)**

| Program | Rate | Amount (IDR) |
| --- | --- | --- |
| BPJS Kesehatan | 4.00% × 10,000,000 | 400,000 |
| JHT | 3.70% × 10,000,000 | 370,000 |
| JP | 2.00% × 10,000,000 | 200,000 |
| JKK (grade 2) | 0.54% × 10,000,000 | 54,000 |
| JKM | 0.30% × 10,000,000 | 30,000 |
| **Total employer cost** |  | **1,054,000** |

### C — Employee deductions (withheld from salary)

**C — Employee deductions (withheld from salary)**

| Program | Rate | Amount (IDR) |
| --- | --- | --- |
| BPJS Kesehatan | 1.00% × 10,000,000 | 100,000 |
| JHT | 2.00% × 10,000,000 | 200,000 |
| JP | 1.00% × 10,000,000 | 100,000 |
| **Total employee BPJS** |  | **400,000** |

### D — Monthly PPh 21 withholding (TER method, Jan–Nov)

- **PPh 21 monthly (TER)** — Status TK/0 → TER Category A. Monthly gross = IDR 10,000,000. From TER Category A table: IDR 9,650,001 – 10,050,000 → rate = 2.00%. PPh 21 monthly (TER) = 10,000,000 × 2.00% = IDR 200,000

### E — Take-home pay

**E — Take-home pay**

| Component | Amount (IDR) |
| --- | --- |
| Monthly gross | 10,000,000 |
| − Employee BPJS | (400,000) |
| − PPh 21 (TER) | (200,000) |
| **Take-home pay** | **9,400,000** |

### F — December recalculation (annual true-up)

**F — December recalculation (annual true-up)**

| Step | Description | Amount (IDR) |
| --- | --- | --- |
| Gross annual income | 10,000,000 × 12 | 120,000,000 |
| − Biaya jabatan | 5% × 120,000,000 = 6,000,000 (at cap) | (6,000,000) |
| − Iuran pensiun (JP employee) | 100,000 × 12 | (1,200,000) |
| **Penghasilan neto** |  | **112,800,000** |
| − PTKP (TK/0) |  | (54,000,000) |
| **PKP** |  | **58,800,000** |

**Annual tax on PKP of 58,800,000**

| Bracket | Taxable in bracket | Rate | Tax |
| --- | --- | --- | --- |
| 0 – 58,800,000 | 58,800,000 | 5% | 2,940,000 |
| **Total PPh 21 annual** |  |  | **2,940,000** |

- **PPh 21 for December** — PPh 21 annual          = IDR 2,940,000 − TER withheld (Jan–Nov) = 200,000 × 11 = IDR 2,200,000 PPh 21 December        = IDR 740,000

## Section 11 — Payroll calculation methods

The `steevenz/id-payroll-calculator` supports three PPh 21 calculation methods:

**Payroll calculation methods**

| Method | Indonesian | Description |
| --- | --- | --- |
| NETT | Pajak ditanggung perusahaan | Employer bears the tax; employee receives full salary |
| GROSS | Pajak ditanggung karyawan | Employee bears the tax; PPh 21 deducted from salary |
| GROSS-UP | Tunjangan pajak | Employer adds a tax allowance equal to the PPh 21 liability, then deducts it — net effect same as NETT but appears on payslip |

## Section 12 — Filing guidance

### Who must file?

- **Who must file** — All resident individuals with income above the PTKP threshold must file an annual SPT.

### Which form?

**Which form?**

| Form | Who |
| --- | --- |
| 1770SS | Single employer, gross income ≤ IDR 60,000,000/year |
| 1770S | Single employer, gross income > IDR 60,000,000/year |
| 1770 | Multiple income sources / business income |

### Key dates

**Key dates**

| Event | Deadline |
| --- | --- |
| Tax year end | 31 December |
| Monthly E-Bupot PPh 21/26 | 20th of following month |
| Annual SPT filing | 31 March |
| E-filing extension | Via DJP Online at https://djponline.pajak.go.id |

### Documents needed

- Bukti Potong 1721-A1 (withholding certificate from employer)
- BPJS contribution statements
- Additional income documentation (if applicable)
- NPWP (Nomor Pokok Wajib Pajak / Tax ID)

## Section 13 — Conservative defaults

When in doubt:

**Conservative defaults**

| Situation | Conservative position |
| --- | --- |
| Employee NPWP status unknown | Assume no NPWP → apply 20% surcharge on PPh 21; flag for confirmation |
| PTKP status unclear | Use TK/0 (lowest PTKP = highest tax); flag for reviewer |
| Company risk grade unknown | Use grade 2 (0.54%) as default; flag for confirmation |
| Employee permanent status unclear | Treat as permanent (pegawai tetap); flag for reviewer |
| Salary above JP cap | Cap JP contributions at IDR 10,547,400 wage basis |
| TER category unclear | Use Category A (most conservative); flag for reviewer |
| BPJS Kesehatan dependents > 5 | Add 1% deduction per extra dependent; confirm family count |
| Bonus / THR month | Include in gross for TER calculation that month; December true-up will reconcile |
| Mid-year joiner | Pro-rate PTKP for partial year; apply TER monthly as normal |

## Section 14 — Classification rules for bank statement

**Classification rules for bank statement**

| Pattern / Keyword | Classification | Notes |
| --- | --- | --- |
| Gaji / Salary / Payroll | Employment income (PPh 21) | Main salary |
| Tunjangan / Allowance | Employment income (PPh 21) | Fixed or variable allowance |
| Bonus / Gratifikasi | Employment income (PPh 21) | Irregular income, included in TER month |
| THR / Tunjangan Hari Raya | Employment income (PPh 21) | Holiday allowance |
| Lembur / Overtime | Employment income (PPh 21) | Overtime pay |
| BPJS / Iuran | Payroll deduction | Social security contribution |
| Potongan Pajak / PPh 21 | Tax withholding | Income tax withheld |
| Honorarium / Fee | PPh 21 (non-employee) or PPh 23 | Depends on relationship |
| Dividen / Dividend | PPh 23 or Final | Investment income |
| Bunga / Interest | PPh 23 or Final | Interest income |
| Sewa / Rent | PPh 23 or PPh 4(2) | Rental income |

## Section 15 — Sources

**Sources**

| Source | URL |
| --- | --- |
| DJP (Direktorat Jenderal Pajak) | https://www.pajak.go.id |
| DJP Online | https://djponline.pajak.go.id |
| UU HPP No. 7/2021 | Revenue Code — Pasal 17 ayat (1) huruf a |
| PP 58/2023 (TER PPh 21) | https://peraturan.bpk.go.id/Details/266564/pp-no-58-tahun-2023 |
| PMK 168/2023 (TER implementation) | https://jdih.kemenkeu.go.id |
| `steevenz/id-payroll-calculator` (MIT, 21★) | https://github.com/steevenz/id-payroll-calculator |
| `KejawenLab/PPH21` (MIT, 6★) | https://github.com/KejawenLab/PPH21 |
| BPJS Kesehatan | https://www.bpjs-kesehatan.go.id |
| BPJS Ketenagakerjaan | https://www.bpjsketenagakerjaan.go.id |

## OpenAccountants footer

OpenAccountants — open-source accounting skills for AI
This is not tax advice. All outputs must be reviewed by a qualified professional before filing.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

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
