---
name: germany-payroll
description: Use this skill whenever asked about German payroll processing for employees. Trigger on phrases like "German payroll", "Lohnsteuer", "Gehaltsabrechnung", "Brutto Netto Rechner", "Steuerklasse", "Sozialversicherung", "Arbeitnehmeranteil", "Arbeitgeberanteil", "Beitragsbemessungsgrenze", "payslip Germany", "Lohnabrechnung", "Nettolohn", "Solidaritätszuschlag", "Kirchensteuer", "Rentenversicherung", "Krankenversicherung", "Pflegeversicherung", "Arbeitslosenversicherung", "Minijob", "Midijob", "minimum wage Germany", "Mindestlohn", "Entgeltabrechnung", or any question about computing employee pay, withholding tax, or social contributions in Germany. This skill extends de-payroll.md with full payroll lifecycle coverage including mandatory benefits, payslip requirements, filing obligations, and employer cost analysis. ALWAYS read this skill before processing any German employee payroll.
version: 1.0
jurisdiction: DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany Payroll

## Germany Payroll Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Germany (Bundesrepublik Deutschland) |
| Currency | EUR only |
| Standard pay frequency | Monthly (Monat) -- dominant; weekly/daily possible |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding | Lohnsteuer (LSt) via BMF Programmablaufplan (PAP) |
| Surcharges | Solidaritätszuschlag (5.5% of LSt, with Freigrenze); Kirchensteuer (8% or 9% of LSt) |
| Social insurance | Rentenversicherung (RV), Krankenversicherung (KV), Pflegeversicherung (PV), Arbeitslosenversicherung (AV) |
| Tax authority | Finanzamt (local tax office); BZSt (Federal Central Tax Office for ELStAM) |
| Social insurance authority | Krankenkasse (health fund) collects all SV contributions |
| Key legislation | EStG §§38--42f; SolZG; SGB IV/V/VI/XI; GewO §108 (payslip); MiLoG (minimum wage) |
| BMF PAP 2026 | Published 12.11.2025 by BMF |
| Online calculator | [bmf-steuerrechner.de](https://www.bmf-steuerrechner.de) |
| Validated by | Pending -- requires sign-off by a German Steuerberater |
| Skill version | 1.0 |

## Section 2 -- Income Tax Withholding (Lohnsteuer)

### Tax Brackets (2026 PAP, Grundtarif)

**Tax Brackets (2026 PAP, Grundtarif)**

| Taxable Income (EUR, annual) | Rate | PAP Zone |
| --- | --- | --- |
| 0 -- 12,348 | 0% | Grundfreibetrag |
| 12,349 -- ~17,500 | 14% -- ~24% | Progressive zone 1 |
| ~17,501 -- ~68,500 | ~24% -- 42% | Progressive zone 2 |
| ~68,501 -- 277,825 | 42% | Proportionalzone |
| 277,826+ | 45% | Reichensteuer |

- **PAP formula usage** — Germany uses the BMF PAP formula (not simple brackets). The PAP annualises the pay period, computes annual tax, then divides back. See de-payroll.md Section 3 for the exact UPTAB formula.  _(de-payroll.md Section 3)_

### Steuerklassen (Tax Classes)

**Steuerklassen (Tax Classes)**

| Class | Who | Key Feature |
| --- | --- | --- |
| I | Single, divorced, widowed | Grundtarif |
| II | Single parent | Grundtarif + Entlastungsbetrag (EUR 4,260) |
| III | Married, sole/higher earner | Splittingverfahren (KZTAB=2) |
| IV | Married, both earning similarly | Grundtarif (with optional Faktor) |
| V | Married, lower earner | Special MST5_6 method, no allowances |
| VI | Second employment | No Pauschbeträge, highest withholding |

### Solidaritätszuschlag (2026)

**Solidaritätszuschlag (2026)**

| Item | Value |
| --- | --- |
| Rate | 5.5% of Lohnsteuer |
| Freigrenze (Stkl I/II/IV/V/VI) | Annual LSt up to EUR ~20,500 → SolZ = 0 |
| Freigrenze (Stkl III) | Annual LSt up to EUR ~41,000 → SolZ = 0 |
| Phase-in (Gleitzone) | 11.9% marginal rate above Freigrenze |

### Kirchensteuer

**Kirchensteuer**

| Land | Rate |
| --- | --- |
| Bavaria, Baden-Württemberg | 8% of Lohnsteuer |
| All other Länder | 9% of Lohnsteuer |
| Applies only if | Employee is a registered church member (R > 0 in ELStAM) |

## Section 3 -- Social Security -- Employee Deductions (2026)

### Contribution Rates and Ceilings

**Contribution Rates and Ceilings**

| Branch | German Name | Employee Rate | Monthly Ceiling | Max Employee/Month |
| --- | --- | --- | --- | --- |
| Pension | Rentenversicherung (RV) | 9.30% | EUR 8,450 | EUR 785.85 |
| Health | Krankenversicherung (KV) | 7.30% + ZB/2 | EUR 5,812.50 | varies |
| Care | Pflegeversicherung (PV) | see table below | EUR 5,812.50 | varies |
| Unemployment | Arbeitslosenversicherung (AV) | 1.30% | EUR 8,450 | EUR 109.85 |

- **Average Zusatzbeitrag 2026** — Average Zusatzbeitrag (ZB) for 2026: 2.90% (varies by Krankenkasse). Employee KV = 7.30% + 1.45% = 8.75%.

### Pflegeversicherung Employee Rates (2026)

**Pflegeversicherung Employee Rates (2026)**

| Situation | Employee Rate | Notes |
| --- | --- | --- |
| Childless, age 23+ | 2.40% | Kinderlosenzuschlag of 0.60% |
| 1 child | 1.80% | Base rate |
| 2 children | 1.55% | Beitragsabschlag 0.25% |
| 3 children | 1.30% | Beitragsabschlag 0.50% |
| 4 children | 1.05% | Beitragsabschlag 0.75% |
| 5+ children | 0.80% | Beitragsabschlag 1.00% |
| Sachsen exception | +0.50% on all above | Buß- und Bettag adjustment |

### Beitragsbemessungsgrenzen (2026)

**Beitragsbemessungsgrenzen (2026)**

| Ceiling | Monthly | Annual | Applies To |
| --- | --- | --- | --- |
| KV/PV-BBG | EUR 5,812.50 | EUR 69,750 | Health + Care |
| RV/AV-BBG | EUR 8,450.00 | EUR 101,400 | Pension + Unemployment |
| JAEG (Versicherungspflichtgrenze) | EUR 6,450.00 | EUR 77,400 | Threshold for PKV opt-out |

## Section 4 -- Social Security -- Employer Contributions (2026)

### Employer Rates and Ceilings

**Employer Rates and Ceilings**

| Branch | Employer Rate | Monthly Ceiling | Max Employer/Month |
| --- | --- | --- | --- |
| Pension (RV) | 9.30% | EUR 8,450 | EUR 785.85 |
| Health (KV) | 7.30% + ZB/2 | EUR 5,812.50 | varies |
| Care (PV) | 1.80% | EUR 5,812.50 | EUR 104.63 |
| Unemployment (AV) | 1.30% | EUR 8,450 | EUR 109.85 |

- **PV employer rate Sachsen exception** — PV employer rate is 1.80% in all Länder except Sachsen (1.30% in Sachsen; employee pays the extra 0.50%).

### Employer-Only Contributions (not deducted from employee)

**Employer-Only Contributions (not deducted from employee)**

| Contribution | Rate | Base |
| --- | --- | --- |
| Umlage U1 (sick pay, < 30 employees) | 0.9% -- 4.1% (varies by Krankenkasse) | Gross up to KV-BBG |
| Umlage U2 (maternity) | 0.19% -- 0.8% (varies) | Gross up to KV-BBG |
| Insolvenzgeldumlage | 0.06% | Gross up to RV-BBG |
| Berufsgenossenschaft (accident insurance) | varies by industry (0.5% -- 10%+) | Gross (industry-specific ceiling) |

### Total Employer Cost Estimate (average employee, EUR 4,500/month gross)

**Total Employer Cost Estimate (average employee, EUR 4,500/month gross)**

| Item | Amount |
| --- | --- |
| Employer SV (RV+KV+PV+AV) | ~EUR 953 |
| Umlagen (U1+U2+Insolvenz) | ~EUR 50--70 |
| Berufsgenossenschaft | varies |
| **Total employer add-on** | **~21--25% of gross** |

## Section 5 -- Minimum Wage and Overtime

### Minimum Wage (Mindestlohn, 2026)

**Minimum Wage (Mindestlohn, 2026)**

| Item | Value |
| --- | --- |
| Statutory minimum | EUR 13.90 per hour |
| Minijob threshold | EUR 603 per month |
| Midijob (Übergangsbereich) | EUR 603.01 -- EUR 2,000 per month |

### Working Hours and Overtime

**Working Hours and Overtime**

| Rule | Detail |
| --- | --- |
| Standard weekly hours | No statutory standard; typically 35--40 hours per employment contract/collective agreement |
| Maximum daily hours | 8 hours (ArbZG §3); extendable to 10 hours if averaged to 8 over 6 months |
| Maximum weekly hours | 48 hours (6 x 8); extendable to 60 hours with compensatory rest |
| Overtime regulation | Not federally mandated beyond ArbZG limits; overtime pay and surcharges governed by Tarifvertrag (collective agreement) or individual contract |
| Typical overtime surcharges | 25% (weekday), 50% (Saturday/Sunday), 100% (public holidays) -- per collective agreements |
| Tax treatment of surcharges | Night work (20:00--06:00) surcharges up to 25% of Grundlohn are tax-free per §3b EStG; Sunday 50% tax-free; public holiday 125--150% tax-free |

## Section 6 -- Mandatory Benefits

### Annual Leave (Bundesurlaubsgesetz)

**Annual Leave (Bundesurlaubsgesetz)**

| Entitlement | Detail |
| --- | --- |
| Minimum statutory | 20 working days (based on 5-day week); 24 days (based on 6-day week) |
| Typical contractual | 25--30 days |
| Carry-over | Must be used by 31 March of following year (§7(3) BUrlG) |

### Sick Leave (Entgeltfortzahlungsgesetz)

**Sick Leave (Entgeltfortzahlungsgesetz)**

| Entitlement | Detail |
| --- | --- |
| Employer-paid sick leave | 6 weeks (42 calendar days) at full pay per illness per year |
| After 6 weeks | Krankengeld from Krankenkasse (~70% of gross, max 90% of net) for up to 78 weeks |
| Medical certificate | Required from day 4 of absence (employer may require from day 1) |

### Maternity Leave (Mutterschutzgesetz)

**Maternity Leave (Mutterschutzgesetz)**

| Entitlement | Detail |
| --- | --- |
| Pre-birth protection | 6 weeks before expected due date (voluntary opt-out possible) |
| Post-birth protection | 8 weeks mandatory (12 weeks for premature/multiple births) |
| Pay | Mutterschaftsgeld from Krankenkasse (EUR 13/day) + employer top-up to full net salary |

### Parental Leave (Elternzeit, BEEG)

**Parental Leave (Elternzeit, BEEG)**

| Entitlement | Detail |
| --- | --- |
| Duration | Up to 3 years per parent (per child) |
| Elterngeld | 65--67% of net income, EUR 300--1,800/month, for 12 months (+2 partner months) |
| ElterngeldPlus | 50% of Elterngeld for up to 24 months |

### 13th Month / Christmas Bonus

No statutory obligation. Commonly paid per Tarifvertrag or employment contract (Weihnachtsgeld, typically 50--100% of monthly salary).

## Section 7 -- Payslip Requirements

German employers must provide an itemised payslip (Entgeltabrechnung/Lohnabrechnung) per §108 GewO.

### Mandatory Payslip Fields

**Mandatory Payslip Fields**  _(§108 GewO)_

| Field | Required |
| --- | --- |
| Employee name, address, tax ID | Yes |
| Pay period | Yes |
| Steuerklasse and Kirchensteuermerkmale | Yes |
| Bruttolohn (gross salary) | Yes |
| Lohnsteuer withheld | Yes |
| Solidaritätszuschlag withheld | Yes |
| Kirchensteuer withheld (if applicable) | Yes |
| Employee SV contributions (RV, KV, PV, AV -- each separately) | Yes |
| Zusatzbeitrag rate (KV) | Yes |
| Nettolohn (net salary) | Yes |
| Employer SV contributions (informational) | Recommended |
| Hours worked / overtime | Yes (if relevant to pay) |
| Deductions (Vorschüsse, Pfändungen, VWL, bAV) | Yes |

### Delivery

- Paper or secure electronic format
- Retention: employer must keep payroll records for minimum 6 years (tax) / 10 years (social security)

## Section 8 -- Filing Obligations

### Monthly

**Monthly**

| Obligation | Deadline | To Whom |
| --- | --- | --- |
| Lohnsteuer-Anmeldung (wage tax return) | 10th of following month | Finanzamt (ELSTER) |
| SV-Beitragsnachweise (contribution statements) | 2nd-to-last working day of current month (estimated) | Krankenkasse (via SV-Meldungen) |
| SV payment | 5th-to-last working day of current month (draft debit) | Krankenkasse |
| DSN-equivalent: DEÜV-Meldungen | Monthly with payroll | Deutsche Rentenversicherung via Krankenkasse |

### Annual

**Annual**

| Obligation | Deadline | Notes |
| --- | --- | --- |
| Lohnsteuerbescheinigung | By 28 February of following year | Electronic transmission to Finanzamt; copy to employee |
| Jahresmeldung (SV annual notification) | By 15 February of following year | To Krankenkasse |
| Lohnsteuer-Jahresausgleich (employer) | Optional; December payroll | §42b EStG; employer may reconcile withholding |

### Employee Income Tax Return

**Employee Income Tax Return**

| Scenario | Deadline |
| --- | --- |
| Mandatory filers (e.g., Stkl III/V combination) | 31 July of following year |
| With Steuerberater | 31 December of following year (may be extended) |
| Voluntary filers | Up to 4 years retroactively |

## Section 9 -- Common Payroll Patterns

### Typical Bank Statement Descriptions (Salary Credits)

**Typical Bank Statement Descriptions (Salary Credits)**

| Pattern | Classification |
| --- | --- |
| GEHALT, LOHN, ENTGELT, NETTOBEZUG | Net salary payment |
| NACHZAHLUNG GEHALT | Salary back-payment (sonstige Bezüge rules may apply) |
| WEIHNACHTSGELD, 13. GEHALT | Christmas bonus / 13th salary |
| URLAUBSGELD | Holiday bonus |
| ABFINDUNG | Severance (Fünftelregelung may apply) |
| ELTERNGELD | Parental allowance (not from employer -- from state) |
| KRANKENGELD | Sick pay from Krankenkasse (not taxable as wages) |

### Typical Employer Debit Patterns

**Typical Employer Debit Patterns**

| Pattern | Classification |
| --- | --- |
| FINANZAMT LST, LOHNSTEUER | Wage tax + SolZ + KiSt remittance |
| [KRANKENKASSE NAME] SV-BEITRAG | Social insurance contributions |
| BG BEITRAG, BERUFSGENOSSENSCHAFT | Accident insurance premium |
| UMLAGE U1 U2 | Sick pay / maternity Umlagen |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (Lohnsteuer + SV) | **This skill (germany-payroll.md)** |
| Detailed PAP formula and worked examples | de-payroll.md |
| Self-employed income tax (Einkommensteuer) | de-income-tax.md |
| Self-employed social contributions | de-social-contributions.md |
| Gewerbesteuer (trade tax) | de-trade-tax.md |
| Umsatzsteuer / VAT | germany-vat-return.md |
| Bookkeeping | germany-bookkeeping.md |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages + employer SV are P&L expenses. LSt/SolZ/KiSt and employee SV are payroll liabilities (Verbindlichkeiten) until remitted. Employer SV is booked to Sozialaufwendungen.
- **Payroll → Income Tax:** Lohnsteuerbescheinigung feeds into the employee's Einkommensteuererklärung. The PAP computation in de-payroll.md is the reference for validating withholding amounts.
- **Payroll → SV:** Beitragsnachweise and DEÜV-Meldungen must reconcile with payslip amounts. The Krankenkasse collects all four branches centrally.

## PROHIBITIONS

- **PAP formula required** — NEVER compute Lohnsteuer without the BMF PAP formula -- simple bracket percentages are wrong
- **BBG confusion** — NEVER confuse KV/PV-BBG (EUR 5,812.50/month) with RV/AV-BBG (EUR 8,450/month)
- **Childless PV surcharge misapplication** — NEVER apply childless PV surcharge to employees with children
- **SV above BBG** — NEVER charge SV contributions above the Beitragsbemessungsgrenze
- **Sachsen PV exception** — NEVER omit the Sachsen PV exception
- **Minijob standard payroll treatment** — NEVER treat Minijobs (≤ EUR 603/month) as standard payroll -- different rules apply
- **Kirchensteuer rate assumption** — NEVER assume Kirchensteuer is 9% everywhere -- Bavaria and Baden-Württemberg use 8%
- **Employer-only costs omission** — NEVER forget employer-only costs (Umlagen, BG, Insolvenzgeldumlage) when computing total cost
- **Payslip field omission** — NEVER issue a payslip missing any field required by §108 GewO  _(§108 GewO)_
- **Definitive presentation prohibition** — NEVER present payroll computations as definitive -- direct to Steuerberater/Lohnbuchhalter for sign-off

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or Lohnbuchhalter in Germany) before implementation.

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
