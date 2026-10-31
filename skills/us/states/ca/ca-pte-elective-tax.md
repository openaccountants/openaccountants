---
name: ca-pte-elective-tax
description: Tier 2 California content skill for the Pass-Through Entity Elective Tax (R&TC §§ 17052.10, 19900-19906; AB 150). Applies to S-corps, partnerships, and LLCs taxed as partnerships with at least one consenting individual, fiduciary, estate, or trust owner. Computes the 9.3% tax on qualified net income (each consenting owner's distributive share of CA-sourced income), produces Form 3804 entity election and Form 3804-CR owner-level nonrefundable credit, schedules the mandatory June 15 prepayment (greater of $1,000 or 50% of prior-year PTE tax) and the balance due by the original return due date, and flags the post-2025 sunset and the federal Notice 2020-75 SALT-cap workaround treatment. Tax year 2025.
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-10-19
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# California pass-through entity (PTE) elective tax

This skill covers the California pass-through entity elective tax (the "PTE elective tax", also called the "AB 150 tax" or the SALT-cap workaround) for a partnership, an LLC taxed as a partnership, or an S corporation, and the matching credit each consenting owner claims on a personal return. Figures are for tax year 2026. The election is available for 2026: the Franchise Tax Board (FTB) says qualifying entities "may annually elect" for "taxable years beginning on or after January 1, 2021, and before January 1, 2031", and that Senate Bill (SB) 132 "extended the PTE elective tax and credit for taxable years beginning on or after January 1, 2026, and before January 1, 2031" ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html); [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). The original AB 150 regime covered taxable years beginning before January 1, 2026; SB 132 is the extension, not a new tax. The main change for 2026 to 2030: a missed or short June 15 payment no longer blocks the election, it cuts the owners' credit instead.

Official pages were read on 19 October 2026: the FTB PTE elective tax page (last updated 04/23/2026), the FTB help and FAQ page (last updated 08/04/2026), the FTB business due dates page, the FTB penalties page, the FTB LLC and S corporation pages, IRS Notice 2020-75, and Public Law 119-21 on govinfo.gov. The California statute site (leginfo.legislature.ca.gov) refused our reader, so statute sections are cited only where an FTB page names them.

## The method, step by step

1. Confirm the entity is a qualified entity: taxed as a partnership or S corporation, not a publicly traded partnership, and not permitted or required to be in a combined reporting group. A disregarded entity can never elect. See the [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html).
2. List every direct owner and mark who can be a qualified taxpayer: an individual, fiduciary, estate or trust subject to California personal income tax, or a disregarded single-member LLC owned by one of those. Corporations and partnerships cannot be. See the [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html).
3. Collect written consent from each qualified taxpayer who wants in. Consent puts all of that owner's pro rata or distributive share and guaranteed payments into qualified net income (QNI). See the [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html).
4. Check the June 15 payment for the year of the election (for 2026: on or before June 15, 2026). The required amount is the greater of the floor and the prior-year share in the FTB table below. For 2026 a missed or short payment does not stop the election but triggers the credit reduction in Section 5.2. See the [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).
5. Compute QNI owner by owner: each consenting owner's share of income and guaranteed payments subject to California personal income tax. A nonresident's share uses the California sourcing rules; a negative share is left out. Apply the rate in the FTB table below. See the [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).
6. Make the election on the timely filed original return (Form 100S, Form 565 or Form 568) by attaching a completed Form 3804 and entering the PTE elective tax on the designated line. It cannot be made on an amended return. See the [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html).
7. Pay the balance by the original due date of the return without regard to extensions (15 March 2027 for a calendar-year 2026 return), by Web Pay, electronic funds withdrawal, or Form 3893 voucher, kept apart from the entity's other payments. See the [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) and [FTB business due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html).
8. On the entity's California return, add back any PTE elective tax deducted for federal purposes. On the federal Form 1065 or 1120-S, deduct the payment under IRS Notice 2020-75 in the year it is paid. See the [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) and [IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf).
9. Give each consenting owner the figures for Form 3804-CR. The owner claims the credit on Form 540, 540NR or 541, after the Other State Tax Credit (OSTC), and carries any unused credit forward for up to 5 years. See the [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html).

## Ask the client first

- Is the entity taxed as a partnership or S corporation, and is it in (or allowed to join) a combined reporting group? A disregarded single-member LLC or sole proprietor cannot elect at all.
- Who owns it directly? For each owner: individual, trust, estate, disregarded LLC (and who owns that LLC), corporation or partnership. For each individual: California resident, nonresident or part-year resident.
- Which owners will consent, in writing? Consent covers all of that owner's share, never part of it.
- What was paid as a PTE elective tax payment on or before June 15, 2026, and what PTE elective tax was paid for 2025? The answers set the required June 15 payment and any credit reduction.
- Is the entity a calendar-year or fiscal-year filer, and was its 2026 return (or a first return) already filed? This decides the due dates and whether a later return is superseding or amended.
- Is any nonresident owner in a group nonresident return, or subject to nonresident withholding? The credit cannot be claimed on a group return, and the election does not change withholding.

## Section 1. Scope

### 1.1 What this skill does

This skill prepares the PTE elective tax computation, the election, the payment schedule and the owner-level credit for a 2026 taxable year, with the rules that still matter for finishing 2025 returns. The election lets a qualified entity pay California tax at the entity level on each consenting owner's share of qualified net income. Each consenting owner gets a nonrefundable California credit for the tax paid on their share, claimed on Form 3804-CR. The federal reason for electing is that IRS Notice 2020-75 lets the entity deduct a state income tax it pays itself, outside the owner's SALT deduction limit under IRC § 164(b)(6). The federal limit for 2026 is in the table in Section 8.

