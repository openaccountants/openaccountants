---
name: ny-pte-tax-ptet
description: NY Pass-Through Entity Tax (PTET) — Article 24-A
jurisdiction: US-NY
tax_year: 2026
last_updated: 2026-10-03
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New York pass-through entity tax (PTET) and New York City PTET

This Guide covers the New York State pass-through entity tax under Tax Law Article 24-A and the New York City pass-through entity tax under Article 24-B. It is for the preparer of a partnership or New York S corporation deciding whether to elect, and for the preparer of an owner's New York return. Figures are for tax year 2026. The rate table and payment rules below are the ones the Department of Taxation and Finance prints today; its pages carry no end year for them. The federal side (the SALT cap after the One Big Beautiful Bill Act) is covered in `us-2026-federal-tax-changes`. Other states' elective entity taxes are covered in `us-pte-state-matrix`; this Guide does not repeat that table.

Official pages were read on 3 October 2026. The main ones: the Department's [PTET page](https://www.tax.ny.gov/bus/ptet/) (updated April 3, 2026), its [calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm) (updated June 18, 2025), the [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm) (updated October 3, 2025) and the [NYC PTET page](https://www.tax.ny.gov/bus/ptet/city.htm) (updated April 3, 2026).

## The method, step by step

1. Confirm the entity is eligible. It must be a partnership with a New York filing requirement under Tax Law § 658(c)(1) that is not publicly traded, or a New York S corporation subject to the fixed dollar minimum tax under § 209. See [Department PTET page](https://www.tax.ny.gov/bus/ptet/).
2. List every direct owner. Mark which ones are taxable under Article 22 (individuals, estates, non-grantor trusts). Corporate partners, partnership partners and S corporation partners get no credit. See [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm).
3. For an S corporation, decide resident or standard. Resident status needs a certification at election time that all shareholders are New York residents. See [Department PTET page](https://www.tax.ny.gov/bus/ptet/).
4. Check the election window. The election runs from 1 January to 15 March of the PTET year, online only, made by an authorized person, not by the tax professional. The 2026 window has closed. See [Department PTET page](https://www.tax.ny.gov/bus/ptet/).
5. Estimate PTE taxable income on the Department's worksheet for the entity type, then apply the rate table. See [calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm).
6. If any partner is a New York City resident, or a resident S corporation has only city taxpayer shareholders, consider the NYC PTET in the same online election. See [NYC PTET page](https://www.tax.ny.gov/bus/ptet/city.htm).
7. Pay quarterly estimates by ACH debit through Web File. See [Department PTET page](https://www.tax.ny.gov/bus/ptet/).
8. File the annual PTET return online by 15 March after the PTET year, listing every eligible credit claimant. See [Department PTET page](https://www.tax.ny.gov/bus/ptet/).
9. Give owners their direct share of the PTET (IT-204-IP for partners, a statement for shareholders). Owners claim it on Form IT-653 and add it back with code A-219 on Form IT-225. See [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm).
10. Work the federal effect for each owner with `us-2026-federal-tax-changes`, using the deduction rule in [IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf).

## Ask the client first

- Who are the direct owners, and which of them are individuals, trusts or estates, as against corporations, partnerships or S corporations? Only direct owners taxable under Article 22 get a credit.
- For each individual owner: New York resident for at least half of the year, or not? For a city election: New York City resident for at least half of the year, or not?
- For an S corporation: are all shareholders New York residents now, so it can certify as a resident S corporation when it elects? Are all of them city taxpayers?
- Does the entity expect positive New York income this year, and can it fund the quarterly estimates in cash? A loss year means a refund by check, not a transfer to owners.
- Do any nonresident owners file through a group return (IT-203-GR or IT-203-S)? They cannot claim the credit there.
- Is the owner's federal state and local tax deduction actually limited by the 2026 cap? The answer decides whether the election saves federal tax; this Guide does not compute it. Check this with `us-2026-federal-tax-changes`.

## Scope

This Guide covers eligibility, the election, the resident and standard S corporation versions, PTE taxable income, the rate table, estimated payments, the annual return, the owner credit and add-back, the resident credit for other states' entity taxes, and the NYC PTET.

Not covered here, with the Guide to use instead:
- New York individual rates and the resident return: `ny-it-201-resident-return`.
- New York corporate franchise tax under Article 9-A: `ny-corporate-franchise-article-9a`.
- Federal SALT cap amounts and phase-down: `us-2026-federal-tax-changes`.
- Other states' elective entity taxes and whether an owner's home state credits New York PTET: `us-pte-state-matrix`.
- New York estimated tax for individuals (IT-2105): `ny-estimated-tax`.
- MCTMT: `ny-mctmt`.

Why the tax exists. Article 24-A was enacted in 2021 (Chapter 59 of the Laws of 2021, Part C, per [TSB-M-21(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m21-1c-1i.pdf)). The PTET is an optional tax for "tax years beginning on or after January 1, 2021" ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). The entity pays the tax. Under IRS Notice 2020-75 the payment is deducted by the entity and is not counted against the owner's federal SALT cap (see the federal section below). The owner then takes a refundable New York credit for the tax paid.

## Eligibility: who can elect

Eligible (both from the [Department PTET page](https://www.tax.ny.gov/bus/ptet/)):
- A partnership, including an LLC treated as a partnership for federal income tax purposes, that "has a filing requirement under Tax Law § 658(c)(1) and is not a publicly traded partnership". It may elect "even if it has partners that are not eligible for the PTET credit, including, but not limited to, corporate partners."
- A New York S corporation (including an LLC treated as an S corporation for New York and federal purposes) as defined by Tax Law § 208.1-A "that is subject to the fixed dollar minimum tax under Tax Law § 209." A federal S corporation with no nexus to New York is an ineligible corporation under § 620(b)(3)(B) and cannot elect.

Not eligible: "single-member LLCs (unless they elect to be treated as an S corporation for New York purposes)", sole proprietorships, trusts, non-profit corporations, and "corporations that are not New York S corporations" ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). A single-member LLC that is disregarded cannot elect; one that elects S corporation treatment for New York purposes can ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). So a single-shareholder New York S corporation can elect.

Owners who are not taxable under Article 22. A partnership that elects must include all partners taxable under Article 22, resident and nonresident. It cannot pick which partners take part ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). Income flowing to a corporate partner, a partnership partner, an S corporation partner or any other owner not taxable under Article 22 is left out of PTE taxable income, and that owner gets no credit. A partnership owned only by a partnership and a corporation may elect, but "will not have any PTE taxable income or PTET credits to distribute" ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). The live version of this Guide suggested carving tax-exempt partners out through the partnership agreement; the Department's pages give no such route, and none is needed, because owners not taxable under Article 22 are already outside the base.

## Election mechanics

Who elects. "Only an authorized person may make this election on behalf of an eligible partnership or eligible S corporation". "Tax professionals may not make this election on behalf of their clients." For a partnership, an authorized person is a member, partner, owner or other individual with authority to bind the entity and sign returns under Tax Law § 653. For an S corporation, it is an officer, manager or shareholder authorized under state law or the organizational documents, who represents that authority under penalty of perjury. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

When. "An eligible entity may opt in on or after January 1, but no later than March 15." If that date falls on a Saturday, Sunday or legal holiday, "the election is due on the next business day." ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) For the 2026 PTET year, 15 March 2026 was a Sunday, so the last day was Monday 16 March 2026, a date derived from the weekend rule above and not printed on any Department page. That window is closed: an entity that did not elect cannot elect for 2026. If the rules are unchanged, the 2027 window is 1 January 2027 to Monday 15 March 2027.

Every year. The election "must be made online on an annual basis". It does not carry over. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

Revoking. The election "is irrevocable after the due date of the entity's first PTET estimated payment." Until then, "The PTET election may be revoked at any time up until the due date of the first estimated payment, through the entity's Business Online Services account." An entity may not file a zero return to undo the election unless it truly has no PTE taxable income. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

No late election. Entities "formed after the annual election deadline" cannot opt in for that calendar year: "There are no tax law provisions to allow for a later opt-in deadline for newly formed entities." ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Fiscal years. A calendar-year entity elects, files and pays on a calendar-year basis. A fiscal-year entity elects, files and pays "for the calendar year in which its fiscal year ends." An entity with more than one short tax year in a calendar year makes one election only, for the first short year that ends in that calendar year. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Reorganizations. After a federal F reorganization of an electing S corporation, the election stays in effect for the successor. For a partnership, it stays in effect only if the successor continues the original partnership, the original files no final return, and all the year's income is reported on the successor's return. ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

## Resident vs standard S corporation election

Two kinds of electing S corporation ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)):
- Electing resident S corporation: one that "certifies at the time it elects to opt in to PTET that all of its shareholders are residents of New York State under Article 22."
- Electing standard S corporation: any other electing S corporation.

The live version of this Guide said all shareholders must be residents "for the entire tax year". The Department's test is a certification at the time of election that all shareholders are residents for Article 22 purposes. If shareholders may change residence during the year, refer the point (see the last section).

Why it matters. On the [calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm), the standard S corporation worksheet computes the New York share of each item "Using the apportionment rules of Article 9-A". The resident S corporation worksheet takes the full Schedule K-1 amounts. So a resident S corporation can bring all of its owners' share of income into the base, while a standard S corporation brings in only the apportioned New York share, even for shareholders who live in New York. Only a resident S corporation can also elect the NYC PTET.

Partnerships have no separate resident election. They classify each partner instead (next section).

## PTE taxable income calculation

General rule: PTE taxable income "includes all income, gain, loss, or deduction of an electing entity that flows through to a direct partner, member, or shareholder for New York State personal income tax purposes." A direct owner is one issued a federal Schedule K-1 by the entity; a K-1 issued to a disregarded entity counts as issued to the person who reports its activity. ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm))

