---
name: ie-transfer-pricing
description: "Use this skill for Irish transfer pricing under Part 35A of the Taxes Consolidation Act 1997 (TCA), as substituted by Finance Act 2019 and amended since. It covers who is associated (s.835B), the arm's length rule and the 2022 OECD Guidelines (s.835C, s.835D), Pillar One Amount B (s.835DA, from 2025), the domestic non-trading exclusion (s.835E), the SME exclusion (s.835EA) and the uncommenced SME regime (s.835F), documentation, master file EUR 250m and local file EUR 50m thresholds, the 30-day request and the EUR 4,000 or EUR 25,000 penalties (s.835G), corresponding adjustments (s.835H), the EUR 25m capital asset thresholds (s.835HA, s.835HB), country-by-country reporting (s.891H, EUR 750m), APAs, MAP and the EU dispute regulations. Tax year 2026. Trigger on: transfer pricing Ireland, Part 35A, Irish local file, master file Ireland, CbCR Ireland, Revenue APA, s.835G penalty. Out of scope: corporation tax rates and the base in general (ie-corporation-tax), treaties and non-residents generally (ie-cross-border), VAT (ie-vat-return)."
version: 0.2
jurisdiction: IE
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland transfer pricing (Part 35A TCA 1997), 2026

This skill sets out how Irish transfer pricing works for chargeable periods in 2026: who is in scope, what must be documented and by when, what happens if Revenue adjusts a price, and how double taxation is removed. The law is Part 35A TCA 1997 (sections 835A to 835HB), substituted by section 27 of Finance Act 2019 for chargeable periods starting on or after 1 January 2020, and amended since: Finance Act 2021 substituted s.835E (the domestic non-trading exclusion), Finance Act 2022 moved s.835D to the 2022 OECD Guidelines, and Finance Act 2024 s.45 inserted s.835DA (Amount B). Finance Act 2025 made no change to Part 35A, and the Finance (No. 2) Bill 2026, as initiated in October 2026, does not amend it. Country-by-country reporting sits in s.891H TCA, which Finance Act 2025 s.50 amended for accounting periods ending on or after 1 January 2026.

Revenue's main guidance is Tax and Duty Manual (TDM) Part 35A-01-01, last reviewed June 2024, and the Notes for Guidance on Part 35A, Finance Act 2025 edition (December 2025). Where the two differ, the Notes for Guidance are newer.

See also: `ie-corporation-tax` (rates, CT1, preliminary tax, interest limitation), `ie-cross-border` (treaties, withholding, non-residents) and the method skill `transfer-pricing-workflow-base` (functional analysis, method choice, benchmarking).

## Who this applies to

**Associated persons (s.835B).** Two persons are associated if one participates in the management, control or capital of the other, or the same person participates in both. The controlled person must be a company. A company controlled by an individual together with relatives (spouse, civil partner, ancestor, lineal descendant, brother or sister, s.433(3)(a)) counts as controlled by that individual. "Control" follows s.11 TCA.

**Arrangements in scope (s.835C(1)).** Any arrangement for the supply and acquisition of goods, services, money, assets (including intangibles) or anything else of commercial value, where supplier and acquirer are associated at the time, and the profits, gains or losses of either side are within the charge to Irish income tax, corporation tax or capital gains tax. Since 2020 this covers trading, non-trading and capital transactions, domestic and cross-border.

**Pre-July 2010 arrangements.** The old grandfathering for terms agreed before 1 July 2010 ended for chargeable periods starting on or after 1 January 2020 (Finance Act 2019 s.27(5)). Those arrangements must now be priced at arm's length.

**Out of scope:**

