---
name: sx-wage-tax-tables
description: "Sint Maarten wage-tax table reference for 2026 based on Annex II to AB 2026 number 11. Covers pay-period selection, the column-thirteen wage-tax base, exact nil-withholding thresholds, the embedded basic credit and the top-of-table calculation. Includes the official low-pay and high-pay examples and distinguishes extraordinary-payment rates from normal salary withholding. Explains why the source’s conditional AOV/AWW illustration does not establish a complete contribution regime. Applies to Dutch Sint Maarten only. Benefits, coverage, employer registration, complete reporting and social-insurance rates need separate verification. Independent accountant review remains outstanding."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sx-wage-tax-tables"
  jurisdiction: "SX"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Sint Maarten: 2026 wage-tax tables

## Start with the correct payroll base

[AB 2026 no. 11, article 2](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Regeling%20vaststelling%20inkomsten-%20en%20loonbelastingtabellen%202026.pdf) establishes Annex II's wage and extraordinary-payment tables. [Annex II](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20II%20TABEL%20LOONBELASTING%202026.pdf) applies to pay periods from 1 January 2026 and defines the table input as the wage-tax base in **column 13 of the wage statement**. It is not automatically the employee's gross cash salary.

Select the table for the actual pay period. Annex II contains half-day, day, week, quincena, month and quarter tables. The basic credit is already included; do not deduct it again from the table output. These rules are for Dutch Sint Maarten, not the French side of the island.

## Nil-withholding override

Annex II specifies no wage-tax withholding when column 13 is no greater than the amount for the applicable period:

| Source table | Maximum base for nil withholding, Cg |
|---|---:|
| Half-day | 52.46 |
| Day | 104.93 |
| Week | 524.64 |
| Quincena | 1,049.28 |
| Month | 2,273.44 |
| Quarter | 6,820.32 |

The annual figure stated is Cg 27,281.28. Use the actual published period threshold rather than inventing a four-week month or rounding the annual amount into a different weekly figure. For all other cases the normal tables apply. [Annex II, Loonbelasting grondslagen 2026](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20II%20TABEL%20LOONBELASTING%202026.pdf).

## Official low-pay illustration

The annex gives this monthly example:

| Step | Cg |
|---|---:|
| Gross pay | 2,473.16 |
| Acquisition-cost deduction in the example | (41.67) |
| Intermediate amount | 2,431.49 |
| Employee AOV/AWW deduction in the example | (158.05) |
| Column 13 base | 2,273.44 |
| Wage tax after the explicit nil-withholding rule | 0.00 |

The annex notes that the ordinary table would show Cg 85.62, but the nil rule controls at this base. Its AOV/AWW footnote explicitly assumes the 2026 employee share is 6.5%. Therefore, this is a reproduction of the official tax-table example, not independent proof of all contribution rates, income definitions or ceilings. Establish contribution coverage and permitted deductions separately before applying the example to an employee. [Annex II, example and footnote](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20II%20TABEL%20LOONBELASTING%202026.pdf).

## Above the final table amount

Annex II directs withholding at 47.5% on the amount above the final table entry. Its monthly example uses a **wage-tax base** of Cg 15,000:

- Final table base: Cg 14,162.33; corresponding tax Cg 3,933.16.
- Excess: Cg 837.67; tax at 47.5%, rounded to cents, Cg 397.89.
- Total wage tax: Cg 4,331.05.

Do not apply 47.5% to the entire Cg 15,000. The source applies that rate only to the excess above the table endpoint. [Annex II, introductory example](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20II%20TABEL%20LOONBELASTING%202026.pdf).

## Extraordinary payments

Annex II has a separate table for bijzondere beloningen, with income thresholds and rates from 0% to 47.5%. The top category starts at Cg 179,500. This is not permission to apply the top rate to every normal monthly salary or every bonus. Establish the payment's classification and the correct income measure under the wage-tax rules before selecting that table. This batch does not supply an unverified prior-year-income formula.

## Payroll controls and open work

As recommended working papers, retain the pay-period choice, column 13 computation, applicable threshold or table row, deduction evidence and tax result. Reconcile these to the employee wage statement and remittance records. A zero wage-tax result does not establish zero AOV/AWW, medical insurance or other payroll obligations.

Checked 22 October 2026 from downloaded regulation and Annex II; the threshold/example page was visually inspected. Full payroll coverage, benefits in kind, social contributions, registration, remittance, annual reporting, later changes and independent accountant review remain open. This draft does not provide a complete payroll implementation.

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sx-wage-tax-tables` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sx-wage-tax-tables. If neither is available, confirm every figure against the official source pages cited above before relying on it.
