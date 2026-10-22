---
name: be-transfer-pricing
description: "Belgian transfer pricing (verrekenprijzen / prix de transfert) for income year 2026 (assessment year 2027): Belgian companies and Belgian establishments of foreign companies that deal with associated enterprises abroad. Covers the arm's length rule in art. 185, § 2 WIB 92 (upward and downward adjustments), abnormal or gratuitous advantages (art. 26, 79 and 206/3), the BEPS 13 documentation duties in art. 321/1 to 321/7 (master file 275 MF, local file 275 LF, country-by-country report 275 CBC, notification 275 CBC NOT), the EUR 50m / EUR 1bn / 100 FTE and EUR 1m thresholds, the EUR 750m CbC threshold, the art. 445, § 3 fine scale, rulings and APAs, MAP, the EU Arbitration Convention and the law of 2 May 2019. Trigger on: verrekenprijzen, prix de transfert, arm's length Belgium, 185 § 2, abnormaal voordeel, avantage anormal, groepsdossier, lokaal dossier, landenrapport, 275 LF, 275 MF, 275 CBC, BEPS 13, Ruling Commission, DVB, SDA, APA Belgium. Out of scope: be-corporate-tax (rates, base, filing), be-cross-border, belgium-payroll."
jurisdiction: BE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Belgian transfer pricing (verrekenprijzen): income year 2026

What changed for 2026: no change to the arm's length rule, the documentation thresholds or the fine scale. Two smaller points are new:

- **Amount B.** Circular 2026/C/45 of 19 March 2026 adds the OECD "Amount B" simplified approach for routine distributors to the Belgian transfer pricing guidance. Belgium does not apply it to its own distributors. It accepts the result where a "covered jurisdiction" that has a tax treaty with Belgium applies it to its resident distributor. It applies to transactions from 1 January 2025 ([circular 2026/C/45](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/bdba1312-92d8-435b-8aa9-266c65626260)).
- **Tax ID in the CbC report.** For taxable periods starting on or after 1 January 2028, the country-by-country report must show taxpayers' tax identification numbers ([art. 321/2, § 4/1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/45e1ce54-89f9-4356-badf-2fcfebbc7fb1), inserted by the law of 16 March 2026). It does not affect 2026.

The corporate tax rates, the taxable base and Biztax filing are in `be-corporate-tax`. This skill covers pricing between associated enterprises and the documentation that supports it.

## Who this applies to

- **Arm's length rule (art. 185, § 2).** It applies to two companies in a multinational group of associated companies, for their cross-border dealings with each other ([art. 185, § 2](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/bf1f6e00-f321-4a51-835c-967f4c019b83)).
  - **Upward adjustment (§ 2, a).** If the two companies agree or impose terms in their commercial or financial relations that differ from terms independent companies would agree, the profit the Belgian company would have made without those terms is added to its profit.
  - **Downward adjustment (§ 2, b).** If the Belgian company's profit includes profit that was also included, and already taxed, in the profit of the other company in a treaty state, and that profit is what the other company would have made on arm's length terms, the Belgian profit is "appropriately revised". A treaty state and prior taxation there are both conditions in the text.
- **Abnormal or gratuitous advantages granted (art. 26).** A company established in Belgium that grants abnormal or gratuitous advantages adds them to its own profit, unless they are taxed in the hands of the recipient. They are always added back when the recipient is ([art. 26](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9e236a9-9b1f-447a-8eae-4e50feaf83d1)):
  1. a non-resident (art. 227) with which the Belgian company has any direct or indirect link of interdependence;
  2. a non-resident or foreign establishment not subject to income tax, or subject to a much more favourable regime, where it is established; or
  3. a non-resident with interests in common with one of those.
  Art. 26 also reaches domestic dealings and dealings outside a group, which art. 185, § 2 does not.
