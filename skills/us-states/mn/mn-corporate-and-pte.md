---
name: mn-corporate-and-pte
description: Minnesota Corporate Franchise Tax and Pass-Through Entity Tax
jurisdiction: US-MN
domain: state-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# mn-corporate-and-pte

## Minnesota Corporate Franchise Tax and Pass-Through Entity Tax

Minnesota corporate franchise tax 9.8% flat rate (one of the highest state corporate rates in the country) plus a separate 5.8% Minnesota corporate alternative minimum tax and a $0-$10,460 sliding-scale minimum fee based on Minnesota property, payroll, and sales. Apportionment uses a single sales factor with market-based sourcing. Combined unitary reporting is mandatory water's-edge with a Minnesota-specific tax-haven inclusion list under Minn. Stat. §290.01 subd. 5b. GILTI is taxed on a residual basis with the 80% §250 deduction. The Pass-Through Entity (PTE) election under Minn. Stat. §289A.08 subd. 7a imposes a 9.85% entity-level tax on electing S-corporations and partnerships, with a refundable credit to owners as a federal SALT-cap workaround. Form M4 corporate, Form M8 S-corp, Form M3 partnership. Tax year 2025.

## 1. Scope

This skill covers Minnesota state-level entity income tax compliance for:

- **C-corporations** doing business in Minnesota or sourcing receipts to Minnesota (nexus under Minn. Stat. §290.015, including economic nexus post-Wayfair and bright-line factor presence tests)
- **S-corporations** (federal Subchapter S elections recognized for Minnesota — Minn. Stat. §290.9725) filing Form M8
- **Partnerships and LLCs taxed as partnerships** filing Form M3
- **Pass-Through Entity (PTE) tax** elections under Minn. Stat. §289A.08 subd. 7a, enacted by 2021 Minn. Laws 1st Spec. Sess., Ch. 14, Art. 1, with the 2023 expansion to resident owners under 2023 Minn. Laws Ch. 64, Art. 1
- **Unitary combined reporting** under Minn. Stat. §290.17 subd. 4 and §290.34, including water's-edge default, the 80/20 foreign corporation rule, the tax-haven inclusion list under §290.01 subd. 5b, and the worldwide election
- **Apportionment** under Minn. Stat. §290.191 (single sales factor) and §290.191 subd. 5 (market-based sourcing for services and intangibles)
- **GILTI and FDII** Minnesota treatment under Minn. Stat. §290.01 subd. 19d and the 80% §250 deduction
- **NOL** under Minn. Stat. §290.095 (post-TCJA conformity with 80% limit and 20-year carryforward)
- **Filing mechanics**: Form M4 (corporate franchise), M8 (S-corp), M3 (partnership), KPI/KS/KF schedules to owners, M4T (tax calc), M4I (apportionment), M4A (apportionment), Schedule NIIT (1% net investment income surcharge), Schedule PTE
- **Minnesota R&D credit** under Minn. Stat. §290.068 (separately filed Schedule RD)
- **Estimated tax** quarterly under Minn. Stat. §289A.25 (corporate) and §289A.26 (S-corp/partnership PTE)

### Out of scope (refer out)

- **Individual income tax M1** beyond the PTE credit mechanics — see `us-mn/mn-form-m1-individual` (not yet written)
- **Sales and use tax** (6.875% state + local local option taxes) — see `us-mn/mn-sales-tax` (not yet written)
- **Property tax refund (PTR)** for renters and homeowners (Form M1PR) — see `us-mn/mn-ptr` (not yet written)
- **Withholding tax** on Minnesota-source wages — separate skill
- **Estate and inheritance tax** (Minnesota imposes an estate tax on estates over $3M)
- **Insurance company premium tax**, financial institution tax, mining occupation tax — out of scope
- **Local Minneapolis/St. Paul payroll/sales overlays** — out of scope
- **Federal computations** (Schedule C, SE, federal NOL, federal AMT, federal GILTI/FDII §250, federal QBI) — defer to the federal skills (`us-tax-workflow-base`, `us-schedule-c-and-se-computation`, etc.)

The standing rule: this skill produces a credentialed-reviewer-ready Minnesota state return. Final signoff is by a CPA, EA, or attorney licensed to practice before the Minnesota Department of Revenue.

## 2. Corporate Franchise Tax Rate

### 2.1 Statutory rate

- **Minnesota corporate franchise tax rate** — 9.8% percent (Flat rate on Minnesota taxable income of every C-corporation doing business in Minnesota)  _(Minn. Stat. §290.06 subd. 1)_

This is one of the three highest state corporate income tax rates in the United States (only New Jersey at 11.5% top with surtax and Pennsylvania historically at 9.99% formerly competed; New Jersey allowed its 2.5% Corporation Business Tax surtax to lapse and then reinstated it for 2024-2028; Pennsylvania is on a phase-down schedule to 4.99% by 2031).

Important characterization: Minnesota calls this a **franchise tax** measured by income, not an income tax. The distinction matters for federal purposes (the tax is fully deductible as a state tax under §164(a)(3), subject to SALT cap for individuals but uncapped for C-corps) and for nexus analysis under Public Law 86-272 (which protects against income tax but not franchise tax as commonly applied; however Minnesota administratively respects PL 86-272 protection in practice).

### 2.2 Tax base

