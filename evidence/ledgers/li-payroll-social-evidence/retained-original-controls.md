# Retained original reviewed calculation controls

All four original blocks from24October2026 are retained byte-for-byte here. This is historical review evidence. They do not confer review on the30October2026 writer changes. Governing rates and applicability remain in the current Guide.

These are assumed ordinary covered adult employees; rates and bases must apply before the arithmetic is used. No occupational-pension, accident/sickness premium, health contribution or wage tax is included in the first two controls.

### Full-year employee contributions

```oa-check
name: Liechtenstein 2026 assumed employee contribution split
inputs:
  established_annual_wage: 60000
  employee_ahv_iv_fak: 0.049
  annual_alv_cap: 126000
  employee_alv: 0.005
steps:
  ahv_iv_fak_deduction: established_annual_wage * employee_ahv_iv_fak
  alv_base: min(established_annual_wage, annual_alv_cap)
  alv_deduction: alv_base * employee_alv
  specified_employee_deductions: ahv_iv_fak_deduction + alv_deduction
expected:
  ahv_iv_fak_deduction: 2940
  alv_base: 60000
  alv_deduction: 300
  specified_employee_deductions: 3240
```

### Full-year employer contributions with ALV cap

Assume CHF 150,000 established annual wage, all subject to AHV/IV/FAK/VK, and full-year ALV coverage in this employment.

```oa-check
name: Liechtenstein 2026 assumed employer contribution and ALV ceiling
inputs:
  established_annual_wage: 150000
  employer_ahv_iv_fak_vk: 0.07385
  annual_alv_cap: 126000
  employer_alv: 0.005
steps:
  ahv_iv_fak_vk_charge: established_annual_wage * employer_ahv_iv_fak_vk
  alv_base: min(established_annual_wage, annual_alv_cap)
  alv_charge: alv_base * employer_alv
  specified_employer_charges: ahv_iv_fak_vk_charge + alv_charge
expected:
  ahv_iv_fak_vk_charge: 11077.50
  alv_base: 126000
  alv_charge: 630
  specified_employer_charges: 11707.50
```

### Part-year ALV cap

This reproduces the institution's section 6 example: 15 April–28 December gives 254 contribution days under its stated convention and CHF 96,200 pay. The cap is CHF 88,900, giving CHF 889 for both sides combined. This is not 254 ordinary actual-calendar days.

```oa-check
name: Liechtenstein bulletin part year ALV example
inputs:
  established_contribution_days: 254
  daily_cap: 350
  established_period_wage: 96200
  employee_rate: 0.005
  employer_rate: 0.005
steps:
  period_cap: established_contribution_days * daily_cap
  liable_wage: min(established_period_wage, period_cap)
  employee_contribution: liable_wage * employee_rate
  employer_contribution: liable_wage * employer_rate
  combined_contribution: employee_contribution + employer_contribution
expected:
  period_cap: 88900
  liable_wage: 88900
  employee_contribution: 444.50
  employer_contribution: 444.50
  combined_contribution: 889
```

### Assumed established wage-withholding instruction

Assume a single resident employee with CHF 90,000 expected full-year gross, no special category/treaty or revised authority instruction, and a confirmed 9% withholding rate. CHF 7,500 current gross gives CHF 675 withholding, before other deductions. This does not calculate final individual tax.

```oa-check
name: Liechtenstein assumed confirmed ordinary wage withholding
inputs:
  established_current_gross: 7500
  established_withholding_rate: 0.09
steps:
  wage_withholding: established_current_gross * established_withholding_rate
expected:
  wage_withholding: 675
```
