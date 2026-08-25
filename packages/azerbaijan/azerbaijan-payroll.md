---
name: azerbaijan-payroll
description: Use this skill whenever asked about Azerbaijan payroll processing for employed persons. Trigger on phrases like "Azerbaijan payroll", "Azerbaijani salary", "emek haqqi", "PIT withholding Azerbaijan", "income tax of physical persons", "SSPF", "DSMF", "social insurance Azerbaijan", "unemployment insurance contribution", "mandatory medical insurance Azerbaijan", "unified payroll declaration", "net salary Azerbaijan", "gross to net AZN", "salary calculation Azerbaijan", "minimum wage Azerbaijan", "oil/gas sector payroll", "non-oil private sector PIT holiday", or any question about computing employee pay, withholding tax, or social/health/unemployment contributions for Azerbaijan-based employees. This skill covers PIT withheld at source (PAYE-style), State Social Protection Fund (SSPF) contributions, the Unemployment Insurance Contribution (UIC), mandatory medical insurance, the 2025 non-oil private-sector PIT holiday and its 2026 replacement, and the unified monthly payroll declaration. ALWAYS read this skill before processing any Azerbaijan payroll. MUST be loaded alongside payroll-workflow-base.
version: 0.1
jurisdiction: AZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Azerbaijan Payroll

## Azerbaijan Payroll Skill v0.1

> **Tier 2 — research-verified.** Figures below are sourced from PwC Worldwide Tax Summaries, the State Tax Service of Azerbaijan (taxes.gov.az), Mercans, Caspian Legal Center, APA.az and EY. They have **not** yet been signed off by a licensed Azerbaijani accountant. Any line marked **[RESEARCH GAP — reviewer to confirm]** must be verified against the Tax Code before the output is relied upon.

> **TWO HARD BRANCHES BEFORE YOU COMPUTE ANYTHING.** Azerbaijani payroll depends on (1) the **tax year** and (2) the **employment sector**.
> - **Tax year:** 2025 is the **final year** of the 2019–2025 seven-year PIT holiday for the non-oil/gas private sector (0% PIT up to AZN 8,000/month). The holiday **expired 31 Dec 2025**; from **1 Jan 2026** a new progressive PIT and revised social/health thresholds apply. Do **not** apply 2026 brackets to 2025 wages, or vice versa (PwC — Significant developments).
> - **Sector:** "non-oil/gas, non-government **PRIVATE** sector" is the default and carries the holiday/subsidy rules. "**Oil/gas** sector" and "**government/state** sector" use the standard 14%/25% PIT and the 3%/22% SSPF split, which differ materially (PwC — Taxes on personal income; Other taxes).

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Azerbaijan (Republic of Azerbaijan) |
| Currency | AZN (Azerbaijani manat) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January – 31 December) |
| Tax withholding system | PIT (income tax of physical persons) withheld at source, PAYE-style — remitted on the **same day** wages are paid (Tax Code; PwC — Tax administration) |
| Tax authority | State Tax Service under the Ministry of Economy (taxes.gov.az) |
| Social security authority | State Social Protection Fund (SSPF / DSMF), administered jointly via the unified payroll declaration |
| Key legislation | Tax Code of the Republic of Azerbaijan (Income Tax of Physical Persons, Arts. 96–101); Law "On Social Insurance"; Law "On Unemployment Insurance"; Mandatory Medical Insurance legislation |
| Filing portal | e-taxes.gov.az / www.taxes.gov.az |
| Monthly filing | Unified payroll declaration (PIT + SSPF + UIC + medical) — due **by the 20th** of the following month (taxes.gov.az tax calendar) |
| Minimum monthly wage (2025) | AZN 400 (raised from AZN 345, Presidential Order, from 1 Jan 2025) (APA.az / AZERTAC) |
| Validated by | Pending — requires sign-off by a licensed Azerbaijani accountant |
| Skill version | 0.1 |

**Conservative defaults (apply when an input is missing)**

| Ambiguity | Default | Rationale |
| --- | --- | --- |
| Tax year not stated | 2025 rules (holiday in force) | The requested year is 2025; the holiday applied for the full year (PwC — Significant developments) |
| Sector not stated | Non-oil/gas **private** sector | Most employers fall here; carries the holiday/subsidy rules (PwC) |
| 2025 non-oil private PIT, wage ≤ AZN 8,000 | 0% PIT | 7-year holiday in force through 31 Dec 2025 (PwC) |
| State subsidy on private SSPF (through 2025) | Treat as 100% subsidised | Confirmed schedule, Law "On Social Insurance" / APA.az |
| State subsidy from 2026 | 80% (2026–2028) | Reduces per statutory schedule (APA.az) |
| Whether subsidy reduces remittance or is reimbursed | **[RESEARCH GAP — reviewer to confirm]** | Mechanism not confirmed from a fetched circular |

