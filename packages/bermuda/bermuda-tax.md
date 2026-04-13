---
name: bermuda-tax
description: >
  Use this skill whenever asked about Bermuda taxation, payroll tax, customs duties, or the absence of income tax and VAT in Bermuda. Trigger on phrases like "Bermuda tax", "Bermuda VAT", "Bermuda payroll tax", "Bermuda customs", or any request involving Bermuda tax compliance. Bermuda does NOT have income tax, capital gains tax, or VAT. Revenue is raised through payroll tax, customs duties, and various fees. ALWAYS read this skill before handling any Bermuda tax work.
version: 2.0
jurisdiction: BM
tax_year: 2025
category: international
---

# Bermuda Tax Compliance Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Bermuda |
| Tax | Payroll tax (primary), customs duties, land tax, stamp duty, social insurance |
| Currency | BMD (1:1 with USD) |
| Tax year | Calendar year |
| Primary legislation | Payroll Tax Act 1995 (as amended); Customs Tariff Act 1970 |
| Supporting legislation | Companies Act 1981; Land Tax Act 1967; Stamp Duties Act 1976 |
| Tax authority | Office of the Tax Commissioner |
| Filing portal | https://www.tax.gov.bm |
| Filing deadline | Payroll tax quarterly (Apr 15, Jul 15, Oct 15, Jan 15); annual reconciliation March 15 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a licensed Bermuda practitioner |
| Skill version | 2.0 |

### Tax Landscape Overview

| Tax Type | Status |
|---|---|
| Income Tax (personal) | None |
| Income Tax (corporate) | None |
| Capital Gains Tax | None |
| Value Added Tax (VAT) | None |
| Sales Tax | None |
| Withholding Tax | None |
| Payroll Tax | Yes -- primary revenue source |
| Customs Duties | Yes -- on imports |
| Land Tax | Yes -- on property |
| Stamp Duty | Yes -- on real estate transfers |
| Social Insurance | Yes -- contributory pension scheme |

Bermuda has a legislative guarantee (Tax Assurance Certificate) that no income, capital gains, or withholding taxes will be introduced before 2035.

### Payroll Tax Rates (Current)

| Employer Rate Tier | Employer Rate |
|---|---|
| Up to BMD 200,000 annual payroll | Reduced rate (concession) |
| BMD 200,001 -- 350,000 | Intermediate rate |
| BMD 350,001 -- 500,000 | Standard rate |
| Above BMD 500,000 | Standard rate (10.25%) |

| Employee Income Tier | Employee Rate |
|---|---|
| Up to BMD 48,000 | 0.50% |
| BMD 48,001 -- 96,000 | 9.25% |
| BMD 96,001 -- 200,000 | 10.00% |
| BMD 200,001 -- 500,000 | 11.50% |
| BMD 500,001 -- 1,000,000 | 12.50% |

Payroll tax is capped at BMD 1,000,000 per person per year.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown employer classification | Standard rate |
| Unknown employee income tier | Highest applicable rate |
| Unknown customs duty category | General merchandise rate (22.25%) |
| Unknown land tax ARV band | Higher rate band |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- employer payroll records for the quarter, number of employees, and total remuneration paid.

**Recommended** -- breakdown of remuneration by employee, employer classification (exempted undertaking vs local), prior quarter returns.

**Ideal** -- complete payroll system export, benefits-in-kind valuations, employer registration documents, prior annual reconciliation.

### Refusal Catalogue

**R-BM-1 -- Income tax computation.** "Bermuda does not have income tax. If the question relates to income tax in another jurisdiction, use the appropriate country skill."

**R-BM-2 -- VAT/sales tax computation.** "Bermuda does not have VAT or sales tax. No indirect tax return exists."

**R-BM-3 -- Economic substance detailed compliance.** "Economic substance requirements are too fact-sensitive. Escalate to a licensed Bermuda practitioner."

**R-BM-4 -- Insurance sector-specific rules.** "Insurance companies have specialised regulatory and tax requirements. Escalate."

---

## Section 3 -- Compliance Pattern Library

### 3.1 Employer Payment Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES, BONUS, COMMISSION | Payroll tax base | Include in taxable remuneration |
| BENEFITS IN KIND, HOUSING ALLOWANCE | Payroll tax base | Include -- benefits are taxable remuneration |
| PENSION CONTRIBUTION (employer) | Check | May be excluded from payroll tax base |
| REIMBURSEMENT (business expense) | EXCLUDE | Not remuneration if properly documented |
| CONTRACTOR PAYMENT | Check | If truly independent contractor, not payroll tax |
| DIRECTOR FEE | Payroll tax base | Include |

### 3.2 Customs Duty Categories

| Category | Duty Rate | Notes |
|---|---|---|
| General merchandise | 22.25% -- 25% | Most goods |
| Food items | 0% -- 10% | Many essentials at lower rates |
| Clothing and footwear | 6.5% | |
| Motor vehicles | 33.5% | Standard |
| Prescription medications | 0% | Exempt |
| Electronics/household goods | 25% | |
| Alcohol | High specific rates | |
| Tobacco | High specific rates | |

### 3.3 Social Insurance Contributions

| Component | Rate/Amount |
|---|---|
| Employer contribution | BMD 35.69 per week per employee |
| Employee contribution | BMD 35.69 per week per employee |
| Self-employed | BMD 63.10 per week |

---

## Section 4 -- Worked Examples

### Example 1 -- Payroll Tax for Standard Employer

**Input:** Employer with annual payroll BMD 600,000, 10 employees. Class not specified.

**Computation:**
- Employer pays payroll tax at standard rate (10.25% on total payroll)
- Employer payroll tax: BMD 600,000 x 10.25% = BMD 61,500
- Employee portion: deducted from each employee's pay at applicable tier rate
- File quarterly

