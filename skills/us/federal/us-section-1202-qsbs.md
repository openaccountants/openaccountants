---
name: us-section-1202-qsbs
description: Section 1202 qualified small business stock (QSBS) gain exclusion for a US non-corporate seller in tax year 2026, with the section 1045 rollover. Splits on the July 4, 2025 applicable date. Old-regime stock (held more than 5 years) keeps the 50, 75 or 100 percent exclusion by purchase date and a USD 10,000,000 per-issuer cap. New-regime stock (acquired after July 4, 2025) gets 50 percent at 3 years, 75 percent at 4 years and 100 percent at 5 years, a USD 15,000,000 cap, and a USD 75,000,000 gross-assets limit for stock issued after that date. Covers the 10-times-basis cap, the excluded fields, redemptions, the 28 percent rate on the non-excluded part, AMT and NIIT, and Form 8949 code Q and R reporting. Trigger on "QSBS", "section 1202", "qualified small business stock", "startup stock exclusion", "section 1045 rollover", "Form 8949 code Q". Federal only.
version: "2.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-28
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US section 1202 qualified small business stock (QSBS) exclusion, tax year 2026

> Federal law checked against the enacted amendments and official sources on 28 November 2026. Form references below identify their edition; future-year model inputs are not filing limits.

**Answer first.** The rules split on the **applicable date, July 4, 2025** (the date the Act was enacted). Stock **acquired** on or before that date must be held more than 5 years; the exclusion is 50, 75 or 100 percent depending on when it was bought (100 percent if after 27 September 2010), and gain from one issuer counts only up to **USD 10,000,000** (or 10 times basis, if more). Stock **acquired** after that date qualifies after 3 years: **50%** at 3 years, **75%** at 4 years, **100%** at 5 years or more, with a **USD 15,000,000** per-issuer cap. A corporation that **issues** stock after July 4, 2025 must have gross assets of no more than **USD 75,000,000** before and immediately after the issue. The part of capped gain not excluded is taxed at a maximum of 28 percent; gain above the cap is ordinary long-term capital gain. For a calendar-year seller, 2026 is the first year the new cap rules apply, and no new-regime stock can reach 3 years before July 2028.

## Scope and who this is for

In scope: a non-corporate US taxpayer (individual, trust, estate, or a partner or shareholder of a pass-through entity) who sells stock in a domestic C corporation in tax year 2026 and wants to exclude gain under section 1202 or defer it under section 1045. The result lands on Form 8949 Part II (code Q) or Part I or II (code R), Schedule D, the 28% Rate Gain Worksheet, Form 6251 and Form 8960.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Capital gains rates and holding periods generally | `us-capital-gains` |
| Equity compensation (RSUs, options) before the sale | `us-equity-compensation-restricted-stock-units-and` |
| Installment reporting on Form 6252 | `us-installment-sale-6252` |
| Opportunity zone deferral of the same gain | `us-opportunity-zones` |
| Choosing a C corporation at formation | `us-s-corp-election-decision`, `us-form-1120-c-corp` |
| State treatment (some states do not follow section 1202) | the state's own statute and revenue department; this skill states no state's position |

## Ask the client first

