---
name: is-corporate-income-tax
description: >
  Prepare Iceland corporate income-tax workpapers for 2026 for resident
  limited companies and other separately taxable legal entities. Determine
  the legal-form rate, reconcile accounting profit to the tax base, support
  deductions, depreciation, participation deductions and loss carryforwards,
  screen group taxation and related-party finance, and reconcile assessment
  payments. Includes the separately identified 2026 filing cycle for 2025
  income. Use for ehf., hf., taxable partnerships, RSK 1.04 and annual tax
  reconciliations and approved research/development credits, cost ceilings and
  public-aid limits, and the stated financial-sector remuneration, additional
  profit and bank-liability taxes, conditional domestic mergers/splits and
  sole-trade incorporation. Other sector taxes, foreign credits, disputed
  restructuring cases, some financial instruments and independent Icelandic
  legal review require further work;
  this source-cited draft is not comprehensive country coverage.
jurisdiction: IS
category: international
tax_year: 2026
last_updated: 2026-10-23
version: 0.8
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland corporate income tax v0.8

## Who this applies to

Prepare **income-year 2026** workpapers for separately taxable Iceland-resident legal entities. Article 2 residence includes Icelandic registration, domicile under the constitution or actual management in Iceland. Confirm the legal form and separate-taxpayer status, including any partnership election; a business name alone does not establish the tax rate. Residents are taxed on worldwide income under Article 2. [Income Tax Act 90/2003, Article 2][law]

An individual's sole trade belongs in the [individual income-tax Guide](iceland-income-tax.md). Exempt bodies require Article 4 and Article 71(4)–(5) review: ordinary income-tax exemption does not itself settle capital-income tax. Non-residents require the source-category method in the [cross-border Guide](is-cross-border.md), rather than a blanket resident-company computation. [Articles 3–4, 70–71][law]

**Keep years separate.** A return labelled 2026 ordinarily reports **2025 income**. The official 2026 assessment page expressly uses that pairing. This Guide distinguishes the current 2026 income computation from confirmed 2026 filing/payment rules; no unissued 2027 deadline is inferred. [2026 assessment information][assessment]; [Article 59][law]

## Rates, bands and thresholds

Amounts are ISK. The rates below concern the ordinary statutory computation, before any applicable sector taxes or relief.

