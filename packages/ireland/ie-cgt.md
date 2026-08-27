---
name: ie-cgt
description: ALWAYS read this skill before touching any Irish Capital Gains Tax work. Trigger on phrases like "Ireland CGT", "33% capital gains Ireland", "PPR exemption Ireland", "Entrepreneur Relief Ireland", "CG50 clearance", "Irish Capital Gains Tax", "Form CG1", "preliminary CGT Ireland", "Retirement Relief Ireland", "Section 597AA", "Section 598", "Section 599", "Revenue Online Service CGT", "ROS CGT", "Irish share disposal tax", "Euronext Dublin share sale CGT", "Irish property gain", "non-resident CGT Ireland", "Irish-situs CGT", "crypto CGT Ireland", or any question about computing, filing, or reporting capital gains on Irish chargeable assets. Scope covers CGT computation for chargeable assets (real property, shares, business assets, crypto, intangibles), the Principal Private Residence relief, Entrepreneur Relief (Section 597AA), Retirement Relief (Sections 598/599), the annual exemption, the CG50 clearance regime for high-value land disposals, loss relief, and the preliminary-CGT / final-return mechanics under Form CG1 via ROS. ALWAYS read this skill before producing any Irish CGT figure.
jurisdiction: IE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IE Cgt

## Section 1 — Quick reference

**Section 1 — Quick reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Ireland |
| Tax | Capital Gains Tax (CGT) |
| Currency | EUR (€) |
| Tax year | 1 January to 31 December (calendar year) |
| Primary legislation | Taxes Consolidation Act (TCA) 1997, Parts 19–21 |
| Headline rate | **33%** on chargeable gains (raised from 30% in Budget 2013; previously 25%, 20%, 22%) |
| Entrepreneur Relief rate | **10%** on first €1,000,000 lifetime of qualifying business asset disposals (TCA 1997 s. 597AA) |
| Annual exemption | **€1,270** per individual per tax year (non-transferable between spouses) |
| Tax authority | Office of the Revenue Commissioners ("Revenue") |
| Filing | Form **CG1** (CGT-only filers) or **Form 11 / Form 11S** self-assessment return for self-employed |
| E-filing | Revenue Online Service (**ROS**) — mandatory for most filers |
| Validated by | Pending — requires sign-off by an Irish chartered tax adviser (CTA, AITI) or chartered accountant (CAI / ACCA / CPA Ireland) |
| Skill version | 1.0 |

### CGT rate at a glance

**CGT rate at a glance table**

| Asset class / scenario | Rate | Notes |
| --- | --- | --- |
| Standard chargeable gains (property, shares, crypto, intangibles) | **33%** | Single headline rate since 6 December 2012 |
| Qualifying business asset disposal — Entrepreneur Relief | **10%** | First €1M lifetime cap (TCA s. 597AA) |
| Foreign life policies, certain offshore funds | 40% | Higher rate under TCA Part 27 — out of scope of this skill |
| Principal Private Residence (PPR) — fully occupied throughout ownership | 0% | TCA s. 604 — full exemption |
| Disposal of land/buildings/minerals > €500,000 — no CG50 | Buyer withholds 15% on account | Refunded once seller's CGT liability assessed |
| Non-resident disposing of Irish-situs land, mineral rights, or unquoted shares deriving value from Irish land | 33% | Limited Irish CGT scope for non-residents (TCA s. 29) |

## Section 2 — Required inputs & refusal catalogue

### Required inputs

