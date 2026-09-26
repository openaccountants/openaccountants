---
name: us-section-1202-qsbs
description: Tier 2 US federal content skill for IRC §1202 Qualified Small Business Stock gain exclusion. Covers OBBBA P.L. 119-21 (July 2025) expansion including the new tiered exclusion (50% at 3 years, 75% at 4 years, 100% at 5 years), the $75M gross-asset cap (raised from $50M), the $15M per-issuer cap (raised from $10M), the §1202(e)(3) SSTB exclusion list, §1045 rollover with 60-day reinvestment, AMT treatment for post-2010 stock, state conformity (CA non-conforming), QSBS-destroying events (S-corp conversion, buyback, recapitalization edge cases), family stacking strategies, SAFE/convertible note conversion treatment, and Form 8949 Code Q reporting. Tax year 2025.
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US §1202 qualified small business stock (QSBS) exclusion

Written for **tax year 2026** (returns filed in 2027), with a dated section for **2025 returns** still open on extension. It covers a non-corporate US taxpayer (individual, trust, estate, or a partner/shareholder of a pass-through entity) who sells stock in a domestic C corporation and wants to exclude gain under IRC §1202 or defer it under §1045. The law is the statute as amended by P.L. 119-21 (the One Big Beautiful Bill Act, enacted July 4, 2025). [26 USC 1202](https://www.law.cornell.edu/uscode/text/26/1202)

The rules now split on dates. **Acquisition date** decides the exclusion percentage, holding period and per-issuer dollar limit. **Issue date** decides the gross-assets limit. The "applicable date" in the statute is July 4, 2025. [26 USC 1202](https://www.law.cornell.edu/uscode/text/26/1202)

This Guide covers federal tax only. States set their own rules, and some do not follow §1202. This Guide does not state any state's position, so check the law of each state where the seller was resident.

## Ask the client first

- Who is the seller: an individual, a trust or estate, or a pass-through entity (partnership, S corporation, RIC, common trust fund)? A corporation cannot use §1202. [26 USC 1202(a)](https://www.law.cornell.edu/uscode/text/26/1202)
- How was the stock acquired: at original issue from the corporation (directly or through an underwriter) for money, property other than stock, or services? Or by gift, at death, in a partnership distribution, by converting other stock of the same corporation, or in a §351/§368 exchange? Stock bought from another shareholder does not qualify. [26 USC 1202(c), (f), (h)](https://www.law.cornell.edu/uscode/text/26/1202)
- What is the exact acquisition date, and is it on or before, or after, July 4, 2025? For options, warrants, SAFEs and convertible notes, get the exercise or conversion date. For restricted stock received for services, ask whether a §83(b) election was filed: without one, the holding period starts just after each tranche substantially vests; with one, just after the transfer. [26 CFR 1.83-4(a)](https://www.law.cornell.edu/cfr/text/26/1.83-4)
- What was the exact issue date of the stock, and what were the corporation's aggregate gross assets (cash plus adjusted basis of other property, with contributed property at its value when contributed) at all times before issue and immediately after issue? Include every member of a more-than-50% parent-subsidiary group. [26 USC 1202(d)](https://www.law.cornell.edu/uscode/text/26/1202)
- Was the company a C corporation, and did it meet the active business test, for substantially all of the seller's holding period? Was there ever an S election or partnership classification?
- What does the company actually do? Get a revenue breakdown and asset list to test the excluded fields and the investment, real estate and portfolio-stock limits.
- Did the corporation buy back any of its own stock around the issue date, from the seller, a related person or anyone else? Get dates, amounts and values. [26 CFR 1.1202-2](https://www.law.cornell.edu/cfr/text/26/1.1202-2)
- How much §1202 gain from this issuer has the seller (and, on past joint returns, the spouse) already taken into account in earlier years?
- Sale details: date, amount realized, basis, any installment payments, escrow or earn-out, and any short sale, put or hedge on the stock.
- If the holding period is too short: did the seller buy other QSBS within 60 days of the sale, and does the seller want to elect §1045? [26 USC 1045](https://www.law.cornell.edu/uscode/text/26/1045)

## The method, step by step

1. **Check the seller.** It must be a taxpayer other than a corporation. For a pass-through entity, the owner must have held the interest on the day the entity acquired the stock and at all times after, until the entity sold it. The owner's share is capped by the interest held when the stock was acquired. [26 USC 1202(g)](https://www.law.cornell.edu/uscode/text/26/1202)
2. **Check the stock is QSBS.** Test original issue, qualified small business status at issue (gross assets), C corporation status and the active business test for substantially all of the holding period, and redemptions. All must pass. Use the tables below.
3. **Fix the acquisition date.** It is the first day the seller held the stock after the §1223 holding-period rules. Tacking from a gift, a death, a conversion of other stock of the same corporation (§1202(f)) or a §1045 rollover can therefore move the date earlier. That date picks the regime. [26 USC 1202(a)(6)(B)](https://www.law.cornell.edu/uscode/text/26/1202)
   - Stock received for property other than money or stock, including in a §351 incorporation or an LLC's conversion to a corporation, is treated as acquired on the date of that exchange. The property's holding period does not tack. [26 USC 1202(i)(1)(A)](https://www.law.cornell.edu/uscode/text/26/1202)
   - Stock received for services and subject to vesting is held from just after it substantially vests, or just after the transfer if a §83(b) election was made. Unvested tranches can therefore fall on different sides of July 4, 2025. Restricted stock granted before that date but vesting after it, with no §83(b) election, is new-regime stock for those tranches. [26 CFR 1.83-4(a)](https://www.law.cornell.edu/cfr/text/26/1.83-4)
4. **Check the holding period.** Stock acquired on or before July 4, 2025 must be held **more than 5 years**. Stock acquired after that date must be held **at least 3 years**. [26 USC 1202(a)(1), (b)(2)](https://www.law.cornell.edu/uscode/text/26/1202)
5. **Cap the eligible gain for each issuer.** The cap is the greater of the applicable dollar limit or 10 times the aggregate adjusted basis of the issuer's QSBS sold in the year. The cap limits the gain taken into account. The exclusion percentage is then applied to that capped gain. [26 USC 1202(b)](https://www.law.cornell.edu/uscode/text/26/1202)
6. **Apply the exclusion percentage** for the regime and holding period.
7. **Classify what remains.** Gain above the cap is long-term capital gain taxed at the normal §1(h) rates. The part of capped gain not excluded only because the percentage is below 100% is "section 1202 gain", taxed at a maximum of 28%. [26 USC 1(h)(4), (7)](https://www.law.cornell.edu/uscode/text/26/1)
8. **AMT and NIIT.** Only stock acquired on or before September 27, 2010 has an AMT preference (7% of the excluded amount). Excluded gain is not in taxable income, so it is not net investment income. [26 USC 57(a)(7)](https://www.law.cornell.edu/uscode/text/26/57)
9. **If the stock fails the holding period,** check a §1045 rollover (held more than 6 months, replacement QSBS bought within 60 days, election on a timely return).
10. **Report** on Form 8949 Part II with code Q (exclusion) or code R (rollover), then Schedule D and, for pre-September 28, 2010 stock, Form 6251.

## Thresholds and figures by date

Figures are statutory. The §1202(b) changes (the $15,000,000 limit and the new separate-return rule) apply to stock acquired after July 4, 2025, and to taxable years beginning after that date, so for a calendar-year taxpayer they first apply in 2026, not 2025. Inflation indexing of the $15,000,000 and $75,000,000 amounts starts only for taxable years beginning after 2026, and no indexed figure has been published yet. [26 USC 1202(b)(5), (d)](https://www.law.cornell.edu/uscode/text/26/1202)

| Item | Stock acquired (or, for gross assets, issued) on or before July 4, 2025 | Stock acquired (issued) after July 4, 2025 |
| --- | --- | --- |
| [Exclusion percentage](https://www.law.cornell.edu/uscode/text/26/1202) | 50% if acquired on or before Feb 17, 2009; 75% if acquired after Feb 17, 2009 and on or before Sept 27, 2010; 100% if acquired after Sept 27, 2010 | 50% after 3 years; 75% after 4 years; 100% after 5 years or more |
| Holding period | more than 5 years | at least 3 years |
| Per-issuer dollar limit | $10,000,000, less eligible gain from the issuer taken into account in earlier years | $15,000,000 (indexed after 2026), less earlier years' eligible gain from the issuer (any stock) and same-year eligible gain from stock acquired on or before July 4, 2025 |
| Married filing separately | $5,000,000 | one-half of the $15,000,000 amount in effect |
| Alternative basis cap | 10 times basis of the issuer's QSBS sold in the year | same |
| Gross assets at all times before issue and immediately after | $50,000,000 | $75,000,000 (indexed after 2026) |
| AMT preference | 7% of the excluded amount, only for stock acquired on or before Sept 27, 2010 | none |

Sources: [26 USC 1202](https://www.law.cornell.edu/uscode/text/26/1202), [26 USC 57](https://www.law.cornell.edu/uscode/text/26/57), [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)

- The $75,000,000 gross-assets limit applies to stock **issued** after July 4, 2025. Stock issued on or before that date is tested against $50,000,000. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)
- When indexing starts, each increase is rounded to the nearest multiple of $10,000. [26 USC 1202(b)(5)](https://www.law.cornell.edu/uscode/text/26/1202)
- **No top-up once used.** If eligible gain from stock of an issuer acquired after July 4, 2025 exceeds the dollar limit in any year, that issuer's dollar limit is zero for every later year, despite indexing. [26 USC 1202(b)(5)(B)](https://www.law.cornell.edu/uscode/text/26/1202)
- The 10-times-basis cap uses adjusted basis without any addition to basis after original issue. For stock received for property, basis is never less than the property's fair market value at the exchange. [26 USC 1202(b)(1), (i)](https://www.law.cornell.edu/uscode/text/26/1202)
- On a joint return, the gain taken into account is split equally between the spouses for later years. The statute does not say whether spouses filing jointly share one dollar limit or have one each. Treat the joint return as one limit unless counsel advises otherwise: the halving of the limit for married filing separately under §1202(b)(3)(A) implies one limit per married couple, but neither the statute nor IRS instructions say so directly. [26 USC 1202(b)(3)](https://www.law.cornell.edu/uscode/text/26/1202)
- For the effective dates: the percentage and holding-period changes (§70431(a)) and the per-issuer limit changes (§70431(b)) apply to taxable years beginning after July 4, 2025, and the gross-assets change applies to stock issued after July 4, 2025. [26 USC 1202 notes](https://www.law.cornell.edu/uscode/text/26/1202)

### What makes stock QSBS

| Test | Rule | Source |
| --- | --- | --- |
| Issuer | Domestic C corporation. Not a DISC or former DISC, RIC, REIT, REMIC or cooperative. | [§1202(d)(1), (e)(4)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Original issue | Issued after August 10, 1993. Acquired at original issue for money, property other than stock, or services (not underwriting). | [§1202(c)(1)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Gross assets | Cash plus adjusted basis of other property; contributed property counts at its value when contributed. The limit must not be exceeded at any time before issue, or immediately after issue counting the amount received. | [§1202(d)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Active business | For substantially all of the holding period, at least 80% of assets by value used in the active conduct of qualified trades or businesses. | [§1202(c)(2), (e)(1)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Working capital | Assets held as reasonably required working capital, or held for investment and reasonably expected to be used within 2 years for research or increased working capital, count as active. After the corporation has existed at least 2 years, no more than 50% of assets can qualify this way. | [§1202(e)(6)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Portfolio stock | Fails for any period in which more than 10% of asset value (net of liabilities) is stock or securities of non-subsidiary corporations. | [§1202(e)(5)(B)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Real estate | Fails for any period in which more than 10% of total asset value is real property not used in the active business. Owning, dealing in or renting real property is not an active business. | [§1202(e)(7)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Subsidiaries | A more-than-50% subsidiary is looked through for the active business test. The parent-subsidiary group is one corporation for the gross-assets test. | [§1202(d)(3), (e)(5)](https://www.law.cornell.edu/uscode/text/26/1202) |

"Substantially all" is not defined in the statute. Do not use a percentage test for it without authority for your facts.

### Excluded fields (not a qualified trade or business)

Under §1202(e)(3), the following do not qualify [26 USC 1202(e)(3)](https://www.law.cornell.edu/uscode/text/26/1202):

- services in health, law, engineering, architecture, accounting, actuarial science, performing arts, consulting, athletics, financial services or brokerage services;
- any business whose principal asset is the reputation or skill of one or more employees;
- banking, insurance, financing, leasing, investing or similar businesses;
- farming, including raising or harvesting trees;
- production or extraction of products eligible for percentage depletion under §613 or §613A;
- operating a hotel, motel, restaurant or similar business.

Assets used in start-up activities, research and experimental work, or in-house research for a future qualified business count as active. Software rights producing active business computer software royalties also count as active. [26 USC 1202(e)(2), (e)(8)](https://www.law.cornell.edu/uscode/text/26/1202)

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Redemption from the seller or a related person | Not QSBS if the corporation bought any of its stock from the seller or a related person (§267(b)/§707(b)) in the 4-year period beginning 2 years before issue. It is ignored only if $10,000 or less was paid, or no more than 2% of the stock held by the seller and related persons was bought. | [§1202(c)(3)(A)](https://www.law.cornell.edu/uscode/text/26/1202); [Reg. 1.1202-2(a)](https://www.law.cornell.edu/cfr/text/26/1.1202-2) |
| Significant redemption from anyone | Stock issued is not QSBS if, in the 2-year period beginning 1 year before issue, buybacks exceed 5% of the value of all stock at the start of that period. It is ignored only if $10,000 or less was paid, or no more than 2% of outstanding stock was bought. | [§1202(c)(3)(B)](https://www.law.cornell.edu/uscode/text/26/1202); [Reg. 1.1202-2(b)](https://www.law.cornell.edu/cfr/text/26/1.1202-2) |
| Buybacks ignored | (1) Stock the seller acquired for services as an employee or director, bought on the seller's retirement or other bona fide termination of those services (an investor director who paid cash does not qualify). (2) Stock held before death by the decedent or spouse (or both), by the decedent and a joint tenant, or by a trust revocable by the decedent or spouse, bought from the estate, a beneficiary, heir, surviving joint tenant or surviving spouse, or a trust set up by the decedent or spouse, within 3 years and 9 months of death. (3) Stock bought incident to the seller's disability or mental incompetency, or divorce (§1041(c)). Also: a shareholder's transfer of stock to an employee or independent contractor is not a buyback. | [Reg. 1.1202-2(c), (d)](https://www.law.cornell.edu/cfr/text/26/1.1202-2) |
| Gift or death | Donee or heir is treated as acquiring the stock the same way as the transferor, with the holding period tacked. | [§1202(h)(1), (2)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Partnership distribution | Qualifies if the partner meets the pass-through holding tests at the time of the distribution. | [§1202(h)(2)(C)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Conversion of QSBS into other stock of the same corporation | New stock is QSBS, and the holding period tacks. | [§1202(f)](https://www.law.cornell.edu/uscode/text/26/1202) |
| §351 or §368 exchange of QSBS for non-QSBS stock | New stock is treated as QSBS acquired when the old stock was acquired. If the new issuer is not a qualified small business, the exclusion is limited to the gain at the exchange. A §351 exchange also needs control of the corporation whose stock was exchanged. | [§1202(h)(4)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Offsetting short position (short sale, put, similar hedge, including by a related person) | No exclusion unless the stock had already met the holding period when the position began and the seller elects to recognize gain as if sold at fair market value that day. | [§1202(j)](https://www.law.cornell.edu/uscode/text/26/1202) |
| Multiple trusts | Trusts with substantially the same grantor and primary beneficiaries, and a principal purpose of tax avoidance, are treated as one trust. A husband and wife count as one person. | [§643(f)](https://www.law.cornell.edu/uscode/text/26/643) |
| Installment sale of unlisted QSBS | Exclusion for each year = total exclusion × (eligible gain recognized that year ÷ total eligible gain). | [Schedule D instructions](https://www.irs.gov/instructions/i1040sd) |

## §1045 rollover (60 days)

- **Who and what:** a taxpayer other than a corporation selling QSBS held for **more than 6 months** can elect to recognize gain only to the extent the amount realized exceeds the cost of other QSBS bought in the **60-day period beginning on the date of sale**. Gain treated as ordinary income cannot be rolled. [26 USC 1045(a)](https://www.law.cornell.edu/uscode/text/26/1045)
- **Replacement stock:** it must be QSBS, and it must meet the active business test for at least its first 6 months after purchase. [26 USC 1045(b)(4)](https://www.law.cornell.edu/uscode/text/26/1045); [Pub. 550](https://www.irs.gov/publications/p550)
- **Basis:** postponed gain reduces the basis of the replacement stock, in the order acquired. [26 USC 1045(b)(3)](https://www.law.cornell.edu/uscode/text/26/1045)
- **Holding period:** the replacement stock's holding period includes the old stock's, for §1202 purposes too, except for §1202(a)(2) and (c)(2)(A). It does not count for the 6-month test on a later rollover. [26 USC 1223(13)](https://www.law.cornell.edu/uscode/text/26/1223); [Pub. 550](https://www.irs.gov/publications/p550) Because the §1202 acquisition date is found after §1223, the statutory text treats replacement stock bought after July 4, 2025 for stock acquired on or before that date as acquired on the old stock's date, so it is old-regime stock ($10,000,000 limit, more than 5 years). No IRS guidance confirms this yet; document the reliance. [26 USC 1202(a)(6)(B)](https://www.law.cornell.edu/uscode/text/26/1202)
- **Election deadline:** make the election by the due date, including extensions, of the return for the year of sale. If the original return was filed on time, an amended return filed within 6 months after the due date (excluding extensions) marked "Filed pursuant to section 301.9100-2" is accepted. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)
- **Pass-through entities** can make the election. An owner who held the interest for the entity's whole holding period can also buy the replacement stock personally within the 60 days. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)

## Tax on what is not excluded

- **Section 1202 gain:** eligible gain minus the exclusion is 28% rate gain. On the 28% Rate Gain Worksheet, line 2, enter the exclusion for 50% stock, 2/3 of it for 60% stock, 1/3 of it for 75% stock, and nothing for 100% stock. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd); [26 USC 1(h)(7)](https://www.law.cornell.edu/uscode/text/26/1)
- **Gain above the per-issuer cap** is long-term capital gain taxed at the normal §1(h) rates. [26 USC 1(h)](https://www.law.cornell.edu/uscode/text/26/1)
- **AMT:** for stock acquired before September 28, 2010 and held more than 5 years, enter 7% of the excluded gain on Form 6251, line 2h. Stock acquired after September 27, 2010 has no preference, including 50% and 75% tier stock acquired after July 4, 2025. [Form 6251 instructions](https://www.irs.gov/instructions/i6251); [26 USC 57(a)(7)](https://www.law.cornell.edu/uscode/text/26/57)
- **NIIT:** the 3.8% tax reaches net gain only "to the extent taken into account in computing taxable income", so excluded gain is outside it. The taxable remainder counts if modified AGI exceeds $250,000 (joint or surviving spouse), $200,000 (single and head of household), or half the joint amount (married filing separately). [26 USC 1411](https://www.law.cornell.edu/uscode/text/26/1411)

## Worked cases

These are hypothetical. Each one assumes every QSBS test passes except where stated.

**Case 1: 2026 sale of 2015 stock (old regime, 100%).** Acquired at original issue in March 2015 for $50,000 cash; sold in 2026 for $30,000,000. Gain = $30,000,000 − $50,000 = $29,950,000. Cap = greater of $10,000,000 or 10 × $50,000 = $500,000, so $10,000,000. Excluded = 100% of $10,000,000 = $10,000,000. Taxable long-term gain = $29,950,000 − $10,000,000 = $19,950,000, at normal rates (not 28% gain). No AMT preference. [26 USC 1202](https://www.law.cornell.edu/uscode/text/26/1202)

**Case 2: 2026 sale of 2008 stock (50%, AMT).** Basis $400,000; gain $2,000,000. Cap = greater of $10,000,000 or $4,000,000, so the whole $2,000,000 is eligible. Excluded = 50% = $1,000,000. Section 1202 gain (28% rate) = $1,000,000. AMT preference = 7% × $1,000,000 = $70,000 on Form 6251, line 2h. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd); [Form 6251 instructions](https://www.irs.gov/instructions/i6251)

**Case 3: new-regime stock sold after 4 years (75%).** Acquired September 2025 for $1,000,000; sold in late 2029 after holding at least 4 but less than 5 years; gain $40,000,000. The 2029 dollar limit will be indexed and is not yet published, so this case uses the unindexed $15,000,000. Cap = greater of $15,000,000 or 10 × $1,000,000 = $10,000,000, so $15,000,000. Excluded = 75% × $15,000,000 = $11,250,000. Section 1202 gain = $15,000,000 − $11,250,000 = $3,750,000, which is 1/3 of the exclusion on worksheet line 2. Long-term gain above the cap, at normal §1(h) rates = $40,000,000 − $15,000,000 = $25,000,000. No AMT preference. [26 USC 1202](https://www.law.cornell.edu/uscode/text/26/1202)

**Case 4: gross-assets boundary.** A C corporation with aggregate gross assets of $74,000,000 issues stock for $2,000,000 cash in October 2025. Immediately after issue, gross assets are $74,000,000 + $2,000,000 = $76,000,000, which exceeds $75,000,000. Stock issued in that round is not QSBS. Stock issued earlier, when the corporation was within the limit, is not affected. [26 USC 1202(d)(1)](https://www.law.cornell.edu/uscode/text/26/1202)

**Case 5: excluded field.** Consulting is a listed field. A company whose main business is placing its engineers with clients to deliver consulting projects should be treated as excluded unless counsel concludes otherwise; its stock then fails however long it is held. A company selling software that customers run themselves is not in a listed field. Mixed businesses need a documented analysis. [26 USC 1202(e)(3)](https://www.law.cornell.edu/uscode/text/26/1202)

**Case 6: §1045 rollover.** QSBS held 8 months (basis $500,000) is sold for $3,000,000, a gain of $2,500,000. Within 60 days, $2,000,000 of other QSBS is bought. Recognized gain = $3,000,000 − $2,000,000 = $1,000,000. Postponed gain = $2,500,000 − $1,000,000 = $1,500,000. Replacement basis = $2,000,000 − $1,500,000 = $500,000. Report on Form 8949 with code R and $1,500,000 in column (g) as a negative. [26 USC 1045](https://www.law.cornell.edu/uscode/text/26/1045); [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)

## 2025 returns (due October 15, 2026 on extension)

- No stock acquired after July 4, 2025 can have met the 3-year holding period in 2025. That will first happen in July 2028. So every 2025 exclusion is old-regime stock held more than 5 years, with the $10,000,000 / 10-times-basis cap. [26 USC 1202](https://www.law.cornell.edu/uscode/text/26/1202)
- The 2025 Schedule D instructions give the 50%/75%/100% windows and the $75,000,000 ($50,000,000 for stock issued on or before July 4, 2025) gross-assets test. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)
- The 2025 Schedule D instructions say the 7% AMT amount goes on "line 13 of Form 6251". The 2025 Form 6251 instructions put it on line 2h, and those instructions govern the form. Use line 2h. [Form 6251 instructions](https://www.irs.gov/instructions/i6251)
- A §1045 election for a 2025 sale is due with the 2025 return, including extensions. For an extended return that is October 15, 2026. [Extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)
- Pub. 550 (2025) still describes only the pre-2025 dollar limit and uses loose holding-period wording. Rely on the statute and the Schedule D instructions.

## When to refuse or refer

- The corporation was ever an S corporation, or taxed as a partnership, during the seller's holding period, or the seller's C-corporation period is unclear. Refer to counsel.
- Stock came from a §351 or §368 exchange, an LLC-to-corporation conversion, a merger for acquirer stock, or a §1045 rollover spanning July 4, 2025 (the text points to old-regime treatment, unconfirmed by IRS guidance). The acquisition date and limit need specialist analysis.
- The issuer has material revenue in any excluded field, or its value depends on key people. Refer for a documented §1202(e)(3) analysis; do not guess.
- The gross-asset history before and immediately after issue cannot be documented. Treat the stock as not QSBS until it can.
- Any buyback near the issue date that may exceed the de minimis amounts.
- Gifts to several trusts, or pre-sale gifts to multiply the per-issuer limit. Refer (§643(f) and assignment-of-income risk).
- Empowerment-zone (60%) stock, SSBIC stock, a short position or hedge, a non-resident alien seller, or a foreign trust or estate. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)
- Any state tax question. Check the state's own statute and revenue department.

## Filing and payment steps with deadlines

1. Report each QSBS sale on Form 8949, Part II (long-term), as if no exclusion were claimed. Enter code **Q** in column (f) and the exclusion as a negative number in column (g). [Form 8949 instructions](https://www.irs.gov/instructions/i8949)
2. For a §1045 rollover, report in Part I or Part II by holding period. Enter code **R** and the postponed gain as a negative number in column (g). [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)
3. For installment sales of unlisted QSBS, report the gain from Form 6252 on Schedule D, line 11, and the prorated exclusion with code Q. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)
4. Complete the 28% Rate Gain Worksheet (line 2) for 50%, 60% and 75% stock, and Form 6251, line 2h, for pre-September 28, 2010 stock. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd); [Form 6251 instructions](https://www.irs.gov/instructions/i6251)
5. The 2026 return is due in April 2027. An extension moves the filing date, but not the payment date, to October 15. The §1045 election must be on a return filed by the extended due date. [Extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)
6. The 2026 versions of Form 8949, Schedule D and Form 6251 instructions were not published when this Guide was written. Check them for any change in codes or line numbers.

## Completion checklist

- [ ] Seller is not a corporation; pass-through holding tests met if relevant.
- [ ] Original-issue evidence (board consent, subscription, payment, ledger) and the acquisition date after §1223, placed on one side of July 4, 2025.
- [ ] Gross-asset evidence at all times before issue and immediately after, against the correct limit.
- [ ] C-corporation status and active business test for substantially all of the holding period, with the 80%, working-capital, portfolio and real estate limits checked. [26 USC 1202(e)](https://www.law.cornell.edu/uscode/text/26/1202)
- [ ] Excluded-field analysis on file.
- [ ] Redemption review for both windows, with de minimis tests.
- [ ] Holding period met (more than 5 years, or at least 3 years for new stock).
- [ ] Per-issuer cap computed, with prior-year and same-year gain reductions and the zero-after-exceeded rule; running tracker kept.
- [ ] Exclusion percentage applied to the capped gain; section 1202 gain, gain above the cap, AMT and NIIT classified.
- [ ] Form 8949 code Q/R, 28% worksheet, Form 6251 line 2h done; §1045 election on a timely return. [Schedule D instructions](https://www.irs.gov/instructions/i1040sd)
- [ ] State treatment checked separately.

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
