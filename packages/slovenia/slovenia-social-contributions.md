---
name: slovenia-social-contributions
description: Use this skill whenever asked about Slovenia social security contributions (prispevki za socialno varnost) for employees, employers, self-employed (samostojni podjetnik / s.p.), or pensioners. Trigger on phrases like "how much social security in Slovenia", "Slovenian payroll contributions", "prispevki za socialno varnost", "PIZ pension contribution", "ZZZS health contribution", "long-term care contribution Slovenia", "ZDOsk-1 LTC", "compulsory health contribution OZP", "REK-O form", "M-1 registration", "employer cost Slovenia", "gross to net Slovenia", "samostojni podjetnik prispevki", "self-employed contribution base Slovenia", or any question about Slovenian SSC obligations, rates, bases, ceilings, or deadlines. Also trigger when classifying bank statement transactions that relate to FURS contribution debits, ZPIZ/ZZZS payments, or eDavki/SPOT social-security transfers from NLB, NKBM, SKB, Intesa Sanpaolo, or other Slovenian banks. Also trigger when preparing payroll or an informative tax calculation (informativni izracun dohodnine) where contribution amounts and PIT withholding interact. This skill covers employee/employer contribution rates, the 1 July 2025 long-term care change, the flat OZP health contribution, the self-employed min/max base, REK-O and M-1 forms, payment deadlines, penalties, interaction with personal income tax (dohodnina), bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Slovenian SSC or payroll work.
version: 0.1
jurisdiction: SI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovenia Social Security Contributions (prispevki za socialno varnost) -- Payroll & Self-Employed

## Slovenia Social Security Contributions (prispevki za socialno varnost) -- Payroll & Self-Employed Skill v0.1

## Section 1 -- Quick reference

Read this whole section before computing or classifying anything.

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Slovenia (Republika Slovenija) |
| Primary Legislation | Zakon o prispevkih za socialno varnost (ZPSV -- Social Security Contributions Act) |
| Supporting Legislation | ZPIZ-2 (pension/disability); ZZVZZ (health insurance); ZDOsk-1 (Long-Term Care Act, LTC effective 1 July 2025); ZDoh-2 (Personal Income Tax Act); ZDavP-2 (Tax Procedure Act) |
| Collecting Authority | Financna uprava Republike Slovenije (FURS, www.fu.gov.si) -- collects SSC and PIT |
| Health / LTC administrator | Zavod za zdravstveno zavarovanje Slovenije (ZZZS) |
| Pension/disability administrator | Zavod za pokojninsko in invalidsko zavarovanje (ZPIZ) |
| Filing portals | eDavki (edavki.durs.si) and SPOT business portal (spot.gov.si) |
| Employee total SSC rate | 22.10% of gross until 30 Jun 2025; 23.10% from 1 Jul 2025 (after LTC) |
| Employer total SSC rate | 16.10% of gross until 30 Jun 2025; 17.10% from 1 Jul 2025 (after LTC) |
| Flat health contribution (OZP) | EUR 35/month Jan-Feb 2025; EUR 37.17/month from 1 Mar 2025 (per insured person) |
| Employee contribution ceiling | NONE -- no maximum assessment base for employees |
| Self-employed max base 2025 | EUR 8,876.11/month (3.5x average salary) |
| Self-employed min base 2025 | 60% of prior-year average monthly gross wage -- [RESEARCH GAP -- reviewer to confirm exact EUR figure against FURS OPSVZ table] |
| Minimum gross monthly wage 2025 | EUR 1,277.72 (full-time), effective 1 Jan 2025 |
| Payment frequency | Monthly (on/by salary payment for employees; by 20th of following month for self-employed) |
| Currency | EUR only |
| Validated by | Pending -- requires sign-off by a Slovenian licensed accountant (preizkuseni racunovodja / davcni svetovalec) |
| Validation date | Pending |

Does Slovenia have personal income tax? YES. Slovenia levies dohodnina (personal income tax) with five progressive brackets for 2025 plus a flat schedular rate on capital income. Contributions are computed on gross income and PIT is withheld separately on top -- they are distinct deductions in payroll. This skill is primarily about contributions; PIT brackets are reproduced in Section 10 for gross-to-net context.

**Employee contribution components (% of gross, do NOT include the separate 1% LTC line)**  _(Source: PwC Worldwide Tax Summaries -- Slovenia, Individual, Other taxes; SPOT)_

| Component | Employee rate | Authority |
| --- | --- | --- |
| Pension and disability insurance (PIZ) | 15.50% | ZPIZ |
| Compulsory health insurance | 6.36% | ZZZS |
| Unemployment (employment) insurance | 0.14% | -- |
| Parental protection (parental care) insurance | 0.10% | -- |
| Injury at work / occupational disease | 0.00% | -- |
| **Subtotal (pre-LTC)** | **22.10%** | -- |
| Long-term care (LTC, ZDOsk-1) -- from 1 Jul 2025 | +1.00% | ZZZS |
| **Total from 1 Jul 2025** | **23.10%** | -- |

