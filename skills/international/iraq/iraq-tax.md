---
name: iraq-tax
description: Use this skill whenever asked about Iraq taxation, sales tax, or the absence of VAT in Iraq. Trigger on phrases like "Iraq tax", "Iraq VAT", "Iraq sales tax", "Iraq income tax", or any request involving Iraqi tax compliance. Iraq does NOT have a broad-based VAT or GST. It imposes extremely high sales taxes on specific products (up to 300% on alcohol and tobacco) and has an income tax system. This skill documents the current tax landscape. ALWAYS read this skill before handling any Iraq tax work.
---

# Iraq Tax Compliance Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Iraq |
| Jurisdiction Code | IQ |
| Primary Legislation | Income Tax Law No. 113 of 1982 (as amended) |
| Supporting Legislation | Sales Tax Instructions (specific goods); Customs Tariff Law; Company Law No. 21 of 1997 |
| Tax Authority | General Commission for Taxes (GCT), Ministry of Finance |
| Filing Portal | No centralized electronic filing portal as of 2026 |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Iraqi tax practitioner |
| Validation Date | Pending |
| Last Research Update | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: no-VAT status, sales tax on specific goods, CIT rates. Tier 2: provincial tax variations, Kurdistan Region treatment, foreign contractor obligations. Tier 3: reconstruction-era incentives, oil sector taxation, complex PE determinations. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

---

## Step 0: Current Tax Landscape Overview [T1]

Iraq's tax system is characterized by the ABSENCE of a broad-based consumption tax:

| Tax Type | Status |
|----------|--------|
| Value Added Tax (VAT) | **NOT implemented** -- No VAT or GST system exists |
| General Sales Tax | **NOT implemented** -- No broad-based sales tax |
| Specific Sales Taxes | **YES** -- Rates on alcohol (300%), tobacco (300%), mobile/internet (20%), travel (15%), cars (15%), hotels (10%), telecom (5%) |
| Corporate Income Tax | **YES** -- 15% standard rate |
| Personal Income Tax | **YES** -- Progressive rates 3% to 15% |
| Withholding Tax | **YES** -- Various rates on payments to non-residents |
| Property Tax | **YES** -- On real estate |
| Customs Duties | **YES** -- On imports |
| Social Security | **YES** -- Contributions for employees |

---

## Step 1: VAT / Broad-Based Sales Tax Status [T1]

### Current Position

- **Iraq does NOT have a VAT system** [T1]
- **Iraq does NOT have a general sales tax** [T1]
- There is no VAT registration requirement [T1]
- There are no VAT return filing obligations [T1]
- There is no VAT invoicing requirement [T1]

### Future Implementation [T2]

- Iraq has periodically discussed introducing a VAT or sales tax
- No legislation has been enacted as of 2026
- Monitor GCT and MOF announcements for developments
- **Flag for practitioner: if VAT is introduced, a new skill will be required**

---

## Step 2: Specific Sales Taxes [T1]

Iraq imposes extremely high sales taxes on specific categories of goods:

| Product | Tax Rate | Notes |
|---------|----------|-------|
| Alcohol | **300%** | Applied at point of sale or import |
| Tobacco products (cigarettes) | **300%** | Applied at point of sale or import |
| Mobile recharge cards and internet | **20%** | Reimposed by government decision |
| Travel tickets | **15%** | Applied at point of sale |
| Cars | **15%** | Applied at point of sale or import |
| Deluxe/first-class restaurants and hotels | **10%** | On services rendered |
| Telecommunications services | **5%** | On telecom services |
| Other specified goods | Variable | Per GCT instructions |

### Application [T1]

- These are NOT a VAT -- they are specific excise-type levies on enumerated goods
- No input tax credit mechanism exists (unlike VAT) [T1]
- The tax is a cost to the final consumer, embedded in the price [T1]
- Importers pay the tax at customs [T1]
- Domestic producers pay the tax to GCT [T1]

### Key Distinction [T1]

These specific sales taxes differ from VAT in critical ways:
- **No input credit:** Tax paid on purchases cannot be offset against tax collected
- **No staged collection:** Tax is not collected at each stage of the supply chain
- **Limited scope:** Applies only to enumerated goods, not all goods and services
- **No registration system:** No separate registration for sales tax

---

