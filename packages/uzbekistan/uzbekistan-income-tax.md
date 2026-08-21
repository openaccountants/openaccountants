---
name: uzbekistan-income-tax
description: Use this skill whenever asked about Uzbekistan personal income tax (PIT) for individuals, self-employed persons, and individual entrepreneurs. Trigger on phrases like "how much income tax in Uzbekistan", "Uzbekistan PIT", "soliq", "12% flat tax", "INPS pension", "social tax", "individual entrepreneur turnover tax", "non-resident tax Uzbekistan", "annual income declaration", "dividends tax Uzbekistan", "payroll Uzbekistan", "minimum wage UZS", "BHM/BRV base amount", or any question about computing or filing personal income tax for a resident or non-resident individual, an employee, a sole trader, or an individual entrepreneur in Uzbekistan. Also trigger when classifying UZS bank-statement lines for income tax, modelling take-home pay, or computing employer social tax. This skill covers the flat 12% PIT, the 5% dividend/interest rate, non-resident rates, the INPS 0.1% accumulative pension carve-out, employer social tax (12%/25%/7%/4.7%/1%), the calendar-year filing cycle, and the 2026 self-employed turnover-tax changes. ALWAYS read this skill before touching any Uzbekistan income tax work.
version: 0.1
jurisdiction: UZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uzbekistan Personal Income Tax -- Individuals & Self-Employed

## Uzbekistan Personal Income Tax -- Individuals & Self-Employed Skill v0.1

