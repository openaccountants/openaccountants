---
name: brazil-transfer-pricing
description: "EN: Use this skill whenever asked about Brazil transfer pricing rules, documentation requirements, or preços de transferência compliance. Trigger on phrases like \"transfer pricing Brazil\", \"Brazilian TP documentation\", \"preços de transferência\", \"master file Brazil\", \"local file Brazil\", \"CbCR Brazil\", \"APA Brazil\", \"Law 14.596/2023\", \"IN RFB 2161\", \"arm's length Brazil\", \"ECF\", or any question about intercompany pricing for Brazilian entities. PT-BR: Use esta skill sempre que for solicitada análise sobre as regras de preços de transferência no Brasil, requisitos de documentação ou conformidade em preços de transferência. Acione com expressões como \"preços de transferência Brasil\", \"documentação de TP brasileira\", \"preços de transferência\", \"master file Brasil\", \"local file Brasil\", \"CbCR Brasil\", \"APA Brasil\", \"Lei 14.596/2023\", \"IN RFB 2161\", \"arm's length Brasil\", \"ECF\", ou qualquer questão sobre precificação intercompany para entidades brasileiras."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/brazil-transfer-pricing"
  jurisdiction: "BR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Brazil transfer pricing: preços de transferência in 2026 v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference.** Brazil's arm's-length regime is mandatory from 2024. For 2026 documentation, measure 2025 controlled transactions before TP adjustments: below BRL 15 million the Local and Global Files are dispensed with, BRL 15 million to below BRL 500 million requires a simplified Local File plus Global File, and BRL 500 million or more requires full Local File plus Global File. Dispensation from those files does not exempt any transaction from arm's-length pricing, other ECF information, underlying evidence or commodity registration. See the source-linked conditions below.

**Required inputs:** Brazilian taxpayer/entity and tax year; full related-party and favoured-regime map; prior-year and current-year transaction totals before adjustments; contracts and functional/risk evidence; comparable prices/margins; group ultimate parent and consolidated revenue. Authority: Receita Federal do Brasil (RFB); currency: Brazilian reais (BRL). Calendar 2026 income is ordinarily documented/returned in 2027; a 2026 filing for 2025 is different.

## Who this applies to

[Lei 14.596/2023 arts. 1-4](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art1) governs IRPJ and CSLL for Brazilian legal persons' controlled commercial/financial relations with related parties abroad. Relatedness turns on direct/indirect influence and the statutory control, common-control, family and other tests, not simply whether a group labels an invoice intercompany. Article 40 extends the relevant rules to the Lei 9.430 arts. 24/24-A favoured-tax-country and privileged-regime cases even where the counterparty is unrelated. Check the current statutory/list definitions; do not restrict the transaction inventory to shareholdings.

The old fixed-margin regime was replaced from 1 January 2024; an irrevocable early election was available for 2023 (Lei 14.596 arts. 45-47). The prior PIC/PRL/CPL and export-margin/commodity labels are relevant when reviewing earlier periods, not substitute 2026 methods. A historical PRL or CPL 20% does not supply a current arm's-length margin.

