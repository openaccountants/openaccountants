---
name: cameroon-payroll
description: "Cameroon payroll for 2026: gross-based salary IRPP deductions and CAC, CNPS handoff, CFC/FNE, full local-development and audiovisual bands, wages, payslips, employer cost and separate statutory filing duties."
version: 0.2
jurisdiction: CM
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Cameroon payroll v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026, calendar 1 January–31 December. The prior file attributed review to **Nkinyam Courage Ndasi** on 2026-06-21. That historical credit is preserved; it does not approve this rewrite, which has not been reviewed by an accountant. All amounts are XAF/FCFA; do not invent FX or treat Cameroon as a no-PIT jurisdiction. The original identifier 3472800 is retained solely as an unverified historical identifier, not a current credential or approval.

## Who this applies to

Employers calculating pay, salary IRPP/PAYE and payroll levies for covered Cameroon employees. Direction Générale des Impôts (DGI), Ministry of Finance administers tax; Caisse Nationale de Prévoyance Sociale (CNPS) administers its separate social branches. Load [social contributions](cameroon-social-contributions.md) for the current CNPS rate/base/coverage owner. Payroll covers cash pay, benefits, allowances, employee deductions, employer cost, bank reconciliation and filings; gross/net salary is not business turnover.

CGI 25 domicile depends on home/main stay, professional activity unless accessory, or economic interests, subject to treaties.30 taxes employment income from work in Cameroon; pensions have payer-location rules. Do not treat a foreign national's 183 day count as an automatic residence or social-coverage decision. Public-sector special schemes, expatriate detachments, nonresidents and treaties require the actual coverage and treaty evidence; no nationality exemption is presumed.

## Rates, bands and thresholds

