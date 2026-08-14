---
name: tw-income-tax
description: Use this skill whenever asked about Taiwan individual income tax. Trigger on phrases like "Taiwan income tax", "綜合所得稅", "個人所得稅", "Taiwan tax return", "eFiling Taiwan", "National Taxation Bureau", "執行業務所得", "營利所得", "standard deduction Taiwan", "progressive rate Taiwan", "Taiwan freelance tax", or any question about computing, filing, or planning individual income tax for a Taiwan tax resident. This skill covers the progressive rate table, deductions, exemptions, filing via eFiling, and common categories of income for self-employed professionals. ALWAYS read this skill before advising on Taiwan individual income tax.
version: 1.0
jurisdiction: TW
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# TW Income Tax

## Taiwan Individual Income Tax -- Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Taiwan (Republic of China / 中華民國) |
| Tax | Consolidated Income Tax (綜合所得稅) |
| Currency | TWD / NTD (New Taiwan Dollar) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (所得稅法) |
| Supporting legislation | Income Basic Tax Act (所得基本稅額條例), Tax Collection Act (稅捐稽徵法) |
| Tax authority | Ministry of Finance (財政部), National Taxation Bureau (國稅局) |
| Filing portal | eFiling (etax.nat.gov.tw) |
| Filing period | May 1 -- May 31 of following year |
| Validated by | Pending — requires sign-off by a Taiwan CPA (會計師) |
| Skill version | 1.0 |

### Progressive Tax Rates (2025)

**Progressive Tax Rates (2025)**

| Net Taxable Income (NT$) | Rate | Progressive Difference (NT$) |
| --- | --- | --- |
| 0 -- 590,000 | 5% | 0 |
| 590,001 -- 1,330,000 | 12% | 41,300 |
| 1,330,001 -- 2,660,000 | 20% | 147,700 |
| 2,660,001 -- 4,980,000 | 30% | 413,700 |
| 4,980,001 and above | 40% | 911,700 |

- **Tax formula** — Net Taxable Income × Rate − Progressive Difference = Tax Payable

### Exemptions and Deductions (2025)

**Exemptions and Deductions (2025)**

| Item | Amount (NT$) |
| --- | --- |
| Personal exemption (免稅額) | 97,000 per person |
| Personal exemption (aged 70+) | 145,500 per person |
| Standard deduction -- single (標準扣除額) | 131,000 |
| Standard deduction -- married filing jointly | 262,000 |
| Special deduction for wage income (薪資所得特別扣除額) | 218,000 |
| Special deduction for disabled (身心障礙特別扣除額) | 218,000 |
| Special deduction for pre-school children (幼兒學前特別扣除額) | 150,000 per child |
| Special deduction for tertiary education (教育學費特別扣除額) | 25,000 per child |
| Special deduction for savings/investment income (儲蓄投資特別扣除額) | Up to 270,000 |
| Special deduction for long-term care (長期照顧特別扣除額) | 120,000 per person |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown filing status | Single (individual) |
| Unknown deduction method | Standard deduction (unless itemised clearly exceeds) |
| Unknown income category | Clarify before proceeding |
| Unknown residency | If present ≥183 days in year, treat as resident |
| Unknown withholding | Verify via eFiling pre-filled data |
| Business vs employment income | Employment (薪資) unless clear business/professional activity |

## Section 2 -- Income Categories

### 2.1 Categories of Income (所得類別)

**Categories of Income**

| Category | Chinese | Description |
| --- | --- | --- |
| Category 1 | 營利所得 | Business/profit income (sole proprietor, partnership) |
| Category 2 | 執行業務所得 | Professional practice income (lawyers, doctors, accountants, freelancers) |
| Category 3 | 薪資所得 | Salary/wage income |
| Category 4 | 利息所得 | Interest income |
| Category 5 | 租賃所得 | Rental income |
| Category 6 | 權利金所得 | Royalty income |
| Category 7 | 財產交易所得 | Property transaction income |
| Category 8 | 競技、競賽及機會中獎之獎金 | Prizes and lottery winnings |
| Category 9 | 退職所得 | Retirement income |
| Category 10 | 其他所得 | Other income |

