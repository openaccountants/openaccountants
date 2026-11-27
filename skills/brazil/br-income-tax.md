---
name: br-income-tax
description: >
  Brazil calendar-year 2026 personal income tax for resident self-employed individuals and
  professionals, normally reconciled in exercise 2027. Computes the ordinary annual table,
  separate income reduction and legal versus simplified deduction choice, then reconciles
  documented withholding and paid advances. Covers cash receipts, all earlier income/expense
  patterns, livro-caixa restrictions, personal deductions, current and historical bank cases and the
  annual workpaper. Trigger on IRPF, DIRPF, income tax Brazil, autônomo, freelance income,
  livro-caixa, desconto simplificado, INSS deduction, platform settlements and bank reconciliation.
  Route monthly Carnê-Leão, social contributions, company tax, crypto, offshore and capital gains
  to their owners. Distinguishes exercise 2026/calendar 2025 history from current calendar 2026
  law; complete exercise 2027 filing procedures and specialist minimum-tax cases are partial.
version: 2.2
jurisdiction: BR
category: international
tax_year: 2026
last_updated: 2026-11-27
source_checked: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: computation
domain: income-tax
---

# Brazil personal income tax: annual receipts, deductions and reconciliation, 2026 v2.2

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Classify a resident individual's actual receipts, establish the calendar-year taxable earnings and compare the complete legal deduction package with the annual simplified alternative. Apply the 2026 annual table to the selected base, then the separate annual reduction using taxable earnings before those deductions. Reconcile documented IRRF and actually paid advances after computing tax. INSS reduces the legal base; it is not an income-tax payment credit. Bank names, platform labels and a zero ordinary tax result do not decide return liability.

## Who this applies to

This Guide owns an ordinary resident individual's annual IRPF calculation for calendar 2026, normally reported in exercise 2027. Employment earnings and self-employed earnings subject to annual adjustment must be reconciled together; exempt, exclusively taxed and definitively taxed items have separate treatment. Residence transitions, estates, rural results, foreign financial/controlled-entity income, capital gains and crypto require their relevant rules before an ordinary base is final. [Lei 9.250 art. 8](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html), [RIR arts. 76,83](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html).

Load [br-estimated-tax](br-estimated-tax.md) for monthly Carnê-Leão classification, current monthly rates/reduction, precise foreign exchange and payment corrections; [br-inss](br-inss.md) for contribution category, plan, ceilings, concurrent sources and payment evidence; and [br-return-assembly](br-return-assembly.md) for the actual return workflow. An annual return does not substitute for a missed monthly payment. Do not divide an annual table by the number of months to invent a monthly table.

A sole individual's receipts are not company IRPJ receipts merely because a customer requests an invoice. Conversely, a company's gross revenue and an owner's individual withdrawals are distinct records. For MEI/Simples, establish actual registration, permitted activity, business revenue, accounting and distributions through [br-simples-nacional](br-simples-nacional.md), with distribution exemptions tested under [LC 123 art. 14](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html). MEI DAS does not establish that every withdrawal is exempt or that only a labelled pró-labore enters IRPF. For MEI status/distributions, check this point with one of our partner accountants. Keep the earlier MEI annual-limit/desenquadramento topic with that owner; turnover alone does not prove registration or eligible occupation.

The earlier corporate topics remain specific referrals to [brazil-corporate-tax](brazil-corporate-tax.md): the basic/additional IRPJ rate and monthly additional-tax boundary, lucro real/presumido/arbitrado, prior-year revenue eligibility and mandatory-activity exclusions, activity-based presumption percentages and the 2026 LC 224 increase on excess revenue. None is a personal-income-tax deduction or annual individual rate. Do not transplant corporate thresholds or rates into this computation. Check this point with one of our partner accountants.

Lei 15.270/2025 changed income tax from 2026 independently of the consumption-tax reform. Monthly dividend withholding and annual minimum tax can affect a person's final result. The ordinary calculation below cannot be used as a final high-income/minimum-tax or dividend computation. Check this point with one of our partner accountants. Screen the all-income position under Lei 9.250 art. 16-A where aggregate receipts exceed BRL 600,000; its base exclusions, credits and redutor require separate work. Received dividends need the actual distributing entity, payment dates and transitional-profit conditions, including the statutory approval date and original payment terms. Do not apply a dividend exemption or minimum-tax result from this Guide. Use [brazil-cross-border-tax](brazil-cross-border-tax.md) and the actual law for the relevant classification. [Lei 15.270 art. 2, adding arts. 6-A,11-A,16-A–16-B](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm).

## Rates, bands and thresholds

These annual base bands apply to **calendar 2026 / exercise 2027**, after the chosen permitted deduction package. The reduction's earnings amount is different from this calculation base. The annual schedule sums the monthly schedules legally in force for that calendar year under [Lei11.482 art.1 sole paragraph](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11482.htm); [Lei15.191 art.2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15191.htm) supplies the monthly table effective from May2025. This is not permission to sum separately calculated monthly tax as the annual liability. The source expressly names exercise 2027; the exercise-2026 Q&A remains useful for continuing substantive rules and historical procedures, not as a 2027 deadline announcement.

