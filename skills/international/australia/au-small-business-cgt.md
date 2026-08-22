---
name: au-small-business-cgt
description: >
  Use this skill whenever an Australian small business owner, company, trust or partnership asks about the Division 152 small business CGT concessions -- selling a business, premises, goodwill, or shares/units in a trading entity; the $2m turnover or $6m maximum net asset value gateways; the active asset test; the 15-year exemption; the 50% active asset reduction; the retirement exemption; the small business rollover; significant individual or CGT concession stakeholder tests; or contributing sale proceeds to super under the CGT cap. Trigger on "small business CGT", "SBCGT", "Div 152", "active asset", "retirement exemption", "CGT cap election". ALWAYS read this skill before touching any Div 152 work.
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

# Australia Small Business CGT Concessions -- Division 152 Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context (Tax Reform No. 1 Act 2026, Royal Assent 26 June 2026).** From **1 July 2027** the *Treasury Laws Amendment (Tax Reform No. 1) Act 2026* replaces the general 50% CGT discount for individuals and trusts (including gains flowing through partnerships) with **cost-base indexation plus a 30% minimum tax rate** on gains accruing from that date, deems assets held on 30 June 2027 (including pre-CGT assets) re-acquired on 1 July 2027, and -- **enacted in the Act via amendments made during passage** -- lifts the aggregated turnover gateway for the **small business 50% active asset reduction only** from **$2 million to $10 million** from 1 July 2027. The other three Div 152 concessions keep the $2m/$6m gateways. Everything below states the law for CGT events happening **up to 30 June 2027**; Rule 15 maps the transition. Straddle and timing questions escalate (R-AU-SBC-5).

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary legislation | ITAA 1997 Division 152 (Subdivs 152-A to 152-E); s 292-100 (CGT cap contributions) |
| Tax authority | Australian Taxation Office (ATO) |
| Income year | 2026-27 (1 July 2026 -- 30 June 2027); lodgment season for 2025-26 |
| Gateway tests (either) | CGT small business entity: aggregated turnover < $2m -- OR -- maximum net asset value (MNAV) <= $6m just before the CGT event |
| Active asset test | Active for at least half the ownership period, or 7.5 years if owned > 15 years |
| Significant individual | Small business participation percentage (SBPP) >= 20% (direct + indirect) |
| CGT concession stakeholder | Significant individual, or their spouse with SBPP > 0% |
| 15-year exemption | 15 years' continuous ownership + (55+ and in connection with retirement, or permanent incapacity) -- gain fully disregarded |
| Retirement exemption | $500,000 lifetime limit per individual; under 55 must pay the amount into complying super/RSA |
| Rollover replacement period | 1 year before to 2 years after the CGT event (extendable); exit via CGT events J2/J5/J6 |
| CGT cap amount | **2026-27: $1,935,000; 2025-26: $1,865,000** (excluded from the NCC cap with a valid election) |
| From 1 July 2027 | 50% reduction gateway becomes $10m aggregated turnover (law); general discount replaced by indexation + 30% minimum |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Turnover unknown or near $2m | Do not assume the SBE gateway; compute MNAV; if both unproven, flag eligibility as unestablished |
| Related entities not mapped | Assume connected/affiliated until control percentages (40%+) and "acts in concert" facts are verified |
| Asset partly rented out | Assume main use is deriving rent (NOT active) until the affiliate/connected-entity carve-out or temporary-use facts are evidenced |
| Discretionary trust, no distribution in event year | Assume no significant individual until prior-year distribution minutes are sighted (s 152-70 alternative rule) |
| Prior retirement-exemption use unknown | Treat the remaining lifetime limit as unverified; require written records of every prior CGT exempt amount |
| Taxpayer's age near 55 | Assume under 55 -- super payment required -- until DOB confirmed against the date the choice is made |
| "In connection with retirement" unclear | Flag: requires at least a significant reduction in working hours/involvement, not necessarily permanent exit |
| CGT event date near 30 June 2027 | Assume the post-reform regime may apply; escalate before any computation is relied on |
| Contract vs settlement dates differ | CGT event A1 happens at CONTRACT date; test everything at that date |

## Section 2 -- Eligibility decision tree

