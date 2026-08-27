---
name: kosovo-social-contributions
description: Use this skill whenever asked about Kosovo payroll social contributions and wage taxation for employees and employers. Trigger on phrases like "how much pension contribution in Kosovo", "Kosovo payroll tax", "mandatory pension Trusti", "KPST contribution", "5% pension Kosovo", "Kosovo social security", "do I pay health insurance in Kosovo", "Kosovo PIT on salary", "withholding tax wages Kosovo", "WM declaration", "CM pension form", "secondary employer 10%", or any question about Kosovo employment-tax obligations. Also trigger when classifying bank statement transactions that relate to TAK/ATK tax payments, Trusti/KPST pension transfers, or salary debits from Kosovan banks (BKT, ProCredit, Raiffeisen Kosovo, TEB, NLB, Banka Ekonomike). Also trigger when preparing a monthly WM (wage withholding) or CM (pension contribution) declaration, or the annual PD personal income tax return. This skill covers the mandatory 10% pension split (5% employee + 5% employer), the 0%/8%/10% progressive personal income tax, the flat 10% secondary-employer withholding, the enacted-but-dormant health insurance regime, minimum wage, benefit-in-kind thresholds, payment schedule, penalties, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Kosovo payroll or social-contribution work.
version: 0.1
jurisdiction: XK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kosovo Social Contributions & Wage Taxation

## Kosovo Social Contributions & Wage Taxation Skill v0.1

> **Tier 2 (research-verified).** Figures are sourced from PwC Worldwide Tax Summaries (last reviewed 13 January 2026), EY/Lexology summaries of Law No. 08/L-142, and the Tax Administration of Kosovo (TAK/ATK) guidance portal. This skill has NOT yet been signed off by a Kosovo-warranted accountant (`verified_by: pending`). Treat every figure as estimated pending professional review.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**  _(PwC Kosovo (Other taxes; Taxes on personal income; Tax administration); EY/Lexology (Law 08/L-142); TAK CRM guidance portal. URLs in Section 10.)_

| Field | Value |
| --- | --- |
| Country | Kosovo (Republic of Kosovo) |
| Jurisdiction code | XK |
| Currency | EUR only |
| Primary social-contribution legislation | Law No. 04/L-101 on Pension Funds of Kosovo (mandatory pension) |
| Wage tax legislation | Law No. 05/L-028 on Personal Income Tax, as amended by Law No. 08/L-142 (Official Gazette, effective 23 Aug 2024) |
| Health insurance legislation | Law No. 04/L-249 on Health Insurance — enacted but NOT operational (no contributions collected as of 2025) |
| Tax authority | Tax Administration of Kosovo (TAK / Administrata Tatimore e Kosovës, ATK) — www.atk-ks.org / crmm.atk-ks.org |
| Pension administrator | Kosovo Pension Savings Trust (Trusti / KPST, www.trusti.org), supervised by Central Bank of Kosovo (BQK) |
| Mandatory pension — employee share | 5% of gross wages (withheld) |
| Mandatory pension — employer share | 5% of gross wages (employer cost) |
| Mandatory pension — total | 10% of gross wages |
| Voluntary additional pension | Up to +15% employee and +15% employer (combined up to 30% above the mandatory 10%) |
| Health insurance contribution | 0% — NOT collected (regime dormant) |
| Unemployment / sickness contribution | 0% — none exists |
| Personal income tax on wages | Progressive 0% / 8% / 10% at the primary employer; flat 10% at any secondary employer |
| Minimum wage | EUR 350.00/month gross (eff. 1 Oct 2024); rises to EUR 425.00 (1 Jan 2026) and EUR 500.00 (1 Jul 2026) |
| Tax year | Calendar year |
| Monthly forms | WM (wage withholding), CM (pension) — declare/pay by 15th of following month |
| Quarterly form | CI (individual pension contribution report) — 1st–15th of month after each quarter |
| Annual return | PD / PD24 (personal income tax) — due 31 March of following year |
| Validated by | Pending — requires sign-off by a Kosovo-warranted accountant |
| Validation date | Pending |

**Contribution overview (per EUR of gross wages)**  _(PwC Kosovo — Other taxes (pension); GrECo/Asinta (health insurance not implemented).)_

| Contribution | Employee | Employer | Total | Legal basis |
| --- | --- | --- | --- | --- |
| Mandatory pension (KPST/Trusti) | 5% | 5% | 10% | Law No. 04/L-101 |
| Health insurance | 0% | 0% | 0% | Law No. 04/L-249 (dormant) |
| Unemployment / sickness / other | 0% | 0% | 0% | none |
| **Total mandatory payroll contributions** | **5%** | **5%** | **10%** | — |

> **Arithmetic check:** employee column 5% + 0% + 0% = **5%**; employer column 5% + 0% + 0% = **5%**; total column 10% + 0% + 0% = **10%**, and 5% + 5% = **10%**. Rows reconcile.
> **Source:** PwC Kosovo — Other taxes (pension); GrECo/Asinta (health insurance not implemented).

