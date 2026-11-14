---
name: sg-gst-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Singapore GST return (GST F5 form) for any client. Trigger on phrases like "prepare GST return", "do the GST", "fill in GST F5", "create the return", "Singapore GST", "IRAS filing", or any request involving Singapore GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill covers Singapore only and only standard GST-registered persons filing GST F5. Group registrations, partial exemption with non-de-minimis exempt supplies, Approved 3rd Party Logistics schemes, and Major Exporter Scheme applications are all in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any Singapore GST work.
jurisdiction: SG
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
version: 1.0
type: filing-howto
---

# Singapore GST: registration, GST F5, input tax and reverse charge v1.0 (2026)

Tax year 2026. The rules below are those published by the Inland Revenue Authority of Singapore (IRAS) read in the scoped official pages on 14 November 2026; historical periods and announced future phases remain explicitly dated. All amounts are Singapore dollars. Source: [IRAS GST pages](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns).

## Scope and who this is for

- Businesses that are, or may have to become, GST-registered in Singapore and file the quarterly GST F5 return, and the people preparing that return for them.
- Covers: the GST rate; compulsory and voluntary registration; standard-rated, zero-rated and exempt supplies; the GST F5 box by box; input tax conditions and blocked items; reverse charge on imported services and low-value goods; the overseas vendor registration (OVR) regime; the GST InvoiceNow Requirement; correcting errors; filing, payment and penalties.
- Does not cover in depth: GST group registration, the Major Exporter Scheme (MES) and other import GST suspension schemes, the Import GST Deferment Scheme, customer accounting for prescribed goods, the gross margin scheme, partial exemption apportionment beyond the de minimis test, the Tourist Refund Scheme and the final GST F8 return. These are listed under "When to refuse or refer".
- This skill explains how IRAS says the return works. It does not replace IRAS's e-Tax Guides where a case turns on detail.

## Ask the client first

- Are you GST-registered? If yes, since when, and was the registration compulsory or voluntary? (Voluntary registrants have a minimum registration period and, for newer registrations, InvoiceNow duties.)
- If not registered: what were your taxable supplies for each calendar year, and what do you expect over the next 12 months? Do you have signed contracts or purchase orders that point to a large increase?
- Which accounting period is this return for, and is it a quarterly or a special accounting period?
- Do you make any exempt supplies (interest income, residential rent or sale, financial services, digital payment tokens, investment precious metals)? Do you have non-business receipts such as donations or grants? This decides the de minimis test and whether you must reverse charge.
- Do you buy services from overseas suppliers or buy low-value goods from overseas? Get the invoices and check whether the supplier charged Singapore GST.
- Do you sell to overseas customers? For services, who is the contracting customer, where do they belong, and who directly benefits from the service? For goods, do you have export documents?
- Do you run an online marketplace or act as a redeliverer, or sell goods held overseas to Singapore consumers?
- Do you hold valid tax invoices for every input tax claim, and import permits in your name for imports?
- Any motor car, club, staff medical, family benefit or private expenses in the purchase ledger?
- Any errors found in past returns? For which periods, and what are the GST and value amounts involved?
- Are any returns or payments overdue? Have you received an estimated Notice of Assessment or penalty notice?
- Are you under GST group registration, MES, the Approved Third Party Logistics scheme, IGDS or any other special scheme?

## The method, step by step

1. **Confirm registration status and the period.** If the client is not registered, run the registration tests first (see "Registration"). If registered, confirm the accounting period and its due date.
2. **List every sale for the period** from the sales ledger and invoices, not the bank statement alone. Classify each as standard-rated (9%, [IRAS current GST rates](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates)), zero-rated (export of goods or an international service under section 21(3) of the GST Act), exempt, or out of scope.
3. **Handle the special sale items.** Deemed supplies (gifts costing more than the IRAS limit where input tax was claimed, business assets put to private use), sales of business assets, and credit or debit notes in the period.
4. **List every purchase and import.** For each, check the input tax conditions: tax invoice or import permit in the client's name, business purpose, attributable to taxable supplies, not a disallowed expense, supplier actually GST-registered.
5. **Take out blocked items** (motor cars, club subscriptions, most staff medical costs and medical or accident insurance, family benefits, betting) from both Box 5 and Box 7.
6. **Decide whether the client is a reverse charge business.** Only a business not entitled to full input tax credit (because it makes exempt supplies or has non-business receipts) reverse charges imported services and low-value goods. A fully taxable business does not.
7. **If the client makes exempt supplies, run the de minimis test.** If it is not met, input tax directly attributable to exempt supplies is not claimable and residual input tax must be apportioned; refer if needed.
8. **Fill Boxes 1 to 17** using the box table below. Track output tax and input tax from the invoices; do not recompute them from Box 1 or Box 5.
9. **Check prior-period errors.** Decide whether each can be adjusted in this return under the IRAS concession or needs a GST F7.
10. **File on myTax Portal and pay** by one month after the period end. File a nil return if there was no activity.
11. **For InvoiceNow-covered businesses**, make sure invoice data for the period has been transmitted by the earlier of the filing date and the filing due date.

## Rates, bands and thresholds

### GST rate ([IRAS current GST rates](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates))

| Period | Standard rate |
| --- | --- |
| From 1 Jan 2024 (current, all of 2026) | 9%  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates) |
| 1 Jan 2023 to 31 Dec 2023 | 8%  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates) |
| 1 Jul 2007 to 31 Dec 2022 | 7%  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates) |

- Zero-rated supplies are taxed at 0%. Exempt supplies carry no GST.
- A supply that straddles a rate change (for example a 2023 invoice for 2024 work) follows the IRAS rate-change rules; refer it rather than guess.

### Registration ([IRAS: Do I need to register for GST](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst))

