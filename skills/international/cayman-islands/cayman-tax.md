---
name: cayman-tax
description: Use this skill whenever asked about Cayman Islands taxation or the absence of direct taxes. Trigger on phrases like "Cayman tax", "Cayman Islands VAT", "Cayman Islands income tax", "Cayman corporate tax", or any request involving Cayman Islands tax compliance. The Cayman Islands does NOT have income tax, capital gains tax, VAT, or any direct taxes. Revenue is raised through import duties, work permit fees, and financial services fees. ALWAYS read this skill before handling any Cayman Islands tax work.
---

# Cayman Islands Tax Compliance Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Cayman Islands |
| Jurisdiction Code | KY |
| Primary Legislation | Tax Concessions Act (Revised); Customs Tariff Act (Revised) |
| Supporting Legislation | Companies Act (Revised); Limited Liability Companies Act; Economic Substance Act, 2018 (as amended) |
| Tax Authority | No dedicated tax authority -- Department of Commerce and Investment; Customs and Border Control |
| Filing Portal | N/A -- no direct tax filing |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: no-tax status, import duties, work permits. Tier 2: economic substance requirements, financial services fees. Tier 3: international regulatory compliance, CRS/FATCA reporting, anti-money laundering. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

---

## Step 0: Tax Landscape Overview [T1]

The Cayman Islands is a TAX-NEUTRAL jurisdiction:

| Tax Type | Status |
|----------|--------|
| Income Tax (personal) | **None** |
| Income Tax (corporate) | **None** |
| Capital Gains Tax | **None** |
| Value Added Tax (VAT) | **None** |
| Sales Tax | **None** |
| Withholding Tax | **None** |
| Payroll Tax | **None** |
| Property Tax | **None** (no annual property tax) |
| Inheritance / Estate Tax | **None** |
| Import Duties | **Yes** -- on imported goods |
| Work Permit Fees | **Yes** -- for non-Caymanian workers |
| Financial Services Fees | **Yes** -- annual registration fees for entities |
| Stamp Duty | **Yes** -- on real estate transfers |
| Tourism Tax | **Yes** -- on hotel stays and cruise passengers |

**The Cayman Islands government can grant a Tax Undertaking Certificate guaranteeing no direct taxation for up to 50 years for exempted companies and 30 years for individuals.** [T1]

---

## Step 1: No Direct Taxes [T1]

### Confirmation

- **No income tax** of any kind -- personal or corporate [T1]
- **No capital gains tax** [T1]
- **No VAT or sales tax** [T1]
- **No withholding tax** on dividends, interest, royalties, or any payment [T1]
- **No payroll tax** [T1]
- **No property tax** (annual) [T1]
- **No estate or inheritance tax** [T1]
- **No profit tax, net worth tax, or turnover tax** [T1]

### Tax Undertaking Certificates [T1]

| Entity Type | Maximum Duration |
|-------------|-----------------|
| Exempted Company | 50 years |
| Exempted Limited Partnership | 50 years |
| Individual | 30 years |

These certificates guarantee that if direct taxes are ever introduced, the holder would be exempt for the certificate period.

---

## Step 2: Import Duties [T1]

### Overview

Import duties are the Cayman Islands' primary source of government revenue.

### Standard Rates [T1]

| Category | Duty Rate |
|----------|-----------|
| General merchandise | 22% - 27% (most common: 22%) |
| Food items | 15% - 22% |
| Motor vehicles | 29.5% (standard) |
| Luxury vehicles | 42% |
| Fuel | Specific rates per imperial gallon |
| Alcohol | High specific rates |
| Tobacco | High specific rates |
| Building materials | 15% - 22% |
| Personal effects | Varies |

**Note [T2]:** Rates are subject to change by government regulation. Confirm current rates with Customs and Border Control.

### Duty Concessions [T2]

- Certain imports may qualify for duty concessions
- Development agreements may include duty waivers
- Temporary imports for specific purposes: conditions apply
- Diplomatic and government imports: exempt

---

## Step 3: Work Permit Fees [T1]

### Overview

Non-Caymanian workers require work permits. Fees vary by category.

| Category | Annual Fee Range (KYD) |
|----------|----------------------|
| Key employee / senior | Higher fees |
| Professional / skilled | Moderate fees |
| Unskilled / manual | Lower fees |

**Note [T2]:** Work permit fees are adjusted periodically. Employer pays the fee. The fee schedule is maintained by the Workforce Opportunities and Residency Cayman (WORC).

---

## Step 4: Financial Services Fees [T1]

### Annual Registration/Licensing Fees

All entities registered in the Cayman Islands pay annual fees:

| Entity Type | Annual Fee (approx. KYD) |
|-------------|-------------------------|
| Exempted company | 850 - 3,000+ |
| Exempted limited partnership | 750 - 2,500+ |
| Foreign company (registered) | 1,500+ |
| Mutual fund (regulated) | 3,000 - 4,000+ |
| Insurance company (Class A-D) | Variable, significant |
| Trust company | Variable |

**Note [T2]:** Fees are subject to periodic revision. Confirm current fees with the relevant registrar (Companies Registry, CIMA for regulated entities).

---

## Step 5: Stamp Duty [T1]

### Real Estate Transfers

| Transaction | Rate |
|-------------|------|
| Transfer of land/property | 7.5% of consideration or market value |
| Transfer of strata lot | 7.5% |
| First-time Caymanian buyer | Reduced rate or exemption [T2] |
| Lease (long-term) | Variable |

---

## Step 6: Tourism Taxes [T1]

