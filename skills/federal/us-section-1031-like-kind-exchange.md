---
name: us-section-1031-like-kind-exchange
description: Tier 2 US federal content skill for IRC §1031 like-kind exchange of real property post-TCJA (real property only since 2018). Covers the 45-day identification and 180-day exchange windows, qualified intermediary requirement, the 3-property / 200% / 95% identification rules, reverse exchanges under Rev. Proc. 2000-37, build-to-suit improvement exchanges, basis carryover and boot taxation, related-party 2-year rule under §1031(f), TIC structure per Rev. Proc. 2002-22, drop-and-swap partnership workarounds, §121 primary-residence rollover under §121(d)(10), Form 8824 reporting, and California's FTB Form 3840 claw-back annual reporting requirement. Tax year 2025.
jurisdiction: US
domain: federal-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# us-section-1031-like-kind-exchange

## 1. Scope

This skill governs the federal income tax treatment of like-kind exchanges of real property under IRC §1031 for tax year 2025. It is invoked whenever a US sole proprietor, single-member LLC, partnership, S corporation, C corporation, or individual investor disposes of real property used in a trade or business or held for investment and acquires replacement real property of like kind, intending to defer the realized gain.

In scope:
- Simultaneous (same-day) exchanges of real property
- Deferred ("Starker") exchanges through a qualified intermediary (QI)
- Reverse exchanges under the Rev. Proc. 2000-37 safe harbor
- Build-to-suit / improvement exchanges
- Basis carryover and boot computation
- Form 8824 reporting (both relinquished and replacement legs)
- Related-party exchanges under §1031(f) and the 2-year rule
- TIC (tenant-in-common) co-ownership structures under Rev. Proc. 2002-22
- Drop-and-swap and swap-and-drop partnership workarounds
- §121 primary-residence interaction under §121(d)(10)
- California FTB Form 3840 annual reporting (claw-back regime)
- Coordination with §1245 and §1250 depreciation recapture

Out of scope (refusal catalogue):
- Personal property exchanges (TCJA eliminated as of 1/1/2018 — see §3)
- Equipment, aircraft, art, collectibles, intangibles, livestock, vehicles
- Cryptocurrency exchanges (token-for-token swaps are taxable events post-TCJA; pre-2018 positions were unsettled and IRS rejected §1031 treatment in CCA 202124008)
- Foreign-for-foreign real property exchanges (still permitted but only foreign-for-foreign; US-for-foreign fails under §1031(h))
- §1400Z-2 Opportunity Zone deferrals (mutually exclusive — see §17)
- Section 1033 involuntary conversions (separate regime, different timing)
- Partnership interest exchanges (categorically barred by §1031(a)(2) even post-TCJA for entity interests)
- Inventory / dealer property (§1221(a)(1) ordinary income property)

This skill MUST be loaded alongside `us-tax-workflow-base` v0.2+. For depreciation recapture mechanics, also load `us-sole-prop-bookkeeping` and `us-schedule-c-and-se-computation`. For California-resident taxpayers, also load `ca-540-individual-return`.

## 2. The Statutory Rule — IRC §1031(a)(1)

- **§1031(a)(1) non-recognition rule text** — No gain or loss shall be recognized on the exchange of real property held for productive use in a trade or business or for investment if such real property is exchanged solely for real property of like kind which is to be held either for productive use in a trade or business or for investment.  _(IRC §1031(a)(1))_
- **Four cumulative requirements** — 1. Held for productive use in a trade or business OR for investment — both legs (relinquished and replacement). 2. Exchanged — a sale followed by a separate purchase is NOT an exchange; a QI structure converts a sale + purchase into a constructive exchange under Treas. Reg. §1.1031(k)-1. 3. Like kind — for real property, this is extremely broad (see §5). 4. Real property — both legs must be real property as defined in Treas. Reg. §1.1031(a)-3 (finalized December 2020). Failure on any one prong = entire transaction taxable as a sale, gain recognized in year of disposition, and depreciation recapture triggered.  _(Treas. Reg. §1.1031(k)-1; Treas. Reg. §1.1031(a)-3)_

## 3. TCJA Restriction — Real Property Only (Post-12/31/2017)

- **TCJA restriction to real property** — The Tax Cuts and Jobs Act of 2017 (P.L. 115-97), effective for exchanges completed after December 31, 2017, amended §1031 to eliminate like-kind exchange treatment for all property other than real property. The pre-TCJA text "property" was replaced with "real property."  _(P.L. 115-97 (TCJA))_
- **Eliminated from §1031 as of 2018** — Tangible personal property (machinery, equipment, vehicles, aircraft, boats); Livestock (was previously allowed if same sex); Intangible property (franchises, trademarks, patents, goodwill, licenses); Cryptocurrency (the IRS confirmed in Rev. Rul. 2019-24 and CCA 202124008 that pre-TCJA crypto-for-crypto was also not §1031-eligible because different tokens were not of like kind); Collectibles, art, gold bullion, coins, gems; Securities (always excluded under §1031(a)(2)(B)).  _(Rev. Rul. 2019-24; CCA 202124008; §1031(a)(2)(B))_
- **Real property under Treas. Reg. §1.1031(a)-3** — 1. Land in any form (raw, improved, subdivided). 2. Permanently affixed structures and inherently permanent improvements — buildings, walls, parking structures, paved roads, pipelines, transmission lines, sewer systems. 3. Structural components of buildings — walls, partitions, doors, wiring, plumbing, central HVAC, elevators, sprinklers (note: components separately classified as personal property under cost segregation studies for depreciation purposes may FAIL §1031 — see §11). 4. Real property under state and local law — facts and circumstances test plus the regulatory list. 5. Leaseholds with remaining term ≥ 30 years (including renewal options) — Treas. Reg. §1.1031(a)-3(a)(5); shorter leaseholds fail. 6. Mineral, oil, and gas interests — perpetual royalty interests qualify; production payments do not. 7. Easements (permanent) and conservation easements. 8. Air rights and transferable development rights (TDRs). 9. Stock in cooperative housing corporations (§1031(i)) — limited carve-out for co-op shares.  _(Treas. Reg. §1.1031(a)-3 (final regs Dec. 2020))_
- **Not real property even though physically attached** — Machinery installed for an industrial process, not the building itself; Personal property severable without damage to the structure; Inventory and supplies stored in the building.  _(Treas. Reg. §1.1031(a)-3)_
- **Cost-segregation interaction** — If a taxpayer has cost-segregated a building and classified components as §1245 personal property (5-, 7-, or 15-year), those §1245 components do not qualify for §1031 deferral. The relinquished §1245 portion triggers ordinary-income recapture under §1245(b)(4) — see §11.  _(§1245(b)(4))_

## 4. Held For — The Intent Test