**Employer contribution components (% of gross, do NOT include the separate 1% LTC line)**  _(Source: PwC; SPOT; KPMG GMS Flash Alert 2025-133)_

| Component | Employer rate | Authority |
| --- | --- | --- |
| Pension and disability insurance (PIZ) | 8.85% | ZPIZ |
| Compulsory health insurance | 6.56% | ZZZS |
| Unemployment (employment) insurance | 0.06% | -- |
| Parental protection (parental care) insurance | 0.10% | -- |
| Injury at work / occupational disease | 0.53% | -- |
| **Subtotal (pre-LTC)** | **16.10%** | -- |
| Long-term care (LTC, ZDOsk-1) -- from 1 Jul 2025 | +1.00% | ZZZS |
| **Total from 1 Jul 2025** | **17.10%** | -- |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown pay period (which side of 1 Jul 2025) | STOP -- the LTC change splits 2025 into two rate periods; do not pick a rate without the period |
| Unknown employment status | Ask -- do not assume employee vs self-employed; the base, min/max and rates differ |
| Unknown gross amount | STOP -- contributions are a percentage of gross; cannot compute without gross |
| Self-employed with unknown income | Apply the minimum contribution base (60% of prior-year average wage) -- flag for reviewer to confirm EUR figure |
| Flat OZP for a part-month / multiple employers | Withhold full EUR 37.17/month per insured person; flag for reviewer (apportionment rules) |
| Unknown whether ceiling applies | Employees have NO ceiling; only self-employed are capped at EUR 8,876.11/month |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Minimum viable -- (1) employment status (employee / employer-cost / self-employed / pensioner), (2) gross monthly amount (or contribution base for self-employed), and (3) the pay period month/year (to select the pre- or post-1 July 2025 rate). Without the pay period, STOP -- the LTC change splits 2025 into two rate periods.

Recommended -- whether the person has multiple insurers/employers (relevant to the flat OZP), prior-year income for self-employed base determination, and whether PIT withholding is also required.

Ideal -- the REK-O filing data, M-1 registration confirmation, FURS account statement (eDavki), and for self-employed the published OPSVZ contribution table for the year.

### Refusal catalogue

- **R-SI-SSC-1 -- Pay period unknown** — Trigger: the month/year of the salary is not provided. Message: "The pay period is mandatory. The long-term care contribution (ZDOsk-1) took effect 1 July 2025, raising employee SSC from 22.10% to 23.10% and employer SSC from 16.10% to 17.10%. I cannot select a rate without knowing whether the payment falls before or after 1 July 2025."
- **R-SI-SSC-2 -- Self-employed minimum/maximum base** — Trigger: computing self-employed contributions where the exact contribution base is required. Message: "The exact 2025 self-employed minimum monthly contribution base in EUR is not confirmed in this skill [RESEARCH GAP]. The minimum is stated as 60% of the prior-year average monthly gross wage; the maximum is EUR 8,876.11/month. Confirm the precise published OPSVZ figure with FURS before filing. Escalate to a Slovenian licensed accountant."
- **R-SI-SSC-3 -- Contribution arrears / default interest** — Trigger: client has unpaid contributions from prior periods or asks to quantify default interest. Message: "Default interest on unpaid contributions accrues under ZDavP-2; sources cite a statutory 7% p.a. (Art. 95) and a daily ~9.02% p.a. rate during procedures (Art. 96) [RESEARCH GAP -- precise applicable 2025 rate not confirmed]. Do not quantify arrears without a FURS statement. Escalate to a Slovenian licensed accountant."
- **R-SI-SSC-4 -- Penalties / administrative fines** — Trigger: client asks about fines for failure to register, report (REK-O) or pay contributions. Message: "Specific administrative fine amounts under ZPSV/ZDavP-2 are not confirmed from an authoritative source in this skill [RESEARCH GAP]. Escalate to a Slovenian licensed accountant."
- **R-SI-SSC-5 -- Cross-border / posted workers / A1 certificates** — Trigger: client works in or from another EU/EEA state, holds an A1, or asks about which country's social security applies. Message: "Cross-border social-security coordination (EU Regulation 883/2004, A1 certificates, posting) determines which state's contributions apply and is outside the scope of this skill. Escalate to a Slovenian licensed accountant."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Slovenian social security. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

