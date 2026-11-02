---
name: netherlands-bookkeeping
description: Use this skill whenever asked about Dutch bookkeeping, chart of accounts, financial statements, RGS mapping, jaarrekening preparation, balance sheet or P&L format in the Netherlands. Trigger on phrases like "Dutch bookkeeping", "boekhouding", "grootboekrekening", "jaarrekening", "RGS", "chart of accounts Netherlands", "balans", "winst- en verliesrekening", "micro-entity Netherlands", "BW2 Title 9", "Dutch GAAP", "RJ guidelines", "small company accounts NL", "annual accounts Netherlands", or any question about recording transactions, financial reporting, or accounting standards for Dutch entities.
version: 1.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands bookkeeping and year-end reporting — 2026

Figures are for tax year 2026 unless a historical transition is expressly identified. [2026 official tax guidance](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026)

## Ask the client first

Use this method for a Dutch business's records, transaction classification, reconciliations, tax-adjustment schedules and annual-reporting handoff. Identify the legal entity before applying a tax rule: a sole trader, partnership and BV do not have interchangeable accounts, owner transactions or filing obligations. This covers the European Netherlands; obtain separate rules for Caribbean jurisdictions.

- Ask for the legal form, KVK and tax identifiers, financial-year dates, activity, VAT schemes, payroll status, group structure and reporting framework. Obtain the prior signed accounts, opening trial balance, tax returns and assessments, contracts, complete bank and cash records, sales and purchase invoices, stock count, asset register, payroll summaries, loans and owner-current-account details. Identify missing periods and unresolved opening balances before producing a final return or filing.

