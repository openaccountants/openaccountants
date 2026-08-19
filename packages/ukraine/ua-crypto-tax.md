---
name: ua-crypto-tax
description: "Taxation of cryptocurrency / virtual assets for individuals in Ukraine under the framework legislated to take effect from 1 January 2026: 18% PIT + 5% military levy on annual gains, the one-off 5% PIT transition for pre-law assets sold in 2026, taxable events, cost basis, and record-keeping."
version: 1.0
jurisdiction: UA
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UA Crypto Tax

## Ukraine — Taxation of Virtual Assets / Cryptocurrency for Individuals (2026) v1.0

CRITICAL — READ FIRST — LEGISLATIVE STATUS (as of May 2026). The rules in this skill describe Draft Law No. 10225-d ("On Amendments to the Tax Code of Ukraine and Certain Other Legislative Acts of Ukraine Regarding the Regulation of the Virtual Asset Market"), introduced 24 April 2025. As of the last verification it had passed only the FIRST reading in the Verkhovna Rada (246 of 450 votes). It had NOT been adopted in the second/final reading, NOT signed by the President, and was therefore NOT in force, even though the bill itself sets a target effective date of 1 January 2026. Substantial amendments were expected before the second reading. Until the final text is enacted and published, every figure and rule below is a PROPOSAL and may change. You MUST re-verify the current in-force status on tax.gov.ua / zakon.rada.gov.ua / the Verkhovna Rada bill card before relying on any number. Treat all outputs as draft pending confirmation of enactment.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Ukraine (UA) |
| Asset class | Virtual assets / cryptocurrency held by an **individual** (non-business holder) |
| Tax (standard) | **PIT 18% + military levy 5% = 23%** on the net annual investment gain (proceeds from disposals − documented acquisition cost) |
| Preferential (2026 only) | **PIT 5% (+ 5% military levy)** for assets **acquired before the law takes effect** and sold during 2026 — see §4. (Military-levy applicability under the preferential rate is one of the points to re-verify in the final text.) |
| Currency | Ukrainian hryvnia (UAH / ₴) — all figures converted to UAH |
| Legislation | Draft Law No. 10225-d (2026 Virtual Assets Market Law) amending the **Tax Code of Ukraine (Податковий кодекс)**; builds on the 2022 Law "On Virtual Assets" |
| Tax authority | Державна податкова служба України (ДПС / State Tax Service, tax.gov.ua / dps.gov.ua) |
| Market regulator(s) | National Securities & Stock Market Commission (НКЦПФР / NSSMC) and the National Bank of Ukraine (NBU), per the framework |
| Portal | **Електронний кабінет платника** (cabinet.tax.gov.ua) |
| Filing | **Annual** personal income tax declaration (Декларація про майновий стан і доходи), due by **30 April** of the year following the tax year; tax payable by **31 July** |
| Tax year | Calendar year |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Ukrainian accountant/auditor** |
| Skill version | 1.0 |

### Conservative defaults (apply when facts or the final law are uncertain)

Assume the law is NOT yet in force unless you have positively verified enactment. Tell the user when the rules become effective and what is still pending.
If unsure whether a receipt is taxable now or only on disposal, default to the disposal-only model that the draft adopts, but flag the uncertainty.
If acquisition cost is undocumented, default to proceeds = full taxable base (no cost deduction). Documented cost is required to reduce the gain.
Use the NBU official exchange rate on the relevant transaction date for UAH conversion unless a more specific rule applies.
Treat frequent, organised, profit-seeking mining/trading as potential business activity (FOP / legal entity), which falls outside this individual-investor skill — route to ua-single-tax or a corporate skill.
Where the draft offers options (e.g. taxing staking at receipt vs at sale), present the conservative reading and mark "verify current in-force status".

## 2. Taxable events & what is NOT taxed

The draft taxes the investment-style gain realised on disposal of a virtual asset, mirroring the existing Tax Code mechanism for income from the sale of investment assets.

### Taxable events

- **Disposal of a virtual asset for fiat money** — e.g. selling BTC for UAH, USD or EUR — cashing out. This is the core taxable event.  _(Draft Law No. 10225-d)_
- **Disposal of a virtual asset in exchange for goods, services or other property** — i.e. spending crypto / barter where ownership passes for non-crypto value. Treat as a disposal at market value.  _(Draft Law No. 10225-d)_

### NOT taxed (per the draft)

