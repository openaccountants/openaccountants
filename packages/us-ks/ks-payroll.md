---
name: ks-payroll
description: >
  Compute Kansas payroll withholding from K-4 and the currently published
  KW-100 percentage tables; determine resident and nonresident wages,
  KW-5 frequencies, electronic KW-3 reconciliation and penalties.
  Current available tables are used, with final 2026 replacement pending.
version: "0.4"
jurisdiction: US-KS
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - ks-income-tax
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: computation
domain: payroll
---

# Kansas payroll withholding, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. Circular 230 section 10.37: establish relevant facts and law; do not assume missing facts or rely on audit risk. A qualified professional must review filing outputs.

Tax year: the calendar year. Authority: Kansas Department of Revenue (KDOR). Currency: US dollars. Governing act: **K.S.A. 79-3294 et seq.** (Kansas Withholding and Declaration of Estimated Tax Act, per KW-110). Covers Kansas income-tax withholding by employers and other payors.

See also: `ks-income-tax`, `ks-social-contributions`, `ks-cross-border`.

## Scope

- **Employers must withhold Kansas tax** for (a) Kansas residents, whether services are performed inside or outside Kansas, and (b) nonresidents performing services in Kansas (KDOR Withholding page; KW-110).
- **Non-wage payors**: "Any employer or payor who must withhold Federal Income Tax from payments other than wages made to Kansas residents must also withhold Kansas Tax" (KDOR Withholding page). This includes qualifying pensions, annuities/deferred income and lottery/gambling payments under their specific required or voluntary federal-withholding conditions. **Interest and dividend backup withholding does not require Kansas withholding**, expressly excluded by current KW-100. Do not apply the summary payor rule without reading those exceptions.
- **Registration**: withholding employers must file the Kansas business tax application **CR-16** before the first wage payment (KW-110).
- **No K-4 on file**: the employer must withhold **at the single rate with no allowances** (K-4 information page).

## Ask the client first

