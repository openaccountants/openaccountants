---
name: au-managed-funds-amit
description: >
  Use this guide for the member side of an Australian attribution managed investment
  trust (AMIT) in the 2026-27 income year: resident individuals, and other entities
  through the guides it routes to, holding units in managed funds or ETFs that are
  AMITs. Covers the AMMA statement and its timing, determined member components and
  character flow-through, the discount capital gain and franking gross-ups, the
  annual cost base increase or decrease, CGT event E10 and the cash-to-attribution
  bridge. Trigger on 'AMIT', 'AMMA statement', 'managed fund tax statement',
  'ETF distribution', 'cost base adjustment' or 'CGT event E10'.
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27"
tier: 2
last_updated: 2026-11-11
version: 0.1
review_status: pending_review
verified_by: pending
license: FSL-1.1-ALv2
depends_on:
  - workflow-base
---

# Australian Managed Funds and AMITs: Member Taxation v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide turns an AMIT member annual (AMMA) statement into member-level workpapers: what the member is taxed on, in which character and how the unit cost base moves. It loads on top of `workflow-base`.

**Covered:**

- Australian resident members holding units in an AMIT on capital account.
- The AMMA statement: who must give it, when, replacement statements and its required contents (ss 276-455, 276-460 of the ITAA 1997).
- Character flow-through of determined member components (s 276-80) and the specific rules for discount capital gains and the franking credit gross-up (s 276-85).
- The annual AMIT cost base net amount, the resulting increase or decrease to the cost base and reduced cost base, and CGT event E10 (ss 104-107A to 104-107E).
- A bridge between cash received, amounts reinvested and amounts attributed.

**Not covered (routed elsewhere):**

- The member's capital gain calculation after gross-up, capital losses, the discount for each entity type, a later sale of units and the changes for CGT events from 1 July 2027 (including a Bill that would bring AMITs into the new regime): `au-capital-gains`.
- Foreign income components and the foreign income tax offset limit: `au-foreign-income`.
- Trusts that are not AMITs, including tax-deferred amounts and CGT event E4: `au-trust-distributions` and `au-capital-gains`.
- A self-managed super fund as the member: `au-smsf`. A company as the member, and franking at company level: `au-company-tax`.
- The return labels for the year: `au-individual-return`.
- Trustee-side AMIT work, foreign resident members and withholding, units held as revenue assets and franking credit entitlement opinions (refusals below).

**Period coverage.** Law as at 2 November 2026: ITAA 1997 compilation 268 (in force from 1 October 2026). The Federal Register lists a later compilation from 1 December 2026 that was not yet published when read; recheck before relying on this guide after that date. The figures apply to the 2026-27 income year (1 July 2026 to 30 June 2027).

## Ask the client first

1. The member's identity, entity type and residence for the income year, and whether the units are held on capital account.
2. Every AMMA statement for the year for each fund, with any replacement statement and its date. A fund that issues a standard trust distribution statement instead is probably not an AMIT for that year; ask.
3. The registry or platform transaction history: units held at the start and end of the year, acquisitions (including distribution reinvestment), disposals and dates.
4. The opening cost base and reduced cost base per parcel, carried from the prior year's workpapers, with the prior years' AMIT adjustments.
5. Cash distribution statements and bank records, including any distribution declared for June but paid in July.
6. The member's own capital losses (current year and carried forward) and residence history, for the hand-off to `au-capital-gains`.
7. Whether any return for the year has been lodged, because a replacement statement may require an amendment.

## The method, step by step

### Key figures

Every figure below was read on 2 November 2026 in ITAA 1997 compilation 268 unless another source is named; full URLs are in Sources.

