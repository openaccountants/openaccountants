---
name: ke-nhif-nssf
description: Use this skill whenever asked about Kenyan social contributions for self-employed individuals -- SHIF (formerly NHIF) health insurance and NSSF pension. Trigger on phrases like "NHIF self-employed", "SHIF contributions", "NSSF Tier I", "NSSF Tier II", "Kenya social security", "Kenya health insurance", or any question about Kenyan social contribution obligations for self-employed persons. Covers the SHIF 2.75% rate (replacing NHIF brackets from October 2024), NSSF Tier I/II structure, voluntary registration, and edge cases. ALWAYS read this skill before touching any Kenyan social contribution work.
version: 2.0
---

# Kenya SHIF (formerly NHIF) and NSSF Contributions -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Kenya |
| Health authority | SHA (Social Health Authority, replacing NHIF) |
| Pension authority | NSSF (National Social Security Fund) |
| Primary legislation | Social Health Insurance Act 2023 (SHIF); NSSF Act 2013 |
| SHIF rate | 2.75% of declared income |
| SHIF minimum | KES 300/month |
| SHIF maximum | No cap |
| NSSF self-employed | 12% of declared pensionable earnings (both portions) |
| NSSF Tier I ceiling | KES 8,000 (Lower Earnings Limit) |
| NSSF Tier II ceiling | KES 72,000 (Upper Earnings Limit) |
| NSSF maximum monthly | KES 8,640 |
| NSSF for self-employed | Voluntary |
| Payment deadline | 9th of following month |
| Currency | KES only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Kenyan CPA |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Employment status** -- self-employed, informal sector, or voluntary?
2. **Monthly declared income** -- determines SHIF and NSSF
3. **Registered with SHA?**
4. **Registered with NSSF?**
5. **Any formal employment alongside?** -- dual status
6. **Sector** -- formal vs informal

**If monthly income is unknown, request estimate. SHIF uses declared household income.**

### Refusal catalogue

**R-KE-SOC-1 -- Court challenges to SHIF.** Trigger: question about SHIF constitutionality. Message: "There have been multiple court challenges to the Social Health Insurance Act. Escalate -- do not advise on constitutional matters."

### Prohibitions

- NEVER use old NHIF brackets from October 2024 onward -- SHIF 2.75% applies
- NEVER tell self-employed that NSSF is mandatory -- it is voluntary for self-employed
- NEVER ignore KES 300 SHIF minimum
- NEVER assume NSSF uncapped -- Upper Earnings Limit KES 72,000 caps the base
- NEVER conflate SHIF household income with individual income without clarifying
- NEVER present old NSSF rates (pre-February 2025)
- NEVER assume foreign residents exempt from SHIF -- residency triggers obligation

---

## Section 3 -- SHIF (replacing NHIF)

**Legislation:** Social Health Insurance Act 2023 (effective October 2024)

| Item | Old (NHIF) | New (SHIF, from Oct 2024) |
|---|---|---|
| Rate | Fixed brackets (KES 150-1,700) | 2.75% of income |
| Self-employed | Flat KES 500 | 2.75% of declared household income |
| Minimum | KES 150 | KES 300 |
| Maximum | KES 1,700 | No cap |

```
shif_monthly = max(declared_monthly_income x 2.75%, KES 300)
```

---

## Section 4 -- NSSF contributions

**Legislation:** NSSF Act 2013 (effective February 2025)

### Self-employed NSSF

| Item | Detail |
|---|---|
| Registration | Voluntary |
| Self-employed pays | Both employee and employer portions (total 12%) |
| Minimum (Tier I only) | KES 960 |
| Maximum (Tier I + II) | KES 8,640 |

```
tier_i = min(declared_income, KES 8,000) x 6% x 2
tier_ii = max(0, min(declared_income, KES 72,000) - KES 8,000) x 6% x 2
total_nssf = tier_i + tier_ii
```

---

## Section 5 -- Computation examples

