---
name: nl-payroll-tax
description: Use this skill whenever asked about Dutch payroll taxes (loonheffingen) or the work cost scheme (werkkostenregeling / WKR). Trigger on phrases like "loonheffingen", "payroll tax Netherlands", "werkkostenregeling", "WKR", "loonbelasting", "premies volksverzekeringen", "premies werknemersverzekeringen", "wage tax NL", "eindheffing", "vrije ruimte", "salary administration", "loonadministratie", "werkgeverslasten", "employer costs NL", "payroll period filing", "loonstrook", "jaarloonopgave", "UWV premies", "WAO/WIA", "ZW premie", "AWf premie", "Whk premie", or any question about Dutch employer withholding, social contributions, or employee benefit taxation. Also trigger when reviewing payroll runs, computing employer costs, or advising on WKR allocation. ALWAYS read this skill before touching any Dutch payroll tax work.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NL Payroll Tax

## Netherlands Payroll Tax — Loonheffingen & Werkkostenregeling (WKR) v1.0

> **Based on work by [John in 't Hout (@johnhout)](https://github.com/johnhout/knowledge-work-belastingzaken)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Netherlands (Koninkrijk der Nederlanden) |
| Tax | Loonheffingen (wage tax + social insurance contributions) |
| Currency | EUR only |
| Period | Per pay period (month/4-week); annual reconciliation (loonaangifte) |
| Primary legislation | Wet op de loonbelasting 1964 (Wet LB); Wet financiering sociale verzekeringen (Wfsv) |
| WKR legislation | Articles 31, 31a Wet LB 1964 |
| Tax authority | Belastingdienst |
| Filing portal | Loonaangifte via payroll software or Mijn Belastingdienst |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a qualified Dutch belastingadviseur or salarisadministrateur |
| Skill version | 1.0 |

### Components of Loonheffingen [T1]

**Components of Loonheffingen**

| Component | Paid by | Rate/Notes |
| --- | --- | --- |
| Loonbelasting (wage tax) | Employee (withheld by employer) | Progressive rates aligned with Box 1 IB |
| Premie volksverzekeringen (AOW/Anw/Wlz) | Employee (withheld by employer) | Combined ~27.65% on first bracket |
| Premie werknemersverzekeringen (WW/WIA/ZW) | Employer | Various rates; see table below |
| Inkomensafhankelijke bijdrage Zvw | Employer | 6.57% (2025) |

### Volksverzekeringen Rates 2025 [T1]

**Volksverzekeringen Rates 2025**

| Premium | Rate | Max income (EUR) |
| --- | --- | --- |
| AOW (state pension) | 17.90% | EUR 38,441 |
| Anw (survivors) | 0.10% | EUR 38,441 |
| Wlz (long-term care) | 9.65% | EUR 38,441 |
| **Total** | **27.65%** | **EUR 38,441** |

- **Withholding note** — These are withheld from the employee's gross salary (combined with wage tax in bracket 1 rate of 35.82%).

### Werknemersverzekeringen (Employer Contributions) 2025 [T1]

**Werknemersverzekeringen (Employer Contributions) 2025**

| Premium | Rate | Max salary base (EUR) | Notes |
| --- | --- | --- | --- |
| AWf (unemployment — general) | 2.64% (fixed) / 7.64% (flex) | EUR 66,956 | Fixed contract = lower rate |
| Whk (disability — differentiated) | Sector-dependent (avg ~1.5%) | EUR 66,956 | Based on sector and claims history |
| Aof (disability — basic) | 6.18% (large) / 5.82% (small employer) | EUR 66,956 | Small = < 25× avg premium base |
| **Zvw (health insurance)** | **6.57%** | **EUR 66,956** | Employer-paid (not withheld from employee) |

### AWf Premium — Contract Type Distinction [T1]

**AWf Premium — Contract Type Distinction**

| Contract type | AWf rate 2025 |
| --- | --- |
| Permanent contract (vast contract, schriftelijk) | 2.64% |
| Flexible contract (bepaalde tijd, oproep, uitzend) | 7.64% |

- **Conditions for low rate** — Written permanent contract (schriftelijke arbeidsovereenkomst voor onbepaalde tijd); Not an on-call contract (geen oproepovereenkomst); Employee works ≥ contracted hours (no excessive overtime correction needed)

### Wage Tax Tables 2025 [T1]

The loonbelasting/premie volksverzekeringen are computed using Belastingdienst-provided tax tables:

**Wage Tax Tables 2025**

| Table type | Application |
| --- | --- |
| White table (witte tabel) | Standard employment |
| Green table (groene tabel) | One-off payments, holiday allowance, bonuses |
| Anonymous table | No BSN or ID provided — 52% flat rate |
| Table for DGA | DGA monthly minimum salary |

## Section 2 — Werkkostenregeling (WKR) — Work Cost Scheme

### Concept [T1]

- **WKR concept** — The WKR allows employers to provide tax-free benefits to employees within a "free space" (vrije ruimte) budget. Benefits exceeding the free space are subject to 80% flat-rate employer tax (eindheffing).

### Vrije Ruimte 2025 [T1]

**Vrije Ruimte 2025**

| Fiscal wage base (loonsom) | Free space percentage |
| --- | --- |
| First EUR 400,000 | 1.92% |
| Above EUR 400,000 | 1.18% |

**Example:** Employer with EUR 1,000,000 wage base:
- Free space = EUR 400,000 × 1.92% + EUR 600,000 × 1.18% = EUR 7,680 + EUR 7,080 = EUR 14,760

### WKR Categories [T1]

**WKR Categories**

| Category | Treatment | Examples |
| --- | --- | --- |
| Gerichte vrijstellingen (targeted exemptions) | Fully exempt — do NOT count against vrije ruimte | Travel allowance (max EUR 0.23/km), training costs, verhuiskostenvergoeding, extraterritoriale kosten (30% ruling) |
| Nihilwaarderingen (nil valuations) | Valued at EUR 0 — do NOT count against vrije ruimte | Workplace facilities (coffee, fruit), work clothing required for job, tools used at workplace |
| Vrije ruimte (free space) | Counts against budget; excess taxed at 80% | Christmas gifts, company parties, non-targeted benefits, staff outings |
| Individueel belast (individually taxed) | Taxed as employee wage (not WKR) | Benefits employee chooses to have taxed individually |

### Gerichte Vrijstellingen — Key Amounts 2025 [T1]

**Gerichte Vrijstellingen — Key Amounts 2025**

| Exemption | Amount/Rule |
| --- | --- |
| Travel allowance (reiskostenvergoeding) | Max EUR 0.23 per km (no cap on distance) |
| Relocation allowance (verhuiskostenvergoeding) | Max EUR 7,750 + actual moving costs |
| Study/training costs | Fully exempt if related to (future) employment |
| Meals at workplace (maaltijden) | Valued at EUR 3.55 per meal (2025); excess over employee contribution = WKR |
| Extraterritoriale kosten (30% ruling) | 30% of salary exempt or actual extraterritorial costs |
| Work-from-home allowance (thuiswerkvergoeding) | EUR 2.35 per day (2025) |
| Internet/phone (if partly business) | Reasonable business portion exempt |

### Eindheffing (Flat-Rate Tax on Excess) [T1]

**Eindheffing (Flat-Rate Tax on Excess)**

| Situation | Rate |
| --- | --- |
| Benefits exceeding vrije ruimte | 80% eindheffing (paid by employer) |
| Benefits exceeding EUR 2,400/occasion (gebruikelijkheidstoets) | Cannot use WKR — must be individually taxed |

- **Gebruikelijkheidstoets** — A single benefit provision cannot exceed EUR 2,400 per employee per occasion under the WKR. If it does, it must be individually taxed or split.

## Section 3 — Filing Obligations and Deadlines

### Periodic Filing [T1]

**Periodic Filing**

| Obligation | Frequency | Deadline |
| --- | --- | --- |
| Loonaangifte (payroll tax return) | Per pay period (monthly or 4-weekly) | Last day of month following pay period |
| Payment of loonheffingen | Per pay period | Same as filing deadline |
| Correctie loonaangifte | As needed | Within 5 years; penalties may apply after initial filing |

### Annual Obligations [T1]

**Annual Obligations**

| Obligation | Deadline | Notes |
| --- | --- | --- |
| Jaaropgave (annual statement to employees) | 28 February | Employer provides to each employee |
| WKR eindheffing determination | In first payroll return of following year | Determine if vrije ruimte exceeded; report 80% tax |
| Renseignementen (information returns) | Various | Third-party payments > EUR 5,000/year |

### Key Dates [T1]

**Key Dates**

| Event | Date |
| --- | --- |
| Payroll return deadline (monthly) | Last day of month + 1 month |
| Annual employer statement (jaaropgave) | 28 February |
| WKR assessment moment | 31 December (assess full year usage) |
| Report eindheffing | First return period of new year |

## Section 4 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Payroll run summary for the period. Employee count and contract types. Gross salary totals.

**Recommended:** Detailed payroll journal, WKR administration (benefits provided per category), sector classification for Whk, AWf contract type split.

**Ideal:** Full payroll software export, employment contracts, WKR policy document, expense claim registers, prior-year WKR reconciliation, UWV correspondence.

### Refusal Catalogue

- **R-LH-1 — No payroll data available** — Cannot compute loonheffingen without payroll run data. Provide at minimum gross salary totals per period.  _(R-LH-1)_
- **R-LH-2 — Contract types unclear** — Cannot determine AWf rate (2.64% vs 7.64%) without confirmed contract types. Flag all employees as flex rate (conservative) until confirmed.  _(R-LH-2)_
- **R-LH-3 — WKR allocation undocumented** — Cannot confirm vrije ruimte compliance without benefit-by-benefit administration. Flag for payroll advisor.  _(R-LH-3)_
- **R-LH-4 — Anonymous employee (no BSN)** — Must apply 52% anonymous rate. Cannot file normally without BSN and ID copy.  _(R-LH-4)_
- **R-LH-5 — 30% ruling status unclear** — Cannot apply extraterritorial exemption without confirmed Belastingdienst ruling. Apply standard treatment.  _(R-LH-5)_

## Section 5 — Computation Examples

### Example: Monthly Payroll Tax Computation

```
Given:
- Gross monthly salary: EUR 5,000
- Employee: permanent contract, below AOW age
- No special deductions

Step 1: Determine loonbelasting + premie volksverzekeringen
  → Use white monthly table from Belastingdienst
  → Approximate: EUR 5,000 × 35.82% = EUR 1,791 (first bracket)
  → Actual amount per tax table (includes heffingskortingen)

Step 2: Employer premiums:
  → AWf (permanent): EUR 5,000 × 2.64% = EUR 132
  → Aof: EUR 5,000 × 5.82% = EUR 291 (small employer)
  → Whk: EUR 5,000 × 1.50% = EUR 75 (example sector rate)
  → Zvw: EUR 5,000 × 6.57% = EUR 328.50

Step 3: Total employer cost above gross:
  → EUR 132 + EUR 291 + EUR 75 + EUR 328.50 = EUR 826.50

Step 4: Employee net (approximate):
  → EUR 5,000 − EUR 1,791 + heffingskortingen (from table) = net salary
```

### Example: WKR Assessment

```
Given:
- Annual wage base (fiscale loonsom): EUR 800,000
- Benefits provided: Christmas packages EUR 8,000, staff party EUR 5,000, bicycle scheme EUR 3,000

Step 1: Calculate vrije ruimte:
  → EUR 400,000 × 1.92% = EUR 7,680
  → EUR 400,000 × 1.18% = EUR 4,720
  → Total: EUR 12,400

Step 2: Determine which benefits count:
  → Christmas packages: EUR 8,000 (vrije ruimte)
  → Staff party: EUR 5,000 (vrije ruimte)
  → Bicycle scheme: EUR 3,000 (vrije ruimte — not a gerichte vrijstelling)
  → Total allocated: EUR 16,000

Step 3: Excess:
  → EUR 16,000 − EUR 12,400 = EUR 3,600

Step 4: Eindheffing:
  → EUR 3,600 × 80% = EUR 2,880 (employer pays)
```

## Section 6 — Control Checks and Red Flags

**Control Checks and Red Flags**

| Check | Issue if triggered |
| --- | --- |
| AWf rate mismatch vs contract type | Incorrect premium — back-payment risk |
| WKR benefit > EUR 2,400 per person per occasion | Gebruikelijkheidstoets failed — must individually tax |
| Vrije ruimte exceeded without eindheffing | Missing tax payment |
| Employee hours > 130% of contracted hours | AWf low rate at risk (herzieningsregeling) |
| Late filing (> 1 month) | EUR 65 fine per return; escalates |
| Missing jaaropgave | Employee cannot file IB return correctly |
| DGA on payroll below EUR 56,000 | Gebruikelijk loon non-compliance |
| No written employment contracts | All employees default to flex AWf rate |

## Section 7 — Official Source Verification Requirements

- **Verification steps** — Before any rate, threshold, or deadline is used in output: 1. Verify payroll filing instructions on `belastingdienst.nl/loonheffingen` 2. Verify premium rates in the annual "Nieuwsbrief Loonheffingen" (Belastingdienst) 3. Verify statutory text on `wetten.overheid.nl` (Wet LB 1964, Wfsv) 4. Record exact URL and retrieval date (YYYY-MM-DD) 5. If source unavailable or conflicting: mark as **UNVERIFIED** and require professional confirmation

## Section 8 — Escalation Points

Escalate to a qualified salarisadviseur or belastingadviseur when:

- Employee/contractor classification (dienstverband vs. opdracht) is unclear
- 30% ruling eligibility or application questions
- Cross-border employment (posting, frontier worker, split payroll)
- Payroll corrections affecting multiple prior periods
- Werknemersverzekeringen premium disputes with UWV
- WKR exceeds vrije ruimte by material amount (> EUR 10,000)
- Reorganisation or mass dismissal payroll implications
- Expatriate or DGA compensation structuring

## Disclaimer

**⚠️ DISCLAIMER: This skill provides workflow support only and does not constitute tax or payroll advice. All positions must be reviewed and signed off by a qualified Dutch belastingadviseur or salarisadministrateur before filing. Rates and thresholds change annually — verify against the current year's Nieuwsbrief Loonheffingen from belastingdienst.nl.**

*OpenAccountants — open-source accounting skills for AI*
*openaccountants.com*

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
