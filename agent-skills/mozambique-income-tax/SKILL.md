---
name: mozambique-income-tax
description: "Mozambique individual IRPS for 2026: annual scale and minimum, residence, income classification, personal/dependent and foreign-credit conditions, separate employment PAYE and ISPC, with current-form and filing holds."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mozambique-income-tax"
  jurisdiction: "MZ"
  tax_year: "2026"
  last_updated: "2026-11-17"
---

# Mozambique individual income tax

## Who this applies to

Individuals with Mozambique employment, business/professional, capital, rental or other income. Establish actual residence, income category, source, year and applicable regime before calculating anything. Use MZN/Metical and the actual calendar year, not an assumed 2025 default. Corporate IRPC is a separate job; this Guide does not calculate company tax.

Employment PAYE is separately definitive under CIRPS 65-A(6) and excluded from annual aggregation by 26(3)(a), with no employment-income deductions under 29. Use [payroll](mozambique-payroll.md)'s actual gross-monthly dependent matrix. INSS employee/employer contributions and TCP are separately addressed in [social contributions](mozambique-social-contributions.md); VAT belongs in [VAT](mozambique-vat.md).

This Guide preserves the annual statutory scale and conditions, but does **not** clear a complete 2026 annual return or live Modelo 10/M10V workflow: the statutory minimum and the currently downloaded form's visible/hidden fields disagree. Do not solve that by discarding the statute or silently relabelling a gross/net-income input as post-minimum collectable income. No accountant approval is claimed.

## Rates, bands and thresholds

### Annual aggregate scale, not the salary-withholding table

The intervals below reproduce the statute's displayed whole-Metical limits. The subtraction column is the practical tax constant; it is not a personal deduction. Fractional-boundary/filing implementation is not inferred from the continuity checks. Confirm that the input is the properly established annual **rendimento colectavel** for this route, separately from employment, final-rate and autonomous income. [CIRPS 54(3)](https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf) qualifies this scale where aggregation contains only second-category income from agriculture or livestock: collection cannot exceed the result of the reduced 10% rate referred to in CIRPC 61(2), **during that reduced rate's validity**. Its actual 2026 validity and applicability have not been established. Do not apply or rule out that ceiling, or give an actual annual tax result for that route, until its operative validity and conditions are established; this is not a claim that 10% is currently available.

| Annual collectable income MZN, as printed | Marginal rate | Parcela a abater MZN | Official source |
|---|---:|---:|---|
| Up to 42,000 | 10% | 0 | CIRPS 54, printed 2602(137): https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| 42,001 to 168,000 | 15% | 2,100 | CIRPS 54, printed 2602(137): https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| 168,001 to 504,000 | 20% | 10,500 | CIRPS 54, printed 2602(137): https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| 504,001 to 1,512,000 | 25% | 35,700 | CIRPS 54, printed 2602(137): https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| Above 1,512,000 | 32% | 141,540 | CIRPS 54, printed 2602(137): https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |

| Item | Rule / amount MZN | Official source |
|---|---|---|
| Annual minimum | Article 56:annual collectable income at/below 225,000 is not taxed; excess subject to tax; family provision applies per income holder up to that holder's income. Current form/implementation reconciliation held. | CIRPS 56: https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| Personal collection deduction |1,800 per resident taxable person, up to tax due; not a monthly PAYE deduction | CIRPS 59-60: https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| Dependents |1:600;2:900;3:1,200;4+:1,800 annually, provided the dependents are not themselves taxable persons; limited to the collection and subject to article 60 conditions | CIRPS 60: https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| Foreign-tax credit | Lesser of qualifying foreign income tax and the proportional Mozambique collection before deduction; treaty limit and source/category conditions apply | CIRPS 26(6),59,61: https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| Ordinary non-resident services/employment final-rate routes |20% on gross for the income specifically listed in 57(2), including the applicable employment/services clauses; not every non-resident receipt | CIRPS 57(1),(2),(4): https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| Artists/athletes |10% in 57(3)(d), subject to its exception for regular employed remuneration | CIRPS 57(3)-(4): https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| Capital/final-rate distinctions | Article 57 separately lists 20% categories and 10% categories such as term-deposit interest; do not aggregate every interest/dividend receipt into the annual scale | CIRPS 26(3),57: https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf |
| New e-money/digital final-rate clauses |10% for actual 57(3)(e)-(g) cases; payer/payee/category/source and regulated collection matter | Law 11/2025,57/65(6): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| New autonomous gains | Separate 54-A scale 10%/15%/20%/25%/32%, with its own treatment; do not import 54's subtraction constants, annual minimum or personal deductions without authority | Law 11/2025,54-A: https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| Reform commencement |1 January 2026; publication 29 December 2025 is different | Law 11/2025 art 6: https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |

