---
name: brazil-transfer-pricing
description: "EN: Use this skill whenever asked about Brazil transfer pricing rules, documentation requirements, or preços de transferência compliance. Trigger on phrases like \"transfer pricing Brazil\", \"Brazilian TP documentation\", \"preços de transferência\", \"master file Brazil\", \"local file Brazil\", \"CbCR Brazil\", \"APA Brazil\", \"Law 14.596/2023\", \"IN RFB 2161\", \"arm's length Brazil\", \"ECF\", or any question about intercompany pricing for Brazilian entities. PT-BR: Use esta skill sempre que for solicitada análise sobre as regras de preços de transferência no Brasil, requisitos de documentação ou conformidade em preços de transferência. Acione com expressões como \"preços de transferência Brasil\", \"documentação de TP brasileira\", \"preços de transferência\", \"master file Brasil\", \"local file Brasil\", \"CbCR Brasil\", \"APA Brasil\", \"Lei 14.596/2023\", \"IN RFB 2161\", \"arm's length Brasil\", \"ECF\", ou qualquer questão sobre precificação intercompany para entidades brasileiras."
version: 1.2
jurisdiction: BR
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: transfer-pricing
type: situation-rules
---

# Brazil transfer pricing: preços de transferência in 2026

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference.** Brazil's arm's-length regime is mandatory from 2024. For 2026 documentation, measure 2025 controlled transactions before TP adjustments: below BRL 15 million the Local and Global Files are dispensed with, BRL 15 million to below BRL 500 million requires a simplified Local File plus Global File, and BRL 500 million or more requires full Local File plus Global File. Dispensation from those files does not exempt any transaction from arm's-length pricing, other ECF information, underlying evidence or commodity registration. See the source-linked conditions below.

**Required inputs:** Brazilian taxpayer/entity and tax year; full related-party and favoured-regime map; prior-year and current-year transaction totals before adjustments; contracts and functional/risk evidence; comparable prices/margins; group ultimate parent and consolidated revenue. Authority: Receita Federal do Brasil (RFB); currency: Brazilian reais (BRL). Calendar 2026 income is ordinarily documented/returned in 2027; a 2026 filing for 2025 is different.

## Who this applies to

[Lei 14.596/2023 arts. 1-4](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art1) governs IRPJ and CSLL for Brazilian legal persons' controlled commercial/financial relations with related parties abroad. Relatedness turns on direct/indirect influence and the statutory control, common-control, family and other tests, not simply whether a group labels an invoice intercompany. Article 40 extends the relevant rules to the Lei 9.430 arts. 24/24-A favoured-tax-country and privileged-regime cases even where the counterparty is unrelated. Check the current statutory/list definitions; do not restrict the transaction inventory to shareholdings.

The old fixed-margin regime was replaced from 1 January 2024; an irrevocable early election was available for 2023 (Lei 14.596 arts. 45-47). The prior PIC/PRL/CPL and export-margin/commodity labels are relevant when reviewing earlier periods, not substitute 2026 methods. A historical PRL or CPL 20% does not supply a current arm's-length margin.

The OECD guidelines are subsidiary only within [IN RFB 2.161/2023 art. 1 §4](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782): later OECD changes require express RFB approval and cannot override Brazilian law/regulation.

Inventory intangibles, cash pools, guarantees, restructurings, financing and cost-sharing arrangements as well as goods, services and royalties. Their specialist valuation and separate-tax outcomes have the explicit holds below. Hiring an external consultant does not transfer the taxpayer's statutory documentation duty under art. 34 to that consultant.

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
| Country-by-country reporting dispensation, prior fiscal year consolidated revenue; Brazilian ultimate parent | Below BRL 2,260,000,000; other filing/notification conditions still apply | [IN RFB 1.681/2016 art. 4 I](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=79444): "R$ 2.260.000.000,00" |
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

