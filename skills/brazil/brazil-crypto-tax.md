---
name: brazil-crypto-tax
description: >
  Prepare Brazilian resident individuals' 2026 crypto tax working papers and reporting
  handoffs. Distinguish domestic capital gains from qualifying foreign financial
  assets, identify disposal and receipt events, reconcile acquisition evidence and
  apply the dated IN 1888 to DeCripto transition. Covers Bitcoin, altcoins,
  stablecoins, NFT classification, domestic custodial lending, swaps, annual asset
  reporting, loss restrictions, reporting penalties and corrections. Trigger on
  Brazil crypto tax, criptoativos, Bitcoin, GCAP, DARF 4600, IN 1888, DeCripto,
  foreign exchange holdings, staking, mining, airdrops or NFT tax. Gives explicit
  unresolved treatment for unsupported native DeFi and cost-method questions;
  it does not assume every digital asset or yield product has the same tax regime.
jurisdiction: BR
category: crypto
domain: tax
tax_year: 2026
tier: 2
last_updated: 2026-11-11
version: 1.1
type: situation-rules
depends_on:
  - br-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Brazil crypto tax v 1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Brazilian tax-resident individuals preparing calendar-year 2026 crypto records. Determine the asset's nature, custody/negotiation location and event before calculating. Domestic disposal gains, qualifying foreign financial income, remuneration and information reporting are separate jobs. A platform's brand, a foreign issuer or a foreign blockchain server does not establish the tax location. [IN 2180 arts 2,9–12](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente).

The output is a transaction schedule, documented basis reconciliation, separate tax/reporting calculations and an annual-return handoff. Company trading, a change of residence, foreign controlled entities/trusts and state gift tax require the corresponding owner Guide; continue the separable individual work. Ordinary native staking, mining, NFT creation and DeFi cases remain partial where the missing treatments listed in Sources affect the answer.

First obtain the year/residency dates; asset rights; actual provider/legal entity and custody history; complete buys, sales, swaps, receipts and transfers; and cost/payment evidence. Do not infer a zero cost from a missing statement. The detailed input list appears below.

## Rates, bands and thresholds

