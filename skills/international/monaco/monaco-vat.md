---
name: monaco-vat
description: "Monaco VAT working paper for 2026 using the Monaco turnover tax code and the France Monaco convention. Covers standard rate calculations, ordinary franchise thresholds, start date and threshold crossing tests, input deduction, business service reverse charge, monthly or permitted quarterly filing, Monaco DSF procedures and statutory penalties. Use for Monaco TVA, VAT returns, small business exemption and foreign service questions. Requires transaction evidence and the assigned filing calendar. Includes reproducible examples, records unresolved special regimes and live forms, and awaits a named Monaco professional review."
version: 2.1
jurisdiction: MC
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Monaco VAT v2.1

> **Source-cited draft; partial scope.** Checked 24 October 2026. No named Monaco professional has reviewed this Guide. It produces a working paper, not a filing or a final tax position. Read the [country gap register](README.md) before use.

## Who this applies to

Tax year 2026. Apply Monaco's Code des taxes sur le chiffre d'affaires to taxable transactions, establishments and recipients. The France–Monaco convention aligns turnover taxes on the same bases and rates; it does not justify replacing Monaco filing rules with an assumed Nice tax-office procedure. Ordinary taxable business services use article 11's recipient/provider location tests, subject to the special rules that follow. Establish transaction type, tax point, customer status and the establishment receiving the service before assigning a rate. [Convention, art. 15](https://legimonaco.mc/tai/convention/1963/05-18-tai1l000235/); [Code, arts. 1, 11–14, A-139](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

This draft covers ordinary standard-rated supplies, an ordinary small-business franchise screen and a business-service reverse-charge illustration. Reduced rates, property, special schemes, imports, intra-community exemptions and electronic-invoicing transition rules need transaction-specific review. Never infer exemption or deduction from a bank merchant's name.

## Rates, bands and thresholds