1. **Is a K-4 on file for every Kansas-withholding employee?** The single-zero default often surprises.
2. **Resident employees working remotely from other states?** Kansas withholding is still required on residents.
3. **Non-wage payment type and required/voluntary withholding election?** Check current KW-100 exceptions, especially interest/dividend backup withholding and consulting payor/service conditions.
4. **Annual Kansas withholding total?** It sets the KW-5 frequency.
5. **E-file readiness:** KCSC access, current KW-3/payee formats, account/year reconciliation and payment evidence; current KW-100 requires all KW-3 returns electronically.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| K-4 percentage-method annual allowance | First allowance single/head of household/married filing separate USD 9,160; married filing jointly USD 18,320; each dependent USD 2,320; head-of-household additional USD 2,320 | Current published tables, 2025-2026 filing cycle fallback | [KW-100](https://www.ksrevenue.gov/kw100.html); [79-32,121](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0121.html) |
| Default with no K-4 | Single, zero allowances | 2026 | [KDOR K-4 information](https://www.ksrevenue.gov/k4info.html) |
| KW-5 frequency: Annual | Withholding ≤ $200 a year; due January 25 | 2026 | [K.S.A. 79-3298(a)(5)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0098.html); [KDOR Withholding FAQ](https://www.ksrevenue.gov/faqs-withholding.html) |
| KW-5 frequency: Quarterly | More than $200 but not more than $1,200; due the 25th of the month after quarter close | 2026 | [K.S.A. 79-3298(a)(4)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0098.html) |
| KW-5 frequency: Monthly | More than $1,200 but not more than $8,000; due the 15th of the following month | 2026 | [K.S.A. 79-3298(a)(3)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0098.html) |
| KW-5 frequency: Semi-Monthly | More than $8,000 but not more than $100,000; wages paid 1st to 15th due the 25th, the rest of the month due the 10th of the next month | 2026 | [K.S.A. 79-3298(a)(2)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0098.html) |
| KW-5 frequency: Quad-Monthly | Over $100,000; periods end the 7th, 15th, 21st and last day; when undeposited tax at a period end is $667 or more it is due within 3 banking days; EFT required | 2026 | [K.S.A. 79-3298(a)(1)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0098.html); KDOR Withholding FAQ (EFT) |
| Nonresident management or consulting fees | 5% of the fee when a Kansas entity pays in its ordinary trade/business/for-profit venture and the nonresident physically performs the services in Kansas; not every nonresident invoice | Current available publication | [KW-100](https://www.ksrevenue.gov/kw100.html); [79-32,100a(d)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0100a.html) |
| E-filing mandate | Current KW-100 requires all KW-3 returns electronically; old 51+ specification is not permission for smaller filers to use paper | Current publication | [KW-100](https://www.ksrevenue.gov/kw100.html) |

Frequency changes take effect January 1 (KDOR Withholding FAQ).

### The taxable base

- **Employee certificate:** Kansas Form K-4 sets the allowances. The "married" allowance is optional, spouses may claim "single" for two-earner joint accuracy; dependents are counted once; extra flat-dollar withholding is allowed (K-4 information page).
- **Computation methods:** the **percentage formula** (rate tables applied to the net wage after allowances) or the **wage-bracket tables**; above the last bracket of a wage table the percentage formula is mandatory (Pub. KW-100).
- **Allowance deduction:** use the first personal/marital allowance and dependent/head-of-household amounts separately, from the actual K-4. USD 2,320 is not the value of every allowance. The period amounts below are already rounded in the published table; do not replace a published period value with a differently rounded annual conversion.
- **Non-wage payments:** apply the payment-specific rules above. Current KW-100 allows the stated 5% percentage method for qualifying separately identified supplemental payments when the specified federal percentage method is used; otherwise use its combined/aggregate method. Do not treat 5% as the ordinary wage rate or a universal rate for every nonresident consulting invoice. K.S.A.79-32,100a(d) and 100d require their actual services/payor/prescribed-rate conditions. Current KW-100 prescribes 5% for the qualifying physically performed Kansas management/consulting fees in the table. Required Kansas lottery/gambling withholding is 5% of proceeds (winnings less the bet), reported on W-2G, rather than the ordinary wage formula.

### Percentage computation from the full current KW-100 tables

The current HTML publication identifies rates for wages paid on/after July 1, 2024. Some internal table captions still say January 2021. The actual fully read table values below use 5.2% and 5.58%. These are the **current available tables, a 2025-2026 filing cycle fallback**; a separately issued final 2026 replacement has **Not yet confirmed** status. Do not invent an inflation adjustment or substitute the individual tax brackets directly. [Current publication](https://www.ksrevenue.gov/kw100.html).

| Pay period | Single first allowance | Married-joint first allowance | Each dependent / additional head-of-household allowance | Source |
| --- | ---: | ---: | ---: | --- |
| Daily | 35.23 | 70.46 | 8.92 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Weekly | 176.15 | 352.31 | 44.62 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Biweekly | 352.31 | 704.62 | 89.23 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Semimonthly | 381.67 | 763.33 | 96.67 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Monthly | 763.33 | 1,526.67 | 193.33 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Quarterly | 2,290 | 4,580 | 580 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Semiannual | 4,580 | 9,160 | 1,160 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Annual | 9,160 | 18,320 | 2,320 | [KW-100](https://www.ksrevenue.gov/kw100.html) |

Subtract the applicable period allowances from gross taxable wages to obtain net wages N. At/below Z, tax is zero. Above Z through H, tax is 5.2% x (N - Z). Above H, tax is B + 5.58% x (N - H). Add the employee's requested extra withholding; apply the resident other-state credit or nonresident service fraction where required. Wage-bracket tables remain an alternative within their limits; above their maximum use the percentage formula for the entire payment. Current KW-100 permits rounding to whole dollars, with 50 cents rounded up; it does not require rounding in every payroll.

| Period | Single Z / H / B | Married-joint Z / H / B | Source |
| --- | --- | --- | --- |
| Daily | 14 / 102 / 4.60 | 32 / 209 / 9.20 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Weekly | 69 / 512 / 23 | 158 / 1,043 / 46 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Biweekly | 139 / 1,023 / 46 | 317 / 2,086 / 92 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Semimonthly | 150 / 1,109 / 49.83 | 343 / 2,260 / 99.67 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Monthly | 300 / 2,217 / 99.67 | 687 / 4,520 / 199.33 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Quarterly | 901 / 6,651 / 299 | 2,060 / 13,560 / 598 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Semiannual | 1,803 / 13,303 / 598 | 4,120 / 27,120 / 1,196 | [KW-100](https://www.ksrevenue.gov/kw100.html) |
| Annual | 3,605 / 26,605 / 1,196 | 8,240 / 54,240 / 2,392 | [KW-100](https://www.ksrevenue.gov/kw100.html) |

## Filing and payment

| Obligation | When | Source |
|---|---|---|
| CR-16 registration | Before the first wage payment | [KW-110](https://www.ksrevenue.gov/pdf/kw-110.pdf) |
| Form K-4 | At hire or when taxable payments begin; review annually and on marital / allowance changes | [KDOR K-4 information](https://www.ksrevenue.gov/k4info.html) |
| KW-5 deposit reports | Per the frequency table above; required for **every** period even with zero withholding; annual filers still file an annual KW-5 (KW-3 does not replace it); file and pay electronically | KDOR Withholding FAQ; Pub. KW-100 |
| KW-3 + W-2 / 1099 annual reconciliation | **January 31** of the following year, with applicable business-day relief; reconcile annual KW-5 withholding and required W-2/1099 state data. The old 2025 specification deadline describes the 2025-2026 filing cycle, not a new 2026 amount | Pub. KW-100; KW-3 e-file specs |
| Media | W-2 / KW-3 magnetic media no longer accepted | KW-3 e-file specs |

### Penalties and interest

- **Failure to withhold or pay over:** the employer remains liable. Under K.S.A.79-32,107(f)(1), a late employer remittance required by 79-3298(b) incurs 2% for 1-5 days, 5% for 6-15 days, 10% after 15 days, or 15% when still unpaid more than ten days after the prescribed notice/demand; reasonable-cause conditions apply. Subsection(f)(2) applies the 79-3228 penalty/interest provisions under subsection(a) beginning at the annual return's due date, not automatically at every deposit due date. The old blanket 1%-per-month/up-to-24% explanation did not replace these deposit stages. Willful failure can trigger the separate 100% liability in subsection(e). [79-32,107](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html); [79-3228](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html). Former 79-32,173 was repealed in 1988 and is not current penalty authority.
- **Worker misclassification:** "Penalties may be imposed on persons who knowingly and intentionally mis-classify an employee as an independent contractor and fail to report state income tax withholding or unemployment insurance contributions" (Pub. KW-100).
- KDOR maintains an Employment Tax Delinquencies page (KDOR business navigation).

### Cross-border points

- For a Kansas resident working outside Kansas, compute Kansas withholding **less tax required to be withheld for the other state**, under current KW-100. The K-4C procedure can shift the remaining difference obligation to the employee under its conditions. Do not collect full Kansas withholding twice without this analysis. Obtain a new K-4C after a substantial change within the stated ten-day period. [KW-100](https://www.ksrevenue.gov/kw100.html), [current withholding FAQ](https://www.ksrevenue.gov/faqs-withholding.html); see `ks-cross-border`.
- For nonresidents working partly in Kansas, compute withholding on total wages and multiply by the Kansas-services fraction under KW-100, rather than calculating a lower bracket on Kansas wages alone. Their home state may allow a credit under that state's rules.
- Reconcile W-2 state wage/withholding boxes to the actual sourcing and required multiple-state records. The old blanket single-state reporting sentence is not a substitute for these facts or current electronic specifications.

## Worked cases

### Example 1: deposit frequency band check

An employer withholds $9,500 a year. That is $1,500 above the monthly band's $8,000 cap and $90,500 below the semi-monthly $100,000 cap, so the semi-monthly band applies: Jan 1-15 withholding is due January 25, Jan 16-31 is due February 10 (KDOR Withholding FAQ).

```oa-check
name: KS withholding frequency band
inputs:
  annual_wh: 9500
  m_top: 8000
  sm_top: 100000
steps:
  - over_monthly_band: annual_wh - m_top
  - headroom_under_semimonthly_cap: sm_top - annual_wh
expected:
  over_monthly_band: 1500
  headroom_under_semimonthly_cap: 90500
```

### Example 2: percentage-formula allowance credit

An employee has **two dependent allowances**, in addition to the applicable first personal/marital allowance. Their dependent component is 2 x USD 2,320 = 4,640 annually, or an unrounded 386.6667 monthly. The published monthly component is 2 x 193.33 =386.66. This preserves the old arithmetic as a dependent-only component; it is **not the complete K-4 deduction**. A single employee also entitled to the first allowance uses 763.33 +386.66 =1,149.99 from the published monthly columns. The old claim that any two allowances had only the dependent value was wrong.

```oa-check
name: KS K-4 dependent component only
inputs:
  allowances: 2
  per_allowance: 2320
steps:
  - annual_credit: per_allowance * allowances
  - monthly_credit: annual_credit / 12
expected:
  annual_credit: 4640
  monthly_credit: 386.6666666666667
```

### Example 3: ordinary weekly wage computation

Invented single employee, USD 1,000 weekly taxable wages, first single allowance only, no dependents/extra withholding or interstate adjustment: net 823.85 after 176.15 allowance. Above 512, tax is 23 +5.58% x 311.85 =40.40123, or 40.40 at cents precision. Optional whole-dollar withholding is 40. For the zero-tax boundary, weekly wages 245.15 less 176.15 give 69 and zero tax.

```oa-check
name: KS current published weekly withholding and zero boundary
inputs:
  wages: 1000
  allowance: 176.15
  zero: 69
  high: 512
  base: 23
  rate: 0.0558
steps:
  - net: wages - allowance
  - tax: base + (net - high) * rate
  - zero_boundary_gross: allowance + zero
expected:
  net: 823.85
  tax: 40.40123
  zero_boundary_gross: 245.15
```

### Electronic submission, reconciliation and correction

In the KDOR Customer Service Center (KCSC), link the withholding account, choose the KW-5 period, enter total Kansas withholding, review/submit, authorize the electronic payment and retain both return and payment confirmations. Verify correct account/period credit. File zero periods while the account remains open. For KW-3 choose Withholding Tax Information, the annual return/year and return type, enter annual payments/withholding and required payee data, reconcile to all KW-5 periods and W-2/1099 totals, complete any balance payment screen, then verify and submit the return. Submission alone is not proof payment cleared. Current KW-100 requires all annual KW-3 returns electronically; magnetic media are not accepted. Final withholding returns after closure are due within 30 days after the month of closure under the publication's rule.

Current KW-100 distinguishes an **additional payment** through KCSC for an underpaid original period from an **amended/corrected KW-5**, for which it requires the paper form. Mark Amended Return, use the corrected amount for each affected original period and include the explanatory letter. Same-year excess can offset subsequent withholding periods using the specified KW-5 line; a prior-year credit requires a KDOR credit memo, with a copy accompanying each use. A remaining annual excess is generally reconciled through KW-3/credit memo. The FAQ says refunds are issued only on closed accounts, while KW-100 describes in-year amended refund requests; actual refund availability must be resolved with KDOR for the particular account. Do not assume any employee refund or cross-year transfer. Save corrected payee records, forms, submissions and payment/credit evidence.

## Boundary and exception table

| Facts | Treatment |
| --- | --- |
| Missing K-4 | Single/no allowance default |
| Resident works out of state | Required other-state withholding offset/K-4C conditions under the KDOR FAQ |
| Part-state nonresident | Full-wage computation times Kansas-service fraction |
| Interest/dividend backup withholding | No Kansas withholding under current KW-100 |
| Wages exceed wage-bracket table | Percentage formula for entire payment |

## When to refuse or refer

Refer uncertain payment classification, residency/localization, disputed notices or K-4C facts. Do not infer a consulting rate or reciprocity agreement, or run payroll without the actual certificate and period table.

## Completion checklist

- K-4/payment type, wage period and residence/services established.
- Published allowance and percentage computation reproduced; rounding documented.
- Assigned KW-5 frequency, zero periods and payment reconciled.
- Electronic KW-3/payee records accepted and payment credited; corrections retained.

## Disclaimer

Informational and computational material only; qualified professional review is required before filing, paying or taking a tax position.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for KDOR Withholding FAQ (statutory filing-frequency table). | https://www.ksrevenue.gov/faqs-withholding.html | 2026-11-13 |
| Read for K.S.A. 79-3298 (remittance frequencies and dates; $667 quad-monthly rule). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0098.html | 2026-11-13 |
| Read for K.S.A. 79-32,100a (non-wage withholding; nonresident management and consulting fees). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0100a.html | 2026-11-13 |
| Read for K.S.A. 79-3228 (penalties). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html | 2026-11-13 |
| Read for Pub. KW-100 Kansas Withholding Tax Guide (KW-3 / W-2 / 1099 due Jan 31, KW-5 every period, percentage formula vs wage-bracket tables, personal/marital/dependent period allowances, full percentage tables, nonwage/interstate exceptions, filing and misclassification). | https://www.ksrevenue.gov/kw100.html | 2026-11-13 |
| Read for KW-3 / W-2 e-file specifications (historical 2025-2026 filing-cycle specifications, Jan 31 and no magnetic media; current KW-100 all-electronic rule controls). | https://www.ksrevenue.gov/pdf/KW-3ECSV.pdf | 2026-10-28 |
| Read for KW-110 withholding duty notice (resident / services-in-Kansas rule, CR-16, K.S.A. 79-3294 et seq.). | https://www.ksrevenue.gov/pdf/kw-110.pdf | 2026-10-28 |
| Read for K.S.A. 79-32,121 (personal exemptions $9,160 / $18,320 / $2,320). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0121.html | 2026-11-13 |
| Read for K.S.A. 79-32,107 (penalties and interest, withholding noncompliance). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html | 2026-11-13 |
| Read for K.S.A. 79-32,173 (repealed 1988). | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0173.html | 2026-11-13 |
| Read for KDOR Withholding (duty, non-wage payor rule). | https://www.ksrevenue.gov/bustaxtypeswh.html | 2026-10-28 |
| Read for KDOR K-4 information (allowance design, single-zero default). | https://www.ksrevenue.gov/k4info.html | 2026-10-28 |
| Read for KDOR business navigation (Employment Tax Delinquencies page). | https://www.ksrevenue.gov/business.html | 2026-10-28 |
| Read for nonwage prescribed-rate delegation. | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0100d.html | 2026-11-13 |

Not yet confirmed: separately issued final 2026 replacement withholding tables/specifications; current available KW-100 amounts above are expressly a 2025-2026 filing cycle fallback, not invented 2026 indexed amounts. Also pending: actual consulting-payment payor/service facts for a particular invoice, any claimed neighboring-state reciprocity agreement, the specific frequency-assignment regulation beyond the verified statute, account-specific cross-year refund treatment and employment-tax delinquency enforcement detail. Federal payroll amounts are owned by `us-form-941-940-payroll`; Kansas UI is owned by `ks-social-contributions`.

> Contributed by Jeff Watts.