**Red-flag thresholds (escalate to a human accountant)**

| Threshold | Value |
| --- | --- |
| HIGH single monthly gross | AZN 8,000 (crosses every PIT/medical/SSPF band) |
| HIGH sector ambiguity | Any oil/gas or government indicator |
| MEDIUM tax-year straddle | Pay period spanning Dec 2025 / Jan 2026 |
| LOW conservative-default count | > 3 defaults applied in one run |

## Section 2 — Required Inputs and Refusal Catalogue

### Required inputs

- **Minimum viable** — gross monthly salary per employee, the **tax year**, and the **sector** (non-oil private / oil-gas / government). Acceptable bank statements from: Kapital Bank, PASHA Bank, International Bank of Azerbaijan (IBA), AccessBank, Bank Respublika, Xalq Bank, or any other.
- **Recommended** — employee VOEN (TIN), employment start date, prior-period unified declaration, confirmation of subsidy eligibility.
- **Ideal** — full employee register with each person's sector flag, the company's SSPF registration, and the prior-month declaration for cumulative checks.

### Refusal catalogue

- **R-AZ-P-1 — Self-employed / sole-trader income** — Trigger: individual not on an employer payroll (simplified-tax entrepreneur, freelancer). Message: "This skill covers **employer payroll** only. Self-employed taxation is out of scope — use a qualified practitioner."
- **R-AZ-P-2 — Annual individual PIT return** — Trigger: user asks to file the annual personal return (foreign-source income, income not taxed at source). Message: "This skill covers monthly payroll withholding, not the annual individual PIT return (due 31 March). Out of scope."
- **R-AZ-P-3 — Free economic / special zone payroll** — Trigger: Alat FEZ or other designated-zone employer. Message: "FEZ and special-regime employers have bespoke contribution rules. Out of scope — refer to a local practitioner."
- **R-AZ-P-4 — Expatriate / cross-border split payroll** — Trigger: employee with tax residence outside Azerbaijan, treaty relief, or split-payroll arrangement. Message: "Cross-border residence and treaty allocation are out of scope. Refer to a cross-border specialist."
- **R-AZ-P-5 — Pension / disability / benefit calculations** — Trigger: user asks to compute SSPF pension entitlement or sickness benefit. Message: "Benefit entitlement calculations are out of scope. This skill computes payroll contributions only."
- **R-AZ-P-6 — VAT / corporate tax** — Trigger: user asks about EDV or profit tax. Message: "Use azerbaijan-vat for EDV and the corporate-tax skill for profit tax. This skill handles payroll only."

## Section 3 — Income Tax Withholding (PIT / Income Tax of Physical Persons)

The employer withholds PIT at source and **remits it on the same day** the income is paid to the employee (Tax Code; PwC — Tax administration). PIT is computed **monthly on taxable employment income** (gross salary). There is no separate personal allowance under the holiday regime — the **0% band IS the relief** for the private sector in 2025.

### 3.1 Non-oil/gas, non-government PRIVATE sector — **2025** (holiday, in force 2019 → 31 Dec 2025)

**3.1 Non-oil/gas PRIVATE sector 2025 PIT bands**  _(PwC — Taxes on personal income & Significant developments. This holiday expired 31 Dec 2025; it is the relevant rule for the 2025 tax year.)_

| Monthly taxable income (AZN) | Rate | Cumulative monthly PIT |
| --- | --- | --- |
| 0 – 8,000 | 0% | 0 |
| Over 8,000 | 14% on the excess above 8,000 | 14% × (income − 8,000) |

**Check:** at AZN 10,000 → 14% × (10,000 − 8,000) = 14% × 2,000 = **AZN 280**.

### 3.2 Oil/gas sector and government/state sector — standard rates (all years)

**3.2 Oil/gas and government sector PIT bands**  _(PwC — Taxes on personal income.)_

| Monthly taxable income (AZN) | Rate | Cumulative monthly PIT |
| --- | --- | --- |
| 0 – 2,500 | 14% | 14% × income |
| Over 2,500 | AZN 350 + 25% on the excess above 2,500 | 350 + 25% × (income − 2,500) |

**Cumulative check:** at AZN 2,500 → 14% × 2,500 = **AZN 350**, which is exactly the fixed amount carried into the second band — consistent. At AZN 5,000 → 350 + 25% × 2,500 = **AZN 975**.

### 3.3 Non-oil/gas PRIVATE sector — NEW progressive structure **from 1 Jan 2026** (replaces the expired holiday)

**3.3 New progressive PIT structure from 2026**  _(PwC — Significant developments; Mercans statutory alert; Caspian Legal Center (2026 amendments).)_

