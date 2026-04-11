---
name: bermuda-tax
description: Use this skill whenever asked about Bermuda taxation, payroll tax, customs duties, or the absence of income tax and VAT in Bermuda. Trigger on phrases like "Bermuda tax", "Bermuda VAT", "Bermuda payroll tax", "Bermuda customs", or any request involving Bermuda tax compliance. Bermuda does NOT have income tax, capital gains tax, or VAT. Revenue is raised through payroll tax, customs duties, and various fees. ALWAYS read this skill before handling any Bermuda tax work.
---

# Bermuda Tax Compliance Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Bermuda |
| Jurisdiction Code | BM |
| Primary Legislation | Payroll Tax Act 1995 (as amended); Customs Tariff Act 1970 |
| Supporting Legislation | Companies Act 1981; Land Tax Act 1967; Stamp Duties Act 1976 |
| Tax Authority | Office of the Tax Commissioner |
| Filing Portal | https://www.tax.gov.bm |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: no income tax/VAT status, payroll tax rates, customs duties. Tier 2: payroll tax exemptions, concessions for exempt companies, land tax. Tier 3: international structures, insurance sector-specific rules, economic substance requirements. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

---

## Step 0: Tax Landscape Overview [T1]

Bermuda is a NO-TAX jurisdiction for income and consumption purposes:

| Tax Type | Status |
|----------|--------|
| Income Tax (personal) | **None** |
| Income Tax (corporate) | **None** |
| Capital Gains Tax | **None** |
| Value Added Tax (VAT) | **None** |
| Sales Tax | **None** |
| Withholding Tax | **None** |
| Payroll Tax | **Yes** -- primary revenue source |
| Customs Duties | **Yes** -- on imports |
| Land Tax | **Yes** -- on property |
| Stamp Duty | **Yes** -- on real estate transfers and certain documents |
| Social Insurance | **Yes** -- contributory pension scheme |

**Bermuda has a legislative guarantee (Tax Assurance Certificate) that no income, capital gains, or withholding taxes will be introduced before 2035.** [T1]

---

## Step 1: Payroll Tax [T1]

### Overview

Payroll tax is Bermuda's primary source of government revenue. It is levied on remuneration paid to employees.

### Rates (Current) [T1]

| Component | Rate |
|-----------|------|
| Employer portion | 10.25% for exempted undertakings (international businesses); sliding scale for local employers based on payroll size |
| Employee portion | Sliding scale: 0.50% (up to BMD 48,000), 9.25% (BMD 48,001-96,000), 10.00% (BMD 96,001-200,000), 11.50% (BMD 200,001-500,000), 12.50% (BMD 500,001-1,000,000) |

### Employer Rate Tiers [T1]

| Annual Payroll | Employer Rate |
|----------------|---------------|
| Up to BMD 200,000 | Reduced rate (concession) |
| BMD 200,001 - BMD 350,000 | Intermediate rate |
| BMD 350,001 - BMD 500,000 | Standard rate |
| Above BMD 500,000 | Standard rate (10.25%) |

**Note [T2]:** Exact rate bands and thresholds are adjusted periodically by the Bermuda Budget. Always verify current rates with the Office of the Tax Commissioner.

### Employee Rate [T1]

| Annual Remuneration | Employee Rate |
|---------------------|---------------|
| Up to BMD 48,000 | Lower rate |
| BMD 48,001 - BMD 96,000 | Standard rate |
| Above BMD 96,000 | Maximum rate (capped at BMD amount) |

### Tax Cap [T1]

- Payroll tax is capped at BMD 1,000,000 per person per year -- remuneration above this is not subject to payroll tax [T1]
- The cap is set in each annual Budget [T2]

### Exempt Employers [T2]

Certain entities may receive payroll tax concessions or exemptions:
- Hotels and tourism sector (reduced rates) [T2]
- New businesses (temporary concessions) [T2]
- Charitable organizations [T2]

**Flag for practitioner: concession eligibility must be confirmed with Tax Commissioner.**

### Filing and Payment [T1]

| Requirement | Detail |
|-------------|--------|
| Filing frequency | Quarterly |
| Q1 deadline | April 15 |
| Q2 deadline | July 15 |
| Q3 deadline | October 15 |
| Q4 deadline | January 15 |
| Annual reconciliation | March 15 following year-end |
| Method | Electronic via tax.gov.bm |

---

## Step 2: Customs Duties [T1]

### Overview

Customs duties are levied on goods imported into Bermuda. There is no domestic manufacturing base, so virtually all goods are imported and subject to duty.

### Standard Rates [T1]

| Category | Duty Rate |
|----------|-----------|
| General merchandise | 22.25% - 25% (varies by category; 25% for electronics/household goods; 22.25% for most other goods) |
| Food items | 0% - 10% (many essentials at lower rates) |
| Clothing and footwear | 6.5% |
| Building materials | Variable |
| Motor vehicles | 33.5% (standard) |
| Fuel | Specific rates per unit |
| Alcohol | Specific rates per unit (high) |
| Tobacco | Specific rates per unit (high) |
| Prescription medications | 0% |

**Note [T2]:** Rates are adjusted periodically. Confirm current rates with Bermuda Customs.

