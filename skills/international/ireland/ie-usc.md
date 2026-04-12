---
name: ie-usc
description: Use this skill whenever asked about Ireland's Universal Social Charge (USC) for self-employed individuals or any taxpayer. Trigger on phrases like "USC calculation", "universal social charge", "USC rates Ireland", "USC bands", "USC surcharge", "USC self-employed", "USC medical card", "USC exemption", or any question about USC obligations. This skill covers standard rates and bands, the self-employed surcharge, exemptions, reduced rates for medical card holders and over-70s, and edge cases. ALWAYS read this skill before touching any Irish USC work.
version: 2.0
---

# Ireland Universal Social Charge (USC) -- Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Ireland |
| Authority | Revenue Commissioners |
| Primary legislation | Finance Act 2011 (as amended); TCA 1997, Part 18D |
| Supporting legislation | Finance Act 2024; Finance Act 2025 (Budget 2026) |
| Exemption threshold | EUR 13,000 (2025/2026) -- all-or-nothing |
| Self-employed surcharge | 3% on non-PAYE income > EUR 100,000 |
| Band 2 ceiling (2025) | EUR 27,382 |
| Band 2 ceiling (2026) | EUR 28,700 |
| Reduced rate cap (medical card / 70+) | 2.0% on income up to EUR 60,000 |
| Payment method | Self-assessment via Form 11 or PAYE at source |
| Currency | EUR only |
| Contributor | Open Accountants |
| Validated by | Pending -- licensed Irish practitioner sign-off required |
| Validation date | Pending |

**2025 bands:**

| Band | Income range | Rate |
|---|---|---|
| 1 | First EUR 12,012 | 0.5% |
| 2 | EUR 12,012.01 -- EUR 27,382 | 2.0% |
| 3 | EUR 27,382.01 -- EUR 70,044 | 3.0% |
| 4 | Above EUR 70,044 | 8.0% |

**2026 bands:**

| Band | Income range | Rate |
|---|---|---|
| 1 | First EUR 12,012 | 0.5% |
| 2 | EUR 12,012.01 -- EUR 28,700 | 2.0% |
| 3 | EUR 28,700.01 -- EUR 70,044 | 3.0% |
| 4 | Above EUR 70,044 | 8.0% |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any USC figure, you MUST obtain:

1. **Tax year** -- bands change annually
2. **Total income** -- USC is charged on gross income before pension contributions or other reliefs
3. **Is total income above or below EUR 13,000?** -- exemption test
4. **Does the client hold a full medical card?** -- reduced rates may apply
5. **Is the client aged 70 or over?** -- reduced rates may apply
6. **Does the client have non-PAYE income exceeding EUR 100,000?** -- surcharge
7. **Is there any DSP income?** -- exempt from USC charge but counted in exemption test

**If tax year is unknown, STOP. Do not compute USC.**

### Refusal catalogue

**R-IE-USC-1 -- Cross-border USC treatment.** Trigger: question about USC for non-residents or cross-border workers. Message: "Cross-border USC treatment requires specialist guidance. Escalate to qualified practitioner."

### Prohibitions

- NEVER compute USC without confirming the tax year
- NEVER apply USC to income at or below the EUR 13,000 exemption threshold
- NEVER forget that the exemption test uses TOTAL income but DSP payments are exempt from the charge itself
- NEVER apply reduced rates without confirming both medical card status AND income <= EUR 60,000
- NEVER omit the 3% surcharge on non-PAYE income exceeding EUR 100,000
- NEVER conflate USC with PRSI or income tax -- three separate charges
- NEVER state that USC is deductible for income tax purposes -- it is NOT
- NEVER apply income tax credits against USC

---

## Section 3 -- Exemption test

**Legislation:** TCA 1997, s 531AN

| Total income | USC liability |
|---|---|
| <= EUR 13,000 | Fully exempt |
| > EUR 13,000 | USC on ENTIRE income (not just excess) |

DSP payments are exempt from USC but are included in the income total for the exemption test.

---

## Section 4 -- Standard bands, surcharge, and reduced rates

### Self-employed surcharge

| Condition | Surcharge |
|---|---|
| Non-PAYE income > EUR 100,000 | Additional 3% on excess |
| Non-PAYE income <= EUR 100,000 | No surcharge |

Effective USC rate on non-PAYE income above EUR 100,000 = 8% + 3% = 11%.

### Formula (2026)

```
USC = (EUR 12,012 x 0.5%)
    + ((EUR 28,700 - EUR 12,012) x 2.0%)
    + ((EUR 70,044 - EUR 28,700) x 3.0%)
    + ((min(total_income, EUR 100,000) - EUR 70,044) x 8.0%)
    + ((total_income - EUR 100,000) x 11.0%)  [if non-PAYE > 100,000]
```

