---
name: belgium-vat-return
description: "Belgian VAT (btw / TVA) for tax year 2026: who must charge it, the 21%, 12%, 6% and 0% rates (hotels and campsites moved from 6% to 12% on 1 March 2026), the small-business exemption at EUR 25,000 with its 10% tolerance and the rises to EUR 26,000-30,000 from 2027, the EU small-business scheme (EUR 100,000), monthly or quarterly returns (EUR 2,500,000 test), the 20th and 25th deadlines, the end of the summer holiday extension in 2026, refunds on request and the VAT provision account, the replacement return, mandatory structured B2B e-invoicing from 1 January 2026, late interest (8% in 2026) and the fines in Royal Decrees 41 and 44. Trigger on: Belgian VAT, btw-aangifte, déclaration TVA, Intervat, kwartaalaangifte, vrijstellingsregeling kleine ondernemingen, franchise TVA, vervangende aangifte, Peppol Belgium, btw-boete. Out of scope: e-invoice formats and Peppol set-up (belgium-einvoice), bookkeeping (belgium-bookkeeping), income tax (be-income-tax), corporate tax (be-corporate-tax)."
version: 2.3
jurisdiction: BE
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
  - eu-vat-directive
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium VAT (btw / TVA): rates, thresholds, returns and penalties, tax year 2026 v2.3

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Belgium.

**What this skill does.** It sets out the law layer of Belgian VAT for 2026: who is in, the rates, the small-business exemption, return frequency, deadlines, refunds, e-invoicing and penalties. Figures come from the VAT Code (Wetboek van de belasting over de toegevoegde waarde, "WBTW", Law of 3 July 1969) and its Royal Decrees (KB nr. 1, 20, 41 and 44), read in the official coordination on FisconetPlus, from amending laws in the Belgisch Staatsblad, and from FOD Financiën pages.

**Sibling skills.** [be-vat-return](be-vat-return.md) covers preparing the return: the full grid map, reverse charges, listings and their fines. [belgium-einvoice](belgium-einvoice.md) covers Peppol and invoice formats. [belgium-bookkeeping](belgium-bookkeeping.md), [be-income-tax](be-income-tax.md) and [be-corporate-tax](be-corporate-tax.md) cover the rest. Load `vat-workflow-base` and `eu-vat-directive` alongside.

## Who this applies to

