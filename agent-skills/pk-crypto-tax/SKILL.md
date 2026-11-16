---
name: pk-crypto-tax
description: "Use for pakistan virtual assets and tax evidence. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pk-crypto-tax"
  jurisdiction: "PK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Pakistan virtual assets and tax evidence v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For Pakistan virtual-asset receipts, disposals and related business activity during 2026. Separate regulatory permission from income-tax classification. The earlier suggestion that a regulator was merely being established is stale: the Virtual Assets Act, 2026 and PVARA framework now exist. This skill reconstructs records and flags unresolved taxation; it does not invent a crypto tax rate or certify a provider.

## Ask the client first

Obtain transaction dates, residence, business/investment purpose, type of token/activity, wallet and exchange records, acquisition evidence, fees, PKR conversion evidence, transfers between own wallets, and provider licensing category. For export compensation obtain contracts and authorised-dealer/e-PRC evidence; crypto receipt alone does not establish the s.154A concession.

## The method, step by step

1. Establish what occurred: payment for work, investment disposal, mining/staking reward or an own-wallet transfer. Preserve gross receipts, costs, dates and fees without assuming these all have the same tax character.
2. Check the regulatory period. The SBP's earlier restrictions are historical context. Its May 2026 circular permits bank relationships with PVARA-licensed VASPs subject to controls; an NOC-only entity has limited-purpose access before licensing. Regulated entities may not invest, trade or hold virtual assets using their own funds/customer deposits. [SBP circular paragraphs 2-7](https://www.sbp.org.pk/circulars/bprd-circular-letter-no-10).
3. Check the actual provider/category against PVARA's public register. A license is activity-specific; a listed asset is not guaranteed or endorsed by PVARA. [PVARA FAQ A.3-4/B.5-7](https://pvara.gov.pk/faq).
4. Prepare the evidenced transaction schedule. Business income, capital gains and other-source treatment must be tested under the Income Tax Ordinance for the facts; no cited FBR ruling establishes the old claim that all crypto disposals have been capital gains since 2023. Refer that classification before producing tax due. [ITO ss.18,37,39](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf).
5. For IT export pay, separately test the authorised-dealer realisation and compliance conditions in `pk-it-export-tax`; never recommend crypto or informal channels to avoid tax or banking rules. [ITO s.154A](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf).

## Rates, bands and thresholds

| Question | Confirmed boundary | Source |
|---|---|---|
| Dedicated crypto tax rate | No rate is adopted in this skill; regulatory licensing does not decide an individual's income-tax rate | [ITO ss.18,37,39](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf) |
| PVARA framework timing | The Services and Activity Specific Regulations were notified on 21 August 2026; apply the actual transaction-period framework | [PVARA FAQ A.1-2](https://pvara.gov.pk/faq) |

## Boundary and exception table

| Situation | Required treatment |
|---|---|
| Historical SBP prohibition cited | Do not present the earlier banking position as the whole current regime; inspect the May 2026 circular and its conditions |
| Own-wallet transfer | Reconcile ownership and transaction IDs before treating it as proceeds; do not double count it as a sale |
| Dedicated tax rate or binding classification requested | Refer for a current statutory/FBR position; no guessed rate or settled treatment |
| VASP, custody, exchange or other regulated business | Refer licensing/AML compliance to the applicable PVARA regime; ordinary investor records do not authorise that business |
| Export income in crypto | Preserve the receipt; do not certify the banking-channel concession from a token transfer |

## Worked cases

These recompute documented economic amounts only, not taxable gains or tax liability. Classification, deductible costs and conversion evidence still require review.

```oa-check
name: Documented disposal proceeds and economic difference
inputs:
  documented_proceeds: 5500000
  documented_cost: 2000000
  documented_fees: 50000
steps:
  - net_receipt: documented_proceeds - documented_fees
  - economic_difference: net_receipt - documented_cost
expected:
  net_receipt: 5450000
  economic_difference: 3450000
```

```oa-check
name: Separate own-wallet transfer from external disposal
inputs:
  all_recorded_credits: 900000
  proved_own_wallet_transfer: 300000
  external_disposal_cost: 450000
  disposal_fees: 10000
steps:
  - external_proceeds: all_recorded_credits - proved_own_wallet_transfer
  - economic_difference: external_proceeds - external_disposal_cost - disposal_fees
expected:
  external_proceeds: 600000
  economic_difference: 140000
```

## When to refuse or refer

Never describe all crypto as fully legal without activity/provider conditions, say the framework is still merely proposed, recommend unlicensed/informal channels, invent an FBR position or a crypto tax rate, or finalise the income category from an economic subtraction. Missing cost, ownership, dates, conversions or transaction evidence must remain explicit. Refer tax classification, banking restrictions, cross-border/FX compliance and VASP licensing to the relevant practitioner.

## Filing and payment

No crypto return, rate, box identifier or payment is prescribed here. Give the transaction schedule and unresolved classification to the income-tax preparer; retain the wallet/exchange, banking and currency evidence rather than omitting the transactions.

## Completion checklist

Regulatory date and provider status checked; receipts distinguished from own transfers; documented economic amounts recomputed; no tax rate invented; export-banking conditions tested separately; unresolved tax/FX/licensing questions handed off.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for SBP May 2026 circular paragraphs 2-7, licensed versus NOC bank access and regulated-entity investment restriction | https://www.sbp.org.pk/circulars/bprd-circular-letter-no-10 | 2026-11-14 |
| Read for PVARA FAQ A.1-4/B.5-7: notified framework date, licence perimeter, register and no asset guarantee | https://pvara.gov.pk/faq | 2026-11-14 |
| Read for ITO ss.18,37,39 categories and s.154A export-realisation conditions; no blanket crypto ruling adopted | https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf | 2026-11-14 |

Not yet confirmed: current legal-tender status; a dedicated crypto tax rate, binding FBR classification of each activity, the unsupported historic claim of a uniform capital-asset position since 2023, specific provider authorisation, individual transaction/FX treatment and applicable return boxes. The regulatory framework is established; these tax and fact questions remain separate.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pk-crypto-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pk-crypto-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
