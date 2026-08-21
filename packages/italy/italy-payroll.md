---
name: italy-payroll
description: Use this skill whenever asked about Italian payroll processing for employees. Trigger on phrases like "Italian payroll", "busta paga", "cedolino", "IRPEF ritenuta", "ritenuta d'acconto dipendenti", "INPS contributi", "contributi previdenziali", "TFR", "trattamento di fine rapporto", "CU certificazione unica", "F24", "tredicesima", "quattordicesima", "stipendio netto Italia", "brutto netto Italia", "Agenzia delle Entrate", "addizionale regionale", "addizionale comunale", "CCNL minimum wage", "ferie maturate", "malattia INPS", "maternità INPS", or any question about computing employee pay, income tax withholding, or social contributions in Italy. This skill covers IRPEF withholding, INPS contributions (employee and employer), TFR, mandatory benefits, busta paga (payslip) requirements, CU/F24 filing, and employer cost analysis. ALWAYS read this skill before processing any Italian employee payroll.
version: 1.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italy Payroll

## Italy Payroll Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Currency | EUR only |
| Standard pay frequency | Monthly (mensile) -- universal; paid in 13 or 14 instalments per year |
| Tax year | Calendar year (1 January -- 31 December) |
| Income tax withholding | IRPEF ritenuta alla fonte (employer as sostituto d'imposta) |
| Local tax surcharges | Addizionale regionale + Addizionale comunale IRPEF |
| Social insurance authority | INPS (Istituto Nazionale della Previdenza Sociale) |
| Tax authority | Agenzia delle Entrate |
| Key legislation | TUIR (DPR 917/1986); Legge di Bilancio 2026 (L. 199/2025); Codice Civile Art. 2120 (TFR) |
| INPS contribution ceiling (2026) | EUR 122,295/year (per maximale L. 335/1995) |
| Online tools | Agenzia delle Entrate -- modello F24 telematico |
| Validated by | Pending -- requires sign-off by an Italian commercialista |
| Skill version | 1.0 |

## Section 2 -- Income Tax Withholding (IRPEF)

- **IRPEF withholding mechanism** — The employer (sostituto d'imposta) withholds IRPEF monthly from the employee's gross pay after deducting INPS employee contributions. Cumulative method used.

### IRPEF Tax Brackets (2026 -- Legge di Bilancio 2026)

**IRPEF Tax Brackets (2026 -- Legge di Bilancio 2026)**

| Taxable Income (EUR, annual) | Rate |
| --- | --- |
| 0 -- 28,000 | 23% |
| 28,001 -- 50,000 | 33% |
| 50,001+ | 43% |

- **Key 2026 change** — The second bracket rate dropped from 35% to 33%, saving up to EUR 440/year for employees with income between EUR 28,000 and EUR 50,000.
- **Neutralisation mechanism for high incomes** — For incomes above EUR 200,000, a neutralisation mechanism (sterilizzazione) claws back the benefit of the 33% rate reduction.  _(Art. 1, commi 3--4, L. 199/2025)_

### Tax-Free Threshold and Detrazioni per Lavoro Dipendente

**Tax-Free Threshold and Detrazioni per Lavoro Dipendente**

| Income Range (EUR) | Detrazione (Employment Deduction) |
| --- | --- |
| Up to 8,500 (no tax area) | IRPEF = 0 (deduction fully offsets tax) |
| 8,501 -- 15,000 | EUR 1,955 (maximum) |
| 15,001 -- 50,000 | Decreasing progressively; minimum EUR 690 |
| Above 50,000 | EUR 690 fixed |

### Addizionali IRPEF (Regional and Municipal Surcharges)

**Addizionali IRPEF (Regional and Municipal Surcharges)**

| Surcharge | Rate | Notes |
| --- | --- | --- |
| Addizionale regionale | 1.23% -- 3.33% | Varies by region of residence |
| Addizionale comunale | 0% -- 0.9% | Varies by municipality; some have progressive brackets |

- **Addizionali withholding timing** — Addizionali for the prior year are withheld in monthly instalments from January to November of the current year (e.g., 2025 addizionali withheld Jan--Nov 2026). Current-year acconto may also be withheld.

## Section 3 -- Social Security -- Employee Deductions (2026)

### INPS Contributions (Employee Share)

**INPS Contributions (Employee Share)**

| Contribution | Employee Rate | Base | Notes |
| --- | --- | --- | --- |
| IVS (Invalidità, Vecchiaia, Superstiti) | 9.19% | Up to INPS ceiling | General rate for industry/commerce employees |
| IVS above ceiling | 9.19% continues but only employer pays excess | Above EUR 122,295/year | For post-1996 first-insured (L. 335/95) |
| Fondo di garanzia TFR | -- | -- | No employee share |
| CIG (Cassa Integrazione Guadagni) | -- | -- | Employer-only for most sectors |
| CIGS (for companies > 15 employees) | -- | -- | Employer-only |

- **Note on standard rate variation** — The 9.19% rate is the standard for most private-sector employees (operai and impiegati in industry and commerce). Actual rates vary by CCNL (Contratto Collettivo Nazionale di Lavoro), sector, and employee classification. Common variants below.

**Sector employee rate variants**

| Sector | Employee Rate |
| --- | --- |
| Industry (> 15 employees) | 9.19% |
| Commerce/services | 9.19% |
| Agriculture | 8.84% |
| Dirigenti (managers) | 9.19% |

### INPS Ceiling (Massimale, 2026)

**INPS Ceiling (Massimale, 2026)**

| Item | Value |
| --- | --- |
| Massimale annuo (post-1996 contributors) | EUR 122,295 |
| Minimale annuo | EUR 18,808 |

- **Massimale applicability** — The massimale applies only to workers first insured after 1 January 1996 with no prior contributions under the old system.

## Section 4 -- Social Security -- Employer Contributions (2026)

### INPS Contributions (Employer Share)

- **Total employer INPS rate range** — The total INPS rate is approximately 30--33% for the employer, depending on sector, company size, and applicable reductions. The main components are shown below.

**INPS Contributions (Employer Share)**

| Contribution | Approximate Employer Rate | Notes |
| --- | --- | --- |
| IVS (pension) | ~23.81% | Main pension contribution |
| Malattia (sickness) | 2.22% | Industry; 0% for commerce impiegati (INPS covers) |
| Maternità | 0.46% |  |
| Disoccupazione (NASpI unemployment) | 1.61% |  |
| CIG ordinaria (companies ≤ 50 employees, industry) | 1.70% | Varies by sector |
| CIGS (companies > 50 employees) | 0.90% | Additional |
| Fondo di garanzia TFR | 0.20% |  |
| CUAF (assegni familiari) | 0.68% | Family allowances |
| INAIL (accident insurance) | Variable (0.4%--12%+) | Risk-based; separate from INPS |

### Typical Total Employer Rates

**Typical Total Employer Rates**

| Sector | Approximate Total Employer Rate |
| --- | --- |
| Industry (> 50 employees) | ~31--33% |
| Industry (≤ 50 employees) | ~30--31% |
| Commerce / services | ~28--30% |
| Dirigenti | ~33--35% |

- **Application of rates and IVS above massimale** — These rates apply on gross salary without ceiling for most components. IVS above the massimale: employer pays an additional ~1% on amounts exceeding EUR 122,295 (no employee share above ceiling).

## Section 5 -- Minimum Wage and Overtime

### Minimum Wage

- **No statutory national minimum wage** — Italy has no statutory national minimum wage. Minimum pay is set by the applicable CCNL (national collective agreement) for each sector. All employers must apply the CCNL relevant to their business activity.

**CCNL Examples**

| CCNL Examples | Approximate Minimum Monthly (Level 1/Entry) |
| --- | --- |
| CCNL Commercio (commerce) | ~EUR 1,580 (14 payments, level VII) |
| CCNL Metalmeccanico (metalwork) | ~EUR 1,600 (13 payments, level 1) |
| CCNL Turismo (tourism) | ~EUR 1,350 (14 payments, level 7) |

- **CCNL minimum composition** — CCNL minimums include the base pay (paga base) + contingenza + EDR. They are updated through periodic renewals.

### Working Hours and Overtime

**Working Hours and Overtime**

| Rule | Detail |
| --- | --- |
| Legal weekly maximum | 40 hours (Art. 3, D.Lgs. 66/2003) |
| Maximum including overtime | 48 hours average over 4 months (extendable to 6 or 12 by CCNL) |
| Annual overtime cap | 250 hours (unless CCNL provides otherwise) |
| Overtime surcharges (typical CCNL) | 25% (first 2 hours/day), 30% (additional), 50% (Saturday/Sunday), 65% (public holidays) |
| Night work surcharge | 15%--30% per CCNL |

## Section 6 -- Mandatory Benefits

### Tredicesima (13th Month Salary)

**Tredicesima (13th Month Salary)**

| Entitlement | Detail |
| --- | --- |
| Amount | 1 additional month's salary |
| Accrual | 1/12 of annual salary per month worked |
| Payment | December (before Christmas) |
| Statutory | Yes -- required by law for all employees |
| Subject to IRPEF and INPS | Yes |

### Quattordicesima (14th Month Salary)

**Quattordicesima (14th Month Salary)**

| Entitlement | Detail |
| --- | --- |
| Amount | 1 additional month's salary |
| Required | Only where mandated by CCNL (e.g., Commercio, Turismo) |
| Payment | Typically June or July |

### TFR (Trattamento di Fine Rapporto)

**TFR (Trattamento di Fine Rapporto)**

| Item | Detail |
| --- | --- |
| What | Deferred compensation accrued annually, paid on termination |
| Accrual formula | Annual gross / 13.5 = annual TFR accrual |
| Revaluation | Accumulated TFR revalued annually: 1.5% + 75% of ISTAT CPI increase |
| Destination | Kept at employer, or transferred to Fondo Tesoreria INPS (≥ 60 employees in 2026--2027), or to supplementary pension fund |
| Tax treatment | Tassazione separata (separate taxation) on payment |

### Ferie (Annual Leave)

**Ferie (Annual Leave)**

| Entitlement | Detail |
| --- | --- |
| Statutory minimum | 4 weeks (20 working days on 5-day week) per D.Lgs. 66/2003 |
| Typical CCNL | 20--26 days depending on seniority |
| Non-substitutable | First 2 weeks must be consecutive; minimum 2 weeks cannot be monetised except on termination |
| Festività | 12 national public holidays (paid) |

### Sick Leave (Malattia)

**Sick Leave (Malattia)**

| Entitlement | Detail |
| --- | --- |
| INPS indennità | Days 4--180: 50% of average daily wage (days 4--20), 66.67% (days 21--180) |
| Employer top-up | Per CCNL (e.g., Commercio: 100% for days 1--3, then 75% through INPS for 180 days) |
| Waiting period | First 3 days (carenza) paid by employer per most CCNLs |
| Medical certificate | Telematic certificate sent by doctor to INPS; employer receives notification |

### Maternity Leave (Congedo di Maternità)

**Maternity Leave (Congedo di Maternità)**

| Entitlement | Detail |
| --- | --- |
| Duration | 5 months total (typically 2 months before + 3 months after birth; flexible 1+4) |
| Pay | 80% of average daily wage from INPS; many CCNLs top up to 100% |
| Parental leave (congedo parentale) | Up to 10 months per family (6 months each parent max); 30% INPS indemnity for 9 months |

### Paternity Leave (Congedo di Paternità)

**Paternity Leave (Congedo di Paternità)**

| Entitlement | Detail |
| --- | --- |
| Mandatory | 10 working days (paid at 100% by INPS) |
| Timing | Within 5 months of birth |

## Section 7 -- Payslip Requirements

- **Payslip governing law** — The busta paga (cedolino) is governed by L. 4/1953 and subsequent regulations.  _(L. 4/1953)_

### Mandatory Payslip Fields

**Mandatory Payslip Fields**

| Field | Required |
| --- | --- |
| Employer: name, address, codice fiscale, INPS position number | Yes |
| Employee: name, codice fiscale, qualifica, livello, CCNL applied | Yes |
| Pay period and payment date | Yes |
| Normal hours and overtime hours worked | Yes |
| Paga base + contingenza + EDR + other CCNL elements | Yes |
| Gross pay (retribuzione lorda) | Yes |
| INPS employee contributions (detail) | Yes |
| IRPEF withheld | Yes |
| Addizionali regionali and comunali withheld | Yes |
| Detrazioni per lavoro dipendente applied | Yes |
| TFR accrual for the period | Yes (or annual statement) |
| Net pay (netto in busta) | Yes |
| Ferie maturate, godute, residue (leave accrued/used/remaining) | Yes |
| ROL/Permessi (paid leave hours) accrued/used/remaining | Yes |

### Delivery

- Paper or electronic (with employee consent)
- Employer must retain for 5 years
- CU (Certificazione Unica) serves as the annual summary document

## Section 8 -- Filing Obligations

### Monthly

**Monthly filing obligations**

| Obligation | Deadline | Method |
| --- | --- | --- |
| F24 payment (INPS contributions + IRPEF + addizionali) | 16th of the following month | Telematic F24 via Agenzia delle Entrate |
| UniEmens (INPS monthly declaration) | Last day of the following month | Telematic via INPS |

### Annual

**Annual filing obligations**

| Obligation | Deadline | Notes |
| --- | --- | --- |
| CU (Certificazione Unica) -- employment income | 16 March of following year | Telematic to Agenzia delle Entrate; copy to employee |
| CU -- self-employment income | 30 April of following year |  |
| Modello 770 (withholding agent annual return) | 31 October of following year | Reconciliation of all withholdings |
| Autoliquidazione INAIL | 16 February (payment) + 28 February (declaration) | Annual accident insurance settlement |

### Employee Obligations

**Employee Obligations**

| Item | Detail |
| --- | --- |
| Modello 730 (assisted tax return) | Submission windows: April -- September; employer/CAF processes refund/debit in July--November payroll |
| Modello Redditi PF | Alternative to 730; deadline 30 November |

## Section 9 -- Common Payroll Patterns

### Typical Bank Statement Descriptions (Salary Credits)

**Typical Bank Statement Descriptions (Salary Credits)**

| Pattern | Classification |
| --- | --- |
| STIPENDIO, EMOLUMENTI, BUSTA PAGA | Net salary payment |
| TREDICESIMA, 13A MENSILITA | 13th month salary |
| QUATTORDICESIMA, 14A MENSILITA | 14th month salary (if applicable) |
| TFR, LIQUIDAZIONE | TFR payment on termination |
| INDENNITA MALATTIA INPS | Sickness indemnity (from INPS, may transit through employer) |
| INDENNITA MATERNITA | Maternity indemnity |
| RIMBORSO 730 | Modello 730 tax refund processed through payroll |

### Typical Employer Debit Patterns

**Typical Employer Debit Patterns**

| Pattern | Classification |
| --- | --- |
| F24 INPS, CONTRIBUTI INPS | INPS contribution payment |
| F24 IRPEF, RITENUTE | IRPEF + addizionali payment |
| INAIL PREMIO | Accident insurance premium |
| FONDO TESORERIA INPS | TFR transfer to INPS fund |
| FONDO PENSIONE [NAME] | Supplementary pension fund contribution |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (IRPEF + INPS) | **This skill (italy-payroll.md)** |
| Self-employed income tax | italy-income-tax.md |
| Italian VAT (IVA) | italy-vat-return.md |
| Bookkeeping | italy-bookkeeping.md |
| E-invoicing (FatturaPA / SDI) | italy-einvoice.md |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages + employer INPS + INAIL + TFR accrual are P&L expenses. Employee IRPEF, addizionali, and INPS deductions are liabilities (debiti verso erario / debiti verso INPS) until F24 payment. TFR is a liability (fondo TFR) until paid or transferred.
- **Payroll → Income Tax:** CU data feeds into the employee's Modello 730 or Redditi PF. The sostituto d'imposta processes 730 refunds/debits in monthly payroll (July--November).
- **Payroll → INPS:** UniEmens monthly submissions reconcile with F24 payments. Annual CU data must match UniEmens totals.

## PROHIBITIONS

- NEVER apply a flat tax rate -- Italy uses progressive IRPEF brackets with detrazioni
- NEVER forget addizionali regionali and comunali -- they are separate from IRPEF and vary by residence
- NEVER omit the tredicesima (13th month) -- it is legally required for all employees
- NEVER confuse the INPS massimale (EUR 122,295) with a general salary cap -- it only affects post-1996 contributors
- NEVER compute TFR without the Art. 2120 formula (gross / 13.5 + revaluation)
- NEVER miss the F24 deadline (16th of the month) -- penalties and interest apply immediately
- NEVER issue a busta paga without all mandatory fields per L. 4/1953
- NEVER assume a national minimum wage exists -- use the applicable CCNL
- NEVER present payroll computations as definitive -- direct to a commercialista or consulente del lavoro for sign-off

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista or consulente del lavoro in Italy) before implementation.

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