| Test | Trigger (strictly "more than") | When to apply | Registered from |
| --- | --- | --- | --- |
| Retrospective view | Taxable turnover for the calendar year (1 Jan to 31 Dec) more than $1 million | 1 Jan to 30 Jan of the following year | 1 Mar of the following year  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| Prospective view, forecast date before 1 Jul 2025 | Taxable turnover expected to be more than $1 million in the next 12 months | Within 30 days after the date of the forecast | The 31st day after the forecast date  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| Prospective view, liability arising on or after 1 Jul 2025 | Same | Within 30 days after the date of the forecast (unchanged) | 2 months from the date of the forecast (two-month grace period to start charging GST)  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |

- **Taxable turnover** is standard-rated plus zero-rated supplies made in Singapore in the course of business, including low-value goods sold to non-registered customers in Singapore from 1 Jan 2023. It excludes exempt supplies, including financial services which are international services and thus zero-rated, out-of-scope supplies and sales of capital assets such as machinery, equipment, office buildings and furniture.
- **Exactly $1 million is not over the line.** Both views use "more than".
- **Prospective view needs evidence.** IRAS lists signed contracts, accepted quotations or confirmed purchase orders, fixed monthly fee invoices, or income statements showing the past 12 months already close to $1 million and rising.
- **Retrospective exception.** A business caught only by the retrospective view need not register if it is certain that taxable turnover for the next 12 months will not exceed $1 million because of specific circumstances (for example large-scale downsizing), and it keeps documentary evidence and a detailed computation. It must keep monitoring.
- **Mid-year crossing.** If turnover passes $1 million during the year but the prospective view does not apply, the business may wait for the year end and apply under the retrospective view in January, or register voluntarily.
- **Exemption from registration** may be applied for where taxable supplies are wholly or mainly zero-rated.
- **Reverse charge and OVR** can also create a registration liability (see below).

### Voluntary registration ([IRAS: Factors to consider before registering voluntarily](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/factors-to-consider-before-registering-voluntarily-for-gst))

- A business that is not liable may register voluntarily if it makes taxable supplies, makes only out-of-scope supplies, makes exempt financial services that are also international services, or procures imported services or low-value goods and would not be entitled to full input tax credit if registered. A business with firm intentions to start such transactions may also apply.
- Voluntarily registered businesses must remain registered for 2 years, and must meet the conditions IRAS imposes before and after registration (IRAS e-Tax Guide "GST: Conditions for GST Voluntary Registration").
- A voluntary registrant from 1 Apr 2026 falls under the GST InvoiceNow Requirement from the start (see "GST InvoiceNow Requirement").

### Filing and payment deadlines ([IRAS: Due dates and requests for extension](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/due-dates-and-requests-for-extension))

Both the return and the payment are due one month after the end of the accounting period. Returns are filed electronically on myTax Portal.

| Accounting period (2026) | Filing and payment due | Nominal GIRO date, subject to next-working-day rule |
| --- | --- | --- |
| Jan to Mar 2026 | 30 Apr 2026 | 15 May 2026  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/due-dates-and-requests-for-extension) |
| Apr to Jun 2026 | 31 Jul 2026 | Nominal 15 Aug 2026 is a Saturday; use the actual next-working-day deduction  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/due-dates-and-requests-for-extension) |
| Jul to Sep 2026 | 31 Oct 2026 | Nominal 15 Nov 2026 is a Sunday; use the actual next-working-day deduction  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/due-dates-and-requests-for-extension) |
| Oct to Dec 2026 | 31 Jan 2027 | 15 Feb 2027  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/due-dates-and-requests-for-extension) |

- GIRO is deducted on the 15th of the month after the payment due date, shifted to the next working day if a weekend/public holiday. Confirm the actual arrangement on the filing acknowledgement; the filing deadline itself does not become the GIRO date.
- Special accounting periods: due one month from the end date of the period.
- No extension is granted as a rule. IRAS may extend for a newly registered business's first return (up to one month) or for listed reasons such as a computer breakdown (up to two weeks); the request must reach IRAS at least 5 working days before the due date.
- A nil return is required when there was no activity.
- Refunds are normally processed within a period equal to the accounting period (quarterly: three months after receipt), subject to exceptions such as outstanding returns or audit review. GIRO/PayNow is the refund route; it is not an unconditional payment guarantee.

### The GST F5 box by box ([IRAS: Completing GST return](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns))

All values are in Singapore dollars and exclude GST. Track output tax (Box 6) and input tax (Box 7) from the invoices and import permits; IRAS says not to compute them by applying 9% to Box 1 or Box 5, because rounding differs.

