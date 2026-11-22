# Pay as you go (PAYG) withholding

This offline worksheet calculates Australian pay as you go (PAYG) withholding on ordinary salary or wages under Schedule 1 and the study and training support loan component under Schedule 8. It also works back from a net pay and recalculates withholding on current-year back pay under Schedule 5 Method B(i).

## Regular pay

Call `calculatePaygWithholding` with:

- `scopeConfirmed: true` once the relevant payroll period, payee declarations, taxable earnings and withholding schedule have been verified. Supply `earnings` as an Australian dollar decimal string with up to 2 decimal places. Include taxable allowances where the schedule applies.
- `payDate` as `YYYY-MM-DD` from 1 July 2024 to 30 June 2027. The payment date determines the schedule. Set `period` to `weekly`, `fortnightly`, `monthly` or `quarterly`.
- `scale` as a number from 1 to 6. Use 1 for no tax-free threshold, 2 for the tax-free threshold, 3 for a foreign resident who quoted a tax file number, 4 where a tax file number was required and not provided, 5 for a full Medicare levy exemption and 6 for a half exemption. For scale 4, supply `foreignResident: true` or `false`. Use the declarations to select the scale. The worksheet takes no tax file number.
- `studyLoan: true` or `false` as applicable to withholding under the payee's declarations. The study loan calculation supports payments from 24 September 2025 and scales 1, 2, 3, 5 and 6. It works out Schedule 1 and Schedule 8 separately, with each rounded to whole dollars. Official combined coefficients can produce a result one dollar different.

For regular pay without a study loan, `taxOffsets` takes an authorised annual offset as a decimal string on scales 2, 5 and 6. `medicareChildren` takes a verified dependent child count on scales 2 and 6 when a levy adjustment applies. Set `extraPay: true` only when the payee requests the extra withholding in a 53-week or 27-fortnight year. Check excess reductions, other schedules and variations against the source before processing the pay.

For example, a weekly scale 2 payment of $2,608.36 in 2026-27 with a study loan gives $654 under Schedule 1 and $193 under Schedule 8, totalling $847.

## Gross-up

Call `grossUpPaygWithholding` with the same date, declarations, period and scale, and `netPay` in place of `earnings`. Other adjustments are outside the gross-up. A result is usable where PAYG withholding is the only difference between gross and net. Whole-dollar rounding can give several matching gross amounts. The worksheet returns the candidates for review and leaves the gross to the pay agreement.

For example, monthly net pay of $4,775.33 on scale 2 in 2026-27 with a study loan can come from $5,884.33 or $5,893.33 gross. The latter crosses a threshold after the schedule's extra cent for monthly earnings ending in 33 cents. Both results reconcile to the same net.

## Back pay for earlier periods in the same year

Call `calculateMethodBi` with current ordinary `earnings` and `priorPeriods`, one row per affected earlier payment in the same financial year. Give each row `payDate`, previously paid `earnings`, the allocated `backPayment` and actual `withheld` in whole dollars. Include any study loan amount in the previously withheld total. Use the same verified ordinary withholding circumstances for these periods. The worksheet covers weekly, fortnightly and monthly pay on scales 1, 2, 3, 5 or 6 with no additional adjustments. Reconcile any changes to the declarations or study loan schedule separately, including the 2025-26 change in Schedule 8.

The worksheet recalculates each period using the revised earnings. It subtracts the amount actually withheld, sums the differences, floors the total at zero and adds withholding on current ordinary pay. The 47% cap for Methods A and B(ii) does not apply to Method B(i). Keep any additional payments for previous financial years or unrelated bonuses separate.

## Sources

- [ATO Schedule 1, 1 July 2024 to 30 June 2026](https://www.ato.gov.au/tax-rates-and-codes/schedule-1-tax-table-01-july-2024-to-30-june-2026).
- [Taxation Administration (Withholding Schedules) Instrument (No. 2) 2025, sch 8](https://www.legislation.gov.au/F2025L01016/asmade/text).
- [Taxation Administration (Withholding Schedules) Instrument 2026, schs 1, 5 and 8](https://www.legislation.gov.au/F2026L00716/asmade/2026-06-12/text/original/epub/OEBPS/document_1/document_1.html) and [ATO Schedule 5 examples](https://www.ato.gov.au/tax-rates-and-codes/schedule-5-tax-table-for-back-payments-commissions-bonuses-and-similar-payments/withholding-amounts-examples).

From the repository root, run `node --test calculators/au-payg-withholding/`. The tests use published table values and synthetic inputs.