| Monthly taxable income (AZN) | Rate | Cumulative monthly PIT |
| --- | --- | --- |
| 0 – 2,500 | 3% (rises to 5% in 2027, 7% from 2028) | 3% × income |
| 2,501 – 8,000 | AZN 75 + 10% on the excess above 2,500 | 75 + 10% × (income − 2,500) |
| Over 8,000 | AZN 625 + 14% on the excess above 8,000 | 625 + 14% × (income − 8,000) |

**Cumulative checks:** at AZN 2,500 → 3% × 2,500 = **AZN 75** (matches band-2 base). At AZN 8,000 → 75 + 10% × 5,500 = 75 + 550 = **AZN 625** (matches band-3 base). Consistent.

**2026 low-income relief:** an **AZN 200/month** PIT exemption is reported where monthly income does not exceed AZN 2,500 (Caspian Legal Center). **[RESEARCH GAP — reviewer to confirm against the Tax Code text.]** This skill computes 2026 PIT **without** the AZN 200 relief by default (conservative); apply it only once verified.

## Section 4 — Social Insurance (SSPF / DSMF) — Employee and Employer

State social insurance is computed **monthly on gross salary**, split at the **AZN 200** threshold for the non-oil private sector. There is **no upper ceiling** (PwC — Other taxes).

### 4.1 Non-oil/gas PRIVATE sector — SSPF (2019–2025; wages ≤ AZN 8,000 continue on this split in 2026)

**4.1 Non-oil/gas private sector SSPF split**  _(PwC — Other taxes.)_

| Portion of gross | Employee | Employer |
| --- | --- | --- |
| First AZN 200 | 3% | 2% |
| Above AZN 200 | AZN 6 + 10% on the excess | AZN 44 + 15% on the excess |

the employee base AZN 6 = 3% × 200 (consistent). The employer base **AZN 44 does NOT equal 2% × 200 (= AZN 4)** — AZN 44 is the legacy fixed amount (22% × 200) carried forward in the statutory formula, while the headline rate on the first band is quoted as 2%. PwC states both "2% on first AZN 200" and "AZN 44 base above AZN 200" together. **[RESEARCH GAP — reviewer to confirm the exact statutory first-band employer figure: AZN 4 (2% × 200) or AZN 44 (legacy).]** This skill applies PwC's **AZN 44 + 15%** wording for the employer above-threshold computation.

- **Worked check (AZN 1,000 gross)** — Employee SSPF = 6 + 10% × (1,000 − 200) = 6 + 80 = **AZN 86** Employer SSPF = 44 + 15% × (1,000 − 200) = 44 + 120 = **AZN 164**  _(PwC — Other taxes.)_

### 4.2 Oil/gas and government sectors — SSPF (standard, all years)

**4.2 Oil/gas and government sectors SSPF**  _(PwC — Other taxes.)_

| Base | Employee | Employer |
| --- | --- | --- |
| Gross monthly salary (no ceiling) | 3% | 22% |

### 4.3 High earners FROM 1 Jan 2026 (non-oil private) — wages above AZN 8,000

**4.3 High earners SSPF from 2026**  _(Mercans statutory alert; PwC — Significant developments. The combined rate on the > AZN 8,000 portion falls from 25% to 21% from 2026.)_

| Portion of gross | Employee | Employer | Combined |
| --- | --- | --- | --- |
| First AZN 8,000 | per §4.1 split | per §4.1 split | per §4.1 |
| Above AZN 8,000 | 10% | 11% | 21% |

### 4.4 State subsidy on private-sector social insurance

**4.4 State subsidy schedule**  _(Law "On Social Insurance"; APA.az. Excludes oil/gas operations.)_

| Period | Share of private-sector SSPF covered by state subsidy |
| --- | --- |
| 1 Jan 2023 – 31 Dec 2025 | 100% |
| 2026 – 2028 | 80% |
| 2029 – 2030 | 60% |
| 2031 – 2032 | 40% |

**Whether the subsidy reduces the amount remitted or is reimbursed separately is [RESEARCH GAP — reviewer to confirm].**

## Section 5 — Unemployment Insurance Contribution (UIC) and Mandatory Medical Insurance

### 5.1 Unemployment Insurance Contribution (UIC) — all sectors (since 1 Jan 2018)

**5.1 UIC all sectors**  _(PwC — Other taxes; Mercans. Unchanged for 2026.)_

| Base | Employee | Employer | Total |
| --- | --- | --- | --- |
| Gross monthly salary | 0.5% | 0.5% | 1% |

### 5.2 Mandatory Medical (Health) Insurance — **2021–2025** regime