Partnerships. Each direct partner taxable under Article 22 is classified as resident or nonresident. "Members or partners may not be classified as part-year residents for PTET purposes." A partner is a resident "if they are a resident of New York for New York personal income tax purposes for at least half of the year." A trust is classified by its own residency, not its beneficiaries'. The partnership computes two pools and adds them ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm)):
- Nonresident pool: New York source items of nonresident partners, under Article 22 sourcing rules.
- Resident pool: all items of resident partners.
Both pools are computed "without regard for any limitations" such as capital losses, passive activity losses and basis limits. Guaranteed payments are included "to the same extent they are taxable by New York at the individual partner level", and they count as special allocations. A loss in one pool offsets income in the other when totalling PTE taxable income; partners in a negative pool get no credit. ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Add-backs in the base. When computing PTE taxable income, the entity adds back "all pass-through entity taxes paid and deducted for federal purposes in the current year, including taxes paid to New York or to other jurisdictions", and NYC UBT payments deducted federally. An S corporation adds back NYC general corporation tax if computed on the entire net income or alternative base. ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Separately stated items. "Other deductions" on the K-1 reduce PTE taxable income and go on the worksheet as negatives ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Sale of the business. Gain on an asset sale that flows through on the K-1 and is taxable to the owner is included. Gain on the sale of an owner's interest, which is not on the K-1, is not included ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Lines 17a and 17b of each worksheet "apply to tax years 2021 and 2022 only. For 2023 and later, leave these lines blank." ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm))

