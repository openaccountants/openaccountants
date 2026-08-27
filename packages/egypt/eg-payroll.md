---
name: eg-payroll
description: Use this skill whenever asked about running payroll for an employer in Egypt, including a sole proprietor who hires staff. Trigger on phrases like "Egypt payroll", "salary tax Egypt", "ضريبة كسب العمل", "payroll tax Egypt", "hiring employees Egypt", "withholding tax on salaries Egypt", "Form 4 Egypt", "نموذج 4", "gross to net salary Egypt", "employer cost Egypt", "end of service Egypt", "employee vs freelancer Egypt", or any request to compute, classify, or advise on Egyptian salary tax (employment income tax) withholding, social-insurance withholding, payroll remittance, or payroll reporting. ALWAYS read this skill before touching any Egypt payroll work.
version: 1.0
jurisdiction: EG
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Payroll

## Egypt Payroll (ضريبة كسب العمل) Skill v1.0

Payroll in Egypt combines two distinct employer obligations on each salary:

1. **Salary / employment income tax** (ضريبة كسب العمل) — withheld monthly from the employee's pay under the **Unified Tax Law No. 91 of 2005** (and its later amendments), administered by the **Egyptian Tax Authority — ETA** (مصلحة الضرائب المصرية, eta.gov.eg).
2. **Social insurance** (التأمينات الاجتماعية) — both an employee share withheld and an employer share, under **Law No. 148 of 2019**, administered by **NOSI** (الهيئة القومية للتأمين الاجتماعي). See companion skill **eg-social-insurance** for the full computation; this skill only cross-references it.

This skill is written for an **employer** running monthly payroll — including a sole proprietor (منشأة فردية) who employs staff. The owner's own tax sits in **eg-income-tax**; the owner's own social insurance sits in **eg-social-insurance**.

> Reply to the user **in their language**. Use English prose with native Arabic terms where useful. All amounts are in Egyptian Pounds (EGP / ج.م).

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Egypt (جمهورية مصر العربية) |
| Payroll taxes | Salary tax (ضريبة كسب العمل) + social insurance (التأمينات) |
| Currency | EGP (Egyptian Pound — ج.م) |
| Tax authority | Egyptian Tax Authority (**ETA** — مصلحة الضرائب المصرية, eta.gov.eg) |
| Social-insurance authority | National Organization for Social Insurance (**NOSI**) |
| **Annual personal exemption** | **EGP 20,000** per employee (residents and non-residents) — *verify current value* |
| Salary-tax basis | Annual taxable employment income after the exemption, on progressive brackets, withheld in monthly instalments |
| **Social insurance — employee** | **11%** of the insurance wage (الأجر التأميني) |
| **Social insurance — employer** | **18.75%** of the insurance wage |
| **Min monthly insurance wage 2026** | **EGP 2,700** (from 1 Jan 2026) — *verify* |
| **Max monthly insurance wage 2026** | **EGP 16,700** (from 1 Jan 2026) — *verify* |
| Salary-tax remittance deadline | by the **15th of the month following** the payroll month |
| Social-insurance deadline | by the **15th of the month following** the payroll month |
| Periodic return | **Form 4** (نموذج ٤) salary-tax declaration filed with ETA |
| Annual reconciliation | annual salary-tax settlement/reconciliation filed by **end of January** of the following year — *verify exact form/deadline* |
| Late / non-compliance penalty | up to ~**80%** of unpaid tax plus delay interest — *verify current rate* |
| Quality tier | **Research-verified — pending sign-off by an Egyptian accountant** |
| Skill version | 1.0 |

### 2025/2026 salary-tax brackets (annual taxable income, after EGP 20,000 exemption)

**2025/2026 salary-tax brackets**

| Annual taxable income (EGP) | Rate |
| --- | --- |
| 1 – 40,000 | **0%** |
| 40,000 – 55,000 | **10%** |
| 55,000 – 70,000 | **15%** |
| 70,000 – 200,000 | **20%** |
| 200,000 – 400,000 | **22.5%** |
| 400,000 – 1,200,000 | **25%** |
| over 1,200,000 | **27.5%** |

