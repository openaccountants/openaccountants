---
name: albania-social-contributions
description: Use this skill whenever asked about Albania social security and health insurance contributions for employees, employers, or the self-employed. Trigger on phrases like "how much social insurance do I pay in Albania", "Albanian payroll contributions", "sigurime shoqerore", "sigurime shendetesore", "social insurance rate Albania", "health insurance contribution Albania", "employer contribution Albania", "self-employed social insurance Albania", "Listepagesa", "E-SIG payroll declaration", "minimum contribution base", "maximum contribution base", "ALL 40,000 minimum wage", "ALL 50,000 minimum wage 2026", or any question about Albanian social/health contribution obligations for a client. Also trigger when classifying Albanian bank-statement lines that relate to DPT (tatime) payroll-tax debits, social/health insurance remittances, or government contribution payments from BKT, Raiffeisen Bank Albania, Credins, Intesa Sanpaolo Bank Albania, or other Albanian banks. This skill covers employee/employer social (9.5%/15%) and health (1.7%/1.7%) rates, the min/max contribution base, self-employed rates (23% social / 3.4% health), the 2026 base changes, the 20th-of-month declaration deadline, bank-statement classification patterns, and edge cases. This skill is scoped to social-security and health contributions; personal income tax (PIT) is covered only as context. ALWAYS read this skill before touching any Albanian contribution work.
version: 0.1
jurisdiction: AL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Albania Social Security & Health Insurance Contributions

## Albania Social Security & Health Insurance Contributions Skill v0.1

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Albania (Republic of Albania) |
| Currency | ALL (Albanian lek) -- only |
| Primary Legislation | Law No. 7703 dated 11.05.1993 "On Social Insurance in the Republic of Albania" (as amended) |
| Supporting Legislation | Law No. 10383 dated 24.02.2011 "On Compulsory Health Care Insurance"; Law No. 29/2023 "On Income Tax" (PIT, effective 1 Jan 2024); DCM (VKM) No. 776 dated 19.12.2025 (minimum wage from 1 Jan 2026) |
| Tax Authority (collection) | General Directorate of Taxation -- Drejtoria e Pergjithshme e Tatimeve (DPT), tatime.gov.al |
| Benefits administrator | Social Insurance Institute -- Instituti i Sigurimeve Shoqerore (ISSH) |
| Filing portal | e-Filing / e-Albania |
| Employee social insurance rate | 9.5% of gross salary (bounded by min/max base) [PwC, reviewed Feb 2026] |
| Employer social insurance rate | 15% of gross salary (bounded by min/max base) [PwC] |
| Employee health insurance rate | 1.7% of gross salary (no ceiling; floored at min base) [PwC] |
| Employer health insurance rate | 1.7% of gross salary (no ceiling; floored at min base) [PwC] |
| Employee total | 11.2% of gross salary [PwC] |
| Employer total | 16.7% of gross salary [PwC] |
| Combined employer + employee | 27.9% of gross salary [PwC] |
| Minimum contribution base (2025) | ALL 40,000/month [HLB Albania] |
| Maximum social-insurance base (2025) | ALL 176,416/month [HLB Albania] |
| Minimum contribution base (2026) | ALL 50,000/month from 1 Jan 2026 [PwC significant developments] |
| Maximum social-insurance base (2026) | ALL 186,416/month from 1 Jan 2026 [PwC + HLB] -- DISPUTED, see caveats |
| Self-employed social insurance | 23% on a base >= minimum salary [PwC] |
| Self-employed health insurance | 3.4% on a base >= double the minimum salary [PwC] |
| Declaration/payment deadline | Electronically by the 20th of the following month [PwC] |
| Validated by | Pending -- requires sign-off by an Albanian licensed accountant |
| Validation date | Pending |

**Rate overview (employment)**  _([PwC Albania -- Other taxes])_

| Component | Employee | Employer | Combined |
| --- | --- | --- | --- |
| Social insurance (pension/disability/maternity) | 9.5% | 15% | 24.5% |
| Health insurance | 1.7% | 1.7% | 3.4% |
| **Total** | **11.2%** | **16.7%** | **27.9%** |