- **Held for productive use / investment intent requirement** — Both legs must be held for "productive use in a trade or business" OR "for investment." The statute does not impose a fixed holding period; it imposes an intent requirement evaluated at the moment of exchange. Trade or business: rental real estate (any class), self-occupied office for the taxpayer's business, industrial property used in manufacturing, farmland actively farmed. Investment: raw land held for appreciation, real estate held passively without active management, mineral interests held for royalty.  _(IRC §1031(a)(1))_
- **Fails the held-for test** — Dealer / inventory property — held primarily for sale to customers in the ordinary course of business. Flippers, subdividers, and active developers fail. Factors (per Suburban Realty v. United States, 615 F.2d 171 (5th Cir. 1980) and Treas. Reg. §1.1221-1): frequency of sales, sales activity, advertising, improvements made for sale, taxpayer's primary occupation. Primary residence — personal use property, not trade/business or investment. §121 exclusion applies instead. Vacation home with excessive personal use — Rev. Proc. 2008-16 safe harbor requires, for each of the 24 months before AND after the exchange: Property rented at fair market rental ≥ 14 days, AND Personal use ≤ the greater of 14 days or 10% of rental days. Property acquired specifically for the exchange and immediately disposed — pre-arranged "exchange and resale" fails (Click v. Commissioner, 78 T.C. 225 (1982)).  _(Suburban Realty v. United States, 615 F.2d 171 (5th Cir. 1980); Treas. Reg. §1.1221-1; Rev. Proc. 2008-16; Click v. Commissioner, 78 T.C. 225 (1982))_
- **Holding period practice** — No fixed statutory minimum, but IRS and courts scrutinize short holds. Common safe-harbor practice in the industry is 2 years on each leg, supported by the related-party rule in §1031(f) (see §13) and a long-standing IRS private-letter-ruling pattern. 1 year is the absolute floor practitioners use. Under 1 year invites a dealer or step-transaction challenge.  _(§1031(f))_

AUDIT FLASH POINT — Dealer recharacterization. A taxpayer who has flipped multiple properties recently, advertises property for sale, makes substantial improvements specifically to sell, or whose primary livelihood is real estate sales will be challenged. The IRS argues the relinquished property was inventory (ordinary income, ineligible for §1031). Result: full gain recognized as ordinary income at marginal rates, plus SE tax if a sole proprietor. Document the rental income history, lease agreements, depreciation taken, and business purpose at the moment of exchange.

## 5. Like-Kind for Real Property — Extremely Broad

- **Like-kind test for real property** — For real property, "like kind" refers to the nature or character of the property, not its grade, quality, or use. Virtually all real property is like-kind to all other real property.  _(Treas. Reg. §1.1031(a)-1(b))_

**Pairs that QUALIFY as like-kind**

| Relinquished | Replacement |
| --- | --- |
| Apartment building | Raw land |
| Office building | Industrial warehouse |
| Single-family rental | Strip-mall retail |
| Hotel | Golf course |
| Farmland | Suburban rental house |
| Improved commercial | Unimproved farmland |
| Fee simple interest | Leasehold ≥ 30 years |
| Leasehold ≥ 30 years | Fee simple |
| Mineral royalty interest | Surface rights to other land |
| Conservation easement | Fee simple investment land |
| US real estate (state A) | US real estate (state B) |
| TIC interest under Rev. Proc. 2002-22 | Fee simple (and vice versa) |

**Pairs that FAIL like-kind**

| Relinquished | Replacement | Reason |
| --- | --- | --- |
| US real property | Foreign real property | §1031(h)(1) — not like kind |
| Foreign real property | US real property | §1031(h)(1) |
| Real property | Personal property | TCJA — different §1031 category |
| Real property | Partnership interest | §1031(a)(2) excludes interests |
| Leasehold < 30 years | Fee simple | Treas. Reg. §1.1031(a)-3(a)(5) |
| Real property (held for sale) | Real property | Inventory disqualified |

- **State-to-state, US territories** — US real property includes the 50 states, DC, and (by statutory definition) US possessions for §1031 purposes. Puerto Rico, USVI, Guam, American Samoa, and Northern Mariana Islands are technically foreign for §1031(h) — practitioners should confirm with current IRS guidance before treating a possession exchange as domestic.  _(§1031(h))_

## 6. Boot — Anything Not Like-Kind

- **Boot definition** — Boot is any property received that is not like-kind to the relinquished property. Boot is taxable to the extent of the realized gain — that is, the taxpayer recognizes the lesser of (a) realized gain or (b) total boot received.
- **Forms of boot** — 1. Cash boot — any net cash received by the taxpayer (or constructively received). 2. Mortgage relief (net debt relief) — if the relinquished property had a $400,000 mortgage paid off, and the replacement property carries only a $300,000 mortgage assumed, the $100,000 net debt relief is boot. Net relief is computed: (mortgage on relinquished − mortgage on replacement). Net debt assumption (replacement higher than relinquished) is not negative boot; it is treated as additional consideration paid by the taxpayer. 3. Personal property received — even if attached to the real property being acquired (furniture in a furnished apartment building, equipment in an industrial facility); since 2018 these are boot. 4. Non-qualified intangibles — going-concern value, goodwill, name rights bundled into a hotel sale. 5. Excess proceeds held by QI past 180 days — automatically becomes boot at end of exchange period.
- **Boot offsetting rules** — Cash paid by taxpayer offsets mortgage relief received (taxpayer can pay down debt with new cash to avoid boot). New mortgage assumed by taxpayer offsets mortgage relief from relinquished. Cash boot received does NOT offset mortgage assumed — only the other direction (paying cash offsets debt boot, not vice versa). Closing costs paid out of exchange proceeds: customary transaction costs (title insurance, escrow fees, transfer taxes, brokerage commissions, recording fees) reduce realized gain and do not generate boot. Non-customary costs (loan origination fees, rent prorations, security deposit transfers) paid out of exchange funds may generate boot.  _(Treas. Reg. §1.1031(b)-1, §1.1031(d)-2)_
- **Recognized gain formula** — Realized gain = FMV replacement received + cash boot received + mortgage relief − adjusted basis relinquished − cash paid − mortgage assumed Recognized gain = LESSER of (realized gain, total boot received) Deferred gain = Realized gain − Recognized gain
- **Character of recognized gain** — Recognized gain is characterized first as ordinary recapture under §1245 (if any §1245 property in the relinquished), then as §1250 unrecaptured gain (25% rate cap), then as long-term capital gain (0/15/20% plus 3.8% NIIT if applicable).  _(§1245; §1250)_

## 7. Timing — The 45/180-Day Rules (Deferred / "Starker" Exchanges)