### Separate ISPC regime: do not call it abolished

Law 11/2025 revokes CIRPS's former simplified-bookkeeping/taxable-income paths and requires second-category organised accounting. **Law 9/2025 separately retains and changes ISPC**, including optional qualifying taxation and its own activity/exclusion/accounting conditions. Do not infer an individual's valid ISPC election or its interaction with the CIRPS accounting duty from turnover alone. Confirm the actual regime and registration with the authority before using an ISPC amount.

| ISPC provision, not ordinary IRPS/IVA | Enacted rule, subject to actual eligibility/classification | Official source |
|---|---|---|
| Scope/threshold | Annual turnover up to 4,000,000; optional, qualifying activities, exclusions and accounting condition in 2-4. New activity forecast confirmed by AT. | Law 9/2025 reprinted 2-4: https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| Goods/defined activities | Article 8(1)(a) specifies 3% up to 1,000,000 annual turnover;4% above 1,000,000 through 2,500,000;5% above 2,500,000 through 4,000,000. Do not invent a marginal-band engine or choose a rate without actual annual classification. | Law 9/2025 art 8: https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| Specified services / liberal professions |12% for specified trades/services;15% for liberal professions including consultants; higher applicable rate for mixed activities. Five-year liberal-profession stay limit with transitional terms. | Law 9/2025 art 8/9-A and transition: https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| Excess |20% on the part exceeding the maximum turnover limit; not an ordinary flat payroll rate | Law 9/2025 art 8(1)(d): https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |
| Quarter / invoices | Quarterly turnover base and payment/declaration; ISPC invoice must not include IVA. Article 10-A waives payment below 500 but not declaration; exact implementation/deadline held. | Law 9/2025 arts 9,10-A,11,12: https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf |

The old 2,500,000 threshold, universal 3%, fixed 75,000 and blanket 2026 abolition/default-organised-accounting conclusion are not current instructions. The preserved VAT retailer case has quarter turnover 400,000, which by itself does not establish the annual band, activity/election or a 12,000 liability.

## The base

### Residence, source and route before arithmetic

Current CIRPS 21 covers principal residence; professional activity in Mozambique unless proved secondary; centre of economic interests; and specified crew serving Mozambique-resident/managed entities. Its household provision and Mozambican nationals abroad not fully taxed there also matter. It applies independently of days/nationality. Do not decide residence under the removed>180-day shortcut or from a bank's location; obtain home/activity/economic-interest, household, foreign-tax and treaty facts.

For aggregate annual income, article 26 distinguishes income categories and excludes employment, article 57 final-rate receipts, qualifying exemptions and the new autonomous route. Annual business/professional taxable income follows the CIRPC rules as adapted by CIRPS 34/31; organised accounting and actual business assets/activities matter. A receipt's description does not prove revenue, an expense deduction or an exemption.

Rental income is separately classified; amended 48 specifies documented maintenance/conservation with its limit and specified interest conditions. Interest, dividends, commissions, independent technical/scientific work, artists, digital goods/services and e-money agents need their actual clauses, not the old 'all other income uses the same scale' shortcut. New 57(3)(e) concerns e-money agent commissions; (f) and(g) have specific digital provider/payer/IRPS-recipient conditions and 65(6) refers collection to regulation. Do not charge 10% on every digital-looking bank credit or automatically use 20% for every consultant.

Foreign tax is recorded gross under 26(6). Article 61 caps the credit by foreign tax and the attributable Mozambique collection, with treaty restrictions and conditional category-limited carryforward. Keep foreign-tax documentation and source/category calculations; a foreign withholding receipt is not an automatic full credit. Resident personal/family deductions under 59-60 cannot create a refund by themselves and do not migrate to salary PAYE, autonomous gains or a non-resident final-rate case. Where marital status changes during the year,60(2)apportions the specified personal/family deductions by the days of the relevant periods; do not assume a full-year deduction for a part-year status.

