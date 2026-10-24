---
name: hu-vat-return
description: "Hungarian VAT (általános forgalmi adó, ÁFA) for tax year 2026: who must charge it, the 27%, 18%, 5% and 0% rates (0% for prescription-only medicines from 1 September 2026), the subjective exemption limit of HUF 20 million for 2026 and HUF 22 million for 2027, the EU small-business scheme (EUR 100,000), monthly, quarterly or annual filing set from 2024 data, the 20th-of-the-month and 25 February deadlines, form 2665 and its M sheets, online invoice data reporting, refund minimums, domestic reverse charge, blocked input VAT, cash accounting, late-payment interest and penalties under the Art. Trigger on: Hungarian VAT, áfa bevallás, 2665, alanyi adómentesség, áfa gyakoriság, havi negyedéves éves áfa, Online Számla, fordított adózás, NAV refund. Out of scope: row-by-row classification and the supplier library (hungary-vat-return), invoice software and data format (hungary-einvoice), income tax (hu-income-tax), corporate tax (hu-corporate-tax)."
version: 2.1
jurisdiction: HU
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
  - eu-vat-directive
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Hungary VAT (ÁFA): rates, thresholds, filing and penalties, tax year 2026 v2.1

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Hungary.

**What this skill does.** It sets out the law layer of Hungarian VAT for 2026: who is in, the rates, the exemption and filing thresholds, deadlines, refunds and penalties. Every figure comes from the VAT Act (Act CXXVII of 2007, "Áfa tv.") or the Tax Procedure Act (Act CL of 2017, "Art."), read on the National Legislation Database, and from NAV guidance.

**Sibling skills.** [hungary-vat-return](hungary-vat-return.md) classifies transactions and fills form 2665 row by row, with the supplier pattern library. [hungary-einvoice](hungary-einvoice.md) covers invoice software and Online Számla data. [hu-income-tax](hu-income-tax.md) and [hu-corporate-tax](hu-corporate-tax.md) cover income taxes. Load `vat-workflow-base` and `eu-vat-directive` alongside.

## Who this applies to

