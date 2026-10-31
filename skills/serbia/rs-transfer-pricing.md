---
name: rs-transfer-pricing
description: "Serbian transfer pricing (transferne cene) for tax year 2026 under the Zakon o porezu na dobit pravnih lica (ZPDPL), Articles 59 to 61v, 10a and 112a, and the Ministry of Finance Rulebook on transfer pricing (Sl. glasnik 61/13 to 95/21). Covers who is a related party (25% capital or votes, family links, any company from a preferential tax jurisdiction); the arm's length principle and the six methods; the interquartile range and adjustment to the midpoint; full and short-form documentation filed with the tax balance, and the RSD 8,000,000 short-form test; the 2026 arm's length interest rate rulebook for related-party loans (Sl. glasnik 36/2026); country-by-country reporting; adjustments, the five-year limitation period and penalties. Trigger on: Serbia transfer pricing, transferne cene, povezana lica, ван дохвата руке, Serbian TP documentation, arm's length interest Serbia. Out of scope: the full tax balance, thin capitalisation detail and withholding (rs-corporate-tax), VAT (serbia-vat)."
version: 0.1
jurisdiction: RS
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Serbia: transfer pricing (transferne cene), tax year 2026

Source-cited draft: not reviewed by an accountant, not for filing.

The rules sit in the corporate income tax law, the Zakon o porezu na dobit pravnih lica (ZPDPL), Articles 59 to 61v, with Article 10a (depreciation base) and Article 112a (missing documentation). The Minister of Finance's Rulebook on transfer prices and arm's length methods (Pravilnik o transfernim cenama i metodama koje se po principu "van dohvata ruke" primenjuju kod utvrđivanja cene transakcija među povezanim licima, Sl. glasnik RS 61/13, 8/14, 94/19 and 95/21) sets the documentation content and how each method is applied. Article numbers below refer to the Ministry of Finance consolidated text.

Law 80/2026 (in force 8 September 2026) does not change Articles 59 to 61v. It deletes the Article 62 thin capitalisation rule and adds an EBITDA interest limit (Article 62a), but those changes apply only from EU accession, so for 2026 thin capitalisation still applies. See [rs-corporate-tax](rs-corporate-tax.md) for the amendment's dates, the tax balance, thin capitalisation and withholding tax. This skill does not repeat them.

## Who this applies to

- **Every corporate income taxpayer with related-party transactions.** A transfer price is the price in a transaction in assets, or the creation of obligations, between related parties (Article 59(1)). The law draws no line between domestic and cross-border transactions, so a Serbian company dealing with another Serbian group company is in scope too.
- **Permanent establishments.** The same rules apply to dealings between a Serbian permanent establishment and its non-resident head office (Article 60(13)).
- **Who is related (Article 59).**
  - A person who directly or indirectly holds at least 25% of the shares or interests is treated as able to control the taxpayer.
  - A person who directly or indirectly holds at least 25% of the votes in the management bodies has significant influence.
  - Two companies are related when the same persons take part in their management, control or capital at those levels.
  - The family of a person who is related under the 25% tests is related too: spouse or partner, descendants, adopted children and their descendants, parents, adoptive parents, siblings and their descendants, grandparents and their descendants, and the spouse's or partner's siblings and parents (Article 59(6)).
  - Any non-resident legal entity from a jurisdiction with a preferential tax system is a related party, whatever the ownership (Article 59(7)). The list of those jurisdictions is a Minister of Finance rulebook (see rs-corporate-tax).
