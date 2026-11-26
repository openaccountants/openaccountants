---
name: netherlands-bookkeeping
description: Use this skill for Dutch bookkeeping and year-end reporting in 2026, the ledger and evidence trail, record retention, invoice and VAT controls, posting and reconciliation, profit timing, limited-deduction costs, vehicles, assets, depreciation, KIA and the KVK annual accounts timetable. Trigger on Dutch bookkeeping, boekhouding, grootboekrekening, jaarrekening, RGS, chart of accounts Netherlands, balans, winst- en verliesrekening, micro-entity Netherlands, BW2 Title 9, Dutch GAAP, RJ guidelines, or annual accounts Netherlands.
version: 2.1
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: bookkeeping
type: situation-rules
---

# Netherlands bookkeeping and year-end reporting, tax year 2026

## Scope

Use this Guide for European Netherlands records, reconciliations, tax bridges and the annual-accounts handoff. Establish the entity and actual reporting year first; the income-tax examples are not BV computations. For Caribbean jurisdictions: Check this point with one of our partner accountants.

## Ask the client first

Obtain legal form, identifiers, financial-year dates, activities, VAT schemes, payroll and group details; the reporting framework; prior signed accounts and opening trial balance; returns, assessments, contracts, bank/cash records, invoices, stock count, asset register, payroll, loans and owner balances. Identify missing periods before finalising anything.

## The method, step by step

1. Reconcile opening balances and collect evidence.
2. Map the ledger; post from documents and contracts, with VAT and profit timing assessed separately.
3. Reconcile bank, cash, debtors/creditors, payroll, VAT, assets, loans and clearing accounts. Investigate differences; never invent a balancing expense.
4. Prepare the adjusted trial balance, P&L, balance sheet, equity bridge and commercial-to-fiscal tax bridge. Record each adjustment's date, evidence and reason.
5. Establish reporting, adoption and filing requirements; obtain approval and preserve submitted documents and acceptance evidence.

### Records and ledger

The administration must let the authority check returns. Retain invoices, bank/cash records, contracts, correspondence, software/data and calculations linking the administration, returns and accounts. Keep hours/mileage evidence where relevant. [Administration duties](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/administratie/)

Suggested internal groups are fixed assets, working assets, money, equity, liabilities, sales, costs and tax adjustments. Within them separate inventory/WIP, receivables/prepayments, each bank/cash/clearing account, owner movements, taxes/payroll/pensions, loans, depreciation and interest. These are working groups, not prescribed account codes or statutory statement models. Preserve the software's identifiers and reconcile any RGS mapping to the trial balance. RGS is an open standard whose core is an alphabetical reference code. Auditfile exports assist examination; keep the underlying records too. [RGS](https://www.belastingdienst.nl/wps/wcm/connect/nl/ondernemers/content/gemakkelijk-administreren-aangifte-doen-en-betalen) [Records](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/administratie/)

| Record | Retention | Source |
|---|---|---|
| Core records | 7 years after current relevance ceases; an ongoing contract's clock does not start at signing | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/ |
| Property and rights over property | 10 years | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/ |
| Supplies under the Union or import OSS scheme | 10 years | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/ |

Shorter periods for other data need a written agreement with the authority. Preserve the original digital/paper form. Printing and deleting digital files is allowed only for a small administration checkable within a reasonable time; digital programs/files must remain usable for examination. Before changing systems, test exported ledgers, mappings and attachments. [Retention](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/) [Digital records](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/hoe_bewaart_u_uw_administratie)

### Invoices and VAT

For an ordinary mandatory invoice, check both parties' names and actual addresses, supplier VAT ID, KVK number if registered, issue date, unique sequential number, supply/advance date, goods/quantity or service/extent, net amount, applicable unit price, rate and VAT. Separate amounts for different rates. Digital invoicing requires recipient agreement and authenticity, integrity and readability. [Contents](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/facturen_maken/factuureisen/) [Digital invoices](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/facturen_maken/)