## Step 3: Corporate Income Tax (CIT) [T1]

### Rates

| Entity Type | Rate |
|-------------|------|
| Iraqi companies (standard) | 15% |
| Foreign companies / branches | 15% |
| Oil and gas companies (production) | 35% [T2] |
| Banks and insurance companies | 15% |
| Agricultural income | Exempt |
| Industrial projects | May qualify for exemptions [T2] |

### Key Rules [T1]

1. **Tax base:** Net profits from Iraqi-source income
2. **Tax year:** Calendar year (January - December) [T1]
3. **Filing deadline:** 31 May of the following year [T1]
4. **Advance payments:** Required for certain large taxpayers [T2]
5. **Books and records:** Must be maintained in Arabic [T1]

### Deductions [T1]

Allowable deductions include:
- Cost of goods sold and direct expenses [T1]
- Depreciation at prescribed rates [T1]
- Employee salaries and benefits [T1]
- Rent and utilities [T1]
- Bad debts (with conditions) [T2]
- Carry-forward of losses: up to 5 years [T1]

### Non-Deductible Expenses [T1]

- Fines and penalties [T1]
- Personal expenses of shareholders/directors [T1]
- Provisions (general) [T1]
- Expenses without proper documentation [T1]
- Entertainment (above limits) [T2]

---

## Step 4: Personal Income Tax [T1]

### Rates

| Annual Income (IQD) | Rate |
|---------------------|------|
| First IQD 250,000 | 3% |
| IQD 250,001 - 500,000 | 5% |
| IQD 500,001 - 1,000,000 | 10% |
| Above IQD 1,000,000 | 15% |

### Exemptions and Allowances [T1]

- Personal allowance for the taxpayer [T1]
- Spouse allowance [T1]
- Child allowances [T1]
- Specific income types may be exempt (agricultural income) [T1]

---

## Step 5: Withholding Tax [T1]

| Payment Type | WHT Rate | Notes |
|-------------|----------|-------|
| Payments to non-resident contractors | Variable, typically deducted at source | [T2] |
| Government contract payments | Advance deduction at source | [T1] |
| Employee salaries | PAYE withholding | [T1] |
| Dividends | Generally no WHT on distributed profits | [T1] |
| Interest | No specific WHT | [T2] |
| Royalties | No specific WHT | [T2] |

---

## Step 6: Kurdistan Region of Iraq (KRI) [T2]

### Separate Tax Administration

The Kurdistan Region has its own tax authority and may apply different rules:

- KRI has its own tax regulations and enforcement [T2]
- Investment incentives differ from federal Iraq [T2]
- Tax rates may be the same but administration differs [T2]
- Companies operating in both regions may have dual obligations [T2]

**Flag for practitioner: ANY business operating in the Kurdistan Region must confirm obligations with both federal and regional tax authorities.**

---

## Step 7: Customs Duties [T1]

| Category | Rate |
|----------|------|
| Reconstruction materials | 0% - 5% |
| Consumer goods | 5% - 30% |
| Luxury items | Higher rates |
| Prohibited goods | Import ban |
| Agricultural products | Variable |

### Key Rules [T1]

- Customs duties assessed on CIF value [T1]
- Paid at point of entry [T1]
- Not recoverable (no input credit system) [T1]
- Iraqi Customs administers duties separately from income tax [T1]

---

## Step 8: Social Security [T1]

| Contribution | Rate |
|-------------|------|
| Employer contribution | 12% of gross salary |
| Employee contribution | 5% of gross salary |
| Total | 17% |

**Legislation:** Social Security Law No. 39 of 1971 (as amended).

---

## Step 9: Filing and Payment [T1]

### Corporate Income Tax

| Requirement | Detail |
|-------------|--------|
| Tax year | Calendar year |
| Filing deadline | 31 May following year-end |
| Financial statements | Must accompany return |
| Language | Arabic |
| Filing method | Paper filing at GCT offices |

### Personal Income Tax

| Requirement | Detail |
|-------------|--------|
| Tax year | Calendar year |
| Filing deadline | 31 May following year-end |
| Employer obligations | Monthly PAYE withholding |

---

## Step 10: Key Thresholds

