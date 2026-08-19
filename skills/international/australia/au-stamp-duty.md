---
name: au-stamp-duty
description: Use this skill whenever asked about Australian stamp duty (transfer duty, conveyance duty, land transfer duty) in any state or territory. Trigger on phrases like "stamp duty", "transfer duty", "conveyance duty", "duty on purchase", "first home buyer duty exemption", "off the plan concession", "foreign purchaser surcharge", "surcharge purchaser duty", "AFAD", "landholder duty", "land rich", "business asset duty", "insurance duty", "motor vehicle duty", "dutiable value", "contract date", or any question about duty payable on acquiring property, businesses, shares or units in Australia. Covers rates by jurisdiction, concessions, surcharges, GL coding and the CGT cost base link.
version: "1.0"
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 duty year"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Stamp Duty

## Australia Stamp Duty (Transfer Duty) -- State & Territory Skill v1.0

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia -- eight separate state/territory duty regimes |
| Tax | Stamp duty / transfer duty / conveyance duty / land transfer duty |
| Currency | AUD only |
| Duty year | Set per jurisdiction; NSW indexes annually from 1 July. Figures below verified 20 August 2026 (2026-27 rate year) |
| Primary legislation | *Duties Act 1997* (NSW); *Duties Act 2000* (VIC); *Duties Act 2001* (QLD); *Duties Act 2008* (WA); *Stamp Duties Act 1923* (SA); *Duties Act 2001* (TAS); *Duties Act 1999* (ACT); *Stamp Duty Act 1978* (NT) |
| Tax authorities | Revenue NSW; SRO Victoria; Queensland Revenue Office; RevenueWA; RevenueSA; SRO Tasmania; ACT Revenue Office; Territory Revenue Office (NT) |
| Not a Commonwealth tax | The ATO has no role. Do not confuse with FRCGW (15%, no threshold, from 1 Jan 2025) or payroll tax (NSW 5.45% over $1.2m) |
| Skill version | 1.0 |

### Core Principles and Conservative Defaults

**Core Principles and Conservative Defaults**

| Principle / ambiguity | Rule / default |
| --- | --- |
| Who pays | The transferee/purchaser, in almost every jurisdiction |
| Dutiable value | The **greater of** consideration paid and the **unencumbered** market value -- a mortgage, lease or caveat does not reduce it |
| Liability event | Generally the **contract/agreement date**, not settlement; the contract date also sets the rate year |
| Concession vs exemption | A **concession reduces** duty; an **exemption eliminates** it (often replaced by nominal duty of $20--$100) |
| Not deductible | Duty on a capital acquisition is a **CGT cost base** item, not an income-tax deduction (§8.2) |
| Jurisdiction not stated | STOP -- duty is state-specific; ask where the land/asset is |
| Contract date unknown | Do not compute -- rate year and concession eligibility both turn on it |
| Related-party transfer, no valuation | Do not compute -- duty is on unencumbered value, not the stated price |
| Foreign person status unclear | Assume the surcharge applies and flag for confirmation |
| Landholder/corporate structure involved | Refuse and escalate (R-AU-SD-2) |
| GST treatment of the price unclear | Assume duty is charged on the **GST-inclusive** amount |

## Section 2 -- What Is Dutiable

### 2.1 The Duty Base by Jurisdiction

**Dutiable Heads by Jurisdiction**

| Head of duty | NSW | VIC | QLD | WA | SA | TAS | ACT | NT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Real property transfer | Yes | Yes | Yes | Yes | Residential/primary production only | Yes | Yes (phasing out) | Yes |
| Business assets (goodwill, IP, licences) | Abolished 1 Jul 2016 | Limited | Yes | Limited | Abolished | Abolished 1 Jul 2008 | Abolished | Tangible business property only |
| Unlisted shares/units (direct transfer) | Abolished | Abolished | Abolished | Abolished | Abolished | Abolished | Abolished | Abolished |
| Landholder duty (indirect land acquisition) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Motor vehicle registration/transfer | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| General insurance | Yes | Yes | Yes | Yes | Yes | Yes | Abolished | Yes |

Mortgage duty is abolished in every jurisdiction. Direct transfers of shares and units are no longer dutiable anywhere in Australia -- land held through an entity is instead caught by the **landholder** regimes (§7.1). Never tell a client "there is no duty on the share sale" without running the landholder test.