### Statutory annual minimum and form discrepancy

Article 54 prints 35,700 for the 25% band and 141,540 for 32%. The old 37,500 constant was wrong; replacing 141,540 with 143,340 would introduce another error. Formula comparisons tie at 42,000/168,000/504,000/1,512,000 at 4,200/23,100/90,300/342,300. They are continuity checks, not repeal of the minimum or an alternative PAYE algorithm.

Article 56 expressly preserves 225,000 and the per-holder family condition. The enacted 2020 M/10V primary Gazette retained on a private mirror has a minimum-before-rate step. The current AT-listed one-page M/10V has a visible total-net-income row and collectable-income reference without a visible minimum row; its extraction contains hidden/duplicate minimum text. Its listing date 22 October 2025 is not commencement or final 2026 clearance. That form conflict does not repeal 56; the private mirror is not promoted to an official-host operative citation. Hold final annual filing calculations and box mapping until the applicable route/current implementation is reconciled.

Consequently an example expressly starting from a separately established **post-minimum aggregate collectable base** may illustrate 54/60 arithmetic. An input originally described as salary or pre-minimum net income cannot silently be relabelled that way. Do not compute an annual employee liability by multiplying pay by 12, subtracting INSS and personal deductions, then dividing by 12.

### Statements, expenses and the workpaper

Match Portuguese terms case-insensitively and inspect direction/underlying evidence. Most-specific narratives win only for provisional bookkeeping classification, not final legal treatment. Preserve these original pattern groups:

| Pattern group | Provisional treatment / evidence required |
|---|---|
| SALARIO, ORDENADO, VENCIMENTO, REMUNERACAO, regular SUBSIDIO | Employment candidate; obtain gross/pay slips and use payroll. No automatic meal exclusion. |
| HONORARIOS, PRESTACAO DE SERVICOS, FACTURA, RECIBO, COMISSAO/COMISSOES | Business/service/commission candidate; identify employment, ordinary services, e-money or digital route and actual withholding/election |
| RENDA RECEBIDA, ARRENDAMENTO; JUROS RECEBIDOS/JUROS; DIVIDENDOS | Rental/capital candidate; apply actual category/final-rate/aggregation rules, not one universal annual scale |
| REEMBOLSO IMPOSTO, RESTITUICAO AT | Reconcile prior-year tax refund/liability; not automatically new business/salary income |
| RENDA ESCRITORIO, ARRENDAMENTO COMERCIAL; CONTABILISTA, CONTABILIDADE, TOC | Rent/accountancy business-cost candidate with activity, invoice and current tax-law support |
| ADVOGADO, JURIDICO, NOTARIO; MATERIAL ESCRITORIO/PAPELARIA; PUBLICIDADE/MARKETING/GOOGLE ADS/META | Legal, supplies and advertising candidates, not narration-only deductions |
| COMISSAO BANCARIA, ENCARGOS, MANUTENCAO CONTA; FORMACAO/CURSO/SEMINARIO; SOFTWARE/ASSINATURA/MICROSOFT/GOOGLE WORKSPACE | Business bank, training and subscription candidates; establish actual business connection and applicable deduction rules |
| EDM/ELECTRICIDADE, AGUA/FIPAG, TMCEL/VODACOM/MOVITEL | Utilities/telecoms: documented business/private split; no assumed home-office percentage |
| COMBUSTIVEL/GASOLINA/GASOLEO/GALP/PUMA/TOTAL | Fuel/running costs: actual business-use and vehicle records; no automatic deduction or invented percentage |
| RESTAURANTE/ALMOCO/JANTAR/ENTRETENIMENTO; SUPERMERCADO/SHOPRITE/GROCERIES/PESSOAL | Identify private/entertainment costs and current restrictions before any deduction; private living costs are not business drawings disguised as expense |
| MULTA/COIMA/PENALIDADE; IRPS/PAGAMENTO IMPOSTO/AT PAGAMENTO; LEVANTAMENTO/ATM/RETIRADA | Separate fines, income-tax settlement and private drawings from the business-cost subtotal; do not assume a deduction from a debit |
| INSS/SEGURANCA SOCIAL; PAGAMENTO POR CONTA/PPC | Separate contribution regimes, payroll liabilities and supported advance-tax credits, not a duplicated expense/credit |
| TRANSFERENCIA INTERNA/CONTA PROPRIA; EMPRESTIMO/REEMBOLSO EMPRESTIMO | Prove own-account transfer or loan principal, reconcile both sides and interest separately |

