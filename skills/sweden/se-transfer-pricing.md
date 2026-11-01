---
name: se-transfer-pricing
description: "Swedish transfer pricing (internprissättning) for companies with cross-border related-party transactions, tax year 2026. Covers the arm's length rule in Inkomstskattelagen 14 kap. 19-20 §§ (korrigeringsregeln) and what counts as ekonomisk intressegemenskap; the documentation duty in Skatteförfarandelagen 39 kap. 15-16 f §§ and Skatteförfarandeförordningen 9 kap. 9-19 §§ (group part and company part, the 250 employees / SEK 450 million / SEK 400 million exemption, the SEK 5 million immaterial-transaction rule, timing, language, seven-year retention); country-by-country reports (SFL 33 a kap., SEK 7 billion, twelve months, notification); prissättningsbesked (APA) fees; MAP and the EU dispute law 2019:601; skattetillägg and reopening periods. Trigger on: internprissättning, transfer pricing Sweden, armlängdsprincipen, korrigeringsregeln, master file, local file, land-för-land-rapport, CbCR Sweden, prissättningsbesked, APA Sweden, ömsesidig överenskommelse. Out of scope: corporate tax computation and interest limitation (se-corporate-tax), cross-border individuals and exit tax (se-cross-border), VAT (sweden-vat-return)."
version: 0.2
jurisdiction: SE
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden: transfer pricing (internprissättning), tax year 2026

> **General reference only.** A source-cited draft, not reviewed by an accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Sweden.

Sweden taxes related-party prices through one adjustment rule in Inkomstskattelagen (1999:1229), "IL" below, and a documentation duty in Skatteförfarandelagen (2011:1244), "SFL" below, filled in by Skatteförfarandeförordningen (2011:1261), "SFF" below. All three were read on 2026-10-23 in the consolidated text on riksdagen.se (IL to SFS 2026:1393, SFL to SFS 2026:1305, SFF to SFS 2026:1570). The tax authority is Skatteverket. Amounts are in Swedish kronor (SEK).

See also, in this pack: `se-corporate-tax` (the 20.6% rate, the taxable base, the interest limitation rules in IL 24 kap., filing dates, kostnadsränta), `se-cross-border` (non-residents, treaties, exit tax), `sweden-bookkeeping` (annual accounts). This skill does not repeat them.

## Who this applies to

- **The adjustment rule (IL 14 kap. 19 §).** Where terms that independent parties would not have agreed lower a business's result, the result is computed as if those terms did not exist (the law says "ska": the adjustment is mandatory), when all three conditions hold:
  1. the counterparty that gains from the terms is not taxed on that gain in Sweden, under IL or because of a tax treaty;
  2. there are probable reasons (sannolika skäl) to assume ekonomisk intressegemenskap between the parties; and
  3. the circumstances do not show that the terms arose for reasons other than that community of interest.
- Condition 1 makes the rule cross-border in practice. Prices between two Swedish taxpayers are dealt with under the withdrawal (uttag) and other rules covered in `se-corporate-tax`, not under 14 kap. 19 §.
- **Ekonomisk intressegemenskap (IL 14 kap. 20 §)** exists when one business, directly or indirectly, takes part in the management or control of the other or owns part of its capital, or when the same persons do so in both. There is no ownership percentage. Any shareholding or management link is enough.
- **Who must document (SFL 39 kap. 16 §).**
  1. A Swedish-resident legal person with transactions with a non-resident company in intressegemenskap;
  2. a Swedish handelsbolag with such transactions, where its result is taxed in Swedish-resident legal persons in intressegemenskap with it and the foreign company;
  3. a Swedish-resident legal person with a permanent establishment (fast driftställe) abroad;
  4. a Swedish handelsbolag with a fast driftställe abroad, where its result is taxed in Swedish-resident legal persons in intressegemenskap with it; and
  5. a foreign legal person taxed on income from a fast driftställe in Sweden.
