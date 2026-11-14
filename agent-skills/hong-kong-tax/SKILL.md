---
name: hong-kong-tax
description: "Use this skill whenever asked about Hong Kong taxation, whether VAT/GST/sales tax exists in Hong Kong, or any question involving Hong Kong tax obligations. Trigger on phrases like \"Hong Kong VAT\", \"Hong Kong GST\", \"Hong Kong sales tax\", \"Hong Kong tax\", \"profits tax\", \"salaries tax\", \"property tax Hong Kong\", or any request involving HK tax compliance. This skill documents that Hong Kong has NO VAT, NO GST, and NO sales tax, and provides an overview of the simple territorial tax system (Profits Tax, Salaries Tax, Property Tax) for context. ALWAYS read this skill before answering any Hong Kong tax question. Year of assessment 2026/27. Built from the law, not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/hong-kong-tax"
  jurisdiction: "HK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Hong Kong Tax

## Who this applies to

### Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Hong Kong Special Administrative Region (Hong Kong SAR) |
| Jurisdiction Code | HK |
| Primary Legislation | Inland Revenue Ordinance (IRO), Chapter 112, Laws of Hong Kong |
| Supporting Legislation | Stamp Duty Ordinance (Cap. 117); Rating Ordinance (Cap. 116); Hotel Accommodation Tax Ordinance (Cap. 348 -- 3% HAT reinstated from 1 January 2025) |
| Tax Authority | Inland Revenue Department (IRD), Hong Kong SAR Government |
| Filing Portal | https://www.ird.gov.hk (eTAX system) |
| Contributor | Open Accounting Skills Registry |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: absence of VAT/GST, profits tax rates, salaries tax rates, property tax rate. Tier 2: source of income determination, offshore claims. Tier 3: complex cross-border structures, transfer pricing, advance rulings. |

### Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed CPA/tax representative must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

### CRITICAL STATEMENT: No VAT, No GST, No Sales Tax [T1]

- **No VAT/GST/Sales Tax**: Hong Kong has NO value-added tax (VAT), NO goods and services tax (GST), and NO general sales tax. There is no consumption tax on goods or services in Hong Kong. There is no input/output tax mechanism, no tax invoicing requirement for indirect tax, and no VAT/GST return to file.  _(The IRO does not contain any provisions for VAT or GST. No separate VAT/GST legislation exists in Hong Kong.)_

A GST proposal was considered in 2006 (Consultation Paper on Tax Reform) but was abandoned due to public opposition. As of 2026, there are no active proposals to introduce VAT or GST.

#### What This Means for Businesses

**What This Means for Businesses**

| Aspect | Hong Kong Position |
| --- | --- |
| VAT/GST registration | Not applicable, no VAT/GST exists |
| VAT/GST return filing | Not applicable |
| Input VAT recovery | Not applicable |
| Output VAT charging | Not applicable |
| Tax invoices (fapiao/GUI equivalent) | Not required for indirect tax (commercial invoices for business purposes only) |
| Import VAT/GST | None, goods imported into Hong Kong are generally duty-free (exceptions: tobacco, alcohol, hydrocarbon fuels, methyl alcohol) |
| Hotel Accommodation Tax (HAT) | 3% on hotel/guesthouse accommodation charges, reinstated from 1 January 2025 (was suspended 2008-2024) |
| Export VAT refund | Not applicable |
| Cross-border service VAT | Not applicable |

#### Implications for International Businesses [T1]

**Implications for International Businesses**

