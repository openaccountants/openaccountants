---
name: ga-payroll
description: Tier 2 Georgia content skill for employer payroll compliance covering tax year 2025. Includes the GA PIT 5.19% flat (reduced from 5.39% by HB 111 signed April 15, 2025, retroactive to January 1, 2025; phasing down toward 4.99% by 2030 contingent on revenue triggers), G-4 state W-4 equivalent, G-7 quarterly withholding return, GA-V payment voucher for monthly/quarterly remittance, G-1003 annual reconciliation, GA UI wage base $9,500 with rates 0.04-8.10%, Administrative Assessment 0.06%, new-hire reporting via GA DOL within 10 days (shorter than federal 20-day deadline), and the absence of state-mandated paid sick leave or paid family leave.
jurisdiction: US-GA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# GA Payroll

## Georgia Payroll Compliance Skill (Tax Year 2025)

> **Loader contract.** This is a Tier 2 content skill. It MUST be loaded alongside `us-tax-workflow-base` (v0.2 or later) and, where relevant, the federal payroll skills (Form 941, 940, W-2/W-3, 1099-NEC issuance). It addresses Georgia-specific state payroll obligations only. Federal income tax withholding, FICA, FUTA, and federal new-hire reporting are out of scope and must be sourced from the federal skills.

> **Reviewer requirement.** Georgia payroll outputs must be reviewed by a Georgia-licensed CPA, an Enrolled Agent, or a payroll professional credentialed for Georgia (FPC or CPP under the American Payroll Association). Reviewer signoff is required before any return, voucher, or wage report is filed with the Georgia Department of Revenue (GA DOR) or the Georgia Department of Labor (GDOL).

## 1. Scope and Out-of-Scope

### 1.1 In scope

- **GA PIT withholding 2025 flat rate** — 5.19%  _(HB 111 (signed April 15, 2025, retroactive to January 1, 2025), reduced from 5.39%, phase-down toward 4.99% by 2030 under HB 1437 (2022) as amended by HB 1015 (2024) and HB 111 (2025))_
- **Form G-4** — Georgia Employee's Withholding Allowance Certificate (the state W-4 equivalent)  _(1.1 In scope)_
- **Form G-7** — Quarterly withholding return for employer remittance reconciliation  _(1.1 In scope)_
- **Form GA-V** — Withholding payment voucher used for monthly (or semi-weekly) and quarterly remittance depending on the employer's filing tier  _(1.1 In scope)_
- **Form G-1003** — Annual income statement reconciliation transmitting W-2 and 1099 data to GA DOR  _(1.1 In scope)_
- **GA UI 2025 taxable wage base** — $9,500 per employee per year  _(7.3 2025 taxable wage base)_
- **GA UI experience-rated rates** — 0.04% to 8.10%  _(1.1 In scope)_
- **GA UI new-employer rate** — 2.70%  _(1.1 In scope)_
- **Administrative Assessment** — 0.06% on UI taxable wages  _(1.1 In scope)_
- **New-hire reporting deadline** — Within 10 days of hire, to GDOL — shorter than federal PRWORA default of 20 days  _(1.1 In scope)_
- **Paid leave mandates** — Absence of state-mandated paid sick leave and absence of state-mandated paid family leave in Georgia  _(1.1 In scope)_
- **Workers' compensation insurance mandatory threshold** — 3 or more employees  _(O.C.G.A. §34-9-1 et seq.)_
- **Worker classification tests** — IRS 20-factor common-law test, plus the Georgia construction industry 4 P's test  _(O.C.G.A. §34-8-35(n))_
- **Final pay standard** — Georgia has no statute requiring accelerated final wage payment; the next regular payday standard applies  _(O.C.G.A. §34-7-2)_
- **W-2 and 1099-NEC filing deadline** — January 31 following the close of the calendar year  _(1.1 In scope)_
- **1099-NEC reporting threshold** — Exceeding $600 in a calendar year (Georgia conforms to federal §6041A threshold for 2025; the OBBBA increase to $2,000 takes effect 2026)  _(1.1 In scope)_

### 1.2 Out of scope

The following are explicitly out of scope for this skill:

- Federal income tax withholding (Form 941, 944, W-4, federal Publication 15 tables).
- FICA (Social Security and Medicare) computation.
- FUTA (Form 940).
- Federal W-2/W-3 filing with SSA (use `us-federal` payroll skill).
- State income tax for any state other than Georgia.
- Local Georgia occupational taxes (Atlanta business license fees, etc.) — these are licensing matters, not payroll.
- Garnishment processing under O.C.G.A. §18-4-1 et seq. — referenced only as a flag, not computed.
- Multi-state allocation beyond the worked example of a GA-resident commuting to Alabama.
- S-corporation reasonable compensation analysis (see `us-s-corp-election-decision`).
- Pass-through entity tax (PTET) elections (Georgia PTET under HB 149 / O.C.G.A. §48-7-23 is income-tax allocation, not payroll).

## 2. Georgia Personal Income Tax (PIT) Withholding — 2025 Rate and Phase-Down

### 2.1 The 2025 flat rate