These are the brackets in force for 2025 and carried into 2026 (apply each rate only to the slice of income inside the band):

> *Verify 2026 brackets against ETA / PwC before filing — Egypt has revised these several times since 2023. If a 2026 update has changed the bands or rates, use the published figures and flag the change.*

### Bracket-elimination rule (higher earners lose the lower brackets)

**Bracket-elimination thresholds**

| Total annual net income (EGP) | Brackets that no longer apply |
| --- | --- |
| up to 600,000 | all brackets apply (full 0% band) |
| 600,000 – 700,000 | **0% band removed** — taxation starts at 10% |
| 700,000 – 800,000 | 0% and 10% removed — starts at 15% |
| 800,000 – 900,000 | 0%, 10%, 15% removed — starts at 20% |
| 900,000 – 1,200,000 | 0%, 10%, 15%, 20% removed — starts at 22.5% |
| over 1,200,000 | all lower bands removed — 25% then 27.5% apply |

As **total annual net income** rises, the lowest brackets are progressively **removed** so that high earners do not benefit from the 0%/low bands. The commonly published thresholds are:

> *Verify the exact elimination thresholds for 2026 — these are tied to the same reform as the brackets above and may move together.*

### Conservative defaults

- **Worker status uncertain** — treat as an employee (subject to salary tax and social insurance), not a freelancer. Misclassification risk sits with the employer. See Section 5.
- **Residency uncertain** — withhold using resident brackets but flag for review; do not assume a treaty rate without documentation.
- **Insurance wage uncertain** — use the statutory floor/ceiling band (min 2,700, max 16,700 for 2026), not the cash salary, and flag the difference.
- **Benefit-in-kind taxability uncertain** — treat as taxable salary and flag.
- **Bracket figures uncertain** — present the formula and rates with "verify current value" rather than inventing a number.

When a fact is missing or ambiguous, the skill must choose the option that does **not** under-withhold tax or under-contribute social insurance:

## Section 2 — Required inputs & refusal catalogue

### Required inputs (ask only for what is missing)

- **Employer details** — legal form (sole proprietor / company), ETA tax file number, NOSI employer registration number.
- **Per employee** — gross monthly salary, breakdown into basic (الأجر الأساسي) and variable (الأجر المتغير) where relevant, fixed allowances, variable allowances/bonuses, benefits in kind, residency status, social-insurance registration status and the agreed insurance wage.
- **Pay frequency** — Egypt is monthly in almost all cases; and the payroll month.
- **Pre-tax deductible items** — employee social-insurance share, approved private pension/insurance within statutory caps, union dues, and any other legally deductible item.
- **Year-to-date figures** — if mid-year, so cumulative tax and the bracket-elimination test are applied correctly.

### Refusals (R-EG-PAY)

- **R-EG-PAY-1** — No filing without authority figures. If 2026 brackets, the exemption, or the insurance wage band cannot be verified, output the method and rates with "verify current value"; do not assert a final tax due as filed.  _(R-EG-PAY-1)_
- **R-EG-PAY-2** — No worker-status laundering. Refuse to classify a genuine employee as a freelancer/contractor purely to avoid salary tax or social insurance. Explain the substance-over-form test instead (Section 5).  _(R-EG-PAY-2)_
- **R-EG-PAY-3** — No under-the-table payroll. Refuse to design schemes that split salary into untaxed cash, sham allowances, or off-book payments to reduce withholding or contributions.  _(R-EG-PAY-3)_
- **R-EG-PAY-4** — No insurance-wage understatement. Refuse to set the insurance wage below the statutory minimum or below the genuine wage to cut the employer share.  _(R-EG-PAY-4)_
- **R-EG-PAY-5** — Not legal/labour advice. End-of-service, termination, and contract questions are summarised for context only; refer disputes to an Egyptian labour lawyer and the Labour Law No. 14 of 2025.  _(R-EG-PAY-5)_
- **R-EG-PAY-6** — Reviewer sign-off required. All output is research-grade and must be reviewed by a qualified Egyptian accountant before filing or payment.  _(R-EG-PAY-6)_

## Section 3 — Gross-to-net + employer-cost computation

