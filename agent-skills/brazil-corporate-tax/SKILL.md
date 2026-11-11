---
name: brazil-corporate-tax
description: "Brazil corporate income tax for calendar year 2026 for ordinary resident companies and advisers calculating IRPJ and CSLL. Covers lucro real, eligibility for lucro presumido, ordinary rates and the IRPJ surcharge, the 2026 increase in presumptive percentages under LC 224/2025, activity allocation, deductions, separate loss pools, quarterly payments, annual estimates, ECF and DCTFWeb/MIT. Includes the dividend changes under Lei 15.270/2025 and two recomputing cases, including a lucro real versus presumido decision. Trigger on IRPJ, CSLL, lucro presumido, lucro real, Brazil company tax, ECF and corporate tax Brazil. Financial-sector rates, incentives, reorganisations and multinational minimum tax need separate advice."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/brazil-corporate-tax"
  jurisdiction: "BR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Brazil corporate income tax: IRPJ and CSLL in 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference.** Ordinary IRPJ is 15% plus 10% on the base above BRL 20,000 multiplied by the months in the assessment period. Ordinary CSLL is 9% on its separately reconciled base. Lucro presumido percentages are not tax rates. From 2026 their increase applies to the excess revenue slice, with IRPJ beginning in the first quarter and CSLL in the second. Sources and conditions are in the table below.

**Required inputs.** Establish the company's activities, prior-year total revenue, actual adjusted profits and separate loss balances, existing regime election, domestic/foreign receipts and quarter before computing. Currency: Brazilian reais (BRL); authority: Receita Federal do Brasil (RFB); year here means income earned in calendar 2026, rather than a return filed during 2026 for 2025.

## Who this applies to

