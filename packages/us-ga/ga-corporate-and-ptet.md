---
name: ga-corporate-and-ptet
description: "Source-cited tax guide for US-GA: ga corporate and ptet. Unverified draft, pending local-accountant review."
jurisdiction: US-GA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# GA Corporate And Ptet

## Georgia Corporate Income Tax and Pass-Through Entity Tax (PTET)

Georgia corporate income tax (CIT) and individual income tax (PIT) are both levied at a flat 5.39% for tax year 2025 under O.C.G.A. §48-7, phasing toward 4.99% by 2030 under HB 1437 (2022) and HB 111 (2024). Georgia apportions multistate income using a single sales factor (since 2007) with market-based sourcing for services effective 2024 (HB 1023). A pass-through entity tax election under O.C.G.A. §48-7-23 lets S corporations and partnerships pay state tax at the entity level at 5.39%, with owners taking a refundable credit on Form 500. Major incentives include the Job Tax Credit, Quality Jobs Tax Credit, and the transferable Film Production Credit (20-30%). Tax year 2025.

## 1. Scope

This skill covers, for tax year 2025:

- Georgia corporate income tax under O.C.G.A. §48-7 (Form 600)
- Georgia S-corporation return (Form 600S)
- Georgia partnership return (Form 700, informational)
- The pass-through entity tax election under O.C.G.A. §48-7-23 (PTET)
- Single sales factor apportionment and the market-based sourcing rules adopted in HB 1023 (effective tax years beginning on or after 1 January 2024)
- Net operating loss treatment under O.C.G.A. §48-7-21(b)(10)
- Estimated tax mechanics for C corporations and PTET-electing entities
- High-level overview of the Job Tax Credit, Quality Jobs Tax Credit, Film Production Credit, and the Georgia tax-credit transfer market

Out of scope (refer out to dedicated skills or specialist reviewer):

- Georgia sales and use tax (4% state plus local) — see future ga-sales-use-tax skill
- Title Ad Valorem Tax (TAVT) on motor vehicles under O.C.G.A. §48-5C-1
- Insurance premium tax, financial institutions business occupation tax, intangibles tax on long-term notes
- Property tax (county-administered)
- Withholding tax on nonresident members of pass-through entities where no PTET election is made (Form G-2-A / NRW-2)
- Multi-state combined unitary group analysis beyond Georgia's consolidated election rules
- IRC §382 limitations on NOL after ownership change (defer to federal reviewer)
- Sales factor sourcing edge cases for intangibles, royalties, financial receipts under Reg. 560-7-7-.03

This skill assumes a Circular 230-credentialed reviewer (CPA, EA, or attorney) signs off on every output before it reaches the taxpayer or the Georgia Department of Revenue.

## 2. Phase-Down Schedule and Rate History

Georgia historically taxed corporate income at a flat 6% (since 1969). The personal income tax was graduated from 1% to 6% (top bracket starting at $7,000 single / $10,000 MFJ). HB 593 (2021) increased the personal exemption. HB 1437 (2022) collapsed the graduated PIT into a single flat rate matching the corporate rate, with a scheduled phase-down. HB 111 (2024) accelerated the phase-down.

### 2.1 Rate Schedule

**Rate Schedule**  _(O.C.G.A. §48-7; HB 1437 (2022); HB 111 (2024))_

| Tax Year | CIT Rate | PIT Rate | Authority / Notes |
| --- | --- | --- | --- |
| 2023 | 5.75% | graduated 1%-5.75% | Pre-HB 1437 PIT; legacy 5.75% CIT |
| 2024 | 5.75% → 5.49% | 5.49% flat | HB 1437 first flat year; HB 111 cut from 5.49% to 5.39% retroactively reconciled for some taxpayers |
| 2025 | 5.39% | 5.39% | HB 111 (2024) accelerated to 5.39% |
| 2026 | 5.29% (if revenue triggers met) | 5.29% (same) | Trigger: revenue estimate must meet statutory threshold |
| 2027 | 5.19% (target if triggers met) | 5.19% | Per HB 1437 framework |
| 2028 | 5.09% (target) | 5.09% |  |
| 2029 | 4.99% (target) | 4.99% |  |
| 2030 | 4.99% (target floor) | 4.99% | Stated target floor; no further automatic cuts in statute |

