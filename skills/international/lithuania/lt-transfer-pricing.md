---
name: lt-transfer-pricing
description: "Use this skill for Lithuanian transfer pricing (sandorių kainodara) in tax year 2026. It covers associated persons (asocijuoti asmenys) and related persons under Corporate Income Tax Law art. 2(8) and 2(33), the arm's length rule in art. 40(1) and (2), the Minister of Finance rules approved by Order No. 1K-123 (methods, the arm's length range and the median, low value-adding services at cost plus 5%, hard-to-value intangibles), documentation (master file above EUR 15 million revenue in a group, local file above EUR 3 million, the EUR 90,000 transaction exemption, 30 days to hand it over), the FR0528 related-party report, advance pricing agreements under Tax Administration Law art. 37-2, country-by-country reporting (EUR 750 million), the 5-year reassessment window, fines of 20% to 100% and late payment interest. Trigger on: transfer pricing Lithuania, kainodaros dokumentai, ištiestosios rankos principas, asocijuoti asmenys, FR0528, local file Lithuania. Out of scope: corporate tax in general (lt-corporate-income-tax), payroll (lt-payroll-social), VAT (lithuania-vat-return)."
version: 0.1
jurisdiction: LT
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lithuania: transfer pricing (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. The law comes from the consolidated texts on e-tar.lt (the Register of Legal Acts) and the guidance from vmi.lt (the State Tax Inspectorate, VMI), all read on 23 October 2026. It prepares working papers; it is not authority to file or pay.

This is the transfer pricing (TP) skill for the Lithuanian pack. It links rather than repeats:

- Corporate income tax, the base and the return: [lt-corporate-income-tax](lt-corporate-income-tax.md) (that skill still carries 2025 figures).
- Overview of the system: [lt-tax-overview](lt-tax-overview.md).
- Individuals with business income follow the same rules through Personal Income Tax Law art. 15(2); see [lithuania-pit](lithuania-pit.md) for the tax itself.

The law is the Law on Corporate Income Tax No. IX-675 ("PMĮ", consolidated version in force from 19 May 2026), the Rules implementing PMĮ art. 40(2) and Personal Income Tax Law art. 15(2), approved by Minister of Finance Order No. 1K-123 of 9 April 2004 as restated by Order 1K-470 and amended by Order 1K-338 ("the Rules", consolidated version in force from 1 January 2021), and the Law on Tax Administration No. IX-2112 ("MAĮ", consolidated version in force from 1 July 2026). Currency: euro (EUR).

## Who this applies to

**Every Lithuanian entity and every Lithuanian permanent establishment.** When it computes taxable profit, an entity must count income from any transaction at its market price, and may deduct costs only up to the market price (PMĮ art. 40(1)). Where associated persons agree conditions that unassociated persons would not, any profit that would otherwise have gone to one of them can be added to its income and taxed (PMĮ art. 40(2)). The Rules apply to Lithuanian entities and to foreign entities with a Lithuanian permanent establishment, and with the necessary changes to resident and non-resident individuals carrying on individual activity through a fixed base (Rules para. 2). They apply to every controlled transaction, written contract or not (para. 4).

**Associated persons (asocijuoti asmenys), PMĮ art. 2(8).** Persons (entities or individuals) are associated if either:

1. they are related persons (see below); or
2. one can influence the other so that their dealings differ from what each would agree when seeking its own maximum economic benefit.

**Related persons (susiję asmenys), PMĮ art. 2(33).** The test is met on any day of the reporting period or of the period before it. Related persons include:

- an entity and its participants, and an entity and members of its management bodies;
- an entity and the spouses, partners and close relatives of its participants or managers;
- members of one group of entities (a parent with subsidiaries in which it holds, directly or indirectly, more than 25% of shares, votes or profit rights, PMĮ art. 2(7));
- two entities where one holds, directly or indirectly, 25% or more of the other's shares or votes, or has agreed to coordinate its decisions with the other, to answer for the other's obligations to third parties, to hand over all or part of its profit, or has given the other the use of 25% or more of its assets;
- further links inside a group through participants with 25% or more, managers and their relatives, and two entities that the same participants or their relatives each own 25% or more of (art. 2(33), points 5 to 7 and 9);
- an entity and its permanent establishment, PEs of one entity, and PEs of group members (points 10 to 12);
- two entities where one has decision-making rights in the other (point 13).

**Domestic deals count.** The arm's length rule applies to transactions between two Lithuanian entities too. Only the documentation duty has a domestic exemption (Rules para. 87.1, see Deadlines).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Corporate income tax rate (applies to a TP adjustment of a company) | 17% (16% for 2025) | 2026 | https://www.vmi.lt/evmi/tarifai-5-str.- ; https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr (art. 5(1)) |
| Reduced rate for small entities with revenue up to EUR 300,000 | 7% (0% for the first two periods of qualifying new entities) | 2026 | https://www.vmi.lt/evmi/tarifai-5-str.- |
| Ownership link for related entities | 25% or more of shares or votes, direct or indirect | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr (art. 2(33)(8)) |
| Master file: Lithuanian entity or PE in an international group with prior-period revenue above | EUR 15,000,000 | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.55EC668C883A/asr (Rules para. 84) |
| Local file: Lithuanian entity or PE with prior-period revenue above (banks, financial and insurance companies always) | EUR 3,000,000 | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.55EC668C883A/asr (Rules para. 85) |
| Documentation exemption: controlled transaction with a value in the period not above | EUR 90,000 (unless repeated, linked or with a target territory) | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.55EC668C883A/asr (Rules para. 87.2) |
| FR0528 related-party report: a transaction, a total, or a loan balance on any day of | EUR 90,000 or more, excluding VAT | 2026 | https://www.vmi.lt/evmi/asocijuot%C5%B3-asmen%C5%B3-tarpusavio-sandori%C5%B3-arba-%C5%ABkini%C5%B3-operacij%C5%B3-ataskaita-fr0528- (answer KM1402) |
| Mark-up for low value-adding intra-group services (simplified approach) | 5% on the cost base | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.55EC668C883A/asr (Rules para. 76-1) |
| Hard-to-value intangibles: no ex post adjustment if the change in price stays within | 20% of the actual price, or the 20% is exceeded only more than 5 years after the year of first third-party income | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.55EC668C883A/asr (Rules para. 67-1) |
| Time to hand documentation to VMI after a request | 30 days | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.55EC668C883A/asr (Rules para. 91) |
| Refresh of the local file and of database comparables when conditions do not change | at least every 3 years (transaction data every year) | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.55EC668C883A/asr (Rules paras. 88, 89) |
| Keep documentation for at least | 5 calendar years from the year after the transaction | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.55EC668C883A/asr (Rules para. 94) |
| Fine on tax found short in a tax audit | 20% to 100% of the shortfall (assessed from the 60% midpoint) | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr (MAĮ art. 139(1), 140(5)) |
| Late payment interest (delspinigiai) | 0.027% a day from 1 August 2026 | 2026 | https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.- (answer KM2633) |
| Reassessment window | current year plus 3 years; current year plus 5 years for adjustments under PMĮ art. 40(2) | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr (MAĮ art. 68(1), 68(4)(4)) |
| Advance pricing agreement: decision period | 90 days, extendable by 90 days | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr (MAĮ art. 37-2(2)) |
| Advance pricing agreement: longest validity | the current year plus 5 calendar years from the decision | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr (MAĮ art. 37-2(5)) |
| Country-by-country report: group consolidated revenue in the prior year of at least | EUR 750,000,000 | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr (MAĮ art. 61(2)) |

Lithuanian law prints some article and paragraph numbers with a superscript (37², 76¹). This skill writes them as 37-2 and 76-1. "Art. 40(2)" means part 2 of article 40.

## The taxable base

**The adjustment.** VMI adds to the entity's income the profit it would have earned on arm's length terms (PMĮ art. 40(2)). The adjustment changes taxable profit, so tax follows at the entity's rate: 17% for most companies in 2026 (PMĮ art. 5(1)).

**How an arm's length price is found** (Rules paras. 6 to 19):

1. Analyse the controlled transaction: the item, a functional analysis of functions, assets and risks, the contract terms (actual conduct wins over the paper), the economic circumstances and the business strategy (paras. 7 to 13).
2. Choose comparables. Internal comparables come first. A taxpayer that has internal comparables but uses external ones must explain why (para. 16).
3. Apply the most appropriate method (para. 21). The five methods are comparable uncontrolled price, resale price, cost plus, profit split and transactional net margin (para. 20). Where traditional and profit methods are equally reliable, traditional methods are preferred, and CUP is preferred over the others (para. 23). Methods may be combined, and other valuation methods (such as discounted cash flow) may be used where needed (paras. 20, 25).
4. A temporary loss from a genuine strategy (market entry, a new product) is not a breach if the taxpayer proves it (para. 12).

**The range.** If the method gives a range, a price inside it is arm's length (para. 54), and VMI does not adjust a price inside the range unless changed conditions justify a different point (para. 57). The range must be built from equally reliable comparables; statistical methods are used when there is no better way to drop outliers (paras. 54, 55). When VMI adjusts using a range and has no better data, it adjusts to the **median**. If the taxpayer avoids cooperating, VMI may use any point in the range (para. 56).

**Services** (paras. 68 to 76-1):

- A service counts only if an unrelated person would pay for it or do it itself. Otherwise the charge is treated as zero (paras. 69, 70).
- Shareholder activities, duplicated services and incidental group benefits are not services to the payer (paras. 71, 72).
- Cost allocation keys (turnover, headcount) are allowed if the charge matches the benefit (para. 74).
- **Low value-adding services** (HR, IT support, accounting, legal and similar back-office work that is not the group's core business, creates no unique intangibles and carries no significant risk, para. 3.1) can be priced at cost plus **5%** without a benchmark, when a cost-based method is the most appropriate. The simplification does not apply where the same services are also bought from or sold to third parties (para. 76-1).

**Intangibles** (paras. 58 to 67-1). Each group member that performs, controls or funds development, enhancement, maintenance, protection or exploitation of an intangible earns a return for that contribution; legal ownership alone does not earn the residual (paras. 59 to 61). Cost-based methods are normally not used to value intangibles (para. 64). For **hard-to-value intangibles** VMI may adjust the original price using later results, unless the taxpayer shows detailed ex ante forecasts and that the difference came from unforeseeable events, or the change would be 20% or less of the actual price, or the 20% is exceeded only more than 5 years after the year in which the buyer first earned income from unassociated persons with the intangible (paras. 67-1.1 to 67-1.3).

**Interest and rent paid to a controlling person** have their own deductibility rules in PMĮ; they are in [lt-corporate-income-tax](lt-corporate-income-tax.md), not here.

## Deadlines and filing

**Supporting documents.** Every taxpayer under the Rules must have the documents that support arm's length pricing ready by the **15th day of the sixth month** after the end of the tax period in which the transaction took place (15 June 2027 for calendar 2026). Lithuanian entities and Lithuanian PEs whose controlled transactions are only with other Lithuanian entities or PEs may prepare them later, but must hand them over within the time VMI sets (Rules para. 19).

**Who must prepare formal TP documentation** (Rules chapter V):

- **Master file (pagrindinė byla):** a Lithuanian entity, or a foreign entity's Lithuanian PE, in an international group, whose revenue in the period before the transaction exceeded EUR 15 million (para. 84). Content: group structure and ownership chart, business description with the five largest products or services and any above 5% of group revenue, functional analysis, restructurings, intra-group services, intangibles and the IP strategy, intra-group financing, and the group's APAs (para. 80). A taxpayer that cannot get all of it must explain why and give what it has (para. 81).
- **Local file (šalies byla):** a Lithuanian entity with prior-period revenue above EUR 3 million; banks, credit and financial institutions; insurers; and Lithuanian PEs with attributed prior-period revenue above EUR 3 million (para. 85). Content: the transaction analysis, the tested party, the method and why, the comparables search step by step with accepted and rejected companies, calculations and adjustments, the preparation and update dates, and business restructurings (paras. 82, 83, 86).
- **Exemptions** (para. 87): (1) transactions between Lithuanian entities, PEs and resident individuals tied to their Lithuanian activity; (2) a controlled transaction worth **EUR 90,000 or less** in the period, unless there are several identical transactions with the same associated person totalling more than EUR 90,000, it is inseparable from another transaction and the total exceeds EUR 90,000, or the counterparty is registered in a target territory (tikslinė teritorija).
- Keep it in any form and language until VMI asks. Hand it over within **30 days** of the request; VMI may require a Lithuanian translation (paras. 90, 91).
- If the documentation was not ready on time and must be produced later, the comparables search must also use data of the year of the transaction (para. 92).
- Refresh: transaction data every year; the rest of the local file and the database search at least every 3 years while the conditions and the market do not change (paras. 88, 89). Keep everything for at least 5 calendar years from the year after the transaction (para. 94).

Taxpayers below the thresholds have no formal file to prepare, but still carry the arm's length rule and must be able to support their prices (para. 19).

**FR0528, the related-party transactions report.** An annex to the annual corporate income tax return (PMĮ art. 50(2)(1)). VMI's answer KM1402 says it is filed by Lithuanian entities and Lithuanian PEs that, with an associated person in the tax period:

- made a transaction worth EUR 90,000 or more; or
- made transactions, of the same or different kinds, totalling EUR 90,000 or more; or
- gave or received loans whose balance was EUR 90,000 or more on any day.

Values are without VAT. Dividends, donations, group loss transfers, advance payments, wages, goodwill, capital contributions and reductions, and liquidation distributions are left out and not counted towards the EUR 90,000. It is due with the annual return, by the 15th day of the sixth month after the period ends; for a final period, within 30 days of ceasing activity (KM1402; PMĮ art. 51(2)).

**Annual corporate return.** Due by the 15th day of the sixth month after the end of the tax period (PMĮ art. 51(2)).

**Advance pricing agreement (išankstinis kainodaros suderinimas), MAĮ art. 37-2.**

- Available for a future transaction (or group of transactions) with an associated person that starts after the request is filed. A request cannot be about the amount of tax (art. 37-2(1)).
- The request describes the transaction, the parties' obligations, risks and assets, the method, the comparables, the price or range, and the critical assumptions (art. 37-2(1)).
- VMI decides within 90 days, extendable once by 90 days (art. 37-2(2)). It can approve, amend with the taxpayer's agreement, or refuse with reasons (art. 37-2(3)).
- An approved APA binds VMI (art. 37-2(4)). It lasts for the period in the request but no longer than the current year plus 5 calendar years, and ends earlier if the law it relies on changes (art. 37-2(5)). It can be amended when conditions shift without breaking the critical assumptions (art. 37-2(7)).
- To renew an APA whose conditions will not change, apply at least 180 days before it ends (art. 37-2(8)). While an APA runs, the taxpayer files an annual report on how it is applied (art. 37-2(10)).
- A request can ask VMI to agree a bilateral or multilateral APA with a treaty partner's competent authority; the article then applies with the necessary changes (art. 37-2(11)). Such a request can cover past periods with the same facts, within the 5-year window of MAĮ art. 68(4) (art. 37-2(12)). The Law on resolution of double taxation disputes can override the validity rule (art. 37-2(5)).
- Article 37-2 was amended by Law No. XV-309 of 19 June 2025.

**Country-by-country report (ataskaita apie TĮG dalyvius), MAĮ art. 61.** Applies to groups whose consolidated revenue was EUR 750 million or more in the financial year before the reporting year (art. 61(2)). A Lithuanian reporting entity files with VMI within **12 months** after the end of the reporting year (art. 61(3)). VMI sets the filing procedure (art. 61(4)).

## Penalties and interest

- **Fine on adjusted tax.** If a tax audit finds that tax was understated, the shortfall is assessed with a fine of **20% to 100%** of it (MAĮ art. 139(1)). VMI starts from the midpoint (60%) and moves down for mitigating circumstances (admitting the breach, cooperating, repairing the damage) or up for aggravating ones (MAĮ art. 140(3) to (5)).
- **Missing or poor TP documents make it worse.** It is an aggravating circumstance when the taxpayer does not give VMI proper documents on transaction values in time, or gives improper ones, and VMI then adjusts under PMĮ art. 40 (MAĮ art. 140(4)(3)). Avoiding cooperation in an audit is another (art. 140(4)(4)).
- **Repeat offence.** A second fine for a breach of the same tax law within the 5-year window doubles (MAĮ art. 139(3)).
- **Voluntary correction.** No fine is imposed when the taxpayer files a corrected return before VMI issues the order to audit it (MAĮ art. 139(4)).
- **Late payment interest (delspinigiai).** Charged on tax found in an audit from the day after the original due date until the audit report date, and again if the tax is not paid on time after it (MAĮ art. 96(1)(2), 97(2)). It runs for no more than 180 days from the date enforced collection becomes possible (art. 98(2)). The rate is the yield on 12-month government securities on the last working day of the previous quarter plus 7 points, set by the Minister of Finance (art. 99). From 1 August 2026 it is **0.027% a day** (VMI answer KM2633, citing Minister of Finance Order 1K-246 of 28 July 2026).
- **Time limit.** Normally tax can be assessed or recalculated for the current year and the 3 previous calendar years (MAĮ art. 68(1)). For an adjustment under PMĮ art. 40(2) it is the current year and 5 previous calendar years, limited to the TP point (art. 68(4)(4)).
- **Relief.** VMI may waive a fine where the taxpayer proves it was not at fault, events were beyond its control, there was no loss to the budget, or it relied on wrong official guidance (MAĮ art. 141(1)).

## Cross-border points

- **Treaties and disputes.** Article 9 (associated enterprises) of Lithuania's tax treaties applies the same arm's length rule. A taxpayer facing double taxation after an adjustment can use the treaty's mutual agreement procedure and, inside the EU, the EU Arbitration Convention or the procedures of Lithuania's Law on resolution of double taxation disputes, which MAĮ art. 37-2(5) names.
- **OECD Guidelines.** The Rules recommend the OECD Transfer Pricing Guidelines to the extent they do not conflict with the Rules (para. 96).
- **Domestic exemption from documentation, not from the rule.** A Lithuanian company dealing only with other Lithuanian entities has no master or local file to prepare (para. 87.1) and can prepare its support later (para. 19), but the prices must still be arm's length.
- **Target territories.** The EUR 90,000 documentation exemption never covers a transaction with an associated person registered in a target territory (para. 87.2.3). A target territory is a state or zone on the Minister of Finance's list; it is listed if it meets at least two criteria, among them a comparable tax rate below 75% of the 17% rate, no effective exchange of information, or a ruling with the controlled entity on its rate or base (PMĮ art. 2(38)).
- **Moving assets or activity abroad (exit tax).** A transfer of assets out of Lithuania without a change of owner, or a move of the business abroad, is taxed on the gain to market price at the moment of transfer. For transfers to qualifying EEA states the tax can be spread over 5 years (PMĮ art. 40-2). No cross-border skill in this pack covers it yet.
- **Permanent establishments.** A foreign entity's Lithuanian PE is a taxpayer under the Rules (para. 2) and has its own master file and local file thresholds (paras. 84, 85.4).

## Worked examples

### Example 1: VMI cuts a management fee paid to a foreign parent

A Lithuanian UAB pays its Estonian parent a management fee of EUR 500,000 for 2026 and deducts it in full. In a 2028 audit VMI benchmarks the services and finds an arm's length range whose median is EUR 380,000. The fee is outside the range, so VMI adjusts to the median (Rules para. 56). The UAB had no local file ready, although its 2025 revenue was above EUR 3 million.

1. Adjustment to taxable profit: EUR 500,000 minus EUR 380,000 = EUR 120,000 (PMĮ art. 40(2)).
2. Extra corporate income tax at 17%: EUR 20,400 (PMĮ art. 5(1)).
3. Fine range 20% to 100% of EUR 20,400: EUR 4,080 to EUR 20,400 (MAĮ art. 139(1)). VMI starts from the midpoint of 60%: EUR 12,240 (art. 140(5)(1)). The missing documentation is an aggravating circumstance (art. 140(4)(3)), so VMI sets the fine above EUR 12,240 unless mitigating circumstances outweigh it.
4. Late payment interest runs from 16 June 2027, the day after the 2026 tax was due, at the rate in force for each day. At 0.027% a day, 100 days of interest on EUR 20,400 is EUR 550.80. The rate is reset each quarter, so the real figure is computed day by day.
5. The adjustment is within the window: 2026 is within the current year (2028) and the 5 previous years (MAĮ art. 68(4)(4)).
6. To remove the double taxation the group can start the mutual agreement procedure under the Lithuania-Estonia treaty or use the EU Arbitration Convention.

```oa-check
name: Management fee cut to the median on audit (2026 profit)
inputs:
  fee_paid: 500000
  median: 380000
  cit_rate: 17
  fine_min_pct: 20
  fine_max_pct: 100
  interest_daily_pct: 0.027
  days: 100
steps:
  - adjustment: fee_paid - median
  - extra_tax: adjustment * cit_rate / 100
  - fine_min: extra_tax * fine_min_pct / 100
  - fine_max: extra_tax * fine_max_pct / 100
  - fine_mid: (fine_min + fine_max) / 2
  - interest_100_days: extra_tax * interest_daily_pct / 100 * days
expected:
  adjustment: 120000
  extra_tax: 20400
  fine_min: 4080
  fine_max: 20400
  fine_mid: 12240
  interest_100_days: 550.80
```

### Example 2: which file is due, and an IT support charge above the 5% mark-up

A Lithuanian UAB in an international group had revenue of EUR 4,200,000 in 2025. In 2026 it buys IT support from a Polish group company. The provider's cost base for the service is EUR 200,000 and it charges cost plus 15%. The service meets the low value-adding definition (Rules para. 3.1) and is not bought from third parties. The UAB also rents a car from a Latvian group company for EUR 30,000 a year, its only deal with that company.

1. Which file: revenue of EUR 4,200,000 is above EUR 3,000,000, so a local file is due (para. 85.1). It is below EUR 15,000,000, so no master file (para. 84).
2. The car rental is EUR 30,000, not above EUR 90,000, is not repeated or linked, and the Latvian company is not in a target territory. It is left out of the local file (para. 87.2). The rent must still be at arm's length.
3. The IT charge: EUR 200,000 plus 15% = EUR 230,000. The simplified price at cost plus 5% is EUR 210,000 (para. 76-1), and the 5% needs no benchmark. The 15% does: without a benchmark that supports it, the EUR 20,000 above the simplified price is the amount at risk in an audit.
4. Tax at risk on the excess at 17%: EUR 3,400.
5. FR0528: the IT purchase of EUR 230,000 is EUR 90,000 or more, so it goes in the report filed with the 2026 return by 15 June 2027 (VMI KM1402).
6. The local file is ready by 15 June 2027 and handed over within 30 days of a VMI request (paras. 19, 91).

```oa-check
name: Local file test and IT support above the 5% safe mark-up (2026)
inputs:
  revenue_2025: 4200000
  local_file_test: 3000000
  master_file_test: 15000000
  service_cost: 200000
  markup_charged_pct: 15
  markup_simplified_pct: 5
  car_rent: 30000
  doc_exemption: 90000
  cit_rate: 17
steps:
  - over_local_test: revenue_2025 - local_file_test
  - below_master_test: master_file_test - revenue_2025
  - charge: service_cost * (1 + markup_charged_pct / 100)
  - simplified_price: service_cost * (1 + markup_simplified_pct / 100)
  - excess: charge - simplified_price
  - tax_at_risk: excess * cit_rate / 100
  - car_headroom: doc_exemption - car_rent
expected:
  over_local_test: 1200000
  below_master_test: 10800000
  charge: 230000
  simplified_price: 210000
  excess: 20000
  tax_at_risk: 3400
  car_headroom: 60000
```

## Ask the client first

1. Who the associated persons are: the ownership chain with percentages (direct and indirect, on any day of this or the prior period), shared managers, guarantees, profit-transfer or asset-use arrangements, and family links.
2. Each transaction with each associated person in the period: type, amount without VAT, loan balances, and whether the counterparty is Lithuanian, foreign, or in a target territory.
3. Revenue in the prior period, whether the company is a bank, financial company or insurer, and whether it belongs to an international group. These decide the master file and local file.
4. How each price was set: the method, any benchmark, any group TP policy, and whether services claimed as low value-adding meet para. 3.1.
5. Whether the group's consolidated revenue reached EUR 750 million, and whether any APA, mutual agreement procedure or VMI audit is open.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law on Corporate Income Tax No. IX-675, consolidated version from 19 May 2026: art. 2(7), 2(8), 2(33), 2(38), 5(1), 40, 40-2 (exit), 50, 51, 53 | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr | 2026-10-23 |
| Minister of Finance Order No. 1K-123, Rules implementing PMĮ art. 40(2) and GPMĮ art. 15(2), consolidated version from 1 January 2021: paras. 2 to 96 | https://www.e-tar.lt/portal/lt/legalAct/TAR.55EC668C883A/asr | 2026-10-23 |
| Law on Tax Administration No. IX-2112, consolidated version from 1 July 2026: art. 37-2, 61, 68, 96 to 99, 139 to 141 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr | 2026-10-23 |
| VMI, corporate income tax rates (art. 5) | https://www.vmi.lt/evmi/tarifai-5-str.- | 2026-10-23 |
| VMI, transaction value adjustment (art. 40), page naming Order 1K-123 | https://www.vmi.lt/evmi/sandoriu-vertes-koregavimas-pajamu-apibudinimas-is-naujo | 2026-10-23 |
| VMI, FR0528 report, answer KM1402 (who files, EUR 90,000, deadline, exclusions) | https://www.vmi.lt/evmi/asocijuot%C5%B3-asmen%C5%B3-tarpusavio-sandori%C5%B3-arba-%C5%ABkini%C5%B3-operacij%C5%B3-ataskaita-fr0528- | 2026-10-23 |
| VMI, late payment interest, answer KM2633 (0.027% a day from 1 August 2026) | https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.- | 2026-10-23 |

Not yet confirmed: the text of the FR0528 form and rules that apply to 2026 returns (VMI's answer KM1402, dated 16 July 2024, cites VMI order VA-27 of 2005; a search shows VA-27 still in force in a consolidated version from 1 January 2026 as amended by order VA-78 of 4 September 2025, but that text sits behind a CAPTCHA on e-seimas.lrs.lt and was not read); whether the FR0528 EUR 90,000 total is counted per associated person or across all of them; the late payment interest rate after 31 October 2026 (it is reset each quarter); the VMI procedure, form and any fee for an APA request, and whether VMI charges for bilateral APAs; the country-by-country notification duty, the VMI filing rules and the penalty for not filing; any separate administrative fine for not preparing or not handing over TP documentation; the Minister of Finance's list of target territories in force for 2026; whether Lithuania makes a secondary adjustment (for example a deemed dividend) after a primary TP adjustment; and the procedure for a downward corresponding adjustment after a foreign adjustment.

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
