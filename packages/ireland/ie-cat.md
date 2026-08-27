---
name: ie-cat
description: Use this skill whenever asked about Irish Capital Acquisitions Tax (CAT) on gifts and inheritances. Trigger on phrases like "Ireland CAT", "Irish inheritance tax", "Irish gift tax", "Group A Ireland", "Group B threshold Ireland", "Group C threshold Ireland", "Dwelling House Exemption", "Section 86 CATCA", "Business Relief Ireland", "Agricultural Relief Ireland", "active farmer test", "Form IT38", "valuation date Ireland", "small gift exemption €3,000", "CAT 33%", "aggregation rule CAT", "foreign gift Ireland", or any question about computing, filing, or reporting Irish CAT for a donee or beneficiary. Scope covers CAT computation under the Capital Acquisitions Tax Consolidation Act 2003 (CATCA 2003) as amended by successive Finance Acts, the three group thresholds (A/B/C), the cumulative aggregation rule back to 5 December 1991, the principal reliefs (Dwelling House, Business, Agricultural), foreign-element situs and residence rules, valuation date mechanics, and the Form IT38 pay-and-file obligation via ROS. ALWAYS read this skill before touching Irish CAT work.
jurisdiction: IE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IE Cat

## Section 1 — Quick reference

**Section 1 — Quick reference table**

| Field | Value |
| --- | --- |
| Country | Ireland (Republic of Ireland) |
| Tax | Capital Acquisitions Tax (CAT) — gift tax + inheritance tax in a single charge |
| Currency | EUR (€) |
| Primary legislation | Capital Acquisitions Tax Consolidation Act 2003 (CATCA 2003) |
| Amending legislation | Finance Acts (annual); most recent threshold uplift — Finance Act 2024 (Group A €335k → €400k; Group B €32,500 → €40,000; Group C €16,250 → €20,000) |
| Headline rate | **33%** on the taxable value of gifts and inheritances above the relevant group threshold |
| Cumulation start | 5 December 1991 (all prior benefits in the same group aggregate to determine remaining threshold) |
| Annual small gift exemption | **€3,000** per donor per donee per calendar year (non-cumulative; ignored for aggregation) |
| Tax authority | Office of the Revenue Commissioners |
| Filing | Form IT38 — filed by donee/beneficiary online via ROS (or IT38S short form where applicable) |
| Pay-and-file deadline | **31 October** following the year of the **valuation date** (valuation date between 1 Jan – 31 Aug → IT38 due 31 Oct same year; valuation date between 1 Sep – 31 Dec → IT38 due 31 Oct following year) |
| Validated by | Pending — requires sign-off by an Irish Chartered Tax Adviser (CTA) or Chartered Accountant (Chartered Accountants Ireland / ACCA Ireland) |
| Skill version | 1.0 |

### Group thresholds (2025 — Finance Act 2024 figures)

**Group thresholds (2025 — Finance Act 2024 figures)**

| Group | Relationship of donee to donor | Lifetime threshold (since 5 Dec 1991) |
| --- | --- | --- |
| **Group A** | Child receiving from parent (incl. step-child, adopted child, certain foster children, certain minor children of a deceased child taking from grandparent) | **€400,000** |
| **Group B** | Lineal ancestor / lineal descendant (other than Group A), brother, sister, child of a brother or sister (niece/nephew), parent receiving an inheritance from a child (gifts from child fall into Group A on parent in limited cases — see §3) | **€40,000** |
| **Group C** | Any relationship not in Group A or Group B (including cohabitant, friend, in-law, more distant relative) | **€20,000** |

### Rate at a glance

**Rate at a glance**

| Cumulative taxable benefit in group | Rate |
| --- | --- |
| Up to threshold | 0% |
| Above threshold | **33%** flat on excess |

## Section 2 — Required inputs & refusal catalogue

### Required inputs

Before computing any Irish CAT position, obtain:

1. **Identity of the donee/beneficiary** — name, PPSN, tax residence and ordinary residence status, domicile (for foreign-element analysis).
2. **Identity of the disponer (donor / deceased)** — name, PPSN if available, residence/ordinary-residence/domicile, and date of death (if inheritance).
3. **Date of the gift or inheritance** — for inheritances, the date of death; for gifts, the date the donee becomes beneficially entitled in possession.
4. **Valuation date** — for gifts, generally the date of the gift; for inheritances, the earliest of (a) the date the personal representative is entitled to retain the asset for the beneficiary, (b) the date the asset is so retained, or (c) the date the asset is delivered, paid over or transferred to the beneficiary (Section 30 CATCA).
5. **Description and market value of each asset at the valuation date** — open-market value, ignoring any restrictions imposed by the disponer.
6. **Liabilities, costs and expenses properly deductible** — funeral expenses, debts of the deceased, costs of administration attributable to the benefit.
7. **Relationship between disponer and donee** — to determine the group threshold.
8. **All prior gifts or inheritances received by the donee from any disponer within the same group since 5 December 1991** — required for cumulation.
9. **Whether any relief is claimed** — Dwelling House Exemption (s.86), Business Relief (ss.90–102), Agricultural Relief (ss.89), Favourite Nephew/Niece relief (s.27), surviving spouse/civil partner of a predeceased relative provisions, etc.
10. **Foreign element** — situs of each asset, residence/ordinary-residence of disponer at date of disposition and of donee at date of gift/inheritance.
11. **Whether any double-taxation treaty applies** — Ireland has CAT treaties with the **UK** and the **USA** only; unilateral credit under s.107 CATCA is available for other jurisdictions.

### Refusal catalogue — do NOT proceed; refer to a qualified Irish CTA

Refuse to issue a final IT38 position (escalate to a qualified Irish Chartered Tax Adviser) where any of the following apply:

- **Discretionary trust tax** (initial 6% charge + annual 1% charge under ss.15–22 CATCA) — specialised area; out of scope of v1.0.
- **Section 86 Dwelling House Exemption claims where the donee owns or has an interest in another dwelling at the date of the gift/inheritance** — anti-avoidance restrictions tightened by FA 2016 are nuanced.
- **Business Relief or Agricultural Relief clawback events** within the 6-year post-acquisition window.
- **The "active farmer" test under s.89(1A) CATCA** — requires either an agricultural qualification, 50% time test on the holding, or a long-term lease to a qualifying farmer; if the facts are unclear, refuse.
- **Foreign-domiciled donee or disponer** where the situs/residence test produces a mixed outcome (Irish-situs and foreign-situs assets in the same disposition).
- **Disclaimers, partial disclaimers and post-death deeds of variation** (s.12 CATCA) — interpretation depends on the precise wording and timing.
- **Limited interests, life interests, annuities, and successive interests** — actuarial valuation under Schedule 1 CATCA Tables A and B is required.
- **Free use of property, interest-free loans, and benefits derived from a private company** (ss.40, 43 CATCA) — deemed gift mechanics are fact-sensitive.
- **Discretionary trust appointments where the beneficiary is not yet absolutely entitled.**
- **Anti-avoidance: Section 811 / 811C TCA 1997 general anti-avoidance challenges** referred to CAT — refer.
- **Cross-border estates with assets in jurisdictions outside Ireland, UK and USA** where double-tax relief computation requires foreign-country probate valuation evidence.
- **The skill MUST NOT compute Irish probate tax, stamp duty on property transfers, or income tax on estate income** — those are separate skills.

If any item above is in play, state clearly: *"This matter falls outside the scope of skill ie-cat v1.0. A qualified Irish Chartered Tax Adviser must review and sign off."*

## Section 3 — Tier 1: Chargeable persons, chargeable benefit, valuation, group thresholds

### 3.1 Chargeable person

