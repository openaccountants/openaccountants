---
name: br-estimated-tax
description: >
  Brazil calendar 2026 Carnê-Leão monthly personal income tax for resident individuals receiving qualifying
  taxable receipts from individuals or abroad. Covers classification, cash receipt month, current progressive
  table and separate 2026 reduction, legal versus simplified deductions, livro-caixa conditions and within-year
  carry, precise foreign exchange, DARF 0190 timing/generation and verified payment evidence, ordinary late
  charges and annual reconciliation. Trigger on Carnê-Leão, recolhimento mensal obrigatório, DARF 0190,
  livro-caixa, Brazilian estimated personal tax, foreign freelance receipts and monthly tax reduction. Includes
  recomputing legal/simplified decision and professional-income examples plus all earlier edge cases/tests.
  Excludes corporate IRPJ estimates, complete annual-return preparation and specialist nonresident, financial,
  crypto, capital-gain, treaty and disputed-deduction computations not established here.
version: 2.1
jurisdiction: BR
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: computation
domain: income-tax
---

# Brazil Carnê-Leão: monthly personal income tax, receipts and payment, 2026 v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** An individual resident in Brazil ordinarily calculates Carnê-Leão monthly on qualifying taxable receipts from individuals or abroad that were not taxed at source in Brazil. Aggregate the month's relevant receipts, establish lawful deductions and compare the monthly simplified alternative, apply the current progressive table, then the separate 2026 reduction using taxable earnings before those deductions. Pay supported tax through DARF 0190 by the last business day of the next month. A bank label, foreign transfer or annual return alone does not establish the monthly tax or prove it was paid.

This Guide covers calendar-year 2026 monthly personal income tax, normally reconciled in exercise 2027. It does not calculate a company's IRPJ monthly estimate: use [brazil-corporate-tax](brazil-corporate-tax.md). Annual personal tax and return liability belong to [br-income-tax](br-income-tax.md) and [br-return-assembly](br-return-assembly.md); INSS contributions to [br-inss](br-inss.md). The 2026 income-tax reduction is a real change under Lei 15.270/2025. Consumption reform is not a basis for saying the income-tax structure remained unchanged.

## Who this applies to

Start with the nature of each receipt, actual payer and residence. Ordinary nonemployee services to individuals, rent received from individuals and qualifying taxable foreign receipts can fall under RIR arts. 118-123. A foreign company paying an individual's ordinary work income is not automatically a Brazilian withholding payer; such foreign receipts can still enter Carnê-Leão. A Brazilian company's ordinary payment for an individual's work generally follows its withholding route instead. Notarial/court-officer receipts can enter this regime regardless of whether the payer is a PF or PJ, except where the officer is remunerated exclusively from public funds (Q 266). This prevents a blanket “no receipt connected with a PJ can ever be Carnê-Leão” rule.

Not every bank credit or overseas item is taxable Carnê-Leão income. Capital gains, financial/offshore income governed by Lei 14.754/2023, crypto and variable-income categories need their own rules and owners: [brazil-crypto-tax](brazil-crypto-tax.md) and [brazil-cross-border-tax](brazil-cross-border-tax.md). Non-residents and residence-transition periods require the cross-border classification first. The old RIR example list also includes received alimony, but current Receita Q 266 explains the STF ADI 5.422 outcome for qualifying family-law alimony: do not copy that historical list as an operative tax charge on the exempt receipt.

No qualifying taxable receipts can mean zero monthly Carnê-Leão, but preserve the ledger and any allowable within-year book-expense carry. A zero tax calculation is not a universal exemption from keeping documents, annual reporting or another tax. Repeated qualifying receipts must be aggregated even when each individual payment is below the first band.

## Rates, bands and thresholds

The base-column amounts apply to the calculation base after the selected permitted deductions, not the gross reduction-test amount. Current figures are from Receita's 2026 table; historical tables in RIR/2018 or the exercise-2026 Q&A must not replace that year's table.

