---
name: be-vat-return
description: "Preparing and filing the Belgian periodic VAT return (periodieke btw-aangifte / déclaration périodique TVA) for tax year 2026: who files, the 21%, 12%, 6% and 0% rates (hotels and campsites 12% from 1 March 2026), monthly or quarterly filing (EUR 2,500,000 test, EUR 50,000 intra-EU test), the 20th and 25th deadlines and the 2026 calendar, Intervat, which grid each transaction goes in, domestic reverse charge for construction (KB nr. 1 art. 20) and other customer-pays cases, the annual client listing (over EUR 250 per customer, before 31 March) and the intra-EU listing, structured B2B e-invoicing from 1 January 2026 and its fines, the small-business exemption at EUR 25,000 with its 10% tolerance and the rises to EUR 26,000-30,000 from 2027, the EU small-business scheme (EUR 100,000), refunds and the VAT provision account, capital goods, late interest of 8% for 2026 and the fines in KB nr. 41 and 44. Trigger on: Belgian VAT return, btw-aangifte invullen, rooster 71, Intervat, klantenlisting, intracommunautaire opgave, medecontractant, verlegging van heffing, btw-boete, vrijstellingsregeling kleine ondernemingen, franchise TVA, vervangende aangifte, Belgian VAT. Out of scope: Peppol set-up (belgium-einvoice), bookkeeping (belgium-bookkeeping), income tax (be-income-tax, be-corporate-tax)."
version: 2.4
jurisdiction: BE
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
  - eu-vat-directive
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium VAT and the periodic VAT return (btw-aangifte / déclaration TVA): the law, preparing and filing, tax year 2026 v2.4

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Belgium.

**What this skill does.** It takes a Belgian business from its invoices and bank lines to a filed periodic VAT return: which grid each transaction goes in, the reverse-charge cases, the listings that go with the return, the deadlines and what a late or wrong return costs. It also sets out the law layer of Belgian VAT for 2026: who is in, the rates, the small-business exemption, refunds and capital goods. Figures come from the VAT Code (Wetboek van de belasting over de toegevoegde waarde, "WBTW", Law of 3 July 1969) and its Royal Decrees (KB nr. 1, 20, 23, 41, 44 and 50) in the official coordination on FisconetPlus, from amending laws in the Belgisch Staatsblad, and from FOD Financiën pages.

**Sibling skills.** [belgium-einvoice](belgium-einvoice.md) covers Peppol and invoice formats. [belgium-bookkeeping](belgium-bookkeeping.md), [be-income-tax](be-income-tax.md), [be-corporate-tax](be-corporate-tax.md) and [be-cross-border](be-cross-border.md) cover the rest. Load `vat-workflow-base` and `eu-vat-directive` alongside.

## Who this applies to

