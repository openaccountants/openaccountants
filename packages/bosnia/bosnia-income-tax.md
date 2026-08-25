---
name: bosnia-income-tax
description: "Use this skill whenever asked about Bosnia and Herzegovina personal income tax (porez na dohodak) for employees or self-employed individuals. Trigger on phrases like \"how much tax do I pay in Bosnia\", \"FBiH income tax\", \"Republika Srpska income tax\", \"Brcko District tax\", \"porez na dohodak\", \"doprinosi\", \"social contributions Bosnia\", \"net pay BAM\", \"personal allowance\", \"lichni odbitak\", \"godisnja poreska prijava\", \"minimum wage Bosnia\", \"VAT registration UINO\", \"PDV\", or any question about computing or filing personal income tax and payroll contributions for a B&H worker or sole trader. CRITICAL: Bosnia has NO single national income tax — there are three separate entity/district systems (FBiH, RS, Brcko District). ALWAYS determine the taxpayer's entity FIRST. Also trigger when reviewing a monthly payroll specification (MIP-1023 / Obrazac 1002) or an annual return (GPD-1051). ALWAYS read this skill before touching any B&H income tax work."
version: 0.1
jurisdiction: BA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bosnia and Herzegovina Income Tax -- Personal/Self-Employed

## Bosnia and Herzegovina Income Tax -- Personal/Self-Employed Skill v0.1

> **Tier 2 (research-verified).** Confidence: medium. Figures are sourced from PwC Worldwide Tax Summaries (2025), the FBiH Official Gazette / Orbitax / Unija legislative summaries, WageIndicator, and the Indirect Taxation Authority (UINO). Several figures carry explicit `[RESEARCH GAP — reviewer to confirm]` markers and MUST be confirmed against the entity-level statutes before filing.

## Section 0 -- READ THIS FIRST: There Is No National Income Tax

- **No national income tax** — Bosnia and Herzegovina does NOT levy a single national personal income tax. Direct taxes (personal income tax and social contributions) are administered at the entity/district level by three separate systems with different rates, allowances, and contribution structures.  _(PwC Worldwide Tax Summaries, Bosnia and Herzegovina – Individual – Taxes on personal income (2025), https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/taxes-on-personal-income)_

**Entity/district PIT systems table**  _(PwC Worldwide Tax Summaries, Bosnia and Herzegovina – Individual – Taxes on personal income (2025))_

| System | Authority | PIT rate | Website |
| --- | --- | --- | --- |
| **Federation of B&H (FBiH)** | Porezna uprava FBiH (Tax Administration of the Federation) | Flat **10%** | www.pufbih.ba |
| **Republika Srpska (RS)** | Poreska uprava RS (Tax Administration of RS) | Flat **8%** | www.poreskaupravars.org |
| **Brčko District (BD)** | Brčko District Tax Administration | Flat **10%** | — |

- **VAT is only state-level tax** — Indirect tax (VAT / PDV) is the only state-level direct-revenue tax, administered by the Indirect Taxation Authority (Uprava za indirektno oporezivanje / UINO) at 17% (www.uino.gov.ba).  _(PwC Worldwide Tax Summaries (2025))_
- **Determine entity before computing** — You MUST determine the taxpayer's entity before computing anything. If the entity is unknown, see the Conservative Defaults (Section 1) — default to FBiH and flag for the reviewer.  _(PwC Worldwide Tax Summaries (2025))_

## Section 1 -- Quick Reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Bosnia and Herzegovina |
| Tax | Personal Income Tax (porez na dohodak) + mandatory social contributions (doprinosi) |
| Currency | BAM (convertible mark; pegged to EUR at ~1.95583 BAM = 1 EUR) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation (FBiH) | Zakon o porezu na dohodak FBiH; Zakon o doprinosima FBiH (amended eff. 1 July 2025) |
| Primary legislation (RS) | Zakon o porezu na dohodak RS; Zakon o doprinosima RS |
| Primary legislation (BD) | Law on Personal Income Tax of Brčko District |
| Indirect tax | State Law on VAT, administered by UINO; 17% single rate |
| Tax authorities | FBiH: Porezna uprava FBiH · RS: Poreska uprava RS · BD: Brčko District Tax Admin · VAT: UINO |
| Annual PIT return deadline | FBiH & RS: **31 March** of following year; BD: **28 February** (only where withholding insufficient) |
| Validated by | Pending — requires sign-off by a B&H tax adviser / certified accountant |
| Validation date | Pending |
| Skill version | 0.1 |

### Personal Income Tax Rates (2025)

**PIT rates table**  _(PwC, Individual – Taxes on personal income (2025))_

| Jurisdiction | Type | Rate | Base |
| --- | --- | --- | --- |
| Federation of B&H (FBiH) | Flat | **10%** | Taxable personal income (worldwide for residents; FBiH-source for non-residents) |
| Republika Srpska (RS) | Flat | **8%** | Taxable personal income |
| Republika Srpska — small entrepreneurs (paušalci) | Flat lump-sum on revenue | **2%** | Total annual revenue, if below the qualifying threshold |
| Brčko District (BD) | Flat | **10%** | Taxable personal income |