- **Phase-down triggers (HB 1437 §3(d))** — Before a 0.10 percentage-point reduction can take effect for a calendar year beginning on or after 1 January 2025: (1) The Governor's revenue estimate for the succeeding fiscal year is at least 3% above the revenue estimate for the present fiscal year, AND (2) the net revenue collection for the most recently completed fiscal year exceeded the net revenue collection of any of the three preceding fiscal years, AND (3) the Revenue Shortfall Reserve at the end of the most recently completed fiscal year is at least equal to the projected reduction in revenue. If any trigger fails for a given year, the reduction does not take effect that year and the rate stays flat. The phase-down resumes when triggers are met.  _(HB 1437 §3(d))_

Reviewer should confirm current-year status with the Georgia Department of Revenue and Office of Planning and Budget releases.

### 2.2 Conformity to Federal Code

- **Conformity date** — Georgia conforms to the Internal Revenue Code as of a fixed conformity date set annually by the General Assembly. For 2025 returns the conformity date is the IRC as enacted on or before 1 January 2025, with specific decoupling provisions in O.C.G.A. §48-7-21.  _(O.C.G.A. §48-7-21)_
- **§168(k) bonus depreciation** — NOT adopted (decoupled). Georgia requires depreciation computed without bonus.  _(O.C.G.A. §48-7-21)_
- **§199A QBI deduction** — Federal individual deduction is taken before federal AGI flows to Georgia, but Georgia has its own conforming treatment via Schedule 1 adjustments on Form 500. For corporations §199A is N/A.  _(O.C.G.A. §48-7-21)_
- **§163(j) business interest limit** — Adopted, with state-specific add-back/subtraction rules.  _(O.C.G.A. §48-7-21)_
- **§172 NOL** — Georgia has its own NOL rules (see §4).  _(O.C.G.A. §48-7-21)_
- **§965 transition tax** — State-level inclusion rules apply.  _(O.C.G.A. §48-7-21)_
- **GILTI / FDII** — Georgia generally treats GILTI as dividend income eligible for the dividends-received-style treatment; reviewer should confirm under Reg. 560-7-3-.06.  _(Reg. 560-7-3-.06)_
- **OBBBA (P.L. 119-21) 2025 federal provisions** — Georgia has not yet enacted explicit conformity to OBBBA-specific items. Reviewer must check the most recent annual conformity bill before filing.  _(P.L. 119-21)_

## 3. Apportionment and Market-Based Sourcing

### 3.1 Single Sales Factor

- **Single sales factor apportionment** — Georgia apportions multistate business income using a single sales factor under O.C.G.A. §48-7-31(d)(2). Property and payroll factors were eliminated effective tax years beginning on or after 1 January 2008 (with the transition completed by 2007 for most taxpayers).  _(O.C.G.A. §48-7-31(d)(2))_
- **Apportionment percentage** — Apportionment % = Georgia sales / total everywhere sales  _(O.C.G.A. §48-7-31(d)(2))_
- **Nonbusiness income allocation** — Nonbusiness income is allocated rather than apportioned, generally to the state of commercial domicile.  _(O.C.G.A. §48-7-31(c))_

### 3.2 Market-Based Sourcing for Services (HB 1023, effective 2024)

- **Market-based sourcing for services and intangibles** — For tax years beginning on or after 1 January 2024, Georgia switched from cost-of-performance sourcing to market-based sourcing for receipts from services and intangibles.  _(O.C.G.A. §48-7-31(d)(2)(A.1); HB 1023 (2023))_
- **Sourcing hierarchy for services** — 1. Receipts from services are sourced to Georgia to the extent the service is delivered to a location in Georgia. 2. If the location of delivery cannot be determined, the service is sourced to the customer's billing address or principal office. 3. A reasonable approximation may be used if neither delivery location nor customer location can be determined. 4. If still indeterminable after reasonable approximation, the receipt is excluded from the denominator (a "throw-out" rule for unsourceable receipts).  _(O.C.G.A. §48-7-31(d)(2)(A.1))_
- **Sourcing for intangibles** — For intangibles (licenses, royalties, franchise fees), receipts are sourced to Georgia based on use of the intangible in Georgia.  _(O.C.G.A. §48-7-31(d)(2)(A.1))_
- **Sourcing for tangible personal property; throwback repeal** — Sourced to Georgia if shipped to a purchaser in Georgia (destination test). The throwback rule was repealed effective tax years beginning on or after 1 January 2006 — sales shipped from Georgia to a state where the seller is not taxable are NOT thrown back into the Georgia numerator.  _(O.C.G.A. §48-7-31(d)(2)(A))_