## Rate schedule

The tax is computed on total PTE taxable income (line 18 of the worksheet). The Department prints the same table in [TSB-M-21(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m21-1c-1i.pdf).

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.tax.ny.gov/e-services/ptet/calculations.htm |
| First bracket ceiling | USD 2 million | "$2 million or less 6.85% of PTE taxable income." |
| Rate up to the first ceiling | 6.85% | "6.85% of PTE taxable income." |
| Tax at USD 2 million | USD 137,000 | "$137,000 plus 9.65% of the excess of PTE taxable income greater than $2 million." |
| Rate on income over USD 2 million up to USD 5 million | 9.65% | "greater than $2 million but less than or equal to $5 million $137,000 plus 9.65%" |
| Second bracket ceiling | USD 5 million | "greater than $2 million but less than or equal to $5 million" |
| Tax at USD 5 million | USD 426,500 | "$426,500 plus 10.30% of the excess of PTE taxable income greater than $5 million." |
| Rate on income over USD 5 million up to USD 25 million | 10.30% | "$426,500 plus 10.30% of the excess" |
| Third bracket ceiling | USD 25 million | "greater than $5 million but less than or equal to $25 million" |
| Tax at USD 25 million | USD 2,486,500 | "$2,486,500 plus 10.90% of the excess of PTE taxable income greater than $25 million." |
| Rate on income over USD 25 million | 10.90% | "$2,486,500 plus 10.90% of the excess" |

How to read it. Each fixed amount applies once income passes the ceiling below it, and the higher rate applies only to the excess over that ceiling. Income of exactly a ceiling stays in the lower row ("less than or equal to"). There is no minimum tax: with zero or negative PTE taxable income the PTET is zero, but the entity must still file the annual return ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

The live version of this Guide compared these rates to the individual brackets. That comparison is not on the PTET pages and is removed; individual rates are in `ny-it-201-resident-return`.

## Estimated payments

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.tax.ny.gov/bus/ptet/ |
| Minimum each quarter, of the required annual payment | 25% | "Each quarterly payment should be an amount equal to at least 25% of the required annual payment for the taxable year." |
| Required annual payment, current-year test | 90% | "90% of the PTET shown on the return of the electing entity for the taxable year" |
| Required annual payment, prior-year test | 100% | "100% of the PTET shown on the return of the electing entity for the preceding taxable year." |

Due dates. Payments "are due on or before March 15, June 15, September 15, and December 15 in the calendar year prior to the year in which the due date of the return falls", moved to the next business day if the date is a Saturday, Sunday or legal holiday ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). For the 2026 PTET year the dates were Monday 16 March 2026 (15 March was a Sunday), Monday 15 June 2026, Tuesday 15 September 2026, and Tuesday 15 December 2026. The fourth payment is in December of the PTET year, not January.