Ordinary Brazilian companies and equivalent enterprises subject to IRPJ and CSLL outside Simples Nacional. Determine whether lucro real is mandatory before comparing regimes. Under [Lei 9.718/1998 arts. 13-14](https://www.planalto.gov.br/ccivil_03/leis/l9718.htm#art13), lucro presumido is available only within the prior-year revenue ceiling and where no mandatory lucro real category applies. Mandatory categories include excess revenue, the specified financial businesses, foreign profits/income/capital gains, specified exemption/reduction incentives, an existing annual-estimate election, factoring and securitisation. A domestic export receipt is not automatically a foreign subsidiary profit; classify it before using that boundary.

Read [br-simples-nacional](br-simples-nacional.md) for the separate simplified regime, [brazil-transfer-pricing](brazil-transfer-pricing.md) for controlled transactions, and [br-income-tax](br-income-tax.md) for individuals. Check their year and source dates before reusing figures while the pack is being updated.

**Out of scope:** banks, insurers, payment institutions and other special CSLL categories; exempt/non-profit entities; rural and real-estate special rules; cooperatives; tax incentives; detailed depreciation asset schedules; mergers, liquidation and tax succession; foreign controlled-company profit attribution; Pillar Two additional CSLL; treaty-specific relief and tax planning through juros sobre capital próprio. These need their own statutory analysis, not an assumed ordinary 34% combined charge.

## Rates, bands and thresholds

Each quotation is the short original wording of the cited provision. The computations below derive period amounts from these figures.

| Item and conditions | Rate or amount, 2026 | Official source and exact words |
|---|---|---|
| Ordinary IRPJ on real, presumed or arbitrated taxable profit | 15% | [Lei 9.249 art. 3](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm#art3): "A alíquota do imposto de renda das pessoas jurídicas é de quinze por cento" |
| IRPJ surcharge on the portion above the assessment-period allowance, with no deduction against the surcharge | 10%; allowance BRL 20,000 × months, hence BRL 60,000 for a full quarter | [Lei 9.249 art. 3 §§1,4](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm#art3): "multiplicação de R$ 20.000,00"; "à alíquota de dez por cento" |
| Ordinary CSLL, excluding special financial categories | 9% on the CSLL base | [Lei 7.689 art. 3 III](https://www.planalto.gov.br/ccivil_03/leis/l7689.htm#art3): "9% (nove por cento), no caso das demais pessoas jurídicas" |
| Lucro presumido eligibility, subject to mandatory lucro real exclusions | Prior-year total revenue at most BRL 78,000,000; BRL 6,500,000 × active months if fewer than 12 | [Lei 9.718 art. 13](https://www.planalto.gov.br/ccivil_03/leis/l9718.htm#art13): "igual ou inferior a R$ 78.000.000,00"; "R$ 6.500.000,00" |
| Ordinary goods/trading IRPJ presumptive percentage; special activities require classification | 8% of relevant gross revenue | [Lei 9.249 art. 15 caput](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm#art15): "percentual de 8% (oito por cento)" |
| Fuel resale IRPJ presumption, for the statutory fuels | 1.6% | [Lei 9.249 art. 15 §1 I](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm#art15): "um inteiro e seis décimos por cento" |
| Non-cargo transport IRPJ presumption; cargo follows the ordinary percentage | 16% | [Lei 9.249 art. 15 §1 II a](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm#art15): "dezesseis por cento"; "exceto o de carga" |
| General services, business intermediation and property/rights administration or letting IRPJ presumption | 32%; qualifying hospital/diagnostic services have an exception requiring business form and Anvisa compliance | [Lei 9.249 art. 15 §1 III](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm#art15): "trinta e dois por cento"; "atenda às normas da Agência Nacional de Vigilância Sanitária" |
| Companies exclusively providing eligible general services; excludes hospital, transport and legally regulated professional-service companies | 16% IRPJ presumption if annual gross revenue is at most BRL 120,000; not a reduction in the CSLL percentage | [Lei 9.250 art. 40 and sole paragraph](https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html): "receita bruta anual seja de até R$ 120.000,00"; "percentual de 16%" |
| Ordinary CSLL presumption | 12%; activities under art. 15 §1 III use 32% instead | [Lei 9.249 art. 20 I,III](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm#art20): "32% (trinta e dois por cento)"; "12% (doze por cento) para as demais receitas brutas" |
| 2026 presumption increase, only on excess relevant gross revenue; allocation and timing below | Increase percentage by 10% of itself, not 10 percentage points; annual reference BRL 5,000,000 | [LC 224 art. 4 §4 VII, §5](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp224.htm#art4): "acréscimo de 10%"; "que exceda o valor de R$ 5.000.000,00" |
| Quarterly excess-revenue test and 2026 CSLL transition | BRL 1,250,000 per quarter; IRPJ from Q1, CSLL from Q2; CSLL 2026 annual reference BRL 3,750,000 | [RFB V5 Q11-14](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/beneficios-fiscais/perguntas-e-respostas-reducao-dos-incentivos-e-beneficios-tributarios-v5-final.pdf/@@download/file): "R$ 1.250.000,00 por trimestre"; "a partir do segundo trimestre de 2026 para a CSLL" |
| Ordinary brought-forward fiscal loss and negative CSLL base offset, separate pools with documentary support | Maximum 30% of the respective positive adjusted period base | [Lei 9.065 arts. 15-16](https://www.planalto.gov.br/ccivil_03/leis/l9065.htm#art15): "trinta por cento do referido lucro líquido ajustado" |
| Quarterly tax instalments, if elected | Up to 3; each at least BRL 1,000; tax below BRL 2,000 paid once | [Lei 9.430 art. 5 §§1-3](https://www.planalto.gov.br/ccivil_03/leis/l9430.htm#art5): "até três quotas mensais"; "inferior a R$ 1.000,00"; "inferior a R$ 2.000,00" |
| Late federal tax payment | 0.33% per day, maximum 20%, plus statutory interest | [Lei 9.430 art. 61](https://www.planalto.gov.br/ccivil_03/leis/l9430.htm#art61): "trinta e três centésimos por cento, por dia de atraso"; "limitado a vinte por cento" |

## The base

### Lucro real

Start from the accounts and build separate reconciliations for IRPJ and CSLL. Costs and operating expenses need evidence of the business activity: [Lei 4.506 art. 47](https://www.planalto.gov.br/ccivil_03/leis/l4506.htm#art47) describes expenses "necessárias à atividade da emprêsa" and usual/normal for the activity. A booked item is not automatically deductible. [Lei 9.249 art. 13](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm#art13) restricts provisions, non-business rent/depreciation and asset costs, owners' meals, non-compulsory contributions, donations and gifts, with its stated employee-benefit and donation exceptions. Test the particular exception before adding back the entire expense.

Reconcile accounting versus tax depreciation, exempt/excluded receipts, foreign results and transfer-pricing adjustments. Retain the timing difference and reversal schedule; a temporary addition is not necessarily a permanent loss. Keep IRPJ fiscal losses apart from negative CSLL bases. Under Lei 9.065 arts. 15-16, brought-forward balances reduce each positive adjusted base by at most 30%, and the taxpayer must retain the supporting books/documents. Do not offset a CSLL balance against IRPJ or presume that every loss survives a reorganisation.

Calculate `IRPJ = base × 15% + max(0, base - 20,000 × months) × 10%`; calculate ordinary CSLL separately at 9%. This formula assumes no incentive, special base or special entity. A quarterly loss does not automatically cancel another quarter's final liability. The annual lucro real option instead has monthly estimates and an annual reconciliation ([Lei 9.430 arts. 1-3](https://www.planalto.gov.br/ccivil_03/leis/l9430.htm#art1)).

### Lucro presumido and the 2026 increase

1. Check eligibility under Lei 9.718 arts. 13-14 and the annual election. Apply the right percentage to each activity's relevant gross revenue, net of statutory returns, cancelled sales and unconditional discounts. Under [Lei 9.430 art. 25](https://www.planalto.gov.br/ccivil_03/leis/l9430.htm#art25), capital gains, financial returns and other fully taxable receipts enter in full, rather than at the sales presumption percentage. Maintain the separate CSLL calculation under Lei 9.249 art. 20.
2. For 2026 IRPJ, split the quarter's relevant gross revenue at BRL 1,250,000. Apply the normal percentage below it and 1.10 times that percentage above it: trading 8% becomes 8.8%, services 32% becomes 35.2%. This is not a change in the 15% IRPJ tax rate.
3. For CSLL, Q1 retains normal presumption. Apply the increase from Q2; the 2026 annual reference for the affected Q2-Q4 period is BRL 3,750,000. Keep the quarterly tests and any later-period adjustment tied to the statutory annual reference. Do not wait until cash receipts first cross BRL 5 million before testing a quarter.
4. With mixed activities, allocate the quarter's allowance in proportion to each activity's relevant revenue. RFB Q14's split of BRL 1,440,000 trading and BRL 360,000 services gives BRL 1,000,000 and BRL 250,000 allowance respectively. Apply the higher percentages to the remaining revenue of each activity. Q11.1 excludes financial receipts/capital gains included directly in full from this allowance test; that does not exempt those receipts from tax.
5. Calculate IRPJ and its surcharge on the resulting base; calculate CSLL on its own resulting base. Actual operating costs and accounting losses do not substitute for the statutory presumption. Compare regimes over the full expected year before making the election.

Authority for steps 2-4: [LC 224 art. 4 §§4-5 and art. 14](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp224.htm#art4), and RFB V5 Q11, 11.1, 12-14, pp. 10-12, linked in the table.

**Small-service exception.** Only companies exclusively providing eligible general services qualify, as [IN RFB 1.700/2017 art. 215 §10](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=81268) specifies: "exclusivamente prestadoras de serviços em geral". Before using the general 32% IRPJ percentage, test the 16% exception in the rates table. It excludes hospital, transport and legally regulated professional-service companies; it is not an across-the-board small-company rate. Under [RIR/2018 art. 592 §§3-6](https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html), if accumulated annual gross revenue later exceeds BRL 120,000, recompute the deferred IRPJ difference for each elapsed quarter and pay that difference by the last business day of the month following the quarter in which the limit was exceeded. The regulation says "a diferença deverá ser paga até o último dia útil do mês subsequente ao do trimestre em que ocorreu o excesso". Keep the annual revenue monitor with the quarterly workpaper. This exception does not reduce ordinary service CSLL presumption to 16%.

## Deadlines and filing

Under [Lei 9.430 arts. 1,5,6](https://www.planalto.gov.br/ccivil_03/leis/l9430.htm#art1), ordinary quarters close on 31 March, 30 June, 30 September and 31 December. A single quarterly payment is due by the last business day of the following month. The optional equal, successive instalments fall on the last business days of the following three months, subject to the minimums above. Later instalments carry SELIC from the statutory start and 1% in the payment month; a three-instalment election is not interest-free.

For annual lucro real, monthly estimates are due by the last business day of the following month. A positive annual balance is payable by the last business day of March of the following year with the art. 6 interest adjustment. December's estimate remains due in January; it does not move to March. A negative annual balance follows the refund/compensation procedure, not a negative DARF.

**Operational handoff:**

1. Close and reconcile the ledger, revenue by activity, adjustments, separate losses, prior estimates and tax withheld. Record the regime election and period length.
2. In Receita's DCTFWeb service, open the **Módulo de Inclusão de Tributos (MIT)** for IRPJ and CSLL not received from another digital return. Enter the assessment period, tax identity, calculated debits and any applicable suspension. Validate, save and close MIT. Closure sends the assessment to DCTFWeb "para compor a declaração em andamento", as the [official MIT manual, sections 4-7](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/DCTFWeb/arquivos/manual-mit-1-0-14-02.pdf) explains. In DCTFWeb, review the consolidated debits, link applicable suspensions/credits/payments under its rules, then sign and transmit the ordinary declaration. MIT closure alone is not DCTFWeb delivery. The [official service](https://www.gov.br/pt-br/servicos/declarar-debitos-e-creditos-tributarios-federais) permits online entry or import. Save the DCTFWeb transmission receipt and DARF; reconcile payment to the tax account. Ordinary monthly DCTFWeb delivery is the last business day of the following month; this does not postpone an earlier payment deadline.
3. Prepare **Escrituração Contábil Fiscal (ECF)** in SPED using the layout for the actual calendar year and chosen regime, reconcile the IRPJ/CSLL calculations and loss controls to the books and MIT, validate, digitally sign and transmit. Save the receipt and validation report. [RFB's ECF FAQ](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/sped/ecf/ecf/qual-e-a-data-limite-regular) sets the ordinary deadline as the last business day of July of the following year. Thus 2026 activity is ordinarily reported in 2027, subject to later amendments; a 2026 filing deadline for 2025 is a different obligation.
4. For merger, division, incorporation or closure, apply the event-period and special ECF deadlines instead of copying the ordinary calendar. The FAQ distinguishes January-April events from May-December events. Stop if the correct event layout or taxpayer authority to sign is missing.

## Penalties and interest

[Lei 9.430 art. 61](https://www.planalto.gov.br/ccivil_03/leis/l9430.htm#art61) imposes the daily late-payment penalty in the table from the day following the deadline through payment, plus SELIC accumulated from the month after the due month through the month before payment and 1% in the payment month. Fetch the actual monthly SELIC factors; do not substitute a remembered annual rate.

For assessed underpayment, [art. 44 I](https://www.planalto.gov.br/ccivil_03/leis/l9430.htm#art44) specifies the ordinary 75% assessment penalty. Its qualified-fraud and repeat-offence rules require their own facts; an ordinary error is not automatically fraud. Late/inaccurate ECF and DCTFWeb returns also have distinct return penalties. Their current regime-specific amounts and reduction conditions are not confirmed here; use the applicable official notice and statute before quoting a figure. Paying tax does not by itself cure an unfiled declaration.

## Cross-border points

[Lei 9.249 art. 25](https://www.planalto.gov.br/ccivil_03/leis/l9249.htm#art25) brings foreign profits, income and capital gains into the lucro real analysis, and art. 26 provides the foreign-income-tax credit with its Brazilian-tax limit and evidence conditions. Foreign income can also remove lucro presumido eligibility under Lei 9.718 art. 14. Controlled dealings require the separate transfer-pricing computation; customs values and IRPJ arm's-length values are different tests.

**Dividends changed in 2026.** Under [Lei 15.270 arts. 2-3,8](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm#art3), Lei 9.249 art. 10 §4 imposes 10% IRRF on outbound profits/dividends without a BRL 50,000 allowance, subject to §5. Section 5 II excludes payments to foreign governments with reciprocal treatment, statutory sovereign funds and foreign entities principally administering pension benefits as defined by regulation. Verify the recipient's qualification before applying an exemption. For a resident individual, Lei 9.250 art. 6-A instead uses amounts exceeding BRL 50,000 from the same company to that individual in one month and taxes the whole monthly amount. Aggregate repeated distributions. The statutory old-profit transition requires results through 2025, distribution approval by 31 December 2025, civil/company-law enforceability and payment, credit, employment or delivery on the originally approved terms. Check any applicable court order affecting those conditions; retained old profits are not automatically grandfathered. The new minimum-income-tax and foreign-beneficiary credit calculations are separate from the company's ordinary IRPJ/CSLL.

CBS/IBS is a consumption-tax transition, not a replacement for corporate income tax. [LC 214 arts. 343,346,348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm#art343) contains the 2026 test-year rules and conditional payment dispensation. Do not replace IRPJ or CSLL with a projected future VAT rate.

## Two worked examples that recompute

### 1. Ordinary quarterly lucro real with separate losses

Assume an ordinary company, a full quarter, identical positive adjusted IRPJ/CSLL bases before losses of BRL 400,000 and BRL 200,000 documented losses in each separate pool. Each offset is limited to BRL 120,000, leaving BRL 280,000 taxable. IRPJ is BRL 42,000 plus BRL 22,000 surcharge; CSLL is BRL 25,200. Combined tax before credits is BRL 89,200. Each remaining loss pool is BRL 80,000. These are assumed inputs, not thresholds.

```oa-check
name: Ordinary quarter with separate loss pools
inputs:
  adjusted: 400000
  irpj_loss: 200000
  csll_loss: 200000
  months: 3
steps:
  irpj_offset: min(irpj_loss, adjusted * 0.30)
  csll_offset: min(csll_loss, adjusted * 0.30)
  irpj_base: adjusted - irpj_offset
  csll_base: adjusted - csll_offset
  irpj: irpj_base * 0.15 + max(0, irpj_base - 20000 * months) * 0.10
  csll: csll_base * 0.09
  total: irpj + csll
  irpj_remaining: irpj_loss - irpj_offset
expected:
  irpj_offset: 120000
  irpj: 64000
  csll: 25200
  total: 89200
  irpj_remaining: 80000
```

### 2. Decision: eligible trading company, first quarter of 2026

Assume prior-year eligibility, no mandatory lucro real category, BRL 1,500,000 sales, no other taxable receipts, and BRL 100,000 adjusted real profit for each tax, no losses or credits. Compare before the annual election and assume this quarter's pattern repeats only if documented in the forecast.

Presumed IRPJ base is BRL 1,250,000 × 8% plus BRL 250,000 × 8.8% = BRL 122,000. IRPJ is BRL 24,500. Q1 CSLL is still 12% of all sales × 9% = BRL 16,200. Total BRL 40,700. Lucro real gives IRPJ BRL 19,000 and CSLL BRL 9,000, total BRL 28,000. The actual-profit route is BRL 12,700 lower on these facts. This comparison excludes PIS/Cofins, compliance costs, future quarters and distribution taxes, so it is not a full-regime election recommendation. Q2 CSLL cannot reuse Q1's unenhanced base.

```oa-check
name: Q1 2026 trading regime decision
inputs:
  revenue: 1500000
  allowance: 1250000
  real_profit: 100000
steps:
  presumed_base: min(revenue, allowance) * 0.08 + max(0, revenue - allowance) * 0.088
  presumed_irpj: presumed_base * 0.15 + max(0, presumed_base - 60000) * 0.10
  presumed_csll_q1: revenue * 0.12 * 0.09
  presumed_total: presumed_irpj + presumed_csll_q1
  real_irpj: real_profit * 0.15 + max(0, real_profit - 60000) * 0.10
  real_total: real_irpj + real_profit * 0.09
  difference: presumed_total - real_total
expected:
  presumed_base: 122000
  presumed_irpj: 24500
  presumed_csll_q1: 16200
  presumed_total: 40700
  real_total: 28000
  difference: 12700
```

## Ask the client first

1. What activities and legal form does the CNPJ conduct, and is it in Simples or a special financial/other regime?
2. What was total prior-year revenue, over how many active months, and what election has already been made?
3. What revenue belongs to each activity this quarter, and what capital gains, financial receipts or foreign results are separate?
4. What are the adjusted profits, IRPJ losses and negative CSLL bases, supported separately by books and prior returns?
5. What estimates, credits, withholding and payments exist, and is there a merger, division or closure?
6. Who receives dividends, in what month, from which profit year and approval, and does any court order affect the transition?

## Sources

Read dates below record reading the listed provisions and neighbouring exceptions, not merely loading a page. Planalto text was read in the normal browser after direct-fetch failure. The RFB PDF was downloaded once and extracted to a source cache outside Git.

| Source and parts read | Official URL | Read on |
|---|---|---|
| Lei 9.249/1995 arts. 3,9-10,13,15,20,25-26; ordinary bases, expense exclusions, foreign results and dividend amendments | https://www.planalto.gov.br/ccivil_03/leis/l9249.htm | 2026-11-11 |
| Lei 7.689/1988 arts. 2-3; CSLL base, ordinary versus special entity rates | https://www.planalto.gov.br/ccivil_03/leis/l7689.htm | 2026-11-11 |
| Lei 9.718/1998 arts. 13-14; eligibility, annual election and mandatory lucro real categories | https://www.planalto.gov.br/ccivil_03/leis/l9718.htm | 2026-11-11 |
| Lei 9.250/1995 art. 40 and sole paragraph; small-service-provider IRPJ presumption and excluded activities | https://www2.camara.leg.br/legin/fed/lei/1995/lei-9250-26-dezembro-1995-362566-normaatualizada-pl.html | 2026-11-11 |
| Decreto 9.580/2018, RIR art. 592 §§1-6; activity exceptions and quarterly small-service catch-up | https://www2.camara.leg.br/legin/fed/decret/2018/decreto-9580-22-novembro-2018-787360-normaatualizada-pe.html | 2026-11-11 |
| LC 224/2025 art. 4 §§1-9 and art. 14; scope, presumption increase and effective dates | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp224.htm | 2026-11-11 |
| RFB reduction-of-benefits Q&A V5, pp. 5-14, especially Q6 and Q11-14; quarterly allocation, dates and fully included receipts | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/beneficios-fiscais/perguntas-e-respostas-reducao-dos-incentivos-e-beneficios-tributarios-v5-final.pdf/@@download/file | 2026-11-11 |
| Lei 9.065/1995 arts. 15-16; separate loss offsets and book/document conditions | https://www.planalto.gov.br/ccivil_03/leis/l9065.htm | 2026-11-11 |
| Lei 4.506/1964 arts. 47-49; necessary/usual expenses and capital versus repair boundary | https://www.planalto.gov.br/ccivil_03/leis/l4506.htm | 2026-11-11 |
| Lei 9.430/1996 arts. 1-6,25-26,44,61; periods, payments, presumed base and penalties | https://www.planalto.gov.br/ccivil_03/leis/l9430.htm | 2026-11-11 |
| RFB ECF deadline FAQ; normal and event deadlines | https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/sped/ecf/ecf/qual-e-a-data-limite-regular | 2026-11-11 |
| RFB federal debit/credit declaration service; MIT entry, DCTFWeb consolidation and deadline | https://www.gov.br/pt-br/servicos/declarar-debitos-e-creditos-tributarios-federais | 2026-11-11 |
| IN RFB 1.700/2017 art. 215 §§10-12; exclusive-services condition, annual revenue and quarterly catch-up | https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=81268 | 2026-11-11 |
| RFB MIT manual, sections 4-7 and 8.3; debit/suspension entry, validation, closure and downstream DCTFWeb handoff | https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/DCTFWeb/arquivos/manual-mit-1-0-14-02.pdf | 2026-11-11 |
| Lei 15.270/2025 arts. 2-3,8; resident/outbound distributions, transition and commencement | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm | 2026-11-11 |
| LC 214/2025 arts. 343-348, including LC 227/2026 additions; consumption-tax transition | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm | 2026-11-11 |

Not yet confirmed: calendar-2026 ECF layout record/field numbers; current regime-specific ECF/DCTFWeb return-penalty amounts and reductions; case-specific court orders affecting pre-2026 dividend approval dates; detailed operational foreign-beneficiary credit procedure. These figures/procedures are omitted, not inferred. The specialist regimes listed out of scope require separate source work.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `brazil-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/brazil-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
