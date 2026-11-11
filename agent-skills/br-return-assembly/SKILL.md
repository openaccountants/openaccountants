---
name: br-return-assembly
description: "Assemble a source-linked Brazilian tax preparation package for calendar 2026 from documented intake and current owner-Guide calculations. Trigger on preparing the final IRPF working papers, reviewer package, reconciliations, DAS/DASN, Carnê-Leão, INSS or self-employed return action list. Covers PF/autônomo, MEI and Simples owners, mixed employment and component handoffs for foreign, crypto, corporate and municipal issues. Retains the workbook, reviewer brief, client actions and evidence trail while separating company turnover from owner income, tax assessed from paid, and invoice fields from tax credits. Routes calculations to their owning Guides instead of copying tables. Marks missing ordinary computations partial, blocks dependent results and continues independent work. Does not imply filing authority or an already published complete exercise 2027 annual-return calendar."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/br-return-assembly"
  jurisdiction: "BR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Brazil return assembly v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Assemble the authorised preparation work into a package a professional can review. The core routes are Brazilian PF/autônomo, MEI and Simples small-business owners, including employment and other income alongside the business. Use `br-freelance-intake` or an equivalent documented existing record. Do not make that router mandatory for a single calculation or re-ask facts already supported by the record.

Calendar 2026 and exercise 2027 are distinct. Retain a separate historical calendar 2025/exercise 2026 path when that is the actual work. The published exercise 2026 questions concern calendar 2025; they do not establish a complete exercise 2027 calendar, forms or final software. Prepare known 2026 facts and calculations while marking unpublished annual procedure partial. [RFB IRPF 2026 questions, cover](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

A full package means every applicable component and gap is visible, not that unsupported results have been guessed. This router owns assembly and reconciliation. Current rates, thresholds, tax calculations, deadlines and form fields remain with their designated tax owners. Specialist issues or ordinary missing subtopics are component referrals/partials; they do not silently remove the taxpayer's annual return from scope.

## Ask the client first

Read the whole existing case, intake, evidence and owner outputs before asking. Obtain only missing facts from these six groups:

1. Owner/entity, residence dates, calendar year/exercise, municipality/UF and requested deliverables/actions.
2. Activity/regime/option history, commencement, employment, staff and each applicable tax component.
3. Complete monthly income, payer/owner split, receipts, invoices, withholding, pro-labore and distributions.
4. Expense/deduction/contribution evidence, dependants/family facts and outstanding classification questions.
5. Prior/current returns, payments, corrections/notices, assets/debts and opening/closing movements.
6. Owner calculation versions/sources, unresolved inputs, actual filing/election history and review/submission authority.

## The method, step by step

### Establish the input and dependency register

Accept documented intake without restarting it. Check factual contradictions and calculation dependencies against source documents; do not treat a previous summary as conclusive where evidence disagrees. Record each component's owner Guide, version, tax period, source read dates, inputs, output location and status. Preserve the evidence ID or document location on calculation rows, not only in the final narrative.

Use four meaningful states: ready for review, partial, blocked by a named dependency, or not applicable with a reason. A missing receipt, regime fact or legal condition blocks the dependent tax/deduction/filing result. Continue independent reconciliations and papers. Never convert an upstream failure into a zero, a successful check or permission to file.

Produce the agreed complete preparation work without asking permission for each reversible step. Preparing papers or accepting intake does not authorise a real return, payment, election or amendment. Keep the current task's authorised actions separate from preparatory outputs.

### Execute the actual owner route

Choose only relevant components and respect their dependencies. Verify the sibling's coverage and open gaps before using its calculation. Resolve overlapping Guides to one calculation owner; do not silently run two methods and choose a convenient answer.

| Route / component | Inputs and outputs required |
|---|---|
| MEI | `br-simples-nacional`: activity/status/start-year and special-route eligibility, monthly revenue, applicable limit/excess consequences, DAS payments and DASN-SIMEI data. Then `br-inss` for contribution history/category and `br-income-tax` for the owner-income bridge and complete annual obligation |
| Simples | `br-simples-nacional`: activity and relevant payroll/revenue history, Annex/factor-R decision, effective calculation, sublimits and DAS reconciliation. `br-inss`/`brazil-payroll` for pro-labore/employer components; annual owner for actual distributions and all personal income |
| PF/autônomo | `br-estimated-tax` for applicable ordinary monthly calculation and payment reconciliation; rental-specific work to `br-carn-monthly-income-tax-rental-income` within its scope. `br-inss` for contribution category/concurrency. `br-income-tax` for annual income, deduction comparison and return |
| Municipal and consumption tax | The pack's designated `br-indirect-tax`/`brazil-vat` owner: actual activity, municipality, ISS retention, ordinary/special regime and tax results. `brazil-einvoice` supplies model/date/version/protocol evidence, not an automatic credit computation |
| Employment/staff | Employment statements feed the annual owner; `brazil-payroll` covers the applicable employer/staff/pro-labore work. Reconcile concurrent contributions with `br-inss` |
| Foreign/crypto/other entity | `brazil-crypto-tax`, `brazil-cross-border-tax`, `brazil-corporate-tax`, and relevant `brazil-transfer-pricing` component. Preserve each component's annual reporting/payment bridge, rather than dropping it from the personal package |
| Annual return | `br-income-tax`: obligation, all applicable income classes, complete/simplified comparison, current reductions/minimum/dividend rules, deductions, assets/debts and actual procedure |

Do not copy limits, contribution ceilings, pension percentages, deduction caps or filing dates from the old assembly. MEI gross revenue, presumed/actual accounting profit, withdrawals, pro-labore and owner income are different quantities. Do not classify all business turnover as individual taxable receipts or all distributions as exempt. The annual owner must apply the dated dividend/annual rules introduced by Lei 15270. [LC 123 art 14](https://legis.senado.gov.br/norma/572878/publicacao/34621013), [Lei 15270](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm).

For Simples, actual activity and the relevant payroll/revenue test determine the applicable branch. Annex IV is not a blanket ISS-outside-DAS rule: LC 123's stated employer CPP exception is distinct from the separate ISS cases. Let the owners resolve the applicable exception. [LC 123 arts 13 VI/VIII and 18](https://legis.senado.gov.br/norma/572878/publicacao/34621013).

### Reconcile the five original bridges

Keep a reconciliation table with source totals, adjustments, resulting destination total, unexplained difference, evidence and status. No universal R$ tolerance is a legal safe harbour. Any operational review materiality must be labelled as an assumption and must not erase an actual difference.

| Bridge | Required work and unsafe shortcut to avoid |
|---|---|
| Revenue between obligations | Reconcile separately for each CPF/CNPJ and payer class. Bridge invoices/competence to receipts with opening/closing receivables, cancellations, returns, fees/withholding and foreign-currency differences as applicable. Identify own transfers, loans and capital separately. Entity gross sales are not the owner's individual receipts |
| Contributions to annual deductions | Match competence, category, payer, assessed amount, withholding and actual payments to the contribution owner's result. Then match the annual owner's legally accepted deduction. Separate employee/pro-labore withholding, own payments, DAS components and supplements; do not deduct twice or use an unverified software payment code |
| Monthly PF income to annual return | Sum the actual monthly payer/source schedules, reconcile owner-accepted livro-caixa/contributions and payments, and preserve corrections/arrears. Compare annual fields to the annual owner's result; do not credit an unpaid assessment or treat every foreign receipt as the same monthly regime |
| Invoices to tax/accounting | Match key/model/date, authorised/cancelled/corrected status, client/owner, gross/net, ISS/IRRF and other taxes. Explain timing/classification differences instead of requiring invoice totals to equal or exceed all declared income. PF nonemployee PJ-paid withholding cannot be replaced by a PJ-to-PJ professional-services percentage |
| Assets and debts | Bridge prior closing to current closing by acquisition, disposal, borrowing, repayment and other documented changes. Preserve ownership, cost/balance, currency and gain/reporting handoffs. Do not automatically depreciate PF declared property, vehicles or equipment, or force changes to equal taxable income |

RIR arts 685/714 distinguish PJ-paid nonemployee PF income from PJ-to-PJ services. Use actual certificates and the correct owner calculation, not a fixed percentage manufactured from sales. [RIR 2018 arts 685,714](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm).

Livro-caixa is a deduction computation, not simply all expenses or annual cash outflows. Reconcile necessary documented professional costs, excluded capital/transport items, monthly income limits and the permitted within-year excess treatment through the owners. Personal mixed use needs evidence; do not reinstate the old percentage bands or carry an unsupported excess into a later year. [RIR 2018 arts 68–69](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm), [RFB Q427–434](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

### Assemble the applicable reform reconciliation

Retain debit, credit, classification/rate, document reconciliation and action topics, but create only applicable working papers. Capture operation/model/date, regime/CRT, actual regular-regime option history, issuer/recipient and evidence from `brazil-einvoice`; obtain tax eligibility/calculation from the consumption-tax owner.

Distinguish amounts shown on documents, legally assessed tax, compliance-based payment waiver, amounts actually collected/compensated and any valid recipient credit. Do not subtract every purchase's highlighted IBS/CBS from every sale or assume a refund/carryforward. LC 214's 2026 test rates exclude the stated Simples operations and its payment waiver has accessory-compliance conditions. [LC 214 arts 343–348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm).

Legal model/sector starts, technical publication, restricted testing and production implementation differ. The invoice owner must establish which applies. Simples/MEI does not mean all pre-existing invoice duties disappear. [Joint Act 4 art 1 and exceptions](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf), [official MEI NFS-e guidance](https://www.gov.br/nfse/pt-br/noticias/resolucao-cgsn-no-169-traz-novos-beneficios-ao-mei).

Future transition planning belongs in a separate dated section. Do not remove historical PIS/Cofins/ICMS/ISS papers because a later reform phase exists. Link the relevant period and tax owner's current law instead of copying a fixed future timetable or claiming all legacy documents become NFS-e. Separate actual existing elections from a potential option; do not assume an expired option window is still open.

### Produce all applicable working papers and three deliverables

Retain the original eleven paper topics. A not-applicable item gets a reason; a missing ordinary computation stays partial with a named dependency. Do not suppress it to make the package look complete.

| Paper | Required contents |
|---|---|
| Executive summary | Identity/residence/year/regime, package status, owner-accepted income/deductions/tax, documented payments, provisional or final balance and key gaps |
| Annual IRPF | All relevant income classes, deductions and complete/simplified comparison; calculation and filing-field mapping from the annual owner, including current annual adjustments and special components |
| Monthly receipts/tax or DAS | Monthly taxable-receipt/Carnê-Leão schedule or relevant MEI/Simples DAS/DASN/PGDAS reconciliation; assessments, payment receipts, differences, arrears and corrections |
| Livro-caixa | Monthly income, each claimed/accepted cost, exclusions/allocations, owner-calculated limit/excess and annual bridge |
| INSS | Category, competence, base/ceiling from owner, concurrency/withholding, assessment, actual payment, supplement and contribution-history differences |
| ISS | Actual municipality/activity/regime, assessed/withheld/paid amounts, invoice links and owner exceptions |
| CBS/IBS | Applicable document debits/inputs, separately established credit/waiver/payment treatment and current/future-phase distinction; do not fabricate a net balance |
| Assets/debts | Prior/current balances, item descriptions/codes only when verified, cost/currency/ownership, documented changes, gains and foreign/crypto liabilities |
| Five reconciliations | Each bridge above with source totals, adjustments, unexplained differences and ready/partial/blocked/not-applicable status |
| Reviewer brief | All positions, original sources/read dates, evidence anchors, owner versions, assumptions, gaps, referrals and check results |
| Client actions/calendar | Required documents/corrections/review, actual payment/filing actions, period, verified due date/source, responsible person and dependency |

Deliver the calculation workbook or appropriate usable equivalent, the reviewer brief and the client action/calendar list. Use the actual workspace/artifact tools and return links to files that were really created. Do not hardcode `/mnt/data`, a tool name or a file-presentation API, or claim a workbook exists when only a plan was written. Include a manifest identifying format, location, version and missing deliverables.

The workbook should preserve inputs, formulas, source links, checks, assumptions and owner-output references, with clear separation between raw records and adjusted calculations. Do not hardcode a formula's tax constants without the tax owner's version/source. The professional must be able to recompute and trace each material figure. Recalculate the delivered workbook or equivalent and check for broken references, formula errors and stale displayed values. Reconcile its displayed totals to the owner outputs and the reviewed reconciliations before delivery; a fixed currency tolerance, if used for an operational check, must be labelled as an assumption and is not a legal safe harbour.

### Reviewer brief and action/calendar contract

The brief must include:

- Identity, residence/year/exercise, activity/regime and professional review status, without unnecessary full identifiers.
- Taxable PF/PJ receipts, employment/pro-labore, exempt and exclusive/definitive items, foreign/crypto and other components, with owner classification.
- Medical/education/PGBL/alimony/dependant/contribution/livro-caixa evidence, accepted amounts and complete-versus-simplified result; do not restate old deduction caps.
- Annual calculation, applicable reductions/minimum/dividend interactions, ordinary versus separate tax, amounts due, actual credits/payments, refund/balance and missing dependencies.
- Monthly PF tax, MEI/DASN and Simples calculations, Annex/payroll/revenue/election decisions, contribution/ISS/reform reconciliations and prior corrections.
- Assets/debts and year-on-year movement explanations; all five bridge results and significant unexplained differences.
- Positions with actual act/article/official URL/read date, assumptions and evidence IDs; unresolved legal/factual questions, owner, next step and dependent results.
- Planning for the actual next period: contribution/category choices, revenue/eligibility trajectory, monthly records, invoice/election dates and later reform phases only as verified by owners.
- Each self-check's result and every missing output; licensed professional approval is recorded only if that person actually reviewed this version and facts.

For the action calendar, each row needs obligation/owner, CPF/CNPJ, period/exercise, filing versus payment, applicable condition, actual amount/status, due date, official source/read date, extension/holiday handling, responsible person, evidence and next action. Separate already-filed, overdue, currently due and future actions. Preserve the annual owner's actual instalment option, number/minimum/payment dates, interest, debit election and proof of each quota where applicable; do not reuse old generic instalment amounts or counts. Include monthly DAS/GPS/Carnê-Leão/municipal obligations and annual returns where applicable, but source dates from owners' current calendars. Preserve the applicability assessment for eSocial, EFD-Reinf, DCTFWeb/MIT, EFD ICMS/IPI, EFD-Contribuições, ECD and ECF; they are not all due from every freelancer.

Do not reuse the old DCTFWeb/ECD dates, unadjusted generic annual date or a complete exercise 2027 calendar before issued. A missing publication is a named calendar gap, not a guessed deadline. Penalty/interest exposure is a separate owner computation with actual notice, payment/filing date and legal condition; do not label unpaid amounts “no exposure” because a paper is incomplete.

## Worked cases

**Invoice-to-bank bridge.** Fictional invoices total R$ 100,000 including R$ 5,000 later cancelled. Opening receivables are R$ 20,000; closing receivables R$ 10,000. Assume no other adjustments, fees or withholding. Expected customer receipts are R$ 105,000. Bank credits total R$ 115,000, including a documented R$ 10,000 loan; net candidate customer receipts also equal R$ 105,000. This reconciles these assumed records. It does not establish tax revenue, owner distributions, an exemption or a legal tolerance.

```oa-check
name: Assembly invoice cash bridge, not tax revenue
inputs:
  invoices_before_cancellation: 100000
  cancellations: 5000
  opening_receivables: 20000
  closing_receivables: 10000
  bank_credits: 115000
  loan_receipt: 10000
steps:
  expected_customer_receipts: invoices_before_cancellation - cancellations + opening_receivables - closing_receivables
  bank_customer_candidates: bank_credits - loan_receipt
  unexplained_difference: bank_customer_candidates - expected_customer_receipts
expected:
  expected_customer_receipts: 105000
  bank_customer_candidates: 105000
  unexplained_difference: 0
```

**Proceed or block.** The receipt bridge is documented, but the contribution receipt and a mixed-use allocation are missing. Complete the receipt paper and other independent schedules. Mark the dependent deduction and annual balance blocked/partial, record the source searched and next action, and provide the package for review with those gaps visible. Do not invent zero deductions or zero tax, and do not submit a return on the strength of intake confirmation.

## When to refuse or refer

Refer the affected calculation to a competent current source/owner if the regime, municipality, contribution category, special receipt or foreign/corporate issue exceeds verified coverage. Residence changes, nonresidents/part-year, Lucro Real/Presumido, S.A., import/export, estates and special MEI/cargo activities remain explicitly tracked components. There is no blanket rule that all S.A. entities have CVM obligations or every nonresident needs a departure return.

Preserve capital-gain/GCAP, rental and foreign-rental income, estate and amended-return topics as named owner components when present. Identify the required return or correction and its dependency; do not claim the whole ordinary annual package is complete while one remains unresolved. Continue supported independent work. Refuse fabrication, falsely recording payment/approval, bypassing a decisive dependency or making an unauthorised filing/payment/election. An unsupported ordinary subtopic remains a partial gap rather than being relabelled wholly out of scope.

## Completion checklist

- Facts/owner versions and original sources traceable; calendar and filing exercise separated.
- All applicable papers and three deliverables produced or named missing; actual links/manifest supplied.
- Five bridges recompute; differences and duplicate payments/deductions remain visible.
- Regime/activity, owner-income and monthly/annual distinctions preserved; no stale copied constants or default exempt distributions.
- Reform document amounts, credits, waiver and actual payment treated separately; future phases labelled.
- Every calendar row has an applicable current source, or an explicit missing-publication status.
- Dependent outputs blocked where facts/law are missing; no unknown-as-zero or assumed professional approval.
- Reviewer positions, evidence, open items and action responsibility clear; preparation is distinct from submission authority.

## Sources

| Source and portion read | URL | Read on |
|---|---|---|
| RIR 2018 arts 68–69,685,714: costs/exclusions, excess and payer/recipient distinctions | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm |2026-11-11 |
| LC 123 arts 13–14,18,18-A/18-F: CPP/ISS distinction, owner income and activity/special-route handoffs; read in part | https://legis.senado.gov.br/norma/572878/publicacao/34621013 |2026-11-11 |
| Lei 15270 amendments to dividend and annual rules; read in part for dated annual-owner handoff | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm |2026-11-11 |
| RFB IRPF 2026 QA cover and Q427–434: actual calendar 2025 scope and professional-cost questions | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf |2026-11-11 |
| LC 214 current arts 343–348 and amendments affecting LC 123; conditional 2026 test/waiver and transition inputs | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm |2026-11-11 |
| Joint Act 4 art 1 and exceptions; model/date/regime distinctions handed to invoice owner | https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf |2026-11-11 |
| Official MEI NFS-e guidance; read for continuing invoice duty and PF-customer distinction | https://www.gov.br/nfse/pt-br/noticias/resolucao-cgsn-no-169-traz-novos-beneficios-ao-mei |2026-11-11 |

Not yet confirmed: complete exercise 2027 annual calendar/software/form fields; owner-level ordinary income, municipal, social-contribution and special-activity gaps; any universal reconciliation tolerance, blanket capital depreciation, automatic invoice credit or uniform five-year-from-January retention rule. Preserve originals/extracts/calculations, payment and filing evidence, amendments and open notices; obtain the applicable record-specific retention rule before destruction. These are visible partial components, not invented results or whole-taxpayer exclusions.

## Talk to a verified accountant

Give the professional the source-linked workbook, reviewer brief and action list with all gaps visible before filing or taking a tax position. Find Brazil Guides and professional-review options at [OpenAccountants](https://openaccountants.com). This Guide is **Not yet approved** and does not record approval of a particular return.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `br-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/br-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