### 1.2 Statutory authority

- **R&TC § 17052.10.** Owner-level PTE elective tax credit (FTB help page).
- **R&TC § 17052.11 and Part 10.4.1 (including § 19914(b)).** Added by SB 132 for taxable years beginning on or after January 1, 2026, and before January 1, 2031; § 19914(b) lets an entity elect despite a missed June 15 payment, and § 17052.11 reduces the credit (FTB help page).
- **R&TC § 17039.** Credit ordering: the PTE credit falls under § 17039(a)(7) from 2022 and under (a)(8) for taxable years on or after January 1, 2026, after the OSTC (FTB help page).
- **AB 150, SB 113, SB 851, SB 132.** The FTB PTE elective tax page lists these four bills as the related law.
- **IRS Notice 2020-75 (November 9, 2020).** Federal treatment of the entity-level payment.

The live version of this skill also cited R&TC §§ 19900 to 19906 by subsection. The FTB pages read for this rewrite do not name those subsections and the statute site could not be read, so the subsection references are not repeated here.

### 1.3 What this skill does NOT cover

1. California nonresident group returns (Form 540NR group return). The entity may file one, but the PTE credit cannot be claimed on it (Section 7.3).
2. Nonresident withholding (Forms 592, 592-PTE, 592-B). The election does not change it (Section 7.3).
3. Tiered structures beyond the owner test: an upper-tier partnership is not a qualified taxpayer; the lower tier may still elect for its other owners.
4. Publicly traded partnerships (excluded).
5. Disregarded entities other than a single-member LLC owned by an individual, fiduciary, estate or trust subject to California personal income tax.
6. Part-year resident sourcing. Which part of a part-year resident's share is subject to California tax is decided in `ca-residency-leaving-california`; this skill takes that answer as its input.
7. Other states' elective entity taxes: see `us-pte-state-matrix`.

### 1.4 Assumed companion skills

This skill runs with `us-tax-workflow-base`. It usually runs alongside:

- `ca-540-individual-return`: owner-level Form 540 claiming the credit.
- `ca-estimated-tax-540es`: owner estimated payments after the credit.
- `ca-smllc-form-568` and `ca-llc-fee-and-tax`: LLC annual tax and fee.
- `us-form-1065-partnership` and `us-federal-return-assembly`: the federal entity return with the Notice 2020-75 deduction.
- `us-s-corp-election-decision`: where a single-member LLC owner is weighing S corporation status, the PTE election is one input.
- `us-2026-federal-tax-changes`: the federal SALT limit after Public Law 119-21.
- `ca-residency-leaving-california`: residency and source of income for part-year and nonresident owners.

## Section 2. Eligibility

Two tests must BOTH be met: the entity must be a qualified entity, AND at least one owner must be a qualified taxpayer who consents. Only consenting owners' shares go into QNI. Non-consenting owners are left out of QNI, but the election still binds them.

### 2.1 Qualified entities

A qualifying PTE is "an entity taxed as a partnership or S corporation". It does not include publicly traded partnerships or "An entity permitted or required to be in a combined reporting group" ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)). An entity can be a qualified entity even if it has a disregarded entity or a partnership as an owner ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

**Eligible entity types** ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html))

| Federal classification | California return | Can elect? |
| --- | --- | --- |
| S corporation (Form 1120-S) | Form 100S | Yes |
| Partnership or multi-member LLC taxed as a partnership (Form 1065) | Form 565 or Form 568 | Yes |
| LLC taxed as an S corporation | Form 100S | Yes |
| Sole proprietorship (Schedule C) | None at entity level | No |
| Single-member LLC disregarded for federal tax | Form 568 | No: "A disregarded entity cannot be a qualified entity" |
| C corporation | Form 100 | No |
| Publicly traded partnership | Form 565 | No |
| Entity permitted or required to be in a combined reporting group | Varies | No |

- **Single-member LLCs.** A disregarded single-member LLC is not taxed as a partnership or S corporation, so it cannot elect. To use the election, the owner would have to (a) elect S corporation treatment (see `us-s-corp-election-decision`) or (b) add a member and become a partnership. Either is a separate decision with its own costs.
- **Sole proprietors.** No entity, no election.

### 2.2 Qualified taxpayers

A qualified taxpayer is a partner, member or shareholder of an electing qualified entity that is "An individual, fiduciary, estate, or trust subject to California personal income tax" or "A disregarded single member LLC that is owned by an individual, fiduciary, estate, or trust subject to California personal income tax". A qualified taxpayer is not a corporation, a partnership, or any other disregarded business entity ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)).

**Eligibility chart for owners** ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html))

| Owner type | Qualified taxpayer? |
| --- | --- |
| Individual, California resident | Yes |
| Individual, nonresident with income subject to California tax | Yes, on the share subject to California tax |
| Individual, part-year resident | Yes, on the share subject to California tax (see `ca-residency-leaving-california`) |
| Grantor trust | Yes: it may consent, and the grantor may generally claim the credit |
| Trust within the R&TC § 17004 definition of "taxpayer" | Yes |
| Estate | Yes |
| Disregarded single-member LLC owned by an individual, fiduciary, estate or trust subject to California personal income tax | Yes |
| Disregarded single-member LLC owned by a partnership or corporation | No |
| C corporation or S corporation owner | No |
| Partnership or LLC taxed as a partnership | No |

