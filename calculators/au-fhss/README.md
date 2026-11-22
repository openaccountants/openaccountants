# First home super saver release

Use this offline worksheet to estimate the first home super saver (FHSS) maximum release amount from eligible voluntary super contributions or to summarise a release using the Australian Taxation Office (ATO) determination. The ATO determination governs each release.

## Estimate

Call `estimateFhssRelease` with:

- `contributionFactsConfirmed: true` after reconciling eligibility, dates, amounts and personal deductions with fund records. Supply only the eligible part of each voluntary contribution. Exclude compulsory, excess and ineligible amounts. Special transfers are outside this worksheet.
- `determinationRequested` and `determinationDate` as `YYYY-MM-DD`. The request date selects the applicable lifetime limit. The determination date ends the associated earnings period. Supported requests start on 1 July 2018 and interest rates run to 31 December 2026.
- `contributions`, an array of up to 1,000 rows. Use `date`, `kind` (`personal` or `employer_voluntary`) and `amount`, a positive Australian dollar decimal string with up to 2 decimal places. Use the date the fund received the contribution. If multiple contributions share a date, give every row for that date `orderWithinDay` as a non-negative integer. Give simultaneous rows the same number. A confirmed empty list gives a zero estimate.
- `personalDeductions`, an object keyed by financial year such as `2026-27`. Supply the eligible personal amount claimed as a deduction for each year with personal contributions, including an explicit `"0"` where none was claimed.

The worksheet counts up to $15,000 each financial year towards a lifetime limit of $50,000, or $30,000 for a determination requested before 1 July 2022. It applies the ordering and personal deduction rules before applying 85% to eligible concessional amounts and 100% to eligible non-concessional amounts. Result rows identify contributions by their one-based position in the original input. A contribution split by a partial deduction can appear in 2 rows.

The associated earnings estimate compounds the daily shortfall interest charge (SIC) rate on the releasable part of each contribution through the determination date, inclusive. The start is 1 July 2017 for a contribution in 2017-18 and the first of its month for later contributions. The calculation rounds earnings down to whole dollars for each contribution. Example 6 of GN 2024/1 gives a different result for its stated contribution history. Use the ATO determination when reconciling a release.

## Actual release

Call `summariseFhssRelease` with `atoDeterminationConfirmed: true`, the dollar amounts `concessional`, `nonConcessional` and `associatedEarnings` from the determination and `actualReleased`, the total released for that determination. Supply these amounts as non-negative decimal strings. The worksheet reconciles the actual amount to the maximum, calculates the assessable portion and applies the 30% non-refundable FHSS offset. It leaves withholding, tax return entries and the separate FHSS tax for review of the actual records.

For example, a determination with $8,500 in releasable concessional contributions, $2,000 in non-concessional contributions and $500 in associated earnings has an $11,000 maximum. If the actual release is $8,035.17, the assessable amount is $6,035.17 and the offset is $1,810.55.

## Sources

- [Taxation Administration Act 1953, sch 1 ss 138-20 to 138-40 and 280-105](https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).
- [Income Tax Assessment Act 1997, ss 313-20 and 313-25](https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text).
- [ATO shortfall interest charge rates](https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates), [GN 2024/1](https://www.ato.gov.au/law/view/document?LocID=%22GDN%2FGDN20241%2FNAT%2FATO%22) and [TR 2024/4](https://www.ato.gov.au/law/view/print?DocID=TXR%2FTR20244%2FNAT%2FATO%2F00001).

From the repository root, run `node --test calculators/au-fhss/`. The tests use synthetic contributions and public rate tables.