| Item | Rule / amount in XAF unless stated | Official source |
|---|---|---|
| Salary annual scale | Net salary 0-2,000,000:10%; next 1,000,000:15%; next 2,000,000:25%; excess above 5,000,000:35%. | CGI 69(1): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Salary CAC | 10% of principal IRPP. Derived effective marginal rates 11%/16.5%/27.5%/38.5%; do not add CAC twice. | CGI 71: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Annual cumulative tax | Derived including CAC: at net 2,000,000 tax 220,000; at 3,000,000 tax 385,000; at 5,000,000 tax 935,000. | CGI 69(1);71: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Professional expense deduction | 30% of gross taxable pay and benefits, capped at 4,800,000/year; compulsory retirement contributions are a separate deduction. Do not compute 30% only after pension. | CGI 34: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Salary abatement | 500,000/year after net category computation, for salaries/wages. The unchanged income-tax sibling omits it; use actual 29 here for salary work. | CGI 29: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Employer salary withholding floor | Gross salary below 62,000/month: employer relieved of IRPP withholding. This is not an exemption from every other levy. | CGI 81: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Benefit valuation | On gross taxable salary: housing 15%, electricity 4%, water 2%, per domestic servant 5%, per vehicle 10%, food 10%, telephone 5%, fuel 10%, security 5%, internet 5%. Unlisted benefits use actual value. Cash substitutes use actual amount unless expressly exempt. | CGI 33: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CFC employee/employer | Employee 1%; employer 1.5%. Employer base includes salary/allowances/emoluments and benefits at actual amount; employee base follows the gross statutory base. No CNPS 750,000 cap applies to these taxes. | Law 77/10 art 4; Law 90/050 art 6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| FNE employer | 1%, no employee FNE. Derived employer CFC+FNE2.5% only if both obligations apply on the relevant base; employer exemptions can differ from employee liability. | Law 90/050 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CFC/FNE rounding | Round contribution base down to 1,000; this statutory rounding is not proof of an identical salary-IRPP rounding rule. | Law 90/050 art 6(3): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CFC/FNE statutory remittance | First 20 days of next month; when monthly levy is below 25,000, statutory quarterly admission within first 20 days of next quarter. Verify actual current combined-return calendar rather than replace this with a blanket 15th. | Law 90/050 art 7: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Monthly IRPP | Withhold at each taxable payment, show it on payslip and remit by 15th of next month; use DIPE bulletin/document actually supplied by administration. | CGI 81-83: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Annual employer DIPE | For the 18 company results return: DGE15 March, medium/specialised centres 15 April, local/individual centres 15 May; DIPE accompanies that return. Do not call every employee return 15 March. | CGI 18(1),(3): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Annual recipient statement | Payer supplies detailed prior-calendar-year income and withholding statement to recipient by 15 March. | CGI 74 bis(5): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Employee annual recap | Public/parapublic staff and designated senior personalities 31 July; staff of DGE/medium/specialised private employers 30 September; other individuals 31 October, for prior-year income. | CGI 74 bis(1): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV collection | First 20 days of next month, on gross salaries actually received; annual individual/monthly recap within results-return deadline. | Ordinance 89/004 arts 3,7,9: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Minimum wage, agriculture | 45,000/month agricultural/related sector; other sectors 60,000/month under 2023 decree from 21 March 2023. Apply category and actual collective/contractual entitlement; this is a wage floor, not net pay. | Decree 2023/00338 art 1: https://www.spm.gov.cm/site/sites/default/files/dpm_2023-00338_s.pdf |
| Minimum wage, State Labour Code employees | 43,969/month from 23 February 2024 for this State Labour Code category, replacing historical 41,875 under 2023 decree. Do not apply it to all civil servants or private workers. | Decree 2024/0168 art 1: https://www.spm.gov.cm/site/sites/default/files/decree_no_2024_0168.pdf; Decree 2023/00338 art 1, historical State 41,875: https://www.spm.gov.cm/site/sites/default/files/dpm_2023-00338_s.pdf |
| Retention | Tax books/registers/support 10 years from last recorded operation or document creation. | LPF L5: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| DGI late declaration/payment | Self-assessed declaration/payment:10% per month capped 30% of principal; collection interest 1.5% per month underL106 start/end rules, without a generic 30-day grace. | LPF L106: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| DGI understatement | Assessment interest 1.5%/month capped 50%, plus 30% good faith,100% bad faith,150% fraud. Spontaneous payment of accepted audit assessments has the separate 15% principle penalty under L96(2), which cannot subsequently be remitted or transacted. | LPF L95-L98: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CFC/FNE annex sanctions | Employer contribution unpaid:1%/month or fraction under amendinglaw 10(2); missing annual 9 statement 10,000 fine. Do not assume every levy uses the same DGI/CNPS penalty. | Law 90/050 art 10: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV missing declaration | 10,000 fine under ordinance 8(5); nonwithholding/nonpayment/latepayment follow its 10 reference to salary direct-tax rules. | Ordinance 89/004 arts 8(5),10: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |


### Local development tax (TDL), actual basic-salary bands

The old name “Taxe Communale Libératoire” and universal>500,000 threshold do not describe C86. It is taxe de développement local, an annual charge for employees collected with IRPP underC87/C88. The equal-month allocations below are derived for a stable full-year workpaper, not a verified partial-year/cessation method. The old 2,520 top charge is corrected to 2,500 as this derived monthly equivalent.

