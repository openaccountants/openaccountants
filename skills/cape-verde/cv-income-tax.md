---
name: cv-income-tax
description: "Personal income tax (IRPS) for Cape Verde (tax year 2026): bands, exemption, employment withholding, Modelo 112 and residence. Built from the Boletim Oficial and DNRE pages."
jurisdiction: CV
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cape Verde Personal Income Tax v0.2

## Who this applies to

Individuals resident in Cape Verde, on the income in the IRPS Code, and non-residents on income obtained in Cape Verde (IRPS Code). Sole traders under REMPE: see [corporate income tax](cv-corporate-income-tax.md) for the single tax. Currency: Cape Verdean escudo (CVE); tax year: calendar year.

## Rates, bands and thresholds

Basis for 2026: the law is the State Budget 2026 (Lei 69/X/2025, in force 1 January 2026), the DNRE Calendario Fiscal 2026 and the base code as published. No consolidated code was found, and Lei 116/IX/2021 could not be opened, so a row resting on original code text carries that limit. The Amending Budget of 13 August 2026 changed no tax rate we could find.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Band 1 | 16.5% up to CVE 960,000 a year | 2026 | https://boe.incv.cv/Bulletins/Download/1952 |
| Band 2 | 23.1% over CVE 960,000 up to CVE 1,800,000 | 2026 | same |
| Band 3 | 27.5% over CVE 1,800,000 | 2026 | same |
| Exempt taxable income (art. 45(2)) | Up to CVE 220,000 | 2026 | same |
| Monthly employee withholding, gross R up to 80,000 (art. 70) | 0.15R - 5,500 | 2026 | same |
| Over 80,000 to 150,000 | 0.21R - 10,300 | 2026 | same |
| Over 150,000 | 0.25R - 16,300 | 2026 | same |
| Category B and C withholding on account | 20% | 2026 | same |
| Category D withholding, final | 20%; 10% for art. 14(f) and (j) | 2026 | same |
| Category E withholding, final | 1% on art. 17(1)(a) to (d); 20% on art. 17(2) | 2026 | same |
| Family deduction from tax (art. 53) | CVE 5,000 each, maximum CVE 25,000 | 2026 | same |
| Deduction of 10% of rent, housing loan interest, education | Maximum CVE 12,500 | 2026 | same |
| Non-habitual resident | Taxed as such for 7 consecutive years from the year of registration | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |

## The base

Five categories are in the DPR table: A employment and pensions, B business and professional, C property, D capital, E gains. Category A is taxed by final progressive withholding unless the person opts to aggregate; on aggregation withholding becomes a payment on account. Withheld tax on account gives a refund if above the tax; art. 53 to 56 deductions do not. Health expenses (with a prescription) and court-ordered maintenance give a 10% deduction. Married couples: each person's withholding is computed separately and added. Pensioners use the same formula.

Resident: more than 183 days, continuous or not, in any 12 months; or a home at 31 December that is the habitual residence; or public duties abroad for Cape Verde; or specified crew.

## Deadlines and filing

Filed electronically on the Porton di Nos Ilha portal (the calendar names www.portondinosilha.cv).

| Who | Form | Date in 2026 |
|---|---|---|
| Category A only, optional | Modelo 112 | 31 March |
| Category B, C, transparent-company partners, non-residents | Modelo 112 | 31 May |
| Organised accounts | Modelo 1B | 31 May |
| Category B, annual accounting return | DAICF | 30 September for category B holders; organised accounts 31 July |
| Category B instalments | Portal | End March, August, November: 30% of prior-year tax each |
| Payers: withheld tax and DPR | DPR | 15th of next month |

### How to file Modelo 112

1. Hold a NIF (Modelo 109 is the registration form on the [DNRE page](https://www.mf.gov.cv/web/dnre/dire%C3%A7%C3%A3o-geral-das-contribui%C3%A7%C3%B5es-e-impostos)).
2. Log in to the portal.
3. Complete Modelo 112 following the DNRE filling instructions on that page.
4. Submit by the date above. A correction goes in within 30 days of the fact that changes declared income (IRPS art. 57(3)).

## Penalties and interest

The Calendario Fiscal says late or missing returns and unpaid tax are infractions under the Regime Juridico das Infracoes Tributarias Nao Aduaneiras, with fines and late-payment interest. That regime could not be opened, so no amount is given here.

## Cross-border points

Non-residents without a permanent establishment suffer the withholding rates; art. 51 makes them final with no aggregation. Category A non-resident code A.4 is 20% in the DPR table. The treaty list was not read.

## Two worked examples that recompute

Case 1, employee on CVE 60,000 a month: withholding is 0.15 x 60,000 - 5,500 = CVE 3,500.

```oa-check
name: Monthly withholding, gross 60,000
inputs:
  r: 60000
steps:
  - wh: r * 0.15 - 5500
expected:
  wh: 3500.00
```

Case 2, the decision between bands: CVE 100,000 is in the middle band, so 0.21 x 100,000 - 10,300 = CVE 10,700. Using the first formula would give CVE 9,500, CVE 1,200 too little.

```oa-check
name: Band choice, gross 100,000
inputs:
  r: 100000
steps:
  - right: r * 0.21 - 10300
  - wrong: r * 0.15 - 5500
  - gap: right - wrong
expected:
  right: 10700.00
  gap: 1200.00
```


## Ask the client first

- Resident under the 183-day or home test?
- Which income categories?
- Aggregating category A or not?
- Organised accounts or REMPE for business income?
- Non-habitual resident registered? Which year?
- Dependants and documented expenses?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 69/X/2025, State Budget 2026, BO I 133 sup. 1, 31 Dec 2025: arts 29, 30, 32, 84, 99, 100 and Anexo I read | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 | 2026-11-01 |
| Lei 1/XI/2026, Amending Budget 2026, BO I 90, 13 Aug 2026: searched for tax-rate changes, none found | https://boe.incv.cv/Bulletins/DownloadAct?id=112975 | 2026-11-01 |
| Lei 78/VIII/2014, Codigo do IRPS, BO I 81, 31 Dec 2014 (original text): arts 21, 45 to 53, 57, 70 to 74 read | https://boe.incv.cv/Bulletins/Download/1952 | 2026-11-01 |
| DNRE, Calendario Fiscal 2026, updated 11 Jun 2026: all months read | https://www.mf.gov.cv/documents/54571/0/Calendario_Fiscal_2026_PEC_Vers%C3%A3o_Atualizado_110626.pdf/7f524ec2-1b35-2f33-8936-42e8b752516e?version=1.0&t=1781260657225 | 2026-11-01 |
| DNRE, DPR FAQ v6: category table and Category A answers read | https://www.mf.gov.cv/documents/54571/273413/DPR%20%E2%80%93%20Perguntas%20Frequentes_FAQ_Vers%C3%A3o%206.pdf | 2026-11-01 |
| DNRE, forms and leaflets page: list read | https://www.mf.gov.cv/web/dnre/dire%C3%A7%C3%A3o-geral-das-contribui%C3%A7%C3%B5es-e-impostos | 2026-11-01 |

Not yet confirmed: Lei 116/IX/2021 and every other amendment not listed in Sources; penalty amounts; interest rate. Whether the employee INPS 8.5% is deductible (the old skill said so; also whether the withholding base is before or after it, the FAQ says "valor base de incidencia"); how the CVE 220,000 exemption interacts with the bands once exceeded; whether the 2014 withholding formula is the one in force; the FAQ also mentions CVE 420,000 and 35,000 a month for 2015; documented health, education and housing expenses scope; category E article references after amendment; non-resident rate equal to resident rate in all cases.

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
