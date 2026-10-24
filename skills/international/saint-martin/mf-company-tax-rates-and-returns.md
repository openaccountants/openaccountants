---
name: mf-company-tax-rates-and-returns
description: >
  French Saint-Martin company-tax reference for taxpayers already established as liable to local corporate income tax. Covers the ordinary rate, conditional small-company profit band, turnover and ownership tests, short-period adjustments, ordinary loss carryforward and separate return and balance-payment deadlines. Includes threshold and arithmetic examples using the official code consolidated through June 2026. Identifies an unresolved instalment-rate cross-reference rather than inventing a payment formula. Residence, territorial entitlement, special gains, group restructuring, incentives and full tax-base adjustments require separate analysis; this is a source-cited draft awaiting independent review, not comprehensive coverage.
version: 0.2
jurisdiction: MF
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# French Saint-Martin: company-tax rates and returns

## Confirm liability before calculating

This Guide assumes the entity and income are within French Saint-Martin's local corporate-tax charge. Article 209(I) refers to profits of enterprises operated in Saint-Martin, specified article 164 B income and profits assigned by applicable tax conventions. A local registration or postal address alone does not establish territorial liability. Entity classification, residence and convention allocation require separate evidence. [CGI article 209, printed pages 211–212](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

The source is the official **5 June 2026 consolidated code**. Its cover says that underlying deliberations are authoritative. A complete check of subsequent amendments and those deliberations remains outstanding. The rates below are the rules in that dated consolidation, not a promise that every later transaction has been fully reviewed.

## Ordinary and reduced rates

Article 219(I) sets the ordinary rate at **20% for financial years beginning on or after 1 September 2014**. Historical rates remain printed immediately above it; do not select a historical rate just because it appears first. Round taxable profit to the nearest euro, with €0.50 upward. [CGI article 219(I), page 233](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

Article 219(I)(b) provides **10% on the first €40,000 of taxable profit per twelve-month period**, subject to all applicable conditions:

- Turnover for the financial year or tax period, annualized where necessary, is **strictly below €7,630,000**.
- Share capital is fully paid.
- At least **75%** is held continuously by individuals or a qualifying company meeting the provision's conditions and at least 75% individual ownership.
- For the parent of an article 223 A group, use aggregate turnover of group members.

The provision has a specific disregard for certain venture-capital/development/innovation holdings where its no-dependence condition is met. Do not simplify complex investment structures to a headline ownership percentage without examining that rule. [CGI article 219(I)(b), page 236](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

The €40,000 band applies for financial years beginning on or after 1 September 2014. Short or long periods require the period adjustment inherent in the twelve-month limit. The reduced rate is conditional; it is not an election available to every locally incorporated company. [Same article](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

## Calculation sequence and examples

1. Establish the locally taxable result from accounts, with supported tax adjustments and any valid loss relief.
2. Separate income subject to special regimes from ordinary profit; this Guide does not calculate long-term gains, participation relief or investment incentives.
3. Record the period length, annualized turnover, paid-up capital and ownership throughout the relevant period.
4. For an eligible twelve-month company with positive ordinary taxable profit P, calculate **10% × min(P, €40,000) + 20% × max(P − €40,000, 0)**. Otherwise apply the ordinary rate to the ordinary taxable profit. Apply statutory rounding and reconcile any separate credits outside this formula.

Illustrations assume an already established ordinary tax base and no credits or special-rate items:

| Case | Calculation | Tax |
|---|---|---:|
| Eligible, €30,000 profit | €30,000 × 10% | €3,000 |
| Eligible, €100,000 profit | €40,000 × 10% + €60,000 × 20% | €16,000 |
| Ineligible, €100,000 profit | €100,000 × 20% | €20,000 |
| Eligible six-month period, €50,000 profit | €20,000 band × 10% + €30,000 × 20% | €8,000 |

For the six-month example, assume turnover annualized to twelve months remains below the limit and all other conditions hold. Turnover exactly **€7,630,000** fails the strict test; an otherwise qualifying ownership percentage exactly **75%** satisfies its minimum. Capital not fully paid fails the test regardless of low turnover. [CGI article 219](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

## Ordinary losses

Article 209(I) treats an ordinary deficit as a charge against the following year's profit, with unused excess carried to subsequent years, subject to the alternative election referenced in article 220 quinquies. This does not automatically establish survival through a restructuring or activity change. Article 209(II) imposes specific approval conditions on certain merger/transfer cases. Keep a year-by-year loss schedule and verify the relevant continuity rules before offsetting losses. [CGI article 209](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

## Returns and payments are separate

Article 223(1) requires the profit/loss declaration within **three months of year-end**. For a 31 December close or a year without a closing, a regulation fixes the date, no later than the **second working day after 1 May**. Confirm the applicable annual date instead of substituting an unverified calendar date. [CGI article 223, page 241](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

Article 1668 specifies quarterly instalment dates of **15 March, 15 June, 15 September and 15 December** and exempts newly created or newly subject companies for the first financial year/first tax period described there. Its balance rule is the **15th of the fourth month after year-end**, or 15 May of the following year if no financial year closes during the year. [CGI article 1668, pages 472–473](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

**Unresolved instalment issue:** article 1668(1) refers to the third paragraph of article 219(I), while the consolidation places the older 22.22% rate there and the later 20% rate in the following paragraph. Obtain the operative payment guidance or underlying amending text before computing instalments. The final-tax examples above apply the explicit later article 219 ordinary rate; they do not settle this cross-reference.

## Filing channel and nil results

The 2026 handbook confirms annual result reporting and requires results returns even without turnover. Its company-tax section corroborates the 10%/20% rates and balance timing, but supplies no calculation resolving the instalment cross-reference above. [Business handbook, pages 8 and 11](https://www.impots-saint-martin.fr/files/file/News/20%20PAGES%20LIVRET%20FISCAL%20COLLECTIVITE.pdf).

The January 2026 notice routes results-return PDFs to `cfip.sxm-pole.fiscal@dgfip.finances.gouv.fr`; IS instalment declarations go to `cfip.sxm.declarations-professionnels@dgfip.finances.gouv.fr`. It requires bank transfers, payment evidence and matching NIF/tax/year references. Use a single recipient without copying other tax offices or agents. The October notice says forms must be downloaded; deadlines remain unchanged. [Official notices](https://www.impots-saint-martin.fr/).

Reconcile the result package, payment reference and supporting computation before submission. Obtain the current prescribed forms and bank instructions from the official site; do not send a result return to the instalment mailbox merely because both concern IS.

## Self-checks and scope limits

Confirm MF rather than Dutch Sint Maarten, local liability, financial-year opening date, period length, strict turnover boundary, continuous ownership, paid-up capital, special income and loss history. Keep declaration timing separate from instalment and balance dates. Retrieve the current official filing channel and forms before submission.

Source-cited draft awaiting independent source and professional review. Detailed residence, tax-base adjustments, distributions, related-party rules, special gains, incentives and the instalment ambiguity remain outside the completed computation scope. This is not a comprehensive company-tax pack or individualized filing advice.

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
