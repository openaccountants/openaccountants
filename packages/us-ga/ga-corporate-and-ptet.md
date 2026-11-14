---
name: ga-corporate-and-ptet
description: Compute Georgia corporate income tax on Form 600 for tax year 2026, and the election by an S corporation (Form 600S) or partnership (Form 700) to pay Georgia income tax at the entity level (the pass-through entity tax). Covers the 4.99% rate tied to the individual rate, the start-of-year rate rule for fiscal years, HB 1199 conformity and bonus depreciation addback, related-member addbacks, single gross receipts apportionment, NOLs with the 80% limit, Georgia consolidated returns, Form 600S-CA nonresident consent, Public Law 86-272, the owner's PTEDED and PTEADD lines, due dates, extensions and penalties, with 2025 returns still open. Trigger on "Georgia corporate income tax", "Form 600", "Georgia PTET", "Georgia entity level election", "Form 700", "Form 600S". Net worth tax is in ga-net-worth-tax; estimated tax in ga-estimated-tax-depth.
version: "1.1"
jurisdiction: US-GA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# Georgia corporate income tax and the pass-through entity tax election, tax year 2026

> **Source-cited draft.** Built from HB 463 (2026), HB 1199 (2026), HB 1023 (2024), HB 111 (2025), the 2025 IT-611, IT-611S and IT-711 booklets, DOR's HB 149 pass-through entity tax FAQ, its corporate income and net worth tax page and its penalty page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A corporation whose taxable year begins in 2026 pays Georgia income tax at **4.99%** of its Georgia taxable income (5.19% for years beginning in 2025), because the corporate rate is tied by statute to the individual rate for the same year. The rate is set by the year the taxable period begins and is not prorated. Business income is apportioned by **gross receipts only**. An S corporation or partnership may elect each year to pay Georgia tax at the entity level at the same rate; its owners then exclude that income (PTEDED) and claim no Georgia credit for it. A calendar-year Form 600 is due 15 April 2027; Forms 600S and 700 are due 15 March 2027.

## Scope and who this is for

In scope, for tax year 2026 with a dated section for 2025 returns:
- the corporate income tax on Form 600;
- the election by an S corporation (Form 600S) or a partnership (Form 700) to pay Georgia income tax at the entity level. This skill calls it the pass-through entity tax (PTET) election; DOR calls it the "election to pay tax at the entity level";
- corporate and electing-entity due dates, extensions and penalties.

Who is subject to it ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download)): "All corporations that own property or do business in Georgia, or that have income from Georgia sources are required to file a Georgia income tax return." A corporation that is a partner, limited or general, in a partnership that owns property, does business or has income in Georgia is treated as doing so itself.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Corporate net worth tax (reported on the same Form 600 or 600S) | `ga-net-worth-tax` |
| Corporate and electing-entity estimated tax (Form 602-ES, Form 600 UET) | `ga-estimated-tax-depth` |
| The owner's own Form 500 | `ga-income-tax` |
| Nonresident withholding and composite returns (Form IT-CR) when no election is made | refer |
| Sales and use tax | `ga-sales-tax` |
| Insurance premium tax, property tax, detail of Georgia credits | refer |

## Ask the client first

