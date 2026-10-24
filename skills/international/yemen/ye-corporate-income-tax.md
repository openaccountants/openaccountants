---
name: ye-corporate-income-tax
description: >
  Yemen corporate income-tax research draft based on Law 17/2010 as reproduced by the Public Prosecution. Covers ordinary and selected special rates, deductible expenditure, qualifying losses, returns and records, with two conditional computations. Flags the separate Sana'a-issued Law 8/2020 and unresolved administration-specific applicability. Not a certified current nationwide tax schedule or complete country pack.
jurisdiction: YE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://agoyemen.net/lib_details.php?id=198"
    title: "Yemen Public Prosecution, Income Tax Law 17/2010, articles 13, 19, 63, 88, 95–96 and 162"
    as_of: "2026-10-22"
  - url: "https://tax.gov.ye/8-2021/"
    title: "Tax and Customs Authority, Sana'a-issued Law 8/2020 adding article 160(c)"
    as_of: "2026-10-22"
---

# Yemen: corporate income-tax framework and filing

## Establish the administration and law first

This Guide translates selected provisions of Law 17/2010 reproduced by the Public Prosecution. It does not establish that an unamended 2010 text governs every 2026 taxpayer. Identify the actual business location, administering tax office, period, entity classification and applicable amendments before computing a live liability. The application of measures across different administrations has not been reconciled. No nationwide operational uniformity is asserted. [Law 17/2010](https://agoyemen.net/lib_details.php?id=198).

The Tax and Customs Authority publishes Law 8/2020, issued in Sana'a on 3 May 2020 by the President of the Supreme Political Council. It adds article 160(c), providing specified small/micro-business, employee and small-property-tax exemptions and special reporting obligations. It is not proof of the same treatment elsewhere. Its business exemption has an annual YER20 million turnover ceiling and named exclusions, including foreign natural/legal taxpayers, imports, exchange/remittances, supplies/contracting and specified professions. This Guide neither applies that exemption nor reproduces the old small-business schedule as universally current. Full eligibility, territorial application and later measures remain separate work. [Law 8/2020, article 1](https://tax.gov.ye/8-2021/).

## Ordinary and special rates

Article 63(a) sets **20%** for legal-person business/professional taxable income, without an exemption allowance, subject to its special categories and the separately classified small enterprises. It also covers non-resident natural persons, but this Guide's examples concern companies. [Article 63](https://agoyemen.net/lib_details.php?id=198).

Article 63(b) specifies **35%** for oil/gas, mining/minerals and concession companies, subject to the constitutionally approved concession/production-sharing agreements identified there. Article 63(c) preserves higher contractual rates above 35%. Article 63(d) specifies **50%** for mobile telecommunications operators; article 63(e) specifies **35%** for international telecommunications and cigar/cigarette production or import. Investment-project treatment under article 64 requires separate eligibility analysis. A business description is not enough to choose a special rate. [Articles 63–64](https://agoyemen.net/lib_details.php?id=198).

## Profit base and losses

Article 13(a) requires deductible costs to relate to the commercial, industrial or service activity, be real, and be supported by documents, subject to the limited rule for expenses customarily lacking documents. Its detailed categories and limits must be checked before deduction; an accounting expense is not automatically a tax expense. This draft does not calculate financing limits, depreciation or incentives. [Article 13](https://agoyemen.net/lib_details.php?id=198).

Article 19 requires the loss-year return to be approved by a licensed legal accountant and supported by regular books/accounts. The loss is deducted in the following year; unused loss continues through the fifth year from the start of deduction, with no carry beyond that fifth year. The rule does not apply to company losses in the tax year and earlier years where ownership of its capital changes by **100%**. Do not use a loss without checking its origin, period, supporting return, remaining balance and ownership history. [Article 19](https://agoyemen.net/lib_details.php?id=198).

## Returns, payment and attachments

Article 95(a) requires an annual return by **30 April** for the preceding tax year, with payment at the same time. Article 95(b) gives taxpayers using an overlapping financial year until the end of the fourth month after that year ends. The law also describes early-filing/payment discounts; no discount is assumed here. Current administrative extensions and payment channels have not been verified. [Article 95](https://agoyemen.net/lib_details.php?id=198).

Article 96 distinguishes large taxpayers' financial statements from medium taxpayers' income statement supported by regular accounts. Large-taxpayer returns, including exempt large taxpayers, require certification by an approved, licensed legal accountant with a valid tax card; public/mixed-sector units have the specified central-audit certification rule. Returns must be signed by the taxpayer or lawful representative. Investment/other exempt taxpayers remain subject to the baseline article 96(b) filing rule, but later special exemptions and their reporting rules must be reconciled rather than ignored. [Article 96](https://agoyemen.net/lib_details.php?id=198).

Article 88 requires books/records under article 86 to be kept for **ten years following the financial year of the entry**. Article 162 moves a return or objection deadline falling on an official holiday to the first working day after that holiday; it does not by itself rewrite every payment deadline. [Articles 88 and 162](https://agoyemen.net/lib_details.php?id=198).

## Example 1: ordinary company with eligible loss

Assume ordinary 20% classification, YER10 million established taxable profit before loss relief, and an eligible YER2 million carried loss satisfying article 19, with no ownership restriction, special regime, credit or discount. Taxable profit is YER8 million and tax YER1.6 million. These assumptions require separate proof.

```oa-check
name: Yemen ordinary company with qualifying carried loss
inputs:
  profit_before_loss: 10000000
  eligible_loss: 2000000
  rate: 0.20
steps:
  - taxable_profit: profit_before_loss - eligible_loss
  - tax: taxable_profit * rate
expected:
  taxable_profit: 8000000
  tax: 1600000
```

## Example 2: loss unavailable after complete ownership change

Assume the same YER10 million profit and 20% company rate, but the ownership change is established to fall within article 19(b), making the carried loss unavailable. Tax is YER2 million, YER400,000 more than the first example. This does not infer a restriction for a smaller ownership change or resolve complex reorganisations.

```oa-check
name: Yemen loss restriction on established complete ownership change
inputs:
  taxable_profit_without_loss: 10000000
  rate: 0.20
  comparator_tax_with_loss: 1600000
steps:
  - tax_without_loss: taxable_profit_without_loss * rate
  - difference: tax_without_loss - comparator_tax_with_loss
expected:
  tax_without_loss: 2000000
  difference: 400000
```

## Intake and outstanding work

Obtain operating locations and administering office, legal form, activities/concessions, year end, accounting adjustments, audited loss returns and ownership history, investment approvals, exemption claims, payments and notices. Still unresolved: current administration-specific amendment chain, residence/source/permanent establishment, full deductions, depreciation, sector regimes, credits, withholding, registration operations, appeal procedures and penalties. This is not complete corporate coverage or professional attestation.

## Sources

- [Public Prosecution: Law 17/2010](https://agoyemen.net/lib_details.php?id=198), exact articles cited above, retrieved 22 October 2026. Arabic controls over this research translation.
- [Tax and Customs Authority: Law 8/2020](https://tax.gov.ye/8-2021/), retrieved 22 October 2026; its issuing authority and geographic applicability must be evaluated for the actual case.

## Disclaimer

Source-cited draft. Verify the governing administration, applicable law, facts and current procedures before filing or paying.
