---
name: us-expatriation-exit-tax
description: US expatriation tax for citizens who renounce and long-term green-card holders who give up status, tax year 2026. Covers the covered expatriate tests of sections 877 and 877A (tax liability more than USD 211,000, net worth USD 2,000,000 or more, five-year certification), the dual-citizen and minor exceptions, the mark-to-market deemed sale with the 2026 exclusion of USD 910,000 (Rev. Proc. 2025-32), deferred compensation, specified tax-deferred accounts and nongrantor trust interests, the deferral election, Form 8854 and its USD 10,000 penalty, and the section 2801 tax of 40% on US recipients of gifts and bequests from covered expatriates above USD 19,000 (Form 708). Trigger on "renounce citizenship", "exit tax", "expatriation tax", "Form 8854", "covered expatriate", "give up green card", "long-term resident", "section 877A", "Form 708", "section 2801". Produces a working paper and a reviewer brief, not a filed return. Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
depends_on:
  - cross-border-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US expatriation and the exit tax (section 877A), tax year 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-32 (sections 4.37, 4.38 and 4.42), the 2025 Instructions for Form 8854, Form 8854, Form W-8CE, the Instructions for Form 708 (December 2025), Notice 2009-85, the IRS expatriation tax and Relief Procedures pages and 26 U.S.C. 877, 877A, 2001, 2801, 6039G and 7701, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A US citizen who renounces, or a long-term resident who gives up a green card, in 2026 is a **covered expatriate** if any one of these is true: average annual net income tax for the 5 prior years is **more than USD 211,000**; net worth on the expatriation date is **USD 2,000,000 or more**; or they cannot certify 5 years of full federal tax compliance on Form 8854. A covered expatriate is treated as selling everything at fair market value on the day before the expatriation date; net gain above **USD 910,000** is taxed at normal rates. Every expatriate, covered or not, files Form 8854; not filing costs USD 10,000. US people who later receive gifts or bequests from a covered expatriate pay **40%** on the amount above USD 19,000 a year.

## Scope and who this is for

In scope: two groups who leave the US tax system on or after 17 June 2008, with an expatriation date in 2026 (a section at the end covers 2025 expatriates still filing):

1. a **US citizen who relinquishes citizenship**; and
2. a **long-term resident (LTR)**, a green-card holder who meets the 8-of-15-years test below, who **stops being a lawful permanent resident** for tax purposes.