1. **Which taxable year, and when does it begin?** The rate follows the year the period begins and is not prorated for fiscal years: a fiscal year beginning 1 July 2025 uses 5.19% throughout.
2. **Entity type for federal purposes:** C corporation, S corporation (and any QSub), partnership or LLC taxed as one, or a disregarded single-member LLC. For an S corporation: any nonresident shareholders, and has each signed Form 600S-CA?
3. **Georgia activity and receipts:** property, employees, whether sales activity goes beyond solicitation of orders for tangible goods (Public Law 86-272), and gross receipts by customer location (Georgia and everywhere).
4. **Federal taxable income and the book-tax detail:** section 168(k) bonus depreciation (this year or earlier), research costs under sections 174 and 174A, business interest (section 163(j)), intangible expenses and interest paid to related members, state income taxes deducted federally.
5. **Net operating losses by loss year** (ended after 31 December 2017? began on or after 1 January 2018?), any farm or insurance-company losses, and whether the corporation is in an affiliated group filing federally consolidated or has a Georgia consolidated election.
6. **For an S corporation or partnership: does it want the entity-level election?** The owners and their residence, owner estimates already paid, and whether any owner prefers owner-level tax. The election binds all owners.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| Corporate income tax rate, taxable years beginning on or after 1 January 2026 | 4.99% | [HB 463 (2026)](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download) |
| Corporate income tax rate, taxable years beginning on or after 1 January 2025 | 5.19% | [HB 111 (2025), O.C.G.A. § 48-7-20(a.1)](https://gov.georgia.gov/document/2025-signed-legislation/hb-111/download); [2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download) |
| Rate for an electing S corporation or partnership | the individual rate for the corresponding year (4.99% for 2026) | [HB 1023 (2024), O.C.G.A. §§ 48-7-21(b)(7)(C)(ii), 48-7-23(b)(3)](https://gov.georgia.gov/document/2024-signed-legislation/hb-1023/download); [HB 463 (2026), 4.99% rate](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download) |
| Apportionment factor, tax years beginning on or after 1 January 2008 | gross receipts only (100%) | [2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download) |
| NOLs from years beginning on or after 1 January 2018, maximum share of Georgia income before NOLs | 80% | same |
| Addback of payments to unauthorized employees, per year | more than $600 | same |
| Late filing penalty, income tax | 5% a month of tax not paid by the original due date, up to 25% | [DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates) |
| Late payment penalty, income tax | 0.5% a month, up to 25% | same |

**Why the corporate rate follows the individual rate.** HB 1023 (2024) rewrote O.C.G.A. § 48-7-21(a): corporations pay tax "at the same rate of the tax imposed on individuals under subsection (a.1) of Code Section 48-7-20 for the corresponding taxable year", for taxable years beginning on or after 1 January 2024; it did the same for electing S corporations and partnerships. HB 463 (2026) set the individual rate at 4.99% for 2026 and states it reduces "the rates of taxation on corporate and partnership income". From 1 January 2027 the rate falls 0.125 of a point a year toward 3.99%, subject to the 1 December revenue tests described in `ga-income-tax`; treat any 2027 rate as unconfirmed until the Office of Planning and Budget reports. DOR's corporate page and the 2025 booklets still show 5.19% because they describe tax year 2025.

### Corporate income tax on Form 600

1. **Pick the rate** by the start of the taxable year (table above).
2. **Decide which return.** C corporation: Form 600. S corporation: Form 600S, unless a nonresident shareholder has not consented on Form 600S-CA, in which case Georgia disregards the S election and the corporation files Form 600 and pays the regular tax. Partnership: Form 700. Disregarded single-member LLC: included in the owner's return.
3. **Start from federal taxable income** and make the Georgia additions and subtractions (Form 600 Schedules 4 and 5), applying HB 1199 conformity ([HB 1199 (2026)](https://gov.georgia.gov/document/2026-signed-legislation/hb-1199/download)):
   - for taxable years beginning on or after 1 January 2025 the Code is federal law "enacted on or before January 1, 2026", so both 2025 and 2026 include P.L. 119-21 apart from the listed exceptions;
   - treated as not in effect: section 168(k) (add back bonus depreciation and use Georgia depreciation), section 174A, section 179(d)(1)(B)(ii), section 199, section 163(h)(4), and the CARES Act changes to sections 172 and 461(l); read the HB 1199 text for any other section in play;
   - applied as before the 2017 federal act: sections 118, 163(j), 174 and 382(k)(1). The 2025 IT-611 says Georgia "does not follow I.R.C Section 174 under the 2017 Tax Cuts and Jobs Act for research and experimental expenditures paid or incurred in tax years beginning after December 31, 2021";
   - add back income taxes of other states, the United States and foreign countries deducted federally;
   - add back intangible expenses, related interest and captive REIT expenses paid to related members, unless an exception is shown on Form IT-Addback or IT-REIT;
   - add back payments of more than $600 in a year to unauthorized employees.
4. **Separate nonbusiness income, then apportion** ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download)). Allocate investment interest, investment rents and non-business gains as the booklet describes. Apportion the rest by Georgia gross receipts divided by gross receipts everywhere: "For tax years beginning on or after January 1, 2008, the Georgia apportionment ratio shall be computed by applying only the gross receipts factor."
   - A company that both makes or sells tangible goods and does other business includes gross receipts from both; one with no tangible-goods business includes only receipts "from activities which constitute the company's regular trade or business".
   - Receipts other than sales of tangible goods are Georgia receipts "if received from customers within this State, or if the receipts are otherwise attributable to this State's marketplace" (Reg. 560-7-7-.03 has the detail).
   - A partner in a partnership or joint venture includes its pro rata share of the partnership's gross receipts.
5. **Apply the NOL** (Schedule 9 and Form IT-552). Losses from years beginning before 2018 apply first, without the 80% limit. Losses from years beginning on or after 1 January 2018 (except certain insurance companies) may offset no more than 80% of Georgia income before NOLs. Losses from years ending after 31 December 2017: no carryback, unlimited carryforward. Farm losses carry back 2 years; certain insurance-company losses carry back 2 and forward 20. Georgia did not adopt the 2020 CARES Act NOL changes, and follows IRC sections 108, 381, 382 and 384. Carry the Georgia apportioned loss, not the federal loss.
6. **Compute income tax** at the year's rate, then credits (Schedule 10) and prepayments. Add the net worth tax from `ga-net-worth-tax`.
7. **Consolidated groups.** Affiliated corporations filing a federal consolidated return file separate Georgia returns unless they have Georgia approval or are required to consolidate. For tax years beginning on or after 1 January 2023 a group may elect a Georgia consolidated return on an original return: the parent ticks "Consolidated GA Parent Return" and each subsidiary files Form 600 ticking "GA Consolidated Subsidiary". Each subsidiary still files its own net worth return, and credits and NOLs are tracked company by company.
8. **Check estimated tax** (`ga-estimated-tax-depth`) and file by the due date; tax is due by the original due date even with an extension.

### The pass-through entity tax election

Source: [DOR HB 149 PTET FAQ](https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq); [2025 IT-711 booklet](https://dor.georgia.gov/document/document/2025-it-711-partnership-income-tax-booklet/download); [2025 IT-611S booklet](https://dor.georgia.gov/document/document/2025-it-611s-s-corporation-income-tax-booklet/download); [HB 1023 (2024)](https://gov.georgia.gov/document/2024-signed-legislation/hb-1023/download).
- **Who can elect.** Available for taxable years beginning on or after 1 January 2022. For taxable years beginning on or after 1 January 2023, "all partnerships are eligible to make the election to pay tax at the entity level, regardless of who owns or controls the partnership". S corporations are eligible. "Single-member LLCs not taxed as a Partnership or S Corporation are not eligible to make the election." (For 2022 only, a partnership had to be wholly owned by persons eligible to hold S corporation shares.)
- **How and when.** Tick the box and complete the schedules on Form 600S or Form 700. The election "must be made by the due date or extended due date of the entity's income tax return and is irrevocable after the applicable due date passes". It is annual.
- **Rate and base.** The individual rate for the year (4.99% for 2026) on the entity's net income allocated and apportioned under O.C.G.A. § 48-7-31. The entity cannot deduct "taxes that are based on or measured by gross or net income or any other variant thereof".
- **Binds everyone.** "The election to pay tax at the entity level is binding on all the owners including the nonresident owners." No composite return for nonresident owners; an electing S corporation is outside the nonresident-member withholding rule.
- **Owners: an exclusion, not a credit.** On Form 500 owners subtract their share of income taxed at entity level (Schedule 1 Line 12, PTEDED) and add their share of entity-level loss (Schedule 1 Line 5, PTEADD). "The owners are not eligible to claim a credit for taxes paid to Georgia with respect to income taxed at the entity level by Georgia." Owner income not taxed at entity level by Georgia (for example a resident's share apportioned elsewhere) stays taxable to the owner, who may claim the other-state credit if O.C.G.A. § 48-7-28 is met, or the § 48-7-27(d) adjustment where another state taxed it at entity level.
- **Attributes stay with the entity.** Credits and NOLs do not pass through, even in a later non-election year. An electing entity may irrevocably elect to pass through credits generated in the year, except the Qualified Education Expense, Qualified Education Donation and Qualified Rural Hospital Expense credits. NOLs follow the C corporation rules.
- **Composite overpayments** from an earlier year cannot be claimed on the electing entity's return; request a refund.
- **Federal side.** Under [IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf) a partnership or S corporation making a "Specified Income Tax Payment" deducts it in computing its taxable income "for the taxable year in which the payment is made"; it is not separately stated and "is not taken into account in applying the SALT deduction limitation" of any owner. A 2026 balance paid in 2027 is a 2027 federal deduction. Whether electing saves tax depends on each owner's federal itemized position: model it per owner (see the federal SALT figures in the federal skills).

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Fiscal year beginning 1 July 2025 | 5.19% for the whole year; the rate is not prorated |
| S corporation with a nonresident shareholder who did not sign Form 600S-CA | Georgia disregards the S election; file Form 600 and pay corporate tax |
| S corporation, no election, nonresident shareholders | Withholding applies unless a composite return (Form IT-CR) is filed, the members' aggregate annual share of Georgia taxable income is under $1,000, or the shareholder has a signed Form 600S-CA and reports and pays the tax |
| Protected by Public Law 86-272 | No income tax (zero on Schedule 1 Line 8, with a statement), but net worth tax still applies and the return is still filed |
| Single-member LLC disregarded federally | Not eligible for the election |
| Partnership wants to elect after the extended due date | Too late for that year |
| Owner of an electing entity asks for a Georgia credit for the entity's tax | Not allowed; exclude the income (PTEDED) instead |
| Consolidated group | Separate Georgia returns unless elected or approved; net worth never consolidated |

## Worked cases

Client facts are invented; rates and rules are those above.

**Case 1: 2026 calendar-year C corporation, multistate.** Georgia taxable income before apportionment (after additions and subtractions) $1,000,000; Georgia gross receipts $3,000,000 of $10,000,000 everywhere. Ratio 30%, Georgia taxable income $300,000, tax $300,000 x 4.99% = $14,970. Using the 2025 rate by mistake would give $15,570.

```oa-check
name: GA 2026 C corporation, single gross receipts factor
inputs:
  income_before_apportionment: 1000000
  ga_receipts: 3000000
  total_receipts: 10000000
  rate_2026: 0.0499
steps:
  - ratio: ga_receipts / total_receipts
  - ga_taxable: income_before_apportionment * ratio
  - tax: ga_taxable * rate_2026
  - tax_at_2025_rate: ga_taxable * 0.0519
expected:
  ratio: 0.30
  ga_taxable: 300000
  tax: 14970
  tax_at_2025_rate: 15570
```

**Case 2: 2026 C corporation using a post-2017 NOL.** Georgia income before NOL $450,000; Georgia NOL carryforward $600,000, all from years beginning after 2017. NOL allowed: 80% of $450,000 = $360,000. Georgia taxable income $90,000; tax $90,000 x 4.99% = $4,491. NOL carried forward $240,000, with no expiry.

```oa-check
name: GA 2026 NOL with the 80% limit
inputs:
  income_before_nol: 450000
  nol_available: 600000
  rate_2026: 0.0499
steps:
  - nol_used: min(nol_available, income_before_nol * 0.80)
  - ga_taxable: income_before_nol - nol_used
  - tax: ga_taxable * rate_2026
  - nol_carried: nol_available - nol_used
expected:
  nol_used: 360000
  ga_taxable: 90000
  tax: 4491
  nol_carried: 240000
```

**Case 3, the election: 2026 S corporation, two Georgia-resident shareholders at 50%, all income from Georgia, Georgia net income $500,000.** Electing: entity tax $500,000 x 4.99% = $24,950, paid by the entity (estimates as a C corporation, see `ga-estimated-tax-depth`); each shareholder subtracts $250,000 (PTEDED) and claims no Georgia credit; the entity deducts the Georgia tax federally in the year paid. Not electing: each shareholder pays Georgia tax on $250,000 on Form 500 (the same 4.99%), and the tax is a federal itemized deduction subject to the SALT cap. The Georgia total is the same either way; the decision turns on the federal deduction for each owner.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GAC-NEXUS | Nexus in doubt, including activity beyond solicitation under Public Law 86-272 and remote sellers of services | Refer |
| R-GAC-SOURCE | Sourcing of services and intangibles where customer location is unclear (Reg. 560-7-7-.03) | Refer |
| R-GAC-CONS | Consolidated return elections, terminations and intercompany transactions | Refer |
| R-GAC-382 | Section 381 and 382 limits after an ownership change; insurance-company or farm NOLs | Refer |
| R-GAC-CREDIT | Georgia credits. HB 463 repealed several for taxable years beginning on or after 1 January 2026, including the port activity credits (§§ 48-7-40.15, 40.15A), the headquarters credit (§ 48-7-40.18) and the alternative-fuel and electric-vehicle-charger credits (§ 48-7-40.16). Carryforwards, film credit, purchases and transfers | Refer |
| R-GAC-PTET | The election for owners with large non-Georgia income, other-state credits or other states' entity-level elections (§ 48-7-27(d)) | Refer |
| R-GAC-AUDIT | Federal audit adjustments and partnership audit elections; amended Georgia returns are due within 180 days of the final federal determination | Refer |
| R-GAC-SPECIAL | Insurance companies, financial institutions, exempt organizations (Form 600-T), fiduciaries (Form 501) | Refer |

## Filing and payment

Source: [2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download); [2025 IT-611S booklet](https://dor.georgia.gov/document/document/2025-it-611s-s-corporation-income-tax-booklet/download); [2025 IT-711 booklet](https://dor.georgia.gov/document/document/2025-it-711-partnership-income-tax-booklet/download); [DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates).

1. **Due dates:** Form 600, the 15th day of the 4th month after year-end (15 April 2027 for calendar 2026); Form 600S and Form 700, the 15th day of the 3rd month (15 March 2027). A weekend or holiday moves to the next business day.
2. **Extensions.** Corporations (Forms 600 and 600S): no Georgia request is needed with an automatic federal extension; there is no late-filing penalty if the return is received within the federal extended period plus one additional month, with Form 7004 attached (from tax years beginning 1 January 2025, HB 1023); Georgia law prohibits an extension of more than seven months. Partnerships (Form 700): within the federal extended period with Form 7004 attached, no extra month; no more than six months. Without a federal extension, use Form IT-303. Tick the "Extension" box, or a late-filing penalty is assessed.
3. **Payment is not extended.** Pay by the original due date with Form IT-560C (claimed on Form 600 Schedule 3 Line 2, or Form 600S Schedule 4 Line 2). Late payment penalty and interest run from the statutory due date.
4. **Electronic filing** is required if payments are made by electronic funds transfer, if the federal counterpart must be e-filed, or if any series 100 credit is used. File through the Georgia Tax Center or approved software, attaching a complete federal return including Schedule L.
5. **Penalties:** late filing 5% of the tax not paid by the original due date for each month or part month, up to 25%; late payment 0.5% a month up to 25%, not due if the return is amended because of an IRS audit; the two together cannot exceed 25%; negligent underpayment 5%; fraudulent underpayment 50%. Interest at the Federal Reserve prime rate plus 3%, reviewed each January.
6. **After filing:** refund claims within three years of the later of payment and the due date including extensions.

**2025 returns still open.** Rate 5.19% for C corporations, electing S corporations and electing partnerships. A calendar-2025 C corporation on federal extension avoids late-filing penalties if the return is received within one month after the federal extended date with Form 7004 attached; tax was due 15 April 2026 and interest runs from then. A calendar-2025 S corporation or partnership that wants the 2025 election must make it on the 2025 Form 600S or Form 700 by that return's due date or extended due date; DOR has not said whether the extra corporate month extends the S corporation election deadline, so elect by the federal extended due date. HB 1199 conformity applies to 2025 even though the 2025 booklets predate it.

## Completion checklist

- Rate 4.99% for years beginning in 2026 (5.19% for 2025), not prorated.
- Right form (600, 600S or 700); Form 600S-CA signed by every nonresident S corporation shareholder.
- Additions: 168(k) addback with Georgia depreciation, other-state income taxes, related-member intangible, interest and REIT addbacks, unauthorized-employee payments.
- Apportionment by gross receipts only; services and intangibles by customer location or market; partnership receipts pro rata.
- NOL: no carryback for losses from years ending after 2017; 80% limit for years beginning on or after 2018.
- Net worth tax computed in `ga-net-worth-tax` and on the same return.
- Election box ticked by the due date or extended due date; no composite return; owners told to use PTEDED or PTEADD and claim no Georgia credit.
- Paid by the original due date with IT-560C; extension box ticked; Form 7004 attached.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| HB 463 (2026). Read for the 4.99% rate for taxable years beginning on or after 1 January 2026, the statement that it reduces corporate and partnership rates, the 2027 cuts and the repealed credits. | https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download | 2026-11-13 |
| HB 111 (2025). Read for the 5.19% rate for 2025. | https://gov.georgia.gov/document/2025-signed-legislation/hb-111/download | 2026-11-13 |
| HB 1023 (2024). Read for the tie of the corporate and electing-entity rates to the individual rate and the extra extension month for corporations. | https://gov.georgia.gov/document/2024-signed-legislation/hb-1023/download | 2026-11-13 |
| HB 1199 (2026). Read for the IRC conformity date and the sections treated as not in effect or applied as before 2017. | https://gov.georgia.gov/document/2026-signed-legislation/hb-1199/download | 2026-11-13 |
| 2025 IT-611 corporate income tax booklet. Read for who must file, additions, apportionment, NOLs, consolidated returns, due dates and extensions. | https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download | 2026-11-13 |
| 2025 IT-611S S corporation booklet. Read for Form 600S-CA, nonresident withholding, the election schedules and due dates. | https://dor.georgia.gov/document/document/2025-it-611s-s-corporation-income-tax-booklet/download | 2026-11-13 |
| 2025 IT-711 partnership booklet. Read for the Form 700 election, due date and six-month extension limit. | https://dor.georgia.gov/document/document/2025-it-711-partnership-income-tax-booklet/download | 2026-11-13 |
| DOR HB 149 pass-through entity tax FAQ. Read for eligibility, timing, binding effect, PTEDED and PTEADD, attributes and estimates. | https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq | 2026-11-13 |
| DOR corporate income and net worth tax page. Read for the page as a whole. | https://dor.georgia.gov/taxes/corporate-income-and-net-worth-tax | 2026-11-13 |
| DOR penalty and interest rates. Read for the income tax penalty table and interest rule. | https://dor.georgia.gov/penalty-and-interest-rates | 2026-11-13 |
| IRS Notice 2020-75. Read for the entity-level deduction of a Specified Income Tax Payment and the SALT limitation rule. | https://www.irs.gov/pub/irs-drop/n-20-75.pdf | 2026-11-13 |

Not yet confirmed: the 2026 IT-611, IT-611S and IT-711 booklets were not published when read, so 2026 form line numbers are not confirmed; any 2027 rate depends on the 1 December 2026 Office of Planning and Budget report; whether the extra corporate extension month also extends the S corporation election deadline (DOR has not said).
