---
name: ny-pte-tax-ptet
description: New York pass-through entity tax (PTET, Tax Law Article 24-A) and New York City PTET (Article 24-B) for 2026. Who can elect (partnerships with a Tax Law 658(c)(1) filing requirement, New York S corporations subject to the fixed dollar minimum), the annual online election by 15 March by an authorized person, resident against standard S corporations, PTE taxable income pools, the graduated rate (6.85% up to $2 million, then 9.65%, 10.30% and 10.90%), the flat 3.876% NYC PTET, quarterly estimates by ACH on 15 March, 15 June, 15 September and 15 December, the annual return by 15 March, and the owners' refundable credit on Form IT-653 with the A-219 add-back. Includes the decision whether and how to elect. Trigger on "New York PTET", "NY pass-through entity tax", "IT-653", "PTET election", "NYC PTET", "SALT workaround New York". New York only.
version: "3.0"
jurisdiction: US-NY
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: decision
---

# New York pass-through entity tax (PTET) and New York City PTET, tax year 2026

> **Source-cited draft.** Built from the Tax Department's PTET page, its PTET and NYC PTET calculation pages, the PTET FAQ, the NYC PTET page, TSB-M-21(1)C, (1)I and TSB-M-22(1)C, (1)I, and IRS Notice 2020-75, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** The PTET is an optional New York tax that a partnership or a New York S corporation elects each year to pay on its owners' share of income. The entity pays **6.85%** on PTE taxable income up to **USD 2 million**, rising to **10.90%** above USD 25 million; the NYC PTET is a flat **3.876%** on the city residents' share. Each direct owner who is an individual, trust or estate taxable under Article 22 gets a **refundable credit** equal to their direct share, so the New York tax is broadly the same; the point of electing is that the entity deducts the tax for federal purposes (IRS Notice 2020-75). The 2026 election window (1 January to Monday 16 March 2026) has **closed**; the 2027 window runs from 1 January to Monday 15 March 2027. Estimates are due 15 March, 15 June, 15 September and 15 December of the PTET year, and the annual return by 15 March after it.

## Scope and who this is for

This skill covers eligibility, the election, the resident and standard S corporation versions, PTE taxable income, the rate table, estimated payments, the annual return, the owner credit and add-back, the resident credit for other states' entity taxes, and the NYC PTET.

Not covered here, with the skill to use instead:
- New York individual rates and the resident return: `ny-it-201-resident-return`.
- New York corporate franchise tax under Article 9-A: `ny-corporate-franchise-article-9a`.
- Federal SALT cap amounts and phase-down: `us-2026-federal-tax-changes`.
- Other states' elective entity taxes and whether an owner's home state credits New York PTET: `us-pte-state-matrix`.
- New York estimated tax for individuals (IT-2105): `ny-estimated-tax`.
- MCTMT: `ny-mctmt`.

Why the tax exists. Article 24-A was enacted in 2021 (Chapter 59 of the Laws of 2021, Part C, per [TSB-M-21(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m21-1c-1i.pdf)). The PTET is an optional tax for "tax years beginning on or after January 1, 2021" ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). The entity pays the tax. Under IRS Notice 2020-75 the payment is deducted by the entity and is not counted against the owner's federal SALT cap (see the federal section below). The owner then takes a refundable New York credit for the tax paid.

## Ask the client first

