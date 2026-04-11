---
name: nz-acc-levies
description: Use this skill whenever asked about New Zealand ACC levies for self-employed individuals. Trigger on phrases like "ACC levy", "earner levy", "work levy", "CoverPlus", "CoverPlus Extra", "accident compensation", "ACC invoice", "classification unit", or any question about ACC obligations for sole traders in New Zealand. Covers earner levy, work levy by classification unit (CU), CoverPlus/CoverPlus Extra, maximum liable earnings, and payment schedules. ALWAYS read this skill before touching any NZ ACC work.
---

# NZ ACC Levies -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | New Zealand |
| Jurisdiction Code | NZ |
| Primary Legislation | Accident Compensation Act 2001 (AC Act) |
| Supporting Legislation | Injury Prevention, Rehabilitation, and Compensation Act 2001 |
| Authority | Accident Compensation Corporation (ACC) |
| Filing Portal | myACC for Business (myacc.acc.co.nz) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a New Zealand chartered accountant (CA) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 (1 April 2025 -- 31 March 2026) |
| Confidence Coverage | Tier 1: earner levy rate, work levy computation, maximum liable earnings. Tier 2: CU selection, CoverPlus Extra, experience rating. Tier 3: claims management, dispute resolution, complex multi-business structures. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any ACC levy figure, you MUST know:

1. **Self-employment status** [T1] -- sole trader, partner, or shareholder-employee
2. **Classification unit (CU) code** [T2] -- determines work levy rate; based on primary business activity
3. **Liable earnings** [T1] -- net self-employment income (as per IR3 or IR7)
4. **CoverPlus or CoverPlus Extra** [T1] -- which ACC cover option is in place
5. **Whether any experience rating applies** [T2] -- claims history adjustment
6. **Tax year** [T1] -- ACC invoices are based on the prior tax year's earnings

**If the client is a PAYE employee only, STOP. Employer pays ACC levies for employees. This skill covers self-employed ACC only.**

---

## Step 1: ACC Levy Components [T1]

**Legislation:** AC Act 2001, Schedule 1

Self-employed individuals pay two ACC levies:

| Levy | Who Pays | Basis |
|------|----------|-------|
| Earner levy | All earners (including self-employed) | Liable earnings |
| Work levy | Self-employed only (replaces employer's work levy) | Liable earnings, rate varies by CU |

### Earner Levy Rate (2025/26) [T1]

| Item | Rate |
|------|------|
| Earner levy | $1.67 per $100 of liable earnings (1.67%) |

**Note:** This rate is set annually by ACC. Verify at acc.co.nz for the current year.

### Work Levy Rates (2025/26) [T2]

Work levy rates vary by classification unit (CU). Examples:

| CU Code | Industry Description | Work Levy Rate (per $100) |
|---------|---------------------|--------------------------|
| 72100 | Computer consultancy | ~$0.08 |
| 69200 | Accounting services | ~$0.08 |
| 62000 | Software development | ~$0.09 |
| 52100 | General retail | ~$0.47 |
| 41100 | Building construction | ~$2.68 |
| 01600 | Dairy farming | ~$2.41 |
| 11200 | Forestry | ~$8.30 |

**These rates are illustrative. Actual rates must be verified at acc.co.nz or on the client's ACC invoice.**

---

## Step 2: Maximum Liable Earnings [T1]

**Legislation:** AC Act 2001, Schedule 1, Clause 10

| Item | Amount (2025/26) |
|------|-----------------|
| Maximum liable earnings | $142,283 (approximate -- verify with ACC) |
| Minimum liable earnings | No statutory minimum for self-employed |

Levies are calculated only on earnings up to the maximum. Earnings above this cap are not subject to ACC levies.

---

## Step 3: Levy Computation [T1]

| Step | Action |
|------|--------|
| 3.1 | Determine liable earnings = net self-employment income from IR3 |
| 3.2 | Cap earnings at maximum liable earnings if applicable |
| 3.3 | Earner levy = Liable earnings x earner levy rate / 100 |
| 3.4 | Work levy = Liable earnings x work levy rate for CU / 100 |
| 3.5 | Add Working Safer levy (if applicable): small per-$100 amount (~$0.08) |
| 3.6 | Total ACC levy = Earner levy + Work levy + Working Safer levy |
| 3.7 | GST: ACC levies are GST-exclusive; GST is added if the self-employed person is GST-registered |

---

## Step 4: CoverPlus vs CoverPlus Extra [T1/T2]

### CoverPlus (Default) [T1]

| Feature | Detail |
|---------|--------|
| Compensation basis | 80% of liable earnings (based on prior year's IR3) |
| Levy basis | Actual liable earnings from prior year |
| Adjustment | Levies adjusted when tax return is filed |

### CoverPlus Extra [T2]

| Feature | Detail |
|---------|--------|
| Compensation basis | Agreed level of cover chosen by the self-employed person |
| Levy basis | Chosen cover amount (not actual earnings) |
| Flexibility | Can choose cover level independent of income |
| Agreement | Must sign CoverPlus Extra agreement with ACC |

[T2] Flag for reviewer: CoverPlus Extra can result in higher or lower cover than actual earnings. Advise client to review chosen level annually.

---

## Step 5: Payment and Invoicing [T1]

| Detail | Value |
|--------|-------|
| Invoice timing | ACC sends invoice after IR3 is filed (typically September-November) |
| Payment options | Single payment, or instalments (2, 4, or monthly by arrangement) |
| Due date | As stated on ACC invoice (typically 30 days from issue) |
| Late payment | Penalties and interest apply |

### Provisional Invoicing [T1]

If the IR3 has not yet been filed, ACC issues a provisional invoice based on the most recent known earnings. This is adjusted once the actual return is processed.

---

## Step 6: Edge Case Registry

### EC1 -- Multiple business activities [T2]
**Situation:** Client runs a software consultancy (CU 72100) and a construction side business (CU 41100).
**Resolution:** ACC assigns the CU based on the primary activity (>50% of time or income). If activities are roughly equal, ACC may split or assign the higher-risk CU. [T2] Flag for reviewer to confirm CU assignment with ACC.

### EC2 -- First year of self-employment [T1]
**Situation:** Client started freelancing in March 2025. No prior-year IR3.
**Resolution:** ACC will estimate levies or use the minimum. Once the first IR3 is filed, levies are recalculated and adjusted. Client may receive a refund or additional invoice.

### EC3 -- Self-employed AND employee [T1]
**Situation:** Client has PAYE employment (employer pays ACC) and a freelance side business.
**Resolution:** Earner levy is paid on total earnings (both sources combined, up to maximum). Work levy applies only to self-employment income. PAYE employer covers work levy for employment income.

### EC4 -- Earnings exceed maximum [T1]
**Situation:** Consultant earns $200,000 net self-employment income.
**Resolution:** Levies are calculated on $142,283 (maximum), not $200,000. Weekly compensation if injured is also capped at 80% of the maximum.

### EC5 -- Client disputes CU classification [T2]
**Situation:** Client classified as "building construction" but primarily does project management from an office.
**Resolution:** Client can apply to ACC for CU reclassification. [T2] Flag for reviewer. CU determines work levy rate and can significantly affect costs.

### EC6 -- GST on ACC levies [T1]
**Situation:** GST-registered sole trader receives ACC invoice. Is GST claimable?
**Resolution:** ACC levies are GST-exclusive. If the self-employed person is GST-registered, ACC adds GST to the invoice, and the GST component is claimable as input tax on the GST return.

---

## Step 7: Test Suite

### Test 1 -- Standard software consultant
**Input:** CU 72100 (computer consultancy), liable earnings $120,000, work levy rate $0.08/100.
**Expected output:**
- Earner levy: $120,000 x 1.67/100 = $2,004.00
- Work levy: $120,000 x 0.08/100 = $96.00
- Working Safer: $120,000 x 0.08/100 = $96.00
- Total ACC levy: ~$2,196.00 (excl. GST)

### Test 2 -- High earner hitting cap
**Input:** CU 69200, liable earnings $200,000, maximum $142,283.
**Expected output:**
- Capped earnings: $142,283
- Earner levy: $142,283 x 1.67/100 = $2,376.13
- Work levy: $142,283 x 0.08/100 = $113.83
- Working Safer: $142,283 x 0.08/100 = $113.83
- Total: ~$2,603.79 (excl. GST)

### Test 3 -- Builder (high-risk CU)
**Input:** CU 41100, liable earnings $80,000, work levy rate $2.68/100.
**Expected output:**
- Earner levy: $80,000 x 1.67/100 = $1,336.00
- Work levy: $80,000 x 2.68/100 = $2,144.00
- Working Safer: $80,000 x 0.08/100 = $64.00
- Total: ~$3,544.00 (excl. GST)

### Test 4 -- Low-income first-year freelancer
**Input:** CU 72100, liable earnings $25,000.
**Expected output:**
- Earner levy: $25,000 x 1.67/100 = $417.50
- Work levy: $25,000 x 0.08/100 = $20.00
- Working Safer: $25,000 x 0.08/100 = $20.00
- Total: ~$457.50 (excl. GST)

---

## PROHIBITIONS

- NEVER assume work levy rates are the same for all industries -- they vary significantly by classification unit
- NEVER calculate levies on earnings above the maximum liable earnings cap
- NEVER confuse CoverPlus (default, based on actual earnings) with CoverPlus Extra (agreed amount)
- NEVER omit the earner levy -- it applies to ALL earners, not just self-employed
- NEVER forget GST treatment -- ACC levies are GST-exclusive; GST is added for registered persons
- NEVER use a work levy rate without verifying it against the current ACC levy guidebook or invoice
- NEVER present calculations as definitive -- always label as estimated and direct client to ACC or a qualified NZ chartered accountant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
