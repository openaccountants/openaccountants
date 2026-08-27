---
name: yt-tax-credits
description: Use this skill for Yukon provincial tax credits — Yukon First Nations Tax Credit, Yukon Small Business Investment Tax Credit (25%), Yukon Research and Development Tax Credit (15%), Yukon Manufacturing and Processing Profits Tax Credit, Yukon Mineral Exploration Tax Credit (25%). Triggers "Yukon tax credits", "Yukon First Nations Tax Credit", "Form YT428", "Yukon SBITC", "Yukon mineral exploration".
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# YT Tax Credits

## Yukon — Provincial Tax Credits & Incentives — Skill v1.0

This skill covers the Yukon-specific personal and corporate tax credits administered alongside the federal T1/T2 return for the 2025 tax year. Yukon is the smallest sub-national jurisdiction in Canada by population but has one of the most distinctive tax credit regimes — notably the **Yukon First Nations Tax Credit (FNTC)**, which has no parallel in any other province or territory, and a **0% provincial small business CIT rate**, the most generous in Canada.

Yukon's personal income tax is administered by the Canada Revenue Agency (CRA) under a tax collection agreement, but the credit parameters, definitions, and unique-to-Yukon credits are set by the Yukon Department of Finance under the *Yukon Income Tax Act* (RSY 2002, c. 118).

## 1. Quick reference — personal + corporate credit summary

### Personal (Form YT428 / YT479 series)

**Personal (Form YT428 / YT479 series)**  _(See table)_

| Credit | Type | 2025 rate / amount | Anchor |
| --- | --- | --- | --- |
| Yukon First Nations Tax Credit (FNTC) | Non-refundable; reduces YT tax payable | Up to **95%** of federal abatement equivalent for Yukon First Nation citizens on Settlement Land | *Yukon Income Tax Act* s. 21 |
| Yukon Small Business Investment Tax Credit (SBITC) | Non-refundable | **25%** of eligible investment; cap **$25,000 credit/year** per investor | YITA Part 2, Div. 2 |
| Yukon Children's Fitness Tax Credit | Refundable | Lesser of expenses or **$1,000 per child under 16** | YT479 line 63800 |
| Yukon Mineral Exploration Tax Credit (YMETC) | Non-refundable | **25%** of eligible YT-source grassroots mineral exploration | YITA Part 2 |
| Yukon political contribution tax credit | Non-refundable | Sliding (max $650) | Standard YT428 |
| Yukon Carbon Price Rebate — Individuals (YGCR) | Refundable | Quarterly fixed amount | YGCR program |

### Corporate (T2 + YT Schedule 443/440)

**Corporate (T2 + YT Schedule 443/440)**  _(See table)_

| Credit | Type | 2025 rate | Anchor |
| --- | --- | --- | --- |
| Yukon general CIT rate | Statutory | **12%** | YITA s. 17 |
| Yukon small business deduction (active income ≤ $500k) | Statutory | **0%** (combined federal-only **9%**) | YITA s. 17 |
| Yukon M&P Profits Tax Credit | Statutory rate reduction | Reduces general 12% to **2.5%** on M&P profits | YITA s. 17.1 |
| Yukon R&D Tax Credit | Refundable | **15%** general; **20%** if paid to YT university/college | YITA Part 2 |
| Yukon Mineral Exploration Tax Credit (corporate) | Non-refundable | **25%** | YITA Part 2 |
| First Nations corporate income tax abatement | Statutory reduction | Up to **95%** abatement for qualifying entities | YITA + Self-Government Agreement |

## 2. Required inputs + refusal catalogue

### Required inputs

- Taxpayer residency status on **December 31, 2025** (full-year YT resident vs. part-year)
- For First Nations Tax Credit: First Nation citizenship, Settlement Land status, Self-Government Agreement reference
- T1 federal return draft (line 26000 taxable income, line 40427 federal tax)
- For corporate: T2 jacket, Schedule 5 (provincial allocation), Schedule 443 (Yukon credits), Schedule 440
- Eligible investment / R&D / mineral exploration substantiation
- Receipts for refundable personal credits (fitness, etc.)

### Refusal catalogue (out of scope for this skill)

