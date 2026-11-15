---
name: norway-mva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Norway MVA return (MVA-melding) for any client. Trigger on phrases like "prepare MVA return", "Norwegian VAT", "MVA-melding", "merverdiavgift", or any request involving Norway VAT filing. Norway is NOT an EU member but IS in the EEA. There are NO intra-community supplies. All goods from EU are imports. ALWAYS read this skill before touching any Norway MVA work.
version: 2.1
jurisdiction: "NO"
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Norway VAT return: registration to reconciliation

## Scope

Figures are for income year 2026. Sources below state the provisions actually reopened on 15 November 2026. This skill is for an ordinary business registered in Norway’s VAT Register. It covers registration, classification control, input-VAT deduction limits, return preparation, payment and evidence. It does not decide a transaction’s place of supply, a zero-rate/exemption provision, partial deduction, joint registration, VAT compensation, VOEC, customs duty or a foreign-business refund.


## Ask the client first

- What is the entity’s registration effective date, settlement period, current Altinn access package and named authorised submitter?
- What is the rolling 12-month taxable-sales total, excluding VAT, and which invoices make it up? Is the entity a charitable or non-profit organisation (NOK 140,000 limit)?
- For each unusual sale, what was supplied, where, to whom and under which rate/zero/exemption provision? Is any food sold as part of a serving service?
- Are there imported goods, customs declarations and shipping dates that differ from invoice dates?
- Are there services bought from abroad, Svalbard or Jan Mayen, and what establishes buyer connection, service type and place of supply?
- Are there restaurant or catering bills, entertainment of business contacts, gifts or promotional items, staff food or benefits, art, staff housing or holiday property, or passenger-car costs? Their input VAT is barred unless an exception applies.
- Is any input used for exempt, private or mixed activity, or paid in cash at NOK 10,000 or more?
- Does the enterprise seek an annual small-enterprise period? Confirm calendar-year taxable supplies and withdrawals are no more than NOK 1,000,000 excluding VAT, at least 12 months’ VAT registration, timely prior returns/payments, the 10 December–1 February application window and actual approval.


## The method, step by step

### Rates, threshold and annual-period figures