**Personal income tax on employment income (primary employer — progressive)**  _(PwC Kosovo — Taxes on personal income; EY (Law 08/L-142, effective 23 Aug 2024, replacing the former four-band 0%/4%/8%/10% schedule).)_

| Band (annual) | Band (monthly) | Marginal rate | Tax within band | Cumulative tax at top of band |
| --- | --- | --- | --- | --- |
| Up to EUR 3,000.00 | Up to EUR 250.00 | 0% | EUR 0.00 | EUR 0.00 |
| EUR 3,000.01 – 5,400.00 | EUR 250.01 – 450.00 | 8% | 8% × 2,400 = EUR 192.00 | EUR 192.00 |
| EUR 5,400.01 and above | EUR 450.01 and above | 10% | 10% × (income − 5,400) | EUR 192.00 + 10% × excess |

> **Arithmetic check:** band 2 width = 5,400 − 3,000 = 2,400; 8% × 2,400 = **192.00**. Cumulative tax at EUR 5,400 = **192.00**. Band 3 starts from a cumulative base of EUR 192.00. Consistent.
> **Source:** PwC Kosovo — Taxes on personal income; EY (Law 08/L-142, effective 23 Aug 2024, replacing the former four-band 0%/4%/8%/10% schedule).

**Secondary-employer withholding**  _(Lexology / TAK notice)_

| Situation | Treatment | Source |
| --- | --- | --- |
| Single (primary) employer | Progressive 0%/8%/10% bands above | PwC Kosovo PIT |
| Each secondary employer (employee with >1 employer) | Flat 10% withholding on the wages it pays (no 0% band) | Lexology / TAK notice — *[RESEARCH GAP: documented in Big-4/legal summaries; ATK official page not directly fetchable during research — reviewer to confirm against TAK PIT regulation text]* |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether worker is employee or contractor | Treat as employee; apply 10% pension + PIT withholding; flag for reviewer |
| Unknown primary vs secondary employer | STOP — ask. Bands vs flat 10% depend entirely on this |
| Unknown gross vs net wage | Treat figure as GROSS; flag for reviewer |
| Unknown whether pension is deductible from PIT base | Compute PIT on gross wages (conservative — higher tax); flag — see Section 6 T2-1 |
| Health/unemployment contribution asked for | State 0% — not collected; cite dormant Law 04/L-249 |
| Minimum-wage figure for a payroll period | Use EUR 350.00 (2025); confirm against the operative Government Decision for the period |
| Pension contribution ceiling | Compute uncapped; flag — no statutory ceiling found (see Section 6 T2-2) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- gross monthly wage, and whether this is the employee's PRIMARY or SECONDARY employer. Without the primary/secondary flag, STOP — the PIT method changes entirely (progressive bands vs flat 10%).

**Recommended** -- pay period, whether the figure provided is gross or net, employer/employee names, and whether any benefits in kind exceed EUR 65/month.

**Ideal** -- the employer's TAK fiscal number, monthly WM and CM declarations, KPST/Trusti contribution statements, and the prior-year PD return.

### Refusal catalogue

- **R-XK-1 -- Primary/secondary employer unknown** — Cannot compute Kosovo wage tax without knowing whether this is the employee's primary or secondary employer. The primary employer applies progressive 0%/8%/10% bands; each secondary employer withholds a flat 10% with no 0% band. Designating primary vs secondary is a legal obligation of the employee. Please confirm before I proceed. (Trigger: employee may have more than one employer and the designation is unclear.)
- **R-XK-2 -- Health insurance contribution requested** — Kosovo's mandatory health-insurance system (Law No. 04/L-249) is enacted but NOT operational — no employer or employee health contributions are collected as of 2025; public healthcare is funded from general taxation. I will not compute a health contribution. Because this bill has repeatedly returned to the legislative agenda, confirm it has not commenced for the relevant payroll period. (Trigger: client asks to compute a Kosovo health-insurance payroll contribution.)
- **R-XK-3 -- Pension contribution ceiling / very high earner** — No statutory maximum pensionable-wage ceiling on the 10% mandatory pension contribution was found in the consulted authoritative sources. I can compute uncapped (10% of full gross wage), but a reviewer must verify against the full text of Law No. 04/L-101 and KPST rules before relying on uncapped figures for a high earner. (Trigger: client asks whether the 10% pension caps out at a maximum pensionable wage.)
- **R-XK-4 -- Pension arrears / penalties** — Understatement penalties (15%–25% of the under-declared amount) and monthly late-payment interest (set above the commercial bank lending rate, accruing up to 10 years) apply. Do not attempt to quantify arrears without a TAK statement. Escalate to a Kosovo-warranted accountant. (Trigger: client has undeclared or unpaid prior-period pension contributions or wage tax.)
- **R-XK-5 -- Voluntary / occupational pension structuring** — Voluntary additional pension contributions (up to a further 15% by the employee and 15% by the employer) are permitted but their tax treatment and election mechanics are case-specific. Escalate to a Kosovo-warranted accountant. (Trigger: client asks about the optional additional pension (up to +15%/+15%) or scheme structuring.)

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Kosovo payroll, pension and wage tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Tax and pension remittances EXCLUDE from any VAT/revenue/expense recharacterisation — they are statutory payroll obligations, not business supplies. Kosovo uses EUR. Albanian-language terms appear alongside English on many statements.

