---
name: bvi-tax
description: Use this skill whenever asked about British Virgin Islands (BVI) taxation, payroll tax, or the absence of income tax and VAT. Trigger on phrases like "BVI tax", "British Virgin Islands tax", "BVI VAT", "BVI payroll tax", or any request involving BVI tax compliance. BVI does NOT have income tax, capital gains tax, or VAT. The primary tax is payroll tax. Revenue also comes from financial services fees and customs duties. ALWAYS read this skill before handling any BVI tax work.
---

# British Virgin Islands (BVI) Tax Compliance Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | British Virgin Islands (BVI) |
| Jurisdiction Code | VG |
| Primary Legislation | Payroll Taxes Act, 2004 (as amended); Customs Management and Duties Act |
| Supporting Legislation | BVI Business Companies Act, 2004; Economic Substance (Companies and Limited Partnerships) Act, 2018 |
| Tax Authority | Inland Revenue Department (IRD) |
| Filing Portal | https://www.bvi.gov.vg/departments/inland-revenue-department |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: no income tax/VAT status, payroll tax rates, customs duties. Tier 2: payroll tax exemptions, concessions. Tier 3: economic substance, international reporting, complex structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

---

## Step 0: Tax Landscape Overview [T1]

BVI is a NO INCOME TAX, NO VAT jurisdiction:

| Tax Type | Status |
|----------|--------|
| Income Tax (personal) | **None** |
| Income Tax (corporate) | **None** |
| Capital Gains Tax | **None** |
| Value Added Tax (VAT) | **None** |
| Sales Tax | **None** |
| Withholding Tax | **None** |
| Payroll Tax | **Yes** -- on employee remuneration |
| Customs Duties | **Yes** -- on imports |
| Property Tax | **Yes** -- on land and buildings |
| Stamp Duty | **Yes** -- on certain transactions |
| Social Security (NHI) | **Yes** -- National Health Insurance |
| Social Security (SSB) | **Yes** -- Social Security Board contributions |

---

## Step 1: Payroll Tax [T1]

### Overview

Payroll tax is the primary direct tax in BVI, levied on remuneration paid to employees.

### Rates [T1]

Payroll tax rates depend on employer classification:

**Class 1 Employer** (7 or fewer employees, annual payroll not exceeding USD 150,000, annual revenue not exceeding USD 300,000):

| Component | Rate |
|-----------|------|
| Employer portion | 2% |
| Employee portion | 8% |
| **Total** | **10%** |

**Class 2 Employer** (all others):

| Component | Rate |
|-----------|------|
| Employer portion | 6% |
| Employee portion | 8% |
| **Total** | **14%** |

**Employee exemption:** The first USD 10,000 of each employee's annual remuneration is exempt from payroll tax.

### Scope [T1]

- Applies to all remuneration paid to employees for services performed in BVI [T1]
- Includes salaries, wages, bonuses, commissions, benefits in kind [T1]
- Applies regardless of whether employer is incorporated in BVI or overseas [T1]

### Exemptions [T2]

- Certain categories of employment may have reduced rates
- Small business concessions may apply
- Flag for practitioner: confirm current exemptions and concessions with IRD

### Filing and Payment [T1]

| Requirement | Detail |
|-------------|--------|
| Filing frequency | Monthly |
| Deadline | 15th of the month following the payroll month |
| Annual reconciliation | March 31 following year-end |
| Method | Through IRD |
| Currency | USD (BVI uses US dollar) |

### Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing | USD 50 per day |
| Late payment | 1.5% per month on unpaid amount |
| Failure to register | Backdated assessment plus penalties |

---

## Step 2: No Income Tax / No VAT Confirmation [T1]

### Absolute Confirmation

- **No personal income tax** [T1]
- **No corporate income tax** [T1]
- **No capital gains tax** [T1]
- **No VAT or sales tax** [T1]
- **No withholding tax** on any payment [T1]
- **No estate or inheritance tax** [T1]
- **No net worth tax** [T1]

