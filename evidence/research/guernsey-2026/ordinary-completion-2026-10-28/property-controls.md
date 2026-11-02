# Statutory property method controls

Writer calculations, pending independent review. The main property Guide retains both original blocks unchanged. Sources read 28 October 2026: [Direct Law ss2–6](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=253627), [Direct Rates Ordinance s1](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=263098), [Indirect Law ss1–5,9](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=253628), [Indirect Rates Ordinance s1](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=263097), and [2025 Fees Regulations rr1,4](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=265347).

## Direct non-arm's-length base

Assume an established non-exempt direct acquisition, otherwise than at arm's length, with supported market value £900,000 and stated consideration £600,000. No family, trust, wholly-owned-company or other exemption is established; no downsizing relief applies. Section 6 uses the £900,000 market value. Duty is £29,750 rather than the £17,750 that the lower consideration would produce. Neither the example nor its arithmetic establishes the actual market value or defeats an exemption.

```oa-check
name: Guernsey non-exempt non-arm-length acquisition uses market value
inputs:
  stated_consideration: 600000
  established_market_value: 900000
steps:
  - correct_first_band: min(established_market_value, 300000) * 0.0225
  - correct_second_band: min(max(established_market_value - 300000, 0), 200000) * 0.035
  - correct_third_band: max(established_market_value - 500000, 0) * 0.04
  - correct_duty: correct_first_band + correct_second_band + correct_third_band
  - unsupported_lower_base_duty: 300000 * 0.0225 + 200000 * 0.035 + (stated_consideration - 500000) * 0.04
  - difference: correct_duty - unsupported_lower_base_duty
expected:
  correct_duty: 29750
  unsupported_lower_base_duty: 17750
  difference: 12000
```

The compact third-band expression is limited to the stated values, both below £950,000. The complete graduated table remains in the Guide.

## Indirect significant-benefit duty, separate fee and penalty ceiling

Assume a relevant transaction actually satisfies the Anti-Avoidance Law's consideration/significant-benefit test, is not subject to direct duty, and is neither excluded nor exempt. Independent valuation has established market value of the transferred significant benefit at £600,000 at the transaction date. This is a valuation input, not a formula equating benefit value to shares, debt or the entire property. The separately sourced indirect rate schedule yields £17,750 duty; the current £158 non-exempt registration fee brings those identified payments to £17,908. Both parties' section 5 self-assessment/payment duties run within 28 days of the transaction.

For a different relevant transaction whose exemption has actually been established, the £79 exempt registration fee still applies, as do the declaration duties. Section 9's 100%-of-duty penalty is a ceiling available on the specified assessment route, not an automatic charge: on £17,750 assessed duty its ceiling is £17,750.

```oa-check
name: Guernsey indirect property benefit and separate 2026 filing fees
inputs:
  established_significant_benefit_value: 600000
  non_exempt_registration_fee: 158
  exempt_registration_fee: 79
  maximum_penalty_fraction: 1
steps:
  - first_band: 300000 * 0.0225
  - second_band: 200000 * 0.035
  - third_band: (established_significant_benefit_value - 500000) * 0.04
  - duty: first_band + second_band + third_band
  - duty_and_non_exempt_fee: duty + non_exempt_registration_fee
  - separate_exempt_case_duty: 0
  - separate_exempt_case_duty_and_fee: separate_exempt_case_duty + exempt_registration_fee
  - assessment_penalty_ceiling: duty * maximum_penalty_fraction
expected:
  duty: 17750
  duty_and_non_exempt_fee: 17908
  separate_exempt_case_duty_and_fee: 79
  assessment_penalty_ceiling: 17750
```
