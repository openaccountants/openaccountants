---
name: au-gst-property
description: >
  Use this skill whenever GST touches Australian real property -- selling or buying new
  residential premises, potential residential land, commercial premises or vacant land; GST at
  settlement withholding (Forms one and two, 1/11th or 7%); margin scheme computations under
  Division 75; GST-free going concern sales and Division 135 clawbacks; developers renting unsold
  stock (Division 129 adjustments); or one-off subdivisions and the enterprise question. Trigger
  on "GST withholding", "GST at settlement", "margin scheme", "going concern", "new residential
  premises", "subdivision GST". Covers classification, withholding mechanics, worked arithmetic
  and escalation lines. ALWAYS read this skill before touching any property GST work.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia GST and Real Property Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, or contracts. Do not rely on it to file, pay, settle, or take a tax position without review by a qualified professional.

> **Relationship to the base GST skill.** General BAS mechanics (labels, tax invoices, Simpler BAS, reverse charge, food/health classifications) live in `australia-gst`. That skill's refusal lines R-AU-3 (margin scheme) and R-AU-4 (going concern) route here: this skill supplies the specialist property layer -- classification, withholding, margin, going concern, and adjustment computations -- with its own, narrower refusal catalogue (Section 8). Escalation still ends with a registered tax agent.

## Section 1 -- Quick reference

**Read this whole section before classifying any property transaction.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary legislation | GST Act 1999: Divs 38, 40, 75, 129, 135; TAA 1953 Sch 1: ss 14-250, 14-255, 18-60 |
| GST rate | 10% (GST = 1/11th of a GST-inclusive price) |
| Registration threshold | $75,000 GST turnover ($150,000 non-profit); mere disposals of capital assets excluded from projected turnover (s 188-25) |
| GST at settlement (RW) | From 1 July 2018: purchaser withholds on new residential premises and potential residential land -- 1/11th of contract price; 7% if margin scheme; 10% of GST-exclusive market value for below-market supplies between associates |
| RW forms | Form one: *GST property settlement withholding notification* (issues PRN + LRN); Form two: *GST property settlement date confirmation* |
| Supplier RW credit | Withheld amount lands in the supplier's *GST property credits* account; transfers to the activity statement account on lodgment (s 18-60 Sch 1 TAA) |
| New residential premises | s 40-75(1): not previously sold as residential premises / no previous long-term lease (50+ years); or created by substantial renovations; or built to replace demolished premises |
| 5-year rule | s 40-75(2): premises stop being "new" after at least 5 years used ONLY for input-taxed residential rent (para 40-35(1)(a)) |
| Margin scheme agreement | In writing, on or before making the supply (settlement) -- s 75-5(1A); Commissioner may allow further period (PS LA 2005/16) |
| Div 129 adjustment periods | Non-business-finance acquisitions: 2 (<= $5,000), 5 (> $5,000 and < $500,000), 10 (>= $500,000) -- s 129-20(3) |
| Div 135 clawback | Increasing adjustment = 1/10 x supply price x proportion of non-creditable use (s 135-5) |
| Penalty unit | $364 (from 1 July 2026) |
| FRCGW (separate regime) | Foreign resident capital gains withholding: 15%, NO price threshold, from 1 January 2025. Income tax withholding, not GST -- different forms; both can apply to one settlement |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Residential premises: new or existing? | Existing (input taxed) for ITC purposes; but flag RW screening as if new until contract sighted |
| Whether the 5-year rule is satisfied | NOT satisfied -- "only used" for renting is strict; any marketing-for-sale period breaks it |
| Margin scheme agreement status | No valid written agreement until the signed contract clause is sighted |
| Going concern conditions | NOT met until written agreement, both registrations, and carry-on-to-settlement are all evidenced |
| Purchaser's intended use after a going concern purchase | Input-taxed use possible -- quantify the Div 135 exposure at full supply price |
| Developer's unsold stock being rented | Div 129 increasing adjustment applies; 10 adjustment periods (assume >= $500,000) |
| One-off subdivision | Enterprise question OPEN -- work the MT 2006/1 factors; never assume mere realisation |
| Vendor GST registration status | Check ABN Lookup; do not accept the contract's assertion alone |

