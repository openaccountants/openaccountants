---
name: mozambique-social-contributions
description: "Mozambique INSS for 2026: separate employee/employer and self-employed contributions, actual bases, registration, remittance, interest, foreign coverage and preserved bank-statement cases."
version: 0.2
jurisdiction: MZ
tax_year: 2026
last_updated: 2026-11-17
depends_on:
  - social-contributions-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Mozambique social contributions

## Who this applies to

Ordinary INSS-covered workers and employers, plus separately classified self-employed workers (TCP). Mozambique has personal income tax as well as social security. IRPS is not INSS; payroll withholding is computed in [payroll](mozambique-payroll.md), annual non-employment tax in [income tax](mozambique-income-tax.md), and IVA in [VAT](mozambique-vat.md). This Guide does not establish that every contractor is an employee or that every foreign/public/domestic worker has the same coverage.

The current RSSO text used is the 2024 republication of Decreto 51/2017 by Decreto 56/2024. The administering site's label says article 100 in one place; the actual amending act names article 110. Do not mix that label or the old 2017 penalty cross-references with the enacted republication. No independent accountant attestation is claimed.

## Rates, bands and thresholds

| Item | Rule | Official source |
|---|---|---|
| Ordinary employee / employer | 3% employee,4% employer;7% remitted in total. Employer share is on top, not shifted onto wages. | INSS contributor guidance; Law 4/2007 art 20: https://www.inss.gov.mz/direitos-e-obrigacoes-do-contribuinte/ |
| TCP | 7%, entirely borne by the self-employed worker; classification and chosen-base rules apply. | INSS TCP guidance; Law 4/2007 art 23: https://www.inss.gov.mz/taxa-contributiva-tcp/ |
| TCP base floor | Chosen conventional remuneration cannot be below the respective sector minimum, not a universal no-floor rule. | RSSO 65-66: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| TCO base / ceiling | RSSO 11 listed remuneration; no general ceiling located in ordinary provisions read. Special conventional bases under 11(2) are not ruled out. | RSSO 11/14: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| Employer affiliation | Within 15 days from activity start or acquisition. Missing required registration documents must be regularised within the separate 30 day rule. | RSSO 7: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| Worker registration / changes | Electronic enrolment and validation documents within 30 days from vínculo under 9; ordinary identification/contract changes within 30 days under 10. | RSSO 9-10: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| Contribution start | TCO:first contractual day through end of paid activity; TCP:month after registration/enquadramento. | RSSO 14/64: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| Declaration and payment | From 20th of reference month to 10th next month; Saturday/Sunday/holiday/tolerancia carry under 12 and contributor guidance. | RSSO 12/14/67: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| Business/TCP suspension or cessation | Specific written notice by 10th next month; employer supplies competent-authority evidence. Failure can create recorded contribution debt. | RSSO 16/63: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| Arrears interest | 2% per month or fraction after the contribution deadline. Court appeal does not interrupt accrual. | RSSO 98: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| Interest relief | Proved force-majeure exemption request; non-attributable production/productivity reduction may support a request, reduction no greater than 50% of interest. | RSSO 98(2)-(5): https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| Pension-branch foreign refund | Definitive departure before pension entitlement; specified foreign beneficiary; no bilateral agreement with origin country; request within 1 year of last contribution. Not an automatic refund of employee 3%. | RSSO 123: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| TCP advance payment | May request up to 12 months in advance; contribution differences from minimum-wage changes paid the month after Gazette publication. | RSSO 67: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |

| Fine band | Offences in actual republication | Official source |
|---|---|---|
| 1-5 sector-minimum wages | RSSO 93(a,d,f,q): specified missing registration documents/data/communications | RSSO 93-94: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| 1-3 sector-minimum wages | RSSO 93(h,k,m): missing remuneration declaration, non-payment, specified employer false statement | RSSO 93-94: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| 1-2 sector-minimum wages | RSSO 93(c,e,g,i,j): listed late documents/declaration, worker omission/false remuneration | RSSO 93-94: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |
| Late payment 93(l) | Interest under 98; do not relabel it the preceding fixed-fine band | RSSO 93-94/98: https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf |

Apply the relevant fine once per affected employed person, using the branch minimum at the violation date. The omission of a clear 93(b) registration-failure mapping in the 94 bands read is not permission to silently assign the old blanket 1-5 band. Obtain the actual assessment/procedure. The old universal late-submission 1-3 headline does not distinguish absent from late declarations.

## The base

### TCO employee and employer contributions

RSSO 3 covers national/foreign employees, including part-time, probation and paid internships, specified paid directors/managers and other listed categories. Employers are responsible for their own and workers' contributions under Law 4/2007 art 20. Contributions and registration do not wait for a large headcount or a bank label.

RSSO 11 includes salary, seniority bonus, management gratuity, regular performance/productivity/attendance premiums, replacement remuneration, night-work remuneration and analogous regular bonuses, allowances and commissions. Law 4/2007 art 28 likewise addresses salary and regular/periodic additions. The original blanket exclusion of meal subsidies, one-off bonuses, profit-share/dividends, holiday pay and reimbursements was not established from the operative sources. Analyse each component's legal character and regularity, with actual pay records and current INSS confirmation where necessary. A true expense reimbursement is not proved merely by its narration; a distribution needs ownership and underlying records.

Original Note 246/INSS/GAB-DG/432/2024 was not recovered/read. The INSS FAQ says 13th salary is included in its payment month, but carries revoked 53/2007 and old Penal Code references elsewhere. Preserve that agency statement and its source-version limit; do not treat it or the old blanket exclusion as complete current component clearance. The income-tax treatment is independently governed: employee INSS is not deducted before the CIRPS 29/65-A gross-employment PAYE algorithm.

For a proven ordinary contributory base B: employee=B x 3%, employer=B x 4%, combined remittance=B x 7%. No general maximum was found in the ordinary TCO clauses read, but special conventional bases and separate TCP/voluntary regimes remain possible. Do not infer the absence of every floor or cap from an unsuccessful source search. Sector minimum-wage compliance is a separate labour check; report underpayment and actual arrears instead of automatically rewriting paid remuneration.

### TCP, voluntary maintenance and foreign coverage

TCP criteria in RSSO 58-59 distinguish an economic activity without collaborators and individual service contracts by control of working means/processes, hours, integration into a sole hierarchy and substitution. Do not presume employee status when the facts are missing. TCP declares activity within 30 days and supplies identification, activity licence/equivalent, NUIT and requested contact/account/family information under 61-62. Contributions begin the following month, on chosen remuneration no lower than the sector minimum under 64-66. A change of base is requested from INSS; upward age/income conditions and special suspension rules must be checked before a real election. Supported sickness exceeding 30 days has the 68 suspension rule; no general 'stop paying whenever work is quiet' election is provided.

Voluntary maintenance is a different route under RSSO 55-56, with an ordinary six-month average and minimum/INSS-approved alternative-base conditions, whole contribution borne by the beneficiary and request-based advance payment. Do not apply TCP's chosen-sector base or an employee/employer split to it without confirming the actual regime and eligibility. Full benefit/pension entitlement is not cleared here.

RSSO 4 excludes the registration obligation for a foreign worker who proves coverage by another country's social-security system, subject to applicable legislation. Proof needs Mozambique consular authentication or competent confirmation of issuing-country formalities. Law 4/2007 art 14 preserves bilateral-agreement qualifications. It is not limited by the old words 'comparable home-country scheme', and neither tax non-residence nor foreign nationality is sufficient proof. Do not omit contributions from an actual payroll without resolving coverage/documentation.

Foreign reimbursement under 123 is conditional on pension-branch status, definitive departure before pension entitlement and absence of the specified agreement, with a one-year request limit. Deduction for benefits already granted applies to restitution under 123(2). Do not promise all 7%, all 3% or a universal expatriate refund. Public/central-bank schemes, domestic-work Decreto 52/2026, detachment, Portugal/bilateral and system-articulation cases remain non-usable special-regime boundaries.

### Statements, postings and workpaper

