---
name: im-related-party-uk-treaty
description: >
  Use this skill for related-party (associated enterprise) pricing between the
  Isle of Man and the United Kingdom for the 2026/27 tax year, under Article 9 of
  the 2018 UK-Isle of Man double taxation agreement. It covers when two enterprises
  are associated (participation in management, control or capital), the primary
  profit adjustment, the corresponding adjustment the other territory must make,
  company treaty residence, the principal purpose test, the three-year mutual
  agreement time limit and the two-year route to arbitration, the Manx company
  rates (0%, 10%, 20%) that decide what a corresponding adjustment is worth, and
  the only express arm's-length rule in the Income Tax Act 1970 (petroleum
  extraction). Trigger on: Isle of Man transfer pricing, UK Isle of Man related
  party, Article 9 corresponding adjustment, Isle of Man MAP, associated
  enterprises Isle of Man. Out of scope: treaties other than the UK, country-by-
  country reporting, Pillar 2 domestic top-up tax, company tax computation
  (im-corporate-income-tax).
jurisdiction: IM
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-30
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Isle of Man-UK related-party treaty adjustments (2026/27) v0.2

This skill covers pricing between associated enterprises in the Isle of Man-UK corridor under the 2018 double taxation agreement (UK SI 2018/1347), which entered into force on 19 December 2018 and has effect for Manx income tax from 6 April 2019. The Manx law is the Income Tax Act 1970 (AT 3 of 1970); the authority is the Income Tax Division of the Treasury. For company tax computation see [im-corporate-income-tax](im-corporate-income-tax.md); for individuals and the treaty's residence, employment and pension articles see [im-non-resident-income-tax](im-non-resident-income-tax.md).

## Who this applies to

- **Associated enterprises (Article 9(1)).** Two enterprises are associated where an enterprise of one territory participates directly or indirectly in the management, control or capital of an enterprise of the other, or the same persons participate directly or indirectly in the management, control or capital of both. The article sets no ownership percentage.
- **Treaty residence of companies (Article 4).** A person is resident if liable to tax by reason of domicile, residence, place of management, place of incorporation or a similar criterion; liability on source income only does not count (Art. 4(1)). A company resident in both territories is assigned by mutual agreement of the competent authorities, having regard to its place of effective management, place of incorporation and other factors. Without that agreement it gets no treaty benefits except under Articles 22 (elimination of double taxation), 24 (non-discrimination) and 25 (mutual agreement) (Art. 4(3)).
- **Manx company residence.** A company incorporated in the Island is resident there for tax purposes (ITA 1970 s.2N; PN 144/07 para 16). A company incorporated elsewhere is resident in the Island if its business is managed and controlled there (PN 144/07 para 17).
- **Out of scope:** pricing with countries other than the UK, and country-by-country reporting.

## Rates, bands and thresholds

Article 9 adjusts profits; it sets no rate. The value of an adjustment depends on the rate the Manx enterprise pays.

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Company rate, all other income | 0% | 2026/27 | PN 227/26 https://www.gov.im/media/1391759/pn-227-26-budget.pdf |
| Company rate, banking business | 10% | 2026/27 | PN 227/26 |
| Company rate, retail business profits above GBP 500,000 | 10% | 2026/27 | PN 227/26 |
| Company rate, land and property in the Isle of Man | 20% | 2026/27 | PN 227/26 |
| Company rate, petroleum extraction | 20% | 2026/27 | PN 227/26 |
| Other non-corporates | 21% | 2026/27 | PN 227/26 |
| Domestic top-up tax (Pillar 2), groups with revenue of EUR 750 million or more | minimum effective rate 15% on Isle of Man profits | fiscal years from 1 January 2025 | PN 227/26 |
| Mutual agreement: time to present a case | 3 years from first notification of the action | from 6 April 2019 | SI 2018/1347 Art. 25(1) |
| Arbitration: unresolved case may go to arbitration | after 2 years from presentation to the other competent authority | from 6 April 2019 | SI 2018/1347 Art. 25(5) |

## The base