| Monthly calculation base, BRL | Rate | Deduct from computed tax, BRL | Period / official source |
|---|---|---|---|
| Up to 2,428.80 | 0% | 0 | 2026, [Receita 2026 monthly table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| 2,428.81 to 2,826.65 | 7.5% | 182.16 | 2026, [same official table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| 2,826.66 to 3,751.05 | 15% | 394.16 | 2026, [same official table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| 3,751.06 to 4,664.68 | 22.5% | 675.49 | 2026, [same official table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| Above 4,664.68 | 27.5% | 908.73 | 2026, [same official table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |

| Additional monthly item | Amount and conditions | Official source |
|---|---|---|
| Dependent legal deduction | BRL 189.59 per eligible dependent; do not duplicate against another monthly withholding calculation | [Receita 2026 table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026); [RIR art. 121 §1](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html) |
| Monthly simplified alternative | BRL 607.20, replacing the legal deduction package, including livro-caixa for this choice; do not add it to INSS, dependents, alimony or book costs | [Lei 9.250 art. 4 §2](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html); [Receita 2026 table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| Reduction where monthly taxable earnings are at most BRL 5,000 | Up to BRL 312.89, limited to the tax produced by the table/selected deductions so it cannot make tax negative | [Lei 9.250 art. 3-A, as added by Lei 15.270](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html) |
| Reduction from BRL 5,000.01 through BRL 7,350 taxable earnings | BRL 978.62 − (0.133145 × taxable earnings subject to monthly incidence), limited to pre-reduction tax. Above BRL 7,350, none | [Lei 9.250 art. 3-A and §§1-2](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html) |
| Small DARF | If positive Carnê-Leão is less than BRL 10, the system does not generate the DARF and adds the amount to the next month's tax; do not silently erase it | [Receita Como pagar, small-DARF paragraph](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/pagar) |

## The base

**Monthly sequence.** (1) Classify each cash receipt and the income/payment period. (2) Convert a qualifying foreign amount using the statutory sequence below. (3) Total the taxable earnings subject to this monthly calculation before legal/simplified deductions; call this `R`. Identify exempt/excluded receipts separately rather than treat every bank credit as `R`. (4) Build the supported legal deduction package without duplicate personal deductions and with the actual book-expense limit/carry. Compare that package with the BRL 607.20 alternative; do not combine them. (5) Floor the resulting calculation base at zero and apply the matching progressive-table row: `T = max(0,base × rate − table_deduction)`. (6) Determine the reduction from `R`, not from the reduced calculation base, cap it at `T` and subtract. Round supported monetary outputs to cents and reconcile to the actual system result. (7) Apply any actually eligible foreign-tax credit under its separate conditions, reconcile earlier/small payments, and retain the month-by-month calculation and payment evidence.

For `R ≤ 5000`, the nominal reduction is 312.89 capped by `T`. For `5000 < R ≤ 7350`, use `max(0,978.62 − .133145 × R)`, capped by `T`; for `R > 7350`, use zero. At exactly 7,350 the literal formula produces 0.00425, which rounds to zero cents. Do not promise the reduction simply because legal deductions reduced an BRL 8,000 gross taxable receipt below BRL 7,350. Likewise, separately zero withholding from one source does not promise zero annual tax once other income is aggregated.

**Legal personal deductions.** Establish the actual eligible official INSS contribution borne/paid or withheld, eligible dependents and qualifying paid family-law alimony under RIR arts. 67,71,72 and 121. Alimony needs the actual court decision, judicially approved agreement or qualifying public deed and its statutory conditions; an informal transfer or arbitral award is not sufficient. Q 267 requires qualifying cash payments and, for a conjugal society, its dissolution. Under RIR art. 72 §§1-2, do not also deduct the same beneficiary as a dependent from the month alimony is paid; qualifying alimony not used as a deduction in its payment month may be deducted in the following month. Record that specific carry separately from book expenses. Medical/education payments for an alimentando do not become monthly alimony deductions, even when court-ordered; their separate annual treatment is subject to art. 72 §§4-5 and the annual owner. RIR art. 121 §1 prevents reusing INSS, dependents and alimony already deducted from other income subject to withholding in that month. Use [br-inss](br-inss.md) to establish the contribution rather than assume an old example amount is a current ceiling. The annual simplified choice is independent of the monthly choice and replaces annual legal deductions under its own rules.

**Livro-caixa.** RIR arts. 68-69 require eligible paid, necessary, documented nonemployee professional costs and bookkeeping. They can include qualifying employee pay/employer charges, office rent, professional utilities and consumables. They are not blanket deductions against employment or rental income. The ordinary book-cost method here excludes expenses relating to transport services and garimpeiro receipts, which Q 427 and RIR art. 68 sole paragraph III treat separately; refer those categories for their own supported classification. Aggregate the actual professional receipts used for the monthly book limit, including eligible PF/PJ/foreign professional receipts as shown in the current manual. Book costs can have annual relevance even for a professional paid exclusively by Brazilian companies; a zero Carnê tax does not abolish the book record.

Maintain the expense ledger separately from the personal deductions: `available = eligible_paid_costs + earlier_same_year_excess`; `used = min(available,eligible_activity_receipts)`; `excess = max(0,available − eligible_activity_receipts)`. The excess can be carried through December of the same calendar year, with no carry into the next year. Do not create a negative taxable activity or treat personal deductions or an unchosen simplified/legal alternative as excess book costs. Apply the specific next-month alimony rule above separately; do not invent a general carry for other unused personal deductions. When professional receipts mix PF/PJ sources, reconcile the manual's book-limit and utilisation screens and the annual book deduction; do not count an expense twice or invent a bank-label allocation.

The earlier general permission for professional travel was too broad. RIR art. 68's sole paragraph and Q 433 exclude ordinary locomotion/transport/vehicle expenses, with the autonomous commercial-representative exception. Q 444 separately permits necessary, unreimbursed professional-specialty congress/seminar costs, including the specified travel/hotel/materials, with attendance proof and supporting records. Consumable materials differ from enduring equipment, furniture or instruments: capital acquisitions are not a current book-cost deduction; depreciation and leasing are not made deductible by merely calling them business expenses. For mixed residence/professional costs whose professional share cannot be proved, Q 436 gives a one-fifth rule for the stated shared costs and excludes the specified owned-property repair/conservation/recovery costs; do not impose an invented universal floor-area percentage. Rental exclusions are governed separately by RIR art. 42 and the rental owner [br-carn-monthly-income-tax-rental-income](br-carn-monthly-income-tax-rental-income.md).

**Annual reconciliation.** RIR art. 120 makes monthly income part of the annual adjustment and paid monthly principal an advance credit. Reconcile annual income/base/choice/tax, eligible IRRF, actually paid Carnê principal and other permitted credits; do not credit an unpaid liability or penalties/interest. Annual tax less actual credits can produce a balance or refund, but the annual return does not automatically settle every monthly debt, separate fine or payment mismatch. Keep monthly debts/charges and annual advances distinct to prevent double payment or double credit. Use the annual owner for the 2026-income reduction, high-income/dividend interaction and exercise-2027 return; its thresholds/calendar must not be copied from the exercise-2026 manual.

## Deadlines and filing

1. **Use the current official service.** Access Carnê-Leão Web through Receita's [Apurar carnê-leão service](https://www.gov.br/pt-br/servicos/apurar-carne-leao/) and the actual GOV.BR route. The application supports calendar periods from 2021 onward; use the named historic-year program for older periods rather than a current table. No taxpayer credentials or real filing are needed for this reference workflow.
2. **Enter verified data for the right year/month.** Use the current manual's configuration, receipts, eligible payment/deduction and dependent records. Record payer/beneficiary identity where required and keep foreign-income capability aligned with the actual facts. Review the Demonstrativo de Apuração and book/foreign-tax compensation screens, rather than infer output from a bank total.
3. **Generate DARF 0190 for supported tax.** Due by the last business day of the month following receipt (RIR art. 123); December income's ordinary payment falls in January of the next year. Check the actual calendar/holiday. The official fields include name, CPF, assessment period as the last date of the receipt month, revenue code 0190, maturity, principal, fine, interest and total; the reference field is not filled under the cited payment guide. Use the actual generated record, not a free-text template as proof of accepted filing.
4. **Pay and verify.** Use an actually supported bank/payment channel and retain the guide, receipt and confirmation in Receita. From calendar 2026 the current manual says nature “Imposto Pago” cannot be added manually: confirmed payments are imported automatically from Receita's systems. Do not manufacture a manual paid item because a bank CSV resembles a tax debit. A lag or mismatch requires reconciliation with actual payment identifiers/status.
5. **Track small balances and corrections.** Positive tax below BRL 10 accumulates under the official system rule; zero tax produces no payable principal. Preserve carry and actual competence. Q 270 permits excess/undue paid principal to be credited against later Carnê-Leão within the same calendar year or in the annual adjustment; its refund request is made through the annual return. Q 272 identifies Redarf for a timely Carnê payment mistakenly coded 0246. Preserve the original record and use the actual correction procedure; an unmatched bank debit is not an established excess credit.

### Bank-statement classification library

| Pattern from the earlier file | Correct evidence-based treatment |
|---|---|
| DARF / DOCUMENTO DE ARRECADACAO | Candidate federal payment only; obtain code 0190, CPF, assessment period, principal and receipt before calling it Carnê-Leão |
| RECEITA FEDERAL / RFB or monthly timing | Insufficient by themselves: many taxes share the issuer and payment month |
| CODIGO0190 / CARNE LEAO / CARNE-LEAO | Strong candidate identifier, still reconcile competence, taxpayer and actual payment status |
| IMPOSTO DE RENDA MENSAL | Candidate, not proof of the actual code or principal |
| February debit / March debit / January next year | Usually January / February / December income only if the actual assessment period confirms; arrears/accumulated amounts can differ |
| Another DARF code / IRPF QUOTA / DECLARACAO ANUAL | Separate obligation: voluntary complement 0246 and annual settlement are not 0190; classify the actual code rather than discard an unexplained debit |
| INSS / CONTRIBUICAO PREVIDENCIARIA / GPS | Social-security payment, separate from monthly income-tax principal |
| ISS / IMPOSTO SOBRE SERVICOS | Municipal service tax, separate from Carnê principal |
| IRRF / RETENCAO NA FONTE | Withholding record, not a duplicate self-paid 0190 by default |
| MULTA / JUROS DE MORA | Separate principal from fine/interest; such text does not erase the Carnê principal included in the same actual payment |

These are bookkeeping evidence rules, not a statutory guarantee that a particular bank description always means one tax. Monthly income tax paid is not a deductible professional operating expense merely because it is a debit.

## Penalties and interest

Lei 9.430 art. 61 governs ordinary late charges: daily fine 0.33%, capped 20%, from the first day after maturity through payment; interest uses the statutory SELIC accumulation from the month after maturity through the month before payment plus 1% in the payment month. No interest is charged when paid within the maturity month. Use the actual calendar/Sicalc result; the older Receita payment page's shorthand “first business day” must not replace the statute's first day following maturity. SELIC is not a daily fixed interest rate.

For a hypothetical principal BRL 667.89, 45 late days and stipulated accumulated pre-payment-month SELIC 0.92%, the fine is BRL 99.18, interest BRL 12.82 and total BRL 779.89. These are assumed inputs, not the actual SELIC or date count for a named month. The older test principal BRL 680.62 would instead give 101.07 fine and 13.07 interest, total 794.76 under those same assumptions. That preserves the historic arithmetic without presenting the old monthly tax as a 2026 result.

Not paying the monthly charge does not remove the obligation or make it an annual paid credit. Q 271 confirms legal accruals do not become tax credits. Q 271 specifies separate DARF 3244 for legal charges where monthly principal was paid late without its fine/interest. That narrow situation is distinct from other assessments: unpaid or partly paid principal and payment corrections still require their actual debt/assessment procedures, not a guessed code for every case.

## Cross-border points

For ordinary taxable foreign receipts, first convert non-USD amounts into USD using the source-country monetary authority's rate on the receipt date, then USD into BRL using Banco Central's **purchase** quote on the last business day of the first fortnight of the preceding month (IN 208 art. 16; RIR art. 119). Foreign-currency deductions use the prescribed **sale** quote under RIR art. 121 §3. Do not substitute the bank's settlement price, receipt-day sell quote, annual average or an unspecified “PTAX”. Keep date, currency, authority and quote direction in the workpaper.

A hypothetical USD 3,000 receipt at a stipulated legally appropriate BRL 5.20 purchase quote gives BRL 15,600; that multiplication does not establish that 5.20 was the correct actual quote/date. Apply the ordinary table/reduction only after confirming the income belongs in this regime. A remittance staying abroad does not by itself defer ordinary receipt taxation.

Foreign income tax may credit subject to treaty/reciprocity, non-refund/non-compensation abroad and the Brazilian incremental-tax cap, with timing and within-year excess rules described in Q 267/current manual. Verify the actual treaty, tax character, payment and permitted carry before using the credit; use [brazil-cross-border-tax](brazil-cross-border-tax.md). Offshore financial/controlled-entity, crypto, non-resident, capital-gain and treaty-special cases are separate classifications, not all foreign cash Carnê-Leão.

## Two worked examples that recompute

### Example 1: standard professional receipt, correct2026 table

Assume qualifying PF receipts BRL 8,000, a stipulated eligible paid official contribution BRL 877.24, one eligible dependent not already deducted elsewhere, and documented allowable book costs BRL 1,200 with no carry/mixed activity complication. Legal deductions total2,266.83, which is greater than607.20. The base is5,733.17. Its27.5% calculation minus 908.73 gives 667.89. Gross taxable earnings8,000 exceed 7,350, so there is no reduction despite the lower base. The877.24 is an assumed valid paid deduction, not a current individual INSS maximum.

```oa-check
name: BR2026 ordinary Carnê-Leão with supported legal deductions
inputs:
  taxable_receipts: 8000
  stipulated_paid_inss: 877.24
  dependent: 189.59
  allowable_book_costs: 1200
  simplified_alternative: 607.20
steps:
  - legal_deductions: stipulated_paid_inss + dependent + allowable_book_costs
  - chosen_deduction: max(legal_deductions, simplified_alternative)
  - base: max(0, taxable_receipts - chosen_deduction)
  - table_tax: round(max(0, base * 0.275 - 908.73), 2)
  - reduction: 0
  - payable_principal: table_tax - reduction
expected:
  legal_deductions: 2266.83
  base: 5733.17
  table_tax: 667.89
  payable_principal: 667.89
```

### Example 2: legal versus simplified choice and separate reduction amount

Assume qualifying ordinary receipts 6,000, supported total legal deductions 800 and no foreign credit/carry. Legal base 5,200 gives pre-reduction 521.27. Simplified base 5,392.80 gives 574.29. Both use the same gross-earnings reduction 978.62−(.133145×6,000)=179.75, capped by their respective tax. Legal-choice tax 341.52 is 53.02 lower than simplified 394.54; choose the legal package for this month. The annual choice must still be tested independently.

```oa-check
name: BR2026 monthly legal versus simplified decision with income reduction
inputs:
  taxable_receipts: 6000
  legal_deductions: 800
  simplified: 607.20
steps:
  - legal_base: max(0, taxable_receipts - legal_deductions)
  - simplified_base: max(0, taxable_receipts - simplified)
  - legal_before: round(max(0, legal_base * 0.275 - 908.73), 2)
  - simplified_before: round(max(0, simplified_base * 0.275 - 908.73), 2)
  - nominal_reduction: max(0, 978.62 - 0.133145 * taxable_receipts)
  - legal_tax: round(legal_before - min(legal_before, nominal_reduction), 2)
  - simplified_tax: round(simplified_before - min(simplified_before, nominal_reduction), 2)
  - legal_saving: simplified_tax - legal_tax
expected:
  legal_base: 5200
  simplified_base: 5392.80
  nominal_reduction: 179.75
  legal_tax: 341.52
  simplified_tax: 394.54
  legal_saving: 53.02
```

### Preserved earlier examples, edge cases and tests

| Original case/topic | Current treatment / arithmetic |
|---|---|
| Original example 1/test 1,8,000 with 877.24/189.59/1,200 deductions | Example 1 above corrects 680.62 to 667.89 under 2026; no gross-income reduction |
| Original example 2/test 2/EC 4,base 2,000 | Below current first band 2,428.80, zero table tax; do not confuse a base threshold with gross reduction threshold |
| Original example 3/test 3/EC 1,PF 5,000 plus Brazilian PJ 10,000 | Classify PF into Carnê and PJ into its ordinary withholding route; with no duplicate deductions, the PF monthly calculation can be zero after 2026 reduction. Annual aggregate can still owe tax |
| Original example 4/test 6/EC 2,USD 3,000 at 5.20 | BRL 15,600 only when 5.20 is a stipulated legally correct quote; actual date/direction/nature must be verified |
| Original example 5,bank record 28.02.2025/DARF 0190/01-2025/−680.62 | Historical explicit period/code example, not 2026 tax: reconcile actual receipt/status; principal is a tax advance, not book cost |
| EC 3/test 4,no qualifying receipts in March | Zero ordinary monthly tax, preserve records/eligible book carry and other obligations |
| EC 5,book costs exceed eligible monthly receipts | Base cannot become negative; only qualifying book excess carries within that calendar year through December, no next-year carry |
| EC 6,monthly simplified versus itemised | Current 607.20 alternative, never add it to legal package; Example 2 shows actual comparison |
| Original test 5,late payment 680.62/45 days/0.92% stipulated SELIC | Fine 101.07,interest 13.07,total 794.76; hypothetical/historical arithmetic, not an actual 2026 period. Current 667.89 illustration is separately 99.18+12.82=779.89 |

Before handing off, reconcile source/type/year, all monthly receipts, correct table and reduction amount, documented book costs/carry, nonduplicated personal deductions, actual FX, DARF code/period, paid principal versus accruals, due date, actual SELIC and the annual reconciliation. Mark unsupported facts as unresolved; professional review concerns the person's actual position, distinct from a source check of this Guide.

## Ask the client first

1. Residence, actual receipt month/year, payer identity/country and income nature; evidence for exemptions or special categories.
2. Monthly qualifying gross receipts and all other taxable/withheld income, with bank, invoice/receipt and foreign-currency evidence.
3. Actual eligible INSS, dependents and qualifying alimony already used in other monthly withholding calculations.
4. Eligible paid book costs, supporting documents, earlier same-year excess and PF/PJ activity receipts used for the limit.
5. Existing 0190/other payment records, CPF/assessment period, principal/fine/interest, actual payment dates and Receita import/status.
6. Foreign tax/treaty/reciprocity facts, residence changes, crypto/financial/capital-gain income or unresolved specialist deductions.

## When to refuse or refer

Do not compute without monthly receipt values and classification; a “soft warning” is not permission to guess a gross amount. Refer ordinary Brazilian-company withholding to its proper owner, crypto/financial/gains and non-residence to their specialist owners, and uncertain book-expense/alimony/foreign-credit eligibility for source-supported determination. Withhold a payment instruction when period, code, actual FX or prior-payment status is missing. Never classify generic RFB/DARF text as a proven 0190 payment, add simplified to legal deductions, carry personal deductions as book losses, use an annual average FX rate, or label unpaid monthly tax as annual credit.

## Sources

| Source and portions actually read | Official URL | Read on |
|---|---|---|
| Receita 2026 table, read for all five monthly bands, dependent/simplified deductions and monthly reduction; annual figures kept in annual owner | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026 | 2026-11-11 |
| Lei 9.250 current Câmara text, arts. 3-A,4 including § 2,6,8,10; current 2026 reduction, legal/simplified choice and foreign currency | https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html | 2026-11-11 |
| Lei 15.270/2025, relevant amendments adding 2026 monthly/annual changes; not a consumption-tax exemption | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm | 2026-11-11 |
| RIR 2018 current Câmara text, arts. 42,67-69,71-72,75-77,118-127: scope, deductions, book carry, FX, monthly/annual interaction and timing; old rate tables not used for 2026 | https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html | 2026-11-11 |
| Receita exercise 2026 Q&A, Q 266-272 and selected Q 427, 433-434, 436, 441 and 444-445 read for classification/deduction/book/credit rules; file identifies calendar 2025 and is not authority for 2027 filing dates | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf | 2026-11-11 |
| IN 208/2002 current text, art. 16 and relevant paragraphs, non-USD→USD and prescribed BRL quote/date | https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=15079 | 2026-11-11 |
| Receita Carnê-Leão manual, read for receipts/payments, 2026 automatic paid-tax import, Demonstrativo and book/foreign-tax compensation sections | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/manual | 2026-11-11 |
| Receita Como pagar, read for current route, DARF fields and less-than-10 carry; statutory day-count wording governs over shorthand | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/pagamento/carne-leao/pagar | 2026-11-11 |
| Official Apurar service, read for current GOV.BR/Carnê-Leão access and named period workflow | https://www.gov.br/pt-br/servicos/apurar-carne-leao/ | 2026-11-11 |
| Lei 9.430 art. 61 and neighboring paragraphs, ordinary late fine/monthly interest and maturity-month rule | https://www.planalto.gov.br/ccivil_03/leis/l9430.htm | 2026-11-11 |

Not yet confirmed: the complete exercise 2027 filing/payment-calendar and annual instalment rules; the taxpayer's actual FX/SELIC/payment status; full separate-penalty/refund/correction procedures; specialist book, private-pension, foreign-credit, treaty, alimony, financial/crypto/gains and residence facts not established by these ordinary inputs. The earlier “up to 8 annual instalments” statement is retained as an annual-owner topic, not promoted from exercise 2026 into a confirmed 2027 rule. Current eligible quarters, annual codes and other taxpayer-specific fields must be verified in that owner rather than guessed from 0190.
