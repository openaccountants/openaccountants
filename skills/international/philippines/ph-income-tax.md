---
name: ph-income-tax
description: Use this skill whenever asked about Philippines income tax for self-employed individuals or professionals. Trigger on phrases like "Philippines income tax", "BIR", "Bureau of Internal Revenue", "TRAIN law", "8% flat rate", "graduated tax", "Form 1701", "Form 1701Q", "OSD", "itemized deductions", "self-employed Philippines", "professional tax Philippines", "bir.gov.ph", "quarterly ITR Philippines", or any question about Philippine income tax rates, filing, deductions, or the 8% option. Covers graduated rates, 8% flat rate option, quarterly and annual filing, deductions, and BIR compliance. ALWAYS read this skill before touching any Philippines income tax work.
version: 1.0
jurisdiction: PH
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Jonathan I. Ruiz, CPA
review_status: current
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PH Income Tax

## Section 1 -- Quick Reference

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
| Annual filing deadline | 15 April of the following year |
| Quarterly filing deadline | BIR Form 1701Q: within 45 days after end of quarter (Q1: 15 May, Q2: 15 August, Q3: 15 November) |
| Validated by | Pending -- requires sign-off by a Philippine CPA |
| Validation date | Pending |
| Skill version | 1.0 |

### Graduated Income Tax Rates (from 1 January 2023 onwards)

**Graduated Income Tax Rates (from 1 January 2023 onwards)**

| Net Taxable Income (₱) | Tax Due |
| --- | --- |
| 0 -- 250,000 | 0% |
| 250,001 -- 400,000 | 15% of excess over ₱250,000 |
| 400,001 -- 800,000 | ₱22,500 + 20% of excess over ₱400,000 |
| 800,001 -- 2,000,000 | ₱102,500 + 25% of excess over ₱800,000 |
| 2,000,001 -- 8,000,000 | ₱402,500 + 30% of excess over ₱2,000,000 |
| Above 8,000,000 | ₱2,202,500 + 35% of excess over ₱8,000,000 |

### 8% Flat Rate Option

**8% Flat Rate Option**

| Item | Detail |
| --- | --- |
| Rate | 8% of gross sales/receipts and other non-operating income in excess of ₱250,000 |
| In lieu of | Graduated income tax AND 3% percentage tax |
| Eligibility | Purely self-employed/professionals; annual gross sales/receipts ≤₱3,000,000; NOT VAT-registered |
| Election | Must elect each year via BIR Form 1905 or Q1 filing (Form 1701Q) |
| Default | Graduated income tax (if no election made) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown tax regime election | Graduated rates (default per BIR) |
| Unknown deduction method | OSD (40% of gross) |
| Unknown VAT/percentage tax status | Non-VAT until confirmed |
| Unknown business-use % | 0% deduction |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement or record of gross sales/receipts for the year, TIN (Tax Identification Number), and confirmation of whether 8% flat rate or graduated rates are elected.

**Recommended** -- all sales invoices/official receipts, purchase records, BIR Form 2307 certificates of withholding, prior year ITR (Form 1701/1701A), BIR registration (Form 2303 / Certificate of Registration).

**Ideal** -- complete books of accounts, general ledger, trial balance, quarterly ITRs (Form 1701Q), percentage tax returns (Form 2551Q), VAT returns (Form 2550Q) if applicable.

### Refusal Catalogue

- **R-PH-1 -- Corporation or partnership** — This skill covers sole proprietors and individual professionals only. Corporations file Form 1702. Escalate to a CPA.
- **R-PH-2 -- VAT-registered taxpayer** — VAT-registered taxpayers have additional obligations (Form 2550Q/2550M) and cannot use the 8% flat rate option. Income tax still applies but filing differs.
- **R-PH-3 -- Mixed income earner (employment + business)** — Mixed income earners can use the 8% option only on business income, while employment income is taxed at graduated rates. Requires careful computation.
- **R-PH-4 -- Non-resident alien** — Non-resident aliens have different rules (NRA-ETB or NRA-NETB). Out of scope.

## Section 3 -- Two Tax Options for Self-Employed

### 3.1 Option 1: Graduated Income Tax

**Option 1: Graduated Income Tax computation steps**

| Step | Description |
| --- | --- |
| Gross sales/receipts | Total business revenue |
| Less: Cost of sales/services | Direct costs |
| = Gross income |  |
| Less: Deductions (itemized OR OSD) |  |
| = Net taxable income | Apply graduated rates |

**Deduction methods**

| Method | Detail |
| --- | --- |
| Itemized deductions | Actual business expenses with supporting documentation (receipts, invoices, BIR-registered) |
| OSD (Optional Standard Deduction) | 40% of gross sales/receipts (no documentation required) |

- **Percentage tax alongside graduated rates** — If graduated rates are elected, the taxpayer is ALSO subject to 3% Percentage Tax (quarterly, Form 2551Q) on gross sales/receipts, unless VAT-registered (12% VAT instead).

### 3.2 Option 2: 8% Flat Rate

**Option 2: 8% Flat Rate computation steps**

| Step | Description |
| --- | --- |
| Gross sales/receipts + other non-operating income | Total |
| Less: ₱250,000 (if purely self-employed) | Exempt threshold |
| × 8% | Tax due |

- **No deductions or percentage tax** — No deductions allowed. No percentage tax due.

### 3.3 When to Choose 8% vs Graduated

**When to Choose 8% vs Graduated**

| Scenario | Better Option |
| --- | --- |
| Low expenses relative to revenue | 8% flat rate |
| High expenses (>60% of gross) | Graduated with itemized deductions |
| Moderate expenses, wants simplicity | 8% flat rate |
| Gross exceeds ₱3,000,000 | Must use graduated (8% not available) |
| VAT-registered | Must use graduated |

