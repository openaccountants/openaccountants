---
name: ua-transfer-pricing
description: "Ukrainian transfer pricing (трансфертне ціноутворення) for tax year 2026 under article 39 of the Tax Code of Ukraine. Covers controlled deals (related non-residents, commission agents, Cabinet of Ministers low-tax states and entity forms, a non-resident and its Ukrainian PE), the UAH 150 million income and UAH 10 million per-counterparty thresholds, related persons (25% and art. 14.1.159), the five methods, the range and median rule, self-adjustment, the controlled transactions report and group notice due 1 October, the local file in 30 days, the master file (EUR 50 million) in 90 days, the country-by-country report (EUR 750 million), APAs and the art. 120 fines. Trigger on: transfer pricing Ukraine, контрольовані операції, звіт про контрольовані операції, ТЦУ, master file Ukraine, CbCR Ukraine. Out of scope: corporate tax generally (ua-corporate-income-tax), withholding, treaties and CFC rules (ua-cross-border), VAT (ukraine-vat)."
version: 0.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ukraine: transfer pricing (2026)

Ukraine requires a company that takes part in a controlled transaction to set its taxable profit at arm's length (TCU art. 39.1.1). If the terms of a controlled transaction differ from those unrelated parties would agree, the profit it would have earned at arm's length is added to its taxable profit (art. 39.1.3). All article numbers are articles of the Tax Code of Ukraine (Податковий кодекс України, Law No. 2755-VI of 2 December 2010) unless another act is named. Currency: hryvnia (UAH).

This skill links rather than repeats:

- Corporate income tax, the 18% rate, the base and the returns: [ua-corporate-income-tax](ua-corporate-income-tax.md).
- Withholding on payments to non-residents, treaty relief, permanent establishments and controlled foreign companies: [ua-cross-border](ua-cross-border.md).
- The country map: [ua-tax-overview](ua-tax-overview.md).

## Who this applies to

**Corporate income taxpayers.** Controlled transactions are business transactions that can affect the taxpayer's corporate income tax base. For Diia City residents that pay tax on special conditions, the test is the effect on the accounting result before tax (art. 39.2.1.1).

**Which deals can be controlled (art. 39.2.1.1).**

1. Transactions with related non-residents, including chains under art. 39.2.1.5.
2. Foreign trade sales or purchases of goods or services through non-resident commission agents.
3. Transactions with non-residents registered in, or resident of, a state on the Cabinet of Ministers list made under art. 39.2.1.2.
4. Transactions with non-residents whose legal form is on the Cabinet of Ministers list of forms that pay no corporate tax or are not tax resident where registered (art. 39.2.1.2-1).
5. Transactions, including internal settlements, between a non-resident and its permanent establishment in Ukraine.

Purely domestic transactions between two Ukrainian residents are not on this list.

**The thresholds (art. 39.2.1.7).** Types 1 to 4, and chains under art. 39.2.1.5, are controlled only if both tests are met for the year:

- the taxpayer's annual income from all activity, under accounting rules and net of indirect taxes, is above **UAH 150,000,000**; and
- the volume of those transactions with each counterparty, net of indirect taxes, is above **UAH 10,000,000**.

Transactions between a non-resident and its Ukrainian permanent establishment are controlled once their volume is above UAH 10,000,000 a year. The volume is counted at arm's length prices (art. 39.2.1.9).

**Related persons (art. 14.1.159).** Between legal entities the tests include: one owns, directly or indirectly, 25% or more of the other; the same person owns 25% or more of each; the same person appoints the sole executive body of each, or 50% or more of the board; the same individual is the ultimate beneficial owner of both; and loans from one entity are more than 3.5 times the other's equity (10 times for financial institutions and pure leasing companies). Between an individual and an entity the tests include: the individual owns 25% or more, appoints the sole executive or 50% or more of the board, acts as the sole executive, or is the ultimate beneficial owner.

**Chains through intermediaries (art. 39.2.1.5).** If goods or services pass between the taxpayer and a non-resident through one or more other persons that perform no substantial functions, use no substantial assets and take no substantial risks, the deal is treated as a controlled transaction with that non-resident.