- **Tiered structures.** If a partnership owns part of the electing entity, the entity can still elect, but only the consenting qualified taxpayers' shares are in QNI. The partnership owner's share gets no PTE tax and no credit. FTB example: Partnership A can elect if it has another owner that is a qualified taxpayer, even where a disregarded LLC owned by Partnership B is a partner; that LLC is not a qualified taxpayer ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

### 2.3 Consent mechanics

To be a qualified taxpayer, the owner "must consent to have all of their pro rata or distributive share and guaranteed payments included in the qualified net income" ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)). Consent is all of the share or none of it. The election is annual, so consent is given year by year: in the FTB credit-reduction example, four partners consent for 2025 and only three for 2026 ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). Once a valid election is made, the entity cannot later amend Form 3804 to change the consenting owners. A non-consenting owner is left out of QNI and pays California tax on that share in the ordinary way.

## Section 3. Election mechanics

### 3.1 How the election is made

For 2026 to 2030 taxable years (beginning on or after January 1, 2026, and before January 1, 2031), the election must be made on a timely filed original return by filing a completed Form 3804 with the entity's return and including the PTE elective tax amount on the designated line of that return, and the entity must make the required initial payment by June 15 of the taxable year of the election. "However, if the June 15 payment is missed or less than the required amount, the qualified entity may still make a PTE elective tax election" ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)). The election is annual. An entity that elected for 2025 must elect again for 2026.

For 2022 to 2025 taxable years the same return rule applied, AND the June 15 payment was a condition of the election (Section 5.2).

### 3.2 Irrevocability and superseding returns

- **Irrevocable.** "Once the election is made, it is irrevocable for that year and is binding on all consenting and nonconsenting partners, shareholders, or members of the qualified entity." It "cannot be made on an amended return" ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)).
- **Superseding returns.** The election can be made, or revoked, on a superseding return. A return is superseding only if (1) the first return and the superseding return were both filed before the original due date, or (2) the original return and the superseding return were both filed on extension. A second return filed after the original due date, when the first was filed on or before it, is an amended return and cannot elect. A second return filed after the extended due date cannot elect ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- **Later changes to income.** If the entity's taxable income later changes, the entity must revise QNI and pay the extra tax or claim the refund; penalties and interest apply to any underpaid amount; the owners must amend with an amended Form 3804-CR and amended Schedule P, Part III. The change can also alter the required June 15 payment for the next year ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

### 3.3 Timing of the election decision

The election is made on the original return filed by the extended due date. For a calendar-year 2026 entity, from the [FTB business due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html) page:

| Entity | Return due | Extended due date |
| --- | --- | --- |
| S corporation (Form 100S) | 15th day of the 3rd month after the close of the tax year (15 March 2027) | 15th day of the 9th month after the close (15 September 2027) |
| Partnership (Form 565) | 15th day of the 3rd month after the close (15 March 2027) | 15th day of the 10th month after the close (15 October 2027) |
| LLC classified as a partnership (Form 568) | 15th day of the 3rd month after the close (15 March 2027) | 15th day of the 10th month after the close (15 October 2027) |

When a due date falls on a weekend or holiday, the next business day counts ([FTB business due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html)).

**Workflow for a calendar-year 2026 election** ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html))

| Date | Action |
| --- | --- |
| Early 2026 | Estimate QNI; identify consenting owners. |
| On or before June 15, 2026 | Payment 1: the greater of the floor and the prior-year share in the FTB table in Section 5. Errors in this payment must be corrected on or before June 15 to meet the statutory requirement. |
| December 31, 2026 | Tax year closes; finalise QNI. Pay any further amount before year end if the federal deduction is wanted in 2026 (Section 8.3). |
| On or before 15 March 2027 | Payment 2: the remaining PTE elective tax, due on the original due date without regard to extensions. Election on the return if not extended. |
| 15 September 2027 (Form 100S) or 15 October 2027 (Form 565 and 568) | Last day to make the election on a timely filed extended original return. |