### 3.4 Election Procedure

**Election Procedure**

| Action | Detail |
| --- | --- |
| New registration | Check 8% option on BIR Form 1901 |
| Existing taxpayer switching | File BIR Form 1905 before first quarter, OR indicate on first Q1 filing (Form 1701Q) |
| Annual renewal | Must elect every year; does not carry over automatically |
| Exceeding ₱3M threshold | Must switch to graduated + 12% VAT from the month threshold is exceeded |

## Section 4 -- Quarterly and Annual Filing

### 4.1 Quarterly Income Tax Return (Form 1701Q)

**Quarterly Income Tax Return (Form 1701Q)**

| Quarter | Period | Deadline |
| --- | --- | --- |
| Q1 | January -- March | 15 May |
| Q2 | April -- June | 15 August |
| Q3 | July -- September | 15 November |
| Q4 | Covered by annual return | -- |

### 4.2 Annual Income Tax Return

**Annual Income Tax Return**

| Form | Who Files | Deadline |
| --- | --- | --- |
| Form 1701 | Self-employed / professionals with itemized deductions or mixed income | 15 April |
| Form 1701A | Self-employed using 8% option or OSD; employees with mixed income from single employer | 15 April |

### 4.3 Percentage Tax (if graduated, non-VAT)

**Percentage Tax (if graduated, non-VAT)**

| Form | Period | Deadline |
| --- | --- | --- |
| Form 2551Q | Quarterly | Within 25 days after end of quarter |
| Rate | 3% of gross sales/receipts |  |

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
| Bad debts (actually written off) | Deductible |
| Interest expense (not on tax deficiency) | Deductible, reduced by 20% of interest income |
| Contributions to pension trust | Deductible |
| Research and development | Deductible |

### 5.2 Non-Deductible Expenses

**Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Personal/family expenses | Not business-related |
| Capital expenditure | Through depreciation |
| Income tax | Tax on income |
| Losses from tax-exempt income | Not deductible |
| Bribes, kickbacks | Public policy |
| Entertainment, amusement, recreation | Limited to 0.50% of net revenue (selling) or 1% (service) |

## Section 6 -- Worked Examples

### Example 1 -- 8% Flat Rate

**Input:** Freelance graphic designer. Gross receipts ₱2,400,000. No employees.

**Tax:** (₱2,400,000 - ₱250,000) × 8% = ₱172,000. No percentage tax. No documentation of expenses required.

### Example 2 -- Graduated with OSD

**Input:** Same freelancer, ₱2,400,000 gross.

**OSD:** 40% × ₱2,400,000 = ₱960,000.
**Net taxable income:** ₱2,400,000 - ₱960,000 = ₱1,440,000.
**Tax:** ₱102,500 + (₱1,440,000 - ₱800,000) × 25% = ₱102,500 + ₱160,000 = ₱262,500.
**Plus 3% percentage tax:** ₱2,400,000 × 3% = ₱72,000.
**Total tax burden:** ₱262,500 + ₱72,000 = ₱334,500.

**Comparison:** 8% flat rate (₱172,000) is significantly better for this taxpayer.

### Example 3 -- Graduated with Itemized Deductions

**Input:** Consultant, gross receipts ₱2,400,000, documented expenses ₱1,800,000.

**Net taxable income:** ₱2,400,000 - ₱1,800,000 = ₱600,000.
**Tax:** ₱22,500 + (₱600,000 - ₱400,000) × 20% = ₱22,500 + ₱40,000 = ₱62,500.
**Plus 3% percentage tax:** ₱72,000.
**Total:** ₱134,500. Better than 8% due to high expenses.

## Section 7 -- Penalties

**Penalties**  _(NIRC ss.248–250, 255; RR 21-2018; RA 11976 (EOPT). Corrected by Jonathan I. Ruiz (CPA, Philippines))_

| Offence | Penalty |
| --- | --- |
| Late filing (general) | 25% surcharge on tax due (NIRC s.248). **Micro/small taxpayers** (gross sales <PHP 3M, and PHP 3M–20M) get a REDUCED civil penalty and a 50% interest reduction under the EOPT Act (RA 11976, in force 22 Jan 2024) — confirm the exact reduced figures against the implementing RR before relying on them. |
| Late payment | 12% interest per annum on unpaid tax (double the 6% BSP legal rate) — NIRC s.249 as amended by TRAIN (RA 10963), per RR 21-2018 |
| Failure to file the INCOME TAX RETURN | NIRC s.255: fine of not less than PHP 10,000 (no stated cap) plus imprisonment of 1–10 years |
| Failure to file an INFORMATION RETURN | NIRC s.250: PHP 1,000 per failure, capped at PHP 25,000 per calendar year |
| Substantial underdeclaration | 50% surcharge |
| Fraud | 50% surcharge + criminal penalties |
| Failure to register | PHP 5,000 – PHP 20,000 fine and/or imprisonment |

## Section 8 -- Reference Material

### Key BIR Forms

**Key BIR Forms**

| Form | Purpose |
| --- | --- |
| 1701 | Annual ITR -- self-employed/professional (itemized or mixed) |
| 1701A | Annual ITR -- 8% or OSD |
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
| Percentage tax | NIRC Section 116 |
| Filing | NIRC Section 51; RR 11-2018 |

## Prohibitions

- NEVER allow the 8% option for VAT-registered taxpayers
- NEVER allow the 8% option if gross sales/receipts exceed ₱3,000,000
- NEVER claim deductions under the 8% flat rate option
- NEVER apply 8% flat rate without confirming annual election
- NEVER ignore the 3% percentage tax obligation for graduated-rate non-VAT taxpayers
- NEVER forget quarterly filing (Form 1701Q) -- penalties are steep
- NEVER present calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
