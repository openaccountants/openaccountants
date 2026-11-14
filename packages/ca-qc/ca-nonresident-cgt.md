---
name: ca-nonresident-cgt
description: "Canada 2026 non-resident property sales: classify taxable Canadian property and treaty exceptions; prepare T2062, T2062A, T2062B or purchaser T2062C; calculate certificate payments and purchaser withholding separately from final Canadian tax; former-home principal residence relief. Trigger on non-resident selling Canadian property or shares, section 116 certificate, purchaser holdback, CRA certificate limit, non-resident rental property sale, T2062 or T2062A."
version: 1.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: filing-howto
depends_on:
  - income-tax-workflow-base
---

# Canada: non-residents selling taxable Canadian property (section 116, T2062, purchaser withholding)

## Scope

[Authority: ITA section 116](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html).

This skill covers a **non-resident of Canada** (individual, corporation or trust) who sells, gives away or otherwise disposes of **taxable Canadian property (TCP)**, and the **purchaser** who buys it. Primary year: **2026** (Canada's tax year for individuals is the calendar year). The enacted section 116 rates discussed here also apply to the ordinary 2025 examples. Use the forms and return package for the actual year. A 2027 proposal is identified separately below and must not be applied to a 2026 closing.

It covers:

- what counts as TCP under ITA s.248(1), including the 60-month look-back and combined ownership tests for shares;
- the section 116 notice and certificate of compliance (Forms T2062, T2062A, T2062B, T2062C; certificates T2064 and T2068);
- the purchaser's liability (25%, or 50% for certain property) and when it does not apply;
- treaty-protected property and the purchaser's notice under s.116(5.02);
- reporting the gain on a Canadian T1 return, the 1/2 inclusion rate and the non-resident surtax;
- the principal residence exemption for someone who is now non-resident.

**Not covered here**, see the **ca-tax-residency** skill: whether a person is resident or non-resident, departure tax on emigration (Forms T1243, T1161, T1244), Part XIII withholding on dividends, rent, pensions and interest, and the section 216 and 217 elections. Dividends and other amounts within the charging provisions can bear a 25% Part XIII tax withheld at source ([ITA s.212(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html)), which a treaty may reduce; that is separate from the capital gains rules here.

**Who is taxed.** A person not resident in Canada who "disposed of a taxable Canadian property, at any time in the year or a previous year" pays Canadian income tax on taxable income earned in Canada ([ITA s.2(3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html)). That taxable income includes "taxable capital gains from dispositions" of TCP ([ITA s.115(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-115.html)). For a person non-resident throughout the year, an ordinary capital gain on property outside TCP is outside this Canadian section 115 charge. Establish capital-versus-business treatment and all actual or deemed TCP rules first; this is not an exemption for Canadian business income. Part-year residence follows the separate residence workflow.

**Section 116 applies because of the vendor's status, not the buyer's.** It applies when the vendor is non-resident or deemed non-resident when the disposition happens, including a vendor who was resident when they agreed to sell but is non-resident at closing. "The purchaser's domicile or country of residence is not relevant" ([IC72-17R6, para 5](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html)).

**Sources read on 14 November 2026.** Current consolidated Income Tax Act sections 2, 13, 38, 40, 54, 110.6, 115, 116, 120, 128.1, 150, 162, 212, 220 and 227, and the relevant definitions in section 248; the current CRA disposition page; IC72-17R6; the relevant parts of CRA 2025 T4058 and T4037 and principal residence Folio S1-F3-C2; actual T2062 E(21), T2062A E(21), T2062B E(16), T2062C(18), T1261 E(25) and T2091(IND) E(25) forms. These older edition numbers are the actual available forms read, not invented 2026 forms. The source list below links them.

**Resolve source conflicts before answering.** Enacted section 116 controls the tax and purchaser-liability formulas. The current CRA process page controls current submission channels and addresses over the 2011 circular. The old T2062C explanatory list of private shares/trust interests predates the current TCP definition: use section 248, not that list, to decide whether property is TCP. The old circular's T1261 attachment and annual-return mailing instructions are not current instructions. Do not treat a transport download, a proposed law, a source check or an AI review as an accountant's approval. This version has no named professional approval; use only the approval actually returned for the exact method/version.

## Ask the client first

- **Residence at the date of disposition.** Was the vendor non-resident (or deemed non-resident by a treaty) on the closing date? If residence is unclear, work it out first with the ca-tax-residency skill.
- **What exactly is being sold?** Canadian land or buildings, a rental property, a cottage, a former home, unlisted shares, listed shares, a partnership or trust interest, business assets, resource or timber property, a life insurance policy.
- **For shares or interests:** is the company listed on a designated stock exchange? At **any time in the 60 months** before the sale, did more than 50% of the share's value come from Canadian real property, resource property or timber property? For listed shares or relevant mutual-fund interests: did the combined taxpayer, non-arm's-length persons and partnerships covered by paragraph (e) hold **25% or more** of a class or units at the **same particular time** that the more-than-50% property-value test was met? A 2% individual holding is not enough information.
- **Dates and amounts:** proposed or actual closing date, vendor's ownership share, proceeds, any section 116 FMV substitution for a gift or non-arm's-length deal, Canadian-dollar ACB with historical exchange rates, separate selling costs, capital cost/UCC history and supported land/building allocation. Get each existing certificate, its purchaser/property details and its actual limit or amount.
- **Was the property ever depreciable** (rental building, business equipment)? Was capital cost allowance claimed? That drives Form T2062A and the 50% rate on the building.
- **Treaty country and treaty claim.** Where is the vendor resident for treaty purposes, and does the treaty exempt this gain? Are vendor and purchaser related?
- **Was it ever the vendor's home?** Years owned, years resident in Canada, year of acquisition, other properties the family designated.
- **Tax identification number:** SIN, ITN, TTN, BN or trust account number. For an individual without an existing number and not eligible for a SIN, apply for an ITN (Form T1261) separately and early. Corporations and trusts use their own account types; do not apply for an individual ITN for them. A purchaser filing T2062C does not need to obtain a new Canadian tax number just for that notice.
- **Any unpaid Canadian tax** for earlier years, any outstanding 2022–2024 Underused Housing Tax obligations for a residential property, the other TCP sold during the year, and the other Canadian income that determines final tax, annual-return obligations and the no-return test.
- **Who holds the purchase money** (usually the purchaser's lawyer or notary) and how much is being held back pending the certificate.

## The method, step by step

1. **Confirm non-residence** at the disposition date. If the vendor is resident, section 116 does not apply (and the ca-tax-residency skill covers any departure tax).
2. **Classify the property** as TCP or not, using the table in "What counts as taxable Canadian property" below. If it is not TCP and is outside the specific section 116(5.2) categories, the ordinary capital-gain section 116 route does not apply; do not use that conclusion to exempt business income, a life policy, resource property or deemed TCP.
3. **Check whether it is excluded property** under s.116(6) (for example shares listed on a recognized stock exchange, units of a mutual fund trust, bonds and mortgages, or treaty-exempt property). Excluded property needs no section 116 notice and carries no purchaser liability, but a gain can still be taxable in Canada and reportable on a return (IC72-17R6, para 3).
4. **Check treaty protection.** If the treaty fully exempts the gain, the property is treaty-protected. If vendor and purchaser are related, it only becomes treaty-exempt (and excluded) if the purchaser files a notice within 30 days. See "Treaty-protected property".
5. **Pick the form.** T2062 for capital property (land, shares, non-depreciable property, and the gain on depreciable property); T2062A for depreciable TCP (recapture or terminal loss), inventory real property, resource and timber property; distinguish the capital gain from the fully taxable income component; T2062B for a life insurance policy (the insurer files it). A rental building usually needs both T2062 and T2062A.
6. **Notify the CRA.** For the ordinary section 116(1)/(3) route, apply before closing (the CRA recommends at least 30 days ahead) or notify no later than **10 days after** the actual disposition, subject to the precise unchanged-proposal exception below. The ten-day penalty timeframe does not apply to the separate subsection (5.2) forms. Arrange their certificate early nevertheless: the purchaser's 50% liability has its own remittance deadline. Supply the supporting documents and arrange payment or acceptable security; do not postpone a required notice just because funds or an ITN are pending.
7. **Compute the payment on account.** For T2062 property: **25% × max(0, proceeds − adjusted cost base)**. Selling costs are ignored in this calculation. For T2062A property: an amount the CRA accepts, using individual, trust or corporate rates on the fully taxable amount.
8. **Get the certificate.** The CRA issues **T2064** (proposed disposition) or **T2068** (actual disposition) to vendor and purchaser once the information is complete and payment or security is received. If the actual deal differs from the proposal (different buyer, higher price, lower ACB), file again.
9. **Purchaser side.** Apply the actual statutory exception or certificate first. Otherwise ordinary liability is **25% × max(0, cost − subsection (2) certificate limit)**; subsection (5.2) property uses **50% × max(0, amount payable − subsection (5.2) certificate amount)**. Never calculate rate × price − unscaled certificate limit. The certificate amount is the price it covers, not the vendor's tax deposit. A partial certificate can leave a remittance due within 30 days after the acquisition month ends. A lawyer's holdback is not itself a payment to the CRA, nor an automatic extension.
10. **File the Canadian return** for the year of disposition (a T1 for an individual, normally by April 30 of the following year, with the qualifying business-filer extension and separate balance-due rule below) unless the no-return exception applies. Attach Copy 2 of the certificate. The payment on account is only an interim payment: the final tax is set on assessment, and any excess is refunded.

## Key figures and time limits (tax year 2026)

| Item | Figure or limit | Source |
|---|---|---|
| Share look-back period for TCP | any time in the **60-month** period ending at the disposition | ITA s.248(1) TCP (d), (e) ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)) |
| Value test for shares and interests | **more than 50%** of FMV from Canadian real, resource or timber property | ITA s.248(1) TCP (d) ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)) |
| Ownership test for listed shares | **25% or more** of any class (with non-arm's-length persons and partnerships) | ITA s.248(1) TCP (e) ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html)) |
| Vendor notice of actual disposition | not later than **10 days** after the disposition | ITA s.116(3) ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html)) |
| Recommended lead time for a proposed-disposition notice | at least **30 days** before closing | IC72-17R6 para 6 ([official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html)) |
| Vendor payment on account (T2062 property) | **25% × max(0, proceeds − ACB)** before any accepted exemption adjustment; no selling-cost deduction | ITA s.116(2), (4); IC72-17R6 para 41 ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html)) |
| Purchaser liability, general TCP | **25% × max(0, cost − subsection (2) certificate limit)** unless the statutory exception applies | [ITA s.116(5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html) |
| Purchaser liability, s.116(5.2) property | **50% × max(0, amount payable − subsection (5.2) certificate amount)** unless the statutory exception applies | ITA s.116(5.3) ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html)) |
| Purchaser remittance deadline | within **30 days** after the end of the month of acquisition | ITA s.116(5), (5.3) ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html)) |
| Purchaser treaty notice (s.116(5.02)) | on or before **30 days** after acquisition | ITA s.116(5.02) ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html)) |
| Late vendor notice penalty | **$25** a day, minimum **$100**, maximum **$2,500** | ITA s.162(7); CRA penalty page ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html)) |
| Late purchaser remittance penalty | **3%** (1-3 days), **5%** (4-5 days), **7%** (6-7 days), **10%** (more than 7 days); **20%** where an earlier penalty under the relevant remittance rules was payable in the year and the new failure is knowing or grossly negligent; on-time remittance in the wrong manner attracts 3% | ITA s.227(9); IC72-17R6 para 56 ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-227.html)) |
| Inclusion rate for capital gains | **1/2** of the capital gain | ITA s.38(a) ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html)) |
| Non-resident surtax (instead of provincial tax) | **48%** applied to tax otherwise payable and the section 120 allocation; not 48% of proceeds or gain | ITA s.120(1) ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-120.html)) |
| Individual return due | **April 30** of the year after the disposition (2026 disposition: April 30, 2027) | CRA disposing page ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html)) |
| Corporation return due | **six months** after the end of the tax year | CRA disposing page ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html)) |
| Trust return due | **90 days** after the end of the trust's tax year | CRA disposing page ([official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html)) |