| Step | Question | Yes | No |
|---|---|---|---|
| 1 | Pre-CGT asset (acquired before 20 Sep 1985)? | Escalate (R-AU-SBC-4) -- and note reform removes pre-CGT status from 1 July 2027 | Continue |
| 2 | Gain from CGT event J5/J6 (failed earlier rollover)? | Skip to retirement exemption only (Rule 12) -- no discount, no AAR, no 15-year | Continue |
| 3 | Gateway: CGT SBE (< $2m aggregated turnover), MNAV <= $6m, passively-held-asset rules, or partner rules satisfied? | Continue | STOP -- no Div 152; general discount only |
| 4 | Active asset test met (Rule 5)? | Continue | STOP -- no Div 152 |
| 5 | Asset is a share or trust interest? | Extra conditions (Rules 7-8): stakeholder/90% test + object entity test + modified active asset test. Fail any -> STOP | Continue |
| 6 | 15-year exemption conditions met (Rule 9)? | Gain FULLY disregarded -- losses preserved, lifetime limits untouched; consider CGT cap contribution | Continue |
| 7 | Waterfall | Capital losses -> general 50% discount (if eligible) -> 50% active asset reduction (automatic unless choose out) -> retirement exemption and/or rollover, in either order, to reduce the remainder (to nil if limits allow) | -- |

## Section 3 -- Basic conditions (Subdiv 152-A)

### Rule 1 -- The gateway: s 152-10

A capital gain (except from CGT events D1, H2, J5, J6 for gateway purposes -- J5/J6 have their own path) may be reduced or disregarded if: (a) a CGT event happens to your asset; (b) the event would otherwise produce a gain; (c) you satisfy ONE of: CGT small business entity (< $2m aggregated turnover), the $6m MNAV test, the passively-held asset rules (s 152-10(1A)/(1B)), or the partner rules; and (d) the asset passes the active asset test. Shares/units carry extra conditions (Rules 7-8). Test everything at the time of the CGT event -- for a sale contract, the CONTRACT date.

### Rule 2 -- CGT small business entity: aggregated turnover < $2 million

"CGT small business entity" (s 152-10(1AA)) = would be a small business entity under s 328-110 if the $10m there read $2m. You must carry on a business in the event year and pass any one of: prior-year aggregated turnover < $2m; a reasonable current-year estimate < $2m (unavailable if actual turnover was $2m+ in BOTH of the two prior years); or actual current-year turnover < $2m. **Aggregated turnover** = your annual turnover + annual turnovers of entities **connected with you** (control >= 40%: shareholdings carrying >= 40% of voting/dividend/capital rights; for a discretionary trust, trustee acts on your directions or you received >= 40% of distributions in any of the 4 prior years) + turnovers of your **affiliates** (an individual or company that acts, or could reasonably be expected to act, on your directions or in concert with you -- spouses and children are NOT automatic affiliates), excluding inter-group dealings.

### Rule 3 -- Maximum net asset value test: $6 million (s 152-20)

Just before the CGT event, the sum of the **net values** (market value minus attached liabilities minus provisions for annual leave, long service leave, unearned income and tax) of the CGT assets of you, entities connected with you, and your affiliates (and entities connected with your affiliates) must not exceed **$6,000,000**. It is a cliff, not a phase-out, and it is NOT indexed. Count affiliate-side assets only if used (or held ready for use) in a business carried on by you or an entity connected with you.

**Excluded assets** (individuals): your own **main residence** to the extent of private use -- if part is used to produce assessable income with deductible interest, include only that percentage of the dwelling's net value; **superannuation** and approved-deposit-fund rights; life insurance policies; assets used solely for personal use and enjoyment by you or your affiliate (boats, holiday homes never rented). Also disregard shares/interests in your own connected entities to avoid double counting (their underlying assets already count).

### Rule 4 -- Passively-held assets and partners

You can access Div 152 without carrying on a business where your asset is used in the business of your **affiliate or an entity connected with you**, and that business entity is the CGT small business entity (s 152-10(1A)/(1B)) -- the classic case: individual owns the premises, their trading company runs the business. A spouse or child under 18 is deemed an affiliate where their entity uses your asset (s 152-47). Partners: an interest in a partnership asset, or a partner's own asset used in the partnership business, qualifies where the partnership is the CGT SBE.

## Section 4 -- Active asset test (s 152-35, s 152-40)

### Rule 5 -- The period test

The asset must be active for at least **half of the ownership period** (acquisition to CGT event, or to business cessation if the event happens within 12 months after cessation), or for at least **7.5 years** if owned for more than 15 years. The active periods do NOT need to be continuous. An asset is active if you, your affiliate, or an entity connected with you uses it (or holds it ready for use) in carrying on a business -- or, for intangibles (goodwill, licences), it is inherently connected with the business. Look at the asset as a whole, not just the portion used.

