---
name: ks-corporate-income-tax
description: >
  Use this skill whenever asked about Kansas corporate income tax for tax
  year 2026, the Form K-120 filing duty for corporations doing business in
  or deriving income from Kansas sources, automatic Subchapter S status for
  Kansas (banks excluded, they file the privilege tax), the repealed
  franchise tax, and federal-extension mechanics. Trigger on "Kansas
  corporate income tax", "K-120", "K-120S", "Kansas privilege tax banks",
  "KDOR corporate". Corrected 2026-10-28 against archived statute text:
  K.S.A. 79-32,110(c) normal tax 4% + surtax 3% over $50,000 (NOT a 12%
  bracket), no rate reduction for TY2026 per KDOR Notice 25-06.
jurisdiction: US-KS
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.3
depends_on:
  - ks-income-tax
---

# Kansas corporate income tax, tax year 2026

> **Source-cited draft.** Built from K.S.A. 79-32,101, 79-32,103, 79-32,107, 79-32,110, 79-32,110c, 79-32,141 and 79-32,142 (Kansas Revisor of Statutes), KDOR Notice 25-06, the KDOR 2025 Corporate Tax Booklet and the KDOR corporate income and franchise tax pages, read on 2026-10-28. No accountant has reviewed it. Do not file, pay, amend, or take a tax position from it without review by a qualified Kansas professional.

Tax year: the corporation's federal tax year (calendar or fiscal). Authority: Kansas Department of Revenue (KDOR). Currency: US dollars. Covers Kansas corporate income tax (Form K-120), S-corporation treatment (Form K-120S) and the bank privilege-tax carve-out.

See also: `ks-income-tax`, `ks-transfer-pricing`, `ks-cross-border`.

## Who this applies to