| Declared income | SHIF | NSSF Tier I | NSSF Tier II | Total NSSF | Grand total |
|---|---|---|---|---|---|
| KES 5,000 | KES 300 (min) | KES 600 | KES 0 | KES 600 | KES 900 |
| KES 50,000 | KES 1,375 | KES 960 | KES 5,040 | KES 6,000 | KES 7,375 |
| KES 200,000 | KES 5,500 | KES 960 | KES 7,680 | KES 8,640 | KES 14,140 |

---

## Section 6 -- Payment, registration, and tax interaction

### Payment schedule

| Contribution | Due date | Frequency |
|---|---|---|
| SHIF | 9th of following month | Monthly |
| NSSF | 9th of following month | Monthly |

Payment via M-Pesa, bank deposit, or online portals.

### Registration

SHIF mandatory for all residents. NSSF voluntary for self-employed. KRA PIN required.

### Tax interaction

| Question | Answer |
|---|---|
| SHIF deductible? | YES -- insurance relief (15% of premiums, capped KES 60,000/year) |
| NSSF deductible? | YES -- pension relief up to KES 30,000/month |
| Where reported? | iTax annual return |

### Penalties

| | SHIF | NSSF |
|---|---|---|
| Late payment | 2.5%/month | 5%/month |
| Non-registration | Denial of healthcare | Loss of benefits |

---

## Section 7 -- NHIF-to-SHIF transition and household income

### Transition

From October 2024, all NHIF members transitioned to SHIF. May involve re-registration with SHA.

### Household income declaration

SHIF for self-employed in informal sector is based on "household income." Definition of how spousal income is factored is still being clarified by SHA. Flag for reviewer.

---

## Section 8 -- Edge case registry

### EC1 -- Informal sector, irregular income
**Situation:** Jua kali worker, no fixed income.
**Resolution:** Declare average estimate. Minimum KES 300 SHIF applies. Flag for reviewer.

### EC2 -- Self-employed with formal employment
**Situation:** Employed (employer deducts SHIF/NSSF) and self-employed.
**Resolution:** Employer handles employment contributions. Additional SHIF may be due on self-employed income. NSSF may be maxed through employment.

### EC3 -- Income above NSSF Upper Limit
**Situation:** Income KES 200,000.
**Resolution:** NSSF capped at KES 8,640. SHIF = KES 5,500 (no cap).

### EC4 -- Non-citizen resident
**Situation:** Foreign national, self-employed in Kenya.
**Resolution:** SHIF applies to all residents. NSSF voluntary. Flag for reviewer.

### EC5 -- Minimum income
**Situation:** Declared KES 5,000.
**Resolution:** SHIF = KES 300 (minimum). NSSF voluntary.

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
Action Required: Qualified accountant must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified accountant. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Moderate income
**Input:** Declared KES 50,000. SHIF + NSSF. 2025.
**Expected output:** SHIF KES 1,375. NSSF KES 6,000. Total KES 7,375.

### Test 2 -- Minimum income
**Input:** Declared KES 5,000. SHIF only.
**Expected output:** SHIF KES 300 (minimum).

### Test 3 -- High income, NSSF capped
**Input:** Declared KES 200,000. Both.
**Expected output:** SHIF KES 5,500. NSSF KES 8,640. Total KES 14,140.

### Test 4 -- Dual status
**Input:** Employment KES 80,000, self-employed KES 40,000.
**Expected output:** Employer handles employment. Additional SHIF KES 1,100 on self-employed. NSSF likely maxed.

### Test 5 -- Informal sector
**Input:** Estimated KES 10,000. SHIF only.
**Expected output:** SHIF KES 300 (minimum; 2.75% = KES 275, below minimum).

### Test 6 -- NSSF at Lower Earnings Limit
**Input:** Declared KES 8,000. NSSF only.
**Expected output:** Tier I only. KES 960.

### Test 7 -- NSSF only, no SHIF
**Input:** KES 30,000, voluntary NSSF, no SHIF registration.
**Expected output:** NSSF KES 3,600. Advise to register for SHIF (mandatory).

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
