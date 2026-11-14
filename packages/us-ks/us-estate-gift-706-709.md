---
name: us-estate-gift-706-709
description: Work out the US federal estate, gift and generation-skipping transfer tax for 2026 on Form 706 (estate) and Form 709 (gift), for US citizens and residents. 2026 figures from Rev. Proc. 2025-32 and the 2026 Form 706 instructions, including the USD 15,000,000 basic exclusion amount and GST exemption set by section 70106 of Public Law 119-21 (no 2026 sunset), the 40% top rate, the USD 5,945,800 basic credit, the USD 19,000 annual exclusion, the USD 194,000 non-citizen spouse exclusion, gift splitting, portability and DSUE with the Rev. Proc. 2022-32 five-year relief, direct tuition and medical payments, the 529 five-year election, alternate valuation, special use valuation, section 6166 installments, the marital and charitable deductions, QDOTs, basis at death and by gift, and the anti-clawback rule. Trigger on "estate tax", "gift tax", "Form 706", "Form 709", "portability", "DSUE", "lifetime exemption", "annual exclusion", "GST tax", "gift splitting". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: estate-wealth-tax
type: computation
---

# US estate, gift and generation-skipping transfer tax (Forms 706 and 709), 2026

> **Source-cited draft.** Built from Rev. Proc. 2025-32, the Instructions for Form 706 (Rev. July 2026, for decedents dying after 31 December 2025), the 2025 Instructions for Form 709, Rev. Proc. 2022-32, Public Law 119-21 section 70106 and 26 U.S.C. 2032, 2503, 2513, 2523, 2631, 2641 and 6075, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional (EA, CPA or attorney) before filing.

**Answer first.** For a death or gift in 2026 the basic exclusion amount is **USD 15,000,000** per person, and the GST exemption is the same **USD 15,000,000**. The 2025 law (Public Law 119-21, section 70106) struck the sunset, so there is no fall back to about USD 7 million in 2026; the amount is indexed from 2027. Tax above the exclusion is effectively **40%**. The basic credit is **USD 5,945,800** (the tax on USD 15,000,000). A donor can give **USD 19,000** per donee in 2026 (present interests) without using any exclusion, and USD 194,000 to a spouse who is not a US citizen. Form 706 is due **9 months after death**; Form 709 for 2026 gifts is due **15 April 2027**.

## Scope and who this is for

In scope: US citizens and US residents (domiciled in the US) who die or make gifts in 2026.

- **Form 706** is required when the gross estate plus adjusted taxable gifts (and any pre-1977 specific exemption used) is more than USD 15,000,000, or when the executor elects portability of the deceased spousal unused exclusion (DSUE), whatever the size of the estate (2026 Form 706 instructions, Which Estates Must File). It is also the return for alternate valuation, special use valuation, section 6166 deferral, QTIP and QDOT elections.
- **Form 709** is required for gifts over the annual exclusion to any one donee, gifts of future interests of any amount, gift splitting, the 529 five-year election, gifts to a non-citizen spouse over USD 194,000, and gifts where GST exemption is allocated or an election out is made.
- **GST tax** (chapter 13): direct skips on Form 706 Schedule R or Form 709 Schedule D; taxable distributions on Form 706-GS(D) and 706-GS(D-1); taxable terminations on Form 706-GS(T).
- Coordination with income tax basis under sections 1014 (death) and 1015 (gift), and the anti-clawback rule of Treas. Reg. 20.2010-1(c) (T.D. 9884).

Out of scope, and where it goes:

| Topic | Where it goes |
| --- | --- |
| Income tax of the estate or trust after death (Form 1041, DNI, 65-day rule, the section 642(g) election from the 1041 side, IRD on the 1041) | `us-form-1041-trust-and-estate-income` |
| State estate, inheritance and gift taxes (thresholds, rates, state portability) | `us-state-estate-and-inheritance-tax-matrix` |
| Non-resident alien decedents (Form 706-NA) and donors (Form 709-NA) beyond the overview below | Refer; `us-form-1040-nr-nonresident-return` for their income tax |
| Covered gifts and bequests from a covered expatriate (section 2801) | `us-expatriation-exit-tax` |
| 529 plan rules other than the gift tax election | `us-529-and-trump-accounts` |
| Charitable remainder and lead trust design and income tax | `us-charitable-giving-strategies` |
| Foreign trusts (Forms 3520, 3520-A) | `us-foreign-trust-reporting` |
| Valuation opinions, FLP discounts, section 2704, QDOT drafting, SLAT drafting, letter rulings, audit defence | Refer (see When to refuse or refer) |

Audience: a Circular 230 practitioner drafting a return or a planning memo. The output is always a reviewer brief plus draft forms, never a final return.

## Ask the client first

