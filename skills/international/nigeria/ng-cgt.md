---
name: ng-cgt
description: Use this skill whenever asked about Nigerian Capital Gains Tax. Trigger on phrases like "Nigeria CGT", "Capital Gains Tax Nigeria", "sale of shares Nigeria", "property gains Nigeria", "10% CGT Nigeria", "CGTA Nigeria", "disposal of chargeable assets Nigeria", "Section 30 CGTA", "rollover relief Nigeria", "NGX share disposal tax", "₦100M share threshold", "non-resident CGT Nigeria", or any question about computing, filing, or reporting capital gains on Nigerian chargeable assets. Scope covers CGT computation for chargeable assets (real property, shares, business assets, intangibles), statutory exemptions, rollover relief on replacement of business assets, the Finance Act 2021 share disposal threshold, and the NTA 2025 consolidation of CGT into the general income tax framework. ALWAYS read this skill before touching Nigerian CGT work.
jurisdiction: NG
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Omolola Fasasi
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NG Cgt

## Nigeria — Capital Gains Tax (CGT) — Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

- **CGT rate - companies** — 0.3  _(NIGERIA TAX ACT 2025)_
- **CGT rate - individuals** — 0% - 25%  _(NIGERIA TAX ACT 2025)_
- **Gain on disposal of principal private residence** — Exempt  _(NIGERIA TAX ACT 2025)_
- **Gains on Nigerian government securities** — Exempt  _(NIGERIA TAX ACT 2025)_
- **Gains from life assurance policies** — Exempt  _(NIGERIA TAX ACT 2025)_
- **CGT return filing deadline** — returns mus be filed bi - annually by 30th june  _(NIGERIA TAX ACT 2025)_
- **Indexation allowance available** — The Nigeria Tax Act (NTA) completely eliminates inflation indexation allowances when computing Capital Gains Tax. The new law explicitly prohibits the indexation of asset base costs for inflation and rules out capital losses for offset. [1]  _(NIGERIA TAX ACT 2025)_
- **Capital losses — offset rule** — capital losses to be offset against gains of the same asset class and carried forward  _(NIGERIA TAX ACT 2025)_
- **CGT - share sale exemption threshold proceeds <#150m and gains <#10m in 12 consecutive months** — Exempt  _(NIGERIA TAX ACT 2025)_

## Section 1 — Quick reference

**Section 1 — Quick reference table**

| Field | Value |
| --- | --- |
| Country | Federal Republic of Nigeria |
| Tax | Capital Gains Tax (CGT) |
| Currency | NGN (Nigerian Naira, ₦) |
| Tax year | 1 January to 31 December (companies); fiscal year of the taxpayer (individuals — generally calendar year) |
| Primary legislation (pre-NTA) | Capital Gains Tax Act (CGTA) Cap C1, LFN 2004 |
| Amending legislation | Finance Act 2019; Finance Act 2020; Finance Act 2021; Finance Act 2022; Finance Act 2023 |
| Post-2025 framework | Nigeria Tax Act (NTA) 2025 — CGT consolidated into the general income tax framework (implementing regulations pending) |
| Headline rate | **10%** on chargeable gains |
| Tax authority (residents) | Federal Inland Revenue Service (FIRS) for companies and non-residents; relevant State Internal Revenue Service (SIRS) for resident individuals |
| Filing | Lodged with the annual income tax return — CIT (companies) or PIT (individuals) |
| Validated by | Verified by Omolola Fasasi (MB058950) on 2026-06-21 |
| Skill version | 1.0 |

### CGT rate at a glance

**CGT rate at a glance**