- **Taxable persons.** Anyone who carries on an economic activity and supplies goods or services in Belgium for consideration. Companies, sole traders and foreign businesses supplying in Belgium are all in.
- **Who files.** Every taxable person with a right to deduct files a periodic return (WBTW art. 53 § 1, first paragraph, 2°). Monthly is the rule; quarterly is an option (KB nr. 1 art. 17).
- **Who does not file.** A business under the small-business exemption (art. 56bis to 56undecies), under the special scheme for farmers, or making only art. 44 exempt supplies with no right to deduct (FOD Financiën, periodic return page). From 2026 a small-business-exemption business still reports its previous year's Belgian turnover, or 0.00, through Intervat before 31 March (FOD Financiën, annual client listing page). It still files the start, change and end-of-activity declarations (art. 53 § 1, second paragraph).
- **Small-business exemption (vrijstellingsregeling / franchise).** A business established in Belgium whose annual turnover in Belgium does not exceed EUR 25,000 may choose not to charge VAT (art. 56ter § 1). The limit is cut pro rata for a business that starts during the year, by the days from 1 January to the start date. Joint owners count their turnover together; spouses with separate activities count separately. The business must notify the VAT administration in advance. It cannot deduct input VAT (art. 56bis § 4).
- **Who cannot use the exemption.** VAT units; businesses that regularly do construction work (except some services by individuals through platforms), businesses that must issue a till receipt from a registered cash system, and dealers in scrap and waste (art. 56bis § 2). The exemption also never covers art. 8 transactions, intra-EU supplies of new means of transport, margin-scheme supplies (art. 58 §§ 1-2), undeclared or unlawful transactions, or hotel-type furnished accommodation under art. 44 § 3, 2°, a), third dash (except some supplies by individuals under art. 50 § 4) (art. 56bis § 3).
- **Crossing the limit.** If the year's turnover exceeds EUR 25,000 by 10% or less (up to EUR 27,500), the business keeps the exemption for that year. If it exceeds it by more than 10%, the exemption ends from that moment. A business that exceeded the limit in the previous year cannot use the exemption for the following calendar year (art. 56decies § 1).
- **Limits already legislated for later years.** EUR 26,000 for 2027, EUR 27,000 for 2028, EUR 28,000 for 2029, EUR 29,000 for 2030 and EUR 30,000 from 2031 (art. 56ter § 1 as replaced by art. 26 of the Law of 23 September 2026, in force 1 January 2027).
- **EU small-business scheme.** A business established in another EU state can use the Belgian exemption if its EU turnover is at most EUR 100,000 and its Belgian turnover at most EUR 25,000. It notifies its home state, which issues a number with the suffix "EX" (art. 56ter § 2). It loses the scheme once EU turnover exceeds EUR 100,000 (art. 56decies § 2). It does not register or file Belgian returns for the exempt supplies (art. 56septies § 1). A Belgian business can use another state's exemption after prior notice to the Belgian administration and gets a Belgian number with the suffix "EX" (art. 56quater).
- **Quarterly filers.** Allowed if annual turnover excluding VAT for the whole economic activity is at most EUR 2,500,000, and the business does not have to file the intra-EU listing monthly (KB nr. 1 art. 17 § 2, text in force from 10 January 2026; the second test was removed by the KB of 17 December 2025, art. 6). The second test the FOD Financiën page still lists (EUR 250,000 of energy products, mobile phones, computers and motor vehicles) is gone from the decree since 10 January 2026; follow the decree.
- **Refer, do not prepare here.** Flat-rate scheme (art. 56, KB nr. 2), farmers' special scheme (art. 57), travel agents, margin schemes, VAT units, mixed taxable and exempt activity needing a pro rata, real estate sales under VAT, a non-resident acting through a fiscal representative, a bankrupt estate (annual return by the trustee, KB nr. 1 art. 17 § 5). A question about income tax goes to [be-income-tax](be-income-tax.md) or [be-corporate-tax](be-corporate-tax.md).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 21% | 2026 | KB nr. 20 art. 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Reduced rate, Table A (food, water, medicines and medical devices, books and newspapers, passenger transport, cultural and sport admission, work on private homes under conditions, and other listed items) | 6% | 2026 | KB nr. 20 art. 1, a) and Table A, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Reduced rate, Table B (restaurant and catering services excluding drinks; furnished accommodation and campsites from 1 March 2026; other listed items) | 12% | 2026 | KB nr. 20 art. 1, b) and Table B, sections I and IV, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Zero rate, Table C (certain periodical publications and other listed items) | 0% | 2026 | KB nr. 20 art. 1, c) and Table C, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Hotels and campsites, before / from 1 March 2026 | 6% / 12% | 2026 | KB nr. 20 Table B, IV (in Table B from 01.03.2026), https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Plant-protection products, before / from 1 March 2026 | 12% / 21% | 2026 | KB nr. 20 Table B, III (repealed from 01.03.2026), https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Heat pumps for heating supplied and installed in, on or next to homes, 1 January 2026 to 31 December 2030, for end consumers and private dwellings; not when combined with a non-electric heater on the same system | 6% | 2026 | KB nr. 20 art. 1quater/1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Small-business exemption, annual turnover in Belgium | EUR 25,000 | 2026 | WBTW art. 56ter § 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6191791d-e4d1-4829-b8f1-56c7a6892136 |
| Tolerance: exemption kept for the year if the limit is exceeded by no more than | 10% (EUR 27,500) | 2026 | WBTW art. 56decies § 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/83f1a474-d23d-446b-ac69-284f8909b300 |
| Small-business exemption limit for 2027 / 2028 / 2029 / 2030 / 2031 onwards | EUR 26,000 / 27,000 / 28,000 / 29,000 / 30,000 | 2027-2031 | Law of 23 September 2026 art. 26-27, https://www.ejustice.just.fgov.be/eli/wet/2026/09/23/2026007237/staatsblad |
| EU small-business scheme: EU-wide turnover cap | EUR 100,000 | 2026 | WBTW art. 56ter § 2, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6191791d-e4d1-4829-b8f1-56c7a6892136 |
| Quarterly returns allowed up to annual turnover (whole activity, excluding VAT) | EUR 2,500,000 | 2026 | KB nr. 1 art. 17 § 2, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c69c7ee9-8e6d-48da-b9f7-c23cb025a777 |
| Quarterly intra-EU listing allowed while intra-EU supplies of goods in the quarter and each of the four before stay at or below | EUR 50,000 | 2026 | KB nr. 50 art. 5 § 1 and art. 11 § 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/90c85f66-9e8b-48bc-9032-ce1f7db88872 |
| Annual client listing: customers supplied for a total of more than | EUR 250 a year, excluding VAT | 2026 | FOD Financiën, annual client listing, https://financien.belgium.be/nl/ondernemingen/btw/aangifte/jaarlijkse_klantenlisting |
| Replacement return when no return is filed: highest grid 71 of the previous 12 months, at least | EUR 2,100 | 2026 | WBTW art. 53 § 1ter, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/773cb22d-053e-4d4d-ae1f-7ddadab87d78 |
| Input VAT on road vehicles and their costs, maximum deduction | 50% | 2026 | WBTW art. 45 § 2, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/58a466d6-c626-4369-854f-add149c06034 |
| Late payment interest: fiscal rate (4% for 2026) plus 4 points | 8% a year | 2026 | WBTW art. 91 § 1; FOD Financiën payment page, https://financien.belgium.be/nl/ondernemingen/btw/betaling-teruggave/betaling |
| Interest paid by the State on late refunds (late rate minus 2 points) | 6% a year | 2026 | WBTW art. 91 § 4, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/87160bad-16b2-40ce-9abf-756a527f77a9 |