- **Minnesota taxable income starting point** — Federal taxable income as reported on Form 1120 Line 28 (before the federal NOL deduction and special deductions)  _(Minn. Stat. §290.0133)_
- **Additions** — Federal NOL claimed (Minnesota computes its own NOL); Federal §199A QBI deduction (Minnesota does not allow QBI for C-corps); Federal dividends-received deduction (Minnesota has its own DRD); State income taxes deducted on federal return (no double-dip); §163(j) business interest deduction limitation adjustment; Foreign-source GILTI deduction (§250) reinstated to extent excess of MN deduction; Federal bonus depreciation (Minnesota requires 80% addback of federal bonus depreciation in year claimed, then 20% subtraction in each of next 5 years); §179 expense in excess of $25,000 (Minnesota statutory cap, with addback and 5-year subtraction, historic cap; 2023 conformity legislation aligned Minnesota with federal §179 limits effective for 2024 and later tax years — confirm year-specific treatment); Domestic Production Activities Deduction (DPAD repealed federally; legacy); State and municipal bond interest from non-Minnesota sources  _(Minn. Stat. §290.0133; §290.0133 subd. 11; §290.0133 subd. 12; 2023 Minn. Laws Ch. 64)_
- **Subtractions** — Minnesota NOL deduction (computed separately, see §6 below); 80% of federal bonus depreciation addback (1/5 each year for 5 years); §179 addback recovery (1/5 each year for 5 years); Foreign royalties to the extent included in federal income (limited); Minnesota dividends-received deduction under §290.21 (80% DRD for ≥20% owned domestic corps; 70% for less-than-20%); GILTI 80% deduction (Minnesota allows 80% subtraction matching federal §250, but only on the post-§250 amount that is in federal taxable income); FDII subtraction (matches federal §250)  _(Minn. Stat. §290.0134; §290.21)_

### 2.3 Surtax / surcharge

- **No corporate surtax** — Minnesota has no corporate surtax of the New Jersey variety. The 9.8% is the all-in C-corp rate.
- **Net investment income surcharge (individuals)** — 1% percent (On net investment income over $1M, effective tax year 2024, applies to individuals, estates, and trusts, not C-corporations)  _(Minn. Stat. §290.033; enacted by 2023 Minn. Laws Ch. 64, Art. 1)_

## 3. Minnesota Corporate Alternative Minimum Tax (5.8%)

### 3.1 Overview

- **Minnesota corporate alternative minimum tax rate** — 5.8% percent (Of Minnesota Alternative Minimum Taxable Income (MN AMTI); separate from federal corporate AMT/CAMT)  _(Minn. Stat. §290.0921)_
- **AMT applicability and credit** — MN AMT applies to a C-corporation if MN AMT exceeds the regular MN franchise tax for the year. The corporation pays the higher of the two. The difference (AMT over regular tax) can give rise to a Minnesota AMT credit usable in future years against regular MN franchise tax (interaction has been simplified over the years; check current Schedule M4T instructions).  _(Minn. Stat. §290.0922 subd. 5)_

This is not the federal corporate AMT (which the TCJA repealed for tax years beginning after 2017, then partially reinstated by the IRA as the 15% Corporate Alternative Minimum Tax on book income for corporations with average annual financial statement income over $1B — federal CAMT is a different beast). Minnesota retained its own state-level AMT structure even after the TCJA federal repeal.

### 3.2 MN AMTI base

- **MN AMTI additions** — MN AMTI starts with MN taxable income and adds back: Tax-exempt interest from private activity bonds (similar to federal AMT adjustment, pre-TCJA); Accelerated depreciation in excess of ADS; Mining-related preferences; Other Minnesota-specific AMT preferences enumerated in §290.0921 subd. 3  _(Minn. Stat. §290.0921 subd. 3)_
- **MN AMT exemption and phase-out** — $40,000 exemption, phased out for AMTI between $150,000 and $310,000 USD (Historic figures — verify current; for most large corporations subject to AMT, the exemption is fully phased out)

### 3.3 Why it matters

For most profitable C-corps, regular tax (9.8% × MN taxable income) exceeds AMT (5.8% × MN AMTI), so AMT is moot. But for corporations with:
- Heavy bonus depreciation (federal deducted, MN partially adds back)
- Significant tax-exempt municipal bond holdings
- Mining or extractive activities
- NOL utilization that reduces regular tax to near zero

…the AMT can become the binding constraint. Schedule M4T computes both and the corporation owes the higher amount.

### 3.4 Minimum fee interaction

- **Total MN franchise liability** — Total MN franchise liability = max(Regular Tax, AMT) + Minimum Fee

## 4. Minimum Fee (Property/Payroll/Sales Sliding Scale)

### 4.1 The schedule

- **Minimum fee overview** — Minn. Stat. §290.0922 imposes a minimum fee on every corporation, partnership, and S-corp doing business in Minnesota, based on the sum of its Minnesota property, Minnesota payroll, and Minnesota sales (PP&S). The fee is on a sliding scale from $0 to $10,460 (the 2024 figures, indexed periodically). The Department of Revenue publishes updated brackets each year via revenue notice.  _(Minn. Stat. §290.0922 subd. 1)_

**MN PP&S Minimum Fee schedule**  _(Minn. Stat. §290.0922 subd. 1)_

| MN PP&S Sum | Minimum Fee |
| --- | --- |
| Less than $1,050,000 | $0 |
| $1,050,000 – $2,099,999 | $220 |
| $2,100,000 – $10,499,999 | $650 |
| $10,500,000 – $20,999,999 | $2,180 |
| $21,000,000 – $41,999,999 | $4,360 |
| $42,000,000 or more | $10,460 |

(Exact bracket thresholds are indexed for inflation — verify the year-2025 numbers against the current Form M4 instructions. The Department of Revenue publishes updated brackets each year via revenue notice.)

### 4.2 Computing PP&S

- **Property, Payroll, Sales components** — Property: average value of Minnesota tangible property (owned at cost, rented at 8× annual rent) — same as historic three-factor numerator. Payroll: Minnesota wages, salaries, commissions, and other compensation paid (UI wage base, generally). Sales: Minnesota-sourced receipts under the market-based sourcing rules of §290.191 subd. 5. The PP&S sum is just an additive total. There is no averaging — it is property + payroll + sales (so a $20M sales operation with no MN property or payroll still triggers the $2,180 bracket).  _(Minn. Stat. §290.191 subd. 5)_

### 4.3 Applicability

