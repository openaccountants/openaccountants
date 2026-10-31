---
name: ks-cross-border
description: >
  Use this skill whenever asked about Kansas cross-border taxation for tax
  year 2026 — part-year and nonresident Kansas filing (Form K-40 with
  Schedule S allocation), the resident-worldwide-plus-credit structure,
  no reciprocity with neighboring states, no exit tax, and the
  resident-employee withholding rule that follows Kansas residents out of
  state. Trigger on "Kansas nonresident", "Kansas part-year", "Schedule S
  Kansas", "K-40PN", "Kansas reciprocity", "moving to Kansas".
  Source-cited draft; KDOR withholding-residence rule verified 2026-10-28;
  form IDs and credit mechanics not yet confirmed.
version: 0.1
jurisdiction: US-KS
tax_year: 2026
last_updated: 2026-10-29
authored_by: Jeff Watts
review_status: pending_review
trust_label: Accountant-authored
depends_on:
  - ks-income-tax
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kansas cross-border taxation, tax year 2026

> **Source-cited draft.** Built from the KDOR Withholding page, K.S.A. 79-32,110 and the KDOR 2025 individual income tax booklet, read on 2026-10-28. The nonresident-return statute and the credit statutes were not readable this run, so form routing and credit mechanics are listed under Not yet confirmed. No accountant has reviewed it.

Tax year: the calendar year for most individuals. Authority: Kansas Department of Revenue (KDOR). Currency: US dollars. Covers Kansas exposure for nonresidents, part-year residents, and Kansans working out of state; the nonresident path runs through Schedule S Part B in `ks-income-tax`.

See also: `ks-income-tax`, `ks-payroll`, `ks-corporate-income-tax`.

## Who this applies to

- **Kansas residents:** taxed on worldwide income regardless of where services are performed; employers must withhold Kansas tax for Kansas residents "performing services inside or outside of Kansas" (KDOR Withholding page).
- **Nonresidents:** taxed on Kansas-source income; Kansas employers must withhold on nonresidents performing services in Kansas (KDOR Withholding page).
- **Part-year residents:** split-year treatment via allocation on Schedule S (form detail under Not yet confirmed).
- **Entities:** corporations with Kansas-source income file K-120 (see `ks-corporate-income-tax`).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Resident and nonresident rates | 5.20% / 5.58% two-bracket schedule (break at $23,000; $46,000 married filing jointly) | 2026 | [K.S.A. 79-32,110](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html); see `ks-income-tax` |

## The taxable base

| Item | Rule | Source |
|---|---|---|
| Resident base | Worldwide income at Kansas rates | Residence-based withholding rule, [KDOR Withholding page](https://www.ksrevenue.gov/bustaxtypeswh.html) |
| Source rules for remote work | Income sourced where services are performed; Kansas resident remote workers are still Kansas-withheld | KDOR Withholding page |

The nonresident base and allocation, the credit for taxes paid to other states, reciprocity and exit-tax status are listed under Not yet confirmed.

## Deadlines and filing

- Form K-40 (with or without Schedule S): **April 15** for calendar-year filers (April 15, 2026 for 2025 returns; fiscal-year returns the 15th day of the 4th month) ([KDOR 2025 individual income tax booklet](https://www.ksrevenue.gov/incomebook25.html)).
- Employers' withholding remittances for nonresident employees follow the payroll calendar (see `ks-payroll`).

## Penalties and interest

- The Kansas late-filing and late-payment tiers for individuals are listed under Not yet confirmed (see `ks-income-tax`).
- Dual-residency disputes (two states claiming residence) are resolved by negotiated credits or litigation; Kansas has no special penalty for the dispute itself.

## Cross-border points

- **Kansas resident working in Missouri** (classic Kansas City metro pattern): Missouri withholds nonresident tax; Kansas taxes worldwide income. The resident credit for Missouri tax is listed under Not yet confirmed.
- **Nonresident working in Kansas:** Kansas withholds and taxes; the home state may credit Kansas tax (check the home state's rule).
- **No Kansas worldwide-unitary extension for individuals** — the state layer is source- and credit-based.

## Worked examples

Both examples assume a resident credit for tax paid to the other state, capped at the crediting state's tax on the same income. That credit mechanism is not yet confirmed for Kansas; the tax amounts are hypothetical figures showing the mechanics only.

### Example 1: Kansas resident commuting to Missouri

Kansas tax on worldwide income is $4,200; Missouri nonresident tax on the same wages is $3,800. If Kansas credits the full Missouri tax, Kansas collects $400 and the household pays $4,200 in total — the higher of the two states' tax, split $3,800 Missouri + $400 Kansas.

```oa-check
name: KS resident MO commuter credit
inputs:
  ks_tax: 4200
  mo_tax: 3800
steps:
  - credit: min(mo_tax, ks_tax)
  - ks_net: ks_tax - credit
  - combined: mo_tax + ks_net
expected:
  credit: 3800
  ks_net: 400
  combined: 4200
```

### Example 2: nonresident working in Kansas

A Missouri resident earns wages in Kansas; Kansas tax is $2,600 and home-state tax on the same income is $3,100 with a full credit for the Kansas tax. The home state collects $500; the total is $3,100.

```oa-check
name: Nonresident KS work home-state credit
inputs:
  ks_tax: 2600
  home_tax: 3100
steps:
  - credit: min(ks_tax, home_tax)
  - home_net: home_tax - credit
  - combined: ks_tax + home_net
expected:
  credit: 2600
  home_net: 500
  combined: 3100
```

## Ask the client first

1. **Where were services physically performed each day?** It drives source.
2. **Kansas residence status for the whole year or part of it?** It drives K-40 vs the Schedule S split.
3. **Employer withholding:** was Kansas withheld for a resident working out of state (required) or for a nonresident working in Kansas (required)?
4. **Home / work state credit rules:** double-tax relief here comes from credits, not exemptions.

## Sources

| Source | URL | Read on |
|---|---|---|
| KDOR Withholding (residence-based withholding, nonresident rule) | https://www.ksrevenue.gov/bustaxtypeswh.html | 2026-10-28 |
| K.S.A. 79-32,110 (individual rates) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html | 2026-10-28 |
| KDOR 2025 individual income tax booklet (due dates) | https://www.ksrevenue.gov/incomebook25.html | 2026-10-28 |

Not yet confirmed: K-40PN vs K-40 + Schedule S Part B form routing for nonresidents (K.S.A. 79-32,150 page at kslegislature.org/li served only a JS shell); the nonresident base and Schedule S Part B allocation detail; part-year allocation detail; the statute, cap and ordering of the resident credit for taxes paid to other states; that Kansas has no reciprocity agreement with Missouri, Nebraska, Oklahoma, Colorado or any other state; that Kansas imposes no exit or departure tax; whether KDOR honours the federal extension for individuals; the individual late-filing and late-payment penalty tiers under K.S.A. 79-32; military residence-retention (MMRA) treatment in Kansas.

> Contributed by Jeff Watts.

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
