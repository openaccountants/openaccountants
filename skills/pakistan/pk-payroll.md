---
name: pk-payroll
description: >
  Use this skill whenever asked about Pakistan payroll and salary-tax withholding for employers.
  Trigger on phrases like "Pakistan payroll", "salary tax withholding Pakistan", "deduct tax from
  salary FBR", "EOBI deduction", "payroll Pakistan freelancer hiring staff". Covers salary income-tax
  withholding under the salaried slabs, EOBI/provincial social security, and monthly withholding
  statements. ALWAYS read before any Pakistan payroll work.
version: 1.0
jurisdiction: PK
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - social-contributions-workflow-base
---

# Pakistan Payroll & Salary Withholding — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Item | Who | Notes (verify current Finance Act) |
|---|---|---|
| Salary income tax | Employer withholds from employee | Salaried slabs, top 35%; first PKR 600,000 exempt |
| EOBI | Employer ~5% + employee ~1% of minimum wage | Where 5+ employees (some 1+) |
| Provincial social security (ESSI) | Employer | For secured (low-wage) employees; province-specific |
| Monthly withholding statement | Employer → FBR (IRIS) | Plus annual statement |
| Currency | — | PKR |
| Quality tier | — | Research-verified — pending sign-off by a Pakistani practitioner |

## Section 2 — Mechanics (Tier 1)
- The employer computes each employee's annual tax under the **salaried slabs**, divides by 12, and **withholds monthly**, depositing to the FBR and filing the **monthly withholding statement** via IRIS.
- **EOBI** (old-age pension) applies once the employer hits the employee threshold; **provincial ESSI** applies for secured employees. Both are employer-administered.
- A solo freelancer with **no employees** has no payroll obligations (see pk-social-contributions).

## Section 3 — Worked example
A small studio pays an employee PKR 1,200,000/year: compute tax on the salaried slabs (first 600k exempt; remainder at the applicable rate — verify), withhold ~1/12 monthly, deposit to FBR, file the monthly statement; register/contribute to EOBI if at the threshold.

## Section 10 — Prohibitions
- NEVER use non-salaried/business slabs for employees (use salaried slabs).
- NEVER skip the monthly withholding statement.
- NEVER state slab/EOBI figures without verifying the current Finance Act.

## Disclaimer
Informational only; not advice. Verify withholding slabs and EOBI/ESSI rules with the FBR and the relevant authority. All outputs must be reviewed and signed off by a qualified Pakistani practitioner. Maintained at [openaccountants.com](https://www.openaccountants.com).
