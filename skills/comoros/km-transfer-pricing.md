---
name: km-transfer-pricing
description: >
  Comoros transfer pricing for tax year 2026, from the Amending Finance Law 2024 (Law 24-013/AU). Covers the arm's length rule in CGI article 31, the 50% control test, the privileged tax regime test in article 31 bis, the annual transfer pricing declaration in article 43 bis, the audit information request in LPF L.21, the documentation duty in L.21 bis, and the fines in L.101 bis and L.114 bis. Use for questions such as: does my Comoros company file a transfer pricing return, what is the KMF 80,000,000 threshold, what is the fine for missing documentation. Out of scope: company tax rates and registration (see km-registration-and-tax-clearance), audit procedure generally (see km-electronic-filing-and-tax-procedure). Not reviewed by an accountant. The ministerial order on documentation content was not found.
version: 0.1
jurisdiction: KM
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Comoros: transfer pricing

## Who this applies to

Companies in Comoros that control, or are controlled by, a company in or outside Comoros. Control means holding more than 50% of capital or votes, directly or through another person, or in fact holding the decision-making power. Two companies under the same controller also count (CGI art. 31(2)). No control link is needed for transfers to a business in a state with a privileged tax regime (art. 31(3)).

## Rates, bands and thresholds

| Item | Figure | Year | Source |
|---|---|---|---|
| Control test | More than 50% of capital or votes, or de facto control (art. 31(2)) | 2026 |  |
| Privileged tax regime | Not taxable there, or profit tax at least 40% lower than Comoros tax (art. 31 bis) | 2026 | same |
| Declaration and documentation threshold | Turnover excluding tax or gross assets of KMF 80,000,000 or more, in the company, a held company or a holder (art. 43 bis, L.21 bis) | 2026 | same |
| Fine for no, incomplete or inaccurate declaration | KMF 50,000,000 fixed (L.101 bis) | 2026 | same |
| Fine after a documentation notice | 2% of the transactions concerned, at least KMF 25,000,000 per audited year (L.114 bis) | 2026 | same |

## The base

Profits moved indirectly, by raising or lowering prices or any other means, are added back to the company's results. The amount is measured against what would have been earned with no link (art. 31(1)).

## Deadlines and filing

- Annual declaration: same deadline as the profit return, 30 April under the 2023 code art. 42(1) ("au plus tard le 30 avril"), on the tax authority's form (art. 43 bis). It covers group information and the company's own related-party transactions, loans, non-cash transactions and advance agreements or rulings with other states.
- Documentation: available on the date an audit starts (L.21 bis). It does not replace evidence for each transaction. Its content is set by order of the Finance Minister.
- Companies below the threshold: on audit, 15 days to answer an L.21 request, then 8 days after a formal notice.
- Companies above the threshold: 8 days after a formal notice (L.21 bis(5)).

## Penalties and interest

L.101 bis applies to the declaration. L.114 bis applies, per audited year, to failure after an L.21 bis notice, and art. L.21 applies the same fine to failure after an L.21 notice.

## Cross-border points

The rule covers links in and outside Comoros, so domestic groups are included. A foreign information request under a treaty can extend on-site audit time by three months (L.42).

## Two worked examples that recompute

A company receives a notice and leaves transactions of KMF 900,000,000 undocumented. 2% is KMF 18,000,000, below the floor, so the fine is KMF 25,000,000.

```oa-check
name: Fine at the floor
inputs:
  transactions: 900000000
steps:
  - fine: max(transactions * 0.02, 25000000)
expected:
  fine: 25000000
```

The same failure on KMF 2,000,000,000 gives 2%, KMF 40,000,000, above the floor.

```oa-check
name: Fine above the floor
inputs:
  transactions: 2000000000
steps:
  - fine: max(transactions * 0.02, 25000000)
expected:
  fine: 40000000
```

## Ask the client first

- Who holds more than 50% of the company, and what does it hold?
- What are turnover and gross assets for each linked company?
- Are there payments to low-tax states, with or without a control link?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 24-013/AU of 27 August 2024, Amending Finance Law 2024, art. 10, pages 9 to 14, scan, OCR read |  | 2026-11-01 |
| Law 25-020/AU, Finance Law 2026, tax section; no change to these articles |  | 2026-11-01 |
| Code general des impots, 2023 edition, art. 42 | https://justice.gouv.km/wp-content/uploads/2025/03/comores-cgi-2023.pdf | 2026-11-01 |

Not yet confirmed: the Finance Minister's order on documentation content; the current declaration form; the Amending Finance Law 2025 (official link returned 404).