- **SMEs (s.835EA).** Part 35A does not apply to a person who is a small or medium-sized enterprise for the chargeable period. The test is the EU definition (Commission Recommendation 2003/361/EC), applied to the whole group: fewer than 250 staff, and turnover of EUR 50 million or less and/or a balance sheet total of EUR 43 million or less. Irish modifications apply (TDM 35A-01-01, section 7).
- **The SME regime in s.835F has not started.** Finance Act 2019 inserted s.835F to bring SMEs into the rules with no documentation for small enterprises and simplified documentation for medium enterprises (arrangements over EUR 1 million with non-qualifying associates). It only starts on a ministerial commencement order under Finance Act 2019 s.27(4). No order has been made: the Irish Statute Book's legislation directory for Finance Act 2019 (updated to 13 October 2026) lists s.27(1), as it relates to the SME provision, as "Not yet commenced", and Revenue's Notes for Guidance (December 2025) say the same. Until then the old SME exclusion continues as s.835EA.
- **Domestic non-trading exclusion (s.835E, as substituted by Finance Act 2021).** Part 35A does not apply to a party's Case III, IV or V (non-trading) profits from an arrangement where both supplier and acquirer are "qualifying persons". A supplier qualifies if its consideration is (or, if there were any, would be) taxed under Case III, IV or V. An acquirer qualifies if its consideration is (or would be) taken into account under Schedule D, or, failing that, if it is Irish resident and its relevant activities are within the Schedule D charge. A person within the charge to income tax must be Irish resident, and a s.110 company never qualifies. The typical case is an interest-free loan between two Irish companies. Trading (Case I and II) income and chargeable gains stay in scope. Anti-avoidance: the exclusion needs bona fide commercial reasons and no main purpose of tax avoidance (s.835E(6)); it is lost where the acquirer would get a deduction or relief, in Ireland or abroad, above the actual consideration (s.835E(7)); and it is lost for a back-to-back arrangement with a non-qualifying person aimed at a tax advantage (s.835E(8)). The parties must keep records showing the exclusion applies (s.835E(9)).
- **Persons not chargeable on the profits.** Funds, IREFs and REITs (taxed on distribution), and non-resident companies with no Irish taxable presence, are outside the rules (TDM 35A-01-01, section 4.7).

**Irish branches of non-resident companies.** A non-resident company chargeable to corporation tax on an Irish branch trade is within the charge, so its arrangements with associated persons that feed into the branch profits are in scope, and it can be a qualifying person for s.835E on arrangements relating to the branch (TDM 35A-01-01, section 6.4.4). Attribution of profit between head office and branch is a separate question, not covered here.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporation tax on trading income (where a TP adjustment hits a trade) | 12.5% | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx |
| Corporation tax on non-trading income and excepted trades | 25% | 2026 | same page |
| Master file: MNE group total revenue in the relevant period | EUR 250 million or more | 2026 | s.835G(1), (3)(a); https://www.irishstatutebook.ie/eli/2019/act/45/section/27/enacted/en/html |
| Local file: MNE group total revenue in the relevant period | EUR 50 million or more | 2026 | s.835G(1), (3)(b); same |
| SME exclusion: group staff / turnover / balance sheet | under 250; EUR 50m or less and/or EUR 43m or less | 2026 | s.835EA; TDM 35A-01-01 section 7 |
| Capital allowances: TP applies to the acquirer's allowances only if capital expenditure on the asset exceeds, and to the supplier's balancing allowance or charge only if the asset's market value exceeds | EUR 25 million | 2026 | s.835HA(1)(a), (c) |
| Chargeable gains: TP applies only if market value of the asset exceeds | EUR 25 million | 2026 | s.835HB(2)(a), (3)(a) |
| Low-value-adding intra-group services, simplified approach mark-up | 5% on relevant costs, no benchmarking needed | 2026 | TDM 35A-01-01 section 8.7 (2022 OECD Guidelines Ch. VII D) |
| Pillar One Amount B: tested party operating expenses must be within | 3% to 30% of net revenues | chargeable periods from 1 Jan 2025 | s.835DA(2)(b)(iii); Finance Act 2024 s.45 |
| Documentation produced on request | within 30 days of a written request | 2026 | s.835G(5)(b) |
| Fixed penalty, failure to produce documentation | EUR 4,000 | 2026 | s.835G(6)(a) |
| Fixed penalty if the local file threshold is met | EUR 25,000 plus EUR 100 a day while the failure continues | 2026 | s.835G(6)(b) |
| Country-by-country report: group revenue in the preceding fiscal year | EUR 750 million or more | 2026 | TDM 38-03-21 paragraphs 2 and 8 (s.891H) |
| CbC report penalty | EUR 19,045 plus EUR 2,535 a day; EUR 19,045 for an incorrect or incomplete report | 2026 | TDM 38-03-21 paragraph 30 (s.891H(7)) |
| Late payment interest on corporation tax | 0.0219% per day | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx |

Pillar Two: in-scope groups also pay the 15% minimum tax; see `ie-corporation-tax`. A transfer pricing adjustment changes the Irish profit that feeds into that computation.

## The taxable base

**The two rules (s.835C(2)).** If the consideration an acquirer pays is more than the arm's length amount, the acquirer's taxable profits are computed as if the arm's length amount were paid. If the consideration a supplier receives is less than the arm's length amount (including nothing at all), the supplier's taxable profits are computed as if the arm's length amount were received. The rules only increase Irish profits or reduce Irish losses. They never reduce Irish taxable profit on their own initiative.

**Finding the arm's length amount (s.835C(3) to (5)).** First identify the actual commercial and financial relations (the "identified arrangement"), based on substance where it differs from the written form. Then apply the most appropriate method from the OECD Guidelines. An arrangement that independent parties acting rationally would not have entered into can be disregarded or replaced (Chapter I, D.2). For loans, this includes testing the amount of debt, not only the interest rate (TDM 35A-01-01, section 4.4.2).

**OECD Guidelines (s.835D).** Part 35A is construed, as far as practicable, consistently with the OECD Transfer Pricing Guidelines. Since chargeable periods starting on or after 1 January 2023 that means the January 2022 edition (Finance Act 2022). The Minister can designate later OECD guidance by order.

**Pillar One Amount B (s.835DA).** For chargeable periods from 1 January 2025, where an Irish company sells goods to a related wholesale distributor (or uses a related sales agent or commissionaire) resident in a "covered jurisdiction" that has a tax treaty with Ireland, and that jurisdiction prices the distributor under Amount B, Ireland accepts that outcome. Commodities, services and digital goods are excluded, and the distributor's operating expenses must sit between 3% and 30% of net revenue. The local file must hold extra Amount B information, and the Irish party must notify Revenue that the section applied.

**Amounts treated as distributions (s.835C(7)).** If part of an excess payment is already treated as a distribution (for example, interest recharacterised under s.130), the TP comparison uses the payment net of that amount, so the same excess is not hit twice.

**Low-value-adding services.** A taxpayer can apply the OECD simplified approach (2022 Guidelines, Chapter VII, D) without an election: cost plus 5%, no benchmarking study, but the Chapter VII D.3 documentation must exist. Financial transactions are not low-value services; Senior management services, R&D, sales and marketing and the group's core business are also excluded (2022 Guidelines para 7.47). Revenue's own example denies penalty protection to a company that priced a loan this way (TDM 35A-01-01, example 8.14.2.1).

**Capital transactions.** TP applies to the acquirer's capital allowances only where the capital expenditure on the asset exceeds EUR 25 million, and to the supplier's balancing allowance or charge only where the asset's market value exceeds EUR 25 million (s.835HA), and to chargeable gains only where the asset's market value exceeds EUR 25 million (s.835HB). Assets split to stay under EUR 25 million are added back together. Several no-gain no-loss reliefs (group transfers, reconstructions) take priority over TP. TP cannot reduce a gain, increase a loss, or raise an acquirer's base cost above what the gains rules give.

**Corresponding adjustment, domestic only (s.835H).** If one Irish taxpayer's profits are adjusted up, the Irish counterparty (the "affected person") can claim the matching downward adjustment, once the tax on the upward adjustment has been paid. Closing trading stock values are not changed. Foreign tax credit is reduced to match. For a cross-border adjustment, relief comes through the treaty (see Cross-border points).

**Documentation (s.835G).** Every relevant person in scope must have records reasonably required to show its profits follow Part 35A. On top of that, a constituent entity of an MNE group must hold:

- a **master file** (Annex I to Chapter V of the OECD Guidelines) if group revenue for the relevant period is EUR 250 million or more;
- a **local file** (Annex II to Chapter V) if group revenue is EUR 50 million or more.