## Section 2 -- Classifying supplies of real property

| Supply | Treatment | Source |
|---|---|---|
| Sale of NEW residential premises | Taxable (RW applies) | s 40-75; s 40-65(2)(b) |
| Sale of existing residential premises | Input taxed | s 40-65 |
| Residential rent (long-term) | Input taxed | s 40-35(1)(a) |
| Commercial premises -- sale or lease (office, retail, industrial) | Taxable | s 9-5 (no exemption) |
| Vacant land sold in the course of an enterprise | Taxable (not residential premises -- no shelter: GSTR 2012/5); RW applies if potential residential land | s 9-5; s 14-250 |
| Commercial residential premises (hotels, motels, boarding houses, caravan parks) | Taxable -- but classification is contested territory; refuse R-AU-GP-4 | s 87; GSTR 2012/6 |
| Farmland with continuing farming business | GST-free (conditions) | Subdiv 38-O |
| Sale of a leased building as a going concern | GST-free (conditions -- Section 5) | s 38-325 |

### 2.1 New residential premises (s 40-75)

Residential premises are **new** if any limb applies, subject to limb (a) overriding (b) and (c):

- **(a)** not previously sold as residential premises (other than commercial residential) and never subject to a long-term lease (50+ years); or
- **(b)** created through **substantial renovations** of a building -- renovations affecting the building as a whole in which all or substantially all of the building is removed or replaced (need not be structural: GSTR 2003/3 paras 53-83); cosmetic refresh (paint, carpet, kitchen swap) is NOT enough; or
- **(c)** built to replace demolished premises on the same land.

Subdividing or strata-titling existing (not-new) residential premises does **not** create new premises (s 40-75(2AA)). Intra-GST-group sales and certain associate "wholesale supply" arrangements are disregarded for the "previously sold" test (ss 40-75(2A), (2B)) -- grouping does not launder newness away; flag any group or development-agreement structure (R-AU-GP-3, R-AU-GP-6).

**AUDIT FLASH POINT -- the 5-year rule (s 40-75(2)).** Premises cease to be new if, for a continuous period of at least 5 years since they first became residential premises / were last substantially renovated / were last built, they have **only** been used for making input-taxed supplies under para 40-35(1)(a) (residential rent). "Only" is strict: a developer who rents an apartment while simultaneously marketing it for sale is applying it to a dual purpose, so the 5-year clock never runs (ATO view in GSTR 2003/3 and GSTR 2009/4). Five years of rental with the property listed for sale in year 2 does NOT convert the premises. Conversion changes everything downstream: the eventual sale becomes input taxed, ITCs claw back through Div 129, and no RW applies.

### 2.2 Input-taxed consequences and mixed developments

Input-taxed supplies (existing residential sales, residential rent) carry **no GST and no input tax credits** on related acquisitions (s 11-15(2)(a)). Consequences:

- A landlord of residential premises claims nothing on agent fees, repairs, or the purchase itself -- even though those suppliers charge GST.
- A developer intending both taxable sales and input-taxed letting must **apportion** every acquisition (construction, professional fees, marketing) to its extent of creditable purpose using a fair and reasonable method (GSTR 2006/4); a mixed tower (shops below, long-term apartments above) apportions by floor area, cost or expected revenue.
- Apportionment percentages set at acquisition are provisional -- Div 129 (Section 6) trues them up against actual use.

## Section 3 -- GST at settlement (residential withholding, from 1 July 2018)

RW re-plumbs **payment**, not liability: the purchaser pays part of the price to the ATO, and the supplier's BAS still self-assesses the actual GST. Statute: s 14-250 Sch 1 TAA (withholding), s 14-255 (supplier notification), s 18-60 (supplier credit); LCR 2018/4.