### 3.1 Pension contribution remittances (KPST / Trusti)

**Pension contribution remittances table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRUSTI, KPST | EXCLUDE -- pension contribution | Mandatory 10% to Kosovo Pension Savings Trust |
| FONDI I KURSIMEVE PENSIONALE, KURSIMET PENSIONALE | EXCLUDE -- pension contribution | Albanian: "pension savings fund" |
| PENSION, PENSIONI | EXCLUDE -- pension contribution | Generic pension reference (outgoing) |
| KONTRIBUT PENSIONAL, KONTRIBUTI | EXCLUDE -- pension contribution | Albanian: "pension contribution" |
| CM, FORM CM | EXCLUDE -- pension contribution | TAK monthly pension form reference |

### 3.2 Wage tax / TAK remittances

**Wage tax / TAK remittances table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TAK, ATK, ADMINISTRATA TATIMORE | EXCLUDE -- wage withholding tax | Tax Administration of Kosovo |
| WM, FORM WM | EXCLUDE -- wage withholding tax | TAK monthly wage withholding form |
| TATIMI NE PAGA, TATIM PAGA | EXCLUDE -- wage withholding tax | Albanian: "tax on wages" |
| MBAJTJE NE BURIM, WITHHOLDING | EXCLUDE -- withholding tax | Albanian: "withheld at source" |

### 3.3 TAK debits appearing on specific Kosovan banks

**TAK debits by bank table**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| BKT (Banka Kombëtare Tregtare) | "TAK" / "ATK" / "PAGESA TATIMORE" | EXCLUDE -- tax/pension remittance |
| ProCredit Bank Kosovo | "ADMINISTRATA TATIMORE" / "TRUSTI" | EXCLUDE -- tax/pension remittance |
| Raiffeisen Bank Kosovo | "TAK PAYMENT" / "KPST" | EXCLUDE -- tax/pension remittance |
| TEB Sh.A. | "TATIMI NE PAGA" / "KONTRIBUT PENSIONAL" | EXCLUDE -- tax/pension remittance |
| NLB Banka / Banka Ekonomike | "TRUSTI" / "ATK" | EXCLUDE -- tax/pension remittance |

### 3.4 Salary and payroll (exclude from contribution classification)

**Salary and payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PAGA, PAGAT, ROGA (outgoing) | EXCLUDE -- payroll expense | Wage payment; not a contribution remittance |
| SALARY, NET PAY (outgoing) | EXCLUDE -- payroll expense | Net wage to employee |
| PAGA, SALARY (incoming) | EXCLUDE -- employment income received | Not a contribution payment |

### 3.5 Pension benefits received (NOT contributions)

**Pension benefits received table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSIONI BAZIK, BASIC PENSION (incoming) | EXCLUDE -- pension income received | Budget-funded basic state pension |
| TRUSTI WITHDRAWAL, TERHEQJE (incoming) | EXCLUDE -- pension withdrawal received | Not a contribution paid |

## Section 4 -- Worked examples

Six bank statement classifications and computations for a hypothetical Kosovan employer running monthly payroll (figures in EUR). All PIT figures use the monthly bands (0% up to 250, 8% on 250.01–450, 10% above 450). PIT is computed on GROSS wages — the conservative default; see Section 6 T2-1 on possible pension-deductibility.

### Example 1 -- Minimum-wage employee, single employer (BKT)

**Inputs:** Gross monthly wage EUR 350.00 (the 2025 minimum wage); this is the employee's only (primary) employer.

**Computation:**
- Monthly PIT: 0% on first 250.00 = 0.00; 8% on (350.00 − 250.00) = 8% × 100.00 = **EUR 8.00**.
- Employee pension 5% × 350.00 = **EUR 17.50** (withheld).
- Employer pension 5% × 350.00 = **EUR 17.50** (employer cost on top of wage).
- Net pay = 350.00 − 8.00 (PIT) − 17.50 (employee pension) = **EUR 324.50**.
- Total employer outlay = 350.00 + 17.50 = **EUR 367.50**.

**Bank lines:**
`05.02.2025 ; PAGA SHKURT - ARDIAN K. ; DEBIT ; NET PAY ; -324.50 ; EUR` → EXCLUDE (payroll, 3.4)
`14.02.2025 ; ATK - WM ; DEBIT ; TATIMI NE PAGA 01/2025 ; -8.00 ; EUR` → EXCLUDE (wage tax, 3.2)
`14.02.2025 ; TRUSTI - CM ; DEBIT ; KONTRIBUT PENSIONAL 01/2025 ; -35.00 ; EUR` → EXCLUDE (pension, 3.1). EUR 35.00 = 17.50 employee + 17.50 employer.

