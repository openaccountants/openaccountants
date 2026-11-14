---
name: au-restructure-rollovers
description: >
  Use this guide to assemble the evidence for, and work the consequences of, three Australian
  income tax restructure rollovers: the small business restructure roll-over (Subdivision 328-G
  ITAA 1997), the roll-over for an individual, trustee or all the partners transferring assets
  to a wholly-owned company (Subdivisions 122-A and 122-B) and the roll-over for interposing a
  company between a company or unit trust and its members (Division 615). Covers sole traders,
  partnerships, trusts and companies for 2026-27. Trigger on 'small business restructure
  roll-over', 'SBRR', 'incorporate my business', 'Div 122', 'interpose a holding company',
  'Div 615' or 'restructure rollover'.
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

# Australia Restructure Rollovers: Subdivision 328-G, Division 122 and Division 615 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide loads on `workflow-base` and fills its Section 7 slots for three rollovers in the *Income Tax Assessment Act 1997* (ITAA 1997):

- **Subdivision 328-G**, the small business restructure roll-over (SBRR): active assets moved between small business entities and related entities without a change in ultimate economic ownership.
- **Subdivisions 122-A and 122-B**: an individual or trustee (122-A), or all the partners in a partnership (122-B), disposing of assets to, or creating assets in, a company they wholly own, for non-redeemable shares.
- **Division 615**: the members of a company or unit trust exchanging all their interests for shares in a new interposed company.

For each it sets out the conditions as an evidence matrix, the cost base and pre-CGT consequences, the depreciating asset and trading stock links, who chooses and when, and the routing of everything else. It prepares work for a specialist; it never chooses the pathway.

**Not covered here; route to the guide that holds it:**

| Topic | Guide |
|---|---|
| Division 152 small business CGT concessions, including the Subdivision 152-E small business roll-over, the active asset test and the s 152-10(1A) passively held asset rule | `au-small-business-cgt` |
| CGT event register, cost base elements, the CGT discount, capital losses and the changes from 1 July 2027 (deemed sale of pre-CGT assets under s 112-175, indexation) | `au-capital-gains` (Section 9) |
| Transfer, landholder and business asset duty, including corporate reconstruction relief | `au-stamp-duty` |
| GST on the transfer, including supplies of a going concern | `au-gst-property`, `australia-gst` |
| Loans, payments and debt forgiveness by a private company to a shareholder or associate | `au-div7a` |
| Trust distributions, family trust elections in their distribution context and the proposed restructure roll-over out of discretionary trusts (Bills, not law) | `au-trust-distributions` (Rule 14) |
| Partnership reconstitution and trading stock elections on a change in partners | `au-partnerships` |
| Company tax rate, franking, losses and consolidation | `au-company-tax` |

Other roll-overs (Subdivision 124-N trust to company, Subdivision 126-A relationship breakdown, Subdivision 126-B wholly-owned group, Subdivision 126-G trust to trust, Division 125 demergers) are out of scope; refer them (R-AU-RR-5).

**Period coverage.** The rules below are the law as read on 2 November 2026 for transfers in the 2026-27 income year. Two law-change items affect this work:

1. **Enacted: pre-CGT status ends after 30 June 2027.** Section 112-175 applies to an asset that is a pre-CGT asset on 30 June 2027 and is still held when a realisation event happens on or after 1 July 2027 (s 112-175(1)). It then deems the asset sold just before, and reacquired on, 1 July 2027 at market value (or under an apportioning method); note 1 says the asset ceases to be a pre-CGT asset, and note 3 says any gain or loss on the deemed sale is disregarded. The pre-CGT inheritance rules in this guide (ss 328-460, 122-40(3), 122-55, 124-10(4), 615-65(2)) therefore matter for transfers up to 30 June 2027; for a later realisation, work the position in `au-capital-gains` Section 9.
2. **Bills, not law: a restructure roll-over out of discretionary trusts.** The ATO page (updated 3 November 2026) says the Government will introduce a time-limited (3 years) restructure rollover, available from 1 July 2027, to move assets out of discretionary trusts. The Treasury Laws Amendment (Tax Reform No. 3) Bill 2026 carries it: the APH page read on 11 November 2026 shows it introduced on 14 October 2026, third reading agreed in the House on 29 October 2026 and a referral to the Senate Economics Legislation Committee with its report due 13 November 2026. It was not law on 11 November 2026. Keep it out of the current-law matrix; label any scenario that models it (R-AU-RR-6).

## Ask the client first

Ask for these before building the matrix. Each feeds a named condition; a missing item leaves that condition open.

