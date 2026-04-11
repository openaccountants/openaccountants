---
name: hong-kong-tax
description: Use this skill whenever asked about Hong Kong taxation, whether VAT/GST/sales tax exists in Hong Kong, or any question involving Hong Kong tax obligations. Trigger on phrases like "Hong Kong VAT", "Hong Kong GST", "Hong Kong sales tax", "Hong Kong tax", "profits tax", "salaries tax", "property tax Hong Kong", or any request involving HK tax compliance. This skill documents that Hong Kong has NO VAT, NO GST, and NO sales tax, and provides an overview of the simple territorial tax system (Profits Tax, Salaries Tax, Property Tax) for context. ALWAYS read this skill before answering any Hong Kong tax question.
---

# Hong Kong Tax Overview Skill (No VAT / No GST)

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Hong Kong Special Administrative Region (Hong Kong SAR) |
| Jurisdiction Code | HK |
| Primary Legislation | Inland Revenue Ordinance (IRO), Chapter 112, Laws of Hong Kong |
| Supporting Legislation | Stamp Duty Ordinance (Cap. 117); Rating Ordinance (Cap. 116); Hotel Accommodation Tax Ordinance (Cap. 348 -- 3% HAT reinstated from 1 January 2025) |
| Tax Authority | Inland Revenue Department (IRD), Hong Kong SAR Government |
| Filing Portal | https://www.ird.gov.hk (eTAX system) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending — requires validation by a licensed Hong Kong CPA or tax representative |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: absence of VAT/GST, profits tax rates, salaries tax rates, property tax rate. Tier 2: source of income determination, offshore claims. Tier 3: complex cross-border structures, transfer pricing, advance rulings. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed CPA/tax representative must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

---

## CRITICAL STATEMENT: No VAT, No GST, No Sales Tax [T1]

**Hong Kong has NO value-added tax (VAT), NO goods and services tax (GST), and NO general sales tax.**

This is a fundamental characteristic of the Hong Kong tax system. There is no consumption tax on goods or services in Hong Kong. There is no input/output tax mechanism, no tax invoicing requirement for indirect tax, and no VAT/GST return to file.

**Legislation:** The IRO does not contain any provisions for VAT or GST. No separate VAT/GST legislation exists in Hong Kong.

**Historical context:** A GST proposal was considered in 2006 (Consultation Paper on Tax Reform) but was abandoned due to public opposition. As of 2026, there are no active proposals to introduce VAT or GST.

### What This Means for Businesses

| Aspect | Hong Kong Position |
|--------|-------------------|
| VAT/GST registration | Not applicable — no VAT/GST exists |
| VAT/GST return filing | Not applicable |
| Input VAT recovery | Not applicable |
| Output VAT charging | Not applicable |
| Tax invoices (fapiao/GUI equivalent) | Not required for indirect tax (commercial invoices for business purposes only) |
| Import VAT/GST | None — goods imported into Hong Kong are generally duty-free (exceptions: tobacco, alcohol, hydrocarbon fuels, methyl alcohol) |
| Hotel Accommodation Tax (HAT) | 3% on hotel/guesthouse accommodation charges — reinstated from 1 January 2025 (was suspended 2008-2024) |
| Export VAT refund | Not applicable |
| Cross-border service VAT | Not applicable |

### Implications for International Businesses [T1]

