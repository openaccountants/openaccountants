---
name: nz-acc-levies
description: >
  Use this skill whenever asked about New Zealand ACC levies for self-employed individuals. Trigger on phrases like "ACC levy", "earner levy", "work levy", "CoverPlus", "CoverPlus Extra", "accident compensation", "ACC invoice", "classification unit", or any question about ACC obligations for sole traders in New Zealand. Covers earner levy, work levy by classification unit (CU), CoverPlus/CoverPlus Extra, maximum liable earnings, and payment schedules. ALWAYS read this skill before touching any NZ ACC work.
version: 2.0
jurisdiction: NZ
tax_year: 2025
category: international
---

# NZ ACC Levies -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

Read this whole section before computing anything.

| Field | Value |
|---|---|
| Country | New Zealand |
| Jurisdiction Code | NZ |
| Primary Legislation | Accident Compensation Act 2001 (AC Act) |
| Supporting Legislation | Injury Prevention, Rehabilitation, and Compensation Act 2001 |
| Authority | Accident Compensation Corporation (ACC) |
| Filing Portal | myACC for Business (myacc.acc.co.nz) |
| Tax Year | 2025 (1 April 2025 -- 31 March 2026) |
| Currency | NZD only |
| Maximum Liable Earnings | $142,283 (approximate -- verify with ACC) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by NZ chartered accountant |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: earner levy rate, work levy computation, maximum liable earnings. Tier 2: CU selection, CoverPlus Extra, experience rating. Tier 3: claims management, dispute resolution, complex multi-business structures. |

**ACC levy components (2025/26):**

| Levy | Who Pays | Rate |
|---|---|---|
| Earner levy | All earners (including self-employed) | $1.67 per $100 (1.67%) |
| Work levy | Self-employed only | Varies by classification unit (CU) |
| Working Safer levy | Self-employed | ~$0.08 per $100 |

**Illustrative work levy rates by CU (2025/26):**

| CU Code | Industry | Work Levy (per $100) |
|---|---|---|
| 72100 | Computer consultancy | ~$0.08 |
| 69200 | Accounting services | ~$0.08 |
| 62000 | Software development | ~$0.09 |
| 52100 | General retail | ~$0.47 |
| 41100 | Building construction | ~$2.68 |
| 01600 | Dairy farming | ~$2.41 |
| 11200 | Forestry | ~$8.30 |

These rates are illustrative. Actual rates must be verified at acc.co.nz or on the client's ACC invoice.

**CoverPlus vs CoverPlus Extra:**

| Feature | CoverPlus (Default) | CoverPlus Extra |
|---|---|---|
| Compensation basis | 80% of liable earnings (prior year IR3) | Agreed level chosen by client |
| Levy basis | Actual earnings | Chosen cover amount |
| Adjustment | Adjusted when IR3 filed | Fixed at agreed level |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown CU code | Flag for reviewer -- CU determines work levy rate |
| Unknown CoverPlus option | CoverPlus (default) |
| Unknown GST status | GST-registered (levies are GST-exclusive, GST added) |
| Unknown liable earnings | Use most recent IR3 figure |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any ACC levy figure, you MUST know:

1. Self-employment status -- sole trader, partner, or shareholder-employee
2. Classification unit (CU) code -- determines work levy rate
3. Liable earnings -- net self-employment income from IR3 or IR7
4. CoverPlus or CoverPlus Extra -- which cover option is in place
5. Whether any experience rating applies -- claims history adjustment
6. Tax year -- ACC invoices based on prior year's earnings

If the client is a PAYE employee only, STOP. Employer pays ACC levies for employees.

### Refusal catalogue

**R-NZ-ACC-1 -- Claims management.** Trigger: client asks about managing an ACC claim or rehabilitation. Message: "ACC claims management and rehabilitation are outside this skill's scope. Please contact ACC directly at 0800 101 996."

