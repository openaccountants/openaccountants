---
name: tanzania-social-contributions
description: >
  Compute and reconcile 2026 Mainland NSSF, PSSSF, SDL, WCF and confirmed HESLB payroll deductions; separate legal bases, PAYE relief, health-insurance holds and remittances.
jurisdiction: TZ
category: payroll
type: computation
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
version: 1.0
---

# Tanzania Mainland social and payroll contributions v1.0

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### Quick reference

Compute and reconcile 2026 Mainland employee pension/payroll contributions, employer levies and related PAYE. Different legal bases apply to NSSF, PSSSF, SDL, WCF, PAYE, HESLB and health insurance. This version has not been reviewed by an accountant. For ordinary employment-tax benefits use [payroll](tanzania-payroll.md); annual business/presumptive income and corporate incentives belong to [tax optimization](tanzania-tax-optimization.md), not this computation. TRA publishes the same monthly PAYE bands for Mainland and Zanzibar. Zanzibar social/SDL/WCF levies need separate authority evidence; the PAYE fact does not extend Mainland levies.

## Ask the client first

- Actual payroll month, pay frequency, Mainland/Zanzibar location, residence and primary/secondary employment.
- Cash, benefits and underlying statutory wage/salary base for each obligation.
- Fund/member registration, public/private/specified corporation status and agreed employee/employer split.
- Monthly headcount, SDL exemption evidence, subsector and actual wage category.
- Board-confirmed HESLB borrower/bill, health scheme/current membership and rates.
- Registers, returns, member schedules, bank receipts/control numbers and official arrears/refund/waiver allocations.

## Rates, bands and thresholds