- Who are the direct owners, and which of them are individuals, trusts or estates, as against corporations, partnerships or S corporations? Only direct owners taxable under Article 22 get a credit.
- For each individual owner: New York resident for at least half of the year, or not? For a city election: New York City resident for at least half of the year, or not?
- For an S corporation: are all shareholders New York residents now, so it can certify as a resident S corporation when it elects? Are all of them city taxpayers?
- Does the entity expect positive New York income this year, and can it fund the quarterly estimates in cash? A loss year means a refund by check, not a transfer to owners.
- Do any nonresident owners file through a group return (IT-203-GR or IT-203-S)? They cannot claim the credit there.
- Is the owner's federal state and local tax deduction actually limited by the 2026 cap? The answer decides whether the election saves federal tax; this skill does not compute it. Check this with `us-2026-federal-tax-changes`.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| PTET on PTE taxable income of USD 2 million or less | 6.85% of PTE taxable income | [Tax Department, calculating the PTET](https://www.tax.ny.gov/e-services/ptet/calculations.htm) |
| PTE taxable income over USD 2 million, not over USD 5 million | USD 137,000 plus 9.65% of the excess over USD 2 million | [Tax Department, calculating the PTET](https://www.tax.ny.gov/e-services/ptet/calculations.htm) |
| PTE taxable income over USD 5 million, not over USD 25 million | USD 426,500 plus 10.30% of the excess over USD 5 million | [Tax Department, calculating the PTET](https://www.tax.ny.gov/e-services/ptet/calculations.htm) |
| PTE taxable income over USD 25 million | USD 2,486,500 plus 10.90% of the excess over USD 25 million | [Tax Department, calculating the PTET](https://www.tax.ny.gov/e-services/ptet/calculations.htm) |
| NYC PTET on NYC PTE taxable income | 3.876% | [Tax Department, calculating the NYC PTET](https://www.tax.ny.gov/e-services/ptet/calculations-city.htm) |
| Election window | 1 January to 15 March of the PTET year (next business day if a weekend or holiday) | [Tax Department, PTET](https://www.tax.ny.gov/bus/ptet/) |
| Estimated payment, each quarter, share of the required annual payment | at least 25% | [Tax Department, PTET](https://www.tax.ny.gov/bus/ptet/) |
| Required annual payment, current-year test | 90% of the PTET for the taxable year | [Tax Department, PTET](https://www.tax.ny.gov/bus/ptet/) |
| Required annual payment, prior-year test (only if the entity elected for the prior year) | 100% of the PTET for the preceding taxable year | [Tax Department, PTET](https://www.tax.ny.gov/bus/ptet/) |
| Number of estimated payments allowed in the PTET year | up to 12 | [Tax Department, PTET](https://www.tax.ny.gov/bus/ptet/) |
| Owners with more than this many credit claimants upload a data file | 100 | [Tax Department, PTET](https://www.tax.ny.gov/bus/ptet/) |

The Department prints the same State table in [TSB-M-21(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m21-1c-1i.pdf) and the same city rate, from tax years beginning on or after 1 January 2022, in [TSB-M-22(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m22-1c-1i.pdf). The Department's pages print no end year for the PTET.

### Steps

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

### Eligibility: who can elect

Eligible (both from the [Department PTET page](https://www.tax.ny.gov/bus/ptet/)):
- A partnership, including an LLC treated as a partnership for federal income tax purposes, that "has a filing requirement under Tax Law § 658(c)(1) and is not a publicly traded partnership". It may elect "even if it has partners that are not eligible for the PTET credit, including, but not limited to, corporate partners."
- A New York S corporation (including an LLC treated as an S corporation for New York and federal purposes) as defined by Tax Law § 208.1-A "that is subject to the fixed dollar minimum tax under Tax Law § 209." A federal S corporation with no nexus to New York is an ineligible corporation under § 620(b)(3)(B) and cannot elect.

Not eligible: "single-member LLCs (unless they elect to be treated as an S corporation for New York purposes)", sole proprietorships, trusts, non-profit corporations, and "corporations that are not New York S corporations" ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). A single-member LLC that is disregarded cannot elect; one that elects S corporation treatment for New York purposes can ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). So a single-shareholder New York S corporation can elect.

Owners who are not taxable under Article 22. A partnership that elects must include all partners taxable under Article 22, resident and nonresident. It cannot pick which partners take part ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). Income flowing to a corporate partner, a partnership partner, an S corporation partner or any other owner not taxable under Article 22 is left out of PTE taxable income, and that owner gets no credit. A partnership owned only by a partnership and a corporation may elect, but "will not have any PTE taxable income or PTET credits to distribute" ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

### Election mechanics

Who elects. "Only an authorized person may make this election on behalf of an eligible partnership or eligible S corporation". "Tax professionals may not make this election on behalf of their clients." For a partnership, an authorized person is a member, partner, owner or other individual with authority to bind the entity and sign returns under Tax Law § 653. For an S corporation, it is an officer, manager or shareholder authorized under state law or the organizational documents, who represents that authority under penalty of perjury. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

When. "An eligible entity may opt in on or after January 1, but no later than March 15." If that date falls on a Saturday, Sunday or legal holiday, "the election is due on the next business day." ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) For the 2026 PTET year, 15 March 2026 was a Sunday, so the last day was Monday 16 March 2026, a date derived from the weekend rule above and not printed on any Department page. That window is closed: an entity that did not elect cannot elect for 2026. If the rules are unchanged, the 2027 window is 1 January 2027 to Monday 15 March 2027.

Every year. The election "must be made online on an annual basis". It does not carry over. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

Revoking. The election "is irrevocable after the due date of the entity's first PTET estimated payment." Until then, "The PTET election may be revoked at any time up until the due date of the first estimated payment, through the entity's Business Online Services account." An entity may not file a zero return to undo the election unless it truly has no PTE taxable income. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

No late election. Entities "formed after the annual election deadline" cannot opt in for that calendar year: "There are no tax law provisions to allow for a later opt-in deadline for newly formed entities." ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Fiscal years. A calendar-year entity elects, files and pays on a calendar-year basis. A fiscal-year entity elects, files and pays "for the calendar year in which its fiscal year ends." An entity with more than one short tax year in a calendar year makes one election only, for the first short year that ends in that calendar year. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Reorganizations. After a federal F reorganization of an electing S corporation, the election stays in effect for the successor. For a partnership, it stays in effect only if the successor continues the original partnership, the original files no final return, and all the year's income is reported on the successor's return. ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

### Resident against standard S corporation

Two kinds of electing S corporation ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)):
- Electing resident S corporation: one that "certifies at the time it elects to opt in to PTET that all of its shareholders are residents of New York State under Article 22."
- Electing standard S corporation: any other electing S corporation.

 The Department's test is a certification at the time of election that all shareholders are residents for Article 22 purposes. If shareholders may change residence during the year, refer the point (see the last section).

Why it matters. On the [calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm), the standard S corporation worksheet computes the New York share of each item "Using the apportionment rules of Article 9-A". The resident S corporation worksheet takes the full Schedule K-1 amounts. So a resident S corporation can bring all of its owners' share of income into the base, while a standard S corporation brings in only the apportioned New York share, even for shareholders who live in New York. Only a resident S corporation can also elect the NYC PTET.

Partnerships have no separate resident election. They classify each partner instead (next section).

### PTE taxable income

General rule: PTE taxable income "includes all income, gain, loss, or deduction of an electing entity that flows through to a direct partner, member, or shareholder for New York State personal income tax purposes." A direct owner is one issued a federal Schedule K-1 by the entity; a K-1 issued to a disregarded entity counts as issued to the person who reports its activity. ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm))

Partnerships. Each direct partner taxable under Article 22 is classified as resident or nonresident. "Members or partners may not be classified as part-year residents for PTET purposes." A partner is a resident "if they are a resident of New York for New York personal income tax purposes for at least half of the year." A trust is classified by its own residency, not its beneficiaries'. The partnership computes two pools and adds them ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm)):
- Nonresident pool: New York source items of nonresident partners, under Article 22 sourcing rules.
- Resident pool: all items of resident partners.
Both pools are computed "without regard for any limitations" such as capital losses, passive activity losses and basis limits. Guaranteed payments are included "to the same extent they are taxable by New York at the individual partner level", and they count as special allocations. A loss in one pool offsets income in the other when totalling PTE taxable income; partners in a negative pool get no credit. ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Add-backs in the base. When computing PTE taxable income, the entity adds back "all pass-through entity taxes paid and deducted for federal purposes in the current year, including taxes paid to New York or to other jurisdictions", and NYC UBT payments deducted federally. An S corporation adds back NYC general corporation tax if computed on the entire net income or alternative base. ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Separately stated items. "Other deductions" on the K-1 reduce PTE taxable income and go on the worksheet as negatives ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Sale of the business. Gain on an asset sale that flows through on the K-1 and is taxable to the owner is included. Gain on the sale of an owner's interest, which is not on the K-1, is not included ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Lines 17a and 17b of each worksheet "apply to tax years 2021 and 2022 only. For 2023 and later, leave these lines blank." ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm))

### Applying the rate

How to read it. Each fixed amount applies once income passes the ceiling below it, and the higher rate applies only to the excess over that ceiling. Income of exactly a ceiling stays in the lower row ("less than or equal to"). There is no minimum tax: with zero or negative PTE taxable income the PTET is zero, but the entity must still file the annual return ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

### Estimated payments

Due dates. Payments "are due on or before March 15, June 15, September 15, and December 15 in the calendar year prior to the year in which the due date of the return falls", moved to the next business day if the date is a Saturday, Sunday or legal holiday ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). For the 2026 PTET year the dates were Monday 16 March 2026 (15 March was a Sunday), Monday 15 June 2026, Tuesday 15 September 2026, and Tuesday 15 December 2026. The fourth payment is in December of the PTET year, not January.

Required annual payment. It is the lesser of the two tests in the table. "If the entity did not opt in to the PTET for the preceding year, the required annual payment is 90% of the tax reported on the PTET return for the taxable year." ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) If the current year's PTE taxable income and PTET are zero or less, the lesser of the two tests is zero and no estimated payments are due. If the entity elected for the preceding year and that year's PTET was zero, the lesser of the two tests is also zero, and "no estimated PTET payments are due". Any unpaid PTET must be paid by 15 March following the close of the calendar year in which the tax year ends ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Penalties. Late or short payments bear penalty and interest "based on the rules in Article 22". Taxpayers "may not apply the annualized installment method under Tax Law § 685(c)(4)" to reduce the penalty. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

How to pay. Authorized persons and tax professionals may both pay. Payments go through Web File "and pay by ACH debit". Entities "cannot pay by check or other methods." Up to 12 payments a year may be made; they can be scheduled ahead until 15 December, and payments from 16 to 31 December are allowed but cannot be scheduled ahead. "An electing entity cannot make estimated tax payments after filing a return." ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

No transfers. PTET payments apply only to New York State PTET or NYC PTET. They cannot be moved to other taxes, to related entities, or to the owners' own estimated tax accounts, even in a loss year. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) State and city PTET payments are applied together on the annual return, and any net overpayment is refunded ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Overpayments. "Overpayments cannot be carried forward to future years and will automatically be reviewed and processed as a refund." The refund is a physical check to the entity's address of record. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

Owners' own estimates. Owners may take the expected PTET credit into account when computing their own IT-2105 estimates ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). An electing partnership must still make MCTMT estimated payments for nonresident partners on Form IT-2658-MTA ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

### Annual return

Due date. "On or before March 15, an electing entity must file an annual PTET return using the online return application", on a calendar-year basis, next business day rule applying ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). For the 2026 PTET year that is Monday 15 March 2027. An entity that elected must file even if it owes nothing ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Extension. A six-month extension to file must be requested online by 15 March. It "is an extension of time to file the annual return, not an extension of time to pay". Filing IT-370-PF or CT-5.4 does not extend the PTET return. With a valid extension the entity may make further PTET payments until it files or until the extended due date, whichever is first, with penalties and interest on payments after the original due date. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)) The extension does not move the next year's 15 March election date.

What it reports. The return lists every eligible credit claimant: name and ID number, any disregarded entity through which the claim is made, taxpayer type, ownership percentage, share of the PTET credit, and (for partnerships) resident or nonresident classification. Over 100 claimants means a data file upload. "The entity cannot change any of the reported information once the return is submitted." ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

Amending. The Tax Commissioner may consent to an amended return "in appropriate circumstances". Requests go through PTET Web File and "must be made within one year of the extended due date of the initial return", whether or not an extension was filed. A federal change does not require an amended PTET return. The entity still "would be required to report federal changes under Tax Articles 22 and 9-A, as applicable" ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Informing owners. Partnerships report each partner's resident or nonresident classification and direct share of the PTET on Form IT-204-IP. S corporations give each shareholder a statement with the direct share of the PTET. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)) The PTET return is separate from the entity's IT-204 or CT-3-S. There is no separate extension form: the extension is requested online.

### Owner-level credit (Form IT-653)

Who claims. Only direct owners taxable under Article 22 (individuals, trusts, estates). A non-grantor trust claims the credit on its own IT-205 and "is not permitted to distribute any PTET credit it receives to its beneficiaries." A grantor trust is disregarded; the grantor claims. A partner that is itself a partnership, or any corporate owner, cannot claim or pass the credit on. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Amount. The credit equals the owner's direct share of the PTET reported on the entity's annual return; credits from several entities are added together ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). For an S corporation, each owner's credit is total PTET multiplied by that owner's ownership percentage. For a partnership, total PTET is split between the resident and nonresident pools in proportion to each pool's PTE taxable income, then within each pool by profit and loss ownership percentage, adjusted for special allocations such as guaranteed payments. If one pool is zero or less, its partners get nothing and the whole PTET goes to the other pool. ([calculation page](https://www.tax.ny.gov/e-services/ptet/calculations.htm); [TSB-M-21(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m21-1c-1i.pdf))