| Box | What goes in | Notes |
| --- | --- | --- |
| 1 | Total value of standard-rated supplies | Sales at 9% net of GST (sell for $100 plus $9 GST: $100 here, $9 in Box 6). Includes deemed supplies, sales of business assets, and the value of imported services and low-value goods that you reverse charge. Deduct credit notes issued, discounts and returns.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 2 | Total value of zero-rated supplies | Exported goods (with export documents) and international services under section 21(3) of the GST Act.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 3 | Total value of exempt supplies | Residential sale or lease, Fourth Schedule financial services (including bank deposit interest), investment precious metals, digital payment tokens. For foreign-currency exchange, report the absolute net realised gain/loss. Qualifying DPT exchanges have their own consistently applied value-of-supply method; do not automatically use gross token turnover or assume a stablecoin/NFT is a DPT. See `singapore-crypto-tax`.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 4 | Total of Boxes 1 + 2 + 3 | Computed automatically.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 5 | Total value of taxable purchases | Standard-rated purchases and imports where the GST can be claimed, zero-rated purchases, and reverse-charged imported services and low-value goods. Exclude disallowed expenses, private purchases, exempt purchases, purchases from non-registered suppliers, wages.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 6 | Output tax due | GST charged on Box 1 supplies, GST on reverse charge, GST on customer-accounted supplies received, GST on debts recovered after bad debt relief.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 7 | Input tax and refunds claimed | Claimable GST on Box 5 purchases and imports; the claimable part of reverse charge GST; tourist refunds; bad debt relief; pre-registration GST (first return only). Deduct credit notes received and input tax repaid for suppliers unpaid after 12 months.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 8 | Net GST to pay or claim | Box 6 minus Box 7, computed automatically. Under $5 payable: no payment needed; under $5 refundable: no refund and nothing carried forward.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 9 | Value of goods imported under MES, A3PL or other approved schemes | Import GST suspended, so no input tax on those imports. Value also in Box 5.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 10 | Did you claim GST refunded to tourists? | Yes/No plus amount, if included in Box 7.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 11 | Bad debt relief and/or refund claims for reverse charge transactions? | Yes/No plus amount, if included in Box 7.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 12 | Pre-registration claims? | First return only.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 13 | Revenue | Main operating income from the accounts; best estimate allowed. An error only in Box 13 does not need a GST F7.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 14 | Imported services and/or low-value goods subject to reverse charge? | Reverse charge businesses only. The same value also goes in Box 1.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 15 | Electronic marketplace operator supplying remote services for third parties? | Marketplace operators only; same value also in Box 1.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 16 | Redeliverer or marketplace operator supplying imported low-value goods for third parties? | Same value also in Box 1.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 17 | Own supplies of imported low-value goods subject to GST? | Same value also in Box 1.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 18 to 21 | Import GST Deferment Scheme section | Only for IGDS-approved businesses.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |

### Supplies: standard-rated, zero-rated, exempt, out of scope ([IRAS: Supplies exempt from GST](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-is-gst-not-charged/supplies-exempt-from-gst); [IRAS: Providing international services](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services))

- **Standard-rated (9%):** every supply of goods or services in Singapore that is not zero-rated or exempt, including sales of business assets (furniture, equipment, commercial property), leases of commercial property and hotel rooms, and sales to staff.
- **Zero-rated exports of goods:** only where the goods are, or will be, exported at the time of supply and the business keeps the required export documents.
- **Zero-rated international services:** only if the service falls within section 21(3) of the GST Act. Not every service to an overseas customer qualifies. The general provision, section 21(3)(j), needs the service to be supplied under a contract with an overseas person and to directly benefit an overseas person who is outside Singapore when the services are performed, or a GST-registered person who belongs in Singapore; the service must not relate to land or goods in Singapore (other than goods for export). Other paragraphs cover transport, services performed wholly outside Singapore and prescribed consultancy services. Check the customer's belonging status: an individual’s usual residence controls, with Singapore address as a proxy. The published multiple-address overseas-study/work exception requires continuous absence of at least a year (temporary returns allowed), a fixed overseas place, and an overseas assignment not connected to Singapore employment. Obtain the evidence rather than using nationality.
- **Exempt:** most financial services under the Fourth Schedule (bank account charges, currency exchange, issuing or selling shares or bonds, loans, life policies), digital payment tokens (from 1 Jan 2020), sale and lease of residential property, and the import and local supply of investment precious metals. Arranging, broking or advising on financial transactions is not exempt: an insurance broker charges 9% on a commission for arranging a life policy for a local policyholder.
- **Out of scope:** for example goods sold from one overseas place to another without entering Singapore. Not reported in Boxes 1 to 3.

### Input tax: conditions ([IRAS: Conditions for claiming input tax](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax))

Input tax is claimable only when all of these are met:

1. The business is GST-registered.
2. The goods or services are supplied to, or imported by, the business.
3. They are used or will be used for the business.
4. Local purchases have a valid tax invoice addressed to the business, or a simplified tax invoice, when the claim is made. For purchases over $1,000 the invoice must show the words "tax invoice", the customer's name and the GST amount; for purchases of $1,000 or less it must show the GST amount or say the price includes GST. The supplier must actually be GST-registered.
5. Imports have an import permit showing the business as importer, plus supporting documents.
6. The input tax is directly attributable to taxable supplies, or to out-of-scope supplies that would be taxable if made in Singapore.
7. The claim is not disallowed under Regulations 26 and 27 of the GST (General) Regulations.
8. The business has taken reasonable steps to conclude that the goods or services were not part of a missing trader fraud arrangement.

- The usual claim period follows the invoice/import-permit date. If the business uses a permitted posting/processing-date basis, verify the applicable consistent-basis, document and no-double-claim conditions rather than moving claims opportunistically; that route is not fully reproduced here.
- If a GST-registered business is charged GST by an overseas vendor registered under the OVR pay-only regime on remote services or low-value goods, it should not claim that GST; it asks the vendor for a refund.
- Entertainment is not a blocked category. A simplified tax invoice normally works at no more than $1,000 including GST. For food/drink entertainment above $1,000, IRAS permits a receipt with all simplified-invoice details plus alternative payment evidence and entertainment particulars. This concession excludes non-food/drink components and does not apply to staff meals; use the applicable valid invoice and business-nexus conditions.

### Input tax: disallowed (blocked) expenses ([IRAS: Conditions for claiming input tax](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax))

