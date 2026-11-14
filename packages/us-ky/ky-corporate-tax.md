---
name: ky-corporate-tax
description: "Kentucky corporate income and limited liability entity tax for 2026: C corporations, SMLLC and pass-through routing, both LLET methods, thresholds, credit, ordinary base and filing."
version: "0.1"
jurisdiction: US-KY
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
tier: 2
type: computation
---

# Kentucky corporate income tax and LLET, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

**Answer first.** A Kentucky C corporation generally computes both corporate income tax and LLET. An individually owned disregarded LLC can owe LLET even though its income is on the owner's return. Federal corporate computation belongs to `us-form-1120-c-corp`; the owner's return belongs to `ky-income-tax`.

## Who this applies to

Corporations and limited-liability pass-through entities doing business in Kentucky, subject to the exemptions in KRS 141.040 and 141.0401. Sole proprietorships and ordinary general partnerships have no limited-liability entity tax merely because they conduct a business. A Kentucky entity's short period or lack of profit does not itself remove the minimum tax. A name reservation alone is not entity formation. [DOR entity FAQ](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx); [KRS 141.0401](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941).

This skill covers ordinary corporate net-income computation, LLET gross-receipts/gross-profits comparison and entity/form routing. The most recent annual form read is 2025, the **2025-2026 filing cycle**; current statutory LLET text includes the amendment effective 15 July 2026. Final 2026 form line numbers and later conformity changes remain pending below.

## Rates, bands and thresholds

| Item | Amount and conditions | Official source |
| --- | --- | --- |
| Corporate income tax | 5% of Kentucky taxable net income after allowed Kentucky NOL deduction | [DOR corporate computation](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx) |
| LLET minimum | USD 175 per taxable year, including small-business cases and after credits | [KRS 141.0401(2)(a)](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941) |
| LLET small-business test | If either all-source receipts OR all-source gross profits is USD 3 million or less, minimum only; affiliated-group totals determine eligibility | [KRS 141.0401(2)(b)](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941) |
| Gross receipts method | 0.095% of Kentucky receipts; reduction when all-source receipts exceed USD 3 million but are below USD 6 million | [KRS 141.0401(2)(b)1](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941) |
| Gross profits method | 0.75% of Kentucky gross profits; reduction when all-source profits exceed USD 3 million but are below USD 6 million | [KRS 141.0401(2)(b)2](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941) |
| Receipts reduction | USD 2,850 x (USD 6 million - Kentucky receipts) / USD 3 million in the middle band | [KRS 141.0401(2)(b)1.b](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941) |
| Profits reduction | USD 22,500 x (USD 6 million - Kentucky gross profits) / USD 3 million in the middle band | [KRS 141.0401(2)(b)2.b](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941) |
| Corporate LLET credit | Current LLET liability after relevant credits less USD 175, nonrefundable and limited to related income tax | [KRS 141.0401(3)](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941) |

## The base

**Corporate income.** Start from the federal corporate return, make Kentucky additions/subtractions, allocate nonapportionable income and apportion business income. Ordinary businesses generally use a single receipts factor; specified industries retain special formulas. Add state income taxes deducted federally, reverse federal/Kentucky depreciation differences and related-party items where required, subtract eligible US-obligation interest and dividends, and track Kentucky basis. Do not add back LLET as though it were an income tax. [DOR corporate computation](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx), [FAQ](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx).

The 2025 form's Part I starts with Form 1120 line 28 on line 1, additions on 2-20, subtractions on 22-39, net income line 40, taxable net income 41, Kentucky NOL 42 and taxable net income after NOL 43. Part III computes income tax and LLET credits. These are the verified 2025-2026 filing-cycle lines, not asserted 2026 line numbers. [Form 720](https://revenue.ky.gov/Forms/Form%20720%20%282025%29.pdf). The DOR page describes fixed-date federal conformity through 31 December 2024 for 2025 onward; depreciation remains separately decoupled. A later federal benefit is not automatically a Kentucky benefit.

**Losses and groups.** DOR describes no Kentucky carryback for years beginning from 2005 and post-2018 NOL carryforward/limitation rules. Unitary combined reporting, the alternative consolidated election and group sharing are separate determinations; do not take the federal consolidated result as the Kentucky result. Group losses, related-party addbacks, special industries and post-2024 federal changes require the year-specific instructions and a specialist. [DOR group/NOL section](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx).