| Item | Rule / amount in XAF unless stated | Official source |
|---|---|---|
| TDL basic monthly salary 62,000-75,000 | 3,000/year; derived equal-month allocation 250. Statutory band uses basic salary, not automatically gross taxable salary. | CGI C86(3)a; C87: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| TDL basic monthly salary 75,001-100,000 | 6,000/year; derived equal-month allocation 500. Statutory band uses basic salary, not automatically gross taxable salary. | CGI C86(3)a; C87: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| TDL basic monthly salary 100,001-125,000 | 9,000/year; derived equal-month allocation 750. Statutory band uses basic salary, not automatically gross taxable salary. | CGI C86(3)a; C87: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| TDL basic monthly salary 125,001-150,000 | 12,000/year; derived equal-month allocation 1,000. Statutory band uses basic salary, not automatically gross taxable salary. | CGI C86(3)a; C87: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| TDL basic monthly salary 150,001-200,000 | 15,000/year; derived equal-month allocation 1,250. Statutory band uses basic salary, not automatically gross taxable salary. | CGI C86(3)a; C87: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| TDL basic monthly salary 200,001-250,000 | 18,000/year; derived equal-month allocation 1,500. Statutory band uses basic salary, not automatically gross taxable salary. | CGI C86(3)a; C87: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| TDL basic monthly salary 250,001-300,000 | 24,000/year; derived equal-month allocation 2,000. Statutory band uses basic salary, not automatically gross taxable salary. | CGI C86(3)a; C87: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| TDL basic monthly salary 300,001-500,000 | 27,000/year; derived equal-month allocation 2,250. Statutory band uses basic salary, not automatically gross taxable salary. | CGI C86(3)a; C87: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| TDL basic monthly salary above 500,000 | 30,000/year; derived equal-month allocation 2,500. Statutory band uses basic salary, not automatically gross taxable salary. | CGI C86(3)a; C87: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |


### Audiovisual royalty (RAV / CRTV), gross-salary bands

The top band is not the only taxable band. Its base is gross salary received under ordinance 3. Pensions/life annuities, domestic staff salaries and workers of individual agricultural/pastoral operations are exempt under 6, with the precise category established. Do not infer exemption merely because salary is below 1,000,000 or income-tax withholding is relieved.

| Item | Rule / amount in XAF unless stated | Official source |
|---|---|---|
| CRTV gross monthly salary 0-50,000 | 0/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 50,001-100,000 | 750/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 100,001-200,000 | 1,950/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 200,001-300,000 | 3,250/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 300,001-400,000 | 4,550/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 400,001-500,000 | 5,850/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 500,001-600,000 | 7,150/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 600,001-700,000 | 8,450/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 700,001-800,000 | 9,750/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 800,001-900,000 | 11,050/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary 900,001-1,000,000 | 12,350/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CRTV gross monthly salary above 1,000,000 | 13,000/month, subject to ordinance 6 exemptions. | Ordinance 89/004 arts 3,6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |


## The base

### Salary IRPP computation and deductions

Establish taxable gross from cash salary, bonuses/gratuities/13th-month pay, allowances and valued benefits (32-33). CGI 31 exempts: (1) job-cost allowances actually used for their purpose and not excessive; (2) family benefits; (3) State/local/public-establishment assistance and insurance benefits under the relevant laws/decrees; (4) temporary indemnities, benefits and life annuities for work-accident victims or heirs; (5) court-awarded personal-injury life annuities only where permanent TOTAL incapacity requires third-person assistance for ordinary acts of life; (6) the complément forfaitaire de solde paid to civil servants; (7) armed-forces service injury/disability pensions; (8) study grants; (9) capital received as pension OR death indemnity OR consolidated death/injury compensation; (10) correction-index salary increases for State civil servants/agents on diplomatic or consular missions abroad; (11) work-medal gratuities on medals awarded by the Ministry responsible for Labour; and (12) the damages component of statutory dismissal indemnity, excluding compensation for lost salary. Keep the particular paragraph and supporting facts; an allowance label does not establish exemption.

For a stable ordinary annual salary:

1. Taxable grossG includes taxable benefits; separate exempt items first.
2. Professional expensesP=min(30%×G, annual cap). This is calculated on gross, not on gross less CNPS.
3. Deduct actual mandatory retirement contributions paid to State/CNPS under 34, using proved coverage/contribution amounts. Do not deduct an employer branch or every payroll levy as employee pension.
4. Apply the salary abatement in 29. Annual salary-category base=max(0, G-P-mandatory retirement-abatement). Here “abatement” means the statutory salary amount, not another professional deduction.
5. Apply progressive 69 bands and 71 CAC once. No marital/single code or dependent-rate band is invented. Net negative base does not create a tax credit.

The old identical “pension then 30% then 500,000” formula understates/overstates components because 30% must be gross-based and capped. The passing income-tax sibling also omits 29 abatement; its salary cases are not the authority for this job. Its non-salary categories remain separate, unchanged.