**R-NZ-ACC-2 -- Dispute resolution.** Trigger: client disputes an ACC levy or classification. Message: "ACC levy disputes and CU reclassification require direct engagement with ACC. This skill cannot advise on dispute procedures. Please escalate to a qualified NZ chartered accountant."

**R-NZ-ACC-3 -- Complex multi-business structures.** Trigger: client has multiple business entities with different CUs. Message: "Multi-entity ACC structuring requires case-specific analysis. Please escalate to a qualified NZ chartered accountant."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement entries related to ACC. Match by case-insensitive substring.

### 3.1 ACC levy payments

| Pattern | Treatment | Notes |
|---|---|---|
| ACC, ACCIDENT COMPENSATION | ACC LEVY PAYMENT | Annual or instalment levy payment |
| ACC LEVY, ACC INVOICE | ACC LEVY PAYMENT | Same |
| ACC COVERPLUS, COVERPLUS EXTRA | ACC LEVY PAYMENT | CoverPlus or CoverPlus Extra invoice payment |

### 3.2 ACC provisional invoicing

| Pattern | Treatment | Notes |
|---|---|---|
| ACC PROVISIONAL, ACC ESTIMATE | PROVISIONAL LEVY | Based on most recent known earnings; adjusted once IR3 processed |
| ACC ADJUSTMENT, ACC REFUND | LEVY ADJUSTMENT | Difference between provisional and actual; may be refund or additional charge |

### 3.3 GST treatment

| Pattern | Treatment | Notes |
|---|---|---|
| ACC + GST component visible | GST INPUT CLAIM | ACC levies are GST-exclusive; GST added for registered persons; GST component claimable |

### 3.4 IRD payments (income return triggers ACC)

| Pattern | Treatment | Notes |
|---|---|---|
| IRD, INLAND REVENUE NZ | TAX PAYMENT | IR3 filing triggers ACC levy calculation |
| IR3 FILED | ACC TRIGGER | Once IR3 processed, ACC issues or adjusts invoice |

---

## Section 4 -- Levy computation rules

### 4.1 Levy computation steps (Tier 1)

Legislation: AC Act 2001, Schedule 1

| Step | Action |
|---|---|
| 4.1 | Determine liable earnings = net self-employment income from IR3 |
| 4.2 | Cap earnings at maximum liable earnings ($142,283) if applicable |
| 4.3 | Earner levy = liable earnings x $1.67 / $100 |
| 4.4 | Work levy = liable earnings x work levy rate for CU / $100 |
| 4.5 | Working Safer levy = liable earnings x $0.08 / $100 |
| 4.6 | Total ACC levy = earner levy + work levy + Working Safer levy |
| 4.7 | GST: levies are GST-exclusive; GST added if GST-registered |

### 4.2 CoverPlus (Default) (Tier 1)

Compensation basis: 80% of liable earnings (based on prior year IR3). Levies adjusted when tax return is filed.

### 4.3 CoverPlus Extra (Tier 2)

Compensation basis: agreed level chosen by self-employed person. Levy basis: chosen cover amount (not actual earnings). Must sign CoverPlus Extra agreement with ACC. Flag for reviewer: can result in higher or lower cover than actual earnings. Advise client to review annually.

---

## Section 5 -- Payment and invoicing

### 5.1 Invoicing (Tier 1)

| Detail | Value |
|---|---|
| Invoice timing | ACC sends invoice after IR3 is filed (typically September-November) |
| Payment options | Single payment, or instalments (2, 4, or monthly by arrangement) |
| Due date | As stated on ACC invoice (typically 30 days from issue) |
| Late payment | Penalties and interest apply |

### 5.2 Provisional invoicing (Tier 1)

If the IR3 has not yet been filed, ACC issues a provisional invoice based on the most recent known earnings. Adjusted once actual return is processed. Client may receive refund or additional invoice.

---

## Section 6 -- GST and deductibility

### 6.1 GST treatment (Tier 1)