**Low-tax states and entity forms.** The Cabinet of Ministers keeps the list of states under art. 39.2.1.2 (Resolution No. 1045 of 27 December 2017, current edition from 1 January 2025). The criteria are offshore status, failure to follow anti-money-laundering recommendations, and failure to exchange tax information for two years in a row. Changes approved by 30 November apply from 1 January of the next year; later changes apply from 1 January of the year after that (art. 39.2.1.2). A deal with a listed entity form is not controlled if the non-resident, or all its partners, are resident in a treaty state, shown by a certificate filed by 1 October of the following year (art. 39.2.1.2-1).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Taxpayer income test for controlled transactions (art. 39.2.1.7) | above UAH 150,000,000 a year, net of indirect taxes | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Volume test, per counterparty (art. 39.2.1.7) | above UAH 10,000,000 a year | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Non-resident and its Ukrainian PE (art. 39.2.1.7) | above UAH 10,000,000 a year | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Related persons, ownership test (art. 14.1.159) | 25% or more | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Related persons, debt test (art. 14.1.159) | loans above 3.5 times equity (10 times for financial institutions and leasing companies) | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Master file: group consolidated revenue for the prior financial year (art. 39.4.7) | EUR 50,000,000 or more | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Country-by-country report: group consolidated revenue for the prior financial year (art. 39.4.10, 39.4.10-2) | EUR 750,000,000 or more | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| EUR conversion for those two tests (art. 39.4.15) | NBU official UAH/EUR rate, average for the calendar year before the reporting year | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Corporate income tax base rate applied to a transfer pricing adjustment (art. 136.1) | 18% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Subsistence minimum for an able-bodied person at 1 January 2026, the unit for transfer pricing fines (State Budget Law 2026, art. 7) | UAH 3,328 | 2026 | https://zakon.rada.gov.ua/laws/show/4695-20 |
| 30% add-back on purchases from listed low-tax states, which does not apply to controlled transactions (art. 140.5.4) | 30% of the cost | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Document retention for transfer pricing (art. 44.3.1) | 2,555 days | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Time limit for a transfer pricing assessment (art. 102.1) | 2,555 days after the filing deadline | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |

## The taxable base

**The arm's length rule.** Profit from controlled transactions is at arm's length if their terms do not differ from those between unrelated persons in comparable uncontrolled transactions (art. 39.1.2). If they differ, the arm's length profit goes into the corporate income tax base (art. 39.1.3). The adjustment only ever raises tax: using the median of the range must not reduce the tax due (art. 39.3.2.3).

**What counts as a transaction (art. 39.2.1.4).** Goods, services, intangibles (royalties, licences, patents, trademarks, know-how), financial transactions (leasing, investments, loans, guarantee fees), sales of shares and long-term assets, dealings between a non-resident and its PE, and transfers of functions, assets, risks or opportunities that unrelated parties would not make without compensation, whether or not they are booked.

**Prices set by law (art. 39.2.1.8).** A state-regulated price is arm's length if set under that regulation. A minimum, maximum or indicative price is a floor or ceiling, not a safe harbour. A mandatory valuation, a mandatory auction or a forced sale under law also sets an arm's length price.

**The five methods (art. 39.3.1).**

1. Comparable uncontrolled price.
2. Resale price.
3. Cost plus.
4. Transactional net margin (чистого прибутку).
5. Profit split.

Closely linked transactions with one person may be grouped for the resale price, cost plus, net margin and profit split methods (art. 39.3.8).

**The range and the median (art. 39.3.2.2, 39.3.2.3).** Where the controlled price or margin is compared with several comparables, a range must be used. Inside the range, the terms are at arm's length. Outside it, tax is computed at the median of the range, unless the taxpayer has made a self-adjustment. The Cabinet of Ministers sets how the range and median are calculated.

**Self-adjustment (art. 39.5.4).** A taxpayer whose controlled prices are not at arm's length, or lack a business purpose, may adjust the price and its tax itself, if that does not reduce tax. The extra tax is paid on the normal deadlines in art. 57. No self-adjustment is allowed while a transfer pricing audit of those transactions is under way.