| Scenario | Treatment |
|----------|-----------|
| Hong Kong entity sells goods/services to EU customer | No Hong Kong VAT to charge; EU customer may need to self-assess VAT under local rules |
| EU entity sells goods to Hong Kong buyer | No import VAT in HK; EU entity may zero-rate the export under EU rules |
| Hong Kong entity sells to China customer | No HK VAT; China import VAT applies at Chinese customs |
| Multinational group with HK holding company | No VAT on management fees, dividends, or intra-group services (but check other jurisdictions' rules) |

---

## Step 1: Hong Kong Tax System Overview [T1]

**Legislation:** IRO Cap. 112.

Hong Kong operates a simple, territorial tax system with three main direct taxes:

| Tax | Rate | Legislation |
|-----|------|-------------|
| Profits Tax (利得稅) | 8.25% on first HKD 2,000,000; 16.5% thereafter (corporations) | IRO s.14, s.14A |
| Profits Tax (unincorporated) | 7.5% on first HKD 2,000,000; 15% thereafter | IRO s.14, s.14A |
| Salaries Tax (薪俸稅) | Progressive rates: 2%, 6%, 10%, 14%, 17%; capped at standard rate 15% | IRO s.8, s.12, Schedule 2 |
| Property Tax (物業稅) | 15% on net assessable value (80% of rental income after statutory deduction) | IRO s.5, s.5B |

### Territorial Principle [T1]

Hong Kong taxes profits only on income arising in or derived from Hong Kong. This is the **territorial source principle**:

- Profits sourced outside Hong Kong are NOT taxable, even if the entity is incorporated/registered in HK
- There is no worldwide taxation
- There is no controlled foreign corporation (CFC) regime (though BEPS measures are being progressively adopted)
- There is no withholding tax on dividends, interest, or royalties (except royalties paid to non-residents under specific circumstances)

**Legislation:** IRO s.14(1) — "every person carrying on a trade, profession or business in Hong Kong... shall be chargeable to profits tax on assessable profits arising in or derived from Hong Kong."

---

## Step 2: Profits Tax [T1]

**Legislation:** IRO Part IV (s.14-19).

### Two-Tiered Profits Tax Rates (effective from Year of Assessment 2018/19)

| Tier | Corporations | Unincorporated Businesses |
|------|-------------|--------------------------|
| First HKD 2,000,000 of assessable profits | 8.25% | 7.5% |
| Remainder | 16.5% | 15% |

**Anti-fragmentation rule:** Only ONE entity within a group of connected entities may elect for the two-tiered rates in any year of assessment. Connected entities must nominate which entity benefits.

**Legislation:** IRO s.14A, s.14B.

### Assessable Profits Calculation [T1]

```
Assessable Profits = Revenue arising in/derived from HK
                   - Allowable deductions (s.16)
                   - Depreciation allowances (s.37-39)
                   + Deemed trading receipts
                   - Losses brought forward (s.19C)
```

### Key Deductible Expenses [T1]

| Expense | Deductible? | Legislation |
|---------|-------------|-------------|
| Rent for business premises | Yes | IRO s.16(1) |
| Employee salaries and wages | Yes | IRO s.16(1) |
| Bad debts (specific provisions) | Yes | IRO s.16(1)(d) |
| Depreciation (tax basis) | Yes -- via depreciation allowance schedule | IRO s.37-39 |
| Interest on borrowings for business | Yes (subject to anti-avoidance rules) | IRO s.16(1)(a), s.16(2) |
| Repairs and maintenance | Yes | IRO s.16(1)(e) |
| Research and development | Yes -- 100% or 300% deduction for qualifying R&D | IRO s.16B |
| Domestic/private expenses | No | IRO s.17(1)(a) |
| Capital expenditure (not via allowances) | No | IRO s.17(1)(c) |
| Tax penalties | No | IRO s.17(1)(e) |

### Depreciation Allowances [T1]

| Category | Initial Allowance | Annual Allowance | Legislation |
|----------|------------------|------------------|-------------|
| Industrial buildings | 20% | 4% | IRO s.34, 35 |
| Commercial buildings | N/A | 4% | IRO s.33A |
| Plant and machinery (Pool system) | 60% | 10%, 20%, or 30% (depending on pool) | IRO s.37, 39B, 39E |
| Environmental protection equipment | 100% in first year | N/A | IRO s.16I |
| Intellectual property | Varies (20% per year over 5 years, or full deduction) | Varies | IRO s.16EA, 16EB |

### Filing Deadlines [T1]

| Entity Type | Year of Assessment | Filing Deadline |
|------------|-------------------|-----------------|
| Corporations (D code) | 1 Apr - 31 Mar | Usually 15 November (1 month extension for e-filing) |
| Sole proprietors (M code) | 1 Apr - 31 Mar | Usually 2 May (1 month extension for e-filing) |
| Partnerships (M code) | 1 Apr - 31 Mar | Usually 2 May |
| Corporations with non-standard year-end | Varies | Per IRD Code of Practice |

**Profits Tax Return:** BIR51 (corporations), BIR52 (sole proprietors/partnerships).

---

## Step 3: Salaries Tax [T1]

**Legislation:** IRO Part III (s.8-13).

### Progressive Rates (Year of Assessment 2024/25 onwards)

| Band | Rate |
|------|------|
| First HKD 50,000 | 2% |
| Next HKD 50,000 | 6% |
| Next HKD 50,000 | 10% |
| Next HKD 50,000 | 14% |
| Remainder | 17% |

**Standard Rate Cap:** Total salaries tax cannot exceed 15% of net assessable income (before personal allowances). The taxpayer pays the LOWER of progressive rate tax or standard rate tax.

### Personal Allowances (2024/25)

| Allowance | Amount (HKD) |
|-----------|-------------|
| Basic Personal Allowance | 132,000 |
| Married Person's Allowance | 264,000 |
| Child Allowance (per child) | 130,000 |
| Child Allowance (year of birth, additional) | 130,000 |
| Dependent Parent/Grandparent (aged 55-59) | 25,000 each |
| Dependent Parent/Grandparent (aged 60+) | 50,000 each |
| Single Parent Allowance | 132,000 |
| Disabled Dependant Allowance | 75,000 each |

### Salaries Tax Deductions [T1]

| Deduction | Limit | Legislation |
|-----------|-------|-------------|
| Self-education expenses | HKD 100,000 | IRO s.12(1)(e) |
| Home loan interest | HKD 100,000 per year (max 20 years) | IRO s.26E |
| Mandatory Provident Fund (MPF) contributions | HKD 18,000 per year | IRO s.12(1)(f) |
| Approved charitable donations | 35% of assessable income | IRO s.26C |
| Elderly residential care expenses | HKD 100,000 per year | IRO s.26D |
| Voluntary health insurance (VHIS) premiums | HKD 8,000 per insured person | IRO s.26P |
| Qualifying annuity premiums and MPF voluntary contributions | HKD 60,000 combined | IRO s.26N, 26Q |
| Domestic rent deduction | HKD 100,000 per year | IRO s.26R |

**Filing:** BIR60 (Individual Tax Return), due within 1 month of issue (typically by 2 May for standard cases, 2 June for e-filing).

---

## Step 4: Property Tax [T1]

**Legislation:** IRO Part II (s.5-5B).

### Rate and Calculation

| Item | Detail |
|------|--------|
| Rate | 15% |
| Base | Net assessable value |
| Net assessable value | Rental income - irrecoverable rent - rates paid by owner - 20% statutory deduction for repairs/outgoings |

```
Property Tax = (Rental Income - Irrecoverable Rent - Rates Paid by Owner) x 80% x 15%
```

### Key Points [T1]

- Property tax applies to owners of land/buildings in Hong Kong who receive rental income
- Corporations already assessed under Profits Tax on the same rental income can apply for Property Tax exemption (to avoid double taxation) under IRO s.5(2)(a)
- Individual owners may elect Personal Assessment (IRO Part VII) to combine all income and claim deductions

---

## Step 5: Other Taxes and Duties [T1]

### Stamp Duty

| Transaction | Rate | Legislation |
|------------|------|-------------|
| Stock transfers | 0.13% of consideration (each side) | Stamp Duty Ordinance Cap. 117 |
| Sale/purchase of immovable property (Scale 2) | Progressive: 1.5% to 4.25% | Cap. 117, Head 1(1) |
| Special Stamp Duty (SSD) — resale within 36 months | 10-20% | Cap. 117, s.29CA |
| Buyer's Stamp Duty (BSD) — non-permanent residents and companies | 15% (suspended in Feb 2024 Budget) | Cap. 117 |
| New Residential Stamp Duty (NRSD) | Suspended from 28 Feb 2024 | Cap. 117 |
| Lease agreements | 0.25-1% of annual rent | Cap. 117, Head 1(2) |

**Note:** BSD and NRSD were suspended effective 28 February 2024 as part of property market support measures. Verify current status for any transaction.

### Hotel Accommodation Tax (HAT) [T1]

**Legislation:** Hotel Accommodation Tax Ordinance (Cap. 348).

| Aspect | Detail |
|--------|--------|
| Rate | 3% of accommodation charges |
| Effective date | 1 January 2025 (reinstated after suspension since 1 July 2008) |
| Applies to | Accommodation charges payable by guests to hotel or guesthouse proprietors |
| Filing | Quarterly returns to IRD |
| Estimated annual revenue | Approximately HKD 1.1 billion |

**Note:** The HAT was reduced to 0% from 1 July 2008 and remained suspended for approximately 17 years. The Legislative Council passed a resolution on 23 October 2024 to resume collection at 3% from 1 January 2025.

### Customs and Excise Duties [T1]

Hong Kong is a free port. There are NO customs duties on general imports. Duties apply ONLY to:

| Dutiable Commodity | Duty Basis |
|--------------------|-----------|
| Tobacco | Per stick/weight |
| Liquor (>30% alcohol) | Per litre of alcohol |
| Hydrocarbon oils (motor fuel) | Per litre |
| Methyl alcohol | Per litre |

**Legislation:** Dutiable Commodities Ordinance (Cap. 109).

### Government Rates and Rent

| Charge | Rate | Basis |
|--------|------|-------|
| Government Rates | 5% | Rateable value of property (assessed by Rating and Valuation Department) |
| Government Rent | 3% | Rateable value (for post-1985 leases) |

---

## Step 6: Anti-Avoidance and International [T2]

### Transfer Pricing [T2]

**Legislation:** IRO s.50AAB-50AAK (effective YA 2018/19).

Hong Kong introduced transfer pricing rules aligned with OECD guidelines:

- Arm's length principle applies to related-party transactions
- Documentation requirements for qualifying entities
- Country-by-Country Reporting (CbCR) for large MNEs (consolidated revenue >= HKD 6.8 billion)
- Advance pricing agreements available

**Flag for reviewer: transfer pricing documentation and compliance require specialist analysis.**

### Foreign-Sourced Income Exemption (FSIE) Regime [T2]

**Legislation:** IRO s.15H-15JA (effective 1 January 2023).

From 2023, Hong Kong implemented a refined FSIE regime for passive income received by MNE entities:

| Income Type | Treatment |
|------------|-----------|
| Foreign-sourced dividends | Exempt if economic substance or participation exemption conditions met |
| Foreign-sourced interest | Exempt if economic substance conditions met |
| Foreign-sourced IP income | Exempt if nexus approach conditions met |
| Foreign-sourced disposal gains | Exempt if economic substance or participation exemption conditions met |

**Flag for reviewer: FSIE regime conditions are complex and require case-by-case analysis by tax specialist.**

### Double Tax Agreements [T1]

Hong Kong has Comprehensive Double Taxation Agreements (CDTAs) with 40+ jurisdictions. Key treaty partners include: China Mainland, UK, Japan, South Korea, India, France, Ireland, Belgium, Luxembourg, Netherlands, Switzerland, and others.

---

## Step 7: Edge Case Registry

### EC1 -- "Does HK Have VAT?" [T1]
**Situation:** Client asks whether Hong Kong has VAT, GST, or sales tax.
**Resolution:** No. Hong Kong has NO VAT, NO GST, and NO general sales tax. There is no indirect consumption tax. This is not a temporary situation — it is a fundamental design feature of the HK tax system.

### EC2 -- Hong Kong Entity Selling to EU Customer [T1]
**Situation:** HK company exports goods/services to an EU customer. EU customer asks about VAT treatment.
**Resolution:** No HK VAT applies. The EU customer may need to account for import VAT (goods) or reverse charge VAT (services) under their own jurisdiction's rules. The HK entity has no VAT obligations.

### EC3 -- Hong Kong Entity Importing from China [T1]
**Situation:** HK company imports goods from mainland China.
**Resolution:** No import VAT in Hong Kong (unless dutiable commodities — tobacco, alcohol, fuel). Chinese export may qualify for Chinese VAT export refund. HK buyer pays no indirect tax on the import.

### EC4 -- Offshore Profits Claim [T2]
**Situation:** HK-incorporated company claims profits are sourced outside Hong Kong and therefore not subject to Profits Tax.
**Resolution:** The source of profits is determined by the nature and location of the profit-generating activities, not the location of the customer or the contract. Key factors: where the contracts are negotiated, concluded, and executed; where the operations are carried out. This requires detailed facts-and-circumstances analysis. Flag for reviewer.
**Legislation:** IRO s.14(1); CIR v Hang Seng Bank [1991]; CIR v HK-TVB International [1992].

### EC5 -- Two-Tiered Rate Election Among Connected Entities [T1]
**Situation:** A group of companies in Hong Kong wants to apply the 8.25% rate on first HKD 2 million.
**Resolution:** Only ONE entity in the connected group may elect for the two-tiered rate. All other connected entities pay the standard rate (16.5%) on all profits. The group must nominate the electing entity.
**Legislation:** IRO s.14B.

### EC6 -- Salaries Tax vs Profits Tax for Freelancers [T2]
**Situation:** An individual provides freelance services. Question is whether income is subject to Salaries Tax or Profits Tax.
**Resolution:** Depends on the nature of the engagement. Key factors: degree of control, provision of equipment, financial risk, integration into client's business. Employment = Salaries Tax. Self-employment/business = Profits Tax. Flag for reviewer for borderline cases.
**Legislation:** IRO s.8 (Salaries Tax), s.14 (Profits Tax); Poon Cho-ming v CIR [1980].

---

## Step 8: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Hong Kong CPA or tax representative must confirm.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed CPA/tax representative. Document gap.
```

---

## Step 9: Test Suite

### Test 1 -- "Does Hong Kong Have VAT?"
**Input:** Client asks "Do I need to register for VAT in Hong Kong?"
**Expected output:** No. Hong Kong has no VAT, no GST, and no sales tax. There is no VAT registration requirement.

### Test 2 -- Profits Tax, Two-Tiered Rate
**Input:** HK corporation with assessable profits of HKD 5,000,000.
**Expected output:** First HKD 2,000,000 x 8.25% = HKD 165,000. Remaining HKD 3,000,000 x 16.5% = HKD 495,000. Total Profits Tax = HKD 660,000.

### Test 3 -- Property Tax
**Input:** Individual owns HK property. Annual rental income HKD 240,000. Rates paid by owner HKD 12,000. No irrecoverable rent.
**Expected output:** Net assessable value = (240,000 - 12,000) x 80% = HKD 182,400. Property Tax = 182,400 x 15% = HKD 27,360.

### Test 4 -- Import of Goods (No VAT)
**Input:** HK company imports electronics from Japan. CIF value HKD 1,000,000.
**Expected output:** No import VAT. No customs duty (electronics are not dutiable commodities). Total tax on import = HKD 0.

### Test 5 -- Salaries Tax, Standard Rate Cap
**Input:** Employee with net assessable income HKD 2,000,000 (after deductions), single, no dependants.
**Expected output:** Progressive tax would be: 50,000 x 2% + 50,000 x 6% + 50,000 x 10% + 50,000 x 14% + 1,800,000 x 17% = 1,000 + 3,000 + 5,000 + 7,000 + 306,000 = HKD 322,000. Standard rate: (2,000,000 - 132,000 basic allowance) x 15% = HKD 280,200. Pay lower = HKD 280,200.

---

## PROHIBITIONS [T1]

- NEVER state or imply that Hong Kong has VAT, GST, or sales tax -- it does not
- NEVER advise a client to register for VAT/GST in Hong Kong -- no such registration exists
- NEVER attempt to prepare a VAT/GST return for Hong Kong -- no such return exists
- NEVER assume profits are automatically taxable -- source must be determined under territorial principle
- NEVER apply the two-tiered rate to more than one entity in a connected group
- NEVER confuse Salaries Tax with Profits Tax for income classification
- NEVER ignore the standard rate cap when computing Salaries Tax
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not by the AI

---

## Contribution Notes

This skill covers the Hong Kong tax system as of early 2026. Hong Kong's tax regime is relatively stable, but practitioners should monitor IRD Practice Notes and legislative amendments, particularly regarding the FSIE regime and BEPS-related measures.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