### Customs Duty Relief [T2]

- Certain imports may qualify for duty relief or exemption
- Diplomatic imports: exempt
- Personal effects (returning residents): conditions apply
- Temporary imports: conditions apply

---

## Step 3: Land Tax [T1]

### Overview

Land tax is assessed on the annual rental value (ARV) of land and buildings.

### Rates [T1]

| ARV Band | Rate |
|----------|------|
| First BMD 11,000 | Lower rate |
| BMD 11,001 - BMD 22,000 | Progressive rate |
| Above BMD 22,000 | Higher rates (progressive) |

**Note [T2]:** Rates and bands are adjusted periodically. Tourist properties and commercial properties may have different rate structures.

### Filing [T1]

- Assessed annually by the Land Valuation Department
- Payable in instalments (quarterly or semi-annually)

---

## Step 4: Stamp Duty [T1]

### Real Estate Transfers

| Transaction Value | Rate |
|-------------------|------|
| First BMD 100,000 | 2% |
| BMD 100,001 - BMD 500,000 | 4% |
| BMD 500,001 - BMD 1,000,000 | 6% |
| Above BMD 1,000,000 | 8% |

### Other Documents [T1]

- Insurance policies: specific rates
- Mortgages: specific rates
- Share transfers: specific rates

---

## Step 5: Social Insurance [T1]

### Contributory Pension Fund

| Component | Rate |
|-----------|------|
| Employer contribution | BMD 35.69 per week per employee |
| Employee contribution | BMD 35.69 per week per employee |
| Self-employed | BMD 63.10 per week |

**Note [T2]:** Rates are adjusted annually. Confirm current rates.

---

## Step 6: Economic Substance [T2]

Bermuda enacted economic substance legislation effective January 2019:

- Entities carrying on "relevant activities" must demonstrate adequate economic substance in Bermuda
- Relevant activities include: banking, insurance, fund management, financing and leasing, headquarters, shipping, distribution and service centre, intellectual property, holding entity
- Substance requirements: decision-making in Bermuda, adequate employees, adequate expenditure, physical presence

**Flag for practitioner: economic substance compliance is [T3] -- requires specialist advice.**

---

## PROHIBITIONS [T1]

- NEVER state that Bermuda has income tax -- it does not
- NEVER state that Bermuda has VAT or sales tax -- it does not
- NEVER apply VAT calculations to Bermuda transactions
- NEVER apply income tax calculations to Bermuda entities
- NEVER ignore payroll tax obligations (primary compliance requirement)
- NEVER assume payroll tax rates without confirming current Budget rates
- NEVER guess economic substance requirements -- escalate to [T3]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not AI

---

## Step 7: Edge Case Registry

### EC1 -- International company with Bermuda employees [T1]
**Situation:** US company has employees working in Bermuda.
**Resolution:** Payroll tax applies on all remuneration paid to employees working in Bermuda, regardless of employer's domicile. Register with Tax Commissioner and remit payroll tax quarterly.

### EC2 -- E-commerce sales to Bermuda [T1]
**Situation:** Online retailer ships goods to Bermuda customer.
**Resolution:** No VAT or sales tax applies. Customs duties apply on import. The recipient pays customs duty when goods arrive in Bermuda.

### EC3 -- Exempt company payroll [T2]
**Situation:** Bermuda-exempted company (international business) employs staff.
**Resolution:** Payroll tax applies to all employers including exempt companies. Exempt company status relates to Companies Act provisions, NOT tax exemptions on payroll tax. Verify if any concession rates apply.

### EC4 -- Self-employed individual [T1]
**Situation:** Self-employed person in Bermuda.
**Resolution:** No income tax applies. Social insurance contributions (contributory pension) are required. No payroll tax on self-employment income (payroll tax applies to employer-employee relationships only).

---

## Step 8: Test Suite

### Test 1 -- Income tax question
**Input:** "What income tax does a Bermuda company pay?"
**Expected output:** None. Bermuda does not impose corporate income tax. Tax Assurance Certificate guarantees no income tax before 2035.

### Test 2 -- VAT question
**Input:** "What is the VAT rate in Bermuda?"
**Expected output:** Bermuda does not have VAT or any sales tax.

### Test 3 -- Payroll tax calculation
**Input:** Employer with annual payroll BMD 600,000, 10 employees.
**Expected output:** Employer pays payroll tax at the standard rate (10.25% on total payroll, subject to current Budget rates). Employee portion deducted from each employee's pay. File quarterly.

### Test 4 -- Import of goods
**Input:** Bermuda resident imports electronics valued at BMD 5,000.
**Expected output:** Customs duty at applicable rate (general merchandise 22.25%). Duty = BMD 1,112.50. No VAT. No sales tax.

---

## Step 9: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Bermuda practitioner must confirm.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed practitioner. Document gap.
```

---

## Contribution Notes

Bermuda is a no-income-tax, no-VAT jurisdiction. Key compliance areas:
1. Payroll tax is the primary tax obligation for employers
2. Customs duties apply to virtually all imported goods
3. Land tax applies to property owners
4. Economic substance requirements apply to relevant entities (since 2019)
5. No double taxation treaties (except for specific arrangements with the US regarding insurance)

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
