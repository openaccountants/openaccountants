---
name: fl-corporate-income-tax
description: "Source-cited tax guide for US-FL: fl corporate income tax. Unverified draft, pending local-accountant review."
jurisdiction: US-FL
tax_year: 2025
last_updated: 2026-11-25
version: "1.1"
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Rob Hoffman"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
---

# FL Corporate Income Tax

## Florida Corporate Income Tax (Ch. 220 Fla. Stat.)

**Non-usable hold:** Multistate service/intangible sourcing and a complete entity-specific filing result are not established by this summary.

Florida Corporate Income/Franchise Tax under Chapter 220, Florida Statutes, applies to C-corporations doing business in Florida at a 5.5% rate on apportioned Florida net income, after a $50,000 exemption. Apportionment uses a three-factor formula with double-weighted sales (property + payroll + 2x sales / 4) and cost-of-performance sourcing for services. Filed on Form F-1120. Florida has no personal income tax, so sole proprietors, partnerships, LLCs taxed as partnerships, and S-corporations generally owe no Florida income tax on operating income. Tax year 2025.

> **Correction draft for tax year 2025.** Independent source review and accountant approval of this changed version are pending. Retained approval metadata does not certify this draft. Explicit non-usable holds do not establish filing, payment or tax positions.

## 1. Scope

This skill covers the Florida Corporate Income/Franchise Tax imposed under Chapter 220 of the Florida Statutes for tax year 2025. It addresses:

- Determination of which entities are subject to the tax and which are exempt.
- The 5.5% headline rate, the $50,000 exemption, and the legislative history of rate-adjustment rebates under the "TRIM Act" (s. 220.1105, F.S.).
- The federal-conformity starting point and the principal Florida additions and subtractions in s. 220.13, F.S.
- Apportionment under s. 220.15, F.S., using the three-factor formula with double-weighted sales and cost-of-performance service sourcing.
- Net operating losses under s. 220.13(1)(b)1., F.S.
- Form F-1120 filing, the F-7004 extension, and quarterly estimated payments.
- The principal Florida corporate income tax credits relevant to small and mid-sized C-corporations.
- Common reviewer-level errors, especially the recurring mistake of treating disregarded single-member LLCs as separately taxable in Florida.

This skill does NOT cover:

- Sales and use tax (Ch. 212, F.S.) — see the Florida sales tax skill.
- Documentary stamp tax on real estate transfers (Ch. 201, F.S.) — refer out.
- Reemployment tax (Ch. 443, F.S.) — refer out.
- Insurance premium tax (Ch. 624, F.S.) — refer out.
- Consolidated/combined return elections under s. 220.131, F.S. — refer to a credentialed Florida specialist.
- Bank and savings association franchise tax under s. 220.63, F.S. (which uses the same Ch. 220 mechanics but applies to financial institutions).
- Federal income tax — federal return must already be complete; this skill picks up at federal taxable income.

This skill assumes the user is a sole proprietor, single-member LLC, multi-member LLC, partnership, S-corp, or small C-corp filing a Florida return. It is not designed for large multistate consolidated groups, REITs, regulated investment companies, or insurance companies.

## 2. Who is Subject to Florida Corporate Income Tax

### 2.1 Entities subject to the tax

- **General tax imposition** — Tax is imposed on the Florida net income of every taxpayer doing business in Florida, deriving income from sources in Florida, or existing with a nexus to Florida sufficient to create a constitutional taxing jurisdiction. "Taxpayer" means a corporation subject to the tax.  _(s. 220.11, F.S.; s. 220.03(1)(z), F.S.)_
- **C-corporations** — C-corporations organized under the laws of Florida or any other jurisdiction, doing business in Florida, are subject to the tax.  _(s. 220.11, F.S.)_
**Non-usable hold:** Consequences of a failed S election require actual classification/election facts; no universal deemed-corporation outcome is cleared.

- **LLCs electing C-corp status** — LLCs that have elected to be taxed as a C-corporation for federal purposes (Form 8832 election to be treated as an association taxable as a corporation, or a deemed corporation election triggered by an S-election that is invalid) file F-1120 in the same manner as any other C-corp.  _(s. 220.11, F.S.)_
**Non-usable hold:** Current economic-nexus law and remote-service facts are not fully established; absence of physical presence does not establish non-filing.

- **Foreign C-corporations nexus** — Foreign (out-of-state) C-corporations with sufficient nexus under s. 220.11, F.S. and Florida's economic nexus jurisprudence are subject to the tax. Florida has not enacted a bright-line economic nexus statute for corporate income tax, but physical presence, employees, or property in Florida triggers nexus.  _(s. 220.11, F.S.)_
**Non-usable hold:** Complete bank/financial-organization rules remain outside this examination.

- **Banks and savings associations** — Banks and savings associations are subject under s. 220.63, F.S. (outside the scope of this skill).  _(s. 220.63, F.S.)_

### 2.2 Entities NOT subject to the tax

- **Sole proprietorships** — Florida has no personal income tax. A self-employed individual operating as a sole proprietor pays no Florida income tax on Schedule C profits, no Florida tax on self-employment earnings, and no Florida tax on wages. The individual files only the federal Form 1040 and Schedule C/SE.  _(Florida has no personal income tax)_
- **Single-member LLCs disregarded**: the LLC has no separate F-1120 filing obligation, but its owner includes the income in the owner's appropriate return. The owner may be a corporation required to file F-1120; individual business, rental and farming activities do not all use Schedule C. [Source](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx).
- **Multi-member LLCs taxed as partnerships** — The LLC files federal Form 1065 and issues K-1s. Florida does not impose an entity-level tax on partnerships or pass-throughs. Florida Form F-1065 (partnership information return) is required only if a partner is a corporation subject to Ch. 220 — most small multi-member LLCs with only individual members do not file F-1065.  _(s. 220.13, F.S.)_
**Non-usable hold:** Complete partnership filing conditions and actual corporate ownership require confirmation.