- **Taxable persons.** Anyone who carries on an economic activity and supplies goods or services in Hungary for consideration is a VAT taxable person (Áfa tv. 2. § a)). Companies (Kft., Zrt.), sole traders (egyéni vállalkozó) and foreign businesses supplying in Hungary are all in.
- **Subjective exemption (alanyi adómentesség).** A business established in Hungary may choose not to charge VAT for 2026 if its total consideration for supplies, annualised, did not exceed HUF 20,000,000 in 2025 and is neither expected to exceed nor actually exceeds it in 2026 (Áfa tv. 188. § (1)-(2), 377. §). Exceeding the 2025 limit of HUF 18 million in 2025 does not bar the choice for 2026. Sales of fixed assets and intangible rights used in the business, new buildings and building plots, public-interest exempt supplies (85. § (1)), ancillary exempt financial and insurance services (86. § (1) a)-g)) and agricultural special-status supplies are left out of the count (188. § (3)). An exempt business charges no VAT, deducts no input VAT and issues invoices without VAT (187. §).
- **Choosing and losing the exemption.** The choice is notified to NAV by the last day of the year before (192. § (2)), or on registration, when the limit is tested pro rata (189. §). The exemption ends when the limit is actually exceeded during the year. The supply whose consideration crosses the limit is already taxable, and the business may not choose the exemption again until the end of the second calendar year after the year it ended (191. § (1) c), (2), (3)). For 2026 and 2027 the law lifts that bar: a business that meets the year's limit may choose the exemption even if the two-year wait has not run (377. § (2), 378. § (2)).
- **Limits already legislated.** HUF 22,000,000 for 2027 (378. §). NAV's notice also gives HUF 24,000,000 from 2028.
- **EU small-business scheme.** A Hungarian business may use another member state's small-business exemption, and an EU business may use the Hungarian exemption, only if its EU-wide turnover did not exceed EUR 100,000 in the previous year or the current year (195/A. § (3), 195/G. § (3)). It must notify NAV in advance. NAV issues an identification number within 35 working days (195/A. § (4)). The scheme ends once EU turnover exceeds EUR 100,000 in the year (195/K. §).
- **Out of scope here.** VAT groups, margin schemes, travel agents, the agricultural special scheme and import VAT under a NAV licence. Refer them.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 27% | 2026 | Áfa tv. 82. § (1), https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Reduced rate, Annex 3 (for example books, periodicals, certain medicines, pork, poultry, eggs, milk, fish, district heating, internet access, restaurant food and on-site non-alcoholic drinks, commercial accommodation, certain new homes) | 5% | 2026 | Áfa tv. 82. § (2) and Annex 3, https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Reduced rate, Annex 3/A (milk products, flour and cereal bakery products, admission to occasional open-air events) | 18% | 2026 | Áfa tv. 82. § (3) and Annex 3/A, https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Zero rate: daily newspapers (published at least four times a week) | 0% | 2026 | Áfa tv. 82. § (4), Annex 3/B row 1, https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Zero rate: prescription-only medicines and magistral preparations for human use, from 1 September 2026 | 0% | 2026 | Annex 3/B rows 2-3, inserted by Act XL of 2026, in force 1 September 2026, https://njt.jog.gov.hu/jogszabaly/2026-40-00-00 |
| VAT fraction of a VAT-inclusive amount at 27% / 18% / 5% | 21.26% / 15.25% / 4.76% | 2026 | Áfa tv. 83. §, https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Subjective exemption limit for 2026 | HUF 20,000,000 | 2026 | Áfa tv. 188. § (2), 377. §; NAV notice, https://nav.gov.hu/ado/afa/Emelkedik_az_alanyi_adomentesseg_ertekhatara |
| Subjective exemption limit for 2027 | HUF 22,000,000 | 2027 | Áfa tv. 378. §, https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| EU small-business scheme: EU-wide turnover cap | EUR 100,000 | 2026 | Áfa tv. 195/A. § (3), 195/G. § (3), https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Cash accounting (pénzforgalmi elszámolás): turnover cap | HUF 125,000,000 | 2026 | Áfa tv. 196/C. § (1), https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Monthly filing: VAT to be accounted for in 2024, annualised, positive and at least | HUF 1,000,000 | 2026 | Art. 2. melléklet I. B) 3.1.2, https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 |
| Annual filing: 2024 VAT to be accounted for, either sign, below | HUF 250,000 | 2026 | Art. 2. melléklet I. B) 3.1.3.1, https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 |
| Annual filing: net supplies, annualised, not above (and no EU VAT number) | HUF 50,000,000 | 2026 | Art. 2. melléklet I. B) 3.1.3.2, https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 |
| Refund minimum: monthly / quarterly / annual filer | HUF 1,000,000 / 250,000 / 50,000 | 2026 | Áfa tv. 186. § (1) b), https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Refund payout deadline (general) | 75 days | 2026 | Art. 64. § (1), https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 |
| Refund payout where every supplier invoice is paid | 30 days; 45 days if the refund exceeds HUF 1,000,000 | 2026 | Art. 64. § (3), https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 |
| Paper invoice data to NAV: within 4 days, or next day if the invoice VAT is at least | HUF 500,000 | 2026 | Áfa tv. Annex 10 point 3, https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Domestic reverse charge on supplies by a business under insolvency-type procedure, above | HUF 100,000 | 2026 | Áfa tv. 142. § (1) g), https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Distance sales and e-services to EU consumers: Hungarian VAT applies up to | EUR 10,000 a year | 2026 | Áfa tv. 49/A. §, https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| EU sales list moves from quarterly to monthly when quarterly intra-EU supplies of goods exceed | EUR 50,000 | 2026 | Áfa tv. Annex 4/A point 3, https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 |
| Central bank base rate (sets late interest) | 5.50% from 26 August 2026 | 2026 | NAV notice, https://nav.gov.hu/ugyfeliranytu/jegybank |

## The taxable base