### Primary adjustment (Article 9(1))

Where associated enterprises make or impose conditions in their commercial or financial relations that differ from those between independent enterprises, profits that would have accrued to one enterprise but for those conditions may be included in its profits and taxed.

### Corresponding adjustment (Article 9(2))

Where one territory includes in its enterprise's profits, and taxes, profits on which the other territory's enterprise has already been charged, and those profits would have accrued to the first enterprise under independent-enterprise conditions, the other territory makes an appropriate adjustment to the tax it charged on those profits. Due regard is had to the other articles, and the competent authorities consult each other if necessary. A foreign assessment alone does not show that the conditions are met.

### Manx domestic law

The only express arm's-length rule found in the consolidated Income Tax Act 1970 is section 119BA: in computing income from petroleum extraction activities or rights, any transaction with a connected person (as defined in s.119C) is computed on an arm's-length basis. No general domestic transfer-pricing provision was found in that Act.

### Deductions and non-discrimination (Article 24)

Interest, royalties and other disbursements paid by an enterprise of one territory to a resident of the other are deductible under the same conditions as if paid to a resident of the first territory, except where Article 9(1), Article 11(8), Article 12(8), Article 20(4) or Article 23 applies (Art. 24(3)). An enterprise owned or controlled by residents of the other territory may not be taxed more heavily than similar local enterprises (Art. 24(4)).

### Workpaper (our preparation method, not a filing requirement)

1. Draw the ownership, management and control links, each enterprise's treaty residence and the period.
2. Identify the transaction, contract terms, invoices, booked amounts and who performed the work.
3. Record the functions, assets and risks behind the independent-party result, with the comparables and their limits.
4. Reconcile the proposed adjustment to each enterprise's ledger and tax computation, keeping currency and timing consistent.
5. Obtain the other territory's assessment, calculation, payment evidence and correspondence, and show which profits were taxed twice.
6. Record the request, decision and implementation of relief, keeping domestic appeal and payment deadlines under separate control.

## Deadlines and filing

- **Mutual agreement.** A person who considers that either territory's action results in taxation not in accordance with the agreement may present the case to either competent authority, whatever the domestic remedies, within three years from the first notification of that action (Art. 25(1)). An agreement reached is implemented notwithstanding domestic time limits (Art. 25(2)).
- **Arbitration.** If the competent authorities cannot agree within two years from presentation of the case to the other competent authority, unresolved issues go to arbitration at the person's request, unless a court or administrative tribunal of either territory has already decided them (Art. 25(5)). The 2024 memorandum of understanding requires a written request identifying the case, with a statement from each person directly affected that no court or tribunal decision has been given on the same issues (Part 1), and sets the minimum information: identity, the treaty provisions at issue, facts, analysis and any parallel requests (Part 2).
- Company return dates are in [im-corporate-income-tax](im-corporate-income-tax.md).

## Penalties and interest

The agreement sets no penalty. Manx penalties and interest on a company return changed by a related-party adjustment are on the Not yet confirmed line.

## Cross-border points

- **Principal purpose test (Article 23).** A treaty benefit, including corresponding relief, is denied where obtaining it was one of the principal purposes of an arrangement, unless granting it accords with the object and purpose of the provision. The competent authority may still grant it on request after considering the facts, and consults the other authority before rejecting a request from a resident of the other territory.
- **Elimination of double taxation (Article 22).** Where the UK may tax income of a Manx resident under the agreement, the Island gives credit subject to its own law on foreign tax credits (Art. 22(1)); for the Manx limit see ITA 1970 s.57 in [im-income-tax](im-income-tax.md).
- **Other treaties** are not covered; read each agreement.

## Worked examples

### Example 1: primary adjustment on goods

A Manx company sells 1,000 units a year to its UK parent at GBP 80 each. A supported analysis shows independent parties would have priced them at GBP 95. The profit that would have accrued to the Manx company under Article 9(1) is GBP 15,000. If the Manx company's trading income is taxed at 0%, the Island gains no tax from this adjustment. The UK parent's cost was below the arm's-length price, so Article 9(1) gives the UK no adjustment to make on its side.