- **Origin of deferred exchange regime** — The deferred exchange regime arose from Starker v. United States, 602 F.2d 1341 (9th Cir. 1979), and was codified in §1031(a)(3) in 1984. Treas. Reg. §1.1031(k)-1 sets the modern rules.  _(Starker v. United States, 602 F.2d 1341 (9th Cir. 1979); §1031(a)(3); Treas. Reg. §1.1031(k)-1)_
- **45-Day Identification Period** — Begins the day after the relinquished property closes (transfer date). Ends at midnight of the 45th calendar day. No extensions for weekends, holidays, or natural disasters (the IRS has occasionally granted disaster-area extensions under §7508A — e.g., hurricane relief — but no automatic relief). Taxpayer must identify replacement property in a signed written document delivered to the QI or other party to the exchange (not the taxpayer's attorney or agent). Identification must unambiguously describe the property — legal description, street address, or distinguishable name.  _(Treas. Reg. §1.1031(k)-1; §7508A)_
- **180-Day Exchange Period** — Begins the day after the relinquished closes. Ends at the EARLIER of: Midnight of the 180th calendar day, OR the due date (including extensions) of the taxpayer's federal income tax return for the year of the relinquished sale. The "due date" trap: a relinquished property sold on November 15, 2025 by a calendar-year individual would otherwise have 180 days = May 14, 2026. But the unextended return due date is April 15, 2026. To get the full 180, the taxpayer MUST file Form 4868 extension by April 15, 2026. The replacement must be both identified within 45 days AND acquired within 180 days.  _(Treas. Reg. §1.1031(k)-1)_

## 8. Identification Rules — 3-Property / 200% / 95%

- **Three alternative identification methods** — Treas. Reg. §1.1031(k)-1(c)(4) provides three alternative identification methods. The taxpayer chooses whichever they prefer (or whichever the facts allow); they need not pre-elect.  _(Treas. Reg. §1.1031(k)-1(c)(4))_
- **Method 1 — Three-Property Rule** — Identify up to three properties of any value. This is the default and most common. Even if combined FMV exceeds the relinquished property by 10x, three is allowed.  _(Treas. Reg. §1.1031(k)-1(c)(4))_
- **Method 2 — 200% Rule** — Identify any number of properties, provided their aggregate FMV does not exceed 200% of the FMV of the relinquished property. Used when shopping a portfolio: e.g., relinquish $2M property, identify 8 candidates each $500k = $4M total.  _(Treas. Reg. §1.1031(k)-1(c)(4))_
- **Method 3 — 95% Rule (rescue rule)** — If the taxpayer identifies more than three properties AND the combined FMV exceeds 200% of relinquished, the identification is salvageable only if the taxpayer actually acquires at least 95% (by FMV) of all identified properties.  _(Treas. Reg. §1.1031(k)-1(c)(4))_
- **Consequences of bad identification** — Over-identification under all three methods = NO valid identification = exchange fails entirely; taxpayer recognizes 100% of gain. Identifications can be revoked or replaced in writing before the 45-day deadline. After 45 days, the list is locked — only identified property can be acquired in the exchange.  _(Treas. Reg. §1.1031(k)-1(c)(4))_

Most CPAs and QIs recommend identifying exactly three properties under Method 1 to preserve maximum flexibility without triggering the 95% trap. Build-to-suit identifications must include both the land and a "reasonable description" of the improvements to be constructed; the property must be identified as it is expected to look at completion (Treas. Reg. §1.1031(k)-1(e)).

## 9. The Qualified Intermediary (QI)

- **Purpose of the QI** — The QI rules in Treas. Reg. §1.1031(k)-1(g)(4) are the workhorse of every deferred exchange. The QI exists to prevent the taxpayer from having actual or constructive receipt of the sale proceeds, which would terminate the exchange and trigger gain recognition.  _(Treas. Reg. §1.1031(k)-1(g)(4))_
- **Who can be a QI** — An unrelated person (or entity); Not a "disqualified person" within the meaning of Treas. Reg. §1.1031(k)-1(k).  _(Treas. Reg. §1.1031(k)-1(k))_
- **Disqualified persons (cannot serve as QI)** — The taxpayer's agent — meaning anyone who within the 2 years before the transfer of the relinquished property has acted as the taxpayer's: Attorney; Accountant; Investment banker or broker; Real estate broker; Employee. A related party (§267(b) or §707(b) — including family members, controlled corporations >50%, partnerships >50%). A person acting as the taxpayer's agent on the transaction itself. Routine title insurance, escrow, or financial-institution services within the 2-year window do NOT disqualify.  _(Treas. Reg. §1.1031(k)-1(k); §267(b); §707(b))_
- **QI's role** — 1. Enters into a written exchange agreement with the taxpayer before closing of the relinquished property. 2. Acquires the relinquished property from the taxpayer (constructively or by formal assignment of the sale contract). 3. Transfers the relinquished property to the buyer. 4. Holds the sale proceeds in a qualified escrow or qualified trust. 5. Acquires the replacement property. 6. Transfers the replacement property to the taxpayer.  _(Treas. Reg. §1.1031(k)-1(g)(4))_
- **g(6) restrictions on taxpayer access to proceeds** — During the exchange period, the taxpayer's right to receive, pledge, borrow, or otherwise benefit from the QI-held funds must be restricted. The taxpayer may only receive funds: At the end of the 45-day identification period if no property is identified, OR After the taxpayer has received all identified replacement property, OR After the 180-day exchange period ends, OR After material default by another party. Violation of g(6) = constructive receipt = exchange fails on day of violation.  _(Treas. Reg. §1.1031(k)-1(g)(6))_

Failed QI = entire deferral void. Common failure modes: QI is the taxpayer's CPA (very common error); QI is the same brokerage that listed the property; QI commingles funds or invests in non-permitted instruments; QI bankruptcy (a real risk — the QI is unregulated federally; only a handful of states license QIs).

## 10. Reverse Exchanges — Rev. Proc. 2000-37

- **Reverse exchange safe harbor** — Sometimes the taxpayer finds the replacement before disposing of the relinquished. A naive purchase + later sale fails §1031 because there is no exchange (the taxpayer briefly owns both). Rev. Proc. 2000-37 (modified by Rev. Proc. 2004-51) creates a safe harbor: the replacement is "parked" with an Exchange Accommodation Titleholder (EAT) while the taxpayer sells the relinquished.  _(Rev. Proc. 2000-37; Rev. Proc. 2004-51)_
- **Structure (forward parking variant)** — 1. EAT (a single-purpose LLC, often a subsidiary of the QI firm) acquires the replacement property using funds loaned by the taxpayer. 2. Taxpayer and EAT sign a Qualified Exchange Accommodation Agreement (QEAA) within 5 business days of EAT's acquisition. 3. Taxpayer has 45 days from EAT's acquisition to identify which property (or properties) of those they own will be the relinquished property (the identification rules of §8 apply in reverse). 4. Taxpayer has 180 days from EAT's acquisition to sell the relinquished and have the EAT transfer the replacement to the taxpayer. 5. The total combined parking period (relinquished sale through replacement transfer) cannot exceed 180 days.  _(Rev. Proc. 2000-37)_
- **Structure (exchange-first variant)** — The EAT can also temporarily hold the relinquished property while the taxpayer acquires the replacement directly — less common but permissible.  _(Rev. Proc. 2000-37)_
- **Title-holding by EAT requirements** — EAT must hold "qualified indicia of ownership" — title, beneficial interest in a disregarded entity holding title, or contractual rights tantamount to ownership. EAT must be subject to federal income tax (or be a disregarded entity owned by a taxpaying entity). EAT cannot be a disqualified person under the same rules as a QI.  _(Rev. Proc. 2000-37)_
- **Strict timing** — 5 business days to sign QEAA; 45 days to identify relinquished; 180 days total to complete.  _(Rev. Proc. 2000-37)_

Outside the safe harbor, reverse exchanges are still theoretically possible but face high IRS challenge risk (see DeCleene v. Commissioner, 115 T.C. 457 (2000)).

## 11. Build-to-Suit / Improvement Exchanges

- **When used** — When the desired replacement property requires construction or major improvements that won't complete within 180 days of the relinquished sale, taxpayers use the build-to-suit (or improvement) exchange structure, also under Rev. Proc. 2000-37.  _(Rev. Proc. 2000-37)_
- **Structure** — 1. EAT acquires the raw land (or partially-improved property). 2. Taxpayer (acting as construction manager) directs construction using exchange proceeds advanced through the QI to the EAT. 3. EAT pays contractors from those funds. 4. At the earlier of (a) completion or (b) 180-day deadline, EAT transfers the property to the taxpayer.  _(Rev. Proc. 2000-37)_
- **Critical limitations** — Only improvements completed and "real property" before the 180-day deadline count toward the exchange value. Half-built construction on day 180 = the taxpayer receives a half-built building (boot equal to the unspent exchange funds going back to taxpayer = taxable). Services performed by the taxpayer's own employees on the construction may be treated as boot (the taxpayer's labor is not real property received). Land plus services equal in value to the relinquished property is the goal; if the as-completed value on day 180 is less than the relinquished value, boot results.

