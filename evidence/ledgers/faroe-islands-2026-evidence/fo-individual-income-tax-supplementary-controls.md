# Supplementary controls: fo-individual-income-tax

Derived case amounts from the cited rules. Original main Guide examples remain unchanged.

### 3. Full-year church member

Assume the same established DKK 300,000 ordinary taxable income as example 1, already a multiple of DKK 100, but a full-year church member in Tórshavn itself. The 2026 parish rate is 0.85%, not the 0.90% rate for Argir/Borðan/Nólsoy. The church base is DKK 270,000 and church tax DKK 2,295. National DKK 32,950 plus municipal DKK 51,300 plus church DKK 2,295 gives DKK 86,545. The DKK 150,000 ordinary-income ceiling is not reached. Assume no credits, foreign income, special regime or other tax/charge; this is not a net-pay calculation. [Tax Act §§46–47, 54(2)][tax]; [Assessment Act §1][rate]; [2026 locality footnote 8][municipal]; [official audit report §4.10, p. 45][church-audit]

```oa-check
name: Faroese full-year Torshavn church member after municipal exempt amount
inputs:
  ordinary_base: 300000
  exempt_amount: 30000
  municipal_rate: 0.19
  church_rate: 0.0085
steps:
  municipal_church_base: max(floor(ordinary_base / 100) * 100 - exempt_amount, 0)
  national: 14950 + (ordinary_base - 180000) * 0.15
  municipal: municipal_church_base * municipal_rate
  church: municipal_church_base * church_rate
  ordinary_income_tax: national + municipal + church
  ceiling: ordinary_base * 0.50
  ceiling_reduction: max(ordinary_income_tax - ceiling, 0)
expected:
  municipal_church_base: 270000
  national: 32950
  municipal: 51300
  church: 2295
  ordinary_income_tax: 86545
  ceiling_reduction: 0
```


## Spouse transfer: separately assessed bases

Sources: Tax Act §4 and TAKS Hjúnafrádráttur, read28October2026. Exact TAKS example says: “fyrra inntøkan sett til 30.000 og seinna til 290.000”. Full-year nonnegative ordinary cohabiting spouse fixture only; no separation/death/part-year case. This is a derived base transformation, not a quoted new statutory rate.

```oa-check
name: Faroese full-year spouse allowance adjustment
inputs:
  lower_income: 20000
  higher_income: 300000
  allowance: 30000
steps:
  transferred: allowance - lower_income
  lower_adjusted: lower_income + transferred
  higher_adjusted: higher_income - transferred
expected:
  transferred: 10000
  lower_adjusted: 30000
  higher_adjusted: 290000
```

## Indicative TAKS2026 part-year calculator, no credits

Observed at https://www.eskatt.fo/sjtp/sjtpsim.aspx through the public UI on28October2026. Synthetic data only:2026,Tórshavn,A-income150000,no church membership,no child/pensioner/other credits,no foreign income,no special income. The calculator's own current year display is2026. Its landing guidance says “úrslitið er vegleiðandi”; calculation page says “Úrslitið er bert ein fyribils útrokning.” It is an administrative observation, not a statutory algorithm universally establishing credits or final settlement rounding.

Full-year365-day run: taxable150000, annualised150000,grosstax33850,reduced33850,net33850,AM3%4500,total38350. 180-day run: actual150000, annualised304100,grosstax85644,reduced/net42235.40, final displayed income tax42235,AM4500,total46735. Source UI extracts and screenshot are retained in root-evidence. Read the displayed2026 child-credit6500 only as a calculator limitation: it differs from current Assessment Act §2 and is NOT adopted. No child-credit cases tested or inferred.

```oa-check
name: Faroese observed no-credit180-day annualisation
inputs:
  actual_income: 150000
  taxable_days: 180
  calendar_days: 365
steps:
  annual_equivalent: actual_income * calendar_days / taxable_days
  rounded_annual_base: floor(annual_equivalent / 100) * 100
  annual_national: 14950 + (rounded_annual_base - 180000) * 0.15
  annual_municipal: (rounded_annual_base - 30000) * 0.19
  annual_tax: annual_national + annual_municipal
  reduced_tax: annual_tax * taxable_days / calendar_days
  am_charge: actual_income * 0.03
expected:
  annual_equivalent: 304166.67
  rounded_annual_base: 304100
  annual_national: 33565
  annual_municipal: 52079
  annual_tax: 85644
  reduced_tax: 42235.40
  am_charge: 4500
```