| Asset class | Rate | Notes |
| --- | --- | --- |
| Real property (land & buildings) | 10% | On chargeable gain (proceeds − cost − allowable expenses) |
| Shares — aggregate disposals ≤ ₦100M in any 12 months | 0% | Exempt (Finance Act 2021) |
| Shares — aggregate disposals > ₦100M in any 12 months, where proceeds NOT reinvested in Nigerian shares within the same year | 10% | Tax base is the chargeable gain only on the portion above ₦100M |
| Business assets (plant, goodwill, intangibles) | 10% | Rollover relief may apply (see §4) |
| Listed shares disposed of via NGX, below threshold | 0% | Pre-Finance Act 2021 blanket exemption now restricted to the ₦100M threshold |
| Non-resident on Nigerian-situs assets | 10% | Buyer / payment agent may be required to withhold |

## Section 2 — Required inputs & refusal catalogue

### Required inputs

- **Required inputs before computing Nigerian CGT position** — 1. Identity & residency — taxpayer name, TIN, residency status (resident individual, resident company, non-resident). 2. Asset description — class (real property, shares, business asset, intangible, other chattel). 3. Acquisition data — acquisition date, acquisition cost (with documentary support), incidental costs of acquisition. 4. Disposal data — disposal date, disposal proceeds, incidental costs of disposal (legal fees, commissions, transfer duties). 5. Connection — whether the parties are connected persons (market value rule applies under CGTA s. 19). 6. For shares — aggregate proceeds from share disposals in the same 12-month window across the taxpayer's portfolio; reinvestment in other Nigerian company shares within the same tax year. 7. For business assets — whether replacement asset has been acquired (or will be) within the rollover window. 8. Prior-year losses — CGT losses brought forward (capital losses ring-fenced from income).

### Refusal catalogue

STOP and do not produce a final CGT figure where any of the following applies:

- **Acquisition cost is unknown or undocumented** — Cannot compute chargeable gain; do not use estimates without explicit reviewer sign-off
- **Asset acquired by gift / inheritance with no probate valuation** — Need market-value documentation for base cost
- **Cross-border disposal where double-tax-treaty relief may apply** — Requires bilateral treaty analysis — out of scope of this skill
- **Disposal of partnership interests** — Treatment uncertain under CGTA; refer to FIRS guidance
- **Mineral rights / oil-block disposals** — Petroleum Industry Act overlay — out of scope
- **Trust / estate disposals** — Specialist trust-CGT regime — out of scope
- **Disposal occurring after NTA 2025 commencement where final implementing regulations are not yet published** — Conservative default: compute under CGTA framework, flag for review once NTA regulations issued
- **Insufficient evidence that the ₦100M share threshold has been correctly aggregated across the taxpayer's full portfolio** — Cannot confirm exemption eligibility

## Section 3 — Tier 1 — chargeable persons, chargeable assets, computation

### 3.1 Chargeable persons (CGTA s. 2)

- **Chargeable persons** — CGT is charged on the chargeable gains accruing to: - A resident individual — on worldwide chargeable assets, subject to remittance basis for non-Nigerian-situs assets where gains are not brought into Nigeria. - A resident company — on worldwide chargeable assets. - A non-resident person — on chargeable assets situated in Nigeria (Nigerian land, Nigerian-incorporated company shares, business assets used in a Nigerian trade or branch).  _(CGTA s. 2)_

### 3.2 Chargeable assets (CGTA s. 3)

- **Chargeable assets** — All forms of property are chargeable assets, including: - Land and buildings (whether in Nigeria or abroad, for residents). - Shares and stocks of any company, subject to the Finance Act 2021 ₦100M threshold (see §4). - Goodwill and other intangible business assets. - Options, debts, and incorporeal property generally. - Currency other than Nigerian currency. - Any form of property created by the person disposing of it.  _(CGTA s. 3)_

### 3.3 Computation formula

- **Chargeable gain / CGT payable formula** — Chargeable gain = Disposal proceeds − Allowable acquisition cost − Incidental costs of acquisition − Incidental costs of disposal − Enhancement expenditure (capital improvements only) CGT payable = Chargeable gain × 10%

### 3.4 Allowable deductions (CGTA s. 13)