- **Taxable persons.** Anyone who carries on an economic activity and supplies goods or services in Belgium for consideration. Companies, sole traders and foreign businesses supplying in Belgium are all in.
- **Who files the periodic return.** Every taxable person with a right to deduct files a periodic return (WBTW art. 53 § 1). No return is filed by a business under the small-business exemption, under the special scheme for farmers, or making only exempt supplies under art. 44 with no right to deduct. A business under the small-business exemption still files the start, change and end-of-activity declarations (art. 53 § 1, second paragraph). The others are listed on the FOD Financiën periodic return page.
- **Small-business exemption (vrijstellingsregeling / franchise).** A business established in Belgium whose annual turnover in Belgium does not exceed EUR 25,000 may choose not to charge VAT (art. 56ter § 1). The limit is cut pro rata for a business that starts during the year, by the days from 1 January to the start date. Joint owners count their turnover together; spouses with separate activities count separately. The business must notify the VAT administration in advance. It cannot deduct input VAT (art. 56bis § 4). It reports its annual turnover for the previous year before 31 March (for 2025: before 31 March 2026; FOD Financiën, btw-kalender).
- **Who cannot use the exemption.** VAT units; businesses that regularly do construction work (except some services by individuals through platforms), businesses that must issue a till receipt from a registered cash system, and dealers in scrap and waste (art. 56bis § 2). The exemption also never covers art. 8 transactions, intra-EU supplies of new means of transport, margin-scheme supplies (art. 58 §§ 1-2), undeclared or unlawful transactions, or hotel-type furnished accommodation under art. 44 § 3, 2°, a), third dash (except some supplies by individuals under art. 50 § 4) (art. 56bis § 3).
- **Crossing the limit.** If the year's turnover exceeds EUR 25,000 by 10% or less (up to EUR 27,500), the business keeps the exemption for that year. If it exceeds it by more than 10%, the exemption ends from that moment. A business that exceeded the limit in the previous year cannot use the exemption for the following calendar year (art. 56decies § 1).
- **Limits already legislated for later years.** EUR 26,000 for 2027, EUR 27,000 for 2028, EUR 28,000 for 2029, EUR 29,000 for 2030 and EUR 30,000 from 2031 (art. 56ter § 1 as replaced by art. 26 of the Law of 23 September 2026, in force 1 January 2027).
- **EU small-business scheme.** A business established in another EU state can use the Belgian exemption if its EU turnover is at most EUR 100,000 and its Belgian turnover at most EUR 25,000. It notifies its home state, which issues a number with the suffix "EX" (art. 56ter § 2). It loses the scheme once EU turnover exceeds EUR 100,000 (art. 56decies § 2). It does not register or file Belgian returns for the exempt supplies (art. 56septies § 1). A Belgian business can use another state's exemption after prior notice to the Belgian administration and gets a Belgian number with the suffix "EX" (art. 56quater).
- **Out of scope here.** The flat-rate scheme (forfaitaire regeling, art. 56 and KB nr. 2), farmers' special scheme (art. 57), margin schemes, VAT units, travel agents and bankrupt estates. Refer them.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 21% | 2026 | KB nr. 20 art. 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Reduced rate, Table B (restaurant and catering services, excluding drinks; furnished accommodation and campsites from 1 March 2026; other listed items) | 12% | 2026 | KB nr. 20 art. 1 and Table B, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Reduced rate, Table A (food, water, medicines and medical devices, books and newspapers, passenger transport, cultural and sport admission, work on private homes under conditions, and other listed items) | 6% | 2026 | KB nr. 20 art. 1 and Table A, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Zero rate, Table C (certain periodical publications and other listed items) | 0% | 2026 | KB nr. 20 art. 1 and Table C, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Hotels (furnished accommodation, with or without breakfast) and campsites: from 6% to 12% | 12% from 1 March 2026 | 2026 | KB 14 February 2026 art. 2, 4 and 5, https://www.ejustice.just.fgov.be/eli/besluit/2026/02/14/2026001322/staatsblad |
| Pesticides and plant-protection products: from 12% to 21% | 21% from 1 March 2026 | 2026 | KB 14 February 2026 art. 3 and 5, https://www.ejustice.just.fgov.be/eli/besluit/2026/02/14/2026001322/staatsblad |
| Heat pumps for heating supplied and installed in, on or next to homes, 1 January 2026 to 31 December 2030, for end consumers and private dwellings; not when combined with a non-electric heater on the same system | 6% | 2026 | KB nr. 20 art. 1quater/1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 |
| Small-business exemption: annual turnover in Belgium | EUR 25,000 | 2026 | WBTW art. 56ter § 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6191791d-e4d1-4829-b8f1-56c7a6892136 |
| Tolerance: exemption kept for the year if the limit is exceeded by no more than | 10% (EUR 27,500) | 2026 | WBTW art. 56decies § 1, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/83f1a474-d23d-446b-ac69-284f8909b300 |
| Small-business exemption limit for 2027 / 2028 / 2029 / 2030 / 2031 onwards | EUR 26,000 / 27,000 / 28,000 / 29,000 / 30,000 | 2027-2031 | Law of 23 September 2026 art. 26-27, https://www.ejustice.just.fgov.be/eli/wet/2026/09/23/2026007237/staatsblad |
| EU small-business scheme: EU-wide turnover cap | EUR 100,000 | 2026 | WBTW art. 56ter § 2, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6191791d-e4d1-4829-b8f1-56c7a6892136 |
| Quarterly returns allowed if annual turnover, excluding VAT, for the whole activity does not exceed | EUR 2,500,000 | 2026 | KB nr. 1 art. 17 § 2, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c69c7ee9-8e6d-48da-b9f7-c23cb025a777 |
| Monthly EU sales listing (and so monthly returns) once intra-EU supplies in a quarter, or one of the four before, exceed | EUR 50,000 | 2026 | FOD Financiën, periodic return page, https://financien.belgium.be/nl/ondernemingen/btw/aangifte/periodieke-aangifte |
| Replacement return when no return is filed: highest grid 71 of the last 12 months, and at least | EUR 2,100 | 2026 | WBTW art. 53 § 1ter, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/773cb22d-053e-4d4d-ae1f-7ddadab87d78 |
| Input VAT on cars and their costs: maximum deduction | 50% | 2026 | WBTW art. 45 § 2, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/58a466d6-c626-4369-854f-add149c06034 |
| Late payment interest (fiscal rate 4% plus 4 points) | 8% a year | 2026 | WBTW art. 91 § 1; FOD Financiën, payment page, https://financien.belgium.be/nl/ondernemingen/btw/betaling-teruggave/betaling |
| Interest paid by the State on late refunds (late rate minus 2 points) | 6% a year | 2026 | WBTW art. 91 § 4, https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/87160bad-16b2-40ce-9abf-756a527f77a9 |

