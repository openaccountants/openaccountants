---
name: be-vat-return
description: "Prepare the Belgian periodic VAT return for 2026: monthly/quarterly eligibility, rates and effective dates, Intervat grids, construction and cross-border reverse charge, listings, SME exemptions, refunds, interest and penalties. Includes original return and transaction cases. Trigger: btw-aangifte, déclaration TVA, Intervat, klantenlisting, medecontractant, franchise TVA. Peppol implementation: belgium-einvoice; income taxes: be-income-tax and be-corporate-tax."
version: 2.7
jurisdiction: BE
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - vat-workflow-base
  - eu-vat-directive
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Belgium VAT and the periodic VAT return (btw-aangifte / déclaration TVA): the law, preparing and filing, tax year 2026 v2.7

> **Not yet approved.** This Guide is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Belgium.

This Guide prepares ordinary Belgian periodic returns from invoices and records. WBTW means the Belgian VAT Code; KB means Royal Decree. Use the law and the dated official instructions in Sources. Establish the period, VAT regime, place of supply and deduction entitlement before classifying a transaction. A bank description or VAT number alone does not establish its treatment.

**Sibling skills.** [belgium-einvoice](belgium-einvoice.md) covers Peppol and invoice formats. [belgium-bookkeeping](belgium-bookkeeping.md), [be-income-tax](be-income-tax.md), [be-corporate-tax](be-corporate-tax.md) and [be-cross-border](be-cross-border.md) cover the rest. Load `vat-workflow-base` and `eu-vat-directive` alongside.

## Who this applies to

- **Taxable persons.** Anyone who regularly and independently carries on the economic supplies described in the Code, with or without a profit motive, irrespective of where the activity is exercised (WBTW art. 4). Belgian liability then depends on the transaction and place-of-supply rules; residence alone does not decide it.
- **Who files.** Every taxable person with a right to deduct files a periodic return (WBTW art. 53 § 1, first paragraph, 2°). Monthly is the rule; quarterly is an option (KB nr. 1 art. 17).
- **Who does not file.** A business under the small-business exemption (art. 56bis to 56undecies), under the special scheme for farmers, or making only art. 44 exempt supplies with no right to deduct (FOD Financiën, periodic return page). From 2026 a small-business-exemption business still reports its previous year's Belgian turnover, or 0.00, through Intervat before 31 March (FOD Financiën, annual client listing page). It still files the start, change and end-of-activity declarations (art. 53 § 1, second paragraph).
- **Small-business exemption (vrijstellingsregeling / franchise).** A business established in Belgium whose annual turnover in Belgium does not exceed EUR 25,000 may choose not to charge VAT (art. 56ter § 1). For starts from 2 March 2026, the limit is reduced proportionately by elapsed days from 1 January to commencement. The former 2025 wording did not contain this paragraph; do not apply the new paragraph retrospectively to January/February starts without checking the earlier implementing rules. Check this point with one of our partner accountants. Joint owners count their turnover together; spouses with separate activities count separately. The business must notify the VAT administration in advance. It cannot deduct input VAT (art. 56bis § 4).
- **Who cannot use the exemption (art. 56bis, wording from 2 March 2026).** VAT units; businesses that regularly do construction work (except some services by individuals through platforms), businesses that must issue a till receipt from a registered cash system, and dealers in scrap and waste (art. 56bis § 2). The exemption also never covers art. 8 transactions, intra-EU supplies of new means of transport, the transactions specifically listed in art. 58 §§ 1-2, undeclared or unlawful transactions, or hotel-type furnished accommodation under art. 44 § 3, 2°, a), third dash (except some supplies by individuals under art. 50 § 4) (art. 56bis § 3).
- **Turnover composition.** Use art. 56nonies: ordinary taxable supplies, qualifying zero/exempt-with-deduction supplies and listed exempt property/financial/insurance transactions unless ancillary; exclude disposals of tangible/intangible investment assets. Separate Belgian and Union turnover. An exemption limit is not a cash-receipts test.
- **Crossing the limit.** If the year's turnover exceeds EUR 25,000 by 10% or less (up to EUR 27,500), the business keeps the exemption for that year. If it exceeds it by more than 10%, the exemption ends from that moment. A business that exceeded the limit in the previous year cannot use the exemption for the following calendar year (art. 56decies § 1).
- **Limits already legislated for later years, not 2026.** EUR 26,000 for 2027, EUR 27,000 for 2028, EUR 28,000 for 2029, EUR 29,000 for 2030 and EUR 30,000 from 2031 (art. 56ter § 1 as replaced by art. 26 of the Law of 23 September 2026, in force 1 January 2027).
- **EU small-business scheme.** A business established in another EU state can use the Belgian exemption if its EU turnover is at most EUR 100,000 and its Belgian turnover at most EUR 25,000. It notifies its home state, which issues a number with the suffix "EX" (art. 56ter § 2). The Belgian and Union turnover lookbacks also apply: a prior-year excess excludes the scheme, and an in-year Union excess ends it immediately (art. 56decies). The exemption from Belgian registration and periodic returns for those exempt supplies depends on compliance with home-state SME reporting (art. 56septies). A Belgian business seeking another state's exemption must satisfy that state's conditions, notify Belgium and receive confirmation of its EX identification before use (art. 56quater).
- **Quarterly filers.** Allowed if annual turnover excluding VAT for the whole economic activity is at most EUR 2,500,000, and the business does not have to file the intra-EU listing monthly (KB nr. 1 art. 17 § 2, text in force from 10 January 2026; the second test was removed by the KB of 17 December 2025, art. 6). The second test the FOD Financiën page still lists (EUR 250,000 of energy products, mobile phones, computers and motor vehicles) is gone from the decree since 10 January 2026; follow the decree.
- **Specialist cases, with no filing conclusion supplied here.** Flat-rate scheme (art. 56, KB nr. 2), farmers' special scheme (art. 57), travel agents, margin schemes, VAT units, mixed taxable and exempt activity needing a pro rata, real estate sales under VAT, a non-resident acting through a fiscal representative, a bankrupt estate (annual return by the trustee, KB nr. 1 art. 17 § 5). Check this point with one of our partner accountants. A question about income tax goes to [be-income-tax](be-income-tax.md) or [be-corporate-tax](be-corporate-tax.md).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 21% | 2026 | KB nr. 20 art. 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Reduced rate, only supplies meeting the relevant Table A entry (including listed food, water, medicines, publications, transport, admissions and housing); ancillary services in a principally different complex contract do not qualify automatically | 6% | 2026 | KB nr. 20 art. 1, a) and Table A, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Reduced rate, Table B (restaurant and catering services excluding drinks; furnished accommodation and campsites from 1 March 2026; other listed items) | 12% | 2026 | KB nr. 20 art. 1, b) and Table B, sections I and IV, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Zero rate, only qualifying periodical publications in Table C; not a general label for all foreign sales | 0% | 2026 | KB nr. 20 art. 1, c) and Table C, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Hotels and campsites, before / from 1 March 2026 | 6% / 12% | 2026 | KB nr. 20 Table B, IV (in Table B from 01.03.2026), https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Plant-protection products, before / from 1 March 2026 | 12% / 21% | 2026 | KB nr. 20 Table B, III (repealed from 01.03.2026), https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Heat pumps, 1 January 2026–31 December 2030 | Classification held: the special 6% provision requires qualifying supply-and-installation, end-consumer/private-dwelling use, first occupation less than ten calendar years before the first invoice, technical standards and prescribed invoice wording; excludes specified hybrid systems and pools/saunas. No rate decision for an actual installation here. Check this point with one of our partner accountants. | 2026 | KB nr. 20 art. 1quater/1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Small-business exemption, annual turnover in Belgium | EUR 25,000 | 2026 | WBTW art. 56ter § 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6191791d-e4d1-4829-b8f1-56c7a6892136 |
| Tolerance: exemption kept for the year if the limit is exceeded by no more than | 10% (EUR 27,500, computed: 25,000 × 1.10) | 2026 | WBTW art. 56decies § 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/83f1a474-d23d-446b-ac69-284f8909b300 |
| Small-business exemption limit for 2027 / 2028 / 2029 / 2030 / 2031 onwards | EUR 26,000 / 27,000 / 28,000 / 29,000 / 30,000 | 2027-2031 | Law of 23 September 2026 art. 26-27, https://www.ejustice.just.fgov.be/eli/wet/2026/09/23/2026007237/staatsblad |
| EU small-business scheme: EU-wide turnover cap | EUR 100,000 | 2026 | WBTW art. 56ter § 2, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6191791d-e4d1-4829-b8f1-56c7a6892136 |
| Quarterly returns allowed up to annual turnover (whole activity, excluding VAT) | EUR 2,500,000 | 2026 | KB nr. 1 art. 17 § 2, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c69c7ee9-8e6d-48da-b9f7-c23cb025a777 |
| Quarterly intra-EU listing allowed while intra-EU supplies of goods in the quarter and each of the four before stay at or below | EUR 50,000 | 2026 | KB nr. 50 art. 5 § 1 and art. 11 § 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/90c85f66-9e8b-48bc-9032-ce1f7db88872 |
| Annual client listing: customers supplied for a total of more than | EUR 250 a year, excluding VAT | 2026 | FOD Financiën, annual client listing, https://financien.belgium.be/nl/ondernemingen/btw/aangifte/jaarlijkse_klantenlisting |
| Replacement return when no return is filed: highest grid 71 of the previous 12 months, at least | EUR 2,100 | 2026 | WBTW art. 53 § 1ter, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/773cb22d-053e-4d4d-ae1f-7ddadab87d78 |
| Input VAT on road vehicles and their costs, maximum deduction | 50% | 2026 | WBTW art. 45 § 2, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/58a466d6-c626-4369-854f-add149c06034 |
| Late payment interest: fiscal rate (4% for 2026) plus 4 points | 8% a year | 2026 | WBTW art. 91 § 1; FOD Financiën payment page, https://financien.belgium.be/nl/ondernemingen/btw/betaling-teruggave/betaling |
| Interest on qualifying late refunds under art. 91 §§ 4–5, with statutory starting dates, EUR 10 base rounding, EUR 5 monthly minimum and withholding/missing-information exclusions (late rate minus 2 points) | 6% a year (computed: 8% minus 2 points) | 2026 | WBTW art. 91 § 4, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/87160bad-16b2-40ce-9abf-756a527f77a9 |

