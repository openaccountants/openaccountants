---
name: ae-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a UAE VAT return (VAT201 form) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in VAT201", "create the return", "UAE VAT filing", "FTA return", or any request involving UAE VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers the UAE only and only standard VAT-registered persons filing VAT201. VAT groups, profit margin schemes, partial exemption with non-trivial exempt supplies, and Designated Zone goods movement classifications are all in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any UAE VAT work.
jurisdiction: AE
tax_year: 2026
last_updated: 2026-09-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UAE VAT: 2026 registration, rates, VAT201 return, reverse charge, input tax and e-invoicing

Tax year 2026. UAE VAT is filed by tax period (usually a quarter), not by annual return, so "2026" here means tax periods that fall in calendar year 2026. The rules below are the law as published on tax.gov.ae and mof.gov.ae on 25 September 2026. Two sets of changes took effect this year (1 January 2026 and 14 April 2026) and one more takes effect on 1 October 2026; each is dated where it applies. A short section covers returns for periods that ended before those dates.

## Scope and who this is for ([VAT Law, consolidated to Decree-Law No. 16 of 2025](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Executive Regulation, consolidated 09-2026](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

This Guide covers federal Value Added Tax under Federal Decree-Law No. 8 of 2017 ("VAT Law") and its Executive Regulation (Cabinet Decision No. 52 of 2017), for:

- businesses deciding whether they must or may register;
- a single VAT-registered business (not a Tax Group) preparing or reviewing its VAT201 return;
- classifying sales and purchases: standard rate, zero rate, exempt, not a supply, reverse charge, blocked input tax;
- invoicing, record keeping, penalties and the e-invoicing timeline.

It does not compute partial-exemption apportionment, Tax Group returns, Designated Zone goods movements, capital asset scheme adjustments, the oil and gas reverse charge, or tourist refund scheme entries. Those are referred out (see "When to refuse or refer"). It does not cover Corporate Tax or Excise Tax.

The standard rate is 5% ([VAT Law, Article 3](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf)). All amounts on the return are in UAE dirhams (AED).

## Ask the client first

