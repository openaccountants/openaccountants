---
name: brazil-references
jurisdiction: BR
category: orchestrator
tax_year: 2026
last_updated: 2026-11-11
version: 1.1
type: router
description: >
  Brazil source-routing catalog for 2026 individual tax, investment records and related
  engineering research. Routes current tax calculations to the owning Brazil Guides and
  official Receita and Banco Central sources. Retains the four legacy investment-project
  identities, their documented scope and limitations, and source-code licence identities.
  Trigger on Brazil tax sources, IRPF references, GCAP, B3 CEI consolidation, investment
  cost software, irpf-investidor, ir_investidor, consolidador-cei and Leao Faminto API.
  Contains no independent operative tax-rate or deadline table. Excludes software security
  approval, current-calculation certification, licence compatibility approval and an
  exhaustive treatment of Brazilian exchange-traded investments.
tier: 2
domain: income-tax
---

# Brazil: official tax sources and investment-project references, 2026 v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Use the owning Guide and the actual official original for a tax result. The four project links below help investigate historic investment-record workflows. Their tax constants, supported formats and output are not evidence that a 2026 calculation is correct. A source-code licence identity does not establish compatibility for a proposed integration.

## Ask the client first

Read the existing record before asking for the missing year, residence, investment type, actual broker/custodian, transaction files, intended output and any proposed software reuse. Distinguish an income-tax question from data consolidation or a code-licensing question. Do not ask for portal credentials to evaluate this catalog.

## Choose the owning Guide and official original