- **All corporations** doing business within or deriving income from sources within Kansas who are required to file a federal income tax return must file a Kansas return, **whether or not tax is due** (KDOR Corporate Income page; 2025 Corporate Tax Booklet).
- **Subchapter S corporations** for federal purposes are **automatically** S for Kansas and must file as such (Form K-120S): **except banks, savings and loan associations, and trust companies**, which are barred from S status for Kansas and file the **privilege tax return** (K.S.A. 79-1107/1108) instead of K-120 (KDOR FAQ).
- **Short-period returns:** required for Kansas whenever required federally (KDOR FAQ).
- **501(c)(3) nonprofits:** no Kansas copy of federal Form 990 is required; most still file the Secretary of State annual report (KDOR FAQ).
- **Franchise tax: repealed.** No Kansas franchise tax for tax year 2011 and after; the old KDOR tax (max $20,000, 0.03125% of net worth in its final year, Form K-150) is historical only. A separate **$55 Secretary of State filing fee** with the annual report still applies (KDOR Franchise page).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Normal tax | **4%** of Kansas taxable income | 2026 | [K.S.A. 79-32,110(c)(1)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html) |
| Surtax | **3%** of Kansas taxable income **in excess of $50,000** (one surtax exemption per corporate taxpayer) | 2026 | [K.S.A. 79-32,110(c)(2)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html); [2025 Corporate Tax Booklet](https://www.ksrevenue.gov/corpbook25.html), line 30 instructions |
| TY2026 rate reduction | **None**: FY2025 adjusted collections did not exceed inflation-adjusted base-year revenues, so the Secretary published no reduction | 2026 | [KDOR Notice 25-06](https://www.ksrevenue.gov/taxnotices/notice25-06.pdf) |
| Future reductions | 79-32,110c (Senate Bill 269 (2025), L. 2025 ch. 116): individual rates are cut first; the corporate surtax is cut only after both individual rates reach 4%, and only until **combined normal + surtax = 4%**. K.S.A. 79-32,110d (L. 2025 ch. 123) adds a separate test at the end of fiscal 2028 that can cut the normal tax for tax years after 2028 | 2027 on | [K.S.A. 79-32,110c](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110c.html); [K.S.A. 79-32,110d](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110d.html) |
| Estimated tax threshold | Required if Kansas liability is reasonably expected to **exceed $500** | 2026 | [K.S.A. 79-32,101(a)(2)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0101.html) |
| Extension payment | **90%** of the tax must be paid by the original due date to avoid the late-payment penalty | 2026 | [KDOR Corporate Income page](https://www.ksrevenue.gov/bustaxtypescorp.html) |
| Franchise tax | None for tax year 2011 and after; Secretary of State filing fee **$55** | 2026 | [KDOR Franchise page](https://www.ksrevenue.gov/bustaxtypesfranchise.html) |

**Correction:** the v0.1 draft carried "commonly cited as 4% first $50,000 and 12% above". K.S.A. 79-32,110(c) has no 12% rate: the law is 4% + 3% surtax over $50,000 = **7% marginal** on income above $50,000.

## The taxable base

| Item | Rule | Source |
|---|---|---|
| Base | Federal taxable income with Kansas modifications (K.S.A. 79-32,138); Kansas-source income for multistate filers | [2025 Corporate Tax Booklet](https://www.ksrevenue.gov/corpbook25.html) |
| Apportionment, tax years starting before 1 January 2027 (so 2026) | Business income x (property factor + payroll factor + sales factor) / 3. A qualifying taxpayer whose payroll factor exceeds 200% of its property factor may elect (property + sales) / 2. Railroads and interstate motor carriers use mileage | [K.S.A. 79-3279(a), (b)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0079.html) |
| Apportionment, tax years starting on or after 1 January 2027 | **Single sales factor** for all business income, with a deferred-tax deduction for publicly traded companies whose deferred tax changes because of the switch | K.S.A. 79-3279(c), (e) |
| Allocation authority | The director may allocate income, deductions and credits among organizations owned or controlled by the same interests | [K.S.A. 79-32,141](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0141.html) |
| Combined / consolidated | Federal-consolidated groups with all-Kansas income **must** file consolidated; the director may permit or require it for affiliated groups (Schedule K-121 mechanics per Booklet) | [K.S.A. 79-32,142](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0142.html); Booklet |
| Banks | Privilege tax return (79-1107/1108), not K-120 | KDOR FAQ |

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Form K-120 (corporate return) | **One month after the federal due date**, including any IRS extension; no separate Kansas extension request is needed (tax years after 2019). The federal due date is April 15 for a calendar-year C corporation and March 15 for an S corporation (26 U.S.C. § 6072(a), (b)), so the K-120 is due May 15 and the K-120S April 15 | [K.S.A. 79-3221(c)(2)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0021.html); [26 U.S.C. § 6072](https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleF-chap61-subchapA-partV-sec6072.htm) |
| Payment | The 2025 booklet states "Payment of any liability shall be due April 15, 2026" for 2025 calendar-year returns; 90% must be paid by the original due date to avoid K.S.A. 79-3228 penalties when the return is extended | [2025 Corporate Tax Booklet](https://www.ksrevenue.gov/corpbook25.html); K.S.A. 79-3221(c)(1) |
| Extension | "Kansas accepts the federal extension of time and will follow accordingly. The extension of time is to file the return not pay the tax. **Ninety percent of the tax must be paid by the due date to avoid late payment penalty**" | [KDOR Corporate Income page](https://www.ksrevenue.gov/bustaxtypescorp.html) |
| Estimated tax (Form K-120ES) | Installments **April 15, June 15, September 15 and December 15** (the corporate 4th installment is Dec 15, not Jan 15). First-year Kansas filers are exempt from estimates and the underpayment penalty | [K.S.A. 79-32,103(a)(1)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0103.html); Booklet |

## Penalties and interest

- Late-payment penalty is avoided only if **90%** of tax is paid by the due date (KDOR Corporate Income page, quoted above).
- Estimated-tax underpayment: a penalty at the delinquent-tax interest rate of K.S.A. 79-2968(b) on the shortfall, measured against **90% of the tax shown on the return**; not added if it does not exceed $1 ([K.S.A. 79-32,107(a)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html); [K.S.A. 79-2968](https://ksrevisor.gov/statutes/chapters/ch79/079_029_0068.html)).
- **Late filing or late payment:** 1% of the unpaid tax for each month or part of a month, up to 24% in total, plus interest; after a field audit of a filed and fully paid return, 1% a month up to 10% (25% where there was no reasonable attempt to comply) ([K.S.A. 79-3228(c)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html)).
- **Interest:** the federal IRC § 6621(a)(2) underpayment rate in effect on July 1 of the preceding year, plus one percentage point (K.S.A. 79-2968).

## Cross-border points

- Non-Kansas corporations with Kansas-source income file K-120 and apportion (see `ks-cross-border`).
- No Kansas franchise or gross-receipts tax stacks on top (franchise repealed, KDOR Franchise page).
- The treatment of S-corporation shareholders, including nonresident shareholders, is listed under Not yet confirmed.

## Worked examples

### Example 1: C corporation with 80% Kansas apportionment

A C corporation has $120,000 of federal-basis unitary income and a Kansas apportionment factor of 0.80. Kansas taxable income is $96,000. Normal tax is 4% of $96,000 = $3,840. The surtax is 3% of the $46,000 above the $50,000 surtax exemption = $1,380. Total Kansas tax $5,220.

```oa-check
name: KS corporate tax statutory rates
inputs:
  income: 120000
  factor: 0.80
  normal: 0.04
  surtax: 0.03
  exemption: 50000
steps:
  - ks_income: income * factor
  - band1: ks_income * normal
  - band2: max(ks_income - exemption, 0) * surtax
  - tax: band1 + band2
expected:
  ks_income: 96000
  band1: 3840
  band2: 1380
  tax: 5220
```

### Example 2: extension safe harbor on the same facts

The corporation extends via federal Form 7006. The extension covers filing, not payment, so 90% of the $5,220, which is $4,698, must be paid by the original due date to avoid the late-payment penalty; the $522 balance follows with the return.

```oa-check
name: KS 90% extension payment
inputs:
  tax: 5220
  safe: 0.90
steps:
  - must_pay: tax * safe
  - balance_due: tax - must_pay
expected:
  must_pay: 4698
  balance_due: 522
```

## Ask the client first

1. **Federal filing status** (C, S, bank / thrift / trust company)? It decides K-120 vs K-120S vs the privilege return.
2. **Kansas nexus footprint:** property, payroll and sales by state? It drives the apportionment factor.
3. **Affiliated group members in other states?** Consolidated-return exposure under 79-32,142.
4. **Was 90% of the tax paid by the unextended due date** before relying on the federal extension?

## Sources

| Source | URL | Read on |
|---|---|---|
| K.S.A. 79-32,110 (rates: 4% normal + 3% surtax over $50,000) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html | 2026-10-28 |
| K.S.A. 79-32,110c (rate-reduction mechanism; surtax floor at combined 4%) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110c.html | 2026-10-28 |
| KDOR Notice 25-06 (no rate reduction for tax year 2026) | https://www.ksrevenue.gov/taxnotices/notice25-06.pdf | 2026-10-28 |
| KDOR 2025 Corporate Tax Booklet (April 15 due date, K-121 mechanics, three-factor formula, first-year estimate exemption) | https://www.ksrevenue.gov/corpbook25.html | 2026-10-28 |
| K.S.A. 79-32,101 (estimated tax, $500 threshold) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0101.html | 2026-10-28 |
| K.S.A. 79-32,103 (installments Apr 15 / Jun 15 / Sep 15 / Dec 15 for corporations) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0103.html | 2026-10-28 |
| K.S.A. 79-32,107 (underpayment penalty at the 79-2968(b) rate, 90% measure) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0107.html | 2026-10-28 |
| K.S.A. 79-2968 (interest on delinquent taxes) | https://ksrevisor.gov/statutes/chapters/ch79/079_029_0068.html | 2026-10-28 |
| K.S.A. 79-32,110d (fiscal 2028 corporate-receipts trigger) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110d.html | 2026-10-29 |
| K.S.A. 79-3279 (apportionment; single sales factor from 2027) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0079.html | 2026-10-29 |
| K.S.A. 79-3221 (corporate return one month after the federal due date) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0021.html | 2026-10-29 |
| K.S.A. 79-3228 (late filing and payment penalties) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html | 2026-10-29 |
| 26 U.S.C. § 6072 (federal due dates: C corporations April 15, S corporations March 15) | https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-10-29 |
| K.S.A. 79-32,141 (allocation authority, controlled groups) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0141.html | 2026-10-28 |
| K.S.A. 79-32,142 (consolidated returns) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0142.html | 2026-10-28 |
| K.S.A. 79-32,138 (Kansas taxable income of corporations; addition and subtraction modifications) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0138.html | 2026-10-28 |
| KDOR Corporate Income (filing duty, S auto-status, bank carve-out, 90% extension rule) | https://www.ksrevenue.gov/bustaxtypescorp.html | 2026-10-28 |
| KDOR FAQ (S status, banks, short periods, 501(c)(3)) | https://www.ksrevenue.gov/faqs.html | 2026-10-28 |
| KDOR Franchise Tax (repealed 2011+; $55 Secretary of State fee) | https://www.ksrevenue.gov/bustaxtypesfranchise.html | 2026-10-28 |

Not yet confirmed: the statutory payment due date for corporations (the booklet says April 15; K.S.A. 79-3221(c)(2) sets the filing date one month after the federal due date, and this review could not reach KDOR to reconcile them); the 2026 value of the K.S.A. 79-2968 interest rate; Kansas taxation of S-corporation shareholders' distributive share (cited in v0.2 as K.S.A. 79-32,139, not archived) and the form nonresident S-shareholders file (K-40 vs K-40PN).

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