- **General and limited partnerships** — General and limited partnerships taxed as partnerships federally receive the same treatment as multi-member LLCs.  _(s. 220.13, F.S.)_
- **S-corporations** — Florida does not impose corporate income tax on income that is taxed at the shareholder level federally. The Florida starting point for an S-corp is the federal taxable income of the S-corp itself, which for pure S-corp income (passing through on Schedule K-1) is generally zero at the entity level. However, an S-corp IS required to file F-1120 if the federal return shows taxable income at the entity level, most commonly: Built-in gains tax under IRC §1374 (if the S-corp pays §1374 tax federally, that built-in gain income flows through as Florida taxable income and the S-corp must file F-1120 reporting the federal taxable income that is subject to Florida tax); LIFO recapture under IRC §1363(d) on conversion from C to S; Excess net passive income tax under IRC §1375. In each case the S-corp files F-1120 reporting only the federally-taxed amount, then claims the $50,000 exemption (which usually wipes out the Florida liability for small S-corps).  Use the federal corporate-level-tax gateway in the [DOR guidance](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx) and [F-1120 instructions](https://floridarevenue.com/Forms_library/current/f1120n.pdf); the instructions refer to Form 1120-S line 23c tax. Section 220.13(2)(k) concerns AMT and is not the S-corporation gateway. The detailed federal conversion/item computations and assumed exemption outcome remain non-usable holds.
- **Sole proprietors using a single-member LLC** — No federal return for the LLC, no Florida return.  _(s. 220.03(1)(e), F.S.)_
**Non-usable hold:** Separate-return treatment does not settle owner-level liability; QSub/trust classification remains unverified.

- **Disregarded entities of any kind** — E.g., QSubs of an S-corp, grantor trust-owned LLCs, are not subject to the tax.  _(s. 220.03(1)(e), F.S.)_
- **Individuals** — Florida has no personal income tax. Art. VII, s. 5, Florida Constitution prohibits state income tax on natural persons without a constitutional amendment, which has not been enacted.  _(Art. VII, s. 5, Florida Constitution)_
- **501(c) exempt organizations** — Not subject except to the extent they have unrelated business taxable income (UBTI) under IRC §511 — UBTI is subject to Florida corporate income tax starting from federal taxable income on Form 990-T.  _(s. 220.13(1)(a), F.S.; IRC §511)_
- **Insurance companies** — Insurance companies subject to insurance premium tax are out of scope.  _(out of scope)_

### 2.3 Why Florida is a "no income tax" state for individuals

**Non-usable hold:** The historical enactment and all-state population narrative is unverified; do not infer other-tax clearance.

Florida is one of nine states with no state-level personal income tax. The prohibition is constitutional: Art. VII, s. 5 of the Florida Constitution provides that no tax upon income shall be levied by the state upon natural persons. The Florida corporate income tax, enacted by Ch. 220 in 1971 following a constitutional amendment authorizing it, applies only to corporations and not to individuals, partnerships, or other pass-through entities.

The practical effect for the typical OpenAccountants user base is:

- A freelance software developer in Miami pays federal income tax and federal self-employment tax. No Florida tax.
- A two-partner consulting LLC taxed as a partnership in Tampa pays no Florida tax at the entity level. Each partner pays only federal tax.
- An owner-operated S-corp in Orlando pays no Florida tax on the pass-through income; the shareholder reports the K-1 on their federal 1040 and pays no Florida tax.
- A small C-corp in Jacksonville pays 5.5% Florida tax on apportioned Florida net income, after the $50,000 exemption.

## 3. Rate and the $50,000 Exemption

### 3.1 Statutory rate

- **Florida corporate income tax rate** — 5.5% (Rate on Florida net income for tax year 2025, after the temporary TRIM Act rebate period.)  _(s. 220.11(2), F.S.)_

### 3.2 Historical rebate periods (TRIM Act mechanics)

**Non-usable hold:** Full refund mechanism and historical application periods are unverified.

- **TRIM Act mechanism** — Section 220.1105, F.S. (the "Tax Refund and Rate Reduction Mechanism," sometimes called the TRIM Act) created an automatic rebate-and-rate-reduction mechanism that operated for tax years 2018 through 2021. When net corporate income tax collections exceeded statutory adjusted-revenue baselines, the Department of Revenue was required to: 1. Issue refunds to taxpayers for the prior year's overpayment. 2. Reduce the rate for the following tax year by a downward adjustment.  _(s. 220.1105, F.S.)_

**Historical effective rates table**: [DOR rate periods](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx) and [TIP 21C01-02](https://floridarevenue.com/taxes/tips/Documents/TIP_21C01-02.pdf). TIP 21C01-01 is IRC adoption, TIP 22C01-01 is internship credit, and TIP 22C01-02 is automatic refund; do not use them as the claimed rate notices.

| Tax year | Effective rate | Source |
| --- | --- | --- |
| 2018 | 5.5% | [DOR rate table](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx) |
| 2019 | 4.458% | [TIP 19C01-04](https://floridarevenue.com/taxes/tips/documents/TIP_19C01-04.pdf) |
| 2020 | 4.458% | [TIP 21C01-02](https://floridarevenue.com/taxes/tips/Documents/TIP_21C01-02.pdf) |
| 2021 | 3.535% | [TIP 21C01-02](https://floridarevenue.com/taxes/tips/Documents/TIP_21C01-02.pdf) |
| 2022 | 5.5% | [TIP 21C01-02](https://floridarevenue.com/taxes/tips/Documents/TIP_21C01-02.pdf) |
| 2023 | 5.5% | [Section 220.11](https://www.flsenate.gov/Laws/Statutes/2025/220.11) |
| 2024 | 5.5% | [Section 220.11](https://www.flsenate.gov/Laws/Statutes/2025/220.11) |
| 2025 | 5.5% | [Section 220.11](https://www.flsenate.gov/Laws/Statutes/2025/220.11) |

**Non-usable hold:** The asserted expiration/last-refund history is unverified; the separate official rate table controls the rate.

- **TRIM Act expiration and 2025 guidance** — The TRIM Act mechanism in s. 220.1105 expired on its own terms after the 2021 fiscal year refund. Beginning with tax year 2022, the rate has been the statutory 5.5% with no further automatic rebates. For 2025, use 5.5%. Do not attempt to apply any TRIM Act reduction. If preparing an amended return for a 2020 or 2021 tax year, verify the correct effective rate from the FL DOR Tax Information Publication for that year.  _(s. 220.1105, F.S.)_

### 3.3 The $50,000 exemption

- **$50,000 exemption** — $50,000 USD (Exemption from Florida net income before applying the 5.5% rate; a true deduction from the tax base, not a credit.)  _(s. 220.14, F.S.)_
- **Florida tax computation mechanics**: 1. Start with the applicable federal taxable-income amount; ordinary Form 1120 line 30 is after federal NOL/special deductions, with the federal NOL separately added back. Do not use Form 1120-S line 21 as a universal S-corporation base. 2. Apply Florida modifications. 3. Remove nonbusiness income before apportionment. 4. Apply the applicable ordinary/reweighted or special factor method. 5. Add Florida-allocated nonbusiness income. 6. Apply the available exemption, including controlled-group sharing. 7. Apply the ordinary 5.5% rate and eligible credits. Apply the separate NOL instructions; this sequence does not resolve held federal/S-corporation/AMT facts. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).
- **Below-exemption filing note** — If apportioned Florida net income is less than $50,000, no Florida tax is due (but F-1120 may still need to be filed — see Section 7).  _(s. 220.14, F.S.)_
- **Short-period proration** — The exemption is pro-rated for short-period returns — multiply $50,000 by (number of days in the short period / 365).  _(s. 220.14(2), F.S.)_
- **Controlled groups filing separately**: Florida members share one exemption under section 220.14(4), equally allocated unless they consent to another allocation. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.14).
- **Consolidated returns single exemption** — For consolidated returns under s. 220.131, F.S., only one $50,000 exemption is available for the entire consolidated group.  _(s. 220.14(3), F.S.)_

### 3.4 Alternative minimum tax — Florida AMT

**Non-usable hold:** The statute retains a 3.3% alternative computation. Complete CAMT and group applicability is unverified; do not assume every small-company case is excluded.

- **Florida AMT status** — Florida historically imposed an alternative minimum tax tied to the federal corporate AMT. With the federal repeal of the corporate AMT for tax years beginning after December 31, 2017 (TCJA), Florida's AMT effectively went dormant. The federal Corporate Alternative Minimum Tax (CAMT) enacted by the Inflation Reduction Act of 2022 applies to "applicable corporations" with three-year average AFSI of $1 billion or more — this is far outside the scope of small-business Florida filings. For 2025, treat Florida AMT as non-applicable for OpenAccountants's typical small-business taxpayers.  _(s. 220.11(3), F.S.)_

## 4. Federal Conformity and Florida Modifications (s. 220.13)

### 4.1 Starting point

- **Specified-date conformity and starting point**: Florida updates its specified IRC adoption date by legislation; conformity is not automatically rolling. The 2025 statute specifies January 1, 2025. The current 2026 statute/TIP adopts January 1, 2026 with enumerated decoupling and pro forma/amendment directions. Complete application of the 2026 changes to a specific 2025 return remains held. Ordinary Form 1120 line 30 is after federal NOL/special deductions; Florida adds the federal NOL separately, avoiding double addition. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.03). [Source](https://floridarevenue.com/taxes/tips/Documents/TIP_26C01-01.pdf). [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

### 4.2 Florida additions (s. 220.13(1)(a), F.S.)

**Non-usable hold:** Historical refund/intangible/965 and section 179 application is unverified; current adoption/pro forma rules require case-specific confirmation.

- **Principal addbacks** — The principal addbacks for a small C-corp are: Federal NOL deduction — Florida disallows the federal NOL deduction (because Florida has its own NOL system). Add back the federal NOL claimed on Line 29a of Form 1120. Federal income tax refund if previously deducted (rare for corporations). Florida intangible tax (now repealed but included for historical adjustments). Income taxes paid to all states, including Florida and DC, deducted federally are added back; this item excludes gross-receipts taxes and city/county income taxes. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf). Depreciation differences under s. 220.13(1)(e), F.S. — Florida decouples from federal bonus depreciation under IRC §168(k) and from the IRC §179 expensing limits for certain periods. For 2025, verify the current addback rules in the Form F-1120 instructions. For covered ordinary bonus additions, one-seventh recovery begins in the same addition year and continues for six subsequent years. Qualified improvement property has a separate recovery based on pre-CARES depreciation; asset windows and current pro forma requirements must be established. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.13). Federal §965 deemed repatriation income addbacks (transition tax) — largely historical now. Interest excluded federally under IRC §103 is added back less attributable expenses disallowed federally; do not assume a blanket Florida-bond exception. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.13).  _(s. 220.13(1)(a), F.S.; s. 220.13(1)(a)1., F.S.; s. 220.13(1)(e), F.S.)_

### 4.3 Florida subtractions (s. 220.13(1)(b), F.S.)

**Non-usable hold:** Treasury immunity, foreign-dividend/Subpart F/GILTI netting and exact current-year deduction amounts remain unverified.

- **Principal subtractions** — Florida NOL carryforward (s. 220.13(1)(b)1., F.S.) — see Section 6. Net operating loss for the year allowed federally but limited federally — Florida applies its own NOL rules. Ordinary covered bonus recovery is one-seventh in the addition year and six subsequent years; qualified improvement property has separate pre-CARES-based recovery. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.13). Interest on US Treasury obligations to the extent included in federal taxable income. Salary and wage adjustment for the federal Work Opportunity Tax Credit — Florida allows the qualifying amounts paid in Florida and disallowed federally under IRC §280C(a), subject to the operative instructions. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.13). Subpart F income exclusions for foreign source income to the extent permitted under s. 220.13(1)(b)2., F.S. GILTI subtraction — Florida treats GILTI (IRC §951A) as subpart F income and follows federal treatment with a partial subtraction; verify current rules in the F-1120 instructions. Foreign-source dividends under s. 220.13(1)(b)2., F.S. that are not eligible for the federal dividends-received deduction.  _(s. 220.13(1)(b), F.S.; s. 220.13(1)(b)1., F.S.; s. 220.13(1)(b)2., F.S.)_

### 4.4 Adjusted federal income

- **Adjusted federal income** — After additions and subtractions, you have "adjusted federal income" — the Florida pre-apportionment base.  _(s. 220.13, F.S.)_

## 5. Apportionment (s. 220.15, F.S.)

### 5.1 The three-factor formula with double-weighted sales

- **Apportionment formula** — Apportionment % = (Property factor + Payroll factor + 2 x Sales factor) / 4. Each factor is the Florida-numerator divided by the everywhere-denominator. Sales is weighted 2x when all three factors are present. Zero/insignificant factors require reweighting: one remaining factor is 100%; without sales the property/payroll weights are 50% each; without one property/payroll factor the remaining nonsales factor is 33⅓% and sales 66⅔%. Apply special-industry methods where required. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.15).  _(s. 220.15, F.S.)_

Florida is one of a shrinking number of states still using a property-and-payroll-inclusive apportionment formula. Most states have moved to single-sales-factor apportionment over the past two decades. Florida's continued use of three-factor double-weighted-sales is a quirk that catches out-of-state preparers.

### 5.2 The property factor (s. 220.15(2), F.S.)

**Non-usable hold:** Inventory, idle property, construction and full property-rule classifications remain unverified; the ordinary cost/net-rent correction does not settle these.

- **Property factor mechanics** — The property factor is the average value of the corporation's real and tangible personal property owned or rented in Florida, divided by the average value of all such property everywhere. Owned property is valued at original cost (not net book value). Rented property is capitalized at eight times net annual rent after subrentals. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.15). Inventory is included at its tax-basis value. Idle property that has been actively used in business but is temporarily not in use is included. Construction in progress is generally excluded until placed in service.  ([ordinary property factor, section 220.15(2)](https://www.flsenate.gov/Laws/Statutes/2025/220.15)); subsection (3) additionally addresses financial-organization intangible property.

### 5.3 The payroll factor (s. 220.15(4), F.S.)

- **Payroll factor sourcing cascade** — The payroll factor is total compensation paid in Florida divided by total compensation paid everywhere. Compensation is sourced to Florida if: 1. The services are performed entirely in Florida; OR 2. The services are performed both in and outside Florida, but the services performed outside are incidental to the services in Florida; OR 3. Some services are performed in Florida and the employee's base of operations is in Florida; OR, where some services are performed in Florida, 4. There is no base of operations in a state where services are performed and direction/control is in Florida; OR 5. Neither the base nor direction/control is in a state where services are performed and the employee resides in Florida. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.15). This is the standard UDITPA-derived "base of operations" cascade. Independent contractor payments are NOT included in the payroll factor.  _(s. 220.15(4), F.S.)_

### 5.4 The sales factor (s. 220.15(5), F.S.) — cost-of-performance sourcing for services

- **Sales factor and tangible property sourcing** — The sales factor is total Florida sales divided by total sales everywhere. For tangible personal property, sales are sourced to Florida if the property is delivered or shipped to a purchaser in Florida, regardless of the FOB point (destination sourcing).  _(s. 220.15(5), F.S.)_
**Non-usable hold:** The full current service/intangible rule and judgments were not read. Categorical all-or-nothing/no-market conclusions are unavailable for reliance.

- **Cost-of-performance sourcing for services** — For services and intangibles, Florida uses cost-of-performance sourcing: A service is sourced to Florida if the income-producing activity is performed entirely in Florida; OR if the income-producing activity is performed in more than one state, the service is sourced to the state where the greater proportion of the income-producing activity is performed, based on costs of performance. This is the "all-or-nothing" cost-of-performance rule (as opposed to "pro-rata cost-of-performance"). The entire receipt goes to one state — whichever state has the highest cost of performance. There is no market-based sourcing in Florida for services.  _(s. 220.15(5)(b), F.S.; Rule 12C-1.0155, F.A.C.)_

**Non-usable hold:** The entirely Florida service proposition does not establish all multistate/SaaS results in this paragraph.

This matters enormously for software developers, consultants, and other service businesses. A Florida-based C-corp that performs services entirely in Florida sources 100% of its service receipts to Florida, even if all customers are out of state. Conversely, a non-Florida C-corp that has Florida customers but performs the work elsewhere sources 0% to Florida.

**Non-usable hold:** Other-state sourcing and historical dates are unverified.

Compare this to California (market-based sourcing — service receipts sourced to the customer's location), New York (market-based for most services since 2015), or Massachusetts (market-based since 2014). The contrast can produce dramatic differences in apportionment percentages.

**Non-usable hold:** Failed-bill history and the categorical current multistate sourcing conclusion are unverified.

Florida has resisted the trend toward market-based sourcing for over a decade despite repeated legislative proposals (e.g., HB 7129 in 2019, HB 7079 in 2021 — both failed). For tax year 2025, the rule remains cost-of-performance.

### 5.5 Special apportionment rules

**Non-usable hold:** Exact financial-organization, telecom and alternative-petition conditions are unverified; transportation has its own mandatory method.

- **Special apportionment categories** — Transportation services (railroads, motor carriers, airlines) — special apportionment formulas under s. 220.151, F.S. Financial organizations (banks, lenders) — special formula under s. 220.15(6), F.S. Insurance companies — separate framework (out of scope). Telecommunications — special rules. Petitions for alternative apportionment under s. 220.152, F.S. — taxpayer or DOR can petition for an alternative method if the standard formula does not fairly represent the extent of the taxpayer's Florida business activity. High burden of proof. Refer out for any alternative apportionment petition.  _(s. 220.151, F.S.; s. 220.15(6), F.S.; s. 220.152, F.S.)_

### 5.6 Nonbusiness income (s. 220.16, F.S.)

**Non-usable hold:** Actual business/nonbusiness character and complete royalty sourcing require confirmation; no actual holding-company income is classified.

- **Allocation of nonbusiness income** — Income that is not "business income" (i.e., income that is not from transactions and activity in the regular course of the taxpayer's trade or business) is allocated rather than apportioned. Common items: Nonbusiness real-property gains/losses allocate to situs; tangible-property gains have situs/taxability branches, while intangible gains allocate to commercial domicile. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.16). Royalties from intangibles — allocated based on the location of use. Dividends — allocated to the commercial domicile. Interest on nonbusiness assets — allocated to the commercial domicile. Rents from nonbusiness real property — allocated to the situs. For most operating C-corps, all income is business income and is fully apportioned. The business/nonbusiness distinction matters mostly for holding companies and investment-heavy entities.  _(s. 220.16, F.S.)_

### 5.7 Apportionable income vs. Florida net income — order of operations

- **Order of operations** — 1. Federal taxable income (Form 1120 Line 30). 2. Apply Florida additions and subtractions per s. 220.13 → "adjusted federal income." 3. Subtract nonbusiness income (which will be allocated separately) → "apportionable income." 4. Apply the three-factor double-weighted sales apportionment formula → Florida apportioned income. 5. Add Florida-allocated nonbusiness income → Florida net income. 6. Subtract the $50,000 exemption (s. 220.14). 7. Multiply by 5.5% → gross Florida tax. 8. Subtract credits.  _(s. 220.13, F.S.; s. 220.14, F.S.; s. 220.15, F.S.; s. 220.16, F.S.)_

## 6. Net Operating Losses (s. 220.13(1)(b)1., F.S.)

### 6.1 Post-2017 NOLs (Florida-mirrors-federal framework)

- **Post-2017 NOL rules** — For NOLs arising in tax years beginning after December 31, 2017, Florida follows the post-TCJA federal framework: For deduction years beginning after 2020, apply the 80% limitation to post-2017 losses as instructed. Earlier deduction years can allow 100%; loss vintage and deduction year are separate conditions. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf). This mirrors IRC §172(a)(2) as amended by TCJA. No carryback — Florida does not permit NOL carrybacks (consistent with federal post-TCJA treatment). Indefinite carryforward — The unused NOL carries forward indefinitely until exhausted (no 20-year limit).  _(IRC §172(a)(2); s. 220.13(1)(b)1., F.S.)_

### 6.2 Pre-2018 NOLs (grandfathered)

- **Pre-2018 NOL grandfathered rules** — NOLs generated in tax years beginning before January 1, 2018 retain their pre-TCJA characteristics: 20-year carryforward limit (so 2017 NOLs expire after 2037). No 80% limitation — they can offset 100% of Florida taxable income. No carryback (Florida never allowed NOL carrybacks). The 80% limitation applies separately to pre- and post-2018 NOLs — pre-2018 NOLs are deducted first, without limitation; then post-2018 NOLs are deducted, subject to 80%.  _(s. 220.13(1)(b)1., F.S.)_

### 6.3 Computation mechanics

**Non-usable hold:** Exact loss-generation base is not established by the simplified steps; use actual federal loss, loss-year factor and permitted adjustments.

- **Florida NOL computation** — The Florida NOL is computed on a Florida-only basis. It is NOT the federal NOL. To compute the Florida NOL: 1. Start with adjusted federal income for the loss year. 2. Apply apportionment. 3. The Florida-apportioned loss (after the $50,000 exemption is NOT subtracted in a loss year — the exemption is for income years only) is the Florida NOL. Track each year's NOL separately. An entirely Florida business reports its carryforward subtraction on Schedule II line 3; a multistate business uses Schedule IV line 4. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf). The DOR requires year-by-year carryforward tracking.  _(s. 220.13(1)(b)1., F.S.)_

### 6.4 Ownership change limitations

**Non-usable hold:** The same dollar cap is not established without federal/Florida ownership-change and apportionment facts.

- **IRC §382 conformity** — Florida conforms to IRC §382 limitations on NOL utilization following an ownership change. If a federal §382 limit applies, the same limit applies for Florida purposes.  _(IRC §382)_

### 6.5 NOL and S-corp conversions

**Non-usable hold:** Complete federal/state conversion, built-in-gains and NOL interaction remains unverified.

- **NOL suspension on S-election** — If a C-corp with NOL carryforwards elects S-corp status, the C-corp NOLs are suspended at the entity level. They can be used to offset any built-in gains tax or other federally-taxed C-corp items that flow into Florida F-1120 (very rare). They cannot pass through to the shareholders.

## 7. Filing — Form F-1120

### 7.1 Who must file

- **Filing requirement** — Every corporation subject to Florida corporate income tax must file Form F-1120, even if no tax is due. Filing is required if: The corporation is doing business, earning income, or existing in Florida. The corporation files a federal Form 1120, 1120-S (with federally-taxed items), 1120-F, or similar. A corporation with no Florida nexus does not file. A pure pass-through (partnership, S-corp without federally-taxed items, disregarded entity) does not file.

### 7.2 Due date

- **F-1120 due date rule**: ordinarily the first day of the fifth month after year-end or the 15th day after the federal due date, whichever is later. A June 30 year-end has the statutory fourth-month branch and seven-month extension for the covered 2025 period. Apply weekends/holidays and the actual return-year instructions. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.222). [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).
- **Calendar-year due dates for 2025** — For calendar-year C-corps: Federal Form 1120 is due April 15, 2026 for tax year 2025. Florida F-1120 is due May 1, 2026 (1st day of the 5th month after Dec 31, 2025). Note: this is one day after the comparable federal extension consideration deadline. The Florida due date is genuinely later than the federal due date, not the same.
- **Fiscal-year filers due date**: use the statutory ordinary fifth-month/later-federal rule, with the June 30 fourth-month exception described above; do not apply fifth-month timing to every fiscal year. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.222).