### Step order (per employee, per month)

- **Step 1 — Insurance wage** — Determine the insurance wage (الأجر التأميني). Clamp the salary to the monthly band: not below EGP 2,700, not above EGP 16,700 (2026). See eg-social-insurance for the basic/variable split and any sub-caps.
- **Step 2 — Employee SI share** — Employee social-insurance share = 11% × insurance wage. This is deducted before computing taxable salary (social-insurance contributions are deductible for salary-tax purposes).
- **Step 3 — Monthly taxable salary** — Compute monthly taxable salary = gross taxable cash + taxable benefits in kind − employee SI share − other statutory pre-tax deductions − (annual exemption ÷ 12).
- **Step 4 — Annualise and apply brackets** — Annualise taxable salary, apply the bracket-elimination test on total annual net income, then the progressive brackets to get annual salary tax.
- **Step 5 — Monthly withholding** — Monthly salary tax withheld ≈ annual salary tax ÷ 12 (reconciled annually). For variable pay, recompute on a cumulative year-to-date basis.
- **Step 6 — Net pay** — Net pay = gross − employee SI share − salary tax withheld.
- **Step 7 — Employer cost** — Employer cost = gross + employer SI share (18.75% × insurance wage). (Salary tax is the employee's money the employer merely withholds and remits; it is not an extra employer cost.)

### Worked example (single employee, full year, EGP)

Employee gross salary **EGP 20,000/month** → **EGP 240,000/year**.
Assume the whole salary counts as the insurance wage but is capped at the 2026 ceiling of **EGP 16,700/month**.

**Social insurance**
- Insurance wage (capped) = **16,700/month**
- Employee share 11% = **1,837/month** → **22,044/year**
- Employer share 18.75% = **3,131.25/month** → **37,575/year**

**Salary tax**
- Annual cash salary = 240,000
- Less employee SI share = −22,044
- Less annual personal exemption = −20,000
- **Annual taxable income ≈ 197,956**
- Total net income < 600,000 → **no bracket elimination**, full bands apply:
  - 0–40,000 @ 0% = 0
  - 40,000–55,000 @ 10% = 1,500
  - 55,000–70,000 @ 15% = 2,250
  - 70,000–197,956 @ 20% = 25,591
  - **Annual salary tax ≈ 29,341** → **≈ 2,445/month withheld**

**Monthly result for this employee**
- Net pay ≈ 20,000 − 1,837 − 2,445 = **EGP 15,718**
- Total employer monthly cost ≈ 20,000 + 3,131 = **EGP 23,131**

> All figures rounded for illustration; recompute precisely and *verify the 2026 brackets, exemption, and insurance band* before filing.

## Section 4 — Reporting & remittance calendar

### Monthly (every payroll month)

- **Withhold** — Withhold salary tax and the employee SI share from each salary.
- **Remit salary tax to ETA** — by the 15th of the following month, together with the salary-tax declaration. Egypt's salary withholding is reported on the ETA system; many employers file the periodic salary-tax return monthly.
- **Remit social insurance to NOSI** — (employee 11% + employer 18.75%) by the 15th of the following month. See eg-social-insurance for the NOSI form.

### Periodic / annual — Form 4 (نموذج ٤) and reconciliation

- **Form 4 (نموذج ٤)** — is the salary-tax declaration listing each employee, their taxable income, and the tax withheld. Depending on registration it is filed monthly or quarterly with ETA — *verify the filer's required frequency*.
- **Annual reconciliation / settlement** — of salary tax is filed by the end of January of the following year, reconciling total salaries paid, exemptions, tax withheld, and tax due across the year. *Verify the exact form number and deadline against ETA for 2026.*

### Penalties

- **Late or short payment** — delay interest plus penalties that can reach up to ~80% of the unpaid tax for non-compliance — *verify current rates*.
- **Late NOSI contributions** — penalty linked to the treasury-bill average rate + 2% — see eg-social-insurance.

> **Tax-year nuance:** salary tax accrues monthly but is *settled annually*. Late joiners, leavers, and variable pay must be reconciled at year-end so total withheld matches the annual progressive computation.

## Section 5 — Employee vs freelancer (موظف مقابل عامل مستقل)

- **Employee vs contractor distinction** — The distinction drives the entire payroll obligation. An employee triggers salary-tax withholding (ضريبة كسب العمل) and social insurance; an independent contractor / freelancer generally invoices, may charge VAT, handles their own income tax (see eg-income-tax / eg-sme-tax), and is not on the employer's payroll or NOSI as an employee.

### Substance-over-form indicators (point to **employee**)

- **Direction and supervision** — Works under the employer's direction, hours, and supervision.
- **Integration** — Integrated into the organisation; uses employer tools/premises.
- **Fixed salary** — Paid a regular fixed salary rather than per deliverable/invoice.
- **Exclusivity** — Exclusive or near-exclusive to one payer; no own business risk.
- **Employer liability** — Employer bears liability for the worker's mistakes (vicarious liability).

### Indicators (point to **independent contractor**)

- **Civil-law engagement** — Fixed-term/project engagement governed by civil law (Law 131/1948), not the Labour Law; bears own risk and liability for own errors.  _(Law 131/1948)_
- **Multiple clients** — Multiple clients, own tools, issues invoices, controls how/when work is done.
- **Own tax registration** — Registered for their own tax/VAT where applicable.

> **Rule:** classify on **substance, not the contract label**. Where indicators conflict or status is unclear, **default to employee** (R-EG-PAY-2) and flag for reviewer judgement. Misclassification exposes the employer to back salary tax, back social insurance, penalties, and labour-law claims under the new **Labour Law No. 14 of 2025** (effective 1 Sept 2025).

### End-of-service (نهاية الخدمة) — context only

Under Labour Law No. 14 of 2025, end-of-service entitlements depend on the termination cause and tenure (e.g. gratuity on early termination of fixed-term contracts, retirement gratuity of half a month's pay per year for the first five years and a full month thereafter where not covered by social insurance, and enhanced severance for economic/structural redundancies). These are **labour-law entitlements**, not payroll-tax items. Treat end-of-service payments as taxable salary unless a specific exemption applies, and refer disputes to an Egyptian labour lawyer (R-EG-PAY-5). *Verify the precise formulas against the current law.*

## Section 6 — Worked examples

### Example A — Low earner at the floor

Gross **EGP 4,000/month** (48,000/year). Insurance wage = 4,000 (above the 2,700 floor, below ceiling).
- Employee SI 11% = 440/month.
- Annual taxable = 48,000 − (440×12) − 20,000 = **22,720**.
- Falls entirely in the **0% band** → **salary tax = 0**.
- Net ≈ 4,000 − 440 = **EGP 3,560**; employer cost ≈ 4,000 + 750 = **EGP 4,750**.

### Example B — Mid earner with a bonus

Gross **EGP 12,000/month**, plus a one-off **EGP 24,000** annual bonus → annual cash 168,000. Insurance wage = 12,000 (below ceiling).
- Employee SI 11% = 1,320/month → 15,840/year.
- Annual taxable = 168,000 − 15,840 − 20,000 = **132,160**.
- < 600,000 → full bands: 0 (0–40k) + 1,500 (10%) + 2,250 (15%) + 12,432 ([70,000–132,160] @ 20%) = **≈ 16,182 annual salary tax**.
- The bonus month carries extra cumulative tax; reconcile YTD so the year totals match. Employer SI = 18.75% × 12,000 = 2,250/month.

### Example C — High earner, bracket elimination

Gross **EGP 80,000/month** → 960,000/year. Insurance wage capped at 16,700.
- Employee SI 11% × 16,700 = 1,837/month → 22,044/year.
- Annual taxable ≈ 960,000 − 22,044 − 20,000 = **917,956**.
- Total net income **900,000–1,200,000 → 0%/10%/15%/20% bands eliminated**; taxation effectively starts at **22.5%** (then 25%). Apply the eliminated-band schedule to the full taxable amount. **This raises effective tax sharply vs a naive bracket read** — *verify the elimination thresholds for 2026*.

### Example D — Sole proprietor hiring one assistant

Owner is a sole proprietor (own tax via **eg-income-tax**). Hires an assistant at **EGP 8,000/month**.
- Register as an employer with NOSI; register the employee.
- Withhold employee SI 11% × 8,000 = 880; pay employer SI 18.75% × 8,000 = 1,500.
- Salary tax: annual taxable = 96,000 − 10,560 − 20,000 = **65,440** → 0 (0–40k) + 1,500 (10%) + 1,566 ([55,000–65,440] @ 15%) = **≈ 3,066/year ≈ 256/month**.
- File **Form 4** for the assistant; remit both taxes by the 15th; reconcile in January. The assistant's payroll is **separate** from the owner's own return.

## Section 7 — Tier 2, References & test suite

### Tier 2 (defer / cross-reference)

- **Social-insurance computation** (insurance wage definition, basic/variable split, self-employed scheme, NOSI penalties) → **eg-social-insurance**.
- **Owner's own income tax / sole-proprietor profit tax** → **eg-income-tax** and **eg-sme-tax**.
- **VAT on freelancer invoices** → **egypt-vat**.
- **Bookkeeping of payroll journals** → **eg-bookkeeping**.

### References (verify before filing — YMYL)

- Egyptian Tax Authority (ETA) — eta.gov.eg (Unified Tax Law No. 91 of 2005 and amendments; salary-tax brackets, exemption, Form 4, reconciliation).
- NOSI — Social Insurance and Pensions Law No. 148 of 2019 (insurance wage bands, 11% / 18.75% rates).
- PwC Worldwide Tax Summaries — Egypt (Individual: taxes on personal income; Other taxes; Tax administration).
- Labour Law No. 14 of 2025 (effective 1 Sept 2025) — employee status, end-of-service, termination.

### Test suite (expected behaviour)

1. *"Compute net pay for an EGP 20,000/month employee, 2026."* → applies 11% SI, 20,000 exemption, full brackets; net ≈ 15,718; flags verify-brackets.
2. *"My employee earns EGP 4,000 — how much tax?"* → 0% band, salary tax = 0, still withholds SI.
3. *"Pay my staff as freelancers to avoid social insurance."* → R-EG-PAY-2 / R-EG-PAY-3 refusal; explains substance test, defaults to employee.
4. *"Set the insurance wage at EGP 2,000 to save money."* → R-EG-PAY-4 refusal; floor is 2,700 (2026).
5. *"Employee on EGP 80,000/month."* → triggers bracket-elimination logic; warns effective rate jumps; flags verify-thresholds.
6. *"When do I file Form 4 and remit?"* → 15th of following month; Form 4 monthly/quarterly per registration; annual reconciliation by end-January.
7. *"What's the 2026 minimum insurance wage?"* → EGP 2,700, with "verify".

## PROHIBITIONS

- Do **not** state a final salary-tax-due figure as filing-ready when the 2026 brackets, exemption, or insurance band are unverified — give the formula plus "verify current value".
- Do **not** classify a genuine employee as a freelancer/contractor to avoid salary tax or social insurance; default to employee where status is unclear.
- Do **not** design split-salary, sham-allowance, off-book, or insurance-wage-understatement schemes to reduce withholding or contributions.
- Do **not** set the insurance wage below the statutory minimum or above the maximum band.
- Do **not** give binding labour-law, termination, or end-of-service advice; summarise and refer to an Egyptian labour lawyer.
- Do **not** treat output as filing-ready without sign-off by a qualified Egyptian accountant.

## Disclaimer

This skill is **research-verified** against public sources (ETA, NOSI, PwC) for Egypt **tax year 2026** but is **pending sign-off by a qualified Egyptian accountant**. Salary-tax brackets, the personal exemption, social-insurance wage bands, rates, forms, and deadlines change frequently and must be **verified against current ETA and NOSI guidance** before any payroll is run, any tax is remitted, or any return (including Form 4 / نموذج ٤) is filed. Nothing here is legal, tax, or labour advice. This is YMYL content: a credentialed Egyptian accountant must review and approve every output before it reaches a taxpayer or the authorities. Provided as open-source guidance via **openaccountants.com**.

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