**Corresponding adjustment (art. 39.5.5).** If a related party in a treaty state has adjusted its tax at arm's length, the Ukrainian taxpayer may apply to the tax authority to make a matching adjustment. A refusal can go to the mutual agreement procedure under the treaty.

**Advance pricing agreements (art. 39.6.1).** A large taxpayer may apply to the State Tax Service for an advance pricing agreement on its controlled transactions.

**Interaction with other add-backs.** The 30% add-back on purchases from listed low-tax states (art. 140.5.4) does not apply to transactions that are controlled under art. 39. Thin capitalisation (art. 140.2) is in [ua-corporate-income-tax](ua-corporate-income-tax.md).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Reporting period | Calendar year | art. 39.4.1 |
| Controlled transactions report (звіт про контрольовані операції), for every controlled transaction in the year | By 1 October of the next year: 1 October 2027 for 2026 | art. 39.4.2 |
| Notice of membership in an international group (повідомлення про участь у міжнародній групі компаній), for group members with controlled transactions | By 1 October of the next year | art. 39.4.2 |
| Local file (документація з трансфертного ціноутворення) | Prepared and kept for each year. Filed within 30 calendar days of a request. A request cannot be sent before 1 October of the year after the transactions | art. 39.4.3 to 39.4.5 |
| Additional information or reasoning when the file is incomplete | Within 30 calendar days of a further request | art. 39.4.9 |
| Master file (глобальна документація), groups with EUR 50 million or more of consolidated revenue | Within 90 calendar days of a request. The request is sent no earlier than 12 months and no later than 36 months after the group's financial year end | art. 39.4.7 |
| Country-by-country report (звіт у розрізі країн), groups with EUR 750 million or more | No later than 12 months after the last day of the group's financial year | art. 39.4.10-2, 39.4.11 |

**Filing channel and language.** The report and the group notice are filed electronically (art. 39.4.2). The local file and master file are filed in Ukrainian, on paper or electronically. Foreign-language documents need a Ukrainian translation, which need not be certified. Master file amounts may be in the parent's reporting currency (art. 39.4.8).

**Corrections.** A new report may replace one filed before the deadline. After the deadline, a corrective report is filed; it does not remove the fines in art. 120.4 and 120.6. No report or corrective report may be filed for a period under a documentary audit (art. 39.4.2.1).

**When a Ukrainian entity files the country-by-country report (art. 39.4.10).** When the Ukrainian taxpayer is the ultimate parent; or the parent appoints it; or the parent's jurisdiction does not require the report; or Ukraine has a tax treaty with exchange of information with that jurisdiction but no competent authority agreement (QCAA) in force at the year end, or the QCAA is systemically not honoured. In the last three cases the Ukrainian member is released if the group files through an authorised member in a jurisdiction that requires and exchanges the report, on time, and a Ukrainian member tells the tax authority who that member is (art. 39.4.10-1).

**Martial law.** A taxpayer that cannot file or pay on time because of martial law is released from liability, but must meet the obligation within six months after martial law ends (TCU section XX, subsection 10, point 69.1; see [ua-corporate-income-tax](ua-corporate-income-tax.md)).

## Penalties and interest

The fines are multiples of the subsistence minimum for an able-bodied person set by law on 1 January of the tax year. For 2026 that is UAH 3,328 (State Budget Law 2026, art. 7). The UAH amounts below are that figure times the multiple.

