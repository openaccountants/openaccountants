# Original Guernsey corporate controls

Moved byte-exact from the published a23757a2 Guide, including explanatory paragraphs. They remain supplementary regression controls; the two main examples now test the ordinary base/loss bridge and the qualifying-loan gross-up/repayment method.

## Two worked examples that recompute

**Established mixed income.** Assume review has established separate ordinary taxable income £100,000, intermediate-category income £30,000 and Guernsey rental taxable income £20,000, with no overriding wider-base or minimum-tax rule. At 0%, 10% and 20%, ordinary company tax is **£7,000**. The example does not establish deductions, stream classification, loss offsets or Pillar Two treatment. [Company rates](https://gov.gg/RevenueService/Companies).

```oa-check
name: Guernsey established corporate income streams
inputs:
  standard_income: 100000
  intermediate_income: 30000
  rental_income: 20000
steps:
  - standard_tax: standard_income * 0
  - intermediate_tax: intermediate_income * 0.10
  - rental_tax: rental_income * 0.20
  - total_tax: standard_tax + intermediate_tax + rental_tax
expected:
  standard_tax: 0
  intermediate_tax: 3000
  rental_tax: 4000
  total_tax: 7000
```

**Daily-penalty catch-up.** Assume no successful appeal/reduction and a corporate return submitted after the 30-day concession period, with **35 chargeable days established from the Order and submission dates**. The guidance calculation is £300 + 35 × £50 = **£2,050**, not merely five daily penalties. A return qualifying for the within-30-day concession would retain the £300 initial penalty without daily penalties. This example does not decide inclusive date counting or the Order's validity. [Penalty FAQ](https://gov.gg/taxpenalties).

```oa-check
name: Guernsey corporate daily penalty after concession period
inputs:
  initial_penalty: 300
  daily_rate: 50
  established_chargeable_days: 35
steps:
  - daily_penalty: daily_rate * established_chargeable_days
  - total_penalty: initial_penalty + daily_penalty
expected:
  daily_penalty: 1750
  total_penalty: 2050
```