- **Abnormal or gratuitous advantages received (art. 79 and art. 206/3).** Losses cannot be set against the part of the profit that comes from abnormal or gratuitous advantages received from an interdependent enterprise ([art. 79](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/836dcd26-5c68-4b5c-a6a1-057dab115af1)). For companies, art. 206/3, § 1 makes that part a minimum taxable base: no current-year loss, carried-forward loss or other deduction may be set against it ([art. 206/3](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1e2ab543-c40d-41fa-8081-591ae036e18e)). This rule used to sit in art. 207; art. 207 now only sets the order of deductions and the basket.
- **Documentation (art. 321/1 to 321/7).** Applies to a "Belgian group entity": an entity of a multinational group that is tax resident in Belgium, including a Belgian establishment for which separate accounts are kept ([art. 321/1, 4° and 6°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/580b569b-f7b1-4737-b66e-6294b7b596ac)). A multinational group has entities in two or more jurisdictions, or one entity with a permanent establishment in another jurisdiction. A group made only of Belgian companies with no foreign entity or establishment is not a multinational group. Once a Belgian group entity passes the thresholds, 275 MF and 275 LF are due ([circular 2020/C/88, FAQ 1.08](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ea99e5c1-8ab9-4ebd-8a4e-d3229a1585ef)).
- **Belgian establishments exempt under a treaty** file no master file and no local file, but still file the 275 CBC NOT notification where it applies (circular 2020/C/88, FAQ 4.03, c).
- **Out of scope here:** individuals (`be-income-tax`), the corporate rates and base (`be-corporate-tax`), and the payments to low-tax recipients that art. 54 denies as expenses unless the payer proves a genuine transaction (see `be-corporate-tax`).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate tax on a primary adjustment | 25% standard rate; 20% on the first EUR 100,000 for small companies that meet the art. 215 conditions | Income 2026 (AY 2027) | [art. 215](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1) |
| Master file (275 MF) and local file (275 LF): entity thresholds | Due if the Belgian group entity exceeded ANY ONE of these in the financial year immediately before the last closed financial year, per its own annual accounts: operating and financial revenue of EUR 50,000,000 excluding non-recurring revenue; balance sheet total of EUR 1,000,000,000; annual average of 100 full-time equivalents | 2026 (unchanged since 2016) | [art. 321/4, § 3](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a411e50a-13b6-4ffc-951e-d8f9a12615af); [art. 321/5, § 3](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/efcb1b25-7a0e-4af5-acc8-fd875f85f8d9) |
| Local file part B (transfer pricing analysis) | Only for each business unit with more than EUR 1,000,000 of cross-border transactions with group entities in the last closed financial year | 2026 | [art. 321/5, § 3, second paragraph](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/efcb1b25-7a0e-4af5-acc8-fd875f85f8d9) |
| How the EUR 1m is counted | Goods + services + financial transactions (interest, not loan principal) + other transactions with foreign group entities; transactions between Belgian group entities are left out | 2026 | [circular 2020/C/88, FAQ 2.02](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ea99e5c1-8ab9-4ebd-8a4e-d3229a1585ef) |
| Short or long financial year | Revenue is prorated to 12 months (each month started counts as a full month); balance sheet total and FTE are not prorated | 2026 | [circular 2020/C/88, FAQ 1.04](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ea99e5c1-8ab9-4ebd-8a4e-d3229a1585ef); [circular 2017/C/56, no. 29](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d36905c4-a9dc-48ba-9565-d9ca86df5082) |
| FTE figure used | Code 1003 of the statutory accounts filed with the National Bank | 2026 | [circular 2020/C/88, FAQ 2.03](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ea99e5c1-8ab9-4ebd-8a4e-d3229a1585ef) |
| Country-by-country report (275 CBC) | Groups with consolidated group revenue of EUR 750,000,000 or more in the reporting period immediately before the last closed reporting period. Unlike the MF/LF test, non-recurring revenue counts | 2026 | [art. 321/2, § 4](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/45e1ce54-89f9-4356-badf-2fcfebbc7fb1); [circular 2020/C/88, FAQ 2.04](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ea99e5c1-8ab9-4ebd-8a4e-d3229a1585ef) |
| CbC notification (275 CBC NOT) | Every Belgian group entity of a group above EUR 750m: say whether it is the ultimate parent, surrogate parent or a filing group entity, or name the reporting entity; only when the information changed from the previous period | 2026 | [art. 321/3](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c31d4a6b-5a15-4d3e-b5d0-56329a4bf16f) |
| Fine for documentation breaches, good faith | 1st: nil. 2nd: EUR 1,250. 3rd: EUR 6,250. 4th: EUR 12,500. Later: EUR 25,000. Breach outside the taxpayer's control: nil | Since 19 July 2018; 2026 text unchanged | [art. 445, § 3](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f); [KB/WIB 92 art. 229/5 (income 2026)](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/184c431f-6fb7-46d2-b2fd-4bce1186ec0b) |
| Fine for documentation breaches, bad faith or intent to evade | 1st: EUR 12,500. Later: EUR 25,000 | Since 8 January 2018 | [art. 445, § 3](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f); [KB/WIB 92 art. 229/5](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/184c431f-6fb7-46d2-b2fd-4bce1186ec0b) |
| Tax increase on undeclared income | 10% to 200% of the tax on the undeclared part, on a royal decree scale; none for a first offence in good faith; only when the undeclared income reaches EUR 2,500 | 2026 | [art. 444](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0) |
| Ruling (advance decision) | Answer within three months of a complete request (can be changed by agreement); valid for at most five years unless the subject justifies longer | 2026 | [law of 24 December 2002, art. 21 and 23](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/b1f37aaf-8af5-4f0c-84c9-ee3b3ee33d48) |