## The taxable base

- **What goes on the return.** Supplies of goods and services in Belgium, intra-EU acquisitions, imports and services received from abroad where the Belgian customer owes the VAT. The base is the price excluding VAT.
- **Exempt without deduction.** The supplies listed in art. 44 (for example medical care, education, most financial and insurance services, letting of immovable property). A business with only these supplies files no periodic return.
- **Domestic reverse charge for construction (medecontractant).** The customer pays the VAT on all work on immovable property (werk in onroerende staat, art. 19 § 2), on supply-and-fix of central heating, air conditioning, sanitary and electrical installations (not lighting), alarm and intercom systems, fitted kitchen and bathroom units, external shutters, wall and floor coverings, the repair and cleaning of those items, and staff hired out for such work. It applies when the supplier is established in Belgium and the customer itself files periodic returns (KB nr. 1 art. 20 §§ 1-2). The invoice shows no rate and no VAT and states the facts that justify the reverse charge. Unless the customer has told the supplier that it does not file periodic returns, the invoice carries the set wording that starts "Verlegging van heffing" and gives the customer one month to dispute it in writing (art. 20 §§ 1 and 3). The customer reports it in the return for the period the VAT falls due (art. 20 § 4).
- **Other customer-pays cases.** Services from a non-established supplier taxed in Belgium under art. 21 § 2 (art. 51 § 2, 1°); other goods and services supplied in Belgium by a non-established supplier to a Belgian-established customer who files returns (art. 51 § 2, 5°); gold (KB nr. 1 art. 20bis); greenhouse gas emission allowances (KB nr. 1 art. 20ter).
- **Capital goods.** Deduction on capital goods is subject to adjustment. For immovable capital goods the adjustment period is 15 years, and 25 years for buildings let under the art. 44 § 3, 2°, d) regime (art. 48 § 2 as amended by the Law of 10 February 2026).
- **Credits.** An excess of deductible VAT goes to the taxpayer's VAT provision account unless a refund is asked for in the return (art. 76 § 1).
- **Grid map** (KB nr. 1 annex II).

| Transaction | Base grid | VAT grid | Notes |
|---|---|---|---|
| Domestic sale at 6% / 12% / 21% | 01 / 02 / 03 | 54 | |
| Sale where the customer pays the VAT (construction, art. 51 § 2, KB nr. 1 art. 20, 20bis, 20ter) | 45 | none | Not on the EU listing |
| Services to an EU business under the general rule | 44 | none | Also on the intra-EU listing |
| Exempt intra-EU supply of goods, ABC triangulation sales | 46 | none | Also on the intra-EU listing |
| Exports and other exempt supplies with deduction | 47 | none | |
| Credit notes issued | 48 (on 44 and 46) / 49 (others) | 64 | VAT recovered on credit notes issued |
| Domestic purchases: goods for resale and raw materials / services and other goods / capital goods | 81 / 82 / 83 | 59 (deductible part) | Art. 45 limits apply |
| Intra-EU acquisition of goods | 86 (and 81-83) | 55, deducted in 59 | |
| Services from an EU supplier taxed in Belgium | 88 (and 81-83) | 55, deducted in 59 | |
| Construction work received under KB nr. 1 art. 20, services from non-EU suppliers, other customer-pays purchases | 87 (and 81-83) | 56, deducted in 59 | |
| Import with VAT deferred to the return (ET 14000 licence) | 87 | 57, deducted in 59 | |
| Credit notes received | 84 (on 86 and 88) / 85 (others) | 63 | VAT to repay |
| Other corrections in favour of the State / the business | | 61 / 62 | |

- **Totals.** VAT due (XX) = 54 + 55 + 56 + 57 + 61 + 63. Deductible VAT (YY) = 59 + 62 + 64. Grid 71 = XX minus YY if positive; grid 72 = YY minus XX. Only one of 71 and 72 is filled (KB nr. 1 annex II, Kader IV to VI).
- **Classifying bank lines.**
  - Not on the return: wages, social contributions, tax payments, fines, loan principal, dividends, owner injections and withdrawals, transfers between own accounts.
  - Exempt purchases, no VAT to deduct: bank charges and payment-processor fees that are financial services, insurance, rent of immovable property (art. 44), unless the invoice charges Belgian VAT.
  - Utilities, post, transport and professional services billed by Belgian suppliers: domestic purchases, at the rate on the invoice.
  - Foreign software and online services: read the billing entity on the invoice, not the brand. An EU entity goes in 88 with VAT in 55; a non-EU entity in 87 with VAT in 56. If the invoice charges Belgian VAT, it is a domestic purchase.
