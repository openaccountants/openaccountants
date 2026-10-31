---
name: li-transfer-pricing
description: >
  Prepare 2026 Liechtenstein transfer pricing workpapers under SteG article 49,
  SteV articles 31a-31b and 36d, and the Country-by-Country Reporting Act.
  Covers the arm's-length rule for related parties and permanent establishments,
  related persons, the OECD methods, the Master File and Local File for groups
  over CHF 900 million (goods over CHF 1 million, other items over CHF 250,000),
  the separate route for entities exceeding all PGR article 1064(2) size criteria
  (CHF 500,000 / CHF 125,000), the residual evidence duty, the 60-day request
  deadline, CbC reporting (registration, 12-month filing, XML upload, fines up to
  CHF 250,000) and corresponding adjustments. Trigger on: Liechtenstein transfer
  pricing, Verrechnungspreise Liechtenstein, Master File, Local File, CbCR
  Liechtenstein. Out of scope: benchmarks, APAs, MAP and public CbC reporting.
jurisdiction: LI
category: transfer-pricing
trust_label: Built by Michael Cutajar and the OpenAccountants team
tax_year: 2026
tier: 2
last_updated: 2026-10-30
version: 0.4
---

# Liechtenstein transfer pricing v0.4

## Who this applies to

SteG article 49 requires related-party and PE dealings to use conditions that independent parties would agree in comparable circumstances, and documentation for material transactions. SteV article 31b implements the methods and evidence routes. These are Liechtenstein rules; no Swiss documentation exemption is imported. This skill prepares the file; it supplies no benchmark. [Tax Act][law]; [Tax Ordinance][ordinance]

## Rates, bands and thresholds

All thresholds below are from current SteV article 31b. “More than” and “exceeds” are strict; an equal amount does not itself cross that particular threshold. This does not exempt the transaction from arm's-length pricing or paragraph 8 evidence.

| Route | Entry gate | Cross-border transaction threshold and content | Official source (2026) |
|---|---|---|---|
| Article 31b(2)–(3) | Part of a group with consolidated turnover **more than CHF 900 million** | OECD Master File and Local File; goods purchases/sales **over CHF 1 million** per connected party/PE/year, or other expenses/income **over CHF 250,000** per expense/income category, party/PE/year | [SteV article 31b][ordinance] |
| Article 31b(4)–(5) | Outside the above group route but exceeding **all** size criteria referenced in PGR article 1064(2) | Specified company/business/structure description, relationship register, functions/risks/assets, reasoned method selection and pricing/arm's-length analyses; goods **over CHF 500,000**, other expenses/income **over CHF 125,000**, on the stated party/category/year bases | [SteV article 31b][ordinance] |
| Article 31b(8) | Transactions/relationships not captured by paragraphs 2–5 and 7 | Suitable evidence of arm's-length compliance on authority request; no blanket small-company or domestic-transaction exemption | [SteV article 31b][ordinance] |

The PGR article 1064(2) criteria currently state CHF 32.4 million balance sheet, CHF 64.8 million net sales and 250 average employees. PGR company classification ordinarily uses two of three, whereas SteV's formal-documentation cross-reference expressly says **all** criteria. Do not replace the latter with the generic “large company” label. PGR article 1064(4) also has a two-consecutive-balance-date rule and an initial-application rule; article 1064(5) addresses other reporting currencies. Retain both years, initial-application and currency evidence and confirm any contested interaction before deciding a formal-duty exemption. [PGR, article 1064, current 1 September 2026 consolidation][pgr]; [SteV, article 31b(4)][ordinance]

## The base

### Related persons and transaction record

SteV article 31a includes direct/indirect participation or beneficial interests in either direction, organs, close personal relationships (including family/friendship), their stated connections and connected participations. Its reach is broader than one percentage test. Article 31b(7)'s at-least-25% participation/benefit condition applies to the formal-documentation duty under paragraphs 2–6 for the relationships in article 31a(a) and (c); it does not erase the residual evidence duty in paragraph 8. Retain the exact relationship and direct/indirect chain, not only an ownership percentage. [SteV, articles 31a–31b][ordinance]

Create a transaction register by party/PE, country, relationship, category, year, amount, currency, contract, invoicing, actual conduct and accounting line. Record functions, risks, assets, personnel/control, value chain and any PE allocation. Reconcile gross flows before testing thresholds; do not net opposite payments or unrelated categories to manufacture a smaller amount. The treatment of an unusual aggregation/currency/period case still needs specific confirmation.

### Method and workpaper

