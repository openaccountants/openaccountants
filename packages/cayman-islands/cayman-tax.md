---
name: cayman-tax
description: >
  Use this skill whenever asked about Cayman Islands taxation or the absence of direct taxes. Trigger on phrases like "Cayman tax", "Cayman Islands VAT", "Cayman Islands income tax", "Cayman corporate tax", or any request involving Cayman Islands tax compliance. The Cayman Islands does NOT have income tax, capital gains tax, VAT, payroll tax, or any direct taxes. Revenue is raised through import duties, work permit fees, and financial services fees. ALWAYS read this skill before handling any Cayman Islands tax work.
version: 2.0
jurisdiction: KY
tax_year: 2025
category: international
---

# Cayman Islands Tax Compliance Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Cayman Islands |
| Tax | Import duties (primary), work permit fees, financial services fees, stamp duty, tourism tax |
| Currency | KYD (1 KYD = ~1.22 USD) |
| Tax year | N/A (no income tax) |
| Primary legislation | Tax Concessions Act (Revised); Customs Tariff Act (Revised) |
| Supporting legislation | Companies Act (Revised); Economic Substance Act, 2018 |
| Tax authority | None dedicated -- Dept of Commerce and Investment; Customs and Border Control |
| Filing portal | N/A -- no direct tax filing |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a licensed Cayman practitioner |
| Skill version | 2.0 |

### Tax Landscape

| Tax Type | Status |
|---|---|
| Income Tax (personal/corporate) | None |
| Capital Gains Tax | None |
| VAT / Sales Tax | None |
| Payroll Tax | None |
| Withholding Tax | None |
| Property Tax (annual) | None |
| Estate / Inheritance Tax | None |
| Import Duties | Yes -- primary revenue source |
| Work Permit Fees | Yes |
| Financial Services Fees | Yes |
| Stamp Duty | Yes -- on real estate transfers |
| Tourism Tax | Yes -- 13% hotel tax |

Tax Undertaking Certificate: up to 50 years for companies, 30 years for individuals.

### Import Duty Rates

| Category | Rate |
|---|---|
| General merchandise | 22% -- 27% |
| Food | 15% -- 22% |
| Motor vehicles (standard) | 29.5% |
| Luxury vehicles | 42% |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown duty rate | General merchandise (22%) |
| Unknown economic substance | Assume relevant activity |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- nature of inquiry (employment, imports, entity registration, property).

**Recommended** -- entity type, number of employees, import values, property details.

**Ideal** -- complete registration documents, prior customs filings, economic substance reports.

### Refusal Catalogue

**R-KY-1 -- Income tax.** "Cayman Islands has no income tax."

**R-KY-2 -- VAT/sales tax.** "Cayman Islands has no VAT or sales tax."

**R-KY-3 -- Economic substance detail.** "Escalate to specialist."

**R-KY-4 -- CRS/FATCA reporting.** "Escalate to specialist."

---

## Section 3 -- Compliance Pattern Library

### 3.1 Employer Obligations

| Obligation | Amount/Rate | Notes |
|---|---|---|
| Pension (mandatory) | 10% (5% employer + 5% employee) | National Pensions Act |
| Health insurance | Employer must provide | Minimum coverage prescribed |
| Work permit fees | Varies by category | Non-Caymanian workers |
| Payroll tax | None | |

### 3.2 Import Duty Categories

| Category | Rate | Notes |
|---|---|---|
| General merchandise | 22% | Most goods |
| Food items | 15% -- 22% | |
| Motor vehicles (standard) | 29.5% | |
| Luxury vehicles | 42% | |
| Fuel | Specific rates | Per gallon |

### 3.3 Entity Registration Fees

| Entity Type | Annual Fee (approx. KYD) |
|---|---|
| Exempted company | 850 -- 3,000+ |
| Exempted limited partnership | 750 -- 2,500+ |
| Mutual fund (regulated) | 3,000 -- 4,000+ |