How to read this table. Match by case-insensitive substring on the counterparty/reference (namen / prejemnik) as it appears in the bank statement. Contribution payments always EXCLUDE from any VAT (DDV) return or revenue/expense supply classification -- they are statutory payroll/personal obligations, not taxable supplies. Note: in Slovenia both contributions AND withheld PIT are paid to FURS, often by reference (sklic) model 19; distinguish by the reference structure, not just the payee name.

### 3.1 FURS contribution debits (employee + employer SSC)

**FURS contribution debit patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| FURS, FINANCNA UPRAVA | EXCLUDE -- statutory payment to FURS | Could be SSC, PIT or other tax; check sklic reference |
| PRISPEVKI, PRISPEVEK | EXCLUDE -- social security contribution | "Contribution(s)" in Slovenian |
| PRISPEVKI ZA SOCIALNO VARNOST | EXCLUDE -- SSC payment | Full statutory term |
| SOCIALNA VARNOST, SOC. VARNOST | EXCLUDE -- SSC payment | Same |
| ZPIZ, POKOJNINSKO | EXCLUDE -- pension/disability (PIZ) | 15.50% employee / 8.85% employer |
| ZZZS, ZDRAVSTVENO | EXCLUDE -- health insurance + LTC + OZP | 6.36%/6.56% + flat OZP + LTC |
| OZP, OPZ | EXCLUDE -- flat compulsory health contribution | EUR 37.17/month from 1 Mar 2025 |
| DOLGOTRAJNA OSKRBA, ZDOsk | EXCLUDE -- long-term care (LTC) | 1%+1% from 1 Jul 2025 |

### 3.2 FURS / contribution debits appearing on specific Slovenian banks

**Bank-specific FURS contribution debit descriptions**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| NLB (Nova Ljubljanska banka) | "FURS PRISPEVKI" or "FINANCNA UPRAVA RS" | EXCLUDE -- SSC/PIT |
| NKBM (Nova KBM / OTP) | "FURS" or "PRISPEVKI SOC. VARNOST" | EXCLUDE -- SSC |
| SKB banka | "FURS PRISPEVKI" or "ZZZS/ZPIZ" | EXCLUDE -- SSC |
| Intesa Sanpaolo Bank (SI) | "FINANCNA UPRAVA" or "PRISPEVKI" | EXCLUDE -- SSC |
| Sberbank/Delavska hranilnica | "FURS" or "SOCIALNA VARNOST" | EXCLUDE -- SSC |
| Revolut / Wise | Rare -- FURS debits typically come from local SI accounts | If present, EXCLUDE |

### 3.3 PIT (dohodnina) payments to FURS (NOT contributions -- do not confuse)

**PIT payment patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AKONTACIJA DOHODNINE | EXCLUDE -- PIT withholding, not SSC | Advance personal income tax |
| DOHODNINA, AKONTACIJA | EXCLUDE -- PIT, not SSC | Tax payment, not social security |
| DAVEK OD DOHODKA | EXCLUDE -- income tax | Not a contribution |
| FURS (sklic for PIT) | EXCLUDE -- distinguish by sklic reference | Same payee as SSC; check reference model |

### 3.4 Salary and payroll (exclude from SSC classification)

**Salary and payroll patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PLACA, NETO PLACA (outgoing) | EXCLUDE -- net salary to employee | Not a contribution payment |
| PLACA, OSEBNI DOHODEK (incoming) | EXCLUDE -- employment income received | Not a contribution payment |
| REGRES, BOZICNICA | EXCLUDE -- holiday allowance / bonus | Payroll item; contribution treatment is separate |

### 3.5 Pension / benefit payments received (not SSC contributions)

**Pension/benefit payment patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| POKOJNINA, ZPIZ POKOJNINA | EXCLUDE -- pension income received | Pensioners now pay 1% LTC on net pension (from 1 Jul 2025) |
| NADOMESTILO, BOLNISKO | EXCLUDE -- sickness/benefit income | Not a contribution paid |

## Section 4 -- Worked examples

Six bank statement classifications and payroll computations for hypothetical Slovenian taxpayers. Currency is EUR. Bank-statement lines use the Slovenian convention (date ; prejemnik/namen ; debit/credit ; reference ; amount ; currency).

### Example 1 -- Standard employer SSC remittance, post-LTC (NLB)

Input line: `18.08.2025 ; FINANCNA UPRAVA RS ; DEBIT ; PRISPEVKI 07/2025 ; -402.00 ; EUR`

Reasoning: Matches "FINANCNA UPRAVA RS" + "PRISPEVKI" (patterns 3.1/3.2, NLB). July 2025 falls AFTER 1 July 2025, so the employer rate is 17.10%. On an illustrative gross of EUR 2,350: 17.10% x EUR 2,350 = EUR 401.85 (approx EUR 402). This is the employer-side SSC remittance. Exclude from DDV (VAT). Record as an employer payroll cost.

