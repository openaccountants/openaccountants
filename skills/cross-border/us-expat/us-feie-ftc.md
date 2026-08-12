---
name: us-feie-ftc
description: "US federal tax for citizens and green-card holders living abroad: the Foreign Earned Income Exclusion (IRC §911, Form 2555) versus the Foreign Tax Credit (IRC §901/§904, Form 1116). Covers the bona-fide-residence and physical-presence tests, the foreign housing exclusion, the §911 election and its revocation lock-out, the stacking rule, and the FEIE-versus-FTC decision. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
version: 0.1
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
depends_on: - cross-border-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Feie Ftc

## US Foreign Earned Income Exclusion vs Foreign Tax Credit v0.1

## What this file is

This is a topic content skill that **loads on top of `cross-border-tax-workflow-base`** and assumes the **`cross-border-tax-router`** has already run its Step 0 residency map and routed the situation here. It carries the substantive US rules for a US citizen or lawful permanent resident (green-card holder) earning wages or self-employment income abroad: when to elect the Foreign Earned Income Exclusion under **IRC §911** (claimed on **Form 2555**), when to instead take the Foreign Tax Credit under **IRC §901 / §904** (claimed on **Form 1116**), and how the two interact. It produces a working paper and reviewer brief; it never produces a filed return, and no human has signed off on its output until `request_accountant_review` returns a credentialed sign-off.

**Currency.** The FEIE cap, the housing base/ceiling amounts, and bracket thresholds are **inflation-indexed and change every year**. This file never hardcodes a current figure as authoritative — it instructs the agent to confirm the current tax-year number from the relevant IRS source (Form 2555 instructions, Rev. Proc. inflation-adjustment release) before computing.

## Layer A — Reference layer (the rules)

### A.1 — Who is in scope (IRC §911(d)(1), §7701(b)(6))

- **Worldwide taxation and scope of relief mechanisms** — US citizens and green-card holders are taxed on worldwide income regardless of where they live. §911 and the FTC are the two relief mechanisms against the resulting double tax. Non-resident aliens are out of scope for this file.  _(IRC §911(d)(1), §7701(b)(6))_

### A.2 — The §911 qualification gate (decision tree)

- **§911 qualification requires both tax home abroad and one presence test** — To exclude foreign earned income under §911 the person must satisfy both: (1) Tax home in a foreign country — the tax home is the person's regular/principal place of business; if their abode remains in the US, they fail this test even if they work abroad. AND (2) One of the two presence tests: Bona-fide-residence test — the person is a bona-fide resident of a foreign country for an uninterrupted period that includes a full tax year; this is a facts-and-circumstances test (intent, ties, duration, family location, local tax status). Available to US citizens and to green-card holders only if a treaty non-discrimination article supports it. Physical-presence test — the person is physically present in a foreign country/countries for ≥330 full days in any 12 consecutive months. Mechanical day-count; the 12-month window can straddle two tax years and the exclusion is prorated.  _(§911(d)(1), (d)(3); §911(d)(1)(A); §911(d)(1)(B))_
- **§911 qualification decision tree** — Foreign earned income? └─ Tax home abroad (abode not in US)?  ──no──▶ §911 unavailable → use FTC (Form 1116) └─ yes ├─ Bona-fide resident a full tax year?  ──yes──▶ §911 available └─ ≥330 full days in 12 consecutive months? ──yes──▶ §911 available (prorated) └─ neither ──▶ §911 unavailable → use FTC (Form 1116)  _(IRC §911(d)(1))_

⚑ AUDIT FLASH POINT — The bona-fide-residence test (§911(d)(1)(A)) is a facts-and-circumstances judgement the IRS actively challenges. Claiming a foreign tax home as a non-resident of the host country, retaining a US abode, short assignments, or filing a host-country return as a non-resident all undercut it. Document: host-country residence permit/visa, local tax-residency status, lease/property, family location, and intent of an indefinite (not temporary) stay. Where bona-fide residence is shaky, fall back to the mechanical 330-day physical-presence test or to the FTC, which needs no presence test.

### A.3 — What §911 excludes, and the cap

- **Foreign earned income definition** — Foreign earned income = compensation for services performed abroad (wages, self-employment income). It does not include passive income (dividends, interest, capital gains, rents), pension/annuity income, or amounts paid by the US government.  _(§911(b)(1), (d)(2))_
- **FEIE exclusion cap** — ~US$120k–130k range in recent years (illustrative only; not current — must be confirmed) USD (Annual, inflation-indexed, per-qualifying-person; confirm current tax-year figure)  _(§911(b)(2)(D))_
- **Proration of exclusion cap** — Prorated by qualifying days if the qualifying period covers only part of the tax year (physical-presence straddles especially).  _(§911(b)(2)(A))_