Original banks remain illustrative: BCI/Banco Comercial e de Investimentos (PDF/CSV; Data/Descricao/Debito/Credito/Saldo), Millennium BIM (Data Valor/Descricao/Montante/Saldo; TRF/DD/PAGAMENTO/COMPRA POS), Standard Bank Mocambique (Date/Description/Amount/Balance), Absa (Date/Narrative/Amount/Balance) and Banco Unico/Nedbank (Data/Movimento/Valor/Saldo). TRANSFERENCIA/TRF, DEBITO DIRECTO/DD, LEVANTAMENTO, ENCARGOS, JUROS and COMPRA POS are clues, not guarantees of format, tax character or deductibility.

The workpaper retains year, Client/NUIT, residence/source/category and dependent evidence, payroll and INSS records; separate employment, business, rental, investment and autonomous-income schedules; candidate expenses by rent, accountancy/legal, supplies/software, advertising, bank fees, training, utilities, vehicle and telecoms; documented business/private splits; actual aggregate collectable base/minimum reconciliation;54 scale/constant,59-61 collection deductions, withholding/advances, payment/refund reconciliation and reviewer flags. Keep employment outside the old A5-all-income minus B10-all-expenses shortcut. Do not use an unsupported Box 2 or M/10V line mapping.

With only statements, classify provisionally, mark every uncertain cost/transfer/regime and obtain invoices, organised-accounting records, prior assessment, payroll, PAYE and advance-payment confirmations. No income evidence is a hard stop. A bank-only cost list is not a supported filing calculation. Missing business-use evidence may be shown as a zero-deduction comparison with an explicit flag; it is not a legal finding that all costs are personal. No residence/category means no exact tax. Never default a valid or invalid ISPC election from missing data.

## Deadlines and filing

Law 11/2025 repeals the stated old employee declaration waiver, but definitive employment withholding and non-aggregation remain distinct. Do not carry the old employment-only 31 March deadline into a universal 2026 instruction. The official OCAM2018 copy visibly has the prefatory annual-declaration rule 1 January-30 April except employment/final-rate income, while missing even pages of its republication; the complete retained Gazette mirror supplies historical context but is not an official-host current consolidation. Reconcile current employee filing, regulator amendments, form and applicable dates before filing.

Original monthly PAYE20th-next-month, annual general 30 April, final 31 May/30 June and three advance dates 20 June/20 September/20 November remain calendar topics held for current operative confirmation and correct scope. CIRPS 66 does establish three equal second-category advances, total 80% of its prior-year/category-share computation, rounded upward under its terms; dates and exact current implementation must not be inferred from a secondary summary or incomplete page. Organised-accounting annual information and employee certificate/authority information are distinct obligations, not simply the Lista Nominal.

Modelo 10/M10V, eDeclaracao, e-fatura and Portal do Contribuinte were historical labels/URLs. Obtain the current official entry point, version and receipt. No live account, portal box or final current annual form was tested. ISPC has separate quarterly declarations/payment and invoicing under Law 9/2025; normal IVA is a different monthly regime.

## Penalties and interest

CIRPS 69 addresses arrears interest from the unpaid liability's due date; taxpayer-caused under-assessment may invoke compensatory interest. The precise current tax juros-de-mora rate and RGIT fixed fines remain unverified; do not convert the old USD estimate or apply MAIBOR plus 2% to every tax or INSS debt. INSS has the distinct RSSO 98 monthly-or-fraction 2% rule and offence-specific fines in social contributions. Escalate disputed enforcement or a request for a certified exact bill with official account/notices and dates; do not infer it from a bank debit.

## Cross-border points

Residence, Mozambique source/category, actual payer/payee, treaty and foreign tax must be established. Resident worldwide scope does not mean every receipt uses the annual scale; non-resident source does not mean every receipt is 20%. New digital/e-money and autonomous gains need their own clauses and collection rules. Non-resident complex source/treaty, capital-gain computations, corporate IRPC and unresolved 2026 regulation/form dependencies remain specialist/referral boundaries. INSS foreign coverage is a separate authenticated-proof question.

## Two worked examples that recompute

### Correct the old annual-table discontinuity claim