1. The proposed steps and draft documents, with the date and income year of each transfer, redemption or issue.
2. Entity charts before and after each step: every share, unit, partnership and trust interest, the capacity in which it is held, and each individual with ultimate economic ownership of each asset and their share.
3. Trust deeds and family trust election records for any discretionary trust (s 328-440).
4. Small business entity evidence for each party for the transfer year: aggregated turnover workings with affiliates and connected entities (s 328-110; s 328-430(1)(b)).
5. Residency of each party at the time of the transfer, and for trusts whether the trust is a resident trust for CGT purposes (ss 328-445, 122-25(6)-(7), 122-135(6)-(7), 615-20(3)).
6. An asset register: category (CGT asset, depreciating asset, pool asset, trading stock, revenue asset, excluded asset), acquisition date, cost base and reduced cost base evidence, adjustable value or pool balance, trading stock value at the start of the year and cost, pre-CGT status, business use and active asset evidence, and market value with valuer, basis and date.
7. Liabilities the transferee will assume, each tied to the asset or assets it relates to (ss 122-37, 615-65(5)-(6)).
8. The consideration: share class, number, rights and whether redeemable; any cash, loan or unpaid amount between the parties.
9. Post-transfer intentions for the next 3 years: any planned sale, new equity holder, change in use or private use of significant assets (s 328-435; LCR 2016/3).
10. Any earlier rollover affecting an asset, and the general ledger, fixed asset register and depreciation schedules to reconcile the register.

## The method, step by step

### Key figures and tests (read 2 November 2026)

| Item | Value | Source |
|---|---|---|
| Small business entity aggregated turnover threshold used by s 328-430(1)(b) | Less than $10 million for the previous year, or likely for the current year (s 328-110(1)), but not on the 'likely' limb if the 2 previous years were each $10 million or more (s 328-110(3)); also less than $10 million for the current year worked out at its end (s 328-110(4)); the ATO SBRR page states the $10 million figure | ITAA 1997 s 328-110; ATO SBRR page |
| SBRR start | Transfers from 1 July 2016 | ATO SBRR page; LCR 2016/3 para 3 |
| SBRR safe harbour period | 3 years after the transaction takes effect | ITAA 1997 s 328-435 |
| Depreciating assets under the SBRR | Automatic roll-over relief (s 40-340(1) item 8); CRP 2017/2 removes other direct income tax consequences for transfers on or after 8 May 2018 | ITAA 1997 ss 40-340, 328-430 (CRP note) |
| Pre-CGT cut-off | Acquired before 20 September 1985 | ITAA 1997 ss 328-460, 122-40(3), 124-10(4), 615-65(2) |
| Time to choose a Part 3-1 or Part 3-3 roll-over (includes Division 122) | By the day the income tax return for the year of the CGT event is lodged, or a further time the Commissioner allows | ITAA 1997 s 103-25(1) |
| Division 615 interposed company choice | Within 2 months after the completion time (choice that s 615-65 applies) or 28 days (consolidated group continuation), or further time the Commissioner allows; irrevocable | ITAA 1997 s 615-30(3) |
| Division 615 shares held by outsiders | No more than 5 shares, of a market value that makes it reasonable to treat the exchanging members as owning all the shares | ITAA 1997 s 615-25(3)(b) |
| Small business pool roll-over choice (simplified depreciation) | In writing, kept 5 years, made within 6 months of the end of the transferee's income year of the balancing adjustment event unless the ATO allows longer; all the transferor's general small business pool assets must be held by the transferee just after the events (s 328-243(2)) | ATO 'Rollover and restructure' page; ITAA 1997 s 328-243 |

**Choice timing not located.** Section 103-25 governs choices under Parts 3-1 and 3-3 only. Subdivision 328-G sits in Part 3-45 and Division 615 in Part 3-80; the sections read set no time for the SBRR choice (s 328-430(1)(f)) or a member's Division 615 choice (s 615-5(1)). The ATO page on choosing a CGT rollover states the general practice (choose by lodgment; the return is evidence; the choice cannot be changed). Record the provision relied on for each choice, or return Needs Input.

### Step 1: Map the structure and the steps

Draw the structure before and after each step: every entity, owner, interest and capacity, and each individual with ultimate economic ownership of each asset and their share. Make each step in the draft documents a row. Do not infer a step the documents do not show.

### Step 2: Build the evidence matrix

One column per candidate pathway, one row per condition below, each cell **evidenced**, **not evidenced** or **question**, with the document reference. A condition is never 'met' on the client's statement alone. The matrix compares pathways as evidence; a specialist chooses (R-AU-RR-1).

### Step 3: Subdivision 328-G conditions (s 328-430)

The roll-over is available for an asset the transferor transfers to one or more transferees if all of these hold:

1. **Genuine restructure of an ongoing business** (s 328-430(1)(a)). Test it on the facts with LCR 2016/3: indicators for (paras 6-7) include a bona fide arrangement to grow, adapt or cut compliance costs, continued use of the assets as active assets, continuity of key staff and trade, and a structure that professional advice would have produced; indicators against (para 10) include a preliminary step to realise assets, a winding down to transfer wealth between generations, extraction of wealth, artificial losses and permanent non-recognition of gain. Tax considerations alone do not disqualify (para 8), but an unduly tax-driven or contrived result does (para 9).
2. **Safe harbour alternative** (s 328-435). The restructure is taken to be genuine if, for 3 years after the transaction takes effect, there is no change in ultimate economic ownership of the significant assets transferred (other than trading stock), they stay active assets and there is no significant or material private use. A breach within 3 years removes only the safe harbour; the ordinary test still applies (LCR 2016/3 paras 25A, 48).
3. **Each party's status for the transfer year** (s 328-430(1)(b)): a small business entity, or an entity with an affiliate that is one, or connected with one, or a partner in a partnership that is one.
4. **No material change in ultimate economic ownership** (s 328-430(1)(c)): the same individuals, and each one's share, before and after. For a non-fixed trust that is a family trust, s 328-440 treats the test as met where every individual with ultimate economic ownership before and after is a member of the family group (Schedule 2F ITAA 1936).
5. **Eligible asset** (s 328-430(1)(d)): a CGT asset (other than a depreciating asset) that is an active asset when the transfer takes effect; for an affiliate or connected entity route, also one for which s 152-10(1A) is satisfied (see `au-small-business-cgt` method steps 2 and 3). Depreciating assets roll over under s 40-340(1) item 8. The ATO page says loans to shareholders are not active assets of the business.
6. **Residency** (s 328-445): an individual or company is an Australian resident; a trust is a resident trust for CGT purposes; a partnership has at least one resident partner; a corporate limited partnership is resident under s 94T ITAA 1936.
7. **Both sides choose** (s 328-430(1)(f)).
8. **Exclusion**: not available if the transferor or any transferee is an exempt entity or a complying superannuation entity (s 328-430(2)).

