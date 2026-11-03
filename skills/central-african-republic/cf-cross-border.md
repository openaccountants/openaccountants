---
name: cf-cross-border
description: >
  Use this Central African Republic cross-border Guide for 2026 research on arrivals, departure tax clearance, foreign services, branch income and foreign transfers. It separates personal residence from corporate territoriality and explains the three-month tax-regularity attestation introduced in the signed 2025 supplementary budget, including its shorter validity where debt is stayed. Search triggers include quitus fiscal, attestation de régularité fiscale, foreign bank transfer, expatriate departure, service withholding and foreign branch. Baseline code provisions and directly read amendments are distinguished. Treaty rates, immigration outcomes and live administrative workflows remain unresolved, so this Guide cannot authorise a payment or filing.
jurisdiction: CF
category: cross-border
tax_year: 2026
tax_year_notes: "2026 research draft; conditional code baseline and named enacted amendments, not full operative coverage"
tier: 2
last_updated: 2026-11-01
version: 0.1
---

# Central African Republic cross-border income and tax clearance v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status:** For individuals changing residence and enterprises dealing with foreign recipients or transfers. It is not a sanctions, immigration, exchange-control or treaty-clearance opinion. Independent pack review is pending. Do not treat this draft as an accountant sign-off or permission to file.

## Who this applies to

Personal residence and category income are determined in the individual Guide; treaties can allocate taxing rights. For new CAR domicile/residence, income brought into charge by that move is counted only from establishment of that domicile/residence. [CGI art. 72](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger X01).

## Rates, bands and thresholds