## The taxable base

1. **Start from the accounts, then test each controlled transaction.** Belgium follows the OECD Transfer Pricing Guidelines (2017) and accepts later changes to them ([circular 2020/C/35, introduction](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/79654895-7b25-40f7-8879-00a72e39ea85)). The question is whether the Belgian company paid too much or charged too little for goods, services, intangibles or financing.
2. **Method.** Pick the most appropriate method (CUP, resale price, cost plus, TNMM, profit split). The taxpayer need not run every method or explain why it rejected the others (circular 2020/C/35, no. 25). For a one-sided method, the tested party is usually the one with the least complex functions (no. 24).
3. **Range.** The administration prefers the interquartile range. A result inside it is accepted. Outside it, without a reasoned explanation, the result is adjusted to the point in the range that best fits the facts, and to the median if no such point can be found (circular 2020/C/35, nos. 125 and 126). The full range can be used only where the comparables are very good.
4. **Primary adjustment, upward.** The excess paid or the shortfall charged is added to the Belgian taxable profit under art. 185, § 2, a, or art. 26. Tax at the art. 215 rate.
5. **Received advantages.** Where the Belgian company received an abnormal or gratuitous advantage from an interdependent enterprise, that part of its profit is a minimum base: no losses or deductions against it (art. 79; art. 206/3, § 1). The same applies to the part of the result corrected by an amended or ex officio assessment where a tax increase of 10% or more is actually applied (art. 206/3, § 1, second paragraph).
6. **Downward adjustment.** Profit revised downward under art. 185, § 2, b, is taken out of the reserves when the taxable result is built up ([art. 206/1, first paragraph, 1°, p)](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/9fc0360b-c34b-4f33-aec5-e3d6b8418130)). The text of art. 185, § 2, b, does not itself require a ruling. A company that wants certainty before filing can ask the Ruling Service (Dienst Voorafgaande Beslissingen / Service des Décisions Anticipées) for an advance decision under the law of 24 December 2002 (art. 20 to 23). A ruling cannot grant an exemption or a reduction of tax (art. 20) and cannot be given where the situation has no economic substance in Belgium (art. 22).
7. **Corresponding adjustment after a foreign audit.** If a foreign tax administration adjusts and the adjustment is correct and well founded, the Belgian administration makes a corresponding adjustment to avoid double tax (circular 2020/C/35, no. 163). Relief of tax overpaid after a MAP, an Arbitration Convention procedure or a procedure under the law of 2 May 2019 is granted ex officio ([art. 376, § 3, 3°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/922814f1-9e8e-40bc-8165-43a67830e65f)).
8. **APAs.** Unilateral certainty comes from a ruling. Bilateral and multilateral advance pricing arrangements are agreed with the other state's administration; the Belgian competent authority handles MAP and APA requests at map.apa@minfin.fed.be ([circular 2018/C/27](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/9a511b78-6594-4df5-92ec-e35d8b488b5f)).
9. **The CbC report is not a basis for an adjustment on its own.** It may start an audit, but adjustments may not be based only on it ([art. 321/6](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/dc69dbd0-73d6-4eae-88ae-152ae44d4037)).

## Deadlines and filing

