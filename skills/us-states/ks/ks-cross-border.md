---
name: ks-cross-border
description: >
  Use this skill whenever asked about Kansas cross-border taxation for tax
  year 2026, part-year and nonresident Kansas filing (Form K-40 with
  Schedule S allocation), the resident-worldwide-plus-credit structure,
  no reciprocity with neighboring states, no exit tax, and the
  resident-employee withholding rule that follows Kansas residents out of
  state. Trigger on "Kansas nonresident", "Kansas part-year", "Schedule S
  Kansas", "K-40PN", "Kansas reciprocity", "moving to Kansas".
  Source-cited draft; KDOR withholding-residence rule verified 2026-10-28;
  form IDs and credit mechanics not yet confirmed.
jurisdiction: US-KS
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.2
depends_on:
  - ks-income-tax
---

# Kansas cross-border taxation, tax year 2026

> **Source-cited draft.** Built from the KDOR Withholding page, K.S.A. 79-32,110, 79-32,111, 79-3221 and 79-3228 and the KDOR 2025 individual income tax booklet, read on 2026-10-28 and 2026-10-29. No accountant has reviewed it.

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
| Resident rates | 5.20% / 5.58% two-bracket schedule (break at $23,000; $46,000 married filing jointly) | 2026 | [K.S.A. 79-32,110(a)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html); see `ks-income-tax` |
| Nonresident tax | Tax computed as if a resident, multiplied by modified Kansas source income / Kansas adjusted gross income | 2026 | [K.S.A. 79-32,110(b)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html) |
| Resident credit for tax paid to another state | Income tax paid to another state on income sourced there and included in Kansas AGI; capped at Kansas tax x (Kansas AGI from that state while resident / total Kansas AGI) | 2026 | [K.S.A. 79-32,111(a)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0111.html) |

## The taxable base

| Item | Rule | Source |
|---|---|---|
| Resident base | Worldwide income at Kansas rates | Residence-based withholding rule, [KDOR Withholding page](https://www.ksrevenue.gov/bustaxtypeswh.html) |
| Source rules for remote work | Income sourced where services are performed; Kansas resident remote workers are still Kansas-withheld | KDOR Withholding page |

| Nonresident base | Kansas tax on all income as if resident, scaled by the Kansas-source share (K.S.A. 79-32,110(b)) | K.S.A. 79-32,110(b) |
| Foreign-country tax | The resident credit for tax paid to a foreign country is limited to that tax less the federal credit allowed for it | K.S.A. 79-32,111(a) |

The Schedule S Part B line detail, reciprocity and exit-tax status are listed under Not yet confirmed.

## Deadlines and filing

- Form K-40 (with or without Schedule S): the 15th day of the 4th month after year end, so **April 15** for calendar-year filers ([K.S.A. 79-3221(b)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0021.html); [KDOR 2025 individual income tax booklet](https://www.ksrevenue.gov/incomebook25.html)). A return filed by the federal due date including an IRS extension is on time (K.S.A. 79-3221(c)(3)).
- Employers' withholding remittances for nonresident employees follow the payroll calendar (see `ks-payroll`).

## Penalties and interest

- Late filing or late payment: 1% of the unpaid tax a month, up to 24%, plus interest ([K.S.A. 79-3228(c)](https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html); see `ks-income-tax`).
- Dual-residency disputes (two states claiming residence) are resolved by negotiated credits or litigation; Kansas has no special penalty for the dispute itself.

## Cross-border points

- **Kansas resident working in Missouri** (classic Kansas City metro pattern): Missouri withholds nonresident tax; Kansas taxes worldwide income and credits the Missouri tax up to the K.S.A. 79-32,111(a) proportional cap.
- **Nonresident working in Kansas:** Kansas withholds and taxes; the home state may credit Kansas tax (check the home state's rule).
- **No Kansas worldwide-unitary extension for individuals**, the state layer is source- and credit-based.

## Worked examples

Kansas amounts use the K.S.A. 79-32,110 rates; client facts and the other state's tax are hypothetical.

### Example 1: Kansas resident with Missouri wages (credit cap binds)

A single Kansas resident has Kansas taxable income of $70,000. Kansas tax is $1,196 + 5.58% x $47,000 = $3,818.60. Kansas AGI is $85,000, of which $60,000 is Missouri wages; Missouri tax on those wages is $2,900. The credit cap is $3,818.60 x 60,000 / 85,000 = $2,695.48, so the credit is $2,695.48, not the full $2,900, and Kansas tax after credit is $1,123.12 (K.S.A. 79-32,111(a)).

```oa-check
name: KS resident credit for Missouri tax, proportional cap
inputs:
  ks_ti: 70000
  ks_agi: 85000
  mo_income: 60000
  mo_tax: 2900
steps:
  - ks_tax: 1196 + (ks_ti - 23000) * 0.0558
  - cap: ks_tax * mo_income / ks_agi
  - credit: min(mo_tax, cap)
  - ks_net: ks_tax - credit
expected:
  ks_tax: 3818.60
  cap: 2695.48
  credit: 2695.48
  ks_net: 1123.12
```

### Example 2: nonresident with Kansas wages

A single Missouri resident has the same $70,000 taxable income and $85,000 Kansas AGI as computed for Kansas, of which $40,000 is Kansas-source wages. Kansas tax as if resident is $3,818.60; the nonresident tax is $3,818.60 x 40,000 / 85,000 = $1,796.99 (K.S.A. 79-32,110(b)).

```oa-check
name: KS nonresident tax by source ratio
inputs:
  ks_ti: 70000
  ks_agi: 85000
  ks_source: 40000
steps:
  - tax_as_resident: 1196 + (ks_ti - 23000) * 0.0558
  - nonresident_tax: tax_as_resident * ks_source / ks_agi
expected:
  tax_as_resident: 3818.60
  nonresident_tax: 1796.99
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
| K.S.A. 79-32,110 (individual rates; (b) nonresident ratio) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0110.html | 2026-10-29 |
| K.S.A. 79-32,111 (resident credit for tax paid to another state) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0111.html | 2026-10-29 |
| K.S.A. 79-3221 (due date, federal extension) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0021.html | 2026-10-29 |
| K.S.A. 79-3228 (penalties) | https://ksrevisor.gov/statutes/chapters/ch79/079_032_0028.html | 2026-10-29 |
| KDOR 2025 individual income tax booklet (due dates) | https://www.ksrevenue.gov/incomebook25.html | 2026-10-28 |

Not yet confirmed: K-40PN vs K-40 + Schedule S Part B form routing for nonresidents (K.S.A. 79-32,150 page at kslegislature.org/li served only a JS shell); the Schedule S Part B line detail; part-year allocation detail; the ordering of the resident credit against other credits; that Kansas has no reciprocity agreement with Missouri, Nebraska, Oklahoma, Colorado or any other state; that Kansas imposes no exit or departure tax; military residence-retention (MMRA) treatment in Kansas.

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