### 2.2 Professional Practice Income (執行業務所得)

For self-employed professionals (freelancers, consultants, independent practitioners):

**Computation methods**

| Method | Computation | When to Use |
| --- | --- | --- |
| Actual expense method | Revenue - documented expenses = net income | Better records; expenses >deemed rate |
| Deemed expense rate (費用率) | Revenue × (1 - deemed rate) = net income | Simpler; no full records |

**Common Deemed Expense Rates (費用率) by Profession**

| Profession | Expense Rate | Net Income Rate |
| --- | --- | --- |
| Lawyers (律師) | 30% | 70% |
| CPAs / Accountants (會計師) | 30% | 70% |
| Architects (建築師) | 35% | 65% |
| Doctors / Dentists (醫師) | 78% (clinic) / 40% (other) | 22% / 60% |
| Pharmacists (藥師) | 20% | 80% |
| Engineers (技師) | 35% | 65% |
| Writers / Authors (著作人) | 30% | 70% |
| Performers / Artists (表演人) | 45% | 55% |
| Software developers / IT consultants | 30% (general services) | 70% |
| Insurance agents (保險經紀人) | 26% | 74% |
| Other professional services | 30% (default) | 70% |

### 2.3 Business Income (營利所得)

- **Business income computation and thresholds** — Compute via bookkeeping (actual income - actual expenses) OR assessed by tax authority based on industry benchmarks. If annual revenue ≤NT$200,000: exempt from business tax. If annual revenue >NT$200,000 but ≤NT$2,000,000: simplified assessment by tax authority.

## Section 3 -- Computation

### 3.1 Tax Computation Worksheet

```
A. GROSS CONSOLIDATED INCOME
   A1. Salary income (薪資所得)                         ___________
   A2. Professional practice income (執行業務所得)       ___________
   A3. Business income (營利所得)                       ___________
   A4. Interest income (利息所得)                       ___________
   A5. Rental income (租賃所得)                         ___________
   A6. Other income                                     ___________
   A7. Total Gross Income (綜合所得總額)                ___________

B. EXEMPTIONS (免稅額)
   B1. Taxpayer (NT$97,000 or NT$145,500 if 70+)       ___________
   B2. Spouse                                           ___________
   B3. Dependants                                       ___________
   B4. Total Exemptions                                 ___________

C. DEDUCTIONS (扣除額)
   C1. Standard deduction OR itemised deductions        ___________
       Standard: NT$131,000 (single) / NT$262,000 (joint)
       Itemised: insurance, medical, disaster, donations,
                 rent, mortgage interest
   C2. Total Deductions                                 ___________

D. SPECIAL DEDUCTIONS (特別扣除額)
   D1. Wage income special deduction (max NT$218,000)   ___________
   D2. Disabled special deduction (NT$218,000 each)     ___________
   D3. Pre-school children (NT$150,000 each)            ___________
   D4. Education tuition (NT$25,000 per child)          ___________
   D5. Savings/investment (max NT$270,000)              ___________
   D6. Long-term care (NT$120,000 per person)           ___________
   D7. Total Special Deductions                         ___________

E. NET TAXABLE INCOME (A7 - B4 - C2 - D7)             ___________

F. TAX COMPUTATION
   F1. Net taxable income × rate - progressive diff    ___________
   F2. Investment tax credits (if applicable)           ___________
   F3. Tax payable (F1 - F2)                           ___________

G. WITHHOLDING AND PREPAYMENTS
   G1. Tax withheld at source (扣繳稅額)               ___________
   G2. Estimated tax paid                               ___________
   G3. Total credits                                    ___________

H. TAX DUE / (REFUND) = F3 - G3                        ___________
```

### 3.2 Worked Example -- Single Freelancer

**Worked Example -- Single Freelancer**

| Item | Amount (NT$) |
| --- | --- |
| Professional practice revenue | 2,000,000 |
| Deemed expense rate (30%) | (600,000) |
| Net professional income | 1,400,000 |
| Interest income | 30,000 |
| Total gross income | 1,430,000 |
| Less: Personal exemption | (97,000) |
| Less: Standard deduction | (131,000) |
| Less: Special deductions (none -- not wage earner) | 0 |
| Net taxable income | 1,202,000 |

