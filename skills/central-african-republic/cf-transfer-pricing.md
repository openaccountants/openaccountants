---
name: cf-transfer-pricing
description: >
  Use this Central African Republic transfer pricing Guide for 2026 research on foreign controlled transactions, profit transfers, low-tax counterparties and cross-border deductions. It works through the fetched code’s control test, the privileged-tax comparison and specific limits on foreign charges and purchasing commissions. Search triggers include prix de transfert, related-party fee, thin capitalisation, management charge, royalty, non-cooperative territory and deduction cap. This is a conditional statutory baseline from the Ministry’s official 2023 edition, with unresolved later amendments and procedural requirements expressly withheld. It does not declare that master files, local files, country reporting or advance agreements are absent.
jurisdiction: CF
category: transfer-pricing
tax_year: 2026
tax_year_notes: "2026 research draft; conditional code baseline and named enacted amendments, not full operative coverage"
tier: 2
last_updated: 2026-11-01
version: 0.1
---

# Central African Republic controlled transfers and foreign deductions v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status:** For enterprises testing the cited foreign-transfer and deduction rules. The job is a documented adjustment working paper, not a transfer-pricing filing or selection of a prescribed method. Independent pack review is pending. Do not treat this draft as an accountant sign-off or permission to file.

## Who this applies to

Controlled foreign-enterprise transfers of profit through purchase/sale prices, thin capitalisation or other means are added back under article 131. Direct majority ownership, actual decision power and common control count. A privileged-tax/non-cooperative recipient removes the dependence condition. [CGI art. 131](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger T01).

## Rates, bands and thresholds

| Item and conditions | Tax year / source |
|---|---|
| A privileged-tax state is one where the enterprise is untaxed or profit/income tax is more than half below the ordinary CAR corporate comparator. Exactly half below does not satisfy this particular limb. Determine comparable tax amounts, not headline rates alone. | 2026 research scope; CGI art. 131 bis(1) [official text](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf); ledger T02 |
| Covered effective services, head-office/technical/financial/accounting fees, commissions, interest and IP charges paid outside the Community require proof of real, normal, non-excessive operations and cannot exceed 20% of taxable profit before those charges. In a loss year the provision uses the last profitable, non-prescribed result. Rejected sums are treated as distributions. | 2026 research scope; CGI art. 126 bis 11 [official text](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf); ledger T04 |
| Purchasing commissions/brokerage for Community enterprises are capped at 5% of purchases by buying centres/intermediaries, with rebates benefiting those enterprises and a regular invoice attached to the supplier invoice. This specific ceiling is not a universal cost-plus margin. | 2026 research scope; CGI art. 126 bis 13 [official text](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf); ledger T06 |

## The base

Payments to privileged-tax recipients require proof of real operations and amounts that are neither abnormal nor excessive. Amounts paid/due to non-cooperative-state recipients are non-deductible under the distinct rule. The list is the specified OECD/UN/CEMAC list, potentially supplemented by ministerial decision; no operative list is authenticated here. [CGI art. 131 bis](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger T03).

IP royalties also require proof the right remains valid. Article 126 bis 12 contains a separate distribution treatment where royalties benefit an enterprise participating in management/capital of an enterprise outside the Community. Do not treat meeting the fee cap as settling this rule. [CGI art. 126 bis 12](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger T05).

Obtain ownership/control records, contracts, service deliverables, recipient tax calculations and payment/invoice evidence. Identify the article 131 transfer and quantify the supported addition without double counting an expense already disallowed. Test privileged/non-cooperative status separately. Apply each specific foreign-charge restriction, including the loss-year condition and IP validity rule; record which restriction determines the final allowance. Do not invent a statutory margin, database preference or master-file threshold.

## Deadlines and filing

Keep the adjustment and foreign-fee reconciliation with the corporate tax working papers and DSF evidence. The annual company calendar is in [corporate income tax](cf-corporate-income-tax.md). No current dedicated TP form, portal, deadline, local/master-file or CbCR procedure was opened; do not make a nil-filing or no-regime conclusion.

## Penalties and interest

General penalties and the unresolved special/general priority are in [tax overview](cf-tax-overview.md). No separate TP fine is established by this reading.

## Cross-border points

The Community wording is retained as written. Recipient location, relationship, treaty and withholding must be examined separately through [cross-border](cf-cross-border.md). A withholding payment does not prove deductibility.

## Two worked examples that recompute

All amounts below are XAF. Inputs are fictional. Code-baseline cases are conditional on confirming the cited provisions remain applicable to the actual 2026 case. Arithmetic checks do not verify current law.

### 1. Foreign fee deduction cap

Assume article 126 bis 11 applies, all reality/normality conditions hold, no additional disallowance and taxable profit before covered fees is XAF 50,000,000. Covered fees are 12,000,000, the cap is 10,000,000 and 2,000,000 is rejected. Do not also add that 2,000,000 under another heading.

```oa-check
name: Foreign fee deduction cap
inputs:
  profit_before: 50000000
  fees: 12000000
steps:
  - cap: profit_before*0.20
  - allowed: min(fees,cap)
  - rejected: fees-allowed
expected:
  allowed: 10000000
  rejected: 2000000
```

### 2. Exactly half or more than half below

Assume comparable CAR ordinary tax would be XAF 3,000,000. Recipient tax of 1,500,000 is exactly half below, while 1,200,000 is more than half below. Only the latter meets this quantitative limb; other non-cooperative and transfer rules remain separate.

```oa-check
name: Exactly half or more than half below
inputs:
  car_tax: 3000000
  tax_a: 1500000
  tax_b: 1200000
steps:
  - boundary: car_tax*0.5
  - below_a: boundary-tax_a
  - below_b: boundary-tax_b
expected:
  boundary: 1500000
  below_a: 0
  below_b: 300000
```

## Ask the client first

- Ownership percentages, actual decision powers and common control?
- Counterparty country, actual tax amounts and authenticated list status?
- Nature, commercial benefit, invoices and evidence of performance?
- Profit before covered foreign charges and last non-prescribed profitable year?
- Rights validity, relevant management/capital relationships and commission purchase base?

## Sources

| Source | URL | Read on / scope |
|---|---|---|
| DGID official CGI edition marked updated 2023 (cover also says mise à jour 2022) | https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf | 2026-11-01; Read cited articles and neighbouring scope/definitions/exceptions; not all 442 pages. Mixed edition dates and later-law consolidation unresolved. |

Not yet confirmed: Full later-law reconciliation; operative privileged/non-cooperative lists; prescribed TP methods, documentation thresholds, filing forms, local file, master file, CbCR, APAs, penalty calendar and treaty corresponding-adjustment procedures. None is declared absent.