**SA's qualifying-land carve-out**: South Australia abolished duty on **non-residential, non-primary-production** land ("qualifying land" -- commercial, industrial, institutional, most vacant non-residential lots, per s 71DC *Stamp Duties Act 1923*), decided by land use code. An Adelaide warehouse purchase attracts **nil** conveyance duty; the same purchase in Sydney or Melbourne is fully dutiable. Confirm the land use code before quoting SA duty.

### 2.2 Related-Party and Non-Arm's-Length Transfers

There is **no market-value relief**. A transfer to a spouse, child, family trust or related company is assessed on the **unencumbered value** even if the stated consideration is $1 or nil. Revenue offices require formal valuation evidence where parties are related, there is no selling agent, consideration is non-monetary, or the same firm acts for both sides (Revenue NSW Ruling DUT 012 v4). Statutory exceptions: matrimonial/de facto property settlements, spouse transfers of the principal place of residence (several jurisdictions), and deceased-estate transfers under a will (§11.1).

## Section 3 -- The Assessment Event

- **Liability date** — Duty is imposed when the dutiable transaction occurs: the date the contract or agreement for sale is entered into. Settlement is generally only the *payment* trigger, not the *liability* trigger.
- **Rate year** — Set by the contract date. A contract signed 28 June is assessed on the old-year scale even if it settles in September (explicit in Revenue NSW guidance). A rate change or new concession announced after contract date does not apply unless the legislation says so — check the transitional rule before promising a saving.
- **Payment deadlines** — NSW: 3 months from the liability date (on settlement for e-conveyancing; off-the-plan owner-occupiers may defer up to 12 months). VIC: 30 days from settlement via Duties Online. QLD: 30 days from the liability date. WA: 1 month from assessment. SA: on settlement via RevenueSA Online. TAS: 3 months from the transaction. ACT: generally 14 days from settlement. NT: 60 days from the transaction or settlement, whichever is earlier. Late payment attracts interest plus penalty tax under each jurisdiction's Taxation Administration Act. Confirm the current lodgement rule before advising.

## Section 4 -- Rates by Jurisdiction (verified 20 August 2026)

### 4.1 New South Wales (2026-27 rate year)

**NSW Transfer Duty**

| Dutiable value | Duty |
| --- | --- |
| $0 -- $38,000 | $1.25 per $100 (minimum $20); then $225 + $1.50 per $100 over $18,000 |
| $38,001 -- $103,000 | $525 + $1.75 per $100 over $38,000 |
| $103,001 -- $387,000 | $1,662 + $3.50 per $100 over $103,000 |
| $387,001 -- $1,290,000 | $11,602 + $4.50 per $100 over $387,000 |
| Over $1,290,000 | $52,237 + $5.50 per $100 over $1,290,000 |
| Premium (residential only) over $3,870,000 | $194,137 + $7.00 per $100 over $3,870,000 |

Thresholds are CPI-indexed each 1 July. Premium duty applies to **residential** land only; on land over 2 hectares it applies to the first 2 hectares proportionally, remainder at general rates.

### 4.2 Victoria (contracts on or after 1 July 2021)

**VIC Land Transfer Duty -- general (non-PPR)**

| Dutiable value | Duty |
| --- | --- |
| $0 -- $25,000 | 1.4% of dutiable value |
| $25,001 -- $960,000 | $350 + 2.4% over $25,000; then $2,870 + 6% over $130,000 |
| $960,001 -- $2,000,000 | **5.5% of the whole dutiable value** (not marginal) |
| Over $2,000,000 | $110,000 + 6.5% over $2,000,000 |

The $960,001--$2,000,000 band is a **flat rate on the entire value** — a notch, not a margin. Crossing $960,000 by one dollar increases duty. Model both sides of the threshold before advising on an offer price.

### 4.3 Queensland

**QLD Transfer Duty -- general**

| Dutiable value | Duty |
| --- | --- |
| Not more than $5,000 | Nil |
| $5,001 -- $540,000 | $1.50 per $100 over $5,000; then $1,050 + $3.50 per $100 over $75,000 |
| $540,001 -- $1,000,000 | $17,325 + $4.50 per $100 over $540,000 |
| Over $1,000,000 | $38,025 + $5.75 per $100 over $1,000,000 |