| Annual calculation base, BRL | Rate | Deduct from computed tax, BRL | Period / official source |
|---|---|---|---|
| Up to 29,145.60 | 0% | 0 | Calendar 2026, [RFB 2026 annual table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| 29,145.61 to 33,919.80 | 7.5% | 2,185.92 | Calendar 2026, [same table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| 33,919.81 to 45,012.60 | 15% | 4,729.91 | Calendar 2026, [same table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| 45,012.61 to 55,976.16 | 22.5% | 8,105.85 | Calendar 2026, [same table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| Above 55,976.16 | 27.5% | 10,904.66 | Calendar 2026, [same table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |

| Annual item | Amount / condition | Official source |
|---|---|---|
| Simplified alternative | 20% of taxable earnings subject to annual adjustment, capped at 17,640; replaces **all** legal deductions, not only livro-caixa | [Lei 9.250 art. 10, including X](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html); [RFB 2026 table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| Eligible dependent | 2,275.08 per year, subject to dependency conditions and inclusion of the dependent's relevant income | [Lei 9.250 art. 8 IIc; RIR art. 71](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html); [RFB 2026 table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| Eligible education | Individual annual limit 3,561.50; qualifying establishment/education types, no transfer of one person's excess to another | [RIR art. 74](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html); [RFB 2026 table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) |
| Annual taxable earnings up to 60,000 | Reduction up to 2,694.15, capped at the annual table tax | [Lei 9.250 art. 11-A and §1](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html) |
| Annual taxable earnings 60,000.01–88,200 | Reduction 8,429.73−(.095575 ×taxable earnings subject to annual adjustment), capped at table tax; above 88,200, none | [Lei 9.250 art. 11-A and §§1–2](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html) |

These are calculation and reduction amounts, not return-filing thresholds. In particular, zero ordinary tax does not mean no return. Historical BRL 35,584 taxable-earnings filing threshold and 23 March–29 May 2026 filing period belonged to **exercise 2026 / calendar 2025**, under IN 2.312/2026. Other historical triggers also existed: exempt/exclusive income, assets, gains, exchange transactions, rural activity, residence and specified offshore positions. The complete exercise 2027 trigger amounts/calendar are a non-usable hold: do not decide filing liability or a filing date from this Guide. Check this point with one of our partner accountants. [RFB exercise 2026 Q&A, Q 1 and Q 21](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

## The base

### Annual sequence and legal versus simplified decision

1. Establish residence and the exact year. Reconcile each actual receipt to payer, source, nature, cash month and gross amount before withholding or platform deductions. A bank credit can instead be a loan, gift, transfer, capital item or refund; preserve its own evidence and separate tax treatment.
2. Sum annual **taxable earnings subject to adjustment**, before the legal/simplified deductions; call this `R`. Keep exempt, exclusive/definitive, capital and specialist items in separate schedules. Do not count a platform settlement twice or convert a net amount to gross using an invented fee percentage.
3. Build total eligible legal deductions `L`: supported professional book deduction plus separately eligible personal official social contribution, dependent, alimony, medical/education and other actually established legal categories. Apply each condition/limit first. A month's INSS or expense is not automatically an annual deduction merely because it is a debit.
4. Compute simplified `S = min(.20×R,17640)`. It substitutes for the whole annual legal package. Compare the two complete calculations; do not subtract INSS, book costs, dependents, health or education a second time after choosing `S`. Monthly Carnê-Leão's choice does not make the annual choice for the taxpayer.
5. Compute each permitted base `B = max(0,R−chosen_package)`, then table tax `T = max(0,B×rate−table_deduction)`. Test the correct band, not a marginal rate applied to gross income without its table deduction.
6. Determine the annual reduction from `R`, not `B`. For `R≤60000`, use up to 2694.15 capped at`T`. For `60000<R≤88200`, cap `max(0,8429.73−.095575×R)` at`T`; above 88200 use 0. Subtract it and round monetary output to cents, reconciling the actual return calculation. At R = 88,200 the literal coefficients give 0.015, although the statutory text says the reduction reaches zero there. This boundary result is a non-usable hold: do not file using an invented cent-rounding convention. Check this point with one of our partner accountants.
7. Separately establish allowed annual tax credits, including documented IRRF and actually paid qualifying Carnê/complement principal. Apply any genuinely eligible foreign credit or other incentive only under its own conditions. Do not credit unpaid monthly liabilities, INSS, annual tax paid for a different exercise or late charges.
8. Reconcile the ordinary balance/refund and all separate monthly debts. Screen the dividend/minimum-tax and other specialist schedules before calling this the final return liability. A payment already used against another period is not a fresh credit.

The annual-income aggregation/base and legal categories come from [Lei 9.250 arts. 8,10–13](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html), with current reduction from [Lei 15.270 art. 2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm). Paid-monthly principal/annual aggregation are also in [RIR arts. 80–81,120,127](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html).

### Classify the source and the withholding

For ordinary nonemployee work paid by a Brazilian company to a person, progressive personal withholding applies under RIR art. 685, using the applicable monthly law. **1.5% professional-services withholding in art. 714 concerns specified PJ→PJ payments**, with its own exceptions; it is not a default on an individual consultant's invoice. A company customer, PIX sender or platform's Brazilian entity name does not prove that withholding actually occurred. Use the actual income certificate and payment records. [RIR arts. 685,714](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html).

Official social contribution withheld from an individual is a different system from corporate labour-supply/empreitada invoice retention under [Lei 8.212 art. 31](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html). Establish the worker's contribution category and concurrent sources through br-inss. The taxpayer's own eligible official contribution is a **personal legal deduction**, while qualifying employer charges on the professional's own employees can be a book cost. Neither is an IRRF tax credit. Do not duplicate personal INSS in both categories. [RIR arts. 68 I,75 I](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html).

Ordinary taxable receipts from PF/abroad need a cash-month Carnê calculation; an actual foreign company's ordinary work payment can fall there. Notarial/public-officer exceptions and categories taxed under financial/capital/crypto law prevent an absolute PF/PJ label rule. Zero computed tax is different from a missing calculation, and a receipt's amount alone does not establish a fine. Use the monthly owner for aggregation, foreign-purchase conversion, reduction and lawful payment due date; income remaining abroad does not alone defer an ordinary receipt. [RIR arts. 118–123; current received-alimony correction in Q 266](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

### Legal deductions and professional costs

**Personal deductions.** Official social contributions require the actual eligible burden/payment; establish dependency and the person's income rather than deduct a name. Qualifying family-law alimony requires the prescribed judicial instrument/agreement/public deed, cash and other statutory conditions. For the monthly deduction under RIR art. 72 §1, do not also deduct the same beneficiary as a dependent from the payment month. Annual dependency/alimony transitions, including the year a family relationship ends, are a non-usable hold here; do not extend the monthly bar to the whole annual return. Check this point with one of our partner accountants. Received qualifying family-law alimony has the STFADI 5422 exemption described in current Q 266, despite the old RIR monthly example list. Monthly medical/education payments for an alimentando do not become alimony deductions; annual treatment has its own statutory rules. Private/complementary pension (including PGBL versus VGBL), FAPI eligibility/limits and disputed alimony are held out of `L` until individually established. Check this point with one of our partner accountants. [RIR arts. 71–76](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html), [Q 266–267](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

Medical/health-plan deductions concern qualifying paid treatment for the taxpayer/dependents and the separately permitted alimentando case, with provider and payment evidence; reimbursed/insured amounts cannot be deducted again. Equipment/prosthesis and special treatment cases have their additional proof conditions. Education covers the specified qualifying establishment/education levels, not every course, with the individual annual cap above and no cross-person excess transfer. Ordinary personal mortgage interest is not among the annual legal deduction categories in Lei 9.250 art. 8; do not add it from a loan description or the earlier “main residence” assumption. This does not certify an unrelated business-financing cost. [RIR arts. 73–74,76](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html); [Lei 9.250 art. 8 II](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html).

**Livro-caixa.** Eligible nonemployee activity costs must be paid, necessary to earn receipts/maintain the source, recorded and supported by suitable documents. They can matter even where professional clients are exclusively PJs; Q 441 separately explains annual income and book-cost entries. Apply the actual monthly activity-receipt limits and within-year carry; excess can pass to later months through December, never to the following year. Do not create a negative activity or treat unused personal deductions as book loss. The specific next-month alimony rule is separate in the monthly owner. Transport-service and garimpeiro categories are outside the ordinary book algorithm here. [RIR arts. 68–69](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html); [Q 427,441](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

Enduring equipment, furniture and instruments are capital acquisitions, not ordinary consumable book costs; depreciation and leasing do not become deductions merely through business use. Ordinary travel/vehicle/fuel expenses are barred, with the autonomous commercial-representative exception. Q 444 permits the stated necessary, unreimbursed specialty congress/seminar travel/hotel/materials with documentation and attendance certificate; it does not approve every business flight. Mixed home/professional costs require evidence; Q 436 permits one fifth of the stated shared costs where the professional portion cannot be proved, and excludes owned-home repairs/conservation/recovery. Do not invent a universal floor-area or mileage percentage. [Q 427,433–436,444](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

### All earlier transaction patterns: evidence before classification

The labels below remain search clues. The tax treatment follows the actual receipt/cost and cited rules above, not a deterministic bank-label classifier. The table is an evidence checklist. A conditional cost enters `L` only after the rule above and its facts are established. Otherwise its deduction is a non-usable hold. Check this point with one of our partner accountants.

| ID | Earlier bank pattern | Current classification / evidence |
|---|---|---|
| I-01 | TED DE / PIX DE client | Reconcile direction, actual payer and service/invoice; an identified sender can transfer loan/capital/gift as well as fees |
| I-02 | PIX RECEBIDO client | Same evidence test; repeated qualifying fees aggregate, but PIX alone does not establish taxable gross or withheld tax |
| I-03 | DOC DE client | Legacy payment-channel clue, same receipt test; no current DOC availability claim |
| I-04 | STRIPE PAYOUT / PAGAMENTOS | Obtain settlement detail, underlying customers, gross fees/refunds and currency; platform label does not establish foreign source or domestic withholding |
| I-05 | PAYPAL SAQUE / TRANSFERÊNCIA | Trace underlying receipt and any own-account transfer; do not automatically treat the withdrawal as a new foreign receipt or use unspecified PTAX |
| I-06 | MERCADO PAGO / MERCADOPAGO | Reconcile gross consideration, fees, returns and net settlement from actual reports; no invented percentage gross-up |
| I-07 | HOTMART / SAQUE | Same gross/net/source reconciliation; neither current fee nor automatic IRRF is verified here |
| I-08 | KIWIFY / EDUZZ | Same; actual contract/payer/receipts, not the brand, determine classification |
| I-09 | NOTA FISCAL / NF SERVIÇOS | Invoice reference is evidence; verify gross, payer, actual IRRF and individual's social contribution separately |
| I-10 | RESTITUIÇÃO IRPF RECEITA | Reconcile the actual income-tax refund separately; it is not a fresh professional-service receipt or a new deduction |
| I-11 | POUPANÇA / CDB / LCI / LCA | Obtain investment certificate and classify exempt/exclusive/definitive items under their product rules; do not put every bank yield into ordinary work receipts or certify exemption from label |
| I-12 | DIVIDENDOS | Obtain distribution/accounting and dates; 2026 withholding/annual minimum and qualifying old-profit conditions require their actual rules, not a blanket exemption |
| E-01 | ALUGUEL ESCRITÓRIO / SALA | Paid necessary professional rent can qualify; distinguish rental-income exclusions from an activity expense and document mixed use |
| E-02 | ENERGIA / LUZ / CPFL / CEMIG | Supported professional share; shared-home Q 436 rule, not automatic 100% or an invented floor-area proportion |
| E-03 | TELEFONE / INTERNET / VIVO / CLARO / TIM / OI | Prove necessary activity use and amount; Q 436 stated shared-cost rule only within its scope, no brand-based deduction |
| E-04 | ADOBE / MICROSOFT 365 / GOOGLE WORKSPACE | Test actual subscription/current service versus a capital acquisition and private use; business label alone is insufficient |
| E-05 | CONTADOR / ESCRITÓRIO CONTÁBIL | Test paid necessary professional service and documentation; no blanket assertion every self-employed person must employ an accountant |
| E-06 | PASSAGEM / LATAM / GOL / AZUL | Ordinary travel bar; apply only a supported statutory exception such as Q 444 event conditions, not any stated business destination |
| E-07 | HOTEL / BOOKING / AIRBNB | No automatic deduction; necessary unreimbursed specialty-event lodging within Q 444 requires records/certificate, other cases held out of `L` |
| E-08 | GPS / INSS | Establish eligible personal official contribution separately; employer charges on own employees differ; no double deduction or income-tax credit |
| E-09 | CARNÊ-LEÃO / DARF 0190 | Actual qualifying paid principal is an annual advance, not book cost; separate late charges and payment status |
| E-10 | DARF IRPF / SALDO DIRPF | Annual tax payment is not deductible operating cost; reconcile its own exercise/liability, not a second annual advance by label |
| E-11 | SEGURO PROFISSIONAL / RC | Establish coverage, necessary activity connection, actual payment and absence of private component; no unconditional deduction verified for the label |
| E-12 | PLANO DE SAÚDE | Test personal annual medical/health-plan deduction, beneficiaries, evidence and reimbursements; do not put personal plan in book costs |
| E-13 | ESCOLA / MENSALIDADE ENSINO | Qualifying personal annual education with individual cap, not book cost or every training bill |
| E-14 | COMBUSTÍVEL / GASOLINA / POSTO | General transport/vehicle bar; commercial-representative exception must actually apply; mileage log alone does not remove the bar |
| E-15 | MATERIAL / PAPELARIA | Actual necessary consumables can qualify; enduring equipment/capital assets require separate treatment |
| E-16 | TARIFA BANCÁRIA / TED ENVIADO / IOF | Transfer is not itself a cost; identify actual charge, legal character and necessary activity connection. No universal deduction for bank fees or IOF certified |
| E-17 | ASSINATURA / MENSALIDADE | Actual necessary current professional service, private-use and capital distinction; not every recurring debit qualifies |
| E-18 | CURSOS / TREINAMENTO / CAPACITAÇÃO | Apply qualifying education or necessary professional-event rules as appropriate; no blanket book deduction for personal development |
| E-19 | REEMBOLSO cliente | Obtain contract, original expense, payer and reimbursement evidence; do not automatically net out taxable receipts or assume reimbursement is exempt; prevent a duplicate cost claim |
| E-20 | NOTA DE DÉBITO / NF COMPRAS | Document actual goods/service, payment, necessity and consumable/capital character; an invoice alone does not make equipment deductible |

These are the earlier 12 income and 20 expense patterns. For unsupported insurance, bank/IOF charges, reimbursements or other disputed costs, do not claim a deduction or exemption from the narration. Check this point with one of our partner accountants. No bank/platform product feature or fee is represented as verified 2026 information.

Earlier additional narrations remain covered: SWIFT/remessa internacional, Upwork/Fiverr and Google AdSense use the I-04–I-08 underlying-source/gross-net test; water/SABESP/Cedae/Copasa use the shared-cost test; Amazon/Mercado Livre purchases use E-15/E-20; Slack/Notion/GitHub/Figma use E-04/E-17. Own-account savings transfers, loan proceeds, personal drawings and credit-card settlements require reconciliation to avoid duplicate income/cost. Professional dues, ISS, legal/marketing costs, clothing/uniforms, meals/entertainment and fines are not approved or rejected solely by their old labels; unestablished treatment is held out of `L`. Check this point with one of our partner accountants.

### Annual working paper

Keep one receipt schedule by month, payer and tax character, including gross/retained/net reconciliation; a separate investment/exempt/capital schedule; and separate book and personal-deduction ledgers. Record supported monthly book excess/utilisation, rather than deriving annual expenses from an incomplete bank sample. Store each deduction's beneficiary, proof, limit and chosen annual method.

The summary should show `R`, legal total`L`, simplified`S`, both bases/table taxes/reductions, chosen ordinary tax, actual IRRF, actual paid 0190/0246 principal, eligible separate credits, ordinary balance/refund and unresolved minimum-tax/other schedules. Keep own INSS among legal deductions only. A separate monthly liability table should show receipt period, due date, principal, fine, interest, payment/import status and unmatched differences. This is a suggested evidence design, not a statutory return layout.

The old worksheet's double subtraction of INSS after simplified, medical costs treated as tax credits, receipt-day sale/annual-average income FX and assumed platform gross-up must not survive. Record actual currency/date/quote evidence from the monthly owner. Carry the taxpayer CPF, source certificates, monthly reconciliation and reviewer exceptions into the actual year's return; do not manufacture a field or filed receipt from this workpaper.

## Deadlines and filing

The annual **tax year** and the **exercise** printed on the return must match the actual receipts. Q 26 describes exercise 2026 access through PGD 2026 or Meu Imposto de Renda via Receita/e-CAC/Portal de Serviços/app, subject to its service exclusions. It is evidence of the available 2026 workflow, not a verified screen map for exercise 2027. Use the actual exercise's official service and instructions before submission. [RFBQ 26](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

1. Establish the actual year's filing triggers, including other income/assets/gains/residence/special positions, before deciding no return is due. Use br-return-assembly and the actual exercise instruction. Historical taxable-income trigger 35,584 does not become a 2027 threshold.
2. Obtain/correct payer certificates and reconcile actual gross receipts and IRRF. Q 55 permits supporting monthly payment evidence in the specified impossible-correction situation, subject to proof; Q 56 requires declaration of all taxable income even without a certificate. Continue reconstructing income while withholding an unsupported tax-credit claim; missing a certificate does not erase earnings.
3. Reconcile the actual income/deduction/credit records into the appropriate annual forms, including separate PJ earnings, PF/foreign earnings and livro-caixa information, eligible personal deductions, investments and specialist schedules. Q 441's PJ-only professional book-cost entry is a useful bounded example; verify actual exercise 2027 fields before filing. Prefilled information remains evidence to reconcile against actual records.
4. Review both annual deduction calculations and any minimum-tax/dividend/special schedules, then transmit only after the taxpayer's actual return is complete. Retain the submission receipt and status, generated payment record and actual bank/Receita payment confirmation separately. A generated DARF is not paid tax.
5. Distinguish codes:0190 mandatory Carnê-Leão,0246 optional complement and 0211 annual IRPF quotas. The old 5936/1854 references are not authority for an annual settlement/Carnê code; use the actual generated record. Reconcile an annual 0211 payment already used against another quota before claiming an excess credit. [RFB payment situations A–B](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/restituicao-ressarcimento-reembolso-e-compensacao/creditos/pagamento/darf/situacoes-especiais), [Q 269–272](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

Certificate timing is a separate issue from the annual return: Q 55 states the last business day of February following the income year, or earlier employment termination, for the specified income evidence. Its 2026/calendar 2025 example supports the earlier calendar topic; verify the applicable current-year obligation and actual certificate rather than assume a report has arrived. Current source-payer reporting moved from routine annual DIRF to eSocial/EFD-Reinf for events from calendar 2025. Do not instruct a 2026 payer to file a new routine DIRF because an old onboarding script mentions DIMEs/DIRFs. The taxpayer's actual access and payer corrections remain necessary. [Q 55–56](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf), [RFB current DIRF support](https://www.gov.br/receitafederal/pt-br/canais_atendimento/fale-conosco/suporte-a-dirf/leiame).

**Historical calendar retained, not 2027 instructions:** exercise 2026 opened 23 March 2026, closed 29 May 2026, with first/single quota 29 May 2026. Q 63 allowed up to 8 monthly quotas, minimum 50 each and tax below 100 paid once, with the prescribed interest on later quotas; Q 64 gives that year's dates. For ordinary annual settlement, Lei 9.250 art. 14 permits up to 8 equal monthly quotas, each at least 50; tax below 100 is paid once. Later quotas carry statutory interest, with the SELIC start corrected by Lei 9.430 art. 62 to the month after the timely-filing month and 1% in the payment month. The complete exercise 2027 deadline, quota calendar and service exclusions remain a non-usable hold. Check this point with one of our partner accountants. Monthly qualifying Carnê remains a distinct last-business-day-next-month workflow in its owner. [Q 21,63–64](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

## Penalties and interest

Keep late filing, late payment and an assessment penalty separate. The shared federal late-payment computation, including the daily fine/cap and SELIC timing, is owned by [br-estimated-tax](br-estimated-tax.md); use its current rule and the [RFB Sicalc guidance](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/pagamentos-e-parcelamentos/darf-calculo-e-impressao-programa-sicalc-1/informacoes-uteis-sobre-o-sicalc) for the actual debt. Use actual calendar/Sicalc inputs, not a daily fixed SELIC percentage. Charges do not become annual tax credits. For the actual covered overdue federal principal, Lei 9.430 art. 61 charges 0.33% per day from the day after maturity through payment, capped at20%; SELIC runs from the month after maturity through the month before payment, plus1% in the payment month. Use Sicalc for same-month and actual-date computation. An annual return does not automatically extinguish every unpaid month. [Lei 9.430 art. 61](https://www.planalto.gov.br/ccivil_03/leis/l9430.htm), [Q 270–271](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

Exercise 2027 late-filing amounts, assessment/fraud penalties, amended-return election limits and dispute/refund procedures are non-usable holds here. Check this point with one of our partner accountants. A PGFN/Receita debt procedure or denúncia espontânea requires the actual debt, authority and legal conditions; the old useful-link label is not an automatic penalty waiver. Do not apply the old automatic 75%/37.5%/150%/225% assertions or promise immunity from voluntary correction. Check this point with one of our partner accountants.

## Cross-border points

For ordinary qualifying foreign work receipts, use br-estimated-tax's full sequence: non-USD toUSD at source-country monetary-authority receipt-date value, then BCB **purchase** on the last business day of the previous month's first fortnight. Foreign-currency deductions use their prescribed **sale** sequence/date. The bank's conversion price, receipt-day sale quote and annual average are not substitutes. [RIR arts. 119,121§3](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html), [RFB Q 266](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

Treaty/reciprocity foreign-tax credits, residence changes and offshore financial/controlled-entity results are non-usable holds in this Guide. Check this point with one of our partner accountants. Route the concrete facts to [brazil-cross-border-tax](brazil-cross-border-tax.md). Crypto and digital-asset reporting/tax categories belong to [brazil-crypto-tax](brazil-crypto-tax.md); the earlier blanket monthly-disposal threshold and all-crypto-as-capital-gain shortcut are not adopted here. Ordinary rent uses [br-carn-monthly-income-tax-rental-income](br-carn-monthly-income-tax-rental-income.md), with the actual permitted exclusions; do not claim maintenance as a blanket rental deduction from this Guide. Domestic capital-gain/GCAP bands and exemptions are separately determined, not included in ordinary professional receipts. The earlier capital-gain tier/threshold topic is retained as a specialist calculation, with no usable rates or exemptions supplied here. For these specialist outcomes: Check this point with one of our partner accountants.

## Worked cases

Use each case's stated calendar year and eligibility assumptions.

## Two worked examples that recompute

### Ana / Bradesco: ordinary annual simplified calculation

Assume calendar 2026 taxable annual earnings 48,000, no other income or specialist/minimum-tax complication, and eligible legal deductions less than the 9,600 simplified amount. Simplified 20% gives 9,600, below the 17,640 cap; base 38,400. The 15% annual row gives 1,030.09. Earnings 48,000 qualify for the first reduction tier; the reduction is capped at 1,030.09, leaving ordinary annual tax 0. Do not invent the old 720 IRRF from 1.5%; any actual advance/refund must be supported by real withholding/payment records. Zero ordinary tax alone is not a return-filing decision.

```oa-check
name: BR2026 annual simplified income and capped reduction
inputs:
  taxable_earnings: 48000
  simplified_rate: 0.20
  simplified_cap: 17640
  annual_reduction_max: 2694.15
steps:
  - simplified: min(taxable_earnings * simplified_rate, simplified_cap)
  - base: max(0, taxable_earnings - simplified)
  - table_tax: round(max(0, base * 0.15 - 4729.91), 2)
  - reduction: min(table_tax, annual_reduction_max)
  - ordinary_tax: table_tax - reduction
expected:
  simplified: 9600
  base: 38400
  table_tax: 1030.09
  reduction: 1030.09
  ordinary_tax: 0
```

### Fernanda / Inter: compare the whole legal package

Assume actual status is a non-MEI individual, calendar 2026 taxable gross 72,000, valid paid personal official contributions 14,400 and allowable paid book costs 6,000. All monthly activity limits/documentation are met; no other income, credits or specialist complication. The contribution is a stipulated documented deduction, not an annual contribution formula or ceiling. Legal total 20,400 exceeds simplified 14,400. Legal base 51,600 gives table tax 3,504.15; simplified base 57,600 gives 4,935.34. Both use earnings 72,000 for reduction 1,548.33. The legal result 1,955.82 is 1,431.19 below simplified 3,387.01. Do not compare only 6,000 expenses against 14,400 while ignoring the personal contribution.

```oa-check
name: BR2026 annual complete legal versus simplified deduction decision
inputs:
  taxable_earnings: 72000
  documented_personal_inss: 14400
  allowable_book_costs: 6000
steps:
  - legal: documented_personal_inss + allowable_book_costs
  - simplified: min(taxable_earnings * 0.20, 17640)
  - legal_base: max(0, taxable_earnings - legal)
  - simplified_base: max(0, taxable_earnings - simplified)
  - legal_table: round(max(0, legal_base * 0.225 - 8105.85), 2)
  - simplified_table: round(max(0, simplified_base * 0.275 - 10904.66), 2)
  - nominal_reduction: max(0, 8429.73 - 0.095575 * taxable_earnings)
  - legal_tax: round(legal_table - min(legal_table, nominal_reduction), 2)
  - simplified_tax: round(simplified_table - min(simplified_table, nominal_reduction), 2)
  - legal_saving: simplified_tax - legal_tax
expected:
  legal: 20400
  simplified: 14400
  legal_base: 51600
  simplified_base: 57600
  legal_table: 3504.15
  simplified_table: 4935.34
  nominal_reduction: 1548.33
  legal_tax: 1955.82
  simplified_tax: 3387.01
  legal_saving: 1431.19
```

### Six 2025 bank cases: original facts, corrected limits

| Earlier case | Historical treatment and reconciliation |
|---|---|
| Carlos / Itaú, mixed TI consulting | The printed sample receipts 7,500+5,500+4,200+1,800+8,200 total 27,200; they do not prove 89,000 annual income. Obtain the missing months/source records. Stripe 4,200 is not proved foreign by label; travel 650 is not automatically deductible; personal INSS belongs outside book costs. Do not annualise selected debits or invent 975 withholding at 1.5% on an assumed 65,000 PJ total. The old claimed 32,685.20 deduction package combined personal INSS 18,691.20 with accounting 9,600, software 3,600, fees 144 and travel 650 without establishing eligibility/full-year payments. Its 4,632.79 was 2025 arithmetic on unsupported assumptions; the printed 850 Carnê debit does not prove an annual paid total |
| Ana / Bradesco, architect | Current 48,000 example above replaces the old 2025 table and unsupported 720 withholding. The old 1,080.97 tax and 360.97 balance were 2025 arithmetic with an unsupported 720 credit. The earlier extra 6,000 INSS cannot be deducted after simplified; its 697.81/22.19 and 293.77/426.23 tax/refund variants also used wrong bands or obsolete table deductions. Compare the full legal package even where a simplified result is available; actual records govern any credit/refund |
| Paulo / Banco do Brasil, hospital and patients | Preserve 120,000 hospital/36,000 patients as assumed gross components, not proof of 1,800 IRRF or 13,200 individual contribution. Reconcile contribution category/monthly ceiling/concurrent work before any 5,400 complement; the assumed 18,000 clinic rent still needs paid/necessary/limit evidence and 8,000 enduring equipment is not a current book deduction. Do not certify the old 111,400 base/19,781.22 tax from those inputs. Reconstruct monthly patient receipts and lawful deductions |
| Julia / Nubank, Hotmart/Kiwify | Net 85,000 and 22,000 do not establish gross 95,000 and 24,500. Even a hypothetical percentage fee must be proved; no current 9.9%+1 tariff is adopted. Obtain settlement-level sales/refunds/fees/source/withholding, not automatic IRRF from platform identity. The old 8,000 cost estimate is not automatically the complete legal package; 119,500 total/17,401.28 tax cannot be reused as a verified result (even its historical arithmetic was 17,401.28 only after rounding 28,255.0565) |
| Ricardo / Santander, CLT plus engineering | Assumed salary 48,000 plus professional gross 60,000 is 108,000 receipts; only after validating 22,000 book costs does 86,000 become the stated pre-personal-deduction base. Establish full legal versus simplified, actual salary INSS and actual 4,800 IRRF separately. Own/withheld INSS never subtracts from tax alongside IRRF/Carnê. Old 12,796.22 was 2025 arithmetic, not the updated result |
| Fernanda / Inter, MEI question | Confirm registration/activity and split business/individual records first;72,000 alone does not make her a MEI or all withdrawals exempt. With confirmed non-MEI status and documented assumptions, Example 2 corrects the deduction comparison and gives 1,955.82 ordinary 2026 tax. The earlier 4,986.22 was 2025 simplified arithmetic. On the same stipulated valid 2025 deductions, the complete legal package gives base 51,600 and tax 3,555.03; actual contribution eligibility remains a hold |

These are the original calendar-2025 situations, not new 2026 taxpayer facts. The two worked examples above separately stipulate calendar 2026. Historical claimed balances are non-usable until their evidence gaps are closed. Check this point with one of our partner accountants. The historic figures are explicitly described as prior calculations or assumptions, not asserted law. One client's concentration of revenue can justify checking the contractual/employment facts; the old 90% concentration is not adopted as a statutory employment test. Do not infer an employment relationship or absence of one from a bank ratio.

### Earlier 2025 bank cases and tests

The original six cases below preceded the six named cases above. Their **calendar 2025** is retained. A historical amount does not become a 2026 rate. Tables use the [RFB 2025 annual bands and cap](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2025); only supported inputs may be used. Unproven historical outcomes remain non-usable. Check this point with one of our partner accountants.

| Historical bank case | Preserved inputs and disposition |
|---|---|
| H1 Itaú consultant | 180,000 PJ + 36,000 PF; claimed IRRF 2,700, book costs 25,000, INSS 14,016, one dependent amount 2,275 and estimated Carnê 5,400. The sample TED 13,250 is not 15,000 less 225 (that is 14,775). Neither 1.5% IRRF nor annual paid credits are established. If every stipulated deduction and its amount were valid, 2025 arithmetic on base 174,709 gives 37,191.20, then 29,091.20 if 8,100 credits were proved; no filing result certified. The rounded dependent input is not silently increased. Check this point with one of our partner accountants. |
| H2 Bradesco designer | 72,000 PF receipts, 12,000 book costs, 7,920 INSS. With all deductions valid, complete package 19,920 gives base 52,080 and 2025 tax 3,663.03; simplified 14,400 gives base 57,600 and tax 4,986.22. Complete saves 1,323.19. Do not subtract INSS again after simplified; earlier bases 49,680/52,080 and estimates 5,913/6,548 did not establish that simplified wins. |
| H3 Banco do Brasil doctor | 400,000 mixed receipts, 80,000 clinic costs, 14,016 INSS, medical 15,000, PGBL 20,000 and two dependent amounts totalling 4,550; claimed IRRF 6,000 and Carnê 18,500. PGBL/INSS entitlement and estimated credits remain unproved. If every stipulated deduction and its amount were valid, 2025 arithmetic on base 266,434 is 62,415.57, then 37,915.57 only if all 24,500 credits were proved. Do not certify the old 62,516/38,016 estimates or an INSS ceiling from these inputs. Check this point with one of our partner accountants. |
| H4 Caixa foreign developer | 60,000 domestic receipts + USD 30,000 assumed to equal 150,000 BRL; book 20,000, INSS 14,016, IRRF 900, Carnê 28,000. The sample 25,000 Stripe credit, 150 IOF and 30 bank fee do not establish conversion or deduction. Pure 2025 arithmetic on base 175,984 is 37,541.82 and balance 8,641.82 if all assumptions/credits were valid, not the old 37,642/8,742. FX/source/payment facts are a non-usable hold. Check this point with one of our partner accountants. |
| H5 Nubank MEI comparison | 75,000 turnover, sample receipts 12,000/6,500, GitHub 180 and DAS 72.85; earlier annual DAS estimate 874 and IRPF 5,000+ did not establish eligibility or a lower whole-tax result. Do not choose MEI from turnover alone or certify a current DAS. Check this point with one of our partner accountants. |
| H6 Santander instalments | 120,000 income and assumed 15,000 final tax; eight principal amounts are 1,875 each. Income alone does not establish the 15,000 liability, and an August sample debit is not proof of a timely first quota. Check actual year, due dates and interest under Lei 9.250 art. 14 / Lei 9.430 art. 62. Check this point with one of our partner accountants. |

The older EC1–EC10 and Test1–Test6 retain their 2025 inputs. Deductions/credits below are conditional on actual eligibility, monthly limits and proof; a missing receipt or unpaid tax is not replaced by an assumption.

| Original ID | Corrected 2025 treatment / retained hold |
|---|---|
| EC1 | March receipts 3,000, eligible book costs 4,500: use 3,000 now; excess 1,500 may carry to later months through December, not the next year. The old “lost immediately” rule was wrong. [RIR69](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html) |
| EC2 | Same-month 5,000 PJ with actual IRRF + 3,000 ordinary PF fees: monthly Carnê computation concerns the 3,000 PF receipt; aggregate both in the annual calculation and credit only evidenced taxes. No automatic fine merely from a receipt. [RIR118,120,685](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html) |
| EC3 | Income 80,000; stipulated eligible INSS 8,000, dependent 2,275, education 3,561, medical 15,000. Total 28,836 beats simplified 16,000: bases 51,164/64,000; 2025 taxes 3,456.93/6,746.22. Preserve the rounded original inputs; validate actual statutory entitlements separately. [2025 table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2025) |
| EC4 | Dental 2,000 with no receipt: hold until statutory payment/provider proof is established; the law includes a named-cheque alternative when documentation is absent, so “no receipt = always impossible” is too absolute. [Lei9.250 art.8 §2 III](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html) |
| EC5 | Separate spouse returns cannot deduct the same dependent concurrently. Do not promise automatic rejection of a particular return. [Lei9.250 art.35 §4](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html) |
| EC6 | Earnings 15,000/month, paid INSS 3,000/month; old assumed ceiling 8,157.41 / contribution 1,631.48. Category, applicable ceiling, excess deduction/refund are held; an amount paid alone does not prove deductible entitlement. Check this point with one of our partner accountants. |
| EC7 | Eligible university tuition 8,000 for one dependent: deduction 3,561.50; 4,438.50 exceeds that person's cap, with no transfer of excess. [RIR74](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html) |
| EC8 | Calendar2025 monthly exemption boundaries were 2,259.20 January–April and 2,428.80 May–December. Use those period-specific tables for historical months, the separate annual table for the annual computation. [2025 tables](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2025) |
| EC9 | Resident's US-company freelance income in USD: apply the ordinary conversion/monthly rules above; actual exchange dates and treaty/credit entitlement are held. Check this point with one of our partner accountants. |
| EC10 | Original turnover above the assumed MEI boundary 81,000 mid-year: preserve facts and establish actual registration/transition consequences; this does not by itself turn a business into an autônomo. Check this point with one of our partner accountants. |
| Test1 | Single, 90,000 PF income; book15,000, INSS12,000, one dependent2,275.08, education3,561.50, medical8,000 and zero paid Carnê/IRRF. Eligible total40,836.58 gives base49,163.42 and 2025 tax3,006.80; simplified cap16,754.34 gives9,288.78. No unpaid Carnê credit; reconstruct each monthly debt rather than infer a fine. [2025 table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2025), [RIR69,120](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html) |
| Test2 | Single, gross50,000, book5,000, INSS6,000; no other deductions. Complete11,000 gives base39,000/tax1,170.97; simplified is20% of50,000 =10,000, base40,000/tax1,320.97. Complete saves150. The old simplified9,000/base36,000/tax720.97 deducted book costs twice. [Lei9.250 art.10](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html), [2025 table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2025) |
| Test3 | Monthly receipts2,000, eligible book costs3,500: current deduction2,000, base0, excess1,500 carries only within the same calendar year under RIR69. [RIR69](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html) |
| Test4 | Ordinary freelancer receives10,000/month exclusively from Brazilian PJs with actual withholding: progressive IRRF, no Carnê merely because the worker is freelance; keep special public-officer/foreign exceptions distinct. [RIR685](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html); [Q266](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf) |
| Test5 | Two eligible dependent children, qualifying tuition5,000/2,000: deduct3,561.50+2,000 =5,561.50, no transfer of unused/excess limits. [RIR74](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html) |
| Test6 | PJ60,000/actual IRRF4,500; PF30,000/paid Carnê2,800; valid book8,000 and INSS10,000. Gross90,000; complete18,000 gives base72,000 and 2025 tax8,946.22; credits7,300 leave1,646.22. Simplified cap16,754.34 gives tax9,288.78, so complete wins. [2025 table](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2025), [Lei9.250 art.12 V](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html) |

### Bank-import evidence checklist

| Bank / earlier topic | Safe import and reconciliation task |
|---|---|
| Itaú Unibanco | If supplied `Data;Histórico;Valor;Tipo`, establish actual C/D convention, DD/MM date and decimal/thousands separators from the file; the earlier export/app path is not verifiedcurrent |
| Bradesco | Inspect actual `Data;Documento;Histórico;Valor;Saldo` or another schema; verify signs/parentheses and opening/closing balance, not assumedpositivecredit |
| Banco do Brasil | Inspect the supplied `Data;Lançamento;Débito;Crédito;Saldo` example/actual columns and PIX sender evidence; schemas can differ |
| Santander Brasil | Use actual PDF/CSV and references such as TRANSFPIXDE/TED; no current app/export capability is certified |
| Nubank | Treat the old PDF-only/no-nativeCSV statement as unconfirmed; inspect the supplied export and reconcile, without recommending a third-party converter as required |
| Caixa Econômica Federal (earlier case) | Inspect the supplied debit/credit/balance layout and actual source/currency evidence; a USD narration is not the statutory exchange rate |
| Banco Inter | Inspect actual `Data;Tipo de Transação;Valor` or supplied layout; the old app navigation and download formats are not current-source verified |

PIX/TED/DOC descriptions and any displayed sender CPF/CNPJ are investigation clues. Obtain the actual counterparty and underlying transaction; a CPF-shaped sender or payment key is not itself proof of a professional service or of withholding. No current bank schema, fee, data-access permission or payment-channel availability has been researched for this Guide.

## Ask the client first

1. Actual residence, calendar/exercise, CPF, registration/MEI/company status and other employment/business/rural/offshore/capital positions.
2. All gross receipts by payer/source/month/currency, full-year bank exports and invoices/settlement reports, distinguishing transfers/refunds/loans from earnings.
3. Income certificates and monthly payment evidence, actual IRRF, personal official contributions and whether they were already used elsewhere; confirm discrepancies with the payer.
4. Eligible book costs, monthly activity-receipt limits/carry, capital purchases, reimbursements and supporting documents; separately eligible dependents/alimony/health/education and other legal categories.
5. Actual 0190/0246/0211 records with taxpayer, period, principal/charges, payment status and prior use; omitted monthly calculations and annual returns/receipts.
6. Investment/dividend/treaty/residence/minimum-tax facts, and the actual exercise's filing instruction/calendar before any payment/submission.

## When to refuse or refer

Continue supported reconstruction when a certificate or bank field is missing, but do not invent gross annual income, withheld credit, currency quote, deduction right or paid advance. MEI/company uncertainty requires classification of the affected receipts, not the claim no individual tax can arise. Missing monthly tax is tested by its actual receipts/base/reduction, not assumed from every PF/foreign credit. For missing foreign dates/currency, pause that conversion while continuing domestic reconciliation.

For full corporate regimes, MEI distributions, municipal ISS, financial/crypto/capital/rental special rules, residence/treaty credits, high-income minimum tax, disputed deductions and debt/dispute procedures: preserve the concrete issue/evidence, hold the affected outcome, and refer the issue. Check this point with one of our partner accountants. Retain unresolved ordinary costs separately and supply the supported comparison. Never add simplified to legal deductions, deduct personal INSS twice, classify a capital asset as a consumable, allow a generic bank/platform label to establish an exemption/credit, or present an unsupported 2027 filing date as confirmed.

## Sources

| Source and portions actually read | Official URL | Read on |
|---|---|---|
| RFB calendar 2026: five annual bands, personal/simplified amounts and reduction, expressly exercise 2027 | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026 | 2026-11-27 |
| Lei 9.250 consolidated: arts. 8,10–14,16-A–16-B screen,34–35; deduction conditions, annual reduction and credits | https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html | 2026-11-27 |
| Lei 15.270 art. 2: 2026 commencement, dividend conditions and annual/minimum-tax changes; full specialist calculation held | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm | 2026-11-27 |
| Lei11.482 art.1 sole paragraph and Lei15.191 art.2: annual schedule aggregation and monthly table from May2025 | https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11482.htm ; https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15191.htm | 2026-11-27 |
| RIR continuing provisions: arts. 38,67–69,71–77,80–81,118–123,127,685,714; old rate tables not used as current | https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html | 2026-11-27 |
| RFB exercise 2026 Q&A: Q 1 taxable-income trigger;21,26,29,55–56,63–64;266–267,427,433–436,441,444; no whole-manual read claimed | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf | 2026-11-27 |
| LC123 art.14 caput/§§1–2: distinct business receipts and owner distributions; full regime held | https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html | 2026-11-27 |
| Lei8.212 art.31 caput/§§1–4: corporate labour-supply retention distinguished from personal contributions | https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html | 2026-11-27 |
| RFB calendar 2025: annual table and simplified cap for historical computations; monthly split for EC8 | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2025 | 2026-11-27 |
| Lei 9.430 arts. 61–62: late-payment charge and quota-interest starting month | https://www.planalto.gov.br/ccivil_03/leis/l9430.htm | 2026-11-27 |
| RFB special payments A–B: annual 0211; monthly 0190/0246 and no double use | https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/restituicao-ressarcimento-reembolso-e-compensacao/creditos/pagamento/darf/situacoes-especiais | 2026-11-27 |
| RFB DIRF support: calendar 2025 onward substitution by eSocial/EFD-Reinf | https://www.gov.br/receitafederal/pt-br/canais_atendimento/fale-conosco/suporte-a-dirf/leiame | 2026-11-27 |

Not yet confirmed: exercise 2027 filing thresholds/calendar/screens/service exclusions; exact output at the annual reduction upper boundary; taxpayer-specific credits/FX/payment facts; current bank/platform schemas/fees; complete MEI/corporate/ISS, pension, minimum-tax/dividend, crypto/offshore/capital/treaty/residence and disputed-cost outcomes; assessment/fraud/late-filing, amendment, debt/refund and voluntary-disclosure procedures. These are non-usable holds, with the concrete facts preserved above. IN 208's cited endpoint returned no readable text; the stated ordinary FX rules are instead supported by RIR119/121 and RFB Q266. Check this point with one of our partner accountants.
