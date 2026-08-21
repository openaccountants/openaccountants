---
name: nt-individual-return
description: Use this skill whenever asked about Northwest Territories territorial income tax for a self-employed sole proprietor. Trigger on phrases like "NWT tax", "NT428", "Northwest Territories income tax", "NWT Cost of Living Tax Credit", "NWT Child Benefit", "territorial tax NWT", or any question about computing Northwest Territories territorial tax. ALWAYS read this skill before touching any Northwest Territories territorial tax work.
version: 1.0
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NT Individual Return

## Section 1 -- Quick Reference

**Section 1 Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Canada -- Northwest Territories |
| Tax | Territorial income tax (NT428) |
| Currency | CAD only |
| Tax year | Calendar year |
| Primary legislation | Income Tax Act (NWT), R.S.N.W.T. 1988, c. I-1 |
| Tax authority | CRA on behalf of NWT (Department of Finance, GNWT) |
| Filing portal | CRA My Account / NETFILE / EFILE |
| Form | NT428 -- NWT Tax; NT479 (Credits) |
| Filing deadline | June 15 (self-employed); payment due April 30 |
| Contributor | Open Accountants Community |
| Validated by | Live status: https://openaccountants.com/skills/nt-individual-return |
| Skill version | 1.0 |

### NWT Tax Rates (2025, indexed from 2024)

**NWT Tax Rates (2025, indexed from 2024)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 51,964 | 5.90% |
| 51,965 -- 103,930 | 8.60% |
| 103,931 -- 168,967 | 12.20% |
| 168,968+ | 14.05% |

### Basic Personal Amount (BPA)

- **NWT BPA 2025** — $17,373 (approximately, indexed; verify against CRA / GNWT published indexation tables)

### NWT-specific credits

**NWT-specific credits**

| Credit | Notes |
| --- | --- |
| NWT Cost of Living Tax Credit | Refundable. Computed in two parts: (a) basic credit on first $12,000 of taxable income at 15.65%; (b) supplementary credit on taxable income $12,000–$66,000 at decreasing rates. Reduces basic tax then refundable balance. |
| NWT Risk Capital Investment Tax Credit | 30% on eligible NWT venture capital investments, lifetime cap $200,000 of investment ($60,000 credit). Non-refundable, 7-year carryforward, 3-year carryback. |
| NWT Political Contribution Tax Credit | Tiered, max $500 credit. |
| NWT Child Benefit | Refundable monthly benefit administered by CRA; not on NT428 directly but assessed from T1 net income. |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown territory | Do not apply this skill |
| Status Indian / Inuvialuit beneficiary | Apply standard rules unless income clearly exempt under s. 87 Indian Act; escalate if uncertain |
| Part-year resident | Escalate |
| Unknown bracket year | 2025 indexed figures |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — territory of residence on Dec 31 (must be NWT), federal taxable income (T1 line 26000), federal net income.
- **Recommended inputs** — marital status, spouse income, children, status Indian indicator, Inuvialuit beneficiary status, T1 line 23600 (net income, for Cost of Living credit calc).
- **Ideal inputs** — complete T1 data, prior NT428, GNWT credit assessments.

### Refusal Catalogue

- **R-NT-1 -- Not NWT resident** — Province/territory is not Northwest Territories on December 31.
- **R-NT-2 -- Corporations/trusts** — Individual sole proprietors only.
- **R-NT-3 -- Part-year resident** — Escalate. Apply NT rates only to the period of NWT residency.
- **R-NT-4 -- Income earned on reserve under s. 87 Indian Act** — Escalate. Federal exemption may also extend to territorial tax.

## Section 3 -- Transaction Pattern Library

NWT tax is computed from federal return data. Transaction classification is in `ca-fed-t2125`.

## Section 4 -- Worked Examples

### Example 1 -- Low Income

**Input:** Taxable income $20,000. Single.

**Computation:**
- Gross NWT tax: $20,000 × 5.90% = $1,180.00
- BPA credit: $17,373 × 5.90% = $1,025.01
- Basic NWT tax before Cost of Living credit: $154.99
- Cost of Living credit (basic): $12,000 × 15.65% = $1,878.00
- Net NWT tax (refundable portion): −$1,723.01 (i.e., $1,723.01 refundable to taxpayer)

### Example 2 -- Mid-Range

**Input:** Taxable income $80,000. Single.

**Computation:**
- $51,964 at 5.90% = $3,065.88
- $28,036 at 8.60% = $2,411.10
- Gross NWT tax: $5,476.98
- BPA credit: $1,025.01
- Basic NWT tax: $4,451.97
- Cost of Living basic credit ($12,000 × 15.65%) = $1,878.00 plus partial supplementary
- Net NWT tax: ~$2,573.97 (approximate; verify supplementary formula)

### Example 3 -- High Income

**Input:** Taxable income $250,000. Single.

**Computation:**
- $51,964 at 5.90% = $3,065.88
- $51,966 at 8.60% = $4,469.08
- $65,037 at 12.20% = $7,934.51
- $81,033 at 14.05% = $11,385.14
- Gross NWT tax: $26,854.61
- BPA credit: $1,025.01
- Basic NWT tax: $25,829.60
- Cost of Living credit fully phased out at this income.

## Section 5 -- Edge Cases

### EC-NT-1: Cost of Living Tax Credit supplementary formula

- **Supplementary credit formula caution** — The supplementary credit on income $12,000–$66,000 uses a decreasing rate. Verify the exact formula from the current GNWT NT479 schedule before computing. Conservative default: report basic credit only and flag supplementary as [T2].

### EC-NT-2: Carbon tax rebate

- **Carbon tax rebate treatment** — The NWT has a territorial carbon tax with its own rebate mechanism administered by GNWT (not the federal Canada Carbon Rebate). Confirm the year's rebate amount from the GNWT Department of Finance.

### EC-NT-3: Resource royalties

- **Resource royalties escalation** — If the taxpayer's T2125 includes NWT diamond, gold or oil/gas royalty income, escalate — territorial royalty interactions are complex and may interact with the Mackenzie Valley resource agreements.

### EC-NT-4: Inuvialuit Final Agreement beneficiaries

- **Inuvialuit Final Agreement beneficiaries escalation** — Income earned within the Inuvialuit Settlement Region may have specific tax treatment under the Inuvialuit Final Agreement. Escalate.

## Section 6 -- Self-checks

- [ ] Confirmed territory of residence is Northwest Territories on Dec 31.
- [ ] Federal taxable income reconciles to line 26000 of T1.
- [ ] BPA applied at 5.90% (lowest NT bracket).
- [ ] Bracket boundaries match 2025 indexed thresholds.
- [ ] Cost of Living Tax Credit computed (refundable component identified separately).
- [ ] NWT-specific credits (Risk Capital, Political) considered.
- [ ] Output flags any [T2]/[T3] item for reviewer judgement.

## Section 7 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Canadian CPA familiar with NWT territorial tax before filing.

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
