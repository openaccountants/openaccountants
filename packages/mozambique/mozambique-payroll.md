---
name: mozambique-payroll
description: "Mozambique payroll for 2026: the complete gross-monthly IRPS/dependent matrix, employee and employer INSS, sector wages, historical pay cases and explicit filing and component-classification holds."
version: 0.2
jurisdiction: MZ
tax_year: 2026
last_updated: 2026-11-17
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Mozambique payroll

## Who this applies to

Employers paying Mozambique employment income and workers whose actual residence, employment status and social-security coverage have been established. IRPS is employee income tax withheld by the employer; INSS separately comprises employee and employer contributions. MZN/MT means Metical. Record the actual pay period; do not default a current job to the old 2025 tables.

This Guide covers gross-to-net computation and reconciliation. Annual non-employment aggregation, the minimum and personal deductions belong in [income tax](mozambique-income-tax.md); full INSS scope, TCP and arrears rules belong in [social contributions](mozambique-social-contributions.md). A bank label does not establish any of those legal facts. No live portal, filing or accountant approval is claimed.

## Rates, bands and thresholds

### Resident monthly employment withholding

The following are amounts of tax at the **lower limit**, not amounts to subtract from gross pay. Column dash means no withholding and no coefficient; a numeric zero means apply only the coefficient. Choose the actual dependent column, with the final column covering four or more dependents. Do not substitute the annual progressive table or subtract employee INSS before this gross-monthly algorithm.

| Gross monthly MZN, inclusive displayed limits | Lower-limit tax: 0 dependents | 1 | 2 | 3 | 4+ | Coefficient on gross above lower limit | Official source |
|---|---:|---:|---:|---:|---:|---:|---|
| Up to 20,249.99 | - | - | - | - | - | - | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| 20,250.00 to 20,749.99 | 0.00 | - | - | - | - | 10% | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| 20,750.00 to 20,999.99 | 50.00 | 0.00 | - | - | - | 10% | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| 21,000.00 to 21,249.99 | 75.00 | 25.00 | 0.00 | - | - | 10% | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| 21,250.00 to 21,749.99 | 100.00 | 50.00 | 25.00 | 0.00 | - | 10% | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| 21,750.00 to 22,249.99 | 150.00 | 100.00 | 75.00 | 50.00 | 0.00 | 10% | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| 22,250.00 to 32,749.99 | 200.00 | 150.00 | 125.00 | 100.00 | 50.00 | 15% | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| 32,750.00 to 60,749.99 | 1,775.00 | 1,725.00 | 1,700.00 | 1,675.00 | 1,625.00 | 20% | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| 60,750.00 to 144,749.99 | 7,375.00 | 7,325.00 | 7,300.00 | 7,275.00 | 7,225.00 | 25% | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| 144,750.00 and above | 28,375.00 | 28,325.00 | 28,300.00 | 28,275.00 | 28,225.00 | 32% | Law 11/2025, CIRPS 65-A(1)-(3), printed 2180(17): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |

### Other payroll amounts

| Item | Rule / MZN | Official source |
|---|---|---|
| Employee INSS / employer INSS | 3% / 4%, total 7%, on the separately established contributory base; employer bears its own share | INSS contribution guidance: https://www.inss.gov.mz/direitos-e-obrigacoes-do-contribuinte/; Law 4/2007 art.20: https://www.inss.gov.mz/wp-content/uploads/2024/04/Lei-4-2007-de-7-de-Fevereiro-Lei-da-Proteccao-Social.pdf |
| Non-resident employment | 20% final withholding on the qualifying Mozambique-source employment income; actual residence/source/treaty status first, not nationality or absence alone | CIRPS 57(1),(2)(b),(4): https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf; 2026 residence amendment: https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| Separate holiday/equivalent and additional salary payments | Holiday/equivalent, 13th and 14th payments separately withheld, not added to ordinary pay in the payment month | CIRPS 65-A(5)-(6): https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| Reform commencement | 1 January 2026; publication on 29 December 2025 is not commencement | Law 11/2025 art.6: https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |

### Sector minimum wages and historical inputs