- **Chargeable person definition** — CAT is a **beneficiary-based tax**. The **donee** (gift recipient) or **successor / beneficiary** (inheritance recipient) — referred to collectively in CATCA 2003 as the "accountable person" — bears the tax. The disponer is **not** the chargeable person (contrast with UK Inheritance Tax, which is levied on the estate). A person is a chargeable person where **either**: - the **disponer** is resident or ordinarily resident in Ireland at the date of the disposition (date of gift / date of death for inheritances); **or** - the **donee** is resident or ordinarily resident in Ireland at the date of the gift / inheritance; **or** - the **asset is situated in Ireland** (Irish-situs asset rule — applies regardless of residence of either party). If none of those conditions is satisfied, the gift/inheritance is **outside the charge to Irish CAT**. > **Special non-domiciled rule (s.6(2)(d) and s.11(2)(d) CATCA):** a person who is not domiciled in Ireland is treated as resident or ordinarily resident for CAT purposes **only if** the person has been resident in Ireland for the **5 consecutive tax years immediately preceding** the year of the gift/inheritance, and is resident or ordinarily resident in Ireland on the date of the disposition. This is the "5-year rule" and shields recent arrivals.  _(s.6(2)(d), s.11(2)(d) CATCA)_

### 3.2 Chargeable benefit ("taxable value")

- **Taxable value computation steps** — The taxable value of a gift or inheritance is computed in three steps (s.28 CATCA): 1. **Incumbrance-free value** of the asset = market value at the valuation date − liabilities, costs and expenses properly payable out of the benefit. 2. **Less consideration paid by the donee** (if any) — full consideration in money or money's worth reduces taxable value €-for-€; partial consideration reduces proportionately. 3. **Less reliefs and exemptions** — Dwelling House Exemption (where the whole value is removed); Business Relief / Agricultural Relief (where 90% of the value is removed, leaving 10% in charge); annual small gift exemption (€3,000 per donor per calendar year). The result is the **taxable value** carried into the aggregation computation.  _(s.28 CATCA)_

### 3.3 Valuation

- **Valuation rules** — - **Open-market value** at the valuation date is the standard (s.26 CATCA) — the price the asset would fetch on a sale in the open market on that date, disregarding any restriction imposed by the disponer. - **Real property** — formal valuation by a qualified valuer is best practice; Revenue will challenge under-valuations and may issue a Notice of Revised Assessment. - **Unquoted shares** — net asset valuation, dividend yield basis, earnings basis, or a blend, depending on the size of the holding and the company's circumstances; informed by Revenue's Tax and Duty Manual Part 19. - **Quoted shares** — the lower of (a) the quarter-up rule on the closing bid/offer and (b) the mean of the two bargain prices on the valuation date. - **Limited interests (life interest, interest for a period of years)** — actuarial value from Schedule 1 CATCA Table A (life interests, by age and gender) or Table B (interests for a fixed period).  _(s.26 CATCA)_

### 3.4 Group thresholds and cumulation

- **Cumulation rule** — The **group threshold** is the lifetime tax-free amount available to the donee from disponers within that group, **cumulated since 5 December 1991**. **Cumulation rule (s.9 CATCA):** > Taxable value of current benefit + sum of taxable values of all prior benefits in the same group received since 5 Dec 1991 = aggregate taxable value. Compare aggregate to the **threshold in force at the date of the current benefit**. Tax at 33% applies to the excess. The threshold to apply is the **current** group threshold (i.e. the threshold at the date of the latest benefit), not the historical threshold at the date of each prior benefit. This is sometimes called the "indexation by reference to current threshold" mechanism. > **Double-aggregation point:** prior gifts received from a person in Group B do **not** aggregate with current inheritances from a person in Group A — aggregation operates **within the same group only**. However, prior gifts and prior inheritances from disponers in the **same group** aggregate together.  _(s.9 CATCA)_

### 3.5 Group A — special inclusions and traps

- **Group A special inclusions** — - **Step-children, adopted children, and certain foster children** (with 5+ years of care before age 18) qualify for Group A. - **Surviving spouse/civil partner of a predeceased child** can inherit at Group A from the parent-in-law (s.2 CATCA definition of "child" extended). - **Parent receiving an inheritance from a child** falls in **Group A** (not Group B) **only where** the child took the asset originally from that parent and the parent now inherits it back — otherwise Group B applies to a parent-from-child receipt. - **A parent receiving a gift (not an inheritance) from a child** is in **Group B**, not Group A.  _(s.2 CATCA)_

