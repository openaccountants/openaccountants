# Ordinary arrears controls

Writer calculations, pending independent review. These controls supplement the existing two main blocks in each Guide. They do not establish notice validity, exemption, discretionary relief, payment allocation or a part-month convention.

## Income-tax surcharge ledger

Sources read 28 October 2026: [Income Tax Law s199](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=253819) and [Surcharges and Supplements Regulations 2005 rr1–4](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=268079). Assume a lawful £10,000 settlement balance, no payments/relief/backdating complication and no other charge over twelve months. The £500 initial surcharge passes the aggregate £50 minimum. The first additional charge at six months is £525; the next is £551.25. Total surcharges £1,576.25, total outstanding £11,576.25. The initial charge is payable on the thirtieth day after settlement; this does not grant thirty days to pay the original debt without its consequences.

```oa-check
name: Guernsey income-tax initial and two six-month surcharge events
inputs:
  principal: 10000
  surcharge_rate: 0.05
steps:
  - initial_surcharge: principal * surcharge_rate
  - balance_before_six_month_event: principal + initial_surcharge
  - first_additional_surcharge: balance_before_six_month_event * surcharge_rate
  - balance_before_twelve_month_event: balance_before_six_month_event + first_additional_surcharge
  - second_additional_surcharge: balance_before_twelve_month_event * surcharge_rate
  - total_surcharges: initial_surcharge + first_additional_surcharge + second_additional_surcharge
  - total_outstanding: principal + total_surcharges
expected:
  initial_surcharge: 500
  first_additional_surcharge: 525
  second_additional_surcharge: 551.25
  total_surcharges: 1576.25
  total_outstanding: 11576.25
```

## Separate statutory Class 1 contribution rule

Source read 28 October 2026: [Social Insurance Law s104(1A)](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=253497). Assume £5,000 primary/secondary Class 1 contribution principal remained unchanged for an established two full months after the prescribed due date, no relief or other charge, and no part-month question. The text specifies an initial 2.5% penalty and monthly 2.5% interest on the outstanding contribution. It gives £125 initial penalty and £250 interest, total £375. It does not justify importing the older employer manual's £50 minimum or treating the monthly interest as the income-tax six-month surcharge. The guidance/statute reconciliation is still open; this is the statutory arithmetic, not an asserted Revenue Service bill.

```oa-check
name: Guernsey statutory Class 1 arrears penalty and two full months interest
inputs:
  outstanding_contribution: 5000
  initial_penalty_rate: 0.025
  monthly_interest_rate: 0.025
  established_full_months: 2
steps:
  - initial_penalty: outstanding_contribution * initial_penalty_rate
  - monthly_interest: outstanding_contribution * monthly_interest_rate
  - period_interest: monthly_interest * established_full_months
  - total_charges: initial_penalty + period_interest
expected:
  initial_penalty: 125
  monthly_interest: 125
  period_interest: 250
  total_charges: 375
```