For a 2025 return still being finished: the 2025 June 15 payment was a condition of the election, and the extended due dates are the 2026 equivalents of the rows above (the FTB due dates page gives an S corporation's 2025 calendar-year return due date as March 16, 2026).

### 3.4 Form 3893, Form 3804 and Form 3804-CR

- **Form 3893 (Pass-Through Entity Elective Tax Payment Voucher).** For payments by voucher. The FTB lists a 2026 version. Payments by Web Pay or electronic funds withdrawal must be designated as a "PTE payment", and then no Form 3893 is filed. Use separate vouchers or transactions for each tax year. PTE payments cannot be combined with the entity's other tax payments. Mail address on the FTB page: Franchise Tax Board, P.O. Box 942857, Sacramento, CA 94257-0531 ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- **Form 3804 (Pass-Through Entity Elective Tax Calculation).** Attached to Form 100S, 565 or 568; it is the election. The 2026 Form 3804 computes the reduced credit where the June 15 payment was short.
- **Form 3804-CR (Pass-Through Entity Elective Tax Credit).** Filed by each consenting owner with Form 540, 540NR or 541.

## Section 4. Rate and qualified net income calculation

**FTB PTE elective tax page: rate and payment figures**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html |
| PTE elective tax rate, on qualified net income | 9.3% | "The PTE elective tax is 9.3% of the qualified entity's qualified net income" |
| June 15 payment: minimum (taxable years 2022 to 2030) | USD 1,000 | "Pay $1,000 or 50% of the PTE elective tax paid for the prior taxable year, whichever is greater." |
| June 15 payment: share of the prior taxable year's PTE elective tax paid | 50% | "Pay $1,000 or 50% of the PTE elective tax paid for the prior taxable year, whichever is greater." |
| Credit reduction, 2026 to 2030 taxable years, applied to each owner's pro rata share of the unpaid June 15 amount | 12.5% | "must reduce their PTE elective tax credit by 12.5% of their pro rata share of the unpaid amount that was due on June 15" |

### 4.1 Rate

The rate is in the table above. It applies to the whole of QNI; there are no brackets. Owners whose personal California rate is higher pay the difference on their own return; the credit is limited to the tax paid on their share.

### 4.2 Qualified net income (QNI)

- **Definition.** QNI is "the sum of the pro rata or distributive share and guaranteed payments of each qualified taxpayers' income subject to California personal income tax" ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)). Only consenting owners' shares are included.
- **Nonresident owners.** QNI includes only the consenting nonresident's share "subject to the California personal income tax, which would be determined by using applicable sourcing rules as necessary" ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- **Resident owners.** A California resident is taxable "upon their entire net income, regardless of whether derived from sources within or without the State" ([18 CCR § 17014, LII mirror](https://www.law.cornell.edu/regulations/california/18-CCR-17014)). So a resident's share subject to California personal income tax is the whole share, not the California-apportioned share.
- **Which K-1 lines.** For an S corporation, the sum of Schedule K-1 (100S) income lines 1 to 10 minus deduction lines 11 and 12. For a partnership, the sum of Schedule K-1 (565/568) lines 1, 2, 3 and 4c through 11 minus deduction lines 12 and 13. All items of the share count even if not on those lines, for example IRC § 179 recapture and gain on disposal of § 179 property ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- **Gains.** Gain on the entity's sale of an entity-level asset is in QNI. Gain or loss on an owner's sale of their interest (partnership or LLC interest, S corporation stock) is owner-level and is NOT in QNI ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- **Negative shares.** If an owner's share of the items is negative, that share is left out of QNI and that owner gets no credit ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). Negative shares are not netted against other owners' positive shares.

### 4.3 Per-owner computation

For each consenting owner: tax on that owner = the owner's QNI × the rate in the Section 4 table. Entity PTE elective tax = the sum over consenting owners. The owner's credit is the tax on that owner's share, not a pro rata cut of the entity total, so owners with equal percentages can get different credits when one is a resident and one is not (Example B in Section 10).

## Section 5. Payment schedule

Two payments: Payment 1 on or before June 15 during the taxable year of the election, and Payment 2, the remaining amount, on or before the due date of the original return without regard to extensions ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)).

### 5.1 June 15 payment

- **Amount.** The greater of the floor and the prior-year share in the Section 4 table. An entity that paid no PTE elective tax for the prior taxable year (for example, a first election) owes the floor. The prior-year figure is the PTE elective tax PAID for the prior taxable year. A one-time sale in the prior year can raise it; "There are no statutory exceptions" for an unusually high prior year ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- **Weekend rule.** When June 15 falls on a weekend or holiday, a payment on the next business day is timely ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)).
- **Short first year.** "Qualified entities whose taxable year does not include June 15 in its short period taxable year are not subject to the June 15 payment requirement for that taxable year" ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- **No carry-forward as Payment 1.** An overpayment cannot be carried forward and designated as a June 15 payment or as PTE elective tax for a later year. It can be applied to the next year's LLC annual tax or fee, or an S corporation's next estimated tax ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- **Disasters.** No statutory exceptions, but a declared federal or state disaster covering the entity's principal place of business may give more time to pay or file ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

### 5.2 Consequences of a missed or short June 15 payment

| Taxable years beginning | What happens | Source |
| --- | --- | --- |
| On or after January 1, 2022, and before January 1, 2026 | The entity "may not make the PTE elective tax election for that taxable year". Paying late does not cure it. | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| On or after January 1, 2026, and before January 1, 2031 | The entity "may still make the PTE elective tax election", but each qualified taxpayer's credit is reduced by the percentage in the Section 4 table times their pro rata share of the amount due but not paid (R&TC § 17052.11; election allowed by § 19914(b)). | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |

For a 2026 election with a missed or short June 15 payment, do not default to "no election". Compute the reduced credit (Example A2 in Section 10) and compare it with not electing.

### 5.3 Balance due at the original return due date

Payment 2 is due on or before the due date of the original return without regard to extensions (15 March 2027 for a calendar-year 2026 entity). The FTB says "the correct amount of tax must be paid by the due date of the original return" and "Applicable penalties and interest will apply to underpaid amounts"; the FTB pages tie the loss of the election (2022 to 2025) or the credit reduction (2026 to 2030) to the June 15 payment only, and do not say what a short Payment 2 does to the election ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). An LLC's annual tax and fee have their own dates (Section 7.1).

### 5.4 Interest and penalties on PTE tax

**FTB penalties page: late payment penalty**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html |
| Late payment penalty, underpayment part (R&TC § 19132) | 5% | "Penalty 5% of the unpaid tax (underpayment), and 0.5% of the unpaid tax for each month or part of the month" |
| Late payment penalty, monthly part, for at most 40 months | 0.5% | "0.5% of the unpaid tax for each month or part of the month" |
| Late filing penalty maximum (a different penalty, for a late return) | 25% | "for each month or part of a month unpaid The maximum penalty is 25%." |