### Step 4: Subdivision 328-G consequences

- The transfer has no direct income tax consequences except as the Subdivision provides (s 328-450(1)). Its example says a company-to-shareholder transfer under the roll-over is not a Division 7A dividend; other Division 7A events still go to `au-div7a`.
- Each asset passes at its **roll-over cost** (s 328-455): a CGT asset's cost base just before the transfer; trading stock at its cost, or its value at the start of the income year if held as trading stock then; a revenue asset at the amount that gives no profit or loss.
- A pre-CGT CGT asset keeps pre-CGT status in the transferee (s 328-460), subject to s 112-175 after 30 June 2027.
- The ATO page says the transferee must hold the asset at least 12 months before a CGT event to claim the CGT discount, and for the 15-year exemption is treated as acquiring it when the transferor did; work both in `au-capital-gains` and `au-small-business-cgt`.
- **New membership interests issued as consideration** (s 328-465): first element of cost base = (roll-over costs of transferred assets that are neither depreciating nor pre-CGT assets + adjustable values of transferred depreciating assets - liabilities the transferee undertakes for the transferred assets) / number of membership interests; reduced cost base likewise. Reduce proportionately where the interests are only part of the consideration (s 328-465(2)). No consideration at all is required for the roll-over (ATO page).
- **Loss integrity** (s 328-470): a later capital loss on a direct or indirect membership interest in the transferor or transferee, or on interests issued under the transaction, is disregarded except to the extent shown to come from another matter.

### Step 5: Subdivision 122-A (individual or trustee to a wholly-owned company)

Conditions:

1. **Trigger event** in the s 122-15 table: A1 (dispose of a CGT asset or all the assets of a business to the company), D1, D2, D3 or F1. Note 3 says Subdivision 328-G may also be available.
2. **Consideration only** non-redeemable shares, plus, for a disposal, the company undertaking to discharge liabilities in respect of the asset or assets (s 122-20(1)-(2)).
3. **Market value test**: the shares' market value is substantially the same as the assets' market value less those liabilities (s 122-20(3)); disregard a difference caused only by possible liabilities attaching to the assets (s 122-20(4)).
4. **Ownership**: the transferor owns all the shares just after the trigger event, in the same capacity as the assets were owned (s 122-25(1) and note).
5. **Excluded assets** (s 122-25(2)): collectables, personal use assets, valour decorations (unless paid for), and registered emissions units, and for a single-asset disposal also precluded assets (depreciating assets, trading stock, film copyright interests under s 118-30, registered emissions units: s 122-25(3)) and assets that become the company's trading stock. For a disposal of all the assets of a business, an asset that becomes the company's trading stock is excluded unless it was already the transferor's trading stock.
6. **Company not exempt** for the income year (s 122-25(5)).
7. **Residency** (s 122-25(6)-(7)): both resident (or, for a trust, a resident trust and a resident company), or each asset and the shares are taxable Australian property; otherwise refer (R-AU-RR-3).
8. **Liability cap** (s 122-35): for a single post-CGT asset, liabilities cannot exceed its cost base (pre-CGT: market value); for all the assets of a business acquired post-CGT, the sum of the precluded assets' market values and the other assets' cost bases (pre-CGT assets: market value). A liability not tied to a specific asset (an overdraft) is in respect of all the business assets, and a liability over several assets is apportioned by market value (s 122-37).

Consequences:

- The capital gain or loss is disregarded (ss 122-40(1), 122-45(1)).
- Single post-CGT asset: each share's first element of cost base = (asset's cost base - liabilities assumed) / number of shares (s 122-40(2)). Pre-CGT asset: the shares are pre-CGT (s 122-40(3)).
- All the assets of a business, all post-CGT: each share's first element = (market values of precluded assets + cost bases of the other assets - liabilities assumed for all of them) / number of shares (s 122-50). All pre-CGT and mixed cases: ss 122-55 and 122-60 work out how many shares are pre-CGT by market value; compute only with every market value evidenced.
- Depreciating assets: automatic roll-over relief under s 40-340(1) item 1, disregarding s 122-25(3) for that purpose (s 40-340(2)(b)). Trading stock: Division 122 gives it no roll-over (s 122-45 note 3 points to Division 70). A disposal outside the ordinary course of business includes the item's market value in the transferor's assessable income (s 70-90(1)) and the company is treated as buying it for that amount (s 70-95). Section 70-100 needs an entity that owned the item beforehand to still have an interest in the item (s 70-100(1)(b)); route any claim that it applies to the reviewer.

