---
name: saudi-arabia-vat
description: >
  Use this skill whenever asked to prepare, review, or classify transactions for
  a Saudi Arabia VAT return for any client. Trigger on phrases like "prepare VAT
  return", "Saudi VAT", "ZATCA return", "KSA VAT", "fill in VAT return",
  "Fatoorah", "e-invoicing Saudi", or any request involving Saudi Arabia VAT
  filing. Also trigger when classifying transactions for VAT purposes from bank
  statements, invoices, or other source data. Covers KSA only and only standard
  VAT-registered persons. The rate is 15%. VAT groups, margin schemes, partial
  exemption, oil and gas, customs suspension and special zone movements,
  residential property relief, capital asset adjustments and marketplace rules
  are refused. This Tier 2 draft supports source checking and reviewer
  questions; it does not authorise filing, payment or a tax position.
version: 2.2
jurisdiction: SA
tax_year: 2026
tax_year_notes: "VAT tax periods in calendar 2026, read at 5 November 2026. VAT has no year of assessment: each return covers a monthly or 3-month tax period under Implementing Regulations Art 58. Rate 15% in force since 1 July 2020."
last_updated: 2026-11-05
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: vat-gst
---

# Saudi Arabia VAT v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Persons registered, or who may have to register, for Value Added Tax in the Kingdom of Saudi Arabia (KSA), and the reviewers working with them. The tax is administered by the Zakat, Tax and Customs Authority (ZATCA, formerly GAZT). Currency is the Saudi riyal (SAR). The return is the ZATCA VAT return, filed through the e-services on the ZATCA website (https://zatca.gov.sa). This file covers KSA only and only standard VAT-registered persons.

Figures apply to VAT tax periods in calendar 2026, read at 5 November 2026. VAT has no year of assessment; each return covers a monthly or 3-month tax period under Implementing Regulations Art 58.

### What this file is

This is a country slot file for `vat-workflow-base`, which owns the workflow, output specification, question form and self-checks. This file supplies the Saudi content. Its status is Tier 2, pending review. It was contributed by the Open Accounting Skills Community. No statement here has been approved by an accountant.

The legacy file declared no `depends_on` field and this conversion adds none. It did require `vat-workflow-base`, and that requirement stands: do not attempt a VAT return without that base loaded.

**Operational hold.** `vat-workflow-base` Step 1 requires a regional or directive layer as well as this file. No Gulf Cooperation Council (GCC) layer was found in this repository at 5 November 2026, so Step 1 stops the workflow. Use this file as a reference only. Stop before producing a workbook, return or filing instruction until a regional layer or an approved non-EU exception exists. The return, workbook and classification sections below are kept ready for that point and for reviewer checking.

Every classification is a working paper for reviewer checking. Input tax credits need a document the law accepts (see 'Input tax'); treat all credits as provisional until it is checked.

### How to read the amounts

- **Law:** printed in the VAT Law, the Unified Agreement or the Implementing Regulations as read.
- **Administered:** what ZATCA says in a guideline, news page or portal screen. ZATCA's guidelines say they do not amend the law.
- **Announced:** reported by ZATCA as a decision whose own text was not read.
- **Held:** not proved. The reason is given and the item appears on the 'Not yet confirmed' line.

Where these differ, both are shown.

### Instruments read

The Arabic texts are the official ones. 2 texts were read only in English: the Unified Agreement, in a copy marked 'Unofficial Translation', and the E-Invoicing Regulation. The English edition of the Implementing Regulations on ZATCA's site is the Eighth Edition of 9 November 2021 and is out of date, so this file cites the Arabic Tenth Edition (Shawwal 1446H, April 2025) throughout.

- **VAT Law:** Royal Decree M/113 of 2 Dhu al-Qa'dah 1438H. Amended by Royal Decree M/52 of 28 Rabi II 1441H (Art 49) and Royal Order A/638 of 15 Shawwal 1441H (Art 2). In effect from 1 January 2018.
- **Unified Agreement:** Common VAT Agreement of the States of the GCC, signed 27 November 2016, ratified by Royal Decree M/51 of 3 Jumada I 1438H.
- **Implementing Regulations (IR):** Board Resolution 3839 of 14 Dhu al-Hijjah 1438H. Amended by Board Resolutions 2-4-17 (28 December 2017), 9-3-19 (3 July 2019), 7-2-20 (5 April 2020), 2-3-20 (9 June 2020), 1-5-20 (1 October 2020), 6-5-20 (28 October 2020), 6-2-21 (3 October 2021), 2-7-21 (9 November 2021), 05-09-22 (29 November 2022), 1-4-23 (15 June 2023) and 24-06-01, by circulation (17 Jumada I 1446H, 19 November 2024).
- **E-Invoicing Regulation:** dated 4 December 2020 on its cover. It says it is an integral part of the IR (Art 2(B)). Implementing Resolution of 19 May 2023.
- **Real Estate Transaction Tax (RETT) Law:** Royal Decree M/84 of 19 Rabi I 1446H, in effect 10 April 2025, per ZATCA. It replaced the regime under Royal Order A/84 of 14 Safar 1442H. RETT belongs to `sa-rett`.

No IR amendment after 19 November 2024 was found. ZATCA's guidelines of May 2026 still cite 24-06-01 as the latest, but this was not a complete search, so the point is held.

### Refusals and boundaries

These are the country refusals for `vat-workflow-base`. The legacy numbering is kept and R-SA-8 is added, because the legacy description promised a margin scheme refusal and the catalogue had none. If a trigger fires, stop, output the message verbatim and end, as Step 5 of the base requires. There is no partial classification.