- **Interest** runs on underpaid tax. The FTB interest-rate page refused our reader, so no rate is given here; take the current rate from the FTB at the time of computation.
- **Estimated tax.** The PTE elective tax liability is not included in the qualified entity's estimated tax under R&TC § 19136 ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

## Section 6. Owner credit (Form 3804-CR)

### 6.1 Mechanics of the credit

The credit equals the owner's share of income and guaranteed payments subject to the election, multiplied by the rate in the Section 4 table ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)), less any 2026 to 2030 reduction for a short June 15 payment. It is claimed on Form 3804-CR with Form 540, 540NR or 541. An owner who consented to a valid election but did not claim the credit may amend to claim it, attaching Form 3804-CR. If an owner reports too much credit, the FTB disallows the excess.

### 6.2 Nonrefundable, with a 5-year carryover

"Qualified taxpayers are eligible to claim a nonrefundable credit" and "Unused credits can be carried over for up to 5 years" ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)). The carryover period is not affected by the repeal of the credit: an unused credit can be carried into years when the PTE credit is not operative ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). The credit is not subject to the R&TC § 17039.4 credit limitation (FTB help page).

A consenting owner with little California tax (a nonresident with a small California share, or an owner with losses elsewhere) may not be able to use the credit in the year. Model that before advising consent.

### 6.3 Ordering rules: PTE credit and the Other State Tax Credit (OSTC)

- **Order.** Under R&TC § 17039, the PTE credit falls under § 17039(a)(7) for taxable years beginning on or after January 1, 2022, and under (a)(8) for taxable years on or after January 1, 2026, and "both must be applied after the Other State Tax Credit (OSTC)" ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- **OSTC add-back.** "For taxable years beginning on or after January 1, 2022, and before January 1, 2031", to calculate the OSTC, taxpayers must increase the "net tax payable" by the amount of PTE credit that reduced net tax, before application of the OSTC, in the same taxable year ([FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)). The live version of this skill attributed this rule to SB 851; the FTB pages list SB 851 as related law but do not tie it to this rule.

### 6.4 Tentative minimum tax and the behavioral health services tax

- "Yes, the PTE elective tax credit may reduce the amount of tax due below the TMT" ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).
- The credit cannot reduce the behavioral health services tax (formerly the mental health services tax) under R&TC § 17043(c)(1); the rate is in the FTB help page table in Section 7.3. So that tax is still owed by a high-income owner, and the credit does not change the estimated payments due for it ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

### 6.5 Trust and estate owners

A trust or estate that consents claims the credit on Form 541. "Generally, estates or trusts are able to pass credits through to beneficiaries." A grantor trust may consent, and "The grantor may generally claim the credit received from the trust on their return" ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). Complex trusts with large distributions need a fiduciary specialist.

## Section 7. Interactions with other California taxes

### 7.1 LLCs: PTE tax is in addition to the LLC annual tax and fee

For an LLC classified as a partnership (Form 568), the PTE elective tax is separate from the annual tax (Form 3522, due the 15th day of the 4th month after the beginning of the tax year) and the LLC fee (estimate on Form 3536 by the 15th day of the 6th month of the current tax year) ([FTB business due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html)). For the fee bands, first-year rules and penalties, use `ca-llc-fee-and-tax`.

**FTB business due dates page and FTB LLC page: LLC annual tax and fee**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html |
| LLC fee, total California income USD 250,000 to USD 499,999 | USD 900 | "$250,000 - $499,999 $900 $500,000 - $999,999 $2,500" |
| LLC fee, total California income USD 500,000 to USD 999,999 | USD 2,500 | "$500,000 - $999,999 $2,500 $1,000,000 - $4,999,999 $6,000" |
| LLC fee, total California income USD 1,000,000 to USD 4,999,999 | USD 6,000 | "$1,000,000 - $4,999,999 $6,000 $5,000,000 or more $11,790" |
| LLC fee, total California income USD 5,000,000 or more | USD 11,790 | "$5,000,000 or more $11,790" |

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html |
| LLC classified as a partnership: annual tax | USD 800 | "Annual tax Your annual tax amount is $800." |

### 7.2 S corporations: PTE tax is in addition to the S corporation tax

For an S corporation (Form 100S), the PTE elective tax is separate from the S corporation tax on California source income and the minimum franchise tax. The owner credit on Form 3804-CR is only for the PTE elective tax, not for the S corporation tax.

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.ftb.ca.gov/file/business/types/corporations/s-corporations.html |
| S corporation tax rate on California source income | 1.5% | "We tax every S corporation that has California source income 1.5%." |
| Minimum franchise tax | USD 800 | "Your minimum franchise tax ($800) is due the first quarter" |

### 7.3 Group returns and nonresident withholding

- **Group nonresident return.** "The partnership/S corporation/LLC can file a group return, but the PTE elective tax credit cannot be claimed on a group return because it is not a flow-through item from the qualified entity. The PTE elective tax credit is available only on the individual return of the qualified taxpayer" ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). A nonresident who wants the credit must file their own Form 540NR.
- **Nonresident withholding.** The election does not change the withholding requirement (rate in the table below). PTE payments do not count as withholding.

**FTB help page: figures**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html |
| Nonresident withholding requirement, unchanged by the election | 7% | "The qualified entities’ election does not affect the 7% withholding requirement." |
| Behavioral health services tax, which the credit cannot reduce | 1% | "The PTE elective tax credit cannot reduce the 1% behavioral health services tax" |

### 7.4 Owner estimated tax (Form 540-ES)

