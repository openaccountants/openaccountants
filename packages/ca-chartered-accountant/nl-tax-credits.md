---
name: nl-tax-credits
description: Use this skill for Newfoundland and Labrador provincial tax credits + NL Insurance Premium Tax. Includes NL Low-Income Tax Reduction, NL Income Supplement, NL Seniors' Benefit, Volunteer Firefighters Tax Credit, NL Direct Equity Tax Credit (35%), NL Film & Video Industry Tax Credit, plus the NL Insurance Premium Tax (15% on commercial insurance — unique to NL). Triggers "Newfoundland tax credits", "NL Income Supplement", "NL Direct Equity Tax Credit", "Newfoundland Insurance Premium Tax", "NL IPT 15%", "Form NL428".
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NL Tax Credits

## Newfoundland and Labrador — Provincial Tax Credits + Insurance Premium Tax — Skill v1.0

This skill covers the personal and corporate tax credit toolkit specific to Newfoundland and Labrador (NL), plus the NL Insurance Premium Tax (IPT) — a province-specific indirect tax that is unusually high (15% on commercial insurance) and frequently overlooked by accountants from other provinces.

Load alongside `ca-tax-workflow-base` and (where relevant) `nl-individual-return`. Federal credits stay with the federal skills; this skill is purely the NL-specific layer.

## 1. Quick reference

### Personal credits (claimed on Form NL428 unless noted)

**Personal credits (claimed on Form NL428 unless noted)**

| Credit | Type | 2025 maximum | Notes |
| --- | --- | --- | --- |
| NL Low-Income Tax Reduction | Non-refundable | Reduces NL tax to $0 | Income-tested; phased out |
| NL Income Supplement | Refundable | ~$520 / adult + ~$200 / child | Quarterly payment, joint w/ federal GST/HST credit |
| NL Seniors' Benefit | Refundable | ~$1,516 | Age 65+, income-tested |
| Volunteer Firefighters / Search & Rescue | Non-refundable | $500 (≈ $44 actual saving at 8.7% bottom rate) | Per individual, 200+ hours |
| Political Contribution Credit | Non-refundable | Up to $500 | Same structure as federal |
| Adoption Expenses | Non-refundable | Mirrors federal |  |

### Corporate / investor credits

**Corporate / investor credits**

| Credit | Type | Rate | Cap |
| --- | --- | --- | --- |
| NL Direct Equity Tax Credit (DETC) | Non-refundable for investor | **35%** (priority sectors) / 20% / 10% | Annual investor cap $50k → max $17,500 credit |
| NL Film & Video Industry Tax Credit | Refundable (corporate) | 40% of eligible NL labour | Capped at 25% of total production cost; $4M / project / yr |
| NL Interactive Digital Media Tax Credit | Refundable | 40% of eligible labour | $40k / employee / yr; $2M / corp / yr |
| Manufacturing & Processing Investment Tax Credit | Refundable / Non-refundable | 10% (refundable for CCPCs) | On qualifying M&P assets |
| Green Technology Tax Credit | Refundable / Non-refundable | 20% | $1M annual limit |

### NL Insurance Premium Tax (IPT)

**NL Insurance Premium Tax (IPT)**

| Premium type | Rate |
| --- | --- |
| **Commercial / property / liability / life / accident & sickness** | **15%** |
| **Automobile insurance** | 5% |

### NL Insurance Premium Tax (IPT)

NL's commercial IPT is the highest in Canada (most provinces 2–4%). It is a real cash cost for NL-based businesses and must be modelled into pricing and budget reviews.

## 2. Required inputs + refusal catalogue

### Required inputs (personal credits)

