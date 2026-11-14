---
name: mf-tgca-scope-and-compliance
description: >
  French Saint-Martin general turnover tax (taxe generale sur le chiffre d'affaires, TGCA) for 2026 under the collectivity's tax code consolidated to 5 June 2026. Covers who is liable, territorial rules for goods and services, the article 251 exclusions (imports, local producers, goods bought as stock), the export exemption that excludes the Dutch side, the 4% ordinary rate and the 2% affordable-housing works rate, the base and rounding, cash basis and the written debit election, no offset of TGCA paid, monthly returns (quarterly if annual tax is under 2,000 euros) by the 15th, registration within 15 days, foreign-supplier checks, and the 2026 email-and-transfer channel. Applies to French Saint-Martin, not Sint Maarten. Trigger phrases include TGCA Saint-Martin, taxe generale sur le chiffre d'affaires, Saint-Martin sales tax 4%, declaration TGCA.
version: "1.0"
jurisdiction: MF
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# French Saint-Martin: TGCA scope, calculation and returns v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This Guide addresses the French collectivity (MF). Its legal reference is the official **CGI consolidated through 5 June 2026**, articles 250–264, printed pages 305–314. The cover says only the underlying deliberations are authoritative. Subsequent amendments have not been exhaustively reconciled; this is a dated research draft, not confirmation of the law for every later transaction. [Official CGI](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

Collect transaction dates, supplier and customer establishments, goods movements, actual service use, invoices, inventory commitments, receipts, any written debit-basis election and annual tax due before choosing treatment. Sector exemptions under article 253 and special valuation rules require transaction-specific checking.

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Ordinary rate | 4% | Art. 259(1) | 2026 | [CGI Saint-Martin, art. 259](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |
| Affordable housing works | 2% | Construction and listed works for LLTS, LLS, PLS, LLI, PSLA and LES housing under the 7 August 2025 regulation (art. 259(2)) | 2026 | same |
| Base rounding | to the nearest euro, 0.50 rounded up | Art. 258 | 2026 | [CGI Saint-Martin, art. 258](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |
| Quarterly filing | allowed if annual tax due is strictly under 2,000 euros | Otherwise monthly | 2026 | [CGI Saint-Martin, art. 263](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |
| Return and payment | by the 15th of the month after the period | | 2026 | same |
| Registration (declaration d'existence) | within 15 days of starting operations | Also for persons established outside Saint-Martin | 2026 | [CGI Saint-Martin, art. 262](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |
| Cessation or disposal return | within 30 days | | 2026 | [CGI Saint-Martin, art. 263](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |

## The base

### Decide whether the transaction is taxable

TGCA applies to consideration-based supplies by independently acting taxable persons under article 250. For ordinary goods, article 252 looks at location on dispatch, installation or making available; special rules also cover imported goods and transport supplies. For services, a locally established provider falls within the territorial rule where the recipient is local **or** the service is used locally. Services of a foreign provider used locally also fall within it. A foreign billing address alone does not establish exclusion. [CGI arts. 250, 252](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

Article 251 excludes these goods transactions, subject to its conditions:

- Imports, whatever origin. It excludes both import after an overseas delivery and, if delivery did not take place overseas, the first local delivery following import. This does not exempt every subsequent resale.
- Invoiced deliveries by local producers to taxable persons, within the article's production definition.
- Invoiced deliveries to taxable purchasers committing to record the goods as inventory for resale or consumption in production/service provision. Fixed assets remain taxable unless the import or producer exceptions apply. Misuse of the inventory exclusion makes the purchaser liable for tax and penalties; a knowingly participating supplier can be jointly liable under article 260(6).

[CGI arts. 251, 260](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

For outward goods, article 254 requires an overseas purchaser and shipment outside the collectivity by or on the supplier's instructions. **The exemption does not apply to a purchaser in, or shipment to, the Dutch part of the island.** Retain invoice, payment proof, transport evidence and destination landing/import evidence signed by the competent authority, or the alternative destination declaration allowed at the tax administration's discretion. For an outward service claimed outside article 252, retain the specified invoice identifying the parties, service and remuneration, stating no local use, plus payment evidence. [CGI arts. 252(II)(3), 254](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

### Base and timing

| Rule | Treatment | Source |
|---|---|---|
| Ordinary base | Consideration including directly price-linked subsidies; other taxes and invoiced ancillary charges included; TGCA itself excluded | [CGI Saint-Martin, arts. 255 to 256](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |
| Direct customer discounts | Excluded from base | same |
| Tax becomes payable | On collection of payments and deposits unless a written debit-basis election applies; special self-supplies have their own rule | [CGI Saint-Martin, art. 257](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf) |

Do not treat every building project as eligible for 2%. The qualifying housing classifications are LLTS, LLS, PLS, LLI, PSLA and LES under the referenced regulation. Eligibility evidence remains necessary; this Guide does not independently resolve that regulation's criteria.

The written debit election covers all operations from the first day of the following month and continues until written withdrawal, also effective from the following month's first day. Under that election, unpaid amounts are deducted from taxable turnover when recorded as irrecoverable; subsequent recovery is reported in the receipt period. This specific adjustment is not a general input-tax credit. [CGI art. 257(3)](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

## Deadlines and filing

1. Classify goods/services, territorial scope and any evidenced exclusion or exemption.
2. Determine the appropriate ordinary or special base; separate payments by applicable rate and period. Do not mechanically use gross invoice value for commissions or travel-agency transactions with special article 255 bases.
3. Apply collection timing or the effective debit election, then the statutory base-rounding rule.
4. Multiply the eligible base by the applicable rate and reconcile to invoices and receipts. The official 2026 handbook states that TGCA paid on purchased services and fixed assets cannot be offset against TGCA collected. It describes expense accounting inclusive of TGCA and deduction in computing taxable results; ordinary expense deductibility still requires the appropriate income-tax analysis. [Business handbook, page 8](https://www.impots-saint-martin.fr/files/file/News/20%20PAGES%20LIVRET%20FISCAL%20COLLECTIVITE.pdf).
5. Declare and pay monthly. Quarterly calendar-period filing is allowed where **annual tax due is strictly below €2,000**. The deadline is the **15th of the month after the relevant period**. Register existence within **15 days of starting operations**; this applies to foreign-established persons with in-scope operations too. File the cessation/disposal return within **30 days**. [CGI arts. 255–258, 262–263](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

### Nil returns and submission

The 2026 handbook requires TGCA returns even without taxable turnover. Do not drop a period from the filing schedule simply because no sales occurred. [Business handbook, page 8](https://www.impots-saint-martin.fr/files/file/News/20%20PAGES%20LIVRET%20FISCAL%20COLLECTIVITE.pdf).

From January 2026, the official notice directs TGCA PDFs to `cfip.sxm.declarations-professionnels@dgfip.finances.gouv.fr`, with bank-transfer proof. Use one PDF per return and one recipient. Match email subject, PDF name and transfer reference using NIF, tax, year and TGCA month. The notice permits paper at Concordia for people without internet or unable to transmit a scan. [Official filing notice](https://www.impots-saint-martin.fr/).

Retain the completed return, calculation, transmission and payment evidence. Confirm current bank instructions directly from the authority before payment; this Guide does not reproduce account credentials.

## Penalties and interest

Misuse of the stock-purchase exclusion makes the purchaser liable for the tax and penalties, and a knowingly participating supplier can be jointly liable (art. 260(6)) ([CGI Saint-Martin](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf)). General penalty rates were not checked for this skill.

## Cross-border points

The supplier owes TGCA on taxable supplies. A taxable customer receiving goods/services from a foreign-established person must verify that supplier's tax registration and keep its certificate of liability; otherwise article 260(5) imposes joint liability. Do not replace this with an assumed universal customer reverse charge. Tax shown on an invoice is owed by the issuer under article 260(2), including erroneous charging. Invoice particulars must separately satisfy article 264. [CGI arts. 260, 264](https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf).

- Exports to the Dutch part of the island do not qualify for the article 254 exemption (see "The base").

## Two worked examples that recompute

Illustrative calculations, assuming ordinary taxable receipts with no exclusion: €10,000 base × 4% = **€400**. A fully evidenced eligible housing base of €10,000 × 2% = **€200**. Annual tax of €1,999 satisfies the quarterly threshold; €2,000 does not. A calendar Q1 return is due 15 April under the code's rule. These examples do not establish any particular taxpayer's eligibility or a special extension.

**Case 1: a monthly return with both rates.** Ordinary taxable receipts 10,000 at 4% = 400; an evidenced affordable-housing works base of 10,000 at 2% = 200; total 600 for the month, due by the 15th of the next month.

```oa-check
name: Saint-Martin TGCA monthly return, 4% and 2%
inputs:
  ordinary_base: 10000
  housing_base: 10000
steps:
  - ordinary_tgca: ordinary_base * 0.04
  - housing_tgca: housing_base * 0.02
  - total: ordinary_tgca + housing_tgca
expected:
  ordinary_tgca: 400.00
  housing_tgca: 200.00
  total: 600.00
```

**Case 2: decision, monthly or quarterly filing.** A business expects 2026 receipts of 49,975 euros at 4%: annual TGCA 1,999, strictly under 2,000, so it may file quarterly (Q1 due 15 April). At 50,000 euros of receipts the tax is exactly 2,000, which fails the strict test: monthly returns. The test is on annual tax due, not turnover.

```oa-check
name: Saint-Martin TGCA quarterly threshold
inputs:
  receipts_a: 49975
  receipts_b: 50000
  limit: 2000
steps:
  - tax_a: receipts_a * 0.04
  - tax_b: receipts_b * 0.04
  - headroom_a: limit - tax_a
  - headroom_b: limit - tax_b
expected:
  tax_a: 1999.00
  tax_b: 2000.00
  headroom_a: 1.00
  headroom_b: 0.00
```

## Ask the client first

1. Is the business in French Saint-Martin, and what does it supply (goods, services, imports)?
2. Where are customers and where are services used (local, Dutch side, abroad)?
3. Does it buy goods as stock under the article 251 commitment, or produce locally?
4. Cash basis, or has it filed a written debit election (and from when)?
5. Expected annual TGCA (quarterly test) and any affordable-housing works.
6. Any foreign suppliers, and do you hold their registration certificates?

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI de la collectivite de Saint-Martin, consolidated to 5 June 2026: read for arts. 250 to 264 (scope, exclusions, export, base, timing, rounding, 4% and 2% rates, registration, filing frequency, liability, invoices) | https://www.impots-saint-martin.fr/files/file/News/CGI_SM_au_05_06_2026.pdf | 2026-11-14 |
| Collectivite de Saint-Martin, livret fiscal (business handbook 2026): read for no offset of TGCA paid on purchases and nil returns | https://www.impots-saint-martin.fr/files/file/News/20%20PAGES%20LIVRET%20FISCAL%20COLLECTIVITE.pdf | 2026-11-14 |
| impots-saint-martin.fr home page notices: read for the January 2026 email-only filing, the TGCA mailbox, file-naming and bank transfer | https://www.impots-saint-martin.fr/ | 2026-11-14 |

Not yet confirmed: the article 253 sector exemptions in detail; the special bases for commissions and travel agencies; penalty rates; amendments after 5 June 2026; the eligibility criteria of the 7 August 2025 housing regulation.