### A.4 — Foreign housing exclusion / deduction (§911(c))

- **Foreign housing exclusion/deduction mechanics** — Qualifying housing expenses above a base amount may be excluded (employees) or deducted (self-employed). The base amount (a percentage of the FEIE cap) and the ceiling on qualifying expenses are both inflation-indexed and the ceiling is adjusted for high-cost locations in the Form 2555 instructions. Confirm both current-year amounts; do not hardcode.  _(§911(c)(1)–(4))_

⚑ AUDIT FLASH POINT — The housing base amount floor and the location-specific ceiling are routinely miscomputed. Expenses below the base produce no benefit; expenses above the (location-adjusted) ceiling are capped. Pull the current-year base and the high-cost-area table from the Form 2555 instructions and show the arithmetic; never assume the standard ceiling for a listed high-cost city.

### A.5 — The election and its revocation lock-out (§911(e), Reg. §1.911-7)

- **§911 election and revocation lock-out** — §911 applies only if elected, on Form 2555 filed with the return. An election stays in effect for future years until revoked. A taxpayer may revoke the election; but once revoked, they cannot re-elect §911 for 5 tax years without IRS consent (a ruling).  _(§911(e)(2), Reg. §1.911-7(b))_

⚑ AUDIT FLASH POINT — The 5-year §911 revocation lock-out is an irreversible trap. Switching from FEIE to FTC in a single year by revoking the election (rather than simply not benefiting from it) bars re-election for 5 years absent a private letter ruling. If the person may want FEIE back soon, do not revoke — model the FTC path without a §911 revocation, and flag the choice for the reviewer to own.

### A.6 — The stacking rule (§911(f))

- **Stacking rule for excluded income** — Excluded income is not taxed, but it still pushes the remaining (non-excluded) income into higher brackets: tax on the non-excluded income is computed as if the excluded amount were the bottom layer of the bracket stack. Practically, §911 removes income from the base but not from the rate-setting stack — use the Foreign Earned Income Tax Worksheet in the Form 1040 instructions.  _(§911(f))_

### A.7 — Foreign Tax Credit mechanics (§901, §904; Form 1116)

- **§901 credit for foreign income taxes** — §901 grants a credit for foreign income taxes paid or accrued.  _(§901)_
- **§904 limitation and basket rules** — §904 limitation: the credit cannot exceed US tax on foreign-source income, computed separately per income category ("basket") — chiefly the general basket (active/earned) and the passive basket. Excess credit in one basket cannot offset US tax on income in another.  _(§904)_
- **FTC carryback/carryforward rules** — Excess FTC carries back 1 year and forward 10 years, within the same basket.  _(§904(c))_
- **§911 coordination — no double-dip** — No FTC is allowed on income excluded under §911. Foreign tax allocable to excluded income is disallowed; only the foreign tax on the non-excluded portion is creditable. You cannot exclude income and credit the foreign tax on it.  _(§911(d)(6))_

### A.8 — The FEIE-vs-FTC decision (decision tree)

- **FEIE-vs-FTC decision tree** — Foreign country effective tax rate on the earned income? ├─ High-tax country (foreign rate ≥ US rate on that income) │     └─ FTC (Form 1116) generally better: │          • foreign tax usually fully offsets US tax, often with carryforward │          • income stays "earned" for refundable Additional Child Tax Credit & IRA room │          • no §911 election to revoke later └─ Low / no-tax country (foreign rate ≈ 0, or < US rate) └─ FEIE (Form 2555) generally better: • little/no foreign tax to credit, so FTC gives little relief • §911 removes the income from the US base (subject to the cap & stacking) • watch: FEIE can ZERO OUT earned income → kills refundable ACTC and IRA room

⚑ AUDIT FLASH POINT — Electing FEIE can destroy the refundable Additional Child Tax Credit and IRA-contribution room. Excluding the earned income removes the compensation that supports an IRA contribution (§219) and removes the earned income that drives the refundable portion of the Child Tax Credit (§24). In a low-tax country a family may net more cash using the FTC (or excluding only up to the cap and leaving enough earned income) than using full FEIE. Model both before recommending.

