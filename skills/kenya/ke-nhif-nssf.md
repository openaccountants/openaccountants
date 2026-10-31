---
name: ke-nhif-nssf
description: Use this skill whenever asked about Kenyan social contributions for self-employed individuals -- SHIF (formerly NHIF) health insurance and NSSF pension. Trigger on phrases like "NHIF self-employed", "SHIF contributions", "NSSF Tier I", "NSSF Tier II", "Kenya social security", "Kenya health insurance", or any question about Kenyan social contribution obligations for self-employed persons. Covers the SHIF 2.75% rate (replacing NHIF brackets from October 2024), NSSF Tier I/II structure, voluntary registration, and edge cases. ALWAYS read this skill before touching any Kenyan social contribution work.
version: 2.1
jurisdiction: KE
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# KE Nhif Nssf

## Kenya SHIF (formerly NHIF) and NSSF Contributions -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Kenya |
| Health authority | SHA (Social Health Authority, replacing NHIF) |
| Pension authority | NSSF (National Social Security Fund) |
| Primary legislation | Social Health Insurance Act 2023 (SHIF); NSSF Act 2013 |
| SHIF rate | 2.75% of declared income |
| SHIF minimum | KES 300/month |
| SHIF maximum | No cap |
| NSSF self-employed | 12% of declared pensionable earnings (both portions) |
| NSSF Tier I ceiling | KES 9,000 (Lower Earnings Limit, Year 4, from February 2026) |
| NSSF Tier II ceiling | KES 108,000 (Upper Earnings Limit, Year 4, from February 2026) |
| NSSF maximum monthly | KES 12,960 |
| NSSF for self-employed | Voluntary |
| Payment deadline | 9th of following month |
| Currency | KES only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Kenyan CPA |
| Validation date | Pending |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Required inputs before computing**: Before computing, you MUST obtain: 1. Employment status -- self-employed, informal sector, or voluntary? 2. Monthly declared income -- determines SHIF and NSSF 3. Registered with SHA? 4. Registered with NSSF? 5. Any formal employment alongside? -- dual status 6. Sector -- formal vs informal. If monthly income is unknown, request estimate. SHIF uses declared household income.

### Refusal catalogue

- **R-KE-SOC-1**: There have been multiple court challenges to the Social Health Insurance Act. Escalate -- do not advise on constitutional matters. (Trigger: question about SHIF constitutionality.)

### Prohibitions

- **Prohibitions list**: NEVER use old NHIF brackets from October 2024 onward -- SHIF 2.75% applies. NEVER tell self-employed that NSSF is mandatory -- it is voluntary for self-employed. NEVER ignore KES 300 SHIF minimum. NEVER assume NSSF uncapped -- Upper Earnings Limit KES 108,000 caps the base. NEVER conflate SHIF household income with individual income without clarifying. NEVER present old NSSF limits (pre-February 2026: KES 8,000 / KES 72,000 / KES 8,640). NEVER assume foreign residents exempt from SHIF -- residency triggers obligation.

## Section 3 -- SHIF (replacing NHIF)

- **Legislation**: Social Health Insurance Act 2023 (effective October 2024)  _(Social Health Insurance Act 2023)_

**SHIF Old vs New comparison**  _(Social Health Insurance Act 2023)_

| Item | Old (NHIF) | New (SHIF, from Oct 2024) |
| --- | --- | --- |
| Rate | Fixed brackets (KES 150-1,700) | 2.75% of income |
| Self-employed | Flat KES 500 | 2.75% of declared household income |
| Minimum | KES 150 | KES 300 |
| Maximum | KES 1,700 | No cap |

- **SHIF monthly formula**: shif_monthly = max(declared_monthly_income x 2.75%, KES 300)  _(Social Health Insurance Act 2023)_

## Section 4 -- NSSF contributions