**Source:** PwC Kosovo PIT & Other taxes; EY (minimum wage EUR 350 eff. 1 Oct 2024).

### Example 2 -- Mid-range employee, single employer (ProCredit)

**Inputs:** Gross monthly wage EUR 600.00; primary (only) employer.

**Computation:**
- Monthly PIT: 0% on 250.00 = 0.00; 8% on (450.00 − 250.00) = 8% × 200.00 = 16.00; 10% on (600.00 − 450.00) = 10% × 150.00 = 15.00. Total PIT = 16.00 + 15.00 = **EUR 31.00**.
- Employee pension 5% × 600.00 = **EUR 30.00**.
- Employer pension 5% × 600.00 = **EUR 30.00**.
- Net pay = 600.00 − 31.00 − 30.00 = **EUR 539.00**.

> **Annual cross-check:** EUR 600 × 12 = 7,200. Annual PIT: 0 + 192.00 (band 2) + 10% × (7,200 − 5,400) = 192.00 + 180.00 = 372.00; ÷ 12 = **EUR 31.00/month**. Reconciles.

**Source:** PwC Kosovo PIT & Other taxes.

### Example 3 -- Higher earner, single employer (Raiffeisen)

**Inputs:** Gross monthly wage EUR 1,000.00; primary (only) employer.

**Computation:**
- Monthly PIT: 0% on 250.00 = 0.00; 8% × (450.00 − 250.00) = 16.00; 10% × (1,000.00 − 450.00) = 10% × 550.00 = 55.00. Total PIT = 16.00 + 55.00 = **EUR 71.00**.
- Employee pension 5% × 1,000.00 = **EUR 50.00**.
- Employer pension 5% × 1,000.00 = **EUR 50.00**.
- Net pay = 1,000.00 − 71.00 − 50.00 = **EUR 879.00**.
- Total employer outlay = 1,000.00 + 50.00 = **EUR 1,050.00**.

> **Annual cross-check:** EUR 1,000 × 12 = 12,000. Annual PIT: 0 + 192.00 + 10% × (12,000 − 5,400) = 192.00 + 660.00 = 852.00; ÷ 12 = **EUR 71.00**. Reconciles.

**Source:** PwC Kosovo PIT & Other taxes.

### Example 4 -- Employee with a SECONDARY employer (flat 10%)

**Inputs:** Employee already has a primary employer elsewhere. This (secondary) employer pays EUR 400.00/month for part-time work.

**Computation (secondary employer):**
- PIT: flat 10% on the full EUR 400.00 (no 0% band at a secondary employer) = **EUR 40.00**.
- Employee pension 5% × 400.00 = **EUR 20.00**.
- Employer pension 5% × 400.00 = **EUR 20.00**.
- Net from this employer = 400.00 − 40.00 − 20.00 = **EUR 340.00**.

> **Contrast:** had this been the primary employer, PIT would be 8% × (400.00 − 250.00) = **EUR 12.00**, not 40.00. The primary/secondary flag changes the tax by EUR 28.00/month here — hence R-XK-1.

**Source:** Lexology / TAK notice (secondary-employer flat 10%). *[RESEARCH GAP — reviewer to confirm against TAK PIT regulation text.]*

### Example 5 -- Benefit in kind above the EUR 65 threshold

**Inputs:** Gross cash wage EUR 600.00 plus a EUR 100.00/month gym membership benefit (not business travel, not work-accident indemnity, not transport reimbursement); primary employer.

**Computation:**
- Benefit in kind exceeds EUR 65/month, so the full EUR 100.00 is taxable employment income. Taxable wage base = 600.00 + 100.00 = **EUR 700.00**.
- Monthly PIT on 700.00: 0% on 250.00 = 0.00; 8% × 200.00 = 16.00; 10% × (700.00 − 450.00) = 10% × 250.00 = 25.00. Total PIT = **EUR 41.00**.
- Pension contributions are computed on gross wages — *[RESEARCH GAP: whether the taxable BIK enters the pension base is not confirmed; reviewer to verify. Conservatively computed on cash wage EUR 600.]* Employee pension 5% × 600.00 = **EUR 30.00**; employer pension 5% × 600.00 = **EUR 30.00**.

**Source:** PwC Kosovo — Income determination (EUR 65 BIK threshold); reimbursed business travel, work-accident indemnity and transport reimbursements excluded.

### Example 6 -- Ambiguous TAK debit (understatement / interest)

**Input line:**
`20.06.2025 ; ADMINISTRATA TATIMORE E KOSOVES ; DEBIT ; RREGULLIM/INTERES ; -640.00 ; EUR`

**Reasoning:** Matches "ADMINISTRATA TATIMORE" (3.2/3.3) but the reference "RREGULLIM/INTERES" (adjustment/interest) and the irregular amount suggest an understatement assessment (15%–25% of the under-declared amount) and/or late-payment interest, not a routine WM remittance. Cannot split principal from penalty/interest without a TAK statement.

