---
name: dj-vat-gst
description: "Use for Djibouti VAT (TVA) for tax year 2026: 10% and 0%, registration at 20 million or 10 million, all liberal professions, exemptions, deduction and the monthly return by the 20th."
version: 2.0
jurisdiction: DJ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Djibouti VAT

## Who this applies to

Businesses at or above the limit, including free-zone and investment-code firms when they supply the local market (arts. 173, 174; 2017 law art. 4). Liberal professions register whatever their turnover (art. 174 al. 2, LF 2024 art. 20). Others may opt in (art. 177). A non-resident must appoint a solvent accredited representative resident in Djibouti and registered for VAT (art. 181).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Standard rate | 10% | All taxable operations (art. 187, LF 2015 art. 26) | https://www.journalofficiel.dj/texte-juridique/loi-n82-an-14-7eme-l-portant-budget-initial-de-letat-pour-lexercice-2015/ |
| Zero rate | 0% | Exports with customs-stamped declaration, export and transit services, international passenger transport, ship and aircraft supplies (art. 187). Input VAT stays deductible. Art. 187 d (externally funded public contracts) repealed by LF 2024 art. 21 | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Build-phase zero rate | 0% | New hotel, real estate and processing investors on imports, after a DGI undertaking (art. 187, LF 2022 art. 19) | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ |
| Limit, goods | 20,000,000 | Goods, on-site food sales, builders supplying materials (art. 174-1, LF 2022 art. 20) | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ |
| Limit, others | 10,000,000 | Services, non-commercial professions, lodging without food | same |
| Mid-year trigger | 120,000,000 | 2011 text: over the limit in year N means VAT from N+1; past 120,000,000 from that month. Figure not restated after 2022 | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Exit | 3 years under the limit | Out from year 4 unless the option is taken before 1 February (art. 174) | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Bank commissions | Taxable | Banking operations exempt except commissions (art. 176-2, LF 2025 art. 12) | https://www.journalofficiel.dj/texte-juridique/loi-n150-an-24-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2025/ |

## The base

Exempt (art. 176): direct farm, livestock and fishing sales, banking, insurance, transfers of property under registration duties, newspapers, non-profit social, health and education services, plus the rest of the art. 176 list. Input VAT is deductible for registered traders, with exclusions in arts. 190 and 191; a pro rata applies to general costs and fixed assets for mixed traders (art. 192). Credit refunds: arts. 196 to 203. The separate TBS turnover tax was repealed (LF 2022 art. 15).

## Deadlines and filing

| Item | Date or rule | Source |
|---|---|---|
| Monthly return and payment | By the 20th, or next working day. Nil returns too, in two signed copies (arts. 206, 207). The old skill said the 15th | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Sales and purchase file | Email to DGI in the 24 hours before filing (art. 206, LF 2015 art. 29) | https://www.journalofficiel.dj/texte-juridique/loi-n82-an-14-7eme-l-portant-budget-initial-de-letat-pour-lexercice-2015/ |
| Start of activity | Declare within 12 days (art. 218) | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |

Steps:
1. Total taxable sales, exempt sales and deductible VAT for the month.
2. Complete the DGI model return in two copies, signed and dated.
3. Send the electronic file the day before.
4. File with the Grandes Entreprises service and pay at the same time.
5. Keep the second copy. Rounded to the nearest franc.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late payment | 5% surcharge plus 0.5% interest per month; no 5% on audit assessments (art. 247) | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Late or missing return | Interest 5% (art. 246 as amended 2021; the earlier text was 0.5% per month) plus 10% if filed within 10 days of formal notice, 40% after that or never | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n111-an-20-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2021/ |

## Cross-border points

Place of supply: a sale delivered in Djibouti, and a service, let object or right used or exploited in Djibouti, is taxed here even if the debtor is abroad (art. 178). Imports: VAT at customs. Goods under customs regimes: see the Code des douanes changes in LF 2026 arts. 6 to 13 (no VAT rate change).

## Two worked examples that recompute

Example 1: sales 10,000,000 at 10%, input VAT 400,000. Payable 600,000.

```oa-check
name: Monthly VAT payable
inputs:
  sales: 10000000
  input_vat: 400000
steps:
  - output: sales*0.10
  - net: output-input_vat
expected:
  net: 600000.00
```

Example 2, the decision: must a services firm with turnover 12,000,000 register? Yes, the 10,000,000 limit applies; a goods trader at the same turnover would not.

```oa-check
name: Excess over services limit
inputs:
  turnover: 12000000
  limit: 10000000
steps:
  - excess: turnover-limit
expected:
  excess: 2000000.00
```

## Ask the client first

- Goods or services, and annual turnover.
- Liberal profession?
- Exports or transit work?
- Mixed exempt and taxable sales?
- Foreign supplier or non-resident seller.
- Free-zone or investment-code status.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition updated to the 2011 finance law, Ministry of Finance: articles cited read in the PDF text; later changes taken from the finance laws listed here | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf | 2026-11-01 |
| Loi 82/AN/14/7eme L, budget 2015: articles 8 to 29 read | https://www.journalofficiel.dj/texte-juridique/loi-n82-an-14-7eme-l-portant-budget-initial-de-letat-pour-lexercice-2015/ | 2026-11-01 |
| Loi de finances 142/AN/21/8eme L, budget 2022: Titre II read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ | 2026-11-01 |
| Loi de finances 64/AN/23/9eme L, budget 2024: Titre II tax articles read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n-64-an-23-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2024/ | 2026-11-01 |
| Loi 150/AN/24/9eme L, budget 2025: Titre II articles 6 to 21 read | https://www.journalofficiel.dj/texte-juridique/loi-n150-an-24-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2025/ | 2026-11-01 |
| Loi de finances 203/AN/25/9eme L, budget 2026 (JO 31/12/2025): Titre II read; direct tax: rectified 2025 measures stay in force, no CGI rate change | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n203-an-25-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2026/ | 2026-11-01 |
| Loi de finances 111/AN/20/8eme L, budget 2021: articles 6 to 20 read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n111-an-20-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2021/ | 2026-11-01 |
| Loi 190/AN/17/7eme L amending the CGI: articles 1 to 5 read | https://www.journalofficiel.dj/texte-juridique/loi-n190-an-17-7eme-l-portant-modification-du-code-general-des-impots/ | 2026-11-01 |

Not yet confirmed: The CGI on the official site is the 2011 edition. No consolidated 2026 code could be opened (impots.dj, dgi.dj and economie.gouv.dj did not answer), so each rule is the 2011 text plus the finance laws read; the finance laws found in the gazette for 2013 to 2026 were scanned for tax articles, the 2012 law was not, so an amendment made only there or in a law the gazette search missed would not show. A reverse charge on imported services was in the old skill; no such rule was found, and art. 181 points to a representative instead. The email address in LF 2015 art. 29 and any current e-filing portal were not confirmed. LF 2022 art. 19 says art. 187 is "rewritten" but gives one paragraph: read here as replacing paragraph f only, since later laws keep charging 10%.

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
