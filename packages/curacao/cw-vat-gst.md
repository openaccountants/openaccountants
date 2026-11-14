---
name: cw-vat-gst
description: "Curacao turnover tax (omzetbelasting, OB) for tax year 2026. OB is a cumulative turnover tax, not a creditable VAT. Covers who is an entrepreneur, the 6% general rate, 7% on insurance and short-stay lodging, the 9% list of goods and services, 0% long-term residential letting, the exemptions, the small-business scheme (RKO) up to NAf 30,000, the 2025 annual, quarterly and monthly filing bands, the 15th-of-the-month deadline and the 2026 due dates, the 50% import deduction, refunds, CRIB registration and the default penalties. Trigger phrases include Curacao VAT, Curacao sales tax, omzetbelasting Curacao, OB 6%, RKO Curacao, aangifte omzetbelasting."
version: "1.0"
jurisdiction: CW
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: vat-gst
type: situation-rules
---

# Curacao turnover tax (omzetbelasting, OB) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar year 2026. Authority: Belastingdienst Curacao (belastingdienst.cw). Amounts are Curacao guilders (ANG or NAf on older pages, XCG or Cg on newer ones).

## Who this applies to

- **OB is cumulative, not a VAT.** Each time a product is sold or a service is supplied, OB is charged and paid; there is no general credit for OB on purchases ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)). The only relief against cumulation is the import deduction below.
- **The entrepreneur pays.** OB is an indirect tax collected from the entrepreneur, who charges it to the customer (same page).
- **Who is an entrepreneur:** anyone who independently carries on a business or profession, profit or loss. This includes sole traders, partnerships (maatschap, V.O.F., C.V.), B.V.s, N.V.s, foundations, SPFs and associations. Nationality does not matter: a foreign entrepreneur supplying services in Curacao is an entrepreneur and owes Curacao OB. A one-off sale of your car is not a business; selling several cars soon is (same page).
- **Out of scope:** import duties and excises, profit tax (`cw-corporate-income-tax`), wage tax (`cw-payroll-social`).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| General rate | 6% | All taxable supplies not listed below | 2026 | [Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/) |
| Insurance | 7% | Insurance other than the exempt life, health and reinsurance | 2026 | same |
| Short-stay lodging | 7% | Hotel, guesthouse, apartment or home let to people staying at most 90 days | 2026 | same |
| Medium-term letting and business property | 6% | Lodging for more than 90 days but under 1 year; shops, offices, warehouses, factories | 2026 | same |
| Long-term residential letting | 0% | Property fitted, meant and used for permanent living, let for at least 1 year, any tenant nationality | 2026 | same |
| High rate | 9% | Listed goods and services, see "The base" | 2026 | same |
| Small-business scheme (RKO) | prior-year turnover of NAf 30,000 or less, excluding OB | Sole trader only, living or established in Curacao, on written request | 2026 | same |
| Annual filer band | taxable annual turnover under Cg 30,000 | Classification used from January 2025 | 2026 | [Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf) |
| Quarterly filer band | Cg 30,000 to Cg 75,000 | Classification used from January 2025 | 2026 | same |
| Monthly filer band | above Cg 75,000 | Classification used from January 2025 | 2026 | same |
| Import deduction (aftrekrecht) | 50% | Imported trading goods only, by decision of the Inspector | 2026 | [Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/) |
| Late payment, first default | 5% of the additional assessment, min NAf 50, max NAf 2,500 | Defaults counted over the previous 9 periods | 2026 | same |
| Second default | 10%, min NAf 100, max NAf 5,000 | same | 2026 | same |
| Third or later default | 15%, min NAf 150, max NAf 10,000 | same | 2026 | same |
| Systematic late or missing returns | up to NAf 2,500 | | 2026 | same |
| Too little declared | 15%, min NAf 25, max NAf 10,000 | | 2026 | same |

## The base

