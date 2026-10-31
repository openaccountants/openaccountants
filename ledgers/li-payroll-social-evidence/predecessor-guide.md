---
name: li-payroll-social
description: >
  Prepare 2026 Liechtenstein payroll and contribution workpapers for ordinary covered
  employees. Use for AHV, IV, FAK, administration contributions, capped ALV, wage
  withholding, annualised gross pay, residence and treaty screening, payroll
  reconciliation and employer health-insurance contributions. It replaces the earlier
  Swiss-rate approximations with the Liechtenstein contribution bulletin and current
  wage-tax instructions. Establish coverage, employment dates, taxable remuneration,
  family status and authority directions before calculating. It does not determine
  disputed employment status, international insurance coordination, every benefit,
  pension-plan premium, insurer invoice or treaty entitlement, and it is not a
  completed payroll filing or a named local accountant's review.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
version: 0.2
---

# Liechtenstein payroll and social contributions v0.2

Independent source/editorial review evidence and correction status are in the [dated whole-pack review record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md). Apply its exact revision and scope limits. Named Liechtenstein accountant review remains open.

## Who this applies to

Use this 2026 source-cited draft for ordinary employees subject to Liechtenstein payroll and insurance. Confirm coverage separately for each employment and country. The combined Guide supplies scoped PR and SC methods; it does not complete either domain. The earlier Swiss contribution approximations and resident-assessment-only instruction are replaced below, with the prior text retained in Git history.

## Rates and bases

The [AHV-IV-FAK bulletin effective 1 January 2026][contributions], sections 5–6, gives these percentages of the established contribution wage:

| Contribution | Employee | Employer |
|---|---:|---:|
| AHV | 4.025% | 4.225% |
| IV | 0.675% | 0.675% |
| FAK | 0.200% | 1.900% |
| Administration, VK | none | 0.585% |
| Total above, excluding ALV | 4.900% | 7.385% |
| ALV | 0.500% | 0.500% |

ALV is capped at CHF 126,000 yearly **per employment**. For part-year employment, the bulletin uses CHF 350 per contribution day with its 30-day-month convention; do not use actual calendar days or an unadjusted annual cap. AHV/IV/FAK/VK and ALV do not necessarily share the same wage ceiling. The employer deducts employee contributions and remits both sides. [Bulletin, sections 5–6][contributions]

For working persons, contributions start on 1 January of the year they turn 18. The bulletin separately addresses apprentices/family members, remuneration in kind, pension age, self-employed persons and non-employed persons. A full-year adult employee example does not settle those cases. [Sections 1–4 and 7–14][contributions]

## Wage withholding is a separate calculation

Source withholding applies to resident employment/replacement income too. Do not classify a resident wage as outside payroll withholding because an annual assessment follows. SteG articles 24–25 and the [February 2026 wage-tax bulletin][wage] govern the category and base. Its base is wage-certificate field 8 less field 6, not take-home pay; remuneration in kind and replacement income require their own treatment.

The bulletin's **maximum ordinary withholding schedule** uses expected annual gross remuneration, annualised for a part-year liability. These are whole-base withholding percentages, not the marginal bands of final individual tax. Obtain family status and any authority instruction before choosing a rate. The table's printed bands meet at their endpoints; confirm the assigned rate for an exact disputed boundary rather than rounding the income into a convenient band. [Section II.1][wage]

| Expected annual gross CHF | Single maximum | Expected annual gross CHF | Married maximum |
|---|---:|---|---:|
| Up to 40,000 | 4% | Up to 80,000 | 4% |
| 40,000–60,000 | 5% | 80,000–140,000 | 5% |
| 60,000–80,000 | 7% | 140,000–200,000 | 7% |
| 80,000–120,000 | 9% | 200,000–250,000 | 9% |
| 120,000–160,000 | 11% | 250,000–350,000 | 11% |
| 160,000–200,000 | 13% | 350,000–450,000 | 13% |
| 200,000–300,000 | 15% | 450,000–600,000 | 15% |
| 300,000–500,000 | 17% | 600,000–1,000,000 | 17% |
| Above 500,000 | 19% | Above 1,000,000 | 19% |

The current bulletin exempts qualifying resident pupils, apprentices and students from wage withholding up to CHF 25,200 from tax year 2025, while still requiring wage-list reporting. The still-linked 2019 orientation says CHF 24,000; use the February 2026 bulletin for this figure. Do not treat that exception as a general wage-tax or social-insurance exemption. [Section II.3 and footnote][wage]

