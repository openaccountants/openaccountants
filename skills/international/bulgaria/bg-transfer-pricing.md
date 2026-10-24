---
name: bg-transfer-pricing
description: "Bulgarian transfer pricing (трансферно ценообразуване) for tax year 2026 under the Corporate Income Tax Act (ZKPO) Article 15, the Tax-Insurance Procedure Code (DOPK) Chapter 8a (Articles 71a to 71zh), Articles 116 and 278a, the related-party definition in DOPK Additional Provisions para. 1 item 3, and Ordinance N-3 of 7 November 2025 on the market price methods, which replaced Ordinance N-9 from 1 January 2026. Covers who is related, the arm's length rule for domestic and cross-border deals, the five methods, the interquartile range and adjustment to the median, local and master file tests and euro thresholds, the 30 June deadline, hidden profit distribution, penalties, country-by-country reporting and the absence of an APA procedure. Trigger on: Bulgaria transfer pricing, местно досие, обобщено досие, свързани лица, Наредба Н-3, Bulgarian local file, country-by-country report Bulgaria. Out of scope: the full CIT computation, thin capitalisation detail and withholding tax (bg-corporate-income-tax), VAT (bulgaria-vat-return)."
version: 0.1
jurisdiction: BG
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bulgaria: transfer pricing (трансферно ценообразуване), tax year 2026

Source-cited draft: not reviewed by an accountant, not for filing.

The arm's length rule is one sentence in the Corporate Income Tax Act (Закон за корпоративното подоходно облагане, ZKPO), Article 15. Everything else sits in the Tax-Insurance Procedure Code (Данъчно-осигурителен процесуален кодекс, DOPK): the related-party definition (Additional Provisions, para. 1, item 3), the list of methods (para. 1, item 10), the burden of proof (Article 116), the documentation rules (Chapter 8a, Articles 71a to 71zh), country-by-country reporting (Articles 143u to 143shch) and the penalties (Article 278a). How the methods are applied is set by the Minister of Finance in Ordinance N-3 of 7 November 2025 (Наредба № Н-3, State Gazette 96/2025). It applies from 1 January 2026 and repeals Ordinance N-9 of 2006 (Ordinance N-3, paras. 3 and 5). Article numbers below refer to the lex.bg consolidated texts (ZKPO to State Gazette 55/2026, DOPK to State Gazette 85/2026).

Bulgaria adopted the euro on 1 January 2026. Some DOPK amounts were rewritten in euro by the Euro Introduction Act. Others are still printed in leva; those are read as euro at the fixed rate of BGN 1.95583, rounded to the cent (Euro Introduction Act, Articles 11(2), 12 and 13). Where this skill shows a euro figure for a leva amount, that is the converted figure.

For the corporate tax computation, the 10% rate, the Article 43 thin capitalisation rule, the Article 43a interest limit and withholding tax, see [bg-corporate-income-tax](bg-corporate-income-tax.md). That skill still carries 2025 figures and will be rewritten separately.

## Who this applies to

- **Every corporate taxpayer with related-party dealings.** Article 15 ZKPO applies to any commercial or financial relationship between related parties whose terms differ from those between unrelated parties and affect the tax base. The tax base is then set on the terms unrelated parties would have agreed. The National Revenue Agency (NRA) states that the rules apply to all related-party deals, not only cross-border ones.
- **Who is related (DOPK para. 1, item 3).** The main tests:
  - spouses, direct-line relatives, collateral relatives to the third degree and in-laws to the second degree (item 3(a));
  - employer and employee; partners (items 3(b) and (c));
  - persons where one takes part in managing the other or its subsidiary, or where the same person sits on both management or supervisory bodies (items 3(d) and (e));
  - a company and a person holding more than 5% of its voting shares. For Chapter 8a (documentation) the test is 25% (item 3(f));
  - one person controls the other, both are controlled by a third person, or both jointly control a third person (items 3(g) to (i)). Control means more than half the votes, the power to appoint more than half of a governing body, or decisive influence by any other means (para. 1, item 4);
  - commercial agent and principal; donor and recipient (items 3(k) and (l));
  - persons who take part directly or indirectly in management, control or capital so that they can agree non-standard terms (item 3(m));
  - a resident and a foreign counterparty if both of these hold: the counterparty is registered outside the EU in a state whose tax on the income from the deals is more than 60% lower than Bulgarian tax, and that state refuses or is unable to exchange information on the deals although a tax treaty is in force (item 3(n)). The first test is met unless the Bulgarian party proves that the counterparty pays tax that is not a preferential regime, or that it sold the goods or performed the services on the local market. Owners of both sides are related too (item 3(o)).
