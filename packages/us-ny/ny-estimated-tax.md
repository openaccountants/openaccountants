---
name: ny-estimated-tax
description: Use this skill whenever asked about New York State estimated tax (Form IT-2105) for self-employed individuals. Trigger on phrases like "IT-2105", "NY estimated tax", "New York quarterly tax", "MCTMT", "NYC estimated tax", "Yonkers tax", "NY underpayment penalty", "IT-2105.9", or any question about quarterly estimated income tax payments for New York State, NYC, or Yonkers. Covers quarterly instalment requirements, safe harbour rules, MCTMT estimated payments, underpayment penalty via IT-2105.9, and NYC estimated tax. ALWAYS read this skill before touching any NY estimated tax work.
version: 2.0
jurisdiction: US-NY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - us-tax-workflow-base
category: state
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NY Estimated Tax

## Section 1 -- Quick reference

**Section 1 -- Quick reference**  _([Form IT-2105-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf))_

| Field | Value |
| --- | --- |
| State | New York |
| Tax | Quarterly estimated income tax (state + NYC + Yonkers) plus MCTMT estimated payments when applicable |
| Forms | IT-2105 (voucher), IT-2105.9 (underpayment penalty) |
| Primary legislation | NY Tax Law Section 685 |
| Supporting legislation | NYC Admin Code 11-1701; NY Tax Law Art. 30-A (Yonkers); NY Tax Law Art. 23 (MCTMT) |
| Authority | New York State Department of Taxation and Finance (NYSDTF) |
| Portal | www.tax.ny.gov |
| Currency | USD only |
| Income-tax threshold | NYS, NYC, or Yonkers estimated income tax after withholding/credits >= $300 |
| MCTMT threshold | Estimated MCTMT payments required if any MCTMT is expected after partnership-paid MCTMT |
| Safe harbors | 90% current year OR 100%/110% prior year |
| Payment schedule | April 15, June 16, September 15, January 15 |
| Contributor | Open Accountants Community |
| Validated by | July 2026 |
| Validation date | July 2026 |

**Payment schedule (TY2025)**  _([Form IT-2105-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf))_

| Instalment | Due date |
| --- | --- |
| 1st | April 15, 2025 |
| 2nd | June 16, 2025 |
| 3rd | September 15, 2025 |
| 4th | January 15, 2026 |

**Key rates**  _([Form IT-2105-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf))_

| Item | Value |
| --- | --- |
| MCTMT Zone 1 (self-employed) | 0.60% of Zone 1 NESE if Zone 1 NESE exceeds $50,000 |
| MCTMT Zone 2 (self-employed) | 0.34% of Zone 2 NESE if Zone 2 NESE exceeds $50,000 |
| NYC top resident rate | 3.876% |
| Yonkers resident surcharge | 16.75% of NY state tax |
| 110% prior-year threshold | Prior-year NYAGI or prior-year MCTD NESE > $150,000 ($75,000 if MFS) |
| 2025 underpayment penalty rate | 9.5% for Apr 15, 2025 through Apr 15, 2026 |