Tax = 1,202,000 × 12% − 41,300 = **NT$102,940**

### 3.3 Worked Example -- Married with One Child

**Worked Example -- Married with One Child**

| Item | Amount (NT$) |
| --- | --- |
| Husband salary income | 1,800,000 |
| Wife professional income (net after deemed) | 700,000 |
| Total gross income | 2,500,000 |
| Less: Exemptions (3 × $97,000) | (291,000) |
| Less: Standard deduction (married) | (262,000) |
| Less: Wage special deduction (husband only) | (218,000) |
| Less: Pre-school child special deduction | (150,000) |
| Net taxable income | 1,579,000 |

Tax = 1,579,000 × 20% − 147,700 = **NT$168,100**

## Section 4 -- Filing

### 4.1 Filing Methods

**Filing Methods**

| Method | Description | Notes |
| --- | --- | --- |
| eFiling (網路申報) | Online via etax.nat.gov.tw | Most common; pre-filled data from withholding |
| Tax filing software | Downloadable IRX software | Offline preparation, online submission |
| Mobile filing | Via mobile app (手機報稅) | For simple returns |
| Paper filing | Physical forms at NTB | Declining usage |
| Tax agent filing | CPA files on behalf | Required for complex situations |

### 4.2 Filing Period and Deadlines

**Filing Period and Deadlines**

| Item | Date |
| --- | --- |
| Filing period | May 1 -- May 31 |
| Extension (for overseas taxpayers) | Automatic extension to June 30 if notified |
| Payment deadline | May 31 (same as filing deadline) |
| Instalment option | 2 instalments if tax >NT$30,000 (first by May 31, second by July 31) |
| Late filing penalty | Delinquent tax surcharge (滯納金): 1% per 2 days overdue, max 15% |

### 4.3 Withholding Tax (扣繳)

**Withholding Tax**

| Income Type | Withholding Rate (Resident) |
| --- | --- |
| Salary | Per withholding tables (progressive approximation) |
| Professional practice fees | 10% |
| Rent | 10% |
| Interest (bank) | 10% (final for most; included in return if total >NT$270,000) |
| Prizes | 10% (or 20% if non-resident) |
| Dividends (domestic) | Included in consolidated income; 8.5% credit (cap NT$80,000) |

### 4.4 Authentication for eFiling

**Authentication for eFiling**

| Method | Description |
| --- | --- |
| Citizen Digital Certificate (自然人憑證) | IC card issued by MOICA |
| Health IC card (健保卡) | NHI card + password |
| Mobile phone verification | Via telecom-linked identity |
| Financial certificate | Issued by banks |
| TW FidO | Biometric mobile authentication |

## Section 5 -- Edge Cases

### 5.1 Dividend Income -- Integrated Taxation (2018 Reform)

Since 2018, dividends are taxed under one of two methods (taxpayer chooses the more beneficial):

**Dividend Taxation Methods**

| Method | Treatment |
| --- | --- |
| Method A: Include in consolidated income | Add to gross income; claim 8.5% credit (cap NT$80,000) |
| Method B: Separate taxation | 28% flat rate on dividend income (no consolidation) |

Method B preferred for high-income taxpayers (marginal rate >28%).

### 5.2 Non-Resident Taxation

**Non-Resident Taxation**

| Rule | Detail |
| --- | --- |
| Resident | Present ≥183 days in tax year → progressive rates (5%--40%) |
| Non-resident (<183 days) | Flat withholding rates on Taiwan-source income |
| Non-resident salary | 18% (if total annual salary ≤NT$1.5M) or 5%--40% progressive |
| Non-resident professional fees | 20% |
| Non-resident dividends | 21% |

### 5.3 Alternative Minimum Tax (AMT / 基本稅額)

**Alternative Minimum Tax (AMT)**