| Breach | Fine | Source |
|---|---|---|
| Controlled transactions report not filed | 300 times (UAH 998,400) | art. 120.3 |
| Local file not filed on request | 3% of the controlled transactions not documented, capped at 200 times (UAH 665,600) | art. 120.3 |
| Master file not filed | 300 times (UAH 998,400) | art. 120.3 |
| Country-by-country report not filed | 1,000 times (UAH 3,328,000) | art. 120.3 |
| Group notice not filed | 100 times (UAH 332,800) | art. 120.3 |
| Still not filed 30 days after the deadline to pay the fine | 5 times (UAH 16,640) a day, capped at 300 times | art. 120.3 |
| Controlled transactions left out of a filed report | 1% of the undeclared transactions, capped at 300 times for the year | art. 120.4 |
| Country-by-country report leaves out a group member | 1% of that member's revenue, capped at 1,000 times | art. 120.4 |
| Wrong information in the group notice | 50 times (UAH 166,400) | art. 120.5 |
| Wrong information in the country-by-country report, per member | 200 times (UAH 665,600) | art. 120.5 |
| Late controlled transactions report | 1 time (UAH 3,328) a day, capped at 300 times | art. 120.6 |
| Late declaration of transactions through a corrective report | 1 time a day, capped at the lower of 300 times and 0.5% of the undeclared transactions | art. 120.6 |
| Late local file | 2 times (UAH 6,656) a day, capped at 200 times | art. 120.6 |
| Late master file | 3 times (UAH 9,984) a day, capped at 300 times | art. 120.6 |
| Late country-by-country report | 10 times (UAH 33,280) a day, capped at 1,000 times | art. 120.6 |
| Late group notice | 1 time a day, capped at 50 times | art. 120.6 |
| Extra tax assessed after an audit | 10% of the assessed tax; 25% if intentional | art. 123.1, 123.2 |
| Penalty interest on tax paid late | 120% a year of the NBU discount rate, for each day late | art. 129.4 |

Paying a fine does not remove the duty to file (art. 120.3).

## Cross-border points

- **Withholding on excess payments.** If a Ukrainian resident pays a non-resident more than the arm's length amount in a way that art. 14.1.49 treats as a dividend, it withholds 15% on the excess, unless a treaty sets another rate (art. 141.4.2). See [ua-cross-border](ua-cross-border.md).
- **Permanent establishments.** A non-resident's Ukrainian PE is taxed as if it were an independent company (art. 141.4.7), and its dealings with head office are controlled above UAH 10,000,000 a year (art. 39.2.1.7).
- **Treaty disputes.** A corresponding adjustment rests on a treaty in force, and a refusal can go to the mutual agreement procedure (art. 39.5.5).
- **Controlled foreign companies.** Separate from transfer pricing. A Ukrainian owner of a CFC can be taxed on its adjusted profit under art. 39-2; see [ua-cross-border](ua-cross-border.md).

## Worked examples

**Example 1. Distributor buying from its foreign parent.** A Ukrainian company had 2026 income of UAH 400,000,000 net of VAT. It buys goods from its Polish parent, which owns 100% of it, for UAH 60,000,000 in 2026. Both thresholds in art. 39.2.1.7 are met, so the purchases are controlled. It uses the net margin method. Its operating margin on resale revenue of UAH 80,000,000 is 1.5%, an operating profit of UAH 1,200,000. The interquartile range of comparable distributors runs from 2.0% to 4.5%, with a median of 3.2%. The margin is below the range, so tax is computed at the median (art. 39.3.2.3): arm's length profit is UAH 2,560,000. The adjustment is UAH 1,360,000 and the extra corporate income tax at 18% is UAH 244,800. The company can make this adjustment itself before an audit (art. 39.5.4). If instead the tax authority assesses it after an audit, a 10% fine of UAH 24,480 is added (art. 123.1), plus penalty interest.

```oa-check
name: Ukraine distributor below the range, adjusted to the median
inputs:
  taxpayer_income: 400000000
  purchases_from_parent: 60000000
  resale_revenue: 80000000
  actual_margin_pct: 1.5
  median_pct: 3.2
steps:
  - income_test_excess: taxpayer_income - 150000000
  - counterparty_test_excess: purchases_from_parent - 10000000
  - actual_profit: resale_revenue * actual_margin_pct / 100
  - arm_length_profit: resale_revenue * median_pct / 100
  - adjustment: arm_length_profit - actual_profit
  - extra_cit: adjustment * 0.18
  - audit_fine: extra_cit * 0.10
expected:
  income_test_excess: 250000000
  counterparty_test_excess: 50000000
  actual_profit: 1200000
  arm_length_profit: 2560000
  adjustment: 1360000
  extra_cit: 244800
  audit_fine: 24480
```