Under the ordinary invoice system, invoice by the fifteenth day of the following month; declare output VAT by invoice date, or the period when a late invoice should have been issued. Input VAT requires receipt of a qualifying invoice and follows invoice-date timing. Keep separate records by rate. [Invoice system](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/bereken_het_bedrag/hoe_berekent_u_het_btw_bedrag/factuurstelsel)

An established cash-VAT scheme normally follows receipts for output VAT; input VAT still follows received invoices and their dates. Private-use VAT can arise without receipts. This VAT scheme does not decide fiscal profit recognition. [Cash VAT](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/bereken_het_bedrag/hoe_berekent_u_het_btw_bedrag/kasstelsel/) [Profit](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/winst_en_verliesrekening_en_balans)

For an established KOR participant's ordinary covered supplies, charge no VAT and recover no input VAT on costs/investments; retain purchase invoices. Incidental returns and revision of earlier deductions may remain necessary. Aggregate all subnumbers of the same entrepreneur when monitoring the EUR 20,000 calendar-year ceiling. The crossing supply itself loses exemption, not only its excess. Entry eligibility, counted turnover and excluded supplies require the separate checks below. [KOR consequences](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling/) [Crossing the ceiling](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor)

For posting, match sales/purchases to invoices, contracts, delivery and business purpose; reconcile provider payouts to gross sales, refunds, fees and outstanding amounts. Match both sides of own transfers. Trace loans, principal/interest, owner contributions/drawings and BV salary, reimbursement, current-account or dividend movements to their supporting documents before determining treatment. iDEAL, Tikkie, SEPA, KVK, pension-fund, card/ATM and BELASTINGDIENST narrations are search clues, not classifications. Reconcile tax remittances to the relevant liabilities and assessments. [Evidence and reconciliation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/administratie/)

### Profit and tax bridge

For income-tax businesses, apply fiscal rules to the commercial P&L and balance sheet; follow consistent sound business practice. Review cut-off, debtors, unpaid costs, accruals/prepayments, inventory and WIP. Tax WIP/unfinished assignments are valued at the attributable agreed consideration; profit is taken progressively, including attributable direct costs, the constant share of overhead and profit. Detailed contract and inventory applications are held below. [Wet IB arts. 3.25, 3.29b](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-01-01_1/xml/BWBR0011353_2026-01-01_1.xml) [2026 explanation, §§7.1–7.3](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/winst_en_verliesrekening_en_balans)

Prepare internal P&L, balance-sheet, equity and tax bridges; reconcile assets to equity/liabilities and opening equity plus result/contributions/distributions to closing equity. Select statutory presentation and commercial measurement separately. Tax depreciation is not automatically commercial depreciation.

### Costs and assets

| Income-tax rule, 2026 | Amount and conditions | Source |
|---|---|---|
| Eligible limited expenses | First EUR 5,700 not deductible, or elect 80% deduction on the return; scope and exceptions below | Wet IB art. 3.15: https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-01-01_1/xml/BWBR0011353_2026-01-01_1.xml |
| Own privately held or privately rented transport | EUR 0.25 per business km under the policy approval, retroactive to 1 January 2026; fuel, insurance, tolls and parking not separately deductible | §2.2: https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html; [included costs](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/zakelijk-gebruik-privevervoermiddel-2026) |
| Low-value asset shortcut | Less than EUR 450 on the established cost basis; exactly EUR 450 does not qualify | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/ |
| Ordinary annual tax depreciation ceilings | Other assets 20% of cost; acquired goodwill 10%; ceilings, not automatic rates; residual value/useful life and part-year use still govern | Wet IB art. 3.30: https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-01-01_1/xml/BWBR0011353_2026-01-01_1.xml; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving |

The limited-expense pool covers food/drink, representation and congresses/seminars/excursions/study trips, including associated travel/stay. The restriction does not apply insofar as the business directly manufactures/trades the relevant goods or supplies related services and those items form part of turnover. Under art. 3.15(4), no private withdrawals are recognised for these costs in respect of the taxpayer personally. Related private-vehicle costs first use the kilometre ceiling before the limitation. Exclude separately disallowed costs before using the pool. For ordinary private-vehicle case C, assume the kilometres are unrelated to this limited-expense pool. [Wet IB art. 3.15](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-01-01_1/xml/BWBR0011353_2026-01-01_1.xml) [2026 kilometre approval, §2.2](https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html)