⚑ AUDIT FLASH POINT — You cannot double-dip (§911(d)(6)). Claiming FEIE on Form 2555 and an FTC on Form 1116 for the foreign tax on the same excluded income is disallowed. If the person exceeds the FEIE cap, only the foreign tax on the excess (non-excluded) income is creditable — allocate the foreign tax pro-rata and show the disallowed portion.

## Layer B — Executable layer (the procedure)

Given a person's facts — foreign salary / SE income, days abroad (and the 12-month window), foreign income tax paid, host country, filing status, children, IRA intent — produce the recommended election, the numbers, and the forms.

0. **Step 1 — Confirm scope** — Verify US citizen or green-card holder with foreign earned income. Separate earned income (in scope) from passive income (FTC only, passive basket — A.7).
0. **Step 2 — Run the §911 gate (A.2)** — Establish tax home abroad (abode not US). Then test bona-fide residence (full tax year) or physical presence (≥330 full days in 12 consecutive months). Record which test, the dates, and the day count. If neither passes → §911 is unavailable; go straight to FTC (Step 6).
0. **Step 3 — Pull current-year indexed figures** — Confirm, for the tax year in question: the FEIE cap, the housing base amount, and the housing ceiling (with high-cost-area adjustment for the host city) from the Form 2555 instructions. Do not reuse a prior-year number.
0. **Step 4 — Compute the FEIE path (if available)** — Excludible earned income = min(foreign earned income, FEIE cap), prorated by qualifying days if the period is partial (A.3). Add the housing exclusion = qualifying housing expenses − base amount, capped at the (location-adjusted) ceiling (A.4). Apply the stacking rule (A.6) — compute residual US tax on non-excluded income via the Foreign Earned Income Tax Worksheet (tax at the rates that apply as if the excluded income were stacked underneath). Note the side effects: does FEIE zero out earned income, killing refundable ACTC / IRA room?
0. **Step 5 — Compute the FTC path** — Foreign tax paid/accrued on the general-basket earned income (and a separate Form 1116 for any passive-basket income). §904 limitation per basket = US tax × (foreign-source taxable income in basket ÷ total taxable income). Allowed credit = min(foreign tax in basket, §904 limit). Excess → carryback 1 / carryforward 10 (A.7). Earned income stays in the base, preserving ACTC refundability and IRA room.
0. **Step 6 — Compare and recommend** — Compute total US tax (and net family cash, including refundable credits) under: (a) full FEIE + housing, (b) full FTC, and, where relevant, (c) FEIE up to the cap with FTC on the excess. Recommend the lowest-tax / highest-net-cash option that is conservative and defensible. If recommending a switch away from a prior §911 election, check whether it requires a revocation (5-year lock-out, A.5) and flag it.
0. **Step 7 — Map the forms & build outputs** — Form 2555 (FEIE/housing), Form 1116 (FTC, one per basket), the Foreign Earned Income Tax Worksheet, and Schedule 3 (credits). Add any information returns the base §7 checklist flags (FBAR/FinCEN 114, Form 8938, 3520, 5471/8865, 8621) — those are not optional just because the income question is answered. Then assemble the base-§7 outputs (situation map, sequenced plan, reference trace, bridge summary, reviewer brief, hand-off).

## Topic self-checks (in addition to base §7)

- [ ] §911 gate documented: tax home abroad and which presence test (with dates / 330-day count)
- [ ] Current-year FEIE cap, housing base, and housing ceiling confirmed from IRS source, not hardcoded
- [ ] Partial-year proration applied where the qualifying period is incomplete
- [ ] Stacking rule (§911(f)) applied — residual tax via the Foreign Earned Income Tax Worksheet
- [ ] No FTC claimed on income excluded under §911 (§911(d)(6)); foreign tax allocated pro-rata to non-excluded income
- [ ] FTC §904 limitation computed per basket (general vs passive); carryback-1 / carryforward-10 noted for excess
- [ ] FEIE side-effects checked: refundable Additional Child Tax Credit (§24) and IRA-contribution room (§219)
- [ ] Any §911 revocation flagged for the 5-year re-election lock-out (§911(e)(2))
- [ ] Both FEIE and FTC paths modelled and the recommendation justified on net result
- [ ] Output marked tier 2 (research-verified); hand-off (base §8) executed

## Disclaimer

Provides computational and interpretive guidance on IRC §911 / §901–904 only. Not tax advice and not a filed return. Outcomes turn on entity- and residence-specific facts. Have outputs reviewed and signed by a qualified, licensed accountant before acting on them. Research-verified (tier 2) pending credentialed sign-off.

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