Required annual payment. It is the lesser of the two tests in the table. "If the entity did not opt in to the PTET for the preceding year, the required annual payment is 90% of the tax reported on the PTET return for the taxable year." ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) If the current year's PTE taxable income and PTET are zero or less, the lesser of the two tests is zero and no estimated payments are due. If the entity elected for the preceding year and that year's PTET was zero, the lesser of the two tests is also zero, and "no estimated PTET payments are due". Any unpaid PTET must be paid by 15 March following the close of the calendar year in which the tax year ends ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Penalties. Late or short payments bear penalty and interest "based on the rules in Article 22". Taxpayers "may not apply the annualized installment method under Tax Law § 685(c)(4)" to reduce the penalty. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) The live version of this Guide stated a penalty rate; no PTET page prints one, so it is removed.

How to pay. Authorized persons and tax professionals may both pay. Payments go through Web File "and pay by ACH debit". Entities "cannot pay by check or other methods." Up to 12 payments a year may be made; they can be scheduled ahead until 15 December, and payments from 16 to 31 December are allowed but cannot be scheduled ahead. "An electing entity cannot make estimated tax payments after filing a return." ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

No transfers. PTET payments apply only to New York State PTET or NYC PTET. They cannot be moved to other taxes, to related entities, or to the owners' own estimated tax accounts, even in a loss year. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) State and city PTET payments are applied together on the annual return, and any net overpayment is refunded ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Overpayments. "Overpayments cannot be carried forward to future years and will automatically be reviewed and processed as a refund." The refund is a physical check to the entity's address of record. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) The live version of this Guide said an overpayment could be applied to next year's first installment; that is wrong.

Owners' own estimates. Owners may take the expected PTET credit into account when computing their own IT-2105 estimates ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). An electing partnership must still make MCTMT estimated payments for nonresident partners on Form IT-2658-MTA ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

## Annual return

Due date. "On or before March 15, an electing entity must file an annual PTET return using the online return application", on a calendar-year basis, next business day rule applying ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). For the 2026 PTET year that is Monday 15 March 2027. An entity that elected must file even if it owes nothing ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Extension. A six-month extension to file must be requested online by 15 March. It "is an extension of time to file the annual return, not an extension of time to pay". Filing IT-370-PF or CT-5.4 does not extend the PTET return. With a valid extension the entity may make further PTET payments until it files or until the extended due date, whichever is first, with penalties and interest on payments after the original due date. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)) The extension does not move the next year's 15 March election date.

