---
name: eg-social-insurance
description: Use this skill whenever asked about Egypt social insurance contributions for an employee, employer, or self-employed business owner, professional, craftsman, merchant, farmer, freelancer, or irregular worker. Trigger on phrases like "Egypt social insurance", "التأمينات الاجتماعية", "social insurance contributions Egypt", "self-employed social insurance Egypt", "Law 148 2019", "NOSI", "insurance wage Egypt", "comprehensive social insurance scheme", "تأمين أصحاب الأعمال", or any request to compute, classify, or advise on Egyptian social insurance obligations. Distinguishes employee, employer, and self-employed contributions. ALWAYS read this skill before touching any Egypt social insurance work.
version: 1.0
jurisdiction: EG
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Social Insurance

## Egypt Social Insurance (التأمينات الاجتماعية) Skill v1.0

Social insurance in Egypt is governed by the **Social Insurance and Pensions Law No. 148 of 2019** (قانون التأمينات الاجتماعية والمعاشات رقم ١٤٨ لسنة ٢٠١٩), effective 1 January 2020. It is administered by the **National Organization for Social Insurance — NOSI** (الهيئة القومية للتأمين الاجتماعي), under the Ministry of Finance / Ministry of Social Solidarity (وزارة التضامن الاجتماعي).

This skill covers contribution computation for three distinct payer types:
1. **Employees** (العاملون بأجر) — the employee share withheld from salary.
2. **Employers** (أصحاب الأعمال) — the employer share paid on staff salaries.
3. **Self-employed / business owners** (المؤمن عليهم من أصحاب الأعمال والمهن الحرة) — the comprehensive scheme under which a sole proprietor insures themselves.

> Reply to the user **in their language**. Use English prose with native Arabic terms where useful. All amounts are in Egyptian Pounds (EGP / ج.م).

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Egypt (جمهورية مصر العربية) |
| Contribution | Social Insurance (التأمينات الاجتماعية) |
| Currency | EGP (Egyptian Pound — ج.م) |
| **Employee share** | **11%** of the insurance wage (الأجر التأميني) |
| **Employer share** | **18.75%** of the insurance wage |
| Combined employee + employer | **29.75%** of the insurance wage |
| **Self-employed / business owner** | **21%** of a self-chosen contribution wage (from NOSI reference table) |
| Board members / managers in commercial register | flat **21%** of the **maximum** insurance wage (insured as employers) |
| **Minimum monthly insurance wage 2026** | **EGP 2,700** (from 1 Jan 2026) — *verify current value* |
| **Maximum monthly insurance wage 2026** | **EGP 16,700** (from 1 Jan 2026) — *verify current value* |
| Annual indexation | min/max raised by **15% each 1 January** (2021–2028 window) — *verify* |
| Legislation | Social Insurance and Pensions Law No. **148 of 2019** |
| Authority | National Organization for Social Insurance (**NOSI** — الهيئة القومية للتأمين الاجتماعي) |
| Late-payment penalty | treasury-bill average rate (prior month) **+ 2%** on overdue amounts — *verify* |
| Payment deadline | by the **15th of the month following** the contribution month |
| Quality tier | **Research-verified — pending sign-off by an Egyptian accountant** |
| Skill version | 1.0 |

- **Employee share** — 11% percent of insurance wage
- **Employer share** — 18.75% percent of insurance wage
- **Combined employee + employer** — 29.75% percent of insurance wage
- **Self-employed / business owner rate** — 21% percent of self-chosen contribution wage
- **Board members / managers in commercial register** — flat 21% of the maximum insurance wage
- **Minimum monthly insurance wage 2026** — EGP 2,700 EGP/month (from 1 Jan 2026 — verify current value)
- **Maximum monthly insurance wage 2026** — EGP 16,700 EGP/month (from 1 Jan 2026 — verify current value)
- **Annual indexation** — min/max raised by 15% each 1 January (2021–2028 window) — verify
- **Legislation** — Social Insurance and Pensions Law No. 148 of 2019
- **Authority** — National Organization for Social Insurance (NOSI — الهيئة القومية للتأمين الاجتماعي)
- **Late-payment penalty** — treasury-bill average rate (prior month) + 2% on overdue amounts — verify
- **Payment deadline** — by the 15th of the month following the contribution month
- **Quality tier** — Research-verified — pending sign-off by an Egyptian accountant
- **Skill version** — 1.0

