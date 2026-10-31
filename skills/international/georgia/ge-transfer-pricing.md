---
name: ge-transfer-pricing
description: "Transfer pricing in Georgia (the country, GE, currency GEL; not the US state) for tax year 2026, under Chapter XVII of the Tax Code (arts. 126 to 129^1) and the Minister of Finance Instruction on international controlled transactions (Order No 423 of 18 December 2013, as amended to Order No 331 of 2 October 2024). Covers related persons and the 50% test, which transactions are controlled (cross-border related parties, any transaction with a resident of a preferential tax country, dealings with a permanent establishment), the Government list of preferential tax countries (Ordinance No 615), the five methods and the CUP preference, the interquartile range and adjustment to the median, services and intangibles, loans treated as capital from 2025, documentation within 30 days of a request, advance pricing agreements, the country-by-country report and its GEL 5,000 fine, and how an adjustment is taxed as distributed profit. Trigger phrases: Georgia transfer pricing, controlled transactions Georgia, arm's length Georgia, offshore list Georgia, TP documentation rs.ge. Out of scope: profit tax generally (ge-corporate-income-tax), withholding and treaties (ge-cross-border), VAT (georgia-vat)."
version: 0.1
jurisdiction: GE
category: international
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia transfer pricing, 2026

Georgia's transfer pricing rules sit in Chapter XVII of the Tax Code of Georgia, "Evaluation of international controlled transactions" (arts. 126 to 129^1). The detail is in the Minister of Finance Instruction on the evaluation of international controlled transactions, approved by Order No 423 of 18 December 2013 (the Instruction). The tax authority is the Revenue Service (rs.ge). Amounts are in Georgian lari (GEL).

The Tax Code text used is the consolidated publication of 15 October 2026 on matsne.gov.ge. The Instruction was read in its original 2013 text plus the three amending orders: No 366 of 2 December 2019, No 45 of 2 March 2021 and No 331 of 2 October 2024. Matsne does not show the consolidated Instruction without a paid login, so each change below was taken from the amending order itself.

Most Georgian companies pay profit tax only when profit leaves the company (see ge-corporate-income-tax). A transfer pricing adjustment fits that model: the shortfall against an arm's length price is treated as distributed profit and taxed then (art. 98^1(4)(b)).

## Who this applies to

- **Related persons.** Two persons are related if one takes part, directly or indirectly, in the management, control or capital of the other, or if the same persons take part in both (art. 126(1)). A person takes part if it owns, directly or indirectly, more than 50% of an enterprise, or actually controls its business decisions (art. 126(2)).
- **Actual control** exists if any one of these holds (Instruction art. 3): the person holds or controls a majority of the voting shares; it can control the make-up of the board; it is entitled to 50% or more of the profit; loans it made to the enterprise plus loans the enterprise took under its guarantee exceed 50% of the book value of the enterprise's total assets; a relative of the person owns more than 50% or manages the enterprise; or control follows from the facts.
- **Controlled transactions under Chapter XVII**:
  - a financial or commercial transaction between a Georgian enterprise and a related enterprise that is not Georgian (art. 127(1)), including a resident company with its foreign parent, sister or subsidiary;
  - any transaction between a Georgian enterprise and a resident of a country with preferential tax treatment, whether or not they are related (art. 127(5));
  - transactions between an enterprise and its own permanent establishment (art. 127(7)).
- **Georgian enterprise**: an enterprise whose place of business or of management is in Georgia (art. 22(1)). A permanent establishment of a foreign enterprise counts as an enterprise (art. 21).
- **Domestic related parties** are outside Chapter XVII. Other non-market dealings are taxed under the profit tax rules instead (art. 98^1(4)):
  - with a related party that is not subject to profit tax, if the price differs from market and the relationship affects the result;
  - with a person exempt from income or profit tax.

  Both are covered in ge-corporate-income-tax.