What it reports. The return lists every eligible credit claimant: name and ID number, any disregarded entity through which the claim is made, taxpayer type, ownership percentage, share of the PTET credit, and (for partnerships) resident or nonresident classification. Over 100 claimants means a data file upload. "The entity cannot change any of the reported information once the return is submitted." ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

Amending. The Tax Commissioner may consent to an amended return "in appropriate circumstances". Requests go through PTET Web File and "must be made within one year of the extended due date of the initial return", whether or not an extension was filed. A federal change does not require an amended PTET return. The entity still "would be required to report federal changes under Tax Articles 22 and 9-A, as applicable" ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Informing owners. Partnerships report each partner's resident or nonresident classification and direct share of the PTET on Form IT-204-IP. S corporations give each shareholder a statement with the direct share of the PTET. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) The PTET return is separate from the entity's IT-204 or CT-3-S; the live version named a "Form PTET-EXT", which no PTET page names, so the online extension request is described instead.

## Owner-level credit (Form IT-653)

Who claims. Only direct owners taxable under Article 22 (individuals, trusts, estates). A non-grantor trust claims the credit on its own IT-205 and "is not permitted to distribute any PTET credit it receives to its beneficiaries." A grantor trust is disregarded; the grantor claims. A partner that is itself a partnership, or any corporate owner, cannot claim or pass the credit on. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Amount. The credit equals the owner's direct share of the PTET reported on the entity's annual return; credits from several entities are added together ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). For an S corporation, each owner's credit is total PTET multiplied by that owner's ownership percentage. For a partnership, total PTET is split between the resident and nonresident pools in proportion to each pool's PTE taxable income, then within each pool by profit and loss ownership percentage, adjusted for special allocations such as guaranteed payments. If one pool is zero or less, its partners get nothing and the whole PTET goes to the other pool. ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm); [TSB-M-21(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m21-1c-1i.pdf)) The live version of this Guide said S corporation credits follow distributive share of PTE taxable income rather than ownership percentage; for S corporations the Department's rule is ownership percentage.

Refundable. The credit offsets all tax on Forms IT-201, IT-203 and IT-205. Any excess "is treated as an overpayment, to be credited or refunded without interest" under Tax Law § 606(kkk). ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Which year. The owner claims the credit on the return for the same tax year as the PTET annual return, whenever the PTET was paid. An owner who filed before receiving the share must amend. ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

How. Attach Form IT-653 to an individual return. Nonresident owners must file an individual IT-203. The credit cannot be claimed on the group returns, Form IT-203-GR or Form IT-203-S. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

Add-back. The owner adds back the PTET credit claimed, once, at the individual level, with addition modification A-219 on Form IT-225 ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). The live version of this Guide called this "EA-219" or "S-219"; the Department's code is A-219. IT-203 filers allocate the A-219 amount using the IT-225 method for items of income ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). Where the entity's federal deduction for PTET in a year differs from the credits claimed for that year (for example after a refund of an overpayment), the entity adds back the difference under § 612(b)(3); the FAQ works three examples ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Order of credits. "The resident tax credit is non-refundable and must be applied before the PTET credit, which is fully refundable." ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

