# Retained original transfer-pricing controls

All three original blocks are unchanged from the24October checkpoint. The30October writer additions still require independent whole-pack review.

### Same-party goods aggregation in the assumed Master/Local route

Assume the group route, qualifying relationship and cross-border goods purchases from one party in one year are established. Two purchases of CHF 600,000 and CHF 500,000 total CHF 1.1 million, over the CHF 1 million threshold. No other party/category is included.

```oa-check
name: Liechtenstein assumed group route goods threshold
inputs:
  first_goods_purchase: 600000
  second_goods_purchase: 500000
  established_route_threshold: 1000000
steps:
  party_year_purchases: first_goods_purchase + second_goods_purchase
  excess_over_threshold: party_year_purchases - established_route_threshold
expected:
  party_year_purchases: 1100000
  excess_over_threshold: 100000
```

### Separate-size route category aggregation

Assume the separate-size route and relationship conditions are established, with two cross-border service expenses in the same category to one party, CHF 80,000 and CHF 60,000. CHF 140,000 exceeds CHF 125,000 by CHF 15,000. This does not establish the company-size or relationship gates.

```oa-check
name: Liechtenstein assumed separate size route service category
inputs:
  first_category_expense: 80000
  second_category_expense: 60000
  established_route_threshold: 125000
steps:
  party_category_year_total: first_category_expense + second_category_expense
  excess_over_threshold: party_category_year_total - established_route_threshold
expected:
  party_category_year_total: 140000
  excess_over_threshold: 15000
```

### Gross cost-plus is not margin on sales

Assume an independently supported gross cost-plus method, CHF 100,000 eligible cost and 8% markup solely for the case. Gross profit is CHF 8,000, revenue CHF 108,000 and profit/revenue approximately 7.407407%. Neither percentage is a Liechtenstein safe harbour; no TNMM benchmark is inferred.

```oa-check
name: Liechtenstein assumed gross cost plus denominator control
inputs:
  established_cost_base: 100000
  assumed_supported_markup: 0.08
steps:
  gross_profit: established_cost_base * assumed_supported_markup
  transaction_revenue: established_cost_base + gross_profit
  profit_as_percent_of_sales: gross_profit / transaction_revenue * 100
expected:
  gross_profit: 8000
  transaction_revenue: 108000
  profit_as_percent_of_sales: 7.407407407407407
```