### Step 6: Subdivision 122-B (all the partners to a wholly-owned company)

The partnership version mirrors Subdivision 122-A, tested **for each partner**: the s 122-125 trigger events; consideration only non-redeemable shares plus liabilities assumed (s 122-130(1)-(2)); each partner's shares substantially equal in market value to that partner's interests less liabilities (s 122-130(3)); the partners own all the shares just after, each in the same capacity as they held their interests (a trustee partner receives shares as trustee) (s 122-135(1)-(2)); the same excluded assets, exempt-company and residency rules (s 122-135(3)-(7)); and the per-partner liability caps (s 122-140). Consequences: each partner's gain or loss is disregarded (s 122-150); post-CGT interests give each share a first element of (sum of the partner's interests' cost bases - liabilities) / the partner's shares (s 122-155(1)); pre-CGT interests give pre-CGT shares (s 122-155(2)); mixed interests use s 122-160. Where the partners dispose of their interests in all the assets of a business, each partner's gain or loss is disregarded (s 122-170) and, for post-CGT interests, the first element = (the market values of the partner's interests in the precluded assets + the cost bases of the partner's interests in the other assets - liabilities assumed for all of them) / the partner's shares (s 122-180(1)(a)); all pre-CGT interests give pre-CGT shares, or only a market-value proportion of them where any asset is precluded (s 122-185); mixed interests use s 122-190. Depreciating assets: s 40-340(1) item 2. Partnership questions beyond these conditions go to `au-partnerships` (its R-AU-PT-5 sends rollover work here).

### Step 7: Division 615 (interposing a company)

Conditions:

1. **Membership** (s 615-5(1)(a)-(b)): the taxpayer is a member of a company or unit trust (the original entity) and, with at least one other entity, the exchanging members own all its shares or units.
2. **Exchange** (s 615-5(1)(c)): under a scheme for reorganising its affairs, the exchanging members dispose of all their shares or units to the interposed company in exchange for shares in it and nothing else. Section 615-10 covers the alternative where the interposed company acquires some interests first and the rest are redeemed or cancelled for its shares.
3. **Completion** (s 615-15): the interposed company owns all the shares or units in the original entity immediately after the completion time.
4. **Proportionality** (s 615-20(1)-(2)): each exchanging member owns a whole number of interposed company shares, in the same percentage as their interests disposed of, and the market value ratios before and after are equal.
5. **Residency** (s 615-20(3)): the member is an Australian resident, or a foreign resident whose interests before and shares after are taxable Australian property.
6. **Interposed company shares** (s 615-25): not redeemable; held from issue until at least the completion time; immediately after, the exchanging members own all the shares, or outsiders own no more than 5 shares of a market value that makes it reasonable to treat the members as owning all of them.
7. **Interposed company choice** (s 615-30): it must choose that s 615-65 applies, within 2 months after the completion time; where a consolidated group continues with it as head company, it must instead choose continuation within 28 days (refer: R-AU-RR-4). The choice cannot be revoked; the way the company prepares its returns is sufficient evidence.

Consequences:

- **Members** (s 615-40, applying Subdivision 124-A): the capital gain or loss is disregarded; each new share's first element of cost base = total cost bases of the original interests / number of new shares (ss 124-10(3), 124-15(3)); pre-CGT interests give pre-CGT shares, with the mixed-holding count in s 124-15(5)-(6).
- **Interposed company** (s 615-65): its shares or units in the original entity take a first element of cost base equal to the total cost bases of the original entity's post-CGT assets less its liabilities in respect of them (s 615-65(4)); where the original entity holds pre-CGT assets, a market-value proportion of the interests is treated as pre-CGT (s 615-65(2)-(3)). A liability not tied to specific assets is in respect of all of them, and one over several assets is apportioned by market value (s 615-65(5)-(6)). The interposed company's cost base therefore does not follow the members' cost bases.
- The underlying business assets stay in the original entity; Division 615 moves no business asset, so it carries no depreciating asset or trading stock transfer. Section 615-60 disregards the trading stock exemption in s 118-25 for the Division.

### Step 8: Depreciating assets, pools and trading stock

Record for each pathway how each asset category moves. SBRR: depreciating assets under s 40-340(1) item 8 (and CRP 2017/2); trading stock and revenue assets at roll-over cost (s 328-455). Division 122: depreciating assets under s 40-340(1) items 1 and 2; trading stock at market value under ss 70-90 and 70-95, with no roll-over. Small business pool assets under the simplified depreciation rules: the ATO page says the transferee takes over the pool, the pool deduction for the change year is split equally, and both parties choose in writing within the 6-month window in the key figures table; the transferee must hold all the transferor's pooled assets just after (s 328-243(2)). A missing adjustable value or pool balance leaves the share cost base open.

### Step 9: Choices, anti-avoidance and the announced trust measure