1. **Base:** the compensation (vergoeding), the total amount charged for the goods or service. If you charge too much by mistake, OB is due on the higher amount ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)).
2. **9% goods:** motor vehicles (except those for public or private passenger transport by road, and recognisable police, fire and ambulance vehicles); yachts and other pleasure and sports boats; food prepared and fit for immediate use; soft drinks except fruit drinks; alcoholic drinks; tobacco; digital carriers with films, games and similar; mobile phones and other communication devices; weapons and ammunition; fireworks; Christmas trees (same page).
3. **9% services:** renting motor vehicles, yachts, pleasure boats, aircraft and spacecraft; outings where such vehicles are essential; diving; admission to cinemas, fairs and exhibitions, erotic shows and permanent recreation facilities; renting films and games; food and drinks served for consumption on the premises by hotels, cafes, restaurants and similar; lotteries, scratch cards, number games and bingo (same page).
4. **Exempt supplies** still go on the return, with their amount. The list includes (same page): utility water, electricity, gas, steam and compressed air, and bottled water; bread, eggs, rice, potatoes, grain, flour, baby food and fresh fruit and vegetables (not tinned or frozen, which are 6%); long-term residential letting; public road transport and school buses; medical services by hospitals, laboratories, doctors, dentists, nurses, midwives, physiotherapists, chiropractors, speech therapists, dietitians, psychologists and podiatrists; medical aids; prescription medicines; care in institutions; non-profit social, cultural, charitable, sports and religious bodies (no serious distortion of competition); life, health and reinsurance and insurance intermediaries; non-commercial education, and congresses at least 90% attended by non-residents; concession postal items; international air and sea transport and fuel and services for such ships and aircraft; services in sea and airport areas for goods entering and leaving; goods exported to customers not living or established in Curacao; fuel to utilities for power; supplies to oil refineries for their operation; aid projects paid by the Netherlands, Aruba, Sint Maarten or international organisations; consuls under reciprocity; supplies under the US forward operating location agreement; currency, banknote and securities dealings; casino games; real estate subject to transfer tax; services by lawyers, tax advisers, asset managers, trust offices, accountants, banks and notaries to holders of a foreign exchange exemption; LNG transshipment; the foreign activities of a Curacao investment company; locally produced goods supplied to an entrepreneur as trading goods (if the supplier processed or assembled them); designated goods exempt from import duty on import; and goods not yet in free circulation.
5. **RKO:** a qualifying sole trader still charges OB to customers but does not pay it to the Belastingdienst; an annual return with total turnover is still filed. Apply in writing through the contact form, not in person (same page). The 2026 handbook says the form is under documents on the website ([Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf)).
6. **Import deduction:** on request and after a decision by the Inspector, an entrepreneur may deduct 50% for imported trading goods from the OB due in the period. Only for trading goods, only if returns are up to date, and the decision may set conditions ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)).
7. **Refunds** (teruggaaf) by written request when OB was paid wrongly, the customer did not pay in full, a price reduction followed, or goods were taken back and the OB repaid. You may not set off the difference on your own return. A refund is paid only if you have no arrears on any assessment (same page).

## Deadlines and filing