Refundable. The credit offsets all tax on Forms IT-201, IT-203 and IT-205. Any excess "is treated as an overpayment, to be credited or refunded without interest" under Tax Law § 606(kkk). ([Department PTET page](https://www.tax.ny.gov/bus/ptet/); [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

Which year. The owner claims the credit on the return for the same tax year as the PTET annual return, whenever the PTET was paid. An owner who filed before receiving the share must amend. ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

How. Attach Form IT-653 to an individual return. Nonresident owners must file an individual IT-203. The credit cannot be claimed on the group returns, Form IT-203-GR or Form IT-203-S. ([Department PTET page](https://www.tax.ny.gov/bus/ptet/))

Add-back. The owner adds back the PTET credit claimed, once, at the individual level, with addition modification A-219 on Form IT-225 ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). IT-203 filers allocate the A-219 amount using the IT-225 method for items of income ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). Where the entity's federal deduction for PTET in a year differs from the credits claimed for that year (for example after a refund of an overpayment), the entity adds back the difference under § 612(b)(3); the FAQ works three examples ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Order of credits. "The resident tax credit is non-refundable and must be applied before the PTET credit, which is fully refundable." ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm))

New York residents with other states' entity taxes. For tax years beginning on or after 1 January 2021, a New York resident owner gets a resident tax credit under Tax Law § 620(b) for a pass-through entity tax "imposed by another state, local government, or the District of Columbia, that is substantially similar to the PTET", paid "on income derived from that jurisdiction and subject to tax under Article 22" ([Department PTET page](https://www.tax.ny.gov/bus/ptet/)). The Department's [list of substantially similar states](https://www.tax.ny.gov/bus/ptet/substantially-similar.htm) "Includes all legislation enacted as of December 15, 2023" and was last updated March 19, 2024, so a later state regime needs checking. The owner adds back the other state's PTET used for the credit with code A-220, and any remaining federally deducted amount with code A-201 ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). A part-year resident may not allocate this add-back ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Nonresident owners and their home state. Whether a nonresident's home state gives a credit for New York PTET is that state's rule. It is not on New York's pages. Use `us-pte-state-matrix` and the home state's own Guide.

### NYC PTET

The same rate is in [TSB-M-22(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m22-1c-1i.pdf), which applies it to tax years beginning on or after 1 January 2022.

Who can elect ([NYC PTET page](https://www.tax.ny.gov/bus/ptet/city.htm)). Only an entity that opts in to the State PTET for the same year, at the same time, in the same online application, and:
- a partnership: it "has at least one partner or member that is a city taxpayer"; or
- an S corporation: it is a resident S corporation for PTET purposes "and all shareholders are city taxpayers".
A standard S corporation cannot elect.

A city taxpayer is a city resident individual, trust or estate under Tax Law § 1305. Owners cannot be part-year city residents; an owner resident in the city "for at least half of the year" is a city resident, and all others are nonresidents with no NYC credit. ([calculation page, city](https://www.tax.ny.gov/e-services/ptet/calculations-city.htm); [TSB-M-22(1)C, (1)I](https://www.tax.ny.gov/pdf/memos/ptet/m22-1c-1i.pdf))

Base. "The NYC PTE taxable income only consists of items flowing through to direct partners, members, or shareholders that are city taxpayers." For a resident S corporation it equals the State PTE taxable income. For a partnership it is the items of the city resident partners only. ([calculation page, city](https://www.tax.ny.gov/e-services/ptet/calculations-city.htm)) The base is the city residents' items, not a city-source test.

Mechanics. Election deadline, estimated payment dates and percentages, the annual return and the six-month extension are the same as for the State PTET ([NYC PTET page](https://www.tax.ny.gov/bus/ptet/city.htm)). The NYC page says the election "is irrevocable after March 15"; the FAQ says "The PTET and NYC PTET election can be revoked up until the due date of the first estimated PTET and NYC PTET payments" ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)). An entity need not file NYC GCT or UBT to elect ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

Owner credit. City resident owners claim it on Form IT-653 with their State return. The credit is refundable without interest under Tax Law § 1310(g), and the owner adds it back on Form IT-225. Owners not taxable under Article 30, corporate partners and partnership partners get none. ([NYC PTET page](https://www.tax.ny.gov/bus/ptet/city.htm)) For a partnership, each city resident partner's share is "based on the partner's ... relative share of NYC PTE taxable income" ([calculation page, city](https://www.tax.ny.gov/e-services/ptet/calculations-city.htm)).

### Federal treatment

IRS Notice 2020-75 says "the forthcoming proposed regulations will clarify that Specified Income Tax Payments (as defined in section 3.02(1) of this notice) are deductible by partnerships and S corporations in computing their non-separately stated income or loss." The entity takes the deduction "for the taxable year in which the payment is made." "Any Specified Income Tax Payment made by a partnership or an S corporation is not taken into account in applying the SALT deduction limitation to any individual who is a partner in the partnership or a shareholder of the S corporation." ([IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf))

Timing follows the payment. Estimates paid during 2026 are deducted for 2026. A balance paid with the return in March 2027 is deducted for 2027, even though the owners' credit for it is a 2026 credit. The Department's FAQ works this split ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).

The One Big Beautiful Bill Act changed the individual SALT cap, but not the treatment of taxes paid by a partnership or S corporation, so Notice 2020-75 is still the IRS statement on entity-level taxes. The individual cap amounts, the MAGI phase-down and the years they apply are federal figures with their own home: see `us-2026-federal-tax-changes`. This skill does not restate or compute them.

What this means for the decision. Whether the entity-level deduction saves federal tax for a given owner depends on that owner's federal return, including the 2026 cap and its MAGI phase-down in `us-2026-federal-tax-changes`. No page cited here computes it. The arithmetic belongs in `us-2026-federal-tax-changes`; this skill does not compute federal savings.

## Boundary and exception table

### When electing does not help

The first eight come from the Department's pages cited. The last two are federal and home-state questions that this skill routes out.
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

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Owner residence for PTET | Resident only if New York resident for at least half of the year; ask |
| Whether all S corporation shareholders can be certified as residents | Treat as a standard S corporation until certified |
| Whether the entity elected for the prior year | Assume not: required annual payment is 90% of the current-year PTET |
| Owner's federal SALT position | Do not assume a federal saving; route to `us-2026-federal-tax-changes` |
| Whether a nonresident files a group return | Ask: the credit cannot be claimed on IT-203-GR or IT-203-S |

### Red flags

| Flag | Why it matters |
| --- | --- |
| Election planned after 15 March | No late election, even for new entities |
| Tax professional plans to make the election | Only an authorized person may elect |
| Loss year with estimates already paid | No transfer to owners; refund by check after the return |
| Owner is a partnership or a corporation | No credit; income is left out of the base |
| Standard S corporation with only New York resident shareholders | Base limited to the apportioned share; consider certifying as resident at the next election |

## Worked cases

All amounts are invented. The rates are from the table above.

**Case 1, a partnership with a city resident and a nonresident.** A calendar-year partnership elected for 2026 by 16 March 2026. It did not elect for 2025. Two individual partners share profit and loss equally. Partner A is a New York City resident all year. Partner B lives in New Jersey all year. No special allocations, no guaranteed payments. Partnership items for 2026 before any PTET deduction: 3,000,000 of ordinary income. Of B's half (1,500,000), 900,000 is New York source under Article 22 rules.

Step 1, pools. Resident pool (A, all items): 1,500,000. Nonresident pool (B, New York source only): 900,000. PTE taxable income: 1,500,000 + 900,000 = 2,400,000.

Step 2, State PTET. Income is over 2,000,000 and not over 5,000,000, so the second row applies: 137,000 + 9.65% × (2,400,000 − 2,000,000) = 137,000 + 9.65% × 400,000 = 137,000 + 38,600 = 175,600.

Step 3, credits. Resident pool share: 1,500,000 / 2,400,000 = 0.625, and 175,600 × 0.625 = 109,750. Nonresident pool share: 900,000 / 2,400,000 = 0.375, and 175,600 × 0.375 = 65,850. Check: 109,750 + 65,850 = 175,600. Each partner is alone in a pool, so A's credit is 109,750 and B's is 65,850.

Step 4, NYC PTET. The partnership has a city taxpayer partner, so it could elect the NYC PTET in the same election. NYC PTE taxable income is A's items only: 1,500,000. NYC PTET: 1,500,000 × 3.876% = 58,140. A's NYC credit is 58,140.

Step 5, estimates. The entity did not elect for 2025, so the required annual payment is 90% of the current-year tax. State: 175,600 × 90% = 158,040, at least 158,040 × 25% = 39,510 each quarter. City: 58,140 × 90% = 52,326, at least 52,326 × 25% = 13,081.50 each quarter. If the entity pays exactly those amounts by 15 December 2026, the balances are 175,600 − 158,040 = 17,560 (State) and 58,140 − 52,326 = 5,814 (City), due by 15 March 2027.

Step 6, federal timing. The 158,040 + 52,326 = 210,366 paid in 2026 is deducted by the partnership for 2026. The 17,560 + 5,814 = 23,374 paid in March 2027 is deducted for 2027.

Step 7, owners. A files IT-201 with IT-653, claiming 109,750 (State) and 58,140 (City), and adds back the State credit with A-219 on IT-225, and adds back the City credit on IT-225 as the IT-225 instructions direct. B files an individual IT-203 with IT-653, claiming 65,850; any excess over B's New York tax is refunded without interest. B's New Jersey treatment is a New Jersey question: see `us-pte-state-matrix`.

```oa-check
name: New York PTET and NYC PTET for a two-partner partnership, 2026
inputs:
  resident_pool: 1500000
  nonresident_pool: 900000
steps:
  - pte_taxable_income: resident_pool + nonresident_pool
  - state_ptet: 137000 + (pte_taxable_income - 2000000) * 0.0965
  - resident_credit: state_ptet * resident_pool / pte_taxable_income
  - nonresident_credit: state_ptet * nonresident_pool / pte_taxable_income
  - nyc_ptet: resident_pool * 0.03876
  - required_annual_payment: state_ptet * 0.9
  - quarterly_minimum: required_annual_payment * 0.25
expected:
  pte_taxable_income: 2400000
  state_ptet: 175600.00
  resident_credit: 109750.00
  nonresident_credit: 65850.00
  nyc_ptet: 58140.00
  required_annual_payment: 158040.00
  quarterly_minimum: 39510.00
```

**Case 2, a decision: resident or standard S corporation?** A calendar-year New York S corporation will elect PTET for 2027. Its owners' share of income is USD 1,000,000; its Article 9-A business apportionment factor is 60%. All three shareholders live in New York. If it certifies at election that all shareholders are New York residents (an electing resident S corporation), PTE taxable income is the full USD 1,000,000 and the PTET is 6.85% x USD 1,000,000 = USD 68,500. As a standard S corporation, only the apportioned share enters: USD 600,000, PTET USD 41,100. In both cases the shareholders get a credit equal to the PTET, so their New York tax is broadly the same; the resident election moves USD 27,400 more of it to the entity, where it is deducted federally, and only the resident election allows the NYC PTET. Decision: certify as a resident S corporation if every shareholder is a New York resident at election and expected to stay so; if any shareholder may move during the year, refer (the pages give only the certification test). If one shareholder lives in New Jersey, it cannot certify and is a standard S corporation.

```oa-check
name: PTET as a resident or a standard S corporation (decision)
inputs:
  owners_income: 1000000
  apportionment_factor: 0.60
steps:
  - resident_base: owners_income
  - standard_base: owners_income * apportionment_factor
  - ptet_resident: resident_base * 0.0685
  - ptet_standard: standard_base * 0.0685
  - extra_entity_tax_resident: ptet_resident - ptet_standard
expected:
  resident_base: 1000000
  standard_base: 600000.00
  ptet_resident: 68500.00
  ptet_standard: 41100.00
  extra_entity_tax_resident: 27400.00
```

## When to refuse or refer

- Refer any decision that turns on shareholder residence changing during the year for a resident S corporation. The pages give only the certification at election time.
- Refer special allocations, guaranteed payments to non-equity partners and negative-pool cases beyond the Department's examples.
- Refer an amended PTET return request, a notice or an assessment. Do not file an amended return to protest an assessment ([PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm)).
- Refer the federal savings estimate, QBI and self-employment tax effects to a federal Guide or a credentialed preparer.
- Refer a nonresident owner's home-state credit to that state's Guide and `us-pte-state-matrix`.
- Refuse to tell a client an election can still be made for 2026. The window closed on 16 March 2026.
- Refuse to treat a tax professional's own login as the election. The authorized person must sign.

## Filing and payment

- **Election:** online through the entity's Business Online Services account (Corporation tax or Partnership tax, PTET web file, "Pass-through entity tax (PTET) annual election"), 1 January to 15 March, by an authorized person who signs electronically. The NYC PTET election is made in the same application. Revocable until the due date of the first estimated payment.
- **Estimates:** PTET web file, "Pass-through entity tax (PTET) estimated payment", by ACH debit only; 15 March, 15 June, 15 September and 15 December 2026 for the 2026 PTET year (16 March 2026, as 15 March was a Sunday). Tax professionals may pay.
- **Extension:** online by 15 March, six months to file, not to pay.
- **Annual return:** PTET web file, "Pass-through entity tax (PTET) annual return", by Monday 15 March 2027 for the 2026 PTET year, listing every eligible credit claimant. It cannot be changed after submission.
- **Owners:** IT-204-IP (partners) or a statement (shareholders) with each owner's direct share; owners attach Form IT-653 to IT-201, IT-203 or IT-205 and add back the credit on Form IT-225 (A-219).

Source for all of this section: [Tax Department, PTET](https://www.tax.ny.gov/bus/ptet/) and [PTET FAQ](https://www.tax.ny.gov/bus/ptet/faq.htm).

## Completion checklist

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

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Tax Department, Pass-through entity tax (PTET) (updated 3 April 2026). Read for eligibility, the election, revocation, estimates (25%, 90%, 100%, 12 payments, ACH), the annual return, extension, the credit and the resident tax credit. | https://www.tax.ny.gov/bus/ptet/ | 2026-11-13 |
| Tax Department, Calculating the PTE taxable income, the PTET, and the credit (updated 18 June 2025). Read for the three worksheets, the pools, the rate table and the credit pools. | https://www.tax.ny.gov/e-services/ptet/calculations.htm | 2026-11-13 |
| Tax Department, PTET frequently asked questions. Read for owners, tiered partnerships, add-backs, A-219, amended returns, late elections and federal timing. | https://www.tax.ny.gov/bus/ptet/faq.htm | 2026-11-13 |
| Tax Department, New York City pass-through entity tax (updated 3 April 2026). Read for who can elect the NYC PTET, city taxpayers and estimates. | https://www.tax.ny.gov/bus/ptet/city.htm | 2026-11-13 |
| Tax Department, Calculating the NYC PTE taxable income (updated 21 November 2024). Read for the 3.876% rate and the NYC credit. | https://www.tax.ny.gov/e-services/ptet/calculations-city.htm | 2026-11-13 |
| Tax Department, States with a tax substantially similar to PTET. Read for the list used for the resident tax credit. | https://www.tax.ny.gov/bus/ptet/substantially-similar.htm | 2026-11-13 |
| TSB-M-21(1)C, (1)I, Pass-Through Entity Tax. Read for the enactment and the rate table. | https://www.tax.ny.gov/pdf/memos/ptet/m21-1c-1i.pdf | 2026-11-13 |
| TSB-M-22(1)C, (1)I, New York City Pass-Through Entity Tax. Read for the 3.876% rate from 2022. | https://www.tax.ny.gov/pdf/memos/ptet/m22-1c-1i.pdf | 2026-11-13 |
| IRS Notice 2020-75. Read for the entity-level deduction in the year paid and exclusion from the owner's SALT limitation. | https://www.irs.gov/pub/irs-drop/n-20-75.pdf | 2026-11-13 |

Not yet confirmed: whether the substantially-similar states list (last updated March 2024) reflects later state laws; the 2027 election and estimate dates are derived from the Department's weekend rule and are not printed on a Department page.
