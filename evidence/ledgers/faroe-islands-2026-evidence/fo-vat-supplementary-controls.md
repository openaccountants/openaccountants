# Faroe foreign telecoms, registered partial-recovery recipient

Derived hypothetical control,28October2026. VAT Act §28(1)–(3),items7–13,§14/§§15–16 and Regulation35/2000 §1. Foreign supplier has60000annual qualifying sales,serviceusedFaroes; no full recovery exception,no domestic-equivalent exemption,no private/blocked costs or special allocation. Telecoms isitem12. A registered buyer of items1–6 is expressly outside this control.

```oa-check
name: Faroese registered partial-recovery telecoms purchase
inputs:
  qualifying_annual_supplier_sales: 60000
  threshold: 50000
  invoice_net: 10000
  vat_rate: 0.25
  shared_recoverable_proportion: 0.60
steps:
  threshold_excess: qualifying_annual_supplier_sales - threshold
  charged_vat: invoice_net * vat_rate
  recoverable_input: charged_vat * shared_recoverable_proportion
  unrecoverable_input: charged_vat - recoverable_input
expected:
  threshold_excess: 10000
  charged_vat: 2500
  recoverable_input: 1500
  unrecoverable_input: 1000
```
