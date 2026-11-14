---
name: sc-sales-tax
description: "South Carolina 6 percent general sales/use, location-specific local taxes, 5 percent maximum-tax items and IMF boundary, software/repair classification, food exemptions, ST-3 and ST-389 filing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sc-sales-tax"
  jurisdiction: "US-SC"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# South Carolina sales and use tax, tax year 2026

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal figures and computations belong to the linked federal owner skills.

**Answer first.** General SC sales/use tax is 6% plus applicable local levies. Qualifying maximum-tax items instead use **5% up to USD 500**, with no SCDOR-administered local sales tax; many vehicle transactions are subject to DMV infrastructure maintenance fee (IMF) instead. The old 6%-cap-plus-unlimited-local calculation was wrong. Sources: [12-36-910, 1110, 2110 and 2120(83)](https://www.scstatehouse.gov/code/t12c036.php); [maximum-tax chapter, pages 1 to 4](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_10.pdf).

## Scope

Ordinary SC retailers, physically present and economic-nexus remote sellers, marketplace reconciliation and purchasers owing use tax. Covers retained specialist topics with explicit limits; admissions, local hospitality/accommodations fees and DMV IMF administration are not general-retail calculations. `us-sales-tax` owns federal/multistate context; state income and employee taxes route to `sc-income-tax`, `sc-corporate-tax` and `sc-payroll`. Original contributor attribution retained: **Open Accounting Skills Registry**.

## Ask the client first

1. SC locations/employees/inventory, current/prior calendar-year SC gross receipts, sales channels and marketplace collection.
2. Product/service contract, delivery address and transaction date; taxable and exempt receipts separately.
3. Maximum-tax item classification, first DMV registration/IMF, boat versus motor/trailer, manufactured-home energy requirements.
4. Resale/exemption evidence, medical/manufacturing/agricultural use and business purchases without collected tax.
5. Local county/city/tribal location, food/hospitality/lodging status and assigned tax codes.
6. Retail licence, assigned filing frequency, sales/use workpapers, discounts already claimed and prior returns/payments.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate, amount and conditions | Official source |
|---|---|---|
| General retail/use | 6% state plus applicable local taxes | [general rate](https://dor.sc.gov/sales-use-tax-index/sales-tax) |
| Local rate lookup | Current fetched map effective 1 May 2026 shows general combined 6% to 9%; exact location/item/date controls | [ST-500 effective-date heading and table](https://dor.sc.gov/sites/dor/files/forms/ST500.pdf) |
| Qualifying maximum-tax item | 5%, no more than USD 500 per qualifying sale; applicable written leases require more than 90 continuous days | [pages 1 to 3](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_10.pdf) |
| Qualifying maximum-tax local treatment | No SCDOR-administered local sales/use tax on max-tax sale/lease | [page 1](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_10.pdf) |
| Certain religious equipment/instruments | 5% capped USD 300 with exempt-purpose/location/affidavit conditions | [page 3, category B](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_10.pdf) |
| Manufactured home | Special USD 300/energy rules and possible additional 2% above USD 6,000; not blanket USD 500 | [12-36-2110(B)/2120(34)](https://www.scstatehouse.gov/code/t12c036.php); [partial exemptions](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_9.pdf) |
| Retail licence | One-time USD 50 for each retail location | [retail licence FAQ](https://dor.sc.gov/sales-use-tax-index/sales-tax/remote-sellers) |
| Remote economic nexus | Gross SC revenue **exceeds** USD 100,000 in previous or current calendar year; no transaction-count test | [current nexus definition](https://dor.sc.gov/sales-use-tax-index/sales-tax/remote-sellers) |
| Electronic mandate | SC sales/use liability USD 15,000 or more per filing period | [filing and payment mandate](https://dor.sc.gov/sales-use-tax-index/sales-tax) |

1. Establish nexus. Physical presence creates collection from its establishment date, regardless of remote threshold. A remote seller exceeding USD 100,000 SC receipts from property, electronic products or services in previous/current calendar year generally begins collecting the first day of the **second calendar month** after nexus is established. Old November 2018 is the historical first implementation, not a fresh annual effective date. Marketplace facilitator/seller reporting must be reconciled to platform statements and current law; do not collect twice or assume all seller obligations disappear. Source: [definition, effective-date and physical-nexus FAQs](https://dor.sc.gov/sales-use-tax-index/sales-tax/remote-sellers).
2. Register Retail Licence through MyDORWAY, separately by location, paying the USD 50 fee where required. Document any valid licensing exception. Retain appropriate resale/exemption certificate and evidence of qualifying use; a nonprofit's status is not a universal exemption for every purchase. Source: [retail licence](https://dor.sc.gov/sales-use-tax-index/sales-tax/remote-sellers); [12-36-510 and exemption provisions](https://www.scstatehouse.gov/code/t12c036.php).
3. Determine ordinary taxable goods and enumerated services, delivery/sourcing and taxable gross proceeds. The 1 May 2026 ST-500 map gives Charleston 9%, Greenville 6%, Berkeley 9%, Myrtle Beach/Horry 9%, among other locations. Use exact address and effective period, not the old assumption Charleston is always 8%. Local option, capital projects, transportation, school/education and tourism levies can differ by item and jurisdiction; Catawba and directly administered hospitality fees need separate treatment. Sources: [dated ST-500](https://dor.sc.gov/sites/dor/files/forms/ST500.pdf); [local tax categories and exemptions, 2025-2026 filing cycle](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_12.pdf).
4. Qualifying unprepared SNAP-eligible food is exempt from **state** sales tax, but not automatically every local levy. Candy/soft drinks eligibility follows the food definitions, not a blanket exemption for all food products; prepared meals remain taxable and may incur separate local hospitality. Prescription medicine/prosthetics and certain diabetic supplies have specific exemption conditions; ordinary OTC medicine is not blanket exempt. DME needs the current statutory Medicare/Medicaid funding/provider conditions, not just a prescription. Residential electricity/fuel has a statutory exemption, so the old general-taxability claim was wrong. Source: [12-36-2120(28), (33), (74), (75)](https://www.scstatehouse.gov/code/t12c036.php); [medical, residential energy and unprepared-food sections](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_9.pdf).
5. Distinguish software delivery/access. Software on tangible media can be taxable whether canned or custom; wholly electronic delivery without any tangible backup is not a taxable TPP sale under RR12-1. **Application Service Provider access** to software on the provider's website is taxable communication under that same ruling. The old inverted claims that electronic canned software is taxable and all SaaS is exempt are corrected. Do not decide a mixed cloud/data service solely from the label SaaS, and do not extend electronic-software treatment to all digital goods/streaming. Sources: [RR12-1, questions, conclusions and discussion](https://dor.sc.gov/sales-use-tax-electronically-delivered-software); [chapter 7 software footnote, corroborating 2025-2026 filing cycle](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_7.pdf).
6. Repair parts/services: where separate agreements and records/invoices distinguish substantial parts transferred unchanged from labor, only the parts may be taxable; an inseparable bundled repair can include both. Auto repair regulation 117-306.2 expressly contains this separation rule. Fabrication/installation/alteration have distinct rules; separately stated reasonable installation can be excluded under 117-313.3. The old prohibition against ever excluding repair labor was wrong. Source: [117-306, 306.1/306.2 and 313](https://www.scstatehouse.gov/coderegs/Chapter%20117.pdf).
7. For boats/watercraft motors/aircraft/motorcycles/RVs and other listed maximum-tax categories, establish the precise item and whether IMF supersedes sales/use. Apply 5% and USD 500 limit only when the relevant maximum-tax regime applies; ordinary threshold reaches the cap at **USD 10,000**, not old USD 8,333. No SCDOR-administered local tax is added on max-tax items. A boat trailer is not necessarily a qualifying capped boat; a motor or trailer can be a separate item. Manufactured homes have separate rules. Source: [categories, exceptions, boats and manufactured homes](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_10.pdf).
8. For tax-free purchases used/stored/consumed in SC, evaluate use tax and properly paid other-state credit. Business purchases route through ST-3 and applicable ST-389; individuals can use the applicable SC1040 use-tax route, but final 2026 line number is Not yet confirmed. Maximum-tax and IMF distinctions still apply. Source: [12-36-1310, 2110 and 2120(83)](https://www.scstatehouse.gov/code/t12c036.php); [use-tax purchases worksheet](https://dor.sc.gov/sites/dor/files/forms/ST3.pdf).

## Boundary and exception table

| Old topic retained | Correct treatment or explicit limit |
|---|---|
| Clothing/footwear | Ordinary taxable goods outside a qualifying holiday; holiday terms below |
| Medical/OTC/DME | No blanket OTC or prescription-only DME exemption; apply statutory conditions |
| Manufacturing machines/components/electricity/pollution equipment | Conditional exemptions under 12-36-2120 and related rules, not every manufacturer's purchase; current detailed mixed-use eligibility Not yet confirmed |
| Agricultural supplies/equipment | Conditional statutory agricultural exemption and SCATE evidence; current detailed card/use rules Not yet confirmed |
| Telecommunication/cable/satellite/laundry/commercial utilities | Enumerated communications, laundry and electricity can be taxable; satellite/federal limitations and exact bundles need transaction-specific research |
| Legal/accounting/medical, haircuts/spa | Professional/personal service versus taxable product true-object test; blanket list not sufficient. Specific accounting/hair/spa transactions Not yet confirmed |
| Contractors/real property/prefabricated units | Contractors generally consume building materials; distinguish real-property improvement from sale of a manufactured unit under 117-314 |
| Delivery/freight | Old blanket separately-stated freight exemption is Not yet confirmed; review gross-proceeds terms and actual delivery contract |
| Casual/private transfers | Specific casual excise/IMF and exempt-transfer rules apply to vehicles/boats; old always-taxable/no-exception prohibition is too broad |
| Exemption forms ST-8A/ST-8F/ST-8B/SSTCE; good-faith/three-year retention | Old form-to-purpose mapping and universal protection/retention claims are **Not yet confirmed**; use current form and statutory seller evidence requirements |
| SST membership | Old nonmember assertion Not yet confirmed here; not used for a tax decision |
| Audit/VDA/penalty abatement | Refer with records and current program terms; no automatic relief |

The sales-tax holiday statute covers specified clothing, school supplies, computers and bed/bath items on the first Friday-Sunday in August. There is no confirmed USD 1,000 computer-price cap in the statutory list: the old cap is not used. For 2026, exact event administration/item exceptions are Not yet confirmed; use the current holiday notice before exempting a transaction. Source: [12-36-2120(57)](https://www.scstatehouse.gov/code/t12c036.php); [holiday list and examples, 2025-2026 filing cycle](https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_9.pdf).

## Worked cases

**Case 1, ordinary dated retail.** Invented Charleston delivery of an USD 800 television during the fetched map's effective period uses 6% state plus 3% SCDOR local, total 9%: state USD 48, local USD 24, tax USD 72. The old USD 64 case assumed 2% local; do not reuse that local rate for this dated scenario. Other locally collected fees are not included.

```oa-check
name: South Carolina ordinary retail at fetched Charleston rate
inputs:
  price: 800
steps:
  - state_tax: price * 0.06
  - local_tax: price * 0.03
  - total_tax: state_tax + local_tax
expected:
  state_tax: 48
  local_tax: 24
  total_tax: 72
```

**Case 2, maximum-tax decision.** Invented qualifying boat sale USD 200,000, with no IMF or other special exception, has 5% computed tax USD 10,000 capped at USD 500. SCDOR local sales tax is zero on this capped transaction, not USD 4,000. Total USD 500 replaces the old USD 4,500. Confirm boat/motor/trailer line items independently.

```oa-check
name: South Carolina qualifying maximum tax boat sale
inputs:
  price: 200000
steps:
  - before_cap: price * 0.05
  - state_tax: min(before_cap, 500)
  - local_tax: 0
  - total_tax: state_tax + local_tax
expected:
  before_cap: 10000
  state_tax: 500
  local_tax: 0
  total_tax: 500
```

### Remaining old cases, corrected or bounded

| Old invented case | Correct result and condition |
|---|---|
| Qualifying capped item USD 10,000 /25,000 /50,000 /100,000 /500,000 | At 5%, uncapped USD 500 /1,250 /2,500 /5,000 /25,000; each capped USD 500; savings USD 0 /750 /2,000 /4,500 /24,500 |
| USD 50,000 or 45,000 vehicle with purported local 2% or 1% | First establish DMV IMF versus max sales tax and residence/registration; old USD 1,500/950 result invalid. Under qualifying max-sales regime alone, USD 500 and no SCDOR local; no IMF amount assumed |
| USD 200 Greenville groceries | Qualifying unprepared food has 0 state; fetched May 2026 map has no SCDOR local general tax for Greenville, so 0 for that location/period; this is not a universal food-local exemption |
| USD 400 monthly software access | If taxable ASP communication,6% state USD 24 plus applicable local. Electronic delivery-only and mixed services require different classification; oldautomatic 0 revoked |
| Remote receipts USD 110,000 and 50 transactions | Exceeds USD 100,000 in relevant current/prior year, so economic nexus; 50 transactions is not a test; collection start follows second-month rule |
| Repair labor USD 300 plusparts USD 400 at hypothetical 8% | Supported separate parts/labor agreements/invoices:USD 400 x 8%=USD 32; if inseparable taxable USD 700 charge, USD 56. Oldalways USD 56 not universal |

## When to refuse or refer

Refer IMF/vehicle/private transfers, uncertain software/communications, manufacturing/agricultural/medical exemptions, tribal/local hospitality, ambiguous labor/delivery, certificate disputes and audits/VDA. Do not use absolute old prohibitions to override primary-law exceptions.

## Filing and payment

Use https://mydorway.dor.sc.gov, choose sales/use account and period; reconcile gross sales plus purchases subject to use tax, itemize exempt/deductible sales and compute net taxable base. **ST-3** reports state tax and **ST-389** applicable local taxes; select locality/type codes and retain workpaper/acceptance. Pay correct period and save separate payment proof. Default monthly due 20th next month; **quarterly and annual filing are available only with SCDOR approval**, requested by MyDORWAY web message or the stated Department route. Quarterly due 20th after quarter and annual 20 January; seasonal accounts follow their authorized active periods. The old no-quarterly/no-annual and universal e-file requirements were wrong. Electronic filing/payment mandatory at USD 15,000 liability per period; paper remains possible below threshold. Source: [all filing schedules, approval footnote and electronic/paper rules](https://dor.sc.gov/sales-use-tax-index/sales-tax).

ST-3 line 7 discount is **3% if total state/local tax is less than USD 100, or 2% of the total if USD 100 or more**, not 3% of first USD 100 only. Combined discount is limited to USD 3,000 per fiscal year for June-May returns filed July-June; verify available cap and electronic additional-discount eligibility before claiming. Source: [line 7 and form notes](https://dor.sc.gov/sites/dor/files/forms/ST3.pdf).

Late-filing/payment/fraud, estimated assessments and interest are governed by Title 12 Chapter 54 and applicable period rules. The old 5%-per-month/25%,0.5%-per-month/25%,75%fraud and federal-rate shorthand are **Not yet confirmed** here for each sales-tax assessment; use current notice/law rather than presenting those as a universal calculation. Source for further determination: [Chapter 54, penalties and interest](https://www.scstatehouse.gov/code/t12c054.php).

## Completion checklist

- Nexus/start date and Retail Licence established; marketplace collections reconciled.
- Item/date/location taxability and exemptions supported; cap/IMF and local-tax exceptions distinguished.
- State/use/local workpaper and ST-3/ST-389 match; discount/fiscal cap checked.
- Authorized frequency and payment mandate followed; acceptance/payment retained; unresolved topics referred.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for Current sales page:6% rate, retail licence,15,000 electronic threshold, paper alternative, monthly/quarterly/annual schedules and approval footnote. | https://dor.sc.gov/sales-use-tax-index/sales-tax | 2026-11-13 |
| Read for Remote-seller definition, exceeds 100,000 current/prior test, physical nexus, second-month collection start,50 licence and taxable services/use/local FAQs. | https://dor.sc.gov/sales-use-tax-index/sales-tax/remote-sellers | 2026-11-13 |
| Read for Current Title 12 Chapter 36:910/920/1110/1310/2110 and 2120 medical, residential energy, food, holiday, IMF exceptions; neighboring conditions read. | https://www.scstatehouse.gov/code/t12c036.php | 2026-11-13 |
| Read for ST-500 effective 1 May 2026: entire county map/rate table, Williamsburg change notice and exclusion of Catawba/direct local taxes. | https://dor.sc.gov/sites/dor/files/forms/ST500.pdf | 2026-11-13 |
| Read for Manual chapter 10, September 2025:5%,500 maximum, no SCDOR local, IMF, leases, boats/trailers, motor vehicles/nonresident and manufactured-home clauses.2025-2026 filing cycle. | https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_10.pdf | 2026-11-13 |
| Read for Manual chapter 9, September 2025:partial exemptions, food/local exception, medical/DME/residential energy, manufacturing/agriculture and holiday list.2025-2026 filing cycle. | https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_9.pdf | 2026-11-13 |
| Read for Manual chapter 12, September 2025:local levy types, delivery and item-specific exemptions; dates distinguished from 2026 map.2025-2026 filing cycle. | https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_12.pdf | 2026-11-13 |
| Read for RR12-1:all questions/conclusions and neighboring discussion of tangible/electronic software and taxable ASP access; 2025 manual corroboration read. | https://dor.sc.gov/sales-use-tax-electronically-delivered-software | 2026-11-13 |
| Read for Manual chapter 7, September 2025:true-object test, professional services, software footnote.2025-2026 filing cycle. | https://dor.sc.gov/resources-site/lawandpolicy/Documents/SandU_7.pdf | 2026-11-13 |
| Read for Current Chapter 117 regulations:117-306/306.1/306.2 repair parts/labor,117-313 installation/fabrication,117-314 contractors, neighboring examples. | https://www.scstatehouse.gov/coderegs/Chapter%20117.pdf | 2026-11-13 |
| Read for ST-3 all 3 pages:gross sales/use purchases, exemption worksheet, ST-389 integration, line 7 discount and fiscal cap; current unyear-marked form. | https://dor.sc.gov/sites/dor/files/forms/ST3.pdf | 2026-11-13 |
| Read for Title 12 Chapter 54 fetched for assessment framework; exact legacy penalty/interest claims not established and held unconfirmed. | https://www.scstatehouse.gov/code/t12c054.php | 2026-11-13 |

Not yet confirmed: final 2026 ST-3/ST-389 line/code updates and post-May locality changes; detailed marketplace exclusions, all certificate mappings/retention/good-faith protections, SST membership, digital goods/mixed cloud services, precise special medical/manufacturing/agriculture/SCATE uses, holiday event terms, IMF/private-transfer/nonresident vehicle exceptions, local hospitality and penalty/interest/VDA calculations. Sources are primary state materials; historical 2025 manual sections are labeled 2025-2026 filing cycle and current law controls. No old subject is silently dropped.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sc-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sc-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
