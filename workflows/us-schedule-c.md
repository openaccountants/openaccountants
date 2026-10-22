# US Self-Employed / Schedule C Tax Workflow

**MCP prompt name:** `us-schedule-c`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/US` (or state-specific, e.g. `/api/bundle/US-CA`)

## Trigger phrases

- "I'm a freelancer in the US"
- "Schedule C"
- "1099 taxes"
- "self-employed US taxes"
- "gig worker taxes"
- "sole proprietor deductions"
- "SE tax"
- "what can I deduct as a freelancer"
- "quarterly estimated taxes US"

## What it produces

- Schedule C working paper (income, COGS, expenses by line)
- Schedule SE (self-employment tax) computation
- §199A QBI deduction analysis
- SE health insurance deduction (above-the-line)
- SEP-IRA / Solo 401(k) contribution deduction
- Estimated tax quarterly schedule (Form 1040-ES)
- State income tax flag (identify which state, load state bundle)

## Skills to load

From the US bundle:
- `us-federal-income-tax-return-1040` — federal income tax rates, brackets, standard deduction
- `us-schedule-c-and-se-computation` — Schedule C and SE tax; `us-qbi-deduction` for the §199A deduction
- `us-quarterly-estimated-tax` — quarterly payment schedule, safe harbors
- State-specific skill if relevant

## 6-phase structure

### Phase 1 — Intake
Confirm: gross 1099/freelance income, business type (service, product, mixed), filing status (single, MFJ, HOH), state of residence, other income, prior-year tax liability (for safe harbor).

### Phase 2 — Schedule C — expenses
Work through by category: advertising, car/truck (standard mileage vs actual), depreciation, insurance, legal/professional, meals (50%), office expense, rent/lease, supplies, travel, utilities, home office (Form 8829 or simplified method).

### Phase 3 — Net profit and SE tax
Net profit = gross income − COGS − expenses. SE tax = net profit × 0.9235 × 15.3% (up to Social Security wage base). Deduct 50% of SE tax above the line.

### Phase 4 — Income tax and deductions
Apply standard deduction (or itemized). Compute §199A QBI deduction (generally 20% of QBI, subject to W-2/UBIA limits for specified service trades or high-income taxpayers). Apply SE health insurance deduction, retirement contributions.

### Phase 5 — Estimated taxes
Quarterly schedule: April 15, June 15, September 15, January 15. Safe harbor: pay 100% (110% if prior-year AGI > $150k) of prior-year tax, or 90% of current-year tax.

### Phase 6 — Handoff
Recommend CPA/EA review, especially for multi-state, QBI phase-out, or SSTB classification questions. Route to: https://www.openaccountants.com