1. **Who is the seller?** Individual, trust or estate, or a pass-through entity (partnership, S corporation, RIC, common trust fund). A corporation cannot use section 1202 ([26 U.S.C. 1202(a)](https://uscode.house.gov/us/usc/t26/s1202/)).
2. **How was the stock acquired, and when?** At original issue from the corporation (directly or through an underwriter) for money, property other than stock, or services? Or by gift, at death, in a partnership distribution, by converting other stock of the same corporation, or in a section 351 or 368 exchange? Stock bought from another shareholder does not qualify. Get the exact acquisition date and which side of July 4, 2025 it falls on; for options and warrants, the exercise and transfer dates; for SAFEs and convertible notes, the instrument and its tax characterization (do not assume every SAFE is debt); for restricted stock received for services, whether a section 83(b) election was filed ([Treas. Reg. 1.83-4(a)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol2/xhtml/CFR-2025-title26-vol2-sec1-83-4.html)).
3. **The corporation's history.** Exact issue date; aggregate gross assets (cash plus adjusted basis of other property, contributed property at its value when contributed) at all times on or after 10 August 1993 before issue and immediately after, including predecessors and every member of a more-than-50 percent parent-subsidiary group; C corporation status and the active business test for substantially all of the holding period; any S election or partnership classification; what the company actually does (revenue breakdown and asset list).
4. **Buybacks near the issue date** from the seller, a related person or anyone else: dates, amounts and values ([Treas. Reg. 1.1202-2](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/xhtml/CFR-2025-title26-vol13-sec1-1202-2.html)).
5. **Gain from this issuer already used.** How much section 1202 gain from this issuer the seller (and, on past joint returns, the spouse) has taken into account in earlier years.
6. **The sale.** Date, amount realized, basis, installment payments, escrow or earn-out, any short sale, put or hedge; and if the holding period is too short, whether other QSBS was bought within 60 days and the seller wants a section 1045 election ([26 U.S.C. 1045](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1045.htm)).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| Applicable date (date of enactment): splits old and new regimes | July 4, 2025 | [Public Law 119-21, section 70431(a)(3)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| New regime: exclusion, stock held 3 years | 50% | [Public Law 119-21, section 70431(a)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| New regime: exclusion, stock held 4 years | 75% | [Public Law 119-21, section 70431(a)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| New regime: exclusion, stock held 5 years or more | 100% | [Public Law 119-21, section 70431(a)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| New regime: per-issuer dollar limit, stock acquired after the applicable date | USD 15,000,000 | [Public Law 119-21, section 70431(b)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Old regime: per-issuer dollar limit, stock acquired on or before the applicable date | USD 10,000,000 | [Public Law 119-21, section 70431(b)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Old regime, married filing separately | USD 5,000,000 | [Public Law 119-21, section 70431(b)(3)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| New regime, married filing separately | one-half of the USD 15,000,000 amount in effect | [Public Law 119-21, section 70431(b)(3)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Alternative cap, both regimes | 10 times the adjusted basis of the issuer's QSBS sold in the year | [26 U.S.C. 1202(b)(1)(B)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Gross assets limit, stock issued after the applicable date | USD 75,000,000 | [Public Law 119-21, section 70431(c)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Gross assets limit, stock issued on or before the applicable date | USD 50,000,000 | [Pre-amendment section 1202(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partI-sec1202.htm); [Act section 70431(c)(3)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Old regime: exclusion, acquired on or before 17 February 2009 | 50% | [Instructions for Schedule D (2025)](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) |
| Old regime: exclusion, acquired after 17 February 2009 and before 28 September 2010 | 75% | [Instructions for Schedule D (2025)](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) |
| Old regime: exclusion, acquired after 27 September 2010 | 100% | [Instructions for Schedule D (2025)](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) |
| Maximum rate on section 1202 gain (the non-excluded part of capped gain) | 28% | [26 U.S.C. 1(h)(4) and (7)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |
| AMT preference, stock acquired on or before 27 September 2010 only | 7% of the excluded amount | [26 U.S.C. 57(a)(7)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec57.htm) |
| NIIT rate, applied to the statutory lesser-of base below | 3.8% | [26 U.S.C. 1411(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| NIIT threshold, joint return or surviving spouse | USD 250,000 | [26 U.S.C. 1411(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| NIIT threshold, other individuals | USD 200,000 | [26 U.S.C. 1411(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| NIIT threshold, married filing separately | USD 125,000 (derived: half the USD 250,000 joint amount) | [26 U.S.C. 1411(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm) |
| Active business test: share of assets by value used in qualified trades or businesses | at least 80 percent | [26 U.S.C. 1202(e)(1)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Working capital counted as active, after the corporation has existed 2 years, at most | 50 percent of assets | [26 U.S.C. 1202(e)(6)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Portfolio stock limit (share of asset value net of liabilities) | more than 10 percent fails | [26 U.S.C. 1202(e)(5)(B)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Real estate not used in the business (share of total assets) | more than 10 percent fails | [26 U.S.C. 1202(e)(7)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Significant redemptions: buybacks in the 2-year window above this share of all stock value | 5 percent | [26 U.S.C. 1202(c)(3)(B)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Redemption de minimis: a buyback counts only if it exceeds both USD 10,000 and this share | 2 percent | [Treas. Reg. 1.1202-2(a)(2) and (b)(2)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/xhtml/CFR-2025-title26-vol13-sec1-1202-2.html) |
| Section 1045 rollover: holding period of the stock sold | more than 6 months | [26 U.S.C. 1045(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1045.htm) |
| Section 1045 rollover: replacement QSBS bought within | 60-day period beginning on the sale date | [26 U.S.C. 1045(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1045.htm) |

**Effective dates.** The percentage and holding-period changes (section 70431(a)) and the per-issuer limit changes (section 70431(b)) apply to taxable years beginning after July 4, 2025, so for a calendar-year taxpayer they first apply in 2026. The USD 75,000,000 gross-assets limit applies to stock issued after July 4, 2025. The Act directs inflation adjustments to the USD 15,000,000 and USD 75,000,000 amounts for taxable years beginning after 2026, using a 2025 base and rounding the increase to the nearest USD 10,000. Its gross-assets indexing paragraph is enacted under a duplicate paragraph (4) in subsection (b), although it refers to the gross-assets amounts in subsection (d). The official Code preserves that drafting anomaly. The future cases below use the original unindexed model inputs; they do not supply the actual indexed limit for a later filing year.

### Steps

1. **Check the seller.** A taxpayer other than a corporation. For a pass-through entity, the owner must have held the interest on the day the entity acquired the stock and at all times after, until the entity sold it; the owner's share is capped by the interest held when the stock was acquired ([26 U.S.C. 1202(g)](https://uscode.house.gov/us/usc/t26/s1202/)).
2. **Check the stock is QSBS:** original issue, qualified small business status at issue (gross assets), C corporation status and the active business test for substantially all of the holding period, and redemptions. All must pass (tables below).
3. **Fix the acquisition date.** "The acquisition date for purposes of this section shall be the first day on which such stock was held by the taxpayer determined after the application of section 1223" ([Public Law 119-21, section 70431(a)(3)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)). Tacking from a gift, a death, a conversion of other stock of the same corporation (section 1202(f)) or a section 1045 rollover can move the date earlier, and the date picks the regime.
   - Stock received for property other than money or stock, including in a section 351 incorporation or an LLC's conversion to a corporation, is treated as acquired on the date of that exchange; the property's holding period does not tack (section 1202(i)(1)(A)).
   - Stock received for services and subject to vesting is held from just after it substantially vests, or just after the transfer if a section 83(b) election was made ([Treas. Reg. 1.83-4(a)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol2/xhtml/CFR-2025-title26-vol2-sec1-83-4.html)). A restricted-stock transfer before July 4, 2025 does not by itself establish an old-regime holding date if vesting occurs later without a section 83(b) election. Such an election must be made no later than 30 days after transfer (section 83(b)(2)); retain proof of timely filing.
4. **Check the holding period:** more than 5 years for stock acquired on or before July 4, 2025; at least 3 years for stock acquired after it.
5. **Cap the eligible gain for each issuer:** the greater of the applicable dollar limit or 10 times the aggregate adjusted basis of the issuer's QSBS sold in the year. The cap limits the gain taken into account; the exclusion percentage is then applied to the capped gain.
   - Old regime: USD 10,000,000 less eligible gain from the issuer taken into account in earlier years.
   - New regime: USD 15,000,000 less earlier years' eligible gain from the issuer (any stock) and less same-year eligible gain from the issuer's old-regime stock.
   - **No later inflation top-up once exceeded:** if eligible gain from new-regime stock of an issuer exceeds the dollar limit in any year, that issuer's dollar limit is zero for every later year, despite indexing. This rule does not eliminate the separate 10-times-basis alternative. Reduce the dollar-limit tracker by eligible gain taken into account, not merely the excluded percentage.
   - The 10-times-basis cap uses adjusted basis without additions after original issue. For stock received for property, basis is never less than the property's fair market value at the exchange (section 1202(b)(1) and (i)).
6. **Apply the exclusion percentage** for the regime and holding period.
7. **Classify what remains.** Gain above the cap is long-term capital gain at the normal rates (`us-capital-gains`). The part of capped gain not excluded only because the percentage is below 100 percent is "section 1202 gain", taxed at a maximum of 28 percent.
8. **AMT and NIIT.** Only stock acquired on or before 27 September 2010 has an AMT preference (7 percent of the excluded amount); new-regime 50 and 75 percent stock has none. NIIT reaches gain only to the extent taken into account in computing taxable income, so excluded gain is outside it; the taxable remainder counts.
9. **If the holding period fails**, test a section 1045 rollover.
10. **Report** on Form 8949 with code Q (exclusion) or code R (rollover), then Schedule D and, for stock acquired before 28 September 2010, Form 6251.

### What makes stock QSBS

| Test | Rule | Source |
| --- | --- | --- |
| Issuer | Domestic C corporation. Not a DISC or former DISC, RIC, REIT, REMIC or cooperative | [26 U.S.C. 1202(d)(1), (e)(4)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Original issue | Originally issued after the date of enactment of the Revenue Reconciliation Act of 1993 (10 August 1993); acquired at original issue for money, property other than stock, or services (not underwriting) | [26 U.S.C. 1202(c)(1)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Gross assets | Cash plus adjusted basis of other property; contributed property at its value when contributed. The limit must not be exceeded at any time on or after 10 August 1993 before issue (including predecessors), or immediately after issue counting the amount received; retain the issuer reporting agreement required by section 1202(d)(1)(C) | [26 U.S.C. 1202(d)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Active business | For substantially all of the holding period, at least 80 percent of assets by value used in the active conduct of qualified trades or businesses | [26 U.S.C. 1202(c)(2), (e)(1)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Working capital | Assets held as reasonably required working capital, or held for investment and reasonably expected to be used within 2 years for research or increased working capital, count as active; after the corporation has existed at least 2 years, no more than 50 percent of assets can qualify this way | [26 U.S.C. 1202(e)(6)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Portfolio stock | Fails for any period in which more than 10 percent of asset value (net of liabilities) is stock or securities of non-subsidiary corporations, other than qualifying working-capital assets under section 1202(e)(6) | [26 U.S.C. 1202(e)(5)(B)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Real estate | Fails for any period in which more than 10 percent of total asset value is real property not used in the active business. For this real-estate limit, owning, dealing in or renting real property is not treated as active conduct of a qualified business | [26 U.S.C. 1202(e)(7)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Subsidiaries | A more-than-50 percent subsidiary is looked through for the active business test; the parent-subsidiary group is one corporation for the gross-assets test | [26 U.S.C. 1202(d)(3), (e)(5)](https://uscode.house.gov/us/usc/t26/s1202/) |

"Substantially all" is not defined in the statute. Do not use a percentage test for it without authority for your facts.

The specialized small business investment company waiver in section 1202(c)(2)(B) concerns the active-business requirement during its qualifying period; it is not a blanket QSBS exemption. A specific SSBIC claim is held under R-QSBS-SPECIAL.

### Excluded fields (not a qualified trade or business)

Under [26 U.S.C. 1202(e)(3)](https://uscode.house.gov/us/usc/t26/s1202/), these do not qualify:

- services in the fields of health, law, engineering, architecture, accounting, actuarial science, performing arts, consulting, athletics, financial services or brokerage services;
- any business whose principal asset is the reputation or skill of one or more employees;
- banking, insurance, financing, leasing, investing or similar businesses;
- farming, including raising or harvesting trees;
- production or extraction of products eligible for percentage depletion under section 613 or 613A;
- operating a hotel, motel, restaurant or similar business.

Assets used for a future qualified business in section 195(c)(1)(A) start-up activities, foreign research under section 174, domestic research under section 174A, or section 41(b)(4) in-house research count as active, without requiring current gross income. Software rights producing active business computer software royalties also count as active (section 1202(e)(2) and (e)(8)).

### Section 1045 rollover (60 days)

- **Who and what:** a taxpayer other than a corporation selling QSBS held for more than 6 months can elect to recognize gain only to the extent the amount realized exceeds the cost of other QSBS bought in the 60-day period beginning on the date of sale. Gain treated as ordinary income cannot be rolled ([26 U.S.C. 1045(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1045.htm)).
- **Replacement stock** must be QSBS. For the rollover test, only its first 6 months are taken into account when applying section 1202(c)(2); this is not a promise that later noncompliance is harmless for a subsequent section 1202 exclusion (section 1045(b)(4)).
- **Basis:** postponed gain reduces the basis of the replacement stock, in the order acquired (section 1045(b)(3)).
- **Holding period:** the replacement stock's holding period includes the old stock's, for section 1202 too, except for section 1202(a)(2) and (c)(2)(A); it does not count for the more-than-6-month test on a later rollover (sections 1223(13) and 1045(b)(4)). Read sections 1202(a)(6) and 1223(13) together: the replacement purchase date alone does not reset the section 1202 acquisition date or establish a new USD 15,000,000 limit. A rollover spanning July 4, 2025 needs a documented chain of holdings. A specific untraced chain is a NON-USABLE HOLD. Check this point with one of our partner accountants.
- **Election deadline:** by the due date, including extensions, of the return for the year of sale. If the original return was filed on time, an amended return filed within 6 months after the due date (excluding extensions) marked "Filed pursuant to section 301.9100-2" is accepted ([Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)).
- **Pass-through rollover:** an entity may elect. Its owner must have held the interest throughout the entity's holding period to receive the benefit; such an owner can instead purchase qualifying replacement QSBS personally within the 60-day period. Partnership election/reporting mechanics under section 1.1045-1 require their own procedure; an unresolved procedural result is a NON-USABLE HOLD. Check this point with one of our partner accountants.

### Tax on what is not excluded

- **Section 1202 gain** (eligible gain minus the exclusion) is 28-percent rate gain, subject to capital-loss netting and the tax computation; 28 percent is a maximum, not an automatic flat rate. In the 2025 form edition, on the 28% Rate Gain Worksheet, line 2, enter the exclusion for 50 percent stock, 2/3 of it for 60 percent stock, 1/3 of it for 75 percent stock, and nothing for 100 percent stock ([Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)).
- **Gain above the per-issuer cap** is long-term capital gain at the normal rates.
- **AMT:** for stock acquired before 28 September 2010 and held more than 5 years, multiply the excluded gain by 7 percent and, under the 2025 form instructions, enter it on Form 6251, line 2h ([Instructions for Form 6251](https://www.irs.gov/pub/irs-pdf/i6251.pdf)). The Act confirms no preference for later stock, including 50 and 75 percent new-regime stock (section 70431(a)(4)).
- **NIIT, individuals:** 3.8 percent of the lesser of net investment income or the positive excess of modified AGI over USD 250,000 (joint or surviving spouse), USD 125,000 (married filing separately), or USD 200,000 (other individuals). Excluded gain is outside the net-gain component; the taxable remainder may enter it after relevant deductions. Modified AGI uses section 1411(d)'s net section 911 foreign-income exclusion addback when applicable. Merely crossing the threshold does not charge 3.8 percent on every taxable dollar ([26 U.S.C. 1411](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm)).

For an estate or trust, section 1411 instead applies 3.8 percent to the lesser of undistributed net investment income or AGI above the start of its highest section 1(e) bracket for that year. Individual thresholds do not apply to a trust/estate calculation. Obtain the filing year's official section 1(e) highest-bracket threshold before computing that result; a missing threshold is a NON-USABLE HOLD. Check this point with one of our partner accountants. Section 1411 excludes nonresident aliens and the charitable trusts specified in subsection (e); other cross-border QSBS consequences are held below.

### Historical 2025 returns (ordinary extension date was 15 October 2026)

- No new-regime stock can have met 3 years in 2025. An ordinary calendar-year 2025 return uses the old dollar-cap rules. A fiscal taxable year beginning after July 4, 2025 uses the amended cap rules; do not classify a fiscal return solely by its ending year.
- The 2025 Schedule D instructions give the 50, 75 and 100 percent windows and the gross-assets test ("$75 million ($50 million if the stock was issued on or before July 4, 2025)").
- The 2025 Schedule D instructions say the 7 percent AMT amount goes on "line 13 of Form 6251"; the 2025 Form 6251 instructions put it on line 2h, and those govern the form. Use line 2h.
- A section 1045 election for a 2025 sale is due with the 2025 return, including extensions (15 October 2026 if extended) ([IRS extensions page](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)).
- As of 28 November 2026, the ordinary 15 October 2026 extension/automatic six-month amended-election window has passed. Late elections, disaster relief and other exceptional deadlines are NON-USABLE HOLDs pending the taxpayer-specific authority. Check this point with one of our partner accountants.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Redemption from the seller or a related person | Not QSBS if the corporation bought any of its stock from the seller or a related person (section 267(b) or 707(b)) in the 4-year period beginning 2 years before issue. Ignored unless the amount paid exceeds USD 10,000 and more than 2 percent of the stock held by the seller and related persons is bought | [26 U.S.C. 1202(c)(3)(A)](https://uscode.house.gov/us/usc/t26/s1202/); [Treas. Reg. 1.1202-2(a)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/xhtml/CFR-2025-title26-vol13-sec1-1202-2.html) |
| Significant redemption from anyone | Stock issued is not QSBS if, in the 2-year period beginning 1 year before issue, buybacks exceed 5 percent of the value of all stock at the start of that period. Ignored unless the amount paid exceeds USD 10,000 and more than 2 percent of outstanding stock is bought | [26 U.S.C. 1202(c)(3)(B)](https://uscode.house.gov/us/usc/t26/s1202/); [Treas. Reg. 1.1202-2(b)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/xhtml/CFR-2025-title26-vol13-sec1-1202-2.html) |
| Buybacks disregarded | (1) Stock the seller acquired for services as an employee or director, bought on retirement or other bona fide termination of those services (merely being an investor/director is insufficient: the services-acquisition connection must be established). (2) Stock held before death by the decedent or spouse (or both), by the decedent and a joint tenant, or by a trust revocable by the decedent or spouse, bought from the estate, a beneficiary, heir, surviving joint tenant or surviving spouse, or a trust set up by the decedent or spouse, within 3 years and 9 months of death. (3) Stock bought incident to the seller's disability or mental incompetency, or divorce (section 1041(c)). A shareholder's transfer of stock to an employee or independent contractor is not a buyback | [Treas. Reg. 1.1202-2(c), (d)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/xhtml/CFR-2025-title26-vol13-sec1-1202-2.html) |
| Gift or death | Donee or heir is treated as acquiring the stock the same way as the transferor, with the holding period tacked | [26 U.S.C. 1202(h)(1), (2)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Partnership distribution | Qualifies if the partner meets the pass-through holding tests at the time of the distribution | [26 U.S.C. 1202(h)(2)(C)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Conversion of QSBS into other stock of the same corporation | New stock is QSBS and the holding period tacks | [26 U.S.C. 1202(f)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Section 351 or 368 exchange of QSBS for non-QSBS stock | New stock is QSBS acquired when the old stock was. If the new issuer is not a qualified small business, the exclusion is limited to the gain at the exchange. A section 351 exchange also needs control of the corporation whose stock was exchanged | [26 U.S.C. 1202(h)(4)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Offsetting short position (short sale, put or similar, including by a related person) | No exclusion unless the stock had already met the holding period when the position began and the seller elects to recognize gain as if sold at fair market value that day | [26 U.S.C. 1202(j)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Multiple trusts | For purposes of subchapter J, section 643(f) addresses trusts with substantially the same grantor and primary beneficiaries and a principal purpose of avoiding chapter 1 tax; spouses count as one person. It does not by itself prove a separate QSBS cap for each trust | [26 U.S.C. 643(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartA-sec643.htm) |
| Joint return | Gain taken into account is split equally between the spouses for later years. The equal allocation for later years is explicit. A proposed doubled joint-return limit or a one-limit default is not established here: NON-USABLE HOLD. Check this point with one of our partner accountants. | [26 U.S.C. 1202(b)(3)](https://uscode.house.gov/us/usc/t26/s1202/) |
| Installment sale of unlisted QSBS | Exclusion each year = total exclusion x (eligible gain recognized that year / total eligible gain) | [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) |
| Fiscal-year seller | The new cap rules apply from the first taxable year beginning after July 4, 2025, which may start in 2025 | [Public Law 119-21, section 70431(b)(4)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Acquisition date | NON-USABLE HOLD until documented; the date picks the regime. Check this point with one of our partner accountants. |
| Gross-asset history before and immediately after issue | NON-USABLE HOLD until documented; missing evidence is not a finding that the stock legally fails. Check this point with one of our partner accountants. |
| Earlier gain from the same issuer | Obtain prior returns and the eligible-gain tracker; hold the available-dollar-limit result until documented. Check this point with one of our partner accountants. |
| Section 83(b) election on restricted stock | Obtain the election and filing evidence; the holding-date output is a NON-USABLE HOLD until documented. Check this point with one of our partner accountants. |
| Joint-return dollar limit or separate trust limits | NON-USABLE HOLD; do not assume either one shared limit or automatic multiplication. Check this point with one of our partner accountants. |
| Excluded-field analysis | NON-USABLE HOLD until the facts establish the activity classification. Check this point with one of our partner accountants. |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| The company was ever an S corporation or taxed as a partnership | C corporation status for substantially all of the holding period may fail |
| Revenue from consulting, health, finance or other listed fields | Section 1202(e)(3) excludes the business |
| Large cash or securities balances after year 2 | The 50 percent working capital and 10 percent portfolio limits |
| A buyback near a funding round | Either redemption window can taint the whole issue |
| Gifts to several trusts before a sale | Section 643(f) aggregation and assignment-of-income risk |
| A sale of new-regime stock before the 5-year date | Only 50 or 75 percent is excluded; the rest is taxed at up to 28 percent plus NIIT |

## Worked cases

These are hypothetical. Except for explicit failure/hold cases, they assume every QSBS test and the available issuer limit are documented. Future cases retain their original years and the unindexed USD 15,000,000 model input, not a forecast of that year's indexed limit. Tax-rate models assume the stated maximum rate applies to the entire modeled taxable gain, no losses or deductions, and sufficient modified-AGI excess for the full NIIT base; actual tax requires the lesser-of calculation above.

**Case 1, a decision: sell new-regime stock at 3, 4 or 5 years?** A founder acquired stock at original issue in September 2025 for USD 1,000,000 and has an offer that values the gain at USD 8,000,000; the buyer will pay the same whenever the deal closes. The cap is the greater of USD 15,000,000 (unindexed) or 10 x USD 1,000,000, so the whole USD 8,000,000 is eligible. At 3 years (September 2028 or later): 50% excluded, USD 4,000,000 of section 1202 gain; at the 28 percent maximum plus 3.8 percent NIIT, tax up to USD 1,272,000. At 4 years: 75% excluded, USD 2,000,000 taxable, tax up to USD 636,000. At 5 years: 100% excluded, no federal tax. The modeled difference between the September 2028 three-year sale and September 2030 five-year sale is USD 1,272,000; the September 2029 four-year model is USD 636,000. This comparison alone does not determine when to sell; the actual deal risk, future law and continued qualification remain necessary inputs.

```oa-check
name: QSBS new regime, sell at 3, 4 or 5 years (gain USD 8,000,000)
inputs:
  gain: 8000000
  basis: 1000000
  dollar_limit: 15000000
  top_rate: 0.318
steps:
  - eligible: min(gain, max(dollar_limit, 10 * basis))
  - taxable_3yr: eligible - eligible * 0.50
  - taxable_4yr: eligible - eligible * 0.75
  - taxable_5yr: eligible - eligible * 1.00
  - tax_3yr: taxable_3yr * top_rate
  - tax_4yr: taxable_4yr * top_rate
  - saving_waiting_to_5yr: tax_3yr - taxable_5yr * top_rate
expected:
  eligible: 8000000.00
  taxable_3yr: 4000000.00
  tax_3yr: 1272000.00
  tax_4yr: 636000.00
  saving_waiting_to_5yr: 1272000.00
```

**Case 2, a 2026 sale of 2015 stock (old regime, 100 percent).** Acquired at original issue in March 2015 for USD 50,000 cash; sold in 2026 for USD 30,000,000. Gain USD 29,950,000. Cap = greater of USD 10,000,000 or 10 x USD 50,000 = USD 500,000, so USD 10,000,000. Excluded 100% of that: USD 10,000,000. Taxable long-term gain USD 19,950,000 at the normal rates (not 28 percent gain); no AMT preference. Had the seller bought the same stock after July 4, 2025, the cap would be USD 15,000,000, but no such stock can be sold with an exclusion in 2026.

```oa-check
name: QSBS old regime, 2026 sale of 2015 stock
inputs:
  amount_realized: 30000000
  basis: 50000
  dollar_limit: 10000000
  exclusion_pct: 1.00
steps:
  - gain: amount_realized - basis
  - cap: max(dollar_limit, 10 * basis)
  - excluded: min(gain, cap) * exclusion_pct
  - taxable_ltcg: gain - excluded
expected:
  gain: 29950000.00
  cap: 10000000.00
  excluded: 10000000.00
  taxable_ltcg: 19950000.00
```

**Case 3, 2026 sale of 2008 stock (50 percent, AMT).** Basis USD 400,000; gain USD 2,000,000. Cap = greater of USD 10,000,000 or USD 4,000,000, so the whole USD 2,000,000 is eligible. Excluded 50%: USD 1,000,000. Section 1202 gain (28 percent rate): USD 1,000,000, AMT preference: 7% x USD 1,000,000 = USD 70,000. The 2025 form mapping is worksheet line 2 and Form 6251 line 2h; the 2026 line mapping is held pending that edition.

**Case 4, gross-assets boundary.** A C corporation with aggregate gross assets of USD 74,000,000 issues stock for USD 2,000,000 cash in October 2025. Immediately after issue, gross assets are USD 76,000,000, above USD 75,000,000: stock issued in that round is not QSBS. Exceeding the gross-assets limit later does not by itself retroactively fail earlier qualifying stock; its other continuing tests still apply.

**Case 5, excluded field.** Consulting is a listed field. A company whose main business is placing its engineers with clients to deliver consulting projects should be treated as excluded unless counsel concludes otherwise; its stock fails however long it is held. Selling software that customers run themselves presents different facts, but a software label alone does not prove qualification. Mixed businesses and the placing-engineers-versus-product distinction need a documented section 1202(e)(3) analysis; an unresolved classification is a NON-USABLE HOLD. Check this point with one of our partner accountants.

**Case 6, section 1045 rollover.** QSBS held 8 months (basis USD 500,000) is sold for USD 3,000,000, a gain of USD 2,500,000. Within 60 days, USD 2,000,000 of other QSBS is bought. Recognized gain = USD 3,000,000 minus USD 2,000,000 = USD 1,000,000. Postponed gain USD 1,500,000. Replacement basis USD 2,000,000 minus USD 1,500,000 = USD 500,000. The 2025 Form 8949 mapping is code R with USD 1,500,000 negative in column (g); use the sale-year instructions before filing.


## Earlier examples and planning destinations

The following preserve the earlier 2025 Guide's subjects and example years. **Model arithmetic is not a forecast or an approved filing position.** An unindexed USD 15,000,000 cap or a supplied state/gift-tax rate remains a model input where stated. No current state conformity or gift/estate-tax conclusion is supplied by these federal-law calculations.

**H1, September 2025 stock, late-2029 sale.** Original-issue basis USD 1,000,000, gain USD 40,000,000, holding period four but less than five years. Using the original unindexed USD 15,000,000 cap against USD 10,000,000 of ten-times basis: eligible gain USD 15,000,000; 75% exclusion USD 11,250,000; section 1202 gain USD 3,750,000; gain above the cap USD 25,000,000 at normal long-term rates. No section 57(a)(7) preference. The actual indexed 2029 dollar-limit output is a NON-USABLE HOLD; do not replace the sale with a 2026 sale. Check this point with one of our partner accountants.

**H2, Earlier gross-assets boundary.** Keep the earlier USD 74,000,000 before issue plus USD 5,000,000 cash raise = USD 79,000,000 after issue. For the original post–July 4, 2025 issuance assumption, that is above USD 75,000,000 and fails the issue test. This is distinct from current Case 4's USD 2,000,000 round and USD 76,000,000 result.

**H3, Earlier rollover figures.** Proceeds USD 5,000,000, basis USD 500,000, gain USD 4,500,000; qualifying replacement cost USD 3,000,000 within 60 days. Conditional on stock actually held more than six months and every other section 1045 condition: recognized gain USD 2,000,000; deferred gain USD 2,500,000; replacement basis USD 500,000. The original case supplies no acquisition/sale year or exact holding period; none is invented here. It is distinct from current Case 6's eight-month, USD 3,000,000 sale.

**H4, Four-holder stacking model.** Original 1,000,000 shares, USD 1,000 basis, USD 200 exit price per share: proceeds USD 200,000,000 and gain USD 199,999,000. Three 250,000-share gifts to a spouse and two children leave the founder with 250,000 shares: four holders, not five. The hypothetical single USD 15,000,000 versus aggregate USD 60,000,000 exclusion model gives taxable gain USD 184,999,000 versus USD 139,999,000; extra modeled exclusion USD 45,000,000 at the supplied 23.8% model rate gives USD 10,710,000. The actual eligibility of separate limits, joint-return treatment, grantor/non-grantor ownership, multiple trusts, gift completion and pre-sale assignment of income are **NON-USABLE HOLDs**. The older narrative also mentioned three child trusts without reconciling its share allocation; that is not an additional usable cap. Check this point with one of our partner accountants.

**H5, Historical California model.** The earlier 2025 discussion treated a USD 100,000,000 exit as USD 100,000,000 gain without supplying basis, assumed USD 15,000,000 federally excluded, and used model rates 23.8% federal and 13.3% state. Those inputs multiply to USD 20,230,000 federal, USD 13,300,000 state, and USD 33,530,000 combined (33.53% of the input gain). Actual basis, exclusion availability, year-specific conformity, rate and state tax are **NON-USABLE HOLDs**; 13.3% is preserved as an old model input, not asserted as a current California rate. Check this point with one of our partner accountants.

**H6, Contributed IP.** Original IP fair market value USD 10,000,000, tax basis zero, and unindexed dollar-cap input USD 15,000,000. Section 1202(i)(1) supplies a USD 10,000,000 minimum basis **for section 1202**, giving a USD 100,000,000 ten-times-basis comparator; the QSBS holding date starts at that property exchange. This does not establish a general tax-basis step-up, recognize built-in gain automatically, or exclude pre-contribution appreciation. No sale price or gain was supplied. Ordinary basis, section 351 qualification and the resulting transaction tax are NON-USABLE HOLDs pending the actual exchange facts. Check this point with one of our partner accountants.


**H7, Original SaaS founder, 2032 exit.** A domestic C-corporation SaaS founder receives 5,000,000 shares in the original 2025 post-enactment issuance assumption, pays USD 5,000 (also the original initial-assets input), and files section 83(b) within 30 days. The founder sells in **2032**, seven years later, for USD 100 per share, and is a Texas resident. Proceeds USD 500,000,000; gain USD 499,995,000; ten-times-basis USD 50,000. Using the original unindexed USD 15,000,000 cap gives taxable gain USD 484,995,000. At the supplied maximum-rate model inputs 20% plus 3.8%, the components are USD 96,999,000 and USD 18,429,810, total USD 115,428,810 (about 23.1% of gain). Without the model exclusion, USD 118,998,810; model difference USD 3,570,000. The old California alternative's supplied 13.3% input multiplies to USD 66,499,335 and combined USD 181,928,145. Actual **2032** indexed cap, federal tax and Texas/California tax/residence consequences are NON-USABLE HOLDs; no state-zero result is established here. Check this point with one of our partner accountants.

**H8, Original employee, 2027 exit.** Employee joined the Series A startup in **2022**, early-exercised NSOs for USD 250,000 in **2022** with a section 83(b) election; issuer assets USD 30,000,000, within the then USD 50,000,000 ceiling. Sale in **2027**, five years two months later, for USD 25,000,000; Washington resident. Gain USD 24,750,000, ten-times basis USD 2,500,000; old-regime cap USD 10,000,000, exclusion USD 10,000,000, taxable gain USD 14,750,000 and no section 57(a)(7) preference. The original federal maximum-rate/full-NIIT model gives USD 2,950,000 plus USD 560,500 = USD 3,510,500, subject to the stated assumptions.

The older Washington illustration applied a **2025** deduction input USD 270,000 to that **2027** sale: USD 14,480,000 at its supplied 7% input = USD 1,013,600; combined model USD 4,524,100 (about 18.3% of gain). Its supplied 2.9% surcharge above USD 1,000,000 then gives USD 390,920, state model USD 1,404,520 and combined USD 4,915,020 (about 19.9%). Those are preserved arithmetic inputs, **not verified 2027 Washington law**. The earlier erroneous USD 1,714,100 state / USD 5,224,600 combined outputs are withdrawn. Actual Washington **2027** tax, deduction and conformity are NON-USABLE HOLDs; do not silently change the exit to 2025. Check this point with one of our partner accountants.

**H9, Original healthtech family/trust case, 2026 gifts and 2030 sale.** The founder's domestic C corporation has the original **2025** post-enactment issuance assumption, 1,000,000 shares for USD 1,000, and section 83(b). Business facts remain **95% software licensing / 5% implementation and training**, no direct patient care. Those facts alone do not prove that the business avoids the health/consulting exclusions; there is no automatic revenue-percentage safe harbor.

In **2026**, shares are valued at USD 5 each. The original three 250,000-share gifts are to a US-citizen spouse and two non-grantor dynasty trusts for different minor children, with different trustees/beneficiaries and asserted non-tax purposes; the spouse receives separate property under the original community-property/prenuptial facts. Each gift's model value is USD 1,250,000; all three USD 3,750,000. Founder retains 250,000 shares, so **four holders**. The older “four gifts/five holders” statement conflicts with these share inputs and is withdrawn.

Keep the original **2030**, five-plus-year sale at USD 200 per share: total proceeds USD 200,000,000; each holder's 250,000 shares produce USD 50,000,000 proceeds, USD 250 allocated original basis, USD 49,999,750 gain and USD 2,500 ten-times-basis comparator. Using only a model of a separate unindexed USD 15,000,000 limit for each, taxable model gain is USD 34,999,750 each / USD 139,999,000 total; single-limit model USD 184,999,000; difference USD 45,000,000 and USD 10,710,000 at the original 23.8% model input.

The old gift-tax illustration separately assumed a marital deduction for the spouse, USD 2,500,000 of trust gifts, present-interest/Crummey eligibility and gift splitting. Its **USD 19,000 × 2 spouses × 2 trusts = USD 76,000** input produced USD 2,424,000 taxable gifts / USD 1,212,000 per spouse. It then improperly used a **2025 USD 13,990,000** exemption input for **2026** gifts, producing about USD 12,780,000 each / USD 25,560,000 remaining. An earlier variant used four donees, USD 152,000 annual exclusions, USD 27,980,000 combined lifetime exemption and about USD 23,000,000 remaining. These contradictory legacy figures are **not usable gift-tax answers**.

Healthtech qualification, timely election, completed gifts, assignment of income, separate QSBS limits, section 643(f), grantor status, marital deduction, annual exclusions, gift splitting, gift/GST exemption, Form 709, future indexed limit, and the original Florida/California alternatives are **NON-USABLE HOLDs** pending their own facts and authorities. No prior “reviewer confirmed” statement supplies proof. Check this point with one of our partner accountants.

### Destinations for the remaining earlier topics

| Original topic | Current destination / usable boundary |
| --- | --- |
| 2025 federal QSBS, old acquisition windows, 2026 corrections and later exits | Rate/cap method, historical 2025 filing section, Cases 1–6 and H1–H9; no year is substituted |
| California, New York, New Jersey, Massachusetts, Washington, Texas, Florida, Pennsylvania, Mississippi, Alabama, Illinois and the old “other 35 states” grouping; relocation/domicile and state QSBS conformity | R-QSBS-STATE and H5, H7–H9. Each year/state output is a NON-USABLE HOLD; no group-wide conformity or zero-tax assumption. Check this point with one of our partner accountants. |
| Gift/death tacking, trust stacking, grantor/non-grantor ownership, death basis, spouse/community-property ownership, Crummey powers, gift splitting, annual/lifetime/GST exemptions and Form 709 | Section 1202(h) tacking remains; H4 and H9 retain the planning inputs. All additional ownership/gift/estate-tax results are NON-USABLE HOLDs. Check this point with one of our partner accountants. |
| Binding sale, LOI/term sheet, pre-sale gift timing and assignment of income | Preserve as planning questions, not a guaranteed “gift before signing” safe harbor. NON-USABLE HOLD. Check this point with one of our partner accountants. |
| Options, warrants, ISO/NSO exercise, early exercise, vesting, cashless exit exercise; 2024 SAFE/convertible instrument converting in 2025 | Exercise/property-transfer and section 83 rules above; no automatic SAFE/debt characterization or tacking from the instrument's purchase. The specific instrument, compensation/AMT treatment and exit-date rollover outcome are NON-USABLE HOLDs. In particular, an immediate exercise/sale does not meet section 1045's actual more-than-six-month holding test. Check this point with one of our partner accountants. |
| RIC/open- or closed-end fund, partnership or S-corporation owner; LLC/S-corporation conversion, stock split/dividend/recapitalization, stock-for-stock or cash merger, dissolution | Section 1202(g), (f), (h) and (i) set the proven boundaries; a former entity classification, secondary purchase or cash disposition is not automatically cured. Transaction-specific qualification/basis/recognition is a NON-USABLE HOLD. Check this point with one of our partner accountants. |
| Contributed IP, pre-contribution appreciation, later capital contributions | Section 1202(i) and H6; no general basis step-up, automatic recognition or post-issue basis inflation of the ten-times-basis cap |
| Hedges/short positions; empowerment-zone 60% stock; SSBIC; foreign seller/trust/estate | Statutory boundaries below; R-QSBS-SPECIAL holds the fact-specific result. Section 1202(a)(2)'s special 60% rule does not apply to gain attributable to periods after 31 December 2018; an SSBIC active-business waiver is not a waiver of every QSBS condition. Check this point with one of our partner accountants. |

The former 90%-of-holding-period shortcut, 25–30% service-revenue threshold, USD 5,000,000 working-capital “safe harbor,” automatic two-year cash safe harbor, unlimited cap refresh, automatic trust multiplication, IPO/audit statistics, and unsupported practitioner/case-law assurances supply no rule in this Guide. Their legal conclusions are withdrawn; the underlying relevant business/case facts remain above.

## When to refuse or refer

Each unresolved outcome in this table is a **NON-USABLE HOLD**, not a determination that the stock is taxable or ineligible. **Check this point with one of our partner accountants.** The ordinary proven federal rules and calculations above remain usable when their facts are established.

| Code | Situation | Action |
| --- | --- | --- |
| R-QSBS-SCORP | The corporation was ever an S corporation or taxed as a partnership during the holding period, or the C corporation period is unclear | Refer to counsel |
| R-QSBS-REORG | Stock from a section 351 or 368 exchange, an LLC-to-corporation conversion, a merger for acquirer stock, or a section 1045 rollover spanning July 4, 2025 | Refer: acquisition date and limit need specialist analysis |
| R-QSBS-FIELD | Material revenue in any excluded field, or value that depends on key people | Refer for a documented section 1202(e)(3) analysis; do not guess |
| R-QSBS-ASSETS | Gross-asset history before and immediately after issue cannot be documented | Hold the qualification output pending evidence |
| R-QSBS-REDEEM | A buyback near the issue date that may exceed the de minimis amounts | Refer |
| R-QSBS-STACK | Gifts to several trusts, or pre-sale gifts to multiply the per-issuer limit | Refer (section 643(f), assignment of income) |
| R-QSBS-SPECIAL | Empowerment zone (60 percent) stock, SSBIC stock, a short position or hedge, a non-resident alien seller, a foreign trust or estate | Refer |
| R-QSBS-STATE | Any state tax question | Check the state's statute and revenue department |

## Filing and payment

**Form-edition boundary:** the read Form 8949, Schedule D and Form 6251 instructions are for **2025**. The codes and lines in items 1–4 are historical 2025 mappings, not confirmed 2026 filing instructions. The 2026 line/code mapping is a NON-USABLE HOLD until the applicable final instructions are read. Check this point with one of our partner accountants. This does not hold the statutory 2026 exclusion or rollover calculations.

1. Report each QSBS sale on Form 8949, Part II (long-term), as if no exclusion were claimed; enter code **Q** in column (f) and the exclusion as a negative number in column (g) ([Instructions for Form 8949](https://www.irs.gov/pub/irs-pdf/i8949.pdf)).
2. For a section 1045 rollover, report in Part I or Part II by holding period; enter code **R** and the postponed gain as a negative number in column (g).
3. For installment sales of unlisted QSBS, report the gain from Form 6252 on Schedule D, line 11, and the prorated exclusion with code Q.
4. Complete the 28% Rate Gain Worksheet (line 2) for 50, 60 and 75 percent stock, and Form 6251 line 2h for stock acquired before 28 September 2010.
5. For an ordinary US individual calendar-year 2026 return, section 6072(a) gives **15 April 2027**. A timely requested ordinary six-month filing extension gives **15 October 2027**; payment remains due in April under section 6151. Foreign-resident, disaster, fiscal-year and other special deadlines require their own applicable relief. A section 1045 election is due by the return due date including extensions; the limited amended-election procedure above has separate conditions.

## Completion checklist

- Seller is not a corporation; pass-through holding tests met if relevant.
- Original-issue evidence (board consent, subscription, payment, ledger) and the acquisition date after section 1223, placed on one side of July 4, 2025.
- Gross-asset evidence at all times on or after 10 August 1993 before issue and immediately after, against USD 50,000,000 or USD 75,000,000 by issue date.
- C corporation status and active business test for substantially all of the holding period, with the 80 percent, working capital, portfolio and real estate limits checked.
- Excluded-field analysis on file.
- Redemption review for both windows, with the de minimis tests.
- Holding period met (more than 5 years, or at least 3 years for new stock).
- Per-issuer cap computed, with prior-year and same-year reductions and the zero-after-exceeded rule; running tracker kept.
- Exclusion applied to the capped gain; section 1202 gain, gain above the cap, AMT and NIIT classified.
- Sale-year Form 8949, Schedule D, Form 6251 and Form 8960 instructions checked; 2025 codes/lines are not used as proof of 2026 mappings; section 1045 election on a timely return.
- State treatment checked separately.

## Sources

Original source-read dates remain in the Guide history. The operative passages used for this correction were actually read on 28 November 2026; successful link access alone was not used as proof.

| Source and operative scope | URL | Read on |
| --- | --- | --- |
| Current section 1202, including original issue, all caps/holding periods, assets, businesses, transfers and editorial/effective-date notes | https://uscode.house.gov/us/usc/t26/s1202/ | 2026-11-28 |
| Public Law 119-21, section 70431: enacted amendments and separate effective dates | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-28 |
| Pre-amendment section 1202: historical USD 50,000,000 issue test | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partI-sec1202.htm | 2026-11-28 |
| Section 1045: rollover, purchase, basis and actual holding tests | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partIII-sec1045.htm | 2026-11-28 |
| Section 1223(13): rollover tacking and its exceptions | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIII-sec1223.htm | 2026-11-28 |
| Section 83(b)(2): 30-day election | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec83.htm | 2026-11-28 |
| Section 1(h)(1), (4), (7): capital gain categories and maximum rates | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm | 2026-11-28 |
| Section 57(a)(7), read together with Act section 70431(a)(4) | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec57.htm | 2026-11-28 |
| Section 1411: lesser-of NIIT bases, individual thresholds and exceptions | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm | 2026-11-28 |
| Section 643(f): multiple-trust rule and its scope | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapJ-partI-subpartA-sec643.htm | 2026-11-28 |
| Treas. Reg. 1.1202-2: redemption windows, de minimis denominators and exceptions | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol13/xhtml/CFR-2025-title26-vol13-sec1-1202-2.html | 2026-11-28 |
| Treas. Reg. 1.83-4(a): restricted-stock holding period | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol2/xhtml/CFR-2025-title26-vol2-sec1-83-4.html | 2026-11-28 |
| 2025 Schedule D instructions: historical Q/R, installment and election procedure (AMT line cross-reference corrected using Form 6251) | https://www.irs.gov/pub/irs-pdf/i1040sd.pdf | 2026-11-28 |
| 2025 Form 8949 instructions: rollover adjustment table | https://www.irs.gov/pub/irs-pdf/i8949.pdf | 2026-11-28 |
| 2025 Form 6251 instructions: line 2h and pre-28-September-2010 stock | https://www.irs.gov/pub/irs-pdf/i6251.pdf | 2026-11-28 |
| Section 6072(a): ordinary calendar/fiscal income-tax filing date | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-11-28 |
| Section 6081(a): filing extension boundary | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partVI-sec6081.htm | 2026-11-28 |
| Section 6151(a): payment without regard to filing extension | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap62-subchapA-sec6151.htm | 2026-11-28 |
| IRS individual-return extension procedure and special situations | https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return | 2026-11-28 |

Not yet confirmed: 2026 form-line/code mappings, later indexed filing limits and the specifically marked state/gift/trust/transaction results are NON-USABLE HOLDs. Check this point with one of our partner accountants.
