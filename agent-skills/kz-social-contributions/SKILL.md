---
name: kz-social-contributions
description: "Kazakhstan 2026 pension, social and health payments: payer-specific bases, rates, caps, exemptions and remittance dates."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kz-social-contributions"
  jurisdiction: "KZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Kazakhstan mandatory social payments v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Ordinary individual entrepreneurs paying for themselves and employers paying staff. This computes the social-payment layer, not ИПН, VAT, CIT or simplified income tax. Load `social-contributions-workflow-base`. Identify pension/health exemptions, date of birth, employment status and the exact regime before calculating. Special self-employed app/platform payments use `kz-simplified-regime` instead. Reply in the user’s language and retain ОПВ, ОПВР, СО, ОСМС, СН, МЗП and МРП.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| 2026 base units | МЗП KZT 85,000; МРП KZT 4,325 (budget law art. 7) | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru |
| ОПВ, employee | 10% of qualifying monthly income; maximum base 50 МЗП per agent (Social Code art. 249) | https://www.gov.kz/org/astana-uzsp/documents/details/1060115?lang=ru |
| ОПВ, ordinary ИП for self | 10% of independently chosen eligible income, tied to the СО choice and not exceeding taxable income; 50 МЗП cap. When actual income is below 1 МЗП, payment from 1 МЗП is a right, not an absolute required floor (art. 249) | https://www.gov.kz/org/astana-uzsp/documents/details/1060115?lang=ru |
| ОПВР | 3.5% during 2026; 4.5% during 2027; 5% from 2028. Ordinary monthly base 1–50 МЗП, with special-regime exceptions (art. 251) | https://www.gov.kz/org/astana-uzsp/documents/details/1060115?lang=ru |
| ОПВР birth/exempt status | Birth before 1 January 1975 is exempt, so 1 January 1975 is included; other exemptions under art. 248 must be checked | https://www.gov.kz/org/astana-uzsp/documents/details/1060115?lang=ru |
| СО, ordinary employee | 5% of qualifying income less ОПВ and statutory exclusions; base normally 1–7 МЗП from each payer (arts. 244–245) | https://www.gov.kz/org/astana-uzsp/documents/details/1060115?lang=ru |
| СО, ordinary ИП for self | 5% of chosen eligible income, equal to pension-choice income and not above actual taxable income; base minimum 1 МЗП when income is lower, maximum 7 МЗП (art. 245) | https://www.gov.kz/org/astana-uzsp/documents/details/1060115?lang=ru |
| ВОСМС employee / ОСМС employer | Employee 2%, base cap 20 МЗП; employer 3%, base cap 40 МЗП; eligible income and exemptions still apply | https://www.gov.kz/org/minfin/press/article/details/235407?lang=ru |
| ОСМС ordinary ИП for self | 5% × 1.4 МЗП = KZT 5,950 monthly (derived); exemption/suspension status must be checked | https://www.gov.kz/org/minfin/press/article/details/235407?lang=ru |
| Ordinary legal-entity social tax | 6% of art. 556 base after ОПВ, ВОСМС and other statutory exclusions; no СО offset (arts. 556–558) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| General-regime ИП social tax | 2 МРП for self and 1 МРП per employee, using МРП on payment date; income/suspension exclusions in art. 556 apply (art. 557) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Special-regime social tax | Self-employed, simplified and farm special-regime taxpayers are not social-tax payers (art. 555); do not add СН to their ordinary contributions | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Separate employee deductions (ОПВ and ВОСМС) from employer-funded ОПВР, СО, employer ОСМС and social tax. Social tax and social contributions are different charges. The pre-2026 СН-minus-СО offset is gone. For a legal-entity employer, the ordinary social-tax base is not gross payroll: apply art. 556 exclusions and its minimum-base rule; for an ИП use the fixed per-person rule.

The ОПВР phase-in began at 1.5% in 2024 and 2.5% in 2025 (art. 251). Do not use these historical rates for 2026. Check all art. 248 exemptions, including retirement, specified indefinite disability and service categories; birth date alone is insufficient. Ordinary ИП themselves are within the employer-pension contribution system subject to the applicable exemptions. For СО, the ИП selected income is expressly tied to pension-choice income, rather than an unresolved automatic subtraction of ОПВ. Do not choose a base exceeding actual taxable income; the low-income statutory floor rules still apply. For employees, subtract qualifying ОПВ before СО and observe the per-payer cap.

The previous employee-health cap of 20 МЗП remains, while employer health rises to 40 МЗП in 2026. Derived maxima using the 2026 МЗП are KZT 34,000 employee and KZT 102,000 employer. Do not reuse the old employer cap of 10 МЗП. Multiple payers, employment plus ИП income, disability, pensioners, foreign/EAEU workers, civil servants/military, hazardous work and unified-payment elections require their own coordination/exemption analysis. Do not assert a blanket aggregation across all contribution types.

## Deadlines and filing