## The taxable base

- **What is taxed.** Supplies of goods and services in Belgium, intra-EU acquisitions, imports, and services bought from abroad where the Belgian customer pays the VAT. The base is the consideration excluding VAT.
- **Exempt without deduction.** The supplies listed in art. 44 (for example medical care, education, most financial and insurance services, letting of immovable property). A business with only these supplies files no periodic return.
- **Domestic reverse charge.** The customer pays the VAT on construction work (werk in onroerende staat) and the related installations listed in KB nr. 1 art. 20, when the customer itself files periodic returns. The supplier's invoice carries no VAT.
- **Input VAT.** Deductible on purchases used for taxable supplies (art. 45 § 1). Limited to 50% on cars used to carry people or goods by road and on goods and services for them, with exceptions for some vehicle types listed in art. 45 § 2. Not deductible at all: tobacco, spirits not for resale, accommodation, food and drink costs (with exceptions) and reception costs (art. 45 § 3).
- **Capital goods.** Deduction on capital goods is subject to adjustment. For immovable capital goods the adjustment period is 15 years, and 25 years for buildings let under the art. 44 § 3, 2°, d) regime (art. 48 § 2 as amended by the Law of 10 February 2026).
- **Credits.** An excess of deductible VAT goes to the taxpayer's VAT provision account unless a refund is asked for in the return (art. 76 § 1).

**Classifying transactions onto the return.** The grid numbers are those of KB nr. 1 annex II.

| Transaction | Base grid | VAT grid | Notes |
|---|---|---|---|
| Domestic sale at 6% / 12% / 21% | 01 / 02 / 03 | 54 | Rate from KB nr. 20 Tables A and B |
| Domestic sale where the customer pays the VAT (construction under KB nr. 1 art. 20, other art. 51 § 2 cases) | 45 | none | Invoice shows no VAT |
| Services to an EU business under the general place-of-supply rule | 44 | none | Also on the EU sales listing |
| Exempt intra-EU supply of goods (art. 39bis) | 46 | none | Customer's EU VAT number needed |
| Exports and other exempt supplies with a right to deduct (art. 39 to 42) | 47 | none | |
| Credit notes issued | 48 (on 44 and 46) or 49 (others) | 64 | VAT recovered on credit notes issued |
| Domestic purchase with Belgian VAT: goods for resale and raw materials / other goods and services / capital goods | 81 / 82 / 83 | 59 (deductible part) | Art. 45 limits apply |
| Intra-EU acquisition of goods | 86 (and 81-83) | 55, deducted in 59 | |
| Services from an EU supplier, place of supply in Belgium | 88 (and 81-83) | 55, deducted in 59 | |
| Services from a non-EU supplier, construction work received under KB nr. 1 art. 20, other customer-pays cases | 87 (and 81-83) | 56, deducted in 59 | |
| Credit notes received | 84 (on 86 and 88) or 85 (others) | 63 | VAT to repay on credit notes received |

- **Not on the return at all.** Wages, social contributions, tax payments, fines, loan capital and interest received or paid, dividends, transfers between own accounts and owner injections or withdrawals involve no supply.
- **Exempt purchases: no VAT to deduct.** Bank charges and other financial services, insurance and the letting of immovable property are exempt under art. 44, so the invoice carries no Belgian VAT.
- **Partly or wholly blocked.** Car costs including fuel: deduction at most 50% (art. 45 § 2). Restaurant, hotel and reception costs, tobacco and spirits not for resale: no deduction (art. 45 § 3).
- **Foreign suppliers.** Read the legal entity and VAT number on the invoice, not the brand name: an EU entity goes in 88 or 86, a non-EU entity in 87. If the invoice charges Belgian VAT, treat it as a domestic purchase.

## Deadlines and filing

