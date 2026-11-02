---
name: tg-payroll-social
description: >
  Togo payroll and social contribution reference for the 2026 tax year, covering private employees, employer withholding, the general CNSS regime and compulsory health insurance under AMU. Use it for IRPP payroll, salary contributions, pension, prestations familiales, risques professionnels, assurance maladie universelle, ADC and DAS. It separates the employee withholding base from the CNSS and AMU contribution bases, records the ordinary employer and employee allocations and their deadlines, and links the annual income tax calculation to the personal income tax Guide. Independent, informal and voluntary CNSS categories are identified separately. The Guide also records unresolved current wage floor evidence, declaration interfaces and nonemployee health contributions rather than extending employee percentages to everyone.
jurisdiction: TG
category: payroll
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
tier: 2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Togo Payroll and Social Contributions v1.0

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This Guide covers ordinary private employment and CNSS/AMU collection, with separate nonemployee routes. The employer withholds IRPP on each taxable payment and records it on the payslip. [LPF art. 26](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). The annual income base, family conditions and tax bands are owned by [Personal income tax](tg-income-tax.md). CNSS and AMU are distinct charges, with different bases and late-payment rules; their rates must not be collapsed into one unsupported net-pay percentage.

## Rates, bands and thresholds

| Item and conditions | 2026 rule | Official source |
|---|---|---|
| CNSS pensions, private employees | Employer 12.5%, worker 4% | [Décret 2012-038, official CNSS rate explanation](https://cnss.tg/prestations/recouvrement/) |
| CNSS family/maternity and professional risk | Employer 3% plus 2%; employer general total 17.5%, worker 4%, combined 21.5% | [Décret 2012-038, official CNSS rate explanation](https://cnss.tg/prestations/recouvrement/) |
| Other CNSS categories | Independent 21.5%; informal economy 19.5%; voluntary pension insurance 16.5%; each on its category base | [CNSS, sections 1-2](https://cnss.tg/prestations/recouvrement/) |
| AMU private employee ordinary allocation | 10% total; art. 29 specifies 5% employer and 5% worker; art. 12 requires at least half to be borne by employer | [Décret 2023-096, arts. 12, 29](https://cnss.tg/cnss-media/2024/01/DECRET-2023-096-fixant-les-taux-de-cotisations-AMU.pdf) |
| Public agents and pensioners, separate AMU categories | Public agents 10%, split equally; pensioners 5% of monthly pension | [Décret 2023-096, arts. 13-19](https://cnss.tg/cnss-media/2024/01/DECRET-2023-096-fixant-les-taux-de-cotisations-AMU.pdf) |

## The base

For CNSS, include all remuneration, bonuses, commissions and cash/noncash advantages, excluding expense reimbursements and family benefits. The contribution base cannot be below the current SMIG. The official source read gives an entire-remuneration basis; no contribution ceiling has been established, so do not invent one. For apprentices/students/stagiaires the described category wage and actual-higher-pay tests apply. Independent IRPP taxpayers use the income-tax-declared base; independent IS taxpayers use average monthly income, and informal workers use declared/category income, subject to the stated floor rules. [CSS art. 12 and CNSS, section 1](https://cnss.tg/prestations/recouvrement/).

AMU employee contributions use basic salary plus taxable bonuses and allowances, excluding expense reimbursements and family benefits, with an SMIG floor. Multiple employers contribute proportionately to their remuneration. Separate independent/informal AMU bases and amounts need the category determination; employee percentages do not establish those amounts. [Décret 2023-096, arts. 9-12, 20-23](https://cnss.tg/cnss-media/2024/01/DECRET-2023-096-fixant-les-taux-de-cotisations-AMU.pdf).

Build three schedules: taxable pay for IRPP, CNSS assessable remuneration and AMU assessable remuneration. Then deduct the employee charges from pay, add employer charges to employer cost, and apply the personal-income rules to the proper net annual tax base. Reimbursements or benefits excluded for one purpose are not automatically excluded for every purpose.

## Deadlines and filing

Withhold IRPP at every payment; remit by the 15th of the following month with the dated/signed bordereau identifying period, employer and total. Preserve payment records for ten years. Unwithheld income and related regularisations have the art. 27 following-15-January requirement. DAS is due by 31 January; private salaried employers of domestic personnel have the art. 28 annual-payment exception. [LPF arts. 26-28](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).

CNSS: the employer owes both shares. Complete each month's appel de cotisations (ADC), including employer number, period, employee count, wage mass by branch, each charge and total; sign, stamp and submit with payment. Contributions are paid within the first 15 days of the following month; check the actual ADC due date. [CSS art. 16 and CNSS sections 3-5](https://cnss.tg/prestations/recouvrement/).

AMU: remit by the 15th of the following month, with the nominal statement and dependent information required by the managing organisation. The employer is liable for the total charge. New employee identification/remuneration information is due within 60 days of entry. The decree makes contributions due from 1 January 2024. [Décret 2023-096, arts. 6-7, 30-34, 47](https://cnss.tg/cnss-media/2024/01/DECRET-2023-096-fixant-les-taux-de-cotisations-AMU.pdf). Current electronic screens, payroll table fields and DNR filing frequency must be obtained before running a live payroll submission.

## Penalties and interest

CNSS arrears incur 5% at the due date, plus 1% per month or part after three months from that date. [CSS art. 17, CNSS section 6](https://cnss.tg/prestations/recouvrement/). AMU has a different 2% per month or fraction, without prejudice to legal-rate interest; a reduction request requires principal payment first, and an appeal does not stop accrual. [Décret 2023-096, arts. 32-33](https://cnss.tg/cnss-media/2024/01/DECRET-2023-096-fixant-les-taux-de-cotisations-AMU.pdf). IRPP withholding is subject to the separate LPF late-payment and withholding sanctions. [LPF arts. 115, 128-135](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). Do not use the CNSS rate for AMU arrears.

## Cross-border points

For internationally mobile staff, establish work location, fiscal domicile, paying employer and any treaty or social-security agreement before deciding withholding and coverage. The domestic fiscal-domicile rule is in CGI arts. 2-3; no treaty payroll exemption or foreign social-insurance waiver is established here. Use [Cross-border](tg-cross-border.md).

## Two worked examples that recompute

A private employee has independently confirmed CNSS and AMU monthly bases of CFA 300,000, above the relevant floor. Under the ordinary allocation, employee charges total CFA 27,000 and employer charges CFA 67,500. This stops before IRPP and does not assume the two assessable bases always match.

```oa-check
name: Monthly employee and employer contribution schedules
inputs:
  cnss_base: 300000
  amu_base: 300000
steps:
  - employee_cnss: cnss_base*0.04
  - employer_cnss: cnss_base*0.175
  - employee_amu: amu_base*0.05
  - employer_amu: amu_base*0.05
  - employee_total: employee_cnss+employee_amu
  - employer_total: employer_cnss+employer_amu
expected:
  employee_total: 27000
  employer_total: 67500
```

An employee has CFA 3.6 million annual gross cash pay, no benefits or other deductions, CFA 144,000 mandatory CNSS and CFA 180,000 AMU employee contributions. After contributions and the 28% professional deduction, the base is CFA 2,358,720. Two qualifying dependants for the full year reduce the rounded base to CFA 2,118,000 and annual IRPP to CFA 36,540. Without documented dependant entitlement it is CFA 43,740, a CFA 7,200 difference. This is an annual reconciliation under CGI arts. 26 and 72-74; obtain the prescribed monthly withholding method before submitting payroll.

```oa-check
name: Annual employment deduction and dependant decision
inputs:
  gross: 3600000
  cnss: 144000
  amu: 180000
  dependants: 2
steps:
  - after_contributions: gross-cnss-amu
  - professional_deduction: min(after_contributions,10000000)*0.28
  - net_before_family: after_contributions-professional_deduction
  - with_family: floor(max(net_before_family-dependants*10000*12,0)/1000)*1000
  - without_family: floor(net_before_family/1000)*1000
  - tax_with: floor((with_family-900000)*0.03/10)*10
  - tax_without: floor((without_family-900000)*0.03/10)*10
  - saving: tax_without-tax_with
expected:
  with_family: 2118000
  tax_with: 36540
  tax_without: 43740
  saving: 7200
```

## Ask the client first

Obtain employment category and locations, gross cash and benefits, expense reimbursements, employee pension/social/AMU statements, contribution-category registration, current SMIG evidence and the actual bases, dependent documents, new-entry dates, ADC/AMU notices, year-to-date tax and the current payroll withholding table.

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| CGI (loi n°2018-024) and LPF (loi n°2018-025), OTR consolidation 2025, archived official copy. Relevant articles specified above, including neighbouring conditions; actual read scopes in the source manifest. Official live download returned 404 after site migration. Current-year archived OTR PDF read locally. | https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html | 2026-11-01 |
| CNSS, Recouvrement. Sections 1-6: base under CSS art. 12, decree 2012-038 rates, payment, ADC and CSS art. 17 penalties. | https://cnss.tg/prestations/recouvrement/ | 2026-11-01 |
| Décret n°2023-096/PR du 4 octobre 2023, AMU. Arts. 1-23, 29-47: employee base/split, nonemployee rules, collection, penalties and commencement; scanned eight-page text read locally. | https://cnss.tg/cnss-media/2024/01/DECRET-2023-096-fixant-les-taux-de-cotisations-AMU.pdf | 2026-11-01 |

Not yet confirmed: An enacted/current primary source establishing the 2026 numeric SMIG (the old CFA 52,500 assertion is withheld until checked for current operation); a contribution ceiling (none is established by the primary explanation read); current DNR periodicity and exact portal/ADC/AMU screen fields; independent/informal AMU category contribution amounts; directors outside the qualifying manager rule; old 3% salary-tax claim; actual monthly IRPP table/annualisation and rounding workflow. PR and SC remain partial; do not label this a complete payroll engine.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