- **Register:** apply for a CRIB number through the contact form or info.belastingdienst@gobiernu.cw with: for an N.V., B.V., foundation or association, the notarial deed, the Chamber of Commerce extract, the director's details and a valid ID; for a sole trader, the extract and ID; for a V.O.F. or maatschap, the extract, the partners' agreement and ID. With staff, add the headcount, first start date and gross payroll ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)).
- **File online** through the portal (user account needed; "Mijn aangifte"); pay by bank, never cash. File a nil return for a period with no turnover or only exempt supplies. A revised return goes through the portal, except a correction that lowers the OB: send the correct return through the contact form (same page).
- **Due date:** return and payment within 15 days after the period, so by the 15th. If the 15th is a holiday, weekend or other day off, the next working day (same page).
- **Frequency:** monthly by default; annual on request for RKO holders, dormant entrepreneurs and those with more than 90% exempt supplies (same page). From January 2025 the Belastingdienst classifies filers by taxable annual turnover: under Cg 30,000 annual, Cg 30,000 to 75,000 quarterly, above Cg 75,000 monthly ([Tax Office Curacao handbook 2026](https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf)).
- **2026 dates** ([Inleverdata 2026](https://belastingdienst.cw/wp-content/uploads/2026/02/Inleverdata-aangiften-2026_huisstijl_ME-LB-OB.docx-2.pdf)): monthly January 2026 by 17 February; February by 16 March; March by 15 April; April by 15 May; May by 15 June; June by 15 July; July by 17 August; August by 15 September; September by 15 October; October by 16 November; November by 15 December; December by 15 January 2027. Quarterly: Q1 by 15 April 2026, Q2 by 15 July, Q3 by 15 October, Q4 by 15 January 2027. Annual 2026 by 15 January 2027.

## Penalties and interest

Penalties are in the rates table. The Inspector counts the defaults in the previous 9 periods, and filing defaults and payment defaults are counted together ([Inleverdata 2026](https://belastingdienst.cw/wp-content/uploads/2026/02/Inleverdata-aangiften-2026_huisstijl_ME-LB-OB.docx-2.pdf)). Interest is not on the pages read.

## Cross-border points

- A foreign entrepreneur supplying services in Curacao owes Curacao OB ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)).
- Exports of goods to customers not living or established in Curacao are exempt; international air and sea transport is exempt (same page).
- How OB applies to digital services supplied from abroad to Curacao customers (a reverse charge was claimed in the old file, citing a blog) is not confirmed.

## Two worked examples that recompute

**Case 1: a bakery-cafe's monthly return.** In March 2026 it sells bread for 20,000 (exempt), cakes to take away for 30,000 (6%) and coffee and sandwiches eaten in the cafe for 15,000 (9%). OB due: 6% of 30,000 = 1,800 plus 9% of 15,000 = 1,350, total 3,150. The 20,000 exempt goes on the return too. Its turnover is above Cg 75,000 a year, so it files monthly; the March return and payment are due by 15 April 2026.

```oa-check
name: Curacao OB monthly return, mixed rates
inputs:
  exempt_sales: 20000
  general_sales: 30000
  high_sales: 15000
  general_rate: 0.06
  high_rate: 0.09
steps:
  - ob_general: general_sales * general_rate
  - ob_high: high_sales * high_rate
  - ob_due: ob_general + ob_high
  - total_turnover_reported: exempt_sales + general_sales + high_sales
expected:
  ob_general: 1800.00
  ob_high: 1350.00
  ob_due: 3150.00
  total_turnover_reported: 65000.00
```

**Case 2: decision, apply for the RKO or not.** A sole trader had 2025 turnover of 28,000 excluding OB and expects the same in 2026, all at 6%. Without the RKO she pays 6% of 28,000 = 1,680 to the Belastingdienst. With the RKO she still charges the 1,680 but keeps it, and files one annual return by 15 January 2027. She qualifies because 28,000 is not more than NAf 30,000 (headroom 2,000). A B.V. with the same turnover would not qualify: the RKO is for sole traders only.

```oa-check
name: RKO for a sole trader under NAf 30000
inputs:
  prior_turnover: 28000
  rko_limit: 30000
  rate: 0.06
steps:
  - ob_charged: prior_turnover * rate
  - headroom: rko_limit - prior_turnover
  - ob_paid_without_rko: ob_charged
  - ob_paid_with_rko: 0
  - kept_with_rko: ob_paid_without_rko - ob_paid_with_rko
expected:
  ob_charged: 1680.00
  headroom: 2000.00
  kept_with_rko: 1680.00
```

## Ask the client first

1. Legal form (only a sole trader can use the RKO), CRIB number and portal access.
2. Turnover excluding OB in 2025 and expected in 2026 (filing band and RKO).
3. What is sold: any 9% goods or services, insurance, lodging (length of stay), exempt items, exports?
4. Are trading goods imported, and is there an import deduction decision?
5. Any late or missing returns or payments in the last 9 periods?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Office Curacao, Omzetbelasting (theme page): read for the entrepreneur test, base, all rates, the 9% list, exemptions, RKO, import deduction, refunds, filing, due dates, CRIB documents and penalties | https://belastingdienst.cw/ondernemer/themas/omzetbelasting/ | 2026-11-14 |
| Tax Office Curacao, Inleverdata aangiften 2026: read for the 2026 monthly, quarterly and annual due dates and how defaults are counted | https://belastingdienst.cw/wp-content/uploads/2026/02/Inleverdata-aangiften-2026_huisstijl_ME-LB-OB.docx-2.pdf | 2026-11-14 |
| Tax Office Curacao handbook "De basis van succesvol ondernemen" (2026): read for the January 2025 filing bands (Cg 30,000 and Cg 75,000), the rates list and the RKO form | https://belastingdienst.cw/wp-content/uploads/2026/08/FIN_Succesvol_Ondernemen_versie2-1.pdf | 2026-11-14 |
| Tax Office Curacao, Overzicht tarieven OB versie 1.1 (May 2013): read for the detailed exempt food items (bread, eggs, rice, grain, flour, baby food, fruit and vegetables) | https://belastingdienst.cw/wp-content/uploads/2023/02/20130506_Overzicht_tarieven_OB__versie1.1_.pdf | 2026-11-14 |

Not yet confirmed: OB on digital or other services supplied from abroad by a non-established supplier, and any reverse charge; whether the 50% import deduction is 50% of the OB paid on import or of another amount (the page wording is short); interest on late OB; the text of the Landsverordening omzetbelasting 1999 itself (not opened).
