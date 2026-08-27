---
name: us-estate-gift-706-709
description: Tier 2 US federal content skill for the unified estate, gift, and generation-skipping transfer tax under §§ 2001 et seq., including Form 706 (estate), Form 709 (gift), and the GST regime. Covers tax year 2025 with the $13.99M per-individual basic exclusion amount, the 40% top rate, the $19,000 annual exclusion, §2513 gift splitting, §2010(c) portability and DSUE with the Rev. Proc. 2022-32 5-year late-election relief, §2503(e) unlimited medical/tuition direct payments, §529 5-year frontload election ($95k/donee), §2032 alternate valuation, §1014 stepped-up basis, the GST regime under § 2601, and the December 31, 2025 TCJA-doubling sunset to ~$7M with anti-clawback T.D. 9884.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Christopher Aryee
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Estate Gift 706 709

## US Estate, Gift & Generation-Skipping Transfer Tax — Form 706 / Form 709

> **Tier 2 federal content skill.** Provides the substantive law, current-year figures, and form line references for the US unified transfer tax system. Workflow scaffolding, intake structure, conservative defaults, self-checks, and reviewer brief format come from `us-tax-workflow-base` (Tier 1). **MUST be loaded alongside `us-tax-workflow-base` v0.2 or later.** Every output produced under this skill requires sign-off by a Circular 230 practitioner (EA, CPA, or attorney admitted to practice before the IRS). Federal only — state estate and inheritance taxes are addressed at an overview level in Section 12 and require separate state-specific content skills for final preparation.

## 1. Scope

### 1.1 In scope

- **Form 706 requirement** — Required when the gross estate plus adjusted taxable gifts of a US citizen or US resident decedent exceeds the basic exclusion amount (BEA) at the date of death, and also filed solely to elect portability of the deceased spousal unused exclusion (DSUE) under §2010(c)(5)(A).  _(§2010(c)(5)(A))_
- **Form 709 requirement** — Required for any donor who, in the calendar year, made gifts in excess of the annual exclusion to any one donee, made gifts of future interests of any amount, elected gift splitting under §2513, made a §529 5-year frontload election, or allocated GST exemption.  _(§2513)_
- **GST tax scope** — GST tax (Chapter 13 of the Internal Revenue Code). Direct skips reported on Form 706 Schedule R or Form 709 Schedule D; taxable distributions on Form 706-GS(D); taxable terminations on Form 706-GS(T).  _(Chapter 13, Internal Revenue Code)_
- **TCJA sunset and anti-clawback coverage** — The permanent $15,000,000 basic exclusion amount effective January 1, 2026 (OBBBA, P.L. 119-21, § 70106), which neutralized the TCJA-doubling sunset previously scheduled for December 31, 2025, and the planning landscape created by the anti-clawback final regulation under T.D. 9884.  _(T.D. 9884)_
- **Basis coordination** — Coordination with the income tax basis rules under §1014 (step-up at death) and §1015 (carryover for inter vivos gifts).  _(§1014; §1015)_
- **Portability election mechanics** — Portability election mechanics including the Rev. Proc. 2022-32 simplified 5-year extension for estates not otherwise required to file.  _(Rev. Proc. 2022-32)_

### 1.2 Out of scope

- **Form 1041 fiduciary income tax** — Form 1041 — Income tax of the estate or trust. Fiduciary income tax is a separate regime under Subchapter J; addressed by `us-form-1041-fiduciary-income` (not yet released).  _(Subchapter J)_
- **State estate, inheritance, and gift taxes** — Covered at overview level only (see Section 12); each affected state requires its own Tier 2 skill for filing.
- **Non-resident alien decedent returns on Form 706-NA** — Mentioned in Section 13 but not produced under this skill; the §60,000 NRA exemption and treaty modifications are sufficiently jurisdiction-specific to warrant dedicated review.  _(§60,000 NRA exemption)_
- **QDOT regulations under §2056A** — Qualified domestic trust (QDOT) regulations under §2056A for non-citizen surviving spouses. Mentioned in Section 7.5; technical QDOT drafting and Schedule M election require a trust and estate attorney.  _(§2056A)_
- **Private letter rulings** — Late portability elections more than 5 years after death, §9100 relief for missed allocations of GST exemption beyond automatic allocation, and split-interest charitable trust qualifications all require a PLR — not produced here.  _(§301.9100)_
- **Section 6166 estate tax installment payments** — Estate tax installment payments for closely held business interests. Mentioned in Section 8.7 but the deferral election and bond/lien negotiation with IRS Estate and Gift Tax Group require specialist review.  _(§6166)_
- **Special use valuation under §2032A** — Mentioned in Section 9 but the 10-year recapture period and qualified heir tracking are out of scope.  _(§2032A)_
- **Generation-skipping technical exceptions** — Beyond direct skips and routine indirect skips with automatic allocation — predeceased ancestor exception under §2651(e), reverse QTIP planning, and ETIP rules are surveyed in Section 10 but complex allocation patterns must be reviewed by a credentialed practitioner.  _(§2651(e))_
- **Valuation discount disputes** — Family limited partnership and minority/marketability discounts under §2031 are mentioned in passing; appraisal review and §2704 disregarded restrictions are out of scope.  _(§2031; §2704)_

### 1.3 Audience

The intended consumer is a Circular 230 practitioner (EA, CPA, or estate-and-trust attorney) using openaccountants.com to draft a return or a planning memorandum. Output from this skill is **always** a reviewer brief plus draft forms, never a final return delivered directly to the client or filed with the IRS.

## 2. Unified Rate Structure and Exemption Amount — Tax Year 2025

### 2.1 The unified credit and the basic exclusion amount

- **Unified transfer tax system definition** — The estate tax (§§ 2001–2058), the gift tax (§§ 2501–2524), and the GST tax (§§ 2601–2664) operate as a single unified transfer tax system. A single lifetime exemption — the basic exclusion amount (BEA) under §2010(c)(3) — applies to cumulative taxable gifts during life and to the taxable estate at death.  _(§2010(c)(3))_

**2025 BEA and related figures**  _(Rev. Proc. 2024-40; IRS news release of October 22, 2024)_

| Item | 2024 | **2025** |
| --- | --- | --- |
| Basic exclusion amount per individual | $13,610,000 | **$13,990,000** |
| Effective exemption per married couple (with portability) | $27,220,000 | **$27,980,000** |
| Annual gift exclusion per donee under §2503(b) | $18,000 | **$19,000** |
| Annual exclusion for gifts to non-citizen spouse under §2523(i)(2) | $185,000 | **$190,000** |
| Section 6166 2% portion ceiling for closely held businesses | $1,850,000 | **$1,900,000** |

- **Rounding rule** — All figures other than the §2523(i) and §6166 amounts continue to be rounded to the nearest $10,000 under §2010(c)(3)(B)(ii).  _(§2010(c)(3)(B)(ii))_

### 2.2 The tax rate table — §2001(c)

- **Effective rate note** — The tax is computed on a graduated table running from 18% on the first $10,000 of taxable transfers to 40% on amounts in excess of $1,000,000. Because the unified credit shelters the full BEA, the graduated brackets between 18% and 40% are subsumed within the credit and only the 40% top bracket has economic effect for any taxable estate or taxable gift in 2025.  _(§2001(c))_

**§2001(c) rate table**  _(§2001(c))_

| Taxable transfer | Rate at top of bracket |
| --- | --- |
| $0 – $10,000 | 18% |
| $10,000 – $20,000 | 20% |
| $20,000 – $40,000 | 22% |
| $40,000 – $60,000 | 24% |
| $60,000 – $80,000 | 26% |
| $80,000 – $100,000 | 28% |
| $100,000 – $150,000 | 30% |
| $150,000 – $250,000 | 32% |
| $250,000 – $500,000 | 34% |
| $500,000 – $750,000 | 37% |
| $750,000 – $1,000,000 | 39% |
| Over $1,000,000 | **40%** |

For all practical purposes, the working rate is 40%. Every reviewer brief should state the marginal and effective rates in 2025 dollars.

### 2.3 The applicable credit amount

- **AEA formula** — AEA = BEA + DSUE + Restored exclusion amount (rarely applicable)  _(§2010(c)(2))_
- **2025 applicable credit amount** — For a single decedent or unmarried donor in 2025, AEA = BEA = $13,990,000, producing an applicable credit amount of $5,389,800 (the tentative tax on $13,990,000 under §2001(c)).  _(§2010(c)(2); §2001(c))_

### 2.4 The "Form 706 Method" — interaction of lifetime gifts and the estate

- **Estate tax computation under §2001(b)** — Estate tax = Tentative tax on (Taxable estate + Adjusted taxable gifts) − Gift tax that would have been payable on lifetime gifts at date-of-death rates − Applicable credit amount (AEA-based) − Other credits (state death tax credit is repealed; foreign death tax credit and prior-transfer credit remain)  _(§2001(b))_
- **Recomputation mechanics** — The recomputation of the gift tax at date-of-death rates is critical: it neutralizes the bracket-arbitrage that would otherwise arise if rates changed between the gift and the death. For decedents dying in 2025, since the top rate has been 40% throughout the entire post-2012 period, the recomputation is mechanical.  _(§2001(b))_

## 3. The December 31, 2025 TCJA Sunset and Planning Urgency

### 3.1 The sunset itself