Match narratives case-insensitively, longest relevant pattern first, then inspect direction, counterparty, period, receipt and account. INSS/I.N.S.S., SEGURANCA SOCIAL/SEGURANÇA SOCIAL, INST NACIONAL/INST NAC SEG SOCIAL, CONTRIBUICAO/CONTRIBUIÇÃO INSS and CONTRIBUICAO SOCIAL are possible INSS transactions. IRPS, AT MOCAMBIQUE, AUTORIDADE TRIBUTARIA and EDECLARACAO denote a different tax job; IRPC is company tax, IVA/VAT is VAT. SALARIO/SALÁRIO, ORDENADO, VENCIMENTO and PAGAMENTO SALARIAL usually identify wage payment/receipt, not contribution remittance.

BCI/Banco Comercial e de Investimentos, Millennium BIM, Standard Bank Mocambique and Absa are the original illustrative bank sources; their narrative patterns and monthly recurrence are clues, not guaranteed statement formats. A debit can settle multiple workers, arrears or fines; a credit can reverse an earlier payment or pay a benefit. Do not impose the old 'always debit/full 7%' rule on every transaction. Liability settlement is not a second VAT supply or revenue item; the underlying employer contribution remains an expense where properly recorded, not excluded from all accounts.

The workpaper retains Client/NUIT, INSS contributor/beneficiary numbers, year and preparation date, worker/coverage/residence evidence, sector/date, each actual pay component, assessed base and supporting exclusions, employee/employer/TCP rate and amount, payment window/carry, reference/receipt, arrears periods and adjustments. Route PAYE through the actual gross-monthly matrix and keep annual non-employment aggregation separate. The old fields labelled 'meal/one-off/reimbursement EXCLUDED' become component review fields, not prefilled exclusions. Do not deduct employee INSS from an assumed annual employment IRPS base.

With statements alone, classify possible liabilities provisionally and request contracts, pay slips, nominative declarations and official account statements. Divide 2,100 by 7% to infer 30,000 only if evidence first proves it is solely the combined ordinary contribution on that base; otherwise refuse the inferred salary. Separate 3% employee liability,4% employer expense, payment and original salary. Unknown residence, sector, worker status or base remains an explicit stop for an exact computation.

## Deadlines and filing

RSSO 7/9/10 registration and change deadlines,16/63 cessation and 12/14/67 monthly declarations/payment are separate obligations. A business suspension/cessation needs the specific next-month notice and supporting document; otherwise debt can continue. Use the actual INSS electronic declaration and payment guide/receipt, not a guessed tax portal.

Official contributor guidance corroborates next-working-day carry for both declaration and payment. TCP can request advance payment; the old FAQ's categorical 'no advance' must not override 67. Current screens and detailed partial-month/unpaid-leave processing remain unverified. Do not substitute a tax calendar's 15th or 20th for the INSS deadline. M/19, Lista Nominal, annual IRPS filing and payment periods are separately addressed/held in payroll and income tax.

## Penalties and interest

Use the mapped 93-94 bands and 98 interest, not MAIBOR or a generic 1-3 multiplier. For a real bill obtain principal by period, due dates/carries, periods/fractions, payment allocation, notices, offence, affected workers, sector/date minimum, relief application and decision. Court appeal does not itself suspend interest. Force-majeure or productivity relief is request-based and conditional, not an automatic reduction.

Decreto 20/2025 was a 12-month programme from 9 July 2025, for specified debt from June 2022 to the month before commencement. It excluded prior-relief defaulters, required application/terms and principal payment, and specified 98% interest reduction for full principal payment or 75% for qualifying instalments with six-month/agreement/default conditions. No extension was located. At the read date it is historical/individual-agreement context, not an automatic current election; retrieve the actual agreement before applying any residual effect. It does not erase criminal liability or procedural costs merely because principal was paid.

Tax fines and tax juros de mora are different. The old approximately USD100-33,000 tax-penalty estimate has no verified current MZN schedule and is not usable. Refuse a definitive bill without the current primary tax law and official account. No fresh interest-rate guess or FX conversion is supplied.

## Cross-border points

Tax residence is governed by 2026 CIRPS 21, independently from INSS coverage and authentication. Source, treaty and category decide the appropriate income-tax route. Ordinary foreign-employee coverage, bilateral exceptions, public schemes and pension-branch reimbursement have distinct conditions. The old >180-day shortcut and a 'non-resident means no INSS' assumption are not usable. No treaty result or foreign refund is certified here.

## Two worked examples that recompute