**Classification:** EXCLUDE from VAT. Flag for reviewer — request the TAK statement to separate principal wage tax (a payroll cost) from penalty/interest (non-deductible). Escalate per R-XK-4.

**Source:** PwC Kosovo — Tax administration (penalties & interest).

## Section 5 -- Tier 1 rules

These rules apply when bank statement data is clear and all required inputs are available. Apply exactly as written. Citations in parentheses.

### Rule 1 -- Mandatory pension formula

- **Mandatory pension formula** — Employee pension = 5% × gross_wages   (withheld) Employer pension = 5% × gross_wages   (employer cost) Total pension    = 10% × gross_wages  → remitted to KPST/Trusti  _(Law No. 04/L-101; PwC Kosovo — Other taxes.)_

### Rule 2 -- No health, unemployment, or sickness payroll contribution

- **No health/unemployment/sickness contribution** — Health insurance (Law 04/L-249) is enacted but dormant — 0% collected. There is no separate unemployment, sickness, or general social-insurance payroll contribution. The basic state pension is budget-funded.  _(PwC Kosovo — Other taxes; GrECo/Asinta.)_

### Rule 3 -- PIT at the primary employer is progressive

- **PIT progressive bands formula** — 0%  on annual income up to EUR 3,000      (monthly up to EUR 250) 8%  on EUR 3,000.01 – 5,400               (monthly EUR 250.01 – 450) 10% on EUR 5,400.01 and above             (monthly EUR 450.01+)  _(Law No. 05/L-028 as amended; PwC Kosovo — Taxes on personal income.)_

### Rule 4 -- Current PIT schedule effective 23 August 2024

- **Current PIT schedule effective date** — The 0%/8%/10% structure was introduced by Law No. 08/L-142 (Official Gazette, effective 23 Aug 2024), replacing the former four-band 0%/4%/8%/10% schedule. For payroll periods before that date, the old schedule applied.  _(EY newsroom; Lexology.)_

### Rule 5 -- Secondary employer withholds flat 10%

- **Secondary employer flat 10%** — Where an employee has more than one employer, the primary employer applies the progressive bands and EACH secondary employer withholds a flat 10% on the wages it pays (no 0% band). Designating primary vs secondary is a legal obligation of the employee.  _(Lexology / TAK notice — *[RESEARCH GAP — reviewer to confirm against TAK regulation text]*.)_

### Rule 6 -- Employer withholds and remits

- **Employer withholds and remits** — The employer withholds PIT and the 5% employee pension contribution at the time of wage payment and remits both, together with the 5% employer pension share, to TAK by the 15th day of the following month.  _(PwC Kosovo — Tax administration.)_

### Rule 7 -- Benefits in kind over EUR 65/month are taxable

- **Benefit in kind threshold** — EUR 65/month EUR (Benefits in kind exceeding this monthly amount are taxable employment income. Reimbursement of business travel, work-accident indemnity, and transport-cost reimbursement are excluded.)  _(PwC Kosovo — Income determination.)_

### Rule 8 -- Voluntary additional pension

- **Voluntary additional pension** — Optional additional pension contributions are permitted: up to a further 15% by the employee and up to 15% by the employer (combined up to 30% above the mandatory 10%).  _(PwC Kosovo — Other taxes.)_

### Rule 9 -- Filing and payment schedule

**Filing and payment schedule table**  _(TAK CRM guidance portal; PwC Kosovo — Tax administration.)_

| Form | Purpose | Deadline |
| --- | --- | --- |
| WM | Wage withholding tax declaration (monthly) | 1st–15th of following month; pay by the 15th |
| CM | Pension contribution declaration & payment (monthly) | 1st–15th of following month |
| CI | Quarterly individual pension contribution report | 1st–15th of month after each quarter |
| PD / PD24 | Annual personal income tax return | 31 March of the following year |

### Rule 10 -- Residence basis

- **Residence basis** — Residents are taxed on worldwide income; non-residents only on Kosovo-source income.  _(PwC Kosovo — Taxes on personal income.)_

### Rule 11 -- New-employee reporting

- **New-employee reporting** — The employer must notify TAK of a new employee one day before that employee begins work.  _(PwC Kosovo — Tax administration.)_

### Rule 12 -- No statutory pension ceiling found

- **No pension ceiling found** — No maximum pensionable-wage ceiling on the 10% pension was found in the consulted sources; compute uncapped. *[RESEARCH GAP — reviewer to verify against Law 04/L-101 / KPST rules before relying on uncapped figures.]*  _(PwC Kosovo — Other taxes; caveat.)_

## Section 6 -- Tier 2 catalogue

When bank statement data is ambiguous or client circumstances are unclear, flag these for reviewer confirmation.

### T2-1 -- Is the employee pension deductible from the PIT base?

**Trigger:** computing PIT where the employee 5% pension is withheld.

**Issue:** The consulted sources state PIT is levied on gross wages but do not explicitly confirm whether the employee's 5% pension contribution is deductible from the PIT base. This skill computes PIT on the full gross wage (conservative — higher tax).