Article 31b(1) applies the current OECD TP Guidelines and requires the most suitable method for the actual transaction facts. It lists CUP, resale price, cost plus, TNMM and profit split; another method is permitted if the listed methods cannot suitably represent the arm's-length result. Do not select a method merely because a markup is easy to compute. [SteV, article 31b(1)][ordinance]

1. Delineate what the parties actually did and identify comparable circumstances, tested transactions, functions, risks and assets.
2. Explain the selected method and rejected alternatives, data reliability, comparability adjustments and limitations. Preserve the underlying search/financial evidence. This skill supplies no local benchmark or safe-harbour margin.
3. Reconcile the method's base and profit measure to the accounts. A gross cost-plus markup on cost is different from a net return on cost or profit as a percentage of sales; the example below illustrates the denominator distinction only.
4. Reconcile any proposed adjustment to SteG article 49 and corporate income, with the actual tax, loss, equity-deduction and foreign/treaty implications separately assessed. A ledger correction is not an agreed corresponding adjustment abroad.
5. Retain contracts, evidence, calculations, file contents, approval/authority communications and the annual refresh record. Apply the separate CbC workflow below; specialist pricing transactions and public corporate-transparency reporting need their own rules.

### Separate CbC reporting: scope and reporting entity

Under CbC Act article 2(1)(c), the ordinary exemption covers a group whose consolidated revenue in the **preceding reporting fiscal year does not exceed CHF 900 million**, subject to the voluntary-waiver rule. The Act requires a multinational group/PE situation and defines the constituent entities, ultimate parent, reporting entity, surrogate and reporting fiscal year. The TP article 31b threshold is not a substitute for those definitions, the prior-year test or the CbC reporting-role decision. Preserve the actual consolidation, year, currency and filing-role evidence. A non-franc threshold/currency dispute remains a separate question. [CbC Act article 2][cbc-law]

A resident ultimate parent within article 3(1), including the condition that it is not exempt under PGR articles 1099–1101 from the consolidated management-report duty, files unless its permitted surrogate appointment removes that duty. An overseas surrogate can be appointed only with the article 3(3) filing-law, partner-state, no-systemic-failure and surrogate-notification conditions. A Liechtenstein-resident surrogate files under article 4. A different resident constituent of a foreign-parented group files locally under article 5 **on the authority's demand**, if the parent's jurisdiction lacks a filing duty, is not a partner, or has systemic failure, subject to the prohibition on demanding a report the authority receives from a partner. Do not impose routine local filing on every foreign-owned subsidiary. [CbC Act articles 3–5][cbc-law]

Collect the report's jurisdictional revenue, pretax profit/loss, paid and accrued income tax, stated capital, accumulated earnings, employees and tangible assets other than cash; identify all constituent entities, residence/incorporation jurisdictions and main activities. Reconcile these figures to the selected reporting data and explain classification/consistency issues. This is a CbC information return; it does not compute a new tax liability or establish that a transaction's price is arm's length. [CbC Act article 2(1)(m) and article 9(2)][cbc-law]

### CbC exchange and technical preparation

Use the **current 2026 CbC Ordinance annex** to establish the partner, first eligible reporting period and permanent non-reciprocal status for each relevant jurisdiction. Article 2(2) requires reporting all constituent entities, even those in nonpartners or permanently non-reciprocal jurisdictions; partner jurisdictions with constituent entities are ReceivingCountry recipients, but permanently non-reciprocal states are excluded from that recipient field. Do not remove their entities from the report or use a treaty-signature list as an exchange-status test. Actual systemic-failure notices and case-specific partner eligibility still require confirmation. [CbC Ordinance article 2 and annex][cbc-ordinance]

Article 3 refers to OECD Action 13 Annex III and the current OECD CbC XML schema. The authority currently links an **XML schema 2.0 upload** and its July 2020 local technical supplement. The public first step requires the authority-issued CbC reporting number, PEID and PIN; obtain these from the authorised filer and keep secrets outside the research record. Validate the completed report against the applicable OECD XSD/user guide and current local instructions, retain original/correction identifiers and the filing receipt. A successful first-step page read is not an authenticated upload or an accepted filing. Full payload/schema testing, correction execution and the separate public CbCR transparency regime are not completed here. [CbC Ordinance article 3][cbc-ordinance]; [authority reporting page][cbc-authority]; [upload landing page][cbc-upload]; [local supplement][cbc-technical]


### Further check

#### Separate-size route category aggregation

Assume the separate-size route and relationship conditions are established, with two cross-border service expenses in the same category to one party, CHF 80,000 and CHF 60,000. CHF 140,000 exceeds CHF 125,000 by CHF 15,000. This does not establish the company-size or relationship gates.


