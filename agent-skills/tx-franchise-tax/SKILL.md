---
name: tx-franchise-tax
description: "Compute and file the Texas franchise tax (the margin tax) for any taxable entity, for reports due in 2026 and 2027 (accounting years ending in 2025 and 2026). Covers who is taxable (single-member LLCs included, sole proprietors and natural-person general partnerships not), the $2,650,000 no tax due threshold on annualized total revenue, the rule that tax under $1,000 is not owed, the four margin bases (70% of revenue, revenue minus cost of goods sold, revenue minus compensation capped at $480,000 a person, revenue minus $1 million), the 0.75% and 0.375% rates, the 0.331% E-Z computation for revenue up to $20 million, single-factor apportionment, the $500,000 nexus rule, combined groups, the Public Information Report and Ownership Information Report, extensions, penalties and forfeiture. Trigger on \"Texas franchise tax\", \"margin tax\", \"no tax due threshold\", \"Form 05-158\", \"Form 05-169\", \"E-Z computation\", \"Public Information Report\", \"05-102\", \"05-167\", \"Texas LLC tax\". Texas Comptroll"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/tx-franchise-tax"
  jurisdiction: "US-TX"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Texas franchise tax (margin tax), 2026 and 2027 reports

> **Source-cited draft.** Built from the Texas Comptroller's franchise tax page (rates, thresholds and deduction limits), the 2026 franchise tax report forms page, the 2026 Texas Franchise Tax Report Information and Instructions (Form 05-915), Form 05-169 (2026), Comptroller Rule 3.586 (as published in STAR 202601004R) and Texas Tax Code Chapter 171, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For the reports due 15 May 2026 and 15 May 2027 (the 2027 report covers an accounting year ending in 2026), a taxable entity whose annualized total revenue is **$2,650,000 or less** owes no franchise tax and files only a Public Information Report (Form 05-102) or Ownership Information Report (Form 05-167). Above that, tax is **0.75%** of taxable margin (**0.375%** for qualifying retailers and wholesalers), or, if revenue is **$20 million or less**, the entity may elect the E-Z computation at **0.331%** of apportioned total revenue. Margin is the lowest of 70% of revenue, revenue minus cost of goods sold, revenue minus compensation (capped at **$480,000** a person), or revenue minus $1 million. If the tax computed is **under $1,000**, nothing is owed, but the reports are still filed. A single-member LLC is taxable even though the IRS disregards it.

**Tax year and report year.** Texas names a report by the year it is due. The 2026 report (due 15 May 2026) is based on the accounting year ending in 2025; the 2027 report (due 15 May 2027) is based on the accounting year ending in 2026. The Comptroller's figures below apply to both. This skill replaces `tx-margin-tax`, which covered the same tax.

## Scope

In scope: the annual franchise tax report of one taxable entity or one combined group: whether it is taxable, the no tax due test, total revenue, the four margin bases, the rate, the E-Z election, apportionment, the information report, extension, payment, penalties, forfeiture and the final report.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Forming the entity, the Secretary of State side, registered agent, foreign registration | `tx-formation` |
| Texas sales and use tax | the Texas sales tax skill named in this folder's README |
| Texas unemployment tax on wages | `tx-payroll` |
| The owner's federal return that the figures come from | `us-schedule-c-and-se-computation`, `us-form-1065-partnership`, `us-form-1120-c-corp`, `us-1120-corporation-return-schedule-ordinary-business` |
| Insurance companies (premium tax) and other regimes outside Chapter 171 | Refer (R-TX-FT-INS) |
| Franchise tax credits, tiered partnership elections, refund claims | Refer (see "When to refuse or refer") |

## Ask the client first