- **Permanent establishments.** Chapter 8a applies to transfers between a Bulgarian place of business of a foreign company and the rest of that company abroad (DOPK Article 71zh(1)).
- **Sole traders.** Sole traders taxed under Article 26 of the Personal Income Tax Act are in the documentation rules (DOPK Article 71b(1)).
- **Who must prepare a local file (DOPK Article 71b).** A resident company, a foreign company with a Bulgarian place of business, or a sole trader with controlled transactions. Excluded:
  - entities exempt from corporate tax and entities taxed only with alternative tax (they document only their corporate-tax activity) (Article 71b(2), items 1 and 2, and (3));
  - entities that, at 31 December of the previous year, do not exceed at least two of: balance sheet assets EUR 20,000,000; net sales revenue EUR 40,000,000; average staff 250 (Article 71b(2), item 3). So a local file is required only when at least two of the three are exceeded;
  - entities whose controlled transactions are all domestic (Article 71b(2), item 4);
  - transactions with individuals other than sole traders (Article 71b(4)).
- **Not exempt from Article 15.** A small company or a purely domestic group has no documentation duty but must still deal at arm's length. Under Article 116(2) DOPK it must prove the market price in an audit.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Corporate income tax rate (applies to any transfer pricing adjustment) | 10% | 2026 | https://lex.bg/laws/ldoc/2135540562 (ZKPO Art. 20) |
| Related party, general shareholding test | more than 5% of voting shares | 2026 | https://lex.bg/laws/ldoc/2135514513 (DOPK para. 1, item 3(f)) |
| Related party, shareholding test for documentation | 25% of voting shares | 2026 | https://lex.bg/laws/ldoc/2135514513 (DOPK para. 1, item 3(f)) |
| Low-tax counterparty test (non-EU state, no information exchange) | tax more than 60% lower than in Bulgaria | 2026 | https://lex.bg/laws/ldoc/2135514513 (DOPK para. 1, item 3(n)) |
| Size test: local file only if at least two exceeded at 31 Dec of the prior year | assets EUR 20,000,000; net revenue EUR 40,000,000; staff 250 | 2026 | https://lex.bg/laws/ldoc/2135514513 (DOPK Art. 71b(2)(3)); https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=224950 (Euro Act para. 34) |
| Local file transaction threshold, sale of goods | BGN 400,000 = EUR 204,516.75 per transaction in the year, excluding VAT and excise | 2026 | https://lex.bg/laws/ldoc/2135514513 (DOPK Art. 71b(5)(1)(a)) |
| Local file transaction threshold, all other transactions | BGN 200,000 = EUR 102,258.38 | 2026 | https://lex.bg/laws/ldoc/2135514513 (DOPK Art. 71b(5)(1)(b)) |
| Local file threshold, loans | principal above BGN 1,000,000 = EUR 511,291.88, or interest and other loan income or expense above BGN 50,000 = EUR 25,564.59 | 2026 | https://lex.bg/laws/ldoc/2135514513 (DOPK Art. 71b(5)(2)) |
| Leva to euro conversion | BGN 1.95583 = EUR 1, rounded to the cent | 2026 | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=224950 (Euro Act Arts. 11 to 13) |
| Comparable search refresh | at least every three years; financial data of comparables every year | 2026 | https://lex.bg/laws/ldoc/2135514513 (DOPK Art. 71e(3)) |
| Country-by-country report group threshold | consolidated revenue above EUR 750,000,000 in the prior year | 2026 | https://lex.bg/laws/ldoc/2135514513 (DOPK Art. 143kh(6)) |
| Interquartile range, adjustment point | first to third quartile; adjust to the median when no point fits better | 2026 | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=238785 (Ordinance N-3 Arts. 20(6), 21(2)) |
| Withholding tax on dividends, including hidden profit distribution, paid to foreign companies | 5% | 2026 | https://lex.bg/laws/ldoc/2135540562 (ZKPO Arts. 194, 200(1), para. 1 item 4) |

## The taxable base

**The rule.** Where related parties deal on terms that differ from those between unrelated parties and the difference affects the tax base, the base is set and taxed on the terms unrelated parties would have agreed (ZKPO Article 15). A market price is the price that would be agreed in a deal on comparable terms between independent persons in comparable circumstances (DOPK para. 1, item 8, as amended from 1 January 2026).

