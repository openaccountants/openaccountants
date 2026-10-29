---
name: ks-payroll
description: >
  Use this skill whenever asked about Kansas payroll withholding for tax
  year 2026: Form K-4 employee withholding allowance certificate, KW-3
  annual withholding reconciliation (due January 31), KW-5 deposit reports
  with the five statutory filing frequencies ($200/$1,200/$8,000/$100,000
  thresholds), the KDOR rule that any payor who must withhold federal tax
  from payments to Kansas residents must also withhold Kansas tax, and
  default withholding when no K-4 is on file. Trigger on "Kansas
  withholding", "K-4", "KW-3", "KW-5", "KDOR withholding", "Kansas W-2".
  Corrected 2026-10-28 against archived KDOR FAQ, Pub. KW-100 (full text
  incl. percentage tables), and KW-3 e-file specs.
jurisdiction: US-KS
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.3
depends_on:
  - ks-income-tax
---

# Kansas payroll withholding, tax year 2026

> **Source-cited draft.** Built from the KDOR Withholding FAQ statutory frequency table, Pub. KW-100 Kansas Withholding Tax Guide, the KW-3 e-file specifications, the KW-110 withholding duty notice, the KDOR K-4 information page and K.S.A. 79-32,121, read on 2026-10-28. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Kansas professional.

Tax year: the calendar year. Authority: Kansas Department of Revenue (KDOR). Currency: US dollars. Governing act: **K.S.A. 79-3294 et seq.** (Kansas Withholding and Declaration of Estimated Tax Act, per KW-110). Covers Kansas income-tax withholding by employers and other payors.

See also: `ks-income-tax`, `ks-social-contributions`, `ks-cross-border`.

## Who this applies to