### 3.6 Spouse / civil partner exemption

- **Spouse/civil partner exemption** — Gifts and inheritances between spouses or civil partners are **wholly exempt** from CAT (s.70 and s.71 CATCA). They are also ignored for aggregation purposes. **Cohabitants are not exempt** — they fall in Group C.  _(s.70, s.71 CATCA)_

### 3.7 Small gift exemption

- **Small gift exemption details** — The first **€3,000** received by a donee from each disponer in each calendar year is exempt (s.69 CATCA). This exemption: - Applies **per donor**, **per donee**, **per calendar year**. - Is available for **gifts only** — not inheritances. - Is **ignored for aggregation** — does not reduce the group threshold. - Allows planned annual transfers (e.g. €3,000 × 2 parents × 2 children = €12,000 per year tax-free and outside the cumulation).  _(s.69 CATCA)_

## Section 4 — Tier 2: Principal reliefs and foreign element

### 4.1 Dwelling House Exemption — s.86 CATCA

- **Dwelling House Exemption conditions** — Where the conditions are met, the gift or inheritance of a dwelling house is **wholly exempt** from CAT — i.e. the value of the dwelling is excluded entirely. **Conditions (post-Finance Act 2016 — significantly tightened):** 1. The dwelling was the **disponer's principal private residence** at the date of death (inheritance only — gifts of dwellings are now exempt **only** to a "dependent relative" — see (1A)). 2. The donee **occupied the dwelling as his/her only or main residence for the 3 years immediately before** the date of the inheritance. 3. The donee **must not be beneficially entitled to any other dwelling** (or interest in any other dwelling) **at the date of the inheritance**. 4. The donee must **continue to occupy the dwelling as his/her only or main residence for 6 years after** the date of the inheritance (with a relaxation for donees aged 65+ at the date of the inheritance, and for donees who are required to leave for reasons of employment or ill-health). **(1A) Gifts:** Since FA 2016, a dwelling house gift qualifies only where the donee is a **"dependent relative"** of the disponer — i.e. a relative who is permanently and totally incapacitated by physical or mental infirmity from maintaining himself/herself, or who is aged 65 or over. **Clawback:** if the donee disposes of the dwelling or ceases to occupy it within the 6-year window, the exemption is clawed back (with relief for replacement dwellings on a reasonable basis).  _(s.86 CATCA)_

### 4.2 Business Relief — ss.90–102 CATCA

- **Business Relief details** — A **90% reduction** in the taxable value of "relevant business property" passed by gift or inheritance. **Qualifying property:** - A business or interest in a business carried on for gain. - Unquoted shares giving the donee control (>25% voting, or any holding where the disponer had >25% before transfer) of a company carrying on a qualifying business. - Land, buildings, machinery and plant used wholly or mainly for the purposes of the business. **Excluded businesses:** dealing in shares, securities, land, or buildings; making or holding investments. The "wholly or mainly" test is applied on a value-of-assets basis. **Ownership period:** the disponer must have owned the property for a **minimum continuous period before the transfer**: - **5 years** for a gift, or - **2 years** for an inheritance. **Clawback (s.101 CATCA):** if the donee disposes of the business or shares (or the company ceases trading) within **6 years** of the transfer, the relief is wholly or partly clawed back. Replacement property within 1 year preserves relief in proportion. > **Refusal point:** if a clawback event has occurred or is likely within the 6-year window, refer to a qualified Irish CTA.  _(ss.90–102 CATCA, s.101 CATCA)_

### 4.3 Agricultural Relief — s.89 CATCA