### BVI Business Companies [T1]

BVI Business Companies (BVI BCs) -- the most common corporate vehicle:
- No income tax on worldwide income [T1]
- No capital gains tax [T1]
- No dividends tax [T1]
- Annual government fee payable (not a tax, but a registration/maintenance fee) [T1]

### Government Fees for BVI BCs [T1]

| Authorized Share Capital | Annual Fee (USD) |
|--------------------------|-----------------|
| Up to 50,000 shares (no par) | 450 |
| 50,001+ shares | 1,200 |
| Shares with par value: up to USD 50,000 | 450 |
| Shares with par value: above USD 50,000 | 1,200 |

---

## Step 3: Customs Duties [T1]

### Overview

Customs duties apply to goods imported into BVI.

### Standard Rates [T1]

| Category | Duty Rate |
|----------|-----------|
| General merchandise | 5% - 20% |
| Food and essential goods | Lower rates or exempt |
| Motor vehicles | 20% + environmental levy |
| Alcohol | High specific rates |
| Tobacco | High specific rates |
| Building materials | 5% - 10% |
| Fuel | Specific rates |

**Note [T2]:** Rates subject to revision. Confirm with BVI Customs.

### Environmental Levy [T1]

An environmental levy applies to certain imported goods:
- Motor vehicles (based on age and engine size) [T1]
- Electronics and appliances [T1]
- Tires and batteries [T1]

---

## Step 4: Social Security [T1]

### Social Security Board (SSB) Contributions [T1]

| Component | Rate |
|-----------|------|
| Employer contribution | 4.5% of insurable earnings |
| Employee contribution | 4.5% of insurable earnings |
| **Total** | **9%** |
| Insurable earnings ceiling | Set annually by SSB |

### National Health Insurance (NHI) [T1]

| Component | Rate |
|-----------|------|
| Employer contribution | 3.75% of payroll |
| Employee contribution | 3.75% of payroll |
| **Total** | **7.5%** |

---

## Step 5: Property Tax [T1]

### Land and Building Tax

- Assessed on the annual rental value of property [T1]
- Rates set by government [T2]
- Applies to land and buildings in BVI [T1]

---

## Step 6: Stamp Duty [T1]

| Transaction | Rate |
|-------------|------|
| Real estate transfers | 4% buyer + 4% seller (standard) |
| Certain legal documents | Variable rates |
| Mortgages | 1.5% |

**Note [T2]:** First-time Belonger buyers may receive concessions. Confirm with practitioner.

---

## Step 7: Economic Substance [T2]

The Economic Substance (Companies and Limited Partnerships) Act, 2018 requires:

- Entities carrying on "relevant activities" must demonstrate adequate economic substance in BVI
- Relevant activities: banking, distribution and service centre, financing and leasing, fund management, headquarters, holding, insurance, intellectual property, shipping
- Requirements: directed and managed in BVI, adequate employees/expenditure, core income-generating activities conducted in BVI
- Annual reporting to the International Tax Authority (ITA)

**Flag for practitioner: economic substance compliance is [T3] -- requires specialist advice.**

---

## Step 8: International Reporting [T2]

### CRS (Common Reporting Standard)

- BVI participates in OECD CRS [T1]
- Financial institutions must report to the ITA [T1]

### FATCA

- BVI has a Model 1 IGA with the United States [T1]
- Financial institutions must report US account holders [T1]

### Beneficial Ownership

- Beneficial Ownership Secure Search System (BOSS) [T1]
- Registered agents must maintain beneficial ownership information [T1]

---

## Step 9: Key Thresholds

| Threshold | Value |
|-----------|-------|
| Payroll tax (employer) | 2% (Class 1) or 6% (Class 2) |
| Payroll tax (employee) | 8% |
| Payroll tax employee exemption | First USD 10,000 per year |
| SSB contributions (total) | 9% |
| NHI contributions (total) | 7.5% |
| Payroll tax filing | Monthly, 15th of following month |
| BVI BC annual fee (standard) | USD 450 |

