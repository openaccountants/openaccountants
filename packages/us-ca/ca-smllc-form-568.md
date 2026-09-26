---
name: ca-smllc-form-568
description: Tier 2 California content skill for preparing California Form 568 (Limited Liability Company Return of Income) for single-member LLCs disregarded for federal tax purposes but treated as separate entities by California for the $800 annual franchise tax and the gross receipts-based LLC fee. Covers tax year 2025 including the $800 minimum franchise tax (R&TC section 17941), the tiered LLC fee schedule (R&TC section 17942), first-year exemption rules, Form 3522 (LLC Tax Voucher), Form 3536 (Estimated Fee), Schedule B balance sheet requirements, and penalty and interest computations. Defers individual income tax to ca-540-individual-return and estimated personal tax to ca-estimated-tax-540es. MUST be loaded alongside us-tax-workflow-base v0.1 or later. California SMLLCs only.
version: 0.2
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# California single-member LLCs: Form 568, the annual tax and the LLC fee (tax year 2026)

Figures are for tax year 2026 unless a line says otherwise. A dated section near the end covers 2025 returns filed on extension. Researched on 25 September 2026 from the Revenue and Taxation Code (R&TC) and Franchise Tax Board (FTB) pages and instructions.

## Scope and who it is for ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

This Guide covers the California return of a **single-member LLC (SMLLC) that is disregarded for federal tax**. Federal law disregards an eligible entity with a single owner as "an entity separate from its owner" unless it elects to be a corporation ([26 CFR 301.7701-3](https://www.law.cornell.edu/cfr/text/26/301.7701-3)). California follows the federal classification. The FTB says: "If an eligible entity is disregarded for federal tax purposes, it is also disregarded for state tax purposes, except that an SMLLC must still pay a tax and fee, file a return, and limit tax credits."

So the SMLLC's income is reported on the **owner's** return, but the SMLLC itself:

- files **Form 568**;
- pays the **annual LLC tax** (form FTB 3522); and
- pays the **LLC fee** if its California total income reaches the first band (estimated on form FTB 3536).

The annual tax and fee rules, fee bands and the full doing-business tests are set out in the companion Guide **ca-llc-fee-and-tax**. This Guide applies them to a single owner and adds what is special to an SMLLC: the owner's consent, Schedule IW, the owner-based due dates, nonresident and corporate owners, and cancellation.

It does **not** cover multi-member LLCs, LLCs taxed as corporations (they file Form 100 or 100S), the owner's own income tax computation (for a California resident individual, see **ca-540-individual-return**), estimated personal tax, nonresident withholding, or the pass-through entity elective tax.

## Ask the client first

- Is the LLC organized in California, registered with the Secretary of State (SOS) as a foreign LLC, or neither? Get the exact SOS filing date.
- Has it elected to be taxed as a corporation (federal Form 8832 or 2553)? If so, it is out of scope.
- Who is the single owner? An individual, a trust or estate, a C corporation, an S corporation, a partnership, or an LLC classified as a partnership? What is the owner's taxable year?
- If the owner is an individual: is the owner a California resident, a part-year resident or a nonresident?
- Will the owner sign the Single Member LLC Information and Consent on Form 568?
- What are the SMLLC's gross receipts, cost of goods sold and other income for the year, and how much is assigned to California customers?
- If it is neither organized nor registered in California: what are its California sales, property and payroll, and its totals?
- What LLC fee was owed for the **preceding** taxable year, and what was paid on forms 3522 and 3536, and when?
- Has it stopped doing business? Has it filed a final Form 568 or any SOS cancellation form, and on what dates?
- Was the owner a deployed member of the US Armed Forces during the year?

## The method, step by step

1. **Confirm the classification.** One owner, disregarded for federal tax. If it elected corporate status, stop and use the corporation rules.
2. **Test whether it must file and pay.** Organized in California, registered with the SOS, or doing business under R&TC §23101: any one is enough. Then check the exceptions: the 15-day short year, the deployed-military exemption, and short form cancellation.
3. **Fix the taxable year.** For a disregarded SMLLC, the owner's taxable year replaces "taxable year" in §17941 and §17942 ([R&TC §18633.5(i)(4)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.)). In the first year, the year starts on the SOS filing date.
4. **Annual tax.** Pay it on form 3522 by the 15th day of the 4th month of the taxable year. In the first year, count the SOS filing month as month 1.
5. **Total income on Schedule IW.** Take the California amounts from the owner's federal schedules (Schedule C, D, E, F and so on). Total income is gross income **plus** cost of goods sold, so neither cost of goods sold nor operating expenses reduce it. Carry Schedule IW line 17 to Form 568 line 1 and read the fee from the table in **ca-llc-fee-and-tax**.
6. **Estimated fee.** If a fee will be owed, pay the estimate on form 3536 by the 15th day of the 6th month. Test the 10% penalty against the prior-year fee ([R&TC §17942(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.)).
7. **Consent.** Have the owner sign the Single Member LLC Information and Consent on Form 568. If a nonresident owner does not sign, complete Schedule T and pay the owner's tax.
8. **Return.** File Form 568 by the due date for the owner's type. Pay any fee balance and Schedule T tax by the **original** due date. The extension is automatic, but it covers filing only.
9. **Owner's return.** Report the SMLLC's income, deductions and credits on the owner's own return: Form 540 for a resident, Form 540NR for a nonresident or part-year resident, Form 100 or 100S for a corporation. Limit credits from the SMLLC.
10. **Stopping.** If the business has ended, file a timely final Form 568 and the SOS cancellation within the time limits below.

## Who must file Form 568 ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

A disregarded SMLLC files Form 568 and pays the annual tax if **any** of these is true ([R&TC §17941](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.)):

- **Organized in California.** The SOS has accepted its articles of organization.
- **Registered in California.** The SOS has issued it a certificate of registration as a foreign LLC. Registration alone is enough, even with no California business.
- **Doing business in California**, as defined in R&TC §23101, even if it never registered.

An organized or registered LLC owes the tax for each taxable year, or part of one, until a certificate of cancellation is filed with the SOS. It is owed whether or not the LLC is active or profitable. The FTB's LLC page says: "This yearly tax will be due, even if you are not conducting business, until you cancel your LLC" ([FTB: Limited liability company](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html)).

**Foreign SMLLC with only California-source income.** A nonregistered foreign LLC classified as disregarded "which is not doing business in California, need not file Form 565 or Form 568". Its owner still reports any California-source income on the owner's own return.

**Doing business, in short** ([R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.)). An LLC is doing business if **any** one of these is met:

- it actively engages in any transaction for financial gain in California;
- it is organized or commercially domiciled in California; or
- its California sales, property or payroll **exceed** the lesser of the indexed amount or 25% of its total sales, property or payroll.

"Exceed" means more than. The 2025 indexed amounts are $757,070 (sales), $75,707 (property) and $75,707 (payroll). The FTB had not published the 2026 amounts at 25 September 2026, so label any use of these as 2025 ([FTB: Doing business in California](https://www.ftb.ca.gov/file/business/doing-business-in-california.html)). The full tests are in **ca-llc-fee-and-tax**.

## Figures and deadlines, tax year 2026 ([FTB: Limited liability company](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html))

### Annual LLC tax: form FTB 3522 ([2026 FTB 3522 instructions](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf))

- **Amount.** $800. There is no proration for a short year, and it is owed even when there is no fee and no income.
- **Due date.** The 15th day of the 4th month of the taxable year ([R&TC §17941(c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.)). For an SMLLC whose owner uses the calendar year, that is 15 April 2026 for 2026. It is a payment at the **start** of the year, not with the return. The FTB says "do not send the $800 annual tax with Form 568".
- **First year.** "You have until the 15th day of the 4th month from the date you file with the SOS to pay your first-year annual tax." The FTB's example: an LLC that registers on 18 June has its tax due on 15 September. So the filing month counts as month 1.
- **When the first year starts.** Under the 2026 form 3522 instructions, an LLC's first taxable year begins when it files its articles of organization with the SOS. A foreign LLC's first taxable year begins when it was organized in its home state, not when it registers in California. A foreign LLC that registers or starts California business after the 15th day of its 4th month pays at once.

### First-year rules ([R&TC §17941(g)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.))

| First taxable year began | First-year annual tax |
|---|---|
| On or after 1 January 2021 and before 1 January 2024 | Exempt for the first taxable year (expired) |
| In 2024, 2025 or 2026 | Full $800. No first-year relief |
| On or after 1 January 2027 and before 1 January 2030 | $400 for the first taxable year only (added by SB 180, 2026) |

An SMLLC formed in 2026 pays $800 for 2026 (unless the 15-day rule in the boundary table applies) and $800 for 2027. The $400 rate, its foreign-LLC trap and an unsettled point about a 15-day year just before 2027 are covered in **ca-llc-fee-and-tax**. Check the 2027 form 3522 instructions before relying on $400.

### LLC fee and Schedule IW ([R&TC §17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.))

- **Bands.** The fee is a flat amount per band of California total income: nothing below $250,000, then $900, $2,500, $6,000 and $11,790 from $5,000,000. Income of exactly $250,000 is in the $900 band. Use the band table in **ca-llc-fee-and-tax**. Do not interpolate.
- **The base.** "Total income" means "gross income, plus the cost of goods sold that are paid or incurred in connection with the trade or business of the taxpayer attributed to California" ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html)). Gross income already has cost of goods sold taken out, and it is added back. For an SMLLC reporting on Schedule C, the base is therefore close to California gross receipts. Operating expenses never reduce it.
- **California only.** Only income "derived from or attributable to this state" counts. Services are assigned to California to the extent the customer receives the benefit there. Goods are assigned to California when delivered to a California buyer. If the business is wholly within California, all of its total income is California income.
- **Where the numbers come from.** SMLLCs below the $3,000,000 Schedule B and K tests "should prepare Schedule IW by entering the California amounts attributable to the disregarded entity from the member's federal Schedule B, C, D, E, F (Form 1040), or additional schedules". Gains go in too: for example, IRC section 1231 gains go on Schedule IW line 14.
- **Result.** Schedule IW line 17 is "Total California Income". It goes to Form 568 Side 1, line 1.
- **Due.** The fee is due by the **original** due date of the return. An extension does not move it.

### Estimated fee: form FTB 3536 ([2026 FTB 3536 instructions](https://www.ftb.ca.gov/forms/2026/2026-3536.pdf))

- **Estimate.** Pay the estimated fee by the 15th day of the 6th month of the taxable year. For a calendar-year owner that is 15 June 2026. "If the LLC does not owe a fee, do not complete or mail form FTB 3536."
- **Short first year.** "If the taxable year of the LLC ends prior to the 15th day of the 6th month of the taxable year, no estimated fee payment is due" (2025 Form 568 booklet, repeated in the 2026 form 3536 instructions). The fee is then due with the return.
- **10% penalty.** If the estimate is short, a penalty of 10% of the underpayment is added. The underpayment is the fee for the year minus the amount paid by the estimate due date ([R&TC §17942(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.)).
- **Safe harbor.** No penalty applies if the amount paid by that date is **equal to or greater than** the total fee for the **preceding** taxable year. A new SMLLC has no preceding year, so it has no safe harbor and must estimate.
- **Balance.** Pay the rest of the fee by the original due date of the return, on form 3536, or on form FTB 3537 if the return will be filed on extension.

### Form 568: due dates and extensions ([R&TC §18633.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.))

| Owner of the SMLLC | Original due date | Automatic extension |
|---|---|---|
| Individual, trust, estate or C corporation | 15th day of the 4th month after the close of the **owner's** taxable year (15 April 2027 for calendar 2026) | Six months (15 October 2027) |
| S corporation | 15th day of the 3rd month after the close of the taxable year (15 March 2027) | Six months (15 September 2027) |
| Partnership, or an LLC classified as a partnership | 15th day of the 3rd month after the close of the taxable year (15 March 2027) | Seven months (15 October 2027) |

- **No form is needed for the extension.** "California does not require the filing of written applications for extensions" ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html)). Federal Form 7004 plays no part in the California extension. A suspended or forfeited LLC gets no extension.
- **Filing only.** An extension "is not an extension of time for payment of tax required to be paid on or before the due date of the return without regard to extension" ([R&TC §18567](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18567.)).
- **Weekends and holidays.** A due date that falls on a weekend or holiday moves to the next business day.

## What goes on Form 568, and the owner's return ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

### The SMLLC's Form 568 ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

- **Always.** "An SMLLC is required to complete Form 568, Side 1, Side 2, Side 3, Side 7 (Schedule IW), and pay the annual tax and LLC fee (if applicable)."
- **Schedules B and K.** Complete these only if either test is met: the income or loss on Schedule B line 1, or lines 3 to 11, is $3,000,000 or more; or Schedule K line 21a (total distributive income/payment items) is $3,000,000 or more, or minus $3,000,000 or less. Take the amounts from the owner's federal return. SMLLCs do not complete Schedule K-1 (568) or form FTB 3832.
- **Consent.** Side 3 carries the Single Member LLC Information and Consent. It gives the owner's name and identification number and the owner's type. The law requires the SMLLC's return to include "the consent of the owner to California tax jurisdiction" ([R&TC §18633.5(i)(1)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.)).
- **Identification.** The vouchers ask for the SMLLC's SOS file number and FEIN ([2026 FTB 3522 instructions](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf)).
- **Separate payments.** Pay the annual tax on form 3522 and the fee on form 3536 (or 3537). Do not send the annual tax with Form 568.

### Resident individual owner: Form 540

The FTB tells an owner: "If you are a single member limited liability company, that is organized or doing business in California, or registered with the California Secretary of State (SOS), you are required to file Form 568, Limited Liability Company Return of Income, pay the annual tax and LLC Fee (if applicable), in addition to filing your tax return" ([2025 Schedule CA (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html)). The SMLLC's business income is reported through the owner's federal Schedule C and California Schedule CA (540), like a sole proprietorship. The resident owner's computation is in **ca-540-individual-return**. Form 568 does not replace the owner's Form 540.

### Nonresident or part-year resident owner: Form 540NR ([2025 Schedule CA (540NR) instructions](https://www.ftb.ca.gov/forms/2025/2025-540nr-ca-instructions.html))

- **Owner's return.** The owner files Form 540NR. Business income goes on Schedule CA (540NR). In column E, the nonresident owner enters "the total amount of profits or losses (including losses allowed from passive activities) from all businesses sourced to California while a nonresident of California".
- **Part in, part out.** If the business was conducted partly inside and partly outside California, "only income from the part conducted within California is considered California source income that you must report in column E." But "If there is any business relationship between the parts within and outside California (flow of goods, etc.), apportion the gross income or loss from the entire business", using the Schedule R formula.
- **Consent does not replace the return.** Filing the single member's consent, or Schedule T, "does not satisfy the member's California filing requirement" ([FTB Pub. 3556](https://www.ftb.ca.gov/forms/misc/3556.html)).

### Nonresident owner who does not sign the consent: Schedule T ([R&TC §18633.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.))

- **The rule.** "If a nonresident has not signed the single member LLC consent on Side 3, then the SMLLC is required to complete Schedule T on Side 4." The SMLLC then pays tax on the owner's behalf. The law treats the missing consent like a nonresident member's missing agreement (§18633.5(i)(2)).
- **The amount.** The payment is the highest marginal rate multiplied by the owner's share of the California-source income on the return. It is reduced by any nonresident withholding the LLC has already paid for the owner.
- **Rates (2025 Form 568 booklet).** These are the rates for 2025. Check the 2026 booklet when it is published.

| Owner type | Schedule T rate, 2025 ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html)) |
|---|---|
| Individual, partnership, LLC, estate or trust | 12.3% |
| C corporation | 8.84% |
| S corporation | 1.5% |

- **When it is due.** The Schedule T tax is due by the **original** due date of Form 568. If it is not paid on time, it is treated as the LLC's tax for the late-payment penalty and interest. No penalty or interest is imposed on the LLC for this if the owner files and pays all California tax on the LLC's income on time (§18633.5(e)(3)).
- **Credit to the owner.** The payment counts as a payment by the owner on account of the owner's California income tax for the year (§18633.5(g)). The owner still files Form 540NR.

### Corporate owner: Form 100 or 100S ([2025 Form 100 booklet](https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html))

- **Where the income goes.** Form 100 Question CC asks whether the corporation owns an SMLLC. The FTB says: "an SMLLC reports its income, deductions, and credits on Form 100. However, the SMLLC is required to file a Form 568 regardless of its inclusion on this form."
- **Due date.** An SMLLC owned by a C corporation files by the 15th day of the 4th month after the close of the owner's year. One owned by an S corporation files by the 15th day of the 3rd month (see the table above).
- **Credit limit.** The corporation applies the credit limit below on Schedule P (100).
- **Nonresident corporate owner.** A foreign corporation that owns the SMLLC signs the consent or faces Schedule T at the corporate rate in the table above.

### Credit limit, for every owner

"Utilization of credits attributable to the SMLLC is limited to the regular tax liability on the income attributable to the activities of the SMLLC" (2025 Form 568 booklet). The owner computes its tax with and without the SMLLC's items. The difference is the most the SMLLC's credits can offset.

## Penalties ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

- **Late annual tax.** If the $800 is not paid by the 15th day of the 4th month, a late-payment penalty and interest run from that date ([2026 FTB 3522 instructions](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf)). Pay a late prior-year tax on that year's form 3522, not the current one.
- **Late payment** (R&TC §19132). This starts at 5% and rises by 0.5% for each month or part of a month unpaid, up to 25%. For the fee balance and the Schedule T tax, it runs from the original due date of the return.
- **Late filing** (R&TC §19131). This is 5% of the unpaid tax, which includes the LLC fee and the Schedule T tax, for each month or part of a month the return is late, up to 25%. If Form 568 is filed after the extended due date, the extension falls away and the penalty runs from the **original** due date. Together, the late-filing and late-payment penalties may not exceed 25% of the unpaid tax. The FTB presumes reasonable cause for the late-payment penalty when 90% of the tax is paid by the original due date.
- **Estimated fee.** 10% of the underpayment, with the prior-year safe harbor above.
- **Per-member penalty.** The Form 568 booklet describes a penalty for filing late (including extensions) or filing an incomplete return: $18 times the number of members, for each month or part of a month, up to 12 months. For one member, the most is $216. The statute it cites, R&TC §19172, is written for a "partnership" ([R&TC §19172](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19172.)). Whether the FTB charges it to a disregarded SMLLC is not clear from these texts. Warn the client it may be charged, and ask for abatement for reasonable cause if it is.
- **Unregistered foreign or suspended SMLLC** (R&TC §19135). If it is doing business in California and does not file within 60 days after an FTB notice and demand, it is charged $2,000 per taxable year, unless it has reasonable cause ([R&TC §19135](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19135.)).
- **Interest** runs on unpaid amounts from the original due date. Use the FTB's current rate. This Guide does not quote one.

## Boundary and exception table ([R&TC §17946](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17946.))

| Situation | Result |
|---|---|
| Taxable year of **15 days or less**, and **no business** done in California in that period | No Form 568, no annual tax and no fee for that year (§17946). For a calendar-year owner, that means an SOS filing on 17 December or later |
| SOS filing on 16 December (a 16-day year), or any business done in a short year | §17946 not met. $800 is owed for that year, due by 15 March (December is month 1) |
| Sole owner a deployed member of the US Armed Forces; California total income $250,000 or less; the SMLLC operates at a loss or ceases operation that year | No annual tax for that year (§17941(f)), for taxable years beginning before 1 January 2030. Enter zero on Form 568 lines 2 and 3, and print "Deployed Military" in the top margin of the return |
| Domestic LLC files the short form cancellation (SOS form LLC-4/8) within 12 months of filing its articles and meets every condition below | Not subject to the annual tax for its first taxable year |
| Foreign disregarded SMLLC, not registered and not doing business in California | No Form 568. The owner reports any California-source income |
| California sales exactly equal to the lesser §23101 amount | "Exceed" is not met. Check the other tests |
| LLC elected to be taxed as a corporation | Outside Form 568. It files Form 100 or 100S |
| California total income just below the first fee band | No fee. Check that interest, gains and other income have all been included on Schedule IW before relying on it |

## Worked cases ([R&TC §17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.))

### Case A: resident consultant, under the fee threshold (2026) ([FTB: Limited liability company](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html))

- **Facts.** A California SMLLC formed in 2023, owned by a resident individual who uses the calendar year. 2026 consulting fees are $180,000, all from California clients, with no other income.
- **Annual tax.** $800, due 15 April 2026 on form 3522.
- **Fee.** California total income is $180,000, below $250,000, so there is no fee and no form 3536.
- **Return.** Form 568 (Sides 1, 2, 3 and 7) is due 15 April 2027. The owner reports the business on Form 540. The total 2026 entity-level charge is $800.

### Case B: reseller, cost of goods sold added back (2026) ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

- **Facts.** A California SMLLC, individual owner, calendar year. It sells goods delivered only to California buyers. 2026 gross receipts are $620,000 and cost of goods sold is $400,000, so gross income is $220,000. Its 2025 fee was $900, and it paid $900 on form 3536 by 15 June 2026.
- **Base.** Gross income $220,000 plus cost of goods sold $400,000 gives $620,000.
- **Fee.** $620,000 is in the $500,000 to $1,000,000 band, so the fee is $2,500. Subtracting cost of goods sold would have given $220,000 and a nil fee. That is the error to avoid.
- **Estimate.** $900 was paid by 15 June, which equals the 2025 fee, so there is no 10% penalty. The balance of $2,500 − $900 = $1,600 is due by 15 April 2027 with form 3536 (or 3537).
- **Total entity-level charge for 2026:** $800 + $2,500 = $3,300.

### Case C: new SMLLC formed in September 2026 (first year) ([2026 FTB 3522 instructions](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf))

- **Facts.** An individual with a calendar year files articles for a California SMLLC on 10 September 2026 and starts trading at once.
- **First-year tax.** Count September as month 1. The 4th month is December, so $800 is due by 15 December 2026. No first-year relief applies to a first year beginning in 2026.
- **Estimated fee.** The 6th month is February 2027. The 2026 taxable year ends on 31 December 2026, before then, so no estimated fee is due for 2026. Any 2026 fee is due with the return on 15 April 2027.
- **Second year.** Another $800 is due on 15 April 2027 for 2027. It is $800, not $400, because the first taxable year began in 2026.

### Case D: nonresident owner, 2025 return filed on extension ([R&TC §18633.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.))

- **Facts.** A Nevada resident individual owns a California SMLLC, calendar year. In 2025 its California total income was $300,000 and its California-source net income was $120,000. The $800 for 2025 was paid on 15 April 2025.
- **Entity charges.** Fee $900 (the $250,000 to $500,000 band). The estimate was due on form 3536 by 15 June 2025. Any unpaid balance was due 15 April 2026, even though the return is extended to 15 October 2026.
- **Consent signed.** The owner signs the consent on Side 3 and reports the $120,000 on Form 540NR, Schedule CA (540NR) column E.
- **Consent not signed.** The SMLLC completes Schedule T and pays 12.3% × $120,000 = $14,760 by 15 April 2026, less any nonresident withholding already paid for the owner. That payment is credited to the owner, who must still file Form 540NR.

### Case E: 2025 return filed after the extended date (penalty) ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

- **Facts.** An SMLLC owned by a resident individual, calendar year. The 2025 fee is $900 and the 2024 fee was nil. The $800 was paid on time, but nothing was paid toward the fee. Form 568 is filed on 20 November 2026, after the extended date of 15 October 2026.
- **Estimate penalty.** None. The prior-year fee was nil, so the safe harbor is met.
- **Late filing.** Filing after the extended date means the penalty runs from 15 April 2026. That is eight months or parts of months, so 5% × 8 = 40%, capped at 25%. The penalty is 25% × $900 = $225.
- **Late payment.** Combined with late filing, the two may not exceed 25% of the unpaid tax, so the two together are $225 at most.
- **Per-member penalty (if charged).** Filing after the extended date loses the extension, so this also counts from 15 April 2026: eight months or parts of months, so $18 × 8 = $144. Whether it applies to an SMLLC at all is the open point under Penalties.
- **Interest** runs on the $900 from 15 April 2026.

### Case F: cancelling a calendar-year SMLLC (2026) ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

- **Facts.** A California SMLLC, individual owner, stops all business on 30 June 2026. The $800 for 2026 was paid on 15 April 2026.
- **2026.** The $800 for 2026 is not prorated. The 2026 fee is still computed on the total income for the final year, here January to June. File a final 2026 Form 568, final return box checked, by 15 April 2027 (15 October 2027 on extension).
- **SOS filings.** Form LLC-3 (dissolution) and form LLC-4/7 (cancellation).
- **Stopping the 2027 tax.** No 2027 tax is assessed only if all three conditions under Cancelling the SMLLC are met. The safest course is to file the SOS cancellation before 31 December 2026. If it is filed later, "a subsequent year return and an additional $800 tax may be required."

## When to refuse or refer

- **Classification is unclear.** This includes an SMLLC that elected corporate status, a pre-1997 foreign SMLLC still classified as a corporation for California, or a second member admitted during the year. Refer.
- **Nexus is disputed.** This includes an out-of-state SMLLC that is near the §23101 thresholds, has agents or staff in California, or relies on Public Law 86-272 (which does not remove the annual tax or fee; see ca-llc-fee-and-tax). Refer to a California multistate specialist.
- **Back years unfiled or suspended.** Refer voluntary disclosure, revivor and penalty abatement to a specialist.
- **Multistate apportionment** for the owner or for the Schedule IW assignment of services, intangibles or real property.
- **Nonresident withholding** (forms 592 and 592-B) and the pass-through entity elective tax. These use other rules.
- **Corporate owner in a combined report** or with a non-unitary SMLLC.
- **Tiered structures.** An SMLLC that owns other LLCs (amounts already subject to the fee are excluded), or one owned by a partnership.
- **Commonly controlled LLCs** that the FTB may aggregate for the fee (§17942(b)(2)). See **ca-llc-fee-and-tax**.

## Filing and payment ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

| Step | Form | Due (calendar-year individual owner, tax year 2026) |
|---|---|---|
| Annual tax | FTB 3522 | 15 April 2026. First year: 15th day of the 4th month counting the SOS filing month as month 1 |
| Estimated fee | FTB 3536 | 15 June 2026, if a fee is expected |
| Return | Form 568 | 15 April 2027 (other owners: see the due-date table) |
| Fee balance and any Schedule T tax | FTB 3536, or FTB 3537 if filing on extension | 15 April 2027, the original due date |
| Extended return | Form 568 | 15 October 2027, with no extension form |
| Owner's return | Form 540, 540NR, 100 or 100S | The owner's own due date |

- **Paying.** Pay by Web Pay, electronic funds withdrawal, credit card, or by mail with the voucher. If paying by Web Pay or credit card, do not also mail the voucher.

### Cancelling the SMLLC ([FTB: Limited liability company](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html))

- **Steps.** File a timely final Form 568 and pay the $800 for the final year. File form LLC-4/7, Certificate of Cancellation, with the SOS. A domestic LLC also files form LLC-3, Certificate of Dissolution. The effective date of form LLC-4/7 stops the $800 for future years. A "final" return alone does not stop it.
- **No tax for the following year** only if **all** of these are met ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html)):
  - the final return for the preceding year is filed on time, including any extension;
  - the SMLLC does no business in California after the final taxable year; and
  - the SOS cancellation is filed within 12 months of that timely final return.