- **No progressive brackets** — All three systems use flat rates (no progressive brackets — there is no "cumulative tax" table to compute).  _(PwC, Individual – Taxes on personal income (2025))_
- **RS paušal threshold research gap** — `[RESEARCH GAP — reviewer to confirm]` the qualifying annual-revenue threshold for the RS 2% paušal regime, and whether it is elective or mandatory — not confirmed from an authoritative source.  _(PwC, Individual – Taxes on personal income (2025))_

### Personal Allowances (2025)

**Personal allowances table**  _(PwC, Individual – Deductions (2025), https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/deductions)_

| Jurisdiction | Personal allowance | Dependent additions |
| --- | --- | --- |
| FBiH | **300 BAM/month** (3,600 BAM/year) | Spouse +150/mo; 1st child +150/mo; 2nd child +270/mo; 3rd+ child +90/mo each; dependent parent (income ≤300 BAM/mo) +90/mo |
| RS | **6,000 BAM/year** (500 BAM/month) | Dependent family members +900 BAM/year each; mortgage interest fully deductible; life insurance and voluntary pension contributions up to 1,200 BAM each |
| BD | **6,000 BAM/year** (500 BAM/month) | **`[RESEARCH GAP — reviewer to confirm]`** BD dependent allowances not separately captured |

### Conservative Defaults