The "relevant period" is the group's fiscal year that corresponds to (or substantially coincides with) the Irish company's chargeable period, not the preceding year. For this test an "MNE group" has entities in two or more jurisdictions, or a foreign permanent establishment, with no CbC-style exclusion for small groups. A purely domestic group is not an MNE group, so the master and local file duties do not apply to it, but the general records duty in s.835G(2) does.

Revenue accepts a single Irish "country file" for all Irish group entities if entity-level data is readily accessible, counterparty documentation if complete from the Irish side, and documentation held abroad if it can be produced in 30 days (TDM 35A-01-01, section 8.8). Revenue expects a full TNMM benchmarking search every 3 years with comparables' financials refreshed every year (section 8.9).

Arrangements agreed before 1 July 2010, unchanged since, between two qualifying persons are excluded from the documentation duty (s.835G(4)).

## Deadlines and filing

| What | When | Where |
|---|---|---|
| TP documentation (records, master file, local file) prepared | No later than the CT1 return filing date for the period (s.835G(5)(a)); for ROS filers, the 23rd of the ninth month after the period ends | Held by the company, not filed |
| Documentation provided to Revenue | Within 30 days of a written request from a Revenue officer (s.835G(5)(b)) | As the request directs |
| Amount B notification | No later than the CT1 return filing date for the period (s.835G(3A), as read with s.835DA(5)(b)) | Revenue, in the form Revenue prescribes |
| CbC notification (who files the report) | By the last day of the group's fiscal year, every year (TDM 38-03-21 paragraph 32) | ROS |
| CbC report | Within 12 months after the end of the fiscal year (TDM 38-03-21 paragraph 27) | ROS, in XML |
| Domestic corresponding adjustment claim (s.835H) | After the tax on the upward adjustment is paid; amend the CT1 within the normal time limits | ROS |
| Correlative adjustment claim for a foreign adjustment (treaty Article 9) | After the foreign tax is paid | Form CA1 |
| MAP request under a treaty | Within the time limit in the treaty. Treaties that follow Article 25 of the OECD Model allow 3 years from the first notification of the action; a few set a different period, so read the treaty and any MLI change. Revenue counts from the date the first assessment notice (or equivalent) is received (TDM 35-02-08 section 2.1.1) | Revenue competent authority |
| EU dispute complaint (S.I. No. 306 of 2019, amended by S.I. No. 673 of 2020) | Within 3 years of receipt of the first notification of the action; competent authorities then accept or reject within 6 months (TDM 35-02-10 sections 2 and 2.1) | Competent authority of each Member State concerned (an Irish individual or smaller company files with Revenue only) |

Revenue works TP compliance through two programmes: the Transfer Pricing Compliance Review, a self-review that is a Level 1 intervention (an unprompted disclosure is still possible), and risk-driven audits by the Large Corporates Division, which are Level 2 (TDM 35A-01-01, section 12).

## Penalties and interest

**Failure to produce documentation (s.835G(6)).** EUR 4,000 if the records are not provided within 30 days of a written request. If the company meets the local file threshold (group revenue EUR 50 million or more), the penalty is EUR 25,000 plus EUR 100 for each day the failure continues. The higher penalty applies to a failure to produce any required TP documentation, not only the local file (TDM 35A-01-01, section 8.14.1).

**Penalty protection (s.835G(7)).** A TP adjustment is ignored when deciding whether a careless-behaviour tax-geared penalty applies (s.1077E(5), or s.1077F(2)(d) where relevant) if all three conditions are met:

1. the documentation was prepared by the return filing date;
2. it was provided within 30 days of the request; and
3. it is complete and accurate and shows reasonable efforts to comply with Part 35A.

Protection does not cover deliberate behaviour. Revenue gives two examples where protection fails: pricing a loan as a low-value service, and ignoring an internal comparable such as a third-party loan on similar terms (TDM 35A-01-01, section 8.14.2).

**Tax and interest.** The adjustment itself brings the extra tax plus late payment interest at 0.0219% a day from the original due date.

