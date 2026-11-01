# Preserved Gibraltar transaction-tax illustrations

Original v0.8 illustration paragraphs and executable control, unchanged. The main Guide has the original import and deduction controls. These are assumed examples, not commodity/valuation rulings.

1. **Import:** customs value £10,000 already includes £400 freight. Separately chargeable excise £1,000 and packing £200 are not included. Taxable amount = £10,000 + £1,000 + £200 = **£11,200**. At an established 15% rate, tax = **£1,680**. Adding the £400 again would overstate tax by £60.
2. **Local production:** established comparable open-market value £8,000; production cost £6,000. At an established 15% rate, tax = **£1,200**, not £900. If disposal rights transfer before dispatch, leaving occurs on that transfer under paragraph 1(2)(b).
3. **No comparable supply:** no purchase price is available and evidenced cost price is £6,000. That establishes a floor of £6,000, not proof that any lower invoice price is acceptable. At 15%, tax on the floor is £900; confirm the final taxable valuation before using that amount.

```oa-check
name: Local production with comparable market value
inputs:
  comparable_value: 8000
  cost: 6000
  rate: 0.15
steps:
  - tax_on_comparable_value: comparable_value * rate
  - tax_on_cost: cost * rate
  - understatement_using_cost: tax_on_comparable_value - tax_on_cost
expected:
  tax_on_comparable_value: 1200
  tax_on_cost: 900
  understatement_using_cost: 300
```
4. **Rate sensitivity:** an independently established £1,000 taxable amount gives £150 at 15%, £50 at 5%, or £0 at 0%. The arithmetic does not prove eligibility for a reduced category.
