---
name: us-state-estimated-tax-safe-harbors-matrix
description: Tier 2 US federal-level reference skill providing the 50-state matrix of estimated tax safe-harbor rules for individuals and corporations. Covers tax year 2025 including California's unique 30/40/0/30 installment schedule under R&TC §19136 (which differs from the federal 25/25/25/25 equal-installment rule), New York's corporate Mandatory First Installment (MFI) of 25% or 40% based on prior-year liability, state-by-state safe-harbor percentages (most mirror federal 100%/110% but some require 90% current-year only), underpayment penalty rates, annualized income method availability under §6654(d)(2)-equivalent state rules, and PTE election estimated payment schedules separate from corporate estimates.
jurisdiction: US
domain: federal-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# us-state-estimated-tax-safe-harbors-matrix

## 1. Scope

This skill is a **reference matrix** for state-level estimated tax obligations layered on top of the federal Form 1040-ES (individual) and Form 1120-W (corporate) regime. It addresses:

- **Quarterly due dates** for each state's individual and corporate estimated tax payments
- **Safe-harbor percentages** that shield taxpayers from underpayment penalties under each state's tax-administration statute
- **Installment schedules** (most states mirror the federal 25/25/25/25 equal-quarter rule; **California** uses **30/40/0/30** under R&TC §19136; **New York** applies a **Mandatory First Installment (MFI)** of 25 % or 40 % for corporations)
- **Underpayment penalty rates** (state-set, sometimes pegged to federal short-term AFR + 3, sometimes statutory flat)
- **Annualized income installment method** availability (the federal §6654(d)(2) equivalent at the state level)
- **Pass-through entity (PTE) election** estimated-payment regimes, which run on their own calendar and are **separate** from the owner's individual estimates and from regular corporate estimates

**Out of scope.** Property tax estimates, sales/use tax prepayments, state employer withholding deposits, state unemployment (SUTA) deposits, local/city estimated tax (NYC UBT, Philadelphia BIRT/NPT, San Francisco Gross Receipts) — these have separate skills.

**Audience.** Federal-and-state preparers, CPAs and Enrolled Agents working multistate returns, and reviewers checking whether a 2025 estimated-tax plan covers both the federal safe harbor under §6654 / §6655 **and** the parallel state safe harbor. A Circular 230 reviewer must sign off before any output reaches the taxpayer or any state revenue agency.

## 2. Federal Baseline (the starting point every state references)

- **Federal Baseline** — Every state's estimated tax rules reference the federal baseline under IRC §6654 (individual) and §6655 (corporate).  _(IRC §6654; IRC §6655)_

### 2.1 Individual — Form 1040-ES, IRC §6654

- **Due dates** — April 15, June 15, September 15, January 15 (of the following year)  _(IRC §6654)_
- **Installment shares** — 25 % / 25 % / 25 % / 25 % of required annual payment  _(IRC §6654)_
- **Safe harbor ("no underpayment penalty" test)** — pay the lesser of 90 % of current-year tax, or 100 % of prior-year tax (110 % if prior-year AGI > $150,000; $75,000 if MFJ filing separately)  _(IRC §6654)_
- **Annualized income installment method** — §6654(d)(2). Allows variable quarterly payments matched to year-to-date income; reported on Form 2210 Schedule AI.  _(IRC §6654(d)(2))_
- **Underpayment penalty rate (2025)** — federal short-term AFR + 3 percentage points, compounded daily. Rate is reset quarterly by the IRS in Revenue Rulings. Q4 2025 rate: 7 %.  _(IRS Revenue Rulings)_

### 2.2 Corporate — Form 1120-W, IRC §6655

- **Due dates (calendar-year C corp)** — April 15, June 15, September 15, December 15  _(IRC §6655)_
- **Installment shares** — 25 / 25 / 25 / 25  _(IRC §6655)_
- **Safe harbor** — 100 % of current-year tax, or 100 % of prior-year tax (only if prior year was a full 12 months and showed a positive tax liability). Large corporations (taxable income ≥ $1 million in any of the 3 preceding years) — current-year only, except the first installment may use the prior-year safe harbor with the shortfall caught up in Q2  _(IRC §6655)_
- **Annualized income** — §6655(e). Available; corporate version of the AI method.  _(IRC §6655(e))_
- **Penalty** — §6655 underpayment penalty at AFR + 3 (same calculation methodology as §6654 for individuals, applied to corporations).  _(IRC §6655)_

### 2.3 Why state rules diverge from federal

States are not required to conform to §6654 / §6655. Five recurring deviations:

1. **Different installment shares.** California (30/40/0/30 individual), New York (MFI for corp), a handful of others use unequal weights to front-load revenue.
2. **Different safe-harbor percentages.** Some states require 90 % current-year only (no prior-year safe harbor). Others bump the high-AGI prior-year threshold (e.g., California uses 110 % at AGI > $150,000 mirroring federal, but applies it at California AGI).
3. **Different due dates.** Most align with federal, but a few (e.g., Iowa, Hawaii) shift the final installment.
4. **Different penalty rates.** Statutory flat rates (Massachusetts at federal rate + 4), or pegged to a different reference (Pennsylvania pegs to AFR + 3 but rounds differently).
5. **PTE election overlay.** 36 states + NYC + DC now have a Pass-Through Entity Tax election. Each has its own estimated-payment schedule for the entity, separate from the owner's individual estimates.

### 3.1 The statutory rule

- **California Revenue and Taxation Code §19136(a)(1)** — imposes an underpayment penalty if the taxpayer fails to pay the required installment by the installment due date. R&TC §19136.1 specifies the installment percentages for individuals.  _(R&TC §19136(a)(1); R&TC §19136.1)_

**California individual installment percentages**  _(R&TC §19136.1)_

| Installment | Due date | % of required annual payment |
| --- | --- | --- |
| **1st** | April 15 | **30 %** |
| **2nd** | June 15 | **40 %** |
| **3rd** | September 15 | **0 %** |
| **4th** | January 15 (following year) | **30 %** |

The September installment is zero. This is the single most-missed quirk in CA estimated tax planning. Taxpayers who use the federal 25/25/25/25 default end the Q1+Q2 cycle having paid 50 % to California when they should have paid **70 %** — and California issues an underpayment penalty on the Q1 + Q2 shortfall computed from those original due dates.

### 3.2 The 110 % high-AGI rule (CA mirrors federal)

- **110% high-AGI prior-year safe harbor** — 110 % of prior-year tax (not 100 %) if California AGI exceeded $150,000 (or $75,000 MFS) in the prior year. California AGI is a different number from federal AGI — Schedule CA (540) adjustments matter.  _(R&TC §19136(c)(2))_

### 3.3 The $1 million income exception (CA-unique)

