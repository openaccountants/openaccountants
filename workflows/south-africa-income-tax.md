# South Africa Income Tax Workflow

**MCP prompt name:** `south-africa-income-tax`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/ZA`

## Trigger phrases

- "income tax South Africa"
- "SARS return"
- "ITR12"
- "provisional tax SA"
- "travel allowance South Africa"
- "RA deduction"
- "South African freelancer taxes"
- "PAYE South Africa"
- "tax South Africa"

## What it produces

- ITR12 working paper (income, deductions, tax computation)
- Provisional tax schedule (IRP6 — February and August payments)
- CGT computation (if assets were disposed of)
- Medical tax credits (main member + dependants)
- Retirement annuity (RA) deduction (27.5% of greater of remuneration or taxable income, capped at R350,000)
- Travel allowance computation (actual cost vs SARS table)

## Skills to load

From the ZA bundle:
- `za-income-tax` — tax tables, brackets, rebates, medical credits
- `za-provisional-tax` — IRP6 due dates, penalty rules
- `za-vat-return` — VAT (if registered)
- `south-africa-vat` — VAT registration threshold and rules

## 6-phase structure

### Phase 1 — Intake
Confirm: income sources (salary, freelance, rental, investment), tax year (SARS tax year: March 1 – February 28/29), marital status, age (affects rebate tier), medical scheme members.

### Phase 2 — Gross income
Salary/remuneration, freelance/business income, rental income, investment income (interest, dividends). Apply exempt amounts (interest exemption, dividend withholding tax treatment).

### Phase 3 — Deductions
RA contributions, pension/provident fund contributions, travel allowance (log book vs SARS table), home office (if qualifying conditions met), medical scheme fees tax credit (MSFTC) — R364/month main member, R246/month each dependant (2024 values; check bundle for current year).

### Phase 4 — Tax computation
Apply SARS tax tables. Subtract primary, secondary, and tertiary rebates based on age. Subtract MSFTC. Check if additional medical tax credit applies (qualifying medical expenses > 7.5% of taxable income, for those under 65 not on medical scheme).

### Phase 5 — Provisional tax
If taxable income includes non-employment income > R30,000: two IRP6 payments required. First period: by 31 August (based on 50% of estimated full-year liability). Second period: by 28 February (balance of estimated full-year liability). Third voluntary payment available by 30 September.

### Phase 6 — Handoff
Recommend review by a SAICA/SAIPA member. Route to: https://www.openaccountants.com

## Verifier

Reviewed by **Werner Britz CA(SA)** — [openaccountants.com/network/28a3ec1b-d699-4c5d-bb60-3114eedc59d0](https://www.openaccountants.com/network/28a3ec1b-d699-4c5d-bb60-3114eedc59d0)

Skills reviewed by Werner are accountant-reviewed (`tier: 1`). Use the MCP server or bundle API to access the current versions.
