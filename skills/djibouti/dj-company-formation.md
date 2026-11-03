---
name: dj-company-formation
description: "Use for setting up a business in Djibouti for 2026: sole trader, SARL or SA, no minimum capital, the ODPIC one-stop steps, the one-month register rule and first tax registrations."
version: 2.0
jurisdiction: DJ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Djibouti Company Formation

## Who this applies to

Founders choosing a form. ODPIC runs the Registre de Commerce et des Societes and the guichet unique. Company law is the Djibouti Code de commerce. A notary, lawyer or bailiff may file for you.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| SARL members | 1 to 100 | Arts. L.313-1, L.313-3. The old skill said 50 | https://www.ministere-finances.dj/Code%20DE%20COMMERCE.pdf |
| Minimum capital | None | "il n existe pas de capital minimum requis"; capital set in the statutes (arts. L.313-2, L.314-2). Funds are blocked and availability attested | https://odpic.dj/creation-dentreprise/ |
| Registration deadline | 1 month | From formation, or a fine | https://odpic.dj/presentation-du-registre-de-commerce-et-des-societes-rcs/ |
| Capital contributions duty | 10,000 fixed | Art. 488 B, 2017 law art. 5 | https://www.journalofficiel.dj/texte-juridique/loi-n190-an-17-7eme-l-portant-modification-du-code-general-des-impots/ |
| Tax start declaration | 12 days | Art. 218 | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| CNSS | 48 hours | Employers | https://cnss.dj/affiliation-employeur/ |
| Patente relief | Classes 5 to 8 exempt 3 years | Art. 100, new payers, 2017 law art. 1, later amended (LF 2022 art. 17) | https://www.journalofficiel.dj/texte-juridique/loi-n190-an-17-7eme-l-portant-modification-du-code-general-des-impots/ |

## The base

Forms recognised: sole trader; partnerships (SNC, SCS, societe en participation); capital companies (SA, SARL, SCA). SA and SARL are the commonest. A sole trader answers with personal assets; a company is separate from its members. Branch: not covered by the ODPIC page.

## Deadlines and filing

| Item | Date or rule | Source |
|---|---|---|
| File at the guichet unique | Single form, negative certificate form, IDs, statutes in two copies, criminal record or sworn statement, licence for regulated activity | https://odpic.dj/creation-dentreprise/ |

Steps:
1. Apply for the negative certificate to clear the name.
2. Draft statutes.
3. Block the funds and obtain proof.
4. File the dossier at the ODPIC guichet unique.
5. Collect the registration receipt.
6. Declare to the DGI within 12 days and join the CNSS within 48 hours if hiring.
7. Each year: accounts, IBP return before 1 April, monthly ITS, CNSS and VAT.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late registration | Fine; amount not stated on the page | https://odpic.dj/presentation-du-registre-de-commerce-et-des-societes-rcs/ |

## Cross-border points

Foreign founders use the same route; regulated activities need prior approval. Free-zone firms: Code des zones franches in the CGI annexes; insurance SAs headquartered in Djibouti need 100 million capital under the Code de commerce (art. 20-3).

## Two worked examples that recompute

Example 1: a society with capital 1,000,000 pays the fixed 10,000 duty on contributions (art. 488 B).

```oa-check
name: Fixed duty on contributions
inputs:
  duty: 10000
  copies: 1
steps:
  - total: duty*copies
expected:
  total: 10000.00
```

Example 2, the decision: SARL or sole trader for 12,000,000 of fees? Both reach VAT above 10,000,000; a sole trader carries unlimited liability, so a SARL fits when risk is real. Tax on profit 2,000,000 is 25% either way, floor 120,000.

```oa-check
name: Profit tax
inputs:
  profit: 2000000
steps:
  - tax: max(profit*0.25,120000)
expected:
  tax: 500000.00
```

## Ask the client first

- Number of founders.
- Regulated activity?
- Foreign owners?
- Free zone?
- Expected turnover.

## Sources

| Source | URL | Read on |
|---|---|---|
| ODPIC, Creation d entreprise: steps read | https://odpic.dj/creation-dentreprise/ | 2026-11-01 |
| ODPIC, Registre de commerce et des societes: presentation read | https://odpic.dj/presentation-du-registre-de-commerce-et-des-societes-rcs/ | 2026-11-01 |
| Code de commerce 2011, Ministry of Finance: arts. L.313-1 to L.313-3 and L.314-2 read | https://www.ministere-finances.dj/Code%20DE%20COMMERCE.pdf | 2026-11-01 |
| Code general des impots, edition updated to the 2011 finance law, Ministry of Finance: articles cited read in the PDF text; later changes taken from the finance laws listed here | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf | 2026-11-01 |
| CNSS, Affiliation employeur: full page read | https://cnss.dj/affiliation-employeur/ | 2026-11-01 |
| Loi 190/AN/17/7eme L amending the CGI: articles 1 to 5 read | https://www.journalofficiel.dj/texte-juridique/loi-n190-an-17-7eme-l-portant-modification-du-code-general-des-impots/ | 2026-11-01 |

Not yet confirmed: The CGI on the official site is the 2011 edition. No consolidated 2026 code could be opened (impots.dj, dgi.dj and economie.gouv.dj did not answer), so each rule is the 2011 text plus the finance laws read; the finance laws found in the gazette for 2013 to 2026 were scanned for tax articles, the 2012 law was not, so an amendment made only there or in a law the gazette search missed would not show. The old skill's 3-day timeline, USD 70,000 free-zone capital and 1,000,000 SARL capital came from non-official sites; the capital figure is contradicted by ODPIC and the others were not confirmed. Fees: ODPIC tariff page not read. Guichet-unique.dj did not open.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