- **What is taxed.** Supplies of goods and services in Hungary, intra-EU acquisitions, imports, and services bought from abroad that are taxable in Hungary under the general business-to-business rule, where the Hungarian buyer pays the VAT (Áfa tv. 37. § (1), 140. §).
- **Base.** The consideration excluding VAT. A VAT-inclusive amount contains VAT equal to the fraction in the table (83. §).
- **Exempt without deduction.** Financial and insurance services, healthcare, education, residential letting and other public-interest and other exempt supplies (85. §-86. §). Where a business has both taxable and exempt supplies and cannot attribute input VAT directly, it apportions.
- **Domestic reverse charge (fordított adózás).** The buyer pays the VAT on construction work on real estate subject to a building permit or notification, related labour hire, scrap and waste (Annex 6), certain steel and other goods (Annexes 6/A and 6/B), real estate where the seller opted to tax, emission rights, and sales of fixed assets, or of other goods and services above HUF 100,000 at market price, by a business under liquidation or another insolvency procedure. Both parties must be VAT-registered in Hungary (142. § (1), (3)).
- **Input VAT.** Deductible on purchases used for taxable supplies with a valid invoice. Blocked in full (124. § (1)-(2)): petrol for any vehicle, passenger cars, other fuel and goods for running or maintaining them, motorcycles over 125 cm3, yachts, residential property, food, drink, hospitality (restaurants), entertainment, taxi, parking and road tolls. Partly blocked: 30% of the VAT on fixed and mobile telephone and VoIP services (124. § (3)); 50% of the VAT on running, maintaining and hiring a passenger car (124. § (4)). Exceptions, for example for taxi firms, car rental and resale, are in 125. §.
- **Cash accounting.** A business under the HUF 125 million cap may elect to pay VAT when paid by its customers. Its buyers then deduct only once they have paid (XIII/A. fejezet).
- **Rounding.** The return main sheets are in thousand forints, rounded (Art. 2. melléklet I. A) 1).

## Deadlines and filing

- **Frequency for 2026 is set by 2024 data** (Art. 2. melléklet I. B) 3.1):
  - **Monthly** if the 2024 VAT to be accounted for (output VAT less deductible input VAT), annualised, was positive and reached HUF 1 million. Also monthly: a business formed without a legal predecessor, in its registration year and the year after (3.1.13); a VAT group (3.1.9).
  - **Annual** only if the 2024 VAT to be accounted for, either sign, was below HUF 250,000, AND annualised net supplies do not exceed HUF 50 million, AND the business has no EU VAT number (3.1.3).
  - **Quarterly** in every other case (3.1.1).
  - **Mid-year switches.** A quarterly filer moves to monthly once its cumulative VAT to be accounted for since 1 January is positive and reaches HUF 1 million (3.1.5). An annual filer moves to quarterly once the cumulative difference reaches HUF 250,000, turnover exceeds HUF 50 million, or it gets an EU VAT number; and to monthly once the positive difference reaches HUF 1 million (3.1.4, 3.1.6).
- **Due dates.** Return and payment by the 20th of the month after the month or quarter. Annual filers by 25 February of the following year (Art. 2. melléklet I. B) 1.1, 2.1 and II. 2.1). A refund can be claimed from the same date.
- **Form.** Form 2665 for 2026 periods, filed through ÁNYK or by approving NAV's eÁfa draft, on the web or by machine interface (Áfa tv. 184. §; NAV booklet 14).
- **M sheets (domestic recapitulative statement).** For every received invoice on which the business deducts VAT, it reports the first eight digits of the supplier's tax number, the base, VAT, invoice number and supply date. There is no value threshold. eÁfa filers are exempt (Áfa tv. Annex 10 points 9-15).
- **Online invoice data (Online Számla).** Data on every invoice issued under the Áfa tv. goes to NAV. Software invoices are reported electronically as issued. Paper invoices within 4 days, or by the next day if the invoice VAT is HUF 500,000 or more (Annex 10 points 1-4). See [hungary-einvoice](hungary-einvoice.md).
- **EU sales list (összesítő nyilatkozat).** Form 26A60 for intra-EU supplies and acquisitions. Monthly filers submit it monthly and quarterly filers quarterly, by the 20th of the following month. A quarterly filer switches to monthly once its intra-EU supplies of goods in a quarter exceed EUR 50,000 (Áfa tv. Annex 4/A points 2-3). Approving an eÁfa draft does not replace it (NAV booklet 14).
- **Exempt businesses** file a VAT return only for the transactions on which they still owe VAT, monthly (Art. 2. melléklet I. B) 3.4).

## Penalties and interest

