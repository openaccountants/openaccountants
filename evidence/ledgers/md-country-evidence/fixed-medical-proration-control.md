# Moldova fixed medical-premium proration source control

Writer arithmetic only. [Government Regulation1246/2018 point22](https://www.legis.md/cautare/getResults?doc_id=151859&lang=ro), read2026-10-30. Assume the actual taxpayer qualifies for the later-entry point27/art23(1) branch, CNAM confirms183 uninsured days including the remaining year, and the applicable full2026 annual premium is12636. This is not the missed31March full-premium branch or the independent-service medical top-up.

The control verifies the **unrounded** statutory fraction. It does not certify CNAM payment/reporting rounding, interest, the actual person's status or day count.

```oa-check
name: Moldova fixed medical later-entry unrounded annual-day fraction
tolerance: 0.000001
inputs:
  full_annual_medical: 12636
  calendar_days_2026: 365
  confirmed_uninsured_days: 183
steps:
  unrounded_prorated_medical: full_annual_medical / calendar_days_2026 * confirmed_uninsured_days
expected:
  unrounded_prorated_medical: 6335.309589
```