### 7.3 Extension — Form F-7004

- **Extension requirements**: timely file F-7004 and pay the tentative tax by the original due date; a federal extension alone does not suffice. Section 220.222(2)(d) tests whether tentative tax is understated by more than the greater of $2,000 or 30% of tax shown; every small final shortfall does not automatically invalidate the extension. Filing extensions do not extend payment. Ordinary extension is six months; the covered June 30 branch is seven months. The ordinary calendar-2025 extended date is November 2, 2026 because November 1 is Sunday. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.222). [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.32). [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

### 7.4 Electronic filing

- **E-filing mandate**: corporations that paid $5,000 or more in Florida corporate income tax during the preceding state fiscal year (July 1–June 30) must file/pay electronically. A federal mandatory electronic-filing requirement independently triggers Florida electronic filing. Use approved MeF software for F-1120; do not infer long-form portal filing from short-form/payment services. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

### 7.5 Penalties

- **Failure to file penalty**: ordinarily 10% of tax due per month/fraction, capped at 50%; a zero-tax late return instead incurs $50 per month/fraction, capped at $300. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).
**Non-usable hold:** The standalone 10%/$10 rule below was not established by the read authorities; do not use it to assess a payment penalty.

- **Failure to pay penalty** — 10% of the unpaid tax. Statutory floor of $10 even if the percentage is less.
- **Interest rate**: floating DOR interest is separate from the fixed annual estimated/tentative tax penalties. DOR lists 11% for both halves of 2026; use the applicable date-specific notice for 2025 balances, not an assumed 9%. [Source](https://floridarevenue.com/taxes/taxesfees/Pages/tax_interest_rates.aspx). [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.807).
- **Fraud penalty** — 100% penalty.  _(s. 220.803, F.S.)_
- **Negligence penalty**: 10% of the deficiency, rather than 25%. Fraud is the separate 100%-of-deficiency alternative. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.803).