**CbC reporting (s.891H(7)).** Failure to file: EUR 19,045 plus EUR 2,535 a day while the failure continues. Incorrect or incomplete report: EUR 19,045. An Irish constituent entity that fails to ask its parent for the information needed for the report is treated as having failed to file (TDM 38-03-21 paragraph 14).

## Cross-border points

**Treaty relief.** Ireland's treaties follow Article 9 of the OECD Model. Where a foreign tax authority adjusts the price and the Irish company accepts and pays, the Irish company can claim a correlative adjustment on Form CA1 (Revenue Article 9 guidance, TDM 35-02-09). Where the adjustment is disputed, the Mutual Agreement Procedure applies (TDM 35-02-08). Revenue's competent authority function is independent of audit.

**EU disputes.** Two routes exist: the EU Arbitration Convention (90/436/EEC), limited to TP and profit attribution, and Council Directive (EU) 2017/1852, given effect by the European Union (Tax Dispute Resolution Mechanisms) Regulations 2019 (S.I. No. 306 of 2019, amended by S.I. No. 673 of 2020) for tax years starting on or after 1 January 2018. A complaint under the Directive ends any MAP or Arbitration Convention case on the same dispute. The competent authorities then have 2 years (extendable by 1) to agree, after which an advisory commission can be set up (TDM 35-02-10).

**Bilateral APAs.** Revenue has run a formal bilateral APA programme since 1 July 2016 (TDM 35-02-07, reviewed October 2026). Key points: no Revenue application fee; no unilateral APAs; a typical term of 5 years plus roll-back in suitable cases; never more than 5 years beyond the date the APA is agreed; target completion 24 months; pre-filing meeting, then application, then annual reports.

**Country-by-country reporting (s.891H).** Groups with consolidated revenue of EUR 750 million or more in the preceding fiscal year file a CbC report. For accounting periods ending on or after 1 January 2026, Finance Act 2025 s.50 requires the report to follow the OECD's May 2024 CbCR implementation guidance and sets three threshold rules in s.891H(13): the EUR 750 million is reduced pro rata where the parent's preceding fiscal year was shorter than 12 months; a group in its first year after leaving another group is treated as below the threshold; and extraordinary investment income and gains shown in the consolidated accounts count as revenue (unless the parent's jurisdiction excludes them for its own filing test). An Irish ultimate parent files in Ireland. An Irish subsidiary or branch files under secondary reporting only in the cases the regulations list (no filing obligation in the parent's country, no exchange agreement, or a systemic failure). Every Irish constituent entity must notify Revenue each year who the reporting entity is, by the last day of the fiscal year, though one entity can notify for all.

**Domestic and cross-border both count.** Irish transfer pricing is not limited to cross-border deals. A trading arrangement between two Irish companies is in scope, but the s.835H corresponding adjustment usually makes it neutral overall.

## Worked examples

### Example 1: back-office service charge from a foreign parent, and an interest-free loan to a foreign sister company

Shannon Components Ltd is an Irish trading company, 100% owned by a German parent. The group has 1,400 staff and revenue of EUR 300 million. With 250 staff or more the group fails the SME test (s.835EA), whatever its balance sheet. Revenue of EUR 300 million is above both documentation thresholds, so Shannon needs a master file and a local file. Year ended 31 December 2026.

1. **Back-office service charge.** The parent charges Shannon EUR 2,000,000 for back-office support (payroll, IT help desk, accounting). These are on the OECD's list of low-value-adding services (2022 Guidelines, para 7.49). The OECD lets a tax administration set a threshold above which it reviews the simplified approach (para 7.63); Revenue's TDM section 8.7 sets none, so the EUR 2 million size does not by itself rule the approach out. What would rule it out is the content: senior management, R&D, sales and marketing, purchasing of raw materials and financial transactions are excluded (para 7.47), so a "management fee" that includes any of these must be split or priced another way. The local file documents the D.3 information. The cost the parent incurred in serving Shannon is EUR 1,500,000. Under the simplified approach, the arm's length charge is cost plus 5%: EUR 1,575,000. Shannon is the acquirer and paid more than arm's length, so s.835C(2)(a) disallows the excess, EUR 425,000. The charge is a deduction against Shannon's trade, so the disallowance is taxed at 12.5%: EUR 53,125.
2. **Loan.** Shannon lent EUR 4,000,000 interest-free to a sister company in the Netherlands. The local file benchmark gives an arm's length rate of 5.0% (company-specific figure). The Dutch borrower is not chargeable to Irish tax, so it is not a qualifying person and the s.835E exclusion does not apply. Shannon is the supplier and received less than arm's length (nothing), so s.835C(2)(b) imputes EUR 200,000 of Case III interest, taxed at 25%: EUR 50,000.