- **Not related.** The Republic, an autonomous province and a local government unit are not treated as legal entities for Articles 59 to 61a (Article 61b).
- **Sale of capital assets.** A company that sells a capital asset covered by Article 27 (capital gains) to a related party does not have to price it at arm's length or document it (Article 60(6)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Related party: capital or vote holding | at least 25%, direct or indirect | 2026 | https://www.mfin.gov.rs/upload/media/vlmAb4_675ab2034cea0.docx (ZPDPL Art. 59) |
| Short-form report allowed (except loans) | one-off transaction, or total with one related party in the year, not above the VAT registration turnover | 2026 | https://www.mfin.gov.rs/upload/media/vlmAb4_675ab2034cea0.docx (ZPDPL Art. 60(4)); https://www.purs.gov.rs/upload/media/2025/2/4/373665/Pravilnikotransfernimcenama.docx (Rulebook Art. 2(3)) |
| VAT registration turnover used for that test | RSD 8,000,000 in the previous 12 months | 2026 | https://www.purs.gov.rs/sr/pravna-lica/pdv/zakon/202/zakon-o-porezu-na-dodatu-vrednost.html (VAT Law Art. 38(1)) |
| Left out of the short-form test value | interest on loans, advances given or received, VAT | 2026 | ZPDPL Art. 60(5) |
| Arm's length range (TNMM) | interquartile range, first to third quartile; weighted average of 3 to 5 years of comparables | 2026 | Rulebook Art. 26(1), (3) and (4) |
| Price outside the range | adjusted to the midpoint of the range | 2026 | ZPDPL Art. 60(10); Rulebook Art. 31(6) |
| Activity analysis can be skipped | activity is not the main one and earns under 10% of total income | 2026 | Rulebook Art. 4(2) |
| Fixed asset bought from a related party | depreciation base is the lower of transfer price and arm's length price; 20% of the difference goes into the adjustment in the year and the next four years | 2026 | ZPDPL Art. 10a; Rulebook Art. 31(3) |
| Arm's length interest, other companies: RSD short-term | 7.13% | 2026 | https://www.mfin.gov.rs/upload/media/aatf8h_69f0810128819.docx (Rulebook Sl. glasnik 36/2026, Art. 2) |
| Arm's length interest, other companies: RSD long-term | 7.21% | 2026 | same |
| Arm's length interest, other companies: EUR or EUR-indexed, short-term | 4.75% | 2026 | same |
| Arm's length interest, other companies: EUR or EUR-indexed, long-term | 5.42% | 2026 | same |
| Arm's length interest, other companies: CHF or CHF-indexed, long-term | 7.10% | 2026 | same |
| Arm's length interest, other companies: USD or USD-indexed, long-term | 4.43% | 2026 | same |
| Arm's length interest, banks and financial leasing: RSD short-term / RSD long-term | 4.40% / 0.33% | 2026 | same |
| Arm's length interest, banks and financial leasing: EUR / USD / CHF / SEK / GBP / RUB (and dinar loans indexed to them) | 4.87% / 4.98% / 3.05% / 4.12% / 1.50% / 10.73% | 2026 | same |
| Country-by-country report | Serbian ultimate parent of a group with consolidated revenue of at least EUR 750 million in the prior period | 2026 | ZPDPL Art. 61v |
| Thin capitalisation (interacts with related-party loans) | interest on related-party debt deductible up to 4 × equity (10 × for banks and leasing) | 2026 | ZPDPL Art. 62; see rs-corporate-tax |
| Corporate income tax rate on an adjustment | 15% | 2026 | ZPDPL Art. 39; see rs-corporate-tax |

The 2026 interest rulebook was signed on 23 April 2026 and applies to loans and credits between related parties "for 2026" (Art. 1). It lists no short-term USD rate for other companies. The rates apply to loans as well as credits (Art. 2(2)).

## The taxable base

**The principle.** The taxpayer shows its related-party transactions separately in the tax balance (Article 60(1)). It shows interest on deposits, loans and credits separately too, up to the level allowed by Article 62 (Article 60(2)). With the tax balance it files documentation that sets each transaction's transfer price against the price on a market for the same or similar transactions between unrelated parties (Article 60(3)).

**Methods (Article 61).**

1. Comparable uncontrolled price method.
2. Cost plus method.
3. Resale price method.
4. Transactional net margin method (TNMM).
5. Profit split method.
6. Any other method, but only if the first five cannot be used or the other method fits the case better.

The taxpayer uses the method that best fits the facts, and may combine methods (Article 61(2)). The method is chosen per type of transaction (Rulebook Article 11). The Rulebook prefers internal comparables over external ones (Articles 18 and 24) and Serbian data first. Foreign comparables are used only when Serbian data cannot be found (Article 6). For TNMM the Rulebook lists four ratios: operating profit to sales (buying from related parties to resell), operating profit to operating costs (services and manufacturing), operating profit to operating assets, and the Berry ratio (Article 27). Transactions may be grouped (aggregated) or split when that suits the case (Article 60(7)).

**The adjustment (Article 60(8) to (10); Rulebook Article 31).** For each related party:

- Income: add the amount by which arm's length income exceeds income at the transfer price.
- Expense: add the amount by which the expense at the transfer price exceeds the arm's length expense.
- If a range was set and the transfer price is inside it, no adjustment. If it is outside, the arm's length price is the midpoint of the range.
- The adjustments for one related party are added up. A negative difference with the same related party can reduce that total, but not below zero (Article 60(11); Rulebook Article 31(5) and (7)). One party's negatives cannot offset another party's positives.
- The final adjustments for all related parties go into the tax base (Rulebook Article 31(9)).