*Arithmetic check: employee 9.5 + 1.7 = 11.2; employer 15 + 1.7 = 16.7; combined 24.5 + 3.4 = 27.9 = 11.2 + 16.7. All reconcile. Source: [PwC Albania -- Other taxes].*

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Period unknown but on/before 31 Dec 2025 | Use 2025 bases (min ALL 40,000 / max ALL 176,416) |
| Period on/after 1 Jan 2026 | Use 2026 bases (min ALL 50,000 / max ALL 186,416), flag for reviewer |
| 2026 maximum base disputed | Use PwC/HLB ALL 186,416; flag for reviewer to confirm vs DCM No. 776 |
| Salary below minimum base | Assess contributions on the minimum base, NOT the lower actual salary |
| Salary above social ceiling | Cap the 9.5%/15% social components at the ceiling; health (1.7%/1.7%) has NO ceiling |
| Unknown employment status | Ask -- do not assume employee vs self-employed |
| Unknown form code (Listepagesa / E-SIG 025) | Use E-SIG 025 payroll list; flag to confirm with e-Filing portal |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — Employment status (employee vs self-employed) and gross monthly salary (or self-employed base reference). Without employment status, STOP.
- **Recommended inputs** — The period/month being computed (to select 2025 vs 2026 bases), and whether the salary is below the minimum base or above the social ceiling.
- **Ideal inputs** — The monthly payroll declaration (Listepagesa / E-SIG 025), bank statements showing DPT contribution remittances, and the DPT/e-Albania account confirming the applicable contribution bases.

### Refusal catalogue

- **R-AL-SSC-1 -- Employment status unknown** — Trigger: not stated whether the person is an employee or self-employed. Message: "Employment status is mandatory. Employees pay 11.2% (employee) with the employer paying 16.7%; the self-employed pay 23% social on the minimum base plus 3.4% health on double the minimum base. Cannot proceed without this."
- **R-AL-SSC-2 -- 2026 maximum base relied upon for a high earner** — Trigger: salary above ALL 186,416/month in a 2026 period AND the result is being relied upon for filing. Message: "The 2026 maximum social-insurance base is DISPUTED across sources (PwC/HLB say ALL 186,416; one firm summary of DCM No. 776 says ALL 220,520). Do not file a high-earner 2026 computation without confirming the ceiling against the published DCM No. 776 / Official Gazette. Escalate to an Albanian licensed accountant."
- **R-AL-SSC-3 -- Penalty / late-payment quantification** — Trigger: client asks for the exact late-filing or late-payment penalty. Message: "Exact penalty amounts and interest rates under Law No. 9920/2008 (Tax Procedures) were not confirmed from an authoritative primary source in this skill [RESEARCH GAP -- reviewer to confirm]. Do not quantify penalties. Escalate to an Albanian licensed accountant."
- **R-AL-SSC-4 -- Personal income tax (PIT) computation** — Trigger: client asks for the PIT (income tax) due, not contributions. Message: "This skill covers social-security and health contributions only. Albanian PIT monthly bands conflict across sources (tax-free portion variously reported as ALL 30,000-50,000) [RESEARCH GAP]. Verify monthly PIT bands with the DPT before computing PIT; use a dedicated PIT skill."
- **R-AL-SSC-5 -- Expat / posted-worker / A1-equivalent coverage** — Trigger: cross-border posting, totalization, or treaty coverage question. Message: "Cross-border social-security coordination (posted workers, totalization agreements) is outside the scope of this skill. Escalate to an Albanian licensed accountant."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for Albanian bank-statement transactions related to contributions. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Contribution remittances EXCLUDE from any VAT return or revenue classification -- they are statutory payroll/personal obligations, not business supplies. Employer contributions are a payroll cost; employee contributions and PIT are withheld from gross pay.

### 3.1 DPT / tax-authority contribution remittances

**DPT / tax-authority contribution remittances pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DPT, TATIME, DREJTORIA E PERGJITHSHME E TATIMEVE | EXCLUDE -- contribution/PIT remittance | Monthly payroll remittance to the tax authority |
| SIGURIME SHOQERORE | EXCLUDE -- social insurance contribution | "Social insurance" in Albanian |
| SIGURIME SHENDETESORE | EXCLUDE -- health insurance contribution | "Health insurance" in Albanian |
| KONTRIBUTE, KONTRIBUTI | EXCLUDE -- contributions | Generic "contributions" reference |
| LISTEPAGESA, E-SIG, E-SIG 025 | EXCLUDE -- payroll declaration payment | Payment tied to the monthly payroll list |
| ISSH, SIGURIMET SHOQERORE | EXCLUDE -- social insurance | ISSH = benefits administrator reference |

### 3.2 Contribution debits appearing on specific Albanian banks

