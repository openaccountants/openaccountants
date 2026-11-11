---
name: br-freelance-intake
description: >
  Prepare a documented intake and handoff for Brazilian self-employed tax work
  covering calendar year 2026, with a separate historical-year path. Trigger on
  preparing IRPF, freelancer, autônomo, MEI, Simples Nacional, missing tax documents
  or assembling a self-employed return package. Read existing records first,
  extract uploaded evidence, reconcile payer and taxpayer identities, then ask
  only for facts still missing. Covers mixed employment, business receipts,
  contributions, deductions, assets, debts and invoice reform routing. Produces
  a structured package for br-return-assembly without inventing tax paid or
  treating bank deposits as income. Tax computations stay with their owning
  Guides. Residence changes, other company regimes and special activities receive
  component referrals while supported preparation continues. This is an intake
  method, not permission to file, pay or make an election.
version: 1.2
jurisdiction: BR
tax_year: 2026
last_updated: 2026-11-11
category: orchestrator
type: router
tier: 2
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Brazil freelance intake v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this preparation workflow when the task is to collect and organise facts for a Brazilian self-employed return package. It covers PF/autônomo, MEI and Simples small-business owners, including employment alongside their business. It is not a prerequisite for answering an unrelated Brazil tax or invoice question. A structured existing record can replace a fresh intake.