These are the **INSS agency's published monthly tables**, current from 1 April 2026 and historical from 1 July 2025. Full operative diploma clauses, exclusions and all wage-enforcement details were not cleared. Determine the actual sector and date; do not inflate an actual pay record to a legal minimum and call the debt corrected. Kapenta, not agriculture, has the lowest listed amount. The old rounded microfinance 16,764 figure is not the precise historical amount.

| Sector | 2025 from 1 July, MZN | 2026 from 1 April, MZN | Official source |
|---|---:|---:|---|
| Agriculture, livestock, hunting, forestry | 6,688.00 | 7,072.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Industrial/semi-industrial fishing | 6,726.88 | 7,063.22 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Kapenta fishing | 4,991.09 | 4,991.09 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Mining: large enterprises | 15,176.66 | 16,239.06 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Quarries/sand: medium enterprises | 8,008.00 | 8,488.48 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Salt: micro/small enterprises | 6,538.44 | 6,824.17 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Manufacturing excluding bakery/cashew | 10,147.50 | 10,622.50 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Bakery | 7,200.00 | 7,500.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Cashew | 6,653.21 | 7,000.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Electricity/gas/water: large | 12,275.00 | 12,775.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Electricity/gas/water: SME | 9,960.62 | 10,366.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Construction | 8,400.00 | 8,652.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Nonfinancial services | 10,310.00 | 10,845.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Hotels/tourism | 9,700.00 | 10,600.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Private security | 8,465.00 | 8,690.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Fuel retail | 9,739.00 | 10,079.00 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Banks/insurance | 19,043.61 | 20,361.43 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |
| Microfinance/microinsurance | 16,764.47 | 17,924.17 | INSS sector tables: https://www.inss.gov.mz/salarios-minimos-em-vigor/ |

## The base

### Gross-monthly algorithm and tax status

For an eligible ordinary resident employment payment, locate gross monthly taxable employment remuneration G in the table. If its dependent cell is a dash, tax is zero and no coefficient applies. Otherwise PAYE = that cell's lower-limit tax + coefficient x (G minus the interval lower limit). Thus the top zero-dependent 28,375 is **added**, not subtracted. The 20,249.99 ceiling of the all-dash row is exact; at 20,250 the zero-dependent formula begins at numeric zero. A dash in another dependent column can continue above that amount. Do not replace the full matrix with an approximate universal threshold.

CIRPS 65-A(3) includes fixed remuneration and other employment amounts, including relevant same-period receipts for earlier periods and third-party work gratuities in its terms. Article 65-A(1)'s specified exclusions and irregularity conditions must be checked against the income component, not a bank label. Article 29 makes no employment-income deduction; article 65-A(6) makes this employment withholding definitive. The 2026 repeal of the filing waiver does not itself turn employment into annual aggregated income or permit personal/INSS deductions in this monthly calculation.

Current CIRPS 21 tests principal residence, professional activity unless proved secondary, centre of economic interests and specified crew. Household and nationals-on-foreign-assignment provisions also apply. Days alone do not decide residence. Obtain treaty/source evidence before applying a special or non-resident route. The service-provider 20% advance withholding, artists/athletes 10% subject to its employment exception, and new digital/e-money 10% rules are distinct income-tax routes, not alternative payroll cells; use the owning income-tax Guide and actual payer/payee facts.

### Keep INSS separate

Start from itemised pay and the actual RSSO 11 contributory base: salary, seniority, management gratuity, regular performance/productivity/attendance premiums, substitution pay, night work and analogous regular allowances/commissions. Do not apply a blanket meal, holiday, profit-sharing, dividend, reimbursement or one-off exclusion from the old prose. The original Note 246/2024 was not recovered. The INSS FAQ includes a 13th-salary rule but has stale legislative references elsewhere; actual current component classification remains necessary. Genuine business distributions and documented reimbursements need their actual legal character established.

Ordinary TCO provisions read contain no general maximum, but this is not proof that no special conventional base exists. TCP has a sector-minimum floor and a distinct insured-funded 7% route; voluntary maintenance is another regime. Never default an unidentified service provider to an employee. Foreign-scheme coverage requires the evidence/authentication in RSSO 4 and any applicable agreement; tax non-residence does not itself remove INSS. The foreign pension-branch reimbursement in RSSO 123 has definitive-departure, no-bilateral-agreement and one-year request conditions, not an automatic refund of the employee's whole 3%.