The five named methods are **PIC/CUP**, **PRL/resale minus**, **MCL/cost plus**, **MLT/TNMM** and **MDL/profit split**, in art. 11 I-V. An alternative under VI requires reliable justification where the named methods cannot apply or do not give reliable results. Select the most appropriate method by reliable data and comparability. Article 11 §2 regards PIC as most appropriate where reliable independent prices exist unless another method is demonstrably more appropriate. [IN art. 34 §4](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782) also prefers PIC/PRL/MCL over MLT/MDL where they can be applied with equal reliability. Article 13 has the commodity-specific PIC rule, with comparability adjustments and the same better-method qualification. For quotation-based PIC, support the agreed pricing date/period with timely reliable evidence, consistent actual conduct and the required registration; absent those conditions, art. 13 §4 permits an authority-determined date/period, or the shipment/import-declaration quotation average where that is not possible.

If a one-sided method needs a tested party, art. 15 selects the party for which the method is most appropriately applied and data most reliable; document both parties' functions/assets/risks. Under art. 16, use the appropriate comparable range. Use the interquartile range where comparability uncertainties cannot be precisely identified or quantified and adjusted. Use the full range only where the uncontrolled transactions have equivalent comparability and no such uncertainty (art. 16 §2). An indicator within the appropriate range requires no adjustment (§3); where the controlled indicator is outside the appropriate range, use the median for the statutory adjustment. Do not manufacture a fixed margin or label a group policy percentage a safe harbour.

### Adjustments and documentation are separate jobs

[Lei 14.596 art. 18](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art18) requires spontaneous/compensating adjustments where non-arm's-length terms understate the Brazilian tax base. A primary authority adjustment is separate. Downward adjustments/increased losses are restricted; the regulated compensating-adjustment and treaty dispute-resolution exceptions must actually be satisfied.

[IN 2.161 arts. 48-50](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782) requires spontaneous/primary adjustments in periods ending on 31 December even for quarterly taxpayers, or on the incorporation, merger, division or closure event date. These adjustments do not enter monthly annual-regime estimated bases. A qualifying compensating adjustment needs definitive symmetric accounting by all parties for the same value and transaction nature; debit/credit or fiscal/commercial documents identifying the transactions, nature and amount; confirmation by the foreign parties' legal representative, attested by the Brazilian representative; and no counterparty within Lei 9.430 arts. 24/24-A. The last two conditions are waived for adjustments increasing the tax bases or reducing tax losses. Multiple adjustments with the same party in the same year may use one confirmation. Article 50 §2 permits completion by ECF delivery only where permanently booked in the transaction year's accounts. No prior RFB authorisation is needed, but subsequent audit remains possible. Do not treat an unrecorded late journal or unilateral downward correction as qualifying.

**Services:** [arts. 23-24](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art23) require a reasonable expected economic/commercial benefit of a kind an independent business would pay for or perform itself. Shareholder activities and duplicative services generally do not meet the benefit test unless the stated additional-benefit exception applies. Incidental group benefits are not separately chargeable services. For cost plus, include related service costs, use direct charging where identifiable and a justified allocation where they cannot reasonably be individualised. Under art. 24 §§4-6, do not mark up passed-through costs of activities/acquisitions from other parties where the provider performs no significant functions, considering assets and economically significant risks. An arm's-length markup can apply only to its own costs of performing the relevant functions in that case. The same cost discipline applies to cost-based MLT. This does not make all reimbursed costs markup-free.

**Optional low-value services:** [IN 2.161 art. 53 I-II, §§1-6](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782) provides a directional simplification: a Brazilian service provider must earn at least 5% gross markup on all direct and indirect transaction costs; a related foreign provider may earn at most 5%. Eligibility requires support services outside the related party's or the group's core activities, no unique valuable intangibles or contribution to their creation, no assumption/control or creation of economically significant risk, and no significant contribution to group value, core capabilities or business success. Services also supplied by the group to unrelated parties do not qualify. Exclusions are core business, R&D except qualifying low-value IT, manufacturing/production, purchasing production inputs, sales/marketing/distribution, financial transactions, natural resources, insurance/reinsurance, senior management except management of qualifying services, and international transport, asset letting or chartering. Allocate costs in proportion to actual or expected benefits where allocation is needed. Deductibility still requires the reasonable expected economic/commercial benefit for which an independent party would pay or act itself. This is not a universal fixed 5% safe harbour.