New York residents with other states' entity taxes. For tax years beginning on or after 1 January 2021, a New York resident owner gets a resident tax credit under Tax Law § 620(b) for a pass-through entity tax "imposed by another state, local government, or the District of Columbia, that is substantially similar to the PTET", paid "on income derived from that jurisdiction and subject to tax under Article 22" ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). The Department's [list of substantially similar states](https://www.tax.ny.gov/bus/ptet/substantially-similar.htm) "Includes all legislation enacted as of December 15, 2023" and was last updated March 19, 2024, so a later state regime needs checking. The owner adds back the other state's PTET used for the credit with code A-220, and any remaining federally deducted amount with code A-201 ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). A part-year resident may not allocate this add-back ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Nonresident owners and their home state. Whether a nonresident's home state gives a credit for New York PTET is that state's rule. It is not on New York's pages. Use `us-pte-state-matrix` and the home state's own Guide.

## NYC PTET

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.tax.ny.gov/e-services/ptet/calculations-city.htm |
| NYC PTET rate on NYC PTE taxable income | 3.876% | "Multiply the NYC PTE taxable income by 3.876% (0.03876)." |

The same rate is in [TSB-M-22(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m22-1c-1i.pdf), which applies it to tax years beginning on or after 1 January 2022. The live version of this Guide said "for tax years 2023 and later"; the memo says from 2022.

Who can elect ([NYC PTET page](https://www.tax.ny.gov/bus/ptet/city.htm)). Only an entity that opts in to the State PTET for the same year, at the same time, in the same online application, and:
- a partnership: it "has at least one partner or member that is a city taxpayer"; or
- an S corporation: it is a resident S corporation for PTET purposes "and all shareholders are city taxpayers".
A standard S corporation cannot elect. The live version of this Guide said one New York City resident owner was enough for any entity; that holds for partnerships only.

A city taxpayer is a city resident individual, trust or estate under Tax Law § 1305. Owners cannot be part-year city residents; an owner resident in the city "for at least half of the year" is a city resident, and all others are nonresidents with no NYC credit. ([calculation page, city](https://www.tax.ny.gov/e-services/ptet/calculations-city.htm); [TSB-M-22(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m22-1c-1i.pdf))

Base. "The NYC PTE taxable income only consists of items flowing through to direct partners, members, or shareholders that are city taxpayers." For a resident S corporation it equals the State PTE taxable income. For a partnership it is the items of the city resident partners only. ([calculation page, city](https://www.tax.ny.gov/e-services/ptet/calculations-city.htm)) The live version said the base was limited to "NYC-source income"; the Department's base is the city residents' items, not a city-source test.

Mechanics. Election deadline, estimated payment dates and percentages, the annual return and the six-month extension are the same as for the State PTET ([NYC PTET page](https://www.tax.ny.gov/bus/ptet/city.htm)). The NYC page says the election "is irrevocable after March 15"; the FAQ says "The PTET and NYC PTET election can be revoked up until the due date of the first estimated PTET and NYC PTET payments" ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). An entity need not file NYC GCT or UBT to elect ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Owner credit. City resident owners claim it on Form IT-653 with their State return. The credit is refundable without interest under Tax Law § 1310(g), and the owner adds it back on Form IT-225. Owners not taxable under Article 30, corporate partners and partnership partners get none. ([NYC PTET page](https://www.tax.ny.gov/bus/ptet/city.htm)) For a partnership, each city resident partner's share is "based on the partner's ... relative share of NYC PTE taxable income" ([calculation page, city](https://www.tax.ny.gov/e-services/ptet/calculations-city.htm)).

## Federal treatment and the SALT cap after the One Big Beautiful Bill Act

IRS Notice 2020-75 says "the forthcoming proposed regulations will clarify that Specified Income Tax Payments (as defined in section 3.02(1) of this notice) are deductible by partnerships and S corporations in computing their non-separately stated income or loss." The entity takes the deduction "for the taxable year in which the payment is made." "Any Specified Income Tax Payment made by a partnership or an S corporation is not taken into account in applying the SALT deduction limitation to any individual who is a partner in the partnership or a shareholder of the S corporation." ([IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf))

Timing follows the payment. Estimates paid during 2026 are deducted for 2026. A balance paid with the return in March 2027 is deducted for 2027, even though the owners' credit for it is a 2026 credit. The Department's FAQ works this split ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm |
| Individual SALT cap, taxable years beginning in 2026 (half for married filing separately) | USD 40,400 | "in the case of any taxable year beginning in calendar year 2026, $40,400" |
| MAGI threshold for the phase-down, 2026 | USD 505,000 | "in the case of any taxable year beginning in calendar year 2026, $505,000" |
| Phase-down rate on MAGI over the threshold, taxable years beginning before 2030 | 30 percent | "reduced by 30 percent of the excess (if any) of the taxpayer's modified adjusted gross income over the threshold amount" |
| Floor: the phase-down cannot take the cap below | USD 10,000 | "shall not result in the applicable limitation amount being less than $10,000" |
| Yearly increase for 2027 to 2029 | 101 percent | "after calendar year 2026 and before 2030, 101 percent of the dollar amount" |
| Cap for taxable years beginning after 2029 | USD 10,000 | "in the case of any taxable year beginning after calendar year 2029, $10,000" |

Section 70120 of the Act changes the cap amounts in § 164(b)(6) and adds § 164(b)(7) with the phase-down. Its text does not address payments made by a partnership or S corporation, so Notice 2020-75 is still the IRS statement on entity-level taxes. The live version of this Guide described a USD 10,000 cap only; that cap applies again only for taxable years beginning after 2029, and as a floor before then.

What this means for the decision. Whether the entity-level deduction saves federal tax for a given owner depends on that owner's federal return, including the 2026 cap and the MAGI phase-down in the table above. No page cited here computes it. The arithmetic belongs in `us-2026-federal-tax-changes`; this Guide does not compute federal savings.

The live version of this Guide also stated effects on the qualified business income deduction and on self-employment tax. No allowed page proves those effects for PTET, so they are removed; refer them.

## When electing does NOT help

The first eight come from the Department's pages cited. The last two are federal and home-state questions that this Guide routes out.
- No owner taxable under Article 22. Income to corporations, partnerships and S corporations is outside the base; they get no credit ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).
- Tiered structures. A partner that is itself a partnership gets no credit and "cannot pass the PTET credit through to its partners" ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). An electing upper-tier partnership includes in its own PTE taxable income the amounts flowing to its direct partners taxable under Article 22, "including any income received from a lower-tier partnership" ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).
- Trust owners whose beneficiaries bear the tax. A non-grantor trust keeps the credit; it cannot pass it to beneficiaries ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)).
- Nonresidents on a group return. The credit cannot be claimed on IT-203-GR or IT-203-S. Each must file an individual IT-203 ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).
- A loss year. Estimates cannot be moved to the owners. The entity files and waits for a refund check; nothing carries forward ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)).
- A standard S corporation with resident owners. Only the apportioned New York share enters the base, and the NYC PTET is not available ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm); [NYC PTET page](https://www.tax.ny.gov/bus/ptet/city.htm)).
- Partners in a negative pool. "Partners in the negative pool will not receive any PTET credit" ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).
- A missed or late election. There is no late relief, including for new entities ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).
- An owner for whom the entity-level deduction may save little federal tax. That turns on the owner's own federal return; see the federal section above and `us-2026-federal-tax-changes`.
- A nonresident whose home state gives no credit for New York PTET. See `us-pte-state-matrix`.