## The taxable base

- **What goes on the return.** Supplies of goods and services in Belgium, intra-EU acquisitions, imports and services received from abroad where the Belgian customer owes the VAT. For ordinary supplies the base is the whole consideration, including price-linked subsidies and incidental charges, excluding VAT itself (WBTW arts. 26 and 28).
- **Exempt supplies.** Test the relevant art. 44 exemption; medical care, education, finance, insurance, post and property transactions are not exempt merely because of the supplier's sector. Exclusively exempt activity without deduction is outside periodic filing. Mixed activity and exemption exceptions require the specialist review above.
- **Domestic reverse charge for construction (medecontractant).** The customer pays the VAT on all work on immovable property (werk in onroerende staat, art. 19 § 2), on supply-and-fix of central heating, air conditioning, sanitary and electrical installations (not lighting), alarm and intercom systems, fitted kitchen and bathroom units, external shutters, wall and floor coverings, the repair and cleaning of those items, and staff hired out for such work. It applies when the supplier is established in Belgium and the customer itself files periodic returns (KB nr. 1 art. 20 §§ 1-2). The invoice shows no rate and no VAT and states the facts that justify the reverse charge. Unless the customer has told the supplier that it does not file periodic returns, the invoice carries the set wording that starts "Verlegging van heffing" and gives the customer one month to dispute it in writing (art. 20 §§ 1 and 3). The customer reports it in the return for the period the VAT falls due (art. 20 § 4).
- **Other customer-pays cases.** Services from a non-established supplier taxed in Belgium under art. 21 § 2 (art. 51 § 2, 1°); other Belgian-taxable, non-exempt goods and services supplied by a non-established supplier to a Belgian-established periodic filer, except transactions falling under art. 51 § 2, 1°, 2° or 6° (art. 51 § 2, 5°); gold and emission allowances have specific customer and product conditions in KB nr. 1 arts. 20bis–20ter. Their application is held here. Check this point with one of our partner accountants.
- **Capital goods.** Deduction on capital goods is subject to adjustment. The general period is five years, fifteen for designated immovable capital goods, and twenty-five for designated buildings let under art. 44 § 3, 2°, d); comparable services are also covered in the wording from 20 February 2026 (art. 48 § 2). Asset classification, commencement, comparable-service allocation and an actual adjustment are held. Check this point with one of our partner accountants.
- **Credits.** An excess of deductible VAT goes to the taxpayer's VAT provision account unless a refund is asked for in the return (art. 76 § 1).
- **Grid map** (KB nr. 1 annex II).