Record who must choose each roll-over, under which provision and by when (key figures table). Making a choice is the taxpayer's decision; an extension of time is a private ruling application (ATO choice page; R-AU-RR-8). The ATO SBRR page says the general anti-avoidance rule can still apply to a scheme that meets the roll-over conditions (PS LA 2005/24): flag Part IVA for the specialist on every pathway (R-AU-RR-2). Keep the proposed discretionary trust roll-over out of the current-law matrix (Scope, item 2).

### Step 10: Route the consequences

Duty to `au-stamp-duty`; GST and going concern treatment to `au-gst-property` and `australia-gst`; private company loans, payments and forgiveness to `au-div7a`; Division 152 concessions to `au-small-business-cgt`; the CGT event register, post-roll-over cost bases, discount and 2027 transition to `au-capital-gains`; trust deed and distribution questions to `au-trust-distributions`; company tax and consolidation to `au-company-tax`.

### Permitted factual defaults

These apply only to a missing fact where the law above is established. Disclose each one, its alternative and its effect in the reviewer brief.

| Missing fact | Default | Disclosure |
|---|---|---|
| Whether the parties have made, or will make, the roll-over choice | Work the no-roll-over outcome as the primary schedule and the roll-over outcome as conditional | Show both; the choice is the taxpayer's |
| Whether an asset was acquired before 20 September 1985, with no acquisition evidence | Treat it as post-CGT | Pre-CGT status would change the share cost base split |
| Whether a liability relates to a specific asset | Treat it as in respect of all the assets (ss 122-37(2), 615-65(5) apply this by law where no specific asset) | Apportion by market value only once values are evidenced |
| Post-transfer intentions for the next 3 years | Do not rely on the safe harbour; test the genuine restructure condition on the LCR 2016/3 factors | Safe harbour status shown as a question |

**No default is permitted** for a market value, cost base, adjustable value, trading stock value, small business entity status, residency or ultimate economic ownership share. Each is unknown, not zero, and leaves every dependent test and cost base open (Needs Input).

### Working paper extension

```
AUSTRALIA RESTRUCTURE ROLLOVERS -- EVIDENCE PACK
Income year: 2026-27   Prepared: [date]   Status: preparation only, specialist to choose

1. STRUCTURE MAP (before / after each step; owner, interest, capacity, UEO share)
2. EVIDENCE MATRIX (rows = conditions with provision; columns = 328-G | 122-A | 122-B | 615)
   cell = evidenced [doc ref] | not evidenced | question
3. ASSET REGISTER (one row per asset, once only)
   category | acquired | pre-CGT? | cost base | RCB | adjustable value | stock value | MV (valuer, date) | liabilities
4. CONSIDERATION SCHEDULE (shares: class, number, redeemable?; liabilities assumed; cash; loans)
5. CONSEQUENCES PER PATHWAY (roll-over cost / share cost base workings; pre-CGT share count)
6. CHOICES (who, provision, deadline or Needs Input)
7. ROUTING LIST and REVIEWER FLAGS (refusal codes raised)
```

## Worked cases

All facts and figures below are hypothetical and set in the 2026-27 income year.

### Case 1: SBRR, new shares as consideration (s 328-465)

A sole trader with a small business entity status evidenced for 2026-27 transfers active assets to a new company she wholly owns, for 100 shares (all the consideration). Roll-over costs: land cost base $400,000, goodwill cost base $20,000, trading stock value at the start of the year $30,000; plant adjustable value $70,000; the company assumes $100,000 of business liabilities. No asset is pre-CGT.

```oa-check
name: SBRR first element of cost base of new shares 2026-27
inputs:
  land_cost_base: 400000
  goodwill_cost_base: 20000
  trading_stock_rollover_cost: 30000
  plant_adjustable_value: 70000
  liabilities_assumed: 100000
  shares_issued: 100
steps:
  - rollover_costs_counted: land_cost_base + goodwill_cost_base + trading_stock_rollover_cost
  - first_element_total: rollover_costs_counted + plant_adjustable_value - liabilities_assumed
  - first_element_per_share: first_element_total / shares_issued
expected:
  rollover_costs_counted: 450000
  first_element_total: 420000
  first_element_per_share: 4200
```

Each share's first element of cost base is $4,200. Had the land been pre-CGT, its roll-over cost would drop out of the sum (s 328-465(1)(d)(i)).

### Case 2: Subdivision 122-A, incorporating a whole business (ss 122-35, 122-50)

A sole trader disposes of all the assets of his business to a new company for 10 non-redeemable shares, and the company assumes an $80,000 overdraft. All assets are post-CGT. Precluded assets at market value: trading stock $40,000, plant $60,000. Other assets: land cost base $300,000 (market value $700,000), goodwill cost base $0 (market value $200,000). An independent valuation puts the 10 shares at $920,000.