- **Who examines**: the Revenue Service examines controlled transactions on a decision of its Head (art. 129(4)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Ownership test for related persons | more than 50%, direct or indirect | 2026 | Tax Code art. 126(2)(a), https://matsne.gov.ge/en/document/view/1043717?publication=247 |
| Control through funding | loans from and guaranteed by the person over 50% of the book value of total assets | 2026 | Instruction art. 3(d), https://matsne.gov.ge/ka/document/view/2078069 |
| Profit tax on an adjustment (distributed-profit model) | 15% of adjustment / 0.85 | 2026 | Tax Code arts. 97(10), 98(1), 98^1(4)(b), same Tax Code URL |
| Profit tax on an adjustment (banks and other annual-profit taxpayers) | 20% of taxable profit | 2026 | Tax Code arts. 98(4), 127(3), same Tax Code URL |
| Preferential tax country test | profit tax exemption, no profit tax, or a rate not over 1/3 of the Georgian rate | 2026 | Tax Code art. 98^2(5), (6), same Tax Code URL |
| Preferential tax country list | Part 1: 15 jurisdictions; Part 2: 50 countries (art. 98^2(6) cases) | 2026 | Government Ordinance No 615 of 29 December 2016, https://matsne.gov.ge/ka/document/view/3523434 |
| Interquartile range | 25th to 75th percentile, both included | 2026 | Instruction art. 2(gh), (q), (sh), same Instruction URL |
| 25th and 75th percentile positions | 1/4 and 3/4 of (number of results + 1) | 2026 | Instruction art. 2(q), (sh), same Instruction URL |
| Adjustment point when outside the range | the median, unless facts clearly point to another point | 2026 | Instruction art. 10(3), same Instruction URL |
| Documentation delivery | within 30 calendar days of a written request | 2026 | Instruction art. 17(1)(b), same Instruction URL |
| Simplified update of external comparables | every third year, if turnover is under GEL 8,000,000 in the tax year and nothing material changed | 2026 | Instruction art. 17(3), same Instruction URL |
| Prior years of data that may be considered | the 4 financial years before the year of the transaction | 2026 | Instruction art. 13(b), same Instruction URL |
| Unilateral advance pricing agreement: longest term | 3 years | 2026 | Instruction art. 22, same Instruction URL |
| Advance pricing agreement: minimum transaction volume | none since 2021 (the old GEL 50,000,000 floor was removed) | 2026 | Order No 45 of 2 March 2021, art. 1(2)(a), https://matsne.gov.ge/ka/document/view/5114015 |
| Loan treated as capital: criteria needed | at least 3 of the 12 listed, one of them from (f) to (h) | 2026 | Instruction art. 14^1(5), added by Order No 331 of 2 October 2024, https://matsne.gov.ge/ka/document/view/6281431 |
| Country-by-country report: group threshold | consolidated group revenue of EUR 750,000,000 or more in the prior fiscal year | 2026 | Tax Code art. 70^1(3)(b), same Tax Code URL |
| Country-by-country report: deadline | 12 months after the end of the accounting year | 2026 | Tax Code art. 70^1(1), same Tax Code URL |
| Late or incomplete country-by-country report | fine of GEL 5,000 | 2026 | Tax Code art. 279^1, same Tax Code URL |
| Penalty interest on late tax | 0.05% of the unpaid tax per day | 2026 | Tax Code art. 272(4), same Tax Code URL |

## The taxable base

**The arm's length principle.** Each party to a controlled transaction sets its taxable profit at arm's length (art. 127(1)). A transaction meets the test if its terms do not differ from those independent enterprises would agree in comparable circumstances (art. 127(2)). If they do differ, the profit that would have arisen at arm's length may be added to the enterprise's profit and taxed (art. 127(3)).

**Comparability.** An uncontrolled transaction is comparable if it has no difference that materially affects the indicator being tested, or if a reasonably accurate adjustment removes the difference (art. 127(4)). The Instruction is based on the OECD Transfer Pricing Guidelines. Where the Code and the Instruction are silent, the Revenue Service may follow the latest edition of the Guidelines in force at the time of the audit (Instruction art. 1(2), (3), as amended by Order No 331 of 2024).

**Methods** (art. 128(1)):

1. comparable uncontrolled price (CUP);
2. resale price;
3. cost plus;
4. transactional net margin (TNMM);
5. transactional profit split.

The most appropriate method for the case is used (art. 128(2)). If CUP and another method are equally reliable, CUP is used. If a traditional method (CUP, resale price, cost plus) and a profit-based method (TNMM, profit split) are equally reliable, the traditional method is used (Instruction art. 8(2)). One method is enough (art. 8(3)). Another method is allowed only if no listed method can reasonably be applied and the result matches what independent parties would reach; the taxpayer bears the burden of proof (art. 8(6), (7)).

**Tested party.** Resale price, cost plus and TNMM need a tested party, chosen from the functional analysis. A foreign tested party is accepted if the method is the most appropriate, the choice follows the rules, and the Georgian enterprise gives enough information on it (Instruction art. 9).

**The range and the median.**

- The arm's length range uses all comparable results when the data is complete and every material difference has been adjusted for. Otherwise it is the interquartile range (Instruction art. 10(1)).
- No adjustment is made if the tested indicator falls inside the range (art. 10(2)).
- If it falls outside, the Revenue Service may adjust the indicator to the median, unless facts clearly point to another point in the range (art. 10(3)).
- Whoever argues for a point other than the median must prove it (art. 10(4)).
- The 25th percentile is the result at position 1/4 x (n + 1) in the results sorted from low to high, and the 75th percentile the result at position 3/4 x (n + 1). If that position is not a whole number, take the nearest result. If it is exactly halfway between two results, take the lower one for the 25th and the higher one for the 75th. The median is the lowest result with at least 50% of results at or below it. If exactly 50% are at or below it, the median is the average of that result and the next higher one (Instruction art. 2).

**Data years.** Use data for the year of the controlled transaction. Earlier years may be used if current data is not available. Data for the 4 prior years may also be used where it shows facts that bear on comparability, such as product or business cycles (Instruction art. 13).

**Actual transactions.** The Revenue Service works from the transaction as the parties actually structured it. It may disregard or replace it only if its substance differs from its form, or if independent parties acting rationally would not have agreed it and the structure prevents a proper test (Instruction art. 14).

**Services.** An intra-group service charge is arm's length only if all of these hold (Instruction art. 15):

- the service was actually provided;
- it has economic or commercial value for the recipient;
- an independent enterprise would pay for it, or perform it for itself;
- the amount is what independent parties would agree.

Shareholder activities cannot be charged. These include the parent's own shareholder meetings, share issues, supervisory board, consolidated reporting, and raising funds to buy group companies that do not benefit the payer. Where services to several group companies cannot be identified one by one, the total is allocated on a reasonable basis.

**Intangibles.** Licences and transfers of intangibles are priced from the view of both the transferor and the transferee. The test takes into account the expected benefit, geographic limits, exclusivity and the right to develop the asset further (Instruction art. 16).

**Loans treated as capital (from 1 January 2025).** In an international controlled transaction, a loan can be treated in whole or in part as a capital contribution (Instruction art. 14^1, added by Order No 331 of 2024). "Loan" here includes credit, overdrafts, letters of credit, credit lines, guarantees and debt securities (art. 14^1(2)). The Revenue Service needs at least three of twelve criteria, at least one of them from (f) to (h), and must write a reasoned conclusion (art. 14^1(5)). The criteria (art. 14^1(3)) are:

- (a) no fixed repayment schedule;
- (b) no interest obligation, or interest not actually charged;
- (c) no enforcement on default;
- (d) the lender is subordinated to other creditors;
- (e) no covenants or security;
- (f) the borrower cannot repay principal and interest from operating profit;
- (g) the borrower's debt to equity ratio is outside the market range;
- (h) no real need for the loan, or the money funds long-term assets or a start-up;
- (i) repeated deferral of payments;
- (j) the lender takes part in management;
- (k) the loan is made in proportion to shareholding;
- (l) the loan can be converted into capital.

The test applies as at the time of the transaction (art. 14^1(4)). It does not apply to exchange differences arising before 1 January 2025, or to interest accrued before that date, on loans issued before that date (Order No 331, art. 2(1)).

**How an adjustment is taxed.** A controlled transaction whose terms fail the arm's length test is distributed profit, in the amount of the adjustment (art. 98^1(4)(b)). Under the distributed-profit model the adjustment is divided by 0.85 and taxed at 15% (arts. 97(1), 97(10), 98(1)). A bank, credit union, microfinance organisation or loan provider adds the extra profit to its annual taxable profit, taxed at 20% (arts. 97(12), 98(4), 127(3)).

**Preferential tax countries.** A country, or a separate territory of a country, has preferential tax treatment if a legal person there is exempt from profit tax, or pays no profit tax, or pays at a rate not over 1/3 of the Georgian rate (art. 98^2(5), (6)). With the 15% rate that is 5% or less. The Government publishes the list (art. 98^2(10)). The list in force is Ordinance No 615 of 29 December 2016, in force from 1 January 2017.

- **Part 1** (15 jurisdictions): Anguilla, Bahamas, Bahrain, Bermuda, British Virgin Islands, Guernsey, Vanuatu, Cayman Islands, Curaçao, Isle of Man, Marshall Islands, Micronesia, Palau, Sark, Turks and Caicos Islands.
- **Part 2** lists 50 countries treated as preferential under art. 98^2(6), where a regime for some legal persons meets the test. Examples are Andorra, the United Arab Emirates, Cyprus, Hong Kong, Jersey, Liechtenstein, Luxembourg, Malaysia, Panama and Seychelles.
- **Treaty countries.** Note 3 of the list matters. If Georgia has a ratified tax treaty in force with a listed country, that country is treated as preferential only for the profit tax rules in art. 98^1(2)(e) (foreign dividends passed on) and art. 98^2(3)(a) to (e) (debt securities, fines, advances, loans and claims). So for art. 127(5) an unrelated counterparty in a treaty country on the list is not caught by the preferential rule.

For an unrelated counterparty in a preferential tax country, the Instruction says the terms are treated as arm's length if the Revenue Service considers the parties are not related under art. 126(1) (Instruction art. 4).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Transfer pricing documentation | prepared before the tax return is filed; delivered within 30 calendar days of a written request | Instruction arts. 2(i), 17(1) |
| Profit tax on a self-made adjustment (distributed-profit model) | monthly return and payment by the 15th of the following month | Tax Code arts. 62(2), 153(10) |
| Annual profit tax return (banks and others on annual profit) | before 1 April of the following year | Tax Code art. 153(1)(b) |
| Advance pricing agreement application | before the transactions start | Tax Code art. 129^1(1); Instruction art. 20(2) |
| Pre-filing meeting for an advance pricing agreement | if the Revenue Service considers one needed, it contacts the company within 14 days of the request to fix a time and place | Instruction art. 23(4), as amended by Order No 45 of 2021 |
| Advance pricing agreement annual compliance report | for each calendar year of the agreement, before 1 April of the following year, on the form in Annex 4 | Instruction art. 31, as amended by Order No 45 of 2021 |
| Revenue Service answer on a corresponding adjustment request | within 6 months of receiving the request | Instruction art. 37 |
| Country-by-country report (Georgian ultimate parent) | within 12 months after the end of the accounting year | Tax Code art. 70^1(1) |
| Notice that a Georgian group member is the ultimate or surrogate parent | before the end of the accounting year | Tax Code art. 70^1(2) |

**What the documentation contains** (Instruction art. 17(2)):

- an overview of the business and the economic factors that affect its pricing;
- the corporate and organisational structure;
- a description of each tested transaction, with the comparability factors and the group pricing policy;
- the method chosen and why;
- the comparability analysis: the comparables, why internal comparables were rejected, the search for external comparables, and any comparability adjustments;
- the economic analysis and forecasts relied on;
- any advance pricing agreement or ruling;
- the conclusion on arm's length, and any adjustment made;
- any other information that materially affects the conclusion.

It may be in Georgian or English, and on paper or electronic. On request, English documents must be translated into Georgian at the taxpayer's cost (art. 17(4), (5)). If turnover is under GEL 8,000,000 in the tax year, the external comparable search needs updating only every third year, if nothing material has changed (art. 17(3)).

**Advance pricing agreements.**

- The Head of the Revenue Service may sign one at the taxpayer's request, before the transactions start, for a fixed period (art. 129^1(1)). It binds only the taxpayer it was made with (art. 129^1(2)).
- While the taxpayer follows it, no contrary decision, tax or sanction may be imposed (art. 129^1(3)).
- It stops applying if the facts it rests on are wrong or the law it rests on changes (art. 129^1(4)).
- The Instruction covers unilateral agreements of up to 3 years (arts. 18, 22). The Revenue Service may also consider bilateral and multilateral agreements (art. 19).
- An annual compliance report is due for each calendar year of the agreement, before 1 April of the following year (art. 31). The Revenue Service may revise, cancel or revoke the agreement (arts. 32 to 34).

**Corresponding adjustments and mutual agreement.**

- If a treaty partner adjusts the profit of a related enterprise, so that profit already taxed in Georgia is taxed there, the Georgian enterprise can ask the Revenue Service to check the adjustment. If it is arm's length, the Revenue Service corrects the Georgian tax (art. 129(2)). The request includes proof of the related party's tax residence and of the foreign adjustment, and the Revenue Service answers within 6 months (Instruction art. 37).
- A case can also go to the mutual agreement procedure under the treaty (Instruction art. 38).

## Penalties and interest

The Tax Code has no separate penalty for missing transfer pricing documentation. An adjustment raises the tax due, so the general sanctions apply.

| Offence | Penalty | Source |
|---|---|---|
| Understatement found on audit, up to 5% of the tax declared | 10% of the understated tax | Tax Code art. 275(2^1) |
| Understatement over 5% and up to 20% | 25% of the understated tax | art. 275(2^2) |
| Understatement in other cases | 50% of the understated tax | art. 275(2) |
| Cap on art. 275 fines from one audit | not more than the tax assessed in that audit | art. 275(5) |
| Understatement over GEL 100,000 | large-scale tax evasion under criminal law | art. 275(4) |
| Late payment | penalty interest 0.05% of the unpaid tax per day, including the day of payment | art. 272(4) |
| Penalty interest time limit | not charged once 3 years have passed from the day the obligation to charge it arose | art. 272(2^1) |
| Late or incomplete country-by-country report | GEL 5,000 | art. 279^1 |
| Acting within an advance pricing agreement | no tax or sanction contrary to the agreement | art. 129^1(3), (7) |

Documentation is the taxpayer's answer to a request to explain why its profit is arm's length (art. 129(1)). The request is satisfied if the documentation was prepared under the Instruction and handed over within 30 calendar days (Instruction art. 17(1)).

## Cross-border points

- **Withholding is separate.** A transfer pricing adjustment does not change withholding on the actual payment. Interest, royalties and other income paid to a person registered in a preferential tax country bear 15% withholding (art. 134(1^1)); see ge-cross-border.
- **Profit tax on payments to preferential tax countries.** Loans, advances, fines, debt securities and lost claims involving a person registered in a preferential tax country are taxed as costs unrelated to business when made, with a credit when the money comes back (art. 98^2(3), (7), (8)); see ge-corporate-income-tax.
- **Permanent establishments.** A permanent establishment is allotted the profit it would earn as an independent enterprise doing the same work in the same conditions. Profit it sends to its head office is distributed profit (art. 98^1(3)). Dealings with the head office are tested under art. 127(7).
- **Treaties.** Corresponding adjustments under art. 129(2) are available only with a treaty country. Treaty relief from withholding follows art. 125; see ge-cross-border.
- **Moving an offshore company's assets to Georgia.** All assets of a foreign enterprise registered in a preferential tax country may move to a Georgian enterprise before 1 January 2028, if the same individuals own 100% of both (art. 309(146)). The reliefs are:
  - no profit or income tax on income from that activity treated as Georgian-source;
  - no import tax on the assets;
  - no property tax on them until 1 January 2030.

## Worked examples

### Example 1: CUP on goods sold to a foreign parent

A Georgian LLC on the distributed-profit model makes furniture. In May 2026 it sells a batch to its parent company in another country for GEL 400,000. In the same month it sells identical furniture to independent buyers on the same terms for GEL 460,000 a batch. The parties are related (over 50% ownership, art. 126(2)(a)), so the sale is a controlled transaction (art. 127(1)). CUP is the preferred method when it is as reliable as the others (Instruction art. 8(2)).

The shortfall of GEL 60,000 is distributed profit (art. 98^1(4)(b)). Grossed up, it is 60,000 / 0.85 = GEL 70,588.24, and profit tax at 15% is GEL 10,588.24 (arts. 97(10), 98(1)). If the LLC makes the adjustment itself, it reports and pays by 15 June 2026 (arts. 62(2), 153(10)).

```oa-check
name: Georgia CUP adjustment on goods sold to a foreign parent, 2026
inputs:
  controlled_price: 400000
  comparable_price: 460000
steps:
  - adjustment: max(comparable_price - controlled_price, 0)
  - taxable_amount: adjustment / 0.85
  - profit_tax: taxable_amount * 0.15
expected:
  adjustment: 60000.00
  taxable_amount: 70588.24
  profit_tax: 10588.24
```

### Example 2: TNMM below the interquartile range, adjusted to the median

A Georgian LLC provides back-office services to its foreign parent. In 2026 its costs are GEL 3,000,000 and it charges a 1.5% mark-up (net cost plus). A search finds seven comparable companies. Their net cost plus margins, sorted from low to high, are 2.1%, 3.4%, 4.0%, 5.2%, 6.1%, 7.5% and 9.0%. The data is not complete enough for the full range, so the interquartile range applies (Instruction art. 10(1)).

With seven results, the 25th percentile is result number 1/4 x 8 = 2 (3.4%) and the 75th percentile is result number 3/4 x 8 = 6 (7.5%). The median is the 4th result (5.2%), since 4 of the 7 results (57%) are at or below it (Instruction art. 2). The 1.5% mark-up is below 3.4%, so the Revenue Service adjusts to the median (art. 10(3)).

The adjustment is (5.2% - 1.5%) x 3,000,000 = GEL 111,000. Grossed up, it is 111,000 / 0.85 = GEL 130,588.24, and profit tax is GEL 19,588.24. Penalty interest and an art. 275 fine also apply if the adjustment comes from an audit; they are not computed here.

```oa-check
name: Georgia TNMM below the interquartile range, adjusted to the median, 2026
inputs:
  costs: 3000000
  tested_markup_pct: 1.5
  n_results: 7
  result_2_pct: 3.4
  result_4_pct: 5.2
  result_6_pct: 7.5
steps:
  - q1_position: (n_results + 1) / 4
  - q3_position: (n_results + 1) * 3 / 4
  - lower_quartile_pct: result_2_pct
  - median_pct: result_4_pct
  - upper_quartile_pct: result_6_pct
  - below_range: max(lower_quartile_pct - tested_markup_pct, 0)
  - adjustment: (median_pct - tested_markup_pct) / 100 * costs
  - taxable_amount: adjustment / 0.85
  - profit_tax: taxable_amount * 0.15
expected:
  q1_position: 2
  q3_position: 6
  below_range: 1.9
  adjustment: 111000.00
  taxable_amount: 130588.24
  profit_tax: 19588.24
```

## Ask the client first

1. Who owns or controls the company, directly and indirectly, and are any owners relatives of each other? This tells you who is related (art. 126; Instruction art. 3).
2. Which counterparties are outside Georgia, and is any of them registered in a jurisdiction on the Government list? If so, does Georgia have a tax treaty in force with that country?
3. What flows each way: goods, services, royalties, loans, guarantees? Get the amounts for the year.
4. Is the company a bank, credit union, microfinance organisation or loan provider (annual profit at 20%), or on the distributed-profit model?
5. Is there existing documentation, an advance pricing agreement, or a foreign adjustment that may call for a corresponding adjustment?
6. Is the company part of a group with consolidated revenue of EUR 750 million or more, and is the ultimate parent Georgian?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Georgia, consolidated English text, publication of 15 October 2026 (arts. 21, 22, 62, 70^1, 97, 98, 98^1, 98^2, 125 to 129^1, 134, 153, 272, 275, 279^1, 309(146)) | https://matsne.gov.ge/en/document/view/1043717?publication=247 | 2026-10-31 |
| Tax Code of Georgia, Georgian original, same publication (arts. 70^1, 125 to 129^1, 134, 279^1) | https://matsne.gov.ge/ka/document/view/1043717?publication=247 | 2026-10-31 |
| Minister of Finance Order No 423 of 18 December 2013, Instruction on the evaluation of international controlled transactions (original text, arts. 1 to 38) | https://matsne.gov.ge/ka/document/view/2078069 | 2026-10-31 |
| Minister of Finance Order No 366 of 2 December 2019 (amends Instruction art. 1) | https://matsne.gov.ge/ka/document/view/4720605 | 2026-10-31 |
| Minister of Finance Order No 45 of 2 March 2021 (amends Instruction arts. 20, 23 to 27, 30 to 32) | https://matsne.gov.ge/ka/document/view/5114015 | 2026-10-31 |
| Minister of Finance Order No 331 of 2 October 2024 (amends Instruction art. 1, adds art. 14^1) | https://matsne.gov.ge/ka/document/view/6281431 | 2026-10-31 |
| Government of Georgia Ordinance No 615 of 29 December 2016, list of countries with preferential tax treatment | https://matsne.gov.ge/ka/document/view/3523434 | 2026-10-31 |

Not yet confirmed: the consolidated text of the Instruction (matsne shows it only with a paid login, so it was rebuilt from the original and the three amending orders, and any change made other than by those orders would be missed); the Minister of Finance order on how the country-by-country report is filed (art. 70^1(4)); whether Georgia requires a master file, a local file or an annual controlled-transaction return beyond the Instruction art. 17 documentation (none found in the Tax Code or the Instruction); the Revenue Service's published mutual agreement procedure; the Minister of Finance annual interest rate cap for related-party loans (art. 98^2(1)(e)); the time limit for a transfer pricing assessment; how the art. 275 fines apply to a deemed distribution found on audit (whether "tax declared" is the monthly return amount).
