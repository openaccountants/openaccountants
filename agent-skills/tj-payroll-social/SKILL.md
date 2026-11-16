---
name: tj-payroll-social
description: "Compute ordinary 2026 Tajikistan employer and employee social tax, reconcile net pay with the personal-income-tax skill, and prepare the unified monthly declaration working paper. Covers budget versus other organisations, payroll exemptions, registration and retirement referral."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/tj-payroll-social"
  jurisdiction: "TJ"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Tajikistan payroll and social tax v0.1

> **General reference only.** This skill prepares a working paper for review by a qualified Tajikistan professional. Confirm the facts, source version and filing procedure before filing, paying or taking a tax position.

**Built from the law. Not yet approved.** Tax year 2026; checked on 2026-11-15.


## Scope

For ordinary payroll of resident workers within art. 328(1) and its social tax; non-resident-worker liability is outside this computation. The old universal 25% employer plus 1% employee statement is true only for budget institutions. Check special regimes and statutory exclusions before applying the ordinary rates. Individual entrepreneurs, farmers and diplomatic/international-organisation cases require the separate art. 332/334 rules. [Arts. 328-334](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


## Ask the client first

- Employer identity, budget-institution or other-organisation status, registration and any special-regime approval.
- Employee identifiers, residence, main-job designation, calendar days employed and personal-deduction documents.
- Gross cash pay, bonuses, benefits, reimbursements, contracts and exemption evidence.
- Payroll month, bank cash-withdrawal/payment date and amounts already remitted.
- Social-insurance registration/individual account and current unified declaration.
- Pension status and any request for pension eligibility advice, kept separate from payroll taxation.


## The method, step by step


### Registration and social-insurance identity

For a newly registered entity, the single-window registration process includes tax, statistics and state social-insurance registration and issues the unified identifier. Retain that certificate and verify the employee insurance identifiers needed for reporting; do not assume that payroll can be run without them. The old instruction to make duplicate entity registrations is not the single-window rule. [Registration Law art. 4(2)-(4)](https://investcom.tj/uploads/post_docs/511/FtMoBDqW4mvU.pdf) and [Tax Code art. 334(9)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Determine the base, then the rates

For the resident-worker categories in art. 328(1), the ordinary base is wages, remuneration and other taxable employment benefits before deductions, including applicable benefits in kind. Arts. 329-330 also address civil-law service remuneration. Apply exclusions under art. 329(4) and exemptions under art. 331 before calculating; art. 331 incorporates art. 189(1) exempt income and also addresses specified foreign/diplomatic and state-investment-project cases. The ordinary base provisions do not set an earnings ceiling; do not invent a cap or treat every reimbursement as exempt. [Arts. 328-331](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

| Ordinary employer category, resident-worker base under art. 328(1) | Employer social tax rate | Employee social tax rate | Combined rate, derived | Official provision |
|---|---|---|---|---|
| Budget institution, resident-worker base | 25% of the applicable base | 1% of the applicable base | 26% = 25% + 1% | [Arts. 328(1), 332(1)-(2)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Other organisation, resident-worker base | 20% of the applicable base | 2% of the applicable base | 22% = 20% + 2% | [Arts. 328(1), 332(1)-(2)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |

Employer social tax is an employer cost, while employee social tax is withheld from pay. Compute each separately on the eligible base. Load [tj-income-tax](tj-income-tax.md) for the income-tax category, allowable employee-social-tax deduction and personal allowance; the old payroll instruction to withhold a universal resident income-tax rate is superseded. [Arts. 191(6), 330, 332, 334(1)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Reconcile and report

Prepare an employee schedule containing gross cash pay, taxable benefits, excluded/exempt items and reasons, social-tax base, employer tax, employee tax, income-tax computation, net pay and bank payment. Net cash pay equals cash wages less employee social tax and income tax, adjusted for documented other deductions; employer cost includes the employer social tax. These working-paper columns are a preparation method, not a claim about live portal box numbers.

The ordinary social-tax period is the calendar month. File the unified income/social-tax declaration and pay by the 15th of the following month under art. 334(5). Separately, art. 236(5)-(6) requires remittance when bank funds are obtained for wages and prohibits bank release without prior income/social-tax payment. Plan for the earlier applicable payment event, rather than treating the return date as a universal payment deferral. [Arts. 236(5)-(6), 333-334](https://www.andoz.tj/docs/kodex/TaxKodex.pdf). For Code filing/payment deadlines, day periods are calendar days unless working days are specified; if the final day is a holiday or non-working day, the deadline moves to the following working day. [Art. 4(6)-(7)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Social tax is paid to the budget and the tax authorities control collection. The Social Insurance and Pensions Agency participates in the reporting rules. Keep pension/social-insurance records distinct from the tax remittance: the old generic State Social Protection Fund label is not a verified payment-account instruction. Obtain the current recipient account and payment reference from the competent authority. [Art. 334(2), (8)-(9)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Use the Tax Committee [personal cabinet](https://www.andoz.tj/) or competent local office to obtain the current unified declaration and attachments. Match identifiers and employee totals, reconcile the accepted declaration to the ledger, retain the submission acknowledgement and bank receipt, and investigate differences before closing the payroll month. Current portal fields have not been inspected for this skill; a local filer must complete that mapping before submission.


### Retirement is a separate eligibility question

The ordinary insurance-pension ages are 63 for men and 58 for women, with contribution obligations fulfilled and at least 300 / 240 insurance months respectively. These are pension conditions, not a payroll-tax exemption. Art. 13(2)-(3) contains earlier-age routes for specified Murghob, disability, radiation-accident and family circumstances; art. 14 addresses incomplete insurance records. Refer those cases for a pension decision. [Pensions Law arts. 11, 13-14](https://nafaka.tj/46-t-dar-borai-nafaaoi-suurtav-va-davlat.html).


## Worked cases


### Other organisation: full payroll reconciliation

Illustrative resident main-job employee, enough days for the ordinary personal deduction, gross cash salary TJS 5,000 and no benefit/exemption. Other-organisation social tax is TJS 1,000 employer and TJS 100 employee. The income-tax skill gives TJS 569.28 income tax after the TJS 156 personal deduction. Net pay is TJS 4,330.72; employer cash cost is TJS 6,000; combined social tax is TJS 1,100.

```oa-check
name: Other-organisation monthly payroll
inputs:
  gross: 5000
  personal_deduction: 156
steps:
  employer_social: gross * 0.20
  employee_social: gross * 0.02
  income_tax: max(0, gross - employee_social - personal_deduction) * 0.12
  net: gross - employee_social - income_tax
  employer_cost: gross + employer_social
  combined_social: employer_social + employee_social
expected:
  employer_social: 1000
  employee_social: 100
  income_tax: 569.28
  net: 4330.72
  employer_cost: 6000
  combined_social: 1100
```


### Budget status changes both sides of social tax

Illustrative same TJS 5,000 qualifying gross pay and TJS 156 personal deduction. A budget institution owes TJS 1,250 employer social tax and withholds TJS 50 employee social tax. Income tax is TJS 575.28 and net pay TJS 4,374.72. Employer cost is TJS 6,250, TJS 250 above the ordinary other-organisation example. Classify the employer from evidence before deciding which computation applies.

```oa-check
name: Budget-institution payroll category
inputs:
  gross: 5000
  personal_deduction: 156
steps:
  employer_social: gross * 0.25
  employee_social: gross * 0.01
  income_tax: max(0, gross - employee_social - personal_deduction) * 0.12
  net: gross - employee_social - income_tax
  employer_cost: gross + employer_social
  employer_cost_difference: employer_cost - (gross + gross * 0.20)
expected:
  employer_social: 1250
  employee_social: 50
  income_tax: 575.28
  net: 4374.72
  employer_cost: 6250
  employer_cost_difference: 250
```


## When to refuse or refer

Stop if employer category, residence, main job, taxable benefit or exemption is unsupported. Refer non-employment contracts, expatriate/diplomatic cases, individual entrepreneurs/farmers, innovative-technology and other special regimes, pension eligibility and disputed insurance histories. Reaching a pension age does not by itself stop payroll withholding.


## Sources

| Official source | Read for | Date read |
|---|---|---|
| [Tax Committee, current consolidated Tax Code](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) | Read for arts. 4(6)-(7), 186, 189(1), 191(6), 236, 241(1), 328-334; ordinary categories, base, exemptions, payment and reporting. | 2026-11-15 |
| [Investment Committee, consolidated State Registration Law](https://investcom.tj/uploads/post_docs/511/FtMoBDqW4mvU.pdf) | Read for art. 4, single-window tax/statistics/social-insurance registration. | 2026-11-15 |
| [Social Insurance and Pensions Agency, Pensions Law](https://nafaka.tj/46-t-dar-borai-nafaaoi-suurtav-va-davlat.html) | Read for arts. 11, 13-14, ordinary ages and neighbouring early/incomplete-record exceptions. | 2026-11-15 |
| [Social Insurance and Pensions Agency, June 2026 amendment No. 2281](https://nafaka.tj/563-onuni-umurii-toikiston-oid-ba-vorid-namudani-tajirot-ba-onuni-umurii-toikiston-dar-borai-nafaaoi-suurtav-va-davlat.html) | Read for entire amending law; no change to art. 13 age conditions. | 2026-11-15 |

Not yet confirmed: Current unified-declaration fields, payment-account references and individual insurance-registration workflow; exact allocation of social tax between pension, insurance and employment programmes; special-regime relief and individual pension awards. Do not use the old fund label as a payment destination.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `tj-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/tj-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
