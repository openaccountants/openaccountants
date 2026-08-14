---
name: yt-individual-return
description: Use this skill whenever asked about Yukon territorial income tax for a self-employed sole proprietor. Trigger on phrases like "Yukon tax", "YT428", "Yukon income tax", "Yukon First Nations Income Tax Credit", "Pioneer Utility Grant", "territorial tax Yukon", or any question about computing Yukon territorial tax. ALWAYS read this skill before touching any Yukon territorial tax work.
version: 1.0
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# YT Individual Return

## Yukon Territorial Income Tax -- Sole Proprietor Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada -- Yukon |
| Tax | Territorial income tax (YT428) |
| Currency | CAD only |
| Tax year | Calendar year |
| Primary legislation | Income Tax Act (Yukon), R.S.Y. 2002, c. 118 |
| Tax authority | CRA on behalf of Yukon |
| Filing portal | CRA My Account / NETFILE / EFILE |
| Form | YT428 -- Yukon Tax; YT479 (Credits); Schedule 14 (carbon rebate) |
| Filing deadline | June 15 (self-employed); payment due April 30 |
| Contributor | Open Accountants Community |
| Validated by | Live status: https://openaccountants.com/skills/yt-individual-return |
| Skill version | 1.0 |

### Yukon Tax Rates (2025, indexed from 2024)

**Yukon Tax Rates (2025, indexed from 2024)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 57,375 | 6.40% |
| 57,376 -- 114,750 | 9.00% |
| 114,751 -- 177,882 | 10.90% |
| 177,883 -- 500,000 | 12.80% |
| 500,001+ | 15.00% |

Yukon parallels the federal brackets except the top bracket starts at $500,000 (not federal level).

### Basic Personal Amount (BPA)

- **Basic Personal Amount (BPA)** — approximately $16,129 CAD (Yukon's BPA tracks the federal enhanced BPA. For 2025, verify against CRA published indexation tables.)

### Yukon-specific credits

**Yukon-specific credits**

| Credit | Notes |
| --- | --- |
| Yukon First Nations Income Tax Credit | For status Indians resident on settlement land of a Yukon First Nation that has a Final Agreement Income Tax Act. Effectively cedes territorial tax to the First Nation. |
| Pioneer Utility Grant | Refundable. Seniors 65+ resident in Yukon. Not part of YT428 itself but flows through the territorial system. |
| Yukon Children's Fitness Tax Credit | Up to $1,000 per child; non-refundable at lowest bracket rate. |
| Yukon Small Business Investment Tax Credit | 25% of eligible investment, up to $25,000/year, with carryforward. Most relevant for corporate but individuals with eligible investments may claim. |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown territory | Do not apply this skill |
| Status Indian on settlement land | Escalate (FN tax may apply instead) |
| Part-year resident | Escalate |
| Unknown bracket year | 2025 indexed figures |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — territory of residence on Dec 31 (must be Yukon), federal taxable income (T1 line 26000), federal net income.
- **Recommended inputs** — marital status, spouse income, children, status Indian indicator, settlement land status, age (for Pioneer Utility Grant).
- **Ideal inputs** — complete T1 data, prior YT428, First Nation membership status, copy of YT479.

### Refusal Catalogue

- **R-YT-1 -- Not Yukon resident** — Province/territory is not Yukon on December 31. This skill only applies to Yukon residents.
- **R-YT-2 -- Corporations/trusts** — Individual sole proprietors only.
- **R-YT-3 -- Part-year resident** — Escalate. Apply YT rates only to the period the taxpayer was Yukon-resident; another province may tax the balance.
- **R-YT-4 -- Status Indian on Yukon First Nation settlement land** — Escalate. A Yukon First Nation with a Final Agreement Income Tax Act may have first-priority taxing right; the Yukon First Nations Income Tax Credit reduces YT tax to nil for that income.

## Section 3 -- Transaction Pattern Library

Yukon tax is computed from federal return data. Transaction classification is in `ca-fed-t2125`.

## Section 4 -- Worked Examples

### Example 1 -- Low Income

**Input:** Taxable income $20,000. Single.

**Computation:**
- Gross Yukon tax: $20,000 × 6.40% = $1,280.00
- BPA credit: $16,129 × 6.40% = $1,032.26
- Basic territorial tax: $247.74

### Example 2 -- Mid-Range

**Input:** Taxable income $90,000. Single.

**Computation:**
- $57,375 at 6.40% = $3,672.00
- $32,625 at 9.00% = $2,936.25
- Gross Yukon tax: $6,608.25
- BPA credit: $1,032.26
- Basic territorial tax: $5,575.99

### Example 3 -- High Income

**Input:** Taxable income $600,000. Single.

**Computation:**
- $57,375 at 6.40% = $3,672.00
- $57,375 at 9.00% = $5,163.75
- $63,132 at 10.90% = $6,881.39
- $322,118 at 12.80% = $41,231.10
- $100,000 at 15.00% = $15,000.00
- Gross Yukon tax: $71,948.24
- BPA credit: $1,032.26
- Basic territorial tax: $70,915.98

### Example 4 -- Status Indian on Yukon FN Settlement Land

**Input:** Status Indian under the Indian Act, resident on settlement land of a Yukon First Nation with a Final Agreement Income Tax Act, employment income $80,000 earned on settlement land.

**Treatment:**
- Income may be exempt from federal tax under s. 87 Indian Act.
- Yukon First Nation income tax (FN Final Agreement) and Yukon First Nations Income Tax Credit interact: territorial tax is effectively transferred to the FN.
- **Escalate to a Yukon CPA familiar with FN Final Agreement Income Tax Acts.**

## Section 5 -- Edge Cases

### EC-YT-1: Carbon Rebate

- **Carbon Rebate** — The federal carbon rebate (formerly Climate Action Incentive) for Yukon residents is delivered through the Yukon Government Carbon Price Rebate. This is delivered separately from YT428.

### EC-YT-2: Yukon Small Business Investment Tax Credit (YSBITC)

- **YSBITC** — Individuals with eligible Yukon investments may claim 25% credit (max $25,000/yr). Non-refundable but carries forward 7 years and back 3. Coordinate with federal investment credits to avoid double benefit.

### EC-YT-3: Mining royalties

- **Mining royalties** — If the taxpayer's T2125 includes Yukon mining or placer claim income, escalate — Yukon mining royalties and the Yukon-specific exploration tax credit have complex interactions.

## Section 6 -- Self-checks

- [ ] Confirmed territory of residence is Yukon on Dec 31 of the tax year.
- [ ] Federal taxable income reconciles to line 26000 of T1.
- [ ] BPA applied at 6.40% (lowest YT bracket).
- [ ] Bracket boundaries match 2025 indexed thresholds.
- [ ] First Nation status checked; YFN Income Tax Credit applied if applicable.
- [ ] Yukon-specific credits (Children's Fitness, YSBITC) considered.
- [ ] Output flags any [T2]/[T3] item for reviewer judgement.

## Section 7 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (a Canadian CPA familiar with Yukon territorial tax) before filing.

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