| Expense | Rule | Exceptions IRAS publishes |
| --- | --- | --- |
| Club subscription fees, including joining and transfer fees, charged by sports and recreation clubs | Disallowed (Regulation 26) | Food/drink business entertainment is tested under the published entertainment conditions. The old blanket club-facility green/buggy/locker-fee claim remains unconfirmed below.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax) |
| Motor car purchase and running costs (cars registered in the business's or an individual's name, or hired) | Disallowed (Regulation 27) | Vehicles outside the "motor car" definition in Regulation 25(1) (lorries, vans, motorcycles; a motor car is built for not more than seven passengers excluding the driver and weighs not more than 3,000 kg unladen). From 1 Apr 2022, pay-per-trip chauffeured private hire car transport. From 1 Jan 2023, costs of a car used by a third party (for example a customer's parking). Cars used by a connected person only where the costs are recovered and the recovery is not ancillary to another supply. Claim only to extent recovered; the connected recipient remains blocked from claiming its recharged car tax. Specific car-service/fleet businesses have additional exceptions requiring their own evidence.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/common-scenarios---do-i-claim-gst/Motor-Vehicles-Expenses) |
| Medical expenses for staff | Disallowed (Regulation 26) | Obligatory under the Work Injury Compensation Act or a collective agreement under the Industrial Relations Act; or (for expenses on or after 1 Oct 2021) treatment linked to health risks of the work and incurred under Singapore written law; or COVID-19 treatment under a government advisory.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax) |
| Medical and accident insurance premiums for staff | Disallowed | Obligatory under the Work Injury Compensation Act or a collective agreement.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax) |
| Benefits for family members or relatives of staff (for example school fees of expatriates' children) | Disallowed (Regulation 26) | None published.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax) |
| Betting, sweepstakes, lotteries, fruit machines or games of chance | Disallowed | None published.  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax) |

Also not claimable: purely private purchases, and household costs of staff working from home.

### Exempt supplies and the de minimis rule ([IRAS: Claiming input tax incurred to make exempt supplies](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/claiming-input-tax-incurred-to-make-exempt-supplies))

- Input tax incurred in making exempt supplies is not claimable unless the De Minimis Rule is satisfied.
- The rule is satisfied when the value of exempt supplies is less than or equal to both: an average of $40,000 per month, and 5% of the total value of all taxable and exempt supplies in the period. Reverse-charged imports, customer-accounted supplies received and marketplace supplies made for underlying suppliers are left out of taxable supplies for this test.
- If satisfied, all input tax is claimable except blocked items, but only provisionally: a longer-period adjustment repeats the test.
- If not satisfied, input tax directly attributable to exempt supplies is not claimable, and residual input tax is apportioned under IRAS's formula. Refer this.

### Reverse charge: imported services and low-value goods ([IRAS: Local businesses importing services and low-value goods](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-and-digital-economy/local-businesses))

- **Who:** only a GST-registered business belonging in Singapore that is not entitled to full input tax credit because it makes exempt supplies or receives non-business receipts (an "RC business"). IRAS's examples: banks and financial institutions, investment-holding companies with dividend income, companies with substantial inter-company loan interest, residential or mixed-use developers, and charities providing free or subsidised services.
- **A business that makes only taxable supplies does not reverse charge** and leaves Box 14 blank. For an overseas supplier that correctly charges no Singapore GST under the applicable regime, there is no reverse-charge entry; do not infer the supplier’s GST treatment merely from its overseas address.
- **What:** from 1 Jan 2020, all services procured from overseas suppliers except those specifically excluded; from 1 Jan 2023, low-value goods bought from local or overseas suppliers, marketplaces or redeliverers, registered or not.
- **How:** account for GST as if you were the supplier: value in Box 1 and Box 14, GST in Box 6; the value in Box 5 and the claimable part of the GST in Box 7 under the normal recovery rules.
- **Unregistered businesses:** a business that would not get full input tax credit if registered must register when its taxable turnover and/or the total value of its imported services and low-value goods is more than $1 million over 12 months.
- **Unpaid overseas supplier:** if reverse charge was applied but the overseas supplier was not paid within 12 months of the due date, an adjustment may be claimed under conditions in the IRAS e-Tax Guide "GST: Reverse Charge" (flag in Box 11).

**Low-value goods** are goods that, at the point of sale, are not dutiable (or the duty is waived under section 11 of the Customs Act), are not exempt from GST, are outside Singapore and are delivered to Singapore by air or post, and are valued at not more than the import relief threshold of $400. A GST-registered local supplier must charge GST on its own direct sales of such goods to customers in Singapore who are not GST-registered; a non-registered local supplier counts those sales towards the $1 million registration threshold.

### Overseas vendor registration (OVR) ([IRAS: Overseas businesses supplying remote services and low-value goods](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-and-digital-economy/overseas-businesses))

- An overseas business must register for GST in Singapore when its annual global turnover exceeds $1 million and its business-to-consumer supplies of remote services and/or low-value goods to customers in Singapore exceed $100,000 a year. It registers under a simplified pay-only regime.
- Remote services are services the customer need not be physically present to receive.
- Overseas marketplace operators and redeliverers may be treated as the supplier of low-value goods and remote services sold through them, and count those supplies towards the thresholds.
- OVR vendors charge GST only on business-to-consumer supplies. A GST-registered Singapore business should not be charged GST by them; if it is, it asks the vendor for a refund rather than claiming input tax (see input tax condition 4).

### GST InvoiceNow Requirement ([IRAS: GST InvoiceNow Requirement](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-invoicenow-requirement))

GST-registered businesses must submit invoice data to IRAS through InvoiceNow (the Peppol-based network) using an InvoiceNow-Ready Solution. IRAS publishes this phased timetable:

| From | Who |
| --- | --- |
| 1 Nov 2025 | Companies that register for GST voluntarily within 6 months of their incorporation date  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-invoicenow-requirement) |
| 1 Apr 2026 | Businesses that apply for voluntary GST registration on or after 1 Apr 2026, whatever their incorporation date or structure  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-invoicenow-requirement) |
| 1 Apr 2028 | Businesses applying for compulsory registration on or after 1 Apr 2028; existing registrants with total annual supplies of S$200,000 or less  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-invoicenow-requirement) |
| 1 Apr 2029 | Existing registrants with total annual supplies of S$1,000,000 or less  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-invoicenow-requirement) |
| 1 Apr 2030 | Existing registrants with total annual supplies of S$4,000,000 or less  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-invoicenow-requirement) |
| 1 Apr 2031 | Existing registrants with total annual supplies above S$4,000,000  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-invoicenow-requirement) |