Classification: EXCLUDE -- employer SSC payment (post-LTC 17.10%). Not a VAT supply.

### Example 2 -- Employee SSC withheld, pre-LTC (NKBM)

Input line: `15.05.2025 ; FURS ; DEBIT ; PRISPEVKI SOC. VARNOST 04/2025 ; -441.97 ; EUR`

Reasoning: Matches "FURS" + "PRISPEVKI SOC. VARNOST" (pattern 3.1/3.2). April 2025 is BEFORE 1 July 2025, so the employee rate is 22.10%. On a gross of EUR 2,000: 22.10% x EUR 2,000 = EUR 442.00 (approx). This is employee SSC withheld from gross and remitted to FURS. The flat OZP (EUR 37.17/month) and PIT are separate lines. Exclude from VAT.

Classification: EXCLUDE -- employee SSC (pre-LTC 22.10%). Not a VAT supply.

### Example 3 -- Flat compulsory health contribution OZP (SKB)

Input line: `20.06.2025 ; ZZZS ; DEBIT ; OZP 05/2025 ; -37.17 ; EUR`

Reasoning: Matches "ZZZS" + "OZP" (pattern 3.1). Amount EUR 37.17 is the flat compulsory health contribution (OZP/OPZ) per insured person, applicable from 1 March 2025 (EUR 35 in Jan-Feb 2025). This is a FLAT euro amount, NOT a percentage, and is distinct from the percentage health insurance (6.36%/6.56%). Withheld by employer for employees. Exclude from VAT.

Classification: EXCLUDE -- flat OZP health contribution (EUR 37.17/month). Not a percentage; not a VAT supply.

### Example 4 -- PIT (dohodnina) payment, NOT a contribution (Intesa Sanpaolo)

Input line: `18.09.2025 ; FINANCNA UPRAVA ; DEBIT ; AKONTACIJA DOHODNINE 08/2025 ; -312.40 ; EUR`

Reasoning: Matches "FINANCNA UPRAVA" but the reference is "AKONTACIJA DOHODNINE" (pattern 3.3). This is advance personal income tax (PIT withholding), NOT a social security contribution. Same payee (FURS) as SSC, so distinguish by the reference. Do not classify as SSC. Exclude from VAT.

Classification: EXCLUDE -- PIT (dohodnina) withholding. NOT a contribution.

### Example 5 -- Self-employed (s.p.) monthly contribution, capped (NLB)

Input line: `19.07.2025 ; FURS ; DEBIT ; OPSVZ 06/2025 ; -3,545.42 ; EUR`

Reasoning: Matches "FURS" + "OPSVZ" (self-employed contribution calculation; pattern 3.1). A high-earning sole trader at the maximum base EUR 8,876.11/month. Combined self-employed SSC for June 2025 (pre-LTC) is employee+employer-equivalent. Illustrative: 38.20% (22.10% + 16.10%, both borne by the s.p.) x EUR 8,876.11 = EUR 3,390.67, plus flat OZP EUR 37.17. The exact total depends on the OPSVZ table and the self-employed LTC (2% from 1 Jul 2025). June 2025 is pre-LTC. Exclude from VAT. Note self-employed pay by the 20th of the following month (Art. 353 ZDavP-2).

Classification: EXCLUDE -- self-employed (s.p.) SSC at capped base. Flag for reviewer to confirm against OPSVZ table. Not a VAT supply.

### Example 6 -- Pensioner LTC on net pension, post-LTC (Delavska hranilnica)

Input line: `05.08.2025 ; ZZZS ; DEBIT ; DOLGOTRAJNA OSKRBA 07/2025 ; -8.45 ; EUR`

Reasoning: Matches "ZZZS" + "DOLGOTRAJNA OSKRBA" (pattern 3.1). From 1 July 2025, pensioners pay 1% LTC on NET pension under ZDOsk-1. On a net pension of EUR 845: 1% x EUR 845 = EUR 8.45. This is a contribution paid (deducted from pension), not pension income received. Exclude from VAT.

Classification: EXCLUDE -- pensioner LTC contribution (1% of net pension, from 1 Jul 2025). Not a VAT supply.

## Section 5 -- Tier 1 rules

These rules apply when bank statement / payroll data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- Employee SSC formula

- **Employee SSC formula** — employee_SSC = gross x employee_rate where employee_rate = 22.10% for pay periods up to 30 Jun 2025 = 23.10% for pay periods from 1 Jul 2025 (LTC +1pp) PLUS flat OZP = EUR 37.17/month (EUR 35 for Jan-Feb 2025), withheld per insured person NO ceiling for employees  _(Source: PwC; SPOT; KPMG GMS Flash Alert 2025-133)_

### Rule 2 -- Employer SSC formula