- Net income, family net income, marital status, dependants
- Residency on Dec 31, 2025 = NL (otherwise refuse — see R-NL-1)
- Age (for Seniors' Benefit)
- Volunteer hours certification letter from Fire Chief / SAR coordinator
- T5/T3 slips for investment income (DETC interaction)

### Required inputs (corporate / investor credits)

- For DETC: Certificate of Registration (CoR) of the Eligible Business Corporation (EBC) issued by NL Department of Industry, Energy and Technology (IET); investor's subscription agreement; share certificate; sector classification (priority vs general)
- For Film TC: Eligibility certificate from NL Film Development Corporation; NL labour breakdown; total production budget
- For IPT: Type of insurance, taxable premium amount, policy effective date

### Refusal catalogue (NL-specific)

- **R-NL-1** — Non-resident of NL on Dec 31. NL428 cannot be filed. Provincial credits go to province of residence.  _(R-NL-1)_
- **R-NL-2** — DETC requested without a valid IET Certificate of Registration for the issuer. Refuse; the credit is statutory, not discretionary.  _(R-NL-2)_
- **R-NL-3** — DETC investor cap exceeded. Investor cannot claim more than $17,500 (35% × $50k) in DETC in a single year; carryforward to 7 years allowed but flag.  _(R-NL-3)_
- **R-NL-4** — Film TC for production where principal photography started before the eligibility certificate date. Not eligible.  _(R-NL-4)_
- **R-NL-5** — IPT on reinsurance ceded to a licensed NL insurer (already taxed once). Do not double-tax.  _(R-NL-5)_
- **R-NL-6** — IPT on marine cargo for international shipping outside NL waters — out of scope of NL IPT.  _(R-NL-6)_
- **R-NL-7** — Seniors' Benefit for a deceased taxpayer who died before July 1 of the benefit year — pro-ration rules apply; do not pay full benefit.  _(R-NL-7)_
- **R-NL-8** — Volunteer Firefighter credit + federal VFA on the same 200 hours — only one of the two; choose the federal $3,000 amount if it produces higher savings (it almost always does at higher incomes).  _(R-NL-8)_

## 3. NL Low-Income Tax Reduction

- **NL Low-Income Tax Reduction** — Reduces NL income tax payable to zero for low-income individuals and families. Calculated on Form NL428, Part C.  _(Form NL428, Part C)_
- **Threshold 2025** — roughly $20,400 single / $34,400 family (indexed)  _(Form NL428, Part C)_
- **Phase-out** — 16% of net income above threshold  _(Form NL428, Part C)_
- **Claim behaviour** — Always claim — fully formulaic. Does not affect federal tax or other provincial refundable credits.  _(Form NL428, Part C)_

Reviewer note: clients who pay no NL tax still get the Income Supplement and Seniors' Benefit because those are refundable; do not skip the rest of NL428.

## 4. NL Income Supplement (refundable)

Paid quarterly with the federal GST/HST credit cycle (Jan, Apr, Jul, Oct).

- **Adult amount** — ~$520 / yr
- **Adult amount** — ~$520 / yr
- **Each child under 19** — ~$200 / yr
- **Persons with disabilities supplement** — ~$240 / yr (if DTC-eligible)
- **Phase-out** — 8% of family net income over ~$40,000 (single) / ~$43,000 (family)

Automatically computed from the T1; no separate application — but must file the T1 to get it. Encourage low-income clients to file even when they owe nothing.

## 5. NL Seniors' Benefit (refundable)

Paid in October each year with the federal GIS top-up cycle in NL.

- **Eligibility age** — Age 65+ on or before Dec 31, 2025
- **Maximum** — ~$1,516 / yr (single senior or senior couple — single benefit per household, not per spouse)
- **Phase-out** — 11.66% of family net income over ~$29,402
- **Fully phased out** — ~$42,404 family net income
- **Computation** — Automatically computed from T1, line 14600 area  _(T1 line 14600)_

Pitfall: the benefit is per household, not per spouse. Common preparer error is double-claiming.

## 6. NL Volunteer Firefighters / Search & Rescue Tax Credit

- **Credit type** — Non-refundable provincial credit on Form NL428  _(Form NL428)_
- **Amount** — $500 (claimed at the 8.7% bottom NL rate → ~$43.50 actual tax saving)  _(Form NL428)_
- **Hours requirement** — Requires 200+ hours of volunteer service in the year
- **Combination restriction** — Cannot combine NL credit with federal $3,000 VFA / SRVA on the same hours

Decision rule for reviewer:
- If marginal NL rate ≤ 8.7% AND federal marginal rate ≥ 15% → claim federal $3,000 (saves $450) and skip NL $500. Almost always the right answer.
- If client has zero federal tax payable → NL credit is still wasted because it's non-refundable. Document the choice in the brief.

## 7. NL Direct Equity Tax Credit (DETC)

One of Canada's most generous direct angel-investor credits. Statutory under the *Direct Equity Tax Credit Act* (NL).

### Mechanics

- **Subscription requirement** — Investor (individual or corporation) subscribes for newly-issued common shares in a registered Eligible Business Corporation (EBC) located in NL.  _(Direct Equity Tax Credit Act (NL), SNL2000 c D-18.1)_
- **CoR requirement** — EBC must hold a current Certificate of Registration from IET issued before the share subscription.  _(Direct Equity Tax Credit Act (NL), SNL2000 c D-18.1)_
- **Priority sectors rate** — 35% (tech, aquaculture, forestry, manufacturing, export, cultural industries, tourism outside NE Avalon)  _(Direct Equity Tax Credit Act (NL), SNL2000 c D-18.1)_
- **Other eligible sectors rate** — 20%  _(Direct Equity Tax Credit Act (NL), SNL2000 c D-18.1)_
- **Registered venture capital corporation rate** — 10%  _(Direct Equity Tax Credit Act (NL), SNL2000 c D-18.1)_
- **Minimum / maximum investment** — Minimum investment $1,000; maximum eligible $50,000 / investor / year → max credit $17,500  _(Direct Equity Tax Credit Act (NL), SNL2000 c D-18.1)_
- **Non-refundable / carryover** — Non-refundable but carries back 3 years / forward 7 years  _(Direct Equity Tax Credit Act (NL), SNL2000 c D-18.1)_
- **Holding period** — Shares must be held for at least 4 years; early disposition triggers recapture  _(Direct Equity Tax Credit Act (NL), SNL2000 c D-18.1)_
- **Lifetime per-EBC cap** — $1M raised under DETC  _(Direct Equity Tax Credit Act (NL), SNL2000 c D-18.1)_

### Reviewer checklist

- Confirm IET Certificate of Registration is dated before the share subscription
- Confirm the investor is at arm's length from the EBC (cannot be a specified shareholder ≥ 10% pre-investment)
- Confirm shares are newly issued treasury shares, not secondary
- Confirm sector classification matches the 35% / 20% / 10% rate on the T5004 / NL-equivalent slip
- 4-year holding period flagged on workpapers for future years

## 8. NL Film & Video Industry Tax Credit

- **Credit description** — Refundable credit for a qualifying NL corporation producing film/video in NL
- **Rate** — 40% of eligible NL labour expenditure
- **Cap on production cost** — Capped at 25% of total certified production cost
- **Per-project annual cap** — $4M
- **Eligibility certificate requirement** — Requires eligibility certificate from the NL Film Development Corporation before principal photography begins
- **Coordination with federal credits** — Coordinated with federal CPTC / PSTC — federal credit reduces the eligible labour base for NL purposes (parallel-grind rule)

## 9. NL Insurance Premium Tax (IPT) — the big NL-specific cost

Governed by the *Insurance Premiums Tax Act* (NL). Tax is levied on the insurer but is statutorily passed through to the insured as a separate line on the policy.

### Rates (2025)

**Rates (2025)**

| Category | Rate |
| --- | --- |
| Property, casualty, liability, fire, surety, fidelity, BI, E&O, D&O, cyber, professional indemnity | **15%** |
| Life, accident & sickness, group health | **15%** |
| Automobile (private passenger and commercial) | **5%** |
| Reinsurance assumed by NL-licensed insurer | exempt (already taxed at source) |
| Marine cargo on international voyages | exempt |
| Federal Crown contracts | exempt |

### Why this matters for accounting work

- A $10,000 commercial general liability premium in NL → $1,500 IPT → $11,500 cash out the door. In Ontario the same premium would carry $800 IPT. NL businesses pay roughly 2x the indirect insurance tax of most provinces.
- IPT is a deductible business expense for income tax — capture it on Schedule C / T2125 / corporate T2 along with the premium.
- IPT is not GST/HST-recoverable — it is not GST/HST, it is a separate provincial premium tax.
- Self-insurance and unlicensed-insurer placements still attract IPT at 4% (special tax) — the insured (not the insurer) must self-assess and remit to NL Department of Finance using Form IPT-1.

- **Self-insurance / unlicensed-insurer placements rate** — 4% (Insured must self-assess and remit using Form IPT-1)  _(Form IPT-1)_

### Reviewer flags

- Brokered placement with a non-NL-licensed insurer (e.g., Lloyd's syndicate direct) → check whether broker collected IPT or the insured must self-assess. Common miss.
- Captive insurance arrangements → captive must register as an unlicensed insurer and remit 4% IPT; consult specialist.
- Multi-province policies → IPT applies only to the NL-situate risk portion. Schedule of values from broker required.

## 10. Form NL428 — Provincial Tax and Credits

Filed with the T1 General. Structure:

## 10. Form NL428 — Provincial Tax and Credits

**Part A — NL Tax on Taxable Income**

| Bracket | Rate |
| --- | --- |
| First $44,192 | 8.7% |
| $44,192–$88,382 | 14.5% |
| $88,382–$157,792 | 15.8% |
| $157,792–$220,910 | 17.8% |
| $220,910–$282,214 | 19.8% |
| $282,214–$564,429 | 20.8% |
| $564,429–$1,128,858 | 21.3% |
| Over $1,128,858 | 21.8% |

## 10. Form NL428 — Provincial Tax and Credits

Part B — NL Non-Refundable Tax Credits — basic personal amount ~$11,067, spouse, age, pension, disability, tuition, donations, medical, volunteer firefighter $500, etc.

## 10. Form NL428 — Provincial Tax and Credits

Part C — NL Tax
- Apply low-income tax reduction
- Apply political contribution credit, DETC, etc.
- Result → Line 42800 of T1

## 10. Form NL428 — Provincial Tax and Credits

Refundable credits (Income Supplement, Seniors' Benefit, Disability Amount Supplement) computed separately on Form NL479.

## 11. Worked example — St. John's tech founder + NL angel investor

Facts. Maya runs an early-stage SaaS startup ("CodCloud Inc.") incorporated in NL, registered as an EBC with IET on 2025-02-01 in the priority "tech" sector. On 2025-06-15 she raises $50,000 from a local angel, Brendan (NL resident, arm's length, owns 0% before the round). Brendan subscribes for newly-issued common shares.

## 11. Worked example — St. John's tech founder + NL angel investor

Brendan's 2025 NL Direct Equity Tax Credit.

- Eligible investment: min($50,000, $50,000 annual cap) = $50,000
- Sector: priority (tech) → rate 35%
- Credit = $50,000 × 35% = **$17,500**
- Applied against Brendan's 2025 NL tax (Line 42800 reduction via NL428)
- Brendan's 2025 NL tax payable before credit: $14,200 → credit absorbs $14,200 → **$3,300 carries forward** for up to 7 years (or back 3)
- 4-year holding period flagged through 2029-06-15 — file note in workpapers

## 11. Worked example — St. John's tech founder + NL angel investor

Maya's IPT on CodCloud's new commercial policy.

- CodCloud buys a $12,000 cyber + E&O package effective 2025-07-01.
- IPT = $12,000 × 15% = **$1,800**
- Total cash out: $13,800. Deductible on T2 Schedule 125 as insurance expense (premium + IPT).
- No GST/HST recovery (IPT is not a sales tax).

## 11. Worked example — St. John's tech founder + NL angel investor

Maya's NL personal credits (separate).

- Maya pays herself a $48,000 T4 salary in 2025. Income above the Low-Income Tax Reduction threshold → no reduction.
- Family net income $48,000 → NL Income Supplement phased out ($40k threshold + 8% claw-back fully erodes by ~$46.5k).
- No senior, no disability, no volunteer service → only basic personal amount on NL428.

## 12. Conservative defaults

- If DETC sector classification is ambiguous → default to 20% (general) until IET letter confirms priority sector.
- If volunteer hours are between 195 and 205 with no signed letter from Fire Chief → do not claim.
- If client moved into NL during 2025 → refer to "province of residence on Dec 31" rule and refuse NL428 if they were resident elsewhere on Dec 31; redirect to ca-tax-workflow-base for the correct province skill.
- If unsure whether IPT applies to a non-NL-licensed placement → assume it does and have client self-assess at 4%; safer than missing the remittance.
- If a client claims the Volunteer Firefighter Credit AND the federal VFA on the same hours → fix it; only one is allowed.
- Always file the T1 for low-income NL residents — Income Supplement and Seniors' Benefit are refundable and require a filed return.

## 13. Sources

- NL Department of Finance — Tax Programs and Incentives, https://www.gov.nl.ca/fin/tax-programs-incentives/
- *Income Tax Act, 2000* (NL), SNL2000 c I-1.1
- *Direct Equity Tax Credit Act* (NL), SNL2000 c D-18.1, and *Direct Equity Tax Credit Regulations*
- *Insurance Premiums Tax Act* (NL), RSNL1990 c I-12, with 2024 amendments confirming 15% commercial / 5% auto
- *Income Supplement and Seniors' Benefit* — administered jointly with CRA under the NL–Canada tax collection agreement
- NL Film Development Corporation — Film & Video Industry Tax Credit Guidelines
- Form NL428 (2025), Form NL479 (2025), Form T5004 (claim slip for DETC)
- NL Department of Industry, Energy and Technology — DETC EBC registration portal

## End of skill.

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
