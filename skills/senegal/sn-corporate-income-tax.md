---
version: 0.2
name: sn-corporate-income-tax
description: "Use for Senegal corporate income tax (IS) for tax year 2026: 30% rate, IMF, regimes, instalments, filing and penalties."
jurisdiction: SN
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Senegal corporate income tax

## Who this applies to

Companies and other legal persons in CGI art. 4, on profits made in Senegal. Exemptions: arts. 5, 6.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| IS | 30% | Under 1,000 ignored (art. 36) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| IMF | 0.5% of prior-year turnover before tax | Loss-makers or low IS; cap 5,000,000 (arts. 38, 40) | same |
| IMF exemption | New firms, 3 years | Not large-enterprise office (art. 39) | same |
| Real normal | Over 100,000,000 turnover with tax | Art. 26; property businesses always | same |
| Simplified | Under 100,000,000 | 15% profit abatement in an approved centre (arts. 28, 29) | same |
| Loss carry-forward | 3 years | Art. 16; depreciation in loss years not limited | same |
| Dividend withholding | 10% | Art. 173 | same |
| Interest | 16%; 13% bonds; 8% deposits | Art. 173 | same |
| Service payments to resident individuals | 5% | Art. 200 | same |

## The base

Net profit from all operations (arts. 7, 8), adjusted per arts. 9 to 16. Transfer pricing: art. 17. Payments to privileged regimes: art. 18. Holding and parent reliefs: arts. 21 to 23.

## Deadlines and filing

| Item | Date | Source |
|---|---|---|
| Return and financial statements | 30 April (arts. 30, 31) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| First instalment | First 15 days of February; at least the IMF (arts. 214, 215) | same |
| Second instalment | 30 April, one third of last year's tax | same |
| Balance | 15 June | same |

Steps:
1. Get the accounts visa, then file at the single filing window through SEN-ETAFI.
2. In SENTAX or Mon Espace Perso (turnover up to 100 million): Teledeclaration, then the six steps.
3. Telepaiement: amounts, bank account, confirmation. Keep the history record.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late payment | 5%, plus 0.5% per further month or part (art. 665) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Missing transfer pricing declaration | 10,000,000 (art. 667) | same |
| Country-by-country report | 25,000,000 (art. 667) | same |
| No compliant accounts | 5,000,000 (art. 668) | same |

## Cross-border points

Transfer pricing documentation: arts. 31 bis, 638, 639. Payments and non-resident withholding: check art. 173 and the treaty list at https://www.dgid.sn/conventions-fiscales.

## Two worked examples that recompute

Example 1: profit 40,000,000, prior turnover 500,000,000. IS 12,000,000 exceeds IMF 2,500,000.

```oa-check
name: IS above IMF
inputs:
  profit: 40000000
  turnover: 500000000
steps:
  - imf: min(turnover * 0.005, 5000000)
  - tax: max(profit * 0.30, imf)
expected:
  tax: 12000000.00
```

Example 2: a loss, turnover 2,000,000,000. IMF would be 10,000,000; the cap makes it 5,000,000.

```oa-check
name: Loss-maker at the cap
inputs:
  profit: 0
  turnover: 2000000000
steps:
  - imf: min(turnover * 0.005, 5000000)
  - tax: max(profit * 0.30, imf)
expected:
  tax: 5000000.00
```

## Ask the client first

- Legal form and first year.
- Turnover with tax, and last year's turnover.
- Tax centre and portal.
- Related parties abroad.
- Dividends, interest and service payments made.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition January 2025 (DGID): articles cited in this skill read in the PDF text | https://www.dgid.sn/storage/docs/CGI-2025.pdf | 2026-11-01 |
| DGID, Lois et reglements: rates table and recent measures (Loi 2025-17) read | https://www.dgid.sn/loi-reglement | 2026-11-01 |
| Loi n. 2025-19, finance law for 2026 (scan, read by OCR, all 64 pages searched): no CGI amendment found; art. 19 adds a cashew export duty | https://budget.sec.gouv.sn/documents/public_download/69556841-a9d4-4658-8c1e-fe230a2a028a/telechargement | 2026-11-01 |
| DGID calendar of annual filings: full table read | https://www.dgid.sn/storage/docs/calendrier-declarations-annuelles.pdf | 2026-11-01 |
| DGID SENTAX user guide v1.1, 2026: contents and steps read | https://www.dgid.sn/storage/uploads/guide-utilisateur-espace-connecte-1790609363.pdf | 2026-11-01 |
| DGID communique: SENTAX for CME1, CME2 and CPR from 1 October 2026: full text read | https://www.dgid.sn/storage/uploads/communique-ouverture-de-la-plateforme-sentax-aux-contribuables-du-cme1-cme2-et-du-cpr-1790699194.pdf | 2026-11-01 |
| DGID Entreprises page: portal descriptions read | https://www.dgid.sn/entreprises | 2026-11-01 |

Not yet confirmed: The text of Loi 2025-17 was not opened; only DGID's summary of it was read, so any CGI change it made beyond that summary is not reflected. Free export enterprise 15% rate; 20% royalty and service withholding to non-residents; first-year instalment exemption; 5% rule as the old file worded it for non-CIT residents is carried only as art. 200.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