| Item | Detail |
| --- | --- |
| Legislation | Income Basic Tax Act (所得基本稅額條例) |
| Threshold | NT$7,500,000 |
| Rate | 20% on amount exceeding threshold |
| Items added back | Overseas income, specific insurance payouts, tax-exempt gains |
| Comparison | Pay the HIGHER of: regular income tax OR AMT |

### 5.4 Property Transaction Income

- **Property Transaction Income rules** — Gains from selling real property acquired after Jan 1, 2016: subject to house/land consolidated income tax (房地合一稅), filed separately. Holding ≤2 years: 45%. Holding 2--5 years: 35%. Holding 5--10 years: 20%. Holding >10 years: 15%. Self-use residence (after 6 years): NT$4,000,000 exempt, 10% on excess.

### 5.5 Overseas Income (海外所得)

- **Overseas Income rules** — Included in AMT calculation if total overseas income ≥NT$1,000,000 in the year. NOT included in regular consolidated income tax. If total basic income (regular taxable + overseas + other additions) >NT$7,500,000, AMT applies.

### 5.6 Married Filing

**Married Filing**

| Option | When |
| --- | --- |
| Mandatory joint filing | All married couples must file jointly (combined household) |
| Separate calculation of tax | Salary/professional income may be calculated separately for each spouse |
| Best method | System auto-optimises in eFiling (choose lowest total tax) |

## Section 6 -- Itemised Deductions (列舉扣除額)

If choosing itemised over standard deduction:

**Itemised Deductions**

| Deduction | Limit |
| --- | --- |
| Insurance premiums (non-NHI) | NT$24,000 per person per year |
| NHI premiums (健保費) | No limit (fully deductible) |
| Medical expenses | No limit (net of insurance reimbursement) |
| Disaster losses | No limit (documented and approved by authority) |
| Charitable donations (general) | Up to 20% of gross income |
| Charitable donations (to government/schools) | No limit (100% deductible) |
| Rent paid for residence | NT$180,000 (cannot claim simultaneously with mortgage interest) |
| Mortgage interest (自用住宅) | NT$300,000 (minus savings interest income) |
| Political party donations | NT$200,000 per year |
| Election candidate donations | NT$200,000 per election |

## Section 7 -- Business Tax Interaction (營業稅)

**Business Tax Interaction**

| Scenario | Treatment |
| --- | --- |
| Professional practice revenue ≤NT$200,000/month | Exempt from business tax (VAT) |
| Professional practice revenue >NT$200,000/month | 5% business tax applies (VAT equivalent) |
| Small-scale business (小規模營業人) | 1% assessed by tax authority (quarterly) |
| VAT-registered business | 5% output tax - input tax; file bimonthly (odd months) |

## Section 8 -- Calendar of Key Dates

**Calendar of Key Dates**

| Date | Event |
| --- | --- |
| January 1 | Start of tax year |
| January 31 | Annual withholding statements issued by payers |
| March 31 | Business tax annual reconciliation (for registered businesses) |
| May 1--31 | Individual income tax filing and payment period |
| July 31 | Second instalment due (if elected) |
| September 30 | Estimated tax payment for current year (if no withholding) |
| December 31 | End of tax year |

## Section 9 -- Reference Material

**Reference Material**

| Topic | Reference |
| --- | --- |
| Income Tax Act | 所得稅法 (Ministry of Finance) |
| Progressive rate table | Income Tax Act Art. 5 |
| Professional income deemed rates | MOF announcement (annually updated) |
| Standard deduction | Income Tax Act Art. 5-1 |
| Exemptions | Income Tax Act Art. 5 |
| Special deductions | Income Tax Act Art. 17 |
| Dividend taxation | Income Tax Act Art. 15 (2018 reform) |
| Withholding | Income Tax Act Art. 88--92 |
| AMT | Income Basic Tax Act (所得基本稅額條例) |
| Property transaction tax | Income Tax Act Art. 14-4 to 14-8 (房地合一) |
| NTB Taipei | ntbt.gov.tw |
| eFiling portal | etax.nat.gov.tw |
| MOF | mof.gov.tw |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Taiwan CPA (會計師), tax agent (記帳士), or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
