---
name: iceland-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Iceland VAT (VSK) return for any client. Trigger on phrases like "prepare VSK return", "Iceland VAT", "virðisaukaskattur", "Icelandic VAT filing", or any request involving Icelandic VAT. Iceland is NOT an EU member but IS in the EEA. This skill covers Iceland only. MUST be loaded alongside vat-workflow-base v0.1 or later. Does NOT require eu-vat-directive (Iceland is not EU). ALWAYS read this skill before touching any Iceland VSK work.
version: 2.0
jurisdiction: IS
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland VAT (VSK): 2026 registration, return and payment method

**Status:** **Source-cited draft** by the OpenAccountants team. It is not accountant-authored, accountant-verified or an attestation. Current administrative guidance was retrieved from Iceland Revenue and Customs (Skatturinn) on 24 September 2026. This operational replacement retains the public `iceland-vat` Guide’s Iceland VSK scope for registration, rate/exemption classification, ordinary foreign-service liability, input VAT, return preparation, correction and payment.

Figures are for tax year 2026.

## Source figures

| Figures used below | Status | Official source |
| --- | --- | --- |
| 2026; ISK 2,000,000; 24%; 11%; 12-month; one month and five days; 5 April; ISK 4,000,000; 15 February; eight days; seven years; ISK 5,000; 1%; 10%; 30 days | Published administrative figures or periods. Apply only under the conditions stated in the method. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 100,000; 24,000; 20,000; 4,800; 19,200; 50,000; 5,500; 250,000; 10,000; 2,400; 1,950,000; 5 June | Hypothetical inputs or arithmetic outputs in the labelled worked cases, not authority figures. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| RSK 5.02 | Official registration form identifier. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 20,000 | Hypothetical Case A purchase base, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| 0% | Case-only mathematical output for the zero-rated Case C; the authority’s zero-rate category still requires its stated conditions. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 100,000 | Hypothetical Case A sales base, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 24,000 | Hypothetical Case A output VAT, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 19,200 | Hypothetical Case A payable difference, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 50,000 | Hypothetical Case B sales base, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 5,500 | Hypothetical Case B output VAT, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 10,000 | Hypothetical Case D purchase base, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 1,950,000 | Hypothetical Case E taxable sales, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 250,000 | Hypothetical Case C export value, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 4,800 | Hypothetical Case A/C input-VAT amount, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| ISK 2,400 | Hypothetical Case D blocked-input VAT amount, not an authority figure. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| RSK 10.24 | Official foreign-service VAT report identifier. | [Skatturinn form RSK 10.24](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf) |
| RSK 10.26 | Official annual-reconciliation correction form identifier. | [Skatturinn VAT-register guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/) |

## The method, step by step

1. Confirm the entity, registration status, settlement period and prior statement.
2. Build invoice-backed sales, purchases and import schedules, then classify each line.
3. Reconcile output and supported input VAT, file the current electronic statement, pay the stated amount and retain confirmation.

## Ask the client first

- What do the Icelandic VAT registration record and current settlement period say?
- What invoice, supplier/customer status, business use and rate/exemption facts support each transaction?
- Are imports, foreign services, VOES, mixed exempt activity, property or a correction involved?
- Has a statement already been filed or an assessment/penalty notice been issued?

## 1. Establish the filing route before calculating VAT

Obtain the legal seller, Icelandic ID (`kennitala`), VAT registration number, registration certificate, settlement period, start date and any prior return. Keep separate facts for each supply: customer identity and location, what was supplied, supply date, amount excluding VAT, invoice, rate/exemption reason, and import or foreign-service evidence.

Skatturinn says domestic and foreign companies and self-employed people selling taxable goods or services in Iceland generally register using form RSK 5.02. A business selling exempt labour/services, or taxable goods/services of **ISK 2,000,000 or less in each 12-month period from commencement**, is exempt from registration duty; employees are not within that duty. A foreign taxable person follows the same rules. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

Registration is a factual test, not a rate election. A foreign company without an Icelandic permanent establishment that sells taxable services in Iceland must use an Iceland-domiciled representative; both are responsible for collection and payment. A foreign business that only supplies goods/services from abroad to Icelandic recipients, other than electronically supplied services, is not liable under the general statement on Skatturinn’s page. Imported goods remain taxable at import. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