The current statute does not establish the old annual-net-salary round-down-to 1,000 rule in the paragraphs read. The historic DGI monthly-table note included in 2026 code still uses obsolete employee CNPS 2.8%/300,000 parameters. It is not a current-rate calculator. Annual/12 below is an estimate for stable-year cash flow, not a verified monthly filing table or legal rounding instruction. Irregular pay, multiple employers and entry/exit months require the actual current withholding method.65 bis has special nonrecurring exceptional-income conditions, a comparison with prior 3 years and alternative treatment; bonuses are not automatically all eligible. Refer that special computation rather than silently apply the stable-salary method to it.

### Benefit and contribution bases are different

Apply 33 benefit percentages to gross taxable salary; cash substitutes and unlisted benefits use actual amount unless expressly exempt. Use actual detail; do not omit known benefits because only cash data were supplied. The CNPS owner separately covers statutory contribution exclusions and capped pension/family versus uncapped risk. All CNPS branches are not capped. Unknown risk or reduced family regime needs actual CNPS evidence; show labelled alternatives, not an invented middle/minimum default.

CFC employee base is the gross statutory wage base in 77/10 art 4; employer base is actual salary, allowances/emoluments and benefits. Employer FNE/CFC exemptions in 90/050 art 3 include State, communes, consular chambers, diplomatic/consular missions, qualifying nonprofit associations under implementing conditions, individual agricultural/livestock operators, private educational establishments, religious hospitals and the specified socioprofessional/secular establishments. Confirm the exact legal entity and decree conditions.77/10 art 5 also exempts family benefits, pensions/life annuities, domestic staff pay and qualifying individual agricultural/pastoral wages from levy. Do not transfer an employer exemption automatically to another employee obligation. These taxes are not reduced by the CNPS ceiling; calculate each on its own properly rounded base.

### Payslip, employer cost and working paper

Record Employee name, NIU/CNPS number, Tax year, Prepared date, employer and employee coverage/registration, currency/frequency, basic salary, cash components, exempt allowances, actual/valued benefits, taxable gross, actual mandatory pension, gross-based professional deduction/cap, salary abatement, annual/category IRPP, monthly estimate/actual withholding basis and CAC. Keep the CNPS assessed bases/class/regime, each employee/employer branch, employee/employer CFC and FNE, basic-salary TDL annual liability/monthly allocation, gross-salary CRTV/exemption, net pay, employer on-cost and fully loaded cost. Show payments, receipts, opening arrears, reconciliations and all assumptions/flags.

Net pay=cash gross less actual employee pension, salary tax, CFC, TDL/CRTV collected and any other authorised deductions, with proper treatment of noncash benefits. Employer cost=cash pay/benefit cost plus actual employer pension/family/uncapped-risk, employer CFC/FNE where liable and other documented employment costs. Never omit family or applicable levies; never conflate noncash taxable value with cash disbursement.

### Bank patterns and local terminology

| Case-insensitive narrative | Investigate / classification after matching supporting record |
|---|---|
| SALAIRE, PAIE, VIREMENT SALAIRE, NET A PAYER; VIREMENT [employer], REMUNERATION | Salary/net-pay movement; distinguish employee credit from employer debit |
| PRIME, BONUS, GRATIFICATION,13E MOIS | Taxable pay unless a specific exemption/special exceptional-income condition is established |
| INDEMNITE | Identify actual allowance and 31 conditions, never exempt automatically |
| REMB CNPS, REMBOURSEMENT CNPS | Refund/reversal or benefit, not automatically taxable salary; inspect the original item |
| DGI, IMPOT, IRPP, DIPE, PRECOMPTE | Salary-tax/other Treasury settlement; reconcile actual liability |
| CAC, CENTIMES ADDITIONNELS | Surcharge within the relevant tax, not another gross-pay tax |
| CNPS, COTISATION CNPS, PREVOYANCE SOCIALE | Separate employee withholding liability from employer contribution expense |
| CFC, CREDIT FONCIER; FNE, FONDS NATIONAL EMPLOI | Housing/employment fund tax levies, separate from CNPS |
| CRTV, REDEVANCE AUDIOVISUELLE; TAXE COMMUNALE, TAXE DEVELOPPEMENT LOCAL | Actual royalty/development-tax liability and band |
| VIREMENT SALAIRES, PAIE DU MOIS, MASSE SALARIALE | Net wages disbursement, not a second expense on settling a previously accrued payable |

