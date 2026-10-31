# Montenegro PIT: nine retained additional examples

Verbatim examples 3 to 11 from the predecessor Guide, retained alongside its two in-Guide examples. These are calculation controls with stated facts, not additional elections or taxpayer facts. The predecessor snapshot and topic map preserve the source chain.

### 3. Occasional work paid by a company

Gross fee 2,000, no documented costs, paid by a company. Standard expenses 600, base 1,400, PIT withheld 210. The 1,790 left is before any contribution due on the fee. [Arts. 16(5), 20(2) and 48a][law]

```oa-check
name: Montenegro occasional independent work withholding
inputs:
  gross_receipt: 2000
steps:
  - standard_expenses: gross_receipt * 0.30
  - taxable_base: gross_receipt - standard_expenses
  - pit_withheld: taxable_base * 0.15
  - receipt_after_pit_only: gross_receipt - pit_withheld
expected:
  standard_expenses: 600
  taxable_base: 1400
  pit_withheld: 210
  receipt_after_pit_only: 1790
```

### 4. Rent with standard expenses

Gross rent 20,000, no documented costs. Ordinary letting: base 14,000, PIT 2,100. Tourist letting with tourist tax paid: base 10,000, PIT 1,500. Tourist letting under an agency or local tourist organisation lease with at least 60 days' average occupancy: base 6,000, PIT 900. These are three different sets of facts. [Arts. 35, 36 and 49a][law]

```oa-check
name: Montenegro rental standard expense alternatives
inputs:
  gross_rent: 20000
steps:
  - ordinary_base: gross_rent * (1 - 0.30)
  - ordinary_pit: ordinary_base * 0.15
  - qualifying_50_base: gross_rent * (1 - 0.50)
  - qualifying_50_pit: qualifying_50_base * 0.15
  - qualifying_70_base: gross_rent * (1 - 0.70)
  - qualifying_70_pit: qualifying_70_base * 0.15
expected:
  ordinary_base: 14000
  ordinary_pit: 2100
  qualifying_50_base: 10000
  qualifying_50_pit: 1500
  qualifying_70_base: 6000
  qualifying_70_pit: 900
```

### 5. Property gain with a same-year capital loss

Sale of a property that was not the only and main residence for 150,000, with documented reconstruction 7,000 and sale costs 3,000; the price is not below market. Indexed acquisition cost is 110,000. Adjusted sale price 140,000, gain 30,000. A capital loss of 5,000 on shares sold in the same year reduces the taxable gain to 25,000; PIT 3,750, paid with the return. [Arts. 37a to 37d, 37g, 37h and 50a][law]

```oa-check
name: Montenegro property gain and current capital loss
inputs:
  sale_price: 150000
  reconstruction: 7000
  sale_costs: 3000
  established_indexed_cost: 110000
  current_capital_loss: 5000
steps:
  - adjusted_sale: sale_price - reconstruction - sale_costs
  - gain: adjusted_sale - established_indexed_cost
  - taxable_capital_gain: max(gain - current_capital_loss, 0)
  - pit: taxable_capital_gain * 0.15
expected:
  adjusted_sale: 140000
  gain: 30000
  taxable_capital_gain: 25000
  pit: 3750
```

### 6. Shares under FIFO

Buy 100 shares at 10, then 100 at 15, of the same issuer; sell 150 at 20. FIFO cost is 100 × 10 + 50 × 15 = 1,750; gain 1,250; PIT 187.50. Fifty shares at 15 remain. [Arts. 37a, 37f and 50a][law]

```oa-check
name: Montenegro securities FIFO gain
inputs:
  first_units: 100
  first_price: 10
  second_units: 100
  second_price: 15
  units_sold: 150
  sale_price_each: 20
steps:
  - first_used: min(first_units, units_sold)
  - second_used: units_sold - first_used
  - proceeds: units_sold * sale_price_each
  - fifo_cost: first_used * first_price + second_used * second_price
  - gain: proceeds - fifo_cost
  - pit: gain * 0.15
  - remaining_second_units: second_units - second_used
expected:
  first_used: 100
  second_used: 50
  proceeds: 3000
  fifo_cost: 1750
  gain: 1250
  pit: 187.50
  remaining_second_units: 50
```

### 7. Internet income versus video-game income

Two receipts of 10,000 each, neither salary nor taxed under another heading. Internet income: 15% expenses, base 8,500, PIT 1,275. Video-game competition income with no documented costs: 20% standard, base 8,000, PIT 1,200. [Arts. 37o to 37r and 50e][law]