СО: monthly by the 25th of the following reporting month under Social Code art. 246; special civil-contract/self-employed timing is specified separately there. ОПВ and ОПВР: employer remittance by the 25th after income-payment month; ordinary ИП self-payment by the 25th after the reporting month (Social Code art. 248(8)(1)–(2), UAPF official contribution table). Health: employer by the 25th after payment month; ИП self-payment by the 25th after reporting month (Health Fund FAQ Q10). Social tax by the 25th after the tax month (Tax Code art. 560). Do not defer ordinary monthly payments to year end. Use the appropriate bank/State Corporation payment channel with beneficiary, individual identifier and reporting month; reconcile fund allocations and acceptance. Quarterly employer reporting is separate under arts. 444–445/561; use the current Form 200.00 package, with regime-specific reporting confirmed before filing.

## Penalties and interest

Late-payment interest and arrears are separate from the contribution calculation. Check the fund-specific current provision, payment date and exempt status before quantifying any sanction. No unverified combined payroll burden or penalty percentage is used.

## Cross-border points

Foreign/EAEU coverage, dual employment/self-employment, treaties and cross-payer caps are referral boundaries. Do not assume every foreign worker pays the resident ordinary package. Voluntary pension contributions, pension withdrawals and investment returns are outside this skill.

## Two worked examples that recompute

Case 1: an ordinary ИП on simplified, no employees, eligible for ОПВР and choosing an actual eligible income/base of KZT 85,000, owes ОПВ 8,500 + ОПВР 2,975 + СО 4,250 + health 5,950 = KZT 21,675; no separate social tax. This is not the special non-ИП self-employed app regime.

```oa-check
name: Ordinary simplified IP chosen base
inputs:
  chosen: 85000
  mw: 85000
steps:
  - opv: chosen * 0.10
  - opvr: chosen * 0.035
  - so: chosen * 0.05
  - health: 1.4 * mw * 0.05
  - total: opv + opvr + so + health
expected:
  opv: 8500
  opvr: 2975
  so: 4250
  health: 5950
  total: 21675
```

Case 2: general-regime ИП chooses KZT 255,000 eligible own income and has 1 employee on KZT 300,000 gross, both non-exempt. Own charges including 2 МРП social tax total KZT 61,775. Employee employer-funded charges are KZT 37,325 (ОПВР 10,500 + СО 13,500 + health 9,000 + fixed СН 4,325); employee pension and health withheld total KZT 36,000 before ИПН.

```oa-check
name: General IP self and one employee
inputs:
  own: 255000
  salary: 300000
  mw: 85000
  mrp: 4325
steps:
  - own_total: own * (0.10 + 0.035 + 0.05) + 1.4 * mw * 0.05 + 2 * mrp
  - employee_opv: salary * 0.10
  - employer_total: salary * 0.035 + (salary - employee_opv) * 0.05 + salary * 0.03 + mrp
  - withheld: employee_opv + salary * 0.02
expected:
  own_total: 61775
  employer_total: 37325
  withheld: 36000
```

Case 3: for hypothetical actual eligible ИП income of 60 МЗП, the ОПВ and ОПВР monthly bases cap at 50 МЗП, СО at 7 МЗП; ordinary fixed ИП health remains unchanged. Derived contributions are KZT 425,000, 148,750, 29,750 and 5,950 respectively. A general-regime social tax, where due, is additional.

```oa-check
name: Ordinary IP ceiling comparison
inputs:
  chosen: 5100000
  mw: 85000
steps:
  - opv: min(chosen, 50 * mw) * 0.10
  - opvr: min(chosen, 50 * mw) * 0.035
  - so: min(chosen, 7 * mw) * 0.05
  - health: 1.4 * mw * 0.05
expected:
  opv: 425000
  opvr: 148750
  so: 29750
  health: 5950
```

## Ask the client first

- Exact regime and ИП/legal-entity employer status?
- Actual and chosen eligible income, payment month and employee earnings/exclusions?
- Birth dates, pension/disability/service/foreign-worker exemptions?
- Other payers, employment plus ИП income and unified-payment elections?
- Fund allocations, arrears and contribution history?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Social Code arts. 243–251, including ordinary and special base exceptions | https://www.gov.kz/org/astana-uzsp/documents/details/1060115?lang=ru | 2026-11-14 |
| Read for Tax Code arts. 555–561 and reporting arts. 444–445 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |
| Read for 2026 budget law art. 7 | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru | 2026-11-14 |
| Read for Health Fund rates, caps and remittance timing Q8–15 | https://www.gov.kz/org/minfin/press/article/details/235407?lang=ru | 2026-11-14 |
| Read for UAPF ordinary employer/ИП contribution and timing table | https://www.enpf.kz/ru/services/pension/ups/330/281181/?sphrase_id=17549487 | 2026-11-14 |

Not yet confirmed: Cross-payer and foreign/EAEU coordination; special exempt categories; unified-payment election calculations; current electronic declaration boxes; OPV payment timing for special classes; numeric late-payment sanctions. Do not use the old gross-pay social-tax base, employer-health 10-МЗП cap, unconditional pension minimum, or a year-end deferral assumption.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kz-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kz-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