**Example 2. Late report and a local file not filed on request (edge case: the cap).** A company files its 2026 controlled transactions report 45 days late. In October 2027 the tax authority asks for the local file on controlled transactions of UAH 50,000,000. The company does not file it. The late report costs 1 subsistence minimum a day: 45 x UAH 3,328 = UAH 149,760, under the 300-times cap (art. 120.6). For the missing local file, 3% of UAH 50,000,000 is UAH 1,500,000, but the cap is 200 x UAH 3,328 = UAH 665,600, so the fine is UAH 665,600 (art. 120.3). Total fines: UAH 815,360. The file is still owed. If it is still missing 30 days after the deadline to pay that fine, a further UAH 16,640 a day runs, up to 300 times.

```oa-check
name: Ukraine transfer pricing fines with the 200-times cap
inputs:
  subsistence_minimum: 3328
  days_late_report: 45
  undocumented_transactions: 50000000
steps:
  - late_report_fine: min(days_late_report * subsistence_minimum, 300 * subsistence_minimum)
  - three_percent: undocumented_transactions * 0.03
  - doc_cap: 200 * subsistence_minimum
  - no_file_fine: min(three_percent, doc_cap)
  - total_fines: late_report_fine + no_file_fine
  - daily_after_30_days: 5 * subsistence_minimum
expected:
  late_report_fine: 149760
  three_percent: 1500000
  doc_cap: 665600
  no_file_fine: 665600
  total_fines: 815360
  daily_after_30_days: 16640
```

## Ask the client first

1. What was the company's 2026 income from all activity, net of VAT? Above UAH 150 million brings in the related-party and low-tax tests.
2. Which non-residents does it deal with, how is each related (shares, board, beneficial owner, loans), and what was the 2026 volume with each?
3. Does it deal with anyone in a state on the Cabinet of Ministers list, with a listed entity form, through a non-resident commission agent, or through intermediaries with no real function?
4. Is it part of an international group? What was the group's consolidated revenue for the prior financial year, and when does the group's year end? This sets the group notice, master file and country-by-country duties.
5. Is it a non-resident's permanent establishment, a Diia City resident or a large taxpayer (for an advance pricing agreement)?
6. What documentation and benchmarking does it already have, and has it been asked for any?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Ukraine (Податковий кодекс України), Law No. 2755-VI, consolidated text with amendments up to Law No. 4967-IX of 3 Sep 2026: arts. 14.1.159, 39 (39.1 to 39.6), 44.3.1, 57, 102.1, 120.3 to 120.6, 123.1, 123.2, 129.4, 136.1, 140.2, 140.5.4, 141.4.2, 141.4.7; section XX subsection 10 point 69.1 | https://zakon.rada.gov.ua/laws/show/2755-17 | 2026-10-30 (zakon.rada.gov.ua timed out from our network; official text read via the web.archive.org capture of 12 Oct 2026, https://web.archive.org/web/20261012050950/https://zakon.rada.gov.ua/laws/show/2755-17/print) |
| Law of Ukraine "On the State Budget of Ukraine for 2026", No. 4695-IX of 3 Dec 2025, art. 7 (subsistence minimum for able-bodied persons from 1 January 2026) | https://zakon.rada.gov.ua/laws/show/4695-20 | 2026-10-30 (read via the web.archive.org capture of 4 Jan 2026, https://web.archive.org/web/20260104102448/https://zakon.rada.gov.ua/laws/show/4695-20/print) |
| Cabinet of Ministers Resolution No. 1045 of 27 Dec 2017, list of states (territories) under art. 39.2.1.2, current edition from 1 Jan 2025 | https://zakon.rada.gov.ua/laws/show/1045-2017-п | 2026-10-30 (document card read via the web.archive.org capture of 14 Oct 2026; the list itself did not load) |
| State Tax Service of Ukraine | https://tax.gov.ua | 2026-10-30 (refused automated access with HTTP 403; not read) |

Not yet confirmed: the states on the Cabinet of Ministers list and the list of entity forms under art. 39.2.1.2-1; the Cabinet of Ministers method for the range and median; the form of the controlled transactions report and group notice (Ministry of Finance orders not read); the full contents list of the local file in art. 39.4.6; the NBU discount rate in 2026; the APA procedure and fees; any amendment after the 12 October 2026 archive capture.