- **Agricultural Relief details** — A **90% reduction** in the taxable value of "agricultural property" passed to a "farmer" by gift or inheritance. **"Agricultural property"** = agricultural land in Ireland, EU, UK, or EEA, together with crops, trees, underwood, farm buildings, dwelling houses appropriate to the property, livestock, bloodstock, and farm machinery. **"Farmer" test (s.89(1) CATCA):** after taking the gift/inheritance, at least **80% of the donee's gross property value** must consist of agricultural property. Liabilities are netted against non-agricultural property first for this test (s.89(2)). **"Active farmer" test (s.89(1A) CATCA — added by FA 2014, in force from 1 Jan 2015):** in addition to the 80% farmer test, the donee must, for **at least 6 years** after the valuation date, **either**: (a) hold a relevant **agricultural qualification** (Teagasc Green Cert or equivalent — listed in Schedule 2 of s.667B TCA 1997), and farm the land on a commercial basis for at least 50% of his/her normal working time; **or** (b) farm the land on a commercial basis for at least **50% of his/her normal working time**; **or** (c) **lease** the land for a minimum of 6 years to a person who meets (a) or (b). > **Refusal point:** if any uncertainty exists as to whether the donee meets the active farmer test, refer to a qualified Irish CTA. Misapplication leads to a full clawback at 33% on the relieved value. **Clawback:** disposal of agricultural property within **6 years** of the valuation date results in clawback unless the proceeds are reinvested in qualifying agricultural property within 1 year (6 years for compulsory acquisition).  _(s.89, s.89(1), s.89(1A), s.89(2) CATCA)_

### 4.4 Double aggregation — gifts taken back

- **Anti-avoidance on gifts taken back** — Where the same property is gifted by Person X to Person Y, and Person Y later transfers (whether back to X, or onward) within 3 years of the original transfer, anti-avoidance provisions in CATCA may treat the property as if X had made the disposition directly to the ultimate donee. This guards against threshold-stacking via intermediate transfers.

### 4.5 Foreign element — situs, residence, treaty relief

#### 4.5.1 Charging conditions (recap)

- **Charging conditions recap** — Irish CAT applies where **any** of the following is true at the date of the disposition: - The **disponer** is resident or ordinarily resident in Ireland. - The **donee** is resident or ordinarily resident in Ireland. - The **asset is Irish-situs** (regardless of residence of either party).

#### 4.5.2 Situs rules (common assets)

**Situs rules (common assets)**

| Asset | Irish-situs if … |
| --- | --- |
| Real property | Located in Ireland |
| Tangible movable property | Physically in Ireland at valuation date |
| Bank account | Branch is in Ireland |
| Registered shares | Company's share register is in Ireland |
| Bearer instruments | Located in Ireland |
| Debts (simple contract) | Debtor is resident in Ireland |
| Goodwill of a business | Business is carried on in Ireland |
| Life policy | Proper law of the contract; in practice, with Irish insurer |

#### 4.5.3 Foreign-domiciled persons — the 5-year rule (recap)

- **5-year rule recap** — A non-Irish-domiciled person is treated as resident/ordinarily resident for CAT only if resident for **5 consecutive tax years immediately preceding** the disposition year and resident/ordinarily resident on the disposition date.

#### 4.5.4 Foreign tax on the same gift/inheritance

- **Foreign tax credit / treaty rules** — - **Ireland–UK CAT Treaty** (1977): allocates primary taxing rights by domicile of the disponer, with credit relief. Important for estates with UK and Irish assets. - **Ireland–USA Estate Tax Treaty** (1949, modified 1951): covers federal estate tax; gift tax is **not** within the treaty. - **Unilateral credit (s.107 CATCA):** for any other country, where foreign tax of a similar character has been paid on the same property, a credit against Irish CAT is allowed up to the lower of (a) the foreign tax paid and (b) the Irish CAT attributable to the same property.  _(s.107 CATCA)_

### 4.6 Favourite nephew / niece relief — s.27 CATCA

