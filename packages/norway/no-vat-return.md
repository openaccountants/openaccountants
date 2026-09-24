---
name: no-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Norway MVA return (MVA-melding) for any client. Trigger on phrases like "prepare MVA return", "Norwegian VAT", "MVA-melding", "merverdiavgift", or any request involving Norway VAT filing. Norway is NOT an EU member but IS in the EEA. There are NO intra-community supplies. All goods from EU are imports. ALWAYS read this skill before touching any Norway MVA work.
jurisdiction: "NO"
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway VAT return: registration to reconciliation

Figures are for tax year 2026 and guidance was retrieved on 24 September 2026. This Guide is for an ordinary business registered in Norway’s VAT Register. It covers registration, classification control, return preparation, payment and evidence. It does not decide a transaction’s place of supply, a zero-rate/exemption provision, partial deduction, joint registration, VAT compensation, VOEC, customs duty or a foreign-business refund.

## Rates, threshold and annual-period figures

| Item | Current published figure | Use | Source |
| --- | --- | --- | --- |
| Registration threshold | NOK 50,000 taxable sales turnover, excluding VAT, in 12 months | Test before ordinary registration. | [Registration](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/) |
| Normal VAT rate | 25% | Use only after confirming normal-rated Norwegian treatment. | [Rates](https://www.skatteetaten.no/en/rates/value-added-tax/) |
| Reduced VAT rates | 15% and 12% | Confirm that the actual food/water-wastewater or listed transport/cinema/room category applies. | [Rates](https://www.skatteetaten.no/en/rates/value-added-tax/) |
| Cash-payment control | NOK 10,000 | A cash purchase at or above this amount can prevent expense and input-VAT deduction. | [Cash purchases](https://www.skatteetaten.no/en/business-and-organisation/start-and-run/best-practices-accounting-and-cash-register-systems/best-practices-for-daily-operations/expenses/) |
| Non-registered foreign-service route | quarterly VAT basis **at least** NOK 2,000 | Apply only after the remotely-deliverable-service conditions are met; use the reverse-tax-liability return. | [Foreign services](https://www.skatteetaten.no/en/rates/vat-rates-for-purchases-of-services-from-abroad-svalbard-and-jan-mayen/) |
| Ordinary two-month return and payment deadlines | 10 April; 10 June; 31 August; 10 October; 10 December; 10 February | The payment deadline is the same as the filing deadline; check the current calendar where a date falls on a non-working day. | [Statutory deadline guidance (Norwegian)](https://www.skatteetaten.no/rettskilder/type/handboker/skattebetalingshandboken/gjeldende/kapittel-10.-forfall/ID-10-13.001/ID-10-13.005/) |
| Annual small-enterprise cap | NOK 1 million excluding VAT | Application route: taxable supplies and withdrawals in the calendar year, 12 months' registration and timely prior returns/payments are all required. | [Annual route](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/paying-vat/) |
| Annual filing deadlines | 10 March; 10 April for primary industry | Apply only to the matching approved/primary-industry route. | [Annual route](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/paying-vat/) |
| Primary-industry other VATable revenue notice | NOK 30,000 | Inform Skatteetaten if the stated condition is met. | [Annual route](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/paying-vat/) |

Official sources and exact locators are in the evidence ledger. A rate table supplies examples, not a legal classification for every supply.

## The method, step by step

1. **Confirm entity, period and authority.** Record the organisation number, VAT registration effective date, settlement period, prior return and the person preparing the return. Access to complete a return is different from authority to submit it. Check the business’s actual Altinn access package and the submitter’s signing/delegated authority before submission; some roles can complete but not submit. [VAT return access](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/)
2. **Test registration and retain the transition evidence.** Maintain a rolling schedule of taxable sales turnover, excluding VAT. When registration follows threshold crossing, retain the registration confirmation and the invoice trail. If an invoice was issued before registration, use the source-described credit and replacement-invoice sequence rather than adding VAT informally. [Registration](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/) and [registration transition](https://www.skatteetaten.no/en/business-and-organisation/start-and-run/new-as-a-business/new-enk/)
3. **Classify each sale before applying a rate.** Retain contract/order, invoice, supplier/customer identity and location, description, date, VAT-exclusive amount, and the rule supporting taxable, zero-rated, exempt or outside-scope treatment. Zero-rated supplies count toward registration and are reported; exempt supplies have a different deduction consequence. Do not merge both into a generic zero-percent ledger code. [Rates](https://www.skatteetaten.no/en/rates/value-added-tax/) and [zero-rating/exemption](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/how-vat-works/difference-between-exemptions-and-exceptions-from-vat?pageid=197)
4. **Test input VAT line by line.** Record supplier invoice, business use, VAT amount, deduction conclusion and any mixed-use allocation. A registered business generally deducts input VAT paid on business purchases, subject to the actual use and restriction. Reconcile every claimed line to invoice/import evidence and retain electronic-payment evidence where the cash-payment rule is relevant. [Output/input VAT](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/how-vat-works/) and [cash purchases](https://www.skatteetaten.no/en/business-and-organisation/start-and-run/best-practices-accounting-and-cash-register-systems/best-practices-for-daily-operations/expenses/)
5. **Treat imports separately.** Do not calculate import VAT from a purchase invoice alone. Check that declaration information on value, transport costs and insurance matches supplier/forwarder evidence. Use the confirmed customs-declaration base: Skatteetaten’s published method adds statistical value to customs duty and other taxes, then applies the supported VAT rate. The purchase invoice date controls accounting-period posting; Norwegian Customs’ shipping date controls the VAT-return period for import VAT. [Imported goods](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/import/calculating-and-reporting-vat-on-goods-imports/)
6. **Test foreign services before reverse charging.** This is not a goods-import rule. Establish buyer connection to Norway, remotely deliverable service, Norwegian taxable treatment and stated exceptions. A registered buyer reports the self-assessed output VAT in the ordinary return without a lower threshold. A non-registered buyer uses the reverse-tax-liability VAT return only when that quarter’s VAT basis is **at least NOK 2,000**; retain the quarter calculation and pay/report through that route. A reverse charge does not itself establish full input recovery. [Services from abroad](https://www.skatteetaten.no/en/rates/vat-rates-for-purchases-of-services-from-abroad-svalbard-and-jan-mayen/)
7. **Reconcile, file and pay.** Calculate the ordinary net position as **output VAT on sales + self-assessed VAT − eligible input VAT**. Reconcile each element to the rate/classification schedule, invoices, customs declaration or foreign-service workpaper; investigate a negative outcome as a refund position rather than silently netting it away. Registered enterprises submit a return even with no VAT activity. Ordinary reporting is generally every other month, with filing and payment due on 10 April, 10 June, 31 August, 10 October, 10 December and 10 February; use the current Tax Administration calendar if the nominal date is a non-working day. Submit using the current service or a compatible accounting system only after the authorised submitter check, then pay from the Altinn payment information at the same deadline. [Ordinary deadline and payment guidance (Norwegian)](https://www.skatteetaten.no/rettskilder/type/handboker/skattebetalingshandboken/gjeldende/kapittel-10.-forfall/ID-10-13.001/ID-10-13.005/), [return service](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/) and [payment route](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/paying-vat/)
8. **Pay, retain and correct.** Pay using the Altinn payment information at submission. Retain the submitted return, confirmation, KID/payment reference and bank evidence. For an ordinary current return error, preserve the original, calculate the corrected amounts from the reconciled records, then submit a new VAT return for the affected term through the logged-in return service or a compatible accounting system. The most recently submitted return applies; the correction must be submitted within three years of the original filing deadline. For an import declaration error, correct the declaration with the shipping agent or Norwegian Customs before relying on it in the return. Historic general and primary-industry periods before 1 January 2022, and reverse-charge or VAT-compensation periods before 1 January 2023, use the separately documented contact-form routes. [Current ordinary correction method (Norwegian)](https://www.skatteetaten.no/om-skatteetaten/om-oss/serviceerklaring/), [import declaration corrections](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/import/how-to-correct-errors-in-a-vat-return/) and [historic correction routes](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/)

## Ask the client first

- What is the entity’s registration effective date, settlement period, current Altinn access package and named authorised submitter?
- What is the rolling taxable-sales-turnover total, excluding VAT, and which invoices make it up?
- For each unusual sale, what was supplied, where, to whom and under which rate/zero/exemption provision?
- Are there imported goods, customs declarations and shipping dates that differ from invoice dates?
- Are there services bought from abroad, Svalbard or Jan Mayen, and what establishes buyer connection, service type and place of supply?
- Is any input used for exempt, private or mixed activity, or paid in cash at the relevant level?
- Does the enterprise seek an annual small-enterprise period? Confirm calendar-year taxable supplies and withdrawals are no more than NOK 1 million excluding VAT, at least 12 months’ VAT registration, timely prior returns/payments, the 10 December–1 February application window and actual approval.

## Worked preparation cases

The four cases below are illustrative only. Amounts in equations are assumed NOK amounts and are intentionally shown as bare decimal numerals. They show arithmetic and workflow; they do not decide the rate, deduction or classification of an actual transaction.

### 1. Threshold-crossing invoice

**Facts.** The rolling taxable-sales schedule totals 48000 excluding VAT. A further normal-rated sale is 5000 excluding VAT. Registration follows the threshold crossing.

**Method and result.** The schedule becomes 48000 + 5000 = 53000. After registration, preserve the registration confirmation and issue the source-described credit/replacement invoice sequence if the 5000 invoice was originally issued without VAT. At the published 25% normal rate, output VAT is 5000 × 25 ÷ 100 = 1250 and the replacement invoice total is 5000 + 1250 = 6250. This case assumes the normal-rate classification. [Registration transition](https://www.skatteetaten.no/en/business-and-organisation/start-and-run/new-as-a-business/new-enk/) and [rates](https://www.skatteetaten.no/en/rates/value-added-tax/)

### 2. Import: confirmed customs base and different dates

**Facts.** The purchase invoice is dated 28 February and Norwegian Customs’ shipping date is 3 March. The confirmed customs declaration has statistical value 3000 and customs duty/other taxes 1700; the business has a supported 25% rate and full deduction in this example.

**Method and result.** Post the purchase using the invoice date, but report import VAT in the period containing the 3 March shipping date. The confirmed import base is 3000 + 1700 = 4700; import VAT is 4700 × 25 ÷ 100 = 1175. Report both the self-assessed import output VAT and the supported input side. The customs declaration, not this example, controls the real base and any deduction restriction. [Imported goods](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/import/calculating-and-reporting-vat-on-goods-imports/)

### 3. Completion access without submission authority

**Facts.** A bookkeeper can complete the VAT return in Altinn but lacks signing/delegated authority to submit it.

**Method and result.** Complete and reconcile the draft, but stop before submission. An authorised person or a valid delegation must submit. Save the access check with the return workpaper. [VAT-return access](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/)

### 4. Ordinary-return correction

**Facts.** A submitted ordinary return omitted 1000 of output VAT. Reconciled records support the correction and the original filing deadline was less than three years ago.

**Method and result.** Preserve the submitted return and correction workpaper. Recalculate the affected term and submit a new return through the logged-in service or a compatible accounting system. The latest return applies. Recompute the whole payment/refund position; 1000 is the assumed omitted output amount, not a standalone payment instruction. [Current ordinary correction method (Norwegian)](https://www.skatteetaten.no/om-skatteetaten/om-oss/serviceerklaring/)

## When to refuse or refer

- The return needs a transaction-specific place-of-supply, exemption, zero-rating or partial-deduction conclusion.
- The matter concerns property adjustments, financial services, joint registration, VAT compensation, VOEC, customs duty or a foreign-business refund.
- The business has no authorised Altinn submitter, has an estimated assessment, or needs an historic correction route not available in the live service.
- Customs/import evidence, foreign-service facts, supplier invoices or VAT-registration status is incomplete.

## Sources

The exact captured official pages, locators and claim-level coverage are in `quality-evidence.json` and `sources.json`.

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