- **Required inputs before computing Irish CGT** — Before computing any Irish CGT position, obtain: 1. Identity & residency — taxpayer name, PPSN (or tax reference), residency status (Irish resident, ordinarily resident, domiciled / non-domiciled, non-resident). 2. Asset description — class (real property, shares, business asset, crypto, intangible, chattel) and whether Irish-situs. 3. Acquisition data — acquisition date, acquisition cost (with documentary support), incidental costs of acquisition (legal, stamp duty, survey). 4. Disposal data — disposal date, disposal proceeds (gross), incidental costs of disposal (solicitor, agent's commission, advertising). 5. Connection — whether the parties are connected persons (market value rule applies under TCA s. 549). 6. For PPR claims — full timeline of occupation, any periods of letting or non-residential use, whether the property exceeded one acre, whether business use occurred. 7. For Entrepreneur Relief — proof of working director / employee role, 5%+ ordinary share capital, continuous holding for ≥ 3 years, qualifying trading activity. 8. For Retirement Relief — taxpayer age (≥ 55), ownership period (≥ 10 years), nature of disposal (third party vs family), aggregate prior Retirement Relief claims. 9. For shares — pooling / FIFO treatment under TCA s. 581 (Irish identification rules); rights issues, bonus issues, and corporate-action history. 10. Indexation — for assets acquired on or before 31 December 2002, the year of acquisition (indexation factor frozen at 2003 levels). 11. Prior-year losses — capital losses brought forward (capital losses ring-fenced from income). 12. CG50 status — for disposals > €500,000 of land/buildings/minerals, whether a CG50 clearance certificate has been obtained.  _(TCA s. 549)_

### Refusal catalogue

**Refusal catalogue table**

| Trigger | Reason |
| --- | --- |
| Acquisition cost unknown or undocumented | Cannot compute chargeable gain; do not estimate without reviewer sign-off |
| Asset acquired by gift / inheritance with no probate / CAT valuation | Need market-value documentation for base cost (TCA s. 547) |
| Non-domiciled resident on remittance basis with foreign-asset gains | Remittance-basis CGT mechanics require specialist review |
| Disposal of partnership interests | Partnership-CGT mechanics under TCA s. 1008 require specialist input |
| Trust / settlement disposals | Specialist trust-CGT regime (TCA Part 19 Ch. 5) — out of scope |
| Disposal of foreign life policies / offshore funds (taxable at 40%) | Specialist gross-roll-up regime — out of scope |
| Reorganisations, mergers, or s. 615/s. 631 reconstructions | Specialist corporate-restructuring CGT reliefs — out of scope |
| Cross-border disposal where double-tax-treaty relief may apply | Requires bilateral treaty analysis — out of scope |
| Development land disposals (TCA s. 648 et seq.) | Specialist development-land CGT rules — out of scope |
| PPR claimed but property was let, used as office, or exceeded 1 acre with garden | Apportionment required — escalate to reviewer |
| Entrepreneur Relief claimed without complete 3-year holding evidence | Cannot confirm s. 597AA eligibility |
| Retirement Relief where prior claims may exceed lifetime threshold | Aggregate threshold check required |
| Disposal > €500,000 of land/buildings without CG50 clearance | Confirm 15% withholding mechanics before completing |

## Section 3 — Tier 1 — chargeable persons, chargeable assets, computation

### 3.1 Chargeable persons (TCA s. 28, s. 29)

- **Chargeable persons** — CGT is charged on the chargeable gains accruing to: A resident or ordinarily resident individual — on worldwide chargeable assets, subject to the remittance basis where non-domiciled (gains on foreign assets taxed only on remittance to Ireland). A resident company — generally within the corporation tax framework, but disposals of certain assets (notably development land) remain within CGT. A non-resident person — on Irish-specified assets only: land and buildings in Ireland, mineral rights and exploration rights in the Irish State or Continental Shelf, unquoted shares deriving the greater part of their value from Irish land or mineral rights, and assets used for the purposes of a trade carried on in Ireland through a branch or agency.  _(TCA s. 28, s. 29)_

### 3.2 Chargeable assets (TCA s. 532)

- **Chargeable assets** — All forms of property are chargeable assets, including: Land and buildings (Irish and foreign, for residents). Shares and securities of any company. Goodwill and other intangible business assets. Options, debts (subject to TCA s. 541), and incorporeal property. Currency other than the euro. Crypto-assets — Revenue treats crypto as a chargeable asset for CGT (no specific carve-out). Chattels — but with exemptions for tangible movable property sold for ≤ €2,540 (TCA s. 602) and for wasting chattels under TCA s. 603.  _(TCA s. 532)_

### 3.3 Computation formula

- **Chargeable gain computation formula** — Chargeable gain = Disposal proceeds − Incidental costs of disposal − (Allowable acquisition cost + Incidental costs of acquisition + Enhancement expenditure). Where indexation applies (pre-2003 acquisitions only), the acquisition cost and enhancement expenditure incurred up to 31 December 2002 are multiplied by the relevant statutory indexation factor frozen at 2003 levels. Annual CGT computation: 1. Compute the chargeable gain on each disposal in the tax year. 2. Aggregate gains; deduct allowable losses (current-year first, then losses brought forward). 3. Deduct the annual exemption of €1,270 (non-transferable between spouses). 4. Apply the 33% rate (or 10% Entrepreneur Relief rate on qualifying portion).

### 3.4 Allowable deductions (TCA s. 552)

- **Allowable deductions** — Original acquisition cost. Incidental costs of acquisition (solicitor's fees, stamp duty, surveyor, auctioneer). Enhancement expenditure reflected in the state of the asset at disposal — routine repairs and revenue expenditure are NOT allowable. Incidental costs of disposal (solicitor, auctioneer, advertising, valuation). Costs of establishing, preserving, or defending title to the asset.  _(TCA s. 552)_

### 3.5 Connected persons rule (TCA s. 549)

- **Connected persons market value rule** — Where the disposal is between connected persons (spouses, relatives, group companies, partners), the transaction is deemed to be at market value, regardless of the stated consideration. Spousal transfers in particular are normally on a no-gain/no-loss basis (TCA s. 1028) provided both spouses are resident.  _(TCA s. 549; TCA s. 1028)_

### 3.6 Capital losses (TCA s. 31, s. 546)

- **Capital losses treatment** — Capital losses are ring-fenced — they may be set against current-year capital gains only, not against income. Losses unused in the current year may be carried forward indefinitely against future capital gains of the same person. Losses on disposals to connected persons are clogged — usable only against future gains on disposals to that same connected person. Losses cannot be carried back, except on death (TCA s. 573).  _(TCA s. 31, s. 546, s. 573)_

## Section 4 — Tier 2 — PPR exemption, Entrepreneur Relief, Retirement Relief, indexation, losses

### 4.1 Principal Private Residence (PPR) relief (TCA s. 604)

- **PPR relief full exemption and apportionment** — Full CGT exemption on the disposal of an individual's sole or main residence (including a garden / grounds up to one acre, excluding the site of the house) where the property has been occupied as the only or main residence throughout the period of ownership. Apportionment. Where the property was not occupied as the PPR throughout ownership, the gain is apportioned as follows: Exempt gain = Total gain × (Period of qualifying occupation + Final 12 months) / Total period of ownership. The last 12 months of ownership are always treated as qualifying occupation, provided the property has been the PPR at some point. Permitted absences that count as qualifying occupation: Any period(s) of absence totalling up to 3 years for any reason. Any period(s) of employment abroad (no time limit). Any period(s) of absence up to 4 years due to work elsewhere in Ireland. Restrictions to PPR: Garden / grounds in excess of one acre — apportionment required. Periods where the property was let (other than rent-a-room qualifying letting) — non-qualifying. Business use of part of the property — apportionment required. Acquired or developed wholly or partly for the purpose of realising a gain — relief may be denied.  _(TCA s. 604)_

### 4.2 Entrepreneur Relief — Section 597AA TCA 1997

- **Entrepreneur Relief rate and conditions** — A reduced CGT rate of 10% applies on qualifying disposals of business assets, subject to a lifetime limit of €1,000,000 (raised from €500,000 by Finance Act 2016, effective 1 January 2017). Qualifying conditions: Individual disposing of chargeable business assets. For shares: must own ≥ 5% of the ordinary share capital of the qualifying company. Held for a continuous period of at least 3 years ending on the disposal date. Individual must have been a working director or employee (devoting ≥ 50% of working time) for the 3 years. Qualifying business must be a trading company (not investment, dealing in shares, dealing in land/development, certain professional services). Mechanics: Gain on the qualifying disposal is charged at 10% up to the cumulative €1M lifetime cap; the excess (and any non-qualifying disposals) is charged at the standard 33% rate.  _(TCA 1997 s. 597AA)_

### 4.3 Retirement Relief — Sections 598 & 599 TCA 1997

- **Retirement Relief conditions and strands** — Despite the name, the taxpayer does not need to retire — the relief applies on disposals of qualifying business or farming assets by individuals aged 55 or over. Common conditions: Individual aged ≥ 55 at the date of disposal. Disposal of qualifying business assets or shares in a qualifying family company where the individual was a working director for ≥ 10 years (and full-time working director for ≥ 5 years). The assets / shares must have been owned for ≥ 10 years. For farms, the land must have been owned and farmed for ≥ 10 years. Two strands: TCA s. 598 — disposals to third parties (outside the family): Full relief where aggregate consideration ≤ €750,000 (reduced to €500,000 if the individual is aged 66 or over). Marginal relief tapered above the threshold. TCA s. 599 — disposals to a child (or qualifying nephew/niece): Full relief on transfers to a child where the disponer is aged 55–65, with no upper consideration limit historically, BUT a cap of €3M applies where the disponer is aged 66 or over (Finance Act 2014). "Child" includes a foster child meeting statutory conditions, and certain nephews/nieces working in the business. Clawback of relief may arise where the child disposes of the asset within 6 years.  _(TCA 1997 s. 598, s. 599; Finance Act 2014)_

### 4.4 Indexation relief (TCA s. 556) — largely abolished

- **Indexation relief mechanics** — Indexation relief allows the acquisition cost (and pre-2003 enhancement expenditure) of an asset to be uplifted by reference to inflation between the year of acquisition and the year of disposal. Key restrictions: Indexation is frozen at 2003 values. No indexation factor accrues for any period after 31 December 2002. For assets acquired on or after 1 January 2003, no indexation is available. For assets acquired on or before 31 December 2002, the indexation factor is the statutory multiplier published by Revenue for the year of acquisition, applied to the cost and to any enhancement expenditure incurred up to 31 December 2002. Practical consequence: indexation is encountered only on legacy holdings (typically pre-2003 property or shares).  _(TCA s. 556)_

### 4.5 Losses (TCA s. 31, s. 546, s. 573)

- **Losses treatment detail** — Current-year losses set against current-year gains before the annual exemption. Unused losses carried forward indefinitely. Losses on disposals to connected persons clogged. Losses on the disposal of development land restricted (development-land regime). Losses on death — unused losses cannot be transferred to the estate, but losses incurred in the year of death may be carried back up to 3 years (TCA s. 573).  _(TCA s. 31, s. 546, s. 573)_

### 4.6 Other reliefs in scope

- **Other reliefs list** — Annual exemption — €1,270 per individual per tax year, non-transferable between spouses. Spousal transfer — no gain / no loss (TCA s. 1028). Disposal of a site to a child for the construction of the child's PPR — exempt up to market value of €500,000 (TCA s. 603A). Wasting chattels (life ≤ 50 years) — exempt under TCA s. 603 (subject to business-use carve-out). Government securities, certain life policies, certain pension lump sums — exempt.  _(TCA s. 1028, s. 603A, s. 603)_

### 4.7 CG50 clearance — TCA s. 980

- **CG50 withholding mechanics** — Where the consideration on a disposal exceeds €500,000 for land, buildings, mineral rights, exploration rights, unquoted shares deriving the greater part of their value from Irish land/minerals, or goodwill of a trade in Ireland, the purchaser is obliged to withhold 15% of the consideration and remit it to Revenue on account of the vendor's CGT liability — UNLESS the vendor produces a CG50A clearance certificate. For disposals of residential property, the threshold is €1,000,000 (TCA s. 980(8)). A CG50A is issued by Revenue on application (Form CG50) by the vendor where the vendor is either Irish-resident, has no outstanding CGT liability, or has paid (or made arrangements to pay) the CGT on the disposal. Without the CG50A, the buyer's withheld 15% is credited against the vendor's final CGT bill — but creates a cashflow drag and reflects poorly on conveyancing practice.  _(TCA s. 980, s. 980(8))_

## Section 5 — Worked examples

### Example A — Disposal of Euronext Dublin (ISEQ) listed shares

Facts. Mr Ó Briain, an Irish resident individual, disposed of 5,000 shares in an Irish PLC listed on Euronext Dublin on 12 May 2025. He had acquired them in two tranches: 3,000 shares in June 2018 for €18,000 and 2,000 shares in February 2021 for €22,000. Proceeds on disposal were €75,000 (broker net of commission). No other share disposals during 2025. No capital losses brought forward. FIFO identification (TCA s. 581): the 3,000 June 2018 shares are deemed disposed of first, then 2,000 of the February 2021 holding. No indexation (post-2003 acquisitions). Mr Ó Briain reports the disposal on Form CG1 (or via Form 11 if otherwise self-assessed).

**Example A computation table**

| Line item | Amount (€) |
| --- | --- |
| Disposal proceeds | 75,000 |
| Less: Cost of 3,000 shares (June 2018) | (18,000) |
| Less: Cost of 2,000 shares (Feb 2021) | (22,000) |
| **Chargeable gain (gross)** | **35,000** |
| Less: Annual exemption | (1,270) |
| **Taxable amount** | **33,730** |
| CGT at 33% | **11,131** |

### Example B — Sale of family home with periods of letting (PPR partial)

Facts. Ms Ní Mhurchú purchased her family home in Galway in January 2008 for €280,000 (plus €5,000 incidental costs). She lived there as her PPR until December 2018. From January 2019 to December 2023 she let the property while working in Dublin (she rented a flat there). She moved back to the Galway property in January 2024 and sold it on 30 November 2025 for €490,000 (€10,000 incidental costs of disposal). Apportionment of qualifying months: PPR occupation: 132 + 23 = 155 months. Plus permitted absence (work elsewhere in Ireland, up to 4 years): 48 months. Plus final 12 months (already included within the qualifying-occupation count for the closing period — DO NOT double count). Total qualifying months: 155 + 48 = 203 months. Non-qualifying months: 215 − 203 = 12 months. The disposal of €490,000 is below the €1,000,000 CG50 threshold for residential property, so no CG50 clearance / 15% withholding applies.

**Example B period table**

| Period | Months | Treatment |
| --- | --- | --- |
| Jan 2008 – Dec 2018 | 132 | PPR — qualifying |
| Jan 2019 – Dec 2023 | 60 | Let — non-qualifying (4-year work-elsewhere-in-Ireland absence relief covers 48 months; final 12 months count as final-period; net non-qualifying = 60 − 48 = 12 months, then offset by the always-qualifying final-12-months at the end of ownership — but the final-12-months rule applies only to the LAST 12 months of ownership) |
| Jan 2024 – Nov 2025 | 23 | PPR — qualifying |
| **Total ownership** | **215** |  |

**Example B computation table**

| Line item | Amount (€) |
| --- | --- |
| Disposal proceeds | 490,000 |
| Less: Incidental costs of disposal | (10,000) |
| Less: Acquisition cost + incidental | (285,000) |
| **Total gain** | **195,000** |
| Apportioned non-qualifying (195,000 × 12/215) | 10,884 |
| Less: Annual exemption | (1,270) |
| **Taxable amount** | **9,614** |
| CGT at 33% | **3,173** |

### Example C — Entrepreneur disposal of trading company shares

Facts. Ms de Paor, aged 47, founded an Irish trading company in 2018 and held 100% of the ordinary share capital. She was a full-time working director throughout. On 1 October 2025 she sold 100% of the shares to an unrelated third party for €1,400,000. Her acquisition cost (initial subscription) was €10,000. She has not previously claimed Entrepreneur Relief. Eligibility check (TCA s. 597AA): Holding period > 3 years ✔. ≥ 5% ordinary share capital ✔. Working director devoting ≥ 50% of working time for ≥ 3 years ✔. Qualifying trading company (not investment / dealing in land) ✔. Lifetime cap not previously used ✔. The disposal exceeds €500,000 (and the asset is unquoted shares of an Irish company deriving value other than primarily from Irish land — confirm whether s. 980 catches this transaction). In practice, where shares derive their value primarily from a Nigerian or other non-land asset, the CG50 regime may not apply. Where the value derives substantially from Irish land/minerals, a CG50A clearance certificate should be obtained.

**Example C computation table**

| Line item | Amount (€) |
| --- | --- |
| Disposal proceeds | 1,400,000 |
| Less: Acquisition cost | (10,000) |
| **Chargeable gain (gross)** | **1,390,000** |
| Less: Annual exemption | (1,270) |
| **Net chargeable gain** | **1,388,730** |
| Qualifying portion (within €1M Entrepreneur Relief lifetime cap) | 1,000,000 |
| CGT at 10% on qualifying portion | **100,000** |
| Excess portion (over €1M cap) | 388,730 |
| CGT at 33% on excess | **128,281** |
| **Total CGT** | **228,281** |

## Section 6 — Filing & payment

### 6.1 Returns — Form CG1 vs Form 11 / 11S

- **Return form usage and filing deadline** — Form CG1 is the standalone CGT return used by taxpayers who are NOT otherwise within the self-assessment ("chargeable persons") regime. It is filed annually for each tax year in which a disposal arose. Form 11 / Form 11S — self-employed individuals (sole traders, professionals, company directors filing as chargeable persons) include their CGT computation within the annual Form 11 self-assessment return. Both forms are filed via the Revenue Online Service (ROS) under the mandatory e-filing regime. Filing deadline for the annual return: 31 October following the end of the tax year (with the ROS pay-and-file extension typically to mid-November for ROS users — confirm Revenue's published extended date each year).

### 6.2 Preliminary CGT — pay-and-file under TCA s. 959AO

- **Two-stage preliminary CGT payment model** — CGT operates a unique two-stage payment model: Initial period — disposals between 1 January and 30 November of the tax year: preliminary CGT is due by 15 December of the same tax year. Later period — disposals between 1 December and 31 December of the tax year: preliminary CGT is due by 31 January of the following year. Any balance of CGT (after preliminary payments) is due with the annual return by 31 October of the year following the tax year. This is unusual relative to other Irish taxes: CGT must be paid largely within the tax year itself, even before the annual return is filed.  _(TCA s. 959AO)_

### 6.3 ROS filing & PPSN

- **ROS filing and payment methods** — All Irish-resident individual taxpayers should have a PPSN and a ROS account. Form CG1 and Form 11 are filed electronically via ROS (myAccount route for PAYE-only taxpayers with simple disposals; ROS for full self-assessment). Payment via ROS Debit Instruction (RDI), credit card, or single-debit authority.

### 6.4 CG50 / CG50A mechanics

- **CG50/CG50A process detail** — On any in-scope disposal > €500,000 (land/buildings/mineral rights/relevant shares/goodwill) — or > €1,000,000 for residential property: Vendor applies for CG50A clearance via Form CG50, lodged with Revenue's CGT clearance unit before completion. If granted, no 15% withholding is required from the buyer. If not produced, the buyer must withhold 15% of the consideration and remit it to Revenue using Form CG50B; the withholding is credited against the vendor's eventual CGT liability.

### 6.5 Records & retention

- **Record retention requirements** — Retain acquisition contracts, valuation evidence, brokerage notes, disposal contracts, and CG50 documentation for 6 years from the end of the relevant tax year (general Revenue record-retention rule — TCA s. 886). For PPR claims, retain evidence of dates of occupation (utility bills, register of electors, correspondence) for the full ownership period.  _(TCA s. 886)_

## Section 7 — Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown acquisition cost | STOP — cannot compute gain |
| Acquisition by gift or inheritance with no probate / CAT valuation | Obtain probate / market valuation; if unavailable, STOP |
| PPR claimed but property had periods of letting beyond rent-a-room | Apportion conservatively; assume non-qualifying for the let period |
| Garden / grounds > 1 acre | Apportion proportionally; restrict PPR to one-acre site |
| Unclear whether Entrepreneur Relief 5% / 3-year / working-director conditions are met | Assume conditions not met → 33% standard rate |
| Unknown whether prior Retirement Relief lifetime threshold breached | Assume threshold partly used → restrict relief conservatively, request prior claim history |
| Indexation factor for pre-2003 acquisition unclear | Use Revenue's published indexation table for the year of acquisition; if year unclear, STOP |
| Unknown whether parties are connected | Treat as connected → apply market value rule |
| Routine repair vs enhancement expenditure ambiguous | Treat as routine repair → NOT deductible |
| Crypto disposal with multiple lots and pooling unclear | Apply FIFO under TCA s. 581 pooling rules; document the share-identification trail |
| Disposal > €500,000 land/buildings without CG50A | Assume buyer must withhold 15%; advise vendor to apply for CG50A immediately |
| Preliminary CGT payment date borderline (e.g. completion late November vs early December) | Confirm exact disposal date (date of unconditional contract, not completion, under TCA s. 542); err toward earlier payment window |
| Non-resident disposing of an Irish-situs asset | Confirm whether asset falls within s. 29 specified assets; if not specified, assume out of charge but flag for review |
| Cross-border disposal with possible treaty relief | STOP — refer to specialist treaty review |
| Spousal transfer where one spouse is non-resident | Spousal no-gain/no-loss rule may not apply; refer to specialist |
| Loss on disposal to connected person | Treat as clogged; usable only against future gains on disposal to same person |

## Section 8 — Sources

1. Taxes Consolidation Act 1997 (TCA 1997) — primary statute, in particular: Part 19 (Principal Provisions Relating to Taxation of Chargeable Gains). Part 20 (Companies' Chargeable Gains). Part 21 (Mergers, Divisions, Transfers of Assets and Exchanges of Shares Concerning Companies of Different Member States). s. 28 (charge to capital gains tax); s. 29 (persons chargeable and territorial scope); s. 532 (assets); s. 542 (date of disposal); s. 547 (acquisition by way of gift); s. 549 (connected persons); s. 552 (allowable deductions); s. 556 (indexation); s. 573 (death); s. 581 (share identification); s. 597AA (Entrepreneur Relief); s. 598 & s. 599 (Retirement Relief); s. 602 (chattels); s. 603 (wasting chattels); s. 603A (site to child); s. 604 (PPR); s. 980 (CG50 / withholding); s. 1028 (spousal transfers). 2. Finance Act 2012 — increased headline CGT rate to 30% (effective 7 December 2011). 3. Finance Act 2013 (Budget 2013 measures) — increased headline CGT rate to 33% (effective 6 December 2012). 4. Finance Act 2013 — introduced Entrepreneur Relief at the original 20% rate. 5. Finance Act 2015 — replaced the original Entrepreneur Relief with the current TCA s. 597AA regime at 20%, capped €1M lifetime. 6. Finance Act 2016 — reduced the Entrepreneur Relief rate to 10% (effective 1 January 2017). 7. Finance Act 2014 — introduced the €3M cap on s. 599 Retirement Relief for disponers aged 66+ on transfers to a child. 8. Finance Act 2024 / Budget 2025 measures — confirm any current-year changes to thresholds, lifetime caps, or rate via published Revenue guidance. 9. Revenue Tax and Duty Manuals (TDMs) — Part 19 series, including the PPR TDM, the Entrepreneur Relief TDM, the Retirement Relief TDM, and the CG50 TDM. 10. Revenue Form CG1 and accompanying guidance notes for the relevant tax year. 11. Revenue Form 11 / Form 11S self-assessment return and accompanying guidance. 12. Revenue Online Service (ROS) guidance — e-filing instructions for CG1 and Form 11. 13. Irish Tax Institute (ITI) Capital Tax materials — practitioner-level commentary on CGT, PPR, Entrepreneur Relief, Retirement Relief, and CG50. 14. Chartered Accountants Ireland — Taxation reference materials — current-year CGT updates and worked guidance.

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
