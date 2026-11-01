---
name: gq-cross-border
description: >
  Cross-border tax in Equatorial Guinea for tax year 2026 under Ley 1/2024 General Tributaria. Covers the 10% tax on non-resident invoices, 15% on dividends and interest to non-residents, rent, permanent establishment tests of 90 and 183 days, gains on shares, foreign tax credit, VAT on foreign suppliers and platforms, and the hydrocarbon sector rate. Use for questions such as what withholding tax applies in Equatorial Guinea, how is a foreign contractor taxed, when do I have a permanent establishment, what is the tax on dividends paid abroad, and how does a non-resident pay. Applies to foreign companies, foreign individuals, and local payers. Treaty rates were not confirmed.
jurisdiction: GQ
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Equatorial Guinea Cross-Border Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Non-residents earning here, and local payers. Residence of individuals: see [Income tax](gq-income-tax.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Non-resident invoices | 10% of gross, charged to a local company's accounts, wherever performed (art 76) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Reimbursed expenses on that form | 0% (line 02) | 2026 | https://minhacienda-gob.com/uploads/2025/10/10_NO-RESIDENTES_SEC.COMUN_.pdf |
| Dividends, interest, other capital income to non-residents | 15% withheld (art 105.1.b) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Non-resident salary | 15% of gross (art 130.3) | 2026 | same |
| Hydrocarbon sector non-residents | 10% of gross (art 312.1.a) | 2026 | same |
| Rent | 5% (art 117) | 2026 | same |
| Royalties | unverified: 10% from the old skill as a separate rate; art 76 covers licences in its section title at 10% | 2026 | unverified |
| CEMAC cap on dividends and interest | unverified: 10% in the old skill, not in art 105 | 2026 | unverified |

## The base

A permanent establishment is a fixed place of business, including a branch, office, warehouse, factory or well (art 40). Site work over 90 days and services by staff over 183 days in 12 months on one project also count (art 40.3). Storage only is excluded (art 40.4).

Art 76 applies to gross invoices. Branch profits distributed are IRCM income on net profit (art 104.6). For a capital company, a subsidiary's net dividends are taxed in the parent less a share of costs fixed at 5% (art 50.1; the wording leaves the mechanism to confirm). The conditions are over 25% held for the prior 365 days, both companies in CEMAC, shares kept registered and held for 2 years, and no exempt or preferential company tax for the subsidiary in the last 10 years (art 50.2).

## Deadlines and filing

Payer steps on the [non-resident form](https://minhacienda-gob.com/uploads/2025/10/10_NO-RESIDENTES_SEC.COMUN_.pdf), code 3920: list suppliers with NIF, activity and amount; line 01 services at 10%; line 02 reimbursed costs at 0%; surcharge and interest; pay and lodge as in [VAT](gq-vat-gst.md). IRCM is due by the 15th of the following month, with a list of payees in the following month (art 107). VAT on foreign services is in the VAT skill.

## Penalties and interest

Arts 410, 411 and 412 apply; the form cites them. Oil sector: art 315.

## Cross-border points

Foreign tax is a credit up to local tax (art 44.1), and capital income relief needs a treaty (art 104.10). A non-resident pays IRCM on gains on local company shares if held for the previous 183 days or at 25% (art 103.2); the buyer and the company are jointly liable (art 108.2).

## Two worked examples that recompute

**Foreign consultant invoices 20,000,000 XAF plus 1,000,000 reimbursed costs.** Tax 2,000,000; costs at 0%.

```oa-check
name: Non-resident invoice
inputs:
  fees: 20000000
  costs: 1000000
steps:
  - tax: fees * 0.10 + costs * 0
expected:
  tax: 2000000
```

**Decision: contract stays under 183 days, or runs longer. Billing 100,000,000 XAF, costs 80,000,000.** Without an establishment: 10,000,000. With one: 25% of 20,000,000 is 5,000,000, above the 1,500,000 minimum. Longer presence costs 5,000,000 less tax, before compliance costs, if art 76 stops applying to the establishment.

```oa-check
name: Withholding against establishment
inputs:
  billing: 100000000
  costs: 80000000
steps:
  - gross_tax: billing * 0.10
  - pe_tax: max((billing - costs) * 0.25, billing * 0.015)
  - gap: gross_tax - pe_tax
expected:
  gross_tax: 10000000
  pe_tax: 5000000
  gap: 5000000
```

## Ask the client first

1. Payer or recipient, and residence?
2. Type of payment?
3. Days and staff on site?
4. Sector: oil, mining or other?
5. Is a treaty claimed?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 1/2024 General Tributaria, Boletin Oficial del Estado scan, read by OCR; arts 40, 44, 50, 76, 103 to 108, 117, 130, 312, 410 to 412 read | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf | 2026-11-01 |
| Non-resident withholding form, read | https://minhacienda-gob.com/uploads/2025/10/10_NO-RESIDENTES_SEC.COMUN_.pdf | 2026-11-01 |

The law is a scan with no text layer: figures were read from machine OCR, and the salary scale from the page image. It applies to tax year 2026; the 2026 Budget Law (Ley 9/2025) changes it only where stated.

Not yet confirmed: the treaty list and rates (the UK manual lists unilateral relief only and was not used); royalties; CEMAC cap; whether art 76 is final; whether a CEMAC convention changes these rates; resident company rate under art 105.

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