1. **Entity type and owners.** LLC, corporation, limited partnership, LLP, general partnership (and are all its direct owners natural persons?), trust, or no entity at all (sole proprietor). This decides whether the tax applies at all.
2. **Total revenue, and the accounting period it covers.** The federal return lines for the period (Schedule C line 3 for a single-member LLC, Form 1065 line 1c and other lines, Form 1120 or 1120-S line 1c and other lines), and the begin and end dates. A short first period must be annualized.
3. **Texas receipts against all receipts.** Where the customers are, and what is sold (goods delivered into Texas, services performed in Texas, internet hosting, intangibles). For an out-of-state entity: Texas receipts of $500,000 or more, or any physical presence, creates nexus.
4. **Cost of goods sold and compensation.** Does the entity sell goods it produces or acquires (if pure services, there is usually no cost of goods sold)? W-2 Medicare wages for each person, benefits paid, and each owner's net distributive income.
5. **Retail or wholesale share.** Is more than half of revenue from retail or wholesale trade, and does less than half of that come from products the entity or an affiliate produces?
6. **Affiliates and history.** Any other entity under more than 50% common ownership in a unitary business (combined group), and whether last year's report was filed and on time (extension options depend on it).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 and 2027 reports | Source |
| --- | --- | --- |
| No tax due threshold (annualized total revenue, entire business) | USD 2,650,000 | [Texas Comptroller, franchise tax: tax rates, thresholds and deduction limits](https://comptroller.texas.gov/taxes/franchise/) |
| Tax rate, retail or wholesale | 0.375% of taxable margin | [Texas Comptroller, franchise tax](https://comptroller.texas.gov/taxes/franchise/); [Tax Code 171.002(b)](https://statutes.capitol.texas.gov/Docs/TX/htm/TX.171.htm) |
| Tax rate, other than retail or wholesale | 0.75% of taxable margin | [Texas Comptroller, franchise tax](https://comptroller.texas.gov/taxes/franchise/); [Tax Code 171.002(a)](https://statutes.capitol.texas.gov/Docs/TX/htm/TX.171.htm) |
| Compensation deduction limit, per person per 12-month period | USD 480,000 | [Texas Comptroller, franchise tax](https://comptroller.texas.gov/taxes/franchise/) |
| E-Z computation total revenue limit | USD 20 million | [Texas Comptroller, franchise tax](https://comptroller.texas.gov/taxes/franchise/); [Tax Code 171.1016(a)](https://statutes.capitol.texas.gov/Docs/TX/htm/TX.171.htm) |
| E-Z computation rate (of apportioned total revenue) | 0.331% | [Texas Comptroller, franchise tax](https://comptroller.texas.gov/taxes/franchise/); [Tax Code 171.1016(b)(3)](https://statutes.capitol.texas.gov/Docs/TX/htm/TX.171.htm) |
| Margin base: share of total revenue | 70% | [Tax Code 171.101(a)(1)(A)(i)](https://tcss.legis.texas.gov/resources/TX/htm/TX.171.htm) |
| Margin base: flat deduction from total revenue | USD 1 million | [Tax Code 171.101(a)(1)](https://statutes.capitol.texas.gov/Docs/TX/htm/TX.171.htm) |
| Tax computed below this amount is not owed | USD 1,000 | [Tax Code 171.002(d)(1)](https://statutes.capitol.texas.gov/Docs/TX/htm/TX.171.htm); [Form 05-915 (2026), Minimum Franchise Tax](https://comptroller.texas.gov/forms/05-915.pdf) |
| Economic nexus for an out-of-state entity (Texas gross receipts in the federal accounting period) | USD 500,000 or more | [Rule 3.586(e)(1), STAR 202601004R](https://star.comptroller.texas.gov/view/202601004R) |
| Electronic payment required next calendar year if franchise tax paid in the prior state fiscal year (1 Sept to 31 Aug) was | USD 10,000 or more | [Form 05-915 (2026), Electronic Funds Transfer](https://comptroller.texas.gov/forms/05-915.pdf) |
| Late report penalty, each report | USD 50 | [Texas Comptroller, franchise tax: penalties and interest](https://comptroller.texas.gov/taxes/franchise/) |
| Late payment penalty | 5% if paid 1 to 30 days late; 10% if more than 30 days late | [Texas Comptroller, franchise tax: penalties and interest](https://comptroller.texas.gov/taxes/franchise/) |
| Interest on late tax | Prime rate plus 1%, starting 61 days after the due date | [Texas Comptroller, franchise tax](https://comptroller.texas.gov/taxes/franchise/); [Form 05-915 (2026), Penalties and Interest](https://comptroller.texas.gov/forms/05-915.pdf) |

The no tax due threshold and the compensation limit are reset every second year by the change in the consumer price index ([Tax Code 171.006(b)](https://statutes.capitol.texas.gov/Docs/TX/htm/TX.171.htm)); the current figures apply to reports originally due from 1 January 2026 to 31 December 2027 (Form 05-915, Important Reminders for 2026). The rates and the USD 20 million E-Z limit are fixed in the statute. Prior figures for the 2024 and 2025 reports: threshold USD 2,470,000, compensation limit USD 450,000, the same rates (Comptroller franchise tax page).

### Step 1: is the entity taxable?

Taxable, if formed in Texas or doing business in Texas: corporations (C and S), LLCs (including single-member and series LLCs), banks, savings and loan associations, professional corporations and associations, partnerships (general, limited and limited liability), certain trusts, business associations, joint ventures and other legal entities (Form 05-915, Entities Subject to Tax).

Not taxable (Form 05-915, Entities Not Subject to Tax): sole proprietorships (but a single-member LLC is taxable); general partnerships whose direct owners are all natural persons (an LLP is taxable); entities exempt under Subchapter B of Chapter 171 (an exemption must be applied for, it is not automatic); qualifying passive entities; certain grantor trusts, estates and escrows; REMICs and qualifying REITs; 401(a) and 501(c)(9) trusts; and others listed there.

**Federal treatment does not decide it.** An LLC or partnership disregarded for federal tax is a separate entity for franchise tax and files its own report unless it is in a combined group (Form 05-915, Disregarded Entities). For a single-member LLC the figures come from the owner's Schedule C.

**Doing business in Texas** (Rule 3.586): a foreign (out-of-state) entity has nexus if it has physical presence in Texas (for example an office, employees, property, or acting as general partner of a partnership doing business in Texas), or, for each federal accounting period ending in 2019 or later, Texas gross receipts of USD 500,000 or more, sourced under Rule 3.591 ([STAR 202601004R](https://star.comptroller.texas.gov/view/202601004R)). Nexus means a filing duty; it does not by itself mean tax is owed.

**New veteran-owned businesses** pre-qualified by the Comptroller (formed on or after 1 January 2016 and before 1 January 2020, or on or after 1 January 2022; 100% owned by honourably discharged natural persons; with a Texas Veterans Commission letter) are not subject to the tax for their first five years and file no PIR or OIR in that period (Form 05-915, New Veteran-Owned Businesses).

### Step 2: total revenue, annualized

1. Build total revenue from the federal return lines named in Form 05-915, Items 1 to 9 (Form 05-158-A). For a single-member LLC filing as a sole proprietorship, Item 1 is Schedule C **line 3** (gross receipts less returns and allowances); Schedule C line 6 and other LLC income items go in Item 7 to the extent not already included. Then subtract the exclusions in Tax Code 171.1011 (Item 9: for example bad debts deducted federally, flow-through funds such as sales tax collected, foreign royalties and dividends, net distributive income from a taxable entity, and the industry-specific subcontractor and pass-through exclusions).
2. From the 2026 report, amounts taken from a federal return follow the federal law in force for that year rather than the 2007 Internal Revenue Code, unless the statute names the Code (Form 05-915, Important Reminders for 2026). One effect: bonus depreciation claimed federally may go in cost of goods sold under 171.1012(c)(6), and the 2026 report allows a one-time depreciation adjustment for qualifying production assets placed in service before the accounting year begin date.
3. **Annualize** if the accounting period is not 12 months: divide total revenue by the days in the period and multiply by 365. Use the annualized figure only for the no tax due test and E-Z eligibility; the tax itself is computed on actual total revenue. The Comptroller's own example: USD 800,000 over 108 days annualizes to USD 2,703,703.70, above the threshold but E-Z eligible (Form 05-915, Annualized Total Revenue).

### Step 3: the no tax due test

If annualized total revenue from the **entire business** (not the Texas share) is USD 2,650,000 or less, the entity owes no tax and is not considered to owe any (Tax Code 171.002(d)(2)). It files no franchise tax report. The No Tax Due Report (Form 05-163) no longer exists for reports due on or after 1 January 2024. It must still file the **Public Information Report (Form 05-102)** or **Ownership Information Report (Form 05-167)** by 15 May ([2026 franchise tax report forms](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php)). Stop here.

Exceptions that file the E-Z or Long Form even at or below the threshold (2026 forms page): a passive entity (no PIR or OIR); a qualifying REIT (with a PIR or OIR); an entity above the threshold with zero Texas gross receipts (with a PIR or OIR; its tax is zero because its apportionment factor is zero).

### Step 4: the four margin bases (Long Form)

Margin is the lowest of (Tax Code 171.101(a)(1); Form 05-915, Margin):

| Base | Computation | Notes |
| --- | --- | --- |
| A | Total revenue x 70% | Always available |
| B | Total revenue minus cost of goods sold | Only entities with qualifying costs of goods (Tax Code 171.1012) |
| C | Total revenue minus compensation | Compensation per Tax Code 171.1013, capped per person |
| D | Total revenue minus USD 1 million | Always available; once per combined group |

A result below zero counts as zero (171.101(c)). The choice between cost of goods sold and compensation is an election made on each annual report and binds only that report (171.101(d)).

**Cost of goods sold (171.1012).** Texas cost of goods sold is its own definition, not federal: the costs of acquiring or producing goods (real or tangible personal property sold in the ordinary course), including direct labour, materials, production overhead, depreciation of production assets and certain handling costs. Selling, distribution, officer compensation and similar costs are excluded. A pure service business generally has none. Construction contractors and some other industries have special inclusions (171.1012(i) and following). Check each claimed cost against the statute.

**Compensation (171.1013).** Wages and cash compensation are the **Medicare wages and tips box of Form W-2** for each officer, director, owner, partner and employee, plus, to the extent not already there: net distributive income paid to a natural person from a partnership, from an LLC or corporation taxed as an S corporation, or from an LLC taxed as a sole proprietorship; and stock awards and options deducted federally. Add the cost of benefits deductible federally (workers' compensation, health care, employer HSA contributions, retirement). Cap each person's wages and cash compensation at **USD 480,000** for a 12-month period; if one person is paid by more than one member of a combined group, the cap applies once across the group (Form 05-915, Combined Compensation). Payments to independent contractors are not compensation.

### Step 5: rate

0.375% if the entity is primarily engaged in retail or wholesale trade, meaning all of: (1) revenue from retail or wholesale activities is greater than revenue from all other activities; (2) less than 50% of the retail or wholesale revenue comes from selling products the entity or an affiliate produces (eating and drinking places, SIC Major Group 58, are exempt from this test); and (3) it does not provide retail or wholesale utilities, including telecommunications, electricity or gas (Tax Code 171.002(c)). Retail and wholesale follow Divisions G and F of the 1987 SIC Manual, plus the listed rental activities (SIC 5999, 7299, 753, 7359, 7353, rental-purchase) (Form 05-915, Tax Rates). Otherwise 0.75%.

### Step 6: apportionment

Apportioned margin = margin x (Texas gross receipts / gross receipts from the entire business), a single receipts factor (Tax Code 171.106(a)). Texas receipts are determined under 171.103 and Rule 3.591: tangible goods delivered to a buyer in Texas; services by the rule's location provisions for each kind of service (read the rule for the service in question rather than assuming a customer-location rule); internet hosting only if the customer is located in Texas (171.106(g)); intangibles and other receipts by the rule's specific provisions. There is no throwback rule: receipts from a state where the seller is not taxed stay out of the Texas numerator.

### Step 7: the E-Z election

If annualized total revenue is USD 20 million or less, the entity (or combined group) may instead pay apportioned **total revenue** x 0.331% (Tax Code 171.1016). No cost of goods sold, compensation, 70% or USD 1 million base, and no credits, including the temporary credit for business loss carryforwards (Form 05-915, EZ Computation). The election is made report by report. Compare both and file the lower, unless the entity needs a credit.

Rule of thumb: on the standard 0.75% rate, E-Z wins when the lowest margin is more than 44.1% of revenue (0.331 / 0.75); on the 0.375% rate, only when margin exceeds 88.3% of revenue (0.331 / 0.375), which is rare.

### Step 8: tax, the USD 1,000 rule and the forms

Tax = apportioned margin x rate (Long Form), or the E-Z amount. If the tax computed is under USD 1,000, the entity is not required to pay and is not considered to owe any tax (Tax Code 171.002(d)(1)), but must still file its report. There is no minimum tax and no estimated tax payments (Form 05-915, Minimum Franchise Tax and Estimated Tax).

Forms for 2026 ([2026 report forms page](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php)): E-Z Computation Report **05-169**, or Long Form **05-158-A** and **05-158-B**; plus **05-102** (PIR, corporations, LLCs and similar) or **05-167** (OIR, partnerships and other entities); **05-170** payment form if not paying electronically; **05-166** Affiliate Schedule and **05-177** Common Owner Information Report for combined groups; **05-175** for a tiered partnership; credit schedules 05-180, 05-181, 05-182 and 05-185. File through Webfile (11-digit taxpayer number and 6-digit XT Webfile number) or approved software.

### Combined groups

Taxable entities under more than 50% common ownership in a unitary business must file one combined report (Tax Code 171.1014; Rule 3.590); affiliated entities are presumed unitary. The group is a single taxable entity: one no tax due threshold and one E-Z limit for the whole group, one USD 1 million deduction, one margin method for every member, intercompany revenue eliminated, and Texas receipts counted only for members organized in Texas or with nexus. Every member organized in Texas or with nexus still files its own PIR or OIR. Members are jointly and severally liable (Form 05-915, Combined Groups).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Sole proprietor with no LLC | Not subject. No franchise tax filing of any kind |
| Single-member LLC disregarded federally | Subject. Files its own PIR, or report if above the threshold, from Schedule C figures |
| General partnership, all direct owners natural persons | Not subject. If any owner is an entity, it is subject |
| Annualized revenue at or below USD 2,650,000 | No tax, no franchise tax report; PIR or OIR by 15 May |
| Short first period | Annualize revenue for the threshold and E-Z tests only; do not prorate the threshold |
| Entity became subject in the year and its federal year ended before that date | First annual report is a zero report with begin and end both on the date it became subject; PIR or OIR still due (Form 05-915) |
| Tax computed under USD 1,000 | Not owed; report still filed |
| Revenue over USD 20 million | Long Form only |
| Owner of an LLC taxed as a sole proprietorship, S corporation or partnership | Owner's net distributive income counts as compensation, within the USD 480,000 cap |
| Pure service business | Usually no cost of goods sold; compare compensation, 70%, USD 1 million and E-Z |
| Out-of-state seller with Texas receipts under USD 500,000 and no physical presence | No nexus for that period |
| Passive entity (90% or more passive federal gross income; partnerships and non-business trusts only) | Files E-Z or Long Form with the passive circle blackened; no PIR or OIR |
| Entity ceasing business in Texas | Final report due 60 days after it ceases, if above the threshold; no PIR or OIR with a final report; a Texas entity must clear its taxes before terminating (Form 05-915, Final Reports) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Accounting period dates | Calendar year; confirm against the federal return |
| Whether a short period applies | Ask whether the entity was formed or became subject during the year |
| Texas receipts | 100% Texas for a Texas-based business; ask for customer locations before filing |
| Retail or wholesale qualification | 0.75% until the three tests are documented |
| Cost of goods sold | None until each cost is tied to 171.1012 |
| Compensation | W-2 box 5 only, plus owner distributive income once confirmed |
| Prior-year report filed on time | Assume not: the 100% prior-year extension option is then unavailable |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Revenue rising toward USD 2,650,000 | Crossing it brings tax on the whole margin, with no phase-in |
| A missed PIR or OIR in any year | Forfeiture of the right to transact business, and officer and director liability for debts (171.255) |
| Several related LLCs each under the threshold | Combined group rules apply one threshold to the group |
| Owner on payroll and paid distributions | Count the W-2 Medicare wages and the distributive income once each, within one USD 480,000 cap |
| Retail rate claimed by a business that makes what it sells | Fails the under-50% produced-products test |

## Worked cases

**Case 1, a decision: E-Z or Long Form?** A Texas single-member LLC providing consulting files its 2027 report for calendar year 2026. Total revenue USD 3,400,000; Texas receipts USD 2,720,000 of USD 3,400,000 (factor 0.8). No goods, so no cost of goods sold. The owner's net distributive income is USD 900,000, capped at USD 480,000; employees' W-2 Medicare wages USD 600,000; benefits USD 60,000. Compensation = USD 1,140,000.

Bases: 70% = USD 2,380,000; revenue minus compensation = USD 2,260,000; revenue minus USD 1 million = USD 2,400,000. The lowest is USD 2,260,000. Long Form tax at 0.75%: USD 2,260,000 x 0.8 x 0.75% = USD 13,560.00. E-Z: USD 3,400,000 x 0.8 x 0.331% = USD 9,003.20. Margin is 66% of revenue, above 44.1%, so E-Z wins by USD 4,556.80. File Form 05-169 and Form 05-102; pay by 17 May 2027 (15 May 2027 is a Saturday).

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

**Case 2, a retailer under the USD 1,000 rule.** A Texas LLC that resells furniture it buys from unrelated makers has 2026 total revenue of USD 2,900,000 (above the threshold), Texas cost of goods sold of USD 2,300,000, and Texas receipts of 40% of the total. It passes the three retail tests, so the rate is 0.375%.

Bases: 70% = USD 2,030,000; revenue minus cost of goods sold = USD 600,000; revenue minus USD 1 million = USD 1,900,000. Margin is USD 600,000. Long Form tax: USD 600,000 x 0.4 x 0.375% = USD 900.00. E-Z would be USD 2,900,000 x 0.4 x 0.331% = USD 3,839.60. The Long Form result is under USD 1,000, so no tax is owed (171.002(d)(1)); the entity still files Forms 05-158-A and 05-158-B and its PIR by 17 May 2027.

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

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-TX-FT-INS | Insurance company, bank or regulated utility | Refer: special rules or other chapters |
| R-TX-FT-TIER | Tiered partnership election (171.1015) | Refer; note it is not allowed where the lower tier entity has USD 2,650,000 or less of annualized revenue |
| R-TX-FT-COMB | Combined group with significant intercompany eliminations | Refer: the elimination workpaper needs a reviewer |
| R-TX-FT-APP | Alternative apportionment or disputed sourcing under Rule 3.591 | Refer |
| R-TX-FT-IND | Industry exclusions from total revenue (staff leasing, pharmacy, health care, legal trust funds and others in 171.1011) | Refer |
| R-TX-FT-CONST | Construction contractor subcontractor costs in cost of goods sold (171.1012(i)) | Refer to confirm the election and the cost list |
| R-TX-FT-FINAL | Merger, conversion, termination or final report in the year | Refer: final period rules |
| R-TX-FT-NOTICE | Audit, assessment or forfeiture notice in hand | Refer: a petition or reinstatement, not a normal report |
| R-TX-FT-PASSIVE | Passive entity claim with passive income near the 90% line | Refer |
| R-TX-FT-CREDIT | Research and development or other franchise tax credits (Form 05-182 is new for 2026) | Refer |
| R-TX-FT-REIT | REIT or other specialty classification | Refer |
| R-TX-FT-FRAUD | Suspected misstatement in earlier reports | Refer to a credentialed practitioner at once |

## Filing and payment

- **Due date:** 15 May of the report year; a weekend or holiday moves it to the next business day, so the 2027 report (accounting year ending in 2026) is due Monday 17 May 2027, because 15 May 2027 is a Saturday (Tax Code 171.202(b); Comptroller franchise tax page).
- **Extension, non-EFT payors:** request on or before 15 May through Webfile or Form 05-164 and pay at least 90% of the tax due with the report, or 100% of the tax on the prior report if that report was filed by 14 May of the current year; the extension runs to 15 November (for 2026 it ran to 16 November 2026 because 15 November was a Sunday). A below-threshold entity may file a zero-money extension for its PIR or OIR. An entity that became subject in the prior year cannot use the 100% option. If the payment rule is not met, the due date reverts to 15 May with penalty and interest (Form 05-915, Extension of Time to File (Non-EFT)). An online extension payment replaces Form 05-164; do not file both.
- **Extension, mandatory EFT payors:** extend first to 15 August (17 August 2026 for 2026) by paying electronically 90% of current tax or 100% of prior-year tax, then to 15 November by paying the balance electronically by the August date (Form 05-915, Extension of Time to File (EFT)).
- **Payment:** Webfile (credit card or electronic check), TEXNET for EFT payors, or a check with Form 05-170 to Texas Comptroller of Public Accounts, P.O. Box 149348, Austin, TX 78714-9348.
- **Penalties:** USD 50 per late report; 5% of tax paid 1 to 30 days late, 10% if later; interest at prime plus 1% from day 61; an extra 5% for not following EFT rules.
- **Forfeiture:** if reports or payments are not made within 45 days of the Notice of Intent to Forfeit (Form 05-211), the right to transact business may be forfeited; 120 days after that, the registration may be forfeited (Form 05-213). Once forfeited, officers and directors are personally liable for each debt created or incurred in Texas after the due date and before revival (Tax Code 171.255; Form 05-915, Forfeiture). A forfeited entity cannot sue in Texas courts until revived.
- **Federal deduction:** the franchise tax paid is a business tax deducted by the entity on its federal return; for a single-member LLC, on Schedule C. It is not the owner's personal state income tax.

## Completion checklist

- Entity type confirmed as taxable, with the federal classification noted but not relied on.
- Total revenue built from the right federal lines, exclusions listed, and annualized if the period is short.
- Threshold tested on the entire-business annualized figure, not the Texas share.
- All four bases shown; cost of goods sold tied to 171.1012; compensation capped at USD 480,000 a person.
- Retail rate only with the three tests documented.
- Apportionment factor supported by a receipts schedule.
- E-Z and Long Form both computed for revenue up to USD 20 million; the USD 1,000 rule applied.
- PIR or OIR prepared for every entity that needs one, including each combined group member.
- Due date, extension option and payment method recorded.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Texas Comptroller, Franchise Tax page. Read for the 2026 and 2027 table ($2,650,000; 0.375%; 0.75%; $480,000; $20 million; 0.331%), the 2024 and 2025 table, the 15 May due date, penalties ($50; 5%; 10%), interest from day 61, final reports and the July/August 2026 forfeiture notices (05-211, 05-213). | https://comptroller.texas.gov/taxes/franchise/ | 2026-11-13 |
| Texas Comptroller, Texas Franchise Tax Report Forms for 2026. Read for the end of the No Tax Due Report, PIR/OIR-only filing at or below $2.65 million, the new veteran-owned business exception, the passive, REIT and zero-receipts paths, the form list, extensions and the mailing address. | https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php | 2026-11-13 |
| Form 05-915, 2026 Texas Franchise Tax Report Information and Instructions. Read for Important Reminders for 2026 (current federal law, depreciation, threshold and compensation adjustments), entities subject and not subject, passive entities, disregarded entities, margin, tax rates and the retail tests, annualized total revenue, minimum tax (under $1,000), E-Z computation, due dates, extensions (non-EFT and EFT), the $10,000 EFT rule, penalties, forfeiture, combined groups and Items 1 to 9. | https://comptroller.texas.gov/forms/05-915.pdf | 2026-11-13 |
| Form 05-169, 2026 Texas Franchise Tax E-Z Computation Report. Read for the report layout. | https://comptroller.texas.gov/forms/05-169-a-26.pdf | 2026-11-13 |
| Texas Tax Code Chapter 171. Read for 171.002 (rates, retail tests, (d) under $1,000 and the threshold), 171.006 (indexing), 171.101 (margin), 171.1013 (compensation, including distributive income), 171.1016 (E-Z), 171.106 (apportionment, (g) internet hosting), 171.202 (annual report and extension) and 171.255 (officer and director liability). | https://statutes.capitol.texas.gov/Docs/TX/htm/TX.171.htm | 2026-11-13 |
| Comptroller Rule 3.586, Margin: Nexus, as published in STAR 202601004R. Read for physical presence and the $500,000 Texas gross receipts test for accounting periods ending in 2019 or later. | https://star.comptroller.texas.gov/view/202601004R | 2026-11-13 |

Not yet confirmed: the 2027 report forms and instructions are not yet published, so the 2027 due-date and extension dates are taken from the statute and the 2026 instructions; the rules on where each kind of service receipt is sourced (Rule 3.591) were not reread for this version, so service sourcing is stated only in outline.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `tx-franchise-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/tx-franchise-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