| Transaction | Base grid | VAT grid | Notes |
|---|---|---|---|
| Domestic sale at 6% / 12% / 21% | 01 / 02 / 03 | 54 | |
| Sale where the customer pays the VAT (construction, art. 51 § 2, KB nr. 1 art. 20, 20bis, 20ter) | 45 | none | Not on the EU listing |
| Services to an EU business under the general rule | 44 | none | Also on the intra-EU listing |
| Exempt intra-EU supply of goods, ABC triangulation sales | 46 | none | Also on the intra-EU listing |
| Exports and other exempt supplies with deduction | 47 | none | |
| Credit notes issued / negative adjustments | 48 (on 44 and 46) / 49 (other outgoing transactions) | 64 only for VAT shown and recoverable | Do not recover VAT that was never charged |
| Purchases: goods for resale and raw materials / services and other goods / capital goods | 81 / 82 / 83 | 59 (deductible part) | Amount excludes deductible VAT, so includes non-deductible VAT; net of received credit notes and adjustments |
| Intra-EU acquisition of goods | 86 (and 81-83) | 55, deductible part in 59 | |
| Services from an EU supplier taxed in Belgium | 88 (and 81-83) | 55, deductible part in 59 | |
| Construction work received under KB nr. 1 art. 20, services from non-EU suppliers, other customer-pays purchases | 87 (and 81-83) | 56, deductible part in 59 | |
| Import with VAT deferred to the return (valid ET 14000 licence) | 87 and applicable 81–83 | 57, deductible part in 59 | Licence eligibility/application is held for specialist review |
| Import VAT paid at customs | Applicable 81–83; no 87 merely for the import | No self-assessed VAT; deductible import VAT in 59 | Customs evidence and taxable business use required |
| Credit notes received / negative adjustments | 84 (on 86 and 88) / 85 (other incoming transactions); reduce 81–83 as applicable | 63 for VAT shown that must be repaid | For VAT corrections on reverse-charge credit notes, do not use the domestic-credit-note recipe: Check this point with one of our partner accountants. |
| Other corrections in favour of the State / the business | | 61 / 62 | |

- **Totals.** VAT due (XX) = 54 + 55 + 56 + 57 + 61 + 63. Deductible VAT (YY) = 59 + 62 + 64. Grid 71 = XX minus YY if positive; grid 72 = YY minus XX. Only one of 71 and 72 is filled (KB nr. 1 annex II, Kader IV to VI).
- **Classifying records.** Reconcile invoices, credit notes, customs papers and bank movements. Wages, tax/social payments, loan principal, dividends, capital injections and own-account transfers do not themselves represent a taxable business purchase. Retain genuine exempt purchases in the appropriate purchase grid; lack of deductible VAT does not mean every amount disappears from the return. Separate a bank/payment-provider's financial service from taxable subscriptions or administration. Utilities, post, transport, food retail, professional services and rent require the actual invoice and use. For foreign software, identify the legal supplier, establishment involved and place-of-supply rule. General B2B services from an EU supplier go to 88/55 and from a non-EU supplier to 87/56; a Belgian VAT charge does not by itself prove domestic treatment or entitlement to deduct. Resolve an incorrect charge before claiming it.
- **Deduction limits.** Input VAT requires taxable/qualifying business use and the prescribed evidence (art. 45 § 1); private use is excluded. The reverse charge does not itself guarantee full deduction. Road vehicles and their costs, fuel included: at most 50% (art. 45 § 2), with exceptions for the vehicle types listed there (for example over 3,500 kg, light goods vehicles as defined, motorcycles, vehicles for resale or for rental to anyone). No deduction on manufactured tobacco, spirits except resale/service/sample/tasting cases, accommodation/food/drink except the specified staff-away-on-assignment and same-service resale cases, and reception costs (art. 45 § 3, 1°–4°). A business purpose alone does not make a client meal deductible. The vehicle cap is a maximum, not an automatic 50% entitlement; establish business use first.
- **Missing facts.** Do not manufacture a VAT rate, customer status, business-use percentage or billing country. Hold the classification until supported; unresolved specialist outcomes use the partner-accountant referral.

## Deadlines and filing