The FTB says "the PTE elective tax credit does reduce the computation of estimated payments for qualified taxpayers" ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). Size the owner's 540-ES payments on tax after the expected credit, and keep the behavioral health services tax in the computation. See `ca-estimated-tax-540es`.

## Section 8. Federal treatment

### 8.1 IRS Notice 2020-75

The Notice (November 9, 2020) says "Specified Income Tax Payments ... are deductible by partnerships and S corporations in computing their non-separately stated income or loss". A Specified Income Tax Payment includes an amount paid by a partnership or S corporation to a state under a direct imposition of income tax on the entity "without regard to whether the imposition of and liability ... for the income tax is the result of an election by the entity". It "does not constitute an item of deduction that a partner or an S corporation shareholder takes into account separately under section 702 or section 1366" ([IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf)). The California PTE elective tax is an elective entity-level income tax of that kind.

### 8.2 Practical federal mechanics

1. The entity pays PTE elective tax.
2. The entity deducts the amount paid in the year in computing non-separately stated income on Form 1065 or 1120-S.
3. Owners' K-1s carry the lower ordinary income.
4. Owners do not deduct the PTE tax again on Schedule A; they did not pay it.
5. On the California side, the entity adds back the PTE elective tax it deducted federally in computing its California net income ("If the qualified entity deducts the PTE elective tax for federal purposes, the amount of the PTE elective tax that was deducted is added back for California purposes", [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html)). The owner is taxed in California on the full share and takes the credit.

The benefit depends on how much of the owner's own state and local taxes the federal limit would disallow. The 2026 federal limit is in the table below; for its detail see `us-2026-federal-tax-changes`.

**Public Law 119-21 (One Big Beautiful Bill Act): SALT limit under IRC § 164(b)(6) and (7)**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm |
| SALT limit, taxable years beginning in 2026 (half for married filing separately) | USD 40,400 | "in the case of any taxable year beginning in calendar year 2026, $40,400" |
| MAGI threshold for the phase-down, taxable years beginning in 2026 | USD 505,000 | "in the case of any taxable year beginning in calendar year 2026, $505,000" |
| Phase-down rate on MAGI above the threshold | 30 percent | "reduced by 30 percent of the excess (if any) of the taxpayer's modified adjusted gross income over the threshold amount" |
| Floor of the phase-down | USD 10,000 | "shall not result in the applicable limitation amount being less than $10,000" |
| SALT limit, taxable years beginning in 2025 | USD 40,000 | "in the case of any taxable year beginning in calendar year 2025, $40,000" |

### 8.3 Timing of the federal deduction

Under the Notice, "the partnership or S corporation is allowed a deduction for the Specified Income Tax Payment in computing its taxable income for the taxable year in which the payment is made" ([IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf)). So the June 15, 2026 payment and anything else paid by December 31, 2026 is a 2026 deduction; Payment 2 made in March 2027 is a 2027 deduction. An entity that wants the whole federal deduction in 2026 must pay by December 31, 2026.

### 8.4 No federal owner credit

The PTE tax is not a separately stated item on the federal K-1. The owner's Form 3804-CR credit is a California item only.

### 8.5 Excess business loss limitation (IRC § 461(l))

The entity-level deduction lowers each owner's share of non-separately stated business income, which is an input to the excess business loss test. Loss-year entities rarely elect, because a negative share gives no credit (Section 4.2). For the full test use `us-tax-workflow-base`.

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf |
| Excess business loss threshold, 2026, other than joint | USD 256,000 | "is $256,000 ($512,000 for joint returns)" |
| Excess business loss threshold, 2026, joint returns | USD 512,000 | "is $256,000 ($512,000 for joint returns)" |

## Section 9. Sunset and legislative outlook

### 9.1 Statutory period

| Taxable years beginning | Status | Source |
| --- | --- | --- |
| On or after January 1, 2021, and before January 1, 2022 | Election on the original return; no June 15 payment; pay by the original due date | [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |
| On or after January 1, 2022, and before January 1, 2026 | Election plus June 15 payment as a condition | [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |
| On or after January 1, 2026, and before January 1, 2031 (SB 132) | Election available; short June 15 payment reduces the credit | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |

**Fiscal-year filers.** The third change made by SB 132: "the credit under both R&TC sections 17052.10 and 17052.11 is allowed for the 2026 and 2031 taxable years, respectively, in situations where the qualified entity making the PTE elective tax election is a fiscal year filer and has a different taxable year beginning than its qualified taxpayer" ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). Our reading, not FTB wording: a calendar-year owner of a fiscal-year entity whose year began in 2025 can still claim the credit on the owner's 2026 return. Confirm against R&TC sections 17052.10 and 17052.11 before relying on it.

### 9.2 Link to the federal SALT limit

The election exists because of the federal SALT limit. Under Public Law 119-21 the limit is higher for 2025 to 2029 than before and returns to a lower amount from 2030 (table in Section 8.2 and `us-2026-federal-tax-changes`). An owner whose own state and local taxes fit under the higher limit gains less from electing. Recheck the federal side every year.

### 9.3 Status on 19 October 2026

The election and credit are in force for taxable years beginning before January 1, 2031, per the FTB pages above. For 2025 returns, the 2025 June 15 payment was a condition. For 2026 to 2030, a missed or short June 15 payment reduces the credit rather than blocking the election. Tell the client both points in writing.

## Section 10. Worked examples

All examples are hypothetical except Examples A and A2, which are the FTB's own example. People and amounts are invented; the rate is the one in the Section 4 table.

### 10.1 Example A: FTB Partnership A, 2025 election

Partnership A has four equal partners, W, X, Y and Z. All four consent for 2025 ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

| Step | Amount | Source |
| --- | --- | --- |
| 2025 QNI | USD 500,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| 2025 PTE elective tax (QNI × the rate) | USD 46,500 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Required June 15, 2026 payment (the greater of the floor and half of the 2025 tax) | USD 23,250 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |

### 10.2 Example A2: FTB Partnership A, 2026 election with a short June 15 payment

Partnership A pays only part of the required amount on June 15, 2026. Only X, Y and Z consent for 2026, each with a share of income and guaranteed payments as below. The partnership elects on its timely filed original return and pays the balance ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)).

