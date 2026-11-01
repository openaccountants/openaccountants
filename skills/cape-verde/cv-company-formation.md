---
name: cv-company-formation
description: "Company formation for Cape Verde (tax year 2026): Lda and SA, Casa do Cidadao, tax and INPS registration, REMPE benefits. Built from official pages; company-law figures are marked unconfirmed."
jurisdiction: CV
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cape Verde Company Formation v0.2

## Who this applies to

Founders setting up in Cape Verde. The usual vehicles are the Sociedade por Quotas (Lda) and Sociedade Anonima (SA). The Companies Code could not be opened, so capital and fee figures are not stated.

## Rates, bands and thresholds

Basis for 2026: the law is the State Budget 2026 (Lei 69/X/2025, in force 1 January 2026), the DNRE Calendario Fiscal 2026 and the base code as published. No consolidated code was found, and Lei 116/IX/2021 could not be opened, so a row resting on original code text carries that limit. The Amending Budget of 13 August 2026 changed no tax rate we could find.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| REMPE acts of formation, capital increase, statute change, closing, registration (art. 44) | Free of stamp duty, fees and emoluments | 2026 | https://boe.incv.cv/Bulletins/Download/6150 |
| REMPE one-stop shop | Casa do Cidadao for formation and certification | 2026 | https://www.mf.gov.cv/documents/54571/273413/Desdobr%C3%A1vel%20REMPE.pdf |
| TEU minimum | CVE 30,000 a year | 2026 | https://boe.incv.cv/Bulletins/Download/1891 |
| INPS registration | Within 15 days of starting | 2026 | https://inps.cv/inscricao/ |

## The base

REMPE companies keep purchase and sales books for 8 years and need no organised accounts (DNRE leaflet). Others keep organised accounts and certified software from Budget 2026.

## Deadlines and filing

### How to set up

1. Go to the Casa do Cidadao, the single counter for constitution and certification.
2. Get a NIF (Modelo 109) and file start of activity (Modelo 110) from the [DNRE page](https://www.mf.gov.cv/web/dnre/dire%C3%A7%C3%A3o-geral-das-contribui%C3%A7%C3%B5es-e-impostos).
3. Notify the municipality where required (REMPE leaflet).
4. Register with INPS within 15 days: inscription form, licence copy, the Boletim Oficial publication, NIF, and a statement naming the representative.
5. Annual duties: see [overview](cv-tax-overview.md).

## Penalties and interest

See the linked skills.

## Cross-border points

Foreign founders: not read.

## Two worked examples that recompute

Case 1: a micro company starting 1 July with turnover under CVE 1,000,000 pays the minimum for 6 months: CVE 15,000.

```oa-check
name: Pro rata minimum
inputs:
  m: 6
steps:
  - due: 30000 * m / 12
expected:
  due: 15000.00
```

Case 2, the choice at formation: sales of CVE 900,000 give 4% = CVE 36,000 on the rate alone, but art. 25(2) says a micro company at or under CVE 1,000,000 pays the minimum: CVE 30,000 on that reading.

```oa-check
name: Rate or minimum
inputs:
  s: 900000
steps:
  - rate: s * 0.04
  - gap: rate - 30000
expected:
  rate: 36000.00
  gap: 6000.00
```


## Ask the client first

- Lda or SA?
- Turnover and workers expected?
- REMPE or organised accounts?
- Foreign shareholders?
- Island of the seat?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 69/X/2025, State Budget 2026, BO I 133 sup. 1, 31 Dec 2025: arts 29, 30, 32, 84, 99, 100 and Anexo I read | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 | 2026-11-01 |
| Lei 1/XI/2026, Amending Budget 2026, BO I 90, 13 Aug 2026: searched for tax-rate changes, none found | https://boe.incv.cv/Bulletins/DownloadAct?id=112975 | 2026-11-01 |
| Lei 70/VIII/2014, REMPE, BO I 51, 26 Aug 2014: arts on the TEU, 25 and 26 read | https://boe.incv.cv/Bulletins/Download/1891 | 2026-11-01 |
| Lei 45/X/2024, Budget 2025: arts 25 and 26 read | https://boe.incv.cv/Bulletins/Download/6150 | 2026-11-01 |
| DNRE, REMPE leaflet, 2015: all read | https://www.mf.gov.cv/documents/54571/273413/Desdobr%C3%A1vel%20REMPE.pdf | 2026-11-01 |
| INPS, Inscricao: all read | https://inps.cv/inscricao/ | 2026-11-01 |
| DNRE, forms and leaflets page: list read | https://www.mf.gov.cv/web/dnre/dire%C3%A7%C3%A3o-geral-das-contribui%C3%A7%C3%B5es-e-impostos | 2026-11-01 |

Not yet confirmed: Whether art. 25(2) is a flat CVE 30,000 up to CVE 1,000,000, or a floor under 4%, which would give CVE 36,000 in case 2. Minimum capital (old skill: CVE 1, CVE 100,000 typical); capital pay-up 50% and 30%; timeline 1 to 2 weeks; notary CVE 5,000 to 15,000; registration CVE 2,500 plus 0.2% stamp duty; chartered accountant requirement; annual financial statement duty. All came from secondary sources and are removed from the body until the Commercial Companies Code is read.

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