- **Entities subject to minimum fee** — The minimum fee applies to: C-corporations (paid in addition to franchise tax); S-corporations (the S-corp itself owes the minimum fee, separate from any PTE election); Partnerships filing M3 (the partnership itself owes the minimum fee); LLCs taxed as partnerships or disregarded entities doing business in MN at the entity level (a single-member LLC disregarded for federal is generally not a separate entity for MN minimum fee purposes — the owner's MN PP&S includes it). The minimum fee is not refundable, not apportioned, and not prorated for short years (it is an entity-level franchise fee for the privilege of operating in Minnesota).

### 4.4 Combined groups

- **Minimum fee for combined groups** — For a unitary combined group filing one M4, the minimum fee is computed on the group's aggregate MN PP&S (not per entity). This avoids stacking minimum fees on each member.

## 5. Apportionment

### 5.1 Single sales factor

- **MN apportionment percentage formula** — MN apportionment % = MN sales / Everywhere sales  _(2008 Minn. Laws Ch. 366, Art. 4)_
- **Single sales factor apportionment** — Effective tax year 2014 onward (per 2008 Minn. Laws Ch. 366, Art. 4, completed phase-in), Minnesota apportions multistate corporate income using a single sales factor. Property and payroll factors are no longer used in the apportionment formula. This phase-in moved Minnesota from a 3-factor (33/33/33) formula through a sales-weighted formula to pure single sales factor. The change benefits Minnesota-based corporations selling out of state (lower apportionment) and disadvantages out-of-state corporations selling into Minnesota (higher apportionment) — a deliberate economic development design.  _(2008 Minn. Laws Ch. 366, Art. 4)_

### 5.2 Market-based sourcing for services and intangibles

- **Market-based sourcing rules** — Also effective tax year 2014, Minnesota uses market-based sourcing for receipts from services and intangibles under §290.191 subd. 5: Tangible personal property sales: sourced to MN if delivered to MN purchaser (destination rule, longstanding); Services: sourced to MN if the service is received in Minnesota (market-based, replacing the prior 'cost of performance' rule); Intangibles (licensing, royalties): sourced to MN if the intangible is used in MN; Software-as-a-service / digital services: generally sourced to where the customer (end user) is located — MN follows the receipt-of-benefit market-based test. The rules for cascading sourcing (when location of customer is not determinable, fall back to billing address, then commercial domicile) follow §290.191 subd. 5(j).  _(Minn. Stat. §290.191 subd. 5; §290.191 subd. 5(j))_

### 5.3 Throwback / throwout

- **No throwback rule** — Minnesota does not have a throwback rule for sales of TPP to states where the seller lacks nexus. (Contrast California, which has throwback; New Jersey, which had throwout and repealed it.) MN sales delivered to a state where the seller has no nexus simply fall out of the numerator (and out of the denominator if you read the statute correctly — actually they remain in the denominator as Everywhere sales, which dilutes the MN factor — verify under §290.191).  _(Minn. Stat. §290.191)_

### 5.4 Special apportionment

- **Special industry apportionment rules** — Specific industries have special apportionment rules under §290.191: Financial institutions: special receipts-factor formula; Air carriers: revenue-tonne-miles or departures formula; Mining: production formula; Railroads, telecoms, trucking: industry-specific. These are out of scope for the standard freelance/SMB skill.  _(Minn. Stat. §290.191)_

## 6. Combined Unitary Reporting

### 6.1 Mandatory water's-edge unitary

- **Mandatory combined reporting** — Minn. Stat. §290.17 subd. 4 and §290.34 require mandatory combined reporting for unitary businesses with more than 50% common ownership (direct or indirect). The default is a water's-edge combination, meaning: All US-incorporated unitary affiliates are combined; Foreign-incorporated affiliates are excluded unless they meet one of the inclusion exceptions (see §6.3 and §7 below); The combined group files one Form M4 with a designated common parent or filing agent; Intercompany transactions between combined members are eliminated; Apportionment uses the group's combined MN sales / combined Everywhere sales.  _(Minn. Stat. §290.17 subd. 4; §290.34)_

### 6.2 Unitary business test

- **Unitary business test** — A unitary business is identified by the 'three unities' historically (ownership, operation, use) refined into the modern Mobil/Container/Allied-Signal functional-integration / centralization-of-management / economies-of-scale test. Minnesota follows federal constitutional limits. Practical indicators of unity: Common centralized management (shared C-suite, shared HR, IT, treasury); Functional integration (sales channel sharing, shared intellectual property, shared manufacturing); Economies of scale (group purchasing, shared insurance, consolidated cash management); Vertical integration (upstream/downstream operations). A holding company with passive subsidiaries operating in unrelated lines of business may not be unitary; treat unity determination as facts-and-circumstances and document the analysis.

### 6.3 Inclusion exceptions (mandatory inclusion despite water's-edge default)

- **Mandatory inclusion entities** — Even under water's-edge, the following entities are mandatorily included in the MN combined return: 1. Domestic International Sales Corporation (DISC) and former Foreign Sales Corporation (FSC) — included regardless of foreign incorporation; 2. §936 possessions corporations (Puerto Rico) — included; 3. Tax-haven corporations under Minn. Stat. §290.01 subd. 5b — included even if foreign-incorporated and otherwise 80/20 (see §7 below). This is the critical Minnesota-specific override; 4. Foreign corporations with 20% or more US property and payroll (i.e., that fail the 80/20 test of §290.01 subd. 19c) — included as US corporations.  _(Minn. Stat. §290.01 subd. 5b; §290.01 subd. 19c)_

### 6.4 Worldwide election

- **Worldwide combination election** — Under §290.17 subd. 4(f), the unitary group may elect worldwide combination, bringing in all foreign affiliates regardless of the 80/20 rule. This election is: Binding for the year and subsequent years until revoked with consent; Rarely beneficial because most foreign affiliates have either low MN sales (denominator-inflating, factor-diluting) or high foreign-source income (base-increasing) — the math usually disfavors worldwide; Considered when foreign losses can be combined against MN-apportioned US income, or when a specific structure has the tax-haven inclusion already triggered and the taxpayer prefers a clean worldwide approach.  _(Minn. Stat. §290.17 subd. 4(f))_

## 7. Tax Haven List and 80/20 Rule

### 7.1 The 80/20 foreign corporation exclusion

- **80/20 computation formula** — Foreign Property + Foreign Payroll / Worldwide Property + Worldwide Payroll ≥ 80%  _(Minn. Stat. §290.01 subd. 19c)_
- **80/20 foreign corporation exclusion rule** — Minn. Stat. §290.01 subd. 19c (and the inclusion rule at subd. 5b) excludes from the unitary combined group any corporation with 80% or more of its property and payroll outside the United States ('80/20 corporation'). The rationale: such an entity is functionally a foreign operation that water's-edge combination is meant to exclude. This is a property-and-payroll test, not a sales test. A foreign-incorporated entity selling primarily into the US with US sales force could fail the 80/20 test (because its payroll is outside but the test only looks at property+payroll average) — typically the rule cleanly excludes genuine foreign-operating affiliates and pulls in shell or near-shell entities.  _(Minn. Stat. §290.01 subd. 19c; §290.01 subd. 5b)_

### 7.2 The Minnesota tax haven list — the critical override

- **Tax haven inclusion override** — Minn. Stat. §290.01 subd. 5b designates approximately 40 jurisdictions as tax havens whose corporations are included in the MN combined return regardless of 80/20 status, regardless of where they actually operate. This is one of the most aggressive state-level anti-base-erosion rules in the US. The current statutory list (as of the most recent legislative update) includes (verify against current §290.01 subd. 5b — Minnesota has periodically updated the list, and the 2023 legislative session made modifications).  _(Minn. Stat. §290.01 subd. 5b)_

**Minnesota tax haven jurisdictions list**  _(Minn. Stat. §290.01 subd. 5b)_

| Jurisdiction |
| --- |
| Andorra |
| Anguilla |
| Antigua and Barbuda |
| Aruba |
| Bahamas |
| Bahrain |
| Barbados |
| Belize |
| Bermuda |
| British Virgin Islands (BVI) |
| Cayman Islands |
| Cook Islands |
| Curaçao (formerly Netherlands Antilles) |
| Cyprus |
| Dominica |
| Gibraltar |
| Grenada |
| Guernsey, Sark, and Alderney (Channel Islands) |
| Isle of Man |
| Jersey |
| Liberia |
| Liechtenstein |
| Luxembourg |
| Malta (note: Malta has been on and off the list across legislative sessions) |
| Marshall Islands |
| Mauritius |
| Monaco |
| Montserrat |
| Nauru |
| Niue |
| Panama |
| St. Kitts and Nevis |
| St. Lucia |
| St. Vincent and the Grenadines |
| Samoa |
| San Marino |
| Seychelles |
| Turks and Caicos |
| US Virgin Islands |
| Vanuatu |

**Critical practitioner note**: This list has been the subject of repeated legislative attention. The 2013, 2016, and 2023 sessions all touched the list. Always verify the current statutory enumeration against the latest version of Minn. Stat. §290.01 subd. 5b and any Revenue Notices interpreting it. Some jurisdictions (notably Luxembourg, Cyprus, and Malta) have appeared on and off depending on EU pressure and Minnesota political winds. The 2023 Legislature added jurisdictions in connection with the broader OECD Pillar Two framework but did not adopt a substance-based exception.

### 7.3 How tax-haven inclusion works

- **Mechanics of tax-haven inclusion** — If a unitary affiliate is incorporated in a listed tax-haven jurisdiction (and is more than 50% commonly owned): 1. Its income is included in the MN combined return regardless of where it operates; 2. Its property, payroll, and sales are included in the apportionment denominators (Everywhere); 3. To the extent it has MN-sourced sales (market-based sourcing), those go in the numerator; 4. Foreign tax credit at the federal level does not flow through to MN; MN gives no FTC. This effectively means a Delaware or Minnesota-parented US group with a Cayman Islands IP holding company that licenses IP to operating affiliates must include the Cayman entity in the MN combined return, even if the Cayman entity has no US operations or US sales. The licensing royalties received from US operating affiliates are eliminated as intercompany, but the apportionment math may shift in unexpected ways.

### 7.4 Constitutional considerations

The Minnesota tax haven inclusion has been challenged on Commerce Clause grounds (foreign-commerce clause and discrimination against foreign-incorporated entities). The Minnesota Tax Court and Minnesota Supreme Court have upheld the rule, citing the unitary business principle and the state's interest in preventing base erosion. Recent challenges have focused on Pillar Two interaction and treaty considerations, but no successful constitutional invalidation has occurred. Practitioners should monitor pending litigation.

## 8. GILTI and FDII

### 8.1 GILTI in Minnesota

- **GILTI Minnesota treatment** — Federal Global Intangible Low-Taxed Income (GILTI) under §951A is taxed at the US shareholder level. Minnesota's treatment: Minnesota starts with federal taxable income (FTI), which includes GILTI; Federal §250 deduction (50% of GILTI for 2018-2025, scheduled to drop to 37.5% in 2026 under pre-OBBBA law; OBBBA modifications may apply — verify) flows through into FTI; Minnesota provides an additional 80% subtraction of the net GILTI amount (post-§250) under Minn. Stat. §290.0134, effectively reducing the MN inclusion further; Result: MN taxes residual GILTI at 9.8% × (GILTI – §250 deduction) × 20% × MN apportionment. This is among the more generous state GILTI regimes (some states tax full GILTI as a dividend with limited deduction; others fully decouple).  _(Minn. Stat. §290.0134)_
- **Worked GILTI example** — Federal GILTI inclusion: $10M; Federal §250 deduction (50%): $5M; Net federal inclusion: $5M; MN 80% subtraction on net inclusion: $4M subtracted; MN GILTI base: $1M; MN tax: $1M × MN apportionment % × 9.8%  _(Minn. Stat. §290.0134)_

### 8.2 FDII

- **FDII Minnesota treatment** — Foreign-Derived Intangible Income (FDII) under §250(a)(1)(A) gets a federal 37.5% deduction for 2018-2025 (scheduled to drop to 21.875% in 2026 under pre-OBBBA law). Minnesota: Follows the federal §250 FDII deduction (it flows through FTI); Provides no additional MN subtraction for FDII beyond the federal §250; Net effect: FDII is taxed in MN at 9.8% on the post-§250 amount, apportioned.  _(§250(a)(1)(A))_

### 8.3 Subpart F

- **Subpart F treatment** — Subpart F income is included in FTI and apportioned at the MN level. Minnesota provides a dividends-received deduction under §290.21 for certain Subpart F amounts treated as foreign-source dividends, but the rules are technical — review §290.21 subd. 4 for the foreign DRD.  _(Minn. Stat. §290.21 subd. 4)_

### 8.4 §965 transition tax

The §965 deemed repatriation transition tax (one-time, for tax year 2017 / 2018 depending on year-end) is largely historic. Minnesota required addbacks of the §965(c) deduction portion in the year of inclusion, with associated DRD treatment. Most clients are past this, but if a fiscal-year C-corp is still installmenting §965 liability under §965(h), monitor the MN coordination.

## 9. Net Operating Losses (NOL)

### 9.1 Conformity with TCJA post-2017

- **MN NOL rules post-TCJA** — Minn. Stat. §290.095 governs the Minnesota NOL. Minnesota conforms to the federal TCJA NOL regime: No carryback for NOLs arising in tax years beginning after December 31, 2017; 20-year carryforward (note: this is longer than the federal indefinite carryforward; Minnesota historically allowed 15-year carryforward and extended to 20 in connection with TCJA conformity — verify the exact MN carryforward period under current §290.095; some practitioner sources cite 'indefinite' matching federal, others cite '20-year'. Use 20-year as conservative unless the current statute clearly says otherwise.); 80% taxable-income limit on NOL utilization (matching federal §172(a)(2)(B)); Separate-return-year limitation (SRLY) rules apply for combined groups, similar to federal consolidated return rules — losses generated by a member before joining the combined group can only offset that member's MN-apportioned income.  _(Minn. Stat. §290.095)_

### 9.2 Pre-2018 NOLs

- **Pre-2018 NOL treatment** — NOLs from tax years beginning before 2018 retain their original carryback/carryforward periods (2-year carryback historically, 20-year carryforward, no 80% limit). These dwindle but may still be in carryforward.

### 9.3 Mechanics

- **NOL computation mechanics** — NOLs are computed at the Minnesota apportioned level — the MN NOL is the loss after MN modifications and apportionment, not the federal NOL. So a federal NOL of $1M for a corporation with 10% MN apportionment generates a $100k MN NOL (plus or minus MN modifications). This is tracked separately on Schedule M4NC (NOL computation). For combined groups, the NOL belongs to the group, not individual members, with SRLY tracking for pre-combination losses.

## 10. Filing and Estimated Tax

### 10.1 Form M4 (corporate franchise)

- **Form M4 due date and extension** — Due date: 15th day of the 4th month after year-end. For calendar-year C-corps, April 15, 2026 for tax year 2025. For fiscal-year corps, the 15th of the 4th month after the fiscal year-end. (Note: Minnesota historically had a March 15 due date; it shifted to April 15 to match the federal post-TCJA C-corp due date.) Extension: Minnesota grants an automatic 7-month extension to file if at least 90% of the tax liability is paid by the original due date. No extension form is required if the federal extension is filed; otherwise file Form M4 with the extension box checked.
- **Forms in the M4 package** — Form M4 — main franchise tax return; Schedule M4I — corporate income and apportionment computation; Schedule M4A — apportionment factor detail; Schedule M4NC — NOL computation; Schedule M4T — tax computation (regular and AMT); Schedule RD — R&D credit; Schedule M4PI — pass-through income (if the corp is a partner in a partnership); Schedule NIIT — N/A for C-corps (this is for individuals)

### 10.2 Form M8 (S-corporation)

- **Form M8 details** — S-corp itself files M8 (no entity tax unless PTE elected; minimum fee still applies); KS schedules issued to shareholders (Minnesota analog of federal K-1); Due date: 15th day of the 3rd month after year-end (March 15 for calendar year)

### 10.3 Form M3 (partnership)

- **Form M3 details** — Partnership files M3 (no entity tax unless PTE elected; minimum fee applies); KPI schedules issued to partners (individual partners) and KPC to corporate partners; Due date: 15th day of the 3rd month after year-end (March 15 for calendar year)

### 10.4 Estimated tax

- **C-corp quarterly estimates** — C-corps (M4): Quarterly estimates under Minn. Stat. §289A.25. Due April 15, June 15, September 15, December 15 (15th day of 4th, 6th, 9th, 12th month of the tax year for calendar-year filers). Safe harbor: pay the lesser of (a) 100% of prior year tax (if prior year was a 12-month tax year) or (b) 90% of current year tax. Required if MN tax liability is > $500.  _(Minn. Stat. §289A.25)_
- **Splitting and underpayment penalty** — Splitting: Equal quarterly payments (25/25/25/25) or annualized income installment method available for seasonal/lumpy income. Underpayment penalty: Computed on Schedule M15C (corporations) using the short-period interest rate published by DOR. S-corps and partnerships (PTE election): Quarterly estimates required for the PTE tax itself — see §11 below.

### 10.5 E-filing and payment

- **E-filing and payment methods** — Minnesota mandates e-filing for most corporate returns. Payments via: Minnesota e-Services portal (preferred); ACH credit/debit; Wire transfer; Check with voucher (paper only, generally discouraged)

## 11. Pass-Through Entity (PTE) Tax Election

### 11.1 Background and statutory authority

- **PTE statutory authority and background** — Minn. Stat. §289A.08 subd. 7a authorizes the Pass-Through Entity Tax (often called 'PTE tax' or 'PTE election'), enacted by 2021 Minn. Laws 1st Spec. Sess., Ch. 14, Art. 1 as Minnesota's response to the federal SALT cap under TCJA §164(b)(6). The election is one of approximately 36 state PTE workarounds blessed by IRS Notice 2020-75, which confirmed that entity-level state taxes paid by partnerships and S-corps are deductible as business expenses at the entity level (escaping the individual $10,000 SALT cap). The 2023 Minnesota Legislature (2023 Minn. Laws Ch. 64) expanded the PTE election to include resident owners, removing the pre-2023 limitation that had been interpreted by some practitioners as nonresident-owner-only. This was a significant expansion and made the MN PTE workable for fully Minnesota-resident-owned S-corps and partnerships.  _(Minn. Stat. §289A.08 subd. 7a; 2021 Minn. Laws 1st Spec. Sess., Ch. 14, Art. 1; 2023 Minn. Laws Ch. 64; IRS Notice 2020-75)_

### 11.2 Eligible entities

- **PTE eligible and non-eligible entities** — Eligible: S-corporations (federal Subchapter S elections, filed via M8); Partnerships (general, limited, LLP, LLLP) filing M3; LLCs taxed as partnerships filing M3; LLCs taxed as S-corporations filing M8. Not eligible: C-corporations (they pay 9.8% directly); Single-member LLCs disregarded for federal tax (no entity tax base; the owner reports on M1); Trusts taxed as partnerships (rare); Publicly traded partnerships; Entities required to be included in a unitary combined group (combined groups file under §290.17 framework, not PTE).  _(Minn. Stat. §290.17)_

### 11.3 Election mechanics

- **PTE election process** — Annual election on the timely-filed M3 or M8 (including extensions). Check the box on the return. Binding for the year — once elected, cannot be revoked for that year. All qualifying owners are bound by the election. There is no opt-out at the partner/shareholder level. (This is in contrast to some other states like New York, which allow partner-by-partner election.) The election is made by the entity, typically by a managing partner or officer with authority.

### 11.4 Tax rate

- **PTE tax rate** — 9.85% percent (Equal to the top Minnesota individual income tax rate; applies to the entity's Minnesota-source income allocable to owners subject to MN individual income tax)  _(Minn. Stat. §290.06 subd. 2c)_
- **PTE base for resident and nonresident owners** — For a fully Minnesota-resident-owned partnership with 100% MN-source income, the PTE base is 100% of the partnership's apportioned MN income. For a multi-state partnership with nonresident partners: Resident partners' share of all entity income (resident-taxed on worldwide basis) is in the PTE base; Nonresident partners' share of MN-source income only is in the PTE base; This combined PTE base is taxed at 9.85% at the entity level.

### 11.5 Owner credit

- **Refundable PTE credit to owners** — The PTE tax paid is refundable as a credit to each owner on their individual return: Form M1 (individual) — line for PTE credit; Form M2 (fiduciary, for trust/estate owners) — analogous line. The credit is refundable — if it exceeds the owner's MN tax, the owner gets a refund check. The credit prevents double taxation (entity pays 9.85%, owner gets it back via credit). The federal benefit comes from the entity deducting the PTE payment as a §164 business expense on its federal partnership / S-corp return, reducing pass-through K-1 income to the federal individual owner — bypassing the $10,000 federal SALT cap for the state-tax portion.

### 11.6 Estimated tax requirement

- **PTE quarterly estimates** — Quarterly estimates required for PTE-electing entities, with the same 4 / 6 / 9 / 12 month due dates as corporate estimates. Safe harbor: 90% of current-year PTE tax or 100% of prior-year PTE tax. Underpayment penalty under §289A.26 for failure to estimate.  _(Minn. Stat. §289A.26)_

### 11.7 Interaction with composite returns

- **Composite vs PTE election** — Minnesota historically allowed S-corps and partnerships to file composite returns on behalf of nonresident owners (paying tax at the highest marginal rate on the owners' MN-source income). With the PTE election available, the composite return is largely superseded for entities that elect PTE. But: An entity can choose composite or PTE — not both for the same owners in the same year; Composite has no federal SALT-cap benefit (composite tax is paid by the entity on behalf of individuals, treated as individual tax for federal purposes — capped); PTE has the federal SALT-cap workaround. Recommendation default: PTE election is preferred over composite for tax years 2022 and later, for any entity with high-income owners hitting the federal SALT cap. Run the math each year — for very small entities with low MN income, the PTE election may not move the needle and the simpler composite (or no entity election) may suffice.

### 11.8 Federal-state coordination

- **Federal-state PTE coordination mechanics** — Entity pays MN PTE tax (9.85% × MN-source income); Entity deducts PTE tax on federal 1065 / 1120-S as a business expense under §164 (per Notice 2020-75); Federal K-1 income to owners is correspondingly reduced; Owner's federal AGI is lower (good for various phase-outs); Owner gets MN PTE credit on M1 (refundable if exceeds MN liability); Owner does not deduct the PTE tax on Schedule A (it was already deducted at the entity); Owner's MN M1 starts with federal AGI, then adds back the PTE deduction to compute MN AGI (because MN doesn't allow the entity-level deduction at the individual side) — and then claims the PTE credit; Net: the math reconciles to roughly the same MN cash outflow but with federal AGI reduced by the PTE deduction.  _(Minn. Stat. §290.0131; IRS Notice 2020-75)_

### 11.9 Owner-level reporting

- **Owner-level PTE reporting** — Schedule KPI (partnership) or KS (S-corp) shows the owner's share of MN income and PTE tax credit. Owner reports on Form M1 (individual), claiming the refundable PTE credit. Nonresident owners with only PTE-paid MN income may have no further filing obligation in Minnesota if the PTE fully discharges their tax (this is administrative — verify under current DOR guidance, as some nonresidents are still required to file M1NR).

## 12. Minnesota R&D Credit

### 12.1 Statutory framework

- **MN R&D Credit for Increasing Research Activities** — Minn. Stat. §290.068 — Credit for Increasing Research Activities — provides a Minnesota R&D credit similar in structure to the federal §41 credit but with Minnesota-specific rate and base.  _(Minn. Stat. §290.068)_

### 12.2 Rate

- **MN R&D credit rate tiers** — 10% of the first $2 million of Minnesota qualified research expenses (QREs) in excess of the base amount; 4% of QREs in excess of $2 million over the base amount percent (The base amount is computed using a fixed-base percentage of average gross receipts (similar mechanism to federal §41) or under the Minnesota alternative simplified credit method)  _(Minn. Stat. §290.068)_

### 12.3 Qualified research expenses

- **Minnesota QRE definitions** — Minnesota QREs mirror federal §41 definitions: Wages for qualified services (research, supervision, support); Supplies consumed in qualified research; Contract research (65% of contracted amounts); Cloud computing rental for research (added in recent federal updates, MN conforms). QREs must be incurred in Minnesota — wages for MN-based researchers, supplies for MN-based research, etc. Out-of-state research is excluded.

### 12.4 Refundability and carryforward

- **MN R&D credit refundability and carryforward** — Non-refundable (per the current §290.068 rules; there was an effort to make it refundable for small businesses but the broad credit remains non-refundable as of 2025); 15-year carryforward of unused credit; No carryback; Credit reduces regular MN franchise tax (does not reduce the minimum fee or AMT directly — AMT credit interaction is separate)  _(Minn. Stat. §290.068)_

### 12.5 Schedule RD

- **Schedule RD filing** — Filed with M4 (C-corp), M8 (S-corp), or M3 (partnership). For pass-through entities, the credit flows through to owners on KPI/KS schedules and is claimed on M1 (with the same 15-year carryforward at the owner level).

### 12.6 Coordination with federal §41

- **Independent MN and federal §41 computations** — Independent computations. Minnesota does not require federal §41 election to claim MN credit, but QREs must meet the federal definition (incorporated by reference under §290.068). For pass-through entities where the federal §41 credit is taken at the owner level (via federal K-1), the MN credit at the entity level passes through similarly.  _(Minn. Stat. §290.068)_

## 13. Worked Examples

### 13.1 Example A — Simple Minnesota C-corporation

**Facts**:
- Acme Manufacturing, Inc., a Minnesota-domiciled C-corp
- All operations in Minnesota (100% apportionment)
- Federal taxable income (Form 1120 Line 28, before NOL/special deductions): **$5,000,000**
- No federal bonus depreciation timing differences this year (steady-state)
- No NOL carryforward
- MN sales: $20M, MN payroll: $8M, MN property: $15M → PP&S = $43M

**MN regular tax**:
- MN taxable income = $5,000,000 (no significant MN adjustments)
- MN apportionment = 100%
- MN regular tax = $5,000,000 × 9.8% = **$490,000**

**MN AMT**:
- MN AMTI ≈ $5,000,000 (no significant preferences)
- MN AMT = $5,000,000 × 5.8% = $290,000
- AMT < Regular Tax, so AMT does not apply

**Minimum fee**:
- PP&S = $43M → falls in the $42M+ bracket → minimum fee = **$10,460**

**Total MN franchise tax**:
- $490,000 (regular) + $10,460 (min fee) = **$500,460**

**Estimated tax**:
- 4 × $125,115 quarterly installments (or 25% of safe harbor calc)

### 13.2 Example B — Multinational with Cayman tax-haven subsidiary forced into combined return

**Facts**:
- TechParent, Inc., Minnesota-domiciled C-corp
- TechOps US, Inc. (Delaware C-corp, 100% subsidiary of TechParent) — US operating subsidiary
- TechIP Holdings, Ltd. (Cayman Islands, 100% subsidiary of TechParent) — holds IP, licenses to TechOps US for $10M/year royalty
- All three are 100% commonly owned and functionally integrated (unitary)
- TechIP has no US property or payroll (would qualify as 80/20 if not for tax-haven inclusion)
- **Cayman Islands is on the §290.01 subd. 5b tax-haven list → TechIP IS included in MN combined return**

**Federal level**:
- TechParent files consolidated 1120 with TechOps US (federal consolidated return for ≥80% owned domestic subsidiaries — Cayman is foreign and not in federal consolidated)
- Cayman royalty income flows through to federal taxable income via Subpart F or GILTI mechanisms at the US shareholder level
- Assume net combined US federal taxable income after Subpart F/GILTI inclusions: $50M

**MN combined return**:
- Group members: TechParent + TechOps US + **TechIP Cayman** (forced inclusion under §290.01 subd. 5b)
- Intercompany royalty between TechIP and TechOps US: **eliminated** in combined return (TechOps's $10M royalty deduction reversed; TechIP's $10M royalty income reversed)
- Combined group income (before MN modifications): assume $50M (matches federal, since intercompany eliminations net out)
- MN apportionment factor:
  - Numerator: combined group's MN-sourced sales = $30M (all from TechOps US, primarily MN customers)
  - Denominator: combined group's Everywhere sales = $200M (US + Cayman group, but Cayman has minimal third-party sales)
  - MN apportionment = 15%
- MN apportioned income = $50M × 15% = $7.5M
- MN regular tax = $7.5M × 9.8% = **$735,000**
- AMT check: AMTI ≈ $7.5M → AMT = $7.5M × 5.8% = $435,000. Regular > AMT, no AMT.
- Minimum fee: group PP&S = $80M → top bracket = $10,460

**Total MN franchise tax**: $735,000 + $10,460 = **$745,460**

**What changes if TechIP were in a non-tax-haven jurisdiction (e.g., Ireland)?**:
- TechIP would qualify as 80/20 foreign and be excluded from MN combined
- TechOps US's $10M royalty deduction would remain
- TechOps US's MN taxable income would be reduced by $10M of royalty expense
- MN apportionment denominator (Everywhere sales) would change too
- Net MN tax would likely be significantly lower — depending on the math, possibly $100k-$300k less
- **This is the policy purpose of the tax haven list** — to prevent base erosion through IP holding structures

### 13.3 Example C — Partnership PTE election (resident and nonresident partners)

**Facts**:
- Northstar Consulting LLP, an LLC taxed as partnership, files M3
- Two partners:
  - Anna, Minnesota resident, 60% partner
  - Ben, Wisconsin resident, 40% partner
- Partnership income (federal Schedule K, total ordinary business income): **$1,000,000**
- All income MN-sourced (consulting services to MN clients, market-based sourcing → 100% MN)
- Partnership elects PTE for tax year 2025

**PTE computation**:
- MN-source income subject to PTE: **$1,000,000** (100% MN-sourced)
- All of Anna's distributive share is in base (resident, taxed on worldwide) → $600,000
- All of Ben's distributive share that is MN-sourced is in base (nonresident, taxed on MN-source only — but here 100% MN-source) → $400,000
- PTE base: $1,000,000
- **PTE tax = $1,000,000 × 9.85% = $98,500**

**Federal effect**:
- Partnership deducts $98,500 on Form 1065 as a business expense (per Notice 2020-75)
- Federal ordinary business income drops from $1,000,000 to $901,500
- K-1 to Anna: $540,900 (60% of $901,500)
- K-1 to Ben: $360,600 (40% of $901,500)
- Anna's federal AGI is lower than it would have been without PTE election (vs. $600k allocation pre-PTE)
- Anna's federal SALT-cap exposure on state taxes is reduced (the entity-level $98,500 is not on her Schedule A)

**Minnesota effect at owner level**:
- Anna's M1 starts from federal AGI (which includes the lower $540,900 K-1)
- Anna **adds back** her share of the PTE deduction on M1 (Schedule M1M addition for PTE deduction add-back) = $59,100 (60% of $98,500)
- Anna's MN AGI now reflects the original $600,000 allocation
- Anna computes MN regular tax on $600,000 plus other income — assume MN tax = $58,000
- Anna claims **PTE credit** of $59,100 (60% × $98,500)
- Anna's net MN: $58,000 owed less $59,100 credit = $1,100 refund

- Ben (Wisconsin resident): files M1NR for MN-source income
- Ben's MN-source income (his $400,000 share of MN-source partnership income — for nonresident purposes computed pre-PTE deduction, but the credit mechanics restore parity)
- Ben claims PTE credit of $39,400 (40% × $98,500)
- Net: Ben's MN tax is largely or fully discharged by the PTE credit; may receive refund

**Cash and timing**:
- Entity makes quarterly PTE estimated payments throughout 2025 (~$24,625 per quarter)
- Anna and Ben get K-1 with PTE credit in early 2026
- Anna files M1 by April 15, 2026; Ben files M1NR
- Anna's federal tax savings on the SALT-cap workaround (assume she's at 37% federal): roughly $98,500 × 37% × her share = $21,867 federal benefit (less the federal-level partnership deduction's pass-through effect — net positive)

**Why the election is worth it**:
- Without PTE: Anna pays MN tax of ~$59,100 on her $600k share. That tax sits on her Schedule A, subject to $10,000 federal SALT cap. She gets at most $10,000 deduction value (~$3,700 federal benefit at 37%).
- With PTE: $59,100 of MN tax is deducted at entity level (full federal benefit ~$21,867 at 37%), and Anna's MN tax is netted against the credit. **Federal benefit improvement: ~$18,000** for Anna alone.

## 14. Provenance and Citations

### Primary statutory sources

- **Minn. Stat. §290** — Income Tax (entire chapter; corporate franchise tax)
- **Minn. Stat. §290.01** — Definitions (subd. 5b tax-haven list; subd. 19c 80/20 corporation; subd. 19d federal tax base conformity)
- **Minn. Stat. §290.06** — Tax rates (subd. 1 corporate 9.8%; subd. 2c individual top rate 9.85%)
- **Minn. Stat. §290.0133–0134** — Additions and subtractions
- **Minn. Stat. §290.17** — Allocation of income (combined unitary at subd. 4; worldwide election at subd. 4(f))
- **Minn. Stat. §290.191** — Apportionment (single sales factor at subd. 2; market-based sourcing at subd. 5)
- **Minn. Stat. §290.0921** — Corporate alternative minimum tax (5.8%)
- **Minn. Stat. §290.0922** — Minimum fee (PP&S sliding scale)
- **Minn. Stat. §290.095** — Net operating loss
- **Minn. Stat. §290.21** — Dividends-received deduction
- **Minn. Stat. §290.068** — R&D credit
- **Minn. Stat. §289A.08 subd. 7a** — PTE election
- **Minn. Stat. §289A.25** — Corporate estimated tax
- **Minn. Stat. §289A.26** — Partnership/S-corp/PTE estimated tax
- **Minn. Stat. §290.033** — 1% net investment income surcharge (individual, 2024+)

### Session laws

- **2008 Minn. Laws Ch. 366, Art. 4** — single sales factor and market-based sourcing phase-in (completed 2014)
- **2021 Minn. Laws 1st Spec. Sess., Ch. 14, Art. 1** — original PTE election enactment
- **2023 Minn. Laws Ch. 64, Art. 1** — PTE expansion to resident owners; net investment income surcharge; conformity updates

### Administrative guidance

- **Minnesota Department of Revenue Form M4 Instructions** — annual; the authoritative line-by-line guidance
- **Form M3, M8 Instructions** — partnership and S-corp filings
- **Schedule RD Instructions** — R&D credit
- **Schedule PTE Instructions** — PTE election
- **MN Revenue Notices** — official interpretive notices, e.g., on apportionment sourcing, combined reporting, tax-haven list updates
- **MN DOR Corporate Franchise Tax Fact Sheets** — practitioner-oriented summaries

### Case law to monitor

- **HMN Financial, Inc. v. Commissioner of Revenue** — combined-return inclusion of holding companies
- **Hutchinson Technology v. Commissioner of Revenue** — apportionment sourcing
- **Pending and historical challenges to the tax-haven inclusion list** on Commerce Clause grounds — Minnesota Tax Court has consistently upheld

### Cross-references within the OpenAccountants skill library

- `us-tax-workflow-base` — Tier 1 workflow scaffolding
- `us-schedule-c-and-se-computation` — federal pass-through computation (feeds owner-level M1)
- `us-federal-return-assembly` — federal 1040/1120 assembly
- `us-qbi-deduction` — federal §199A (Minnesota does not allow QBI for individuals — note the M1M add-back; covered conceptually here only by reference)
- `us-quarterly-estimated-tax` — federal quarterlies (Minnesota state quarterlies are computed in parallel)
- `us-ca-return-assembly` and `us-federal-tx-return-assembly` — parallel state assembly patterns to model the MN return assembly on

### Reviewer signoff requirements

Every Minnesota M4, M8, or M3 produced from this skill must be reviewed and signed by:

- An **EA, CPA, or attorney** with practitioner standing before the Minnesota DOR
- Familiarity with **combined unitary reporting** for any multi-entity engagement
- Familiarity with **PTE election cost-benefit analysis** if PTE is being considered
- Familiarity with the **current §290.01 subd. 5b tax haven list** (verify against current statute every engagement — the list changes)

This skill provides preparation scaffolding only. It is not a substitute for credentialed review and is not authoritative tax advice to the taxpayer.

## End of mn-corporate-and-pte v0.1

*End of mn-corporate-and-pte v0.1. Last updated 2025-11-15. Verification status: pending — content awaits review by a Minnesota-licensed CPA or EA with combined-reporting expertise before being marked verified.*

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