- **R-YT-1** — Non-resident of Yukon on Dec 31 — provincial credits do not apply; refer to province of residence  _(R-YT-1)_
- **R-YT-2** — Federal credit substitution — this skill does not duplicate federal SR&ED, ITC, or CMETC computations  _(R-YT-2)_
- **R-YT-3** — First Nations Self-Government tax sharing disputes — refer to the relevant Self-Government Financial Transfer Agreement; do not compute  _(R-YT-3)_
- **R-YT-4** — Trust returns (T3) claiming YT credits — out of scope  _(R-YT-4)_
- **R-YT-5** — Corporate associated-group SBD allocation — defer to a corporate tax skill  _(R-YT-5)_
- **R-YT-6** — Partial-year YT residency with mid-year FN status change — refer to credentialed reviewer  _(R-YT-6)_

## 3. Yukon First Nations Tax Credit (FNTC) — unique to Yukon

The FNTC is the single most distinctive feature of the Yukon personal and corporate tax system. **No other Canadian jurisdiction operates a credit of this design.** It implements the tax-sharing provisions of the Yukon Self-Government Agreements signed between Canada, Yukon, and the 11 self-governing Yukon First Nations.

### Mechanism

- **FNTC mechanism** — For an individual who is a citizen of a self-governing Yukon First Nation and whose income is attributable to a Settlement Land under a Final Agreement, the FNTC reduces Yukon personal income tax payable by an amount equivalent to up to 95% of the federal abatement that would otherwise be remitted to the First Nation government under the Personal Income Tax Administration Agreement. For practical computation: 1. Compute Yukon tax payable on Form YT428 as if no FNTC applied. 2. Determine the attributable portion of taxable income (income earned on Settlement Land or otherwise attributable under the Final Agreement). 3. Multiply by the Yukon effective rate. 4. Apply the up to 95% abatement factor — the residual 5% remains with the Yukon government. 5. Claim the FNTC on the designated YT428 line.  _(Yukon Income Tax Act s. 21)_

### Corporate FNTC

- **Corporate FNTC** — A corporation whose income is attributable to a Yukon First Nation Settlement Land and which is owned by, or controlled by, a self-governing Yukon First Nation, may claim a parallel corporate FNTC reducing Yukon CIT payable by up to 95% of the attributable portion.  _(YITA + Self-Government Agreement)_

### Key references

- *Yukon Income Tax Act* s. 21 (individuals), s. 17 (corporations) — as amended through 2025
- Personal Income Tax Administration Agreement between Canada, Yukon, and each self-governing Yukon First Nation
- Final Agreements and Self-Government Agreements of the 11 self-governing Yukon First Nations

**Refer all FNTC computations to a credentialed reviewer.** The interaction with the federal abatement, the attribution rules, and the specific terms of each First Nation's Self-Government Agreement make this an area where the conservative default is **always refer**, never auto-compute.

## 4. Yukon Small Business Investment Tax Credit (SBITC)

The Yukon SBITC encourages investment in eligible Yukon-based small businesses by individual Yukon-resident investors.

### Parameters (2025)

- **SBITC rate** — 25% percent (of qualifying investment)  _(YITA Part 2, Div. 2)_
- **Annual cap per investor** — $25,000 credit (i.e., $100,000 of qualifying investment)  _(YITA Part 2, Div. 2)_
- **SBITC type** — Non-refundable (carryforward 7 years, carryback 3 years)  _(YITA Part 2, Div. 2)_
- **Eligible investment** — Equity in an eligible Yukon small business corporation registered with the Yukon Department of Economic Development; certificate issued  _(YITA Part 2, Div. 2)_
- **Eligible investor** — Yukon resident individual at the time of investment  _(YITA Part 2, Div. 2)_

### Workflow

- **SBITC workflow** — 1. Investor receives a Yukon SBITC certificate from the Department of Economic Development. 2. Certificate number and credit amount entered on Form YT479. 3. Credit applied against Yukon tax payable on Form YT428 (after the FNTC and most other non-refundables). 4. Unused balance carried forward / back as above.  _(YITA Part 2, Div. 2)_

## 5. Yukon Research and Development Tax Credit

A refundable credit available to both individuals and corporations carrying on Scientific Research and Experimental Development (SR&ED) work in Yukon, **in addition to** the federal SR&ED ITC.

### Parameters (2025)

- **General rate** — 15% percent (of eligible Yukon SR&ED expenditures)  _(YITA Part 2)_
- **Enhanced rate** — 20% percent (on the portion of expenditures paid to a Yukon university or college)  _(YITA Part 2)_
- **Type** — Refundable (paid out even if no tax owing)  _(YITA Part 2)_
- **Coordination** — Computed on Yukon-source portion; federal SR&ED ITC is computed separately on Schedule T661 + Schedule 31  _(YITA Part 2)_

