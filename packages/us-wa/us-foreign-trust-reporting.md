---
name: us-foreign-trust-reporting
description: US taxation and reporting of foreign trusts and large foreign gifts for US persons, tax year 2026. Covers the court and control tests of section 7701(a)(30)(E), grantor trust ownership under sections 671 to 679 (especially section 679 and the section 672(f) foreign owner limit), loans and free use of trust property under section 643(i), the throwback tax on accumulation distributions with its interest charge, and Forms 3520 and 3520-A with their deadlines and section 6677 and 6039F penalties. 2026 figures include the Form 3520 Part IV thresholds of more than USD 100,000 from nonresident aliens and foreign estates and more than USD 20,573 from foreign corporations and partnerships (Rev. Proc. 2025-32). Trigger on "foreign trust", "Form 3520", "Form 3520-A", "gift from a foreign person", "inheritance from abroad", "throwback tax", "accumulation distribution", "section 679", "foreign grantor trust". Produces a working paper and a reviewer brief, not a filed return. Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
depends_on:
  - cross-border-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# US reporting of foreign trusts and large foreign gifts (Forms 3520 and 3520-A), tax year 2026

> **Source-cited draft.** Built from the Instructions for Form 3520 (Rev. December 2025), the Instructions for Form 3520-A, Form 3520, Rev. Proc. 2025-32, Rev. Proc. 2020-17, the IRS page on gifts from foreign persons and 26 U.S.C. 643, 665, 668, 672, 679, 6039F, 6048, 6677 and 7701, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A US person files Form 3520 for 2026 if they transferred property to a foreign trust, are treated as owner of any part of one, received a distribution (or a loan or free use of property) from one, or received gifts or bequests of **more than USD 100,000** from nonresident aliens or foreign estates, or **more than USD 20,573** from foreign corporations or partnerships. A foreign trust with a US owner files Form 3520-A by the 15th day of the 3rd month after its year end. For a calendar-year individual the 2026 Form 3520 is due **15 April 2027**. Missing it costs the greater of USD 10,000 or 35% of the amount for trust transfers and distributions, and 5% a month up to 25% for foreign gifts.

## Scope and who this is for

In scope: US federal rules for tax year 2026 for a preparer or a US person who:

- created, funded, or lent to a foreign trust;
- is treated as the owner of any part of a foreign trust under the grantor trust rules (sections 671 to 679);
- received a distribution, a loan, or the free use of property from a foreign trust;
- received large gifts or bequests from foreign persons.

It covers four things: whether the trust is foreign, who (if anyone) is the owner, how a US beneficiary is taxed on distributions (including the throwback tax and its interest charge), and which of Form 3520 and Form 3520-A must be filed, when, and with what penalties.