- "Total annual supplies" means Box 4 totals for accounting periods ending in calendar year 2025. IRAS has notified businesses registered before 2026 of their implementation dates and provides an implementation date calculator; rely on the notification.
- Excluded: overseas entities (including OVR vendors) and businesses registered only because of reverse charge.
- Data covers standard-rated and zero-rated supplies and purchases and exempt supplies. Not needed for deemed supplies, reverse charge transactions, exempt financial services and digital payment token exchanges or loans, and import permits.
- Due: by the earlier of the date the relevant GST return is filed and that return's filing due date.
- InvoiceNow does not replace the GST F5: returns must still be accurate and records kept for at least 5 years.

### Deemed supplies and other output tax items ([IRAS: Completing GST return](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns))

- Gifts of goods: output tax is due on a gift that costs more than $200 where input tax on it was claimed (including gifts to staff). IRAS's input tax page says the value is the open market value.
- Business assets put to private use, and free use of business premises by a third party, are deemed supplies in Box 1.
- Sales of business assets (office furniture, equipment, machinery, commercial property) are standard-rated even though they are not trading stock.
- On cancellation (GST F8), business assets held on the last day of registration are taxed if their total value exceeds $10,000 and input tax was allowed.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Taxable turnover for the calendar year exactly $1 million | Not liable under the retrospective view ("more than") | [IRAS registration](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst) |
| Sale of a used machine or office building | Excluded from taxable turnover for registration, but standard-rated in Box 1 once registered | [IRAS registration](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst); [Box 1](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| Services to an overseas company whose staff receive the benefit in Singapore | Fails section 21(3)(j), which needs the direct beneficiary to be outside Singapore (or GST-registered in Singapore). Check the prescribed services under section 21(3)(k), where the overseas customer may be in Singapore; otherwise standard-rated. Refer if unsure | [IRAS international services](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services) |
| Customer with a Singapore residential address | Singapore proxy, subject to the published usual-residence/multiple-address overseas-study or work conditions, not an absolute nationality rule | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services) |
| Goods sold with no export documents | Standard-rated, not zero-rated | [IRAS completing returns](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| Exempt supplies averaging exactly $40,000 a month and not more than 5% of total supplies | De minimis met ("less than or equal to") | [IRAS de minimis](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/claiming-input-tax-incurred-to-make-exempt-supplies) |
| Fully taxable business buys software from a US supplier with no Singapore GST | No reverse charge, no Box 14 | [IRAS completing returns](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| Club food/drink versus other facility charges | Test actual food/drink under entertainment conditions; membership itself is blocked. Do not claim green/buggy/locker fees from the old blanket statement pending confirmation | [IRAS input tax](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax) |
| Petrol for a van or lorry | Claimable (not a "motor car") | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/common-scenarios---do-i-claim-gst/Motor-Vehicles-Expenses) |
| Airport limousine paid per trip | Claimable from 1 Apr 2022 with a valid invoice | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax) |
| Ordinary purchase over $1,000 without customer name | Obtain a valid reissued invoice before claiming; test the separate food/drink entertainment concession where actually applicable, not for staff meals | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax) |
| Supplier not paid within 12 months of the payment due date | Repay the input tax claimed (deduct in Box 5 and Box 7) | [IRAS completing returns](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| Net GST payable under $5 | No payment; not carried forward | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| Error only in Box 13 (revenue) | No GST F7 needed | [IRAS GST F7](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/correcting-errors-made-in-gst-return-%28filing-gst-f7%29) |
| Error with net GST exactly $3,000 and value errors within 5% of Box 4 | Concession available ("not more than") | [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/correcting-errors-made-in-gst-return-%28filing-gst-f7%29) |

## Worked cases

Amounts in cases 1 to 5 are hypothetical. Cases 6 and 7 are IRAS's own published examples.

### Case 1: retrospective registration ([IRAS registration](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst))

A trading company made standard-rated and zero-rated sales of $1,050,000 in calendar year 2025 and also sold a used delivery machine for $150,000. It does not expect more than $1 million of taxable supplies in the next 12 months, but has no specified circumstance to show a drop.

- Taxable turnover is $1,050,000: the machine is a capital asset and is excluded.
- $1,050,000 is more than $1 million, so the company is liable under the retrospective view. It must apply between 1 Jan and 30 Jan 2026 and is registered from 1 Mar 2026. Its first GST F5 is due one month after the end of the first accounting period IRAS assigns, and may carry pre-registration input tax claims (Box 12).
- Had taxable turnover been exactly $1,000,000, there would be no liability under the retrospective view.

### Case 2: prospective registration after 1 Jul 2025 ([IRAS registration](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst))

On 15 Aug 2026 a consultancy signs a 12-month contract worth $1,200,000.

- Its taxable turnover is expected to be more than $1 million in the next 12 months, so it is liable under the prospective view on 15 Aug 2026.
- It must apply within 30 days after that forecast date, that is by 14 Sep 2026.
- Because the liability arises after 1 Jul 2025, it is registered 2 months from the forecast date and starts charging GST then. Use the effective date IRAS confirms.
- Keep the signed contract as the supporting document.

### Case 3: a quarterly GST F5 for Jul to Sep 2026 ([IRAS completing returns](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns))

A Singapore distributor (confirmed entitled to full input recovery and not an RC business) has, for 1 Jul to 30 Sep 2026:

- Local sales $200,000 plus GST $18,000 (per invoices).
- Exports $50,000 with export permits and bills of lading.
- Fixed deposit interest $400.
- Local stock and overhead purchases $80,000 plus GST $7,200, all with valid tax invoices.
- Golf club annual subscription $3,000 plus GST $270, and petrol for a company saloon car $500 plus GST $45.
- A $1,000 project-management subscription from a US supplier that charged no Singapore GST.

Working:

- De minimis: exempt supplies of $400 for the quarter are far below an average of $40,000 a month and below 5% of total supplies of $250,400, so the rule is met.
- The club subscription and car petrol are blocked: they stay out of Box 5 and Box 7.
- The US subscription is not reverse charged because the assumed distributor is entitled to full input recovery, including the satisfied de minimis test; it is not on IRAS's list of Box 5 taxable purchases.

| Box | Amount |
| --- | --- |
| 1 | $200,000  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 2 | $50,000  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 3 | $400  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 4 | $250,400  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 5 | $80,000  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 6 | $18,000  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 7 | $7,200  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 8 | $10,800 payable by 31 Oct 2026  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |
| 14 | Not applicable  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns) |