- **Frequency.** Monthly is the rule (art. 53 § 1). A business may file quarterly if annual turnover excluding VAT for its whole activity is at most EUR 2,500,000, unless it must file the EU sales listing monthly (KB nr. 1 art. 17 § 2). A quarterly filer that stops meeting the test moves to monthly at the end of that quarter and must notify the change by the 10th of the next month (art. 17 § 3). The former second test (at most EUR 250,000 of supplies of energy products, mobile phones and computers, and motor vehicles) was removed from 10 January 2026 by the KB of 17 December 2025 (art. 6); the FOD Financiën periodic return page still lists it.
- **Return due dates.** Monthly return by the 20th of the following month. Quarterly return by the 25th of the month after the quarter (KB nr. 1 art. 17 §§ 1-2, rules in force since 1 January 2025). The tax is paid within the same deadline (art. 53 § 1, 3°).
- **2026 calendar.** Quarterly returns: Q4 2025 by 26 January 2026, Q1 2026 by 27 April 2026, Q2 by 25 July 2026, Q3 by 25 October 2026, Q4 2026 by 25 January 2027. Monthly returns are due on the 20th, moved to 22 June 2026 for May, 21 September 2026 for August and 21 December 2026 for November. The payment dates in the calendar are the same as the return dates, and quarterly filers no longer pay quarterly advances (FOD Financiën, btw-kalender).
- **No holiday extension from 2026.** The old summer extension for the June, Q2 and July returns no longer applies; a return filed after the legal date is late. As a transition, no late-filing fine is charged in 2026 if the June 2026 or Q2 2026 return is filed by 10 August 2026, or the July 2026 return by 10 September 2026. The return still counts as late for the other effects: the limitation period runs a year longer, any credit reaches the provision account later, and no refund can be asked through the return for the next 6 months (FOD Financiën, periodic return page).
- **Correcting.** A material error found before the deadline is fixed by filing a new return for the same period, which replaces the first one. After the deadline, the correction goes in the next return (KB nr. 1 art. 17 § 4).
- **Filing.** Electronically through Intervat (KB nr. 1 art. 18).
- **Replacement return (vervangende aangifte).** If a return is not filed, after three months the administration sends a proposed replacement return for the highest VAT due in the previous 12 months, or EUR 2,100 if higher or if there is no earlier return. Filing the missing return within one month ends the procedure. If not, the replacement return becomes final and the tax is payable at once with late interest (art. 53 § 1ter).
- **Refunds.** A credit is refunded only on express request, by the end of the third month after the return period, and only if all returns for the previous six months were filed on time. Otherwise the credit goes to the VAT provision account (art. 76 § 1, as replaced by the Law of 10 February 2026). A refund of the provision account can be asked in MyMinfin.
- **Main return grids.** Base at 6%, 12% and 21%: grids 01, 02, 03. VAT due on them: grid 54. Deductible VAT: grid 59. VAT payable: grid 71. Credit due by the State: grid 72; only one of 71 and 72 is filled (KB nr. 1 annex II).
- **Annual listings.** The annual client listing and the annual EU listing for 2025 were due before 31 March 2026 (FOD Financiën, btw-kalender).
- **Structured e-invoicing from 1 January 2026.** A taxable person established in Belgium must issue a structured electronic invoice for every taxable supply to another Belgian VAT-registered business (art. 53 § 2bis). This includes businesses under the small-business exemption. Flat-rate taxpayers under art. 56 and art. 44 exempt supplies are outside it. Every Belgian VAT-registered customer must be able to receive such invoices. Where the customer cannot receive one for technical reasons, an ordinary invoice is still issued (art. 53 § 2bis, last paragraph, added by the Law of 10 February 2026). Businesses not established in Belgium are not covered (FOD Financiën e-invoicing FAQ). See [belgium-einvoice](belgium-einvoice.md).

## Penalties and interest