### Rule 6 -- Excluded assets and the rent nuance

**Never active:** assets whose main use is to derive rent, interest, an annuity, royalties or foreign exchange gains; financial instruments (loans, debentures, futures); shares and trust interests (unless the 80% test below is met); subdivided vacant land held passively.

**The rent carve-out that saves most premises:** in working out "main use", **disregard rent derived from your affiliate or a connected entity that uses the asset in its business** (s 152-40(4A)) -- premises leased to your own trading company or trust ARE active. Rent from unrelated tenants counts against you: a building mainly let to third parties fails even if the business occupies part. Temporary rental use is also disregarded. Short-stay accommodation with substantial services and no exclusive possession (motel-style) may not be "rent" at all -- degree-of-control analysis (TD 2006/78); flag, don't assume.

**The 80% test for shares/units as active assets:** a share in an Australian-resident company (or interest in a resident trust) is active where active assets plus inherently-connected cash and financial instruments are >= 80% of the market value of all its assets. Momentary or temporary dips below 80% are ignored.

## Section 5 -- Shares and trust interests: extra conditions (s 152-10(2))

### Rule 7 -- Significant individual, stakeholder, 90% test

- **Small business participation percentage (SBPP)** = direct + indirect. Direct, for a company: the **smallest** of the percentages of voting power, dividend entitlement, and capital entitlement (all share classes except redeemable; discretionary dividend rights can drive it to 0%). For a trust where entitlements are not fixed: the smaller of the income and capital distribution percentages actually made **during the event year**; if the trustee distributed nothing and the trust had no net income or a tax loss that year, use the most recent prior distribution year (s 152-70). Indirect = your direct percentage in the interposed entity x its total percentage in the target.
- **Significant individual**: SBPP >= 20% in the company or trust.
- **CGT concession stakeholder**: a significant individual, or the spouse of one with SBPP > 0%.
- **The 90% test**: where the entity CLAIMING the concession is itself a company or trust, CGT concession stakeholders in the object company/trust must together hold an SBPP of at least **90% in the claimant entity**.

### Rule 8 -- The four extra conditions (gains from 8 February 2018)

For a gain on shares or trust interests, ALL of:

1. You either carried on a business just before the CGT event or you satisfy the MNAV test yourself;
2. Just before the event, you are a CGT concession stakeholder in the object company/trust, OR the 90% test is met for the claimant entity;
3. The object company/trust would itself be a CGT small business entity or satisfy the MNAV test, applying a **modified connected-entity rule** (deemed control at 20%+ when tracing what the object entity controls) so groups cannot be fragmented;
4. The shares/units pass the **modified active asset test**: look through to the underlying assets; active assets + inherently-connected cash and financial instruments must be >= 80% of total market value, disregarding cash/instruments injected to pass the test, and ignoring temporary breaches.

Gains made before 8 February 2018 faced fewer conditions -- historical only. These integrity rules kill many HoldCo sales: run them BEFORE the waterfall.

## Section 6 -- The four concessions

### Rule 9 -- 15-year exemption (Subdiv 152-B) -- always first