- **TCJA doubling and sunset** — The Tax Cuts and Jobs Act of 2017 (P.L. 115-97) doubled the §2010(c)(3) BEA from $5,000,000 (indexed) to $10,000,000 (indexed) for decedents dying and gifts made after December 31, 2017 and before January 1, 2026. Section 11061(a) of TCJA enacted §2010(c)(3)(C), the sunset clause, under which the BEA would have reverted to $5,000,000 indexed for transfers after December 31, 2025. The sunset never took effect: § 70106 of the OBBBA (P.L. 119-21, enacted July 4, 2025) made the increased exclusion permanent at $15,000,000 from 2026.  _(P.L. 115-97; §11061(a); §2010(c)(3)(C))_
- **OBBBA did not extend sunset** — The One Big Beautiful Bill Act (OBBBA, P.L. 119-21, enacted July 4, 2025) eliminated the §2010(c)(3)(C) sunset and made the increased exemption permanent. Section 70106 amended §2010(c)(3) to set the basic exclusion amount at $15,000,000 for decedents dying and gifts made after December 31, 2025, indexed for inflation for calendar years after 2026. The scheduled reversion to $5,000,000 (indexed) never took effect.  _(P.L. 119-21; §2010(c)(3)(C))_

### 3.2 Estimated 2026 BEA

- **Projected 2026 BEA figures** — The 2026 BEA is fixed by statute, not projected: $15,000,000 per individual and $30,000,000 per married couple with portability. Section 70106 of P.L. 119-21 amended §2010(c)(3)(A) to provide: "For purposes of this subsection, the basic exclusion amount is $15,000,000." The amount is indexed for inflation for calendar years after 2026 (2025 base year); the 2025 BEA remains $13,990,000 (Rev. Proc. 2024-40).  _(§1(f)(3))_

### 3.3 The anti-clawback final regulation — T.D. 9884

- **Anti-clawback rule §20.2010-1(c)** — In November 2019, the IRS finalized §20.2010-1(c) (T.D. 9884) providing that if a decedent's estate computes its estate tax using a BEA at death that is lower than the BEA in effect when a gift was made, the AEA used in the §2001(b)(2) gift-tax credit computation is the larger of the two BEAs. Because § 70106 of the OBBBA (P.L. 119-21) made the BEA permanent at $15,000,000 from 2026, no reversion occurs under current law; the rule remains relevant as protection against any future statutory reduction of the BEA.  _(T.D. 9884; §20.2010-1(c); §2001(b)(2))_
- **Use it or lose it** — The "use it or lose it" pressure ended with the OBBBA: under § 70106 of P.L. 119-21 a donor who makes no large gift before 2026 and then dies in 2026 still has the permanent $15,000,000 BEA available to shelter the estate. The urgency returns only if a future statute reduces the BEA.  _(T.D. 9884)_
- **Top of the stack principle** — Anti-clawback only protects gifts that consumed exclusion above the BEA in effect at death. Gifts under the BEA at death are absorbed first; only the excess generates the §20.2010-1(c) protection. This is the so-called "use the top of the stack" principle. With the BEA made permanent at $15,000,000 from 2026 by § 70106 of P.L. 119-21, the rule matters only if a future statute reduces the BEA below a donor's cumulative gifts.  _(§20.2010-1(c))_
- **2022 amendment anti-abuse rule** — In April 2022 the IRS published T.D. 9884 amending §20.2010-1(c)(3) to add an anti-abuse rule preventing certain transfers that are includible in the gross estate under §§2035–2042 (i.e., transfers with retained interests or strings) from generating the anti-clawback protection. Practical effect: an aggressive "gift" that is in substance not a completed transfer — for example, an outright gift followed by a side agreement retaining benefits — does not lock in the doubled BEA.  _(T.D. 9884; §20.2010-1(c)(3); §§2035–2042)_

### 3.4 Planning structures (overview only)

**Planning structures overview table**

| Structure | Mechanism | Why used pre-sunset |
| --- | --- | --- |
| **SLAT — Spousal Lifetime Access Trust** | Donor gifts to irrevocable trust naming the other spouse as discretionary beneficiary | Uses BEA while preserving indirect economic access; reciprocal SLATs require care to avoid the reciprocal trust doctrine |
| **Dynasty trust** | Long-duration GST-exempt trust in a jurisdiction that has abolished or extended the rule against perpetuities (DE, SD, NV, AK, TN, etc.) | Allocates GST exemption while the inflation-doubled GST exemption is in effect; benefits compound across multiple generations |
| **Gift-back-to-trust / IDGT installment sale** | Donor sells appreciating asset to a grantor trust in exchange for a low-interest promissory note at the §7520 / §1274 rate | Freezes value at sale date; future appreciation accrues inside the trust outside the donor's estate; grantor pays the income tax, further depleting the estate |
| **GRAT — Grantor Retained Annuity Trust** | Donor transfers asset to a trust retaining an annuity stream at the §7520 rate | Zero-out GRATs use no exemption; only excess return passes free; ideal for assets expected to outperform §7520 |
| **QPRT — Qualified Personal Residence Trust** | Donor transfers residence to a trust retaining use for a term of years | Discounted gift value; donor must survive the term or value is in the estate under §2036 |
| **CLAT — Charitable Lead Annuity Trust** | Charity receives annuity stream; remainder to family | Useful when §7520 rate is low; remainder passes at discounted gift value |

### 3.5 The "DSUE preservation" alternative for moderate estates

For decedents with estates below the 2025 BEA but where the surviving spouse may have appreciable assets approaching the post-sunset BEA, filing Form 706 solely to elect portability preserves the deceased spouse's full unused BEA at the 2025 level. Rev. Proc. 2022-32 makes this election available without a PLR for 5 years after death. See Section 5.

## 4. Annual Exclusion, Medical/Education Exception, Gift-Splitting, and §529 Frontload

### 4.1 The annual exclusion — §2503(b)

- **2025 annual exclusion amount** — For 2025, a donor may give up to $19,000 per donee per year free of gift tax, without consuming any BEA, provided the gift is of a present interest.  _(§2503(b))_
- **Per donee per year** — Per donee, per year. A donor with three children can give $19,000 to each ($57,000 total) annually with no Form 709 filing required (subject to the §2513 split-gift complication discussed below).  _(§2503(b))_
- **Present interest requirement / Crummey** — Present interest required. Gifts in trust generally fail the present-interest test unless the beneficiary has a Crummey withdrawal right (a temporary unrestricted right to withdraw the contribution, typically 30–60 days). Reviewer must confirm proper Crummey notices were sent.  _(§2503(b))_
- **Future interests do not qualify** — Future interests — including most gifts to a trust without Crummey powers, remainder interests, and reversionary interests — do not qualify for the annual exclusion and require Form 709 regardless of dollar amount.  _(§2503(b))_
- **No carryover** — Carryover does not apply. Unused annual exclusion in 2025 evaporates on December 31, 2025; it does not carry forward.  _(§2503(b))_

### 4.2 The §2503(e) medical and education exception

- **Unlimited exclusion for direct payments** — Under §2503(e), direct payments of qualifying medical expenses and tuition are excluded from the gift tax in unlimited amounts and do not count against the annual exclusion or the BEA.  _(§2503(e))_
- **Direct payment to provider requirement** — Payment must be made directly to the provider — the medical institution, the doctor, or the educational institution. Payment to the beneficiary (even with documentation showing they paid the provider) does not qualify and reverts to a normal gift.  _(§2503(e))_
- **Qualifying medical expenses** — Medical: any expense described in §213(d) — diagnosis, cure, mitigation, treatment, or prevention of disease, including health insurance premiums. Excludes amounts reimbursed by insurance.  _(§213(d))_
- **Qualifying education expenses** — Education: tuition only. Room, board, books, supplies, fees, and other costs of attendance do not qualify and must be funded through the annual exclusion, §529 frontload, or BEA.  _(§2503(e))_
- **No beneficiary restrictions** — No age, family relationship, or US citizen requirement for the beneficiary.  _(§2503(e))_
- **Not reported on Form 709** — The §2503(e) payment is not reported on Form 709.  _(§2503(e))_

### 4.3 Gift-splitting — §2513

- **Gift-splitting effect** — A married couple may elect to treat all gifts made by either spouse during the calendar year as made one-half by each spouse. The effect is to double the annual exclusion ($38,000 per donee in 2025) and to share the BEA across both spouses.  _(§2513)_
- **Requirement — citizenship/residency** — Both spouses must be US citizens or residents at the time of the gift.  _(§2513(a))_
- **Requirement — marriage status** — Both spouses must be married to each other at the time of the gift and either remain married throughout the calendar year or, if divorced before year-end, neither remarry before year-end.  _(§2513(a))_
- **Election applies to all gifts** — The election applies to all gifts made by either spouse during the year — it is not selective. Exception: gifts in which the non-donor spouse has any interest (other than as a remainderman) cannot be split.  _(§2513(a))_
- **Election mechanics on Form 709** — The election is made on Form 709, Page 1, by checking the box on Line 12 and obtaining the consenting spouse's signature on Line 18.  _(Form 709, Line 12, Line 18)_
- **Both spouses must file** — Both spouses must file Form 709 in any year the election is made if either spouse made a gift exceeding $19,000 to any one donee. The non-donor spouse files a return showing the deemed half-gifts.  _(§2513)_

A common review error: a couple making gifts only at or below the $19,000 annual exclusion does not need to split, because each spouse's gifts are already under the annual exclusion individually. Splitting is needed when one spouse makes a gift between $19,001 and $38,000 from separate property, or when one spouse made the gift from joint or community property where the deemed allocation is otherwise unclear.

### 4.4 The §529 5-year frontload election — §529(c)(2)(B)

