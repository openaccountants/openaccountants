---
name: ny-estimated-tax
description: >
  Use this skill whenever asked about New York State estimated tax (Form IT-2105) for self-employed individuals. Trigger on phrases like "IT-2105", "NY estimated tax", "New York quarterly tax", "MCTMT", "NYC estimated tax", "Yonkers tax", "NY underpayment penalty", "IT-2105.9", or any question about quarterly estimated income tax payments for New York State, NYC, or Yonkers. Covers quarterly instalment requirements, safe harbour rules, MCTMT estimated payments, underpayment penalty via IT-2105.9, and NYC estimated tax. ALWAYS read this skill before touching any NY estimated tax work.
version: 2.0
jurisdiction: US-NY
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# NY Estimated Tax (IT-2105) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| State | New York |
| Tax | Quarterly estimated income tax (state + NYC + Yonkers + MCTMT) |
| Forms | IT-2105 (voucher), IT-2105.9 (underpayment penalty) |
| Primary legislation | NY Tax Law Section 685 |
| Supporting legislation | NYC Admin Code 11-1701; NY Tax Law Art. 30-A (Yonkers) |
| Authority | New York State Department of Taxation and Finance (NYSDTF) |
| Portal | www.tax.ny.gov |
| Currency | USD only |
| Threshold | Estimated tax (state + city + MCTMT) after withholding >= $300 |
| Safe harbours | 90% current year OR 100%/110% prior year |
| Payment schedule | April 15, June 15, September 15, January 15 |
| Contributor | Open Accountants Community |
| Validated by | April 2026 |
| Validation date | April 2026 |

**Payment schedule (TY2025):**

| Instalment | Due date |
|---|---|
| 1st | April 15, 2025 |
| 2nd | June 15, 2025 |
| 3rd | September 15, 2025 |
| 4th | January 15, 2026 |

**Key rates:**

| Item | Value |
|---|---|
| MCTMT Zone 1 (self-employed) | 0.60% of NESE > $50,000 |
| MCTMT Zone 2 (self-employed) | 0.34% of NESE > $50,000 |
| NYC top resident rate | 3.876% |
| Yonkers resident surcharge | 16.75% of NY state tax |
| 110% prior-year threshold | NYAGI > $150,000 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Prior year NYAGI unknown | Assume > $150K, use 110% safe harbour |
| MCTMT zone uncertain | Confirm county of self-employment |
| NYC residency unclear | Do not include NYC tax unless confirmed NYC resident |
| UBT credit available | Include only if taxpayer files NYC UBT return |
| Annualized method | Default to equal instalments; flag annualized option for reviewer |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- expected NY state tax, NYC tax (if applicable), MCTMT (if applicable), prior year NY tax return, expected withholding.

**Recommended** -- prior year NYAGI (for 110% test), county of self-employment (for MCTMT zone), NYC UBT credit estimate.

**Ideal** -- complete prior year IT-201, current year income projection, W-2 withholding estimates, NYC UBT return data.

**Refusal policy if minimum is missing -- SOFT WARN.** Without prior year data, the safe harbour cannot be computed.

### Refusal catalogue

**R-NY-ET-1 -- Corporate estimated tax (CT-400).** Trigger: corporation. Message: "Corporate estimated tax has different rules."

**R-NY-ET-2 -- Partnership/fiduciary estimated tax.** Trigger: partnership or trust. Message: "Partnership and fiduciary estimated tax are outside this skill."

**R-NY-ET-3 -- PTET estimated payments.** Trigger: pass-through entity tax. Message: "PTET estimated payments are outside this skill."

**R-NY-ET-4 -- Non-resident filers.** Trigger: non-resident of NY. Message: "Non-resident estimated tax has different rules."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a NY estimated tax payment.

### 3.1 NYSDTF estimated tax debits

| Pattern | Treatment | Notes |
|---|---|---|
| NYS TAX, NY STATE TAX, NYSDTF | NY estimated payment | Match with Apr/Jun/Sep/Jan timing |
| IT-2105, IT2105 | NY estimated payment | Form number reference |
| NEW YORK ESTIMATED TAX | NY estimated payment | Explicit description |
| TAX.NY.GOV PAYMENT | NY estimated payment | Online payment |

### 3.2 Timing-based identification

| Debit date range | Likely instalment | Confidence |
|---|---|---|
| 10 April -- 20 April | 1st instalment | High if NY tax payee |
| 10 June -- 20 June | 2nd instalment | High |
| 10 September -- 20 September | 3rd instalment | High |
| 10 January -- 20 January | 4th instalment | High |

### 3.3 Related but NOT NY estimated tax

| Pattern | Treatment | Notes |
|---|---|---|
| IRS, FEDERAL ESTIMATED | EXCLUDE | Federal estimated tax |
| NYC DOF, NYC PROPERTY | EXCLUDE | NYC property tax |
| NY SALES TAX | EXCLUDE | Sales tax payment |
| NYS PENALTY, NYS INTEREST | EXCLUDE | Penalty/interest |
| IT-201 BALANCE | Flag for reviewer | Annual return balance, not estimated |

---

## Section 4 -- Worked examples

### Example 1 -- Standard NYC freelancer

**Input:** Single NYC resident. NYAGI $120,000. NY tax $6,500. NYC tax $3,800. MCTMT ($120,000 - $50,000) x 0.60% = $420. No withholding.

| Component | Amount |
|---|---|
| NY state tax | $6,500 |
| NYC tax | $3,800 |
| MCTMT | $420 |
| **Total** | **$10,720** |

Required: 90% x $10,720 = $9,648 (or 100% prior if lower). Quarterly: $2,412.

