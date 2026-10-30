# Preserved original non-resident rent control

This original block is unchanged; the service and property blocks remain in the Guide.

```oa-check
name: Andorra non-resident rental income base
inputs:
  gross_rent: 15000
  base_reduction_rate: 0.20
  tax_rate: 0.10
steps:
  reduction: gross_rent * base_reduction_rate
  taxable_base: gross_rent - reduction
  tax: taxable_base * tax_rate
expected:
  reduction: 3000
  taxable_base: 12000
  tax: 1200
```