**Contribution debits by bank table**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| BKT (Banka Kombetare Tregtare) | "DPT" / "TATIME" / "SIGURIME SHOQERORE" | EXCLUDE -- contribution remittance |
| Raiffeisen Bank Albania | "DREJTORIA E TATIMEVE" / "KONTRIBUTE" | EXCLUDE -- contribution remittance |
| Credins Bank | "TATIME" / "SIGURIME" | EXCLUDE -- contribution remittance |
| Intesa Sanpaolo Bank Albania | "DPT KONTRIBUTE" / "SIGURIME SHENDETESORE" | EXCLUDE -- contribution remittance |
| Banka e Tiranes / Tirana Bank | "TATIME / SIGURIME" | EXCLUDE -- contribution remittance |

### 3.3 PIT (income tax) remittances -- exclude, but NOT a contribution

**PIT remittances pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TATIMI MBI TE ARDHURAT, TAP | EXCLUDE -- personal income tax | PIT withheld from salary, not a social contribution |
| DIVA | EXCLUDE -- annual income declaration payment | Annual PIT reconciliation, not a contribution |

### 3.4 Salary / payroll (exclude from contribution classification)

**Salary/payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PAGA, PAGAT, RROGA (outgoing) | EXCLUDE -- payroll expense | Net salary paid to employee, not a contribution |
| PAGA (incoming) | EXCLUDE -- employment income received | Not a contribution payment |

### 3.5 Benefits received (not contributions)

**Benefits received pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION, PENSIONI (incoming) | EXCLUDE -- pension income received | ISSH benefit, not a contribution paid |
| RAPORT MJEKESOR, BARRELINDJE (incoming) | EXCLUDE -- sickness/maternity benefit received | Not a contribution paid |

## Section 4 -- Worked examples

Six bank-statement classifications and computations for a hypothetical Albanian small business and its staff. All figures in ALL. Rates: 2025 unless stated.

### Example 1 -- Standard salary within bounds (2025)

**Scenario:** Employee on gross ALL 100,000/month (between the ALL 40,000 floor and ALL 176,416 ceiling).

**Reasoning:**
- Social base = 100,000 (within bounds). Employee social 9.5% = 9,500; employer social 15% = 15,000.
- Health base = 100,000 (no ceiling). Employee health 1.7% = 1,700; employer health 1.7% = 1,700.
- Employee total = 9,500 + 1,700 = **11,200** (= 11.2% of 100,000 ✓).
- Employer total = 15,000 + 1,700 = **16,700** (= 16.7% of 100,000 ✓).
- Combined = 11,200 + 16,700 = 27,900 (= 27.9% ✓).

**Bank line:** `20.02.2025 ; DPT KONTRIBUTE ; DEBIT ; SIGURIME 01/2025 ; -27,900 ; ALL`
**Classification:** EXCLUDE -- combined employer+employee contribution remittance (Section 3.1). Source: [PwC Albania -- Other taxes].

### Example 2 -- High earner above the social ceiling (2025)

**Scenario:** Employee on gross ALL 250,000/month (above the ALL 176,416 social ceiling).

**Reasoning:**
- Social base CAPPED at 176,416. Employee social 9.5% = 176,416 x 0.095 = **16,759.52**; employer social 15% = 176,416 x 0.15 = **26,462.40**.
- Health has NO ceiling, so health base = full 250,000. Employee health 1.7% = 4,250; employer health 1.7% = 4,250.
- Employee total = 16,759.52 + 4,250 = **21,009.52**.
- Employer total = 26,462.40 + 4,250 = **30,712.40**.

**Note:** Because social is capped but health is not, the employee total (21,009.52) is LESS than 11.2% of 250,000 (= 28,000). The cap only bites the social component. Source: [PwC; HLB Albania for the ALL 176,416 ceiling].

### Example 3 -- Salary below the minimum base (2025)

**Scenario:** Part-time/low-wage employee on gross ALL 30,000/month (below the ALL 40,000 floor).

**Reasoning:**
- Contributions are assessed on the MINIMUM base (40,000), not the lower actual 30,000 (conservative default; Tier 1 Rule 4).
- Social: employee 40,000 x 0.095 = 3,800; employer 40,000 x 0.15 = 6,000.
- Health: employee 40,000 x 0.017 = 680; employer 40,000 x 0.017 = 680.
- Employee total = 3,800 + 680 = **4,480**; employer total = 6,000 + 680 = **6,680**.

**Classification note:** Flag for reviewer -- confirm the employee is genuinely on a sub-minimum gross (e.g., legitimate part-time below the floor) versus an underdeclaration. Source: [HLB Albania for the ALL 40,000 floor].

### Example 4 -- Self-employed individual (2025)

**Scenario:** Self-employed (private) individual, 2025.

**Reasoning:**
- Social insurance: 23% on a base of at least the minimum salary (ALL 40,000) = 40,000 x 0.23 = **9,200/month**.
- Health insurance: 3.4% on a base of at least double the minimum salary (ALL 80,000) = 80,000 x 0.034 = **2,720/month**.
- Total self-employed contribution = 9,200 + 2,720 = **11,920/month**.