At the original 504,000 test boundary, compare the adjacent 54 formulas:20% x 504,000 -10,500 =90,300 and 25% x 504,000 -35,700 =90,300. At 1,512,000 both adjacent formulas give 342,300. This is a mathematical check of the printed constants, not a completed annual return, employment assessment or determination of the minimum's application to a particular input.

```oa-check
name: Statutory annual constants meet at original boundaries
inputs:
  boundary_1: 504000
  boundary_2: 1512000
steps:
  lower_1: boundary_1 * 0.20 - 10500
  upper_1: boundary_1 * 0.25 - 35700
  lower_2: boundary_2 * 0.25 - 35700
  upper_2: boundary_2 * 0.32 - 141540
expected:
  lower_1: 90300
  upper_1: 90300
  lower_2: 342300
  upper_2: 342300
```

### Original non-resident consultant, with route established

Original input: `10/04/2025 ; STANDARD BANK ; CLIENTE INTERNACIONAL ; HONORÁRIOS ; +200,000.00 ; MZN`. If this is the actual ordinary Mozambique-source non-resident service category under 57(2)(g), with no treaty/digital/special exception, withholding 20% of 200,000 is 40,000, leaving 160,000 after that withholding. The narrative alone is insufficient and no resident personal deduction is applied.

```oa-check
name: Original 200000 consultant conditional ordinary final-rate route
inputs:
  gross: 200000
  established_rate: 0.20
steps:
  withheld: gross * established_rate
  after_withholding: gross - withheld
expected:
  withheld: 40000
  after_withholding: 160000
```

### Remaining original cases, workpaper tests and corrections

- `25/03/2025 ; BCI TRANSFERÊNCIA ; EMPRESA XYZ LDA ; SALÁRIO MARÇO ; +50,000.00 ; MZN`: retain the original salary facts; do not treat a bank credit as proved gross. If gross monthly taxable pay really is 50,000 with zero dependents, payroll's matrix gives 1,775 +(50,000 -32,750) x 20% =5,225. On a separately established equal INSS base, employee 1,500/employer 2,000/combined 3,500; cash net 43,275. The old annual 600,000 / gross 112,500 / after-personal 110,700 employment computation is superseded, not an alternative liability.
- `25/03/2025 ; MILLENNIUM BIM ; ORGANIZAÇÃO ABC ; ORDENADO ; +14,000.00 ; MZN`, original two dependents: if 14,000 is established gross, monthly PAYE zero and employee INSS420. The old annual 168,000 / gross 23,100 / after 1,800+900 deduction 20,400 employment computation is rejected. It is not permissible to use annual personal/dependent deductions instead of the monthly column.
- `05/05/2025 ; BCI DÉBITO ; CONTABILISTA LDA ; HONORÁRIOS CONTABILIDADE ; -8,000.00 ; MZN`: retained accountancy-cost candidate for an actual business/professional job, not an unconditional 8,000 deduction. Obtain invoice, business link, regime and applicable CIRPC/CIRPS restrictions.
- `08/04/2025 ; MILLENNIUM BIM ; INSS ; CONTRIBUIÇÃO MARÇO ; -3,500.00 ; MZN`: matches 7% of an assumed 50,000 ordinary base, split 1,500 employee/2,000 employer, but needs receipt and period/base proof. INSS's own rule resolves the old 10th-versus 15th conflict; payroll tax has separate timing. Do not duplicate employer expense and liability settlement.
- `15/05/2025 ; BCI TRANSFERÊNCIA ; CONTA PRÓPRIA - POUPANÇA ; ; -20,000.00 ; MZN`: prove own-account transfer and reconcile the other side, then exclude from a new income/expense subtotal; do not infer a business deduction.
- Original annual tests 42,000,168,000,600,000 and 2,000,000: **if** each is a separately established aggregate post-minimum collectable base eligible for 54, scale arithmetic is 4,200;23,100;114,300;498,460. If 60's personal 1,800 and, for the original 168,000 case, two-dependent 900 deduction separately apply, arithmetic becomes 2,400;20,400;112,500;496,660. These are bounded formula regressions, not final liability on the original employment/pre-minimum facts or the unresolved current form. The former 37,500 constant and alleged statutory discontinuity are rejected.
- Original salary 30,000 + meal 4,000: no blanket meal exclusion. If competent evidence establishes a 30,000 contributory base, employee 900/employer 1,200/total 2,100; if all 34,000 is contributory,1,020/1,360/2,380. Obtain the component ruling; the old 2,100 default is not proved by its label.

