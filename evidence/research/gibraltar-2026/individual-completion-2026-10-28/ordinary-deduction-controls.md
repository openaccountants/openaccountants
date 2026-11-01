# Ordinary individual deduction controls

All entitlement and input facts below are explicit assumptions. These checks verify arithmetic for separate cases, not a combined assessment or a filing.

## Family deductions

Assume the statutory joint-custody conditions and full-year residence are established. Each parent's ordinary half is £2,900 from £5,800. Separately, an eligible ordinarily resident claimant paying £6,000 for a nursery meeting every rule 14A condition is limited to £5,480. No death or monthly adjustment is assumed.

```oa-check
name: Ordinary custody half and qualified nursery cap
inputs:
  rule12_amount: 5800
  eligible_nursery_paid: 6000
  nursery_cap: 5480
steps:
  - joint_custody_each: rule12_amount / 2
  - nursery_deduction: min(eligible_nursery_paid, nursery_cap)
expected:
  joint_custody_each: 2900
  nursery_deduction: 5480
```

## Approved personal-pension contribution

Assume an ABS claimant, approved scheme/contract, £50,000 qualifying earned income excluding employment that provides a pension/annuity, and actual £12,000 contributions. No other limitation or adjustment is assumed.

```oa-check
name: Approved personal pension contribution earned-income and money caps
inputs:
  qualifying_earned_income: 50000
  eligible_contributions_paid: 12000
  money_cap: 35000
steps:
  - earned_income_cap: qualifying_earned_income * 0.2
  - allowed_deduction: min(eligible_contributions_paid, earned_income_cap, money_cap)
expected:
  earned_income_cap: 10000
  allowed_deduction: 10000
```

## Separate gym and private-school credits

Assume all statutory location, supplier, child/school and evidence conditions are met. Liability is independently established for each separate case. These are neither combined credits nor an asserted ordering between them; there is no unused-credit refund, transfer or carry-forward.

```oa-check
name: Separate qualifying gym and tuition credits capped by own liability
inputs:
  gym_cost: 900
  gym_case_liability: 50
  tuition_cost: 8000
  school_case_liability: 900
steps:
  - gym_credit: min(gym_cost * 0.1, gym_case_liability)
  - school_credit: min(tuition_cost * 0.1, school_case_liability)
expected:
  gym_credit: 50
  school_credit: 800
```

## Home-purchase aggregate balance

Separate claimants acquired qualifying dwellings after 1 July 2019, with all ordinary Rules 2/8 eligibility, spouse/allocation, cost and prior-claim tests independently established. £13,000 and £7,500 are assumed applicable total entitlements after all ownership/claim restrictions. Actual eligible current payments meet the assumed current claim. No forfeiture or special £4,000 deduction is included.

```oa-check
name: Home purchase aggregate deduction consumed across years
inputs:
  abs_total_entitlement: 13000
  abs_prior_claimed: 4000
  abs_current_eligible_paid: 6000
  gibs_total_entitlement: 7500
  gibs_prior_claimed: 2500
  gibs_current_eligible_paid: 4000
steps:
  - abs_current: min(abs_current_eligible_paid, abs_total_entitlement - abs_prior_claimed)
  - abs_remaining: abs_total_entitlement - abs_prior_claimed - abs_current
  - gibs_current: min(gibs_current_eligible_paid, gibs_total_entitlement - gibs_prior_claimed)
  - gibs_remaining: gibs_total_entitlement - gibs_prior_claimed - gibs_current
expected:
  abs_current: 6000
  abs_remaining: 3000
  gibs_current: 4000
  gibs_remaining: 1000
```