- **Employers must withhold Kansas tax** for (a) Kansas residents, whether services are performed inside or outside Kansas, and (b) nonresidents performing services in Kansas (KDOR Withholding page; KW-110).
- **Non-wage payors**: "Any employer or payor who must withhold Federal Income Tax from payments other than wages made to Kansas residents must also withhold Kansas Tax" (KDOR Withholding page). This sweeps in pensions, annuities and deferred income, interest and dividends, and lottery / gambling winnings when federal withholding applies (KW-100).
- **Registration**: withholding employers must file the Kansas business tax application **CR-16** before the first wage payment (KW-110).
- **No K-4 on file**: the employer must withhold **at the single rate with no allowances** (K-4 information page).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Allowance value (TY2025+ tables) | **$2,320** per allowance, tied to the K.S.A. 79-32,121 exemptions ($9,160 single / $18,320 married) | 2026 | [Pub. KW-100](https://ksrevenue.gov/pdf/kw100.pdf); [K.S.A. 79-32,121](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0121.html) |
| Default with no K-4 | Single, zero allowances | 2026 | [KDOR K-4 information](https://www.ksrevenue.gov/k4info.html) |
| KW-5 frequency: Annual | Withholding ≤ $200 a year; due January 25 | 2026 | [K.S.A. 79-3298(a)(5)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0098.html); [KDOR Withholding FAQ](https://www.ksrevenue.gov/faqs-withholding.html) |
| KW-5 frequency: Quarterly | $200.01 to $1,200; due the 25th of the month after quarter close | 2026 | K.S.A. 79-3298(a)(4) |
| KW-5 frequency: Monthly | $1,200.01 to $8,000; due the 15th of the following month | 2026 | K.S.A. 79-3298(a)(3) |
| KW-5 frequency: Semi-Monthly | $8,000.01 to $100,000; wages paid 1st to 15th due the 25th, the rest of the month due the 10th of the next month | 2026 | K.S.A. 79-3298(a)(2) |
| KW-5 frequency: Quad-Monthly | Over $100,000; periods end the 7th, 15th, 21st and last day; when undeposited tax at a period end is $667 or more it is due within 3 banking days; EFT required | 2026 | K.S.A. 79-3298(a)(1); KDOR Withholding FAQ (EFT) |
| Nonresident management or consulting fees | Payer withholds Kansas tax on management or consulting fees paid to a nonresident | 2026 | [K.S.A. 79-32,100a(d)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0100a.html) |
| E-filing mandate | **51+ employees / payees must e-file** W-2s / KW-3 | 2026 | [KW-3 e-file specs](https://www.ksrevenue.gov/pdf/KW-3ECSV.pdf) |

Frequency changes take effect January 1 (KDOR Withholding FAQ).

## The taxable base

- **Employee certificate:** Kansas Form K-4 sets the allowances. The "married" allowance is optional, spouses may claim "single" for two-earner joint accuracy; dependents are counted once; extra flat-dollar withholding is allowed (K-4 information page).
- **Computation methods:** the **percentage formula** (rate tables applied to the net wage after allowances) or the **wage-bracket tables**; above the last bracket of a wage table the percentage formula is mandatory (Pub. KW-100).
- **Allowance deduction:** each K-4 allowance removes $2,320 a year from the wage before the rate tables apply (Pub. KW-100; K.S.A. 79-32,121).
- **Non-wage payments** subject to federal withholding carry Kansas withholding too (see Who this applies to).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| CR-16 registration | Before the first wage payment | [KW-110](https://www.ksrevenue.gov/pdf/kw-110.pdf) |
| Form K-4 | At hire or when taxable payments begin; review annually and on marital / allowance changes | [KDOR K-4 information](https://www.ksrevenue.gov/k4info.html) |
| KW-5 deposit reports | Per the frequency table above; required for **every** period even with zero withholding; annual filers still file an annual KW-5 (KW-3 does not replace it); file and pay electronically | KDOR Withholding FAQ; Pub. KW-100 |
| KW-3 + W-2 / 1099 annual reconciliation | **January 31** of the following year ("The annual return, W-2s and 1099s are due by January 31 of the following year": KW-100; "All 2025 KW-3Es must be filed by January 31, 2026": KW-3 e-file specs) | Pub. KW-100; KW-3 e-file specs |
| Media | W-2 / KW-3 magnetic media no longer accepted | KW-3 e-file specs |

## Penalties and interest

- **Failure to withhold or pay over:** the employer is liable for the tax plus penalties under the withholding act (K.S.A. 79-3294 et seq.); K.S.A. 79-32,107(a) applies the K.S.A. 79-3228 income-tax penalties and interest to withholding noncompliance ([K.S.A. 79-32,107](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html)). Under K.S.A. 79-3228(c) that is 1% of the unpaid tax for each month or part of a month, up to 24%, plus interest ([K.S.A. 79-3228](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html)). The old 79-32,173 was repealed in 1988 ([K.S.A. 79-32,173](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0173.html)).
- **Worker misclassification:** "Penalties may be imposed on persons who knowingly and intentionally mis-classify an employee as an independent contractor and fail to report state income tax withholding or unemployment insurance contributions" (Pub. KW-100).
- KDOR maintains an Employment Tax Delinquencies page (KDOR business navigation).

## Cross-border points

- The resident-employee rule means Kansas withholding follows the **employee's residence** even for work performed out of state, multi-state employers must not net this against other states' nonresident withholding without credit analysis (see `ks-cross-border`).
- Nonresident employees working in Kansas: withhold Kansas; their home state may credit Kansas tax.
- W-2 state box reporting: single-state reporting per wage-source rules (KW-3 e-file specs).

## Worked examples

### Example 1: deposit frequency band check

An employer withholds $9,500 a year. That is $1,500 above the monthly band's $8,000 cap and $90,500 below the semi-monthly $100,000 cap, so the semi-monthly band applies: Jan 1–15 withholding is due January 25, Jan 16–31 is due February 10 (KDOR Withholding FAQ).

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

An employee claims 2 allowances on Form K-4 and is paid monthly. The annual allowance amount is 2 × $2,320 = $4,640, so $386.67 a month comes off gross pay before the rate tables apply.

```oa-check
name: KS K-4 allowance deduction
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

## Ask the client first

1. **Is a K-4 on file for every Kansas-withholding employee?** The single-zero default often surprises.
2. **Resident employees working remotely from other states?** Kansas withholding is still required on residents.
3. **Non-wage payments to Kansas residents** (pensions, contractor payments with federal withholding)? The Kansas duty mirrors the federal one.
4. **Annual Kansas withholding total?** It sets the KW-5 frequency.
5. **E-file readiness:** KCSC portal, KW-3E / W-2 spec formats; 51+ payees must e-file.

## Sources

| Source | URL | Read on |
|---|---|---|
| KDOR Withholding FAQ (statutory filing-frequency table) | https://www.ksrevenue.gov/faqs-withholding.html | 2026-10-28 |
| K.S.A. 79-3298 (remittance frequencies and dates; $667 quad-monthly rule) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0098.html | 2026-10-29 |
| K.S.A. 79-32,100a (non-wage withholding; nonresident management and consulting fees) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0100a.html | 2026-10-29 |
| K.S.A. 79-3228 (penalties) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html | 2026-10-29 |
| Pub. KW-100 Kansas Withholding Tax Guide (KW-3 / W-2 / 1099 due Jan 31, KW-5 every period, percentage formula vs wage-bracket tables, $2,320 allowance, misclassification) | https://ksrevenue.gov/pdf/kw100.pdf | 2026-10-28 |
| KW-3 / W-2 e-file specifications (Jan 31 deadline; 51+ e-file mandate; no magnetic media) | https://www.ksrevenue.gov/pdf/KW-3ECSV.pdf | 2026-10-28 |
| KW-110 withholding duty notice (resident / services-in-Kansas rule, CR-16, K.S.A. 79-3294 et seq.) | https://www.ksrevenue.gov/pdf/kw-110.pdf | 2026-10-28 |
| K.S.A. 79-32,121 (personal exemptions $9,160 / $18,320 / $2,320) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0121.html | 2026-10-28 |
| K.S.A. 79-32,107 (penalties and interest, withholding noncompliance) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html | 2026-10-28 |
| K.S.A. 79-32,173 (repealed 1988) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0173.html | 2026-10-28 |
| KDOR Withholding (duty, non-wage payor rule) | https://www.ksrevenue.gov/bustaxtypeswh.html | 2026-10-28 |
| KDOR K-4 information (allowance design, single-zero default) | https://www.ksrevenue.gov/k4info.html | 2026-10-28 |
| KDOR business navigation (Employment Tax Delinquencies page) | https://www.ksrevenue.gov/business.html | 2026-10-28 |

Not yet confirmed: the 2026 Kansas withholding percentage-method rate tables (Pub. KW-100 was not re-read in this review); the withholding rate under K.S.A. 79-32,100d for nonresident management and consulting fees; a citation for the statement that Kansas has no withholding reciprocity agreement with neighboring states; the exact K.A.R. regulation that assigns filing frequency; KDOR's enforcement detail for employment-tax delinquencies.

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