### 3.3 Combined and Consolidated Returns

- **No combined unitary reporting required** — Georgia does NOT require combined unitary reporting. A separate-entity state in the default case.  _(O.C.G.A. §48-7-21(b)(7))_
- **Consolidated return election** — An affiliated group with more than 50% common ownership may make an election to file a Georgia consolidated return. The election: is binding for five years; requires every member of the affiliated group with Georgia nexus to be included; mirrors the federal §1501 consolidated group composition; is made on Form 600 with a Schedule 1 election attachment.  _(O.C.G.A. §48-7-21(b)(7))_
- **Default separate filing** — Without the consolidated election each Georgia-nexused entity files a separate Form 600. Intercompany transactions are NOT eliminated absent a consolidated election; transfer-pricing scrutiny applies.  _(O.C.G.A. §48-7-21(b)(7))_

Reviewer note: the consolidated election can produce double benefit or detriment depending on whether group members have Georgia-source income or losses. Model both before electing.

## 4. Net Operating Losses

### 4.1 Georgia NOL Rules

- **Statutory basis for NOLs** — Georgia NOLs are governed by O.C.G.A. §48-7-21(b)(10) (corporate) and §48-7-27 (individual). State NOLs are computed separately from federal NOLs.  _(O.C.G.A. §48-7-21(b)(10); §48-7-27)_
- **Carryforward period** — 20 years (Georgia did NOT adopt the federal TCJA indefinite-carryforward rule for state purposes; the pre-TCJA 20-year window is preserved).  _(O.C.G.A. §48-7-21(b)(10))_
- **Carryback period** — 2 years for corporate NOLs (Georgia did NOT adopt the federal CARES Act 5-year carryback; the legacy 2-year carryback under §48-7-21(b)(10.1) remains).  _(O.C.G.A. §48-7-21(b)(10.1))_
- **80% limitation** — Georgia conforms to the federal §172(a)(2) 80% of taxable income limitation for NOLs arising in tax years beginning on or after 1 January 2018. NOLs from pre-2018 tax years remain at 100% deductibility against state taxable income.  _(O.C.G.A. §48-7-21(b)(10); federal §172(a)(2))_
- **Election to forgo carryback** — An election to waive the 2-year carryback and only carry forward is available, and must be made by the original due date (including extensions) of the loss-year return.  _(O.C.G.A. §48-7-21(b)(10.1)(B))_
- **Mergers and §381/§382** — Georgia generally conforms to the federal limitations on NOL transfer in §381 (carryover on liquidation) and §382 (limitation after ownership change). Reviewer must apply the federal §382 limit and then re-apply Georgia rules.  _(IRC §381; §382)_
- **Apportionment of NOL** — Pre-apportionment vs post-apportionment NOL treatment matters. Georgia uses post-apportionment NOL — the loss is apportioned in the year incurred and the apportioned loss is carried forward.  _(O.C.G.A. §48-7-21(b)(10))_

### 4.2 Comparison Table

**Federal vs Georgia NOL comparison**  _(Federal §172; O.C.G.A. §48-7-21(b)(10))_

| Feature | Federal §172 (post-TCJA) | Georgia §48-7-21(b)(10) |
| --- | --- | --- |
| Carryback | None (CARES 5-yr expired) | 2 years (corporate) |
| Carryforward | Indefinite | 20 years |
| 80% limitation | Yes (post-2017 NOLs) | Yes (post-2017 NOLs) |
| Pre/post apportionment | N/A (federal) | Post-apportionment |
| Waive carryback election | N/A | By original due date |

## 5. Filing and Estimated Tax

### 5.1 Returns

**Returns table**  _(Georgia DOR Form 600, 600S, 700, 500 instructions, tax year 2025)_

| Entity Type | Form | Due Date | Extension |
| --- | --- | --- | --- |
| C corporation | Form 600 | 15th day of 4th month after year-end (e.g., 15 April for calendar year) | 6-month automatic via federal Form 7004 |
| S corporation | Form 600S | 15th day of 3rd month after year-end (15 March calendar year) | 6-month via Form 7004 / GA Form IT-303 |
| Partnership / LLC taxed as partnership | Form 700 (informational) | 15th day of 3rd month (15 March) | 6-month |
| Composite return for nonresident members | Form IT-CR | Same as entity | Tied to entity extension |
| PTET-electing S-corp | Form 600S with PTET election | 15 March | 6-month |
| PTET-electing partnership | Form 700 with PTET election | 15 March | 6-month |
| Individual claiming PTET credit | Form 500 | 15 April | 6-month via Form IT-303 |

