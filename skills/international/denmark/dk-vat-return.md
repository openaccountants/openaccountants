---
name: dk-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Danish VAT return (Momsangivelse) for a self-employed individual or small business in Denmark. Trigger on phrases like "prepare VAT return", "do the VAT", "Danish VAT", "moms", "momsangivelse", or any request involving Denmark VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Denmark only and only standard-registered businesses. Loensumsafgift-only entities, VAT groups, and fiscal representatives are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Danish VAT work.
jurisdiction: DK
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark VAT return (moms) — 2026 operational method

**Status:** **Source-cited draft** by the OpenAccountants team. It is not accountant-authored, accountant-verified or an attestation. Figures and procedures were retrieved from the Danish Tax Agency (Skattestyrelsen/SKAT) on 24 September 2026.

This method prepares an ordinary Danish VAT return for a registered business for **tax year 2026**. It covers domestic 25% sales, supported input VAT, ordinary EU/foreign purchase routing, imports, EU reporting records, filing, payment and correction. It does not decide exemptions, VAT groups, OSS/IOSS, margin schemes, property, capital-goods adjustments or a partial-deduction rate.

## Key figures and return routes

| Figure or route | Use | Official source |
| --- | --- | --- |
| DKK 50,000 per calendar year | Registration is required above this sales threshold; the small-business exemption also depends on the preceding calendar year. | [VAT registration](https://skat.dk/erhverv/moms/moms-saadan-goer-du/saadan-registrerer-du-din-virksomhed-for-moms) |
| 25% | General Danish VAT rate; use it for the domestic taxable-sale examples below. The EU-purchase route separately directs a registered purchaser to calculate Danish VAT. | [Get started on VAT](https://skat.dk/erhverv/moms/i-gang-med-moms) and [EU purchases](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-eu-countries/purchases-of-goods-and-services-in-the-eu) |
| Input VAT / output VAT | Reconcile totals from the business accounts; refund results only where input exceeds output. | [VAT accounts](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-do-your-business-vat-accounts) |
| Box A goods / A services; B goods / B services; C | International-trade value records: EU purchases, EU sales and exports respectively. | [VAT accounts](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-do-your-business-vat-accounts) |
| 4 pm filing-day cut-off | Select the official before/after 4 pm correction branch for the filing day; use the prior-period correction route for later changes. | [Correct a VAT return](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-change-your-vat-return-or-vat-payment) |

Amounts in the cases are hypothetical arithmetic, not authority figures. Prepare the return in DKK. Where an invoice is in another currency, retain the documented conversion basis and resolve the applicable official exchange-rate treatment before entering it; do not use a bank debit as the VAT base.

## Ask the client first

- CVR/VAT number, registration date, current assigned period and prior filed return/receipt.
- Sales and purchase ledgers, invoices and credit notes for the period; do not classify from a bank payee alone.
- Customer/supplier VAT number, country, goods movement or service facts, and invoice treatment for every international item.
- Customs/import records, business-use and invoice evidence for claimed input VAT.
- Whether a return has been filed, corrected, assessed or is a negative return still being processed.

## The method, step by step

1. **Confirm registration and period.** Register through Virk when taxable sales exceed DKK 50,000 per calendar year. Once registered, file every assigned period in TastSelv Erhverv, including a zero declaration where there were no relevant sales. Do not treat a zero declaration as a classification for zero-rated sales. [VAT registration](https://skat.dk/erhverv/moms/moms-saadan-goer-du/saadan-registrerer-du-din-virksomhed-for-moms)
2. **Build the evidence schedule.** Use invoice dates for the reporting period even when unpaid; prepayments without invoices are the stated exception and can trigger VAT on payment. [Period rule](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-do-your-business-vat-accounts)  Record invoice date, legal counterparty, VAT number, goods/services, origin/destination, VAT-exclusive base, VAT shown, rate/route, business purpose, customs evidence and document ID. Reconcile sales/purchases to the ledger before entering a return.
3. **Calculate domestic VAT.** For a confirmed ordinary domestic taxable sale, calculate `output VAT = VAT-exclusive sale × 25 ÷ 100`. Total output VAT and supported input VAT from the period accounts. Claim input VAT only where both business and seller are VAT registered and an invoice documents a resale or business-running purchase. Test private, mixed and exempt use separately. [Get started on VAT](https://skat.dk/erhverv/moms/i-gang-med-moms) and [VAT deductions](https://skat.dk/en-us/businesses/vat/vat-deductions/getting-your-vat-deductions)
4. **Route international purchases separately.** A registered business calculates Danish VAT on goods/services bought in other EU countries. Report the purchase value in **A goods** for EU goods or **A services** for EU services, and report goods VAT in **Moms af varekøb i udlandet** and services VAT in **Moms af ydelseskøb i udlandet med omvendt betalingspligt**; ordinary fully deductible input VAT can normally be deducted at the same time. The same source says an unregistered business has an EU-goods exception below DKK 80,000 annually but foreign services usually remain taxable regardless of amount. Do not use this method for the listed place-of-supply exclusions, such as foreign hotel/property, passenger transport, catering, events or short-term transport hire. [EU purchases](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-eu-countries/purchases-of-goods-and-services-in-the-eu)
5. **Handle imports and sales records.** For non-EU goods, confirm importer registration and obtain the customs declaration/import statement. Reconcile import VAT to the documented customs value plus customs duty, other import charges and transport/insurance to the known EU destination; avoid counting costs already included twice. Put import VAT in **Moms af varekøb i udlandet**, and only the deductible portion in **Købsmoms (indgående moms)**. Non-EU goods do not enter A goods. For qualifying non-EU business services, calculate Danish VAT under the supported place-of-supply route, put it in **Moms af ydelseskøb i udlandet med omvendt betalingspligt**, and separately test input deduction; non-EU services do not enter A services. Refer excluded services before calculation. [Non-EU purchases](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-non-eu-countries/buying-goods-and-services-in-countries-outside-the-eu) and [special VAT accounts/import base](https://info.skat.dk/data.aspx?oid=2068799). For EU sales without Danish VAT, keep verified buyer VAT number and dispatch/transport evidence; Use the **B goods** box marked for EU-salg uden moms for ordinary qualifying EU goods sales and **B services** for qualifying reverse-charge services; also report those sales by buyer VAT number in **EU-salg uden moms** and reconcile the totals across both submissions. A separate B goods box covers supplies excluded from that listing, such as specified installation sales; do not mix the two. **C** is for other qualifying supplies without Danish VAT, including exports and certain services, not every foreign invoice. Follow the separate EU-salg filing deadline shown for the relevant period. [Exact return fields and dual reporting](https://skat.dk/erhverv/moms/moms-ved-handel-med-udlandet/indberet-din-handel-med-udlandet). [VAT accounts](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-do-your-business-vat-accounts) and [EU documentation](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-eu-countries/documentation-requirements-for-eu-trade)
6. **Reconcile and file.** Tie output VAT to sales schedules, input VAT to invoice-level support, foreign-purchase VAT to the EU A schedules and separate non-EU import/service schedules, B/C to cross-border evidence and the net result to the VAT control account. For the ordinary scope here, calculate **net VAT = domestic output VAT + VAT on foreign goods purchases + reverse-charge VAT on foreign services − deductible input VAT**. Positive net VAT is payable; negative net VAT is a refund claim, subject to processing. Do not count foreign-purchase VAT twice as domestic output VAT. File in TastSelv Erhverv. The digital receipt states whether VAT is payable or refundable; the filing and payment deadline are the same. [Pay VAT](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-pay-vat)
7. **Correct the affected period.** Open the affected period in TastSelv Erhverv and follow the official correction branch for **before 4 pm on the day filed** or **after 4 pm**. Enter the corrected period amounts following that branch, then retain the acknowledgement and reconcile the changed liability. If TastSelv does not permit the correction, contact SKAT with the period, original amount, corrected amount and supporting records; do not place the difference in an unrelated period. Ordinary changes after three years require the stated exceptional conditions and an application; a forgotten deduction or wrong entry does not itself qualify. [Correction guidance](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-change-your-vat-return-or-vat-payment)

## Worked checks

| Case | Facts and arithmetic | Result |
| --- | --- | --- |
| Domestic sale | Hypothetical Danish taxable sale DKK 100,000 excluding VAT. [General rate](https://skat.dk/erhverv/moms/i-gang-med-moms) | Output VAT **DKK 25,000** (`100,000 × 25 ÷ 100`). |
| Supported business purchase | Hypothetical domestic business purchase has DKK 10,000 VAT, valid invoice and wholly taxable use. [Input VAT conditions](https://skat.dk/en-us/businesses/vat/vat-deductions/getting-your-vat-deductions) | Put **DKK 10,000** in input VAT; do not infer it from bank payment alone. |
| EU service purchase | Registered business buys a qualifying EU business service for DKK 20,000, 25%, wholly taxable use. [EU purchase route](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-eu-countries/purchases-of-goods-and-services-in-the-eu) | Record **A services DKK 20,000**, self-assess **DKK 5,000** VAT and test the same DKK 5,000 for input deduction. |
| EU goods sale | Seller has buyer VAT number and evidence goods left Denmark for another EU state. [EU documentation](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-eu-countries/documentation-requirements-for-eu-trade) | Record the supported value in **B goods**; do not substitute an unverified foreign customer. |
| Correction | Filed return omitted a DKK 10,000 domestic 25% sale. [General rate](https://skat.dk/erhverv/moms/i-gang-med-moms) and [correction route](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-change-your-vat-return-or-vat-payment) | Correct the affected period; omitted output VAT is **DKK 2,500** (`10,000 × 25 ÷ 100`). |

### Complete ordinary return example

Assume the domestic sale and supported input invoice above, the EU service purchase above, and a non-EU import whose customs statement confirms **DKK 2,500** import VAT. All purchases are used wholly for deductible taxable activity. [Accounts](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-do-your-business-vat-accounts), [EU purchases](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-eu-countries/purchases-of-goods-and-services-in-the-eu) and [non-EU reporting](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-non-eu-countries/buying-goods-and-services-in-countries-outside-the-eu) support the routes.

- Domestic output VAT: **DKK 25,000**.
- Foreign-goods VAT field: **DKK 2,500** import VAT; **A goods is zero** because this example has no EU goods purchases.
- Foreign-services VAT field: **DKK 5,000**; **A services DKK 20,000**.
- Input VAT: **DKK 17,500** = DKK 10,000 domestic + DKK 5,000 EU service + DKK 2,500 import. [Deduction conditions](https://skat.dk/en-us/businesses/vat/vat-deductions/getting-your-vat-deductions).
- Net payable: **DKK 15,000** = DKK 25,000 + DKK 2,500 + DKK 5,000 − DKK 17,500. No B/C sales occur in this example. [Foreign VAT added to payable and deductible input](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-non-eu-countries/buying-goods-and-services-in-countries-outside-the-eu).

Retain the return receipt, control-account reconciliation and invoice/customs schedule together. If an input deduction fails, change the input total; never delete the corresponding acquisition/import liability merely to make the return balance.

## When to refuse or refer

- Missing registration, invoice, customs, buyer-VAT-number or EU transport evidence; retain the records and identify the exact unresolved route.
- Exemption, place-of-supply uncertainty, partial deduction, VAT group, property, margin scheme, capital-goods adjustment, OSS/IOSS or non-established supplier position.
- A negative or authority-corrected return outside the self-service route.

Official sources: [SKAT VAT hub](https://skat.dk/en-us/businesses/vat), [Get started on VAT](https://skat.dk/erhverv/moms/i-gang-med-moms), [VAT registration](https://skat.dk/erhverv/moms/moms-saadan-goer-du/saadan-registrerer-du-din-virksomhed-for-moms), [EU purchases](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-eu-countries/purchases-of-goods-and-services-in-the-eu), [VAT deductions](https://skat.dk/en-us/businesses/vat/vat-deductions/getting-your-vat-deductions), [VAT accounts](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-do-your-business-vat-accounts), [EU documentation](https://skat.dk/en-us/businesses/vat/vat-on-international-trade/vat-on-sales-to-businesses/trading-with-eu-countries/documentation-requirements-for-eu-trade), [pay VAT](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-pay-vat), [correction guidance](https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-change-your-vat-return-or-vat-payment).

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