- **Favourite nephew/niece relief** — A nephew or niece who has worked **substantially full-time** for the disponer in a business for the **5 years immediately before** the gift or inheritance may be treated as a **Group A** beneficiary in respect of business assets only. "Substantially full-time" = ≥ 24 hours per week, or ≥ 15 hours per week where the business is run by the disponer and the disponer's spouse with no other full-time employees.  _(s.27 CATCA)_

## Section 5 — Worked examples

### Example 5.1 — Child receives €800,000 inheritance from parent (Group A)

**Facts:** Aoife inherits €800,000 in cash from her father Seán on his death in March 2025. Aoife is Irish-resident and domiciled. She has previously received one gift in the same group: €60,000 from her mother in 2018 (no relief claimed at the time; threshold remaining was reduced by €60,000 of taxable value). The valuation date is 1 June 2025 (the date the executor transfers the cash to Aoife).

**Step 1 — Identify the group threshold (2025):** Group A = €400,000.

**Step 2 — Compute taxable value of current benefit:**

**Step 2 — Taxable value of current benefit**

| Item | € |
| --- | --- |
| Market value at valuation date | 800,000 |
| Less liabilities/expenses payable from the benefit | 0 |
| Less consideration paid by donee | 0 |
| Less applicable reliefs (none — cash) | 0 |
| **Taxable value of current benefit** | **800,000** |

**Step 3 — Cumulate prior Group A benefits since 5 Dec 1991:**

**Step 3 — Cumulation table**

| Date | Disponer | Group | Taxable value |
| --- | --- | --- | --- |
| 2018 | Mother | A | 60,000 |
| 2025 (current) | Father | A | 800,000 |
| **Aggregate Group A** |  |  | **860,000** |

**Step 4 — Apply 2025 threshold and compute tax:**

**Step 4 — Tax computation table**

| Computation | € |
| --- | --- |
| Aggregate taxable value | 860,000 |
| Group A threshold (2025) | (400,000) |
| Excess subject to CAT | 460,000 |
| CAT at 33% | **151,800** |

**Step 5 — Less tax (if any) previously paid on prior benefits:** the 2018 gift was within the then-threshold, so no prior CAT was paid; no credit to offset.

**CAT payable on the current inheritance: €151,800.**

**Filing:** valuation date 1 June 2025 → IT38 due **31 October 2025** via ROS.

### Example 5.2 — Sibling gift of €100,000 (Group B)

**Facts:** Niamh gifts €100,000 cash to her brother Cillian in July 2025. Cillian has received no prior Group B benefits. Both are Irish-resident and domiciled.

**Step 1 — Group threshold (2025):** Group B = €40,000.

**Step 2 — Small gift exemption:** the first €3,000 is exempt (s.69).

**Step 3 — Taxable value of current benefit:**

**Step 3 — Taxable value of current benefit**

| Item | € |
| --- | --- |
| Market value | 100,000 |
| Less small gift exemption | (3,000) |
| **Taxable value of current benefit** | **97,000** |

**Step 4 — Cumulate prior Group B benefits since 5 Dec 1991:**

**Step 4 — Cumulation table**

| Date | Disponer | Group | Taxable value |
| --- | --- | --- | --- |
| 2025 (current) | Niamh | B | 97,000 |
| **Aggregate Group B** |  |  | **97,000** |

**Step 5 — Apply threshold and compute tax:**

**Step 5 — Tax computation table**

| Computation | € |
| --- | --- |
| Aggregate taxable value | 97,000 |
| Group B threshold (2025) | (40,000) |
| Excess subject to CAT | 57,000 |
| CAT at 33% | **18,810** |

**CAT payable: €18,810.**

**Filing:** valuation date = date of gift (July 2025) → IT38 due **31 October 2025** via ROS. Cillian is the accountable person; Niamh has no Irish CAT liability (she may have foreign gift-tax implications if non-Irish — out of scope).

> **Threshold trigger rule:** the obligation to file Form IT38 arises whenever the aggregate taxable value in the group exceeds **80%** of the group threshold (s.46 CATCA), even if no tax is ultimately payable. For Group B in 2025, the 80% trigger is **€32,000**.

## Section 6 — Filing and payment — Form IT38