## Deadlines and filing

For the formal files under paragraphs 2–5, paragraph 6 requires submission **within 60 days of request**, in **German or English**. It is a request deadline, not an invented annual automatic filing date. Record receipt, scope, due date and submitted version. The CHF 900 million TP group route and the separate CbC law below have distinct tests; do not infer CbC status from the TP documentation decision. [SteV, article 31b(6)][ordinance]

### CbC registration and submission dates

A resident reporting entity registers unprompted **by the last day of its first reporting fiscal period**, updates registered changes immediately and deregisters when reporting-entity status ends. The authority permits initial registration by an informal letter. Under CbC Act article 6, prepare the report in German or English, in the national or the group's relevant currency, and submit **within 12 months after the reporting period ends**. For the article 5(1)(c) systemic-failure case, the authority sets a reasonable deadline. Record the actual demand and date rules; a TP document request's 60 days is a different deadline. [CbC Act articles 6–7][cbc-law]; [authority reporting page][cbc-authority]

## Penalties and interest

SteG article 135 provides fines for intentional/negligent noncompliance after a reminder, with the stated ordinary and serious/repeat maxima. It is not a specific automatic TP file fine. Incorrect profit, tax evasion and procedural noncompliance have different legal bases. Do not calculate a penalty or treat 60 days as extended without an actual authority decision. [SteG, articles 49 and 135][law]

CbC sanctions have their **own** legal basis. Under article 20, the filing-duty maximum is CHF 250,000 for intentional breach and CHF 100,000 for negligence. The intentional registration-duty maximum is CHF 20,000; the negligent registration-duty maximum is CHF 10,000. Article 21 permits up to CHF 500,000 for serious, repeated or systematic filing breaches, while article 21a separately covers the stated aggravated participation in another's filing breach. These are statutory ceilings subject to the actual offence/procedure, not a fee automatically added to the tax bill. [CbC Act articles 20–21a][cbc-law]

For ordinary administrative orders under the CbC procedure section, article 18 provides a written objection within 30 days of service, stating relief and supporting facts. Criminal-administrative routes differ: article 23 gives 14 days for its stated appeals and an objection to a penalty order. Identify the decision type before selecting a route; a 30-day administrative objection must not be used to extend a 14-day penalty-order remedy. [CbC Act articles 18 and 22–23][cbc-law]

## Cross-border points

SteG article 63 addresses treaty/reciprocity relief and specified corresponding adjustments. Articles 124a and the actual foreign finality/treaty facts need separate review before seeking a change to a final assessment. This skill does not promise double-tax relief, an APA, a MAP result or an accepted transfer-price range.

For a non-treaty foreign TP correction, SteG article 63(2) requires an application and proof both that the taxpayer could assume its original price complied with article 49 and that the foreign correction itself satisfies arm's length and was appropriately challenged abroad. Article 63(3) supplies a distinct application route for the recipient of a domestic related-party upward correction, with its original-price reliance gate. Article 124a changes a final assessment only for its article 63(2) situation: apply within 90 days of foreign-assessment finality and no later than 10 years after the relevant tax year ends. Keep the foreign final decision, challenge record, pricing evidence and service/finality dates; no universal corresponding adjustment or reopening right is promised. Actual treaty/MAP and foreign counterpart decisions remain separate. [SteG articles 63 and 124a][law]

### Corresponding-adjustment application and finality clocks

SteV article 36d supplies the procedure for article 63 applications. For a foreign article 63(2) correction, submit the complete facts, the original pricing/arm’s-length documentation, the foreign authority’s pricing/correction documentation, proof that all reasonable foreign challenge measures were taken, and the final foreign assessment. The stated rejection gates concern the original price’s defensible article 49 legal basis, whether the foreign correction is arm’s length, and whether reasonable foreign measures were taken. A domestic article 63(3) application instead needs 36d(1)(a)–(b)’s facts/original-price material and has its stated 36d(2)(a) rejection gate. [SteV article 36d(1)–(3)][ordinance]

Both applications are due **within three months after finality of the assessment of the taxpayer whose taxable profit was increased by the TP correction**. Retain that taxpayer’s actual finality evidence; do not substitute the applicant’s own assessment date. If a final Liechtenstein assessment also requires reopening under SteG 124a for a foreign article 63(2) correction, meet its separate 90-day foreign-finality and 10-year outer limits as well. Three calendar months and 90 days are distinct periods. Actual finality/service/holiday questions remain case-specific. [SteV article 36d(4)][ordinance]; [SteG article 124a][law]

## Two worked examples that recompute

### Same-party goods aggregation in the assumed Master/Local route