### Example 2 -- High-income, 110% prior year

**Input:** Single. NYAGI $200,000. Current year total $18,000. Prior year $14,000.

**Computation:** 90% current = $16,200. 110% prior = $15,400. Required = $15,400 (lesser). Quarterly = $3,850.

### Example 3 -- Below threshold

**Input:** NYC resident. Estimated tax after withholding = $250.

**Output:** $250 < $300 threshold. No estimated payments required.

### Example 4 -- Yonkers resident

**Input:** Yonkers resident. NY state tax $5,000. Yonkers surcharge = $5,000 x 16.75% = $837.50.

**Output:** Include $837.50 in estimated tax total.

### Example 5 -- MCTMT Zone 2 only

**Input:** Westchester resident (Zone 2). NESE $80,000.

**Output:** MCTMT = ($80,000 - $50,000) x 0.34% = $102.

---

## Section 5 -- Computation rules

### 5.1 Determine total estimated tax

```
total_estimated = NY_state_tax + NYC_tax + Yonkers_tax + MCTMT
net_estimated = total_estimated - expected_withholding - credits
if net_estimated < 300: no estimated payments required
```

### 5.2 Required annual payment

Required = lesser of:
- 90% of current year tax, OR
- 100% of prior year tax (110% if NYAGI > $150,000)

### 5.3 Quarterly instalments

Each instalment = required annual payment / 4 (25% each).

### 5.4 NY state tax computation

Federal AGI + NY additions - NY subtractions = NYAGI. Apply NY rate schedule (4% to 10.9%). Subtract NY credits.

### 5.5 NYC resident tax

NYC taxable income x NYC rates (3.078% to 3.876%). Subtract NYC household credit and UBT credit.

### 5.6 MCTMT

Self-employed in MCTD (12 counties): NESE above $50,000 x zone rate (0.60% Zone 1, 0.34% Zone 2).

### 5.7 Yonkers

Resident: 16.75% of NY state tax. Nonresident working in Yonkers: 0.5% of Yonkers-source earnings.

---

## Section 6 -- Penalties and interest

### 6.1 Underpayment penalty

Computed on IT-2105.9. Rate varies quarterly (set by NYSDTF). Applied per-quarter on the shortfall from each instalment due date.

### 6.2 Safe harbour protection

If payments meet the required annual payment (lesser of 90% current or 100%/110% prior), no penalty.

### 6.3 Annualized income instalment method

IT-2105.9 allows annualized method for uneven income. Computes income actually earned through each quarter-end. Reduces early-quarter payments for seasonal freelancers.

---

## Section 7 -- Filing and payment procedure

**Paper vouchers:** Form IT-2105 mailed to NYSDTF.

**Online:** Pay at www.tax.ny.gov (no voucher needed).

**Prior year overpayment:** Applied to reduce 1st quarter payment. Document on voucher.

---

## Section 8 -- Edge cases

**EC1 -- 110% prior-year rule.** NYAGI > $150,000 requires 110% of prior year (not 100%). Mirrors federal rule.

**EC2 -- MCTMT included in estimated tax.** MCTMT is on Form IT-201 (Lines 54a/54b). NOT a separate filing.

**EC3 -- NYC UBT credit.** IT-219 credit reduces NYC estimated tax. Include when estimating.

**EC4 -- First year of self-employment.** Prior year safe harbour = $0. Use 90% current year.

**EC5 -- Annualized income method.** Seasonal freelancer: use IT-2105.9 to reduce early-quarter payments.

**EC6 -- Overpayment from prior year.** Applied to 1st quarter estimated payment.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] $300 threshold applied correctly
- [ ] All tax layers included (state + city + Yonkers + MCTMT as applicable)
- [ ] 110% prior-year rule applied for NYAGI > $150,000
- [ ] MCTMT computed with correct zone rate and $50,000 threshold
- [ ] NYC UBT credit offset included if applicable
- [ ] Quarterly payments divided evenly (25% each)
- [ ] Withholding and prior-year overpayment credits subtracted
- [ ] Reviewer brief notes which safe harbour method was used
- [ ] Due dates confirmed (Apr 15, Jun 15, Sep 15, Jan 15)
- [ ] Output labelled as estimated until reviewer confirms

---

## Section 10 -- Test suite

### Test 1 -- NYC freelancer
**Input:** NYAGI $120,000. NY tax $6,500. NYC $3,800. MCTMT $420. No withholding.
**Expected:** Total $10,720. Required 90% = $9,648. Quarterly $2,412.

### Test 2 -- High-income 110% rule
**Input:** NYAGI $200,000. Current $18,000. Prior $14,000.
**Expected:** 90% current = $16,200. 110% prior = $15,400. Required = $15,400. Quarterly = $3,850.

### Test 3 -- Below threshold
**Input:** Estimated tax after withholding = $250.
**Expected:** No payments required.

### Test 4 -- Yonkers resident
**Input:** NY state tax $5,000.
**Expected:** Yonkers = $837.50. Include in total.

### Test 5 -- MCTMT Zone 2
**Input:** Westchester. NESE $80,000.
**Expected:** MCTMT = $102.

### Test 6 -- First year
**Input:** No prior NY return.
**Expected:** Prior year safe harbour = $0. Use 90% current.

---

## Prohibitions

- NEVER omit MCTMT from estimated tax calculations
- NEVER use 100% prior-year safe harbour for NYAGI > $150,000 -- use 110%
- NEVER estimate NYC tax for non-NYC residents
- NEVER ignore the NYC UBT credit when estimating NYC tax
- NEVER advise on penalty waiver requests -- procedural matter
- NEVER confuse NY estimated tax with federal estimated tax

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