- **Tax year 2025 Georgia PIT withholding rate** — 5.19% flat  _(O.C.G.A. §48-7-20(b)(3) as amended by HB 1437 (2022), HB 1015 (2024), and HB 111 (signed April 15, 2025))_
- **2024 base rate and retroactive reduction** — The 2024 base rate was 5.39%; HB 111 reduced the rate to 5.19% retroactive to January 1, 2025, and accelerated the phase-down schedule toward the long-term 4.99% target. GA DOR updated the TSD-WH Employer's Tax Guide in June 2025 to reflect the 5.19% rate; employers who used 5.39% for January–May 2025 payrolls were instructed to adjust subsequent withholdings or true up at year end, with employees reconciling any overwithholding on Form 500.  _(O.C.G.A. §48-7-20(b)(3); HB 111 (signed April 15, 2025))_
- **Supplemental wages withholding rate** — Withhold at the same 5.19% flat rate for supplemental wage payments; Georgia does not maintain a separate supplemental rate distinct from the regular rate the way the federal §3402(g) 22% supplemental rate operates.  _(GA DOR Employer's Tax Guide (2025 edition, June 2025 revision))_

### 2.2 Phase-down schedule (statutory, contingent on revenue triggers)

The HB 1437 / HB 1015 / HB 111 phase-down is not automatic — it operates as a statutory ceiling with annual triggers tied to revenue collections, debt service coverage, and reserve fund levels under O.C.G.A. §48-7-20(b)(4)(B):

**Phase-down schedule**  _(O.C.G.A. §48-7-20(b)(4)(B))_

| Report year | Statutory rate | Trigger / authority |
| --- | --- | --- |
| 2024 | 5.39% | Effective from HB 1437 base |
| 2025 | **5.19%** | **HB 111 (April 2025) reduced from 5.39%, retroactive to 1/1/2025** |
| 2026 | 5.09% (expected) | Subject to FY 2025 revenue trigger |
| 2027 | 4.99% | Subject to FY 2026 revenue trigger |
| 2028 | 4.99% | Statutory floor (no further reductions absent new legislation) |
| 2029 | 4.99% | Statutory floor |
| 2030 | 4.99% | Statutory floor (long-term policy target) |

> **AUDIT FLASH POINT — GA PIT mid-year rate change for 2025.** Many payroll software vendors, third-party processors, and even some CPAs did not promptly update Georgia withholding tables when HB 111 dropped the 2025 rate to 5.19% in April 2025 (retroactive to January 1). Employers who continued withholding at 5.39% for Q2 and beyond overwithheld Georgia income tax; employees reconcile on Form 500 and receive refunds. Employers who switched promptly but did not adjust YTD on the next paycheck created a small mismatch on the G-1003 annual reconciliation. The reverse risk applies to future rate drops (5.09% expected 2026, 4.99% expected 2027): payroll systems that fail to load the new TSD-WH guide into Q1 will underwithhold, and the employer is legally on the hook under O.C.G.A. §48-7-126. Before the first payroll of any new calendar year, confirm the employer's payroll system has loaded the current-year GA DOR Employer's Tax Guide rate. This is a recurring exam item GA DOR is actively scrutinizing on routine compliance audits.

### 2.3 Withholding computation methods

GA DOR publishes two methods in the annual Employer's Tax Guide (Publication TSD-WH):

1. **Percentage method** — apply the 5.19% rate to wages after subtracting the per-pay-period equivalent of the employee's Form G-4 allowances and standard deduction. Used by most payroll software.
2. **Tax tables** — pre-computed lookup tables published by GA DOR for weekly, biweekly, semi-monthly, monthly, and daily/miscellaneous payroll frequencies. Used primarily by small employers running payroll manually.

- **2025 GA standard deduction — Single / Head of Household** — $12,000  _(2.3 Withholding computation methods)_
- **2025 GA standard deduction — Married Filing Jointly** — $24,000 (each spouse $12,000 if both employed; the G-4 instructs how to allocate)  _(2.3 Withholding computation methods)_
- **2025 GA standard deduction — Married Filing Separately** — $12,000  _(2.3 Withholding computation methods)_
- **Personal exemption 2025** — $0 for 2025. The personal exemption was eliminated under HB 1437 when Georgia moved to the flat-rate structure, replaced by a higher standard deduction.  _(HB 1437)_
- **Dependent exemption** — $4,000 per qualifying dependent (this remains in place under HB 1437 — only the personal exemption was eliminated)  _(HB 1437)_

### 2.4 Withholding worked computation

**Example:** Single employee, biweekly pay, gross wages $2,500, claims 0 dependents on Form G-4.

1. Annualized gross: $2,500 × 26 = $65,000.
2. Less GA standard deduction (Single): $65,000 − $12,000 = $53,000.
3. Less dependents (0): $53,000.
4. Annual GA tax at 5.19%: $53,000 × 0.0519 = **$2,750.70**.
5. Per-pay-period withholding: $2,750.70 ÷ 26 = **$105.80**.

If the same employee claimed 2 dependents on G-4:

1. Annualized gross: $65,000.
2. Less standard deduction: $65,000 − $12,000 = $53,000.
3. Less dependents (2 × $4,000): $53,000 − $8,000 = $45,000.
4. Annual tax: $45,000 × 0.0519 = **$2,335.50**.
5. Per-pay-period: $2,335.50 ÷ 26 = **$89.83**.

## 3. Form G-4 — Georgia Employee's Withholding Allowance Certificate

### 3.1 Purpose and required collection

- **G-4 completion requirement** — Form G-4 is the Georgia equivalent of federal Form W-4. Every Georgia employee — including a Georgia resident working in Georgia, a Georgia resident working out-of-state with Georgia withholding elections, and a nonresident working in Georgia — must complete Form G-4 on or before their first day of work.  _(O.C.G.A. §48-7-102)_
- **G-4 retention requirement** — The employer is not required to file the G-4 with GA DOR routinely. The G-4 is retained in the employee personnel file for at least four years after the last return on which the form's elections were used. GA DOR may request copies during a compliance audit, and certain high-allowance claims trigger mandatory employer reporting (see §3.4).  _(O.C.G.A. §48-7-119)_

### 3.2 Key fields on the 2025 G-4

1. **Marital status** — Single, Married Filing Joint (both spouses working), Married Filing Joint (one spouse working), Married Filing Separate, Head of Household.
2. **Total allowances** — sum of self, spouse (if MFJ and not working), and dependents.
3. **Additional withholding amount** — discretionary flat dollar amount per pay period the employee wants withheld above the formula amount.
4. **Letter of exemption** (Line 8) — claim of exemption from Georgia withholding entirely. Allowed only if (a) the employee had no GA tax liability in the prior year AND (b) reasonably expects no GA liability in the current year. The exemption expires February 15 of the following year and a new G-4 must be filed.
5. **Nonresident military spouse exemption** — under the Military Spouses Residency Relief Act (50 U.S.C. §4001) and Georgia conformity, a military spouse whose state of domicile is not Georgia may claim exemption from Georgia withholding even when working in Georgia.

### 3.3 When the employer must default to "Single, zero allowances"

- **Default withholding requirement** — Under GA DOR Regulation 560-7-8-.34, the employer must default to Single with zero allowances (the maximum withholding default) when: the employee fails to submit a Form G-4; the G-4 is submitted but unsigned or is illegible; the G-4 claims an obviously invalid status (e.g., a clearly unmarried employee claims MFJ with non-working spouse and the employer has actual knowledge). The 'Single, zero' default applies until a valid G-4 is received. The employer should not invent allowances based on the federal W-4 — Georgia treats the W-4 as a federal document and does not import allowance counts from it.  _(GA DOR Regulation 560-7-8-.34)_

### 3.4 G-4 exemption / high-allowance employer reporting

- **High-allowance/exemption reporting requirement** — If an employee claims more than 14 allowances OR claims complete exemption from Georgia withholding and earns wages above the federal withholding minimum, the employer must submit a copy of the Form G-4 to GA DOR Withholding Tax Unit within 30 days of receipt. GA DOR may reject the claim and instruct the employer in writing on the correct withholding amount.  _(3.4 G-4 exemption / high-allowance employer reporting)_

This is a small-volume but high-audit-risk filing — many employers either miss the reporting requirement or never identify which G-4s cross the 14-allowance threshold.

## 4. Form G-7 — Quarterly Withholding Return

### 4.1 Filing tiers

- **Look-back period definition** — Georgia employers are classified into one of four filing tiers based on look-back-period withholding liability. The look-back period is July 1 through June 30 of the year immediately preceding the calendar year (e.g., the 2025 calendar year tier is determined by withholding liability for the 12 months July 1, 2023 through June 30, 2024).  _(4.1 Filing tiers)_

**Filing tiers**  _(4.1 Filing tiers)_

| Tier | Liability threshold | Payment frequency | Return |
| --- | --- | --- | --- |
| Quarterly | < $200 per month average | With G-7 quarterly | Form G-7 (one for each quarter) |
| Monthly | $200 – $416.66 per month (i.e., < $5,000 lookback annual) | GA-V voucher monthly | Form G-7 |
| Semi-weekly | > $50,000 lookback annual liability | Federal semi-weekly mirror | Form G-7 |
| Quarterly aggregate (G-7 NRW) | Nonresident withholding only | Quarterly with G-7 NRW | Form G-7 NRW |

- **GA monthly threshold vs federal comparison** — Note the GA monthly threshold ($500 per quarter aggregate, roughly $200/month) is materially lower than the comparable federal §3402 monthly tier (federal lookback for monthly depositor status is $50,000 over the lookback year). A small Atlanta employer can be a federal monthly depositor while being a Georgia semi-weekly depositor if their GA withholding exceeds $50,000 in the lookback period.  _(4.1 Filing tiers)_

### 4.2 G-7 due dates (calendar year 2025)

**G-7 due dates 2025**  _(4.2 G-7 due dates (calendar year 2025))_

| Quarter | Period covered | G-7 due date |
| --- | --- | --- |
| Q1 | Jan 1 – Mar 31 | **April 30, 2025** |
| Q2 | Apr 1 – Jun 30 | **July 31, 2025** |
| Q3 | Jul 1 – Sep 30 | **October 31, 2025** |
| Q4 | Oct 1 – Dec 31 | **January 31, 2026** |

- **Weekend/holiday and Q4 2025 due date** — If the due date falls on a Saturday, Sunday, or Georgia legal holiday, the return is timely if filed on the next business day. None of the 2025 quarterly G-7 due dates above fall on a weekend except Q4 January 31, 2026 (a Saturday) — so the effective Q4 2025 G-7 due date is Monday, February 2, 2026.  _(4.2 G-7 due dates (calendar year 2025))_

### 4.3 What G-7 reports

Form G-7 captures:

1. Georgia employer withholding account number (8-digit GA WH account).
2. FEIN.
3. Quarter and year.
4. Total Georgia income tax withheld from wages during the quarter.
5. Total Georgia tax remitted via GA-V vouchers during the quarter.
6. Difference (overpayment refund/credit OR balance due).
7. Adjustments for prior period errors corrected in the current quarter.
8. Employer signature and date.

GA-V remittances and the G-7 are reconciliation pair — the G-7 is not the payment vehicle. Payment travels with GA-V. If the G-7 shows a balance due, that balance must accompany the G-7 (functionally treated as a late GA-V).

### 4.4 G-7 filing channels

- **Mandatory e-filing threshold** — Georgia Tax Center (GTC) at https://gtc.dor.ga.gov — mandatory for employers with $500+ annual withholding liability.  _(GA DOR Regulation 560-3-2-.26 e-filing rule)_

2. **Paper Form G-7** — permitted only for employers below the e-file threshold or with an approved hardship waiver.
3. **Bulk filing via approved payroll software** — most major providers (ADP, Paychex, Gusto, QuickBooks) file G-7 on behalf of clients via the GA DOR bulk file specification.

### 4.5 G-7 penalties

- **Late filing penalty** — $25 per return, plus 5% per month of unpaid balance up to 25% maximum  _(O.C.G.A. §48-7-126)_
- **Late payment penalty** — 0.5% per month of unpaid balance up to 25% maximum, separate from the late filing penalty  _(4.5 G-7 penalties)_
- **Failure to withhold penalty** — 100% of the amount that should have been withheld, plus 9% interest per annum  _(O.C.G.A. §48-2-40 sets the 2025 interest rate at 9% — the prime rate plus 3% with quarterly resets)_
- **Negligence and fraud penalties** — Additional 5% if the underpayment is due to negligence; additional 50% if due to fraud  _(4.5 G-7 penalties)_

## 5. Form GA-V — Withholding Payment Voucher

### 5.1 When GA-V is used

- **GA-V frequency by tier** — Quarterly tier (< $200/month or < $500/quarter aggregate withholding liability): GA-V is submitted with the G-7 quarterly return. No separate monthly vouchers. Monthly tier ($200 – $416.66/month, i.e., $5,000 annual lookback): GA-V is submitted by the 15th day of the month following the month of withholding. For example, January 2025 withholding GA-V is due February 15, 2025. Semi-weekly tier (> $50,000 annual lookback): GA-V is submitted on the federal semi-weekly schedule — Wednesday GA-V for wages paid Wednesday/Thursday/Friday, Friday GA-V for wages paid Saturday/Sunday/Monday/Tuesday. Georgia mirrors the federal Reg §31.6302-1 schedule.  _(5.1 When GA-V is used; federal Reg §31.6302-1)_

### 5.2 The $500/quarter monthly threshold

- **$500/quarter monthly remittance trigger** — A common simplification used by GA DOR field staff and many payroll guides: an employer with $500 or more of withholding liability per quarter must remit on the monthly schedule. Below $500/quarter, the employer remits with the quarterly G-7. Above $500/quarter, monthly GA-V vouchers are required.  _(5.2 The $500/quarter monthly threshold)_
- **$500/quarter trigger duration** — The $500/quarter rule operates as a one-quarter trigger — once an employer crosses $500 in any quarter, the employer must remit on the monthly schedule for the balance of the calendar year and the following calendar year, after which the lookback-period rule resets the tier.  _(5.2 The $500/quarter monthly threshold)_

### 5.3 GA-V fields

1. Period (month and year) covered.
2. GA withholding account number.
3. FEIN.
4. Total Georgia income tax withheld for the period.
5. Total Georgia income tax remitted (the dollar amount of the voucher).
6. Signature.

### 5.4 EFT requirement

- **EFT requirement threshold** — Employers with $500 or more in any single GA-V payment must remit electronically via GTC ACH debit or ACH credit. Paper check is permitted only for payments under $500 and for employers without GTC access.  _(O.C.G.A. §48-2-32)_

### 5.5 GA-V late payment treatment

- **Late/short GA-V treatment** — If a GA-V is missed or short, the deficiency is carried into the next GA-V and the eventual G-7. The G-7 reconciliation will show a balance due that travels with the G-7 itself, treated as a late voucher subject to the 0.5%/month late payment penalty plus 9% interest.  _(5.5 GA-V late payment treatment)_

## 6. Form G-1003 — Annual Income Statement Reconciliation

### 6.1 Purpose

Form G-1003 is the annual transmittal by which the employer:

1. Reconciles total Georgia withholding reported on quarterly G-7s with total Georgia withholding reported on the employees' Forms W-2.
2. Transmits copies of all Forms W-2 issued for the calendar year.
3. Transmits copies of all Forms 1099 with Georgia withholding (1099-NEC, 1099-MISC, 1099-R with GA tax withheld).

### 6.2 Due date

- **G-1003 due date** — January 31 of the year following the close of the calendar year. For 2025 wages: Monday, February 2, 2026 (because January 31, 2026 falls on a Saturday).  _(6.2 Due date)_
- **No automatic extension** — GA DOR strictly enforces this date — Georgia, like the federal SSA, moved to the accelerated January 31 W-2 filing schedule effective for the 2017 tax year onward. There is no automatic extension for G-1003. A discretionary 30-day extension may be requested in writing before January 31, but is granted only for documented hardship.  _(6.2 Due date)_

### 6.3 G-1003 fields

1. Total number of W-2s transmitted.
2. Total Georgia wages from W-2 Box 16.
3. Total Georgia tax withheld from W-2 Box 17.
4. Total number of 1099s transmitted (only those with GA withholding or those exceeding $600 in nonemployee compensation).
5. Total Georgia withholding from 1099s.
6. Total combined GA withholding (must match sum of all 2025 G-7s).
7. Reconciliation difference (should be zero).

### 6.4 1099-NEC reporting requirement under G-1003

- **1099-NEC GA reporting threshold** — Georgia requires the filing of Form 1099-NEC with the state when the payment exceeds $600 in nonemployee compensation and the payee is a Georgia resident or the services were performed in Georgia. This conforms to the federal §6041A threshold for tax year 2025.  _(6.4 1099-NEC reporting requirement under G-1003)_

> **Threshold change watch.** OBBBA (P.L. 119-21) raises the federal §6041A 1099 reporting threshold from $600 to $2,000 effective January 1, 2026. Georgia has not yet enacted conforming legislation as of the November 15, 2025 last_updated of this skill. Until Georgia conforms, the $600 threshold applies for Georgia 1099 reporting under G-1003 even though the federal threshold has risen to $2,000. Reviewer must check current GA DOR guidance at year-end 2025 / early 2026 for any conformity update.

### 6.5 G-1003 filing channels

1. **Georgia Tax Center (GTC)** — primary channel, supports both individual entry and bulk W-2/1099 file upload using the SSA EFW2 format for W-2s and IRS Publication 1220 format for 1099s.
2. **Paper G-1003** with paper W-2/1099 copies — permitted only for employers with fewer than 25 information returns.

### 6.6 G-1003 penalties

- **Late filing of G-1003** — $10 per information return, capped at $50,000 per calendar year  _(O.C.G.A. §48-7-126(d))_
- **Failure to file electronically when required** — $10 per return  _(6.6 G-1003 penalties)_
- **Late information returns within 30 days** — reduced $5 per return  _(6.6 G-1003 penalties)_

## 7. Georgia Unemployment Insurance (GA UI) and Administrative Assessment

### 7.1 Authority and administration

- **GA UI administration** — Georgia UI is administered by the Georgia Department of Labor (GDOL) under the Georgia Employment Security Law. UI is not a GA DOR matter — the two agencies are entirely separate, and an employer's GA WH account number with GA DOR is distinct from the employer's GDOL account number.  _(O.C.G.A. §34-8-1 et seq.)_

### 7.2 Coverage threshold

- **UI liability conditions** — Under O.C.G.A. §34-8-33, an employer is liable for Georgia UI when any of the following apply: 1. Pays $1,500 or more in wages in any calendar quarter, OR 2. Employs at least one worker for some portion of a day in each of 20 different calendar weeks (not necessarily consecutive) in a calendar year, OR 3. Is liable for FUTA under federal §3306, OR 4. Is an agricultural employer paying $20,000+ in wages in any quarter or employing 10+ agricultural workers in 20 different weeks, OR 5. Is a domestic service employer paying $1,000+ in any quarter.  _(O.C.G.A. §34-8-33)_
- **New employer registration deadline** — A new employer crossing the $1,500-quarter threshold must register with GDOL on or before the last day of the month following the quarter in which liability begins. Registration is via the GDOL Employer Portal at https://gdol.ga.gov.  _(7.2 Coverage threshold)_

### 7.3 2025 taxable wage base

- **GA UI 2025 taxable wage base** — $9,500 per employee per year  _(7.3 2025 taxable wage base)_

Georgia is among the states with the lowest UI wage base — for context, federal FUTA wage base is $7,000, and many neighboring states are materially higher (Tennessee $7,000, Alabama $8,000, Florida $7,000, South Carolina $14,000, North Carolina $32,600). Georgia has held the $9,500 wage base unchanged since 2013.

### 7.4 2025 contribution rates

**2025 contribution rates**  _(7.4 2025 contribution rates)_

| Component | 2025 rate range | Notes |
| --- | --- | --- |
| Experience rate | **0.04% – 8.10%** | Assigned annually per employer based on reserve ratio under O.C.G.A. §34-8-155 |
| New employer rate | **2.70%** | Default for the first ~36 months of liability, until experience rating kicks in |
| Administrative Assessment | **0.06%** | Separate component on UI taxable wages under O.C.G.A. §34-8-180 |

- **Administrative Assessment application** — The Administrative Assessment is a separate line item that funds GDOL operations. It applies to the same UI taxable wage base as the experience-rate contribution ($9,500 per employee in 2025). It is not absorbed into the experience rate — the employer pays both components.  _(7.4 2025 contribution rates)_
- **Maximum 2025 GA UI cost per employee** — Experience rate: $9,500 × 8.10% = $769.50; Administrative Assessment: $9,500 × 0.06% = $5.70; Total maximum per employee per year: $775.20  _(7.4 2025 contribution rates)_
- **Minimum 2025 GA UI cost per employee** — Experience rate: $9,500 × 0.04% = $3.80; Administrative Assessment: $9,500 × 0.06% = $5.70; Total minimum per employee per year: $9.50  _(7.4 2025 contribution rates)_
- **New employer 2025 cost per employee** — Experience rate: $9,500 × 2.70% = $256.50; Administrative Assessment: $9,500 × 0.06% = $5.70; Total new-employer per employee per year: $262.20  _(7.4 2025 contribution rates)_

### 7.5 GA UI quarterly filing — Form DOL-4N

**DOL-4N due dates**  _(7.5 GA UI quarterly filing — Form DOL-4N)_

| Quarter | Period | DOL-4N due |
| --- | --- | --- |
| Q1 | Jan – Mar | April 30 |
| Q2 | Apr – Jun | July 31 |
| Q3 | Jul – Sep | October 31 |
| Q4 | Oct – Dec | January 31 |

- **DOL-4N content and e-filing mandate** — The DOL-4N reports each employee's gross wages, taxable wages (capped at $9,500), and the employer's experience-rate contribution plus Administrative Assessment. Online filing via the GDOL Employer Portal is mandatory for employers with 100 or more employees; encouraged for all others.  _(7.5 GA UI quarterly filing — Form DOL-4N)_

### 7.6 SUTA dumping

- **SUTA dumping rule and penalty** — Georgia adopted the federal SUTA Dumping Prevention Act of 2004 via O.C.G.A. §34-8-172. Mandatory transfer of experience rating applies when there is substantially common ownership, management, or control between transferring and acquiring employers, and the transfer was made primarily for a lower UI rate. Penalty: highest rate (8.10% in 2025) plus an additional 2% for the year of transfer and the following three years, plus criminal exposure.  _(O.C.G.A. §34-8-172)_

## 8. New-Hire Reporting (GDOL) — 10-Day Deadline

### 8.1 The deadline

- **New-hire reporting deadline** — Every Georgia employer must report each newly hired or rehired employee to GDOL within 10 days of hire date.  _(O.C.G.A. §19-11-9.2)_

> **AUDIT FLASH POINT — 10-day GA new-hire deadline (shorter than federal default).** The federal Personal Responsibility and Work Opportunity Reconciliation Act of 1996 (PRWORA), at 42 U.S.C. §653a, sets a baseline new-hire reporting deadline of 20 days, with states permitted to require shorter deadlines. Georgia has elected the shorter 10-day deadline. Multi-state payroll departments routinely default to the 20-day federal baseline and miss the GA 10-day window — particularly for remote hires onboarded by an out-of-state HR team. GDOL does not commonly assess the per-failure penalty under O.C.G.A. §19-11-9.2(g), but the late reports flag the employer in child-support enforcement databases and create audit exposure. Every Georgia employer client should confirm with their payroll provider whether new-hire reports are filed on the 10-day or 20-day cadence.

### 8.2 What constitutes a "newly hired" employee

- **Newly hired employee definition** — Under O.C.G.A. §19-11-9.2(a)(3), a newly hired employee is one: 1. Who has not previously been employed by the employer, OR 2. Who was previously employed but has been separated from such employer for at least 60 consecutive days (rehire reporting requirement).  _(O.C.G.A. §19-11-9.2(a)(3))_
- **Independent contractors not reportable** — Independent contractors are not required to be reported under Georgia's new-hire law, even when paid via Form 1099-NEC. (This differs from some states — California, Massachusetts, Iowa, New Jersey, and New York require certain 1099 contractor reporting; Georgia does not.)  _(8.2 What constitutes a "newly hired" employee)_

### 8.3 Required data

1. Employee name.
2. Employee address.
3. Employee Social Security Number.
4. Employee date of hire.
5. Employer name.
6. Employer address.
7. FEIN.

### 8.4 Filing channels

1. **GDOL New Hire Reporting Portal** at https://gnhr.dol.state.ga.us — preferred, free.
2. **Electronic file upload** via the same portal in the federal OCSE-approved format.
3. **Paper Form DOL-1199A** — permitted but discouraged.
4. **Submission via the W-4 itself** — Georgia permits submission of the federal W-4 (with employer info added) in lieu of the dedicated new-hire report, mailed or faxed to GDOL. This is the original PRWORA fallback method.

### 8.5 Penalties

- **New-hire reporting penalties** — Up to $25 per failure, or up to $500 per failure if the failure is the result of conspiracy between the employer and employee to avoid the report. In practice, GDOL very rarely assesses these penalties — the practical risk is downstream: missing new-hire reports breaks the child-support enforcement match and exposes the employer to wage garnishment processing failures.  _(O.C.G.A. §19-11-9.2(g))_

### 8.6 Multistate employer election

- **Multistate new-hire reporting election** — Under PRWORA at 42 U.S.C. §653a(b)(1)(B), a multistate employer may elect to report all new hires to a single state. Georgia accepts inbound multistate elections. The election is made on a federal form filed with the federal Office of Child Support Enforcement (OCSE), not with GDOL directly. Once elected, the employer is bound by the chosen state's deadline — but a Georgia employer that elects to report all hires to Georgia is still bound by the 10-day GA deadline for those reports.  _(42 U.S.C. §653a(b)(1)(B))_

## 9. Worker Classification — IRS 20-Factor Test and the GA Construction 4 P's

### 9.1 General classification

- **Baseline classification test** — For Georgia state employment tax purposes, GDOL applies the IRS common-law 20-factor test (Revenue Ruling 87-41) as the baseline test for employee versus independent contractor. The 20 factors fall into three broad categories — behavioral control, financial control, and the nature of the relationship — and no single factor is dispositive.  _(Revenue Ruling 87-41)_

**Behavioral control (factors 1–10):**
1. Instructions about when/where/how to work.
2. Training.
3. Integration into the principal's business.
4. Services rendered personally.
5. Hiring, supervising, paying assistants.
6. Continuing relationship.
7. Set hours of work.
8. Full-time required.
9. Doing work on principal's premises.
10. Order or sequence set.

**Financial control (factors 11–15):**
11. Reports required (oral or written).
12. Payment by hour, week, or month (vs. by job).
13. Payment of business and traveling expenses.
14. Furnishing of tools and materials.
15. Significant investment by worker.

**Nature of relationship (factors 16–20):**
16. Realization of profit or loss.
17. Working for more than one firm at a time.
18. Making services available to the general public.
19. Right to discharge.
20. Right to terminate.

GA DOR has indicated informal acceptance of the IRS 3-category collapse (behavioral / financial / relationship) used in IRS Publication 1779. For Georgia withholding audits, demonstrating compliance under either framing is acceptable.

### 9.2 GA construction industry "4 P's" test — special rule

> **AUDIT FLASH POINT — Construction industry 4 P's test.** Under O.C.G.A. §34-8-35(n), Georgia applies a separate, four-factor presumptive test for worker classification in the construction industry. This test, known as the "4 P's," operates in addition to the 20-factor common-law test, and a failure on the 4 P's creates a presumption of employee status that is very difficult to rebut on a GDOL UI audit. Most construction subcontractors and 1099 framers, roofers, drywallers, and finishers in Georgia are misclassified under this rule — it is one of the highest-yield GDOL audit areas.

- **The 4 P's of construction worker classification** — 1. **Place of business** — Does the worker maintain a separate, identifiable place of business distinct from the principal's job site? A worker who only operates from the principal's job sites generally fails this prong. 2. **Profession** — Is the worker engaged in an independently established trade, occupation, profession, or business? A worker who works only for one general contractor and lacks an independent customer base generally fails this prong. 3. **Permission** — Is the worker free from control or direction over the performance of services, both under the contract and in fact? A worker who is supervised, scheduled, or directed in day-to-day execution generally fails this prong. 4. **Possession** — Does the worker possess the tools, equipment, vehicles, and other materials of the trade? A worker who shows up with only personal hand tools while the principal supplies powered equipment, scaffolding, and materials generally fails this prong. To classify a worker as an independent contractor in Georgia construction, the principal must affirmatively satisfy all four prongs. Failure on any one prong creates the presumption of employment.  _(O.C.G.A. §34-8-35(n))_

In practice, GDOL audits the 4 P's by examining:

- Copies of the worker's business license (City of Atlanta general contractor license, Georgia Secretary of State LLC registration, etc.).
- Copies of certificates of insurance showing the worker's own general liability and workers' compensation coverage.
- Copies of the worker's invoices to other unrelated principals during the same time period.
- Copies of the written subcontract showing scope and deliverables (not hours/days worked).
- Evidence the worker supplied trade-specific equipment.

### 9.3 GA UI versus IRS classification — split risk

- **Split classification risk** — A worker can be properly classified as an independent contractor for federal income tax / FICA purposes (passes the IRS 20-factor test on balance) but misclassified as an employee for Georgia UI purposes (fails the GA 4 P's test for construction work). GDOL is not bound by the IRS determination, and a Section 530 safe harbor (federal Revenue Act of 1978 §530) does not apply to Georgia UI proceedings. The reverse can also occur, though far more rarely.  _(9.3 GA UI versus IRS classification — split risk)_

### 9.4 GDOL audit penalties for misclassification

- **Misclassification consequences** — When GDOL determines a worker was misclassified: 1. Employer is assessed back UI contributions on the misclassified worker's wages for the entire audit period (typically the open three-year statute of limitations, or longer if fraud). 2. Administrative Assessment is assessed on the same wages. 3. Interest accrues at 1.5% per month under O.C.G.A. §34-8-166. 4. Penalty: 10% per quarter of unpaid contributions plus a minimum $35 per quarter (O.C.G.A. §34-8-165). 5. Cross-referral to GA DOR for income tax withholding assessment and to the Workers' Compensation Board.  _(O.C.G.A. §34-8-166; O.C.G.A. §34-8-165)_

## 10. Workers' Compensation, Final Pay, and Paid Leave Mandates

### 10.1 Workers' compensation — 3-employee threshold

- **Workers' comp insurance mandatory threshold** — Every Georgia employer with 3 or more employees (full-time, part-time, regular, seasonal, or otherwise) is required to maintain workers' compensation insurance, either via: 1. An admitted Georgia workers' comp insurer, OR 2. Self-insurance with State Board of Workers' Compensation approval (rare — requires substantial reserves).  _(O.C.G.A. §34-9-2)_
- **3-employee count composition** — The 3-employee count includes the employer's officers and shareholders (unless excluded via O.C.G.A. §34-9-2.2 corporate officer election). Independent contractors properly classified are not counted toward the 3-employee threshold — but if GDOL reclassifies a 1099 worker as an employee, that worker counts retroactively, exposing the employer to uninsured-employer liability under O.C.G.A. §34-9-126.  _(O.C.G.A. §34-9-2.2; O.C.G.A. §34-9-126)_
- **Penalties for failure to maintain coverage** — Civil penalties up to $10,000 per violation. Treble damages payable to an injured worker who was uninsured. Criminal exposure: misdemeanor under O.C.G.A. §34-9-126.  _(O.C.G.A. §34-9-126)_

### 10.2 Final pay — next regular payday

- **Final wage payment standard** — Georgia does not require accelerated payment of final wages. Under O.C.G.A. §34-7-2 and Georgia common law, an employer's obligation is to pay all wages earned through the date of separation on the next regular payday following the termination, voluntary or involuntary. This is markedly less aggressive than California (immediate for involuntary termination, 72 hours for voluntary resignation), Colorado (immediate for involuntary), or Massachusetts (same day for involuntary).  _(O.C.G.A. §34-7-2)_
- **Accrued PTO payout treatment** — Accrued but unused vacation/PTO is paid out at separation only if the employer's written policy or employment contract provides for such payment. Georgia common law treats unused PTO as a contractual benefit, not a wage, absent affirmative policy language. (Cf. California Labor Code §227.3, which treats accrued vacation as a wage that must be paid out.)  _(10.2 Final pay — next regular payday)_

### 10.3 Paid sick leave — no state mandate

- **No state-mandated paid sick leave** — Georgia has no state-mandated paid sick leave. There is no statewide accrual requirement, no minimum allotment, and no statewide pre-emption either way. Atlanta, Savannah, and other Georgia municipalities have not enacted local paid-sick-leave ordinances applicable to private employers (the City of Atlanta paid-sick-leave ordinance applies only to City of Atlanta employees).  _(10.3 Paid sick leave — no state mandate)_
- **Federal FMLA applicability** — Federal Family and Medical Leave Act (FMLA) unpaid leave still applies in Georgia for employers with 50+ employees. The federal Healthy Families Act has not been enacted.  _(10.3 Paid sick leave — no state mandate)_

### 10.4 Paid family leave — no state mandate

- **No state-mandated paid family leave** — Georgia has no state-mandated paid family leave insurance program comparable to California PFL, New York PFL, Washington PFML, Massachusetts PFML, Colorado FAMLI, Oregon Paid Leave, or the Connecticut, Delaware, Maine, Minnesota, Maryland, New Jersey, Rhode Island, or D.C. programs. Georgia employers therefore have no payroll deduction for PFML and no employer contribution for PFML.  _(10.4 Paid family leave — no state mandate)_
- **State employee paid parental leave exception** — A modest exception applies to state employees: under O.C.G.A. §45-20-100 (the "Georgia State Government Paid Parental Leave Act"), state government employees receive up to 120 hours of paid parental leave. This applies only to the state's own workforce and creates no obligation for private employers.  _(O.C.G.A. §45-20-100)_

## 11. Worked Examples

### 11.1 Example A — Atlanta-based 10-employee employer, full Q1 2025 payroll cycle

Atlanta Software Studio LLC, a single-member LLC disregarded for federal tax (owned by Maria Chen, GA resident), elects to be treated as an S-corporation effective January 1, 2025. The company has 10 W-2 employees including Maria as a shareholder-employee, all working from a midtown Atlanta office. Total Q1 2025 GA wages: $480,000. Total Q1 2025 GA withholding remitted: $19,200 (4% effective rate after G-4 allowances). No 1099 contractors paid in Q1.

- **Step 1 — Filing tier** — $19,200 ÷ 3 months = $6,400/month average withholding. This exceeds the $200/month quarterly-tier ceiling and the $5,000-annual semi-weekly-tier floor. Atlanta Software Studio is in the monthly tier for 2025.  _(n/a)_

**Step 2 — GA-V monthly vouchers**  _(n/a)_

| Month | GA WH liability | GA-V due | GA-V amount |
| --- | --- | --- | --- |
| January 2025 | $6,400 | February 15, 2025 | $6,400 |
| February 2025 | $6,300 | March 15, 2025 | $6,300 |
| March 2025 | $6,500 | April 15, 2025 | $6,500 |

- **EFT requirement** — EFT required (each voucher exceeds $500). Submit via GTC ACH debit.  _(n/a)_

Due April 30, 2025.
- Box: Q1 2025.
- Total GA tax withheld: $19,200.
- Total GA-V remittances: $6,400 + $6,300 + $6,500 = $19,200.
- Balance due: $0.

File via GTC.

- **Step 4 — GA UI / Administrative Assessment (DOL-4N for Q1)** — Due April 30, 2025. Assume 9 of 10 employees earn above the $9,500 wage base by end of Q1 (engineer salaries), Maria's S-corp reasonable compensation $80,000 annualized also exceeds. Taxable wages capped at 10 × $9,500 = $95,000 for the year, all of which falls in Q1 because of high salaries. Assume experience rate 1.5% (representative for a non-new employer): - Experience contribution: $95,000 × 1.5% = $1,425.00 - Administrative Assessment: $95,000 × 0.06% = $57.00 - Q1 total GDOL liability: $1,482.00 Note: Q2, Q3, Q4 DOL-4Ns will show zero taxable wages because the per-employee $9,500 cap is already exhausted in Q1.  _(n/a)_
- **Step 5 — New-hire reporting** — Two employees hired in February 2025 (Feb 3 and Feb 18). Each must be reported to GDOL within 10 days: - Feb 3 hire → reported by Feb 13, 2025. - Feb 18 hire → reported by Feb 28, 2025. If Atlanta Software Studio's payroll provider defaults to the federal 20-day cadence, the Feb 3 hire reported Feb 23 would be 10 days late, exposure under O.C.G.A. §19-11-9.2(g).  _(O.C.G.A. §19-11-9.2(g))_
- **Step 6 — Workers' compensation** — With 10 employees, mandatory under O.C.G.A. §34-9-2. Confirm policy in force, certificate of insurance on file. Maria as a corporate officer of the S-corp may elect exclusion under O.C.G.A. §34-9-2.2.  _(O.C.G.A. §34-9-2, O.C.G.A. §34-9-2.2)_

By February 2, 2026 (January 31, 2026 is Saturday), file G-1003 transmitting all 10 W-2s. Reconciliation: G-7 totals across Q1–Q4 must equal sum of Box 17 on the 10 W-2s.

**Monthly withholding figures**  _($6,400; $6,300; $6,500)_

| Month | Amount |
| --- | --- |
| January 2025 | $6,400 |
| February 2025 | $6,300 |
| March 2025 | $6,500 |

### 11.2 Example B — Georgia resident commuting to Alabama

Devon Brooks lives in Columbus, GA and commutes daily to Phenix City, AL where he works for an Alabama-based manufacturer (Phenix Industrial Inc.). Phenix Industrial has no Georgia employees, no Georgia office, and no Georgia nexus. Devon's annual W-2 wages: $72,000. Phenix Industrial withholds Alabama state income tax under Alabama law.

- **Step 1 — Phenix Industrial's Georgia obligations** — As an out-of-state employer with no Georgia nexus, Phenix Industrial is not required to withhold Georgia income tax for Devon (under O.C.G.A. §48-7-100 the duty to withhold runs to "employers" doing business in or deriving income from Georgia, which Phenix is not). Phenix has no Georgia W-2 reporting obligation and no Georgia UI obligation for Devon (his services are performed in Alabama, so under O.C.G.A. §34-8-35 he is an Alabama UI worker).  _(O.C.G.A. §48-7-100, O.C.G.A. §34-8-35)_
- **Step 2 — Devon's Georgia individual return** — Devon files Georgia Form 500 as a Georgia resident. He reports all $72,000 of wages on the Georgia return. He claims a credit for taxes paid to Alabama under O.C.G.A. §48-7-28 to avoid double taxation, limited to the lesser of (a) Alabama tax actually paid, or (b) the Georgia tax on the same income. - Alabama tax (at AL flat 5% / actually graduated up to 5% for high incomes — Alabama is graduated, not flat): assume $3,200. - Georgia tax on $72,000 at 5.19% after $12,000 standard deduction: ($72,000 − $12,000) × 5.19% = $60,000 × 5.19% = $3,114. - Credit allowed: lesser of $3,200 (AL paid) and $3,234 (GA on same income) = $3,200. - Net Georgia tax owed: $3,234 − $3,200 = $34. Devon will owe approximately $34 to Georgia at filing time (plus any quarterly estimated tax obligation if he wishes to avoid §48-7-120 underpayment penalty).  _(O.C.G.A. §48-7-28, §48-7-120)_

Devon may submit a Form G-4 to Phenix Industrial requesting voluntary Georgia withholding, but Phenix is not obligated to honor it absent a separate Georgia registration. Practical solution: Devon makes Georgia estimated tax payments via Form 500-ES if the shortfall would otherwise trigger §48-7-120 penalty.

Phenix Industrial reports Devon to Alabama new-hire reporting (Devon works in Alabama). Georgia GDOL does not need a new-hire report from Phenix because services are not performed in Georgia.

- **Step 5 — Watch-out — work-from-home days** — If Devon works some days remotely from his Columbus, GA home, the analysis changes. Days worked in Georgia create: - A potential Georgia withholding obligation for Phenix Industrial on the portion of wages allocable to Georgia work days (Phenix would need to register as a Georgia withholding agent). - A potential Georgia UI liability for Phenix on Georgia-source wages under O.C.G.A. §34-8-35(g)(2) "localization of work" tests. - A potential nexus issue for corporate income tax — beyond the scope of this skill, refer to GA corporate income tax skill. Many cross-border commuter arrangements break exactly here when COVID-era remote work patterns persist. Confirm with the employee and employer the actual physical location of work performance for each pay period.  _(O.C.G.A. §34-8-35(g)(2))_

### 11.3 Example C — Contractor classification, Atlanta general contractor with framing subcontractor

Peachtree Builders LLC is an Atlanta-based residential general contractor with 5 W-2 employees. Peachtree engages Carlos Reyes to perform framing on a series of single-family homes during 2025. Peachtree pays Carlos $48,000 over the year via 1099-NEC. The question on a GDOL UI audit: is Carlos an independent contractor or an employee?

- Carlos sets his own hours within the project schedule — neutral.
- Carlos works exclusively for Peachtree during 2025 (no other GC clients) — points toward employee.
- Carlos is paid weekly based on hours worked, not by completed job — points toward employee.
- Carlos owns his nail guns, framing hammers, and tape measures but Peachtree supplies the lumber and the framing tables and ladders — mixed but points toward employee on equipment.
- Carlos has no business license, no LLC registration, no general liability insurance — points strongly toward employee.

A balanced IRS 20-factor read: more likely employee than independent contractor.

- **Georgia 4 P's analysis (state special rule for construction)** — 1. Place of business — Carlos has no separate office, shop, or yard. Operates from Peachtree's job sites. FAIL. 2. Profession — Carlos works only for Peachtree, has no other unrelated principals during 2025, has no advertising or business identity. FAIL. 3. Permission — Carlos is supervised by Peachtree's site superintendent who directs the daily framing sequence. FAIL. 4. Possession — Carlos supplies hand tools but not the major framing equipment (table saws, scaffolding, the lumber itself). FAIL. All four prongs fail. Under O.C.G.A. §34-8-35(n) Carlos is presumptively an employee for Georgia UI. The presumption is very difficult to rebut.  _(O.C.G.A. §34-8-35(n))_
- **Audit assessment if GDOL reclassifies** — - Back UI contributions on $48,000 of wages (capped at $9,500 GA UI taxable wages). At new-employer 2.70%: $9,500 × 2.70% = $256.50. - Administrative Assessment: $9,500 × 0.06% = $5.70. - Penalty under O.C.G.A. §34-8-165: 10% × $256.50 × 4 quarters = $102.60 (minimum $35/quarter floor binds in any quarter where 10% is lower). - Interest at 1.5%/month from each original quarterly due date. - Cross-referral to GA DOR: assessment of unwithheld Georgia income tax on Carlos's wages. At 5.19% with no G-4 (single/zero default): roughly $48,000 × 5.19% = $2,491, plus 9% interest under O.C.G.A. §48-2-40 and possibly 100% failure-to-withhold penalty under O.C.G.A. §48-7-126. - Cross-referral to Workers' Compensation Board: with Carlos counted, Peachtree had 6 employees (5 W-2 + Carlos), so workers' comp was already required. If Carlos was injured during the period and Peachtree's workers' comp policy excluded him as a "1099," uninsured-employer liability under O.C.G.A. §34-9-126 — civil penalty up to $10,000 plus treble damages payable to Carlos for any work injury.  _(O.C.G.A. §34-8-165, §48-2-40, §48-7-126, §34-9-126)_

Reclassify Carlos as a W-2 employee prospectively. Discuss with Peachtree's counsel whether to file amended returns voluntarily (potentially mitigating penalties) or wait for audit assessment. Document the 4 P's analysis in the file.

## 12. Cross-Reference to Federal Payroll Skills

When this skill is loaded alongside the federal payroll content skills, the following responsibilities are split:

**Federal vs GA payroll responsibilities**  _(O.C.G.A. §48-7-100, §34-8-30 et seq., O.C.G.A. §34-9-2, O.C.G.A. §34-7-2)_

| Item | Federal skill | GA skill (this one) |
| --- | --- | --- |
| Income tax withholding | Federal §3402, Pub 15 tables, W-4 | GA §48-7-100, TSD-WH tables, G-4 |
| FICA | Federal §3101, §3111 | n/a (no GA equivalent) |
| FUTA | Federal §3301, Form 940 | n/a |
| State UI | n/a | O.C.G.A. §34-8-30 et seq., GA UI / Administrative Assessment |
| W-2 issuance | Federal §6051 | n/a |
| W-3 transmittal to SSA | Federal | n/a |
| W-2 transmittal to state | n/a | G-1003 to GA DOR |
| 1099-NEC issuance | §6041A (federal copy to IRS + recipient) | n/a |
| 1099-NEC transmittal to state | n/a | G-1003 + 1099 copy to GA DOR if GA payee or GA-source services |
| New-hire report | PRWORA 20-day default | **10-day** GA deadline via GDOL |
| Workers' comp | n/a (state matter) | O.C.G.A. §34-9-2, 3-employee threshold |
| Worker classification | IRS 20-factor / 3-category | IRS 20-factor + **GA construction 4 P's** |
| Final pay | n/a (state matter) | Next regular payday under O.C.G.A. §34-7-2 |
| Paid sick leave | None federal | **None** in Georgia |
| Paid family leave | None federal (FMLA is unpaid) | **None** in Georgia |
| Supplemental wage withholding | Federal 22% / 37% under §3402(g) | GA flat **5.19%** for 2025 |

## 13. Reviewer Checklist (Self-Test)

A reviewer signing off on a 2025 Georgia payroll engagement should confirm:

- [ ] GA WH account number is on file and matches the FEIN.
- [ ] GDOL employer account number is on file and is distinct from the GA WH account.
- [ ] G-4 on file for every active employee; "Single, zero" default applied for any missing G-4.
- [ ] Any G-4 with 14+ allowances or full exemption reported to GA DOR within 30 days of receipt.
- [ ] Filing tier determined correctly from prior year July–June lookback.
- [ ] All GA-V vouchers remitted on time (monthly 15th, or semi-weekly per federal schedule, or quarterly with G-7).
- [ ] All four quarterly G-7s filed by their respective due dates.
- [ ] G-1003 filed by January 31 (or next business day) following the calendar year, with all W-2s and qualifying 1099-NECs transmitted.
- [ ] DOL-4N filed for each quarter with correct taxable wage cap ($9,500) and both experience-rate and Administrative Assessment components computed.
- [ ] Every new hire reported to GDOL within **10 days**, not 20.
- [ ] Workers' comp policy in force if 3+ employees (including misclassified workers reclassified retroactively).
- [ ] Any 1099 contractor in the construction industry reviewed under the **4 P's** test, not just the IRS 20-factor test.
- [ ] If multistate workers, work-state allocation reviewed and Georgia withholding/UI registration triggers confirmed.
- [ ] Phase-down rate confusion check: current calendar year's Georgia withholding rate matches the year's TSD-WH publication, not the prior year's.
- [ ] All findings memorialized in the reviewer file with citations to O.C.G.A. provisions or GA DOR Regulations 560.

## 14. Authority Citations

- §34-7-2 — Time of payment of wages.
- §34-8-1 et seq. — Employment Security Law (UI).
- §34-8-33 — Coverage.
- §34-8-35 — Employment definition (including (n) construction 4 P's).
- §34-8-155 — Experience rating.
- §34-8-165 — Interest and penalties on UI.
- §34-8-166 — Interest rate.
- §34-8-172 — SUTA dumping.
- §34-8-180 — Administrative Assessment.
- §34-9-1 et seq. — Workers' Compensation.
- §34-9-2 — Coverage threshold (3 employees).
- §34-9-126 — Penalty for failure to insure.
- §19-11-9.2 — New-hire reporting.
- §45-20-100 — State employee paid parental leave.
- §48-2-32 — Electronic funds transfer.
- §48-2-40 — Interest on deficiencies.
- §48-7-20 — Income tax rates (HB 1437 / HB 1015 / HB 111 amendments).
- §48-7-23 — Pass-through entity tax election.
- §48-7-28 — Credit for taxes paid to other states.
- §48-7-100 — Withholding by employers.
- §48-7-102 — Form G-4 collection.
- §48-7-119 — Records retention.
- §48-7-120 — Estimated tax penalty.
- §48-7-126 — Withholding penalties.

- 560-3-2-.26 — Electronic filing requirements.
- 560-7-8-.34 — Withholding form defaults.

- Employer's Tax Guide (TSD-WH), 2025 edition.
- G-4 Instructions (2025).
- G-7 / GA-V Instructions (2025).
- G-1003 Instructions (2025).

- Employer Handbook (2025).
- DOL-4N Instructions.
- New Hire Reporting program documentation.

- 42 U.S.C. §653a — PRWORA new-hire reporting baseline.
- 50 U.S.C. §4001 — Military Spouses Residency Relief Act.
- IRC §3402, §3406, §6041A.
- Treas. Reg. §31.6302-1 — Semi-weekly deposit schedule.
- IRS Revenue Ruling 87-41 — 20-factor common-law test.
- IRS Publication 1779 — three-category common-law summary.
- Revenue Act of 1978 §530 — federal safe harbor (does NOT apply to GA UI).
- P.L. 119-21 (OBBBA) — §6041A threshold change effective 2026.

- HB 1437 (Ga. 2022 Regular Session) — flat tax conversion and phase-down.
- HB 1015 (Ga. 2024 Regular Session) — rate acceleration.
- HB 111 (Ga. 2025) — signed April 15, 2025; reduced PIT rate to 5.19% retroactive to January 1, 2025; accelerated phase-down schedule toward 4.99% target.
- GA DOR Employer's Tax Guide (TSD-WH), June 2025 revision — implementation guidance for HB 111 mid-year rate change.

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