ACC levies are GST-exclusive. If the self-employed person is GST-registered, ACC adds GST to the invoice. The GST component is claimable as input tax on the GST return.

### 6.2 Income tax deductibility (Tier 1)

ACC levies paid are deductible business expenses for income tax purposes. The earner levy and work levy are both deductible against business income.

---

## Section 7 -- Edge case registry

### EC1 -- Multiple business activities (Tier 2)
Situation: Client runs a software consultancy (CU 72100) and a construction side business (CU 41100).
Resolution: ACC assigns the CU based on the primary activity (>50% of time or income). If roughly equal, ACC may split or assign higher-risk CU. Flag for reviewer.

### EC2 -- First year of self-employment (Tier 1)
Situation: Client started freelancing in March 2025. No prior-year IR3.
Resolution: ACC will estimate levies or use the minimum. Once first IR3 is filed, levies are recalculated and adjusted.

### EC3 -- Self-employed AND employee (Tier 1)
Situation: Client has PAYE employment and a freelance side business.
Resolution: Earner levy on total earnings (both sources combined, up to maximum). Work levy applies only to self-employment income. PAYE employer covers work levy for employment income.

### EC4 -- Earnings exceed maximum (Tier 1)
Situation: Consultant earns $200,000 net self-employment income.
Resolution: Levies calculated on $142,283 (maximum), not $200,000. Weekly compensation if injured is also capped.

### EC5 -- Client disputes CU classification (Tier 2)
Situation: Client classified as "building construction" but primarily does office-based project management.
Resolution: Client can apply to ACC for CU reclassification. CU determines work levy rate and can significantly affect costs. Flag for reviewer.

### EC6 -- GST on ACC levies (Tier 1)
Situation: GST-registered sole trader receives ACC invoice.
Resolution: ACC levies are GST-exclusive. ACC adds GST to the invoice. GST component is claimable as input tax.

---

## Section 8 -- Reviewer escalation protocol

When a Tier 2 situation is identified:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified NZ chartered accountant must confirm before advising client.
```

When a Tier 3 situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified NZ chartered accountant. Document gap.
```

---

## Section 9 -- Test suite

### Test 1 -- Standard software consultant
Input: CU 72100, liable earnings $120,000, work levy rate $0.08/100.
Expected output: Earner levy: $2,004.00. Work levy: $96.00. Working Safer: $96.00. Total: ~$2,196.00 (excl. GST).

### Test 2 -- High earner hitting cap
Input: CU 69200, liable earnings $200,000, maximum $142,283.
Expected output: Capped at $142,283. Earner levy: $2,376.13. Work levy: $113.83. Working Safer: $113.83. Total: ~$2,603.79 (excl. GST).

### Test 3 -- Builder (high-risk CU)
Input: CU 41100, liable earnings $80,000, work levy rate $2.68/100.
Expected output: Earner levy: $1,336.00. Work levy: $2,144.00. Working Safer: $64.00. Total: ~$3,544.00 (excl. GST).

### Test 4 -- Low-income first-year freelancer
Input: CU 72100, liable earnings $25,000.
Expected output: Earner levy: $417.50. Work levy: $20.00. Working Safer: $20.00. Total: ~$457.50 (excl. GST).

---

## Section 10 -- Prohibitions and disclaimer

### Prohibitions

- NEVER assume work levy rates are the same for all industries -- they vary significantly by classification unit
- NEVER calculate levies on earnings above the maximum liable earnings cap
- NEVER confuse CoverPlus (default, based on actual earnings) with CoverPlus Extra (agreed amount)
- NEVER omit the earner levy -- it applies to ALL earners, not just self-employed
- NEVER forget GST treatment -- ACC levies are GST-exclusive; GST is added for registered persons
- NEVER use a work levy rate without verifying it against the current ACC levy guidebook or invoice
- NEVER present calculations as definitive -- always label as estimated and direct client to ACC or a qualified NZ chartered accountant

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
