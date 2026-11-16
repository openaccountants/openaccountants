---
name: er-tax-overview
description: "A map of Eritrean taxes: income tax, sales and excise tax, stamp duty, farm tax, the diaspora tax and customs, the authority, currency and where each rule lives in the pack. Provides a 2026 reference using identified historical Eritrean gazettes; later current-period amendments remain unconfirmed. Use for questions such as: what taxes are there in Eritrea, who collects tax in Eritrea, Eritrea top tax rate, stamp duty in Eritrea."
jurisdiction: ER
category: international
tax_year: 2026
last_updated: 2026-11-16
version: 0.3
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: decision
---

# Eritrea Tax Overview

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

2026 reference using the available source-year gazettes read on 15 November 2026; that completed research was recovered on 16 November 2026 without redating the old law reads. The latest income-tax amendment recovered here is Legal Notice 119/2012; the Ministry of Justice’s 2023 inventory is a list, not proof that no later law exists. No 2026 consolidated income-tax text or current return was recovered. Before using these source-year rules for a current liability, establish the taxpayer’s actual period and whether a later operative instrument changes them. If current applicability cannot be established, stop the current calculation or filing; retain these historical rules as reference only. Unresolved current implementation remains under Not yet confirmed.

## Who this applies to

Anyone needing the map and an explicitly limited company-versus-person rate comparison first. Detailed calculations live in the linked skills; their unchanged bodies are not reapproved by this update. Currency is the Nakfa (ERN). The Inland Revenue Department under the Minister of Finance administers tax (Proc 62/1994 art 2).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Top personal rate | 30% | Over 3,500 a month; see [Income tax](er-income-tax.md) | Proc 116/2001 art 2, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf |
| Company rate | 30% | See [Corporate income tax](er-corporate-income-tax.md) | Proc 116/2001 art 4, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf |
| Published sales-tax framework | 5%, 10%, 12% | Schedule A goods 5%, other goods 12% unless exempt Schedule D; Schedule B services 5%, C services 10%, other services 10% unless exempt Schedule E/ministerial regulation. This is the sales-tax framework read, not proof that no later VAT/GST exists; see [VAT or GST](er-vat-gst.md) | Proc 117/2001, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-117-2001/eritrean-proc-117-2001.pdf |
| Diaspora tax | 2% of net income | Eligible Eritrean citizens living abroad; separate from domestic-origin taxation. Exact net-income and local collection conditions require their actual source; see Income tax. | Original Proc 67/1995 art 2, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-67-1995/eritrean-proc-67-1995.pdf; official Eritrean Embassy RRT page, https://us.embassyeritrea.org/rrt/ |
| Stamp duty payment/penalty | 50 Nakfa; 10% of duty | Under 50: adhesive stamp. At 50 or more, or where instrument type/nature requires, the Minister may provide payment against receipt by regulation. Failure to pay pursuant to art 8 incurs 10% under 13(3). An unstamped petition/application is rejected but incurs no penalty/fine under 13(4)-(5). | Proc 180/2017, https://shabait.com/2017/03/15/proclamation-no-180-2017/ |
| Rural farm and livestock tax | Rates not recovered | Official notice reports effect from 1 December 2016 and replacement of earlier rules; MoJ inventory identifies Proclamation 178/2016 and Legal Notice 125/2016, reversing the news item’s instrument labels. Actual rate/procedure text remains held. | Ministry of Information notice, https://shabait.com/2016/12/02/legal-notice-on-farm-and-livestock-income-tax/ |

## The base

Income is taxed by origin in Eritrea (Proc 62/1994 art 2(8)), by separate schedule: employment, rent, business, commercial farming (art 5); benefits in kind are valued by the authority (art 6). Separate citizen-abroad obligations require their own net-income facts. Do not merge scheduled income or infer an incorporation saving from gross receipts.

## Deadlines and filing

Employment: monthly declaration and employer remittance within 1 month of month-end, except the self-declaration branches for multiple employers and non-exempt mission employees (Act 11-15). Business: 1,2 or 4 months after accounting year-end according to the prescribed books required, not a taxpayer’s free choice (Act 26). The original monthly sales-tax filing topic remains routed to VAT or GST; the sales-tax declaration/payment provisions were not reread for a new current filing conclusion here. Use the owner skill and actual operative text before filing.

## Penalties and interest

Act 63: Department may assess 20% of finally assessed tax for declaration/payment failure within art 26’s periods; it is not a universal penalty for every tax. Act 64: 5% of tax in default per month, maximum 50% of amount due; partial-month convention held. Act 65: 20% of finally assessed tax when required books are missing/unacceptable. Arts 63-65 penalties are recovered as tax and may be waived wholly/partly by the Department under 66. Stamp duty has its distinct rule and petition exception above; do not apply the income-tax penalties to all taxes.

## Cross-border points

Ordinary income-tax scope is Eritrean origin wherever paid; eligible citizens abroad have the separate 2% net-income levy. No treaty, residence or universal consular procedure is established by this map. Customs is listed under Proc 112/2000 in the Ministry of Justice inventory; its rates/procedure remain outside usable instructions here.

