---
name: fi-tax-overview
description: >
  Find the existing Finland tax skills for 2026 preparation and identify their
  scope and review limits. Routes individual and corporate income tax, VAT, YEL,
  payroll, transfer-pricing documentation, cross-border residence, prepayments,
  country-by-country reporting and property-transfer questions to the relevant
  source skill. Use when a Finland tax question needs classification before any
  calculation, when checking which workpaper applies, or when reconciling the
  country pack's partial coverage. This overview supplies no standalone tax
  calculation of its own or current formation fee, and the country remains a source-cited
  draft with source-review evidence in the pack README; professional attestation is separate.
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.4
category: international
---

# Finland tax overview v0.4

## Start with the question and the taxpayer

Use the existing topic skill and its source/read-date record before applying a figure. Distinguish tax residence, legal entity, income or transaction category and the relevant year. The [pack README](README.md) records coverage and remaining gaps; the revised ordinary pack’s review evidence is recorded there.

| Question | Existing preparation skill | Remaining boundary |
|---|---|---|
| Resident individual tax or sole-trader income | [Individual income tax](fi-income-tax.md) | Includes deductions, mainland/Åland components, pensions, rent/gains and business allocation; special regimes are scoped separately. |
| Company profits, losses or tax return | [Corporate income tax](fi-corporate-income-tax.md) | Use the book-to-tax, interest, group, loss and participation calculations; corporate cross-border is linked below. |
| VAT classification and return | [VAT return](finland-vat-return.md) | Ordinary rates, EU/import, Åland and construction routes; special schemes require separate work. |
| Self-employed pension insurance | [YEL](fi-yel-social.md) | Establish eligibility and provider decisions; this does not cover all social insurance. |
| Employee deductions and employer reporting | [Payroll](fi-employer-payroll.md) | Includes benefit valuation and statutory employee/employer insurance bases; coverage facts control. |
| Related-party documentation | [Transfer pricing](fi-transfer-pricing.md) | Documentation does not establish an arm's-length price. |
| Arrival/departure and foreign tax relief | [Individual cross-border residence](fi-individual-cross-border-residence.md) | Includes source income, source/progressive tax and foreign relief; read the actual treaty for country-specific outcomes. |
| Income-tax payments during the year | [Prepayments](fi-prepayments.md) | The issued decision and applicable taxpayer route control. |
| Multinational reporting | [CbCR](fi-country-by-country-reporting.md) | Threshold, filer role and notification are separate checks. |
| Corporate cross-border | [Corporate cross-border](fi-corporate-cross-border-tax.md) | Residence, PE, source withholding, credit and exit; treaty conditions remain case-specific. |
| Annual property ownership | [Annual real-estate tax](fi-annual-real-estate-tax.md) | Uses preceding-year values and actual municipal rates, including Åland deviations. |
| Acquisition of real estate or housing-company shares | [Property-transfer tax](fi-property-transfer-tax.md) | Acquisition base, debt, earnouts, filing and sanctions; annual tax and rent/gains use separate linked computations. |
| Entity formation | [Formation draft](fi-company-formation.md) | Current PRH setup/fee and selected statutory checks; broader entity, accounting and specialist review remain open. |

## Finland at a glance (2026)

| Point | 2026 position | Where it is computed |
|---|---|---|
| Levels of tax | State income tax, municipal tax and, for church members, parish tax; administered by the Finnish Tax Administration (Vero), e-services in MyTax (OmaVero) | [Individual income tax](fi-income-tax.md) |
| Tax year and currency | Calendar year; euro | [Individual income tax](fi-income-tax.md); [Corporate income tax](fi-corporate-income-tax.md) |
| Basis | Residents on worldwide income; non-residents on Finnish-source income | [Individual cross-border residence](fi-individual-cross-border-residence.md); [Income Tax Act 1535/1992, sections 9–10][ita] |
| Individual rates | Progressive state tax on earned income plus municipal/parish tax; capital income 30% up to EUR 30,000, 34% above | [Individual income tax](fi-income-tax.md); [Income Tax Act, section 124][ita] |
| Corporate rate | 20% | [Corporate income tax](fi-corporate-income-tax.md); [Income Tax Act, section 124][ita] |
| VAT rates | 25.5% general; 13.5% reduced from 1 January 2026 (formerly 14%); 10% newspapers/magazines | [VAT return](finland-vat-return.md); [VAT Act 1501/1993, sections 84–85a][vat] |
| Individual return | Review and correct the pre-completed return in MyTax by the date allocated on it | [Individual income tax](fi-income-tax.md) |
| Corporate return | Within four months after the end of the calendar month in which the financial period ends | [Corporate income tax](fi-corporate-income-tax.md) |

## Workpaper handoff

Record the facts, selected skill/version, source passages, assumptions, calculations and unresolved points together. Separate preparation from a return submitted or a payment made. File count, executable arithmetic and an HTTP success response do not establish country completeness or named accountant review.

## Sources and review limits

This router was reconciled to the existing Finland source pack on 26 October 2026. Tax rules and official URLs belong to the linked topic skills; no independent legal conclusion is supplied by this index. Earlier 2025 summary figures remain in Git history and must not substitute for current topic-source checks.

The independent source review, corrections and remaining gaps are recorded in the [country README](README.md#evidence-and-next-action). See [OWNERS.md](../../../OWNERS.md) and [country issue #392](https://github.com/openaccountants/openaccountants/issues/392) for allocation and progress.

[ita]: https://www.finlex.fi/fi/lainsaadanto/1992/1535
[vat]: https://www.finlex.fi/fi/lainsaadanto/1993/1501

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

## Sources and review limits

This router was reconciled to the existing Finland source pack on 26 October 2026. Tax rules and official URLs belong to the linked topic Guides; no independent legal conclusion is supplied by this index. Earlier 2025 summary figures remain in Git history and must not substitute for current topic-source checks.

The independent source review, corrections and remaining gaps are recorded in the [country README](README.md#evidence-and-next-action). See [OWNERS.md](../../../OWNERS.md) and [country issue #392](https://github.com/openaccountants/openaccountants/issues/392) for allocation and progress.