**QLD home concession rate** (occupied as your home): $1.00 per $100 to $350,000; $3,500 + $3.50 per $100 to $540,000; $10,150 + $4.50 per $100 to $1,000,000; $30,850 + $5.75 per $100 above. The general scale above is also used for **corporate trustee duty and landholder duty**.

### 4.4 Western Australia

**WA Transfer Duty -- general rate**

| Dutiable value | Duty |
| --- | --- |
| $0 -- $120,000 | $1.90 per $100 |
| $120,001 -- $360,000 | $2,280 + $2.85 per $100 over $120,000; then $3,135 + $3.80 per $100 over $150,000 |
| $360,001 -- $725,000 | $11,115 + $4.75 per $100 over $360,000 |
| Over $725,000 | $28,453 + $5.15 per $100 over $725,000 |

WA also has a separate concessional **residential rate** for lower-value homes and the first home owner rate (§5.1) — check which scale applies before computing.

### 4.5 SA, TAS, ACT and NT

**SA / TAS / ACT / NT Duty Scales**

| Jurisdiction | Dutiable value | Duty |
| --- | --- | --- |
| SA (residential/primary production only) | $250,001 -- $300,000 | $8,955 + $4.75 per $100 over $250,000 |
| SA | $300,001 -- $500,000 | $11,330 + $5.00 per $100 over $300,000 |
| SA | Over $500,000 | $21,330 + $5.50 per $100 over $500,000 |
| TAS (chattels included in value) | Not more than $3,000 | $50 |
| TAS | $3,001 -- $75,000 | $50 + $1.75 per $100 over $3,000; then $435 + $2.25 per $100 over $25,000 |
| TAS | $75,001 -- $375,000 | $1,560 + $3.50 per $100 over $75,000; then $5,935 + $4.00 per $100 over $200,000 |
| TAS | $375,001 -- $725,000 | $12,935 + $4.25 per $100 over $375,000 |
| TAS | Over $725,000 | $27,810 + $4.50 per $100 over $725,000 |
| ACT (eligible owner-occupier, non-commercial) | Up to $260,000 | $0.28 per $100 |
| ACT | $260,001 -- $500,000 | $728 + $2.20 per $100 over $260,000; then $1,608 + $3.40 per $100 over $300,000 |
| ACT | $500,001 -- $1,000,000 | $8,408 + $4.32 per $100 over $500,000; then $19,208 + $5.90 per $100 over $750,000 |
| ACT | $1,000,001 -- $1,455,000 | $33,958 + $6.40 per $100 over $1,000,000 |
| ACT | Over $1,455,000 | Flat $4.54 per $100 of the **whole** transaction value |
| NT | Up to $525,000 | D = (0.06571441 × V²) + 15V, where V = dutiable value ÷ 1,000 |
| NT | $525,001 -- $3,000,000 | 4.95% of dutiable value |
| NT | $3,000,001 -- $5,000,000 | 5.75% of dutiable value |
| NT | Over $5,000,000 | 5.95% of dutiable value |

ACT rates above are the eligible owner-occupier scale (unchanged from 1 July 2025); non-owner-occupiers pay a higher scale. ACT is phasing conveyance duty out over 20 years in favour of general rates -- from 1 July 2026 commercial property with a dutiable value of $2,100,000 or less pays **no** conveyance duty, with a flat 5% above that.

## Section 5 -- Concessions and Exemptions

### 5.1 First Home Buyer Relief (verified 20 August 2026)

**First Home Buyer Duty Relief**

