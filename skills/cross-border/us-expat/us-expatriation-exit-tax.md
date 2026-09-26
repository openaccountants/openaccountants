---
name: us-expatriation-exit-tax
description: "US expatriation tax for citizens renouncing and long-term green-card holders abandoning status: the covered-expatriate tests (IRC §877A/§877), the mark-to-market exit tax, the special rules for deferred compensation, tax-deferred accounts and non-grantor trust interests, the dual-citizen and minor exceptions, Form 8854, and the §2801 tax on US recipients of gifts from covered expatriates. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
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

# US expatriation and the exit tax (IRC §877A): 2026 method, with 2025 return notes

Figures are for 2026 unless a line says 2025. The 2026 amounts come from [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) (§4.37, §4.38 and §4.42), the inflation adjustments issued after the One Big Beautiful Bill Act (P.L. 119-21). The 2025 amounts come from [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) and the [2025 Instructions for Form 8854](https://www.irs.gov/instructions/i8854). A separate section covers people who expatriated in 2025. Their extended return deadline is December 15, 2026 if they were nonresident at the end of 2025 with no US wages subject to withholding, or October 15, 2026 otherwise.

## Scope and who this is for

- **Covers:** two groups who leave the US tax system on or after June 17, 2008:
  1. a **US citizen who relinquishes citizenship**; and
  2. a **long-term resident (LTR)**, meaning a green-card holder who meets the 8-of-15-years test below, who **stops being a lawful permanent resident** for tax purposes.
- It covers the covered-expatriate tests, the exceptions, the mark-to-market deemed sale, the special rules for deferred compensation, specified tax-deferred accounts and nongrantor trusts, the deferral election, Form 8854, and the §2801 tax on US people who receive gifts or bequests from a covered expatriate.
- **Does not cover:** people who expatriated before June 17, 2008 (the older §877 regime applies; see the [IRS expatriation tax page](https://www.irs.gov/individuals/international-taxpayers/expatriation-tax)); green-card holders who are **not** LTRs; the immigration or State Department steps.
- **State tax is separate.** This Guide gives the federal answer only. A state may tax the deemed sale or the deemed distributions differently, or may treat the person as still resident. Check the state's own rules before giving a combined figure.

## Ask the client first

- **Status.** Citizen or green-card holder? If a citizen: born a citizen, or naturalized? Citizen of which other countries, and since when (at birth or later)?
- **Expatriation date evidence.** For a citizen: date of the oath of renunciation, or of a signed statement of voluntary relinquishment, and whether the State Department has issued a Certificate of Loss of Nationality (CLN). For a green-card holder: date Form I-407 was filed, any final administrative or removal order, and any year a tax-treaty residence position was taken.
- **Green-card years.** The date the green card was issued, and every tax year the person held it. For each year: was a treaty "resident of the other country" position taken (Form 8833), and were treaty benefits waived?
- **Days in the US.** A year-by-year count of US residence (substantial presence test) for the last 15 years. This is needed for the dual-citizen and minor exceptions.
- **Age.** Date of birth, if the person is renouncing young.
- **Five-year tax record.** Copies of the Form 1040 returns for the 5 tax years before the expatriation year. Also every other federal obligation for those years: FBARs, Form 8938, Form 3520/3520-A, Form 5471/8865, gift tax returns, employment tax. Any year not filed or wrong breaks the certification test.
- **Balance sheet on the expatriation date.** Worldwide assets at fair market value and basis: property, shares, private companies, partnerships, trust interests, pensions, deferred compensation, options and RSUs, IRAs, 529/ABLE/Coverdell accounts, HSAs. Also liabilities, and any large gifts in the last 5 years.
- **Date first became a US resident**, and the value of assets held on that date (for the basis rule in §877A(h)(2)).
- **Family plans.** Will the person make gifts or leave bequests to US citizens or residents later? That triggers the §2801 questions.

## The method, step by step

Fix the expatriation date and covered status **before** planning any sale. The deemed sale happens on the day before the expatriation date, so it sets the basis for every later sale.

1. **Confirm the person is an "expatriate".** A citizen who relinquishes citizenship, or an LTR who stops being a lawful permanent resident ([§877A(g)(2)](https://www.law.cornell.edu/uscode/text/26/877A)). An ordinary green-card holder who is not an LTR is outside §877A.
2. **Fix the expatriation date.**
   - **Citizen:** the earliest of (a) the renunciation before a US diplomatic or consular officer, (b) the date a signed statement of voluntary relinquishment was given to the State Department, (c) the date the State Department issues a CLN, or (d) the date a US court cancels a naturalization certificate. Dates (a) and (b) count only if a CLN is later issued ([§877A(g)(4)](https://www.law.cornell.edu/uscode/text/26/877A)).
   - **LTR:** the earliest of (a) filing Form I-407 with a US consular or immigration officer, (b) a final administrative order of abandonment (or the final judicial order if appealed), (c) a final removal order, or (d) the date a dual resident starts to be treated as a resident of a treaty country, does not waive treaty benefits, **and** notifies the IRS ([Form 8854 instructions](https://www.irs.gov/instructions/i8854); [§7701(b)(6)](https://www.law.cornell.edu/uscode/text/26/7701)).
3. **For a green-card holder, test LTR status.** LTR means a lawful permanent resident in **at least 8** tax years during the 15 tax years ending with the tax year of expatriation. **Do not count** a year in which the person was treated as a resident of a foreign country under a tax treaty **and** did not waive the treaty benefits ([§877(e)(2)](https://www.law.cornell.edu/uscode/text/26/877)). The statute counts tax years, not elapsed time. If the answer turns on a partial first or last year, refer.
4. **Run the three covered-expatriate tests.** Any one of them makes the person covered ([§877(a)(2)](https://www.law.cornell.edu/uscode/text/26/877); [§877A(g)(1)(A)](https://www.law.cornell.edu/uscode/text/26/877A)):
   - **Tax liability test:** average annual net income tax for the **5 tax years ending before the expatriation date** is **more than** the indexed amount for the year of expatriation. On Form 8854 each year's figure is total tax less any foreign tax credit.
   - **Net worth test:** net worth of **$2 million or more** on the expatriation date. This amount is fixed by statute and is not indexed.
   - **Certification test:** the person fails to certify on Form 8854, under penalties of perjury, that they met **all** federal tax obligations for the 5 tax years before expatriation, or fails to give evidence of compliance if the IRS asks.
5. **Apply the exceptions, but only to the first two tests.** The dual-citizen and minor exceptions switch off the tax liability and net worth tests only. The certification test still applies, so the person must still file Form 8854 and certify ([§877A(g)(1)(B)](https://www.law.cornell.edu/uscode/text/26/877A); [Form 8854 instructions](https://www.irs.gov/instructions/i8854)). See the table below for the exact conditions.
6. **If not covered:** there is no exit tax. The person still files Form 8854 for the year of expatriation. Stop here, apart from the filing steps.
7. **If covered, sort the assets into four groups.**
   - **Ordinary property:** marked to market.
   - **Deferred compensation items:** eligible or ineligible.
   - **Specified tax-deferred accounts.**
   - **Interests in nongrantor trusts.**

   The last three are **not** marked to market ([§877A(c)](https://www.law.cornell.edu/uscode/text/26/877A)).
8. **Mark ordinary property to market.** Treat all property as sold at fair market value on the day before the expatriation date ([§877A(a)(1)](https://www.law.cornell.edu/uscode/text/26/877A)). Work out each asset's gain or loss.
   - Gains are taken into account in full.
   - Losses count only as far as the Code otherwise allows (for example, the capital loss limit). The wash-sale rule of §1091 does **not** apply to these losses ([§877A(a)(2)](https://www.law.cornell.edu/uscode/text/26/877A)).
   - Basis rule: property held on the day the person first became a US resident is treated as having a basis of at least its fair market value on that day, unless the person elects out. The election is irrevocable ([§877A(h)(2)](https://www.law.cornell.edu/uscode/text/26/877A)). Form 8854 lets a naturalized citizen or an LTR make it by writing "(h)(2)" next to the entry.
9. **Apply the exclusion amount.** Reduce the net gain, but not below zero, by the exclusion for the year of expatriation. Allocate the exclusion to each **gain** asset in proportion to its gain. No asset can take more exclusion than its own gain. If total gain is below the exclusion, the exclusion is limited to the total gain ([Form 8854 instructions, Section C, column (e)](https://www.irs.gov/instructions/i8854)).
10. **Tax the recognized gain at normal rates.** Each deemed sale is reported as if the asset had actually been sold: Form 8949 for shares or a home, Form 4797 for depreciated business property. Capital gain stays capital gain, and ordinary gain stays ordinary ([Form 8854 instructions](https://www.irs.gov/instructions/i8854)). Use the `us-capital-gains` Guide for the rates.
11. **Run the special regimes** (see the table below):
    - **Eligible deferred compensation:** 30% withholding on later payments.
    - **Ineligible deferred compensation:** present value taxed now.
    - **Specified tax-deferred accounts:** the whole balance is taxed now.
    - **Nongrantor trusts:** 30% withholding on later distributions.
12. **Decide on the deferral election, asset by asset** (§877A(b); see the table below).
13. **File.** File Form 8854 with the return for the year that includes the expatriation date. For a covered expatriate that return is usually a dual-status return. See Filing and payment below.
14. **Flag §2801** for any future gift or bequest to a US citizen or resident.

## Figures by year

| Figure | 2026 | 2025 | Source |
| --- | --- | --- | --- |
| Tax liability test: average annual net income tax must be **more than** | $211,000 | $206,000 | [Rev. Proc. 2025-32 §4.37](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Rev. Proc. 2024-40 §2.37](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| Exclusion from the mark-to-market gain | $910,000 | $890,000 | [Rev. Proc. 2025-32 §4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Rev. Proc. 2024-40 §2.38](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| Net worth test: **$2 million or more** (not indexed) | $2,000,000 | $2,000,000 | [§877(a)(2)(B)](https://www.law.cornell.edu/uscode/text/26/877) |
| §2801 tax applies only to covered gifts and bequests received in the year **above** | $19,000 | $19,000 | [Rev. Proc. 2025-32 §4.42(3)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Rev. Proc. 2024-40 §2.43](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) with [§2801(c)](https://www.law.cornell.edu/uscode/text/26/2801) |
| §2801 tax rate (the highest estate and gift tax rate) | 40% | 40% | [Form 708 instructions](https://www.irs.gov/pub/irs-pdf/i708.pdf); [§2001(c)](https://www.law.cornell.edu/uscode/text/26/2001) |
| Withholding on eligible deferred compensation and nongrantor trust distributions | 30% | 30% | [§877A(d)(1), (f)(1)](https://www.law.cornell.edu/uscode/text/26/877A) |
| Penalty for failing to file Form 8854, or for filing it incomplete or wrong (per year) | $10,000 | $10,000 | [§6039G(c)](https://www.law.cornell.edu/uscode/text/26/6039G) |

Use the figures for the calendar year of the expatriation date. Earlier years' tax-liability amounts are listed on the [IRS expatriation tax page](https://www.irs.gov/individuals/international-taxpayers/expatriation-tax). The 2026 Form 8854 instructions were not yet published when this was written. The 2026 amounts above come from Rev. Proc. 2025-32.

## Boundaries and exceptions

| Rule | Exact condition | What goes wrong |
| --- | --- | --- |
| **Dual citizen at birth** ([§877A(g)(1)(B)(i)](https://www.law.cornell.edu/uscode/text/26/877A)) | **All** of these: (1) became a US citizen **and** a citizen of another country **at birth**; (2) on the expatriation date, is still a citizen of **and taxed as a resident of** that same country; (3) was a US resident (substantial presence test) for **not more than 10** tax years in the 15-tax-year period **ending with** the year of expatriation. | Naturalized citizens, and people who got the second citizenship after birth, do not qualify. Nor does someone who is a citizen but tax resident in a third country. 11 or more years of US residence fails. The certification test still applies. |
| **Minor** ([§877A(g)(1)(B)(ii)](https://www.law.cornell.edu/uscode/text/26/877A)) | Both: (1) the person relinquishes **citizenship** before reaching **age 18½**; and (2) was a US resident (substantial presence test) for **not more than 10** tax years **before** relinquishment. | Citizens only; an LTR cannot use it. The date that matters is the relinquishment date under §877A(g)(4), not the date the CLN arrives, but a CLN must follow. The certification test still applies. |
| **LTR year count** ([§877(e)(2)](https://www.law.cornell.edu/uscode/text/26/877)) | At least 8 tax years as a lawful permanent resident in the 15 tax years ending with the year of expatriation. A year does not count if the person was a treaty resident of another country and did not waive the treaty benefits. | 7 years is not LTR. Separately, a treaty-residence position taken **with notice to the IRS** can itself end LPR status and create the expatriation date ([§7701(b)(6)](https://www.law.cornell.edu/uscode/text/26/7701)). Test that before filing any treaty tie-breaker claim. |
| **Tax liability test** | **More than** the indexed amount. Equal to it is not enough. | Using the wrong year's amount, or using a figure before the foreign tax credit instead of after. |
| **Net worth test** ([Form 8854 instructions, Section B](https://www.irs.gov/instructions/i8854)) | **$2 million or more** on the expatriation date: exactly $2,000,000 is covered. Values follow the gift tax rules (§2512). The person is treated as owning any interest that would be a taxable gift if transferred just before expatriation, including trust interests. Good-faith estimates are allowed; formal appraisals are not required. | Leaving out pensions, deferred compensation, unvested equity or trust interests. If net worth was $2 million or more at any time in the 5 prior years but lower on the date, Form 8854 Part II line 3 needs a statement explaining the change. |
| **Certification** ([Form 8854 instructions, line 7](https://www.irs.gov/instructions/i8854)) | Compliance for the 5 tax years before expatriation: income tax, employment tax, gift tax and information returns, and payment of all tax, interest and penalties. | Missing FBAR, Form 8938 or Form 3520 filings, or an unfiled return. Failing certification makes the person covered whatever their wealth or income, and it overrides both exceptions. |
| **Relief Procedures for Certain Former Citizens** ([IRS page](https://www.irs.gov/individuals/international-taxpayers/relief-procedures-for-certain-former-citizens)) | **All** of these must be met: (1) the person has **already relinquished** US citizenship, after March 18, 2010; (2) **no filing history** as a US citizen or resident; (3) average annual net income tax for the 5 years before expatriation did **not exceed** the §877(a)(2)(A) threshold; (4) net worth under $2 million both at expatriation and when they make the submission; (5) aggregate tax liability of $25,000 or less for the 5 years before expatriation and the year of expatriation; (6) all required federal returns for the 6 tax years at issue are filed with the submission; (7) the failures were non-willful. | Not available to LTRs, to anyone who has ever filed as a US citizen or resident, to anyone who has not yet relinquished, to anyone at $2 million or more, or where the conduct was willful. Read the IRS FAQs for the filing package before relying on it. |
| **§1091 wash sales** | Do **not** apply to losses from the deemed sale ([§877A(a)(2)(B)](https://www.law.cornell.edu/uscode/text/26/877A)). Other loss limits, such as §1211(b), still apply. | Deferring a deemed-sale loss because replacement shares were bought within 30 days. The loss is taken into account in the expatriation year, subject to the other limits. |
| **Pending deferral windows** ([§877A(h)(1)](https://www.law.cornell.edu/uscode/text/26/877A)) | For a covered expatriate, any open period to buy replacement property that would reduce gain (for example, a like-kind exchange window) ends on the day before the expatriation date. Any existing extension of time to pay tax also ends then. | Assuming a §1031 exchange started before expatriation can be finished afterwards. |
| **Deferred compensation items** (qualified plans, 401(k), SEP and SIMPLE plans, foreign pensions, nonqualified deferred compensation, unvested §83 property; [§877A(d)](https://www.law.cornell.edu/uscode/text/26/877A); [Form 8854 instructions, line 1a](https://www.irs.gov/instructions/i8854)) | **Eligible only if all three hold:** (1) the payer is a US person, or a non-US payer that elects to be treated as one; (2) the person notifies the payer on **Form W-8CE**, by the earlier of the day before the first distribution after the expatriation date or 30 days after the expatriation date; (3) the person irrevocably waives any treaty reduction in withholding, on Form 8854. Result: the payer withholds 30% of each taxable payment, and there is no tax up front. | If any condition fails, the item is **ineligible**. The present value of the accrued benefit is then treated as received on the day before the expatriation date. For §83 property, the rights are treated as vested and transferable on that day. No early distribution tax applies. The rules do not reach the part of an item earned for services performed outside the US while the person was neither a citizen nor a resident. |
| **Specified tax-deferred accounts** ([§877A(e)](https://www.law.cornell.edu/uscode/text/26/877A)) | IRAs (other than SEP and SIMPLE IRAs), 529 plans, ABLE accounts, Coverdell ESAs, HSAs and Archer MSAs. The **entire** balance is treated as distributed on the day before the expatriation date. No early distribution tax applies (the additional taxes listed in §877A(g)(6), such as §72(t)). Later distributions are adjusted so the same amount is not taxed twice. | Folding these amounts into the mark-to-market pool, where the exclusion would wrongly shelter them. |
| **Nongrantor trusts** ([§877A(f)](https://www.law.cornell.edu/uscode/text/26/877A); [Form 8854 instructions, line 1d](https://www.irs.gov/instructions/i8854)) | Applies only if the person was a beneficiary on the day before the expatriation date. Grantor or nongrantor status is tested immediately before expatriation. The trustee withholds 30% of the taxable portion of each direct or indirect distribution, and the person is treated as having waived treaty reductions. If the trust distributes appreciated property, the trust recognizes gain as if it had sold the property. **Alternative:** elect to be treated as receiving the value of the whole interest on the day before expatriation. This needs an IRS valuation letter ruling, attached to Form 8854 and to the timely filed return. | A **grantor** trust portion is not a nongrantor trust. Its assets are marked to market as the person's own property. Get the classification right first (see the `us-foreign-trust-reporting` Guide). |
| **Deferral election** ([§877A(b)](https://www.law.cornell.edu/uscode/text/26/877A); [Form 8854 instructions, Section D](https://www.irs.gov/instructions/i8854)) | Made **property by property**, and irrevocable. Needs **adequate security**: a bond accepted by the IRS that meets §6325, or other security the IRS accepts, such as a letter of credit. Also needs an irrevocable **waiver of treaty rights** that would block assessment or collection, a tax deferral agreement, and a **US agent**. Interest runs at the underpayment rate from the return due date (without extensions) for the expatriation year ([Notice 2009-85 §3E](https://www.irs.gov/pub/irs-drop/n-09-85.pdf)). | Tax on an asset falls due with the return for the year it is sold. It can never run past the due date of the return for the year of death, or past the time the security stops being adequate (after the correction period the IRS allows). Form 8854 must be filed **every year** until the deferred tax and interest are paid. |
| **§877A(g)(1)(C)** | If a covered expatriate later becomes taxable again as a US citizen or resident, they are not treated as covered during that period for the 30% withholding rules and §2801. | Continuing to withhold 30% on a returning resident. |

## §2801: tax on US recipients of gifts and bequests from a covered expatriate

- **Who pays:** the **US citizen or resident who receives** the covered gift or bequest, not the expatriate ([§2801(a)-(b)](https://www.law.cornell.edu/uscode/text/26/2801)). A domestic trust that receives one is treated as a US citizen and pays the tax itself. For a foreign trust, the tax falls on distributions to US recipients that come from covered gifts, unless the trust elects to be treated as domestic.
- **What is covered:** property acquired directly or indirectly by gift from a person who is a covered expatriate at the time, or because of the death of someone who was a covered expatriate immediately before death. This applies for as long as the donor stays a covered expatriate; the regime does not expire.
- **What is not covered** ([§2801(e)(2)-(3)](https://www.law.cornell.edu/uscode/text/26/2801)):
  - a taxable gift shown on a **timely filed US gift tax return** of the expatriate;
  - property included in the expatriate's gross estate and shown on a **timely filed US estate tax return**;
  - transfers that would qualify for the marital or charitable deduction if the donor were a US person.
- **Amount:** 40% × (covered gifts and bequests received in the calendar year − the §2801(c) amount). The §2801(c) amount is the annual gift exclusion for that year: $19,000 for 2026. The tax is reduced by any **foreign gift or estate tax** paid on the same transfer ([§2801(d)](https://www.law.cornell.edu/uscode/text/26/2801)).
- **Presumption:** a living donor who may have expatriated and who does not authorize the IRS to disclose their return information to the recipient is treated as a covered expatriate for §2801, unless the recipient can show otherwise ([Form 708 instructions](https://www.irs.gov/pub/irs-pdf/i708.pdf); [Form 8854 instructions](https://www.irs.gov/instructions/i8854)).
- **Return:** Form 708. The final regulations apply to covered gifts and bequests **received on or after January 1, 2025** ([IRS What's new, estate and gift tax](https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax)).
  - **Due date:** the 15th day of the 18th month after the end of the calendar year of receipt ([26 CFR 28.6071-1](https://www.law.cornell.edu/cfr/text/26/28.6071-1)). So 2025 receipts are due June 15, 2027, and 2026 receipts are due June 15, 2028.
  - **Bequests received after the date of death:** a later date may apply.
  - **Extension:** Form 7004 gives an automatic 6-month extension to file, but not to pay.
  - **Protective return:** a recipient who reasonably concludes that a gift is not covered may file a protective Form 708 to start the limitations period.

## Worked cases

All amounts are hypothetical unless a source is named.

### Case 1: 2026 covered expatriate, allocating the exclusion ([Rev. Proc. 2025-32 §4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Form 8854 instructions](https://www.irs.gov/instructions/i8854))

A naturalized citizen renounces in 2026, and the CLN is later issued. Net worth is $3,500,000, so the person is covered under the net worth test. On the day before the expatriation date:

- Asset A has a gain of $1,200,000.
- Asset B has a gain of $300,000.

The total gain is $1,500,000.

The 2026 exclusion of $910,000 is split in proportion to each asset's gain:

- **Asset A** takes $728,000 (910,000 × 1,200,000 ÷ 1,500,000) and recognizes $472,000.
- **Asset B** takes $182,000 (910,000 × 300,000 ÷ 1,500,000) and recognizes $118,000.

The total recognized gain is $590,000, which is 1,500,000 − 910,000. Report each asset on Form 8949 or Form 4797 as if it had been sold, keeping its character.

### Case 2: dual citizen at birth ([§877A(g)(1)(B)(i)](https://www.law.cornell.edu/uscode/text/26/877A))

Born in the US to French parents, the person was a US and French citizen at birth. They lived in the US for 9 of the 15 tax years ending with 2026, and are a French citizen and French tax resident on the expatriation date. Net worth is $3,000,000. They certify 5 compliant years on Form 8854.

- **Result: not covered.** The exception switches off the net worth test.
- **Variant 1:** with 11 years of US residence, the exception fails and the person is covered.
- **Variant 2:** if the person lives and is taxed in Switzerland, not France, the exception also fails.
- **Variant 3:** if one year of FBARs is missing, the certification fails and the person is covered despite the exception.

### Case 3: 2026 LTR count ([§877(e)(2)](https://www.law.cornell.edu/uscode/text/26/877))

A green card was issued in 2017 and held for the whole of every tax year from 2018 to 2025. Form I-407 was filed in May 2026. The person took no treaty-residence position.

- **Result: LTR.** The full years 2018 to 2025 alone are 8 tax years, so the answer does not depend on how the partial years 2017 and 2026 count. The I-407 filing date is the expatriation date.
- **Variant 1:** a card issued in March 2019, with an I-407 filed in May 2026. The full years 2020 to 2025 are only 6. Reaching 8 needs both partial years, 2019 and 2026, to count. **Refer** this one; do not give a definite answer.
- **Variant 2:** the first facts, but a treaty-resident position (without waiver) taken for 2022. 2022 drops out, leaving 7 full years, so the answer again turns on the partial years. Also check whether that treaty position, if notified to the IRS, already ended LPR status in 2022 (§7701(b)(6)). **Refer.**

### Case 4: certification failure with low wealth ([Form 8854 instructions](https://www.irs.gov/instructions/i8854); [Relief Procedures](https://www.irs.gov/individuals/international-taxpayers/relief-procedures-for-certain-former-citizens))

A citizen living abroad renounces in 2026. Net worth is $400,000, and the average net income tax is far below $211,000. Two of the last 5 years' returns and FBARs were never filed.

- **Result: covered, under the certification test,** unless the gaps are fixed. Consequences include the deemed IRA distribution and permanent §2801 exposure for US heirs.
- **Relief Procedures: not available.** The person filed 3 of the 5 returns, so they have a filing history as a US citizen. The procedures also apply only after citizenship has been relinquished.
- **Route:** file the missing returns and FBARs so that all 5 years are compliant, then certify on Form 8854. Refer the catch-up filing to a professional.

### Case 5: IRA and 401(k) of a covered expatriate ([§877A(d)-(e)](https://www.law.cornell.edu/uscode/text/26/877A))

A covered expatriate has a traditional IRA of $300,000 (all pre-tax) and a US employer's 401(k).

- **IRA:** the whole $300,000 is treated as distributed on the day before the expatriation date. It is ordinary income on the pre-expatriation part of the return, with no early distribution tax.
- **401(k):** this is a deferred compensation item. If the person gives the plan Form W-8CE on time and waives treaty reductions on Form 8854, it is eligible. The plan then withholds 30% of each later taxable payment, and nothing is taxed up front.
- **If the W-8CE or waiver is missing:** the item is ineligible, and its present value is taxed now.

### Case 6: §2801 on a 2026 gift ([§2801](https://www.law.cornell.edu/uscode/text/26/2801); [Form 708 instructions](https://www.irs.gov/pub/irs-pdf/i708.pdf))

In 2026 a covered expatriate, now a nonresident, gives $500,000 of foreign shares to a US-citizen child. No US gift tax return is required or filed for the gift, and no foreign gift tax is paid.

- The child owes 40% × ($500,000 − $19,000) = 40% × $481,000 = **$192,400**.
- It is reported on Form 708, due June 15, 2028.
- If the parent had timely reported the gift on a US gift tax return as a taxable gift, it would not be a covered gift.

### Case 7: the 2025 versus 2026 threshold ([Rev. Proc. 2024-40 §2.37](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf); [Rev. Proc. 2025-32 §4.37](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf))

A person's average annual net income tax for the 5 prior years is $208,000, and their net worth is $1,900,000.

- If they expatriated in 2025, the average is more than $206,000, so they are **covered**.
- If they expatriate in 2026, it is not more than $211,000, and net worth is under $2 million. If they certify, they are **not covered**.
- If net worth were exactly $2,000,000 on the date, they would be covered in either year, because the test is "or more".

## 2025 returns: people who expatriated in 2025 (extended deadline December 15 or October 15, 2026)

- **Thresholds for 2025:** the tax liability test is more than $206,000, and the exclusion is $890,000 ([2025 Form 8854 instructions](https://www.irs.gov/instructions/i8854); [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf)).
- **Form 8854:** the initial statement (Parts I and II) is attached to the 2025 return and filed by that return's due date, including extensions. Someone with no return to file sends Form 8854 alone to the IRS in Austin by the date the return would have been due. Which date applies depends on the return ([Pub. 519](https://www.irs.gov/publications/p519)):
  - **Nonresident alien on December 31, 2025 (the usual case, filing a dual-status Form 1040-NR), with no US wages subject to withholding:** due **June 15, 2026**. Form 4868 extends it to **December 15, 2026**.
  - **With US wages subject to withholding, or a resident at the end of 2025:** due **April 15, 2026**. Form 4868 extends it to **October 15, 2026**.
  - Form 8854 follows the due date of that return, including extensions. An extension covers filing, not payment ([IRS extension page](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)).
- **§2801:** covered gifts and bequests received in 2025 above $19,000 go on a Form 708 due **June 15, 2027**.

## When to refuse or refer

Refer to a qualified US tax professional, and do not give a final answer, when:

- **the expatriation date is unclear.** Examples: an old expatriating act with no CLN, an I-407 that was not accepted, or an order under appeal.
- **the LTR count turns on a partial year, or on a treaty-residence position.** In particular, refer where a treaty claim may already have ended LPR status.
- **net worth is near $2 million ([Form 8854 instructions](https://www.irs.gov/instructions/i8854)), or contains assets that are hard to value.** Examples: private companies, partnership interests, trust interests (Notice 97-19 method), foreign pensions, or unvested equity.
- **the 5-year record has gaps**, so certification cannot yet be signed. Also refer if the person is weighing the Relief Procedures or other compliance programs.
- **a trust is involved.** That includes grantor versus nongrantor classification, the §684 interaction ([§877A(h)(3)](https://www.law.cornell.edu/uscode/text/26/877A)), and the valuation-ruling election.
- **the person wants the deferral election.** It needs security, a tax deferral agreement and a US agent.
- **a foreign pension or foreign deferred compensation is involved**, including the treaty questions and the services-abroad carve-out.
- **the tax liability average is within a few thousand dollars of the threshold.**
- **the person is a US recipient of a gift or bequest from someone who may be a covered expatriate**, including gifts through foreign trusts.
- **state residency or state tax on the deemed sale matters.**
- **the person expatriated before June 17, 2008**, or never filed Form 8854 after an earlier expatriation.

Do not state that a person is "not covered" until a signed Form 8854 certification of 5 compliant years is in hand.

## Filing and payment

- **Initial Form 8854** (Parts I and II): attach it to the income tax return for the year that includes the expatriation date, and file by that return's due date. If no return is required, send it separately to Internal Revenue Service, 3651 S IH35, MS 4301 AUSC, Austin, TX 78741 by the date the return would have been due, including extensions ([Form 8854 instructions](https://www.irs.gov/instructions/i8854)). Every expatriate files it, covered or not.
- **Return type in the year of expatriation:** a covered expatriate who was a citizen or LTR for only part of the year files a **dual-status return**: Form 1040-NR with a Form 1040 attached as a schedule. The deemed sale, the ineligible deferred compensation and the specified tax-deferred accounts go on the Form 1040 part. For a covered expatriate, an expatriation date of January 1 means no dual-status return ([Notice 2009-85 §8](https://www.irs.gov/pub/irs-drop/n-09-85.pdf)). [Pub. 519](https://www.irs.gov/publications/p519) has the general dual-status rules.
- **Annual Form 8854** (Parts I and III): file every year after the expatriation year while the person has deferred tax outstanding, an eligible deferred compensation item, or an interest in a nongrantor trust. Attach it to Form 1040-NR if one is filed, and send a copy marked "Copy" to Austin. Otherwise send it alone by the date the return would have been due.
- **Penalty:** $10,000 for each year Form 8854 is not filed, or is filed incomplete or wrong, unless the failure is due to reasonable cause and not willful neglect ([§6039G(c)](https://www.law.cornell.edu/uscode/text/26/6039G)).
- **Payment:** mark-to-market tax is due with the return for the expatriation year, unless it has been deferred under an accepted tax deferral agreement. Deferred tax plus interest on an asset sold in a later year is due by that year's return due date, without extensions.
- **Form W-8CE:** give it to each payer of a deferred compensation item, each specified-account custodian, and each nongrantor trust trustee. File it by the earlier of the day before the first distribution after expatriation or 30 days after the expatriation date ([Form W-8CE](https://www.irs.gov/forms-pubs/about-form-w-8-ce)).
- **FBAR and Form 8938:** these may still be required for the part of the expatriation year in which the person was a US person.
- **Form 708:** filed by the US recipient under §2801 (see the dates above).

## Completion checklist ([Form 8854 instructions](https://www.irs.gov/instructions/i8854); [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf))

- [ ] Expatriate type confirmed: citizen, or LTR with at least 8 of 15 tax years after removing treaty years.
- [ ] Expatriation date fixed from the earliest qualifying event, with a CLN in hand for a citizen.
- [ ] Tax liability test run against the correct year's amount: 2026 more than $211,000, 2025 more than $206,000. Tax is net of the foreign tax credit, for the 5 years before the expatriation date.
- [ ] Net worth balance sheet at FMV (Form 8854 Section B), including pensions, deferred compensation, equity, trust interests and gifts. Tested against $2 million or more.
- [ ] Five-year compliance checked across income, employment, gift and information returns, including FBARs. Certification ready to sign, or a route to compliance chosen.
- [ ] Dual-citizen or minor exception tested against every condition, and used only against the first two tests.
- [ ] If covered: assets split into ordinary property, deferred compensation (eligible or ineligible), specified tax-deferred accounts and nongrantor trusts.
- [ ] Mark-to-market gains and losses computed, with the §877A(h)(2) basis rule considered, §1091 not applied, and the exclusion allocated asset by asset: 2026 $910,000, 2025 $890,000.
- [ ] Deemed distributions included with no early distribution tax. W-8CE sent and treaty waivers made where eligibility is wanted.
- [ ] Deferral election decided asset by asset, with security, waiver, US agent and agreement in place if used.
- [ ] Dual-status return prepared. Initial Form 8854 filed on time, and annual Form 8854 obligations diarised.
- [ ] Any open §1031 or other replacement window, or any existing payment extension, treated as ending on the day before the expatriation date.
- [ ] §2801 exposure explained for future gifts and bequests to US persons. Any donor disclosure authorization considered.
- [ ] State tax treatment checked separately.

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