- **Short form cancellation** (form LLC-4/8). This is available only to a domestic LLC, and only if **all** of these are true:
  - it is filed within 12 months of the date the articles were filed;
  - the LLC has no debts or liabilities other than tax;
  - its known assets have been distributed, or none were acquired;
  - the final return has been or will be filed with the FTB;
  - it has done no business since filing its articles;
  - a majority of managers or members (or of the organizers, if there are none) voted to dissolve; and
  - any investor payments have been returned.

  If all are met, "Your LLC will not be subject to the annual $800 tax for its first tax year."

### 2025 returns, including those filed on extension ([FTB: Doing business in California](https://www.ftb.ca.gov/file/business/doing-business-in-california.html))

- **Same rates.** The $800 annual tax, the fee bands and the 10% estimate penalty were the same for 2025.
- **Deadlines for a calendar-year individual owner.** The 2025 annual tax was due 15 April 2025, the estimated fee 15 June 2025, and Form 568 15 April 2026. The automatic six-month extension runs to 15 October 2026.
- **Paying late.** Any fee or Schedule T tax paid with an extended return is late. Penalty and interest run from 15 April 2026.
- **First-year relief.** An SMLLC formed in 2024 or 2025 had none.
- **Thresholds and rates.** The doing-business amounts and Schedule T rates quoted above are the 2025 figures.

## Completion checklist ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

- [ ] Single owner and disregarded status confirmed. No corporate election.
- [ ] Trigger recorded: organized, registered, or doing business under §23101, with each test run against the lesser of 25% and that year's indexed amount.
- [ ] Exceptions checked: 15-day year, deployed-military exemption, short form cancellation.
- [ ] Owner's taxable year used. Form 3522 paid by the 15th day of the 4th month (first year: SOS filing month is month 1), separately from Form 568.
- [ ] Schedule IW built from the owner's federal schedules: gross income plus cost of goods sold, assigned to California, with no operating expenses deducted.
- [ ] Fee read from the band table in ca-llc-fee-and-tax. Form 3536 payment compared with the prior-year fee.
- [ ] Form 568 Sides 1, 2, 3 and 7 completed. Schedules B and K added if the $3,000,000 tests are met.
- [ ] Owner's consent signed on Side 3, or Schedule T computed and paid by the original due date.
- [ ] Due date matched to the owner type. Fee balance paid by the original due date, whatever the extension.
- [ ] SMLLC income, deductions and credits reported on the owner's Form 540, 540NR, 100 or 100S, with credits limited.
- [ ] If closing: timely final return, SOS cancellation within 12 months of it, and no business afterwards.

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