```oa-check
name: Montenegro residual internet and video game bases
inputs:
  internet_receipts: 10000
  game_receipts: 10000
steps:
  - internet_base: internet_receipts * (1 - 0.15)
  - internet_pit: internet_base * 0.15
  - game_base: game_receipts * (1 - 0.20)
  - game_pit: game_base * 0.15
expected:
  internet_base: 8500
  internet_pit: 1275
  game_base: 8000
  game_pit: 1200
```

### 8. Foreign dividend with a capped credit

A resident receives a foreign dividend of 10,000 gross and proves 2,000 of foreign income tax paid. Montenegrin tax is 1,500, so the credit is capped at 1,500 and nothing is left to pay. The 500 excess is not carried forward, refunded or set against other income. [Arts. 37, 44 and 45][law]

```oa-check
name: Montenegro private foreign dividend credit cap
inputs:
  foreign_gross_dividend: 10000
  qualifying_foreign_tax: 2000
steps:
  - domestic_tax_on_foreign: foreign_gross_dividend * 0.15
  - allowed_credit: min(qualifying_foreign_tax, domestic_tax_on_foreign)
  - residual_domestic_pit: domestic_tax_on_foreign - allowed_credit
  - excess_not_claimed: qualifying_foreign_tax - allowed_credit
expected:
  domestic_tax_on_foreign: 1500
  allowed_credit: 1500
  residual_domestic_pit: 0
  excess_not_claimed: 500
```

### 9. Fine-art royalty and amateur sport

Fine-art rights 5,000 with no documented costs: 60% standard, base 2,000, PIT 300. Amateur sport income 5,000 (not salary) with no documented costs: 90% standard, base 500, PIT 75. [Arts. 37i to 37m, 50b and 50c][law]

```oa-check
name: Montenegro fine art royalty and amateur sport
inputs:
  fine_art_rights: 5000
  qualifying_amateur_sport: 5000
steps:
  - royalty_base: fine_art_rights * (1 - 0.60)
  - royalty_pit: royalty_base * 0.15
  - sport_base: qualifying_amateur_sport * (1 - 0.90)
  - sport_pit: sport_base * 0.15
expected:
  royalty_base: 2000
  royalty_pit: 300
  sport_base: 500
  sport_pit: 75
```

### 10. Sole proprietor with municipal surtax

Principal-business taxable profit 20,000; the municipality's surtax decision sets 13%. PIT is 324 + 8,000 × 15% = 1,524. Surtax is 13% of the PIT, 198.12. Total 1,722.12. Contributions are computed separately. [PIT Law art. 10(1)(2)][law]; [Local Self-Government Financing Law arts. 8 and 9][local]

```oa-check
name: Montenegro principal business PIT with municipal surtax
inputs:
  taxable_profit: 20000
  surtax_rate: 0.13
steps:
  - pit: max(min(taxable_profit, 12000) - 8400, 0) * 0.09 + max(taxable_profit - 12000, 0) * 0.15
  - surtax: round(pit * surtax_rate, 2)
  - total: pit + surtax
expected:
  pit: 1524
  surtax: 198.12
  total: 1722.12
```

### 11. Gambling winning before and after 21 May 2026

A betting winning of 1,500 after deducting the stake. Paid on 10 March 2026, the bands apply: 1,450 × 10% = 145. Paid on 10 June 2026, the flat rate applies: 1,500 × 12% = 180. The organiser withholds and pays by the 15th of the next month. [PIT Law arts. 10(1)(4), 37s and 50f][law]; [70/26 arts. 1 and 3][may]

```oa-check
name: Montenegro gambling winning before and after the 70/26 change
inputs:
  winning: 1500
steps:
  - tax_before_21_may: max(min(winning, 1500) - 50, 0) * 0.10 + max(winning - 1500, 0) * 0.15
  - tax_from_21_may: winning * 0.12
expected:
  tax_before_21_may: 145
  tax_from_21_may: 180
```

[law]: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0
[amend]: https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0
[may]: https://www.sluzbenilist.me/propisi/394390/download
[mayrecord]: https://www.sluzbenilist.me/propisi/394390
[return]: https://wapi.gov.me/download/afb50b45-7e83-4dac-b69e-2a1e280d3ffc?version=1.0
[local]: https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0
[contrib]: https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0
[vat]: https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0