| Tax | Rate |
|-----|------|
| Hotel/guest house tax | 13% of room charges |
| Cruise ship passenger fee | Per-head fee |
| Departure tax | Included in airfare |

---

## Step 7: Social Insurance [T1]

### Pension

| Requirement | Detail |
|-------------|--------|
| National Pensions Act | Mandatory for employees aged 18-65 |
| Minimum contribution | 10% of earnings (5% employer + 5% employee) |
| Earnings ceiling | Set annually |

### Health Insurance [T1]

- Mandatory health insurance for all employees [T1]
- Employer must provide compliant health insurance plan [T1]
- Minimum coverage standards prescribed by law [T1]

---

## Step 8: Economic Substance [T2]

The Economic Substance Act, 2018 (as amended) requires:

- Entities conducting "relevant activities" must demonstrate adequate economic substance in the Cayman Islands
- Relevant activities: banking, distribution and service centre, financing and leasing, fund management, headquarters, holding entity, insurance, intellectual property, shipping
- Requirements: directed and managed in Cayman, adequate employees/expenditure/physical presence
- Annual reporting to the Tax Information Authority

**Flag for practitioner: economic substance compliance is [T3] for detailed analysis. Requires specialist advice.**

---

## Step 9: International Reporting [T2]

### CRS (Common Reporting Standard)

- Cayman Islands participates in OECD CRS [T1]
- Financial institutions must report account holder information to the Cayman Islands Tax Information Authority [T1]
- Information is exchanged with participating jurisdictions [T1]

### FATCA

- Cayman Islands has an IGA (Model 1) with the United States [T1]
- Financial institutions must report US account holders [T1]
- Annual reporting to the Tax Information Authority [T1]

### Beneficial Ownership

- Beneficial ownership registers maintained [T1]
- Information available to authorities [T1]

**All international reporting obligations are [T3] for detailed compliance -- escalate to specialist.**

---

## PROHIBITIONS [T1]

- NEVER state that the Cayman Islands has income tax -- it does not
- NEVER state that the Cayman Islands has VAT or sales tax -- it does not
- NEVER state that the Cayman Islands has payroll tax -- it does not
- NEVER apply any direct tax calculations to Cayman Islands entities
- NEVER ignore import duty obligations (primary compliance area)
- NEVER ignore economic substance reporting requirements for relevant entities
- NEVER ignore CRS/FATCA reporting for financial institutions
- NEVER assume duty rates without confirming current schedule
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not AI

---

## Step 10: Edge Case Registry

### EC1 -- Fund domiciled in Cayman [T1]
**Situation:** Investment fund registered as an exempted company in Cayman.
**Resolution:** No income or capital gains tax on fund returns. Annual registration fee payable. Economic substance requirements may apply (fund management). CRS/FATCA reporting obligations exist. Management activities may trigger substance requirements.

### EC2 -- Employee working in Cayman [T1]
**Situation:** Company employs staff in Grand Cayman.
**Resolution:** No payroll tax and no income tax. However: mandatory pension (10% -- split equally), mandatory health insurance, work permit fees for non-Caymanians. These are the employer's primary compliance obligations.

### EC3 -- Importing goods for business [T1]
**Situation:** Cayman business imports inventory from the US.
**Resolution:** Import duty at applicable rate (typically 22% general merchandise). No VAT or sales tax on top. Duty is a cost of goods. Paid to Customs at point of import.

### EC4 -- Real estate purchase by foreign entity [T2]
**Situation:** Non-Caymanian purchases property.
**Resolution:** Stamp duty at 7.5% applies. No annual property tax. No capital gains tax on future sale. Foreign ownership restrictions may apply for certain property types. Flag for practitioner: confirm eligibility and any additional government fees.

### EC5 -- Holding company with no local operations [T2]
**Situation:** Cayman exempted company holds shares in overseas subsidiaries only.
**Resolution:** No tax on dividends, gains, or income. Annual registration fee applies. Economic substance for "holding entity" activity requires minimal substance (but still must be met). Flag for practitioner: confirm economic substance filing requirements.

---

## Step 11: Test Suite

### Test 1 -- Income tax question
**Input:** "What corporate tax does a Cayman Islands company pay?"
**Expected output:** None. The Cayman Islands does not impose corporate income tax. A Tax Undertaking Certificate can guarantee this for up to 50 years.

### Test 2 -- VAT question
**Input:** "What is the VAT rate in the Cayman Islands?"
**Expected output:** The Cayman Islands does not have VAT or any sales tax.

### Test 3 -- Import duty
**Input:** Business imports office equipment valued at KYD 10,000.
**Expected output:** Import duty at applicable rate (general merchandise 22%). Duty = KYD 2,200. No VAT. No sales tax.

### Test 4 -- Employment obligations
**Input:** Cayman company hires a non-Caymanian employee at KYD 60,000/year.
**Expected output:** No income tax, no payroll tax. Pension: 10% (KYD 6,000 -- split 5% employer, 5% employee). Health insurance: mandatory, employer-provided. Work permit: required, annual fee paid by employer.

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
Action Required: Licensed Cayman Islands practitioner must confirm.
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

The Cayman Islands is a tax-neutral jurisdiction. Key points:
1. No direct taxes of any kind (income, capital gains, VAT, payroll, property)
2. Revenue comes from import duties, fees, and tourism taxes
3. Economic substance requirements apply since 2019
4. CRS/FATCA international reporting obligations exist for financial institutions
5. Mandatory pension and health insurance are the primary employer compliance areas

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
