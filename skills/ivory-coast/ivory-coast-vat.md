---
name: ivory-coast-vat
description: >
  Use this skill to prepare, review or explain a Côte d'Ivoire (Ivory Coast) VAT or TVA return for 2026. It covers who must charge VAT by regime, the 18% and 9% rates, exemptions and the 2026 changes for factoring and animal feed, the taxable base and when VAT falls due, mobile money deductibility, refunds of credits, monthly deadlines by taxpayer type, non-resident digital platforms and supplier classification on bank statements. Trigger on "TVA Côte d'Ivoire", "DGI return", "e-impots", "VAT Ivory Coast", "FNE", "crédit de TVA". ALWAYS read it before handling Ivory Coast VAT work. It is for businesses, accountants and foreign platforms selling into the country.
version: 2.1
jurisdiction: CI
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ivory Coast VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it without checking the cited official source or a licensed professional.

Tax year 2026. Authority: DGI. Currency XOF. Côte d'Ivoire is a WAEMU member (Benin, Burkina Faso, Guinea-Bissau, Mali, Niger, Senegal, Togo).

## Who this applies to

VAT payers are businesses on a real regime, so turnover TTC above 200,000,000, and those who opt in. TEE and micro taxpayers may not charge VAT or pass on a deduction (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page9.html). Agriculture is outside VAT unless the operator opts; the option threshold is 50,000,000 (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page76.html).

## Rates, bands and thresholds

| Item | Rate | Conditions | Source |
|---|---|---|---|
| Standard | 18% | On the price before tax | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page50.html |
| Reduced | 9% | Milk (not yoghurt or other dairy), durum wheat pasta, petroleum products, infant milk and foods, meat imported from outside ECOWAS, luxury rice | same |
| Exports | Exempt with refund right | Art. 355, Art. 382 | https://www.dgi.gouv.ci/assets/documents/IMPOTS%20ET%20TAXES%20EN%20COTE%20D%27IVOIRE%20.pdf |
| Factoring | 18% | Taxable from 2026, Art. 344 | https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page50.html |
| Jute and sisal fibre, animal feed, inputs and packaging for feed and for fertiliser | 18% | Exemption ended 2026, Art. 355-17, 27, 28, 30 | https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page51.html |
| Dessert bananas | Outside the fruit exemption | Art. 355-9 | https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page77.html |
| Fuel for vehicles and plant of opted farmers | 95% deductible | Art. 365 | https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page123.html |
| Refund on large capital goods | Over 40,000,000 TTC | Art. 382 | https://www.dgi.gouv.ci/assets/documents/PROCEDURE_DE_REMBOURSEMENT_DE_CREDIT_TVA.pdf |

Pre-2026 pages that still list animal feed as exempt are out of date; the annex wins.

## The base

Price, price supplements and incidental costs. Excluded: discounts on the invoice, damages, investment subsidies and true disbursements. Goods: VAT is due on delivery. Services: on payment received, unless authorised on debits. Between related parties, service VAT falls due after two years unpaid (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page49.html).