### Reduced rates (medical card / aged 70+)

| Condition | Relief |
|---|---|
| Full medical card AND income <= EUR 60,000 | Max 2.0% on all income |
| Aged 70+ AND income <= EUR 60,000 | Max 2.0% on all income |
| Either condition AND income > EUR 60,000 | Standard rates on income above EUR 60,000 |

Reduced rate bands: Band 1 at 0.5% on first EUR 12,012; Band 2 at 2.0% on remainder up to EUR 60,000. Relief extended through 31 December 2027.

---

## Section 5 -- USC and other charges interaction

| Question | Answer |
|---|---|
| Is USC deductible for income tax? | NO |
| Is USC part of PRSI? | NO -- entirely separate |
| Applied before or after tax credits? | USC on gross income; credits do not reduce USC |
| Does USC apply to DSP payments? | NO |
| Does USC apply to DIRT income? | NO -- deposit interest subject to DIRT is exempt |

---

## Section 6 -- Payment schedule

| Payment method | Detail |
|---|---|
| PAYE employees | Deducted at source by employer |
| Self-assessed | Included in preliminary tax (31 Oct / mid-Nov ROS) and balance on Form 11 |

---

## Section 7 -- Total marginal burden context

For self-employed individuals, USC combines with income tax and PRSI:

| Income level | Income tax | PRSI | USC | Combined |
|---|---|---|---|---|
| Below standard rate band | 20% | 4.125% | 0.5-2% | ~24-26% |
| Above EUR 70,044 | 40% | 4.125% | 8% | ~52% |
| Above EUR 100,000 (non-PAYE) | 40% | 4.125% | 11% | ~55% |

---

## Section 8 -- Edge case registry

### EC1 -- Income exactly EUR 13,000
**Situation:** Total income exactly EUR 13,000.
**Resolution:** Exempt. The threshold is "not exceeding EUR 13,000".

### EC2 -- Income EUR 13,001
**Situation:** Total income EUR 13,001.
**Resolution:** USC on full EUR 13,001. Band 1: EUR 60.06. Band 2: EUR 19.78. Total = EUR 79.84.

### EC3 -- Medical card holder with income EUR 61,000
**Situation:** Full medical card, income EUR 61,000.
**Resolution:** Exceeds EUR 60,000 limit. Standard rates apply. Flag for reviewer.

### EC4 -- Mixed PAYE and non-PAYE, surcharge test
**Situation:** EUR 80,000 PAYE + EUR 40,000 self-employment = EUR 120,000.
**Resolution:** Non-PAYE is EUR 40,000 (below EUR 100,000). No surcharge. Standard rates on full EUR 120,000.

### EC5 -- DSP income in exemption test
**Situation:** EUR 10,000 self-employment + EUR 4,000 Jobseeker's Benefit.
**Resolution:** Total for test = EUR 14,000 (exceeds EUR 13,000). USC charged on EUR 10,000 only.

### EC6 -- DIRT-subject deposit interest
**Situation:** EUR 5,000 deposit interest subject to DIRT.
**Resolution:** DIRT income exempt from USC. Exclude from calculation. Include in total for exemption test.

---

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified practitioner must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified practitioner. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard self-employed (2026)
**Input:** Total income EUR 50,000, age 45, no medical card.
**Expected output:** Band 1: EUR 60.06. Band 2: EUR 333.76. Band 3: EUR 639.00. Total = EUR 1,032.82.

### Test 2 -- Exempt
**Input:** Total income EUR 12,500, age 35.
**Expected output:** USC = EUR 0.

### Test 3 -- Surcharge applies (2026)
**Input:** Non-PAYE income EUR 150,000, age 50.
**Expected output:** Bands 1-4 on first EUR 100,000 = EUR 4,030.62. Surcharge: EUR 50,000 x 11% = EUR 5,500.00. Total = EUR 9,530.62.

### Test 4 -- Medical card holder, reduced rates
**Input:** Full medical card, total income EUR 40,000, age 72.
**Expected output:** Band 1: EUR 60.06. Band 2: EUR 27,988 x 2.0% = EUR 559.76. Total = EUR 619.82.

### Test 5 -- Just above exemption
**Input:** Total income EUR 13,001, age 30.
**Expected output:** Band 1: EUR 60.06. Band 2: EUR 19.78. Total = EUR 79.84.

### Test 6 -- DSP income in exemption test
**Input:** Self-employment EUR 10,000, DSP EUR 4,000, age 40.
**Expected output:** Total for test = EUR 14,000. USC on EUR 10,000 only. Band 1: EUR 50.00. Total = EUR 50.00.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CTA, AITI, or equivalent licensed practitioner in Ireland) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
