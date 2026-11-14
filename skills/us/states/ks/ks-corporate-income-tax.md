---
name: ks-corporate-income-tax
description: >
  Use this skill whenever asked about Kansas corporate income tax for tax
  year 2026, the Form K-120 filing duty for corporations doing business in
  or deriving income from Kansas sources, automatic Subchapter S status for
  Kansas (banks excluded, they file the privilege tax), the repealed
  franchise tax, and federal-extension mechanics. Trigger on "Kansas
  corporate income tax", "K-120", "K-120S", "Kansas privilege tax banks",
  "KDOR corporate". Use the APEX-adjusted 3.5% normal rate plus 3% surtax over USD50,000;
  Notice23-10 effective2024 controls the earlier reduction. Notice25-06
  announces no additional revenue-triggered reduction for2026.
version: "0.4"
jurisdiction: US-KS
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - ks-income-tax
category: state-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: computation
domain: corporate-tax
---

# Kansas corporate income tax, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. Circular 230 section 10.37: establish relevant facts and law; do not assume missing facts or rely on audit risk. A qualified professional must review filing outputs.

Tax year: the corporation's federal tax year (calendar or fiscal). Authority: Kansas Department of Revenue (KDOR). Currency: US dollars. Covers Kansas corporate income tax (Form K-120), S-corporation treatment (Form K-120S) and the bank privilege-tax carve-out.

See also: `ks-income-tax`, `ks-transfer-pricing`, `ks-cross-border`.

## Scope

- **All corporations** doing business within or deriving income from sources within Kansas who are required to file a federal income tax return must file a Kansas return, **whether or not tax is due** (KDOR Corporate Income page; 2025 Corporate Tax Booklet).
- **Subchapter S corporations** for federal purposes are **automatically** S for Kansas and must file as such (Form K-120S): **except banks, savings and loan associations, and trust companies**, which are barred from S status for Kansas and file the **privilege tax return** (K.S.A. 79-1107/1108) instead of K-120 (KDOR FAQ).
- **Short-period returns:** required for Kansas whenever required federally (KDOR FAQ).
- **Exempt organizations:** the prior FAQ says no Kansas copy of Form 990 is required for a qualifying exempt organization. The current booklet distinguishes unrelated business taxable income reported on Form 990-T, which does require K-120. Secretary of State reporting is a separate obligation; its current cycle/fee is not established here.
- **Franchise tax: repealed.** No Kansas franchise tax for tax year 2011 and after; the old KDOR tax (max $20,000, 0.03125% of net worth in its final year, Form K-150) is historical only. The old KDOR page mentions a separate **USD 55 Secretary of State annual-report fee**; that historical amount/report cycle is **not verified for 2026** and must not be quoted as a current tax or fee.

## Ask the client first