### Workflow

- **R&D credit workflow** — 1. Complete federal Form T661 (SR&ED claim) and Schedule 31 first. 2. Identify the Yukon-source portion of eligible expenditures. 3. Apply the 15% / 20% rate. 4. Claim the refundable credit on the corporate T2 (Schedule 443) or individual YT479.  _(YITA Part 2)_

## 6. Yukon Manufacturing and Processing Profits Tax Credit

This is a **statutory rate reduction**, not a discrete credit line. Under YITA s. 17.1, M&P profits earned in Yukon are taxed at **2.5%** rather than the general 12%, mirroring the federal M&P rate reduction.

- Applies to **non-CCPC** income and to CCPC income above the $500,000 SBD limit when classified as M&P profit
- M&P determination follows the federal rules: Schedule 27 (Calculation of Canadian Manufacturing and Processing Profits Deduction)
- Reported on T2 Schedule 5 (provincial tax) with M&P portion identified
- Combined federal-Yukon rate on M&P profit: 15% federal + 2.5% Yukon = **17.5%**

- **M&P Yukon rate reduction** — 2.5% percent (reduces general 12% rate on M&P profits)  _(YITA s. 17.1)_

## 7. Yukon Mineral Exploration Tax Credit (YMETC)

Mining is the single largest private-sector industry in Yukon. The YMETC supports **grassroots** mineral exploration on Yukon-staked claims.

### Parameters (2025)

- **YMETC rate** — 25% percent (of eligible Yukon-source grassroots mineral exploration expenses (i.e., pre-feasibility, surface exploration))  _(YITA Part 2)_
- **Type** — Non-refundable for both individuals and corporations; carryforward 10 years  _(YITA Part 2)_
- **Eligible expenditures** — Defined by reference to the federal Canadian Exploration Expense (CEE) under ITA s. 66.1, but restricted to grassroots-stage Yukon-source amounts  _(ITA s. 66.1)_
- **Coordination** — In addition to the federal Critical Mineral Exploration Tax Credit (CMETC) at 30% where applicable, and the federal Mineral Exploration Tax Credit (METC) at 15% otherwise  _(YITA Part 2)_

### Flow-through share interaction

- **Flow-through share interaction** — The YMETC is typically claimed by an investor receiving a flow-through share renunciation of eligible CEE from a Yukon junior mining company. Reported on: - Individual: Form T1229 (federal flow-through) + Form YT479 line for YMETC - Corporate: Schedule 443  _(YITA Part 2)_

## 8. Yukon Children's Fitness Tax Credit

A refundable provincial credit (Yukon retained this credit after the federal version was eliminated in 2017).

- **Maximum eligible expense** — $1,000 per child under 16 (under 18 if eligible for disability tax credit)  _(Form YT479)_
- **Refundable rate** — 6.4% percent (Yukon lowest tax bracket rate for 2025)  _(Form YT479)_
- **Maximum refundable credit** — $1,000 × 6.4% = $64 per child; plus a $500 supplement for children eligible for the disability tax credit (total expense allowance)  _(Form YT479)_
- **Claim location** — Claimed on Form YT479  _(Form YT479)_

## 9. Yukon Corporate Tax — 12% / 0% structure

Yukon operates **the most generous CIT rate structure in Canada** for small CCPCs.

### 2025 rates

**2025 rates**  _(Yukon Department of Finance)_

| Income type | Federal | Yukon | Combined |
| --- | --- | --- | --- |
| Small business income (CCPC, ≤ $500k active) | 9% | **0%** | **9%** |
| General active business income | 15% | 12% | 27% |
| M&P profits | 15% | 2.5% | 17.5% |
| Investment income (CCPC) | 38.67% (incl. refundable Part I) | 12% | up to 50.67% before RDTOH |

### Key implications

- A Yukon CCPC with $500,000 of active business income pays only **$45,000 in combined CIT** ($500,000 × 9%), compared to e.g. $63,500 in Ontario (12.2% combined) or $50,000 in BC (10%).
- The 0% rate is conditioned on standard SBD requirements: CCPC status, active business income, associated-group $500k limit, passive-income grind under ITA s. 125(5.1) where applicable.

## 10. Form YT428 — personal credit form