Keep Salaire brut, Salaire net/Net à payer, Bulletin de paie, Précompte/Retenue à la source, Prime/Gratification, Indemnité and NIU (Numéro Identifiant Unique) as local terminology. DIPE means Document d’Information sur le Personnel Employé under 83, not the old expanded wording “Déclaration des Impôts et des Prélèvements sur les Salaires”. Cameroon is bilingual; actual statement language may be French or English. Descriptions are clues, not proof of compliance or a deterministic posting rule.

## Deadlines and filing

Obtain DGI NIU/tax registration and CNPS employer/worker registration. The CNPS decree in the sibling requires affiliation within 8 days of first hire and timely hire/cessation notices; the old “must already be registered before hiring” wording is replaced by the actual statutory deadline. Check documents/current registration rather than certify a computation as lawful merely by labelling it “subject to registration”. [Decree 2015/2517 arts 3 and 8](https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf).

81-83 require withholding on payment, payslip disclosure and the administration's DIPE bulletin for salary-IRPP remittance. Company annual DIPE accompanies 18 results return;74 bisrecipient statements and individual recap have different deadlines listed above. Annual recap shows prior-year categories, source withholdings/instalments and balance; pay a balance with the return. Overpaid amounts require validation/request for refund or credit. Professional business returns remain 74/91, not a universal employee 15 March deadline. Use actual current tax-account forms; no unverified portal steps or boxes are supplied.

CFC/FNE/CRTV statutory annex deadlines are shown separately. The present combined electronic-return calendar and reconciliation of any DGI harmonising instruction were not recovered; do not give the old blanket 15th for every levy as law. Plan and confirm the actual applicable return/payment process before filing. Keep 10-year evidence, matching payment references and the statutory yearly CFC/CRTV recap.

## Penalties and interest

Use the relevant tax and legal period; do not mix CNPS arrears with DGI/PAYE. L106 collection interest runs by its notice/declaration/due-date start and last-day-of-payment-month rules. The 50% assessment-interest cap inL95/L98 is not a universal cap forL106. L97 failure after formal notice brings default assessment plus 100%/150% repeat and separate office-specific fines; annual nonprofessional recap failure has its own 100,000 fine underL99(4). CFC/FNE/CRTV annex provisions require their own reading with current harmonised administration before quoting an actual enforcement balance. Obtain principal by month, notices, payments and official statement; refer disputes and arrears instead of certifying a bill from a bank debit.

## Cross-border points

Domicile, source and treaty relief need the actual 25-27/30 facts; diplomatic exemptions have reciprocity/status/foreign-tax conditions and are not an employer-name shortcut. Local nondiplomatic staff generally remain taxable under 25. Separate CNPS coverage/detachment from IRPP residence. The old shares 16.5%, other-activity 33% and tax-haven-dividend 33% snippets do not classify salary; route investment/business/IGS and nonresident payments to the passing income/cross-border/company skills with their own conditions. Do not apply a turnover minimum tax to employees.

## Two worked examples that recompute

### Ordinary salary and the corrected deduction order

JEAN M. is retained from the old bank-line case: `VIREMENT SALAIRE - JEAN M. - XAF 2xx,xxx`. Assume full-year monthly all-cash/basic/contributory salary 250,000, proven general CNPS coverage, no exemptions or extra benefits, no exceptional-income regime, and actual employee pension 10,500/month. Annual gross 3,000,000;30% gross expenses 900,000; pension 126,000; salary abatement 500,000; net 1,474,000. Principal 147,400+CAC14,740=162,140/year; indicative annual/12 is 13,511.6667. TDL annual 18,000 gives derived 1,500/month; CRTV at gross 250,000 is 3,250, not zero; CFC employee 2,500. Indicative net 218,738.3333 before actual filing/payroll rounding. The old payroll net 223,149 both used the wrong deduction order and omitted real local levies.

