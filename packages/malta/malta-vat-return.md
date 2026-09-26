---
name: malta-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Malta VAT return (Article 10 periodic return via CFR) or Article 11 annual declaration for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "periodic VAT return", "CFR VAT", "create the return", "Article 11 declaration", or any request involving Malta VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Malta only and only Article 10 (standard) and Article 11 (small enterprise) registrations. Article 12, partial exemption, capital goods scheme adjustments, margin schemes, and VAT groups are all in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any Malta VAT work.
version: 2.0
jurisdiction: MT
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta VAT returns: Article 10, Article 11 and Article 12

## Scope

This Guide covers preparing and checking Maltese VAT filings for a business established in Malta: the Article 10 periodic return, the Article 11 small-enterprise declaration and the Article 12 obligations. It covers registration type, rates, input VAT, cross-border reverse charge, recapitulative statements, the One Stop Shop (OSS), penalties, interest and records.

Figures are for tax year 2026. The law is the VAT Act, Chapter 406 of the Laws of Malta, as consolidated on 27 March 2026 (amendments up to Act III of 2026 and Legal Notice 75 of 2026), plus its subsidiary legislation. VAT in Malta is charged per transaction and per tax period, so "tax year 2026" means periods falling in calendar 2026. A short section near the end covers 2025 periods still being filed.

The authority is the Malta Tax and Customs Administration (MTCA); the Act calls the office-holder the Commissioner for Tax and Customs. Returns, registrations and statements go through MTCA's online services. This Guide does not reproduce the box numbers of the return form. Take them from the live form on the MTCA site, and check MTCA's published filing calendar against the statutory dates below.

Main sources, all on legislation.mt:

- VAT Act, Cap. 406, current consolidated text: https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20
- VAT Act, Cap. 406, as in force on 13 September 2024 (for the pre-2025 Article 11 rules): https://legislation.mt/getpdf/67691cdeb52f1d38d8a4103f
- S.L. 406.19, VAT (Rate of Interest) Regulations: https://legislation.mt/getpdf/632835ddda6f862638d03ac1
- S.L. 406.12, VAT (Adjustments relating to Input Tax on Capital Goods) Regulations: https://legislation.mt/getpdf/60225988bc8272018c0f72fb
- S.L. 406.14, VAT (Recapitulative Statement of Intra-Community Transactions) Regulations: https://legislation.mt/getpdf/678a0da50dba9f0950780cb6

## Ask the client first