| Item | Figure / rule and complete conditions | Official source |
|---|---|---|
| NSSF covered Mainland employee | 20% of statutory wages total; employee at most 10%, employer balance. Documented 10/10, employee 5/employer 15, or employer 20/employee 0 arrangements. No automatic exemption just because the employee is foreign. | [Rates of Contributions; NSSF ss 6,12-13](https://www.nssf.go.tz/pages/payment-of-contributions) |
| NSSF wages and coverage | s 3 contractual money wages include living allowance and pay in lieu of notice. ss 6-7 cover Mainland private, self-employed, foreign/international categories and Board-approved religious ministers. Employee scheme computation does not establish a self-employed contribution arrangement. | [ss 3,6-7](https://www.nssf.go.tz/uploads/publications/en-1771921274-NSSF%20ACT%20CAP%2050%20RE.%202023.pdf) |
| PSSSF default | 20% of s 3 salary: employee 5%/employer 15% (in words on the page). s 3 excludes bonus, commission, cost-of-living allowance, overtime, directors fees and other additional emoluments. This is not the PAYE gross base. | [ss 3,18](https://elibrary.osg.go.tz/bitstreams/cf923cdc-b36a-4a5b-88f8-21818597c3a2/download) |
| PSSSF higher contributions/coverage | Actual higher employee/employer contributions allowed; employee contribution at most 50% of total (in words on the page). Applies to Mainland public service/former schemes/specified corporations, including government ownership at least 30% or designation. Do not select a fund from a bank description. | [ss 2-5,18(6)](https://elibrary.osg.go.tz/bitstreams/cf923cdc-b36a-4a5b-88f8-21818597c3a2/download) |
| SDL | 3.5% employer-only on total monthly cash emoluments for at least 10 employees, unless s 19 exemption. Includes permanent, part-time, secondary and casual staff; irregular periods allocated monthly. | [Chargeability, Who is liable, Applicable rates](https://www.tra.go.tz/page/skills-development-levy-sdl) |
| WCF | 0.5% employer-only for formal Mainland private and public sectors; agency base basic salary plus fixed allowances. Private 0.6% is historical, replaced from 1 July 2022 by GN478F. Variable-pay inclusions beyond this guidance remain unconfirmed. | [UCHANGIAJI(a)-(f)and rate/base FAQ; GN478F](https://www.wcf.go.tz/pages/contribution); [GN478F regs1-2, historical private-rate amendment](https://www.wcf.go.tz/uploads/documents/sw-1666602227-sw1658489842-GN%20No.%20478F%20Tariff%20Regulation.pdf) |
| HESLB covered borrower | After Board confirmation/billing, deduct at least 15% of basic salary, wages or remuneration as applicable, monthly (minimum and bases in words on the scanned law page). Agency guidance uses billed 15% of basic salary. Do not apply 15% to all staff or to total outstanding loan balance. | [Amendment s 19; substituted principal s 20(1)(b)](https://www.heslb.go.tz/images/storage/downloads/1761132137_heslb-act-amendment-2016.pdf) |
| HESLB employer reporting/remittance | Notify Board of employed degree/diploma graduates within 28 days from employment; upon confirmed beneficiary status deduct under principal 20(1)(b), report beneficiary status/rank and name/address/occupation/salary changes under 20(1)(d), and remit within 15 days after month-end under 20(2). Numbers in words on the scanned law; agency before-15th guidance does not override statutory within-15-days. | [Amendment s 19; substituted principal s 20(1)(a),(b),(d),(2)](https://www.heslb.go.tz/images/storage/downloads/1761132137_heslb-act-amendment-2016.pdf) |
| HESLB priority and arrears | Statutory loan deduction has priority over nonstatutory salary deductions. Replacement s 21 imposes 10% of amount due for repayment for each month not remitted (in words on law page), not 10% of the entire loan by default; obtain Board schedule. | [Amendment s 19; substituted principal ss 20-21](https://www.heslb.go.tz/images/storage/downloads/1761132137_heslb-act-amendment-2016.pdf) |
| Resident PAYE | Monthly taxable income after eligible approved-retirement relief: up to 270,000 nil; over 270,000-520,000 8% excess; over 520,000-760,000 20,000+20% excess; over 760,000-1,000,000 68,000+25% excess; above 1,000,000 128,000+30% excess. All TZS. | [Mainland/Zanzibar monthly tables](https://www.tra.go.tz/page/income-tax-for-individuals) |
| Approved pension relief | Lower of actual eligible contribution and statutory fund amount. Employer contribution only where included in employment income. Do not reduce taxable pay twice, or treat voluntary/health/loan deductions as automatically eligible pension relief. | [How contributions made to approved retirement funds are treated](https://www.tra.go.tz/page/pay-as-you-earn) |
| Nonresident employee PAYE | 15% gross Tanzania-source employment pay, final for that employment. Pension coverage is separate; foreign citizenship alone is not an NSSF exemption. | [Nonresident employees](https://www.tra.go.tz/page/pay-as-you-earn) |
| Combined on-cost illustration | 14% (derived:10% NSSF+3.5% SDL+0.5% WCF) only for proved SDL liability, employee 10/employer 10 split and identical bases. Below 10 staff, no SDL, that illustration becomes 10.5%. Not a universal employer-cost percentage. | [Rates of Contributions; VETA 14; WCF guidance](https://www.nssf.go.tz/pages/payment-of-contributions); [VETA14](https://elibrary.osg.go.tz/bitstreams/46a41d49-ae99-478c-8188-310fdc970d1b/download); [Current WCF rate/base](https://www.wcf.go.tz/pages/contribution) |
| Private-sector wages | GN605A/2025 from 1 January 2026: choose actual category and pay-period rate. Full monthly table is in payroll and complete rates in official Second Schedule. Other-sector TZS 175,000 and other-domestic TZS 80,000 are specific monthly categories, not universal floors; the old claimed average is unconfirmed under Sources. | [paras 1-7 and Schedules 1-2](https://www.kazi.go.tz/uploads/documents/en-1760702541-GN%20605A-THE%20LABOUR%20INSTITUTIONS%20%28MINIMUM%20WAGE%20FOR%20PRIVATE%20SECTOR%29%20ORDER%2C%202025%20%285%29.pdf) |

## The method, step by step

1. Establish Mainland/Zanzibar location, residence, employment month, actual pension scheme and member registration. Unknown location/sector is a hold, not a private/Mainland default.
2. Reconcile cash, benefits and the legally different NSSF wages/PSSSF salary/WCF basic-plus-fixed/SDL cash/PAYE taxable bases. Check headcount, SDL exemption, loan Board status and health scheme.
3. Compute pension using actual split; apply only proved approved-retirement relief once for resident PAYE. Use payroll skill for benefits and resident monthly computation; confirmed nonresident 15% gross is a separate rule. Keep employer-only charges out of employee deductions.
4. Calculate net cash, employer cost and each remittance; match payment, schedule and member allocation. A salary or fund bank line is insufficient to reconstruct gross or taxable pay.
5. Compare official due dates and receipts. Separate principal, arrears, penalty, interest and refunds. Obtain official statements and actual remission/waiver decisions before any arrears bill.

### SDL exemptions

VETA s 19 covers government/subvention institutions (2026 wording), diplomatic missions, UN, foreign aid/technical assistance, qualifying solely religious/public-health staff, qualified resident public-character charities, registered educational institutions, local authorities, qualifying Tanzania Employment Service Agency interns, sole farming workers excluding farm management/processing, and water/sanitation authority casual project labour. Charity registration/functions and Commissioner due diligence/ruling evidence must be established; Ministerial public-interest relief needs the actual Gazette order. Exempt employers need not submit SDL returns under s 16. All conditions remain beside any exemption; headcount alone does not establish taxable status. [VETA 14-21](https://elibrary.osg.go.tz/bitstreams/46a41d49-ae99-478c-8188-310fdc970d1b/download),[FA 2026 s 98](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf).

VETA 19(2) specifically requires a resident public-character entity registered as such, functioning solely for relief of public poverty/distress AND provision of education or public health, with the Commissioner General satisfied after due diligence that its business is for public good. TRA SDL guidance uses a broader ITA-style charity definition and current ruling language; do not substitute it for the distinct VETA wording. Establish the statutory conditions and actual evidence, or hold relief. [VETA 19(2)](https://elibrary.osg.go.tz/bitstreams/46a41d49-ae99-478c-8188-310fdc970d1b/download), [TRA SDL guidance](https://www.tra.go.tz/page/skills-development-levy-sdl).

| Item | Figure / rule and complete conditions | Official source |
|---|---|---|
| NSSF registration | Employer within 1 month after becoming a contributing employer; covered employees without delay (number in words on page). Keep old membership, avoid duplicate registration and allocate each contribution to the member. | [s 11](https://www.nssf.go.tz/uploads/publications/en-1771921274-NSSF%20ACT%20CAP%2050%20RE.%202023.pdf) |
| NSSF payment and support | Within 1 month after contribution month-end. Send complete NSSF/CON.05 to relevant office immediately after GePG payment; retain bank/control number and member earnings schedule. A consolidated multi-region payer needs branch allocation. | [Payment/support and location paragraphs; Act 14](https://www.nssf.go.tz/pages/payment-of-contributions) |
| Employee recovery of missed NSSF | s 13 permits current deduction or recovery within 6 months, by at least 4 approximately equal instalments unless employee agrees fewer or lump sum (numbers in words on page). Do not deduct employer share from wages or sweep arrears without checking conditions. | [s 13](https://www.nssf.go.tz/uploads/publications/en-1771921274-NSSF%20ACT%20CAP%2050%20RE.%202023.pdf) |
| NSSF penalty | 5% unpaid contribution per month or part (in words on page); do not presume compound-on-penalty computation. Board remission and exact principal/period allocation require actual decision/statement. | [Penalties; Act 14](https://www.nssf.go.tz/pages/payment-of-contributions) |
| PSSSF timing and surcharge | s 18 deems remitted on last day of month salary paid. s 19 initial 1.5% unremitted contribution; after 30 days, additional 1.5% of aggregate remaining unpaid per month or part (all in words on page). Waiver requires Board with Minister approval; do not substitute NSSF 5% penalty. | [ss 18-20](https://elibrary.osg.go.tz/bitstreams/cf923cdc-b36a-4a5b-88f8-21818597c3a2/download) |
| PAYE / SDL | TRA 7th following month; SDL ITX300.01.E credit slip and monthly return through IDRAS; half-year certificate must tally monthly returns per agency guidance. Exact live half-year form/deadline is held. PAYE certificate/return details in payroll. | [Employer obligation](https://www.tra.go.tz/page/skills-development-levy-sdl) |
| WCF payment | Within contribution month or following month. Agency FAQ permits 3-month,6-month or annual only with actual DG consent; obtain it. Portal/control number does not replace salary-base/member schedule. | [UCHANGIAJI; frequency FAQ](https://www.wcf.go.tz/pages/contribution) |
| TRA s 89 penalty | For failure to file return or pay tax on due date, per month/part, higher of 2.5% (in words on the page) tax assessable less paid at period start or 5 currency points individual/15 corporate. Separate provisional/final return failures. | [s 89](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf) |
| Currency point / interest | Current point TZS 20,000 under FA 2024 s 97, so minima TZS 100,000 individual/TZS 300,000 corporate (derived). s 87 late-payment interest compounds monthly at prevailing BoT discount; no fixed/current percentage supplied. | [s 97; TAA definition/s 87](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf); [Statutory rate definition and s 87](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf) |
| WCF late amount | Current agency guidance says 2% of delayed amount. Principal 2016 reg 13/2017 tariff not recovered for full frequency/base mechanics; no definitive per-month/compound bill from this statement. | [UCHANGIAJI(e); GN668 amendment](https://www.wcf.go.tz/pages/contribution) |

### Health insurance: supported scope and unresolved current rate

Health insurance is separate from NSSF/PSSSF. The recovered NHIF R.E.2023 Act ss 2/9/11 covers public servants and formal-private categories; s 9 states employer 3% and employee 3%, with special Treasury 6.25% treatment for police, prisons, immigration, fire/rescue and a 1 month payment provision (figures in words on the page). This older consolidation is NOT proof of the final 2026 deduction or deadline for every employee. Its apparent 2025 amendment download is expressly a BILL, not an enacted amendment. [Official Special Bill Supplement,22 January 2025, cover/notice only](https://elibrary.osg.go.tz/bitstreams/a551ff1e-24a3-408a-a121-5ffbf228bfca/download). These historical figures are preserved here as a source boundary; do not apply them automatically.

The enacted Universal Health Insurance Act s 3 distinguishes public salary (excluding additional payments/benefits/allowances) from private salary (including statutory entitlements paid as salary). s 22 requires public/formal-private employer registration within 30 days from contract commencement; s 23 makes the actual public-scheme law or approved private-scheme premium relevant. GN 700 A commenced specified provisions from 16 August 2024 but excluded ss 5,37,43 and 58-65; do not infer universal mandatory coverage from the title alone or infer current non coverage from that original exception. GN 809 reg 23 describes employer scheme choice with employee participation and remittance by 15th of following month from registration; this is not a basis to silently retain the older one-month assumption. Read numbers expressed as words on these Swahili pages. [NHIF Act](https://elibrary.osg.go.tz/bitstreams/c135c899-14da-4a3f-b832-563eb52278f1/download), [UHI Act](https://www.nhif.or.tz/uploads/documents/sw-1736978659-sw1729595633-Sheria%20ya%20Bima%20ya%20Afya%20kwa%20Wote.pdf), [GN 700 A](https://www.nhif.or.tz/uploads/documents/sw-1744266564-BIMA-GN%20NO.%20700A%20OF%202024%20-%20TANGAZO-KUANZA%20KUTUMIKA.pdf), [GN 809 reg 23](https://www.nhif.or.tz/uploads/documents/sw-1744266616-BIMA-Kanuni%20ya%20Bima%20ya%20Afya-2024.pdf).

For final payroll, hold the health line until the employer's actual scheme, covered status, current governing rate/base, operative later amendments/commencement and remittance rules are established. Do not describe unknown health contribution as zero, apply 6% to all private staff, or treat insurance deductions as pension relief.

### Statement classification and Kiswahili terminology

Descriptions are search clues. Confirm counterparty, debit/credit direction, control number, tax type, period and receipt before posting. `TRA`, `KODI` or `WITHHOLDING TAX` alone does not prove PAYE; `PENSION` alone does not prove NSSF. Mixed tax payments need the official allocation.

| Original pattern family | Provisional treatment, subject to documents |
|---|---|
| `SALARY`, `MSHAHARA`, `MISHAHARA`, `PAYROLL`, `NET PAY`, `MALIPO YA MSHAHARA`, `WAGE`, `TRANSF.* [employer]` | Salary candidate. A bank credit is usually net cash and cannot establish taxable gross; distinguish transfers and reimbursements. |
| `NET WAGES`, `MALIPO YA MISHAHARA`, `SALARY RUN`, `DISBURSEMENT` | Employer wage-disbursement candidate, not necessarily the gross wage expense. |
| `TRA`, `TANZANIA REVENUE AUTHORITY`, `PAYE`, `P.A.Y.E`, `ITX 300`, `ITX300.01.E`, `KODI`, `WITHHOLDING TAX` | Tax/remittance candidate; separate employee PAYE from SDL/other taxes using receipt/schedule. |
| `SDL`, `SKILLS DEVELOPMENT LEVY`, `TOZO YA UJUZI`, `TOZO YA MAENDELEO YA UJUZI` | SDL candidate, employer expense/liability settlement if established. |
| `NSSF`, `MICHANGO NSSF`, `NATIONAL SOCIAL SECURITY FUND`, `CON.5`, `NSSF/CON.05`, `PENSION`, `MICHANGO YA PENSHENI` | Pension candidate; split employer expense and employee withheld liability, distinguish arrears. |
| `PSSSF`, `PUBLIC SERVICE SOCIAL SECURITY` | Public-service pension candidate; establish actual fund and member allocation. |
| `WCF`, `FIDIA YA WAFANYAKAZI`, `MFUKO WA FIDIA KWA WAFANYAKAZI`, `WORKERS COMPENSATION` | WCF candidate, employer obligation, never automatic employee deduction. |
| `NSSF REFUND`, `MAREJESHO NSSF`, `TRA REFUND`, `PAYE REFUND` | Refund/adjustment candidate; reconcile original principal, employee entitlement and any interest rather than classifying all credits as tax-free income. |
| `NSSF PENSION`, `PSSSF PENSION`, `PENSHENI` on a credit | Benefit receipt candidate, not a contribution remittance; benefit tax treatment is a separate inquiry. |

CRDB, NMB and NBC statement labels can use these English/Kiswahili terms. `Mkazi` means resident; `Asiye mkazi` nonresident; `Malipo halisi` net pay. Timing near tax due dates is a clue, not evidence of the liability period. Statutory payroll remittances and wages are not invoices for taxable business purchases; do not manufacture input VAT. Employee deductions settle liabilities, while employer contributions/levies are separately classified expenses subject to deductibility rules, not automatic credits. Refunds may reverse prior postings.


### Workpaper and bank-only onboarding

Record Client/Employer, Employee name, Tax year (calendar 1 January-31 December), Prepared date, employer/TIN, member identifier, month, location, residence, fund and split; cash/benefits; each contribution base; approved-retirement relief; PAYE base/tax; employee/employer contributions; SDL headcount/exemption; WCF base; confirmed HESLB basic/bill; health pending/actual scheme; net cash; employer cost; returns/control numbers/receipts; arrears statements; source/version and unresolved facts. Missing facts remain blank/unresolved, not zero or guessed. Payroll workpaper has the resident tax formula; do not apply it to the bank credit or apply pension relief twice.

CRDB/NMB/NBC labels are clues. A gross-base hypothesis from NSSF total/20% or SDL/3.5% requires proof of period, principal-only amount, actual rate/base and scheme. Never infer the fund exclusively from a label or assume all statutory transfers are debits: refunds/reversals can be credits. Suggested prior 3 months of registers/receipts is a workflow choice, not law. A mixed TRA debit must be split by official allocation; employee tax/pension withheld settles liabilities, employer pension/levies are separately classified costs. These remittances are not taxable-supply purchases and do not generate input VAT. Actual business deductibility is a separate issue, not a promise from bank classification.

## Worked cases

These are hypothetical TZS amounts; all results are derived. Resident cases assume regular Mainland cash wages, proved eligible NSSF employee 10%/employer 10%, same pension/cash base, no other benefits or deductions. Health/HESLB are excluded unless expressly specified, not deemed inapplicable to an actual employee.

| Retained scenario | Gross | Employee NSSF | PAYE base | PAYE | Cash net |
|---|---:|---:|---:|---:|---:|
| Mid-bracket |800,000|80,000|720,000|60,000|660,000|
| Top band |1,500,000|150,000|1,350,000|233,000|1,117,000|
| Low earner |290,000|29,000|261,000|0|261,000|
| Lower-middle |600,000|60,000|540,000|24,000|516,000|
| Upper-middle |1,000,000|100,000|900,000|103,000|797,000|

The 800,000 case's SDL-liable employer adds NSSF 80,000+SDL 28,000+WCF 4,000=112,000, total cost 912,000; the old WCF 4,800 used obsolete 0.6%. The 290,000 case is NOT automatically below a 358,322 minimum; sector/subsector determines compliance. Confirmed nonresident gross 4,000,000 yields PAYE 600,000 final for that employment, with pension coverage tested separately. A 30 staff employer with proved identical cash/SDL/WCF bases 50,000,000 owes SDL 1,750,000 and WCF 250,000, not the old 300,000. Public-service PSSSF on proved s 3 salary 1,200,000 gives employee 60,000/employer 180,000/total 240,000; do not assume additional bonuses belong to that base.

```oa-check
name: Approved pension relief and corrected WCF separate net pay from cost
inputs:
  regular_cash_wage: 800000
steps:
  employee_nssf: regular_cash_wage * 0.10
  employer_nssf: regular_cash_wage * 0.10
  taxable_pay: regular_cash_wage - employee_nssf
  paye: clamp(taxable_pay - 270000, 0, 250000) * 0.08 + clamp(taxable_pay - 520000, 0, 240000) * 0.20 + clamp(taxable_pay - 760000, 0, 240000) * 0.25 + max(taxable_pay - 1000000, 0) * 0.30
  net_cash: regular_cash_wage - employee_nssf - paye
  sdl: regular_cash_wage * 0.035
  wcf: regular_cash_wage * 0.005
  employer_cost: regular_cash_wage + employer_nssf + sdl + wcf
expected:
  taxable_pay: 720000
  paye: 60000
  net_cash: 660000
  wcf: 4000
  employer_cost: 912000
```

```oa-check
name: Public pension base excludes separately proved overtime
inputs:
  psssf_salary: 1200000
  excluded_overtime: 200000
steps:
  employee_psssf: psssf_salary * 0.05
  employer_psssf: psssf_salary * 0.15
  total_psssf: employee_psssf + employer_psssf
  wrong_total_if_overtime_included: (psssf_salary + excluded_overtime) * 0.20
  overstatement: wrong_total_if_overtime_included - total_psssf
expected:
  employee_psssf: 60000
  employer_psssf: 180000
  total_psssf: 240000
  overstatement: 40000
```

For a separately confirmed, billed HESLB borrower with hypothetical basic pay 1,000,000 and actual 15% deduction, deduction 150,000 reduces cash net, not taxable pay as pension relief. Loan balance, insurance, pension base and PAYE base must each be established separately. The 15% figure is a statutory minimum and current agency billed rate, not permission to ignore a higher lawful Board arrangement.

Retained statement cases: `07.02.2026 ; TANZANIA REVENUE AUTHORITY ; DEBIT ; ITX 300.01.E JAN PAYE+SDL ; -1,250,000 ; TZS` is a mixed-payment candidate; obtain the official PAYE/SDL split rather than expense all 1,250,000 or claim input VAT. `20.03.2026 ; NATIONAL SOCIAL SECURITY FUND ; DEBIT ; ARREARS ; -3,500,000 ; TZS` requires the member/contribution/penalty/period statement; do not divide the whole debit by 20% or multiply it by 5% without that allocation. These workflow cases preserve the original scenarios without treating strings as legal proof.

## When to refuse or refer

Hold where residence, location, payroll period, gross, legally different bases, scheme/split, staff count, exemption, loan status or health scheme is unresolved. Do not assume private/Mainland/resident status, NSSF 10/10, SDL off or historical WCF 0.6% as a conservative default. Refuse employer-only levies deducted from employees, illegal omissions, automatic pension relief for any deduction, and a universal wage average as floor. Refer arrears, recovery/waiver, nonmonthly PAYE, unrecovered wage caps/variable WCF base, self-employment contributions, Zanzibar obligations, and unverified health implementation before final filing/payment. Foreign workers are not automatically pension-exempt; obtain any actual lawful exception. Estimates require qualified review.

## Disclaimer

This contribution reconciliation template does not file a return, settle a fund balance or establish an individual's benefit entitlement. Use actual records and current official procedures, and obtain qualified local review before relying on the calculation.


## Sources

| Source and actual reading scope | Official URL | Read on |
|---|---|---|
| National Social Security Fund Act, Cap. 50 R.E. 2023: Read for definitions employee/wages; ss 6-17 and complete First Schedule | https://www.nssf.go.tz/uploads/publications/en-1771921274-NSSF%20ACT%20CAP%2050%20RE.%202023.pdf | 2026-11-15 |
| NSSF: Payment of Contributions: Read for all operative payment, schedule, branch, split and penalty paragraphs | https://www.nssf.go.tz/pages/payment-of-contributions | 2026-11-15 |
| Public Service Social Security Fund Act, Cap. 371, R.E. 2023 A.S. 2025: Read for ss 2-5 coverage/definitions; ss 16-23 membership, contributions, remittance, recovery and surcharge | https://elibrary.osg.go.tz/bitstreams/cf923cdc-b36a-4a5b-88f8-21818597c3a2/download | 2026-11-15 |
| Vocational Education and Training Act, Cap. 82, R.E. 2023 A.S. 2025: Read for whole Part IV ss 14-21; neighbors 13/22-23; all s 19 exemptions and charity conditions | https://elibrary.osg.go.tz/bitstreams/46a41d49-ae99-478c-8188-310fdc970d1b/download | 2026-11-15 |
| TRA: Skills Development Levy: Read for all charge/base/headcount/rate/payment/return/half-year certificate/exemption guidance | https://www.tra.go.tz/page/skills-development-levy-sdl | 2026-11-15 |
| Finance Act 2026, Act No. 2: Read for commencement ss 1-2; Part IX; administration ss 70-80; VAT/SDL ss 88-98 | https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf | 2026-11-15 |
| WCF: Contributions (Swahili): Read for UCHANGIAJI(a)-(f), plus registration, employer-only, base, rate, portal and frequency FAQs; not all benefit FAQs | https://www.wcf.go.tz/pages/contribution | 2026-11-15 |
| WCF tariff amendment 2022, GN 478F: Read for whole one-page GN478F/2022: commencement and private-rate amendment | https://www.wcf.go.tz/uploads/documents/sw-1666602227-sw1658489842-GN%20No.%20478F%20Tariff%20Regulation.pdf | 2026-11-15 |
| Written Laws (Miscellaneous Amendments) (No. 3) Act 2016, Part IV, scanned excerpt: Read for all 7 scanned pages visually read: Part IV ss 16-20 including substituted 20-21; full Act commencement not in this excerpt; current HESLB corroborates | https://www.heslb.go.tz/images/storage/downloads/1761132137_heslb-act-amendment-2016.pdf | 2026-11-15 |
| HESLB: Obligations: Read for all operative employer/beneficiary obligation guidance | https://www.heslb.go.tz/loanrepayment/obligation | 2026-11-15 |
| HESLB: About Loan Repayment: Read for employer steps 1-4, graduate notification, billed basic-salary deduction and payment proof | https://www.heslb.go.tz/loanrepayment/about-loan-repayment | 2026-11-15 |
| TRA: Pay As You Earn: Read for all operative income, exclusions, benefits, approved-retirement relief, resident/nonresident/director, multiple employment and records guidance | https://www.tra.go.tz/page/pay-as-you-earn | 2026-11-15 |
| TRA: Income Tax for Individuals: Read for Mainland/Zanzibar monthly tax tables, annual threshold and individual filing guidance | https://www.tra.go.tz/page/income-tax-for-individuals | 2026-11-15 |
| Labour Institutions (Minimum Wage for Private Sector) Order 2025, GN 605A: Read for whole 9-page Order, paras 1-7 and all rows of both Schedules | https://www.kazi.go.tz/uploads/documents/en-1760702541-GN%20605A-THE%20LABOUR%20INSTITUTIONS%20%28MINIMUM%20WAGE%20FOR%20PRIVATE%20SECTOR%29%20ORDER%2C%202025%20%285%29.pdf | 2026-11-15 |
| Tax Administration Act, Cap. 438 R.E. 2023: Read for statutory-rate definition; ss 87-89 and 90 opening | https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf | 2026-11-15 |
| Finance Act 2024, Act No. 6: Read for income amendments 32-43 and s 97 currency point amendment | https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf | 2026-11-15 |
| National Health Insurance Fund Act, Cap. 395 R.E.2023: Read for ss 2-3 coverage/definitions, ss 8-11 contributions/coverage and 15 membership; read as older consolidation, not proof of later amendment | https://elibrary.osg.go.tz/bitstreams/c135c899-14da-4a3f-b832-563eb52278f1/download | 2026-11-15 |
| Universal Health Insurance Act 2023, official Swahili text: Read for s 3 salary and sector definitions; ss 22-24 registration, contribution scheme choice and indigent coverage with neighbors | https://www.nhif.or.tz/uploads/documents/sw-1736978659-sw1729595633-Sheria%20ya%20Bima%20ya%20Afya%20kwa%20Wote.pdf | 2026-11-15 |
| Universal Health Insurance Regulations 2024, GN809, Swahili: Read for regs 22-25, especially 23 employer scheme choice/remittance with neighboring waiting/cessation rules | https://www.nhif.or.tz/uploads/documents/sw-1744266616-BIMA-Kanuni%20ya%20Bima%20ya%20Afya-2024.pdf | 2026-11-15 |
| GN700A/2024, commencement notice, Swahili: Read for whole notice, paras 1-2, all commenced and excluded provisions | https://www.nhif.or.tz/uploads/documents/sw-1744266564-BIMA-GN%20NO.%20700A%20OF%202024%20-%20TANGAZO-KUANZA%20KUTUMIKA.pdf | 2026-11-15 |
| National Health Insurance Fund amendment proposals, Special Bill Supplement: Read for cover and notice of Special Bill Supplement 22 January 2025 only; not enacted provisions or current rate authority | https://elibrary.osg.go.tz/bitstreams/a551ff1e-24a3-408a-a121-5ffbf228bfca/download | 2026-11-15 |

Not yet confirmed: The old claimed average TZS 358,322 is not independently confirmed by GN605A and is not an employee minimum.  Final current NHIF rate, base, covered status and remittance rules after any enacted 2025 amendment or later commencement: the retrieved 2025 text is a BILL. Historical 3% plus 3%, special 6.25% and one-month timing are not automatic 2026 instructions. WCF principal 2016 regulations/2017 tariff for variable pay and full late-charge frequency or compounding; any later NSSF cap/floor instrument; live PAYE/SDL half-year form and deadline; dated BoT discount rate and official arrears allocations; nonmonthly/terminal PAYE; Zanzibar SDL and social levies. The old 33.4% average wage increase and 45-hour-week basis remain unconfirmed; use the actual Gazette payment-period rates. Old presumptive 100 million/3.5% and corporate 30%/listing 25% context does not establish payroll liability; use current income/incentive sources.
