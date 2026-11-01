---
name: cv-corporate-income-tax
description: "Corporate income tax (IRPC) for Cape Verde (tax year 2026): 20% rate from 1 January 2026, REMPE single tax, instalments, losses, Pillar Two. Built from the Boletim Oficial and DNRE pages."
jurisdiction: CV
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cape Verde Corporate Income Tax v0.2

## Who this applies to

Companies and other entities in the IRPC, resident or with a permanent establishment, on adjusted accounting profit; non-residents without one, by withholding. Micro and small companies in REMPE pay the Tributo Especial Unificado (TEU) instead.

## Rates, bands and thresholds

Basis for 2026: the law is the State Budget 2026 (Lei 69/X/2025, in force 1 January 2026), the DNRE Calendario Fiscal 2026 and the base code as published. No consolidated code was found, and Lei 116/IX/2021 could not be opened, so a row resting on original code text carries that limit. The Amending Budget of 13 August 2026 changed no tax rate we could find.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| IRPC rate, organised accounts (art. 84(1)) | 20% | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |
| Rate to 31 Dec 2025 | 21% | 2025 | https://boe.incv.cv/Bulletins/Download/5549 |
| TEU (REMPE art. 25) | 4% of gross sales | 2026 | https://boe.incv.cv/Bulletins/Download/1891 |
| TEU minimum, micro company turnover up to CVE 1,000,000 | CVE 30,000 a year, pro rata in a start year | 2026 | same |
| TEU retention by organised-accounts payers (art. 25-A) | 4% on account of the quarter | 2026 | https://boe.incv.cv/Bulletins/Download/5549 |
| REMPE micro | Turnover up to CVE 5,000,000 and/or up to 5 workers | 2026 | https://www.mf.gov.cv/documents/54571/273413/Desdobr%C3%A1vel%20REMPE.pdf |
| REMPE small | Turnover CVE 5,000,000 to 10,000,000 and/or 6 to 10 workers | 2026 | same |
| REMPE exit | Over 30% above the art. 3(1)(c) turnover in a year: excluded next year | 2026 | https://boe.incv.cv/Bulletins/Download/6150 |
| Qualified minimum tax (IMG) | 15%, groups with EUR 750,000,000 revenue in 2 of the prior 4 years; detail in separate rules | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |
| Capital income withholding (art. 85) | 20%, some items 10%; on account for organised accounts, otherwise final | 2026 | https://boe.incv.cv/Bulletins/Download/1957 |
| Loss deduction cap per year (art. 59(2)) | 50% of taxable profit | 2026 | https://boe.incv.cv/Bulletins/Download/1957 |
| Fractional payments (calendar) | 30% of prior-year tax at end March, August and November | 2026 | https://www.mf.gov.cv/documents/54571/0/Calendario_Fiscal_2026_PEC_Vers%C3%A3o_Atualizado_110626.pdf/7f524ec2-1b35-2f33-8936-42e8b752516e?version=1.0&t=1781260657225 |
| Category B and transparent regime payments (art. 96(3)) | 15% of prior-year taxable profit, in 3 equal parts | 2026 | https://boe.incv.cv/Bulletins/Download/4568 |
| Start-up Jovem IRPC | 5% for 5 years; 2.5% for ICT and R&D, on conditions | 2026 | https://boe.incv.cv/Bulletins/Download/4568 |
| R&D credit | 40% base, 50% incremental | 2026 | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 |

## The base

Start from accounting profit, adjust under the Code. Losses carry forward; the 2024 budget text removes the original 7-year wording from art. 59(1), and art. 59(2) kept its place. Health insurance premiums are deductible up to 20% of staff costs if they cover staff generally on one plan (art. 35(3)). Art. 68 limits financing costs, with exceptions for Banco de Cabo Verde supervised entities and approved projects. A group regime exists (arts 59-A to 59-C). Transfer prices must be at arm's length (art. 65).

The TEU replaces income tax, VAT, fire tax and the employer social contribution. Workers must still be registered with INPS.

## Deadlines and filing

| Who | Form | Date in 2026 |
|---|---|---|
| Organised accounts, annual return | Modelo 1B | 31 May |
| Accounting return | DAICF | 31 July |
| Instalments | Portal | 31 March, 31 August, 30 November |
| REMPE, quarterly | Modelo 107 with purchase and sales books; pay TEU | 31 January, 30 April, 31 July, 31 October |
| REMPE micro exempt from TEU | Annual turnover return | 31 January |
| SAF-T inventories | saft.efatura.cv | 31 January |
| Investment credit evidence | Portal | 31 July |

### How to file Modelo 1B

1. Log in to Porton di Nos Ilha.
2. Complete Modelo 1B with the DNRE instructions.
3. Submit by 31 May, working day or not (art. 102).
4. Pay the balance. Then file the DAICF.

### How to file Modelo 107