- **Allowable deductions** — - Original acquisition cost. - Incidental costs of acquisition (legal fees, stamp duty, survey, commission). - Enhancement expenditure reflected in the state of the asset at disposal — routine repairs and revenue expenditure are NOT allowable. - Incidental costs of disposal (legal fees, agent's commission, advertising). - Costs of establishing, preserving, or defending title to the asset.  _(CGTA s. 13)_

### 3.5 Connected persons rule (CGTA s. 19)

- **Connected persons rule** — Where the disposal is between connected persons (relatives, controlling shareholders, group companies), the transaction is deemed to be at market value, regardless of the stated consideration. This prevents undervaluation between related parties.  _(CGTA s. 19)_

### 3.6 Capital losses (CGTA s. 5)

- **Capital losses** — - Capital losses are ring-fenced — they may only be set against capital gains, not against income. - Losses may be carried forward indefinitely against future capital gains of the same person. - Losses on disposals to connected persons are restricted to gains on subsequent disposals to the same connected person.  _(CGTA s. 5)_

## Section 4 — Tier 2 — exemptions, rollover relief, NTA 2025 changes

### 4.1 Statutory exemptions (CGTA ss. 26-43)

The following are exempt from CGT:

**Statutory exemptions table**  _(CGTA ss. 26-43)_

| Exemption | Authority | Notes |
| --- | --- | --- |
| Principal private residence | CGTA s. 36 | Sole or main dwelling, subject to area limit |
| Personal chattels disposed of for ≤ ₦1,000 | CGTA s. 37 | Small disposal exemption |
| Motor vehicles (private passenger cars) | CGTA s. 38 | Not commercial vehicles |
| Gifts to charity / educational / ecclesiastical bodies | CGTA s. 30 | Recipient must be registered |
| Life assurance policy proceeds | CGTA s. 33 | To original policyholder |
| Stocks & bonds — Federal Government, State Government, LGA, statutory corporation securities | CGTA s. 30 | Sovereign and parastatal debt exempt |
| Transfers between spouses | CGTA s. 36 | No-gain-no-loss treatment |
| Compensation for personal injury | CGTA s. 35 | Restricted to genuine injury awards |
| Diplomatic missions | CGTA s. 39 | Reciprocal basis |

### 4.2 Shares — the ₦100M threshold (Finance Act 2021)

- **₦100M share threshold rule** — Before the Finance Act 2021, gains on disposals of shares (especially listed shares) were broadly exempt. The Finance Act 2021 introduced a threshold rule: - Share disposals where the aggregate proceeds across all share disposals by the taxpayer in any 12-month period do not exceed ₦100 million remain exempt. - Where aggregate proceeds exceed ₦100 million in any 12-month period, the portion above ₦100M is brought into charge at 10%, unless the proceeds are reinvested in the shares of any Nigerian company within the same tax year. - The reinvestment relief is asset-class specific — reinvestment must be in Nigerian company shares, not in other asset classes. - The taxpayer must aggregate disposals across all brokers, accounts, and NGX-listed and unlisted companies. Worked aggregation rule: Compute total share-disposal proceeds in the rolling 12-month window. Deduct ₦100M. If the residual is positive AND not reinvested in Nigerian shares within the tax year, the chargeable gain attributable to that residual portion is taxable at 10%.  _(Finance Act 2021)_

### 4.3 Rollover relief — replacement of business assets (CGTA s. 32)

- **Rollover relief on replacement business assets** — Where a person disposes of a business asset and acquires a replacement business asset within 12 months before or after the disposal, the gain on the old asset may be deferred (rolled over) into the base cost of the new asset. Qualifying classes of business assets include: - Land and buildings occupied and used for the trade. - Fixed plant and machinery. - Ships, aircraft, hovercraft. - Goodwill. The classes must match — e.g. land replaced with land, plant with plant. Mixed-class rollover requires FIRS confirmation. Where only part of the proceeds is reinvested, partial rollover applies and the un-reinvested portion is immediately chargeable.  _(CGTA s. 32)_

### 4.4 NTA 2025 — consolidation of CGT into the income tax framework

- **NTA 2025 consolidation** — The Nigeria Tax Act (NTA) 2025, part of the suite of fiscal reforms enacted in 2025, consolidates Capital Gains Tax into the general income tax framework. Pre-2025 CGTA provisions remain operative for disposals during transitional periods, but for periods on or after the NTA commencement date: - CGT is administered alongside Companies Income Tax (CIT) and Personal Income Tax (PIT) under a unified return. - The 10% headline rate is retained for most asset classes (subject to confirmation in implementing regulations). - Treatment of share disposals, the ₦100M threshold, rollover relief, and exemptions is being re-codified — implementing regulations are pending as of the 2025 tax year. - Conservative default: until FIRS publishes the implementing regulations, prepare CGT computations under the pre-NTA CGTA framework and flag the position for review once the regulations are finalised.  _(Nigeria Tax Act (NTA) 2025)_

## Section 5 — Worked examples

### Example A — Sale of investment property (resident individual)

Mr Adewale, a Lagos-resident individual, sold a commercial property in Ikeja on 15 June 2025. The property was acquired in 2018.

**Example A computation table**

| Line item | Amount (₦) |
| --- | --- |
| Disposal proceeds | 250,000,000 |
| Less: Incidental costs of disposal (legal 1.5%, agent 5%) | (16,250,000) |
| Net proceeds | 233,750,000 |
| Less: Acquisition cost (2018) | (120,000,000) |
| Less: Incidental costs of acquisition (stamp duty, legal) | (6,000,000) |
| Less: Enhancement expenditure (extension, 2021) | (25,000,000) |
| **Chargeable gain** | **82,750,000** |
| CGT at 10% | **8,275,000** |

The CGT of ₦8,275,000 is reported alongside Mr Adewale's PIT return for 2025 to the Lagos State Internal Revenue Service. Routine repairs incurred over the holding period are NOT deductible.

### Example B — Sale of company shares (resident individual)

Mrs Okonkwo disposed of equity holdings during 2025 as follows:

**Example B disposals table**

| Disposal | Date | Proceeds (₦) | Cost (₦) |
| --- | --- | --- | --- |
| NGX-listed Co. A shares | March 2025 | 60,000,000 | 25,000,000 |
| NGX-listed Co. B shares | August 2025 | 85,000,000 | 40,000,000 |
| Unlisted Co. C shares | November 2025 | 40,000,000 | 30,000,000 |
| **Aggregate proceeds (12-month window)** |  | **185,000,000** |  |

Aggregate share-disposal proceeds in 2025 exceed ₦100M. The portion above the threshold is ₦85,000,000.

Mrs Okonkwo did not reinvest in any Nigerian company shares during 2025. The taxable portion of the gain is computed by apportioning the total chargeable gain to the residual proceeds above the threshold:

**Example B apportionment table**

| Line item | Amount (₦) |
| --- | --- |
| Total proceeds | 185,000,000 |
| Total cost basis | 95,000,000 |
| Total chargeable gain | 90,000,000 |
| Apportioned to residual above ₦100M (85,000,000 / 185,000,000 × 90,000,000) | 41,351,351 |
| CGT at 10% | **4,135,135** |

The CGT is reported with the 2025 PIT return. If Mrs Okonkwo had reinvested ≥ ₦85M into Nigerian shares within 2025, the residual gain would be exempt.

## Section 6 — Filing & payment

### 6.1 Resident individuals (PIT)

- **Resident individuals filing rules** — - CGT computation is appended to the annual Personal Income Tax (PIT) return filed with the relevant State Internal Revenue Service (SIRS) in the taxpayer's state of residence. - Filing deadline: 31 March following the end of the tax year (calendar-year basis), per Personal Income Tax Act (PITA) s. 41. - Payment: due on filing.  _(Personal Income Tax Act (PITA) s. 41)_

### 6.2 Resident companies (CIT)

- **Resident companies filing rules** — - CGT computation is appended to the annual Companies Income Tax (CIT) return filed with FIRS. - Filing deadline: 6 months after the end of the company's accounting year (Companies Income Tax Act s. 55). - Payment: due on filing; companies in their first 18 months may use the self-assessment provisions.  _(Companies Income Tax Act s. 55)_

### 6.3 Non-residents

- **Non-resident filing / withholding rules** — - 10% CGT applies on chargeable gains from Nigerian-situs assets (Nigerian land, Nigerian-incorporated company shares, Nigerian business assets). - For non-resident disposals of Nigerian real property or shares, the buyer / Nigerian payment agent may be required to withhold CGT and remit to FIRS. Confirm in each case whether withholding is mandated by current FIRS Information Circular. - Non-resident sellers should obtain a Tax Clearance Certificate (TCC) confirming CGT has been settled before perfecting title transfer.

### 6.4 Records & retention

- **Records retention rules** — - Retain acquisition contracts, valuation evidence, brokerage notes, and disposal contracts for 6 years from the end of the relevant tax year (general FIRS / SIRS retention rule). - Where rollover relief is claimed, retain documentation of the replacement asset acquisition for the life of the replacement asset plus 6 years.

## Section 7 — Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown acquisition cost | STOP — cannot compute gain |
| Acquisition by gift or inheritance with no valuation | Obtain probate / market valuation; if unavailable, STOP |
| Unknown whether the ₦100M share threshold is breached in aggregate | Assume breached → compute at 10% conservatively, refund position later if portfolio aggregation confirms exemption |
| Unknown whether reinvestment in Nigerian shares occurred within the tax year | Assume no reinvestment → tax the residual |
| Unknown whether parties are connected | Treat as connected → apply market value rule |
| Routine repair vs enhancement expenditure ambiguous | Treat as routine repair → NOT deductible |
| Disposal post NTA 2025 commencement, regulations pending | Compute under CGTA framework; flag for review under NTA implementing regulations |
| Cross-border disposal with possible treaty relief | STOP — refer to specialist treaty review |
| PPR claimed but property was let or had non-residential use | Restrict PPR proportionally; conservative default → no PPR |
| Non-resident disposal where withholding obligation unclear | Assume withholding applies; remit 10% to FIRS pending clarification |

## Section 8 — Sources

1. Capital Gains Tax Act (CGTA) Cap C1, Laws of the Federation of Nigeria 2004 — primary CGT statute.
2. Finance Act 2019 — amendments to CGTA (administrative provisions).
3. Finance Act 2020 — further administrative amendments and definitions.
4. Finance Act 2021 — introduced the ₦100M aggregate share-disposal threshold under CGTA s. 30 (formerly blanket exempt for shares).
5. Finance Act 2022 — clarifications to share-disposal mechanics.
6. Finance Act 2023 — further amendments.
7. Personal Income Tax Act (PITA) Cap P8, LFN 2004 (as amended) — return-filing framework for resident individuals.
8. Companies Income Tax Act (CITA) Cap C21, LFN 2004 (as amended) — return-filing framework for companies; CGT is administered alongside.
9. Nigeria Tax Act (NTA) 2025 — consolidates CGT into the unified income tax framework; implementing regulations pending as of skill publication.
10. FIRS Information Circulars on CGT — including circulars issued post Finance Act 2021 on the ₦100M share threshold and the reinvestment relief.
11. FIRS Information Circular on Tax Implications of Mergers and Acquisitions — relevant for share-disposal rollover and reorganisation reliefs.
12. CITN (Chartered Institute of Taxation of Nigeria) practice guidance — practitioner-level commentary on Finance Act and NTA 2025 changes.

## End of Skill — Nigeria CGT v1.0

End of Skill — Nigeria CGT v1.0

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