| Jurisdiction | Full exemption | Tapered concession |
| --- | --- | --- |
| NSW (FHBAS) | New or existing home to $800,000; vacant land to $350,000 | Home $800,001--$1,000,000; land $350,001--$450,000 |
| VIC | Dutiable value to $600,000 | $600,001--$750,000, phased by (value − $600,000) ÷ $150,000 |
| QLD | Established home to $700,000; **new home or vacant land — full concession, no value cap**, contracts from 1 May 2025 | Established home $700,000--$799,999.99 (concession tapers from $17,350 to nil at $800,000) |
| WA | Home to $600,000 (from 7 May 2026); vacant land to $450,000 | Home $600,001--$800,000 at $16.15 per $100 over $600,000; land $450,001--$550,000 at $20.14 per $100 over $450,000 |
| SA | New home, off-the-plan apartment or vacant land — relief for contracts from 15 June 2023 (value caps depend on contract date) | Per RevenueSA calculator. Note: for contracts from 13 February 2025, FHB relief no longer extends to the foreign ownership surcharge — a foreign first home buyer pays the 7% surcharge even when the base duty is relieved |
| TAS | **Expired** — the 100% established-home exemption (to $750,000) is unavailable for transfers settling after 30 June 2026 | None currently |
| ACT | Home Buyer Concession Scheme — income-tested, full exemption to $1,020,000 property value (from 1 July 2025), maximum concession $35,238 | Above $1,020,000 |
| NT | No general first home duty concession currently; territory home-owner grants operate separately | — |