**Action:** Flag for reviewer. *[RESEARCH GAP — reviewer to confirm whether the 5% employee pension reduces the PIT base under Law 05/L-028.]*

### T2-2 -- High earner / pension ceiling

**Trigger:** gross wage high enough that an uncapped 10% pension is material.

**Issue:** No statutory maximum pensionable-wage ceiling was found. Uncapped computation may overstate the contribution if a cap exists.

**Action:** Flag for reviewer to verify Law 04/L-101 / KPST rules. *[RESEARCH GAP.]*

### T2-3 -- Primary vs secondary employer designation

**Trigger:** employee may have more than one employer; designation unclear or changed mid-period.

**Issue:** The progressive bands apply only at the primary employer; secondary employers withhold flat 10%. A wrong designation materially mis-states tax (see Example 4).

**Action:** STOP and confirm (R-XK-1). Flag any mid-period change of designation for reviewer.

### T2-4 -- Health-insurance regime status

**Trigger:** a new payroll period, or any client expectation that health contributions are due.

**Issue:** Law 04/L-249 is dormant but has repeatedly returned to the legislative agenda; it could commence.

**Action:** Confirm no mandatory health contribution has commenced for the relevant period before finalising. Flag for reviewer each new tax year.

### T2-5 -- Minimum wage in transition

**Trigger:** payroll period spanning a minimum-wage change date.

**Issue:** Minimum wage is EUR 350.00 in 2025, scheduled to rise to EUR 425.00 (1 Jan 2026) and EUR 500.00 (1 Jul 2026) per ministry/press reporting.

**Action:** Confirm the operative figure against the official Government Decision / Official Gazette for the period. Flag for reviewer.

### T2-6 -- Contractor vs employee classification

**Trigger:** payment to an individual that could be either employment or independent services.

**Issue:** Employment triggers 10% pension + wage withholding; independent services may fall under different rules. Mis-classification mis-states both contributions and tax.

**Action:** Flag for reviewer. Do not assume contractor status to avoid contributions.

### T2-7 -- Benefit-in-kind valuation

**Trigger:** non-cash benefits near or above the EUR 65/month threshold, or whether a BIK enters the pension base.

**Issue:** Valuation of BIKs and whether the taxable BIK is included in the pension base are not fully confirmed in the consulted sources.

**Action:** Flag for reviewer. *[RESEARCH GAP — pension base treatment of BIK.]*

## Section 7 -- Excel working paper template

When producing a Kosovo payroll/contribution computation, structure the working paper as follows:

```
KOSOVO PAYROLL & SOCIAL-CONTRIBUTION COMPUTATION -- WORKING PAPER
Employer: [name]            TAK fiscal no: [____]
Employee: [name]            Pay period:    [month/year]
Prepared: [date]

INPUT DATA
  Gross monthly wage (EUR):           [____]
  Figure is gross / net:              [GROSS / NET]
  Primary or secondary employer:      [PRIMARY / SECONDARY]   <- mandatory
  Benefits in kind > EUR 65/month:    [YES/NO]  amount: [____]
  Voluntary pension elected:          [YES/NO]  rates: [emp __% / empr __%]

PERSONAL INCOME TAX (monthly bands: 0% to 250 | 8% to 450 | 10% above)
  Taxable wage base (gross + taxable BIK):  EUR [____]
  IF PRIMARY:
    0% on first 250.00:                     EUR 0.00
    8% on (min(base,450) - 250):            EUR [____]
    10% on (base - 450, if > 450):          EUR [____]
    PIT total:                              EUR [____]
  IF SECONDARY:
    10% x base (flat, no 0% band):          EUR [____]

MANDATORY PENSION (KPST / Trusti)
  Employee 5% x gross:                      EUR [____]
  Employer 5% x gross:                      EUR [____]
  Total 10% x gross:                        EUR [____]
  [No statutory ceiling found — uncapped; RESEARCH GAP]

VOLUNTARY PENSION (optional, up to +15% / +15%)
  Employee voluntary:                       EUR [____]
  Employer voluntary:                       EUR [____]

NET PAY
  Net = gross - PIT - employee pension(s):  EUR [____]
  Total employer outlay = gross + employer pension(s): EUR [____]

FILING
  WM (wage tax) due:        15th of following month
  CM (pension) due:         15th of following month
  CI (quarterly):           1st-15th after quarter
  PD/PD24 (annual):         31 March following year

REVIEWER FLAGS
  [List any Tier 2 flags / RESEARCH GAP items here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their tax impact]
```

## Section 8 -- Bank statement reading guide

### How Kosovo payroll, tax and pension items appear on bank statements

**Currency:** EUR (Kosovo uses the euro unilaterally). Statements are commonly bilingual (Albanian / English); Serbian appears in some northern municipalities.

**Pension remittances (KPST / Trusti):**
- Descriptions: "TRUSTI", "KPST", "FONDI I KURSIMEVE PENSIONALE", "KONTRIBUT PENSIONAL", "CM".
- Timing: monthly, by the 15th of the following month.
- Amount: 10% of gross payroll (5% employee + 5% employer); always outgoing (DEBIT).