- **Monthly return** by the 20th of the following month; **quarterly return** by the 25th of the month after the quarter (KB nr. 1 art. 17 §§ 1-2). The VAT is paid by the same date (art. 53 § 1, 3°; FOD Financiën, btw-kalender). Quarterly filers pay no quarterly advances any more (FOD Financiën, btw-kalender).
- **2026 calendar (FOD Financiën).** Quarterly: Q4 2025 by 26 January 2026, Q1 by 27 April, Q2 by 25 July, Q3 by 25 October, Q4 2026 by 25 January 2027. Monthly: the 20th, except May (22 June 2026), August (21 September 2026) and November (21 December 2026); December 2026 by 20 January 2027.
- **No summer extension from 2026.** A return after the legal date is late. As a 2026 transition, no late-filing fine is charged if the June or Q2 2026 return is filed by 10 August 2026, or the July 2026 return by 10 September 2026. Late filing still extends the limitation period by a year, delays the credit to the provision account, and blocks refund requests through the return for the next 6 months (FOD Financiën, periodic return page).
- **Switching.** A quarterly filer that fails the test moves to monthly at the end of that quarter and notifies it by the 10th of the next month (KB nr. 1 art. 17 § 3).
- **Corrections.** A material error found before the deadline: file a new return for the same period, which replaces the first. After the deadline: correct in the next return. This material-error procedure excludes errors requiring a corrective document (art. 17 § 4).
- **Intervat.** Returns and listings are filed electronically through Intervat (KB nr. 1 art. 18; KB nr. 23 art. 2; FOD Financiën). Paper form 625 only if the business or its agent cannot file electronically, with a signed written statement of the reasons to the competent office (KB nr. 1 art. 18 § 2; FOD Financiën, periodic return page).
- **Replacement return.** After three months following an unfiled period, the ordinary proposal uses the highest VAT due in the preceding twelve months, minimum EUR 2,100. No proposal is sent if the return was filed before notice, the taxpayer is not VAT-identified, or Treasury rights are endangered. Notice ordinarily takes effect on the third working day after postal handover unless disproved. File the missing return within one month from that effective date to end the proposal; otherwise the final replacement is notified and payable without delay with interest (art. 53 § 1ter). An objection to the final replacement can be filed at the designated electronic address within six months from its effective notice (KB nr. 1 art. 17bis); this does not itself stop collection.
- **Refunds.** Request the current return's credit expressly in the return. It must reach EUR 50; supply a valid bank account using the prescribed declaration by the end of the month before the refund-order month. The credit return and all returns for the preceding six months must have been timely and correctly filed. The refund order is due by the end of the second month after a monthly period, or third month after a quarterly period (KB nr. 4 art. 8/1 § 1; WBTW art. 76). This is subject to debt set-off, withholding and information checks, not a guaranteed unconditional payment. Otherwise a credit reaching EUR 2.50 is entered on the provision account; a late return shifts the crediting timetable (art. 8/1 §§ 2–3). Available provisions can be viewed and repayment requested in MyMinfin. The FOD implementation page says the account became technically visible there from 1 May 2026; earlier transitional credits/payments require the contemporaneous instructions, not retrospective use of this process. Keep a prior-period credit separate from the current return's grid 59/71 calculation.
- **Annual client listing.** Before 31 March, listing each Belgian VAT-registered customer supplied in the previous year (more than EUR 250 excluding VAT per customer, FOD Financiën), with the total excluding VAT and the VAT charged (WBTW art. 53quinquies; KB nr. 23 art. 1 § 1). Customers making only art. 44 exempt supplies and non-taxable legal persons are left out. If there is nothing to list, tick the "nihil" box in the last return of the year (KB nr. 1 annex II, Kader VIII). On ceasing activity, file within 3 months (KB nr. 23 art. 1 § 3). The 2026 listing is due before 31 March 2027.
- **Intra-EU listing (intracommunautaire opgave).** Part 1 lists qualifying exempt intra-EU goods/ABC sales and general B2B services not exempt in the destination state; part 2 covers call-off-stock movements. Monthly filers file monthly by the 20th. Quarterly filing by the 25th is available only to quarterly/non-periodic return filers (or qualifying VAT-unit members), with the relevant goods total at most EUR 50,000 in the quarter and each of the four preceding quarters. Services alone do not consume this goods threshold. On exceeding it, prepare separate monthly listings for the months elapsed since the quarter began, due by the 25th of the month after the crossing month (KB nr. 50 arts. 1, 5, 9, 11). Part 1 need not be filed if there is nothing to report (art. 7). The annual listing is for farmers not required to file periodic returns: part 1 by 31 March and part 2 before 31 March of the following year, or within three months on loss of that status (arts. 5 § 2, 11 § 2). It never replaces an ordinary periodic filer's listing.
- **Structured e-invoicing from 1 January 2026.** A taxable person established in Belgium must issue a structured electronic invoice for every supply, other than one exempt under art. 44, to a customer that must give its Belgian VAT number, including credit notes in the same format (art. 53 § 2bis). This includes businesses under the small-business exemption, whose supplies are not art. 44 supplies (art. 53 § 2bis; efactuur.belgium.be FAQ, question 2). Flat-rate taxpayers under art. 56 and bankrupt taxpayers for the bankrupt activity are excluded. A recipient of a required structured invoice identified under art. 50 § 1, first paragraph, 1° must be able to receive that invoice itself or through a third party. The receiving duty is not established merely by possession of any Belgian VAT number. Where the customer cannot receive one for technical reasons, an ordinary invoice is still issued (art. 53 § 2bis, last paragraph, added by the Law of 10 February 2026). Formats and Peppol: [belgium-einvoice](belgium-einvoice.md).

## Penalties and interest