**5.2 Mandatory Medical Insurance 2021-2025**  _(PwC — Other taxes (effective 1 Jan 2021).)_

| Portion of gross | Employee | Employer |
| --- | --- | --- |
| First AZN 8,000 | 2% | 2% |
| Above AZN 8,000 | AZN 160 + 0.5% on the excess | AZN 160 + 0.5% on the excess |

base AZN 160 = 2% × 8,000 (consistent for both sides).

### 5.3 Mandatory Medical (Health) Insurance — **from 1 Jan 2026** (threshold lowered to AZN 2,500)

**5.3 Mandatory Medical Insurance from 2026**  _(Mercans statutory alert; PwC — Significant developments; Caspian Legal Center. The total rate on the AZN 2,500–8,000 band drops from 4% to 1%. Exact wording (whether the 2% applies to the first AZN 2,500 only) is corroborated by Mercans and Caspian but the official confirmation circular was not fetched — [RESEARCH GAP — reviewer to confirm].)_

| Portion of gross | Employee | Employer |
| --- | --- | --- |
| First AZN 2,500 | 2% | 2% |
| Above AZN 2,500 | 0.5% | 0.5% |

## Section 6 — Combined Contribution Summary Tables

### 6.1 Non-oil/gas PRIVATE sector — **2025**, gross **AZN 1,000** (illustrative totals)

**6.1 Combined contributions AZN 1,000 gross**

| Component | Employee | Employer | Total |
| --- | --- | --- | --- |
| PIT (0% ≤ 8,000) | 0.00 | — | 0.00 |
| SSPF (6 + 10%×800 / 44 + 15%×800) | 86.00 | 164.00 | 250.00 |
| UIC (0.5% / 0.5%) | 5.00 | 5.00 | 10.00 |
| Medical (2% / 2%) | 20.00 | 20.00 | 40.00 |
| **Total deductions / contributions** | **111.00** | **189.00** | **300.00** |

*Employee column: 0 + 86 + 5 + 20 = 111.00. Employer column: 164 + 5 + 20 = 189.00. Total column: 0 + 250 + 10 + 40 = 300.00. All reconcile.* The 100% state subsidy through 2025 applies to the SSPF employer/employee amounts (mechanism is a [RESEARCH GAP — reviewer to confirm]).

### 6.2 Oil/gas or government sector — **2025**, gross **AZN 5,000** (illustrative totals)

**6.2 Combined contributions AZN 5,000 gross**

| Component | Employee | Employer | Total |
| --- | --- | --- | --- |
| PIT (350 + 25%×2,500) | 975.00 | — | 975.00 |
| SSPF (3% / 22%) | 150.00 | 1,100.00 | 1,250.00 |
| UIC (0.5% / 0.5%) | 25.00 | 25.00 | 50.00 |
| Medical (2% / 2%) | 100.00 | 100.00 | 200.00 |
| **Total deductions / contributions** | **1,250.00** | **1,225.00** | **2,475.00** |

*Employee column: 975 + 150 + 25 + 100 = 1,250.00. Employer column: 1,100 + 25 + 100 = 1,225.00. Total: 975 + 1,250 + 50 + 200 = 2,475.00. All reconcile. No state subsidy applies (oil/gas / government excluded).*

## Section 7 — Transaction / Payment Pattern Library (deterministic)

Bank-statement lines and ledger postings, with a deterministic classification. Azerbaijani-language terms are shown alongside.

### 7.1 Salary outflows (net wages to employees)

**7.1 Salary outflows patterns**

| Pattern | Classification | Note |
| --- | --- | --- |
| EMEK HAQQI, MAAS, SALARY | Net salary disbursement | Excludes PIT + employee SSPF/UIC/medical already withheld |
| AVANS | Salary advance | Recover against month-end net pay |
| MUKAFAT, BONUS, PREMIYA | Bonus (taxable employment income) | Add to PIT/SSPF base for the month |

### 7.2 Statutory remittances (employer debits)

**7.2 Statutory remittances patterns**

| Pattern | Classification | Note |
| --- | --- | --- |
| VERGI XIDMETI, STATE TAX SERVICE, GELIR VERGISI | PIT remittance to State Tax Service | Same-day as wage payment (Tax Code) |
| DSMF, SSPF, SOSIAL SIGORTA | SSPF social insurance contribution | Employee + employer split |
| ISSIZLIK SIGORTASI, UNEMPLOYMENT | UIC remittance | 0.5% + 0.5% |
| TIBBI SIGORTA, MEDICAL INSURANCE, ICBARI TIBBI | Mandatory medical insurance | Per §5.2 / §5.3 by year |

### 7.3 Excluded / out-of-scope lines

**7.3 Excluded/out-of-scope patterns**

