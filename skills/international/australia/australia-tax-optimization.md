---
name: australia-tax-optimization
description: Use this skill when advising on LEGAL tax minimization strategies for Australian taxpayers — individuals, sole traders, and small business owners. Trigger on phrases like "reduce my tax", "tax planning Australia", "salary vs dividends", "negative gearing", "instant asset write-off", "superannuation strategy", "CGT discount", "trust distribution", "income splitting", "GAAR", "Part IVA", or any question about structuring affairs to legally minimize Australian tax. Covers entity selection, deduction optimization, capital allowances, loss utilization, timing strategies, GST planning, superannuation, and red lines. ALWAYS read this skill before giving Australian tax optimization advice.
version: 1.1
jurisdiction: AU
tax_year: 2025
tax_year_notes: "2025-26; includes 1 July 2026/2027 reform alerts (Tax Reform No. 1 Act 2026)"
last_updated: 2026-08-20
review_status: pending_review
depends_on: - bookkeeping-workflow-base
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Tax Optimization

> **Law-change alert (Tax Reform No. 1 Act 2026 — passed June 2026, applies from 1 July 2027).** Three strategies in this skill change fundamentally from 1 July 2027: (1) the **50% CGT discount** for individuals/trusts/partnerships is replaced by cost-base indexation + a 30% minimum rate on gains accruing from 1 July 2027 (assets deemed re-acquired 1 July 2027; new residential dwellings keep the discount); (2) **negative gearing** on residential property is limited to new builds — properties acquired on or before Budget night 12 May 2026 are grandfathered, later non-new-build acquisitions have losses quarantined from 1 July 2027; (3) from 1 July 2026 a **$1,000 standard deduction** for work-related expenses applies to labour income (excluding PSI), and from 2027-28 a $250 **Working Australians Tax Offset**. Timing advice that straddles 30 June 2027 must model both regimes — escalate.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD |
| Tax year | 1 July – 30 June (2025–26) |
| Primary legislation | Income Tax Assessment Act 1997 (ITAA 1997); Income Tax Assessment Act 1936 (ITAA 1936) |
| Anti-avoidance | Part IVA, ITAA 1936 (General Anti-Avoidance Rule) |
| Tax authority | Australian Taxation Office (ATO) |
| Filing deadline | 31 October (self-lodgers); agent-lodged extensions vary |
| Individual top rate | 45% + 2% Medicare levy = 47% effective |
| Company rate (base rate entity) | 25% (aggregated turnover < $50m, ≤80% passive income) |
| Company rate (other) | 30% |
| CGT discount (individuals) | 50% on assets held >12 months |
| GST rate | 10% |
| Superannuation guarantee | 12% (2025–26) |

### Individual Tax Brackets (2025–26)

**Individual Tax Brackets (2025–26)**

| Taxable Income (AUD) | Rate | Cumulative Tax |
| --- | --- | --- |
| 0 – 18,200 | 0% | $0 |
| 18,201 – 45,000 | 16% | $4,288 |
| 45,001 – 135,000 | 30% | $31,288 |
| 135,001 – 190,000 | 37% | $51,638 |
| 190,001+ | 45% | — |

Plus 2% Medicare levy on total taxable income. Medicare levy surcharge (1%–1.5%) applies if no private hospital cover and income exceeds $101,000 (single).

## Section 2 — Income Splitting & Structuring

### Sole Trader vs Company

- **Sole trader taxation** — all profit taxed at individual marginal rates (up to 47%). Simple structure, ABN-based. Losses offset other personal income (subject to non-commercial loss rules, s 35-10 ITAA 1997). No separate return.  _(s 35-10 ITAA 1997)_
- **Company (Pty Ltd) taxation** — profits taxed at 25% (base rate entity) or 30%. Profits retained in the company are not taxed again until distributed. Franking credits attached to dividends prevent double taxation. Division 7A (ITAA 1936, ss 109C–109T) treats loans and payments to shareholders/associates as unfranked dividends unless complying loan agreements are in place.  _(Division 7A, ITAA 1936, ss 109C–109T)_
- **Rule of thumb — incorporation threshold** — incorporation typically benefits when taxable profit consistently exceeds ~$100,000, allowing retention at 25% vs 47% marginal. Below $45,000 profit, sole trader is usually superior (16% marginal vs 25% corporate + extraction costs).

### Salary vs Dividends (Company Directors)

- **Salary** — deductible to the company, taxed to the individual, triggers PAYG withholding and super guarantee (12%). Generates assessable income for super contribution purposes.
- **Franked dividends** — not deductible to the company, carry franking credits. Grossed-up amount included in individual return, franking credit offset applied. No super guarantee obligation.
- **Optimal mix** — pay enough salary to cover super guarantee obligations and utilise the tax-free threshold ($18,200); distribute remaining as franked dividends. Model the combined company + personal tax.