| Item | Rule | Source |
|---|---|---|
| Late payment interest | 8% a year for 2026; monthly on VAT rounded down to EUR 10, EUR 5 monthly minimum. Interest periods run 21st–20th for monthly filers and 26th–25th for quarterly filers; each started period counts in full | WBTW art. 91 § 1; FOD Financiën payment page; https://financien.belgium.be/nl/ondernemingen/btw/betaling-teruggave/betaling |
| Unpaid or late VAT, return filed on time | 5% of the VAT | KB nr. 41 Table G, section 1, I.1; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d48c176f-6bdd-41fb-b0a1-725841887613 |
| Unpaid VAT, return filed late or within the replacement-return month | 10% of the VAT | KB nr. 41 Table G, section 1, I.2; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d48c176f-6bdd-41fb-b0a1-725841887613 |
| VAT under a final replacement return | 15% of the VAT | KB nr. 41 Table G, section 1, I.3; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d48c176f-6bdd-41fb-b0a1-725841887613 |
| Reverse charge wrongly applied (art. 51 § 2, KB nr. 1 art. 20) | 20% of the VAT | KB nr. 41 Table G, section 1, IV; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d48c176f-6bdd-41fb-b0a1-725841887613 |
| Return not filed | EUR 500, then 1,250, then 2,500, then 5,000 per return | KB nr. 44 annex, section 1, I.A; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Return filed up to 5 months late, or validly ending the replacement-return procedure | EUR 100 per return per started month, maximum EUR 500 | KB nr. 44 annex, section 1, I.B; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Return wrongly completed | EUR 80 (purely accidental) or EUR 500 per return | KB nr. 44 annex, section 1, I.C; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Wrong filing frequency / wrong filing procedure | EUR 250 / EUR 400 per return | KB nr. 44 annex, section 1, I.D and I.E; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Client listing not filed, or more than 9 months late | EUR 3,000 per listing | KB nr. 44 annex, section 1, IV.1; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Client listing up to 3 months late | Nil listing EUR 50; otherwise EUR 25 per customer, minimum 75, maximum 1,500 | KB nr. 44 annex, section 1, IV.1.B; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Client listing more than 3 and at most 9 months late | Nil listing EUR 150; otherwise EUR 75 per customer, minimum 225, maximum 2,250 | KB nr. 44 annex, section 1, IV.1.B; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Intra-EU listing not filed, or more than 6 months late | Part 1 EUR 3,000; part 2 EUR 1,500 | KB nr. 44 annex, section 1, IV.2; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Intra-EU listing up to 2 months late | Part 1 EUR 25, part 2 EUR 15 per person listed; minimum 75, maximum 1,500 | KB nr. 44 annex, section 1, IV.2.B; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Intra-EU listing more than 2 and at most 6 months late | Part 1 EUR 75, part 2 EUR 45 per person; minimum 225, maximum 2,250 | KB nr. 44 annex, section 1, IV.2.B; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Invoice not issued on time | Per invoice EUR 50 (max 500), then 125 (max 1,250), then 250 (max 5,000) | KB nr. 44 annex, section 2, I.A (from 1 January 2026); https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| No technical means to issue and receive structured e-invoices | EUR 1,500, then 3,000, then 5,000; a later offence counts only if found at least 3 months after the previous fine | KB nr. 44 annex, section 2, I.C; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac |
| Rounding of fines | The total fine is rounded down to the euro below EUR 250 and to the ten euros above | KB nr. 41 art. 4 § 1; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d48c176f-6bdd-41fb-b0a1-725841887613 |
| Spontaneous correction | Full remission of these proportional fines for spontaneous correction before any intervention by a tax administration; do not extend this decree to fixed fines | KB nr. 41 art. 3; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d48c176f-6bdd-41fb-b0a1-725841887613 |