### Example 2 -- Import of Goods

**Input:** Bermuda resident imports electronics valued at BMD 5,000.

**Computation:**
- Customs duty at applicable rate (general merchandise ~22.25%)
- Duty: BMD 5,000 x 22.25% = BMD 1,112.50
- No VAT. No sales tax.

### Example 3 -- Self-Employed Individual

**Input:** Self-employed person in Bermuda.

**Classification:**
- No income tax applies
- Social insurance contributions required (BMD 63.10/week)
- No payroll tax on self-employment income (payroll tax applies to employer-employee relationships only)

### Example 4 -- Real Estate Transfer

**Input:** Property sold for BMD 2,000,000.

**Computation:**
- First BMD 100,000: 2% = BMD 2,000
- BMD 100,001 -- 500,000: 4% = BMD 16,000
- BMD 500,001 -- 1,000,000: 6% = BMD 30,000
- Above BMD 1,000,000: 8% = BMD 80,000
- Total stamp duty: BMD 128,000

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 No Income Tax / No VAT Confirmation

Bermuda has no personal income tax, no corporate income tax, no capital gains tax, no VAT, no sales tax, no withholding tax. Tax Assurance Certificate guarantees this until 2035.

### 5.2 Payroll Tax Filing

Filing frequency: quarterly. Q1 deadline: April 15. Q2: July 15. Q3: October 15. Q4: January 15. Annual reconciliation: March 15 following year-end. Method: electronic via tax.gov.bm.

### 5.3 Land Tax

Assessed annually on the annual rental value (ARV) of land and buildings. Progressive rates by ARV band. Payable in instalments (quarterly or semi-annually).

### 5.4 Stamp Duty on Real Estate

Progressive rates: 2% on first BMD 100,000; 4% on 100,001--500,000; 6% on 500,001--1,000,000; 8% above 1,000,000.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Payroll Tax Exemptions and Concessions

Certain entities may receive payroll tax concessions or exemptions: hotels/tourism sector, new businesses, charitable organizations. Flag for practitioner -- concession eligibility must be confirmed with Tax Commissioner.

### 6.2 Exempt Company Payroll

Exempted company status relates to Companies Act provisions, NOT tax exemptions on payroll tax. Payroll tax applies to all employers including exempt companies. Verify if any concession rates apply.

### 6.3 Economic Substance

Entities carrying on "relevant activities" must demonstrate adequate economic substance in Bermuda. Relevant activities include: banking, insurance, fund management, financing and leasing, headquarters, shipping, distribution and service centre, intellectual property, holding entity. Flag for practitioner.

---

## Section 7 -- Excel Working Paper Template

```
BERMUDA TAX -- Working Paper
Period: [Quarter / Year]

A. PAYROLL TAX
  A1. Total remuneration paid                      ___________
  A2. Number of employees                          ___________
  A3. Employer classification (Class)              ___________
  A4. Employer payroll tax rate                    ___________
  A5. Employer payroll tax                         ___________
  A6. Employee payroll tax (per tier)              ___________

B. SOCIAL INSURANCE
  B1. Employer pension contributions               ___________
  B2. Employee pension contributions               ___________

C. CUSTOMS DUTIES (if applicable)
  C1. Import value                                 ___________
  C2. Duty rate                                    ___________
  C3. Total duty                                   ___________

REVIEWER FLAGS:
  [ ] Employer classification confirmed?
  [ ] Payroll tax cap checked (BMD 1M/person)?
  [ ] Concession eligibility confirmed?
  [ ] Economic substance filing required?
```

---

## Section 8 -- Bank Statement Reading Guide

### Bermuda Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| Butterfield, HSBC Bermuda | PDF, CSV | Date, Description, Debit, Credit, Balance |
| Clarien | CSV, PDF | Date, Narrative, Amount |

### Key Bermuda Banking Terms

| Term | Classification Hint |
|---|---|
| PAYROLL, SALARY | Remuneration -- payroll tax applies |
| CUSTOMS, DUTY | Import duty payment |
| LAND TAX | Property tax payment |
| PENSION, CONTRIBUTORY | Social insurance contribution |
| INSURANCE PREMIUM | May be exempt financial service |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- BERMUDA TAX
1. Are you an employer with employees in Bermuda?
2. How many employees do you have?
3. What is your total annual payroll?
4. Are you an exempted undertaking or local employer?
5. Do you import goods into Bermuda?
6. Do you own property in Bermuda?
7. Are any employees non-Bermudian (work permits)?
8. Have you applied for any payroll tax concessions?
9. Do you conduct any "relevant activities" for economic substance purposes?
10. Prior quarter payroll tax returns available?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Payroll tax rates | Payroll Tax Act 1995 (as amended); annual Budget |
| Payroll tax cap | Payroll Tax Act 1995 |
| Customs duties | Customs Tariff Act 1970 |
| Land tax | Land Tax Act 1967 |
| Stamp duty | Stamp Duties Act 1976 |
| Social insurance | Contributory Pensions Act 1970 |
| Economic substance | Economic Substance Act 2018 |
| Tax Assurance Certificate | Tax Assurance Act |

### International Reporting

Bermuda has a specific arrangement with the US regarding insurance. No general double taxation treaties.

---

## PROHIBITIONS

- NEVER state that Bermuda has income tax -- it does not
- NEVER state that Bermuda has VAT or sales tax -- it does not
- NEVER apply VAT calculations to Bermuda transactions
- NEVER apply income tax calculations to Bermuda entities
- NEVER ignore payroll tax obligations (primary compliance requirement)
- NEVER assume payroll tax rates without confirming current Budget rates
- NEVER guess economic substance requirements -- escalate to practitioner
- NEVER present calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