---

## PROHIBITIONS [T1]

- NEVER state that BVI has income tax -- it does not
- NEVER state that BVI has VAT or sales tax -- it does not
- NEVER apply income tax or VAT calculations to BVI transactions
- NEVER ignore payroll tax obligations (primary compliance requirement)
- NEVER confuse government annual fees with taxes (they are registration fees)
- NEVER ignore economic substance reporting requirements for relevant entities
- NEVER ignore social security (SSB) and health insurance (NHI) contributions
- NEVER assume duty rates without confirming current schedule
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not AI

---

## Step 10: Edge Case Registry

### EC1 -- BVI BC with no local employees [T1]
**Situation:** BVI Business Company has no employees in BVI, only a registered agent.
**Resolution:** No payroll tax obligation (no payroll). Annual government fee still payable. Economic substance requirements still apply if conducting relevant activities. CRS/FATCA obligations apply if a financial institution.

### EC2 -- Employer with both Belonger and non-Belonger employees [T1]
**Situation:** BVI company employs a mix of local and work-permit holders.
**Resolution:** Payroll tax applies equally to all employees regardless of status. Rate is 6% employer (Class 2) + 8% employee on remuneration above the USD 10,000 annual exemption. SSB and NHI apply to all employees.

### EC3 -- International service provider with BVI clients [T1]
**Situation:** Non-BVI company provides services to BVI entity remotely.
**Resolution:** No BVI tax implications for the service provider (no income tax, no withholding). No VAT on the service. If the provider has employees in BVI, payroll tax applies to those employees.

### EC4 -- Real estate purchase by non-Belonger [T2]
**Situation:** Non-Belonger purchases property in BVI.
**Resolution:** Non-Belonger Land Holding Licence required. Stamp duty applies (4% buyer + 4% seller). Annual licence fees may apply. No capital gains tax on future sale. Flag for practitioner: licence requirements and additional fees.

### EC5 -- Fund administrator in BVI [T2]
**Situation:** Fund administration company operates in BVI with local staff.
**Resolution:** No income tax on fund administration fees. Payroll tax on employee remuneration (8% + 8%). Economic substance requirements for fund management activity. Annual fees to financial services regulator. Flag for practitioner: confirm substance requirements.

---

## Step 11: Test Suite

### Test 1 -- Income tax question
**Input:** "What income tax does a BVI company pay?"
**Expected output:** None. BVI does not impose corporate or personal income tax.

### Test 2 -- VAT question
**Input:** "What is the VAT rate in BVI?"
**Expected output:** BVI does not have VAT or any sales tax.

### Test 3 -- Payroll tax
**Input:** BVI employer pays monthly payroll of USD 50,000 to 5 employees. Class 2 employer.
**Expected output:** Employer payroll tax = 6%. Employee payroll tax = 8% (on remuneration above the USD 10,000 annual exemption per employee). Plus SSB 4.5% each + NHI 3.75% each. File by 15th of following month.

### Test 4 -- BVI BC annual obligations
**Input:** BVI Business Company with 10,000 no-par-value shares, no employees.
**Expected output:** Annual government fee USD 450. No income tax. No payroll tax (no employees). Economic substance filing required if conducting relevant activities.

---

## Step 12: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed BVI practitioner must confirm.
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

BVI is a no-income-tax, no-VAT jurisdiction. Key compliance areas:
1. Payroll tax (10% Class 1 or 14% Class 2 total) is the primary employer obligation
2. Social security (SSB 9%) and health insurance (NHI 7.5%) are mandatory
3. Annual government fees for BVI Business Companies
4. Economic substance requirements since 2019
5. CRS/FATCA reporting for financial institutions
6. BVI uses the US dollar as its currency

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