| Item | Value | Source |
| --- | --- | --- |
| AMMA statement deadline | No later than 3 months after the end of the income year | s 276-455(2) |
| Replacement statements | A trustee that gave statements on time does not breach the deadline by later giving replacement statements | s 276-455(4) |
| No statement needed | Where all of the member's determined member components are nil and the cost base net amount of all its interests is nil | s 276-455(3) |
| Outer limit | A statement given more than 4 years after the end of the income year is not an AMMA statement | s 276-460(3) |
| Statement contents | Amount and character of each member component, and the trustee's reasonable estimate of the cost base excess or shortfall for the member's unit or interest | s 276-460(2) |
| Discount capital gain component | Treated as double the component's amount (the trustee's discounted figure, not a grossed-up line) for s 276-80 | s 276-85(3)-(4) |
| Cost base excess (decrease) | Reduce the cost base and reduced cost base by the excess, or to nil if the excess is larger than the cost base | s 104-107B(2) |
| Cost base shortfall (increase) | Increase the cost base and reduced cost base by the shortfall | s 104-107B(3) |
| Timing of the adjustment | Just before the end of the income year, or just before a CGT event that happens to the unit during the year | s 104-107B(4) |
| CGT event E10 gain | The excess over the cost base (or the whole excess if the cost base is already nil); no capital loss can arise | s 104-107A(1), (3) |
| E10 exception | A gain is disregarded for units acquired before 20 September 1985 | s 104-107A(4) |
| Discount availability for an E10 gain | E10 is not in the list of events whose gains cannot be discount capital gains; the 12-month holding test applies to the unit | s 115-25(1), (3) |
| CGT discount for an individual | 50% for a discount capital gain from a CGT event before 1 July 2027 where ss 115-105 and 115-110 do not apply; other entities and later events: `au-capital-gains` | s 115-100(aa) |

### Step 1: Confirm the regime for the year

Apply this guide only where the fund gives an AMMA statement for the income year. The statement replaces the standard distribution statement other investment trusts give (ATO, Attributing amounts to members). An ETF or managed fund name, or a distribution receipt, does not prove AMIT status. If there is no AMMA statement, stop and route to `au-trust-distributions`; never apply the AMIT cost base rules by analogy.

### Step 2: Control the statement versions

List each AMMA statement with its date. Use the latest statement for the year and record the superseded figures, so each component is used once. A replacement received after lodgment goes to `au-amending-individual-income-tax-return-period`.

### Step 3: Schedule every component by character

Record each determined member component as the statement characterises it: Australian income by type, franked distributions and the franking credit gross-up, foreign income and its foreign tax, capital gains by type, exempt and non-assessable non-exempt amounts, and tax offsets. The member is treated as having derived each amount in its own right and in the same circumstances as the AMIT, so the character carries through; the trustee's residence and place of central management are not part of those circumstances (ss 276-80(2), 276-85(7)). Taxable attribution can differ from cash; do not force one to match the other (ATO, Attributing amounts to members).

### Step 4: Gross up discount capital gains, then hand off

Double each discount capital gain component as the trustee determined it, the amount after the trust's discount (s 276-85(4)). AMMA statements need not follow an ATO-approved form, so a statement may also print a grossed-up figure: never double a line the statement labels grossed up, and ask the fund when the label is unclear. The member then applies its own capital losses and its own discount, if any, in `au-capital-gains`. The trust's 'discounted' label does not decide whether the member is entitled to a discount, or to which percentage. For an individual and a CGT event before 1 July 2027, the method in Case 3 uses the 50% in s 115-100(aa).

### Step 5: Franking credits and tax offsets

Take franking credits and other tax offsets as attributed (s 276-80(4)-(6)), with the franking credit gross-up under s 276-85(5)-(6). Whether the member is a qualified person entitled to the franking credit is outside this guide (R-AU-AMIT-4).

### Step 6: Bridge cash, reinvestment and attribution

Prepare one bridge per fund: cash entitlements for the year, amounts reinvested, attributed components and the cost base net amount. Explain every difference. A distribution reinvested in new units is an acquisition of a new parcel at the registry's date and amount; keep it separate from the annual cost base adjustment so the same amount is not added twice. Its cost base is settled in `au-capital-gains`.