**VOES is separate.** It is an optional simplified, pay-only registration for qualifying foreign suppliers to non-taxable Icelandic customers. It covers listed electronic, telecom, paper/magazine-subscription, broadcasting and certain tourist services; it cannot be used where an Icelandic permanent establishment supplies the goods/services. A foreign B2C supplier of electronic services exceeding ISK 2,000,000 in a 12-month period must register/account for VAT, while a registered Icelandic B2B buyer can account for the VAT as input tax. Establish the seller, customer status and supply before choosing ordinary registration, VOES or a different route. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

## 2. Classify every supply from evidence

Iceland VAT is generally charged on domestic business transactions and imports unless a direct exemption applies. The published rates are **24% standard** and **11% reduced**. Do not choose a rate from a merchant name, product label or the customer’s country alone. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

| Classification | Operational treatment | Evidence to retain |
| --- | --- | --- |
| Standard taxable supply | Apply 24% to the VAT-exclusive consideration once the domestic taxable supply is confirmed. | Contract/order, invoice, customer/location and rate calculation. |
| Reduced taxable supply | Apply 11% only when the actual supply fits the published list, including qualifying short-term accommodation, camping, catering/food, alcohol, certain passenger transport/tours, self-employed guides, spas, radio/TV subscriptions, books and listed media. | What was supplied, duration/location where relevant, and invoice description. |
| Zero-rated supply | Charge 0% only after meeting a published zero-rate condition. Examples include qualifying exports, international goods transport, passenger transport to/from Iceland, certain foreign-use services and qualifying services to vessels/aircraft. A zero-rated supply remains within VAT scope. | Export/customs or transport evidence; purchaser establishment/use evidence for services. |
| Exempt supply | Do not charge output VAT. Skatturinn lists, among others, health, social/education, certain culture/sport, listed public transport, postal, qualifying property rental/sale, insurance, banking/financial, lotteries and certain artistic activities. Exempt-business purchases do not give input VAT credit. | Legal/service facts and any voluntary property-registration evidence. |
| Import fact pattern | Do not infer a domestic rate or input credit. Identify importer, customs document, supplier establishment, buyer VAT status, use and the applicable Icelandic rule. | Customs declaration, supplier invoice, contract and customer VAT status. |
| Foreign-service purchase from abroad | Use RSK 10.24 only where this purchaser-liability route applies. A VAT-registered buyer that could count the VAT as input tax if the service were domestic is exempt from this route. A liable purchaser reports the **full** VAT-exclusive consideration and 24% VAT. Hold a partly creditable/mixed-use service for a separately sourced method. | Supplier invoice/contract, service description, supplier country/Iceland VAT registration or agent status, purchaser’s registration and input-credit facts, transaction date and full VAT-exclusive total consideration. [Skatturinn foreign-service guidance](https://www.skatturinn.is/media/baeklingar/rsk_1119.is.pdf) and [RSK 10.24](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf). |

For ordinary calculations, use `output VAT = taxable VAT-exclusive sales × confirmed rate`. Keep 24%, 11%, zero-rated and exempt sales in separate schedules. A zero rate is not an exemption: zero-rated supplies can retain VAT-law input-deduction treatment, while exempt activities do not. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

## 3. Test input VAT before deducting it

Input VAT is deductible only for VAT on goods, business assets and services bought for a VAT-liable business activity. The VAT must be verified by a sales invoice, and the vendor must have charged VAT and been VAT-registered at the transaction date. Check the invoice and vendor registration; a bank line alone is not sufficient. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

Apply an invoice-control check to every ordinary sales and purchase invoice before it enters the VAT schedules. Subject to the fact-specific Article 21 exception, confirm seller and buyer identifiers, seller VAT number, issue date, consecutive invoice number, clear supply description, quantity/unit where applicable, total price, and whether VAT is included or stated separately. Escalate a missing or inconsistent control instead of substituting a bank transaction. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

Do **not** include input VAT for the listed blocked categories: staff/owner dining and food except resale; owner/staff living quarters; owner/staff perquisites; vacation homes and similar facilities; entertainment and gifts; and acquisition, operation or rental of passenger cars and specified light delivery/transport/off-road vehicles. Mixed taxable/exempt activity needs a separate supportable attribution method; this draft does not invent one. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

Build a purchase schedule with supplier, date, invoice number, VAT-exclusive amount, VAT shown, vendor VAT status, business use, classification and deduction result. Reconcile the deductible total to the purchase ledger and evidence before netting it against output VAT.

### Foreign-service purchaser workflow

Use this route only for a service bought from abroad that is within the published imported-service categories, such as electronically supplied, telecom, broadcasting, advertising or specialist services. It does not turn every foreign invoice into a VAT charge.

1. Record the foreign seller, country, invoice/contract, transaction date, service type and VAT-exclusive total consideration. Check whether the seller or an Icelandic agent is already Iceland VAT-registered; if so, do not apply the buyer route merely because the seller is foreign.
2. Identify the buyer’s registration and input-credit result. A VAT-registered buyer that could count VAT on the service as input tax if it were acquired domestically is exempt from this purchaser route. A liable purchaser, including the wholly exempt buyer in Case F, must use the full consideration. Do not derive a partial-liability percentage for mixed or partly creditable use from these sources; hold that fact pattern.
3. For a liable purchaser, calculate `foreign-service VAT = full VAT-exclusive consideration × 24 ÷ 100`. Complete **RSK 10.24** with the service line(s), supplier and buyer details, the full VAT-exclusive consideration, 24% VAT, and the stated use purpose. Submit with payment for that period by the due date printed on the form: the fifth day of the second month after the ordinary settlement period. Retain the form, invoice and input-credit analysis.

This is a purchaser-liability payment route. Do not also claim the same amount as ordinary input VAT unless a separate current rule supports that result for the taxpayer’s exact facts. [Skatturinn foreign-service guidance](https://www.skatturinn.is/media/baeklingar/rsk_1119.is.pdf) and [RSK 10.24](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf)

## 4. Prepare the return for the correct period

The ordinary settlement periods are Jan–Feb, Mar–Apr, May–Jun, Jul–Aug, Sep–Oct and Nov–Dec. The electronic VAT statement and payment are due **one month and five days after period end**: for example, Jan–Feb is due 5 April, moved to the next business day if the date is a weekend or Icelandic public holiday. A registered person must file electronically even with no sales. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

The return requires total VAT-exclusive sales by tax rate, zero-rate sales, and total output and input VAT. Do not reproduce historic, unlabeled return-field letters: use the current Skatturinn filing screen and match each value to the schedules. After filing, payment can be made through Icelandic online banking. A foreign-bank payment must use the current official instructions and identify the VAT registration number, year and period. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

Use this working sequence:

1. Lock the legal entity and settlement period; check whether the business is registered and whether a special period has been granted.
2. Reconcile invoices, credit notes, import documents and payment records to a sales and purchase schedule. Do not record gross bank deposits as sales without the underlying evidence.
3. Classify each sale as 24%, 11%, zero-rated, exempt or unresolved; total each group excluding VAT.
4. Compute output VAT for confirmed taxable sales. Keep zero-rated and exempt values visible even where output VAT is zero.
5. Test each purchase for a valid VAT invoice, registered vendor, VAT-liable business use and blocked/mixed-use status; total only supported deductible input VAT.
6. Compute `net VSK = total output VAT − deductible input VAT`. A positive calculated difference is payable. If the difference is negative, enter the supported totals and use the live statement/account process to determine handling; this source set does not establish a normal refund/offset outcome.
7. Enter the totals in the live electronic statement, review the confirmation, pay any stated liability or retain the account outcome, and archive the submission, ledger and support.

## 5. Period choices, amendments and record controls

A taxpayer with taxable sales below **ISK 4,000,000 in a whole calendar year** may request annual settlement for the following year; apply before 15 February for that year. Six-month settlement is available only to agriculture. Monthly settlement can be available where input VAT is generally higher than output VAT because a major share of turnover is exempt, or where reduced-rate sales dominate but standard-rate input VAT dominates; apply at least one month before the next period. These are application-based alternatives, not automatic selections. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

Notify Skatturinn of a post-registration change in operations, including a different activity or VAT-taxable cessation, within eight days. Keep VAT accounts, sales documents and vouchers available to the authority. For a foreign company using an Icelandic representative, the representative must keep the complete VAT accounts and supporting documents in Iceland for at least seven years after the accounting year. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

Failure to file permits an estimated assessment. Skatturinn states that filing after an estimate adds an ISK 5,000 surcharge. Late payment has a 1% daily penalty up to 10%, followed after one month by late-payment interest; sufficient cause can support cancellation of the penalty. An appeal to the Director of Internal Revenue is generally due within 30 days of the decision, with a further written appeal route to the Internal Revenue Board. Use the live account/notice and current procedural instructions for an actual dispute. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

### Correct a filed ordinary statement

1. Identify the exact settlement period, original filing/assessment status, the omitted or wrong record, and the schedules that change. Preserve the original statement, correction calculation and evidence.
2. Before assessment for that period is complete, the taxpayer can correct the submitted statement electronically. Skatturinn states that assessment is completed one month after the due date. Use the live service rather than a paper workaround unless the authority’s stated exception applies.
3. After the annual reconciliation identifies a difference between the returns and annual accounts, use **RSK 10.26**. A taxpayer with a settlement period shorter than two months cannot use RSK 10.26 for after-year corrections and instead files one RSK 10.01 statement for each affected period. Do not apply either correction route to a mixed-activity allocation or capital-use adjustment without the applicable specialised method.

[Skatturinn VAT-register correction guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/)

## 6. Worked mechanical cases

These cases are arithmetic illustrations from the cited rules, not filing results. They assume the evidence and eligibility stated in each case; they do not establish VAT treatment for a different supply.

| Case | Facts and calculation | Expected VSK result |
| --- | --- | --- |
| Standard domestic sale with supported input | Registered Icelandic business sells a confirmed 24% domestic service for ISK 100,000 excluding VAT: output `100,000 × 24% = 24,000`. It has a valid invoice for a wholly taxable-business purchase of ISK 20,000 plus ISK 4,800 VAT: deductible input 4,800. | **ISK 19,200 payable** (`24,000 − 4,800`). |
| Reduced-rate sale | Registered business makes a confirmed 11% qualifying accommodation sale for ISK 50,000 excluding VAT. | **ISK 5,500 output VAT**; input VAT depends on separately tested purchases. |
| Zero-rated export | Registered seller has a documented qualifying export of goods for ISK 250,000 and a valid input-VAT invoice for ISK 4,800 used in the taxable/zero-rated activity. | **No output VAT** on the export and a calculated **ISK 4,800 negative difference** before the live statement/account process; this packet does not state whether that becomes a refund or offset. |
| Input is blocked | Registered business buys owner/staff food for ISK 10,000 plus ISK 2,400 VAT. | **No deductible input VAT** for that purchase. |
| Registration screen | A new business has ISK 1,950,000 of taxable sales in the relevant 12-month period from commencement and no other registration trigger shown. | It is within the stated ISK 2,000,000-or-less registration-duty exemption. Monitor the rolling commencement-period facts; do not issue/collect VAT without first resolving registration status. |
| Missed ordinary return | A registered business makes no sales in Mar–Apr. | It still files the electronic return by **5 June** unless that day moves to the next business day. |
| Foreign specialist service used in exempt activity | An exempt Icelandic business buys a covered foreign specialist service for ISK 100,000 from a supplier with no Iceland VAT registration/agent. The buyer cannot count the VAT as input tax. | Complete RSK 10.24 with the buyer/supplier, date, service, ISK 100,000 VAT-exclusive consideration and **ISK 24,000 VAT** (`100,000 × 24 ÷ 100`); pay by the form’s stated deadline. |
| Correction before assessment | A Mar–Apr electronic statement omitted a supported ISK 100,000 standard-rate domestic sale. The period’s assessment is not complete. | Preserve the correction schedule and submit the electronic correction for that period. The missing **ISK 24,000 output VAT** (`100,000 × 24 ÷ 100`) is included in the revised period data; do not invent a separate delta box. |

## When to refuse or refer

- Registration, rate, exemption, place, Customs or input-VAT evidence is missing.
- The matter requires VOES conclusion, mixed attribution, property analysis, special scheme, a foreign-service category outside the sourced ordinary purchaser route, or a mixed/partly creditable foreign-service purchase.
- A required invoice, vendor-registration check, Customs document, prior statement or assessment notice is unavailable.

## 7. Stop conditions

Use a separate sourced method or professional review for mixed taxable/exempt attribution, voluntary real-property registration, imported goods/customs valuation, VOES eligibility, foreign representative arrangements, special investment/fishing schemes, a foreign-service category outside the ordinary purchaser route, a missing VAT invoice, a supplier that was not registered, and an estimated assessment or appeal. The normal method above handles confirmed domestic taxable rates, zero-rated evidence, exempt outputs, supported input VAT, invoice controls, the ordinary foreign-service purchaser payment route, corrections before assessment and the ordinary return timetable.

Official sources: [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/); [Skatturinn foreign-service guidance](https://www.skatturinn.is/media/baeklingar/rsk_1119.is.pdf); [RSK 10.24 foreign-service purchase report](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf); [Skatturinn VAT-register correction guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/). Source snapshots, evidence ledger and cases are retained in the controlled editorial packet.

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
