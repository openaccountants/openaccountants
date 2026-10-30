---
name: slovenia-tax-optimization
description: Use this skill whenever asked about reducing tax in Slovenia, tax planning, or legal strategies to minimise tax for a self-employed person (s.p.) or small company in Slovenia, for tax year 2026. Trigger on phrases like "reduce tax Slovenia", "normiranec", "normirani s.p.", "lump-sum tax Slovenia", "80% expense deduction", "flat-rate sole proprietor Slovenia", "s.p. vs d.o.o.", "save tax Slovenia", "tax planning Slovenia", "ZPZR". It covers the normed-expense (normiranec) regime under ZPZR from 2026 (two-year average revenue tests of EUR 120,000, 85,000 and 50,000, the 80% and 40% normed expenses, final tax of 20% then 35%), the regular s.p., the d.o.o. at 22% corporate tax with dividends at 25%, the tipping points, and the red lines (forced exit, related-party revenue, disguised employment). Out of scope, see the siblings slovenia-income-tax (full income tax), slovenia-social-contributions, si-corporate-income-tax and si-company-formation. ALWAYS read this skill before advising on any Slovenian tax optimisation.
version: 0.2
jurisdiction: SI
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovenia Tax Optimization

## Slovenia Tax Optimization Skill v0.2

**Tier 2. Figures for tax year 2026 are taken from the consolidated laws on pisrs.si and from FURS, read on 30 October 2026. Not yet signed off by a Slovenian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

| Field | Value |
| --- | --- |
| Country | Republic of Slovenia |
| Currency | EUR |
| Headline lever | **Normiranec** (normed-expense) s.p.: 80% of revenue deemed as expenses up to a cap, no receipts needed, final tax on the rest |
| Normiranec final tax (2026) | 20% on the base up to EUR 72,000 (EUR 33,000 if not full-time self-insured), 35% above (ZPZR art. 7) |
| Corporate tax (d.o.o.) | **22%** for 2024 to 2028 (ZORZFS art. 64); the ZDDPO-2 rate is 19% |
| Dividends to an individual | 25% final (ZDoh-2 art. 132(1)) |
| Anti-avoidance | Two-year revenue tests; related-party revenue counted; disguised employment (single-client "s.p.") |

> **The Slovenian headline is the NORMIRANEC regime.** A full-time self-insured sole proprietor deducts 80% of revenue up to EUR 60,000 as normed expenses, with no receipts. On revenue of EUR 60,000 the taxed base is EUR 12,000. That base is taxed at 20% as a final tax. This gives a very low effective rate for service freelancers with low real costs.

## Section 2 -- Normiranec (normed-expense) Regime

From tax year 2026 the entry and exit tests and the tax rate come from ZPZR (Uradni list RS 91/25, amended by ZPZR-A 32/26), which overrides ZDoh-2 arts. 48 and 135.a (ZPZR arts. 6, 7 and 21(2)). The normed expenses themselves still come from ZDoh-2 art. 59 (ZPZR art. 20).

| Feature | Full-time self-insured s.p. (at least 9 months in the year) | Other s.p. (for example, employed elsewhere) |
| --- | --- | --- |
| Normed expenses | 80% of revenue up to EUR 60,000; nothing on revenue above | 80% up to EUR 12,500; 40% from EUR 12,500 to 30,000; nothing above |
| Entry and stay-in test: average revenue of the two previous years | not over **EUR 120,000** | not over **EUR 50,000** |
| Final tax on the base | 20% up to EUR 72,000; EUR 14,400 + 35% above | 20% up to EUR 33,000; EUR 6,600 + 35% above |

Sources: ZDoh-2 art. 59(1) and (2); ZPZR arts. 6(3), 6(13) and 7(1).

- **The middle test.** An s.p. that was full-time self-insured in only one of the two previous years has a EUR 85,000 average test (ZPZR art. 6(3) and (13)).
- **"Nine months" in practice.** The full-time condition is met if the s.p. was compulsorily insured on the basis of self-employment for at least 75% of the minimum annual full-time hours (ZPZR art. 6(16)).
- **Part years and new businesses.** If the s.p. traded for only part of a previous year, the average is adjusted pro rata to the period traded (art. 6(4)). A previous year with no activity counts as zero revenue (art. 6(14)). So a brand-new s.p. qualifies. The pro rata adjustment does not apply if, in the 18 months before electing, the person set up a company, transformed the business or took over a business (art. 6(8)).
- **The base.** Revenue less normed expenses. No bookkeeping of actual costs is needed for the tax base. Social contributions are a separate charge (see [slovenia-social-contributions](slovenia-social-contributions.md)).
- **Election.** By 31 March of the year concerned. A new business elects within 8 days of registration, and a late election is rejected (ZDavP-2 art. 308(1) to (3)). The election carries on each year unless the s.p. gives notice of leaving by 31 March (art. 308(4)).
- **2026 status.** FURS confirmed on 16 October 2026 that ZPZR governs 2026. It said a separate law, ZIURS, would change the normed-expense rules from 1 January 2026 if it enters into force after a referendum. FURS said it will issue decisions moving s.p.s that fail the ZPZR tests to actual expenses for all of 2026 if ZIURS does not take effect (FURS news, 16 Oct 2026). Check the FURS page before advising.

