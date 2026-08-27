---
name: us-section-1202-qsbs
description: Tier 2 US federal content skill for IRC §1202 Qualified Small Business Stock gain exclusion. Covers OBBBA P.L. 119-21 (July 2025) expansion including the new tiered exclusion (50% at 3 years, 75% at 4 years, 100% at 5 years), the $75M gross-asset cap (raised from $50M), the $15M per-issuer cap (raised from $10M), the §1202(e)(3) SSTB exclusion list, §1045 rollover with 60-day reinvestment, AMT treatment for post-2010 stock, state conformity (CA non-conforming), QSBS-destroying events (S-corp conversion, buyback, recapitalization edge cases), family stacking strategies, SAFE/convertible note conversion treatment, and Form 8949 Code Q reporting. Tax year 2025.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Section 1202 QSBS

## IRC §1202 — Qualified Small Business Stock Gain Exclusion (Tax Year 2025)

> **Circular 230 disclosure.** This skill produces draft workpapers and analytical positions for review by a credentialed practitioner (Enrolled Agent, CPA, or attorney admitted to practice before the IRS). Nothing produced here is a written opinion within the meaning of Circular 230 §10.37, is not marketed tax advice, and may not be used by the taxpayer for the purpose of avoiding tax penalties unless a reviewer signs off on the position in a separate written communication that satisfies §10.37(a)(2). The §1202 position has been litigated repeatedly (see Section 14, Provenance) and the SSTB determination under §1202(e)(3) is fact-intensive — every conclusion in this skill is provisional pending reviewer confirmation against the actual corporate records, gross-asset history, and trade-or-business facts of the issuer.

## 1. Scope and Refusal Catalogue

### 1.1 In scope