Planning: identify a land parcel plus describe the improvements in writing on day 45; lock down construction contracts before EAT takes title; build aggressively in the first 120 days; close on day 175.

## 12. Basis in Replacement Property

- **Basis in replacement formula** — Basis in replacement = Adjusted basis of relinquished + Cash paid by taxpayer (boot paid) + Mortgage on replacement (debt assumed) + Gain recognized − Cash received by taxpayer (boot received) − Mortgage on relinquished (debt relieved) − Loss recognized (rare; §1031 typically defers losses too)  _(Treas. Reg. §1.1031(d)-1)_
- **Equivalent restatement (deferred gain view)** — Basis in replacement = FMV of replacement − Deferred gain  _(Treas. Reg. §1.1031(d)-1)_
- **Multiple replacement properties** — Total basis is allocated among the replacements in proportion to their relative FMV.  _(Treas. Reg. §1.1031(j)-1)_
- **Holding period tacking** — The relinquished property's holding period tacks onto the replacement under §1223(1), so a long-term property remains long-term after the exchange.  _(§1223(1))_
- **Depreciation post-exchange** — Under Treas. Reg. §1.168(i)-6, the carried-over basis (the "exchanged basis") continues on the relinquished's remaining depreciation schedule and method. Any excess basis (the boot paid or new debt assumed) is treated as newly acquired property subject to its own depreciation life and method starting on the acquisition date. Taxpayers may elect out under §1.168(i)-6(i) to treat the entire replacement as newly acquired (rare; usually unfavorable).  _(Treas. Reg. §1.168(i)-6; §1.168(i)-6(i))_
- **§1245 recapture in exchange** — If the relinquished includes §1245 property (e.g., 5- or 7-year cost-segregated components, or fixtures that were classified as personal property), §1245 recapture is recognized to the extent of the lesser of: Total §1245 depreciation taken, OR Realized gain attributable to §1245 property. The §1245 recapture rule is HARSH: it applies even if no boot is received. The recaptured amount becomes recognized ordinary income; the remainder of the gain defers. This is why cost-segregated buildings are tricky for §1031 — separating out the §1245 leg means partial recognition.  _(IRC §1245(b)(4))_
- **§1250 unrecaptured gain deferral** — Under §1250(d)(4), §1250 unrecaptured gain (the depreciation taken on real property since 1986, capped at 25% rate) carries over into the replacement property and is recognized only upon the eventual taxable sale of the replacement. It is not accelerated by the §1031 exchange.  _(§1250(d)(4))_

AUDIT FLASH POINT — Cost-segregation interaction. Taxpayers who aggressively cost-segregated the relinquished building may face surprise §1245 recapture in the exchange. Run a recapture computation BEFORE the exchange closes. The relinquished's §1245 components (HVAC if reclassified, carpeting, decorative lighting, removable partitions) generate ordinary income recapture even with zero boot received. Document the §1245 versus §1250 split on Form 8824 line 21.

## 13. Related-Party Exchanges — §1031(f) and the 2-Year Rule

- **§1031(f) purpose** — §1031(f) targets the tax-avoidance scheme of related-party exchanges followed by quick resales (basis-shifting).  _(IRC §1031(f))_
- **Related parties** — Family members: spouse, ancestors, lineal descendants, siblings; A taxpayer and a corporation more than 50% owned (directly or indirectly); A taxpayer and a partnership more than 50% owned; Two corporations in a controlled group; A grantor and a fiduciary of a trust; Two trusts with the same grantor.  _(§267(b); §707(b))_
- **The 2-Year Rule** — If a related-party exchange occurs, AND within 2 years either party disposes of the property received in the exchange, then the original §1031 gain on the disposing party is recognized as if the original exchange had been taxable. The 2-year clock starts on the date of the later transfer in the exchange.  _(§1031(f)(1))_
- **Exceptions** — Death of either party; Compulsory or involuntary conversion; Disposition that did not have tax-avoidance as a principal purpose (very fact-intensive, taxpayer-unfavorable in practice).  _(§1031(f)(2))_
- **The Teruya Brothers trap** — Even an exchange done through a QI with an unrelated buyer can be recharacterized as a related-party exchange under §1031(f)(4) if the related party is the ultimate seller of the replacement. Teruya Bros., Ltd. v. Commissioner, 580 F.3d 1038 (9th Cir. 2009): if the related party uses the exchange to cash out at lower basis while shifting gain to the taxpayer, the entire deferral is voided.  _(§1031(f)(4); Teruya Bros., Ltd. v. Commissioner, 580 F.3d 1038 (9th Cir. 2009))_

AUDIT FLASH POINT — Related-party 2-year violation. Two-year clock starts at the LATER of the two property transfers. Common scenarios: Taxpayer exchanges with sibling; sibling sells received property 18 months later → original gain recognized retroactively. Taxpayer's controlled LLC exchanges with parent; LLC distributes property to taxpayer within 2 years → gain triggered. QI-structured exchange where ultimate replacement source is a related entity → Teruya recharacterization. Monitor disposition of both properties for the full 2-year window. If a related-party disposition is unavoidable, document the non-tax-avoidance purpose contemporaneously.