- **Crypto-to-crypto exchanges** — Exchanging one virtual asset for another (e.g. BTC → USDT, ETH → USDC) is exempt — no taxable income arises at the swap. Income is recognised only when the position is later converted to fiat/goods/services. (This is a deliberate design choice in 10225-d / the NSSMC matrix; re-verify it survived the second reading, as crypto-to-crypto neutrality is the single most likely provision to be narrowed.)  _(Draft Law No. 10225-d / NSSMC matrix)_
- **Transfers between the holder's own wallets / accounts** — Moving the same asset between wallets you control is not a disposal — no change of ownership, no tax.  _(Draft Law No. 10225-d)_
- **Receipt at issuance, creation, or free of charge** — incl. tokens received in exchange for personal data — generally not income at receipt; tax is deferred to eventual disposal (see §5).  _(Draft Law No. 10225-d)_
- **Small annual proceeds de-minimis** — one minimum monthly wage UAH minimum monthly wage (Exact threshold/wording must be confirmed in the final text — verify current in-force status.)  _(Draft Law No. 10225-d)_

## 2. Taxable events & what is NOT taxed

Because crypto-to-crypto is not taxed, the practical taxable universe is off-ramps: the moment value leaves the crypto domain into fiat, goods or services.

## 3. Computing the gain — proceeds, acquisition cost, FX conversion, losses

The taxable base for the year is the net positive investment result:

- **Annual taxable gain / Tax due formula** — Annual taxable gain = Σ (proceeds on each disposal in UAH) − Σ (documented acquisition cost of the assets disposed of, in UAH) − allowable transaction costs (where documented/permitted) Tax due = Annual taxable gain × (PIT rate + 5% military levy) where PIT rate = 18% standard, or 5% under the 2026 transition (§4)  _(Draft Law No. 10225-d)_

### Proceeds

- **Proceeds conversion** — The fiat amount (or fair market value of goods/services) received on disposal, converted to UAH at the NBU rate on the transaction date.  _(Draft Law No. 10225-d)_

### Acquisition cost (cost basis)

- **Documented cost** — Documented cost of acquiring the disposed asset (purchase price + directly attributable, documented costs), in UAH.  _(Draft Law No. 10225-d)_
- **No documentation → no deduction** — If the holder cannot evidence acquisition cost, the entire disposal proceeds become the taxable base. This makes record-keeping decisive (see §7).  _(Draft Law No. 10225-d)_
- **Cost-basis ordering method** — Cost-basis ordering method (FIFO / specific identification / weighted average) is not unambiguously fixed in the public draft summaries. Default to a consistent, defensible method (FIFO is the conservative, common choice) and document the method used; verify what the enacted regulations require.  _(Draft Law No. 10225-d)_

### Foreign-exchange / NBU conversion

- **NBU conversion rule** — All amounts in foreign fiat or foreign-currency-denominated values are converted to UAH using the NBU official rate on the relevant date. Exchange-rate differences feed into the financial-result calculation.  _(NBU official rate)_

### Losses

- **Loss carry-forward** — The draft allows a net loss to be carried FORWARD to offset gains from virtual-asset transactions in subsequent years. Losses are ring-fenced to the virtual-asset category (they do not offset salary or other income). (Carry-back is not provided; carry-forward duration/limits to be confirmed — verify current in-force status.)  _(Draft Law No. 10225-d)_

## 4. The 2026 preferential 5% transition rule

To encourage voluntary disclosure and a smooth start, the draft provides a one-off transitional regime in the first year:

- **Eligibility** — the virtual asset must have been acquired BEFORE the law's effective date (i.e. legacy holdings), and disposed of during 2026 (the first year the regime is in force).  _(Draft Law No. 10225-d)_
- **Preferential rate** — 5% PIT instead of 18%. The 5% military levy continues to apply in the published descriptions, so the practical preferential combined rate is commonly described as 5% + 5% = 10% for 2026. (Whether the military levy is reduced/waived under the preferential PIT is NOT fully settled across sources — flag and verify in the final text.)  _(Draft Law No. 10225-d)_
- **After the window** — from 2027 onward (and for assets acquired after the effective date), the standard 18% + 5% = 23% applies.  _(Draft Law No. 10225-d)_

a fixed, low entry rate to bring pre-existing, often poorly documented, holdings into the system.

Practical guidance: a holder sitting on large pre-law gains has a strong incentive to realise (cash out) eligible legacy positions within 2026 to lock in the 5% PIT, provided the law is actually in force and the asset qualifies. Do NOT advise acting on this until enactment is confirmed.

## 5. Mining, staking, airdrops, hard forks

The published draft / NSSMC "tax matrix" leans toward a disposal-only model for individuals — i.e. tokens received from these activities are generally not income at the moment of receipt, and tax arises when the tokens are later sold/converted (with acquisition cost frequently treated as low or zero, so most of the proceeds become gain). However, several of these treatments are conceptual options, not finalised law, and must be flagged.

**Activity treatment table**  _(NSSMC tax matrix / Draft Law No. 10225-d)_