### 5.2 Estimated Tax — Corporations

- **Estimated tax structure for corporations** — Georgia corporate estimated tax under O.C.G.A. §48-7-115 mirrors federal §6655 in structure. Required installments are 25/25/25/25 of the lesser of: 1. 100% of current year tax, OR 2. 100% of prior year tax (provided the prior year was a 12-month year showing a tax liability)  _(O.C.G.A. §48-7-115)_
- **Due dates for calendar-year filers** — 1st installment: 15 April; 2nd installment: 15 June; 3rd installment: 15 September; 4th installment: 15 December  _(O.C.G.A. §48-7-115)_
- **Underpayment penalty** — Interest at the prime rate plus 3% per annum on each unpaid installment. Form 600-UET computes the penalty. The annualized income installment method is available for seasonal corporations.  _(O.C.G.A. §48-2-40)_
- **De minimis estimated tax threshold** — $500 USD (A corporation owing $500 or less in net tax is not required to make estimated payments.)  _(O.C.G.A. §48-7-115)_

### 5.3 Estimated Tax — PTET-Electing Entities

- **PTET estimated payments** — PTET-electing S-corps and partnerships must also make estimated payments if PTET liability is expected to exceed $500. Same 25/25/25/25 schedule. Payments are remitted with Form 602-ES.  _(O.C.G.A. §48-7-23)_

## 6. Pass-Through Entity Tax (PTET) Election

### 6.1 Statutory Basis