> **Tier 2 (research-verified).** Core PIT rates and the calendar filing cycle are well-confirmed by PwC Worldwide Tax Summaries (reviewed 16 January 2026). Several 2026-effective changes, the INPS mechanism, and exact penalty figures require primary-source confirmation against lex.uz / soliq.uz and are marked **[RESEARCH GAP — reviewer to confirm]**. This skill must be signed off by a qualified Uzbekistan tax practitioner before filing.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Uzbekistan (Republic of Uzbekistan / O'zbekiston Respublikasi) |
| Tax | Personal Income Tax (Jismoniy shaxslardan olinadigan daromad solig'i) |
| Currency | UZS (Uzbekistani so'm) only |
| Tax year | Calendar year (1 January -- 31 December) (PwC) |
| Primary legislation | Tax Code of the Republic of Uzbekistan (Soliq kodeksi), in force from 1 January 2020 as amended |
| Supporting legislation | Annual tax-and-budget amendment laws; Presidential Decree (July 2025) setting minimum wage / base calculation amount (BHM/BRV) effective 1 August 2025 |
| Tax authority | State Tax Committee of the Republic of Uzbekistan (Soliq qo'mitasi) |
| Filing portal | soliq.uz / my.soliq.uz e-services |
| Annual declaration deadline | 1 April of the following year; tax due by 1 June (PwC) |
| Validated by | Pending — requires sign-off by a qualified Uzbekistan tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

### PIT Rate Table (2025 — flat system, NO progressive bands)

**PIT Rate Table (2025)**  _(PwC, Taxes on personal income)_

| Income type | Taxpayer | Rate | Source |
| --- | --- | --- | --- |
| Employment, rental, capital gains, most other income | Resident individual | **12%** | PwC, Taxes on personal income |
| Dividends and interest | Resident individual | **5%** | PwC |
| Dividends from JOINT-STOCK COMPANY shares | Resident or non-resident | **EXEMPT** (1 Apr 2022 – 31 Dec 2028) | PwC |
| Employment, royalties, other Uzbek-source income | Non-resident | **12%** (reduced from 20% by Presidential Resolution) | PwC |
| Dividends and interest | Non-resident | **10%** | PwC |
| Transportation (freight) services income | Non-resident | **6%** | PwC |
| PIT in certain designated areas (e.g. Sokh district, Shahimardan / Chungara enclaves) | Resident in designated area | **1%** | LegalAct.uz |

- **Flat rate system statement** — Uzbekistan PIT is a flat 12% — there are no progressive brackets and no general tax-free personal allowance. The flat rate IS the system.  _(PwC)_

### Employer Social Tax (ST) Rates — paid by employer, NOT withheld from employee

**Employer Social Tax Rates**  _(PwC, Other taxes)_

| Employer category | Rate | Base | Source |
| --- | --- | --- | --- |
| Standard (non-budget) entity | **12%** | total payroll cost (wage fund) | PwC, Other taxes |
| State budget organisation | **25%** | total payroll cost | PwC |
| 'SOS Children's Villages of Uzbekistan' | **7.0%** | total payroll cost | PwC |
| Employers of persons with disabilities | **4.7%** | total payroll cost | PwC |
| Low-income employees relief (temporary, 1 Jan 2025 – 1 Jan 2028) | **1%** | payroll for employees earning above 1.5x minimum wage | PwC |

- **Social tax employer cost clarification** — Social tax is an EMPLOYER cost on the wage fund. It is not deducted from the employee's gross pay. Default to 12% unless the entity is a confirmed state budget organisation (25%) or qualifies for a documented reduced rate.  _(PwC)_

### Employee Carve-Out — INPS Accumulative Pension

**INPS Carve-Out**  _(LegalAct.uz)_

| Item | Rate | Mechanism | Source |
| --- | --- | --- | --- |
| INPS (Individual Accumulated Pension Account) | **0.1%** of employee gross income | Carved **OUT OF** the 12% PIT already withheld and redirected to the employee's individual accumulative pension account. **Not** an additional levy on top of the 12%. | LegalAct.uz |

- **INPS mechanism critical note** — Critical: The INPS 0.1% does NOT increase the employee's burden. Of the 12% PIT withheld, 0.1 percentage point of income is diverted to the individual pension account and 11.9 percentage points go to the budget. The total deducted from the employee is still 12%. [RESEARCH GAP — reviewer to confirm] the INPS mechanism is sourced to LegalAct.uz (a secondary site). Verify against the Tax Code before relying on the carve-out treatment for a specific client.  _(LegalAct.uz)_

### Statutory Base Amounts (from 1 August 2025)

**Statutory Base Amounts**  _(WageIndicator; goldenpages.uz)_

| Amount | Value | Previous | Purpose | Source |
| --- | --- | --- | --- | --- |
| Minimum monthly wage | **UZS 1,271,000** | UZS 1,155,000 (1 Oct 2024) | wage floor | WageIndicator |
| Base calculation amount (BHM / BRV / BCU) | **UZS 412,000** | UZS 375,000 | tax thresholds, fines, state duties, patents, IE minimum social tax | goldenpages.uz |
| Basic pension calculation amount (BVIP) | **UZS 471,000** | UZS 428,000 | pension calculations | goldenpages.uz |

- **BHM/BRV/BCU equivalence** — BHM, BRV and BCU are three names for the SAME statutory base calculation amount.  _(goldenpages.uz)_

[RESEARCH GAP — reviewer to confirm] these figures are reported from the July 2025 Presidential Decree via WageIndicator / goldenpages; the primary decree on lex.uz was not fetched. Confirm before filing.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | Treat as **non-resident** until 183-day test is documented (non-resident rates differ by income type) |
| Unknown income type | Treat as employment / general income at **12%** (the universal default) |
| Unknown employer category for social tax | **12%** (standard non-budget) — only use 25% for a confirmed state budget organisation |
| Dividend source unknown (JSC vs other) | Treat as NON-JSC dividend at **5%** (do not assume the JSC exemption) |
| Designated-area 1% rate | Do NOT apply unless the taxpayer's location is documented as a qualifying area |
| Self-employed turnover regime (2026+) | **1% turnover tax** + minimum **1 BHM/month** social tax — do NOT assume the old sub-UZS 100m exemption applies |
| INPS treatment | Carve-out within the 12% PIT — never add as an extra deduction |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — Minimum viable -- confirmation of (1) residency status (resident if present in Uzbekistan 183+ days in any consecutive 12-month period ending in the tax year — PwC), (2) the type of income (employment, dividends, interest, rental, freight, self-employment/turnover), and (3) the gross amounts in UZS for the calendar year.  _(PwC)_

Recommended -- full bank statement(s) for the tax year in CSV/PDF/pasted text, employer payroll records, dividend/interest vouchers, prior-year declaration, and (for self-employed) turnover ledger.

Ideal -- complete income summary by source, social-tax payment records, INPS contribution records, individual-entrepreneur turnover-tax filings, and (for departing expats) date of departure.

- **Refusal if minimum missing** — Refusal if minimum is missing -- SOFT WARN. No information on residency OR income type = hard stop (the rate cannot be selected). Income type known but no documentation = proceed with reviewer warning: "This computation was produced without source documents. The reviewer must verify residency, income classification, and amounts against primary records."

### Refusal Catalogue

- **R-UZ-1** — Residency unknown. "Residency determines which rate applies (residents 12%/5%; non-residents 12%/10%/6%). This skill cannot select a rate without knowing whether the individual was present in Uzbekistan 183+ days in the relevant 12-month period. Please confirm."
- **R-UZ-2** — Corporate income tax / legal entities. "This skill covers individuals, sole traders and individual entrepreneurs only. Companies file corporate income tax / turnover tax separately. Escalate to a qualified Uzbekistan tax practitioner."
- **R-UZ-3** — Designated-area 1% rate claimed. "The 1% PIT rate applies only to specific designated areas (e.g. Sokh, Shahimardan/Chungara enclaves). Do not apply it without documentary proof of the taxpayer's qualifying location. Escalate to a reviewer."
- **R-UZ-4** — New 2026 special tax regime for foreign citizens. "A special tax regime for foreign citizens is reported to be introduced from January 2026, but its rate, eligibility and any minimum-salary threshold are unconfirmed. Do not compute under it. Escalate to a qualified practitioner. [RESEARCH GAP — reviewer to confirm]"
- **R-UZ-5** — Penalties / arrears / enforcement. "Specific late-filing and late-payment penalty percentages and interest (peni) are not confirmed in the available sources. Do not advise on penalty amounts. Escalate to a qualified practitioner. [RESEARCH GAP — reviewer to confirm]"
- **R-UZ-6** — VAT / corporate turnover for entities. "This skill covers personal income tax only. For Uzbekistan VAT or company turnover tax, use the relevant Uzbekistan VAT / corporate skill."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a UZS bank-statement transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty name or description. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

> **Note on language.** Uzbek statements use Latin-script Uzbek, Cyrillic, or Russian. Common terms: *daromad* (income), *ish haqi / oylik* (salary/wages), *dividend* (dividend), *foiz / protsent* (interest/percent), *ijara* (rent), *soliq* (tax), *pensiya* (pension), *o'tkazma / perevod* (transfer).

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| ISH HAQI, OYLIK, ZARPLATA, SALARY, [employer name] | Employment income | 12% PIT (resident) / 12% (non-resident) | Withheld at source by employer; verify withholding done |
| GONORAR, HONORARIUM, KONSULTATSIYA, CONSULTANCY, FEES | Self-employment / service income | 12% (resident general income) | If individual entrepreneur, see turnover-tax regime |
| DIVIDEND, DIVIDENDLAR | Dividend income | 5% (resident) / 10% (non-resident); **EXEMPT if from JSC shares** | Confirm JSC vs other; default 5% if unknown |
| FOIZ, PROTSENT, INTEREST | Interest income | 5% (resident) / 10% (non-resident) | Bank/loan interest |
| IJARA, ARENDA, RENT RECEIVED | Rental income | 12% (resident) | Property/IP income — declarable |
| FRAHT, FREIGHT, TRANSPORT (non-resident carrier) | Freight/transport income | 6% (non-resident only) | Non-resident transportation services |
| UPWORK, FIVERR, STRIPE, PAYPAL, WISE PAYOUT | Platform / freelance payout | 12% (resident self-employment) | Match to underlying invoices; foreign-source for residents is declarable |
| SOLIQ QAYTARISH, TAX REFUND | Not income | EXCLUDE | Refund of prior-year tax |
| GRANT, SUBSIDIYA | Check nature | EXCLUDE if capital grant; income if revenue grant | Flag for reviewer |

### 3.2 Withholding / Tax & Pension Debits (NOT deductions against income)

**Withholding / Tax & Pension Debits**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| PIT, JISMONIY SHAXS SOLIG'I, NDFL | Income tax withheld/paid | Credit against PIT liability — NOT an expense | 12% withheld at source |
| INPS, JAMG'ARMA PENSIYA, PENSION ACCOUNT | INPS pension carve-out | Part of the 12% PIT (0.1% of income) — do NOT double count | Carved out, not additional |
| IJTIMOIY SOLIQ, SOCIAL TAX, ST | Employer social tax | Employer cost (12%/25%/7%/4.7%/1%) — NOT employee deduction | Only relevant to employer cost models |

### 3.3 Self-Employed / Individual Entrepreneur Patterns

**Self-Employed / Individual Entrepreneur Patterns**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| OBOROT SOLIG'I, TURNOVER TAX | Turnover tax | 1% on turnover up to UZS 1bn (from 1 Jan 2026) | See Section 5.7 |
| IE SOCIAL TAX, IP IJTIMOIY SOLIQ | IE minimum social tax | At least 1 BHM/month (UZS 412,000) regardless of turnover | PwC |
| PATENT | Patent fee | Historic fixed-amount regime — cancelled from 1 Jan 2026 | [RESEARCH GAP — confirm year] |

### 3.4 Exclusions (Neither Income nor Deduction)

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| O'Z HISOBIM, OWN ACCOUNT, INTERNAL TRANSFER | EXCLUDE | Own-account transfer |
| KREDIT, QARZ, LOAN REPAYMENT | EXCLUDE | Loan principal movement |
| BANK KOMISSIYASI, BANK FEE (personal) | EXCLUDE | Personal bank charge |

### 3.5 Uzbek Banks -- Statement Format Reference

**Uzbek Banks Statement Format Reference**

| Bank | Common patterns | Notes |
| --- | --- | --- |
| NBU (National Bank of Uzbekistan) | O'TKAZMA, ISH HAQI, KOMISSIYA | PDF/CSV; Latin/Cyrillic mix |
| Kapitalbank | PEREVOD, ZARPLATA, OPLATA | Russian + Uzbek descriptions |
| Hamkorbank | O'TKAZMA, IJARA, DIVIDEND | Latin-script Uzbek |
| Ipoteka Bank / Ipak Yo'li | PEREVOD, NALOG, PENSIYA | Mixed-language |
| Payme / Click (e-wallet exports) | TO'LOV, PAYMENT | Reference-rich descriptions |

## Section 4 -- Worked Examples

All figures in UZS. Rates per Section 1 (PwC / LegalAct.uz). Arithmetic recomputed end-to-end.

### Example 1 -- Resident Employee, Monthly Salary

**Input line:**
`31/03/2025 ; NBU ; ISH HAQI MART ; [employer] ; +5,000,000.00 ; UZS`

**Reasoning:**
Resident employment income. PIT = 12% of 5,000,000 = **600,000**. Of that 600,000, the INPS carve-out is 0.1% of income = 0.1% × 5,000,000 = **5,000** redirected to the individual pension account (the remaining 595,000 goes to the budget). The INPS is NOT additional. Net pay to employee = 5,000,000 − 600,000 = **4,400,000**.

**Employer side (not deducted from employee):** social tax 12% × 5,000,000 = **600,000**.

**Classification:** Gross 5,000,000; PIT 600,000 (incl. INPS 5,000); Net 4,400,000.

### Example 2 -- Cumulative Monthly Withholding Check

**Input:** Same employee, gross 5,000,000 in January, February and March.

**Reasoning (cumulative method, LegalAct.uz):** PIT is computed cumulatively: PIT(Jan–current month) − PIT(Jan–previous month).
- Cumulative Jan–Mar income = 15,000,000. Cumulative PIT = 12% × 15,000,000 = 1,800,000.
- Cumulative Jan–Feb PIT = 12% × 10,000,000 = 1,200,000.
- March withholding = 1,800,000 − 1,200,000 = **600,000**. ✓ Consistent with the flat monthly 600,000.

**Classification:** March PIT withheld = 600,000.

### Example 3 -- Resident Dividend from a Non-JSC Company

**Input line:**
`15/05/2025 ; Kapitalbank ; DIVIDEND ; OOO [company] ; +10,000,000.00 ; UZS`

**Reasoning:**
Resident dividend from a limited-liability company (not joint-stock). Rate = 5%. PIT = 5% × 10,000,000 = **500,000**. (If the payer were a joint-stock company, the dividend would be PIT-EXEMPT through 31 Dec 2028.)

**Classification:** Dividend 10,000,000; PIT 500,000; net 9,500,000.

### Example 4 -- Non-Resident Freight Income

**Input line:**
`20/06/2025 ; Hamkorbank ; FREIGHT SERVICES ; [non-resident carrier] ; +50,000,000.00 ; UZS`

**Reasoning:**
Non-resident transportation (freight) services income. Rate = 6%. PIT = 6% × 50,000,000 = **3,000,000**.

**Classification:** Freight income 50,000,000; non-resident PIT 3,000,000.

### Example 5 -- Individual Entrepreneur, 2026 Turnover Regime

**Input:** Individual entrepreneur, annual turnover 800,000,000 in 2026 (≤ UZS 1bn).

**Reasoning:**
From 1 January 2026 turnover ≤ UZS 1bn attracts a **1% turnover tax** (PwC significant developments). Turnover tax = 1% × 800,000,000 = **8,000,000**. Plus minimum social tax of 1 BHM/month = 412,000 × 12 = **4,944,000** regardless of turnover (PwC). The old sub-UZS-100m exemption is abolished from 1 Jan 2026 — do not apply it. Total = 8,000,000 + 4,944,000 = **12,944,000**.

**Classification:** Turnover tax 8,000,000; social tax 4,944,000; total 12,944,000.

### Example 6 -- Annual Salary, Full-Year Reconciliation

**Input:** Resident employee, total annual employment income 60,000,000.

**Reasoning:**
PIT = 12% × 60,000,000 = **7,200,000**. INPS carve-out = 0.1% × 60,000,000 = **60,000** (part of the 7,200,000, not extra). Net = 60,000,000 − 7,200,000 = **52,800,000**. Employer social tax (standard) = 12% × 60,000,000 = **7,200,000** (employer cost, not deducted).

**Classification:** Gross 60,000,000; PIT 7,200,000 (incl. INPS 60,000); Net 52,800,000.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Flat-Rate System

- **Flat rate system** — Personal income tax is a flat 12% on employment, rental, capital-gains and most other income of resident individuals. There are no progressive bands and no general tax-free personal allowance.  _(PwC; Tax Code of the Republic of Uzbekistan (in force from 1 Jan 2020, as amended))_

### 5.2 Dividends and Interest (Residents)

- **Dividends and interest residents** — Resident individuals pay 5% PIT on dividends and interest. Dividends paid on joint-stock company shares are PIT-EXEMPT for both residents and non-residents from 1 April 2022 through 31 December 2028.  _(PwC)_

### 5.3 Non-Resident Rates

**Non-Resident Rates**  _(PwC)_

| Income type | Rate | Source |
| --- | --- | --- |
| Employment, royalties, other Uzbek-source income | 12% (reduced from 20% by Presidential Resolution) | PwC |
| Dividends and interest | 10% | PwC |
| Transportation (freight) services income | 6% | PwC |

- **Residency definition** — Residency = present in Uzbekistan 183+ days in any consecutive 12-month period ending in the calendar tax year.  _(PwC)_

### 5.4 Designated-Area Reduced Rate

- **Designated-area reduced rate** — A 1% PIT rate applies for individuals in certain designated areas (e.g. Sokh district, Shahimardan, Chungara/Shahimardan enclaves). Apply only with documented proof of qualifying location — otherwise default to 12%.  _(LegalAct.uz)_

### 5.5 Withholding and INPS Mechanism

- **Cumulative withholding** — Employers withhold 12% PIT cumulatively each month: PIT(Jan–current month) − PIT(Jan–previous month), remitted with salary no later than the PIT reporting deadline.  _(PwC / LegalAct.uz)_
- **INPS carve-out mechanism** — The INPS 0.1% of employee income is carved OUT of the 12% PIT into the employee's individual accumulative pension account — it is NOT an additional levy.  _(LegalAct.uz; [RESEARCH GAP — reviewer to confirm] against the Tax Code.)_
- **Non-primary workplace income** — Income from a non-primary place of work is taxed at a flat 12% without benefits/deductions and reconciled via the annual declaration.  _(LegalAct.uz)_

### 5.6 Employer Social Tax

- **Employer social tax rates list** — Social tax on the total wage fund, paid by the employer (NOT withheld from the employee): 12% standard (non-budget) entities; 25% state budget organisations; 7.0% 'SOS Children's Villages of Uzbekistan'; 4.7% employers of persons with disabilities; 1% temporary relief, 1 Jan 2025 – 1 Jan 2028, for employees earning above 1.5x minimum wage.  _(PwC)_
- **No ceiling; IE minimum social tax** — There is no general ceiling. Individual entrepreneurs pay social tax of at least 1 BHM/month (UZS 412,000) regardless of turnover.  _(PwC)_

### 5.7 Self-Employed / Individual Entrepreneurs (2026 changes)

**Self-Employed / Individual Entrepreneurs 2026 changes**  _(PwC significant developments)_

| Rule | Detail | Source |
| --- | --- | --- |
| Turnover tax (from 1 Jan 2026) | 1% where annual turnover ≤ UZS 1 billion | PwC significant developments |
| Sub-UZS-100m exemption | ABOLISHED from 1 Jan 2026 | PwC / EY |
| Fixed-amount PIT regime for IEs | CANCELLED from 1 Jan 2026 | PwC / EY |
| IE minimum social tax | At least 1 BHM/month (UZS 412,000) regardless of turnover | PwC |
| Remote registration | From 1 Nov 2025, self-employed/IEs can register remotely via digital platforms with biometric + SMS verification | PwC |

### 5.8 Tax Year and Filing

- **Tax year** — Tax year = calendar year (1 Jan – 31 Dec).  _(PwC)_
- **Annual declaration deadline** — Annual PIT declaration due by 1 April of the following year; resulting tax due by 1 June.  _(PwC)_
- **Departing expatriates exit return** — Departing expatriates file an exit return at least one month before departure (unless leaving before 1 February).  _(PwC)_

### 5.9 Statute of Limitations

- **Statute of limitations** — Three-year limitation period for individual tax matters; no formal individual audits — declarations are reviewed at filing.  _(PwC)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Residency Determination

- Apply the 183-day test over any consecutive 12-month period ending in the tax year.
- Dual residence and treaty tie-breakers require treaty analysis.
- **Flag for reviewer:** confirm day-count and any applicable double-tax treaty.

### 6.2 JSC vs Non-JSC Dividend Classification

- JSC-share dividends are exempt (to 31 Dec 2028); other dividends are 5% (resident) / 10% (non-resident).
- **Conservative default:** treat as non-JSC (5%) until JSC status is documented.
- **Flag for reviewer:** confirm the legal form of the distributing entity.

### 6.3 Foreign-Source Income of Residents

- Residents are taxable on worldwide income; foreign-source income generally requires an annual declaration.
- **Flag for reviewer:** confirm foreign-source amounts, foreign tax paid, and treaty relief.

### 6.4 Designated-Area 1% Rate

- Narrow, location-specific relief.
- **Conservative default:** do not apply.
- **Flag for reviewer:** require documentary proof of qualifying location.

### 6.5 New 2026 Special Tax Regime for Foreign Citizens

- A special regime for foreign citizens is reported from January 2026; rate, eligibility and any minimum-salary threshold are unconfirmed.
- **[RESEARCH GAP — reviewer to confirm]** against the official text. Do not compute under it without confirmation.

### 6.6 INPS Treatment in Take-Home Models

- Treat 0.1% INPS as part of the 12% PIT, never as an extra deduction.
- **Flag for reviewer:** confirm the carve-out mechanism against the Tax Code if material to the model.

## Section 7 -- Excel Working Paper Template

```
UZBEKISTAN PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025 (calendar year)
Client: ___________________________
Residency: Resident (183+ days) / Non-resident
Currency: UZS

A. INCOME BY SOURCE (gross, UZS)
  A1. Employment income (primary)               ___________
  A2. Employment income (secondary)             ___________
  A3. Self-employment / service income          ___________
  A4. Rental income                             ___________
  A5. Dividends — JSC shares (EXEMPT to 2028)   ___________
  A6. Dividends — non-JSC                        ___________
  A7. Interest                                   ___________
  A8. Freight/transport (non-resident only)     ___________
  A9. Foreign-source income (residents)          ___________

B. PIT BY RATE
  B1. 12% income (A1+A2+A3+A4+A9)  x 12%        ___________
  B2. 5% income, resident (A6+A7) x 5%          ___________
  B3. 10% income, non-resident (A6+A7) x 10%    ___________
  B4. 6% freight, non-resident (A8) x 6%        ___________
  B5. 1% designated-area (if documented)        ___________
  B6. TOTAL PIT (sum of applicable B rows)      ___________

C. INPS CARVE-OUT (informational — within B)
  C1. 0.1% x employment income                  ___________
      (part of B1, NOT an additional cost)

D. EMPLOYER SOCIAL TAX (cost model only)
  D1. Wage fund                                  ___________
  D2. Rate (12% / 25% / 7% / 4.7% / 1%)         ___________
  D3. Social tax (D1 x D2)                       ___________

E. SELF-EMPLOYED / IE (2026+)
  E1. Annual turnover (≤ UZS 1bn)               ___________
  E2. Turnover tax (E1 x 1%)                     ___________
  E3. Minimum social tax (1 BHM x 12 months)    ___________
  E4. TOTAL IE liability (E2 + E3)               ___________

F. NET / DUE
  F1. PIT withheld at source                     ___________
  F2. Tax already paid                           ___________
  F3. Tax due / (refund) (B6 - F1 - F2)         ___________

REVIEWER FLAGS:
  [ ] Residency confirmed (183-day count)?
  [ ] Income classified by correct rate?
  [ ] JSC vs non-JSC dividend confirmed?
  [ ] INPS treated as carve-out, not extra?
  [ ] Social-tax employer category confirmed (12% default)?
  [ ] Designated-area 1% rate proven (if used)?
  [ ] 2026 turnover regime applied for the right year?
  [ ] BHM/min-wage figures confirmed against lex.uz?
```

## Section 8 -- Bank Statement Reading Guide

### Uzbek Bank Statement Formats

**Uzbek Bank Statement Formats**

| Bank | Format | Key fields | Notes |
| --- | --- | --- | --- |
| NBU (National Bank) | PDF, CSV | Sana (date), Tavsif (description), Debet, Kredit, Qoldiq (balance) | Latin/Cyrillic mix |
| Kapitalbank | PDF, CSV | Дата, Описание, Сумма | Russian-language descriptions common |
| Hamkorbank | PDF | Sana, Tavsif, Summa | Latin-script Uzbek |
| Ipoteka Bank | PDF, CSV | Sana / Дата, Tavsif, Summa | Mixed-language |
| Payme / Click (e-wallet) | CSV | Date, Type, Amount, Reference | Reference-rich |

### Key Uzbek / Russian Banking Terms

**Key Uzbek / Russian Banking Terms**

| Term | English | Classification hint |
| --- | --- | --- |
| ISH HAQI / OYLIK / ZARPLATA | Salary / wages | Employment income (12%) |
| O'TKAZMA / PEREVOD | Transfer | Check direction for income/expense |
| DIVIDEND | Dividend | 5% resident / 10% non-resident; JSC exempt |
| FOIZ / PROTSENT | Interest | 5% resident / 10% non-resident |
| IJARA / ARENDA | Rent | Rental income (12%) |
| SOLIQ / NALOG | Tax | Tax payment — credit, not expense |
| PENSIYA / INPS | Pension / INPS | Carve-out within 12% PIT |
| KOMISSIYA | Commission/fee | Bank charge |
| TO'LOV / OPLATA | Payment | Check counterparty |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions:

```
ONBOARDING QUESTIONS -- UZBEKISTAN PERSONAL INCOME TAX
1. Residency: were you present in Uzbekistan 183+ days in the relevant 12-month period?
2. What types of income did you receive (salary, self-employment, dividends, interest, rent, freight, foreign)?
3. For dividends: were they paid on joint-stock company shares (JSC) or another entity type?
4. Are you an employee, a sole trader, or a registered individual entrepreneur?
5. (Employers) Are you a standard entity (12% social tax) or a state budget organisation (25%)?
6. (Self-employed, 2026) What was your annual turnover? Was it ≤ UZS 1 billion?
7. Do you operate in a designated reduced-rate area (e.g. Sokh, Shahimardan)?
8. (Expats) Are you planning to depart Uzbekistan? On what date?
9. Total amounts in UZS for each income source for the calendar year?
10. PIT already withheld at source / tax already paid?
```

## Section 10 -- Reference Material

### Key Legislation & Authority References

**Key Legislation & Authority References**

| Topic | Reference | Source |
| --- | --- | --- |
| Flat 12% PIT; 5% dividends/interest | Tax Code; PwC, Taxes on personal income | PwC (reviewed 16 Jan 2026) |
| Non-resident rates (12%/10%/6%) | Tax Code; Presidential Resolution | PwC |
| JSC dividend exemption (to 31 Dec 2028) | Tax Code amendment | PwC |
| INPS 0.1% carve-out | LegalAct.uz | **[RESEARCH GAP — reviewer to confirm]** |
| Employer social tax (12%/25%/7%/4.7%/1%) | Tax Code; PwC Other taxes | PwC |
| Residency (183 days) | Tax Code | PwC |
| Filing (1 Apr) / payment (1 Jun) | Tax Code | PwC |
| Exit return (1 month before departure) | Tax Code | PwC |
| 2026 turnover tax 1% / exemption abolition | Amendment laws | PwC / EY |
| Minimum wage UZS 1,271,000 / BHM UZS 412,000 (1 Aug 2025) | Presidential Decree (Jul 2025) | WageIndicator / goldenpages — **[RESEARCH GAP — confirm on lex.uz]** |
| Late-filing / late-payment penalties (peni) | Tax Code (general) | **[RESEARCH GAP — reviewer to confirm exact %]** |

### Source List

**Source List**

| Title | Publisher | URL |
| --- | --- | --- |
| Uzbekistan — Individual — Taxes on personal income | PwC Worldwide Tax Summaries (reviewed 16 Jan 2026) | https://taxsummaries.pwc.com/republic-of-uzbekistan/individual/taxes-on-personal-income |
| Uzbekistan — Individual — Tax administration | PwC | https://taxsummaries.pwc.com/republic-of-uzbekistan/individual/tax-administration |
| Uzbekistan — Individual — Significant developments | PwC | https://taxsummaries.pwc.com/republic-of-uzbekistan/individual/significant-developments |
| Uzbekistan — Other taxes (Social Tax) | PwC | https://taxsummaries.pwc.com/republic-of-uzbekistan/corporate/other-taxes |
| Uzbekistan: tax updates effective from 2026 | EY Global (Tax Alert, Jan 2026) | https://www.ey.com/en_uz/technical/tax-alerts/2026/01/uzbekistan-tax-updates-2026 |
| How to Calculate PIT in Uzbekistan | LegalAct.uz | https://legalact.uz/en/news/personal-income-tax-in-uzbekistan-how-calculate-correctly |
| Minimum Wage Updated from 01 August 2025 | WageIndicator.org | https://wageindicator.org/salary/minimum-wage/uzbekistan |
| Minimum wage, basic salary and pension today | goldenpages.uz | https://www.goldenpages.uz/en/zarplata/ |

### Test Suite

**Test 1 -- Resident monthly salary.**
Input: Resident, monthly gross 5,000,000.
Expected: PIT 12% = 600,000 (incl. INPS 0.1% = 5,000 carved out); net = 4,400,000; employer social tax 12% = 600,000.

**Test 2 -- Cumulative withholding.**
Input: Same employee, 5,000,000 in each of Jan/Feb/Mar.
Expected: March PIT = 12% × 15,000,000 − 12% × 10,000,000 = 1,800,000 − 1,200,000 = 600,000.

**Test 3 -- Resident non-JSC dividend.**
Input: Resident dividend 10,000,000 from an LLC.
Expected: 5% = 500,000; net 9,500,000. (If JSC: exempt.)

**Test 4 -- Non-resident freight.**
Input: Non-resident freight income 50,000,000.
Expected: 6% = 3,000,000.

**Test 5 -- IE 2026 turnover regime.**
Input: Individual entrepreneur, 2026 turnover 800,000,000 (≤ UZS 1bn).
Expected: turnover tax 1% = 8,000,000; minimum social tax 412,000 × 12 = 4,944,000; total 12,944,000. Old sub-100m exemption does NOT apply.

**Test 6 -- Annual salary reconciliation.**
Input: Resident, annual employment income 60,000,000.
Expected: PIT 12% = 7,200,000 (incl. INPS 0.1% = 60,000); net = 52,800,000; employer social tax 12% = 7,200,000.

**Test 7 -- Non-resident dividend.**
Input: Non-resident dividend 10,000,000 from an LLC.
Expected: 10% = 1,000,000; net 9,000,000. (If JSC: exempt.)

## PROHIBITIONS

- NEVER apply a rate without first confirming residency (resident vs non-resident rates differ).
- NEVER add the INPS 0.1% as an extra deduction on top of the 12% PIT — it is carved OUT of the 12%.
- NEVER treat employer social tax (12%/25%/etc.) as a deduction from the employee's gross pay.
- NEVER assume a dividend is JSC-exempt without confirming the entity's legal form — default to 5% (resident).
- NEVER apply the designated-area 1% rate without documentary proof of qualifying location.
- NEVER apply the abolished sub-UZS-100m self-employed exemption to 2026-onward periods.
- NEVER state late-filing/late-payment penalty percentages — they are unconfirmed [RESEARCH GAP].
- NEVER compute under the new 2026 "special tax regime for foreign citizens" — its terms are unconfirmed.
- NEVER use progressive bands — Uzbekistan PIT is flat.
- NEVER present tax calculations as definitive — always label as estimated and pending reviewer sign-off.

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