---

## Section 4 -- Worked Examples

### Example 1 -- Import Duty

**Input:** Office equipment KYD 10,000.

**Computation:** Duty at 22%: KYD 2,200. No VAT. No sales tax.

### Example 2 -- Employment Obligations

**Input:** Employee at KYD 60,000/year, non-Caymanian.

**Classification:** No income tax. No payroll tax. Pension: KYD 6,000 (5%+5%). Health insurance: mandatory. Work permit: required, annual fee.

### Example 3 -- Hotel Tax

**Input:** Hotel room charges KYD 500.

**Computation:** Tourism tax: 13% x KYD 500 = KYD 65.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 No Direct Taxes

No income tax of any kind. No capital gains tax. No VAT/sales tax. No withholding tax. No payroll tax. No property tax. No estate tax. Tax Undertaking Certificates guarantee this for up to 50 years.

### 5.2 Stamp Duty

Real estate transfers: 7.5% of consideration or market value. First-time Caymanian buyer concessions may apply.

### 5.3 Pension and Health Insurance

Mandatory for all employees aged 18-65. Pension: 10% split equally. Health insurance: employer must provide compliant plan.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Economic Substance

Entities conducting relevant activities must demonstrate adequate substance. Flag for specialist.

### 6.2 Duty Concessions

Development agreements may include duty waivers. Flag for practitioner.

### 6.3 Real Estate (Non-Caymanian)

Foreign ownership restrictions may apply. Stamp duty 7.5%. Flag for practitioner.

---

## Section 7 -- Excel Working Paper Template

```
CAYMAN ISLANDS -- Working Paper

A. IMPORT DUTIES
  A1. Import value                                 ___________
  A2. Category / duty rate                         ___________
  A3. Total duty                                   ___________

B. EMPLOYMENT OBLIGATIONS
  B1. Total payroll                                ___________
  B2. Pension contributions (10%)                  ___________
  B3. Health insurance cost                        ___________
  B4. Work permit fees                             ___________

C. ENTITY FEES
  C1. Annual registration fee                      ___________

REVIEWER FLAGS:
  [ ] Economic substance filing required?
  [ ] Work permits current?
  [ ] Pension contributions current?
```

---

## Section 8 -- Bank Statement Reading Guide

| Bank | Format | Key Fields |
|---|---|---|
| Cayman National, Butterfield | PDF, CSV | Date, Description, Debit, Credit, Balance |
| CIBC FirstCaribbean | CSV | Date, Narrative, Amount |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- CAYMAN ISLANDS
1. Nature of inquiry (employment, imports, entity, property)?
2. Entity type (exempted company, LP, fund)?
3. Employees in Cayman? How many?
4. Non-Caymanian employees (work permits)?
5. Import goods into Cayman?
6. Own property in Cayman?
7. Relevant activities for economic substance?
8. Hotel/tourism operations?
9. Annual registration fee current?
10. Prior customs/duty filings available?
```

---

## Section 10 -- Reference Material

| Topic | Reference |
|---|---|
| Tax concessions | Tax Concessions Act (Revised) |
| Customs duties | Customs Tariff Act (Revised) |
| Companies | Companies Act (Revised) |
| Economic substance | Economic Substance Act, 2018 |
| Pensions | National Pensions Act |
| Health insurance | Health Insurance Act |
| Stamp duty | Stamp Duty Act |
| Tourism tax | Tourism Accommodation Tax |

---

## PROHIBITIONS

- NEVER state Cayman Islands has income tax -- it does not
- NEVER state Cayman Islands has VAT or sales tax -- it does not
- NEVER state Cayman Islands has payroll tax -- it does not
- NEVER apply direct tax calculations to Cayman entities
- NEVER ignore import duty obligations
- NEVER ignore economic substance requirements
- NEVER ignore CRS/FATCA reporting for financial institutions
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