| Step | Amount | Source |
| --- | --- | --- |
| June 15, 2026 payment made | USD 10,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Share of each of X, Y and Z | USD 100,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| 2026 QNI | USD 300,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| 2026 PTE elective tax | USD 27,900 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Credit per partner before reduction | USD 9,300 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Reduction per partner: 12.5% × (USD 23,250 minus USD 10,000) × USD 100,000 / USD 300,000 | USD 552 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Credit allowed to each of X, Y and Z for 2026 | USD 8,748 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |

The FTB rounds the reduction to whole dollars (the unrounded figure is a little above it). W did not consent for 2026 and gets no 2026 credit, but is bound by the election.

### 10.3 Example B: S corporation, one resident and one nonresident shareholder (hypothetical)

An S corporation (Form 100S) has two individual shareholders: Chris, a California resident, 60%, and Dana, a Nevada resident, 40%. 2026 ordinary income USD 400,000, of which 75% is California source. Both consent. ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html))

| Step | Amount | Source |
| --- | --- | --- |
| Chris: whole share (resident, 60% of USD 400,000) | USD 240,000 | [18 CCR § 17014](https://www.law.cornell.edu/regulations/california/18-CCR-17014) |
| Dana: California-source share only (40% of 75% of USD 400,000) | USD 120,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| QNI of both owners together | USD 360,000 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| PTE elective tax at the rate in the Section 4 table | USD 33,480 | [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |
| Chris's credit | USD 22,320 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |
| Dana's credit | USD 11,160 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |

Dana files Form 540NR to claim the credit. If her California tax on her California-source income is lower than her credit, the excess is not refunded; she carries it forward for up to 5 years and loses it if she has no later California tax. Model this before she consents. The S corporation also owes its own S corporation tax (Section 7.2), which gives no owner credit.

### 10.4 Example C: Tiered partnership (hypothetical)

An LLC taxed as a partnership has 2026 California-source ordinary income of USD 1,000,000. An upper-tier LLC taxed as a partnership owns 30%; seven California-resident individuals own 10% each, and all seven consent. ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html))