### Step 7: Roll the cost base forward per parcel

For each parcel:

1. Start from the opening cost base and reduced cost base.
2. Take the cost base net amount for the year from the AMMA statement, which states the trustee's estimate (s 276-460(2)(b)). Allocate it to parcels on the per-unit basis the statement uses.
3. Reconcile the statement's amount to the statutory parts where the statement shows them. The reduction amount is money and the market value of property the member started to have a right to receive in the year, plus tax offsets attributed under s 276-80 (s 104-107D(1)). The increase amount is attributed assessable and non-assessable non-exempt amounts (disregarding the AMIT's net capital gain), plus capital-gain components taken into account under s 276-80 (s 104-107E). The net amount is the difference (s 104-107C).
4. Apply an excess as a decrease and a shortfall as an increase, to both the cost base and the reduced cost base (s 104-107B).
5. If the excess is larger than the cost base, reduce both to nil and record a CGT event E10 gain (s 104-107A). Do not stop at nil without recording the gain.
6. For units sold during the year, the adjustment applies just before the sale (s 104-107B(4)(b)); include it in the disposal workings for `au-capital-gains`.

### Permitted factual defaults

| Missing fact | Default | Disclose |
| --- | --- | --- |
| Whether a newer replacement statement will issue | Use the latest statement held | A later replacement may need an amendment |
| Brokerage on reinvested units | Omit it from the parcel's cost base | Cost base understated by the omitted cost |

No default is permitted for AMIT status, the cost base net amount, its direction, an opening cost base, parcel dates or residence. Return Needs Input for each.

### Working paper additions

Add to the base outputs: (1) a statement version log; (2) a component schedule by character; (3) the cash, reinvestment and attribution bridge; (4) a per-parcel cost base roll-forward showing each excess, shortfall and E10 gain.

## Worked cases

All facts are hypothetical. The member is an Australian resident individual holding units on capital account for the whole of 2026-27, with the AMMA statement as described.

### Case 1: Annual cost base decrease (2026-27)

A member holds one parcel of 10,000 units, acquired on 1 August 2023, with an opening cost base of $20,000. The 2026-27 AMMA statement shows cash entitlements of $1,100, attributed tax offsets of $100 (franking credits and foreign tax), attributed non-capital amounts of $700, capital-gain components counted under s 104-107E(4) of $400, and an estimated cost base excess of $100.

```oa-check
name: AMIT annual cost base net amount and parcel roll-forward 2026-27
inputs:
  opening_cost_base: 20000
  cash_entitlements: 1100
  attributed_tax_offsets: 100
  non_capital_attributed_amounts: 700
  capital_gain_components: 400
  statement_excess: 100
steps:
  - reduction_amount: cash_entitlements + attributed_tax_offsets
  - increase_amount: non_capital_attributed_amounts + capital_gain_components
  - net_excess: reduction_amount - increase_amount
  - statement_difference: net_excess - statement_excess
  - closing_cost_base: opening_cost_base - net_excess
expected:
  reduction_amount: 1200
  increase_amount: 1100
  net_excess: 100
  statement_difference: 0
  closing_cost_base: 19900
```

The statement reconciles to the statutory parts, so both the cost base and the reduced cost base fall by $100 just before the end of the 2026-27 income year (s 104-107B(2), (4)(a)). If the parts did not reconcile, record the difference and ask the fund before using either figure.

### Case 2: A decrease larger than the cost base: CGT event E10 (2026-27)

A second parcel of 500 units, acquired on 1 February 2019, has a cost base of $150 at 1 July 2026 after earlier decreases. The 2026-27 statement shows an excess of $400 for the parcel. The member has no capital losses.

```oa-check
name: AMIT cost base decrease exceeding cost base triggers CGT event E10 2026-27
inputs:
  opening_cost_base: 150
  statement_excess: 400
  discount_percent: 50
steps:
  - e10_capital_gain: statement_excess - opening_cost_base
  - closing_cost_base: max(0, opening_cost_base - statement_excess)
  - discounted_gain: e10_capital_gain - pct(e10_capital_gain, discount_percent)
expected:
  e10_capital_gain: 250
  closing_cost_base: 0
  discounted_gain: 125
```