1. **Citizenship and domicile** of the decedent or donor, and of the spouse. A non-citizen spouse changes the marital deduction (QDOT) and the gift exclusion; a non-resident non-citizen decedent is out of scope.
2. **Date of death or date of each gift.** The year fixes the exclusion: 2026 uses USD 15,000,000; earlier years use their own amounts (2025: USD 13,990,000).
3. **Every Form 709 ever filed**, and every post-1976 taxable gift. Adjusted taxable gifts drive both the Form 706 filing test and the tax.
4. **Marital status and prior marriages.** Is there a surviving spouse? Did a previous spouse die and leave DSUE (and did that estate elect portability)? Has the survivor remarried?
5. **The will and trust documents**: what passes to the spouse outright, to a QTIP or bypass trust, to charity, to grandchildren or to trusts that can benefit skip persons.
6. **Asset list with values and basis**: real estate, securities, closely held businesses, life insurance (who owns the policy, who is the beneficiary; Form 712 from each insurer), retirement accounts, jointly held property (with whom, and who contributed).
7. **Lifetime transfers with strings**: retained income or use, powers to revoke or change, life insurance given away within 3 years of death, GRATs, QPRTs, SLATs.
8. **Appraisals** for real estate, business interests and art.
9. **For gifts**: donee name and relationship, present or future interest, Crummey notices sent, whether the spouse will consent to split, 529 contributions, direct tuition or medical payments.
10. **State of domicile and states where real property sits** (for the state skill).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Basic exclusion amount, death or gift in 2026 (section 2010(c)(3), as amended by Public Law 119-21 section 70106) | USD 15,000,000 | [Rev. Proc. 2025-32, section 3.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| GST exemption, 2026 (section 2631(c)) | USD 15,000,000 | [Rev. Proc. 2025-32, section 3.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Basic credit amount (tentative tax on USD 15,000,000), decedents dying in 2026 | USD 5,945,800 | [Instructions for Form 706 (Rev. July 2026), What's New](https://www.irs.gov/pub/irs-pdf/i706.pdf) |
| Unified rate schedule (section 2001(c)): 18% on the first USD 10,000 rising to 40% over USD 1,000,000; the tax on USD 1,000,000 is USD 345,800 | 40% top rate | [Instructions for Form 706 (Rev. July 2026), Table A](https://www.irs.gov/pub/irs-pdf/i706.pdf) |
| GST tax rate: the maximum estate tax rate times the inclusion ratio (section 2641) | 40% times inclusion ratio | [26 U.S.C. 2641](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapE-sec2641.htm) |
| Annual exclusion per donee, present interests (section 2503(b)) | USD 19,000 | [Rev. Proc. 2025-32, section 4.42(1)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Annual exclusion for gifts to a spouse who is not a US citizen (section 2523(i)(2)) | USD 194,000 | [Rev. Proc. 2025-32, section 4.42(2)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Ceiling on the reduction in value from special use valuation (section 2032A) | USD 1,460,000 | [Rev. Proc. 2025-32, section 4.41](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Amount used to figure the 2-percent portion of tax deferred under section 6166 (section 6601(j)) | USD 1,940,000 | [Rev. Proc. 2025-32, section 4.51](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Form 706 due date (section 6075(a)) | 9 months after death | [26 U.S.C. 6075](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6075.htm) |
| Form 709 due date (section 6075(b)) | 15 April after the gift year (15 April 2027 for 2026 gifts) | [26 U.S.C. 6075](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6075.htm) |
| Late portability election without a ruling (Rev. Proc. 2022-32) | On or before the fifth anniversary of death | [Rev. Proc. 2022-32, section 4.01](https://www.irs.gov/pub/irs-drop/rp-22-32.pdf) |

Derived figures used below (arithmetic only): with gift splitting, two spouses can give USD 38,000 per donee (2 x USD 19,000); the 529 five-year election covers up to USD 95,000 per donee from one donor (5 x USD 19,000), or USD 190,000 with a consenting spouse; a married couple with full portability shelters up to USD 30,000,000 (2 x USD 15,000,000) at 2026 amounts.

### Step 1. The unified system

The estate tax (sections 2001 to 2058), the gift tax (sections 2501 to 2524) and the GST tax (sections 2601 to 2664) share one lifetime exclusion. The applicable exclusion amount (AEA) under section 2010(c)(2) is the basic exclusion amount (BEA) plus any DSUE from the last deceased spouse (plus any restored exclusion, rarely relevant). The applicable credit is the tentative tax on the AEA. Because the BEA is far above USD 1,000,000, every taxable dollar above the AEA is taxed at the 40% top rate; the lower brackets are absorbed by the credit.

From 2027 the BEA is indexed with 2025 as the base year (section 70106 of Public Law 119-21 changed section 2010(c)(3)(B)) and rounded to a multiple of USD 10,000; the annual exclusion is rounded down to a multiple of USD 1,000 (section 2503(b)(2)).

### Step 2. Form 709: is a gift return needed, and what is taxable

1. **Exclude first.** Per donee per year, the first USD 19,000 of present-interest gifts is excluded (section 2503(b)). It does not carry forward: an unused 2026 exclusion ends on 31 December 2026.
2. **Present interest.** Gifts in trust usually fail unless the beneficiary holds a Crummey withdrawal right (a temporary right to withdraw, typically 30 to 60 days). Confirm notices were sent. Future interests (most trust gifts without Crummey powers, remainders, reversions) get no exclusion and need Form 709 whatever the amount.
3. **Unlimited direct tuition and medical payments (section 2503(e)).** Tuition paid directly to an educational organization (section 170(b)(1)(A)(ii)) and medical care paid directly to the provider (section 213(d), including health insurance premiums; not amounts reimbursed by insurance) are not gifts. Payment to the beneficiary, even with receipts, does not qualify. Tuition only: room, board, books and fees do not qualify. No relationship, age or citizenship test for the beneficiary. Not reported on Form 709.
4. **Spouse.** Gifts to a US-citizen spouse get the unlimited marital deduction (section 2523(a)). Gifts to a non-citizen spouse do not; instead the first USD 194,000 a year of present-interest gifts is excluded (section 2523(i)(2)). Above that, the excess uses the BEA.
5. **Gift splitting (section 2513).** Spouses may treat all gifts to third parties made by either during the year as made half by each, doubling the exclusion to USD 38,000 per donee and sharing the BEA. Conditions: each spouse is a US citizen or resident at the time of the gift; married to each other at the gift and, if the marriage ends later in the year, the donor does not remarry before year end; the election covers all gifts by both to third parties that year. A gift in which the consenting spouse has an interest (other than a remote one) cannot be split. The election is made on Form 709 Part III (lines 1 to 7) with a Notice of Consent signed by the consenting spouse, who no longer signs the return. Both spouses generally file, except that only the donor spouse files when the donor's gifts to any third party were more than USD 19,000 but not more than USD 38,000, the consenting spouse's gifts were not more than USD 19,000 to any third party, and all gifts were present interests.
   - Review point: a couple whose gifts are each at or under USD 19,000 per donee does not need to split. Splitting matters when one spouse gives between USD 19,001 and USD 38,000 to a donee from separate property, or when the source of a gift from joint or community property is unclear.
6. **529 five-year election (section 529(c)(2)(B)).** A contribution above the annual exclusion can be spread over five years, up to USD 95,000 per donee per donor (USD 190,000 split). Form 709 must be filed for the contribution year even with no tax; the election is on Schedule A, line B, and one-fifth is reported in each year. During the five years the annual exclusion for that donee is used by the 529, so other gifts to that donee use the BEA. If the donor dies within the five years, the amounts for years after death are pulled back into the gross estate (section 529(c)(4)(C)); the year of death and earlier years stay out.
7. **Taxable gifts and the cumulative computation (section 2502).** Tax for the year = tax on all taxable gifts to date minus tax on prior-period gifts, minus the unused applicable credit. Schedule B lists prior gifts; get every prior return. Nobody pays gift tax until cumulative taxable gifts pass the AEA.

Schedule A items: donee name, address and relationship; description (number of shares and issuer, or the share of a property and its address); date; donor's adjusted basis and date acquired (the donee takes carryover basis under section 1015); value at the date of gift; and, for split gifts, a mark that this is the donor's half.

Form 709 layout: page 1 Part I (general information) and Part II (tax computation); Part III spouse's consent (moved from Part I lines 12 to 18 in the 2025 redesign); Schedule A Part 1 gifts subject only to gift tax, Part 2 direct skips, Part 3 indirect skips, Part 4 taxable gift reconciliation; Schedule B prior periods; Schedule C DSUE used by a surviving spouse on lifetime gifts; Schedule D GST (Part 1 transfers, Part 2 exemption reconciliation and allocation, Part 3 tax on direct skips).

### Step 3. Form 706: the gross estate to the tax

1. **Gross estate (Schedules A to I)**: A real estate (A-1 special use election); B stocks and bonds; C mortgages, notes and cash; D insurance on the decedent's life (attach Form 712); E jointly held property (Part 1 qualified joint interests with a spouse, Part 2 all other); F other property (tangible property, business interests, IRAs and 401(k)s, partnership interests, royalties); G transfers during life (sections 2035 to 2038, including insurance given away within 3 years); H powers of appointment (section 2041); I annuities (section 2039).
2. **Deductions**: J funeral and administration expenses; K debts, mortgages and liens; L losses during administration; M bequests to the spouse (section 2056); O charity (section 2055); line 3b state death taxes (section 2058, a deduction since the credit was repealed for deaths after 2004); U conservation easement exclusion (section 2031(c)).
3. **Taxable estate plus adjusted taxable gifts** (post-1976 taxable gifts not included in the gross estate) = the tentative tax base. Gifts pulled back into the gross estate under section 2035 are not added again as adjusted taxable gifts (section 2001(b)).
4. **Tentative tax** on that base under Table A.
5. **Less gift tax payable** on post-1976 gifts, recomputed at the rates in effect at death (section 2001(b)(2)); this neutralises rate changes between gift and death.
6. **Less the applicable credit** (on BEA plus DSUE), the foreign death tax credit (section 2014, Schedule P) and the credit for tax on prior transfers (section 2013, Schedule Q).
7. **Plus GST tax** on direct skips (Schedule R; Schedule R-1 for a direct skip from a trust, sent to the trustee). The old section 4980A excess retirement accumulation tax is repealed for deaths after 1996; ignore it.

Schedule PC is the protective claim for refund.

### Step 4. Marital deduction, QTIP and QDOT

- The property must pass to a surviving spouse who is a US citizen (section 2056). Terminable interests generally fail (section 2056(b)(1)).
- **QTIP**: the executor may elect under section 2056(b)(7) for property where the spouse gets all the income for life. The price is inclusion in the survivor's estate (section 2044). The election is made on Schedule M by listing the property.
- **Non-citizen spouse**: no marital deduction unless the property passes to a qualified domestic trust (section 2056A): at least one trustee a US citizen or domestic corporation, the trustee able to withhold the deferred estate tax on corpus distributions, and the security rules of Treas. Reg. 20.2056A-2(d) (for example a bond or letter of credit when QDOT assets exceed USD 2 million). The deferred tax falls on corpus distributions and on the survivor's death. Issue-spot only; drafting is referred.

### Step 5. Charitable deduction

Section 2055 is unlimited in amount; the recipient must be a qualified organisation. Charitable remainder trusts must meet section 664. A charitable lead interest is valued with the section 7520 rate at death (or the alternate valuation date). Foreign charities: the estate tax rule in section 2055 is more permissive than the income tax rule in section 170(c), so do not apply the income tax test to an estate bequest.

### Step 6. Portability and DSUE

- **Formula**: DSUE = the lesser of the BEA of the deceased spouse at death and that spouse's AEA minus (taxable estate plus adjusted taxable gifts). A spouse who died in 2026 and used nothing leaves DSUE of USD 15,000,000. DSUE is fixed at the first death; it is not indexed later.
- **Last deceased spouse (section 2010(c)(4)(B)(i))**: the survivor uses DSUE only from the most recently deceased spouse. If the survivor remarries and the new spouse dies first, the earlier DSUE is lost, except that DSUE already used on the survivor's gifts stays used.
- **How to elect**: a complete and properly prepared Form 706, filed on time (9 months, or within the 6-month extension on Form 4768). A portability-only return may use the simplified valuation rule of Treas. Reg. 20.2010-2(a)(7)(ii): no values for property passing to the spouse or charity, but the estimated total from the Table of Estimated Values in the Form 706 instructions goes into the totals; property not deducted is valued in full.
- **Late election (Rev. Proc. 2022-32)**: an estate not otherwise required to file under section 6018(a) may file on or before the fifth anniversary of death, without a ruling or user fee, writing at the top: "FILED PURSUANT TO REV. PROC. 2022-32 TO ELECT PORTABILITY UNDER § 2010(c)(5)(A)". The decedent must have been survived by a spouse, been a US citizen or resident, and not have been required to file. After five years, relief is only by letter ruling under Treas. Reg. 301.9100-3. Rev. Proc. 2022-32 superseded Rev. Proc. 2017-34.
- **Examination (section 2010(c)(5)(B))**: the IRS may examine the first spouse's return to check the DSUE whenever the survivor uses it, even after the normal limitation period under section 6501. Keep the records until the survivor's estate is closed.
- **When not to elect**: cost of preparation; the return opens the estate to examination; a likely remarriage may waste the DSUE; most states with an estate tax do not allow state portability (check the state skill), so a bypass trust may still be needed for state tax. For a surviving spouse with assets near or above the BEA, electing usually wins. Worked case 2 is the test.

### Step 7. Alternate valuation (section 2032)

- All property is valued at 6 months after death, or at the date of sale, exchange or distribution if earlier within the 6 months.
- All or nothing: the election covers the whole gross estate.
- Allowed only if it reduces both the gross estate and the estate plus GST tax (section 2032(c)), so it cannot be used just to raise basis.
- Made on Form 706 Part III, line 1, with the alternate value column on each schedule. It may be made on a late return filed not later than 1 year after the due date (with extensions actually granted); once made it cannot be revoked.
- Income earned in the 6 months is not part of the gross estate; it is estate income on Form 1041.
- Basis under section 1014(a)(2) becomes the alternate value, which hurts heirs if the asset later recovers.

### Step 8. Special use valuation and installment payment

- **Section 2032A** (farm or business real property): the value may be reduced by up to USD 1,460,000 for 2026 deaths. The election may be made on a late return if it is the first return filed. Qualified heirs and a 10-year recapture period follow; tracking recapture is referred.
- **Section 6166**: where the closely held business interest is more than 35% of the adjusted gross estate (gross estate less section 2053 and 2054 items), the executor may defer the tax on that interest, pay interest only for up to 5 years and then the tax in up to 10 annual installments. Interest is 2% on the "2-percent portion": the tentative tax on USD 1,940,000 plus the applicable exclusion amount, less the applicable credit (or the deferred tax, if less). The rest bears 45% of the section 6601(a) underpayment rate. Elected on Part III, line 3. Disposing of or withdrawing 50% or more of the interest ends the deferral (section 6166(g)(1)(A)). Bond and lien negotiations are referred. Section 6163 postpones tax on reversionary or remainder interests (Part III, line 4); section 6161 extensions to pay are discretionary and need reasonable cause.

### Step 9. GST tax

| Transfer | What it is | Return |
| --- | --- | --- |
| Direct skip | Transfer to a skip person subject to gift or estate tax | Form 709 Schedule D Part 3; Form 706 Schedule R |
| Taxable distribution | Distribution from a trust to a skip person | Form 706-GS(D) (distributee), 706-GS(D-1) (trustee) |
| Taxable termination | An interest ends and only skip persons hold interests after | Form 706-GS(T) (trustee) |

- **Skip person (section 2613)**: a person two or more generations below the transferor (grandchildren and lower); for non-relatives, more than 37.5 years younger (12.5 to 37.5 years younger is the children's generation; within 12.5 years is the transferor's generation); or a trust where all interests are held by skip persons, or where no one holds an interest and no distribution can ever go to a non-skip person.
- **Predeceased parent (section 2651(e))**: if the skip person's parent who is the transferor's descendant died before the transfer, the skip person moves up a generation.
- **Exemption USD 15,000,000 for 2026**, allocated separately from the BEA. A gift to a child uses BEA and no GST exemption; a direct skip uses both.
- **Inclusion ratio (section 2642)** = 1 minus (exemption allocated / value of the property transferred). 0 means fully exempt (the aim for a dynasty trust); 1 means fully taxable; in between, later distributions are taxed in proportion.
- **Automatic allocation**: to direct skips (section 2632(b), elect out under (b)(3)) and to indirect skips to a "GST trust" (section 2632(c), elect out under (c)(5)). "GST trust" is defined by six tests in section 2632(c)(3)(B); misclassification is common, so test each one.
- **Elections on Schedule D Part 2**: elect in or out, or allocate in writing by the due date. A missed allocation can be made late on a later Form 709, effective on filing, at the value then (section 2642(d)); other relief needs section 9100 (referred).
- **ETIP (section 2642(f))**: no allocation while the property would be in the transferor's estate under sections 2035 to 2042 (GRATs, other section 2702 retained interests); allocation waits until the ETIP closes.
- **Reverse QTIP (section 2652(a)(3))**: lets the first spouse stay the transferor of QTIP property for GST purposes, so that spouse's exemption is used; elected on Schedule R Part 1.
- Allocations are fixed when made. Trusts funded before 2026 to beat the old sunset keep their inclusion ratio.

### Step 10. Basis at death and by gift

- **Section 1014**: property acquired from a decedent takes fair market value at death (or the alternate value): a step-up or a step-down. Covers everything in the gross estate, taxable or not; the included part of joint property; both halves of community property (section 1014(b)(6)); property included under sections 2036, 2038 or 2041.
- **No step-up for income in respect of a decedent (section 691)**: IRAs and qualified plans, unpaid wages and similar items keep the decedent's character and are taxed to the recipient, with the section 691(c) deduction for estate tax on them (see `us-form-1041-trust-and-estate-income`). Completed lifetime gifts not pulled back into the estate get no step-up.
- **Section 1015 (gift)**: carryover basis for gain, increased under section 1015(d) by gift tax paid on the appreciation; for loss, the lower of the donor's basis and value at the gift (the double basis rule).
- **Consistent basis**: when Form 706 is required, the executor files Form 8971, separately from Form 706, with Schedules A to the beneficiaries (sections 1014(f) and 6035).

| Asset | Hold until death | Give now |
| --- | --- | --- |
| Value above basis | Usually better: step-up wipes the gain | Gain carries over to the donee |
| Value below basis | Step-down loses the loss | Donee cannot use the loss below value at gift; often better to sell and give cash |

Trade-off for a large gift of low-basis assets: the gift moves future growth out of the estate (saving 40%) but gives up the step-up, so the donee pays capital gains tax, net investment income tax and state tax on a later sale (often more than 30% combined). High-basis assets suit gifts; low-basis assets held long term often suit holding, or a freeze (GRAT, sale to a grantor trust) that moves growth without using basis.

### Step 11. The anti-clawback rule (Treas. Reg. 20.2010-1(c), T.D. 9884)

- If the BEA at death is lower than the BEA used on lifetime gifts, the credit in the estate computation is based on the larger of the BEA at death and the BEA used on post-1976 gifts (for section 2001(b)(2)).
- Top of the stack: the protection covers only gifts above the BEA at death. Example under a hypothetical future law cut: gifts of USD 13,000,000 made in 2025, death in a later year with a BEA of USD 7,000,000. Protected excess USD 6,000,000; the USD 7,000,000 BEA shelters the rest; USD 13,000,000 of transfers is sheltered in total.
- Under current law no cut is scheduled: the BEA is USD 15,000,000 for 2026 and indexed after. A donor who died in 2026 after USD 13,000,000 of gifts needs no anti-clawback computation; the gifts sit inside the USD 15,000,000. The rule matters only if a future statute reduces the BEA.
- **Proposed anti-abuse rule** (REG-118913-21, 87 FR 24918, April 2022, not final): no protection for transfers included in the gross estate under sections 2035 to 2042 (retained interests, revocable transfers, powers, insurance), with an exception for includible transfers whose taxable amount is 5% or less of the transfer. To rely on anti-clawback, a gift must be complete under section 2511 and outside sections 2035 to 2042; reciprocal SLATs risk the reciprocal trust doctrine and section 2036.

### Step 12. Non-resident non-citizens (overview only)

- A decedent neither a US citizen nor domiciled in the US is taxed only on US-situs property (sections 2101 to 2108). The unified credit is USD 13,000 (section 2102(b)), about USD 60,000 of exemption. Form 706-NA is required when US-situs gross estate exceeds USD 60,000; due 9 months after death.
- US-situs: US real property, tangible property located in the US, stock of US corporations wherever the certificates are held, and most debt of US persons. Not US-situs: US bank deposits not connected with a US business (section 2105(b)(1)), portfolio interest debt (section 2105(b)(3)), and insurance on the non-resident's life (section 2105(a)).
- Estate and gift tax treaties (the IRS list includes Australia, Austria, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Japan, the Netherlands, South Africa, Switzerland and the United Kingdom, plus estate provisions in the Canada income tax treaty) may prorate the credit or give a credit for foreign death tax.
- A non-resident donor pays gift tax only on US real property and tangible property in the US; gifts of intangibles, including US stock, are not taxed (section 2501(a)(2)). The donee takes carryover basis.
- Preparing Form 706-NA or 709-NA is referred.

### Planning structures (overview only)

| Structure | How it works | Point to watch |
| --- | --- | --- |
| Spousal lifetime access trust (SLAT) | Gift to an irrevocable trust for the other spouse | Reciprocal SLATs need real differences (trustees, terms, dates, assets), separate meetings and independent counsel |
| Dynasty trust | Long-lived GST-exempt trust in a state with no or a long perpetuities rule | Allocate GST exemption to get a zero inclusion ratio |
| Sale to an intentionally defective grantor trust | Sale for a note at the section 7520 or 1274 rate | Freezes value; grantor pays the income tax, further reducing the estate |
| GRAT | Donor keeps an annuity at the section 7520 rate | Zeroed-out GRAT uses little exemption; ETIP blocks GST allocation |
| QPRT | Residence to a trust, donor keeps use for a term | Donor must outlive the term (section 2036) |
| Charitable lead annuity trust | Charity gets the annuity, family the remainder | Works best when the section 7520 rate is low |

### Filing logistics

- **Form 706**: due 9 months after death; Form 4768 gives an automatic 6-month extension to file (not to pay). Extension to pay is under section 6161, or by electing sections 6166 or 6163. Mail to Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999 (private delivery: Internal Revenue Submission Processing Center, 333 W. Pershing Road, Kansas City, MO 64108; supplemental returns go to Florence, KY). Attach the death certificate and a certified copy of the will. E-filing: the 2026 instructions list Forms 8453-EG and 8879-EG as the e-file declaration and authorization for Forms 706 and 709. Pay by EFTPS or same-day wire where possible.
- **Estate tax closing letter**: issued only on request through Pay.gov with a user fee, at least 9 months after filing; otherwise use an account transcript.
- **Form 709**: due 15 April 2027 for 2026 gifts. A Form 4868 extension for the donor's income tax return also extends Form 709 (section 6075(b)(2)); otherwise use Form 8892, which also serves as a payment voucher. For a donor who died during the year, the executor uses Form 4768. An extension to file is not an extension to pay; interest runs from 15 April. Form 709 can be e-filed through MeF (2025 instructions); paper returns go to Kansas City, MO 64999.

### Check of the 2026 credit

Tentative tax on USD 15,000,000 = USD 345,800 + 40% x (USD 15,000,000 minus USD 1,000,000) = USD 345,800 + USD 5,600,000 = USD 5,945,800, which matches the basic credit printed in the 2026 Form 706 instructions.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Death or gift before 2026 | Use that year's amounts (2025: BEA USD 13,990,000, annual exclusion USD 19,000, non-citizen spouse USD 190,000, per Rev. Proc. 2024-40); do not apply 2026 figures |
| Gross estate under USD 15,000,000 but a spouse survives | No filing duty, but consider a portability-only return (Step 6) |
| Survivor remarried and the new spouse died first | Only the newest deceased spouse's DSUE is available |
| Surviving spouse already dead when the return is filed | Portability is moot; no return needed for it |
| Gift to a trust with no withdrawal right | Future interest: no annual exclusion, Form 709 required |
| Tuition paid to the student, not the school | A normal gift, not section 2503(e) |
| Non-citizen surviving spouse | No Schedule M deduction without a QDOT |
| Alternate valuation that does not lower both value and tax | Not allowed (section 2032(c)); value at death |
| Life insurance on the decedent payable to the estate or owned by the decedent | Included (section 2042); an ILIT would have kept it out |
| Gift of a policy within 3 years of death | Pulled back under section 2035 |
| IRA left to the spouse | Marital deduction allowed; the spouse still pays income tax on distributions (IRD) |
| Closely held interest over 35% of adjusted gross estate | Section 6166 deferral may be elected |
| Gift-splitting where each spouse is a beneficiary of the other's SLAT | Splitting not allowed for those gifts |

### Defaults when a fact is missing

| Missing fact | Default | Flag |
| --- | --- | --- |
| Prior Form 709 history | Do not finalise; ask for transcripts and every prior return, or a client representation | Adjusted taxable gifts unreconciled |
| Whether a trust gift is a present interest | Treat as a future interest | Confirm Crummey notices |
| Spouse's citizenship | Treat as non-citizen until proved | QDOT and USD 194,000 limit |
| GST allocation intent | Accept the automatic allocation rules | State the risk in the brief |
| Value of a closely held interest | No discount until an appraisal supports one | Appraisal required |
| Whether portability is wanted | Recommend electing where a spouse survives | Client decision recorded |
| Whether a year-end gift was completed (delivery, intent, acceptance) | Treat as made when completed, possibly the next year | Different year's figures |

### Red flags

| Red flag | Why it matters |
| --- | --- |
| A spouse died in the last 5 years and no Form 706 was filed | Late portability still possible under Rev. Proc. 2022-32 |
| Reciprocal SLATs with near-identical terms | Reciprocal trust doctrine may pull both back under section 2036 |
| Large pre-death gifts of low-basis assets | Lost step-up; carryover basis |
| Appraisal missing for real estate, a business or art over USD 3,000 | Return incomplete; undervaluation penalties |
| State domicile with an estate tax | Separate state return; see the state skill |
| Gifts funded just before a law change with matching structures | Step-transaction scrutiny; document independent decisions |

## Worked cases

### Case 1. Taxable estate, single decedent, 2026

Decedent dies unmarried in 2026. Taxable estate USD 16,500,000 after deductions; adjusted taxable gifts USD 1,000,000 (no gift tax was paid on them). Tentative tax base USD 17,500,000. Tentative tax = USD 345,800 + 40% x USD 16,500,000 = USD 6,945,800. Less the basic credit USD 5,945,800. Net estate tax **USD 1,000,000**, which is 40% of the USD 2,500,000 above the BEA. Form 706 is due 9 months after death.

```oa-check
name: Single decedent, taxable estate plus prior gifts above the 2026 BEA
inputs:
  taxable_estate: 16500000
  adjusted_taxable_gifts: 1000000
  bea: 15000000
steps:
  - tax_base: taxable_estate + adjusted_taxable_gifts
  - tentative_tax: 345800 + (tax_base - 1000000) * 0.40
  - applicable_credit: 345800 + (bea - 1000000) * 0.40
  - net_estate_tax: max(tentative_tax - applicable_credit, 0)
expected:
  tax_base: 17500000
  tentative_tax: 6945800.00
  applicable_credit: 5945800.00
  net_estate_tax: 1000000.00
```

### Case 2. Decision: file Form 706 only to elect portability?

First spouse dies in 2026 leaving a USD 4,000,000 estate entirely to the US-citizen surviving spouse (all marital deduction, taxable estate nil). The first spouse made USD 500,000 of taxable gifts earlier. The survivor expects an estate of USD 22,000,000. Holding the BEA at USD 15,000,000 (indexing ignored); estimated cost of a portability-only return USD 25,000 (an assumption for the case).

DSUE = USD 15,000,000 minus USD 500,000 = USD 14,500,000. Without portability the survivor's estate tax is 40% x USD 7,000,000 = USD 2,800,000; with portability the survivor's AEA is USD 29,500,000 and the tax is nil. Saving USD 2,800,000 against a USD 25,000 cost: **elect**. File within 9 months (or the extension); if missed, within 5 years under Rev. Proc. 2022-32. Keep the records until the survivor's estate closes, and warn about remarriage.

```oa-check
name: Portability decision, 2026 death, survivor estate 22 million
inputs:
  bea: 15000000
  first_taxable_estate: 0
  first_adjusted_gifts: 500000
  survivor_estate: 22000000
  return_cost: 25000
steps:
  - dsue: min(bea, bea - (first_taxable_estate + first_adjusted_gifts))
  - tax_without: max(survivor_estate - bea, 0) * 0.40
  - tax_with: max(survivor_estate - bea - dsue, 0) * 0.40
  - saving: tax_without - tax_with
  - elect: min(max(saving - return_cost, 0), 1)
expected:
  dsue: 14500000
  tax_without: 2800000.00
  tax_with: 0.00
  saving: 2800000.00
  elect: 1
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-ET-NRA | Decedent or donor neither a US citizen nor US-domiciled (Form 706-NA, 709-NA) | Refer to an international specialist |
| R-ET-LATEPORT | Portability wanted more than 5 years after death | Refer: letter ruling under Treas. Reg. 301.9100-3 |
| R-ET-6166 | Section 6166 bond or lien negotiation | Refer to a specialist; IRS Estate and Gift Tax |
| R-ET-2032A | Special use election and 10-year recapture tracking | Refer to a farm or ranch specialist |
| R-ET-QDOT | QDOT drafting for a non-citizen spouse | Refer to a trusts and estates attorney |
| R-ET-FLP | FLP discounts and section 2704 restrictions | Refer to appraiser and attorney |
| R-ET-SLAT | Reciprocal SLAT differentiation memo, or a large SLAT gift with no attorney memo | Refer to an attorney; do not prepare the return without the memo |
| R-ET-9100 | Section 9100 relief for a missed GST allocation | Refer: letter ruling |
| R-ET-CHAR | Opinion that a split-interest charitable trust qualifies | Refer to attorney and actuary |
| R-ET-VALUE | Valuation opinion for real estate, a business or art | Refer to a qualified appraiser |
| R-ET-AUDIT | Estate or gift tax examination | Refer to a credentialed representative |
| R-ET-STATE | State estate or inheritance tax return | `us-state-estate-and-inheritance-tax-matrix` |
| R-ET-PROPREG | Planning that depends on the 2022 proposed anti-abuse rule | Flag: not final; reviewer decides |

## Filing and payment

| Return | Due | Extension | Payment |
| --- | --- | --- | --- |
| Form 706 (2026 death) | 9 months after death | Form 4768, 6 months to file | Due at 9 months; sections 6161, 6163, 6166 |
| Form 709 (2026 gifts) | 15 April 2027 | Form 4868 or Form 8892, to 15 October 2027 | Due 15 April 2027 |
| Form 706, portability only, late | Fifth anniversary of death | Rev. Proc. 2022-32 | None due |
| Form 8971 | Filed separately from Form 706 when Form 706 is required | None | Not applicable |

Reviewer brief to deliver: forms, due dates and extension status, e-file or paper, payment method and amount; the full computation (Form 706 from gross estate to net tax; Form 709 cumulative history and tax; GST inclusion ratios and allocations); each schedule tied to source documents (appraisals, statements, deeds, Form 712, K-1s) with any discount and the appraiser named; the elections (portability, alternate valuation with its section 2032(c) test, QTIP, reverse QTIP, 529 election, gift splitting, GST allocations by gift); anti-clawback and basis trade-off notes; state points (domicile, filing duty, state portability); open items (appraisals, donee TINs, Crummey notices, Notice of Consent, sections 2036 to 2042 review); a citation for every line.

## Completion checklist

- Citizen, resident or non-resident status confirmed for decedent or donor and spouse.
- Date of death or gift confirmed in 2026, or the right year's figures used.
- Form 706 filing test run on gross estate plus adjusted taxable gifts against USD 15,000,000.
- Surviving spouse alive at filing if portability is elected; late election within 5 years.
- Every Schedule M item passes to the spouse and is not a non-deductible terminable interest; QTIP elected where wanted; QDOT in place for a non-citizen spouse.
- Each Form 709 gift has donee, date, value, basis and present-interest status; future interests carry no exclusion.
- Gift splitting: both spouses citizens or residents and married through the year; Notice of Consent attached.
- 529 election shows the five-year spread and the donor was told no more exclusion is left for that donee.
- GST: automatic allocation accepted, elected out, or allocated, gift by gift.
- Prior Form 709s collected and adjusted taxable gifts reconciled.
- Alternate valuation passes section 2032(c).
- Gifts meant to be completed in a year were delivered and accepted in that year.
- Large SLAT gifts backed by an attorney's drafting memo on section 2036 and the reciprocal trust doctrine.
- Appraisals attached where required.
- State estate tax return identified through the state skill.
- Form 8971 filed when Form 706 is required.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Rev. Proc. 2025-32. Read for section 3.14 (BEA and GST exemption USD 15,000,000 under section 70106), 4.41 (section 2032A USD 1,460,000), 4.42 (USD 19,000 and USD 194,000) and 4.51 (section 6166 USD 1,940,000). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Instructions for Form 706 (Rev. July 2026), for decedents dying after 31 December 2025. Read for What's New (USD 15,000,000; USD 1,460,000; USD 1,940,000; basic credit USD 5,945,800), Which Estates Must File, When To File, portability and Rev. Proc. 2022-32, Where To File, Table A, alternate valuation on a late return, the 2% portion, Form 8971 and the e-file forms. | https://www.irs.gov/pub/irs-pdf/i706.pdf | 2026-11-13 |
| Instructions for Form 709 (2025). Read for MeF e-filing, the Part III spouse's consent and the one-spouse filing exception, Form 8892 and Form 4868, where to file. | https://www.irs.gov/pub/irs-pdf/i709.pdf | 2026-11-13 |
| Rev. Proc. 2022-32. Read for section 4.01 (filing on or before the fifth anniversary of death and the heading to write). | https://www.irs.gov/pub/irs-drop/rp-22-32.pdf | 2026-11-13 |
| Public Law 119-21, section 70106. Read for the USD 15,000,000 amount, the 2025 indexing base and the striking of section 2010(c)(3)(C), for decedents dying and gifts made after 31 December 2025. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 6075 (govinfo). Read for (a) 9 months, (b) 15 April and the income tax extension rule. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6075.htm | 2026-11-13 |
| 26 U.S.C. 2641 (govinfo). Read for the applicable rate as the maximum estate tax rate times the inclusion ratio. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapE-sec2641.htm | 2026-11-13 |
| 26 U.S.C. 2503 (govinfo). Read for (e) direct tuition and medical payments. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapA-sec2503.htm | 2026-11-13 |
| 26 U.S.C. 2513 (govinfo). Read for the one-half rule and the citizen or resident condition. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapB-sec2513.htm | 2026-11-13 |
| 26 U.S.C. 2523 (govinfo). Read for the marital deduction and (i) the non-citizen spouse. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapC-sec2523.htm | 2026-11-13 |
| 26 U.S.C. 2631 (govinfo). Read for the GST exemption tied to the basic exclusion amount. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapD-sec2631.htm | 2026-11-13 |
| 26 U.S.C. 2032 (govinfo). Read for the 6-month date and (c) the decrease test. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partIII-sec2032.htm | 2026-11-13 |
| Federal Register document 2022-08865 (REG-118913-21), read through the Federal Register API. Read for the title, the abstract (proposed amendments) and the citation 87 FR 24918. | https://www.federalregister.gov/documents/2022/04/27/2022-08865/estate-and-gift-taxes-limitation-on-the-special-rule-regarding-a-difference-in-the-basic-exclusion | 2026-11-13 |

Not yet confirmed: the 2026 Form 709 and its instructions were not yet published when read, so Form 709 line and part references are from the 2025 edition; the 5% exception in the 2022 proposed anti-abuse rule could not be re-read (the full-text page refused the request) and is carried from the old file; the USD 2 million QDOT security threshold, the section 6166 35% and 45% rules, the 37.5-year generation rule, the USD 13,000 non-resident credit and the treaty country list were not re-read today and are carried from the old file.
