---
name: gn-income-tax
description: "Guinea individual income-tax routing and ordinary monthly salary-tax working method for 2026. Use it to establish residence and salary territoriality, distinguish categorical taxes from the old annual IRPP idea, build the ITS base from cash pay and real-value benefits, test actual expense reimbursements and capped flat allowances, deduct employee compulsory contributions, and apply the monthly progressive bands. It separates the employee's tax from employer CNSS and salary taxes, explains local withholding, foreign-paid salary and annual employer statements, and flags year-end multi-source reconciliation. Applicability of the source versions, including any October rectifying law, must be established before live use. Non-employment income, treaty relief, exceptional payments and complete annual reconciliation remain explicit separate gaps."
jurisdiction: GN
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 1.1
---

# Guinea individual income tax and monthly ITS v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

**Governing-version prerequisite:** establish that the CGI base, cited amendments and April 2026 DGI interpretation govern the actual salary period and facts, including any October rectification effect. The final October promulgated text/effect has not been retrieved. If unresolved, label results hypothetical source-version analysis and stop before a live tax, exemption, withholding, filing or payment conclusion. An unretrieved amendment is not proof of non-enactment.

Guinea's enacted Code uses categorical income taxes. Ordinary employment remuneration is subject to monthly Impôt sur les Traitements et Salaires (ITS), not the historical Guide's general annual IRPP bands. Other jobs are separate: pensions/rentes use IPRV; property income uses [CFU](gn-property-tax.md); business/professional/agricultural profits use IBIC, IBNC or IBEA; capital income uses IRCM and non-professional property disposals use IPVI. This Guide computes ordinary salary ITS after classification; it does not apply salary bands to all personal income. [CGI 1,51-63](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §3.1](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

Article 4's residence tests include a permanent home or a stay of more than six months in the year; professional activity unless proved accessory to the principal foreign activity; centre of economic interests; habitual stay; and specified state agents abroad who are not taxed on their income there. Do not replace these alternatives with an invented universal 183-day test. Article 15 taxes residents on worldwide categorical income, except business profits governed by article 15 bis, and non-residents on Guinea-source income. Record the actual residence/treaty evidence. [CGI 4,15](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

Subject to treaties, resident salary is taxable even if the work occurs and employer is established abroad. A non-resident's remuneration is taxable where the paid work is performed in Guinea. Ordinary local employment is the calculation scope below; director remuneration, foreign payroll, pensions and multiple sources need their stated branches. [CGI 51,56,61,65](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Rates, bands and thresholds

Apply these **marginal monthly** bands to taxable salary after the documented exemptions and employee deductions. Do not apply the top rate to the whole salary or use the old annual exemption/top rate. Each row comes from article 63, corroborated by current DGI doctrine. [CGI 63](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

| Monthly taxable salary slice, GNF | Marginal rate | Official source |
|---|---|---|
| 0 to 1,000,000 | 0% | [CGI 63](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| Above 1,000,000 to 3,000,000 | 5% | [CGI 63](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| Above 3,000,000 to 5,000,000 | 8% | [CGI 63](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| Above 5,000,000 to 10,000,000 | 10% | [CGI 63](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| Above 10,000,000 to 20,000,000 | 15% | [CGI 63](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| Above 20,000,000 | 20% | [CGI 63](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |
| Specified ordinary flat allowances collectively | Exempt only up to 25% of gross salary; director/assimilated executive flat expenses remain taxable under article 52(4) | [CGI 55(3),52(4)](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf) |

The DGI précis's salary worked example and annual-statement paragraph use an inconsistent 15% allowance ceiling, despite its earlier discussion and enacted article 55(3) specifying 25%. Its example also has inconsistent tax/effective-rate figures. The law's 25% controls this method; those example figures are not copied. This allowance ceiling is not a universal 25% deduction from every salary. [CGI 55(3)](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [précis §3.2.1.3-5](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

## The base

1. Identify the employee, payer, residence, paid-work location, month and all remuneration made available, including amounts credited to an account. Reconcile the contract, payroll, payment record and benefits. Do not run a full-year or multi-employer regularisation by simply multiplying these monthly bands by twelve. [CGI 51,57,61-63,80](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
2. Start with cash salary plus taxable supplements, bonuses, incentive and distance/expatriation pay, and benefits in kind. Article 53 requires the real value of in-kind benefits. Record valuation evidence and distinguish business-use equipment from private benefit. Flat expense allowances paid to directors and assimilated executives are taxable regardless of their stated purpose. [CGI 52-53](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
3. Remove actual professional expense reimbursements only to their real substantiated amount, used for their proper purpose. Do not exempt an unsupported round-sum payment because it is labelled an expense. Separately sum the specified ordinary flat housing, transport, meal/basket, cost-of-living and chalk allowances; their collective exempt part is the smaller of the qualifying total and 25% of documented gross salary. Tax the excess. Resolve gross-salary definition or director status before relying on the cap. [CGI 52(3)-(4),55(2)-(3)](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
4. Test statutory exemptions from their actual conditions: statutory family benefits; qualifying dismissal/retirement departure compensation; work-accident benefits; apprenticeship wages under a compliant apprenticeship contract; specified public assistance; specified judicial bodily-injury annuities; and qualifying diplomatic remuneration with reciprocity and non-Guinean nationality. For trainees, article 55(10) refers to a stage no longer than twelve months and GNF 1,200,000 monthly; DGI interprets failure of either condition as making the whole stipend taxable. The automatic ordinary salary cases below do not decide these special exemptions. Voluntary resignation pay is taxable under article 54. [CGI 54-55](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §3.2.1.1](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).
5. Deduct the **employee's** compulsory social-insurance and mandatory pension contributions under article 58. Obtain the separately validated [CNSS contribution result](gn-payroll-social.md) and other compulsory-plan evidence. Do not deduct the employer CNSS share from the employee's ITS base or deduct the same pension/social payment twice. Voluntary contributions are not within the statutory mandatory deduction. Salary ITS exemptions do not automatically determine the CNSS base. [CGI 58](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §3.2.1.3](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).
6. For the ordinary monthly case, take taxable salary as gross cash/in-kind remuneration less verified exemptions and deductible employee compulsory contributions, then apply each band to its own slice. If the assembled facts produce a negative base, stop and reconcile classification/period inputs rather than create a negative salary-tax credit. Compute take-home cash from actual cash pay, employee contributions and ITS; in-kind benefits affect the tax base without automatically adding cash. Keep employer costs outside that cash reconciliation. [CGI 57-63](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).
7. Retain gross cash, benefits, each exemption and its evidence, eligible flat allowances/cap/excess, compulsory employee deductions, taxable base, each band tax, total ITS and cash reconciliation. Local employers withhold on each payment and give the beneficiary evidence of the amount withheld. [CGI 61,71](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

Article 64 calls the withholding final, but article 80 also provides year-end totalisation for same/different-source salary and pensions and an adjustment/refund-claim mechanism. Multiple employers, irregular payments, exceptional remuneration or a year-end correction therefore require the governing reconciliation method; this Guide does not silently erase article 80 or invent an annual IRPP return. [CGI 64,80](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Deadlines and filing

Withheld salary tax is paid within the first ten days of the following month under CGI 72 I as replaced by LFI 2024 article 25 and repeated by LFI 2025 article 13. The older fifteen-day text in the 2021 base is superseded. Keep this tax deadline separate from the CNSS fifteen/twenty-day source conflict. Accompany the payment with the DMU: period, payer identity/address/activity, employee count, salary paid, withholding base and total tax withheld. [LFI 2024 art. 25](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf); [LFI 2025 art. 13](https://dgb.gov.gn/wp-content/uploads/2025/02/Loi-de-Finances-Initiale-2025.pdf); [CGI 74](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

Article 76 separately requires the employer's prior-year nominative salary statement during January, expressed as by 31 January in current DGI guidance. Include employee identity/residence, cash and in-kind pay, the period where shorter than a year, relevant expense allowances and tax withheld; reconcile to monthly payroll/DMUs. Electronic declarations are required by amended article 1001 bis. Retain the electronic acknowledgement and payment evidence; no authenticated e-Tax form boxes or submission were inspected. [CGI 76](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [LFI 2025 art. 23](https://dgb.gov.gn/wp-content/uploads/2025/02/Loi-de-Finances-Initiale-2025.pdf); [DGI précis §3.2.1.5](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

Foreign-paid residents have their own salary declaration under article 65 and prior-year details under article 79. The DGI describes monthly ITS declaration followed by assessment and a recap statement. Obtain the actual assessment and filing instructions; do not assume a foreign employer has fulfilled the local duties or impose the old universal 31 March individual-return date. Cessation, transfer abroad or death have separate accelerated rules under articles 73 and 78 and require a specific calendar. [CGI 65,73,78-79](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf); [DGI précis §3.2.1.5](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx).

## Penalties and interest

An employer that fails to withhold or withholds too little is personally liable for the unwithheld amount under article 81. An employer that withholds but does not remit is assessed for what it should have paid under article 82. Employer/pension-payer fines cannot be charged against the employee's salary/pension under article 86. These liability rules do not establish every current penalty percentage or appeal deadline; do not invent them or import the CNSS surcharge into ITS. Full salary-tax sanctions and dispute procedures remain unresolved. [CGI 81-86](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Cross-border points

Apply residence, paid-work location and any actually applicable treaty before withholding. A foreign payer does not make a resident's salary exempt; foreign salary declarations follow the separate branch above. Article 51's source test is not the same question as a foreign company's permanent establishment or a social-security posting exemption. Obtain the contract, workday/location record, residence and treaty evidence separately. No treaty rate, foreign-tax credit or automatic CNSS/ITS exemption is asserted here. [CGI 4,15,51,65](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

Pensions are separately IPRV. Articles 60 and 66-70 use the article 63 monthly scale for the pension base; a Guinea-established payer withholds whether the beneficiary lives locally or abroad, subject to the governing treaty/scope. Do not automatically deduct an active employee CNSS contribution from a pension. Full pension exemptions, foreign-paid pension filing and multi-source annual reconciliation remain outside the ordinary salary computation. [CGI 51 II,60,66-70,79-80](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf).

## Two worked examples that recompute

An ordinary employee receives GNF 5,000,000 cash salary for one full month, with no benefits or exemptions. The separate CNSS workpaper establishes deductible employee contribution GNF 125,000. ITS base is GNF 4,875,000: the first million is tax free, the next two million gives GNF 100,000 and the remaining GNF 1,875,000 gives GNF 150,000. ITS is GNF 250,000 and take-home cash GNF 4,625,000. Employer contributions/taxes are separate. All source-version and scope prerequisites are assumed established.

```oa-check
name: Ordinary salary monthly ITS with separately validated employee CNSS
inputs:
  gross_cash: 5000000
  validated_employee_compulsory_contribution: 125000
steps:
  - base: gross_cash - validated_employee_compulsory_contribution
  - band_5: min(max(base - 1000000, 0), 2000000) * 0.05
  - band_8: min(max(base - 3000000, 0), 2000000) * 0.08
  - band_10: min(max(base - 5000000, 0), 5000000) * 0.10
  - band_15: min(max(base - 10000000, 0), 10000000) * 0.15
  - band_20: max(base - 20000000, 0) * 0.20
  - its: band_5 + band_8 + band_10 + band_15 + band_20
  - take_home_cash: gross_cash - validated_employee_compulsory_contribution - its
expected:
  base: 4875000
  its: 250000
  take_home_cash: 4625000
```

The second case tests evidence/classification, not an election to rename salary. An ordinary employee receives total cash GNF 8,000,000, including GNF 3,000,000 claimed as an allowance. If it is a qualifying flat allowance and documented gross salary for the cap is GNF 8,000,000, only GNF 2,000,000 is exempt; ITS is GNF 347,500 after the separately validated GNF 125,000 employee contribution. If instead documents prove that GNF 3,000,000 is genuine actual professional expense reimbursement used for its purpose, article 55(2) exempts the substantiated amount, giving ITS GNF 250,000. In both scenarios the independently checked CNSS contribution is assumed the same. The GNF 97,500 tax difference follows the facts; flat allowances cannot simply be relabelled as actual costs. Directors/assimilated executives are outside this ordinary flat-allowance case.

```oa-check
name: Capped flat allowance versus proved actual professional reimbursement
inputs:
  gross_cash: 8000000
  claimed_payment: 3000000
  confirmed_gross_salary_for_cap: 8000000
  validated_employee_compulsory_contribution: 125000
steps:
  - flat_exemption: min(claimed_payment, confirmed_gross_salary_for_cap * 0.25)
  - flat_base: gross_cash - flat_exemption - validated_employee_compulsory_contribution
  - actual_base: gross_cash - claimed_payment - validated_employee_compulsory_contribution
  - flat_tax: min(max(flat_base - 1000000, 0), 2000000) * 0.05 + min(max(flat_base - 3000000, 0), 2000000) * 0.08 + min(max(flat_base - 5000000, 0), 5000000) * 0.10 + min(max(flat_base - 10000000, 0), 10000000) * 0.15 + max(flat_base - 20000000, 0) * 0.20
  - actual_tax: min(max(actual_base - 1000000, 0), 2000000) * 0.05 + min(max(actual_base - 3000000, 0), 2000000) * 0.08 + min(max(actual_base - 5000000, 0), 5000000) * 0.10 + min(max(actual_base - 10000000, 0), 10000000) * 0.15 + max(actual_base - 20000000, 0) * 0.20
  - additional_tax_flat: flat_tax - actual_tax
  - flat_take_home: gross_cash - validated_employee_compulsory_contribution - flat_tax
  - actual_take_home: gross_cash - validated_employee_compulsory_contribution - actual_tax
expected:
  flat_exemption: 2000000
  flat_base: 5875000
  actual_base: 4875000
  flat_tax: 347500
  actual_tax: 250000
  additional_tax_flat: 97500
  flat_take_home: 7527500
  actual_take_home: 7625000
```

## Ask the client first

- What residence, treaty and work-location evidence governs the employee and month?
- Who pays, what contract/status applies, and are there other employers, pensions or exceptional payments?
- What cash, in-kind benefits and valuation records comprise remuneration made available?
- Which payments are evidenced actual costs, qualifying flat allowances or special exemptions, and is the person a director/assimilated executive?
- What independently validated compulsory employee contribution and mandatory pension amounts apply without double counting?
- What payroll, withholding proof, DMUs, annual statements, assessment notices, receipts and current source-version evidence are available?

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [DGI enacted CGI, L/2021/032/AN](https://itie-guinee.org/wp-content/uploads/2022/01/NOUVEAU-CODE-GENERAL-DES-IMPOTS.pdf), arts. 1-4,15,51-86, with neighbouring definitions, exclusions, monthly table and annual regularisation. The historical base is used with the amendments below, not represented as a current consolidation. | 2026-11-01 |
| [LFI 2024](https://dgb.gov.gn/wp-content/uploads/2024/11/Loi-de-Finances-Initiale-2024.pdf), art. 25 changing CGI 72 I to ten days, original scan and neighbours; [LFI 2025](https://dgb.gov.gn/wp-content/uploads/2025/02/Loi-de-Finances-Initiale-2025.pdf), art. 13 repeating the deadline and art. 23 on electronic declarations. | 2026-11-01 |
| [DGI Précis fiscal 2026, version 10 April](https://dgi.gov.gn/wp-content/uploads/2026/04/Guinee-Precis-fiscal-2026.04.10-VF.docx), §3.1 and complete relevant salary/pension portions of §3.2, with cover/introduction. Inconsistent 15% allowance/example passages are rejected in favour of the enacted 25% provision. | 2026-11-01 |

Not yet confirmed: October 2026 final promulgation/text/effect and applicability of all source versions; full multi-employer/irregular-payment annual reconciliation and correction forms; gross-salary boundary disputes and special director/trainee/termination valuation; detailed pension and foreign payroll filing/relief; complete IBIC, IBNC, IBEA, IRCM and IPVI computations; employer VF/TA exact base and separate training contribution; authenticated e-Tax boxes/receipts and all sanctions/appeal procedures. The country individual and payroll domains remain partial.

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