### Original ordinary remittance, all-cash base confirmed

Original input: `10.02.2025 ; INSS CONTRIB ; DEBITO ; REF JANEIRO 2025 ; -2,100.00 ; MZN`. Assuming the receipt proves one worker's ordinary base 30,000: employee 900, employer 1,200, combined 2,100. The amount/date alone do not prove its period, actual base or timely filing.

```oa-check
name: Original ordinary 30000 base and 2100 remittance
inputs:
  base: 30000
steps:
  employee: base * 0.03
  employer: base * 0.04
  combined: employee + employer
expected:
  employee: 900
  employer: 1200
  combined: 2100
```

### Original meal-component case: two explicitly conditional outcomes

Original input: `08.03.2025 ; SEGURANCA SOCIAL ; DEBITO ; FEV 2025 ; -1,400.00 ; MZN`, gross 25,000 including meal 5,000. A legally established exclusion would leave 20,000, employee 600/employer 800/total 1,400. If the full 25,000 is contributory, employee 750/employer 1,000/total 1,750. The bank amount does not prove exclusion; current component classification remains held. These two arithmetic comparisons are not a unilateral exclusion election.

```oa-check
name: Original 25000 and 5000 case with base unresolved
inputs:
  gross: 25000
  disputed_component: 5000
steps:
  conditional_excluded_base: gross - disputed_component
  conditional_excluded_total: conditional_excluded_base * 0.07
  conditional_included_total: gross * 0.07
  difference: conditional_included_total - conditional_excluded_total
expected:
  conditional_excluded_base: 20000
  conditional_excluded_total: 1400
  conditional_included_total: 1750
  difference: 350
```

### Remaining original cases and regressions retained

- `18.02.2025 ; AUTORIDADE TRIBUTARIA ; DEBITO ; IRPS JANEIRO ; -3,200.00 ; MZN`: investigate tax remittance, not INSS. The description does not prove a correct PAYE amount, timely filing or gross salary; route tax reconciliation separately.
- `25.02.2025 ; SALARIO JOAO MUCAVELE ; DEBITO ; VENCIMENTO FEV ; -28,100.00 ; MZN`: original name and facts retained. Possible net wage, not an INSS remittance; pay slips must establish deductions, not a narration-only assumption that 3% and PAYE were already correctly withheld.
- Original resident employee with 'annual taxable income 300,000': the standalone art 54 arithmetic 300,000 x 20% -10,500 =49,500 is retained **only as an annual-table regression**, not annual employment assessment. Actual employment uses payroll's monthly matrix. The additional original assumption of 300,000/12 =25,000 fully contributory monthly pay yields employee 750/month/9,000 year and employer 1,000/month/12,000 year, independently from IRPS. Employee INSS does not reduce the monthly PAYE base.
- Original non-resident contractor Mozambique-source fee 100,000: if the actual art 57(2) ordinary-services final 20% route is established and no treaty/special rule applies,20,000 withholding. Digital/e-money/artists cases have different conditions; a consultancy label alone does not establish the route.
- Original construction salary 8,000/month is below the agency 2025 construction minimum 8,400 and current 2026 amount 8,652. Preserve the historical comparison and flag underpayment; do not automatically amend the pay record or declare a lawful contribution base without the assessment facts.
- Original quick bases 10,000/20,000/30,000/50,000 produce employee 300/600/900/1,500; employer 400/800/1,200/2,000; total 700/1,400/2,100/3,500. These are derived ordinary equal-base arithmetic, not sector/floor compliance.
- Original annual-table regressions 42,000/168,000/300,000/504,000/2,000,000 give 4,200/23,100/49,500/**90,300**/498,460 before any separately applicable annual minimum or collection deduction. Old 504,000 result 88,500 used the wrong 37,500 constant; correct annual 25% constant 35,700. They are not employment PAYE or a completed annual filing calculation.
- Original foreign worker with unproved coverage: no final exclusion or exempt-pay calculation; obtain RSSO 4 evidence and actual coverage determination. Original unknown-sector/base and exact-penalty cases remain refusals, with the now-sourced 98 rate distinguished from a certified account bill.

## Ask the client first