Net cash pay = actual cash pay minus employee INSS, PAYE and other separately evidenced deductions. Employer payroll cost = gross pay plus employer INSS and any other independently applicable employer costs. Do not subtract the employer 4% from employee wages. Only use the same numerical base in both taxes when the facts establish that equality.

### Bank evidence, workpaper and fallback

Use case-insensitive Portuguese/English narratives as clues, longest relevant description first; direction, counterparty, receipt and payroll determine classification. BCI/Banco Comercial e de Investimentos (PDF/CSV; Data, Descricao, Debito, Credito, Saldo); Millennium BIM (TRF, DD, PAGAMENTO, COMPRA POS); Standard Bank Mocambique and Absa (TRANSFER, DEBIT ORDER, FEE); Banco Unico/Nedbank (TRANSFERENCIA, ENCARGOS) are historical statement examples, not bank-format guarantees.

| Narrative | Investigate and reconcile |
|---|---|
| SALARIO, ORDENADO, VENCIMENTO, PAGAMENTO SALARIO, CREDITO SALARIO, TRANSF with employer | Incoming employee net pay or outgoing net wages, not proved gross pay |
| FOLHA SALARIAL, PROCESSAMENTO, PAGAMENTO SALARIOS | Payroll register/run or net-wage disbursement |
| SUBSIDIO REFEICAO, SUBS. ALIMENTACAO | Meal component; no automatic INSS exclusion |
| SUBSIDIO FERIAS, SUBSIDIO NATAL, 13.* MES | Holiday/Christmas/additional payment; check separate IRPS withholding and actual INSS classification |
| REEMBOLSO INSS, DEVOLUCAO INSS | Refund/adjustment; determine period and original liability, not new salary |
| AT, IRPS, RETENCAO IRPS, MODELO 19, M/19, EDECLARACAO | Income-tax filing/payment clue; settlement is not a second expense or VAT supply |
| INSS, SEGURANCA SOCIAL, CONTRIBUICAO INSS | Reconcile employee liability plus employer expense and settlement; not automatically one worker's amount |
| IRPC, IMPOSTO RENDIMENTO PESSOAS COLECTIVAS | Corporate-tax job, not employment withholding |

The workpaper retains Client/NUIT, employee name, preparation/pay dates, worker regime, residence evidence, dependent proof, sector/date, each gross component, separate taxable/contributory bases, cell/lower limit/coefficient, PAYE, employee 3%, employer 4%, net cash and employer cost, filings/receipts, adjustments, foreign coverage and reviewer flags. Spreadsheet columns A-M from the old template are retained as these fields; replace its annualise-minus-INSS/divide-by-12 columns with the actual monthly cell algorithm. A currency amount with no supported Metical conversion means no precise payroll.

With only a statement, request the last three payroll registers, contracts and INSS/AT receipts. Infer an aggregate INSS base only after proving the remittance is solely the full applicable 7%, for a specified period with no arrears/refunds/fines. Otherwise do not divide a bank debit by a rate and call it a worker's gross salary. An unproved dependent count may be shown as a labelled zero-dependent comparison, never silently treated as the confirmed filing column. Do not invent residence, sector, historical year or exemptions.

## Deadlines and filing

INSS declaration and payment normally run from the reference month's 20th to the next month's 10th; the next-working-day carry applies under RSSO 12 and official contributor guidance. Employer affiliation, worker validation and cessation dates differ; see social contributions.

CIRPS 65/65-A impose employer withholding. The old M/19/Modelo 19 label, 20th-next-month tax remittance, 30 April Lista Nominal, employment-only 31 March, general 30 April and May/June final-payment claims are retained as calendar topics requiring the applicable current official instrument and obligation mapping. Do not use one as a universal 2026 deadline. The retained complete 2018 Gazette is a private-host primary mirror; the official OCAM copy is incomplete. No current filing-screen or calendar clearance is claimed from it. Current employee filing after the waiver repeal and definitive withholding must be reconciled separately.