**Files:** Global File describes group structure, value chain, intangibles, financing, restructurings and consolidated financial/tax context (IN arts. 55,58). Full Local File covers the business, competitors, transactions, functions, methods, comparables, accounting reconciliation and specialised transaction material (arts. 59-60). The simplified version still requires entities, transaction values, methods, comparables/ranges, selection reasons and adjustments (art. 61). It is not a zero-documentation exemption. Article 57's largest-transaction selection does not exempt the remaining controlled transactions from law or evidence. If a third-party technical study is submitted, art. 59 IV(m) requires the preparer's declaration of responsibility for its information and techniques. That requirement does not transfer the taxpayer's own documentation or tax duties to the consultant.

**Language and evidence:** IN art. 62 requires contemporaneously organised support. Foreign-language supporting documents need simple translation; English/Spanish support requires translation only on request, and the authority can request a sworn translation for procedure. Article 63 allows the authority to require reproduction of comparable-database searches on the taxpayer's premises. Separately, art. 58 §§1-2 expressly permits a foreign-language Global File with simple Portuguese translation; for an English or Spanish Global File, translation is required only on request. The authority may require a sworn translation for procedural purposes. Article 59 §§2-3 applies the corresponding rule to Local File contracts and foreign tax agreements specified there; it does not establish the language of the Local File body. **Local File body-language hold:** do not submit a body based on the old unconditional Portuguese-only claim or infer permission for another language from supporting-document rules. Check this point with one of our partner accountants.

### CbCR is distinct from Local/Global Files

[IN 1.681 arts. 3-9](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=79444) makes a Brazilian ultimate parent responsible, subject to the revenue dispensation in the table. A Brazilian constituent has secondary filing if the foreign ultimate parent need not file, if its jurisdiction has an international agreement with Brazil but no competent-authority agreement by the ECF deadline, or if RFB notifies systemic failure. With multiple Brazilian constituents, designate the filer and notify RFB. Surrogate filing switches off secondary filing only if the surrogate's jurisdiction requires an art. 9-compliant report, it files within twelve months after group fiscal year-end, an effective competent-authority agreement with Brazil exists by the deadline, neither jurisdiction has notified systemic failure, the surrogate notifies its jurisdiction that it reports, and RFB receives the reporting-entity identification. All Brazilian constituents must notify their reporting role/entity; below-threshold groups must notify the dispensation too. Historical 2016 transition permissions are not current exemptions.

Report through ECF for the preceding fiscal year. The data include jurisdictional revenues (related/unrelated and total), profits, income tax paid/accrued (including Brazilian CSLL), capital, accumulated earnings, employees and non-cash tangible assets, constituent entities/activities and explanations. Aggregate by jurisdiction in one ultimate-parent currency, taking full entity amounts rather than ownership-proportion netting. Use one of Portuguese, English or Spanish for all free text (art. 9 §3). Treat CbCR as reporting, not as a substitute for the transaction-level pricing analysis. On notified systemic failure, art. 10 requires the affected reports or surrogate designation within thirty days of notice; do not keep naming a filer in that jurisdiction for later years while failure persists.

## Deadlines and filing