| Item and conditions | Amount / period | Official source and exact anchor |
|---|---|---|
| Domestic custody/negotiation: gain exemption tests the aggregate monthly disposal proceeds of all crypto species, not the gain or a separate limit per exchange | Total disposals ≤R$ 35,000; above the limit, the taxable gain is not reduced by R$ 35,000 | [SC 184 conclusion 28(c)](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/138933): “de todas as espécies de criptoativos”; “igual ou inferior a R$ 35.000,00” |
| Ordinary taxable capital gain, marginal band |15% on gain up to R$ 5 million | [Lei 8981 art 21 I](https://www.planalto.gov.br/ccivil_03/leis/l8981.htm#art21): “sobre a parcela dos ganhos que não ultrapassar R$ 5.000.000,00” |
| Ordinary taxable capital gain, next marginal band |17.5% on gain above R$ 5 million up to R$ 10 million | [Lei 8981 art 21 II](https://www.planalto.gov.br/ccivil_03/leis/l8981.htm#art21): “exceder R$ 5.000.000,00”; “não ultrapassar R$ 10.000.000,00” |
| Ordinary taxable capital gain, next marginal band |20% on gain above R$ 10 million up to R$ 30 million | [Lei 8981 art 21 III](https://www.planalto.gov.br/ccivil_03/leis/l8981.htm#art21): “exceder R$ 10.000.000,00”; “não ultrapassar R$ 30.000.000,00” |
| Ordinary taxable capital gain, top marginal band |22.5% on gain above R$ 30 million | [Lei 8981 art 21 IV](https://www.planalto.gov.br/ccivil_03/leis/l8981.htm#art21): “ultrapassar R$ 30.000.000,00” |
| Resident PF's qualifying foreign financial-asset income, realized under the cash rules |15% in the annual DAA; the domestic small-disposal exemption does not apply | [Lei 14754 arts 2–3](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm), [IN 2180 arts 9–10](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente): “à alíquota de 15%”; “não se aplicando nenhuma dedução da base de cálculo” |
| Annual asset entry, distinct from the obligation to file the entire return | Group 08 entry when acquisition value of each crypto type is ≥R$ 5,000; use the applicable exercise's form | [RFB 2026 Q 473](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf): “de cada tipo de criptoativo”; “igual ou superior a R$ 5.000,00” |
| Historical information reporting: resident user with foreign exchange/no-exchange operations | January–June 2026 monthly operations >R$ 30,000; Brazilian exchange has its own reporting duty | [IN 1888 art 6](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/100592/visao/multivigente), [IN 2291 arts 18–19](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709): “ultrapassar R$ 30.000,00” |
| DeCripto resident user: foreign provider, decentralised platform or no provider | July–December 2026 monthly operations >R$ 35,000 | [IN 2291 art 5 II/§3 and art 19](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709): “for maior que R$ 35.000,00” |

## The base

### Classify the asset, location and event

1. Identify the legal/economic rights. A virtual asset that represents another financial investment, or whose nature/characteristics meet that definition, can be a financial application. BTC is generally in that class; an artwork NFT is not automatically financial. Do not default an unidentified token to either class. [IN 2180 art 9§1](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente), [official foreign-income FAQ Q 18](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2024/abril/receita-federal-e-secretaria-da-reforma-tributaria-lancam-atualizacao-do-perguntas-e-respostas-sobre-tributacao-de-rendimentos-no-exterior/perguntas-e-respostas-offshores-lei-14-754-e-in-rfb-2-180.pdf).
2. Custody or negotiation by an institution abroad establishes foreign location for this test, independently of the issuer's location. Self-custody by a Brazilian resident without an intermediary is not foreign solely because of the network's location. Record changes in custody and the provider's actual domicile. [IN 2180 art 9§2](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente), [official FAQ Q 19](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2024/abril/receita-federal-e-secretaria-da-reforma-tributaria-lancam-atualizacao-do-perguntas-e-respostas-sobre-tributacao-de-rendimentos-no-exterior/perguntas-e-respostas-offshores-lei-14-754-e-in-rfb-2-180.pdf).
3. Identify sales, swaps, payment for goods/services, rewards, gifts, inheritance and own-wallet transfers separately. A swap can dispose of an asset without fiat cash-out. An own-wallet transfer must reconcile ownership and basis; its reporting classification is a separate question. [SC 184 conclusion 28(b)](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/138933), [IN 2291 arts 6,16](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709).

### Domestic ordinary disposal calculation

Reconcile quantity, documented BRL acquisition cost and disposal value for each transaction. Ordinary gain is the positive difference between proceeds and acquisition cost; non-cash disposal value is market value. Document any commission/cost included and the applicable legal condition. Do not silently impose a universal averaging method or treat every network fee as deductible. Missing basis/method blocks that transaction's final calculation, while other reconciled transactions can proceed. [IN 84 arts 2,5,17–19](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/14400/visao/vigente).

Aggregate monthly disposal proceeds for the exemption test. For taxable gains apply the marginal bands above. If parts of the same asset/right are sold, check the aggregation rule from the second disposal through the end of the calendar year following the first and deduct prior tax as prescribed; do not restart a marginal band for each fragment. [SC 184 conclusion 28](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/138933), [Lei 8981 art 21§§3–4](https://www.planalto.gov.br/ccivil_03/leis/l8981.htm#art21).

Ordinary capital losses cannot offset gains on another disposal, even in the same month: “O prejuízo apurado em uma alienação não pode ser compensado com ganhos obtidos em outra”. Keep losing transactions in the reconciliation, without turning them into an ordinary monthly/future credit. [IN 84 art 2 sole paragraph](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/14400/visao/vigente).

### Qualifying foreign financial assets

Record BRL income realized on receipt of remuneration and on redemption, amortisation, disposal, maturity or liquidation, including exchange variation on principal. Apply the annual 15% regime separately from the ordinary progressive return. Convert using the BCB closing sale quotation for the taxable event unless a specific statutory rule differs. Foreign nonfinancial assets remain under the specific capital-gain rules, rather than being forced into this financial regime. [Lei 14754 arts 2–3,15](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm), [IN 2180 arts 2,9–10](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente).

Documented realized foreign financial losses can offset foreign financial income in the same annual period, then qualifying controlled-entity profits/dividends included that period; unused losses carry to subsequent eligible periods. Use losses only once, at nominal value. This is not the domestic loss rule. [Lei 14754 art 9](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm), [IN 2180 art 11](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente).

Foreign tax credit requires treaty/reciprocity, the applicable per-income ceiling and tax not refundable/creditable abroad. It cannot be carried to earlier/later years or used indiscriminately against other investments. Foreign tax paid is converted with the BCB closing purchase quotation on payment date. Hand the resulting income/loss/credit schedule to `br-income-tax` for the complete annual reconciliation, including any applicable high-income rules. [Lei 14754 art 4](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm), [IN 2180 art 12](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente).

### Receipts, lending and special events

| Event | Supported treatment or required distinction | Official source |
|---|---|---|
| Remuneration for fungible crypto lent to a Brazilian PJ custodian | Exclusive-source IRRF, withheld by the payer in the receipt month, at market value even without cash withdrawal. The fixed-income holding-period rates apply to this fact pattern, not automatically to every protocol called staking. Obtain term/contract and withholding evidence. | [SC 184 scope 7–9, discussion 19–24, conclusion 28(a)](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/138933) |
| Payment for professional services in crypto | Separate service income at receipt from later asset disposal; route payer/residency/withholding facts to `br-income-tax` and monthly-income owner. A subsequent sale is not the first and only event. | [RIR 2018 art 47 IV](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm) |
| Gift/inheritance transfer | ITCMD and income tax are separate. A transfer above the donor/estate's declared cost can create taxable capital gain; recipient basis follows the chosen transfer value and supporting returns. Obtain transfer valuation and state. | [IN 84 art 20](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/14400/visao/vigente) |
| Native staking, mining, airdrop/fork, lending to other counterparties, liquidity pools, wrapping/bridging, farming, NFT creation | Preserve each receipt/disposal and evidence; obtain the legal nature and counterparty. Do not assign the unsupported universal tax/basis answers removed from the old version. The specific missing treatments are listed in Sources. | [IN 2291 art 16](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709): reporting follows specific taxation law |

## Deadlines and filing

### Tax payment and annual handoff

For ordinary resident capital gains, prepare the applicable year's GCAP calculation and DARF 4600 by the last business day of the month following receipt of the gain. Reconcile instalment receipts rather than taxing an assumed receipt date. These gains are separate from ordinary annual taxable income and the tax is not a general annual-return credit. Qualifying foreign financial income instead goes to the annual DAA regime. [Lei 8981 art 21§§1–2](https://www.planalto.gov.br/ccivil_03/leis/l8981.htm#art21), [IN 84 arts 30–31](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/14400/visao/vigente), [RFB Q 653](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

Prepare the GCAP transaction schedule, then use the official year's program and tax-payment service; retain the saved calculation, generated payment document and payment receipt, and match them to the annual import/handoff. Start at the [official GCAP directory](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/download/pgd/gcap), select the applicable year and retain its calculation/payment output.

Annual holdings: use acquisition values, quantity, asset type and custody details. The published exercise 2026 instructions use Group 08 codes 01 BTC,02 other cryptocurrencies,03 stablecoins,10 NFTs and 99 other cryptoassets. Preserve per-type records and the local country/foreign income-or-loss/foreign tax fields where applicable. After a full disposal, reconcile the actual closing quantity to zero and retain the disposal history; the annual owner must apply the published form rules instead of deleting the historical acquisition/disposal trail. Also hand off crypto-related loans, debts and liabilities with counterparty, balance and security/repayment evidence; this Guide does not establish their annual entry codes or thresholds. This reference does not assert that exercise 2027 software, boxes or its filing deadline have already been issued; use `br-income-tax` for the complete return obligation and current filing procedure. [RFB Q 473](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf).

### Separate information reporting by period

| Period / filer | What is reported and when | Official source |
|---|---|---|
| January–June 2026 resident users within the old threshold test | IN 1888 operations reporting; use the historical applicable layout, not the DeCripto file for an old period | [IN 1888 arts 6–9](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/100592/visao/multivigente), [IN 2291 arts 18–19](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709) |
| July–December 2026 DeCripto users | Monthly by the last business day of the following calendar month, closing 23:59:59 Brasília; art 9 information for reportable art 6 I–VII operations | [IN 2291 arts 5,9,12,19](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709) |
| Providers under the Brazilian nexus tests | Individualised art 7 reporting from July 2026; annual art 8 CARF reporting applies from January 2026. Annual balances/CARF are due by the last business day of January of the next year; art 8 CARF relief below is conditional | [IN 2291 arts 5,7–8,12,19](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709) |

For the provider's annual CARF duty only, art 8§1 relieves the specified nexus cases after qualifying partner-jurisdiction compliance: art 5 I(b)–(d) where tax-resident there; (c)/(d) through the corresponding (b) link; (d) through the corresponding (c) link; and (d) for a tax-resident individual. For art 5 I(a)–(d), compliance under substantially similar partner rules also requires notification to Receita. Art 8§2 separately relieves operations through a branch that fulfilled the duty in a partner jurisdiction. Verify the applicable nexus/compliance evidence rather than assuming every foreign provider is exempt. These are exceptions to the art 8 provider duty; they do not eliminate the Brazilian user's independent art 5 II/art 9 duty. [IN 2291 art 8§§1–2](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709).

Provider scope includes Brazilian tax residence/constitution/management/business and the specified provision of services in Brazil; art 5§1 defines .br domains, local collection/payment arrangements and targeted advertising. A foreign provider's duty does not, by itself, erase the resident user's art 5 II duty. [IN 2291 art 5](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709).

DeCripto includes buys/sales/swaps; transfers such as airdrop/staking/mining/loans and goods/services; transfer to unhosted wallets; involuntary loss; and provider-specific asset-reference operations. The greater-than-USD 50,000 retail-payment category is an operation classification, not a blanket reporting exemption for smaller payments. For users, capture art 9 identity, tax residence/NIF where applicable, asset/quantity, BRL value excluding service fees, fees separately and provider/platform. For an indivisible smart-contract sequence, art 9 permits the specified atomic-transaction hash alternative. [IN 2291 arts 6–9](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709).

For reporting, value fair value under art 10; convert foreign currency to USD then BRL using closing PTAX sale quotation on the operation/balance date under art 11. These reporting valuation methods do not establish a universal income-tax cost method. [IN 2291 arts 10–11](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709).

Prepare the period's UTF-8 pipe-delimited file in the approved layout using the corresponding manual sections for provider, foreign-provider user or no-provider user. Access RFB's Coleta Nacional through e-CAC, select the crypto reporting obligation and correct period, validate, resolve errors, transmit only within the user's filing authority, then retain the transmitted file, receipt and records. A digital signature is required when e-CAC requires it. Wallet sending/receiving addresses are mandatory only upon the specified fiscal-procedure summons. The downloaded current manual is version 1.01, with the August 2026 large-file update; do not assume its old v 1 URL means its first edition. [IN 2291 arts 3–4,12,17](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709), [official manual pp 7–9 and sections 5–6](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/manuais/manual-orientacao-leiaute-criptoativos/manual-de-orientacao-do-leiaute-da-decripto-v1.pdf).

## Penalties and interest

| DeCripto infringement and filer | Penalty / condition | Official source |
|---|---|---|
| Late PF reporting | R$ 100 per month or fraction | [IN 2291 art 13 I(c)](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709) |
| Late reporting, specified entities starting activity, immune/exempt, Simples, or last-return lucro presumido | R$ 500 per month or fraction; art 13§3 switches the stated multiple-method/reorganisation cases to the other entity rate | [IN 2291 art 13 I(a)/§3](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709) |
| Other late entity reporting | R$ 1,500 per month or fraction | [IN 2291 art 13 I(b)](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709) |
| Inaccurate/incomplete/incorrect/omitted information | Entity 3% of the affected operation, minimum R$ 100; PF 1.5% of the affected operation | [IN 2291 art 13 II](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709) |
| Failure to comply with RFB summons within its stipulated period | R$ 500 per calendar month | [IN 2291 art 13 III](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709) |
| Reductions and correction | Late-reporting fine halves if fulfilled before an official procedure; entity misinformation fine reduces 70% for Simples. Errors corrected before an official procedure escape the error/omission fine under art 15, not automatically the late-reporting fine | [IN 2291 art 13§§1–2/art 15](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709) |

For January–June historical infringements use the old rule's applicable art 10–12, not a new penalty mechanically applied backwards. Late tax payment is also separate from late reporting: route the original liability, payment date and official updated payment calculation to `br-estimated-tax` for the pack's shared late-payment rule, with `br-income-tax` for the annual bridge; do not combine a reporting fine with a tax-payment charge. Historical IN 1888 guidance in RFB Q473 identifies reporting-fine DARF revenue code 5720. This does not establish the current DeCripto fine-payment code, which remains unconfirmed. [RFB Q473](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf). [IN 1888 arts 10–12](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/100592/visao/multivigente), [IN 2291 arts 13–19](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709).

## Cross-border points

Keep the three tests separate: asset location/nature for tax; provider/user scope for information reporting; aggregate foreign holdings for BCB CBE. Load `brazil-cross-border-tax` for CBE, residence, controlled entities, trusts and treaty questions. Use the official [CBE service](https://www.gov.br/pt-br/servicos/preencher-declaracao-de-capitais-brasileiros-no-exterior) for its current threshold/date tests; a crypto tax exemption is not a CBE exemption.

Law 14478's virtual-asset framework is not proof that a provider is currently licensed, nor does reporting make a transaction tax exempt. Do not apply corporate transfer-pricing law to every individual's crypto transaction or claim that all asset sales in separate months are automatically aggregated as avoidance. Record ownership, counterparties, valuations and transaction history, and refer the specific disputed classification. [IN 2291 art 16](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709).

## Two worked examples that recompute

**1. Domestic threshold decision, with another crypto disposal.** Assume a resident's documented single-lot domestic sale has proceeds R$ 30,000 and cost R$ 20,000; no other disposals means R$ 10,000 gain is exempt. Alternatively, another domestic crypto sale that month has proceeds R$ 10,000/cost R$ 8,000. Total proceeds R$ 40,000 exceed the limit, so both positive gains are taxable: R$ 12,000 × 15%=R$ 1,800. No losses, special aggregation or costs are assumed. This is a classification/compliance comparison, not a recommendation to split transactions artificially. Information reporting still requires its separate operations test. [SC 184 conclusion 28](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/138933), [Lei 8981 art 21](https://www.planalto.gov.br/ccivil_03/leis/l8981.htm#art21).

```oa-check
name: Domestic threshold with another crypto sale
inputs:
  sale_a: 30000
  cost_a: 20000
  sale_b: 10000
  cost_b: 8000
steps:
  gain_a: sale_a - cost_a
  proceeds_both: sale_a + sale_b
  gains_both: gain_a + sale_b - cost_b
  tax_both: gains_both * 0.15
expected:
  gain_a: 10000
  proceeds_both: 40000
  gains_both: 12000
  tax_both: 1800
```

**2. Foreign annual financial regime with a documented loss.** Assume qualifying foreign financial crypto held by a foreign institution, all values already correctly established in BRL. Sales R$ 50,000+R$ 15,000 less costs R$ 30,000+R$ 8,000 give R$ 27,000 realized gains. A separately documented eligible foreign financial loss R$ 7,000 in the same annual period leaves R$ 20,000;15% tax is R$ 3,000 before any eligible foreign tax credit and the full annual-return reconciliation. It is not monthly GCAP/DARF 4600 and the domestic proceeds exemption is not used. The loss would not be netted against another disposal under the domestic ordinary regime. [Lei 14754 arts 2–3,9](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm), [IN 2180 arts 10–11](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente).

```oa-check
name: Foreign financial crypto annual loss
inputs:
  sale_a: 50000
  sale_b: 15000
  cost_a: 30000
  cost_b: 8000
  eligible_loss: 7000
steps:
  gross_gains: sale_a + sale_b - cost_a - cost_b
  annual_net: gross_gains - eligible_loss
  annual_tax_before_credit: annual_net * 0.15
expected:
  gross_gains: 27000
  annual_net: 20000
  annual_tax_before_credit: 3000
```

### Retained staking scenario with an unresolved tax result

The old scenario is retained as a fact pattern: a resident receives 1 ETH in rewards with total market value of R$ 10,000 at receipt dates, then sells that ETH domestically for R$ 12,000. If a separately verified legal basis were R$ 10,000, the subtraction would be R$ 2,000. The contract, custodian, counterparty and reward mechanism are missing, so receipt taxation and acquisition basis are unresolved. Do not certify the old zero-tax answer or assume that every receipt is the Brazilian custodial-lending case in SC 184. Confirm other disposals in that sale month as well. Keep receipt and disposal schedules while the affected classification is referred. [SC 184 scope 7–9 and conclusion 28(a)](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/138933).

```oa-check
name: Retained staking scenario arithmetic only, basis unresolved
inputs:
  reward_eth: 1
  receipt_market_values_total: 10000
  sale_proceeds: 12000
  assumed_basis_for_subtraction_only: 10000
steps:
  conditional_difference: sale_proceeds - assumed_basis_for_subtraction_only
  closing_quantity_after_full_sale: reward_eth - reward_eth
expected:
  conditional_difference: 2000
  closing_quantity_after_full_sale: 0
```

## Ask the client first

Use the existing record/documents before asking for these six fact groups:

1. Calendar year, residence changes, owner/entity and any foreign controlled entity/trust involvement.
2. Asset rights/type and actual custody/provider domicile, including self-custody and migrations.
3. Complete dated buys, disposals, swaps, transfers and receipts across all wallets/providers, with transaction hashes.
4. Quantities, acquisition/basis records, currency conversion evidence, fees and records explaining missing/transferred lots.
5. Reward/lending/service/gift/inheritance contracts, receipt valuations, holding periods and withholding evidence.
6. Prior reports/returns, eligible loss/foreign-credit records, payments, notices and corrections already submitted.

Reconcile opening quantity+receipts−outflows=closing quantity for each asset and account; match own transfers on both sides. Preserve bank/fiat and exchange ledgers separately, then bridge them without treating every bank deposit as a new taxable gain. Before completion verify the domestic/foreign split, exemption aggregation, loss restrictions, dated reporting regime, filing/payment receipts and open gaps. Missing facts block only the dependent output. No filing/payment is implied by preparing working papers.

## Sources

| Source and portion read | URL | Read on |
|---|---|---|
| Lei 14754, arts 2–4,9,15,47: annual foreign financial income, losses, FX and effective dates | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm |2026-11-11 |
| IN 2180, current original structured text; arts 2,8–12: classification, location, annual rate, losses and credits | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136603/visao/multivigente |2026-11-11 |
| SC 184,24 June 2024; ementas, facts 7–9, discussion 19–24 and conclusion 28 | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/138933 |2026-11-11 |
| Lei 8981 current art 21 including marginal bands and partial-disposal aggregation | https://www.planalto.gov.br/ccivil_03/leis/l8981.htm#art21 |2026-11-11 |
| IN 84 current arts 2,5,17–20,30–31: ordinary gain, costs, non-cash values, gifts, payment | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/14400/visao/vigente |2026-11-11 |
| IN 1888 historical reporting main articles; repeal/effects checked against IN 2291 | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/100592/visao/multivigente |2026-11-11 |
| IN 2291 main arts 1–19 and AnnexI definitions: reporting, dates, fees/FX, penalties and corrections | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/147709 |2026-11-11 |
| DeCripto manual actualv 1.01: version table,pp 7–9, operation tables and user sections 5–6 | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/manuais/manual-orientacao-leiaute-criptoativos/manual-de-orientacao-do-leiaute-da-decripto-v1.pdf |2026-11-11 |
| RFB official foreign-income FAQ Q 18–20: asset nature/self-custody; complements IN 2180 | https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2024/abril/receita-federal-e-secretaria-da-reforma-tributaria-lancam-atualizacao-do-perguntas-e-respostas-sobre-tributacao-de-rendimentos-no-exterior/perguntas-e-respostas-offshores-lei-14-754-e-in-rfb-2-180.pdf |2026-11-11 |
| RFB exercise 2026 QA actualv 1.03, Q 473/653; calendar 2025 form references only, with noted inconsistency below | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirpf/p-r-irpf-2026-v1-00-2026-04-23.pdf |2026-11-11 |
| RIR 2018 art 47 IV, remuneration in assets | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm |2026-11-11 |
| RFB GCAP directory, applicable-year program entries and stated calculation purpose | https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/download/pgd/gcap |2026-11-11 |
| BCB-owned CBE service, trigger paragraphs; owner Guide handles full CBE computation/calendar | https://www.gov.br/pt-br/servicos/preencher-declaracao-de-capitais-brasileiros-no-exterior |2026-11-11 |

RFB Q 653 retains a progressive-rate warning inside its current foreign-financial subsection. Apply Lei 14754/IN 2180's annual 15% to qualifying foreign financial assets, rather than copying that inconsistent warning. Its old IN 1888 procedure is also not the July 2026 DeCripto procedure.

Not yet confirmed: current DeCripto reporting-fine payment code (historical IN1888 code5720 is not assumed current); universal crypto weighted-average, identification, FIFO or LIFO; all gas/transfer-fee and self-transfer basis adjustments; native protocol staking; mining receipt/cost/professional-MEI treatment; pure airdrop and hardfork basis; liquidity-pool entry/exit, wrapping, bridging, farming and liquidation; NFT creator/business treatment and NFT royalty income/basis/withholding; annual crypto-related debt/liability entry rules; lost keys/theft losses; decentralised arrangements' tax location beyond the stated institution/self-custody cases; state-specific ITCMD; current BCB provider-licensing requirements and the old framework's commencement/decree details; scope of CTN 116 and interposed-person/trust anti-avoidance assertions beyond the sourced foreign-tax regimes; any blanket CBS/IBS exclusion; a general artificial-monthly-sales aggregation rule; exercise 2027 annual-return boxes/software/deadline. Refer affected components and continue verified ordinary work; do not invent these answers.

Find the Brazil Guide library and professional-review options at [OpenAccountants](https://openaccountants.com). This draft's source-cited status does not itself attest a taxpayer's return.