**No downward adjustment on your own.** The taxpayer can reduce its tax base for related-party transactions only under a double tax treaty (Article 60(12)). So a corresponding adjustment comes through the treaty's mutual agreement article, not through the tax balance.

**Related-party loans (Article 61(3) to (6)).** The interest rulebook gives rates treated as arm's length. Instead, the taxpayer may price loans under the general method rules. If it chooses that, it must apply the general rules to all its related-party loans and credits, and the Tax Administration is then not bound by the rulebook rates either. Default interest between related parties is never deductible (Article 7a, item 7).

**Fixed assets from a related party (Article 10a).** The depreciation base is the lower of the transfer price and the arm's length price. The Rulebook spreads the difference: 20% of it goes into the adjustment in the year of purchase and in each of the next four years (Article 31(3)).

**What the full report contains (Rulebook Articles 2 to 8).**

1. Group analysis: the group's business, structure, policy changes, the taxpayer's history and figures, the related parties it deals with, and whether it belongs to a group that files a country-by-country report and who the ultimate parent is.
2. Activity analysis: market conditions, competitors, price drivers, risks. Skip it for an activity that is not the main one and earns under 10% of income.
3. Functional analysis: each transaction type, contracts, functions, risks and assets.
4. Choice of method, with the reasons.
5. Conclusion: whether prices are at arm's length, and the adjustment for each related party.
6. Annexes: the data and comparables used.

**The short-form report (Article 60(4); Rulebook Article 2(3) and (4)).** It is allowed for transactions other than loans and credits where either the transaction is one-off in the year and not above RSD 8,000,000, or the total with that one related party in the year is not above RSD 8,000,000. Interest, advances and VAT are left out of the value (Article 60(5)). The short form lists each transaction's description, value and related party. It does not have to show an arm's length price.

## Deadlines and filing

- **Documentation.** Filed with the tax balance (Article 60(3)). The return and tax balance are due within 180 days after the end of the tax period (Article 63). For a calendar year 2026 that is 29 June 2027. Filing and the PDP return are covered in rs-corporate-tax.
- **Extra documents on request.** The Tax Administration may ask for more documentation if what was filed is not enough. It must allow a reasonable time. If the documentation gives no adequate basis, the tax authority may prepare or complete the analysis itself (Rulebook Article 9).
- **Country-by-country report.** A resident ultimate parent files the annual report on controlled transactions of the international group within 12 months of the end of the financial year (Article 61v(6)). For a calendar 2026 year that is 31 December 2027. It uses Form CbC, on paper (Rulebook Article 33). A Serbian subsidiary of a foreign group does not file a CbC report under the law; it states in its own report who the ultimate parent is and where it is resident (Rulebook Article 3, item 6).
- **Advance pricing agreements.** Neither the ZPDPL nor the Tax Procedure Law (ZPPPA) consolidated texts read for this skill contain an advance pricing agreement procedure. Treaty mutual agreement procedures remain.
- **Limitation period.** The Tax Administration's right to assess tax expires five years after 1 January of the year following the year in which the tax should have been assessed (ZPPPA Article 114). So a 2026 tax balance, assessed in 2027, stays open until the end of 2032.

## Penalties and interest

- **Missing or incomplete documentation (ZPDPL Article 112a).** The tax authority first issues a warning and orders the taxpayer to file or complete the documentation within a period of 30 to 90 days from delivery of the warning.
- **Documentation not filed with the return (ZPPPA Article 178a).** A legal entity is fined RSD 100,000 to 2,000,000. If it files the documents after the deadline, the fine is RSD 100,000. The responsible person is fined RSD 10,000 to 100,000 (RSD 10,000 for late filing).
- **Documents not produced on request in an audit (ZPPPA Article 179(1), item 10).** RSD 100,000 to 2,000,000 for the company, RSD 10,000 to 100,000 for the responsible person.
- **Tax understated because of a transfer pricing adjustment (ZPPPA Article 178).** 30% to 40% of the tax difference, at least RSD 200,000. If the difference is up to 5% of the correct tax, the fine is RSD 100,000 (RSD 10,000 for the responsible person). Otherwise the responsible person is fined RSD 10,000 to 100,000. No fine may exceed the maximum set by the law on misdemeanours (Article 178(6)).
- **Late-payment interest (ZPPPA Article 75).** The National Bank of Serbia reference rate plus 10 percentage points, simple interest, from the day after the original due date. The current rate is in rs-corporate-tax.

