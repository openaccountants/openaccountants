---
name: gu-payroll
description: Run 2026 payroll for a Guam employer. Covers Guam territorial income tax withholding on wages under the mirror of IRC chapter 24 (Form W-4 and the federal withholding methods with Guam read for the United States), the quarterly withholding return (Form W-1) due by the last day of the month after each quarter, the quarterly SWICA wage report, Form W-2GU to employees and Copy 1 with Form W-3SS to the Department of Revenue and Taxation, Copy A to the SSA by 1 February 2027, federal social security and Medicare (FICA) which apply in Guam on Form 941, no FUTA in Guam, MSRRA spouses and federal employees. Trigger on "Guam payroll", "W-2GU", "Guam withholding", "Form W-1 Guam", "SWICA Guam", "Guam employer FICA", "Guam unemployment tax".
version: "1.0"
jurisdiction: US-GU
tax_year: 2026
last_updated: 2026-11-14
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Guam: payroll, 2026

> **Source-cited draft.** Built from 48 U.S.C. 1421i, IRS Pub. 15 (2026), the 2026 General Instructions for Forms W-2 and W-3, Form W-2GU (2026), the Guam Department of Revenue and Taxation (DRT) tax calendar and its GuamTax.com e-services page, read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A Guam employer withholds **Guam income tax** (not US income tax) from wages, using the US withholding rules that Guam mirrors (48 U.S.C. 1421i(d)(1) includes IRC chapter 24). It reports and pays that tax to the **DRT** on the quarterly **Form W-1**, due by the **last day of the month after each quarter** (30 April, 31 July, 31 October, 31 January), with the quarterly **SWICA** wage report. The **federal** social security and Medicare taxes (FICA) apply to Guam wages as they do in the 50 states and go to the IRS on **Form 941**. **FUTA does not apply** in Guam. After the year, each employee gets a **Form W-2GU** (box 2 is Guam income tax withheld) by **1 February 2027**; Copy A with Form W-3SS goes to the SSA by the same date and Copy 1 with Form W-3SS goes to the DRT.

## Scope and who this is for

In scope: a private employer with employees working in Guam, for wages paid in 2026: what to withhold, which returns to file with Guam and with the IRS, year-end W-2GU, and the special cases (MSRRA spouses, US-withholding employees, federal agencies).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| FICA rates, wage base, Additional Medicare Tax, Form 941 deposits and lines | `us-form-941-940-payroll` |
| The withholding tables and methods for 2026 (Pub. 15-T) | `us-form-941-940-payroll` |
| Employee or contractor | `us-worker-classification-w2-vs-1099` |
| Employee's own Guam return and residence | `gu-individual-income-tax` |
| Business privilege tax on the employer's receipts | `gu-business-privilege-tax` |
| Federal agencies withholding for Guam residents (Pub. 15, section 17) | refer |

## Ask the client first