The OECD guidelines are subsidiary only within [IN RFB 2.161/2023 art. 1 §4](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): later OECD changes require express RFB approval and cannot override Brazilian law/regulation. The old claim that Brazil joined the OECD in January 2024 is incorrect: the [OECD's Brazil page](https://www.oecd.org/en/countries/brazil.html) describes it as an accession candidate and non-member. Institutional status is not what makes the Brazilian statute apply.

**Out of scope:** full economic valuation of hard-to-value intangibles, cash pools/guarantees, restructurings and complex financing; detailed CbCR entity-by-entity preparation; treaty-specific MAP/APA administration; customs valuation; consumption-tax computations. These still belong in the transaction inventory and specialist handoff. Hiring an external consultant does not transfer the taxpayer's statutory documentation duty under art. 34 to that consultant.

## Rates, bands and thresholds

| Item and conditions | Amount/rule in 2026 | Official article URL and exact words |
|---|---|---|
| Mandatory new regime; 2023 early election separate | From 1 January 2024 | [Lei 14.596 art. 47](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art47): "entra em vigor em 1º de janeiro de 2024" |
| Local/Global File dispensation, prior-calendar-year controlled total before adjustments | Below BRL 15,000,000; underlying TP obligations remain | [IN 2.161 art. 57 III, §§1,3](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "menor que R$ 15.000.000,00"; "O Arquivo Global será dispensado" |
| Simplified Local File plus Global File, same measuring rule | At least BRL 15,000,000 and below BRL 500,000,000 | [IN 2.161 art. 57 II](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "maior ou igual a R$ 15.000.000,00"; "menor que R$ 500.000.000,00" |
| Full Local File plus Global File, same measuring rule | At least BRL 500,000,000 | [IN 2.161 art. 57 I](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "maior ou igual a R$ 500.000.000,00" |
| Local File ordinary goods/service categories, largest transactions; commodities and specified other categories fully covered | 80% of each listed category's value; 100% of commodities, rights, restructurings, cost sharing, finance and intangibles | [IN 2.161 art. 57 §2](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "representem 80%"; "commodities, que deverão ser informadas na sua totalidade"; "a totalidade das transações" |
| Optional low-value-service gross markup on all direct/indirect costs, with art. 53 eligibility and benefit tests below | Brazilian provider: at least 5%; related foreign provider: at most 5% | [IN 2.161 art. 53 I-II](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "no mínimo 5%"; "no máximo 5%" |
| Global File supply-chain description | Five largest products/services and others above 5% of group gross revenue | [IN 2.161 art. 58 II c](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "5 (cinco) maiores"; "mais de 5%" |
| Country-by-country reporting dispensation, prior fiscal year consolidated revenue; Brazilian ultimate parent | Below BRL 2,260,000,000, not BRL 2.4 billion; other filing/notification conditions still apply | [IN RFB 1.681/2016 art. 4 I](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=79444): "R$ 2.260.000.000,00" |
| CbCR foreign ultimate parent threshold | EUR 750,000,000 or equivalent converted using 31 January 2015 rate into ultimate parent's local currency | [IN 1.681 art. 4 II](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=79444): "€ 750.000.000,00"; "cotação de 31 de janeiro de 2015" |
| Local/Global File delivery | Within 3 months after the relevant ECF transmission deadline, through digital process | [IN 2.161 art. 56](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "em até 3 (três) meses após o prazo assinalado para a transmissão da ECF" |
| Current commodity-contract registration, including re-negotiation | By the tenth day of the month following contract conclusion, subject to art. 64; historical 2025 transition not a 2026 extension | [IN 2.161 art. 64, current IN 2.249/2025 wording](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "até o décimo dia do mês subsequente ao de a celebração do contrato" |
| Local/Global late filing | 0.2% per calendar month/fraction of relevant-period taxpayer gross revenue | [IN 2.161 art. 66 I a](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "0,2%"; "por mês-calendário ou fração" |
| Local/Global submission failing requirements | 3% of relevant-period taxpayer gross revenue | [IN 2.161 art. 66 I b](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "3% (três por cento)" |
| Inaccurate/incomplete/omitted Global File information, subject to formal/immaterial error exception | 0.2% of prior-year multinational consolidated revenue | [IN 2.161 art. 66 II, §§4-5](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "0,2%"; "receita consolidada do grupo multinacional do ano anterior" |
| Failure to produce requested information/obstruction in audit | 5% of corresponding transaction value as priced by the authority | [IN 2.161 art. 66 III](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "5% (cinco por cento) sobre o valor da transação correspondente" |
| Article 66 documentation penalties, including the specified maximum fallback | Minimum BRL 20,000; maximum BRL 5,000,000 | [IN 2.161 art. 66 §§1-2](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): "valor mínimo de R$ 20.000,00"; "máximo de R$ 5.000.000,00" |
| Statutory specific-consultation validity, subject to implementing process and approval | Up to 4 years, extendable by 2; not an automatic current APA offer | [Lei 14.596 art. 38 §3](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art38): "validade de até 4 (quatro) anos"; "prorrogada por 2 (dois) anos" |

## The base

### Delineate, compare and select the method

Under [Lei 14.596 arts. 2,5-11](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art2), use the actual transaction, functions performed, assets used, risks controlled and financially borne, contractual terms and economic circumstances. Conduct can override a paper contract. Document both parties' contributions and why transactions are compared separately or together. Ownership of an intangible alone does not allocate all returns to its legal owner; arts. 19-22 address actual development, enhancement, maintenance, protection and exploitation functions and risk/control.

The five named methods are **PIC/CUP**, **PRL/resale minus**, **MCL/cost plus**, **MLT/TNMM** and **MDL/profit split**, in art. 11 I-V. An alternative under VI requires reliable justification where the named methods cannot apply or do not give reliable results. Select the most appropriate method by reliable data and comparability; it is wrong to claim there is no statutory preference. Article 11 §2 regards PIC as most appropriate where reliable independent prices exist unless another method is demonstrably more appropriate. Article 13 has the commodity-specific PIC rule, with comparability adjustments and the same better-method qualification.

If a one-sided method needs a tested party, art. 15 selects the party for which the method is most appropriately applied and data most reliable; document both parties' functions/assets/risks. Under art. 16, use the appropriate comparable range. Use the interquartile range where comparability uncertainties cannot be precisely identified or quantified and adjusted. Use the full range only where the uncontrolled transactions have equivalent comparability and no such uncertainty (art. 16 §2). An indicator within the appropriate range requires no adjustment (§3); where the controlled indicator is outside the appropriate range, use the median for the statutory adjustment. Do not manufacture a fixed margin or label a group policy percentage a safe harbour.

### Adjustments and documentation are separate jobs

[Lei 14.596 art. 18](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art18) requires spontaneous/compensating adjustments where non-arm's-length terms understate the Brazilian tax base. A primary authority adjustment is separate. Downward adjustments/increased losses are restricted; the regulated compensating-adjustment and treaty dispute-resolution exceptions must actually be satisfied.

[IN 2.161 arts. 48-50](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782) requires the relevant year-end Brazilian tax-base adjustment even for quarterly taxpayers, with event-date rules for merger/division/closure; it is not a monthly annual-estimate-base adjustment. A qualifying compensating adjustment needs permanent symmetric accounting, debit/credit or commercial/tax documents and the specified confirmations/counterparty conditions. Article 50 permits completion by ECF delivery where permanently booked in the transaction year's accounts; do not infer that every unrecorded late journal or unilateral downward correction qualifies. Retain the special upward-adjustment exceptions to some formal conditions.

**Services:** [arts. 23-24](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art23) require a reasonable expected economic/commercial benefit of a kind an independent business would pay for or perform itself. Shareholder activities and duplicative services generally do not meet the benefit test unless the stated additional-benefit exception applies. Incidental group benefits are not separately chargeable services. For cost plus, include related service costs, use direct charging where identifiable and a justified allocation where they cannot reasonably be individualised. Under art. 24 §§4-6, do not mark up passed-through costs of activities/acquisitions from other parties where the provider performs no significant functions, considering assets and economically significant risks. An arm's-length markup can apply only to its own costs of performing the relevant functions in that case. The same cost discipline applies to cost-based MLT. This does not make all reimbursed costs markup-free.

**Optional low-value services:** [IN 2.161 art. 53 I-II, §§1-6](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782) provides a directional simplification: a Brazilian service provider must earn at least 5% gross markup on all direct and indirect transaction costs; a related foreign provider may earn at most 5%. Eligibility requires support services outside the related party's or the group's core activities, no unique valuable intangibles or contribution to their creation, no assumption/control or creation of economically significant risk, and no significant contribution to group value, core capabilities or business success. Services also supplied by the group to unrelated parties do not qualify. Exclusions are core business, R&D except qualifying low-value IT, manufacturing/production, purchasing production inputs, sales/marketing/distribution, financial transactions, natural resources, insurance/reinsurance, senior management except management of qualifying services, and international transport, asset letting or chartering. Allocate costs in proportion to actual or expected benefits where allocation is needed. Deductibility still requires the reasonable expected economic/commercial benefit for which an independent party would pay or act itself. This is not a universal fixed 5% safe harbour.

**Files:** Global File describes group structure, value chain, intangibles, financing, restructurings and consolidated financial/tax context (IN arts. 55,58). Full Local File covers the business, competitors, transactions, functions, methods, comparables, accounting reconciliation and specialised transaction material (arts. 59-60). The simplified version still requires entities, transaction values, methods, comparables/ranges, selection reasons and adjustments (art. 61). It is not a zero-documentation exemption. Article 57's largest-transaction selection does not exempt the remaining controlled transactions from law or evidence. If a third-party technical study is submitted, art. 59 IV(m) requires the preparer's declaration of responsibility for its information and techniques. That requirement does not transfer the taxpayer's own documentation or tax duties to the consultant.

**Language and evidence:** IN art. 62 requires contemporaneously organised support. Foreign-language supporting documents need simple translation; English/Spanish support requires translation only on request, and the authority can request a sworn translation for procedure. Article 63 allows the authority to require reproduction of comparable-database searches on the taxpayer's premises. Separately, art. 58 §§1-2 expressly permits a foreign-language Global File with simple Portuguese translation; for an English or Spanish Global File, translation is required only on request. The authority may require a sworn translation for procedural purposes. The Local File body's full filing-language rule remains unconfirmed; do not infer it solely from rules for supporting records.

### CbCR is distinct from Local/Global Files

[IN 1.681 arts. 3-9](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=79444) generally makes a Brazilian ultimate parent the reporting entity, with secondary-filing triggers where a foreign parent's jurisdiction does not require reporting, has no effective competent-authority arrangement, or has notified systemic failure. A qualifying surrogate-reporting arrangement can switch off secondary filing. Apply the actual conditions and obtain the entity notification even where the group's revenue is below the reporting threshold.

Report through ECF for the preceding fiscal year. The data include jurisdictional revenues, profits, income tax paid/accrued (including Brazilian CSLL), capital, accumulated earnings, employees and non-cash tangible assets, constituent entities/activities and explanations. Monetary data use one ultimate-parent currency and full group entities, not ownership-proportion netting. Text explanations use Portuguese, English or Spanish under art. 9 §3. CbCR informs risk assessment; it is not itself an arm's-length pricing method.

## Deadlines and filing

1. Determine the covered year and prior-year file thresholds. Assemble the transaction inventory, analysis and current-year adjustments contemporaneously, not after a file threshold is crossed. Reconcile values to the accounts and ECF.
2. ECF ordinarily falls on the last business day of July of the following year, according to [Receita's ECF FAQ](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/sped/ecf/ecf/qual-e-a-data-limite-regular). Use its event-specific deadline after merger, division, incorporation or closure. Populate the applicable ECF TP and CbCR records from the correct year's layout, validate/sign/transmit and retain the receipt. Current record/field numbers are not confirmed here.
3. Under IN art. 56, file the Global and Local Files through a digital process within three months of the applicable ECF deadline. This is measured from the deadline, not the taxpayer's early actual filing day. For 2026 activity this normally means 2027 filings, subject to later legal changes. The historical 2024 file deadline was the last business day of 2025, and an early-election 2023 file was due the last business day of 2024; these are not extensions for current work.
4. Use [Receita's official documentation service](https://www.gov.br/pt-br/servicos/entregar-documentacao-de-precos-de-transferencia): select area **Preços de Transferência** and service **Apresentar Documentação de Preços de Transferência relativas ao IRPJ e CSLL**. Open only one process for each calendar year, attach the required files, submit and save the protocol. Corrections/additions go into the same year's existing process; review status/documents under **Meus Processos**. Opening a process without attaching/submitting the files does not establish complete delivery.
5. For controlled commodity imports/exports, separately register the contract and any re-negotiated terms in the e-CAC RTC system by art. 64's deadline. The old idea that commodity rules are still merely being developed is stale. Registration includes the price-setting date/period and the prescribed contract information; a Local File or ECF does not replace RTC. Use the current official RTC layout, not a remembered file format.

## Penalties and interest

Apply the specific documentation penalties in the table, with their exact base, minimum, maximum and exceptions. The 0.2% consolidated-group-revenue information penalty is for the **Global File**, not automatically every inaccurate Local File or CbCR entry. If group revenue is not supplied/proved in the specified case, IN art. 66 §2 applies its maximum fallback. There is a primary-text cross-reference discrepancy: Lei 14.596 art. 35 §2 refers its missing/unproved-group-revenue maximum fallback to art. 35 I(c), the 3% failure-of-requirements penalty, while IN 2.161 art. 66 §2 refers to art. 66 II, the Global information penalty. The IN rule is reported here as written; obtain legal review of the actual assessment rather than assume the two cross-references agree. Formal errors/immaterial information under §§4-5 have the stated exception; immaterial means not compromising reliable arm's-length results.

CbCR's own penalties are in [IN 1.681 art. 11, as amended by IN 2.161](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=79444), including 0.2% per month/fraction of taxpayer gross revenue for late reporting, 5% of the corresponding transaction for requested-information failure/obstruction, and 0.2% of prior-year group consolidated revenue for inaccurate/incomplete/omitted information, with BRL 20,000 minimum/BRL 5 million maximum and specified exceptions. Do not use the repealed BRL 1,500 per-month CbCR rule as a universal ECF fine. ECF return penalties depend on their own governing regime and are not confirmed here.

An income-tax adjustment also requires IRPJ/CSLL, late-payment interest and any assessed penalty analysis. [Lei 9.430 arts. 44,61](https://www.planalto.gov.br/ccivil_03/leis/l9430.htm#art44) distinguishes the ordinary 75% assessment penalty from qualified intentional fraud (100%) and the statutory repeat case (150%, with its two-year test and conditions), rather than automatic 150% for any error. The daily late-payment penalty is 0.33% capped at 20%, plus actual SELIC and payment-month 1%. Do not combine overlapping penalties mechanically without checking the assessment provision.

Lei 14.596 art. 36 permits authorised correction during audit only on its cooperative/reasonable-effort and other stated conditions; it is not a taxpayer's unconditional entitlement to erase penalties by amending.

## Cross-border points

**Specific consultation/APA topic:** [Lei 14.596 art. 38](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art38) authorises RFB to institute a specific future-transaction methodology consultation and its admission rules. Statutory duration is in the table; critical-assumption/legal changes, false or omitted information and approved extensions matter. The earlier claim that operative APA regulations were in force from January 2025 has not been confirmed and must not be repeated. Current admission process, bilateral/multilateral availability and indexed payable fees are not supplied here. Article 39 separately implements results agreed under a relevant treaty dispute mechanism; a unilateral consultation is not automatic foreign corresponding relief.

**Related taxes:** TP adjustments affect IRPJ/CSLL. Separate thin-capitalisation rules in Lei 12.249 arts. 24-25 remain relevant to related-party financing, as Lei 14.596 art. 42 expressly recognises; arm's-length interest is not necessarily fully deductible. Customs valuation has a separate legal test. Imported intercompany services also need their consumption-tax analysis: [LC 214 arts. 343,346,348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm#art343) already provides the 2026 CBS/IBS test-year and conditional payment dispensation, so do not say cross-border consumption rules start only in 2027. TP compliance does not settle that separate liability.

**Minimum-tax topic:** multinational minimum-tax/additional-CSLL obligations require separate current-law research. They are not characterised as merely an ongoing discussion in this Guide. This referral preserves the old topic without inventing thresholds.

## Two worked examples that recompute

### 1. Comparable-price adjustment, no fixed margin

Assume a 2026 Brazilian importer buys 10,000 units from its related foreign supplier at BRL 120 each. Reliable fully comparable independent transactions support BRL 110 per unit; assume appropriate PIC selection, no remaining comparability adjustment and the expense otherwise deductible. Booked cost is BRL 1,200,000; arm's-length cost is BRL 1,100,000. The spontaneous addition to the relevant IRPJ/CSLL bases is BRL 100,000. Compute actual taxes with the company's own regime and loss/surcharge facts; this example does not assume a universal 34% marginal charge.

```oa-check
name: PIC import cost adjustment
inputs:
  units: 10000
  controlled_unit_price: 120
  comparable_unit_price: 110
steps:
  booked_cost: units * controlled_unit_price
  comparable_cost: units * comparable_unit_price
  addition: booked_cost - comparable_cost
expected:
  booked_cost: 1200000
  comparable_cost: 1100000
  addition: 100000
```

### 2. Documentation decision at the threshold

Assume 2025 controlled transactions before TP adjustments comprise BRL 8 million goods imports, BRL 4 million services and BRL 3 million royalties. Total BRL 15 million exactly: simplified Local File plus Global File is required for 2026, even if a later adjustment reduces the reported net amount. With the same facts except royalties of BRL 2,999,999, total is BRL 14,999,999: Local/Global delivery is dispensed with, but substantive TP, support, ECF and any RTC obligations remain. This is a classification decision, not permission to split one transaction artificially. CbCR has a different group-revenue test.

```oa-check
name: File-threshold classification
inputs:
  goods: 8000000
  services: 4000000
  royalties_equal: 3000000
  royalties_below: 2999999
steps:
  total_equal: goods + services + royalties_equal
  total_below: goods + services + royalties_below
  equal_minus_threshold: total_equal - 15000000
  below_minus_threshold: total_below - 15000000
expected:
  total_equal: 15000000
  total_below: 14999999
  equal_minus_threshold: 0
  below_minus_threshold: -1
```

## Ask the client first

1. Which Brazilian taxpayer and calendar year are covered, and is any special event or historical 2023 election relevant?
2. Who controls/influences each counterparty, and does a tax-favoured jurisdiction/regime bring unrelated dealings into scope?
3. What are prior-year and current-year controlled totals before adjustments by transaction class, including royalties, financing, restructurings and commodities?
4. What evidence establishes functions/assets/risks, actual conduct, benefits, costs, price-setting dates and reliable comparables?
5. Who is the ultimate parent, what is prior-year consolidated revenue/currency, and which entity files CbCR with what exchange/surrogate arrangement?
6. What ECF/digital processes/RTC filings and receipts exist, and are there audit notices, compensating adjustments or treaty disputes?

## Sources

Read scope is specified; statutes and Normas were read in the normal browser after direct-fetch issues. No secondary tax guide supplies a figure. The exact short original words in the table support its amounts; full articles and neighbouring exceptions were read.

| Official source and parts read | URL | Read on |
|---|---|---|
| Lei 14.596/2023 arts. 1-18,19-24,34-40,42,45-47; scope, methods, adjustments, services, documentation, consultation and commencement | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm | 2026-11-11 |
| IN RFB 2.161/2023 arts. 1-6,48-66; subsidiary guidelines, adjustment conditions, complete documentation/thresholds, RTC amendments and penalties | https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782 | 2026-11-11 |
| IN RFB 1.681/2016 arts. 3-11 including current amended penalty provisions; CbCR scope, threshold, filing, notifications and content | https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=79444 | 2026-11-11 |
| RFB documentation delivery service; process selection, one process per year, attachments/corrections and tracking | https://www.gov.br/pt-br/servicos/entregar-documentacao-de-precos-de-transferencia | 2026-11-11 |
| RFB ECF deadline FAQ, ordinary and event branches | https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/sped/ecf/ecf/qual-e-a-data-limite-regular | 2026-11-11 |
| Lei 9.430/1996 arts. 44,61, including qualification and repeat-offence paragraphs; assessment and payment penalties | https://www.planalto.gov.br/ccivil_03/leis/l9430.htm | 2026-11-11 |
| LC 214/2025 arts. 343-348; current test-year consumption-tax transition | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm | 2026-11-11 |
| OECD official Brazil institutional-status page; accession-candidate/non-member statement only | https://www.oecd.org/en/countries/brazil.html | 2026-11-11 |

Not yet confirmed: current operational specific-consultation/APA admission rules, unilateral/bilateral/multilateral availability and indexed payable fees (the old file's January-2025 availability assertion is not carried as fact); current full filing-language rules for the Local File body, distinct from the verified Global File and supporting-document rules; 2026 ECF TP/CbCR record/field numbers and regime-specific ECF late-return fine (old generic BRL 1,500/month claim not verified); full current RTC file layout; Pillar Two additional-CSLL computations and detailed thin-capitalisation ratios. These old topics are retained here as explicit omissions where not established, rather than guessed. Historical labels PCI, PCEx, PVEx, PVA, PVV, MMA, MMR, MMT, MTM, CAP and CPL from the old version are not 2026 pricing instructions; their precise earlier-period applicability and the old generic BEPS-signatory claim have not been verified here.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `brazil-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/brazil-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