| Item | Rule for the stated period | Official source |
|---|---|---|
| Ordinary Article 2(1)(1)–(2) entities, including hf./ehf. | 20% of taxable income for 2026 | [Article 71(1)][law]; [2026 rates][rates] |
| Other separately taxable Article 2(1)(3)–(5) entities | 37.6% of taxable income for 2026 | [Article 71(2)][law]; [2026 rates][rates] |
| Dividends received by the specified higher-rate entities | Separate 22% treatment; do not apply 37.6% indiscriminately | [Article 71(3)][law] |
| Loss vintage | Unused qualifying trading losses from the ten years preceding the income year | [Article 31(8)][law] |
| Eligible closing business receivables/loans; inventory | Optional reductions up to 5%; reverse previously expensed prior-year reductions | [Article 31(3)–(4)][law] |
| Immediate expensing of an asset or asset group | Acquisition cost **below 600,000**, not equal to it | [Article 39][law] |
| Ordinary office equipment depreciation | 20%–35% of the statutory depreciation base | [Article 37(4)(a)][law] |
| Related-party financing, absent an exception | Excess above 100,000,000 limited to 30% of statutory profit; first 100,000,000 retained subject to ordinary deductibility | [Article 57b][law]; [2020 amendment](https://www.althingi.is/altext/stjt/2020.033.html) |
| Approved R&D credit | 35% for a supported small/medium classification; 25% for large enterprises; aid cumulation can reduce it | [Act 152/2009, Articles 3, 10 and 15][rd-law] |
| R&D annual eligible-cost ceiling | 1,100,000,000 across related applicants; the same ceiling applies to a qualifying cooperation project as a whole | [Article 10][rd-law] |
| Purchased R&D sublimit | 20% of the statutory ceiling, calculated as 220,000,000; supplier/project conditions also apply | [Article 10(5)][rd-law] |
| Special small-enterprise project approval | A project with planned annual cost no greater than 125,000,000 can receive two-year approval, subject to the statutory plans/report | [Article 9, amended by Act 27/2026][rd-law] |
| Ordinary domestic group-tax ownership screen | At least 90%, with approval and further conditions | [Article 55][law] |
| Financial activities remuneration tax | 5.5% of the supported Articles 4–5 base, including employer pension contributions before applicable exclusions | [Act 165/2011, Articles 4–6][fat-law]; [2026 employer notice][fat-notice] |
| Additional financial activities income tax | 6% of the applicable stand-alone base above 1,000,000,000, without group taxation or brought-forward losses | [Income Tax Act Article 71(3)][law] |
| Special tax on financial institutions' liabilities | 0.145% of the applicable year-end tax-return liabilities above 50,000,000,000, subject to the Act's own scope and exceptions | [Act 155/2010, Articles 2–4][bank-law] |
| 2026 assessment-year advances | 8.5% of 2025 assessed public levies at each due date; current guidance describes eight February–September payments totalling 68% | [Regulation 1370/2025, Articles 1–2][payment-reg]; [Advance-tax guidance][advances] |

The three financial-sector charges in the table are separate computations; the method below establishes their scope, bases and reconciliation. It does not cover every regulatory charge or transaction-specific financial instrument. The 2024 exceptional 21%/38.4% ordinary rates in transitional provision LXXVI do not replace the 2026 rates. [Article 71(3), transitional provision LXXVI][law]

## The base

### 1. Reconcile income and timing

Start with a reconciled trial balance and statutory accounts. Identify trading receipts, interest, dividends, gains, foreign items and related-party transactions. Article 59 ordinarily recognises income when the claim arises, subject to its uncertain-income rule. Bank receipts alone do not establish the income year. Under Article 61(2), legal-entity taxable income is statutory income less deductions permitted by Article 31. [Articles 7–8, 59, 61][law]

Prepare a bridge from accounting profit **before tax**. Add back book depreciation and any expenses not permitted for tax; replace them with the supported statutory depreciation/deductions. Reconcile provisions, reserves, share income, exchange differences and losses separately. Keep income-tax payments and withholding credits in a payment schedule, not as deductions from taxable profit. [Articles 31–50, 61, 112][law]

### 2. Support deductions and adjustments

| Area | Workpaper rule | Source |
|---|---|---|
| Operating expenses | Evidence the cost, relevant year and connection to acquiring, securing or maintaining income. Missing required payroll/contractor reporting can lead to deduction denial under the stated procedure. | [Article 31(1)][law] |
| Bad debts | Distinguish business-connected debts demonstrably lost from an accounting provision. For an elected up-to-5% closing reduction, verify the eligible base and reverse the prior year's expensed reduction. | [Article 31(3)][law] |
| Inventory | Establish the Article 73 valuation first; calculate the optional up-to-5% reduction once and reverse the prior year's expensed reduction. Do not duplicate a book write-down and tax deduction. | [Articles 31(4), 73(4)][law] |
| Gifts/donations | Review Article 31(2)'s recipient registration, qualifying purposes and limits; do not deduct all gifts under the general expense rule. | [Articles 31(2), 50(1)][law] |
| Fines and unlawful payments | Article 50 disallows the specified criminal penalties, related unlawful-gain costs and unlawful payments. Classify the actual charge; this is not a blanket conclusion about every interest or fee item. | [Article 50][law] |
| Interest and FX | Apply Article 49's business connection and timing rules. Its net exchange-loss rule spreads the qualifying net loss equally over three years; a book loss is not automatically the same-year tax deduction. Review related-party interest separately under Article 57b. | [Articles 49, 57b][law] |
| Start-up and specified development costs | Article 32 permits the stated cost classes to be written down in the year incurred or equally over five years; classify the cost before choosing that treatment. | [Article 32][law] |

Retain invoices, contracts, allocation evidence, payroll filings and the reconciliation to each return field. These are preparation controls implementing the cited rules; they do not establish an expense's eligibility without its facts.

### 3. Depreciation and disposals

Build an asset register showing original cost, category, business use, first-use date, prior tax depreciation, opening tax value, additions, disposals and closing value. Articles 33–36 define depreciable assets, first use and the base. Movable assets under Article 33(1) use cost less prior depreciation; other specified classes use original cost. Do not apply the office-equipment rate to buildings or purchased intangibles. [Articles 33–37][law]

Selected statutory ranges are 10%–20% for the specified ships/passenger vehicles and aircraft, 10%–30% for industrial machinery, 20%–35% for office equipment and the stated other movables, 1%–3% for residential/office/retail buildings, 15%–20% for purchased intellectual-property rights and 10%–20% for purchased goodwill. Other building classes have their own ranges. Determine the precise class and business use before selecting a rate. [Article 37][law]

Article 39's immediate-expense threshold is strictly below ISK 600,000 for the asset **or asset group**. Articles 35 and 45 address disposal/cessation years; an ordinary annual charge is not automatically available then. Article 42 generally leaves a 10% original-cost residual for Article 33(1)–(2) assets. Reconcile disposal proceeds, tax value and any gain/loss under the relevant disposal provisions instead of simply deleting the asset. [Articles 12–27, 33–45][law]

### 4. Dividends, share gains and losses

Article 31(9) provides a deduction for qualifying dividends received by the specified entity classes. It extends to foreign dividends only under its foreign-tax and rate conditions. Article 31(9a) addresses qualifying share gains and states that excess share-sale losses are neither generally deductible from other income nor carried forward as trading losses. Retain recipient/issuer classifications, dividend decisions, holding/disposal schedules and the evidence supporting foreign treatment. A group relationship alone does not establish a participation deduction. [Article 31(9), (9a)][law]

Keep higher-rate entities' Article 71(3) dividend treatment separate. Do not assume that the limited-company deduction or ordinary 37.6% rate resolves every partnership's dividend receipt. [Articles 31, 71][law]

### 5. Trading-loss schedule

For a calendar 2026 computation, the ordinary preceding-ten-year window covers **2016–2025**, subject to adequate original reporting, unused balances and the change-of-ownership/business rules. A 2015 vintage is outside that ordinary window. Retain origin, opening balance, prior use, eligible amount used now and closing balance for each vintage. Article 31(8) restricts use after material business/activity changes unless the ordinary-business-purpose condition is established; age alone is insufficient. [Article 31(8)][law]

Separate share-loss restrictions, foreign CFC losses and pre-group losses. Mergers/splits also require Article 54's loss-transfer conditions; unused losses do not automatically follow a purchase or reorganisation. This Guide supplies no loss carryback claim. [Articles 31(9a), 54–55, 57a][law]

### 6. Group taxation and related-party finance

Article 55 group taxation requires authority approval, at least 90% ownership, the same accounting year and all-year ownership subject to the stated new-entity/closure exceptions. It normally lasts at least five years; the statute also restricts restarting after termination. Apply at least **30 days before the applicable return deadline**. Current-year results are settled before brought-forward losses; losses from before group taxation remain usable only in their originating company. Do not consolidate separate returns merely because management prepares group accounts. [Article 55][law]

### 7. Related-party interest limitation

First establish that a financing cost is otherwise deductible under Articles 31 and 49, then apply arm's-length terms under Article 57 and the separate Article 57b limitation. The limitation covers related-party interest and discounts; do not net unrelated interest income against that gross pool without a legal basis. Keep principal, counterparty, related status, dates, rates, discounts and charges in the financing schedule. See the [transfer-pricing method](is-transfer-pricing.md). [Articles 31, 49, 57–57b][law]

For the **amount above ISK 100 million**, deduction is limited to 30% of Article 57b profit. The first 100 million is not made subject to the cap merely because the pool exceeds it. This reading is confirmed by the enacted 2020 amendment and its official explanation: interest 300 million and statutory profit 400 million produce allowed interest **220 million** and disallowed interest **80 million**. [Article 57b][law], [Act 33/2020, Article 6](https://www.althingi.is/altext/stjt/2020.033.html), [bill 626/150, section 3.5](https://www.althingi.is/altext/150/s/0626.html)

Prepare these stages:

1. **Statutory profit:** start from annual-accounts profit; add income tax, the finance-item adjustment, depreciation and fixed-asset write-downs. Subtract within-group equity-method income and add distributed dividends from that same company where paid. Reconcile every signed adjustment to the accounts; a management “EBITDA” label is insufficient.
2. **Domestic-group exception:** establish Article 55 approval or eligibility and that every company in the relevant group is Iceland-resident. One resident lender alone is insufficient.
3. **Equity exception:** establish that the taxpayer's equity ratio is no more than two percentage points below its group's ratio. Use cost rather than equity-method carrying value for a group holding where Article 57b requires it. The exception does not apply to an equity increase less than six months before balance-sheet date reversed by a corresponding decrease less than six months afterwards.
4. **Financial-sector exception:** document whether the taxpayer falls within the statutory financial undertaking, insurer or specified owned similar-business category; do not exempt every group finance company by name.
5. **If no exception:** deduct the otherwise-eligible first 100 million plus the allowed part of the excess, capped at the actual interest pool. Record the disallowed amount as a tax adjustment. Article 57b states that excess is not deductible and supplies no carryforward permission; do not create an automatic deferred interest deduction.

[Article 57b(1)–(3)][law]

For a nonnegative established statutory profit, the arithmetic control is:

```text
excess_pool = max(0, related_interest_and_discounts − 100,000,000)
allowed = min(pool, 100,000,000) + min(excess_pool, statutory_profit × 30%)
disallowed = pool − allowed
```

A loss/negative statutory-profit case needs a documented local interpretation before a final calculation; this positive-profit control does not resolve that boundary.

### 8. Controlled foreign holdings

Article 57a's low-tax comparison is **less than two thirds of the Icelandic tax that would apply to the foreign entity's profit**, not simply a country's headline rate. Establish direct/indirect ownership or control throughout the year: the provision addresses at least half held by Icelandic taxpayers or management control during the year. Trace the taxpayer's proportionate interest and recompute the foreign profit under Icelandic rules, without waiting for distribution. [Article 57a][law]

Test the exceptions from evidence: a qualifying treaty/information-exchange case whose income is not mainly passive, or qualifying EEA/EFTA/Faroe establishment carrying on genuine business with the required information access or taxpayer disclosure. Location alone does not establish genuine activity. Ring-fence losses to that entity's profits and retain adequate loss support; do not use them against unrelated Icelandic operations. Keep a previously taxed-income/distribution ledger to avoid taxing the same included profit again, subject to Article 57a's excess-distribution rule. The following implementation stages apply alongside the current statute. [Article 57a][law]

**CFC workpaper under Regulation 1102/2013.** Reconcile the foreign accounts to Icelandic income/deduction rules for the comparable legal form, then compare actual foreign income tax with two thirds of the resulting hypothetical Icelandic tax. Multiply ownership along each indirect chain, aggregating the relevant Icelandic holdings/control for the trigger. The regulation distinguishes a control/ownership trigger at any time in the year from the year-end share used to allocate profit/loss; preserve acquisitions/disposals and refer a disputed timing case rather than assuming continuous ownership. [Regulation, Articles 2–5 and 8](https://files.reglugerd.is/pdf/1102-2013/current)

The substance file addresses actual premises/equipment, local management and staff, their decision-making authority and expertise, local economic connections and demonstrable value from intragroup services. For the Article 7 outside-EEA/EFTA/Faroe exception, establish the information-access agreement and that more than half of income arises from genuine business. For the within-area exception, prove genuine activity and the required information access/disclosure. A registered-office service or treaty listing alone does not settle these tests. [Regulation, Articles 6–7](https://files.reglugerd.is/pdf/1102-2013/current); [Article 57a][law]

If taxable, allocate the Icelandic-rule profit to the supported ownership share. Keep losses by **owner, foreign entity and origin year**: only proved losses arising during that owner's holding period, verified at year end, offset that owner's later share of the same entity's profit. The regulation excludes pre-2010 losses, permits a ten-year period and does not transfer the unused owner loss to a buyer. Keep distributions and previously taxed inclusions in a separate roll-forward; only the specified excess distribution is taxable again. Any underlying or distribution-level foreign-tax relief needs its own legal basis and claim. [Regulation, Articles 8–9](https://files.reglugerd.is/pdf/1102-2013/current)

**Reporting.** Skatturinn specifies an Icelandic identifier for the CFC, applied for through RSK 17.90 if needed; the annual entity report RSK 4.24 with accounts; and each owner's RSK 4.25 with the owner's return. Multiple Icelandic owners coordinate the entity report. Current general guidance describes the entity report as a paper form and owner reporting as electronically available; confirm the accepted current-year route before submission. Do not substitute a foreign annual report for both filings. [CFC reporting guidance](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/cfc-felog/)

The regulation reproduction says the official Gazette prevails if texts differ. Read it with the current Article 57a, not as authority to override later legislation.


### 9. Approved research and development credit

**Establish entitlement before calculating a percentage.** Act 152/2009 concerns a qualifying legal-entity owner of a Rannís-confirmed project who bears its financial risk. Retain the approval, project/year, ownership and funding contracts. Universities and public institutions are outside the applicant definition. Test financial distress, including the controlling parent's position under the 2026 amendment, and outstanding unlawful-state-aid recovery. A contractor paid to deliver results for someone else's use does not acquire its own credit merely by calling that work R&D. [Articles 2–5 and 10][rd-law]; [Act 27/2026][rd-amendment]

Document enterprise size using the applicable Annex I assessment, including linked/partner enterprises and the economic unit. Do not select 35% from the Icelandic subsidiary's headcount alone. The August 2026 handbook requires an auditor-confirmed size self-assessment for the relevant group/parent/subsidiary SME applicants. Its Icelandic size shorthand and the Commission's summary differ at some exact staff/financial boundaries; resolve a borderline classification under the applicable legal definition before using the higher rate. [Article 3][rd-law]; [Rannís handbook, pages 8, 10–11][rd-handbook]; [Commission SME definition][rd-sme]

**Cost workpaper, by approved project.** Reconcile actual eligible operating expenditure to the ledger, payroll, invoices and signed project statement. Project payroll includes the supported employer levy and only time worked on the project, not a customer billing rate. Equipment/building costs use eligible depreciation attributable to project use and duration; an asset's whole purchase price is not automatically an R&D credit base. Exclude finance, sales/marketing, application-preparation costs and ordinary operations such as routine software updates, training, production and ordinary quality control. A general expense deduction is not proof of eligibility for this credit. [Act, Articles 3(5) and 10][rd-law]; [Regulation 758/2011, Articles 3 and 5][rd-reg]

For purchased R&D, establish the work's inclusion in the approved project, an unrelated supplier, and its location in the EEA or a state with an Icelandic double-tax or information-exchange agreement. The current Article 10(5) sublimit is **220 million**, derived from 20% of the 1.1-billion ceiling; it is not 20% of a small project's actual cost and is not a separate addition to the overall ceiling. Do not claim the same work as both the supplier's own project and the customer's purchase. [Article 10][rd-law]; [2026 amendment, Article 6][rd-amendment]

Apply the **1.1-billion annual ceiling once**, aggregating related applicants under Article 10's ownership/control definition. Where the combined eligible costs exceed it, allocate the capped base proportionately; separate companies or project numbers do not multiply the allowance. An unrelated cooperation project also shares one project ceiling, with the participants' supported shares. Keep the related-enterprise and project-cap calculations together where both apply; resolve overlapping limits before finalising a claim. [Articles 7 and 10][rd-law]; [Regulation, Article 7][rd-reg]

**Other public support limits the credit.** Match domestic and foreign public funding to the same project and supported eligible costs. The following are maximum **combined public-aid percentages**, including this credit, not alternative credit rates:

| Supported enterprise size | Research, ordinary / qualifying enhanced case | Development, ordinary / qualifying cooperation | Source |
|---|---|---|---|
| Small | 70% / 80% | 45% / 60% | [Article 15][rd-law] |
| Medium | 60% / 75% | 35% / 50% | [Article 15][rd-law] |
| Large | 50% / 65% | 25% / 40% | [Article 15][rd-law] |

Use an enhanced ceiling only after proving the relevant Article 15 branch. Company cooperation requires actual collaboration between independent enterprises, no participant above 70% of eligible costs, and the prescribed SME or two-EEA-country condition. The research-institution branch requires at least 10% institutional cost participation and publication rights. Research-only public dissemination is a separate enhancement branch. Subcontracting alone is not cooperation; the large-enterprise enhancement has its own cross-border/SME condition. Keep the collaboration agreement, cost shares and the branch relied on. [Article 15][rd-law]; [Regulation, Article 6][rd-reg]

For a single supported project below the cost ceiling, compare the nominal credit with the residual permitted aid after other project grants. Do not simply deduct grants from the cost base and multiply the remainder by 35%/25%. A zero additional credit does not cure other grants already above the aid ceiling. Rannís's worked illustration uses 10 million eligible research cost, a small enterprise, a 70% total-aid limit and 6 million other grants: the nominal 3.5-million credit becomes **1 million**. [Handbook, page 15][rd-handbook]; [Articles 10 and 15][rd-law]

The credit reduces **assessed tax**, after the ordinary taxable-profit computation; do not deduct the credit again as an expense. Eligible underlying costs follow the ordinary tax rules once. Article 11 provides for the excess credit to be paid when it exceeds assessed income tax or there is a tax loss, subject to public-debt setoff. Regulation Article 8 orders the offsets before any cash balance, so a calculated refund is not a promised payment date or bank receipt. [Articles 10–11][rd-law]; [Regulation, Articles 7–8][rd-reg]

### 10. Financial-sector taxes: scope and three separate bases

**First determine each charge independently.** Act 165/2011 Articles 2–3 cover the specified insurers, financial/e-money/fund-management undertakings, other operators supplying the stated VAT-exempt financial services, and relevant foreign branches/representatives, with the statutory public-body exception. A non-bank financial-services operator cannot dismiss the remuneration tax merely because it lacks a banking licence. The bank-liability tax has the narrower and separate permissions/winding-up tests in Act 155/2010 Article 2. Keep licences, actual service classification, branch status, public ownership/statutory role and any exemption decision in the scope file. [Act 165/2011, Articles 2–3][fat-law]; [Act 155/2010, Article 2][bank-law]

**A. Remuneration tax, fjársýsluskattur.** Reconcile cash pay, fees, director/committee remuneration, calculated remuneration, taxable benefits and the other Article 4 items. Employer pension contributions are expressly in the base; do not reduce it by the employee's personal pension deduction or assume only cash salary is taxed. Test Article 5 separately for pension payments, amounts attributable to the taxpayer's VAT-taxable activity outside the specified exempt financial services, and the maternity-leave payment portion reimbursed by the fund. Preserve evidence for the actual excluded cost; a VAT turnover ratio is not automatically a wage allocation. Apply **5.5%** to the supported remaining base. [Act 165/2011, Articles 4–6][fat-law]

Keep taxable/exempt operations separate in the ledger and financial-activities return and retain the records for **seven years** from the accounting-year end. Under Article 15, this remuneration tax is an ordinary deductible operating cost **only to the extent** calculated on wages that themselves qualify under Income Tax Act Article 31. Where book profit already includes that deductible charge, do not deduct it again in the tax bridge. These are employer charges, separate from employee PAYE and the social-contribution method. [Act 165/2011, Articles 14–15][fat-law]; [Payroll](iceland-payroll.md); [Social contributions](iceland-social-contributions.md)

**B. Additional income tax, sérstakur fjársýsluskattur.** Prepare a second Article 61(2) income-tax-base reconciliation for the Article 71(3) charge. Disregard group taxation and brought-forward losses when determining this base; an ordinary CIT loss offset does not itself reduce it. Apply **6% only to the excess over 1 billion**. Show this charge alongside ordinary CIT, not as a universal 26% rate on all income. Do not treat income-tax payments as deductible operating expenses or deduct this tax from its own base. Resolve unusual instrument, exemption or taxpayer-status questions from their specific provisions before finalising. [Income Tax Act, Articles 31, 61(2) and 71(3)][law]

**C. Liability tax, sérstakur skattur á fjármálafyrirtæki.** For an in-scope institution, reconcile year-end liabilities to the tax-return amount under Income Tax Act Article 75. The base is the amount **above 50 billion**, and the rate is **0.145%**. Act 155/2010 Article 3 prohibits netting assets and liabilities within items or categories; net assets are not this tax base. Winding-up cases instead use the specified admitted-claims measure. Test Article 2's exemptions and transitional II's qualifying currency-reserve adjustment separately; do not deduct a general accounting reserve as that exception. [Act 155/2010, Articles 2–4 and transitional II][bank-law]

This liability tax is **not deductible** as operating expenditure under Act 155/2010 Article 6. If book profit before income tax includes it as an expense, add it back in the ordinary CIT bridge and the corresponding additional-profit-tax reconciliation. This differs from the conditional wage-cost deduction for the 5.5% remuneration tax. Preserve three distinct schedules and payment-credit balances rather than combining the percentages. [Act 155/2010, Article 6][bank-law]; [Act 165/2011, Article 15][fat-law]; [Income Tax Act, Article 71(3)][law]

### 11. Restructuring: transaction, tax succession and loss tests

**Classify the legal transaction before carrying balances forward.** Record each entity's legal form, separate-taxpayer status and residence; the dissolution/succession documents; consideration; shareholder proportions; effective date; and approvals. Articles 51–53a have different conditions for company mergers, splits, partnerships, cooperatives and funds. A sale of assets, a sale of shares and a qualifying statutory merger are different transactions. Do not treat common ownership or a company-registry entry alone as tax-neutral treatment. [Articles 51–54][law]

For the ordinary domestic company-merger route in Article 51(1), document the disappearing company's full merger into the recipient and the shareholders' shares-only consideration. The qualifying exchange itself does not create taxable income for the exchanging shareholder; the recipient succeeds to tax rights and obligations. Keep an asset-by-asset tax-cost/depreciation roll-forward and liability history rather than creating a tax step-up from the merger valuation. Wholly owned mergers without new shares, cash consideration, nonstandard legal forms and disputed continuity require a separate documented determination; this ordinary route does not decide them. [Articles 33–51][law]

For an Article 52 company split, reconcile all assets/liabilities across the remaining and recipient companies, shares-only consideration, and each shareholder's unchanged relative ownership proportions. Assets and liabilities transfer at book value. Allocate supported tax rights and duties in the ratio of **transferred book assets less liabilities**, not an arbitrary ratio of issued shares. Losses first require Article 54 qualification; an allocation percentage does not make an ineligible loss transferable. Zero/negative net-asset or valuation disputes need resolution before using the simple positive-net-assets example below. [Article 52(1)–(2), Article 54][law]

A qualifying Article 53 partnership merger/conversion also requires the specified equity/shares-only consideration and tax succession. Establish the partnership's separate-taxpayer status and the precise statutory route. The former partners retain unlimited liability for public levies relating to accounting years before the dissolution/conversion. Cooperative transactions under Article 51 and equal-value fund mergers under Article 53a require their own legal-form conditions; do not extend the ordinary company method automatically. [Articles 2, 51, 53–53a][law]

**Loss succession is a separate cumulative decision.** For an Article 51–53a merger/split loss, retain evidence for every Article 54 condition:

- The recipient carries on activity related to the transferor's activity.
- The transferor had actual operations and more than insignificant assets before dissolution.
- The transaction has a normal and ordinary business purpose.
- The loss arose in the same kind of business that the recipient carries on.

Retain contracts, actual operations/assets, business-purpose approvals, the loss-generating activity and the Article 31(8) vintage/use schedule. A loss-company purchase or a qualifying share exchange does not prove all four conditions. Reject an unsupported transfer from the computation pending determination; do not silently use it because the merger itself qualifies. Incoming cross-border cases also require Article 54(3)'s genuine foreign activity and adequate proof concerning unusability/prior use of the loss. [Articles 31(8), 54][law]

**Domestic sole-trade incorporation under Article 56.** The individual must have unlimited Icelandic tax liability and form a new Iceland-registered ehf. with unlimited Icelandic tax liability. It must take **all** business assets and liabilities and continue the same kind of activity; the owner receives **only shares**. Obtain the audited, unqualified **31 December** business balance sheet, no older than **four months at formation**, and the auditor's confirmation that owner withdrawals have not depleted the business between that date and formation. This is a conditional statutory route, not a blanket exemption for every owner-to-company transfer. [Article 56(1)][law]; [Regulation 223/2003, Articles 1–5][incorp-reg]

On qualification the company succeeds to the business's tax rights and obligations from the balance-sheet date, including unused losses only where Article 31(8) permits them; the owner retains unlimited liability for pretransfer public levies. Reconcile transferred assets/debts at book values and the minimum capital supported by transferred net equity. If a properly supported revaluation is accepted for company-registry/accounts purposes, keep a separate tax schedule: original asset tax cost and remaining depreciation basis **do not increase**. The owner's shares have the statutory book-equity basis, taking extra depreciation into account; for a later share-gain computation the regulation specifies **tax book equity**. Do not substitute revalued accounting equity for that tax basis. [Article 56(2)][law]; [Regulation, Articles 2 and 6–8][incorp-reg]; [Current incorporation guidance][incorp-guidance]

**Cross-border is a separate branch.** Articles 52 and 56 invoke Article 51(3)–(9)'s valuation, reporting, assessment, payment-deferral and security rules for their qualifying cross-border transactions. Use the [cross-border valuation/payment workpaper](is-cross-border.md) with the actual transaction's provisions; domestic carryover does not establish an exit-tax exemption. Article 52 imposes the stated joint tax liability on the split participants, or recipients where the original company dissolves; Article 56 makes the individual and recipient jointly liable for incorporation taxes. Territory, substance, information-assistance and retained-PE evidence remain necessary. [Articles 51–52, 54 and 56–56a][law]

## Deadlines and filing

### Return and assessment workflow

Use **RSK 1.04** for the legal-entity business return through the taxpayer service or software meeting Skatturinn's electronic specification. The legal-entity version is distinct from an individual's business schedule. Reconcile accounts, asset register, deductions, loss/group schedules and applicable information returns; retain submission and acceptance evidence. [RSK 1.04 guidance][return]

For **2025 income filed in 2026**, the 30 January 2026 notice states a general deadline of **31 May 2026** and a professional extension available up to **21 September 2026**. An extension is not automatic. The former generic 30 September statement did not match that notice. Article 93 establishes annual deadline-setting: verify the notice for **2026 income filed in 2027** when available. [2026 filing notice][filing-notice]; [Article 93][law]

Calendar year is the ordinary income period; another accounting year needs the Article 59 permission. For approved foreign-currency accounts, Article 91 requires the supporting accounts and statutory ISK conversion statement; it distinguishes income/expense average rates from balance-sheet closing rates. Check its detailed tax-basis rules before using a single year-end rate for the whole return. [Articles 59, 90–91][law]

Compare assessment with the return, tax calculation and payment ledger. Article 99 gives legal entities a **one-month** initial assessment-complaint period measured from the specified assessment announcement; do not substitute the different individual period or assume every later reassessment follows the same trigger. [Article 99][law]

### R&D approval and claim records

New-project applications reach Rannís by **1 October** for the application year; ordinary extensions are due by **1 April**, with no more than three extensions of the same project. Keep submission receipts, cost/work plans, business plan, staff expertise, funding and collaboration evidence. The dated 2026 notice specified **1 October 2026 at 23:59 Icelandic time** through Rannís's electronic system; that deadline had passed at this Guide's research date. Do not assume an unsubmitted 2026 application can be created retrospectively. [Articles 4–5 and 9][rd-law]; [20 August 2026 notice][rd-notice]

The 2026 amendment permits the stated small-company two-year approval with both years' plans and a first-year progress report. Obtain the actual approval rather than treating every small project as automatically covered for two years. Current statutory processing time is **three months**; the older regulation reproduction still says two months, so do not promise that older interval. Approval does not settle the tax authority's cost/aid calculation. [Articles 8–9][rd-law]; [Amendment, Articles 4–5][rd-amendment]; [Handbook, pages 3 and 6–8][rd-handbook]

Prepare a separate signed cost statement and **RSK 4.21 for each project**, with **RSK 4.22** for cooperation and reconciled participant shares. The statutory signatory is an auditor, examiner or recognised bookkeeper. The handbook links a 2026 RSK 4.21 and a 2025-labelled RSK 4.22: these establish the published layout, not the accepted 2027 form for 2026 income. In particular, the older 4.21 explanation's land-financing wording must not override the current Act's financing-cost exclusion. Confirm current-year forms and upload acceptance before filing; retain the submission and assessment evidence. [Article 10][rd-law]; [Handbook, pages 7–8 and 11][rd-handbook]; [Published RSK 4.21][rd-form]; [Published RSK 4.22][rd-coop-form]

### Financial-sector reporting and payment

For remuneration tax, Act 165/2011 Article 7 requires notification **at least eight days before activity starts**. Article 8 makes each calendar month a payment period, due on the **first of the next month**, with final payment **fourteen days later**. Submit the authority's required statement and reconcile the monthly tax with the annual financial-activities return due within the applicable income-tax-return deadline. Allocate calculated remuneration across periods under Article 10 unless the records demonstrate the different actual split. Keep an annual reconciliation to wages, returns, payments and assessment. [Act 165/2011, Articles 7–11][fat-law]

The Act gives separate annual due dates for specified benefit/non-withheld amounts: **1 June for individuals and 1 November for legal entities**, with final payment one month later. This is not permission to defer ordinary monthly remuneration tax. Correct an omission by the original payment periods under Article 11 rather than assigning all arrears to the annual date. Confirm applicable calendar shifts and the issued notice. [Act 165/2011, Articles 10–11][fat-law]

For the **2026 assessment on 2025 income/year-end liabilities**, Regulation 1370/2025 Article 2 expressly includes additional financial activities tax and bank-liability tax alongside ordinary CIT in the advance public levies. The authority describes eight 8.5% advances and settlement against the assessment. Keep those payment-year credits separate from the 2026-income computation; do not reuse the 2012 launch notice's transitional advance timetable or infer the unissued 2027 timetable. The existing final-date conflict and reduction conditions below remain relevant. [Regulation, Articles 1–4][payment-reg]; [Advance guidance][advances]; [2026 assessment][assessment]

### Restructuring dates and return evidence

For an Article 54 merger/split, retain the effective date under the approved documents and the corresponding operation/return cut-off. The current rule requires the start date to fall **within the income year** and approval in **all participating companies in that year**; do not apply an old unrestricted backdating assumption. Reconcile the transferor/recipient returns and loss/asset schedules to those dates. [Article 54(2), as amended in 2023][law]

For the domestic Article 56 route, Skatturinn specifies **formation by 30 April** and delivery of formation documents to the company registry **by 30 June of the same year**. June is the document-lodging deadline, not an extension of the four-month balance-sheet condition. The 2026 dates have already passed at this research date. Include the audited opening balance and transfer declaration with the first company return, and retain the formation/registration evidence, tax-cost roll-forward, owner-drawings confirmation and continuing pretransfer-liability record. Confirm the applicable year's accepted forms before submission. [Article 56][law]; [Regulation, Articles 3–5][incorp-reg]; [Current registry guidance][incorp-guidance]

### Payment-year reconciliation

Regulation 1370/2025 governs **2026 payments towards the 2026 assessment on 2025 income**. Each pre-assessment payment is 8.5% of 2025 assessed public levies; current guidance describes eight equal February–September payments totalling 68%. Reconcile actual notices, reductions and payments rather than treating advances as a tax expense or calling them payments against 2026 trading profit. The regulation also has an ISK 5,000 collection minimum per due date. [Regulation, Articles 1–2][payment-reg]; [Advance guidance][advances]

Article 112 allocates the assessed balance, after the stated advances/credits, across remaining due dates. Do not promise two identical November/December instalments without checking the actual assessment and prior payments. **Final-date discrepancy:** Article 112(1)'s ordinary wording is the month's last business day, whereas Regulation 1370/2025 Article 1 and the guidance say one month after due date. Preserve the issued payment notice and obtain a documented resolution where dates differ; this draft does not silently treat them as identical. [Articles 112, 114][law]; [Regulation, Articles 1–4][payment-reg]

For a requested advance reduction, Regulation 1370/2025 Article 6 says the relevant 2025 bases are **more than 25%** below 2024; the authority's general guidance instead says **at least 25%**, adds an ISK 100,000 tax reduction and describes a 31 May application deadline. Exactly 25% and the applicable year's notice require resolution before assuming eligibility. A request does not itself reduce the amount due. [Regulation, Articles 5–7][payment-reg]; [Advance guidance][advances]

## Penalties and interest

Article 108 increases **tax bases**, rather than imposing the listed percentages directly on tax due:

| Circumstance | Statutory maximum/treatment | Source |
|---|---|---|
| No timely return; estimated bases | Up to 15%, considering withholding already collected | [Article 108(1)][law] |
| Late return received before assessment finishes | 0.5% of bases per late day, capped at 10% | [Article 108(1)][law] |
| Defective/understated bases | Up to 25%; maximum 15% if corrected before assessment | [Article 108(2)][law] |
| Proven absence of taxpayer fault/uncontrollable circumstances | Statutory waiver conditions in Article 108(3) | [Article 108(3)][law] |

Article 114 links assessment late interest to the Central Bank rate. Regulation 1370/2025 Article 4 says unpaid 2026 advances/assessments after a month attract interest from the due date and addresses acceleration after partial nonpayment. Use the actual collection basis, due dates and period-specific rate; no undated floating rate is quoted here. Documentation fines, payroll/VAT collection penalties and criminal sanctions are separate regimes. [Article 114][law]; [Regulation, Article 4][payment-reg]

For R&D overstatement, Article 12 permits a **25% surcharge on the reduction of the credit**, not 25% of all project costs. Its no-fault and criminal-case exceptions must be considered; this is not an automatic charge in every correction. Article 5 permits approval revocation for materially false/misleading application information, reaching the current and preceding two income years. False/fabricated claims also require the separate Article 15a criminal-law analysis. [Articles 5, 12 and 15a][rd-law]

For remuneration tax unpaid by the monthly final date, Act 165/2011 Articles 8 and 11 provide default interest from the original due date. Article 9 imports the Withholding Act only as applicable and **expressly excludes Article 28(2)(1)'s daily surcharge**. Do not add the ordinary PAYE 1%-per-day/10%-cap charge to this tax. Assessment/information/sanction rules also require Articles 10–13; criminal penalties are not an automatic payroll calculation. The bank-liability tax uses Act 155/2010 Article 5's separate reference to the Income Tax Act's assessment, collection and sanction chapters. [Act 165/2011, Articles 8–13][fat-law]; [Act 155/2010, Article 5][bank-law]

## Cross-border points

Resident worldwide income still needs treaty and foreign-tax-relief analysis. Article 119 permits an application-based reduction where no double-tax treaty exists and the statutory conditions apply; it is not automatic dollar-for-dollar credit. Use the [resident foreign-income relief workpaper](is-cross-border.md) for country/category matching, tax attribution and the conditional current-UK credit example. Other treaty-specific limitations and exemption methods still need the actual treaty analysis. Company/asset migration now has a statutory computation and payment workpaper in the [cross-border Guide](is-cross-border.md); do not treat a qualifying move as automatically tax-free. [Articles 2, 119][law]

For non-resident payments, preserve the [cross-border Guide](is-cross-border.md)'s distinctions: Article 70 national rates include 20% for the relevant company service/dividend categories, **22% for Article 3(6) royalties**, and **12% for taxable corporate interest**, before exclusions/treaty relief. Do not apply ordinary resident CIT to every gross cross-border receipt. [Articles 3, 70][law]

Screen foreign holdings under Article 57a, related-party transactions under Article 57, CbC reporting under Article 91a, and migration/restructuring under Articles 51–56a. These screens require their own evidence and computations. The R&D method above includes the foreign-supplier and foreign-public-aid screens; territory alone does not establish purchase eligibility. The stated financial-sector scope includes relevant foreign branches, but an actual branch still needs liability/attribution evidence. Other sector taxes/incentives, financial instruments and any applicable group minimum-tax regime still need their own applicability audit; this ordinary computation does not establish their absence.

## Worked examples that recompute

### 1. Profit-to-tax reconciliation

Assume a resident ehf. with ISK 12 million accounting profit before tax, including book depreciation ISK 2 million, a supported nondeductible item ISK 1 million and qualifying dividend income ISK 2 million. Tax depreciation is ISK 3 million and substantiated eligible brought-forward losses are ISK 4 million. The bridge is 12 + 2 + 1 − 3 − 2 = **ISK 10 million** before losses; taxable income is **ISK 6 million** and ordinary tax **ISK 1.2 million**. Assume all participation/loss conditions are met and no other adjustment or sector tax applies. Eligibility is a fact assumption requiring evidence.

```oa-check
name: Iceland company profit to ordinary tax bridge
inputs:
  accounting_profit: 12000000
  book_depreciation: 2000000
  disallowed_item: 1000000
  tax_depreciation: 3000000
  qualifying_dividend_deduction: 2000000
  eligible_losses: 4000000
  ordinary_rate: 0.20
steps:
  before_losses: accounting_profit + book_depreciation + disallowed_item - tax_depreciation - qualifying_dividend_deduction
  loss_used: min(eligible_losses, max(0, before_losses))
  taxable_income: max(0, before_losses - loss_used)
  ordinary_tax: taxable_income * ordinary_rate
expected:
  before_losses: 10000000
  loss_used: 4000000
  taxable_income: 6000000
  ordinary_tax: 1200000
```

### 2. Reverse last year's closing reductions

Assume eligible closing receivables ISK 20 million and inventory ISK 30 million, already valued under the relevant rules. Elect 5% reductions: ISK 1 million and ISK 1.5 million. Prior-year expensed reductions of ISK 750,000 and ISK 1.2 million must be reversed. The net current deduction is **ISK 550,000**, not ISK 2.5 million. Assume no overlapping book or other tax write-down. [Article 31(3)–(4)][law]

```oa-check
name: Iceland closing reductions with prior year reversals
inputs:
  eligible_receivables: 20000000
  eligible_inventory: 30000000
  elected_rate: 0.05
  prior_receivable_reduction: 750000
  prior_inventory_reduction: 1200000
steps:
  current_receivable_reduction: eligible_receivables * elected_rate
  current_inventory_reduction: eligible_inventory * elected_rate
  net_deduction: current_receivable_reduction + current_inventory_reduction - prior_receivable_reduction - prior_inventory_reduction
expected:
  current_receivable_reduction: 1000000
  current_inventory_reduction: 1500000
  net_deduction: 550000
```

### 3. Exact acquisition threshold and the depreciation floor

Assume qualifying office equipment first used this year costs **exactly ISK 600,000**. Article 39's below-threshold expensing does not apply. At an elected permitted 20% rate, first-year depreciation is **ISK 120,000**, leaving **ISK 480,000**. Separately, assume continuing-use equipment with the same original cost but opening tax value ISK 65,000: a 20% charge would be ISK 13,000, but Article 42's ISK 60,000 floor limits the charge to **ISK 5,000**. These are not disposal-year examples. [Articles 34, 36–39, 42][law]

```oa-check
name: Iceland office equipment depreciation and residual floor
inputs:
  original_cost: 600000
  elected_rate: 0.20
  later_opening_tax_value: 65000
  residual_rate: 0.10
steps:
  first_depreciation: original_cost * elected_rate
  first_closing_value: original_cost - first_depreciation
  residual_floor: original_cost * residual_rate
  later_uncapped_depreciation: later_opening_tax_value * elected_rate
  later_depreciation: min(later_uncapped_depreciation, max(0, later_opening_tax_value - residual_floor))
  later_closing_value: later_opening_tax_value - later_depreciation
expected:
  first_depreciation: 120000
  first_closing_value: 480000
  residual_floor: 60000
  later_uncapped_depreciation: 13000
  later_depreciation: 5000
  later_closing_value: 60000
```

### 4. Assessment-year cash reconciliation

Assume 2025 assessed public levies of ISK 5 million, eight unreduced 2026 advances paid in full, and a 2026 assessment on 2025 income of ISK 3.6 million, with no other credits or charges. Each advance is **ISK 425,000**, total **ISK 3.4 million**, leaving **ISK 200,000**. This is a payment reconciliation for the 2026 assessment cycle; it does not calculate tax on 2026 trading income or establish actual instalment dates. [Regulation, Articles 1–2][payment-reg]

```oa-check
name: Iceland 2026 assessment advances and balance
inputs:
  assessment_2025: 5000000
  instalment_rate: 0.085
  paid_instalments: 8
  assessment_2026: 3600000
steps:
  each_advance: assessment_2025 * instalment_rate
  paid_advances: each_advance * paid_instalments
  assessment_balance: assessment_2026 - paid_advances
expected:
  each_advance: 425000
  paid_advances: 3400000
  assessment_balance: 200000
```

### 5. Related-party financing, official positive-profit illustration

Assume all 300 million of related-party interest/discounts is otherwise eligible, statutory profit is 400 million, and no exception applies. The official amendment explanation's result is 220 million deductible, 80 million disallowed. [Bill 626/150, section 3.5](https://www.althingi.is/altext/150/s/0626.html); current [Article 57b][law]. This is a deduction adjustment, not a claim that 80 million itself is tax due.

```oa-check
name: Iceland related-party interest, first 100 million plus capped excess
inputs:
  related_interest: 300000000
  statutory_profit: 400000000
  protected_slice: 100000000
steps:
  - excess_pool: max(0, related_interest - protected_slice)
  - profit_capacity: statutory_profit * 0.30
  - allowed_interest: min(related_interest, protected_slice) + min(excess_pool, profit_capacity)
  - disallowed_interest: related_interest - allowed_interest
expected:
  excess_pool: 200000000
  profit_capacity: 120000000
  allowed_interest: 220000000
  disallowed_interest: 80000000
```

### 6. Financing threshold and equity-ratio boundaries

With otherwise eligible interest exactly 100 million, no amount enters the capped excess pool. Separately, taxpayer equity ratio 28% and group ratio 30% meet the two-percentage-point numeric boundary; 27.9% does not. The latter is only an arithmetic screen: timing, valuation and the other conditions still require evidence. [Article 57b][law]

```oa-check
name: Iceland interest exact threshold and equity-ratio distance
inputs:
  related_interest: 100000000
  taxpayer_ratio: 28
  lower_ratio: 27.9
  group_ratio: 30
steps:
  - excess_pool: max(0, related_interest - 100000000)
  - boundary_distance_points: group_ratio - taxpayer_ratio
  - failing_distance_points: group_ratio - lower_ratio
expected:
  excess_pool: 0
  boundary_distance_points: 2
  failing_distance_points: 2.1
```

### 7. CFC indirect ownership, tax comparison and owner loss

Assume the taxpayer owns 60% of an intermediate company which owns 90% of the foreign entity throughout the year, with a combined 54% indirect interest and no applicable exemption. The foreign entity's profit has already been reconciled to an Icelandic comparable-company base of 20 million; at 20%, hypothetical Icelandic tax is 4 million, so the two-thirds comparison is 2,666,666.67. Actual foreign income tax of 1 million is below that threshold. The owner's profit share is **10.8 million**. A proved eligible same-owner/same-entity carried loss of 2.8 million leaves an **8 million** inclusion; gross Icelandic tax at 20% is **1.6 million before any separately established relief**. No unrelated domestic income is reduced by the ring-fenced CFC loss. [Article 57a][law], [Regulation 1102/2013, Articles 2, 4 and 8](https://files.reglugerd.is/pdf/1102-2013/current)

```oa-check
name: Iceland CFC indirect share and owner-specific same-entity loss
inputs:
  intermediate_share: 0.60
  intermediate_cfc_share: 0.90
  foreign_profit_reconciled_to_iceland_rules: 20000000
  comparable_iceland_rate: 0.20
  actual_foreign_income_tax: 1000000
  proved_owner_same_entity_loss: 2800000
steps:
  - indirect_share: intermediate_share * intermediate_cfc_share
  - hypothetical_iceland_tax: foreign_profit_reconciled_to_iceland_rules * comparable_iceland_rate
  - low_tax_comparison: hypothetical_iceland_tax * 2 / 3
  - owner_profit_share: foreign_profit_reconciled_to_iceland_rules * indirect_share
  - loss_used: min(owner_profit_share, proved_owner_same_entity_loss)
  - inclusion: owner_profit_share - loss_used
  - gross_iceland_tax_before_separate_relief: inclusion * comparable_iceland_rate
expected:
  indirect_share: 0.54
  hypothetical_iceland_tax: 4000000
  low_tax_comparison: 2666666.67
  owner_profit_share: 10800000
  inclusion: 8000000
  gross_iceland_tax_before_separate_relief: 1600000
```

### 8. R&D purchased-cost sublimit and annual ceiling

Assume approved research owned by a supported SME, eligible internal project costs 900 million and otherwise eligible purchased R&D 300 million from qualifying unrelated suppliers. There are no other projects/related applicants, no other public aid, and no further eligibility restriction. Purchased cost is limited to **220 million**; the combined 1.12-billion amount then meets the separate **1.1-billion overall ceiling**. Nominal credit is **385 million**. These assumptions establish neither project approval nor SME classification for a real company. [Article 10][rd-law]

```oa-check
name: Iceland R&D purchased subcap before overall annual ceiling
inputs:
  internal_eligible: 900000000
  qualifying_purchased: 300000000
  annual_cap: 1100000000
  purchased_fraction: 0.20
  credit_rate: 0.35
steps:
  - purchased_cap: annual_cap * purchased_fraction
  - allowed_purchased: min(qualifying_purchased, purchased_cap)
  - eligible_before_overall_cap: internal_eligible + allowed_purchased
  - credit_base: min(eligible_before_overall_cap, annual_cap)
  - nominal_credit: credit_base * credit_rate
expected:
  purchased_cap: 220000000
  allowed_purchased: 220000000
  eligible_before_overall_cap: 1120000000
  credit_base: 1100000000
  nominal_credit: 385000000
```

### 9. R&D public-aid ceiling and tax/refund split

Use the handbook's stated small-enterprise ordinary research assumptions: 10 million eligible cost, 6 million other public grants, 35% nominal credit and a 70% total-aid ceiling. Credit is limited to **1 million**. With assumed assessed income tax of 600,000, it offsets that tax and leaves **400,000 before other public-debt offsets**. This is not a second deduction from the underlying business profit or a promised cash payment. [Handbook, page 15][rd-handbook]; [Articles 10–11 and 15][rd-law]

```oa-check
name: Iceland R&D grant cap and excess credit before debt setoff
inputs:
  eligible_cost: 10000000
  other_public_grants: 6000000
  nominal_rate: 0.35
  aid_ceiling_rate: 0.70
  assessed_income_tax: 600000
steps:
  - nominal_credit: eligible_cost * nominal_rate
  - total_aid_limit: eligible_cost * aid_ceiling_rate
  - remaining_aid_capacity: max(0, total_aid_limit - other_public_grants)
  - allowed_credit: min(nominal_credit, remaining_aid_capacity)
  - income_tax_offset: min(allowed_credit, assessed_income_tax)
  - excess_before_other_debts: allowed_credit - income_tax_offset
expected:
  nominal_credit: 3500000
  total_aid_limit: 7000000
  allowed_credit: 1000000
  income_tax_offset: 600000
  excess_before_other_debts: 400000
```

### 10. R&D related-applicant ceiling shared once

Assume two related applicants, both within the supported SME classification, each has 700 million otherwise eligible approved internal research cost, no purchased work, no other grants or projects and no further aid restriction. Aggregate cost **1.4 billion** exceeds one **1.1-billion** ceiling. Each receives a proportionate **550-million** credit base and **192.5-million** nominal credit; total credit is **385 million**, not 490 million. [Article 10][rd-law]; [Handbook, page 14][rd-handbook]

```oa-check
name: Iceland R&D related applicants proportionate annual cap
inputs:
  first_cost: 700000000
  second_cost: 700000000
  shared_cap: 1100000000
  supported_sme_rate: 0.35
steps:
  - aggregate_cost: first_cost + second_cost
  - capped_total: min(aggregate_cost, shared_cap)
  - first_base: capped_total * first_cost / aggregate_cost
  - second_base: capped_total * second_cost / aggregate_cost
  - first_credit: first_base * supported_sme_rate
  - second_credit: second_base * supported_sme_rate
  - combined_credit: first_credit + second_credit
expected:
  aggregate_cost: 1400000000
  first_base: 550000000
  second_base: 550000000
  first_credit: 192500000
  second_credit: 192500000
  combined_credit: 385000000
```

### 11. R&D surcharge uses the credit reduction

Assume an originally allowed 5-million credit is corrected to 3.5 million, the authority applies the permitted 25% surcharge, and neither statutory exception applies. The credit reduction is **1.5 million** and surcharge **375,000**. Project-cost totals are not the surcharge base. [Article 12][rd-law]

```oa-check
name: Iceland R&D overstatement surcharge on reduced credit
inputs:
  original_credit: 5000000
  corrected_credit: 3500000
  applied_surcharge_rate: 0.25
steps:
  - credit_reduction: original_credit - corrected_credit
  - surcharge: credit_reduction * applied_surcharge_rate
expected:
  credit_reduction: 1500000
  surcharge: 375000
```

### 12. Financial remuneration tax includes employer pension

Assume an in-scope employer has 100 million gross cash remuneration, 11.5 million employer pension contributions and 2 million taxable benefits. Evidence supports excluding 20 million of that combined remuneration base because it relates to the employer's VAT-taxable non-financial operations; there are no other exclusions. The remaining **93.5 million** base gives **5,142,500** financial activities tax at 5.5%. The assumed pension amount is a supported case input; it does not establish every employee's pension contract. [Act 165/2011, Articles 4–6][fat-law]

```oa-check
name: Iceland financial remuneration tax includes pension and proved exclusion
inputs:
  gross_cash_pay: 100000000
  employer_pension: 11500000
  taxable_benefits: 2000000
  proved_vat_taxable_activity_exclusion: 20000000
  financial_remuneration_rate: 0.055
steps:
  - remuneration_before_exclusions: gross_cash_pay + employer_pension + taxable_benefits
  - financial_tax_base: remuneration_before_exclusions - proved_vat_taxable_activity_exclusion
  - financial_remuneration_tax: financial_tax_base * financial_remuneration_rate
expected:
  remuneration_before_exclusions: 113500000
  financial_tax_base: 93500000
  financial_remuneration_tax: 5142500
```

### 13. Bank-liability tax: gross debts and exact threshold

Assume an in-scope institution has established tax-return year-end liabilities of 60 billion, assets of 55 billion, no reserve adjustment and no exemption. Assets are **not** netted against debt: taxable excess is **10 billion** and the charge is **14.5 million**. At exactly 50 billion of qualifying liabilities, the excess and charge are zero. This does not establish a winding-up claim balance or allow a consolidation/netting shortcut. [Act 155/2010, Articles 2–4][bank-law]

```oa-check
name: Iceland bank liabilities charge without asset netting
inputs:
  tax_return_liabilities: 60000000000
  threshold: 50000000000
  rate: 0.00145
steps:
  - excess_debts: max(0, tax_return_liabilities - threshold)
  - bank_liability_tax: excess_debts * rate
  - exact_threshold_tax: max(0, threshold - threshold) * rate
expected:
  excess_debts: 10000000000
  bank_liability_tax: 14500000
  exact_threshold_tax: 0
```

### 14. Separate ordinary and additional income-tax bases

Assume an in-scope resident limited company has 1.2 billion book profit before income taxes. That profit already expenses 14.5 million bank-liability tax and a proved deductible financial-remuneration tax; the only book-to-tax adjustment is the **14.5-million add-back**. Assume 300 million qualifying prior-year trading losses, no group adjustment, no credits and no other restriction. Current income-tax base before those losses is **1,214.5 million**. Ordinary CIT at 20% on 914.5 million is **182.9 million**. The separate 6% charge ignores brought-forward losses and applies to 214.5 million above its billion threshold, giving **12.87 million**; total income taxes are **195.77 million**. The liability tax itself remains a distinct charge. [Act 155/2010, Article 6][bank-law]; [Act 165/2011, Article 15][fat-law]; [Income Tax Act, Articles 31, 61 and 71][law]

```oa-check
name: Iceland financial profit tax ignores prior loss and adds back bank tax
inputs:
  book_profit_before_income_taxes: 1200000000
  expensed_bank_liability_tax: 14500000
  eligible_prior_losses: 300000000
  ordinary_cit_rate: 0.20
  additional_threshold: 1000000000
  additional_rate: 0.06
steps:
  - current_tax_base_before_prior_loss: book_profit_before_income_taxes + expensed_bank_liability_tax
  - ordinary_cit_base: max(0, current_tax_base_before_prior_loss - eligible_prior_losses)
  - ordinary_cit: ordinary_cit_base * ordinary_cit_rate
  - additional_profit_base: max(0, current_tax_base_before_prior_loss - additional_threshold)
  - additional_profit_tax: additional_profit_base * additional_rate
  - combined_income_taxes: ordinary_cit + additional_profit_tax
expected:
  current_tax_base_before_prior_loss: 1214500000
  ordinary_cit_base: 914500000
  ordinary_cit: 182900000
  additional_profit_base: 214500000
  additional_profit_tax: 12870000
  combined_income_taxes: 195770000
```

### 15. A qualifying merger does not itself prove the loss transfer

Assume a resident ehf. has 20 million current taxable profit before a proposed transferred loss. The other company's unused, unexpired loss is 30 million. If a documented determination confirms **all Article 54 conditions** and no other restriction, 20 million is used and 10 million remains in its original vintage. If that loss-transfer test fails, none of that loss is available: ordinary tax on the assumed 20-million base is **4 million at 20%**. Both outcomes assume the merger route has separately been established; the arithmetic cannot decide legal eligibility. [Articles 31(8), 51, 54 and 71][law]

```oa-check
name: Iceland merger loss computation depends on separate qualification
inputs:
  recipient_profit_before_loss: 20000000
  unused_unexpired_loss: 30000000
  ordinary_rate: 0.20
steps:
  - qualified_loss_used: min(recipient_profit_before_loss, unused_unexpired_loss)
  - qualified_remaining_vintage: unused_unexpired_loss - qualified_loss_used
  - qualified_tax: max(0, recipient_profit_before_loss - qualified_loss_used) * ordinary_rate
  - failed_loss_test_tax: recipient_profit_before_loss * ordinary_rate
expected:
  qualified_loss_used: 20000000
  qualified_remaining_vintage: 10000000
  qualified_tax: 0
  failed_loss_test_tax: 4000000
```

### 16. Split allocation uses transferred book net assets

Assume every Article 52 condition is proved, including each shareholder retaining the same relative ownership, and all relevant Article 54 conditions are separately met. Recipient A receives book assets of 90 million and liabilities of 30 million; recipient B receives 65 million and 25 million. Their positive book net assets are **60 million and 40 million**, giving **60%/40%** of the total. An established transferable tax-loss balance of 10 million is therefore allocated **6 million/4 million**, preserving the original vintage. The example assumes no other recipient/remaining company, valuation dispute or restriction; it does not establish the transferability of a loss or resolve nonpositive net assets. [Articles 52(2), 54][law]

```oa-check
name: Iceland qualifying split net book asset allocation
inputs:
  a_book_assets: 90000000
  a_book_liabilities: 30000000
  b_book_assets: 65000000
  b_book_liabilities: 25000000
  established_transferable_loss: 10000000
steps:
  - a_net_assets: a_book_assets - a_book_liabilities
  - b_net_assets: b_book_assets - b_book_liabilities
  - combined_net_assets: a_net_assets + b_net_assets
  - a_ratio: a_net_assets / combined_net_assets
  - b_ratio: b_net_assets / combined_net_assets
  - a_allocated_loss: established_transferable_loss * a_ratio
  - b_allocated_loss: established_transferable_loss * b_ratio
expected:
  a_net_assets: 60000000
  b_net_assets: 40000000
  combined_net_assets: 100000000
  a_ratio: 0.6
  b_ratio: 0.4
  a_allocated_loss: 6000000
  b_allocated_loss: 4000000
```

### 17. Incorporation revaluation does not step up tax basis

Assume all domestic Article 56 conditions are met, the accepted opening balance has business assets of 40 million and liabilities of 15 million before revaluation, and those book amounts equal the supported tax amounts after all depreciation adjustments. Assume a properly accepted accounting revaluation increases an asset by 20 million without changing liabilities. Accounting equity then becomes **45 million**, while the owner's share basis for a later gain remains **25 million tax book equity**. The transferred assets' aggregate remaining tax carrying amount stays **40 million**, and original tax cost/depreciation bases continue unchanged in their own schedules; the 20 million is not new tax depreciation basis. This simplified example assumes no other book/tax differences or owner withdrawals. [Article 56][law]; [Regulation 223/2003, Articles 7–8][incorp-reg]; [Current guidance][incorp-guidance]

```oa-check
name: Iceland incorporation preserves tax basis despite book revaluation
inputs:
  pre_revaluation_book_and_tax_assets: 40000000
  supported_liabilities: 15000000
  accepted_accounting_revaluation: 20000000
steps:
  - tax_book_equity_share_basis: pre_revaluation_book_and_tax_assets - supported_liabilities
  - revalued_book_assets: pre_revaluation_book_and_tax_assets + accepted_accounting_revaluation
  - revalued_accounting_equity: revalued_book_assets - supported_liabilities
  - remaining_transferred_tax_carrying_amount: pre_revaluation_book_and_tax_assets
  - tax_carrying_amount_increase: remaining_transferred_tax_carrying_amount - pre_revaluation_book_and_tax_assets
expected:
  tax_book_equity_share_basis: 25000000
  revalued_book_assets: 60000000
  revalued_accounting_equity: 45000000
  remaining_transferred_tax_carrying_amount: 40000000
  tax_carrying_amount_increase: 0
```

## Ask the client first

- What are the entity's legal form, separate-taxpayer election, residence/management, accounting year and approved currency?
- Which accounts, ledgers, contracts, payroll reports, asset registers, inventory and receivable schedules reconcile to the return?
- What dividends, share disposals, financing, FX and foreign items need distinct adjustments?
- Which loss vintages, ownership/business changes, group approvals or reorganisations affect use of losses?
- For restructuring, what legal transaction, taxpayer status, consideration, shareholder proportions, approvals/effective dates, book/tax asset values, loss-purpose/activity evidence and audit/formation records establish the claimed route?
- What filing extension, assessment, advance notices, reductions, withholding and actual payments already exist?
- Are there regulated financial activities, foreign holdings, incentives, related parties or planned asset/company moves?
- For financial-sector taxes, what actual licences/services and exemptions apply, which wage/benefit/pension allocations support the remuneration base, what stand-alone profit base precedes losses, and which year-end tax-return liabilities and payment notices reconcile to the separate charges?
- For R&D, who owns and funds the project, what timely approval covers the year, what enterprise-size/group evidence applies, and which signed cost statements, supplier-country/relationship records, collaboration terms and domestic/foreign public grants reconcile to the claim?

<!-- openaccountants-cta-block -->

## Talk to an accountant

For professional review of the facts and workpapers, [contact OpenAccountants](https://www.openaccountants.com/contact).

## Sources

Read **23 October 2026**. Statutes display the 1 October 2026 compilation. Regulation 1370/2025 was retrieved directly as HTML; its page states that the official Gazette prevails over its reproduction. The primary-source rewrite replaces the former short 2025 summary while preserving its file identity and attribution. This is a source-cited draft, not professional attestation. Independent Icelandic legal review, the negative-profit interest-cap boundary, CFC timing/substance disputes and foreign-relief cases outside the shared workpaper, other sector/incentive/minimum-tax applicability, disputed restructuring/valuation/loss cases and current filing-system verification remain open. The restructuring addition covers the stated domestic routes and their separate loss/basis/date controls; it does not resolve every atypical transaction or company-law procedure. The official linked procedure page retains historical rates and broad no-succession wording; current Article 56, Regulation 223/2003 and the current registry page control the conditional incorporation method. The financial-sector addition supplies the stated three-charge computation and reporting method; disputed classifications, foreign-branch attribution, reserve/winding-up exceptions and actual submission acceptance still need their evidence and independent review. The added R&D method uses the current 2026 amendment and August 2026 handbook; enterprise-size boundaries, overlapping aid/cost limits and accepted future-year claim forms require the stated evidence and independent review. The 2027 filing/payment timetable is not established by the 2026 notices. Example amounts are invented assumptions.
| Source | URL | Read on |
|---|---|---|
| Income Tax Act 90/2003, Articles 2–4, 7–8, 12–61, 70–71, 90–99, 108, 112–114, 119 | [Alþingi][law] | 2026-10-23 |
| Skatturinn, corporate income tax | [Authority guidance][corporate] | 2026-10-23 |
| Skatturinn, 2026 rates | [Current-year rate table][rates] | 2026-10-23 |
| Skatturinn, 2026 assessment on 2025 income | [Assessment information][assessment] | 2026-10-23 |
| Skatturinn, RSK 1.04 filing method | [Return instructions][return] | 2026-10-23 |
| Skatturinn, 30 January 2026 corporate filing notice | [Filing notice][filing-notice] | 2026-10-23 |
| Regulation 1370/2025, 2026 payment cycle | [Regulation][payment-reg] | 2026-10-23 |
| Skatturinn, corporate advance-tax guidance | [Advance payments][advances] | 2026-10-23 |
| Act 33/2020, Article 6, excess-interest wording | [Enacted amendment](https://www.althingi.is/altext/stjt/2020.033.html) | 2026-10-23 |
| Bill 626/150, section 3.5, positive-profit interest calculation | [Official explanation](https://www.althingi.is/altext/150/s/0626.html) | 2026-10-23 |
| CFC Regulation 1102/2013, computation, substance, losses and reports | [Regulation](https://files.reglugerd.is/pdf/1102-2013/current) | 2026-10-23 |
| Skatturinn, CFC report and identifier requirements | [Reporting guidance](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/cfc-felog/) | 2026-10-23 |
| Act 152/2009, current R&D entitlement, costs, credit, aid, procedure and sanctions | [Current statute][rd-law] | 2026-10-23 |
| Act 27/2026, 2026 R&D procedural and purchased-cost amendments | [Enacted amendment][rd-amendment] | 2026-10-23 |
| Regulation 758/2011, project costs, aid and debt setoff; older decision period distinguished | [Current reproduction][rd-reg] | 2026-10-23 |
| Rannís, August 2026 application handbook, linked from the official grants portal | [Official handbook][rd-handbook] | 2026-10-23 |
| Rannís, 20 August 2026 application notice | [Dated notice][rd-notice] | 2026-10-23 |
| Skatturinn, published RSK 4.21 (2026 return) and RSK 4.22 (2025 label) | [4.21][rd-form]; [4.22][rd-coop-form] | 2026-10-23 |
| European Commission, SME definition and group-data warning | [Definition][rd-sme] | 2026-10-23 |
| Act 165/2011, financial remuneration tax scope, bases, exclusions, collection and deduction | [Current statute][fat-law] | 2026-10-23 |
| Act 155/2010, bank-liability scope/base/rate and nondeductibility | [Current statute][bank-law] | 2026-10-23 |
| Skatturinn, January 2026 employer notice, financial remuneration rate | [Dated notice][fat-notice] | 2026-10-23 |
| Regulation 223/2003, sole-trade incorporation, audit, succession and continued tax/share bases | [Current reproduction][incorp-reg] | 2026-10-23 |
| Skatturinn, current ehf. incorporation and sole-trade conversion dates | [Registry guidance][incorp-guidance] | 2026-10-23 |
| Skatturinn, linked procedure page; historical rates/overbroad succession wording distinguished | [Procedure page][incorp-procedure] | 2026-10-23 |

[law]: https://www.althingi.is/lagas/nuna/2003090.html
[corporate]: https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tekjuskattur/
[rates]: https://www.skatturinn.is/einstaklingar/helstutolur/2026
[assessment]: https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/alagningarsedill-og-forsendur/2026/
[return]: https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/skattframtal-rekstraradila/
[filing-notice]: https://www.skatturinn.is/um-rsk/frettir-og-tilkynningar/opnad-fyrir-skil-a-skattframtali-logadila-2026
[payment-reg]: https://island.is/reglugerdir/nr/1370-2025
[advances]: https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/fyrirframgreidsla-thinggjalda/

[rd-law]: https://www.althingi.is/lagas/nuna/2009152.html
[rd-amendment]: https://www.althingi.is/altext/stjt/2026.027.html
[rd-reg]: https://files.reglugerd.is/pdf/0758-2011/current
[rd-handbook]: https://assets.ctfassets.net/8k0h54kbe6bj/2RRCQujMqAjymTTMW8B5rb/5c12a20c7dcaf5b905f629c6805dcc57/6588aab1-6369-4453-9990-35a7c22eab13.pdf
[rd-notice]: https://island.is/frett/opid-fyrir-nyjar-umsoknir-um-skattfradratt-vegna-rannsokna-og-throunarverkefna-a-arinu-2026
[rd-form]: https://www.skatturinn.is/media/rsk04/rsk_0421_2026.is.pdf
[rd-coop-form]: https://www.skatturinn.is/media/rsk04/rsk_0422_2025.is.pdf
[rd-sme]: https://single-market-economy.ec.europa.eu/smes/sme-fundamentals/sme-definition_en

[fat-law]: https://www.althingi.is/lagas/nuna/2011165.html
[bank-law]: https://www.althingi.is/lagas/nuna/2010155.html
[fat-notice]: https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf

[incorp-reg]: https://files.reglugerd.is/pdf/0223-2003/current
[incorp-guidance]: https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/
[incorp-procedure]: https://www.skatturinn.is/fyrirtaekjaskra/stofnun-felaga/einkahlutafelog/verklagsreglur