```oa-check
name: Div 122-A all-assets incorporation liability cap and share cost base 2026-27
inputs:
  trading_stock_mv: 40000
  plant_mv: 60000
  land_cost_base: 300000
  goodwill_cost_base: 0
  land_mv: 700000
  goodwill_mv: 200000
  liabilities_assumed: 80000
  shares_issued: 10
  share_valuation: 920000
steps:
  - precluded_mv: trading_stock_mv + plant_mv
  - other_cost_bases: land_cost_base + goodwill_cost_base
  - liability_cap: precluded_mv + other_cost_bases
  - cap_headroom: liability_cap - liabilities_assumed
  - first_element_per_share: (liability_cap - liabilities_assumed) / shares_issued
  - net_asset_mv: precluded_mv + land_mv + goodwill_mv - liabilities_assumed
  - share_value_gap: share_valuation - net_asset_mv
expected:
  precluded_mv: 100000
  other_cost_bases: 300000
  liability_cap: 400000
  cap_headroom: 320000
  first_element_per_share: 32000
  net_asset_mv: 920000
  share_value_gap: 0
```

The liabilities are within the s 122-35(2) cap, each share's first element is $32,000 and the share valuation matches net asset market value. 'Substantially the same' (s 122-20(3)) is a judgement on evidenced values; a gap is a reviewer question, not a computed pass. Plant rolls over under s 40-340(1) item 1.

### Case 3: Division 615, interposing a holding company (ss 615-20, 124-15, 615-65)

A Pty Ltd has 100 shares with equal rights, all post-CGT: Jo holds 60 (total cost base $60,000) and Sam 40 (total cost base $40,000). HoldCo acquires all 100 for 10 HoldCo shares each. A Pty Ltd's post-CGT assets have total cost bases of $500,000 and its liabilities in respect of them are $150,000; it holds no pre-CGT assets. HoldCo chooses within 2 months that s 615-65 applies.

```oa-check
name: Div 615 member and interposed company cost bases 2026-27
inputs:
  total_original_shares: 100
  jo_original_shares: 60
  sam_original_shares: 40
  exchange_ratio: 10
  jo_cost_base: 60000
  entity_post_cgt_cost_bases: 500000
  entity_liabilities: 150000
steps:
  - jo_new_shares: jo_original_shares * exchange_ratio
  - sam_new_shares: sam_original_shares * exchange_ratio
  - jo_percent_after: jo_new_shares / (jo_new_shares + sam_new_shares) * 100
  - jo_percent_before: jo_original_shares / total_original_shares * 100
  - jo_first_element_per_new_share: jo_cost_base / jo_new_shares
  - holdco_first_element_total: entity_post_cgt_cost_bases - entity_liabilities
  - holdco_first_element_per_share: holdco_first_element_total / total_original_shares
expected:
  jo_new_shares: 600
  sam_new_shares: 400
  jo_percent_after: 60
  jo_percent_before: 60
  jo_first_element_per_new_share: 100
  holdco_first_element_total: 350000
  holdco_first_element_per_share: 3500
```

Jo's percentage is unchanged (s 615-20(1)); the market value ratio test (s 615-20(2)) still needs valuations. Jo's HoldCo shares start at $100 each; HoldCo's A Pty Ltd shares start at $3,500 each, from A Pty Ltd's net asset cost bases, not from the members' $100,000.

### Case 4: Changed shares on a partnership incorporation

Three equal partners move their business to a company issuing 100, 150 and 50 shares so that 2 of them, a couple, lower their combined tax (the ATO SBRR page example). The same individuals keep ultimate economic ownership but their shares change: s 328-430(1)(c) fails. The Subdivision 122-B market value test per partner (s 122-130(3)) also fails, because 2 partners receive shares worth more or less than their one-third interests. Record both as not met; neither roll-over is available on these facts.

### Case 5: A transfer that precedes a sale

A company transfers its active assets to its sole shareholder, who sells them to buyers 12 months later and seeks the CGT discount (LCR 2016/3 Example 5). The sale within 3 years removes the safe harbour, and the facts match the para 10 indicator of a preliminary step to realise assets. Record the genuine restructure condition as not evidenced and raise R-AU-RR-2; do not compute a roll-over outcome as the primary position.

### Case 6: Redeemable shares on incorporation

The draft documents issue redeemable preference shares to the sole trader. Section 122-20(2) fails, so Subdivision 122-A is unavailable on the drafts. The SBRR does not require shares or any consideration (ATO SBRR page), so its column stays open on its own conditions. Report the drafting point to the specialist; do not redraft.

## When to refuse or refer

Stop the affected calculation where a fact, source condition or scope requirement above is unresolved, and return Needs Input or the refusal below.

### Refusal catalogue