- **Frontload maximum** — A donor may elect to treat contributions to a §529 qualified tuition program in excess of the annual exclusion as made ratably over a five-year period beginning with the year of contribution. For 2025, the maximum frontload is 5 × $19,000 = $95,000 per donee from a single donor (or $190,000 per donee if both spouses gift-split).  _(§529(c)(2)(B))_
- **Election mechanics** — Election is made on Form 709, Schedule A, by checking the appropriate box and listing one-fifth in each of the five years.  _(Form 709, Schedule A)_
- **Filing requirement even if no tax due** — Form 709 must be filed for the contribution year even if no gift tax is due, because the election itself is a return requirement.  _(§529(c)(2)(B))_
- **No additional annual exclusion during 5-year period** — No additional annual exclusion is available to that donee for that §529 account during the five-year period. Other gifts to the same donee outside the §529 still consume the annual exclusion; but if the §529 frontload has already absorbed the annual exclusion for the year, additional non-§529 gifts consume BEA.  _(§529(c)(2)(B))_
- **Donor death during frontload period** — If the donor dies before the end of the five-year period, the portion attributable to years after death is included in the gross estate under §529(c)(4)(C). The portion attributable to the year of death and prior years is permanently excluded.  _(§529(c)(4)(C))_

### 4.5 Annual exclusion for non-citizen spouse — §2523(i)

- **Enhanced annual exclusion for non-citizen spouse gifts** — $190,000 for 2025 USD  _(§2523(i)(2))_
- **Non-citizen spouse marital deduction denial** — Gifts from a US-citizen donor to a non-US-citizen spouse do not qualify for the unlimited §2523(a) marital deduction. Instead, §2523(i)(2) provides an enhanced annual exclusion of $190,000 for 2025 (in lieu of the $19,000 figure). Gifts above this amount consume BEA.  _(§2523(a); §2523(i)(2))_

## 5. Portability and DSUE — §2010(c)(4) and Rev. Proc. 2022-32

### 5.1 The portability concept

- **Portability concept** — Section 2010(c)(4), enacted by ATRA 2012, permits a surviving spouse to add the deceased spousal unused exclusion (DSUE) of the most recently deceased spouse to the survivor's own BEA. The combined amount is the surviving spouse's applicable exclusion amount (AEA) and is available against gifts during life and against the estate at death.  _(§2010(c)(4))_
- **DSUE formula** — DSUE = BEA of deceased spouse at death − (Taxable estate + adjusted taxable gifts of deceased spouse)  _(§2010(c)(4))_
- **DSUE cap** — Cap: the DSUE may not exceed the BEA of the first-deceased spouse at the time of his or her death.  _(§2010(c)(4))_

### 5.2 The "last deceased spouse" rule — §2010(c)(4)(B)(i)