| Item | Rule | Source |
|---|---|---|
| Late payment interest | 8% a year in 2026 (fiscal rate 4% plus 4 points). Calculated per month on the VAT due rounded down to EUR 10; each started month counts in full; not charged under EUR 5 a month | WBTW art. 91 § 1; FOD Financiën payment page |
| Late or partial payment, return filed on time | Fine of 5% of the VAT unpaid | KB nr. 41, Table G, section 1, I.1 |
| Late payment, return filed late or within the replacement-return month | 10% of the VAT | KB nr. 41, Table G, I.2 |
| VAT due under a final replacement return | 15% of the VAT | KB nr. 41, Table G, I.3 |
| Periodic return not filed | EUR 500 per return for the 1st offence, EUR 1,250 the 2nd, EUR 2,500 the 3rd, EUR 5,000 after | KB nr. 44 annex, section 1, I.A |
| Periodic return filed up to five months late | EUR 100 per return per month late, maximum EUR 500 | KB nr. 44 annex, section 1, I.B |
| Return wrongly completed | EUR 80 for purely accidental errors, EUR 500 for others, per return | KB nr. 44 annex, section 1, I.C |
| Return filed at the wrong frequency | EUR 250 per return | KB nr. 44 annex, section 1, I.D |
| Invoice not issued on time | Per invoice: EUR 50 (maximum EUR 500), then EUR 125 (maximum EUR 1,250), then EUR 250 (maximum EUR 5,000) | KB nr. 44 annex, section 2, I.A (as amended from 1 January 2026) |
| No technical means to issue and receive structured e-invoices | EUR 1,500 the 1st offence, EUR 3,000 the 2nd, EUR 5,000 after. A later offence counts only if found at least three months after the previous fine | KB nr. 44 annex, section 2, I.C |
| Spontaneous correction | Full remission of proportional fines if the taxpayer corrects before any intervention by the administration | KB nr. 41 art. 3 |

The KB nr. 41 scale does not apply where the offence was committed to evade tax (KB nr. 41 art. 1).

## Cross-border points

- **Services bought from abroad** under the general business-to-business rule: the Belgian customer self-assesses VAT. EU services go in grid 88 with the VAT in grid 55; other reverse-charge purchases go in grid 87 with the VAT in grid 56. The VAT is deducted in grid 59 if the purchase is for taxable use (KB nr. 1 annex II).
- **Intra-EU acquisitions of goods** go in grid 86, with the VAT in grid 55.
- **Services sold to EU businesses** under the general rule go in grid 44 and on the EU sales listing. Intra-EU supplies of goods go in grid 46.
- **EU sales listing.** Quarterly, by the 25th of the month after the quarter (25 January, 25 April, 25 July and 25 October 2026 in the calendar), or monthly by the 20th once intra-EU supplies exceed EUR 50,000 in a quarter. A monthly-listing business cannot file quarterly returns (KB nr. 1 art. 17 § 2; FOD Financiën).
- **Foreign businesses.** A business not established in Belgium is not under the B2B e-invoicing mandate. It may use the Belgian small-business exemption only through the EU scheme (art. 56ter § 2).
- **Sales to EU consumers** of goods at a distance and of e-services above the EU-wide threshold are taxed in the customer's state, usually through the one-stop shop. See `eu-vat-directive`.

## Worked examples

**Example 1: quarterly return, Q3 2026.** A Belgian BV files quarterly. In July to September 2026 it invoices EUR 80,000 of consultancy at 21%. It buys EUR 30,000 of goods and services at 21%, has EUR 4,000 net of costs on a passenger car at 21%, and a EUR 500 net client dinner at 12%. Output VAT is 80,000 × 21% = 16,800 (grid 54). Input VAT on the general purchases is 6,300. The car VAT is 840, of which 50% is deductible: 420. The dinner VAT of 60 is not deductible. Deductible VAT in grid 59 is 6,720. VAT payable in grid 71 is 10,080, due with the return by 25 October 2026. If it pays a month late but filed on time, the fine is 5% of 10,080, which is EUR 504. A total fine above EUR 250 is rounded down to the ten euros (KB nr. 41 art. 4 § 1), so the fine is EUR 500. Late interest at 8% for one month is EUR 67.20.

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

**Example 2: the small-business exemption and its 10% tolerance.** A self-employed designer has used the exemption for years. By 30 November 2026 her 2026 turnover is EUR 24,000. In December she invoices EUR 2,500 more, so the year ends at EUR 26,500. That is EUR 1,500 over the EUR 25,000 limit, or 6%. Because the excess is no more than 10% (the ceiling is EUR 27,500), she keeps the exemption for all of 2026 and charges no VAT on the December invoices. But she exceeded the limit in 2026, so she cannot use the exemption in 2027, even though the 2027 limit is EUR 26,000 (art. 56decies § 1). From 1 January 2027 she charges 21%. On EUR 3,000 of January 2027 invoices that is EUR 630. Had her December invoices been EUR 4,000 (year total EUR 28,000, 12% over), the exemption would have ended during December, at the moment the 10% margin was passed.

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