Assume the group route, qualifying relationship and cross-border goods purchases from one party in one year are established. Two purchases of CHF 600,000 and CHF 500,000 total CHF 1.1 million, over the CHF 1 million threshold. No other party/category is included.

```oa-check
name: Liechtenstein assumed group route goods threshold
inputs:
  first_goods_purchase: 600000
  second_goods_purchase: 500000
  established_route_threshold: 1000000
steps:
  party_year_purchases: first_goods_purchase + second_goods_purchase
  excess_over_threshold: party_year_purchases - established_route_threshold
expected:
  party_year_purchases: 1100000
  excess_over_threshold: 100000
```

### Gross cost-plus is not margin on sales

Assume an independently supported gross cost-plus method, CHF 100,000 eligible cost and 8% markup solely for the case. Gross profit is CHF 8,000, revenue CHF 108,000 and profit/revenue approximately 7.407407%. Neither percentage is a Liechtenstein safe harbour; no TNMM benchmark is inferred.

```oa-check
name: Liechtenstein assumed gross cost plus denominator control
inputs:
  established_cost_base: 100000
  assumed_supported_markup: 0.08
steps:
  gross_profit: established_cost_base * assumed_supported_markup
  transaction_revenue: established_cost_base + gross_profit
  profit_as_percent_of_sales: gross_profit / transaction_revenue * 100
expected:
  gross_profit: 8000
  transaction_revenue: 108000
  profit_as_percent_of_sales: 7.407407407407407
```

## Ask the client first

Obtain the full group/benefit/relationship chart, turnover and consolidation evidence, both years' company-size data, currency, all party/category transactions, PE facts and actual authority requests. Require the functions/risks/assets record, method/comparable support and accounts reconciliation. Refer financing, guarantees, intangibles, restructurings, PE allocation, contested aggregation/size tests, foreign CbC demands/currency/systemic-failure, public CbCR transparency, advance agreements and cross-border disputes.

## Sources

| Source | URL | Read on |
|---|---|---|
| Steuergesetz (SteG), LR 640.0, consolidated 1 July 2026, articles 49, 63, 124a, 135 | https://www.gesetze.li/konso/pdf/2010340000 | 2026-10-30 |
| Steuerverordnung (SteV), consolidated 1 July 2026, articles 31a-31b, 36d | https://www.gesetze.li/konso/pdf/2010437000 | 2026-10-30 |
| Personen- und Gesellschaftsrecht (PGR), consolidated 1 September 2026, article 1064 | https://www.gesetze.li/konso/pdf/1926004000 | 2026-10-30 |
| CbC Act (Gesetz über den internationalen automatischen Austausch länderbezogener Berichte multinationaler Konzerne), consolidated 1 January 2026, articles 2-9, 14-23 | https://www.gesetze.li/konso/pdf/2016502000 | 2026-10-30 |
| CbC Ordinance, consolidated 1 January 2026, articles 2-3 and annex | https://www.gesetze.li/konso/pdf/2016510000 | 2026-10-30 |
| Steuerverwaltung, CbC reporting | https://www.llv.li/de/landesverwaltung/steuerverwaltung/internationaler-informationsaustausch/cbcreporting | 2026-10-30 |
| Steuerverwaltung, CbC upload | https://formulare.llv.li/formserver_CBC/start.do?generalid=STV_CBC_MM | 2026-10-30 |
| Steuerverwaltung, CbC XML technical supplement (July 2020) | https://www.llv.li/serviceportal2/amtsstellen/steuerverwaltung/int_cbc_xml_zusatzspezifikation.pdf | 2026-10-30 |

Not yet confirmed: size, period and currency interactions for entities reporting in a currency other than CHF; comparables and special methods (financing, intangibles, restructurings); a foreign jurisdiction's partner or systemic-failure status in a given case; public CbC transparency reporting; APA and MAP procedure.

[cbc-law]: https://www.gesetze.li/konso/pdf/2016502000
[cbc-ordinance]: https://www.gesetze.li/konso/pdf/2016510000
[cbc-authority]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/internationaler-informationsaustausch/cbcreporting
[cbc-upload]: https://formulare.llv.li/formserver_CBC/start.do?generalid=STV_CBC_MM
[cbc-technical]: https://www.llv.li/serviceportal2/amtsstellen/steuerverwaltung/int_cbc_xml_zusatzspezifikation.pdf

[law]: https://www.gesetze.li/konso/pdf/2010340000
[ordinance]: https://www.gesetze.li/konso/pdf/2010437000
[pgr]: https://www.gesetze.li/konso/pdf/1926004000

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