**Conservative defaults table**  _(PwC (2025); Unija, Amendments to the Law on Contributions in the FBiH (eff. 1 July 2025), https://unija.com/en/amendments-to-the-law-on-contibutions-in-the-fbih/)_

| Ambiguity | Default |
| --- | --- |
| Unknown entity (FBiH / RS / BD) | Default to **FBiH** (larger by population); apply 10% PIT + FBiH allowances/contributions. FBiH 10% > RS 8%, so this avoids understating tax. Flag for reviewer. |
| FBiH employer cost, date unknown in 2025 | Use period-appropriate rate: ~10.5% social-fund total **before** 1 July 2025; 5.0% **from** 1 July 2025 |
| RS individual, paušal status unconfirmed | Default to **8% standard** rate, NOT the 2% lump-sum regime |
| Unknown dependents | Apply personal allowance only (no dependent additions) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT registration | Assume not registered until turnover confirmed ≥ 100,000 BAM |

## Section 1A -- Social Contribution Tables (doprinosi)

> **Arithmetic note:** every "total" row below is the exact sum of its component rows. Verify before relying on it.

### FBiH Contributions (% of gross salary)

**FBiH contributions table**  _(PwC, Individual – Other taxes (2025), https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/other-taxes; employer reduction per Unija/Orbitax (Official Gazette FBiH, 7 May 2025; effective 1 July 2025).)_

| Contribution | Employee | Employer (from 1 July 2025) |
| --- | --- | --- |
| Pension and disability insurance | 17.0% | 2.5% (reduced from 6.0%) |
| Health insurance | 12.5% | 2.0% (reduced from 4.0%) |
| Unemployment insurance | 1.5% | 0.5% (unchanged) |
| **TOTAL on gross** | **31.0%** | **5.0%** |

**FBiH employer levies on net salary table**  _(PwC, Individual – Other taxes (2025))_

| Employer levy (base = net salary) | Rate |
| --- | --- |
| Protection from natural and other disasters | 0.5% |
| Water protection charge | 0.5% |

- **Component checks** — Component check (employee): 17.0 + 12.5 + 1.5 = **31.0%** ✓ Component check (employer social funds): 2.5 + 2.0 + 0.5 = **5.0%** ✓  _(PwC, Individual – Other taxes (2025))_
- **Pre-1 July 2025 employer rates** — Pre-1 July 2025 employer rates (for H1 2025 computations): pension/disability 6.0%, health 4.0%, unemployment 0.5% = ~10.5% (social-fund total cited variously as 10.0% on the three funds, or ~10.5% including the two 0.5% net-salary levies). `[RESEARCH GAP — reviewer to confirm]` the exact pre-July employer total against the entity Law on Contributions text.  _(PwC (2025))_

### RS Contributions (% of gross salary) — employee bears ALL

**RS contributions table**  _(PwC, Individual – Other taxes (2025))_

| Contribution | Employee | Employer |
| --- | --- | --- |
| Pension and disability insurance | 18.5% | 0% |
| Health insurance | 12.0% | 0% |
| Unemployment insurance | 0.6% | 0% |
| Child protection | 1.7% | 0% |
| **TOTAL on gross** | **32.8%** | **0%** |

- **Component check RS** — Component check: 18.5 + 12.0 + 0.6 + 1.7 = **32.8%** ✓ RS has no employer social contributions; the employee carries the full 32.8%.  _(PwC, Individual – Other taxes (2025))_

### Brčko District Contributions

**BD contributions table**  _(PwC, Individual – Other taxes (2025))_

| Contribution | Detail |
| --- | --- |
| Pension | Employee may elect to contribute to **either** the RS or FBiH pension fund; rate depends on the chosen fund |
| Health insurance | **12.0%** of gross |

- **BD employer/employee split research gap** — `[RESEARCH GAP — reviewer to confirm]` the exact BD employer/employee split, which follows the chosen entity fund.  _(PwC, Individual – Other taxes (2025))_

### Contribution Base Notes (self-employed / entrepreneurs)

- **FBiH self-employed contribution base coefficients** — FBiH self-employed/entrepreneur contribution bases are set by coefficient multiples of the published average salary (e.g. ~1.1 liberal professions, 0.65 crafts, 0.55 without books, 0.29 sole traders with books). The monthly base BAM amounts are published annually by the Federal Minister of Finance by 31 December. `[RESEARCH GAP — reviewer to confirm]` the exact 2025 BAM base figures from the official Službene novine — not obtained. No explicit monthly contribution ceiling was confirmed for either entity for 2025; the minimum base is effectively tied to the minimum wage.  _(PwC (2025) + caveats)_

### Required Inputs

- **Minimum viable** — Minimum viable — the taxpayer's entity (FBiH / RS / BD), gross monthly salary or annual income, and number/type of dependents.
- **Recommended** — Recommended — full-year payslips or bank statement, monthly payroll specifications (MIP-1023 / Obrazac 1002), confirmation of resident vs non-resident status, prior-year annual return, and (for self-employed) the contribution base/coefficient applied.
- **Ideal** — Ideal — complete income and expenditure records, asset register, deductible items (RS mortgage interest, life-insurance / voluntary-pension up to 1,200 BAM each), VAT registration status (UINO), and confirmation of period for any H1/H2 2025 employer-rate split.
- **Refusal if minimum missing** — Refusal if minimum is missing — SOFT WARN. No entity = hard stop (the rate, allowances, and contributions differ entirely between systems). Income without supporting documents = proceed with reviewer warning: "This computation was produced from limited data. The reviewer must verify the entity, contribution base, and allowable deductions."

### Refusal Catalogue

- **R-BA-1** — Entity unknown. "Bosnia and Herzegovina has three separate income-tax systems (FBiH, RS, Brčko District) with different rates (10% / 8% / 10%), allowances, and contributions. This skill cannot compute tax without the taxpayer's entity. Please confirm before proceeding."
- **R-BA-2** — RS small-entrepreneur (paušal) regime. "The RS 2% lump-sum regime is threshold-gated and the qualifying revenue limit is unconfirmed. Do not apply 2% without confirming eligibility. Default to 8% standard and escalate to a B&H adviser."
- **R-BA-3** — Non-resident / cross-border income. "Non-resident and dual-residence taxation, and inter-entity allocation, have different rules. Out of scope. Escalate to a B&H tax adviser."
- **R-BA-4** — Capital gains / property disposals. "Capital gains and property-transfer taxation require specialised entity-level analysis. Escalate to a B&H tax adviser."
- **R-BA-5** — Arrears / enforcement. "Client has outstanding tax/contribution arrears or is subject to enforcement. Default interest and entity-specific fines apply. Do not advise. Escalate immediately."
- **R-BA-6** — VAT / PDV return requested. "This skill covers personal income tax and payroll contributions only. B&H VAT is a separate state-level tax under UINO. Use a dedicated VAT skill."
- **R-BA-7** — Mid-2025 FBiH employer-rate period unknown. "FBiH employer contributions changed on 1 July 2025. For an employer-cost computation, confirm whether the period is before or after that date before applying a rate."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank-statement transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty name or description. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5. Bosnian/Serbian/Croatian terms (Latin and Cyrillic where relevant) are given alongside English.

### 3.1 Income Patterns (Credits)

**Income patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PLATA, PLAĆA, ПЛАТА, SALARY, NETO PLATA | Employment income | Net salary credit; gross-up to recompute PIT + contributions |
| HONORAR, NAKNADA, FEES, PROFESSIONAL FEES | Other income / self-employment | Service fee — check entity treatment |
| UPLATA, DOZNAKA, TRANSFER IN, PAYMENT RECEIVED | Business income | If self-employed; match to invoices |
| STRIPE PAYOUT, PAYPAL, WISE, REVOLUT PAYOUT | Business income | Platform payout — match to underlying invoices |
| KIRIJA, ZAKUP, RENT RECEIVED | Rental income | Separate income category |
| KAMATA, КАМАТА, INTEREST | Investment income | Interest income |
| DIVIDENDA, ДИВИДЕНДА, DIVIDEND | Investment income | Dividend income |
| POVRAT POREZA, TAX REFUND | EXCLUDE | Prior-year tax refund — not income |
| POTICAJ, SUBVENCIJA, GRANT | Check nature | Capital grants EXCLUDE; revenue grants = income |

### 3.2 Expense Patterns (Debits) — potentially deductible (self-employed)

**Potentially deductible expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ZAKUP UREDA, NAJAM, OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| KNJIGOVODSTVO, RAČUNOVODSTVO, ACCOUNTANT | Accountancy fees | Deductible |  |
| ADVOKAT, PRAVNE USLUGE, LEGAL | Legal fees | Deductible | Must be business-related |
| MARKETING, GOOGLE ADS, META ADS, OGLAŠAVANJE | Marketing | Deductible |  |
| OBUKA, SEMINAR, KONFERENCIJA, TRAINING | Training/CPD | Deductible | Must relate to current business |
| BANKARSKA NAKNADA, BANK FEE, PROVIZIJA | Bank charges | Deductible | Business account only |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE, ANTHROPIC, OPENAI | Software subscription | Deductible | Recurring operating expense |
| DOMAIN, HOSTING, AWS, CLOUD | IT infrastructure | Deductible |  |

### 3.3 Expense Patterns (Debits) — utilities, may need apportionment

**Utilities expense patterns table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ELEKTROPRIVREDA, STRUJA, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| VODOVOD, VODA, WATER | Water | T2 if home office |  |
| BH TELECOM, M:TEL, HT ERONET, TELEKOM, INTERNET | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| MOBILNI, MOBILE | Phone | T2 | Business-use portion only |

### 3.4 Expense Patterns (Debits) — travel

**Travel expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AVIO, RYANAIR, WIZZ, FLIGHT | Flights | Deductible if business | Must be wholly business purpose |
| HOTEL, BOOKING.COM, SMJEŠTAJ | Accommodation | Deductible if business |  |
| TAXI, BOLT, PREVOZ | Local transport | Deductible if business |  |
| GORIVO, BENZIN, FUEL, PETROL | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARKING | Parking | T2 — business % only |  |

### 3.5 Expense Patterns (Debits) — NOT deductible

**Not deductible expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORAN, RUČAK, REPREZENTACIJA, ENTERTAINMENT | Entertainment | NOT deductible | Personal/representation |
| TRGOVINA, MARKET, KONZUM, BINGO, GROCERIES | Personal | NOT deductible | Private living costs |
| KAZNA, PENAL, FINE | Fines/penalties | NOT deductible | Public policy |
| POREZ NA DOHODAK, INCOME TAX PAYMENT | Tax payment | NOT deductible | Income tax cannot reduce income |
| ISPLATA VLASNIKU, DRAWINGS | Drawings | NOT deductible | Not an expense |

### 3.6 Capital Items

**Capital items table**

| Pattern | Category | Notes |
| --- | --- | --- |
| LAPTOP, RAČUNAR, COMPUTER, MACBOOK | Computer hardware | Capitalise per entity depreciation rules — **`[RESEARCH GAP — reviewer to confirm]`** B&H individual capital-allowance rates not captured |
| OPREMA, EQUIPMENT, NAMJEŠTAJ, FURNITURE | Equipment/furniture | Capitalise; reviewer confirms rate |
| VOZILO, AUTO, VEHICLE | Motor vehicle | Capitalise; business % only |

### 3.7 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNI TRANSFER, OWN ACCOUNT, IZMEĐU RAČUNA | EXCLUDE | Own-account transfer |
| KREDIT, OTPLATA KREDITA, LOAN REPAYMENT | EXCLUDE | Loan principal movement |
| DOPRINOSI, CONTRIBUTIONS, PIO, ZDRAVSTVO | Contribution payment | Withheld payroll item — not a Box 2 business expense |
| PDV, VAT PAYMENT | EXCLUDE | VAT liability payment to UINO, not an expense |

### 3.8 B&H Banks — Statement Format Reference

**Bank format reference table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| UniCredit Bank | UPLATA, ISPLATA, NAKNADA, TRANSFER | PDF/CSV; date format DD.MM.YYYY |
| Raiffeisen Bank BiH | TRANSFER, DD, NAKNADA | PDF/CSV; counterparty in description |
| Intesa Sanpaolo Banka | PLAĆANJE, UPLATA, PROVIZIJA | PDF |
| NLB Banka | TRANSFER, TROŠAK | PDF/CSV |
| Nova banka (RS) | UPLATA, ISPLATA, КАМАТА | PDF; may use Cyrillic |
| Addiko Bank | PAYMENT, TRANSFER, FEE | CSV available |

## Section 4 -- Worked Examples

> All figures recomputed end-to-end below. BAM throughout.

### Example 1 — FBiH minimum-wage employee (sanity check)

**Input:** Single FBiH employee, gross 1,562 BAM/month (2025 minimum wage gross), no dependents.

**Reasoning:**
- Employee contributions: 31.0% × 1,562 = **484.22**
- Income after contributions: 1,562 − 484.22 = **1,077.78**
- Personal allowance: 300
- PIT base: 1,077.78 − 300 = **777.78**
- PIT @ 10%: 777.78 × 0.10 = **77.78**
- **Net pay: 1,077.78 − 77.78 = 1,000.00**

**Cross-check:** This reconciles to the published FBiH 2025 minimum wage of **1,000 BAM net** (WageIndicator). ✓
Source: WageIndicator, Minimum Wage FBiH from 01 Jan 2025; PwC (2025).

### Example 2 — FBiH single employee, gross 3,000 BAM

**Input:** Single FBiH employee, gross 3,000 BAM/month, no dependents. Payment date in H2 2025 (employer rates from 1 July 2025).

**Reasoning (employee side):**
- Employee contributions: 31.0% × 3,000 = **930.00**
- After contributions: 3,000 − 930 = **2,070.00**
- Personal allowance: 300 → PIT base: 2,070 − 300 = **1,770.00**
- PIT @ 10%: **177.00**
- **Net pay: 2,070 − 177 = 1,893.00**

**Employer cost (from 1 July 2025):**
- Social funds 5.0% × 3,000 = **150.00**
- Natural-disaster levy 0.5% × net 1,893 = **9.47**
- Water protection 0.5% × net 1,893 = **9.47**
- **Total employer cost ≈ 3,000 + 150 + 9.47 + 9.47 = 3,168.94**

**`[RESEARCH GAP — reviewer to confirm]`** the exact base for the two 0.5% levies ("net salary" definition). Source: PwC (2025); Unija (eff. 1 July 2025).

### Example 3 — FBiH married employee, 2 children, gross 4,000 BAM

**Input:** Married FBiH employee, gross 4,000 BAM/month, spouse dependent, 2 children.

**Reasoning:**
- Employee contributions: 31.0% × 4,000 = **1,240.00**
- After contributions: 4,000 − 1,240 = **2,760.00**
- Allowances: personal 300 + spouse 150 + 1st child 150 + 2nd child 270 = **870.00**
- PIT base: 2,760 − 870 = **1,890.00**
- PIT @ 10%: **189.00**
- **Net pay: 2,760 − 189 = 2,571.00**

Source: PwC, Deductions (2025) for the dependent allowance schedule.

### Example 4 — RS single employee, gross 2,000 BAM

**Input:** Single RS employee, gross 2,000 BAM/month. RS has NO employer contributions.

**Reasoning:**
- Employee contributions: 32.8% × 2,000 = **656.00**
- After contributions: 2,000 − 656 = **1,344.00**
- Personal allowance: 6,000/year = 500/month → PIT base: 1,344 − 500 = **844.00**
- PIT @ 8%: 844 × 0.08 = **67.52**
- **Net pay: 1,344 − 67.52 = 1,276.48**
- **Employer cost: 2,000.00** (gross only — RS employer contributions = 0%)

Source: PwC, Other taxes and Deductions (2025).

### Example 5 — RS small entrepreneur (2% lump-sum)

**Input:** RS sole trader confirmed eligible for the paušal regime, total annual revenue 50,000 BAM.

**Reasoning:**
- Lump-sum PIT @ 2% × 50,000 = **1,000.00** for the year.

**WARNING:** Apply 2% ONLY if paušal eligibility is confirmed. **`[RESEARCH GAP — reviewer to confirm]`** the qualifying revenue threshold and whether the regime is elective. If unconfirmed, default to RS standard 8%. Source: PwC (2025).

### Example 6 — Entity unknown (conservative default)

**Input:** Gross 3,000 BAM/month, entity NOT stated.

**Reasoning:** Default to **FBiH** (10%, larger entity, higher of 10% vs RS 8% — avoids understating tax). Compute as Example 2: net pay **1,893.00**. Flag: "Entity assumed FBiH under conservative default — reviewer must confirm; RS would yield a different result (8% PIT, 32.8% employee contributions, no employer contributions)."

Source: PwC (2025) per Conservative Defaults (Section 1).

### 5.1 Determine the Entity First

- **Entity determination rule** — No computation is valid without the entity. FBiH = 10% PIT + 31.0% employee / 5.0% employer (H2 2025) contributions. RS = 8% PIT + 32.8% employee / 0% employer. BD = 10% PIT + 12% health + elective RS/FBiH pension.  _(PwC (2025))_

### 5.2 Residence and Source

- **Worldwide vs source income** — FBiH residents are taxed on worldwide income; non-residents on FBiH-source income. Confirm residence before applying worldwide treatment.  _(PwC, Taxes on personal income (2025))_

### 5.3 PIT Base = Income − Contributions − Allowances

- **PIT base formula** — The PIT base is gross income reduced by mandatory employee social contributions and the applicable personal/dependent allowances. Apply the flat entity rate to the resulting base. (See Worked Examples for the order of operations.)

### 5.4 Personal and Dependent Allowances

**Personal and dependent allowances table**  _(PwC, Deductions (2025))_

| Entity | Personal | Dependents |
| --- | --- | --- |
| FBiH | 300/mo | Spouse 150; 1st child 150; 2nd child 270; 3rd+ child 90 each; dependent parent (income ≤300/mo) 90 |
| RS | 6,000/yr | Family members 900/yr each; mortgage interest (full); life insurance + voluntary pension up to 1,200 each |
| BD | 6,000/yr | **`[RESEARCH GAP — reviewer to confirm]`** |

### 5.5 Withholding (PAYE-style)

- **Withholding rule** — Employers withhold PIT and employee contributions monthly and remit them with salary. FBiH: salary-tax specification due the same day as payment, no later than 1 day after. RS: monthly specification due by the 10th of the following month.  _(PwC, Tax administration (2025))_

### 5.6 FBiH Employer-Rate Change (1 July 2025)

- **FBiH employer rate change** — FBiH employer social contributions were cut effective 1 July 2025: pension/disability 6.0% → 2.5%, health 4.0% → 2.0%, unemployment 0.5% unchanged — taking the social-fund total from ~10.0% to 5.0%. The employee 31.0% is unchanged and net pay is unchanged. Always apply the period-appropriate rate.  _(Unija/Orbitax (Official Gazette FBiH, 7 May 2025))_

### 5.7 RS Has No Employer Contributions

- **RS no employer contributions** — In RS the employee bears the full 32.8%; there are no employer social contributions.  _(PwC, Other taxes (2025))_

### 5.8 Wholly-and-Exclusively (self-employed deductions)

- **Wholly and exclusively rule** — For self-employed/entrepreneur taxpayers, only expenses incurred wholly and exclusively for business are deductible; mixed-use items must be apportioned and documented. Entertainment/representation, personal living costs, fines, and the income tax itself are not deductible. (Apportionment items are Tier 2 — Section 6.)

### 5.9 VAT (PDV) Interaction

- **VAT interaction rule** — VAT is state-level (UINO) at 17%, single rate, no reduced rate. Registration threshold is 100,000 BAM annual taxable turnover (raised from 50,000 BAM on 2 Dec 2023); non-resident digital-service (ESS) suppliers register via a VAT representative at the same 100,000 BAM threshold. VAT collected on sales is not income; recoverable input VAT is not an expense.  _(UINO; vatcalc; Deloitte (2025))_

### 5.10 Annual Returns and Deadlines

**Annual returns and deadlines table**  _(PwC, Tax administration (2025))_

| Entity | Return | Deadline |
| --- | --- | --- |
| FBiH | Annual PIT return (GPD-1051 / godišnja prijava poreza na dohodak) | **31 March** of following year |
| RS | Annual income tax return (godišnja poreska prijava) | **31 March** of following year |
| BD | Annual PIT return (only where withholding insufficient) | **28 February** of following year |

- **Form codes research gap** — `[RESEARCH GAP — reviewer to confirm]` exact form codes against the current entity authority forms.  _(PwC, Tax administration (2025))_

### 5.11 Monthly Payroll Specifications

**Monthly payroll specifications table**  _(PwC, Tax administration (2025))_

| Entity | Form | Deadline |
| --- | --- | --- |
| FBiH | Monthly salary tax/contributions specification (Specifikacija MIP-1023) | Same day as salary payment, no later than 1 day after |
| RS | Monthly salary tax/contributions specification (Obrazac 1002) | By the 10th of the following month |

- **Form codes research gap** — Form codes drawn from common practice — `[RESEARCH GAP — reviewer to confirm]`.  _(PwC, Tax administration (2025))_

### 5.12 Corporate Context (incorporation comparison)

- **Corporate income tax rate** — Corporate income tax is 10% across FBiH, RS, and BD — relevant when a self-employed individual considers incorporation.  _(PwC, Corporate – Taxes on corporate income (2025))_

### 6.1 Home Office Deduction (self-employed)

- **Home office deduction** — Apportion rent, electricity, water, internet by dedicated-space percentage; dual-use space does not qualify. Conservative default: 0% until reviewer confirms the arrangement.

### 6.2 Motor Vehicle Business Use

- **Vehicle business use** — Only business-use % of fuel, insurance, maintenance, depreciation is deductible; requires a mileage log. Conservative default: 0% business use until log provided.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use** — Business-use portion only; reasonable documented estimate required. Conservative default: 0% until confirmed.

### 6.4 FBiH H1/H2 2025 Employer-Rate Split

- **FBiH H1/H2 split** — For an employer-cost computation spanning the 1 July 2025 change, split the year: ~10.0% social funds Jan–Jun, 5.0% Jul–Dec. `[RESEARCH GAP — reviewer to confirm]` the exact pre-July total.

### 6.5 RS Paušal (2%) Eligibility

- **RS paušal eligibility** — Confirm the small-entrepreneur revenue threshold and elective/mandatory status before applying 2%. `[RESEARCH GAP — reviewer to confirm]`.

### 6.6 Self-Employed Contribution Base (FBiH coefficients)

- **FBiH coefficient bases** — Bases are coefficient multiples of the published average salary (~1.1 liberal professions, 0.65 crafts, 0.55 without books, 0.29 sole traders with books); the 2025 BAM base amounts are published by the Federal Minister of Finance. `[RESEARCH GAP — reviewer to confirm]` the 2025 figures from Službene novine.

### 6.7 RS Deductible Items

- **RS deductible items** — Mortgage interest (full), life insurance and voluntary pension up to 1,200 BAM each, dependent family member 900/yr — confirm documentation.  _(PwC, Deductions (2025))_

### 6.8 Capital Allowances (individuals)

- **Capital allowances research gap** — B&H individual capital-allowance/depreciation rates were not captured. `[RESEARCH GAP — reviewer to confirm]` entity depreciation rules before capitalising assets.

## Section 7 -- Excel Working Paper Template

```
BOSNIA AND HERZEGOVINA INCOME TAX -- WORKING PAPER
Tax Year: 2025
Entity: FBiH / RS / Brčko District   (MUST be confirmed)
Client: ___________________________
Marital/dependent status: __________
Payment period (FBiH only): H1 (pre-1 Jul) / H2 (from 1 Jul)

A. GROSS INCOME
  A1. Gross monthly salary (BAM)                 ___________
  A2. Other income (rent, interest, dividends)   ___________
  A3. TOTAL gross                                ___________

B. EMPLOYEE SOCIAL CONTRIBUTIONS
  FBiH: 31.0% of gross  |  RS: 32.8% of gross
  B1. Contribution rate applied (%)              ___________
  B2. Employee contributions (A1 × rate)         ___________

C. INCOME AFTER CONTRIBUTIONS (A1 - B2)          ___________

D. ALLOWANCES
  D1. Personal allowance                         ___________
       (FBiH 300/mo · RS & BD 500/mo)
  D2. Dependent allowances                       ___________
  D3. TOTAL allowances                           ___________

E. PIT BASE (C - D3)                             ___________

F. PIT
  F1. Rate (FBiH 10% · RS 8% · BD 10% ·          ___________
       RS paušal 2% on revenue — if confirmed)
  F2. PIT (E × rate)                             ___________

G. NET PAY (C - F2)                              ___________

H. EMPLOYER COST (informational)
  H1. Employer social funds                      ___________
       (FBiH 5.0% from 1 Jul / ~10.0% before · RS 0%)
  H2. FBiH natural-disaster 0.5% of net          ___________
  H3. FBiH water protection 0.5% of net          ___________
  H4. TOTAL employer cost (A1 + H1 + H2 + H3)    ___________

REVIEWER FLAGS:
  [ ] Entity confirmed (FBiH / RS / BD)?
  [ ] Resident vs non-resident confirmed?
  [ ] Dependent allowances confirmed?
  [ ] FBiH employer period (H1/H2 2025) confirmed?
  [ ] RS paušal eligibility confirmed (if 2% used)?
  [ ] Self-employed contribution base/coefficient confirmed?
  [ ] T2 apportionment items flagged?
  [ ] VAT registration status (≥100,000 BAM) confirmed?
```

### B&H Bank Statement Formats

**Bank statement formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| UniCredit Bank | PDF, CSV | Datum, Opis, Duguje, Potražuje, Saldo | Date format DD.MM.YYYY |
| Raiffeisen Bank BiH | PDF, CSV | Datum, Opis, Iznos, Saldo | Counterparty in description |
| Intesa Sanpaolo Banka | PDF | Datum, Opis, Isplata, Uplata |  |
| NLB Banka | PDF, CSV | Datum, Opis, Iznos |  |
| Nova banka (RS) | PDF | Датум, Опис, Износ | May use Cyrillic |
| Addiko Bank | CSV | Date, Description, Amount, Balance | English available |

### Key B&H Banking / Tax Terms

**Key banking/tax terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| PLATA / PLAĆA / ПЛАТА | Salary | Employment income (gross-up for PIT + contributions) |
| UPLATA | Credit / inbound payment | Potential income |
| ISPLATA | Debit / outbound payment | Potential expense |
| DOPRINOSI / ДОПРИНОСИ | Social contributions | Withheld payroll item (PIO, zdravstvo, nezaposlenost) |
| PIO | Pension & disability insurance | Contribution |
| ZDRAVSTVO | Health insurance | Contribution |
| POREZ NA DOHODAK | Personal income tax | Tax withheld — not deductible |
| LIČNI ODBITAK | Personal allowance | Reduces PIT base |
| NAKNADA / PROVIZIJA | Fee / commission | Bank charge (deductible if business) |
| KAMATA / КАМАТА | Interest | Interest income or bank charge |
| KIRIJA / ZAKUP | Rent | Rental income or office-rent expense |
| PDV | VAT | UINO liability — exclude |

## Section 9 -- Onboarding Fallback

If the client provides records but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1) — including defaulting to FBiH if entity unknown.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- BOSNIA AND HERZEGOVINA INCOME TAX
1. Which entity/district? Federation of B&H (FBiH), Republika Srpska (RS), or Brčko District?
2. Employee or self-employed? If self-employed, which contribution base/coefficient applies?
3. Resident or non-resident of B&H?
4. Marital status and number of dependent children / dependent parent?
5. (RS) Are you registered as a small entrepreneur (paušalac)? What is annual revenue?
6. (FBiH employer cost) Is the period before or after 1 July 2025?
7. Gross monthly salary (BAM)?
8. Any other income (rental, interest, dividends)?
9. (RS) Mortgage interest, life insurance, or voluntary pension contributions paid?
10. VAT (PDV) registered with UINO? Annual taxable turnover ≥ 100,000 BAM?
```

### Key Figures and Their Sources

**Key figures and sources table**

| Item | Value | Source |
| --- | --- | --- |
| FBiH PIT rate | 10% flat | PwC, *Taxes on personal income* (2025) |
| RS PIT rate | 8% flat | PwC (2025) |
| RS paušal rate | 2% on revenue (threshold unconfirmed) | PwC (2025) — `[RESEARCH GAP]` threshold |
| BD PIT rate | 10% flat | PwC (2025) |
| FBiH personal allowance | 300 BAM/mo (3,600/yr) | PwC, *Deductions* (2025) |
| RS / BD personal allowance | 6,000 BAM/yr | PwC, *Deductions* (2025) |
| FBiH employee contributions | 31.0% (17.0 + 12.5 + 1.5) | PwC, *Other taxes* (2025) |
| FBiH employer contributions (from 1 Jul 2025) | 5.0% (2.5 + 2.0 + 0.5) + 0.5% disaster + 0.5% water on net | PwC (2025); Unija/Orbitax (Gazette 7 May 2025) |
| RS employee contributions | 32.8% (18.5 + 12.0 + 0.6 + 1.7) | PwC, *Other taxes* (2025) |
| RS employer contributions | 0% | PwC (2025) |
| BD health insurance | 12% of gross | PwC (2025) |
| FBiH minimum wage 2025 | 1,000 BAM net / 1,562 BAM gross/mo | WageIndicator (eff. 1 Jan 2025) |
| RS minimum wage 2025 (tiered) | 900 net (1,344.26 gross) basic → 1,300 net (2,000 gross) higher-education | WageIndicator (eff. 1 Jan 2025) |
| VAT (PDV) rate | 17% single rate | UINO (official) |
| VAT registration threshold | 100,000 BAM turnover (raised from 50,000 on 2 Dec 2023) | vatcalc; UINO |
| Corporate income tax | 10% (all entities) | PwC, *Corporate* (2025) |
| FBiH/RS annual return deadline | 31 March | PwC, *Tax administration* (2025) |
| BD annual return deadline | 28 February | PwC, *Tax administration* (2025) |
| Penalties | Entity-level fines + default interest; ranges not captured | PwC (2025) — `[RESEARCH GAP]` figure-level |

### Authorities and Legislation

**Authorities and legislation table**

| Topic | Reference |
| --- | --- |
| FBiH PIT | Zakon o porezu na dohodak FBiH (Porezna uprava FBiH, www.pufbih.ba) |
| FBiH contributions | Zakon o doprinosima FBiH (amended eff. 1 July 2025) |
| RS PIT | Zakon o porezu na dohodak RS (Poreska uprava RS, www.poreskaupravars.org) |
| RS contributions | Zakon o doprinosima RS |
| BD PIT | Law on Personal Income Tax of Brčko District |
| VAT | State Law on VAT — Indirect Taxation Authority (UINO), www.uino.gov.ba |

### Primary Sources

1. PwC Worldwide Tax Summaries — Bosnia and Herzegovina – Individual – Taxes on personal income — https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/taxes-on-personal-income
2. PwC — Individual – Other taxes — https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/other-taxes
3. PwC — Individual – Deductions — https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/deductions
4. PwC — Individual – Tax administration — https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/tax-administration
5. PwC — Corporate – Taxes on corporate income — https://taxsummaries.pwc.com/bosnia-and-herzegovina/corporate/taxes-on-corporate-income
6. Orbitax — FBiH Approves Cut in Employer Social Security Contribution Rates — https://orbitax.com/news/archive.php/Federation-of-Bosnia-and-Herze-58893
7. Unija — Amendments to the Law on Contributions in the FBiH (eff. 1 July 2025) — https://unija.com/en/amendments-to-the-law-on-contibutions-in-the-fbih/
8. WageIndicator — Minimum Wage FBiH from 01 Jan 2025
9. WageIndicator — Minimum Wage Republika Srpska from 01 Jan 2025
10. UINO (official) — General information on VAT system in B&H — https://www.uino.gov.ba/portal/en/vat/general-information-on-vat-system-in-bosnia-and-herzegovina/
11. vatcalc — B&H VAT registration threshold increase — https://www.vatcalc.com/bosnia-and-herzegovina/bosnia-and-herzegovina-vat-registration-rise/

### Test Suite

**Test 1 — FBiH minimum wage reconciliation.**
Input: FBiH, single, gross 1,562 BAM, no dependents.
Expected: contributions 484.22; after-contributions 1,077.78; allowance 300; base 777.78; PIT 77.78; **net 1,000.00** (matches published net minimum wage).

**Test 2 — FBiH single, gross 3,000.**
Input: FBiH, single, gross 3,000, H2 2025.
Expected: contributions 930.00; after 2,070.00; base 1,770.00; PIT 177.00; **net 1,893.00**. Employer cost ≈ 3,168.94 (150 social + 9.47 + 9.47 levies).

**Test 3 — FBiH married, 2 children, gross 4,000.**
Input: FBiH, married, spouse + 2 children, gross 4,000.
Expected: contributions 1,240.00; after 2,760.00; allowances 870.00 (300+150+150+270); base 1,890.00; PIT 189.00; **net 2,571.00**.

**Test 4 — RS single, gross 2,000.**
Input: RS, single, gross 2,000.
Expected: contributions 656.00; after 1,344.00; allowance 500; base 844.00; PIT @8% 67.52; **net 1,276.48**. Employer cost 2,000.00 (RS employer = 0%).

**Test 5 — RS paušal 2%.**
Input: RS sole trader, confirmed paušal, revenue 50,000.
Expected: PIT 2% × 50,000 = **1,000.00**. Only if eligibility confirmed — else default to 8%.

**Test 6 — Entity unknown.**
Input: gross 3,000, entity not stated.
Expected: default FBiH → net 1,893.00; flag entity assumption for reviewer (RS would differ: 8% PIT, 32.8% employee, 0% employer).

**Test 7 — VAT threshold.**
Input: sole trader, annual taxable turnover 120,000 BAM.
Expected: above 100,000 BAM → VAT registration required with UINO at 17%. (Out of scope for PIT computation — escalate per R-BA-6.)

## PROHIBITIONS

- NEVER compute B&H income tax without first confirming the entity (FBiH / RS / Brčko District) — the systems differ entirely.
- NEVER apply the RS 2% paušal rate without confirming eligibility and the revenue threshold.
- NEVER apply post-1-July-2025 FBiH employer rates to an H1 2025 period (or vice versa).
- NEVER add RS employer social contributions — RS has none (employee bears 32.8%).
- NEVER treat B&H as having a single national income tax.
- NEVER allow entertainment/representation, personal living costs, fines, or income tax itself as a deduction.
- NEVER include VAT collected on sales as income, or recoverable input VAT as an expense.
- NEVER present any figure marked `[RESEARCH GAP]` as confirmed — flag it for the reviewer.
- NEVER present tax calculations as definitive — always label as estimated and require professional sign-off.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