| Code | Trigger | Message (verbatim) |
|---|---|---|
| R-AU-RR-1 | Asked to choose, recommend or sequence a pathway, or to draft transaction documents | "Choosing a rollover pathway, sequencing the steps and drafting the documents is specialist tax and legal work. I have prepared the condition matrix and conditional consequences only." |
| R-AU-RR-2 | Any LCR 2016/3 para 10 indicator, a step that removes an existing liability, or any scheme with a tax benefit as a dominant feature | "These facts raise the genuine restructure condition and Part IVA. I have recorded the indicators; a specialist must assess them before any roll-over outcome is relied on." |
| R-AU-RR-3 | A party that is not an Australian resident, a trust that is not a resident trust for CGT purposes, or reliance on taxable Australian property | "Foreign-resident and taxable Australian property roll-overs are outside this guide. Refer to a specialist." |
| R-AU-RR-4 | A consolidated group, a head company continuing through Division 615, or an ADI restructure (ss 615-5(2), 615-30(2), 615-35) | "Consolidation and ADI restructures are outside this guide. Refer to a specialist; see also au-company-tax R-AU-CT-1." |
| R-AU-RR-5 | Another roll-over or a demerger (Subdivisions 124-N, 126-A, 126-B, 126-G; Division 125) | "That roll-over is outside this guide. Refer to a specialist." |
| R-AU-RR-6 | A transfer or realisation on or after 1 July 2027 involving pre-CGT status or the s 112-175 deemed sale, or any reliance on the proposed discretionary trust roll-over | "This turns on the 1 July 2027 CGT changes or on Bills that were not law on 11 November 2026. Refer to au-capital-gains Section 9 or au-trust-distributions Rule 14 and a specialist." |
| R-AU-RR-7 | A market value, cost base or adjustable value needed for a test or cost base is missing | "That value is unknown, not zero. The dependent tests and cost bases stay open until a dated valuation or record is supplied." |
| R-AU-RR-8 | A choice deadline has passed or an extension of time is sought | "An extension of time is a private ruling application to the ATO. Assemble the facts and refer to the registered tax agent." |

### Reviewer attention thresholds

The reviewer attention threshold for a roll-over position is **AUD 0**: every roll-over, share cost base and pre-CGT share count requires review, whatever its amount. Flag regardless of amount: any condition recorded as a question; any market value without a dated independent valuation; any residency, trust or family trust election issue; any post-transfer change within 3 years; and any interaction with Division 7A, duty or GST.

### Prohibitions

- NEVER choose or recommend a pathway, or record a condition as met on the client's statement alone.
- NEVER treat a missing market value, cost base or adjustable value as zero.
- NEVER rely on the safe harbour without evidence covering the full 3 years.
- NEVER treat redeemable shares, or any consideration other than shares and assumed liabilities, as satisfying Division 122.
- NEVER carry the members' cost bases into the interposed company's cost base under Division 615.
- NEVER model the proposed discretionary trust roll-over as current law.
- NEVER present figures as definitive.

## Completion checklist

- [ ] Structure map shows every entity, interest, capacity and ultimate economic ownership share before and after each step.
- [ ] Each condition in Steps 3, 5, 6 and 7 has a provision reference and an evidence status for every candidate pathway.
- [ ] Every asset appears once in the register, reconciled to the ledger, fixed asset register and depreciation schedules.
- [ ] Share cost bases recompute from the register and match the provision used (ss 328-465, 122-40, 122-50, 122-155, 122-180, 124-10, 124-15, 615-65).
- [ ] Market value comparisons are made only where both sides are evidenced.
- [ ] Each choice records who chooses, the provision and the deadline, or Needs Input.
- [ ] Pre-CGT outcomes are checked against s 112-175 for anything realised after 30 June 2027.
- [ ] Part IVA is flagged on every pathway; the routing list is complete.
- [ ] Every unresolved item records the evidence needed, owner, status and next action.

## Sources