Exempt (Art. 355) include butane gas, books and newspapers, teaching, medicines, fertiliser, seeds, unprocessed meat and locally grown natural food fruit (https://www.dgi.gouv.ci/assets/documents/IMPOTS%20ET%20TAXES%20EN%20COTE%20D%27IVOIRE%20.pdf). Insurance is outside VAT under the insurance contract tax. Banking pays TOB at 10% or 5%, not VAT (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page51.html).

Mobile money payments escape the 250,000 XOF limit in Art. 373, so the charge stays deductible whatever the amount (https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page52.html).

Refund cases, Art. 382: exports, end of business, industrial investment, leasing, capital goods above 40,000,000 TTC, reduced rate supplies, convention exemptions. Other credits carry forward.

## Deadlines and filing

Monthly, by the 15th. DGE and DME: industry, oil, mining 10th; trade 15th; services 20th of the next month. Non-resident platforms and foreign gambling operators file online by the 15th under a simplified procedure (https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page50.html; https://www.dgi.gouv.ci/assets/documents/CALENDRIER.pdf).

Steps: 1. Total sales by rate, exempt sales and exports. 2. Total VAT on valid purchases; invoices must be supplier normalised invoices (FNE). 3. Log in at https://e-impots.gouv.ci as Contribuable. 4. Complete the return. 5. Submit and pay by the date; keep the receipt. 6. For a refund case, follow note 01248.

The earlier box map (unverified, form not opened): lines 1 to 10 output, 11 to 17 input, 18 to 21 net.

## Penalties and interest

Non-resident platforms that fail to declare or pay are listed each quarter by the 30th of the next month (Art. 438, 439, https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page113.html). General amounts: see the last line of Sources.

## Cross-border points

WAEMU is not an intra-community system; goods from Senegal pay VAT at customs. The VAT on foreign digital platforms is paid through the simplified route; the DGI publishes defaulters. Foreign platforms also face the 2026 profit tax in [Income tax](ivory-coast-income-tax.md).

## Two worked examples that recompute

Example 1. Sales 20,000,000 at 18%, purchases with 1,800,000 VAT.

```oa-check
name: Standard month
inputs:
  sales: 20000000
  input_vat: 1800000
steps:
  - output: sales * 0.18
  - due: output - input_vat
expected:
  output: 3600000
  due: 1800000
```

Example 2, a decision. Trader, turnover TTC 150,000,000, profit 20,000,000, clients want VAT invoices. Micro at 6% is 9,000,000 and no VAT. RSI option: profit tax 5,000,000 above the 3,000,000 minimum. The RSI costs 4,000,000 less and allows VAT invoices, with heavier filing. The option must be made before 1 February and holds three years.

```oa-check
name: Micro against RSI
inputs:
  turnover: 150000000
  profit: 20000000
steps:
  - micro: turnover * 0.06
  - rsi: max(profit * 0.25, max(turnover * 0.005, 3000000))
  - saving: micro - rsi
expected:
  micro: 9000000
  rsi: 5000000
  saving: 4000000
```

## Working material carried from the earlier version

### 3.1 Ivorian banks (exempt -- exclude)

**Ivorian banks (exempt -- exclude)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SGCI, SOCIETE GENERALE CI | EXCLUDE | Exempt financial service |
| BICICI | EXCLUDE | Same |
| ECOBANK CI, NSIA BANQUE | EXCLUDE | Same |
| BOA CI, BRIDGE BANK | EXCLUDE | Same |

### 3.2 Government

**Government**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGI | EXCLUDE | Tax payment |
| DOUANE | Check for import TVA | TVA recoverable |
| CNPS | EXCLUDE | Social security |

### 3.3 Utilities

**Utilities**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CIE, ELECTRICITE | Domestic 18% | Electricity |
| SODECI | Domestic 18% | Water |
| MTN CI, ORANGE CI, MOOV | Domestic 18% | Telecoms |

### 3.4 SaaS

**SaaS**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, AWS | Check: reverse charge unconfirmed | Non-resident; see the last line of Sources |

Edge cases: capital goods adjustment and Investment Code firms go to a reviewer. Never confuse exempt with zero. Never treat WAEMU as intra-community. Reject invoices without the supplier's NCC.

## Ask the client first

1. Regime and turnover TTC?
2. What is sold, and is any of it at 9% or exempt?
3. Exports or supplies to foreign customers?
4. Tax office, DGE or DME, and sector?
5. Investment Code or a convention?

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Annexe fiscale 2026 (loi n° 2025-987), note de service and arts. 1 to 41 headings; articles quoted here read in full | https://www.dgi.gouv.ci/assets/documents/ANNEXE_FISCALE_2026/files/basic-html/page2.html | 2026-11-01 |
| DGI, Le système fiscal ivoirien (undated e-book, predates the 2026 annex; the annex wins where they differ), pp. 3-51 read | https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page3.html | 2026-11-01 |
| DGI, Impôts et taxes en Côte d'Ivoire, édition 2025 (art. 146 table, regimes, IRVM, VAT sections read) | https://www.dgi.gouv.ci/assets/documents/IMPOTS%20ET%20TAXES%20EN%20COTE%20D%27IVOIRE%20.pdf | 2026-11-01 |
| DGI, Calendrier des obligations fiscales (VAT and BIC parts read) | https://www.dgi.gouv.ci/assets/documents/CALENDRIER.pdf | 2026-11-01 |
| DGI note n° 00026 of 3 Jan 2024, employer contribution part read | https://www.dgi.gouv.ci/assets/documents/DOCTRINE%20FISCALE%202024/IMPOTS%20DIRECTS/IMPOT%20SUR%20LES%20TRAITEMENTS,%20SALAIRES,%20PENSIONS%20ET%20RENTES%20VIAGERES/N%C2%B0%2000026%20MFB%20DGI%20DLCD%20DU%2003%20JAN%202024%20Pr%C3%A9cisions%20relatives%20aux%20am%C3%A9nagements%20...%20des%20salari%C3%A9s.pdf | 2026-11-01 |
| DGI note n° 01248 on VAT credit refunds, opening part read | https://www.dgi.gouv.ci/assets/documents/PROCEDURE_DE_REMBOURSEMENT_DE_CREDIT_TVA.pdf | 2026-11-01 |
| CNPS, communiqué on ceilings from 1 Jan 2023 (whole notice read) | https://www.cnps.ci/wp-content/uploads/2023/01/NOUVEAU-PLAFOND-DES-COTISATIONS-SOCIALES-DE-LA-CNPS.pdf | 2026-11-01 |
| CNPS, employer page (paying contributions read; its SMIG and pension ceiling are out of date, the communiqué wins) | https://www.cnps.ci/employeur | 2026-11-01 |

Not yet confirmed: the full consolidated Code général des Impôts and Livre de Procédures fiscales 2026 (DGI lists them in its paid kiosk; the text was not opened), so article numbers come from the DGI documents above; rule that a reverse charge applies at 18% to foreign services (earlier version, Art. 344 not read for it); blocked input VAT list, prorata and the 500,000 gift limit (Art. 359 to 363 cited earlier; note the DGI places rates at Art. 359, so those references need checking); capital goods adjustment periods; quarterly filing for RSI, which the DGI text does not support (RSI files monthly, https://www.dgi.gouv.ci/assets/documents/EBOOK/LE_SYTEME_FISCAL_IVOIRIEN/files/basic-html/page10.html); late filing 25% and 100%, late payment 1% a month; FNE rules and e-impots form boxes.

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