### 6.1 Who files

- **Who files IT38** — The **donee/beneficiary** (accountable person) files. Joint donees (e.g. siblings inheriting a property jointly) each file their own IT38 in respect of their respective interest.

### 6.2 Form variants

- **IT38 vs IT38S form variants** — - **Form IT38** — full form, mandatory where reliefs are claimed (Dwelling House, Business, Agricultural, Favourite Nephew, etc.), where prior benefits aggregate, or where the benefit includes non-cash assets requiring valuation. - **Form IT38S** — short form, available only where the benefit is wholly in cash, no reliefs are claimed, the donee is Irish-resident, and there are no prior benefits in the same group. Most cases require IT38, not IT38S.

### 6.3 When the obligation to file arises

- **Filing obligation rule** — A donee must file an IT38 where the **aggregate taxable value in the group (after the current benefit) exceeds 80% of the relevant group threshold** (s.46 CATCA). This is independent of whether tax is payable — the filing obligation is triggered by the 80% test.  _(s.46 CATCA)_

**80% triggers (2025)**  _(s.46 CATCA)_

| Group | 80% trigger |
| --- | --- |
| A | €320,000 |
| B | €32,000 |
| C | €16,000 |

### 6.4 Valuation date and payment date

- **Pay-and-file deadline rule** — The **pay-and-file deadline** is **31 October** following the year in which the valuation date falls **only if** the valuation date is between **1 January and 31 August**. Where the valuation date is between **1 September and 31 December**, the pay-and-file deadline is **31 October of the following year**.

**Valuation date / IT38 due table**

| Valuation date | IT38 due |
| --- | --- |
| 1 Jan 2025 – 31 Aug 2025 | 31 October 2025 |
| 1 Sep 2025 – 31 Dec 2025 | 31 October 2026 |

### 6.5 ROS filing mechanics

- **ROS filing mechanics** — - IT38 is filed **online via ROS** (Revenue Online Service). Paper IT38 is no longer accepted for most cases. - The accountable person must have an active **PPSN** and ROS access (or file via a registered agent). - Payment is made via ROS Debit Instruction, bank transfer, or card payment. - A **statement of affairs** (assets, liabilities, prior benefits) accompanies the return.

### 6.6 Interest and penalties

- **Interest and penalty rates** — - **Interest on late payment**: charged daily at the statutory rate (currently 0.0219% per day ≈ 8% p.a.). - **Surcharge on late filing**: - **5% of tax** (capped at €12,695) if filed within 2 months of the deadline. - **10% of tax** (capped at €63,485) if filed more than 2 months late. - **Penalty for fraudulent or negligent return**: up to 100% of the tax under-declared, plus prosecution risk for serious cases.

### 6.7 Self-assessment

- **Self-assessment and Revenue review window** — CAT is a **full self-assessment** tax. Revenue may select an IT38 for compliance intervention up to 4 years after filing (or with no time limit in the case of fraud or neglect).

## Section 7 — Conservative defaults

When information is incomplete and a position must still be taken for planning purposes (subject to reviewer sign-off), apply these defaults:

1. **Assume Group C threshold** where the relationship cannot be verified — most conservative.
2. **Assume no reliefs apply** (no Dwelling House, no Business, no Agricultural) until the qualifying conditions are documented and the 6-year holding window is committed to in writing.
3. **Assume valuation date = date of gift / date of death** unless the executor has formally confirmed a later valuation date.
4. **Assume prior benefits exhaust the threshold** — i.e. start the computation as if the current benefit is the marginal excess at 33%, until the donee has signed a statutory declaration of prior benefits.
5. **Assume no double-tax treaty applies** unless the relevant treaty (UK or USA) is explicitly invoked and the foreign tax is documented by a foreign assessment.
6. **Assume the donee is resident/ordinarily resident in Ireland** at the date of the gift/inheritance unless evidence of non-residence is provided.
7. **Assume the 5-year non-domiciled rule applies** — i.e. a non-domiciled donee who has been in Ireland 5+ tax years is treated as resident for CAT.
8. **Assume Dwelling House Exemption is denied** if the donee owns or has any beneficial interest in any other dwelling at the date of the gift/inheritance.
9. **Assume Agricultural Relief is denied** if the active farmer test (s.89(1A)) cannot be evidenced by a Teagasc Green Cert, time-test records, or a registered long-term lease.
10. **Assume IT38 (not IT38S)** is required wherever any non-cash asset, relief claim, or prior benefit is in play.
11. **Always recommend a formal valuation** by a qualified valuer for any real property, unquoted shares, or chattels above €5,000.
12. **Always recommend that the donee retain documentation** of all prior gifts received since 5 Dec 1991 for the lifetime of the donee.
13. **Always flag the 80% filing trigger** to the donee even where no tax is payable.