| Filing | Who | Deadline | Channel | Source |
|---|---|---|---|---|
| 275 LF, local file | Belgian group entity above the MF/LF thresholds | With the corporate tax return (VenB) or non-resident companies return (BNI/ven) for the same financial year; it is part of the return | Electronically, MyMinfin | [art. 321/5, § 1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/efcb1b25-7a0e-4af5-acc8-fd875f85f8d9); [circular 2017/C/56, no. 37](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d36905c4-a9dc-48ba-9565-d9ca86df5082) |
| 275 MF, master file | Belgian group entity above the MF/LF thresholds | Within 12 months after the last day of the group's reporting period | MyMinfin | [art. 321/4, § 1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a411e50a-13b6-4ffc-951e-d8f9a12615af); [circular 2020/C/88, FAQ 1.07 and 6.07](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ea99e5c1-8ab9-4ebd-8a4e-d3229a1585ef) |
| 275 CBC, country-by-country report | Belgian ultimate parent; or a Belgian group entity when the parent's state does not require a report, has no qualifying exchange agreement with Belgium in force, or has systemically failed to exchange | Within 12 months after the last day of the reporting period | MyMinfin, XML format | [art. 321/2, § 1 and § 2](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/45e1ce54-89f9-4356-badf-2fcfebbc7fb1); [circular 2017/C/56](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d36905c4-a9dc-48ba-9565-d9ca86df5082) |
| 275 CBC NOT, notification | Every Belgian group entity of a group above EUR 750m | By the last day of the group's reporting period, only if the information differs from the previous period | MyMinfin | [art. 321/3](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c31d4a6b-5a15-4d3e-b5d0-56329a4bf16f) |

- For a calendar-year group, the 2026 master file and CbC report are due by **31 December 2027**. The local file for income 2026 follows the AY 2027 return deadline, which was not yet published on 22 October 2026 (see `be-corporate-tax`).
- The deadlines for the master file, CbC report and notification follow the group's reporting period, not the Belgian entity's own year (circular 2020/C/88, FAQ 1.07).
- The forms can be completed in English as well as Dutch, French or German ([art. 321/7](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a6005852-ca6d-4d8b-9c58-161e4c2e122d)).
- A missing local file lets the administration assess ex officio under art. 351 (circular 2017/C/56, no. 37).
- **Ruling requests** go in writing, with reasons, to FOD Financiën before the transaction has had tax effect ([law of 24 December 2002, art. 20 and 21](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/b1f37aaf-8af5-4f0c-84c9-ee3b3ee33d48)).

## Penalties and interest

- **Documentation fines (art. 445, § 3 and KB/WIB 92 art. 229/5).** They cover a 275 CBC, MF, LF or CBC NOT that is not filed, filed late, incomplete or wrong ([circular 2019/C/14](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d747344b-6161-489d-93d6-0377665ea5f9)). Good faith: first breach nil, then EUR 1,250, EUR 6,250, EUR 12,500 and EUR 25,000. Bad faith or intent to evade: EUR 12,500, then EUR 25,000. A breach caused by circumstances outside the taxpayer's control: nil, and it does not count.
- **How breaches are counted.** All breaches of art. 321/1 to 321/6 in the same category (good faith, bad faith) count together. A new breach is a "second" breach only if the company had already received a fine notice for the earlier one when it committed the new one (circular 2019/C/14, part 3.C.b). The date of the breach is the filing deadline for a missing or late form, and the filing date for an incomplete or wrong one; for the local file, it is the return deadline (part 5.A).
- **Tax increase.** An upward adjustment that was not declared carries a tax increase of 10% to 200% of the tax on it, none for a first good-faith offence, and only from EUR 2,500 of undeclared income ([art. 444](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0)). If an increase of 10% or more is actually applied, the corrected part of the result cannot be absorbed by losses (art. 206/3, § 1, second paragraph).
- **General fine.** Other breaches of the Code: EUR 50 to EUR 1,250 ([art. 445, § 1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f)).
- **Late payment interest** on the extra tax follows the general rules in `be-corporate-tax` (art. 414).

## Cross-border points