| Pattern | Classification | Note |
| --- | --- | --- |
| DAXILI, INTERNAL, OWN TRANSFER | Internal transfer | Exclude |
| DIVIDEND | Dividend (5% WHT context) | Not payroll — exclude |
| FAIZ, INTEREST / KREDIT, LOAN | Finance | Exclude |
| NAGD, ATM, CASH | Cash withdrawal | Default exclude; ask if it funds wages |

## Section 8 — Worked Examples

> All figures in AZN. Each example recomputed end-to-end. Bank-statement lines use the semicolon-delimited DD.MM.YYYY format common to Kapital Bank / PASHA Bank exports.

### Example 1 — Non-oil private, 2025, gross AZN 1,000 (holiday, below all thresholds)

**Input line:** `31.07.2025 ; EMEK HAQQI — Rashad M. ; DEBIT ; July salary ; gross 1,000.00 ; AZN`

- PIT: 0% (≤ 8,000, holiday) = **0.00**
- SSPF employee: 6 + 10% × (1,000 − 200) = **86.00**
- UIC employee: 0.5% × 1,000 = **5.00**
- Medical employee: 2% × 1,000 = **20.00**
- Employee deductions: 0 + 86 + 5 + 20 = **111.00**
- **Net pay: 1,000.00 − 111.00 = 889.00**
- Employer-side: SSPF 164.00 + UIC 5.00 + medical 20.00 = **189.00** (100% state-subsidised through 2025; mechanism [RESEARCH GAP])

### Example 2 — Non-oil private, 2025, gross AZN 10,000 (crosses PIT and medical thresholds)

**Input line:** `31.08.2025 ; MAAS — Leyla Q. ; DEBIT ; Aug salary ; gross 10,000.00 ; AZN`

- PIT: 14% × (10,000 − 8,000) = **280.00**
- SSPF employee: 6 + 10% × (10,000 − 200) = 6 + 980 = **986.00**
- UIC employee: 0.5% × 10,000 = **50.00**
- Medical employee: 2% × 8,000 + 0.5% × (10,000 − 8,000) = 160 + 10 = **170.00**
- Employee deductions: 280 + 986 + 50 + 170 = **1,486.00**
- **Net pay: 10,000.00 − 1,486.00 = 8,514.00**
- Employer-side: SSPF (44 + 15% × 9,800 = 44 + 1,470 = 1,514.00) + UIC 50.00 + medical 170.00 = **1,734.00**

### Example 3 — Oil/gas sector, 2025, gross AZN 5,000 (standard rates)

**Input line:** `31.09.2025 ; SALARY — Kamran A. (offshore) ; DEBIT ; Sep salary ; gross 5,000.00 ; AZN`

- PIT: 350 + 25% × (5,000 − 2,500) = 350 + 625 = **975.00**
- SSPF employee: 3% × 5,000 = **150.00**
- UIC employee: 0.5% × 5,000 = **25.00**
- Medical employee: 2% × 5,000 = **100.00**
- Employee deductions: 975 + 150 + 25 + 100 = **1,250.00**
- **Net pay: 5,000.00 − 1,250.00 = 3,750.00**
- Employer-side: SSPF 22% × 5,000 = 1,100.00 + UIC 25.00 + medical 100.00 = **1,225.00** (no subsidy — oil/gas excluded)

### Example 4 — Government sector, 2025, gross AZN 2,500 (band boundary)

**Input line:** `31.10.2025 ; EMEK HAQQI — public employee ; DEBIT ; Oct salary ; gross 2,500.00 ; AZN`

- PIT: 14% × 2,500 = **350.00** (exactly at the boundary; the second band has not yet begun)
- SSPF employee: 3% × 2,500 = **75.00**
- UIC employee: 0.5% × 2,500 = **12.50**
- Medical employee: 2% × 2,500 = **50.00**
- Employee deductions: 350 + 75 + 12.50 + 50 = **487.50**
- **Net pay: 2,500.00 − 487.50 = 2,012.50**
- Employer-side: SSPF 22% × 2,500 = 550.00 + UIC 12.50 + medical 50.00 = **612.50**

### Example 5 — Non-oil private, **2026**, gross AZN 3,000 (new progressive PIT + lowered medical threshold)

**Input line:** `31.01.2026 ; MAAS — Nigar S. ; DEBIT ; Jan salary ; gross 3,000.00 ; AZN`