- **Employer SSC formula** — employer_SSC = gross x employer_rate where employer_rate = 16.10% for pay periods up to 30 Jun 2025 = 17.10% for pay periods from 1 Jul 2025 (LTC +1pp) NO ceiling for employees  _(Source: PwC; SPOT)_

### Rule 3 -- The 1 July 2025 LTC change splits 2025 into two periods

- **LTC split rule** — The long-term care contribution (ZDOsk-1) is effective 1 July 2025. It adds 1 percentage point to BOTH the employee total (22.10% -> 23.10%) and the employer total (16.10% -> 17.10%). Always select the rate by the pay period: Jan-Jun 2025 = pre-LTC, Jul-Dec 2025 = post-LTC. The LTC is collected like health contributions by ZZZS.  _(Source: KPMG GMS Flash Alert 2025-133)_

### Rule 4 -- Component breakdown does NOT include the separate LTC line

- **Component breakdown rule** — The statutory employee breakdown (15.50% PIZ / 6.36% health / 0.14% unemployment / 0.10% parental / 0.00% work-injury = 22.10%) and employer breakdown (8.85% / 6.56% / 0.06% / 0.10% / 0.53% = 16.10%) are the long-standing rates. The 1% LTC is additive on top, which is why each total rises by 1pp from 1 July 2025. Do not double-count.  _(Source: PwC; SPOT)_

### Rule 5 -- The flat OZP is a euro amount, not a percentage

- **Flat OZP rule** — The compulsory health contribution (OZP/OPZ), introduced 1 January 2024, is a FLAT per-capita amount: EUR 35/month in Jan-Feb 2025, EUR 37.17/month from 1 March 2025. It is adjusted annually on 1 March. It is separate from the percentage health insurance (6.36%/6.56%) and is withheld by the employer for employees.  _(Source: KPMG GMS Flash Alert 2024-046; PwC)_

### Rule 6 -- No ceiling for employees; cap only for self-employed

- **Ceiling rule** — Employees have NO maximum contribution assessment base -- contributions apply to the full gross. Only self-employed are capped, at 3.5x the average salary = EUR 8,876.11/month for 2025.  _(Source: European Commission "Your social security rights in Slovenia"; RRA Koroska)_

### Rule 7 -- Self-employed contribution base

- **Self-employed base rule** — The self-employed (s.p.) base ranges from a minimum of 60% of the prior-year average monthly gross wage to a maximum of EUR 8,876.11/month for 2025. The self-employed person bears BOTH the employee and employer rates, and a 2% LTC from 1 July 2025. [RESEARCH GAP -- exact 2025 minimum EUR base to be confirmed against the FURS OPSVZ table.]  _(Source: RRA Koroska; ZPSV)_

### Rule 8 -- Contribution base is gross employment income

- **Contribution base rule** — Contributions are computed on the gross amount of employment income. The employer withholds employee contributions and PIT and pays the employer-side contributions at the time of salary payment.  _(Source: PwC; SPOT)_

### Rule 9 -- Payment / filing schedule

**Payment / filing schedule**  _(Source: SPOT; FURS eDavki; payroll guides -- [RESEARCH GAP -- the exact statutory REK-O deadline should be cross-checked with FURS eDavki documentation.])_

| Obligor | Report | Filing / payment timing |
| --- | --- | --- |
| Employer (per employee) | REK-O (formerly REK-1) via eDavki | Filed on/by the employee's pay day; data flows to AJPES |
| Employer (new hire) | M-1 via SPOT/eDavki to ZPIZ | Before commencement of work |
| Self-employed | OPSVZ calculation via eDavki | Submit by 15th of month for prior month; pay by 20th (Art. 353 ZDavP-2) |

### Rule 10 -- Slovenia HAS personal income tax (kept separate from SSC)

- **PIT separation rule** — PIT (dohodnina) is withheld as akontacija dohodnine on top of contributions; the two are distinct payroll deductions. Annual PIT is reconciled via the informative tax calculation (informativni izracun dohodnine, IID). Do not net PIT against contributions. (See Section 10 for 2025 brackets.)  _(Source: PwC; FURS)_

## Section 6 -- Tier 2 catalogue

When payroll/bank data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Pay period straddling 1 July 2025

Trigger: A salary payment relates to a period spanning June-July 2025, or a back-payment is made after 1 July for an earlier period.

Issue: The applicable LTC (1pp) depends on whether the relevant period falls before or after 1 July 2025. Back-payments and mixed periods can be ambiguous.

Action: Flag for reviewer. Confirm the period the salary relates to before selecting 22.10%/16.10% vs 23.10%/17.10%.

### T2-2 -- Self-employed minimum base determination

Trigger: Computing s.p. contributions where prior-year income is low or the person is newly self-employed.