- **$1 million income exception** — if California AGI exceeded $1,000,000 in the prior year (any filing status except MFS, where it's $500,000), the prior-year safe harbor is unavailable. The taxpayer must use the 90 % current-year safe harbor — meaning the only way to avoid penalty is to estimate 2025 California tax accurately, in real time.  _(R&TC §19136(c)(3))_

### 3.4 Penalty mechanics — Form 5805

- **Form 5805 penalty mechanics** — California uses Form 5805 Underpayment of Estimated Tax by Individuals and Fiduciaries. The penalty rate for 2025 is set by the FTB quarterly and is generally aligned with the federal §6621 rate but published separately. Q4 2025 rate is 7 %.  _(CA Form 5805)_

### 3.5 Corporate side (R&TC §19142 et seq.)

- **California corporate estimated tax schedule** — California corporations follow the federal 25/25/25/25 schedule — the 30/40/0/30 rule is individuals only. But California has its own twist for first-year corporations: a new corporation's first taxable year minimum franchise tax ($800) is waived under R&TC §17941 for LLCs (legislatively extended through 2023, expired for entities formed 2024 onward unless re-extended — verify current legislative status before applying).  _(R&TC §19142 et seq.; R&TC §17941)_

### 3.6 AUDIT FLASH POINT — California 30/40/0/30 missed installments

**The single most common multistate CPA error.** Symptoms:

- Federal estimates paid 25/25/25/25, totaling 100 % of safe harbor by January 15 — clean federally.
- California estimates also paid 25/25/25/25, totaling 100 % of safe harbor by January 15.
- FTB issues a Form 5805 underpayment penalty notice for Q1 + Q2 shortfall (paid 50 %, should have paid 70 %), computed at the daily rate from April 15 to the date paid.

**Remediation in a 2025 plan.** Build the California schedule on a 30/40/0/30 basis from the start. Do not copy the federal vouchers into the CA vouchers. The FTB's Form 540-ES voucher pre-prints the percentages on the back of the form.

### 4.1 The rule (Tax Law §213-b for Article 9-A corporations; §1085 for Article 33)

- **NY Mandatory First Installment** — Corporations subject to the New York State franchise tax (Article 9-A) must pay a Mandatory First Installment by the 15th day of the 3rd month following the close of the prior taxable year — March 15 for calendar-year filers. The MFI is calculated as a percentage of the second preceding year's tax (i.e., for the 2025 MFI, you look at the 2023 return): 25 % if the second preceding year's franchise tax was ≤ $100,000; 40 % if the second preceding year's franchise tax was > $100,000. This is separate from the federal Form 1120-W schedule. The remaining 75 % (or 60 %) is paid on the standard June 15, September 15, December 15 installments via Form CT-400.  _(Tax Law §213-b; Tax Law §1085)_

### 4.2 The $100,000 cliff

- **NY $100,000 cliff** — There is no graduated zone. A corporation with prior-year tax of $99,999 pays an MFI of $24,999.75. A corporation with prior-year tax of $100,001 pays an MFI of $40,000.40 — a $15,400 jump for $2 of additional prior tax. Tax-planning corollary: a corporation that anticipates crossing the threshold should not artificially compress year-end deductions to land at $99,999, because the second preceding year governs (not last year), creating a two-year lag.

### 4.3 NYC parallel rules

- **NYC parallel MFI rules** — New York City General Corporation Tax and Business Corporation Tax have parallel MFI rules under NYC Admin. Code §11-658 — same 25 % / 40 % at the same $100,000 threshold, but applied to the NYC tax (not the NYS tax). A corporation operating in NYC pays two MFIs on March 15: one to NYS, one to NYC.  _(NYC Admin. Code §11-658)_

### 4.4 AUDIT FLASH POINT — NY MFI underpayment at the $100k cliff

If a corporation's second-preceding-year tax was right at $100,000 and the corporation paid 25 % (assuming the lower threshold), but the actual second-preceding-year tax on a later audit-adjusted return was $100,250, the corporation underpaid the MFI by 15 % of the second-preceding-year tax. The penalty under Tax Law §1085(c) is computed at the underpayment rate set quarterly by the Commissioner of Taxation and Finance — Q4 2025 rate 7.5 % — from March 15 to the date paid.

### 5.1 Federal mechanics

- **Annualized Income Installment Method (Form 2210 Schedule AI)** — Q1: YTD through March 31 × 4 = annualized; multiply by tax rate; multiply by 22.5 %. Q2: YTD through May 31 × (12/5) = annualized; multiply by tax rate; multiply by 45 %. Q3: YTD through August 31 × (12/8) = annualized; multiply by tax rate; multiply by 67.5 %. Q4: YTD through December 31 = actual; multiply by tax rate; multiply by 90 %. The cumulative required installment is the lesser of (a) the annualized amount, or (b) the standard 25/25/25/25 cumulative amount. Lower installments early, larger ones late — useful for any taxpayer who realizes most income in Q4.  _(Form 2210 Schedule AI)_

### 5.2 State availability

- **State AIM availability** — Most states with PIT explicitly adopt the annualized income method (by conformity or by parallel statute). California uses Form 5805 Schedule AI, but the periods are different because the 30/40/0/30 installment schedule means the cumulative-percentage targets are 22.5 % / 67.5 % (skip Q3) / 90 %. The Q3 zero-installment makes the CA schedule AI substantially different from federal — preparers must not copy federal numbers. States that do not publish an explicit annualized income method but conform-by-reference to federal (e.g., Massachusetts, via G.L. c.62C §32A) require attaching the federal Schedule AI to the state penalty form. Texas, Florida, and the other no-PIT states have no individual annualized method (no individual estimated tax at all).  _(CA Form 5805 Schedule AI; G.L. c.62C §32A)_

## 6. PTE Election Estimated Payments

- **PTE elective regime overview** — The pass-through entity tax (PTE) elective regime is now in 36 states + NYC + DC as of tax year 2025 (the AICPA state-PTE tracker is the authoritative source). Each PTE election creates an entity-level tax liability that is separate from the owner's individual estimated tax. The owner's individual estimates do not count toward the PTE — and the PTE estimates do not count toward the owner's individual estimates. They are two parallel obligations.  _(AICPA state-PTE tracker)_

### 6.1 Common features

- **Common PTE features** — - The PTE files quarterly estimates (typically on the same federal calendar of 4/15, 6/15, 9/15, 12/15 or 1/15) - The PTE issues a credit certificate (K-1 footnote or state-specific form) to each owner - The owner claims the PTE credit on their individual state return — but the individual still has to pay state estimated tax on non-PTE income through normal channels - California's PTE (R&TC §19900) is the most-cited trap: requires a June 15 payment of the greater of 50 % of last year's PTE tax or $1,000 to validly elect for the year. Miss the June 15 payment by even a day and the election is invalid for that year — there is no late-payment cure. The PTE then files as a normal entity (no entity-level tax, no owner credit), generally a worse outcome than not electing at all.  _(R&TC §19900)_

### 6.2 PTE-only quarterly schedule examples (illustrative)

**PTE-only quarterly schedule examples**

| State | PTE estimate due dates | Notes |
| --- | --- | --- |
| CA | June 15 (prepay), March 15 (final) | June 15 prepay is gate to validity |
| NY | March 15, June 15, September 15, December 15 | 4 equal installments; election due March 15 |
| NJ | April 15, June 15, September 15, January 15 | Mirrors federal individual schedule |
| MA | April 15, June 15, September 15, January 15 | Mirrors federal individual |
| IL | April 15, June 15, September 15, December 15 | Mirrors federal corporate |

See `us-pte-state-matrix.md` for the comprehensive PTE-by-state schedule.

## 7. 50-State + DC Matrix

- **Matrix legend** — **PIT** = Personal Income Tax **Equal** = 25 / 25 / 25 / 25 standard federal-mirrored quarterly installments **AIM** = Annualized Income Method available (Y/N) **PTE** = Pass-Through Entity election with separate entity-level estimates (Y/N) Penalty rate = base annual rate as of late 2025; verify quarterly publication for current period Corporate **MFI** column = mandatory first installment overlay (only NY/NYC use this terminology)

### 7.1 States with NO personal income tax

**States with no personal income tax**

| State | Note |
| --- | --- |
| **AK** | No PIT. Corporate income tax estimated quarterly on federal schedule. |
| **FL** | No PIT. Corporate income tax (5.5 %) estimated quarterly. |
| **NV** | No PIT, no corp income tax. Commerce Tax (gross receipts) on annual schedule. |
| **NH** | No PIT on wages/SE income. Interest & Dividends Tax repealed effective 2025. BPT/BET corporate-level. |
| **SD** | No PIT, no corp income tax. Bank franchise tax only. |
| **TN** | No PIT (Hall income tax repealed 2021). Franchise & Excise Tax estimated quarterly. |
| **TX** | No PIT. Texas Franchise Tax estimated **annually** (no quarterly), Form 05-160 if required. |
| **WA** | No PIT. B&O Tax + new Capital Gains Tax (7 % on long-term gains > $270,000 in 2025) with **quarterly** estimates. |
| **WY** | No PIT, no corp income tax. No estimated tax regime at the state level. |

### 7.2 Full 50-state + DC matrix (states with PIT)

**Full 50-state + DC matrix**

| State | Indiv. due dates | Indiv. safe harbor | Indiv. installment % | Corp. due dates | Corp. safe harbor | Penalty rate (2025) | AIM | PTE | Notable quirks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **AL** | 4/15, 6/15, 9/15, 1/15 | 100 % prior / 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior, 90 % current | Fed AFR + 3 | Y | Y | Form 40ES; conforms heavily to federal |
| **AK** | n/a (no PIT) | — | — | 4/15, 6/15, 9/15, 12/15 | 100 % prior or 90 % current | 11 % | n/a | n/a | Form 6240; corp only |
| **AZ** | 4/15, 6/15, 9/15, 1/15 | 100 % / 110 % at AGI > $150k | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 90 % current / 100 % prior | Statute § 42-1125 | Y | Y | Form 140ES; conforms to federal |
| **AR** | 4/15, 6/15, 9/15, 1/15 | 100 % prior, 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 90 % current | 10 % | Y | Y | Form AR1000ES |
| **CA** | 4/15, 6/15, **none**, 1/15 | 110 % at AGI > $150k; **unavailable at AGI > $1M** | **30 / 40 / 0 / 30** | 4/15, 6/15, 9/15, 12/15 (corp 25/25/25/25) | Greater of $800 min or 100 % prior / 90 % current | FTB-published quarterly (Q4 25 = 7 %) | Y | Y | **R&TC §19136 unique installment schedule;** PTE election validity gated on 6/15 prepay |
| **CO** | 4/15, 6/15, 9/15, 1/15 | 100 % / 110 % at AGI > $150k | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 70 % current | 7 % | Y | Y | Form 104EP; low 70 % corp threshold |
| **CT** | 4/15, 6/15, 9/15, 1/15 | 100 % prior / 90 % current | 25/25/25/25 | 3/15, 6/15, 9/15, 12/15 | 100 % prior or 90 % current | 1 %/month (12 % APR) | Y | Y | Corp Q1 due **March 15**, not April |
| **DE** | 4/30, 6/15, 9/15, 1/15 | 100 % / 110 % at AGI > $150k | 25/25/25/25 (Q1 due 4/30) | 4/15, 6/15, 9/15, 12/15 | 50/20/20/10 split available | 0.5 %/month | Y | Y | Indiv Q1 due **April 30** (not 15) |
| **DC** | 4/15, 6/15, 9/15, 1/15 | 100 % prior / 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior / 90 % current | Fed AFR + 3 | Y | Y | DC Form D-40ES |
| **FL** | n/a (no PIT) | — | — | 5/31, 6/30, 12/31, 3/31 (FY ending June 30) | 80 % current | 12 % | n/a | n/a | Corp due dates **diverge from federal**; 5.5 % rate |
| **GA** | 4/15, 6/15, 9/15, 1/15 | 70 % current OR 100 % prior | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 70 % current | Fed AFR + 3 | Y | Y | Lowest corp current-year threshold (70 %) |
| **HI** | 4/20, 6/20, 9/20, 1/20 | 60 % current OR 100 % prior | 25/25/25/25 | 4/20, 6/20, 9/20, 12/20 | 60 % current | 2/3 of 1 %/month | Y | Y | **Due dates on the 20th**, not 15th |
| **ID** | 4/15, 6/15, 9/15, 1/15 | 80 % current OR 100 % prior | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 80 % current OR 100 % prior | 4 % statutory + 0.5 %/mo | Y | Y | Form 51 |
| **IL** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | Fed AFR + 3 | Y | Y | Flat 4.95 % indiv; flat 7 % corp + 2.5 % replacement |
| **IN** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current; **80 % adj. gross threshold** at high income | 25/25/25/25 | 4/20, 6/20, 9/20, 12/20 | 100 % prior OR 90 % current | Fed AFR | Y | Y | Corp dates on the 20th |
| **IA** | 4/30, 6/30, 9/30, **1/31** | 100 % prior OR 90 % current | 25/25/25/25 | 4/30, 6/30, 9/30, 1/31 | 100 % prior OR 90 % current | 0.4 %/month | Y | Y | **Final installment 1/31**, not 1/15; quarter-ends shifted |
| **KS** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | Fed AFR + 1 | Y | Y | Form K-40ES |
| **KY** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 70 % current (low threshold) | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 70 % current | Tax Comm. published | Y | Y | 70 % current safe harbor |
| **LA** | 4/15, 6/15, 9/15, 1/15 | 90 % current OR 100 % prior | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 90 % current | 0.5 %/month + interest at Sec'y rate | Y | Y | Form IT-540ES |
| **ME** | 4/15, 6/15, 9/15, 1/15 | 100 % / 110 % at AGI > $150k | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 90 % current OR 100 % prior | Fed AFR + 3 | Y | Y | Form 1040ES-ME |
| **MD** | 4/15, 6/15, 9/15, 1/15 | 110 % prior if AGI > $150k | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 90 % current OR 110 % prior | 9.0 % stat. + variable | Y | Y | Includes county tax in estimate |
| **MA** | 4/15, 6/15, 9/15, 1/15 | 80 % current OR 100 % prior | 25/25/25/25 | 3/15, 6/15, 9/15, 12/15 | 100 % prior | Fed rate + 4 | Y | Y | **Corp Q1 due 3/15**, not 4/15 |
| **MI** | 4/15, 6/15, 9/15, 1/15 | 90 % current OR 100 % prior | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 85 % current (lower threshold) | Adj. AFR + 1 | Y | Y | CIT applies only to C corps |
| **MN** | 4/15, 6/15, 9/15, 1/15 | 100 % / 110 % at AGI > $150k | 25/25/25/25 | 3/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | 3 % below market + 5 % | Y | Y | **Corp Q1 due 3/15** |
| **MS** | 4/15, 6/15, 9/15, 1/15 | 80 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 80 % current | 0.5 %/mo + interest | Y | Y | Lower 80 % threshold |
| **MO** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | Director-set; ~ 7 % | Y | Y | Form MO-1040ES |
| **MT** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 80 % current | Fed AFR + 3 | Y | Y | Form ESW |
| **NE** | 4/15, 6/15, 9/15, 1/15 | 100 % / 110 % at AGI > $150k | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | 3 % above prime | Y | Y | Conforms to federal closely |
| **NV** | n/a (no PIT) | — | — | — (no corp income tax) | — | — | n/a | n/a | Commerce Tax annual; MBT for some |
| **NH** | I&D repealed 2025 | n/a | n/a | 4/15, 6/15, 9/15, 12/15 | 25/25/25/25 of BPT/BET | Fed AFR + 2 | n/a | n/a | BPT 7.5 % + BET 0.55 %; entity-level only |
| **NJ** | 4/15, 6/15, 9/15, 1/15 | 80 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 50/25/25/0 (front-loaded) | 3 % above prime | Y | Y | **Corp split front-loaded 50/25/25/0** |
| **NM** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 80 % current OR 100 % prior | Fed AFR | Y | Y | Form PIT-ES |
| **NY** | 4/15, 6/15, 9/15, 1/15 | 100 % / 110 % at NY AGI > $150k | 25/25/25/25 | **3/15 MFI** + 6/15, 9/15, 12/15 | **MFI = 25 % or 40 %** based on second-preceding-year tax | Comm.-published quarterly | Y | Y | **Corp MFI on 3/15;** $100k cliff |
| **NC** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | 5 % flat | Y | Y | Form NC-40 |
| **ND** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | 12 % stat. | Y | Y | Form ND-1ES |
| **OH** | 4/15, 6/15, 9/15, 1/15 | 90 % current OR 100 % prior | 22.5/45/67.5/90 cumulative | n/a (CAT only) | n/a | Statutory + AFR | Y | Y | Commercial Activity Tax replaced corp inc 2010; quarterly CAT |
| **OK** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 70 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 70 % current | Statutory + interest | Y | Y | 70 % current safe harbor |
| **OR** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | 5 % flat plus AFR | Y | Y | CAT (Corporate Activity Tax) separate quarterly schedule |
| **PA** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 3/15, 6/15, 9/15, 12/15 | 30/30/30/10 first-year; 25/25/25/25 thereafter | AFR + 3 | Y | Y | **Corp Q1 due 3/15**; CNIT 8.49 % declining |
| **RI** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 80 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 80 % current | 18 % statutory | Y | Y | Highest statutory penalty rate |
| **SC** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | Fed AFR + 4 | Y | Y | Form SC1040ES |
| **SD** | n/a (no PIT) | — | — | n/a (no corp tax) | — | — | n/a | n/a | Bank franchise only |
| **TN** | n/a (no PIT) | — | — | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current (F&E) | Comm.-published | n/a | n/a | F&E tax estimated quarterly |
| **TX** | n/a (no PIT) | — | — | **Annual** (5/15) | n/a — annual only | 5 % late + 10 % delinquency | n/a | n/a | No quarterly franchise tax estimates |
| **UT** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | Fed AFR + 2 | Y | Y | Form TC-546 |
| **VT** | 4/15, 6/15, 9/15, 1/15 | 100 % / 110 % at AGI > $150k | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | AFR + 2 | Y | Y | Form IN-114 |
| **VA** | **5/1**, 6/15, 9/15, **1/15** | 100 % prior OR 90 % current | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | Fed AFR + 2 | Y | Y | **Indiv Q1 due May 1**, not April 15 |
| **WA** | n/a (no general PIT) | n/a | n/a | n/a (B&O is gross receipts) | n/a | 9 % stat | n/a | n/a | **Capital Gains Tax (7 %) quarterly 4/15, 6/15, 9/15, 1/15** for individuals > $270k LT gains |
| **WV** | 4/15, 6/15, 9/15, 1/15 | 90 % current OR 100 % prior | 25/25/25/25 | 4/15, 6/15, 9/15, 12/15 | 100 % prior OR 90 % current | 9.5 % statutory | Y | Y | Form IT-140ES |
| **WI** | 4/15, 6/15, 9/15, 1/15 | 100 % prior OR 90 % current | 25/25/25/25 | 3/15, 6/15, 9/15, 12/15 | 90 % current OR 100 % prior | 12 % statutory | Y | Y | **Corp Q1 due 3/15** |
| **WY** | n/a (no PIT) | — | — | n/a (no corp inc tax) | — | — | n/a | n/a | No state estimated tax regime |

### 7.3 Key clusters and traps

**Corp Q1 due March 15 (not April 15):** CT, MA, MN, NY, PA, WI. Six states require the first corporate installment one month earlier than federal. Calendar-block these separately.

**Individual Q1 due other than April 15:** DE (4/30), HI (4/20), IA (4/30), VA (5/1). Four states. Most preparers default the Q1 voucher to April 15 and miss these.

**Final installment due other than January 15:** HI (1/20), IA (1/31). Both unusual.

**No prior-year safe harbor at the corporate level:** GA (70 %), KY (70 %), OK (70 %), CO (70 %), MS (80 %), MT (80 %), NJ (80 %), RI (80 %). Current-year accuracy required.

**Highest statutory penalty rates:** RI 18 %, ND 12 %, WI 12 %, FL 12 %, AK 11 %. Underpayment is expensive.

**No quarterly estimates at all:** TX (annual franchise tax only), WY, SD, NV (general corp/personal income).

## 8. Worked Examples

### 8.1 California freelancer with seasonal income

**Facts.** Sole proprietor in Los Angeles, CA. 2024 California tax liability $42,000 on California AGI of $260,000 (above the $150k threshold). 2025 projected income lumpy: $30k Q1, $50k Q2, $20k Q3, $200k Q4 (year-end consulting project). Projected 2025 CA tax ≈ $48,000.

**Federal safe harbor (for reference).** 110 % × prior-year federal tax. Pay 4 × 25 % = 25 % of safe harbor each quarter.

**California safe harbor.** Because 2024 California AGI > $150,000, the prior-year safe harbor is 110 % × $42,000 = $46,200. Lower of $46,200 (110 % prior) or 90 % × $48,000 = $43,200 (90 % current) — required annual payment = $43,200.

**Default (wrong) approach — 25/25/25/25.**

**Federal vs CA installment comparison**

| Q | Due | Required cumulative under federal 25/25/25/25 | Required cumulative under CA 30/40/0/30 | Shortfall |
| --- | --- | --- | --- | --- |
| Q1 | 4/15 | $10,800 (25 %) | **$12,960 (30 %)** | $2,160 |
| Q2 | 6/15 | $21,600 (50 %) | **$30,240 (70 %)** | $8,640 |
| Q3 | 9/15 | $32,400 (75 %) | $30,240 (70 %) | overpaid (not penalized) |
| Q4 | 1/15 | $43,200 (100 %) | $43,200 (100 %) | $0 |

The 25/25/25/25 approach generates a Q1 + Q2 cumulative shortfall of $8,640 from June 15 through whenever it's caught up. At the FTB's 7 % rate, the penalty for a 3-month delay (caught up at Q3) is approximately $151 — small, but the FTB sends a notice that takes professional time to respond to.

**Annualized income method alternative.** The Q3 zero-installment in CA's schedule already accommodates seasonal income better than federal. But CA's Form 5805 Schedule AI lets the freelancer annualize: Q1 cumulative income $30k → annualized $120k → CA tax ≈ $7,800 → 22.5 % × $7,800 = $1,755 Q1. Substantially lower than $12,960. This works only if the freelancer commits to the AIM for all four installments — can't switch between regular and AIM mid-year. The Q4 catch-up after the big project will be large but penalty-free.

**Recommendation.** Use CA AIM Schedule. Pay $1,755 by 4/15, recalculate at each due date.

### 8.2 New York corporation crossing the MFI threshold

**Facts.** Calendar-year C corp. Article 9-A franchise tax for tax year 2023 was $98,000. Tax year 2024 was $145,000. Tax year 2025 projected at $160,000.

**2025 MFI calculation.** Use second preceding year = 2023. 2023 tax was $98,000, which is ≤ $100,000. MFI = 25 % × $98,000 = $24,500, due March 15, 2025.

**Remaining 2025 installments.** Required total = $160,000 (current-year). Required remaining after MFI = $160,000 − $24,500 = $135,500, paid as $45,167 per installment on 6/15, 9/15, 12/15.

**The trap.** A preparer who looks only at 2024 tax ($145,000, above $100k) and computes MFI as 40 % × $145,000 = $58,000 overpays, locking up $33,500 in unnecessary state estimated payments. Conversely, a preparer who uses the current-year projection ($160,000) and 40 % gets $64,000 — even more wrong.

**Year-after-next trap.** For tax year 2026, the second-preceding year is 2024 = $145,000 — now over $100k. So 2026 MFI = 40 % × $145,000 = $58,000, due 3/15/2026. The corporation should plan March cash flow accordingly. The two-year lag means a one-year revenue spike pushes the MFI rate up two years later.

### 8.3 Multistate partnership making PTE election in CA, NY, and NJ

**Facts.** Three-partner consulting LLP. Calendar-year 2025. Allocated income: 50 % CA-source, 30 % NY-source, 20 % NJ-source. Partners are individuals resident in California. Each state allows PTE election. Total projected partnership net income $1,200,000.

**Apportioned PTE liabilities (illustrative)**

| State | Apportioned income | Approximate PTE rate (2025) | PTE tax | Critical estimate dates |
| --- | --- | --- | --- | --- |
| CA | $600,000 | 9.3 % | $55,800 | **6/15/25 prepay** $27,900 (50 %) → election gate; balance 3/15/26 |
| NY | $360,000 | 6.85 % (graduated) | ≈ $25,800 | 3/15, 6/15, 9/15, 12/15 → 4 equal of $6,450 |
| NJ | $240,000 | 5.675 % (sliding) | ≈ $13,600 | 4/15, 6/15, 9/15, 1/16 → 4 equal of $3,400 |

**Critical dependencies.**

- The June 15, 2025 California PTE prepayment of $27,900 is the gate to the entire CA election. Miss by one day and the LLP cannot make the CA PTE election for 2025. The partners then lose the federal-deduction SALT-cap workaround for $55,800 of CA tax. Federal cost ≈ 37 % × $55,800 = $20,646 in lost federal deduction value.
- The NY 3/15/2025 first installment of $6,450 must be paid by the partnership separately from any individual estimate. The individual partners' CA Form 540-ES vouchers do not satisfy the NY entity-level estimate.
- Individual partners still owe California Form 540-ES estimates on non-PTE income (e.g., spouse W-2, investment income). The PTE credit on the 2025 California return offsets the PTE-source tax only; everything else needs to be on the 30/40/0/30 individual schedule.

**Calendar action items**

| Date | Action |
| --- | --- |
| 3/15/25 | NY PTE Q1 ($6,450); NY corp MFI if any (separate entity) |
| 4/15/25 | NJ PTE Q1 ($3,400); individual federal & CA Q1 |
| **6/15/25** | **CA PTE prepayment ($27,900)** — gates election; individual federal & CA Q2 |
| 6/15/25 | NY PTE Q2; NJ PTE Q2 |
| 9/15/25 | NY PTE Q3; NJ PTE Q3; individual federal Q3 (CA individual Q3 = $0 — do not pay) |
| 12/15/25 | NY PTE Q4 |
| 1/15/26 | Individual federal Q4 & CA Q4; NJ PTE Q4 |
| 3/15/26 | CA PTE final ($27,900); NY entity tax return; partnership return federally |

## 9. Audit Flash Points (consolidated)

1. **CA 30/40/0/30 missed installments.** Preparer defaults to 25/25/25/25 for CA, generating a Q1 + Q2 cumulative shortfall and an FTB Form 5805 penalty notice. Always build CA on the unique installment schedule from scratch.
2. **NY MFI underpayment at the $100k cliff.** Corporation with second-preceding-year tax of $98,000–$102,000 — the 25 %/40 % distinction creates large nominal swings on the March 15 payment. Verify the second-preceding-year tax from the filed return as adjusted, not the original return.
3. **Multistate freelancers using federal safe harbor without state coverage.** Paying 110 % of prior federal tax is irrelevant to most state safe harbors. Each state safe harbor is computed on that state's prior-year tax (allocated to that state). A California-resident consultant who moves Q3 to New York for the year owes individual estimates to both states for the year of the move.
4. **CA $1 million income exception.** If prior-year CA AGI > $1,000,000, the prior-year safe harbor is unavailable. Must use 90 % current-year. Common error: rolling forward 110 % prior calculation without checking the $1M threshold.
5. **CA PTE June 15 prepayment.** Missing by even one day invalidates the election for the entire year. No late-payment cure. Set a calendar alert at 5/15 and 6/1.
6. **Iowa late final installment (1/31).** Iowa individual Q4 is January 31, not January 15. Federally-aligned preparers underpay Iowa Q4 from 1/15 to 1/31 with zero consequence (Iowa expects nothing until 1/31), but more importantly, an Iowa taxpayer who pays the federal Q4 on 1/15 to IA expecting to satisfy both gets it backwards — federal isn't satisfied, Iowa is.
7. **Corporate Q1 March 15 states.** CT, MA, MN, NY, PA, WI. Missing the March 15 payment and paying on April 15 with federal generates one month of underpayment penalty.
8. **PTE-vs-individual double-payment risk.** Partners sometimes pay individual estimates AND PTE estimates assuming one will absorb the other. They don't — the partners then claim a PTE credit on the return and end up with a large refund. Not penalized, but cash-flow distortive.
9. **Texas franchise tax annual-only.** No Texas quarterly estimates exist. Preparers from quarterly-states may inadvertently set up phantom quarterly vouchers.
10. **NH I&D Tax repealed 2025.** Estimated payments for the New Hampshire Interest & Dividends Tax should have ceased after the 2024 final installment. Continued payments will be refunded but generate an FTB notice.

### 10.1 Primary federal sources

- IRC §6654 — Failure by individual to pay estimated income tax (the federal individual safe-harbor statute)
- IRC §6654(d)(2) — Annualized income installment method
- IRC §6655 — Failure by corporation to pay estimated income tax (the federal corporate safe-harbor statute)
- IRC §6655(e) — Corporate annualized income method
- IRS Form 1040-ES (2025); Form 2210 (2025); Form 2210 Schedule AI (2025)
- IRS Form 1120-W (2025); Form 2220 (2025)
- IRS Rev. Rul. 2025-XX — quarterly underpayment rate publications (current Q4 2025 rate: 7 %)

### 10.2 Key state primary sources (sample — not exhaustive)

- **California:** R&TC §19136 (individual installments), §19136.1 (30/40/0/30 percentages), §19142 (corporate), §19900 (PTE election). FTB Form 540-ES; Form 5805; Form 5805 Schedule AI; Form 100-ES.
- **New York:** Tax Law §213-b (Article 9-A MFI); Tax Law §1085 (penalty); Tax Law §1085(c). NYS DTF Form CT-300 (MFI form); Form CT-400; Form IT-2105.
- **New Jersey:** N.J.S.A. 54A:8-6 (individual estimated tax); N.J.S.A. 54:10A-15 (corporation). NJ Form NJ-1040-ES; Form CBT-150.
- **Massachusetts:** G.L. c.62C §32A; G.L. c.63 §29A. MA Form 1-ES; Form 355-ES.
- **Illinois:** 35 ILCS 5/803 (individual); 35 ILCS 5/804 (corporate). IL Form IL-1040-ES; Form IL-1120-ES.

### 10.3 Secondary references

- AICPA State PTE Tax Implementation Map (current 2025 release)
- CCH State Tax Reporter — Estimated Tax (state-by-state)
- BNA / Bloomberg Tax — Multistate Quick Answers Chart (Estimated Tax)
- Each state revenue department's instructions for its current-year individual and corporate estimated-tax forms (verify due dates and penalty rates against the published form for the year of preparation; some states adjust rates each January and July)

### 10.4 Last verified

This matrix was compiled with information current through November 15, 2025. Penalty rates published by each state on a quarterly schedule must be re-verified at the time of computing any penalty. Safe-harbor percentages and installment shares are stable across the year. PTE election rules are evolving rapidly — verify the AICPA tracker before recommending a PTE election to a client.

## END — us-state-estimated-tax-safe-harbors-matrix v0.1

END — us-state-estimated-tax-safe-harbors-matrix v0.1

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