- **Is the business registered, and from what date?** Get the TRN, the effective date of registration and the tax period on the registration certificate. The period the FTA assigned governs, not a rule of thumb.
- **Is it a single registrant or a member of a Tax Group?** Tax Groups are referred out.
- **Where is it established?** Which Emirate (for the Box 1 split), and is it in a Designated Zone, a free zone that is not designated, or the mainland?
- **What does it sell, and to whom?** Local customers, customers abroad, other GCC countries, consumers or businesses. Any residential property, bare land, financial services, education, healthcare or local passenger transport?
- **Does it make any exempt supplies?** If more than trivial, input tax must be apportioned: refer.
- **What did it buy from abroad?** Services or software billed by a supplier with no UAE TRN (reverse charge), and goods imported through UAE customs (Box 6).
- **Which costs are entertainment, cars, or staff benefits?** These are the main blocked items.
- **Has it paid its suppliers?** Input tax on an unpaid bill is claimable only if the business intends to pay within six months of the agreed payment date ([Executive Regulation, Article 54(2)](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf)).
- **Any errors in earlier returns?** The size of the tax difference decides whether a voluntary disclosure is needed.
- **Excess input tax carried forward?** And from which tax period it arose (the five-year limit applies from 1 January 2026).
- **Revenue in the last accounting period?** It decides the e-invoicing deadline (the AED 50,000,000 test in [Ministerial Decision No. 244 of 2025](https://mof.gov.ae/wp-content/uploads/2025/09/Ministerial-Decision-No.-244-of-2025-on-the-Implementation-of-the-Electronic-Invoicing-System.pdf)).

## The method, step by step

1. **Confirm registration.** If not registered, test the mandatory threshold (supplies in the last 12 months, or expected in the next 30 days) and the voluntary threshold ([Executive Regulation, Articles 7 and 8](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf)). A late registrant owes VAT on supplies made from the date it should have been registered.
2. **Fix the tax period and deadline.** Take the period from the certificate. The return and the payment must both reach the FTA by the 28th day after the period ends.
3. **Classify each sale.** Standard 5%, zero-rated, exempt, or not a supply ([VAT Law, Articles 3, 45 and 46](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf)). Check the zero-rating conditions. Services to an overseas customer are zero-rated only if all of these hold: the customer has no place of residence in a GCC implementing state; the customer is outside the UAE when the services are performed; the services are not directly connected with real estate in the UAE, or with moveable goods in the UAE at the time the services are performed; and the services are not treated as performed in the UAE under the special place-of-supply rules in VAT Law Articles 30(3)-(8) and 31. Services actually performed outside the implementing states are also zero-rated ([Executive Regulation, Article 31(1)](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf)).
4. **Split standard-rated sales by Emirate** for Box 1a-1g.
5. **Pick up reverse-charge purchases.** Services and goods from suppliers with no UAE place of residence who are not charging UAE VAT go in Box 3 (output VAT) and, if recoverable, Box 10. Imports through UAE customs appear in Box 6; correct them in Box 7.
6. **Classify each purchase.** Keep only input tax on costs used for taxable supplies, backed by a tax invoice (or import documents), and paid or intended to be paid within six months of the agreed payment date. Strip out blocked items: entertainment of non-employees, motor vehicles available for personal use, and free personal benefits to staff. Conservative defaults where the facts are missing: an item whose blocked status is unknown is treated as blocked; a purchase whose VAT status is unknown is not recovered; if the Emirate of a sale is unknown, ask before filing.
7. **Deal with credit notes and past errors.** Credit notes reduce the relevant box. Where a past return understated the payable tax: an error of AED 10,000 or less in tax is corrected in the return; above that, file a voluntary disclosure within 20 business days. An error in the business's favour (tax overstated) may be corrected by voluntary disclosure but need not be ([Cabinet Decision No. 74 of 2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2074%20of%202023%20on%20Executive%20Regulation%20of%20Federal%20Decree-Law%20No.%2028%20of%202022%20on%20Tax%20Procedures%20-%20For%20Publishing.pdf)).
8. **Compute the return.** Box 12 (due tax) less Box 13 (recoverable tax) gives Box 14. If Box 14 is negative, choose a refund or carry the excess forward, noting the five-year limit.
9. **File and pay** through the FTA's online portal by the 28th day. Keep the records for at least five years.

## Rates, thresholds and periods for 2026

### Registration ([VAT Law, Articles 13 and 17](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Executive Regulation, Articles 7 and 8](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

| Test | Rule |
| --- | --- |
| Mandatory Registration Threshold | AED 375,000 |
| When it bites | A person with a place of residence in the UAE or another GCC implementing state must register where the supplies counted under Article 19 in the previous 12 months **exceeded** the threshold, or are expected to exceed it in the next 30 days |
| Application deadline | Within 30 days of becoming required to register |
| Effective date set by the FTA | Look-back test: the first day of the month after the month in which the person became required to register. Look-forward test: the date there were reasonable grounds to expect the threshold to be exceeded. Either way, whether or not the person applies |
| Non-resident | Must register if making supplies in the UAE where no other person is obliged to pay the VAT; registered from the date it started making supplies; no threshold |
| Voluntary Registration Threshold | AED 187,500 |
| Voluntary test | Supplies **or taxable expenses** in the previous 12 months exceeded the voluntary threshold (shown at the end of any month), or are expected to in the next 30 days. "Taxable expenses" means standard-rated expenses incurred in the UAE by a person with a place of residence in the UAE. The person must also prove it carries on a business in the UAE and intends to make taxable (or equivalent) supplies. Registration takes effect from the first day of the month after the application, or an earlier agreed date |
| Late registration | VAT is due on all taxable supplies and imports made before registering |

"Exceeded" means more than the threshold; supplies of exactly AED 375,000 do not trigger mandatory registration.

### Rates ([VAT Law, Articles 3, 45 and 46](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Executive Regulation, Articles 31 and 42](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

| Treatment | Supplies |
| --- | --- |
| Standard rate 5% | Every taxable supply and import that is not zero-rated or exempt |
| Zero rate 0% (input tax recoverable) | Exports of goods and services outside the GCC implementing states (on the Executive Regulation's conditions); international transport of passengers and goods; qualifying means of transport and related goods and services; investment precious metals; first supply of a residential building within 3 years of completion (sale or lease); first supply of buildings designed for charities and of buildings converted to residential; crude oil and natural gas; qualifying education; qualifying preventive and basic healthcare |
| Exempt (no VAT, related input tax not recoverable) | Financial services specified in the Executive Regulation (including margin-based services, and life insurance and its reinsurance); residential buildings other than the zero-rated first supplies, but only where the lease is more than 6 months or the tenant holds a UAE ID card (Executive Regulation Article 43(1)); bare land; local passenger transport in a qualifying means of transport (Article 45, not pleasure trips) |
| Standard rate, although property | Commercial property: "Supplies of commercial property" are listed among the Box 1 standard-rated supplies in the [FTA VAT Returns User Guide](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf), so a commercial lease is standard-rated |
| Not a supply | The transfer of the whole or an independent part of a business to a taxable person to continue it; vouchers unless the consideration exceeds their face value |

Salaries, dividends, loan principal and similar money movements are not supplies and are left off the return.

### Tax period and deadline ([Executive Regulation, Articles 62 and 64](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

- The standard tax period is three calendar months, ending on the date the FTA sets. The FTA may assign a shorter (for example monthly) or longer period, and a business on the standard period may ask for its quarters to end in a month it chooses.
- The return must be received by the FTA no later than the 28th day after the end of the tax period, "or by such other date as directed by the Authority", and the payable tax must be received by the same date.
- A deregistered person files a final return for its last period.

### Excess recoverable tax ([VAT Law, Article 74](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Tax Procedures Law, consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%2028%20of%202022%20-%20publishing%2003%2012%202025.pdf))

- The FTA first offsets excess recoverable tax against tax and penalties due.
- If no refund is requested, the excess is carried forward for no more than five years from the end of the tax period in which it arose. After that the right lapses and it cannot be used to settle any liability.
- A refund application must be made within five years from the end of the relevant tax period. Transitional rule: where that five-year period had already run out, the taxpayer may still apply for the refund, or use the balance, within one year from 1 January 2026. A voluntary disclosure linked to such a refund application must be made within two years of the application. Check the facts before relying on it.

## The VAT201 return, box by box ([FTA VAT Returns User Guide](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf); [Executive Regulation, Article 64(5)](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

The box layout is from the FTA's returns user guide (August 2021 edition, the latest found on tax.gov.ae). The portal form is the final word if it differs.

| Box | What goes in it |
| --- | --- |
| 1a-1g | Standard-rated supplies, net amount and 5% VAT, split by Emirate: Abu Dhabi, Dubai, Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah, Fujairah. A business with fixed establishments in the UAE reports in the Emirate of the fixed establishment most closely connected to the supply; a business not established in the UAE reports in the Emirate where the supply was received |
| 2 | Tax refunds given to tourists under the Tax Refunds for Tourists Scheme. Prepopulated for enrolled retailers; not editable |
| 3 | Supplies subject to the reverse charge: net value and output VAT on services (and goods not declared through UAE customs) received from non-resident suppliers, and on domestic reverse-charge supplies |
| 4 | Zero-rated supplies, net value only |
| 5 | Exempt supplies, net value only |
| 6 | Goods imported into the UAE through customs where the import VAT is paid on the return. Prepopulated from customs declarations at 5% |
| 7 | Adjustments to goods imported (Box 6 missing or wrong, or imports that are not at 5%) |
| 8 | Totals of the output boxes (automatic) |
| 9 | Standard-rated expenses: net value and recoverable VAT only |
| 10 | Supplies subject to the reverse charge: the recoverable part of the VAT declared in Boxes 3, 6 and 7 |
| 11 | Totals of the input boxes (automatic) |
| 12 | Total value of due tax for the period |
| 13 | Total value of recoverable tax for the period |
| 14 | Payable tax for the period: Box 12 less Box 13 |
| 15 | Whether you request a refund of an excess |

- Credit notes issued reduce Box 1; credit notes received reduce Box 9.
- The output-side "Adjustment" column is only for bad debt relief claimed by the business and adjustments for sales of taxable commercial property. The input-side "Adjustment" column is only for bad debt relief claimed by a supplier, the annual input tax apportionment adjustment and capital asset scheme adjustments.
- Supplier bad debt relief ([VAT Law, Article 64(2)](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf)): the buyer must reduce its recoverable input tax only when all of these hold: the supplier has written off the debt, reduced its output tax and notified the buyer; the buyer deducted the input tax; and the consideration has been unpaid, in full or in part, for over 6 months. The reduction equals the tax on the amount written off.
- Separately, input tax is claimable only for consideration paid, or intended to be paid within six months after the agreed payment date ([Executive Regulation, Article 54(1)-(2)](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf)). If the business does not intend to pay, it should not claim the input tax.
- Past errors of AED 10,000 or less in tax may be corrected in the return for the period in which they are found.

## Reverse charge on imports and services ([VAT Law, Article 48](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [FTA VAT Returns User Guide](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf))

- A taxable person that imports goods or services for its business is treated as making a taxable supply to itself and accounts for the VAT.
- **From 1 January 2026** the business no longer issues a tax invoice to itself for a reverse charge (Decree-Law No. 16 of 2025 amended Article 48(1)). It still keeps the supplier's invoice: input tax on imported services is recoverable only if it "receives and retains invoices" for them (Article 55(1)(a)).
- Services from a supplier with no UAE place of residence and no UAE VAT on the invoice: output VAT in Box 3; recoverable part in Box 10. For a fully taxable business the net effect is nil.
- Goods cleared through UAE customs by a registrant: prepopulated in Box 6 at 5%; corrections in Box 7; recoverable part in Box 10.
- A supplier that is UAE-registered (TRN on the invoice) charges UAE VAT in the normal way: Box 9, not Box 3.
- A domestic reverse charge applies to crude or refined oil, natural gas and pure hydrocarbons between registrants (Article 48(3)); refer.

## Input tax recovery and blocked items ([VAT Law, Articles 54, 54 (bis) and 55](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Executive Regulation, Articles 53 and 54](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

**Recoverable.** Input tax on goods and services used, or intended to be used, for taxable supplies (including zero-rated supplies), and for supplies outside the UAE that would be taxable if made here. Conditions:

- the business holds the tax invoice (or import documents), or the other document the law allows;
- it has paid the consideration, or intends to pay it within six months after the agreed payment date;
- where the tax invoice must be (or was) an electronic invoice, it is kept in the e-invoicing system;
- input tax not claimed in the first possible period may be claimed in the next one.

**Tax evasion chains (from 1 January 2026).** The FTA must reject a deduction if the supply was part of a chain linked to tax evasion and the business knew. It may reject it if the business should have known; a business is treated as should-have-known if it did not verify the validity and integrity of the supplies it received as the FTA requires (VAT Law Article 54 (bis)).

**Blocked (not recoverable) for a business that is not a listed government entity:**

| Item | Rule |
| --- | --- |
| Entertainment of non-employees | Hospitality of any kind for customers, potential customers, officials, shareholders, owners or investors: accommodation, food and drinks not provided in the normal course of a meeting, access to shows or events, pleasure trips. Food and drink provided in the normal course of a meeting are not "entertainment" |
| Motor vehicles | Purchased, rented or leased for the business **and available for personal use by any person**. A motor vehicle is a road vehicle designed or adapted for no more than 10 people including the driver; trucks, forklifts and hoists are not motor vehicles. Not treated as available for private use: a licensed taxi, a registered emergency vehicle, a vehicle used in a rental business |
| Free goods or services for employees' personal benefit (including entertainment) | Blocked unless: required by UAE (or free zone) labour law; or a contractual obligation or documented policy (see the 1 October 2026 change below); or health insurance (including enhanced) for employees and family up to one spouse and three children under 18; or the provision is itself a deemed supply |

**Change from 1 October 2026** ([Cabinet Decision No. 149 of 2026](https://mof.gov.ae/wp-content/uploads/2026/09/Cabinet-Decision-No.-149-of-2026-Amending-Certain-Provisions-of-The-Executive-Regulation-of-VAT-EN.pdf)): the labour-law exception excludes staff accommodation unless the Ministry of Human Resources and Emiratisation makes it mandatory; the contract-or-policy exception applies "in accordance with the cases and conditions specified by the Authority" (until 30 September 2026 the goods or services must be provided "in order that they may perform their role" and this must be shown to be normal business practice, [Executive Regulation as at October 2025](https://mof.gov.ae/wp-content/uploads/2025/10/Cabinet-Decision-No.-52-of-2017-of-the-Executive-Regulation-of-the-Federal-Decree-Law-No.-8-of-2017-on-Value-Added-Tax-and-its-amendments.pdf)). A new rule also blocks input tax on a supply above a value set by a Minister's decision where it is paid, or intended to be paid, in cash. We did not find that decision on the FTA or MoF sites: check before relying on either side of it.

**Partial exemption.** A business with exempt supplies apportions input tax that relates to both taxable and exempt supplies. A new apportionment method set by Cabinet Decision No. 149 of 2026 applies from the first tax year beginning after 1 October 2027. Refer apportionment cases out.

## Deemed supplies and gifts ([VAT Law, Article 12](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Executive Regulation, Article 5](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

- Business goods given away free can be a deemed supply only if input tax was recovered on them. No input tax recovered, no deemed supply.
- Goods given "as samples or commercial gifts" are not a deemed supply where their value to each recipient in a 12-month period does not exceed AED 500.
- The total output tax on all deemed supplies is also relieved up to AED 2,000 per supplier in a 12-month period; output tax above that is payable.
- A deemed supply is reported in Box 1 and needs a tax invoice (delivered to the recipient, or kept on file if there is none).

## Designated Zones ([Executive Regulation, Article 51](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [VAT Law, Articles 51 and 52](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf))

- A Designated Zone is a zone named by Cabinet decision that is fenced, has customs controls and has internal procedures for goods. Only then is it treated as outside the UAE. Not every free zone is a Designated Zone: check the current Cabinet list.
- Services supplied in a Designated Zone are treated as supplied inside the UAE: 5% as normal. Water and energy too.
- Goods moved between Designated Zones are not taxed if they are not released, used or altered in transit and move under customs suspension.
- Goods supplied within a Designated Zone to be consumed there are supplied inside the UAE, unless incorporated into another good in the same zone that is not consumed, or evidenced as removed from the UAE or imported with VAT paid.
- A person established or registered in a Designated Zone is treated as resident in the UAE.
- Goods movements into, out of and between zones are referred out.

## Tax invoices and simplified invoices ([VAT Law, Articles 65, 67 and 69](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Executive Regulation, Article 59](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

- A registrant issues a tax invoice within 14 days of the date of supply. Amounts in a foreign currency are converted to AED at the UAE Central Bank rate on the date of supply.
- **Full tax invoice:** the words "Tax Invoice"; supplier's name, address and TRN; recipient's name, address and TRN if registered; sequential or unique number; date of issue; date of supply if different; description; unit price, quantity, rate and amount in AED for each item; any discount; gross amount in AED; VAT in AED with the exchange rate used; and, for a reverse-charge supply, a statement that the recipient must account for the tax with the legal reference.
- **Simplified tax invoice** (the words "Tax Invoice", supplier name, address and TRN, date, description, total and VAT in AED) is allowed where the customer is not registered, or the customer is registered and the consideration does not exceed AED 10,000. It is not allowed for reverse-charge supplies.
- A wholly zero-rated supply needs no tax invoice if records are sufficient.
- Buyer-created ("Tax Invoice raised by buyer") invoices are allowed if the buyer is registered and both parties agree in writing.
- A tax credit note must show the words "Tax Credit Note" (the exact wording set by Cabinet Decision No. 149 of 2026 from 1 October 2026).
- Where the business is within the e-invoicing system, tax invoices must be issued and transmitted as electronic invoices ([VAT Law, Article 65(5)](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf)).

## Profit margin scheme ([Executive Regulation, Article 29](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [FTA Profit Margin Scheme Guide VATGPM1](https://tax.gov.ae/Datafolder/Files/Pdf/2026/Guide/Profit%20Margin-Scheme-EN-02-01-2026-re.pdf))

- Available for second-hand goods, antiques (over 50 years old) and collectors' items that have already borne VAT, bought from a non-registrant or from a seller who used the margin scheme; also for goods on which input tax was blocked under Executive Regulation Article 53.
- VAT is charged on the margin (selling price less purchase price), which is treated as VAT-inclusive.
- Not available if the invoice for the sale shows an amount of VAT.
- The seller keeps a stock book and purchase invoices (self-issued where bought from a non-registrant) and issues a tax invoice stating that VAT was charged on the margin, without showing the VAT amount.
- The purchase price includes costs or fees incurred to buy the goods. From 1 October 2026 it includes only those costs or fees whose input tax is not recoverable, which narrows the purchase price and so can increase the margin.
- The business must notify the FTA that it uses the scheme; failing to is a penalty of AED 2,500.

## Changes in 2026 ([VAT Law, consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Penalties decision, consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Cabinet%20Decision%20No.%2040%20of%202017%20and%20its%20amendments%20-%20publishing%2011%202025.pdf); [Cabinet Decision No. 149 of 2026](https://mof.gov.ae/wp-content/uploads/2026/09/Cabinet-Decision-No.-149-of-2026-Amending-Certain-Provisions-of-The-Executive-Regulation-of-VAT-EN.pdf))

| Effective | Measure | What changed |
| --- | --- | --- |
| 1 January 2026 | Federal Decree-Law No. 16 of 2025 (VAT) | No self-invoice for the reverse charge; FTA may or must deny input tax in tax-evasion chains; excess recoverable tax lapses if not used or reclaimed within five years |
| 1 January 2026 | Federal Decree-Law No. 17 of 2025 (Tax Procedures) | Refund applications within five years of the relevant tax period; a one-year window from 1 January 2026 for balances already older than that |
| 14 April 2026 | Cabinet Decision No. 129 of 2025 | New administrative penalties table for tax procedures and VAT violations, amending Cabinet Decision No. 40 of 2017 (see "Penalties") |
| 1 October 2026 | Cabinet Decision No. 149 of 2026 | Composite supply rule (components that are interconnected and cannot be separated are one supply, taxed by its principal component); employee-benefit exceptions; cash-payment block; profit margin purchase price; capital asset wording; "Tax Credit Note" wording; healthcare goods zero rating |
| First tax year beginning after 1 October 2027 | Cabinet Decision No. 149 of 2026 | New input tax apportionment method, including for government entities and charities |

## E-invoicing timeline ([Ministerial Decision No. 244 of 2025](https://mof.gov.ae/wp-content/uploads/2025/09/Ministerial-Decision-No.-244-of-2025-on-the-Implementation-of-the-Electronic-Invoicing-System.pdf); [Ministerial Decision No. 66 of 2026](https://mof.gov.ae/wp-content/uploads/2026/05/Ministerial-Resolution-No.-66-of-2026-Amending-Certain-Provisions-of-Ministerial-Resolution-No.-244-of-2025-Regarding-the-Implementation-of-the-Electronic-Invoicing-System-En-20260514.pdf); [Cabinet Decision No. 106 of 2025](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Cabinet%20Decision%20No.%20106%20of%202025.pdf))

| Who | Appoint an Accredited Service Provider by | Implement by |
| --- | --- | --- |
| Pilot programme (by invitation, written agreement) | n/a | Pilot starts 1 July 2026 |
| Anyone, voluntarily | n/a | From 1 July 2026 |
| Revenue of AED 50,000,000 or more | 30 October 2026 (moved from 31 July 2026 by Ministerial Decision No. 66 of 2026) | 1 January 2027 |
| Revenue below AED 50,000,000 | 31 March 2027 | 1 July 2027 |
| Government entities | 31 March 2027 | 1 October 2027 |

- After these phases, every person or government entity subject to the system must appoint a provider and implement it.
- "Revenue" is gross income in the most recent accounting period per the financial statements.
- Business-to-consumer transactions are outside the system until the Minister decides otherwise; a business that only sells to consumers is not yet subject to it.
- Penalties (Cabinet Decision No. 106 of 2025, in force from 15 October 2025; not applied to voluntary users): failure to implement, including failure to appoint a provider on time, AED 5,000 for each month or part of a month of delay; failure to issue and transmit an electronic invoice or credit note AED 100 each, up to AED 5,000 per calendar month; failure to notify a system failure AED 1,000 per day; failure to notify the accredited service provider of changes to the data registered with the FTA AED 1,000 per day.

## Boundaries and exceptions ([Executive Regulation, Articles 7, 31, 53, 57 and 59](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [VAT Law, Articles 13, 17 and 48](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf))

| Question | Answer | Boundary |
| --- | --- | --- |
| Supplies of exactly AED 375,000 in 12 months | Not required to register | Mandatory only when supplies "exceeded" the threshold |
| No sales yet, taxable expenses above AED 187,500 | May register voluntarily | Expenses count for voluntary, not mandatory, registration |
| Consulting for a foreign company with no GCC residence whose director visits Dubai for 10 days, not connected to the work; advice not about UAE real estate or goods in the UAE | Can be zero-rated | "Outside the State" means present for less than 30 days and not effectively connected with the supply; all Article 31(1)(a) conditions must hold |
| Valuation of a warehouse in Dubai for a foreign client | Standard-rated | Directly connected with real estate in the UAE |
| Same, but the services are received in the UAE by the foreign client's UAE staff and that person could not fully recover VAT | Standard-rated | Executive Regulation Article 31(3) anti-avoidance |
| Invoice to a registered customer for AED 10,000 | Simplified invoice allowed | Allowed where consideration "does not exceed" AED 10,000 |
| Same for AED 10,001 | Full tax invoice | Above the limit |
| Past error of exactly AED 10,000 in tax | Correct in the return | Voluntary disclosure required only above AED 10,000 |
| Pool car used by sales staff, taken home at night | Input tax blocked | Available for personal use |
| Pickup truck or forklift | Not a "motor vehicle"; recoverable if used for taxable supplies | The definition excludes trucks, forklifts and hoists |
| Client lunch | Blocked | Hospitality for non-employees |
| Tea and sandwiches in a client meeting | Not entertainment; recoverable | Food and drink in the normal course of a meeting |
| Building costing AED 5,000,000 or more excluding VAT, on which VAT is payable, life 10 years or more | Capital asset scheme | Refer |
| Supplier invoice unpaid 7 months after the supply; supplier has written it off, reduced its output tax and notified the buyer | Buyer reduces its recoverable input tax by the tax on the amount written off (input-side Adjustment column) | VAT Law Article 64(2): all conditions, including over 6 months unpaid |
| Invoice not yet paid and the business does not intend to pay within six months of the agreed date | Do not claim the input tax | Executive Regulation Article 54(1)-(2) |

## Worked cases ([VAT Law, consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Executive Regulation, consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [FTA VAT Returns User Guide](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf))

**Case 1: mandatory registration.** A Dubai mainland trading LLC, not registered, has taxable supplies of AED 390,000 in the 12 months to 30 June 2026. That exceeds AED 375,000, so it must apply within 30 days of becoming required to register. The FTA registers it from the first day of the month after the month in which it became required to register, whether or not it applies, and it owes VAT on its taxable supplies from that date. A late application is a penalty of AED 10,000.

**Case 2: voluntary registration.** A start-up has no sales yet but taxable expenses of AED 200,000 in the last 12 months. That exceeds AED 187,500, so it may register voluntarily and recover input tax. It is not required to register.

**Case 3: reverse charge on software.** A registered Dubai consultancy pays a US software company AED 3,672 for a subscription. The supplier has no UAE TRN and charges no VAT. Box 3: amount AED 3,672, VAT 3,672 x 5% = AED 183.60. Box 10: the same amounts, because the consultancy makes only taxable supplies. Net effect nil. For a supply received after 1 January 2026 no self-invoice is issued; the supplier's invoice is kept.

**Case 4: a quarterly return.** Same consultancy, quarter 1 July to 30 September 2026:

| Line | Amount (AED) | VAT (AED) | Box |
| --- | --- | --- | --- |
| Services to Dubai clients | 400,000 | 20,000 | 1b |
| Services to a foreign client outside the UAE (zero-rated) | 100,000 | 0 | 4 |
| Software from US supplier (Case 3) | 3,672 | 183.60 | 3 and 10 |
| Local business purchases with tax invoices | 200,000 | 10,000 | 9 |
| Client dinner (blocked, not reported) | 1,200 | 0 | none |

Box 12 = 20,000 + 183.60 = 20,183.60. Box 13 = 10,000 + 183.60 = 10,183.60. Box 14 = 20,183.60 - 10,183.60 = 10,000. The return and AED 10,000 must reach the FTA by 28 October 2026.

**Case 5: gift limit.** In the 12 months to 31 August 2026 a business gives commercial gifts of goods on which it recovered input tax. One customer receives goods costing AED 400: no deemed supply (not above AED 500). Another receives goods costing AED 700: that is a deemed supply reported in Box 1, subject to the AED 2,000 relief on total output tax on deemed supplies in the 12 months.

**Case 6: correcting an error.** In September 2026 a business finds it under-declared output tax of AED 12,000 in the quarter to 31 March 2026. That is above AED 10,000, so it files a voluntary disclosure within 20 business days of finding the error. If the difference had been AED 8,000 it would correct it in the next return instead.

## When to refuse or refer

- **Tax Group members:** consolidation and intra-group supplies need a registered tax agent.
- **Partial exemption:** any business with more than incidental exempt supplies (residential property, margin-based financial services) needs apportionment of mixed input tax, and a new method applies from the first tax year beginning after 1 October 2027.
- **Designated Zone goods movements:** goods entering, leaving or moving between Designated Zones.
- **Capital asset scheme:** assets costing AED 5,000,000 or more (excluding VAT), on which VAT is payable, with a useful life of 10 years or more for buildings, 5 years or more otherwise ([Executive Regulation, Article 57](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf)).
- **Oil, gas and hydrocarbons** between registrants (domestic reverse charge) and other special reverse charges.
- **Tourist Refund Scheme** operators or retailers.
- **Complex profit margin scheme** cases (mixed stock, second-hand vehicles, partial exports).
- **Tax evasion chain notices** from the FTA, audits, objections and reconsideration requests.
- **Penalties for violations that began before 14 April 2026:** the decision text we found does not say whether the new table applies to them; check with the FTA.
- **Cash-payment input tax block** from 1 October 2026, until the Minister's decision setting the value is found.
- **GCC implementing-state supplies** (goods or services to or from other GCC countries).

## Filing and payment

### Returns and payment ([Executive Regulation, Article 64](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf))

- File the VAT201 return online through the FTA's portal for every tax period, including nil periods.
- The return and the payment must reach the FTA no later than the 28th day after the end of the tax period, or such other date as the FTA directs (for a quarter ending 30 September 2026, by 28 October 2026). There is no separate annual VAT return.
- For the late payment penalty, tax shown in a voluntary disclosure is due 20 business days after submission, and tax in an FTA assessment 20 business days after receipt.

### Returns being filed now for earlier periods ([VAT Law, consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf))

- A tax period that ended before 1 January 2026 follows the VAT Law before Decree-Law No. 16 of 2025, including the self-invoice requirement for reverse-charge supplies in that period. Correct past errors on the rules of the period concerned.
- Penalties for a return or payment due before 14 April 2026 may fall under the earlier table (Cabinet Decision No. 49 of 2021); check.
- Excess recoverable tax that arose in earlier periods is now subject to the five-year limit; check the age of any carried-forward balance.

### Penalties from 14 April 2026 ([Cabinet Decision No. 40 of 2017 as amended by Cabinet Decision No. 129 of 2025](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Cabinet%20Decision%20No.%2040%20of%202017%20and%20its%20amendments%20-%20publishing%2011%202025.pdf))

| Violation | Penalty (AED) |
| --- | --- |
| Late registration application | 10,000 |
| Late deregistration application | 1,000 on the same date each month, up to 10,000 |
| Late return | 1,000 first time; 2,000 if repeated within 24 months |
| Late payment | Monthly penalty at 14% per annum for each month or part of a month on the unpaid tax, from the day after the due date and on the same date each month |
| Incorrect return | 500, unless corrected within the filing deadline or by a voluntary disclosure that does not change the tax due |
| Voluntary disclosure of an error | 1% of the tax difference per month or part of a month, from the day after the original return's due date to the disclosure |
| No voluntary disclosure before notice of audit | Fixed 15% of the tax difference plus 1% per month or part of a month |
| Failure to keep records | 10,000; 20,000 if repeated within 24 months |
| Failure to give records in Arabic when asked | 5,000 |
| Failure to notify changes to the tax record | 1,000; 5,000 if repeated within 24 months |
| Failure to display VAT-inclusive prices | 5,000 |
| Failure to notify use of the profit margin scheme | 2,500 |
| No tax invoice, credit note or alternative document on time; electronic invoice rules not met | 2,500 for each detected case |
| Designated Zone goods conditions not met | Higher of 50,000 or 50% of the tax |
| Failure to account for import VAT | 50% of the unpaid or undeclared tax |

## Record keeping ([VAT Law, Article 78](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Executive Regulation, Article 71](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [Cabinet Decision No. 74 of 2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2074%20of%202023%20on%20Executive%20Regulation%20of%20Federal%20Decree-Law%20No.%2028%20of%202022%20on%20Tax%20Procedures%20-%20For%20Publishing.pdf))

- Keep: records of all supplies and imports; tax invoices and credit notes issued and received (or alternative documents); records of goods and services used for non-business purposes and of purchases where input tax was not deducted; records of exports; records of adjustments and corrections; and a tax record of due tax, reverse-charge tax, recoverable tax and corrections.
- Keep them for five years following the tax period they relate to; records about real estate for 15 years after the end of the tax period. The FTA can ask for them in Arabic.

## Completion checklist ([Executive Regulation, consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [Cabinet Decision No. 74 of 2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2074%20of%202023%20on%20Executive%20Regulation%20of%20Federal%20Decree-Law%20No.%2028%20of%202022%20on%20Tax%20Procedures%20-%20For%20Publishing.pdf))

- [ ] Registration status, TRN, effective date and tax period confirmed from the certificate.
- [ ] Mandatory (AED 375,000, more-than) or voluntary (AED 187,500) test applied if not registered.
- [ ] Each sale classified standard, zero, exempt or not a supply; export conditions evidenced.
- [ ] Box 1 split by Emirate.
- [ ] Reverse-charge services in Box 3 and Box 10; customs imports checked against Box 6, corrections in Box 7.
- [ ] Input tax backed by tax invoices, paid or to be paid within six months; blocked items removed.
- [ ] Gifts and other deemed supplies checked against the AED 500 and AED 2,000 limits.
- [ ] Credit notes and past errors dealt with; voluntary disclosure if tax was understated by more than AED 10,000.
- [ ] Box 12 less Box 13 equals Box 14; refund or carry-forward decided; age of carried-forward excess checked.
- [ ] Filed and paid by the 28th day after the period end.
- [ ] E-invoicing deadline identified from last year's revenue.
- [ ] Changes effective 1 October 2026 applied to supplies from that date.
- [ ] Records kept for five years (15 years for real estate).

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