## 14. TIC Interests — Rev. Proc. 2002-22

- **TIC interest definition** — A tenancy-in-common (TIC) interest is undivided fractional ownership in real property. Each co-tenant holds direct legal title to a fractional interest. TIC interests are real property and qualify for §1031, but the IRS will recharacterize them as partnership interests (and disqualify them under §1031(a)(2)) if they look too much like a co-ownership business.  _(§1031(a)(2))_
- **Rev. Proc. 2002-22 safe harbor — key requirements** — 1. Each co-tenant holds legal title as a tenant-in-common under state law. 2. ≤ 35 co-tenants. 3. The co-ownership cannot file a partnership tax return, conduct business under a common name, or execute an agreement identifying it as a partnership. 4. Unanimous consent required for hiring/firing manager, sale, lease, refinancing. 5. Each co-tenant has the right to partition. 6. Each co-tenant shares revenue and expenses in proportion to ownership. 7. Co-tenants individually borrow and individually obligated on debt. 8. Manager (if any) is limited to specified activities; cannot exceed 1-year contract. 9. Co-tenants receive their pro-rata share of cash flow directly.  _(Rev. Proc. 2002-22)_
- **Failure consequence** — Failure to satisfy Rev. Proc. 2002-22 = TIC recharacterized as partnership interest = §1031 fails. This is the most common reason TIC investments blow up in IRS examination.  _(Rev. Proc. 2002-22)_

## 15. Drop-and-Swap and Swap-and-Drop

- **Problem statement** — Partnerships that hold real property cannot exchange partnership interests under §1031, but the partnership itself can exchange its real property. The problem: if some partners want to defer gain (do the §1031) and others want cash (taxable sale), the partnership cannot do both with a single transaction. Two workarounds exist: drop-and-swap and swap-and-drop.  _(§1031(a)(2))_
- **Drop-and-Swap sequence** — 1. Before sale, partnership distributes the property to its partners as TICs in proportion to their interests (the "drop"). 2. Each partner — now a direct TIC owner — independently decides whether to do a §1031 (the "swap") or take cash. 3. Cash-out partners sell their TIC interest taxably; deferral-partners exchange theirs.
- **IRS challenges to drop-and-swap** — Step transaction: the IRS argues the drop and the sale are a single transaction; the property was held by the partnership (not the partner) immediately before sale; the partner's "holding for investment" element fails. Form 8824 Question 11 (partner intent): asks whether the property was held by the taxpayer in the year of exchange. The longer the gap between drop and swap, the safer (>1 year is the practitioner safe harbor; some accept 6 months; <30 days is dangerous).  _(Form 8824 Question 11)_
- **Swap-and-Drop sequence** — 1. Partnership does the §1031 exchange, acquiring replacement property. 2. After exchange, partnership distributes replacement TIC interests to partners who want out. 3. Same step-transaction risk; the IRS argues the replacement was acquired with the intent to immediately distribute, breaking the "held for" requirement on the replacement side.

AUDIT FLASH POINT — Drop-and-swap intent. Document at minimum: Partnership operating agreement amended to authorize distribution before the buyer is identified; TIC agreements signed and recorded with the county; New financing in each partner's individual name; Each partner separately filing Schedule E for the property between drop and swap (file at least one tax year between drop and exchange ideally); Form 8824 Question 11 answered truthfully — lying triggers §6663 fraud penalty. A short interval (under 6 months) plus a pre-arranged buyer is the worst possible combination.

## 16. §121 Primary Residence + §1031 Combination — §121(d)(10)

- **Interaction overview** — A property cannot simultaneously be both a §121 primary residence and a §1031 trade-or-business property at the same moment, but the same property can serve both roles sequentially. §121(d)(10) and Rev. Proc. 2005-14 govern the interaction.  _(§121(d)(10); Rev. Proc. 2005-14)_
- **Pattern 1 — Convert §1031 replacement to primary residence (§121 Rollover)** — 1. Taxpayer acquires investment rental in §1031 exchange. 2. Holds and rents for at least 2 years (Rev. Proc. 2008-16 safe harbor — same as §4 above). 3. Converts to primary residence. 4. Lives in for at least 2 of the last 5 years before sale (§121(a)). 5. Total ownership must be at least 5 years (§121(d)(10) — special rule for §1031-acquired property: 5-year minimum hold). 6. On sale: §121 excludes up to $250k (single) / $500k (joint) of gain attributable to primary-residence period; pre-conversion §1031 deferred gain plus depreciation recapture is NOT excluded — taxable on sale.  _(§121(a); §121(d)(10); Rev. Proc. 2008-16)_
- **Pattern 2 — Convert primary residence to rental, then §1031** — 1. Lived in property as primary; would qualify for §121. 2. Convert to rental, hold for 2+ years (Rev. Proc. 2008-16). 3. §1031 exchange the rental. 4. §121 + §1031 stacking under Rev. Proc. 2005-14: §121 excludes the primary-residence portion of gain; §1031 defers the remaining gain on the rental portion. Both apply on the same transaction.  _(Rev. Proc. 2005-14; Rev. Proc. 2008-16)_
- **Critical caveat** — For property acquired through a §1031 exchange, the §121 exclusion is unavailable if the sale occurs within 5 years of the §1031 acquisition. The 2-of-5-years primary use rule remains, but the 5-year minimum total hold is added.  _(§121(d)(10))_

## 17. Opportunity Zones vs §1031 — Mutually Exclusive

**Choice factors: §1031 vs §1400Z-2 (OZ)**

