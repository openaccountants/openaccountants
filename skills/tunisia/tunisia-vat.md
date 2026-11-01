---
name: tunisia-vat
description: "Tunisia VAT (TVA) for tax year 2026: 19%, 13% and 7% rates, the TND 400,000 developer cap, suspension versus exemption, State withholding at 25% of the VAT, customer withholding on non-established suppliers, blocked input, monthly return dates, e-invoicing widening and a bank statement pattern library. Use whenever asked to prepare, review or classify transactions for a Tunisian VAT return, or any question on TVA rates or filing. ALWAYS read before handling Tunisia TVA work. Unopened items are marked unverified."
version: 2.1
jurisdiction: TN
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tunisia VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Those making taxable supplies in Tunisia, those who invoice VAT, and those who opt in (Code TVA art. 2). The code sets no general TND 100,000 goods or 50,000 services registration threshold; the old figures were not found. The TND 100,000 in art. 2 concerns retail traders reselling goods. Flat-tax payers under Code IRPP-IS art. 44 bis may opt in.

Out of scope for escalation: offshore companies (R-TN-1).

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Standard rate | 19% | 2026 | Everything not at another rate. Art. 7 | https://web.archive.org/web/20250906073223/https://jibaya.tn/wp-content/uploads/2024/02/Code-de-la-taxe-sur-la-valeur-ajoutee-2023_compressed.pdf |
| Reduced rate | 7% | 2026 | Table B: includes transport, lodging and catering services. Check the exact line | same |
| Intermediate rate | 13% | 2026 | Listed petroleum products; domestic low-voltage electricity above 300 kWh a month. Art. 7(3), LF 2025 art. 31 | https://web.archive.org/web/20251205000847/https://jibaya.tn/wp-content/uploads/2024/12/Loi2024_48.pdf |
| New homes by developers | 7% up to TND 400,000 excl. VAT | 2026 | To individuals or public developers; Table B no. 31. The 13% line is repealed, so above the cap the 19% default applies. LF 2025 art. 64 | same |
| Lithium battery inputs | 7% | 2026 | Listed non-local inputs. LF 2026 art. 46 | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf |
| State withholding | 25% of the VAT | 2026 | Payments of TND 1,000 or more incl. VAT by State, local bodies, public entities; phone, water, power exempt. Art. 19 bis | https://web.archive.org/web/20250906073223/https://jibaya.tn/wp-content/uploads/2024/02/Code-de-la-taxe-sur-la-valeur-ajoutee-2023_compressed.pdf |
| Non-established supplier | Customer withholds all VAT | 2026 | Art. 19 | same |
| Cash purchase block | TND 5,000 excl. VAT | 2026 | No deduction if paid in cash. Art. 10 | same |
| Late filing | unverified: 1% a month, min TND 50, old file | 2026 | Tax Procedures Code not opened | unverified |
| Late payment | unverified: 0.75% a month, old file | 2026 | same | unverified |

Hotels at 13% and legal or accounting services at 13% in the old file are wrong against art. 7: lodging is in Table B and professional services take the default rate. Exempt lines include bread, flours and pasta (Table A no. 41) and insurance under the single tax; finance, education and medical exemptions are in Table A and must be checked line by line.

## The base

Taxable amount includes the price and charges (art. 6). Excise (droit de consommation) sits in the VAT base.

No deduction (art. 10): passenger cars not used as the trade itself, their hire and running costs; supplies from flat-tax payers; cash payments of TND 5,000 or more; payments to privileged-tax jurisdictions.

Suspension is not a zero rate: certain buyers acquire without VAT on an attestation. Do not sell under suspension without seeing it. Art. 11 opens the regime to those whose exports pass 50% of turnover; the 80% test in the old file is not in the text read. LF 2026 adds suspension for listed bodies and updates art. 13 bis (arts. 16, 17, 19, 33, 44, 86).

Credit refund: exports, suspension sales and withheld VAT from a monthly return (art. 15). Mixed supplies use a prorata; the rule that suspension turnover counts in the numerator comes from the old file.