**Tolerance in early 2026.** FOD Financiën applied no penalties during the first three months of 2026 (January to March) for offences specific to the new e-invoicing obligation: not yet having the technical means to send or receive a structured e-invoice, or not issuing one because the business's own system, or a third party's, could not yet produce a valid one. The condition is that the business can show it took steps in a timely and reasonable manner. The invoice still had to be issued in another format or by another channel. Each case is assessed individually and there is no general postponement ([einvoice.belgium.be, tolerance during the first three months of 2026](https://einvoice.belgium.be/en/news/period-tolerance-during-first-three-months-2026)). For self-billing invoices the administration is lenient until 30 June 2026 where sending or receiving them is not yet technically possible, if the business shows its software supplier is still building the function; until then they may be made and sent another way, with no fine for sender or receiver ([efactuur.belgium.be FAQ B2B, question 23](https://efactuur.belgium.be/nl/FAQ/algemene-vragen-b2b)).

The KB nr. 41 scale does not apply to evasion or enabling evasion (art. 1). KB nr. 44 repeat-offence counting looks back four years and requires the earlier same offence to have been penalised before the new offence; evasion doubles the highest applicable fixed fine, capped at EUR 5,000 (arts. 2–3). The worked fines below illustrate the statutory scale before any remission or case-specific relief, assuming no evasion and no spontaneous-correction relief. A summer late-filing fine waiver does not itself establish a 5% payment fine: the return remains late. For its actual payment-fine treatment, Check this point with one of our partner accountants.

## Cross-border points

- **Services bought from EU suppliers** under the general B2B rule: base in 88, VAT in 55, deductible part in 59. **From non-EU suppliers:** base in 87, VAT in 56, deductible part in 59 (KB nr. 1 annex II).
- **Intra-EU acquisitions of goods:** base in 86, VAT in 55.
- **Sales to EU businesses:** services in 44, goods in 46, and both on the intra-EU listing; the customer's EU VAT number is needed.
- **Non-established suppliers selling goods in Belgium** to a Belgian-established customer that files returns: the customer pays the VAT (art. 51 § 2, 5°). A supplier with a Belgian fixed establishment not involved in the supply counts as non-established (art. 51 § 2, second paragraph).
- **Foreign businesses** without a Belgian fixed establishment are outside the mandate according to the official e-invoice FAQ; the statutory issuing rule addresses Belgian-established taxpayers. A Belgian fixed establishment requires a separate scope check, not a blanket foreign-business exclusion. Check this point with one of our partner accountants. A business not established in Belgium may use the Belgian small-business exemption only through the EU scheme (art. 56ter § 2).
- **Distance sales and e-services to EU consumers** require the place-of-supply and SME tests before choosing OSS or local registration; OSS is not mandatory for every such sale. Use `eu-vat-directive`. No cross-border consumer or platform return is prepared here. Check this point with one of our partner accountants.

## Worked examples

**Example 1: monthly return of a construction company, September 2026.** A Belgian BV files monthly. In September 2026 it invoices EUR 60,000 of renovation work to a general contractor that files Belgian VAT returns: reverse charge, grid 45, no VAT on the invoice. Assume ordinary standard-rated commercial work and full taxable-business-use deduction on the purchases. It also invoices EUR 10,000 of work at 21% to a business customer that does not file returns (an art. 44 exempt medical practice), so the BV charges VAT: grid 03, VAT 2,100 in grid 54. It receives EUR 25,000 of subcontracted tiling under reverse charge: grid 87, VAT 5,250 in grid 56, deducted in grid 59. It buys EUR 8,000 of materials at 21% (grid 81, VAT 1,680). VAT due is 2,100 + 5,250 = 7,350. Deductible VAT is 5,250 + 1,680 = 6,930. Grid 71 is 420, filed and paid by 20 October 2026.

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

**Example 2: quarterly return Q3 2026 with EU services, paid late, and a late client listing.** A consultancy files quarterly, has full deduction on documented taxable-business purchases, and supplies ordinary general-rule services to customers acting as businesses at their other-EU establishments, liable for destination VAT. In Q3 2026 it invoices EUR 20,000 at 21% to Belgian clients (grid 03, VAT 4,200 in 54) and EUR 30,000 of services to EU businesses (grid 44 and the intra-EU listing). It buys EUR 2,000 of advertising from an Irish entity (grid 88, VAT 420 in 55), EUR 1,000 of software from a US entity (grid 87, VAT 210 in 56) and EUR 5,000 of Belgian services at 21% (VAT 1,050). VAT due is 4,830; deductible VAT is 1,680; grid 71 is 3,150. The return is filed on time by 25 October 2026 but paid on 20 December 2026. Interest runs from 26 October: two started months, so 3,150 × 8% × 2/12 = EUR 42. The fine for late payment with a timely return is 5%, EUR 157.50, rounded down to EUR 157 (KB nr. 41 art. 4). Separately, its 2026 client listing of 12 customers, due before 31 March 2027, is filed two months late: 12 × EUR 25 = EUR 300, inside the EUR 75 to EUR 1,500 range.

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

**Example 3: quarterly return, Q3 2026, with car and restaurant limits.** A Belgian BV files quarterly. In July to September 2026 it invoices EUR 80,000 of consultancy at 21%. It buys EUR 30,000 of goods and services at 21%, has EUR 4,000 net of costs on a passenger car at 21%, and a EUR 500 net client dinner at 12%. Output VAT is 80,000 × 21% = 16,800 (grid 54). Input VAT on the general purchases is 6,300. The car VAT is 840, of which 50% is deductible: 420, assuming demonstrated business use supports at least that capped share. The dinner VAT of 60 is not deductible. Grid 82 includes the EUR 60 blocked VAT, and the car purchase-cost grid includes its EUR 420 blocked VAT. Deductible VAT in grid 59 is 6,720. VAT payable in grid 71 is 10,080, due with the return by 25 October 2026. If it pays a month late but filed on time, the fine is 5% of 10,080, which is EUR 504. A total fine above EUR 250 is rounded down to the ten euros (KB nr. 41 art. 4 § 1), so the fine is EUR 500. Late interest at 8% for one month is EUR 67.20.

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

**Example 4: the small-business exemption and its 10% tolerance.** A self-employed designer has used the exemption for years. By 30 November 2026 her 2026 turnover is EUR 24,000. Assume only ordinary standard-rated design services and no excluded activity or other turnover. In December she invoices EUR 2,500 more, so the year ends at EUR 26,500. That is EUR 1,500 over the EUR 25,000 limit, or 6%. Because the excess is no more than 10% (the ceiling is EUR 27,500), she keeps the exemption for all of 2026 and charges no VAT on the December invoices. But she exceeded the limit in 2026, so she cannot use the exemption in 2027, even though the enacted 2027 limit is EUR 26,000 (art. 56decies § 1). From 1 January 2027 she charges 21%. On EUR 3,000 of January 2027 invoices that is EUR 630. Had her December invoices been EUR 4,000 (year total EUR 28,000, 12% over), the exemption would have ended during December, at the moment the 10% margin was passed.

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

### Original transaction cases retained

These cases preserve the historical inputs; the grid and deduction conditions above control. Amounts are EUR unless stated. For purchases, grids 81–83 exclude only deductible VAT. A positive bank credit is not enough to establish a sale. Standard-rated general B2B services below assume no involved supplier establishment in Belgium, no place-of-supply exception, proper evidence and full taxable business use where full deduction is shown. For qualifying EU goods, require actual cross-border transport, the customer's communicated other-state VAT identification and the required listing; SME and margin exclusions still apply (see `eu-vat-directive`).

| Original case / input | Corrected result or bounded hold |
|---|---|
| 3 April 2026, NOTION LABS INC, debit USD 16.00, recorded EUR 14.68 subscription | Keep the recorded conversion as a case input, not a claimed exchange rate. On those facts: 82 and 87 = 14.68; 56 = 3.08; deductible 59 = 3.08. It is not grid 63. |
| 10 April 2026, GOOGLE IRELAND LIMITED, debit EUR 850 advertising | 82 and 88 = 850; 55 = 178.50; deductible 59 = 178.50. Billing entity is a stated case fact, not a brand rule. |
| 15 April 2026, COMME CHEZ SOI BRUXELLES, debit EUR 220 business dinner | Client hospitality is blocked: 82 = 220 gross; 59 = 0. Names/business purpose alone do not create deduction. Do not infer the food/drink VAT split from the bank amount. |
| 18 April 2026, DELL BELGIQUE SA, Laptop XPS 15, debit EUR 1,595 gross at 21% | Arithmetic: net 1,318.18; VAT 276.82. If documented as a qualifying capital purchase for fully taxable use: 83 = 1,318.18; 59 = 276.82. No universal monetary capitalisation threshold or actual adjustment is asserted here. |
| 22 April 2026, STUDIO KREBS GMBH, invoice BE-2026-018, credit EUR 3,500 IT consultancy | On qualifying general B2B destination-taxed facts: 44 = 3,500, no Belgian output VAT, include in intra-EU listing. This is not a domestic zero rate or grid 45. |
| 28 April 2026, ARVAL BELGIUM, BMW 3 Series lease, debit EUR 650 gross | At the stipulated 21%, net 537.19 and VAT 112.81. The original automatic 50% default and EUR 56.40 recovery are not a usable deduction decision. Actual business use, invoice rounding and the capped claim must be established. Check this point with one of our partner accountants. |
| Historical test 1: Belgian office supplies, 242 gross = 200 net + 42 VAT | With full deduction: 82 = 200; 59 = 42. |
| Historical test 2 / SaaS edge case: US software, 100/month, no VAT | 82 and 87 = 100; 56 = 21; deductible 59 = 21; net 0. |
| Historical test 3: French raw materials shipped to Belgium, 5,000, no VAT | Qualifying taxable acquisition at 21%: 81 and 86 = 5,000; 55 = 1,050; deductible 59 = 1,050. |
| Historical test 4: goods, Belgium to Germany, 3,000; valid DE VAT number | Subject also to transport, reporting and all exemption conditions: 46 = 3,000, no Belgian output VAT; list the customer. It is not grid 45. |
| Historical test 5: exempt small business, turnover 18,000; furniture 500 + 105 VAT | Assuming scheme eligibility: no periodic return for exempt supplies and no input deduction; gross cost 605. |
| Historical test 6 / car-base case: passenger car 25,000 + 5,250 VAT; no logbook | Do not assume 50% because evidence is absent. Only if the supported deductible share reaches the cap: 59 = 2,625; 83 = 27,625 including blocked VAT. Actual share remains held until established. Check this point with one of our partner accountants. |
| Historical car edge case: passenger car 30,000 + 6,300 VAT; either no proof or proven 75% business use | No proof gives no automatic deduction. If 75% taxable business use is proved and the ordinary car cap applies, deduction remains 50%: 59 = 3,150; 83 = 33,150. The former 4,725 deduction and 31,575 purchase amount are wrong. |
| Historical test 7: Italian hotel, 300 including Italian IVA; German hotel edge case | Foreign VAT is not Belgian input VAT in 59. Do not reverse-charge accommodation merely because the supplier is foreign. Foreign recovery is a separate claim subject to the destination rules; a Belgian purchase-grid amount depends on the recoverable portion. Check this point with one of our partner accountants. |
| Historical test 8: Belgian commercial-office renovation, 10,000 without VAT, both VAT-registered | Registration alone is insufficient: require a Belgian-established supplier, qualifying work and a customer filing periodic returns. At stipulated 21% with full deductible use: supplier 45 = 10,000; customer 82/83 as appropriate and 87 = 10,000, 56 = 2,100, 59 = 2,100. |
| Historical test 9: client reception, 3,000 + 630 VAT | As stipulated reception costs: 82 = 3,630; 59 = 0. The quoted 21% is an original invoice input, not a restaurant/catering rate decision. |
| Historical test 10: client lunch, food 80 + 9.60 VAT, drinks 20 + 4.20 VAT | Blocked client meal: 82 = 113.80; 59 = 0. The former 13.80 deduction is wrong. |
| Historical test 11: renovation of private dwelling built in 2005, homeowner; 15,000 + 900 VAT | 15,000 × 6% = 900 is arithmetic only. Age alone does not establish the renovation rate: the exact works, first occupation, use, end-consumer and invoice/exclusion conditions must be met. No filing outcome for this particular job is supplied until that classification is proved. Check this point with one of our partner accountants. |
| Historical test 12: manufactured goods exported to United States, invoice 20,000 without VAT | Once the export exemption and documentary conditions are established: 47 = 20,000, no output VAT. It is not grid 46 or 00. Actual exemption eligibility must be supported. |
| Historical test 13: domestic service credit note, 500 + 105 VAT previously fully deducted | 85 = 500; reduce 82 by 500; repay 105 in 63. Do not also reduce 59 by the same 105, and do not use 84/57. |
| Historical test 14: German advisory service, 2,000, no VAT | General B2B rule: 82 and 88 = 2,000; 55 = 420; deductible 59 = 420. |
| Historical mixed-use building: 30% office / 70% private, costs 200,000 + 42,000 VAT | Arithmetic at a stipulated 30% eligible share: 12,600 deductible, 29,400 blocked, 83 = 229,400. This does not establish the allocation, election or adjustment for the property; no actual filing conclusion is supplied. Check this point with one of our partner accountants. |
| Historical meal/reception edge case: lunch 100 + 12 VAT and 4.20 drinks VAT; separate reception for 50 clients, 5,000 + 1,050 VAT | Client meal VAT recovery = 0; confirm the invoice's food/drink bases before fixing 82. For the stated reception: 82 = 6,050, 59 = 0. Both original VAT amounts remain case inputs; no business-purpose deduction exception is invented. |
| Historical triangulation: Belgian intermediary buys in Netherlands, sells to France; goods go NL to FR | Preserve the corridor; do not infer simplification from transport alone. No triangulation liability/invoice outcome is supplied here. Check this point with one of our partner accountants. |

Keep transaction-level records of date, counterparty, document, currency, net, invoice VAT, deduction share, reverse-charge VAT, grids and unresolved questions; aggregate by grid and reconcile to the return. Preserve the original CSV date format, semicolon delimiters and currency conversion evidence rather than guessing from an IBAN or structured communication. Check supplier billing entities for bank/processor subscriptions, utilities, post/logistics, transport, supermarkets, SaaS, professional services and property. Payroll/social/tax names are prompts to identify the underlying payment, not universal supplier exclusions. Retain prior credits separately and save the filing acknowledgement and payment evidence. The working-paper method remains in `vat-workflow-base`.

## Ask the client first

- What is your annual turnover for the whole activity, and do your intra-EU supplies of goods exceed EUR 50,000 in any quarter? What was your turnover in Belgium in 2025, what do you expect for 2026, and when did you start? (Monthly or quarterly returns and listings; the EUR 25,000 exemption, its pro rata limit and the 10% tolerance.)
- Do you do construction work or installations, and do your customers file Belgian VAT returns? Do you run a registered cash system, deal in scrap, or belong to a VAT unit? (Decides reverse charge on sales and the invoice wording; these exclude the exemption.)
- Who are your foreign suppliers, by legal entity and country on the invoice? (Grids 86, 87, 88 and self-assessed VAT.)
- Do you have cars, restaurant, hotel or reception costs? (50% limit and blocked VAT.)
- Do you also make exempt supplies such as letting, medical care or financial services? (Pro rata; refer.)
- Can your software send and receive structured e-invoices, and were any 2026 returns, payments or listings late? (Fines and interest.)

## Sources

The Dutch operative provisions and the cited instructions below were actually read on 27 November 2026. Fisconet HTML was read in the browser or decoded from its official public-document endpoint; annex II was read as the official PDF, including the operative grids before the historical versions. Failed fetches and blank JavaScript shells were not evidence. Article/section labels specify what was read, not a claim to have audited every provision of the Code.

| Source / operative passages read | URL | Read on |
|---|---|---|
| WBTW arts. 4, 26, 28: taxable person and ordinary base | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4cbef7fa-98c3-430b-9ed8-32aa1a1db95c ; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/caf77db0-3975-4a4a-a5b5-9b8382c69a35 ; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d99cb5ca-ea22-48f6-9154-4b28a709771d | 2026-11-27 |
| WBTW art. 45: taxable use, mixed private use, car cap/exceptions, blocked expenses | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/58a466d6-c626-4369-854f-add149c06034 | 2026-11-27 |
| WBTW art. 48 § 2: adjustment framework, including 20 February 2026 amendment | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c6328e66-dd56-4eb1-b365-eeb022566d3d | 2026-11-27 |
| WBTW art. 51 §§ 1–2: liability and establishments | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/09a92203-ce33-4e57-8620-fbbfcdbfbbf0 | 2026-11-27 |
| WBTW art. 53: returns, replacement procedure, e-invoice requirements and historical commencement | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/773cb22d-053e-4d4d-ae1f-7ddadab87d78 | 2026-11-27 |
| WBTW arts. 53quinquies and 56bis: listing and SME exclusions/no deduction | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/94b855fa-1105-42e6-9944-0310b45bc31e ; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0cd39ffd-676c-4846-b0c7-2328b1e94524 | 2026-11-27 |
| WBTW arts. 56ter, 56nonies, 56decies: 2026 limit, composition, overrun and lookback | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6191791d-e4d1-4829-b8f1-56c7a6892136 ; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c47be544-0837-4bcf-8de1-4034b9c5fecb ; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/83f1a474-d23d-446b-ac69-284f8909b300 | 2026-11-27 |
| WBTW arts. 56quater, 56septies: EX start/notice and reporting conditions | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4d1f067f-e125-46d0-855d-3b4228daa289 ; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/65d1e5eb-b0a4-4eb1-af80-374c06a44892 | 2026-11-27 |
| Law 23 September 2026 arts. 26–27: enacted future thresholds and commencement, actual Gazette text | https://www.ejustice.just.fgov.be/eli/wet/2026/09/23/2026007237/staatsblad | 2026-11-27 |
| KB nr. 1 arts. 17–18, 20–20ter: filing, construction, wording and specialist reverse charges | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c69c7ee9-8e6d-48da-b9f7-c23cb025a777 | 2026-11-27 |
| KB nr. 1 annex II, operative 10 April 2021 text: grids and totals | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0ac584ed-a3ad-4734-9537-160f30357de5 | 2026-11-27 |
| KB nr. 20 art. 1, art. 1quater/1 and rate tables: statutory framework, hotel/pesticide changes, heat-pump limitations | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 | 2026-11-27 |
| KB nr. 23 arts. 1–2: listing date/content/electronic filing | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0e6d7db6-7de7-480e-89ab-5d0763e32251 | 2026-11-27 |
| KB nr. 50 arts. 1, 5–7, 9, 11: EU listings and annual farmers' exception | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/90c85f66-9e8b-48bc-9032-ce1f7db88872 | 2026-11-27 |
| KB nr. 41 arts. 1, 3–4 and Table G first division: reduced fines and relief | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d48c176f-6bdd-41fb-b0a1-725841887613 | 2026-11-27 |
| KB nr. 44 arts. 2–3, annex divisions 1 I/IV and 2 I: fixed fines/recurrence | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac | 2026-11-27 |
| WBTW art. 76 § 1; KB nr. 4 art. 8/1 §§ 1–3: refund request/conditions/timing/crediting and holds | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/11d42f57-9159-47a5-b967-004f74497d5c ; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/78a784be-1c34-497c-90e0-330c2ae62768 | 2026-11-27 |
| WBTW art. 91 §§ 1, 4–5; FOD payment FAQ: 2026 interest and interest-month boundaries | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/87160bad-16b2-40ce-9abf-756a527f77a9 ; https://financien.belgium.be/nl/ondernemingen/btw/betaling-teruggave/betaling | 2026-11-27 |
| FOD periodic-return FAQ and both expanded 2026 calendar tables: filing/payment, summer relief, paper exception | https://financien.belgium.be/nl/ondernemingen/btw/aangifte/periodieke-aangifte ; https://financien.belgium.be/nl/ondernemingen/btw/btw-kalender | 2026-11-27 |
| FOD client listing FAQ: EUR 250 administrative floor, exclusions, turnover including zero | https://financien.belgium.be/nl/ondernemingen/btw/aangifte/jaarlijkse_klantenlisting | 2026-11-27 |
| FOD provision-account implementation and operation; older circular's deferral checked against these later 2026 instructions | https://financien.belgium.be/nl/ondernemingen/btw/betaling-teruggave/btw-rekening-courant ; https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f8fe3162-0f49-4040-9285-8ded195cd922 | 2026-11-27 |
| FOD/BOSA Dutch e-invoice tolerance notice; B2B FAQ questions 2, 8, 14, 23 | https://einvoice.belgium.be/nl/news/tolerantieperiode-eerste-drie-maanden-2026 ; https://efactuur.belgium.be/nl/FAQ/algemene-vragen-b2b | 2026-11-27 |
| EU general B2B place/liability, acquisition exemption and deduction conditions; unchanged applicable source reads reused from `eu-vat-directive` | https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng | 2026-11-27 (completed read reused) |

Not yet confirmed: no unverified outcome is usable. The following specific outcomes remain on hold: the 2027 interest rate; January/February 2026 start-up proration and prior-year proration interactions; detailed reduced/zero-rate product classification (including renovation, heat pumps, energy, agricultural inputs, publications, admission, repairs, hygiene products, defibrillators, social housing, copyright, demolition and historic hotel booking transition); short-term letting/Airbnb and platform sales; gift-deduction cutoffs; pro-rata/actual-use methods; asset definitions and actual adjustments; fiscal representation, triangulation, call-off-stock movements and special schemes; pre-May VAT-chain transitional accounts; actual moratorium-interest computation; disputed summer payment fines; invoice-language regional requirements; Intrastat and annual accounts. Check this point with one of our partner accountants. The former hotel booking claim (reservation before 1 March 2026, payment/invoice by 30 June 2026, 6%) is retained only as this non-usable historical outcome, not as an established transition. The former EUR 50 gift cutoff and CO2/car-use formulas are likewise not usable VAT rules. Direct-tax rates and social/payroll computations are routed to the relevant Guides. Internal EUR 5,000 transaction and EUR 400 default-delta flags were working conventions, not law; do not treat them as legal thresholds.

> Contributed by OpenAccountants.