1. **Where each employee works and lives**, and whether any is a **civilian spouse of a servicemember** claiming a state residence under MSRRA.
2. **Wages paid each pay period in 2026**, pay frequency, and each employee's Form W-4.
3. **Guam income tax withheld and paid** for each quarter, and W-1 returns already filed.
4. **Form 941** filings and FICA deposits so far (handled in `us-form-941-940-payroll`).
5. **GuamTax.com business account** and SWICA and W-2/W-3 e-filing registration.
6. **New hires** in 2026 (Pub. 15 says most territories have a new hire registry; check with the DRT).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule, 2026 | Source |
| --- | --- | --- |
| Guam income tax withholding on wages | US chapter 24 rules applied as Guam law (Form W-4, Pub. 15-T methods) | [48 U.S.C. 1421i(d)(1) and (e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title48/html/USCODE-2024-title48-chap8A-subchapI-sec1421i.htm) |
| Federal income tax withholding by a Guam employer | Not applicable unless the employee is subject to US withholding | [IRS Pub. 15 (2026), Federal Income Tax Withholding, Caution](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Social security and Medicare (FICA) | Apply in Guam ("United States" includes Guam) | [IRS Pub. 15 (2026), Introduction](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| FUTA | Does not apply to employers in Guam | [IRS Pub. 15 (2026), section 14, Caution](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Quarterly withholding return (W-1) and SWICA due | Last day of the month after the quarter: 30 April, 31 July, 31 October, 31 January | [DRT tax calendar](https://www.guamtax.com/info/calendar.html) |
| W-2GU to employees and to the DRT | 31 January (DRT calendar); 1 February 2027 for 2026 forms (31 January 2027 is a Sunday) | [DRT tax calendar](https://www.guamtax.com/info/calendar.html); [General Instructions for Forms W-2 and W-3 (2026)](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf) |
| W-2GU Copy A and W-3SS to the SSA | 1 February 2027 | [General Instructions for Forms W-2 and W-3 (2026), Due date for filing with SSA](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf) |

The 2026 FICA rates and wage base are in `us-form-941-940-payroll`; they are not restated here.

### Step 1: each pay period

1. **Guam income tax**: compute it from the employee's Form W-4 with the 2026 Pub. 15-T method, exactly as for US withholding, but it is Guam tax payable to the DRT.
2. **FICA**: withhold the employee share and add the employer share as in `us-form-941-940-payroll`. It is federal tax, paid to the IRS.
3. **MSRRA spouse** who properly claims a state residence: the wages are not Guam income; withhold **US** income tax instead and report on Form W-2, not W-2GU (General Instructions for Forms W-2 and W-3, MSRRA).

### Step 2: each quarter

4. **Form W-1** (Employer's Quarterly Withholding Tax Return) to the DRT for the Guam income tax withheld in the quarter, e-filed at GuamTax.com ("E-File W-1"), by the last day of the following month.
5. **SWICA** quarterly wage report to the DRT, same date ("E-File SWICA").
6. **Form 941** to the IRS for FICA (and any US income tax withheld from MSRRA employees), with deposits on the IRS schedule (`us-form-941-940-payroll`).

### Step 3: year end

7. **Form W-2GU** for each employee: box 1 wages, **box 2 Guam income tax withheld**, boxes 3 to 6 social security and Medicare wages and tax.
8. Furnish W-2GU to employees by 1 February 2027. File **Copy A with Form W-3SS** with the SSA by 1 February 2027 (paper or Business Services Online) and **Copy 1 with Form W-3SS** with the DRT, P.O. Box 23607, Barrigada, GU 96921, or e-file at GuamTax.com ("E-File W-3/W-2GU").
9. **Reconcile**: the W-2GU box 2 total must equal the Guam tax on the four W-1 returns, and boxes 3 to 6 must agree with the four Forms 941.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Employee works in Guam, lives in Guam | Guam withholding; W-2GU |
| MSRRA civilian spouse with a state residence | US withholding; Form W-2; not on the W-1 |
| Employee of a mainland employer temporarily in Guam | Mainland employer's US rules; check the de minimis rule in `gu-individual-income-tax` |
| Guam employer with no FICA-exempt workers | FICA on all wages up to the wage base |
| Employer asks about Guam unemployment insurance | No FUTA in Guam; no Guam unemployment contribution was found on the DRT calendar (not confirmed) |
| EIC notice to employees | Not required for employees in Guam (Pub. 15, section 10) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| MSRRA claim | Treat as Guam wages until the employee documents a state residence |
| Form W-4 | Withhold as a single filer with no adjustments, as Pub. 15-T directs |
| GuamTax.com e-file registration | Register with the SWICA and W-2/W-3 e-filing form before the first due date |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Guam tax withheld but sent to the IRS on Form 941 | Wrong government; the DRT will assess |
| Form W-2 issued instead of W-2GU | The employee's Guam return will not match |
| FUTA paid for Guam employees | Not owed; claim it back |
| W-2GU box 2 total differs from the W-1 returns | DRT mismatch notice |

## Worked cases

**Case 1, quarterly W-1 and year-end reconciliation.** A Guam restaurant withheld Guam income tax of USD 3,200, USD 3,450, USD 3,100 and USD 3,900 in the four quarters of 2026 (worked out from the employees' Forms W-4 with Pub. 15-T). Each amount goes on that quarter's W-1, the fourth by 31 January 2027. The W-2GU box 2 total for the year must be USD 13,650; the W-2GUs show USD 13,600, so one employee's form is USD 50 short and must be corrected before filing.

```oa-check
name: Guam W-1 quarters against W-2GU box 2 (2026)
inputs:
  q1: 3200
  q2: 3450
  q3: 3100
  q4: 3900
  w2gu_box2_total: 13600
steps:
  - w1_total: q1 + q2 + q3 + q4
  - difference: w1_total - w2gu_box2_total
expected:
  w1_total: 13650
  difference: 50
```

**Case 2, a decision: Guam or US withholding for an MSRRA spouse.** A Guam clinic has three employees. Two live in Guam; Guam tax withheld in the quarter is USD 1,800 and USD 1,350. The third is the civilian spouse of a sailor stationed in Guam and keeps a Texas residence under MSRRA; the payroll system computed USD 900 on her wages. Her wages are not Guam income, so her USD 900 is withheld as **US** income tax, reported on Form 941 and a Form W-2, and left off the W-1. The W-1 shows USD 3,150. If she does not document the state residence, the default is Guam withholding, and the W-1 would show USD 4,050.

```oa-check
name: MSRRA spouse left off the Guam W-1 (2026 quarter)
inputs:
  guam_emp_a: 1800
  guam_emp_b: 1350
  msrra_emp: 900
steps:
  - w1_guam_tax: guam_emp_a + guam_emp_b
  - us_income_tax_on_941: msrra_emp
  - w1_if_no_msrra: guam_emp_a + guam_emp_b + msrra_emp
expected:
  w1_guam_tax: 3150
  us_income_tax_on_941: 900
  w1_if_no_msrra: 4050
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GU-PR-FED | Federal agency employer, or federal pensions to Guam residents | Refer: Pub. 15, section 17 certification |
| R-GU-PR-DEPOSIT | When Guam withholding must be deposited within the quarter | Refer to DRT: not confirmed (see Sources) |
| R-GU-PR-H2 | H-2 or other nonimmigrant workers and their FICA status | Refer: Pub. 15 special rules |
| R-GU-PR-PENALTY | Late W-1, late W-2GU penalties | Refer: mirror code penalties applied by DRT |

## Filing and payment

Guam income tax withheld: Form W-1 by **30 April, 31 July and 31 October 2026 and 31 January 2027**, with SWICA on the same dates, at GuamTax.com. FICA: Form 941 to the IRS on its quarterly dates with deposits (`us-form-941-940-payroll`). Year end: W-2GU to employees, Copy A with W-3SS to the SSA and Copy 1 with W-3SS to the DRT, all by **1 February 2027**. A due date on a weekend or holiday moves to the next working day (DRT calendar).

## Completion checklist

- Guam income tax withheld on Guam wages with the 2026 Pub. 15-T method; US withholding only for MSRRA or other US-withholding employees.
- FICA withheld and reported on Form 941; no FUTA.
- Four W-1 returns and four SWICA reports filed.
- W-2GU box 2 reconciled to the W-1 returns; W-3SS to the SSA and to the DRT.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 48 U.S.C. 1421i (govinfo, 2024 edition). Read for (d)(1): chapters 24 and 25 (collection of income tax at source on wages) are part of the Guam income tax laws; (e) "Guam" read for "United States". | https://www.govinfo.gov/content/pkg/USCODE-2024-title48/html/USCODE-2024-title48-chap8A-subchapI-sec1421i.htm | 2026-11-14 |
| IRS Pub. 15 (2026). Read for "United States" including Guam, federal income tax withholding not applying to Guam employers, FUTA not applying to Guam employers (section 14), the EIC notice exception (section 10), new hire registries, section 17 on federal agencies. | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-14 |
| General Instructions for Forms W-2 and W-3 (2026). Read for Form W-2GU for Guam wages paid by Guam employers, MSRRA, the 1 February 2027 due date to the SSA and employees, Copy 1 with W-3SS to the DRT address. | https://www.irs.gov/pub/irs-pdf/iw2w3.pdf | 2026-11-14 |
| Form W-2GU (2026). Read for box 2 "Guam income tax withheld" and boxes 3 to 6. | https://www.irs.gov/pub/irs-pdf/fw2gu.pdf | 2026-11-14 |
| DRT tax calendar. Read for the quarterly W-1 and SWICA dates, W-2GU to employees and to DRT by 31 January, the weekend rule. | https://www.guamtax.com/info/calendar.html | 2026-11-14 |
| DRT GuamTax.com home page and SWICA and W-2/W-3 e-filing registration form. Read for the e-services (E-File W-1, SWICA, W-3/W-2GU). | https://www.guamtax.com/ | 2026-11-14 |

Not yet confirmed: no DRT page or regulation stating whether Guam withholding must be deposited more often than quarterly was found (the calendar shows only the quarterly W-1); whether Guam has a new hire registry or any employer contribution of its own; that DRT uses the 2026 Pub. 15-T tables without change (inferred from 48 U.S.C. 1421i).