### Supplier patterns

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BIAT | EXCLUDE | Exempt financial |
| BNA, BANQUE NATIONALE AGRICOLE | EXCLUDE | Same |
| AMEN BANK, STB | EXCLUDE | Same |
| BT, ATB | EXCLUDE | Same |
| DGI | EXCLUDE | Tax payment |
| DOUANE | Check for import TVA |  |
| CNSS, CNRPS | EXCLUDE | Social security |
| STEG | 7% or 13% domestic low voltage by consumption, otherwise check | Electricity |
| SONEDE | Check rate | Water |
| TUNISIE TELECOM, OOREDOO TN, ORANGE TN | Domestic 19% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Autoliquidation 19% | Non-resident |

## Deadlines and filing

Monthly return, no quarterly option in art. 18: within 15 days for individuals, 28 days for legal persons, with a nil return if nothing is due. The DGI calendar for June 2026 showed 15 June for individuals and 22 June for legal persons on online filing, so check that month's calendar. Occasional sellers file in 48 hours. E-invoicing now also covers service supplies listed by the decree under art. 18 II ter (LF 2026 art. 53).

Steps: 1. Join online filing with the adhesion form at the tax office. 2. Get an ANCE certificate. 3. Complete the monthly return (form mensuelle 2026) on jibaya.tn and pay. The old file's line map (output 1 to 13, input 14 to 21, net 22 to 25) was not matched to the 2026 form.

## Penalties and interest

See the two unverified rows above. Keep invoices with the supplier's tax number.

## Cross-border points

A foreign supplier with no Tunisian establishment: the customer withholds the VAT (art. 19). Such as SaaS bought in from Google, Microsoft or AWS at 19%. The supplier may instead declare and deduct (art. 19(2)). Whether the customer deducts this VAT follows art. 9. Exports are exempt (Table A).

## Two worked examples that recompute

Simple: ministry pays TND 50,000 plus VAT 9,500. Withholding 25% = 2,375; the supplier credits it.

```oa-check
name: State withholding
inputs:
  net: 50000
steps:
  - vat: net * 0.19
  - withheld: vat * 0.25
expected:
  vat: 9500.00
  withheld: 2375.00
```

Decision: home at TND 380,000 or TND 450,000. Below the cap VAT is 26,600 at 7%; above, 85,500 at 19%. The cap decides the rate for the whole price.

```oa-check
name: Developer sale either side of the cap
inputs:
  low: 380000
  high: 450000
steps:
  - vat_low: low * 0.07
  - vat_high: high * 0.19
  - gap: vat_high - vat_low
expected:
  gap: 58900.00
```

## Ask the client first

1. Individual or company, and taxable or flat-tax?
2. What goods or services, for Table A or B?
3. Any exports or suspension sales, with attestations?
4. Foreign suppliers without a Tunisian establishment?
5. Sales to the State or public bodies?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code de la TVA, 2023 French edition, archived copy of the DGI file; arts. 2, 7, 10, 15, 18, 19, 19 bis and Tables A and B read. The 2026 edition PDF could not be opened | https://web.archive.org/web/20250906073223/https://jibaya.tn/wp-content/uploads/2024/02/Code-de-la-taxe-sur-la-valeur-ajoutee-2023_compressed.pdf | 2026-11-01 |
| Loi n° 2024-48 du 9 decembre 2024, loi de finances 2025, archived copy of the DGI file; arts. 31, 64 and the job-loss fund article read | https://web.archive.org/web/20251205000847/https://jibaya.tn/wp-content/uploads/2024/12/Loi2024_48.pdf | 2026-11-01 |
| Loi n° 2025-17 du 12 decembre 2025, loi de finances 2026, JORT n° 148, archived copy of the DGI file; tax articles read | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf | 2026-11-01 |
| DGI professional space with tax calendar, archived 8 June 2026; calendar entries read | https://web.archive.org/web/20260608115736/https://jibaya.tn/ar/espace-professionnel/ | 2026-11-01 |
| DGI page on online filing, archived April 2025; steps read | https://web.archive.org/web/20250419084126/https://jibaya.tn/blog/la-tele-declaration-fiscale/ | 2026-11-01 |

Not yet confirmed: Late penalties. Suspension 80% test. Prorata numerator. Table A and B 2026 changes, since the 2026 and 2025 consolidated PDFs would not open and LF 2024 was not read. General rule behind the 22nd in the DGI calendar. Excise example with 25% rate. Return line numbers. Supplier pattern treatments of telecom and water rates, carried from the old file.

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