For foreign residents, inspect the January 2026 treaty annex and the actual treaty, residence, workdays and public/private employment facts. Austrian or Swiss commuter treatment is not determined by a postal address alone. SteG article 26 provides authority confirmation for exemption/reduction and a separate excess-withholding refund route. Specified board/pension payments under article 25(3) have a separate 12% rule; do not apply the ordinary wage table automatically. Treaty analysis and all exceptional payment categories remain open. [SteG, articles 24–26][law]

## Preparation and filing method

1. Retain contracts, residence/treaty evidence, birth date, employment dates, work countries, status and insurance decisions, family status, expected annual remuneration and any authority rate direction.
2. Build separate social-contribution and wage-tax bases from pay, benefits, reimbursements and replacement income. The bulletin lists the contribution-wage items; the wage-tax bulletin supplies its own base. Resolve disputed classification before calculation.
3. Calculate employee AHV/IV/FAK and capped ALV; record employer AHV/IV/FAK/VK and ALV separately. Reconcile to the provider's account and actual contribution period.
4. Calculate wage withholding under the applicable instruction, issue the wage certificate, and retain the employee/employer liability reconciliation. Benefits-only payments still require collection of the tax from the recipient under SteG article 27; do not invent a universal cash-only cap.
5. Remit ordinary wage withholding quarterly. The authority's demand letter fixes the quarterly due dates. The February 2026 bulletin states wage lists and the annual balancing payment by 31 January of the next year, with separate lists by resident municipality and foreign-residence categories. For 2026 payroll, verify the actual 2027 calendar/holiday and authority notice before assigning a final date. [SteG, articles 27–28][law]; [section III][wage]
6. Social-insurance advance payments, year-end reporting, corrections and interest use the actual institution instructions. This draft has not verified their complete due-date and sanctions chain; a wage-tax calendar is not an AHV calendar.

## Other employer costs and sanctions

The [health authority's 2026 contribution page][health] sets the monthly employer health-care amount at CHF 180.50 for adults and CHF 90.25 for the stated youth category, reduced for part-time work; age-group changes apply from the following 1 January. Its separately displayed 2027 amounts are not 2026 rates. Daily sickness insurance, accident cover and occupational pensions require applicable eligibility and provider/plan terms. Do not advertise one all-in employer percentage.

SteG article 27 makes the payer liable for underwithholding and requires corrected certification; article 28 addresses interest on a late annual difference. Exact current interest, social penalties, appeals and collection procedures remain to be reconciled. Do not calculate a fine from a statutory maximum or describe withholding as the employee's final assessed tax. [SteG, articles 27–28][law]

## Worked controls

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

## Ask before preparing and refer when unresolved

Establish coverage, contribution dates/wages, residence and treaty status, public/private employment, family status and the authority instruction. Ask for the pension/insurance plan, benefit details, current remittance notices and prior corrections. Refer disputed status, multi-country insurance/telework, every treaty entitlement, family/retirement exceptions, specialist benefits and plan pricing. The SC/PR domains, full source chain, live filing and named local accountant review remain open.

## Sources

Read 24 October 2026, within the sections identified above:

- [AHV-IV-FAK 2026 contribution bulletin][contributions], especially 1–6, 7–14. Direct PDF text and the contribution table were inspected.
- [Current Tax Act, consolidated 1 July 2026][law], selected articles 24–28. Current consolidation is not a complete within-year amendment audit.
- [Wage-tax bulletin, February 2026, treaty annex January 2026][wage]. The newer training threshold supersedes the conflicting older orientation; treaty annex facts still require transaction-specific legal review.
- [Authority wage/source-tax page][wage-page].
- [Employer health-care contributions, 2026 and separately labelled 2027][health].

[contributions]: https://www.ahv.li/fileadmin/user_upload/Dokumente/Online-Schalter/MB/AHV-IV-FAK-MB-1-01-2026--AHV-IV-FAK-ALV-Beitraege.pdf
[law]: https://www.gesetze.li/konso/pdf/2010340000
[wage]: https://www.llv.li/servicekonto/steuerverwaltung/quellensteuer-lohnsteuer-unselbstaendige-taetigkeit-und-ersatzeinkuenfte-merkblatt.pdf
[wage-page]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/lohn-quellensteuer-personalvorsorge/lohn-quellensteuer
[health]: https://www.llv.li/de/privatpersonen/gesundheit-vorsorge-und-pflege/krankenversicherung/praemien-beitraege

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