- **Mutual agreement procedure (MAP) under a treaty.** Most Belgian treaties follow art. 25(1) of the OECD Model: the case must be presented within three years of the first notification of the action causing taxation not in line with the treaty. In Belgium the three years run from receipt of the assessment notice, not from a notice of adjustment (art. 346) or of ex officio assessment (art. 351). Requests are made in writing, by post, e-mail or hand delivery ([circular 2018/C/27, nos. 34, 38 to 41](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/9a511b78-6594-4df5-92ec-e35d8b488b5f)). Where the treaty has an arbitration clause, issues unresolved after two years can go to arbitration (no. 67).
- **EU Arbitration Convention (90/436/EEC).** For profit adjustments between associated enterprises in EU member states. The case must be presented within three years of the first notification of the action that leads or will lead to double taxation (art. 6(1)), counted from the second of the two states' actions; in Belgium that is receipt of the assessment notice (circular 2018/C/27, no. 39).
- **EU Dispute Resolution Directive 2017/1852, law of 2 May 2019.** For complaints filed from 1 July 2019 on income of taxable periods starting on or after 1 January 2018. The complaint is filed within three years of the first notification of the action giving rise to the dispute. The Belgian competent authority decides on acceptance within six months (silence counts as acceptance). The authorities then have two years to agree, extendable by one year, before an advisory commission can be set up ([law of 2 May 2019, art. 3, 4, 5 and 26](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/fe0e1a5c-4abe-44f6-a27b-3dcd90f7a4c8)).
- **Amount B.** Belgium accepts the Amount B return when a covered jurisdiction with a treaty with Belgium applies it to its own distributor, and can use it in a MAP or arbitration case with such a jurisdiction. It does not apply Amount B to Belgian distributors or to purely Belgian transactions ([circular 2026/C/45](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/bdba1312-92d8-435b-8aa9-266c65626260)).
- **Exchange of CbC reports.** Belgium exchanges CbC reports with EU member states under Directive 2011/16/EU as amended by Directive 2016/881, and with other states under qualifying competent authority agreements ([circular 2017/C/56, nos. 21 and 22](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d36905c4-a9dc-48ba-9565-d9ca86df5082)).
- **Withholding tax, CFC and exit tax** are in `be-corporate-tax` and `be-cross-border`. An excessive intra-group payment can raise questions beyond transfer pricing (deemed distribution, withholding); this skill does not decide them.

## Worked examples

### Example 1: excessive royalty to a foreign parent, art. 185, § 2 primary adjustment

A Belgian BV, wholly owned by its Dutch parent, distributes the group's products in Belgium. In 2026 it had sales of EUR 10,000,000 and paid the parent a trademark royalty of 8% of sales. A benchmark of comparable licences supports 5% at most (the top of the interquartile range). The BV is 100% owned by a company, so it cannot use the 20% rate (art. 215, third paragraph, 2°); 25% applies to the adjustment. Its profit is otherwise fully taxed and it has no losses.

1. Royalty paid: 10,000,000 x 8% = EUR 800,000.
2. Arm's length royalty: 10,000,000 x 5% = EUR 500,000.
3. Upward adjustment under art. 185, § 2, a (art. 26 reaches the same amount; the excess is added once): EUR 300,000.
4. Extra corporate tax: 300,000 x 25% = EUR 75,000.
5. If the administration finds the adjustment in an audit and applies a 10% tax increase (no increase for a first good-faith offence): 75,000 x 10% = EUR 7,500, total EUR 82,500. With an increase of 10% or more, the EUR 300,000 also could not have been absorbed by losses (art. 206/3).
6. To avoid double tax, the group asks the Netherlands for a corresponding adjustment, or files a MAP or a complaint under the law of 2 May 2019 within three years of receiving the Belgian assessment notice.

```oa-check
name: Belgian BV, royalty 8% vs arm's length 5% on sales EUR 10m, income 2026
inputs:
  sales: 10000000
  royalty_rate_paid: 0.08
  royalty_rate_arm: 0.05
  cit_rate: 0.25
  increase_rate: 0.10
steps:
  - royalty_paid: sales * royalty_rate_paid
  - royalty_arm: sales * royalty_rate_arm
  - adjustment: royalty_paid - royalty_arm
  - extra_tax: adjustment * cit_rate
  - tax_increase: extra_tax * increase_rate
  - total_cost: extra_tax + tax_increase
expected:
  royalty_paid: 800000
  royalty_arm: 500000
  adjustment: 300000
  extra_tax: 75000
  tax_increase: 7500
  total_cost: 82500
```

### Example 2: does a Belgian subsidiary with a short year pass the MF/LF thresholds?