BV/NV and other specified legal persons normally file annual accounts at KVK; a sole trader has no KVK annual-accounts publication obligation. Do not infer an exemption merely from low turnover. [KVK filing scope](https://www.kvk.nl/deponeren/jaarrekening-deponeren/)

## The method, step by step

1. Confirm the entity, tax period, reporting framework and applicable schemes; reconcile opening balances.
2. Collect source documents, build the ledger mapping and preserve digital records.
3. Post transactions from evidence, applying invoice/VAT timing separately from profit recognition.
4. Reconcile balances and record supported year-end adjustments; prepare separate commercial and fiscal schedules.
5. Establish annual-accounts scope, size class and the actual preparation/adoption/filing dates.
6. Resolve exceptions, obtain approval and retain the filed return/accounts and acceptance evidence.

The sections below give the decision rules and supporting official sources for these steps.

## Set up the ledger and evidence trail

The administration must allow the tax authority to check the returns. Include original business correspondence and contracts, invoice copies, bank statements, cash notes, software/data and supporting calculations; keep hours and mileage evidence when a claim depends on it. Retain a bridge between the ledger, tax returns and accounts. [Administration duties](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/administratie/)

Use the following **illustrative internal structure**. It is a working layout, not prescribed Dutch account numbering or a ready-made RGS mapping:

| Ledger group | Separate accounts and checks |
|---|---|
| Fixed assets | Intangibles, equipment, buildings, accumulated depreciation, disposals |
| Working assets | Inventory, work in progress, trade debtors, other receivables, prepayments |
| Money | Each bank/currency account, cash, payment-provider clearing, transfers in transit |
| Equity | Capital, reserves, retained result; separate sole-trader contributions/drawings |
| Liabilities | Trade creditors, loans, accruals, customer advances, taxes, payroll and pension liabilities |
| Sales | Goods/services, returns and discounts; VAT classification separately |
| Costs | Purchases, stock movement, payroll, rent, software, travel, professional fees, depreciation, interest |
| Tax adjustments | Separate reconciliation of private, limited-deduction and tax-only items |

RGS is an open reference standard. Its core identifier is an alphabetical reference code; an arbitrary four-digit software account is not automatically an official RGS code. Preserve the software's actual account identifiers, document the supported RGS version and mapping, and check mapped totals against the trial balance. Auditfile exports help examination but do not replace underlying evidence. [RGS and Auditfile guidance](https://www.belastingdienst.nl/wps/wcm/connect/nl/ondernemers/content/gemakkelijk-administreren-aangifte-doen-en-betalen)

## Keep records retrievable

Retain core tax records for seven years; property and relevant OSS records have a ten-year period. The clock begins when records cease to have current relevance, so an ongoing contract is not simply discarded seven years after signing. Agree any permitted shorter retention for non-core data with the tax authority in writing. [Retention periods](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/)

Preserve original digital records and the ability to inspect them. Merely printing computer records and deleting the files is generally insufficient; the authority describes a limited small-administration exception. When changing systems, export the ledger, attachments and mapping and check their readability before losing the old system. [Digital retention](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/administratie_bewaren/hoe_bewaart_u_uw_administratie)

## Invoice and VAT controls

For an ordinary mandatory invoice, check supplier/customer names and actual addresses, supplier VAT ID, KVK number where registered, issue date, unique sequential invoice number, supply/advance date, description and quantity/extent, net consideration and unit price where relevant, rate and VAT amount. Multiple rates need separate amounts. Simplified and cross-border invoices require their own rule check. [Invoice contents](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/facturen_maken/factuureisen/)

Normally issue the invoice by the fifteenth day of the following month. Advance payments and international transactions have specific rules. Digital invoices also need recipient agreement and preserved authenticity, integrity and readability. [Invoice issue rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/facturen_maken/)

Link every posting bidirectionally to its invoice. Store customer VAT ID when required, and keep consideration and VAT separately by rate. Do not classify an export, exemption or reverse charge merely from the bank's country code. [Invoice records](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/administratie_bijhouden/wat_administreert_u_voor_de_btw/uitgaande_facturen_administreren)

Under the invoice VAT system, use the invoice timing rules, including the period in which an overdue invoice should have been issued; do not wait for payment. Under an applicable cash VAT scheme, output VAT generally follows receipts, while input VAT still follows qualifying received invoices and invoice-date timing. Cash VAT eligibility must be established; it does **not** establish a cash basis for profit or annual accounts. [Invoice VAT rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/bereken_het_bedrag/hoe_berekent_u_het_btw_bedrag/factuurstelsel) [Cash VAT rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/bereken_het_bedrag/hoe_berekent_u_het_btw_bedrag/kasstelsel/)

KOR participation means no VAT charged, generally no periodic VAT returns and no deduction of VAT on business costs/investments. Purchase invoices remain necessary; incidental returns and revision of previously deducted VAT can still arise. Monitor the €20,000 calendar-year turnover ceiling across the same entrepreneur's subnumbers, and examine the transaction that crosses it immediately. Do not assume low turnover automatically enrols a business. [KOR consequences](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling/)

## Transaction posting and reconciliation

The following are bookkeeping controls implementing the evidence and reconciliation duties, not statutory bank-description classifications:

- Match a sale to its invoice/contract and delivery; post debtor, revenue and VAT classification, then clear the debtor on settlement.
- Match a purchase to supplier evidence and business purpose; separate deductible VAT from the cost/asset and retain non-deductible VAT in the appropriate cost basis.
- Treat a payment-provider payout as a settlement: reconcile gross sales, refunds, fees and amounts still receivable. Booking the net payout as sales understates both revenue and fees.
- Match transfers between own accounts on both sides. A bank loan receipt is a liability movement, not sales; repayment of principal is not operating expense. Classify interest separately after eligibility review.
- Separate owner contributions/drawings from business income/cost. For a BV, establish whether an owner payment is salary, reimbursed expense, loan/current-account settlement or dividend; obtain the supporting decision and payroll/tax treatment.
- A bank narration such as iDEAL, Tikkie, SEPA or BELASTINGDIENST is a search clue, not proof of accounting treatment. Reconcile VAT and payroll remittances to their liabilities; distinguish assessments, interest, penalties and other taxes.

At each close, reconcile bank opening balance plus movements to the statement closing balance; cash to actual cash; debtor/creditor control accounts to ageing; payroll to payslips and declarations; VAT to filed returns; assets to register; loans to lender statements; and transfers/clearing accounts to identifiable outstanding items. Investigate unexplained balances instead of posting a balancing expense. Maintain a dated adjustment log with document reference, preparer and reason. [Administration duties](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/administratie/)

## Profit timing, inventory and reporting schedules

For income-tax businesses, derive fiscal profit from the commercial P&L and balance sheet with the necessary fiscal adjustments. Sound business practice requires a consistent method. Include cut-off, unpaid invoices, accruals and prepayments rather than treating all bank movements as the year's profit. Work in progress requires progressive recognition including attributable costs and profit; do not simply defer all profit until completion. Inventory valuation requires a consistent permissible system. [Fiscal profit and balance-sheet guidance](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/winst_en_verliesrekening_en_balans)

Prepare these internal schedules, adapting the final presentation to the entity's approved reporting framework:

- **P&L:** sales less returns; inventory/work-in-progress movement; purchase costs; staff and other operating costs; depreciation; financial result; tax charge where applicable; final result.
- **Balance sheet:** fixed assets and accumulated depreciation; inventory/WIP, receivables, prepayments and cash; equity/reserves; provisions; long-term and current liabilities. Reconcile total assets to total equity and liabilities.
- **Equity bridge:** opening equity, profit/loss, contributions, distributions/drawings and other supported movements to closing equity.
- **Tax bridge:** commercial profit to taxable profit, with permanent differences, timing differences, investment deductions and tax-specific adjustments individually supported.

These are reconciliation layouts, not a claim that every Dutch company must use one vertical balance sheet model. For statutory accounts, confirm the applicable Dutch company-law/RJ or IFRS framework and disclosure requirements with the responsible accountant. Do not automatically apply tax depreciation as commercial depreciation or assume simplified public filing removes internal accounting duties. Refer complex contracts, consolidation, provisions, deferred tax, financial instruments and changes of accounting policy for framework-specific review.

## Costs, private use and the tax bridge

Classify the business purpose before calculating deduction. Personal expenses, fines, home-workspace rules, ordinary clothing and training for a new profession need separate treatment. A payment labelled travel, training or rent is not automatically fully deductible. Keep ordinary business costs, mixed expenses and private items in distinct accounts. [Cost restrictions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten/overzicht-mogelijk-aftrekbare-zakelijke-kosten)

For eligible limited-deduction expenses in an income-tax business, the 2026 annual threshold is €5,700; alternatively deduct 80% of that eligible pool. The corporate-tax percentage alternative is 73.5%, not 80%. A BV using the threshold route must have its separate corporate wage-related threshold and applicable rules checked; the income-tax flat threshold alone is not a complete BV calculation. Do not apply a blanket rule based on a client's gift exceeding an invented per-gift minimum. VAT deductibility is a separate question. [2026 limited expenses](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026)

For an income-tax entrepreneur's privately owned or privately rented vehicle, current 2026 guidance allows €0.25 per business kilometre. Fuel, insurance, parking and tolls cannot additionally be deducted from profit under that method. Keep a mileage record and do not substitute the older-year amount. [2026 private-vehicle deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/zakelijk-gebruik-privevervoermiddel-2026)

For a business vehicle, obtain first-admission date, value, emissions, age, private mileage and supporting records before determining the income-tax/private-use addition. Do not apply a single historic electric-car rate to all vehicles. VAT private-use adjustment is separate: commuting counts as private for VAT although it is business mileage for income-tax purposes. Keep those records and calculations distinct. [Income-tax private use](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/privegebruik_auto/) [VAT private use](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/btw_en_de_auto/privegebruik_auto_van_de_zaak/)

## Assets and investment deductions

For tax purposes, an asset used for several years normally goes on the balance sheet. A business asset costing **less than €450** can be expensed immediately; an item exactly at the boundary is not covered by that shortcut. Establish what constitutes the actual asset, the cost basis and recoverable VAT before applying it. [Asset versus expense](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/)

Ordinary annual tax depreciation follows cost less residual value over estimated useful life, subject to a ceiling of 20% of original cost; acquired goodwill has a 10% ceiling. Prorate for part-year use and stop at residual value. These are ceilings, not automatic rates for every asset. Buildings and special depreciation regimes need separate rules. [Depreciation calculation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving)

For buildings, exclude land from depreciation and use the actual acquisition/useful-life/residual-value calculation. The normal fiscal floor is the WOZ value. The old half-WOZ rule is not the current general rule for owner-occupied property. An income-tax transition can retain that old floor only until three years after first use for qualifying buildings already in use before 2024 with less than three years' depreciation then. Obtain first-use date and historic deductions before applying this exception. [Building depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/afschrijving_bedrijfspand)

KIA is a separate tax deduction, not a reduction of invoice cost or a substitute for depreciation. For 2026, the published table starts at €2,901 and ends at €398,236 of qualifying annual investment; the first band through €71,683 gives 28%. Use the full official table for higher totals. Check asset exclusions, commitment/use/payment timing and partnership allocation before calculating a claim; assets below €450 do not qualify for KIA. [2026 KIA table](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026) [KIA eligibility](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/kleinschaligheidsinvesteringsaftrek_kia)

## Annual accounts and KVK filing

Establish legal-form obligations and the correct size class using both the current and previous financial years, including relevant group data. KVK describes a two-year, two-criteria size test using assets, turnover and employee count. Its overview is a screening aid; obtain the applicable statutory boundary and group/start-up rules before classifying a borderline entity. Public micro accounts contain a limited balance sheet; small accounts include an abbreviated balance sheet and notes. Medium/large publications are broader, with management/reporting and audit material. Do not conclude that any company with a small standalone balance has no audit or consolidation obligation. [KVK size and publication overview](https://www.kvk.nl/deponeren/waaruit-bestaat-de-jaarrekening/)

For a BV, schedule preparation within five months after year-end; shareholders can extend preparation by up to five months for special circumstances. File within eight days after adoption. Apply the statutory preparation/adoption timetable: ordinarily five months for preparation plus two months for adoption, extended only by a valid preparation extension; once adopted, the eight-day filing clock applies; if adoption is late, file the prepared unadopted version and later the adopted version. Publication cannot exceed twelve months after year-end. Where all shareholders are also directors, signing commonly constitutes adoption and removes the additional adoption period; check the articles and conditions. With maximum valid preparation extension, that route normally requires filing within ten months and eight days. Treat the twelve-month limit as an outer limit, not permission to ignore earlier deadlines. [BV filing timetable](https://www.kvk.nl/deponeren/uiterste-termijn-deponeren-jaarrekening/)

Micro, small and medium legal persons file digitally in XBRL; from financial year 2025 large legal persons also have a digital-filing requirement. Use the applicable KVK portal/software route and preserve acceptance evidence. [Digital filing requirements](https://www.kvk.nl/hulp-en-contact/deponeren/) Check the company's filed year in the Handelsregister; saving an accounts file locally is not filing. [Confirm filed accounts](https://www.kvk.nl/deponeren/controleer-je-jaarrekening/)

## Worked and decision checks

All amounts below are hypothetical and do not establish eligibility on their own. Calculations are illustrative, with exact arithmetic here; use the applicable return's rounding instructions at filing.

**A — Depreciation ceiling.** An ordinary machine costs €5,000, has €500 residual value and an estimated three-year life; it is used for the full year and has no special depreciation relief. Economic depreciation is €1,500, but the annual tax ceiling is €1,000. Record separate commercial and fiscal schedules if the reporting framework requires this difference. [Depreciation calculation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving)

**B — Mixed expenses.** An income-tax business has €6,000 of eligible mixed expenses, no excluded private amounts and chooses the percentage alternative. Deduction is €4,800 and the add-back is €1,200. Under the flat-threshold alternative only €300 would be deductible. A BV cannot reuse this 80% calculation. [2026 limited expenses](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026)

**C — Private vehicle.** An income-tax entrepreneur supports 800 business kilometres in a private vehicle during 2026. Profit deduction is €200. Parking is already included in the method and cannot be added to that profit deduction. [2026 private-vehicle deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/zakelijk-gebruik-privevervoermiddel-2026)

**D — KOR purchase.** A participating entrepreneur buys equipment with VAT on the invoice. Do not post recoverable input VAT merely because the purchase is business-related; the KOR blocks that deduction. Preserve the invoice and examine the capitalisation cost including irrecoverable VAT. [KOR consequences](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling/)

**E — Own transfer.** A statement shows a debit to another account owned by the same business. Match the receiving statement and clear transfer-in-transit. Without that evidence, leave an explained investigation item; do not infer an expense from the SEPA label. [Administration duties](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/ondernemen/administratie/)

**F — VAT versus profit.** A cash-VAT business supplies a service before year-end and receives payment after year-end. Determine output VAT using the applicable cash scheme, but separately assess the contract, earned income and year-end debtor under profit rules. Do not move the accounting revenue solely because VAT follows cash. [Cash VAT rules](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/bereken_het_bedrag/hoe_berekent_u_het_btw_bedrag/kasstelsel/) [Fiscal profit and balance-sheet guidance](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/winst_en_verliesrekening_en_balans)

**G — Filing clock.** A BV has adopted its accounts before the outer annual limit. Schedule filing within eight days of adoption; do not wait for that outer limit. If shareholder/director identity or articles are missing, resolve them before calculating the adoption timetable. [BV filing timetable](https://www.kvk.nl/deponeren/uiterste-termijn-deponeren-jaarrekening/)

**H — Asset boundary.** A durable asset costs exactly €450 on its established tax cost basis. It does not meet the less-than-€450 immediate-expense rule. Evaluate normal capitalisation/depreciation and separately test KIA eligibility. [Asset versus expense](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/) [KIA eligibility](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/kleinschaligheidsinvesteringsaftrek_kia)

## When to refuse or refer

Deliver the reconciled trial balance, transaction exceptions, draft balance sheet/P&L, asset schedule, VAT/payroll reconciliations, tax bridge, size-class assessment and filing calendar. Show the chosen period, evidence references, assumptions and unresolved decisions. Obtain the responsible person's approval before filing.

- Stop and request the missing evidence where the opening balance cannot be reconciled, an invoice or business purpose is unsupported, a group/size boundary is unclear, private-use records are missing or a contract requires specialist accounting judgment. Do not invent amounts to balance the books. Use the Netherlands VAT, income-tax, corporate-tax and payroll Guides for their complete calculations; a bookkeeping classification alone does not establish the tax result.

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