## Two worked examples that recompute

**Case 1: ordinary incorporated body, 100,000 taxable profit.** Assume the ordinary 30% source-year rule applies, no mining/petroleum special regime and no unresolved later amendment. Tax 30,000; this is not a gross-turnover calculation.

```oa-check
name: Company
inputs:
  profit: 100000
steps:
  - tax: profit * 0.30
expected:
  tax: 30000.00
```

**Case 2, a bounded decision: person or ordinary company at 100,000 taxable business income?** Compare the same already-established base under marginal personal bands and the flat corporate rate. This excludes formation costs, social charges, special regimes and any unresolved later law; a marginal-rate comparison alone does not recommend incorporation.

```oa-check
name: Sole trader against company
inputs:
  income: 100000
steps:
  - band_1: min(income, 2400) * 0.02
  - band_2: (min(income, 14400) - min(income, 2400)) * 0.10
  - band_3: (min(income, 30000) - min(income, 14400)) * 0.20
  - band_4: (min(income, 42000) - min(income, 30000)) * 0.25
  - band_5: (income - min(income, 42000)) * 0.30
  - tax: band_1 + band_2 + band_3 + band_4 + band_5
  - company: income * 0.30
  - saving: company - tax
expected:
  tax: 24768.00
  saving: 5232.00
```

The person’s computed tax is 24,768 and the company’s 30,000; the difference 5,232 is derived. Art 31(5) exempts dividends received by shareholders from Eritrean incorporated/corporated bodies in the text read; do not turn that into a general foreign-dividend exemption or an incorporation recommendation.

## Ask the client first

- Which tax?
- Person or company?
- Resident in Eritrea or a citizen abroad?
- Sector?

## Sources

| Source and actual reading scope | Official URL | Read on |
|---|---|---|
| act: Read for English text arts 1-71, physical pages 21-42; arts 2,5-9,11-31,40-41,55-66 operative clauses and neighbors. Rate schedules superseded by Proclamation 116/2001 are not reused. Schedule C-3 and definition page visually checked. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf | 2026-11-15 |
| rates: Read for English arts 1-7, physical 7-11; all employment/rent/business rate tables visually checked at 7-9, loss carry-forward and commencement read. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf | 2026-11-15 |
| sales: Read for English arts 1-5, physical 20-22, and complete service Schedules B/C, physical 33-34. Goods exemption/classification lists not read for new determinations. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-117-2001/eritrean-proc-117-2001.pdf | 2026-11-15 |
| diaspora: Read for Original Tigrinya operative page 2 visually inspected for instrument identity, embedded employment/net income/2% and arts 2-4; compared with the UK Government English Annex II, printed 11-12. No claim of an authoritative English original. | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-67-1995/eritrean-proc-67-1995.pdf | 2026-11-15 |
| embassy: Read for Whole operative General Information, status-specific evidence requirements, full-time-student FAQ and steps, web lines 59-112. US consular practice is not a universal statutory payment calendar. | https://us.embassyeritrea.org/rrt/ | 2026-11-16 |
| stamp: Read for Whole published operative arts 1-14; in particular 8 payment/threshold and 13 penalty/petition exceptions. Missing article 4 rate schedule is not guessed. | https://shabait.com/2017/03/15/proclamation-no-180-2017/ | 2026-11-15 |
| farm: Read for Whole operative government notice, paragraphs 13-19; reported 1 Dec 2016 commencement and replacement, not actual statutory rate tables. | https://shabait.com/2016/12/02/legal-notice-on-farm-and-livestock-income-tax/ | 2026-11-15 |
| list: Read for Intro and entire section 16 Taxes (Except Customs), printed 10-11; Customs 112/2000 identity in section 15. Inventory is not proof that no later law exists. | https://mojeritrea.net/wp-content/uploads/2023/05/Thematic-Categorization-of-Domestic-Legislations-of-the-State-of-Eritrea.pdf | 2026-11-15 |

The original 67/1995 scan and the Eritrean Embassy page replace reliance on a foreign-hosted English translation; the UK Government Annex II remains preserved in the evidence as a translation aid. The 15 November read dates are the recovered completed writer reads, not new whole-document reads on 16 November. The Embassy page alone was opened again on 16 November for the stated consular scope. Gazette source years and actual read scopes are explicit. No full reading of the current unrecovered consolidated law or live portal is claimed.

Not yet confirmed: Current 2026 consolidated tax law/later amendments, fiscal-year dates and current forms/portal. The original calendar-year claim remains unconfirmed. Actual stamp-duty rate schedule, current farm/livestock rate text, customs rates/procedures and detailed sales-tax filing provisions are not established here. The Ministry farm news item swaps the Proclamation/Legal Notice numbers compared with the MoJ inventory; use actual enacted texts for a determination. A general no-VAT/GST conclusion, treaty/day-count residence, diaspora net-income details and current consular collection are not inferred from this map. Existing passing siblings retain their bytes, including their older scope statements; this rewrite does not attest to them.