- PIT: 75 + 10% × (3,000 − 2,500) = 75 + 50 = **125.00** (AZN 200 low-income relief NOT applied — [RESEARCH GAP])
- SSPF employee (≤ 8,000 split continues): 6 + 10% × (3,000 − 200) = 6 + 280 = **286.00**
- UIC employee: 0.5% × 3,000 = **15.00**
- Medical employee (2026 threshold 2,500): 2% × 2,500 + 0.5% × (3,000 − 2,500) = 50 + 2.50 = **52.50**
- Employee deductions: 125 + 286 + 15 + 52.50 = **478.50**
- **Net pay: 3,000.00 − 478.50 = 2,521.50**
- Employer-side: SSPF (44 + 15% × 2,800 = 44 + 420 = 464.00) + UIC 15.00 + medical 52.50 = **531.50** (state subsidy 80% from 2026; mechanism [RESEARCH GAP])

### Example 6 — Minimum wage employee, 2025, gross AZN 400 (non-oil private)

**Input line:** `31.06.2025 ; EMEK HAQQI — minimum wage ; DEBIT ; Jun salary ; gross 400.00 ; AZN`

- PIT: 0% (holiday) = **0.00**
- SSPF employee: 6 + 10% × (400 − 200) = 6 + 20 = **26.00**
- UIC employee: 0.5% × 400 = **2.00**
- Medical employee: 2% × 400 = **8.00**
- Employee deductions: 0 + 26 + 2 + 8 = **36.00**
- **Net pay: 400.00 − 36.00 = 364.00**

## Section 9 — Tier 1 Rules (deterministic — apply without asking)

- **PIT withholding and remittance timing** — Withhold PIT at source and remit it on the same day wages are paid.  _(Tax Code; PwC — Tax administration)_
- **2025 non-oil/gas private sector PIT** — 0% PIT up to AZN 8,000/month; 14% on the excess — the final year of the 2019–2025 holiday  _(PwC — Significant developments)_
- **Oil/gas and government sectors PIT** — 14% up to AZN 2,500/month, then AZN 350 + 25% on the excess  _(PwC — Taxes on personal income)_
- **From 1 Jan 2026 (private) progressive PIT** — progressive 3% up to 2,500; AZN 75 + 10% on 2,501–8,000; AZN 625 + 14% above 8,000 (lowest band rises to 5% in 2027, 7% from 2028)  _(PwC; Mercans; Caspian)_
- **SSPF, non-oil private** — employee 3% on first AZN 200 + AZN 6 + 10% above; employer 2% on first AZN 200 + AZN 44 + 15% above; no ceiling  _(PwC — Other taxes)_
- **SSPF, oil/gas and government** — employee 3%, employer 22% flat  _(PwC — Other taxes)_
- **UIC** — 0.5% employee + 0.5% employer, all sectors  _(PwC; Mercans)_
- **Medical (2021–2025)** — 2% each on first AZN 8,000; 0.5% each (AZN 160 + 0.5%) above  _(PwC — Other taxes)_
- **Medical (from 2026)** — threshold drops to AZN 2,500; 2% each up to 2,500, 0.5% each above  _(Mercans; Caspian)_
- **High earners from 2026 (private, > AZN 8,000)** — combined SSPF on the excess falls to 21% (employee 10%, employer 11%)  _(Mercans)_
- **State subsidy schedule** — State subsidy covers 100% of private SSPF through 31 Dec 2025; 80% (2026–2028), 60% (2029–2030), 40% (2031–2032); excludes oil/gas  _(Law "On Social Insurance"; APA.az)_
- **Minimum monthly wage** — AZN 400 from 1 Jan 2025  _(Presidential Order; APA.az / AZERTAC)_
- **Unified monthly payroll declaration filing** — File the unified monthly payroll declaration (PIT + SSPF + UIC + medical) via e-taxes.gov.az by the 20th of the following month  _(taxes.gov.az tax calendar)_

### 10.1 Sector classification

Default: non-oil private. Question: "Is the employer in the oil/gas sector or government/state sector?" — changes PIT and SSPF materially.

### 10.2 Tax-year straddle (Dec 2025 / Jan 2026)

Default: apply the rules of the month in which the income is paid. Question: "Which month's payroll run is this?" — the holiday ends 31 Dec 2025.

### 10.3 Subsidy mechanism

Default: present gross contributions and note the subsidy. Question: "Does the SSPF reduce the remitted amount or reimburse later?" — [RESEARCH GAP].

### 10.4 2026 AZN 200 low-income relief

Default: do not apply. Question: "Has the AZN 200/month PIT relief (income ≤ 2,500) been confirmed against the Tax Code?" — [RESEARCH GAP].

### 10.5 Variable / bonus pay

Default: add to the month's PIT and contribution base. Question: "Is the bonus part of gross emoluments?"

### 10.6 Benefits in kind

Default: treat as taxable employment income unless an exemption is confirmed. Question: "Any non-cash benefits?" — [RESEARCH GAP — confirm BIK valuation rules].

### 10.7 Mid-month joiner/leaver