Total extra corporation tax: EUR 103,125. No corresponding adjustment is available in Ireland, because the counterparties are not Irish taxpayers. Relief in Germany or the Netherlands depends on those countries and the treaties. If the loan were to an Irish resident sister company within the Schedule D charge on its activities, both parties would be qualifying persons and s.835E would switch off the Case III imputation.

```oa-check
name: Shannon Components Ltd, 2026, back-office service charge and interest-free loan
inputs:
  fee_paid: 2000000
  service_cost: 1500000
  lvs_markup: 0.05
  loan: 4000000
  arm_length_rate: 0.05
  trading_rate: 0.125
  non_trading_rate: 0.25
steps:
  - arm_length_fee: service_cost * (1 + lvs_markup)
  - fee_disallowed: max(fee_paid - arm_length_fee, 0)
  - ct_on_fee: fee_disallowed * trading_rate
  - imputed_interest: loan * arm_length_rate
  - ct_on_interest: imputed_interest * non_trading_rate
  - total_extra_ct: ct_on_fee + ct_on_interest
expected:
  arm_length_fee: 1575000
  fee_disallowed: 425000
  ct_on_fee: 53125
  imputed_interest: 200000
  ct_on_interest: 50000
  total_extra_ct: 103125
```

### Example 2: documentation thresholds and the late-documentation penalty

Liffey Distribution Ltd is an Irish distributor in a US-parented group. The group's revenue in the fiscal year matching Liffey's 2026 chargeable period is EUR 80 million, with 600 staff, so the group is not an SME. EUR 80 million is above the EUR 50 million local file threshold but below the EUR 250 million master file threshold: Liffey needs a local file, not a master file. It is also below the EUR 750 million CbC threshold.

A Revenue officer asks in writing for Liffey's TP documentation. Liffey does not produce it within 30 days, and the failure continues for 45 days after the deadline. Because Liffey meets the local file threshold, the s.835G(6)(b) penalty applies: EUR 25,000 plus EUR 100 for each of the 45 days, EUR 29,500. A company below the local file threshold would face the EUR 4,000 fixed penalty instead. Liffey also loses s.835G(7) penalty protection for any later adjustment, because it did not provide the records within 30 days.

```oa-check
name: Liffey Distribution Ltd, 2026, local file threshold and s.835G(6) penalty
inputs:
  group_revenue: 80000000
  local_file_threshold: 50000000
  master_file_threshold: 250000000
  base_penalty_local_file: 25000
  daily_penalty: 100
  days_continuing: 45
  base_penalty_other: 4000
steps:
  - headroom_over_local_file: group_revenue - local_file_threshold
  - shortfall_to_master_file: master_file_threshold - group_revenue
  - penalty_local_file_size: base_penalty_local_file + daily_penalty * days_continuing
  - extra_vs_smaller_company: penalty_local_file_size - base_penalty_other
expected:
  headroom_over_local_file: 30000000
  shortfall_to_master_file: 170000000
  penalty_local_file_size: 29500
  extra_vs_smaller_company: 25500
```

## Ask the client first

