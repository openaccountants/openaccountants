---
name: bd-payroll
description: >
  Use this skill whenever asked about Bangladesh payroll and salary-tax withholding for employers.
  Trigger on phrases like "Bangladesh payroll", "salary TDS Bangladesh", "deduct tax from salary NBR",
  "provident fund gratuity Bangladesh", "payroll Bangladesh freelancer hiring staff". Covers salary
  income-tax withholding under the slabs, provident fund/gratuity, the (limited) social-security
  position, and monthly TDS deposit/returns. ALWAYS read before any Bangladesh payroll work.
version: 1.0
jurisdiction: BD
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - social-contributions-workflow-base
---

# Bangladesh Payroll & Salary Withholding — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Item | Who | Notes (verify current Finance Act) |
|---|---|---|
| Salary income tax (TDS) | Employer withholds from employee | Individual slabs; first ~৳350,000 tax-free |
| Provident fund | Employer scheme (if any) | Recognised PF — contributions/withdrawals have specific tax rules |
| Gratuity | Employer scheme (if any) | Per the Labour Act / scheme |
| Universal Pension (Progoti) | Private-sector employees — voluntary | Employee + employer contribution |
| Monthly TDS deposit + returns | Employer → NBR | Deposit withheld tax; file the withholding return |
| Currency | — | BDT (৳) |
| Quality tier | — | Research-verified — pending sign-off by a Bangladeshi practitioner |

## Section 2 — Mechanics (Tier 1)
- The employer estimates each employee's annual tax under the **individual slabs** (with the tax-free threshold and any rebate), divides across the year, **withholds monthly (TDS)**, deposits to the NBR, and files the **monthly/periodic withholding return**.
- **No broad national social-security payroll tax.** Benefits run through **provident fund** and **gratuity** schemes where the employer operates them; the **Universal Pension Scheme (Progoti)** is a voluntary option for private employees.
- A **solo freelancer with no employees** has no payroll obligation (see bd-social-contributions).

## Section 3 — Worked example
A studio pays an employee ৳600,000/year: compute tax on the slabs (first ~৳350,000 tax-free; remainder at the applicable rates — verify), withhold ~1/12 monthly, deposit to the NBR, and file the withholding return. PF/gratuity only if the employer runs such schemes.

## Section 10 — Prohibitions
- NEVER skip monthly TDS deposit/return for salaried staff.
- NEVER assume a mandatory national social-insurance payroll tax (there isn't a broad one).
- NEVER state slab/rebate figures without verifying the current Finance Act.

## Disclaimer
Informational only; not advice. Verify withholding slabs, PF/gratuity, and pension rules with the NBR and relevant authority. All outputs must be reviewed and signed off by a qualified Bangladeshi practitioner. Maintained at [openaccountants.com](https://www.openaccountants.com).