- For the documentation rules, intressegemenskap means parent and subsidiary, or companies under mainly common management (SFL 39 kap. 2 a §). This is narrower than IL 14 kap. 20 §. A company outside the documentation duty can still be adjusted under IL 14 kap. 19 §.
- **Individuals are out of scope** of the documentation duty: it applies to legal persons and handelsbolag only.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Tax on an upward transfer pricing adjustment | 20.6% corporate income tax on the extra income (see `se-corporate-tax`) | 2026 | IL 65 kap. 10 §, https://data.riksdagen.se/dokument/sfs-1999-1229.text |
| Exemption from documentation: employees | Group (intressegemenskap) has fewer than 250 employees in the year before the tax year | 2026 | SFL 39 kap. 16 a §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Exemption from documentation: size | And either turnover of not more than SEK 450,000,000 or a balance sheet total of not more than SEK 400,000,000, for the whole group, in the year before the tax year | 2026 | SFL 39 kap. 16 a §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Immaterial transactions, local file | Transactions with one non-resident related company (or attributable to one fast driftställe) totalling less than SEK 5,000,000 in the financial year always count as immaterial. Does not cover licensing or transfer of intangibles that matter to the business | 2026 | SFL 39 kap. 16 c §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Documentation languages | Swedish, Danish, Norwegian or English | 2026 | SFL 39 kap. 16 e §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Retention of documentation | Seven years after the end of the calendar year in which the tax year ended | 2026 | SFF 9 kap. 19 §, https://data.riksdagen.se/dokument/sfs-2011-1261.text |
| Country-by-country report: threshold | Groups with consolidated revenue of SEK 7,000,000,000 or more in the year before the reported year. A Swedish group member of a foreign-parented group is exempt if the parent is exempt at home because revenue is below EUR 750 million or the local equivalent | 2026 | SFL 33 a kap. 6 §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Country-by-country report: deadline | Within 12 months after the end of the reported financial year | 2026 | SFL 33 a kap. 11 §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Country-by-country notification | Before the end of the reported financial year | 2026 | SFL 33 a kap. 12 §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| APA fee, new application | SEK 150,000 per foreign state covered | 2026 | Förordning (2009:1295) 7-8 §§, https://data.riksdagen.se/dokument/sfs-2009-1295.text |
| APA fee, renewal | SEK 100,000 per foreign state | 2026 | Förordning (2009:1295) 7-8 §§, https://data.riksdagen.se/dokument/sfs-2009-1295.text |
| APA fee, renewal with changes | SEK 125,000 per foreign state | 2026 | Förordning (2009:1295) 7-8 §§, https://data.riksdagen.se/dokument/sfs-2009-1295.text |
| APA term | Three to five tax years, unless special reasons | 2026 | Lag (2009:1289) 15 §, https://data.riksdagen.se/dokument/sfs-2009-1289.text |
| MAP request | No fee | 2026 | Skatteverket, Undanröjande av dubbelbeskattning, https://www.skatteverket.se/foretagochorganisationer/skatter/internationellt/dubbelbeskattning/undanrojandeavdubbelbeskattning.106.233f91f71260075abe8800018011.html |
| EU dispute resolution request | Within three years of being notified of the measure causing the dispute | 2026 | Lag (2019:601) 2 kap. 2 §, https://data.riksdagen.se/dokument/sfs-2019-601.text |
| Skattetillägg on an incorrect return | 40% of the tax that would have been avoided; 10% if the error only puts income in the wrong year | 2026 | SFL 49 kap. 11 §, 13 §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Ordinary reassessment period (to the taxpayer's detriment) | Two years from the end of the calendar year in which the tax year ended | 2026 | SFL 66 kap. 21 §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Extended reassessment (efterbeskattning) | Six years from the end of that calendar year, for example where the return contained an oriktig uppgift | 2026 | SFL 66 kap. 27 §, https://data.riksdagen.se/dokument/sfs-2011-1244.text |

## The taxable base

**The adjustment.** When IL 14 kap. 19 § applies, the result is recomputed as if arm's length terms had been agreed. The adjustment is the difference between the agreed price and the arm's length price. It is added to taxable income and taxed at 20.6% with the rest of the company's income (`se-corporate-tax`). The rule only raises a Swedish result. It never lowers one.

**Burden.** Skatteverket needs "probable reasons" for intressegemenskap (condition 2). The taxpayer escapes the rule if the circumstances show the terms were set for other reasons (condition 3).

**What the documentation must show (SFL 39 kap. 15 §).** Enough to judge whether terms between related companies, or between a company and its fast driftställe, depart from arm's length terms, lead to income being exempted or foreign tax being credited, and whether the right income has been attributed to the fast driftställe.

**Two parts (SFL 39 kap. 16 b §).**
- **Group part (koncerngemensam del, the master file).** An overview of the group and its business (SFF 9 kap. 9-14 §§): ownership chart; value drivers; supply chain for the five largest products or services and any above 5% of group turnover; main markets; shared service functions and how they are priced; a short functional analysis; restructurings; intangibles strategy, owners and key agreements; intra-group financing; the consolidated accounts; and a list of the group's APAs and other rulings on profit allocation.
- **Company part (företagsspecifik del, the local file).** The company and each important type of related-party transaction (SFF 9 kap. 15-17 §§): management structure; business strategy; competitors; transaction descriptions and amounts; parties; copies of key contracts; functional and comparability analysis; the method chosen and why; the tested party; key assumptions; comparables and search; adjustments; why the result is at arm's length; the annual report and a reconciliation of the financial data used; and foreign APAs touching the transactions. Information already in the group part need not be repeated; a cross-reference is enough (SFF 9 kap. 18 §). The older SEK 25 million simplified-documentation threshold is not in SFL 39 kap. or SFF 9 kap. as in force (searched 2026-10-23); the only size tests are the 16 a § exemption and the 16 c § SEK 5,000,000 rule.

**What can be left out of the company part (SFL 39 kap. 16 c §).** Immaterial transactions. Transactions with one non-resident related company totalling less than SEK 5,000,000 in the financial year always count as immaterial. The same SEK 5,000,000 test applies to transactions attributed to a fast driftställe. The carve-out does not apply to licensing or transfer of an intangible unless the intangible itself is immaterial to the business.

**Interest on related-party debt.** The price of intra-group loans is tested under IL 14 kap. 19 §. Separately, IL 24 kap. 18-19 a §§ can deny the deduction for interest paid to a lender in intressegemenskap, and the general 30% EBITDA limit applies on top. Both are in `se-corporate-tax`. The IL 24 kap. 10 a-10 f §§ rules were repealed by SFS 2018:1206 and no longer apply.

## Deadlines and filing

- **Company part:** must be ready when the company's income tax return (Inkomstdeklaration 2) is due, or, for a handelsbolag in cases 2 and 4 above, when its special information is due (SFL 39 kap. 16 d §). Filing dates by year end are in `se-corporate-tax`.
- **Group part:** must be ready no later than the date the parent company must file its own income tax return (SFL 39 kap. 16 d §).
- **Not filed with the return.** The documentation is handed to Skatteverket on request (SFL 39 kap. 16 f §). The law sets no fixed number of days for handing it over.
- **Country-by-country report:** filed with Skatteverket within 12 months after the end of the reported financial year (SFL 33 a kap. 11 §). A Swedish parent of a multinational group files it (33 a kap. 4 §). A Swedish group member files it only when the foreign parent does not have to file at home, the parent's state has no exchange agreement with Sweden in force, or Skatteverket has told the entity of a systemic failure in that state (33 a kap. 5 §).
- **Country-by-country notification:** every Swedish entity of an in-scope group tells Skatteverket, before the end of the reported financial year, whether it is the parent or the surrogate parent or must report, or else which group entity reports and where it is resident (SFL 33 a kap. 8-9, 12 §§).
- **APA (prissättningsbesked):** written application to Skatteverket; the fee is paid on application, and an application whose fee is not paid after a reminder is rejected (Förordning 2009:1295, 9 §). An APA is given only once a mutual agreement has been reached with the other state, which must be a treaty partner (Lag 2009:1289, 13 §). Skatteverket offers a pre-filing meeting (förmöte) (Lag 2009:1289, 9 §). Skatteverket may waive all or part of the fee for special reasons (Lag 2009:1289, 24 §). An APA cannot be appealed (25 §).

## Penalties and interest

- **No separate documentation penalty.** SFL has no fixed fee for missing or late transfer pricing documentation. The cost of having none is practical: Skatteverket can estimate the result, and skattetillägg follows the rules below.
- **Skattetillägg.** 40% of the tax that would have been avoided if an oriktig uppgift (incorrect information) in the return had been accepted (SFL 49 kap. 4, 11 §§); 10% where the error only shifts income to the wrong year (49 kap. 13 §); 40% on tax raised by an estimated assessment (skönsbeskattning) (49 kap. 15 §).
- **When there is no oriktig uppgift.** Information is not oriktig if, together with the other information given, it was enough for a correct decision (SFL 49 kap. 5 § second paragraph). So if the return and its attachments set out the related-party transaction openly and the dispute is only about the arm's length price, the 40% does not follow automatically. Ask what was disclosed before applying it.
- **Other exits.** No skattetillägg if the company corrects the return on its own initiative, or the amount is insignificant (SFL 49 kap. 10 §). Skatteverket must remit it in full or in part where charging it in full would be unreasonable, for example where the error came from a misjudgement of a rule or of the facts (SFL 51 kap. 1 §).
- **Reopening.** Skatteverket may reassess to the company's detriment within two years from the end of the calendar year in which the tax year ended (SFL 66 kap. 21 §). Where the company gave an oriktig uppgift, or the change follows from a decision on an APA, the period is six years (efterbeskattning, SFL 66 kap. 27 § 1 and 4 f).
- **Interest.** Extra tax from an adjustment is final tax. Kostnadsränta at the basränta runs from the 13th of the second month after the tax year ends (SFL 65 kap. 4, 8-9 §§), and at the basränta plus 15 percentage points on any amount not paid by its due date (65 kap. 13 §). The rates (basränta 2.5% from 1 December 2024; 17.5% after the due date) are in `se-corporate-tax`. Kostnadsränta is not deductible.

## Cross-border points

- **Mutual agreement procedure (MAP).** A company taxed twice because of an adjustment in Sweden or abroad asks Skatteverket, as competent authority, for a mutual agreement under the tax treaty. Many Swedish treaties require the request within three years of learning of the measure; not all treaties have that limit. Applying is free. A pending Swedish court case does not stop a MAP request, but the treaty deadline still runs (Skatteverket, Undanröjande av dubbelbeskattning).
- **Inside the EU.** Two further routes: the EU Arbitration Convention (90/436/EEC) for transfer pricing and permanent establishment cases, and Lag (2019:601), which implements Directive (EU) 2017/1852. Under Lag 2019:601 the request goes to Skatteverket within three years of notice of the measure (2 kap. 2 §); Skatteverket decides whether to accept it within six months (2 kap. 5 §). If the authorities do not agree within two years, or three after an extension, Skatteverket tells the applicant (3 kap. 6 §), who may then ask for an advisory commission (4 kap. 1 §). The law applies to tax years beginning after 31 December 2017 and to requests filed after 30 June 2019 (transitional provisions to Lag 2019:601). Filing under Lag 2019:601 closes any treaty MAP on the same issue (Skatteverket, Undanröjande av dubbelbeskattning).
- **Corresponding adjustment.** Sweden lowers a Swedish result after a foreign adjustment on a request to Skatteverket as competent authority. Skatteverket first checks whether it can resolve the case alone (unilaterally); if not, it opens a mutual agreement procedure. When an agreement lowers Swedish tax, Skatteverket makes the reduction itself, no new return is needed, and any skattetillägg falls in proportion. Secondary adjustments are outside MAP. A company can ask for anstånd (deferral) of Swedish tax while the case runs, once the foreign tax is paid (Skatteverket, Undanröjande av dubbelbeskattning). A Swedish reassessment needed to give effect to an APA decision can be made within six years (SFL 66 kap. 27 § 4 f).
- **Permanent establishments.** Profit attribution between a Swedish company and its fast driftställe abroad, or a foreign company and its Swedish fast driftställe, falls within the documentation duty (SFL 39 kap. 15-16 §§).
- **Pillar Two.** Groups with revenue of EUR 750 million or more also fall under Lag (2023:875) om tilläggsskatt; see `se-corporate-tax`.

## Worked examples

**Example 1: an above-arm's-length management fee.** Fjällvik AB, Stockholm, is wholly owned by a German GmbH. In calendar year 2026 it pays the parent a management fee of SEK 6,000,000, deducted in full. Its benchmarking shows independent parties would have paid SEK 3,500,000 for the same services. The parent is not taxed in Sweden on the fee and owns Fjällvik's capital, so all three conditions in IL 14 kap. 19 § hold. Skatteverket adds SEK 2,500,000 to taxable income. At 20.6% the extra tax is SEK 515,000. If the return left out facts needed for a correct decision, skattetillägg is 40% of SEK 515,000, SEK 206,000 (SFL 49 kap. 11 §). If the return and its attachments set out the fee and its basis well enough for a correct decision, the information is not oriktig and no skattetillägg is charged (SFL 49 kap. 5 § second paragraph); so ask what was disclosed before applying the 40%. Kostnadsränta comes on top. The German parent's way to avoid double tax is a MAP request or the EU dispute route.

```oa-check
name: SE TP example 1, management fee above arm's length, 2026
inputs:
  fee_paid: 6000000
  arm_length_fee: 3500000
  corporate_rate_pct: 20.6
  skattetillagg_pct: 40
steps:
  - adjustment: fee_paid - arm_length_fee
  - extra_tax: pct(adjustment, corporate_rate_pct)
  - skattetillagg: pct(extra_tax, skattetillagg_pct)
  - total_if_incorrect_return: extra_tax + skattetillagg
expected:
  adjustment: 2500000
  extra_tax: 515000
  skattetillagg: 206000
  total_if_incorrect_return: 721000
```

**Example 2: does a mid-size group need documentation, and what goes in the local file?** Nordbro AB is the Swedish subsidiary of a Danish-parented group. For 2025 (the year before tax year 2026) the whole group had 180 employees, turnover of SEK 520,000,000 and a balance sheet total of SEK 380,000,000. The SEK 450 million turnover test fails, but the balance sheet is not more than SEK 400 million and there are fewer than 250 employees, so the group is exempt for 2026 (SFL 39 kap. 16 a §). The arm's length rule still applies.

Suppose instead the group had 260 employees. Then no exemption. In 2026 Nordbro has these transactions: SEK 4,200,000 of IT services from a Danish sister company; SEK 12,000,000 of goods bought from the Danish parent; and a SEK 1,500,000 royalty to the parent for a trade mark that is central to its sales. The IT services total less than SEK 5,000,000 with that company and count as immaterial. The goods purchases from the parent must be documented. The royalty is also paid to the parent, so the parent's total is SEK 13,500,000, above SEK 5,000,000; and even alone it would not be immaterial, because a licence of an important intangible is outside the carve-out (SFL 39 kap. 16 c §). The local file covers SEK 13,500,000 of the SEK 17,700,000 total.

In the check block, a test result of 1 means "met" and 0 means "not met". Each test uses whole kronor or whole employees.

```oa-check
name: SE TP example 2, documentation exemption test and local-file scope, 2026
inputs:
  employees: 180
  turnover: 520000000
  balance_sheet: 380000000
  employees_alt: 260
  it_services_sister: 4200000
  goods_parent: 12000000
  royalty_parent: 1500000
steps:
  - employees_test: clamp(250 - employees, 0, 1)
  - turnover_test: clamp(450000000 - turnover + 1, 0, 1)
  - balance_test: clamp(400000000 - balance_sheet + 1, 0, 1)
  - exempt: employees_test * max(turnover_test, balance_test)
  - exempt_alt: clamp(250 - employees_alt, 0, 1) * max(turnover_test, balance_test)
  - parent_total: goods_parent + royalty_parent
  - sister_material: clamp(it_services_sister - 5000000 + 1, 0, 1)
  - documented: parent_total + it_services_sister * sister_material
  - total_related: parent_total + it_services_sister
expected:
  employees_test: 1
  turnover_test: 0
  balance_test: 1
  exempt: 1
  exempt_alt: 0
  parent_total: 13500000
  sister_material: 0
  documented: 13500000
  total_related: 17700000
```

## Ask the client first

1. Which related companies abroad does the Swedish company deal with, how is each related (shares, management), and where is each resident? This decides whether IL 14 kap. 19 § and the documentation duty apply.
2. For the year before the tax year: the whole group's employees, turnover and balance sheet total. This decides the SFL 39 kap. 16 a § exemption.
3. The value of each year's transactions with each related company, and whether any involve licensing or selling an intangible. This sets the SEK 5,000,000 carve-out.
4. The group's consolidated revenue for the prior year, who the ultimate parent is and where. This decides country-by-country reporting and the notification.
5. When the parent files its own return. The group part must exist by then.
6. Has any foreign tax authority adjusted the same transactions, or is an APA in place or wanted? This decides whether MAP, the EU route or an APA is the next step.

## Sources

| Source | URL | Read on |
|---|---|---|
| Inkomstskattelag (1999:1229), consolidated to SFS 2026:1393 (14 kap. 19-20 §§, 24 kap. 10 a-10 f, 16-19 a §§, 65 kap. 10 §) | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-10-23 |
| Skatteförfarandelag (2011:1244), consolidated to SFS 2026:1305 (33 a kap.; 39 kap. 2 a, 15-16 f §§; 49 kap. 4-15 §§; 51 kap. 1 §; 65 kap. 3-4, 8-9, 13 §§; 66 kap. 21, 27 §§) | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-10-23 |
| Skatteförfarandeförordning (2011:1261), consolidated to SFS 2026:1570 (9 kap. 9-19 §§) | https://data.riksdagen.se/dokument/sfs-2011-1261.text | 2026-10-23 |
| Lag (2009:1289) om prissättningsbesked vid internationella transaktioner | https://data.riksdagen.se/dokument/sfs-2009-1289.text | 2026-10-23 |
| Förordning (2009:1295) om prissättningsbesked vid internationella transaktioner (7-9 §§, fees) | https://data.riksdagen.se/dokument/sfs-2009-1295.text | 2026-10-23 |
| Lag (2019:601) om tvistlösningsförfarande i ärenden som rör skatteavtal inom Europeiska unionen | https://data.riksdagen.se/dokument/sfs-2019-601.text | 2026-10-23 |
| Skatteverket: Internprissättning och vinstallokering | https://www.skatteverket.se/foretag/internationellt/internprissattningochvinstallokering.4.3dfca4f410f4fc63c8680005982.html | 2026-10-23 |
| Skatteverket: Ansökan om prissättningsbesked | https://www.skatteverket.se/foretag/internationellt/ansokanomprissattningsbesked.4.58d555751259e4d661680003946.html | 2026-10-23 |
| Skatteverket: Undanröjande av dubbelbeskattning (MAP, Arbitration Convention, Lag 2019:601) | https://www.skatteverket.se/foretagochorganisationer/skatter/internationellt/dubbelbeskattning/undanrojandeavdubbelbeskattning.106.233f91f71260075abe8800018011.html | 2026-10-23 |

Not yet confirmed: how many days Skatteverket gives to hand over documentation on request in practice (the law sets no period); which treaties lack a three-year MAP deadline; the Swedish statute implementing the EU Arbitration Convention (90/436/EEC) was not read.

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