### Case 4: reverse charge for a partially exempt business ([IRAS reverse charge for local businesses](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-and-digital-economy/local-businesses))

An investment-holding company that receives dividend income is GST-registered and is not entitled to full input tax credit. In the Jul to Sep 2026 quarter it buys $10,000 of consulting services from a US firm that charges no Singapore GST.

- It must reverse charge: $10,000 in Box 1 and Box 14 and in Box 5; GST of $900 (9% of $10,000) in Box 6.
- Only the part of the $900 allowed by its input tax recovery rules goes in Box 7. That fraction depends on its apportionment and is not computed here; refer if it has not been agreed.
- Contrast case 3: a fully taxable business buying the same service does nothing under reverse charge.

### Case 5: correcting an error ([IRAS GST F7](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/correcting-errors-made-in-gst-return-%28filing-gst-f7%29))

In July 2026 a business finds that its Jan to Mar 2026 return (Box 4 total supplies $500,000) left out a standard-rated sale of $20,000 plus GST $1,800.

- Net GST in error is $1,800, not more than $3,000.
- The value error in the other boxes is $20,000, not more than 5% of $500,000 ($25,000).
- Both criteria are met, so it may adjust in its next GST F5 (Apr to Jun 2026, due 31 Jul 2026) instead of filing a GST F7.
- If the omitted sale had been $40,000 plus GST $3,600, neither test would be met and a GST F7 would be needed. Filed within 1 year of the original filing deadline and meeting the Voluntary Disclosure Programme conditions, no late payment penalty is imposed on the additional GST disclosed.

### Case 6: IRAS's de minimis example ([IRAS de minimis](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/claiming-input-tax-incurred-to-make-exempt-supplies))

For a quarter IRAS takes standard-rated supplies of $2,080,000, zero-rated supplies of $300,000 and exempt supplies of $120,000, total $2,500,000.

- Average exempt supplies: $120,000 ÷ 3 = $40,000 a month, not more than $40,000.
- Exempt share: $120,000 ÷ $2,500,000 = 4.8%, not more than 5%.
- The rule is met; all input tax for exempt supplies is provisionally claimable, subject to the longer-period adjustment.

### Case 7: IRAS's late payment example ([IRAS late payment](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-payments-refunds/late-payment-or-non-payment-of-gst))

A business filed its return for the period ending 30 Jun 2025 on time (due 31 Jul 2025) but did not pay GST of $10,000. IRAS issued its penalty notice on 5 Aug 2025; payment was made on 16 Dec 2025.

- 5% late payment penalty: $500.
- The tax stayed unpaid 60 days after the penalty, so 2% a month applied for Aug, Sep, Oct and Nov 2025: $10,000 × 2% × 4 = $800.
- Total penalties: $1,300.

### Case 8: late filing ([IRAS late filing](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/late-filing-or-non-filing-of-GST-returns-f5-f8))

A return stays outstanding for 3 completed months after its due date.

- $200 immediately, plus $200 for each of the 3 completed months: $800 in total, on top of the 5% late payment penalty on any estimated assessment.
- The late submission penalty for one return is capped at $10,000.


```oa-check
name: GSTF5 quarterly tax from supported invoice amounts
inputs:
  standard_sales: 200000
  exports: 50000
  exempt_interest: 400
  output_tax_invoices: 18000
  claimable_input_tax_invoices: 7200
  blocked_club_tax: 270
  blocked_car_tax: 45
steps:
  - total_supplies: standard_sales + exports + exempt_interest
  - exempt_monthly_average: exempt_interest / 3
  - exempt_share_percent: exempt_interest * 100 / total_supplies
  - blocked_tax_excluded: blocked_club_tax + blocked_car_tax
  - net_payable: output_tax_invoices - claimable_input_tax_invoices
expected:
  total_supplies: 250400
  exempt_monthly_average: 133.33333333333334
  blocked_tax_excluded: 315
  net_payable: 10800
```

Do not infer Box 6/7 by re-grossing boxes1/5; the inputs above are actual hypothetical invoice GST. The exempt share is below 5% and average below40,000, assuming no excluded denominator items or unresolved longer-period adjustment.

```oa-check
name: De minimis boundary and late penalties remain different computations
inputs:
  standard_sales: 2080000
  zero_rated_sales: 300000
  exempt_supplies: 120000
  unpaid_gst: 10000
  additional_penalty_months: 4
steps:
  - total_supplies: standard_sales + zero_rated_sales + exempt_supplies
  - monthly_exempt: exempt_supplies / 3
  - exempt_percent: exempt_supplies * 100 / total_supplies
  - initial_penalty: unpaid_gst * 0.05
  - additional_penalty: min(unpaid_gst * 0.02 * additional_penalty_months, unpaid_gst * 0.50)
  - total_penalty: initial_penalty + additional_penalty
expected:
  total_supplies: 2500000
  monthly_exempt: 40000
  exempt_percent: 4.8
  initial_penalty: 500
  additional_penalty: 800
  total_penalty: 1300
```