| Item | Rule | Source |
|---|---|---|
| Late payment interest (késedelmi pótlék) | Central bank base rate plus 5 percentage points, divided by 365, per day. At 5.50%, 10.50% a year | Art. 209. § (1); NAV base rate notice |
| Self-revision surcharge (önellenőrzési pótlék) | Base rate divided by 365, per day; 1.5 times on a second self-revision of the same return | Art. 212. § (1), (1a) |
| Tax penalty (adóbírság) on a shortfall found by NAV | 50% of the shortfall; 200% if linked to hidden income or false or destroyed records. Late interest still runs | Art. 215. § (3)-(5) |
| Penalty discount | Half the penalty is waived if the taxpayer waives appeal and pays by the due date | Art. 216. § |
| Default fine (mulasztási bírság) for late, missing or wrong returns and reports | Up to HUF 400,000 for an individual, HUF 1,000,000 for others | Art. 220. § (1) |
| Missed return or report after NAV's 15-day call | HUF 50,000 (individual) or HUF 200,000 (others), then HUF 200,000 or HUF 500,000 after a second call | Art. 221. § (2)-(3) |
| Errors in the M sheets (recapitulative statement) | Cap: number of invoices affected times the default fine maximum | Art. 229. § |

Correcting an error by self-revision before NAV finds it removes the tax penalty and default fine (Art. 214. §).

## Cross-border points

- **Services bought from EU or non-EU businesses** that are taxable in Hungary under the general rule (Áfa tv. 37. § (1)): the Hungarian business buyer self-assesses VAT at the Hungarian rate and deducts it in the same return if entitled (140. §).
- **Services sold to EU businesses** under the general rule are taxed in the customer's state. The invoice says "fordított adózás" and the service goes on the EU sales list.
- **Intra-EU supplies of goods** to a VAT-registered buyer are exempt with deduction. Intra-EU acquisitions are self-assessed by the buyer.
- **Sales to EU consumers.** Distance sales of goods and telecom, broadcasting and electronic services stay taxed in Hungary up to EUR 10,000 a year EU-wide. Above it, the customer's state's VAT applies, usually through the one-stop shop (Áfa tv. 49/A. §).
- **Foreign businesses** making taxable supplies in Hungary on which the buyer does not self-assess must register with NAV. The subjective exemption is open only to Hungarian-established businesses and to EU businesses using the EU small-business scheme (187. §, 195/G. §).
- **Exports** of goods outside the EU are exempt with the right to deduct.

## Worked examples

**Example 1: quarterly Kft, Q3 2026.** A Budapest Kft files quarterly. In July to September 2026 it sells HUF 12,000,000 net of services at 27%. It buys HUF 4,000,000 net of 27% goods and services, a HUF 200,000 net mobile phone contract, and a HUF 100,000 net client dinner. Output VAT is 12,000,000 × 27% = 3,240,000. Input VAT on the goods and services is 4,000,000 × 27% = 1,080,000. The phone contract carries 54,000 VAT, of which 30% is blocked, so 37,800 is deductible. The dinner's VAT is blocked in full. VAT payable is 3,240,000 − 1,080,000 − 37,800 = 2,122,200, shown on form 2665 as 2,122 thousand forints. Return and payment are due on 20 October 2026.

```oa-check
name: Quarterly Kft, Q3 2026, 27% sales with telephone and hospitality input VAT limits
inputs:
  sales_net: 12000000
  purchases_net: 4000000
  phone_net: 200000
  dinner_net: 100000
steps:
  - output_vat: sales_net * 0.27
  - input_vat_purchases: purchases_net * 0.27
  - phone_vat: phone_net * 0.27
  - phone_deductible: phone_vat * (1 - 0.30)
  - dinner_deductible: dinner_net * 0.27 * 0
  - payable: output_vat - input_vat_purchases - phone_deductible - dinner_deductible
  - return_thousands: round(payable / 1000)
expected:
  output_vat: 3240000
  input_vat_purchases: 1080000
  phone_deductible: 37800
  payable: 2122200
  return_thousands: 2122
```

