---
name: id-payroll-pph21
description: >
  Calculate Indonesian calendar-2026 employment withholding, monthly TER and
  final-period reconciliation, keeping taxable benefits, employee deductions and
  BPJS contribution bases distinct. Trigger on PPh 21, payroll Indonesia, BPJS,
  PTKP, biaya jabatan, TER, THR, gross-up and termination withholding. Includes
  classification boundaries for non-employees, daily workers and non-residents.
version: "2.0"
jurisdiction: ID
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Indonesia Payroll: PPh 21 and BPJS v2.0

## Scope

Calendar-2026 Indonesian resident permanent-employee withholding, social-insurance reconciliation and related classification routes. Monthly cash pay, taxable employment gross, contribution wage and employer cost are different amounts. A salary-only TER calculation can be wrong if employer-paid health, accident or death insurance was omitted. [PMK 168/2023 arts. 5,7-10,15](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

Retain the original contributor credit: **Open Accountants Community**. The earlier `steevenz/id-payroll-calculator` (MIT) and `KejawenLab/PPH21` (MIT) are research history, not sources for legal rates. Their old pre-HPP brackets, wage caps and minimum-wage deduction logic are not used. No accountant approval is added.

## Ask the client first

Read intake and existing records before asking again. Obtain the actual employee category, tax residence/subjection dates, registration and mapped NIK/NPWP, start/end dates, marital/dependent status at the applicable date, earlier-employer slips, contract and gross/net/nett/gross-up arrangement. Collect the month-by-month pay ledger, bonuses/THR/overtime, cash allowances, benefits in kind, taxable insurance, employee pension/old-age payments through the employer, permitted religious contributions and earlier withholding/refunds.

For BPJS obtain the employer's registration and risk classification, worker's programme memberships, fixed wage and allowances, municipality/province and current minimum wage, pension ceiling by period, dependants, actual invoices and any approved temporary relief. Do not assume the tax-gross amount is the contribution wage. Preserve identifiers privately; never invent an NPWP or risk grade.

## The method, step by step

## Rates, bands and thresholds

## Section 2 : PPh 21 progressive tax brackets (Tarif Pasal 17 UU HPP)

Tax is computed on **Penghasilan Kena Pajak (PKP)** : taxable income after deductions and PTKP.

These brackets are from UU HPP No. 7/2021, effective from 1 January 2022 onward. Use these statutory bands for the 2026 calculation, with the actual employment period and taxpayer status established.

**PPh 21 progressive tax brackets**

| Annual PKP (IDR) | Rate | Max tax in bracket |
| --- | --- | --- |
| Up to 60,000,000 | 5% | 3,000,000 (computed maximum from the statutory band) [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 60,000,000, up to 250,000,000 | 15% | 28,500,000 (computed maximum from the statutory band) [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 250,000,000, up to 500,000,000 | 25% | 62,500,000 (computed maximum from the statutory band) [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 500,000,000, up to 5,000,000,000 | 30% | 1,350,000,000 (computed maximum from the statutory band) [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 5,000,000,000 | 35% | : (computed maximum from the statutory band) [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |

> **Note:** The `steevenz/id-payroll-calculator` and `KejawenLab/PPH21` repos use the older pre-HPP brackets (first bracket 0 to 50M, no 35% bracket). The brackets above reflect the current law.

- **No NPWP:** Income Tax Law art. 21(5a) imposes withholding twenty percent higher for a taxpayer without an NPWP. Establish actual tax registration and valid NIK/NPWP mapping first; citizenship, a missing printed card or a failed lookup is not proof of no registration. Do not derive the rule from a software repository. [Income Tax Law art. 21(5a)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

## Section 3 : PTKP (Penghasilan Tidak Kena Pajak / Non-Taxable Income)

PTKP is deducted from annual net income before applying the progressive brackets. Amounts are per PMK 101/PMK.010/2016, shown in DJP's official withholding book; apply the beginning-of-year status rule and specific exceptions in PMK 168 art. 9.

**PTKP status table**

| Status code | Description | Annual PTKP (IDR) |
| --- | --- | --- |
| TK/0 | Single, no dependents | 54,000,000 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| TK/1 | Single, 1 dependent | 58,500,000 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| TK/2 | Single, 2 dependents | 63,000,000 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| TK/3 | Single, 3 dependents | 67,500,000 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| K/0 | Married, no dependents | 58,500,000 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| K/1 | Married, 1 dependent | 63,000,000 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| K/2 | Married, 2 dependents | 67,500,000 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| K/3 | Married, 3 dependents | 72,000,000 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |

- **Additional rules** : Maximum 3 dependents (tanggungan) are recognized; If wife's income is combined (penghasilan digabung), add an additional IDR 54,000,000

Source: [DJP withholding book, PTKP tables and PMK 101/2016 reference](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf); [PMK 168 art. 9](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

### Employment deductions and taxable gross

1. Include salary, all taxable allowances, overtime, bonus, THR and other regular/irregular employment remuneration. Employer-paid JKK, JKM and health-insurance contributions/premiums described by art. 5(3)(d)-(f) enter employment gross. Qualifying employer-paid pension/old-age contributions are excluded under art. 7(c); employer-paid JHT/JP are not automatically added to taxable gross. Value any taxable benefits under the applicable natura rule, keeping exemptions separate. Foreign-currency pay uses the ministerial rate at the earlier payment/due event under art. 5(4). [PMK 168 arts. 5-7](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).
2. In non-final periods TER is applied to taxable gross without first subtracting employee BPJS, biaya jabatan or PTKP. These matter in final-period reconciliation where the law allows them. [PMK 168 arts. 8,15](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).
3. A permanent employee's biaya jabatan is five percent of gross, at most IDR 500,000 for each applicable employment month and IDR 6,000,000 annually. There is no general minimum-wage exclusion from this deduction. Qualifying employee-paid pension AND old-age contributions through the employer are deductible in the final calculation, not only JP. Permitted compulsory zakat/religious donations through the employer have their own conditions. [PMK 168 art. 10](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).
4. Pensioners instead have the separate five-percent pension-cost deduction capped at IDR 200,000 monthly/2,400,000 annually. Multiple employers/funds and non-withholding employers have the explicit art. 10/11 treatment; do not combine caps or duplicate a relief without analysing it. [PMK 168 arts. 10-11](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).
5. Determine PTKP using the relevant beginning-of-calendar-year status. A married female employee ordinarily receives her own allowance; the written local-government evidence that her husband has no income is required for the specified additional married/dependant treatment. A newcomer settling in Indonesia uses beginning-of-part-year-month facts under art. 9(5). Combined-spouse annual-return allowances are not automatically payroll PTKP at each employer. [PMK 168 art. 9](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1); [DJP PTKP explanation](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf).
6. Final PKP is net employment income less permitted PTKP, floored at zero and rounded DOWN to whole thousands of rupiah. Apply progressive bands to that base, then subtract earlier withholding. Round the final tax/payment only under the applicable official rule; do not round every intermediate component for convenience. [PMK 168 art. 8(3)-(5),15](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

### BPJS health: correct base, period and family

PPU health contributions are five percent total, split four percent employer and one percent employee. The upper monthly wage base is IDR 12,000,000. Perpres 59/2024's amended art. 32 changes the floor: provincial minimum, municipality/city minimum if one is set, with micro/small-business and specified-worker exceptions. Do not reuse an outdated universal municipal-floor statement or apply the ceiling to all employment cash indiscriminately. [Perpres 64/2020 amended arts. 30,32](https://jdih.djsn.go.id/assets/file/64-bpjs-2020.pdf); [Perpres 59/2024 art. I item 7, amended art. 32](https://jdih.djsn.go.id/assets/file/peraturan%20presiden%20nomor%2059%20tahun%202024.pdf).

Keep family enrolment separate from the employee's income-tax dependants. The old phrase "more than five family dependants" was not a safe entitlement test. Obtain covered family members and extra-family enrolment, relationship, authorisation and current BPJS assessment. Not yet confirmed: the precise extra-family one-percent collection and family-category rule for the actual employee under the current consolidated health legislation. Do not deduct an extra charge by counting every household member. KRIS/benefit-class changes do not by themselves prove that PPU contribution rates changed; obtain any actual later rate instrument rather than infer one from a benefit announcement.

### Employment social insurance

For wage-earning private-sector participants, JHT is 5.7% of the prescribed wage, split 3.7% employer and 2% employee. The wage ordinarily consists of basic pay plus fixed allowances; daily and output-based employment have their own averaging rules. [PP 46/2015 arts. 16-17](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/15122015_104556_PP%2046%20Tahun%202015.pdf). JP is 3% total, split 2% employer and 1% employee, on its separately capped wage; BPJS adjusts/announces the cap using prior-year GDP under art. 29. [PP 45/2015 arts. 28-29](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/15122015_104556_PP%2045%20Tahun%202015.pdf).

Not yet confirmed: the official BPJS-hosted 2026 pension-ceiling announcement and its effective periods. The old top-line IDR 11,086,300 marked "March 2025" linked to a privately hosted 2026 notice; the body used the earlier IDR 10,547,400 ceiling. Neither is certified as the current 2026 input here. Keep the actual period's official assessment/notice in the workpaper and stop a ceiling-sensitive computation until obtained. A copied vendor PDF is not used as authority. The rate and annual adjustment mechanism remain supported by PP 45; no guessed ceiling is substituted.

Ordinary JKK risk rates are 0.24%, 0.54%, 0.89%, 1.27% and 1.74%, paid by the employer. BPJS determines the actual risk group; the old retail/office/industry examples are clues, not an automatic assignment. Ordinary JKM is 0.30% employer-paid. Wage definitions and payment records must be checked against the participant category. [PP 44/2015 arts. 16-19](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/15122015_104557_PP%2044%20Tahun%202015.pdf).

JKP participants have a distinct allocation. PP 49/2023 inserted art. 16A: JKK after its 0.14% recomposition is 0.10%,0.40%,0.75%,1.13%,1.60%; its applicability and arrears exceptions must hold. It also inserted art. 18A with a 0.20% JKM amount after the stated recomposition. Do not treat those net allocations as a universal replacement for ordinary programme rates. [PP 49/2023 art. I items 3-4](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/Salinan_PP_Nomor_49_Tahun_2023.pdf).

The later PP 6/2025 amends JKP art. 11: total 0.36%, comprising government 0.22% and JKK recomposition 0.14%, with an IDR 5,000,000 wage ceiling. It is not the old 0.46% three-way funding formula, and is not an additional employee deduction. Establish enrolment, eligibility and the actual allocation on the assessed bill rather than adding JKP again to gross JKK. [PP 6/2025 amended art. 11, visually read pages 3-4](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/PP_Nomor_6_Tahun_2025.pdf).

Not yet confirmed: reconciliation of JKM allocation for an affected 2026 JKP participant where PP 49/2023 art. 18A and the later PP 6/2025 funding mechanism do not yield an unambiguous assessed split. The BPJS December-2025 article quotes ordinary JKM and contains an old JKM recomposition example alongside its new JKP funding text. The law and actual applicable assessment must resolve this; do not turn that article's mixed example into a universal payroll total. Ordinary non-JKP amounts above remain distinct. Also confirm any labour-intensive JKK relief and its actual period; the announced historical relief ran into January 2026, not automatically every 2026 month.

The old aggregate employer 10.54%, worker 4% and combined 14.54% only recompute if all underlying wage bases coincide, full ordinary low-risk JKK applies, health/JP caps do not bind, programme membership is established and no additional relief/charge applies: 4+3.7+2+0.54+0.30 and 1+2+1. Those are computed conditional comparisons, not a single statutory payroll rate.

### Monthly TER and worker classification

- **TER scheme applicability** : Since 1 January 2024, monthly PPh 21 withholding for permanent employees uses the TER scheme (PP 58/2023, PMK 168/2023) instead of the old cumulative method.  _(PP 58/2023, PMK 168/2023)_
- **Method:** For a permanent employee, apply TER to the entire taxable gross amount in each non-final employment period. In December or the actual final employment month, calculate the tax for the year/part year and subtract earlier withholding; do not take TER again. Pensioners and irregular commissioners have their stated separate rules. [PMK 168 arts. 8,15-16](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

### TER category assignment

**TER category assignment**

| TER Category | PTKP Status |
| --- | --- |
| A | TK/0, TK/1, K/0 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| B | TK/2, TK/3, K/1, K/2 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| C | K/3 [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |

### TER Category A : selected rates (common salary ranges)

**TER Category A : selected rates (common salary ranges)**

| Monthly gross income (IDR) | TER rate |
| --- | --- |
| Up to 5,400,000 | 0% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 5,400,000, up to 5,650,000 | 0.25% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 5,650,000, up to 5,950,000 | 0.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 5,950,000, up to 6,300,000 | 0.75% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 6,300,000, up to 6,750,000 | 1.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 6,750,000, up to 7,500,000 | 1.25% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 7,500,000, up to 8,550,000 | 1.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 8,550,000, up to 9,650,000 | 1.75% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 9,650,000, up to 10,050,000 | 2.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 10,050,000, up to 10,350,000 | 2.25% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 10,350,000, up to 10,700,000 | 2.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 10,700,000, up to 11,050,000 | 3.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 11,050,000, up to 11,600,000 | 3.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 11,600,000, up to 12,500,000 | 4.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 12,500,000, up to 13,750,000 | 5.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 13,750,000, up to 15,100,000 | 6.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 15,100,000, up to 16,950,000 | 7.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 16,950,000, up to 19,750,000 | 8.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 19,750,000, up to 24,150,000 | 9.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 24,150,000, up to 26,450,000 | 10.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 26,450,000, up to 28,000,000 | 11.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 28,000,000, up to 30,050,000 | 12.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 30,050,000, up to 32,400,000 | 13.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 32,400,000, up to 35,400,000 | 14.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 35,400,000, up to 39,100,000 | 15.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 39,100,000, up to 43,850,000 | 16.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 43,850,000, up to 47,800,000 | 17.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 47,800,000, up to 51,400,000 | 18.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 51,400,000, up to 56,300,000 | 19.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 56,300,000, up to 62,200,000 | 20.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 62,200,000, up to 68,600,000 | 21.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 68,600,000, up to 77,500,000 | 22.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 77,500,000, up to 89,000,000 | 23.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 89,000,000, up to 103,000,000 | 24.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 103,000,000, up to 125,000,000 | 25.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 125,000,000, up to 157,000,000 | 26.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 157,000,000, up to 206,000,000 | 27.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 206,000,000, up to 337,000,000 | 28.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 337,000,000, up to 454,000,000 | 29.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 454,000,000, up to 550,000,000 | 30.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 550,000,000, up to 695,000,000 | 31.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 695,000,000, up to 910,000,000 | 32.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 910,000,000, up to 1,400,000,000 | 33.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 1,400,000,000 | 34.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |

### TER Category B : selected rates (common salary ranges)

**TER Category B : selected rates (common salary ranges)**

| Monthly gross income (IDR) | TER rate |
| --- | --- |
| Up to 6,200,000 | 0% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 6,200,000, up to 6,500,000 | 0.25% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 6,500,000, up to 6,850,000 | 0.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 6,850,000, up to 7,300,000 | 0.75% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 7,300,000, up to 9,200,000 | 1.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 9,200,000, up to 10,750,000 | 1.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 10,750,000, up to 11,250,000 | 2.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 11,250,000, up to 11,600,000 | 2.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 11,600,000, up to 12,600,000 | 3.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 12,600,000, up to 13,600,000 | 4.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 13,600,000, up to 14,950,000 | 5.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 14,950,000, up to 16,400,000 | 6.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 16,400,000, up to 18,450,000 | 7.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 18,450,000, up to 21,850,000 | 8.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 21,850,000, up to 26,000,000 | 9.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 26,000,000, up to 27,700,000 | 10.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 27,700,000 | 11% to 34% (see PP 58/2023 Annex) [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |

### TER Category C : selected rates (common salary ranges)

**TER Category C : selected rates (common salary ranges)**

| Monthly gross income (IDR) | TER rate |
| --- | --- |
| Up to 6,600,000 | 0% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 6,600,000, up to 6,950,000 | 0.25% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 6,950,000, up to 7,350,000 | 0.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 7,350,000, up to 7,800,000 | 0.75% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 7,800,000, up to 8,850,000 | 1.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 8,850,000, up to 9,800,000 | 1.25% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 9,800,000, up to 10,950,000 | 1.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 10,950,000, up to 11,200,000 | 1.75% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 11,200,000, up to 12,050,000 | 2.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 12,050,000, up to 12,950,000 | 3.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 12,950,000, up to 14,150,000 | 4.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 14,150,000, up to 15,550,000 | 5.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 15,550,000, up to 17,050,000 | 6.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 17,050,000, up to 19,500,000 | 7.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 19,500,000, up to 22,700,000 | 8.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 22,700,000, up to 26,600,000 | 9.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 26,600,000, up to 28,100,000 | 10.00% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 28,100,000 | 11% to 34% (see PP 58/2023 Annex) [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |

### TER Harian (Daily Rate) : for non-permanent employees

**TER Harian (Daily Rate) : for non-permanent employees**

| Daily gross income (IDR) | TER rate |
| --- | --- |
| ≤ 450,000 | 0% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| Over 450,000, up to 2,500,000 | 0.50% [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |
| > 2,500,000 | Use 50% × gross × progressive rates (Pasal 17) [Official source](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) |

For non-permanent workers paid otherwise than monthly, apply daily/average-daily rules only in the art. 12(2)(a) category. The above IDR 2,500,000 daily route uses progressive rates on fifty percent of gross; monthly-paid non-permanent workers use monthly TER instead. A non-employee service recipient uses progressive rates on fifty percent of the documented gross under arts. 12(3)-(5), with the specific catering and evidenced pass-through rules. Irregular commissioners, activity participants, former employees and pension withdrawals have their own bases under art. 12 and rates under art. 16. Do not classify every freelancer as a permanent employee or apply the daily table to every consultant. [PMK 168 arts. 3,12-16](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

### Final-period reconciliation and payroll arrangements

Annualise net income and apportion tax when the employee's SUBJECTIVE TAX LIABILITY begins after January or ends before December under art. 15(3). A full-year resident merely starting or leaving a job mid-year is not automatically that case, and annual PTKP is not reduced in proportion to employment months. Use actual employment income/deductions for that job and any previous-employer documentation as required. Leave unexplained multi-employer and residence conflicts in the reviewer brief. [PMK 168 arts. 8-10,15](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

If earlier withholding exceeds final liability, return the excess to the employee with the withholding evidence by the end of the following month, subject to the government-borne-tax exclusion. The employer's overdeposit is dealt with through the applicable subsequent-period/correction mechanism, not silently kept as employer income. [PMK 168 arts. 21-22](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

Preserve gross, nett and gross-up contract distinctions. In gross pay the employee bears the computed tax; a net-pay promise requires the employer-funded tax/allowance and taxable-benefit treatment to be analysed. Gross-up adds the properly computed allowance, which can move TER bands; solve and re-test the entire gross amount, including taxable premiums. "NETT" and "GROSS-UP" are not automatically identical calculations, and an employer-borne payment is not automatically an exempt non-cash benefit. Not yet confirmed: the exact allowance/tax-borne treatment for a particular contract or specific government-borne incentive. Do not use a fixed-rate gross-up when a band changes.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| THR, bonus, overtime or irregular pay | Include in that month's taxable gross and use that month's complete TER band, with final reconciliation; no invented separate flat bonus rate |
| Employee without a printed NPWP or foreign passport | Establish actual valid tax registration and residence; NIK applies to resident individuals and sixteen-digit NPWP also covers non-resident individuals/entities, not a citizenship-only fifteen-digit rule |
| Non-resident worker | PPh 26 employment withholding, treaty/procedure and any later change to residence require their own analysis; do not apply resident PTKP/TER automatically |
| Mid-year hiring, cessation or foreign arrival/departure | Distinguish employment period from subjective-tax period; preserve all slips, dates and reasons before annualising |
| Unresolved BPJS cap, membership, JKP split, risk or temporary relief | Do not certify a complete contribution total; compute unaffected withholding only from established actual gross/premiums and name the unresolved item |
| Minimum wage or mixed fixed/variable allowances | Contribution-floor and wage-base tests are separate from taxable gross; no software-derived exemption from the position deduction |
| Benefits in kind or tax borne by another person | Identify the exact benefit, valuation, exemption and contract; avoid blanket tax-free/net-pay assumptions |
| Special sector, severance, pension lump sum or disputed status | Preserve the facts and route to the applicable separate final/non-final/special employment rules |

## Worked cases

### Case 1. The original IDR 10 million salary, with the missing tax-base bridge

Keep the original full-year 2026 resident permanent employee, TK/0, valid registration and IDR 10,000,000 cash salary. To test withholding rather than guess a BPJS assessment, the supplied employer documents establish monthly taxable premiums of health IDR 400,000, JKK IDR 54,000 and JKM IDR 30,000; employee qualifying JHT is IDR 200,000 and JP IDR 100,000. Employee health withholding is IDR 100,000. Employer JHT/JP are separately recorded as IDR 370,000/200,000 and excluded from taxable employment gross under art. 7(c). These are explicit case inputs; their assessed membership/risk/cap allocation must be independently correct for a real taxpayer, and this case does not resolve the pending JKP split. Assume no bonus/THR, other benefits, permitted religious deductions or previous employment. [PMK 168 arts. 5,7-10,15](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

Taxable monthly gross is 10,484,000, in Category A's over-10,350,000 through-10,700,000 band at 2.5%. Monthly non-final withholding is **262,100**, not the old salary-only 200,000. Annual gross 125,808,000 less position cost 6,000,000 and employee JHT+JP 3,600,000 gives net 116,208,000; less PTKP 54,000,000 gives PKP 62,208,000. Tax is 3,000,000 plus 15% of 2,208,000 = **3,331,200**. Earlier withholding 2,883,100 leaves **448,100** for December. Jan-Nov cash take-home is **9,337,900**; December is **9,151,900**. The old annual 2,940,000 and December 740,000 omitted taxable premiums and JHT relief. [DJP TER/PTKP tables](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf); [PMK 168 arts. 5-15](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

```oa-check
name: Original salary corrected taxable insurance and JHT relief
inputs:
  salary: 10000000
  health_employer: 400000
  jkk_employer: 54000
  jkm_employer: 30000
  employee_jht: 200000
  employee_jp: 100000
  health_employee: 100000
  ter: 0.025
  ptkp: 54000000
steps:
  - gross_month: salary + health_employer + jkk_employer + jkm_employer
  - monthly_tax: gross_month * ter
  - gross_year: gross_month * 12
  - position_cost: min(gross_year * 0.05, 6000000)
  - employee_qualifying_contributions: (employee_jht + employee_jp) * 12
  - net: gross_year - position_cost - employee_qualifying_contributions
  - taxable: max(net - ptkp, 0)
  - annual_tax: min(taxable, 60000000) * 0.05 + max(taxable - 60000000, 0) * 0.15
  - previous_withholding: monthly_tax * 11
  - december_tax: annual_tax - previous_withholding
  - employee_contributions: employee_jht + employee_jp + health_employee
  - ordinary_take_home: salary - employee_contributions - monthly_tax
  - december_take_home: salary - employee_contributions - december_tax
expected:
  gross_month: 10484000
  monthly_tax: 262100
  gross_year: 125808000
  position_cost: 6000000
  employee_qualifying_contributions: 3600000
  net: 116208000
  taxable: 62208000
  annual_tax: 3331200
  previous_withholding: 2883100
  december_tax: 448100
  employee_contributions: 400000
  ordinary_take_home: 9337900
  december_take_home: 9151900
```

### Case 2. Full-year resident hired in July, PTKP is not halved

Assume the employee is resident throughout 2026, TK/0, with no earlier employment or other income. July-December taxable gross, already including all taxable benefits, totals IDR 60,000,000; documented employee pension/old-age deductions total IDR 1,800,000. Position cost is 3,000,000, within the six-month cap, net 55,200,000 and annual PTKP remains 54,000,000. PKP is 1,200,000, tax **60,000**. Using a half-year PTKP of 27,000,000 would wrongly produce tax 1,410,000. Actual final withholding is that 60,000 less prior withholding; a negative difference is an employee refund, not zeroed away. This case does not apply to a person whose subjective Indonesian liability first begins in July. [PMK 168 arts. 8-10,15,21](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

```oa-check
name: Employment start is not a subjective-tax start
inputs:
  gross: 60000000
  months: 6
  employee_qualifying: 1800000
  full_ptkp: 54000000
steps:
  - position_cost: min(gross * 0.05, months * 500000)
  - net: gross - position_cost - employee_qualifying
  - taxable: max(net - full_ptkp, 0)
  - tax: taxable * 0.05
  - incorrect_taxable: net - full_ptkp * months / 12
  - incorrect_tax: incorrect_taxable * 0.05
  - overstatement: incorrect_tax - tax
expected:
  position_cost: 3000000
  net: 55200000
  taxable: 1200000
  tax: 60000
  incorrect_taxable: 28200000
  incorrect_tax: 1410000
  overstatement: 1350000
```

## When to refuse or refer

Do not produce a taxpayer-specific withholding result without the taxable pay, worker category, status/period and necessary prior withholding. Do not fabricate BPJS ceilings, residence, dependants, NPWP status, risk grade, a programme membership or exemption. Compute only established portions with explicit assumptions and a named list of unresolved portions. Refer non-residents/treaties, severance and pension lump sums, benefits outside the supported rule, unusual multi-employer histories, disputed employment and uncertain incentives. Never submit a return, enrol someone, transmit credentials or post payroll from this method.

## Filing and payment

Ordinary monthly PPh 21 deposit is due on the fifteenth of the following month, replacing the old tenth-of-month instruction. Apply the actual holiday rule under PMK 81 art. 100 and distinguish tax payment from BPJS remittance. Monthly withholding return ordinarily follows the twenty-day-after-period-end rule, with the actual current return and exceptions checked. Keep calculation, state receipt/NTPN, withholding evidence and submission receipt separate. PMK 168 art. 20 requires reporting even for nil withholding where income was paid; no income at all has the separate art. 20(4) exception. [PMK 81 arts. 94,100](https://pajak.go.id/en/node/113110); [KUP art. 3(3)(a)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 168 arts. 19-22](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

Use the current Coretax PPh 21/26 return and employer-issued annual/final-period employee slip. Legacy 1721-A1/A2 names are search aids; an employee withholding certificate is not a separate annual employer tax return due in March. The individual's annual return is a different obligation, ordinarily three months after calendar-year end. Confirm the actual current form, certificate issuance period, e-signing role and supported channel against the official period-specific instructions. NPWP migration is based on resident-individual status, not a blanket Indonesian-citizen/foreign-citizen split; non-resident individuals and entities also use the sixteen-digit format. [DJP identification launch](https://www.pajak.go.id/index.php/id/siaran-pers/peluncuran-layanan-perpajakan-berbasis-nik-sebagai-npwp-npwp-16-digit-dan-nitku); [PMK 168 arts. 20-22](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1); [KUP arts. 3,28](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

The retained payroll output is a monthly employee register, payslip, employer-cost bridge, separately based BPJS schedule, withholding certificate register and annual/final reconciliation with payment/submission evidence. Export an approval-ready workbook when requested, using formulas and a per-employee assumptions/exception column. The original statutory deduction, annual liability, TER, cash pay and employer costs must each reconcile independently; do not use the cash payroll total as the tax return's entire gross amount.

## Completion checklist

- Category, residence/subjection and employment periods established; previous slips reconciled.
- Taxable gross includes the specified employer premiums and taxable benefits; excluded employer retirement contributions are separate.
- PTKP status, position/pension cost, employee JHT/JP and religious deductions follow the applicable rule; taxable base is floored and rounded correctly.
- Monthly TER table/category uses the full taxable gross and exact limits; final month uses progressive reconciliation and returns any excess.
- BPJS wage bases, floors, caps, risk, JKP membership, allocation and temporary relief documented; unresolved portions are not presented as complete payroll.
- Gross/nett/gross-up contract and allowance treatment documented; no double tax or benefit counted.
- Monthly deposit, filing and withholding evidence are separately scheduled; taxpayer annual return and employee certificate are not confused.
- Report every remaining uncertainty and send the computation for the original required professional review before filing.

## Sources

| Official source | Read for and read date |
|---|---|
| [DJP consolidated Income Tax/KUP laws](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) | Income Tax arts. 17,21(5a),25 and KUP arts. 3,7,9,28; statutory bands, no-NPWP uplift, deadlines and records. Read 2026-11-14. |
| [PMK 168/2023 operative text](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1) | Arts. 1-25, taxable/excluded premiums, deductions, PTKP status, categories, resident/non-resident bases, final-month and excess-withholding treatment. Read 2026-11-14. |
| [PP 58/2023](https://jdih.kemenkeu.go.id/api/download/e47c3fc4-a912-4bf1-bcad-335fee3f71f8/2023pp058.pdf) | Operative monthly/daily TER framework and category assignment; annex figures cross-read in DJP's clearer book tables. Read 2026-11-14. |
| [DJP Cermat PPh 21 book](https://www.pajak.go.id/sites/default/files/2024-01/Buku%20Cermat%20Pemotongan%20PPh%20Pasal%2021.pdf) | Printed pages 39-42 and 46-48, full Category A and selected B/C/daily tables and PTKP, not the old software rates. Read 2026-11-14. |
| [PP 46/2015](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/15122015_104556_PP%2046%20Tahun%202015.pdf) | Arts. 16-17 private wage-earner JHT rate/split and contribution wage. Read 2026-11-14. |
| [PP 45/2015](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/15122015_104556_PP%2045%20Tahun%202015.pdf) | Arts. 28-29 JP rate/split, basic+fixed wage and official GDP adjustment/announcement mechanism, not a verified current cap. Read 2026-11-14. |
| [PP 44/2015](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/15122015_104557_PP%2044%20Tahun%202015.pdf) | Arts. 16-19 ordinary JKK/JKM rates, assigned risk and wage base. Read 2026-11-14. |
| [PP 49/2023](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/Salinan_PP_Nomor_49_Tahun_2023.pdf) | Inserted arts. 16A/18A participant/arrears conditions and recomposed allocations; current JKM split remains flagged. Read 2026-11-14. |
| [PP 6/2025](https://www.bpjsketenagakerjaan.go.id/assets/uploads/peraturan/PP_Nomor_6_Tahun_2025.pdf) | Amended art. 11 on visually inspected pages 3-4, current JKP funding/rates/cap; scan OCR saved for evidence. Read 2026-11-14. |
| [Perpres 64/2020](https://jdih.djsn.go.id/assets/file/64-bpjs-2020.pdf) | Amended arts. 30,32 health contribution split and ceiling. Read 2026-11-14. |
| [Perpres 59/2024](https://jdih.djsn.go.id/assets/file/peraturan%20presiden%20nomor%2059%20tahun%202024.pdf) | Amended art. 32 current floor/ceiling and micro/small exception. Read 2026-11-14. |
| [PMK 81/2024](https://pajak.go.id/en/node/113110) | Arts. 94-95,100 ordinary tax deposits, annual settlement and holiday adjustment, separate from BPJS collection. Read 2026-11-14. |
| [DJP NIK/NPWP/NITKU launch](https://www.pajak.go.id/index.php/id/siaran-pers/peluncuran-layanan-perpajakan-berbasis-nik-sebagai-npwp-npwp-16-digit-dan-nitku) | Resident/non-resident identifier distinction. Read 2026-11-14. |

Not yet confirmed: official current 2026 JP ceiling and effective periods; affected JKP/JKM allocation against the later law and actual assessment; current extra-family health collection rule; particular gross-up/employer-borne-tax contracts, benefit/incentive exceptions, labour-intensive relief period, prescribed payment rounding and exact current Coretax field/certificate issuance details. Do not use the older copied/vendor figures as substitutes.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs require the qualified professional review already required by this workflow before filing.

The most up-to-date version is maintained at openaccountants.com.
