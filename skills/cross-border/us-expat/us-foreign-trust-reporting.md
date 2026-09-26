---
name: us-foreign-trust-reporting
description: "US taxation and reporting of foreign trusts for US persons: the court/control tests (IRC §7701), grantor-trust ownership under §671–679 (especially §679), the throwback / accumulation-distribution regime (§665–668) and its interest charge, and Forms 3520 and 3520-A with their penalties. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
version: 0.1
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
depends_on:
  - cross-border-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US reporting of foreign trusts and large foreign gifts (Forms 3520 and 3520-A)

## Scope and who this is for

This Guide covers US federal rules for tax year 2026, with a dated section for 2025 returns. It is for a preparer or a US person who:

- created, funded, or lent to a foreign trust;
- is treated as the owner of any part of a foreign trust under the grantor trust rules (sections 671 to 679);
- received a distribution, a loan, or the free use of property from a foreign trust;
- received large gifts or bequests from foreign persons.

It covers four things: whether the trust is foreign, who (if anyone) is the owner, how a US beneficiary is taxed on distributions (including the throwback tax and its interest charge), and which of Form 3520 and Form 3520-A must be filed, when, and with what penalties.

It does not cover the foreign country's own treatment of the trust, FBAR (FinCEN Form 114) or Form 8938 in detail, estate and gift tax planning, or the section 2801 tax on gifts from covered expatriates. Those are flagged for referral below.

The Form 3520 instructions in force are the 12/2025 revision, which applies "for tax year 2025 and subsequent years until a superseding revision is issued" ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)). The only figure in this Guide that changes by year is the foreign corporation and partnership gift threshold.

## Ask the client first