```oa-check
name: Full-year250000 salary, gross-based deduction and actual local bands
inputs:
  monthly: 250000
  pension_monthly: 10500
steps:
  - annual: monthly * 12
  - professional: min(annual * 0.30, 4800000)
  - pension: pension_monthly * 12
  - net_base: max(0, annual - professional - pension - 500000)
  - principal: net_base * 0.10
  - cac: principal * 0.10
  - annual_tax: principal + cac
  - monthly_estimate: annual_tax / 12
  - tdl_allocation: 18000 / 12
  - cfc: monthly * 0.01
  - indicative_net: monthly - pension_monthly - monthly_estimate - tdl_allocation - cfc - 3250
expected:
  professional: 900000
  net_base: 1474000
  annual_tax: 162140
  monthly_estimate: 13511.6666667
  indicative_net: 218738.3333333
```

### Above cap: full accident base and local levies

A. NGUEMA is retained from `PAIE DU MOIS - A. NGUEMA - VIREMENT`. Same assumptions at 800,000/month, actual Group B and general family regime; employer is fully liable for CFC/FNE. Annual gross 9,600,000; expenses 2,880,000; pension 378,000; salary abatement 500,000 gives net 5,842,000. Annual IRPP1,259,170, indicative 104,930.8333/month. Employee pension 31,500+CFC8,000+TDL2,500+CRTV9,750 produces indicative net 643,319.1667. Old 649,424 omitted the applicable CRTV and used wrong tax/base/TDL.

Employer pension 31,500+family 52,500+risk 20,000 (2.5% of full 800,000)+CFC12,000+FNE8,000=124,000 on-cost, total 924,000. Old 922,750 wrongly capped accident at 750,000, understating cost 1,250. That is a real base correction, not a new levy.

```oa-check
name: Above pension cap, uncapped GroupB and correct gross deduction
inputs:
  monthly: 800000
  cap: 750000
steps:
  - annual: monthly * 12
  - pension_monthly: min(monthly, cap) * 0.042
  - professional: min(annual * 0.30, 4800000)
  - net_base: annual - professional - pension_monthly * 12 - 500000
  - annual_tax: (850000 + (net_base - 5000000) * 0.35) * 1.10
  - monthly_estimate: annual_tax / 12
  - indicative_net: monthly - pension_monthly - monthly * 0.01 - monthly_estimate - 2500 - 9750
  - family: min(monthly, cap) * 0.07
  - risk: monthly * 0.025
  - employer_levies: monthly * 0.025
  - oncost: pension_monthly + family + risk + employer_levies
  - loaded: monthly + oncost
  - old_capped_risk: min(monthly, cap) * 0.025
  - understatement: risk - old_capped_risk
expected:
  net_base: 5842000
  annual_tax: 1259170
  monthly_estimate: 104930.8333333
  indicative_net: 643319.1666667
  risk: 20000
  oncost: 124000
  loaded: 924000
  understatement: 1250
```

### Retained high-pay, wage-floor and checkpoint cases

At monthly 1,500,000 under the same facts: annual 18,000,000; professional deduction capped 4,800,000; pension 378,000; salary abatement 500,000; net 12,322,000. Annual IRPP3,753,970; indicative 312,830.8333/month. Employee CFC15,000, TDL2,500, CRTV13,000 and pension 31,500 give indicative net 1,125,169.1667. This replaces old 11,835,000 net-base/3,566,475 tax and 1,140,774 net-pay figures. Actual monthly withholding/rounding still needs confirmation.