- **Last deceased spouse rule** — The surviving spouse may only use DSUE from the most recently deceased spouse. If the surviving spouse remarries and the new spouse dies first, the DSUE from the prior spouse is lost (subject to a "use it or lose it" rule — DSUE consumed by gifts before the new spouse's death is locked in).  _(§2010(c)(4)(B)(i))_

### 5.3 How portability is elected — Form 706

- **Timely filing requirement** — Portability is elected by the timely filing of a complete and properly prepared Form 706 by the executor of the deceased spouse's estate. "Timely" means within 9 months of death plus the automatic 6-month extension on Form 4768.  _(Form 4768)_
- **Simplified valuation method for portability-only filings** — A Form 706 filed solely for portability where the gross estate is below the BEA may use the simplified valuation method under §20.2010-2(a)(7)(ii): the executor reports estimated values rounded to the nearest $250,000 for property that qualifies for the marital or charitable deduction. Property generating tax (i.e., not deducted) must still be reported at full FMV.  _(§20.2010-2(a)(7)(ii))_

### 5.4 Late portability election — Rev. Proc. 2022-32

- **5-year relief period** — For estates not otherwise required to file Form 706 (i.e., the gross estate plus adjusted taxable gifts is below the BEA), Rev. Proc. 2022-32 (released July 8, 2022) replaced Rev. Proc. 2017-34 and extended the simplified relief period to 5 years after the decedent's date of death.  _(Rev. Proc. 2022-32; Rev. Proc. 2017-34)_
- **Qualification requirements** — 1. The decedent must have been survived by a spouse, must have been a US citizen or resident, and must not have been required to file Form 706 for any reason other than electing portability. 2. The executor files a complete and properly prepared Form 706 within 5 years of death. 3. The return must state at the top: "FILED PURSUANT TO REV. PROC. 2022-32 TO ELECT PORTABILITY UNDER §2010(c)(5)(A)".  _(Rev. Proc. 2022-32; §2010(c)(5)(A))_
- **No PLR or user fee required** — This relief does not require a private letter ruling or user fee. After 5 years, the only remaining route is a PLR under §301.9100-3 — typically expensive and uncertain.  _(§301.9100-3)_

### 5.5 When NOT to elect portability

- **Cost of preparation** — Cost of preparation. A Form 706 even at simplified valuations involves substantial work.
- **Statute of limitations exposure** — Filing Form 706 starts the §6501 3-year statute on the entire estate (subject to the §2010(c)(5)(B) special rule allowing the IRS to examine the DSUE computation any time before the surviving spouse's estate is examined).  _(§6501; §2010(c)(5)(B))_
- **Last-deceased-spouse risk** — If the surviving spouse is likely to remarry and outlive a new spouse, the portability of the first spouse may be lost anyway.
- **State residency limitation** — Some states (e.g., Massachusetts) do not permit portability of the state exemption; the federal election does not save state estate tax.

For most clients with a surviving spouse and combined assets approaching or exceeding the BEA, portability should be elected.

### 5.6 The "examination of DSUE" exception — §2010(c)(5)(B)

- **Examination exception** — The IRS may examine the deceased spouse's return at any time the DSUE is being used by the surviving spouse, even after the §6501 statute would otherwise have closed the deceased spouse's return. Practical effect: the deceased spouse's Form 706 records must be retained until the surviving spouse's estate is closed.  _(§2010(c)(5)(B); §6501)_

## 6. Form 709 — Gift Tax Return Mechanics

### 6.1 When Form 709 is required

- **Filing triggers list** — A US citizen or resident must file Form 709 for any calendar year in which the donor: 1. Made a gift to any one donee exceeding the annual exclusion ($19,000 in 2025); 2. Made a gift of a future interest of any amount; 3. Made a gift in a calendar year and is electing gift splitting under §2513; 4. Made a §529 frontload election; 5. Made a gift to a trust that is or could be subject to GST (so that GST exemption is allocated or affirmatively not allocated); 6. Made a gift to a non-citizen spouse exceeding the §2523(i)(2) enhanced annual exclusion ($190,000 in 2025); 7. Made any gift in trust other than a Crummey-power trust where the present-interest test is clearly satisfied at the annual exclusion level for each beneficiary.  _(§2513; §2523(i)(2))_

### 6.2 Due date

- **Form 709 due date and extensions** — Form 709 is due April 15 of the year following the gift. An automatic 6-month extension to October 15 is available by: Filing Form 4868 for the donor's Form 1040 (which also extends the Form 709), or Filing Form 8892 (the gift-tax-only extension), or Filing Form 4768 if the donor died during the year and the executor is filing on the donor's behalf.  _(Form 4868; Form 8892; Form 4768)_
- **Extension to file is not extension to pay** — Note that an extension of time to file is not an extension of time to pay. Gift tax owed accrues interest from April 15.

### 6.3 Form 709 structure

**Form 709 structure table**

| Section | Content |
| --- | --- |
| Page 1 | Donor information; gift-splitting election (Lines 12, 17, 18); summary computation (Lines 1–20) |
| Schedule A — Part 1 | Gifts subject only to gift tax (no GST) |
| Schedule A — Part 2 | **Direct skips** subject to both gift tax and GST |
| Schedule A — Part 3 | **Indirect skips** subject to gift tax that may later be subject to GST |
| Schedule A — Part 4 | Taxable gift reconciliation |
| Schedule B | Gifts from prior periods (cumulative tracking) |
| Schedule C | **Deceased Spousal Unused Exclusion (DSUE)** — claimed by surviving spouse using DSUE on lifetime gifts |
| Schedule D — Part 1 | GST exemption reconciliation |
| Schedule D — Part 2 | GST exemption allocation |
| Schedule D — Part 3 | GST tax computation on direct skips |

### 6.4 Schedule A — gift listing

- **Required gift listing items** — For each gift, the donor reports: Item number; Donee's name, address, and relationship (and donee's SSN if the donor wishes to claim the §2503(c) minor's-trust exclusion — generally good practice to provide regardless); Description (e.g., "10,000 shares of Apple Inc. common stock", "Undivided 1/3 interest in 123 Main St., Phoenix AZ 85001"); Date of gift; Adjusted basis (relevant for carryover-basis computations under §1015); Date acquired; Value at date of gift; For split gifts: indication that this is the donor's half (the other half appears on the consenting spouse's Form 709).  _(§2503(c); §1015)_

### 6.5 Cumulative computation — the §2502 mechanic

- **Tentative tax formula** — Tentative tax = Tax on (cumulative taxable gifts including current year) − Tax on (cumulative taxable gifts through prior year) − Unused applicable credit amount  _(§2502(a))_
- **Bracket-arbitrage note** — Because the rate schedule is graduated, current-year gifts are pushed into the higher 40% bracket once cumulative taxable gifts exceed $1,000,000. In 2025, given the $13.99M BEA, no donor will pay actual gift tax until cumulative taxable gifts exceed the BEA — but the credit-consumption tracking on Schedule B from prior periods is essential.  _(§2502(a))_

### 6.6 Allocation of GST exemption — Schedule D

- **Automatic allocation for direct skips** — Direct skips (gifts to a "skip person" — grandchild, more remote descendant, or a non-relative more than 37.5 years younger than the donor) — exemption allocation is automatic under §2632(b) unless the donor elects out.  _(§2632(b))_
- **Automatic allocation for indirect skips** — Indirect skips (gifts to a "GST trust" that may later distribute to skip persons) — exemption allocation is automatic under §2632(c) unless the donor elects out; this rule applies regardless of whether the gift is to a present-interest or future-interest trust.  _(§2632(c))_
- **Elect in/out mechanics** — The donor may elect in or out of automatic allocation on Schedule D Part 2 by checking the appropriate box. Affirmative allocation in writing (filed by the due date) is treated as an election in; non-filing or affirmative election out leaves the gift unallocated, in which case GST applies at the later taxable distribution or termination.  _(Schedule D Part 2)_
- **Curing missed allocation** — A missed allocation may be cured by: 1. A late allocation on a subsequent Form 709 (effective on the filing date, with revaluation under §2642(d)); or 2. §9100 relief (out of scope here).  _(§2642(d); §9100)_

### 6.7 Filing logistics

- **Where to file** — Where to file (2025): Internal Revenue Service Center, Kansas City, MO 64999 (verify in current Form 709 instructions; the address has occasionally changed).
- **E-filing availability** — Form 709 was added to the IRS Modernized e-File system in 2023 and is now widely supported by commercial software. Paper filing remains acceptable.
- **Payment methods** — Electronic via EFTPS, IRS Direct Pay (limit $10M per transaction), or check with Form 1040-V-equivalent (no separate gift-tax voucher; identify the payment in the memo line).

## 7. Form 706 — Estate Tax Return Mechanics

### 7.1 When Form 706 is required

- **Filing triggers** — A Form 706 is required when: 1. The gross estate plus adjusted taxable gifts exceeds the BEA ($13,990,000 in 2025); or 2. The executor wishes to elect portability under §2010(c)(5)(A); or 3. The executor wishes to elect alternate valuation under §2032 (which requires a return regardless of size); or 4. The estate qualifies for and the executor elects §6166 deferral, §2032A special-use valuation, or a QDOT under §2056A.  _(§2010(c)(5)(A); §2032; §6166; §2032A; §2056A)_
- **§2035 add-back note** — Note: gifts made within 3 years of death that are subject to §2035 add-back (life insurance transferred within 3 years, transfers with retained interests "released" within 3 years) increase the gross estate but not the adjusted-taxable-gifts pile (the latter excludes such gifts under §2001(b) to avoid double-counting).  _(§2035; §2001(b))_

### 7.2 Due date and extensions

- **Due date and extensions** — Form 706 is due 9 months after the date of death. An automatic 6-month extension of time to file is granted upon timely filing of Form 4768. An extension of time to pay is discretionary under §6161 and requires a showing of reasonable cause.  _(Form 4768; §6161)_
- **§6166 installment election summary** — For estates qualifying under §6166 (closely held business interest > 35% of adjusted gross estate), the executor may elect to pay the qualifying portion of the estate tax in up to 10 annual installments beginning up to 5 years after the original due date, at the favorable §6601(j) "2% portion" rate on the first $1,900,000 (2025) of taxable amount above the BEA.  _(§6166; §6601(j))_

### 7.3 Form 706 structure

**Form 706 asset schedules**

| Schedule | Assets reported |
| --- | --- |
| **A** | Real estate (including out-of-state and out-of-country real property) |
| **A-1** | Section 2032A election: special-use valuation |
| **B** | Stocks and bonds (publicly traded and privately held) |
| **C** | Mortgages, notes, and cash |
| **D** | Insurance on the decedent's life (Form 712 from each insurance company is attached) |
| **E** | Jointly held property (Part 1: qualified joint interests with spouse; Part 2: all other) |
| **F** | Other miscellaneous property — tangible personal property, art, business interests, IRA/401(k) balances, partnership interests, royalties, patents |
| **G** | Transfers during life — §§2035, 2036, 2037, 2038 retained-interest transfers and 3-year-add-back items |
| **H** | Powers of appointment under §2041 |
| **I** | Annuities — §2039, including IRA-style annuities, pension survivor benefits |

**Form 706 deduction schedules**

| Schedule | Deductions reported |
| --- | --- |
| **J** | Funeral and administration expenses |
| **K** | Debts of the decedent, mortgages, and liens |
| **L** | Net losses during administration, expenses incurred on property not subject to claims |
| **M** | Bequests to a surviving spouse — §2056 marital deduction |
| **O** | Charitable, public, and similar gifts — §2055 |

**Form 706 GST and credit schedules**

| Schedule | Content |
| --- | --- |
| **P** | Credit for foreign death taxes — §2014 |
| **Q** | Credit for tax on prior transfers (PTC) — §2013 |
| **R** | GST tax — direct skips and trust skip-person determinations |
| **R-1** | GST tax for direct skip from a trust (separate form sent to the trustee for payment) |
| **U** | Qualified conservation easement exclusion — §2031(c) |
| **PC** | Protective claim for refund |

### 7.4 Schedule M — marital deduction mechanics

- **Marital deduction gating rules** — 1. Spouse must be a US citizen — otherwise the QDOT rules of §2056A apply (see Section 7.5). 2. Property must "pass" to the spouse within the meaning of §2056(c). 3. Terminable interest rule. Generally, terminable interests passing to the spouse do not qualify (§2056(b)(1)). Exception: QTIP (qualified terminable interest property) — the executor may elect under §2056(b)(7) to treat property as marital-deductible if the spouse receives all the income for life. The trade-off: the property is included in the surviving spouse's estate under §2044.  _(§2056(c); §2056(b)(1); §2056(b)(7); §2044; §2056A)_
- **QTIP election mechanics** — QTIP election is made on Schedule M by listing the property and checking the QTIP election box.  _(Schedule M)_

### 7.5 Non-citizen spouse — QDOT under §2056A

- **QDOT requirements** — If the surviving spouse is not a US citizen, the §2056 marital deduction is denied unless property passes through a Qualified Domestic Trust (QDOT) that satisfies §2056A: At least one trustee must be a US citizen or US domestic corporation; The trustee must have authority to withhold US estate tax from any distribution of corpus; The trust must satisfy security requirements set out in §20.2056A-2(d) (e.g., bond or letter of credit if QDOT assets exceed $2 million).  _(§2056; §2056A; §20.2056A-2(d))_

QDOT mechanics generate a deferred §2056A tax on corpus distributions and on the death of the non-citizen spouse. Out of scope for drafting; mentioned for issue-spotting.

### 7.6 Schedule O — charitable deduction

- **Charitable deduction basics** — The §2055 charitable deduction is unlimited as to dollar amount, but the recipient must be a qualified §170(c) charity.  _(§2055; §170(c))_
- **Charitable remainder trust requirements** — Charitable remainder trusts must meet the strict §664 requirements (annual valuation, no commutation, etc.).  _(§664)_
- **Charitable lead trust deduction** — Charitable lead trusts generate a deduction equal to the actuarial value of the charitable lead interest (using the §7520 rate at date of death or alternate valuation date).  _(§7520)_
- **Foreign charities treatment** — Foreign charities generally do not qualify under §2055(a)(2) — distinguish from §170(c) treatment for income tax. Estate tax treats foreign charity deductibility more permissively than income tax.  _(§2055(a)(2); §170(c))_

### 7.7 Computation summary — Form 706 Page 1

- **Form 706 Page 1 computation flow** — Total gross estate (sum of Schedules A through I) − Total allowable deductions (sum of Schedules J, K, L, M, O, U) = Taxable estate + Adjusted taxable gifts (post-1976 gifts not included in gross estate) = Tentative tax base × §2001(c) rate schedule = Tentative tax − Gift tax payable on adjusted taxable gifts (recomputed at DOD rates) − Applicable credit amount (based on AEA = BEA + DSUE + restored exclusion) − Credit for foreign death taxes (§2014) − Credit for tax on prior transfers (§2013, Schedule Q) = Net estate tax + GST tax payable (from Schedule R) + §4980A tax on excess retirement accumulations (repealed for deaths after 1996; ignore) = Total transfer tax  _(§2001(c); §2014; §2013; §4980A)_

### 7.8 §6166 installment payment of estate tax

- **§6166 mechanics and 2% portion rate** — For estates where the closely held business interest under §6166(b) exceeds 35% of the adjusted gross estate (gross estate minus §§2053–2054 expenses, claims, and losses), the executor may elect to defer principal for 5 years and pay the deferred tax in up to 10 annual installments starting at the end of year 5. The "2% portion" — the tax attributable to the first $1,900,000 of taxable amount above the BEA in 2025 — accrues interest at 2%. Amounts above the 2% portion accrue at 45% of the §6601(a) underpayment rate.  _(§6166(b); §§2053–2054; §6601(a))_

### 7.9 Filing logistics

- **Where to file** — Where to file: Department of the Treasury, IRS, Cincinnati, OH 45999 (verify in current instructions).
- **E-filing not available** — Form 706 is not electronically filed as of 2025. Paper filing only, certified mail with return receipt strongly recommended.
- **Payment methods** — EFTPS or check with the return.
- **Closing letter fee** — Since June 1, 2021, Form 706 closing letters are issued only upon request and payment of a $67 user fee under Rev. Proc. 2021-30; otherwise the executor must rely on the Form 4422 transcript request to confirm the return has been processed.  _(Rev. Proc. 2021-30; Form 4422)_

## 8. Alternate Valuation Date — §2032

### 8.1 The election

- **Alternate valuation date rule** — If the §2032 election is made, all property in the gross estate is valued at the earlier of: 1. The date 6 months after the decedent's date of death; or 2. The date the property is sold, exchanged, distributed, or otherwise disposed of during that 6-month period.  _(§2032)_

### 8.2 All-or-nothing

- **All-or-nothing rule** — The election applies to the entire gross estate, not to selected assets. A partial election is not permitted.  _(§2032)_

### 8.3 Pre-condition — §2032(c)

- **Pre-condition for election** — The election is permitted only if both: 1. The gross estate value decreases between the date of death and the alternate valuation date; and 2. The estate tax due decreases as a result. This second test was added by §2032(c) to prevent elections that would reduce gross estate (and step-up basis under §1014) without producing offsetting tax savings.  _(§2032(c); §1014)_

### 8.4 Mechanics

- **Election mechanics and irrevocability** — Election is made on Form 706, Part 3, Line 1 by checking "Yes" and entering the alternate valuation date column for each asset on the schedules. Election is irrevocable after the due date of the return (including extensions). Income earned by estate assets during the 6-month period (e.g., interest on bonds, dividends already declared) is not part of the gross estate at the alternate date — it is income of the estate reported on Form 1041.  _(Form 706, Part 3, Line 1)_

### 8.5 Interaction with §1014 basis

- **Basis step-up at alternate valuation date** — When alternate valuation is elected, the basis step-up under §1014(a)(2) is to the alternate valuation date value (or the disposition value, if earlier). This is generally adverse for inherited assets that subsequently appreciate, because the heirs receive a lower step-up than they would on a date-of-death valuation.  _(§1014(a)(2))_

## 9. Generation-Skipping Transfer Tax — §§ 2601–2664

### 9.1 The 40% flat rate

- **GST flat tax rate** — 40%  _(§2641(a)(1))_

**GST transfer classes table**

| Transfer | Definition | Form |
| --- | --- | --- |
| **Direct skip** | Transfer to a "skip person" subject to gift or estate tax | Form 709 Schedule D Part 3 (lifetime) or Form 706 Schedule R (deathtime) |
| **Taxable distribution** | Distribution from a trust to a skip person | Form 706-GS(D) (distributee) and 706-GS(D-1) (trustee) |
| **Taxable termination** | Termination of an interest in a trust where, immediately after, only skip persons hold interests | Form 706-GS(T) (trustee) |

### 9.2 Skip person — §2613

- **Skip person definition** — A skip person is: 1. A natural person assigned to a generation that is two or more generations below the transferor's generation (e.g., grandchildren of the transferor); or 2. A trust in which all interests are held by skip persons, or no person holds an interest and at no time can a distribution be made to a non-skip person.  _(§2613)_
- **Generation assignment rules** — For lineal descendants: by descent. For non-lineal individuals: persons born within 12.5 years of the transferor are in the transferor's generation; persons born 12.5–37.5 years after the transferor are in the children's generation; persons born more than 37.5 years after the transferor are skip persons.  _(§2613)_
- **Predeceased ancestor exception** — Predeceased ancestor exception, §2651(e): if the parent of a would-be skip person predeceased the transferor (or, in the case of collateral relatives, predeceased the transfer), the would-be skip person is moved up one generation.  _(§2651(e))_

### 9.3 GST exemption — §2631

- **GST exemption amount 2025** — $13,990,000  _(§2631)_
- **Separate allocation of GST exemption and BEA** — The GST exemption is equal to the BEA ($13,990,000 in 2025) and is unified for estate tax exemption purposes — but the allocation is separate. A donor may consume BEA on a gift to a non-skip person without consuming GST exemption, and may consume GST exemption on a direct skip without (separately) consuming BEA only if the direct skip is otherwise covered by BEA on the gift-tax side.  _(§2631)_

### 9.4 Inclusion ratio — §2642

- **Inclusion ratio formula** — Inclusion ratio = 1 − (GST exemption allocated / Value of property at transfer)  _(§2642)_
- **Inclusion ratio interpretation** — Inclusion ratio of 0 → entirely GST-exempt. Inclusion ratio of 1 → entirely GST-taxable. Inclusion ratio between 0 and 1 → partially exempt; future distributions taxed proportionally. A trust funded with allocations exactly equal to its value at transfer has an inclusion ratio of zero — the gold standard for dynasty trusts.  _(§2642)_

### 9.5 Automatic allocation rules — §2632

- **Automatic allocation — direct skips** — Direct skips: GST exemption is automatically allocated to the extent of any unused exemption, unless the donor elects out under §2632(b)(3).  _(§2632(b)(3))_
- **Automatic allocation — indirect skips** — Indirect skips to a GST trust: automatic allocation under §2632(c), unless the donor elects out under §2632(c)(5).  _(§2632(c); §2632(c)(5))_
- **GST trust definition** — "GST trust" is defined in §2632(c)(3)(B) by six tests — generally a trust where future distributions to skip persons are possible. Misclassification is common; reviewer must apply each test.  _(§2632(c)(3)(B))_

### 9.6 Reverse QTIP election — §2652(a)(3)

- **Reverse QTIP election mechanics** — Allows the first-deceased spouse's estate to be treated as the transferor for GST purposes even though the QTIP property passes through the surviving spouse's estate under §2044. Used to preserve the first spouse's GST exemption against the QTIP. Election is made on Form 706 Schedule R Part 1.  _(§2652(a)(3); §2044; Form 706 Schedule R Part 1)_

### 9.7 ETIP — §2642(f)

- **ETIP allocation deferral rule** — If property is subject to inclusion in the transferor's estate under §§2035–2042 (an "estate tax inclusion period"), GST exemption cannot be allocated during the ETIP — allocation is deferred until the ETIP closes. Common with GRATs and §2702 retained-interest trusts.  _(§2642(f); §§2035–2042; §2702)_

### 9.8 Sunset interaction

- **GST exemption sunset tie-in** — The GST exemption is tied to the estate-tax BEA and no longer sunsets: § 70106 of the OBBBA (P.L. 119-21) made the exemption permanent at $15,000,000 from 2026 (indexed after 2026). Allocations are locked when made: the inclusion ratio is computed at the time of allocation. Dynasty-trust funding completed ahead of the previously scheduled 2026 sunset remains effective.

## 10. Basis Rules — §1014 (Step-Up) and §1015 (Carryover)

### 10.1 §1014 — basis of property acquired from a decedent

- **Step-up basis rule** — Property acquired from a decedent takes a basis equal to the fair market value at the decedent's date of death (or the alternate valuation date if §2032 was elected). This is the so-called "step-up" (or step-down) in basis.  _(§1014; §2032)_
- **Property covered by step-up** — All property included in the gross estate, whether or not the estate was taxable. Property held in joint tenancy with right of survivorship — basis adjustment is on the included portion. For community property (in community-property states and in some elective community-property arrangements), §1014(b)(6) provides a double step-up on both halves at the death of either spouse. Property included under §§2036, 2038, or 2041 (retained-interest, revocable, or general-power transfers).  _(§1014(b)(6); §§2036; 2038; 2041)_
- **Property not covered by step-up** — IRD — "income in respect of a decedent" — under §691 takes carryover basis and is taxed to the recipient at ordinary income rates (subject to the §691(c) deduction for estate tax attributable to IRD). Annuities and qualified plan balances (largely IRD). Inter vivos completed gifts not pulled into the estate.  _(§691; §691(c))_

### 10.2 §1015 — basis of property acquired by gift

- **Carryover basis for gain purposes** — For gain purposes: the donor's basis, increased by §1015(d) for any gift tax paid on the appreciation portion of the gift.  _(§1015(d))_
- **Double basis rule for loss purposes** — For loss purposes: the lesser of donor's basis or FMV at date of gift (the "double basis" rule prevents transferring a built-in loss by gift).  _(§1015)_

### 10.3 Planning consequence — appreciation vs. depreciation

**Hold vs. gift comparison table**  _(§1014)_

| Asset condition | Better to hold until death | Better to gift |
| --- | --- | --- |
| Appreciated (FMV > basis) | **Yes — §1014 step-up** | No — carryover preserves the gain |
| Depreciated (FMV < basis) | No — step-down at §1014 destroys the loss | **Yes — but donee can only use loss to extent of donor's basis on a sale below FMV at gift; selling and giving cash is often better** |

### 10.4 Carryover-basis "hidden cost" of pre-sunset gifting

- **Trade-off analysis for pre-sunset gifting** — A donor considering a large pre-sunset gift of highly appreciated assets (e.g., founder stock with near-zero basis) faces a trade-off: the gift uses BEA at the doubled level, but the donee inherits carryover basis. If the donor would otherwise hold the asset until death and obtain a §1014 step-up, the gift saves estate tax at 40% but sacrifices income tax savings of (federal LTCG + NIIT + state) on the future sale of the appreciated asset — potentially 35%+ depending on state. The breakeven depends on time horizon, expected appreciation, and the income tax bracket of the donee.  _(§1014)_

For high-basis assets or assets unlikely to appreciate significantly, the trade-off favors gifting pre-sunset. For low-basis assets that have already appreciated substantially and are likely to be held long term, the §1014 step-up frequently wins — and the planning shifts to leveraged transfers (GRAT, sale to IDGT) that freeze value without consuming basis.

## 11. The Anti-Clawback Final Regulation in Detail — T.D. 9884 and 2022 Amendment

### 11.1 The general rule

- **Anti-clawback general rule** — §20.2010-1(c)(1) provides that if the BEA at the time of a gift exceeds the BEA at the donor's death, the applicable credit amount used in the estate tax computation is based on the higher of: The BEA at death (the "normal" credit), or The total BEA allowable as a credit against gift tax on the post-1976 gifts.  _(§20.2010-1(c)(1))_

### 11.2 The "top of the stack" mechanic

- **Top of the stack mechanic** — The protection applies only to the portion of cumulative lifetime gifts that exceeds the BEA at death. Mechanically: 1. Determine total post-1976 taxable gifts. 2. Determine BEA at death. 3. If total post-1976 gifts ≤ BEA at death: no anti-clawback protection needed (gifts are within the BEA anyway). 4. If total post-1976 gifts > BEA at death: the excess is protected — the estate tax computation uses an AEA equal to total post-1976 gifts (not BEA at death) for purposes of §2001(b)(2).  _(§2001(b)(2))_

Practical example: donor uses $13M of BEA in 2025 (when BEA = $13.99M); donor dies in 2027 when BEA has reverted to ~$7M. Protected gift portion = $13M − $7M = $6M; the $7M post-sunset BEA is also available to shelter the estate; total protection = $7M (BEA at death) + $6M (anti-clawback) = $13M of total transfers shielded.

### 11.3 The 2022 anti-abuse amendment

- **2022 anti-abuse amendment** — T.D. 9884 was amended in April 2022 (final regs published as T.D. 9884-A, 87 F.R. 25530) to disqualify from anti-clawback protection any transfer that is includible in the gross estate under §§ 2035, 2036, 2037, 2038, 2039, 2040, 2041, or 2042. The intent is to prevent "string-attached" gifts from generating clawback protection without being completed transfers.  _(T.D. 9884-A, 87 F.R. 25530)_
- **Insurance exception** — Exception: gifts of insurance brought back into the estate under §2035(a) by reason of transfer within 3 years of death are not disqualified — these were always pulled back into the estate and the doubled exemption was always available.  _(§2035(a))_

### 11.4 Practical implications for pre-sunset planning

- **Requirements to fully secure anti-clawback benefits** — To fully secure anti-clawback benefits, a pre-sunset gift must: 1. Be a completed gift for §2511 purposes — no retained interests, no retained powers, no implied retention of beneficial enjoyment. 2. Be made before December 31, 2025. 3. Not be a transfer described in §§ 2035–2042. (This requires careful drafting of SLATs, dynasty trusts, and GRATs to avoid §§ 2036 and 2038 inclusion.)  _(§2511; §§2035-2042; §2036; §2038)_

This is why reciprocal SLATs (each spouse creating a SLAT for the other) require careful drafting — the reciprocal trust doctrine could re-characterize the trusts as economically equivalent to retained interests, drawing them back under §2036.

## 12. State Estate, Inheritance, and Gift Tax — Overview

### 12.1 The two-tax distinction

- **Estate tax** — Imposed on the estate of the decedent; computed on the value of the estate. (Federal model.)  _(12.1 The two-tax distinction)_
- **Inheritance tax** — Imposed on the recipient; computed by reference to the relationship of the recipient to the decedent (closer relatives = lower or zero rate; non-relatives = highest rate).  _(12.1 The two-tax distinction)_

A state can have both.

### 12.2 Overview table — states with estate or inheritance tax (2025)

**States with estate or inheritance tax (2025)**  _(12.2 Overview table — states with estate or inheritance tax (2025))_

| State | Type | 2025 exemption / threshold | Top rate | Notes |
| --- | --- | --- | --- | --- |
| **Connecticut** | Estate | $13,990,000 (matches federal) | 12% | Highest state exemption; matches federal for 2025 |
| **DC** | Estate | $4,873,200 | 16% | Indexed |
| **Hawaii** | Estate | $5,490,000 | 20% | Top rate raised effective 2024 |
| **Illinois** | Estate | $4,000,000 | 16% | Not indexed; "cliff" effect at threshold |
| **Maine** | Estate | $7,000,000 | 12% | Indexed |
| **Maryland** | Estate **and** Inheritance | Estate: $5,000,000; Inheritance: no threshold | Estate 16%; Inheritance 10% | Two-tax state |
| **Massachusetts** | Estate | $2,000,000 | 16% | "Cliff" raised to $2M effective 2023 by Ch. 50 of 2023 Acts |
| **Minnesota** | Estate | $3,000,000 | 16% | Not indexed |
| **New York** | Estate | $6,940,000 | 16% | "Cliff" effect — full estate taxed if > 105% of threshold |
| **Oregon** | Estate | $1,000,000 | 16% | Lowest state threshold |
| **Rhode Island** | Estate | $1,802,431 | 16% | Indexed |
| **Vermont** | Estate | $5,000,000 | 16% | Not indexed |
| **Washington** | Estate | $2,193,000 | 20% | Top rate 20% — highest of any state |
| **Iowa** | Inheritance | — | 0% in 2025 | Phased out effective January 1, 2025 |
| **Kentucky** | Inheritance | Class A exempt | 16% Class C | Class A (immediate family) exempt; Class C non-relatives highest |
| **Nebraska** | Inheritance | $100,000 immediate family; lower others | 15% non-relatives | Reduced effective 2023 |
| **New Jersey** | Inheritance | Class A exempt | 16% non-relatives | Estate tax repealed 2018; inheritance tax remains |
| **Pennsylvania** | Inheritance | No exemption | 15% non-relatives | 4.5% lineal, 12% siblings, 15% other |

(These figures should be confirmed against current state department of revenue publications when preparing a state return. State estate-tax law has been in active flux in 2023–2025.)

### 12.3 The "decoupling" problem

- **Decoupling problem** — The federal credit for state death taxes was repealed effective 2005; states that previously imposed a pickup tax under the credit either re-coupled with new freestanding estate taxes or repealed the tax entirely. For federal Form 706 purposes, state death taxes are deductible under §2058, not credited. The deduction is taken on Form 706 Page 1 Line 3b.  _(§2058; Form 706 Page 1 Line 3b)_

### 12.4 No portability at the state level (mostly)

- **State-level DSUE portability** — Only Hawaii and Maryland allow some form of state-level DSUE portability as of 2025. The federal §2010(c) portability election is irrelevant for state purposes in all other jurisdictions. This drives state-level estate planning to use bypass trusts (credit shelter trusts) funded up to the state exemption at the first spouse's death — even where the federal portability election would seem to make a bypass trust unnecessary.  _(§2010(c))_

### 12.5 Gift tax at the state level

- **State gift tax** — Only Connecticut imposes a state gift tax as of 2025 (Conn. Gen. Stat. §§ 12-640 et seq.), with a $13,990,000 lifetime exemption that matches the federal BEA. All other states have no separate gift tax.  _(Conn. Gen. Stat. §§ 12-640 et seq.)_

## 13. Non-Resident Alien Estate Tax — Overview

### 13.1 The §60,000 exclusion for non-resident, non-citizen decedents

- **NRA estate tax exclusion** — A decedent who was neither a US citizen nor a US resident at death (a "non-resident alien" or NRA) is subject to US estate tax only on US-situs assets under §§2101–2108. The applicable credit for an NRA decedent is $13,000, which corresponds to a §2102(b) credit-equivalent exclusion of $60,000 — vastly smaller than the citizen/resident BEA.  _(§§2101-2108; §2102(b))_

### 13.2 US-situs assets

- **US-situs assets (included)** — Under §§2104 and 2105, the following are US-situs: US real property; Tangible personal property located in the US (with exceptions for property in transit); Stock of US corporations (regardless of where the share certificates are held); Debt obligations of US persons (with broad exceptions — see §2105(b) for portfolio debt and bank deposits).  _(§§2104-2105)_
- **Not US-situs assets** — Specifically not US-situs: Bank deposits in US banks not connected with a US trade or business (§2105(b)(1)); Portfolio interest debt obligations of US persons (§2105(b)(3)); Life insurance proceeds on the life of the NRA (§2105(a)).  _(§2105(b)(1); §2105(b)(3); §2105(a))_

### 13.3 Form 706-NA

- **Form 706-NA filing** — Filed by NRA executors when US-situs gross estate exceeds $60,000. Due 9 months after death. Out of scope for drafting under this skill — refer to specialist.  _(Form 706-NA)_

### 13.4 Treaty modifications

- **Estate tax treaties** — The US has estate-tax treaties with approximately 16 countries (Australia, Austria, Canada [via the income tax treaty], Denmark, Finland, France, Germany, Greece, Ireland, Italy, Japan, the Netherlands, Norway, South Africa, Switzerland, and the United Kingdom). Treaty provisions typically: Apportion the BEA between the US and the treaty country in proportion to US-situs vs worldwide assets, or Grant the NRA decedent a credit against US estate tax for foreign death taxes paid on the same property.  _(13.4 Treaty modifications)_

The Canadian "treaty" provisions are unusual — they appear in the income tax treaty but operate as estate-tax coordination provisions.

### 13.5 NRA gift tax

- **NRA gift tax scope** — NRA donors are subject to US gift tax only on gifts of US-situs tangible personal property and US real property (§2511(a) limitation). Crucially, gifts of intangibles (including US stock) by an NRA are NOT subject to US gift tax under §2501(a)(2). This generates planning opportunities — an NRA can transfer US stock by gift free of gift tax, with the donee taking carryover basis.  _(§2511(a); §2501(a)(2))_

## 14. Worked Examples

### Example 14.1 — $5 million estate; portability election only

D dies in 2025 leaving a gross estate of $5,000,000. D is survived by spouse S. D's will leaves everything to S outright. No prior gifts.

Gross estate: $5,000,000; Marital deduction (Schedule M): $5,000,000; Taxable estate: $0; Adjusted taxable gifts: $0; Tentative tax base: $0; Federal estate tax: $0.

Form 706 is not required by the threshold test because the gross estate plus adjusted taxable gifts is below the $13,990,000 BEA. However, S will likely die with assets approaching or exceeding the post-sunset BEA. Filing Form 706 solely to elect portability is strongly recommended.

- **DSUE computation** — DSUE = $13,990,000 (BEA) − $0 (taxable estate + adjusted taxable gifts) − $0 (gift tax paid) = $13,990,000  _(Example 14.1)_

S's AEA after the election: $13,990,000 (S's own BEA in 2025) + $13,990,000 (DSUE) = $27,980,000. After the 2025 sunset, S's own BEA reverts to ~$7M, but the DSUE — locked in at $13,990,000 — remains.

1. Use simplified valuation under §20.2010-2(a)(7)(ii) for marital-deduction property. 2. File Form 706 within 9 months of death + 6-month extension under Form 4768. If missed, file under Rev. Proc. 2022-32 within 5 years of death. 3. At top of return: write "FILED PURSUANT TO REV. PROC. 2022-32 TO ELECT PORTABILITY UNDER §2010(c)(5)(A)" if filing under the late-relief procedure.

Portability locks in DSUE at $13,990,000 — a benefit worth (13.99M − 7M) × 40% = ~$2.8M in expected estate tax savings if S dies after the sunset. The §2010(c)(5)(B) examination-deferral rule means D's Form 706 records must be retained until S's estate is closed. If S is likely to remarry, the last-deceased-spouse rule under §2010(c)(4)(B)(i) may forfeit the DSUE — discuss with client.

### Example 14.2 — $20 million estate; full BEA + marital deduction

D dies in 2025. D is survived by spouse S (US citizen) and three adult children. Gross estate (date-of-death values) shown in table below. D's will: $13,990,000 to a credit shelter (bypass) trust for the benefit of S during life with remainder to the children; residue outright to S. Prior gifts: D used $500,000 of BEA in 2018 on a gift to children.

**Gross estate asset table**  _(Example 14.2)_

| Asset | Value |
| --- | --- |
| Primary residence (jointly held with S) | $3,000,000 |
| Brokerage account (D's separate) | $9,000,000 |
| IRA (S is sole beneficiary) | $4,000,000 |
| Life insurance (proceeds payable to D's estate) | $2,000,000 |
| Personal effects, autos | $500,000 |
| 50% interest in family LLC (closely held real estate) | $1,500,000 |
| **Total gross estate** | **$20,000,000** |

**Analysis computation table**  _(Example 14.2)_

| Line | Amount |
| --- | --- |
| Gross estate | $20,000,000 |
| Schedule J — funeral & admin | ($200,000) |
| Schedule K — debts (residential mortgage $400k) | ($400,000) |
| Schedule M — marital deduction (residue + 1/2 JTWROS + IRA = $1.5M + $4M + remaining residue) | ($5,910,000) |
| Schedule M — bypass trust is NOT marital because it terminates at S's death without QTIP | $0 |
| Taxable estate | $13,490,000 |
| Adjusted taxable gifts (post-1976 gifts not in gross estate) | $500,000 |
| Tentative tax base | $13,990,000 |
| Tentative tax (§2001(c) at 40% top rate) | $5,389,800 |
| Less gift tax payable on adjusted taxable gifts at DOD rates | $0 (within BEA) |
| Net tentative tax | $5,389,800 |
| Less applicable credit amount (AEA = BEA only, no DSUE) | ($5,389,800) |
| **Net federal estate tax** | **$0** |

D's BEA is fully consumed: $13,490,000 to the bypass trust at death + $500,000 prior gifts = $13,990,000. Exactly matches 2025 BEA. IRA passing to S qualifies for marital deduction even though it is IRD — S will pay income tax on distributions; estate tax avoidance is preserved. Life insurance payable to the estate is fully included under §2042 — note the planning miss; an ILIT would have kept the $2M outside the estate. The 50% LLC interest may qualify for valuation discounts (minority interest + lack of marketability) — typically 25-40% combined. Requires appraisal. Not reflected in this example.

The bypass trust has remainder beneficiaries who are children (not skip persons). No GST exemption need be allocated unless the trust permits skip-person distributions (e.g., to grandchildren). If the trust does permit skip-person distributions, the executor should allocate D's full GST exemption ($13,990,000) on Schedule R to obtain inclusion ratio zero.

D used the full BEA — DSUE = $0. No portability benefit to S. However, S now holds substantial assets ($5.91M from D's estate + S's own pre-existing assets). S should engage in pre-sunset planning of his/her own — see Example 14.3.

### Example 14.3 — $30 million couple maxing out 2025 SLAT before sunset

H and W are married US citizens, ages 65 and 63, with combined assets of $30,000,000 (rough 50/50 split between them, mostly publicly traded securities and a closely held business interest). No prior taxable gifts. Three adult children, six grandchildren. Both spouses are healthy with normal life expectancy. Date: November 2025. The TCJA sunset is approximately 6 weeks away.

Consume as much of the doubled BEA as possible before December 31, 2025, retaining sufficient liquid assets for lifestyle.

H establishes an irrevocable trust (SLAT-1) for the benefit of W and descendants, funded with $13,000,000 of separately owned assets. W establishes an irrevocable trust (SLAT-2) for the benefit of H and descendants, funded with $13,000,000 of separately owned assets.

Different trustees; Different dispositive provisions (e.g., SLAT-1 is HEMS-only for W; SLAT-2 has an annual 5/5 withdrawal power for H); Different remainder structures (SLAT-1 distributes outright to descendants at age 35; SLAT-2 remains in further trust for descendants); Different commencement and funding dates by a meaningful interval (e.g., several weeks apart); Each spouse contributes different specific assets (not pro rata); Memorialize separate planning meetings for each spouse with independent counsel.

**Gift tax computation (each spouse, 2025)**  _(Example 14.3)_

| Line | Amount |
| --- | --- |
| Gift to SLAT (Schedule A Part 1) | $13,000,000 |
| Less annual exclusion (Crummey rights to descendants × multiple beneficiaries, capped at $19,000 each) | (varies; for simplicity, ignore here) |
| Net taxable gift | $13,000,000 |
| Cumulative prior gifts | $0 |
| Cumulative gifts | $13,000,000 |
| Applicable credit on $13,000,000 | $4,989,800 (tax on $13M at the §2001(c) rates) |
| Applicable credit available (2025 = $5,389,800) | $5,389,800 |
| Net gift tax due | $0 |

Each spouse uses $13,000,000 of the $13,990,000 BEA. Remaining BEA per spouse for end-of-2025 = $990,000.

If the SLATs are dynasty trusts (multi-generational), allocate full $13,000,000 GST exemption per spouse to obtain inclusion ratio zero for each trust. Resulting trusts can compound indefinitely for the benefit of children, grandchildren, and beyond without GST tax — subject to the trust's perpetuities period under the situs jurisdiction.

- **Anti-clawback analysis if death in 2026** — Total post-1976 gifts: $13,000,000. BEA at death (2026, per § 70106 of P.L. 119-21): $15,000,000. Because the BEA at death exceeds cumulative gifts, no anti-clawback computation is needed: the gifts are fully absorbed by the $15,000,000 BEA and T.D. 9884 protection is not triggered. The anti-clawback rule would apply only if a future statute reduced the BEA below cumulative gifts.  _(T.D. 9884)_

$26M of value (the two SLATs) plus all future appreciation is permanently outside the H/W taxable estate. If the SLATs grow at 6% net for 20 years, future value ≈ $26M × (1.06)²⁰ ≈ $83M, all GST-exempt and estate-tax-exempt. Compared to doing nothing pre-sunset, estimated federal estate tax savings (assuming death in 2045 at age 85): approximately $25M – $30M depending on appreciation.

1. Carryover basis: assets gifted to the SLATs take §1015 carryover basis. If $13M of contributed assets had a $3M basis, the donee trust holds a $10M built-in gain. Compared to a §1014 step-up at death, the income-tax cost on eventual sale at the same FMV would be ~$2.4M federal LTCG + NIIT per spouse — a significant offset to estate tax savings. Consider contributing high-basis assets if possible. 2. Reciprocal trust doctrine: if the IRS or a court uncrosses the SLATs, each spouse is treated as having made a gift to a trust of which he/she is a beneficiary — pulling the trust back under §2036. Anti-clawback protection lost; estate tax savings reversed. Drafting differentiation must be defensible. 3. Step-transaction concerns: funding the SLATs immediately before the sunset and with similar structures could attract IRS scrutiny. Document independent decision-making. 4. Divorce risk: if H and W divorce, the indirect access to the SLAT corpus (through the spouse beneficiary) evaporates. Discuss with client. 5. Liquidity: the couple retains $4M of liquid assets ($30M total − $26M gifted). Confirm this is sufficient for lifestyle plus reserves. 6. State estate tax: does the couple live in a state with a lower threshold (e.g., NY at $6.94M)? If so, the SLATs may also reduce state estate tax. Confirm state of domicile.

H files Form 709 reporting the $13M gift to SLAT-1, GST exemption allocation, no gift tax due. W files Form 709 reporting the $13M gift to SLAT-2, GST exemption allocation, no gift tax due. No gift splitting — each spouse is making a gift from separate property, and gift-splitting is precluded because each non-donor spouse has a beneficial interest in the other's SLAT. Both Form 709s due April 15, 2026, with extensions available to October 15, 2026.

## 15. Self-Checks (Tier 2-Specific Extensions to the Tier 1 List)

The Tier 1 base provides workflow self-checks. The following additional self-checks apply specifically to estate, gift, and GST work:

**Self-checks table**  _(15. Self-Checks (Tier 2-Specific Extensions to the Tier 1 List))_

| # | Check | Action if fails |
| --- | --- | --- |
| ET-1 | Confirm whether the decedent is a US citizen, US resident, or NRA. | If NRA, refuse and refer — Form 706-NA is out of scope. |
| ET-2 | Confirm date of death is within the 2025 calendar year (or applicable year). | If not 2025, update figures to applicable year before proceeding. |
| ET-3 | For Form 706, verify gross estate plus adjusted taxable gifts against BEA threshold. | If below threshold and no portability election sought, no return required — confirm with client. |
| ET-4 | For portability elections, verify that the surviving spouse is alive at the time of filing. | If not, portability is moot — no return required. |
| ET-5 | For late portability under Rev. Proc. 2022-32, verify date of death is within 5 years of the proposed filing date. | If beyond 5 years, refuse and refer for PLR. |
| ET-6 | For each Schedule M item, verify the property "passes" to the surviving spouse and is not a non-deductible terminable interest. | Apply QTIP election if appropriate; otherwise remove from Schedule M. |
| ET-7 | For non-citizen surviving spouse, confirm QDOT requirements satisfied before claiming §2056 deduction. | If not, refuse Schedule M treatment and refer to specialist. |
| ET-8 | For each Form 709 gift, confirm donee identification, date of gift, FMV, and present-interest status. | If future interest, ensure not claimed as annual exclusion. |
| ET-9 | If gift splitting elected, confirm both spouses are US citizens or residents and married through end of year. | If failed, do not split. |
| ET-10 | For §529 frontload, confirm five-year proration shown and donor advised that no further annual exclusion to that donee is available during the period. | Document in reviewer brief. |
| ET-11 | For GST allocation, confirm automatic allocation rules under §2632 are explicitly addressed — either accepted, elected out, or affirmatively allocated. | If silent, default to automatic allocation but note risk to reviewer. |
| ET-12 | For Form 706 with prior gifts, verify all prior Form 709 filings have been collected and adjusted taxable gifts line item reconciles to cumulative gift history. | If gaps in history, document and obtain client representation. |
| ET-13 | If alternate valuation elected, verify the §2032(c) gateway: both gross estate AND tax must decrease. | If not, election not permitted — re-value at date of death. |
| ET-14 | For pre-sunset planning gifts in 2025, confirm completion of gift before December 31, 2025 (delivery, donative intent, acceptance). | If incomplete, gift is in 2026 — different BEA. |
| ET-15 | For SLAT or other large gift, confirm reciprocal trust doctrine and §2036 retention concerns addressed in attorney's drafting memo. | If no attorney memo, do not produce return — refer. |
| ET-16 | For each schedule, confirm signed appraisal attached where required (real estate, closely held business, art > $3,000, etc.). | If missing, flag in reviewer brief as required prior to filing. |
| ET-17 | For state estate tax states (CT, DC, HI, IL, ME, MD, MA, MN, NY, OR, RI, VT, WA), confirm separate state return prepared or scheduled. | If not, flag in reviewer brief. |

## 16. Reviewer Brief Output Specification (Tier 2 Slot)

Each output produced under this skill must include:

### 16.1 Filing summary

Form(s) being filed (706 / 709 / 706-GS(D) / 706-GS(T) / 706-NA); Tax year; Due date and extension status; E-filing vs paper filing; Payment method and amount

### 16.2 Computation worksheet

For Form 706: full computation from gross estate through net transfer tax (Page 1 lines); For Form 709: cumulative gift history, current-year gifts, tax computation; For GST: inclusion ratio analysis and allocation summary

### 16.3 Schedule-by-schedule reconciliation

Each schedule cross-referenced to source documents (appraisals, account statements, deeds, insurance policies, Form 712, K-1s); Discounts taken (with appraiser identification and methodology summary)

### 16.4 Election summary

Portability under §2010(c)(5)(A) — yes/no; Alternate valuation under §2032 — yes/no, gateway test; QTIP under §2056(b)(7) — itemized; Reverse QTIP under §2652(a)(3) — itemized; §529 frontload — yes/no, donees, amounts; Gift splitting under §2513 — yes/no; GST automatic allocation in/out — itemized by gift

### 16.5 Anti-clawback / sunset planning analysis

Pre-sunset gifts identified; Anti-clawback protection quantified; Carryover-basis trade-off documented

### 16.6 State considerations

State of domicile at death; State estate / inheritance tax filing requirement; State portability rules (if any)

### 16.7 Open items / required client confirmations

Missing appraisals; Outstanding W-9s / TINs for donees; Crummey notices proof; Spousal consent (Line 18) — if gift splitting; Anti-abuse review for §§2036–2042 retained interests

### 16.8 Citations

Each computation line cross-referenced to IRC section, Treasury regulation, or Rev. Proc.

## 17. Refusal Catalogue (Tier 2 Extensions)

In addition to the Tier 1 universal refusals, this skill refuses the following without escalation:

**Refusal catalogue table**  _(17. Refusal Catalogue (Tier 2 Extensions))_

| # | Refusal | Reason |
| --- | --- | --- |
| ETG-1 | Late portability election more than 5 years after death | Out of Rev. Proc. 2022-32 scope; PLR required |
| ETG-2 | Form 706-NA preparation for NRA decedents | Out of scope; refer to international specialist |
| ETG-3 | §6166 election bond / lien negotiation | Out of scope; refer to IRS Estate and Gift Tax Group |
| ETG-4 | §2032A special-use valuation election and 10-year recapture tracking | Out of scope; refer to farm/ranch specialist |
| ETG-5 | QDOT drafting under §2056A for non-citizen surviving spouse | Out of scope; refer to trust and estate attorney |
| ETG-6 | Family limited partnership valuation discount drafting and §2704 disregarded restrictions analysis | Out of scope; refer to appraiser + attorney team |
| ETG-7 | Reciprocal SLAT differentiation memorandum | Out of scope; refer to attorney |
| ETG-8 | Section 9100 relief request for missed GST allocation beyond automatic allocation rules | PLR required |
| ETG-9 | Charitable lead trust §664 qualification opinion | Out of scope; refer to attorney + actuary |
| ETG-10 | Valuation opinion (real estate, closely held business, art) | Out of scope; refer to qualified appraiser |
| ETG-11 | Estate tax audit defense before IRS Estate and Gift Tax Examiner | Out of scope; refer to credentialed practitioner for representation |
| ETG-12 | State estate or inheritance tax preparation | Refer to state-specific Tier 2 skill (not yet released) |

## 18. Provenance and Citations

### 18.1 Primary statutory authority

IRC §§ 2001–2058 (Estate tax); IRC §§ 2501–2524 (Gift tax); IRC §§ 2601–2664 (GST tax); IRC § 1014 (Basis of property acquired from a decedent); IRC § 1015 (Basis of property acquired by gift); IRC § 6018 (Estate tax return requirement); IRC § 6019 (Gift tax return requirement); IRC § 6075 (Time for filing estate and gift tax returns); IRC § 6166 (Extension of time for payment of estate tax — closely held businesses); IRC § 7520 (Valuation tables)

### 18.2 Regulations

Treas. Reg. § 20.2010-1 (anti-clawback final rule — T.D. 9884, 2019, as amended by T.D. 9884-A, 2022); Treas. Reg. § 20.2010-2 (portability election mechanics, including simplified valuation rule); Treas. Reg. § 20.2010-3 (DSUE computation); Treas. Reg. § 20.2032-1 (alternate valuation); Treas. Reg. § 20.2056A (QDOT requirements); Treas. Reg. § 25.2503-3 (future interests — annual exclusion eligibility); Treas. Reg. § 25.2513-1 (gift splitting mechanics); Treas. Reg. § 26.2632-1 (GST exemption allocation)

### 18.3 Revenue Procedures and Rulings

Rev. Proc. 2024-40 (2025 inflation-adjusted amounts); Rev. Proc. 2022-32 (5-year late portability election); Rev. Proc. 2017-34 (predecessor — superseded); Rev. Proc. 2021-30 (Form 706 closing letter user fee); T.D. 9884 (November 2019) and T.D. 9884-A (April 2022, anti-abuse amendment)

### 18.4 Forms and instructions

Form 706 (Rev. September 2024) and instructions; Form 709 (2024 revision, used for calendar year 2024 gifts; 2025 revision expected late 2025) and instructions; Form 706-GS(D), 706-GS(D-1), 706-GS(T); Form 706-NA (NRA estate tax — referenced but not produced); Form 4768 (extension); Form 8892 (gift tax extension); Form 4422 (release of estate tax lien); Form 712 (life insurance statement); Form 8971 (consistent basis reporting — §1014(f) and §6035)

### 18.5 Legislative

Tax Cuts and Jobs Act of 2017, Pub. L. 115-97, §11061 (BEA doubling and sunset); One Big Beautiful Bill Act of 2025, Pub. L. 119-21 (no estate tax extension; verified); American Taxpayer Relief Act of 2012, Pub. L. 112-240 (portability made permanent)

### 18.6 Last-updated note

Last updated 2025-11-15 for tax year 2025 figures. Verify the OBBBA P.L. 119-21 status of the §2010(c)(3)(C) sunset before relying on the sunset analysis for any return crossing the December 31, 2025 boundary. As of the last update, no legislation has been enacted to extend, repeal, or modify the sunset.

### 18.7 Version history

0.1 (2025-11-15) — initial draft for 2025 tax year, pending Tier 1 reviewer verification

## End of skill notice

End of skill. Combine with us-tax-workflow-base v0.2+ before producing any output. All outputs require Circular 230 practitioner sign-off.

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