## Section 8 — Sources

### Primary legislation

- **Capital Acquisitions Tax Consolidation Act 2003** (CATCA 2003) — the consolidating statute, replacing the Capital Acquisitions Tax Act 1976.
- **Finance Act 2024** — Group A €335,000 → €400,000; Group B €32,500 → €40,000; Group C €16,250 → €20,000 (effective for gifts/inheritances on or after 2 October 2024).
- **Finance Act 2016** — Dwelling House Exemption tightened: gifts of dwellings restricted to "dependent relatives"; donee must not own any other dwelling at the date of the inheritance.
- **Finance Act 2014** — introduction of the "active farmer" test for Agricultural Relief (s.89(1A) CATCA, in force 1 January 2015).
- **Finance (No. 2) Act 2008** — rate increased from 20% to 22%; subsequent Finance Acts brought the rate to 25% (2009), 30% (2011), and 33% (2012 — current).

### Key sections of CATCA 2003 referenced in this skill

**Key sections of CATCA 2003 table**

| Section | Subject |
| --- | --- |
| s.6, s.11 | Charge to gift tax / inheritance tax; resident/ordinarily resident rules |
| s.9 | Aggregation of prior benefits in the same group |
| s.26 | Market value at valuation date |
| s.27 | Favourite nephew / niece relief |
| s.28 | Computation of taxable value |
| s.30 | Valuation date for inheritances |
| s.40, s.43 | Free use of property; benefits from a private company |
| s.46 | Obligation to file IT38 (80% threshold trigger) |
| s.69 | Small gift exemption (€3,000) |
| s.70, s.71 | Spouse / civil partner exemption |
| s.86 | Dwelling House Exemption |
| s.89, s.89(1A) | Agricultural Relief; active farmer test |
| ss.90–102 | Business Relief |
| s.101 | Business Relief clawback |
| s.107 | Unilateral credit for foreign tax |

### Treaties

- **Ireland / United Kingdom Convention for the Avoidance of Double Taxation in respect of Estate Duties** (signed 14 April 1977; entered into force 5 March 1978) — extended in practice to CAT.
- **Ireland / United States Convention for the Avoidance of Double Taxation in respect of Estate Taxes** (signed 13 September 1949; modified 1951).

### Revenue Commissioners published guidance

- **CAT — A Guide** (Revenue Tax and Duty Manual, Part 19).
- **Revenue eBrief** on annual threshold changes — most recently confirming the Finance Act 2024 uplifts.
- **CAT Manual Part 11** — Agricultural Relief; the active farmer test interpretation.
- **CAT Manual Part 12** — Business Relief; qualifying business property and clawback events.
- **CAT Manual Part 24** — Dwelling House Exemption.
- **Schedule 1 CATCA — Tables A and B** — actuarial factors for limited interests.

### Sign-off requirement

This skill output requires sign-off by a qualified Irish Chartered Tax Adviser (CTA, Irish Tax Institute) or a Chartered Accountant (Chartered Accountants Ireland, ACCA Ireland, or CPA Ireland) with CAT competence before being relied on by a taxpayer or filed with Revenue. The `verified_by` frontmatter remains **pending** until a credentialed reviewer signs off.

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