**Scope.** Withholding applies to taxable supplies, by way of sale or long-term lease, of:
- **new residential premises** (except those created by substantial renovations, and except commercial residential premises); and
- **potential residential land** (zoned to permit residential use, no building that is residential premises -- e.g. a subdivision lot), unless the purchaser is GST-registered and acquires for a creditable purpose.

**Excluded:** substantial-renovation premises, commercial residential, commercial property, premises no longer new (previously sold, or 5-year rule satisfied), potential residential land with a building in commercial use, and non-taxable sales (the family home, mere realisations).

**Amounts** (rounded down to the whole dollar): 1/11th of the contract price (adjusted for pre-settlement rebates); **7%** of the contract price where the margin scheme applies; 10% of the GST-exclusive market value for below-market supplies between associates.

**Process (both forms are the purchaser's obligation, usually run by their conveyancer under a signed authority):**

| Step | Who | What |
|---|---|---|
| 1 | Supplier | Written **supplier notification** before settlement -- required for any sale of residential premises or potential residential land, even to say "no withholding required". If withholding applies, must state: names + ABNs of all suppliers, GST branch number (if any), the amount, when payable, and the GST-inclusive contract price. Standard land contracts in every state (not NT) embed it |
| 2 | Purchaser | Lodge **Form one** online any time after exchange, up to the payment due date -- returns a **PRN** (payment reference) and **LRN** (lodgment reference) |
| 3 | Purchaser | Lodge **Form two** within 2 business days before settlement, on the day, or the next business day after (instalment contracts: keyed to the first payment other than the deposit) |
| 4 | Purchaser | Pay the withheld amount at settlement quoting the PRN (or hand the supplier's bank cheque process per the ATO supplier guide) |
| 5 | ATO | Credits the amount to the supplier's **GST property credits** account; email confirmation to the supplier |
| 6 | Supplier | BAS for the settlement period: full sale price at **G1**, actual GST at **1A**. Do NOT net off the withheld amount at 1A. On lodgment the property credit transfers to the activity statement account (allow up to 2 business days) |

**Penalties.** Supplier's failure to give the notification: strict liability offence, up to 100 penalty units ($36,400 at $364/unit from 1 July 2026; x5 for bodies corporate). Purchaser's failure to withhold: administrative penalty equal to the amount not withheld -- but no penalty where the purchaser reasonably relied on the supplier's notification (unreasonable where the purchaser knows the vendor is registered and the premises are plainly new).

**FRCGW is a different regime.** Foreign resident capital gains withholding (15%, no threshold, all real property, from 1 January 2025) is income tax withholding with its own forms and clearance certificates. A new-apartment sale by a foreign developer can trigger BOTH. Cross-lodging the wrong regime's forms strands the credit -- the ATO will not allocate a GST property credit until the correct GST forms are lodged.

## Section 4 -- The margin scheme (Division 75)

GST on an eligible taxable sale of real property may be worked out as **1/11th of the margin** instead of 1/11th of the full price.

- **Written agreement.** Supplier and recipient must agree in writing that the margin scheme applies, **on or before the making of the supply** -- settlement, not exchange (s 75-5(1), (1A)). The Commissioner can allow a later agreement (reviewable decision; PS LA 2005/16) but never plan on it. The clause lives in the contract: sight it, never draft it (R-AU-GP-1).
- **Eligibility.** Not available if the supplier acquired the entire interest through a supply that was *ineligible for the margin scheme* -- centrally, a fully taxable supply on which GST was worked out **without** the margin scheme (s 75-5(2), (3)). Eligible acquisition histories include: purchases from unregistered vendors, input-taxed purchases (existing residential), pre-1 July 2000 holdings, GST-free going concern or farmland acquisitions (special margin rules in s 75-11 apply -- often the vendor's acquisition cost carries through), and purchases that themselves used the margin scheme.
- **Margin** = consideration for the sale minus consideration for the acquisition (s 75-10(2)). Development, construction, and holding costs do NOT increase the acquisition consideration -- they are recovered only through ordinary ITCs.
- **Pre-1 July 2000 holdings:** the margin may instead be sale price minus an **approved valuation** of the property, generally as at 1 July 2000 (day of registration if registered later) -- s 75-10(3). An approved valuation must meet MSV 2020/1 (professional valuer, signed certificate, made by the required date). Valuations are refusal territory: R-AU-GP-2.
- **The purchaser gets NO input tax credit** on a margin scheme acquisition (s 75-20), and no tax invoice showing GST exists. Price the deal accordingly.
- **Flow-on:** because the purchaser's acquisition was not a fully-taxable-without-margin supply, the purchaser can itself use the margin scheme on a later taxable resale (fresh written agreement required). A full-GST purchase permanently kills margin eligibility for that interest.
- **RW interaction:** withholding on a margin scheme sale is 7% of the contract price, credited against the actual margin GST in the supplier's BAS -- over-withholding refunds through the BAS (Example 2).

## Section 5 -- Going concern (s 38-325) and the Division 135 clawback

A supply of a going concern is **GST-free** if ALL of:

1. the supply is for consideration;
2. the **recipient is registered** or required to be registered;
3. supplier and recipient have **agreed in writing** that the supply is of a going concern (on or before the day of supply);
4. the supplier supplies **all of the things necessary** for the continued operation of the enterprise; and
5. the supplier **carries on the enterprise until the day of the supply** (settlement).

GSTR 2002/5 is the operative ruling. The classic property case: sale of a **leased commercial building** -- the enterprise is leasing; "all things necessary" = the building plus the benefit of the existing lease(s). A building with the tenant already departed and no new lease in place generally fails; partially vacant buildings with active marketing of the vacancies can pass (GSTR 2002/5 paras 150-151). Benefits: no GST cash flow, and stamp duty bases in some states exclude GST. Risks: mis-classification means 1/11th of the whole price is owed with penalties -- verification is escalation territory (base skill R-AU-4).

**Division 135 clawback.** The GST-free treatment assumes the purchaser keeps making taxable/GST-free supplies. If the recipient of a going concern (or GST-free farmland) intends that some or all supplies through the enterprise will be **neither taxable nor GST-free** (input taxed -- residential rent is the classic), s 135-5 imposes an immediate **increasing adjustment**:

```
Increasing adjustment = 1/10 x supply price x proportion of non-creditable use
```

-- attributable to the purchaser's tax period of the acquisition. Later changes in actual use adjust again under s 135-10 via Div 129. A purchaser buying a tenanted office block GST-free and converting it to long-term apartments pays 1/10th of the full price to the ATO with no offsetting credit (Example 3). ALWAYS screen the purchaser's intended use before anyone signs a going concern clause.

## Section 6 -- Developers who rent unsold stock: apportionment and Division 129

The **build-to-sell-then-rent trap**: a developer claims full ITCs during construction (intended 100% taxable sales), then the market softens and unsold apartments are rented out. Renting is input taxed, so the extent of creditable purpose has changed -- Div 129 requires **increasing adjustments**.

- **Adjustment periods (s 129-20):** the first is the tax period ending on or nearest 30 June starting at least 12 months after the acquisition's tax period; thereafter annually. Number of periods for non-business-finance acquisitions: **2** where the GST-exclusive value is $5,000 or less; **5** where more than $5,000 but under $500,000; **10** where $500,000 or more. Apartment-scale construction acquisitions are almost always in the 10-period band -- a decade of annual true-ups.
- **Mechanic:** at each adjustment period, compare the ITC actually claimed (intended application) with the ITC that reflects **actual application** to date. Actual application below intended -> increasing adjustment (label 1A side); a later taxable sale within the adjustment periods lifts actual application and can produce decreasing adjustments.
- **Dual concurrent use:** while a rented apartment is still genuinely held for sale, the application is split between taxable-sale purpose and input-taxed renting. GSTR 2009/4 accepts fair and reasonable methods (e.g. expected sale proceeds vs total expected consideration, or time-based weighting). Method choice is judgement-heavy -- compute a sketch, flag the method, and escalate sign-off.
- **Interaction with the 5-year rule:** if the developer stops marketing and rents solely, the 5-year clock starts; once premises stop being new, the eventual sale is input taxed and adjustments trend the credits toward nil. Selling while still new keeps the sale taxable (and RW applies).

**AUDIT FLASH POINT -- enterprise vs mere realisation (MT 2006/1).** One-off subdivisions are the other side of this coin: an "enterprise" includes an isolated venture in the form of an adventure in the nature of trade (s 9-20), but the **mere realisation** of a capital asset -- even enhanced by subdivision -- is not one. MT 2006/1 paras 262-302 factors pointing TO an enterprise: change of purpose for which the land is held; additional land acquired; land brought to account as a business asset; a coherent plan for subdivision; a business organisation (manager, office, borrowings); interest on borrowed development funds claimed; development beyond what council approval minimally requires; buildings erected. The retiree subdividing the family block into three lots with minimum-compliance works and no borrowings is ordinarily realising a capital asset: no enterprise, no registration, no GST, no RW -- and s 188-25 excludes capital asset disposals from projected GST turnover, so the $75,000 threshold is not tripped by the sale itself. But add borrowings, staged construction, and a sales office, and the same block becomes an enterprise making taxable supplies of potential residential land -- with an isolated-transaction registration obligation the client never saw coming. Work the factors in writing every time; never assume either way.

## Section 7 -- Worked examples

### Example 1 -- New residential sale with RW and the BAS credit

DevCo (registered, quarterly) sells a newly built townhouse for $880,000, margin scheme not applied. Contract notification: withholding $80,000 (1/11th). Purchaser pays a $88,000 deposit; her conveyancer lodges Form one (gets PRN/LRN), lodges Form two two days before settlement, and at settlement pays the ATO $80,000 and DevCo the balance:

```
$880,000 - $88,000 deposit - $80,000 RW = $712,000 to DevCo at settlement
```

DevCo's BAS for the settlement quarter: G1 $880,000; 1A $80,000. The $80,000 sits in DevCo's GST property credits account and transfers on lodgment -- net GST cash on the sale: nil. DevCo must NOT report only the net price or skip 1A "because the purchaser already paid it".

### Example 2 -- Margin scheme with a 1 July 2000 valuation

HoldCo, registered since 1998, has owned a vacant residentially-zoned lot since 1995. In 2026-27 it sells the lot for $1,650,000 to an unregistered individual; the contract contains a margin scheme agreement. An approved valuation (MSV 2020/1-compliant, signed certificate) fixes the 1 July 2000 value at $400,000.

```
Margin = $1,650,000 - $400,000            = $1,250,000
GST    = $1,250,000 x 1/11                = $113,636 (vs $150,000 without the margin scheme)
RW     = 7% x $1,650,000 (potential residential land, margin scheme) = $115,500
BAS: G1 $1,250,000 margin-basis reporting per ATO instructions; 1A $113,636
Credit $115,500 - liability $113,636      = $1,864 refund to HoldCo
```

The purchaser has no ITC (s 75-20) but keeps margin scheme eligibility for any future taxable resale.

### Example 3 -- Going concern sale, purchaser converts to residential rental (Div 135)

VendorCo sells a fully tenanted office building for $3,300,000, GST-free under s 38-325 (both parties registered, written going concern clause, leases assigned, enterprise carried on to settlement). BuyerCo intends to convert the building entirely to long-term residential apartments for rent -- 100% input-taxed use.

```
Increasing adjustment (s 135-5) = 1/10 x $3,300,000 x 100% = $330,000
```

payable in BuyerCo's tax period of acquisition, with no offsetting credit. Had BuyerCo intended 40% continued commercial letting / 60% residential: 1/10 x $3,300,000 x 60% = $198,000, with later actual-use changes adjusted via s 135-10 and Div 129. The "GST-free" label on the contract saved VendorCo nothing for BuyerCo -- screen intended use BEFORE settlement.

### Example 4 -- Developer rents unsold apartments (Div 129 sketch)

BuildCo claimed $55,000 of ITCs per apartment on development costs of $550,000 (GST-exclusive) each -- >= $500,000, so **10 adjustment periods**. Four apartments remain unsold at completion (Feb 2027) and are rented from March 2027 while still listed for sale. At the first adjustment period (June 2028 quarter), BuildCo's fair-and-reasonable method (GSTR 2009/4, expected-consideration basis) puts actual application at 80% creditable:

```
Increasing adjustment = 4 x $55,000 x (100% - 80%) = $44,000
```

Repeated (recomputed on cumulative actual use) at each of the remaining adjustment periods. If an apartment sells as new residential premises in 2029, that sale is taxable (RW applies) and later periods can throw off decreasing adjustments; if BuildCo instead delists and rents solely for 5+ years, the premises stop being new, the sale becomes input taxed, and the credits unwind toward nil. Method selection and the register need tax agent sign-off -- sketch, flag, escalate.

### Example 5 -- Subdivision enterprise assessment

Margaret, 68, retired, subdivides her 4,000 m2 home block (owned 30 years) into three lots, keeping the house lot. Works: only what council requires (survey, one access driveway, utility connections), funded from savings; lots listed with a local agent. MT 2006/1 factors: no change of purpose beyond realisation, no extra land bought, no business organisation, no borrowings, minimum-compliance development, nothing built. **Conclusion:** mere realisation of a capital asset -- no enterprise, no GST registration (s 188-25 keeps the proceeds out of projected turnover), sales out of scope, no RW; the standard contract's supplier notification states "no withholding required". **Contrast:** had Margaret borrowed $900,000, built three houses and run the sales campaign through a site office, the venture is an enterprise; registration is required regardless of her retirement, the house sales are taxable supplies of new residential premises, and purchasers withhold 1/11th at settlement.

## Section 8 -- GL sweep library

Property GST problems surface in the ledger before anyone mentions them:

| GL pattern | Likely issue | Action |
|---|---|---|
| Settlement statement line "GST withholding paid to ATO" | RW credit must be reconciled, not treated as GST paid | Report full price G1 / actual GST 1A in the settlement period; trace the credit in the GST property credits account |
| Land or building purchase with no GST in the price | Unregistered vendor, input-taxed, going concern, or margin scheme purchase -- no ITC, but margin eligibility may exist | File the contract; record vendor's GST status and margin/going-concern clauses -- they control resale treatment |
| Contract labelled "GST-free going concern" | s 38-325 conditions + Div 135 exposure unverified | Evidence all five conditions; screen intended use; escalate (base skill R-AU-4) |
| "Plus GST" / "GST inclusive" price clause disputes | Consideration ambiguity -- output GST at stake | Legal question: refuse drafting (R-AU-GP-1); compute both readings for the reviewer |
| Council contributions, DA fees, headworks charges | Most are Div 81 exempt taxes/fees -- no GST despite invoice look | Check Div 81 and regulations before claiming any ITC |
| Valuation, survey, legal fees during development | Creditable only to extent of taxable-sale purpose | Apportion if any letting is planned; feed the Div 129 register |
| Rental income appearing in a developer's TB | Build-to-sell-then-rent: Div 129 trigger, 5-year clock, ITC apportionment | Open an adjustment-period register per acquisition (Section 6) |
| Forfeited purchaser deposits | Div 99: forfeiture is consideration -- GST event for taxable-supply intent | Output GST 1/11th on forfeiture; do not book as GST-free windfall |
| Stamp duty on acquisitions | Never creditable -- state tax, no GST | Cost base only; exclude from GST workings |

## Section 9 -- Refusal catalogue (property)

If a trigger fires: stop, output the message, escalate. These sit on top of the base skill's R-AU-1 to R-AU-5.

- **R-AU-GP-1 -- Contract clause drafting.** Trigger: any request to draft, amend, or "fix" a margin scheme clause, going concern clause, GST gross-up, or supplier notification wording. Message: "GST clauses in land contracts are legal drafting with settlement-critical consequences -- a defective margin scheme or going concern clause changes the tax by 1/11th of the price and cannot always be repaired after settlement. Please have the clause drafted or reviewed by a property lawyer; a registered tax agent can confirm the GST position it needs to achieve."
- **R-AU-GP-2 -- Margin scheme valuations.** Trigger: any request to estimate, produce, or bless a valuation (especially as at 1 July 2000) for Div 75. Message: "Margin scheme valuations must be approved valuations meeting MSV 2020/1, made by a professional valuer with a signed certificate. I cannot estimate historical land values. Please engage a registered valuer and have a registered tax agent confirm the method and date."
- **R-AU-GP-3 -- GST grouping / joint venture property structures.** Trigger: property held or moved within a Div 48 GST group or Div 51 joint venture, or restructure proposals. Message: "Intra-group and joint venture supplies have special rules (including disregarded supplies that preserve 'new' status under s 40-75(2A)). This requires structure-level advice from a registered tax agent."
- **R-AU-GP-4 -- Commercial residential classification.** Trigger: hotels, motels, boarding houses, serviced apartments, student accommodation, caravan parks -- any question of whether premises are commercial residential. Message: "Commercial residential classification under GSTR 2012/6 is fact-intensive and heavily contested; it flips supplies between taxable, input taxed, and the Div 87 concession. Please escalate to a registered tax agent."
- **R-AU-GP-5 -- Retirement villages.** Trigger: retirement village entry payments, deferred management fees, serviced apartments in villages. Message: "Retirement village GST sits under its own rulings and concessions and interacts with state retirement villages legislation. Out of scope -- specialist advice required."
- **R-AU-GP-6 -- Government development agreements and long-term leases.** Trigger: development leases/agreements with government, 99-year Crown leases, build-to-rent concessions, Div 81 edge cases. Message: "Supplies under development arrangements with government (GSTR 2015/2) and long-term lease structures have bespoke GST outcomes. Please escalate to a registered tax agent."

## Section 10 -- Reading guide and onboarding fallback

### Reading guide

1. **Classify the premises first** (Section 2) -- new vs existing vs commercial vs potential residential land controls everything downstream: taxability, ITCs, RW, and which concessions are even available.
2. **The contract is the primary document.** Margin scheme agreements, going concern clauses, and supplier notifications all live in it; sight the executed clause, never a summary, and never rely on the agent's covering email.
3. **Dates are unforgiving:** margin scheme agreement on or before settlement; going concern agreement and carry-on to the day of supply; Form two within the 2-business-day window; RW paid at settlement. Late fixes need the Commissioner's discretion or don't exist.
4. **Withholding is not the liability.** RW is a payment plumbing change -- the BAS always self-assesses actual GST (full 1/11th or margin), and the credit arrives separately. Reconcile the GST property credits account every settlement.
5. **Screen intent, not just facts:** Div 135 and Div 129 both turn on what the buyer/developer *intends* -- ask, document, and re-test at every adjustment period.
6. **The enterprise question comes before registration**, and registration comes before any of this machinery applies. For one-off subdivisions, write up the MT 2006/1 factors before touching the GST treatment.

### Onboarding fallback

If the client provides only a settlement statement and a trial balance:

1. Sweep the GL per Section 8 -- pull every land/building line, RW line, and "GST-free" contract reference
2. Request the full contract (including annexures) for every property transaction in the period; classify per Section 2 with all clause statuses UNKNOWN flagged
3. Compute RW, margin, Div 135 and Div 129 exposures on stated figures, assumptions listed
4. **Flag:** "Property GST positions built from settlement statement and TB only. Contracts, margin scheme agreements, going concern clauses, supplier notifications, valuations, and the purchaser's intended use are unverified. A registered tax agent must confirm every classification before lodgment."

## Section 11 -- Reference material

### Prohibitions

- NEVER treat a sale as margin-scheme eligible without sighting the written agreement AND the supplier's acquisition history
- NEVER let a purchaser claim an ITC on a margin scheme acquisition (s 75-20) -- there is no tax invoice with GST for a reason
- NEVER assume the 5-year rule is met from rental duration alone -- "only used" fails if the property was marketed for sale at any point
- NEVER sign off a going concern position without all five s 38-325 conditions evidenced, and never without a Div 135 intended-use screen
- NEVER net the RW amount against 1A -- report full GST; the credit arrives separately (s 18-60)
- NEVER apply 5 adjustment periods to acquisitions of $500,000 or more -- s 129-20(3) gives them 10
- NEVER conclude "mere realisation" or "enterprise" without documenting the MT 2006/1 factors
- NEVER confuse FRCGW (15%, income tax, from 1 Jan 2025) with GST at settlement -- separate forms, both may apply
- NEVER present computed figures as definitive

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| Taxable supply; enterprise | GST Act ss 9-5, 9-20; turnover s 188-25 |
| Residential premises: input taxed | GST Act ss 40-35, 40-65, 40-70; GSTR 2012/5 |
| New residential premises; 5-year rule | GST Act s 40-75; GSTR 2003/3 (as amended, current) |
| GST at settlement | TAA 1953 Sch 1 ss 14-250, 14-255, 18-60; LCR 2018/4; ato.gov.au "GST at settlement" (QC 55431, updated 4 June 2025) and supplier guide (QC 56252, updated 9 July 2026) |
| Margin scheme | GST Act Div 75 (ss 75-5, 75-10, 75-11, 75-20, 75-22); GSTR 2006/7 (pre-1 July 2000 acquisitions), GSTR 2006/8 (post-1 July 2000 -- both current); MSV 2020/1; PS LA 2005/16 |
| Going concern | GST Act s 38-325; GSTR 2002/5 (current, as amended) |
| Div 135 clawback | GST Act ss 135-5, 135-10 |
| Change of use adjustments | GST Act Div 129 (s 129-20 adjustment periods); GSTR 2009/4 (new residential premises held for sale and rented); GSTR 2006/4 (apportionment) |
| Enterprise vs mere realisation | MT 2006/1, esp. paras 262-302 |
| Commercial residential | GSTR 2012/6; Div 87 |
| FRCGW (contrast) | TAA 1953 Sch 1 Subdiv 14-D: 15%, no threshold, from 1 January 2025 |
| Penalty unit | $364 from 1 July 2026 (Crimes Act 1914 s 4AA, as indexed) |

### Test suite

**Test 1:** New townhouse $880,000, no margin scheme -> RW $80,000; supplier BAS G1 $880,000 / 1A $80,000; credit $80,000.

**Test 2:** Margin sale $1,650,000, 1 July 2000 valuation $400,000 -> margin $1,250,000; GST $113,636; RW 7% = $115,500; refund $1,864.

**Test 3:** Apartment rented 6 years but listed for sale in year 2 -> still NEW residential premises (s 40-75(2) "only used" fails); sale taxable, RW applies.

**Test 4:** Going concern purchase $3,300,000, 100% intended residential rent -> Div 135 increasing adjustment $330,000.

**Test 5:** Developer acquisition $550,000 GST-exclusive -> 10 adjustment periods; ITC $55,000; actual application 80% at first period -> increasing adjustment $11,000.

**Test 6:** Property bought with full 10% GST, full ITC claimed -> margin scheme NOT available on resale (s 75-5(2)); bought under margin scheme -> available again.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