The ENTIRE gain is disregarded (no cap) if: basic conditions are met; you **continuously owned the asset for the 15 years** ending just before the CGT event; and you are **55 or older** at the event and it happens **in connection with your retirement** (a significant reduction in hours/involvement suffices; permanent exit not required), or you are **permanently incapacitated** (no age requirement). Company/trust claimants must additionally have had a significant individual for periods totalling at least 15 years of ownership (not necessarily the same person or continuous), and the individual who is a significant individual just before the event must satisfy the 55+/retirement or incapacity limb. Payments of the exempt amount by a company/trust to its CGT concession stakeholders **within 2 years** of the event (capped by each stakeholder's participation percentage) are not assessable and not dividends (s 152-125). If the 15-year exemption applies, capital losses are NOT consumed and the other concessions are irrelevant. Death: the LPR/beneficiary can claim within 2 years of death to the extent the deceased could have (55+ just before death; no retirement connection needed).

### Rule 10 -- 50% active asset reduction (Subdiv 152-C)

Basic conditions only -- no extra tests. The remaining gain (after losses and the general discount) is reduced by 50%. It applies **automatically unless you choose for it not to apply**. Why skip it: a company or trust that skips the AAR can shelter a LARGER amount with the retirement exemption and pay it out tax-free to stakeholders -- the AAR-sheltered half otherwise sits in the company as untaxed profit that is an **unfranked dividend** (or CGT event G1/E4 issue) when extracted later. Companies never get the general discount; the AAR is their only 50%.

### Rule 11 -- Retirement exemption (Subdiv 152-D)

Disregard a chosen "CGT exempt amount" up to a **$500,000 lifetime limit per individual** (per CGT concession stakeholder for company/trust claimants -- also $500,000 each, reduced by earlier use). No requirement to actually retire or stop working. Keep a written record of every amount chosen. **Individuals under 55 just before making the choice** (the choice is generally made when the return is lodged -- turning 55 before then removes the requirement) must contribute the exempt amount to a complying super fund or RSA by the later of making the choice and receiving the proceeds. **Company/trust claimants** must PAY the exempt amount to at least one CGT concession stakeholder (capped by participation percentage) by 7 days after the later of making the choice and receiving capital proceeds; if the stakeholder is under 55 just before the payment, the entity must pay it into super on their behalf. The payment is NANE income of the stakeholder, not a dividend. Gains from CGT events J5/J6 can use this exemption without re-meeting the basic conditions.

### Rule 12 -- Replacement asset rollover (Subdiv 152-E; CGT events J2/J5/J6)

Defer all or part of the remaining gain by acquiring a **replacement active asset or making a 4th-element capital improvement** to an existing asset within the **replacement asset period: 1 year before to 2 years after** the CGT event (extendable by the Commissioner; extended automatically for look-through earnout rights). The same entity must choose and acquire. Replacement shares/units must pass the 80% test with a stakeholder connection maintained. Exit events:

- **J5** -- no qualifying replacement (or it isn't active) at the end of the period: the whole rolled-over gain crystallises at that time.
- **J6** -- replacement acquired but its cost (1st + 2nd element + improvement spend) is less than the rolled-over amount: the shortfall crystallises at the end of the period.
- **J2** -- after the period, the replacement asset later changes status (sold, stops being active, becomes trading stock): the deferred gain revives then; a further rollover or the retirement exemption can be chosen.

J5/J6 gains get NO general discount, NO 50% AAR and NO 15-year exemption -- only the retirement exemption (basic conditions not re-tested). Rolling over into nothing is therefore only a 2-year deferral, commonly used by 53-54 year-olds to reach 55 before a retirement-exemption choice (planning -- escalate, don't advise).

## Section 7 -- Ordering and stacking

### Rule 13 -- The waterfall and the arithmetic

For each gain, in order: **(0)** 15-year exemption -- if it applies, stop, the gain never enters the net-capital-gain calculation; **(1)** capital losses (current then carried forward; taxpayer chooses allocation for pre-1 July 2027 events); **(2)** general 50% discount (individuals/trusts, asset held > 12 months; NEVER companies; not J2/J5/J6 gains); **(3)** small business 50% active asset reduction (automatic unless choose out); **(4)** retirement exemption and/or rollover on the remainder, in either order, until nil.

```
Individual, active asset held > 12 months, no losses, gain G:
  after discount              G x 50%        = 0.50G
  after 50% AAR               0.50G x 50%    = 0.25G   (25% inclusion)
  tax at 47% top marginal     0.25G x 47%    = 11.75% effective
  retirement exemption/rollover on 0.25G     -> 0% if within limits
Trust beneficiary gross-up: x2 if one halving applied, x4 if both.
Company: no discount -- AAR alone leaves 0.50G; 25% rate -> 12.5% effective,
  and the sheltered half is untaxed profit with an extraction cost later.
```

The concessions apply per-asset, per-gain: with several gains you may stack every concession you qualify for on each until each is nil.

## Section 8 -- CGT cap super contributions (s 292-100; QC 18123)

### Rule 14 -- Getting sale proceeds into super outside the NCC cap

Amounts sheltered by the **15-year exemption** (up to the whole **capital proceeds**, even though the gain was disregarded) and the **retirement exemption** (the CGT exempt amount, max $500,000) can be contributed to super and **excluded from the non-concessional contributions cap**, up to the lifetime **CGT cap amount**: **$1,935,000 for 2026-27** ($1,865,000 for 2025-26; indexed to AWOTE in $5,000 increments). Mechanics -- all three must hold, or the contribution counts as an ordinary NCC (2026-27 NCC cap: $130,000):

1. **Form**: give the fund a **CGT cap election (NAT 71161) at or before the time the contribution is made** -- late is fatal;
2. **Timing (individual)**: contribute by the later of the day the return for the event year is due to be lodged and 30 days after receiving the proceeds. The compulsory under-55 retirement-exemption payment automatically counts against the CGT cap;
3. **Timing (via company/trust)**: the stakeholder contributes within 30 days after receiving the s 152-125 / s 152-325 payment.

The CGT cap is a lifetime running total across both concessions. Contributions still count toward total super balance and transfer balance cap planning -- flag, don't advise.

## Section 9 -- Interaction with the 1 July 2027 CGT reform

### Rule 15 -- What is law and what is only announced (as at 20 August 2026)

| Item | Status |
|---|---|
| *Treasury Laws Amendment (Tax Reform No. 1) Act 2026* | **Law** -- Royal Assent 26 June 2026 |
| General 50% discount replaced by cost-base indexation + 30% minimum tax rate on gains accruing from 1 July 2027 (individuals and trusts, incl. gains through partnerships); discount retained for new residential dwellings and affordable housing | **Law** -- applies from 1 July 2027 |
| Deemed disposal/re-acquisition of assets held 30 June 2027; later disposals split into pre/post components across four asset categories | **Law** -- from 1 July 2027 |
| Pre-CGT (pre-20 Sep 1985) status removed after 30 June 2027 | **Law** |
| Capital losses must be applied against discounted gains first | **Law** -- from 1 July 2027 (removes taxpayer choice) |
| **Small business 50% active asset reduction gateway: aggregated turnover $2m -> $10m** | **Law** -- enacted in the Act (added by government amendments during passage), commencing **1 July 2027**, and applying **ONLY to the 50% reduction**. The 15-year exemption, retirement exemption and rollover keep the $2m turnover / $6m MNAV gateways |
| 50% discount for early-stage investors/founders (start-up carve-out) | **Announced only** -- Treasury consultation; not law |
| 30% minimum tax on discretionary trusts from 1 July 2028 | **Announced only** -- consultation closed 31 July 2026; not law |

Practical consequences: CGT events **up to 30 June 2027** use everything in this skill unchanged. From 1 July 2027, Div 152 itself survives -- the AAR still halves the gain -- but the base it halves is an indexed gain, the 30% minimum rate applies underneath, and a $2m-$10m turnover business gains AAR access (but still needs the $6m MNAV or another gateway for the other three concessions). How the minimum rate, indexation, deemed re-acquisition and the Div 152 waterfall interleave in detail awaits ATO guidance -- **any disposal, rollover tail (J2/J5/J6) or contribution-timing question straddling 1 July 2027 escalates (R-AU-SBC-5)**. Never advise accelerating or deferring a sale around the date.

## Section 10 -- Worked examples

All examples assume CGT events in 2026-27 (before 1 July 2027), Australian residents, and no capital losses unless stated.

### Example 1 -- Gateways: turnover fails, MNAV passes (and a fail variant)

Nadia (58) contracts on 30 November 2026 to sell her sole-trader business premises, owned 8 years and used in her business throughout. Aggregated turnover (including her 100%-owned company) was $3.4m in 2025-26 and is estimated at $3.1m for 2026-27 -- **CGT SBE gateway fails**. MNAV just before the event:

```
Business premises ($2,600,000 MV - $700,000 mortgage)        $1,900,000
Trading company (connected, 100%): net CGT assets            $1,750,000
Share portfolio                                                $600,000
Main residence: 10% deductible-interest office use
  10% x ($2,400,000 - $900,000)                                $150,000
Super balance $1,900,000                                       excluded
Boat (solely personal use)                                     excluded
Total net asset value                                        $4,400,000  <= $6,000,000  PASS
```

Basic conditions met via MNAV. **Variant:** if the portfolio were $2,500,000, the total is $6,300,000 -- MNAV fails by $300,000, both gateways fail, and only the general 50% discount applies. There is no shading: $6,000,001 is out.

### Example 2 -- Stacking to zero

Continuing Example 1: gain $900,000; premises active 8 of 8 years (>= half) -- active asset test passed. Not owned 15 years, so no 15-year exemption.

```
Capital gain                                    $900,000
less general 50% discount (held > 12 months)   -$450,000  -> $450,000
less 50% active asset reduction                -$225,000  -> $225,000
less retirement exemption (elects $225,000)    -$225,000  -> NET GAIN NIL
```

Nadia is 58 -- 55+ just before making the choice, so NO super payment is required. Lifetime retirement-exemption tally: $225,000 used, $275,000 remains. She may still voluntarily contribute the $225,000 to super under the CGT cap (Rule 14). Without the retirement exemption her tax would have been $225,000 x 47% = **$105,750** (11.75% effective on the gross gain); with it, **nil**.

### Example 3 -- Retirement exemption under 55: super is compulsory

Marco (48) sells an active asset in March 2027: gain $600,000, held 4 years, basic conditions met.

```
Gain $600,000 -> discount -> $300,000 -> 50% AAR -> $150,000
Retirement exemption elected: $150,000 -> net gain NIL
```

Because Marco is **under 55 just before making the choice**, he MUST pay $150,000 into a complying super fund/RSA by the later of making the choice and receiving the proceeds -- with a **CGT cap election (NAT 71161) given to the fund at or before the contribution**. The $150,000 is excluded from his $130,000 (2026-27) NCC cap and uses $150,000 of his $1,935,000 lifetime CGT cap. Lifetime retirement limit remaining: $350,000. (A 53-54 year-old wanting the cash instead could roll over for up to 2 years and choose the retirement exemption after turning 55 -- planning; escalate.)

### Example 4 -- Share sale with the stakeholder tests

Priya has owned 40% of OpCo Pty Ltd (one ordinary class, equal rights) for 9 years; unrelated Kai owns 60%. She sells her parcel in October 2026 for a $700,000 gain. Extra conditions (Rule 8):

1. Priya carries on no business -- she must pass MNAV herself. Her 40% >= 40% makes her **connected** with OpCo, so OpCo's net assets count: total $4.2m <= $6m. PASS.
2. Direct SBPP = smallest of voting/dividend/capital = 40% >= 20% -- **significant individual**, hence CGT concession stakeholder. PASS (90% test not needed for an individual claimant who is a stakeholder).
3. OpCo is a CGT SBE (aggregated turnover $1.6m), applying the modified connected-entity rule. PASS.
4. Modified active asset test: OpCo assets at market value $2.0m; active assets $1,550,000 + inherently-connected cash and receivables $250,000 = $1,800,000; $1,800,000 / $2,000,000 = **90% >= 80%**. PASS.

Waterfall: $700,000 -> discount -> $350,000 -> AAR -> $175,000 -> retirement exemption/rollover available. **Fail variants:** if Priya held non-voting shares with discretionary dividends, her smallest percentage could be 0% -- not a significant individual, concessions denied. If a HoldCo she owns 100% held the 40% instead and sold, Priya's indirect SBPP in OpCo = 100% x 40% = 40% (stakeholder), and stakeholders of OpCo hold 100% >= 90% of HoldCo -- the **90% test** rescues the HoldCo sale.

### Example 5 -- 15-year exemption plus CGT cap contribution

Colin (62) contracts in September 2026 to sell farmland owned 22 years, used in his primary production business for 16 of those years (>= 7.5-year test), turnover $850,000, retiring to part-time consulting (significant reduction -- "in connection with retirement"). Gain $1,100,000; proceeds $2,100,000.

The gain is **fully disregarded** under the 15-year exemption -- no discount, no losses consumed, retirement lifetime limit untouched. Colin may contribute up to the **capital proceeds** to super under the CGT cap: maximum exclusion **$1,935,000** (2026-27 cap; the remaining $165,000 of proceeds would be an ordinary NCC against his $130,000 cap -- flag bring-forward analysis). Deadline: later of his 2026-27 lodgment due date and 30 days after receiving proceeds; NAT 71161 at or before each contribution.

### Example 6 -- Rollover with no replacement: CGT event J5

A trading trust rolls over a $180,000 remainder (after discount and AAR) from a March 2027 disposal. Replacement asset period: March 2026 to March 2029. By March 2029 it has acquired nothing. **CGT event J5** happens at the end of the period: a $180,000 capital gain arises in 2028-29 -- no discount, no AAR, no 15-year exemption. The trust may choose the **retirement exemption** without re-meeting the basic conditions, but must have a CGT concession stakeholder to pay (Rule 11). NOTE: this J5 gain arises AFTER 1 July 2027 -- how the reform's indexation/minimum-rate rules treat J-event gains from pre-reform rollovers is not yet settled in ATO guidance. Escalate (R-AU-SBC-5).

## Section 11 -- Refusal catalogue

### R-AU-SBC-1 -- Look-through earnout rights

**Trigger:** sale consideration includes contingent financial benefits over up to 5 years (Subdiv 118-I). **Issue:** MNAV valuation choices for the right, prior-year amendments as benefits arrive, retirement-exemption payment and CGT cap timing recalibrated to each benefit, extended replacement periods. **Action:** refuse computation; document the earnout terms; escalate.

### R-AU-SBC-2 -- Marriage/relationship breakdown rollovers combined with Div 152

**Trigger:** asset previously transferred under a Subdiv 126-A breakdown rollover now claimed under Div 152. **Issue:** the transferee inherits acquisition history for some purposes but active-asset and 15-year continuity questions (and s 152-45 modifications) are fact-heavy and unforgiving. **Action:** map the transfer chain; escalate.

### R-AU-SBC-3 -- Non-resident or temporary-resident stakeholders

**Trigger:** any significant individual, spouse stakeholder, or claimant who is (or becomes) a foreign or temporary resident; non-resident object entities; assets that are not taxable Australian property. **Issue:** residency interacts with the discount denial, the 80% test's residency limb, and payment mechanics. **Action:** refuse analysis; escalate.

### R-AU-SBC-4 -- Pre-CGT assets

**Trigger:** asset acquired before 20 September 1985. **Issue:** gains generally disregarded without Div 152 -- but the Tax Reform No. 1 Act 2026 removes pre-CGT status after 30 June 2027 (deemed re-acquisition), making the exemption's endgame a valuation and timing problem. **Action:** never assume continued exemption; escalate.

### R-AU-SBC-5 -- Transactions straddling 1 July 2027

**Trigger:** contracts, settlements, rollover tails (J2/J5/J6), retirement-exemption payments or CGT cap contributions falling on either side of 1 July 2027, or requests to time a sale around it. **Action:** compute the pre-reform position only, labelled as such; refuse timing recommendations; escalate.

### R-AU-SBC-6 -- Death, incapacity evidence, and extensions of time

**Trigger:** deceased-estate claims outside the 2-year window, permanent-incapacity determinations, or any Commissioner discretion (replacement-period or 2-year extensions). **Action:** state the standard rule; refuse to assume a discretion will be exercised; escalate.

## Section 12 -- Excel working paper template

```
AUSTRALIA DIV 152 -- SBCGT ELIGIBILITY AND WATERFALL
Taxpayer: [name/entity]   CGT event + date (CONTRACT date): [____]
Income year: 2026-27      Prepared: [date]

GATEWAY
  Aggregated turnover (self + connected + affiliates): AUD [____]  < $2m? [Y/N]
  Connected entities (>= 40% control) mapped:          [list]
  Affiliates (acts in concert) mapped:                 [list]
  MNAV just before event (per schedule):               AUD [____]  <= $6m? [Y/N]
    - main residence % included / super excluded / personal-use excluded? [Y/N]
  Passively-held asset rules relied on?                [Y/N -- business entity: ____]

ACTIVE ASSET TEST
  Ownership period: [____] yrs   Active periods: [____] yrs
  Test: >= half, or >= 7.5 yrs if owned > 15 yrs:      [PASS/FAIL]
  Rent component? Carve-out (affiliate/connected user) evidenced? [____]

SHARES/UNITS ONLY (s 152-10(2))
  Claimant carried on business OR own MNAV pass:       [____]
  Stakeholder status / 90% test (SBPP workings):       [____]
  Object entity CGT SBE or MNAV (modified rule):       [____]
  Modified active asset test: [active+cash] / [total] = [____]% >= 80%? [Y/N]

WATERFALL (per gain)
  Gross gain:                       AUD [____]
  15-year exemption? (15 yrs + 55+/retirement or incapacity) [Y/N -> if Y, STOP]
  less capital losses:              AUD [____]
  less general 50% discount:        AUD [____]   (individual/trust only; > 12 mths)
  less 50% AAR (unless choose-out): AUD [____]   (choose-out reason: ____)
  less retirement exemption:        AUD [____]   (lifetime register below)
  less rollover:                    AUD [____]   (replacement period ends: ____)
  NET CAPITAL GAIN:                 AUD [____]

REGISTERS
  Retirement exemption lifetime ($500,000): prior use AUD [____] + this AUD [____]
  Under 55 at choice? Super payment made + date:        [____]
  CGT cap (2026-27 $1,935,000): prior use AUD [____] + this AUD [____]
  NAT 71161 given at/before contribution?               [Y/N + date]
  Company/trust: stakeholder payment within 7 days (152-D) / 2 yrs (152-B)? [____]

REVIEWER FLAGS
  [R-AU-SBC items triggered; post-1 July 2027 exposure]
```

## Section 13 -- Reference material

### Key figures

| Item | Value |
|---|---|
| Gateways | < $2m aggregated turnover (CGT SBE) OR <= $6m MNAV (not indexed) |
| Active asset period | >= half of ownership, or >= 7.5 years if owned > 15 years |
| Significant individual / stakeholder | SBPP >= 20% / significant individual or spouse with > 0% |
| 90% test / modified active asset test | 90% SBPP in claimant entity / 80% underlying-asset threshold |
| Retirement exemption | $500,000 lifetime per individual; under-55 super payment compulsory |
| Rollover window | 1 year before to 2 years after event; J5/J6 at period end; J2 later |
| CGT cap | 2026-27: $1,935,000; 2025-26: $1,865,000 (NCC caps: $130,000 / $120,000) |
| Company/trust payment windows | Retirement: 7 days after later of choice/proceeds; 15-year: 2 years |
| From 1 July 2027 | AAR turnover gateway $10m (law); indexation + 30% minimum replaces discount |

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| Statute | ITAA 1997 Div 152: Subdiv 152-A (basic conditions, ss 152-10 to 152-49), 152-B (15-year), 152-C (50% AAR), 152-D (retirement), 152-E (rollover); ss 104-185/190/197-198 (J2/J5/J6); s 292-100 (CGT cap) |
| ATO hub | Small business CGT concessions (QC 72742); eligibility conditions (QC 72743) |
| Gateways | Maximum net asset value test (QC 52270); CGT small business entity eligibility pages under QC 72743 |
| Active asset test | QC 52271 (updated 2 February 2026) -- rent carve-out, 80% test |
| Shares/trust interests | Additional conditions (QC 52283) -- stakeholder, SBPP, 90% test, modified tests |
| The four concessions | 15-year exemption (QC 52288); 50% active asset reduction (QC 52289); retirement exemption (QC 52290); roll-over (QC 52291) |
| CGT cap amount | ATO key super rates and thresholds -- contributions caps, Table 6 (QC 18123); CGT cap election form NAT 71161 |
| Reform | Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Royal Assent 26 June 2026); 2026-27 Budget (12 May 2026); Treasury consultations on start-up carve-out and trust minimum tax (not law) |

### Test suite

**Test 1:** Turnover $3.4m, MNAV $4.4m. -> Gateway passes via MNAV; turnover irrelevant.

**Test 2:** MNAV $6,000,001. -> Fails; no Div 152; general discount only.

**Test 3:** Premises leased 100% to the owner's own trading company for 10 of 10 years. -> Rent disregarded (s 152-40(4A)); active asset.

**Test 4:** Same premises leased to unrelated tenants for 6 of 10 years, own business 4. -> Main use deriving rent for the majority; fails unless facts change the main-use conclusion; flag.

**Test 5:** Individual gain $900,000, discount + AAR + retirement $225,000. -> Net gain nil; lifetime tally $225,000; 58yo -> no super payment.

**Test 6:** Same but company. -> No discount: $900,000 -> AAR $450,000 -> retirement exemption capped at $500,000 per stakeholder; consider choosing OUT of AAR so two 50% stakeholders can extract $450,000 each ($900,000 total) tax-free within their lifetime limits.

**Test 7:** 30% shareholding, one equal-rights class. -> SBPP 30%; significant individual; stakeholder.

**Test 8:** Discretionary trust, no distribution and tax loss in event year; last distribution year gave A 21%. -> A is a significant individual via the prior-year rule.

**Test 9:** Rolled over $200,000; replacement cost only $150,000 at period end. -> J6 gain $50,000; retirement exemption only.

**Test 10:** Retirement exemption $150,000, taxpayer 48. -> Compulsory super payment $150,000; NAT 71161 at/before contribution; excluded from NCC cap; CGT cap reduced to $1,785,000.

**Test 11:** 2027-28 disposal, turnover $7m, net assets $8m. -> Post-reform: 50% AAR available ($10m gateway, law from 1 July 2027); 15-year/retirement/rollover NOT available (fails $2m and $6m); escalate for indexation/minimum-rate mechanics.

### Prohibitions

- NEVER apply any concession before the gateway AND active asset test are evidenced at the CGT event (contract) date
- NEVER treat a rent-deriving asset as active without checking the affiliate/connected-entity carve-out -- and never the reverse
- NEVER apply the general 50% discount to a company, or any discount/AAR/15-year to a J5/J6 gain
- NEVER exceed the $500,000 lifetime retirement limit or skip the under-55 compulsory super payment
- NEVER treat a CGT cap contribution as excluded without a NAT 71161 given at or before the contribution
- NEVER use the $10m turnover gateway before 1 July 2027, or for any concession other than the 50% active asset reduction
- NEVER advise timing a disposal around 1 July 2027 -- compute the pre-reform position, label it, escalate
- NEVER present figures as definitive

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