**Bank line:** `20.05.2025 ; TATIME ; DEBIT ; KONTRIBUTE I VETEPUNESUAR ; -11,920 ; ALL`
**Classification:** EXCLUDE -- self-employed contribution remittance (Section 3.1). Source: [PwC Albania -- Other taxes].

### Example 5 -- High earner above the social ceiling (2026)

**Scenario:** Employee on gross ALL 250,000/month in a 2026 period (social ceiling ALL 186,416 per PwC/HLB).

**Reasoning:**
- Social base CAPPED at 186,416. Employee social 9.5% = 186,416 x 0.095 = **17,709.52**; employer social 15% = 186,416 x 0.15 = **27,962.40**.
- Health (no ceiling) on full 250,000: employee 4,250; employer 4,250.
- Employee total = 17,709.52 + 4,250 = **21,959.52**; employer total = 27,962.40 + 4,250 = **32,212.40**.

**WARNING:** The 2026 maximum base of ALL 186,416 is DISPUTED (one source states ALL 220,520). Do NOT file this high-earner 2026 computation without confirming the ceiling against the published DCM No. 776 / Official Gazette (Refusal R-AL-SSC-2). Source: [PwC significant developments; HLB Albania].

### Example 6 -- Ambiguous DPT debit (contributions + PIT combined)

**Input line:**
`20.03.2025 ; DREJTORIA E TATIMEVE ; DEBIT ; PAGESA 02/2025 ; -45,000 ; ALL`

**Reasoning:**
Matches "DREJTORIA E TATIMEVE" (Section 3.2, Raiffeisen). A single monthly remittance to the DPT can bundle (a) withheld employee PIT, (b) employee social + health contributions, and (c) employer social + health contributions. The amount cannot be split into PIT vs contributions from the bank line alone -- the payroll declaration (Listepagesa / E-SIG 025) is needed.

**Classification:** EXCLUDE from VAT. Flag for reviewer -- request the E-SIG 025 payroll list to split PIT from social/health contributions. Source: [PwC -- employer withholds and remits PIT + contributions together].

## Section 5 -- Tier 1 rules

These rules apply when payroll data is clear and all required inputs are available. Apply exactly as written. All figures are sourced; any gap is marked.

### Rule 1 -- Employment contribution formulae

- **Employment contribution formulae** — employee_social   = clamp(gross, min_base, social_ceiling) x 9.5% employer_social   = clamp(gross, min_base, social_ceiling) x 15% employee_health   = max(gross, min_base)                   x 1.7%   # NO ceiling employer_health   = max(gross, min_base)                   x 1.7%   # NO ceiling employee_total    = employee_social + employee_health   (= 11.2% within bounds) employer_total    = employer_social + employer_health   (= 16.7% within bounds)  _([PwC Albania -- Other taxes])_

### Rule 2 -- Contribution bases (2025)

- **Contribution bases (2025)** — Minimum base = ALL 40,000/month; maximum social-insurance base = ALL 176,416/month. Apply for any period through 31 December 2025.  _([HLB Albania])_

### Rule 3 -- Contribution bases (2026)

- **Contribution bases (2026)** — From 1 January 2026: minimum base = ALL 50,000/month; maximum social-insurance base = ALL 186,416/month. The 2026 maximum is DISPUTED -- one firm summary of DCM No. 776 states ALL 220,520; use ALL 186,416 and flag (Conservative default; Refusal R-AL-SSC-2).  _([PwC significant developments; HLB Albania])_

### Rule 4 -- Salary below the minimum base is grossed up to the minimum base

- **Sub-minimum gross treatment** — Contributions are assessed on the minimum base, not the lower actual salary. A sub-minimum gross still attracts contributions on ALL 40,000 (2025) / ALL 50,000 (2026).  _([conservative default, corroborated by min-base rule])_

### Rule 5 -- Health insurance has NO ceiling

- **Health insurance ceiling rule** — The 1.7% employee and 1.7% employer health contributions are assessed on full gross salary, floored at the minimum base only. The maximum (ceiling) applies ONLY to the 9.5%/15% social-insurance components.  _([tax-checker / TPA; PwC])_

### Rule 6 -- Self-employed social insurance

- **Self-employed social insurance rate** — 23% on a base of at least the minimum salary (ALL 40,000 in 2025; ALL 50,000 in 2026)  _([PwC])_

### Rule 7 -- Self-employed health insurance