The corporate-tax percentage alternative is 73.5%. The BV threshold route and employee/wage-base conditions require their own calculation; do not reuse the flat income-tax threshold. Check this point with one of our partner accountants. [Wet Vpb art. 8(5)](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml)

For ordinary acquired assets, establish cost, residual value and useful life. Deductible purchase VAT is excluded from the depreciation basis; irrecoverable VAT is included. Prorate for part-year use. For a building, exclude land from the depreciation calculation and stop at its fiscal WOZ floor. The income-tax transition permits the old 50% WOZ floor only until three years after first use for an own-use building first used before 2024 with fewer than three years' depreciation then. Special asset regimes/complex ownership are held below. [Depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving) [Buildings](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/afschrijving_bedrijfspand)

KIA is a separate profit deduction, not a reduction of asset cost. Keep a separate investment schedule. Assets costing less than EUR 450 are excluded; the annual totals alone do not establish eligibility. The 2026 official table has no deduction through EUR 2,900, 28% at EUR 2,901–71,683, EUR 20,072 at EUR 71,684–132,746, then EUR 20,072 less 7.56% of investment above EUR 132,746 through EUR 398,236; above that no deduction. Asset exclusions, commitments, payment/use timing and partnership allocation are held below before calculating a claim. [2026 table](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026) [Eligibility](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/kleinschaligheidsinvesteringsaftrek_kia)

### Annual accounts and filing

