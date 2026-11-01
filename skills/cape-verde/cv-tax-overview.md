---
name: cv-tax-overview
description: "Tax overview for Cape Verde (tax year 2026): main taxes, rates and dates, linked to the skill that owns each. Built from the Boletim Oficial and DNRE pages."
jurisdiction: CV
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cape Verde Tax Overview v0.2

## Who this applies to

Anyone needing a map of Cape Verde tax. Tax year: calendar year. Currency: escudo (CVE). DNRE runs tax today on its pages; DL 34/2025 approved the statutes of the Autoridade Tributaria e Aduaneira (ATCV, I.P.), which published acts in October 2026. INPS runs social security.

## Rates, bands and thresholds

Basis for 2026: the law is the State Budget 2026 (Lei 69/X/2025, in force 1 January 2026), the DNRE Calendario Fiscal 2026 and the base code as published. No consolidated code was found, and Lei 116/IX/2021 could not be opened, so a row resting on original code text carries that limit. The Amending Budget of 13 August 2026 changed no tax rate we could find.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Company tax | 20%: see [corporate](cv-corporate-income-tax.md) | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |
| Personal tax | 16.5% to 27.5%: see [income tax](cv-income-tax.md) | 2026 | https://boe.incv.cv/Bulletins/Download/1952 |
| VAT | 15%, 8% on electricity and water: see [VAT](cv-vat-gst.md) | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |
| REMPE single tax | 4% of gross sales | 2026 | https://boe.incv.cv/Bulletins/Download/1891 |
| Social contributions | 24.5%: see [payroll](cv-payroll-social.md) | 2026 | https://inps.cv/obrigacoes/ |
| Minimum tax | 15%, large groups | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |

## The base

Residents are taxed on income under the IRPS Code, non-residents on income obtained in Cape Verde. Each base is in the linked skill.

## Deadlines and filing

See the linked skills. Monthly: DPR on the 15th, Modelo 106 at month end. Annual: Modelo 1B and Modelo 112 on 31 May, DAICF on 31 July.

## Penalties and interest

The Calendario Fiscal says late or missing returns and unpaid tax are infractions under the Regime Juridico das Infracoes Tributarias Nao Aduaneiras, with fines and late-payment interest. That regime could not be opened, so no amount is given here.

## Cross-border points

See the linked skills.

## Two worked examples that recompute

Case 1: on CVE 1,000,000 of profit, IRPC is CVE 200,000.

```oa-check
name: IRPC
inputs:
  p: 1000000
steps:
  - t: p * 0.20
expected:
  t: 200000.00
```

Case 2, company or REMPE on sales of CVE 2,000,000: TEU is CVE 80,000; it beats IRPC if profit exceeds CVE 400,000.

```oa-check
name: TEU break-even
inputs:
  s: 2000000
steps:
  - teu: s * 0.04
  - profit: teu / 0.20
expected:
  teu: 80000.00
  profit: 400000.00
```


## Ask the client first

- Person or company?
- Resident?
- Turnover and workers?
- Which tax is the question about?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 69/X/2025, State Budget 2026, BO I 133 sup. 1, 31 Dec 2025: arts 29, 30, 32, 84, 99, 100 and Anexo I read | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 | 2026-11-01 |
| Lei 1/XI/2026, Amending Budget 2026, BO I 90, 13 Aug 2026: searched for tax-rate changes, none found | https://boe.incv.cv/Bulletins/DownloadAct?id=112975 | 2026-11-01 |
| Lei 78/VIII/2014, Codigo do IRPS, BO I 81, 31 Dec 2014 (original text): arts 21, 45 to 53, 57, 70 to 74 read | https://boe.incv.cv/Bulletins/Download/1952 | 2026-11-01 |
| Lei 70/VIII/2014, REMPE, BO I 51, 26 Aug 2014: arts on the TEU, 25 and 26 read | https://boe.incv.cv/Bulletins/Download/1891 | 2026-11-01 |
| INPS, Obrigacoes: all read | https://inps.cv/obrigacoes/ | 2026-11-01 |
| Deliberacao 06/CD/ATCV/2026, BO II 209, 30 Oct 2026: preamble read | https://boe.incv.cv/Bulletins/DownloadAct?id=114418 | 2026-11-01 |
| DNRE, Calendario Fiscal 2026, updated 11 Jun 2026: all months read | https://www.mf.gov.cv/documents/54571/0/Calendario_Fiscal_2026_PEC_Vers%C3%A3o_Atualizado_110626.pdf/7f524ec2-1b35-2f33-8936-42e8b752516e?version=1.0&t=1781260657225 | 2026-11-01 |

Not yet confirmed: Lei 116/IX/2021 and every other amendment not listed in Sources; penalty amounts; interest rate. CVE to EUR peg of 110.265 (Banco de Cabo Verde site did not open); other tax years by Ministry authorisation; worldwide basis wording for residents.

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