Generate the XML in software, validate against the XSD DNRE publishes, upload with both books, and pay at a tax office, bank, Home Banking, Vinti4 or online.

## Penalties and interest

The Calendario Fiscal says late or missing returns and unpaid tax are infractions under the Regime Juridico das Infracoes Tributarias Nao Aduaneiras, with fines and late-payment interest. That regime could not be opened, so no amount is given here.

## Cross-border points

Non-residents without a permanent establishment: final withholding at IRPS rates; if none applies, a compulsory return at the general rate (art. 86, which still prints 25% in the 2015 text; art. 84(1) is now 20%). Treaty relief: not read.

## Two worked examples that recompute

Case 1: taxable profit CVE 5,000,000 at 20% is CVE 1,000,000. With instalments from prior-year tax of CVE 800,000, 3 x 240,000 is paid, leaving CVE 280,000.

```oa-check
name: IRPC and balance
inputs:
  profit: 5000000
  prior: 800000
steps:
  - tax: profit * 0.20
  - paid: prior * 0.30 * 3
  - balance: tax - paid
expected:
  tax: 1000000.00
  paid: 720000.00
  balance: 280000.00
```

Case 2, REMPE or organised accounts: sales CVE 4,000,000, profit CVE 900,000. TEU CVE 160,000; IRPC CVE 180,000. On income tax alone REMPE wins by CVE 20,000, before VAT and employer INPS, which REMPE also removes.

```oa-check
name: REMPE or organised accounts
inputs:
  sales: 4000000
  profit: 900000
steps:
  - teu: sales * 0.04
  - irpc: profit * 0.20
  - saving: irpc - teu
expected:
  teu: 160000.00
  irpc: 180000.00
  saving: 20000.00
```


## Ask the client first

- Organised accounts or REMPE?
- Turnover and workers?
- Prior-year tax?
- Part of a group, or over EUR 750 million?
- Incentives claimed (Start-up Jovem, R&D, investment credit)?
- Payments to non-residents?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 69/X/2025, State Budget 2026, BO I 133 sup. 1, 31 Dec 2025: arts 29, 30, 32, 84, 99, 100 and Anexo I read | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 | 2026-11-01 |
| Lei 1/XI/2026, Amending Budget 2026, BO I 90, 13 Aug 2026: searched for tax-rate changes, none found | https://boe.incv.cv/Bulletins/DownloadAct?id=112975 | 2026-11-01 |
| Lei 82/VIII/2015, Codigo do IRPC, BO I 3, 8 Jan 2015 (original text): arts 59, 84 to 86, 96, annual return read | https://boe.incv.cv/Bulletins/Download/1957 | 2026-11-01 |
| Lei 70/VIII/2014, REMPE, BO I 51, 26 Aug 2014: arts on the TEU, 25 and 26 read | https://boe.incv.cv/Bulletins/Download/1891 | 2026-11-01 |
| Lei 16/X/2022, Budget 2023: arts 32 to 34 read | https://boe.incv.cv/Bulletins/Download/4568 | 2026-11-01 |
| Lei 35/X/2023, Budget 2024: amendments to IRPC, REMPE and IVA read | https://boe.incv.cv/Bulletins/Download/5549 | 2026-11-01 |
| Lei 45/X/2024, Budget 2025: arts 25 and 26 read | https://boe.incv.cv/Bulletins/Download/6150 | 2026-11-01 |
| DNRE, Calendario Fiscal 2026, updated 11 Jun 2026: all months read | https://www.mf.gov.cv/documents/54571/0/Calendario_Fiscal_2026_PEC_Vers%C3%A3o_Atualizado_110626.pdf/7f524ec2-1b35-2f33-8936-42e8b752516e?version=1.0&t=1781260657225 | 2026-11-01 |
| DNRE, REMPE leaflet, 2015: all read | https://www.mf.gov.cv/documents/54571/273413/Desdobr%C3%A1vel%20REMPE.pdf | 2026-11-01 |
| DNRE, forms and leaflets page: list read | https://www.mf.gov.cv/web/dnre/dire%C3%A7%C3%A3o-geral-das-contribui%C3%A7%C3%B5es-e-impostos | 2026-11-01 |

Not yet confirmed: Lei 116/IX/2021 and every other amendment not listed in Sources; penalty amounts; interest rate. Fire surcharge (Taxa de Incendio) of 2% in Praia and Mindelo and the 20.40% effective rate: the tax exists in the budget, the rate was not found; the art. 85 list of 10% items; old rates of 10% on bonds, 5% on listed bonds and full dividend relief; 20% on royalties; 15% on services to non-residents; whether the third instalment is 30% (calendar) or 20% (2015 text; the calendar is followed); the calendar month August against July in the 2015 text; loss carry-forward period after the 2024 change; whether the TEU 2.8% and 3.2% codes in the DPR FAQ are current; the TEU reductions in art. 41; any later change to the 4% rate.

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