- **Legislation**: NSSF Act 2013, Third Schedule, Year 4 limits from February 2026  _([Year 4 notice](https://gaa.go.ke/sites/default/files/2026-02/Notice%20To%20Employers%20%E2%80%94%20Year%204%20%282026%29%20NSSF%20Contribution%20Rates%20.pdf), read 2026-10-31)_

### Self-employed NSSF

**Self-employed NSSF table**  _(NSSF Act 2013)_

| Item | Detail |
| --- | --- |
| Registration | Voluntary |
| Self-employed pays | Both employee and employer portions (total 12%) |
| Minimum (Tier I only) | KES 1,080 |
| Maximum (Tier I + II) | KES 12,960 |

- **NSSF Tier I/II formula**: tier_i = min(declared_income, KES 9,000) x 6% x 2 tier_ii = max(0, min(declared_income, KES 108,000) - KES 9,000) x 6% x 2 total_nssf = tier_i + tier_ii  _(NSSF Act 2013)_

## Section 5 -- Computation examples

**Computation examples table**

| Declared income | SHIF | NSSF Tier I | NSSF Tier II | Total NSSF | Grand total |
| --- | --- | --- | --- | --- | --- |
| KES 5,000 | KES 300 (min) | KES 600 | KES 0 | KES 600 | KES 900 |
| KES 50,000 | KES 1,375 | KES 1,080 | KES 4,920 | KES 6,000 | KES 7,375 |
| KES 200,000 | KES 5,500 | KES 1,080 | KES 11,880 | KES 12,960 | KES 18,460 |

```oa-check
name: Declared KES 50,000 a month, SHIF and NSSF Year 4
inputs:
  income: 50000
steps:
  - shif: max(income * 0.0275, 300)
  - tier_i: min(income, 9000) * 0.12
  - tier_ii: max(0, min(income, 108000) - 9000) * 0.12
  - total: shif + tier_i + tier_ii
expected:
  shif: 1375
  total: 7375
```

```oa-check
name: Declared KES 200,000 a month, NSSF at the Year 4 cap
inputs:
  income: 200000
steps:
  - shif: max(income * 0.0275, 300)
  - nssf: min(income, 9000) * 0.12 + max(0, min(income, 108000) - 9000) * 0.12
  - total: shif + nssf
expected:
  nssf: 12960
  total: 18460
```

## Section 6 -- Payment, registration, and tax interaction

### Payment schedule

**Payment schedule table**

| Contribution | Due date | Frequency |
| --- | --- | --- |
| SHIF | Unverified for self-employed members; confirm with SHA | Unverified |
| NSSF | 9th of following month | Monthly |

Payment via M-Pesa, bank deposit, or online portals.

### Registration

- **Registration requirements**: SHIF mandatory for all residents. NSSF voluntary for self-employed. KRA PIN required.

### Tax interaction

**Tax interaction table**

| Question | Answer |
| --- | --- |
| SHIF deductible? | YES -- deduction under ITA s15(2)(ae) ([KRA PAYE page](https://www.kra.go.ke/individual/filing-paying/types-of-taxes/paye)). Insurance relief does not apply ([KRA notice 8 Nov 2024](https://www.kra.go.ke/news-center/public-notices/2152-applicability-of-insurance-relief-to-contributions-made-to-the-social-health-insurance-fund-shif)) |
| NSSF deductible? | YES -- pension relief up to KES 30,000/month |
| Where reported? | iTax annual return |

### Penalties

**Penalties table**

|  | SHIF | NSSF |
| --- | --- | --- |
| Late payment | Unverified; confirm with SHA | 5%/month |
| Non-registration | Unverified; confirm with SHA | Loss of benefits |

## Section 7 -- NHIF-to-SHIF transition and household income

### Transition

From October 2024, all NHIF members transitioned to SHIF. May involve re-registration with SHA.

### Household income declaration

SHIF for self-employed in informal sector is based on "household income." Definition of how spousal income is factored is still being clarified by SHA. Flag for reviewer.

## Section 8 -- Edge case registry

### EC1 -- Informal sector, irregular income

Situation: Jua kali worker, no fixed income.
Resolution: Declare average estimate. Minimum KES 300 SHIF applies. Flag for reviewer.

### EC2 -- Self-employed with formal employment

Situation: Employed (employer deducts SHIF/NSSF) and self-employed.
Resolution: Employer handles employment contributions. Additional SHIF may be due on self-employed income. NSSF may be maxed through employment.

### EC3 -- Income above NSSF Upper Limit

Situation: Income KES 200,000.
Resolution: NSSF capped at KES 12,960. SHIF = KES 5,500 (no cap).

### EC4 -- Non-citizen resident

Situation: Foreign national, self-employed in Kenya.
Resolution: SHIF applies to all residents. NSSF voluntary. Flag for reviewer.

### EC5 -- Minimum income

Situation: Declared KES 5,000.
Resolution: SHIF = KES 300 (minimum). NSSF voluntary.

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

## Section 10 -- Test suite

### Test 1 -- Moderate income

Input: Declared KES 50,000. SHIF + NSSF. 2025.
Expected output: SHIF KES 1,375. NSSF KES 6,000. Total KES 7,375.

### Test 2 -- Minimum income

Input: Declared KES 5,000. SHIF only.
Expected output: SHIF KES 300 (minimum).

### Test 3 -- High income, NSSF capped

Input: Declared KES 200,000. Both.
Expected output: SHIF KES 5,500. NSSF KES 12,960. Total KES 18,460.

### Test 4 -- Dual status

Input: Employment KES 80,000, self-employed KES 40,000.
Expected output: Employer handles employment. Additional SHIF KES 1,100 on self-employed. NSSF likely maxed.

### Test 5 -- Informal sector

Input: Estimated KES 10,000. SHIF only.
Expected output: SHIF KES 300 (minimum; 2.75% = KES 275, below minimum).

### Test 6 -- NSSF at Lower Earnings Limit

Input: Declared KES 9,000. NSSF only.
Expected output: Tier I only. KES 1,080.

### Test 7 -- NSSF only, no SHIF

Input: KES 30,000, voluntary NSSF, no SHIF registration.
Expected output: NSSF KES 3,600. Advise to register for SHIF (mandatory).

## Sources

1. KRA PAYE page, read 2026-10-31 -- https://www.kra.go.ke/individual/filing-paying/types-of-taxes/paye
2. KRA public notice on insurance relief and SHIF, 8 November 2024, read 2026-10-31 -- https://www.kra.go.ke/news-center/public-notices/2152-applicability-of-insurance-relief-to-contributions-made-to-the-social-health-insurance-fund-shif
3. NSSF Year 4 notice to employers, read 2026-10-31 -- https://gaa.go.ke/sites/default/files/2026-02/Notice%20To%20Employers%20%E2%80%94%20Year%204%20%282026%29%20NSSF%20Contribution%20Rates%20.pdf

Not yet confirmed: self-employed SHIF payment timing and SHIF penalties.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