- What was your turnover in Belgium in 2025, what do you expect for 2026, and when did you start? (Decides the EUR 25,000 exemption, the pro rata limit and the 10% tolerance.)
- What is your annual turnover for the whole activity, and do your intra-EU supplies of goods exceed EUR 50,000 a quarter? (Decides monthly or quarterly returns.)
- Do you do construction work, run a registered cash system, deal in scrap, or belong to a VAT unit? (These exclude the exemption.)
- Do you make exempt supplies such as letting, medical care or financial services? (Decides deduction and whether you file returns.)
- Do you have cars, restaurant, hotel or reception costs? (Decides the 50% limit and blocked VAT.)
- Do you invoice other Belgian businesses, and can your software send and receive Peppol invoices? (Decides e-invoicing compliance.)

## Sources

| Source | URL | Read on |
|---|---|---|
| FisconetPlus, VAT Code table of contents (official coordination to Staatsblad 8 October 2026) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e154233d-dc0e-4c0f-9bbf-afc79e797448 | 2026-10-23 |
| WBTW art. 53 (returns, replacement return, structured e-invoice) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/773cb22d-053e-4d4d-ae1f-7ddadab87d78 | 2026-10-23 |
| WBTW art. 56ter (small-business exemption) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/6191791d-e4d1-4829-b8f1-56c7a6892136 | 2026-10-23 |
| WBTW art. 56decies (losing the exemption, 10% tolerance) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/83f1a474-d23d-446b-ac69-284f8909b300 | 2026-10-23 |
| WBTW art. 45 (deduction limits) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/58a466d6-c626-4369-854f-add149c06034 | 2026-10-23 |
| WBTW art. 76 (refunds) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/11d42f57-9159-47a5-b967-004f74497d5c | 2026-10-23 |
| WBTW art. 91 (interest) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/87160bad-16b2-40ce-9abf-756a527f77a9 | 2026-10-23 |
| KB nr. 1 (return frequency and deadlines) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c69c7ee9-8e6d-48da-b9f7-c23cb025a777 | 2026-10-23 |
| KB nr. 1 art. 17, version history (EUR 250,000 test removed from 10 January 2026) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/bce4326d-6d49-4680-bd6d-8bf05cb7f6bc | 2026-10-23 |
| KB nr. 1 annex II (description of the return grids) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0ac584ed-a3ad-4734-9537-160f30357de5 | 2026-10-23 |
| WBTW art. 56bis (exclusions from the small-business exemption) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0cd39ffd-676c-4846-b0c7-2328b1e94524 | 2026-10-23 |
| KB nr. 20 (rates and Tables A, B and C) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/52d3e79e-132b-4ac6-8ce6-fb79b9634d59 | 2026-10-23 |
| KB nr. 41 (proportional fines) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d48c176f-6bdd-41fb-b0a1-725841887613 | 2026-10-23 |
| KB nr. 44 (non-proportional fines) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1d5dbc36-f527-4d36-8673-b1267367e2ac | 2026-10-23 |
| KB 14 February 2026 (hotels and campsites 12%, pesticides 21%, from 1 March 2026) | https://www.ejustice.just.fgov.be/eli/besluit/2026/02/14/2026001322/staatsblad | 2026-10-23 |
| Law of 10 February 2026, various VAT provisions | https://www.ejustice.just.fgov.be/eli/wet/2026/02/10/2026001291/staatsblad | 2026-10-23 |
| Law of 23 September 2026, art. 26-27 (exemption limits 2027-2031) | https://www.ejustice.just.fgov.be/eli/wet/2026/09/23/2026007237/staatsblad | 2026-10-23 |
| FOD Financiën, periodieke aangifte (no holiday extension in 2026) | https://financien.belgium.be/nl/ondernemingen/btw/aangifte/periodieke-aangifte | 2026-10-23 |
| FOD Financiën, btw-kalender 2026 | https://financien.belgium.be/nl/ondernemingen/btw/btw-kalender | 2026-10-23 |
| FOD Financiën, betaling (late interest 8% for 2026) | https://financien.belgium.be/nl/ondernemingen/btw/betaling-teruggave/betaling | 2026-10-23 |
| FOD Financiën, e-factuur FAQ on the B2B obligation | https://efactuur.belgium.be/nl/FAQ/algemene-vragen-b2b | 2026-10-23 |

Not yet confirmed: whether the pro rata limit for a business that starts mid-year is also the limit tested for the "exceeded in the previous year" bar in art. 56decies; the full item lists of Tables A, B and C are summarised, not reproduced; any tolerance period the administration may grant for the first months of B2B e-invoicing was not found in the sources read.

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