## Section 3 -- Regime Choice

| Route | Best when |
| --- | --- |
| **Normiranec s.p.** | Low real expenses, revenue within the two-year average tests, want simplicity. Tax is 20% of the base up to EUR 72,000 (full-time) |
| **Regular s.p.** (actual expenses) | Real expenses above the normed level (80% of revenue up to EUR 60,000, so EUR 48,000 at most for a full-time s.p.), or forced out by the average test. Profit goes into the progressive scale, 16% to 50%, with allowances (see [slovenia-income-tax](slovenia-income-tax.md)) |
| **d.o.o.** (company) | Higher profit kept in the business; limited liability; control over salary and dividend extraction. 22% corporate tax, then 25% on dividends paid out |

- **Tipping points.**
  - Revenue above EUR 60,000 (full-time s.p.): each extra euro gets no normed expense, so it is fully in the base.
  - A base above EUR 72,000 (revenue above EUR 120,000 for a full-time s.p.): the extra base is taxed at 35%.
  - A two-year average above EUR 120,000, 85,000 or 50,000: forced exit next year.
  - Real expenses above the normed amount: actual expenses win.
  - Profit you do not need to draw: model a d.o.o.

## Section 4 -- d.o.o. Extraction

- **Corporate income tax (CIT).** 22% of the tax base for 2024 to 2028 (ZORZFS art. 64(1)). Profit kept in the company is not taxed again until it is paid out. Detail: [si-corporate-income-tax](si-corporate-income-tax.md).
- **Dividends.** Taxed at 25% as a final tax for a Slovenian resident individual (ZDoh-2 arts. 80(1) and 132(1)).
- **Owner salary.** A salary is a deductible cost for the company but carries social contributions and is taxed on the progressive scale. Owner-managers also pay social contributions, with the long-term care contribution at 2% (ZDOsk-1 art. 56(2)). The contribution bases are in the sibling skills. See [slovenia-social-contributions](slovenia-social-contributions.md) and [slovenia-payroll](slovenia-payroll.md).

## Section 5 -- Worked examples

**Example 1: full-time normiranec with revenue in the 35% band.** A designer is a full-time self-insured s.p. all of 2026. Average revenue for 2024 and 2025 was EUR 110,000, which is under EUR 120,000, so the s.p. can stay on normed expenses (ZPZR art. 6(3)). Revenue for 2026 is EUR 130,000. Normed expenses are 80% of the first EUR 60,000, which is EUR 48,000 (ZDoh-2 art. 59(1)). The base is 130,000 minus 48,000, which is EUR 82,000. Tax is EUR 14,400 on the first EUR 72,000 plus 35% of the EUR 10,000 above, which is EUR 17,900 final (ZPZR art. 7(1)). For 2027 the test is the average of 2025 and 2026. If 2025 revenue was over EUR 110,000, that average is over EUR 120,000 and the s.p. must use actual expenses in 2027 (ZPZR art. 6(13)).

```oa-check
name: Slovenia full-time normiranec, revenue EUR 130,000, 2026 (ZPZR art. 7)
inputs:
  revenue: 130000
  normed_cap: 60000
  band_limit: 72000
steps:
  - normed_expenses: min(revenue, normed_cap) * 0.80
  - base: revenue - normed_expenses
  - tax_20: min(base, band_limit) * 0.20
  - tax_35: max(base - band_limit, 0) * 0.35
  - tax: tax_20 + tax_35
expected:
  normed_expenses: 48000.00
  base: 82000.00
  tax: 17900.00
```

**Example 2: d.o.o. paying out all of its profit.** A d.o.o. has a 2026 tax base of EUR 100,000. Corporate tax at 22% is EUR 22,000 (ZORZFS art. 64(1)). It pays the rest, EUR 78,000, as a dividend to its resident owner. Dividend tax at 25% is EUR 19,500 (ZDoh-2 art. 132(1)). Total tax is EUR 41,500 and the owner keeps EUR 58,500. If the company keeps the EUR 78,000 instead, only the EUR 22,000 is due for now.