**LLET calculation, KRS 141.0401(1)-(3).** Determine Kentucky and all-source receipts/gross profits, including proportionate lower-tier amounts and applicable exempt-organization reductions. All-source amounts select the threshold band. Kentucky amounts enter the multiplication and reduction, including the reduction numerator. Do not accidentally use all-source receipts in that numerator.

1. Compute eligible Kentucky cost of goods sold on Schedule COGS. Only manufacturing, producing, reselling, retailing and wholesaling tangible products qualify; direct qualifying costs differ from federal COGS and indirect labour is excluded. Other activities have no COGS deduction. Kentucky gross profit = adjusted Kentucky receipts minus eligible COGS.
2. If either all-source measure is at most USD 3 million, LLET = USD 175. Otherwise compute each method separately.
3. Receipts method: when all-source receipts are below USD 6 million, calculate Kentucky receipts x 0.00095 minus 2,850 x (6,000,000 - Kentucky receipts)/3,000,000; otherwise Kentucky receipts x 0.00095.
4. Profits method: when all-source profits are below USD 6 million, calculate Kentucky profits x 0.0075 minus 22,500 x (6,000,000 - Kentucky profits)/3,000,000; otherwise Kentucky profits x 0.0075.
5. Take the smaller method, subject to the USD 175 floor, and apply allowable credits without reducing below that floor. Then calculate any LLET credit against corporate tax; do not offset away the minimum. [Current statute](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941), [Form 720 Schedule L](https://revenue.ky.gov/Forms/Form%20720%20%282025%29.pdf).

## Deadlines and filing

| Entity | Return/job | Official source |
| --- | --- | --- |
| Ordinary C corporation or eligible elective consolidated group | Form 720: corporate income and LLET | [DOR form routing](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx) |
| Unitary combined C corporations | Form 720U | [DOR form routing](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx) |
| Individually owned disregarded SMLLC | Form 725 for LLET; owner income separately | [DOR form routing](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx) |
| S corporation, multi-member LLC, limited partnership/LLP | Form PTE, LLET where applicable; special S corporation income tax can still apply | [DOR form routing](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx) |
| Ordinary general partnership | Form PTE informational reporting, no ordinary LLET | [DOR form routing](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx) |

Register tax accounts through the DOR process or Form 10A100 and retain the corporation/LLET account. Use approved e-file software for business returns: MyTaxes accepts payments but is not a direct corporate-return preparation facility. DOR requires e-filing for separate corporations and pass-throughs over its published gross-receipts threshold; determine the current mandate and waiver eligibility. [FAQ](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx); [DOR electronic-filing section](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx).

Prepare Schedule L Sections A/B (Kentucky/all-source amounts), C/D (both methods), E (minimum and lesser method). Transfer to Form 720 Part II line 1, then compute liability and credits, with Part III line 6 reflecting LLET less the minimum. Complete questionnaire, federal return attachment, schedules and signature; submit through supported software, resolve rejections, save acceptance and separately reconcile payment confirmation. [2025 Form 720](https://revenue.ky.gov/Forms/Form%20720%20%282025%29.pdf).

Return and payment are due the 15th day of the fourth month after year end, ordinarily 15 April 2027 for a calendar 2026 return. A valid C corporation filing extension can provide seven months, but does not extend payment. Four calendar corporate estimated instalments are 15 April, 15 June, 15 September and 15 December, ordinarily 25% each; annualization/seasonal methods need the applicable forms. Nonresident-owner withholding is a separate job, Form 740 NP-WH, and not a composite return. [DOR](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx); [FAQ](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx); [KRS 141.0401(4)](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941).

## Penalties and interest

An extension does not stop late-payment charges. Use the DOR penalty/interest notice and current-year estimate computation; final 2026 addition-to-tax computation is pending below. The same DOR notice, now retitled 2027, states the base rate is unchanged from 2026; unpaid tax bears the statutory deficiency adjustment. [FAQ](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx); [interest notice](https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-26.aspx).

## Cross-border points

Income-tax nexus/P.L. 86-272 analysis and LLET are distinct: protection from a net-income tax is not a blanket LLET exemption. Kentucky-source pass-through ownership can require a corporate return even without nonresident corporate withholding. Foreign registration, combined group, market sourcing and special-industry cases must be tested from the entity's facts; do not use the sales-tax threshold as corporate nexus. [FAQ](https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx); [KRS 141.0401](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941).

## Two worked examples that recompute

**Case 1, compare both LLET bases and corporate credit.** A standalone retailer has all-source receipts USD 10 million, profits USD 7 million; Kentucky receipts USD 4 million, profits USD 3.5 million; Kentucky corporate taxable income after allowed NOL USD 100,000, no other credits. Both worldwide measures exceed USD 6 million. Receipts method USD 3,800; profits method USD 26,250; LLET USD 3,800. Corporate tax USD 5,000 less USD 3,625 LLET credit = USD 1,375; total state entity tax USD 5,175. Both methods must be computed, although the receipts method wins.

```oa-check
name: Kentucky LLET two methods and income credit
inputs:
  ky_receipts: 4000000
  ky_profit: 3500000
  income: 100000
steps:
  - receipts_tax: ky_receipts * 0.00095
  - profits_tax: ky_profit * 0.0075
  - llet: max(min(receipts_tax, profits_tax), 175)
  - income_gross: income * 0.05
  - credit: min(max(llet - 175, 0), income_gross)
  - income_net: income_gross - credit
  - total: llet + income_net
expected:
  receipts_tax: 3800
  profits_tax: 26250
  llet: 3800
  credit: 3625
  income_net: 1375
  total: 5175
```

**Case 2, middle-band computation and minimum alternative.** All-source receipts USD 5 million and profits USD 4 million; Kentucky receipts USD 4 million and profits USD 3.5 million. Receipts method: USD 3,800 - USD 1,900 = USD 1,900. Profits method: USD 26,250 - USD 18,750 = USD 7,500. LLET is USD 1,900. If eligible all-source gross profits were instead USD 2.9 million, the small-business test produces USD 175, even with USD 5 million receipts. The factual classification of COGS decides eligibility; it is not an election to invent expenses.

```oa-check
name: Kentucky middle bands and small business boundary
inputs:
  ky_receipts: 4000000
  ky_profit: 3500000
steps:
  - receipts_tax: ky_receipts * 0.00095 - 2850 * (6000000 - ky_receipts) / 3000000
  - profits_tax: ky_profit * 0.0075 - 22500 * (6000000 - ky_profit) / 3000000
  - llet: max(min(receipts_tax, profits_tax), 175)
  - small_business_llet: 175
  - difference: llet - small_business_llet
expected:
  receipts_tax: 1900
  profits_tax: 7500
  llet: 1900
  small_business_llet: 175
  difference: 1725
```

## Ask the client first

1. Entity/legal liability, federal classification, Kentucky formation/registration, year end and short periods?
2. Kentucky activity, property/payroll/receipts and destination, plus all-source receipts and qualifying COGS/gross profits?
3. Affiliates, unitary activities, lower-tier pass-through ownership and exempt owners?
4. Federal return, Kentucky adjustments/basis, NOL history and post-2024 federal tax benefits?
5. Tax accounts, prior filing method/elections, credits, estimated payments, nonresident owners and notices?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR corporate/LLET page. Read for corporate rate, computation, apportionment, group/NOL, estimates and conformity sections. | https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx | 2026-11-13 |
| Current KRS 141.0401. Read for definitions, all LLET calculation bands, credit, exemptions, filing and July 2026 amendment. | https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=57941 | 2026-11-13 |
| DOR entity FAQ. Read for entity/form table, registration, filing deadline, software, LLET deductibility and nonresident withholding. | https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/Corporation-LLC-Pass-Through-Tax-FAQs.aspx | 2026-11-13 |
| DOR Form 720, 2025-2026 filing cycle. Read for Part I, Part II, Part III, Schedule Q and full Schedule L. | https://revenue.ky.gov/Forms/Form%20720%20%282025%29.pdf | 2026-11-13 |

Not yet confirmed: final 2026 Form 720/720U/PTE/725 line numbers, corporate estimate safe-harbour and addition-to-tax detail, later 2026 conformity enactments and post-2024 research-expensing adjustments; detailed unitary/special-industry, nexus/P.L. 86-272 and elective pass-through income tax computations. Ordinary LLET methods are covered; the README labels the remaining entity-income computation gaps.
