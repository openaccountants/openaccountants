---
name: tx-franchise-tax
description: Compute Texas franchise tax for 2026 and 2027 reports. Covers taxable entities, nexus, annualized whole-business revenue, margin and E-Z computations, compensation, COGS, retail rates, apportionment, combined groups, information reports, extensions and payment. Preserves historical cases with explicit conditions and holds.
version: "2.2"
jurisdiction: US-TX
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - us-tax-workflow-base
category: state
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Texas franchise tax (margin tax), 2026 and 2027 reports

**Built from the law. Not yet approved.** For an ordinary taxable entity, annualized revenue from the entire business of **USD 2,650,000 or less** means no franchise tax and normally only the applicable information report. Above that threshold, compare Long Form tax at **0.75%** (or **0.375%** for a qualifying retailer/wholesaler) with the optional **0.331%** E-Z computation if annualized revenue is **USD 20 million or less**. The wages/cash-compensation cap is **USD 480,000 per person per twelve months**, prorated for the reporting period; deductible benefits are separate. [Comptroller rates and thresholds](https://comptroller.texas.gov/taxes/franchise/), [Tax Code §§171.002, 171.1013, 171.1016](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [2026 instructions, pp. 2, 5, 21](https://comptroller.texas.gov/forms/05-915.pdf).

## Scope

Compute the ordinary annual Texas franchise tax and identify its filing/payment path. A report year is the year the report is due: the 2026 report uses the last federal accounting period ending in 2025; the 2027 report uses the corresponding period ending in 2026. First periods and changes of accounting period need their actual dates. [2026 instructions, pp. 5–7](https://comptroller.texas.gov/forms/05-915.pdf).

Use `tx-formation` for formation, registered agents and foreign qualification; `texas-sales-tax` for sales/use tax; `tx-payroll` for unemployment/payroll; and `us-tax-workflow-base` with the relevant Schedule C, partnership or corporate return Guide for the federal return. This Guide also preserves the cases from retired `tx-margin-tax`; it does not create a second tax.

**Specialist boundary:** exemption applications (including AP-204), insurance, banking, utilities, trusts/estates/escrows, REMICs, REITs, passive entities, tiered partnerships, credits, refunds and final/merger/conversion reports need their specific rules. Do not infer exemption or a filing obligation from a name alone. Check this point with one of our partner accountants.

## Ask the client first

Obtain entity type, direct owners, federal classification, formation/nexus dates, Texas use-tax permit history, actual accounting dates, federal-return revenue lines and exclusions, Texas/everywhere receipts with sourcing evidence, qualifying goods costs, each person's wages/distributive income/benefits, retail activities, related entities and prior reports/payments. Ask whether active-duty relief, aerospace costs, new health-benefit relief, credits, a special industry or a notice applies before finalizing the ordinary computation.

**Do not invent missing facts.** Unknown receipts, dates, per-person wages, owner income, retail status or prior filings stop a final recommendation. A provisional calculation must label every assumption; never default to calendar year, 100% Texas, W-2-only compensation or a guessed extension eligibility.

## The method, step by step

### 1. Entity and nexus

An LLC (including a single-member LLC), corporation, LP or LLP is generally a taxable entity if formed/organized in Texas or doing business there. Federal disregarded status does not exempt an LLC. A sole proprietor without a separate limited-liability entity is excluded, as is a general partnership directly owned entirely by natural persons whose liability is not limited, including through LLP registration. Other statutory exclusions require their full conditions. [Tax Code §§171.0002, 171.001](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm).

For a foreign entity, Rule 3.586 identifies physical-presence activities such as Texas employees/representatives, property, a place of business or services. For each federal accounting period ending in 2019 or later, **USD 500,000 or more of Texas-sourced gross receipts** also creates nexus, even without physical presence. This is gross revenue reportable federally before costs, sourced under Rule 3.591(e) and (f), including when a different method apportions margin. A Texas use-tax permit creates a rebuttable nexus presumption. The beginning date is the earliest applicable physical-presence date, permit date (January 1, 2019 for an older permit), or first day of the qualifying receipts period. Being below USD 500,000 alone is not a no-nexus conclusion. [Rule 3.586(c)–(g), current January 7, 2026 text](https://star.comptroller.texas.gov/view/202601004R).

### 2. Rates and thresholds

| Item | Applicable amount and condition | Official source |
| --- | --- | --- |
| No tax due threshold | USD 2,650,000; entire-business annualized revenue, reports originally due in 2026 or 2027 | [Comptroller](https://comptroller.texas.gov/taxes/franchise/) |
| Wages/cash-compensation cap | USD 480,000 per person per twelve months, prorated to period; one cap across a combined group | [2026 instructions, p. 21](https://comptroller.texas.gov/forms/05-915.pdf) |
| Ordinary Long Form rate | 0.75% of taxable margin | [Tax Code §171.002(a)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm) |
| Qualifying retail/wholesale rate | 0.375% of taxable margin; all tests below | [Tax Code §171.002(b)–(c-2)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm) |
| E-Z election | Annualized revenue at most USD 20 million; 0.331% of apportioned actual total revenue | [Comptroller](https://comptroller.texas.gov/taxes/franchise/), [§171.1016](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm) |
| Small computed liability | Tax below USD 1,000 is not payable; required reports still filed; tiered-partnership cases held | [§171.002(d)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [instructions, p. 5](https://comptroller.texas.gov/forms/05-915.pdf) |
| Historical 2024/2025 reports only | No tax due threshold USD 2,470,000; wages cap USD 450,000 | [Comptroller prior-year table](https://comptroller.texas.gov/taxes/franchise/) |

Section 171.006 adjusts the no-tax-due amount and compensation cap biennially; it does **not** index the E-Z ceiling. Do not use the 2026/2027 amounts for an old report. [§171.006](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm).

### 3. Total revenue and annualization

Build total revenue using the entity's federal-return mapping and statutory exclusions, rather than federal taxable profit. Long Form Items 1–8 collect gross receipts and other income; Item 9 subtracts exclusions and Item 10 is total revenue. For an SMLLC federally filing as a sole proprietor, Item 1 uses Schedule C **line 3**, and Item 7 includes line 6 amounts not already included plus other relevant LLC income. [§171.1011](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [2026 instructions, pp. 15–18](https://comptroller.texas.gov/forms/05-915.pdf).

Apply exclusions only to amounts included in revenue and meeting their conditions: for example, qualifying previously included bad debts, foreign royalties/dividends, net distributive income from a taxable partnership/S corporation, or qualifying flow-through funds. Industry exclusions need specialist confirmation. From the 2026 report, the federal-return amounts use the federal tax law for that federal year unless the statute/rule expressly cites the Internal Revenue Code; an express Code reference is not automatically updated. [§171.1011(b), (c), (f)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [2026 instructions, pp. 1–2](https://comptroller.texas.gov/forms/05-915.pdf).

If the period is not twelve months, annualize **only for threshold and E-Z eligibility**: actual total revenue / days × 365. The tax calculation still uses actual revenue. The instructions' September 15–December 31, 2025 example is USD 800,000 over 108 days: annualized USD 2,703,703.70, above USD 2,650,000 and within E-Z eligibility. [2026 instructions, p. 5](https://comptroller.texas.gov/forms/05-915.pdf).

### 4. Below threshold and exceptional filing paths

For an ordinary taxable entity at or below the threshold, no tax computation report or Form 05-163 is filed; file the PIR or OIR instead. Form 05-163 was discontinued for reports due from January 1, 2024. Above threshold with zero Texas receipts, a Long Form or eligible E-Z report plus PIR/OIR is still required; the zero factor produces zero tax. [§171.204](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [2026 forms](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php).

Passive entities and qualifying REITs use a different certification/report path, not the ordinary below-threshold shortcut. Qualified new veteran-owned businesses also have a separate initial-five-year regime. These classifications and their filings are **HOLD — non-usable until individually confirmed**. Check this point with one of our partner accountants.

### 5. Long Form margin

For the ordinary case, compare these bases using entire-business total revenue: **70% of revenue; revenue minus qualifying COGS; revenue minus qualifying compensation; revenue minus USD 1 million**. Amounts at or below zero become zero. The COGS/compensation election is annual and must be notified by the annual report's due date. Do not subtract COGS and compensation together. Active-duty/replacement-training and aerospace adjustments, PEOs and other special relief are held for specialist computation. [§171.101(a)–(f)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm).

**COGS:** goods are real or tangible personal property sold in the ordinary course; the taxpayer normally must own them. Qualifying direct acquisition/production costs can include materials, production labor and production-asset depreciation. Computer programs are expressly included in the statutory goods definition; do not classify software automatically as a pure service. Selling labor, distribution/outbound freight, advertising, officers' compensation and non-production premises costs are excluded. Only demonstrably allocable indirect/administrative overhead can enter the separate deduction, capped at **4% of total indirect/administrative overhead**, with excluded costs still excluded. [§171.1012(a)–(f), (i)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm).

**Compensation:** start with W-2 Medicare wages and tips and add eligible natural-person owner net distributive income from partnerships, S corporations and sole-proprietor LLCs, plus eligible federally deducted stock awards/options, without double counting. Owner net distributive income is reportable income/gain/deductions/loss, **whether or not cash is distributed**; negative net distributive income reduces compensation and has no negative cap. Apply the prorated wages/cash cap per person across the group. Then add federally deductible employee benefits (including eligible health, retirement, workers' compensation and employer HSA contributions); benefits are not subject to the wages cap. Forms 1099 payments and employer payroll taxes are not wages/cash compensation. Undocumented-worker, military-housing, PEO/management reimbursements and new-health-benefit adjustments need their specific rules before use. [§171.1013](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [2026 instructions, p. 21](https://comptroller.texas.gov/forms/05-915.pdf).

**COGS depreciation transition:** bonus depreciation and the one-time 2026 production-asset adjustment are not a blanket deduction. Eligibility, original basis, previous deductions, asset retention and production use must be reconciled. **HOLD** this adjustment until that workpaper is checked. Check this point with one of our partner accountants.

### 6. Retail/wholesale rate

All three tests apply: retail/wholesale revenue exceeds other-trade revenue; less than half of retail/wholesale revenue comes from products produced by the entity or an affiliate (the produced-products test does not apply to SIC Major Group 58 eating/drinking activities); and the entity does not provide retail/wholesale utilities. Selling prepaid telephone calling cards is expressly excluded from “telecommunications services” for that last test. Retail/wholesale classification follows the **1987 SIC** definitions, not a NAICS label alone. [§171.002(c)–(c-2)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm).

Retail includes Division G and the specified apparel rentals (5999/7299), automotive repair (753), rental-purchase, tool/party/event/furniture rentals (7359) and heavy construction equipment rentals (7353); wholesale is Division F. For reports originally due from **January 1, 2027**, qualifying industrial-uniform, garment and linen rentals (7213/7218) are added. [§171.0001(12), (18)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [SB 2774 §§1–3](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB02774F.htm).

### 7. Apportionment

Multiply margin by Texas gross receipts / everywhere gross receipts; the denominator includes Texas receipts. Excluded revenue is generally excluded from both receipts totals. Goods delivered/shipped to a Texas buyer are Texas receipts. The general service rule concerns **services performed in Texas**, not a universal customer-head-office rule. Internet hosting has its own customer-location rule. Confirm the specific receipt category under Rule 3.591 before finalizing; SaaS, digital downloads, transportation, royalties/intangibles, reseller chains and alternative apportionment cannot be sourced merely from the customer's address. **HOLD** unresolved sourcing. Check this point with one of our partner accountants. [§§171.103, 171.105, 171.1055, 171.106(a), (g)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm).

### 8. Compare E-Z and finish the computation

At annualized total revenue no greater than USD 20 million, E-Z tax = actual total revenue × factor × **0.331%**. It allows no margin deductions or credits. Long Form tax = taxable margin after apportionment/allowable deductions × applicable rate; refer credits or other special adjustments before comparing the final liabilities. [§§171.101, 171.1016](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm).

Derived ordinary-case comparison, before credits/special adjustments and with the same positive receipts factor: E-Z beats a 0.75% Long Form computation when margin/revenue exceeds 0.331/0.75 = **44.133333…%**, not a rounded 44.1% boundary. At a qualifying 0.375% rate, the 70% margin ceiling already gives at most 0.2625% of apportioned revenue, below 0.331%; ordinary retail E-Z cannot be the cheaper method. These are arithmetic comparisons, not extra statutory rates.

If computed tax is **less than** USD 1,000, it is not payable but required reports remain due. Exactly USD 1,000 is not covered. Tiered-partnership elections are outside this shortcut. There is no general minimum franchise tax or estimated-tax report/payment requirement. [§171.002(d), §171.204(a)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [instructions, p. 5](https://comptroller.texas.gov/forms/05-915.pdf).

### 9. Combined groups

More than 50% controlling common ownership plus a unitary business can require one combined report; statutory controlling-interest tests differ by entity. Check statutory exclusions, including foreign-business exclusions, before deciding group membership. The group is one taxpayer for the threshold, E-Z limit and USD 1 million base, and uses one margin method. Intercompany revenue and related deduction eliminations must reconcile. Each member is jointly/severally liable. [§§171.0001(1), (8), (17), 171.1014](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm).

Generally the numerator includes nexus members' Texas receipts and the denominator all members' everywhere receipts; the intercompany tangible-goods resale rule in §171.1055(b) can affect the numerator. Each Texas-organized/nexus member files its own PIR/OIR. Below the group threshold, no Affiliate Schedule or Common Owner Report is required. A Common Owner Information Report is not automatic for every above-threshold group: the instructions tie it to preserved temporary loss credits. **HOLD** membership disputes, significant eliminations, foreign exclusions or resale chains. Check this point with one of our partner accountants. [§§171.103(b), 171.105(c), 171.1055](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [instructions, pp. 8–10](https://comptroller.texas.gov/forms/05-915.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Ordinary below-threshold LLC | PIR only; federal disregarded status does not remove the entity |
| Missing per-person compensation or owner net income | Do not certify a pooled compensation total |
| First federal year ends before the date the entity became subject | First annual report has that subject date as both begin/end: zero report; applicable PIR/OIR still required; next annual period starts on that date (instructions, p. 6) |
| Several related LLCs below threshold individually | Determine the combined group before testing the group threshold |
| Special classifications/reliefs, final reports, notices | Non-usable holds below; no automatic exemption, deduction or deadline conclusion |

## Worked cases

Amounts below are in USD. Each positive-tax calculation assumes an ordinary taxable entity, no special relief/credits and documented receipts; compensation totals require every person's eligibility/cap to be checked. Tax amounts shown in cents are computations; use the applicable report-year form instructions when filing.

**Case 1 — consulting LLC, 2027 report for calendar 2026.** Original inputs: revenue 3,400,000; Texas receipts 2,720,000 (factor 0.8); owner net distributive income 900,000; employees' Medicare wages 600,000; benefits 60,000; no goods. Assuming each employee is within the cap, deductible compensation is 480,000 + 600,000 + 60,000 = 1,140,000. Bases are 2,380,000 (70%), 2,260,000 (compensation), 2,400,000 (flat deduction). Long Form = 13,560.00; E-Z = 9,003.20; saving 4,556.80. E-Z wins under these facts. Annual due date: May 17, 2027, as May 15 is Saturday. Use the applicable report-year E-Z form and PIR; 2027 form layout is held pending publication/confirmation.

```oa-check
name: E-Z against Long Form, consulting LLC (2027 report)
inputs:
  revenue: 3400000
  factor: 0.8
  owner_income: 900000
  cap: 480000
  employee_wages: 600000
  benefits: 60000
steps:
  - compensation: min(owner_income, cap) + employee_wages + benefits
  - base_70: revenue * 0.70
  - base_comp: revenue - compensation
  - base_1m: revenue - 1000000
  - margin: min(base_70, base_comp, base_1m)
  - long_form_tax: margin * factor * 0.0075
  - ez_tax: revenue * factor * 0.00331
  - ez_saving: long_form_tax - ez_tax
expected:
  compensation: 1140000.00
  margin: 2260000.00
  long_form_tax: 13560.00
  ez_tax: 9003.20
  ez_saving: 4556.80
```

**Case 2 — furniture retailer, 2027 report for calendar 2026.** Original inputs: revenue 2,900,000; qualifying Texas-defined COGS 2,300,000; receipts factor 0.4. Furniture is bought from unrelated manufacturers and all retail tests are assumed documented. Bases shown: 2,030,000 (70%), 600,000 (COGS), 1,900,000 (flat deduction). Missing compensation cannot increase the least available margin; 600,000 gives tax 900.00 at 0.375%, already below the payment threshold. E-Z = 3,839.60. No payment; Long Form and PIR still due May 17, 2027. Obtain compensation to establish the exact lowest margin rather than assert it is necessarily 600,000.

```oa-check
name: Retailer, cost of goods sold base and the USD 1,000 rule (2027 report)
inputs:
  revenue: 2900000
  cogs: 2300000
  factor: 0.4
steps:
  - base_70: revenue * 0.70
  - base_cogs: revenue - cogs
  - base_1m: revenue - 1000000
  - margin: min(base_70, base_cogs, base_1m)
  - long_form_tax: margin * factor * 0.00375
  - ez_tax: revenue * factor * 0.00331
expected:
  margin: 600000.00
  long_form_tax: 900.00
  ez_tax: 3839.60
```

### Preserved historical tests and retired margin-tax cases

The earlier franchise-tax file carried a 2025 metadata year alongside some 2026 amounts. Keep these as historical inputs, not authority for using a future threshold on a 2025 report. The five original tests are:

- **H1:** SMLLC revenue 180,000: below both the 2025 and 2026 thresholds; zero tax and ordinarily PIR only.
- **H2:** SMLLC revenue 3,000,000, 100% Texas: E-Z = 9,930; Long Form cannot be compared without deductions.
- **H3:** service SMLLC revenue 5,000,000, compensation paid 2,000,000, 100% Texas: if that is verified deductible compensation, the compensation base is 3,000,000 versus 3,500,000 (70%) and 4,000,000 (flat), giving Long Form 22,500. E-Z = 16,550. Pooled payments alone do not prove deductible compensation. **HOLD final liability.** Check this point with one of our partner accountants.
- **H4:** retail SMLLC revenue 4,000,000, COGS 2,500,000: the original 1,500,000 margin and 5,625 tax require qualifying costs, retail status, a 100% Texas factor and no lower compensation base. The 70% base is 2,800,000, flat base 3,000,000; E-Z at that assumed factor is 13,240. The original facts do not supply the factor or compensation. **HOLD final liability.** Check this point with one of our partner accountants.
- **H5:** individual freelancer without an LLC/entity: no franchise tax or franchise-tax filing.

**M1 — software-development LLC, federal 2025 / 2026 report.** Preserve revenue 3,500,000; five wages of 250,000 (=1,250,000); health 40,000; retirement 30,000; owner draws with no amount; stipulated 100% Texas. Staff compensation is 1,320,000. Excluding owner net income would give bases 2,450,000 / 2,180,000 / 2,500,000, Long Form 16,350, E-Z 11,585 and apparent saving 4,765. These are **conditional arithmetic only, not a recommended election**: lack of owner W-2 does not exclude net distributive income, and software can be statutory goods. Owner net income and the software/COGS classification are missing. **HOLD final margin/election.** Check this point with one of our partner accountants.

**M2 — SaaS apportionment case, historical report year unspecified.** Preserve revenue 5,000,000 and customer principal-office figures Texas 1,200,000 (24%), California 2,000,000 (40%), other US 1,500,000 (30%), EU 300,000 (6%); assumed Long Form margin 3,000,000. Arithmetic at an assumed factor 0.24 gives E-Z 3,972, Long Form 5,400, difference 1,428. Customer offices alone do not establish the correct SaaS sourcing category or factor. **HOLD all tax outputs/election as non-usable until sourcing is proved.** Check this point with one of our partner accountants.

**M3 — SaaS LLC below threshold, 2026 report / calendar 2025.** Preserve January 2023 formation, revenue 480,000, stated customers 60% Texas/40% other US and factor 0.60, owner draws/no W-2 and one employee at 80,000. The earlier 288,000 apportioned figure is arithmetic, not the threshold base. Whole-business annual revenue 480,000 is below 2,650,000 regardless of that factor: zero tax; ordinary PIR only, due May 15, 2026. No need to decide SaaS sourcing to reach that threshold result.

**M4 — furniture retailer, 2026 report / federal 2025.** Preserve revenue 4,200,000; furniture purchase costs 2,000,000; sales-floor labor 300,000; showroom rent/utilities 180,000; pooled W-2 compensation 720,000 (old narrative used a 450,000 cap); 75% Texas/25% elsewhere; original NAICS 442110; no own/affiliate manufacture and no utilities. The old COGS 2,480,000 improperly included selling labor and non-production premises costs. With only the stated qualifying purchase costs, COGS is 2,000,000 and its base is 2,200,000; the 70% and flat bases are 2,940,000 and 3,200,000. If 720,000 is the complete deductible compensation, its base is 3,480,000. After confirming SIC retail status and factor 0.75, ordinary Long Form = 6,187.50; E-Z = 10,426.50 (the earlier rounded presentation was 10,427). The previous 4,838 is not usable. The correct 2026 wages cap is 480,000; benefits/owner income were not supplied. **HOLD final liability until the complete compensation and classification are checked.** Check this point with one of our partner accountants.

**M5 — two-manager consulting LLC, 2026 report.** Preserve revenue 3,800,000; two W-2 amounts 300,000 each; four staff 150,000 each (=600,000); health 80,000 and retirement 60,000; no goods; customer split 50% Texas/30% other US/20% international and stated receipts 1,900,000 Texas. Conditional wages/benefits total = 1,340,000, with bases 2,660,000 / 2,460,000 / 2,800,000. At an independently proved factor 0.50: Long Form 9,225; E-Z 6,289; difference 2,936. The prior 450,000 cap is replaced by 480,000 for 2026. Neither a purported §761 election nor customer-head-office sourcing validates these facts; federal status, valid payroll, all owner net distributive income and service sourcing need confirmation. If compensation were zero, 70% tax would be 9,975, but that is not a substitute for the missing facts. **HOLD final margin/election.** Check this point with one of our partner accountants.

## When to refuse or refer

A hold means no final filing figure, election or legal conclusion for the held point. Use the ordinary core computation for other supported facts; do not turn a specialty hold into a claim that the entity owes no tax.

For each of these, **Check this point with one of our partner accountants.**

- Insurance/banking/utilities; AP-204/nonprofit exemptions; grantor/business trusts, estates, escrows, REMICs, REIT/RIC or exchange vehicles; passive-entity tests (including the historical 90% boundary); veteran qualification/initial-five-year filings.
- Tiered-partnership elections and Form 05-175; significant combined-group eliminations, foreign membership exclusions, intercompany resales or temporary-credit/Common Owner Form 05-177 requirements.
- Industry-specific revenue exclusions, construction subcontractor costs, bonus-depreciation transition/one-time 2026 adjustment, active-duty/replacement training, aerospace, new small-employer health relief or special compensation exclusions.
- Credits (including research, historic-structure, housing and carryforwards; Forms 05-180/181/182/185), refunds/amended claims, alternative apportionment or disputed SaaS/digital/transportation/intangible/crypto sourcing.
- Final reports, merger/conversion/termination, acquisition/disposal periods, foreign qualification, audit/assessment/forfeiture notices, reinstatement or suspected prior misstatement; federal deductibility and the timing/form line of a franchise-tax deduction.

## Filing and payment

**Forms and portal.** For 2026: Form 05-169 is E-Z; Forms 05-158-A/B are Long Form. PIR **05-102** applies to corporations, LLCs, **limited partnerships** professional associations and financial institutions; other reportable entities use OIR **05-167**. Complete the applicable information report even when an ordinary below-threshold entity pays no tax. Webfile needs the eleven-digit taxpayer number and six-digit XT number; approved software is another route. Confirm successful submission/payment with the portal/software. [§171.203](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [instructions, pp. 2, 14, 26](https://comptroller.texas.gov/forms/05-915.pdf), [2026 forms](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php).

**Due dates.** Annual reports/information reports are due May 15; weekends/legal holidays move the date to the next business day. Thus May 15, 2026 and May 17, 2027. The 2027 date is derived from the general rule/calendar, not a claim to have read 2027 forms. [§171.202(b)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [Comptroller due-date rule](https://comptroller.texas.gov/taxes/franchise/).

**Non-EFT extension.** Timely request by the original due date through Webfile/Form 05-164 and pay at least 90% of current liability or 100% of tax reported on the previous report filed by May 14 of the current year. For 2026 the extension ends November 16 (November 15 is Sunday). New taxable entities and an entity formerly included in a combined group now filing separately cannot use the prior-year option as described in the instructions. A below-threshold entity can request a zero-money extension for its PIR/OIR. If payment requirements fail, the original due date governs and applicable underpayment incurs penalty/interest. Do not submit the paper request as well as an online extension payment. [§171.202(c), (i)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [instructions, pp. 7–8](https://comptroller.texas.gov/forms/05-915.pdf).

**EFT extension.** Mandatory electronic payors first extend to August 15 (August 17, 2026), meeting the same 90%/eligible-100% payment test electronically; for a second extension to November 15 (November 16, 2026), request by the August deadline and pay the remaining liability electronically. If all tax was paid with the first extension, the second request may be a paper Form 05-164. Combined-group extensions need the applicable Extension Affiliate List **05-165**, not just the payment. [§171.202(e)–(f)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [instructions, pp. 7–10](https://comptroller.texas.gov/forms/05-915.pdf). Final-report extensions are held separately.

**Payment method.** Prior state fiscal-year payments of at least **USD 10,000** require electronic payment in the following calendar year; that state year is September 1–August 31. At **USD 500,000 or more**, TEXNET is required. Otherwise use the permitted Webfile electronic options or check with Form 05-170; do not assume a check satisfies mandatory EFT. Paper payments go to Texas Comptroller of Public Accounts, P.O. Box 149348, Austin, TX 78714-9348. [Payment requirements](https://comptroller.texas.gov/taxes/franchise/filing-requirements.php), [instructions, p. 7](https://comptroller.texas.gov/forms/05-915.pdf), [2026 forms](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php).

**Penalties/interest.** A late required report carries USD 50 even with no tax; failure to pay/file can also impose 5% of tax due and another 5% after 30 days (minimum under those percentage provisions USD 1). Late taxes bear interest beginning on day 61; the statutory rate is the applicable prime rate plus one percentage point, with its annual determination. EFT failures can bring another 5%. Notices, fraud penalties, forfeiture and officer/director debt liability require individual review; do not state liability without the statutory defenses. Check this point with one of our partner accountants. [§171.362](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm), [§111.060](https://tcss.legis.texas.gov/resources/TX/htm/TX.111.htm), [instructions, p. 8](https://comptroller.texas.gov/forms/05-915.pdf).

**Final-report boundary.** A foreign entity ending nexus generally has a sixty-day final-report deadline; a Texas entity must satisfy the final-report/payment requirements in connection with termination, conversion or merger. They are not one identical sixty-day rule. Do not issue a final report from this annual-return method. Check this point with one of our partner accountants. [Comptroller final-report guidance](https://comptroller.texas.gov/taxes/franchise/).

## Completion checklist

Document entity/nexus, whole-business revenue and period, applicable threshold, all ordinary margin bases with each deduction supported, retail tests, receipts sourcing, E-Z comparison and payment threshold. Identify any special adjustment/hold before giving a final result. Confirm PIR/OIR/group schedules, applicable-year forms, extension conditions and payment method. Retain submission confirmation. Historical conditional outputs above are not filing recommendations.

**Circular 230 §10.37:** this material does not replace advice based on all relevant facts and applicable law. Do not rely on an incomplete historical case or an assumed fact to file a return.

## Sources

| Source | Provisions actually read | Read on |
| --- | --- | --- |
| [Texas Tax Code Chapter 171](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm) | Definitions/entity exclusions; §§171.002, .006, .101–.1016, .103–.106, .202–.205, .255–.256 and .362; special regimes identified above remain held | 2026-11-27 |
| [Comptroller franchise tax](https://comptroller.texas.gov/taxes/franchise/) | 2026/2027 and 2024/2025 rates/limits; due-date rule; final-report distinction and penalties | 2026-11-27 |
| [2026 instructions, Form 05-915](https://comptroller.texas.gov/forms/05-915.pdf) | pp. 1–10 for report/period, transition and payment rules; Items 1, 7–10, 15–17 and the relevant COGS/transition text; PIR and form instructions | 2026-11-27 |
| [2026 forms](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php) | Filing paths, form list, extensions and payment address | 2026-11-27 |
| [Rule 3.586, STAR 202601004R](https://star.comptroller.texas.gov/view/202601004R) | Entire current nexus rule, including use-tax permit, economic receipts and beginning date; browser-rendered text, effective January 7, 2026, not superseded | 2026-11-27 |
| [SB 2774 enrolled text](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB02774F.htm) | §§1–3, rental classification and application to reports originally due from January 1, 2027 | 2026-11-27 |
| [Tax Code Chapter 111](https://tcss.legis.texas.gov/resources/TX/htm/TX.111.htm) | §111.060 late-tax interest only | 2026-11-27 |
| [Payment requirements](https://comptroller.texas.gov/taxes/franchise/filing-requirements.php) | Prior-fiscal-year electronic-payment and TEXNET bands | 2026-11-27 |

Not yet confirmed: 2027 form layout; individual specialty classifications/reliefs, unresolved receipt sourcing, historical cases' missing owner/per-person compensation facts and federal deduction timing. All are explicit non-usable holds above. Check this point with one of our partner accountants.
