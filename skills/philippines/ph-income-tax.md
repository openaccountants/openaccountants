---
name: ph-income-tax
description: Use this skill whenever asked about Philippines income tax for self-employed individuals or professionals. Trigger on phrases like "Philippines income tax", "BIR", "Bureau of Internal Revenue", "TRAIN law", "8% flat rate", "graduated tax", "Form 1701", "Form 1701Q", "OSD", "itemized deductions", "self-employed Philippines", "professional tax Philippines", "bir.gov.ph", "quarterly ITR Philippines", or any question about Philippine income tax rates, filing, deductions, or the 8% option. Covers graduated rates, 8% flat rate option, quarterly and annual filing, deductions, and BIR compliance. ALWAYS read this skill before touching any Philippines income tax work.
version: 1.1
jurisdiction: PH
tax_year: 2026
last_updated: 2026-11-26
type: computation
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# PH Income Tax

## Scope

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Philippines (Republic of the Philippines / Republika ng Pilipinas) |
| Tax | Income Tax |
| Currency | PHP (Philippine Peso / ₱) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | National Internal Revenue Code (NIRC) of 1997, as amended by RA 10963 (TRAIN Law, 2018) |
| Tax authority | Bureau of Internal Revenue (BIR) |
| Filing portal | eFPS / eBIRForms (https://www.bir.gov.ph) |
| Annual filing deadline | Normally 15 April of the following year. The calendar-year 2025 deadline was extended to 15 May 2026. [RMC 30-2026](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2030-2026.pdf) |
| Quarterly filing deadline | BIR Form 1701Q: 15 May, 15 August and 15 November for Q1, Q2 and Q3, subject to the next-business-day rule and specific extensions. [RR 8-2018](https://bir-cdn.bir.gov.ph/local/pdf/Digest%20RR%208-2018_copy.pdf) |

## Rates, bands and thresholds

**Graduated Income Tax Rates (from 1 January 2023 onwards)**

| Net Taxable Income (₱) | Tax Due |
| --- | --- |
| 0 -- 250,000 | 0% [RR 8-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%208-2018.pdf) |
| Over 250,000 up to 400,000 | 15% of excess over ₱250,000 [RR 8-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%208-2018.pdf) |
| Over 400,000 up to 800,000 | ₱22,500 + 20% of excess over ₱400,000 [RR 8-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%208-2018.pdf) |
| Over 800,000 up to 2,000,000 | ₱102,500 + 25% of excess over ₱800,000 [RR 8-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%208-2018.pdf) |
| Over 2,000,000 up to 8,000,000 | ₱402,500 + 30% of excess over ₱2,000,000 [RR 8-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%208-2018.pdf) |
| Above 8,000,000 | ₱2,202,500 + 35% of excess over ₱8,000,000 [RR 8-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%208-2018.pdf) |

### 8% Flat Rate Option

**8% Flat Rate Option**

| Item | Detail |
| --- | --- |
| Rate | 8% of gross sales or receipts and other taxable non-operating income. Deduct ₱250,000 from that base for purely self-employed individuals or professionals. Mixed-income earners tax qualifying business income at 8% on the full base and apply graduated rates to compensation. [RMO 23-2018](https://bir-cdn.bir.gov.ph/local/pdf/RMO%20NO.23-2018.pdf) |
| In lieu of | Graduated income tax AND 3% percentage tax [RMO 23-2018](https://bir-cdn.bir.gov.ph/local/pdf/RMO%20NO.23-2018.pdf) |
| Eligibility | Individuals with business or professional income, including mixed-income earners. Annual gross sales or receipts plus other taxable non-operating income must be within the ₱3,000,000 threshold. Exclusions include VAT registration, liability for a Title V percentage tax other than section 116, income tax exemption and a general professional partner's distributive share. [RMO 23-2018](https://bir-cdn.bir.gov.ph/local/pdf/RMO%20NO.23-2018.pdf) |
| Election | Elect for each taxable year. Use the registration or first quarterly return routes in section 3.4. [RMO 23-2018](https://bir-cdn.bir.gov.ph/local/pdf/RMO%20NO.23-2018.pdf) |
| Default | Graduated income tax (if no election made) [RMO 23-2018](https://bir-cdn.bir.gov.ph/local/pdf/RMO%20NO.23-2018.pdf) |

## Conservative defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown tax regime election | Graduated rates (default per BIR) |
| Unknown deduction method | Confirm the election. Itemised deductions apply by default if the taxpayer did not elect OSD. |
| Unknown VAT/percentage tax status | Confirm registration and whether section 116 or another business tax applies. |
| Unknown business-use % | 0% deduction |

## Ask the client first

### Required Inputs

**Minimum viable** -- bank statement or record of gross sales/receipts for the year, TIN (Tax Identification Number), and confirmation of whether 8% flat rate or graduated rates are elected.

**Recommended** -- all sales invoices/official receipts, purchase records, BIR Form 2307 certificates of withholding, prior year ITR (Form 1701, 1701A or 1701-MS, as applicable), BIR registration (Form 2303 / Certificate of Registration).

**Ideal** -- complete books of accounts, general ledger, trial balance, quarterly ITRs (Form 1701Q), percentage tax returns (Form 2551Q), VAT returns (Form 2550Q) if applicable.

### Refusal Catalogue

- **R-PH-1 -- Corporation or partnership**. This skill covers sole proprietors and individual professionals only. Corporations file Form 1702. Escalate to a CPA.
- **R-PH-2 -- VAT-registered taxpayer**. VAT-registered taxpayers have additional obligations (quarterly Form 2550Q, with optional monthly Form 2550M) and cannot use the 8% flat rate option. Income tax still applies but filing differs.
- **R-PH-3 -- Mixed income earner (employment + business)**. Mixed income earners can use the 8% option only on business income, while employment income is taxed at graduated rates. Requires careful computation.
- **R-PH-4 -- Non-resident alien**. Non-resident aliens have different rules (NRA-ETB or NRA-NETB). Out of scope.

## The method, step by step

### 3.1 Option 1: Graduated Income Tax

**Option 1: Graduated Income Tax computation steps**

| Method | Net taxable income calculation |
| --- | --- |
| Itemised | Include taxable business and other income, then subtract allowable cost of sales or services and substantiated deductions. |
| Optional Standard Deduction (OSD) | Deduct up to 40% of gross sales or receipts from taxable income before business deductions. The OSD replaces separate deductions, including cost of sales or services. |

**Deduction methods**

| Method | Detail |
| --- | --- |
| Itemized deductions | Actual business expenses with supporting documentation (receipts, invoices, BIR-registered) |
| OSD (Optional Standard Deduction) | Elect in the first quarterly income tax return and use it for the taxable year. Keep records of gross sales or receipts. Separate expense substantiation is unnecessary for the standard deduction. |

- **Business taxes alongside graduated rates.** Section 116 applies a 3% percentage tax to gross sales of persons covered by the section, with a cooperative exemption. A VAT-registered taxpayer accounts for VAT, generally at 12% on taxable supplies, subject to exemptions, zero-rating and allowable input credits. If both compensation and business income are taxed at graduated rates, combine taxable compensation and net business income.

### 3.2 Option 2: 8% Flat Rate

**Option 2: 8% Flat Rate computation steps**

| Step | Description |
| --- | --- |
| Gross sales/receipts + other non-operating income | Total |
| Less: ₱250,000 (if purely self-employed) | Exempt threshold |
| × 8% | Tax due |

- **No deductions or percentage tax**. No deductions allowed. No percentage tax due.

### 3.3 When to Choose 8% vs Graduated

**When to Choose 8% vs Graduated**

| Scenario | Better Option |
| --- | --- |
| Eligible for both regimes | Compare the 8% result with graduated tax using the elected deduction method, plus any applicable business tax. The break-even point depends on the income bands, allowable deductions and whether the ₱250,000 reduction applies. |
| Gross exceeds ₱3,000,000 | Must use graduated (8% not available) |
| VAT-registered | Must use graduated |

### 3.4 Election Procedure

**Election Procedure**

| Action | Detail |
| --- | --- |
| New registration | Elect in Form 1901, the initial quarterly percentage tax return (2551Q), the initial quarterly income tax return (1701Q), or a combination of those routes under RMO 23-2018. |
| Existing taxpayer switching | Elect in the first quarterly 2551Q or 1701Q, or file Form 1905 at the beginning of the year and select 8% in the first quarterly income tax return. |
| Annual renewal | Make a new election each year. An election is irrevocable for that year whilst the taxpayer qualifies. |
| Exceeding the threshold | Recompute the year's income tax at graduated rates and credit previous 8% income tax instalments. If gross sales breach the VAT threshold, update registration in the following month. VAT applies from its first day, with percentage tax due for the period before VAT liability began. |

## Section 4 -- Quarterly and Annual Filing

### 4.1 Quarterly Income Tax Return (Form 1701Q)

**Quarterly Income Tax Return (Form 1701Q)**

| Quarter | Period | Deadline |
| --- | --- | --- |
| Q1 | January -- March | 15 May |
| Q2 | April -- June | 15 August |
| Q3 | July -- September | 15 November |
| Q4 | Covered by annual return | -- |

Use the next business day if the statutory filing date falls on a Saturday, Sunday or holiday. The ordinary dates for calendar-year 2026 were 15 May, 17 August and 16 November, subject to applicable BIR extensions.

### 4.2 Annual Income Tax Return

**Annual Income Tax Return**

| Form | Who Files | Deadline |
| --- | --- | --- |
| Form 1701 | Individual business or professional income with itemised deductions, or mixed income, subject to the simplified return option. | Normally 15 April of the following year |
| Form 1701A | Purely business or professional income using the 8% option or OSD with graduated rates. | Same date |
| Form 1701-MS | Optional simplified annual return for qualifying micro and small taxpayers, including mixed-income earners with a single applicable business income tax rate. Check BIR channel instructions. | Same date |

BIR RMC 30-2026 extended filing, payment and submission of required attachments for calendar-year 2025 from 15 April to 15 May 2026. The ordinary calendar-year 2026 annual deadline under section 51 is 15 April 2027.

### 4.3 Percentage Tax (if graduated, non-VAT)

**Percentage Tax (if graduated, non-VAT)**

| Form | Period | Deadline |
| --- | --- | --- |
| Form 2551Q | Quarterly | Within 25 days after end of quarter |
| Rate | 3% of gross sales for taxpayers within section 116 |  |

## Section 5 -- Allowable Deductions (Graduated Option)

### 5.1 Itemized Deductions

**Itemized Deductions**

| Category | Treatment |
| --- | --- |
| Cost of goods sold / services | Deductible |
| Salaries and wages (with BIR-registered payroll) | Deductible |
| Rent (business premises) | Deductible |
| Utilities (business) | Deductible |
| Professional fees | Deductible |
| Depreciation | Per NIRC rules |
| Bad debts | Business debts ascertained to be worthless and charged off during the year, subject to the related-party exclusion and recovery rule. |
| Interest expense | Qualifying business interest paid or incurred during the year, reduced by 20% of interest income subjected to final tax. Apply the other limitations in section 34(B). |
| Contributions to pension trust | Apply the employer contribution and timing rules in section 34(I). |
| Research and development | Apply section 34(J) to qualifying business expenditure, including its rules for expenditure chargeable to capital account. |
| Entertainment, amusement and recreation | Deduct substantiated qualifying costs up to 0.50% of net sales of goods or properties or 1% of net revenue from services. Apportion actual expenses if both activities apply and cap each portion separately under RR 10-2002. |

### 5.2 Non-Deductible Expenses

**Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Personal/family expenses | Not business-related |
| Capital expenditure | Through depreciation |
| Income tax | Tax on income |
| Losses from tax-exempt income | Not deductible |
| Bribes, kickbacks | Public policy |

## Worked cases

### Example 1 -- 8% Flat Rate

**Input:** Freelance graphic designer with ₱2,400,000 in tax-basis gross receipts and no employment or other taxable non-operating income. The taxpayer qualifies for the 8% option and elected it on time.

**Tax:** (₱2,400,000 − ₱250,000) × 8% = ₱172,000. The 8% election replaces section 116 percentage tax. Keep books and issue required invoices.

```oa-check
name: Flat rate
steps:
  total: pct(2400000 - 250000, 8)
expected:
  total: 172000
```

### Example 2 -- Graduated with OSD

**Input:** Same freelancer, with ₱2,400,000 in gross receipts for income tax and ₱2,400,000 in gross sales for section 116. Assume the taxpayer elected OSD instead of the 8% option.

**OSD:** 40% × ₱2,400,000 = ₱960,000.
**Net taxable income:** ₱2,400,000 - ₱960,000 = ₱1,440,000.
**Tax:** ₱102,500 + (₱1,440,000 - ₱800,000) × 25% = ₱102,500 + ₱160,000 = ₱262,500.
**Plus 3% percentage tax:** ₱2,400,000 × 3% = ₱72,000.
**Total tax burden:** ₱262,500 + ₱72,000 = ₱334,500.

**Comparison:** 8% flat rate (₱172,000) is significantly better for this taxpayer.

```oa-check
name: Graduated with OSD
steps:
  total: 102500 + pct(2400000 - pct(2400000, 40) - 800000, 25) + pct(2400000, 3)
expected:
  total: 334500
```

### Example 3 -- Graduated with Itemized Deductions

**Input:** Non-VAT consultant with ₱2,400,000 in gross receipts for income tax and ₱2,400,000 in gross sales for section 116. Allowable documented itemised deductions total ₱1,800,000, including any deductible percentage tax for the year.

**Net taxable income:** ₱2,400,000 - ₱1,800,000 = ₱600,000.
**Tax:** ₱22,500 + (₱600,000 - ₱400,000) × 20% = ₱22,500 + ₱40,000 = ₱62,500.
**Plus 3% percentage tax:** ₱72,000.
**Total:** ₱134,500. Better than 8% due to high expenses.

```oa-check
name: Graduated with itemised deductions
steps:
  total: 22500 + pct(2400000 - 1800000 - 400000, 20) + pct(2400000, 3)
expected:
  total: 134500
```

## Section 7 -- Penalties

**Penalties**  _(NIRC ss.248–250, 255; RR 21-2018; RA 11976 (EOPT). Corrected by Jonathan I. Ruiz (CPA, Philippines))_

| Offence | Penalty |
| --- | --- |
| Ordinary civil surcharge | Generally 25% of the amount due under section 248(A). Under RR 6-2024 qualifying micro and small taxpayers pay 10%. Micro means gross sales below ₱3 million and small means at least ₱3 million and below ₱20 million. |
| Interest on unpaid tax | Generally 12% a year under section 249 and RR 21-2018, and 6% for qualifying micro and small taxpayers under RR 6-2024. Deficiency and delinquency interest cannot run simultaneously. |
| Wilful failure to file an income tax return | On conviction under section 255, a fine of at least ₱10,000 and imprisonment of 1–10 years, in addition to other penalties. |
| Information return or record failure | Under section 250 and RR 6-2024, generally ₱1,000 per failure, capped at ₱25,000 per calendar year. For qualifying micro and small taxpayers, ₱500 per failure and ₱12,500 per calendar year. Check notice and demand and the statutory reasonable-cause exception. |
| Wilful neglect to file or false or fraudulent return | 50% surcharge on the tax or applicable deficiency under section 248(B). Unreported sales or income exceeding 30% of the amount declared, or overstated deductions exceeding 30% of actual deductions, constitute prima facie evidence if determined by the Commissioner. Criminal liability depends on the offence and conviction. |
| Late or missing BIR registration | RR 15-2024 section 13 lists ₱1,000 as the compromise amount for voluntary late registration. For discovered non-registration of a head office or branch, it lists ₱5,000 for micro, ₱15,000 for small, ₱20,000 for medium or large and ₱50,000 for business subject to excise tax. |

## Section 8 -- Reference Material

### Key BIR Forms

**Key BIR Forms**

| Form | Purpose |
| --- | --- |
| 1701 | Annual ITR -- self-employed/professional (itemized or mixed) |
| 1701A | Annual ITR, purely business or professional income using 8% or OSD |
| 1701-MS | Optional simplified annual ITR for eligible micro and small taxpayers |
| 1701Q | Quarterly ITR |
| 2551Q | Quarterly Percentage Tax |
| 1905 | Application for registration update (including 8% election) |
| 1901 | Initial registration |
| 2303 | Certificate of Registration |

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Income tax rates | NIRC Section 24(A), as amended by RA 10963 (TRAIN Law) |
| 8% option | NIRC Section 24(A)(2)(b); RMO 23-2018 |
| OSD | NIRC Section 34(L) |
| Withholding tax | NIRC Section 57; RR 11-2018 |
| Percentage tax | NIRC Sections 109(CC) and 116, as amended by RA 11976 |
| Filing | NIRC Sections 51 and 74(A), RR 8-2018 and RMC 65-2016 |

## When to refuse or refer

- NEVER allow the 8% option for VAT-registered taxpayers
- Check both gross sales or receipts and other taxable non-operating income against the ₱3,000,000 eligibility limit before using the 8% option.
- NEVER claim deductions under the 8% flat rate option
- NEVER apply 8% flat rate without confirming annual election
- Test section 116 liability before applying the 3% percentage tax.
- NEVER forget quarterly filing (Form 1701Q) -- penalties are steep
- NEVER present calculations as definitive -- always label as estimated

## Sources

| Source | Read date | Read for |
|---|---|---|
| [BIR, RR 8-2018 digest, graduated income tax, the 8% option and return deadlines](https://bir-cdn.bir.gov.ph/local/pdf/Digest%20RR%208-2018_copy.pdf) | 2026-11-24 | Section 3 tax schedule effective in 2023 and the quarterly and annual return dates. |
| [BIR, RMO 23-2018, election, threshold and VAT transition](https://bir-cdn.bir.gov.ph/local/pdf/RMO%20NO.23-2018.pdf) | 2026-11-24 | Section II, paragraphs 4–16, eligibility, election, mixed income and VAT transition. |
| [BIR, RMC 65-2016, next-business-day rule](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2065-2016.pdf) and [RMC 30-2026, annual filing extension](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2030-2026.pdf) | 2026-11-24 | Parts A–C of RMC 65 and RMC 30 extension for calendar-year 2025 returns. |
| [BIR, RMC 20-2026 Annex C, eligible annual return forms](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026%20Annex%20C%20%283%29.pdf) | 2026-11-24 | Questions 1–3 and the annual form comparison for micro and small filers. |
| [BIR, RR 16-2008, OSD base for an individual](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/43850) and [RR 2-2010, first-quarter OSD election](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/50806) | 2026-11-24 | Section 3 of RR 16 and adjusted section 7 of RR 2, OSD base and election. |
| [National Internal Revenue Code, deductions and penalties](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896), [RA 11534, section 34(B)](https://elibrary.judiciary.gov.ph/thebookshelf//showdocs/2/93191) and [BIR RR 10-2002, entertainment expense ceilings](https://bir-cdn.bir.gov.ph/BIR/pdf/2294rr10_02.pdf) | 2026-11-24 | NIRC sections 34, 36 and 248–255, RA 11534 section 7 and RR 10 section 5. |
| [RA 11976, percentage tax and micro or small taxpayer relief](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948), [BIR RR 6-2024 digest, reduced penalties](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%206-2024%20%28final%29.pdf), [RR 21-2018, interest](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No%2021-2018.pdf) and [RR 15-2024, registration compromise schedule](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2015-2024.pdf) | 2026-11-24 | EOPT sections 21 and 45 and amended sections 116 and 248, RR 6 sections 2–5, RR 21 section 2 and RR 15 section 13. |
| [BIR, RMC 52-2023, optional monthly VAT returns](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%2052-2023%20%281%29.pdf) and [RR 11-2018, income tax withholding certificates](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) | 2026-11-24 | RMC 52 part II and RR 11 Form 2307 certificate and credit provisions. |

Not yet confirmed: BIR annual filing circular and channel-specific instructions for calendar-year 2026 returns to be filed in 2027. Apply the ordinary deadline and confirm any later eligible extension.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