1. Determine the covered year and prior-year file thresholds. Assemble the transaction inventory, analysis and current-year adjustments contemporaneously, not after a file threshold is crossed. Reconcile values to the accounts and ECF.
2. ECF ordinarily falls on the last business day of July of the following year, according to [Receita's ECF FAQ](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/sped/ecf/ecf/qual-e-a-data-limite-regular). For division, merger, incorporation or closure in January-April, use the last business day of July of that year; for May-December, the last business day of the third following month. Populate TP/CbCR records from the applicable year's official ECF layout, validate/sign/transmit and retain the receipt. **Layout hold:** no ECF record/field number or RTC import-file layout in an old workpaper is authorised by this Guide. Check this point with one of our partner accountants.
3. Under IN art. 56, file the Global and Local Files through a digital process within three months of the applicable ECF deadline. This is measured from the deadline, not the taxpayer's early actual filing day. For 2026 activity this normally means 2027 filings, subject to later legal changes. The historical 2024 file deadline was the last business day of 2025, and an early-election 2023 file was due the last business day of 2024; these are not extensions for current work.
4. Use [Receita's official documentation service](https://www.gov.br/pt-br/servicos/entregar-documentacao-de-precos-de-transferencia): select area **Preços de Transferência** and service **Apresentar Documentação de Preços de Transferência relativas ao IRPJ e CSLL**. Open only one process for each calendar year, attach the required files, submit and save the protocol. Corrections/additions go into the same year's existing process; review status/documents under **Meus Processos**. Opening a process without attaching/submitting the files does not establish complete delivery.
5. For controlled commodity imports/exports, separately register the contract and any renegotiation or extension in the e-CAC RTC system by art. 64's deadline, linking a renegotiated contract to its original registration. Register even if PIC is not used and regardless of contract form. Pre-2025 contracts supporting imports/exports from January 2025 also required registration. The 31 March 2025 transition covered those contracts and January/February 2025 contracts; it is not a 2026 extension. Registration includes parties, contract, commodity, price/formula, pricing date/period, references and method. The Local File retains contracts and RTC receipts (arts. 38,60). For proven errors, art. 38 §5 allows pricing-information corrections through the tenth business day after the registration deadline, and other-information corrections at any time; uncertain formula components do not need correction simply when realised (§6). A registration alone does not prove arm's-length pricing. Use the layout hold above where the current layout has not been established.

## Penalties and interest

Apply the specific documentation penalties in the table. For lateness, count from the day after the original deadline through compliance or, if still outstanding, the assessment notice. The 0.2% group-revenue information penalty is for the **Global File**, not automatically every inaccurate Local File entry. Its exception covers proven formal errors or information not compromising reliable arm's-length results (IN art. 66 §§4-5). **Maximum-fallback hold:** Lei 14.596 art. 35 §2 refers missing/unproved group revenue to I(c), whereas IN art. 66 §2 refers it to II. Do not calculate an assessment under that conflicting cross-reference from this Guide. Check this point with one of our partner accountants.

CbCR's separate [IN 1.681 art. 11](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=79444), as amended by IN 2.161 art. 76, imposes: late reporting, 0.2% per month/fraction of the taxpayer's relevant-period gross revenue; audit information/document failure or obstruction, 5% of the corresponding transaction as priced by the authority; inaccurate/incomplete/omitted reporting, 0.2% of prior-year group consolidated revenue; and failure of filing requirements, 3% of the taxpayer's relevant-period gross revenue. Minimum BRL 20,000/maximum BRL 5 million applies. Missing/unproved group revenue gives the maximum for the information penalty. Lateness runs from the next day after the original deadline to compliance or assessment. Proven formal errors/immaterial information are excepted from the information penalty; immaterial means not compromising reliable arm's-length results. **ECF return-penalty hold:** the old generic BRL 1,500/month is not a usable ECF penalty calculation; determine the taxpayer's own governing regime. Check this point with one of our partner accountants.

An adjustment also requires IRPJ/CSLL and interest analysis. [Lei 9.430 art. 44](https://www.planalto.gov.br/ccivil_03/leis/L9430compilada.htm#art44) sets the ordinary 75% assessment penalty. Qualified conduct under Lei 4.502 arts. 71-73 gives 100%, or 150% for proven recurrence within two years of the earlier assessment; qualification requires individualised, proven intent and does not apply after a merits acquittal in the proceeding from which the taxpayer's criminal charge arises. Article 44 §2 increases the applicable percentage by half for the specified unanswered information/document demands; reductions and special assessment rules must also be tested. **Assessment hold:** no final payable penalty follows from the headline percentages alone. Check this point with one of our partner accountants. [Article 61](https://www.planalto.gov.br/ccivil_03/leis/L9430compilada.htm#art61) late-payment penalty runs at 0.33% daily from the day after due date through payment, capped at 20%; SELIC runs from the following month through the month before payment, plus 1% in the payment month. Do not mechanically stack overlapping assessment and late-payment penalties.

Lei 14.596 art. 36 and [IN art. 67](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782) condition audit regularisation on complying with binding acts, cooperation, reasonable compliance efforts and coherent, reasonably justified tax-base criteria. The authority must issue a Termo de Constatação before assessment for a qualifying taxpayer, allowing thirty days to correct the ECF and, where a tax credit results, DCTF. Corrections must cover the whole transaction specified; late/missing required Local/Global Files fail the reasonable-effort condition. No assessment fine applies to directly corrected infractions only if the resulting tax credit is fully paid with art. 61 additions within that correction period. Accepted correction closes that matter; later amendments need RFB authorisation. It is not unconditional penalty forgiveness.

## Cross-border points

**Specific consultation/APA:** [Lei 14.596 art. 38](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm#art38) authorises a future-transaction methodology consultation. Duration is in the table; extension needs an application and authority approval. False, misleading or omitted information can invalidate it retroactively; critical-assumption changes ordinarily invalidate it from the change, while legal changes can prompt revision. **Operational APA hold:** do not use the historical January 2025 availability claim, unilateral/bilateral/multilateral labels, expected three-to-five-year duration or an assumed fee as filing instructions. Current admission and indexed payable fees require case-specific clearance. Check this point with one of our partner accountants. Article 39 implements agreed treaty dispute results; it does not automatically award foreign corresponding relief. **Treaty/MAP hold:** establish the applicable agreement and procedure before claiming relief. Check this point with one of our partner accountants.

**Related taxes:** separate thin-capitalisation rules remain relevant under Lei 14.596 art. 42; arm's-length interest alone does not establish deductibility. [IN art. 51](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782) expressly says spontaneous/compensating adjustments do not automatically adjust other taxes, including import taxes. Imported intercompany services need their own consumption-tax analysis: [LC 214 art. 348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm#art348) provides a conditional 2026 IBS/CBS payment dispensation for accessory-compliant taxpayers, not a blanket rule that consumption-tax consequences begin only in 2027.

**Specialist holds, no usable outcome supplied:** for hard-to-value intangibles, cash pools/guarantees, financing, cost sharing and restructurings, retain the actual contracts, amounts, functions/assets/risks and years; do not assume a fixed-margin or financing safe harbour. Check this point with one of our partner accountants. For thin-capitalisation ratios, customs valuation/import taxes, imported-service IBS/CBS computations and multinational minimum-tax/additional-CSLL calculations, do not infer a payable amount, exemption or credit from TP compliance. Check this point with one of our partner accountants.

**Earlier-period hold:** retain the original 2025 context and any pre-2024 records/election evidence. The archived labels PIC, PRL, CPL, PVEx, PVA, PVV, PCI, PCEx, MMA, MMR, MMT, MTM and CAP, including old PRL/CPL 20% references, are not current pricing instructions. No historical method/margin conclusion is supplied for an earlier-year correction. Check this point with one of our partner accountants.

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

Sources below were read on 27 November 2026, except the expressly reused, unchanged LC 214 payment-dispensation proof. Normas articles were read in Receita's rendered current-text view after the ordinary links returned an app shell. The private claim ledger contains the exact Portuguese operative sentences and historical topic destinations.

| Official source and parts read | URL | Read on |
|---|---|---|
| Lei 14.596/2023 arts. 1-24,34-40,42,45-47; scope, methods, adjustments, services, documentation, consultation and commencement | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm | 2026-11-27 |
| IN RFB 2.161/2023 arts. 1-6,34,37-38,48-73,76; subsidiary guidelines, equal-reliability preference, adjustments, documentation, RTC and penalties | https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=133782 | 2026-11-27 |
| IN RFB 1.681/2016 arts. 3-11, with current penalty wording checked against IN 2.161 art. 76 | https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=79444 | 2026-11-27 |
| RFB documentation service: process selection, one process per year, attachments/corrections and tracking | https://www.gov.br/pt-br/servicos/entregar-documentacao-de-precos-de-transferencia | 2026-11-27 |
| RFB ECF deadline FAQ: ordinary and special-event branches | https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/sped/ecf/ecf/qual-e-a-data-limite-regular | 2026-11-27 |
| Lei 9.430/1996 compiled arts. 44,61 and art. 5 §3 interest reference | https://www.planalto.gov.br/ccivil_03/leis/L9430compilada.htm | 2026-11-27 |
| LC 214/2025 art. 348 §1: unchanged 2026 accessory-compliance payment dispensation; completed br-indirect-tax proof reused after applicability check | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm#art348 | 2026-11-26; applicability 2026-11-27 |

Not yet confirmed: no unproven outcome is supplied as usable guidance. The Local File language, layouts, ECF fine, maximum-fallback dispute, final assessment, operational APA/MAP, specialist computations and earlier-period conclusions above are explicit non-usable holds. Check this point with one of our partner accountants.