At all-cash/basic/contributory salary 60,000 in the other-sector minimum-wage category, assume full coverage and no levy exemption: salary IRPP withholding 0; pension 2,520 and CFC600 remain; CRTV750 is not removed by the IRPP floor. TDL has no listed band below 62,000; indicative net 56,130. This is a scoped example, not a universal net minimum wage or entitlement certification. The original 55,000 scenario is below that other-sector wage floor; don't certify compliance or treat a nilIRPP withholding as nilsocial liability. Confirm the actual worker category, hours and contribution floor.

At a confirmed pension base 750,000 employee/employer pension 31,500 each and general family 52,500 remain correct. At a base exactly 750,000, accidentA/B/C13,125/18,750/37,500 are derived amounts, not maximum accident contributions. At net taxable 1,000,000, CAC-inclusive IRPP110,000; no second CAC. Checkpoints 220,000/385,000/935,000 are in the table. An unknown risk class or benefits package does not authorise an exact cost; a full statement/assumptions block is mandatory.

## Ask the client first

1. Employee/employer identity, tax year, coverage/residence, NIU/CNPS numbers and actual work location?
2. Basic/cash salary, currency/frequency, hours, allowances, benefits and any exceptional/irregular payment?
3. Actual employee pension, contributory exclusions, CNPS family regime and assigned risk class?
4. CFC/FNE/CRTV employer/worker exemption facts, gross/basic tax bases and prior deductions?
5. Current payslips/DIPE, annual statements, prior-year recap, payment receipts and notices?
6. Confirmed current monthly withholding/rounding method and the actual electronic return/deadline calendar?

No gross salary/currency/frequency means stop exact computation; no FX assumption. A bank statement alone supports only provisional reconciliation. Unknown benefits require disclosure and an incomplete-base warning, not silent cash-only certification. Refuse to certify SMIG/working-time/overtime compliance without correct worker category and current legal/contractual facts. Refer nonresident/treaty/special pension/exceptional-income/arrears questions with their evidence. Never file/sign DIPE/tax returns or present an estimate as professional approval; qualified review is required. Never omit actual local bands, add CAC twice, cap accident, deduct all contributions as pension, or treat salary as turnover.

## Sources

| Official source | URL | Read on / actual scope |
|---|---|---|
| DGI CGI Edition 2026 and annexed laws | https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf | 2026-11-15. Read for 18/25-34/65 bis/69/71/74 bis/80-84; C83/C86-C88; LPF L5/L95-L106; Law 77/10 arts 1-16 with Law 90/050 arts 1-3 replacing provisions incl 3/6-10; Ordinance 89/004 arts 1-13 and full salary table; Decrees 2015/2517 arts 1-27,2016/072 arts 1-12 and full risk Annex. Read historical IRPP note 878-879, explicitly not a current CNPS-rate table. Not entire code or every implementing exemption decree. |
| Prime Minister, Decree 2023/00338 | https://www.spm.gov.cm/site/sites/default/files/dpm_2023-00338_s.pdf | 2026-11-15. Read all 4 bilingual pages and visually checked French page 1 for dates and monthly categories 45,000/60,000; State category updated by 2024 decree. |
| Prime Minister, Decree 2024/0168 | https://www.spm.gov.cm/site/sites/default/files/decree_no_2024_0168.pdf | 2026-11-15. Read and visually checked full 1 page: State LabourCode employees 43,969,23 February 2024, repugnant prior provisions repealed. |

Not yet confirmed: current monthly salary-IRPP table/rounding and the old annual-net round-down-to 1,000 instruction; partial-year/multiple-employer/entry-exit withholding and precise exceptional-income implementation; current combined electronic-return calendar reconciling CFC/FNE/CRTV annex 20-day provisions with any later harmonising instruction; TDL partial-year collection; working hours (old commonly cited 40/week), overtime multipliers and weekly rest; actual collective agreement rates; detailed CNPS excluded-cost lists/contribution floor and voluntary minimum; current portal screens; particular employer/worker exemption implementing conditions and foreign treaty/detachment. These are outside usable filing/compliance instructions. All annual/12 andTDLmonthly-equivalent outputs above are labelled estimates/derived, not a certified payslip rounding method.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