| Job | Owning Guide | Official source to open and read for that job |
|---|---|---|
| Personal annual income tax and the distinction between calendar year and filing exercise | [br-income-tax](br-income-tax.md); [br-return-assembly](br-return-assembly.md) for preparation | [Receita 2026 tables](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026) and the [exercise 2026 Q&A](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf). The latter identifies its filing exercise; it is not a future filing calendar |
| Monthly personal income, qualifying foreign work receipts, livro-caixa and tax payments | [br-estimated-tax](br-estimated-tax.md); [br-inss](br-inss.md) for contributions | [Official Apurar Carnê-Leão service](https://www.gov.br/pt-br/servicos/apurar-carne-leao/); use the owner's separate contribution sources rather than an investment application's defaults |
| Ordinary capital-gain computation and program selection | [br-income-tax](br-income-tax.md); [brazil-crypto-tax](brazil-crypto-tax.md) for its supported digital-asset cases | [Official GCAP directory](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/download/pgd/gcap). Select the actual calendar-year program and distinguish an ordinary capital gain from a foreign financial application |
| Foreign financial investments, tax residence and foreign reporting | [brazil-cross-border-tax](brazil-cross-border-tax.md), with the annual owner | [Current IN RFB 2.180](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente), relevant asset/income provisions; [BCB CBE service](https://www.gov.br/pt-br/servicos/preencher-declaracao-de-capitais-brasileiros-no-exterior) for its separate reporting test |
| Digital-asset tax and dated information reporting | [brazil-crypto-tax](brazil-crypto-tax.md) | [Current IN RFB 2.291 / DeCripto](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709). Read its commencement and scope; a project using the old reporting model is not current authority |
| Stocks, options, ETFs, FIIs, normal trading and day trading outside a supported owner calculation | Start with the annual owner and the actual transaction documents | Use the relevant subject in the [official Q&A](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf) as a research index, then the operative law for the year. This catalog does not certify complete exchange-market computations |

## Legacy projects: documented scope and limits

These are the same four project identities retained from the earlier catalog. The descriptions below report what their authors document, not a finding that the software currently produces a correct tax result. No code was installed, executed, integrated or audited for this update. Star counts are omitted because they do not establish correctness or continued maintenance.

| Project and original repository | Documented scope and important limits | Source-code licence identity and access record |
|---|---|---|
| [staticdev/irpf-investidor](https://github.com/staticdev/irpf-investidor) | Its Portuguese README describes costs for stocks, ETFs and FIIs, including emoluments, settlement fees and asset-declaration cost records. It expressly limits its tested tariff years to 2019-2022, excludes day trading, futures and the stated index, and says new XLSX exports are unsupported. B3/CEI import patterns are engineering research; do not directly reuse old tariffs for 2026 | [README](https://github.com/staticdev/irpf-investidor/blob/main/README.md) and [LICENSE](https://github.com/staticdev/irpf-investidor/blob/main/LICENSE) read. MIT-style permission text; repository metadata labels MIT and marks the repository archived |
| [barbolo/ir_investidor](https://github.com/barbolo/ir_investidor) | Its Portuguese README describes local Docker execution for variable-income tax and lists stocks, options, FIIs and subscriptions, with normal/day-trade categories where shown. It describes a Clear brokerage-note conversion script. Its assumptions are the project's assumptions, including the stated omission of settlement dates; they are not copied into this catalog as tax law | [README](https://github.com/barbolo/ir_investidor/blob/master/README.md) and [LICENSE](https://github.com/barbolo/ir_investidor/blob/master/LICENSE) read. MIT licence text; repository metadata marks it archived |
| [danilofrp/consolidador-cei](https://github.com/danilofrp/consolidador-cei) | Its Portuguese README describes consolidation of B3 CEI exports, positions, transaction history, asset reports and monthly realized results. It warns that overlapping input dates duplicate transactions and that options/exercise functionality was disabled after its refactor. Its earnings worksheet is expressly for checking, rather than a source for the tax return. These limits qualify the old consolidation/integration suggestion | [README](https://github.com/danilofrp/consolidador-cei/blob/master/README.md) read; [LICENSE](https://github.com/danilofrp/consolidador-cei/blob/master/LICENSE) title identifies GNU GPL version 3. Licence identity only; no compatibility or redistribution approval |
| [jeancsanchez/leaofaminto-api-kt](https://github.com/jeancsanchez/leaofaminto-api-kt) / Leão Faminto API | Its Portuguese README describes stock-market record consolidation and IRPF support. Stocks and FIIs normal/day-trade calculations and CEI XLS integration are checked features; US stocks, REITs and the general annual-return report are unchecked desired features. The old catalog incorrectly presented US stocks/REITs as supported. Treat its Kotlin API/data patterns as research, not a current calculation service | [README](https://github.com/jeancsanchez/leaofaminto-api-kt/blob/dev/README.md) and [LICENSE.md](https://github.com/jeancsanchez/leaofaminto-api-kt/blob/dev/LICENSE.md) read. MIT licence text; repository metadata marks it archived |

## The method, step by step

1. Identify the exact tax year, asset, event, custody, output and owner. Preserve raw broker files and explain any missing acquisition records or duplicate transactions before using a tool's totals.
2. Open the official original and the owner Guide. Record the rule, period, conditions and read date. Use the project's README to understand its data assumptions, not to establish the law.
3. For an engineering investigation, pin the actual revision, examine the current file format and keep test data separate from real taxpayer records. A successful import does not prove basis, loss offsets or tax payment.
4. If reusing code, inspect the actual licence files, dependencies and proposed distribution. The old statement that all projects have compatible licences is withdrawn; this catalog gives no legal compatibility opinion.
5. Reconcile any proposed output against source documents and the supported owner calculation before a taxpayer-specific handoff. A catalog entry does not authorize installation, access to taxpayer accounts or filing.

## When to refuse or refer

Withhold a tax result where the year, asset or supporting transaction record is missing. Refer an unsupported exchange-market or specialist calculation to the owner and its primary law. Do not approve software reuse from this catalog: dependency licensing, security and proposed distribution need their own actual review. A source cited as an index is not an assertion that every linked rule was read.

## Sources

| Source and portion actually read | URL | Read on |
|---|---|---|
| Read for Receita 2026 tables, monthly/annual headings and dated tables; catalog routes to owner rather than repeating figures | https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026 | 2026-11-11 |
| Exercise 2026 Q&A actual v1.03: cover, selected Q266-272, Q427,433-434,436,441,444-445,473,653 used in the owner research; other subjects are index referrals, not read/verified computations | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf | 2026-11-11 |
| Read for official Apurar Carnê-Leão service, stated purpose and access workflow | https://www.gov.br/pt-br/servicos/apurar-carne-leao/ | 2026-11-11 |
| Read for official GCAP directory, stated calculation/payment/import purpose and calendar-year entries | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/download/pgd/gcap | 2026-11-11 |
| IN2180 arts2 and8-12, asset classification and foreign-financial regime; other provisions not represented as a whole-law read | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente | 2026-11-11 |
| IN2291 arts1-19 and AnnexI definitions, current DeCripto scope and phased effect | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709 | 2026-11-11 |
| Read for BCB-owned CBE service, purpose, reporting-test and steps; full case calculation belongs to owner | https://www.gov.br/pt-br/servicos/preencher-declaracao-de-capitais-brasileiros-no-exterior | 2026-11-11 |
| Read for irpf-investidor author README, complete text including historical tariff/format limits; licence text and repository metadata | https://github.com/staticdev/irpf-investidor/blob/main/README.md | 2026-11-11 |
| Read for ir_investidor author README, complete text including features/assumptions; licence text and repository metadata | https://github.com/barbolo/ir_investidor/blob/master/README.md | 2026-11-11 |
| Read for consolidador-cei author README, complete text including disabled options/checking-only earnings; licence title and repository metadata | https://github.com/danilofrp/consolidador-cei/blob/master/README.md | 2026-11-11 |
| Read for Leão Faminto author README, complete text and checked/unchecked feature list; licence text and repository metadata | https://github.com/jeancsanchez/leaofaminto-api-kt/blob/dev/README.md | 2026-11-11 |

Not yet confirmed: complete current stocks/options/ETF/FII/day-trade taxation; correctness or security of any project's output; support for current broker exports beyond its documented claims; live API availability; complete dependency licensing and compatibility for any proposed use. No tax computation or zero-tax conclusion is supplied by this router. Read the actual owner and primary rule for the requested year; do not fill a gap from a third-party constant.
