---
name: gu-payroll
description: Run 2026 payroll for a Guam employer. Covers Guam territorial income tax withholding on wages under the mirror of IRC chapter 24 (Form W-4 and the federal withholding methods with Guam read for the United States), the quarterly withholding return (Form W-1) due by the last day of the month after each quarter, the quarterly SWICA wage report, Form W-2GU to employees and Copy 1 with Form W-3SS to the Department of Revenue and Taxation, Copy A to the SSA by 1 February 2027, federal social security and Medicare (FICA) which apply in Guam on Form 941, no FUTA in Guam, MSRRA spouses and federal employees. Trigger on "Guam payroll", "W-2GU", "Guam withholding", "Form W-1 Guam", "SWICA Guam", "Guam employer FICA", "Guam unemployment tax".
version: "1.2"
jurisdiction: US-GU
tax_year: 2026
last_updated: 2026-11-22
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Guam: payroll, 2026

> **Source-cited draft.** Built from 48 U.S.C. 1421i, IRS Pub. 15 (2026), the 2026 General Instructions for Forms W-2 and W-3, Form W-2GU (2026), the Guam Department of Revenue and Taxation (DRT) tax calendar and its GuamTax.com e-services page, read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A Guam employer withholds **Guam income tax** (not US income tax) from wages, using the US withholding rules that Guam mirrors (48 U.S.C. 1421i(d)(1) includes IRC chapter 24). Report withholding to the **DRT** on quarterly **Form W-1**, normally due on the **last day of the following month**, and make deposits during the quarter when required. File the separate **SWICA** wage report by the **30th day after the quarter** under 11 GCA 41104. The **federal** social security and Medicare taxes (FICA) apply to Guam wages as they do in the 50 states and go to the IRS on **Form 941**. **FUTA does not apply** in Guam. After the year, each employee gets a **Form W-2GU** (box 2 is Guam income tax withheld) by **1 February 2027**; Copy A with Form W-3SS goes to the SSA by the same date and Copy 1 with Form W-3SS goes to the DRT.

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
6. **New hires and rehires** in 2026 and when they were reported to the Guam Directory of New Hires.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule, 2026 | Source |
| --- | --- | --- |
| Guam income tax withholding on wages | US chapter 24 rules applied as Guam law (Form W-4, Pub. 15-T methods) | [48 U.S.C. 1421i(d)(1) and (e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title48/html/USCODE-2024-title48-chap8A-subchapI-sec1421i.htm) |
| Federal income tax withholding by a Guam employer | Not applicable unless the employee is subject to US withholding | [IRS Pub. 15 (2026), Federal Income Tax Withholding, Caution](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Social security and Medicare (FICA) | Apply in Guam ("United States" includes Guam) | [IRS Pub. 15 (2026), Introduction](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| FUTA | Does not apply to employers in Guam | [IRS Pub. 15 (2026), section 14, Caution](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Quarterly withholding return (W-1) | Last day of the following month, subject to the DRT weekend and legal holiday rule | [DRT tax calendar](https://www.guamtax.com/info/calendar.html) |
| Quarterly SWICA report (SW-2) | 30th day after the quarter under the statute. The DRT calendar lists the last day of the month. Meet the statutory date or obtain DRT confirmation of any extension. | [11 GCA 41104](https://www.guamcourts.org/CompilerofLaws/GCA/11gca/11gc041.PDF) |
| W-2GU to employees and to the DRT | 31 January (DRT calendar); 1 February 2027 for 2026 forms (31 January 2027 is a Sunday) | [DRT tax calendar](https://www.guamtax.com/info/calendar.html); [General Instructions for Forms W-2 and W-3 (2026)](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf) |
| W-2GU Copy A and W-3SS to the SSA | 1 February 2027 | [General Instructions for Forms W-2 and W-3 (2026), Due date for filing with SSA](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf) |
| FICA territorial link | Guam is in "State" (IRC 3121(e)(1)) and "United States" (3121(e)(2)) | [IRC section 3121](https://uscode.house.gov/us/usc/119-124/t26/s3121/) |
| Philippines residents on H-2 in Guam | Not employment for FICA: service in Guam by a resident of the Philippines temporarily in Guam as a nonimmigrant under INA 101(a)(15)(H)(ii) (3121(b)(18)) | same |
| Government of Guam service | Brought back into FICA by 3121(b)(7)(B) and (D), subject to the retirement-system conditions; Medicare for government service follows 3121(u) | same |

The 2026 FICA rates and wage base are in `us-form-941-940-payroll`; they are not restated here.

### Step 1: each pay period

1. **Guam income tax**: apply the mirrored withholding rules using the employee’s valid Form W-4 and the [2026 Pub. 15-T method](https://www.irs.gov/pub/irs-pdf/p15t.pdf). Confirm any DRT-specific instructions. The tax is payable to the DRT.
2. **FICA**: withhold the employee share and add the employer share as in `us-form-941-940-payroll`. It is federal tax, paid to the IRS.
3. **MSRRA spouse** with qualifying state tax residence or domicile: if in Guam solely to accompany a servicemember stationed there under military orders, wages are generally outside Guam withholding. Withhold **US** income tax and use Form W-2. Check state and local withholding and any residence election under [50 U.S.C. 4001(a)(3), (c)](https://uscode.house.gov/us/usc/119-120/t50/s4001/).

### Step 2: each quarter

4. **Form W-1** to the DRT for the Guam income tax withheld in the quarter by the last day of the following month, adjusted for weekends and legal holidays. Use E-File W-1 at GuamTax.com. See Filing and payment for deposits.
5. **SWICA** quarterly wage report (SW-2) to the DRT by the statutory 30th day after the quarter. Use E-File SWICA. Report new hires and rehires separately within **20 days** of hire unless the statutory electronic or magnetic reporting schedule applies. Under that option, send two transmissions per month, 12 to 16 days apart. [5 GCA 34304](https://www.guamcourts.org/compileroflaws/GCA/05gca/5gc034.pdf)
6. **Form 941** to the IRS for FICA (and any US income tax withheld from MSRRA employees), with deposits on the IRS schedule (`us-form-941-940-payroll`).

### Step 3: year end

7. **Form W-2GU** for each employee with Guam wages. Box 1 shows wages and taxable compensation, **box 2 Guam income tax withheld**, boxes 3 and 4 social security wages excluding tips and social security tax, box 5 Medicare wages and tips, and box 6 Medicare tax. Social security tips go in box 7.
8. Furnish W-2GU to employees by 1 February 2027. File **Copy A with Form W-3SS** with the SSA by 1 February 2027 and **Copy 1 with Form W-3SS** with the DRT. Use the applicable electronic filing service when mandatory. If paper filing is permitted, the DRT address is P.O. Box 23607, Barrigada, GU 96921. Check the [IRS instructions](https://www.irs.gov/pub/irs-pdf/iw2w3.pdf) and [DRT electronic filing requirements](https://www.guamtax.com/help/help_w2w3.html).
9. **Reconcile** W-2GU box 2 totals against Guam withholding reported on the W-1 returns. Reconcile federal wages and taxes to the Forms 941 using the totals from all applicable wage statements, including Forms W-2 for employees subject to US withholding. Include social security tips and account for applicable adjustments and explain any differences.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Employee works in Guam, lives in Guam | Guam withholding; W-2GU |
| MSRRA civilian spouse meeting the federal residence and accompanying-spouse conditions | US withholding and Form W-2. Exclude from W-1. Check state and local withholding. |
| Employee of a mainland employer temporarily in Guam | Check the employer’s obligations in both jurisdictions. Establish the source of the wages and any de minimis exclusion in `gu-individual-income-tax`. |
| Guam employer with no FICA-exempt workers | Apply the annual wage base to social security wages. Medicare tax has no wage base limit. |
| Employer asks about Guam unemployment insurance | No FUTA in Guam; no Guam unemployment contribution was found on the DRT calendar (not confirmed) |
| EIC notice to employees | Not required for employees in Guam (Pub. 15, section 10) |
| Philippine national or a visa label offered as the 3121(b)(18) exception | Hold until the actual conditions are shown: resident of the Philippines, temporarily in Guam, admitted under INA 101(a)(15)(H)(ii) |
| Government of Guam employee treated as FICA-exempt under the opening words of 3121(b)(7) | Hold the (7)(B) and (D) branches, the retirement-system facts and 3121(u) |
| Guam residence or the Puerto Rico citizen sentence offered as proof that every worker is a US citizen and covered | Hold; establish the actual service, status and coverage |
| Medicare, or all FICA, capped at the OASDI wage base | Wrong: the 3121(a)(1) ceiling applies only to OASDI; Medicare has no limit (`us-form-941-940-payroll`) |
| Two pay components each capped separately | Aggregate per employee, per employer, per calendar year, then apply the OASDI base once |
| Employee asks to stop Additional Medicare at the joint-return threshold, or the employer matches it | No: the employer withholds on wages it pays over the threshold from the crossing payment, regardless of filing status; there is no employer match (`us-form-941-940-payroll`) |
| Territorial income tax rules or Guam taxable income used as the FICA base | Hold: FICA is federal and its base is covered remuneration |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| MSRRA claim | Apply Guam withholding to covered wages until the employer establishes the applicable exemption. |
| Form W-4 | Keep using any valid form already on file. When no valid form is on file for a 2026 hire, use Single or Married filing separately and leave Steps 2–4 blank. |
| GuamTax.com e-file registration | Commercial employers filing for themselves register online. Payroll processors and Guam government filers use the respective DRT registration forms. |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Guam tax withheld but sent to the IRS on Form 941 | Wrong government; the DRT will assess |
| Form W-2 issued for Guam withholding | Check whether W-2GU and corrections are required. |
| FUTA paid for Guam employees | Not owed; claim it back |
| W-2GU box 2 total differs from the W-1 returns | Compare the W-1 returns and wage statements with payroll records. Correct the source of the discrepancy. |

## Worked cases

**Case 1, quarterly W-1 and year-end reconciliation.** A Guam restaurant withheld Guam income tax of USD 3,200, USD 3,450, USD 3,100 and USD 3,900 in the four quarters of 2026 (worked out from the employees' Forms W-4 with Pub. 15-T). Each amount goes on that quarter's W-1, the fourth by **1 February 2027** because 31 January is a Sunday. Quarterly withholding exceeds USD 2,500 in each quarter, so check the deposits separately from the W-1 filings. The W-1 amounts total USD 13,650 and the W-2GUs show USD 13,600. Reconcile the USD 50 difference to payroll records before filing. The totals alone cannot identify the document or employee affected.

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

**Case 2, a decision: Guam or US withholding for an MSRRA spouse.** A Guam clinic has three employees. Two live in Guam; Guam tax withheld in the quarter is USD 1,800 and USD 1,350. The third is the civilian spouse of a sailor stationed in Guam and is solely in Guam to accompany the servicemember under military orders. Assume she qualifies to retain Texas tax residence and the verified US withholding on her wages is USD 900. Report this withholding on Form 941 and Form W-2. The W-1 shows USD 3,150. If she does not qualify and the separately computed Guam withholding for her wages is also USD 900, the W-1 would show USD 4,050.

```oa-check
name: MSRRA spouse left off the Guam W-1 (2026 quarter)
inputs:
  guam_emp_a: 1800
  guam_emp_b: 1350
  msrra_emp: 900
  guam_tax_without_exemption: 900
steps:
  - w1_guam_tax: guam_emp_a + guam_emp_b
  - us_income_tax_on_941: msrra_emp
  - w1_if_no_msrra: guam_emp_a + guam_emp_b + guam_tax_without_exemption
expected:
  w1_guam_tax: 3150
  us_income_tax_on_941: 900
  w1_if_no_msrra: 4050
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GU-PR-FED | Federal agency employer, or federal pensions to Guam residents | Refer: Pub. 15, section 17 certification |
| R-GU-PR-DEPOSIT | Guam deposits at exactly USD 2,500 for the quarter or an unclear deposit schedule | Confirm with the DRT. See Filing and payment. |
| R-GU-PR-H2 | H-2 or other nonimmigrant workers and their FICA status | Refer: Pub. 15 special rules |
| R-GU-PR-PENALTY | Late W-1, late W-2GU penalties | Refer: mirror code penalties applied by DRT |

## Filing and payment

File W-1 by **30 April and 31 July 2026** for Q1 and Q2. The ordinary Q3 date, 31 October, falls on a Saturday. Confirm the next working day with the DRT, taking local legal holidays into account. The Q4 W-1 is due **1 February 2027**. SWICA statutory dates before any applicable extension are **30 April, 30 July and 30 October 2026 and 30 January 2027**. Confirm any SWICA extension separately.

The [DRT Form 500 instructions](https://www.govguamdocs.com/revtax/docs/F500winstructions_201102.pdf) require deposits when Guam wage withholding **exceeds USD 2,500** for the quarter and allow payment with a timely W-1 when it is **below USD 2,500**. Confirm the treatment of exactly USD 2,500 with the DRT. The instructions describe monthly deposits by the **15th of the next month** for new employers subject to exceptions and for employers with **USD 50,000 or less** in lookback tax, and semiweekly deposits above **USD 50,000**. See the instructions for the applicable payment days.

File Form 941 with the IRS on its own quarterly timetable and make federal deposits separately. Furnish W-2GU to employees, file Copy A with W-3SS with the SSA and send Copy 1 with W-3SS to the DRT by **1 February 2027**.

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
| DRT tax calendar. Read for W-1, W-2GU and the weekend and legal holiday rule. Check SWICA separately against 11 GCA 41104. | https://www.guamtax.com/info/calendar.html | 2026-11-14 |
| DRT GuamTax.com home page and SWICA and W-2/W-3 e-filing registration form. Read for the e-services (E-File W-1, SWICA, W-3/W-2GU). | https://www.guamtax.com/ | 2026-11-14 |
| IRC section 3121 (House, through Public Law 119-124). Read for (a)(1), (b)(7)(B) and (D), (b)(18), (e)(1) and (e)(2) including the Puerto Rico citizen sentence, and (u). | https://uscode.house.gov/us/usc/119-124/t26/s3121/ | 2026-11-14 |

| Guam Form 500 instructions and current W-1 help. DRT deposit requirements and W-1 reconciliation. | https://www.govguamdocs.com/revtax/docs/F500winstructions_201102.pdf and https://www.guamtax.com/help/help_w1.html | 2026-11-22 |
| 11 GCA 41104. SWICA reporting deadline. | https://www.guamcourts.org/CompilerofLaws/GCA/11gca/11gc041.PDF | 2026-11-22 |
| 5 GCA chapter 34, article 3. New hire reporting. | https://www.guamcourts.org/compileroflaws/GCA/05gca/5gc034.pdf | 2026-11-22 |

Confirm with the DRT whether it uses the 2026 Pub. 15-T tables without changes, any Guam employer unemployment contribution and any generally applicable SWICA weekend extension.

Not yet confirmed: DRT adoption of every federal 2026 withholding worksheet without adjustment, deposit treatment at exactly USD 2,500 and local holiday treatment of the separate SWICA report. Confirm the due dates with DRT for the affected period.
