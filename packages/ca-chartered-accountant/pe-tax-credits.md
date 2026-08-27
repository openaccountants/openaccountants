---
name: pe-tax-credits
description: Use this skill for Prince Edward Island provincial tax credits — PEI Low-Income Tax Reduction, PEI Sales Tax Credit, PEI Volunteer Firefighter / Ground Search and Rescue Tax Credit, Teacher School Supply Amount (PEI), PEI Equity Tax Credit (35%), PEI Innovation and Development Labour Rebate. Triggers "PEI tax credits", "Prince Edward Island credits", "PEI Equity Tax Credit", "Form PE428", "PEI ITC".
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PE Tax Credits

## Prince Edward Island — Provincial Tax Credits — Skill v1.0

This skill covers the full inventory of Prince Edward Island provincial tax credits available to individuals and corporations for the 2025 tax year. It is designed to be loaded alongside `pe-individual-return` (for personal returns) or alongside the federal T2 corporate skill (for CIT credits). It is the canonical reference for PEI-specific reductions, refundable credits, non-refundable credits, and the two flagship business incentives: the **PEI Equity Tax Credit** and the **PEI Innovation and Development Labour Rebate**.

PEI has a comparatively small credit catalogue versus Ontario or BC, but it punches above its weight on two fronts: (1) a generous 35% angel-investor Equity Tax Credit, and (2) the lowest small-business CIT rate in Canada when combined with the federal 9% SBD (federal 9% + PEI 1% = **10% combined** on the first $500,000 of active business income).

## 1. Quick Reference — Personal + Corporate Credit Summary

**Quick Reference — Personal + Corporate Credit Summary**

| Credit | Type | Amount / Rate | Form |
| --- | --- | --- | --- |
| PEI Low-Income Tax Reduction | Reduction | Reduces PE tax to nil for low-income filers | PE428 |
| PEI Sales Tax Credit | Refundable | Up to ~$220 single + ~$110/child, quarterly | Auto via T1 |
| PEI Volunteer Firefighter / GSAR | Non-refundable | $500 amount (× 9.65% = $48.25) | PE428 |
| Teacher School Supply Amount (PE) | Non-refundable | $500 amount | PE428 |
| PEI Children's Wellness Tax Credit | Non-refundable | $500/child amount | PE428 |
| **PEI Equity Tax Credit (PEI ETC)** | Non-refundable | **35%** on eligible investment | T1 Sch ETC / PE428 |
| PEI Innovation & Development Labour Rebate | Refundable rebate | 25% of eligible labour | Innovation PEI application |
| PEI Provincial CIT — General | Corporate rate | 16% | T2 / Sch 5 |
| PEI Provincial CIT — Small Business | Corporate rate | 1% (combined fed+PE = 10%) | T2 / Sch 5 |