Default: pro-rate gross; apply full monthly thresholds (no statutory pro-ration confirmed). Question: "Start/leave date?" — [RESEARCH GAP — confirm threshold pro-ration].

## Section 11 — Excel Working Paper Template

Per `payroll-workflow-base` Section 3, with Azerbaijan-specific columns. One row per employee per month.

**Excel Working Paper Template columns**

| Column | Content |
| --- | --- |
| A | Employee name |
| B | VOEN (TIN) |
| C | Sector (non-oil private / oil-gas / government) |
| D | Tax year + month |
| E | Gross monthly salary (AZN) |
| F | PIT base |
| G | PIT withheld (per §3 by sector/year) |
| H | SSPF employee (per §4) |
| I | SSPF employer (per §4) |
| J | UIC employee (0.5%) |
| K | UIC employer (0.5%) |
| L | Medical employee (per §5) |
| M | Medical employer (per §5) |
| N | Total employee deductions (G + H + J + L) |
| O | Net pay (E − N) |
| P | Total employer contributions (I + K + M) |
| Q | State subsidy applied? (Y/N + %) |
| R | Default flags / [RESEARCH GAP] notes |

- **Control totals** — sum of column N must equal sum of (G + H + J + L) across the cohort; sum of O must equal sum of (E − N); these feed the unified monthly declaration.

## Section 12 — Azerbaijani Bank Statement / Terminology Reading Guide

CSV conventions. Kapital Bank and PASHA Bank exports use semicolon delimiters and DD.MM.YYYY dates. Amounts in AZN.

**Azerbaijani payroll terms**

| Term | Meaning |
| --- | --- |
| Emek haqqi / Maas | Salary / wages |
| Avans | Salary advance |
| Mukafat / Premiya | Bonus |
| Gelir vergisi | Income tax (PIT) |
| Sosial sigorta / DSMF | Social insurance / SSPF |
| Issizlik sigortasi | Unemployment insurance (UIC) |
| Icbari tibbi sigorta | Mandatory medical insurance |
| VOEN | Taxpayer identification number (TIN) |
| Daxili | Internal transfer |
| Faiz / Kredit | Interest / loan |
| Nagd | Cash |

Internal transfers between the client's own Kapital / PASHA / IBA accounts: always exclude. Foreign currency: convert to AZN at the Central Bank of Azerbaijan (cbar.az) rate. IBAN prefix AZ = Azerbaijan.

### 13.1 Sector

Fallback: "Non-oil private, oil/gas, or government employer?" (Default: non-oil private.)

### 13.2 Tax year

Inference: statement/pay-run dates. Fallback: "Which tax year — 2025 or 2026?"

### 13.3 VOEN

Fallback: "What is the employee/employer VOEN?"

### 13.4 Gross salary

Fallback: "Confirm each employee's gross monthly salary in AZN."

### 13.5 Subsidy eligibility

Fallback: "Is the employer eligible for the private-sector SSPF subsidy (non-oil)?"

### 13.6 Joiners/leavers

Fallback: "Any mid-month start or leave dates?"

### 13.7 Bonuses / BIK

Fallback: "Any bonuses or benefits in kind this month?"

### Monthly

**Monthly filing obligations**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Unified monthly payroll declaration (PIT + SSPF + UIC + medical) | Report gross wages, withheld PIT, SSPF, UIC and medical contributions per employee; filed electronically via e-taxes.gov.az | By the **20th** of the month following the reporting month (taxes.gov.az tax calendar) |
| PIT remittance to the State Tax Service | Withheld PIT must be remitted | **Same day** income is paid (Tax Code; PwC — Tax administration) |

### Annual

**Annual filing obligations**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Annual personal income tax return (individuals) | For residents with income not taxed at source or foreign-source income, and non-residents with Azerbaijani-source income not withheld | **31 March** of the following year (3-month extension available if tax already paid) (PwC — Tax administration) |

### 15.1 Context figures (for cross-reference only — not payroll computations)

**Context figures**

| Item | Value | Source |
| --- | --- | --- |
| Corporate profit tax | Flat 20% | PwC — Taxes on corporate income |
| Dividend withholding | 5% at source (from 1 Jan 2024) | PwC — Withholding taxes |
| Minimum monthly wage (2025) | AZN 400 | APA.az / AZERTAC |

### 15.2 Penalties

**Penalties**

| Type | Amount | Source |
| --- | --- | --- |
| Late tax payment | 0.1% per day on the unpaid tax | PwC / Grant Thornton AZ guides; Tax Code — **[RESEARCH GAP — verify article reference]** |
| Failure to submit a return / declaration | AZN 40 financial sanction per return | Azerbaijan Tax Code; Caspian — **[RESEARCH GAP — verify article reference]** |

