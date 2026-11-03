---
version: 0.2
name: sn-company-formation
description: "Company formation for Senegal, tax year 2026: tax registration steps from DGID; company law items listed as unconfirmed."
jurisdiction: SN
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Senegal company formation

## Entity types, capital and incorporation

| Item | Rule | Source |
|---|---|---|
| NINEA | Free apart from the fiscal stamp; about 3 days | https://www.dgid.sn/fiches/ninea |
| Declaration of existence | Within 20 days of starting (CGI art. 633) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Regime choice | Real, CGU or CGF by turnover | https://www.dgid.sn/particuliers |
| Annual accounts | With the return by 30 April (arts. 30, 31) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Monthly filings | VAT by the 15th (art. 363); salary withholding by the 15th, or quarterly for real simplified and CGU employers (art. 185) | same |

Steps: 1. Get the NINEA. 2. File the declaration of existence. 3. Choose the regime. Formalise online at https://dgid-digitale.dgid.sn.

## Two worked examples that recompute

Example 1: an individual provides services with turnover of 400,000. CGU at 5% is 20,000, so the 30,000 minimum applies (art. 141).

```oa-check
name: CGU services at the minimum
inputs:
  turnover: 400000
steps:
  - cgu: max(turnover * 0.05, 30000)
expected:
  cgu: 30000.00
```

Example 2: an individual trader with turnover of 10,000,000. CGU at 2% is 200,000, above the 25,000 minimum (art. 141).

```oa-check
name: CGU trader above the minimum
inputs:
  turnover: 10000000
steps:
  - cgu: max(turnover * 0.02, 25000)
expected:
  cgu: 200000.00
```

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
| DGID NINEA sheet: page read | https://www.dgid.sn/fiches/ninea | 2026-11-01 |

Not yet confirmed: OHADA forms (SARL, SA, SAS), SA capital of XOF 10,000,000 and SARL capital, APIX one-stop steps and timing, and CSS and IPRES employer registration. The old citations were secondary, apix.sn and the social bodies did not open, and the OHADA Uniform Act was not read.

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