### Family Trusts

Discretionary (family) trusts allow income distribution to adult family members in lower brackets. The trustee resolution must be made before 30 June. Key constraints:

- **Section 100A reimbursement agreements** — trust distributions to low-income beneficiaries who redirect funds back to the primary earner are void.  _(Section 100A (ITAA 1936))_
- **Family Trust Election (FTE)** — required to access franking credits and carry forward losses.
- **Minor beneficiaries penalty rates** — Minor beneficiaries (under 18) taxed at penalty rates on unearned income (Division 6AA) — effectively 66% on amounts above $416.  _(Division 6AA)_

### Superannuation as Income Splitting

- **Spouse contributions** — up to $3,000 contribution to a low-income spouse's super fund → tax offset of up to $540 (18% of $3,000). Spouse must earn <$40,000.
- **Contribution splitting** — up to 85% of concessional contributions from the prior year can be rolled to a spouse's super account (not a deduction, but shifts wealth tax-efficiently).

## Section 3 — Deductions Most People Miss

**Deductions Most People Miss**

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Home office running expenses | s 8-1 ITAA 1997 | Fixed rate 70c/hour (PCG 2023/1, from 1 July 2024; was 67c 2022-24) or actual cost. Must keep contemporaneous records (timesheets, diary) |
| Self-education expenses | s 8-1 | Must have sufficient connection to current employment/business. First $250 non-deductible for employees (not self-employed) |
| Phone and internet | s 8-1 | Apportion business use %. ATO accepts a representative 4-week diary |
| Income protection insurance | s 8-1 | Premiums for policies replacing lost income are deductible |
| Professional memberships and subscriptions | s 8-1 | CPA Australia, CA ANZ, industry bodies |
| Tax agent fees | s 25-5 | Cost of managing tax affairs including prior-year amendments |
| Union fees | s 8-1 | Full deduction |
| Tools and equipment (≤$300) | s 8-1 | Immediately deductible if cost ≤$300 and used for income |
| Travel between workplaces | s 8-1 | Deductible (but NOT home-to-work commuting) |
| Donations to DGRs | Div 30 | Deductible gifts to Deductible Gift Recipients |
| Prepaid expenses ≤12 months | s 82KZM ITAA 1936 | Non-business individuals can prepay deductible expenses before 30 June for immediate deduction |

## Section 4 — Capital Allowances Optimization

### Instant Asset Write-Off (2025–26)

- **Instant asset write-off eligibility** — Small businesses (aggregated turnover <$10m) can immediately deduct assets costing less than $20,000 (per asset). The $20,000 limit is law for 2024-25 and 2025-26 (Treasury Laws Amendment (Strengthening Financial Systems and Other Measures) Act 2025) and the 2026-27 Budget announced it becomes permanent from 1 July 2026 — confirm enactment before relying on it for 2026-27.  _(ITAA 1997 Div 328; ATO QC 103578)_
- **Simplified depreciation pool** — Assets ≥$20,000 enter the small business simplified depreciation pool: 15% first year, 30% declining balance thereafter. Pool balance <$20,000 at 30 June 2026 can be written off entirely.

### General Depreciation

**General Depreciation Methods**

| Method | How It Works |
| --- | --- |
| Diminishing value | Base value × (days held / 365) × (200% / effective life) |
| Prime cost (straight-line) | Cost × (days held / 365) × (100% / effective life) |

- **Effective life determination** — Effective life determined by ATO schedule (TR 2024/3) or taxpayer's own reasonable estimate. Self-assessed life must be supportable if audited.  _(TR 2024/3)_

### Motor Vehicles

- **Car cost limit for depreciation** — 2025–26: $69,674; 2026–27: $69,883 AUD (only the business-use portion of this amount can be depreciated)
- **Business-use substantiation** — Business-use percentage must be substantiated via logbook (minimum continuous 12-week period, valid for 5 years) or cents-per-km method (88c/km in 2025-26; 91c/km in 2026-27; max 5,000 business km).

## Section 5 — Loss Utilization

### Individual/Sole Trader Losses

- **Loss carry forward** — Tax losses carry forward indefinitely (s 36-15 ITAA 1997). No carry-back for individuals.  _(s 36-15 ITAA 1997)_
- **Non-commercial loss rules (Division 35) — four tests** — business losses can only offset non-business income if one of four tests is met: 1. Assessable income ≥$20,000 from the activity; 2. Profit in 3 of the last 5 years (including current year); 3. Real property used ≥$500,000; 4. Other assets used ≥$100,000. If no test is met AND adjusted taxable income >$250,000, loss is quarantined. Commissioner discretion may apply.  _(Division 35)_

### Company Losses