- **R-SA-1, proportional deduction.** Trigger: the client makes both taxable and exempt supplies and bears input tax on goods or services used for both, or where the exempt supply cannot be separated (IR Art 51(3)). There is no 'trivial' or incidental exempt floor in Art 51; Art 51(11) deals with separate incidental cases and also needs the method. Message: 'You make both taxable and exempt supplies. Your input tax must be apportioned under Implementing Regulations Article 51 and Unified Agreement Article 46. This skill cannot compute the apportionment ratio for filing. Please engage a qualified tax consultant to determine and confirm the recovery rate before input tax is claimed.'
- **R-SA-2, VAT groups.** Trigger: client is part of a VAT group (IR Arts 10 to 12). Message: 'VAT group registrations require consolidation across all group members. This skill covers single-entity VAT returns only. Please engage a qualified tax consultant.'
- **R-SA-3, oil and gas.** Trigger: client operates in the oil and gas sector with specific VAT treatments for crude oil, refined products or hydrocarbons. Message: 'Oil and gas sector transactions are fact-sensitive and out of scope for this skill. Please engage a qualified tax consultant.'
- **R-SA-4, customs suspension and special zones.** Trigger: client operates under customs suspension or in a special zone and the transaction involves goods moving into, within or out of it (IR Art 32 bis, added by 24-06-01). Art 32 bis(5) sets 4 conditions for special zones and Art 32 bis(8) leaves water and energy outside the relief. Message: 'Customs suspension and special zone goods movements have specific treatment under Implementing Regulations Article 32 bis. Not every free zone qualifies. This skill applies standard rules only. Please engage a qualified tax consultant to confirm zone treatment.'
- **R-SA-5, capital asset adjustments.** Trigger: the period contains an adjustment to previously deducted input tax on a capital asset, because its use or the VAT status of that use changed or it was sold (IR Art 52). The adjustment period is 6 years for movable assets and 10 years for immovable assets permanently attached to land or property, from purchase, or the shorter accounting life, with part of a year counted as a full year. Art 52 as read has no value floor. Message: 'Capital asset adjustments under Implementing Regulations Article 52 require tracking the original deduction, current and intended use, and the annual fraction. Out of scope for this skill.'
- **R-SA-6, residential property and first home relief.** Trigger: client is selling real estate and claims zero-rating or a housing relief, or the sale involves a first home certificate. Message: 'A supply of real estate by transfer of ownership is exempt under Implementing Regulations Article 30(1)(a), not zero-rated, and Real Estate Transaction Tax applies separately. This skill does not determine first home eligibility or compute relief. Stop and refer this to a qualified tax consultant.'
- **R-SA-7, electronic marketplaces.** Trigger: client operates a platform through which electronic services of non-resident suppliers (IR Art 47(2)), or goods or services of resident suppliers not registered for VAT (IR Art 47(3)), are facilitated in KSA. Each paragraph has exception limbs and Art 47(4) excludes platforms that only process payments, market or redirect. ZATCA says the Art 47(3) amendments apply starting from January 2026. Message: 'Deemed supplier obligations for electronic marketplace operators require specific assessment. Out of scope.'
- **R-SA-8, margin scheme.** Trigger: client accounts, or wants to account, for used goods on the profit margin method (IR Art 48, which needs ZATCA's notice of approval). Message: 'The profit margin scheme for used goods is out of scope for this skill. Please engage a qualified tax consultant.'

### Required inputs

Slot 14 of `vat-workflow-base`.

**Minimum viable.** Bank statement for the period in CSV, PDF or pasted text, covering the full filing period, from any Saudi business bank: Al Rajhi Bank, Saudi National Bank (SNB/NCB), Riyad Bank, Saudi British Bank (SABB), Banque Saudi Fransi (BSF), Arab National Bank (ANB), Alinma Bank, Bank AlJazira, Bank Albilad or another.

**Recommended.** Sales invoices for the period, especially zero-rated exports and international services; purchase invoices for every input tax claim; the VAT number in writing (15 digits, first and last digit 3); Commercial Registration (CR) number.

**Ideal.** Complete e-invoice register, VAT registration certificate, prior period VAT return, and a reconciliation of any excess input tax.

**Policy if the minimum is missing.** HARD STOP with no bank statement. With a bank statement but no invoices, nothing that depends on a document can be entered: an input claim, a zero rate and a reverse charge line all stay Needs Input until the document is held. The legacy SAR 2,000 evidence floor is removed, because IR Art 49(7) sets no floor. The legacy 'proceed' on a bank statement alone does not survive the workflow base's rule on evidence conditions.

## Rates, bands and thresholds

Each row carries its official source. Status words are defined under 'How to read the amounts'. Articles are of the Arabic Tenth Edition of the IR unless stated.

| Item | Amount or rule | Position at 5 November 2026 | Source |
| --- | --- | --- | --- |
| Standard rate | 15% from 1 July 2020 (VAT Law Art 2(2), as amended by Royal Order A/638) | Law. Applies unless the supply is exempt or zero-rated (Art 2(2)). Agreement Art 25 prints 5%; Art 2(2) of the Law is the Saudi rate. | [VAT Law, official Arabic text](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%82%D9%8A%D9%85%D8%A9%20%D8%A7%D9%84%D9%85%D8%B6%D8%A7%D9%81%D8%A9%20(2).pdf) |
| Former rate | 5% from 1 January 2018 to 30 June 2020 | Law, read with IR Art 79(10). The rate applied is the rate at the date of supply or import (VAT Law Art 18). | [VAT Law, official Arabic text](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%82%D9%8A%D9%85%D8%A9%20%D8%A7%D9%84%D9%85%D8%B6%D8%A7%D9%81%D8%A9%20(2).pdf); [ZATCA About VAT page](https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/About-Vat.aspx) |
| Reduced rates | None. Supplies are standard-rated, zero-rated or exempt. | Law | [VAT Law, official Arabic text](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%82%D9%8A%D9%85%D8%A9%20%D8%A7%D9%84%D9%85%D8%B6%D8%A7%D9%81%D8%A9%20(2).pdf) |
| Zero rate | 0%: IR Arts 31 to 36 bis(2) | Law | [IR, official Arabic Tenth Edition](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Tax fraction at 15% | 15/115 of a tax-inclusive amount (Art 45(2): consideration x rate / (100% + rate)) | Law | same |
| Compulsory registration | Annual supplies exceeding SAR 375,000, or expected to (Agreement Art 50(1), (2)) | Law. The ministerial committee may amend after 3 years; ZATCA's filing guideline still uses SAR 375,000. Whether it was amended is held. | [Unified Agreement](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/GCC%20VAT%20Agreement.pdf) |
| Voluntary registration | 50% of the mandatory threshold (Agreement Art 51(3)): SAR 187,500, computed. Supplies or expenses not less than that amount, past or next 12 months (IR Art 7). | Law. The amount is derived, not printed in the IR. | [Unified Agreement](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/GCC%20VAT%20Agreement.pdf); [IR, official Arabic Tenth Edition](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Non-resident supplier | Must register regardless of turnover if obliged to pay tax in KSA (Agreement Art 50(3)), within 30 days of the first supply (IR Art 5) | Law | [Unified Agreement](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/GCC%20VAT%20Agreement.pdf); [IR, official Arabic Tenth Edition](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Monthly tax period | Annual taxable supplies exceeding SAR 40,000,000 in the previous 12 months (Art 58(1)) | Law | [IR, official Arabic Tenth Edition](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| 3-month tax period | Everyone else (Art 58(2)), who may apply for monthly (Art 58(3)) | Law | same |
| Return and payment deadline | Last day of the month following the tax period (Arts 59(1), 62(1)) | Law | same |
| Correction within a return | Net understatement less than SAR 15,000 (Art 63(3), as amended by 24-06-01) | Law. The legacy SAR 5,000 is the former figure. | same |
| Records | 6 years from the end of the tax period; capital assets, the adjustment period plus 5 years from acquisition (Art 66(1)), which ZATCA gives as 11 years for movable and 15 for immovable capital assets (Imports and Exports Guideline s 11.3) | Law. Agreement Art 59 says not less than 5 years, and 15 for real estate: held for real estate that is not a capital asset. | same |
| Simplified tax invoice | Business customer, supply under SAR 1,000 (Art 53(1)(c)) | Law | same |
| Cash basis | Past and current year supplies not over SAR 5,000,000, and no VAT violation notice in the last 12 months (Art 46) | Law | same |
| Refund by a person eligible under Art 70 | Claim not less than SAR 5,000 (Art 70(11), as amended by 24-06-01) | Law | same |
| Bad debt, legal action | Debt over SAR 100,000 needs evidence of formal legal action (Art 40(7)) | Law | same |
| Late registration fine | SAR 10,000 (VAT Law Art 41) | Law | [VAT Law, official Arabic text](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%82%D9%8A%D9%85%D8%A9%20%D8%A7%D9%84%D9%85%D8%B6%D8%A7%D9%81%D8%A9%20(2).pdf) |
| Incorrect return | 50% of the difference (Art 42(1)) | Law. ZATCA's May 2026 guideline states 25%, adjustable up to 50% or down to 0%. ZATCA's Penalties page, updated 30 August 2026, still prints 50%. Both are shown; see 'Penalties and interest'. | same |
| Late filing | 5% to 25% of the tax that should have been declared (Art 42(3)) | Law | same |
| Late payment | 5% of the unpaid tax for each month or part of a month (Art 43) | Law | same |
| Fine waiver initiative | Runs 1 July to 31 December 2026 | Announced. Minister's decision not read. | [ZATCA simplified guide, as of 1 July 2026](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf) |
| E-invoicing Wave 24 | Revenue subject to VAT above SAR 375,000 during 2022, 2023 or 2024; integrate by 30 June 2026 | Administered | [ZATCA news, Wave 24](https://zatca.gov.sa/en/Pages/news-1426.aspx) |
| E-invoicing Wave 25 | Revenue subject to VAT above SAR 187,500 during 2022, 2023, 2024 or 2025; ZATCA notifies; integrate by no later than 1 February 2027 | Administered | [ZATCA news, Wave 25](https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx) |

## The base

### What is charged

VAT applies to supplies of goods and services by a taxable person in the course of an economic activity, and to imports, unless exempt or zero-rated. The value of a supply excludes the VAT; a tax-inclusive amount is split with the tax fraction.

**Date of supply.** Tax falls due on the earliest of supply, tax invoice, or partial or full receipt of the consideration, to the extent received (Agreement Art 23(1)). So a deposit or part payment is taxed when received, to that extent. ZATCA's filing guide lists undeclared advance payments as a common error. IR Art 20 has special cases: government contracts (the earlier of the payment order and receipt, Art 20(5)), continuous supplies (with a 12-month backstop), oil, gas, water and electricity (Art 20(4)), and deemed supplies on ceasing activity (Art 20(6)). No rule was read for agreements subject to a suspensive condition; refer one to the reviewer.

**Transitional supplies at the rate change (IR Art 79(10)).** All of this relief ended by 30 June 2021 at the latest. It matters now only for corrections to old periods.

- (a) A supply after 1 July 2020 is taxed by its date of supply, whatever the invoice or payment date, except supplies invoiced before 11 May 2020, up to the invoiced value, actually supplied before the end of 30 June 2021. An extra invoice covers the difference.
- (b) Continuous supplies take the new rate on the part after 1 July 2020, with the same exception. The supplier may apply the new rate to the whole with the customer's approval.
- (c) Contract made before 11 May 2020, both parties registered, customer entitled to full input deduction: the supplier may apply the old rate until expiry, renewal or 30 June 2021, whichever is earliest.
- (d) Contract signed with or awarded by a government body before 11 May 2020: the supplier may apply the old rate, with the same end dates.

**Out of scope.** Not reported on the return, on these conditions only:

- Transfer of an economic activity, wholly or in part, is outside tax only if all 4 limbs of IR Art 17(1) are met: (a) the transferred part can run independently and all tangible and intangible assets needed are included; (b) the recipient is, or by the transfer becomes, a taxable person and uses the assets directly in the same activity; (c) supplier and recipient agree in writing that it is a transfer of an economic activity; (d) both notify ZATCA by the end of the month after the transfer. Otherwise the goods and services transferred are a taxable supply (Art 17(6)), and IR Art 47(5) can also make both jointly liable where the transferor stops entirely and ZATCA was not notified.
- A government body's activity as a public authority is outside economic activity only if all 3 limbs of IR Art 9(5) are met: (a) a statutory instrument authorises it; (b) it is not carried on by economic or commercial criteria; (c) it is exclusive, with no competition from the private sector.
- Work by employees and others in an employment relationship is not an economic activity (IR Art 9(6)). Art 9(7) deals with seconded labour.

Salaries, GOSI contributions, zakat, fines, dividends and loan principal are legacy exclusion patterns; see Slot 7 under 'Supplier discovery library'.

### Exempt supplies

- **Financial services (IR Art 29).** Exempt, except where consideration is paid explicitly as a fee, commission or commercial discount (Art 29(1)). So interest and implicit margin are exempt; an explicit bank fee, card fee or payment processor fee is not exempt. The services are in Art 29(2) (issue or transfer of money, credit, accounts, derivatives), Art 29(3) (Islamic finance), Art 29(5) (a non-exhaustive list) and Art 29(6) (securities).
- **Life insurance (Art 29(7), (8)).** Life insurance and life reinsurance are exempt, including explicit fees (from Board Resolution 1-4-23). A life contract is conventional, takaful or other Islamic cover from a KSA-licensed provider that pays on death or a life event, or a similar contract from a non-resident. Other insurance is not within the exemption.
- **Real estate (Art 30(1)).** 'Subject to any other provision of these Regulations': (a) a supply of real estate of any kind, residential, commercial, agricultural, developed or undeveloped land, by transfer of ownership or disposal as owner; (b) a residential lease or licence. Hotels, inns, guest houses, rest houses, serviced shelter and temporary accommodation are not residential (Art 30(2) to (4)). A commercial lease is outside the exemption. Art 31(2) makes a zero rate prevail over an exemption.

Report exempt sales in Box 5. There is no input deduction on costs tied exclusively and directly to an exempt supply (IR Art 51(2)).

The legacy zero rate for a first residential property up to SAR 1,000,000 was not found in the IR and is removed. ZATCA's RETT guideline, Version 6 of May 2026, says the State bears RETT, not VAT, on up to SAR 1,000,000 of a citizen's first home, and that it bore VAT on up to SAR 850,000 before Royal Order A/84. See `sa-rett` and R-SA-6. `sa-rett` still cites only A/84 and is due its own review.

### Zero-rated supplies

- **Exports of goods (IR Art 32).** Evidence within 90 days of 3 kinds: export documents from customs or a similar administration; commercial documents showing the customer and place of delivery; transport documents (Art 32(3)). Art 32(7) was deleted by 24-06-01.
- **Services to non-residents (Art 33).** Services by a taxable person to a customer not resident in any Member State (Art 33(1)). Not zero-rated where any of these applies (Art 33(2)): (a) the place of supply is in a Member State under the special cases in Agreement Arts 17 to 21, which does not catch a service supplied separately from such a service, even if connected with it directly or indirectly; (b) the customer is resident in a Member State; (c) the customer or a related person benefits directly whilst present in a Member State, and that related person cannot fully recover input tax on the services; (d) the service is physically performed on tangible goods in a Member State during the supply. Limb (a) tests the special cases only. A customer registered for VAT only outside the GCC is not a taxable customer, so the general rule places the service where the supplier resides (Agreement Art 15; Imports and Exports Guideline s 8.1), and that alone does not defeat the zero rate. ZATCA reads limb (c) narrowly, and applies it where a customer's employees or representatives temporarily here benefit (s 8.2). The legacy test of 'no KSA establishment' was too narrow. Art 33(3) covers tourist refund providers.
- **International transport (Art 34).** Art 34 asks for neither a certificate nor the 75% test on: international transport of goods and of passengers (Art 34(1), (2)), meaning transport by vehicle, aircraft or ship with driver, pilot or crew, to or from the Kingdom (Art 34(7)); services directly or incidentally connected with international passenger transport, such as baggage, seat booking and cabin charges (Art 34(3)); and the Art 25(2) services that support zero-rated international transport (Art 34(5)(a)). 3 reliefs turn on a qualifying means of transport, so the 75% test reaches them through its definition: supply of the means, with the customer's certificate to ZATCA or the supplier, checked by the customer first and kept by the supplier (Art 34(4), (9)); Art 25(2) services connected with it at an airport or port, where Art 34 names no certificate (Art 34(5)(b)); and its maintenance, repair or modification with parts, where the supplier holds a customer certificate and the purpose is to keep it operating as a qualifying means; maintenance and repair must also be physically performed on it (Art 34(6)). A qualifying means has international transport as its main purpose: a vehicle built for at least 10 persons or for goods commercially, or a ship or aircraft built for passengers or goods commercially, not converted or used for recreational or personal purposes (Art 34(8)). Main purpose means at least 75%, the average of 4 ratios (trips, distance, revenue, operating cost), which the operator proves on 12 months' actual data, or 6 months' planned data for a new means (Art 34(10)).
- **Medicines and medical goods (Art 35).** As classified by the Ministry of Health or competent authority, subject to the GCC Health Ministers' controls. The legacy 'SFDA list' was not in the text read and is held.
- **Qualifying metals (Art 36).** First supply of gold, silver or platinum by a producer or refiner; purity at least 99% and tradeable on the global bullion market. Art 36(2) covers certain rights in such metal.
- **Military (Art 36 bis).** Locally manufactured qualifying military goods supplied to the armed forces or government internal security forces, by a registered taxable person licensed in military manufacturing by the General Authority for Military Industries and holding its qualifying supply certificate. The zero rate applies only if every condition is met at the date tax falls due, and only up to the consideration for the qualifying goods.
- **Diplomatic missions (Art 36 bis(2)).** Supplied by qualified suppliers under a decision of the Governor, subject to Art 70(2).

### Input tax

**Right to deduct.** Tax on goods and services supplied in the course of the economic activity is deductible to the extent they are used for taxable supplies, zero-rated included, Intra-GCC supplies, or supplies that would be taxable had they been made in KSA (IR Art 49(1)). VAT wrongly charged, or charged by an unregistered supplier, is not deductible (ZATCA Input Tax Guideline). Pre-registration tax is deductible on services within 6 months before registration and on goods, on the conditions of Art 49(2) to (4), none of which reach Art 50 items. The claim must be made not later than 5 calendar years after the calendar year of supply (Art 49(8)).

**Documents.** The usual documents are a tax invoice and, for imports, customs documents (Agreement Art 48). Without those, IR Art 49(7) accepts (a) a correctly issued simplified tax invoice; (b) for a transfer of goods to another Member State, the commercial or other document proving the value; (c) other commercial documents ZATCA allows at its discretion, proving the person was correctly charged and paid the VAT. A reverse charge line rests on the supplier's invoice, kept to support the calculation (Imports and Exports Guideline s 6.3), or other commercial documents proving the service and consideration, with the tax calculation (Input Tax Guideline s 8). Whether an invoice that breaks the e-invoicing rules still supports a deduction was not proved, so the legacy line that it 'is still a valid invoice' is held.

**Restricted input (IR Art 50, as amended by 24-06-01).** Treated as outside economic activity and not deductible, unless resupplied as a taxable supply (Art 50(1), (4)):

- (a) any entertainment, sporting or cultural service, or attending an entertainment event;
- (b) hospitality and food and drink catering, unless a law in force in KSA obliges the person to provide it to employees at the workplace;
- (c) insurance or healthcare for employees and dependants, unless a law in force in KSA obliges the person to provide it;
- (d) purchase or lease of restricted vehicles;
- (e) insurance, repair, alteration, maintenance or similar services on them;
- (f) fuel used in them;
- (g) goods or services for personal use or any purpose other than the activity.

The legacy block on employee housing and childcare has no limb of its own in Art 50(1) and is held: limb (g) or a statutory duty may decide it, and the Employee Benefits Guideline was not obtained. ZATCA says these apply even where there is a business purpose, as with a client dinner or match tickets. Where only part of a cover is statutory, only that part is deductible (Input Tax Guideline, Example 16).

A restricted vehicle is one designed to carry no more than 10 persons (Art 50(2)), except: (a) trucks, cranes and similar heavy equipment used exclusively for the economic activity and not available for private use; (b) vehicles bought or leased for taxable resupply by sale, lease or similar; (c) registered emergency vehicles, such as ambulance, fire, security and guard vehicles; (d) vehicles used exclusively for the economic activity and not available for private use. Any availability for private use defeats (a) and (d), there is no apportionment, and ZATCA may look behind a contract. Legacy cites to IR Art 49(3), (4) and (5) and the 'essential to the business' test were wrong and are replaced.

Goods prohibited for sale in KSA carry no deduction (Agreement Art 45(2)).

**Proportional deduction (IR Art 51).** The default fraction is taxable supplies over taxable plus exempt supplies of the past calendar year (Art 51(4)), excluding capital asset supplies and supplies outside KSA by an establishment there (Art 51(5)). A person not registered last year uses estimates (Art 51(6)). There is an annual true-up in the final return of the year (Art 51(7)). Other methods need ZATCA's approval (Art 51(8) to (10)). This is shown for reference only: R-SA-1 stops the workflow.

**Adjustments (IR Art 40).** Credit and debit notes must be issued by the 15th of the month after the event (Art 54(6)). Enter them through the adjustments column of the box that holds the original supply. ZATCA warns against using that column to cut tax without a document.

Bad debt relief (Art 40(7)) needs all of: the tax was previously declared and paid; the debtor is not related; at least 12 months since supply; a licensed accountant's certificate, or other evidence if no auditor is required; and evidence of formal legal action for debts over SAR 100,000. It is not available on the cash basis (Art 40(8)). Later receipts are taxed again (Art 40(9)). A customer who has not paid after 12 months from the month after the supply adjusts the input tax, except goods under a finance contract on the stated conditions (Art 40(10)).

### Tax invoices

A tax invoice is required for supplies to a taxable person, a non-taxable legal person, a sole establishment or any entity established in KSA; for prepayments; for Intra-GCC supplies and exports; and for zero-rated services to a non-GCC customer. It is due by the 15th of the month after supply (IR Art 53(1)). Under SAR 1,000 a simplified tax invoice is allowed (Art 53(1)(c)). Contents: Art 53(5). Otherwise a simplified tax invoice is issued at the earlier of supply or receipt (Art 53(7)), with a financial services exception (Art 53(7)(c)); contents: Art 53(8).

### E-invoicing (FATOORA)

`saudi-einvoice` owns the detail. In outline, all administered unless stated:

- **Phase 1, generation.** In force since 4 December 2021 for resident taxable persons, and for a customer or third party issuing for one. Non-residents are not required to comply (E-Invoicing Regulation Art 3). Invoices are generated in XML or PDF/A-3 with embedded XML. A QR code is mandatory on simplified invoices and their notes.
- **Phase 2, integration.** Rolling waves from 1 January 2023, notified at least 6 months ahead. Tax invoices are cleared by ZATCA's platform; simplified invoices are reported. A QR code is mandatory on all types, and each document carries a UUID. Waves 24 and 25 are in the rates table. ZATCA may suspend the requirement under IR Art 53(10).
- **Who is in a wave.** ZATCA notifies. Do not infer a wave from revenue alone.
- **Penalties.** The regulation applies the VAT Law's penalties (Art 4(A)(1); Resolution of 19 May 2023, clause Eighth(2)). The amounts sit in a ZATCA classification not read: held.

Legacy claims that all invoices must be electronic and that handwritten invoices are prohibited are narrowed to the resident scope above.

Codes (XML Implementation Standard, v1.2, and Resolution annexes):

- **VAT number.** 15 digits, first and last digit 3 (the XML standard's business rule on BT-31).
- **Invoice type.** 388 tax invoice, 386 prepayment invoice, 383 debit note, 381 credit note. Subtype 01 standard, 02 simplified.
- **Tax category.** S standard, Z zero-rated, E exempt, O not subject to VAT.
- **Payment means.** The standard requires a value from a subset of UNTDID 4461. The legacy list (10 cash, 30 credit, 42 bank account, 48 bank card) was not found in that form in what was read: held.
- **QR fields.** 1 seller's name, 2 seller's VAT number, 3 time stamp, 4 total with VAT, 5 VAT total. Phase 2 adds 6 hash of the XML, 7 ECDSA signature of the hash, 8 ECDSA public key, and 9, for simplified documents, the ECDSA signature of the cryptographic stamp issued by ZATCA's technical CA.

### Conservative defaults

Slot 10. These apply the Tier 2 rule and the permitted factual defaults rule in `vat-workflow-base`. A default stands only where the law read fixes the result of the missing fact. Unknown rates, legal scope, counterparty jurisdiction or evidence conditions are otherwise Needs Input. Every legacy default that picked a rate or a location is withdrawn.

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Needs Input |
| Unknown VAT status of a purchase | Needs Input. No deduction is entered until a document IR Art 49(7) accepts supports the amount. |
| Unknown counterparty location | Needs Input |
| Unknown business use, vehicle, phone, restricted category | No deduction is entered until the Art 50 facts are established; disclose the amount at stake |
| Unknown SaaS billing entity | Needs Input |
| Unknown whether a transaction is in scope | Needs Input |
| Unknown GCC state treatment | Needs Input. There is no GCC field on the return; apply IR Art 79(6), (7) once the country is known. |
| Export shown, evidence missing | No zero rate. 15% only where the sale is verified as a taxable supply in KSA and not exempt; disclose the missing evidence, the zero-rated alternative and the tax at stake. Otherwise Needs Input. |
| Unknown whether a sale is zero-rated or exempt | Needs Input |

### Red flag thresholds

Slot 13. Working review settings for the reviewer brief, not legal amounts.

| Flag | Value |
| --- | --- |
| HIGH single transaction | SAR 20,000 |
| HIGH tax delta on a single default | SAR 2,000 |
| MEDIUM counterparty concentration | More than 40% of output or input |
| MEDIUM conservative default count | More than 4 across the return |
| LOW absolute net VAT position | SAR 50,000 |
| Tier 2 question threshold | SAR 0: no row is filtered on amount, as no Saudi floor was set |

### VAT return boxes

Slot 3. The legacy 20-field table did not match ZATCA's form and is replaced. The form below was viewed in ZATCA's e-services manual and Simplified VAT Filing Guidelines. It has 3 columns: Amount, Adjustments, VAT amount. Amounts exclude VAT.

| Box | Label on the form | Use |
| --- | --- | --- |
| 1 | Standard Rated Sales (15%) | Domestic sales at 15% |
| 2 | Sales on which the government bears the VAT | ZATCA's example is private education and healthcare to citizens. The instrument was not read; the XML standard codes them VATEX-SA-EDU and VATEX-SA-HEA. Needs Input before use. |
| 3 | Zero Rated Domestic Sales | Medicines, medical equipment, qualifying investment metals. Other zero-rated domestic supplies, reviewer to confirm. |
| 4 | Exports | Exports of goods and services to non-residents. What was read does not say which box takes a seller's international transport under Art 34: Needs Input. |
| 5 | Exempt Sales | Financial services, real estate sales, residential rent |
| 6 | Total Sales | Computed |
| 7 | Standard Rated Domestic Purchases | Only purchases with a deductible amount proved by a document |
| 8 | Imports subject to VAT paid on import | Value and VAT from the customs declaration |
| 9 | Imports subject to VAT accounted for through the reverse charge mechanism | Services from non-residents, and goods under IR Art 44. The form treats the tax as deductible; a non-deductible part goes in the adjustments column. |
| 10 | Zero Rated Purchases | International flights bought, on reading Art 34 with the label; no source read names them, so a reviewer confirms |
| 11 | Exempt Purchases | Exempt purchases from KSA suppliers. Exempt imports (Imports and Exports Guideline s 5.1) and exempt services from non-residents (s 6.3) are not reported. |
| 12 | Total Purchases | Computed |

The next screen, 'Total VAT', shows Total VAT due for current period, VAT Credit from previous period(s), Corrections from previous periods and Net VAT. Rows on that screen are named, not numbered, on the form viewed. The low-resolution screen in ZATCA's manual appears to show a SAR 5,000 limit; IR Art 63(3) and the Simplified VAT Filing Guidelines say SAR 15,000. The IR prevails over an older screen; test the live portal before relying on it.

Restricted purchases, purchases without a document, purchases from outside KSA except imports meeting the conditions, and purchases of a later period do not go in Box 7. The Simplified VAT Filing Guidelines say so.

A purchase may be added from an earlier period if it has not been deducted before and it meets IR Arts 49 and 53.

### Supplier discovery library

Slot 6. Match by case-insensitive substring on the counterparty name; if several match, use the most specific. A match is a discovery aid, not a classification: the legacy instruction 'do not second-guess' is removed. Before a row is entered, confirm the billing entity and hold a document IR Art 49(7) accepts. The billing entities are legacy notes, not verified. 'Box 7' below means Box 7 with VAT split at 15/115, once the invoice shows VAT and no Art 50 limb applies. Otherwise the row is Needs Input.

**Saudi banks and finance**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AL RAJHI, ALRAJHI, مصرف الراجحي | Tier 2 | Interest or margin exempt. Explicit fees are not exempt (Art 29(1)): Box 7 if VAT is shown on a document; otherwise Needs Input. |
| SNB, SAUDI NATIONAL BANK, NCB, البنك الأهلي | Tier 2 | Same |
| RIYAD BANK, بنك الرياض | Tier 2 | Same |
| SABB, SAUDI BRITISH BANK | Tier 2 | Same |
| BSF, BANQUE SAUDI FRANSI | Tier 2 | Same |
| ANB, ARAB NATIONAL BANK | Tier 2 | Same |
| ALINMA, مصرف الإنماء | Tier 2 | Same |
| BANK ALJAZIRA, بنك الجزيرة | Tier 2 | Same |
| BANK ALBILAD, بنك البلاد | Tier 2 | Same |
| REVOLUT, WISE (fee lines) | Tier 2 | Explicit fees are not exempt. Check for VAT, the billing entity and separate taxable subscription invoices: non-resident means possible reverse charge. |
| INTEREST, PROFIT, MURABAHA (margin) | Exempt | Box 11 on purchases, Box 5 on income, once confirmed as margin and not a fee |
| LOAN, TAMWEEL, FINANCING (principal) | Exclude | Principal, not consideration for a supply |

**Payment processors**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees) | Tier 2 | Explicit fee, not exempt. Non-resident: Box 9. KSA entity with VAT: Box 7. |
| PAYPAL (transaction fees) | Tier 2 | Same |
| MADA, MADA PAYMENT | Tier 2 | Explicit fee, not exempt. Check the acquirer's document. |
| HYPERPAY, MOYASAR, PAYFORT | Tier 2 | KSA entity: Box 7. Otherwise possible Box 9. |

**Government, regulators and statutory bodies**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ZATCA, GAZT, هيئة الزكاة والضريبة والجمارك | Exclude | Tax or zakat payment, not a supply |
| VAT PAYMENT, ضريبة القيمة المضافة | Exclude | VAT payment |
| ZAKAT PAYMENT, زكاة | Exclude | Zakat, separate from VAT |
| CUSTOMS, جمارك | Exclude the duty | Check for import VAT, Box 8 |
| GOSI, GENERAL ORGANIZATION FOR SOCIAL INSURANCE, التأمينات الاجتماعية | Exclude | Social insurance, statutory |
| MOC, MINISTRY OF COMMERCE, وزارة التجارة | Tier 2 | Exclude only where Art 9(5)(a) to (c) are verified. Limb (c), exclusivity, is the one usually unverified from a bank line. If the document shows VAT, follow the document. |
| MOL, MINISTRY OF LABOR, HRSD | Tier 2 | Same |
| MUNICIPALITY, BALADIYA, أمانة | Tier 2 | Same |
| CITC, COMMUNICATIONS AND IT COMMISSION | Tier 2 | Same |
| CMA, CAPITAL MARKET AUTHORITY | Tier 2 | Same |
| ABSHER, MUQEEM, QIWA, MUDAD | Tier 2 | Same. Some are platforms, not the charging body. |
| SADAD | Look through | Payment channel. Classify on the biller after the prefix. |

**Utilities and telecoms**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SEC, SAUDI ELECTRICITY COMPANY, الشركة السعودية للكهرباء | Box 7 | Business premises only |
| SWCC, SALINE WATER CONVERSION, المؤسسة العامة لتحلية المياه المالحة | Box 7 | Same |
| NATIONAL WATER COMPANY, NWC, شركة المياه الوطنية | Box 7 | Same |
| MARAFIQ | Box 7 | Jubail and Yanbu utilities |
| STC, SAUDI TELECOM, الاتصالات السعودية | Box 7 | Business line; mixed use is Tier 2 |
| MOBILY, ETIHAD ETISALAT, اتحاد اتصالات | Box 7 | Same |
| ZAIN, زين | Box 7 | Same |
| VIRGIN MOBILE KSA | Box 7 | Same |

**Insurance**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TAWUNIYA, التعاونية | Tier 2 | Life, including life takaful: exempt (Art 29(7), (8)). Motor or health: Art 50 applies first. |
| BUPA ARABIA | Tier 2 | Health cover for staff: deductible only to the extent of a statutory duty (Art 50(1)(c)) |
| MEDGULF | Tier 2 | As Tawuniya |
| MALATH, WALAA, AL RAJHI TAKAFUL | Tier 2 | Same |
| MOTOR INSURANCE, VEHICLE INSURANCE | Tier 2 | No deduction on a restricted vehicle (Art 50(1)(e)) |
| HEALTH INSURANCE, MEDICAL INSURANCE | Tier 2 | As Bupa |

Life is exempt by Art 29(7), (8), life takaful included. No provision was read that rates general insurance or general takaful beyond their being outside that exemption: follow the invoice.

**Transport, fuel and travel**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UBER SA, CAREEM KSA | Box 7 | Ride-hailing; business purpose to be shown |
| SAUDIA, SAUDI ARABIAN AIRLINES, الخطوط السعودية (international) | Box 10 | Zero-rated purchase under Art 34, not an export |
| SAUDIA (domestic) | Box 7 | Check the invoice |
| FLYNAS, طيران ناس (international) | Box 10 | Same as Saudia international |
| FLYNAS (domestic) | Box 7 | Check the invoice |
| SAR, SAUDI RAILWAY, سار | Box 7 | Check the invoice |
| DHL KSA, ARAMEX KSA | Box 7 | International carriage may be zero-rated under Art 34 |
| PETROL, FUEL, ALDREES, SASCO, NAFT, محطة وقود | Tier 2 | No deduction for a restricted vehicle (Art 50(1)(f)) |
| HOTEL, FUNDUQ, فندق, MARRIOTT, HILTON | Tier 2 | Hotels are not residential (Art 30), so the supply is taxable. Whether a stay is 'hospitality' under Art 50(1)(b) was not settled by what was read: Needs Input. |

**Food retail and restaurants**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PANDA, بنده | Tier 2 | No deduction until shown to be stock or a business use. Personal: Art 50(1)(g). |
| CARREFOUR KSA, كارفور | Tier 2 | Same |
| DANUBE, الدانوب | Tier 2 | Same |
| TAMIMI MARKETS, التميمي | Tier 2 | Same |
| OTHAIM, العثيم | Tier 2 | Same |
| BIN DAWOOD, بن داود | Tier 2 | Same |
| RESTAURANTS, CAFES (any named restaurant) | Blocked | Art 50(1)(b), unless a statutory duty to feed staff at the workplace is shown |

**SaaS and non-resident suppliers (reverse charge)**

Report the service in Box 9 where all of these hold: the supplier is non-resident; the place of supply is in KSA; the client is a taxable customer; and the supplier charged no KSA VAT. A KSA VAT number and VAT on the invoice means Box 7. An exempt service is not reported.

| Pattern | Billing entity (legacy note) | Box |
| --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) or Google LLC (US) | 9 |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 9 |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 9 |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 9 |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 9 |
| AWS, AMAZON WEB SERVICES | AWS Inc (US) or AWS EMEA SARL (LU) | 9 |
| NOTION | Notion Labs Inc (US) | 9 |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 9 |
| OPENAI, CHATGPT | OpenAI Inc (US) | 9 |
| GITHUB | GitHub Inc (US) | 9 |
| FIGMA | Figma Inc (US) | 9 |
| CANVA | Canva Pty Ltd (AU) | 9 |
| SLACK | Slack Technologies LLC (US) | 9 |
| ATLASSIAN (Jira, Confluence) | Atlassian Pty Ltd (AU) | 9 |
| ZOOM | Zoom Video Communications Inc (US) | 9 |
| HUBSPOT | HubSpot Inc (US) | 9 |
| STRIPE (subscription) | Stripe Inc (US) | 9 |
| SHOPIFY | Shopify Inc (CA) | 9 |
| TWILIO | Twilio Inc (US) | 9 |
| APPLE, APPLE.COM/BILL, ITUNES | Check the invoice | 9 or 7 |
| DROPBOX | Check the invoice | 9 or 7 |

**Retail, office and professional**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| JARIR, مكتبة جرير | Box 7 | Business purpose to be shown |
| EXTRA, اكسترا | Box 7 | Same |
| IKEA KSA | Box 7 | Same |
| SACO, ساكو | Box 7 | Same |
| LAW FIRM names, محاماة, LEGAL | Box 7 | Same |
| ACCOUNTANT, AUDIT FIRM, محاسبة | Box 7 | Same. The legacy 'always claimable' is removed. |
| DELOITTE KSA, PwC KSA, KPMG KSA, EY KSA | Box 7 | Same |
| PRO SERVICES, TASHEEL, MUQEEM SERVICES | Box 7 | Same. Government fees passed through need separating. |
| COWORKING, REGUS, WEWORK, مساحة عمل | Box 7 | Commercial licence to occupy, outside Art 30(1)(b) |

**Property and rent**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| COMMERCIAL RENT, OFFICE RENT (with VAT invoice) | Box 7 | Commercial lease |
| RESIDENTIAL RENT, APARTMENT RENT, إيجار سكني | Exempt | Box 11 if it is a business cost; Art 30(1)(b) |
| EJAR, إيجار (residential) | Tier 2 | Residential tenancy platform; confirm the property type |
| WAREHOUSE, INDUSTRIAL RENT | Box 7 | Commercial lease |
| WAFI (residential off-plan sales platform) | R-SA-6 | May involve real estate sale and first home relief |

**Slot 7: exclusion patterns**

Excluded from the return. Salaries and employment rest on IR Art 9(6); tax payments and statutory contributions are named in the workflow base's slot. No provision specific to dividends, owner drawings or end of service awards was read; they are kept as patterns for the reviewer, on the footing that none is consideration for a supply.

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES, PAYROLL, WPS, رواتب | Exclude | Employment |
| GOSI, SOCIAL INSURANCE | Exclude | Social insurance contributions |
| IQAMA RENEWAL, VISA FEES | Tier 2 | Government fee; Art 9(5) limbs apply |
| END OF SERVICE, مكافأة نهاية الخدمة | Exclude | Employment termination benefit |
| OWN TRANSFER, INTERNAL, BETWEEN ACCOUNTS, حوالة داخلية | Exclude | Internal movement |
| DIVIDEND, توزيعات | Exclude | Dividend |
| LOAN REPAYMENT, FINANCING REPAYMENT | Exclude the principal | Finance charges are separate |
| PARTNER DRAWING, OWNER DRAWING | Exclude | Drawing |
| CASH WITHDRAWAL, ATM, سحب نقدي | Tier 2 | Ask what the cash was spent on |

### Bank exports and language cues

Slot 15. Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these. Formats are legacy notes, not tested against real exports.

- **Al Rajhi Bank.** CSV or Excel with DD/MM/YYYY (Gregorian) dates; some statements also show Hijri dates. Columns: Transaction Date, Description, Debit, Credit, Balance. The description carries the counterparty, sometimes in Arabic. SADAD bill payments show the biller ('SADAD-STC', 'SADAD-SEC'). SWIFT transfers show the beneficiary name separately.
- **Saudi National Bank (SNB/NCB).** CSV: Date, Description, Reference, Debit, Credit, Balance. Card purchases show the merchant. Mada payments show 'MADA POS' then the merchant. SWIFT transfers show the beneficiary bank and name.
- **Riyad Bank.** Date, Narrative, Reference, Debit, Credit, Balance. The narrative identifies the counterparty.
- **Revolut, Wise Business.** ISO dates, clear names, separate fee lines. Classify fee lines as explicit fees, not as exempt.
- **Internal transfers.** 'Transfer between accounts', 'internal', 'حوالة داخلية'. Exclude.
- **WPS.** 'WPS', 'SALARY TRANSFER', 'رواتب' or individual employee names. Exclude as employment, once the payee is confirmed as an employee.
- **SADAD.** National bill payment system. Map on the biller name after the 'SADAD-' prefix.
- **Mada.** National debit card network. 'MADA' or 'MADA POS' then the merchant and city. The merchant is the key.
- **Arabic terms.** مشتريات (purchases), مبيعات (sales), رواتب (salaries), إيجار (rent), كهرباء (electricity), مياه (water), اتصالات (telecom).
- **Foreign currency.** Convert at the Saudi Central Bank (SAMA) rate on the date the tax falls due (IR Art 61), not the transaction date, and note the rate in the workbook.
- **GOSI.** Statutory contributions. Exclude.
- **Zakat and tax.** ZATCA debits may be VAT, zakat or both. Exclude; do not treat a VAT payment as a VAT-inclusive purchase.

### Transaction questions and defaults

Slot 9. Tier 2 catalogue for the structured form in `vat-workflow-base`.

| Item | What is missing | Default | Question | How the answer changes it |
| --- | --- | --- | --- | --- |
| Vehicle, including petrol, parking, car rental and maintenance | Whether it is restricted | No deduction | 'How many persons is the vehicle designed to carry? Is it a truck, crane or heavy equipment, held for sale or lease, a registered emergency vehicle, or used exclusively for the business with no private use at all?' | An Art 50(2) exception allows Box 7 |
| Entertainment or staff food | Whether a statutory duty applies | No deduction | 'Was this client entertainment, a staff event, or food the law obliges you to give staff at the workplace? Which law?' | Only a statutory duty allows Box 7 |
| SaaS billing entity | Legal entity and VAT number | Needs Input | 'Could you check the invoice for the legal entity and any KSA VAT number?' | KSA VAT shown: Box 7. Non-resident: Box 9. |
| Owner-named credits | Nature of the receipt | Needs Input | 'The SAR X transfer from [name]: is this a customer payment, your own money, or a loan?' | Sale, or excluded |
| Foreign credits | Art 33 limbs | Needs Input | 'Was this a service to an overseas customer? What was the service? Is it any of these: (1) leasing a means of transport by a taxable supplier to a customer that is not a taxable customer: where was it put at the customer's disposal? (2) transport of goods or passengers, or a related service: where did the transport begin? (3) a service closely linked to real estate: where is the property? (4) telecoms or an electronically supplied service: where was it actually used or enjoyed? (5) a restaurant, hotel, catering, cultural, artistic, sport, educational or recreational service: where was it actually performed? (6) a service linked to transported goods, from a taxable supplier in one Member State to a non-taxable customer in another: where was it actually performed? If any applies, is this charge for that service itself, or for a separately supplied service only connected with it? Where is the customer resident? Did the customer or a related person benefit from it directly whilst in a Member State, and can that related person fully recover input tax on it? Was it physically performed on goods in a Member State?' | All limbs met: Box 4 |
| Insurance | Type and duty | Needs Input | 'Is this life cover, or motor, health or other general cover? For staff cover, does a law require it?' | Life: exempt. Otherwise Art 50 and the invoice decide. |
| Property | Commercial or residential | Needs Input | 'Is this a commercial property with a VAT invoice, or residential?' | Commercial: Box 7. Residential: Box 11. |
| Phone and internet | Use | No deduction | 'Is this a dedicated business line or mixed use? If mixed, how is business use measured?' | Business part, if supported |
| Cash withdrawals | Use of the cash | Excluded until explained | 'What was the cash used for?' | Each purchase classified on its document |
| Payments to individuals | Nature | Needs Input | 'Was this a contractor payment with an invoice, salary, or a personal transfer?' | Contractor: invoice decides. Salary or personal: excluded. |
| GOSI | None | Excluded | None | None |
| ZATCA debit | Tax type | Excluded | 'Was this a VAT payment, a zakat payment, or both?' | No effect on boxes |
| Bank fee | Whether VAT was charged | Needs Input | 'Does the bank's advice show VAT on this fee?' | VAT shown: Box 7 |
| Government fee | Art 9(5) limbs | Needs Input | 'Does the receipt show VAT? Is this a service only that government body can provide by law?' | All limbs met: excluded |

### Excel working paper

Slot 12. The columns are those in `vat-workflow-base` Section 3. Column H accepts 1, 2, 3, 4, 5, 7, 8, 9, 10 and 11, and is blank for excluded rows. The legacy code 'RC' is replaced by 9.

**Sheet 'Box Summary'.** One row per box, computed with =SUMIFS() on column H, showing Amount, Adjustments and VAT amount: for Boxes 1, 7 and 8, VAT amount = (Amount + Adjustments) x 15%, with a reduction entered as a negative on this sheet. Box 9 VAT amount = Box 9 adjustment x 15%, with the non-deductible amount entered as a positive, as in ZATCA's example. Box 8 VAT comes from the customs declaration if it differs. Boxes 6 and 12 are totals.

**Sheet 'Return Form'.**

```
SAUDI ARABIA VAT RETURN WORKING PAPER
Tax period: ____________  VAT number: ____________

Total Sales VAT (Box 6)                                     ___________
Total Purchases VAT excluding Box 9 (Box 7 + Box 8)         ___________
Box 9 non-deductible part: Box 9 adjustment x 15%           ___________
Total VAT due for current period                            ___________
VAT Credit from previous period(s)                          ___________
Corrections from previous periods (net under SAR 15,000)    ___________
Net VAT                                                     ___________

IF Net VAT > 0: payable to ZATCA
ELSE: excess input tax, refundable or carried forward (IR Art 69)

REVIEWER FLAGS:
  [ ] Accepted documents held for every Box 7 and 8 line, and supporting documents for every Box 9 line?
  [ ] Art 50 restricted items removed?
  [ ] Export evidence within 90 days held for Box 4 goods?
  [ ] Art 33 limbs tested for Box 4 services?
  [ ] Explicit bank and processor fees tested for VAT?
  [ ] Deposits and part payments declared?
  [ ] Foreign currency at the SAMA rate?
```

The portal's own arrangement of Box 9 VAT, and the sign it takes in the adjustments column, were not viewed with figures. The net result above follows ZATCA's example in the Imports and Exports Guideline.

Use the base's conventions: blue for hardcoded values, black for formulas, green for cross-sheet references, yellow background for rows where the default flag is set. Run the base's mandatory recalculation step after building the workbook.

### Known gaps

1. The supplier library does not cover every local business, and Arabic patterns are limited to major brands.
2. The transaction patterns come from a hypothetical IT consultant in Riyadh. They do not cover construction, oil and gas, real estate or food and beverage.
3. Intra-GCC rules after the Electronic Services System are not covered.
4. First home relief is refused (R-SA-6). RETT at 5% is not computed here.
5. Marketplace rules are refused (R-SA-7).
6. Deregistration (IR Art 13), payment instalments (Art 60), assessments (Art 64), security (Art 65) and representatives (Art 77) are named, not worked.
7. Open source ZATCA repositories listed in `references.md` are not authority for any statement here.

## Deadlines and filing

**Tax periods (IR Art 58).** Monthly above SAR 40,000,000; 3-month otherwise. A person may apply for monthly (Art 58(3)) and, after 2 years on monthly, may apply for 3-month if not over the limit (Art 58(5)). ZATCA may direct otherwise (Art 58(7)). Changes take effect from the next period (Art 58(4), (6)).

**Return and payment.** Both by the last day of the month following the tax period (Arts 59(1), 62(1)). Neither the return nor the payment moves if that date falls on a non-working day: file and pay on or before it (Art 74(1)). Any other obligation under the Law or the IR that falls on a non-working day counts as done on time if done on the next working day (Art 74(2)). A working day excludes Friday, Saturday and state holidays (Art 74(3)). A separate repository guide, `sa-return-assembly`, says the 28th of the month: that conflicts with the IR and is reported. ZATCA's VAT page says 'annual tax return' for up to SAR 40,000,000: that conflicts with Art 58(2), and the IR is followed.

**Portal (Slot 4).** ZATCA website, e-services, 'Submit VAT Return' under Returns, VAT. Companies and establishments log in with their ZATCA credentials; individuals with Nafath. Payment follows through a SADAD bill ('Submit & Generate SADAD Bill').

**Registration.** At each month end, test the previous 12 months and apply within 30 days of that month end. Registration takes effect from the start of the month after the application (IR Art 3). On the forward test it takes effect from the first month expected to exceed (Art 4).

Value of annual supplies (Agreement Art 52): the total excluding exempt supplies, at any month end plus the previous 11 months, or expected at any month end plus the following 11. It counts:

- taxable supplies, standard and zero-rated, except capital asset supplies;
- goods and services supplied to the person who must pay the tax on them, which is reverse charge purchases;
- Intra-GCC supplies placed in another Member State that would be taxable at home.

A capital asset supply is left out if the asset ran the activity under a CR or similar licence and was not held for rental income or resale (IR Art 6(5)).

Each person is tested alone. Only where ZATCA gives notice under IR Art 9(2) are related persons with similar or linked activities aggregated. A person making only zero-rated supplies is excepted and may register voluntarily (Art 9(1)).

**Corrections (IR Art 63).**

- Understated net tax: notify ZATCA within 20 days of learning of it, by correcting the return (Art 63(1)).
- Exception: a net understatement less than SAR 15,000 may be added in the return for the period in which it was discovered (Art 63(3)). SAR 15,000 itself does not qualify.
- Overstated net tax: may be deducted in any later return (Art 63(2)), but not more than 5 years after the end of the calendar year containing that period (Art 63(4)).
- Every correction states the periods, the output and input tax to correct, and the reason (Art 63(5)).

ZATCA's Simplified VAT Filing Guidelines describe the 20-day notice in looser words; the IR is followed.

**Refunds.** Excess input tax: IR Art 69. A claim may be made with the return or within 5 years from the end of the calendar year of the event (Art 69(2)); an unclaimed amount carries forward (Art 69(6)). ZATCA may refuse whilst a return is outstanding (Art 69(3)), may set off or retain (Art 69(5)), pays within 60 days of approval (Art 69(4)) and may examine within 1 calendar year of the claim (Art 69(7)). Claims by persons eligible under Art 70 are separate.

**Records.** See the rates table. Kept in the Kingdom, with electronic conditions (Art 66(3)).

## Penalties and interest

VAT Law Arts 39 to 49 as read:

| Art | Breach | Penalty |
| --- | --- | --- |
| 39, 40 | Evasion | Not less than the tax due, not more than 3 times the value of the goods or services |
| 41 | Failure to apply for registration in time | SAR 10,000 |
| 42(1) | Incorrect return or amendment, or any document, that understates tax | 50% of the difference |
| 42(3) | Late filing | 5% to 25% of the tax that should have been declared |
| 43 | Late payment | 5% of the unpaid tax for each month or part of a month |
| 44 | Tax invoice issued by a non-registered person | Up to SAR 100,000 |
| 45 | Records for a tax period; obstruction; any other breach of the Law or IR | Up to SAR 50,000 |
| 47 | Repeat within 3 years | May be doubled |

Art 42(2) lets the Board waive or reduce under its rules. Art 49 is objection, under Royal Order 25711 of 8 Rabi II 1445H.

No interest charge was found in Arts 39 to 49. That was not a complete search of Saudi law, so whether interest can apply is held.

**ZATCA's lower starting point (administered).** The Law prints 50%. ZATCA's Imports and Exports Guideline, Second Edition, May 2026, s 12, says 25% of the difference, which it may raise to 50% or cut to 0%. The Agents guideline repeats it. ZATCA's Penalties page, updated 30 August 2026, still prints 50%. The Board rules behind it were not read. Show both:

- Raised by: 10% for an evasion decision under Art 39; 10% for a very poor record; 5% for a poor record; 5% where the difference exceeds 20% (monthly) or 40% (3-monthly).
- Cut by: 5% for a good record; 5% where the difference is under 5% (monthly) or 15% (3-monthly); 10% for paying within 30 days of the assessment decision; and 15% for a micro-enterprise with annual taxable revenue up to SAR 3,000,000 in the previous 12 months. Only the payment factor combines with another. No cut applies where the error is tied to an evasion decision.
- Record: good is no violations in 12 months. Poor is more than 2 and up to 6 on monthly filing, or 1 or 2 on 3-monthly. Very poor is more than 6, or more than 2.
- None: where corrected under IR Art 63 before notice of audit; or where the difference is less than SAR 5,000.
- After notice of audit: a voluntary disclosure exceeding 50% of the differences found reduces it to 10%, and to 0% if the tax is paid within 30 days of the assessment.

**Field violations (administered).** Reclassified from 30 January 2022. A first violation brings notice, with 30 to 60 days to fix it (ZATCA's 2022 news page said up to 3 months); fines start on recurrence. Obstruction has at most 10 days. The classification table, including e-invoicing amounts, is in a ZATCA guideline not obtained: held. The E-Invoicing Regulation is part of the IR and applies the Law's penalties by express text; that Art 45 is the limb reaching it is an inference.

**Instalments.** IR Art 60 lets ZATCA allow instalments on evidence of inability to pay or hardship. ZATCA answers within 20 days. The span is at most 12 months, which the Board may extend under separate controls. Missing 2 instalments lets ZATCA cancel the plan, and any late payment fine continues over the extension (Art 60(7)).

**Fine waiver initiative (announced).** ZATCA's Cancellation of Fines and Exemption of Financial Penalties Initiative was extended 6 months from 1 July 2026 and ends on 31 December 2026, per its news page last updated 29 June 2026 and its simplified guide as of 1 July 2026. The Minister's decision was not read.

- Covers unpaid fines for late registration, late payment and late filing in all tax laws, and VAT return correction fines. Taxes: VAT, withholding tax, excise tax, corporate income tax and RETT.
- Requires: registration; every outstanding return submitted or corrected; and full principal tax paid, or an instalment request made whilst the initiative is in effect with every instalment paid on time. A cancelled plan restores the fines.
- Excludes: fines under VAT Law Art 45; fines paid before the effective date; fines on any return due after 30 June 2026, which ZATCA says any further extension will not cover either; and evasion fines, including late payment, filing, registration or amendment fines tied to evasion.

## Cross-border points

**Reverse charge.** A taxable customer pays tax on a supply from a non-resident supplier where the place of supply is in KSA (Agreement Arts 9(2), 41; IR Art 47(1)), and reports output tax and any deductible input tax in that period's return. Box 9 holds the amount. The form treats the tax as deductible, so a fully taxable customer pays nothing net. A person who cannot deduct in full enters the non-deductible part in the adjustments column. An exempt service, such as a loan from a non-resident, is not reported. ZATCA applies this to services from a GCC resident too (Imports and Exports Guideline, s 9.3).

**Imports.** The importer pays tax to customs on release, on the customs value plus insurance, transport, ZATCA's charges and customs and excise duties (Agreement Arts 28(1), 42; IR Art 43; Imports and Exports Guideline s 15). Box 8. A taxable person may instead account through the return (IR Art 44), with ZATCA's approval, in the cases in Art 44(2), read here as cumulative: (a) monthly tax period and an intention to import at least once a month; (b) all returns and payments in the last 12 months, or the shorter registered period, were on time and other VAT obligations met; (c) sufficient proof of financial stability. Art 44(8) lets the Board allow other cases. Then Box 9.

**GCC states.** IR Art 79(6) treats a Member State with no VAT, or with no Electronic Services System with KSA, as a third country. Until that system is in place in all Member States, goods from another Member State are imports and goods to one are exports (Art 79(7)), with the same evidence as other exports. ZATCA starts the system by order (Art 79(8)); no such order was found, and its May 2026 guideline still describes the transitional rules as current. So:

- There is no GCC box. The legacy Field 3/4 at 15% and the rule to treat the UAE, Bahrain and Oman as domestic are removed.
- Services to a recipient in another GCC state may be zero-rated under Art 33, because Art 79(6) treats that state as outside GCC territory for now, if all Art 33 limbs are met.
- Whether a named state has a VAT system at the date of supply is a fact to verify.

## Two worked examples that recompute

All examples are hypothetical. Examples 1 to 5 each carry an `oa-check` block that `scripts/check-examples.py` recomputes. The patterns meet the workflow base's minimum.

### Example 1: registration test

In the 12 months to the end of May 2026, a sole establishment has standard-rated sales of SAR 300,000, exports of SAR 60,000, residential rent of SAR 150,000 and a van sold for SAR 40,000 that had run the business under its CR. It received services from a non-resident of SAR 20,000. A second trader has the same figures but no reverse charge services.

```oa-check
name: SA annual supplies test with exempt and capital assets out
inputs:
  standard: 300000
  zero_rated: 60000
  exempt: 150000
  capital_asset: 40000
  reverse_charge: 20000
  mandatory: 375000
  voluntary: 187500
steps:
  - value_first: standard + zero_rated + reverse_charge
  - excess_first: max(value_first - mandatory, 0)
  - value_second: standard + zero_rated
  - excess_second: max(value_second - mandatory, 0)
  - voluntary_room_second: max(value_second - voluntary, 0)
expected:
  value_first: 380000
  excess_first: 5000
  value_second: 360000
  excess_second: 0
  voluntary_room_second: 172500
```

Decision: the first trader's value exceeds SAR 375,000, so it must apply within 30 days of the end of May 2026. The second trader's does not, so it need not register, though it may. Only the trader's own figures count, unless ZATCA gives notice under IR Art 9(2).

### Example 2: 3-month return, paid late

Tax period July to September 2026. Box 1 SAR 400,000, Box 4 SAR 100,000, Box 7 SAR 150,000, Box 9 SAR 10,000 with no adjustment. Prior credit SAR 2,000. A net understatement from an earlier period of SAR 3,000 is added. The due date is Saturday 31 October 2026 and does not roll forward (Art 74(1)). It is paid on 10 December 2026, 2 months or part months late.

```oa-check
name: SA 3-month return and late payment fine
inputs:
  box1: 400000
  box7: 150000
  box9: 10000
  box9_adjustment: 0
  rate: 0.15
  prior_credit: 2000
  correction: 3000
  months_late: 2
  fine_rate: 0.05
steps:
  - output: box1 * rate
  - input: box7 * rate
  - box9_net: box9_adjustment * rate
  - net_vat: max(output - input + box9_net - prior_credit + correction, 0)
  - fine: net_vat * fine_rate * months_late
expected:
  output: 60000
  input: 22500
  box9_net: 0
  net_vat: 38500
  fine: 3850
```

Decision: pay SAR 38,500 and SAR 3,850 for late payment. The initiative does not help, because this return fell due after 30 June 2026. The late filing fine under Art 42(3) is separate if the return was also late.

### Example 3: correction gate and penalty on both footings

Understatements of SAR 12,000 and of SAR 15,000, then one of SAR 20,000 found on audit, paid within 30 days, with a good record and no other factor.

```oa-check
name: SA Art 63 gate and incorrect return penalty
inputs:
  small: 12000
  at_limit: 15000
  limit: 15000
  audited: 20000
  law_rate: 0.5
  guideline_rate: 0.25
  good_record_cut: 0.05
  payment_cut: 0.10
steps:
  - room_small: limit - small
  - room_at_limit: limit - at_limit
  - penalty_law: audited * law_rate
  - penalty_guideline_start: audited * guideline_rate
  - penalty_guideline_cut: audited * max(guideline_rate - good_record_cut - payment_cut, 0)
expected:
  room_small: 3000
  room_at_limit: 0
  penalty_law: 10000
  penalty_guideline_start: 5000
  penalty_guideline_cut: 2000
```

Decision: positive room means the correction may go in the return, so SAR 12,000 may. Zero room means it is not 'less than' SAR 15,000, so SAR 15,000 needs the return corrected within 20 days. On SAR 20,000 show SAR 10,000 under the Law and SAR 2,000 under ZATCA's guideline, and refer the gap.

### Example 4: proportional deduction, reference only

Figures from ZATCA's example in its Simplified VAT Filing Guidelines, which uses annual rents; here they are treated as the past calendar year's supplies for Art 51(4). Taxable SAR 500,000, exempt SAR 300,000. Shared cost SAR 20,000 plus VAT SAR 3,000. R-SA-1 stops the workflow on these facts; the figures show the Art 51(4) fraction.

```oa-check
name: SA Art 51 default fraction
inputs:
  taxable: 500000
  exempt: 300000
  shared_base: 20000
  shared_vat: 3000
steps:
  - fraction: taxable / (taxable + exempt)
  - deductible_vat: shared_vat * fraction
  - blocked_vat: shared_vat - deductible_vat
  - blocked_base: shared_base - shared_base * fraction
expected:
  fraction: 0.625
  deductible_vat: 1875
  blocked_vat: 1125
  blocked_base: 7500
```

Decision: SAR 1,875 is deductible. In the box, SAR 7,500 goes in the adjustments column as a reduction.

### Example 5: reverse charge, partly deductible

ZATCA's example uses a 2018 invoice at 5%. A bank may deduct 70%. It receives legal advice from a British firm for SAR 100,000. Box 9 Amount SAR 100,000, adjustments SAR 30,000. The same facts at 15% are shown.

```oa-check
name: SA Box 9 non-deductible part at 5% and 15%
inputs:
  amount: 100000
  deductible_share: 0.7
  old_rate: 0.05
  rate: 0.15
steps:
  - adjustment: amount * (1 - deductible_share)
  - payable_old: adjustment * old_rate
  - payable_now: adjustment * rate
expected:
  adjustment: 30000
  payable_old: 1500
  payable_now: 4500
```

Decision: VAT payable of SAR 4,500 at 15%, against nil for a fully taxable customer. R-SA-1 would stop a real workflow here.

### Transaction patterns

Slot 11. Six classifications from a hypothetical self-employed IT consultant in Riyadh, all subject to the operational hold.

**1. Non-resident SaaS.** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; SAR 60.00`. Invoice from a US entity with no KSA VAT: Box 9, Amount SAR 60, VAT SAR 9, deductible through the form, net nil for a fully taxable client. Without the invoice, Needs Input. Convert at the IR Art 61 rate.

**2. Export of services.** `10.04.2026 ; TECHCORP INC DELAWARE ; CREDIT ; Invoice SA-2026-018 IT consultancy March ; +25,000.00 ; SAR`. Box 4 at 0% only if no Art 33(2) limb applies: (a) no special case in Agreement Arts 17 to 21 places the service in a Member State (a place in KSA under the general rule in Art 15 does not count, and a service supplied separately from a special case service is not caught); (b) the customer is not resident in any Member State; (c) the customer or a related person does not benefit directly from the same services whilst in a Member State where that related person cannot fully recover input tax on them; (d) the service is not physically performed on tangible goods in a Member State during the supply. Otherwise Needs Input. The legacy 'no KSA establishment' question is too narrow.

**3. Client dinner.** `15.04.2026 ; THE GLOBE RESTAURANT RIYADH ; DEBIT ; Client dinner ; -1,800.00 ; SAR`. Blocked by Art 50(1)(b) despite the business purpose. Not in Box 7; excluded, with the reason noted.

**4. Office equipment.** `18.04.2026 ; JARIR BOOKSTORE ; DEBIT ; Invoice JR-2026-441 Laptop HP ; -5,750.00 ; SAR`. Gross SAR 5,750 with 15% VAT: net SAR 5,000, VAT SAR 750, Box 7, for business use, with a tax invoice, a correctly issued simplified tax invoice or other Art 49(7) document held. Otherwise Needs Input. A capital asset: Art 52 applies if its use later changes.

**5. Car lease.** `22.04.2026 ; AL JAZIRAH VEHICLES ; DEBIT ; Monthly car lease ; -4,500.00 ; SAR`. A car for no more than 10 persons is restricted unless an Art 50(2) exception is shown. Blocked by Art 50(1)(d) by default, excluded with the question asked. If used exclusively for the business and not available for private use, Box 7.

**6. Bank fee.** `28.04.2026 ; AL RAJHI BANK ; DEBIT ; Monthly account maintenance ; -50.00 ; SAR`. An explicit fee, so not exempt under Art 29(1). If the bank's document shows VAT: net SAR 43.48, VAT SAR 6.52, Box 7. If not, Needs Input. It is not 'exempt financial service'.

## Ask the client first

Ask these 6 groups before any output. The onboarding fallback is intake only: questions come before any working paper (`vat-workflow-base` Step 6.5 before Step 7), and whatever stays unanswered is Needs Input. Nothing is generated with pending flags first.

1. **Entity.** Are you a sole establishment ('مؤسسة'), an LLC ('شركة ذات مسؤولية محدودة') or another type? What is your VAT number (15 digits, first and last digit 3) and CR number? In one sentence, what does the business do?
2. **Period.** Which tax period does this cover? Monthly (which month) or 3-month (which quarter)? Monthly applies above SAR 40,000,000 of annual taxable supplies, or on application.
3. **Sales.** Do you make exempt sales, such as residential rent, financial services or life insurance (if so R-SA-1 may fire)? Do you have customers outside KSA, are they businesses, and where are they resident? Have you received deposits or part payments?
4. **Purchases.** Do you hold tax invoices for purchases, and which foreign suppliers bill KSA VAT? Do you have vehicles, and do you have employees?
5. **E-invoicing.** Are you in Phase 2, integrated with FATOORA? If not, has ZATCA notified you of a wave?
6. **Balances.** Do you have excess input tax carried forward from the previous period? Are any earlier returns wrong?

### Completion checks

- Every Box 7, 8 and 9 line has a document the law accepts.
- Art 50 items are removed, with a statutory duty named where one is relied on.
- Box 4 goods have evidence within 90 days; Box 4 services pass every Art 33 limb.
- Explicit financial fees are tested, not assumed exempt.
- Deposits and part payments are declared.
- Prior period credit is carried forward; corrections respect the SAR 15,000 limit.
- The operational hold is stated in the reviewer brief.

## Sources

Read dates are actual. All were retrieved by plain request from ZATCA's site. Where a row says 'read in part', the rest was not read.

| Source | URL | Read on |
| --- | --- | --- |
| VAT Law, official Arabic text, read in part: Arts 2, 18 and 39 to 49, and the article count | https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%82%D9%8A%D9%85%D8%A9%20%D8%A7%D9%84%D9%85%D8%B6%D8%A7%D9%81%D8%A9%20(2).pdf | 2026-11-05 |
| ZATCA VAT Law page, for dates | https://zatca.gov.sa/en/RulesRegulations/Taxes/Pages/VATLaw.aspx | 2026-11-05 |
| Unified Agreement, read in full in the copy on ZATCA's Arabic path, an English text marked 'Unofficial Translation'; the Agreement says it was executed in Arabic | https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/GCC%20VAT%20Agreement.pdf | 2026-11-05 |
| Implementing Regulations, official Arabic Tenth Edition, read in part: Arts 3 to 7, 9, 10, 13, 17, 20, 25, 29 to 36 bis(2), 40, 43 to 47, 48(1) to (3), 49 to 54, 58 to 63, 66, 69, 70(9) to (11), 74 and 79 and the amendment appendix for Art 63; headings only of Arts 11, 12, 64, 65 and 77 | https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf | 2026-11-05 |
| Implementing Regulations, English Eighth Edition, read in full. Unofficial and out of date; used to locate provisions and to corroborate that Art 34(7) covers either direction | https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf | 2026-11-05 |
| ZATCA guide to the IR amendments, Issue 1, April 2025, read in part: Art 47 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Amendments-to-the-Implementing-Regulation-of-(VAT).PDF | 2026-11-05 |
| Input Tax Guideline, 3rd version, May 2026, read in part: ss 4, 7, 8 and the apportionment example | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Guideline-on-Input-Tax-Deduction-under-VAT-Provisions.pdf | 2026-11-05 |
| Imports and Exports Guideline, Second Edition, May 2026, read in part: ss 5.1, 5.3, 6, 8, 9, 11.3, 12 and 15 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Guideline-on-Imports-and-Exports-under-VAT-Provision.pdf | 2026-11-05 |
| Agents Guideline, Second Version, May 2026, read in part: penalties | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Guideline-For-Agents-under-VAT-Provisions.pdf | 2026-11-05 |
| Tax Groups Guideline, Third Version, read in part: field violations | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Guideline-on-Tax-Groups-under-VAT-Provisions.pdf | 2026-11-05 |
| Simplified VAT Filing Guidelines, Arabic, read in full, form pages viewed | https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/Simplified_VAT_Filing_Guidelines.pdf | 2026-11-05 |
| ZATCA e-services manual 009, return screens viewed | https://zatca.gov.sa/en/eServices/Documents/eServices_Manual_009.pdf | 2026-11-05 |
| E-Invoicing Regulation, read in full | https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/E-invoicing-Regulations.pdf | 2026-11-05 |
| E-Invoicing Implementation Resolution of 19 May 2023, unofficial English, read in part: clauses Eighth and Ninth and QR annex | https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/20230519_E-Invoicing%20Implementation%20Resolution%20English.pdf | 2026-11-05 |
| XML Implementation Standard v1.2, read in part: code lists and BR-KSA rules | https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf | 2026-11-05 |
| ZATCA e-invoicing roll-out phases | https://zatca.gov.sa/en/E-Invoicing/Introduction/Pages/Roll-out-phases.aspx | 2026-11-05 |
| ZATCA news, Wave 24 | https://zatca.gov.sa/en/Pages/news-1426.aspx | 2026-11-05 |
| ZATCA news, Wave 25 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx | 2026-11-05 |
| ZATCA Penalties page | https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/Penalties.aspx | 2026-11-05 |
| ZATCA news on reclassifying field violations | https://zatca.gov.sa/en/MediaCenter/News/Pages/reclassifing-field-violations-of-VAT.aspx | 2026-11-05 |
| ZATCA news on the fine waiver extension, last updated 29 June 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Cancellation-of-fines-Dec-2026.aspx | 2026-11-05 |
| ZATCA simplified guide to the fine waiver, as of 1 July 2026, read in part: to Example 2 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf | 2026-11-05 |
| ZATCA RETT Law page | https://zatca.gov.sa/en/RulesRegulations/Taxes/Pages/RETTRegulation.aspx | 2026-11-05 |
| ZATCA RETT Guideline, Version 6, May 2026, read in part: ss 1.1, 4.5 and 5 opening | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Detailed-Guideline-for-RETT-In-accordance-with-provision-of-RETT-Law-and-its-Implementing-Regulations.pdf | 2026-11-05 |
| ZATCA VAT page, read for the 'annual tax return' wording | https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/default.aspx | 2026-11-05 |
| ZATCA About VAT page, read for the 2018 start and rate | https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/About-Vat.aspx | 2026-11-05 |

Not yet confirmed: the Arabic text of the Unified Agreement, read only in an unofficial English translation; any IR amendment after Resolution 24-06-01; whether the GCC ministerial committee changed SAR 375,000 or the 50% voluntary level; the Gregorian date on the IR's cover, which does not match its Hijri date; the Board rules behind ZATCA's 25% starting point against the Law's 50%; the ZATCA guideline classifying general VAT violations and e-invoicing fine amounts; the Minister's decision on the fine waiver; the order starting the Electronic Services System and each GCC state's position; the instrument for sales on which the government bears the VAT; whether hotel stays are 'hospitality' under Art 50(1)(b), how employee housing and childcare fall under Art 50, and the Employee Benefits Guideline; the rate of general insurance and general takaful beyond the Art 29(7) exemption; the 'SFDA list' for medicines; whether a non-compliant e-invoice supports a deduction; the payment means subset of UNTDID 4461; the rule for agreements subject to a suspensive condition; the record period for real estate that is not a capital asset (6 or 15 years); interest on late VAT; the live portal's correction limit, adjustment sign and row numbers after Box 12; the box for a seller's international transport under Art 34 and for flights bought; the legacy note that SAR is pegged to USD at about 3.75; the instrument fixing the Art 47(3) start beyond ZATCA's 'starting from January 2026'.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | 2026-11-05 | Converted to the upstream template. `reviewed_by` removed and tier set to 2 because this text has not been reviewed. Rebuilt the return boxes on ZATCA's form. Corrected instruments, input restrictions, financial fee and real estate treatment, GCC rules, Art 33 limbs, correction limit, currency date and refusal citations. Replaced rate and location defaults with Needs Input. Added the operational hold, penalties, Wave 25 and R-SA-8. |
| 2.1 | November 2026 | Legacy: penalty amnesty updated to the extension ending 31 December 2026. |
| 2.0 | April 2026 | Legacy: rewrite on the Malta v2.0 structure. |
| 1.1 | April 2026 | Legacy: April 2025 IR amendments, amnesty extension, Wave 24. |
| 1.0 | April 2026 | Legacy: initial standalone skill. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax consultant, CPA, or equivalent practitioner in your jurisdiction) before filing or acting upon.
