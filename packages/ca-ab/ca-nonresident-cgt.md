---
name: ca-nonresident-cgt
description: "Canada non-resident capital gains: Section 116 clearance certificate, Part XIII withholding, taxable Canadian property (TCP), notional assessment. Trigger on: \"non-resident selling Canadian property\", \"Section 116 Canada\", \"clearance certificate CRA\", \"TCP taxable Canadian property\", \"withholding on sale Canada\", \"non-resident selling Canadian shares\", \"Part XIII withholding Canada\", \"NR4 Canada\"."
version: 1.0
jurisdiction: CA
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada: non-residents selling taxable Canadian property (section 116, T2062, purchaser withholding)

## Scope and who this is for ([ITA s.116](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html))

This Guide covers a **non-resident of Canada** (individual, corporation or trust) who sells, gives away or otherwise disposes of **taxable Canadian property (TCP)**, and the **purchaser** who buys it. Primary year: **2026** (Canada's tax year for individuals is the calendar year). The same rules applied to 2025 dispositions unless a line says otherwise.

It covers:

- what counts as TCP under ITA s.248(1), including the 60-month look-back for shares;
- the section 116 notice and certificate of compliance (Forms T2062, T2062A, T2062B, T2062C; certificates T2064 and T2068);
- the purchaser's liability (25%, or 50% for certain property) and when it does not apply;
- treaty-protected property and the purchaser's notice under s.116(5.02);
- reporting the gain on a Canadian T1 return, the 1/2 inclusion rate and the non-resident surtax;
- the principal residence exemption for someone who is now non-resident.

**Not covered here**, see the **ca-tax-residency** Guide: whether a person is resident or non-resident, departure tax on emigration (Forms T1243, T1161, T1244), Part XIII withholding on dividends, rent, pensions and interest, and the section 216 and 217 elections. In short, dividends and other listed amounts paid to a non-resident bear a 25% Part XIII tax withheld at source ([ITA s.212(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html)), which a treaty may reduce; that is separate from the capital gains rules here.

**Who is taxed.** A person not resident in Canada who "disposed of a taxable Canadian property, at any time in the year or a previous year" pays Canadian income tax on taxable income earned in Canada ([ITA s.2(3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html)). That taxable income includes "taxable capital gains from dispositions" of TCP ([ITA s.115(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-115.html)). A gain on property that is not TCP (for example most listed shares held as a small holding) is not taxed in Canada.

**Section 116 applies because of the vendor's status, not the buyer's.** It applies when the vendor is non-resident or deemed non-resident when the disposition happens, including a vendor who was resident when they agreed to sell but is non-resident at closing. "The purchaser's domicile or country of residence is not relevant" ([IC72-17R6, para 5](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html)).

**Sources used.** The Income Tax Act on Justice Laws (current to 2026-09-03); CRA Information Circular IC72-17R6 (dated 2011, page updated 2025); the CRA page [Disposing of or acquiring certain Canadian property](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/disposing-acquiring-certain-canadian-property.html); CRA Guide T4058 (2025 edition); CRA Guide T4037 (2025); Income Tax Folio S1-F3-C2. Where IC72-17R6 and the newer CRA page differ on procedure (for example online submission), this Guide follows the newer page.

## Ask the client first

- **Residence at the date of disposition.** Was the vendor non-resident (or deemed non-resident by a treaty) on the closing date? If residence is unclear, work it out first with the ca-tax-residency Guide.
- **What exactly is being sold?** Canadian land or buildings, a rental property, a cottage, a former home, unlisted shares, listed shares, a partnership or trust interest, business assets, resource or timber property, a life insurance policy.
- **For shares or interests:** is the company listed on a designated stock exchange? At **any time in the 60 months** before the sale, did more than 50% of the share's value come from Canadian real property, resource property or timber property? For listed shares: did the vendor and non-arm's-length persons own **25% or more** of any class at any time in those 60 months?
- **Dates and amounts:** proposed or actual closing date, proceeds (or fair market value if a gift or non-arm's-length sale), adjusted cost base in Canadian dollars, selling costs.
- **Was the property ever depreciable** (rental building, business equipment)? Was capital cost allowance claimed? That drives Form T2062A and the 50% rate on the building.
- **Treaty country and treaty claim.** Where is the vendor resident for treaty purposes, and does the treaty exempt this gain? Are vendor and purchaser related?
- **Was it ever the vendor's home?** Years owned, years resident in Canada, year of acquisition, other properties the family designated.
- **Tax identification number:** SIN, ITN, TTN, BN or trust account number. Without one, apply for an ITN (Form T1261) separately and early.
- **Any unpaid Canadian tax** for earlier years, and any Underused Housing Tax filings for a residential property.
- **Who holds the purchase money** (usually the purchaser's lawyer or notary) and how much is being held back pending the certificate.

## The method, step by step

1. **Confirm non-residence** at the disposition date. If the vendor is resident, section 116 does not apply (and the ca-tax-residency Guide covers any departure tax).
2. **Classify the property** as TCP or not, using the table in "What counts as taxable Canadian property" below. If it is not TCP, there is no section 116 notice, no purchaser liability and no Canadian tax on the gain.
3. **Check whether it is excluded property** under s.116(6) (for example shares listed on a recognized stock exchange, units of a mutual fund trust, bonds and mortgages, or treaty-exempt property). Excluded property needs no section 116 notice and carries no purchaser liability, but a gain can still be taxable in Canada and reportable on a return (IC72-17R6, para 3).
4. **Check treaty protection.** If the treaty fully exempts the gain, the property is treaty-protected. If vendor and purchaser are related, it only becomes treaty-exempt (and excluded) if the purchaser files a notice within 30 days. See "Treaty-protected property".
5. **Pick the form.** T2062 for capital property (land, shares, non-depreciable property, and the gain on depreciable property); T2062A for depreciable TCP (recapture or terminal loss), inventory real property, resource and timber property; T2062B for a life insurance policy (the insurer files it). A rental building usually needs both T2062 and T2062A.
6. **Notify the CRA.** Either before closing (a proposed disposition, ideally at least 30 days ahead), or no later than **10 days after** the actual disposition. Send the form with supporting documents and the payment on account or acceptable security.
7. **Compute the payment on account.** For T2062 property: **25% of (proceeds minus adjusted cost base)**. Selling costs are ignored in this calculation. For T2062A property: an amount the CRA accepts, using individual, trust or corporate rates on the fully taxable amount.
8. **Get the certificate.** The CRA issues **T2064** (proposed disposition) or **T2068** (actual disposition) to vendor and purchaser once the information is complete and payment or security is received. If the actual deal differs from the proposal (different buyer, higher price, lower ACB), file again.
9. **Purchaser side.** Until a certificate covering the full price arrives, the purchaser (in practice their lawyer) holds back 25% of the price (50% for T2062A-type property) minus any certificate limit. If no certificate is received, the purchaser remits it within 30 days after the end of the month of acquisition.
10. **File the Canadian return** for the year of disposition (a T1 for an individual, by April 30 of the following year) unless the no-return exception applies. Attach Copy 2 of the certificate. The payment on account is only an interim payment: the final tax is set on assessment, and any excess is refunded.

## Key figures and time limits (tax year 2026)

| Item | Figure or limit | Source |
|---|---|---|
| Share look-back period for TCP | any time in the **60-month** period ending at the disposition | ITA s.248(1) TCP (d), (e) |
| Value test for shares and interests | **more than 50%** of FMV from Canadian real, resource or timber property | ITA s.248(1) TCP (d) |
| Ownership test for listed shares | **25% or more** of any class (with non-arm's-length persons and partnerships) | ITA s.248(1) TCP (e) |
| Vendor notice of actual disposition | not later than **10 days** after the disposition | ITA s.116(3) |
| Recommended lead time for a proposed-disposition notice | at least **30 days** before closing | IC72-17R6 para 6 |
| Vendor payment on account (T2062 property) | **25%** of proceeds minus ACB | ITA s.116(2), (4); IC72-17R6 para 41 |
| Purchaser liability, general TCP | **25%** of cost to purchaser minus certificate limit | [ITA s.116(5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html) |
| Purchaser liability, s.116(5.2) property | **50%** of amount payable minus certificate amount | ITA s.116(5.3) |
| Purchaser remittance deadline | within **30 days** after the end of the month of acquisition | ITA s.116(5), (5.3) |
| Purchaser treaty notice (s.116(5.02)) | on or before **30 days** after acquisition | ITA s.116(5.02) |
| Late vendor notice penalty | **$25** a day, minimum **$100**, maximum **$2,500** | ITA s.162(7); CRA penalty page |
| Late purchaser remittance penalty | **3%** (1-3 days), **5%** (4-5 days), **7%** (6-7 days), **10%** (more than 7 days); **20%** for second and later failures in the same year made knowingly or with gross negligence | ITA s.227(9); IC72-17R6 para 56 |
| Inclusion rate for capital gains | **1/2** of the capital gain | ITA s.38(a) |
| Non-resident surtax (instead of provincial tax) | **48%** of federal tax on income not earned in a province | ITA s.120(1) |
| Individual return due | **April 30** of the year after the disposition (2026 disposition: April 30, 2027) | CRA disposing page |
| Corporation return due | **six months** after the end of the tax year | CRA disposing page |
| Trust return due | **90 days** after the end of the trust's tax year | CRA disposing page |

**The inclusion rate is 1/2.** ITA s.38(a) (current to 2026-09-03) says a taxable capital gain "is ½ of the taxpayer's capital gain". In 2024 the government proposed raising it to two-thirds; the CRA administered that for a period, then on January 31, 2025 it "reverted to administering the currently enacted capital gains inclusion rate of one-half" when the start date was deferred to January 1, 2026 ([CRA, 31 January 2025](https://www.canada.ca/en/revenue-agency/news/newsroom/tax-tips/tax-tips-2025/update-cra-administration-proposed-capital-gains-taxation-changes.html)). The CRA's later note says: "It was later announced that this proposed increase was cancelled" ([CRA: What's new for corporations](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/whats-new-corporations.html)). So for 2025 and 2026 dispositions, use 1/2. The section 116 payment on account (25% of the whole gain) is a separate, flat interim figure and does not depend on the inclusion rate.

**No capital gains deduction.** The lifetime capital gains exemption requires residence in Canada throughout the year (or residence for part of the year plus throughout the year before or after) ([T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)). A non-resident for the whole year cannot claim it.

## What counts as taxable Canadian property ([ITA s.248(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html))

TCP of a taxpayer at any time is property that is:

| Property | TCP? | Condition |
|---|---|---|
| (a) Real or immovable property situated in Canada | **Always** | Land, buildings, condos, cottages, a former home |
| (b) Property used or held in, or inventory of, a business carried on in Canada | Yes | Excludes property of an insurance business, and (for a non-resident) certain international ships and aircraft on a reciprocal basis |
| (c) Designated insurance property of an insurer | Yes | Insurers only |
| (d) Share of a corporation **not listed** on a designated stock exchange (other than a mutual fund corporation), a partnership interest, or a trust interest (other than a mutual fund trust unit or an income interest in a Canadian-resident trust) | Yes, **if** at any time in the **60 months** ending at that time, **more than 50%** of its FMV came directly or indirectly from Canadian real or immovable property, Canadian resource property, timber resource property, or options or interests in them | Value held through an entity whose shares or interests were not themselves TCP at the time does not count |
| (e) Share **listed** on a designated stock exchange, mutual fund corporation share, or mutual fund trust unit | Yes, **only if both** tests are met at the same particular time in the 60 months: (i) the taxpayer, non-arm's-length persons and their partnerships owned **25% or more** of the issued shares of any class (or units), **and** (ii) **more than 50%** of FMV came from the property in (d) | Otherwise not TCP |
| (f) An option in respect of, or an interest in, any property in (a) to (e) | Yes | Whether or not the property exists |
| (g) to (k) Canadian resource property, timber resource property, an income interest in a trust resident in Canada, a right to a share of income or loss under a s.96(1.1)(a) agreement, a life insurance policy in Canada | Yes, for the tax charge in s.2, s.150 filing, s.128.1 and certain rollover rules | This is why a gain on them is taxed and needs a return; the resource, timber and life insurance items use the s.116(5.2) certificate route |

Points that are easy to get wrong:

- **"Private" is not the test.** The test in (d) is "not listed on a designated stock exchange", and the value test counts resource and timber property as well as real property.
- **The 60-month look-back** means a share can be TCP even though the company holds no Canadian real property today, if more than 50% of its value came from such property at any particular time in the previous 60 months. For shares the CRA suggests getting "a declaration from the corporation certifying that the value of the shares is not principally derived, and has not been for the previous 60 months" from such property ([CRA disposing page](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/disposing-acquiring-certain-canadian-property.html)).
- **Operating-company shares** whose value comes from the business, not land, are generally not TCP; the CRA says the seller need not notify and the buyer need not withhold where the shares do not derive their value, now or in the previous 60 months, principally from Canadian real, resource or timber property.
- **Deemed TCP.** Other provisions can deem property to be TCP (for example on some rollovers). Property that is TCP **solely** because of a deeming rule is excluded property for section 116 (s.116(6)(a)), but the gain can still be taxable.
- **Emigrants.** Canadian real property is not deemed disposed of on departure, so it stays TCP and a later sale falls under section 116, unless the emigrant elected under s.128.1(4)(b)(v) (Form T2061A) to include it in the deemed disposition (see ca-tax-residency).

**Excluded property** ([s.116(6)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html)): no notice, no certificate and no purchaser liability, but the gain may still be taxable. It includes: property that is TCP solely because of a deeming provision; business inventory other than real property, resource or timber property; a share listed on a **recognized** stock exchange (or SIFT wind-up entity equity); a mutual fund trust unit; a bond, debenture, bill, note, mortgage, hypothecary claim or similar obligation; property of a licensed non-resident insurer carrying on insurance business in Canada; property of an authorized foreign bank carrying on Canadian banking business; options on and interests in those; and **treaty-exempt property**.

## Section 116: notice, payment and certificate ([IC72-17R6](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html))

**Two routes to a certificate.**

- **Proposed disposition (s.116(1), (2)).** The vendor "may, at any time before the disposition" send a notice with the proposed purchaser's name and address, a description of the property, the estimated proceeds and the ACB. On payment of **25%** of (estimated proceeds minus ACB), or acceptable security, the CRA issues **Form T2064** fixing a "certificate limit" equal to the estimated proceeds. The CRA asks for the notice "at least 30 days before" closing. If the buyer changes, the proceeds turn out higher, or the ACB falls before closing, the vendor must also file a notice of the actual disposition within 10 days. If proceeds turn out lower or ACB higher, no second notice is needed (IC72-17R6 para 6).
- **Actual disposition (s.116(3), (4)).** Otherwise the vendor "shall, not later than 10 days after the disposition" notify the CRA. The statute says by registered mail; the CRA also accepts the form online through My Account, Represent a Client or My Business Account, or by fax. On payment of **25%** of (proceeds minus ACB), or security, the CRA issues **Form T2068**.

**When is the disposition?** Usually the closing date, when the executed deed is delivered to the purchaser (IC72-17R6 para 19). The 10 days run from then.

**Which form.**

- **T2062**: capital property that is TCP, including the capital gain on depreciable TCP.
- **T2062A**: s.116(5.2) property, that is depreciable TCP (for the recapture or terminal loss), real property in Canada held as inventory, Canadian resource and timber resource property, and interests or options in them; with Schedule 1 for resource property. File it "even if capital cost allowance has not been claimed" (IC72-17R6 para 15). A rental building usually needs **both** T2062 (gain) and T2062A (recapture), and two certificates are issued. The statutory 10-day notice in s.116(3) does not cover s.116(5.2) property, and the CRA does not apply the 10-day penalty timeframe to it, but without a s.116(5.2) certificate the purchaser is liable at 50%, so in practice the certificate is still obtained before or at closing.
- **T2062B**: a life insurance policy in Canada; the insurer files it and remits.
- **T2062C**: the **purchaser's** notice of acquiring treaty-protected property. No certificate is issued for it (IC72-17R6 para 49).

**Payment on account.** For T2062 property the CRA requires "a flat rate of 25% of the excess of the proceeds of disposition over the adjusted cost base"; selling costs are not taken into account and are claimed on the return instead (IC72-17R6 para 41). For T2062A property the amount is worked out at individual, trust or corporate federal rates because it is fully included in income (para 42). For a depreciable building: 25% of the gain on land and building, plus the applicable federal rate on the recapture (para 43). Security must be acceptable to the CRA; "A letter of undertaking is not considered acceptable security" in a treaty dispute (para 31). Payments go by wire or cheque marked "Section 116" with the account or case number.

**Supporting documents** include the purchase and sale agreement, proof of ACB, and an appraisal or valuation where needed. If the CRA thinks the reported ACB is wrong it treats the information as not provided and withholds the certificate (para 21). Foreign currency: ACB at the historical rate, proceeds at the rate on the disposition date (para 22).

**Gifts and non-arm's-length sales.** If proceeds are below FMV to a non-arm's-length person, or the property is gifted, FMV replaces proceeds and cost throughout section 116 (s.116(5.1)).

**Several vendors.** Each co-owner files a separate notice for their share. For a partnership, the CRA accepts one notice for all partners with a full listing (para 10).

**Underused Housing Tax link.** Under s.116(8) the CRA may refuse a certificate for residential property if the vendor has not filed Underused Housing Tax returns or paid that tax. The CRA says "Affected owners do not need to file a return or pay the underused housing tax (UHT) for 2025 and subsequent calendar years", but "the requirement to file a UHT return and pay the tax still applies to the 2022, 2023, and 2024 calendar years" ([CRA UHTN1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/uhtn1/introduction-underused-housing-tax.html)). So s.116(8) now matters only where 2022 to 2024 UHT returns or tax are outstanding.

## Purchaser's liability ([ITA s.116(5), (5.3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html))

**General TCP (s.116(5)).** A purchaser who acquires TCP (other than depreciable property or excluded property) from a non-resident is liable to pay, on the vendor's behalf, **25%** of the amount by which the purchaser's cost exceeds any certificate limit fixed under s.116(2). This does **not** apply if:

- after reasonable inquiry the purchaser "had no reason to believe" the vendor was non-resident;
- s.116(5.01) applies (treaty-protected property with the purchaser's notice, see below); or
- a s.116(4) certificate (T2068) has been issued to the purchaser for the property.

**Section 116(5.2) property (s.116(5.3)).** For depreciable TCP, inventory real property, resource or timber property and life insurance policies, the rate is **50%** of the amount payable minus the amount fixed in any s.116(5.2) certificate, with the same reasonable-inquiry and (5.01) exceptions.

**What it means in practice.** The liability is measured on the **price**, not the gain. The purchaser may deduct or withhold the amount from the price, and must remit it "within 30 days after the end of the month in which the purchaser acquired the property". Purchasers' lawyers therefore hold back 25% (or 50% on the building portion of a rental) until a certificate covering the full price is delivered. "Purchaser liability assessments are not subject to any time restrictions" (IC72-17R6 para 50). Remittances count as payments on the vendor's account.

**Reasonable inquiry** means prudent steps to confirm the vendor's residence; the CRA "will not make inquiries on behalf of a purchaser" (para 58). Late remittance attracts the 3% to 10% penalty (20% for second and later knowing or grossly negligent failures in the same year) plus interest.

**Mortgagees.** A mortgagee who takes a property by foreclosure is generally not a purchaser liable under section 116, unless foreclosure is used as a device to sell. Under a power of sale, title passes from the non-resident mortgagor to the buyer, so section 116 applies to that buyer (paras 53-54).

## Treaty-protected property ([ITA s.116(5.01), (5.02), (6.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html))

**Definitions.** "Treaty-protected property" is property any gain on which would, "because of a tax treaty with another country, be exempt from tax under Part I" (s.248(1)). It is **treaty-exempt property** (and so excluded property) at the time of disposition if it is treaty-protected **and**, where purchaser and vendor are related, the purchaser gives the s.116(5.02) notice (s.116(6.1)).

**Which property is typically protected.** The CRA explains that most treaties let Canada tax gains "only on Canadian real and resources properties and on shares of companies that derive most of their value from such properties" ([CRA disposing page](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/disposing-acquiring-certain-canadian-property.html)). Canadian real property itself is almost never treaty-protected; for example the Canada-US Convention says gains "from the alienation of real property situated in the other Contracting State may be taxed in that other State" ([Article XIII(1)](https://laws-lois.justice.gc.ca/eng/acts/C-10.7/FullText.html)). Share and business-property cases turn on the wording of the specific treaty article (including its own look-back and value tests) and any protocol, so read the treaty.

**Purchaser's notice (s.116(5.02)).** The purchaser sends the CRA, "on or before the day that is 30 days after the date of the acquisition", a notice giving: the acquisition date; the vendor's name and address; a description of the property; the amount paid or payable; and the treaty country. Form T2062C is the CRA's form for it.

- **Related purchaser:** the notice is **required** for the property to be treaty-exempt. If it is missing or late, "the notification will be invalid and the vendor will be required to notify the CRA of the disposition", and the normal purchaser liability applies.
- **Unrelated purchaser:** neither party has to notify. The purchaser is protected from liability under s.116(5.01) only if, after reasonable inquiry, they conclude the vendor is treaty-resident, the property would be treaty-protected, **and** they send the notice. The CRA "will generally not issue such an assessment" against an unrelated purchaser who filed T2062C and made every reasonable effort. A late T2062C is invalid. The CRA generally does not acknowledge receipt.

**Vendor claiming a treaty exemption on T2062.** The vendor names the treaty provision and supplies proof, for example NR301 (individuals), NR302 (partnerships) or NR303 (hybrid entities) and a certificate of residence (for US residents, IRS Form 6166). If the CRA disagrees, the vendor must pay or secure the tax before the certificate issues (IC72-17R6 paras 29-31).

**On the return.** "Do not report any gain or claim a loss from the disposition of taxable Canadian property if, under a tax treaty, any gain from the disposition of the property would be exempt from tax in Canada"; if a return is required, attach a note saying so ([T4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html)).

## Reporting the gain on the Canadian return ([CRA Guide T4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html))

**Who must file.** A non-resident must file a Canadian return for the year if they "realized a taxable capital gain or disposed of taxable Canadian property" in the year (T4058). The section 116 payment is not the final tax: "All payments ... that you or the buyer makes to the CRA as a result of a disposition are considered interim payments. You make a final settlement of tax for the disposition when you file your return."

**No-return exception ([ITA s.150(5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html)).** A disposition is an "excluded disposition", and no return is needed for it, only if **all** of these hold: the taxpayer is non-resident at that time; **no tax is payable** under Part I for the year; the taxpayer owes nothing for any previous year (other than amounts for which the CRA holds adequate section 116 or 220 security); **and** each TCP disposed of in the year is either excluded property or property for which the CRA issued a certificate under s.116(2), (4) or (5.2). In practice a taxable gain means tax is payable, so a return is needed; the exception mainly helps treaty-exempt and loss cases.

**How an individual reports.**

- Use the income tax package for non-residents and deemed residents. Complete **Schedule 3** and report the taxable capital gain on **line 12700**.
- Gains on T2062A-type property (inventory real property, resource or timber property, life insurance) are income, not capital gains: report them on line 13000 or 13500 and attach a note, not on Schedule 3.
- Recapture of capital cost allowance on a rental building is fully included in income.
- Selling costs reduce the gain on the return even though they were ignored for the payment on account.
- Attach **Copy 2** of the certificate of compliance (T2064 or T2068).
- Claim the section 116 payment (and any purchaser remittance) as tax paid.

**Tax rate.** Only 1/2 of the gain is taxable (s.38(a)). If the non-resident has no income earned in a province (for example only TCP gains), "Other" is entered as the jurisdiction and they pay federal tax "plus the surtax for non-residents and deemed residents of Canada" (T4058), which is **48%** of the federal tax on that income (s.120(1)), instead of provincial tax. Federal brackets and credits for 2026 are in the 2026 return package; this Guide does not reproduce them. Where the person also has employment income or a business with a permanent establishment in a province, Form T2203 splits the tax.

**Excess payment.** After assessment, "any excess payment is refunded or provision is made for the release of security" (IC72-17R6 para 60). A return filed before the end of the tax year is processed only after the year ends.

## Principal residence of a non-resident ([Folio S1-F3-C2](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-1-individuals/folio-3-family-unit-issues/income-tax-folio-s1-f3-c2-principal-residence.html))

A home in Canada is real property, so it is **always TCP** and a sale by a non-resident falls under section 116 even if part of the gain is exempt.

**The exemption formula** (ITA s.40(2)(b); Folio para 2.20). Exempt gain = **A x (B / C)**:

- **A** is the gain otherwise determined.
- **B**, if the owner "was resident in Canada during the year that includes the acquisition date", is **1 +** the number of tax years ending after the acquisition date for which the property was their principal residence **and during which they were resident in Canada**. If they were not resident in Canada in the acquisition year, B has **no "1 +"**. That limit applies to dispositions after October 3, 2016.
- **C** is the number of tax years ending after the acquisition date during which they owned the property.

**What this means for a non-resident seller.** Years of ownership after the owner left Canada count in C but can never count in B, so the exempt share shrinks for each year owned while non-resident. "During" means at any time in the year, so the departure year can still count if the home was designated for it. A person who bought while non-resident gets no "plus 1" year (T4037). One property per family unit can be designated for each year.

**Reporting.** The designation is made on Schedule 3 and **Form T2091(IND)** with the return for the year of sale (Folio para 2.15). The section 116 notice is still required, and the CRA says "The tax or security required may be reduced accordingly where the gain is reduced by the principal residence exemption". To ask for that, send Form T2091(IND), or a letter signed by the taxpayer, with the section 116 notice as well as with the return. On the T2091, "ensure that lines 1 to 3 do not include any tax years during which the taxpayer was not resident in Canada" (IC72-17R6 para 73).

**Departure note.** Leaving Canada does not trigger a deemed disposition of Canadian real property, so the whole gain (including growth after departure) is dealt with on the later sale, reduced by the formula above, unless the emigrant elected under s.128.1(4)(b)(v) (Form T2061A) to include it in the deemed disposition. See ca-tax-residency for the departure rules.

## Boundaries and exceptions

| Situation | Treatment | Source |
|---|---|---|
| Vendor resident at closing | Section 116 does not apply | s.116(1), (3); IC72-17R6 para 5 |
| Vendor resident at signing, non-resident at closing | Section 116 applies | IC72-17R6 para 5 |
| Purchaser is Canadian or foreign | Irrelevant to whether section 116 applies | IC72-17R6 para 5 |
| Listed shares, holding under 25% of every class throughout 60 months | Not TCP: no Canadian tax, no notice | s.248(1) TCP (e) |
| Listed shares that are TCP (25%+ and real-property rich) | Excluded property if listed on a recognized exchange: no notice or purchaser liability, but gain taxable unless treaty-exempt | s.116(6)(b); IC72-17R6 para 3 |
| Unlisted shares, more than 50% real-property value at any time in last 60 months | TCP; notice and purchaser liability apply | s.248(1) TCP (d) |
| Unlisted operating company, never real-property rich in 60 months | Not TCP; no notice, no withholding | CRA disposing page |
| Rental building (depreciable) | T2062 and T2062A; 50% purchaser rate on the building, 25% on the land | [s.116(5.2), (5.3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html); IC72-17R6 para 15 |
| Land held as inventory (developer) | T2062A; 50% rate; CRA may grant a "qualified business exemption" | IC72-17R6 para 36 |
| Treaty-protected property, unrelated purchaser | Excluded property; optional T2062C within 30 days protects purchaser | s.116(5.01), (6.1); CRA page |
| Treaty-protected property, related purchaser | Treaty-exempt only if purchaser files within 30 days; otherwise normal rules | s.116(6.1); IC72-17R6 paras 27-28 |
| Proposed disposition later changes (new buyer, higher price, lower ACB) | New notice within 10 days of actual disposition | IC72-17R6 para 6 |
| Share-for-share exchange deemed not a disposition by s.51(1)(c) | No vendor notice; the corporation may be a purchaser and can ask for a certificate | IC72-17R6 para 40 |
| Foreclosure by mortgagee | Generally no purchaser liability | IC72-17R6 para 53 |
| Proposed dispositions and s.116(5.2) dispositions | Not subject to the 10-day penalty timeframe | CRA penalty page |
| Late notice caused by circumstances beyond control | Ask for penalty relief under s.220(3.1), to the office that issued the certificate | CRA penalty page |

## Worked cases ([ITA s.116](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html); [IC72-17R6](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html))

**Case 1: cottage sold by a US resident, certificate obtained.** A US-resident individual sells an Ontario cottage (never rented, never her home) on 15 June 2026. Proceeds $800,000, ACB $500,000, selling costs $40,000.

- Property: Canadian real property, so TCP; not excluded; not treaty-protected (Article XIII(1)).
- Form T2062. Payment on account: 25% x ($800,000 - $500,000) = **$75,000**. Selling costs are ignored here.
- The CRA issues T2068 once paid (or T2064 if she filed before closing).
- 2026 return (due April 30, 2027): gain $800,000 - $500,000 - $40,000 = $260,000; taxable capital gain 1/2 x $260,000 = **$130,000** on line 12700. Tax is federal tax plus the 48% surtax; the $75,000 is credited and any excess refunded.

**Case 2: same sale, no certificate at closing.** The purchaser's lawyer holds back 25% x $800,000 = **$200,000**. If no T2068 arrives, the purchaser remits it within 30 days after the end of June 2026, that is by **July 30, 2026**. If the purchaser does not withhold and remit, the purchaser owes the $200,000 itself, with no time limit on the assessment. A certificate "protects the purchaser from any further tax liability" for that disposition (IC72-17R6 para 46), which is why holdbacks are usually released once it arrives.

**Case 3: rental property, split land and building.** A non-resident sells a Canadian rental property for $1,000,000: land $600,000, building $400,000. No certificates are obtained.

- Land (capital property, TCP): purchaser liability 25% x $600,000 = **$150,000** (s.116(5)).
- Building (depreciable TCP, a s.116(5.2) property): 50% x $400,000 = **$200,000** (s.116(5.3)).
- Total purchaser exposure: $150,000 + $200,000 = **$350,000**.
- The vendor should file T2062 (gain on land and building) and T2062A (recapture on the building), get two certificates, and report the recapture as fully taxable income on the return.

**Case 4: late notice.** Closing 1 March 2026, so the notice is due by 11 March 2026. The vendor notifies on 10 April 2026: 30 days late, 30 x $25 = **$750** (between the $100 minimum and $2,500 maximum). Three days late: 3 x $25 = $75, raised to the **$100** minimum. 120 days late: 120 x $25 = $3,000, capped at **$2,500**.

**Case 5: former home sold after emigrating.** Bought in 2015 for $420,000 while resident; lived in it and designated it for 2015 to 2020; emigrated in 2020 and kept it; sold in 2026 for $900,000 while non-resident.

- Gain A = $900,000 - $420,000 = $480,000.
- Resident in the acquisition year, so B = 1 + 6 (2015 to 2020) = **7**. C = tax years ending after acquisition while owned, 2015 to 2026 = **12**.
- Exempt: $480,000 x 7 / 12 = **$280,000**. Remaining gain $480,000 - $280,000 = $200,000; taxable 1/2 x $200,000 = **$100,000**.
- Section 116 notice still required. The payment on account may be reduced for the exempt part (IC72-17R6 para 73): send T2091(IND), with lines 1 to 3 leaving out the years of non-residence, or a signed letter, with the T2062. Payment on account: 25% x ($480,000 - $280,000) = **$50,000**. Designate again on Schedule 3 and T2091(IND) with the 2026 return.

**Case 6: the 60-month look-back.** A non-resident sells unlisted shares of a Canadian company on 1 October 2026. The company sold its Canadian land, which had been more than 50% of its value, in March 2023.

- March 2023 is within the 60 months ending 1 October 2026, so the shares are **TCP**: notice, certificate and purchaser liability apply (unless treaty-protected).
- If the land had been sold in June 2021 and the company was never real-property rich afterwards, that is outside the 60 months, so the shares are **not TCP**.

**Case 7: listed shares.** A non-resident holds 2% of a TSX-listed company: not TCP (the 25% test fails), so no Canadian tax and no notice. If instead the holding with non-arm's-length persons was 30% of a class and more than 50% of the value came from Canadian real estate, the shares are TCP; but a share listed on a recognized stock exchange is excluded property, so there is no section 116 notice or purchaser liability. The gain is still taxable in Canada unless a treaty exempts it, and a return is needed if tax is payable.

## When to refuse or refer

Refer to a Canadian cross-border tax adviser, or decline, when:

- residence or treaty residence at the closing date is unclear or disputed;
- the vendor is a corporation, trust, estate (including the death of a non-resident owner) or partnership;
- the vendor claims a treaty exemption on shares or business property and the treaty article, protocol or anti-abuse rules need analysis;
- the transaction involves a section 85 rollover, a corporate reorganization, resource or timber property, inventory land, or a life insurance policy;
- the property is in Quebec: this Guide covers only the federal rules, so check Revenu Québec's own requirements for dispositions by non-residents;
- the CRA disputes the ACB, the valuation or the treaty claim, or a purchaser liability assessment has been raised;
- Underused Housing Tax returns or tax for 2022 to 2024 may be outstanding;
- the client wants to close without a certificate or without a holdback.

This Guide explains the federal rules; it does not replace a review of the documents by a Canadian professional.

## Filing and payment ([CRA: Disposing of or acquiring certain Canadian property](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/disposing-acquiring-certain-canadian-property.html))

**Vendor.**

- **Identification number first.** A former resident uses their SIN. Anyone without a SIN, TTN or ITN applies for an ITN on Form T1261, sent "separately and in advance of your disposition request". A certificate cannot be issued without an identification number (IC72-17R6 para 9).
- **Notice:** T2062 / T2062A with supporting documents, before closing or within 10 days after. Submit online (My Account, Represent a Client or My Business Account, "Submit documents") or by mail or fax to the Section 116 Centre of Expertise for the region where the property is. For real property that is the property's address; for shares, the corporation's head office.
- **Payment:** wire or cheque, marked "Section 116" with the account or case number.
- **Return:** individuals by **April 30** of the following year (2026 dispositions: April 30, 2027), corporations within six months after the tax year-end, trusts within 90 days after the tax year-end. Attach Copy 2 of the certificate. Late returns attract interest and penalties.

**Purchaser.**

- Confirm the vendor's residence by reasonable inquiry, and hold back 25% (50% for s.116(5.2) property) of the price, minus any certificate limit, until a certificate covering the price arrives.
- Without a certificate, remit to the Receiver General within 30 days after the end of the month of acquisition, identifying it as a subsection 116(5) or 116(5.3) payment with the vendor's and purchaser's names and addresses (IC72-17R6 para 55).
- Treaty-protected property: send T2062C (or an equivalent notice) within 30 days of acquisition. Required if related to the vendor; optional but protective if unrelated.

**Returns being filed now for 2025.** For a 2025 disposition, the individual return was due April 30, 2026. The rules above (1/2 inclusion rate, 25% and 50% rates, 10-day notice) were the same in 2025. If the 2025 return has not been filed, file it now with Copy 2 of the certificate; interest and penalties run from the due date.

## Completion checklist

- [ ] Vendor's residence (and treaty residence) at the closing date confirmed and documented.
- [ ] Property classified as TCP or not, with the 60-month look-back checked for shares and interests (and a corporate declaration obtained where relied on).
- [ ] Excluded-property and treaty-protected status checked; related or unrelated purchaser identified.
- [ ] Correct form(s) chosen: T2062, T2062A (depreciable, inventory land, resource, timber), T2062B, T2062C.
- [ ] Identification number in place (SIN, ITN, TTN, BN or trust number).
- [ ] Notice sent before closing, or within 10 days after; late-notice penalty assessed if not.
- [ ] Payment on account computed (25% of proceeds minus ACB for T2062 property) or security agreed.
- [ ] Certificate T2064 or T2068 received; a new notice filed if the actual deal differed from the proposal.
- [ ] Purchaser's holdback set at 25% or 50% of price minus any certificate limit; remittance date diarised if no certificate.
- [ ] Principal residence formula applied with only years of Canadian residence in B; T2091(IND) (or signed letter) sent with the section 116 notice to reduce the payment, and T2091(IND) filed with the return.
- [ ] Return for the year of disposition filed on time (or s.150(5) exception documented), with Schedule 3, line 12700 at the 1/2 inclusion rate, any recapture, Copy 2 of the certificate, and the section 116 and purchaser payments claimed.
- [ ] Cross-checked with the ca-tax-residency Guide for departure tax and Part XIII items.

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