**Wage withholding tax (TAK / ATK):**
- Descriptions: "TAK", "ATK", "ADMINISTRATA TATIMORE", "TATIMI NE PAGA", "MBAJTJE NE BURIM", "WM".
- Timing: monthly, by the 15th of the following month.
- Amount: per the progressive bands (primary) or flat 10% (secondary).

**Salary (PAGA):**
- "PAGA", "PAGAT", "ROGA", "NET PAY" — outgoing net wages to employees. Not a contribution.

**Key identification tips:**
1. Pension and wage-tax remittances are always outgoing (DEBIT), recur monthly, and cluster around the 15th.
2. A pension remittance equal to exactly 10% of total gross payroll for the month is the mandatory KPST contribution.
3. Do NOT confuse "TATIMI NE PAGA" (wage tax → TAK) with "KONTRIBUT PENSIONAL" (pension → Trusti) — they are separate forms (WM vs CM).
4. Incoming "PENSIONI BAZIK" / "BASIC PENSION" or "TRUSTI" withdrawals are benefits received, not contributions.
5. Irregular TAK debits referencing "INTERES" or "RREGULLIM" may be interest/penalties — flag for reviewer.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for remittances** -- identify outgoing payments matching Section 3 (Trusti/KPST pension; TAK/ATK wage tax; PAGA salary).
2. **Reconstruct gross payroll** -- a pension remittance is 10% of gross payroll, so estimated monthly gross payroll ≈ pension remittance ÷ 0.10.
3. **Cross-check wage tax** -- the WM remittance should be consistent with the progressive bands on that gross (primary) or flat 10% (secondary).
4. **Flag the unknowns** -- "Computation derived from bank statement amounts only. Primary/secondary employer status, gross-vs-net basis, benefits in kind, and any pension ceiling have NOT been independently verified. Health-insurance regime assumed dormant. Reviewer must confirm before filing WM/CM/PD."

### Quick computation table (single primary employer, 2025 bands, PIT on gross)

**Quick computation table (single primary employer, 2025 bands, PIT on gross)**  _(PwC Kosovo — Taxes on personal income & Other taxes.)_

| Gross/month | Monthly PIT | Employee pension 5% | Employer pension 5% | Net pay |
| --- | --- | --- | --- | --- |
| EUR 250.00 | EUR 0.00 | EUR 12.50 | EUR 12.50 | EUR 237.50 |
| EUR 350.00 (min wage) | EUR 8.00 | EUR 17.50 | EUR 17.50 | EUR 324.50 |
| EUR 450.00 | EUR 16.00 | EUR 22.50 | EUR 22.50 | EUR 411.50 |
| EUR 600.00 | EUR 31.00 | EUR 30.00 | EUR 30.00 | EUR 539.00 |
| EUR 1,000.00 | EUR 71.00 | EUR 50.00 | EUR 50.00 | EUR 879.00 |

> **Arithmetic checks (PIT on gross; net = gross − PIT − employee pension):**
> - 250: PIT 0; net = 250 − 0 − 12.50 = 237.50 ✓
> - 350: PIT = 8% × 100 = 8.00; net = 350 − 8.00 − 17.50 = 324.50 ✓
> - 450: PIT = 8% × 200 = 16.00; net = 450 − 16.00 − 22.50 = 411.50 ✓
> - 600: PIT = 16.00 + 10% × 150 = 31.00; net = 600 − 31.00 − 30.00 = 539.00 ✓
> - 1,000: PIT = 16.00 + 10% × 550 = 71.00; net = 1,000 − 71.00 − 50.00 = 879.00 ✓
>
> **Source:** PwC Kosovo — Taxes on personal income & Other taxes.

### Thresholds and key figures

**Thresholds and key figures**  _(PwC Kosovo — Taxes on personal income; PwC Kosovo — Other taxes; Law 04/L-101; GrECo/Asinta; PwC Kosovo — Income determination; EY newsroom; PwC Kosovo — Taxes on corporate income; PwC/Law 04/L-101 (caveat))_

| Item | Value | Source |
| --- | --- | --- |
| PIT zero-rate threshold | EUR 3,000/year (EUR 250/month) | PwC Kosovo — Taxes on personal income |
| 8% band | EUR 3,000.01 – 5,400/year | PwC Kosovo — Taxes on personal income |
| 10% band | EUR 5,400.01+/year | PwC Kosovo — Taxes on personal income |
| Mandatory pension | 10% (5% employee + 5% employer) | PwC Kosovo — Other taxes; Law 04/L-101 |
| Voluntary pension | up to +15% employee / +15% employer | PwC Kosovo — Other taxes |
| Health insurance | 0% (Law 04/L-249 dormant) | GrECo/Asinta |
| Taxable BIK threshold | EUR 65/month | PwC Kosovo — Income determination |
| Minimum wage (2025) | EUR 350.00/month gross | EY newsroom (eff. 1 Oct 2024) |
| Minimum wage (from 1 Jan 2026) | EUR 425.00/month | EY newsroom |
| Minimum wage (from 1 Jul 2026) | EUR 500.00/month | EY newsroom |
| Small business CIT exemption | gross income up to EUR 30,000 (turnover tax instead: 3%/9%/10%, min EUR 37.50) | PwC Kosovo — Taxes on corporate income |
| Standard CIT rate | 10% | PwC Kosovo — Taxes on corporate income |
| Pension contribution ceiling | none found *[RESEARCH GAP — reviewer to confirm]* | PwC/Law 04/L-101 (caveat) |