The old eDeclaracao URL, INSS SISSMO/electronic platform, Portal do Contribuinte and e-fatura references identify historical systems. Verify the current official entry point, form/version and actual receipt before filing; this Guide does not assert that a historic URL is a tested live portal or that e-fatura is a VAT-return portal.

## Penalties and interest

RSSO 98 charges INSS interest of 2% for each month or fraction in arrears, not MAIBOR plus 2%. RSSO 93-94 use offence-specific sector-minimum multipliers and affected-person counts, not a universal late-submission fine. Quantify only from actual periods, due dates, notices, payments, offences and official account records; see social contributions.

Tax arrears interest, compensatory interest and refunds to the taxpayer are different concepts. The visible 2018 regulation's MAIBOR 12-month plus two-point provisions concern compensatory/indemnity interest; they do not prove a universal INSS or late-tax-payment rate. Current tax juros-de-mora rate, M/19 fixed fines and complete RGIT schedule remain held. Refuse a certified arrears bill from a bank narration alone.

## Cross-border points

Confirm IRPS residence under the 2026 statute, the source/category of the income, actual payer and treaty. Do not equate days, nationality, foreign bank payment, resident absence or a consultancy label with the 20% route. Foreign INSS exemption and refund have separate documentary conditions. Public schemes, domestic-work changes and specific bilateral/detachment cases require their own operative instruments; no blanket exemption or pension entitlement follows here.

## Two worked examples that recompute

### Ordinary resident mid-earner: original salary, corrected mechanism

Original facts: gross 30,000/month, resident, zero dependents. Assume ordinary covered employment, all-cash pay and a separately established INSS base of 30,000. PAYE = 200 + (30,000 - 22,250) x 15% = 1,362.50. Employee INSS 900; employer 1,200; net 27,737.50; employer cost 31,200. The old annual 349,200 taxable / 59,340 tax / 4,945 monthly / 24,155 net route is rejected, not a competing estimate.

```oa-check
name: Original 30000 salary using actual gross-monthly matrix
inputs:
  gross: 30000
  lower: 22250
  lower_tax: 200
  coefficient: 0.15
steps:
  paye: lower_tax + (gross - lower) * coefficient
  employee_inss: gross * 0.03
  employer_inss: gross * 0.04
  net: gross - paye - employee_inss
  employer_cost: gross + employer_inss
expected:
  paye: 1362.5
  employee_inss: 900
  employer_inss: 1200
  net: 27737.5
  employer_cost: 31200
```

### Original top salary: lower-limit amount is added

Gross 150,000/month, ordinary resident, zero dependents, separately confirmed equal INSS base. PAYE = 28,375 + (150,000 - 144,750) x 32% = 30,055; employee INSS 4,500; net 115,445; employer cost 156,000. The former 34,765 monthly tax / 110,735 net from annual taxable 1,746,000 and annual tax 417,180 is not the statutory monthly method.

```oa-check
name: Original 150000 salary using top monthly interval
inputs:
  gross: 150000
  lower: 144750
  lower_tax: 28375
  coefficient: 0.32
steps:
  paye: lower_tax + (gross - lower) * coefficient
  employee_inss: gross * 0.03
  employer_inss: gross * 0.04
  net: gross - paye - employee_inss
  employer_cost: gross + employer_inss
expected:
  paye: 30055
  employee_inss: 4500
  employer_inss: 6000
  net: 115445
  employer_cost: 156000
```

### Every other original payroll case retained