### 15.3 Sources

1. PwC Worldwide Tax Summaries — Azerbaijan: Taxes on personal income; Other taxes; Significant developments; Tax administration; Corporate / Withholding taxes — https://taxsummaries.pwc.com/azerbaijan
2. State Tax Service under the Ministry of Economy — https://www.taxes.gov.az/en (tax calendar: /en/page/vergi-teqvimi)
3. Mercans — "Azerbaijan – Changes in Tax rate and Social Security Rates – 1st January 2026"
4. Caspian Legal Center — "Payroll Taxes in Azerbaijan (2026)" — https://www.caspianlegalcenter.az
5. APA.az — non-oil social insurance adjustment & subsidy schedule; AZN 400 minimum wage (official news)
6. EY — "Doing Business in Azerbaijan 2025"
7. Central Bank of Azerbaijan (FX) — https://www.cbar.az

### 15.4 Test Suite (each figure recomputed; PASS = matches the stated result)

1. **Non-oil private, 2025, AZN 1,000** → PIT 0; employee deductions 111.00; **net 889.00**. (§Ex.1)
2. **Non-oil private, 2025, AZN 10,000** → PIT 280.00; employee deductions 1,486.00; **net 8,514.00**. (§Ex.2)
3. **Oil/gas, 2025, AZN 5,000** → PIT 975.00; employee deductions 1,250.00; **net 3,750.00**. (§Ex.3)
4. **Government, 2025, AZN 2,500** → PIT 350.00 (boundary); employee deductions 487.50; **net 2,012.50**. (§Ex.4)
5. **Non-oil private, 2026, AZN 3,000** → PIT 125.00; medical 52.50; employee deductions 478.50; **net 2,521.50**. (§Ex.5)
6. **Minimum wage, 2025, AZN 400** → PIT 0; SSPF employee 26.00; employee deductions 36.00; **net 364.00**. (§Ex.6)
7. **Cumulative-PIT check (oil/gas):** at AZN 2,500, both formulas give 350.00 → PASS.
8. **Cumulative-PIT check (2026 private):** at 2,500 → 75.00; at 8,000 → 625.00 → PASS.
9. **SSPF base check:** employee base 6 = 3% × 200 → PASS; employer base 44 ≠ 2% × 200 → flagged [RESEARCH GAP].
10. **Medical base check (2025):** 160 = 2% × 8,000 → PASS.

### 15.5 Change log

- **v0.1 (2026):** Initial Tier-2 research-verified draft. Branches on tax year (2025 holiday vs 2026 progressive) and sector (non-oil private / oil-gas / government). Pending Azerbaijani accountant sign-off.

## PROHIBITIONS

- **Prohibited actions** — - NEVER apply the 2026 progressive PIT brackets to 2025 wages — the holiday was in force for all of 2025 (expired 31 Dec 2025). - NEVER apply the 2025 holiday (0% to AZN 8,000) to oil/gas or government employees — they use 14%/25% standard rates. - NEVER use the non-oil private SSPF split (3%/2% with AZN 6/44 bases) for oil/gas or government employees — they use 3% employee / 22% employer flat. - NEVER silently apply the AZN 200 (2026) low-income PIT relief — it is a [RESEARCH GAP] until confirmed against the Tax Code. - NEVER assume the state subsidy reduces the remitted amount — the mechanism is unconfirmed; present gross contributions and flag it. - NEVER delay PIT remittance — it is due the same day wages are paid. - NEVER omit any of the four components (PIT, SSPF, UIC, medical) from the unified monthly declaration. - NEVER miss the 20th-of-the-following-month declaration deadline — penalties apply. - NEVER invent figures — every rate/threshold must carry an inline citation or a [RESEARCH GAP — reviewer to confirm] marker. - NEVER present payroll computations as definitive — always label them estimated and direct the user to a licensed Azerbaijani accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Azerbaijan) before implementation.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Section 11 — Excel Working Paper Template

- **A** — Employee name
- **B** — VOEN (TIN)
- **C** — Sector (non-oil private / oil-gas / government)
- **D** — Tax year + month
- **E** — Gross monthly salary (AZN)
- **F** — PIT base
- **G** — PIT withheld (per §3 by sector/year)
- **H** — SSPF employee (per §4)
- **I** — SSPF employer (per §4)
- **J** — UIC employee (0.5%)
- **K** — UIC employer (0.5%)
- **L** — Medical employee (per §5)
- **M** — Medical employer (per §5)
- **N** — Total employee deductions (G + H + J + L)
- **O** — Net pay (E − N)
- **P** — Total employer contributions (I + K + M)
- **Q** — State subsidy applied? (Y/N + %)
- **R** — Default flags / [RESEARCH GAP] notes

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