## Worked example (hypothetical)

All amounts in this example are invented US dollars, written without a currency code because they are not official figures. The rates are from the tables above.

Facts. A calendar-year partnership elected for 2026 by 16 March 2026. It did not elect for 2025. Two individual partners share profit and loss equally. Partner A is a New York City resident all year. Partner B lives in New Jersey all year. No special allocations, no guaranteed payments. Partnership items for 2026 before any PTET deduction: 3,000,000 of ordinary income. Of B's half (1,500,000), 900,000 is New York source under Article 22 rules.

Step 1, pools. Resident pool (A, all items): 1,500,000. Nonresident pool (B, New York source only): 900,000. PTE taxable income: 1,500,000 + 900,000 = 2,400,000.

Step 2, State PTET. Income is over 2,000,000 and not over 5,000,000, so the second row applies: 137,000 + 9.65% × (2,400,000 − 2,000,000) = 137,000 + 9.65% × 400,000 = 137,000 + 38,600 = 175,600.

Step 3, credits. Resident pool share: 1,500,000 / 2,400,000 = 0.625, and 175,600 × 0.625 = 109,750. Nonresident pool share: 900,000 / 2,400,000 = 0.375, and 175,600 × 0.375 = 65,850. Check: 109,750 + 65,850 = 175,600. Each partner is alone in a pool, so A's credit is 109,750 and B's is 65,850.

Step 4, NYC PTET. The partnership has a city taxpayer partner, so it could elect the NYC PTET in the same election. NYC PTE taxable income is A's items only: 1,500,000. NYC PTET: 1,500,000 × 3.876% = 58,140. A's NYC credit is 58,140.

Step 5, estimates. The entity did not elect for 2025, so the required annual payment is 90% of the current-year tax. State: 175,600 × 90% = 158,040, at least 158,040 × 25% = 39,510 each quarter. City: 58,140 × 90% = 52,326, at least 52,326 × 25% = 13,081.50 each quarter. If the entity pays exactly those amounts by 15 December 2026, the balances are 175,600 − 158,040 = 17,560 (State) and 58,140 − 52,326 = 5,814 (City), due by 15 March 2027.