**Methods (DOPK para. 1, item 10; Ordinance N-3, Article 1).** Comparable uncontrolled price, resale price, cost plus, transactional net margin and transactional profit split. Since 2026 a taxpayer may use another method if none of the five is suitable and the other method gives a more reliable result (Ordinance N-3, Article 14(8)). The most appropriate method is chosen on the facts (Article 14(2) and (3)). On a tie, comparable uncontrolled price beats the others, and a traditional method beats a profit method (Article 14(5)). Ordinance N-3 is to be read in line with the OECD Transfer Pricing Guidelines (Ordinance N-3, para. 2). The NRA says its old Transfer Pricing Manual still applies only where it does not contradict the new rules.

**Accurate delineation first.** The analysis has two stages: describe the actual transaction by its economic substance, then compare it with uncontrolled deals (Ordinance N-3, Article 3). Where the contract is missing, unclear or not followed, conduct decides (Article 5(2)). A party that assumes a risk by contract but does not control it, or lacks the financial capacity to bear it, is treated as not bearing it; the risk is allocated to the related party that controls it and can bear it (Article 8(5)).

**Range and adjustment (Ordinance N-3, Articles 20 and 21).**
- Two or more comparables form a range. When comparability defects remain, the range is narrowed, for example to the interquartile range (first to third quartile) (Article 20(4) to (6)).
- A result inside the range is arm's length (Article 21(1)).
- A result outside the range is moved to the point that best fits the facts. If no such point can be identified, it goes to the arithmetic mean (fully reliable range), the median (interquartile range) or another measure of central tendency (Article 21(2)). Multi-year analyses compare averages (Article 21(3)).

**Services (Ordinance N-3, Articles 44 to 48).** An intra-group service charge is deductible only if the service gives a real or reasonably expected benefit and the price matches what an independent party would pay. Shareholder activity, duplicated services and incidental benefits from group membership fail the test (Article 44(2)). Indirect allocation needs a key tied to benefit, not to controlled terms, and applied consistently (Article 47).

**Financial transactions (Ordinance N-3, Articles 53 and 54).** A related-party loan can be recharacterised in whole or part after a full analysis (Article 53(2)). The debtor's credit rating drives the rate. The parent's consolidated rating may be used in limited cases (Article 54(3)). A bank "comfort letter" on a loan that was never made is not a reliable rating (Article 54(4)). Interest-free loans and loans at off-market rates are also listed as tax evasion in ZKPO Article 16(2)(3), and Article 16 applies even between unrelated parties.

**Hidden profit distribution.** Amounts unrelated to the business, or above normal market levels, accrued, paid or distributed in any form to shareholders, partners or persons related to them are a hidden profit distribution (ZKPO para. 1, item 5(a)). Interest on a loan that meets three of four equity-like tests (loan above equity, no fixed term, payment tied to profit, subordinated) is also a hidden distribution (item 5(b)). Such expenses are not deductible (ZKPO Article 26, item 11). A hidden distribution is a dividend (para. 1, item 4(c)), so 5% withholding tax applies when the recipient is a foreign company (Articles 194(1), item 1, and 200(1)). A non-resident individual shareholder is taxed under the Personal Income Tax Act, which this skill does not cover. The EU and EEA parent exemption does not cover a hidden distribution (Article 194(3), item 3).

