---
name: us-federal-cost-segregation
description: "US federal cost segregation for tax year 2026: establish land and component basis, classify 5-, 7-, 15-, 27.5- and 39-year property, select the acquisition-cohort bonus rate, assess Form 3115/DCN 7 eligibility and a signed section 481(a) adjustment, apply rental-loss limits and model ordinary taxable sale recapture. Includes the original 2019 look-back and 2025 contract cases. Trigger on cost segregation, cost seg study, look-back study, accelerate building depreciation or bonus on rental property. Federal only."
version: "2.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: income-tax
type: computation
---

# US federal cost segregation for real property, tax year 2026

**Answer first.** Determine each asset's supported classification and depreciable basis before applying bonus. Ordinary qualified short-life property acquired and placed in service after January 19, 2025 generally receives 100% bonus; an ordinary pre-January 20, 2025 acquisition placed in service in 2026 receives 20%. A look-back study needs a separate method-change eligibility check, and accelerated depreciation is not necessarily a currently usable loss. [Notice 2026-11 §§2–3](https://www.irs.gov/pub/irs-drop/n-26-11.pdf).

Built from the law. Not yet approved. This is written tax guidance under Circular 230 §10.37; establish the actual facts and applicable law before using a filing position.

## Scope and who this is for

Individuals, partnerships, S corporations and C corporations owning US business or rental real property: purchases, new construction, improvements and look-back studies. Federal depreciation, catch-up, loss usability and an ordinary taxable sale are the job. The study reallocates supported cost; it does not create additional basis.

| Adjacent job | Destination |
|---|---|
| Section 179 limits, equipment and vehicle caps | `us-section-179-and-bonus-depreciation` |
| State conformity | `us-state-bonus-depreciation-conformity-matrix`, then the state's rules |
| Rental return | `us-schedule-e-rental-income` |
| Real estate professional and short stays | `us-real-estate-professional-and-short-term-rentals` |
| Exchanges, installment sales, capital gains, NOL | `us-section-1031-like-kind-exchange`, `us-installment-sale-6252`, `us-capital-gains`, `us-net-operating-loss-172` |

Personal residences, dealer property, mainly foreign use and housing/rehabilitation credits remain outside this computation. Do not project this method onto them.

## Ask the client first

Obtain the tax year, entity and year-end; contracts, amendments, damages provisions, enforceability, cancellation/contingency dates and closing; each asset's ready-for-use date; construction dates/cost records; appraisals, land and component allocations; business/personal use; prior depreciation and bonus elections; ADS and interest-election status; ownership, basis and financing; filing status, modified AGI, other losses/passive income and participation evidence for both spouses; and exit plans. These are required facts, not inferred defaults. Missing eligibility, dates, basis or loss evidence means **HOLD the affected result**. Do not assign an earlier acquisition date, invent hours or assume a sale date. Check this point with one of our partner accountants.

## The method, step by step

### Basis, study and recovery classes