Issue: The minimum base is 60% of the prior-year average monthly gross wage, but the exact 2025 EUR figure is not confirmed here, and newly self-employed may have a different (often reduced) base in the first periods.

Action: Flag for reviewer. Confirm the EUR minimum against the FURS published OPSVZ table. [RESEARCH GAP]

### T2-3 -- Flat OZP with multiple insurers / part month

Trigger: A person is insured through more than one basis (e.g., employment + self-employment), or starts/ends mid-month.

Issue: The flat OZP (EUR 37.17/month) is per insured person; apportionment or single-charge rules across multiple bases / part months are not detailed here.

Action: Flag for reviewer to confirm how many flat OZP charges apply.

### T2-4 -- Contribution arrears / default interest

Trigger: Client has unpaid contributions from prior periods.

Issue: Default interest accrues under ZDavP-2; sources cite 7% p.a. (Art. 95) and a daily ~9.02% p.a. (Art. 96) during procedures. The precise 2025 applicable rate is not confirmed.

Action: Do not quantify arrears without a FURS statement. Escalate to a Slovenian licensed accountant. [RESEARCH GAP]

### T2-5 -- Pensioner / mixed-income LTC

Trigger: Client receives a pension and also has employment/self-employment income.

Issue: From 1 July 2025 pensioners pay 1% LTC on net pension; the interaction of LTC across pension + employment + self-employment is not detailed here.

Action: Flag for reviewer to confirm the LTC base(s) that apply.

### T2-6 -- Cross-border / posted workers

Trigger: Work performed in/from another EU/EEA state, A1 certificate held, or uncertainty over which state's social security applies.

Issue: EU coordination (Reg. 883/2004) determines the competent state; Slovenian contributions may not apply.

Action: Flag for reviewer. Do not assume Slovenian contributions without confirming the competent state.

## Section 7 -- Excel working paper template

When producing a Slovenian SSC computation, structure the working paper as follows:

```
SLOVENIA SOCIAL SECURITY CONTRIBUTIONS -- WORKING PAPER
Client: [name]
Tax Year / Pay Period: [month/year]
Prepared: [date]

INPUT DATA
  Status (employee/employer/self-employed/pensioner): [____]
  Pay period (which side of 1 Jul 2025):              [PRE / POST]
  Gross monthly income / contribution base:           EUR [____]
  Multiple insurers / employers:                      [YES/NO]
  Prior-year income (self-employed only):             EUR [____]

RATE SELECTION
  Employee rate (22.10% pre / 23.10% post):           [____]%
  Employer rate (16.10% pre / 17.10% post):           [____]%
  Self-employed combined (where applicable):          [____]%
  Self-employed cap applied (EUR 8,876.11/month):     [YES/NO]
  Employee ceiling:                                   NONE

COMPUTATION
  Employee SSC (gross x employee rate):               EUR [____]
  Employer SSC (gross x employer rate):               EUR [____]
  Flat OZP health contribution:                       EUR 37.17  (EUR 35 Jan-Feb 2025)
  Long-term care (LTC) -- only from 1 Jul 2025:       EUR [____]  (included in the rate from Jul)
  Total contributions:                                EUR [____]

PIT INTERACTION (separate from SSC)
  Akontacija dohodnine withheld (see Section 10):     EUR [____]
  Net pay (gross - employee SSC - OZP - PIT):         EUR [____]

FILING
  REK-O filed (on pay day):                           [YES/NO]
  M-1 filed (new hire, before work start):            [YES/NO/NA]
  Self-employed OPSVZ (file by 15th, pay by 20th):    [YES/NO/NA]

REVIEWER FLAGS
  [List any Tier 2 flags here]

RESEARCH GAPS / CONSERVATIVE DEFAULTS APPLIED
  [List any RESEARCH GAP markers and defaults applied]
```

## Section 8 -- Bank statement reading guide

### How contribution debits appear on Slovenian bank statements

NLB (Nova Ljubljanska banka):
- Description: "FINANCNA UPRAVA RS" or "FURS PRISPEVKI" with a sklic (reference) model 19
- Timing: Around salary payment day (employers); by the 20th of the following month (self-employed)
- Amount: A percentage of gross (employee/employer rate) plus a separate flat OZP line

NKBM / OTP:
- Description: "FURS" or "PRISPEVKI SOC. VARNOST"
- Timing: Same monthly cycle
- Amount: Percentage of gross + flat OZP

SKB banka / Intesa Sanpaolo / Delavska hranilnica:
- Description: "FURS PRISPEVKI", "ZZZS", "ZPIZ", "DOLGOTRAJNA OSKRBA", or "OZP"
- Timing: Same monthly cycle