- **Scope description** — This skill computes and documents the §1202 gain exclusion for a US individual taxpayer (or a passthrough holder where §1202(g) flow-through applies) who sells stock in a domestic C-corporation that qualified as Qualified Small Business Stock at the time of issuance and at all relevant times during the holding period. It covers: The four §1202 acquisition windows (pre-2/18/2009, 2/18/2009–9/27/2010, post-9/27/2010 pre-applicable-date, post-applicable-date enactment); The OBBBA P.L. 119-21 (July 4, 2025) tiered exclusion at 3, 4, and 5 years of holding, the $75M gross-asset cap (up from $50M), and the $15M per-issuer cap (up from $10M); The §1202(c) 'qualified small business stock' definition, the §1202(d) 'qualified small business' definition, the §1202(e) active business requirement, and the §1202(e)(3) SSTB exclusion list; The §1045 rollover election (60-day reinvestment) for taxpayers who sell before satisfying the holding period; The §1202(g) flow-through rules for partnership-held QSBS; AMT treatment under §57(a)(7) for §1202 gain; Form 8949 Code 'Q' reporting and Schedule D carryover; State conformity in the major founder-resident states (CA, NY, NJ, MA, WA, TX, FL); Family/trust stacking strategies and the §1202(h) tacking rules for gifts and bequests; SAFE, convertible-note, and option exercise mechanics that determine the QSBS clock start date.  _([§1202](https://www.law.cornell.edu/uscode/text/26/1202))_

### 1.2 Out of scope — refusal catalogue

- **Refusal 1 — C-corp status broken** — The corporation has ever been an S-corp, partnership, LLC taxed as a partnership, or disregarded entity during any part of the taxpayer's holding period. §1202(c)(1) requires C-corp status at issuance AND substantially all of the holding period. The conversion-tacking question is a fact-and-circumstances mess — escalate.  _([§1202(c)(1)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Refusal 2 — reorganization with non-QSBS stock or boot** — The corporation underwent a tax-free reorganization (§354, §355, §368) and the taxpayer received non-QSBS stock or boot. §1202(h)(4) preserves QSBS character for §368(a) reorganizations only in limited circumstances — escalate.  _([§1202(h)(4)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Refusal 3 — excluded entity type** — The corporation is a Regulated Investment Company (RIC), Real Estate Investment Trust (REIT), Real Estate Mortgage Investment Conduit (REMIC), Domestic International Sales Corporation (DISC), or cooperative — §1202(e)(4) categorically excludes these.  _([§1202(e)(4)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Refusal 4 — excluded business types over 20% asset value** — The corporation is engaged in farming, mineral extraction (§613), hotel/motel/restaurant operation, banking, insurance, financing, or leasing as more than 20% of asset value — §1202(e)(3) and §1202(e)(7).  _([§1202(e)(3); §1202(e)(7)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Refusal 5 — taxpayer is a C-corporation** — The taxpayer is a C-corporation. §1202(a) applies only to 'taxpayer other than a corporation.'  _([§1202(a)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Refusal 6 — option acquired more than 6 months before C-corp status** — The stock was acquired by exercise of an option that itself was acquired more than 6 months before the underlying corporation was a C-corp; the issuance-date analysis is too fact-specific for an automated skill.
- **Refusal 7 — §351 incorporation with built-in gain exceeding $50,000** — The taxpayer is claiming §1202 on stock acquired through a §351 incorporation where the contributed property's built-in gain exceeds $50,000 — the §1202(i) basis-step-up rules and the carryover holding period need manual analysis.  _([§1202(i)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Refusal 8 — significant redemption** — The corporation made a 'significant redemption' under §1202(c)(3) (more than 5% of stock by value from related parties within 2 years before or after the issuance) — this destroys QSBS for all holders and requires factual investigation.  _([§1202(c)(3)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Refusal 9 — non-grantor trust holder** — The taxpayer holds the stock through a trust that is not a grantor trust — the §1202(g) flow-through analysis for non-grantor trusts is unsettled.  _([§1202(g)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Refusal 10 — non-resident alien or foreign trust/estate** — The taxpayer is a non-resident alien or a foreign trust/estate.
- **Refusal 11 — state conformity outside covered states** — State conformity questions outside CA, NY, NJ, MA, WA, TX, FL — escalate to a state specialist.

### 1.3 Conservative defaults principle

- **Default to not QSBS** — Default to 'not QSBS' unless the taxpayer provides documentary proof of all four §1202(c) requirements.  _([§1202(c)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Default to pre-applicable-date caps if ambiguous** — Default to the pre-applicable-date rules ($10M / 10x basis / 5-year hold / $50M gross-asset cap) if the acquisition or issuance date is ambiguous around July 4, 2025. OBBBA §70431 applies the new acquisition-side rules only to stock acquired after the enactment date; the $75M gross-asset amendment applies to stock issued after the enactment date.  _([P.L. 119-21 §70431; IRC §1202(a)(6)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_
- **Default to fully taxable in non-conforming states** — Default to 'fully taxable' for state purposes in CA, NJ, MS, and PA (the four major non-conforming states) until the reviewer confirms state treatment.

## 2. Statutory Anatomy: §1202 in Twelve Pieces

**§1202 subsections table**  _([§1202](https://www.law.cornell.edu/uscode/text/26/1202))_

**§1202 subsections table**  _([§1202](https://www.law.cornell.edu/uscode/text/26/1202))_

| Subsection | What it does |
| --- | --- |
| §1202(a) | Operative exclusion percentage (50%, 75%, or 100% pre-applicable-date; tiered 50/75/100% post-applicable-date based on holding period). |
| §1202(b) | Per-issuer dollar cap: greater of $10M lifetime ($15M post-applicable-date) or 10× aggregate adjusted basis of QSBS disposed of by the taxpayer during the taxable year. |
| §1202(c) | Definition of QSBS: original-issuance requirement, C-corp requirement at issuance and during substantially all of the holding period, active business requirement. |
| §1202(c)(3) | Anti-abuse: significant redemptions destroy QSBS. |
| §1202(d) | Definition of "qualified small business": $50M gross-asset cap pre-applicable-date, $75M post-applicable-date, measured at any time from corporate formation through and immediately after issuance. |
| §1202(e) | Active business requirement: at least 80% of corporate assets used in qualified trade or business during substantially all of the holding period. |
| §1202(e)(3) | Excluded SSTB list — see Section 5. |
| §1202(e)(4) | Excluded entity types (RIC, REIT, REMIC, DISC, cooperative). |
| §1202(f) | Treatment of stock acquired by conversion of other stock — preserves §1202 character. |
| §1202(g) | Pass-thru entities: partnerships, S-corporations, RICs, and common trust funds may pass §1202 gain to partners, shareholders, and beneficiaries who held the entity interest at the time the QSBS was acquired by the entity and continuously thereafter. |
| §1202(h) | Tacking: gift, death, and certain partnership distributions preserve §1202 character and tack holding period. |
| §1202(i) | Basis rules for stock received in §351 incorporations and contributions of appreciated property. |
| §1202(j) | Stock acquired on conversion of convertible debt — clock starts at conversion. |
| §1202(k) | Regulatory authority. |
| §1202(l) | Stock in pass-through holding companies — limited application. |

## 3. Pre-applicable-date §1202 (Stock Acquired On or Before July 4, 2025)

For stock acquired on or before the OBBBA enactment date, three exclusion percentages apply based on acquisition window. **These rules continue to apply to all QSBS acquired on or before July 4, 2025**, regardless of when the stock is sold.

### 3.1 Acquisition windows

**Acquisition windows table**  _([§1202(a); §57(a)(7); P.L. 119-21 §70431(a)](https://www.law.cornell.edu/uscode/text/26/1202))_

| Acquisition window | §1202(a) exclusion | §57(a)(7) AMT add-back |
| --- | --- | --- |
| Pre-2/18/2009 | 50% | 7% of excluded gain |
| 2/18/2009-9/27/2010 | 75% | 7% of excluded gain |
| Post-9/27/2010 through 7/4/2025 | 100% | None (zero AMT preference) |

Source: §1202(a)(3) (50% baseline), §1202(a)(3)(A) and §1202(a)(4) (75% and 100% as enacted by the American Recovery and Reinvestment Act of 2009 and the Small Business Jobs Act of 2010 respectively; made permanent by the PATH Act of 2015).

### 3.2 Holding period

- **Pre-applicable-date holding period binary** — Pre-applicable-date, the holding period requirement was binary: 5 years or no §1202 benefit. If the taxpayer sold before 5 years, the only escape was a §1045 rollover (Section 6) or treating the gain as ordinary capital gain.  _([§1202](https://www.law.cornell.edu/uscode/text/26/1202))_

### 3.3 Per-issuer cap

- **Per-issuer cap definition** — §1202(b)(1) caps eligible gain at the greater of the applicable dollar limit or 10x aggregate adjusted basis of QSBS from that issuer disposed of during the taxable year. For stock acquired on or before July 4, 2025, the dollar limit is $10M (or $5M for MFS). For stock acquired after July 4, 2025, the dollar limit is $15M (one-half for MFS), inflation-indexed after 2026, and reduced by prior same-issuer eligible gains including gains from stock acquired before, on, or after the applicable date.  _([IRC §1202(b)(1), (b)(4), (b)(5); P.L. 119-21 §70431(b)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Per-issuer, per-taxpayer nature** — This is a per-issuer, per-taxpayer cap. A taxpayer can claim up to $10M (now $15M, see Section 4) of excluded gain from each separate qualifying corporation. Married couples filing jointly share a single cap per issuer (§1202(b)(3)(B)) — but separate spouses with separately-acquired QSBS each get their own cap.  _([§1202(b)(3)(B)](https://www.law.cornell.edu/uscode/text/26/1202))_

### 3.4 Gross-asset cap

- **Pre-applicable-date gross-asset cap** — Pre-applicable-date, the corporation's aggregate gross assets could not exceed $50M at any time from August 10, 1993, through and immediately after the issuance of the stock.  _([§1202(d)(1)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Gross assets measured at basis** — The test is on gross assets at adjusted basis, not fair market value (with a special rule for contributed property valued at FMV at contribution).  _(§1202(d)(2)(B))_
- **Test applies through issuance only** — The gross-asset test applies at every moment in the corporation's history up to and through the issuance, but not after issuance. Use $50M for stock issued on or before July 4, 2025 and $75M for stock issued after July 4, 2025. A company can exceed the applicable cap after issuance without destroying QSBS for stock already validly issued.  _([IRC §1202(d)(1); P.L. 119-21 §70431(c)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Aggregation of controlled group** — All corporations in the same parent-subsidiary controlled group under §1202(d)(3) are aggregated.  _([§1202(d)(3)](https://www.law.cornell.edu/uscode/text/26/1202))_

## 4. OBBBA 2025 Expansion (Stock Acquired After July 4, 2025)

The One Big Beautiful Bill Act (P.L. 119-21), enacted July 4, 2025, dramatically expanded §1202 for stock acquired after the date of enactment. The expansion has four moving parts:

### 4.1 Tiered exclusion by holding period — NEW

**Tiered exclusion table**  _([OBBBA §70431(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

| Holding period | §1202(a) exclusion | Taxable LTCG portion |
| --- | --- | --- |
| Less than 3 years | 0% (no §1202 benefit; §1045 rollover only) | 100% |
| 3 years to less than 4 years | 50% | 50% |
| 4 years to less than 5 years | 75% | 25% |
| 5 years or more | 100% | 0% (subject to per-issuer cap) |

- **Ramp replaces cliff** — The pre-applicable-date '5-year cliff' is replaced by a graduated ramp. A founder who exits at year 3 still captures meaningful §1202 benefit; pre-applicable-date, that founder would have had to choose between §1045 rollover or full LTCG treatment.  _([OBBBA §70431(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

> **AUDIT FLASH POINT — holding-period documentation.** For the 3-year and 4-year tiers, the IRS will scrutinize the exact acquisition date. SAFEs that convert (Section 11.3), option exercises (Section 11.4), and §351 incorporations (Section 11.5) all introduce holding-period ambiguity. Maintain a contemporaneous record: original stock certificate or electronic ledger entry, board resolutions authorizing issuance, cap table entries with effective dates, and (for conversions) the conversion documentation showing the exact date QSBS clock started.

### 4.2 Per-issuer cap raised to $15M — NEW

- **Per-issuer cap raised to $15M** — $15,000,000 USD (raises §1202(b)(1) per-issuer cap from $10M to $15M, with conforming amendment to retain the 10× basis alternative; indexed for inflation beginning in 2027 (first adjustment in the 2027 Rev. Proc. annual update))  _([OBBBA §70431(b); §70431(b)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

### 4.3 Gross-asset cap raised to $75M — NEW

- **Gross-asset cap raised to $75M** — $75,000,000 USD (raises §1202(d)(1) gross-asset cap from $50M to $75M, also indexed for inflation beginning in 2027; expands the universe of 'qualified small business' issuers)  _([OBBBA §70431(c)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

### 4.4 Effective date

- **Effective date of OBBBA amendments** — OBBBA §70431 added §1202(a)(6): the applicable date is the date of enactment, and the new tiered exclusion applies to stock acquired after that date. Because P.L. 119-21 was enacted July 4, 2025, treat the new acquisition-side rules as applying to stock acquired after July 4, 2025; stock acquired on or before July 4, 2025 remains under the prior holding-period and cap rules. The $75M gross-asset amendment applies to stock issued after the enactment date.  _([P.L. 119-21 §70431(a), (c); IRC §1202(a)(6)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

**Practical consequence — the "dual track" period.** After July 4, 2025, taxpayers and reviewers must track QSBS by acquisition/issuance date: stock acquired on or before July 4, 2025 remains under the $10M / 10x basis cap and 5-year holding-period rule; stock acquired after July 4, 2025 can use the 3/4/5-year tiered exclusion and the $15M / 10x basis cap. The $75M gross-asset cap applies to stock issued after July 4, 2025. For same-issuer mixed holdings, apply the statutory §1202(b)(4) reduction rule: the $15M post-applicable-date dollar limit is reduced by prior same-issuer eligible gains, including gains from stock acquired before, on, or after the applicable date, and by same-year eligible gains from stock acquired on or before the applicable date.

### 4.5 OBBBA expansion summary table

**OBBBA expansion summary table**  _([P.L. 119-21 §70431; IRC §1202](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

| Element | Pre-applicable-date rule | Post-applicable-date rule |
| --- | --- | --- |
| §1202(a) exclusion | 100% at 5 years for post-9/27/2010 stock acquired on or before 7/4/2025 | 50% at 3 years, 75% at 4 years, 100% at 5 years for stock acquired after 7/4/2025 |
| §1202(b)(1) per-issuer cap | $10M / 10x basis | $15M / 10x basis, inflation-indexed after 2026, reduced by prior same-issuer eligible gains under §1202(b)(4)(B) |
| §1202(d)(1) gross-asset cap | $50M | $75M for stock issued after 7/4/2025, inflation-indexed after 2026 |
| §57(a)(7) AMT preference | Zero for post-9/27/2010 stock; 7% preference only for pre-9/27/2010 50%/75% stock | Zero §57(a)(7) preference for all post-applicable-date tiers |
| §1045 rollover | Available | Available, and less critical once the 3-year tier is met |

## 5. The §1202(c) Qualification Requirements

For stock to be QSBS, every one of the following five requirements must be satisfied. Failure of any one destroys QSBS character.

### 5.1 C-corporation status

- **C-corp status requirement** — The issuer must be a domestic C-corporation at the time of issuance and during substantially all of the taxpayer's holding period. 'Substantially all' is not defined in the statute but is generally interpreted (per IRS Field Service Advice 200145011 and consistent practitioner practice) as more than 90% of the holding period.  _(§1202(c)(1); §1202(c)(2); IRS FSA 200145011)_
- **S-corp at any time destroys QSBS** — S-corp at any time during holding period → QSBS destroyed. §1202(c)(2)(A) makes this categorical. An S-corp election made after issuance terminates QSBS status from the date of the S-election.  _([§1202(c)(2)(A)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **LLC taxed as partnership destroys QSBS** — LLC taxed as partnership at any time → QSBS destroyed. The corporation must be a C-corp under Subchapter C, not a state-law LLC even if it has elected C-corp tax status from inception (the entity must be a 'corporation' within the §7701 meaning AND have elected C-corp treatment from inception, with no intervening partnership period).  _(§7701)_
- **LLC to C-corp conversion clock start** — Conversion of LLC to C-corp: the QSBS clock starts at the date of conversion (not the date of the original LLC formation). Pre-conversion LLC holding does NOT tack. See Section 11.5.
- **C-corp to S-corp or LLC conversion** — Conversion of C-corp to S-corp or LLC: kills QSBS prospectively. If the corp has been C-corp for at least 90% of the holding period before conversion, the analysis is fact-intensive — escalate.

> **AUDIT FLASH POINT — corporate form history.** The IRS routinely requests the complete entity history from formation to sale: state filings, Form 8832 entity classification elections, Form 2553 S-elections (and revocations), Form 1120 vs Form 1120-S filings, and operating agreements. A single Form 1120-S filing during the holding period can destroy the entire §1202 position. Reviewer must verify the corp's full Schedule B from each year's return shows C-corp filing status.

### 5.2 Original issuance requirement

- **Direct-from-corporation requirement** — The taxpayer must acquire the stock directly from the corporation in exchange for money, property (other than stock), or services. Stock acquired in the secondary market — from another shareholder, in a tender offer, or on an exchange — is NOT QSBS in the hands of the new holder.  _(§1202(c)(1)(B))_
- **Exception — gift** — Gift (§1202(h)(1)(A)) — donee tacks donor's holding period.  _([§1202(h)(1)(A)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Exception — death** — Death (§1202(h)(1)(B)) — heir tacks decedent's holding period.  _([§1202(h)(1)(B)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Exception — partnership distribution** — Partnership distribution to a partner who was a partner when the partnership acquired the QSBS (§1202(h)(2)) — see Section 8.4.  _([§1202(h)(2)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Conversion of stock for stock** — Conversions of stock for stock in the same corporation under §1202(f) also preserve QSBS character (common preferred-to-common conversion at IPO).  _([§1202(f)](https://www.law.cornell.edu/uscode/text/26/1202))_

### 5.3 Gross-asset cap at and immediately before issuance

- **Gross-asset cap definition** — The issuer's aggregate gross assets must not have exceeded the applicable cap at any time from August 10, 1993, through and immediately after issuance: $50M for stock issued on or before July 4, 2025, and $75M for stock issued after July 4, 2025, with inflation adjustments after 2026.  _([IRC §1202(d)(1); P.L. 119-21 §70431(c)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Gross assets at basis except contributed property** — Gross assets at basis, not FMV (except contributed property valued at FMV at contribution under §1202(d)(2)(B)).  _([§1202(d)(2)(B)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Immediately after issuance test** — 'Immediately after' issuance: the cash or property received in the very issuance that produced the QSBS is included in the asset test. A company at $74M gross assets that raises $5M cannot issue QSBS in that round because the post-issuance balance is $79M.  _(§1202(d)(1))_
- **Aggregation under §1202(d)(3)** — Aggregation under §1202(d)(3): all corporations in a parent-subsidiary §1563(a) controlled group are aggregated. The 50%-by-vote-or-value threshold under §1563 applies.  _([§1202(d)(3); §1563(a)](https://www.law.cornell.edu/uscode/text/26/1202))_

> **AUDIT FLASH POINT — gross-asset documentation.** The single most common §1202 disqualifier on audit is failure to prove the gross-asset test at the moment of issuance. Reviewers MUST obtain: The corporation's balance sheet as of the day immediately before and immediately after each QSBS issuance event the taxpayer participated in. The §351 contribution documentation if applicable, with FMV valuations of contributed property. The aggregation analysis for any subsidiaries. For series-A/B/C rounds, the pre-money and post-money cap tables and signed financing documents. If the corporation cannot produce this, default to "not QSBS" and report the gain as ordinary LTCG.

### 5.4 Active business requirement (§1202(e))

- **80% asset use requirement** — During substantially all of the holding period: At least 80% of the corporation's assets (by value) must be used in the active conduct of one or more qualified trades or businesses.  _(§1202(e)(1)(A))_
- **Working capital exception** — 'Active conduct' excludes passive investment activities. Cash and working capital held for reasonable working capital needs (and reasonably expected to be used within 2 years for R&D or business expansion) DOES count as 'used in' the active business.  _(§1202(e)(6))_
- **Real property test** — Real property test: ownership or operation of real property is treated as a non-qualified business unless the real property is used in the corporation's qualified trade or business. More than 10% of total asset value in non-qualified real property fails the test.  _(§1202(e)(7))_
- **Portfolio stock and securities test** — Portfolio stock and securities test: more than 10% of total asset value in stock or securities of other corporations (other than subsidiaries) fails the test.  _(§1202(e)(5)(B))_

### 5.5 §1202(e)(3) excluded trades or businesses (the "SSTB" list)

The active business must NOT be a 'qualified trade or business' within the §1202(e)(3) exclusion list. This list is similar to but not identical to the §199A SSTB list — practitioners should NOT assume §199A and §1202 SSTB analyses produce the same result.

- **Excluded trade 1 — service fields** — Any trade or business involving the performance of services in the fields of: Health, Law, Engineering, Architecture, Accounting, Actuarial science, Performing arts, Consulting, Athletics, Financial services, Brokerage services.  _(§1202(e)(3))_
- **Excluded trade 2 — reputation or skill of employees** — Any business where the principal asset is the reputation or skill of one or more employees.  _(§1202(e)(3))_
- **Excluded trade 3 — banking, insurance, financing, leasing, investing** — Any banking, insurance, financing, leasing, investing, or similar business.  _(§1202(e)(3))_
- **Excluded trade 4 — farming** — Any farming business (including the business of raising or harvesting trees).  _(§1202(e)(3))_
- **Excluded trade 5 — mining, oil and gas** — Any business involving the production or extraction of products of a character with respect to which a deduction is allowable under §613 or §613A (mining, oil and gas).  _(§613; §613A; §1202(e)(3))_
- **Excluded trade 6 — hotel, motel, restaurant** — Any business of operating a hotel, motel, restaurant, or similar business.  _(§1202(e)(3))_
- **Eligible businesses** — Tech, software, manufacturing, retail, distribution, transportation, telecommunications, and most product-based businesses are NOT on this list and ARE eligible for §1202.  _([§1202(e)(3)](https://www.law.cornell.edu/uscode/text/26/1202))_

> **AUDIT FLASH POINT — the "consulting" challenge.** The IRS has repeatedly challenged §1202 positions where a technology company derives revenue from services that look like consulting or "reputation/skill of employees." The leading guidance is: **PLR 201436001 (June 2014)** — health-tech company providing services to insurance companies was held NOT a "health" business because it did not provide medical care. **PLR 201717010 (Jan 2017)** — pharmacy company providing services to nursing homes was NOT a "health" business. **PLR 202144026 (July 2021)** — staffing agency providing IT consultants WAS a "consulting" business; QSBS denied. **Recent practitioner litigation (2023-2024)** has focused on the line between "software product" and "software-enabled consulting service." Companies that ship software that customers operate themselves are clearly product businesses; companies that deploy engineers to implement, customize, or operate software on behalf of customers risk the "consulting" or "reputation/skill" exclusion. When a company has mixed revenue (product + professional services), the §1202(e)(3) test is applied at the entity level by reference to the trade or business as a whole. There is no clean revenue percentage threshold; practitioners typically apply a "principal activity" test. If professional services revenue exceeds 25-30% of total revenue, escalate.

### 5.6 §5M-capital-deployment safe harbor

- **Working capital safe harbor** — §1202(e)(6) treats assets held by the corporation that are reasonably expected to be used in a qualified trade or business or in R&D within 2 years as meeting the active business test. This means freshly-raised cash from a financing round is 'active business' assets for up to 2 years even if it's parked in money-market funds.  _([§1202(e)(6)](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Startup working capital safe harbor** — For very young companies (within 2 years of becoming an active business), there is a working-capital safe harbor that effectively waives the active business test during the startup period.  _(§1202(e)(6))_

## 6. §1045 Rollover (60-Day Reinvestment)

§1045 allows a taxpayer who sells QSBS before satisfying the §1202 holding period to roll over the gain by purchasing replacement QSBS within 60 days. This is a critical exit strategy for founders who experience an early acquisition.

### 6.1 Mechanics

- **§1045 rollover mechanics** — 1. Taxpayer sells QSBS at a gain. 2. Within 60 days of the sale, taxpayer purchases replacement QSBS in a different (or same) qualified small business. 3. Taxpayer elects §1045 on a timely-filed return (including extensions) for the year of sale — election is made on Form 8949 with code "R" and a statement attached per Rev. Proc. 98-48. 4. Gain is recognized only to the extent the sale proceeds exceed the cost of the replacement QSBS. 5. The replacement QSBS takes a substituted basis equal to its cost reduced by the deferred gain.  _(§1045; Rev. Proc. 98-48)_

### 6.2 Holding period of replacement QSBS — the open question

**Position A (statutory text)**: §1045(b)(4) provides that the holding period for the replacement QSBS includes the holding period of the original QSBS for purposes of determining gain or loss but is explicitly not tacked for purposes of §1202(c)(2) (the C-corp-at-issuance test). The statute is silent on §1202(a) holding period.

**Position B (Rev. Proc. 98-48 and longstanding IRS administrative position)**: the §1202 5-year clock RESTARTS at the acquisition of replacement QSBS. This is the IRS position.

**Position C (some practitioner commentary, e.g., Polsky 2024)**: the statute can be read to tack the holding period for all §1202 purposes; some practitioners take the aggressive position on disclosure.

- **Skill default position** — This skill defaults to Position B (IRS administrative position): the §1202 clock restarts. Reviewer may consider Position C with proper disclosure (Form 8275) only if the planning context warrants it.  _([Rev. Proc. 98-48](https://www.law.cornell.edu/uscode/text/26/1202))_

### 6.3 §1045 with OBBBA tiered exclusion

- **§1045 relevance post-applicable-date** — Post-applicable-date, §1045 becomes less critical for the 3-year and 4-year tiers — a founder who sells at year 3 can claim 50% exclusion directly without rolling over. But §1045 remains valuable for: Sales before 3 years (no §1202 exclusion is available at all). Sales at year 4-5 where rolling into a new investment with a fresh 5-year clock might yield a better total exclusion than 75% at year 4.  _([§1045](https://www.law.cornell.edu/uscode/text/26/1202))_

> **AUDIT FLASH POINT — late §1045 elections.** §1045(a) requires the election on a timely-filed return. Late elections require §301.9100 relief, which is granted on a fact-specific basis and requires showing reasonable action and good faith. The IRS has denied §9100 relief for §1045 in multiple PLRs where the taxpayer waited too long. Mark all §1045 sales on the engagement calendar and confirm the election goes out with the original (or extended) return.

### 6.4 Mechanics of the substituted basis

Example: Sell QSBS for $5M with $500k basis → $4.5M gain. Within 60 days, buy replacement QSBS for $3M. Recognized gain: $5M proceeds − $3M reinvested = $2M recognized now. Deferred gain: $4.5M − $2M = $2.5M. Basis in replacement QSBS: $3M − $2.5M deferred gain = $500k. New §1202 clock starts at acquisition of replacement QSBS. If the replacement QSBS is held for 5+ years and qualifies under §1202, the $2.5M deferred gain plus any further appreciation can be excluded under §1202 (subject to the per-issuer cap of the replacement issuer).

## 7. AMT Treatment

### 7.1 100% exclusion stock (acquired after 9/27/2010)

- **AMT preference suspended for 100% stock** — §57(a)(7) now limits the 7% AMT preference to stock acquired on or before September 27, 2010. Post-2010 100%-exclusion stock and post-applicable-date OBBBA tiered stock produce no §57(a)(7) AMT preference.  _([IRC §57(a)(7); P.L. 119-21 §70431(a)(4)](https://www.law.cornell.edu/uscode/text/26/1202))_

### 7.2 50% and 75% exclusion stock

- **AMT preference applies to 50%/75% stock** — For 50%-exclusion stock (pre-2/18/2009) and 75%-exclusion stock (2/18/2009–9/27/2010), §57(a)(7) applies: 7% of the excluded gain is an AMT preference item. With the current AMT exemption levels (post-TCJA and confirmed by OBBBA), this rarely produces AMT for individual founders but should be modeled.  _([§57(a)(7)](https://www.law.cornell.edu/uscode/text/26/1202))_

### 7.3 OBBBA tiered exclusion stock (after 7/4/2025)

- **AMT treatment by tier** — OBBBA §70431(a)(4) amended §57(a)(7), so the AMT preference is limited to stock acquired on or before September 27, 2010. Post-applicable-date QSBS has no §57(a)(7) preference at the 50%, 75%, or 100% exclusion tiers. Model AMT only on the taxable portion of the gain that remains after the §1202 exclusion.  _([IRC §57(a)(7); P.L. 119-21 §70431(a)(4)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_
- **No AMT preference for post-applicable-date tiers** — Do not apply the §57(a)(7) AMT preference to post-applicable-date QSBS merely because the exclusion percentage is 50% or 75%. OBBBA §70431(a)(4) limits the preference to stock acquired on or before the 2010 Small Business Jobs Act date. The taxable portion of a 3-year or 4-year sale remains regular capital gain and may affect AMT through the normal AMT calculation.  _([IRC §57(a)(7); P.L. 119-21 §70431(a)(4)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

### 7.4 Section 1411 NIIT

- **NIIT treatment of QSBS gain** — The 3.8% Net Investment Income Tax under §1411 applies to the taxable portion of QSBS gain (the portion NOT excluded by §1202). For 100%-exclusion stock, the entire excluded amount is exempt from NIIT (because there's no income to tax). For partial-exclusion stock, the taxable portion is NII. Above the per-issuer cap, the excess is also NII.  _([§1411](https://www.law.cornell.edu/uscode/text/26/1202))_

## 8. Gifting, Estate Planning, and §1202 Stacking

### 8.1 Tacking under §1202(h)

- **Tacking rules** — §1202(h) provides that QSBS character and holding period tack through: Gift (§1202(h)(1)(A)) — donee tacks donor's holding period. Death (§1202(h)(1)(B)) — heir tacks decedent's holding period; QSBS basis is NOT stepped up under §1014 because §1202 is a recognition rule, not a basis rule. Actually — and this is a subtlety — the §1014 basis step-up DOES apply (death triggers FMV basis), but the §1202 character is preserved per §1202(h)(1)(B). The interplay: the step-up reduces the gain on a later sale, but to the extent gain remains (e.g., post-death appreciation), §1202 excludes it up to the cap. Distribution from partnership to partner under §1202(h)(2) — see Section 8.4.  _([§1202(h); §1014](https://www.law.cornell.edu/uscode/text/26/1202))_

### 8.2 Family stacking strategy

Because the §1202(b) per-issuer cap is per taxpayer, a founder who gifts QSBS to family members (or trusts for their benefit) creates additional caps: Founder: $15M cap. Spouse (if QSBS held separately as separate property): $15M cap (married-filing-jointly couples share a single cap if the QSBS is jointly held — gift to spouse creates separate property if structured correctly). Each child: $15M cap. Each non-grantor trust for benefit of a child: potentially $15M cap (with caveats — see Section 8.3).

**Worked stacking example.** Founder has 1M QSBS shares with $1,000 total basis, anticipated exit at $200/share = $200M proceeds, $199.999M gain. No stacking: $15M excluded, $185M taxable LTCG. 4-person stack (founder + spouse + 2 kids): pre-sale gift 250k shares each to spouse and 2 kids (3 separate non-grantor trusts for the kids if minor children). Each holder claims $15M cap = $60M total excluded; $140M taxable LTCG. **Tax savings**: $45M of additional exclusion × ~23.8% federal LTCG+NIIT = ~$10.7M federal saved (plus state if conforming).

### 8.3 Trust stacking — the caveats

Trust stacking is the most aggressive §1202 planning technique. The IRS has signaled in informal commentary (no formal guidance) that it scrutinizes:

- **Multiple trusts with identical terms — §643(f)** — Multiple trusts with substantially identical terms and beneficiaries: §643(f) trust-aggregation rule may collapse multiple trusts created for tax-avoidance purposes into a single trust with a single $15M cap. The §643(f) regulations (T.D. 9913, finalized in 2020) require a 'principal purpose of tax avoidance' — a fact-and-circumstances test.  _([§643(f); T.D. 9913](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Grantor trusts share cap** — Grantor trusts: a grantor trust is the grantor for income tax purposes (§671), so the grantor and the trust share a single $15M cap. To create a separate cap, the trust must be a non-grantor trust (typically a 'Dynasty Trust' or 'Beneficiary Deemed Owner Trust' structured to be non-grantor).  _([§671](https://www.law.cornell.edu/uscode/text/26/1202))_
- **Gift tax on QSBS transfers** — Gift tax: gifts of QSBS use the donor's lifetime gift exemption ($13.99M for 2025, scheduled to remain elevated under OBBBA Section TBD). Gifts exceeding the annual exclusion ($19,000 for 2025) require Form 709. The gift is valued at the QSBS FMV at the date of gift; for early-stage company stock, this can be very low.  _([Form 709](https://www.law.cornell.edu/uscode/text/26/1202))_

> **AUDIT FLASH POINT — §643(f) aggregation.** Stacking strategies involving 4+ trusts created in close temporal proximity to a known liquidity event will draw §643(f) scrutiny. The defense: each trust serves a distinct, non-tax purpose (asset protection, generation-skipping, specific beneficiary needs), is funded with different assets, has different trustees, and has different terms beyond the §1202 stacking. Document the non-tax purposes contemporaneously, not after the fact.

### 8.4 Partnership distribution under §1202(h)(2)

- **Partnership distribution rule** — If a partnership holds QSBS and distributes the QSBS to a partner, the partner takes the QSBS with §1202 character preserved, but only if the partner was a partner in the partnership at the time the partnership acquired the QSBS and continuously thereafter. The partner's share is determined by the partner's smallest interest in the partnership during that period.  _([§1202(h)(2)(C)](https://www.law.cornell.edu/uscode/text/26/1202))_

## 9. State Conformity (Tax Year 2025)

State conformity to §1202 is highly variable and changes with state legislative cycles. The summary below reflects state law as of 2025-11-15.

**State conformity table**  _([R&TC §17131](https://www.law.cornell.edu/uscode/text/26/1202))_

| State | Conformity | Notes |
| --- | --- | --- |
| California | **Does NOT conform.** | R&TC §17131 specifically denies §1202 conformity. CA fully taxes the excluded gain at the CA marginal rate (up to 13.3%, plus 1% mental health surcharge over $1M MAGI). This is the single largest state-conformity gap for CA-resident founders. |
| New York | Conforms with modifications. | NY conforms to federal §1202 but only for QSBS issued by corporations meeting certain NY-specific criteria. Verify with NY-specific analysis. |
| New Jersey | **Does NOT conform.** | NJ has no parallel exclusion. |
| Massachusetts | Conforms for stock acquired after 1/1/2011 with 3% Massachusetts SSTB-equivalent test. | MA-resident founders may need to satisfy both federal and MA tests. |
| Washington | No state income tax on individuals; no §1202 conformity question. | The 7% WA capital gains tax (enacted 2021, effective 2022) **applies to QSBS gain** to the extent not excluded federally — the WA tax has its own $250k standard exemption per individual but does NOT incorporate §1202. |
| Texas | No state income tax on individuals; no §1202 conformity question. |  |
| Florida | No state income tax on individuals; no §1202 conformity question. |  |
| Pennsylvania | **Does NOT conform.** | PA personal income tax has its own capital gains regime with no §1202 analog. |
| Mississippi | **Does NOT conform.** |  |
| Alabama | Conforms with modifications. |  |
| Illinois | Conforms. |  |
| Other states | Generally conform (about 35 states) but verify. |  |

> **PRACTITIONER NOTE — the CA non-conformity gotcha.** A CA-resident founder selling QSBS will pay ~13.3% CA tax on the entire gain plus ~23.8% federal on the portion above the per-issuer cap. For a $100M exit with $15M federally excluded: Federal: ($100M − $15M) × 23.8% = $20.23M. California: $100M × ~13.3% = $13.3M (no exclusion). Combined: $33.53M of $100M, or ~33.5%. Pre-sale relocation to a non-income-tax state (TX, FL, NV, WA, WY, SD, TN) is a common planning move, but requires actual change of domicile under CA's strict residency rules (R&TC §17014 and FTB Pub. 1031). CA will pursue back taxes for residents who move "temporarily" to avoid the tax. Plan early and document the domicile change rigorously.

## 10. Events That Destroy QSBS

**Events That Destroy QSBS**  _(https://www.law.cornell.edu/uscode/text/26/1202)_

| Event | Effect on QSBS |
| --- | --- |
| C-corp converts to S-corp | QSBS destroyed prospectively from S-election date. Gain accrued before S-election may still qualify if the holding period at the time of S-election was already >90% of subsequent holding — fact-intensive, escalate. |
| C-corp converts to LLC taxed as partnership | QSBS destroyed prospectively. |
| Reorganization where holder receives non-QSBS stock | If the reorg is a §368(a)(1)(A)/(B)/(C)/(E)/(F) tax-free reorg and the holder receives stock in the acquiring corporation, QSBS character may carry over under §1202(h)(4) — but only if the acquiring corporation also satisfies §1202 requirements. Most public-company acquisitions kill QSBS because the acquirer fails the $75M gross-asset cap. |
| Cash-out merger | Treated as a sale at the merger date; §1202 applies if requirements satisfied at that date. |
| Significant redemption of >5% of stock from related parties within 2 years of issuance | §1202(c)(3): destroys QSBS for all holders, not just the redeemed party. This is an anti-abuse rule targeting "issue-and-redeem" schemes. The 5% test is computed by value. |
| Significant redemption of >2% of stock from same shareholder within 2 years either side of issuance | §1202(c)(3): destroys QSBS only for that shareholder. |
| Stock split, stock dividend | Preserved under §1202(f). Holding period tacks. |
| Recapitalization (§368(a)(1)(E)) | Preserved if all stock received is in same corp and corp still qualifies. |
| Issuance of new options or warrants | No effect on existing QSBS holders. New options, when exercised, start their own §1202 clock at exercise date. |
| Corporate dissolution | Treated as sale of stock; §1202 applies if holding period met. |
| Open-end RIC (mutual fund) holding QSBS | §1202(g) does NOT flow through to mutual fund shareholders. Mutual funds are categorically excluded from §1202. |
| Closed-end RIC | §1202(l) provides limited application — escalate. |

## 11. SAFE Notes, Convertible Notes, and Option Exercises — Clock-Start Mechanics

The single most common §1202 reviewer question is: **"When does the QSBS clock start?"** The answer depends on the form of the instrument and the timing of conversion or exercise.

### 11.1 Direct stock purchase at incorporation

- **QSBS clock start - direct purchase at incorporation** — Founder purchases common stock at par at incorporation for de minimis cash → QSBS clock starts at issuance date. This is the cleanest case.

### 11.2 §83(b) election on restricted stock

- **QSBS clock start - restricted stock with/without §83(b)** — Founder receives restricted stock subject to vesting; files §83(b) election within 30 days → QSBS clock starts at issuance date (the §83(b) election causes the stock to be treated as issued and held for §1202 purposes from the date of grant). Without §83(b) election → QSBS clock starts at vesting date for each tranche. This delay is one of the most expensive §1202 mistakes for founders who fail to file §83(b).  _([§83(b)](https://www.law.cornell.edu/uscode/text/26/1202))_

### 11.3 SAFEs and convertible notes

- **SAFE/convertible note clock start** — A SAFE (Simple Agreement for Future Equity) or convertible note is not stock until it converts. §1202(c) requires "stock" — SAFEs and convertible notes are debt or contractual rights, not stock. Clock start: at conversion, not at SAFE/note issuance. An investor who buys a SAFE in 2024 and converts to preferred at a 2025 priced round starts the QSBS clock in 2025, not 2024. Five years from conversion to 100% exclusion (or three years to 50% post-applicable-date). Some practitioners argue (with no clean statutory or regulatory support) that SAFEs that economically function as equity should start the clock at SAFE issuance. This skill rejects that position and defaults to clock start at conversion.  _([§1202(c)](https://www.law.cornell.edu/uscode/text/26/1202))_

### 11.4 Stock options (ISO and NSO)

- **Stock option clock start and implications** — Stock options are not stock until exercised. The §1202 clock starts at exercise date, not at grant date. Implications: An early employee with options vested over 4 years who exercises at exit fails the §1202 holding period entirely — the exercise date and sale date are simultaneous. An early employee who early-exercises options (exercising unvested options at low strike price, with §83(b) election) starts the QSBS clock at early-exercise date — this is the standard early-employee §1202 strategy. Cashless exercise at exit: the exercise and sale are simultaneous; no §1202 (but may qualify for §1045 rollover into new QSBS).  _(https://www.law.cornell.edu/uscode/text/26/1202)_

### 11.5 LLC-to-C-corp conversion

- **LLC-to-C-corp conversion effects** — When an LLC (taxed as partnership) converts to a C-corp: Pre-conversion LLC interests are not QSBS. Post-conversion C-corp stock is QSBS only if all §1202(c) requirements are met at the conversion (treated as the issuance date). Holding period of LLC interest does NOT tack. Pre-conversion built-in gain is recognized at conversion under §721/§351 rules (depending on conversion structure); only post-conversion gain qualifies for §1202. For founders planning a conversion, the timing matters: convert before significant valuation appreciation so the QSBS basis is low and the 10× basis cap is small, then ride the appreciation under §1202.  _([§721; §351](https://www.law.cornell.edu/uscode/text/26/1202))_

### 11.6 §351 incorporation with contributed property

- **§351 incorporation basis rules for QSBS** — If a founder incorporates by contributing appreciated property under §351: The C-corp's stock received in the §351 exchange is QSBS only to the extent the contributed property's FMV did not exceed the corp's gross-asset cap at issuance. The stock's basis under §358 is the founder's basis in the contributed property; but for §1202(b)(1)(B) 10× basis cap purposes, the basis is the FMV at contribution (§1202(i)) — this can substantially expand the 10× cap.  _([§351; §358; §1202(i); §1202(b)(1)(B)](https://www.law.cornell.edu/uscode/text/26/1202))_

Example: Founder contributes IP valued at $10M to new C-corp in exchange for stock with §358 basis of $0 (zero adjusted basis in IP). The 10× basis cap for §1202 purposes uses $10M FMV, so 10× = $100M. Combined with the $15M absolute cap, the greater of $15M or $100M = $100M cap. Substantial planning value.

### 12.1 Reporting mechanics

- **Form 8949 code Q reporting mechanics** — QSBS gain is reported on Form 8949 with code "Q" in column (f). The exclusion is shown as a negative adjustment in column (g). Column (a): description of property (corporation name and number of shares). Column (b): date acquired. Column (c): date sold. Column (d): proceeds. Column (e): cost or other basis. Column (f): code "Q". Column (g): negative adjustment for excluded gain (shown as a negative number). Column (h): net gain after exclusion. The net amount in column (h) carries to Schedule D Line 8b or 12 depending on holding period categorization.  _(Form 8949)_

### 12.2 §1045 rollover reporting

- **§1045 rollover reporting** — §1045 rollover is reported on Form 8949 with code "R" in column (f), with a negative adjustment in column (g) for the deferred gain. A statement must be attached identifying the replacement QSBS and the §1045 election under Rev. Proc. 98-48.  _(§1045; Rev. Proc. 98-48)_

### 12.3 Per-issuer cap tracking

- **Per-issuer cap tracking rules** — The taxpayer must maintain a running tally of §1202 exclusion claimed from each issuer across all years. Once the $15M (or $10M pre-applicable-date) cumulative cap is reached for an issuer, no further exclusion is available from that issuer. For partial-exclusion years (50% or 75% post-applicable-date), the cumulative cap is reduced by the excluded portion only, not the total gain. So a taxpayer at the 50% tier who excludes $5M of $10M total gain has used $5M of the $15M cap.  _([§1202](https://www.law.cornell.edu/uscode/text/26/1202))_

## 13. Three Worked Examples

### 13.1 Example 1 — Founder, $500M exit (post-applicable-date)

Founder Anya incorporates a SaaS company in 2025 (post-applicable-date), receiving 5,000,000 shares of common stock at par for $5,000 total. Files §83(b) election within 30 days of issuance. Company is a domestic C-corp; gross assets at issuance: $5,000. Company satisfies §1202(c) requirements throughout. In 2032 (7 years later), company is acquired for $100/share = $500M total to Anya. Anya is a Texas resident at the time of sale.

Holding period: 7 years → 100% exclusion tier (post-applicable-date). Gain: $500,000,000 − $5,000 = $499,995,000. §1202(b)(1) per-issuer cap: greater of $15M or 10 × $5,000 = max($15M, $50,000) = $15,000,000. Excluded gain: $15,000,000. Taxable LTCG: $499,995,000 − $15,000,000 = $484,995,000.

LTCG at 20%: $484,995,000 × 20% = $96,999,000. NIIT at 3.8%: $484,995,000 × 3.8% = $18,429,810. AMT: zero (100% exclusion stock, post-9/27/2010 regime). Total federal: $115,428,810 on $499,995,000 gain (effective rate ~23.1%).

Texas: zero state income tax.

Without §1202: ($499,995,000) × 23.8% = $118,998,810. With §1202: $115,428,810. Savings: $3,570,000 (only the cap-limited $15M × 23.8% = $3.57M).

CA does not conform: $499,995,000 × 13.3% = $66,499,335. Federal unchanged: $115,428,810. Combined: $181,928,145. The CA non-conformity costs $66.5M of state tax on gain that's federally excluded — escalation to CA pre-sale relocation planning.

### 13.2 Example 2 — Early employee, $25M exit (mixed pre/post-applicable-date)

Employee Ben joined a Series A startup in 2022 (pre-applicable-date). Early-exercised NSOs in 2022 for $250,000 ($250k basis), filed §83(b). Company gross assets at exercise: $30M (under pre-applicable-date $50M cap). Sells stock in 2027 (5 years and 2 months after exercise) for $25M in an acquisition. Ben is a Washington state resident.

Stock acquired pre-applicable-date → pre-applicable-date rules apply: $10M cap, 5-year cliff. Holding period: 5+ years → 100% exclusion. Gain: $25,000,000 − $250,000 = $24,750,000. §1202(b)(1) per-issuer cap: greater of $10M (pre-applicable-date) or 10 × $250,000 = max($10M, $2.5M) = $10,000,000. Excluded gain: $10,000,000. Taxable LTCG: $24,750,000 − $10,000,000 = $14,750,000.

LTCG at 20%: $14,750,000 × 20% = $2,950,000. NIIT at 3.8%: $14,750,000 × 3.8% = $560,500. AMT: zero. Total federal: $3,510,500.

Washington 7% capital gains tax: Washington does not conform to §1202. Gain over the $250k WA standard exemption (2025 inflation-adjusted figure ~$270k) is taxed at 7%. WA tax: ($24,750,000 − $270,000) × 7% = $1,714,100. (Note: WA's "long-term capital gains" tax is technically an excise tax, not income tax, and was upheld by the WA Supreme Court in Quinn v. State, 2023.) Total combined: $5,224,600 on $24.75M gain (~21.1%).

### 13.3 Example 3 — Family stacking, $200M exit (post-applicable-date)

Founder Carla incorporates a healthtech SaaS company in 2025 (post-applicable-date). Note: company sells software to hospital IT departments; does NOT provide medical services. §1202(e)(3) "health" exclusion does NOT apply — confirmed by reviewer analysis of revenue streams (95% software license, 5% implementation training, no direct patient care). Receives 1,000,000 shares for $1,000 at incorporation. Files §83(b). In 2026 (pre-liquidity, FMV $5/share), Carla gifts 250,000 shares each to: spouse Dan (separate property in a community-property-state pre-nup), and to two non-grantor dynasty trusts for the benefit of their two minor children (one trust per child, with distinct trustees, distinct beneficiary classes, and documented non-tax purposes — asset protection and GST planning). Gift tax: 4 gifts of $1,250,000 each ($5/share × 250k shares); using annual exclusions ($19k × 2 spouses × 4 donees = $152k) and lifetime exemption ($13.99M × 2 = $27.98M); Form 709 filed; remaining exemption: ~$23M. Holding period tacks under §1202(h)(1)(A). In 2030 (5+ years from 2025 issuance), company is acquired for $200/share = $200M total. All five holders sell their respective shares simultaneously.

| Holder | Shares | Basis | Proceeds | Gain | §1202(b)(1) cap | Excluded | Taxable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Carla | 0 (after gifts to children, gift to spouse, retained ?) — let's recompute. |

Carla retained 1,000,000 − 750,000 gifted = 250,000 shares. Hmm — that's only 4 holders. Let me restructure: Carla gifts to spouse Dan, and to one trust per child (2 trusts), retains balance herself = 4 holders total.

**§1202 analysis per holder (final)**  _(https://www.law.cornell.edu/uscode/text/26/1202)_

| Holder | Shares retained | Basis | Proceeds at $200/share | Gain | §1202(b)(1) cap (greater of $15M or 10× basis) | Excluded | Taxable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Carla | 250,000 | $250 | $50,000,000 | $49,999,750 | max($15M, $2,500) = $15M | $15,000,000 | $34,999,750 |
| Dan (spouse) | 250,000 | $250 | $50,000,000 | $49,999,750 | $15M | $15,000,000 | $34,999,750 |
| Trust 1 (child A) | 250,000 | $250 | $50,000,000 | $49,999,750 | $15M | $15,000,000 | $34,999,750 |
| Trust 2 (child B) | 250,000 | $250 | $50,000,000 | $49,999,750 | $15M | $15,000,000 | $34,999,750 |
| **Total** | **1,000,000** | **$1,000** | **$200,000,000** | **$199,999,000** | — | **$60,000,000** | **$139,999,000** |

Carla holds all 1M shares. Gain: $199,999,000. §1202(b)(1) cap: max($15M, 10 × $1,000) = $15M. Excluded: $15M. Taxable: $184,999,000. Stacking saves $60M − $15M = $45M of additional exclusion. At 23.8% combined federal LTCG+NIIT, that's $10,710,000 of federal tax savings.

If Carla and family are Florida residents: $0 state tax — full $10.71M federal savings captured. If Carla and family are CA residents: CA fully taxes all $200M of gain at marginal rates regardless of stacking — the stacking only captures federal savings, no CA savings.

Two trusts with distinct trustees, distinct beneficiaries (one per child), distinct asset-protection purposes, and distinct GST allocations. Each trust's terms differ beyond §1202 stacking: distribution standards differ, ages of mandatory principal distribution differ, trustee succession rules differ. Contemporaneous documentation of non-tax purposes (asset protection from minor's eventual creditors, GST shelter). Defensible against §643(f) challenge — but reviewer must confirm and engagement letter must disclose the audit risk.

AUDIT FLASH POINT — pre-sale gifting. The IRS scrutinizes QSBS gifts that occur close to a known liquidity event under both §643(f) (multiple trust aggregation) and the assignment-of-income doctrine. The defense: gifts must occur before there is a "fixed and determinable right" to sale proceeds. Practitioner threshold: gifts should occur before a binding letter of intent or definitive merger agreement; gifts after term sheet but before LOI are higher risk; gifts after LOI are at substantial risk of assignment-of-income recharacterization (Salvatore v. Comm'r, T.C. Memo 1970-30; Ferguson v. Comm'r, 174 F.3d 997 (9th Cir. 1999)). Document the timing rigorously.

## 14. Documentation Required

Reviewer must obtain and retain in the engagement file:
1. Corporate formation documents: certificate of incorporation, bylaws, organizational consent, original Form SS-4 EIN application showing C-corp election.
2. Entity classification history: Form 8832 elections (if any), Form 2553 S-elections (if any — should be NONE for QSBS), Form 1120 vs 1120-S filing history. Verify C-corp filing for every year of the holding period.
3. Gross-asset balance sheets: corp's balance sheet at adjusted basis at every issuance event the taxpayer participated in, plus immediately before and after each event. For multiple financing rounds, document each round's pre-money and post-money assets.
4. Original stock issuance documentation: stock subscription agreement, board resolution authorizing issuance, original stock certificate or electronic ledger entry showing taxpayer as direct purchaser from corp, payment receipt.
5. §83(b) election if applicable: copy of timely-filed §83(b) election with USPS-certified-mail receipt or IRS acknowledgment.
6. Cap table history: capitalization table at each financing round, conversion event, and the sale date.
7. Trade-or-business analysis: revenue breakdown by activity type (product vs services), employee roster, customer contracts (sample), website/marketing materials demonstrating product-vs-service character — to defend the §1202(e)(3) determination.
8. Active business asset test workpapers: corp's annual balance sheet with asset categorization (active business vs portfolio investment vs real property) for each year of the holding period; documentation of working capital intended for R&D/expansion within 2 years.
9. Sale documentation: closing statement showing proceeds, allocation of proceeds among consideration types (cash, stock, escrow, earnouts), date of closing.
10. Per-issuer cap tracker: spreadsheet showing cumulative §1202 exclusion claimed from each issuer across all years.
11. §1045 election documentation if applicable: timely-filed Form 8949 with code "R", statement under Rev. Proc. 98-48, replacement QSBS acquisition documentation.
12. Gift/estate documentation if applicable: Form 709 for gifts, valuation reports for QSBS at gift date, trust documents, donor/donee acknowledgments.
13. State conformity analysis: state-specific schedules for each state where the taxpayer was a resident during the holding period or at sale.

## 15. Reviewer Checklist (Run Before Sign-Off)

- [ ] Confirmed C-corp status at issuance and continuously during holding period (no S-election, no LLC conversion).
- [ ] Confirmed original-issuance acquisition (direct from corp, gift, inheritance, or qualifying partnership distribution).
- [ ] Confirmed gross-asset cap at and immediately after issuance ($50M pre-applicable-date / $75M post-applicable-date).
- [ ] Confirmed active business requirement satisfied for substantially all of holding period (≥80% of assets in qualified trade or business).
- [ ] Confirmed §1202(e)(3) trade-or-business is NOT excluded (run the SSTB analysis, especially the "consulting" and "reputation/skill" tests for any company with material services revenue).
- [ ] Confirmed no §1202(c)(3) significant redemption within 2 years either side of issuance.
- [ ] Confirmed acquisition date (clock start) — paying attention to SAFE conversion date, option exercise date, §83(b) election date, LLC-to-C-corp conversion date.
- [ ] Confirmed holding period (counting from clock start to disposition date) and identified applicable exclusion tier (50%, 75%, or 100% for OBBBA stock).
- [ ] Computed per-issuer cap: greater of $15M (or $10M pre-applicable-date) or 10× aggregate adjusted basis of QSBS from this issuer disposed of in the tax year.
- [ ] Computed §57(a)(7) AMT preference (zero for post-2010 100% stock; 7% of excluded for partial-exclusion stock).
- [ ] Confirmed NIIT computation on taxable portion only.
- [ ] Confirmed Form 8949 code "Q" with proper column (g) adjustment.
- [ ] Confirmed §1045 election (if applicable) is on timely-filed return with Rev. Proc. 98-48 statement.
- [ ] Verified state conformity for each state of residence — special attention to CA, NJ, PA, MS non-conformity.
- [ ] For stacking structures: documented non-tax purposes for each trust contemporaneously; verified §643(f) defensibility; verified gift timing predates LOI to avoid assignment-of-income risk.
- [ ] Obtained engagement letter with explicit disclosure of §1202 audit risk (especially SSTB, gross-asset documentation, holding period under conversion scenarios).

## 16. Provenance and Authorities

### 16.1 Statutory authority

- **Statutory authorities list** — IRC §1202 (current; as amended by OBBBA P.L. 119-21 §70431, July 4, 2025). IRC §1045 (rollover of gain on QSBS). IRC §57(a)(7) (AMT preference for §1202 gain). IRC §1411 (NIIT — applies to taxable portion of QSBS gain). IRC §643(f) (multiple-trust aggregation). IRC §83(b) (election for restricted property). IRC §351 (incorporation transfers). IRC §358 (basis in §351 exchange). IRC §1014 (basis step-up at death — coordinates with §1202(h)(1)(B)).  _([IRC §1202; §1045; §57(a)(7); §1411; §643(f); §83(b); §351; §358; §1014](https://www.law.cornell.edu/uscode/text/26/1202))_

### 16.2 Treasury regulations

- **Treasury regulations list** — Treas. Reg. §1.643(f)-1 (finalized 2020 under T.D. 9913; multiple-trust aggregation rule). Prop. Reg. for §1202 — none currently active.  _([Treas. Reg. §1.643(f)-1; T.D. 9913](https://www.law.cornell.edu/uscode/text/26/1202))_

### 16.3 IRS administrative guidance

- **IRS administrative guidance list** — Rev. Proc. 98-48 (§1045 election procedures). PLR 201436001 (health-tech company is not "health" business). PLR 201717010 (pharmacy services not "health" business). PLR 202144026 (IT staffing is "consulting" business — QSBS denied). CCA 201610006 (factual analysis for §1202(e)(3) SSTB determination). FSA 200145011 ("substantially all" generally means >90% of holding period).  _([Rev. Proc. 98-48; PLR 201436001; PLR 201717010; PLR 202144026; CCA 201610006; FSA 200145011](https://www.law.cornell.edu/uscode/text/26/1202))_

### 16.4 Case law

- **Case law list** — Owen v. Comm'r, T.C. Memo 2012-21 (active business requirement; "passive investment" of cash). Salvatore v. Comm'r, T.C. Memo 1970-30 (assignment-of-income on pre-sale gift). Ferguson v. Comm'r, 174 F.3d 997 (9th Cir. 1999) (assignment-of-income on pre-sale gift after LOI). Quinn v. State, 526 P.3d 1 (Wash. 2023) (WA capital gains tax upheld; no §1202 conformity).  _([Owen v. Comm'r, T.C. Memo 2012-21; Salvatore v. Comm'r, T.C. Memo 1970-30; Ferguson v. Comm'r, 174 F.3d 997 (9th Cir. 1999); Quinn v. State, 526 P.3d 1 (Wash. 2023)](https://www.law.cornell.edu/uscode/text/26/1202))_

### 16.5 Legislative history

- **Legislative history list** — Revenue Reconciliation Act of 1993 (P.L. 103-66) — original §1202 enactment, 50% exclusion. American Recovery and Reinvestment Act of 2009 (P.L. 111-5) — 75% exclusion for stock 2/18/2009–12/31/2010. Small Business Jobs Act of 2010 (P.L. 111-240) — 100% exclusion for stock acquired 9/27/2010–12/31/2010; §57(a)(7) suspension. Tax Relief Act of 2010 (P.L. 111-312) — extended 100% through 12/31/2011. American Taxpayer Relief Act of 2012 (P.L. 112-240) — extended 100% through 12/31/2013. PATH Act of 2015 (P.L. 114-113) — made 100% exclusion and §57(a)(7) suspension PERMANENT. OBBBA P.L. 119-21 (July 4, 2025) §70431 — tiered 50/75/100% exclusion; $15M cap; $75M gross-asset cap; inflation indexing from 2027.  _([P.L. 103-66; P.L. 111-5; P.L. 111-240; P.L. 111-312; P.L. 112-240; P.L. 114-113; P.L. 119-21 §70431](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

### 16.6 Practitioner commentary

Polsky, "§1045 Rollover Holding Period Tacking" (2024) — Position C aggressive holding-period argument. ABA Tax Section Comments on §643(f) Final Regulations (T.D. 9913) — discussion of stacking strategies. AICPA §1202 Practice Guide (2024 edition; awaiting 2025 update for OBBBA).

## 17. Circular 230 Disclosure (Repeated)

This skill produces draft workpapers and analytical positions for review by a credentialed practitioner. Nothing here is a written opinion within §10.37 of Circular 230, is not marketed tax advice, and is not intended for taxpayer reliance to avoid penalties. Every §1202 position requires:
1. Documentary proof of all five §1202(c) requirements (Section 5).
2. A reviewer-confirmed §1202(e)(3) trade-or-business analysis (Section 5.5).
3. Reviewer confirmation of the per-issuer cap computation (Section 12.3).
4. Reviewer confirmation of state conformity treatment for each applicable state (Section 9).
5. For any §1045 rollover, reviewer confirmation that the election was timely filed (Section 6.1).
6. For any family stacking, reviewer confirmation of §643(f) defensibility and assignment-of-income defense (Sections 8.3 and 13.3 AUDIT FLASH POINTS).
The §1202 position is high-value, high-scrutiny. Take the conservative position whenever the record is incomplete and escalate to the credentialed reviewer.

## *End of skill. Tax year 2025. Last updated 2025-11-15. Version 0.1. Verified by: pending.*

End of skill. Tax year 2025. Last updated 2025-11-15. Version 0.1. Verified by: pending.

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
