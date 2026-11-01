---
name: gq-vat-gst
description: >
  Value added tax (IVA) in Equatorial Guinea for tax year 2026 under Ley 1/2024 General Tributaria and the 2026 Budget Law. Covers the 15%, 5% and 0% rates, who must charge VAT, the absence of a turnover threshold, invoices, input deductions and blocked input VAT, the monthly return with box numbers, credits and refunds, import VAT, digital platforms, withholding by public bodies and penalties. Use for questions such as what is the VAT rate in Equatorial Guinea, do I need to register for VAT, IVA Guinea Ecuatorial, when is the VAT return due, how do I get a VAT refund, and is there VAT on imports. Applies to companies and individuals taxed under IS or IBN.
jurisdiction: GQ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Equatorial Guinea VAT v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone carrying on an economic activity for payment, regularly or occasionally (art 137). All IS and IBN taxpayers are in VAT whatever their form, income or activity: there is no turnover threshold (art 138.1). A business is a VAT taxpayer once it has an NIF and is registered (art 138.3, art 164). REAM traders are final consumers and do not charge or deduct VAT (arts 90.3, 138.2). The old note of a registration threshold is removed for that reason.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 15% on all taxable supplies not at 5% or 0% (art 155.2) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Reduced rate | 5% on the art 155.3 list, including baby food, hygiene products, bakery goods, rice, pasta, meat, fish, flour, fertiliser, pesticide, ordinary cement, local mineral water, and household water, gas and electricity | 2026 | same |
| Zero rate | 0% on exports and international transport, malaria drugs, medical masks and lab reagents, school books, chemotherapy and dialysis products, farm inputs, and certain subsoil products (art 155.4) | 2026 | same |
| Imports 2026, first list | 0% VAT, 5% duty on fish, rice, flour, yeast, feed, canned sardines, sugar, milk, meat, frozen potatoes, salt, tomato, eggs, pasta, pulses, oils, detergent, baby food, nappies and others (Budget art 13) | 2026 | https://minhacienda-gob.com/uploads/2026/05/libro-lpge-2026-bcb5ebfc7795.pdf |
| Imports 2026, second list | 5% VAT, 5% duty on biscuits and cereals, vegetables and fruit, dairy, cocoa powder, cement, chainsaws, pesticides, fertiliser, mineral water, mattresses, reinforcing steel, fishing gear (Budget art 13) | 2026 | same |
| Capital goods import self-assessment | Over 100,000,000 XAF (art 169) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Refund request minimum | 25,000,000 XAF credit (art 170.3.b) | 2026 | same |
| Refund on capital investment | Over 100,000,000 XAF (art 170.2.d) | 2026 | same |
| VAT withholding, when the tax administration requires it of public bodies or private companies | 100% for significant fiscal risk, including individuals and non-residents; 40% others; 0% resident Large Companies Unit members (art 167.4) | 2026 | same |
| Cash purchases | No input VAT over 300,000 XAF (art 158.1.h) | 2026 | same |
| Records | Keep 10 years (art 166.2) | 2026 | same |

## The base

Invoices must show the supplier's number, date, tax address, NIF, phone, email, signature and stamp, the net amount, rate, tax and total, and the customer's address, NIF, phone and email; a gap voids the invoice (arts 24, 165). Taxed and untaxed sales are kept apart (art 165.3). Input VAT is blocked on hotels, meals and entertainment (except those trades), oil products, gifts, free promotional goods, false invoices, and passenger vehicles with listed exceptions (art 158). Mixed businesses use a pro rata (arts 159, 160). Bad debts and cancelled sales are corrected by a duplicate invoice (art 163).

## Deadlines and filing