Key identification tips:
1. Contribution debits are always outgoing (DEBIT), never credits.
2. Both contributions AND PIT (akontacija dohodnine) are paid to FURS -- distinguish by the reference (sklic), not just the payee name.
3. A flat EUR 37.17 (or EUR 35 in Jan-Feb 2025) line is the OZP health contribution, NOT a percentage.
4. A small "DOLGOTRAJNA OSKRBA" / LTC line only appears from 1 July 2025.
5. Slovenian language terms: prispevki = contributions; dohodnina = personal income tax; placa = salary; pokojnina = pension; zdravstveno = health; pokojninsko = pension.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. Scan for FURS / ZZZS / ZPIZ debits -- identify all outgoing payments matching Section 3 patterns.
2. Separate contributions from PIT -- use the sklic reference to split SSC from akontacija dohodnine; do not lump them together.
3. Identify the flat OZP -- a recurring EUR 37.17 (or EUR 35 in Jan-Feb 2025) line is the flat health contribution per insured person.
4. Determine the period for LTC -- payments for periods from 1 July 2025 should reflect the +1pp LTC; pre-July payments should not.
5. Reverse-engineer the gross (employees):
   - If an SSC debit / gross approximates 22.10% (pre-Jul) or 23.10% (post-Jul), it is the employee side.
   - If it approximates 16.10% (pre-Jul) or 17.10% (post-Jul), it is the employer side.
6. Flag for reviewer: "Contribution classification derived from bank statement amounts only. Employment status, gross, pay period, and the self-employed base have not been independently verified. Reviewer must confirm before filing REK-O / OPSVZ and the informative tax calculation."

## Section 10 -- Reference material

### 2025 personal income tax (dohodnina) brackets -- for gross-to-net context

**2025 PIT brackets**  _(Source: PwC Worldwide Tax Summaries -- Slovenia, Individual.)_

| Band | Lower (EUR) | Upper (EUR) | Rate | Tax on lower bound (EUR) |
| --- | --- | --- | --- | --- |
| Bracket 1 | 0 | 9,210.26 | 16% | 0 |
| Bracket 2 | 9,210.26 | 27,089.00 | 26% | 1,473.64 |
| Bracket 3 | 27,089.00 | 54,178.00 | 33% | 6,122.11 |
| Bracket 4 | 54,178.00 | 78,016.32 | 39% | 15,061.48 |
| Bracket 5 | 78,016.32 | -- | 50% | 24,358.43 |
| Capital income (interest, dividends, capital gains, rental) | flat 25% (schedular, generally final); rental may have deductible costs |  |  |  |

(Cumulative-tax check, PwC figures: 9,210.26 x 16% = 1,473.64; +(27,089.00-9,210.26) x 26% = 6,122.11; +(54,178.00-27,089.00) x 33% = 15,061.48; +(78,016.32-54,178.00) x 39% = 24,358.42 -- PwC tabulates 24,358.43, a EUR 0.01 rounding difference; use the PwC figure. Source: PwC Worldwide Tax Summaries -- Slovenia, Individual, Taxes on personal income.)

General (basic) personal allowance 2025: EUR 5,260.00 general allowance; additional general allowance for income up to EUR 16,832.00 computed as 19,736.99 - 1.17259 x total income. (Source: PwC) -- [RESEARCH GAP -- if FURS publishes ZDoh-2 inflation-indexed thresholds that differ slightly for 2025, prefer the FURS-published values.]

### Contribution rate summary (2025)

**Contribution rate summary table**

| Component | Employee | Employer | Authority |
| --- | --- | --- | --- |
| Pension and disability (PIZ) | 15.50% | 8.85% | ZPIZ |
| Compulsory health insurance | 6.36% | 6.56% | ZZZS |
| Unemployment (employment) | 0.14% | 0.06% | -- |
| Parental protection | 0.10% | 0.10% | -- |
| Injury at work / occupational disease | 0.00% | 0.53% | -- |
| **Subtotal (pre-LTC)** | **22.10%** | **16.10%** | -- |
| Long-term care (LTC, from 1 Jul 2025) | +1.00% | +1.00% | ZZZS |
| **Total from 1 Jul 2025** | **23.10%** | **17.10%** | -- |
| Flat OZP health contribution | EUR 35/mo Jan-Feb 2025; EUR 37.17/mo from 1 Mar 2025 | (withheld by employer) | ZZZS |
| LTC -- pensioners | 1% of net pension (from 1 Jul 2025) | -- | -- |
| LTC -- self-employed | 2% (acts as both sides, from 1 Jul 2025) | -- | -- |

### Key thresholds and bases (2025)

**Key thresholds and bases table**