### Penalties

**Penalties**  _(PwC Kosovo — Tax administration)_

| Penalty | Amount | Source |
| --- | --- | --- |
| Understatement of tax | 15%–25% of the under-declared amount (by size of understatement) | PwC Kosovo — Tax administration |
| Late-payment interest | Monthly interest, set at least annually above the commercial bank lending rate; accrues up to 10 years from due date | PwC Kosovo — Tax administration |

### Albanian-language glossary

**Albanian-language glossary**

| Albanian | English |
| --- | --- |
| Paga / Pagat | Wage / wages |
| Tatimi në paga | Tax on wages |
| Mbajtje në burim | Withholding at source |
| Kontribut pensional | Pension contribution |
| Fondi i Kursimeve Pensionale | Pension Savings Fund (Trusti/KPST) |
| Administrata Tatimore e Kosovës (ATK) | Tax Administration of Kosovo (TAK) |
| Pensioni bazik | Basic (state) pension |
| Rregullim / Interes | Adjustment / interest |

### Test suite

**Test 1:** Single (primary) employer, gross EUR 250.00/month. → PIT EUR 0.00; employee pension EUR 12.50; employer pension EUR 12.50; net EUR 237.50.

**Test 2:** Single employer, gross EUR 350.00 (min wage). → PIT 8% × 100 = EUR 8.00; employee pension EUR 17.50; net EUR 324.50; employer outlay EUR 367.50.

**Test 3:** Single employer, gross EUR 600.00. → PIT EUR 31.00 (16.00 + 15.00); employee pension EUR 30.00; employer pension EUR 30.00; net EUR 539.00.

**Test 4:** Single employer, gross EUR 1,000.00. → PIT EUR 71.00 (16.00 + 55.00); employee pension EUR 50.00; net EUR 879.00; employer outlay EUR 1,050.00.

**Test 5:** SECONDARY employer, gross EUR 400.00. → PIT flat 10% = EUR 40.00; employee pension EUR 20.00; net EUR 340.00. (Had it been primary: PIT 8% × 150 = EUR 12.00.)

**Test 6:** Gross EUR 600.00 + taxable BIK EUR 100.00 (over EUR 65), primary. → PIT base EUR 700.00; PIT = 16.00 + 10% × 250 = EUR 41.00. Pension on cash wage EUR 600 = EUR 30.00 each side *[BIK-in-base RESEARCH GAP]*.

**Test 7:** Client asks for the Kosovo health-insurance contribution. → EUR 0.00; Law 04/L-249 dormant; no contribution collected (R-XK-2).

**Test 8:** Annual cross-check, gross EUR 1,000/month = EUR 12,000/year. → Annual PIT = 0 + 192.00 + 10% × (12,000 − 5,400) = EUR 852.00; ÷ 12 = EUR 71.00/month (matches Test 4).

### Prohibitions

- **Confirm employer status before computing wage tax** — NEVER compute Kosovo wage tax without confirming PRIMARY vs SECONDARY employer — bands vs flat 10% depend on it.
- **No health-insurance contribution** — NEVER add a health-insurance contribution — Law 04/L-249 is dormant; 0% is collected.
- **No invented social-insurance contributions** — NEVER invent an unemployment, sickness, or general social-insurance payroll contribution — none exists beyond pension.
- **No unsourced pension ceiling** — NEVER apply a pension ceiling that is not in the source material — none was found; mark uncapped figures with the RESEARCH GAP and flag for reviewer.
- **Do not apply old PIT schedule after 23 Aug 2024** — NEVER apply the old 0%/4%/8%/10% schedule to periods on/after 23 Aug 2024 — the current schedule is 0%/8%/10%.
- **Escalate arrears/penalties without TAK statement** — NEVER quantify pension/wage-tax arrears or penalties without a TAK statement — escalate (R-XK-4).
- **Do not confuse wage tax and pension contribution** — NEVER confuse "TATIMI NE PAGA" (wage tax → TAK, form WM) with "KONTRIBUT PENSIONAL" (pension → Trusti, form CM).
- **Do not treat Trusti withdrawals as contributions paid** — NEVER treat incoming "PENSIONI BAZIK" / Trusti withdrawals as contributions paid.
- **Label outputs as estimated (Tier 2)** — NEVER present figures as definitive — this skill is Tier 2 (`verified_by: pending`); label outputs as estimated and direct the client to TAK/KPST statements.
- **Surface research gaps to reviewer** — NEVER silently resolve a `[RESEARCH GAP]` item — surface it to the reviewer.

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