1. **Federal filing status** (C, S, bank / thrift / trust company)? It decides K-120 vs K-120S vs the privilege return.
2. **Kansas nexus footprint:** property, payroll and sales by state? It drives the apportionment factor.
3. **Affiliated group members in other states?** Consolidated-return exposure under 79-32,142.
4. **Was 90% of the tax paid by the unextended due date** before relying on the federal extension?

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Normal tax | **3.5%** of Kansas taxable income (derived: the 4% normal tax in K.S.A. 79-32,110(c)(1) less the one-time 0.5% APEX reduction under 74-50,321(b), announced in Notice 23-10), effective tax years beginning 2024 | 2026 current continuing rate | [KDOR Notice 23-10](https://www.ksrevenue.gov/taxnotices/notice23-10.pdf); [74-50,321](https://ksrevisor.gov/statutes/chapters/ch74/074_050_0321.html); [79-32,110](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html); [2025 booklet](https://www.ksrevenue.gov/corpbook25.html) |
| Surtax | **3%** of Kansas taxable income **in excess of $50,000** (one surtax exemption per corporate taxpayer) | 2026 | [K.S.A. 79-32,110(c)(2)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html); [2025 Corporate Tax Booklet](https://www.ksrevenue.gov/corpbook25.html), line 30 instructions |
| TY2026 rate reduction | **No additional revenue-triggered reduction**: FY2025 collections failed the test. This does not reverse the APEX reduction already effective 2024 | 2026 | [KDOR Notice 25-06](https://www.ksrevenue.gov/taxnotices/notice25-06.pdf) |
| Future reductions | 79-32,110c (Senate Bill 269 (2025), L. 2025 ch. 116): individual rates are cut first; the corporate surtax is cut only after both individual rates reach 4%, and only until **combined normal + surtax = 4%**. K.S.A. 79-32,110d (L. 2025 ch. 123) adds a separate test at the end of fiscal 2028 that can cut the normal tax for tax years after 2028 | 2027 on | [K.S.A. 79-32,110c](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110c.html); [K.S.A. 79-32,110d](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110d.html) |
| Estimated tax threshold | Required if Kansas liability is reasonably expected to **exceed $500** | 2026 | [K.S.A. 79-32,101(a)(2)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0101.html) |
| Extension payment | **90%** of the tax must be paid by the original due date to avoid the late-payment penalty | 2026 | [KDOR Corporate Income page](https://www.ksrevenue.gov/bustaxtypescorp.html) |
| Franchise tax | None for tax year 2011 onward; old USD 55 Secretary of State fee is historical and not confirmed current | 2026 | [KDOR Franchise page](https://www.ksrevenue.gov/bustaxtypesfranchise.html) |

**Correction:** the v 0.1 draft carried "commonly cited as 4% first $50,000 and 12% above". The earlier 4% +3% correction removed a fictitious 12% bracket but missed the APEX reduction. Notice 23-10 reduced normal tax to 3.5% effective 2024; the current total marginal rate above 50,000 is **6.5%**, not 7% or 12%. Notice 25-06 announces no additional 2026 revenue-triggered cut.

### The taxable base

| Item | Rule | Source |
|---|---|---|
| Base | Federal taxable income with Kansas modifications (K.S.A. 79-32,138); Kansas-source income for multistate filers | [2025 Corporate Tax Booklet](https://www.ksrevenue.gov/corpbook25.html) |
| Apportionment, tax years starting before 1 January 2027 (so 2026) | Business income x (property factor + payroll factor + sales factor) / 3. A qualifying taxpayer whose payroll factor exceeds 200% of the **average of its property and sales factors** may elect (property + sales) / 2. Railroads and interstate motor carriers use mileage | [K.S.A. 79-3279(a), (b)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0079.html) |
| Apportionment, tax years starting on or after 1 January 2027 | **Single sales factor** subject to the statute's special-industry exception, including the subsection(f) alcoholic-beverage manufacturer rule; a deferred-tax deduction for qualifying publicly traded companies has its own eligibility/election conditions | [K.S.A.79-3279(c), (e), (f)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0079.html) |
| Allocation authority | The director may allocate income, deductions and credits among organizations owned or controlled by the same interests | [K.S.A. 79-32,141](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0141.html) |
| Combined / consolidated | Federal-consolidated groups with all-Kansas income **must** file consolidated; the director may permit or require it for affiliated groups (Schedule K-121 mechanics per Booklet) | [K.S.A. 79-32,142](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0142.html); Booklet |
| Banks | Privilege tax return (79-1107/1108), not K-120 | KDOR FAQ |

## Filing and payment

| Obligation | When | Source |
|---|---|---|
| Form K-120 (corporate return) | **One month after the federal due date**, including any IRS extension; no separate Kansas extension request is needed (tax years after 2019). Obtain the actual federal deadline from `us-form-1120-c-corp` and apply Kansas's calendar-month/business-day rule; do not confuse return timing with tax-payment timing | [K.S.A. 79-3221(c)(2)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0021.html) |
| Payment | **15th day of the fourth month after year-end**, under 79-3225(a), separately from the one-month-after-federal return rule. The 2025 booklet's April 15,2026 is the **2025-2026 filing cycle** example; calendar 2026 tax is payable April 15,2027. Extension relief requires 90% by the original payment date; interest still accrues on unpaid tax | [2025 Corporate Tax Booklet](https://www.ksrevenue.gov/corpbook25.html); [79-3225(a)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0025.html) |
| Extension | "Kansas accepts the federal extension of time and will follow accordingly. The extension of time is to file the return not pay the tax. **Ninety percent of the tax must be paid by the due date to avoid late payment penalty**" | [KDOR Corporate Income page](https://www.ksrevenue.gov/bustaxtypescorp.html) |
| Estimated tax (Form K-120ES) | Installments **April 15, June 15, September 15 and December 15** (the corporate 4th installment is Dec 15, not Jan 15). First-year Kansas filers are exempt from estimates and the underpayment penalty | [K.S.A. 79-32,103(a)(1)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0103.html); Booklet |

### Penalties and interest

- Late-payment penalty is avoided only if **90%** of tax is paid by the due date (KDOR Corporate Income page, quoted above).
- Estimated-tax underpayment: a penalty at the delinquent-tax interest rate of K.S.A. 79-2968(b) on the shortfall, measured against **90% of the tax shown on the return**; not added if it does not exceed $1 ([K.S.A. 79-32,107(a)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html); [K.S.A. 79-2968](https://ksrevisor.gov/statutes/chapters/ch79/079_029_0068.html)).
- **Late filing or late payment:** 1% of the unpaid tax for each month or part of a month, up to 24% in total, plus interest; after a field audit of a filed and fully paid return, 1% a month up to 10% (25% where there was no reasonable attempt to comply) ([K.S.A. 79-3228(c)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html)).
- **Interest:** the federal IRC § 6621(a)(2) underpayment rate in effect on July 1 of the preceding year, plus one percentage point (K.S.A. 79-2968).

### Cross-border points

- Non-Kansas corporations with Kansas-source income file K-120 and apportion (see `ks-cross-border`).
- General corporate franchise tax is repealed. This does not establish absence of every industry-specific gross-receipts levy; special bank privilege and insurance premium regimes remain outside the ordinary K-120 computation.
- The treatment of S-corporation shareholders, including nonresident shareholders, is listed under Not yet confirmed.

### Ordinary K-120 assembly and submission

Start from the actual federal return; `us-form-1120-c-corp` owns the federal computation and `us-pl-86-272-income-tax-nexus` owns the federal nexus limitation. Using the **2025-2026 filing cycle** booklet as the verified available form model, K-120 line 1 starts with federal taxable income after federal NOL/special deductions. Add back federal NOL at line 4 and make the supported Kansas additions/subtractions, including income-tax addbacks and applicable exempt US interest. Separate business income from allocated nonbusiness income; compute K-120AS factors and apportioned income, then allocated income and applicable expensing adjustments. Compute the separately supportable Kansas NOL rather than deducting the federal NOL twice. Kansas taxable income is line 28; normal/surtax are 29/30, total 31, credits 32, net 33 and payments/credits 34-40. Final 2026 line mapping and each claimed credit/NOL condition require the actual 2026 forms. [Current available booklet](https://www.ksrevenue.gov/corpbook25.html).

Combined groups use K-121, company-by-company income/balance-sheet reconciliation and the required allocation/apportionment schedules; one surtax exemption per corporate taxpayer is not one exemption for any arbitrary aggregate. The booklet requires the actual filed federal return and supporting modification schedules. Its special bank-holding/privilege-filer rule also requires the specified pro-forma information; do not use a pro-forma return as an ordinary substitute or consolidate an income-tax filer with a privilege-tax filer. A taxpayer electing all qualifying income as business income uses K-120EL, binding for the election year and following nine years; new-business 60-day and existing-business prior-year-end deadlines differ. Separate accounting requires KDOR permission and the booklet's separate books, management and interdependence conditions; do not choose it merely because its result is lower.

Use a KDOR-approved corporate electronic filing channel or the booklet's permitted paper route with required federal/state attachments; KCSC's corporate estimate/balance payment function alone does not file K-120. Select the correct corporate account/year and payment type for K-120ES, extension or balance payments, authorize payment, save confirmation and verify posting. Retain the return acceptance or paper delivery evidence separately. For amendments use the correct year/amended status and reconcile original payments, refunds and credits; do not count an original payment twice. Unconfirmed final 2026 e-file/vendor specifications must be checked before submission.

## Worked cases

### Example 1: C corporation with 80% Kansas apportionment

A C corporation has $120,000 of federal-basis unitary income and a Kansas apportionment factor of 0.80. Kansas taxable income is $96,000. Normal tax is 3.5% of USD 96,000 =3,360. The surtax is 3% of the $46,000 above the $50,000 surtax exemption = $1,380. Total Kansas tax USD 4,740. The former 4% assumption produced 5,220 and overstated 480; it is not the current rate.

```oa-check
name: KS corporate tax statutory rates
inputs:
  income: 120000
  factor: 0.80
  normal: 0.035
  surtax: 0.03
  exemption: 50000
steps:
  - ks_income: income * factor
  - band1: ks_income * normal
  - band2: max(ks_income - exemption, 0) * surtax
  - tax: band1 + band2
expected:
  ks_income: 96000
  band1: 3360
  band2: 1380
  tax: 4740
```

### Example 2: extension safe harbor on the same facts

The corporation extends via federal Form 7004. The extension covers filing, not payment, so 90% of USD 4,740, which is 4,266, must be paid by the original due date to avoid the late-payment penalty; the 474 balance remains subject to interest from the original payment deadline until paid; filing extension does not extend payment.

```oa-check
name: KS 90% extension payment
inputs:
  tax: 4740
  safe: 0.90
steps:
  - must_pay: tax * safe
  - balance_due: tax - must_pay
expected:
  must_pay: 4266
  balance_due: 474
```

## Boundary and exception table

| Facts | Treatment |
| --- | --- |
| Ordinary C corporation | K-120, adjusted 3.5% normal plus 3% above 50,000 |
| Federal S corporation | K-120S; bank/thrift/trust exception |
| Bank/thrift/trust or insurance | Separate privilege/premium regime, not ordinary K-120 tax |
| Extended return | Payment date remains fourth-month15th;90% penalty relief is not interest relief |
| Unitary/all-Kansas consolidated group | Apply required combined/consolidated rules and entity exemption treatment |

## When to refuse or refer

Refer uncertain nexus, banking/insurance status, unitary grouping, NOL/credit eligibility, special apportionment or missing payment history. Do not infer federal law protection from an ordinary remote-sales rule.

## Completion checklist

- Establish entity/nexus/group and actual tax year.
- Reconcile federal starting income and supported Kansas modifications/NOL.
- Support allocation/factors and compute current normal/surtax and credits.
- Calendar return and separate payment/estimates; save acceptance, attachments and posting evidence.

## Disclaimer

Informational and computational material only; qualified professional review is required before filing, paying or taking a tax position.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for K.S.A.79-32,110 (base statute and cross-reference to rate adjustments; read with APEX notice). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html | 2026-11-13 |
| Read for K.S.A. 79-32,110c (rate-reduction mechanism; surtax floor at combined 4%). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110c.html | 2026-11-13 |
| Read for KDOR Notice 25-06 (no additional revenue-triggered reduction for 2026, not reversal of APEX). | https://www.ksrevenue.gov/taxnotices/notice25-06.pdf | 2026-11-13 |
| Read for KDOR 2025 Corporate Tax Booklet (April 15 due date, K-121 mechanics, three-factor formula, first-year estimate exemption). | https://www.ksrevenue.gov/corpbook25.html | 2026-11-13 |
| Read for K.S.A. 79-32,101 (estimated tax, $500 threshold). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0101.html | 2026-11-13 |
| Read for K.S.A. 79-32,103 (installments Apr 15 / Jun 15 / Sep 15 / Dec 15 for corporations). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0103.html | 2026-11-13 |
| Read for K.S.A. 79-32,107 (underpayment penalty at the 79-2968(b) rate, 90% measure). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html | 2026-11-13 |
| Read for K.S.A. 79-2968 (interest on delinquent taxes). | https://ksrevisor.gov/statutes/chapters/ch79/079_029_0068.html | 2026-11-13 |
| Read for K.S.A. 79-32,110d (fiscal 2028 corporate-receipts trigger). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110d.html | 2026-11-13 |
| Read for K.S.A. 79-3279 (apportionment; single sales factor from 2027). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0079.html | 2026-11-13 |
| Read for K.S.A. 79-3221 (corporate return one month after the federal due date). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0021.html | 2026-11-13 |
| Read for K.S.A. 79-3228 (late filing and payment penalties). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html | 2026-11-13 |
| Read for K.S.A. 79-32,141 (allocation authority, controlled groups). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0141.html | 2026-11-13 |
| Read for K.S.A. 79-32,142 (consolidated returns). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0142.html | 2026-11-13 |
| Read for K.S.A. 79-32,138 (Kansas taxable income of corporations; addition and subtraction modifications). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0138.html | 2026-11-13 |
| Read for KDOR Corporate Income (filing duty, S auto-status, bank carve-out, 90% extension rule). | https://www.ksrevenue.gov/bustaxtypescorp.html | 2026-10-28 |
| Read for KDOR FAQ (S status, banks, short periods, 501(c)(3)). | https://www.ksrevenue.gov/faqs.html | 2026-10-28 |
| Read for KDOR Franchise Tax (repealed 2011+; $55 Secretary of State fee). | https://www.ksrevenue.gov/bustaxtypesfranchise.html | 2026-10-28 |
| Read for actual APEX reduction from 4% to 3.5% effective tax years beginning 2024, with 3% surtax unchanged. | https://www.ksrevenue.gov/taxnotices/notice23-10.pdf | 2026-11-13 |
| Read for separate APEX certification/normal-rate reduction mechanism, not the 2025 revenue-triggered surtax mechanism. | https://ksrevisor.gov/statutes/chapters/ch74/074_050_0321.html | 2026-11-13 |
| Read for payment 15th day fourth month, distinct from corporate filing one month after federal. | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0025.html | 2026-11-13 |

Not yet confirmed: final 2026 K-120/K-120AS/K-121 line mapping and electronic specifications; the 2026 79-2968 interest percentage; particular credit/NOL carryover and future single-sales/deferred-tax election facts; current Secretary of State fee/report cycle (old USD 55 claim is historical); S-shareholder distributive-share and nonresident return detail (old 79-32,139/K-40 vs K-40PN question remains unresolved). Bank privilege/insurance premium calculations and generic industry gross-receipts regimes are separate jobs. The payment/return distinction is now resolved by 79-3225 versus 79-3221. The separate `ks-transfer-pricing` skill now delegates corporate rate computation to this owner; its other legal gaps remain explicit.

> Contributed by Jeff Watts.
