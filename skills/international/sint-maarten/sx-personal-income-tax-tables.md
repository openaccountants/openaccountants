---
name: sx-personal-income-tax-tables
description: >
  Sint Maarten personal income tax calculation reference for calendar year 2026. Uses enacted regulation AB 2026 number 11 and its income-tax annex to explain the low-income override, marginal bands, lookup-table interpolation and basic credit already embedded in published amounts. Reproduces verified worked examples and distinguishes taxable income from salary or turnover. Highlights rounding risks when rebuilding the schedule and avoids assuming eligibility for child, elderly or sole-earner supplements. Applies to Dutch Sint Maarten, not French Saint-Martin. Residence, deductions, filing, credits eligibility and complete amendment reconciliation require further work. Independent accountant review is pending.
jurisdiction: SX
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Sint Maarten: 2026 personal income-tax tables

## Source and scope

[AB 2026 no. 11](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Regeling%20vaststelling%20inkomsten-%20en%20loonbelastingtabellen%202026.pdf), dated 16 March and published 18 March 2026, establishes the 2026 income and wage-tax tables. Article 1 adopts Annex I for income tax; article 3 repeals the 2025 table regulation. Article 4 provides for entry into force with retrospective effect to 1 January 2026, subject to the constitutional-review provisions stated there.

This Guide explains the official 2026 calculation on an **already determined taxable-income figure**. It does not determine residence, income source, allowable deductions or special tax treatment. Amounts use the source's Cg currency notation. Dutch Sint Maarten (SX) and French Saint-Martin (MF) are separate jurisdictions.

## Apply the low-income rule first

[Annex I, introductory instructions](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20I%20TABEL%20INKOMSTENBELASTING%202026.pdf) states that no income tax is levied when taxable income is **Cg 27,281.28 or less** from 1 January 2026. Otherwise, the normal 2026 table applies.

This is not an instruction to deduct Cg 27,281.28 from everyone's income. It is also not safe to ignore the rule because the detailed lookup table shows positive amounts below that threshold. For example, the printed lookup row at Cg 27,248 shows Cg 1,025, but the express low-income rule makes the tax nil at that income.

## Ordinary marginal schedule

Annex I gives the following bands. Boundary descriptions below follow its greater-than / less-than-or-equal columns.

| Taxable income above Cg | Up to and including Cg | Marginal percentage |
|---:|---:|---:|
| 0 | 36,576 | 12.5% |
| 36,576 | 54,864 | 20% |
| 54,864 | 76,200 | 26.25% |
| 76,200 | 114,297 | 33.75% |
| 114,297 | 161,540 | 40% |
| 161,540 | No upper limit shown | 47.5% |

Use these to understand the marginal rates, together with the separate low-income rule. For a return computation, use the published lookup procedure and values rather than reconstructing cumulative tax from rounded band thresholds. The annex's published cumulative amounts contain cent differences that a simple rounded-threshold formula would miss. [Annex I, schedule and detailed table](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20I%20TABEL%20INKOMSTENBELASTING%202026.pdf).

## Lookup-table method and examples

The introductory instructions say to take the published tax amount at the relevant table income and add the residual income multiplied by the listed percentage. The examples below are in Annex I and were checked arithmetically:

| Taxable income | Published anchor | Tax at anchor | Residual calculation | Total |
|---|---:|---:|---:|---:|
| Cg 42,360 | 42,348 | 3,345.40 | 12 × 20% = 2.40 | 3,347.80 |
| Cg 169,958 | 169,948 | 47,197.96 | 10 × 47.5% = 4.75 | 47,202.71 |

The source expressly states that the **basic credit is already deducted** in these calculated amounts. Do not deduct it again. Annex I lists Cg 2,381 for the basic amount; its detailed table is labelled as including the basic credit. Other eligible supplements still need to be deducted, but the resulting tax cannot be below zero. [Annex I](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20I%20TABEL%20INKOMSTENBELASTING%202026.pdf).

## Supplements need eligibility evidence

The annex lists sole-earner, child and elderly supplements, but a rate table alone does not establish who qualifies, how competing claims are assigned or which child/elderly category applies. Obtain the applicable statutory conditions and facts before applying those amounts. This Guide deliberately does not convert a list of supplement figures into automatic relief.

## Verification and remaining work

Checked 22 October 2026. Official regulation and Annex I downloaded; introductory examples and nil-tax instruction visually checked. The government host's expired certificate required a one-off certificate-verification bypass for these public PDF downloads; the indexed official titles and matching PDF content were also checked. The alternate www1 host returned an under-construction page.

Residence, taxable scope, deductions, filing obligations, supplement eligibility, constitutional-review status and the complete amendment history still require reconciliation before merge. Independent accountant review has not occurred. This is a source-cited calculation draft, not comprehensive country coverage.