| Activity | Likely individual treatment (draft) | Confidence / flag |
| --- | --- | --- |
| **Mining** | Tokens created by mining are **not taxed at creation**; taxed on disposal. BUT **regular, profit-seeking, infrastructure-dependent mining is likely BUSINESS activity** (FOP / company), outside this individual skill. Small-scale personal mining may use de-minimis. | Medium — business-vs-personal line is a key judgement; verify |
| **Staking** | **Two options debated:** (a) tax staking rewards as income **at receipt** (like deposit interest), or (b) tax **only at sale**. The draft/matrix tilts toward recognising income **on conversion to fiat**. | **Low — unsettled.** Default conservative: be ready for receipt-level taxation; verify in-force text |
| **Airdrops** | Generally **not taxed at receipt**; taxed on later disposal. Cost basis often **zero**. DAO/participation rewards may be ordinary income. | Medium — verify |
| **Hard forks** | New tokens from a fork: **not taxed at receipt**, taxed on disposal. | Low/Medium — verify |
| **Free issuance / tokens for personal data** | Explicitly contemplated as **non-taxable at receipt**. | Medium — verify |

If the user's activity is systematic and commercial (mining farm, professional trading desk, validator-as-a-business), this individual investor skill does not apply — route to the Ukrainian business regimes (FOP single tax via ua-single-tax, or corporate income tax). Flag clearly.

## 6. Worked examples

All examples assume the law is in force as drafted; re-verify before relying. Rates: standard 18% PIT + 5% levy; 2026 preferential 5% PIT (+5% levy on the descriptions used here).

### Example A — Simple cash-out, standard rate

Bought 1 BTC for ₴1,000,000 (documented), acquired after the effective date.
Sold 1 BTC for ₴1,600,000 in 2027.
Gain = 1,600,000 − 1,000,000 = ₴600,000.
Tax = 600,000 × 23% = ₴138,000 (PIT 18% = 108,000 + levy 5% = 30,000).
Net after tax = ₴462,000.

### Example B — Pre-law asset sold in 2026 (preferential 5%)

Bought 2 ETH for ₴100,000 in 2023 (documented), i.e. before the effective date.
Sold 2 ETH for ₴300,000 in 2026.
Gain = 300,000 − 100,000 = ₴200,000, qualifies for the transition.
Tax = 200,000 × (5% PIT + 5% levy) = 200,000 × 10% = ₴20,000.
Compare standard 23% = ₴46,000 → the transition saves ₴26,000. (If the final law also waives the levy under the preferential rate, tax would be ₴10,000 — confirm.)

### Example C — Crypto-to-crypto then cash-out

Buy BTC for ₴500,000. Later swap BTC → ETH when BTC is worth ₴700,000.
The swap is NOT taxed (crypto-to-crypto exempt). No tax event yet; carry the ₴500,000 cost into the ETH position.
Later sell ETH for ₴900,000 fiat.
Gain on the off-ramp = 900,000 − 500,000 = ₴400,000.
Tax (standard) = 400,000 × 23% = ₴92,000. The intermediate swap is irrelevant to tax.

### Example D — Loss carry-forward

Year 1: net virtual-asset result = −₴150,000 (loss). Tax = 0; carry forward ₴150,000.
Year 2: gross gain = ₴400,000; apply carried loss → taxable = 400,000 − 150,000 = ₴250,000.
Tax = 250,000 × 23% = ₴57,500.

### Example E — Undocumented cost basis

Sold crypto for ₴300,000 but no acquisition records.
Deductible cost = ₴0 → taxable base = ₴300,000.
Tax (standard) = 300,000 × 23% = ₴69,000. (Records would have cut this sharply — see §7.)

## 7. Tier 2 catalogue — reviewer judgement, record-keeping, foreign holdings

These items require human reviewer judgement and/or are not fully settled in the draft. Escalate to a qualified Ukrainian accountant.