| Source | URL | Read on |
|---|---|---|
| ATO, Small business restructure roll-over (QC48586, last updated 7 May 2025): eligibility, $10 million, from 1 July 2016, consequences, 12-month discount and 15-year exemption notes, Part IVA, ownership example | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/income-and-deductions-for-business/concessions-offsets-and-rebates/small-business-restructure-roll-over | 2026-11-02 |
| LCR 2016/3, genuine restructure of an ongoing business: paras 3, 6-11, 25A, 48, Examples 5 and 9 | https://www.ato.gov.au/law/view/document?DocID=COG/LCR20163/NAT/ATO/00001 | 2026-11-02 |
| ITAA 1997 s 328-110 (small business entity) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-110 | 2026-11-02 |
| ITAA 1997 s 328-430 (conditions; CRP 2017/2 note) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-430 | 2026-11-02 |
| ITAA 1997 s 328-435 (safe harbour) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-435 | 2026-11-02 |
| ITAA 1997 s 328-440 (discretionary trusts) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-440 | 2026-11-02 |
| ITAA 1997 s 328-445 (residency) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-445 | 2026-11-02 |
| ITAA 1997 s 328-450 (no direct consequences) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-450 | 2026-11-02 |
| ITAA 1997 s 328-455 (roll-over cost) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-455 | 2026-11-02 |
| ITAA 1997 s 328-460 (pre-CGT assets) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-460 | 2026-11-02 |
| ITAA 1997 s 328-465 (new membership interests) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-465 | 2026-11-02 |
| ITAA 1997 s 328-470 (loss integrity) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-470 | 2026-11-02 |
| ITAA 1997 s 122-15 (Subdivision 122-A trigger events) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-15 | 2026-11-02 |
| ITAA 1997 s 122-20 (consideration, market value) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-20 | 2026-11-02 |
| ITAA 1997 s 122-25 (other requirements, precluded assets) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-25 | 2026-11-02 |
| ITAA 1997 s 122-35 (liability caps) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-35 | 2026-11-02 |
| ITAA 1997 s 122-37 (liability rules) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-37 | 2026-11-02 |
| ITAA 1997 s 122-40 (single asset consequences) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-40 | 2026-11-02 |
| ITAA 1997 s 122-45 (all assets of a business) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-45 | 2026-11-02 |
| ITAA 1997 s 122-50 (all post-CGT assets) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-50 | 2026-11-02 |
| ITAA 1997 s 122-55 (all pre-CGT assets) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-55 | 2026-11-02 |
| ITAA 1997 s 122-60 (mixed assets) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-60 | 2026-11-02 |
| ITAA 1997 s 122-125 (Subdivision 122-B trigger events) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-125 | 2026-11-02 |
| ITAA 1997 s 122-130 (partners' consideration) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-130 | 2026-11-02 |
| ITAA 1997 s 122-135 (partners' other requirements) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-135 | 2026-11-02 |
| ITAA 1997 s 122-140 (partners' liability caps) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-140 | 2026-11-02 |
| ITAA 1997 s 122-150 (partners' gain disregarded) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-150 | 2026-11-02 |
| ITAA 1997 s 122-155 (partners' share cost base) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-155 | 2026-11-02 |
| ITAA 1997 s 122-160 (partners' mixed interests) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-160 | 2026-11-02 |
| ITAA 1997 s 122-170 (partners' business gain disregarded) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-170 | 2026-11-02 |
| ITAA 1997 s 122-175 (partners' business consequences) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-175 | 2026-11-02 |
| ITAA 1997 s 122-180 (partners' post-CGT business interests) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-180 | 2026-11-02 |
| ITAA 1997 s 122-185 (partners' pre-CGT business interests) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-185 | 2026-11-02 |
| ITAA 1997 s 122-190 (partners' mixed business interests) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/122-190 | 2026-11-02 |
| ITAA 1997 s 615-5 (Division 615 exchange) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-5 | 2026-11-02 |
| ITAA 1997 s 615-10 (redemption or cancellation) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-10 | 2026-11-02 |
| ITAA 1997 s 615-15 (completion time) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-15 | 2026-11-02 |
| ITAA 1997 s 615-20 (members' interests, residency) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-20 | 2026-11-02 |
| ITAA 1997 s 615-25 (interposed company shares) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-25 | 2026-11-02 |
| ITAA 1997 s 615-30 (interposed company choice) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-30 | 2026-11-02 |
| ITAA 1997 s 615-35 (ADI restructures) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-35 | 2026-11-02 |
| ITAA 1997 s 615-40 (CGT consequences) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-40 | 2026-11-02 |
| ITAA 1997 s 615-60 (trading stock exemption disregarded) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-60 | 2026-11-02 |
| ITAA 1997 s 615-65 (interposed company cost base) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/615-65 | 2026-11-02 |
| ITAA 1997 s 124-10 (one original asset) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/124-10 | 2026-11-02 |
| ITAA 1997 s 124-15 (several original assets) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/124-15 | 2026-11-02 |
| ITAA 1997 s 103-25 (time to choose) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/103-25 | 2026-11-02 |
| ITAA 1997 s 40-340 (depreciating asset roll-over relief) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/40-340 | 2026-11-02 |
| ITAA 1997 s 328-243 (small business pool roll-over relief) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/328-243 | 2026-11-02 |
| ITAA 1997 s 70-90 (trading stock disposed of outside the ordinary course of business) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/70-90 | 2026-11-02 |
| ITAA 1997 s 70-95 (acquirer's cost is that market value) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/70-95 | 2026-11-02 |
| ITAA 1997 s 70-100 (notional disposal where an owner keeps an interest) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/70-100 | 2026-11-02 |
| ITAA 1997 s 112-175 (pre-CGT deemed sale, 1 July 2027) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/112-175 | 2026-11-02 |
| ATO, Rollover and restructure, simpler depreciation (QC64427, last updated 27 June 2025): pool roll-over choice | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/rollover-and-restructure | 2026-11-02 |
| ATO, How to choose a CGT rollover and apply for an extension (QC66018, last updated 22 June 2026) | https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-events/how-to-choose-a-cgt-rollover-and-apply-for-an-extension | 2026-11-02 |
| ATO, Tax reform: introducing a minimum tax on discretionary trusts (QC107302, last updated 3 November 2026): 'not yet law'; 3-year roll-over from 1 July 2027 | https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/tax-reform-introducing-a-minimum-tax-on-discretionary-trusts | 2026-11-11 |
| APH, Treasury Laws Amendment (Tax Reform No. 3) Bill 2026: progress and committee referral | https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7554 | 2026-11-11 |

Named on the ATO SBRR page but not read in this session: LCR 2016/2 (consequences of a roll-over), CRP 2017/2 (text read only as the legal database note at s 328-430) and PS LA 2005/24. The active asset test (s 152-40) and s 152-10(1A) were not re-read; `au-small-business-cgt` holds them.

**Currency and revision.** Version 0.1, currency date 2 November 2026. Change log: v0.1 (2 November 2026) first draft from primary sources read that day; 11 November 2026 recheck: the ATO discretionary trust page date corrected to 3 November 2026 and the Bill's status reread unchanged; awaiting qualified Australian review.

Method adapted by its author from the `au-restructure-rollovers` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Topic chosen from the public Ask Nagaris skill list (names only); no Nagaris text was used.

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