- **Continuity of ownership test (COT)** — Carry forward subject to continuity of ownership test (COT) — same persons must maintain >50% voting, dividend, and capital rights (s 165-12). If COT fails, the same business test (SBT) may save losses if the company carries on the same business (s 165-13). SBT was broadened in 2015 to a "similar business test."  _(s 165-12; s 165-13)_

### Loss Carry-Back (Companies) — ENDED

- **Loss carry-back has ended** — The temporary loss carry-back (aggregated turnover <$5bn, refundable offset capped by the franking account) applied only to losses of the 2019-20 to 2022-23 income years, claimable in the 2020-21 to 2022-23 returns. It is NOT available for current-year losses; companies are back to carry-forward only (subject to COT/similar business test). Do not advise clients to expect a carry-back refund.  _(former Div 160 ITAA 1997)_

## Section 6 — Timing Strategies

**Timing Strategies**

| Strategy | Detail |
| --- | --- |
| Defer income to next FY | Delay invoicing until after 30 June if cash-basis taxpayer. For accrual-basis, delay delivery/completion |
| Accelerate deductions before 30 June | Prepay up to 12 months of deductible expenses (rent, insurance, subscriptions) — s 82KZM ITAA 1936 |
| Bring forward asset purchases | Use instant asset write-off before 30 June deadline. Asset must be first used or installed ready for use |
| Concessional super contribution | Maximise contributions before 30 June — $30,000 cap (2025–26). Carry-forward unused cap available if total super balance <$500,000 |
| Capital gains harvest | Realise capital losses before 30 June to offset gains. Wash sale rules: ATO will scrutinise buybacks of substantially similar assets |
| Defer capital gains | Hold assets >12 months to access 50% CGT discount (individuals and trusts) |
| Small business CGT concessions | Div 152: 15-year exemption, 50% active asset reduction, retirement exemption ($500k lifetime cap), rollover. Net assets <$6m or aggregated turnover <$2m |

## Section 7 — GST Optimization

**GST Optimization**

| Topic | Detail |
| --- | --- |
| Registration threshold | Mandatory if current or projected GST turnover ≥$75,000 ($150,000 for non-profits). Voluntary registration below threshold to claim input tax credits |
| Cash vs accrual reporting | Cash basis available if aggregated turnover <$10m. Defers GST on income until payment received |
| Input tax credits | Claim GST on business purchases. Apportionment required for mixed (business/private) use |
| GST-free supplies | Exports, health, education, some food — no GST charged, but input credits still claimable. Valuable for exporters |
| Going concern | Sale of a business as a going concern is GST-free (Div 38) — avoids cash flow impact on business transfers |
| Margin scheme (property) | GST calculated on margin (sale price minus purchase price) rather than full sale price. Buyer cannot claim input credits |
| Tax periods | Monthly, quarterly, or annual BAS. Quarterly if turnover <$20m. Annual election available if turnover <$75,000 |

## Section 8 — Superannuation & Social Security Optimization

### Superannuation (Retirement)

**Superannuation (Retirement)**

| Strategy | Detail | Legislation |
| --- | --- | --- |
| Concessional contributions | Cap $30,000/year (2025–26). Tax-deductible for self-employed. Taxed at 15% in the fund | s 291-20 ITAA 1997 |
| Carry-forward unused cap | Unused concessional cap from up to 5 prior years if total super balance <$500,000 at prior 30 June | s 291-170 |
| Non-concessional contributions | Cap $120,000/year (or $360,000 under bring-forward rule over 3 years). Not deductible, but earnings taxed at max 15% in super | s 292-85 |
| Salary sacrifice | Pre-tax super contributions reduce assessable income. Counted towards concessional cap |  |
| Spouse contribution offset | Contribute to low-income spouse's super for tax offset up to $540 | s 290-230 |
| Government co-contribution | Contribute to low-income earner's super; government matches up to $500 (income <$45,400) | s 12A SGAA |
| Division 293 tax | Additional 15% contributions tax on individuals with income + concessional contributions >$250,000 | Div 293 |

### Medicare Levy Surcharge Avoidance

- **MLS avoidance** — Private hospital cover avoids 1%–1.5% MLS if income >$101,000 (single) or >$202,000 (family). Cost of basic hospital cover is often less than the MLS.

## Section 9 — Investment & Retirement

**Investment & Retirement**

| Strategy | Detail |
| --- | --- |
| CGT 50% discount | Individuals and trusts — hold assets >12 months for 50% discount on net capital gain. **Ends for gains accruing from 1 July 2027** (indexation + 30% minimum rate instead — see alert at top) |
| Negative gearing | Investment property/share portfolio borrowing costs exceed income → net loss offsets other income. Uncapped through 30 June 2027; from 1 July 2027 residential-property losses are quarantined unless the property is a new build or was acquired on or before 12 May 2026 (see alert at top) |
| Franking credits | Australian company dividends carry franking credits. Excess credits refundable for individuals and super funds |
| Super in pension phase | Earnings on assets supporting income streams in pension phase are tax-free (up to the general transfer balance cap — $2.1m in 2026-27; $2.0m in 2025-26) |
| Transition to retirement (TTR) | Access super as income stream from preservation age while still working. Earnings in TTR taxed at 15% (not tax-free) |