All FHB schemes impose residence requirements (typically 6--12 months' continuous occupation starting within 12 months of settlement), a natural-person requirement (no companies or trusts), and a prior-ownership bar covering spouses.

### 5.2 Off-the-Plan and Residence Concessions

- **NSW off-the-plan** — No value deduction, but owner-occupiers may **defer** duty up to 12 months or until settlement, whichever is earlier. Deferral is cash flow, not a saving.
- **VIC off-the-plan** — Deducts outstanding **construction and refurbishment costs** from dutiable value. The temporarily expanded version (all buyers including investors and companies, strata apartments and townhouses, no value threshold) runs from 21 October 2024 and is extended to **21 April 2027**. QLD, SA and NT have no dedicated off-the-plan concession — ordinary rates apply to the full contract price.
- **Residence concessions** — VIC PPR concession: dutiable value up to $550,000 with 12 continuous months' occupation, not combinable with the FHB exemption. VIC City of Melbourne: 50% concession or full exemption for new residential property in the LGA up to $1 million (different contract-date windows). QLD home concession: available to any buyer occupying the property as a home, not just first home buyers (§4.3 scale).
- **Pensioner/concession-card relief** — VIC (to $750,000), SA seniors downsizing relief, and jurisdiction-specific equivalents. One benefit per transaction: an eligible pensioner who is also a first home buyer must choose.

## Section 6 -- Foreign Purchaser Surcharges

**Foreign Purchaser Additional Duty (residential land)**

| Jurisdiction | Surcharge | Notes |
| --- | --- | --- |
| NSW | **9%** (from 1 Jan 2025) | Surcharge purchaser duty, flat on dutiable value, on top of transfer duty |
| VIC | **8%** (from 1 Jul 2019) | Foreign purchaser additional duty (FPAD), applied before concessions |
| QLD | **8%** | Additional foreign acquirer duty (AFAD); includes foreign companies and trusts |
| WA | **7%** | Foreign buyers duty; includes landholder acquisitions |
| SA | **7%** | Foreign ownership surcharge, applied to the foreign interest only |
| TAS | **8%** | Foreign investor duty surcharge (residential, from 1 Apr 2020); lower rate for primary production |
| ACT | Nil on conveyance duty | A separate land tax foreign ownership surcharge applies |
| NT | Nil | — |

- The surcharge is **in addition to** ordinary duty and is generally not reduced by first home or PPR concessions.
- NSW's international tax treaty exemption (New Zealand, Finland, Germany, India, Japan, Norway, South Africa, Switzerland) was **removed for agreements entered on or after 8 April 2024** following the Commonwealth *Treasury Laws Amendment (Foreign Investment) Act 2024*. Older advice claiming a treaty exemption is out of date.
- A discretionary trust with a potential foreign beneficiary is generally treated as a foreign person unless the deed irrevocably excludes them. This is the most common accidental surcharge trigger — flag it, do not fix it (R-AU-SD-5).
- Separate from **FRCGW** (15% vendor withholding, no threshold, from 1 Jan 2025) and from Commonwealth FIRB fees.

## Section 7 -- Landholder, Business Asset and Other Duties

### 7.1 Landholder Duty

Acquiring shares or units in an entity whose land exceeds the threshold is taxed as if the land itself were transferred.

**Landholder Duty Thresholds**

| Jurisdiction | Land value threshold | Significant interest -- private | Public/listed |
| --- | --- | --- | --- |
| NSW | $2,000,000 | 50% (private company); **20%** (private unit trust, from 1 Feb 2024) | 90% |
| VIC | $1,000,000 | 50% (private company / wholesale unit trust); 20% (private unit trust) | 90% |
| QLD | $2,000,000 | 50% | 90% |
| WA | $2,000,000 | 50% | 90% |
| SA / TAS / ACT / NT | Per each Duties Act | Generally 50% | Generally 90% |

Duty is charged at the ordinary transfer duty scale on the proportion of the landholder's land (and, in some jurisdictions, goods) acquired. Acquisitions **aggregate**: moving from 45% to 50% is a relevant acquisition on the whole 50% interest, not the 5% step. NSW requires payment within 3 months of the relevant acquisition, and foreign surcharges can apply to landholder acquisitions of residential land. Anything beyond identifying that the regime is *engaged* is out of scope (R-AU-SD-2).

### 7.2 Business Asset Duty

- **NSW** abolished business asset duty, marketable securities duty and mortgage duty from **1 July 2016**. A NSW business sale is dutiable only to the extent it includes land.
- **QLD** still taxes Queensland **business assets** — goodwill, business names, IP, statutory business licences, debts and some personal property (s 35 *Duties Act 2001*).
- **NT** taxes tangible business property (land, buildings, plant acquired with other dutiable property, chattels, certain statutory licences) but **not** intangibles such as goodwill, trademarks, stock-in-trade, work in progress or livestock.
- **TAS** abolished duty on goodwill and other non-real business assets from 1 July 2008; **SA** and **ACT** have abolished it.
- In a multi-state business sale, apportion the price by jurisdiction and asset class before assuming a duty outcome.

### 7.3 Motor Vehicle and Insurance Duty

- **Motor vehicle duty** — Payable on registration or transfer of registration. NSW: $3 per $100 of value (higher above the luxury threshold). QLD: $2--$4 per $100 by cylinder count, with hybrid and electric vehicles at $2 per $100 up to $100,000. Each jurisdiction has its own scale and EV settings.
- **Insurance duty** — Charged on the **premium**. NSW: 9% (Type A general), 5% (Type B — motor vehicle, aviation, disability income, occupational indemnity, health); crop and livestock exempt from 1 January 2018; a small business exemption applies to CGT small businesses. QLD: 9% of the premium **including GST** for class 1 and class 2 general insurance, 5% of the first year's premium for term life. SA: 11% general insurance. ACT has abolished insurance duty. Insurance duty is embedded in the premium and shows on the tax invoice, not as a separate assessment.

## Section 8 -- Interactions

### 8.1 GST

- Dutiable value is the **GST-inclusive** consideration. A commercial property sold for $1.1m including GST is assessed on $1.1m, not $1m. The margin scheme does not reduce dutiable value.
- Where the sale is a **GST-free going concern** or **farmland**, there is no GST in the price, so dutiable value is simply the price.
- Duty **itself** carries no GST — it is an Australian tax, not consideration for a supply. Code duty payments as BAS-excluded/no-GST; never claim an input tax credit on a duty payment.
- The VIC Digital Duties Form requires GST-exclusive price, GST payable and total to be entered separately; duty is assessed on the total.

### 8.2 CGT Cost Base -- cross-reference `au-capital-gains`

- Transfer duty on acquiring a CGT asset is an **incidental cost** forming part of the **second element** of the cost base (ss 110-25(3), 110-35 ITAA 1997).
- It is **not** an immediate deduction for a capital acquisition and not a rental property deduction (contrast land tax and council rates, which are deductible while the property is income-producing — see `au-rental-property`).
- Duty on a **leasehold** acquisition or a lease premium may be deductible or amortisable in narrow cases — escalate rather than assume.
- Keep the duty assessment notice with the contract for the life of the asset: it is primary evidence of the cost base, and CGT records must be kept until 5 years after disposal.

### 8.3 Objections and Reassessment

- Every jurisdiction allows a written **objection** to a duty assessment, generally within **60 days** of the assessment notice, under its Taxation Administration Act; late objections require the Commissioner's discretion. Common grounds: valuation, misclassification of land use (critical in SA), incorrect application of a concession, and aggregation disputes.
- **Refunds/reassessment** — A cancelled contract, corrected concession claim, or a first home buyer who paid at settlement can usually be reassessed; SA allows FHB relief refund applications within 5 years of settlement. Deadlines vary — verify before relying on one. Objection is administrative review, but drafting the objection is legal work (R-AU-SD-1).

## Section 9 -- GL Sweep

**Bookkeeping Patterns -- Duty**

| Bank/ledger pattern | Classification | Treatment |
| --- | --- | --- |
| REVENUE NSW DUTY, SRO VIC DUTIES ONLINE, QRO TRANSFER DUTY, REVENUEWA, REVENUESA, ACT REVENUE | Transfer duty on property purchase | **Capitalise** to the property asset account; add to CGT cost base. No GST |
| PEXA / SETTLEMENT DISBURSEMENT (duty line on settlement statement) | Duty within a settlement bundle | Split the statement: duty → asset cost; rates/water adjustments → expense; agent and legal fees → cost base |
| LANDHOLDER DUTY ASSESSMENT | Duty on a share/unit acquisition | Capitalise to the **cost of the shares/units**, not to the underlying land. No GST |
| DUTY -- BUSINESS ASSETS (QLD/NT) | Duty on a business acquisition | Allocate across acquired assets on the same basis as the purchase price allocation; goodwill portion → goodwill cost base |
| SURCHARGE PURCHASER DUTY / AFAD / FPAD | Foreign purchaser surcharge | Same treatment as the underlying duty — capitalise. Never expense to "taxes" |
| MOTOR VEHICLE DUTY / REGO DUTY | Vehicle registration duty | Capitalise into the vehicle's cost for depreciation. No GST |
| STAMP DUTY ON INSURANCE (line within a premium) | Insurance duty | Part of the insurance expense; not itself subject to GST, so GST on the premium is computed on base premium plus levies, not on the duty |
| DUTY PENALTY TAX / INTEREST | Penalty and interest on late duty | Expense. Penalty tax is **not** deductible; general interest may be — flag for review |
| DUTY REFUND RECEIVED | Reassessment refund | Credit against the original capitalised amount (reduces cost base), not to income |

**Never** post transfer duty to a "Taxes and licences" expense account for a property or share purchase. It is a capital cost, and mis-posting it silently understates the CGT cost base years later.

## Section 10 -- Worked Examples

### Example 1 -- NSW first home buyer at the exemption cap

Contract 15 August 2026, existing home in Newcastle, price **$800,000**, both buyers eligible under FHBAS.

- General duty: $11,602 + 4.5% × ($800,000 − $387,000) = $11,602 + $18,585 = **$30,187**. FHBAS gives a full exemption at $800,000 or less → duty payable **$0**.
- **Saving: $30,187.** At $800,001 the concessional (not exempt) scale begins — one dollar of price is worth tens of thousands.

### Example 2 -- VIC first home buyer, tapered concession

Contract 3 July 2026, established home in Geelong, dutiable value **$650,000**, eligible first home buyer.

- General duty: $2,870 + 6% × ($650,000 − $130,000) = $2,870 + $31,200 = **$34,070**. Phase-in factor: ($650,000 − $600,000) ÷ $150,000 = 0.3333.
- Duty payable: $34,070 × 0.3333 = **$11,357** (rounded). **Saving: $22,713.** Nil at $600,000, full duty at $750,000.

### Example 3 -- VIC aggregation across two lots

One purchaser buys two adjoining vacant lots from the same vendor under one arrangement, **$480,000 each**.

- Assessed separately: $2,870 + 6% × $350,000 = $23,870 each → **$47,740**. Aggregated at $960,000: $2,870 + 6% × ($960,000 − $130,000) = $2,870 + $49,800 = **$52,670**.
- **Extra duty from aggregation: $4,930.** Watch the notch immediately above: at $960,001 the flat 5.5% band applies to the *whole* value ($52,800), so a small price rise costs more than the increment.

### Example 4 -- QLD foreign purchaser, investment property

A foreign-owned company contracts on 10 August 2026 to buy a Brisbane residential unit for **$1,300,000**. No home concession (not a residence).

- Transfer duty: $38,025 + 5.75% × ($1,300,000 − $1,000,000) = $38,025 + $17,250 = **$55,275**. AFAD: 8% × $1,300,000 = **$104,000**.
- **Total duty: $159,275** — the surcharge adds 65% again on top of base duty. An Australian resident individual occupying the unit would instead use the home concession scale: $30,850 + 5.75% × $300,000 = **$48,100**.

### Example 5 -- NSW landholder duty, 60% share acquisition

A private company holds NSW land with an unencumbered value of **$4,000,000** plus goods of **$500,000**. An investor acquires **60%** of the shares on 1 August 2026 — a relevant acquisition (50%+ in a private landholder; land above the $2m threshold).

- Dutiable value: 60% × ($4,000,000 + $500,000) = **$2,700,000**. Duty: $52,237 + 5.5% × ($2,700,000 − $1,290,000) = $52,237 + $77,550 = **$129,787**, payable within 3 months of the acquisition. Surcharge purchaser duty may also apply if the land is residential and the acquirer is foreign.
- **This illustrates the threshold test only.** Real landholder calculations trace linked entities, prior acquisitions in the aggregation window and constructive interests — refuse and escalate (R-AU-SD-2).

## Section 11 -- Edge Cases

### 11.1 Deceased Estates

- A transfer from a deceased estate to a beneficiary **in conformity with the will** or on intestacy is generally exempt or attracts only nominal duty. NSW charges a concessional **$100**; Victoria treats it as exempt under s 42(1) *Duties Act 2000* and extends the same treatment to the first transfer into a testamentary trust.
- The concession is fragile: a transfer for **valuable consideration**, an unequal distribution settled with cash between beneficiaries, or a transfer that does not conform to the will can be assessed at full ad valorem rates. Put the grant of probate and the will in front of the revenue office.
- CGT rollover on death is a separate question — see `au-capital-gains`.

### 11.2 Trust Distributions and Trust Dealings

- An in-specie distribution of real property from a trust to a beneficiary is **generally a dutiable transfer**, even with no money changing hands. Some jurisdictions provide narrow relief for distributions to a beneficiary of a fixed trust where no consideration passes and the beneficiary's existing interest is being satisfied.
- Trust **resettlements**, deed variations, changes of trustee and changes of beneficial ownership are separate dutiable heads in several jurisdictions (NT charges nominal $20 duty on a trust deed). These need jurisdiction-specific advice **before** the deed is signed — after the fact there is usually no fix. Refuse and escalate (R-AU-SD-5).

### 11.3 Corporate Reconstruction and Consolidation Relief

All jurisdictions offer some form of **corporate reconstruction/consolidation** relief for transfers within a wholly-owned group, but the tests (group composition, pre- and post-association periods, clawback on group exit) differ materially and several require an **application before** the transaction. Relief is discretionary in some jurisdictions and a statutory exemption in others, ranging from full exemption to a 90% reduction. Do not model a restructure assuming relief will be granted (R-AU-SD-3).

### 11.4 Other Traps

- **Nominations and sub-sales** — Naming a different purchaser before settlement can create a **second dutiable transaction** (double duty), particularly under Victoria's sub-sale provisions. **Options**: granting or assigning a call option over land is dutiable in several jurisdictions (call option assignment duty in NSW).
- **Chattels** — Chattels sold with land are dutiable in TAS and several others; allocating price to chattels rarely reduces duty and invites reassessment. **Partnership interests**: acquiring an interest in a land-holding partnership can be dutiable as an indirect land acquisition.

## Section 12 -- Refusal Catalogue

- **R-AU-SD-1 -- Duty clause drafting** — Trigger: request to draft, review or amend a duty clause, special condition, objection letter or contract term. Message: "Drafting or reviewing contractual duty clauses is legal work. Refer to a property solicitor or licensed conveyancer in the relevant jurisdiction."
- **R-AU-SD-2 -- Complex landholder duty structures** — Trigger: multi-entity groups, linked or tracing interests, staged acquisitions, unit trust conversions, or any landholder analysis beyond confirming the threshold is engaged. Message: "Landholder duty across linked entities requires specialist state taxes advice. This skill can identify that the regime is engaged, not compute the liability."
- **R-AU-SD-3 -- Corporate reconstruction and consolidation relief** — Trigger: intra-group restructure, demerger, group consolidation, or a request to confirm relief eligibility. Message: "Corporate reconstruction relief has jurisdiction-specific pre-approval and clawback conditions. Escalate before executing any transaction."
- **R-AU-SD-4 -- Cross-border and interstate share/unit transfers** — Trigger: acquisition of shares or units in an entity holding land in more than one jurisdiction, or a non-resident acquirer. Message: "Multi-jurisdiction and cross-border acquisitions require concurrent analysis under each Duties Act plus FIRB. Escalate to a state taxes specialist."
- **R-AU-SD-5 -- Trust distributions and dealings in dutiable property** — Trigger: in-specie distribution, resettlement, deed variation, change of trustee, or discretionary-trust foreign-beneficiary questions. Message: "Duty on trust dealings in dutiable property is jurisdiction-specific and depends on the deed. Obtain advice before the deed is executed."
- **R-AU-SD-6 -- Valuation disputes and objections** — Trigger: client disputes the Commissioner's valuation or land-use classification. Message: "Valuation objections require a qualified valuer's report and a formal objection within the statutory period. Escalate."

## Section 13 -- Provenance

**Primary legislation** — *Duties Act 1997* (NSW): Ch 2 transfer duty, Ch 4 landholder, Ch 8 insurance. *Duties Act 2000* (Vic): Ch 2 land transfer duty (s 42(1) deceased estates), Ch 3 landholder. *Duties Act 2001* (Qld): Ch 2 transfer duty, s 35 business assets, Ch 3 landholder, Ch 8 insurance. *Duties Act 2008* (WA). *Stamp Duties Act 1923* (SA): s 71DC qualifying land. *Duties Act 2001* (Tas): Ch 2. *Duties Act 1999* (ACT). *Stamp Duty Act 1978* (NT). Commonwealth: ITAA 1997 ss 110-25, 110-35 (cost base); *Treasury Laws Amendment (Foreign Investment) Act 2024*.

**Revenue office sources verified 20 August 2026**

- Revenue NSW — "How to calculate transfer duty" (2026/27 thresholds, premium duty, FHBAS, 9% surcharge); "What is landholder duty"; "Types of insurance"; "Transfer duty concession for deceased estate transfers"; "Off the plan property purchases"; Revenue Ruling DUT 012 v4.
- SRO Victoria — "Land transfer duty – non-principal place of residence (current rates)"; "First home buyer duty exemption or concession"; "Principal place of residence duty concession"; "Strata apartments and townhouses temporary concession" (extended to 21 April 2027); "Understanding foreign purchaser additional duty"; "Deceased estates and duty".
- Queensland Revenue Office — "Transfer duty rates"; "Transfer duty home concession rates"; "Additional foreign acquirer duty"; "Insurance duty rates"; "Assessing if business asset transfers are dutiable"; qld.gov.au vehicle registration duty rates.
- Government of WA (Treasury/Finance) — "Transfer duty assessment" (general and first home owner rates); "Duties Fact Sheet – First Home Owner Rate"; "About foreign buyers duty".
- RevenueSA — "Stamp Duty on Land"; "Calculate stamp duty" (qualifying land use codes, IC 103); "Stamp Duty Relief for Eligible First Home Buyers"; "Foreign Ownership Surcharge".
- SRO Tasmania — "Rates of duty"; "First home buyers of established homes duty relief"; "Foreign investor duty surcharge".
- ACT Revenue Office — "Conveyance duty for non-commercial property"; "About conveyance duty (stamp duty)".
- Territory Revenue Office (NT) — "Stamp duty: buying or selling a home"; "Examples of duty and rates"; conveyance calculator formula.

**Cross-references**: `au-capital-gains` (cost base), `au-rental-property` (which property outgoings are deductible), `au-nonresident-cgt` (FRCGW — separate from duty), `australia-bookkeeping` (capitalisation and chart of accounts), `australia-payroll` (payroll tax — a different state tax, do not conflate).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

Duty rates, thresholds and concessions change frequently, and several are indexed annually or set by budget announcement. Always re-verify against the relevant revenue office before quoting a figure to a client.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
