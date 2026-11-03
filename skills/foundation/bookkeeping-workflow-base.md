---
name: bookkeeping-workflow-base
description: Universal bookkeeping workflow base that defines the classification, posting, and reporting runbook for all jurisdictions. Contains no jurisdiction-specific content — no charts of accounts, no local GAAP rules, no tax rates, no currency conventions. This skill MUST be loaded alongside a country-specific bookkeeping skill that provides the chart of accounts, P&L/balance sheet format, and local conventions. This skill alone cannot produce any output.
version: 1.0
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-06-12
tier: 2
---

# Bookkeeping Workflow Base Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a bookkeeping task: the order of operations, how to classify transactions, how to handle ambiguity, what to produce as output, what to check before delivering. It contains no charts of accounts, no nominal codes, no local GAAP rules, no P&L formats, no balance sheet layouts, no currency conventions.

**This file must always be loaded with a country-specific bookkeeping skill** that provides the chart of accounts, reporting formats, and local conventions (e.g., `uk-bookkeeping`, `au-bookkeeping`, `de-bookkeeping`). This file alone cannot produce a trial balance, P&L, or balance sheet. Loading it without a companion is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a country bookkeeping skill says it conforms to v1.0 of this base, it means: it fills the country slots specified in Section 7, it produces outputs in the format specified in Section 3, its classifications can be validated by the self-checks in Section 5, and it participates in the workflow in Section 1.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping a small business owner produce bookkeeping records from raw financial data. The output will be reviewed by a qualified accountant before use. Your job is to do the mechanical classification and posting work and produce a working set of accounts plus a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these nine steps in order. Do not skip. Do not reorder. Do not start classifying transactions before step 4. Do not build any output files before step 6.

### Step 1 — Confirm the companion skills are loaded

This workflow base requires a country-specific bookkeeping skill providing the chart of accounts, reporting format, and local conventions.

If no country-specific skill is loaded, stop and tell the user: "I need a country-specific bookkeeping skill loaded alongside this workflow base. Which jurisdiction are these accounts for?" Do not proceed without it.

If a VAT or GST workflow skill is also loaded, note its presence — reconciliation between the bookkeeping ledger and the tax control account will be required at Step 7.

### Step 2 — Read the data

The user will provide one or more of: bank statements (CSV, PDF, or pasted text), invoices, receipts, or a combination. Read every line of every document provided. Do not skim. Identify:

- The period covered (earliest transaction date to latest)
- The currency (must match the country skill's expected currency or be flagged as multi-currency)
- The number of transactions across all sources
- The source type for each document (bank statement, sales invoice, purchase invoice, receipt, journal entry)
- Any obvious format problems (missing columns, truncated data, unreadable encoding, duplicate documents)
- Whether the data set is complete for the period (gaps in date sequences, missing months)

If the data is unreadable, covers a different country than the loaded skill, or is so incomplete that a meaningful trial balance cannot be produced, stop and tell the user.

### Step 3 — Infer the client profile from the data

Before asking the user onboarding questions, attempt to infer the client profile from the data alone. Look for:

- **Entity type.** Owner withdrawals, drawings, private transfers → sole trader / self-employed. Multiple salary payments to non-owner names → company with employees. Single director salary → single-director company. Share capital references, dividend payments → limited company.
- **Industry signals.** Stock purchases (retail/wholesale), subcontractor payments (construction/services), raw materials (manufacturing), booking platforms (hospitality), patient references (healthcare).
- **Scale indicators.** Monthly transaction volume, typical transaction size, number of distinct customers and suppliers, presence of fixed assets.
- **Accounting basis signals.** Invoices dated differently from payment dates (accrual basis likely), all transactions cash-settled on the day (cash basis likely), prepayment patterns.
- **VAT/GST registration signals.** Tax authority payments, round-number quarterly payments to revenue bodies, VAT-inclusive pricing patterns in descriptions.
- **Employees.** Payroll patterns, pension contributions, social security payments to known statutory bodies.
- **Fixed assets.** Large one-off purchases, hire purchase or lease payments, depreciation-eligible items.
- **Multi-currency activity.** Foreign currency transactions, exchange rate differences, international supplier payments.

Produce a one-paragraph inferred profile. State it as a hypothesis, not a fact.

### Step 4 — Confirm the inferred profile (one round trip)

Output the inferred profile to the user in this exact form:

> "Based on the data provided, here is what I believe about your situation:
>
> [One paragraph: entity type, industry, scale, accounting basis, VAT status, employee status, fixed asset presence, period covered.]
>
> Is this correct? If anything is wrong, tell me and I will adjust before I start classifying. If it is correct, reply 'confirmed' and I will proceed."

Wait for confirmation. If the user corrects anything, update the profile and re-confirm in one sentence. Do not ask a full onboarding questionnaire — only ask follow-ups for items the data could not infer at all.

### Step 5 — Transaction classification to nominal codes

For every transaction across all data sources, in chronological order:

1. **Exclusion check.** Apply the country skill's exclusion patterns (inter-account transfers that net to zero, duplicate entries across sources, non-financial items). If the line matches an exclusion, mark it excluded with the reason and move on.

2. **Tier 1 classification (Confident).** Check the transaction against the country skill's classification rules and chart of accounts. If the transaction clearly maps to one and only one nominal code with no ambiguity from the data alone, classify it. Examples: bank charges → bank fees account, salary payment to named employee → wages account, utility payment to known provider → utilities account.

3. **Tier 2 classification (Assumed).** If the transaction could map to multiple nominal codes but one is more conservative, apply the conservative default (see Section 2) and flag for review. Record the alternative code and the reasoning.

4. **Tier 3 classification (Needs Input).** If the transaction cannot be classified without information only the user has, queue it for the user question step. Do not guess. Examples: large round-number transfer (loan repayment? owner injection? inter-company?), payment to an individual (subcontractor? employee? personal?), mixed-use expense (what percentage business?).

Every transaction MUST end up in exactly one state: excluded with reason, classified at Tier 1, classified at Tier 2 with default and flag, or queued as Tier 3 for user input. No transaction may be silently dropped.

### Step 5.5 — Ask the user about Tier 3 items

Before building any output, present Tier 3 items to the user grouped by category. Order by financial impact (largest amounts first). For each item or group:

- Name the transaction(s) explicitly (date, counterparty, amount)
- Explain what information is needed
- Offer 2-4 options where possible
- Always include a "Don't know — apply conservative default" option

Wait for the user's answers. Apply them to the classification. Any items where the user selects "don't know" receive the conservative default from Section 2 and are flagged in the reviewer brief.

### Step 6 — Double-entry posting

For every classified transaction, create the double-entry journal:

- Every debit has an equal and opposite credit. No exceptions.
- Bank account is the control account for bank statement transactions.
- Sales ledger (accounts receivable) is the control for sales invoices.
- Purchase ledger (accounts payable) is the control for purchase invoices.
- For cash basis: revenue recognized on receipt, expense recognized on payment.
- For accrual basis: revenue recognized on invoice date, expense recognized on invoice date, with separate entries for payment against the receivable/payable.
- VAT/GST: if a tax skill is loaded, post the tax element to the appropriate control account per the tax skill's instructions. If no tax skill is loaded, post gross amounts only and note that tax has not been separated.

Verify as you post: running total of debits must equal running total of credits at every point. If they diverge, stop and find the error before continuing.

### Step 7 — Reconciliation

Perform bank reconciliation:

- Opening bank balance (from bank statement or user-provided)
- Plus all receipts posted to the bank account
- Minus all payments posted from the bank account
- Equals closing bank balance per ledger
- Compare to closing balance per bank statement
- Identify and list any unmatched items (items on the bank statement not in the books, items in the books not on the bank statement)

If a VAT/GST skill is also loaded, reconcile the VAT control account:
- Output VAT collected (per ledger) vs output VAT on the return
- Input VAT claimed (per ledger) vs input VAT on the return
- Net balance on control account vs amount payable/refundable

### Step 8 — Trial balance and financial statements

Produce the trial balance: list every nominal code that has been posted to, with its debit or credit balance. Verify total debits equal total credits.

From the trial balance, produce:
- **Profit & Loss statement** in the format specified by the country skill (single-step or multi-step, grouped by the country skill's categories)
- **Balance sheet** in the format specified by the country skill (horizontal or vertical, current/non-current classification per the country skill)

Cross-check: net profit on the P&L equals the movement in retained earnings on the balance sheet (adjusted for drawings/dividends). If it does not, find and fix the error.

### Step 9 — Build and deliver outputs

Produce the five output artefacts specified in Section 3. Run the self-checks in Section 5 against all outputs. If any check fails, fix and re-run. Only present files to the user when all checks pass.

Write a short closing chat response:
- Net profit/loss figure for the period
- One sentence on what each output file contains
- The highest-priority item from the reviewer brief
- An invitation to revise: "If any classification needs changing, tell me which transaction and I'll update the accounts."

---

## Section 2 — Classification rules and conservative defaults

Every transaction falls into one of three tiers.

### Tier 1 — Confident

The transaction clearly maps to one nominal code with no ambiguity. The counterparty, description, amount pattern, and context all point to the same account. A competent bookkeeper looking at the same data would reach the same conclusion without hesitation.

**Action:** Classify silently. Do not narrate. Do not flag.

### Tier 2 — Assumed

The transaction could reasonably map to two or more nominal codes. The data provides clues but not certainty. A competent bookkeeper would classify it but note the assumption.

**Action:** Apply the conservative default (below), flag in the reviewer brief with the alternative treatment, and record in the transaction register as Tier 2.

### Tier 3 — Needs Input

The transaction cannot be classified without information only the user possesses. The data provides insufficient clues for even a conservative assumption.

**Action:** Queue for user question in Step 5.5. Do not guess. Do not apply a default until the user has been asked and either answered or selected "don't know."

### Conservative defaults — universal principles

When uncertain, apply the treatment that is most conservative from a tax and financial reporting perspective:

- **Expense vs. capitalize:** Expense it. Capitalizing creates an asset that may be overstated; expensing is immediately prudent.
- **Business vs. personal:** Treat as personal (exclude from business accounts). Including a personal expense in business accounts overstates deductions.
- **Current period vs. prepaid:** Recognize in the current period. Deferring may understate current-period expenses.
- **Revenue vs. non-revenue receipt:** Treat as revenue. Non-revenue treatment (loan, owner injection) understates income.
- **Cost of goods sold vs. operating expense:** Operating expense. COGS misclassification affects gross margin but not net profit; operating expense is the safer category.
- **Current liability vs. long-term:** Current. Treating a current obligation as long-term overstates working capital.
- **Gross vs. net of tax:** Post gross if tax treatment is uncertain. Let the tax skill handle separation when loaded.

The country skill provides concrete defaults for country-specific ambiguities (e.g., which nominal code for a specific type of statutory payment). The principles above govern when the country skill is silent.

### Mixed-use transaction handling

When a transaction is partially business and partially personal:

- If the user has stated a business-use percentage, apply it.
- If the user has not stated a percentage and the item is commonly mixed-use (vehicle, phone, home office), ask in Step 5.5.
- If the user selects "don't know," apply 0% business use (fully personal — the most conservative default).
- Record the split in the transaction register with the source of the percentage (user-stated, default, or country-skill rule).

### Recurring vs. one-off treatment

- If a transaction recurs monthly at the same amount to the same counterparty, classify the first instance and apply the same classification to all subsequent instances automatically.
- If a recurring transaction changes amount by more than 20%, flag the change but maintain the classification unless the nature has clearly changed.
- One-off large transactions (above the country skill's materiality threshold) always receive individual attention regardless of Tier.

### Revenue recognition timing

- **Cash basis:** Revenue recognized when cash is received. Expense recognized when cash is paid. No receivables or payables.
- **Accrual basis:** Revenue recognized when earned (invoice date or delivery date). Expense recognized when incurred (invoice date or receipt of goods/services). Receivables and payables tracked.
- The accounting basis is determined in Step 4 (confirmed client profile). If the user does not specify, the country skill's default for the entity type applies. If the country skill is silent, default to cash basis for sole traders and accrual basis for companies.

---

## Section 3 — Output specification

Five outputs per bookkeeping engagement. All five are mandatory. Never produce one without the others.

### Output 1 — Trial balance

Tabular format with columns:

| Column | Content |
|---|---|
| Account code | The nominal code from the country skill's chart |
| Account name | The descriptive name |
| Debit balance | Positive number if the account has a debit balance |
| Credit balance | Positive number if the account has a credit balance |

Footer row: total debits, total credits (must be equal).

Grouped by category per the country skill's chart structure (assets, liabilities, equity, revenue, cost of sales, expenses).

### Output 2 — Profit & Loss statement

Format per the country skill's specification. Universal structure:

```
Revenue (grouped by category)
- Cost of goods sold (if applicable)
= Gross profit
- Operating expenses (grouped by category per country skill)
= Operating profit / Net profit before tax
- Tax (if tax skills loaded and applicable)
= Net profit after tax
```

Each line item shows the nominal code, description, and amount. Categories are subtotalled. The country skill specifies whether single-step (all revenue minus all expenses) or multi-step (with gross profit intermediate).

### Output 3 — Balance sheet

Format per the country skill's specification. Universal structure:

```
Assets
  Non-current assets (if any)
  Current assets
    Bank and cash
    Accounts receivable (accrual basis only)
    Prepayments (if any)
Total assets

Liabilities
  Current liabilities
    Accounts payable (accrual basis only)
    Tax liabilities (if tax skills loaded)
    Accruals (if any)
  Non-current liabilities (if any)
Total liabilities

Equity
  Capital / owner's equity
  Retained earnings / current year profit
  Drawings (sole trader) / dividends (company)
Total equity

Total liabilities + equity (must equal total assets)
```

The country skill specifies horizontal vs. vertical format, current/non-current thresholds, and local GAAP terminology.

### Output 4 — Reviewer brief

A short narrative document for the human reviewer:

```markdown
# [Country] Bookkeeping — Reviewer Brief
**Period:** [period]
**Generated:** [date]
**Source data:** [list of documents provided]
**Entity type:** [confirmed entity type]
**Accounting basis:** [cash / accrual]

## Summary
- Net profit/loss: [amount] [currency]
- Total transactions classified: [count]
- Tier 1 (confident): [count]
- Tier 2 (assumed, flagged): [count]
- Tier 3 (user-answered): [count]
- Excluded: [count]
- Unmatched items in bank reconciliation: [count]

## High-priority items (review first)
[Numbered list: items with largest financial impact or highest uncertainty.
Each: one sentence what, one sentence why it matters, one sentence
what the reviewer should do.]

## Assumptions made (Tier 2 defaults)
[For each Tier 2 classification: date, counterparty, amount, nominal code
applied, alternative code, reason for assumption, cash impact of alternative.]

## Questions asked and user answers (Tier 3)
[For each Tier 3 item: the question, the user's answer or "don't know —
default applied", and the resulting classification.]

## Bank reconciliation summary
- Closing balance per bank statement: [amount]
- Closing balance per ledger: [amount]
- Difference: [amount or "nil"]
- Unmatched items: [list or "none"]

## Items the reviewer should verify
[Specific items, not generic "check everything." Invoices to pull,
confirmations to obtain, balances to verify with third parties.]
```

### Output 5 — Transaction register

Every transaction with full classification detail:

| Column | Content |
|---|---|
| Date | Transaction date |
| Source | Bank/invoice/receipt reference |
| Counterparty | Name |
| Description | As provided in source data |
| Gross amount | Original amount |
| Net amount | Excluding tax (if tax skill loaded) |
| Tax amount | If tax skill loaded |
| Debit account | Nominal code and name |
| Credit account | Nominal code and name |
| Confidence tier | 1, 2, or 3 |
| Notes | Assumptions, user answers, flags |
| Excluded | Y/N with reason if Y |

---

## Section 4 — Detailed classification guidance

### When to classify vs. when to ask

**Classify silently (Tier 1) when:**
- The counterparty name matches a known pattern in the country skill's supplier/payee library
- The transaction description contains keywords that map unambiguously to a nominal code
- The amount, frequency, and counterparty combination leaves no reasonable alternative
- A competent bookkeeper would not pause on this transaction

**Classify with assumption (Tier 2) when:**
- Two or more codes are plausible but one is more conservative
- The description is ambiguous but the amount pattern suggests a category
- The transaction type is common but the specific business purpose is unclear
- The counterparty is not in the supplier library but the transaction characteristics strongly suggest a category

**Ask the user (Tier 3) when:**
- The transaction could be personal or business and no data signal disambiguates
- A large round-number transfer has no description or counterparty context
- The transaction type depends on the user's specific business arrangements (e.g., is this person an employee or a subcontractor?)
- Misclassification would materially affect the P&L or balance sheet and the data does not carry the answer

### Personal vs. business split rules

- Payments to/from the business owner by name: Tier 3 unless the description clarifies (e.g., "drawings," "loan repayment," "expense reimbursement")
- Payments to retail stores with no description: Tier 3 if above the country skill's materiality threshold, excluded as personal if below
- Subscriptions to consumer services (streaming, personal insurance): excluded as personal unless the user has confirmed business use
- Mixed-use utilities (home office): Tier 3 — ask for business-use percentage

### Recurring vs. one-off treatment

- First occurrence of a new counterparty: classify on its merits
- Second and subsequent occurrences of the same counterparty at similar amounts: apply the same classification as the first unless the description has changed materially
- If a recurring pattern breaks (amount doubles, frequency changes, description changes): re-evaluate as if new, flag in reviewer brief

### Revenue recognition timing

**Cash basis recognition:**
- Sales: recognized when payment hits the bank account
- Purchases: recognized when payment leaves the bank account
- No accounts receivable or accounts payable on the balance sheet
- Prepayments and accruals may still exist depending on country GAAP

**Accrual basis recognition:**
- Sales: recognized on invoice date (or delivery date if no invoice)
- Purchases: recognized on invoice date (or receipt of goods/services)
- Payment against invoice is a separate posting (debit bank, credit receivable / debit payable, credit bank)
- Period-end adjustments: accrue uninvoiced revenue/expenses, defer prepaid items

**Determination of basis:**
1. User states their basis in Step 4 → use it
2. User does not state → apply the country skill's default for the entity type
3. Country skill is silent → sole traders use cash basis, companies use accrual basis
4. If the data clearly shows accrual patterns (invoices with later payment) but the user claimed cash basis, flag in the reviewer brief — do not override the user's stated basis

---

## Section 5 — Self-checks (run before delivering output)

Run these twelve checks against all outputs. If any fails, fix and re-run. Do not deliver until all pass.

### Structural integrity

**Check 1 — Trial balance balances.** Total debits on the trial balance exactly equal total credits. Not approximately — exactly. A difference of even 0.01 means a posting error exists.

**Check 2 — Completeness.** Every transaction in the source data appears exactly once in the transaction register, either classified (with debit and credit accounts) or excluded (with reason). Count source transactions; count register rows; they must match.

**Check 3 — Double-entry integrity.** Every journal entry in the transaction register has equal debits and credits. Sum all debit postings; sum all credit postings across the entire register; they must be equal.

**Check 4 — Bank reconciliation ties out.** The closing bank balance per ledger equals the closing bank balance per bank statement, after accounting for listed unmatched items. If unmatched items exist, the ledger balance ± unmatched items = bank statement balance.

### Cross-document consistency

**Check 5 — P&L matches trial balance.** Net profit on the P&L equals the sum of all revenue account balances minus the sum of all expense account balances on the trial balance. No rounding differences.

**Check 6 — Balance sheet balances.** Total assets on the balance sheet equal total liabilities plus total equity. The accounting equation must hold.

**Check 7 — Balance sheet matches trial balance.** Every asset, liability, and equity account balance on the balance sheet matches the corresponding balance on the trial balance.

**Check 8 — Tier 2/3 disclosure.** Every transaction marked as Tier 2 or Tier 3 in the transaction register has a corresponding entry in the reviewer brief (in "Assumptions made" for Tier 2, in "Questions asked" for Tier 3). Count on both sides; they must match.

### Logical consistency

**Check 9 — No personal transactions in business P&L.** No transaction classified as personal (excluded for personal reasons) appears in any revenue or expense account. Scan the P&L account codes; none should contain items flagged as personal in the register.

**Check 10 — Revenue matches bank deposits.** Total revenue on the P&L should be reconcilable to total receipts in the bank account, adjusted for: non-revenue receipts (loans, owner injections, refunds), opening receivables (accrual basis), and timing differences. If the figures cannot be reconciled within the reviewer brief, flag it.

**Check 11 — All nominal codes are valid.** Every nominal code used in the transaction register exists in the country skill's chart of accounts. No invented codes. No codes from a different country's chart.

**Check 12 — VAT/GST control account reconciles.** If a tax skill is also loaded: the VAT/GST control account balance on the trial balance equals the net amount payable/refundable on the VAT/GST return (or the amount already paid to the tax authority, plus any outstanding balance). If no tax skill is loaded, this check is skipped.

### Failure handling

If any check fails, fix the output and re-run all twelve. Do not deliver until all pass. If a check fails twice in a row on the same item, stop and report the failure to the user rather than silently working around it.

---

## Section 6 — What this file is NOT

This file does NOT contain:

- **No chart of accounts.** The nominal codes, account names, and account groupings come from the country-specific bookkeeping skill.
- **No tax rates.** VAT, GST, income tax, corporation tax — all come from separate tax skills.
- **No jurisdiction-specific GAAP.** Local accounting standards, micro-entity exemptions, filing requirements — all from the country skill.
- **No P&L or balance sheet format.** Single-step vs. multi-step, horizontal vs. vertical, grouping conventions — all from the country skill.
- **No currency conventions.** Base currency, decimal separators, thousand separators, rounding rules — all from the country skill.
- **No bank format patterns.** CSV column layouts, date formats, description field parsing — all from the country skill.
- **No sample transactions or worked examples.** Those live in country skills to avoid eval contamination.
- **No filing requirements.** Deadlines, portals, statutory accounts formats — all from the country skill.

This file cannot produce any output without a country-specific companion. It is the engine without fuel. If loaded alone, refuse to proceed and ask which country the accounts are for.

---

## Section 7 — Country skill contract

Every country-specific bookkeeping skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Chart of accounts** — complete list of nominal codes, account names, account types (asset/liability/equity/revenue/COGS/expense), and normal balance direction (debit/credit). Minimum 30 accounts for a sole trader chart, 50+ for a company chart.

2. **P&L format specification** — single-step or multi-step, category groupings (with the nominal codes that belong to each group), subtotal points, local terminology.

3. **Balance sheet format specification** — horizontal or vertical presentation, current vs. non-current classification thresholds (e.g., 12 months), groupings, local terminology.

4. **Local GAAP requirements for micro-entities/sole traders** — simplified reporting options, exemptions from full accounts, abbreviated balance sheet rules.

5. **Classification rules** — country-specific Tier 1 rules mapping common transaction types to nominal codes. Minimum 20 rules covering: revenue types, common expense categories, owner transactions, payroll, statutory payments, bank charges, fixed asset thresholds.

6. **Supplier/payee pattern library** — lookup table mapping common counterparty patterns to their nominal code treatment. Similar to the VAT skill's supplier pattern library. Minimum 15 entries covering: major banks, utilities, telecoms, tax authorities, pension/social security bodies, common SaaS providers.

7. **Exclusion patterns** — transactions that should be excluded from classification (inter-account transfers, duplicates, non-financial items) with the local-language patterns that identify them.

8. **Conservative defaults** — country-specific concrete defaults for each ambiguity type in Section 2. What nominal code to use when uncertain about each common ambiguity.

9. **Materiality threshold** — the amount below which transactions can be classified using simplified rules or grouped into a sundry/miscellaneous account.

10. **Bank statement format guide** — local CSV format conventions, common bank export column names, date formats (DD/MM/YYYY vs. MM/DD/YYYY vs. YYYY-MM-DD), description field structure, known bank quirks.

11. **Currency and number format** — base currency, ISO code, decimal separator (. or ,), thousand separator, rounding rules (bankers rounding, truncation, etc.).

12. **Entity type defaults** — for each entity type common in the country (sole trader, partnership, private limited company, etc.): default accounting basis, default chart complexity level, default reporting requirements.

### Optional slots

13. **Industry-specific chart extensions** — additional nominal codes for common industries (construction, hospitality, retail, professional services) beyond the base chart.

14. **Year-end adjustment guidance** — depreciation methods, accrual conventions, stock valuation methods common in the country.

15. **Integration notes** — how the bookkeeping skill interacts with the country's VAT/GST skill, payroll skill, or income tax skill if loaded simultaneously.

---

## Section 8 — Reference material

### Validation status

This file is v1.0 of `bookkeeping-workflow-base`, drafted as part of the Open Accountants skill architecture in May 2026. It follows the structural pattern established by `vat-workflow-base` v0.2.0 and extends it to general bookkeeping.

### Design decisions

1. **Three-tier vs. two-tier classification.** The VAT workflow uses two tiers (know vs. don't know). Bookkeeping uses three tiers because the "don't know" category splits into two meaningfully different cases: "I can make a conservative assumption" (Tier 2) and "I genuinely cannot classify without user input" (Tier 3). The tax impact of a bookkeeping misclassification is less immediate than a VAT box error, so the tolerance for Tier 2 assumptions is higher.

2. **No mandatory Excel output.** Unlike the VAT workflow, bookkeeping outputs are specified format-agnostically. Country skills may specify Excel, CSV, or JSON output depending on local tooling conventions.

3. **Bank as control account.** The bank account is always the anchor. All bank statement transactions post through it. This makes reconciliation the primary integrity check, which aligns with practitioner workflows.

4. **Cash vs. accrual flexibility.** The workflow supports both bases because different entity types in different countries use different bases. The country skill specifies the default; the user can override.

### Known gaps

1. Multi-currency bookkeeping is acknowledged but not deeply specified. A future `multi-currency-workflow-base` may extend this.
2. Fixed asset registers and depreciation schedules are referenced but not fully specified at the workflow level.
3. Payroll journal integration is stub-level — a payroll-workflow-base would need to specify the full interaction.
4. Stock/inventory valuation is not covered beyond classification of purchases.
5. The 12 self-checks are deterministic integrity checks, not substantive correctness checks. A line-by-line review pass (analogous to vat-workflow-base Step 7.5) may be added in a future version.

### Change log

- **v1.0 (May 2026):** Initial release. Establishes the universal bookkeeping workflow, three-tier classification system, five-output specification, 12 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