The penalty month count reproduces the published 2025 case only: the source specifies a 5 August penalty notice and 16 December payment, with the additional monthly charge after the 60-day trigger counted back to when the tax became payable. It is not the individual income-tax penalty clock.

## When to refuse or refer

- GST group or divisional registration: intra-group supplies and consolidation are outside this skill.
- Major Exporter Scheme, Approved Third Party Logistics scheme, licensed or zero GST warehouses, or the Import GST Deferment Scheme (Boxes 9 and 18 to 21).
- Customer accounting for prescribed goods, the gross margin scheme or the discounted sale price scheme for used vehicles.
- The de minimis rule is not met, or the longer-period adjustment is due: apportionment of residual input tax needs the IRAS formula and the e-Tax Guide "GST: Partial Exemption and Input Tax Recovery".
- An RC business whose input tax recovery fraction has not been worked out.
- Electronic marketplace operators, redeliverers and OVR vendors (Boxes 15 to 17).
- Zero-rating of services where the customer's belonging status or the direct beneficiary is unclear, or where the service relates to land or goods in Singapore.
- Supplies that straddle the 2023 or 2024 rate changes.
- Errors that need a GST F7 and may involve penalties, an estimated Notice of Assessment, a Notice to Attend Court, or suspected fraud.
- The GST F8 on cancellation, and the Tourist Refund Scheme.
- Any request to backdate an invoice, zero-rate without documents, or claim input tax without a valid tax invoice: refuse.

## Filing and payment

### Filing the GST F5 ([IRAS: Due dates](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/due-dates-and-requests-for-extension); [IRAS: Late filing](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/late-filing-or-non-filing-of-GST-returns-f5-f8))

- In authorised myTax Portal access choose GST → File GST Return/Edit Past Return, select the actual period and F5, reconcile boxes and declarations, then submit and retain the acknowledgement. Check payment/GIRO status and retain settlement evidence. Preparation is not submission. File by one month after the period end and pay by the same date unless an actual approved GIRO/extension arrangement applies. See the 2026 due-date table above.
- A nil return is needed for a period with no activity. A business that has ceased should apply to cancel its registration.
- Failing to file on time is an offence. IRAS may issue an estimated Notice of Assessment with a 5% late payment penalty on the estimated tax, impose a late submission penalty, and summon the business or the people running it. The estimate is revised when the actual return is filed; it can only be revised if the return is filed within 5 years of the period end.

### Correcting errors ([IRAS: Correcting errors (GST F7)](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/correcting-errors-made-in-gst-return-%28filing-gst-f7%29))

- **Administrative concession:** errors may be adjusted in the next GST F5 only if both criteria are met: (a) the net GST amount in error for all affected periods is not more than $3,000 (additional Box 6 output tax less additional Box 7 input tax); and (b) for each affected period, the total error in all boxes other than Boxes 6, 7 and 12 is not more than 5% of that period's Box 4 (or Box 5 if there were no supplies). Errors in Box 12 cannot use the concession. IRAS offers a GST F7 calculator to test this.
- **Otherwise file a GST F7** on myTax Portal. Under GST → File GST Return/Edit Past Return choose Request for GST F7, enter the actual period, then file within 14 days of requesting (or the auditor’s stated deadline), entering the full revised figures for every box; it supersedes the earlier return. Keep the error description and acknowledgement/payment instructions; non-GIRO payment uses the actual payment slip number, while GIRO follows the notified deduction. Errors across several periods in one year may be consolidated into the F7 for the last period of that year.
- **Time limits:** errors must be corrected within five years from the end of the accounting period; refund claims for GST overpaid must also be made within five years. Corrections made more than one year after the end of the period may attract penalties.
- **Voluntary disclosure:** IRAS may reduce penalties for disclosures that meet the Voluntary Disclosure Programme conditions. A GST F7 filed within 1 year from the original filing deadline that meets those conditions carries no late payment penalty on the additional GST.
- **Incorrect returns:** penalties of up to 200% of the tax undercharged, plus a fine and imprisonment; fraud is dealt with more severely.

### Penalties ([IRAS: Late payment](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-payments-refunds/late-payment-or-non-payment-of-gst); [IRAS: Late filing](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/late-filing-or-non-filing-of-GST-returns-f5-f8))

| Failure | Penalty |
| --- | --- |
| Return filed on time, GST not paid by the due date | 5% late payment penalty on the tax declared  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-payments-refunds/late-payment-or-non-payment-of-gst) |
| Return not filed or filed late | 5% late payment penalty on IRAS's estimated tax, revised to the actual liability once filed  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-payments-refunds/late-payment-or-non-payment-of-gst) |
| GST F7 filed more than 1 year after the original due date | 5% late payment penalty on the additional tax  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-payments-refunds/late-payment-or-non-payment-of-gst) |
| Tax still unpaid 60 days after the 5% penalty | Additional 2% for each month the tax remains unpaid, capped at 50% of the unpaid tax  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-payments-refunds/late-payment-or-non-payment-of-gst) |
| Return not filed by the due date | $200 immediately, then $200 for every completed month it remains outstanding, capped at $10,000 per return  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-payments-refunds/late-payment-or-non-payment-of-gst) |
| Incorrect return | Up to 200% of the tax undercharged, plus possible fine and imprisonment  [Official source](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-payments-refunds/late-payment-or-non-payment-of-gst) |