1. Remove nondepreciable land. Divide a purchased property's cost using relative fair market values at purchase; if those values are uncertain, assessed values may support the ratio. Do not substitute an unsupported percentage. [Publication 527, Basis of Depreciable Property](https://www.irs.gov/publications/p527).
2. Reconcile the study to actual total cost, including indirect costs, and document asset descriptions, methodology, cost support, legal classification, photographs where relevant and preparer expertise. The IRS audit guide prescribes no exclusive study methodology; actual-cost engineering is generally the most accurate approach, but purchased-property estimates require support. Its six Whiteco questions consider movability, intended permanence, expected affixation period, removal effort, removal damage and manner of attachment. The audit guide is examination guidance, not a pronouncement of law. [Publication 5653, chapters 2–4](https://www.irs.gov/pub/irs-pdf/p5653.pdf).
3. Classify each asset under the applicable asset class and law; a building's structural component does not acquire a short life merely because it can be identified separately. The following are ordinary GDS classes, subject to the actual activity/asset classification, elections and required ADS. [26 USC 168(b)–(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm).

| Class | Examples and ordinary method | Source |
|---|---|---|
| 5 years | Residential rental appliances, carpets and furniture; computers and office machinery. Generally 200% declining balance, switching to straight line when larger. | [Pub. 946, Which Property Class Applies; §168(b)](https://www.irs.gov/publications/p946) |
| 7 years | Office furniture/fixtures; otherwise-unassigned property without a class life. Generally 200% declining balance with the straight-line switch. | [Pub. 946; §168(e)(3)(C)](https://www.irs.gov/publications/p946) |
| 15 years | Certain land improvements such as shrubbery, fences, roads, sidewalks and bridges: generally 150% declining balance with the straight-line switch. Qualified improvement property (QIP): straight line. A label alone does not settle classification. | [Pub. 946](https://www.irs.gov/publications/p946); [§168(b)(2)–(3), (e)(3)(E)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| 27.5 years | Residential rental building and structural components; straight line, mid-month. Residential means at least 80% of gross rental income from dwelling units; a hotel/motel/other establishment with more than half the units used transiently is excluded from dwelling units. Include fair rental value of owner-occupied space as the statute requires. | [§168(b)(3), (c), (d)(2), (e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| 39 years | Ordinary nonresidential building and structural components; straight line, mid-month. March first-year Table A-7a rate: 2.033%. Qualified production property under §168(n) is a separate held issue below. | [§168(b)–(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm); [Pub. 946 Table A-7a](https://www.irs.gov/publications/p946) |

QIP is an improvement **made by the taxpayer** to an interior portion of a nonresidential building, placed in service after the building's first service date; exclude enlargement, elevators/escalators and internal structural framework. An acquired existing interior is not automatically the buyer's QIP. [§168(e)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm).

For ordinary short-life residual basis use half-year unless the mid-quarter test applies: more than 40% of relevant annual bases placed in service in the final three months. Exclude residential/nonresidential real property, railroad grading/tunnel bores and assets placed and disposed of in the same year from that test. Check actual tax-basis adjustments rather than gross project spending. [§168(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm).

### Bonus and section 179

| Cohort | Rate and operative conditions | Source |
|---|---|---|
| Qualified property acquired AND placed in service after January 19, 2025 | 100%, unless an applicable election; no scheduled phase-down for this cohort. | [PL 119-21 §70301](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [Pub. 946](https://www.irs.gov/publications/p946) |
| Ordinary acquisition after September 27, 2017 but before January 20, 2025 | 40% if placed in service in 2025; 20% if in 2026. Long-production/aircraft have different rules, held below. | [Former §168(k)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm); [Notice §2.01](https://www.irs.gov/pub/irs-drop/n-26-11.pdf) |
| First taxable year ending after January 19, 2025, new acquisition cohort | Transition election substitutes 40% (60% for specified long-production/aircraft) for 100%; calendar-year 2025, not calendar-year 2026. Timely-return statement including extensions. | [PL 119-21 §70301(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [Notice §4.03](https://www.irs.gov/pub/irs-drop/n-26-11.pdf) |

For a binding purchase contract, use the latest of signing, state-law enforceability, end of cancellation periods and satisfaction of controlled contingencies. A damages cap of **at least 5% of total contract price** is not treated as a specified-damages limit; consider the highest of multiple caps. Conditions outside either party's/predecessor's control need not prevent binding status. An option or letter of intent is not a binding contract. A nonbinding-contract acquisition generally occurs when paid/incurred cost exceeds 10%, excluding land/preliminaries. Construction has separate physical-work and payment-safe-harbor rules; actual self/third-party construction and component elections are held below. [Notice §§2.03, 3.03–3.05](https://www.irs.gov/pub/irs-drop/n-26-11.pdf); [Reg. §1.168(k)-2(b)(5)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol3/pdf/CFR-2025-title26-vol3-sec1-168k-2.pdf).

Bonus is not automatic for every study allocation. For the ordinary short-life route require MACRS recovery of 20 years or less and original use or a qualifying used acquisition. Used acquisitions must satisfy §179(d)(2)–(3) purchase/basis rules, including related-party, controlled-group and carryover/inherited-basis restrictions. Prior depreciable interest of the taxpayer **or predecessor** is tested over the regulatory five-calendar-year lookback plus the current pre-service period, limited to existence periods; a plain prior lease without depreciable interest is not itself disqualifying. Hold unresolved prior-interest/acquisition cases. [§168(k)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm); [Reg. §1.168(k)-2(b)(3)](https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol3/pdf/CFR-2025-title26-vol3-sec1-168k-2.pdf).

Required ADS prevents §168(k) bonus; a voluntary ADS election alone is excluded from this statutory bonus test. An electing real property trade/business must use ADS for nonresidential real property, residential rental property and QIP, not automatically every personal-property/land-improvement component. Ordinary 27.5/39-year buildings do not meet the 20-year short-life route; §168(n) remains separately held. Same-year placement/disposal, acquisition-year conversion to personal use and utility/floor-plan-financing exclusions also need testing. [§168(g)(8), (k)(2)(D), (k)(9)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm); [Form 4562 instructions](https://www.irs.gov/instructions/i4562).

Apply any allowable elected section 179 first, then bonus on eligible adjusted business/investment basis after allocable credits/deductions, then regular MACRS on the remainder. Property is placed in service when ready and available for its specific use. Bonus election out is by class for all qualifying property in that class for the year, by the owning entity; attach the statement to a timely return including extensions. Revocation generally needs IRS consent; DCN 7 does not undo an election. Notice reliance requires applying its §§3–5 in full to all eligible property as specified in §6.02. [Pub. 946](https://www.irs.gov/publications/p946); [§168(k)(7)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm); [Notice](https://www.irs.gov/pub/irs-drop/n-26-11.pdf).

Section 179 requires an eligible purchase for active trade/business use and is subject to aggregate dollar, investment phase-out and business-income limits; income-limited elected cost carries forward. Land/ordinary land improvements do not qualify. Elected qualified real property includes QIP and later roofs, HVAC, fire/alarm and security improvements to nonresidential real property. Section 179(d)(1) expressly excepts §50(b)(2) from its exclusion: **withdraw the blanket apartment-contents exclusion**. Noncorporate lessors need the manufactured-property alternative or lease under 50% of class life plus §162 deductions (excluding rents/reimbursements) above 15% of rent in the first 12 months after transfer to the lessee. An S corporation is a corporation for this lessor rule. Apply the full computation in `us-section-179-and-bonus-depreciation`; actual rental-business/lessor classification unresolved: Check this point with one of our partner accountants. [§179(b), (d), (e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec179.htm).

### Look-back method and signed catch-up

DCN 7 is the automatic impermissible-to-permissible depreciation change under Rev. Proc. 2025-23 §6.01. Ordinary applicability includes an impermissible method in at least the two immediately preceding taxable years, a method change under the regulation and ownership at the beginning of the change year. Check **all** §6.01 exclusions and Rev. Proc. 2015-13 eligibility before using it; a study alone does not establish consent. For one-year depreciable property, §6.01(1)(b) permits Form 3115 or an amendment/AAR for the service year before filing the succeeding-year return. Thus “never amend” is not a universal rule. [Rev. Proc. 2025-23 §§6.01(1), (9)](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf).

Compute signed §481(a) adjustment = depreciation taken into account under the old method **minus** allowable depreciation under the proposed method for all prior open/closed years, with required capitalization adjustments. Use each asset's historical service-year bonus eligibility/rate, not the 2026 rate. Adjust opening basis to allowable depreciation. A negative adjustment decreases income, normally entirely in the change year; a positive adjustment normally enters ratably over four taxable years. A positive adjustment **below $50,000** may elect one year on Form 3115. Examination, cessation/acquisition and other special periods require separate review. [Rev. Proc. 2025-23 §§6.01(5)–(7)](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf); [Rev. Proc. 2015-13 §7.03](https://www.irs.gov/pub/irs-drop/rp-15-13.pdf).

Supply detailed old/new methods, asset facts, legal classification and service dates; “MACRS to MACRS” is insufficient. Reduced Form 3115 completion under §6.01(4) is available for qualifying three-prior-year average receipts **at most $10 million**, computed under the cited regulation; it does not remove the applicable statements. Do not use DCN 7 for late/revoked elections, a changed service date/use or excluded reclassifications. Actual eligibility/examination/late-election relief: Check this point with one of our partner accountants. [Rev. Proc. 2025-23 §§6.01(1)(c), (3)–(4)](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf).

### Loss usability

Apply owner basis and at-risk limitations before passive limits, then the noncorporate excess-business-loss rules. Do not infer a wage offset from bonus or real estate professional status. Qualified nonrecourse financing under §465(b)(6), lender identity, related lenders and other at-risk exceptions require actual financing analysis: Check this point with one of our partner accountants. [Forms 8582 and 461 instructions](https://www.irs.gov/instructions/i8582).

Rentals generally remain passive under §469(c)(2). Real estate professional status requires **both** more than 750 hours and more than half of personal services in trades/businesses in real-property trades/businesses materially participated in. On a joint return one spouse must satisfy both separately; spouse participation counts in deciding material participation. Employee services count as real-property services only during qualifying more-than-5%-ownership periods, with attribution rules. A qualifying person must still materially participate in each rental or the validly elected combined rental activity; the aggregation statement goes with the original return. [§469(c)(7), (h)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm); [Reg. §1.469-9](https://www.ecfr.gov/current/title-26/section-1.469-9).

| Rental-loss rule | Amount and conditions | Source |
|---|---|---|
| Active rental allowance, individual single/joint | Annual aggregate maximum $25,000; active participation and at least 10% ownership by value including spouse throughout the relevant period. Limited-partner interests generally do not qualify; PTPs are separate and excluded from this allowance. | [§469(i)(1)–(2), (6), (k)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Phase-out | Reduce by 50% of modified AGI above $100,000, floor zero; eliminated at $150,000. MAGI is the statutory §469(i)(3)(E) amount, not unadjusted return AGI. | [§469(i)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Married separate, apart all year | $12,500 maximum, phase-out starts $50,000 and reaches zero at $75,000; if not apart all year, no allowance. | [§469(i)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Excess business loss, tax years beginning 2026 | $256,000; $512,000 joint. Aggregate business-loss computation after passive limits, not an automatic cap on every rental loss. | [Rev. Proc. 2025-32 §4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

Active participation involves bona fide management decisions/arranging services, not ownership alone. For MAGI disregard §86 income; exclusions under §§85(c), 135, 137; deductions under §§219, 221, 250; passive losses and §469(c)(7) losses. Suspended passive losses carry forward; entire-interest taxable unrelated-party dispositions require the §469(g) computation, with installment/grouped-activity exceptions held. Short stays averaging at most seven days, or at most 30 days with significant personal services, can be outside rental treatment; determine material participation and other conditions using the dedicated Guide. Corporate passive-loss/real-property-business tests, including the closely held corporation's more-than-50%-gross-receipts test, and actual excess-loss/NOL outcomes: Check this point with one of our partner accountants. [§469(b), (c)(7), (g), (i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm); [Reg. §1.469-1T(e)(3)](https://www.ecfr.gov/current/title-26/section-1.469-1T).

### Exit

Allocate supported consideration and adjusted basis to each asset. For an ordinary taxable §1245 sale, ordinary income is the positive excess of the lower of recomputed basis or amount realized over adjusted basis; recomputed basis restores allowed/allowable depreciation, including bonus and section 179. For §1250 property held over one year, additional depreciation above straight line can be ordinary income; do not apply a flat 25% rate to all sale gain. Remaining unrecaptured §1250 gain has a **maximum** 25% rate under §1(h), subject to annual netting. Net §1231 gain is recharacterized as ordinary to the extent of nonrecaptured net §1231 losses in the five preceding taxable years. [§1245](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIV-sec1245.htm); [§1250](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIV-sec1250.htm); [§1(h)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm); [§1231(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIV-sec1231.htm).

## Boundary and exception table

| Situation | Action |
|---|---|
| Unsupported percentage or disputed classification/basis | HOLD the deduction. Obtain cost support and legal analysis; no generic “20%–40% reclassifiable” forecast. |
| Prior election out, related acquisition, required ADS, unknown dates/use | Apply the specific rule above; HOLD unresolved entitlement, rather than selecting a supposedly conservative rate. |
| Construction/component election, long-production/aircraft, §168(n), utility property, consolidated group | Non-usable HOLD, including the original §168(n) construction-before-January 1, 2029/service-before-January 1, 2031 boundaries; those dates alone do not establish qualification. Historical special-property 60% for 2025 / 40% for 2026 service belongs to its own pre-2025 acquisition schedule, not the ordinary 40%/20% row. Check this point with one of our partner accountants. |
| One-return property, excluded method change, changed use/date, examination, late/revoked election, cessation/acquisition or automatic six-month relief | Non-usable procedural HOLD until the specific eligibility/relief is established. Check this point with one of our partner accountants. |
| Exchange/carryover versus excess basis; §1245/§1250 land-improvement classification; §179 real-property recapture; §291 corporate recapture (the historical 20% excess formula is not a proved result for this owner); installment sale; grouped-activity disposal | Non-usable HOLD for actual recapture/basis result; do not assume no gain without cash or spread recapture with payments. Check this point with one of our partner accountants. |

## Worked cases

Illustrative inputs, not appraisals or filing determinations. Unless stated otherwise, assume documented qualifying business/investment basis, no disqualifying use/election, no required ADS and no unmentioned credit/basis adjustment. Actual eligibility and loss usability remain separate checks.

**Case 1 — 2026 office decision.** Binding contract February 2026, closing and service March 2026; price $3,000,000, land $600,000; supported study: 5-year $240,000, 7-year $60,000, 15-year $300,000, 39-year $1,800,000. Assume the short-life allocations qualify for 100% bonus and Table A-7a is applicable. Without the study: $2,400,000 × 2.033% = $48,792. With it: $600,000 bonus + $36,594 building = $636,594; incremental first-year deduction $587,802. Compare usable tax savings, study fee and exit recapture before recommending it. Neither C corporation ownership nor real estate professional status alone proves usability. [Pub. 946 Table A-7a](https://www.irs.gov/publications/p946).

```oa-check
name: Cost segregation decision, 2026 office purchase
inputs:
  building_basis: 2400000
  short_life: 600000
  building_after_study: 1800000
  rate_39yr_month3: 0.02033
  bonus_rate: 1.00
steps:
  - without_study: building_basis * rate_39yr_month3
  - with_study: short_life * bonus_rate + building_after_study * rate_39yr_month3
  - extra_deduction: with_study - without_study
expected:
  without_study: 48792.00
  with_study: 636594.00
  extra_deduction: 587802.00
```

**Case 2 — 2019 rental look-back in 2026.** Single owner; 2019–2025 returns used 27.5 years, no bonus election out. Study moves $200,000 to 5-/15-year assets; assume 2019 acquisition/service qualified for 100% historical bonus, DCN 7 eligibility and $47,000 actually taken. Signed adjustment = $47,000 − $200,000 = **−$153,000**, ordinarily a 2026 deduction. Rental net before adjustment $20,000 gives $133,000 loss. With active participation, qualifying ownership, no other passive income/competing losses or credits, adequate basis/at-risk and statutory MAGI $130,000, allowance is $10,000 and $123,000 is suspended under §469. These stipulated facts do not establish an actual filing position. [Rev. Proc. 2025-23 §6.01](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf); [§469(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm).

```oa-check
name: Signed look-back adjustment and special allowance, 2026
inputs:
  allowable: 200000
  claimed: 47000
  rental_net_before: 20000
  magi: 130000
steps:
  - adjustment_481a: claimed - allowable
  - rental_loss: -(rental_net_before + adjustment_481a)
  - allowance: max(25000 - max(magi - 100000, 0) * 0.5, 0)
  - allowed: min(allowance, rental_loss)
  - suspended: rental_loss - allowed
expected:
  adjustment_481a: -153000.00
  rental_loss: 133000.00
  allowance: 10000.00
  suspended: 123000.00
```

**Case 3 — old contract.** Binding December 2024 contract, closing/service February 2025, $500,000 ordinary qualifying 5-/15-year property. Assume enforceability with no later cancellation/controlled contingency, no special construction/long-production/aircraft rule. 40% bonus = $200,000, residual MACRS basis $300,000. Hypothetical service in 2026 instead gives 20% = $100,000 bonus and $400,000 residual. Do not silently replace the original 2025 facts. [Former §168(k)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm).

**Case 4 — spouses.** A: full-time W-2 work and 400 rental hours; B: no other work and 900 rental hours. If B's 900 hours are qualifying personal services in real-property trades/businesses materially participated in, B independently exceeds 750 and half of B's services; joint-return status can qualify. Do not add A's hours to B's two tests. Spouse participation can count for material participation in the separate or validly combined rental activity; the loss still needs all other limits. [§469(c)(7), (h)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm).

**Case 5 — ordinary taxable sale.** Individual, rental held over one year. 5-year items: $100,000 bonus, zero adjusted basis, $10,000 allocated amount realized, no other adjustments; ordinary §1245 gain $10,000. Building: $180,000 straight-line depreciation, $400,000 gain, no prior §1231 losses. Assume no other annual §1231/capital netting items or ordinary recapture. Then $400,000 is §1231 long-term gain, $180,000 unrecaptured §1250 gain (maximum 25%) and $220,000 remainder subject to applicable capital-gain rates. This is gain character, not a tax-due computation. [§1245](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIV-sec1245.htm); [§1(h)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm).

**Case 6 — restored original section 179 case.** Corporation places $4,200,000 qualifying property in service in a tax year beginning in 2026. Ceiling: $2,560,000 − ($4,200,000 − $4,090,000) = **$2,450,000**, before business-income and other limits. [Rev. Proc. 2025-32 §4.24](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).

**Case 7 — restored original allowance case.** Single active participant, MAGI $130,000, bonus-driven rental loss $40,000, no other passive income. With qualifying ownership and other-limit/no-competing-item assumptions as in Case 2: reduction $15,000, allowance/deduction $10,000, suspended $30,000. These inputs differ from Case 2 and are retained separately. [§469(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm).

## When to refuse or refer

Refuse unsupported percentages and missing eligibility evidence. Engineering study preparation, unsubstantiated participation, actual at-risk financing, corporate passive tests, rare boundary rows and unresolved return mechanics are non-usable HOLDs. Check this point with one of our partner accountants.

## Filing and payment

Form 4562 supports current depreciation; the **2025** instructions place section 179 in Part I, ordinary non-listed bonus on line 14 in Part II and regular MACRS in Part III. Final 2026 line mapping is held, not inferred from those instructions. [Form 4562 instructions](https://www.irs.gov/instructions/i4562).

For an eligible automatic change, attach the original Form 3115 to the timely filed original return for the change year including extensions; file the signed duplicate with the IRS, ordinarily Ogden under current instructions, no earlier than the first day of that year and no later than filing the original. No user fee applies to an automatic change. Confirm current delivery instructions. [Form 3115 instructions, When/Where To File](https://www.irs.gov/instructions/i3115).

Reconcile the owner’s return destination (Schedule E/Form 8825/Form 1065/Form 1120), possible loss-limit forms (6198/8582/461) and sale forms (4797/Schedule D worksheet). Actual form applicability and 2026 line mapping, including Schedule E line 43, is a non-usable HOLD. Check this point with one of our partner accountants.

Ordinary calendar-2026 individual filing/payment date: April 15, 2027; valid timely Form 4868 with properly estimated full tax gives six months to October 15, 2027. Payment is not extended. Calendar partnerships/S corporations ordinarily file March 15, 2027. Special deadlines, actual late interest/penalties and fiscal/entity variations: Check this point with one of our partner accountants. [§6072](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm); [Reg. §1.6081-4](https://www.ecfr.gov/current/title-26/section-1.6081-4).

Historical 2025 returns remain a separate cohort, not “still open” by default: ordinary individual extension date October 15, 2026 has passed. The 2025 section 179 ceiling/phase-out was $2,500,000/$4,000,000 and excess-loss threshold $313,000/$626,000 joint; retain those years for historical analysis only. Actual late-return, automatic six-month Form 3115 relief or election remedy: Check this point with one of our partner accountants. [Rev. Proc. 2025-32 §§3.02, 4.24](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Rev. Proc. 2024-40 §2.32](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf).

## Completion checklist

Reconcile cost/land/components; establish service/acquisition/ADS/elections; calculate depreciation and signed catch-up; establish method-change consent/filing; apply owner loss limits; model supported asset-level exit; check state treatment separately. Report usable amounts separately from arithmetic scenarios and HOLDs.

## Sources

| Official source and operative portions read | URL | Read on |
|---|---|---|
| §168(b)–(e): GDS methods, periods, conventions, residential definition and QIP; (g)(8), (k): ADS/bonus. 2024 baseline reconciled to PL 119-21 for amended bonus cohorts. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm | 2026-11-27 |
| PL 119-21 §70301 bonus cohorts/transition; Notice §§2–6 contract/rate/election/reliance. Unchanged passages reused from independently passed depreciation ledger after applicability check. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm ; https://www.irs.gov/pub/irs-drop/n-26-11.pdf | 2026-11-27 |
| §1.168(k)-2(b)(3), (5) used interests/contracts; §179(b), (d), (e) limits, purchase, lessors, qualified real property; passed same-year depreciation ledger quotes reused. | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol3/pdf/CFR-2025-title26-vol3-sec1-168k-2.pdf ; https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec179.htm | 2026-11-27 |
| Publications 527 basis/land; 946 classes, service, bonus basis and March Table A-7a; 5653 chapters 2–4 classification/study documentation (audit guide limitations noted). | https://www.irs.gov/publications/p527 ; https://www.irs.gov/publications/p946 ; https://www.irs.gov/pub/irs-pdf/p5653.pdf | 2026-11-27 |
| Rev. Proc. 2025-23 §6.01 applicability/exclusions/statements/adjustment/DCN; Rev. Proc. 2015-13 §7.03 periods/exceptions. | https://www.irs.gov/pub/irs-drop/rp-25-23.pdf ; https://www.irs.gov/pub/irs-drop/rp-15-13.pdf | 2026-11-27 |
| §469(b), (c)(7), (g), (h), (i), (k); regulations §§1.469-9 and 1.469-1T(e)(3). Same-year independently passed rental Guide quotes reused where unchanged. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm ; https://www.ecfr.gov/current/title-26/section-1.469-9 ; https://www.ecfr.gov/current/title-26/section-1.469-1T | 2026-11-27 |
| Rev. Proc. 2025-32 §§3.02, 4.24, 4.31; Rev. Proc. 2024-40 §2.32: indexed amounts, with years kept separate. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf ; https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-27 |
| §§1245(a), 1250(a)–(b), 1231(a)–(c), 1(h)(1)/(6): ordinary sale and annual-netting limits; Pub. 544 corresponding recapture discussion. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIV-sec1245.htm ; https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIV-sec1250.htm ; https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partIV-sec1231.htm ; https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm ; https://www.irs.gov/publications/p544 | 2026-11-27 |
| Forms 4562 (2025), 3115 (12/2022), 8582 and 461: prior-edition mechanics/ordering only. §6072 and Reg. §1.6081-4 deadlines/extension; passed same-year rental/depreciation ledger reused. | https://www.irs.gov/instructions/i4562 ; https://www.irs.gov/instructions/i3115 ; https://www.irs.gov/instructions/i8582 ; https://www.irs.gov/instructions/i461 ; https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm ; https://www.ecfr.gov/current/title-26/section-1.6081-4 | 2026-11-27 |

Not yet confirmed: actual engineering classifications, construction/component/special-property and §168(n) outcomes, at-risk/corporate/rare disposal outcomes, election/late-return/examination remedies and final 2026 form lines are explicit non-usable HOLDs above. Check this point with one of our partner accountants.