Form YT428 (Yukon Tax) and its companion Form YT479 (Yukon Credits) are filed as part of the T1 General. Key lines for 2025:

**Form lines table**  _(CRA Form YT428 / YT479 (2025 tax year))_

| Form | Line | Credit |
| --- | --- | --- |
| YT428 | 58040–58400 | Basic personal amount, age, spouse, eligible dependant, etc. (mirror federal where harmonized) |
| YT428 | (FNTC line) | Yukon First Nations Tax Credit |
| YT428 | (Political contribution) | Political contribution credit |
| YT479 | 63855 | Yukon Children's Fitness Credit (refundable) |
| YT479 | (SBITC line) | Small Business Investment Tax Credit |
| YT479 | (YMETC line) | Mineral Exploration Tax Credit |
| YT479 | (R&D line) | Yukon R&D Tax Credit (refundable, individual) |

## 10. Form YT428 — personal credit form

Yukon harmonizes most personal non-refundable credit definitions with the federal T1 schedule, including the basic personal amount mechanism — but applies them at **Yukon rates** (lowest bracket 6.4%, top bracket 15% for 2025).

## 11. Worked example — Yukon CCPC, Whitehorse, $400k active income

**Facts.** Whitehorse Tech Ltd. is a Yukon-incorporated CCPC, 100% owned by a Yukon-resident individual. 2025 calendar year. Active business income $400,000. No associated corporations. No passive income grind. Not engaged in M&P.

**Step 1 — Federal tax.**
- Federal general rate: 15%
- Federal SBD: 19% rate reduction on first $500k → effective 9%
- $400,000 × 9% = **$36,000 federal Part I tax**

**Step 2 — Yukon tax.**
- Yukon small business rate on active income ≤ $500k: **0%**
- $400,000 × 0% = **$0 Yukon CIT**

**Step 3 — Combined.**
- Total CIT: **$36,000** on $400,000 of active business income
- Combined effective rate: **9.00%**

**Step 4 — Comparison.**
- Same facts in Ontario: $400,000 × 12.2% combined = $48,800 (Yukon saves $12,800)
- Same facts in BC: $400,000 × 11.0% combined = $44,000 (Yukon saves $8,000)
- Same facts in Saskatchewan (1% SB rate): $400,000 × 10% combined = $40,000 (Yukon saves $4,000)

**Reviewer note.** The 0% Yukon SBD rate is a powerful incentive for genuine Yukon-resident operating businesses. It does **not** by itself justify a Yukon incorporation for a business operated elsewhere — the corporation must have a permanent establishment in Yukon under federal Reg. 400, and provincial allocation under Schedule 5 applies. Sham residency / mailbox PE schemes will be reassessed.

## 12. Conservative defaults

- **Conservative defaults** — - Default the FNTC to 'refer to reviewer' — never auto-compute without the citizenship determination, Settlement Land attribution, and confirmation of which Self-Government Agreement applies. - Default SBITC to uncertified until the Yukon Department of Economic Development certificate number is in hand. - Default YMETC eligibility to grassroots only — if the work is past pre-feasibility, refuse and refer. - Default R&D credit Yukon-source allocation to the conservative attribution (lesser of T661 expenditures and Yukon-PE expenditures). - Default provincial allocation (Schedule 5) to the federal Reg. 400 result — do not optimize. - If the taxpayer was a YT resident for less than the full year, refuse and refer.

## 13. Sources

- *Yukon Income Tax Act*, RSY 2002, c. 118 (as amended through 2025), Yukon Department of Justice consolidated text
- Yukon Department of Finance, *Tax Credits and Incentives* policy bulletins (2024 and 2025 editions)
- Canada Revenue Agency, *Form YT428 — Yukon Tax* (2025 tax year)
- Canada Revenue Agency, *Form YT479 — Yukon Credits* (2025 tax year)
- Canada Revenue Agency, *T2 Corporation Income Tax Guide*, provincial and territorial tax — Yukon section
- Yukon Self-Government Agreements (11 self-governing First Nations) and the related Personal Income Tax Administration Agreements
- Federal *Income Tax Act* (Canada), RSC 1985, c. 1 (5th Supp.), ss. 66.1, 125, 125.1 — as cross-referenced by YITA
- Yukon Department of Economic Development — Small Business Investment Tax Credit Program guidelines (2025)

## End of skill marker

*End of skill — Yukon Provincial Tax Credits & Incentives v1.0.*

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