Step 6, federal timing. The 158,040 + 52,326 = 210,366 paid in 2026 is deducted by the partnership for 2026. The 17,560 + 5,814 = 23,374 paid in March 2027 is deducted for 2027.

Step 7, owners. A files IT-201 with IT-653, claiming 109,750 (State) and 58,140 (City), and adds back the State credit with A-219 on IT-225, and adds back the City credit on IT-225 as the IT-225 instructions direct. B files an individual IT-203 with IT-653, claiming 65,850; any excess over B's New York tax is refunded without interest. B's New Jersey treatment is a New Jersey question: see `us-pte-state-matrix`.

## Practitioner checklist

1. Eligibility: partnership with a § 658(c)(1) filing requirement and not publicly traded, or a New York S corporation subject to the § 209 fixed dollar minimum.
2. Owner list: who is taxable under Article 22; who is a resident (at least half the year); who is a city taxpayer.
3. S corporation: can it certify all shareholders as New York residents at election time?
4. Election by an authorized person by 15 March (next business day if a weekend or holiday); not by the tax professional. Diary it every year.
5. Revoke only before the first estimated payment due date if the facts change.
6. Estimates by ACH debit on the four dates; size them on the 90% or 100% tests.
7. Annual return by 15 March; online extension if needed, but pay by 15 March.
8. IT-204-IP or shareholder statements with each owner's direct share.
9. Owners: IT-653, A-219 add-back, individual IT-203 for nonresidents, resident credit and A-220 for other states' entity taxes.
10. Federal: deduct in the year paid; work owner effect with `us-2026-federal-tax-changes`.

## When to refuse or refer

- Refer any decision that turns on shareholder residence changing during the year for a resident S corporation. The pages give only the certification at election time.
- Refer special allocations, guaranteed payments to non-equity partners and negative-pool cases beyond the Department's examples.
- Refer an amended PTET return request, a notice or an assessment. Do not file an amended return to protest an assessment ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).
- Refer the federal savings estimate, QBI and self-employment tax effects to a federal Guide or a credentialed preparer.
- Refer a nonresident owner's home-state credit to that state's Guide and `us-pte-state-matrix`.
- Refuse to tell a client an election can still be made for 2026. The window closed on 16 March 2026.
- Refuse to treat a tax professional's own login as the election. The authorized person must sign.

## Sources

- New York State Department of Taxation and Finance, [Pass-through entity tax (PTET)](https://www.tax.ny.gov/bus/ptet/), updated April 3, 2026.
- Department, [Calculating the PTE taxable income, the PTET, and the credit](https://www.tax.ny.gov/e-services/ptet/calculations.htm), updated June 18, 2025.
- Department, [Frequently asked questions about the PTET](https://www.tax.ny.gov/bus/ptet/faq.htm), updated October 3, 2025.
- Department, [New York City pass-through entity tax (NYC PTET)](https://www.tax.ny.gov/bus/ptet/city.htm), updated April 3, 2026.
- Department, [Calculating the NYC PTE taxable income, the NYC PTET, and the credit](https://www.tax.ny.gov/e-services/ptet/calculations-city.htm), updated November 21, 2024.
- Department, [States with a tax substantially similar to PTET](https://www.tax.ny.gov/bus/ptet/substantially-similar.htm), updated March 19, 2024.
- [TSB-M-21(1)C, (1)I, Pass-Through Entity Tax](https://www.tax.ny.gov/pdf/memos/ptet/m21-1c-1i.pdf), August 25, 2021.
- [TSB-M-22(1)C, (1)I, New York City Pass-Through Entity Tax](https://www.tax.ny.gov/pdf/memos/ptet/m22-1c-1i.pdf), October 11, 2022.
- [IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf).
- [Public Law 119-21 (One Big Beautiful Bill Act), section 70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

This Guide must be reviewed by a New York-licensed CPA, Enrolled Agent, or attorney admitted in New York before it is used for client deliverables. Practitioners must check current-year rates, deadlines, form numbers and modification codes against the Department's website before relying on it.

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