| Item | Current published figure | Use | Source |
| --- | --- | --- | --- |
| Registration threshold | Taxable sales and withdrawals **exceeding** NOK 50,000, excluding VAT, in any 12-month period | Registration is required once the limit has been exceeded, not when it is reached. Only VAT-able turnover counts. | [Registration](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/) and [VAT Act § 2-1](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*) |
| Registration threshold, charitable and non-profit organisations | NOK 140,000 excluding VAT | Use instead of NOK 50,000 only for charitable and non-profit institutions and organisations. | [Registration](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/) |
| Registration threshold, tickets to sporting events | NOK 3,000,000 (in words on the page) | Applies to sales of the right to attend sporting events; the two top men’s football divisions and the top men’s ice hockey division use the ordinary limit. | [VAT Act § 2-1](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*) |
| Normal VAT rate | 25% | Use only after confirming normal-rated Norwegian treatment. | [Rates](https://www.skatteetaten.no/en/rates/value-added-tax/) |
| Reduced rate: foodstuffs, water and wastewater | 15% | Foodstuffs sold as part of a serving (restaurant/catering) service are charged at 25%, not 15%. Medicines, tobacco, alcoholic drinks and water from waterworks are not foodstuffs (water from waterworks is still 15%, under the separate water and wastewater rate). | [Rates](https://www.skatteetaten.no/en/rates/value-added-tax/) and [VAT Act § 5-2](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*) |
| Reduced rate: passenger transport, accommodation and listed admissions | 12% | Passenger transport, accommodation (letting of rooms), public broadcasting, and entry to cinemas, sporting events, amusement parks and activity centres. | [Rates](https://www.skatteetaten.no/en/rates/value-added-tax/) |
| Cash-payment rule | NOK 10,000 | A cost paid in cash of NOK 10,000 or more gives no deduction for the expense or its input VAT. Instalments of one purchase are added together. | [Cash purchases](https://www.skatteetaten.no/en/business-and-organisation/start-and-run/best-practices-accounting-and-cash-register-systems/best-practices-for-daily-operations/expenses/) |
| Non-registered foreign-service route | quarterly VAT basis **exceeding** NOK 2,000 | Apply only after the remotely-deliverable-service conditions are met; use the reverse-tax-liability return. At NOK 2,000 or less in the quarter there is no reporting/payment obligation under § 11-3(1); the English rate page says “at least”, but the statute says “overstiger” and controls. | [VAT Act § 11-3(1)](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*) |
| Ordinary two-month return and payment deadlines | 10 April; 10 June; 31 August; 10 October; 10 December; 10 February | Nominal dates derived from the statutory periods and filing rule; payment has the same deadline. A Saturday/holiday moves to the following working day under the cited day-count rules. | [Tax Administration Regulation §§ 8-3-1, 8-3-10](https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/*); [Tax Administration Act § 5-5](https://lovdata.no/dokument/NL/lov/2016-05-27-14); [Courts Act § 149](https://lovdata.no/lov/1915-08-13-5/§149); [Tax Payment Act §§ 10-2, 10-30](https://lovdata.no/dokument/NL/lov/2005-06-17-67) |
| Annual small-enterprise cap | NOK 1,000,000 (in words on the statute page) excluding VAT | Application route only: taxable supplies and withdrawals in the calendar year must not exceed the cap, the business must have been registered for at least 12 months, and prior returns and payments must have been on time. | [Annual route](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/paying-vat/) |
| Annual filing deadlines | 10 March (approved small enterprises); 10 April (agriculture, forestry, reindeer husbandry, fishing and other primary industry) | Primary industry must file annually whatever its turnover; the NOK 1,000,000 (in words on the statute page) cap does not apply to it. | [Annual route](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/paying-vat/) |
| Primary-industry other VATable revenue notice | more than NOK 30,000 | A primary-industry business with other VATable revenue of more than NOK 30,000 must tell Skatteetaten. | [Annual route](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/paying-vat/) |

The ordinary registration test is VAT Act § 2-1; the annual-period conditions are Tax Administration Regulation §§ 8-3-3 to 8-3-7. [VAT Act](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*); [filing regulation](https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/*). A rate table supplies examples, not a legal classification for every supply.


1. **Confirm entity, period and authority.** Record the organisation number, VAT registration effective date, settlement period, prior return and the person preparing the return. Access to complete a return is different from authority to submit it. To complete and submit, the person needs the Altinn access package "Value added tax" or "Accountant with signing rights". "Auditor in charge", "Assistant auditor" and "Accountant without signing rights" can complete the return but not submit it. The older Altinn II roles (for example limited signing rights, or a NUF contact person) work only until 31 December 2026; from 1 January 2027 only the correct access package gives access. [VAT return access](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/)
2. **Test registration and retain the transition evidence.** Maintain a rolling 12-month schedule of taxable sales and withdrawals, excluding VAT, and exclude exempt turnover. Registration is required once the total has exceeded NOK 50,000 (NOK 140,000 for a charitable or non-profit organisation). The business cannot charge VAT on invoices until registration has been approved. After registration, the sale that took turnover over the limit must be invoiced with VAT; if that invoice was issued before registration, issue a credit invoice without VAT and a new invoice with VAT rather than adding VAT informally. Late registration makes interest accrue on the VAT that should have been paid for the earlier periods and can lead to additional tax, and the missed returns must be filed as soon as possible. Once registered, the business may claim input VAT on purchases acquired up to 3 years before registration to the extent directly linked to its registered turnover, excluding goods/services already sold before registration; claim within 3 years after registration. The capital-property exception is outside this ordinary method. Keep the receipts. [VAT Act § 8-6](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*). Pre-registration is possible before the limit is reached in two cases: documented start-up purchases subject to VAT of at least NOK 250,000, with at least 4 months (in words on the statute page) expected from application before the limit is reached; the purchases must be intended for use in the enterprise, the activity must be a business, and normal-operation turnover must very probably be significantly above the limit (Skatteetaten often asks for a budget); if the business does not perform as expected, the VAT refunded must be paid back; or where taxable turnover will exceed the limit within 3 weeks after it commences (week count in words on the statute page). The significant-purchase amount includes VAT; the timing wording follows [VAT Regulation § 2-4-1](https://lovdata.no/dokument/SF/forskrift/2009-12-15-1540/*), which excludes a period of less than 4 months, rather than the English guidance’s “more than 4 months”. For a registration application, first confirm the enterprise is in Enhetsregisteret; use the Tax Administration’s “Register in the Value Added Tax Register” service. Submission needs the “Value added tax” access package; “Accountant with signing rights” alone can complete the registration application but cannot submit it. Check the decision in the Altinn inbox before issuing VAT invoices. [Registration](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/) and [registration transition](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/)
3. **Classify each sale before applying a rate.** Retain contract/order, invoice, supplier/customer identity and location, description, date, VAT-exclusive amount, and the rule supporting taxable, zero-rated, exempt or outside-scope treatment. Food sold as part of a serving service (restaurant, café, catering) is 25%, not the 15% food rate. Zero-rated supplies count toward registration and are reported; exempt supplies have a different deduction consequence. Do not merge both into a generic zero-percent ledger code. [Rates](https://www.skatteetaten.no/en/rates/value-added-tax/), [VAT Act § 5-2](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*) and [zero-rating/exemption](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/how-vat-works/difference-between-exemptions-and-exceptions-from-vat?pageid=197)
4. **Test input VAT line by line.** Record supplier invoice, business use, VAT amount, deduction conclusion and any mixed-use allocation. A registered business generally deducts input VAT paid on business purchases, subject to the actual use and the following statutory bars, which apply even when the cost is wholly for the business:
   - **No deduction (VAT Act § 8-3)** for input VAT on: serving (restaurant meals, catering) and the hire of function rooms in connection with serving; art and antiques, unless the buyer sells goods of the same kind; food for, and benefits in kind to, the owner, management, employees and pensioners; representation (entertaining business contacts); gifts, and goods and services handed out for advertising, unless the value is insignificant; and building, maintaining, renting and running real property that meets housing or welfare needs, including its furniture and equipment. Building and maintaining a staff canteen, including its loose furniture, remains deductible. Rare exceptions exist (art for use in a museum-type business under § 5-9, gifts of goods exported for use outside the VAT area, and goods for aircraft in foreign traffic or for vessels of at least 15 metres in foreign traffic); refer these.
   - **No deduction for passenger cars (VAT Act § 8-4)**: input VAT on acquiring, running and maintaining a passenger vehicle is not deductible, except for a car held as stock for sale, a rental car in a professional car-rental business, or a car used to carry passengers for payment in a passenger-transport business. Whether a particular vehicle is a "passenger vehicle" depends on its registration class; if unclear, refer.
   - **Cash payments**: a cost paid in cash of NOK 10,000 or more gives no deduction for the expense or its input VAT; instalments of one purchase are added together. Retain electronic-payment evidence.
   Reconcile every claimed line to invoice/import evidence. [Output/input VAT](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/how-vat-works/), [VAT Act § 8-3](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*), [VAT Act § 8-4](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*) and [cash purchases](https://www.skatteetaten.no/en/business-and-organisation/start-and-run/best-practices-accounting-and-cash-register-systems/best-practices-for-daily-operations/expenses/)
5. **Treat imports separately.** Norway is not a member of the EU, so EU intra-community rules do not apply: there are no intra-community acquisitions or zero-rated intra-EU supplies, and an EU VAT-number (VIES) check does not change Norwegian treatment. Goods bought from a supplier in an EU country are imports like goods from any other country, with a customs declaration. [Norway not an EU member](https://www.skatteetaten.no/en/rettskilder/type/kunngjoringer/brexit/) A VAT-registered business calculates import VAT itself in the VAT return for all goods it imports, including goods for which it has no deduction right. A business that is not VAT-registered instead pays import VAT to Norwegian Customs or to its shipping agent. Do not calculate import VAT from a purchase invoice alone. Check that declaration information on value, transport costs and insurance matches supplier/forwarder evidence. Use the confirmed customs-declaration base: For ordinary goods under the general rule, Skatteetaten’s published method adds statistical value to customs duty and other taxes, then applies the supported VAT rate. Art/antiques, dental products and re-import after processing/repair have special bases under [VAT Act § 4-11(2)-(5)](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*) and are referred before using that formula. The purchase invoice date controls accounting-period posting; Norwegian Customs’ shipping date controls the VAT-return period for import VAT. Report on the import codes: 81 (deductible, high rate), 82 (no deduction, high rate), 83 (deductible, medium rate), 84 (no deduction, medium rate) and 85 (zero rate). Deduction on imports follows the same rules as domestic purchases, including the bars in step 4. [Imported goods](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/import/calculating-and-reporting-vat-on-goods-imports/)
6. **Test foreign services before reverse charging.** This is not a goods-import rule. All of these must hold: the buyer is a business or public-sector body with a head office, branch or other fixed place of business in Norway (or a foreign business with a Norwegian VAT representative); the service would be VAT-able if sold in Norway; and the service can be delivered remotely (for example advisory, accounting, electronic services or hire of labour). The scheme does not apply to private individuals, or to non-profit organisations and associations that do not carry on commercial activity. Work that must physically be done in Norway is not in this scheme; the foreign supplier must register. A service performed internally between offices of the same company is not itself a sale/purchase; distinguish an actual external purchase received abroad for use by the same legal entity in Norway. For external services from 1 July 2026, VAT Act § 3-30(2) covers the foreign recipient’s service used by that legal entity’s Norwegian business/public-sector part. Under § 3-30(3), this charge does not apply if the service is wholly for a use that would give input deduction, or if foreign VAT was calculated and the business documents/probably establishes that it cannot be deducted or refunded. Merely showing that foreign VAT was charged is insufficient. The pre-1-July intra-office external-purchase treatment is held below. [VAT Act § 3-30](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*); [2025 amendment, parts II-III](https://lovdata.no/dokument/LTI/lov/2025-12-22-121); [June 2026 amendment, parts I-II](https://lovdata.no/dokument/LTI/lov/2026-06-23-70). Convert the price to NOK using Norwegian Customs’ exchange rate at the time of delivery. A registered buyer reports the self-assessed VAT as output VAT in the ordinary return with no lower threshold. A non-registered buyer uses the reverse-tax-liability VAT return only when that quarter’s VAT basis is **more than NOK 2,000 excluding VAT**; retain the quarter calculation and pay/report through that route. Exactly NOK 2,000 does not cross the statutory test. [VAT Act § 11-3(1)](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*). A reverse charge does not itself establish input recovery: deduction follows the ordinary rules in step 4. [Services from abroad](https://www.skatteetaten.no/en/rates/vat-rates-for-purchases-of-services-from-abroad-svalbard-and-jan-mayen/)
7. **Reconcile, file and pay.** Calculate the ordinary net position as **output VAT on sales + self-assessed VAT − eligible input VAT**. Reconcile each element to the rate/classification schedule, invoices, customs declaration or foreign-service workpaper; investigate a negative outcome as a refund position rather than silently netting it away. Registered enterprises submit a return even with no VAT activity. Ordinary reporting is generally every other month, with filing and payment due on 10 April, 10 June, 31 August, 10 October, 10 December and 10 February; use the current Tax Administration calendar if the nominal date is a non-working day. An approved annual small enterprise files and pays by 10 March; primary industry by 10 April. An annual-period enterprise whose turnover exceeds NOK 1 million must apply to return to two-monthly reporting, and a business that leaves the annual route must report every other month for at least the next two years. Submit using the current service or a compatible accounting system only after the authorised submitter check, then pay from the Altinn payment information at the same deadline. A late return can lead to enforcement fines, even for a period with no turnover, and interest accrues on late payment from the due date until paid. [Ordinary deadline and payment guidance (Norwegian)](https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/*), [return service](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/), [payment route](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/paying-vat/) and [enforcement fines](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/)
8. **Pay, retain and correct.** Pay using the Altinn payment information at submission. Retain the submitted return, confirmation, KID/payment reference and bank evidence. For an ordinary current return error, preserve the original, calculate the corrected amounts from the reconciled records, then submit a new VAT return for the affected term through the logged-in return service or a compatible accounting system. The most recently submitted return applies; the correction must be submitted within 3 years of the original filing deadline. For an import declaration error, correct the declaration with the shipping agent or Norwegian Customs before relying on it in the return. Historic general and primary-industry periods before 1 January 2022, and reverse-charge or VAT-compensation periods before 1 January 2023, use the separately documented contact-form routes. [Current ordinary correction method (Norwegian)](https://www.skatteetaten.no/om-skatteetaten/om-oss/serviceerklaring/), [import declaration corrections](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/import/how-to-correct-errors-in-a-vat-return/) and [historic correction routes](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/)


For the filing deadlines, Tax Administration Act § 5-5(2) applies Courts Act §§ 148-149, including extension from a Saturday/holiday to the following working day. For payment, Tax Payment Act § 10-2 supplies the equivalent rule. [Tax Administration Act](https://lovdata.no/dokument/NL/lov/2016-05-27-14); [Courts Act §§ 148-149](https://lovdata.no/lov/1915-08-13-5/§149); [Tax Payment Act §§ 10-2, 10-30](https://lovdata.no/dokument/NL/lov/2005-06-17-67).

## Worked cases

The 5 cases below are illustrative only. Amounts in equations are assumed NOK amounts and are intentionally shown as bare decimal numerals. They show arithmetic and workflow; they do not decide the rate, deduction or classification of an actual transaction.

### 1. Threshold-crossing invoice

**Facts.** The rolling taxable-sales schedule totals 48000 excluding VAT. A further normal-rated sale is 5000 excluding VAT. Registration follows the threshold crossing.

**Method and result.** The schedule becomes 48000 + 5000 = 53000, which exceeds the limit, so registration is required. After registration, preserve the registration confirmation and issue the credit/replacement invoice sequence if the 5000 invoice was originally issued without VAT. At the published 25% normal rate, output VAT is 5000 × 25 ÷ 100 = 1250 and the replacement invoice total is 5000 + 1250 = 6250. This case assumes the normal-rate classification. [Registration transition](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/) and [rates](https://www.skatteetaten.no/en/rates/value-added-tax/)

### 2. Import: confirmed customs base and different dates

**Facts.** A VAT-registered business receives a purchase invoice dated 28 February; Norwegian Customs’ shipping date is 3 March. The confirmed customs declaration has statistical value 3000 and customs duty/other taxes 1700; the business has a supported 25% rate and full deduction in this example.

**Method and result.** Post the purchase using the invoice date, but report import VAT in the period containing the 3 March shipping date. The confirmed import base is 3000 + 1700 = 4700; import VAT is 4700 × 25 ÷ 100 = 1175. Report both the self-assessed import output VAT and the supported input side. The customs declaration, not this example, controls the real base and any deduction restriction. [Imported goods](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/import/calculating-and-reporting-vat-on-goods-imports/)

### 3. Completion access without submission authority

**Facts.** A bookkeeper has the "Accountant without signing rights" access package and can complete the VAT return in the Tax Administration’s service using Altinn access packages, but cannot submit it.

**Method and result.** Complete and reconcile the draft, but stop before submission. A person with the "Value added tax" or "Accountant with signing rights" access package must submit. Save the access check with the return workpaper. [VAT-return access](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/)

### 4. Ordinary-return correction

**Facts.** A submitted ordinary return omitted 1000 of output VAT. Reconciled records support the correction and the original filing deadline was less than 3 years ago.

**Method and result.** Preserve the submitted return and correction workpaper. Recalculate the affected term and submit a new return through the logged-in service or a compatible accounting system. The latest return applies. Recompute the whole payment/refund position; 1000 is the assumed omitted output amount, not a standalone payment instruction. [Current ordinary correction method (Norwegian)](https://www.skatteetaten.no/om-skatteetaten/om-oss/serviceerklaring/)

### 5. Client lunch and a company passenger car

**Facts.** A registered consultancy pays a restaurant bill for a lunch with a client: 2000 excluding VAT plus 500 VAT at 25%. It also receives a workshop invoice for servicing the managing director’s passenger car, used only for the business. The business does not sell, rent out or carry passengers for payment with cars.

**Method and result.** The restaurant bill is serving and representation, so none of the 500 input VAT is deductible, even though the lunch is for the business. The car servicing is running and maintenance of a passenger vehicle, so its input VAT is not deductible either. Book both costs gross. [VAT Act § 8-3](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*) and [VAT Act § 8-4](https://lovdata.no/dokument/NL/lov/2009-06-19-58/*)



### Recompute the threshold and import cases

These are the assumed records in cases 1 and 2. The threshold-crossing decision uses the whole crossing sale once registered; the import case assumes an ordinary customs base and full deduction, giving a derived zero net VAT effect for that import alone.

```oa-check
name: Norway MVA 2026 threshold crossing and replacement invoice
inputs:
  earlier_sales: 48000
  crossing_sale: 5000
  threshold: 50000
  normal_rate: 0.25
steps:
  - rolling_sales: earlier_sales + crossing_sale
  - threshold_excess: rolling_sales - threshold
  - crossing_invoice_vat: crossing_sale * normal_rate
  - replacement_invoice_total: crossing_sale + crossing_invoice_vat
expected:
  rolling_sales: 53000
  threshold_excess: 3000
  crossing_invoice_vat: 1250
  replacement_invoice_total: 6250
```

```oa-check
name: Norway MVA 2026 ordinary import with full deduction
inputs:
  statistical_value: 3000
  duties_and_other_taxes: 1700
  rate: 0.25
steps:
  - import_base: statistical_value + duties_and_other_taxes
  - import_output_vat: import_base * rate
  - supported_input_vat: import_output_vat
  - net_import_vat: import_output_vat - supported_input_vat
expected:
  import_base: 4700
  import_output_vat: 1175
  supported_input_vat: 1175
  net_import_vat: 0
```

## When to refuse or refer

- The return needs a transaction-specific place-of-supply, exemption, zero-rating or partial-deduction conclusion.
- The matter concerns property adjustments, financial services, joint registration, VAT compensation, VOEC, customs duty or a foreign-business refund.
- It is unclear whether a vehicle is a passenger vehicle, whether a gift or promotional item is of insignificant value, or whether property serves housing or welfare needs.
- The business has no authorised Altinn submitter, has an estimated assessment, or needs an historic correction route not available in the live service.
- Customs/import evidence, foreign-service facts, supplier invoices or VAT-registration status is incomplete.


## Sources

| Actual scope read | Official URL | Read on |
|---|---|---|
| Read for registration, invoicing transition, registration access, decision, late registration and annual period; statutory timing wording takes precedence | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/ | 2026-11-15 |
| Read for VAT Act §§ 2-1, 2-4, 3-30, 4-11, 4-12, 5-2, 8-1 to 8-4, 8-6, 8-8, 11-3, including relevant exceptions | https://lovdata.no/dokument/NL/lov/2009-06-19-58/* | 2026-11-15 |
| Read for 2026 ordinary/reduced VAT rates | https://www.skatteetaten.no/en/rates/value-added-tax/ | 2026-11-15 |
| Read for cash purchase bar and aggregation only | https://www.skatteetaten.no/en/business-and-organisation/start-and-run/best-practices-accounting-and-cash-register-systems/best-practices-for-daily-operations/expenses/ | 2026-11-15 |
| Read for Tax Administration Regulation §§ 8-3-1, 8-3-3 to 8-3-7, 8-3-10: periods, annual conditions and deadlines | https://lovdata.no/dokument/SF/forskrift/2016-11-23-1360/* | 2026-11-15 |
| Read for Tax Administration Act § 5-5: deadline computation cross-reference | https://lovdata.no/dokument/NL/lov/2016-05-27-14 | 2026-11-15 |
| Read for Courts Act §§ 148-149: calendar periods and Saturday/holiday extension | https://lovdata.no/lov/1915-08-13-5/§149 | 2026-11-15 |
| Read for Tax Payment Act §§ 10-2, 10-30: payment deadline and holiday rule | https://lovdata.no/dokument/NL/lov/2005-06-17-67 | 2026-11-15 |
| Read for payment information, annual applicants, primary industries and period changes | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/paying-vat/ | 2026-11-15 |
| Read for return submission access and dated Altinn II transition; historic correction routes | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/ | 2026-11-15 |
| Read for VAT Regulation § 2-4-1: VAT-inclusive significant purchases and strict timing conditions | https://lovdata.no/dokument/SF/forskrift/2009-12-15-1540/* | 2026-11-15 |
| Read for zero-rate versus exemption, registration and deduction consequences | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/how-vat-works/difference-between-exemptions-and-exceptions-from-vat?pageid=197 | 2026-11-15 |
| Read for output/input VAT framework | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/how-vat-works/ | 2026-11-15 |
| Read for Norway outside EU and VAT treatment of goods from EU countries | https://www.skatteetaten.no/en/rettskilder/type/kunngjoringer/brexit/ | 2026-11-15 |
| Read for ordinary and exceptional import bases, declarations, invoice/shipping dates, five codes and deduction evidence | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/import/calculating-and-reporting-vat-on-goods-imports/ | 2026-11-15 |
| Read for 2025 amending law parts II-III in full: foreign external services, exceptions and 1 July 2026 commencement | https://lovdata.no/dokument/LTI/lov/2025-12-22-121 | 2026-11-15 |
| Read for 2026 amending law in full: non-refundable foreign VAT condition, effective 1 July 2026 | https://lovdata.no/dokument/LTI/lov/2026-06-23-70 | 2026-11-15 |
| Read for remote-service/buyer tests, currency conversion and reporting; superseded threshold/intra-office wording not used over current statutes | https://www.skatteetaten.no/en/rates/vat-rates-for-purchases-of-services-from-abroad-svalbard-and-jan-mayen/ | 2026-11-15 |
| Read for MVA resubmission, most recent return, three-year amendment window and payment information | https://www.skatteetaten.no/om-skatteetaten/om-oss/serviceerklaring/ | 2026-11-15 |
| Read for customs correction, new return and amendment window | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/import/how-to-correct-errors-in-a-vat-return/ | 2026-11-15 |

Not yet confirmed: treatment before 1 July 2026 of an external service purchased by a foreign part of the same legal entity for its Norwegian part; client-specific classification, partial deduction and live form fields. Property adjustments, joint registration, compensation, VOEC, special import valuation and foreign-business refunds require their separate method. The English remote-services page says “at least NOK 2,000” and retains older foreign-VAT wording; the operative statute instead requires a quarterly basis exceeding NOK 2,000 and supplies the post-1-July exceptions. The English registration page says “more than 4 months”; VAT Regulation § 2-4-1 excludes a period of less than 4 months. These differences are reconciled above rather than treated as usable alternatives.