| Item | Amount | Period | Official source |
|---|---|---|---|
| Standard rate | 20% | 2026 | [Art. 51](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Ordinary franchise, prior-year national turnover | Total EUR 85,000; relevant service subset EUR 37,500 | 2026 screen | [Art. 87(I)](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Ordinary franchise, current-year national turnover | Total EUR 93,500; relevant service subset EUR 41,250 | 2026 screen | [Art. 87(I), (III)](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Quarterly filing permission | Annual tax strictly below EUR 4,000 | 2026 | [Art. 70(2)](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |
| Late-payment interest | 0.20% per month | 2026, statutory conditions | [Art. 110](https://legimonaco.mc/code/code-taxes-chiffre-affaires) |

## The base

For an established ordinary business, test both total national turnover and the service subset excluding on-premises consumption and accommodation. The prior-year and current-year tests differ. Crossing either current-year ceiling ends franchise for transactions from the crossing date. Special authors/artists thresholds are outside this ordinary screen. Article 89 defines included/excluded turnover and prorates thresholds for a mid-year start. Article 88 has exclusions. Its July 2026 amendment and article 89 changes specify application from 21 February 2026: inspect the transaction date. [Arts. 87–89](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

A franchise business cannot deduct input VAT or show VAT on invoices; article 90 prescribes “TVA non applicable, article 87 du Code des taxes”. Article 91 allows an option effective the first day of the declaration month, covering two years including that year, with renewal conditions. Reverse-charge obligations require a separate test; franchise is not a universal exemption from all recipient obligations. [Arts. 62, 87–91](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

For ordinary taxable business, reconcile output VAT, recipient-accounted VAT and deductible input VAT. Article 42 conditions deduction; invoice requirements are in article 71. A general-rule B2B service supplied by a taxable supplier established outside both Monaco and France to a Monaco taxable recipient is screened under articles 11 and 62(2). Self-assessment does not automatically create an equal deduction. Confirm invoice, business use, taxable use, exclusions and timing. Do not default an unknown counterparty to domestic treatment. [Arts. 11, 42, 62(2), 71](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

## Deadlines and filing

Article 66 registration and article 68 identification must be assessed before filing; the current application form and portal onboarding have not been operationally tested. Article 70 requires an administration-prescribed return to the Recette des taxes, ordinarily monthly with monthly payment. Annual tax below EUR 4,000 permits quarterly declarations; exactly EUR 4,000 does not meet that condition. Cessation requires a declaration within thirty days. [Arts. 66, 68, 70](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

Under A-139, file ordinary declarations with Monaco DSF. A-144 allows DSF category-specific filing periods; absent one, the declaration must be submitted **before the 25th**. It moves the deadline to the next working day when it coincides with a public holiday or deemed holiday. Nil returns remain required, with the stated seasonal-closure exception. A-145 governs authorised extra time, not an automatic extension. Confirm the taxpayer's assigned calendar and actual form with DSF; no live return was filed for this research. [Annex, A-139, A-144–A-145](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

## Penalties and interest

Article 110 sets 0.20% monthly late-payment interest on unpaid or deferred amounts, calculated from the first day of the month following the due month through the last day of the payment month. Article 111 adds a 10% late/non-declaration surcharge, escalating to 40% after the first unanswered thirty-day formal notice and 80% after the second; hidden activity also attracts 80%. Article 112 adds 40% for established bad faith on inaccurate/insufficient declarations, 80% for fraud. These provisions have different triggers; do not stack percentages without establishing the facts and applicable procedural rule. [Arts. 110–112](https://legimonaco.mc/code/code-taxes-chiffre-affaires).

## Cross-border points

Use Monaco Code transaction-location rules and the France–Monaco framework; distinguish goods from services, France from another state, establishment from invoice address and import from recipient-accounted service VAT. This draft does not establish the documents, reporting or eligibility for intra-community exemption, export exemption or special online schemes. Route them to a current Monaco VAT specialist. Never turn a foreign customer name into automatic zero-rating. [Arts. 2, 7, 11–14, 29–33, 62](https://legimonaco.mc/code/code-taxes-chiffre-affaires); [Art. 15](https://legimonaco.mc/tai/convention/1963/05-18-tai1l000235/).

## Two worked examples that recompute

### Ordinary domestic standard-rated sale

Assume a correctly classified EUR 12,000 VAT-inclusive sale at 20%, and EUR 600 documented deductible input VAT in the same period. Net sales are EUR 10,000, output VAT EUR 2,000 and net payable EUR 1,400. No other transactions or carried credit exist.

```oa-check
name: Standard-rate VAT inclusive sale and allowed inputs
inputs:
  gross: 12000
  allowed_input: 600
steps:
  - net: gross / 1.2
  - output: gross - net
  - payable: output - allowed_input
expected:
  net: 10000
  output: 2000
  payable: 1400
```

### Foreign service with incomplete input recovery

Assume a taxable supplier established outside both Monaco and France supplies a EUR 2,000 general-rule B2B service that meets articles 11 and 62(2), has no special place rule and is standard-rated. Recipient VAT is EUR 400. A separately established deductible-use fraction of 50% gives EUR 200 input credit and EUR 200 net tax. The fraction is an assumed result of a separate deduction analysis, not a Monaco default.

```oa-check
name: Recipient VAT with a separately established deduction fraction
inputs:
  service: 2000
  deductible_fraction: 0.5
steps:
  - output: service * 0.2
  - input_credit: output * deductible_fraction
  - payable: output - input_credit
expected:
  output: 400
  input_credit: 200
  payable: 200
```

## Ask the client first

- What are the establishment, registration, franchise/option and assigned filing details?
- What are the transaction, tax point, goods route or service type, and customer status?
- What are prior/current-year national turnover and the relevant service subset?
- What invoice, taxable-use and deduction evidence supports each input?
- What prior credits, imports, foreign supplies, special schemes or cessation dates exist?

**Not yet confirmed:** live forms/portal, reduced-rate scope, special schemes, imports/intra-community reporting, mixed exemption and staged invoicing changes. This is a partial VAT working paper. Version 2.1 replaces the earlier unsourced Nice filing route and generic bank-pattern defaults.

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Code, arts. 11, 42, 51, 62, 66, 68, 70–71, 87–91, 110–112; annex A-139, A-144–A-145 | https://legimonaco.mc/code/code-taxes-chiffre-affaires | 2026-10-24 |
| France–Monaco convention, art. 15 | https://legimonaco.mc/tai/convention/1963/05-18-tai1l000235/ | 2026-10-24 |
