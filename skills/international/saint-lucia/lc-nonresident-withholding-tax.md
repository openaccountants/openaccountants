---
name: lc-nonresident-withholding-tax
description: >
  Saint Lucia non-resident withholding reference covering payment classification, gross-basis rates, treaty directions, accrual timing, remittance, certificates and annual reconciliation. Distinguishes interest and discount from other covered payments and identifies residential-rental, exemption and permanent-establishment boundaries. Flags older brochure terminology and incomplete later-order and treaty verification.
jurisdiction: LC
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: "0.3"
verified_by: pending
---

# Saint Lucia: non-resident withholding tax

## Classify the payment before selecting a rate

Section 76 and Schedule 3 govern covered payments to non-residents, including payments by a non-resident company's branch to its overseas head office, branch or associate. Payment to an address outside Saint Lucia creates a rebuttable non-residence presumption; retain the recipient's residence evidence. Part 4 exempt income and expenses incurred to generate income sourced outside Saint Lucia are excluded by section 76(4). Do not treat every foreign invoice as automatically taxable or exempt. [Section 76](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/section-76).

The following rates are in the **2023 revised-law edition**, subject to section 60 treaty provisions and Schedule 3 paragraph 2. Full subsequent-order verification remains pending.

| Covered payment | Schedule 3 rate on gross payment |
|---|---:|
| Interest or discount | **15%** |
| Royalty or management charge | **25%** |
| Commission or fee outside the employment withholding provision | **25%** |
| Covered trust distribution, insurance premium excluding reinsurance, or other covered income payment | **25%**, subject to the Schedule's character and scope rules |

Schedule 3 excludes dividends, specified lease/premium/licence payments and annuities or periodic alimony/maintenance payments. These exclusions from this Schedule do not establish that the receipt is exempt from all income tax. The Schedule separately addresses independent personal services performed in Saint Lucia outside a local permanent-establishment business. Its business/employment boundary requires checking the actual activity. [Schedule 3, paragraphs 1–3](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/schedule-3).

For **residential accommodation rent accruing to a non-resident**, paragraph 2(d) directs the reader to Parts 5 and 6 and Schedule 5. Do not substitute the generic 25% gross-payment calculation for that explicit rule. Likewise, retain the underlying character when assessing trust income rather than assuming every trust payment has the same treatment. [Schedule 3](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/schedule-3).

## Treaty treatment and older summaries

Section 76(3) permits the Comptroller to direct a lower deduction where the recipient resides in a treaty country and the relevant agreement provides a lower withholding rate. Establish the treaty, residence and applicable payment article, and the required direction, before applying relief. This draft does not certify a blanket CARICOM rate. [Section 76(3)](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/section-76).

An older IRD “Know Your Taxes” brochure describes 15% by reference to CARICOM nationals, whereas the revised Schedule expressly assigns 15% to interest or discount. The brochure also contains other historical figures. Use the statutory payment classification and separately verify treaty relief; citizenship alone is not the residence evidence described in section 76(3). [Older brochure](https://irdstlucia.gov.lc/images/Documents/Publications/Know_Your_Taxes_view.pdf); [Schedule 3](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/schedule-3).

## Deduction, timing and examples

Deduct from the **gross amount**. The Schedule describes the resulting tax as final liability for the covered income, within its stated scope. If an accrual-basis business expenses a covered amount but leaves it unpaid, paragraph 1(3) requires deduction and accounting as though paid on the last day of that income year. [Schedule 3, paragraphs 1–3](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/schedule-3).

For a covered EC$10,000 gross royalty at 25%, withhold EC$2,500 and pay EC$7,500 to the recipient. For covered EC$10,000 gross interest at 15%, withhold EC$1,500 and pay EC$8,500. These assume no exemption or treaty reduction. Net-of-tax contract gross-up treatment needs separate review.

Section 116 requires payment to the Comptroller **within 15 days after the month-end** in which tax was deducted **or deductible**. Failing to deduct does not defer that deadline. Imported-services VAT is a separate obligation; use the [imported-services VAT Guide](lc-imported-services-vat.md), not its payment timing for withholding. [Section 116](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/section-116).

## Certificates and reconciliation

Give the payee a certificate recording the gross payment and tax deducted. Keep calendar-year records of payment nature, gross amounts by recipient and deductions available for examination for the Schedule's six-year period; check any longer applicable retention requirement. With each section 116 remittance, submit the approved return and copies of deduction certificates. Within **two months after each calendar year ends**, or an allowed extension, file the annual totals of deductions and remittances and account for any shortfall. [Schedule 3, paragraphs 4–5](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/schedule-3).

Failure to deduct makes the payer personally liable for the undeducted tax within the section 116 period, in addition to potential penalties. The Schedule provides recovery from the payee for tax subsequently paid by the payer. In contrast, section 117 makes late-deduction interest the payer's own debt, unrecoverable from the payee. Its rate depends on the prime rate or a ministerial order; this draft does not certify the current rate or amnesty treatment. [Schedule 3, paragraph 6](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/schedule-3); [section 117](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/section-117).

## Remaining checks

Later amendments and orders, exemptions for each income type, treaty and permanent-establishment analysis, current forms/channels, interest and penalties, and independent review remain outstanding. These rules do not establish comprehensive country coverage.

## Executable check of the existing examples

These checks reproduce the gross-payment examples above. They do not resolve the stated eligibility, amendment or procedural gaps.

```oa-check
name: Saint Lucia existing royalty and interest examples
inputs:
  gross: 10000
  royalty_rate: 0.25
  interest_rate: 0.15
steps:
  - royalty_tax: gross * royalty_rate
  - royalty_net: gross - royalty_tax
  - interest_tax: gross * interest_rate
  - interest_net: gross - interest_tax
expected:
  royalty_tax: 2500
  royalty_net: 7500
  interest_tax: 1500
  interest_net: 8500
```

## Disclaimer

Source-cited research draft, not accountant attestation.

## Sources


The following links collect the sources already cited above. Their applicable versions, statutory locators and unresolved limitations remain as stated in the body; this list is not a new source verification.

- [Section 76](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/section-76)
- [Schedule 3, paragraphs 1–3](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/schedule-3)
- [Older brochure](https://irdstlucia.gov.lc/images/Documents/Publications/Know_Your_Taxes_view.pdf)
- [Section 116](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/section-116)
- [section 117](https://attorneygeneralchambers.com/laws-of-saint-lucia/income-tax-act/section-117)