**Brackets reminder (for credit conversion):** the PEI lowest-bracket rate for 2025 is **9.65%**, which is the rate at which most non-refundable amounts are multiplied. (Confirm against the current PE428 — PEI's lowest rate has historically been 9.65%; if PEI legislation revised this for 2025, defer to the published PE428 schedule.)

## 2. Required Inputs + Refusal Catalogue

### Inputs required from intake

- **PEI residency** — PEI residency on December 31, 2025 (required for all personal credits in this skill — non-residents and part-year residents need a different routing).
- **Family net income** — Family net income (line 23600 + spouse line 23600) — drives Low-Income Reduction and Sales Tax Credit thresholds.
- **Number of eligible children** — Number of eligible children under 18 — drives Wellness Credit and Sales Tax Credit family component.
- **Volunteer hours** — 200+ hours of eligible volunteer firefighting OR ground search-and-rescue with a recognized PEI department — required for the $500 amount.
- **Teacher credentials** — PEI-licensed elementary or secondary teacher and a record of out-of-pocket school supply purchases.
- **Equity investment documentation** — PEI ETC certificate of registration issued by PEI Finance, share subscription agreement, and proof of payment.
- **Innovation PEI rebate application** — pre-approval letter from Innovation PEI and eligible labour cost schedule (T4 reconciliation).

### Refusals (route elsewhere or escalate to reviewer)

**Refusals (route elsewhere or escalate to reviewer)**

| Scenario | Reason |
| --- | --- |
| Non-resident of PE on 31 Dec 2025 | Provincial credits are residency-based — route to province of residence |
| Part-year PEI resident | Pro-ration rules differ — escalate to reviewer |
| Equity Tax Credit on an investment in a non-registered issuer | Refuse — only PEI-registered eligible business corporations qualify |
| Equity Tax Credit claim for an RRSP-held investment | Refuse — RRSP/RRIF holdings do not qualify for the ETC |
| Innovation Labour Rebate without Innovation PEI pre-approval | Refuse — pre-approval is mandatory; cannot self-claim |
| Corporate claim under M&P credit or PEI Film credit | Out of scope for v1.0 — escalate |
| Indigenous taxpayer with Section 87 exempt income | Escalate — interaction with PEI credits requires reviewer |
| Bankruptcy filings | Out of scope — escalate |

## 3. PEI Low-Income Tax Reduction

The PEI Low-Income Tax Reduction is a non-refundable mechanism on Form PE428 that reduces PEI provincial tax owing to **nil** for taxpayers below a defined family-net-income threshold, and phases out gradually above that threshold.

### Mechanics (2025)

- **Mechanics steps** — Compute base PEI tax after non-refundable credits on PE428. Apply the basic reduction amount + spouse amount + each dependant amount. Subtract the phase-out: a percentage of the family net income above the threshold. If the result is positive, it reduces PEI tax dollar-for-dollar; if negative, the reduction is zero (it cannot create a refund).

### Typical 2025 parameters (confirm against the current PE428 instructions)

- **Basic reduction amount** — ~$350 per filer
- **Each dependent child under 18** — ~$300
- **Each dependent child under 18** — ~$300
- **Phase-out threshold** — family net income around $22,000
- **Phase-out rate** — 5% percent (on each dollar above the threshold)

Conservative default: if the published PE428 for 2025 has not been confirmed by reviewer, **use prior-year values and flag for review** rather than estimating.

### Worked example

Single PEI filer with net income of $19,500 and one child under 18:
- Reduction amount: $350 (basic) + $300 (child) = $650
- Family net income $19,500 is below the $22,000 threshold → no phase-out
- Reduction = $650
- If base PE tax after credits is $480, the reduction wipes it out → **PE tax payable = $0**. The excess $170 of reduction is lost (no refund).

## 4. PEI Sales Tax Credit

The PEI Sales Tax Credit is a **refundable** quarterly benefit paid by the CRA together with the federal GST/HST credit, designed to offset the regressive impact of HST on low- and modest-income PEI households. There is no separate application — eligibility is determined automatically from the T1.

### 2025 amounts (annual maximums; confirm against PEI Finance bulletin)

- **Adult basic component** — ~$110
- **Single parent supplement** — ~$55
- **Single parent supplement** — ~$55
- **Each dependent child under 19** — ~$60
- **Family maximum (typical 2-parent + 2-child household)** — ~$285–$330

PEI Finance has periodically described the credit as "up to roughly $220 for a single adult plus $110 per child" in summary materials — these figures bundle the spouse/child components together. Use the per-component table for line-item precision.

### Income test

- **Full-payment threshold** — approximately $30,000
- **Phase-out rate** — 2% percent (per dollar of family net income above the threshold)
- **Fully phased out at** — family net income in the $45,000–$50,000 range for a typical family

### Payment schedule

- **Payment schedule** — Paid quarterly in July, October, January, and April alongside the federal GST/HST credit deposit. The benefit year runs July 2026 through June 2027 based on the 2025 T1.

## 5. PEI Volunteer Firefighter & Ground Search and Rescue Tax Credit

- **Volunteer Firefighter/GSAR credit amount** — $500 ($500 × 9.65% = approximately $48.25 in actual tax savings) (individuals who performed at least 200 hours of eligible volunteer service during 2025 with a recognized PEI fire department, ground search-and-rescue organization, or both combined)

### Rules

- **Hours combination rule** — Hours from federal Volunteer Firefighters Amount (VFA) and federal Search and Rescue Volunteers Amount (SRVA) can be combined to meet the 200-hour threshold for the PEI credit, but the same hours cannot be used twice (i.e., if the taxpayer already claimed the $6,000 federal VFA, those same 200 hours cannot be re-used for any other purpose).
- **No payment rule** — The taxpayer cannot also be receiving payment for the same work (the credit is for genuine volunteers only).
- **Certification retention** — A signed certification from the fire chief or GSAR coordinator confirming the hours must be retained — not filed with the return but produced on CRA review.

## 6. PEI Equity Tax Credit (PEI ETC)

The flagship business-investment incentive in PEI. The **PEI Equity Tax Credit** is a **non-refundable 35% personal income tax credit** on qualifying equity investments made by an individual into a registered PEI eligible business corporation. This is among the **most generous angel-investor credits in Atlantic Canada** — Nova Scotia's equivalent is 35% (cap $50k), New Brunswick's is 50% but with stricter caps, and Newfoundland's is 35–45%. PEI's 35% with a more generous annual cap makes it competitive.

### Key parameters (2025)

**Key parameters (2025)**

| Parameter | Value |
| --- | --- |
| Credit rate | **35%** |
| Maximum eligible investment per investor per year | **$100,000** (yielding $35,000 credit) |
| Maximum credit per year | **$35,000** |
| Minimum investment | Typically **$1,000** |
| Hold period | **4 years** — shares must be held for at least 4 years or the credit is clawed back |
| Carryforward of unused credit | **7 years** |
| Carryback | **3 years** |

### Who qualifies as an "eligible business corporation" (EBC)?

- **PEI presence requirement** — PEI head office and substantial PEI presence (typically ≥75% of payroll attributable to PEI residents).
- **Eligible active business** — Engaged in an eligible active business — generally manufacturing, processing, tourism, export services, technology, aquaculture, or other approved sectors; explicitly excludes retail/restaurant, real estate development, and professional services (law, accounting, medicine).
- **Gross assets threshold** — historically $25 million
- **Registration requirement** — Registered with PEI Department of Finance as an EBC and issued a registration number before share issuance.

### Investor eligibility

- **Individual resident requirement** — Must be an individual resident of PEI (corporations cannot claim — there is no corporate ETC stream in v1.0 scope).
- **New shares requirement** — Must subscribe for newly-issued common voting shares (or eligible preferred shares per the program rules) — secondary-market share purchases do not qualify.
- **Arm's-length requirement** — Must not be related to the issuer in a way that would make this a non-arm's-length transaction outside the program rules.
- **Hold period requirement** — Must hold the shares for the full 4-year hold period.

### Documentation required for the T1 claim

- **PEI ETC Certificate** — issued by PEI Finance to the issuer, then forwarded to each investor — this is the controlling document.
- **Share subscription agreement** — and proof of payment (bank transfer or cancelled cheque).
- **Share certificate** — in the investor's name.

### Filing

- **Filing rule** — The credit is claimed on Form PE428 in the year of investment. Unused credit carries forward 7 years and back 3 years. The credit reduces PEI tax payable but cannot create a refund (non-refundable).  _(Form PE428)_

### Clawback

- **Clawback rule** — If the investor disposes of the shares before 4 years from issuance, PEI Finance recaptures the credit on a sliding scale (or in full if disposed in year 1). Disposal includes redemption, share buyback, or any transfer not specifically permitted under the regulations.

## 7. PEI Innovation and Development Labour Rebate

- **Innovation and Development Labour Rebate rate** — 25% of eligible labour costs (refundable rebate for businesses operating in PEI in innovation-related sectors; not a tax credit claimed on the T1 or T2 — program administered by Innovation PEI (a provincial Crown agency) that issues cash payments directly to the business after audit)

### Mechanics

- **Pre-approval requirement** — Business applies to Innovation PEI before incurring the labour costs — pre-approval is required.
- **Eligible labour** — T4 wages, T4A contractor payments, and certain employer benefits paid to individuals working on the approved project.
- **Post-year-end submission** — After year-end, the business submits an audited expenditure schedule and supporting payroll records.
- **Verification and issuance** — Innovation PEI verifies and issues the rebate as a cash payment (treated as government assistance — reduces the business's deductible labour expense for T2 purposes, OR is included in income if so elected).

### Eligible sectors

- **Eligible sectors list** — Bioscience and life sciences; Information technology and software development; Aerospace; Advanced manufacturing; Renewable energy; Other approved innovation sectors at Innovation PEI's discretion

### Annual rebate cap

- **Annual rebate cap** — Typically capped per business per year — historically around $500,000 per project but program parameters are renegotiated each provincial budget cycle. Confirm with Innovation PEI.

### Interaction with federal SR&ED

- **SR&ED stacking rule** — A business can claim both the federal SR&ED ITC (Investment Tax Credit) and the PEI Innovation Labour Rebate on the same labour costs, but the rebate reduces the federal SR&ED qualifying expenditure pool (it is government assistance under ITA s. 127(11.1)). Reviewer should model the net combined benefit.  _(ITA s. 127(11.1))_

## 8. PEI Children's Wellness Tax Credit

- **Children's Wellness Tax Credit amount** — $500 per eligible child under 18 (for registration fees in eligible fitness, sports, arts, or wellness activities during 2025. Multiplied by 9.65% → approximately $48.25 per child in actual tax savings)

### Eligible expenses

- **Program duration requirement** — Registration / membership fees in an eligible program of at least 8 consecutive weeks OR a day-camp of at least 5 consecutive days.
- **Wellbeing contribution requirement** — Programs must contribute to the child's physical, mental, or social wellbeing.
- **Exclusions** — Excludes equipment purchases, travel, meals, and lodging.

### Documentation

- **Documentation rule** — Retain receipts from the program operator showing the child's name, program description, dates, and amount paid. The credit can be claimed by either parent (or split) but the same expense cannot be claimed twice.

## 9. PEI Provincial Corporate Income Tax

While CIT credits are largely out of scope for this v1.0 skill (handled at the T2 layer), the PEI provincial CIT rates are documented here for context because they affect after-tax modelling of the credits above.

**PEI Provincial Corporate Income Tax rates**

| Income type | Federal rate | PE rate | **Combined** |
| --- | --- | --- | --- |
| General active business income | 15% | **16%** | **31%** |
| Active business income within the SBD ($500k) | 9% | **1%** | **10%** |
| Investment income (CCPC, AAII) | 38.67% (after refundable component netting) | 16% | varies |
| Manufacturing & processing (within SBD) | 9% | 1% | 10% |

The 1% PEI small business rate is the lowest provincial small business CIT rate in Canada (tied with Manitoba's 0% in some prior years; PEI has been at 1% since the most recent budget cycle). Combined with the federal 9%, a PEI CCPC pays just 10% on its first $500,000 of active business income — a meaningful inducement for owner-managers to incorporate in PEI.

## 10. Form PE428

- **Form PE428 definition** — Form PE428 — Prince Edward Island Tax is the personal-tax provincial schedule for PEI residents and is filed with the T1 General. It contains: Part A: PEI non-refundable tax credits (basic personal amount, spouse, age, disability, CPP/EI, medical, donations — most of these mirror the federal Schedule 1 amounts but at PEI rates). Part B: PEI tax on taxable income (bracket calculation). Part C: PEI Low-Income Tax Reduction (Section 3 of this skill). Part D: PEI surtax (if applicable in a given year — PEI has periodically had a surtax for high-income earners; confirm against the 2025 form). Part E: PEI Volunteer Firefighter & GSAR amount, Teacher School Supply amount, Children's Wellness amount. Schedule for the PEI Equity Tax Credit (separate schedule attached to PE428, referencing the certificate number).  _(Form PE428)_
- **Filing deadline** — with the T1, by April 30, 2026 (or June 15, 2026 for self-employed). Balance due always April 30.

## 11. Worked Example — Charlottetown Angel Investor

Janet, a PEI-resident software consultant with 2025 net employment income of $185,000, invests $100,000 on October 1, 2025 into newly-issued common shares of *Atlantic Bioscience Inc.*, a PEI-registered Eligible Business Corporation. She receives ETC Certificate #2025-ETC-0142 from PEI Finance. She has no other PEI-specific credits this year.

- Eligible investment: $100,000
- ETC rate: 35%
- **2025 ETC credit: $35,000**

- PEI taxable income (after federal-to-PE adjustments): approximately $182,000
- PEI tax (after basic personal amount and standard non-refundable credits at 9.65%, plus higher brackets): approximately **$22,800**
- Apply 2025 ETC credit: $22,800 used → PE tax payable becomes **$0**
- Remaining ETC credit: $35,000 − $22,800 = **$12,200 carried forward**

Janet has up to 7 years to use the remaining $12,200. Assuming her PEI tax in 2026 is roughly $24,000, she can fully absorb the carried-forward $12,200 in 2026 and reduce 2026 PE tax by that amount.

Janet must hold the Atlantic Bioscience shares until October 1, 2029 (4 years from issuance). If she sells before then, PEI Finance will issue a clawback assessment — full clawback if disposed in year 1, sliding scale for years 2–4.

If Janet's 2025 PE tax had been insufficient AND her 2024/2023/2022 PE tax was higher, she could elect to carry back unused ETC up to 3 years. In her case carryforward is more efficient because her income is rising.

The reviewer should verify (a) Atlantic Bioscience's EBC registration was active on October 1, 2025, (b) the certificate number matches the share subscription, and (c) Janet is not a "specified shareholder" creating a non-arm's-length disqualification.

## 12. Conservative Defaults

When parameters are ambiguous or the 2025 PEI Finance bulletin has not yet been published in final form, apply these defaults:

1. **Use prior-year (2024) parameter values** and flag the line as "PROVISIONAL — confirm against final 2025 PE428".
2. **For the Equity Tax Credit**: always verify the EBC certificate number against the PEI Finance registry before claiming; never accept investor representations alone.
3. **For the Sales Tax Credit**: do not manually compute the quarterly payment — let CRA compute it. The T1 simply triggers eligibility.
4. **For the Low-Income Reduction**: if the family net income is within $1,000 of the phase-out threshold, recompute carefully and verify against the form's worksheet — small errors here can flip the credit between $0 and several hundred dollars.
5. **For the Innovation Labour Rebate**: never claim or model this on the T2 itself — it flows through Innovation PEI as a separate cash payment, with separate accounting and timing.
6. **For all non-refundable credits**: confirm the conversion rate against the current PE428 (historically 9.65%, but verify).
7. **Refuse and escalate** any scenario involving part-year PEI residency, non-resident claims, RRSP-held ETC investments, or bankruptcy interactions.

## 13. Sources

- **PEI Income Tax Act**, RSPEI 1988, c. I-1 — primary statute for provincial credits.
- **PEI Equity Tax Credit Act** and its regulations — governs the 35% ETC, EBC registration, hold periods, and clawback rules.
- **PEI Department of Finance — Taxation and Property Records Division** — administrative bulletins and PE428 instructions.
- **Innovation PEI** — program guidelines for the Innovation and Development Labour Rebate, including pre-approval procedures and audit requirements.
- **CRA Form PE428 (2025)** — the form-level authority for credit amounts, thresholds, and conversion rates.
- **CRA T4055 / T4012 (T2 corporation guide)** — for PEI CIT rates and SBD interaction.
- **PEI Provincial Budget 2025** — annual revisions to credit parameters, thresholds, and program caps.

*All figures should be confirmed against the final 2025 PE428 and the PEI Finance bulletin issued for the 2025 tax year before any return is filed. This skill is reviewer-supervised and is not a substitute for credentialed PEI tax practitioner signoff.*

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