- Agriculture salary 6,688, resident, zero dependents: zero PAYE; INSS employee 200.64, employer 267.52; net 6,487.36; cost 6,955.52. The original bank description is losslessly represented as `PAGAMENTO SALARIO \u2014 JUNHO` (the escape denotes its original punctuation). The agency's 6,688 minimum is from 1 July 2025, so that JUNHO description does not prove historical minimum-wage compliance. In 2026 the published agriculture amount is 7,072.
- Financial salary 19,043.61: zero PAYE; employee INSS 571.31 and net 18,472.30, using cents rounding only as an example convention. Its 2025 date/sector assumption is retained. The old annual 221,667.60 / 33,833.52 / 2,819.46 reconciliation is rejected because employment does not use that annualised-minus-INSS path. Current 2026 banks/insurance minimum 20,361.43 is a different amount and is above the all-dash row.
- Original gross 60,000, ordinary resident and zero dependents: PAYE 1,775 + (60,000 - 32,750) x 20% = 7,225; employee INSS 1,800; net 50,975; employer 2,400; cost 62,400. The old annual 698,400 / 137,100 / 11,425 monthly / 46,775 net outputs are superseded.
- Original non-resident Mozambique-source employment 60,000: if the statutory 20% route applies, withholding 12,000 and the remainder after IRPS alone 48,000. If ordinary INSS also applies on 60,000, subtract employee 1,800 for net 46,200; employer 2,400 is additional cost. Never call 48,000 final net without resolving INSS.
- Employer-cost case 30,000 + 1,200 = 31,200 remains correct under the stated equal-base assumption; 3% + 4% = 7% is arithmetic, not proof of every regime's applicability. Annual table endpoints 42,000 and 168,000 produce 4,200 and 23,100 as statutory table arithmetic in income tax; they are not PAYE tests.
- Salary only in USD with no supported MZN conversion remains a refusal. Unknown gross, residence, pay period, dependent column or component base means no exact result. Self-employment, digital/e-money receipts and artists are routed to income tax; requests to omit statutory tax/INSS or certify an exact liability are refused.

## Ask the client first

Obtain gross and itemised cash/in-kind pay, pay dates/frequency and currency evidence; actual residence/source/treaty facts; dependent documentation; worker status, sector and INSS base; foreign scheme/authentication or exemption decision; contracts, registration, last payrolls, returns and payment receipts. Resolve holiday/additional payments, refunds and arrears separately. Missing data may support a provisional classification workpaper, not a silently selected filing result. Never use the old annual fallback, automatic meal exclusion, unknown-worker employee default, universal cap/floor denial, blanket 20% non-resident rule, MAIBOR-as-INSS rule or unverified filing calendar.

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions or outcomes arising from its use. A qualified professional must review and sign off every output before filing or relying on it.

## Sources

| Official source | URL | Read on / actual scope |
|---|---|---|
| AT actual Gazette, Law 11/2025 | https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf | 2026-11-15, retained primary read; 2026-11-17 matrix image and operative clauses rechecked. CIRPS 21/22/26/57/65/65-A/72, commencement/repeals; not a later consolidated regulation. |
| CIRPS 2017 enacted Gazette copy held by OCAM | https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf | 2026-11-15 retained source reading; 2026-11-17 focused visual/text recheck. Articles 26/29/31/54/56/57/59-61/65-A; no reliance on old superseded residence test. |
| INSS RSSO republication 2024 | https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf | 2026-11-15 full relevant contribution/coverage chapters read; reused for unchanged provisions, not the entire benefit system. |
| INSS contributor guidance | https://www.inss.gov.mz/direitos-e-obrigacoes-do-contribuinte/ | 2026-11-15; reopened/read 2026-11-17 for full operative registration,7%/4%/3%, declaration/payment and carry guidance. |
| INSS sector tables | https://www.inss.gov.mz/salarios-minimos-em-vigor/ | 2026-11-15. All 18 current 2026 and 18 historical 2025 amounts read; later open timed out, not relabelled a new read. |
| Law 4/2007 | https://www.inss.gov.mz/wp-content/uploads/2024/04/Lei-4-2007-de-7-de-Fevereiro-Lei-da-Proteccao-Social.pdf | 2026-11-15. Relevant coverage, employer/worker responsibility and contribution provisions read. |

Not yet confirmed: current 2026 tax filing calendar, M/19 version/boxes, Lista Nominal deadline and actual portals; complete current IRPS regulation and annual employee filing implementation; precise tax fines/default interest; original INSS Note 246/2024 and disputed component exclusions; legal rounding, special conventional bases, full wage-diploma clauses, domestic-work Decreto 52/2026 and individual public/bilateral/detachment/refund determinations. No failed page, partial official copy or private mirror is described as a complete official-host consolidation.