The Form 3520 instructions in force are the December 2025 revision, which applies for tax year 2025 "and subsequent years until a superseding revision is issued" ([Instructions for Form 3520](https://www.irs.gov/pub/irs-pdf/i3520.pdf)). The only figure here that changes by year is the foreign corporation and partnership gift threshold.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| FBAR (FinCEN Form 114) and Form 8938 for the same trust or accounts | `us-fbar-and-fatca-8938` |
| A foreign corporation owned by the trust or the client (Form 5471) | `us-form-5471-cfc-information` |
| A domestic trust or estate's own return (Form 1041) | `us-form-1041-trust-and-estate-income` |
| US gift and estate tax planning, Forms 706 and 709 | `us-estate-gift-706-709` |
| The section 2801 tax on gifts from covered expatriates (Form 708), and the exit tax | `us-expatriation-exit-tax` |
| Whether the client is a US person at all | `us-tax-residency` |
| The foreign country's own treatment of the trust | refer to a local adviser |

## Ask the client first

1. Who created the trust, and who has transferred money or property to it since? When, and for what consideration? Was any transferor a US person at the time, or within 5 years before becoming a US resident ([26 U.S.C. 679](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartE-sec679.htm))?
2. Where is the trustee, which law governs, and who controls each substantial decision (distributions, investments, adding or removing beneficiaries, replacing the trustee, ending the trust)?
3. Can the settlor revoke the trust alone, or can only the settlor and spouse receive anything during the settlor's life?
4. Who are the beneficiaries, including contingent ones and any US persons who could ever benefit?
5. What did the client receive from the trust this year: cash, property, a loan, the rent-free use of a house or car, card charges paid by the trust?
6. Did the trust send a Foreign Grantor Trust Owner Statement, a Foreign Grantor Trust Beneficiary Statement, or a Foreign Nongrantor Trust Beneficiary Statement? Has it appointed a US agent?
7. Does the trust have year-by-year records of income, distributions and undistributed net income? How many years has it been a foreign trust, and what did it distribute to the client in each of the last 3 years?
8. Is the "trust" really a foreign pension, retirement, medical, disability or education plan (for example a Canadian RRSP or a workplace pension)?
9. Separately from any trust: what gifts or bequests did the client receive from nonresident aliens, foreign estates, foreign corporations or foreign partnerships this year, from whom, and are any of the donors related to each other?
10. Has the client already filed, filed late, or never filed Forms 3520 or 3520-A for earlier years?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Part IV: gifts or bequests from nonresident aliens or foreign estates (related donors and nominees aggregated) | more than USD 100,000 (not indexed) | [Instructions for Form 3520 (Rev. 12-2025), Who Must File, item 4a](https://www.irs.gov/pub/irs-pdf/i3520.pdf) |
| Once over that threshold, each gift listed separately | each gift over USD 5,000 | [Instructions for Form 3520 (Rev. 12-2025), Part IV](https://www.irs.gov/pub/irs-pdf/i3520.pdf) |
| Part IV: purported gifts from foreign corporations or partnerships (related persons aggregated), taxable years beginning in 2026 | exceeds USD 20,573 | [Rev. Proc. 2025-32, section 4.47](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Form 3520 penalty: unreported transfer (Part I) or distribution (Part III) | greater of USD 10,000 or 35% of the gross reportable amount | [26 U.S.C. 6677(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6677.htm) |
| Form 3520-A penalty (charged to the US owner) | greater of USD 10,000 or 5% of the gross value of the owned portion at the close of the year | [26 U.S.C. 6677(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6677.htm) |
| Continuation penalty after 90 days from IRS notice | USD 10,000 for each 30-day period or part of one | [26 U.S.C. 6677(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6677.htm) |
| Unreported foreign gift | 5% of the gift for each month, at most 25% | [26 U.S.C. 6039F(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6039F.htm) |
| Accuracy penalty on an underpayment tied to an undisclosed foreign trust transaction | 20% raised to 40% (section 6662(j)) | [Instructions for Form 3520 (Rev. 12-2025), Penalties](https://www.irs.gov/pub/irs-pdf/i3520.pdf) |
| Default method (Schedule A): prior 3 years' distributions multiplied by | 1.25 | [Form 3520, line 34](https://www.irs.gov/pub/irs-pdf/f3520.pdf) |
| Throwback interest for periods 1977 to 1995 | 6% simple | [Instructions for Form 3520 (Rev. 12-2025), Part III](https://www.irs.gov/pub/irs-pdf/i3520.pdf) |
| Rev. Proc. 2020-17 retirement trust contribution limit (or a percentage-of-earned-income limit) | annual USD 50,000 or less, or lifetime USD 1,000,000 or less | [Rev. Proc. 2020-17, section 5](https://www.irs.gov/pub/irs-drop/rp-20-17.pdf) |
| Rev. Proc. 2020-17 non-retirement savings trust contribution limit | USD 10,000 or less annually, or USD 200,000 or less lifetime | [Rev. Proc. 2020-17, section 5](https://www.irs.gov/pub/irs-drop/rp-20-17.pdf) |

### Is the trust foreign, and who owns it

1. **Decide whether the trust is foreign.** A trust is domestic only if both tests are met: "(i) a court within the United States is able to exercise primary supervision over the administration of the trust, and (ii) one or more United States persons have the authority to control all substantial decisions of the trust" ([26 U.S.C. 7701(a)(30)(E)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm)). A foreign trust is any trust other than that. If either test is not clearly met on the documents, treat the trust as foreign and flag it.
2. **Check the reporting exceptions before anything else.** Some arrangements are trusts for US purposes but need no Form 3520 or 3520-A (see the boundary table): Canadian RRSPs and RRIFs under Rev. Proc. 2014-55, tax-favored foreign retirement and non-retirement savings trusts under Rev. Proc. 2020-17, and the proposed section 1.6048-5 regulations. An exception from reporting does not change income tax, FBAR or Form 8938 duties.
3. **Test for a foreign owner first (section 672(f)).** The grantor trust rules apply only to the extent they make a US citizen, resident or domestic corporation currently taxable. A foreign person is treated as owner only if (i) the settlor alone (or with a related or subordinate party subservient to the settlor) can revest the property in the settlor, or (ii) during the settlor's life the only amounts distributable are to the settlor or the settlor's spouse ([26 U.S.C. 672(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartE-sec672.htm)). A trust whose distributions are taxable as pay for services is also outside the limit (672(f)(2)(B)). If a US beneficiary has made gifts (other than annual-exclusion gifts) to the foreign person who would otherwise be owner, that beneficiary is treated as the grantor of the portion to that extent (672(f)(5)). A typical irrevocable discretionary trust set up by a non-US parent for a family that includes US children is therefore a foreign **nongrantor** trust.
4. **Test for a US owner (sections 673 to 679).** A US person is owner of a portion if an ordinary grantor-trust power applies, or under section 679: a US person who directly or indirectly transfers property to a foreign trust is treated as the owner of the portion attributable to that property "if for such year there is a United States beneficiary of any portion of such trust" ([26 U.S.C. 679(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartE-sec679.htm)). Apply it to each US person separately; one trust can have several owners of different portions.
5. **Apply the section 679 details.**
   - A trust has a US beneficiary unless no income or corpus may be paid or accumulated for a US person, and none could be paid to one if the trust ended. A contingent interest counts.
   - Exceptions: transfers by reason of death, and transfers for at least fair market value (trust and related-party obligations are not counted as consideration).
   - A nonresident who becomes a US resident within 5 years after a transfer is treated as transferring it again on the residency starting date (679(a)(4)).
   - A domestic trust funded by a US citizen or resident that becomes foreign while that individual is alive is treated as a new transfer on that date (679(a)(5)).
   - A beneficiary who first became a US person more than 5 years after the transfer is disregarded (679(c)(3)).
   - If the trust lends cash or marketable securities to a US person, or lets a US person use trust property, the trust is treated as having a US beneficiary, except to the extent the US person repays the loan at a market rate of interest (or pays the fair market value of the use) within a reasonable period (679(c)(6)).

### What follows from the answer

6. **If there is a US owner:** the owner reports the trust income on their own return each year, whether or not anything is distributed. The owner files Form 3520 Part II every year, even with no transactions, and must make sure the trust files Form 3520-A. If the trust will not file, the owner attaches a substitute Form 3520-A to their Form 3520. A distribution to the owner from the owned portion is reported only on lines 24 and 27 of Part III, so the DNI, default and throwback schedules do not apply to it ([Instructions for Form 3520](https://www.irs.gov/pub/irs-pdf/i3520.pdf)).
7. **If a US person transferred appreciated property to a foreign nongrantor trust:** check for gain under section 684, and refer (see the refusal table).
8. **If a US beneficiary received a distribution from a nongrantor trust:**
   - Current-year distributable net income (DNI) comes out first. For a foreign trust, DNI includes net capital gains ([26 U.S.C. 643(a)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartA-sec643.htm)).
   - Anything above DNI is an accumulation distribution ([26 U.S.C. 665](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartD-sec665.htm)). It carries the throwback tax (Form 4970) plus the section 668 interest charge.
   - Choose the calculation. Use Schedule B (actual) only if the trust gave a Foreign Nongrantor Trust Beneficiary Statement and Schedule A has never been used for this trust. Otherwise use Schedule A (default). Without adequate records, section 6048(c)(2) treats the distribution as an accumulation distribution ([26 U.S.C. 6048](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6048.htm)).
   - **Schedule A, line by line** ([Form 3520](https://www.irs.gov/pub/irs-pdf/f3520.pdf)): line 33 is distributions in the 3 preceding years; line 34 multiplies it by 1.25; line 35 divides by 3.0 (or by the number of years the trust has been foreign, if fewer than 3; in the trust's first year as a foreign trust do not complete the rest of Part III); line 36 is the smaller of this year's distribution and line 35, taxed as ordinary income; line 37 is the rest, the accumulation distribution; line 38 is the applicable number of years (years foreign divided by 2.0).
   - Once Schedule A is used for a trust, it must generally be used in later years too. The only exception is Schedule B in the year the trust ends, if a statement is received that year.
9. **If the distribution came from a trust owned by a foreign person** and the beneficiary has a complete Foreign Grantor Trust Beneficiary Statement: treat it as if paid directly by the owner (for example, a gift is not income), and report it in Part III with the statement attached ([Instructions for Form 3520](https://www.irs.gov/pub/irs-pdf/i3520.pdf)).
10. **Treat loans and free use as distributions.** A loan of cash or marketable securities, or use of trust property, to a US grantor or beneficiary (or a related US person) is treated as a distribution of the loan amount or of the fair value of the use. For use of property, the rule does not apply to the extent fair market value is paid within a reasonable period ([26 U.S.C. 643(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartA-sec643.htm)). A loan that keeps its status as a qualified obligation is reported on Form 3520 but, if it loses that status, the holder is treated as receiving a distribution ([Instructions for Form 3520](https://www.irs.gov/pub/irs-pdf/i3520.pdf)).
11. **Run the foreign gift test separately (Part IV).** Apply the thresholds in the rates table, aggregating related donors. Anything received from a foreign trust goes in Part III, not Part IV.
12. **Fix the filings and deadlines,** check for late years, and write the working paper (see Filing and payment).

### Notes on the penalties

- The Form 3520 and 3520-A penalties are charged once for each failure; the 5% figure is not monthly. The monthly penalty is the separate foreign gift penalty.
- Once the IRS can determine the gross reportable amount, later section 6677 penalties are reduced so the total does not exceed it ([26 U.S.C. 6677(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6677.htm)).
- **Reasonable cause:** no section 6677 or 6039F penalty applies if the failure was due to reasonable cause and not willful neglect (6677(d), 6039F(c)(2)). A foreign-law penalty for disclosure, or a trustee's refusal to provide information, is not reasonable cause ([Instructions for Form 3520](https://www.irs.gov/pub/irs-pdf/i3520.pdf)).
- Deficiency procedures do not apply to section 6677 penalties (6677(e)).
- For an unreported foreign gift, the IRS may also decide the income tax consequences of the gift itself ([26 U.S.C. 6039F(c)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6039F.htm)).
- After 1995, throwback interest compounds daily at the underpayment rate, and it also runs on the pre-1996 simple interest.
- **Cap:** the throwback tax plus interest cannot exceed the accumulation distribution: "The total amount of the interest charge shall not, when added to the total partial tax computed under section 667(b), exceed the amount of the accumulation distribution (other than the amount of tax deemed distributed by section 666(b) or (c))" ([26 U.S.C. 668](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartD-sec668.htm)). The interest charge is not deductible.
- The assessment period for tax related to an unreported item stays open until 3 years after the information is reported (section 6501(c)(8)) ([Instructions for Form 3520](https://www.irs.gov/pub/irs-pdf/i3520.pdf)).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Gifts from nonresident aliens total exactly USD 100,000 in the year | Not reportable in Part IV; the test is "more than" |
| Two nonresident donors you know are related give USD 75,000 and USD 40,000 | Aggregate; report, listing each gift over USD 5,000 ([Instructions for Form 3520](https://www.irs.gov/pub/irs-pdf/i3520.pdf)) |
| Foreign person pays tuition or medical bills directly | Not a foreign gift (qualified transfer under section 2503(e)(2)) ([26 U.S.C. 6039F(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6039F.htm)) |
| Money from a foreign trust described as a "gift" | Report as a distribution in Part III, not Part IV |
| Purported gift from a foreign corporation or partnership | Reportable above USD 20,573, and the IRS may recharacterize it (section 672(f)(4)) |
| Canadian RRSP, RRIF or other plan within Rev. Proc. 2014-55 | No Form 3520 or 3520-A ([Instructions for Form 3520-A](https://www.irs.gov/pub/irs-pdf/i3520a.pdf)) |
| Foreign pension or savings trust meeting every test in Rev. Proc. 2020-17 section 5, held by an eligible individual who is compliant with US return filing and has reported any taxable amounts | No Form 3520 or 3520-A; penalties already assessed can be challenged on Form 843 ([Rev. Proc. 2020-17](https://www.irs.gov/pub/irs-drop/rp-20-17.pdf)) |
| Tax-favored foreign trust covered by proposed regulations section 1.6048-5 | May rely on them for tax years ending after 8 May 2024, only if the individual and all related persons apply them in full and consistently ([Instructions for Form 3520](https://www.irs.gov/pub/irs-pdf/i3520.pdf)) |
| Section 402(b) funded deferred compensation, section 404(a)(4) foreign pension trusts, section 404A qualified foreign plans | No Form 3520 |
| Most transfers to a foreign trust for fair market value | No Form 3520. Report anyway if the transfer is for a qualified obligation, is of appreciated property with gain not fully recognized, or is by a related US transferor |
| Distribution taxable as pay for services, reported as such | No Form 3520 for it |
| Foreign law would penalize disclosure, or the trustee refuses to give information | Not reasonable cause |
| Trust whose foreign settlor can revoke it alone | Foreign grantor trust owned by a foreign person; a US beneficiary follows step 9 |
| Trust foreign for fewer than 3 years | Schedule A line 35 divides by the number of years foreign; in the first year as a foreign trust, the rest of Part III is not completed |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether the court test and control test are both met | Treat the trust as foreign until the deed and trustee arrangements show otherwise |
| Whether two foreign donors are related | Ask; if there is reason to know they are related, aggregate |
| A Foreign Nongrantor Trust Beneficiary Statement | Schedule A (default method); note that it then binds later years |
| Trust records of DNI and undistributed income | Treat the excess over current-year amounts as an accumulation distribution (6048(c)(2)) |
| Whether a foreign pension meets Rev. Proc. 2020-17 | Assume reporting is required until every section 5 test is shown |
| Prior-year filing history | Ask; do not assume earlier Forms 3520 or 3520-A were filed |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| A US person ever funded the trust, or moved to the US within 5 years after funding it | Section 679 owner; Form 3520-A becomes the owner's problem |
| Rent-free use of a trust home or car, or a loan from the trust | Section 643(i) distribution and 679(c)(6) US beneficiary |
| Long accumulation history and no records | Throwback tax plus interest can take most of the distribution |
| Earlier years with no Form 3520 | 35% penalties and an open assessment period |
| A donor who gave up US citizenship or a green card | Possible section 2801 tax: see `us-expatriation-exit-tax` |
| A promoter says the arrangement is outside these rules | The IRS warns about abusive foreign trust schemes |

## Worked cases

These are illustrations with invented amounts, not advice.

**Case 1, a decision: must she file Part IV, and what does not filing cost?** A US citizen receives USD 60,000 from her nonresident mother and USD 45,000 from her nonresident father in 2026. The donors are related, so aggregate: USD 105,000 is USD 5,000 more than the USD 100,000 threshold, so she must file Form 3520 Part IV and list both gifts, each being over USD 5,000. The gifts are not income. If she files 7 months late with no reasonable cause, the penalty is 5% a month, capped at 25%: 25% of USD 105,000 is USD 26,250. Decision: file Part IV by 15 April 2027 (or 15 October 2027 with an income tax extension). Had the gifts totalled exactly USD 100,000, no Part IV would be due.

```oa-check
name: Foreign gifts from related donors, Part IV test and late penalty (2026)
inputs:
  gift_mother: 60000
  gift_father: 45000
  threshold: 100000
  months_late: 7
steps:
  - aggregate: gift_mother + gift_father
  - over_threshold: max(aggregate - threshold, 0)
  - penalty_rate: min(0.05 * months_late, 0.25)
  - late_penalty: penalty_rate * aggregate
expected:
  aggregate: 105000.00
  over_threshold: 5000.00
  penalty_rate: 0.25
  late_penalty: 26250.00
```

**Case 2, default calculation of a nongrantor trust distribution (Schedule A).** The trust has been foreign for 10 years, including 2026, and the beneficiary has no Foreign Nongrantor Trust Beneficiary Statement. Distributions to the beneficiary in the 3 preceding years total USD 12,000, and the 2026 distribution is USD 40,000. Line 34: USD 12,000 x 1.25 = USD 15,000. Line 35: USD 15,000 / 3.0 = USD 5,000. Line 36: the smaller of USD 40,000 and USD 5,000 is USD 5,000, taxed as ordinary income. Line 37: USD 35,000 is the accumulation distribution. Line 38: 10 / 2.0 = 5 applicable years. Tax on the USD 35,000 is computed on Form 4970, interest is added, and tax plus interest cannot exceed USD 35,000. If the beneficiary had not filed Form 3520 for this distribution, the initial penalty would be the greater of USD 10,000 or 35% of USD 40,000, which is USD 14,000.

```oa-check
name: Schedule A default distribution and section 6677 exposure (2026)
inputs:
  prior_three_years: 12000
  current_distribution: 40000
  years_foreign: 10
steps:
  - line_34: prior_three_years * 1.25
  - line_35: line_34 / 3
  - line_36: min(current_distribution, line_35)
  - line_37: current_distribution - line_36
  - line_38: years_foreign / 2
  - penalty_if_unreported: max(10000, 0.35 * current_distribution)
expected:
  line_34: 15000.00
  line_35: 5000.00
  line_36: 5000.00
  line_37: 35000.00
  line_38: 5.00
  penalty_if_unreported: 14000.00
```

**Case 3, purported gift from a foreign company.** A foreign corporation owned by the client's nonresident uncle sends the client USD 21,000 in 2026, called a gift. It exceeds USD 20,573, so Part IV applies. Before treating it as a gift, consider whether it is really pay, a dividend or a distribution, because the IRS may recharacterize it (section 672(f)(4)).

**Case 4, unreported distribution.** A US beneficiary received USD 200,000 from a foreign nongrantor trust and filed no Form 3520. The initial penalty is the greater of USD 10,000 or 35% of USD 200,000, which is USD 70,000. More is added at USD 10,000 per 30-day period if the failure continues more than 90 days after an IRS notice, and the total cannot exceed the gross reportable amount.

**Case 5, US owner, trust files no Form 3520-A.** A US citizen is the section 679 owner of a foreign trust whose assets are worth USD 150,000 at year end. If the owner attaches a substitute Form 3520-A to a timely Form 3520, there is no penalty for the trust's failure. If neither is filed, the penalty is the greater of USD 10,000 or 5% of USD 150,000 (USD 7,500), so USD 10,000.

**Case 6, foreign settlor, US child.** A nonresident grandmother sets up an irrevocable discretionary trust abroad for her grandchildren, one of whom is a US citizen. She cannot revoke it and the trust can pay the grandchildren in her lifetime, so section 672(f) stops her being treated as owner. It is a foreign nongrantor trust: the US grandchild reports each distribution in Part III (Case 2 method if there is no statement), and the trust files no Form 3520-A. If instead she could revoke it alone, she would be the foreign owner, and a distribution backed by a complete Foreign Grantor Trust Beneficiary Statement would be treated as a gift from her, still reported in Part III.

**Case 7, workplace pension abroad.** A US citizen working abroad belongs to an employer pension that is tax-favored locally and reported to the local tax authority, takes only earned-income contributions capped by a percentage of pay, and locks withdrawals until retirement age. If every Rev. Proc. 2020-17 section 5.03 test is met and the client is compliant with US return filing, no Form 3520 or 3520-A is needed. FBAR, Form 8938 and US income tax on the plan may still apply.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-FT-LOCAL | The foreign country's tax treatment of the trust, its distributions and gains | Refer to a local adviser; the two systems often characterize the same trust differently and double tax relief is not automatic |
| R-FT-LATE | Forms 3520 or 3520-A missed in earlier years and the client wants to fix it | Refer; the route into compliance and the reasonable cause argument are judgement calls. Never promise a waiver |
| R-FT-RECORDS | Long accumulation history and no records | Refer; the default method applies and throwback tax plus interest can take most of the distribution |
| R-FT-684 | Section 684 gain on appreciated property sent to a foreign nongrantor trust, a trust migration under 679(a)(5), or pre-immigration trust planning under 679(a)(4) | Refer |
| R-FT-2801 | Gifts or bequests from a former US citizen or green-card holder who may be a covered expatriate | Refer: section 2801 and Form 708, see `us-expatriation-exit-tax` |
| R-FT-EXPAT | A US owner or beneficiary is giving up citizenship or long-term residence, or plans to sell trust assets around a change of status | Refer; section 877A and the section 679 answer interact, and the order of steps changes the result |
| R-FT-PROMOTER | A promoter says the arrangement is outside these rules | Refuse to accept that; the IRS warns about abusive foreign trust schemes |

## Filing and payment

- **Form 3520 (US person):** due on the 15th day of the 4th month after the end of the tax year. For a calendar-year individual, the 2026 form is due **15 April 2027** ([Instructions for Form 3520](https://www.irs.gov/pub/irs-pdf/i3520.pdf)).
  - A US citizen or resident who lives and has their place of business or post of duty outside the US and Puerto Rico, or is on military duty abroad, has until the 15th day of the 6th month (15 June 2027). Check line 1j and attach a statement.
  - An extension of the income tax return extends Form 3520 to no later than the 15th day of the 10th month (15 October 2027). Check box 1k and enter the return's form number. The discretionary 2-month extension to 15 December does not extend Form 3520.
  - The form is filed separately from the income tax return, by mail to Internal Revenue Service Center, P.O. Box 409101, Ogden, UT 84409. Use one Form 3520 per foreign trust. Spouses filing jointly may file one joint Form 3520 if both are transferors, grantors or beneficiaries of the same trust.
  - Only a complete form, with all attachments, counts as timely.
- **Form 3520-A (foreign trust with a US owner):** due on the 15th day of the 3rd month after the trust's year end (15 March 2027 for a calendar-year trust) ([Instructions for Form 3520-A](https://www.irs.gov/pub/irs-pdf/i3520a.pdf)).
  - The trust must also send the Owner and Beneficiary Statements to its US owners and beneficiaries by that date.
  - To extend, file Form 7004 under the trust's EIN by the same date. The owner's income tax extension does not extend Form 3520-A.
  - The trustee signs. A substitute Form 3520-A, signed by the US owner, is due with the owner's Form 3520, and copies of the statements go out by the same date.
- **US agent:** if a foreign trust with a US owner has no US agent named on Form 3520 lines 3a to 3g, the IRS may redetermine the owner's amounts.
- **Tax due:** income of an owned portion, DNI and throwback tax are paid with the income tax return. The throwback total (Form 3520 line 53) goes on Schedule 2 (Form 1040) as additional tax. Use Form 8082 if a return treats an item differently from the trust's Form 3520-A.
- **Also consider:** FBAR and Form 8938 (`us-fbar-and-fatca-8938`). A Form 3520 filer who also files Form 8938 checks item C.

### Returns for 2025 still being filed

The December 2025 instructions apply to 2025 and 2026. For 2025 the foreign corporation and partnership gift threshold is more than USD 20,116 ([Rev. Proc. 2024-40, section 2.48](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf)); the nonresident alien threshold is still more than USD 100,000. A calendar-year 2025 Form 3520 was due 15 April 2026 (15 June 2026 for a qualifying person abroad); with a timely Form 4868 it is due 15 October 2026 and cannot be extended further. If the trust missed its 2025 Form 3520-A, the owner's substitute must be attached to the 2025 Form 3520 by that same date.

## Completion checklist

- [ ] Court test and control test both applied; foreign or domestic conclusion stated.
- [ ] Rev. Proc. 2014-55, Rev. Proc. 2020-17 and proposed section 1.6048-5 exceptions tested before any form is prepared.
- [ ] Section 672(f) applied for any foreign settlor; section 673 to 679 ownership fixed for each US person, with funding history, 5-year residency rule and US-beneficiary test documented.
- [ ] Loans and use of trust property checked under section 643(i).
- [ ] For an owner: income reported currently; Form 3520 Part II filed; Form 3520-A or substitute confirmed; US agent status noted.
- [ ] For a beneficiary: DNI and accumulation distribution computed; Schedule A or B chosen and the consistency rule respected; Form 4970 and interest charge done; section 668 cap applied.
- [ ] Foreign gifts aggregated by related donor and tested against the 2026 thresholds; trust receipts moved to Part III.
- [ ] Deadlines set (Form 3520, Form 3520-A, Form 7004, box 1k, line 1j) and prior-year gaps listed with penalty exposure.
- [ ] Foreign-country treatment and any section 2801 issue referred.
- [ ] Output labelled as a working paper for a qualified professional to check before filing.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Instructions for Form 3520 (Rev. December 2025). Read for who must file (item 4a, more than $100,000), the $5,000 listing rule, due dates (4th, 6th and 10th month), line 1j, box 1k, Ogden address, penalties, exceptions and the first-year rule. | https://www.irs.gov/pub/irs-pdf/i3520.pdf | 2026-11-13 |
| Form 3520. Read for Part III Schedule A, lines 33 to 38 (1.25, 3.0, 2.0) and line 53. | https://www.irs.gov/pub/irs-pdf/f3520.pdf | 2026-11-13 |
| Instructions for Form 3520-A. Read for the 3rd-month due date, Form 7004, the substitute Form 3520-A and Rev. Proc. 2014-55. | https://www.irs.gov/pub/irs-pdf/i3520a.pdf | 2026-11-13 |
| Rev. Proc. 2025-32. Read for section 4.47 ($20,573 for taxable years beginning in 2026). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Rev. Proc. 2024-40. Read for section 2.48 ($20,116 for 2025). | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-13 |
| Rev. Proc. 2020-17. Read for section 5 contribution limits ($50,000, $1,000,000, $10,000, $200,000). | https://www.irs.gov/pub/irs-drop/rp-20-17.pdf | 2026-11-13 |
| IRS, Gifts from foreign person. Read for the $100,000 aggregate test and separate listing above $5,000. | https://www.irs.gov/businesses/gifts-from-foreign-person | 2026-11-13 |
| 26 U.S.C. 6677 (govinfo). Read for (a) greater of $10,000 or 35%, the 30-day continuation penalty, (b) 5% for Form 3520-A, (d) reasonable cause, (e) no deficiency procedures. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6677.htm | 2026-11-13 |
| 26 U.S.C. 6039F (govinfo). Read for the 5% a month, 25% cap, reasonable cause and qualified transfers. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6039F.htm | 2026-11-13 |
| 26 U.S.C. 7701(a)(30)(E) (govinfo). Read for the court and control tests. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap79-sec7701.htm | 2026-11-13 |
| 26 U.S.C. 679 (govinfo). Read for (a)(1), (a)(4), (a)(5), (c)(3) and (c)(6). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartE-sec679.htm | 2026-11-13 |
| 26 U.S.C. 672(f) (govinfo). Read for the foreign owner limit and (f)(4), (f)(5). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartE-sec672.htm | 2026-11-13 |
| 26 U.S.C. 643 (govinfo). Read for (a)(6) foreign trust DNI and (i) loans and use of property. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartA-sec643.htm | 2026-11-13 |
| 26 U.S.C. 665 (govinfo). Read for the accumulation distribution. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartD-sec665.htm | 2026-11-13 |
| 26 U.S.C. 668 (govinfo). Read for the interest charge and its cap. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartD-sec668.htm | 2026-11-13 |
| 26 U.S.C. 6048 (govinfo). Read for (c)(2), distributions without adequate records. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6048.htm | 2026-11-13 |

Not yet confirmed: the 2026 revision of Form 3520 and its instructions was not published when read (the December 2025 instructions say they apply until superseded); the US Code text read is the 2024 edition, and no change to sections 643, 665 to 668, 672, 679, 6039F, 6048 or 6677 by Public Law 119-21 was found, but that was not checked line by line against the Public Law.