| Step | Amount | Source |
| --- | --- | --- |
| Share of the upper-tier partnership (30%), excluded | USD 300,000 | [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |
| QNI: consenting individuals (70%) | USD 700,000 | [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |
| PTE elective tax | USD 65,100 | [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |
| Credit per consenting individual (each 10%, share USD 100,000) | USD 9,300 | [FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) |

The upper tier's share gets no PTE tax and no credit; its own members pay California tax on it personally. Restructuring the upper tier is a multi-year, multi-entity question and out of scope.

### 10.5 Example D: Disregarded single-member LLC owned by an individual (hypothetical)

A partnership has 2026 California-source income of USD 800,000. One partner (25%) is Erin Single LLC, a disregarded single-member LLC wholly owned by Erin, a California resident. The LLC's share is USD 200,000. ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html))

| Step | Amount | Source |
| --- | --- | --- |
| QNI attributable to Erin's LLC | USD 200,000 | [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |
| PTE elective tax on that share, and the credit | USD 18,600 | [FTB PTE elective tax page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) |

The single-member LLC is a qualified taxpayer because it is owned by an individual subject to California personal income tax ([FTB help page](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html)). Erin claims the credit on her Form 540 with Form 3804-CR. Record both the LLC and Erin on the consent register, so the credit can be matched to the person who files the personal return; follow the 2026 Form 3804 instructions on how to list them.

### 10.6 Part-year resident owner

The live version of this skill had a part-year resident example with a residence-period split. The FTB pages read for this rewrite do not set out how QNI is split for a part-year resident beyond "income subject to California personal income tax". Take the owner's California-taxable share from `ca-residency-leaving-california` and apply Section 4.3.

## Section 11. Common errors and reviewer checks

- **Check 301.** June 15 payment. Confirm the amount (Section 5.1) and the date. For 2025 a short payment blocks the election. For 2026 to 2030 it keeps the election but reduces the credit (Section 5.2). Match the voucher or electronic payment designated as a "PTE payment" to the FTB account.
- **Check 302.** Prior-year PTE tax used for the June 15 amount is the tax PAID for the prior year, from the prior-year Form 3804 and account.
- **Check 303.** Every consenting owner is a qualified taxpayer (Section 2.2). No corporation, partnership or disregarded entity owned by one.
- **Check 304.** Form 3804 total ties to the PTE line on Form 100S, 565 or 568, and per-owner amounts add to the entity total.
- **Check 305.** Each consenting owner has a Form 3804-CR matching Form 3804 (after any 2026 reduction).
- **Check 306.** Nonresident QNI uses only the share subject to California tax under the sourcing rules.
- **Check 307.** Resident QNI uses the whole share.
- **Check 308.** Guaranteed payments to consenting partners are in QNI.
- **Check 309.** Partnership and corporate owners are excluded from QNI.
- **Check 310.** The election was made on a timely filed original or superseding return, not an amended one (Section 3.2).
- **Check 311.** Payment 2 paid by the original due date without extensions; otherwise penalties and interest (Section 5.4).
- **Check 312.** Unused credit carryover recorded per owner with its 5-year limit.
- **Check 313.** PTE credit applied after the OSTC, with the "net tax payable" add-back in the OSTC computation.
- **Check 314.** Federal deduction taken at the entity level under Notice 2020-75.
- **Check 315.** Federal deduction in the year paid (Section 8.3).
- **Check 316.** Entity is not a publicly traded partnership and not in, or eligible for, a combined reporting group.
- **Check 317.** Entity is not a disregarded single-member LLC trying to elect.
- **Check 318.** Written consent on file for each consenting owner, covering all of that owner's share.
- **Check 319.** No consenting owner expects to claim the credit through a group nonresident return.
- **Check 320.** Nonresident withholding still made; the election does not change it.
- **Check 321.** Client told in writing that the election runs to taxable years beginning before January 1, 2031, and that a short June 15 payment for 2026 to 2030 reduces the credit.
- **Check 322.** Trust or estate owner: credit claimed on Form 541 or passed to beneficiaries; grantor trust credit on the grantor's return.
- **Check 323.** Negative shares excluded; no credit for those owners.
- **Check 324.** Disregarded single-member LLC owner: the individual behind it is identified on the consent register.
- **Check 325.** Part-year resident: share from `ca-residency-leaving-california`.
- **Check 326.** Federal deduction added back on the entity's California return.
- **Check 327.** Owner's sale of an interest kept out of QNI; entity asset sales kept in.
- **Check 328.** Owner estimated tax resized for the credit, keeping the behavioral health services tax.

## Section 12. Output specification

1. Eligibility memo: entity status and each owner's status, with reasons.
2. Consent register: per-owner consent and copies.
3. Form 3804: per-owner QNI and tax; for 2026 to 2030, any credit reduction.
4. Payment record: June 15 payment and Payment 2, by voucher (Form 3893) or electronic payment designated as a PTE payment.
5. Form 3804-CR figures per consenting owner.
6. Federal deduction memo: Notice 2020-75 deduction, year paid.
7. Handoffs: to `ca-540-individual-return` and `ca-estimated-tax-540es` (credit, OSTC interaction, estimated tax); to `us-form-1065-partnership` or `us-federal-return-assembly` (entity deduction); to `us-s-corp-election-decision` (where relevant).
8. Reviewer brief: Section 11 checks done, and the Check 321 disclosure.

## Section 13. Cross-skill references

Inputs from: entity bookkeeping (California-source income and apportionment); prior-year Form 3804 and FTB account; operating or shareholder agreement (ownership and consent); `ca-residency-leaving-california` (owner residency and source).

Outputs to: `ca-540-individual-return`, `ca-estimated-tax-540es`, `ca-smllc-form-568`, `ca-llc-fee-and-tax`, `us-form-1065-partnership`, `us-federal-return-assembly`, `us-ca-return-assembly`.

## Section 14. Known gaps and uncertainty flags

1. The R&TC text itself (Part 10.4 and Part 10.4.1) could not be read from leginfo.legislature.ca.gov; this skill relies on the FTB pages. Check the statute for any point the FTB pages do not address.
2. The 2026 Form 3804, 3804-CR and 3893 instructions were not read for this rewrite; follow them for line-by-line reporting, including how a disregarded LLC owner is listed.
3. FTB interest rates could not be read; take the rate at computation time.
4. Federal: Notice 2020-75 still governs the entity deduction as far as the pages read show. Recheck for later IRS guidance every year.
5. Part-year resident QNI split is not set out on the FTB pages.
6. Complex trusts: credit pass-through to beneficiaries is "generally" allowed; specialist review needed.

## When to refuse or refer

- Refer when the entity is in, or may be required or permitted to be in, a combined reporting group; or is a publicly traded partnership.
- Refer tiered structures where restructuring is being considered, and complex trusts with large distributions.
- Refer part-year resident owners whose California-taxable share is disputed (`ca-residency-leaving-california`).
- Refuse to state that an election made on an amended return is valid; the FTB page says it cannot be.
- Refuse to state that a 2022 to 2025 election survives a missed or short June 15 payment.
- Refer any question on federal treatment beyond Notice 2020-75 to `us-2026-federal-tax-changes` and a federal preparer.
- Refuse to sign off a return: this skill is a source-cited draft and needs review by a California CPA, EA or tax attorney.

## Sources

- [FTB: Pass-through entity elective tax](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/index.html) (last updated 04/23/2026)
- [FTB: Help with pass-through entity (PTE) elective tax](https://www.ftb.ca.gov/file/business/credits/pass-through-entity-elective-tax/help.html) (last updated 08/04/2026)
- [FTB: Due dates for businesses](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html)
- [FTB: Penalties and interest](https://www.ftb.ca.gov/pay/penalties-and-interest/index.html)
- [FTB: Limited liability company](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html)
- [FTB: S corporations](https://www.ftb.ca.gov/file/business/types/corporations/s-corporations.html)
- [18 CCR § 17014, LII mirror](https://www.law.cornell.edu/regulations/california/18-CCR-17014)
- [IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf)
- [Public Law 119-21 on govinfo.gov](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)
- [IRS Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