```oa-check
name: Slovenia d.o.o. base EUR 100,000, full payout as dividend, 2026
inputs:
  profit: 100000
steps:
  - cit: profit * 0.22
  - dividend: profit - cit
  - dividend_tax: dividend * 0.25
  - total_tax: cit + dividend_tax
  - owner_net: dividend - dividend_tax
expected:
  cit: 22000.00
  dividend_tax: 19500.00
  total_tax: 41500.00
  owner_net: 58500.00
```

## Section 6 -- Red Lines (do not cross)

- **Forced exit.** If the average revenue of the two previous years is over EUR 120,000 (full-time), EUR 85,000 (mixed) or EUR 50,000 (others), the s.p. must use actual expenses and keep full books for the year (ZPZR art. 6(13); ZDavP-2 art. 308(5)). Do not under-report to stay in.
- **Related-party revenue counts.** Revenue of related persons is added for the entry and exit tests. It is left out only if the taxpayer proves that meeting the normed-expense conditions was not the main reason, or one of the main reasons, for the set-up (ZPZR art. 6(9) and (13)). Splitting one business across related s.p.s or companies to stay under the tests does not work.
- **Disclosure.** A normiranec must disclose in the annual return the revenue earned from each related person and from any employer it also works for under an employment contract (ZPZR art. 6(15)).
- **Disguised employment.** Work must not be done under civil-law contracts where the elements of an employment relationship exist (ZDR-1 art. 13(2)). A single-client "s.p." under employer-like control can be reclassified. **AUDIT FLASH POINT.**

## PROHIBITIONS

- **No combining regimes.** NEVER combine normed expenses with actual-expense deductions. It is one or the other for the year.
- **No under-reporting advice.** NEVER advise under-reporting revenue to remain a normiranec.
- **No disguised employment presentation.** NEVER present a single-client s.p. as genuine self-employment.
- **No contradiction of related skills.** Rates must agree with `slovenia-income-tax.md`, `slovenia-social-contributions.md` and `si-corporate-income-tax.md`. Where they differ on the 2026 normed-expense rules, the ZPZR text cited here governs; flag the difference.
- **No presenting open points as confirmed.** NEVER present the "Not yet confirmed" items as settled, nor optimisation as definitive advice. Route to a licensed Slovenian tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Slovenia) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act on the Right to a Winter Allowance and the Reform of Normed Expenses (ZPZR), Uradni list RS 91/25 as amended by ZPZR-A 32/26, consolidated text NPB 1, arts. 6, 7, 19, 20, 21 | https://pisrs.si/pregledPredpisa?id=ZAKO9359 | 2026-10-30 |
| Personal Income Tax Act (ZDoh-2), consolidated text NPB 36, arts. 59, 80, 132 | https://pisrs.si/pregledPredpisa?id=ZAKO4697 | 2026-10-30 |
| Act amending ZDoh-2 (ZDoh-2AB), Uradni list RS 104/24, consolidated text NPB 1, art. 23 (point b not applied for 2026 under ZPZR art. 19) | https://pisrs.si/pregledPredpisa?sop=2024-01-3309 | 2026-10-30 |
| Reconstruction, Development and Financing Act (ZORZFS), consolidated text NPB 4, art. 64 | https://pisrs.si/pregledPredpisa?id=ZAKO8910 | 2026-10-30 |
| Corporate Income Tax Act (ZDDPO-2), consolidated text NPB 23, art. 60 | https://pisrs.si/pregledPredpisa?id=ZAKO4687 | 2026-10-30 |
| Tax Procedure Act (ZDavP-2), consolidated text NPB 32, art. 308 | https://pisrs.si/pregledPredpisa?id=ZAKO4703 | 2026-10-30 |
| Long-Term Care Act (ZDOsk-1), consolidated text NPB 2, art. 56 | https://pisrs.si/pregledPredpisa?id=ZAKO8819 | 2026-10-30 |
| Employment Relationships Act (ZDR-1), consolidated text, art. 13 | https://pisrs.si/pregledPredpisa?id=ZAKO5944 | 2026-10-30 |
| FURS news, normed expenses in 2026 and ZIURS (16 Oct 2026) | https://www.gov.si/novice/2026-10-16-ugotavljanje-davcne-osnove-z-normiranimi-odhodki-v-letu-2026-v-povezavi-z-interventnim-zakonom-ziurs/ | 2026-10-30 |

Not yet confirmed: the content of ZIURS and whether it enters into force for 2026 (it awaits a referendum); the owner-manager minimum contribution base and the s.p. contribution base (left to slovenia-social-contributions); the fines for disguised employment under ZDR-1; whether normed expenses also cover the s.p.'s own social contributions or these are deducted on top (not stated in ZPZR; check the FURS business-income brochure).

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