- Which article are you registered under: 10, 11, 11A or 12, or more than one? Send the registration certificate. It states the article, the effective date and the registration number. An MT prefix means Article 10 or 12. An Article 11 number has no MT prefix and is not a VAT identification number.
- What are the start and end dates of your tax period? Do not assume calendar quarters. The Commissioner sets your first period, and each later period runs three months from the end of the one before.
- What was your turnover, excluding VAT, in calendar 2025, and so far in 2026? If you are a company, does anyone who owns or controls more than 10% of you also trade? ([Act, Sixth Schedule](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))
- What do you sell, and to whom? Split sales into: Malta sales by rate, exempt sales, exports outside the EU, EU business customers (goods or services), and EU consumers.
- Do you buy goods or services from suppliers outside Malta, and do their invoices show foreign VAT, Maltese VAT or no VAT?
- Do you make any exempt-without-credit supplies (residential letting, insurance, financial services, medical care, education)?
- Did you buy any car, boat or aircraft, or pay for fuel, repairs, entertainment, alcohol or tobacco in the period?
- Did you buy equipment, tools or office furniture costing €1,160 or more, or any property? ([S.L. 406.12](https://legislation.mt/getpdf/60225988bc8272018c0f72fb))
- Is there an excess credit from the previous period, and has any of it been refunded or set off?
- Have you filed every earlier VAT return and income tax return? A refund is withheld while a return is missing.

## The method, step by step

1. Confirm the registration type from the certificate before anything else ([Act, arts 10-13](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)). Article 10 files periodic returns and recovers input VAT. Article 11 charges no VAT, recovers none and files a declaration. Article 12 only pays VAT on its EU acquisitions and reverse-charge services. If you prepare the wrong filing, every later step is wrong.
2. Fix the period from the certificate or the MTCA account (art. 17). Sort every invoice by the date VAT became chargeable, not by bank date.
3. Split sales into ([Act, Eighth and Fifth Schedules](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)): taxable at 18%, 12%, 7% or 5%; exempt with credit (exports, intra-EU goods to a valid VAT number, food, medicines, international passenger transport); exempt without credit; and outside the scope (for example B2B services supplied to a customer established abroad). Use the rate table below.
4. For each foreign purchase, decide whether the supplier charged VAT. No VAT and the supplier is not established in Malta: you, as an Article 10 person, owe the Maltese VAT under art. 20(2) and put it in both output and input tax. Foreign VAT charged: that is not Maltese input tax; do not put it on the return.
5. Remove blocked input VAT (Tenth Schedule item 3), then apportion anything partly private (item 4). If you also make exempt-without-credit supplies, stop and refer (partial exemption).
6. Flag capital goods ([S.L. 406.12](https://legislation.mt/getpdf/60225988bc8272018c0f72fb)): equipment, tools or office furniture at €1,160 or more, and all immovable property. Record the date of first use, because later changes of use are adjusted over 5 or 20 years.
7. Net output against input tax, deduct any excess credit brought forward that has not been refunded or set off (art. 21(1)), and read the balance: payable, or an excess credit to carry forward or claim.
8. File and pay by the due date. Then file the recapitulative statement if you supplied goods or services to EU business customers, and the OSS return if you use OSS.
9. Keep the VAT account and working papers with the records listed below, for at least six years. For capital goods, the six years start only when the 5-year or 20-year adjustment period ends.

## Registration types ([Act, arts 10-12 and Sixth Schedule](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))

| Type | Who | Key rules |
| --- | --- | --- |
| Article 10 (standard) | A taxable person established in Malta who makes supplies in Malta other than exempt-without-credit supplies, or who supplies services in another Member State where the customer pays the VAT | Apply within thirty days of the first such supply. Charges VAT, recovers input VAT, files periodic returns. Apply to cancel within fifteen days of ceasing to qualify. |
| Article 11 (small enterprise, domestic) | A taxable person established in Malta whose turnover in the preceding calendar year was not more than the domestic threshold of €35,000 | Optional: the person applies. Charges no VAT and recovers none. Loses status on the date turnover passes €35,000 within a calendar year and must apply to cancel within fifteen days. An Article 10 registrant cannot switch in the first whole 12 calendar months, and the Commissioner may accept an earlier switch only if no input tax was claimed. |
| Article 11A | A small enterprise established in Malta using another Member State's small-enterprise exemption | EU-wide turnover must stay below the Union threshold of €100,000. Quarterly declaration by the last day of the month after the quarter. Number carries the suffix EX. |
| Article 11B | A small enterprise established in another Member State using Malta's exemption | Needs Malta turnover not above €35,000 and EU turnover below €100,000 in the preceding year. |
| Article 12 | A person not registered under Article 10 who: buys goods from other Member States above the acquisitions threshold of €10,000 in a calendar year; or receives services on which it must pay Maltese VAT under art. 20(2); or supplies services in another Member State where the customer pays | Register by the date of the acquisition, the service received or the service supplied. Pays the VAT; no input VAT recovery. An Article 11 person who does any of these must also register under Article 12. |

Turnover for Article 11 excludes VAT and disposals of capital assets. For a company, add the proportionate turnover of any person who owns or controls it, directly or indirectly, by more than 10%.

### What changed on 1 January 2025 ([2024 text of the Act](https://legislation.mt/getpdf/67691cdeb52f1d38d8a4103f))

Before 2025, Article 11 used two activity-based thresholds, tested on a rolling twelve months. They no longer apply. Use them only to understand pre-2025 files.

| Category (pre-2025) | Entry threshold | Exit threshold |
| --- | --- | --- |
| Economic activities consisting principally in the supply of goods | €35,000 | €28,000 |
| Other economic activities | €30,000 | €24,000 |

From 2025 there is one domestic threshold of €35,000 for all activities, measured on the preceding calendar year, with a Union threshold of €100,000 for the cross-border schemes. The current text, after Act IX of 2025 and Act III of 2026, still states €35,000.

## Rates for 2026 ([Act, art. 19, Eighth Schedule and Fifth Schedule](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))

| Rate | What it covers (summary of the statutory items) |
| --- | --- |
| 18% | Every taxable supply not listed below, and imports (art. 19(1) and (4)) |
| 12% | Custody and management of securities; management of credit and credit guarantees by someone other than the person who granted the credit; hire of a pleasure boat for a term that, with earlier hires to the same person in the previous twelve months, does not exceed five weeks; care of the human body by a profession regulated by the Health Care Professions Act, including health studios, other than exempt medical care |
| 7% | Accommodation in premises that must be licensed under the Malta Travel and Tourism Services Act; use of sporting facilities |
| 5% | Electricity; listed confectionery and similar goods by CN code; listed medical accessories; printed matter, including books and audio books on physical media or supplied electronically (not publications mainly advertising, video or music); listed items for the exclusive use of disabled persons; imports of works of art, collectors' items and antiques; minor repairs of bicycles, shoes and leather goods, clothing and household linen; domestic care services; admission to museums, art exhibitions, concerts and theatres |
| Exempt with credit (zero-rated) | Exports; intra-EU goods to a customer with a valid and active VAT number of another Member State; food for human consumption, excluding catering; pharmaceutical goods; international passenger transport; scheduled bus services; listed sea vessel and aircraft supplies |
| Exempt without credit | Most lettings of immovable property; transfers of immovable property; insurance; most credit, banking and securities dealing; medical care; education; public postal services; supplies by Article 11, 11A and 11B persons |

Accommodation priced with other goods or services: 80% of the price is treated as accommodation and 20% as the other supplies. The goods lists at 5% are by CN code, so check the code, not the product name.

## Input VAT: recovery and blocked items ([Act, arts 22-24 and Tenth Schedule](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))

Only an Article 10 person recovers input VAT. It is recoverable to the extent the purchase is used for taxable supplies, exempt-with-credit supplies, or supplies made outside Malta that would be taxable here.

Evidence: a tax invoice in your name (or an import document naming you as importer), held and producible. For reverse-charge purchases and intra-EU acquisitions, the VAT must also be declared as due on the same return. Under cash accounting, deduction arises when you pay the supplier.

| Blocked (item 3(1)) | Exception (item 3(2) and (1)(c)) |
| --- | --- |
| Tobacco and tobacco products; alcoholic beverages; works of art, collectors' items and antiques | Bought for resale in the normal course of business |
| Motor vehicles, vessels and aircraft, including hire and leasing, and their repair, maintenance and fuel | Resale; carriage of goods or passengers for a consideration; hire with a driver or self-drive hire (self-drive fuel stays blocked); driving instruction; vehicles designed for goods with seats next to the driver, or with seats for nine or more; listed vessel and aircraft charter and commercial uses |
| Receptions, entertainment and hospitality | Where you provide them for consideration in the normal course of your business |
| Transport or entertainment for employees or officers | Transport on vehicles with a seating capacity of not less than seven |

Partly private use: only the business proportion is input tax.

Partial exemption: if input tax relates to both deductible and exempt-without-credit supplies, the credit uses last year's ratio provisionally and this year's ratio definitively, with the difference in the first return of the next year. A non-deductible amount under €20 multiplied by the months in the period is allowed in full. Refer this work (see "When to refuse or refer").

Capital goods ([S.L. 406.12](https://legislation.mt/getpdf/60225988bc8272018c0f72fb)): small equipment, working tools and office furniture below €1,160 are outside the scheme. Deductions on capital goods are adjusted by one-fifth a year over 5 years, and on immovable property by one-twentieth a year over 20 years, when the deductible use changes. The regulation says "price, or open market value" and does not say whether VAT is included. Check with MTCA before relying on a VAT-inclusive test. Keep a list of the capital goods subject to adjustment, showing the input tax deducted and each adjustment. For these goods, the six-year retention period in art. 48(4) starts from the end of the adjustment period (regs 6 and 7).

Credit notes and price reductions ([Act, Tenth Schedule item 11](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)): if the taxable value of a supply or intra-EU acquisition is reduced after it takes place, the output tax on the reduction is deducted in the period in which the cause of the reduction occurs. You do not amend the original period. The condition is that the output tax on the original value was properly accounted for.

Foreign currency ([Act, Seventh Schedule item 8](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)): convert to euro at the latest selling rate applied by commercial banks in Malta at the time the tax becomes chargeable. The latest European Central Bank rate at that time is also accepted. Imports follow the customs valuation rules.

Excess credit ([Act, art. 24](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)): if deductions exceed output tax, the excess is carried forward or refunded. A refund is due not later than 5 months after the later of the return's due date or its filing date. The Commissioner can extend this by up to twelve months to verify it, and withholds it while any VAT or income tax return is missing.

## Cross-border: reverse charge, recapitulative statements and OSS

### Reverse charge ([Act, art. 20 and Third Schedule](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))

- Services bought by a business: taxed where the customer is established (Third Schedule Part Two item 2(a)). When the supplier is not established in Malta and not registered under Article 10, the Maltese customer pays the VAT (art. 20(2)). For B2B services taxed in Malta under the general rule, this means any taxable person, including an Article 11 person, and any VAT-identified non-taxable legal person (art. 20(2)(b)). For other goods and services it means an Article 10 or Article 12 person, or a VAT-identified non-taxable legal person (art. 20(2)(c)).
- Article 10 customer: declare the VAT as output tax and deduct it as input tax on the same return, subject to the blocks above. For a fully taxable business the net is nil.
- Article 12 customer (including an Article 11 person that registered under Article 12): pays the VAT by the 15th of the second month after the invoice date or the month of receipt, whichever is earlier (art. 21(3)), with a notice of payment (art. 30A). No deduction.
- Goods bought from another Member State by an Article 10 person are an intra-EU acquisition, taxed at the rate for the same goods in Malta. Declare and deduct as above.
- A foreign supplier that charged its own VAT has not used the reverse charge. That VAT is not Maltese input tax. Any recovery goes through that State's refund procedure.

### Sales to other EU countries

- Services to a business established in another Member State: taxed there. No Maltese VAT; the customer accounts for it. You must be registered under Article 10 or 12 for these supplies.
- Goods to a business in another Member State: exempt with credit only if the customer's valid and active VAT number of another Member State is on the invoice, the goods leave Malta, and you file a correct recapitulative statement. Article 11 and 11B persons cannot use this exemption.

### Recapitulative statements ([S.L. 406.14](https://legislation.mt/getpdf/678a0da50dba9f0950780cb6))

Article 10 persons file one for intra-EU supplies of goods, triangulation onward supplies, and services to EU customers who pay the VAT (Act, art. 30(2)).

| Filer | Period | Due |
| --- | --- | --- |
| Default | Each calendar month | 15th of the following month |
| Goods: quarterly total, excluding VAT, not over €50,000 in the quarter or in any of the previous four quarters | Each calendar quarter | 15th of the month after the quarter |
| Goods: quarterly total passes €50,000 during the quarter | Monthly, from the end of the month in which it is passed; a statement is due for each month already elapsed in the quarter | 15th of the month after the last month covered |
| Services only | Each calendar quarter | 15th of the month after the quarter |
| Both goods and services | Follow the goods rules | As for goods |

### OSS for sales to EU consumers ([Act, Third Schedule and Fourteenth Schedule Part Seven](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))

- Intra-EU distance sales of goods, together with telecommunications, broadcasting and electronically supplied services to consumers in other Member States, stay taxed in Malta while their total, excluding VAT, does not exceed €10,000 in the current calendar year and did not in the previous one. This applies only to a supplier established in one Member State. Above that total, from the moment it is passed, they are taxed in the customer's State. You may also opt in below the threshold; the option lasts at least two calendar years.
- The Union OSS scheme lets you declare that foreign VAT on one quarterly return filed through MTCA, due by the end of the month after the quarter, even if nothing was sold. OSS records must be kept for ten years from 31 December of the year of the transaction.

## Boundary and exception table ([Act, Fifth, Eighth and Tenth Schedules](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))

| Situation | Treatment |
| --- | --- |
| 2025 turnover €35,000 exactly | Qualifies for Article 11: the test is "not more than" the threshold |
| Article 11 person passes €35,000 during 2026 | Stops qualifying on that date; apply to cancel within fifteen days. After the person applies, cancellation takes effect from the first day of the next calendar month (art. 11(7)), and the Article 10 registration, if liable, runs from that same date (art. 10(6)(c), (7a)). If the Commissioner cancels instead (art. 11(8)), both take effect from the date the person stopped qualifying |
| Company with a shareholder who owns more than 10% and trades | Add that person's proportionate turnover before testing €35,000 |
| Food sold in a shop | Exempt with credit |
| Food served in the course of catering | Not in the food exemption; 18% unless another item applies |
| Confectionery or similar goods | 5% only for the CN codes listed in item 3 of the Eighth Schedule; otherwise 18% |
| Holiday let in premises licensed under the Malta Travel and Tourism Services Act | 7% |
| Residential letting in premises that need no such licence | Exempt without credit, including lets of thirty days or less |
| Other letting of immovable property for thirty days or less by a taxable person in business | Taxable (18%). This does not apply to: licensed accommodation (7%), designated parking, letting of installed equipment and machinery or safes, and a company's letting to an Article 10 person (each taxed under its own rule); nor to space for artistic and cultural activities, unlicensed residential lets, garages and stores, or rooms lawfully designated for poker (these stay exempt) |
| Letting by a limited liability company to an Article 10 person for its business | Taxable (18%) |
| Van designed for goods with seats next to the driver | Not blocked; fuel and repairs deductible |
| Company car used only for business | Blocked, including lease, fuel and repairs |
| Restaurant bill for a client meeting | Blocked |
| Restaurant's own food purchases for meals it sells | Not blocked (provided for consideration in the normal course of business) |
| Laptop at €1,160 or more | Capital good: input VAT recoverable now, adjustable over 5 years if use changes |
| Office furniture below €1,160 | Outside the capital goods scheme |
| Error of no more than 5% of the output tax (or input tax) declared | May be corrected in the VAT account and in the return for the period in which the error is discovered. That period must start no later than six months after the end of the period with the error |
| Larger error | Correct with the prescribed form (art. 28(1)); 10% penalty if done before a provisional assessment, otherwise 20% |
| Excess credit | Carry forward, or refund within 5 months of the later of due date and filing date |

## Worked cases

Hypothetical figures, for tax year 2026 periods.

**Case 1: deadline for a March quarter.** An Article 10 person's tax period is January to March 2026. The period ends in March; the second month after March is May, so the return and payment are due by 15 May 2026 ([art. 27(1) and art. 21(1)](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)). If the return is filed electronically by 22 May 2026, no late-filing penalty is due (art. 42(1)(d)), and no interest is due if the payment is made with it (art. 21(4A)).

**Case 2: a simple Article 10 return.** Malta sales of €10,000 at 18% give output tax of €1,800 ([Act, art. 19](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)). Purchases for the business of €2,000 at 18% give input tax of €360. A car lease invoice in the same period is blocked, so its VAT is left out. Payable: €1,800 minus €360 = €1,440.

**Case 3: an Article 11 consultant buys software from an Irish company.** The consultant is registered under Article 11. On 10 March 2026 an Irish supplier invoices €1,000 for a software subscription, with no VAT. The consultant receives a service on which it must pay the VAT under art. 20(2), so it must also register under Article 12 (art. 11(10), art. 12(3)) ([Act](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)). VAT due: €1,000 at 18% = €180, payable by 15 May 2026 (the 15th of the second month after March). It cannot deduct the €180, and it still charges no VAT on its own sales.

**Case 4: a late return.** An Article 10 return for January to March 2026 shows net tax of €5,000. It was due on 15 May 2026 but filed and paid on 20 July 2026: three months or part months late, so the seven-day relief does not apply ([art. 38(1) and art. 21(4)](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)). Penalty per month: the higher of 1% of €5,000 (€50) and €20, so €50. Three months: €150. On the Act's wording the proviso caps this at €250, so €150 stands. Interest ([S.L. 406.19](https://legislation.mt/getpdf/632835ddda6f862638d03ac1)): 0.6% of €5,000 = €30 a month, three months = €90.

**Case 5: leaving Article 11.** A shop registered under Article 11 had 2025 turnover of €31,000, so it qualified at the start of 2026 ([Act, Sixth Schedule](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)). Its 2026 turnover passes €35,000 on 10 September 2026. It stops qualifying on that date and must apply to cancel by 25 September 2026 (fifteen days, art. 11(5)(b)). If it applies, the cancellation takes effect on 1 October 2026 (art. 11(7)). Because it makes taxable supplies, it is registered under Article 10 from that same date (art. 10(6)(c), (7a)), and charges VAT on sales from then. If the Commissioner cancels under art. 11(8) instead, both dates are 10 September 2026. Missing the cancellation deadline costs the higher of 10% of the first period's net tax and €100 for each month or part month, capped at €500 (art. 40).

## When to refuse or refer

- Partial exemption: the business makes both deductible supplies and exempt-without-credit supplies (for example lettings, insurance, finance, medical or education) and the non-deductible share is more than €20 multiplied by the months in the period. The annual ratio needs a year-end calculation ([Act, Tenth Schedule items 6 and 9](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)).
- Capital goods adjustments: a change of use, sale or cessation within the 5-year or 20-year period.
- Margin schemes for second-hand goods, works of art, collectors' items and antiques, and travel agents.
- Several persons registered as a single taxable person (VAT group).
- A supplier not established in Malta, with or without a representative.
- Preparing an OSS or import-scheme return, or Article 11A and 11B cases.
- Immovable property transfers or developments, investment gold, new means of transport, excise goods, call-off stock.
- An assessment, provisional assessment, investigation or appeal to the Administrative Review Tribunal (thirty days from service to appeal).
- Anything the client cannot evidence with invoices.
- A request about Maltese income tax: this Guide covers VAT only.

## Filing and payment

### Due dates and penalties ([Act, arts 21, 27, 30, 37-42 and Sixth Schedule](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))

| Filing | Due | Late or wrong |
| --- | --- | --- |
| Article 10 return and payment | 15th of the second month after the month the period ends; filed electronically, no late-filing penalty up to seven days after, and no interest if paid with it | Late return: the higher of 1% of the net tax declared (before any credit brought forward) and €20, for each month or part month. Where the tax payable is less than €250, the penalty does not exceed that tax or €50, whichever is greater; on the Act's wording it does not exceed €250 in all other cases. The Act does not make clear whether "for every month" multiplies only the €20 limb or the 1% limb too; below the €250 cap the difference rarely matters |
| Incorrect Article 10 return | Correct by later return or form | 20% of the understated tax or overstated deductions; 10% if corrected under art. 28(1) before a provisional assessment; €150 flat for a person supplying only exempt-with-credit items, unless a higher penalty applies; 10% of the tax due if settled during an investigation and paid within one month of the agreement |
| Last return after Article 10 cancellation | Within thirty days of the cancellation notice | As above |
| Article 11 declaration | Calendar-year declaration by 15 February of the next year (15th of the second month after the period ends); a shorter period may be chosen. Filed electronically within seven days after the due date, no late penalty is due (art. 42(1)(d)) | €10 a month or part month, maximum €120 per declaration |
| Article 11A declaration | Last day of the month after each quarter | As for Article 11 |
| Article 12 VAT and notice of payment | 15th of the second month after the invoice date or month of receipt, whichever is earlier | 20% of understated or assessed tax; late notice €10 a month, maximum €120 |
| Recapitulative statement | See the table in the cross-border section | €50 a month or part month, maximum €600 per statement |
| Registration under Article 10 | Within thirty days of the first supply | The higher of 1% of the first period's net tax and €20 a month; capped at €250 if that net tax is €2,000 or less, otherwise at 20% of it |
| Registration under Article 12 | By the date of the acquisition or service | The higher of 1% of the VAT on those transactions and €20 a month; the same €250 or 20% caps around €2,000 |
| Notices of change (art. 13) | Within fifteen days of the change | €20 a month, maximum €250 per notice |
| Article 11 cancellation | Within fifteen days of ceasing to qualify | The higher of 10% of the first period's net tax and €100 a month, maximum €500 |

No administrative penalty is due where there is a reasonable excuse. Lack of funds, or relying on someone else, is not a reasonable excuse. The Commissioner may remit part of a penalty or, for a genuine mistake, all of it (art. 42).

### Interest ([S.L. 406.19](https://legislation.mt/getpdf/632835ddda6f862638d03ac1))

Unpaid VAT carries interest of 0.6% for each month or part month from the due date (Act, art. 21(4)). Balances that became payable before 1 September 2022 stay at 0.33%. The same rate is paid to the taxpayer on refunds paid late (art. 24(3)).

### Records ([Act, art. 48 and Eleventh Schedule](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20))

- Keep full records of every transaction for at least six years from the end of the year they relate to. For a late return or a correction, the six years run from the date of filing or of the correction request. For capital goods, they run from the end of the 5-year or 20-year adjustment period, and the list of capital goods is part of the records ([S.L. 406.12, regs 6-7](https://legislation.mt/getpdf/60225988bc8272018c0f72fb)).
- An Article 10 person keeps: proper accounts; a VAT account for each period that ties to every figure on the return; an annual VAT account; copies of invoices issued; all invoices received; customs documents; fiscal receipts issued; credit and debit notes; registers for goods sent to other Member States, goods received for work, and call-off stock.
- Store invoices in the form they were sent or received, paper or electronic. If stored electronically, MTCA must be able to access and download them online.
- An Article 11 or 11A person keeps: proper accounts, fiscal receipts issued, fiscal receipts and tax invoices received, credit and debit notes, and other documents given to customers.
- A person not registered under Article 10 keeps records of its intra-EU acquisitions and reverse-charge purchases.
- If records requested by written notice are not produced within thirty days without reasonable excuse, they cannot be relied on later in an assessment or appeal.

## Returns being filed now for 2025

The version of the Act in force from 1 January 2025 ([Act as at 1 January 2025](https://legislation.mt/getpdf/6811d40a495e132a18426aea)) already had the €35,000 domestic threshold, the €100,000 Union threshold, the 12-month bar on switching from Article 10, and the Article 11 declaration date (15th of the second month after the period ends). So the calendar-2025 Article 11 declaration was due by 15 February 2026. Late 2025 returns carry the penalties and the 0.6% interest shown above. Use the pre-2025 thresholds only for periods up to 31 December 2024; they were tested on a rolling twelve months, not a calendar year.

## Completion checklist

- Registration article, number and tax period confirmed from the certificate.
- Every sale placed in one of ([Act, Eighth Schedule](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)): 18%, 12%, 7%, 5%, exempt with credit, exempt without credit, outside the scope.
- Rates checked against the Eighth Schedule item (CN code for goods).
- Customer VAT numbers valid and on the invoice for every intra-EU supply of goods and B2B service.
- Reverse-charge purchases in both output and input tax (Article 10), or paid under Article 12.
- Blocked input VAT removed; private use apportioned; partial exemption referred if present.
- Capital goods of €1,160 or more, and all property, listed with the date of first use ([S.L. 406.12](https://legislation.mt/getpdf/60225988bc8272018c0f72fb)).
- Excess credit brought forward matches the last return and any refund or set-off.
- Errors from earlier periods: 5% rule applied, or the art. 28(1) form prepared ([Act, Eleventh Schedule item 4](https://legislation.mt/getpdf/6a7d667d73ff6d305c833d20)).
- Box numbers taken from the live MTCA return form.
- Return filed and paid by the 15th of the second month after the period (or within the seven-day electronic window).
- Recapitulative statement and OSS return filed where required.
- Credit notes and price reductions deducted in the period they occur; foreign-currency amounts converted at the Maltese bank selling rate or the ECB rate when the tax became chargeable.
- VAT account and supporting documents kept for at least six years (capital goods: six years from the end of the adjustment period, plus the capital goods list).

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