Return and payment are due by the 15th of the following month. A nil return is required (art 167). Steps on the [Regimen Real form](https://minhacienda-gob.com/uploads/2025/10/I.V.A.-REAL.pdf), code 1220:

1. Output VAT: 15% base and tax boxes 01 to 03, 5% boxes 04 to 06, 0% boxes 07 to 09.
2. Interest (art 412) boxes 010 to 012; surcharges (art 410) boxes 013 to 015.
3. Total output VAT, box 021.
4. Input VAT: domestic 022, imports 023, capital goods 025, regularisation 026, prior credits 027; total 028.
5. Box 029 is payable; if negative, box 030 is the credit to refund or carry.
6. Pay at a Treasury bank, lodge the form with proof at the Ministry (https://www.guineaecuatorialpress.com/noticias/presentacion_oficial_de_la_nueva_ley_general_tributaria_de_guinea_ecuatorial). The Ministry and Treasury then verify.

The Regimen a Destajo form on the https://minhacienda-gob.com/formularios-de-declaraciones-fiscales page has output boxes only, with no input VAT.

Credits carry forward (art 170.1). Refund or set-off within 3 months is open to legal persons, if compliant (art 170.3.a), that export, have structural credits from reduced rates, or invested over 100,000,000 XAF, and to diplomatic missions (art 170.2). Credits cannot be set against other taxes, except credits arising from a tax audit (art 170.6). Credit in a refund claim cannot be deducted the next month, and it is cancelled automatically if the refund is refused (art 170.5). Exporters attach export certificates and proof of repatriated funds, and the refund cannot exceed the VAT that the current rate would give on the period's exports (art 170.4).

## Penalties and interest

Surcharge 5%, 10% or 15% (art 410). Interest 2.5% a month or part (art 412). Unlawful VAT invoicing 25% (art 411.A.3.c). Credit cut after audit 10%, or 15% if already refunded (art 411.A.4).

## Cross-border points

A foreign supplier's service taxed here needs a solvent resident representative, jointly liable; failing that the withholding agent pays the VAT and penalties (art 146). Platforms that link non-resident providers with local clients are liable for VAT in their own name (art 139). Import VAT is paid before release from customs (art 168).

## Two worked examples that recompute

**Monthly return.** Sales 100,000,000 XAF at 15% give 15,000,000. Input VAT 9,000,000. Box 029 is 6,000,000. Paid 10 days late, add 5% surcharge and one month's interest.

```oa-check
name: Late monthly return
inputs:
  sales: 100000000
  input_vat: 9000000
steps:
  - due: sales * 0.15 - input_vat
  - surcharge: due * 0.05
  - interest: due * 0.025
  - total: due + surcharge + interest
expected:
  due: 6000000
  surcharge: 300000
  interest: 150000
  total: 6450000
```

**Decision: exporter with a credit, refund or carry forward.** A credit of 20,000,000 is under the minimum and carries forward. At 30,000,000 a refund claim is open, and that amount leaves the next return. If the refund is refused, the claimed credit is cancelled (art 170.5). Claim only if export VAT will not absorb it and the file is complete.

```oa-check
name: Refund eligibility gap
inputs:
  credit: 30000000
  minimum: 25000000
steps:
  - over: max(credit - minimum, 0)
expected:
  over: 5000000
```

## Ask the client first

1. IS, IBN or REAM taxpayer, and NIF obtained?
2. Goods or services, and are any on the 5% or 0% lists?
3. Imports or exports?
4. Customers that are public bodies?
5. Credit balance brought forward?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 1/2024 General Tributaria, Boletin Oficial del Estado scan, read by OCR; arts 24, 90, 137 to 139, 146, 155, 158 to 170, 410 to 412 read | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf | 2026-11-01 |
| Ley 9/2025, 2026 Budget Law, Title II arts 13 and 14 read | https://minhacienda-gob.com/uploads/2026/05/libro-lpge-2026-bcb5ebfc7795.pdf | 2026-11-01 |
| Ministry of Finance, tax return forms page, list read | https://minhacienda-gob.com/formularios-de-declaraciones-fiscales | 2026-11-01 |
| Government press office, 13 Jan 2025 presentation, read in full (filing route) | https://www.guineaecuatorialpress.com/noticias/presentacion_oficial_de_la_nueva_ley_general_tributaria_de_guinea_ecuatorial | 2026-11-01 |
| VAT Regimen Real form, read | https://minhacienda-gob.com/uploads/2025/10/I.V.A.-REAL.pdf | 2026-11-01 |

The law is a scan with no text layer: figures were read from machine OCR, and the salary scale from the page image. It applies to tax year 2026; the 2026 Budget Law (Ley 9/2025) changes it only where stated.

Not yet confirmed: who uses the Regimen a Destajo; reverse charge for a registered local customer, which was not found as such in the arts read (art 146 was); box 019 to 020 intracommunity lines; whether art 155 goods and Budget art 13 differ for domestic sales.

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