Obtain actual worker regime/contract, itemised gross and documentary base, sector/date, residence/source facts for the separate tax job, registration, foreign-scheme proof/authentication, declarations/payment receipts, payroll records, arrears statements/notices and any relief agreement. Do not default every unknown worker to employment, every meal to exclusion, every remittance to full 7%, every foreign worker to exemption, or every unregistered case to the same fine. Outputs remain provisional and require qualified review before filing.

### Original adjacent-tax topics kept as explicit boundaries

Municipal personal tax remains a separate municipality/year determination; the old Maputo 510/year figure is a 2024 historical assertion, not a current payroll deduction. Sector wage values and all eighteen historical/current rows remain in payroll, with actual bank/case facts preserved here.

The original corporate/other-tax context listed IRPC32%, general no-PE withholding 20%/some 10%, confidential expenses 35%, SISA2%/10%, inheritance/gifts 2%-10%, stamp 0.03%-50% or 0.50-5,000 fixed, and 'no net wealth tax'. Those are retained as **unverified adjacent topics, not operative 2026 rules**; obtain their current owning primary instruments before use. This INSS rewrite does not clear those taxes or confuse IRPC with individual IRPS54-A. Historical Form 6, commencement/NUIT and eDeclaracao/Portal do Contribuinte references also require current official form/portal confirmation.

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions or outcomes arising from its use. A qualified professional must review and sign off every output before filing or relying on it.

## Sources

| Official source | URL | Read on / actual scope |
|---|---|---|
| RSSO 2024 republication | https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf | 2026-11-15: contribution/coverage/registration/TCP/interest/refund provisions and relevant neighbours; operative text reused and reviewed 2026-11-17. Not full benefit clearance. |
| Law 4/2007 | https://www.inss.gov.mz/wp-content/uploads/2024/04/Lei-4-2007-de-7-de-Fevereiro-Lei-da-Proteccao-Social.pdf | 2026-11-15:14-23,28-30 coverage, responsibilities and contribution rules. |
| INSS contributor guidance | https://www.inss.gov.mz/direitos-e-obrigacoes-do-contribuinte/ | 2026-11-15; reopened/read 2026-11-17:7% split and full operative registration, monthly windows and carry. |
| INSS TCP guidance | https://www.inss.gov.mz/taxa-contributiva-tcp/ | 2026-11-15; reopened/read 2026-11-17:7% wholly borne by TCP. |
| TCP DM105/2015 | https://www.inss.gov.mz/wp-content/uploads/2024/04/Diploma-Ministerial-no-105-2015-de-27-de-Novembro-Determina-os-Requisitos-de-Inscricao-dos-TCP.pdf | 2026-11-15:actual instrument registration requirements and explicit 7%cross-reference; original 14/2015 scan not claimed visually cleared. |
| INSS FAQ | https://www.inss.gov.mz/duvidas/ | 2026-11-15:operative guidance read with obsolete references recorded, including 13 thsalary statement; not a complete current exclusion schedule. |
| Debt relief 20/2025 | https://www.inss.gov.mz/wp-content/uploads/2025/07/BR_129_I_SERIE_2025.pdf | 2026-11-15:both pages, scope, exclusions, reductions, application, duration and default conditions. |
| Wage tables | https://www.inss.gov.mz/salarios-minimos-em-vigor/ | 2026-11-15:all 18 current 2026 and 18 historical 2025 amounts; full wage diplomas not read. |
| CIRPS 2017 | https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf | 2026-11-15; focused text/image recheck 2026-11-17:26/29/54/56/57/59-61/65-A for corrected routed cases. |
| Law 11/2025 | https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf | 2026-11-15 retained primary reading;2026-11-17 focused gross-matrix, residence, commencement and non-aggregation review. |

Not yet confirmed: original Note 246/2024 and detailed component exclusions, statutory rounding/partial-month/unpaid-leave methods, special conventional bases, full wage-diploma clauses, domestic Decreto 52/2026, precise 93(b) fine mapping/procedure, current portals, individual public/bilateral/detachment/benefit/refund eligibility, current tax penalty and municipal/adjacent-tax figures. The full 2018 IRPS Gazette is a primary document on a private mirror, not cleared as an official-host operational calendar. No failed page is marked read and no historical relief is represented as an automatic current election.