| Item | Value |
| --- | --- |
| Employee contribution ceiling | NONE -- no maximum assessment base |
| Self-employed minimum base | 60% of prior-year average monthly gross wage [RESEARCH GAP -- exact EUR to confirm] |
| Self-employed maximum base | EUR 8,876.11/month (3.5x average salary) |
| Minimum gross monthly wage 2025 | EUR 1,277.72 (full-time), effective 1 Jan 2025 |
| Minimum gross monthly wage 2026 | EUR 1,481.88 (full-time) |
| Average gross wage 2025 (OECD) | approx EUR 30,135/year (approx EUR 2,511/month) |

### Forms

**Forms table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| REK-O (formerly REK-1) | Employer monthly report of gross income, contributions and withheld PIT per employee, via eDavki; data to AJPES | On/by the employee's pay day [RESEARCH GAP -- confirm with FURS] |
| M-1 | Registration of a new employee into pension/disability, health, unemployment | Before commencement of work |
| OPSVZ | Self-employed monthly social-security contribution calculation | Submit by 15th; pay by 20th of month for prior month (Art. 353 ZDavP-2) |
| Informativni izracun dohodnine (IID) | Annual PIT informative calculation issued by FURS; becomes the assessment if not objected to | Issued by FURS by end of March / by end of May; object within 30 days; if no IID, file return by 31 July |

### Penalties

**Penalties table**

| Penalty | Detail |
| --- | --- |
| Late payment default interest | Under ZDavP-2: statutory 7% p.a. (Art. 95); daily 0.0247% (approx 9.02% p.a.) during procedures (Art. 96). [RESEARCH GAP -- confirm precise applicable 2025 rate] |
| Failure to register/report/pay | Administrative fines for employers under ZPSV/ZDavP-2; FURS verifies payment. [RESEARCH GAP -- specific fine amounts not confirmed] |

### Test suite

Test 1: Employee, gross EUR 2,000, pay period May 2025 (pre-LTC). -> Employee SSC = 22.10% x 2,000 = EUR 442.00, plus flat OZP EUR 37.17. Employer SSC = 16.10% x 2,000 = EUR 322.00.

Test 2: Employee, gross EUR 2,000, pay period August 2025 (post-LTC). -> Employee SSC = 23.10% x 2,000 = EUR 462.00, plus flat OZP EUR 37.17. Employer SSC = 17.10% x 2,000 = EUR 342.00.

Test 3: Employee, gross EUR 50,000/month (high earner), pay period September 2025. -> NO ceiling applies. Employee SSC = 23.10% x 50,000 = EUR 11,550.00. Employer SSC = 17.10% x 50,000 = EUR 8,550.00.

Test 4: Self-employed, base capped at EUR 8,876.11/month, June 2025 (pre-LTC). -> Combined 38.20% (22.10% + 16.10%) x 8,876.11 = EUR 3,390.67, plus flat OZP EUR 37.17. Flag for reviewer to confirm against OPSVZ table.

Test 5: Flat OZP for January 2025. -> EUR 35.00 (the EUR 37.17 figure applies only from 1 March 2025).

Test 6: Pensioner, net pension EUR 845, July 2025. -> LTC = 1% x 845 = EUR 8.45 (LTC effective 1 Jul 2025; no LTC for pre-July periods).

Test 7: Employee, gross EUR 1,277.72 (2025 minimum wage), April 2025. -> Employee SSC = 22.10% x 1,277.72 = EUR 282.38, plus flat OZP EUR 37.17. Employer SSC = 16.10% x 1,277.72 = EUR 205.71.

Test 8: FURS debit referenced "AKONTACIJA DOHODNINE". -> NOT a contribution. Classify as PIT withholding; exclude from SSC and from VAT.

### Prohibitions

- NEVER select an SSC rate without knowing the pay period -- the 1 July 2025 LTC change splits 2025 into 22.10%/16.10% (pre) and 23.10%/17.10% (post).
- NEVER apply a maximum ceiling to an EMPLOYEE -- only self-employed are capped (EUR 8,876.11/month for 2025).
- NEVER treat the flat OZP (EUR 37.17/month) as a percentage -- it is a fixed euro amount per insured person.
- NEVER double-count the LTC -- it is already included in the 23.10%/17.10% post-July totals; the component breakdown excludes it.
- NEVER conflate contributions with PIT (akontacija dohodnine) -- both go to FURS but are distinct deductions; distinguish by the sklic reference.
- NEVER invent the self-employed minimum EUR base -- it is a RESEARCH GAP; confirm against the FURS OPSVZ table.
- NEVER quantify contribution arrears or default interest without a FURS statement -- the precise rate is a RESEARCH GAP.
- NEVER state specific administrative fine amounts -- they are a RESEARCH GAP; escalate to a licensed accountant.
- NEVER assume Slovenian contributions apply to a cross-border / posted worker without confirming the competent EU state.
- NEVER present contribution or PIT figures as definitive -- always label as estimated and direct the client to their FURS (eDavki) statement.

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