### What each scheme covers

The single combined contribution funds the integrated branches under Law 148/2019: old-age, disability and death pensions (الشيخوخة والعجز والوفاة), work injury (إصابة العمل), sickness (المرض), and unemployment (البطالة), plus an end-of-service component. The self-employed comprehensive scheme provides pension coverage on the chosen contribution wage; some risk branches (e.g. unemployment) apply only to salaried employees.

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown insurance wage for an employee | use the **employee's gross fixed wage**, then cap to the min/max band |
| Wage below the 2026 minimum | contribute on **EGP 2,700** (the minimum), not the actual lower figure |
| Wage above the 2026 maximum | cap the insurance wage at **EGP 16,700** |
| Self-employed contribution wage not chosen | default to the **minimum** wage tier until the client elects a higher one |
| Unsure whether a person is "employer" or "employee" | if their name is in the commercial register → treat as **employer/business owner** |
| Any rate or cap older than the current January | **re-verify against NOSI** before computing |

## Section 2 — Who contributes and how

Egypt's social insurance system separates the obligation by the payer's legal relationship to the work. Get this classification right *before* computing — it determines the rate and who remits.

### A. The employee (العامل بأجر)

- **Employee contribution and withholding** — An employee pays 11% of their insurance wage. The employer withholds this from salary and remits it together with the employer share. The employee does not register or pay directly — registration and remittance are the employer's duty. Cross-reference eg-payroll for how the 11% interacts with income tax (ضريبة كسب العمل) withholding on the same salary.

### B. The employer (صاحب العمل) — paying for staff

- **Employer contribution and duties** — An employer pays 18.75% of each employee's insurance wage, on top of the employee's 11%. The employer registers the establishment and every employee with NOSI, submits the salary forms (Form 1 / Form 2 / Form 6 — Estimارات النموذج), and remits the combined 29.75% monthly. A separate small deduction (e.g. the Martyrs and Victims Fund, ~0.05% of gross) may apply at payroll — handle this in eg-payroll, not here. See eg-payroll for the full employer remittance workflow.

### C. The self-employed business owner (صاحب العمل / المهن الحرة) — paying for themselves

- **Self-employed comprehensive scheme** — A sole proprietor, freelancer, professional, craftsman, merchant or farmer is self-insured (يؤمّن على نفسه): there is no employer, so they pay the whole contribution themselves. The comprehensive scheme rate is 21% of a contribution wage they choose from a NOSI reference table, between the statutory minimum and maximum. They register directly with NOSI as an insured business owner. Because they choose the contribution wage, the monthly cost ranges from 21% of the minimum (EGP 2,700) up to 21% of the maximum (EGP 16,700). Irregular / informal-economy workers (العمالة غير المنتظمة) may pay a reduced share of the lowest contribution wage, with the remainder subsidised — verify the current subsidised split and eligibility with NOSI before relying on it.

### Quick comparison

**Quick comparison table**

| Payer | Rate | Base | Who remits |
| --- | --- | --- | --- |
| Employee | 11% | own insurance wage | employer withholds |
| Employer (per staff member) | 18.75% | each employee's insurance wage | employer |
| Self-employed business owner | 21% | self-chosen contribution wage | the individual |
| Board member / manager in register | 21% | the **maximum** insurance wage | the company |

## Section 3 — Computation

### 3.1 The insurance wage and its bands

- **Insurance wage bands** — Contributions are not on full salary without limit. They apply to the insurance wage (الأجر التأميني), which is clamped between the annual minimum and maximum: 2026 minimum: EGP 2,700 per month; 2026 maximum: EGP 16,700 per month.
- **Insurance wage formula** — insurance_wage = min( max( actual_wage, 2700 ), 16700 )
- **Indexation and historical values** — Both caps are indexed up by 15% each 1 January under Law 148/2019 (the mechanism runs through 2028). Historically: 2025 min EGP 2,300 / max EGP 14,500 → 2026 min EGP 2,700 / max EGP 16,700. Always re-verify the January value for the current year against NOSI before computing.