1. **Group size, on a group basis.** Staff headcount, turnover and balance sheet total of the whole group for the period. If the group is an SME, Part 35A does not apply at all (s.835EA).
2. **Group revenue for the fiscal year that matches the Irish chargeable period**, and whether the group has entities or branches in more than one country. This decides the local file (EUR 50 million) and master file (EUR 250 million).
3. **A list of every related-party arrangement**: goods, services, loans and balances, guarantees, IP, asset transfers, with amounts and counterparties' tax residence. Cross-border and non-trading items are where the s.835E exclusion does not help.
4. **Any asset transfers over EUR 25 million** between associated persons, and whether a group or reconstruction relief applies.
5. **Existing documentation and its date.** Was it ready by the CT1 filing date? When was the last full benchmarking search? Without both, penalty protection under s.835G(7) is lost.
6. **Foreign adjustments, APAs or disputes** with the counterparty country, and the dates of first notification (for MAP and the 3-year limits).

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act 2019, s.27 (substituting Part 35A TCA 1997, ss.835A to 835HB) | https://www.irishstatutebook.ie/eli/2019/act/45/section/27/enacted/en/html | 2026-10-22 |
| Finance Act 2024, s.45 (inserting s.835DA, Pillar One Amount B) | https://www.irishstatutebook.ie/eli/2024/act/43/section/45/enacted/en/html | 2026-10-22 |
| Revenue, Notes for Guidance TCA 1997 Part 35A, Finance Act 2025 edition (December 2025) | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part35A.pdf | 2026-10-22 |
| Revenue, TDM Part 35A-01-01 Transfer Pricing (reviewed June 2024) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35a/35a-01-01.pdf | 2026-10-22 |
| OECD Transfer Pricing Guidelines, January 2022, Chapter VII section D (paras 7.43 to 7.65) | https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/01/oecd-transfer-pricing-guidelines-for-multinational-enterprises-and-tax-administrations-2022_57104b3a/0e655865-en.pdf | 2026-10-22 |
| Irish Statute Book, Finance Act 2019 legislation directory (commencement of s.27, updated to 13 October 2026) | https://www.irishstatutebook.ie/eli/isbc/2019_45.html | 2026-10-22 |
| Finance Act 2025, s.50 (amending s.891H, CbC reporting) | https://www.irishstatutebook.ie/2025/en/act/pub/0018/sec0050.html | 2026-10-22 |
| Finance (No. 2) Bill 2026, as initiated (Bill No. 98 of 2026) | https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/initiated/b9826d.pdf | 2026-10-22 |
| Revenue, TDM Part 38-03-21 Country-by-Country Reporting (reviewed September 2025) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-38/38-03-21.pdf | 2026-10-22 |
| Revenue, TDM Part 35-02-07 Bilateral APA Guidelines (reviewed October 2026) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35/35-02-07.pdf | 2026-10-22 |
| Revenue, TDM Part 35-02-08 MAP Guidelines (updated September 2026) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35/35-02-08.pdf | 2026-10-22 |
| Revenue, TDM Part 35-02-10 EU Tax Dispute Resolution Mechanisms Regulations 2019 (reviewed September 2026) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35/35-02-10.pdf | 2026-10-22 |
| Revenue, Transfer pricing (including MAP requests) | https://www.revenue.ie/en/companies-and-charities/international-tax/transfer-pricing/index.aspx | 2026-10-22 |
| Revenue, Advance Pricing Agreement (APA) | https://www.revenue.ie/en/companies-and-charities/international-tax/transfer-pricing/advance-pricing-agreement-apa.aspx | 2026-10-22 |
| Revenue, Mutual Agreement Procedures (MAP) | https://www.revenue.ie/en/companies-and-charities/international-tax/transfer-pricing/mutual-agreement-procedures-map.aspx | 2026-10-22 |
| Revenue, Article 9 correlative adjustment claims (Form CA1) | https://www.revenue.ie/en/companies-and-charities/international-tax/transfer-pricing/article-9-correlative-adjustment-claims.aspx | 2026-10-22 |
| Revenue, Corporation tax basis of charge (12.5% and 25%) | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx | 2026-10-22 |
| Revenue, CT payment and filing (filing date, 0.0219% daily interest) | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx | 2026-10-22 |

Not yet confirmed: the percentages of the s.1077E tax-geared penalties (not stated here); what TP questions the 2026 CT1 asks; whether the Finance (No. 2) Bill 2026 is amended at later stages to touch Part 35A or s.891H (as initiated it does not); how profit is attributed between an Irish branch and its foreign head office (not part of Part 35A, not covered here).

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