**Burden of proof.** A taxpayer dealing with related parties must prove the market price and any reason for departing from it, including with evidence from abroad (DOPK Article 116(2)). If it does not, the revenue officer sets the market price from available information (Article 116(4)), including exchange prices and statistical sources (Article 116(5)). The officer takes the taxpayer's own analysis into account only if it was presented in time and covers the points in Ordinance N-3, Article 55.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Annual CIT return (with the annual activity report) | 1 March to 30 June of the following year | ZKPO Art. 92(2) and (3) |
| Local file prepared | by 30 June of the following year (the NRA transfer pricing page still says 31 March; the law has said 30 June since State Gazette 104/2020, in force 1 January 2021, and the law governs) | DOPK Art. 71d(1) |
| Local file updated after a corrective return under ZKPO Art. 75(3) | within 14 days of the corrective return, and no later than 30 September | DOPK Art. 71d(2) |
| Master file available (for the ultimate parent's year starting on or after 1 January of the local file year) | within 12 months after the local file deadline | DOPK Art. 71d(3) |
| Documentation produced to the NRA | on request during a tax audit, within the period the officer sets | DOPK Arts. 71e(1), 278a(5) |
| CbC notification (who files the report) | by the last day of the group's reporting year | DOPK Art. 143sh |
| CbC report | within 12 months of the end of the group's reporting year | DOPK Art. 143f(1) |

- The local file and the master file are not filed. They are kept and handed over on request (DOPK Article 71e(1)). Both are prepared every year (Article 71e(2)).
- **Local file thresholds are per transaction (Article 71b(6)).** Comparable transactions that can be tested with one method are added together (Article 71b(7)). Transactions with one party that cannot be separated are added together, and the threshold of the largest part applies (Article 71b(8)). A local file is needed only for the transactions over the threshold (Article 71b(9)).
- **Local file content (Article 71v).** Management structure and owners; business and strategy; each controlled transaction with its value, contracts, functional and comparability analysis, method and tested party; comparables and adjustments; allocation keys; APAs and rulings issued abroad; the financial statements reconciled to the analysis.
- **Master file (Article 71g).** Group structure, value chain for the top five products and any above 5% of group revenue, transfer pricing policy, main service agreements, intangibles, financing and the consolidated accounts. A group member that must prepare a local file must also *have* a master file, prepared by the ultimate parent or another group member (Article 71b(10)).
- **Language and format.** Not yet confirmed. The DOPK text read does not state a language for the local file.
- **Country-by-country reporting.** A Bulgarian ultimate parent of a group with consolidated revenue above EUR 750,000,000 in the prior year files the CbC report (Articles 143kh(1), (2) and (6)). A Bulgarian group member files in place of a foreign parent when the parent's state does not require a report, has no qualifying exchange agreement, or is in systemic failure (Article 143ts(1)). Every Bulgarian group member files the Article 143sh notification. The NRA uses CbC data for risk assessment only and cannot set market prices from it (Article 143shch(2)).
- **Advance pricing agreements.** Bulgaria has no APA procedure. Para. 59(5) of the transitional provisions of the DOPK amending act (State Gazette 63/2017) says the NRA only receives APA information from other member states "until there is a legal basis" to issue APAs.
- **Disputes.** The EU tax dispute resolution procedure (Directive 2017/1852) is in DOPK Articles 134a onwards, with the Minister of Finance as competent authority (Article 134b(3)). Treaty mutual agreement procedures follow the treaty.

## Penalties and interest

| Breach | Penalty (leva in the law; euro at the fixed rate) | Source |
|---|---|---|
| No local file, or not produced on request in time | up to 0.5% of the total value of the transactions it should have covered; for a loan, the value is the principal | DOPK Art. 278a(5) |
| No master file when required | BGN 5,000 to 10,000 = EUR 2,556.46 to 5,112.92 | DOPK Art. 278a(6) |
| False or incomplete data in the documentation | BGN 1,500 to 5,000 = EUR 766.94 to 2,556.46 | DOPK Art. 278a(7) |
| Repeat breach of the three above | double | DOPK Art. 278a(8) |
| CbC report not filed in time | BGN 100,000 to 200,000 = EUR 51,129.19 to 102,258.38 (repeat BGN 200,000 to 300,000 = EUR 102,258.38 to 153,387.56) | DOPK Art. 278a(1) |
| CbC report with false or incomplete data | BGN 50,000 to 150,000 = EUR 25,564.59 to 76,693.78 (repeat BGN 100,000 to 250,000 = EUR 51,129.19 to 127,822.97) | DOPK Art. 278a(2) |
| Notification under Art. 143ts(2) or 143ch(5) missing | BGN 10,000 = EUR 5,112.92 (repeat BGN 15,000 = EUR 7,669.38) | DOPK Art. 278a(3) |
| CbC notification under Art. 143sh missing | BGN 50,000 to 150,000 = EUR 25,564.59 to 76,693.78 (repeat BGN 100,000 to 200,000 = EUR 51,129.19 to 102,258.38) | DOPK Art. 278a(4) |
| Hidden profit distribution not shown in the CIT return | 20% of the hidden distribution | ZKPO Art. 267 |
| Return understating tax | BGN 500 to 3,000 = EUR 255.65 to 1,533.88 (repeat BGN 1,000 to 6,000 = EUR 511.29 to 3,067.75) | ZKPO Art. 261 |

- **Additional tax.** An adjustment adds 10% CIT on the increase in the base (ZKPO Article 20).
- **Late-payment interest.** Unpaid tax carries statutory interest. From 1 January 2026 the annual rate is the ECB main refinancing rate in force on 1 January or 1 July, plus 8 percentage points (Council of Ministers Decree 347 of 29 December 2025, State Gazette 115/2025, amending Decree 426 of 2014, as stated by the NRA). Until 31 December 2025 the rate was the BNB base rate plus 10 points. No interest runs on interest or on fines.
- **Time limit.** No assessment proceeding can start after 5 years from the end of the year in which the return was filed or due (DOPK Article 109(1)). Public receivables expire after 5 years from 1 January of the year after payment fell due (DOPK Article 171(1)).

## Cross-border points

- **Documentation is cross-border only.** A company whose controlled transactions are all with Bulgarian parties has no local file duty (DOPK Article 71b(2)(4)), though Article 15 still applies to it.
- **Hidden distributions to foreign corporate shareholders** are dividends and bear 5% withholding tax (ZKPO Articles 194 and 200(1)). The EU and EEA exemption does not apply to them (Article 194(3), item 3). A treaty can lower the rate; check the treaty for the shareholder's state. Withholding on interest, royalties and fees is in bg-corporate-income-tax.
- **Low-tax counterparties.** A foreign party in a non-EU state whose tax is more than 60% below Bulgarian tax, and which does not exchange information, is related to the Bulgarian party whatever the ownership (DOPK para. 1, item 3(n)).
- **Corresponding adjustments.** The DOPK text read has no rule for a unilateral downward adjustment in Bulgaria after a foreign upward adjustment. Relief runs through the treaty MAP or the EU dispute procedure (DOPK Articles 134a onwards).
- **Permanent establishments.** Transfers between a Bulgarian branch and its head office are priced and documented as controlled transactions (DOPK Article 71zh(1)).

## Worked examples

### Example 1: Does a Bulgarian subsidiary need a local file in 2026, and what is the maximum fine?

A Bulgarian EOOD is 100% owned by a German GmbH. At 31 December 2025 it had assets of EUR 25,000,000, net revenue of EUR 45,000,000 and 180 staff. Two of the three size tests are exceeded, so it is not exempt (DOPK Article 71b(2)(3)). In 2026 it sells goods to the parent for EUR 3,000,000, buys management services from it for EUR 90,000, and borrows EUR 600,000 from it at 6%, paying EUR 36,000 interest.

Convert the leva thresholds: goods BGN 400,000 / 1.95583 = EUR 204,516.75; other BGN 200,000 / 1.95583 = EUR 102,258.38; loan principal BGN 1,000,000 / 1.95583 = EUR 511,291.88. Goods (EUR 3,000,000) and the loan (EUR 600,000) are over their thresholds and need a local file. The services (EUR 90,000) are under EUR 102,258.38 and need none (Article 71b(9)), though they must still be at arm's length and the benefit test in Ordinance N-3 Article 44 still applies. The interest, EUR 36,000, is also over the EUR 25,564.59 interest threshold, but the loan is already in. The local file is due by 30 June 2027. If it is not produced on request, the fine is up to 0.5% of EUR 3,600,000, which is EUR 18,000 (DOPK Article 278a(5)).

```oa-check
name: Example 1, local file thresholds in euro and maximum Art. 278a(5) fine
inputs:
  rate: 1.95583
  goods_sales: 3000000
  services: 90000
  loan: 600000
  interest: 36000
steps:
  - goods_threshold: round(400000 / rate, 2)
  - other_threshold: round(200000 / rate, 2)
  - loan_threshold: round(1000000 / rate, 2)
  - interest_threshold: round(50000 / rate, 2)
  - goods_margin: goods_sales - goods_threshold
  - services_margin: services - other_threshold
  - loan_margin: loan - loan_threshold
  - documented_value: goods_sales + loan
  - max_fine: documented_value * 0.5 / 100
expected:
  goods_threshold: 204516.75
  other_threshold: 102258.38
  loan_threshold: 511291.88
  interest_threshold: 25564.59
  goods_margin: 2795483.25
  services_margin: -12258.38
  loan_margin: 88708.12
  documented_value: 3600000
  max_fine: 18000
```

### Example 2: Contract manufacturer below the interquartile range

A Bulgarian contract manufacturer sells its whole output to its Austrian parent. Its 2026 total costs are EUR 10,000,000 and its operating profit is EUR 200,000, a net cost plus of 2%. The tested party is the Bulgarian company and the method is TNMM. A benchmark of independent manufacturers gives an interquartile range of 4.0% to 8.5% with a median of 6.0%. The 2% result is outside the range. No point in the range fits the facts better, so the result is moved to the median (Ordinance N-3, Article 21(2)(2)). Arm's length profit is EUR 600,000 (10,000,000 x 6%). The base rises by EUR 400,000 and the extra CIT at 10% is EUR 40,000 (ZKPO Articles 15 and 20). Late-payment interest runs from the CIT due date. Whether underpriced sales to the parent are also a hidden profit distribution (with 5% withholding and the 20% Article 267 sanction) is not yet confirmed; see the end of this skill.

```oa-check
name: Example 2, TNMM net cost plus 2% adjusted to the 6% median
inputs:
  total_costs: 10000000
  operating_profit: 200000
  q1: 4.0
  median: 6.0
  q3: 8.5
steps:
  - ncp_pct: operating_profit / total_costs * 100
  - below_q1: q1 - ncp_pct
  - arm_length_profit: total_costs * median / 100
  - adjustment: arm_length_profit - operating_profit
  - extra_cit: adjustment * 0.10
expected:
  ncp_pct: 2.0
  below_q1: 2.0
  arm_length_profit: 600000
  adjustment: 400000
  extra_cit: 40000
```

## Ask the client first

1. Who holds 5% or more, and 25% or more, of the voting shares, and who controls the company? Any family or management links to other companies? Any counterparty in a low-tax non-EU state?
2. At 31 December 2025: balance sheet assets, net sales revenue and average staff. This decides whether a local file is needed at all.
3. List each foreign related party and the 2026 value of each transaction type: goods, services, royalties, loans (principal and interest). Are any transactions comparable enough to be added together?
4. For related-party loans: principal, rate, term, security, and how the rate was set. Is there a credit rating for the Bulgarian borrower?
5. Is the group's consolidated revenue above EUR 750,000,000? Who files the CbC report, and has the Article 143sh notification been made?
6. Does the group have a master file and a benchmark study, and when were the comparables last searched?

## Sources

| Source | URL | Read on |
|---|---|---|
| lex.bg: Corporate Income Tax Act (ZKPO), consolidated to State Gazette 55/2026, Arts. 15, 16, 20, 26, 43, 43a, 92, 194, 200, 261, 262, 267, para. 1 items 4 and 5 | https://lex.bg/laws/ldoc/2135540562 | 2026-10-23 |
| lex.bg: Tax-Insurance Procedure Code (DOPK), consolidated to State Gazette 85/2026, Arts. 71a to 71zh, 109, 116, 134a, 134b, 143u to 143shch, 171, 175, 278a, Additional Provisions para. 1 items 3, 4, 8, 10, para. 59 of the transitional provisions to the State Gazette 63/2017 amending act | https://lex.bg/laws/ldoc/2135514513 | 2026-10-23 |
| State Gazette 96/2025: Ordinance N-3 of 7 November 2025 on the market price methods (in force 1 January 2026) | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=238785 | 2026-10-23 |
| State Gazette 70/2024: Euro Introduction Act, Arts. 11 to 13 and para. 34 (DOPK amounts in euro) | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=224950 | 2026-10-23 |
| NRA: Transfer pricing | https://nra.bg/wps/portal/nra/mezhdunarodni-deinosti/transferno-tzenoobrazuvane | 2026-10-23 |
| NRA: Overdue liabilities (statutory interest from 2026) | https://nra.bg/wps/portal/nra/delayed.payments | 2026-10-23 |

Leva amounts: the Euro Introduction Act (para. 34) restated in euro only the DOPK Article 71b(2), item 3 size tests and the CbC thresholds. The Article 71b(5) transaction thresholds and the Article 278a penalties are still printed in leva and are read as euro at BGN 1.95583, rounded to the cent (Euro Introduction Act, Articles 11(2), 12 and 13).

Not yet confirmed: whether underpricing of sales to a shareholder (not only overpayments) counts as a hidden profit distribution under ZKPO para. 1, item 5(a); the required language of the local file; whether the annual CIT return has a related-party disclosure schedule; the text of Council of Ministers Decree 347/2025 itself (the interest formula is taken from the NRA overdue liabilities page); whether the old NRA Transfer Pricing Manual will be reissued under Ordinance N-3.

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