- **Deduction limits.** Input VAT is deductible on purchases used for taxable supplies (art. 45 § 1). Road vehicles and their costs, fuel included: at most 50% (art. 45 § 2), with exceptions for the vehicle types listed there (for example over 3,500 kg, light goods vehicles as defined, motorcycles, vehicles for resale or for rental to anyone). No deduction on tobacco, spirits not for resale, accommodation, food and drink (with exceptions such as staff working away and businesses that resell the same services) and reception costs (art. 45 § 3).
- **Conservative defaults when the facts are missing.** Treat an unknown sale rate as 21%, an unknown purchase as non-deductible, an unknown EU customer as a consumer (charge 21%), an unknown business-use share as 0%. These are working defaults for drafting, not law: confirm each one with the client before filing.

## Deadlines and filing

- **Monthly return** by the 20th of the following month; **quarterly return** by the 25th of the month after the quarter (KB nr. 1 art. 17 §§ 1-2). The VAT is paid by the same date (art. 53 § 1, 3°; FOD Financiën, btw-kalender). Quarterly filers pay no quarterly advances any more (FOD Financiën, btw-kalender).
- **2026 calendar (FOD Financiën).** Quarterly: Q4 2025 by 26 January 2026, Q1 by 27 April, Q2 by 25 July, Q3 by 25 October, Q4 2026 by 25 January 2027. Monthly: the 20th, except May (22 June 2026), August (21 September 2026) and November (21 December 2026); December 2026 by 20 January 2027.
- **No summer extension from 2026.** A return after the legal date is late. As a 2026 transition, no late-filing fine is charged if the June or Q2 2026 return is filed by 10 August 2026, or the July 2026 return by 10 September 2026. Late filing still extends the limitation period by a year, delays the credit to the provision account, and blocks refund requests through the return for the next 6 months (FOD Financiën, periodic return page).
- **Switching.** A quarterly filer that fails the test moves to monthly at the end of that quarter and notifies it by the 10th of the next month (KB nr. 1 art. 17 § 3).
- **Corrections.** A material error found before the deadline: file a new return for the same period, which replaces the first. After the deadline: correct in the next return (art. 17 § 4).
- **Intervat.** Returns and listings are filed electronically through Intervat (KB nr. 1 art. 18; KB nr. 23 art. 2; FOD Financiën). Paper form 625 only if the business or its agent cannot file electronically, with a signed written statement of the reasons to the competent office (KB nr. 1 art. 18 § 2; FOD Financiën, periodic return page).
- **Replacement return.** No return within 3 months after the period: the administration proposes a replacement return for the highest grid 71 of the previous 12 months, or EUR 2,100 if that is higher or there is none. Filing the real return within one month ends it; otherwise it becomes final and the tax is payable at once with late interest (art. 53 § 1ter). An objection can be filed within 6 months through Intervat (KB nr. 1 art. 17bis).
- **Refunds.** A credit is refunded only on express request, by the end of the third month after the return period, and only if all returns for the previous six months and the return showing the credit were filed on time and in the required way. Otherwise the credit goes to the VAT provision account, unless it is first set against a tax debt or retained (art. 76 § 1, as replaced by the Law of 10 February 2026). The State pays interest on a late refund (rate above; art. 91 § 4).
- **Annual client listing.** Before 31 March, listing each Belgian VAT-registered customer supplied in the previous year (more than EUR 250 excluding VAT per customer, FOD Financiën), with the total excluding VAT and the VAT charged (WBTW art. 53quinquies; KB nr. 23 art. 1 § 1). Customers making only art. 44 exempt supplies and non-taxable legal persons are left out. If there is nothing to list, tick the "nihil" box in the last return of the year (KB nr. 1 annex II, Kader VIII). On ceasing activity, file within 3 months (KB nr. 23 art. 1 § 3). The 2026 listing is due before 31 March 2027.
- **Intra-EU listing (intracommunautaire opgave).** Part 1 lists, per EU VAT number, exempt intra-EU supplies of goods, ABC sales and services under the general B2B rule; part 2 covers call-off stock (WBTW art. 53sexies; KB nr. 50 art. 1 and 9). Monthly by the 20th; quarterly by the 25th while intra-EU supplies of goods stay at or below EUR 50,000 in the quarter and each of the four before. Once exceeded, monthly listings start, with the months already elapsed in the quarter due by the 25th of the next month (KB nr. 50 art. 5 and 11).
- **Structured e-invoicing from 1 January 2026.** A taxable person established in Belgium must issue a structured electronic invoice for every supply, other than one exempt under art. 44, to a customer that must give its Belgian VAT number, including credit notes in the same format (art. 53 § 2bis). This includes businesses under the small-business exemption, whose supplies are not art. 44 supplies (art. 53 § 2bis; efactuur.belgium.be FAQ, question 2). Flat-rate taxpayers under art. 56 and bankrupt taxpayers for the bankrupt activity are excluded. Every Belgian VAT-registered business must be able to receive one. Where the customer cannot receive one for technical reasons, an ordinary invoice is still issued (art. 53 § 2bis, last paragraph, added by the Law of 10 February 2026). Formats and Peppol: [belgium-einvoice](belgium-einvoice.md).