```oa-check
name: IM-UK associated enterprises, pricing difference on goods
inputs:
  units: 1000
  booked_unit_price: 80
  supported_unit_price: 95
steps:
  - booked_revenue: units * booked_unit_price
  - supported_revenue: units * supported_unit_price
  - adjustment: supported_revenue - booked_revenue
expected:
  booked_revenue: 80000.00
  supported_revenue: 95000.00
  adjustment: 15000.00
```

### Example 2: corresponding adjustment, rate decides the value

A Manx company lets Isle of Man property to its UK-resident affiliate for GBP 110,000 a year and pays 20% Manx tax on that land and property income. HMRC finds an arm's-length rent of GBP 95,000 and disallows GBP 15,000 of the UK deduction. If the Article 9(2) conditions are met, the Island reduces the Manx company's taxable profit by GBP 15,000, which cuts its Manx tax by GBP 3,000. Had the income been taxed at 0%, the corresponding adjustment would be worth nothing in the Island, and the GBP 15,000 would be taxed once, in the UK.

```oa-check
name: IM-UK corresponding adjustment at 20% and 0%
inputs:
  rent_paid: 110000
  arm_length_rent: 95000
  rate_land: 20
  rate_other: 0
steps:
  - adjustment: rent_paid - arm_length_rent
  - manx_relief_land: pct(adjustment, rate_land)
  - manx_relief_other: pct(adjustment, rate_other)
expected:
  adjustment: 15000.00
  manx_relief_land: 3000.00
  manx_relief_other: 0.00
```

## Ask the client first

1. Which entities are involved, where is each tax resident, and who participates in their management, control or capital?
2. What was supplied, on what terms, and what evidence supports the price?
3. Which Manx rate applies to the Manx entity's income (0%, 10% or 20%)?
4. Has either tax authority adjusted the profits, when was the first notification, and what tax has been assessed and paid?
5. Has a mutual agreement or arbitration request already been made?

## Sources

| Source | URL | Read on |
|---|---|---|
| UK-Isle of Man Double Taxation Agreement 2018, SI 2018/1347, Articles 4, 9, 22, 23, 24, 25 | https://www.legislation.gov.uk/uksi/2018/1347/pdfs/uksi_20181347_en.pdf | 2026-10-30 |
| HMRC, Isle of Man tax treaties (2018 agreement in force from 19 December 2018) | https://www.gov.uk/government/publications/isle-of-man-tax-treaties | 2026-10-30 |
| HMRC, 2024 UK-Isle of Man memorandum of understanding (arbitration), Parts 1 and 2 | https://www.gov.uk/government/publications/isle-of-man-tax-treaties/2024-uk-isle-of-man-memorandum-of-understanding-in-force | 2026-10-30 |
| Income Tax Division, International agreements and double taxation relief (UK agreement effective 6 April 2019) | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/international-agreements-and-double-taxation-relief/ | 2026-10-30 |
| Practice Note PN 227/26, Budget 2026 proposals (company rates, Pillar 2) | https://www.gov.im/media/1391759/pn-227-26-budget.pdf | 2026-10-30 |
| Practice Note PN 144/07, Tax residence in the Isle of Man, paras 16 and 17 | https://www.gov.im/media/97083/pn14407taxresidenceintheisl.pdf | 2026-10-30 |
| Income Tax Act 1970 (AT 3 of 1970), consolidated text [62], ss.2N, 57, 119BA, 119C | https://legislation.gov.im/cms/images/LEGISLATION/PRINCIPAL/1970/1970-0003/1970-0003_62.pdf | 2026-10-30 |

Not yet confirmed: whether other Manx legislation (outside the Income Tax Act 1970) contains a general related-party pricing rule; country-by-country reporting scope and deadlines (the 2017 regulations, SD 2017/0091, could not be opened); Manx penalties and interest on an adjusted company return; the domestic procedure and time limit for claiming a corresponding adjustment in the Island; pricing methods, documentation and safe harbours accepted by the Income Tax Division.

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