The cost base and reduced cost base fall to nil and the member makes a $250 capital gain from CGT event E10, at the time of the reduction, just before the end of the 2026-27 income year (ss 104-107A(2)-(3), 104-107B(2)(a), (4)(a)). The units were held for more than 12 months and E10 is not excluded from the discount, so the individual's discount for an event before 1 July 2027 gives $125 (ss 115-25, 115-100(aa)). Next year's decreases start from nil and produce further E10 gains (s 104-107A(1)(b)(ii)).

### Case 3: Discount capital gain gross-up and the member's losses (2026-27)

The statement attributes a discount capital gain component of $300 and other capital gains of $100. The member has $250 of net capital losses carried forward.

```oa-check
name: AMIT discount capital gain gross-up and member losses 2026-27
inputs:
  discounted_gain_component: 300
  other_capital_gain_component: 100
  prior_net_capital_losses: 250
  discount_percent: 50
steps:
  - grossed_up_discount_gain: discounted_gain_component * 2
  - losses_used_on_other_gains: min(prior_net_capital_losses, other_capital_gain_component)
  - remaining_losses: prior_net_capital_losses - losses_used_on_other_gains
  - discount_gain_after_losses: grossed_up_discount_gain - remaining_losses
  - discount_amount: pct(discount_gain_after_losses, discount_percent)
  - net_capital_gain: (other_capital_gain_component - losses_used_on_other_gains) + discount_gain_after_losses - discount_amount
expected:
  grossed_up_discount_gain: 600
  losses_used_on_other_gains: 100
  remaining_losses: 150
  discount_gain_after_losses: 450
  discount_amount: 225
  net_capital_gain: 225
```

The $300 component is treated as $600 (s 276-85(4)). Losses go first against the gain that does not qualify for the discount, the ordering `au-capital-gains` sets out, and only then is the individual's discount applied. Skipping the gross-up would leave $150 of discount gain after losses and a $75 net capital gain, understating it by $150.

### Case 4: Attribution above cash: a cost base increase

A fund pays $300 in cash for the year but attributes $500 of assessable components, with no tax offsets or capital gains. The reduction amount is $300 and the increase amount $500, so the statement should show a $200 shortfall, which increases both the cost base and the reduced cost base (ss 104-107C(b), 104-107B(3)). The member is taxed on $500, not $300.

### Case 5: A replacement statement after lodgment

A fund issues a replacement AMMA statement in November 2027 that lifts attributed foreign income by $80. The original was given on time, so the fund has not breached s 276-455 (s 276-455(4)). The return already lodged on the original figures needs an amendment request through `au-amending-individual-income-tax-return-period`, and the foreign income goes to `au-foreign-income`.

### Case 6: Reinvestment counted twice

A member reinvests a $600 June distribution in 40 new units. The workpapers add $600 to the existing parcel's cost base and also record the new parcel at $600. Remove the addition to the old parcel: the reinvestment is a new parcel, and the old parcel moves only by the statement's cost base net amount.

## When to refuse or refer

Stop the affected calculation where a fact, condition or source in this guide is unresolved, and return Needs Input or refer it for qualified review.