## 8. Estimated Tax (s. 220.222 and 220.34, F.S.)

### 8.1 When estimated payments are required

- **Estimated payment threshold** — $2,500 USD (A corporation must make quarterly estimated payments if its estimated Florida tax liability for the year exceeds this amount. Below that threshold, no estimated payments are required and the full liability can be paid with the F-1120.)  _(s. 220.222, F.S.)_

### 8.2 Installment due dates

**Installment due dates**: [section 220.33](https://www.flsenate.gov/Laws/Statutes/2025/220.33). General calendar pattern only; apply weekend/holiday, first-liability and special June-weekend acceleration rules.

| Installment | Due date | % of total |
| --- | --- | --- |
| 1st | May 31 (last day of 5th month of tax year) | 25% |
| 2nd | June 30 (last day of 6th month) | 25% |
| 3rd | September 30 (last day of 9th month) | 25% |
| 4th | December 31 of the calendar tax year (before the next tax year begins) | 25%; [section 220.33](https://www.flsenate.gov/Laws/Statutes/2025/220.33) |

- **Fiscal-year substitution** — For fiscal-year filers, substitute the corresponding months of the fiscal year.

### 8.3 Form

- **Estimated payment form**: use F-1120ES or electronic payments. General installments are 25%; the F-1120 instructions expressly prohibit annualizing payments. Short-year annualization to determine declaration liability is a different rule. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

### 8.4 Underpayment penalty

- **Underpayment penalty and safe harbors**: compute on F-2220 under section 220.34. The prior-year alternative uses prior-year facts/law with current-year rates and applicable current-credit adjustments, rather than blindly paying the prior return's dollar tax. The 90%-of-current-year alternative is separate. Do not annualize installments. The estimated-tax penalty is 12% per year; floating interest under section 220.807 is separate. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.34). [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf). [Source](https://floridarevenue.com/taxes/tips/Documents/TIP_21C01-02.pdf).

## 9. Credits

Florida offers a modest set of corporate income tax credits, most of which are narrow and not applicable to typical small C-corps.

### 9.1 Capital Investment Tax Credit (s. 220.191, F.S.)

**Non-usable hold:** Current agency, project certification, jobs/wages and application facts remain unverified; headline measure/tier corrections do not establish eligibility.

- **Capital Investment Tax Credit** — For corporations making a "qualifying project" investment in Florida of at least $25 million in certain target industries (clean energy, biomedical, financial services, information technology, silicon technology, transportation equipment manufacturing). The ordinary annual measure is 5% of eligible capital cost for up to 20 years, with project-tax limits of 50%, 75% and 100% at the $25 million, $50 million and $100 million tiers respectively. Special project branches and certification conditions require separate confirmation. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.191). Application to Enterprise Florida is required before the project begins. This is a high-bar credit aimed at large corporate relocations.  _(s. 220.191, F.S.)_

### 9.2 Research and Development Tax Credit (s. 220.196, F.S.)

- **R&D Tax Credit** — A credit equal to 10% of qualified research expenses in Florida that exceed the taxpayer's average Florida QRE for the prior four years. The credit: Mirrors the federal IRC §41 R&D credit definition of qualified research. Requires the taxpayer to be in one of the target industries (manufacturing, life sciences, information technology, aviation/aerospace, homeland security/defense, cloud information technology, marine sciences, materials science, nanotechnology). Requires an allocation from the FL DOR — total annual credit is capped at $9 million statewide, allocated proportionately if eligible applications exceed the cap. The statutory application window is March 20–26 of the following year. The credit is limited to 50% of remaining tax after other credits; each missing base year reduces the credit by 25%. Apply the required Commerce certification and allowed-federal-credit gateway. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.196). Unused credit carries forward 5 years.  _(s. 220.196, F.S.; IRC §41)_

### 9.3 Voluntary Cleanup Tax Credit (s. 220.1845, F.S.)

- **Voluntary Cleanup Tax Credit** — A credit for voluntary cleanup of brownfield sites and dry-cleaning solvent contamination. 50% of cleanup costs, capped at $500,000 per site per year. Statewide authorization is $35 million per state fiscal year under section 376.30781(4). [Source](https://www.flsenate.gov/Laws/Statutes/2025/376.30781). Application to FL DEP required. Useful for real estate developers and industrial users.  ([section 220.1845](https://www.flsenate.gov/Laws/Statutes/2025/220.1845))

### 9.4 Florida Tax Credit Scholarship Program (s. 220.1875, F.S.)

- **Tax Credit Scholarship Program**: the initial credit measure is 100% of an eligible contribution to an approved SFO, including the original Step Up For Students example, subject to allocation, timing and ordering. Section 220.1875 requires reduction for the federal tax benefit and section 220.13 requires a state addback. Therefore the final credit is not automatically the gross contribution or a zero balance. The corporate program allows unused-credit carryforward for no more than ten years. Apply the separate federal deduction rules, including the corporate section 162 safe harbor in Rev. Proc. 2019-12; do not promise a cost-free tax redirection. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.1875). [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.13). [Source](https://floridarevenue.com/taxes/taxesfees/Pages/sfo_taxes.aspx).

### 9.5 Other credits (brief list)

**Non-usable hold:** Full caps, sunsets, eligibility and certification for the listed minor credits are unverified.

- **Other Florida credits** — Community Contribution Tax Credit (s. 220.183) — 50% of contributions to approved community development projects, capped statewide. Hazardous Waste Facility Tax Credit (s. 220.184). Renewable Energy Production Credit (s. 220.193) — closed to new applicants. Strong Families Tax Credit (s. 220.1876) — contributions to eligible charitable organizations serving families. Florida New Markets Tax Credit (s. 220.185). Experiential Learning Tax Credit (s. 220.198) — for businesses hosting student internships. Internship Tax Credit Program (s. 220.198). Child Care Tax Credit (s. 220.1873). All Florida credits require contemporaneous documentation. Most require pre-approval by the DOR or a partner agency. Refer to F-1120 Schedule V for the credit summary.  _(s. 220.183, F.S.; s. 220.184, F.S.; s. 220.193, F.S.; s. 220.1876, F.S.; s. 220.185, F.S.; s. 220.198, F.S.; s. 220.1873, F.S.)_

### 9.6 Credit ordering

**Non-usable hold:** The full generic ordering algorithm is unverified; the scholarship-specific correction does not establish it.

- **Credit ordering rule** — Credits are applied in the order specified in s. 220.02(8), F.S. Generally, credits without carryforward are taken first, followed by carryforward credits. The scholarship credit has a maximum ten-year carryforward and follows other allowable credits under its own rules; the complete generic ordering algorithm remains held. [Source](https://floridarevenue.com/taxes/taxesfees/Pages/sfo_taxes.aspx).  _(s. 220.02(8), F.S.)_

## 10. No Franchise Tax / No Separate Privilege Tax

**Non-usable hold:** Complete all-industry/local-tax absence claims, other-state comparisons and annual-report fees/deadlines below are unverified. The ordinary income-tax computation does not establish a complete tax/fee clearance.

- **No additional entity taxes** — Florida does NOT impose: A general corporate franchise tax (separate from the income tax). A net worth tax. A privilege tax for the privilege of doing business as a corporation. A "minimum" corporate income tax (Florida's tax is purely income-based — if Florida apportioned income is below $50,000, no tax is due). A gross receipts tax on corporations. A capital stock tax. The Florida corporate income tax IS labeled as the "corporate income/franchise tax" in s. 220.11, F.S., but functionally it is an income tax. There is no separate franchise component.  _(s. 220.11, F.S.)_

This contrasts with, for example, Texas (franchise tax / margin tax separate from federal income tax), Delaware (annual franchise tax based on authorized shares plus a separate corporate income tax), and California ($800 minimum franchise tax plus 8.84% corporate income tax).

The only annual maintenance fee paid to the state for a Florida corporation is the annual report fee to the Florida Department of State, Division of Corporations ($150 for for-profit corporations, $138.75 for LLCs). This is filed via Sunbiz.org by May 1 each year. It is NOT a tax — it is a corporate maintenance fee and is not addressed by this skill.

## 11. Documentary Stamp Tax — Refer Out

**Non-usable hold:** Chapter 201 operative exceptions, caps and the quoted documentary-stamp amounts/forms have not been confirmed. This retained topic is unavailable for reliance; refer for a primary-source check.

Florida documentary stamp tax (Ch. 201, F.S.) is a separate tax on:

- Deeds and other instruments transferring interests in Florida real estate (70 cents per $100 of consideration, except 60 cents per $100 in Miami-Dade County for single-family residences; surtax of 45 cents per $100 in Miami-Dade for other deeds).
- Promissory notes and other written obligations to pay money (35 cents per $100 of face value).
- Mortgages, deeds of trust, security agreements (35 cents per $100 of indebtedness).

Doc stamp is collected at the county recorder's office (for real estate) or paid via Form DR-225 (for notes not recorded). It is NOT a corporate income tax matter and is outside the scope of this skill. Refer the client to a Florida real estate attorney or title agent.

## 12. Common Errors

### 12.1 Treating a disregarded SMLLC as subject to Florida CIT

This is by far the most frequent error among out-of-state preparers and software-driven services. A Florida single-member LLC that has NOT elected to be taxed as a corporation:

- Files no separate federal return of its own; income/expense is reported by its owner on the appropriate return, including a corporate owner where applicable.
- Files no separate F-1120 solely as a disregarded LLC.
- May have income included in an owner's F-1120; the natural-person owner's ordinary income-tax result is different.

**Non-usable hold:** The list is not a complete other-tax/fee clearance; the annual-report deadline has not been confirmed.

The LLC's only Florida obligations are:
- Annual report with the FL Division of Corporations (Sunbiz) by May 1.
- Sales tax registration if making taxable sales (separate analysis).
- Reemployment tax if employer (separate analysis).

Before answering, determine federal classification and who owns the LLC. A corporate owner may need F-1120 even though the LLC has no separate return; Form 8832 is not the sole filing gateway. [Source](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx).

### 12.2 Filing F-1120 for an S-corp with pure pass-through income

An S-corp with only ordinary pass-through income (federal Form 1120-S, no built-in gains, no LIFO recapture, no §1375 tax) is NOT required to file Florida F-1120 because it has zero federal taxable income at the entity level. Some preparers reflexively file a zero-tax F-1120; this is unnecessary and clogs the DOR's records. Do not file unless required.

### 12.3 Using market-based sourcing for services

**Non-usable hold:** The categorical multistate sourcing and other-state comparison is not established; read the actual operative rule/judgments before use.

Florida uses COST-OF-PERFORMANCE sourcing. A preparer trained on California, New York, or Massachusetts (all market-based) will instinctively source receipts to the customer location. This produces a wrong Florida apportionment. Always read s. 220.15(5)(b), F.S. and Rule 12C-1.0155, F.A.C., and source based on where the income-producing activity is performed.

### 12.4 Using single-sales-factor apportionment

For the ordinary method with all three factors present, use (P + Pa + 2S) / 4. Reweight zero/insignificant factors and apply required special-industry methods as explained in §5.1. The comparative all-state population claim is unverified.

### 12.5 Treating the $50,000 exemption as a credit

The $50,000 is a deduction from Florida net income, not a credit against tax. It saves 5.5% × $50,000 = $2,750 of Florida tax for a profitable corporation, not $50,000.

### 12.6 Forgetting to add back the federal NOL

Add back the federal NOL on Schedule I line 3, then apply the Florida carryforward separately: Schedule II line 3 for entirely Florida businesses or Schedule IV line 4 for multistate businesses. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

### 12.7 Forgetting the Florida bonus depreciation addback

For a covered ordinary bonus addition, add the qualifying amount and recover one-seventh beginning in the same year, then for six subsequent years. QIP has separate pre-CARES-based recovery. Current TIP 26C01-01 has additional pro forma/decoupling requirements; full application to a specific 2025 return remains held. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.13). [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

### 12.8 Missing the F-7004 tentative-tax payment

A Florida extension requires timely F-7004 and tentative payment. Apply the statutory material-understatement test in §7.3; do not equate every final shortfall with an invalid extension. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.222).

### 12.9 Using the wrong rate for 2020 or 2021 amended returns

For years beginning in 2020 use 4.458%; for years beginning in 2021 use 3.535%; for 2022–2025 the ordinary rate is 5.5%. [Source](https://floridarevenue.com/taxes/tips/Documents/TIP_21C01-02.pdf).

### 12.10 Filing F-1120 instead of F-1120A

- **F-1120A eligibility criteria**: the official short form permits Florida net income of $45,000 or less and 100% Florida business. Its modifications are limited to NOL and state-income-tax items; federal NOL deduction is added on line 2 and Florida NOL deducted on line 3. The corporation cannot be included in a consolidated return. Tentative/estimated-payment credits are permitted. Apply all official form criteria; extra blanket controlled-group/HOA/AMT exclusions remain unconfirmed. Complete both sides of the return; the official form/instruction package has four pages, not a one-page return. [Source](https://floridarevenue.com/Forms_library/current/f1120a.pdf).

### 12.11 Confusing "doing business in Florida" with "incorporated in Florida"

Corporate filing can arise from doing business, earning income or existing in Florida. The Delaware/Florida operating example requires filing on its facts; do not conclude a Florida corporation with Texas operations has no filing obligation merely because it has no Florida office. [Source](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx).

### 13.1 Example 1 — Florida-only C-corp software development company

**Facts.** SunCode Inc., a Florida C-corporation, develops custom software for clients nationwide from its sole office in Tampa. All employees (10 W-2 developers, 1 owner-CEO) work from the Tampa office. All R&D, project management, and customer support is performed in Florida. Customers are located in 35 states; about 12% of revenue comes from Florida customers, 88% from out-of-state customers.

For tax year 2025:
- Federal taxable income (Form 1120 Line 30): $480,000
- Federal NOL deduction included: $0
- Federal bonus depreciation claimed: $30,000 (new server equipment placed in service in 2025)
- Florida bonus depreciation addback for prior years: $5,000 (1/7 of prior addbacks reversing)

**Step 1 — Federal taxable income.** $480,000.

**Step 2 — Florida additions.** Add back federal bonus depreciation: +$30,000.

**Step 3: Florida subtractions.** Retain the $5,000 prior recovery and include current ordinary-bonus recovery of $30,000 / 7 = $4,285.714286, conditional on the supplied addition being valid and the applicable asset/pro forma rules. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.13).

**Step 4: Adjusted federal income.** $480,000 + $30,000 - $5,000 - $4,285.714286 = $500,714.285714 (conditional).

**Step 5 — Apportionment.**

*Property factor.* All property is in Tampa. Numerator = $50,000 average cost. Denominator = $50,000. Property factor = 100%.

*Payroll factor.* All employees in Tampa. Numerator = $1,200,000. Denominator = $1,200,000. Payroll factor = 100%.

*Sales factor.* All services performed in Florida. Under cost-of-performance, 100% of service receipts are sourced to Florida — even though 88% of customers are out of state. Numerator = $3,500,000. Denominator = $3,500,000. Sales factor = 100%.

*Apportionment %.* (100% + 100% + 2 × 100%) / 4 = 400% / 4 = 100%.

**Step 6: Florida apportioned income.** $500,714.285714 × 100% = $500,714.285714 (conditional).

**Step 7: $50,000 exemption.** $500,714.285714 - $50,000 = $450,714.285714, assuming the full exemption is available.

**Step 8: Florida tax at 5.5%.** $450,714.285714 × 5.5% = **$24,789.29**, ordinarily $24,789 whole-dollar, conditional on the stated base and asset assumptions.

**Step 9: Estimated payments.** Expected 2025 tax exceeding $2,500 could already require estimates in 2025. The 2026 obligation depends on expected 2026 tax and applicable exceptions; this conditional 2025 result alone does not decide it. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

**Filing.** Form F-1120 due May 1, 2026 (calendar year 2025).

**Commentary.** Despite serving customers in 35 states, SunCode is 100% Florida-apportioned because Florida uses cost-of-performance and all the work is done in Tampa. If the same company were headquartered in California (market-based sourcing), only 12% of receipts would be California-sourced. This is the **cost-of-performance trap** for Florida service businesses serving national customers — it concentrates tax in Florida.

```oa-check
name: Conditional SunCode ordinary bonus recovery
inputs:
  federal_income: 480000
  current_addition: 30000
  prior_recovery: 5000
  exemption: 50000
steps:
  current_recovery: current_addition / 7
  adjusted_income: federal_income + current_addition - prior_recovery - current_recovery
  base: adjusted_income - exemption
  tax: base * 0.055
expected:
  current_recovery: 4285.714286
  adjusted_income: 500714.285714
  tax: 24789.285714
```

### 13.2 Example 2 — Out-of-state C-corp with Florida customers but no Florida operations

**Non-usable hold:** Nexus, SaaS/IP classification and current sourcing authority are unresolved for this case. All no-return/zero-tax conclusions below are unavailable for reliance.

**Facts.** TechFlow Inc., a Delaware C-corporation headquartered in Boston, Massachusetts, provides cloud-based SaaS to customers nationwide. All servers, employees, and operations are in Massachusetts. Florida customers generate $800,000 of annual revenue out of $10,000,000 total revenue. TechFlow has no Florida employees, no Florida property, and no Florida office.

For tax year 2025:
- Federal taxable income: $2,000,000.

**Nexus analysis.** TechFlow has no physical presence in Florida. Florida has not enacted a bright-line economic nexus statute for corporate income tax (unlike for sales tax). Whether TechFlow has Florida CIT nexus depends on the specific facts and constitutional limits. Conservative position: if TechFlow has substantial Florida customers, P.L. 86-272 might not protect it because P.L. 86-272 only protects solicitation of orders for **tangible personal property**, not services or SaaS. However, without physical presence, the case for Florida nexus is weak.

**Non-usable hold:** No filing decision is established by the supplied facts and incomplete current-law reading.

**Decision.** TechFlow likely has no Florida CIT filing obligation. **No F-1120 filed.**

**Non-usable hold:** The remote-employee example does not establish every constitutional/nexus condition.

**Counterfactual.** If TechFlow had a single Florida employee (a remote sales rep), nexus would clearly exist, and TechFlow would file F-1120.

*If TechFlow were subject to Florida CIT:*

*Sales factor (cost-of-performance).* All service activity is performed in Massachusetts. Florida sales numerator = $0 (none of the income-producing activity is in Florida). Florida sales factor = 0%.

*Property factor.* 0% (no Florida property).
*Payroll factor.* 0% (no Florida payroll).
*Apportionment %.* (0 + 0 + 2 × 0) / 4 = 0%.

*Florida apportioned income.* $2,000,000 × 0% = $0.
*Florida tax.* $0.

**Non-usable hold:** Zero ordinary-factor arithmetic does not establish a zero tax liability under the applicable sourcing law.

Even if a return is filed defensively, the tax would be $0. This is the inverse of Example 1 — under cost-of-performance, out-of-state service providers with Florida customers owe nothing.

**Commentary.** Florida's cost-of-performance sourcing rewards out-of-state service providers and disadvantages in-state ones, relative to a market-based regime. Tax planners with mobility have, over the years, used this asymmetry to locate service operations outside Florida while serving Florida customers — but the corollary is that in-state C-corps face high Florida concentration.

```oa-check
name: TechFlow assumed zero factors only; nexus and sourcing held
inputs:
  federal_income: 2000000
  property: 0
  payroll: 0
  sales: 0
steps:
  factor: (property + payroll + 2 * sales) / 4
  apportioned: federal_income * factor
expected:
  factor: 0
  apportioned: 0
```

### 13.3 Example 3 — Florida SMLLC with no C-corp election

**Non-usable hold:** The original federal income-tax estimate, sales-tax classification, annual-report amount and comparisons are unverified. Ordinary Florida personal/corporate income-tax zero does not clear all taxes/fees.

**Facts.** Maria Santos operates "Coral Reef Consulting LLC," a Florida single-member LLC formed in 2023. The LLC has not filed Form 8832 to elect corporate treatment. Maria is the sole owner and reports all LLC income on her Schedule C. For 2025:

- Schedule C net profit: $145,000.
- Self-employment tax (Schedule SE): conditional on this being the sole SE income and no Social Security wages, $145,000 × 92.35% × (12.4% + 2.9%) = $20,487.8475, ordinarily $20,488 whole-dollar.
- The original $24,300 federal income-tax estimate is unverified. Adding the conditional SE figure gives $44,787.8475 (about $44,788), not a validated total: half-SE deduction, QBI and all other federal facts still need computation.

**Florida obligations.**

- **Florida corporate income tax.** None. The LLC is disregarded and Maria is a natural person. No F-1120 filed.
- **Florida personal income tax.** None. Florida has no personal income tax (Art. VII, s. 5, Fla. Const.).
- **Florida self-employment tax.** None. Florida does not piggyback on federal SE tax.
- **Florida sales tax.** Required only if Maria provides taxable services or sells tangible personal property in Florida. Most consulting services are not taxable in Florida. Verify per Ch. 212, F.S.
- **Florida annual report.** $138.75 to Sunbiz by May 1, 2026, to keep the LLC active. Not a tax.

**Non-usable hold:** Only the ordinary personal/corporate income-tax conclusion is supported; the all-tax total is not established.

**Total Florida state-level tax burden: $0.**

**Non-usable hold:** Other-state comparison amounts, annual-report fee and complete other-tax clearance are unverified.

**Commentary.** This is why Florida is so attractive to freelancers and single-member LLC owners. A New York or California freelancer with the same $145,000 federal income pays an additional ~$8,500–$12,000 in state income tax. The Florida equivalent pays only the $138.75 annual report fee.

This is also why Florida is the **wrong place** to consider an S-corp election purely for state tax savings — there are no state-level SE tax savings to capture (because there's no state SE tax to begin with). Federal SE tax savings still motivate the S-corp election for high-earning Florida sole proprietors, but the analysis is purely federal. See the `us-s-corp-election-decision` skill.

```oa-check
name: Conditional sole Schedule C income; no Social Security wages
inputs:
  schedule_c_profit: 145000
  held_income_tax_estimate: 24300
steps:
  net_earnings: schedule_c_profit * 0.9235
  social_security: net_earnings * 0.124
  medicare: net_earnings * 0.029
  se_tax: social_security + medicare
  unverified_combined_estimate: held_income_tax_estimate + se_tax
expected:
  net_earnings: 133907.50
  social_security: 16604.53
  medicare: 3883.3175
  se_tax: 20487.8475
  unverified_combined_estimate: 44787.8475
```

### 13.4 Example 4 — Florida C-corp claiming Florida Tax Credit Scholarship credit

**Facts.** Atlantic Manufacturing Inc., a Florida C-corp, projects a 2025 Florida tax liability of $40,000. The CEO wants to redirect tax dollars to Step Up For Students (an approved SFO) to fund private school scholarships for low-income students.

**Steps.**

1. **Pre-approval.** Atlantic submits the **Application for Credit Allocation** through the FL DOR e-services portal in early 2025. The DOR allocates a credit reservation up to the total annual statewide cap.
2. **Contribution.** Atlantic contributes $40,000 to Step Up For Students within the allocation period.
3. **Documentation.** Step Up For Students issues a receipt to Atlantic. Atlantic also retains the DOR allocation letter.
4. **F-1120 filing.** On Form F-1120 for 2025:
   - Gross Florida tax: $40,000.
   - Initial contribution-based measure: $40,000 before statutory federal-benefit reduction and state addback.
   - Final allowable credit and net Florida tax: **not determined**; recompute the adjusted base, tax benefit and other-credit ordering. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.1875). [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.13).
5. **Federal treatment.** Notice 2019-12 concerns certain individuals under section 164. The corporate safe harbor is Rev. Proc. 2019-12 section 3 under section 162; determine its actual conditions and the state-credit interaction. The general 2025 individual SALT limit is $40,000/$20,000 MFS with phaseout under enacted P.L. 119-21; the original $10,000 aside is not the general 2025 rule. This does not establish a deduction or a final corporate amount. [Source](https://www.irs.gov/pub/irs-drop/n-19-12.pdf). [Source](https://www.irs.gov/pub/irs-drop/rp-2019-12.pdf). [Source](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

**Net effect.** Preserve the stipulated $40,000 contribution and projected tax. $40,000 - $40,000 = $0 is arithmetic only; the statutory federal-benefit reduction and state addback prevent assuming the final credit, tax or net cost. No automatic 21% counter-result is supplied. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.1875).

**Non-usable hold:** Popularity, client-range and cost-free redirection claims are unverified; final credit/tax must reflect the statutory interactions.

**Commentary.** This credit is the most popular Florida corporate income tax credit because it is a true dollar-for-dollar tax-to-contribution redirection. It works particularly well for C-corps that would otherwise have a Florida tax liability between $10,000 and $500,000.

```oa-check
name: Atlantic original gross subtraction only; final credit and tax held
inputs:
  projected_tax: 40000
  gross_contribution: 40000
steps:
  original_gross_subtraction: projected_tax - gross_contribution
expected:
  original_gross_subtraction: 0
```

### 13.5 Example 5 — Multistate apportionment with mixed property and sales

**Facts.** GulfCoast Logistics Inc., a Florida C-corp, operates trucking and warehousing services in Florida, Georgia, and Alabama. For 2025:

- Federal taxable income: $1,200,000.
- Property: $2,000,000 Florida, $500,000 Georgia, $300,000 Alabama. Total: $2,800,000.
- Payroll: $4,000,000 Florida, $800,000 Georgia, $600,000 Alabama. Total: $5,400,000.
- Sales (services performed in each state — sourced under cost-of-performance):
  - Services originating from Florida warehouse: $6,000,000 → 100% Florida-sourced.
  - Services originating from Georgia: $1,500,000 → 0% Florida-sourced.
  - Services originating from Alabama: $700,000 → 0% Florida-sourced.
  - Total: $8,200,000.

**Apportionment.**

*Property factor.* $2,000,000 / $2,800,000 = 71.43%.
*Payroll factor.* $4,000,000 / $5,400,000 = 74.07%.
*Sales factor (cost-of-performance).* $6,000,000 / $8,200,000 = 73.17%.

**Non-usable hold:** Transportation activities require the section 220.151 revenue-mile method; it is not optional simply for illustration. Activity splits/miles are absent. The ordinary-factor computation below is a conditional arithmetic illustration, not GulfCoast's cleared filing method. [Source](https://www.flsenate.gov/Laws/Statutes/2025/220.151).

*Apportionment percentage.* Under the F-1120 six-decimal ratio/weighted-factor method, rounded property weight is 0.178572, payroll 0.185185 and sales 0.365854, totaling **0.729611**. Premature rounding to 72.96% gives a different intermediate base. [Source](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

**Florida apportioned income.** $1,200,000 × 0.729611 = $875,533.20 (conditional ordinary-factor illustration).

**$50,000 exemption.** $875,533.20 - $50,000 = $825,533.20, assuming the full exemption is available.

**Florida tax at 5.5%.** $825,533.20 × 5.5% = $45,404.326, or **$45,404** whole-dollar, as in the original final amount. This does not settle the transportation method.

**Commentary.** The double-weighting of sales means the sales factor effectively determines ~50% of the apportionment. Because Florida uses cost-of-performance, the $6M of services originating from Florida warehouse all source to Florida. If Florida used market-based sourcing, the answer might be quite different depending on customer locations.

**Non-usable hold:** Actual Georgia/Alabama filing obligations and total state tax require separate authorities and facts.

The corporation would also file Georgia and Alabama corporate income tax returns. Total state tax across the three states is unlikely to sum to 100% because each state uses its own apportionment formula — possible double tax or apportionment gaps.

```oa-check
name: GulfCoast conditional ordinary factors; transportation method held
inputs:
  income: 1200000
  property_fl: 2000000
  property_all: 2800000
  payroll_fl: 4000000
  payroll_all: 5400000
  sales_fl: 6000000
  sales_all: 8200000
  exemption: 50000
steps:
  property_ratio: round(property_fl / property_all, 6)
  payroll_ratio: round(payroll_fl / payroll_all, 6)
  sales_ratio: round(sales_fl / sales_all, 6)
  property_weight: round(property_ratio * 0.25, 6)
  payroll_weight: round(payroll_ratio * 0.25, 6)
  sales_weight: round(sales_ratio * 0.5, 6)
  factor: property_weight + payroll_weight + sales_weight
  apportioned: income * factor
  base: apportioned - exemption
  tax: base * 0.055
expected:
  property_weight: 0.178572
  payroll_weight: 0.185185
  sales_weight: 0.365854
  factor: 0.729611
  apportioned: 875533.20
  tax: 45404.326
```

## 14. Self-Checks

Before signing off on an F-1120:

1. [ ] Confirm entity is a C-corp (or an LLC electing C-corp treatment, or an S-corp with federally-taxed items).
2. [ ] Confirm Florida nexus.
3. [ ] Start with Form 1120 Line 30 (federal taxable income).
4. [ ] Add back federal NOL deduction.
5. [ ] Apply the correct bonus/QIP windows and pro forma requirements; ordinary one-seventh recovery starts in the addition year.
6. [ ] Apply ordinary/reweighted or required special-industry apportionment; use the form's six-decimal rounding.
7. [ ] Confirm the operative service/SaaS/intangible rule and current judicial application; the held categorical statements are not a sourcing decision.
8. [ ] Apply the available $50,000 exemption (short-period proration, consolidated and separately filing controlled-group sharing).
9. [ ] Use the rate for the tax year: 2020 4.458%, 2021 3.535%, 2022–2025 ordinary 5.5%.
10. [ ] Verify all credits have pre-approval and contemporaneous documentation.
11. [ ] Confirm the ordinary/later-federal due date and June 30 year-end exception; calendar-2025 ordinarily May 1, 2026.
12. [ ] Confirm F-7004 extension paid with tentative tax (if extending).
13. [ ] Confirm estimated payments made if Florida tax > $2,500.
14. [ ] Test $5,000 paid in the preceding state fiscal year and the separate federal mandatory-e-filing gateway.

## 15. Provenance and Citations

- **s. 220.03, F.S.** — Definitions (including federal IRC conformity date).  _(s. 220.03, F.S.)_
- **Tax imposed; 5.5% rate** — 5.5%  _(s. 220.11, F.S.)_
- **Tax Refund and Rate Reduction Mechanism** — TRIM Act; historical 2018–2021.  _(s. 220.1105, F.S.)_
- **Adjusted federal income (additions and subtractions); Florida NOL** — Adjusted federal income (additions and subtractions); Florida NOL.  _(s. 220.13, F.S.)_
- **Consolidated returns** — Consolidated returns.  _(s. 220.131, F.S.)_
- **$50,000 exemption** — $50,000 USD (Exemption from Florida net income before applying the 5.5% rate; a true deduction from the tax base, not a credit.)  _(s. 220.14, F.S.)_
- **Three-factor apportionment with double-weighted sales; cost-of-performance sourcing for services** — Three-factor apportionment with double-weighted sales; cost-of-performance sourcing for services.  _(s. 220.15, F.S.)_
- **Special apportionment for transportation services** — Special apportionment for transportation services.  _(s. 220.151, F.S.)_
- **Petition for alternative apportionment** — Petition for alternative apportionment.  _(s. 220.152, F.S.)_
**Non-usable hold:** Actual business/nonbusiness character and complete royalty sourcing require confirmation; no actual holding-company income is classified.

- **Allocation of nonbusiness income** — Allocation of nonbusiness income.  _(s. 220.16, F.S.)_
- **Community Contribution Tax Credit** — Community Contribution Tax Credit.  _(s. 220.183, F.S.)_
- **Voluntary Cleanup Tax Credit** — Voluntary Cleanup Tax Credit.  ([section 220.1845](https://www.flsenate.gov/Laws/Statutes/2025/220.1845))
- **Hazardous Waste Facility Credit**: [section 220.184](https://www.flsenate.gov/Laws/Statutes/2025/220.184).
- **New Markets Tax Credit** — New Markets Tax Credit.  _(s. 220.185, F.S.)_
- **Florida Tax Credit Scholarship Program** — Florida Tax Credit Scholarship Program.  _(s. 220.1875, F.S.)_
- **Strong Families Tax Credit** — Strong Families Tax Credit.  _(s. 220.1876, F.S.)_
**Non-usable hold:** Current agency, project certification, jobs/wages and application facts remain unverified; headline measure/tier corrections do not establish eligibility.

- **Capital Investment Tax Credit** — Capital Investment Tax Credit.  _(s. 220.191, F.S.)_
- **Research and Development Tax Credit** — Research and Development Tax Credit.  _(s. 220.196, F.S.)_
- **Experiential Learning Tax Credit (Internship Tax Credit)** — Experiential Learning Tax Credit (Internship Tax Credit).  _(s. 220.198, F.S.)_
- **Returns; due dates** — Returns; due dates.  _(s. 220.222, F.S.)_
- **Declaration of estimated tax; quarterly payments** — Declaration of estimated tax; quarterly payments.  _(s. 220.33 and 220.34, F.S.)_
- **Bank and savings association franchise tax** — Bank and savings association franchise tax.  _(s. 220.63, F.S.)_
- **Penalties** — Penalties.  _(s. 220.803, F.S.)_
- **Adjusted federal income (F.A.C.)** — Adjusted federal income.  _(Rule 12C-1.013, F.A.C.)_
- **Apportionment; sales factor; cost-of-performance** — Apportionment; sales factor; cost-of-performance.  _(Rule 12C-1.0155, F.A.C.)_
- **Property factor (F.A.C.)** — Property factor.  _(Rule 12C-1.0151, F.A.C.)_
- **Payroll factor (F.A.C.)** — Payroll factor.  _(Rule 12C-1.0152, F.A.C.)_
- **Prohibition on personal income tax on natural persons** — Prohibition on personal income tax on natural persons.  _(Art. VII, s. 5, Fla. Const.)_
- **Corporate income tax authorization** — Corporate income tax authorization.  ([Article VII, section 5](https://www.flsenate.gov/Laws/Constitution)); section 6 concerns homestead exemptions.
- **Form F-1120** — Florida Corporate Income/Franchise Tax Return.  _(FL DOR Forms (2025))_
- **Form F-1120A** — short form.  _(FL DOR Forms (2025))_
- **Form F-1120ES** — estimated tax voucher.  _(FL DOR Forms (2025))_
- **Form F-7004** — extension.  _(FL DOR Forms (2025))_
- **Form F-2220** — underpayment of estimated tax.  _(FL DOR Forms (2025))_
- **Form F-1065** — partnership information return — corporate partners only.  _(FL DOR Forms (2025))_
- **TIP 22C01-02** — rate restored to 5.5% for 2022.  _(TIP 22C01-02)_
- **TIP 22C01-01** — 2021 rate retroactively reduced to 3.535%.  _(TIP 22C01-01)_
- **TIP 21C01-01** — 2020 rate 3.535%.  _(TIP 21C01-01)_
- **TIP 20C01-01 and TIP 19C01-04** — 2019 and 2018 rates 4.458%.  _(TIP 20C01-01 and TIP 19C01-04)_
- **Net operating losses (Florida-mirrored post-2017)** — Net operating losses (Florida-mirrored post-2017).  _(IRC §172)_
- **Bonus depreciation (Florida decoupled)** — Bonus depreciation (Florida decoupled).  _(IRC §168(k))_
- **Section 179 expensing (Florida partial decoupling)** — Section 179 expensing (Florida partial decoupling).  _(IRC §179)_
- **Ownership change NOL limit (Florida conforms)** — Ownership change NOL limit (Florida conforms).  _(IRC §382)_
- **GILTI (Florida partial subtraction)** — GILTI (Florida partial subtraction).  _(IRC §951A)_
- **Transition tax (Florida addback, historical)** — Transition tax (Florida addback, historical).  _(IRC §965)_
- **Built-in gains tax (S-corp)** — Built-in gains tax (S-corp).  _(IRC §1374)_
- **Excess net passive income tax (S-corp)** — Excess net passive income tax (S-corp).  _(IRC §1375)_
- **Federal R&D credit (referenced by FL §220.196)** — Federal R&D credit (referenced by FL §220.196).  _(IRC §41)_
- **Charitable contribution / state tax credit interaction** — Charitable contribution / state tax credit interaction.  _(IRC §170 / Treas. Reg. §1.170A-1(h)(3))_
- **Safe harbor for state tax credit contributions** — Safe harbor for state tax credit contributions.  ([Rev. Proc. 2019-12, section 3](https://www.irs.gov/pub/irs-drop/rp-2019-12.pdf)); Notice 2019-12 concerns certain individuals under section 164.
- **Federal interstate commerce protection** — Federal interstate commerce protection (tangible personal property only; does not protect SaaS or services).  _(P.L. 86-272)_
- **us-tax-workflow-base** — workflow architecture, required base.  _(Companion skills)_
- **us-sole-prop-bookkeeping** — Schedule C classification (federal); does not make Schedule C universal or eliminate a corporate owner's F-1120 obligation.  _(Companion skills)_
- **us-federal-return-assembly** — federal 1040 / 1120 assembly.  _(Companion skills)_
- **us-s-corp-election-decision** — relevant for Florida sole proprietors considering S-corp election (federal-only analysis since FL has no SE tax).  _(Companion skills)_
- **florida-sales-and-use-tax (separate skill)** — Ch. 212, F.S. obligations for taxable sales.  _(Companion skills)_

Version 1.1 correction draft, pending independent source review and approval by the approving accountant. Maintained 2026-11-25; bounded source-read dates and unresolved operative conditions are recorded below.


## Sources

These bounded source reads were completed on 22 November 2026. The maintenance date records the correction, not fresh reads or approval. Tax-year 2025 coverage and the stated application limits are retained.

| Authority | Actual read scope and short source wording | Read on |
| --- | --- | --- |
| [DOR corporate tax](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx) | Read in the linked authority (bounded scope): Entity gateways, owner reporting, rates and ordinary tax-base/apportionment passages read. Short exact excerpt: “even if the only activity of the corporation is ownership”. | 2026-11-22 |
| [2025 F-1120 instructions, R.01/26](https://floridarevenue.com/Forms_library/current/f1120n.pdf) | Read in the linked authority (bounded scope): Bounded entity, filing, estimates, penalty, NOL, starting line, tax addback, foreign income, depreciation, ordinary factors and transportation passages read. Not all seventeen pages. Short exact excerpt: “beginning with the tax year of the addition”. | 2026-11-22 |
| [2025 F.S.220.13](https://www.flsenate.gov/Laws/Statutes/2025/220.13) | Read in the linked authority (bounded scope): Additions, foreign subtractions, NOL, bonus/179 windows and AMT definition passages read; not every modification. Short exact excerpt: “For the taxable year and for each of the 6 subsequent taxable years”. | 2026-11-22 |
| [2025 F.S.220.14](https://www.flsenate.gov/Laws/Statutes/2025/220.14) | Read in the linked authority (bounded scope): All operative exemption subsections1–4 read. Short exact excerpt: “not more than one exemption”. | 2026-11-22 |
| [2025 F.S.220.15](https://www.flsenate.gov/Laws/Statutes/2025/220.15) | Read in the linked authority (bounded scope): Ordinary factors, reweighting, property/rent, payroll cascade, tangible sales and financial-organization passages read; not full service rule/judgments. Short exact excerpt: “representing 50 percent”. | 2026-11-22 |
| [2025 F.S.220.16](https://www.flsenate.gov/Laws/Statutes/2025/220.16) | Read in the linked authority (bounded scope): Operative real/tangible/intangible gains, rent, dividends/interest and royalty allocation read. Short exact excerpt: “Capital gains and losses from sales of real property”. | 2026-11-22 |
| [2025 F.S.220.803](https://www.flsenate.gov/Laws/Statutes/2025/220.803) | Read in the linked authority (bounded scope): Operative negligence/fraud and deficiency provisions read. Short exact excerpt: “10 percent of the deficiency”. | 2026-11-22 |
| [2025 F.S.220.34](https://www.flsenate.gov/Laws/Statutes/2025/220.34) | Read in the linked authority (bounded scope): Underpayment, safe harbors and penalty/interest passages read; floating-interest interaction also checked against B25. Short exact excerpt: “rates applicable to the taxable year”. | 2026-11-22 |
| [2025 F.S.220.03](https://www.flsenate.gov/Laws/Statutes/2025/220.03) | Read in the linked authority (bounded scope): Specified federal adoption date and future-amendment mechanism read; not entire definitions. Short exact excerpt: “January 1, 2025”. | 2026-11-22 |
| [2025 F.S.220.11](https://www.flsenate.gov/Laws/Statutes/2025/220.11) | Read in the linked authority (bounded scope): Ordinary and alternative imposition subsections read. Short exact excerpt: “5 1/2 percent”. | 2026-11-22 |
| [2025 F.S.220.1875](https://www.flsenate.gov/Laws/Statutes/2025/220.1875) | Read in the linked authority (bounded scope): Eligible scholarship credit, federal-benefit reduction, ordering and extension compliance read. Short exact excerpt: “shall be reduced by the difference”. | 2026-11-22 |
| [2025 F.S.220.196](https://www.flsenate.gov/Laws/Statutes/2025/220.196) | Read in the linked authority (bounded scope): Four-year base,10%,50%limit, startup reduction, industries, allocation window/cap/proration and carryforward read. Short exact excerpt: “allocated on a prorated basis”. | 2026-11-22 |
| [TIP26C01-01](https://floridarevenue.com/taxes/tips/Documents/TIP_26C01-01.pdf) | Read in the linked authority (bounded scope): Current July2026 adoption/decoupling, pro forma, amendment, bonus/QIP and wage-credit passages read. Full session-law application still held. Short exact excerpt: “recompute its federal taxable income”. | 2026-11-22 |
| [2026 F.S.220.03](https://www.flsenate.gov/Laws/Statutes/2026/220.03) | Read in the linked authority (bounded scope): Current specified adoption date and exception cross-reference read; not whole 2026 law. Short exact excerpt: “except as provided in paragraph (1)(n)”. | 2026-11-22 |
| [IRS Notice2019-12](https://www.irs.gov/pub/irs-drop/n-19-12.pdf) | Read in the linked authority (bounded scope): Purpose, individual gateway and distinction from corporate procedure read; not a new corporate filing opinion. Short exact excerpt: “for certain individuals”. | 2026-11-22 |
| [IRS Rev.Proc.2019-12](https://www.irs.gov/pub/irs-drop/rp-2019-12.pdf) | Read in the linked authority (bounded scope): Purpose and section3 corporate safe harbor/examples read. Guessed shortened filename404; full official filename succeeded. Current final regulation not fully read. Short exact excerpt: “ordinary and necessary business expense”. | 2026-11-22 |
| [2025 F.S.220.191](https://www.flsenate.gov/Laws/Statutes/2025/220.191) | Read in the linked authority (bounded scope): General5%capital-cost measure,20year period,25/50/100million tiers and special project limits read; full certifications held. Short exact excerpt: “5 percent of the eligible capital costs”. | 2026-11-22 |
| [2025 F.S.220.184](https://www.flsenate.gov/Laws/Statutes/2025/220.184) | Read in the linked authority (bounded scope): Hazardous waste facility title and operative credit subsections read, establishing swapped citation. Short exact excerpt: “Hazardous waste facility tax credit”. | 2026-11-22 |
| [2025 F.S.220.1845](https://www.flsenate.gov/Laws/Statutes/2025/220.1845) | Read in the linked authority (bounded scope): Rehabilitation title, ordinary50%/$500k, eligibility and carryforward passages read; not every transfer/bonus provision. Short exact excerpt: “Contaminated site rehabilitation tax credit”. | 2026-11-22 |
| [2025 F.S.220.151](https://www.flsenate.gov/Laws/Statutes/2025/220.151) | Read in the linked authority (bounded scope): Transportation subsection2 revenue miles and activity-specific rule read; no actual mile allocation. Short exact excerpt: “taxpayer furnishing transportation services”. | 2026-11-22 |
| [Florida Constitution ArticleVII](https://www.flsenate.gov/Laws/Constitution) | Read in the linked authority (bounded scope): Section5(a)/(b) and section6 heading read. Section6 is homestead, not the claimed corporate-tax authorization. Entire Constitution not read. Short exact excerpt: “Estate, inheritance and income taxes”. | 2026-11-22 |
| [2025 F.S.220.222](https://www.flsenate.gov/Laws/Statutes/2025/220.222) | Read in the linked authority (bounded scope): Filing dates,June30 branch, extensions, material-underpayment and special-credit conditions read. Short exact excerpt: “more than the greater of $2,000 or 30 percent”. | 2026-11-22 |
| [2025 F.S.220.33](https://www.flsenate.gov/Laws/Statutes/2025/220.33) | Read in the linked authority (bounded scope): Four/later-start installments and last-June-weekend acceleration read. Short exact excerpt: “before the 1st day of the next taxable year”. | 2026-11-22 |
| [2025 F.S.220.32](https://www.flsenate.gov/Laws/Statutes/2025/220.32) | Read in the linked authority (bounded scope): Tentative estimate/payment and12%annual penalty read. Short exact excerpt: “12 percent per year”. | 2026-11-22 |
| [2025 F.S.220.807](https://www.flsenate.gov/Laws/Statutes/2025/220.807) | Read in the linked authority (bounded scope): Floating interest adjustment and12%ceiling read. Short exact excerpt: “shall never be greater than 12 percent”. | 2026-11-22 |
| [DOR scholarship program](https://floridarevenue.com/taxes/taxesfees/Pages/sfo_taxes.aspx) | Read in the linked authority (bounded scope): Corporate reduction/addback, timing, transfer and ten-year unused-credit passages read. Short exact excerpt: “cannot be carried forward more than 10 years”. | 2026-11-22 |
| [DEP voluntary cleanup](https://floridadep.gov/waste/waste-cleanup/content/voluntary-cleanup-tax-credit) | Read in the linked authority (bounded scope): Current authority,35million authorization,50%/$500k and eligibility passages read. Current2026deadline not silently used for2025. Short exact excerpt: “annual $35 million authorization”. | 2026-11-22 |
| [2025 F.S.376.30781](https://www.flsenate.gov/Laws/Statutes/2025/376.30781) | Read in the linked authority (bounded scope): Credit/bonuses,35million statutory annual cap and application passages read; not all program conditions. Short exact excerpt: “$35 million in tax credits each fiscal year”. | 2026-11-22 |
| [TIP21C01-02](https://floridarevenue.com/taxes/tips/Documents/TIP_21C01-02.pdf) | Read in the linked authority (bounded scope): 2021rate reduction, full year table and current-rate prior-year exception read. Short exact excerpt: “2021 Tax Rate Reduction”. | 2026-11-22 |
| [TIP19C01-04](https://floridarevenue.com/taxes/tips/documents/TIP_19C01-04.pdf) | Read in the linked authority (bounded scope): 2019rate reduction and then-prospective table read; reconciled with later B29. Uppercase Documents variant reader-inaccessible; lowercase succeeds. Short exact excerpt: “2019 Tax Rate Reduction”. | 2026-11-22 |
| [F-1120A R.01/24](https://floridarevenue.com/Forms_library/current/f1120a.pdf) | Read in the linked authority (bounded scope): Eligibility and displayed form columns read; not all four pages. Short exact excerpt: “$45,000 or less”. | 2026-11-22 |
| [F-7004](https://floridarevenue.com/Forms_library/current/f7004.pdf) | Read in the linked authority (bounded scope): Front form identity/tentative-payment boxes read; operative extension findings use B2/B22/B24, not unread reverse. Short exact excerpt: “Tentative tax due”. | 2026-11-22 |
| [F-1120ES](https://floridarevenue.com/Forms_library/current/f1120es.pdf) | Read in the linked authority (bounded scope): Front form title/function read; installment rules checked via B2/B23. Short exact excerpt: “Declaration/Installment”. | 2026-11-22 |
| [DOR tax/interest rates](https://floridarevenue.com/taxes/taxesfees/Pages/tax_interest_rates.aspx) | Read in the linked authority (bounded scope): Applicable completed same-session rate-table/2026interest read reused from unit42; no redundant full scan. Short exact excerpt: “11% for July 1, 2026 through December 31, 2026”. | 2026-11-22 |
| [Sunbiz annual report — failed reader access](https://dos.fl.gov/sunbiz/manage-business/efile/annual-report/) | Access attempt only: 403. No substantive page read; fee/deadline claims remain held. | Not read; access failed |
| [IRS2025ScheduleSE](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf) | Read in the linked authority (bounded scope): Page1 ordinary net-earnings multiplier,12.4%/2.9%,wagebase and half-tax deduction read. Short exact excerpt: “multiply line 3 by 92.35%”. | 2026-11-22 |
| [TIP21C01-01, redirects/revised21C01-01R](https://floridarevenue.com/taxes/tips/Documents/TIP_21C01-01.pdf) | Read in the linked authority (bounded scope): Actual2021adoption/NOL/bonus passages read; not the claimed2020rate notice. Short exact excerpt: “Adoption of 2021 Internal Revenue Code”. | 2026-11-22 |
| [TIP22C01-01](https://floridarevenue.com/taxes/tips/Documents/TIP_22C01-01.pdf) | Read in the linked authority (bounded scope): Actual internship-credit title and opening applicability read; not a2021rate notice. Short exact excerpt: “Internship Tax Credit Program”. | 2026-11-22 |
| [TIP22C01-02](https://floridarevenue.com/taxes/tips/Documents/TIP_22C01-02.pdf) | Read in the linked authority (bounded scope): Actual automatic-refund eligibility/timing read; not the claimed2022rate restoration notice. Short exact excerpt: “2022 Automatic Refund”. | 2026-11-22 |

[Enacted P.L. 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) and [2025 Schedule A instructions](https://www.irs.gov/pub/irs-pdf/f1040sa.pdf), read on 2026-11-22 for the 2025 individual SALT limitation only: the completed 2025 federal SALT-limit read is reused for the individual-cap aside only; this does not establish the corporate deduction or scholarship credit.

**Not yet confirmed; non-usable holds:** detailed federal classification/election, QSub/trust/partnership and S-conversion rules; current nexus and multistate service/SaaS/intangible sourcing/judgments; financial-organization and special telecom/alternative methods; historical enactment, refund mechanism and state comparisons; AMT/CAMT application; complete current adoption/session-law/pro forma effect on each 2025 return; historical or section 179 adjustments; Treasury/foreign-source subtraction calculations; inventory/idle/construction/sponsored-research details; full business/nonbusiness character and royalty allocation; exact NOL creation, ownership-change and S-election computations; direct long-form portal functionality and standalone late-payment penalty; actual payment calendars/cutoffs and historical interest balances; project certifications and minor-credit conditions/ordering; annual-report fees/deadlines, documentary stamps and complete other-tax/fee clearance; and all held worked-case facts. Inline holds govern the retained original assertions. No held statement may be used to select a filing or calculate a final tax or fee. Independent source review and accountant approval of this changed version are pending.