| Scenario | Treatment |
| --- | --- |
| Hong Kong entity sells goods/services to EU customer | No Hong Kong VAT to charge; EU customer may need to self-assess VAT under local rules |
| EU entity sells goods to Hong Kong buyer | No import VAT in HK; EU entity may zero-rate the export under EU rules |
| Hong Kong entity sells to China customer | No HK VAT; China import VAT applies at Chinese customs |
| Multinational group with HK holding company | No VAT on management fees, dividends, or intra-group services (but check other jurisdictions' rules) |

### Step 1: Hong Kong Tax System Overview [T1]

- **System overview**: Hong Kong operates a simple, territorial tax system with three main direct taxes.  _(IRO Cap. 112)_

**Main direct taxes**

| Tax | Rate | Legislation |
| --- | --- | --- |
| Profits Tax (利得稅) | 8.25% on first HKD 2,000,000; 16.5% thereafter (corporations) | IRO s.14, s.14A |
| Profits Tax (unincorporated) | 7.5% on first HKD 2,000,000; 15% thereafter | IRO s.14, s.14A |
| Salaries Tax (薪俸稅) | Progressive rates: 2%, 6%, 10%, 14%, 17%; capped at standard rate 15% | IRO s.8, s.12, Schedule 2 |
| Property Tax (物業稅) | 15% on net assessable value (80% of rental income after statutory deduction) | IRO s.5, s.5B |

#### Territorial Principle [T1]

- **Territorial source principle**: Hong Kong taxes profits only on income arising in or derived from Hong Kong. Profits sourced outside Hong Kong are NOT taxable, even if the entity is incorporated/registered in HK. There is no worldwide taxation. There is no controlled foreign corporation (CFC) regime (though BEPS measures are being progressively adopted). There is no withholding tax on dividends, interest, or royalties (except royalties paid to non-residents under specific circumstances).  _(IRO s.14(1), "every person carrying on a trade, profession or business in Hong Kong... shall be chargeable to profits tax on assessable profits arising in or derived from Hong Kong.")_

## Rates, bands and thresholds

Year of assessment 2026/27 unless stated.

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| VAT, GST, sales tax | None | Not among the taxes the IRD administers | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf |
| Profits tax, corporations | 8.25% to HKD 2,000,000; 16.5% above | Two-tiered; one nominated entity per connected group | https://www.ird.gov.hk/eng/tax/bus_pft.htm |
| Profits tax, unincorporated | 7.5% to HKD 2,000,000; 15% above | Same | same |
| Plant and machinery initial allowance | 60% of cost | Annual allowance then 10%, 20% or 30% on reducing value | same |
| Industrial building initial allowance | 20% | Person who incurs the construction expenditure | same |
| Salaries tax, progressive | 2%, 6%, 10%, 14% on HKD 50,000 bands; 17% above | Net chargeable income | https://www.gov.hk/en/residents/taxes/taxfiling/taxrates/salariesrates.htm |
| Salaries tax, standard rate | 15% on the first HKD 5,000,000 of net income; 16% above | Lower of progressive and standard applies | same |
| Basic allowance | HKD 145,000 | From YA 2026/27; other allowances in the base section | https://www.ird.gov.hk/eng/tax/budget.htm |
| Elderly residential care deduction | Up to HKD 110,000 | From YA 2026/27 | same |
| Property tax | 15% of net assessable value | After rates paid by the owner and a 20% statutory allowance | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf |
| Stamp duty, Hong Kong stock | 0.1% of the consideration, buyer and seller each | From 17 November 2023 | same |
| Stamp duty, immovable property | HKD 100 up to HKD 4,000,000; 1.5%, 2.25%, 3%, 3.75%, 4.25% above | From 26 February 2025; marginal relief | same |
| Stamp duty on lease rent | 0.25% to 1% of annual rent | By lease term; premium at the property scale (4.25% where premium and rent) | same |
| Hotel accommodation tax | 3% of accommodation charges | From 1 January 2025 | same |
| Global minimum tax and HKMTT | 15% | MNE groups with revenue of EUR 750 million or more; fiscal years from 1 January 2025 | https://www.ird.gov.hk/eng/tax/bus_beps.htm |
| Profits tax returns 2025/26, "D" and "M" codes | 17 August 2026 and 16 November 2026 | Represented taxpayers | https://www.ird.gov.hk/eng/pdf/bel26e.pdf |

## The base

### Step 2: Profits Tax [T1]

- **Profits Tax legislation**: Profits Tax is governed by IRO Part IV.  _(IRO Part IV (s.14-19))_

#### Two-Tiered Profits Tax Rates (effective from Year of Assessment 2018/19)

**Two-Tiered Profits Tax Rates**

| Tier | Corporations | Unincorporated Businesses |
| --- | --- | --- |
| First HKD 2,000,000 of assessable profits | 8.25% | 7.5% |
| Remainder | 16.5% | 15% |

- **Anti-fragmentation rule**: Only ONE entity within a group of connected entities may elect for the two-tiered rates in any year of assessment. Connected entities must nominate which entity benefits.  _(IRO s.14A, s.14B)_

#### Assessable Profits Calculation [T1]

- **Assessable Profits Calculation**: Assessable Profits = Revenue arising in/derived from HK - Allowable deductions (s.16) - Depreciation allowances (s.37-39) + Deemed trading receipts - Losses brought forward (s.19C)  _(IRO s.16, s.37-39, s.19C)_

#### Key Deductible Expenses [T1]

**Key Deductible Expenses**

| Expense | Deductible? | Legislation |
| --- | --- | --- |
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

#### Depreciation Allowances [T1]

**Depreciation Allowances**

| Category | Initial Allowance | Annual Allowance | Legislation |
| --- | --- | --- | --- |
| Industrial buildings | 20% | 4% | IRO s.34, 35 |
| Commercial buildings | N/A | 4% | IRO s.33A |
| Plant and machinery (Pool system) | 60% | 10%, 20%, or 30% (depending on pool) | IRO s.37, 39B, 39E |
| Environmental protection equipment | 100% in first year | N/A | IRO s.16I |
| Intellectual property | Varies (20% per year over 5 years, or full deduction) | Varies | IRO s.16EA, 16EB |

#### Filing Deadlines [T1]

**Filing Deadlines**

| Entity Type | Year of Assessment | Filing Deadline |
| --- | --- | --- |
| Accounting date 1 April to 30 November 2025 ("N" code) | 2025/26 | No block extension |
| Accounting date in December 2025 ("D" code) | 2025/26 | 17 August 2026 (represented) |
| Accounting date 1 January to 31 March 2026 ("M" code) | 2025/26 | 16 November 2026 (represented); 1 February 2027 for loss cases on request |
| Sole proprietors (accounts filed with BIR60) | 2025/26 | 5 October 2026 (represented) |

- **Profits Tax Return forms**: BIR51 (corporations), BIR52 (sole proprietors/partnerships).

### Step 3: Salaries Tax [T1]

- **Salaries Tax legislation**: Salaries Tax is governed by IRO Part III.  _(IRO Part III (s.8-13))_

#### Progressive Rates (Year of Assessment 2024/25 onwards)

**Progressive Rates**

| Band | Rate |
| --- | --- |
| First HKD 50,000 | 2% |
| Next HKD 50,000 | 6% |
| Next HKD 50,000 | 10% |
| Next HKD 50,000 | 14% |
| Remainder | 17% |

- **Standard rate**: 15% on the first HKD 5,000,000 of net income (before personal allowances) and 16% above (YA 2024/25 onwards). The taxpayer pays the LOWER of progressive rate tax or standard rate tax.

#### Personal Allowances (YA 2026/27)

**Personal Allowances**

| Allowance | Amount (HKD) |
| --- | --- |
| Basic Personal Allowance | 145,000 |
| Married Person's Allowance | 290,000 |
| Child Allowance (per child, 1st to 9th) | 140,000 |
| Child Allowance (newborn, additional, first two years) | 140,000 |
| Dependent Parent/Grandparent (aged 55-59) | 27,500 each (plus 27,500 if living together) |
| Dependent Parent/Grandparent (aged 60+) | 55,000 each (plus 55,000 if living together) |
| Single Parent Allowance | 145,000 |
| Disabled Dependant Allowance | 75,000 each |

#### Salaries Tax Deductions [T1]

**Salaries Tax Deductions**

| Deduction | Limit | Legislation |
| --- | --- | --- |
| Self-education expenses | HKD 100,000 | IRO s.12(1)(e) |
| Home loan interest | HKD 100,000 per year (max 20 years); up to 120,000 with the additional deduction from 2024/25 | IRO s.26E |
| Mandatory Provident Fund (MPF) contributions | HKD 18,000 per year | IRO s.12(1)(f) |
| Approved charitable donations | 35% of assessable income | IRO s.26C |
| Elderly residential care expenses | HKD 110,000 per year from YA 2026/27 | IRO s.26D |
| Voluntary health insurance (VHIS) premiums | HKD 8,000 per insured person | IRO s.26P |
| Qualifying annuity premiums and MPF voluntary contributions | HKD 60,000 combined | IRO s.26N, 26Q |
| Domestic rent deduction | HKD 100,000 per year; up to 120,000 with the additional deduction from 2024/25 | IRO s.26R |

- **Salaries Tax filing**: BIR60 (Individual Tax Return), issued in early May (4 May 2026 for 2025/26) and normally due within one month; represented cases extended to 4 July 2026, or 5 October 2026 with sole proprietorship accounts. Correction: the old file said "by 2 May".

### Step 4: Property Tax [T1]

- **Property Tax legislation**: Property Tax is governed by IRO Part II.  _(IRO Part II (s.5-5B))_

#### Rate and Calculation

**Rate and Calculation**

| Item | Detail |
| --- | --- |
| Rate | 15% |
| Base | Net assessable value |
| Net assessable value | Rental income - irrecoverable rent - rates paid by owner - 20% statutory deduction for repairs/outgoings |

- **Property Tax formula**: Property Tax = (Rental Income - Irrecoverable Rent - Rates Paid by Owner) x 80% x 15%

#### Key Points [T1]

- **Key Points**: Property tax applies to owners of land/buildings in Hong Kong who receive rental income. Corporations already assessed under Profits Tax on the same rental income can apply for Property Tax exemption (to avoid double taxation) under IRO s.5(2)(a). Individual owners may elect Personal Assessment (IRO Part VII) to combine all income and claim deductions.  _(IRO s.5(2)(a); IRO Part VII)_

### Step 5: Other Taxes and Duties [T1]

- **Other taxes and duties**: 

#### Stamp Duty

**Stamp Duty**

| Transaction | Rate | Legislation |
| --- | --- | --- |
| Stock transfers | 0.1% of consideration (each side), from 17 November 2023 | Stamp Duty Ordinance Cap. 117 |
| Sale/purchase of immovable property | HKD 100 up to HKD 4,000,000; then 1.5% to 4.25% (from 26 February 2025) | Cap. 117, Head 1(1) |
| Special Stamp Duty (SSD), Buyer's Stamp Duty (BSD), New Residential Stamp Duty (NRSD) | Not listed in the IRD brief guide 2025/26, which shows only ad valorem duty; the old file said BSD and NRSD were suspended from 28 February 2024 (status not confirmed here; check before any transaction) | Cap. 117 |
| Lease agreements | 0.25-1% of annual rent | Cap. 117, Head 1(2) |

**Note:** the demand-side property duties (SSD, BSD, NRSD) are not in the IRD 2025/26 brief guide; verify their status on the IRD stamp duty pages for any transaction.

#### Hotel Accommodation Tax (HAT) [T1]

- **HAT legislation**: Hotel Accommodation Tax Ordinance (Cap. 348).  _(Hotel Accommodation Tax Ordinance (Cap. 348))_

**HAT details**

| Aspect | Detail |
| --- | --- |
| Rate | 3% of accommodation charges |
| Effective date | 1 January 2025 (reinstated after suspension since 1 July 2008) |
| Applies to | Accommodation charges payable by guests to hotel or guesthouse proprietors |
| Filing | Quarterly returns to IRD |
| Estimated annual revenue | Approximately HKD 1.1 billion |

**Note:** The HAT was reduced to 0% from 1 July 2008 and remained suspended for approximately 17 years. The Legislative Council passed a resolution on 23 October 2024 to resume collection at 3% from 1 January 2025.

#### Customs and Excise Duties [T1]

- **Free port status**: Hong Kong is a free port. There are NO customs duties on general imports. Duties apply ONLY to specific dutiable commodities.  _(Dutiable Commodities Ordinance (Cap. 109))_

**Dutiable Commodities**

| Dutiable Commodity | Duty Basis |
| --- | --- |
| Tobacco | Per stick/weight |
| Liquor (>30% alcohol) | Per litre of alcohol |
| Hydrocarbon oils (motor fuel) | Per litre |
| Methyl alcohol | Per litre |

#### Government Rates and Rent

**Government Rates and Rent**

| Charge | Rate | Basis |
| --- | --- | --- |
| Government Rates | 5% | Rateable value of property (assessed by Rating and Valuation Department) |
| Government Rent | 3% | Rateable value (for post-1985 leases) |

## Deadlines and filing

Profits tax: returns issue on the first working day of April (1 April 2026 for 2025/26) and are due in one month unless the block extension applies (table under Step 2 and `hk-corporate-income-tax`). Salaries tax: BIR60 issues in early May (4 May 2026 for 2025/26). Property tax: BIR57 or BIR58 returns, also issued in April (form dates not restated). Provisional tax for the next year is charged with each final assessment. For YA 2026/27 the returns issue in April and May 2027.

## Penalties and interest

Late or incorrect returns without reasonable excuse: fine of HKD 10,000 plus treble the tax undercharged (IRO s. 80(2)), or additional tax up to treble under s. 82A in lieu of prosecution. Wilful evasion (s. 82): HKD 50,000, treble the tax and up to 3 years' imprisonment. Unpaid tax: 5% surcharge on the outstanding balance of the demand notice, with recovery action under IRO Part XII.

## Cross-border points

### Step 6: Anti-Avoidance and International [T2]

- **Anti-avoidance and international overview**: 

#### Transfer Pricing [T2]

- **Transfer Pricing rules**: Hong Kong introduced transfer pricing rules aligned with OECD guidelines: Arm's length principle applies to related-party transactions; Documentation requirements for qualifying entities; Country-by-Country Reporting (CbCR) for large MNEs (consolidated revenue >= HKD 6.8 billion); Advance pricing agreements available. Flag for reviewer: transfer pricing documentation and compliance require specialist analysis.  _(IRO s.50AAB-50AAK (effective YA 2018/19))_

#### Foreign-Sourced Income Exemption (FSIE) Regime [T2]

- **FSIE regime**: From 2023, Hong Kong implemented a refined FSIE regime for passive income received by MNE entities.  _(IRO s.15H-15JA (effective 1 January 2023))_

**FSIE Income Type Treatment**

| Income Type | Treatment |
| --- | --- |
| Foreign-sourced dividends | Exempt if economic substance or participation exemption conditions met |
| Foreign-sourced interest | Exempt if economic substance conditions met |
| Foreign-sourced IP income | Exempt if nexus approach conditions met |
| Foreign-sourced disposal gains | Exempt if economic substance or participation exemption conditions met |

**Flag for reviewer: FSIE regime conditions are complex and require case-by-case analysis by tax specialist.**

#### Double Tax Agreements [T1]

- **CDTAs**: Hong Kong has Comprehensive Double Taxation Agreements (CDTAs) with 40+ jurisdictions. Key treaty partners include: China Mainland, UK, Japan, South Korea, India, France, Ireland, Belgium, Luxembourg, Netherlands, Switzerland, and others.

### Step 7: Edge Case Registry

#### EC1 -- "Does HK Have VAT?" [T1]

- **EC1**: **Situation:** Client asks whether Hong Kong has VAT, GST, or sales tax. **Resolution:** No. Hong Kong has NO VAT, NO GST, and NO general sales tax. There is no indirect consumption tax. This is not a temporary situation, it is a fundamental design feature of the HK tax system.

#### EC2 -- Hong Kong Entity Selling to EU Customer [T1]

- **EC2**: **Situation:** HK company exports goods/services to an EU customer. EU customer asks about VAT treatment. **Resolution:** No HK VAT applies. The EU customer may need to account for import VAT (goods) or reverse charge VAT (services) under their own jurisdiction's rules. The HK entity has no VAT obligations.

#### EC3 -- Hong Kong Entity Importing from China [T1]

- **EC3**: **Situation:** HK company imports goods from mainland China. **Resolution:** No import VAT in Hong Kong (unless dutiable commodities, tobacco, alcohol, fuel). Chinese export may qualify for Chinese VAT export refund. HK buyer pays no indirect tax on the import.

#### EC4 -- Offshore Profits Claim [T2]

- **EC4**: **Situation:** HK-incorporated company claims profits are sourced outside Hong Kong and therefore not subject to Profits Tax. **Resolution:** The source of profits is determined by the nature and location of the profit-generating activities, not the location of the customer or the contract. Key factors: where the contracts are negotiated, concluded, and executed; where the operations are carried out. This requires detailed facts-and-circumstances analysis. Flag for reviewer.  _(IRO s.14(1); CIR v Hang Seng Bank [1991]; CIR v HK-TVB International [1992].)_

#### EC5 -- Two-Tiered Rate Election Among Connected Entities [T1]

- **EC5**: **Situation:** A group of companies in Hong Kong wants to apply the 8.25% rate on first HKD 2 million. **Resolution:** Only ONE entity in the connected group may elect for the two-tiered rate. All other connected entities pay the standard rate (16.5%) on all profits. The group must nominate the electing entity.  _(IRO s.14B.)_

#### EC6 -- Salaries Tax vs Profits Tax for Freelancers [T2]

- **EC6**: **Situation:** An individual provides freelance services. Question is whether income is subject to Salaries Tax or Profits Tax. **Resolution:** Depends on the nature of the engagement. Key factors: degree of control, provision of equipment, financial risk, integration into client's business. Employment = Salaries Tax. Self-employment/business = Profits Tax. Flag for reviewer for borderline cases.  _(IRO s.8 (Salaries Tax), s.14 (Profits Tax); Poon Cho-ming v CIR [1980].)_

## Two worked examples that recompute

**Example 1: profits tax on HKD 5,000,000 (corporation, nominated for the two-tiered rates).** 8.25% of 2,000,000 = 165,000; 16.5% of 3,000,000 = 495,000; total HKD 660,000.

```oa-check
name: HK 2026/27 corporation profits tax on HKD 5m
inputs:
  profits: 5000000
steps:
  - tax: min(profits, 2000000) * 0.0825 + max(profits - 2000000, 0) * 0.165
expected:
  tax: 660000
```

**Example 2: decision, does the standard rate or the progressive rate apply (net income HKD 2,000,000, single, YA 2026/27).** Progressive on 1,855,000 (after the 145,000 basic allowance) = 297,350; standard rate 15% of 2,000,000 = 300,000. The progressive result is lower, so HKD 297,350 is payable. The crossover moves up as allowances rise; at higher incomes the standard rate wins.

```oa-check
name: HK 2026/27 progressive vs standard rate at HKD 2m net income
inputs:
  net_income: 2000000
  basic: 145000
steps:
  - nci: net_income - basic
  - progressive: 16000 + (nci - 200000) * 0.17
  - standard: min(net_income, 5000000) * 0.15 + max(net_income - 5000000, 0) * 0.16
  - tax: min(progressive, standard)
expected:
  progressive: 297350
  standard: 300000
  tax: 297350
```

Property tax check (test 3 below): (240,000 less 12,000 rates) x 80% x 15% = HKD 27,360.

### Step 9: Test Suite

#### Test 1 -- "Does Hong Kong Have VAT?"

**Input:** Client asks "Do I need to register for VAT in Hong Kong?"
**Expected output:** No. Hong Kong has no VAT, no GST, and no sales tax. There is no VAT registration requirement.

#### Test 2 -- Profits Tax, Two-Tiered Rate

**Input:** HK corporation with assessable profits of HKD 5,000,000.
**Expected output:** First HKD 2,000,000 x 8.25% = HKD 165,000. Remaining HKD 3,000,000 x 16.5% = HKD 495,000. Total Profits Tax = HKD 660,000.

#### Test 3 -- Property Tax

**Input:** Individual owns HK property. Annual rental income HKD 240,000. Rates paid by owner HKD 12,000. No irrecoverable rent.
**Expected output:** Net assessable value = (240,000 - 12,000) x 80% = HKD 182,400. Property Tax = 182,400 x 15% = HKD 27,360.

#### Test 4 -- Import of Goods (No VAT)

**Input:** HK company imports electronics from Japan. CIF value HKD 1,000,000.
**Expected output:** No import VAT. No customs duty (electronics are not dutiable commodities). Total tax on import = HKD 0.

#### Test 5 -- Salaries Tax, Standard Rate Cap

**Input:** Employee with net assessable income HKD 2,000,000 (after deductions), single, no dependants.
**Expected output (YA 2026/27):** Progressive tax on net chargeable income (2,000,000 less the 145,000 basic allowance = 1,855,000): 16,000 on the first 200,000 plus 1,655,000 x 17% = 281,350; total HKD 297,350. Standard rate on net income BEFORE allowances: 2,000,000 x 15% = HKD 300,000. Pay lower = HKD 297,350. Correction: the old test applied the allowance to the standard rate and not to the progressive rate (it gave 322,000 and 280,200); both are wrong.

## Ask the client first

1. Which tax: business profits, employment income, rental income, a share or property deal, hotel accommodation?
2. Where the business is carried on and where profits are made (source).
3. For individuals: employment or self-employment, marital status, children, dependants (allowances).
4. For groups: connected entities, MNE membership, consolidated revenue.
5. For property and shares: the instrument, price and dates (stamp duty).
6. Year of assessment concerned (2025/26 returns being filed now, or 2026/27).

### Step 8: Reviewer Escalation Protocol

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

### PROHIBITIONS [T1]

- **Prohibitions**: - NEVER state or imply that Hong Kong has VAT, GST, or sales tax -- it does not - NEVER advise a client to register for VAT/GST in Hong Kong -- no such registration exists - NEVER attempt to prepare a VAT/GST return for Hong Kong -- no such return exists - NEVER assume profits are automatically taxable -- source must be determined under territorial principle - NEVER apply the two-tiered rate to more than one entity in a connected group - NEVER confuse Salaries Tax with Profits Tax for income classification - NEVER ignore the standard rate cap when computing Salaries Tax - NEVER compute any number -- all arithmetic is handled by the deterministic engine, not by the AI

### Contribution Notes

This skill covers the Hong Kong tax system as of early 2026. Hong Kong's tax regime is relatively stable, but practitioners should monitor IRD Practice Notes and legislative amendments, particularly regarding the FSIE regime and BEPS-related measures.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRD, A brief guide to taxes 2025/26 (PDF). Read for the list of taxes, property tax, stamp duty scales, stock duty 0.1%, HAT 3%, FSIE and deductions | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf | 2026-11-14 |
| IRD, profits tax page. Read for the two-tiered rates and capital allowances (60% and 20% initial allowances) | https://www.ird.gov.hk/eng/tax/bus_pft.htm | 2026-11-14 |
| GovHK, salaries tax rates. Read for the progressive and standard rates | https://www.gov.hk/en/residents/taxes/taxfiling/taxrates/salariesrates.htm | 2026-11-14 |
| IRD, 2026-27 Budget tax measures. Read for the YA 2026/27 allowances and the 110,000 elderly care cap | https://www.ird.gov.hk/eng/tax/budget.htm | 2026-11-14 |
| IRD, global minimum tax and HKMTT. Read for the 15% rate and scope | https://www.ird.gov.hk/eng/tax/bus_beps.htm | 2026-11-14 |
| IRD, block extension letter 2025/26 (PDF). Read for the profits tax and BIR60 due dates | https://www.ird.gov.hk/eng/pdf/bel26e.pdf | 2026-11-14 |
| IRD penalty policy. Read for ss. 80(2), 82 and 82A | https://www.ird.gov.hk/eng/pol/ppo.htm | 2026-11-14 |

Not yet confirmed: status of SSD, BSD and NRSD; R&D deductions of 100% or 300% (s. 16B); government rates 5% and government rent 3% (Rating and Valuation Department pages not read); HAT quarterly returns, the HKD 1.1 billion revenue estimate and the 23 October 2024 LegCo resolution date; the 2006 GST consultation; the number of comprehensive double taxation agreements (old file: 40 or more); transfer pricing documentation thresholds; dutiable commodity rates.

**Disclaimer**

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `hong-kong-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/hong-kong-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