For an ordinary unlisted BV, prepare accounts within five months after year-end; the general meeting may extend by up to five months for special circumstances. File within eight days after adoption. If unadopted two months after the preparation period ends, publish the prepared accounts without delay, marked unadopted; publish the adopted version later. The absolute publication limit is twelve months after year-end. [BW2 arts. 210, 394](https://wetten.overheid.nl/BWBR0003045/2026-07-01)

All directors and supervisory directors sign or explain missing signatures. Signing also adopts a BV's accounts only if all shareholders are directors, all other meeting-right holders had access and consented to that adoption method, and the articles do not exclude it. Apply the eight-day clock then; do not add another two-month period. [BW2 art. 210(2), (5)](https://wetten.overheid.nl/BWBR0003045/2026-07-01)

For micro/small/medium legal persons, KVK requires digital XBRL filing; large legal persons also file digitally from financial year 2025. Confirm the filed year appears in the register and retain acceptance evidence. Size, public-document scope, audit/consolidation and technical exceptions are held below; a small standalone balance does not establish relief. [KVK digital filing](https://www.kvk.nl/hulp-en-contact/deponeren/)

## Boundary and exception table

Each referral below is a non-usable hold on that particular determination.

| Point requiring a separate determination | Action |
|---|---|
| Ordinary/simplified/cross-border invoice applicability; advances, continuous supplies, non-invoiced supplies and VAT timing exceptions; cash-VAT eligibility; export/exemption/reverse charge and customer VAT-ID requirements | Check this point with one of our partner accountants. |
| KOR entry/current and prior turnover tests, counted turnover, excluded supplies, incidental returns, revisions, import-scheme/property-letting interaction | Check this point with one of our partner accountants. |
| Business-purpose/private costs; fines, income/corporate tax, home workspace, clothing and training; gifts, hospitality VAT, zelfstandigenaftrek, startersaftrek, MKB exemption and other deduction restrictions | Check this point with one of our partner accountants. |
| Business-vehicle additions, electric/older cars, private mileage, commuting and separate VAT private-use calculations | Check this point with one of our partner accountants. |
| Special depreciation, self-created intangibles, building ownership/WOZ allocation and investment-deduction eligibility, higher-band rounding or partnership allocation | Check this point with one of our partner accountants. |
| Specific revenue/long-term contracts, inventory methods, consolidation, provisions, deferred tax, instruments and policy changes under Dutch GAAP/RJ/IFRS; commercial depreciation | Check this point with one of our partner accountants. |
| Entity/sole-trader publication scope; micro/small/medium size eligibility, prior years/group/start-up/excluded entities; tax-basis accounts, notes, management/cash-flow statements, audit/consolidation relief; listed/special-entity filing and technical exceptions | Check this point with one of our partner accountants. |

## Worked cases

All original amounts are hypothetical; eligibility is assumed only as stated. Arithmetic is exact here; return rounding requires its own instructions.

**A: Depreciation ceiling.** An ordinary acquired machine costs EUR 5,000, residual EUR 500, life three years, full-year use, no special relief. Economic depreciation is EUR 1,500; the ordinary tax ceiling limits the fiscal amount to EUR 1,000. Commercial treatment remains subject to the selected framework. [Tax calculation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving)

**B: Mixed expenses.** An income-tax business has EUR 6,000 of eligible art. 3.15 costs after all exclusions and private-vehicle limits; no turnover-supply exception. Electing 80% gives EUR 4,800 deduction and EUR 1,200 add-back. The threshold method gives EUR 300; the percentage route improves deduction by EUR 4,500. Do not reuse this for a BV. [Wet IB art. 3.15](https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-01-01_1/xml/BWBR0011353_2026-01-01_1.xml)

**C: Private vehicle.** An income-tax entrepreneur supports 800 qualifying business kilometres in a private vehicle during 2026, unrelated to limited expenses. At EUR 0.25 the deduction is EUR 200; no extra parking deduction. The policy approval governs this 2026 rate; it expires on 1 January 2027, so later-year treatment is not established here. [Approval §§2.2, 3](https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html)

**D: KOR purchase.** An established KOR participant buys business equipment with VAT. No input VAT deduction; include irrecoverable VAT in the asset's tax cost. [KOR](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling/) [Cost basis](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving)

**E: Own transfer.** A debit appears to go to the business's other account. Match the receiving statement and clear transfer-in-transit; without evidence, retain an investigation item. The SEPA label alone establishes no expense. [Evidence](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/administratie/)

**F: VAT versus profit.** An established cash-VAT business supplies a service before year-end and receives payment after year-end. Check output VAT under that scheme and separately determine earned income and the debtor under fiscal profit rules. The contract-specific profit answer remains referred above. [Cash VAT](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/bereken_het_bedrag/hoe_berekent_u_het_btw_bedrag/kasstelsel/) [Profit](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/winst_en_verliesrekening_en_balans)

**G: Filing clock.** An ordinary BV adopts before the outer annual limit: file within eight days, constrained by that limit. Resolve signatures, other meeting-right holders, articles and actual adoption before setting the timetable. [BW2 arts. 210, 394](https://wetten.overheid.nl/BWBR0003045/2026-07-01)

**H: Asset boundary.** A durable acquired asset costs exactly EUR 450 on its established tax cost basis. The less-than-EUR-450 shortcut does not apply. Assess ordinary depreciation and KIA eligibility separately. [Asset](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/) [KIA](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/kleinschaligheidsinvesteringsaftrek_kia)

```oa-check
name: Depreciation ceiling on a EUR 5,000 machine, 2026
inputs:
  cost: 5000
  residual: 500
  life_years: 3
  ceiling_rate: 0.20
steps:
  - economic: (cost - residual) / life_years
  - ceiling: cost * ceiling_rate
  - fiscal_depreciation: min(economic, ceiling)
expected:
  economic: 1500.00
  fiscal_depreciation: 1000.00
```

```oa-check
name: Mixed expenses EUR 6,000, 80% route versus EUR 5,700 threshold, 2026
inputs:
  mixed_costs: 6000
  pct: 0.80
  threshold: 5700
  business_km: 800
  km_rate: 0.25
steps:
  - pct_route_deduction: mixed_costs * pct
  - pct_route_addback: mixed_costs - pct_route_deduction
  - threshold_route_deduction: max(mixed_costs - threshold, 0)
  - better_route_gain: pct_route_deduction - threshold_route_deduction
  - vehicle_deduction: business_km * km_rate
expected:
  pct_route_deduction: 4800.00
  pct_route_addback: 1200.00
  threshold_route_deduction: 300.00
  better_route_gain: 4500.00
  vehicle_deduction: 200.00
```

## When to refuse or refer

Stop where evidence, opening balances, eligibility, framework or a referral above remains unresolved. Hand over the reconciled trial balance, exceptions, draft statements, asset schedule, VAT/payroll reconciliations, tax bridge and filing calendar with assumptions and evidence. Obtain responsible-person approval before filing. Use the Dutch VAT, income-tax, corporate-tax and payroll Guides for their separate calculations.

## Sources

| Source and bounded read | URL | Read on |
|---|---|---|
| Administration: evidence and reconciliation | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/administratie/ | 2026-11-26, read only the stated provisions |
| Retention: periods, current relevance, written agreements | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/ | 2026-11-26, read only the stated provisions |
| Digital records and small-administration exception | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/hoe_bewaart_u_uw_administratie | 2026-11-26, read only the stated provisions |
| RGS reference code and Auditfile | https://www.belastingdienst.nl/wps/wcm/connect/nl/ondernemers/content/gemakkelijk-administreren-aangifte-doen-en-betalen | 2026-11-26, read only the stated provisions |
| Ordinary mandatory invoice contents | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/facturen_maken/factuureisen/ | 2026-11-26, read only the stated provisions |
| Digital invoice conditions | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/facturen_maken/ | 2026-11-26, read only the stated provisions |
| Invoice timing, overdue invoices and input invoices | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/bereken_het_bedrag/hoe_berekent_u_het_btw_bedrag/factuurstelsel | 2026-11-26, read only the stated provisions |
| Cash receipts, private use and input invoices | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/bereken_het_bedrag/hoe_berekent_u_het_btw_bedrag/kasstelsel/ | 2026-11-26, read only the stated provisions |
| KOR consequences, subnumbers and special supplies | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling/ | 2026-11-26, read only the stated provisions |
| 2026 §§7.1–7.3: fiscal bridge and WIP | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/winst_en_verliesrekening_en_balans | 2026-11-26, read only the stated provisions |
| Wet IB arts. 3.15, 3.25, 3.29b, 3.30: operative wording | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0011353/2026-01-01_1/xml/BWBR0011353_2026-01-01_1.xml | 2026-11-26, read only the stated provisions |
| Policy approval §§2.2, 3: 2026 transport rate and expiry | https://zoek.officielebekendmakingen.nl/stcrt-2026-18302.html | 2026-11-26, read only the stated provisions |
| Low-value acquired assets | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/ | 2026-11-26, read only the stated provisions |
| Cost basis, useful life, ceilings and part-year use | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving | 2026-11-26, read only the stated provisions |
| Building calculation and income-tax transition | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/afschrijving_bedrijfspand | 2026-11-26, read only the stated provisions |
| Full 2026 KIA band table | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026 | 2026-11-26, read only the stated provisions |
| Separate deduction and low-value exclusion | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/kleinschaligheidsinvesteringsaftrek_kia | 2026-11-26, read only the stated provisions |
| BW2 arts. 210, 394: completed same-day annual-accounts proof reused | https://wetten.overheid.nl/BWBR0003045/2026-07-01 | 2026-11-26, read only the stated provisions |
| Digital filing: completed same-day KVK proof reused | https://www.kvk.nl/hulp-en-contact/deponeren/ | 2026-11-26, read only the stated provisions |
| Wet Vpb art. 8(5): percentage alternative; completed Dutch corporate-tax proof reused | https://repository.officiele-overheidspublicaties.nl/bwb/BWBR0002672/2026-01-01_0/xml/BWBR0002672_2026-01-01_0.xml | 2026-11-23, bounded operative read reused |
| KOR crossing transaction: completed Dutch VAT proof reused | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor | 2026-11-23, crossing-supply sentence reused |

Not yet confirmed: the precise determinations held in the boundary table, the BV threshold calculation and later-year transport treatment. They are non-usable referrals, not complete calculation instructions. No substantive RJ rule or authenticated filing screen is claimed as read.