It covers the covered expatriate tests, the exceptions, the mark-to-market deemed sale, the special rules for deferred compensation, specified tax-deferred accounts and nongrantor trusts, the deferral election, Form 8854, and the section 2801 tax on US people who receive gifts or bequests from a covered expatriate.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| People who expatriated before 17 June 2008 (older section 877 regime) | refer; see the [IRS expatriation tax page](https://www.irs.gov/individuals/international-taxpayers/expatriation-tax) |
| Green-card holders who are not LTRs, and residency starting and ending dates | `us-tax-residency` |
| Capital gains rates on the recognized gain | `us-capital-gains` |
| The dual-status Form 1040-NR itself | `us-form-1040-nr-nonresident-return` |
| Practical tax of living abroad before or without renouncing | `us-citizen-moving-abroad-tax` |
| FBAR and Form 8938 for the part year as a US person | `us-fbar-and-fatca-8938` |
| Foreign trusts: grantor or nongrantor, Forms 3520 and 3520-A | `us-foreign-trust-reporting` |
| US gift and estate tax returns (Forms 706 and 709) | `us-estate-gift-706-709` |
| State tax on the deemed sale or deemed distributions | the state's income tax skill; a state may treat the person as still resident |
| Immigration and State Department steps | outside tax; refer |

## Ask the client first

1. **Status.** Citizen or green-card holder? If a citizen: born a citizen, or naturalized? Citizen of which other countries, and since when (at birth or later)?
2. **Expatriation date evidence.** For a citizen: date of the oath of renunciation, or of a signed statement of voluntary relinquishment, and whether the State Department has issued a Certificate of Loss of Nationality (CLN). For a green-card holder: date Form I-407 was filed, any final administrative or removal order, and any year a tax-treaty residence position was taken.
3. **Green-card years.** The date the green card was issued, and every tax year the person held it. For each year: was a treaty "resident of the other country" position taken (Form 8833), and were treaty benefits waived?
4. **Days in the US.** A year-by-year count of US residence (substantial presence test) for the last 15 years, needed for the dual-citizen and minor exceptions.
5. **Age.** Date of birth, if the person is renouncing young.
6. **Five-year tax record.** The Form 1040 returns for the 5 tax years before the expatriation year, and every other federal obligation for those years: FBARs, Form 8938, Forms 3520 and 3520-A, Forms 5471 and 8865, gift tax returns, employment tax. Any year not filed or wrong breaks the certification test.
7. **Balance sheet on the expatriation date.** Worldwide assets at fair market value and basis: property, shares, private companies, partnerships, trust interests, pensions, deferred compensation, options and RSUs, IRAs, 529, ABLE and Coverdell accounts, HSAs. Also liabilities, and any large gifts in the last 5 years.
8. **Date first became a US resident**, and the value of assets held on that date (for the basis rule in section 877A(h)(2)).
9. **Family plans.** Will the person make gifts or leave bequests to US citizens or residents later? That triggers section 2801.

## The method, step by step

Fix the expatriation date and covered status **before** planning any sale. The deemed sale happens on the day before the expatriation date, so it sets the basis for every later sale.

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Tax liability test: average annual net income tax for the 5 years before the expatriation date must be more than | USD 211,000 | [Rev. Proc. 2025-32, section 4.37](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Exclusion from the mark-to-market gain (taxable years beginning in 2026) | USD 910,000 | [Rev. Proc. 2025-32, section 4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Net worth test (not indexed) | USD 2,000,000 or more | [26 U.S.C. 877(a)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877.htm) |
| LTR: lawful permanent resident in at least this many of the 15 tax years ending with the expatriation year | 8 | [26 U.S.C. 877(e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877.htm) |
| Dual-citizen and minor exceptions: US residence for not more than | 10 tax years | [26 U.S.C. 877A(g)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877A.htm) |
| Minor exception: relinquishment before age | 18½ | [26 U.S.C. 877A(g)(1)(B)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877A.htm) |
| Withholding on eligible deferred compensation and nongrantor trust distributions | 30% | [26 U.S.C. 877A(d)(1), (f)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877A.htm) |
| Penalty for not filing Form 8854, or filing it incomplete or wrong (per year) | USD 10,000 | [26 U.S.C. 6039G(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6039G.htm) |
| Section 2801 tax applies only to covered gifts and bequests received in calendar 2026 above | USD 19,000 | [Rev. Proc. 2025-32, section 4.42(3)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Section 2801 tax rate (highest rate in the section 2001(c) table) | 40% | [26 U.S.C. 2001(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partI-sec2001.htm); [Instructions for Form 708](https://www.irs.gov/pub/irs-pdf/i708.pdf) |

Use the figures for the calendar year of the expatriation date. Earlier years' tax liability amounts are listed on the [IRS expatriation tax page](https://www.irs.gov/individuals/international-taxpayers/expatriation-tax). The USD 211,000 and USD 910,000 are indexed each year; the USD 2,000,000 is fixed by statute.

### Is the person a covered expatriate

1. **Confirm the person is an "expatriate".** A citizen who relinquishes citizenship, or an LTR who stops being a lawful permanent resident ([26 U.S.C. 877A(g)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877A.htm)). An ordinary green-card holder who is not an LTR is outside section 877A.
2. **Fix the expatriation date.**
   - **Citizen:** the earliest of (a) the renunciation before a US diplomatic or consular officer, (b) the date a signed statement of voluntary relinquishment was given to the State Department, (c) the date the State Department issues a CLN, or (d) the date a US court cancels a naturalization certificate. Dates (a) and (b) count only if a CLN is later issued (877A(g)(4)).
   - **LTR:** the earliest of (a) filing Form I-407 with a US consular or immigration officer, (b) a final administrative order of abandonment (or the final judicial order if appealed), (c) a final removal order, or (d) the date a dual resident starts to be treated as a resident of a treaty country, does not waive treaty benefits, **and** notifies the IRS ([Instructions for Form 8854](https://www.irs.gov/pub/irs-pdf/i8854.pdf); [26 U.S.C. 7701(b)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm)).
3. **For a green-card holder, test LTR status.** At least 8 tax years as a lawful permanent resident during the 15 tax years ending with the expatriation year. **Do not count** a year in which the person was treated as a resident of a foreign country under a tax treaty **and** did not waive the treaty benefits (877(e)(2)). The statute counts tax years, not elapsed time. If the answer turns on a partial first or last year, refer.
4. **Run the three covered expatriate tests.** Any one makes the person covered ([26 U.S.C. 877(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877.htm); 877A(g)(1)(A)):
   - **Tax liability test:** average annual net income tax for the **5 tax years ending before the expatriation date** is **more than** USD 211,000 (2026). On Form 8854 each year's figure is total tax less any foreign tax credit.
   - **Net worth test:** net worth of **USD 2,000,000 or more** on the expatriation date.
   - **Certification test:** the person fails to certify on Form 8854, under penalties of perjury, that they met **all** federal tax obligations for the 5 tax years before expatriation, or fails to give evidence of compliance if the IRS asks.
5. **Apply the exceptions, but only to the first two tests.** The dual-citizen and minor exceptions switch off the tax liability and net worth tests only. The certification test still applies, so the person must still file Form 8854 and certify (877A(g)(1)(B)). See the boundary table for the exact conditions.
6. **If not covered:** there is no exit tax. The person still files Form 8854 for the year of expatriation. Stop here, apart from the filing steps.

### If covered: the exit tax

7. **Sort the assets into four groups:** ordinary property (marked to market); deferred compensation items (eligible or ineligible); specified tax-deferred accounts; interests in nongrantor trusts. The last three are **not** marked to market (877A(c)).
8. **Mark ordinary property to market.** Treat all property as sold at fair market value on the day before the expatriation date (877A(a)(1)) and work out each asset's gain or loss.
   - Gains are taken into account in full.
   - Losses count only as far as the Code otherwise allows (for example, the capital loss limit). The wash-sale rule of section 1091 does **not** apply (877A(a)(2)).
   - Basis rule: property held on the day the person first became a US resident is treated as having a basis of at least its fair market value on that day, unless the person elects out; the election is irrevocable (877A(h)(2)). On Form 8854 a naturalized citizen or an LTR uses it by writing "(h)(2)" next to the entry.
9. **Apply the exclusion.** Reduce the net gain, but not below zero, by USD 910,000 (2026). Allocate it to each **gain** asset in proportion to its gain: asset exclusion = 910,000 x asset gain / total gain of all gain assets. No asset takes more exclusion than its own gain; if total gain is below the exclusion, the exclusion is limited to the total gain ([Instructions for Form 8854, Section C](https://www.irs.gov/pub/irs-pdf/i8854.pdf)).
10. **Tax the recognized gain at normal rates.** Each deemed sale is reported as if the asset had actually been sold: Form 8949 for shares or a home, Form 4797 for depreciated business property. Capital gain stays capital, ordinary stays ordinary. Rates: `us-capital-gains`.
11. **Run the special regimes** (boundary table): eligible deferred compensation, 30% withholding on later payments; ineligible deferred compensation, present value taxed now; specified tax-deferred accounts, the whole balance taxed now; nongrantor trusts, 30% withholding on later distributions.
12. **Decide on the deferral election, asset by asset** (877A(b); boundary table).
13. **File** Form 8854 with the return for the year that includes the expatriation date (usually a dual-status return). See Filing and payment.
14. **Flag section 2801** for any future gift or bequest to a US citizen or resident.

### Section 2801: tax on US recipients of gifts and bequests from a covered expatriate

- **Who pays:** the **US citizen or resident who receives** the covered gift or bequest, not the expatriate ([26 U.S.C. 2801(a), (b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap15-sec2801.htm)). A domestic trust that receives one is treated as a US citizen and pays the tax itself. For a foreign trust, the tax falls on distributions to US recipients that come from covered gifts, unless the trust elects to be treated as domestic.
- **What is covered:** property acquired directly or indirectly by gift from a person who is a covered expatriate at the time, or because of the death of someone who was a covered expatriate immediately before death. This lasts as long as the donor stays a covered expatriate; it does not expire.
- **What is not covered** (2801(e)(2), (3)): a taxable gift shown on a **timely filed US gift tax return** of the expatriate; property included in the expatriate's gross estate and shown on a **timely filed US estate tax return**; transfers that would qualify for the marital or charitable deduction if the donor were a US person.
- **Amount:** 40% x (covered gifts and bequests received in the calendar year minus USD 19,000 for 2026). The tax is reduced by any **foreign gift or estate tax** paid on the same transfer (2801(d)).
- **Presumption:** a living donor who may have expatriated and who does not authorize the IRS to disclose their return information to the recipient is treated as a covered expatriate for section 2801, unless the recipient can show otherwise ([Instructions for Form 708](https://www.irs.gov/pub/irs-pdf/i708.pdf)).
- **Return:** Form 708, for covered gifts and bequests received on or after 1 January 2025. Due on the 15th day of the 18th month after the end of the calendar year of receipt, so 2026 receipts are due **15 June 2028** and 2025 receipts **15 June 2027**. A covered bequest received after the date of death may have a later date. Form 7004 gives an automatic 6-month extension to file, not to pay. A recipient who reasonably concludes a gift is not covered may file a protective Form 708 to start the limitations period ([Instructions for Form 708](https://www.irs.gov/pub/irs-pdf/i708.pdf)).

## Boundary and exception table

| Rule | Exact condition | What goes wrong |
| --- | --- | --- |
| **Dual citizen at birth** (877A(g)(1)(B)(i)) | **All** of: (1) became a US citizen **and** a citizen of another country **at birth**; (2) on the expatriation date, is still a citizen of **and taxed as a resident of** that same country; (3) was a US resident (substantial presence test) for **not more than 10** tax years in the 15-tax-year period **ending with** the expatriation year. | Naturalized citizens, and people who got the second citizenship after birth, do not qualify; nor does someone tax resident in a third country. 11 or more years fails. The certification test still applies. |
| **Minor** (877A(g)(1)(B)(ii)) | Both: (1) relinquishes **citizenship** before age **18½**; (2) was a US resident for **not more than 10** tax years **before** relinquishment. | Citizens only; an LTR cannot use it. The date that matters is the relinquishment date under 877A(g)(4), not the date the CLN arrives, but a CLN must follow. Certification still applies. |
| **LTR year count** (877(e)(2)) | At least 8 tax years as a lawful permanent resident in the 15 tax years ending with the expatriation year; a treaty-resident year without waiver does not count. | 7 years is not LTR. A treaty-residence position taken **with notice to the IRS** can itself end LPR status and create the expatriation date (7701(b)(6)); test that before filing any treaty tie-breaker claim. |
| **Tax liability test** | **More than** USD 211,000 (2026). Equal is not enough. | Using the wrong year's amount, or tax before the foreign tax credit instead of after. |
| **Net worth test** ([Instructions for Form 8854, Section B](https://www.irs.gov/pub/irs-pdf/i8854.pdf)) | **USD 2,000,000 or more** on the expatriation date: exactly USD 2,000,000 is covered. Values follow the gift tax rules (section 2512); the person is treated as owning any interest that would be a taxable gift if transferred just before expatriation, including trust interests. Good-faith estimates are allowed; formal appraisals are not required. | Leaving out pensions, deferred compensation, unvested equity or trust interests. If net worth was USD 2,000,000 or more at any time in the 5 prior years but lower on the date, Form 8854 Part II needs a statement explaining the change. |
| **Certification** ([Instructions for Form 8854](https://www.irs.gov/pub/irs-pdf/i8854.pdf)) | Compliance for the 5 tax years before expatriation: income, employment and gift tax and information returns, and payment of all tax, interest and penalties. | Missing FBAR, Form 8938 or Form 3520 filings, or an unfiled return. Failing makes the person covered whatever their wealth or income, and overrides both exceptions. |
| **Relief Procedures for Certain Former Citizens** ([IRS page](https://www.irs.gov/individuals/international-taxpayers/relief-procedures-for-certain-former-citizens)) | **All** of: (1) **already relinquished** US citizenship, after 18 March 2010; (2) **no filing history** as a US citizen or resident; (3) average annual net income tax for the 5 years before expatriation did **not exceed** the 877(a)(2)(A) threshold; (4) net worth under USD 2 million at expatriation and at submission; (5) aggregate tax liability of USD 25,000 or less for the 5 years before and the year of expatriation; (6) all required federal returns for the 6 years filed with the submission; (7) non-willful failures. | Not for LTRs, anyone who has ever filed as a US citizen or resident, anyone who has not yet relinquished, anyone at USD 2 million or more, or willful conduct. Read the IRS FAQs before relying on it. |
| **Section 1091 wash sales** | Do **not** apply to deemed-sale losses (877A(a)(2)); other limits such as 1211(b) still apply. | Deferring a loss because replacement shares were bought within 30 days. |
| **Pending deferral windows** (877A(h)(1)) | Any open period to buy replacement property that would reduce gain (for example a like-kind exchange window) ends on the day before the expatriation date, as does any existing extension of time to pay tax. | Assuming a section 1031 exchange started before expatriation can be finished afterwards. |
| **Deferred compensation items** (qualified plans, 401(k), SEP and SIMPLE plans, foreign pensions, nonqualified deferred compensation, unvested section 83 property; 877A(d)) | **Eligible only if all three hold:** (1) the payer is a US person, or a non-US payer that elects to be treated as one; (2) the person notifies the payer on **Form W-8CE** by the earlier of the day before the first distribution after the expatriation date or 30 days after the expatriation date; (3) the person irrevocably waives any treaty reduction in withholding, on Form 8854. The payer then withholds 30% of each taxable payment; no tax up front. | If any condition fails the item is **ineligible**: the present value of the accrued benefit is treated as received on the day before the expatriation date (section 83 property treated as vested). No early distribution tax. The rules do not reach the part earned for services outside the US while neither a citizen nor a resident. |
| **Specified tax-deferred accounts** (877A(e)) | IRAs (other than SEP and SIMPLE IRAs), 529 plans, ABLE accounts, Coverdell ESAs, HSAs and Archer MSAs. The **entire** balance is treated as distributed on the day before the expatriation date, with no early distribution tax (877A(g)(6)); later distributions are adjusted so the amount is not taxed twice. | Folding these into the mark-to-market pool, where the USD 910,000 would wrongly shelter them. |
| **Nongrantor trusts** (877A(f)) | Applies if the person was a beneficiary on the day before the expatriation date; status is tested immediately before expatriation. The trustee withholds 30% of the taxable portion of each distribution, treaty reductions waived; appreciated property distributed triggers gain in the trust. **Alternative:** elect to be treated as receiving the value of the whole interest on the day before expatriation, with an IRS valuation letter ruling attached to Form 8854 and the timely return. | A **grantor** trust portion is not a nongrantor trust; its assets are marked to market as the person's own. Classify first (`us-foreign-trust-reporting`). |
| **Deferral election** (877A(b); [Instructions for Form 8854, Section D](https://www.irs.gov/pub/irs-pdf/i8854.pdf)) | Property by property, irrevocable. Needs **adequate security** (a bond meeting section 6325, or other security the IRS accepts such as a letter of credit), an irrevocable **waiver of treaty rights** that would block assessment or collection, a tax deferral agreement and a **US agent**. Interest runs at the underpayment rate from the return due date (without extensions) for the expatriation year ([Notice 2009-85, section 3E](https://www.irs.gov/pub/irs-drop/n-09-85.pdf)). | Tax on an asset falls due with the return for the year it is sold, never later than the return due date for the year of death or when the security stops being adequate. Form 8854 must be filed **every year** until paid. |
| **877A(g)(1)(C)** | A covered expatriate who later becomes taxable again as a US citizen or resident is not treated as covered during that period for the 30% withholding rules and section 2801. | Continuing to withhold 30% on a returning resident. |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Signed 5-year certification | Treat as covered (certification test) until every year is shown compliant |
| CLN for a citizen | No expatriation date yet; plan on the earliest qualifying act but do not file as final |
| Treaty-residence history of a green-card holder | Count every year held; ask about Form 8833 before concluding |
| Value of a private company, trust interest or foreign pension | Good-faith estimate with method noted; refer if net worth is near USD 2,000,000 |
| Basis of assets held when the person first became resident | Use actual basis; offer the 877A(h)(2) step-up only once the arrival-date value is documented |
| Whether a W-8CE was sent on time | Treat the deferred compensation item as ineligible |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Net worth within about 10% of USD 2,000,000 | One valuation choice decides covered status |
| Average tax within a few thousand dollars of USD 211,000 | Wrong year's figure or a foreign tax credit error flips the result |
| Any missing FBAR, Form 8938 or Form 3520 in the 5 years | Covered under the certification test, whatever the wealth |
| A large IRA, 529 or HSA | Whole balance taxed as distributed, outside the exclusion |
| US children or heirs | Permanent 40% section 2801 exposure on future gifts and bequests |
| Treaty tie-breaker claims while holding a green card | May already have ended LPR status |

## Worked cases

All amounts are hypothetical; the thresholds are real.

**Case 1, a decision: does expatriating in 2026 instead of 2025 change covered status?** A person's average annual net income tax for the 5 prior years is USD 208,000, and their net worth is USD 1,900,000. If they expatriated in 2025, the average is USD 2,000 more than the 2025 threshold of USD 206,000, so they were **covered**. Expatriating in 2026, the average is not more than USD 211,000 (excess zero), and net worth is USD 100,000 short of USD 2,000,000. If they certify 5 compliant years, they are **not covered** in 2026. Had net worth been exactly USD 2,000,000 on the date, they would be covered in either year, because the test is "or more". Decision: on these facts a 2026 expatriation date avoids covered status; keep net worth below USD 2,000,000 on the date and fix any compliance gap first.

```oa-check
name: Covered expatriate tests, 2025 against 2026 thresholds
inputs:
  average_tax: 208000
  net_worth: 1900000
  threshold_2025: 206000
  threshold_2026: 211000
  net_worth_test: 2000000
steps:
  - excess_2025: max(average_tax - threshold_2025, 0)
  - excess_2026: max(average_tax - threshold_2026, 0)
  - net_worth_headroom: net_worth_test - net_worth
expected:
  excess_2025: 2000.00
  excess_2026: 0.00
  net_worth_headroom: 100000.00
```

**Case 2, allocating the 2026 exclusion.** A naturalized citizen renounces in 2026, and the CLN is later issued. Net worth is USD 3,500,000, so the person is covered. On the day before the expatriation date asset A has a gain of USD 1,200,000 and asset B a gain of USD 300,000: USD 1,500,000 in total. The USD 910,000 exclusion is split by gain: asset A takes 910,000 x 1,200,000 / 1,500,000 = USD 728,000 and recognizes USD 472,000; asset B takes USD 182,000 and recognizes USD 118,000. Total recognized gain is USD 590,000. Each asset goes on Form 8949 or Form 4797 as if sold, keeping its character.

```oa-check
name: Mark-to-market exclusion allocation (2026)
inputs:
  exclusion: 910000
  gain_a: 1200000
  gain_b: 300000
steps:
  - total_gain: gain_a + gain_b
  - exclusion_a: exclusion * gain_a / total_gain
  - exclusion_b: exclusion * gain_b / total_gain
  - recognized_a: gain_a - exclusion_a
  - recognized_b: gain_b - exclusion_b
  - total_recognized: max(total_gain - exclusion, 0)
expected:
  total_gain: 1500000.00
  exclusion_a: 728000.00
  exclusion_b: 182000.00
  recognized_a: 472000.00
  recognized_b: 118000.00
  total_recognized: 590000.00
```

**Case 3, dual citizen at birth.** Born in the US to French parents, the person was a US and French citizen at birth, lived in the US for 9 of the 15 tax years ending with 2026, and is a French citizen and French tax resident on the expatriation date. Net worth is USD 3,000,000. They certify 5 compliant years. **Not covered:** the exception switches off the net worth test. With 11 years of US residence the exception fails; if they live and are taxed in Switzerland, not France, it also fails; if one year of FBARs is missing, certification fails and they are covered despite the exception.

**Case 4, LTR count in 2026.** A green card was issued in 2017 and held for the whole of every tax year from 2018 to 2025; Form I-407 was filed in May 2026; no treaty position. **LTR:** the full years 2018 to 2025 alone are 8. Variant: a card issued in March 2019 with an I-407 in May 2026 gives only 6 full years, so 8 needs both partial years: **refer**. Variant: the first facts with a treaty-resident position (without waiver) for 2022 leaves 7 full years, and the treaty position may itself have ended LPR status in 2022 (7701(b)(6)): **refer**.

**Case 5, certification failure with low wealth.** A citizen abroad renounces in 2026 with net worth USD 400,000 and average tax far below USD 211,000, but 2 of the last 5 years' returns and FBARs were never filed. **Covered under the certification test** unless fixed, with the deemed IRA distribution and permanent section 2801 exposure for US heirs. The Relief Procedures are not available: the person has a filing history (3 of 5 returns) and they apply only after relinquishment. Route: file the missing years so all 5 are compliant, then certify; refer the catch-up.

**Case 6, IRA and 401(k) of a covered expatriate.** A traditional IRA of USD 300,000 (all pre-tax) is treated as distributed in full on the day before the expatriation date: ordinary income on the pre-expatriation part of the return, no early distribution tax. A US employer's 401(k) is a deferred compensation item: with Form W-8CE given on time and the treaty waiver on Form 8854 it is eligible, and the plan withholds 30% of each later payment. Without them it is ineligible and its present value is taxed now.

**Case 7, section 2801 on a 2026 gift.** A covered expatriate, now a nonresident, gives USD 500,000 of foreign shares to a US-citizen child in 2026. No US gift tax return is required or filed and no foreign gift tax is paid. The child owes 40% x (USD 500,000 minus USD 19,000) = 40% x USD 481,000 = USD 192,400, on Form 708 due 15 June 2028. Had the parent timely reported the gift as a taxable gift on a US gift tax return, it would not be a covered gift.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-EX-DATE | Expatriation date unclear: an old expatriating act with no CLN, an I-407 not accepted, an order under appeal | Refer; do not give a final answer |
| R-EX-LTR | LTR count turns on a partial year or a treaty-residence position, especially where a treaty claim may already have ended LPR status | Refer |
| R-EX-VALUE | Net worth near USD 2,000,000, or hard-to-value assets (private companies, partnership or trust interests by the Notice 97-19 method, foreign pensions, unvested equity) | Refer |
| R-EX-CERT | The 5-year record has gaps, or the person is weighing the Relief Procedures or another compliance program | Refer |
| R-EX-TRUST | A trust is involved: grantor or nongrantor classification, the section 684 interaction (877A(h)(3)), the valuation-ruling election | Refer; see `us-foreign-trust-reporting` |
| R-EX-DEFER | The person wants the deferral election (security, agreement, US agent) | Refer |
| R-EX-PENSION | Foreign pension or foreign deferred compensation, treaty questions, the services-abroad carve-out | Refer |
| R-EX-NEAR | Tax liability average within a few thousand dollars of USD 211,000 | Refer |
| R-EX-2801 | A US recipient of a gift or bequest from someone who may be a covered expatriate, including through foreign trusts | Refer |
| R-EX-STATE | State residency or state tax on the deemed sale matters | Refer to the state skill |
| R-EX-PRE2008 | Expatriated before 17 June 2008, or never filed Form 8854 after an earlier expatriation | Refer |

Do not state that a person is "not covered" until a signed Form 8854 certification of 5 compliant years is in hand.

## Filing and payment

- **Initial Form 8854** (Parts I and II): attach it to the income tax return for the year that includes the expatriation date, and file by that return's due date including extensions. If no return is required, send it separately to Internal Revenue Service, 3651 S IH35, MS 4301 AUSC, Austin, TX 78741 by the date the return would have been due ([Instructions for Form 8854](https://www.irs.gov/pub/irs-pdf/i8854.pdf)). Every expatriate files it, covered or not.
- **Due dates for a 2026 expatriate (calendar year):** nonresident on 31 December 2026 filing a dual-status Form 1040-NR with no US wages subject to withholding, **15 June 2027**, extended by Form 4868 to **15 December 2027**; with US wages subject to withholding or a resident at the end of 2026, **15 April 2027**, extended to **15 October 2027**. An extension covers filing, not payment.
- **Return type in the year of expatriation:** a covered expatriate who was a citizen or LTR for only part of the year files a **dual-status return**: Form 1040-NR with a Form 1040 attached as a schedule. The deemed sale, the ineligible deferred compensation and the specified tax-deferred accounts go on the Form 1040 part. An expatriation date of 1 January means no dual-status return ([Notice 2009-85, section 8](https://www.irs.gov/pub/irs-drop/n-09-85.pdf)). See `us-form-1040-nr-nonresident-return`.
- **Annual Form 8854** (Parts I and III): every year after the expatriation year while the person has deferred tax outstanding, an eligible deferred compensation item, or an interest in a nongrantor trust. Attach to Form 1040-NR if one is filed and send a copy marked "Copy" to Austin; otherwise send it alone by the date the return would have been due.
- **Penalty:** USD 10,000 for each year Form 8854 is not filed, or is incomplete or wrong, unless due to reasonable cause and not willful neglect (6039G(c)).
- **Payment:** mark-to-market tax is due with the return for the expatriation year, unless deferred under an accepted tax deferral agreement. Deferred tax plus interest on an asset sold later is due by that year's return due date, without extensions.
- **Form W-8CE:** give it to each payer of a deferred compensation item, each specified-account custodian, and each nongrantor trust trustee, by the earlier of the day before the first distribution after expatriation or 30 days after the expatriation date ([Form W-8CE](https://www.irs.gov/pub/irs-pdf/fw8ce.pdf)).
- **FBAR and Form 8938:** may still be required for the part of the year as a US person (`us-fbar-and-fatca-8938`).
- **Form 708:** filed by the US recipient under section 2801 (dates above).

### People who expatriated in 2025, still filing

For 2025 the tax liability test is more than USD 206,000 and the exclusion is USD 890,000 ([Rev. Proc. 2024-40, sections 2.37 and 2.38](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf); [Instructions for Form 8854 (2025)](https://www.irs.gov/pub/irs-pdf/i8854.pdf)). The initial Form 8854 goes with the 2025 return: a nonresident on 31 December 2025 with no US wages subject to withholding had until 15 June 2026, extended by Form 4868 to **15 December 2026**; otherwise 15 April 2026, extended to **15 October 2026**. Covered gifts and bequests received in 2025 above USD 19,000 go on a Form 708 due **15 June 2027**.

## Completion checklist

- [ ] Expatriate type confirmed: citizen, or LTR with at least 8 of 15 tax years after removing treaty years.
- [ ] Expatriation date fixed from the earliest qualifying event, with a CLN in hand for a citizen.
- [ ] Tax liability test run against the correct year's amount (2026 more than USD 211,000), net of the foreign tax credit, for the 5 years before the expatriation date.
- [ ] Net worth balance sheet at fair market value (Form 8854 Section B), including pensions, deferred compensation, equity, trust interests and gifts, tested against USD 2,000,000 or more.
- [ ] Five-year compliance checked across income, employment, gift and information returns, including FBARs; certification ready to sign, or a route to compliance chosen.
- [ ] Dual-citizen or minor exception tested against every condition, and used only against the first two tests.
- [ ] If covered: assets split into ordinary property, deferred compensation (eligible or ineligible), specified tax-deferred accounts and nongrantor trusts.
- [ ] Mark-to-market gains and losses computed, 877A(h)(2) basis rule considered, section 1091 not applied, and the USD 910,000 exclusion allocated asset by asset.
- [ ] Deemed distributions included with no early distribution tax; W-8CE sent and treaty waivers made where eligibility is wanted.
- [ ] Deferral election decided asset by asset, with security, waiver, US agent and agreement if used.
- [ ] Any open section 1031 or other replacement window, or payment extension, treated as ending on the day before the expatriation date.
- [ ] Dual-status return prepared; initial Form 8854 filed on time; annual Form 8854 obligations diarised.
- [ ] Section 2801 exposure explained for future gifts and bequests to US persons; donor disclosure authorization considered.
- [ ] State tax treatment checked separately.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 4.37 (more than $211,000), 4.38 ($910,000) and 4.42(3) ($19,000 for section 2801). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Rev. Proc. 2024-40. Read for sections 2.37 ($206,000) and 2.38 ($890,000) for 2025. | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-13 |
| Instructions for Form 8854 (2025). Read for the covered expatriate tests, Section B net worth, Section C allocation of the exclusion, Section D deferral, certification, the Austin address and annual filing. | https://www.irs.gov/pub/irs-pdf/i8854.pdf | 2026-11-13 |
| Form W-8CE. Read for who must file and the timing (earlier of the day before the first distribution or 30 days after expatriation). | https://www.irs.gov/pub/irs-pdf/fw8ce.pdf | 2026-11-13 |
| Instructions for Form 708 (December 2025). Read for the $19,000 section 2801(c) amount for 2025 and 2026, the 40% rate, the 18th-month due date, Form 7004 extension, protective return and presumption. | https://www.irs.gov/pub/irs-pdf/i708.pdf | 2026-11-13 |
| Notice 2009-85. Read for section 3E (deferral interest) and section 8 (dual-status return). | https://www.irs.gov/pub/irs-drop/n-09-85.pdf | 2026-11-13 |
| IRS, Expatriation tax. Read for the regime overview and earlier years' thresholds. | https://www.irs.gov/individuals/international-taxpayers/expatriation-tax | 2026-11-13 |
| IRS, Relief Procedures for Certain Former Citizens. Read for the eligibility conditions (after 18 March 2010, no filing history, $25,000, under $2 million). | https://www.irs.gov/individuals/international-taxpayers/relief-procedures-for-certain-former-citizens | 2026-11-13 |
| 26 U.S.C. 877 (govinfo). Read for (a)(2)(B) $2,000,000 or more, (a)(2)(C) certification and (e)(2) the 8-of-15-years test. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877.htm | 2026-11-13 |
| 26 U.S.C. 877A (govinfo). Read for (a) to (h), the 30% withholding, the exceptions (10 years, age 18½) and (g)(4) relinquishment date. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec877A.htm | 2026-11-13 |
| 26 U.S.C. 6039G (govinfo). Read for the $10,000 penalty. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6039G.htm | 2026-11-13 |
| 26 U.S.C. 2801 (govinfo). Read for who pays, covered gifts, exclusions, the highest-rate rule and the foreign tax credit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap15-sec2801.htm | 2026-11-13 |
| 26 U.S.C. 2001(c) (govinfo). Read for the top rate of 40%. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partI-sec2001.htm | 2026-11-13 |
| 26 U.S.C. 7701(b)(6) (govinfo). Read for when lawful permanent residence ends under a treaty position. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm | 2026-11-13 |

Not yet confirmed: the 2026 Form 8854 and its instructions were not published when read, so Form 8854 line references follow the 2025 instructions and the 2026 thresholds come from Rev. Proc. 2025-32; the US Code text read is the 2024 edition, and no change by Public Law 119-21 to sections 877, 877A, 2001(c), 2801 or 6039G was found, but that was not checked line by line against the Public Law.