### 3.2 Employee and employer rates

- **Employee/employer/combined contribution formulas** — employee_contribution = 0.11   × insurance_wage employer_contribution = 0.1875 × insurance_wage combined              = 0.2975 × insurance_wage

### 3.3 Self-employed comprehensive scheme

- **Self-employed contribution formula** — chosen_wage           = elected by the owner, in [2700, 16700] self_employed_monthly = 0.21 × chosen_wage

### 3.4 Worked bands (2026)

**Worked bands (2026)**

| Insurance wage | Employee 11% | Employer 18.75% | Combined 29.75% | Self-employed 21% |
| --- | --- | --- | --- | --- |
| EGP 2,700 (min) | 297.00 | 506.25 | 803.25 | 567.00 |
| EGP 8,000 | 880.00 | 1,500.00 | 2,380.00 | 1,680.00 |
| EGP 16,700 (max) | 1,837.00 | 3,131.25 | 4,968.25 | 3,507.00 |

All figures EGP/month. Note: the self-employed pay 21% of their chosen wage — not 29.75% — because the comprehensive scheme uses a single combined rate.

## Section 4 — Registration and payment

### Registration with NOSI (التسجيل)

- **Registration requirements** — Employers: must register the establishment and each new employee with NOSI using the prescribed forms (Form 1 to open the file, Form 2 for new hires, Form 6 on termination — verify current form numbers). New hires must be reported promptly to avoid lapses in coverage. Self-employed / business owners: register themselves directly at the competent NOSI office (or online portal where available), declaring their activity and electing a contribution wage from the reference table. Insurance numbers (الرقم التأميني) follow the individual; the national ID (الرقم القومي) is the key identifier.

### Payment cadence (سداد الاشتراكات)

- **Payment cadence** — Contributions are due monthly. Remittance must reach NOSI by the 15th of the month following the month for which contributions are due. Paying on or before the 15th avoids the late charge. Employers remit the combined employee + employer amount; self-employed pay their own 21%.

### Penalties (غرامات التأخير)

- **Late payment penalties and under-declaration** — Late contributions accrue an additional delay charge equal to the average yield on treasury bills/bonds for the month before payment, plus 2%, applied until the debt is settled — verify the exact current formula with NOSI. Failure to register employees or under-declaring wages exposes the employer to back-contributions plus the delay charge and possible administrative penalties.

## Section 5 — Worked examples

### Example 1 — Employee on a mid-range salary

A salaried developer earns a fixed monthly wage of EGP 12,000 (within the band).

- Insurance wage = EGP 12,000 (between 2,700 and 16,700).
- Employee share = 11% × 12,000 = **EGP 1,320**.
- Employer share = 18.75% × 12,000 = **EGP 2,250**.
- Combined remitted by employer = **EGP 3,570/month**.

### Example 2 — High earner above the cap

An employee earns EGP 25,000/month.

- Insurance wage is **capped at EGP 16,700** (not 25,000).
- Employee share = 11% × 16,700 = **EGP 1,837**.
- Employer share = 18.75% × 16,700 = **EGP 3,131.25**.
- Salary above EGP 16,700 carries **no** statutory social insurance contribution.

### Example 3 — Self-employed freelancer choosing a mid tier

A freelance graphic designer registers as a self-employed business owner and elects a contribution wage of EGP 8,000.

- Self-employed contribution = 21% × 8,000 = **EGP 1,680/month**.
- She pays this herself, directly to NOSI, by the 15th of the next month.
- If she instead elected the minimum (EGP 2,700), she would pay 21% × 2,700 = **EGP 567/month**; at the maximum (EGP 16,700), **EGP 3,507/month**.

### Example 4 — Owner-manager named in the commercial register

A managing partner whose name is in the company's commercial register is insured as an employer, not a salaried employee.

- Contribution = **21% of the maximum** insurance wage = 21% × 16,700 = **EGP 3,507/month**, regardless of the salary actually drawn.
- *Verify whether this flat treatment applies to the specific role and register entry with an Egyptian accountant.*