**Conservative defaults**  _(https://www.tax.ny.gov/pdf/2025/inc/it2105_9i_2025.pdf)_

| Ambiguity | Default |
| --- | --- |
| Prior year NYAGI unknown | Assume > $150K, use 110% safe harbour |
| MCTMT zone uncertain | Confirm county of self-employment |
| NYC residency unclear | Do not include NYC tax unless confirmed NYC resident |
| UBT credit available | Include only if taxpayer files NYC UBT return |
| Annualized method | Default to equal instalments; flag annualized option for reviewer |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — expected NY state tax, NYC tax (if applicable), MCTMT (if applicable), prior year NY tax return, expected withholding.  _(https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf)_
- **Recommended inputs** — prior-year NYAGI and prior-year MCTD NESE (for 110% test), filing status, county of self-employment (for MCTMT zone), NYC UBT credit estimate.  _(https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf)_
- **Ideal inputs** — complete prior year IT-201, current year income projection, W-2 withholding estimates, NYC UBT return data.
- **Refusal policy if minimum is missing** — SOFT WARN. Without prior year data, the safe harbour cannot be computed.

### Refusal catalogue

- **R-NY-ET-1 -- Corporate estimated tax (CT-400)** — Trigger: corporation. Message: "Corporate estimated tax has different rules."
- **R-NY-ET-2 -- Partnership/fiduciary estimated tax** — Trigger: partnership or trust. Message: "Partnership and fiduciary estimated tax are outside this skill."
- **R-NY-ET-3 -- PTET estimated payments** — Trigger: pass-through entity tax. Message: "PTET estimated payments are outside this skill."
- **R-NY-ET-4 -- Non-resident filers** — Trigger: non-resident of NY. Message: "Non-resident estimated tax has different rules."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a NY estimated tax payment.

### 3.1 NYSDTF estimated tax debits

**NYSDTF estimated tax debits**  _(https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NYS TAX, NY STATE TAX, NYSDTF | NY estimated payment | Match with Apr/Jun/Sep/Jan timing |
| IT-2105, IT2105 | NY estimated payment | Form number reference |
| NEW YORK ESTIMATED TAX | NY estimated payment | Explicit description |
| TAX.NY.GOV PAYMENT | NY estimated payment | Online payment |

### 3.2 Timing-based identification

**Timing-based identification**  _(https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf)_

| Debit date range | Likely instalment | Confidence |
| --- | --- | --- |
| 10 April -- 20 April | 1st instalment | High if NY tax payee |
| 10 June -- 20 June (June 16 statutory/observed due date for 2025) | 2nd instalment | High |
| 10 September -- 20 September | 3rd instalment | High |
| 10 January -- 20 January | 4th instalment | High |

### 3.3 Related but NOT NY estimated tax

**Related but NOT NY estimated tax**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRS, FEDERAL ESTIMATED | EXCLUDE | Federal estimated tax |
| NYC DOF, NYC PROPERTY | EXCLUDE | NYC property tax |
| NY SALES TAX | EXCLUDE | Sales tax payment |
| NYS PENALTY, NYS INTEREST | EXCLUDE | Penalty/interest |
| IT-201 BALANCE | Flag for reviewer | Annual return balance, not estimated |

## Section 4 -- Worked examples

### Example 1 -- Standard NYC freelancer

**Standard NYC freelancer component table**  _(https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf)_

| Component | Amount |
| --- | --- |
| NY state tax | $6,500 |
| NYC tax | $3,800 |
| MCTMT | $720 |
| **Total** | **$11,020** |

Input: Single NYC resident. NYAGI $120,000. NY tax $6,500. NYC tax $3,800. MCTMT $120,000 x 0.60% = $720 because Zone 1 NESE exceeds the $50,000 threshold. No withholding.

Required: 90% x $11,020 = $9,918 (or 100% prior if lower). Quarterly: $2,479.50 (round voucher payments to whole dollars).

### Example 2 -- High-income, 110% prior year

Input: Single. NYAGI $200,000. Current year total $18,000. Prior year $14,000.

Computation: 90% current = $16,200. 110% prior = $15,400. Required = $15,400 (lesser). Quarterly = $3,850.

### Example 3 -- Below threshold

Input: NYC resident. Estimated NYS/NYC/Yonkers income tax after withholding = $250 and no MCTMT expected.

Output: $250 < $300 income-tax threshold and MCTMT = $0, so no estimated payments required.

### Example 4 -- Yonkers resident

Input: Yonkers resident. NY state tax $5,000. Yonkers surcharge = $5,000 x 16.75% = $837.50.

Output: Include $837.50 in estimated tax total.

### Example 5 -- MCTMT Zone 2 only

Input: Westchester resident (Zone 2). NESE $80,000.

Output: MCTMT = $80,000 x 0.34% = $272 because Zone 2 NESE exceeds the $50,000 threshold.

## Section 5 -- Computation rules

### 5.1 Determine total estimated tax

- **Total estimated tax formula** — total_estimated = NY_state_tax + NYC_tax + Yonkers_tax + MCTMT net_estimated = total_estimated - expected_withholding - credits if income_tax_net_estimated < 300 and no MCTMT is expected: no estimated payments required; if MCTMT is expected, include MCTMT estimated payments even if income-tax estimated payments are below $300  _(https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf)_

### 5.2 Required annual payment

- **Required annual payment rule** — Required annual payment = lesser of 90% of current-year tax, or 100% of prior-year tax (110% if prior-year NYAGI or prior-year MCTD NESE exceeded $150,000; $75,000 if MFS). The prior-year return must cover a full 12-month year.  _([Form IT-2105.9-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it2105_9i_2025.pdf))_

### 5.3 Quarterly instalments

- **Quarterly instalment rule** — Each instalment = required annual payment / 4 (25% each).

### 5.4 NY state tax computation

- **NY state tax computation** — Federal AGI + NY additions - NY subtractions = NYAGI. Apply NY rate schedule (4% to 10.9%). Subtract NY credits.

### 5.5 NYC resident tax

- **NYC resident tax computation** — NYC taxable income x NYC rates (3.078% to 3.876%). Subtract NYC household credit and UBT credit.

### 5.6 MCTMT

- **MCTMT computation** — For self-employed individuals in the MCTD, test each zone separately. If allocated NESE in Zone 1 exceeds $50,000, MCTMT is 0.60% of the Zone 1 allocated NESE base. If allocated NESE in Zone 2 exceeds $50,000, MCTMT is 0.34% of the Zone 2 allocated NESE base. Do not subtract the $50,000 threshold from the taxable base.  _([Form IT-2105-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf))_

### 5.7 Yonkers

- **Yonkers tax computation** — Resident: 16.75% of NY state tax. Nonresident working in Yonkers: 0.5% of Yonkers-source earnings.

## Section 6 -- Penalties and interest

### 6.1 Underpayment penalty

- **Underpayment penalty rule** — Computed on Form IT-2105.9. For tax year 2025, the penalty rate is 9.5% for each period from April 15, 2025 through April 15, 2026. The statutory formula is the federal short-term rate plus 5.5 percentage points, with a 7.5% floor, adjusted quarterly.  _([Form IT-2105.9-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it2105_9i_2025.pdf))_

### 6.2 Safe harbour protection

- **Safe harbor protection rule** — No underpayment penalty applies if withholding and estimated payments meet the required annual payment: the smaller of 90% of 2025 tax or 100%/110% of 2024 tax, with the 110% rule triggered by prior-year NYAGI or MCTD NESE above $150,000 ($75,000 if MFS).  _([Form IT-2105.9-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it2105_9i_2025.pdf))_

### 6.3 Annualized income instalment method

- **Annualized income instalment method rule** — IT-2105.9 allows annualized method for uneven income. Computes income actually earned through each quarter-end. Reduces early-quarter payments for seasonal freelancers.  _(https://www.tax.ny.gov/pdf/2025/inc/it2105i_2025.pdf)_

## Section 7 -- Filing and payment procedure

**Paper vouchers:** Form IT-2105 mailed to NYSDTF.

**Online:** Pay at www.tax.ny.gov (no voucher needed).

**Prior year overpayment:** Applied to reduce 1st quarter payment. Document on voucher.

## Section 8 -- Edge cases

Prior-year NYAGI or prior-year MCTD NESE above $150,000 ($75,000 if MFS) requires 110% of prior-year tax (not 100%).

MCTMT is on Form IT-201 (Lines 54a/54b). NOT a separate filing.

IT-219 credit reduces NYC estimated tax. Include when estimating.

Prior year safe harbour = $0. Use 90% current year.

Seasonal freelancer: use IT-2105.9 to reduce early-quarter payments.

Applied to 1st quarter estimated payment.

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] $300 income-tax threshold applied correctly and MCTMT tested separately
- [ ] All tax layers included (state + city + Yonkers + MCTMT as applicable)
- [ ] 110% prior-year rule applied when prior-year NYAGI or MCTD NESE exceeds $150,000 ($75,000 if MFS)
- [ ] MCTMT computed with correct zone rate and $50,000 threshold-as-trigger (not an exemption amount)
- [ ] NYC UBT credit offset included if applicable
- [ ] Quarterly payments divided evenly (25% each)
- [ ] Withholding and prior-year overpayment credits subtracted
- [ ] Reviewer brief notes which safe harbour method was used
- [ ] Due dates confirmed (Apr 15, Jun 16, Sep 15, Jan 15 for TY2025)
- [ ] Output labelled as estimated until reviewer confirms

## Section 10 -- Test suite

### Test 1 -- NYC freelancer

Input: NYAGI $120,000. NY tax $6,500. NYC $3,800. MCTMT $720. No withholding.
Expected: Total $11,020. Required 90% = $9,918. Quarterly ~$2,480.

### Test 2 -- High-income 110% rule

Input: NYAGI $200,000. Current $18,000. Prior $14,000.
Expected: 90% current = $16,200. 110% prior = $15,400. Required = $15,400. Quarterly = $3,850.

### Test 3 -- Below threshold

Input: Estimated tax after withholding = $250.
Expected: No payments required.

### Test 4 -- Yonkers resident

Input: NY state tax $5,000.
Expected: Yonkers = $837.50. Include in total.

### Test 5 -- MCTMT Zone 2

Input: Westchester. NESE $80,000.
Expected: MCTMT = $272.

### Test 6 -- First year

Input: No prior NY return.
Expected: Prior year safe harbour = $0. Use 90% current.

## Prohibitions

- NEVER omit MCTMT from estimated tax calculations
- NEVER use 100% prior-year safe harbour when prior-year NYAGI or MCTD NESE exceeds $150,000 ($75,000 if MFS) -- use 110%
- NEVER estimate NYC tax for non-NYC residents
- NEVER ignore the NYC UBT credit when estimating NYC tax
- NEVER advise on penalty waiver requests -- procedural matter
- NEVER confuse NY estimated tax with federal estimated tax

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