## Penalties and interest

| Item | Rule | Source |
|---|---|---|
| Late payment interest | 8% a year for 2026; per month on the VAT rounded down to EUR 10; each started month counts in full; not charged under EUR 5 a month | WBTW art. 91 § 1; FOD Financiën payment page |
| Unpaid or late VAT, return filed on time | 5% of the VAT | KB nr. 41 Table G, section 1, I.1 |
| Unpaid VAT, return filed late or within the replacement-return month | 10% of the VAT | KB nr. 41 Table G, section 1, I.2 |
| VAT under a final replacement return | 15% of the VAT | KB nr. 41 Table G, section 1, I.3 |
| Reverse charge wrongly applied (art. 51 § 2, KB nr. 1 art. 20) | 20% of the VAT | KB nr. 41 Table G, section 1, IV |
| Return not filed | EUR 500, then 1,250, then 2,500, then 5,000 per return | KB nr. 44 annex, section 1, I.A |
| Return filed up to 5 months late | EUR 100 per return per started month, maximum EUR 500 | KB nr. 44 annex, section 1, I.B |
| Return wrongly completed | EUR 80 (purely accidental) or EUR 500 per return | KB nr. 44 annex, section 1, I.C |
| Wrong filing frequency / wrong filing procedure | EUR 250 / EUR 400 per return | KB nr. 44 annex, section 1, I.D and I.E |
| Client listing not filed, or more than 9 months late | EUR 3,000 per listing | KB nr. 44 annex, section 1, IV.1 |
| Client listing up to 3 months late | Nil listing EUR 50; otherwise EUR 25 per customer, minimum 75, maximum 1,500 | KB nr. 44 annex, section 1, IV.1.B |
| Client listing up to 9 months late | Nil listing EUR 150; otherwise EUR 75 per customer, minimum 225, maximum 2,250 | KB nr. 44 annex, section 1, IV.1.B |
| Intra-EU listing not filed, or more than 6 months late | Part 1 EUR 3,000; part 2 EUR 1,500 | KB nr. 44 annex, section 1, IV.2 |
| Intra-EU listing up to 2 months late | Part 1 EUR 25, part 2 EUR 15 per person listed; minimum 75, maximum 1,500 | KB nr. 44 annex, section 1, IV.2.B |
| Invoice not issued on time | Per invoice EUR 50 (max 500), then 125 (max 1,250), then 250 (max 5,000) | KB nr. 44 annex, section 2, I.A (from 1 January 2026) |
| No technical means to issue and receive structured e-invoices | EUR 1,500, then 3,000, then 5,000; a later offence counts only if found at least 3 months after the previous fine | KB nr. 44 annex, section 2, I.C |
| Rounding of fines | The total fine is rounded down to the euro below EUR 250 and to the ten euros above | KB nr. 41 art. 4 § 1 |
| Spontaneous correction | Full remission of proportional fines if corrected before any intervention by a tax administration | KB nr. 41 art. 3 |