- **PTET enactment and purpose** — The Georgia PTET was enacted in 2021 (HB 149) and codified at O.C.G.A. §48-7-23. It is an annual elective entity-level tax designed to circumvent the federal §164(b)(6) $10,000 SALT cap by shifting state income tax from owners (Schedule A itemized deduction limited) to the entity (above-the-line deduction on the entity's federal return).  _(O.C.G.A. §48-7-23; HB 149 (2021); IRC §164(b)(6))_
- **IRS blessing of PTET workaround** — The federal IRS blessed this state-PTET workaround in Notice 2020-75 (9 November 2020), confirming that specified income tax payments made by partnerships and S corporations are deductible at the entity level.  _(IRS Notice 2020-75)_
- **OBBBA SALT cap change** — OBBBA (P.L. 119-21, 4 July 2025) raised the federal SALT cap from $10,000 to $40,000 for 2025 with a phase-down at higher AGI levels. PTET elections remain valuable for higher-income owners, but the breakeven analysis must be redone for each client.  _(P.L. 119-21)_

### 6.2 Eligibility

- **Eligible and ineligible entities** — S corporations that are properly elected under federal §1362 and registered in Georgia; Partnerships including LLCs taxed as partnerships, general partnerships, and limited partnerships. NOT eligible: C corporations, sole proprietorships, single-member LLCs disregarded for federal tax, trusts and estates.  _(O.C.G.A. §48-7-23; IRC §1362)_

### 6.3 Election Mechanics

- **Annual election** — Made on the original (timely-filed including extensions) Form 600S or Form 700 by checking the PTET box and computing the tax on the entity return.  _(O.C.G.A. §48-7-23)_
- **Binding for the year** — Once made, the election is irrevocable for that tax year.  _(O.C.G.A. §48-7-23)_
- **All-or-nothing** — The election applies to ALL owners; you cannot elect for some owners and not others.  _(O.C.G.A. §48-7-23)_
- **No multi-year binding** — Unlike a consolidated election, the PTET is year-by-year.  _(O.C.G.A. §48-7-23)_

### 6.4 Computation

- **Taxable base for PTET** — Taxable base: Georgia-source taxable income of the entity, computed as if the entity were a C corporation, after apportionment. Each owner's share follows Schedule K-1 allocation percentages.  _(O.C.G.A. §48-7-23)_
- **PTET formula for 2025** — PTET = 5.39% × Georgia taxable income (post-apportionment) for tax year 2025  _(O.C.G.A. §48-7-23)_
- **Nonresident partner treatment** — For a partnership with nonresident partners, the PTET-electing entity pays on 100% of the Georgia-apportioned income regardless of partner residency. Resident partners get credit on Form 500; nonresident partners get credit on Form 500 (nonresident) or are relieved of composite filing.  _(O.C.G.A. §48-7-23)_

### 6.5 Owner-Level Credit (Form 500)

- **Owner refundable credit** — Owners receive a refundable Georgia credit equal to their pro-rata share of PTET paid by the entity, claimed on Form 500 Schedule 2 (resident) or 500 Schedule 3 (nonresident). The credit is refundable to the extent it exceeds the owner's Georgia income tax liability.  _(O.C.G.A. §48-7-23; Form 500)_
- **Federal K-1 reduction** — For federal purposes, the owner's K-1 income is REDUCED by the PTET (the entity took the deduction at the federal level), and the owner does NOT take a state tax deduction on Schedule A for amounts paid via the PTET.  _(O.C.G.A. §48-7-23)_

### 6.6 Estimated Tax Considerations

- **Owner estimated payment reduction** — If the entity elects PTET, owners should reduce their individual Georgia estimated payments to reflect that the entity is paying their state tax. Otherwise the owner will overpay and seek a refund.  _(O.C.G.A. §48-7-23)_

### 6.7 Reasonable Compensation (S-Corp PTET)

- **Reasonable compensation requirement** — PTET-electing S-corps still must pay reasonable compensation to shareholder-employees under federal §3121 / §3306 rules. Reasonable comp does NOT flow through the PTET — it remains W-2 wages taxable at the federal individual level. Only the K-1 ordinary income portion runs through PTET.  _(IRC §3121; §3306)_

### 6.8 Composite Return Interaction

- **PTET vs composite return** — A PTET election generally eliminates the need for a composite return (Form IT-CR) covering nonresident members, since the entity is already paying tax on the members' shares. Reviewer should confirm filing requirements per most recent Georgia DOR guidance.  _(Form IT-CR)_

## 7. Major Credits

### 7.1 Job Tax Credit (O.C.G.A. §48-7-40 and §48-7-40.1)

- **Job Tax Credit description** — A credit for businesses in qualifying industries (manufacturing, warehousing/distribution, processing, telecommunications, broadcasting, tourism, R&D, biomedical manufacturing, software development) that create net new jobs in Georgia.  _(O.C.G.A. §48-7-40; §48-7-40.1)_
- **Credit amount per net new job** — $1,250 to $4,000 per year, depending on county tier (Tier 1 highest credit, Tier 4 lowest)  _(O.C.G.A. §48-7-40)_
- **Minimum new jobs to qualify** — 2 to 25, depending on county tier  _(O.C.G.A. §48-7-40)_
- **Credit duration and carryforward** — Credit available for 5 years per qualifying job. Carryforward: 10 years.  _(O.C.G.A. §48-7-40)_
- **Offset limits** — Offsets up to 50% of Georgia income tax liability (100% in Tier 1 counties). Tier 1 counties also allow excess credit to offset Georgia withholding tax.  _(O.C.G.A. §48-7-40.1)_

Counties are re-tiered annually by the Georgia Department of Community Affairs based on per-capita income, unemployment rate, and poverty rate.

### 7.2 Quality Jobs Tax Credit (O.C.G.A. §48-7-40.17)

- **Quality Jobs Tax Credit description** — A higher-value credit for jobs paying at least 110% of the county average wage.  _(O.C.G.A. §48-7-40.17)_
- **Credit per qualifying high-wage job** — $2,500 to $5,000 per year for 5 years  _(O.C.G.A. §48-7-40.17)_
- **Minimum new jobs** — 50 within a 24-month window  _(O.C.G.A. §48-7-40.17)_

**Wage threshold scale**  _(O.C.G.A. §48-7-40.17)_

| Wage Threshold | Credit |
| --- | --- |
| 110% to 119% of county average | $2,500 |
| 120-149% of county average | $3,000 |
| 150-174% of county average | $4,000 |
| 175-199% of county average | $4,500 |
| 200%+ of county average | $5,000 |

- **Offset limits, carryforward, and stacking** — Offsets up to 100% of Georgia income tax AND state withholding. Carryforward: 10 years. Cannot be claimed on the same jobs as the standard Job Tax Credit.  _(O.C.G.A. §48-7-40.17)_

### 7.3 Film Production Credit (O.C.G.A. §48-7-40.26) — Transferable

- **Overview** — Georgia's flagship economic-development credit, often called the largest and most active state film credit in the United States.  _(O.C.G.A. §48-7-40.26)_
- **Base credit** — 20% of qualified Georgia production expenditures, minimum $500,000 of in-state spend per project  _(O.C.G.A. §48-7-40.26)_
- **Uplift** — Additional 10% if the production includes the Georgia promotional logo (the "Made in Georgia" peach logo) in qualifying placement  _(O.C.G.A. §48-7-40.26)_
- **Total combined credit** — Up to 30% of qualified spend  _(O.C.G.A. §48-7-40.26)_
- **Qualified spend** — In-state goods and services, in-state labor (Georgia residents) capped per individual, post-production done in Georgia  _(O.C.G.A. §48-7-40.26)_
- **Caps on individual compensation** — $500,000 cap per loan-out or W-2 employee  _(O.C.G.A. §48-7-40.26)_
- **Transferability** — The credit is fully transferable to any Georgia taxpayer (corporate or individual). Transfer must be reported to the Georgia DOR within 30 days using Form IT-TRANS.  _(O.C.G.A. §48-7-40.26(c))_
- **Carryforward** — 5 years for the original earner; transferees inherit the remaining carryforward.  _(O.C.G.A. §48-7-40.26)_

No statewide cap on issuance (unlike many states that cap film credits at $50-100M per year), though 2025 legislation has discussed introducing a cap; reviewer should confirm current law.

- **Audit requirement** — Mandatory third-party audit by a Georgia DOR-approved CPA firm before credits over $2.5M can be claimed or transferred.  _(HB 1037 (2020))_

### 7.4 Other Notable Credits (brief mention)

- Retraining Tax Credit (O.C.G.A. §48-7-40.5): up to $1,250 per employee for approved retraining
- R&D Tax Credit (O.C.G.A. §48-7-40.12): 10% of qualified Georgia R&D expenses above a base amount
- Investment Tax Credit (O.C.G.A. §48-7-40.2): for manufacturers and telecommunications in less-developed counties
- Port Activity Tax Credit (O.C.G.A. §48-7-40.15): bonus to Job Tax Credit for taxpayers that increase port traffic through Georgia ports by at least 10%
- Rural Hospital Tax Credit (O.C.G.A. §48-7-29.20): for individuals and corporations donating to qualified rural hospitals; donor receives 100% credit up to caps
- GOAL Scholarship Tax Credit (O.C.G.A. §48-7-29.16): redirect Georgia tax to qualified student scholarship organizations

## 8. Georgia Tax-Credit Transfer Market

Georgia has one of the largest, most liquid state tax-credit transfer markets in the United States. The market is dominated by film credits but also includes Low-Income Housing, Historic Rehabilitation, and certain conservation easement credits.

### 8.1 Market Mechanics

- **Sellers** — Film productions, real estate developers, conservation easement donors who have earned more credit than they can use against their own Georgia liability.
- **Buyers** — Georgia individuals and businesses with significant Georgia income tax liability seeking to reduce their effective rate.
- **Brokers** — Licensed credit brokerages (Stonehenge Capital, Monarch Private Capital, Tax Credit Marketplace, among others) match buyers and sellers and handle the IT-TRANS filing.
- **Pricing** — Film credits typically trade at $0.88 to $0.92 per $1.00 of face credit value. Pricing varies by: Vintage (year credit was earned, since carryforward window shortens with age); Production audit completion status (post-audit credits trade at a premium); Volume discount on large purchases ($1M+); Time of year (December/March rushes compress spreads)
- **Buyer's net benefit** — A buyer purchasing at $0.90 on the dollar saves $0.10 per $1 of Georgia tax (a 10% return on the purchase price, less transaction costs).
- **Federal tax treatment of credit purchase** — The IRS treats the purchase as the acquisition of a state tax benefit. Under Rev. Rul. 2023-... and the Tempel v. Commissioner line of cases, the credit purchase generates a short-term capital loss equal to the discount (purchase price less the state tax saved). For most buyers this is a wash or modest tax-efficient saving.  _(Tempel v. Commissioner, 136 T.C. 341 (2011))_

### 8.2 Risk Factors

- **Recapture risk** — If the underlying production fails its audit, the credits can be recaptured. Most transfer agreements include indemnification but it should be verified.
- **Authenticity / fraud** — Use a reputable broker and verify the IT-TRANS filing was accepted by Georgia DOR.
- **Federal treatment uncertainty** — IRS positions on the federal characterization of credit purchases have evolved; reviewer should consult current guidance.

## 9. Worked Examples

### Example 1 — Small Georgia C-Corp, 2025 vs Projected 2030

Acme Widgets Inc., a Georgia C-corp, manufactures and sells widgets nationwide.

Federal taxable income 2025: $1,200,000
Plus: Georgia §168(k) bonus depreciation add-back: $80,000
Less: Georgia §168 normal depreciation: $40,000
Georgia pre-apportionment taxable income: $1,240,000

Sales factor:
  Georgia sales (post-HB 1023 market-based sourcing): $4,500,000
  Total everywhere sales: $15,000,000
  Apportionment % = 4,500,000 / 15,000,000 = 30.00%

Georgia apportioned taxable income: $1,240,000 × 30.00% = $372,000

Tax at 2025 rate of 5.39%:
  $372,000 × 5.39% = $20,051

Tax at projected 2030 rate of 4.99% (assuming triggers met every year):
  $372,000 × 4.99% = $18,563

Savings 2030 vs 2025 on same income: $1,488 (about 7.4%)

Estimated payments due in 2025 (25% each):
  $5,013 due 15 April
  $5,013 due 15 June
  $5,013 due 15 September
  $5,013 due 15 December

Filing: Form 600 due 15 April 2026 (calendar year).

### Example 2 — S-Corporation Pass-Through Entity Election at $1M Net Income

Peach Software LLC, an S-corp with three resident Georgia individual shareholders (33.33% each).

Federal §1366 ordinary income flowing to K-1s: $1,000,000
Plus reasonable comp to sole shareholder-employee (already on W-2): $150,000 each = $450,000 (NOT in PTET base — W-2)
Georgia-apportioned ordinary income (single-state, 100%): $1,000,000

PTET computation (electing for 2025):
  PTET = $1,000,000 × 5.39% = $53,900
  Paid by entity with Form 600S, 25/25/25/25 estimated.
  Federal deduction: $53,900 is deducted on the federal §1120-S above-the-line, reducing each shareholder's K-1 ordinary income by $17,967.

Shareholder-level analysis (per shareholder):
  K-1 income before PTET deduction: $333,333
  K-1 income after PTET deduction at federal level: $315,367 (reduced by their $17,967 share)
  Owner's Georgia credit on Form 500: $17,967 (refundable)
  Owner's Georgia taxable income (Schedule 1 add-back of PTET, then credit applied):
    Georgia AGI = federal AGI + PTET addback $17,967 = effectively $333,333
    Georgia tax = $333,333 × 5.39% = $17,967
    Less PTET credit = $17,967
    Net Georgia tax owed by owner = $0 (excluding other income)

Federal savings (per shareholder, marginal 37% bracket):
  Federal tax saved by PTET deduction: $17,967 × 37% = $6,648
  Net SALT cap benefit (PTET workaround) over taking $40,000 OBBBA cap: depends on owner's other SALT items; reviewer must model.

Conclusion: PTET election produces meaningful federal savings for high-income owners even after OBBBA's $40,000 SALT cap expansion, because the PTET deduction is above-the-line at the entity and is not subject to the cap.

### Example 3 — Individual Buying Film Credits at $0.90 for $100,000 of Georgia Tax Savings

Dr. Smith, a Georgia individual taxpayer, projects $100,000 of Georgia individual income tax liability for 2025.

Without credits: Dr. Smith owes Georgia DOR $100,000.

With credits: Dr. Smith buys $100,000 face-value Georgia Film Tax Credits from a 2024-vintage production through a licensed broker at $0.90 on the dollar.

Purchase price: $100,000 × $0.90 = $90,000
Broker fee (typical): $500 to $1,500 flat
Total out-of-pocket: ~$91,000

Georgia tax savings: $100,000 (credit applied dollar-for-dollar against liability on Form 500)

Net cash benefit: $100,000 saved − $91,000 paid = $9,000 (about 9.9% return on capital deployed for the year)

Federal treatment:
  - The $90,000 purchase is treated as the acquisition of a state tax benefit.
  - Federal deduction for state income tax: limited by OBBBA SALT cap (now $40,000 for 2025).
  - Many practitioners treat the discount ($10,000) as a short-term capital gain when the credit is used, because the taxpayer effectively bought a $100,000 deduction-equivalent for $90,000. Reviewer must consult current IRS guidance and Tempel v. Commissioner line.

Risk: If the 2024 production is later audited and credits recaptured, Dr. Smith's $90,000 is at risk unless the broker provided indemnification. Confirm IT-TRANS was accepted by Georgia DOR before claiming.

Conclusion: Credit purchase generates roughly $9,000 of pre-federal-tax benefit on a $91,000 outlay, an attractive return if the buyer has the Georgia liability to absorb and the federal characterization holds.

## 10. Self-Checks Before Submission

Before sending output to the reviewer, confirm:

1. Tax year is identified and rates correspond to that year (5.39% for 2025).
2. Apportionment is single sales factor; market-based sourcing applied for service receipts in tax years 2024+.
3. NOL carryforward and carryback periods are state-specific (20 / 2), not federal.
4. PTET election, if made, is documented on the entity return and owners' credits flow to Form 500.
5. Federal SALT cap interaction (post-OBBBA) has been considered if PTET is recommended.
6. Bonus depreciation add-back is computed for Georgia (Georgia does not adopt §168(k)).
7. Conformity date is current (1 January 2025 for 2025 returns, subject to annual conformity bill).
8. Estimated tax mechanics are right: 25/25/25/25 schedule, $500 de minimis.
9. Credits are sequenced correctly: nonrefundable credits before refundable; PTET credit is refundable.
10. Phase-down triggers verified against most recent Georgia DOR/OPB announcements before relying on a 2026+ rate below 5.39%.
11. Cited statutes verified by reviewer against current O.C.G.A.; reviewer is responsible for final sign-off.

## 11. Refusal Catalogue

- **R-GA-1** — Combined unitary group analysis beyond Georgia's consolidated election rules (separate-entity-state assumptions break for unitary cases)  _(R-GA-1)_
- **R-GA-2** — Insurance company premium tax (entirely separate regime under O.C.G.A. §33-8)  _(R-GA-2; O.C.G.A. §33-8)_
- **R-GA-3** — Financial institutions business occupation tax (separate municipal tax)  _(R-GA-3)_
- **R-GA-4** — Sales and use tax (refer to ga-sales-use-tax)  _(R-GA-4)_
- **R-GA-5** — TAVT on motor vehicles (refer to ga-tavt skill or specialist)  _(R-GA-5)_
- **R-GA-6** — Trust and estate Georgia income tax (Form 501)  _(R-GA-6)_
- **R-GA-7** — Nexus determinations for taxpayers with no clearly established Georgia presence (P.L. 86-272 analysis required)  _(R-GA-7; P.L. 86-272)_
- **R-GA-8** — Federal §382 limitation calculations after ownership change (defer to federal reviewer)  _(R-GA-8)_
- **R-GA-9** — Transfer pricing under §482 between affiliated members not filing consolidated (specialist required)  _(R-GA-9)_
- **R-GA-10** — Credit broker selection or specific broker recommendations (compliance / fiduciary scope)  _(R-GA-10)_

## 12. Provenance

- O.C.G.A. Title 48, Chapter 7 (Income Taxes), particularly:
  - §48-7-20 (individual rate)
  - §48-7-21 (corporate net income; conformity; NOL; consolidated election)
  - §48-7-23 (Pass-Through Entity Tax)
  - §48-7-27 (individual NOL)
  - §48-7-31 (apportionment and allocation)
  - §48-7-40 et seq. (credits including Job Tax Credit, Quality Jobs, Film Production)
  - §48-7-115 (corporate estimated tax)
- HB 1437 (2022 General Assembly) — flat tax conversion and phase-down framework
- HB 111 (2024) — accelerated phase-down to 5.39%
- HB 1023 (2023) — market-based sourcing effective 2024
- HB 149 (2021) — PTET enactment
- HB 1037 (2020) — film credit mandatory audit
- IRS Notice 2020-75 — federal blessing of state PTET workaround
- P.L. 119-21 (One Big Beautiful Bill Act, 4 July 2025) — federal SALT cap to $40,000
- Georgia Department of Revenue Regulations 560-7 (income tax)
- Georgia DOR Form 600, 600S, 700, 500 instructions, tax year 2025
- Georgia Department of Community Affairs annual county tier designation
- Tempel v. Commissioner, 136 T.C. 341 (2011) — federal treatment of state credit purchase

Reviewer must independently verify every statutory citation, every rate, and every trigger status against current Georgia law before signing off. This skill is a research-and-drafting aid only and does not constitute tax advice.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