- **1. In-force status (top priority)** — Confirm the bill has passed the second reading, been signed and published, and verify the actual effective date and final rates before any computation.  _(Verkhovna Rada bill card)_
- **2. Cost-basis method** — FIFO vs weighted-average vs specific-ID is not unambiguous in public summaries — confirm the enacted method; apply consistently and document it.  _(Draft Law No. 10225-d)_
- **3. Staking timing** — Receipt vs disposal taxation is unsettled — get the final rule before advising stakers/validators.  _(NSSMC tax matrix)_
- **4. Business vs investor line** — Frequency, scale, organisation and intent determine whether mining/trading is FOP/corporate (out of scope here). Document the analysis.  _(Draft Law No. 10225-d)_
- **5. De-minimis threshold** — Confirm the minimum-monthly-wage exemption figure and whether it is per-transaction or per-year.  _(Draft Law No. 10225-d)_
- **6. Military levy under the 5% preferential rate** — Confirm whether the 5% levy applies, is reduced, or is waived in 2026.  _(Draft Law No. 10225-d)_
- **7. Record-keeping (decisive)** — Keep, per asset and per transaction: date, type (buy/sell/swap/transfer/reward), counterparty/exchange; quantity, fiat value and the UAH amount at the NBU rate on that date; acquisition documents (invoices, exchange statements, on-chain references); running cost basis and method used. Without records, undocumented cost defaults to ₴0 (Example E).  _(Draft Law No. 10225-d)_
- **8. Foreign-exchange / foreign-held assets** — Crypto held on foreign exchanges or in self-custody abroad is still taxable in Ukraine for Ukrainian tax residents on worldwide income; consider currency-control, foreign-account reporting, and double-tax-treaty interaction. Confirm residency first.  _(Draft Law No. 10225-d)_
- **9. Interaction with the FOP simplified system** — Whether a FOP can run virtual-asset activity inside the єдиний податок regime is a separate question — route to ua-single-tax and confirm permitted activities.  _(ua-single-tax)_
- **10. Anti-avoidance / wash sales** — Confirm whether the final law restricts loss harvesting via near-simultaneous repurchase.  _(Draft Law No. 10225-d)_

## 8. Reference material + test suite

### Sources consulted (re-verify currency before use)

State Tax Service of Ukraine — tax.gov.ua / dps.gov.ua (authority, declaration, Електронний кабінет).
Verkhovna Rada — Draft Law No. 10225-d, "On Amendments to the Tax Code of Ukraine … Regulation of the Virtual Asset Market" (introduced 24 Apr 2025; first reading passed). Check the bill card on zakon.rada.gov.ua / w1.c1.rada.gov.ua for current status.
NSSMC (НКЦПФР) — the "tax matrix" concept paper on virtual-asset taxation (token classes; mining/staking/airdrop options).
EY Ukraine — IT/Tax/Law digest on the draft law (rates, taxable events, transition, declaration).
Global Legal Insights — Blockchain & Cryptocurrency Laws & Regulations 2026 (Ukraine).
PwC / CMS / Lexology crypto-tax commentary on the 2026 framework.
Underlying 2022 Law of Ukraine "On Virtual Assets" (foundational definitions).

### Quick test suite (expected answers under the draft)

1. Is selling BTC for UAH taxable? → Yes (off-ramp; 18% PIT + 5% levy on the gain).
2. Is swapping BTC for ETH taxable? → No (crypto-to-crypto exempt); tax deferred to fiat conversion. (Verify provision survived.)
3. Moving ETH between my own two wallets? → No (no change of ownership).
4. I bought BTC in 2021 and sell it in 2026 — what rate? → Preferential 5% PIT (pre-law asset sold in the transition window) + 5% levy as described. Confirm levy treatment.
5. I have no purchase records — what's my taxable base? → Full proceeds (cost = ₴0).
6. Net loss this year — is it wasted? → No — carry forward to offset future crypto gains.
7. Standard combined rate from 2027? → 23% (18% PIT + 5% military levy).
8. Is the law definitely in force in 2026? → Not confirmed — as of May 2026 only the first reading had passed; verify enactment before relying on anything.

## PROHIBITIONS

Do NOT state the law is in force or that 2026 figures are final unless you have positively verified enactment (second reading + signature + publication). Default to "draft / pending".
Do NOT fabricate rates, thresholds, the de-minimis figure, carry-forward limits, the cost-basis method, or the levy treatment under the preferential rate. If the final text is unverified, say so and mark "verify current in-force status".
Do NOT advise a client to cash out legacy holdings in 2026 to capture the 5% rate until enactment and eligibility are confirmed — premature action could be wrong if the law shifts.
Do NOT handle business-scale mining/trading or legal entities here — that is FOP/corporate scope; route accordingly.
Do NOT give VAT, customs, social-contribution (ЄСВ), residency, or AML/currency-control conclusions from this skill — those are out of scope; route to the relevant skill or a professional.
Do NOT skip the human reviewer. This is YMYL content on a fast-moving, not-yet-final law.

## Disclaimer

This skill is research-verified against Ukrainian State Tax Service material, the Verkhovna Rada bill record for Draft Law No. 10225-d, NSSMC commentary, and Big-4/legal analysis — but it describes a new and fast-moving law that, as of May 2026, had passed only the first reading and was not confirmed in force. Every rate, threshold and rule is therefore provisional and may change before (or after) enactment. Nothing here is legal or tax advice. It must be reviewed and signed off by a qualified Ukrainian accountant, auditor or tax adviser, and the current in-force status must be re-checked on tax.gov.ua and the Verkhovna Rada bill card before use. Part of the open-source tax-skill library at openaccountants.com.

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