## Ask the client first

Preserve the original onboarding questions: residence evidence; employment/business/other category and source; dependents and their taxable status; organised accounts and actual ISPC election; dedicated home-office arrangements; vehicle/mileage and business-use splits; telecoms use; INSS registration/payments; foreign income/tax and treaty facts; PAYE/advance payments and prior assessments. Add the actual year, payer/payee/beneficial ownership and current form/version when relevant. No invoices/organised books means no certified business deduction or annual return.

R-MZ-1 unknown residence/category/income is a stop; R-MZ-2 companies/IRPC is a separate job; R-MZ-3 complex non-resident source/treaty and R-MZ-4 autonomous gains require specialist facts; R-MZ-5 arrears/enforcement needs official records; R-MZ-6 routes IVA separately; R-MZ-7 holds unverified 2026 mechanics. Do not misuse personal deductions, automatic meal exclusions, the removed day test, an assumed ISPC abolition/election, unverified tax interest or an annual salary fallback. Every output is provisional pending qualified review.

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions or outcomes arising from its use. A qualified professional must review and sign off every output before filing or relying on it.

## Sources

| Official source | URL | Read on / actual scope |
|---|---|---|
| CIRPS 2017 enacted Gazette copy, OCAM | https://ocam.org.mz/wp-content/uploads/2024/06/Lei-n-19_2017-de-28-de-Dezembro-IRPS-2-1.pdf | 2026-11-15 retained original read;2026-11-17 focused visual/text review of 26/29/31/54/56/57/59-61/65-A/66/69, including 54(3) conditional ceiling. CIRPC 61(2) actual 2026 validity was not established. Source is an actual Gazette copy, not PwC commentary. |
| AT2025 reform Gazette Laws 9/10/11 | https://www.at.gov.mz/api/webdav?path=%2FLEGISLA%C3%87%C3%83O%2FLEGISLA%C3%87%C3%83O%20FISCAL%2FLEI%2FBR_248_I_SERIE_SUPLEMENTO_2025.pdf | 2026-11-15 actual official download and operative reads;2026-11-17 focused ISPC, income/residence and PAYE review. Commencement 1 January 2026. Not a complete later regulation. |
| Official AT form catalogue / actual retained M10V | https://www.at.gov.mz/formularios-tributarios | 2026-11-15:actual one-page download fully visually read and compared with text layer. Not a final 2026 form clearance. Catalogue access that failed is not described as read law. |
| Official 2018 decree copy, partial | https://ocam.org.mz/wp-content/uploads/2024/06/Decreto-51-2018-altera-o-CIRPS.pdf | 2026-11-15:all six odd Gazette pages visually read;2026-11-17 selected pages rechecked. Missing even pages remain missing; no complete-republication claim. |
| INSS contributor guidance | https://www.inss.gov.mz/direitos-e-obrigacoes-do-contribuinte/ | 2026-11-15; operative rate/registration/payment/carry text reopened/read 2026-11-17. |
| INSS2024 RSSO | https://www.inss.gov.mz/wp-content/uploads/2025/02/Decreto-56.2024-Altera-os-artigos-5-27-60-73-e-110-do-RSSO-aprovado-pelo-Decreto-5.2017-de-9-de-Outubro.pdf | 2026-11-15 contribution/coverage chapters; retained source bank reused for routed social contribution cases. |

Not yet confirmed: actual 2026 validity/application of 54(3) agricultural/livestock ceiling and its CIRPC 61(2) dependency, current annual minimum/form arithmetic and exact 2026 M10/M10V fields, fractional annual-band implementation, full current IRPS regulation/calendar and employee filing procedure, particular ISPC eligibility/accounting interaction and collection implementation, autonomous-gain and individual treaty/source/foreign-credit computations, complete CIRPC-specific business-cost restrictions, precise tax fines/juros-de-mora rate, municipal personal tax (old Maputo 510 in 2024 is not a current figure), detailed INSS component exclusions and special schemes. The 2018/2020 complete Gazette mirrors are retained research context, not official-host operative citations. No unverified secondary figure, hidden form text or unnumbered proposal is promoted to current law.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-17. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mozambique-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mozambique-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