- **Self-employed health insurance rate** — 3.4% on a base of at least double the minimum salary (ALL 80,000 in 2025; ALL 100,000 in 2026)  _([PwC])_

### Rule 8 -- Withholding and remittance

- **Withholding and remittance** — The employer withholds employee PIT plus employee social + health contributions and remits them together with the employer social + health contributions each month.  _([PwC])_

### Rule 9 -- Declaration and payment deadline

- **Declaration and payment deadline** — The monthly payroll declaration (Listepagesa / E-SIG 025), PIT, and social/health contributions must be filed and paid electronically by the 20th day of the following month.  _([PwC])_

### Rule 10 -- PIT is separate from contributions

- **PIT separation rule** — Employment-income PIT is progressive (13% and 23% with a tax-free portion) under Law No. 29/2023, effective 1 Jan 2024. It is NOT a social contribution. The monthly PIT bands conflict across sources [RESEARCH GAP -- reviewer to confirm] -- do not compute PIT in this skill.  _([PwC])_

## Section 6 -- Tier 2 catalogue

When payroll data is ambiguous or client circumstances are unclear, flag these for reviewer confirmation.

### T2-1 -- 2026 high-earner maximum base

- **T2-1 -- 2026 high-earner maximum base** — Trigger: Salary above ALL 186,416/month in a 2026 period. Issue: The 2026 social-insurance ceiling is disputed (PwC/HLB ALL 186,416 vs ARS summary ALL 220,520). The two cannot both be correct. Action: Use ALL 186,416 and flag; do not file without confirming against DCM No. 776 / Official Gazette.

### T2-2 -- Sub-minimum gross salary

- **T2-2 -- Sub-minimum gross salary** — Trigger: Stated gross is below the minimum contribution base. Issue: Contributions must be grossed up to the minimum base; a genuinely sub-minimum gross is unusual and may indicate part-time arrangements, underdeclaration, or a data error. Action: Confirm the actual gross and the basis (Rule 4) with the reviewer.

### T2-3 -- Mixed employment and self-employment

- **T2-3 -- Mixed employment and self-employment** — Trigger: Individual is both employed and self-employed. Issue: Interaction of the employee (11.2%) and self-employed (23% / 3.4%) regimes, and whether minimum bases overlap, is not fully specified in this research. Action: Flag for reviewer; do not net the two regimes without confirmation. [RESEARCH GAP -- reviewer to confirm overlap rules.]

### T2-4 -- Contribution arrears / late-payment penalties

- **T2-4 -- Contribution arrears / late-payment penalties** — Trigger: Unpaid contributions from prior months/years. Issue: Penalty and interest figures under Law No. 9920/2008 were not confirmed from an authoritative source [RESEARCH GAP]. Action: Do not quantify. Escalate to an Albanian licensed accountant (Refusal R-AL-SSC-3).

### T2-5 -- Undeclared work / unregistered employees

- **T2-5 -- Undeclared work / unregistered employees** — Trigger: Workers not on the payroll declaration. Issue: Significant fines apply for undeclared work; the exact figure is not confirmed here [RESEARCH GAP]. Action: Flag for reviewer; do not estimate the fine.

### T2-6 -- Bundled DPT remittance (PIT + contributions)

- **T2-6 -- Bundled DPT remittance (PIT + contributions)** — Trigger: A single DPT debit covers PIT and contributions together. Issue: The bank line cannot be split without the E-SIG 025 payroll list. Action: Request the payroll declaration; flag for reviewer (see Example 6).

## Section 7 -- Excel working paper template

When producing an Albanian contribution computation, structure the working paper as follows:

```
ALBANIA CONTRIBUTIONS COMPUTATION -- WORKING PAPER
Client: [name]
Period (month/year): [____]   Base set: [2025 / 2026]
Prepared: [date]

INPUT DATA
  Employment status:             [Employee / Self-employed]
  Gross monthly salary (ALL):    [____]
  Minimum base (ALL):            [40,000 (2025) / 50,000 (2026)]
  Social ceiling (ALL):          [176,416 (2025) / 186,416 (2026) -- DISPUTED 2026]

EMPLOYEE COMPUTATION (if employee)
  Social base = clamp(gross, min, ceiling): ALL [____]
  Employee social  (x 9.5%):     ALL [____]
  Employer social  (x 15%):      ALL [____]
  Health base = max(gross, min) [NO ceiling]: ALL [____]
  Employee health  (x 1.7%):     ALL [____]
  Employer health  (x 1.7%):     ALL [____]
  Employee TOTAL  (= 11.2% in-bounds): ALL [____]
  Employer TOTAL  (= 16.7% in-bounds): ALL [____]
  Combined TOTAL  (= 27.9% in-bounds): ALL [____]

SELF-EMPLOYED COMPUTATION (if self-employed)
  Social base (>= min salary):   ALL [____]
  Social (x 23%):                ALL [____]
  Health base (>= 2 x min salary): ALL [____]
  Health (x 3.4%):               ALL [____]
  Self-employed TOTAL:           ALL [____]

REMITTANCE
  Declaration form: Listepagesa / E-SIG 025
  Deadline:         20th of following month
  PIT withheld (separate -- not in this skill): ALL [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How contribution remittances appear on Albanian bank statements

**BKT (Banka Kombetare Tregtare):**
- Description: "DPT", "TATIME", "SIGURIME SHOQERORE"
- Timing: By the 20th of the month following the payroll month
- Amount: Combined employer + employee contributions (and often PIT bundled)

**Raiffeisen Bank Albania:**
- Description: "DREJTORIA E TATIMEVE", "KONTRIBUTE"
- Timing: Same monthly cycle

**Credins Bank / Intesa Sanpaolo Bank Albania:**
- Description: "TATIME", "SIGURIME", "DPT KONTRIBUTE", "SIGURIME SHENDETESORE"
- Timing: Same monthly cycle

**Albanian-language terms to recognise:**
- "Sigurime shoqerore" = social insurance contributions
- "Sigurime shendetesore" = health insurance contributions
- "Kontribute" = contributions
- "Listepagesa" = the monthly payroll list/declaration
- "Tatim mbi te ardhurat / TAP" = personal income tax (NOT a contribution)
- "Paga / rroga" = salary/wage
- "Pension / pensioni" = pension (benefit received, not a contribution)

**Key identification tips:**
1. Contribution remittances are always outgoing (DEBIT) to the DPT/tatime.
2. They recur monthly, due by the 20th of the following month.
3. A single DPT debit may bundle PIT + employee contributions + employer contributions -- request the E-SIG 025 list to split.
4. Do not confuse outbound DPT debits (contributions/PIT paid) with inbound pension/sickness/maternity credits (benefits received).
5. Within bounds, employee total = 11.2% and employer total = 16.7% of gross; above the social ceiling the social component caps but health does not.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for DPT/tatime debits** -- identify all outgoing payments matching Section 3 patterns.
2. **Group by month** -- contributions are monthly, due by the 20th of the following month.
3. **Estimate the gross from the contribution** (within bounds, employer+employee combined = 27.9% of gross):
   - Implied gross ~= combined remittance / 0.279 (only valid if no PIT is bundled and salary is within bounds). Treat as a rough estimate only.
4. **Flag the floor/ceiling:**
   - If the combined remittance is small, the salary may be at/below the minimum base (ALL 40,000 in 2025 / ALL 50,000 in 2026).
   - If large, the social component may be capped at the ceiling (ALL 176,416 in 2025 / ALL 186,416 in 2026).
5. **Flag for reviewer:** "Contribution classification derived from bank-statement amounts only. Gross salary, period (2025 vs 2026 bases), and whether PIT is bundled have not been independently verified. Reviewer must confirm against the E-SIG 025 payroll list before filing."

### Contribution rates (2025) -- with provenance

**Contribution rates (2025) -- with provenance**  _([PwC Albania -- Other taxes]; [PwC])_

| Component | Employee | Employer | Source |
| --- | --- | --- | --- |
| Social insurance | 9.5% | 15% | [PwC Albania -- Other taxes] |
| Health insurance | 1.7% | 1.7% | [PwC Albania -- Other taxes] |
| **Total** | **11.2%** | **16.7%** | [PwC] |
| **Combined** | colspan -> **27.9%** |  | [PwC] |

*Arithmetic check: 9.5 + 1.7 = 11.2; 15 + 1.7 = 16.7; 11.2 + 16.7 = 27.9. Reconciles.*

### Contribution bases -- with provenance

**Contribution bases -- with provenance**  _(2025: [HLB Albania]; 2026: [PwC significant developments])_

| Item | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| Minimum monthly base | ALL 40,000 | ALL 50,000 | 2025: [HLB Albania]; 2026: [PwC significant developments] |
| Maximum social-insurance base | ALL 176,416 | ALL 186,416 (DISPUTED) | 2025: [HLB Albania]; 2026: [PwC + HLB] -- one source says ALL 220,520 [ARS] |
| Health insurance ceiling | None | None | [tax-checker / TPA] |
| Minimum wage | ALL 40,000 (since 1 Apr 2023) | ALL 50,000 (DCM No. 776, 19.12.2025) | 2025: [PwC]; 2026: [ARS / DCM No. 776] |
| Self-employed social base | >= ALL 40,000 | >= ALL 50,000 | [PwC] |
| Self-employed health base | >= ALL 80,000 (2x min) | >= ALL 100,000 (2x min) | [PwC] |

### Self-employed rates -- with provenance

**Self-employed rates -- with provenance**  _([PwC])_

| Component | Rate | Base (2025) | Base (2026) | Source |
| --- | --- | --- | --- | --- |
| Social insurance | 23% | >= ALL 40,000 | >= ALL 50,000 | [PwC] |
| Health insurance | 3.4% | >= ALL 80,000 | >= ALL 100,000 | [PwC] |

*Self-employed monthly check (2025): social 40,000 x 0.23 = 9,200; health 80,000 x 0.034 = 2,720; total 11,920. (2026): social 50,000 x 0.23 = 11,500; health 100,000 x 0.034 = 3,400; total 14,900.*

### Forms

**Forms**  _([PwC]; [PwC -- Tax administration])_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Monthly payroll declaration (Listepagesa / E-SIG 025) | Declare salaries, withheld PIT, employer + employee social/health contributions | Electronically by the 20th of the following month | [PwC] |
| Annual individual income declaration (DIVA) | Annual personal income reconciliation for individuals above the filing threshold | By 31 March of the following year (verify threshold) [RESEARCH GAP -- threshold] | [PwC -- Tax administration] |

### Personal income tax (context only -- NOT this skill's scope)

Employment-income PIT under Law No. 29/2023 (effective 1 Jan 2024) is progressive with a tax-free portion, then 13%, then 23% above ~ALL 200,000/month [PwC -- Taxes on personal income]. The monthly tax-free threshold is reported variously as ALL 30,000-50,000 depending on salary level and the post-Constitutional-Court 2024-25 changes [RESEARCH GAP -- reviewer to confirm monthly PIT bands]. Do not compute PIT here.

### Penalties

**Penalties**  _([PwC -- Tax administration]; [PwC])_

| Item | Detail | Source / status |
| --- | --- | --- |
| Late declaration / late payment | Administrative penalties + late-payment interest under Law No. 9920/2008 (Tax Procedures); exact ALL/percentage figures not confirmed | [PwC -- Tax administration]; [RESEARCH GAP -- reviewer to confirm exact figures] |
| Undeclared work / failure to register employees | Significant fines apply; exact figure not confirmed | [PwC]; [RESEARCH GAP -- reviewer to confirm] |

### Test suite

**Test 1:** Employee, gross ALL 100,000/month, 2025. -> Employee social 9,500; employer social 15,000; employee health 1,700; employer health 1,700. Employee total = **11,200**; employer total = **16,700**; combined = **27,900**.

**Test 2:** Employee, gross ALL 250,000/month, 2025 (above ceiling 176,416). -> Employee social = 176,416 x 0.095 = **16,759.52**; employer social = 176,416 x 0.15 = **26,462.40**; employee health = 250,000 x 0.017 = **4,250**; employer health = **4,250**. Employee total = **21,009.52**; employer total = **30,712.40**.

**Test 3:** Employee, gross ALL 30,000/month, 2025 (below floor 40,000). -> Assess on min base 40,000. Employee social = 3,800; employer social = 6,000; employee health = 680; employer health = 680. Employee total = **4,480**; employer total = **6,680**.

**Test 4:** Self-employed, 2025. -> Social = 40,000 x 0.23 = **9,200**; health = 80,000 x 0.034 = **2,720**; total = **11,920**/month.

**Test 5:** Self-employed, 2026. -> Social = 50,000 x 0.23 = **11,500**; health = 100,000 x 0.034 = **3,400**; total = **14,900**/month.

**Test 6:** Employee, gross ALL 250,000/month, 2026 (above ceiling 186,416, PwC/HLB). -> Employee social = 186,416 x 0.095 = **17,709.52**; employer social = 186,416 x 0.15 = **27,962.40**; employee health = **4,250**; employer health = **4,250**. Employee total = **21,959.52**; employer total = **32,212.40**. FLAG: 2026 ceiling disputed.

**Test 7:** Employee, gross ALL 50,000/month, 2026 (within bounds: floor 50,000, ceiling 186,416). -> Employee social = 4,750; employer social = 7,500; employee health = 850; employer health = 850. Employee total = **5,600** (= 11.2%); employer total = **8,350** (= 16.7%).

**Test 8:** Bundled DPT debit ALL 45,000, single line, no payroll list. -> Cannot split PIT from contributions. EXCLUDE from VAT; request E-SIG 025; flag for reviewer.

### Prohibitions

- **Prohibition - employment status** — NEVER compute contributions without knowing employment status (employee vs self-employed).  _([PwC])_
- **Prohibition - health ceiling** — NEVER apply the social ceiling to the health components -- health (1.7%/1.7%) has NO ceiling.  _([tax-checker / TPA])_
- **Prohibition - sub-minimum gross** — NEVER assess contributions on a sub-minimum gross -- gross up to the minimum base.  _([HLB Albania])_
- **Prohibition - 2026 maximum base reliance** — NEVER rely on the 2026 maximum base (ALL 186,416) for a high earner without confirming against DCM No. 776 / Official Gazette -- it is disputed.  _([ARS / DCM No. 776])_
- **Prohibition - penalty quantification** — NEVER quantify late-payment or undeclared-work penalties -- the figures are unconfirmed [RESEARCH GAP]; escalate.  _([PwC -- Tax administration])_
- **Prohibition - PIT computation** — NEVER compute PIT in this skill -- the monthly bands conflict across sources; use a dedicated PIT skill.  _([PwC -- Taxes on personal income])_
- **Prohibition - employer vs employee lines** — NEVER treat employer contributions as the same line as withheld employee contributions -- they are distinct (16.7% vs 11.2%).  _([PwC])_
- **Prohibition - inbound vs outbound confusion** — NEVER confuse inbound benefits (pension, sickness, maternity) with outbound contributions.
- **Prohibition - definitive presentation** — NEVER present contribution figures as definitive -- label as estimated and direct the client to their E-SIG 025 payroll list and DPT/e-Albania account.
- **Prohibition - secondary aggregator figures** — NEVER use secondary aggregator base figures (e.g., ALL 22,000/95,130 or ALL 45,000/310,000) -- they conflict with PwC/HLB and appear erroneous.

## References

**References**  _(n/a)_

| Tag | Title | Publisher | URL |
| --- | --- | --- | --- |
| [PwC -- Other taxes] | Albania - Individual - Other taxes | PwC (reviewed 19 Feb 2026) | https://taxsummaries.pwc.com/albania/individual/other-taxes |
| [PwC significant developments] | Albania - Individual - Significant developments | PwC | https://taxsummaries.pwc.com/albania/individual/significant-developments |
| [PwC -- Taxes on personal income] | Albania - Individual - Taxes on personal income | PwC | https://taxsummaries.pwc.com/albania/individual/taxes-on-personal-income |
| [PwC -- Tax administration] | Albania - Individual - Tax administration | PwC | https://taxsummaries.pwc.com/albania/individual/tax-administration |
| [HLB Albania] | Increase of the Minimum Wage in Albania from 1 January 2026 | HLB Albania | https://www.hlb.al/increase-of-the-minimum-wage-in-albania-from-1-january-2026-what-changes-for-employers-and-employees/ |
| [ARS / DCM No. 776] | Council of Ministers Decision No. 776 dated 19.12.2025 -- National Minimum Wage | ARS firm (summary of official DCM) | https://arsfirm.al/en/council-of-ministers-decision-no-776-dated-december-19-2025-on-the-determination-of-the-minimum-wage-at-the-national-level/ |
| [tax-checker / TPA] | Social insurance in Albania | TPA Group / tax-checker (dated 2023) | https://www.tax-checker.com/tax-system-in-albania/social-insurance-in-albania/ |
| [Eurofast] | Albania Payroll Guide 2025 | Eurofast | https://eurofast.eu/wp-content/uploads/2025/02/Payroll-Guide-2025_Albania-1.pdf |
| [DPT] | Tax on personal income (official authority page) | General Directorate of Taxation (DPT) | https://www.tatime.gov.al/eng/c/4/96/108/tax-on-personal-income |

**Caveats (read before relying on 2026 figures):** The 2026 MAXIMUM social-insurance base is DISPUTED. PwC (reviewed Feb 2026) and HLB Albania state ALL 186,416 (same absolute +ALL 10,000 increase as the minimum wage); one firm summary (ARS) of DCM No. 776 states ALL 220,520 (25% proportional indexation matching the 40,000->50,000 minimum-wage rise). These cannot both be correct -- confirm against the published DCM No. 776 / Official Gazette before relying on the 2026 maximum. The 2025 figures (min ALL 40,000 / max ALL 176,416) are well-corroborated (high confidence). Penalty amounts and interest rates under Law No. 9920/2008 are not confirmed (low confidence) [RESEARCH GAP]. PIT monthly bands conflict across sources and are out of scope here. Confirm exact form codes (Listepagesa / E-SIG 025) with the e-Filing / e-Albania portal. Overall confidence: medium.

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