## Section 6 — Tier 2, references, and test suite

### Tier 2 — escalate to a human reviewer when

- **Escalation triggers** — The worker's classification is ambiguous (employee vs. business owner vs. irregular worker), or their name's presence in the commercial register is unclear. The client is an irregular / informal-economy worker eligible for the subsidised contribution split — confirm eligibility and the current subsidised %. Multiple simultaneous capacities exist (e.g. employed and running a business) — aggregation and cap rules need a reviewer. The current-year January min/max or rates cannot be confirmed against NOSI. Back-contributions, settlements, or penalty negotiations are involved. Foreign nationals / totalization agreements (اتفاقيات التأمين المتبادل) apply.

### References

- Social Insurance and Pensions Law No. **148 of 2019** and its Executive Regulations (اللائحة التنفيذية).
- **NOSI** — National Organization for Social Insurance (الهيئة القومية للتأمين الاجتماعي). Verify min/max wage and rates each January.
- **PwC Worldwide Tax Summaries — Egypt, Individual / Other taxes** (employee 11%, employer 18.75%, 2026 min EGP 2,700 / max EGP 16,700, board flat 21%).
- **BDO**, **Mercans**, **Fragomen** statutory alerts on the January 2026 insurable wage increase.
- Cross-reference: **eg-payroll** (employer remittance + income-tax interaction), **egypt-vat** (indirect tax for the same self-employed client).

### Test suite (sanity checks)

**Test suite table**

| # | Input | Expected |
| --- | --- | --- |
| T1 | Employee, wage EGP 10,000 | employee 1,100; employer 1,875 |
| T2 | Employee, wage EGP 1,500 | clamp to 2,700 → employee 297; employer 506.25 |
| T3 | Employee, wage EGP 30,000 | cap to 16,700 → employee 1,837; employer 3,131.25 |
| T4 | Self-employed, chosen wage EGP 5,000 | 21% × 5,000 = 1,050 |
| T5 | Self-employed, no wage chosen | default to min 2,700 → 567 |
| T6 | Board member in register | 21% × 16,700 = 3,507 |
| T7 | Payment made on the 16th | late — delay charge (T-bill avg + 2%) applies |
| T8 | Asked for 2027 figures | re-verify January 2027 indexed min/max before answering |

## PROHIBITIONS

- **Prohibitions list** — - Do NOT state the minimum or maximum insurance wage, or the contribution rates, as settled fact for any year without re-verifying against NOSI — the caps are indexed +15% every January and change annually. - Do NOT apply the 11% / 18.75% employee/employer split to a self-employed person; the self-employed comprehensive rate is 21% of a chosen wage. - Do NOT compute contributions on uncapped salary — always clamp to the min/max band. - Do NOT treat an owner-manager named in the commercial register as a salaried employee; they are insured as an employer (flat 21% of the maximum wage). - Do NOT advise on irregular/informal-worker subsidised contributions without confirming the current subsidised split and eligibility with NOSI. - Do NOT handle income tax (كسب العمل) withholding, the Martyrs Fund deduction, or payroll mechanics here — defer to eg-payroll. - Do NOT advise on totalization agreements, expatriate exemptions, or penalty settlements without a qualified Egyptian reviewer. - Do NOT file, register, or remit on the client's behalf — produce the computation and instructions only.

## Disclaimer

This skill is **research-verified** against NOSI, the Social Insurance and Pensions Law No. 148 of 2019, PwC Worldwide Tax Summaries, and Big-4 / payroll-provider statutory alerts, current as of **May 2026 for tax year 2026**. Social insurance is a **Your-Money-or-Your-Life (YMYL)** domain: the minimum and maximum insurance wages are re-indexed by 15% every January, and rates or subsidy rules may change. **Every output must be reviewed and signed off by a qualified Egyptian accountant (محاسب قانوني) before reliance or submission.** Where a current value cannot be confirmed, the skill provides the formula and flags "verify current value."

Part of **openaccountants.com** — open-source tax skills for the self-employed.

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