- Who created the trust, and who has transferred money or property to it since? When, and for what consideration? Was any transferor a US person at the time, or within 5 years before becoming a US resident ([26 U.S.C. 679](https://www.law.cornell.edu/uscode/text/26/679))?
- Where is the trustee, which law governs, and who controls each substantial decision (distributions, investments, adding or removing beneficiaries, replacing the trustee, ending the trust)?
- Can the settlor revoke the trust alone, or can only the settlor and spouse receive anything during the settlor's life?
- Who are the beneficiaries, including contingent ones and any US persons who could ever benefit?
- What did the client receive from the trust this year: cash, property, a loan, the rent-free use of a house or car, card charges paid by the trust?
- Did the trust send a Foreign Grantor Trust Owner Statement, a Foreign Grantor Trust Beneficiary Statement, or a Foreign Nongrantor Trust Beneficiary Statement? Has it appointed a US agent?
- Does the trust have year-by-year records of income, distributions and undistributed net income? How many years has it been a foreign trust, and what did it distribute to the client in each of the last 3 years?
- Is the "trust" really a foreign pension, retirement, medical, disability or education plan (for example a Canadian RRSP or a workplace pension)?
- Separately from any trust: what gifts or bequests did the client receive from nonresident aliens, foreign estates, foreign corporations or foreign partnerships this year, from whom, and are any of the donors related to each other?
- Has the client already filed, filed late, or never filed Forms 3520 or 3520-A for earlier years?

## The method, step by step

1. **Decide whether the trust is foreign.** A trust is domestic only if both tests are met: "a court within the United States is able to exercise primary supervision over the administration of the trust, and one or more United States persons have the authority to control all substantial decisions of the trust" ([26 U.S.C. 7701(a)(30)(E)](https://www.law.cornell.edu/uscode/text/26/7701)). A foreign trust is "any trust other than" that. If either test is not clearly met on the documents, treat the trust as foreign and flag it.
2. **Check the reporting exceptions before anything else.** Some arrangements are trusts for US purposes but need no Form 3520 or 3520-A (see the boundary table): Canadian RRSPs and RRIFs under Rev. Proc. 2014-55, tax-favored foreign retirement and non-retirement savings trusts under Rev. Proc. 2020-17, and the proposed section 6048 regulations. An exception from reporting does not change income tax, FBAR or Form 8938 duties.
3. **Test for a foreign owner first (section 672(f)).** The grantor trust rules apply only to the extent they make a US citizen, resident or domestic corporation currently taxable. A foreign person is treated as owner only if (i) the settlor alone (or with a related or subordinate party subservient to the settlor) can revest the property in the settlor, or (ii) during the settlor's life the only amounts distributable are to the settlor or the settlor's spouse ([26 U.S.C. 672(f)](https://www.law.cornell.edu/uscode/text/26/672)). A trust whose distributions are taxable as pay for services is also outside the limit (672(f)(2)(B)). And if a US beneficiary has made gifts (other than annual-exclusion gifts) to the foreign person who would otherwise be owner, that beneficiary is treated as the grantor of the portion to that extent (672(f)(5)). A typical irrevocable discretionary trust set up by a non-US parent for a family that includes US children is therefore a foreign **nongrantor** trust.
4. **Test for a US owner (sections 673 to 679).** A US person is owner of a portion if an ordinary grantor-trust power applies, or under section 679: "A United States person who directly or indirectly transfers property to a foreign trust ... shall be treated as the owner ... of the portion of such trust attributable to such property if for such year there is a United States beneficiary of any portion of such trust" ([26 U.S.C. 679](https://www.law.cornell.edu/uscode/text/26/679)). Apply it to each US person separately; one trust can have several owners of different portions.
5. **Apply the section 679 details.**
   - A trust has a US beneficiary unless no income or corpus may be paid or accumulated for a US person, and none could be paid to one if the trust ended. A contingent interest counts.
   - Exceptions: transfers by reason of death, and transfers for at least fair market value (trust and related-party obligations are not counted as consideration).
   - A nonresident who becomes a US resident within 5 years after a transfer is treated as transferring it again on the residency starting date (679(a)(4)).
   - A domestic trust funded by a US citizen or resident that becomes foreign while that individual is alive is treated as a new transfer on that date (679(a)(5)).
   - A beneficiary who first became a US person more than 5 years after the transfer is disregarded (679(c)(3)).
   - If the trust lends cash or marketable securities to a US person who does not repay it at a market rate of interest within a reasonable period, or lets a US person use trust property without paying its fair market value within a reasonable period, the trust is treated as having a US beneficiary (679(c)(6)). The statute: "The preceding sentence shall not apply to the extent that the United States person repays the loan at a market rate of interest (or pays the fair market value of the use of such property) within a reasonable period of time" ([26 U.S.C. 679](https://www.law.cornell.edu/uscode/text/26/679); [Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).
6. **If there is a US owner:** the owner reports the trust income on their own return each year, whether or not anything is distributed ([IRS foreign trust page](https://www.irs.gov/businesses/international-businesses/foreign-trust-reporting-requirements-and-tax-consequences)). The owner files Form 3520 Part II every year, even with no transactions, and must make sure the trust files Form 3520-A. If the trust will not file, the owner attaches a substitute Form 3520-A to their Form 3520. A distribution to the owner from the owned portion is reported only on lines 24 and 27 of Part III, so the DNI, default and throwback schedules do not apply to it; the owner is already taxed on that portion's income as it is earned ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).
7. **If a US person transferred appreciated property to a foreign nongrantor trust:** check for gain under section 684 ([IRS foreign trust page](https://www.irs.gov/businesses/international-businesses/foreign-trust-reporting-requirements-and-tax-consequences)).
8. **If a US beneficiary received a distribution from a nongrantor trust:**
   - Current-year distributable net income (DNI) comes out first. For a foreign trust, DNI includes net capital gains ([26 U.S.C. 643(a)(6)](https://www.law.cornell.edu/uscode/text/26/643)).
   - Anything above DNI is an accumulation distribution ([26 U.S.C. 665](https://www.law.cornell.edu/uscode/text/26/665)). It carries the throwback tax (Form 4970) plus the section 668 interest charge.
   - Choose the calculation. Use Schedule B (actual) only if the trust gave a Foreign Nongrantor Trust Beneficiary Statement and Schedule A has never been used for this trust. Otherwise use Schedule A (default). Without adequate records, section 6048(c)(2) treats the distribution as an accumulation distribution ([26 U.S.C. 6048](https://www.law.cornell.edu/uscode/text/26/6048)).
9. **If the distribution came from a trust owned by a foreign person** and the beneficiary has a complete Foreign Grantor Trust Beneficiary Statement: treat it as if paid directly by the owner (for example, a gift is not income), and report it in Part III with the statement attached ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).
10. **Treat loans and free use as distributions.** A loan of cash or marketable securities, or use of trust property, to a US grantor or beneficiary (or a related US person) is treated as a distribution of the loan amount or of the fair value of the use. For use of property other than a loan of cash or securities, the rule does not apply to the extent fair market value is paid within a reasonable period ([26 U.S.C. 643(i)](https://www.law.cornell.edu/uscode/text/26/643)). A loan that keeps its status as a qualified obligation is reported on Form 3520 but, if it loses that status, the holder is treated as receiving a taxable distribution ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).
11. **Run the foreign gift test separately (Part IV).** Apply the thresholds in the next section, aggregating related donors. Anything received from a foreign trust goes in Part III, not Part IV.
12. **Fix the filings and deadlines,** check for late years, and write the working paper (see Filing and payment).

## Thresholds and figures, with years

| Item | Amount | Year | Source |
|---|---|---|---|
| Part IV: gifts or bequests from nonresident aliens or foreign estates (aggregate donors you know or have reason to know are related, and nominees) | more than $100,000 | every year (not indexed) | [IRS gifts from foreign person](https://www.irs.gov/businesses/gifts-from-foreign-person) |
| Once over that threshold, each gift to be listed separately | each gift over $5,000 | every year | [IRS gifts from foreign person](https://www.irs.gov/businesses/gifts-from-foreign-person) |
| Part IV: purported gifts from foreign corporations or partnerships (related persons aggregated) | exceeds $20,573 | taxable years beginning in 2026 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Same threshold | exceeds $20,116 | taxable years beginning in 2025 | [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| Form 3520 penalty: unreported transfer (Part I) or distribution (Part III) | greater of $10,000 or 35% of the gross amount | every year | [26 U.S.C. 6677](https://www.law.cornell.edu/uscode/text/26/6677) |
| Form 3520-A penalty (charged to the US owner) | greater of $10,000 or 5% of the gross value of the owned portion at the close of the year | every year | [26 U.S.C. 6677](https://www.law.cornell.edu/uscode/text/26/6677) |
| Continuation penalty after 90 days from IRS notice | $10,000 for each 30-day period or part of one | every year | [26 U.S.C. 6677](https://www.law.cornell.edu/uscode/text/26/6677) |
| Unreported foreign gift | 5% of the gift per month, at most 25% | every year | [26 U.S.C. 6039F](https://www.law.cornell.edu/uscode/text/26/6039F) |
| Accuracy penalty on underpayment tied to a Form 3520-A asset | 20% raised to 40% | every year | [Instructions for Form 3520](https://www.irs.gov/instructions/i3520) |
| Throwback interest before 1996 | 6% simple | periods 1977 to 1995 | [Instructions for Form 3520](https://www.irs.gov/instructions/i3520) |
| Rev. Proc. 2020-17 retirement trust contribution limit (met by a percentage-of-earned-income limit, or either amount shown) | annual limit of $50,000 or less, or lifetime limit of $1,000,000 or less | every year | [Rev. Proc. 2020-17](https://www.irs.gov/pub/irs-drop/rp-20-17.pdf) |
| Rev. Proc. 2020-17 non-retirement savings trust contribution limit | $10,000 or less annually or $200,000 or less lifetime | every year | [Rev. Proc. 2020-17](https://www.irs.gov/pub/irs-drop/rp-20-17.pdf) |

Notes on the penalties:

- The Form 3520 and 3520-A penalties are charged once for each failure. The 5% figure is not charged monthly. The monthly penalty is the separate foreign gift penalty.
- Once the IRS can determine the gross reportable amount, later section 6677 penalties are reduced so the total does not exceed it ([26 U.S.C. 6677](https://www.law.cornell.edu/uscode/text/26/6677)).
- **Reasonable cause:** no section 6677 or 6039F penalty applies if the failure was due to reasonable cause and not willful neglect. Section 6677(d): "No penalty shall be imposed by this section on any failure which is shown to be due to reasonable cause and not due to willful neglect" ([26 U.S.C. 6677](https://www.law.cornell.edu/uscode/text/26/6677)). Section 6039F(c)(2): the penalty "shall not apply to any failure to report a foreign gift if the United States person shows that the failure is due to reasonable cause and not due to willful neglect" ([26 U.S.C. 6039F](https://www.law.cornell.edu/uscode/text/26/6039F)). A foreign-law penalty for disclosure, or a trustee's refusal to provide information, is not reasonable cause ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).
- Deficiency procedures do not apply to section 6677 penalties ([26 U.S.C. 6677(e)](https://www.law.cornell.edu/uscode/text/26/6677)).
- For an unreported foreign gift, the IRS may also decide the income tax consequences of the gift itself ([26 U.S.C. 6039F](https://www.law.cornell.edu/uscode/text/26/6039F)).
- After 1995, throwback interest compounds daily at the underpayment rate, and it also runs on the pre-1996 simple interest.
- **Cap:** the throwback tax plus interest cannot exceed the accumulation distribution: "The total amount of the interest charge shall not, when added to the total partial tax computed under section 667(b), exceed the amount of the accumulation distribution (other than the amount of tax deemed distributed by section 666(b) or (c))" ([26 U.S.C. 668](https://www.law.cornell.edu/uscode/text/26/668)). The interest charge is not deductible.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Gifts from nonresident aliens total exactly $100,000 in the year | Not reportable in Part IV; the test is "more than" ([IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person)) |
| Two nonresident donors you know are related give $75,000 and $40,000 | Aggregate; report, listing each gift over $5,000 ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)) |
| Foreign person pays tuition or medical bills directly | Not a foreign gift (qualified transfer under section 2503(e)(2)) ([26 U.S.C. 6039F](https://www.law.cornell.edu/uscode/text/26/6039F)) |
| Money from a foreign trust described as a "gift" | Report as a distribution in Part III, not Part IV ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)) |
| Purported gift from a foreign corporation or partnership | Reportable above the threshold, and the IRS may recharacterize it (section 672(f)(4)) ([26 U.S.C. 672](https://www.law.cornell.edu/uscode/text/26/672)) |
| Canadian RRSP, RRIF or other plan within Rev. Proc. 2014-55 | No Form 3520 or 3520-A ([Instructions for Form 3520-A](https://www.irs.gov/instructions/i3520a)) |
| Foreign pension or savings trust meeting every test in Rev. Proc. 2020-17 section 5, held by an eligible individual who is compliant with US return filing and has reported any taxable amounts | No Form 3520 or 3520-A; penalties already assessed can be challenged on Form 843 ([Rev. Proc. 2020-17](https://www.irs.gov/pub/irs-drop/rp-20-17.pdf)) |
| Tax-favored foreign trust covered by the proposed regulations section 1.6048-5 | May rely on them for tax years ending after May 8, 2024, only if the individual and all related persons apply them in full and consistently ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)) |
| Section 402(b) funded deferred compensation, section 404(a)(4) foreign pension trusts, section 404A qualified foreign plans | No Form 3520 ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)) |
| Most transfers to a foreign trust for fair market value | No Form 3520. Report anyway if the transfer is for a qualified obligation, is of appreciated property with gain not fully recognized, or is by a related US transferor ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)) |
| Distribution taxable as pay for services, reported as such | No Form 3520 for it ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)) |
| Foreign law would penalize disclosure, or the trustee refuses to give information | Not reasonable cause ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)) |
| Trust whose foreign settlor can revoke it alone | Foreign grantor trust owned by a foreign person; US beneficiary follows step 9 ([26 U.S.C. 672](https://www.law.cornell.edu/uscode/text/26/672)) |

## Worked cases

These are illustrations with invented amounts, not advice.

### Case 1: gifts from two related nonresident parents, 2026 ([IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person))

A US citizen receives $60,000 from her nonresident mother and $45,000 from her nonresident father in 2026. The donors are related, so aggregate: $105,000 is more than $100,000. She files Form 3520 Part IV and lists both gifts, because each is over $5,000. The gifts are not income. If she files late with no reasonable cause, the penalty is 5% of the gifts per month, up to 25% ([26 U.S.C. 6039F](https://www.law.cornell.edu/uscode/text/26/6039F)).

### Case 2: exactly at the threshold ([IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person))

A US resident receives one bequest of $100,000 from a foreign estate in 2026 and nothing else from foreign persons. The amount does not exceed $100,000, so there is no Part IV requirement. Check first whether any other gift came from a related foreign person; if so, it must be added in.

### Case 3: purported gift from a foreign company, 2026 ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf))

A foreign corporation owned by the client's nonresident uncle sends the client $21,000 in 2026, called a gift. It exceeds $20,573, so Part IV line 55 applies. Before treating it as a gift, consider whether it is really pay, a dividend or a distribution, because the IRS may recharacterize it ([26 U.S.C. 672](https://www.law.cornell.edu/uscode/text/26/672)).

### Case 4: unreported distribution from a foreign nongrantor trust ([26 U.S.C. 6677](https://www.law.cornell.edu/uscode/text/26/6677))

A US beneficiary received $200,000 from a foreign nongrantor trust and filed no Form 3520. The initial penalty is the greater of $10,000 or 35% of $200,000, which is $70,000. More is added at $10,000 per 30-day period if the failure continues more than 90 days after an IRS notice. The total cannot exceed the gross reportable amount. Separately, the assessment period for related tax stays open until 3 years after the information is reported (section 6501(c)(8)) ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).

### Case 5: US owner, trust files no Form 3520-A ([Instructions for Form 3520-A](https://www.irs.gov/instructions/i3520a))

A US citizen is the section 679 owner of a foreign trust whose assets are worth $150,000 at year end. The trustee will not file Form 3520-A. If the owner attaches a substitute Form 3520-A to a timely Form 3520, there is no penalty for the trust's failure. If neither is filed, the penalty is the greater of $10,000 or 5% of $150,000 ($7,500), so $10,000 ([26 U.S.C. 6677](https://www.law.cornell.edu/uscode/text/26/6677)).

### Case 6: default calculation of a distribution (Schedule A) ([Form 3520](https://www.irs.gov/pub/irs-pdf/f3520.pdf))

The trust has been foreign for 10 years, including 2026, and the beneficiary has no Foreign Nongrantor Trust Beneficiary Statement. Distributions to the beneficiary in the 3 preceding years total $12,000, and the 2026 distribution is $40,000.

- Line 34: $12,000 times 1.25 is $15,000 ([Form 3520](https://www.irs.gov/pub/irs-pdf/f3520.pdf)).
- Line 35: $15,000 divided by 3.0 is $5,000 ([Form 3520](https://www.irs.gov/pub/irs-pdf/f3520.pdf)). If the trust has been foreign for fewer than 3 years, divide by that number of years instead, and in the trust's first year as a foreign trust do not complete the rest of Part III ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).
- Line 36: the smaller of $40,000 and $5,000 is $5,000, taxed as ordinary income ([Form 3520](https://www.irs.gov/pub/irs-pdf/f3520.pdf)).
- Line 37: $35,000 is the accumulation distribution ([Form 3520](https://www.irs.gov/pub/irs-pdf/f3520.pdf)).
- Line 38: the applicable number of years is 10 divided by 2.0, which is 5.

Tax on the $35,000 is computed on Form 4970. Interest is then added, and the combined tax and interest cannot exceed $35,000, measured without any tax deemed distributed under section 666(b) or (c) ([26 U.S.C. 668](https://www.law.cornell.edu/uscode/text/26/668)). Once Schedule A is used for a trust, it must generally be used in later years too. The only exception is Schedule B in the year the trust ends, if a statement is received that year.

### Case 7: foreign settlor, US child ([26 U.S.C. 672](https://www.law.cornell.edu/uscode/text/26/672))

A nonresident grandmother sets up an irrevocable discretionary trust abroad for her grandchildren, one of whom is a US citizen. She cannot revoke it, and the trust can pay the grandchildren in her lifetime, so section 672(f) stops her being treated as owner. The trust is a foreign nongrantor trust. The US grandchild reports each distribution in Part III (Case 6 method if there is no statement). The trust files no Form 3520-A, because it has no US owner. If instead she could revoke it alone, she would be the foreign owner. A distribution to the grandchild backed by a complete Foreign Grantor Trust Beneficiary Statement would then be treated as a gift from her, still reported in Part III.

### Case 8: workplace pension abroad ([Rev. Proc. 2020-17](https://www.irs.gov/pub/irs-drop/rp-20-17.pdf))

A US citizen working abroad belongs to an employer pension. It is tax-favored locally and reported to the local tax authority. Only earned-income contributions are allowed, with a cap by percentage of pay, and withdrawals are locked until retirement age. If every section 5.03 test is met and the client is compliant with US return filing, no Form 3520 or 3520-A is needed. FBAR and Form 8938 may still apply, and so may US income tax on the plan.

## When to refuse or refer

- Refer the foreign country's tax treatment of the trust, its distributions and gains to a local adviser. The two systems often characterize the same trust differently, and relief from double tax is not automatic.
- Refer if the client did not file Forms 3520 or 3520-A in earlier years and wants to fix it. How to come into compliance and argue reasonable cause is a judgement call with large penalties at stake. Do not promise that penalties will be waived.
- Refer when a trust has a long accumulation history and no records. The default method applies, and the throwback tax plus interest can take most of the accumulation distribution.
- Refer section 684 gain on transfers of appreciated property to a foreign nongrantor trust, trust migrations under section 679(a)(5), and pre-immigration trust planning under section 679(a)(4).
- Refer gifts or bequests from a former US citizen or green-card holder who may be a covered expatriate. The section 2801 tax may apply ([IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person)), and Form 708 may be required ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).
- Refer any case where a US owner or beneficiary is giving up citizenship or long-term residence, or plans to sell trust assets around a change of status. The section 877A exit tax and the section 679 ownership answer interact, and the order of steps changes the result.
- Refuse to treat an arrangement as outside these rules just because a promoter says so. The IRS warns about abusive foreign trust schemes ([IRS foreign trust page](https://www.irs.gov/businesses/international-businesses/foreign-trust-reporting-requirements-and-tax-consequences)).

## Filing and payment steps with deadlines

- **Form 3520 (US person):** due on the 15th day of the 4th month after the end of the tax year. For a calendar-year individual, the 2026 form is due April 15, 2027 ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).
  - A US citizen or resident who lives and has their place of business or post of duty outside the US and Puerto Rico, or is on military duty abroad, gets until the 15th day of the 6th month. A statement must be attached.
  - An extension of the income tax return extends Form 3520 to no later than the 15th day of the 10th month (October 15). Check box 1k and enter the return's form number.
  - The discretionary 2-month extension to December 15 does not extend Form 3520 ([IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person)).
  - The form is filed separately from the income tax return, by mail to Internal Revenue Service Center, P.O. Box 409101, Ogden, UT 84409. Use one Form 3520 per foreign trust. Spouses filing jointly may file one joint Form 3520 if both are transferors, grantors or beneficiaries of the same trust.
  - Only a complete form, with all attachments, counts as timely.
- **Form 3520-A (foreign trust with a US owner):** due on the 15th day of the 3rd month after the trust's year end ([Instructions for Form 3520-A](https://www.irs.gov/instructions/i3520a)).
  - The trust must also send the Owner and Beneficiary Statements to its US owners and beneficiaries by that date.
  - To extend, file Form 7004 under the trust's EIN by the same date. The owner's income tax extension does not extend Form 3520-A.
  - The trustee signs.
  - A substitute Form 3520-A, signed by the US owner, is due with the owner's Form 3520, and copies of the statements go out by the same date.
- **US agent:** if a foreign trust with a US owner has no US agent named on Form 3520 lines 3a to 3g, the IRS may redetermine the owner's amounts ([Instructions for Form 3520](https://www.irs.gov/instructions/i3520)).
- **Tax due:** income of an owned portion, DNI, and throwback tax are paid with the income tax return. The Schedule C total goes on Schedule 2 (Form 1040) as additional tax. Use Form 8082 if a return treats an item differently from the trust's Form 3520-A.
- **Also consider:** FBAR (FinCEN Form 114) and Form 8938. A Form 3520 filer who also files Form 8938 checks item C.

## 2025 returns (tax year 2025, extended deadline October 15, 2026)

- The foreign corporation and partnership gift threshold for 2025 is $20,116 ([Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf)). The nonresident alien and foreign estate threshold is still more than $100,000 ([IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person)).
- For a calendar-year individual, the 2025 Form 3520 was due April 15, 2026, or June 15, 2026 for a qualifying person abroad. With a timely Form 4868 it is due October 15, 2026, and this cannot be extended further ([IRS gifts page](https://www.irs.gov/businesses/gifts-from-foreign-person)).
- If the trust missed its 2025 Form 3520-A, the owner's substitute must be attached to the 2025 Form 3520 by that same date to avoid the penalty.
- The same 12/2025 instructions apply to 2025 and 2026.

## Completion checklist

- [ ] Court test and control test both applied; foreign or domestic conclusion stated.
- [ ] Rev. Proc. 2014-55, Rev. Proc. 2020-17 and proposed section 1.6048-5 exceptions tested before any form is prepared.
- [ ] Section 672(f) applied for any foreign settlor; section 673 to 679 ownership fixed for each US person, with funding history, 5-year residency rule and US-beneficiary test documented.
- [ ] Loans and use of trust property checked under section 643(i).
- [ ] For an owner: income reported currently; Form 3520 Part II filed; Form 3520-A or substitute confirmed; US agent status noted.
- [ ] For a beneficiary: DNI and accumulation distribution computed; Schedule A or B chosen and the consistency rule respected; Form 4970 and interest charge done; section 668 cap applied.
- [ ] Foreign gifts aggregated by related donor and tested against the correct year's thresholds; trust receipts moved to Part III.
- [ ] Deadlines set (Form 3520, Form 3520-A, Form 7004, box 1k) and prior-year gaps listed with penalty exposure.
- [ ] Foreign-country treatment and any section 2801 issue referred.
- [ ] Output labelled as a working paper for a qualified professional to check before filing.

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