**The ordinary inclusion rate is 1/2.** Current [ITA section 38(a)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) is the authority for the ordinary taxable capital gain. Specific statutory zero-inclusion exceptions are not a general exemption for selling Canadian real property. The old 2024 increase and the CRA's [31 January 2025 administration announcement](https://www.canada.ca/en/revenue-agency/news/newsroom/tax-tips/tax-tips-2025/update-cra-administration-proposed-capital-gains-taxation-changes.html) are historical proposals, not authority to apply two-thirds or a 35% section 116 rate to this 2026 sale. The old guide's quotation about cancellation is no longer on the current corporate What's New page; do not present that missing quotation as freshly verified. The section 116 certificate payment is a different interim calculation from annual tax.

**Proposed changes after 2026, not the 2026 calculation.** The [Budget 2026 Notice of Ways and Means Motion, Taxable Canadian Property, clauses 1–2](https://www.budget.canada.ca/2026/report-rapport/nwmm-amvm-1-en.html) proposes corporate vendor payments of 15%, corporate-purchaser cases at 15%/30%, and a conditional section 85 rollover acquisition exception with elections, reasonable inquiry and notice within 30 days. It also proposes clock resets when an amended election creates Canadian income and a five-year anti-avoidance/look-through measure. Those clauses expressly target dispositions **after 2026**. This is a proposal, not an enacted 2026 exception or a general rollover waiver. Recheck enacted law and the actual effective date before advising on a later closing.

**Capital gains deduction: residence gate, not a blanket denial to every departing seller.** The lifetime capital gains exemption requires residence in Canada throughout the year (or residence for part of the year plus throughout the year before or after) ([T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)). A non-resident for the whole year cannot claim it.

## What counts as taxable Canadian property ([ITA s.248(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html))

TCP of a taxpayer at any time is property that is:

| Property | TCP? | Condition |
|---|---|---|
| (a) Real or immovable property situated in Canada | **Always** | Land, buildings, condos, cottages, a former home |
| (b) Property used or held in, Class 14.1 property of, or inventory of, a business carried on in Canada | Yes | Excludes property of an insurance business, and (for a non-resident) certain international ships and aircraft on a reciprocal basis |
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
- **Emigrants.** An individual's Canadian real property is ordinarily excluded from the departure deemed disposition by section **128.1(4)(b)(i)**. The elective disposition is under **128.1(4)(d)** (T2061A), not subparagraph (b)(v). That election can change the later ACB through deemed reacquisition; it does **not** make Canadian land cease to be TCP or exempt a later non-resident sale from section 116. Get the actual filed election and valuation, reconcile the new basis, and use ca-tax-residency for the departure work. [ITA section 128.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html).

**Excluded property** ([s.116(6)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html)): no notice, no certificate and no purchaser liability, but the gain may still be taxable. It includes: property that is TCP solely because of a deeming provision; business inventory other than real property, resource or timber property; a share listed on a **recognized** stock exchange (or SIFT wind-up entity equity); a mutual fund trust unit; a bond, debenture, bill, note, mortgage, hypothecary claim or similar obligation; property of a licensed non-resident insurer carrying on insurance business in Canada; property of an authorized foreign bank carrying on Canadian banking business; options on and interests in those; and **treaty-exempt property**.

## Section 116: notice, payment and certificate ([IC72-17R6](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html))

**Two routes to a certificate.**

- **Proposed disposition (s.116(1), (2)).** The vendor "may, at any time before the disposition" send a notice with the proposed purchaser's name and address, a description of the property, the estimated proceeds and the ACB. On payment of **25% × max(0, estimated proceeds − ACB)**, or acceptable security, the CRA issues **Form T2064** fixing a "certificate limit" equal to the estimated proceeds. The CRA asks for the notice "at least 30 days before" closing. If the buyer changes, the proceeds turn out higher, or the ACB falls before closing, the vendor must also file a notice of the actual disposition within 10 days. No second subsection (3) notice is needed only when **all three** statutory conditions hold: same purchaser, estimated proceeds at least actual proceeds, and notified ACB no greater than actual ACB. Check them together. A higher price, lower ACB or different purchaser requires the actual notice. A proposal notice is not itself a certificate or proof of payment.
- **Actual disposition (s.116(3), (4)).** Otherwise the vendor "shall, not later than 10 days after the disposition" notify the CRA. The statute says by registered mail; the CRA also accepts the form online through My Account, Represent a Client or My Business Account, or by fax. On payment of **25% × max(0, proceeds − ACB)**, or security, the CRA issues **Form T2068**.

**When is the disposition?** Usually the closing date, when the executed deed is delivered to the purchaser (IC72-17R6 para 19). The 10 days run from then.

**Which form.**

- **T2062**: capital property that is TCP, including the capital gain on depreciable TCP.
- **T2062A**: s.116(5.2) property, that is depreciable TCP (for the recapture or terminal loss), real property in Canada held as inventory, Canadian resource and timber resource property, and interests or options in them; with Schedule 1 for resource property. File it "even if capital cost allowance has not been claimed" (IC72-17R6 para 15). A rental building usually needs **both** T2062 (gain) and T2062A (recapture), and two certificates are issued. The statutory 10-day notice in s.116(3) does not cover s.116(5.2) property, and the CRA does not apply the 10-day penalty timeframe to it, but without a s.116(5.2) certificate the purchaser is liable at 50%, so in practice the certificate is still obtained before or at closing.
- **T2062B**: a life insurance policy in Canada; the insurer files it and remits.
- **T2062C**: the **purchaser's** notice of acquiring treaty-protected property. No certificate is issued for it (IC72-17R6 para 49).

**Payment on account.** For T2062 property the CRA requires "a flat rate of 25% of the excess of the proceeds of disposition over the adjusted cost base"; selling costs are not taken into account and are claimed on the return instead (IC72-17R6 para 41). For T2062A property the amount is worked out at individual, trust or corporate federal rates because it is fully included in income (para 42). For a depreciable building: 25% of the gain on land and building, plus the applicable federal rate on the recapture (para 43). Security must be acceptable to the CRA; "A letter of undertaking is not considered acceptable security" in a treaty dispute (para 31). The current CRA process page expressly supports **wire transfer or mail (cheque)**. Include Section 116 and the account or case number in the payment note. Use the actual current payment instructions and separate cheque address below; obtain the correct wire destination/allocation instructions rather than inventing bank coordinates or an income-tax payment code.

**Supporting documents** include the purchase and sale agreement, proof of ACB, and an appraisal or valuation where needed. If the CRA thinks the reported ACB is wrong it treats the information as not provided and withholds the certificate (para 21). Foreign currency: ACB at the historical rate, proceeds at the rate on the disposition date (para 22).

**Gifts and non-arm's-length sales.** For a non-arm's-length disposition below FMV, an acquisition above FMV in the statutory case, or a gift **other than a gift on death**, subsection 116(5.1) substitutes FMV for the relevant proceeds and purchaser cost. Do not net this with an unrelated ordinary sale or assume a no-cash gift has no purchaser exposure. A death is a distinct deemed-disposition/estate case requiring review; this subsection expressly excludes a gift on death.

**Several vendors.** Each co-owner files a separate notice for their share. For a partnership, the CRA accepts one notice for all partners with a full listing (para 10).

**Underused Housing Tax link.** Under s.116(8) the CRA may refuse a certificate for residential property if the vendor has not filed Underused Housing Tax returns or paid that tax. The CRA says "Affected owners do not need to file a return or pay the underused housing tax (UHT) for 2025 and subsequent calendar years", but "the requirement to file a UHT return and pay the tax still applies to the 2022, 2023, and 2024 calendar years" ([CRA UHTN1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/uhtn1/introduction-underused-housing-tax.html)). This is enacted non-application for 2025 onward: [UHT Act sections 1.1 and 6.1](https://laws-lois.justice.gc.ca/eng/acts/U-0.5/FullText.html) respectively remove the tax and override sections 7 and 10 on returns for those years. Section 7 alone still contains generic filing language; read the overriding provision. For a 2026 certificate, check the actual outstanding 2022–2024 obligations, interest/penalties and CRA requirements under section 116(8), rather than demanding a new 2026 UHT return or declaring all historical liabilities repealed.

## Purchaser's liability ([ITA s.116(5), (5.3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html))

**General TCP (s.116(5)).** A purchaser who acquires TCP (other than depreciable property or excluded property) from a non-resident is liable to pay, on the vendor's behalf, **25% × max(0, purchaser's cost − certificate limit fixed under s.116(2))**. This does **not** apply if:

- after reasonable inquiry the purchaser "had no reason to believe" the vendor was non-resident;
- s.116(5.01) applies (treaty-protected property with the purchaser's notice, see below); or
- a s.116(4) certificate (T2068) has been issued to the purchaser for the property.

**Section 116(5.2) property (s.116(5.3)).** For depreciable TCP, inventory real property, resource or timber property and life insurance policies, the rate is **50% × max(0, amount payable − amount fixed in the s.116(5.2) certificate)**, with the same reasonable-inquiry and (5.01) exceptions.

**What it means in practice.** The liability is measured on the **price**, not the gain. The purchaser may deduct or withhold the amount from the price, and must remit it "within 30 days after the end of the month in which the purchaser acquired the property". Purchasers' lawyers therefore hold back 25% (or 50% on the building portion of a rental) until a certificate covering the full price is delivered. "Purchaser liability assessments are not subject to any time restrictions" (IC72-17R6 para 50). Remittances count as payments on the vendor's account.

**Reasonable inquiry** means prudent steps to confirm the vendor's residence; the CRA "will not make inquiries on behalf of a purchaser" (para 58). [Section 227(9)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-227.html) sets late-remittance penalties of 3% for 1–3 days, 5% for 4–5 days, 7% for 6–7 days and 10% for more than 7 days, plus prescribed interest. A required payment made on time but in the wrong manner attracts 3%. The 20% rule requires both an earlier penalty payable in the year under the specified remittance provisions and a knowing or grossly negligent new failure. Section 227(9.1)'s $500 limitation is for the stated payroll-withholding case, not a section 116 exemption. Do not quote a fixed interest rate without checking the relevant quarter.

**Mortgagees.** A mortgagee who takes a property by foreclosure is generally not a purchaser liable under section 116, unless foreclosure is used as a device to sell. Under a power of sale, title passes from the non-resident mortgagor to the buyer, so section 116 applies to that buyer (paras 53-54).

## Treaty-protected property ([ITA s.116(5.01), (5.02), (6.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html))

**Definitions.** "Treaty-protected property" is property any **income or gain** from whose disposition would, because of a treaty with another country, be exempt from Part I tax (s.248(1)). It is **treaty-exempt property** (and so excluded property) at the time of disposition if it is treaty-protected **and**, where purchaser and vendor are related, the purchaser gives the s.116(5.02) notice (s.116(6.1)).

**Which property is typically protected.** The CRA explains that most treaties let Canada tax gains "only on Canadian real and resources properties and on shares of companies that derive most of their value from such properties" ([CRA disposing page](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/disposing-acquiring-certain-canadian-property.html)). Canadian real property itself is almost never treaty-protected; for example the Canada-US Convention says gains "from the alienation of real property situated in the other Contracting State may be taxed in that other State" ([Article XIII(1)](https://laws-lois.justice.gc.ca/eng/acts/C-10.7/FullText.html)). Share and business-property cases turn on the wording of the specific treaty article (including its own look-back and value tests) and any protocol, so read the treaty.

**Purchaser's notice (s.116(5.02)).** The purchaser sends the CRA, "on or before the day that is 30 days after the date of the acquisition", a notice giving: the acquisition date; the vendor's name and address; a description of the property; the amount paid or payable; and the treaty country. Form T2062C is the CRA's form for it.

- **Related purchaser:** the notice is **required** for the property to be treaty-exempt. If it is missing or late, "the notification will be invalid and the vendor will be required to notify the CRA of the disposition", and the normal purchaser liability applies.
- **Unrelated purchaser, property actually fully treaty-protected:** subsection (6.1) can make it excluded without a purchaser notice. That is a substantive treaty conclusion, not a safe assumption from a foreign address. The purchaser is protected from liability under s.116(5.01) only if, after reasonable inquiry, they conclude the vendor is treaty-resident, the property would be treaty-protected, **and** they send the notice. The CRA "will generally not issue such an assessment" against an unrelated purchaser who filed T2062C and made every reasonable effort. A late T2062C is invalid. The CRA generally does not acknowledge receipt.

**Vendor claiming a treaty exemption on T2062.** The vendor names the treaty provision and supplies proof, for example NR301 (the general non-resident person declaration, not only individuals), NR302 for partnerships or NR303 for hybrid entities, a certificate of treaty residence where needed, and proof of entitlement under any limitation-on-benefits provision. The existing Canadian/US example may require treaty-residence evidence such as Form 6166; this guide does not determine US domestic tax. If the CRA disagrees, the vendor must pay or secure the tax before the certificate issues (IC72-17R6 paras 29-31).

**On the return.** "Do not report any gain or claim a loss from the disposition of taxable Canadian property if, under a tax treaty, any gain from the disposition of the property would be exempt from tax in Canada"; if a return is required, attach a note saying so ([T4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html)).

## Reporting the gain on the Canadian return ([CRA Guide T4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html))

**Who must file.** A non-resident must file a Canadian return for the year if they "realized a taxable capital gain or disposed of taxable Canadian property" in the year (T4058). The section 116 payment is not the final tax: "All payments ... that you or the buyer makes to the CRA as a result of a disposition are considered interim payments. You make a final settlement of tax for the disposition when you file your return."

**No-return exception ([ITA s.150(5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html)).** A disposition is an "excluded disposition", and no return is needed for it, only if **all** of these hold: the taxpayer is non-resident at that time; **no Part I tax is payable for the entire year**; **at the time of that disposition**, the taxpayer is not liable for any amount for a previous year (other than amounts for which the CRA then holds adequate section 116 or 220 security); **and** each TCP disposed of in the year is either excluded property or property for which the CRA issued a certificate under s.116(2), (4) or (5.2). A capital gain alone does not prove positive tax payable after the year's permitted deductions, losses and credits. Conversely a loss on this sale does not prove zero whole-year tax. Document the actual annual computation, prior liabilities or accepted security and **every** TCP disposition in the year. This definition does not waive another filing obligation. In particular CRA T4058 requires a return, Schedule 3 and the principal residence designation when claiming that exemption, even where its four general no-return conditions appear satisfied.

**How an individual reports.**

- Select the actual T4058 package for the residence/income situation. A person non-resident throughout the year with only this capital gain generally uses the non-resident/deemed-resident package; a part-year emigrant uses the appropriate departure return, while employment or a business permanent establishment may require the provincial/territorial package and allocation. Complete **Schedule 3** for the capital component and carry the taxable amount to **line 12700**. Do not substitute the section 116 gross-price holdback.
- Do not classify income by the form name alone. A depreciable building may have both a **capital gain** (Schedule 3/12700) and **recapture** included fully in the relevant income computation. T4058 separately routes Canadian life-policy income and real property held as inventory, resource or timber income to **line 13000 or 13500, whichever applies**, with a disposition-details note instead of Schedule 3 for those income amounts. For these income categories a treaty exemption is claimed as an offset on **line 25600**; that differs from the treaty-protected capital-gain omission-and-note rule above.
- Recapture of capital cost allowance on a rental building is fully included in income.
- Selling costs reduce the gain on the return even though they were ignored for the payment on account.
- Attach **Copy 2** of the certificate of compliance (T2064 or T2068).
- Reconcile the vendor's deposit and purchaser's actual CRA remittances against the same disposition and CRA account. Claim the credited interim payments through the actual return/CRA assessment instructions; do not invent a return-line number or include a lawyer's unremitted holdback as tax paid. Exclude penalties and interest from refundable tax deposits.

**Tax rate.** Only 1/2 of the gain is taxable (s.38(a)). If the non-resident has no income earned in a province (for example only TCP gains), "Other" is entered as the jurisdiction and they pay federal tax "plus the surtax for non-residents and deemed residents of Canada" (T4058), which is **48%** of the federal tax on that income (s.120(1)), instead of provincial tax. The available 2025 package is a filing-layout reference, not proof a final 2026 package has been published. Use the actual applicable-year enacted brackets, credits, loss rules and any AMT calculation when computing final tax; this guide does not manufacture a final dollar tax from a gain alone. Where the person also has employment income or a business with a permanent establishment in a province, Form T2203 splits the tax.

**Excess payment.** After assessment, "any excess payment is refunded or provision is made for the release of security" (IC72-17R6 para 60). A return filed before the end of the tax year is processed only after the year ends.

## Principal residence of a non-resident ([Folio S1-F3-C2](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-1-individuals/folio-3-family-unit-issues/income-tax-folio-s1-f3-c2-principal-residence.html))

A home in Canada is real property, so it is **always TCP** and a sale by a non-resident falls under section 116 even if part of the gain is exempt.

**The exemption formula** ([ITA section 40(2)(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html); Folio paragraphs 2.20–2.23). The statutory remaining gain is **A − A × (B / C) − D**. The common exemption component **A × (B / C)** is the whole reduction only where **D = 0**. D is the additional capital-gains-election reduction in the specified pre-23-February-1994/T664 or T664(Seniors) cases. Get those records and the current worksheet if applicable; do not silently set D to zero for an older property. For the ordinary calculation:

- **A** is the gain otherwise determined.
- **B**, if the owner "was resident in Canada during the year that includes the acquisition date", is **1 +** the number of tax years ending after the acquisition date for which the property was their principal residence **and during which they were resident in Canada**. If they were not resident in Canada in the acquisition year, B has **no "1 +"**. That limit applies to dispositions **on or after October 3, 2016**, which the current form expresses as after October 2, 2016.
- **C** is the number of tax years ending after the acquisition date during which they owned the property.

**What this means for a non-resident seller.** Full tax years owned entirely while non-resident count in C but not B, so the exempt share shrinks for each year owned while non-resident. "During" means at any time in the year, so the departure year can still count if the home was designated for it. A person non-resident **throughout the acquisition year** gets no "plus 1" year; Canadian residence during any part of that year can satisfy the acquisition-year residence condition (T4037). One property per family unit can be designated for each year.

**Reporting.** The designation is made on Schedule 3 and **Form T2091(IND)** with the return for the year of sale (Folio para 2.15). The section 116 notice is still required, and the CRA says "The tax or security required may be reduced accordingly where the gain is reduced by the principal residence exemption". For the notice-stage reduction request, send Form T2091(IND), or a letter signed by the taxpayer, with the section 116 notice. That letter option does not replace the annual Schedule 3 and T2091(IND) designation required with the return. Reconcile the current form to the legal variables and retain a year-by-year residence/designation schedule: only eligible Canadian-resident designated years enter B; all relevant ownership years enter C. Do not reuse the circular's old exemption-line number. On actual T2091(IND) E(25), lines 1–3 record designated years, lines 5–7 count ownership years, line 18 is the gain before exemption, line 20 is the eligible years plus any permitted one, line 22 is the **divisor**, line 23 the ordinary exemption amount and line 24 the remaining gain; the eventual amount goes through lines 54/57 to Schedule 3 line 15800. A 1994 election needs Part 4/T2091(IND)-WS. For electronic filing retain the form; for paper filing complete, sign and attach it. Use the actual sale-year form when issued.

**Departure note.** Leaving Canada does not trigger a deemed disposition of Canadian real property, so the whole gain (including growth after departure) is dealt with on the later sale, reduced by the formula above. An election under section **128.1(4)(d)** (T2061A) can instead create a departure disposition and reacquisition that changes the later basis. Even then the later Canadian property is still TCP and section 116 must be checked. See ca-tax-residency and reconcile the election, departure valuation and later basis to avoid taxing the same gain twice or omitting the post-departure gain.

## Boundaries and exceptions

| Situation | Treatment | Source |
|---|---|---|
| Vendor resident at closing | Section 116 does not apply | s.116(1), (3); IC72-17R6 para 5 |
| Vendor resident at signing, non-resident at closing | Section 116 applies | IC72-17R6 para 5 |
| Purchaser is Canadian or foreign | Irrelevant to whether section 116 applies | IC72-17R6 para 5 |
| Listed shares, combined paragraph (e) persons/partnerships under 25% of every class throughout 60 months | Not TCP under this test; ordinary non-resident capital gain outside section 115, no section 116 notice | s.248(1) TCP (e) |
| Listed shares that are TCP (25%+ and real-property rich) | Excluded property if listed on a recognized exchange: no notice or purchaser liability, but gain taxable unless treaty-exempt | s.116(6)(b); IC72-17R6 para 3 |
| Unlisted shares, more than 50% real-property value at any time in last 60 months | TCP; notice and purchaser liability apply | s.248(1) TCP (d) |
| Unlisted operating company, never more-than-50% Canadian real/resource/timber rich in 60 months | Not TCP; no notice, no withholding | CRA disposing page |
| Rental building (depreciable) | T2062 and T2062A; 50% purchaser rate on the building, 25% on the land | [s.116(5.2), (5.3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html); IC72-17R6 para 15 |
| Land held as inventory (developer) | T2062A; 50% purchaser rate absent certificate/exception; discretionary qualified-business certificate treatment requires the conditions below, not self-declared exemption | IC72-17R6 para 36 |
| Treaty-protected property, unrelated purchaser | Excluded property; optional T2062C within 30 days protects purchaser | s.116(5.01), (6.1); CRA page |
| Treaty-protected property, related purchaser | Treaty-exempt only if purchaser files within 30 days; otherwise normal rules | s.116(6.1); IC72-17R6 paras 27-28 |
| Proposed disposition later changes (new buyer, higher price, lower ACB) | New notice within 10 days of actual disposition | IC72-17R6 para 6 |
| Share-for-share exchange deemed not a disposition by s.51(1)(c) | No vendor notice; the corporation may be a purchaser and can ask for a certificate | IC72-17R6 para 40 |
| Foreclosure by mortgagee | Generally no purchaser liability | IC72-17R6 para 53 |
| Proposed dispositions and s.116(5.2) dispositions | Not subject to the 10-day penalty timeframe | CRA penalty page |
| Late notice caused by circumstances beyond control | Ask for penalty relief under s.220(3.1), to the office that issued the certificate | CRA penalty page |

## Worked cases

Authorities: [ITA section 116](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html) and [IC72-17R6](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html).

**Case 1: original Canadian cottage example, certificate obtained.** A US-resident individual sells an Ontario cottage (never rented, never her home) on 15 June 2026. Proceeds $800,000, ACB $500,000, selling costs $40,000.

- Property: Canadian real property, so TCP; not excluded; not treaty-protected (Article XIII(1)).
- Form T2062. Payment on account: 25% x ($800,000 - $500,000) = **$75,000**. Selling costs are ignored here.
- The CRA issues T2068 once paid (or T2064 if she filed before closing).
- 2026 return (due April 30, 2027): gain $800,000 - $500,000 - $40,000 = $260,000; taxable capital gain 1/2 x $260,000 = **$130,000** on line 12700. Assuming this is a full-year non-resident with no income earned in a province, apply the section 120 surtax to the applicable federal-tax base, not directly to the $130,000 gain. Final dollars require the annual facts. Reconcile the $75,000 actual deposit and any purchaser remittance for credit once, with excess refunded after assessment.

**Case 2: same sale, no certificate at closing.** The purchaser's lawyer holds back 25% x $800,000 = **$200,000**. Unless an applicable statutory exception or certificate removes/reduces the exposure, the purchaser remits the amount due within 30 days after the end of June 2026, that is by **July 30, 2026**. If the purchaser does not withhold and remit, the purchaser owes the $200,000 itself, with no time limit on the assessment. A certificate "protects the purchaser from any further tax liability" for that disposition (IC72-17R6 para 46), but a proposed certificate covers only its particular purchaser/property and limit; a partial certificate does not release every dollar of holdback. Reconcile amounts paid and the actual transaction before releasing funds.

**Case 3: rental property, split land and building.** A non-resident sells a Canadian rental property for $1,000,000: land $600,000, building $400,000. No certificates are obtained.

- Land (capital property, TCP): purchaser liability 25% x $600,000 = **$150,000** (s.116(5)).
- Building (depreciable TCP, a s.116(5.2) property): 50% x $400,000 = **$200,000** (s.116(5.3)).
- Total purchaser exposure: $150,000 + $200,000 = **$350,000**.
- The vendor should file T2062 (gain on land and building) and T2062A (recapture on the building), get two certificates, and report the recapture as fully taxable income on the return.

**Case 4: late notice.** Closing 1 March 2026, so the notice is due by 11 March 2026. The vendor notifies on 10 April 2026: 30 days late, 30 x $25 = **$750** (between the $100 minimum and $2,500 maximum). Three days late: 3 x $25 = $75, raised to the **$100** minimum. 120 days late: 120 x $25 = $3,000, capped at **$2,500**.

**Case 5: former home sold after emigrating.** Assume D = 0, no selling costs, no departure elective disposition or change-of-use adjustment, actual principal-residence eligibility and no conflicting family designation. Bought in 2015 for $420,000 while resident; lived in it and designated it for 2015 to 2020; emigrated in 2020 and kept it; sold in 2026 for $900,000 while non-resident.

- Gain A = $900,000 - $420,000 = $480,000.
- Resident in the acquisition year, so B = 1 + 6 (2015 to 2020) = **7**. C = tax years ending after acquisition while owned, 2015 to 2026 = **12**.
- Exempt: $480,000 x 7 / 12 = **$280,000**. Remaining gain $480,000 - $280,000 = $200,000; taxable 1/2 x $200,000 = **$100,000**.
- Section 116 notice still required. The payment on account may be reduced for the exempt part (IC72-17R6 para 73): send T2091(IND) with the eligible residence/designation-year schedule, or a signed letter, with the T2062. Payment on account: 25% x ($480,000 - $280,000) = **$50,000**. Designate again on Schedule 3 and T2091(IND) with the 2026 return.

**Case 6: the 60-month look-back.** A non-resident sells unlisted shares of a Canadian company on 1 October 2026. The company sold its Canadian land, which had been more than 50% of its value, in March 2023.

- March 2023 is within the 60 months ending 1 October 2026, so the shares are **TCP**: notice, certificate and purchaser liability apply (unless treaty-protected).
- If the land had been sold in June 2021, the entire relevant 60-month window ended at this disposition contains no qualifying more-than-50% Canadian real/resource/timber value, and no other TCP deeming rule applies, the shares are **not TCP**. Prove the valuation history throughout the window, not merely the date the land was sold. The strict threshold is more than 50%, not 50% or more.

**Case 7: listed shares.** A non-resident individually holds 2% of a TSX-listed company. It is not TCP under paragraph (e) only if the **combined** relevant persons/partnerships never met the 25% ownership test at a time when the more-than-50% value test also held during the window; a 2% personal holding alone proves nothing. With that combined-under-25% assumption and no other TCP deeming rule, no Canadian section 115 capital-gain charge or section 116 notice arises. If instead combined ownership was 30% of a class and more than 50% of value came from Canadian real estate at the **same particular time** in the window, the shares are TCP; but a share listed on a recognized stock exchange is excluded property, so there is no section 116 notice or purchaser liability. The gain is still taxable in Canada unless a treaty exempts it, and a return is needed if tax is payable.

## When to refuse or refer

Refer to a Canadian cross-border tax adviser, or decline, when:

- residence or treaty residence at the closing date is unclear or disputed;
- the vendor is a corporation, trust, estate (including the death of a non-resident owner) or partnership;
- the vendor claims a treaty exemption on shares or business property and the treaty article, protocol or anti-abuse rules need analysis;
- the transaction involves a section 85 rollover, a corporate reorganization, resource or timber property, inventory land, or a life insurance policy;
- the property is in Quebec: this skill covers only the federal rules, so check Revenu Québec's own requirements for dispositions by non-residents;
- the CRA disputes the ACB, the valuation or the treaty claim, or a purchaser liability assessment has been raised;
- Underused Housing Tax returns or tax for 2022 to 2024 may be outstanding;
- the client wants to close without a certificate or without a holdback.

This skill explains the federal rules; it does not replace a review of the documents by a Canadian professional. Before using a principal residence exemption, resolve capital-versus-inventory treatment, any applicable residential-property flipping rule, rental/change-of-use history, CCA and any prior election. Those facts are not defaulted from the owner calling the asset a home. [C09][C13][C21][C38]

## Filing and payment ([CRA: Disposing of or acquiring certain Canadian property](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/disposing-acquiring-certain-canadian-property.html))

**Vendor.**

- **Identification number first.** A former resident uses their SIN. An individual without an existing SIN, TTN or ITN who is not eligible for a SIN applies for an ITN on Form T1261, sent "separately and in advance of your disposition request". A certificate cannot be issued without an identification number (IC72-17R6 para 9).
- **Notice:** T2062 with supporting documents before closing or within 10 days after under subsection (3), subject to the unchanged-proposal conditions. T2062A/T2062B follow subsection (5.2), not that ten-day penalty timeframe; arrange them early enough to manage purchaser remittance. Submit online (My Account, Represent a Client or My Business Account, "Submit documents") or by mail or fax to the Section 116 Centre of Expertise for the region where the property is. For real property that is the property's address; for shares, the corporation's head office.
- **Payment:** use a separately allocated section 116 payment by the supported wire-transfer or cheque route, with Section 116 and the account/case number. Obtain confirmed wire instructions; do not invent bank details. Mail cheques, with Section 116 and the account/case reference as instructed, to **Canada Revenue Agency, PO Box 3800 STN A, Sudbury ON P3A 0C3, Canada**. This payment address is different from the regional notice address and the ITN address. Retain cleared-payment/allocation evidence; obtain confirmed CRA instructions before an alternative transfer.
- **Return:** an ordinary individual's 2026 return is due **30 April 2027**. If the statutory business-filer conditions for the individual or spouse/common-law partner apply, the return can instead be due **15 June 2027**, while the ordinary balance remains due **30 April 2027**. Corporations file within six months after year-end; trusts generally within 90 days after year-end. Separate death, demand-to-file and other special deadlines must be checked. Attach Copy 2 as applicable and retain electronic-filing support. A late return can attract a penalty when its statutory conditions are met; unpaid tax attracts interest. Do not say a zero-balance late return always attracts the ordinary balance-based penalty. [ITA section 150(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html), T4058 and the applicable-year package.

**Purchaser.**

- Confirm the vendor's residence by reasonable inquiry, and calculate 25% × max(0, cost − subsection (2) certificate limit), or 50% × max(0, amount payable − subsection (5.2) certificate amount), unless the actual statutory exception applies, until a certificate covering the price arrives.
- Without a certificate, remit to the Receiver General within 30 days after the end of the month of acquisition, identifying it as a subsection 116(5) or 116(5.3) payment with the vendor's and purchaser's names and addresses (IC72-17R6 para 55).
- Treaty-protected property: send T2062C (or an equivalent notice) within 30 days of acquisition. Required if related to the vendor; optional but protective if unrelated.

**Returns being filed now for 2025.** For a 2025 disposition, the individual return was due April 30, 2026. The rules above (1/2 inclusion rate, 25% and 50% rates, 10-day notice) were the same in 2025. If the 2025 return has not been filed, file it now with Copy 2 of the certificate; determine the actual balance, statutory filing/payment deadlines and applicable interest/penalty conditions rather than assuming a penalty solely from a late zero-tax return. A qualifying 2025 business-filer return could instead have been due 15 June 2026, with the ordinary balance still due 30 April 2026.

## Complete the actual certificate and purchaser forms

The form name does not settle the annual tax treatment. Prepare a disposition reconciliation showing each owner's share, each asset, the purchase price allocation, ACB/capital cost/UCC, certificate deposit, certificate limit, purchaser exposure, actual remittances and final-return treatment. All form amounts are Canadian dollars. Do not merge land and a depreciable building into one rate simply because they share a conveyance. [C01][C05][C32][C33]

### T2062: ordinary capital property and the capital-gain component

Use the actual T2062 E(21) instructions and pages5–6, subject to the law and current submission page. The form collects:

1. Vendor entity type and the appropriate BN, trust account or SIN/ITN/subsidiary ledger number; for an individual, name, date of birth, departure date if applicable, present address and country of treaty residence. If T1261 was sent separately, record that fact in the form's checkbox rather than pretending a number has been issued.
2. Vendor and purchaser contact/representative details and which addressee should receive correspondence. A signature or representative name is not proof of general access to CRA online accounts.
3. Asset category, proposed or actual disposition date, acquisition date, municipality/province/postcode and a description sufficient to identify the actual property, shareholding or interest. Attach a schedule for multiple properties where the form instructions permit it. Each co-owner normally reports only their own share. A partnership notice needs the full partner listing and allocation/support described by the circular and form.
4. Column1 proceeds, column2 ACB, column3 their difference, column4 supported exemptions, column5 the net gain. The form asks for 25% of the net gain as the interim payment. A supported exemption can reduce the deposit; neither the printed field nor a preliminary calculation proves the CRA has accepted it. Selling costs belong in the final-return calculation, not as a section 116 ACB deduction.
5. The page 6 questions: section 85 election/reorganization, rental/lease history and Part XIII withholding or unwithheld gross-rent statements, unpaid Canadian tax, last Canadian return, non-arm's-length transfer/gift and the FMV facts. Supply the relevant records; do not leave these questions blank merely because the closing lawyer has a price.
6. The vendor's certification, signer name/position, signature and date. Any form authorization is limited to the stated T2062/T1261 work and expires within six months of certificate issuance or finalization, whichever comes first; use the actual wording. It does not grant access to unrelated tax information or Represent a Client.

Support the ACB rather than copying a sale advertisement: acquisition/closing documents, improvements and historical currency conversions, sale agreement, valuations where needed, and the relevant ownership/departure/change-of-use/election records. For a former home include the designation/year schedule and any T664/T2091 worksheet or T2061A records; for shares/interests, include the applicable share/partnership records, financial statements and value history. Where claiming treaty relief, include the actual article, residence evidence, beneficial/qualified-person facts and the applicable NR301/302/303 declaration. The form's fuller property-specific support list also covers vendor-take-back mortgages, foreclosures, bundled business assets, trust interests and reorganizations; request the appropriate documents rather than applying a residential-property checklist to every asset. [C05 paras17–44][C32]

### T2062A: fully taxable components and depreciable property

Use T2062A even where no CCA has been claimed if the property falls within subsection 116(5.2). Where both forms apply, file T2062 and T2062A together with a reconciled allocation; do not charge two purchaser holdbacks on the same building merely because it has two vendor tax components. The land and building portions still have different purchaser-rate rules. [C05 paras15,41–43][C33]

The actual page 5 form repeats the entity, contact, dates and asset-identification fields and asks for:

- column1 proceeds and column2 capital cost;
- column3 the lesser of proceeds and capital cost for depreciable property; **for real property held as inventory or timber resource property, the instructions put proceeds directly in column3**;
- column4 UCC or cost amount, column5 the resulting income/loss, column6 supported exemptions and column7 net income/loss;
- the applicable **Part I federal tax on net income**, not a universal 25% payment. Resource property uses its actual T2062A Schedule 1 calculation, with the amount from lineH. Obtain the applicable schedule before preparing it; this guide does not invent the schedule's fields or a resource-pool computation.

Reconcile CCA schedules and UCC, capital improvements, rental/use periods, allocation evidence and the required property-specific support. For a building with a gain above capital cost, the capital-gain component can require T2062 in addition to the recapture computation on T2062A. Do not turn UCC into the capital-gain ACB or assume an asset-level loss automatically creates an annual terminal-loss deduction: class and continued-ownership rules need their own computation. The purchaser's potential 50% gross-price exposure is separate from this vendor's Part I federal-tax deposit. [C01(5.2),(5.3)][C05 paras15,42–43][C24][C33]

**Qualified-business policy is discretionary.** IC72-17R6 para 36 describes possible certificate relief for real property held as inventory in an established Canadian business, where the CRA is satisfied about prior income-account reporting and/or required instalments and no outstanding tax debts. It is not an automatic exclusion from section 116, not the capital-gains deduction and not permission for the purchaser to release funds without an applicable certificate/exception. For section 85 rollovers, corporate reorganizations or a section 51 exchange, retain professional review: the current 2026 law has no general 'rollover therefore no116' exemption. IC para 40's section 51 holder no-disposition case can still leave a corporation as purchaser; its subscription/stated-capital and certificate/security treatment must be considered. The proposed after 2026 section 85 route above is not a 2026 solution. [C01][C05 paras36,39–40][C41]

### T2062B: insurer-filed life policy disposition

T2062B E(16) is completed by the insurer, with copies for CRA, the policyholder and the insurer. It identifies the non-resident policyholder, insurer, purchaser if different, disposition date and policy, proceeds, policy adjusted cost basis, resulting income and the federal-tax payment. Attach the actual **T2062B Schedule 1**, authorization and payment as directed; this guide has read the T2062B itself, not every field of that separate schedule. These amounts are not an ordinary half-included land gain. The form covers the specified policy dispositions and treats the insurer as the purchaser for the applicable section 116 rules; refer the actual contract and section 148 event to a specialist rather than assuming every death benefit is a taxable policy disposition. [C01(5.2),(5.4)][C34]

### T2062C: purchaser notice, not a vendor certificate application

Complete actual Parts A–C: identify Type I/Type II property and a usable description, price and acquisition date; vendor name/address and country of treaty residence; purchaser identity/address/entity type, relationship to vendor and any **existing** tax account number. The purchaser certifies the information and its reasonable inquiry into treaty residence. Part D is an **optional** vendor certification; it supports inquiry but does not establish the substantive treaty exemption by itself. No new Canadian tax number is required solely for this purchaser notice. [C06][C35]

For the subsection 116(5.01) protection, document all three statutory conditions: reasonable inquiry supports the vendor's treaty-country residence; the property would be treaty-protected on that residence assumption; and a subsection(5.02) notice is provided on or before 30 days after acquisition. That notice condition applies to the safe harbor even for an unrelated purchaser. A related purchaser additionally needs a timely notice to make the actually treaty-protected property treaty-exempt under subsection(6.1). An unrelated purchaser may instead rely on property actually being treaty-exempt under(6.1); a bare foreign address does not prove that. [C01(5.01),(5.02),(6.1)]

Use the current CRA regional submission instructions rather than T2062C's old local-office wording. Keep the entire filed notice, supporting reasonable-inquiry records and delivery/portal/fax confirmation. CRA generally does not acknowledge receipt and issues no T2064/T2068 for T2062C. A filing receipt is not a ruling that the gain is exempt. Do not import the old form's broad private-Canadian-share/trust TCP descriptions or its 2004 draft foreign-bank note over current sections248/116. [C05 paras27–31,49–52][C06][C10][C35]

## Identification, submission and payment controls

### Individual ITN application is a separate process

Use an existing SIN, ITN or TTN. A person eligible for a SIN should obtain that number rather than apply for an ITN. An otherwise eligible non-resident individual needing an ITN for this sale uses actual T1261 E(25), checks the disposition reason, completes sections1–4, supplies the foreign home address even when using a Canadian correspondence address, and signs/dates the applicant certification. The actual form **does not accept an electronic applicant signature**. [C36]

Provide certified copies of current identity documents showing name, date of birth and photograph; **do not send original passports or identity documents**. The certification must be in original ink, with the certifier's name, title, signature, address and contact number, and meet the actual form's certifier requirements. A CPA certifier supplies their membership number in the private application, not in a public skill or answer. Do not self-certify. Include the required official English/French translations. An executor application additionally needs the prescribed death/will or appointment and executor identity records. [C36]

Mail the application and certified documents **separately and in advance** to **Attn: ITN Unit, Services and Benefits Division, Sudbury Tax Centre,1050 Notre Dame Ave, Sudbury ON P3A5C1, Canada**. The form gives a six-to-eight-week response estimate; it is not a promised certificate-processing or closing timetable. T1261 is not accepted by fax, scanned email or the section 116 document portals. Keep mailing proof, note the pending application on T2062/A and follow up if necessary. A missing ITN is not an extension of a required sale notice or annual return: T4058 instructs a near-deadline return to be filed with an explanatory note if the requested SIN/ITN has not arrived. [C06][C13][C36]

### Section116 documents: keep the actual channel evidence

The Act's subsection 116(3) refers to registered mail. CRA's current page also accepts online documents and fax for section 116 applications. Use those actual agency instructions without representing them as an amendment to the statutory wording. For the online path, choose **Submit documents** in My Account, My Business Account or Represent a Client, select the section 116 reason and distinguish a new request from additional documents for an existing case. For an existing case supply its number; do not create duplicate applications for routine follow-up. In Represent a Client, follow the current page's instruction **not to enter the vendor SIN/BN in the client access field** for this particular submission route. Use the section 116 submission option; do not assume ordinary representative authorization is required or that the T2062 authorization grants general account access. [C01(3)][C06]

Identify each attachment clearly, provide the description and contact details and retain the confirmation/reference number. The current page states a ten-file limit per session for My Account and Represent a Client, with combined attachments up to 500MB. For My Business Account it states the combined 500MB limit but does not specify that ten-file cap; follow the actual portal's current limits. For property in more than one region or several assets, follow CRA's multiple-property routing and include a clear schedule instead of sending inconsistent copies. Additional-document submissions need the existing case reference. [C06]

**Mail or fax.** Use the **current Section116 Centre of Expertise** for the property's location; the CRA page sets the location rules for business assets, a corporation's head office for shares, partnership property and trusts. Recheck that page for the actual address before dispatch; regional ordinary-mail and registered/courier addresses can differ. This is not the annual-return destination. Section116 fax numbers on the current page are **1-833-329-1161** from Canada/US and **418-566-0324** from outside Canada/US. Keep transmission proof and the correct case identifier; those numbers do **not** make T1261 faxable. [C06]

**Payment is separate from uploading a form.** Use the supported wire-transfer or cheque route above and obtain the actual bank instructions before any transfer. Ensure the payment reaches the correct vendor/section 116 case, distinguish the certificate deposit from the purchaser's statutory remittance and reconcile both so final tax credit is not duplicated. Acceptance of security is a CRA decision; a private undertaking or lawyer holdback is not automatically acceptable security. Do not release funds because someone uploaded an application or received a generic document receipt. [C01][C05 paras31,41–49,55,59–60][C06]

## Extra calculation and decision checks

These are controlled examples of the Canadian rules, not a calculation of a real client's final tax. Use the original seven cases above and the following controls together. Each price, deposit and certificate amount is a different input.

### Check 1: the original cottage deposit and final capital gain

The original Canadian-side treaty example's75,000 deposit and 130,000 taxable capital gain are different bases. Selling costs40,000 reduce the final gain, not the ordinary certificate deposit. The example does not calculate final federal tax, credits, losses or surtax dollars. [C01][C12][C16]

```oa-check
name: Canadian cottage deposit versus final capital gain
inputs:
  proceeds: 800000
  acb: 500000
  selling_costs: 40000
steps:
  certificate_base: max(0, proceeds - acb)
  vendor_deposit: certificate_base * 0.25
  final_gain: proceeds - acb - selling_costs
  taxable_capital_gain: final_gain * 0.5
expected:
  certificate_base: 300000
  vendor_deposit: 75000
  final_gain: 260000
  taxable_capital_gain: 130000
```

### Check 2: no, partial and sufficient ordinary proposed certificates

For a purchaser cost 800,000 and an applicable subsection(2) certificate limit600,000, exposure is **25% ×200,000=50,000**, not200,000−600,000. With no certificate it is200,000; a limit covering at least800,000 leaves zero under this formula. These are subsection(2) limit controls; an actual subsection(4) certificate is a distinct statutory exception. The limit600,000 is **not** a600,000 tax payment and not the vendor's75,000 deposit. Apply no-certificate remittance by 30July2026 for a15June2026 acquisition, unless the actual statutory protection changes that result before it is due. [C01(2),(4),(5)]

```oa-check
name: Ordinary purchaser certificate limits are deducted before applying rate
inputs:
  cost: 800000
  partial_limit: 600000
  excess_limit: 900000
steps:
  no_certificate: cost * 0.25
  partial_certificate: max(0, cost - partial_limit) * 0.25
  sufficient_certificate: max(0, cost - cost) * 0.25
  excess_certificate: max(0, cost - excess_limit) * 0.25
expected:
  no_certificate: 200000
  partial_certificate: 50000
  sufficient_certificate: 0
  excess_certificate: 0
```

### Check 3: original rental allocation and partial building certificate

Without certificates,600,000 land×25% plus 400,000 building×50% gives 350,000. If a valid subsection(5.2) certificate fixes300,000 for the building, its residual exposure is **50% ×(400,000−300,000)=50,000**; the uncovered land remains150,000, total 200,000. Verify which asset and purchaser each certificate actually covers. Do not subtract the vendor's estimated recapture tax from the gross building price as though it were the certificate amount. [C01(5),(5.2),(5.3)][C33]

```oa-check
name: Land and depreciable building use different purchaser bases
inputs:
  land_price: 600000
  building_price: 400000
  building_certificate_amount: 300000
steps:
  land_exposure: land_price * 0.25
  building_no_certificate: building_price * 0.5
  total_no_certificate: land_exposure + building_no_certificate
  building_partial_certificate: max(0, building_price - building_certificate_amount) * 0.5
  total_with_partial_building: land_exposure + building_partial_certificate
expected:
  land_exposure: 150000
  building_no_certificate: 200000
  total_no_certificate: 350000
  building_partial_certificate: 50000
  total_with_partial_building: 200000
```

### Check 4: original late-notice cases and on-time control

For a disposition actually subject to subsection(3),1March2026 plus 10 days is11March2026;10April2026 is30 days after that deadline, penalty750. Three late days give the 100 minimum,120 late days the 2,500 cap. No failure gives zero, not the minimum100. This does not impose that ten-day penalty on proposed dispositions or subsection(5.2) forms; discretionary relief under 220(3.1) is a separate decision. [C18][C25][C40]

```oa-check
name: Ordinary vendor late notice minimum maximum and no failure
inputs:
  days_3: 3
  days_30: 30
  days_120: 120
steps:
  short_late: min(2500, max(100, days_3 * 25))
  ordinary_late: min(2500, max(100, days_30 * 25))
  capped_late: min(2500, max(100, days_120 * 25))
  on_time: 0
expected:
  short_late: 100
  ordinary_late: 750
  capped_late: 2500
  on_time: 0
```

### Check 5: original former-home calculation with D=0

The stated2015–2026 ownership period contains12 tax-year ends after acquisition; six eligible designated resident years 2015–2020 plus the permittedone gives 7. Gain480,000, ordinary exemption280,000, remaining gain 200,000, taxable gain 100,000. The50,000 interim payment assumes CRA accepts that principal-residence adjustment. Prove eligible ordinary habitation/designation/residence, no conflicting family designation, D=0, no selling costs and the actual basis; do not apply the example blindly to an old1994 election, a rental conversion or property acquired throughout a non-resident year. Even full exemption requires the annual reporting/designation described above. [C15][C20][C21][C38]

```oa-check
name: Former Canadian home exemption and separate interim deposit
inputs:
  proceeds: 900000
  acb: 420000
  eligible_designated_years: 6
  plus_one: 1
  owned_years: 12
steps:
  gain: proceeds - acb
  b: eligible_designated_years + plus_one
  ordinary_exemption: gain * b / owned_years
  remaining_gain: gain - ordinary_exemption
  taxable_gain: remaining_gain * 0.5
  accepted_interim_deposit: remaining_gain * 0.25
expected:
  gain: 480000
  b: 7
  ordinary_exemption: 280000
  remaining_gain: 200000
  taxable_gain: 100000
  accepted_interim_deposit: 50000
```

### Check 6: TCP decisions require history and combined ownership

| Facts held constant except as stated | Canadian result |
|---|---|
| Original unlisted-share1October2026 sale; more-than-50% Canadian land value existed inMarch2023 | Within60 months: TCP unless another applicable rule changes the conclusion; separately check treaty/excluded status |
| Land soldJune2021; no qualifying more-than-50% Canadian real/resource/timber value anywhere in the entire relevant60-month window and no deeming rule | Outside paragraph(d), not TCP on those facts |
| Exactly50% qualifying value throughout the window | Does not satisfy the strict **more-than-50%** test |
| Listed-share personal 2% holding, combined relevant group 30%, more-than-50% property value at the same time in the window | Paragraph(e) can be met despite the personal 2%; recognized-exchange share then has separate section 116 exclusion |
| Combined relevant group 24.99% at every relevant time | Fails the at-least25% ownership test under paragraph(e) |
| Combined relevant group exactly 25% and qualifying value50.01% at the same relevant time | Meets these two thresholds; apply all other definitions and treaty rules |
| Group30% in one period but qualifying value only in another, with no point when both hold | Does not meet paragraph(e)'s same-particular-time condition on those facts |

Keep the original7 th case's30% alternative and the original6 th case's two land-sale dates; none of these cases authorizes a domestic American tax conclusion. [C10]

### Check 7: zero-gain certificate base and gift price substitution

An ordinary sale400,000 with ACB 450,000 has no positive subsection(2)/(4) certificate tax base. It still needs the applicable notice/certificate work unless excluded, and the purchaser without a certificate or exception can still face100,000 gross-cost exposure. A lifetime gift of Canadian land with FMV800,000 and ACB 500,000 uses the section 116(5.1)FMV substitution: ordinary vendor deposit75,000 and no-certificate purchaser exposure200,000, even where no cash changes hands. This is not a gift-on-death calculation. [C01(2)–(5.1)]

```oa-check
name: No positive vendor gain does not eliminate purchaser exposure
inputs:
  loss_sale_price: 400000
  loss_sale_acb: 450000
  gift_fmv: 800000
  gift_acb: 500000
steps:
  loss_sale_vendor_deposit: max(0, loss_sale_price - loss_sale_acb) * 0.25
  loss_sale_uncovered_purchaser: loss_sale_price * 0.25
  gift_vendor_deposit: max(0, gift_fmv - gift_acb) * 0.25
  gift_uncovered_purchaser: gift_fmv * 0.25
expected:
  loss_sale_vendor_deposit: 0
  loss_sale_uncovered_purchaser: 100000
  gift_vendor_deposit: 75000
  gift_uncovered_purchaser: 200000
```

### Check 8: annual-return and unchanged-proposal decisions

| Situation | Required decision |
|---|---|
| Same proposed buyer; actual price no higher and actual ACB no lower than notified; all subsection(3) conditions met | No new subsection(3) actual notice needed; still reconcile certificate coverage, payment and final-return obligations |
| Lower actual price but different buyer | Same-buyer condition fails; ordinary actual notice required within 10 days |
| Same buyer/price but lower actual ACB | ACB condition fails; ordinary actual notice required within 10 days |
| Sale loss but other Canadian income creates Part I tax for the year | Fails the no-tax-payable gate; this sale's loss does not create a whole-year no-return exemption |
| Zero whole-year Part I tax, all earlier liabilities paid or adequately secured **at the disposition time** as specified, every year's TCP disposed of certified/excluded, and no other filing duty | The section 150(5) excluded-disposition test can be satisfied; record all evidence |
| Those same facts but principal-residence exemption claimed | File the return/designation as instructed by T4058; do not omit it because no tax is payable |
| Related treaty buyer files a valid notice by 30 days and the property is actually fully treaty-protected | Subsection(6.1) treaty-exempt branch can apply |
| Related buyer merely obtains vendor's residence declaration but files no notice | Does not meet subsection(6.1)'s notice requirement; declaration alone is not exclusion |
| Unrelated buyer invokes subsection(5.01) but files no notice | That particular safe harbor fails even though an independently proven actual treaty-exempt-property branch may exist |
|2026 corporate vendor asks to use15%/30% or the new section 85 proposal | Do not apply it: current enacted 2026 section 116 remains the authority; proposed after 2026 rules require a fresh effective-law check |

[C01][C13][C14][C41]

## Required handoff and unresolved work

Return a working paper identifying: the actual residence date and status; property/TCP/excluded/treaty classification with supporting facts; the exact forms and owner shares; vendor deposit/security calculation; purchaser liability calculation and certificate coverage; each separate notice/remittance/annual deadline; proof of submissions and actual CRA payments; annual capital-gain/income/recapture/PRE treatment; and the final tax-versus-interim-payment reconciliation. Include the source/section and actual year for each figure. Do not name a Canadian accountant as approving this method because a different Canadian skill or the country directory names them: use only the exact method's approval record, and do not invent approval for this rewritten version.

List missing agreements, ACB/FX/CCA records, valuations, ownership history, treaty residence evidence, certificate documents, account allocation confirmations, schedules and annual facts as open items with the consequence for the conclusion. An estimated calculation can be shown with explicit assumptions, but unresolved mandatory facts mean the relevant result and completion status stay unresolved. A download, a proposed bank transfer, an unremitted holdback, a portal receipt or passing automated checks alone is not a filed notice, an issued certificate, a paid tax or a complete annual return.

## Completion checklist

- [ ] Vendor's residence (and treaty residence) at the closing date confirmed and documented.
- [ ] Property classified as TCP or not, with the 60-month look-back checked for shares and interests (and a corporate declaration obtained where relied on).
- [ ] Excluded-property and treaty-protected status checked; related or unrelated purchaser identified.
- [ ] Correct form(s) chosen: T2062, T2062A (depreciable, inventory land, resource, timber), T2062B, T2062C.
- [ ] Identification number in place (SIN, ITN, TTN, BN or trust number).
- [ ] Applicable notice deadline identified: ordinary subsection (3) notice within 10 days unless every unchanged-proposal condition holds; no invented ten-day penalty on subsection (5.2) forms; evidence of timely submission retained.
- [ ] Payment on account computed as 25% × max(0, proceeds − ACB) for the ordinary T2062 route, with any supported exemption adjustment, or CRA security agreed; fully taxable T2062A components separately calculated.
- [ ] Certificate T2064 or T2068 received; a new notice filed if the actual deal differed from the proposal.
- [ ] Purchaser's statutory exposure calculated with the correct 25%/50% rate **outside** max(0, price − applicable certificate limit/amount); deposit/limit distinguished; partial certificate and actual exception checked; remittance deadline diarised.
- [ ] Principal residence formula applied with only years of Canadian residence in B; T2091(IND) (or signed letter) sent with the section 116 notice to reduce the payment, and T2091(IND) filed with the return.
- [ ] Return for the year of disposition filed on time (or s.150(5) exception documented), with Schedule 3, line 12700 at the 1/2 inclusion rate, any recapture, Copy 2 of the certificate, and the section 116 and purchaser payments claimed.
- [ ] Cross-checked with the ca-tax-residency skill for departure tax and Part XIII items.

## Sources

- [C01] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-116.html). Read for ITA116: notice, certificates, purchaser liability, exclusions and UHT gate. Read 2026-11-14.
- [C02] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html). Read for ITA212: separate Part XIII boundary. Read 2026-11-14.
- [C03] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html). Read for ITA2: non-resident charge. Read 2026-11-14.
- [C04] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-115.html). Read for ITA115: non-resident Canadian income and treaty-protected gains. Read 2026-11-14.
- [C05] [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html). Read for IC72-17R6: operative paragraphs1–74, subject to current law/process. Read 2026-11-14.
- [C06] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/disposing-acquiring-certain-canadian-property.html). Read for CRA current disposition workflow, regional offices, online submission, fax and cheque payment. Read 2026-11-14.
- [C09] [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html). Read for T4037(2025): capital versus income, gain expenses and residence gate. Read 2026-11-14.
- [C10] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html). Read for ITA248(1): actual TCP and treaty-protected definitions. Read 2026-11-14.
- [C11] [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/uhtn1/introduction-underused-housing-tax.html). Read for CRA UHTN1: enacted2025+ non-application and2022–2024 retained duties. Read 2026-11-14.
- [C12] [Official source](https://laws-lois.justice.gc.ca/eng/acts/C-10.7/FullText.html). Read for Canadian enacted Canada–US Convention ArticleXIII(1), Canadian property example only. Read 2026-11-14.
- [C13] [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html). Read for T4058(2025): non-resident return routes and interim payments. Read 2026-11-14.
- [C14] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html). Read for ITA150(1),(5): annual deadlines and exact excluded-disposition test. Read 2026-11-14.
- [C15] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-1-individuals/folio-3-family-unit-issues/income-tax-folio-s1-f3-c2-principal-residence.html). Read for Principal residence Folio S1-F3-C2, especially2.15–2.23. Read 2026-11-14.
- [C16] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html). Read for ITA38(a): enacted ordinary1/2 inclusion. Read 2026-11-14.
- [C17] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-120.html). Read for ITA120: actual non-resident surtax base/allocation. Read 2026-11-14.
- [C18] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html). Read for ITA162(7): failure-to-comply penalty. Read 2026-11-14.
- [C19] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-227.html). Read for ITA227(9),(9.1),(9.2),(10.1): remittance penalties, interest and assessment. Read 2026-11-14.
- [C20] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html). Read for ITA40(2)(b): full principal residence formula includingD. Read 2026-11-14.
- [C21] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html). Read for ITA54: basis, capital property and principal residence definition. Read 2026-11-14.
- [C22] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html). Read for ITA110.6(5): part-year deemed-residence condition for capital gains deduction. Read 2026-11-14.
- [C24] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-13.html). Read for ITA13(1): recapture included in income. Read 2026-11-14.
- [C25] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html). Read for ITA220(3.1): discretionary relief boundary. Read 2026-11-14.
- [C32] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2062/t2062-21e.pdf). Read for Actual T2062 E(21),6pages, all operative fields/instructions; page5 visually inspected. Read 2026-11-14.
- [C33] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2062a/t2062a-21e.pdf). Read for Actual T2062A E(21),6pages, all operative fields/instructions; page5 visually inspected. Read 2026-11-14.
- [C34] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2062b/t2062b-16e.pdf). Read for Actual T2062B E(16),4pages, insurer/policyholder/payment instructions. Read 2026-11-14.
- [C35] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2062c/t2062c-18e.pdf). Read for Actual T2062C(18),3pages, purchaser notice fields; stale TCP explanation not followed. Read 2026-11-14.
- [C36] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1261/t1261-25e.pdf). Read for Actual T1261 E(25),3pages, eligibility/signature/certified copies/separate mailing; page1 visually inspected. Read 2026-11-14.
- [C38] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2091ind/t2091ind-25e.pdf). Read for Actual T2091(IND) E(25),4pages, designation and gain calculation. Read 2026-11-14.
- [C40] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-agreements-notices/failure-comply-penalty-non-resident-vendor-notification-on-disposition-taxable-canadian-property.html). Read for CRA vendor late-notification policy and subsection(5.2) exceptions. Read 2026-11-14.
- [C41] [Official source](https://www.budget.canada.ca/2026/report-rapport/nwmm-amvm-1-en.html). Read for Budget2026 NWMM, Taxable Canadian Property clauses1–2, proposal only after2026. Read 2026-11-14.
- [C42] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html). Read for ITA128.1(4)(b)(i),(c),(d): departure exceptions and elective disposition. Read 2026-11-14.
- [C43] [Official source](https://laws-lois.justice.gc.ca/eng/acts/U-0.5/FullText.html). Read for UHTAct1.1,6.1: enacted non-application overrides, not repeal of historical liabilities. Read 2026-11-14.

Not yet confirmed: final 2026 return-package fields and the exact annual credit field for these section 116 payments; actual blank T2064/T2068 certificate layouts; full T2062A/B Schedule 1 computations and a complete provincial-allocation engine. Obtain the actual document/rule when that job is required. The generic interim-credit principle, certificate function and source-specific handoffs above are supported, but these unconfirmed fields are not invented or treated as complete. No actual CRA case, certificate, account allocation, filing or payment has been made or independently verified for a real client.
