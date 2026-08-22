---
name: nu-individual-return
description: Use this skill whenever asked about Nunavut territorial income tax for a self-employed sole proprietor. Trigger on phrases like "Nunavut tax", "NU428", "Nunavut income tax", "Nunavut Cost of Living Tax Credit", "Nunavut Child Benefit", "territorial tax Nunavut", or any question about computing Nunavut territorial tax. ALWAYS read this skill before touching any Nunavut territorial tax work.
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

# NU Individual Return

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada -- Nunavut |
| Tax | Territorial income tax (NU428) |
| Currency | CAD only |
| Tax year | Calendar year |
| Primary legislation | Income Tax Act (Nunavut), S.Nu. 2001, c. 7 |
| Tax authority | CRA on behalf of Nunavut (Department of Finance, GN) |
| Filing portal | CRA My Account / NETFILE / EFILE |
| Form | NU428 -- Nunavut Tax; NU479 (Credits) |
| Filing deadline | June 15 (self-employed); payment due April 30 |
| Contributor | Open Accountants Community |
| Validated by | Live status: https://openaccountants.com/skills/nu-individual-return |
| Skill version | 1.0 |

### Nunavut Tax Rates (2025, indexed from 2024)

**Nunavut Tax Rates (2025, indexed from 2024)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 54,707 | 4.00% |
| 54,708 -- 109,413 | 7.00% |
| 109,414 -- 177,881 | 9.00% |
| 177,882+ | 11.50% |

**Nunavut has the lowest top marginal territorial rate in Canada at 11.50%.**

### Basic Personal Amount (BPA)

- **Nunavut BPA 2025** — approximately $19,274 CAD (indexed; verify against CRA / GN published indexation tables)

Nunavut historically has had the highest territorial BPA in Canada.

### Nunavut-specific credits

**Nunavut-specific credits**

| Credit | Notes |
| --- | --- |
| Nunavut Cost of Living Tax Credit | Refundable. Two components: basic credit on first $12,000 of taxable income at 4%; supplementary credit on income $12,000–$65,000 with a phase-out. Reduces basic tax then refundable. |
| Nunavut Child Benefit (NUCB) | Refundable monthly benefit administered by CRA; not on NU428 directly but assessed from T1 net income. |
| Nunavut Political Contribution Tax Credit | Tiered, max $500 credit. |
| Nunavut Volunteer Firefighters' Tax Credit | $500 non-refundable. |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown territory | Do not apply this skill |
| Inuit beneficiary under Nunavut Agreement | Apply standard rules; escalate any s. 87 / Nunavut Agreement question |
| Part-year resident | Escalate |
| Unknown bracket year | 2025 indexed figures |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — territory of residence on Dec 31 (must be Nunavut), federal taxable income (T1 line 26000), federal net income.
- **Recommended inputs** — marital status, spouse income, children, Inuit beneficiary status under Nunavut Agreement, T1 line 23600 (for Cost of Living credit).
- **Ideal inputs** — complete T1 data, prior NU428, GN credit assessments.

### Refusal Catalogue

- **R-NU-1** — Province/territory is not Nunavut on December 31. (Not Nunavut resident.)  _(R-NU-1)_
- **R-NU-2** — Individual sole proprietors only. (Corporations/trusts.)  _(R-NU-2)_
- **R-NU-3** — Escalate. Apply NU rates only to the period of Nunavut residency. (Part-year resident.)  _(R-NU-3)_
- **R-NU-4** — Escalate. Nunavut has no Indian Act reserves but specific Nunavut Agreement provisions may apply to Inuit beneficiaries. (Income earned on reserve under s. 87 Indian Act.)  _(R-NU-4)_

## Section 3 -- Transaction Pattern Library

Nunavut tax is computed from federal return data. Transaction classification is in `ca-fed-t2125`.

## Section 4 -- Worked Examples

### Example 1 -- Low Income

**Input:** Taxable income $22,000. Single.

**Computation:**
- Gross Nunavut tax: $22,000 × 4.00% = $880.00
- BPA credit: $19,274 × 4.00% = $770.96
- Basic NU tax before Cost of Living credit: $109.04
- Cost of Living basic credit ($12,000 × 4%) = $480.00
- Net NU tax: −$370.96 (refundable to taxpayer)

### Example 2 -- Mid-Range

**Input:** Taxable income $85,000. Single.

**Computation:**
- $54,707 at 4.00% = $2,188.28
- $30,293 at 7.00% = $2,120.51
- Gross NU tax: $4,308.79
- BPA credit: $770.96
- Basic NU tax: $3,537.83
- Cost of Living basic ($480.00) plus partial supplementary; net NU tax approximately $2,800 (verify supplementary formula).

### Example 3 -- High Income

**Input:** Taxable income $300,000. Single.

**Computation:**
- $54,707 at 4.00% = $2,188.28
- $54,706 at 7.00% = $3,829.42
- $68,468 at 9.00% = $6,162.12
- $122,119 at 11.50% = $14,043.69
- Gross NU tax: $26,223.51
- BPA credit: $770.96
- Basic NU tax: $25,452.55
- Cost of Living credit fully phased out.

## Section 5 -- Edge Cases

### EC-NU-1: Cost of Living Tax Credit supplementary formula

- **EC-NU-1** — Verify the current NU479 supplementary formula from the GN Department of Finance before computing. Conservative default: report basic credit only and flag supplementary as [T2].

### EC-NU-2: Northern Residents Deductions interaction

- **EC-NU-2** — Federal Northern Residents Deductions (line 25500 of T1) reduce federal taxable income for residents of prescribed northern zones. ALL of Nunavut is a prescribed northern zone. Confirm the deduction is claimed federally before computing NU428; it will lower territorial taxable income proportionally.

### EC-NU-3: Inuit beneficiary income from Nunavut Land Claims Agreement

- **EC-NU-3** — Income arising directly from the Nunavut Agreement (e.g., royalty distributions to a Designated Inuit Organization) may have specific tax treatment. Escalate.

### EC-NU-4: Mining and resource royalties

- **EC-NU-4** — If T2125 includes Nunavut mining royalty income, escalate — interactions with the Nunavut Agreement royalty mechanism are complex.

## Section 6 -- Self-checks

- [ ] Confirmed territory of residence is Nunavut on Dec 31.
- [ ] Federal taxable income reconciles to line 26000 of T1.
- [ ] Northern Residents Deductions checked for federal return.
- [ ] BPA applied at 4.00% (lowest NU bracket).
- [ ] Bracket boundaries match 2025 indexed thresholds.
- [ ] Cost of Living Tax Credit computed (refundable component identified).
- [ ] NU-specific credits (Volunteer Firefighter, Political) considered.
- [ ] Output flags any [T2]/[T3] item for reviewer judgement.

## Section 7 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Canadian CPA familiar with Nunavut territorial tax before filing.

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