**Tolerance in early 2026.** FOD Financiën applied no penalties during the first three months of 2026 (January to March) for offences specific to the new e-invoicing obligation: not yet having the technical means to send or receive a structured e-invoice, or not issuing one because the business's own system, or a third party's, could not yet produce a valid one. The condition is that the business can show it took steps in a timely and reasonable manner. The invoice still had to be issued in another format or by another channel. Each case is assessed individually and there is no general postponement ([einvoice.belgium.be, tolerance during the first three months of 2026](https://einvoice.belgium.be/en/news/period-tolerance-during-first-three-months-2026)). For self-billing invoices the administration is lenient until 30 June 2026 where sending or receiving them is not yet technically possible, if the business shows its software supplier is still building the function; until then they may be made and sent another way, with no fine for sender or receiver ([efactuur.belgium.be FAQ B2B, question 23](https://efactuur.belgium.be/nl/FAQ/algemene-vragen-b2b)).

The KB nr. 41 scale does not apply where the offence was committed to evade tax (KB nr. 41 art. 1).

## Cross-border points

- **Services bought from EU suppliers** under the general B2B rule: base in 88, VAT in 55, deducted in 59. **From non-EU suppliers:** base in 87, VAT in 56, deducted in 59 (KB nr. 1 annex II).
- **Intra-EU acquisitions of goods:** base in 86, VAT in 55.
- **Sales to EU businesses:** services in 44, goods in 46, and both on the intra-EU listing; the customer's EU VAT number is needed.
- **Non-established suppliers selling goods in Belgium** to a Belgian-established customer that files returns: the customer pays the VAT (art. 51 § 2, 5°). A supplier with a Belgian fixed establishment not involved in the supply counts as non-established (art. 51 § 2, second paragraph).
- **Foreign businesses** are outside the B2B e-invoicing mandate, which applies to taxable persons established in Belgium (art. 53 § 2bis). A business not established in Belgium may use the Belgian small-business exemption only through the EU scheme (art. 56ter § 2).
- **Distance sales and e-services to EU consumers** go through the one-stop shop, not this return. See `eu-vat-directive`.

## Worked examples

**Example 1: monthly return of a construction company, September 2026.** A Belgian BV files monthly. In September 2026 it invoices EUR 60,000 of renovation work to a general contractor that files Belgian VAT returns: reverse charge, grid 45, no VAT on the invoice. It also invoices EUR 10,000 of work at 21% to a business customer that does not file returns (an art. 44 exempt medical practice), so the BV charges VAT: grid 03, VAT 2,100 in grid 54. It receives EUR 25,000 of subcontracted tiling under reverse charge: grid 87, VAT 5,250 in grid 56, deducted in grid 59. It buys EUR 8,000 of materials at 21% (grid 81, VAT 1,680). VAT due is 2,100 + 5,250 = 7,350. Deductible VAT is 5,250 + 1,680 = 6,930. Grid 71 is 420, filed and paid by 20 October 2026.

```oa-check
name: Belgium monthly return September 2026, construction reverse charge
inputs:
  sales_reverse_charge: 60000
  sales_21: 10000
  subcontract_received: 25000
  materials_21: 8000
steps:
  - grid_45: sales_reverse_charge
  - grid_54: sales_21 * 0.21
  - grid_56: subcontract_received * 0.21
  - vat_due: grid_54 + grid_56
  - grid_59: grid_56 + materials_21 * 0.21
  - grid_71: vat_due - grid_59
expected:
  grid_45: 60000
  grid_54: 2100
  grid_56: 5250
  vat_due: 7350
  grid_59: 6930
  grid_71: 420
```

**Example 2: quarterly return Q3 2026 with EU services, paid late, and a late client listing.** A consultancy files quarterly. In Q3 2026 it invoices EUR 20,000 at 21% to Belgian clients (grid 03, VAT 4,200 in 54) and EUR 30,000 of services to EU businesses (grid 44 and the intra-EU listing). It buys EUR 2,000 of advertising from an Irish entity (grid 88, VAT 420 in 55), EUR 1,000 of software from a US entity (grid 87, VAT 210 in 56) and EUR 5,000 of Belgian services at 21% (VAT 1,050). VAT due is 4,830; deductible VAT is 1,680; grid 71 is 3,150. The return is filed on time by 25 October 2026 but paid on 20 December 2026. Interest runs from 26 October: two started months, so 3,150 × 8% × 2/12 = EUR 42. The fine for late payment with a timely return is 5%, EUR 157.50, rounded down to EUR 157 (KB nr. 41 art. 4). Separately, its 2026 client listing of 12 customers, due before 31 March 2027, is filed two months late: 12 × EUR 25 = EUR 300, inside the EUR 75 to EUR 1,500 range.

```oa-check
name: Belgium quarterly return Q3 2026, late payment and late client listing
inputs:
  sales_be_21: 20000
  eu_services_sold: 30000
  ads_from_eu: 2000
  software_non_eu: 1000
  purchases_be_21: 5000
  months_late: 2
  listed_customers: 12
steps:
  - grid_54: sales_be_21 * 0.21
  - grid_55: ads_from_eu * 0.21
  - grid_56: software_non_eu * 0.21
  - vat_due: grid_54 + grid_55 + grid_56
  - grid_59: purchases_be_21 * 0.21 + grid_55 + grid_56
  - grid_71: vat_due - grid_59
  - interest: floor(grid_71 / 10) * 10 * 0.08 * months_late / 12
  - late_payment_fine: floor(grid_71 * 0.05)
  - listing_fine: clamp(listed_customers * 25, 75, 1500)
expected:
  vat_due: 4830
  grid_59: 1680
  grid_71: 3150
  interest: 42
  late_payment_fine: 157
  listing_fine: 300
```

**Example 3: quarterly return, Q3 2026, with car and restaurant limits.** A Belgian BV files quarterly. In July to September 2026 it invoices EUR 80,000 of consultancy at 21%. It buys EUR 30,000 of goods and services at 21%, has EUR 4,000 net of costs on a passenger car at 21%, and a EUR 500 net client dinner at 12%. Output VAT is 80,000 × 21% = 16,800 (grid 54). Input VAT on the general purchases is 6,300. The car VAT is 840, of which 50% is deductible: 420. The dinner VAT of 60 is not deductible. Deductible VAT in grid 59 is 6,720. VAT payable in grid 71 is 10,080, due with the return by 25 October 2026. If it pays a month late but filed on time, the fine is 5% of 10,080, which is EUR 504. A total fine above EUR 250 is rounded down to the ten euros (KB nr. 41 art. 4 § 1), so the fine is EUR 500. Late interest at 8% for one month is EUR 67.20.

```oa-check
name: Belgium quarterly return Q3 2026 with car and restaurant limits
inputs:
  sales_net: 80000
  purchases_net: 30000
  car_costs_net: 4000
  dinner_net: 500
steps:
  - output_vat: sales_net * 0.21
  - input_general: purchases_net * 0.21
  - car_vat: car_costs_net * 0.21
  - car_deductible: car_vat * 0.50
  - dinner_deductible: dinner_net * 0.12 * 0
  - grid_59: input_general + car_deductible + dinner_deductible
  - grid_71: output_vat - grid_59
  - fine_unrounded: grid_71 * 0.05
  - late_payment_fine: floor(fine_unrounded / 10) * 10
  - interest_one_month: floor(grid_71 / 10) * 10 * 0.08 / 12
expected:
  output_vat: 16800
  grid_59: 6720
  grid_71: 10080
  late_payment_fine: 500
  interest_one_month: 67.20
```

**Example 4: the small-business exemption and its 10% tolerance.** A self-employed designer has used the exemption for years. By 30 November 2026 her 2026 turnover is EUR 24,000. In December she invoices EUR 2,500 more, so the year ends at EUR 26,500. That is EUR 1,500 over the EUR 25,000 limit, or 6%. Because the excess is no more than 10% (the ceiling is EUR 27,500), she keeps the exemption for all of 2026 and charges no VAT on the December invoices. But she exceeded the limit in 2026, so she cannot use the exemption in 2027, even though the 2027 limit is EUR 26,000 (art. 56decies § 1). From 1 January 2027 she charges 21%. On EUR 3,000 of January 2027 invoices that is EUR 630. Had her December invoices been EUR 4,000 (year total EUR 28,000, 12% over), the exemption would have ended during December, at the moment the 10% margin was passed.

```oa-check
name: Belgium small-business exemption tolerance, 2026 into 2027
inputs:
  turnover_to_november: 24000
  december_invoices: 2500
  limit: 25000
  january_2027_net: 3000
steps:
  - year_turnover: turnover_to_november + december_invoices
  - excess: year_turnover - limit
  - excess_pct: excess / limit * 100
  - tolerance_ceiling: limit * 1.10
  - headroom_left: tolerance_ceiling - year_turnover
  - vat_january_2027: january_2027_net * 0.21
expected:
  year_turnover: 26500
  excess: 1500
  excess_pct: 6
  tolerance_ceiling: 27500
  headroom_left: 1000
  vat_january_2027: 630
```

## Ask the client first

- What is your annual turnover for the whole activity, and do your intra-EU supplies of goods exceed EUR 50,000 in any quarter? What was your turnover in Belgium in 2025, what do you expect for 2026, and when did you start? (Monthly or quarterly returns and listings; the EUR 25,000 exemption, its pro rata limit and the 10% tolerance.)
- Do you do construction work or installations, and do your customers file Belgian VAT returns? Do you run a registered cash system, deal in scrap, or belong to a VAT unit? (Decides reverse charge on sales and the invoice wording; these exclude the exemption.)
- Who are your foreign suppliers, by legal entity and country on the invoice? (Grids 86, 87, 88 and self-assessed VAT.)
- Do you have cars, restaurant, hotel or reception costs? (50% limit and blocked VAT.)
- Do you also make exempt supplies such as letting, medical care or financial services? (Pro rata; refer.)
- Can your software send and receive structured e-invoices, and were any 2026 returns, payments or listings late? (Fines and interest.)

## Sources

| Source | URL | Read on |
|---|---|---|
| FisconetPlus, VAT Code (WBTW), official coordination, table of contents | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e154233d-dc0e-4c0f-9bbf-afc79e797448 | 2026-10-24 |
| WBTW art. 45 (deduction limits) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/58a466d6-c626-4369-854f-add149c06034 | 2026-10-31 |
| WBTW art. 51 (who owes the VAT, reverse charge) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/09a92203-ce33-4e57-8620-fbbfcdbfbbf0 | 2026-10-24 |
| WBTW art. 53 (returns, replacement return, structured e-invoice), text from 20.02.2026 | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/773cb22d-053e-4d4d-ae1f-7ddadab87d78 | 2026-10-31 |
| WBTW art. 53quinquies (annual client listing) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/94b855fa-1105-42e6-9944-0310b45bc31e | 2026-10-24 |
| WBTW art. 53sexies (intra-EU listing) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f6abfe10-db3d-4bb2-8fbc-f2a9e144e0ae | 2026-10-24 |
| WBTW art. 56ter (small-business exemption) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6191791d-e4d1-4829-b8f1-56c7a6892136 | 2026-10-31 |
| WBTW art. 91 (late interest), text from 09.03.2026 | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/87160bad-16b2-40ce-9abf-756a527f77a9 | 2026-10-31 |
| KB nr. 1 (art. 17 frequency and deadlines from 10.01.2026; art. 18 electronic filing; art. 20 to 20ter reverse charge) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c69c7ee9-8e6d-48da-b9f7-c23cb025a777 | 2026-10-24 |
| KB nr. 1 annex II (description of the return grids) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0ac584ed-a3ad-4734-9537-160f30357de5 | 2026-10-24 |
| KB nr. 20 (rates, Tables A, B and C) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 | 2026-10-24 |
| KB nr. 23 (annual client listing) and its annex (model form 725) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0e6d7db6-7de7-480e-89ab-5d0763e32251 | 2026-10-24 |
| KB nr. 41 (proportional fines, art. 3 and 4, Table G), coordination to 10.01.2026 | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d48c176f-6bdd-41fb-b0a1-725841887613 | 2026-10-24 |
| KB nr. 44 (non-proportional fines), coordination to 10.01.2026 | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac | 2026-10-24 |
| KB nr. 50 (intra-EU listing) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/90c85f66-9e8b-48bc-9032-ce1f7db88872 | 2026-10-24 |
| FOD Financiën, periodieke btw-aangifte (frequency, Intervat, replacement return, no holiday scheme in 2026) | https://financien.belgium.be/nl/ondernemingen/btw/aangifte/periodieke-aangifte | 2026-10-24 |
| FOD Financiën, btw-kalender 2026 | https://financien.belgium.be/nl/ondernemingen/btw/btw-kalender | 2026-10-24 |
| FOD Financiën, jaarlijkse klantenlisting (EUR 250, 31 March, exemption turnover report) | https://financien.belgium.be/nl/ondernemingen/btw/aangifte/jaarlijkse_klantenlisting | 2026-10-24 |
| FOD Financiën, betaling (8% late interest for 2026) | https://financien.belgium.be/nl/ondernemingen/btw/betaling-teruggave/betaling | 2026-10-24 |
| WBTW art. 56decies (losing the exemption, 10% tolerance) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/83f1a474-d23d-446b-ac69-284f8909b300 | 2026-10-31 |
| WBTW art. 76 (refunds) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/11d42f57-9159-47a5-b967-004f74497d5c | 2026-10-31 |
| KB nr. 1 art. 17, version history (EUR 250,000 test removed from 10 January 2026) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/bce4326d-6d49-4680-bd6d-8bf05cb7f6bc | 2026-10-23 |
| WBTW art. 56bis (exclusions from the small-business exemption) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0cd39ffd-676c-4846-b0c7-2328b1e94524 | 2026-10-31 |
| KB 14 February 2026 (hotels and campsites 12%, pesticides 21%, from 1 March 2026) | https://www.ejustice.just.fgov.be/eli/besluit/2026/02/14/2026001322/staatsblad | 2026-10-23 |
| Law of 10 February 2026, various VAT provisions | https://www.ejustice.just.fgov.be/eli/wet/2026/02/10/2026001291/staatsblad | 2026-10-23 |
| Law of 23 September 2026, art. 26-27 (exemption limits 2027-2031) | https://www.ejustice.just.fgov.be/eli/wet/2026/09/23/2026007237/staatsblad | 2026-10-23 |
| FPS BOSA / FOD Financiën, "Period of tolerance during the first three months of 2026" (e-invoicing) | https://einvoice.belgium.be/en/news/period-tolerance-during-first-three-months-2026 | 2026-10-30 |
| efactuur.belgium.be, FAQ algemene vragen B2B, question 23 (self-billing tolerance to 30 June 2026) | https://efactuur.belgium.be/nl/FAQ/algemene-vragen-b2b | 2026-10-30 |

Not yet confirmed: the EUR 250 per-customer floor of the client listing is on the FOD Financiën page but not in KB nr. 23 (neither its articles nor its annex, model form 725, state an amount), so its legal basis was not found; the 2027 late-interest rate (the fiscal rate for 2027 is published in the third quarter) was not looked up; the FOD Financiën page waives only the fine for late filing (KB nr. 44) for June, Q2 and July 2026 returns filed by 10 August or 10 September 2026; whether the late-payment fine on such a return is 5% or 10% (KB nr. 41 Table G, I.1 or I.2) is not stated in the sources read; the old v2.0 internal review flags (EUR 5,000 single transaction, EUR 400 default delta and similar) were working rules, not law, and were not carried; the treatment of short-term letting income (platform sales, Airbnb) beyond the 12% rate for furnished accommodation is not covered here; whether the pro rata limit for a business that starts mid-year is also the limit tested for the "exceeded in the previous year" bar in art. 56decies; the full item lists of Tables A, B and C are summarised, not reproduced; the "annual EU listing" due before 31 March that an earlier version attributed to the btw-kalender was not carried, because the calendar could not be read and KB nr. 50 sets monthly and quarterly listings.

> Contributed by Michael Cutajar.

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
