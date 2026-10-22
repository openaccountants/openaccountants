# Malta Freelancer / Self-Employed Tax Workflow

**MCP prompt name:** `malta-freelancer`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/MT`

## Trigger phrases

- "self-employed Malta"
- "freelancer Malta"
- "part-time work Malta"
- "FS5 Malta"
- "SSC Malta"
- "Malta VAT registration"
- "malta-income-tax"
- "Malta sole trader"
- "tax Malta"

## What it produces

- Part-time flat-rate (15%) vs progressive rate comparison
- SSC Class 2 contribution computation (self-occupied)
- VAT3 working paper (if VAT-registered)
- FS5 provisional tax schedule
- Annual income tax return working paper

## Skills to load

From the MT bundle:
- `malta-income-tax` — tax rates, brackets, single/married/parent computation, part-time 15% rule
- `malta-ssc` — Social Security Contributions (Class 2 self-occupied rates)
- `malta-vat-return` — VAT3 periods, thresholds, deductible input VAT
- `mt-estimated-tax` — FS5 provisional tax due dates

## 6-phase structure

### Phase 1 — Intake
Confirm: employment status (full-time employed + part-time self-employed, or full-time self-employed), type of income (service, product, rental), annual gross revenue, major expenses, VAT registration status, marital status (affects rate structure).

### Phase 2 — Part-time vs standard rate decision
If the taxpayer is also in full-time employment and earns ≤€10,000 from part-time self-employment: eligible for 15% flat rate on gross part-time income (no deductions). Compare to declaring under the progressive rates with deductions — run both and show which is lower.

### Phase 3 — SSC computation
Class 2 (self-occupied): weekly flat-rate contribution based on annual net income bracket. Compute annual SSC liability. Note: Class 2 does not apply to part-time income declared under the 15% flat rate — check the rules for the current year in the bundle.

### Phase 4 — VAT position
If annual turnover exceeds the Malta VAT registration threshold: mandatory VAT registration. VAT3 returns: bi-monthly or quarterly. Compute output VAT (sales × applicable rate) less deductible input VAT (business purchases).

### Phase 5 — FS5 provisional tax
Self-employed taxpayers pay provisional tax via FS5 slips: three equal instalments (April, August, December). Based on the prior year's assessed income tax liability (or estimated current-year if income changes materially).

### Phase 6 — Handoff
Recommend review by a Malta-qualified CPA or warranted accountant. Route to: https://www.openaccountants.com

## Verifier

Reviewed by **Michael Cutajar CPA (Malta)** — [openaccountants.com/network](https://www.openaccountants.com/network)

Skills reviewed by Michael are accountant-reviewed (`tier: 1`). Use the MCP server or bundle API to access the current versions.