## Cross-border points

- **Preferential tax jurisdictions.** Any company from a listed jurisdiction is a related party by law (Article 59(7)). Royalties, interest, rent and services paid to it also bear 25% withholding (see rs-corporate-tax).
- **Treaties.** The only way to reduce the Serbian base for a related-party transaction is a treaty provision (Article 60(12)), in practice the associated enterprises and mutual agreement articles of the treaty with the other state.
- **Permanent establishments.** Dealings between a Serbian PE and its foreign head office are priced at arm's length and documented in the same way (Article 60(13)).
- **Group revenue in euro.** The EUR 750 million CbC test is converted at the National Bank of Serbia middle rate on the day the consolidated statements are adopted (Article 61v(2)).
- **After EU accession.** Law 80/2026 adds CFC, exit tax, hybrid mismatch rules and an EBITDA interest cap, all from EU accession only. None applies in 2026.

## Worked examples

### Example 1: distributor priced with TNMM, outside the range

Novi Sad Distribucija d.o.o. buys all its goods from its German parent and sells them to unrelated Serbian retailers. In 2026 its sales are RSD 500,000,000 and its operating profit is RSD 5,000,000, an operating margin of 1%. The company tests the purchases with TNMM using operating profit to sales (Rulebook Article 27, item 1). Its benchmark of comparable independent distributors gives an interquartile range of 2.4% to 4.0%, median 3.2%. In this example the median and the arithmetic middle of the range are both 3.2%.

The 1% margin is below the range, so the arm's length result is the midpoint, 3.2% (Article 60(10)). Arm's length operating profit is 3.2% of RSD 500,000,000, which is RSD 16,000,000. The purchases from the parent were overpriced by RSD 11,000,000 (Article 60(8), item 2). That amount goes into the 2026 tax base. At 15% the extra tax is RSD 1,650,000. The company cannot reduce its base for any other year or party to offset this.

```oa-check
name: Example 1, TNMM distributor outside the interquartile range (2026)
inputs:
  sales: 500000000
  operating_profit: 5000000
  q1_pct: 2.4
  median_pct: 3.2
  q3_pct: 4.0
steps:
  - margin_pct: operating_profit / sales * 100
  - arm_length_profit: sales * median_pct / 100
  - adjustment: max(arm_length_profit - operating_profit, 0)
  - extra_tax: adjustment * 0.15
expected:
  margin_pct: 1.00
  arm_length_profit: 16000000
  adjustment: 11000000
  extra_tax: 1650000
```

### Example 2: related-party RSD loan above the 2026 rulebook rate, drawn part-year

Šumadija Gradnja d.o.o. borrows RSD 100,000,000 from its Cypriot parent on a five-year loan at 10% a year. The loan is drawn on 1 April 2026, so it runs 275 days in 2026. The company uses the rulebook rates (it has not elected the general method under Article 61(4)). The 2026 rate for a long-term RSD loan to a company that is not a bank or leasing company is 7.21%.

Thin capitalisation is not a problem here. Equity under the Article 62 definition is RSD 30,000,000, so the limit is RSD 120,000,000 of related-party debt, above the RSD 100,000,000 borrowed. Interest charged in 2026 is RSD 7,534,246.58 (100,000,000 × 10% × 275 / 365). Arm's length interest is RSD 5,432,191.78 (at 7.21%). The excess expense of RSD 2,102,054.79 goes into the tax base (Article 60(8), item 2), and the extra tax at 15% is RSD 315,308.22. Withholding on the interest paid to Cyprus (20%, or 25% if the payee is from a jurisdiction on the preferential tax list) and any treaty rate are a separate question covered in rs-corporate-tax.

```oa-check
name: Example 2, RSD long-term related-party loan at 10% against the 7.21% rulebook rate, 275 days
inputs:
  principal: 100000000
  rate_charged: 10
  rulebook_rate: 7.21
  days: 275
  equity: 30000000
steps:
  - thin_cap_limit: equity * 4
  - interest_charged: principal * rate_charged / 100 * days / 365
  - interest_arm_length: principal * rulebook_rate / 100 * days / 365
  - adjustment: interest_charged - interest_arm_length
  - extra_tax: adjustment * 0.15
expected:
  thin_cap_limit: 120000000
  interest_charged: 7534246.58
  interest_arm_length: 5432191.78
  adjustment: 2102054.79
  extra_tax: 315308.22
```