| Threshold | Value |
|-----------|-------|
| CIT rate | 15% |
| Maximum PIT rate | 15% |
| Sales tax on alcohol/tobacco | 300% |
| Sales tax on mobile/internet | 20% |
| Sales tax on travel tickets / cars | 15% |
| Sales tax on deluxe hotels/restaurants | 10% |
| Sales tax on telecom services | 5% |
| Loss carry-forward | 5 years |
| Social security (total) | 17% |
| CIT filing deadline | 31 May |

---

## PROHIBITIONS [T1]

- NEVER state that Iraq has VAT -- it does not
- NEVER apply VAT calculations to Iraq transactions
- NEVER apply input tax credits to sales tax on alcohol/tobacco (no credit mechanism exists)
- NEVER treat the 300% sales tax on alcohol/tobacco as a VAT
- NEVER assume federal rules automatically apply in Kurdistan Region
- NEVER file returns without Arabic-language documentation
- NEVER assume electronic filing is available (paper filing may be required)
- NEVER guess oil sector taxation rules -- escalate to [T3]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not AI

---

## Step 11: Edge Case Registry

### EC1 -- Foreign contractor in Iraq [T2]
**Situation:** US company provides construction services in Iraq under a government contract.
**Resolution:** CIT at 15% applies to Iraqi-source income. Government may withhold tax at source. Company must register with GCT, file annual returns, maintain Arabic records. Flag for practitioner: government contract tax provisions vary.

### EC2 -- Alcohol import [T1]
**Situation:** Importer brings alcohol into Iraq.
**Resolution:** 300% sales tax applies at customs, in addition to customs duties. No input credit. Tax is a direct cost. Note: alcohol import may be restricted or prohibited in certain provinces and in KRI.

### EC3 -- E-commerce / digital services [T1]
**Situation:** Foreign digital company provides services to Iraqi customers.
**Resolution:** No VAT or sales tax applies to digital services. However, if the company has a PE in Iraq, CIT may apply. PE determination is [T3] -- escalate.

### EC4 -- Kurdistan Region operations [T2]
**Situation:** Company operates in both Baghdad and Erbil.
**Resolution:** May need to file with both federal GCT and KRI tax authority. Investment incentives in KRI may differ. Flag for practitioner: dual filing obligations require specialist advice.

### EC5 -- Agricultural income [T1]
**Situation:** Iraqi farmer earns income from crop sales.
**Resolution:** Agricultural income is exempt from income tax under the Income Tax Law. No CIT or PIT applies to agricultural income.

---

## Step 12: Test Suite

### Test 1 -- VAT question
**Input:** Client asks "What is the VAT rate in Iraq?"
**Expected output:** Iraq does not have VAT. No broad-based consumption tax exists. Specific sales taxes apply to alcohol (300%), tobacco (300%), mobile/internet (20%), travel tickets (15%), cars (15%), hotels (10%), and telecom (5%).

### Test 2 -- Corporate income tax
**Input:** Iraqi company, net profits IQD 100,000,000 from trading activities.
**Expected output:** CIT at 15%. Tax = IQD 15,000,000. File by 31 May.

### Test 3 -- Alcohol sales tax
**Input:** Retailer sells imported alcohol, cost IQD 1,000,000.
**Expected output:** 300% sales tax was applied at import stage. No input credit mechanism. The sales tax is embedded in the cost of goods.

### Test 4 -- Agricultural exemption
**Input:** Farmer earns IQD 50,000,000 from rice cultivation.
**Expected output:** Agricultural income is exempt from income tax. No CIT or PIT.

### Test 5 -- Foreign contractor
**Input:** UK engineering firm earns IQD 500,000,000 from Iraqi government contract.
**Expected output:** CIT at 15% on Iraqi-source income. Government may withhold tax at source. Must register with GCT, file annual return.

---

## Step 13: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Iraqi tax practitioner must confirm.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax practitioner. Document gap.
```

---

## Contribution Notes

This skill documents Iraq's tax landscape, which notably lacks a broad-based consumption tax (VAT/GST). Key points:
1. No VAT or GST exists in Iraq
2. Specific sales taxes apply to enumerated goods: alcohol/tobacco (300%), mobile/internet (20%), travel tickets/cars (15%), hotels (10%), telecom (5%)
3. Income tax is the primary direct tax (15% CIT, up to 15% PIT)
4. Kurdistan Region may have different administrative requirements
5. Electronic filing infrastructure is limited

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