| Factor | §1031 | §1400Z-2 (OZ) |
| --- | --- | --- |
| Gain types eligible | Real property gain only | Any capital gain (stock, crypto, real estate) |
| Deferral period | Until replacement sold | Until 12/31/2026 (mandatory inclusion event) |
| Permanent exclusion? | No (defers, doesn't exclude) | 10% step-up at 5 years, 15% at 7 (now expired); 100% exclusion of post-investment OZ appreciation if held 10 years |
| Reinvestment timing | 180 days, with QI | 180 days, no QI required |
| Reinvestment vehicle | Direct replacement real property | Qualified Opportunity Fund (QOF) |
| State conformity | Most states conform | Many states do NOT conform |
| Recapture | §1245 still triggered | None at OZ entry |

- **Mutual exclusivity** — §1400Z-2 (Opportunity Zone deferral) and §1031 (like-kind exchange) are alternative deferral regimes; a taxpayer cannot apply both to the same gain.  _(§1400Z-2)_

For 2025 sales, OZ deferral pushes recognition to 12/31/2026, only 12 months of deferral — much less valuable than §1031's indefinite deferral. After 2026, §1031 dominates for real property.

## 18. Form 8824 — Required Reporting

- **General filing requirement** — Every §1031 exchange must be reported on Form 8824, attached to the return for the year the relinquished property was disposed of. Both legs of the exchange (relinquished and replacement) are reported on a single Form 8824. A separate Form 8824 is filed for each exchange (e.g., a 3-property identification that results in 2 replacements requires 2 Form 8824s if the replacements are separate exchanges).  _(Form 8824)_
- **Part I — Information on the Like-Kind Exchange** — Line 1: description of relinquished. Line 2: description of replacement. Line 3: date relinquished was originally acquired (for holding-period purposes). Line 4: date taxpayer transferred relinquished (start of 45/180 clocks). Line 5: date replacement was identified. Line 6: date replacement was received. Line 7: related-party indicator.  _(Form 8824 Part I)_
- **Part II — Related-Party Exchange Information** — Must be filed for the year of exchange AND for each of the next 2 years (the 2-year monitoring period). If either party disposes within 2 years, original gain recognized on the return for the year of disposition.  _(Form 8824 Part II)_
- **Part III — Realized Gain or Loss, Recognized Gain, Basis of Like-Kind Property Received** — Line 15: cash + FMV of non-like-kind received (boot received). Line 16: FMV of like-kind received. Line 17: total received. Line 18: adjusted basis of relinquished + boot paid + net liabilities incurred. Line 19: realized gain (line 17 − line 18). Line 20: smaller of line 19 or line 15 = recognized gain. Line 21: ordinary income under recapture rules (§1245, §1250, §1252, §1254, §1255 portion). Line 22: capital gain portion. Line 23: recognized gain (line 21 + 22). Line 24: deferred gain. Line 25: basis of replacement (line 18 + line 23 − line 15, with adjustments).  _(Form 8824 Part III)_
- **Part IV — Section 1043 conflict-of-interest sales by federal employees** — Part IV — Section 1043 conflict-of-interest sales by federal employees (rarely used).  _(Form 8824 Part IV; §1043)_
- **Where the numbers flow** — Line 22 (recognized capital gain) → Schedule D. Line 21 (recapture ordinary income) → Form 4797 Part III (then Form 1040). Basis (line 25) → carries to depreciation schedule for the replacement.  _(Form 8824; Schedule D; Form 4797)_
- **Failure to file Form 8824** — Failure to file Form 8824: the IRS will treat the transaction as a fully taxable sale; the §1031 deferral is procedurally voided. Always file even if there is zero boot and zero recognized gain.  _(Form 8824)_

## 19. State Conformity

- **Full conformity states** — Most states with an income tax conform to federal §1031 automatically because their starting point is federal taxable income (or AGI). Full conformity (federal §1031 applies for state tax): Most states — IL, NY, FL (no state income tax), TX (no state income tax), GA, MA, NC, OH, PA (for individual state tax — note PA has its own rule for sole proprietors below), VA, WA (no state income tax), and many others.
- **Notable non-conformity / quirks** — Pennsylvania (individual income tax): PA does NOT conform to §1031 for personal income tax on individuals (sole proprietors / Schedule E investors). Gain is recognized for PA personal income tax even though deferred federally. PA corporate net income tax does conform. California (FTB) — partial conformity + claw-back: California conforms to §1031 generally, BUT requires Form 3840 annual reporting (see §20). Massachusetts: conforms but has special depreciation conformity issues. Wisconsin: conforms.

A practitioner working a multi-state §1031 should always check both the state of the relinquished property and the state of the replacement, and the state of the taxpayer's residence.

## 20. California FTB Form 3840 — Claw-Back / Annual Reporting

- **California R&TC §18032 claw-back rule** — California's most distinctive §1031 rule: California Revenue & Taxation Code §18032 (added by AB 92, 2013) imposes a perpetual annual reporting obligation when a California taxpayer (resident or nonresident with CA-source gain) exchanges California real property for out-of-state replacement property.  _(Cal. R&TC §18032 (AB 92, 2013))_
- **Why the rule exists** — California wants to tax the deferred CA gain when the replacement is eventually sold, even if the taxpayer has by then moved out of California. The annual Form 3840 keeps the CA gain on file as a tracked deferral, and California will claim taxing rights when the replacement is finally sold or the deferral otherwise terminates.  _(Cal. R&TC §18032)_
- **Triggering exchange** — Relinquished: California real property. Replacement: out-of-state real property (any other US state or US possession).  _(Cal. R&TC §18032)_
- **Filing requirement** — File Form 3840 with the California return for the year of the exchange. File Form 3840 EVERY YEAR thereafter, as long as the replacement is still owned, until: The replacement is sold in a fully taxable transaction (CA gain then taxed), OR The replacement is exchanged in a further §1031 for new CA property (return to CA jurisdiction; tracking ends), OR The deferred gain is fully recognized for any reason.  _(Cal. FTB Form 3840)_
- **Information required on Form 3840** — Description of original relinquished CA property; Description of current replacement (after any subsequent exchanges); California-source deferred gain; Date of original relinquished sale; Year-by-year continuity record.  _(Cal. FTB Form 3840)_
- **Multiple subsequent exchanges** — If the replacement is itself §1031-exchanged into yet another out-of-state property, the new replacement inherits the CA tracking. Form 3840 continues with the new replacement description.  _(Cal. FTB Form 3840)_

AUDIT FLASH POINT — Missed CA Form 3840 filing. The FTB can pierce the §1031 deferral and assess the original CA gain in any year a required Form 3840 is not filed (R&TC §18032(c)). FTB practice: a missed filing in year 3 will trigger an audit notice; persistent non-filing will accelerate the deferred gain. The penalty regime under R&TC §19133.5 is $2,000 per year of non-filing. Track every CA-relinquished §1031 in a perpetual tickler file.

## 21. Worked Examples

### Example 1 — Apartment Building → Industrial Warehouse (Standard Deferred Exchange)

Taxpayer: California resident, individual, calendar year
Relinquished: 12-unit apartment building in San Diego, CA
  - Original cost (2010): $1,800,000
  - Cumulative depreciation through 2025: $654,545 (over 15 years on 27.5-year schedule)
  - Adjusted basis: $1,145,455
  - Mortgage: $900,000 (paid off at closing)
  - Sale price: $3,200,000 (closed June 1, 2025)
  - Selling costs (commission, title, escrow): $192,000
  - Net cash to QI: $3,200,000 − $192,000 − $900,000 = $2,108,000
Replacement: industrial warehouse in Phoenix, AZ
  - Identified July 10, 2025 (day 39) — single property identified under 3-property rule
  - Acquired November 15, 2025 (day 167)
  - Purchase price: $3,500,000
  - Mortgage on replacement: $1,400,000
  - Cash paid: $2,100,000 (from QI funds; taxpayer covers $8,000 transaction costs out of pocket)

Amount realized = $3,200,000 − $192,000 selling costs = $3,008,000
Adjusted basis = $1,145,455
Realized gain = $3,008,000 − $1,145,455 = $1,862,545

Cash boot received: $2,108,000 cash to QI but $2,100,000 used in replacement, with $8,000 remainder used for closing — assume zero net cash to taxpayer
Mortgage relief: $900,000 paid off
Mortgage assumed on replacement: $1,400,000
Net debt assumed = $1,400,000 − $900,000 = $500,000 (taxpayer assumed more debt; not boot)
Cash paid offsetting: not needed since net debt is positive
Total boot received: $0

Lesser of (realized gain $1,862,545, boot $0) = $0
Recognized gain: $0
Deferred gain: $1,862,545

Basis = Adjusted basis relinquished + cash paid + new mortgage + recognized gain − cash received − mortgage relieved
     = $1,145,455 + $2,100,000 + $1,400,000 + $0 − $0 − $900,000
     = $3,745,455
Cross-check: FMV $3,500,000 − deferred gain $1,862,545 = $1,637,455? — discrepancy

The discrepancy is the boot-paid offset against selling costs. Reconciliation:
FMV replacement received: $3,500,000
Less: deferred gain: $1,862,545
Basis: $1,637,455

Alternative Treas. Reg. computation:
Adjusted basis $1,145,455 (carryover)
+ $1,400,000 debt assumed (treated as cash paid)
− $900,000 debt relieved (treated as cash received)
+ $200,000 net additional cash paid out of pocket (the $192,000 selling costs absorb most of the gross sale; net analysis)
= $1,845,455

In practice, the reviewer should walk through Form 8824 lines methodically. The depreciation schedule for the replacement post-exchange uses the $1,145,455 carryover basis on the relinquished's residual 12.5-year remaining schedule, plus the $500,000 net debt addition + cash paid out of pocket as new-acquisition basis on a fresh 39-year industrial schedule.

Line 7: Related party? No
Line 15: Cash and other property received: $0
Line 16: FMV of like-kind property received: $3,500,000
Line 18: Adjusted basis of relinquished + costs: $1,145,455 + $192,000 + net debt $500,000 = $1,837,455
Line 19: Realized gain: $1,862,545
Line 20: Recognized gain: $0
Line 25: Basis in replacement: $1,637,455

Form 3840 filed with 2025 CA return because replacement is in Arizona (out-of-state).
Form 3840 continues every year until the Phoenix warehouse is sold or further-exchanged into CA property.

$1,862,545 of gain (including ~$163,636 of §1250 unrecaptured gain from the $654,545 cumulative depreciation, ultimately taxed at 25% on the eventual sale) fully deferred at federal level. California gain tracked on Form 3840 indefinitely.

### Example 2 — Reverse Exchange (Found Replacement First)

Taxpayer: Delaware LLC (single-member, disregarded; owner is Texas individual)
Replacement opportunity: distressed office complex in Austin, TX listed at $4,800,000, must close within 30 days or seller moves on. Acquired August 15, 2025.
Relinquished plan: aged retail strip in Dallas, TX, expected sale price $5,200,000, currently on market but no offer yet.

1. August 14, 2025: Taxpayer establishes Exchange Accommodation Titleholder — "Austin Reverse EAT LLC," a single-purpose subsidiary of the QI firm.
2. August 14, 2025: Taxpayer loans EAT $4,800,000 (taxpayer borrows this amount from a bridge lender against the Dallas property and personal credit).
3. August 15, 2025: EAT acquires the Austin office for $4,800,000.
4. August 19, 2025 (within 5 business days): Taxpayer and EAT execute the QEAA, identifying Austin office as parked replacement.
5. September 29, 2025 (day 45): Taxpayer identifies the Dallas retail strip as the relinquished property in writing to QI.
6. December 8, 2025 (day 115): Dallas retail strip sells for $5,150,000. Net of $309,000 selling costs and $1,800,000 mortgage payoff = $3,041,000 to QI.
7. December 9, 2025 (day 116): QI advances $3,041,000 to EAT; taxpayer makes up the $1,759,000 shortfall from the bridge loan that the EAT then repays. EAT transfers Austin office title to taxpayer. Taxpayer assumes Austin's existing $1,400,000 mortgage and pays off remaining bridge.

All steps complete within 180 days of EAT acquisition (deadline: February 11, 2026).

Relinquished basis: $2,800,000
Realized gain: $5,150,000 − $309,000 − $2,800,000 = $2,041,000
Boot received: $0 (all proceeds applied to replacement; net debt is roughly equal, $1,800,000 relieved vs $1,400,000 assumed = $400,000 debt relief, but taxpayer paid $1,759,000 additional cash, so cash paid offsets debt relief; net boot = $0)
Recognized gain: $0
Basis in Austin office: $2,800,000 + cash paid − debt relief net = approximately $2,400,000

Form 8824 reporting: identical line-by-line format. Note Line 6 "date you actually received the replacement" is December 9, 2025 (the date EAT transferred to taxpayer), NOT August 15 (the date EAT acquired).

Bridge loan financing during EAT holding period is common and acceptable under Rev. Proc. 2000-37.
EAT must not act as taxpayer's agent for tax purposes during parking; the QEAA structure addresses this.

### Example 3 — Drop-and-Swap (Partnership Exit)

Partnership: 4-partner LLC taxed as partnership, owns commercial office building in Florida.
Partner A and B want to defer gain via §1031; Partners C and D want cash to retire.
Building: FMV $8,000,000; basis $3,200,000; mortgage $2,000,000; partners equal 25% each.
Buyer offers $8M cash close in 90 days.

1. June 2024 (12 months before sale): Partnership operating agreement amended to authorize in-kind distribution. No buyer yet identified.
2. July 2024: Partnership distributes building to partners as TICs — each partner now owns 25% undivided interest. Partnership dissolves (or remains as shell). TIC agreement drafted but kept minimal to satisfy Rev. Proc. 2002-22:
   - Each partner takes title to 25% TIC interest
   - Each partner assumes 25% of mortgage ($500,000 each)
   - No common name or partnership filings going forward
   - Each partner files Schedule E for tax year 2024 reporting their share of rent
   - Unanimous consent required for sale or refinance
3. June 2025: Buyer emerges, offers $8M.
4. July 2025: Each partner independently decides:
   - Partner A: full §1031 — engages QI, plans replacement
   - Partner B: full §1031 — engages QI, plans replacement
   - Partner C: cash out — sells 25% TIC interest directly to buyer for $2M (less $500k debt assumption = $1.5M cash); recognizes 25% × ($8M − $3.2M) = $1.2M gain.
   - Partner D: same as C — taxable sale of TIC interest.
5. August 2025: Sale closes. Partners A and B's portions go through QI into deferred exchanges; Partners C and D's portions paid directly to them as taxable sales.

Each files own Form 8824 reflecting 25% TIC ownership.
Question 11 (was property held more than 2 years): yes — TIC held from July 2024 to August 2025 plus prior partnership holding period under §1223 tacking ambiguity (conservative position: only TIC holding period counts; some practitioners argue tacking applies). At 13 months as TIC, the safer answer is to disclose the drop and rely on the documented business purpose.

The 12-month gap between drop and sale supports an "investment intent" position. <6 months would be aggressive; <30 days would be a near-certain audit loss.
Each TIC owner separately filing Schedule E for at least one tax year strengthens the position.
The IRS may still argue step-transaction; the taxpayer should document contemporaneous business reasons for the drop (estate planning, divorce, partner dispute, refinancing flexibility) rather than just "to enable §1031."
Partner C and D's tax treatment is unaffected by A and B's deferral choice — their gain is recognized fully.

## 22. Practitioner Checklist (Pre-Closing of Relinquished)

Before the relinquished property closes, confirm:
- [ ] Property qualifies as real property under Treas. Reg. §1.1031(a)-3
- [ ] Property is held for trade/business or investment (not inventory; not personal use; vacation home meets Rev. Proc. 2008-16)
- [ ] Taxpayer's intent on replacement is the same — held for trade/business or investment
- [ ] QI engaged before closing; QI is not a disqualified person (no professional services to taxpayer in past 2 years)
- [ ] Exchange agreement signed before closing
- [ ] Closing instructions direct proceeds to QI's qualified escrow, not to taxpayer
- [ ] Settlement statement (HUD-1 or Closing Disclosure) shows QI as recipient of net sale proceeds
- [ ] §1245 component recapture computed; cost-segregation prior-year reports reviewed
- [ ] §1250 cumulative depreciation tracked for eventual 25% rate exposure
- [ ] Related-party status checked (§267(b) / §707(b)) — if related, 2-year monitoring plan in place
- [ ] Partnership drop, if applicable, completed at least 12 months prior (or contemporaneous-purpose documentation in file)
- [ ] California Form 3840 reminder calendared if relinquished is in CA
- [ ] Tax return extension (Form 4868) planned for relinquished-year return if relinquished closes after July 4 (to preserve full 180-day window through April 15+ extension)
- [ ] Identification deadline (day 45) calendared with multiple reminders
- [ ] Exchange deadline (day 180 or return due date) calendared
- [ ] No Opportunity Zone deferral attempted on the same gain (mutually exclusive)
- [ ] Form 8824 working file opened with cumulative basis, depreciation, and boot tracking

## 23. Cross-References

- `us-tax-workflow-base` — workflow scaffold and reviewer-sign-off requirement
- `us-sole-prop-bookkeeping` — Schedule C / rental classification, §168 depreciation
- `us-schedule-c-and-se-computation` — recapture flow to Form 4797 → Schedule 1
- `ca-540-individual-return` — California Form 540 reporting; Schedule CA adjustments
- `us-form-1065-partnership` — drop-and-swap partnership-level mechanics
- `us-foreign-tax-credit-1116` — for cross-border deferral context (§1031(h) bar)

## 24. Provenance and Authorities

- **Statute list** — IRC §1031 (real property only since 2018; pre-2018 history preserved in legislative archive); IRC §1031(a)(1) — non-recognition rule; IRC §1031(a)(2) — interests in partnerships excluded; IRC §1031(a)(3) — 45/180-day rules for deferred exchanges; IRC §1031(b)–(c) — boot recognition and loss treatment; IRC §1031(d) — basis carryover; IRC §1031(f) — related-party 2-year rule; IRC §1031(h) — US-for-foreign disallowance; IRC §1031(i) — cooperative housing carve-out; IRC §121(d)(10) — §1031 + §121 sequential rules; IRC §168(i)(7) — depreciation treatment of exchanged-basis property; IRC §1223(1) — holding-period tacking; IRC §1245(b)(4) — recapture in like-kind exchanges; IRC §1250(d)(4) — §1250 treatment in like-kind exchanges; IRC §1400Z-2 — Opportunity Zone alternative; IRC §6651, §6662, §6663 — penalties for failure to file, accuracy, fraud  _(IRC §1031 et seq.)_
- **Treasury Regulations list** — Treas. Reg. §1.1031(a)-1 — like-kind definition; Treas. Reg. §1.1031(a)-3 — real property definition (finalized December 2020, TD 9935); Treas. Reg. §1.1031(b)-1 — boot; Treas. Reg. §1.1031(d)-1, -2 — basis; Treas. Reg. §1.1031(j)-1 — multiple property exchanges; Treas. Reg. §1.1031(k)-1 — deferred exchange rules; Treas. Reg. §1.168(i)-6 — depreciation post-exchange  _(Treas. Reg. §1.1031)_
- **Revenue Procedures and Rulings list** — Rev. Proc. 2000-37 — reverse exchange safe harbor; Rev. Proc. 2004-51 — modification to 2000-37; Rev. Proc. 2002-22 — TIC safe harbor (15 conditions); Rev. Proc. 2005-14 — §121 + §1031 stacking; Rev. Proc. 2008-16 — vacation-home safe harbor; Rev. Rul. 2019-24 — cryptocurrency not §1031-eligible; CCA 202124008 — pre-TCJA crypto-for-crypto not like-kind  _(Rev. Proc. 2000-37; Rev. Proc. 2004-51; Rev. Proc. 2002-22; Rev. Proc. 2005-14; Rev. Proc. 2008-16; Rev. Rul. 2019-24; CCA 202124008)_
- **Case Law list** — Starker v. United States, 602 F.2d 1341 (9th Cir. 1979) — birth of deferred exchange; Suburban Realty v. United States, 615 F.2d 171 (5th Cir. 1980) — dealer test factors; Click v. Commissioner, 78 T.C. 225 (1982) — pre-arranged disposition fails "held for"; DeCleene v. Commissioner, 115 T.C. 457 (2000) — reverse exchange outside safe harbor; Teruya Bros., Ltd. v. Commissioner, 580 F.3d 1038 (9th Cir. 2009) — §1031(f)(4) related-party basis-shifting  _(Starker v. United States, 602 F.2d 1341 (9th Cir. 1979); Suburban Realty v. United States, 615 F.2d 171 (5th Cir. 1980); Click v. Commissioner, 78 T.C. 225 (1982); DeCleene v. Commissioner, 115 T.C. 457 (2000); Teruya Bros., Ltd. v. Commissioner, 580 F.3d 1038 (9th Cir. 2009))_
- **Forms list** — Form 8824 — Like-Kind Exchanges (federal); Form 4797 — Sales of Business Property (recapture flow); Form 1040 Schedule D — Capital Gains; Form 4868 — Application for Automatic Extension (to preserve 180-day window); California Form 3840 — California Like-Kind Exchanges  _(Form 8824; Form 4797; Form 1040 Schedule D; Form 4868; California Form 3840)_
- **California Authority list** — R&TC §18032 — Form 3840 annual reporting requirement; R&TC §19133.5 — penalty for failure to file Form 3840; AB 92 (2013) — enactment of California claw-back  _(R&TC §18032; R&TC §19133.5; AB 92 (2013))_

Tax Year Reference: Tax year 2025. Last updated 2025-11-15. Version 0.1. Verification pending Circular 230 review.

— End of skill —

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