A Belgian NV belongs to a group with consolidated revenue of EUR 600,000,000, so there is no CbC report or 275 CBC NOT. Its 2025 financial year was short: 1 April to 31 December 2025 (nine months). Its 2025 accounts show operating and financial revenue of EUR 40,000,000 excluding non-recurring revenue, plus EUR 3,000,000 of non-recurring revenue, a balance sheet total of EUR 35,000,000 and an average of 80 FTE. The question is whether a master file and a local file are due for calendar 2026, the last closed financial year when the AY 2027 return is filed. The test looks at the year before that: 2025.

1. Non-recurring revenue is left out of the MF/LF test (art. 321/4, § 3; FAQ 2.04): revenue EUR 40,000,000.
2. Prorate to 12 months because the year was nine months: 40,000,000 / 9 x 12 = EUR 53,333,333.33. This is above EUR 50,000,000, so the test is met on revenue alone. The balance sheet (EUR 35m) and FTE (80) are not prorated and are below their limits, but one criterion is enough.
3. Result: 275 LF with the 2026 return, and 275 MF within 12 months after the group's 2026 reporting period ends.
4. Part B of the local file: the NV's single business unit bought goods of EUR 600,000 from a French sister company and earned EUR 100,000 interest on a EUR 2,000,000 loan to a Dutch sister company in 2026. The amount counted is 600,000 + 100,000 = EUR 700,000; the loan principal is not counted (FAQ 2.02). That is EUR 300,000 under EUR 1,000,000, so only part A of the local file is filled in.

```oa-check
name: Belgian NV, 9-month 2025 year, MF/LF revenue test and local file part B test
inputs:
  revenue_excl_nonrecurring: 40000000
  months_in_year: 9
  revenue_threshold: 50000000
  goods_from_fr: 600000
  interest_from_nl: 100000
  unit_threshold: 1000000
steps:
  - revenue_12m: revenue_excl_nonrecurring / months_in_year * 12
  - revenue_over_threshold: revenue_12m - revenue_threshold
  - unit_cross_border: goods_from_fr + interest_from_nl
  - unit_headroom: unit_threshold - unit_cross_border
expected:
  revenue_12m: 53333333.33
  revenue_over_threshold: 3333333.33
  unit_cross_border: 700000
  unit_headroom: 300000
```

A positive `revenue_over_threshold` means the revenue criterion is exceeded; a positive `unit_headroom` means the business unit stays under EUR 1m and part B is not needed.

## Ask the client first

1. **Which group entities does the Belgian company deal with, in which countries, and for how much?** Cross-border dealings inside a multinational group fall under art. 185, § 2; anything else falls under art. 26. Amounts per business unit decide local file part B.
2. **What were the company's revenue (excluding non-recurring), balance sheet total and FTE in the year before the last closed year, and how long was that year?** Any one criterion over the limit triggers 275 MF and 275 LF.
3. **What was the group's consolidated revenue in the previous reporting period, where is the ultimate parent, and who files the CbC report?** This decides 275 CBC and 275 CBC NOT.
4. **Is there a transfer pricing policy, an intercompany agreement and a benchmark for each flow?** Without them the administration can adjust to its own point in the range, usually the median.
5. **Has any Belgian or foreign ruling, APA or audit adjustment touched these flows, and when was the assessment notice received?** This decides whether a downward adjustment, a MAP or an arbitration request is still possible within three years.
6. **Has the company ever received a fine notice under art. 445, § 3?** The fine depends on the rank of the breach.

## Sources