## Ask the client first

1. Who owns at least 25% of the company's capital or votes, and which other companies do those owners hold at that level? Any family links? Any counterparty in a jurisdiction on the preferential tax list?
2. List each related party and the 2026 value of transactions with it, split into goods, services, royalties, loans and advances. This decides full report or short form for each party.
3. For related-party loans: currency, term (short or long), rate, drawdown dates, and the company's equity under Article 62. Has the company ever elected the general method instead of the rulebook rates?
4. Did the company buy fixed assets from a related party in 2026 or in the past four years?
5. Does the group have consolidated revenue of at least EUR 750 million, and is the Serbian company the ultimate parent?
6. Is there a benchmark study from the group (a master file or a foreign local file) that can be reused, and does it use Serbian comparables?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ministry of Finance: ZPDPL consolidated text with amendments up to 94/2024 (the text that applies to 2026), Arts. 7a, 10a, 59 to 62, 63, 112a | https://www.mfin.gov.rs/upload/media/vlmAb4_675ab2034cea0.docx | 2026-10-23 |
| Ministry of Finance: ZPDPL consolidated text with amendments up to 80/2026 (Arts. 59 to 61v unchanged; Art. 62 deleted from EU accession) | https://www.mfin.gov.rs/propisi/zakon-o-porezu-na-dobit-pravnih-lica ; https://www.mfin.gov.rs//upload/media/SByOge_6aa127acd2250.docx | 2026-10-23 |
| Tax Administration: Rulebook on transfer prices and arm's length methods (Sl. glasnik 61/13, 8/14, 94/19, 95/21), page and .docx | https://www.purs.gov.rs/sr/pravna-lica/porez-na-dobit/podzakonska-akta-pdp/7721/pravilnik-o-transfernim-cenama-i-metodama-koje-se-po-principu-van-dohvata-ruke-primenjuju-kod-utvrdjivanja-cene-transakcija-medju-povezanim-licima-.html ; https://www.purs.gov.rs/upload/media/2025/2/4/373665/Pravilnikotransfernimcenama.docx | 2026-10-23 |
| Ministry of Finance: Rulebook on arm's length interest rates for 2026 (Sl. glasnik 36/2026), page and .docx | https://www.mfin.gov.rs/propisi/pravilnik-o-kamatnim-stopama-za-koje-se-smatra-da-su-u-skladu-sa-principom-van-dohvata-ruke-za-2026-godinu-slubeni-glasnik-rs-br-362026 ; https://www.mfin.gov.rs/upload/media/aatf8h_69f0810128819.docx | 2026-10-23 |
| Tax Administration: Rulebook on arm's length interest rates for 2025 (Sl. glasnik 17/25), for comparison | https://www.purs.gov.rs/sr/pravna-lica/porez-na-dobit/podzakonska-akta-pdp/4608137/pravilnik-o-kamatnim-stopama-za-koje-se-smatra-da-su-u-skladu-sa-principom-van-dohvata-ruke-za-2025-godinu.html | 2026-10-23 |
| Tax Administration: Law on VAT, consolidated to 80/26 (Art. 38(1), RSD 8,000,000 registration turnover), page and PDF | https://www.purs.gov.rs/sr/pravna-lica/pdv/zakon/202/zakon-o-porezu-na-dodatu-vrednost.html | 2026-10-23 |
| Ministry of Finance: Zakon o poreskom postupku i poreskoj administraciji, consolidated to 80/2026 (Arts. 75, 114, 178, 178a, 179) | https://www.mfin.gov.rs/upload/media/2UkJa3_6a9fe325297c3.docx | 2026-10-23 |
| Tax Administration: corporate income tax secondary legislation list | https://www.purs.gov.rs/sr/pravna-lica/porez-na-dobit/podzakonska-akta-pdp.html | 2026-10-23 |

Not yet confirmed: whether "midpoint" (средишња вредност) in Article 60(10) means the median or the arithmetic middle of the interquartile range, so Example 1 uses a range where both are equal; how the Tax Administration orders the thin capitalisation limit and the arm's length interest test when both bite on the same loan; whether ZPPPA Article 178a fines are imposed before the ZPDPL Article 112a warning period has run out; that no advance pricing agreement procedure exists in any other Serbian law or bylaw (only the ZPDPL and ZPPPA were searched); the tax balance line codes where related-party transactions are shown.

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