## Section 10 — Red Lines (GAAR & Scrutiny Triggers)

### Part IVA (General Anti-Avoidance Rule)

- **Part IVA GAAR** — ITAA 1936, Part IVA (ss 177A–177J). The Commissioner can cancel a tax benefit arising from a scheme if the dominant purpose (assessed objectively) was to obtain the tax benefit. Penalties: 50% shortfall (scheme); 25% if reasonably arguable position.  _(ITAA 1936, Part IVA (ss 177A–177J))_

### ATO Scrutiny Triggers

**ATO Scrutiny Triggers**

| Trigger | Risk |
| --- | --- |
| Trust distributions to low-income beneficiaries with reimbursement agreements | s 100A — voided, trustee taxed at top rate |
| Division 7A non-complying loans | Deemed unfranked dividend |
| Non-commercial losses claimed without meeting 4 tests | Loss quarantined, amended assessment |
| Large work-related deductions vs income | Risk of audit |
| Wash sales around 30 June | CGT loss disallowed |
| Artificial income splitting via interposed entities | Part IVA application |
| Personal services income (PSI) through company or trust | PSI rules attribute income back to individual (Div 86–87) |
| Excessive salary sacrifice to reduce Division 293 exposure | ATO scrutiny, potential SG shortfall |
| Contractor vs employee misclassification | Super guarantee charge, penalties |
| Cryptocurrency — unreported disposal events | ATO data-matching from exchanges |

### Absolute Prohibitions

- **NEVER advise backdating trust distribution resolutions past 30 June** — NEVER advise backdating trust distribution resolutions past 30 June
- **NEVER advise sham contracting arrangements** — NEVER advise sham contracting arrangements
- **NEVER advise fabricating deductions or inflating claims** — NEVER advise fabricating deductions or inflating claims
- **NEVER structure arrangements with the dominant purpose of tax avoidance** — NEVER structure arrangements with the dominant purpose of tax avoidance
- **NEVER advise ignoring Division 7A requirements for private company loans** — NEVER advise ignoring Division 7A requirements for private company loans

## Section 11 — Annual Tax Planning Calendar

**Annual Tax Planning Calendar**

| When | Action |
| --- | --- |
| July | New FY starts. Review prior year's unused concessional super cap. Lodge prior-year BAS |
| August–September | Obtain prior-year tax assessment. Review loss carry-forward position |
| October | Self-lodger deadline (31 Oct). Review investment portfolio for CGT planning |
| November–December | Mid-year tax review. Adjust PAYG instalments if income changed materially |
| January | Superannuation guarantee due (Q2). Review Division 7A loan repayments |
| February–March | Lodge Q2 BAS. Model year-end tax position. Begin pre-30 June planning |
| April–May | Execute prepayment strategies. Make concessional super contributions. Review asset purchases for instant write-off |
| June (before 30 June) | **Critical month.** Finalise trust distribution resolutions. Make super contributions (allow processing time — contribute by ~25 June). Prepay expenses. Realise capital losses. Lodge PAYG variation if needed |

## Section 12 — Cash Impact Examples

### Example 1 — Sole Trader Incorporates

**Before:** Sole trader, $180,000 net profit. Tax: ~$51,067 + $3,600 Medicare = $54,667.

**After:** Pty Ltd, pays $80,000 salary + $12,000 super. Retains $88,000 in company at 25% = $22,000 company tax. Personal tax on $80,000 salary: ~$16,788 + $1,600 Medicare = $18,388. **Total tax: $40,388. Saving: ~$14,279.**

### Example 2 — Maximising Super Contributions

Sole trader, $120,000 profit. Claims $30,000 concessional super contribution (deductible). Taxable income drops to $90,000. Tax saving at 30% marginal: $9,000 less 15% super tax ($4,500) = **net saving $4,500 + compounding in super environment.**

### Example 3 — Instant Asset Write-Off

Small business buys 3 laptops at $2,500 each and a vehicle at $18,000. Total: $25,500 immediately deductible (each asset <$20,000). At 30% marginal rate = **$7,650 cash saving in the year of purchase** vs multi-year depreciation.

### Example 4 — Negative Gearing Investment Property

Employee earns $120,000. Investment property: $25,000 rent less $35,000 expenses (interest, rates, depreciation) = $10,000 net loss. Taxable income: $110,000. Tax saving at 30% marginal: **$3,000 cash refund via PAYG variation.**

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
