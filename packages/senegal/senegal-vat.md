---
name: senegal-vat
description: "Use for Senegal VAT (TVA) for tax year 2026: 18% and 10%, exemptions, precompte, deduction, monthly filing and penalties."
version: 2.2
jurisdiction: SN
tax_year: 2026
last_updated: 2026-11-14
type: situation-rules
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
---

# Senegal VAT

## Who this applies to

Anyone carrying on an economic activity independently (CGI art. 354). Individuals on CGU do not charge VAT: CGU replaces it (art. 134). Non-established businesses appoint an accredited tax representative, or the customer owes the VAT (art. 355). Foreign digital suppliers are handled by art. 355 bis.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Standard rate | 18% | Art. 369 | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Reduced rate | 10% | Services of approved tourist accommodation (art. 369) | same |
| Exempt | Art. 361 list | Care, medicines, unprocessed staple food, schooling, social-tier water and power, finance and insurance, property transfers, books and press | same |
| Gift limit | 20,000 | Input VAT on gifts blocked above this, before tax (art. 383) | same |
| Exporter status | 80% of turnover | Monthly refund claims (art. 391) | same |
| CGU turnover limit | 50,000,000 | Individuals, with tax (art. 135) | same |

## The base

Output VAT applies to taxable supplies at turnover (art. 364). Input VAT is deducted in the month the invoice is received, or within two years (arts. 375, 379). Blocked (art. 383): gifts, lodging, meals, receptions, shows, except where resold or for security staff on site; passenger and mixed vehicles unless for resale new or professional hire; ads for banned goods. Mixed activity uses the prorata (art. 385). Changes of use, disposal or loss trigger adjustment within a month (arts. 386, 387).

Precompte: the State, public bodies, public utilities, large construction firms, cement and petroleum sellers for transport withhold the whole VAT and declare it separately (art. 372). Do not treat WAEMU supplies as intra-community.

Bank pattern defaults: bank fees exempt, tax and social payments outside VAT, power, water and telecoms at 18% unless social tier. Foreign software: check art. 355 bis and art. 357 first.

## Deadlines and filing

| Item | Date | Source |
|---|---|---|
| Monthly VAT | By the 15th of the next month (art. 363) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Art. 355 bis digital | 15 January, April, July, October (art. 363) | same |
| Imports | At import | same |
| Refund claim | Quarterly, within 2 years; exporters monthly (art. 391) | same |

Steps:
1. Log in: SENTAX if your centre has moved (CME1, CME2, CPR from 1 October 2026, no paper), otherwise Mon Espace Perso for turnover up to 100 million.
2. Teledeclaration, then Declarations a effectuer.
3. Presentation, entry, attachments, annexes, preview, confirmation.
4. Telepaiement: select, choose the account, confirm.
5. Keep the history record. Check the form boxes on screen: the old line numbers could not be matched to an official form.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late payment | 5%, plus 0.5% per further month or part (art. 665) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| General breach | 200,000 (art. 667) | same |
| False NINEA or false refund | 5,000,000 (art. 668) | same |

## Cross-border points

Place of supply: arts. 356 to 360. A Senegal business that cannot prove a foreign place is taxed in Senegal (art. 360). Exports carry a right to deduct under arts. 380 and 389.

## Two worked examples that recompute

Example 1: sales 10,000,000 at 18%, input VAT 900,000. Payable 900,000.

```oa-check
name: Monthly VAT payable
inputs:
  sales: 10000000
  input_vat: 900000
steps:
  - output: sales * 0.18
  - net: output - input_vat
expected:
  net: 900000.00
```

Example 2: a hotel, approved, sells rooms of 5,000,000 at 10%, input 800,000. A credit of 300,000 carries forward, for up to two years.

```oa-check
name: Approved hotel credit
inputs:
  sales: 5000000
  input_vat: 800000
steps:
  - output: sales * 0.10
  - credit: input_vat - output
expected:
  credit: 300000.00
```

## Ask the client first

- Legal form and turnover with tax.
- Tax centre and portal.
- Any exempt supplies.
- Customers in the art. 372 list.
- Imports, exports and foreign suppliers.
- Approved tourist status.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition January 2025 (DGID): articles cited in this skill read in the PDF text | https://www.dgid.sn/storage/docs/CGI-2025.pdf | 2026-11-14 |
| DGID, Lois et reglements: read for rates table and recent measures (Loi 2025-17) | https://www.dgid.sn/loi-reglement | 2026-11-14 |
| Loi n. 2025-19, finance law for 2026 (64-page scan): read by OCR on 2026-11-01, all pages searched: no CGI amendment found; art. 19 adds a cashew export duty. Reopened 2026-11-14, not re-read | https://budget.sec.gouv.sn/documents/public_download/69556841-a9d4-4658-8c1e-fe230a2a028a/telechargement | 2026-11-14 (opened, not re-read) |
| DGID calendar of annual filings: read for full table | https://www.dgid.sn/storage/docs/calendrier-declarations-annuelles.pdf | 2026-11-14 |
| DGID SENTAX user guide v1.1, 2026: read for contents and steps | https://www.dgid.sn/storage/uploads/guide-utilisateur-espace-connecte-1790609363.pdf | 2026-11-14 |
| DGID communique, SENTAX for CME1, CME2 and CPR from 1 October 2026: read in full | https://www.dgid.sn/storage/uploads/communique-ouverture-de-la-plateforme-sentax-aux-contribuables-du-cme1-cme2-et-du-cpr-1790699194.pdf | 2026-11-14 |
| DGID Entreprises page: read for portal descriptions | https://www.dgid.sn/entreprises | 2026-11-14 |

Not yet confirmed: The text of Loi 2025-17 was not opened; only DGID's summary of it was read, so any CGI change it made beyond that summary is not reflected. The old registration threshold (100M goods, 50M services): no such VAT threshold found in arts. 351 to 355. Old capital goods periods of 20 and 5 years and the old 50% late filing surcharge and 1% monthly interest were not found and conflict with art. 665. Old list of exempt rent and agricultural inputs: read arts. 361 onward. Exact return form boxes. Quarterly filing for the simplified regime.
