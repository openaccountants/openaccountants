# Moldova independent-service medical allocation controls

Writer controls only, read 2026-10-30. Statutory basis: [Fiscal Code arts. 69^25(4)(c), 69^26(2)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [medical budget Law 321/2025 art. 4(3)](https://www.legis.md/cautare/getResults?doc_id=156542&lang=ro). Actual single-tax totals and unchanged entitlement/status are hypothetical inputs. No independent review or filing rounding/partial-year rule is established by these controls.

The medical allocation is 15.4% of the single tax. For an annual allocation below the 2,527 benchmark, the positive difference is the additional amount.

```oa-check
name: Moldova independent service medical allocation below benchmark
inputs:
  assumed_annual_single_tax: 10000
  medical_allocation_fraction: 0.154
  benchmark: 2527
steps:
  annual_medical_allocation: assumed_annual_single_tax * medical_allocation_fraction
  additional_medical: max(benchmark - annual_medical_allocation, 0)
expected:
  annual_medical_allocation: 1540
  additional_medical: 987
```

When the allocation covers the benchmark, this difference mechanism does not create a refund.

```oa-check
name: Moldova independent service medical allocation covers benchmark
inputs:
  assumed_annual_single_tax: 20000
  medical_allocation_fraction: 0.154
  benchmark: 2527
steps:
  annual_medical_allocation: assumed_annual_single_tax * medical_allocation_fraction
  additional_medical: max(benchmark - annual_medical_allocation, 0)
  allocation_above_benchmark: annual_medical_allocation - benchmark
expected:
  annual_medical_allocation: 3080
  additional_medical: 0
  allocation_above_benchmark: 553
```