| Code | Trigger | Message (verbatim) |
| --- | --- | --- |
| R-AU-AMIT-1 | Trustee-side work: choosing AMIT status, trust components, unders and overs, or a fair and reasonable attribution question | 'This guide covers members only. Trustee attribution and AMIT eligibility are specialist work; refer to the fund's tax adviser.' |
| R-AU-AMIT-2 | A foreign resident member, or MIT or non-resident withholding on the member's distributions | 'Foreign resident members are taxed through withholding rules this guide does not apply. I have recorded the statement components; refer to a qualified reviewer and au-foreign-income.' |
| R-AU-AMIT-3 | Units held as trading stock or revenue assets (s 104-107G) | 'Revenue-account holdings adjust the cost of the units under separate rules. Refer the treatment to a qualified reviewer.' |
| R-AU-AMIT-4 | A question whether the member is entitled to franking credits (holding period, qualified person or a Commissioner determination under s 276-90) | 'Franking credit entitlement is outside this guide. I have recorded the credits as attributed; a qualified reviewer must confirm entitlement.' |
| R-AU-AMIT-5 | No AMMA statement, or a fund whose AMIT status for the year is unclear | 'Without an AMMA statement I cannot apply the AMIT rules. Provide the fund's statement for the year or route to au-trust-distributions.' |
| R-AU-AMIT-6 | A disposal, deemed sale or cost base question for a CGT event on or after 1 July 2027 | 'The CGT rules change for events from 1 July 2027 and a Bill would change them again for AMITs. Route to au-capital-gains Section 9.' |

**Reviewer attention thresholds.** These are this guide's review settings, not statutory figures. Flag for reviewer attention regardless of confidence:

| Threshold | Why |
| --- | --- |
| Any CGT event E10 gain | The cost base is exhausted and every later decrease is a gain |
| A cost base decrease above 10% of a parcel's opening cost base in one year | Large returns of capital need the statement and registry checked |
| A cash-to-attribution difference above $5,000 for one fund | The bridge must explain it before lodgment |
| Any replacement statement received after lodgment | An amendment may be required |
| Statement parts that do not reconcile to its cost base net amount | The trustee's estimate may be wrong |

## Completion checklist

- [ ] Each fund's AMIT status for the year rests on an AMMA statement; non-AMIT funds were routed.
- [ ] The latest statement version was used and superseded figures were recorded once.
- [ ] Every component was scheduled by character and mapped to the year's return labels through `au-individual-return`.
- [ ] Discount capital gain components (the trustee's discounted amounts, not any grossed-up line) were doubled before the member's own losses and discount.
- [ ] The cash, reinvestment and attribution bridge explains every difference.
- [ ] Each parcel's cost base and reduced cost base moved by the statement's net amount, with any E10 gain recorded and no silent stop at nil.
- [ ] Reinvested distributions are separate parcels and were not also added to an existing parcel.
- [ ] Every figure used matches the key figures table and its source.

Change log: v0.1 (2 November 2026), first draft from Division 276 and ss 104-107A to 104-107G of ITAA 1997 compilation 268.

## Sources

All read on 2 November 2026; figures and dates rechecked against the same sources on 11 November 2026.

| Source | URL | Read on |
| --- | --- | --- |
| ITAA 1997, compilation 268 (from 1 October 2026), Volume 3: ss 104-107A to 104-107G (AMIT cost base adjustments and CGT event E10), 115-25, 115-100 | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html | 2 November 2026 |
| ITAA 1997, compilation 268, Volume 6: ss 276-10, 276-80, 276-85, 276-455, 276-460 | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html | 2 November 2026 |
| ATO, Attributing amounts to members (QC82269, last updated 23 July 2025): character retained, attribution can differ from cash, AMMA statement replaces the standard distribution statement, 3-month deadline | https://www.ato.gov.au/businesses-and-organisations/trusts/specific-rules-for-some-trusts/managed-investment-trusts/managed-investment-trusts-overview/attribution-managed-investment-trusts/attribution-method-for-managed-investment-trusts/attributing-amounts-to-members | 2 November 2026 |

Not yet confirmed: the 2026-27 return labels for AMIT components; the member-level treatment of each tax offset type; and any amendment in the ITAA 1997 compilation from 1 December 2026. No accountant has reviewed this draft.

Method adapted by its author from the `au-managed-fund-amit` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Copyright 2026 Ryan Duguid. From github.com/ryanduguid/australian-accounting-skills, FSL-1.1-ALv2. Copies and adaptations of this file must keep this notice.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
