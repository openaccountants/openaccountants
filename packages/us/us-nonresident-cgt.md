---
name: us-nonresident-cgt
description: "US capital gains tax for non-resident aliens: FIRPTA withholding on US real property, ECI rules, FDAP withholding, portfolio interest exemption. Trigger on: \"FIRPTA\", \"non-resident alien US CGT\", \"sell US property non-resident\", \"10% FIRPTA withholding\", \"15% FIRPTA withholding\", \"ECI US non-resident\", \"US real property interest USRPI\", \"withholding certificate FIRPTA\", \"non-resident selling US shares\". For US residents see us-capital-gains."
version: 1.0
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US capital gains of nonresident alien individuals: 2026 method (FIRPTA, 183-day rule, ECI)

This Guide is written for tax year 2026, with a short section for 2025 returns still being filed on extension. It covers one question: when does the United States tax a nonresident alien individual's gain on selling property, and how is the tax collected and reported?

Core sources: [Publication 519, U.S. Tax Guide for Aliens](https://www.irs.gov/publications/p519) (2025 edition, the latest published) and [Publication 515, Withholding of Tax on Nonresident Aliens and Foreign Entities](https://www.irs.gov/publications/p515) (2026 edition). The statutes are [26 U.S.C. 871](https://www.law.cornell.edu/uscode/text/26/871), [26 U.S.C. 897](https://www.law.cornell.edu/uscode/text/26/897) and [26 U.S.C. 1445](https://www.law.cornell.edu/uscode/text/26/1445).

## Scope and who it is for

- **In scope:** individuals who are nonresident aliens for US income tax purposes for the whole year. That includes people treated as nonresidents under a treaty tie-breaker rule (where that claim is not itself in doubt) and "exempt individuals" such as F, J, M or Q students and A or G visa holders. They sell US real property, shares in US companies, other securities or personal property.
- **Out of scope:** US citizens and resident aliens, including green-card holders and anyone who meets the substantial presence test. Use a resident capital-gains Guide for them.
- **Also out of scope:** foreign corporations, partnerships, trusts and estates as sellers; US estate and gift tax; and expatriation tax for former citizens and long-term residents ([Pub 519, ch. 4, Expatriation Tax](https://www.irs.gov/publications/p519)).
- **Dual-status years:** a year that is part resident and part nonresident follows the dual-status rules in [Pub 519, ch. 6](https://www.irs.gov/publications/p519). This Guide applies only to the nonresident part, so refer the year as a whole.

## Ask the client first

- Are you a nonresident alien for the whole of the year of sale? Check this against the green card test and the substantial presence test in [Pub 519, ch. 1](https://www.irs.gov/publications/p519). Also ask whether any treaty tie-breaker claim is made, because that claim needs Form 8833.
- How many days were you physically present in the United States in the tax year of the sale? Were you an exempt individual (a student, teacher, trainee, or foreign-government or international-organization employee) on any of those days?
- Where is your tax home, meaning your main place of work? When you came to the US, did you intend to stay more than one year?
- What exactly was sold? For example: US land or buildings; shares in a US corporation (listed or unlisted, and what percentage of the class you held in the past five years); REIT or other fund shares; a partnership or LLC interest; foreign shares; personal-use items.
- Do you have an office, employees or a fixed place of business in the US? Do you deal in securities, or only trade for your own account through a broker?
- For real property: what is the amount realized (cash, plus the fair market value of other property received, plus any liabilities the buyer assumes or takes the property subject to)? Is the buyer an individual who plans to live in the property? Were there co-owners who are US persons?
- Do you have a US taxpayer identification number (SSN or ITIN)? Has the buyer, closing agent or broker asked for Form W-8BEN or a non-foreign certification?
- Which country are you resident in for treaty purposes, and does that treaty have a capital gains article?
- Did you rent the property out, and have you ever elected to treat that rental income as effectively connected?
- Which states did the property sit in, or did you live or work in during the year? (See the state note below.)

## The method, step by step

1. **Confirm nonresident alien status for the whole year.** If the client is a resident for any part of the year, stop. Use the dual-status or resident rules instead. Treaty tie-breaker nonresidents compute tax as nonresidents and file Form 1040-NR with Form 8833 ([Pub 519, Effect of Tax Treaties](https://www.irs.gov/publications/p519)).
2. **Classify each asset sold.** Is it a US real property interest (USRPI)? If not, is the gain effectively connected income (ECI)? If neither, is it a non-ECI capital gain? Work through steps 3 to 5 in that order, because a USRPI gain is always treated as ECI.
3. **USRPI test (FIRPTA, [26 U.S.C. 897](https://www.law.cornell.edu/uscode/text/26/897)).** Gain or loss on a USRPI is taxed as if the seller were engaged in a US trade or business and is treated as ECI, whether or not the property is a capital asset ([Pub 519, Real Property Gain or Loss](https://www.irs.gov/publications/p519)). See "What counts as a USRPI" below.
4. **ECI test for other assets.** Gain from assets used in or held for a US trade or business is ECI. Trading in stocks or securities for your own account, through a US broker or agent, is **not** a US trade or business. This safe harbour is lost if you have a US office or other fixed place of business through which, or by whose direction, the trades are carried out ([Pub 519, Trading in stocks, securities, and commodities](https://www.irs.gov/publications/p519)). Gain on selling an interest in a partnership that has a US business can be ECI under section 864(c)(8). Refer these cases (see below).
5. **183-day test for non-ECI capital gains ([26 U.S.C. 871(a)(2)](https://www.law.cornell.edu/uscode/text/26/871)).** Apply this only to gains that are neither USRPI nor ECI.
   - If the client was present in the US for **183 days or more** during the tax year, US-source net capital gain is taxed at a flat 30% (or lower treaty) rate ([Pub 519, 183-day rule](https://www.irs.gov/publications/p519)).
   - If presence was **less than 183 days**, these gains are exempt.
   - The threshold is "183 days or more", so exactly 183 days is caught.
   - The rule applies even to sales made while the client was outside the US.
   - A client who is not in a US trade or business and has not established an earlier tax year uses the calendar year for this test.
6. **Source the gain.** For step 5, gain on personal property (including shares) is generally US-source only if the seller has a **tax home in the United States**. With no US tax home the gain is foreign-source and not taxed ([Pub 519, Personal Property](https://www.irs.gov/publications/p519)). The IRS notes that most students, scholars and foreign-government employees who come intending to stay more than one year have a US tax home from the day they arrive ([IRS, capital gains of nonresident students, scholars and employees of foreign governments](https://www.irs.gov/individuals/international-taxpayers/the-taxation-of-capital-gains-of-nonresident-alien-students-scholars-and-employees-of-foreign-governments)).
7. **Compute the tax.**
   - **ECI and FIRPTA gains:** taxed after allowable deductions at the same graduated rates as citizens and residents ([Pub 519, ch. 4](https://www.irs.gov/publications/p519)). Use the tax computation in the 2026 Form 1040-NR instructions. Nonresident aliens generally cannot claim the standard deduction (Pub 519, ch. 5).
   - **Minimum tax:** a minimum tax may apply to net USRPI gain. Figure it on Form 6251 ([26 U.S.C. 897(a)(2)](https://www.law.cornell.edu/uscode/text/26/897)).
   - **Losses on USRPIs:** an individual's USRPI loss counts only if it would be allowed under section 165(c) ([26 U.S.C. 897(b)](https://www.law.cornell.edu/uscode/text/26/897)). So a loss on a personal-use home is not deductible.
   - **183-day gains:** the net gain is US-source capital gains minus US-source capital losses. Count gains and losses only if, and to the extent that, they would be recognized and taken into account if they were effectively connected with a US trade or business. Do not take into account the capital loss carryover, capital losses in excess of capital gains, the section 1202 exclusion, or losses on personal-use property. Apply 30% or the treaty rate to the net figure ([Pub 519, 183-day rule](https://www.irs.gov/publications/p519)).
   - **Net investment income tax:** this does not apply to a nonresident alien. Only a dual-status taxpayer may owe it, for the resident part of the year ([Form 1040-NR instructions, line 12](https://www.irs.gov/instructions/i1040nr)).
8. **Apply treaty relief, if claimed.** Most treaties exempt gains on personal property. Gains on US real property are generally still taxable ([Pub 519, ch. 9, Capital Gains](https://www.irs.gov/publications/p519)). Read the actual treaty article; do not assume the OECD model. Disclose the treaty position on Form 8833 when required (see the treaty table).
9. **Handle withholding and credits.** For real property, the buyer withholds under FIRPTA (see the withholding section). For securities, give the broker Form W-8BEN. Tax withheld under section 1445 is claimed on Form 1040-NR, line 25f, with the stamped Copy B of Form 8288-A ([Form 1040-NR instructions](https://www.irs.gov/instructions/i1040nr)).
10. **File Form 1040-NR.**
    - Report 183-day gains on Schedule NEC (Form 1040-NR).
    - Report ECI and FIRPTA gains on Schedule D (Form 1040) and/or Form 4797, attached to Form 1040-NR ([Pub 519, Reporting](https://www.irs.gov/publications/p519)).
    - Anyone who is in a US trade or business, or has US-source income on which the tax was not fully paid by withholding, must file ([Pub 519, ch. 7](https://www.irs.gov/publications/p519)). A FIRPTA seller files because USRPI gain is treated as ECI from a US trade or business; the return settles the actual tax and recovers any excess withholding.

## What counts as a USRPI

Source: [Pub 519, Real Property Gain or Loss](https://www.irs.gov/publications/p519) and [26 U.S.C. 897(c)](https://www.law.cornell.edu/uscode/text/26/897).

- **Real property in the US or the US Virgin Islands:** land, buildings and their structural components, and unsevered natural products such as crops, timber, mines and wells. It also includes personal property associated with the use of the real property, such as farming or construction equipment and furnishings of lodging facilities. That personal property is excluded only if it is disposed of more than one year before or after the real property, or sold separately to persons unrelated to the seller or buyer.
- **Any interest (other than as a creditor) in a domestic corporation that is a US real property holding corporation (USRPHC).** A corporation is a USRPHC if the fair market value of its USRPIs is **at least 50%** of the total fair market value of its USRPIs, its real property outside the US, and its other trade or business assets ([Pub 519](https://www.irs.gov/publications/p519)).
  - Stock in a domestic corporation is treated as USRPHC stock unless the seller establishes that the corporation is not a USRPHC.
  - The test looks back over the shorter of the seller's holding period and the 5-year period ending on the date of disposition ([IRS, FIRPTA withholding](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding)).
  - **Cleansing exception:** an interest in a corporation is not a USRPI if, on the date of disposition, the corporation held no USRPIs; all USRPIs it held during the look-back period were disposed of in transactions in which the full gain was recognized; and it was not a RIC or REIT during that period (same IRS page). Refer if you need to rely on it.
- **Not a USRPI:**
  - **Listed shares:** a class of stock regularly traded on an established securities market, unless the seller held **more than 5%** of that class at some time in the testing period. For a REIT the limit is **more than 10%** ([Pub 519, Publicly traded exception](https://www.irs.gov/publications/p519)).
  - **Domestically controlled funds:** an interest in a domestically controlled qualified investment entity (REIT or qualifying RIC) where foreign persons held less than 50% in value throughout the testing period ([Pub 519, Domestically controlled QIE](https://www.irs.gov/publications/p519)).
  - **Qualified shareholders:** REIT stock held by a qualified shareholder under section 897(k).
  - **Foreign corporations:** an interest in a foreign corporation, unless it has elected to be treated as domestic.
- **QIE wash-sale anti-abuse rule:** suppose the client sells an interest in a domestically controlled QIE in the 30 days before the ex-dividend date of a distribution that would have been USRPI gain, and acquires a substantially identical interest within the 61-day period. The distribution amount is then treated as USRPI gain. This does not apply if the client actually received the distribution, or if the stock is regularly traded and the client held no more than 5% of the class at any time in the 1-year period ending on the distribution date ([Pub 519, Wash sale](https://www.irs.gov/publications/p519)).

## FIRPTA withholding on a sale of US real property

The buyer (transferee) is the withholding agent. It must find out whether the seller is a foreign person. A buyer that fails to withhold may be held liable for the tax ([IRS, FIRPTA withholding](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding)).

| Situation | Withholding (on the **amount realized**, not the gain) | Source |
| --- | --- | --- |
| General rule | 15% | [26 U.S.C. 1445(a)](https://www.law.cornell.edu/uscode/text/26/1445) |
| Buyer acquires for use as a residence, amount realized more than $300,000 but not more than $1,000,000 | 10% | [26 U.S.C. 1445(c)(4)](https://www.law.cornell.edu/uscode/text/26/1445); [Pub 515](https://www.irs.gov/publications/p515) |
| Buyer acquires for use as a residence, amount realized not more than $300,000 | No withholding | [26 U.S.C. 1445(b)(5)](https://www.law.cornell.edu/uscode/text/26/1445); [Pub 515](https://www.irs.gov/publications/p515) |
| Residence purchase, amount realized more than $1,000,000 | 15% | [Pub 515, Residences](https://www.irs.gov/publications/p515) |

- **Amount realized** = cash paid or to be paid (principal only) + fair market value of other property transferred + any liability the buyer assumes or takes the property subject to ([Pub 519, Tax withheld on real property sales](https://www.irs.gov/publications/p519)). Where US and foreign persons own the property jointly, the amount realized is allocated by capital contribution. Spouses are treated as contributing 50% each ([IRS, FIRPTA withholding, question 1](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding)). The buyer withholds on the total amount allocated to the foreign seller or sellers. Foreign co-sellers must ask for the credit to be split as they agree by the 10th day after the transfer; otherwise it is divided evenly among them.
- **Joint sellers and the residence limits:** the $300,000 and $1,000,000 residence limits apply to the **total** amount realized on the whole property, not to each seller's allocated share. Allocation only decides how much withholding falls on each foreign seller. A nonresident is not exempt where the total is greater than $300,000, even if every seller's share is $300,000 or less ([IRS, FIRPTA withholding, question 17](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding)).
- **The residence conditions** decide both reduced bands. The **buyer** (not the seller) must be an individual. The buyer or a family member must have definite plans to reside at the property for at least 50% of the days it is used by any person, in each of the first two 12-month periods after the transfer. Vacant days are not counted ([IRS, Exceptions from FIRPTA withholding](https://www.irs.gov/individuals/international-taxpayers/exceptions-from-firpta-withholding)). It need not be the buyer's "primary" residence. The dollar limits are "does not exceed", so exactly $300,000 needs no withholding and exactly $1,000,000 falls in the reduced band ([26 U.S.C. 1445](https://www.law.cornell.edu/uscode/text/26/1445)).
- **Other exceptions from withholding** ([IRS, Exceptions from FIRPTA withholding](https://www.irs.gov/individuals/international-taxpayers/exceptions-from-firpta-withholding)):
  - the seller certifies it is not a foreign person;
  - the interest is in a domestic corporation with a class of stock regularly traded on an established securities market. This does not apply to certain dispositions of substantial amounts of non-publicly traded interests in publicly traded corporations (refer those);
  - a domestic corporation certifies that the interest is not a USRPI;
  - the IRS issues a withholding certificate;
  - the seller gives written notice of a nonrecognition or treaty provision, which the buyer files with the IRS by the 20th day after the transfer;
  - the amount realized is zero;
  - the property is acquired by a US government unit.
- **Withholding is not the tax.** It is a credit against the Form 1040-NR liability. Even where no withholding applies, the seller still reports the gain.

### Reporting and paying over (buyer)

- The buyer files Form 8288, with Copies A and B of Form 8288-A, and pays the tax **by the 20th day after the date of transfer** ([Instructions for Form 8288](https://www.irs.gov/instructions/i8288)).
- The IRS stamps Copy B of Form 8288-A and sends it to the seller. It will not provide a stamped Copy B if the seller's TIN is missing ([IRS, Reporting and paying tax on USRPIs](https://www.irs.gov/individuals/international-taxpayers/reporting-and-paying-tax-on-us-real-property-interests)). In that case the seller must attach substantial evidence of withholding, such as closing documents, and a statement with the Form 8288/8288-A information, including the TIN.
- A seller with no TIN who is eligible for an ITIN can apply by attaching Form 8288-B to Form W-7.

### Withholding certificate (Form 8288-B)

Source: [IRS, Withholding certificates](https://www.irs.gov/individuals/international-taxpayers/withholding-certificates); [Instructions for Form 8288](https://www.irs.gov/instructions/i8288).

- **Who applies:** the buyer, the buyer's agent or the seller can apply to reduce or eliminate withholding.
- **Grounds:**
  - the withholding would exceed the seller's maximum tax liability;
  - the gain is exempt;
  - the transfer qualifies for nonrecognition;
  - a security agreement is made for payment of the tax.
- **Processing time:** the IRS generally acts within 90 days after it receives a complete application that includes the TINs of all parties.
- **If an application is pending at closing,** the buyer must still withhold the full statutory amount. It pays over the withheld amount (or the lesser amount the IRS approves) within 20 days after the IRS mails the certificate or denial.
  - This deferral applies only if the application was submitted on or before the date of transfer.
  - A seller that applies must notify the buyer in writing on the day of the transfer or the day before.
  - If the main purpose of applying was to delay payment, interest and penalties run from the 21st day after the transfer.
- **Timing of the gain:** report it in the year of the actual disposition, even if the stamped Form 8288-A shows a later date because of a certificate request ([IRS, FIRPTA withholding, question 3](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding)).

## Selling US shares through a broker

- **No US tax on the gain in the ordinary case.** A nonresident alien with less than 183 days of presence, no US tax home and no US trade or business owes no US tax on selling listed US shares (Pub 519, 183-day rule and Trading safe harbour, linked above).
- **When the gain is taxed:**
  - the 183-day rule applies (with a US tax home);
  - the gain is ECI;
  - the shares are USRPHC stock, and the seller held more than 5% of the class during the testing period, or the class is not regularly traded ([Pub 519](https://www.irs.gov/publications/p519)).
- **W-8BEN:** give the broker Form W-8BEN to establish foreign status. A broker can rely on it to treat gross proceeds from securities sales as not subject to Form 1099 reporting or backup withholding ([Pub 515, Form W-8BEN](https://www.irs.gov/publications/p515)).
  - **Validity:** the form generally remains in effect from the date signed until the last day of the third succeeding calendar year, unless a change in circumstances makes it incorrect ([Instructions for Form W-8BEN](https://www.irs.gov/instructions/iw8ben)).
  - **When income becomes ECI:** that is a change in circumstances. Use Form W-8ECI instead.
- **Dividends are not capital gains.** Non-ECI US dividends are generally taxed at 30% or a lower treaty rate, withheld at source ([Pub 519, ch. 7](https://www.irs.gov/publications/p519)).

## Treaty relief and Form 8833

| Point | Rule | Source |
| --- | --- | --- |
| Personal property gains | Most treaties exempt them. Read the specific treaty article. | [Pub 519, ch. 9](https://www.irs.gov/publications/p519) |
| US real property gains | Generally still taxable under treaties | [Pub 519, ch. 9](https://www.irs.gov/publications/p519) |
| When Form 8833 is required | Any treaty position that overrides or modifies the Code and reduces, or might reduce, tax. Specifically required when claiming a treaty reduction or modification of tax on USRPI gain or loss. | [Pub 519, Reporting Treaty Benefits Claimed](https://www.irs.gov/publications/p519) |
| Exceptions | Include treaty-reduced withholding on FDAP income, and disclosable items totalling no more than $10,000; see Pub 519 and Regulations section 301.6114-1(c) | [Pub 519](https://www.irs.gov/publications/p519) |
| Penalty for not disclosing | $1,000 for each failure (individuals). It can be waived for reasonable cause and good faith. | [Pub 519](https://www.irs.gov/publications/p519); [26 U.S.C. 6712](https://www.law.cornell.edu/uscode/text/26/6712) |

## Boundary and exception table

| Fact pattern | Result | Source |
| --- | --- | --- |
| Presence exactly 183 days, US tax home, non-ECI gain on shares | Taxed at 30% (or treaty rate): the test is "183 days or more" | [26 U.S.C. 871(a)(2)](https://www.law.cornell.edu/uscode/text/26/871) |
| 183 days or more, but no US tax home | Gain is foreign-source, so not taxed under the 183-day rule | [Pub 519, Personal Property](https://www.irs.gov/publications/p519) |
| F-1 student (exempt individual) present 200 days | Still a nonresident, but exempt-individual days still count for the 183-day capital gains rule | [IRS students and scholars page](https://www.irs.gov/individuals/international-taxpayers/the-taxation-of-capital-gains-of-nonresident-alien-students-scholars-and-employees-of-foreign-governments) |
| Holding 5% exactly of a listed USRPHC class | Not a USRPI (the exception is lost only above 5%) | [26 U.S.C. 897(c)(3)](https://www.law.cornell.edu/uscode/text/26/897) |
| Listed REIT shares, holding more than 5% but not more than 10% | Not a USRPI (REIT limit is more than 10%) | [Pub 519](https://www.irs.gov/publications/p519) |
| Residence buyer, amount realized exactly $300,000 | No withholding | [26 U.S.C. 1445(b)(5)](https://www.law.cornell.edu/uscode/text/26/1445) |
| Residence buyer, amount realized exactly $1,000,000 | 10% withholding | [26 U.S.C. 1445(c)(4)](https://www.law.cornell.edu/uscode/text/26/1445) |
| Foreign spouse and US spouse sell their home to a residence buyer for a total of $500,000; foreign spouse's share is $250,000 | The $300,000 exemption is not available (it tests the total). Withholding is 10% × $250,000 = $25,000, from the foreign spouse's share only | [IRS, FIRPTA withholding, questions 1 and 17](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding) |
| Buyer is a company or an investor who will rent it out | 15%, whatever the price | [26 U.S.C. 1445(a)](https://www.law.cornell.edu/uscode/text/26/1445) |
| Seller sells their own former US home | Section 121 exclusion may apply if the eligibility test is met; maximum excludable gain on Form 1040-NR is $250,000. Withholding can then exceed the tax, so consider a withholding certificate. | [IRS, FIRPTA withholding, question 5](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding) |
| Assignment of a purchase contract for US property | Also a disposition, so FIRPTA withholding applies to the amount realized | [IRS, FIRPTA withholding, question 4](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding) |
| Sale of a partnership interest where the partnership has a US business | Gain can be ECI (section 864(c)(8)). The buyer generally withholds 10% of the amount realized under section 1446(f). Refer. | [Pub 515, Section 1446(f) Withholding](https://www.irs.gov/publications/p515) |

## Worked cases

These amounts are illustrations, not client data.

- **Case 1: listed shares, no US presence.** A resident of another country, with 20 days in the US, no US office and no US tax home, sells shares in a large listed US company through a US broker. She held far less than 5% of the class. The gain is not a USRPI, is not ECI (trading safe harbour) and is not caught by the 183-day rule. There is no US tax, and no Form 1040-NR is needed for the gain. She should keep a current W-8BEN with the broker ([Pub 519](https://www.irs.gov/publications/p519)).
- **Case 2: 183-day rule.** An F-1 student with a US tax home was present for 200 days in 2026 and is still a nonresident (exempt individual). He has US-source capital gains of $12,000 and US-source capital losses of $2,000 (net gain $10,000). Tax at the statutory 30% is $3,000, reported on Schedule NEC, unless his treaty exempts the gain. If it does, he claims the exemption and files Form 8833 unless a Pub 519 exception applies ([26 U.S.C. 871(a)(2)](https://www.law.cornell.edu/uscode/text/26/871); [Pub 519](https://www.irs.gov/publications/p519)).
- **Case 3: FIRPTA, residence band.** A nonresident sells a condo. The buyer pays cash of $520,000 and assumes the seller's mortgage of $230,000, so the amount realized is $750,000. The buyer is an individual who plans to live there for the required days. Withholding is 10% × $750,000 = $75,000. If the buyer were an investor, withholding would be 15% × $750,000 = $112,500. Either way, the seller files Form 1040-NR, reports the gain as ECI, and claims the withholding ([Pub 515, Residences](https://www.irs.gov/publications/p515)).
- **Case 4: at the thresholds.** A residence buyer pays exactly $300,000, so no withholding is required. The seller must still report the gain on Form 1040-NR. A different residence buyer pays exactly $1,000,000: the reduced band applies, so withholding is 10% × $1,000,000 = $100,000 ([26 U.S.C. 1445](https://www.law.cornell.edu/uscode/text/26/1445)).
- **Case 5: non-residence buyer at a low price.** An investor buys for $280,000. The residence exception is not available because the buyer will not live there, so withholding is 15% × $280,000 = $42,000 ([26 U.S.C. 1445](https://www.law.cornell.edu/uscode/text/26/1445)).

## When to refuse or refer

- Residency is unclear: substantial-presence counts near the line, a closer-connection claim, a treaty tie-breaker claim whose outcome is in doubt, or a dual-status year. Refer these to a US international tax preparer.
- The seller is a corporation, partnership, trust or estate, or the property is held through an entity. The distribution and entity-level rules under section 1445(e) and Pub 515 apply.
- Sale of unlisted US corporate stock where USRPHC status has to be tested, or a large holding in a listed class, or REIT or RIC interests beyond the plain exceptions.
- Sale of a partnership or LLC interest (sections 864(c)(8) and 1446(f)).
- Installment sales, like-kind exchanges or other nonrecognition claims, or a withholding certificate based on a security agreement.
- A treaty claim that US real property gain is exempt or reduced.
- Former US citizens or long-term residents (expatriation rules), and any estate or gift tax question.
- Any state tax question. State rules are outside this Guide.

## Filing and payment steps with deadlines

- **Buyer at closing:** withhold, then file Form 8288 with Copies A and B of Form 8288-A and pay by the 20th day after the transfer. If a Form 8288-B application was pending on the transfer date, file within 20 days after the IRS mails its decision ([Instructions for Form 8288](https://www.irs.gov/instructions/i8288)).
- **Seller with no TIN:** apply for an ITIN (Form W-7, attached to Form 8288-B where a certificate is also sought) so that a stamped Form 8288-A can be issued.
- **Form 1040-NR due date for tax year 2026:** the 15th day of the 6th month after year end (June 15, 2027) if the client had no wages subject to US withholding. If the client had such wages, it is the 15th day of the 4th month (April 15, 2027). Form 4868 extends time to file, not time to pay ([Pub 519, ch. 7, When To File](https://www.irs.gov/publications/p519)).
- **Attach:** stamped Form 8288-A Copy B (claim it on line 25f), Schedule NEC and/or Schedule D or Form 4797, and Form 8833 where required.
- **Estimated tax:** a nonresident expecting 2026 tax not covered by withholding uses Form 1040-ES (NR). The first instalment is due on the original due date of the prior year's return (Pub 519, ch. 8).
- **Refund timing:** allow up to 6 months for refunds of tax withheld on Form 8288-A ([Pub 519](https://www.irs.gov/publications/p519)).

### 2025 returns still open (filed in 2026)

For the 2025 calendar year, a Form 1040-NR was due June 15, 2026 if the client had no wages subject to withholding, or April 15, 2026 with such wages. A timely Form 4868 extends these to December 15, 2026 or October 15, 2026 respectively ([Pub 519, When To File](https://www.irs.gov/publications/p519); [Form 1040-NR instructions](https://www.irs.gov/instructions/i1040nr)). The rules in this Guide (the 183-day rule, FIRPTA rates and thresholds, and Form 8833) are the same for 2025 and 2026. The FIRPTA dollar thresholds are fixed in the statute, not indexed.

## State tax note

State income tax is separate from federal tax. A state can treat a gain differently from the federal rules and can have its own withholding or filing requirements when property is sold. This Guide makes no statement about any state's rules. Check with the revenue department of the state where the real property is located, and of any state where the client lived or worked during the year, before closing and before filing.

## Completion checklist

- [ ] Nonresident alien status confirmed for the whole year, and any treaty tie-breaker documented.
- [ ] Each asset classified as USRPI, ECI or other, with the USRPHC look-back and the listed-stock ownership tests applied where relevant.
- [ ] Days of US presence counted (including exempt-individual days) and tax home established for the 183-day rule.
- [ ] Net 183-day gain computed without carryovers, the section 1202 exclusion or personal-use losses.
- [ ] Amount realized computed, including assumed liabilities, and the FIRPTA rate chosen from the buyer's residence facts (individual buyer, residence-use test).
- [ ] Withholding certificate considered where withholding exceeds the likely tax (for example with a section 121 exclusion or a small gain).
- [ ] Form 8288/8288-A filed by the buyer within 20 days, and seller's TIN or ITIN in place.
- [ ] W-8BEN current with each broker.
- [ ] Treaty article read, and Form 8833 attached unless an exception applies.
- [ ] Form 1040-NR filed by the correct due date, with Form 8288-A credit claimed on line 25f.
- [ ] State position checked with the state's own revenue department.

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
