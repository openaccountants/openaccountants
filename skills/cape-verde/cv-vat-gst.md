---
name: cv-vat-gst
description: "VAT (IVA) for Cape Verde (tax year 2026): 15% rate, 8% on electricity and water, Modelo 106, e-invoicing and goods removed from exemption in 2026. Built from the Boletim Oficial and DNRE pages."
jurisdiction: CV
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cape Verde VAT v0.2

## Who this applies to

Businesses supplying goods and services in Cape Verde, and importers. REMPE companies do not charge IVA: see [corporate income tax](cv-corporate-income-tax.md).

## Rates, bands and thresholds

Basis for 2026: the law is the State Budget 2026 (Lei 69/X/2025, in force 1 January 2026), the DNRE Calendario Fiscal 2026 and the base code as published. No consolidated code was found, and Lei 116/IX/2021 could not be opened, so a row resting on original code text carries that limit. The Amending Budget of 13 August 2026 changed no tax rate we could find.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate (art. 17) | 15% | 2026 | https://boe.incv.cv/Bulletins/Download/12387 |
| Electricity and water to final consumers (Budget art. 84) | 8% | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |
| Ice for licensed fish preservation | Exempt | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |
| Water for irrigated farming | Exempt | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |
| Goods moved out of the exempt list (Budget art. 32, Anexo I) | 15%, for the listed tariff codes | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |
| REMPE, micro turnover | Up to CVE 5,000,000: no IVA charged | 2026 | https://www.mf.gov.cv/documents/54571/273413/Desdobr%C3%A1vel%20REMPE.pdf |

## The base

Output tax on supplies, less input tax on valid invoices. Budget 2026 requires certified software for electronic invoices (art. 25(1)(f)), electronic issue (art. 32(13)) and a QR Code and unique document identifier (art. 32(17)). Self-billing needs a prior agreement, proof of acceptance and a special series marked autofaturacao (art. 32(13), 2024 text). Budget 2026 also lists import exemptions for specific goods, such as electric vehicles and solar panels: check the article for the good.

## Deadlines and filing

Monthly Modelo 106 with annexes, by the last day of the next month, even with no operations. Pay by the same date at a tax office, commercial bank, Home Banking, Vinti4 or online.

### How to file Modelo 106

1. Register: start of activity is Modelo 110 on the [DNRE page](https://www.mf.gov.cv/web/dnre/dire%C3%A7%C3%A3o-geral-das-contribui%C3%A7%C3%B5es-e-impostos); changes within 15 days, cessation within 30 days.
2. Prepare the clients and suppliers annexes.
3. Log in to Porton di Nos Ilha and submit Modelo 106 with the annexes.
4. Pay by the last day of the month.

Example: the February 2026 period was due 31 March 2026.

## Penalties and interest

The Calendario Fiscal says late or missing returns and unpaid tax are infractions under the Regime Juridico das Infracoes Tributarias Nao Aduaneiras, with fines and late-payment interest. That regime could not be opened, so no amount is given here.

## Cross-border points

A non-resident without an establishment acts through a resident representative named before the supply (art. 26); failing one, a business customer meets the obligations.

## Two worked examples that recompute

Case 1: sales CVE 200,000 at 15%, input tax CVE 12,000: pay CVE 18,000.

```oa-check
name: Monthly IVA
inputs:
  sales: 200000
  input: 12000
steps:
  - output: sales * 0.15
  - due: output - input
expected:
  output: 30000.00
  due: 18000.00
```

Case 2: electricity of CVE 10,000 to a final consumer: 8% is CVE 800, not CVE 1,500.

```oa-check
name: Electricity 8%
inputs:
  base: 10000
steps:
  - vat: base * 0.08
  - gap: base * 0.15 - vat
expected:
  vat: 800.00
  gap: 700.00
```


## Ask the client first

- REMPE or normal regime?
- What is supplied, and is the tariff code on the Budget Anexo I list?
- Any final-consumer electricity or water?
- Exports or supplies by non-residents?
- Is the software certified?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 69/X/2025, State Budget 2026, BO I 133 sup. 1, 31 Dec 2025: arts 29, 30, 32, 84, 99, 100 and Anexo I read | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 | 2026-11-01 |
| Lei 1/XI/2026, Amending Budget 2026, BO I 90, 13 Aug 2026: searched for tax-rate changes, none found | https://boe.incv.cv/Bulletins/DownloadAct?id=112975 | 2026-11-01 |
| Lei 21/VI/2003, IVA Code and Regulation, BO I 21, 14 Jul 2003 (original text): arts 17, 26 to 30, 47 to 54 read | https://boe.incv.cv/Bulletins/Download/12387 | 2026-11-01 |
| Lei 35/X/2023, Budget 2024: amendments to IRPC, REMPE and IVA read | https://boe.incv.cv/Bulletins/Download/5549 | 2026-11-01 |
| DNRE, Calendario Fiscal 2026, updated 11 Jun 2026: all months read | https://www.mf.gov.cv/documents/54571/0/Calendario_Fiscal_2026_PEC_Vers%C3%A3o_Atualizado_110626.pdf/7f524ec2-1b35-2f33-8936-42e8b752516e?version=1.0&t=1781260657225 | 2026-11-01 |
| DNRE, REMPE leaflet, 2015: all read | https://www.mf.gov.cv/documents/54571/273413/Desdobr%C3%A1vel%20REMPE.pdf | 2026-11-01 |
| DNRE, forms and leaflets page: list read | https://www.mf.gov.cv/web/dnre/dire%C3%A7%C3%A3o-geral-das-contribui%C3%A7%C3%B5es-e-impostos | 2026-11-01 |

Not yet confirmed: Lei 116/IX/2021 and every other amendment not listed in Sources; penalty amounts; interest rate. VAT registration threshold outside REMPE and the current art. 47 exemption; tourism at 8% (old skill); zero-rated exports and the imports listed in the old skill; current reverse charge wording on services from non-residents (art. 26 is the 2003 text); the Modelo 106 box numbers; refund procedure.

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