| Item and conditions | Tax year / source |
|---|---|
| A company borrowing domestically, transferring funds abroad, or entering state contracts must first provide the stated tax-regularity attestation. LPF article 28 bis gives ordinary validity of three months from signature; one month where a tax debt has a granted stay/moratorium. Debt does not always bar issuance: the statutory not-yet-due or duly stayed conditions apply. | 2026 research scope; 2025 supplementary Finance Act arts. 9–10; CGI 393; LPF 28 bis [official text](https://www.finances.gouv.cf/sites/default/files/2025-07/COLLECTIF%202025.pdf); ledger X04 |
| Foreign service remuneration is subject to 15% withholding as a final levy, subject to treaties. Distributed investment income is withheld at 15% of gross distributions under the separate paragraph. The text does not establish the old draft’s independent 20% royalty rate or an exemption for all foreign interest. | 2026 research scope; CGI art. 166 bis 1 [official text](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf); ledger X07 |

## The base

Subject to treaties, a foreign branch/agency belonging to a CAR enterprise has its results attached to and taxed at the parent seat. If precise evidence is missing, results are determined by comparison with similar normally operated CAR enterprises. This qualifies the ordinary territorial corporate base. [CGI art. 131 bis 1](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger X06).

Start with taxpayer type, income character and location. Apply personal arrival/departure dates only after residence is established. For companies, test ordinary territorial rules and the special foreign-branch inclusion. Classify payments before withholding and obtain treaty text plus entitlement evidence before relief. For an attestation, establish tax accounts, due dates and any formal stay; distinguish ordinary validity from debt-stay validity.

## Deadlines and filing

A departing resident is assessed on income disposed of through departure, post-last-assessed business profits and income acquired even if not yet received. Provisional return is due at least 30 days before departure and can be completed during the first two months of the next fiscal year. Abandoning every CAR residence follows the same rule. [CGI art. 73](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger X02).

The departing-person clearance rule covers persons other than CAR nationals by origin, including temporary departure and current-year tax. Employer information is due one month before the employee leaves, or by notification of contract rupture. The text includes a bank guarantee of at least 10% annual turnover for permanent-departure certificates of managers of enterprises under audit; do not apply it to every traveller. [2025 supplementary Finance Act art. 9; CGI 393](https://www.finances.gouv.cf/sites/default/files/2025-07/COLLECTIF%202025.pdf) (ledger X03).

LPF 28 bis attestation is issued by DGID manually or electronically and is the unique administrative tax-status evidence. A valid attestation is required for specified approvals, foreign bank transfers, tax exemption, covered public/large-business supplier payments and exports; implementing issue conditions remain to be read. [2025 supplementary Finance Act art. 10; LPF 28 bis](https://www.finances.gouv.cf/sites/default/files/2025-07/COLLECTIF%202025.pdf) (ledger X05).

Amounts withheld under the income prepayment mechanism are remitted by the 15th of the month following invoicing/withholding. Keep the invoice and withholding record; treaty relief must be authenticated before reducing a domestic rate. [CGI arts. 166 bis 2–5](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger X08).

For departures, prepare the provisional return and employer notification, then obtain the tax clearance required by the cited text. For foreign bank transfers or other listed operations, obtain the DGID attestation and verify signatories and validity. Current application forms, electronic route, supporting attachments, fees and exchange-control paperwork were not read and stop execution.

## Penalties and interest

Use the procedure Guide [tax overview](cf-tax-overview.md). Attestation entitlement is conditional and does not erase underlying debt or penalty exposure.

## Cross-border points

Consult [individual tax](cf-income-tax.md), [company tax](cf-corporate-income-tax.md), [VAT](cf-vat-gst.md) and [transfer pricing](cf-transfer-pricing.md) for the separate taxes. No authenticated treaty inventory or reduced-rate table is supplied.

## Two worked examples that recompute

All amounts below are XAF. Inputs are fictional. Code-baseline cases are conditional on confirming the cited provisions remain applicable to the actual 2026 case. Arithmetic checks do not verify current law.

### 1. Foreign service payment with domestic withholding

Assume a XAF 10,000,000 gross foreign service fee within the cited domestic provision, no treaty reduction and no gross-up clause. Withholding is 1,500,000 and net payment 8,500,000. VAT and deductibility are separate tests.

```oa-check
name: Foreign service payment with domestic withholding
inputs:
  gross: 10000000
steps:
  - withholding: gross*0.15
  - net: gross-withholding
expected:
  withholding: 1500000
  net: 8500000
```

### 2. Departure bank guarantee boundary

Assume the special permanent-departure certificate rule applies to a manager whose enterprise is under audit, with annual turnover XAF 200,000,000. A 15,000,000 guarantee is 5,000,000 below the statutory minimum, while 20,000,000 reaches it. This does not establish that either guarantee alone ensures clearance.

```oa-check
name: Departure bank guarantee boundary
inputs:
  turnover: 200000000
  offer: 15000000
steps:
  - minimum: turnover*0.10
  - shortfall: max(0,minimum-offer)
expected:
  minimum: 20000000
  shortfall: 5000000
```

## Ask the client first

- Individual or entity, residence facts and precise arrival/departure dates?
- Income type, place of performance/use, payer and beneficial recipient?
- Counterparty relationship and treaty document/entitlement evidence?
- Tax arrears, notice due dates and formally granted stay/moratorium?
- Transfer purpose, attestation signatories and date of signature?

## Sources

| Source | URL | Read on / scope |
|---|---|---|
| DGID official CGI edition marked updated 2023 (cover also says mise à jour 2022) | https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf | 2026-11-01; Read cited articles and neighbouring scope/definitions/exceptions; not all 442 pages. Mixed edition dates and later-law consolidation unresolved. |
| Signed 2025 supplementary Finance Act, clearance amendments | https://www.finances.gouv.cf/sites/default/files/2025-07/COLLECTIF%202025.pdf | 2026-11-01; Read arts.9–10 and surrounding fiscal section; no reliance on budget/immigration schedules. |

Not yet confirmed: Full later-law reconciliation; operative treaty inventory and entitlement procedures; source/base and gross-up for each payment type; royalty and interest classification; immigration/foreign-exchange requirements; live tax-clearance forms, fees, signatories and implementation; dedicated current TP/reporting obligations.