| Source | URL | Read on |
|---|---|---|
| FisconetPlus, WIB 92 income 2026 (table of contents) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2ebbd3f4-ca47-41f5-8f17-2a243befae75 | 2026-10-22 |
| WIB 92 art. 26 (abnormal or gratuitous advantages granted) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9e236a9-9b1f-447a-8eae-4e50feaf83d1 | 2026-10-22 |
| WIB 92 art. 79 (no loss offset against advantages received) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/836dcd26-5c68-4b5c-a6a1-057dab115af1 | 2026-10-22 |
| WIB 92 art. 185 (arm's length, § 2) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/bf1f6e00-f321-4a51-835c-967f4c019b83 | 2026-10-22 |
| WIB 92 art. 206/1 (downward adjustment taken out of reserves) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/9fc0360b-c34b-4f33-aec5-e3d6b8418130 | 2026-10-22 |
| WIB 92 art. 206/3 (minimum base: advantages received, increases of 10% or more) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1e2ab543-c40d-41fa-8081-591ae036e18e | 2026-10-22 |
| WIB 92 art. 207 (order of deductions; no longer holds the advantages rule) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c5cbf033-a4dc-40d9-8848-4ed87bbb5586 | 2026-10-22 |
| WIB 92 art. 215 (rates) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1 | 2026-10-22 |
| WIB 92 art. 321/1 (definitions) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/580b569b-f7b1-4737-b66e-6294b7b596ac | 2026-10-22 |
| WIB 92 art. 321/2 (CbC report, EUR 750m, § 4/1 from 2028) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/45e1ce54-89f9-4356-badf-2fcfebbc7fb1 | 2026-10-22 |
| WIB 92 art. 321/3 (CbC notification) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c31d4a6b-5a15-4d3e-b5d0-56329a4bf16f | 2026-10-22 |
| WIB 92 art. 321/4 (master file) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a411e50a-13b6-4ffc-951e-d8f9a12615af | 2026-10-22 |
| WIB 92 art. 321/5 (local file, EUR 1m per business unit) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/efcb1b25-7a0e-4af5-acc8-fd875f85f8d9 | 2026-10-22 |
| WIB 92 art. 321/6 (use of the CbC report) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/dc69dbd0-73d6-4eae-88ae-152ae44d4037 | 2026-10-22 |
| WIB 92 art. 321/7 (English allowed) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a6005852-ca6d-4d8b-9c58-161e4c2e122d | 2026-10-22 |
| WIB 92 art. 376 (ex officio relief after MAP or arbitration) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/922814f1-9e8e-40bc-8165-43a67830e65f | 2026-10-22 |
| WIB 92 art. 444 (tax increases) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0 | 2026-10-22 |
| WIB 92 art. 445 (fines, § 3 transfer pricing) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f | 2026-10-22 |
| KB/WIB 92 art. 229/5, income 2026 (fine scale) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/184c431f-6fb7-46d2-b2fd-4bce1186ec0b | 2026-10-22 |
| Law of 24 December 2002, title III (advance decisions), art. 20 to 24 | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/b1f37aaf-8af5-4f0c-84c9-ee3b3ee33d48 | 2026-10-22 |
| Law of 2 May 2019 transposing Directive (EU) 2017/1852 (B.S. 17 May 2019) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/fe0e1a5c-4abe-44f6-a27b-3dcd90f7a4c8 | 2026-10-22 |
| Circular 2017/C/56 (275 CBC, CBC NOT, MF, LF) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d36905c4-a9dc-48ba-9565-d9ca86df5082 | 2026-10-22 |
| Circular 2019/C/14 (art. 445, § 3 fines) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d747344b-6161-489d-93d6-0377665ea5f9 | 2026-10-22 |
| Circular 2020/C/88 (BEPS 13 FAQ) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ea99e5c1-8ab9-4ebd-8a4e-d3229a1585ef | 2026-10-22 |
| Circular 2020/C/35 (Belgian transfer pricing guidelines) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/79654895-7b25-40f7-8879-00a72e39ea85 | 2026-10-22 |
| Circular 2026/C/45 (Amount B addendum, 19 March 2026) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/bdba1312-92d8-435b-8aa9-266c65626260 | 2026-10-22 |
| Circular 2018/C/27 (MAP, arbitration, APA contact) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/9a511b78-6594-4df5-92ec-e35d8b488b5f | 2026-10-22 |
| FOD Financiën, transfer pricing pages (financien.belgium.be) | https://financien.belgium.be/nl/experten-partners/verrekenprijzen | Not read: the site returned a bot-protection page on 2026-10-22; no figure relies on it |

Not yet confirmed: the AY 2027 corporate return deadline (and so the 2026 local file deadline), not published on 22 October 2026; whether the administration still expects a ruling before it grants a downward adjustment under art. 185, § 2, b (the statute does not require one; the official TP page could not be read); the current upload channel for 275 LF (circular 2017/C/56 named e-mail, the 2020 FAQ says all BEPS 13 forms were brought onto MyMinfin; the FOD Financiën page that would confirm the 2026 channel could not be read).