**Example 2: a sole trader crosses the HUF 20 million exemption limit.** A sole trader chose the subjective exemption for 2026. By mid-November 2026 its supplies total HUF 19,200,000. It then invoices HUF 1,500,000, at a price agreed with the customer as final, so VAT is inside it. That supply takes the year's total to HUF 20,700,000, HUF 700,000 over the limit. The exemption ends, and the crossing supply is already taxable in full, not only the excess (Áfa tv. 191. § (2)). The VAT inside the agreed price is 1,500,000 × 21.26% = 318,900. In December it sells HUF 800,000 net, now charging 27%: 216,000. VAT due for 2026 is 534,900. It notifies NAV of the change. Under 191. § (3) it would be barred from the exemption until the end of 2028, but 378. § (2) lifts the bar for 2027: its 2026 supplies are under HUF 22 million, so if its expected 2027 supplies also stay within HUF 22 million it may choose the exemption again for 2027.

```oa-check
name: Sole trader crossing the 2026 subjective exemption limit
inputs:
  sales_before: 19200000
  crossing_sale_gross: 1500000
  limit: 20000000
  december_net: 800000
steps:
  - excess_over_limit: sales_before + crossing_sale_gross - limit
  - vat_in_crossing_sale: crossing_sale_gross * 0.2126
  - vat_december: december_net * 0.27
  - vat_due: vat_in_crossing_sale + vat_december
expected:
  excess_over_limit: 700000
  vat_in_crossing_sale: 318900
  vat_december: 216000
  vat_due: 534900
```

## Ask the client first

- What were your total supplies in 2025, and what do you expect in 2026? (Decides whether the HUF 20 million exemption is available and whether it has been lost.)
- What did your 2024 returns show, when did you register, did you take over a predecessor, and do you hold an EU VAT number? (Decides monthly, quarterly or annual filing.)
- Do you file through eÁfa or on form 2665 through ÁNYK? (Decides whether you fill the M sheets.)
- Do you make exempt supplies, such as financial services, insurance or residential letting? (Decides apportionment.)
- Do you buy or run passenger cars, phones, restaurant or entertainment services? (Decides blocked input VAT.)
- Do you buy from or sell to businesses or consumers abroad, and have you chosen cash accounting? (Decides reverse charge, the EU sales list, the one-stop shop and the timing of deduction.)

## Sources

| Source | URL | Read on |
|---|---|---|
| Áfa tv., Act CXXVII of 2007 on VAT (consolidated, state of 15 September 2026, with annexes) | https://njt.jog.gov.hu/jogszabaly/2007-127-00-00 | 2026-10-23 |
| Art., Act CL of 2017 on the rules of taxation (2. melléklet, 64. §, 209.-229. §) | https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 | 2026-10-23 |
| Act XL of 2026 (0% rate for prescription-only medicines from 1 September 2026) | https://njt.jog.gov.hu/jogszabaly/2026-40-00-00 | 2026-10-23 |
| NAV, notice on the higher subjective exemption limit (11 December 2025) | https://nav.gov.hu/ado/afa/Emelkedik_az_alanyi_adomentesseg_ertekhatara | 2026-10-23 |
| NAV, information booklet 14 (VAT for new taxpayers, 2026) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/14.-Hasznos-tudnivalok-kezdo-afaalanyoknak-2025.-02.-03 | 2026-10-23 |
| NAV, information booklet 24 (filing and payment, 2026) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/24.-Bevallasi-adofizetesi-informaciok-2026.01.26 | 2026-10-23 |
| NAV, form 2665 completion guide | https://nav.gov.hu/pfile/file?path=%2Fnyomtatvanyok%2Fletoltesek%2Fnyomtatvanykitolto_programok%2Fnyomtatvanykitolto_programok_nav%2F2665%2F2665-kitoltesi-utmutato | 2026-10-23 |
| NAV, central bank base rate notice (5.50% from 26 August 2026) | https://nav.gov.hu/ugyfeliranytu/jegybank | 2026-10-23 |

Not yet confirmed: the HUF 24,000,000 exemption limit for 2028 is in NAV's notice but not in the consolidated Áfa tv. text read today; the specific fine for missing or late online invoice data was not located in the Art. today, so only the general default fine (Art. 220. §) is given; the full Annex 3 list of 5% items is summarised, not reproduced.

> Contributed by Ryan Duguid.

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