The current coverage year is calendar 2026. Record filing exercise separately: a historical calendar 2025 return belongs to exercise 2026; calendar 2026 annual adjustment belongs to exercise 2027. Do not apply the published exercise 2026 software or calendar to an unissued exercise 2027 filing procedure. The official 2026 questions document explicitly identifies calendar 2025. [RFB IRPF 2026 questions, cover](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

Tax amounts, eligibility limits, rates, deadlines, deductible amounts and software fields are owned by the linked tax Guides below. This router collects their inputs and preserves unresolved ordinary subtopics as partial components. It does not calculate a complete IRPF return, resolve every municipal rule, or certify a particular contribution plan.

## Ask the client first

Read the whole existing client record, timeline, notes, drafts and available correspondence before asking. Reconcile conflicting documents and identify their source. Ask only for missing facts from these six groups, using available tools or concise grouped questions rather than requiring a particular tool name:

1. Calendar year/exercise, tax residence and changes, owner/entity, municipality/UF and work requested.
2. Actual activity, CNPJ/start date, registration and option/election history, other businesses, employees and concurrent employment.
3. Receipts by payer and CPF/CNPJ owner, foreign/crypto/other income, gross versus net, dates and withholding evidence.
4. Business expenses, mixed use, contribution category/payments and personal deduction facts, including dependants and family/property arrangements.
5. Opening and closing assets/debts, acquisitions/disposals, owner withdrawals/profit distributions and prior returns/payments/notices.
6. Documents available, missing evidence, invoice model/technical history and any actual election or filing already made.

## The method, step by step

### Read existing records, then obtain documents

Start with a short explanation that the work will produce a documented draft for professional review. Do the preparation already authorised; do not ask whether to begin each routine stage. Do not promise a fixed completion time or number of user turns.

Use documents already supplied before requesting more. For an existing firm client, search the established case record and connected correspondence/document stores within the authorised scope before asking. Ask for originals or usable exports in one grouped request. Partial uploads are enough to begin extracting and reconciling supported pieces; identify the exact remaining items later. Do not ask a client to research tax law.

| Evidence group | Documents and facts to preserve |
|---|---|
| Identity and regime | Existing identity/residence facts, CNPJ registration, commencement/closure dates, actual Simples/SIMEI option history, prior declarations and payment history. A registration card alone is not proof of every tax election |
| Bank and payment accounts | PDF/CSV statements for relevant PF/PJ accounts, card/payment-platform settlements, cash records and foreign-currency records; preserve account owner and dates |
| Sales and service evidence | Issued/received invoices and original XML, cancellation/correction/authorisation events, contracts, client CPF/CNPJ and payer country; gross amounts, fees, withholding and receipt dates |
| PF income and monthly tax | Monthly receipt records, Carnê-Leão calculations/exports, DARFs and payment confirmations, corrections and prior unpaid balances |
| Employment and other income | Employer/payer income statements, withholding/contribution certificates, employment plus side activity, year-end/holiday pay classification, bank/broker statements, exempt/exclusive-source and foreign receipts |
| Business costs and payroll | Livro-caixa, invoices/receipts, professional purpose, employees/contractors and payroll, rent, supplies, software and telephone/internet evidence; equipment purchases and travel/commuting kept distinct |
| Social contributions | GPS/DARF/DAS and actual contribution statements, competence month, category/code, payer withholding, pro-labore and concurrent jobs; separate assessment from payment |
| Personal deductions and family | Dependants' identity/relationship/income, medical and education receipts/reimbursements, PGBL and other pension statements, alimony instrument/payment and applicable marital/property arrangement |
| Assets, debts and prior year | Prior return, acquisition/disposal contracts, year-end balances, investments, crypto, property, vehicles, loans, security and ownership; distinguish cost, balance and valuation |
| MEI/Simples | Monthly revenue reports, DAS/DASN-SIMEI/PGDAS-D outputs and payments, activity breakdown, commencement, trailing revenue/payroll, pro-labore, accounts and profit approvals/distributions |
| Notices and reform | Official correspondence and response dates; invoice model, actual dates, regime/CRT, classifications, supplier/acquisition evidence, CBS/IBS election history and existing integrations |

If the person does not know where records are, suggest bank/broker exports, their previous accountant, existing email documents, the official tax account and contribution records. Do not request passwords or signing keys or fabricate portal menu steps. Explain which missing record matters and continue independent preparation while it is obtained.

### Extract facts without inventing tax classifications

For every document record evidence ID, filename/source, owner, covered dates, extraction location and reliability. Preserve originals separately from edited extracts. Distinguish **documented**, **inferred**, **client-confirmed**, **assumed**, **missing** and **disputed**. Confirmation is not proof a payment reached the authority; keep both evidence types.

Bank patterns support investigation, not automatic tax assessment. Repeated credits with a customer name are candidate receipts. Match them to invoices/contracts and payer records. Identify transfers between the person's own accounts, loans, capital introductions, refunds and reversals. For card/platform settlements, bridge gross sales, fees, withholding and net deposits. Match both legs of PF/PJ transfers and distinguish pro-labore, loans, reimbursements, capital and distributions. Unknown credits remain unclassified, not zero and not automatically taxable.

For each receipt preserve CPF/CNPJ owner, payer type/country, activity, currency, invoice and receipt dates, gross amount, deductions/fees, withholding and bank match. A company's gross revenue is not the owner's individual income. Separate PF receipts from PJ invoices and the amounts the entity actually pays or distributes to the owner. LC 123 treats owner distributions separately, and the 2026 dividend qualification must be applied by the annual tax owner. [LC 123 art 14](https://legis.senado.gov.br/norma/572878/publicacao/34621013), [Lei 15270 amendments to dividend and annual rules](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm).

Do not infer a fixed PF withholding percentage from an invoice to a company. RIR art 685 addresses nonemployee income paid by PJ to PF using progressive tables; art 714's professional-services withholding concerns PJ payments to another PJ. Capture the actual payer certificate and payment date, then let the owner apply the right rule. [RIR 2018 arts 685,714](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm).

For costs, extract amounts and purpose before classifying deductions. Necessary documented professional costs, monthly limits and within-year excess treatment require the annual/monthly tax owner. Keep equipment/capital expenditure, commuting/transport and employee costs separate; do not import the old blanket transport allowance or a domestic-employee count rule. RIR arts 68–69 distinguish necessary costs and restrict transport, depreciation and excess treatment. Do not turn a capital purchase into a depreciation deduction without a supported rule. [RIR 2018 arts 68–69](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm), [RFB Q427–434](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

Capture actual mixed professional/private use with allocation evidence, period and method. Do not offer the old home-office percentage bands as legal allowances. Personal deduction receipts, reimbursements, dependants' other returns/income, pension eligibility and alimony facts need their own validation. Store gross expense, claimed allocation and owner-accepted deductible amount separately.

### Choose the owner route from actual facts

Check the actual file/Guide and its current coverage before using its output. These are repository slugs, not automatic assertions that every ordinary subtopic in a sibling is complete.

| Component | Owner and required handoff |
|---|---|
| Complete annual individual tax | `br-income-tax`: filing obligation, full income classification, deductions, complete-versus-simplified comparison, annual tax/reductions/minimum-tax/dividend interactions, assets/debts and actual annual procedure |
| Self-employed PF monthly receipts | `br-estimated-tax`: ordinary monthly computation, payments and annual bridge. Use `br-carn-monthly-income-tax-rental-income` for its actual rental/receipt scope; resolve overlap before invoking two calculations |
| MEI and Simples | `br-simples-nacional`: actual eligibility/activity, start-year limits, excess consequences, Annex/factor-R inputs, DAS/DASN/PGDAS, owner-profit bridge and dated regular-regime election. Do not assign an Annex solely from profession/CNAE |
| Contributions and employees | `br-inss`: category, competence, concurrent earnings, withholding and payments; `brazil-payroll` for staff/employer/pro-labore obligations within its verified scope |
| Municipal/consumption tax | `br-indirect-tax` or `brazil-vat`, according to the pack's designated owner and scope; actual municipality/activity, ISS retention and ordinary/special regime inputs. Avoid a second inconsistent assessment |
| Invoice issuance and reform fields | `brazil-einvoice`: model, date, UF/municipality, regime/CRT, XML, protocols and technical/deployment history. An invoice question does not need this full intake |
| Crypto/foreign/other entity | `brazil-crypto-tax`, `brazil-cross-border-tax`, `brazil-corporate-tax` and, when relevant, `brazil-transfer-pricing`; hand off only the affected facts and preserve the resulting annual reconciliation |
| Final package | `br-return-assembly`: documented intake, reconciliations, owner outputs, unresolved components and authorised actions |

MEI and Simples eligibility needs actual start date, type of activity and relevant revenue history. MEI cargo and other exceptions cannot use a blanket ordinary limit. Factor-R-sensitive activities require the relevant payroll/revenue history, not just a job title. Annex IV is not a blanket exclusion of ISS from DAS: the employer CPP exception and any separate ISS exceptions must be handled by their owners. [LC 123 arts 3,13 VI/VIII,18,18-A,18-F](https://legis.senado.gov.br/norma/572878/publicacao/34621013).

Retain all five former reform topics as dated inputs: issued document model; Simples/SIMEI status; any MEI transition; actual reduced/special classification; and supplier/acquisition profile. Add actual election date, evidence, result and effective period. The governing regular-regime option is not established by the old art 21-A label. Use the Simples owner for current option windows and LC 123 art 13 conditions as amended. Invoices and consumption-tax credit decisions then go to their owners. [LC 214, amendments to LC 123 and arts 343–348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm).

Do not presume that 2026 test tax applies to Simples transactions, that buying from a regular supplier creates an automatic credit, or that MEI has no existing invoice duties. Legal duty, elected regime, current technical deployment and tax payment/waiver are separate facts. [LC 214 art 348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm), [official MEI NFS-e guidance](https://www.gov.br/nfse/pt-br/noticias/resolucao-cgsn-no-169-traz-novos-beneficios-ao-mei).

### Confirm the summary and resolve only consequential gaps

Show a compact summary of identity/residence/year, activities/regimes, income by owner/payer, expenses/contributions, deductions, assets/debts and outstanding documents. Mask identifiers where full values are unnecessary. State which amounts are documented, which inferred and which missing. Invite correction once; do not re-ask facts already supported in records.

Then ask only unresolved facts that change a calculation, route or filing. A user preference for complete/simplified is not a substitute for the annual owner's lawful comparison. Preserve marital status and applicable property arrangement, dependant identity/relationship/income, mixed-use allocation, alimony basis, home-office facts, asset/debt movements, foreign income and exempt/exclusive receipts. Do not supply default percentages, ages, thresholds or deduction caps here.

Build a gap register with item, source searched, reason needed, owner, dependent output and next action. Missing legally decisive facts block the dependent result; they do not stop unrelated work. An unsupported question in an ordinary component remains labelled partial rather than being silently removed from the package.

### Structured handoff

The following is a preparation contract, not an official filing schema. `null` means unknown; verified zero needs its own evidence. For each amount/choice, attach provenance through `fact_register`, using a JSON pointer as the field identifier. Arrays keep source records and periods, not merely totals. No tax constants are embedded as facts.

```json
{
  "contract_version": "1.1",
  "jurisdiction": "BR",
  "tax_year": 2026,
  "filing_exercise": 2027,
  "preparation_status": "draft",
  "taxpayer": {
    "name": null,
    "cpf": null,
    "cnpj": null,
    "birth_year": null,
    "marital_status": null,
    "property_regime": null,
    "residency": null,
    "residency_dates": [],
    "business_type": null,
    "cnae_principal": null,
    "actual_activities": [],
    "start_date": null,
    "option_history": [],
    "employment_status": null,
    "municipality": null,
    "state": null
  },
  "income": {
    "rendimentos_tributaveis_pj": null,
    "rendimentos_tributaveis_pf": null,
    "irrf_retido": null,
    "rendimentos_isentos": null,
    "rendimentos_sujeitos_tributacao_exclusiva": null,
    "faturamento_bruto_mei_simples": null,
    "client_breakdown": [],
    "receipts_by_month_owner_payer": [],
    "foreign_and_crypto": [],
    "unclassified_credits": []
  },
  "expenses": {
    "livro_caixa": [],
    "total_livro_caixa": null,
    "mixed_use": [],
    "capital_purchases": [],
    "despesas_medicas": null,
    "despesas_educacao": null,
    "pgbl": null,
    "pensao_alimenticia": null
  },
  "carne_leao": {
    "monthly_receipts_pf": [],
    "monthly_darfs_paid": [],
    "total_paid": null
  },
  "inss": {
    "contribution_type": null,
    "concurrent_employment": [],
    "monthly_payments": [],
    "total_paid": null
  },
  "mei": {
    "faturamento_bruto": null,
    "das_payments": [],
    "das_total": null,
    "parcela_isenta_servicos": null,
    "parcela_isenta_comercio": null,
    "parcela_isenta_industria": null,
    "parcela_isenta_transporte": null,
    "profit_calculation_owner_output": null
  },
  "simples_nacional": {
    "faturamento_bruto_12m": null,
    "anexo": null,
    "fator_r": null,
    "das_payments": [],
    "das_total": null,
    "pro_labore": null,
    "distribuicao_lucros_isenta": null,
    "profit_payment_approval_period_records": []
  },
  "deducoes_legais": {
    "dependentes": [],
    "despesas_medicas": null,
    "despesas_educacao": null,
    "pgbl": null,
    "pensao_alimenticia": null,
    "inss": null
  },
  "bens_e_direitos": [],
  "dividas_e_onus": [],
  "prior_year": {
    "imposto_devido": null,
    "rendimentos_tributaveis": null,
    "bens_e_direitos": [],
    "dividas_e_onus": [],
    "return_and_payment_evidence": []
  },
  "modelo_declaracao": "calculate_both_if_available_and_applicable",
  "reforma_tributaria_2026": {
    "g1_emite_nf": null,
    "g2_simples_nacional": null,
    "g3_mei_status": null,
    "g4_aliquota_reduzida": null,
    "g5_fornecedores_regulares": null,
    "regular_regime_election_history": [],
    "skills_downstream_acionadas": []
  },
  "owner_calculations": [],
  "fact_register": [],
  "reconciliations": [],
  "open_flags": [],
  "referrals": [],
  "documents_received": [],
  "authorised_actions": []
}
```

The legacy `parcela_isenta_*` fields above are **owner-computed monetary results**, not automatic statutory percentage constants. The field name `distribuicao_lucros_isenta` is a proposed classification pending the annual owner's review; keep total distributions separately in underlying records. The former `regime_hibrido_art21a_lc123` field is replaced by dated `regular_regime_election_history`; old `refusals_triggered` becomes component-level `referrals`. Marital-status categories (single, married under the applicable property regime, stable union and other actual status) are facts, not a legal conclusion about joint filing. No meaningful old input topic is discarded by these changes.

Hand `br-return-assembly` the document index, source-linked fact register, monthly reconciliations, owner-output versions, confirmation/correction record and gap register. State what is ready and which result remains dependent. Do not describe the intake as complete if required evidence is still missing.

## Worked cases

**Payer classification decision.** Fictional PF service receipts are R$ 72,000 from Company A, R$ 36,000 from Company B and R$ 12,000 from individual customers. The PJ-payer subtotal is R$ 108,000, PF-payer subtotal R$ 12,000 and total R$ 120,000. Classifying the entire R$ 120,000 as PJ-paid and then adding PF receipts would wrongly produce R$ 132,000. No withholding amount is inferred. A missing contribution receipt or expense-allocation fact blocks the dependent deduction, not the receipt reconciliation.

```oa-check
name: Intake payer split, not a tax calculation
inputs:
  company_a: 72000
  company_b: 36000
  individual_customers: 12000
steps:
  pj_payer_total: company_a + company_b
  pf_payer_total: individual_customers
  total_receipts: pj_payer_total + pf_payer_total
  erroneous_double_count: total_receipts + pf_payer_total
  overstatement: erroneous_double_count - total_receipts
expected:
  pj_payer_total: 108000
  pf_payer_total: 12000
  total_receipts: 120000
  erroneous_double_count: 132000
  overstatement: 12000
```

**Maria's retained fictional confirmation scenario.** Assume a full-year Brazilian-resident PF technology consultant in São Paulo, single, with no claimed dependants. Use the payer split above: company-paid receipts R$ 108,000 and PF-paid receipts R$ 12,000. The record lists claimed office rent R$ 14,400, mixed telephone/internet R$ 3,600, software R$ 4,800 and supplies R$ 1,200, totalling R$ 24,000 **candidate** costs. Actual payment, professional purpose, allocation, monthly limits and deductible treatment remain for evidence and the tax owner; the candidate total is not an accepted deduction. Claimed medical spending R$ 8,400 and PGBL R$ 9,600 likewise need beneficiary, reimbursement, payment and eligibility evidence. Do not infer their deductible amounts from the scenario.

The prior record lists an apartment at R$ 450,000, vehicle R$ 85,000, bank/savings balance R$ 42,000 and investments R$ 120,000, totalling R$ 697,000. Preserve cost versus closing balance, ownership and current-year movements for the annual owner; this sum is not income or a filing-obligation test. Education evidence and contribution/payment records remain missing. No withholding is manufactured and no contribution ceiling, education cap or universal mixed-use percentage is assumed. Present these known, claimed and missing items together for correction before the structured handoff.

```oa-check
name: Retained fictional confirmation totals, no deduction eligibility assumed
inputs:
  candidate_rent: 14400
  candidate_mixed_phone_internet: 3600
  candidate_software: 4800
  candidate_supplies: 1200
  apartment_record_value: 450000
  vehicle_record_value: 85000
  bank_savings_record_balance: 42000
  investments_record_balance: 120000
steps:
  candidate_cost_total: candidate_rent + candidate_mixed_phone_internet + candidate_software + candidate_supplies
  recorded_asset_total: apartment_record_value + vehicle_record_value + bank_savings_record_balance + investments_record_balance
expected:
  candidate_cost_total: 24000
  recorded_asset_total: 697000
```

**Mixed-work route.** An employee also has a service business and foreign investments. Preserve the employment statement and PF/PJ distinction. Route contribution concurrency to `br-inss`, business regime to `br-simples-nacional` or the corporate owner, and foreign income to the foreign/annual owners. Do not refuse the whole intake because one component requires additional source work.

## When to refuse or refer

Refer the affected calculation where current sources or necessary facts are unavailable. Residence changes/nonresident/part-year issues go to cross-border and annual owners; someone never resident is not automatically a departure-return case. Lucro Real/Presumido, S.A. entities, import/export, special MEI/cargo activities, estates or foreign structures require the appropriate corporate/customs/specialist component. Do not infer that every S.A. is CVM-regulated. CLT-only facts go directly to the annual owner when this self-employment intake is unnecessary.

Continue clearly separable authorised preparation and document the boundary. Refuse to fabricate facts, treat unknown as paid, certify an unsupported deduction or make an unauthorised submission. A mere referral does not erase the affected topic from the package.

## Completion checklist

- Existing records and documents read before gap questions; no repeated questions or unavailable-tool dependency.
- Year/exercise, owner, residence dates, activity/regime/elections and applicable municipality identified or explicitly missing.
- PF/PJ payer and taxpayer-owner distinctions preserved; gross/net and transfer bridges reconcile without a universal monetary tolerance.
- Contributions, deductions, assets/debts and all former reform inputs retained with evidence and actual owner routes.
- Unknowns are not zero; unsupported percentages/constants and tax paid are not invented.
- Structured package, client corrections, partial components and next actions passed to assembly; required professional review is identified honestly.

## Sources

| Source and portion read | URL | Read on |
|---|---|---|
| RIR 2018 arts 68–69,685,714: necessary costs, restrictions, excess and PF/PJ withholding distinctions | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm |2026-11-11 |
| LC 123 arts 3,13–14,18,18-A/18-F: eligibility/start-year, employer CPP/ISS, activity/payroll, owner distributions and special MEI route | https://legis.senado.gov.br/norma/572878/publicacao/34621013 |2026-11-11 |
| Lei 15270 amendments to Lei 9249 art 10 and Lei 9250 annual/dividend rules; read for dated owner handoff, not duplicated computation | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm |2026-11-11 |
| RFB IRPF 2026 QA cover and Q427–434; published exercise 2026/calendar 2025, not a complete 2027 calendar | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf |2026-11-11 |
| LC 214 arts 343–348 and amendments to LC 123 art 13; reform duty/rate/election conditions, read in part | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm |2026-11-11 |
| Official NFS-e/CGSN169 explanation; read for existing MEI invoice duty and PF-customer distinction | https://www.gov.br/nfse/pt-br/noticias/resolucao-cgsn-no-169-traz-novos-beneficios-ao-mei |2026-11-11 |

Not yet confirmed: complete exercise 2027 annual-return publication/calendar/software fields; owner Guide gaps in ordinary income, municipal tax, social contribution categories and special MEI activities; universal mixed-use percentages; a registration-card-only tax-regime determination; exact portal download menus not read here. Such items remain partial or owner handoffs, not assumed exemptions or reasons to evict an entire ordinary taxpayer group.

## Talk to a verified accountant

Use the draft intake and evidence trail for professional review before filing or taking a tax position. Find Brazil Guides and professional-review options at [OpenAccountants](https://openaccountants.com). This Guide is **Not yet approved** and does not record accountant approval of the taxpayer's facts or return.