- IRAS can also appoint agents such as banks, tenants or lawyers to recover overdue GST, issue Travel Restriction Orders to sole proprietors or partners, and take legal action.
- Penalty waivers are requested through the Appeal Penalty Waiver service on myTax Portal. For a late submission penalty IRAS considers an appeal only if all outstanding returns have been filed, all overdue GST has been paid, and returns have been filed on time for the past year.
- Paying the late submission penalty does not end the obligation: the outstanding return must still be filed.

## Returns being filed now for 2025

### 2025 periods ([IRAS current GST rates](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates); [IRAS: Due dates](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/due-dates-and-requests-for-extension))

- Periods in 2025 were taxed at 9%, with the same boxes, deadlines and penalties as above. The Oct to Dec 2025 return was due by 31 Jan 2026.
- The GST InvoiceNow Requirement applied during 2025 only from 1 Nov 2025, and only to companies registering voluntarily within 6 months of incorporation.
- Prospective registrations with a forecast date before 1 Jul 2025 were effective on the 31st day after the forecast date; from 1 Jul 2025 the two-month rule applies.
- Errors in 2025 returns can be corrected until five years after the end of each period; the concession tests above apply.

## Completion checklist

- [ ] Registration status and accounting period confirmed; for unregistered clients, both the retrospective and prospective tests run with "more than" [IRAS registration](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst).
- [ ] Every sale classified as standard-rated, zero-rated (with export documents or a section 21(3) basis), exempt or out of scope.
- [ ] Deemed supplies, asset sales and credit notes included.
- [ ] Every input tax claim backed by a valid tax invoice or import permit in the client's name, for business use, in the right period.
- [ ] Blocked items (club subscriptions, motor cars, staff medical costs and insurance, family benefits, betting) removed from Boxes 5 and 7.
- [ ] Reverse charge applied only if the client is an RC business, with the value in Boxes 1, 5 and 14.
- [ ] De minimis test run if there are any exempt supplies, including exchange differences and interest in Box 3.
- [ ] Boxes 1 to 17 completed; Box 6 and Box 7 taken from invoices, not recomputed.
- [ ] Prior-period errors tested against both concession criteria; GST F7 prepared where needed.
- [ ] Return filed and GST paid by one month after the period end; nil return filed if no activity.
- [ ] InvoiceNow data transmitted where the business is in scope [IRAS InvoiceNow](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-invoicenow-requirement).
- [ ] Records kept for at least 5 years.

## Sources

| Source and scope read | Official URL | Read on |
|---|---|---|
| Read for complete F5 box descriptions1-21, tax versus value reporting, deemed supplies, input repayment and common errors. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns | 2026-11-14 |
| Read for current nine-percent and dated historical standard rates. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/basics-of-gst/current-gst-rates | 2026-11-14 |
| Read for calendar-year retrospective, supported prospective forecast, two-month commencement, exclusions and exceptions; aggregate sole-proprietor turnover. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/do-i-need-to-register-for-gst | 2026-11-14 |
| Read for voluntary eligibility, two-year minimum, supplier/customer economics and continuing conditions. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-registration-deregistration/factors-to-consider-before-registering-voluntarily-for-gst | 2026-11-14 |
| Read for one-month return/payment, nil returns, GIRO next-working-day rule, extension reasons and conditional refund processing. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/due-dates-and-requests-for-extension | 2026-11-14 |
| Read for financial services/DPT, residential and IPM boundaries, reporting and arranging-fee distinction. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-is-gst-not-charged/supplies-exempt-from-gst | 2026-11-14 |
| Read for general international-service boundary, s21(3)(j)/(k), relevant transport/overseas-service examples and individual/business belonging including multiple-address exception. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services | 2026-11-14 |
| Read for eight input conditions, blocked categories, invoices, new food/drink entertainment concession and no duplicate import claim. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax | 2026-11-14 |
| Read for both inclusive de minimis limbs, excluded denominators, longer-period adjustment and published example. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/claiming-input-tax-incurred-to-make-exempt-supplies | 2026-11-14 |
| Read for RC eligibility and unregistered threshold wording, low-value goods, OVR purchaser refund and marketplace/redeliverer boundaries. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-and-digital-economy/local-businesses | 2026-11-14 |
| Read for OVR thresholds, pay-only/no-input-credit, B2C and marketplace/consumer belonging. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-and-digital-economy/overseas-businesses | 2026-11-14 |
| Read for current phase table,2025 total-supplies measure, exclusions, transaction scope and earlier-of transmission deadline. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-invoicenow-requirement | 2026-11-14 |
| Read for F7/concession tests, five-year limits, complete revised boxes, request/14-day/payment process and conditional disclosure relief. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/correcting-errors-made-in-gst-return-%28filing-gst-f7%29 | 2026-11-14 |
| Read for late-payment rates/trigger, published four-month2025 example, approved GIRO, collection and waiver. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-payments-refunds/late-payment-or-non-payment-of-gst | 2026-11-14 |
| Read for late-submission200/10,000, estimated assessments, five-year correction and court/waiver conditions. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/late-filing-or-non-filing-of-GST-returns-f5-f8 | 2026-11-14 |

| Read for motor-car definition, blocked business use, third-party and connected-person exceptions, pay-per-trip and special vehicle-business distinctions. | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/common-scenarios---do-i-claim-gst/Motor-Vehicles-Expenses | 2026-11-14 |

Not yet confirmed: old blanket green/buggy/locker club-facility input recovery;  client-specific registration/return/GIRO dates and extension approval, actual export/customer-belonging evidence, any special-scheme permission, residual input recovery and longer-period adjustment, permitted posting-date claim conditions, and detailed F8/TRS procedures remain the stated hold/referral matters. No fresh statutory article-by-article read is claimed; the legislation references above are those in the scoped authority guidance. Historic2025 examples remain explicitly historical, and future InvoiceNow phases are announced dates, not evidence that every current business is already covered.
