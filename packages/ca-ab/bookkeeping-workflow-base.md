---
name: bookkeeping-workflow-base
description: "Shared bookkeeping preparation method for source intake, confirmed entity/framework and chart, classification, double-entry journals, bank/tax reconciliation, trial balance, reporting and reviewer handoff. Country and entity rules remain necessary for legal basis, recognition, tax and filing. Preserves every source transaction and supports read-only ledgers through proposed journals/import files rather than unauthorised posting."
version: 1.1
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-11-14
tax_year: 2026
type: cross-country-method
tier: 2
domain: bookkeeping
---

# Bookkeeping Workflow Base Skill v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a bookkeeping task: the order of operations, how to classify transactions, how to handle ambiguity, what to produce as output, what to check before delivering. It supplies no country chart/nominal codes, statutory reporting layout or currency policy. Its bounded IFRS and UK tax examples explain recognition boundaries and do not replace the applicable country/entity rules.

**This file must always be loaded with a country-specific bookkeeping skill** that provides the chart of accounts, reporting formats, and local conventions (e.g., `uk-bookkeeping`, `au-bookkeeping`, `de-bookkeeping`). Without the actual entity chart, reporting framework/basis and required country rules, do not present a final compliant trial balance, P&L or balance sheet. Claude can still inventory evidence, reconcile source completeness and prepare clearly provisional mappings/questions; do not refuse all useful preparation merely because a catalogue companion is missing.

**This file is the contract.** When a country bookkeeping skill says it conforms to v1.1 of this base, it means: it fills the country slots specified in Section 7, it produces outputs in the format specified in Section 3, its classifications can be validated by the self-checks in Section 5, and it participates in the workflow in Section 1.

---

## Ask the client first

Read the existing client record, intake, prior accounts, chart and supplied documents first. Confirm legal entity and reporting jurisdiction/framework; period and opening balances; functional/reporting and transaction currencies; financial-reporting versus tax basis/election; bank/payment channels, VAT/GST and payroll registration; source completeness and requested delivery/access. Country, counterparties and bank patterns are clues, not proof of legal status. Ask only for missing facts.

## The method, step by step

You are helping a small business owner produce bookkeeping records from raw financial data. The output will be reviewed by a qualified accountant before use. Your job is to do the mechanical classification and posting work and produce a working set of accounts plus a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these nine steps in order. Do not skip. Do not reorder. Do not start classifying transactions before step 4. Do not build any output files before step 6.

### Step 1 : Confirm the companion skills are loaded

This workflow base requires a country-specific bookkeeping skill providing the chart of accounts, reporting format, and local conventions.

If the country/framework/companion is missing, first search the current available catalogue using facts already in the client record. Ask only for missing jurisdiction/framework. Continue safe source inventory, but hold final classifications/reports that require missing legal/accounting rules and list the exact gap. An unapproved companion does not acquire an approval from this base.

If a VAT or GST workflow skill is also loaded, note its presence : reconciliation between the bookkeeping ledger and the tax control account will be required at Step 7.

### Step 2 : Read the data

The user will provide one or more of: bank statements (CSV, PDF, or pasted text), invoices, receipts, or a combination. Read every line of every document provided. Do not skim. Identify:

- The period covered (earliest transaction date to latest)
- Every source currency, actual functional/reporting currency and conversion evidence; a country does not necessarily prescribe the entity's functional currency. Retain original amounts and flag unresolved FX rules/rates
- The number of transactions across all sources
- The source type for each document (bank statement, sales invoice, purchase invoice, receipt, journal entry)
- Any obvious format problems (missing columns, truncated data, unreadable encoding, duplicate documents)
- Whether the data set is complete for the period (gaps in date sequences, missing months)

If the data is unreadable, covers a different country than the loaded skill, or is so incomplete that a meaningful trial balance cannot be produced, stop and tell the user.

### Step 3 : Infer the client profile from the data

Before asking the user onboarding questions, attempt to infer the client profile from the data alone. Look for:

- **Entity type.** Drawings, salaries, share capital and dividend descriptions suggest questions but do not prove sole-trader/company/employee status. Use actual registration, ownership and contracts before entity-dependent treatment.
- **Industry signals.** Stock purchases (retail/wholesale), subcontractor payments (construction/services), raw materials (manufacturing), booking platforms (hospitality), patient references (healthcare).
- **Scale indicators.** Monthly transaction volume, typical transaction size, number of distinct customers and suppliers, presence of fixed assets.
- **Accounting basis signals.** Invoice/payment timing and prepayments help identify missing evidence; they do not establish a legally permitted basis or election. Separate financial reporting from the tax computation and reconcile to prior policy.
- **VAT/GST registration signals.** Tax authority payments, round-number quarterly payments to revenue bodies, VAT-inclusive pricing patterns in descriptions.
- **Employees.** Payroll patterns, pension contributions, social security payments to known statutory bodies.
- **Fixed assets.** Large one-off purchases, hire purchase or lease payments, depreciation-eligible items.
- **Multi-currency activity.** Foreign currency transactions, exchange rate differences, international supplier payments.

Produce a one-paragraph inferred profile. State it as a hypothesis, not a fact.

### Step 4 : Confirm the inferred profile (one round trip)

Output the inferred profile to the user in this exact form:

> "Based on the data provided, here is what I believe about your situation:
>
> [One paragraph: entity type, industry, scale, accounting basis, VAT status, employee status, fixed asset presence, period covered.]
>
> Is this correct? If anything is wrong, tell me and I will adjust before I start classifying. If it is correct, reply 'confirmed' and I will proceed."

Wait for confirmation. If the user corrects anything, update the profile and re-confirm in one sentence. Do not ask a full onboarding questionnaire : only ask follow-ups for items the data could not infer at all.

### Step 5 : Transaction classification to nominal codes

For every transaction across all data sources, in chronological order:

1. **Source matching and exclusion:** assign stable document/line and transaction/journal IDs. Link duplicate copies to the retained source; distinguish a duplicate invoice from a legitimate bank settlement of that invoice. Exclude only genuine duplicate representations/non-financial lines, with the retained reference and reason. Inter-account transfers remain postings between bank accounts, including any fee/FX legs. Personal payments from a business bank remain bank entries with the actual drawings, equity, receivable or other supported counterpart, outside business P&L where appropriate.

2. **Tier 1 classification (Confident).** Check the transaction against the country skill's classification rules and chart of accounts. If the transaction clearly maps to one and only one nominal code with no ambiguity from the data alone, classify it. Examples: evidenced bank charges may map to bank fees; confirmed utility supply may map to utilities subject to period/tax treatment. A salary bank payment usually settles net-pay liability after the gross payroll journal; do not automatically debit gross wages again.

3. **Tier 2 classification (Assumed).** If a supported provisional mapping can be made without inventing recognition, tax eligibility or legal status, record it with the evidence, alternative and effect. Prudence does not authorise a systematically lower asset/profit or higher revenue. Where the uncertainty changes recognition or tax treatment, keep the counterpart unresolved and follow Section 2.

4. **Tier 3 classification (Needs Input).** If the transaction cannot be classified without information only the user has, queue it for the user question step. Do not guess. Examples: large round-number transfer (loan repayment? owner injection? inter-company?), payment to an individual (subcontractor? employee? personal?), mixed-use expense (what percentage business?).

Every transaction MUST end up in exactly one state: excluded with reason, classified at Tier 1, classified at Tier 2 with default and flag, or queued as Tier 3 for user input. No transaction may be silently dropped.

### Step 5.5 : Ask the user about Tier 3 items

Before building any output, present Tier 3 items to the user grouped by category. Order by financial impact (largest amounts first). For each item or group:

- Name the transaction(s) explicitly (date, counterparty, amount)
- Explain what information is needed
- Offer 2-4 options where possible
- Include "Don't know, keep unresolved for review"; never offer a default that invents a business purpose, legal relationship or tax entitlement

Wait for the user's answers. Apply them to the classification. Any items where the user selects "don't know" stay unresolved in the reviewer brief. Where a draft balancing counterpart is necessary, use only an existing authorised suspense/clearing account with a separate schedule; do not turn the uncertainty into final revenue, expense or personal expenditure.

### Step 6 : Double-entry posting

For every classified transaction, create the double-entry journal:

- Every debit has an equal and opposite credit. No exceptions.
- Bank account is the control account for bank statement transactions.
- Sales ledger (accounts receivable) is the control for sales invoices.
- Purchase ledger (accounts payable) is the control for purchase invoices.
- For a confirmed eligible cash-basis tax computation, apply the actual receipt/payment, capital, private-use and VAT rules. Do not infer that every bank deposit is income or every payment deductible. Maintain the full cash/bank record and a separate tax bridge.
- For accrual reporting, apply the actual recognition framework and performance/receipt period, not invoice date alone. Under IFRS 15 revenue follows the satisfied performance obligation; an early invoice/payment can be a receivable/contract liability rather than earned revenue. Post settlement separately against the existing receivable/payable. [IFRS 15 overview](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/).
- VAT/GST: establish actual registration, tax point, recoverability, special scheme and reporting basis; a loaded skill is evidence assistance, not eligibility. Post confirmed control accounts and timing differences per the country method. If tax facts are missing, preserve the gross source amount in a provisional schedule/authorised clearing treatment without pretending the full amount is final revenue, deductible expense or recoverable VAT. UK cash-basis VAT-inclusive/exclusive methods require consistent treatment and their actual conditions. [HMRC cash-basis records](https://www.gov.uk/simpler-income-tax-cash-basis/income-and-expenses-under-cash-basis).

Verify as you post: running total of debits must equal running total of credits at every point. If they diverge, stop and find the error before continuing.

### Step 7 : Reconciliation

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

### Step 8 : Trial balance and financial statements

Produce the trial balance: list every nominal code that has been posted to, with its debit or credit balance. Verify total debits equal total credits.

From the trial balance, produce:
- **Profit & Loss statement** in the format specified by the country skill (single-step or multi-step, grouped by the country skill's categories)
- **Balance sheet** in the format specified by the country skill (horizontal or vertical, current/non-current classification per the country skill)

Cross-check the equity roll-forward: opening equity/retained earnings plus the actual profit allocation and other recognised movements, contributions, distributions and permitted adjustments equals closing equity. Distinguish proprietor drawings from company dividends/director balances and retained earnings from other equity/OCI. A simple retained-earnings movement is not universally equal to net profit. Investigate every reconciling item.

### Step 9 : Build and deliver outputs

Produce the five output artefacts specified in Section 3, including a numbered proposed journal/import schedule within the transaction-register delivery. With read-only/no ledger access, supply import-ready journals or a clear list of postings for a human to approve. Never post, change master data, create bank transactions or run an import merely because credentials are available. Validate the target template and dates/accounts/tax codes in a preview. Run Section 5; final-ready outputs require all applicable checks and resolved material issues. A clearly labelled exception draft can be delivered with failing checks/uncertainty visible, without claiming completed accounts.

Write a short closing chat response:
- Net profit/loss figure for the period
- One sentence on what each output file contains
- The highest-priority item from the reviewer brief
- An invitation to revise: "If any classification needs changing, tell me which transaction and I'll update the accounts."

---

## Section 2 : Classification rules and conservative defaults

Every transaction falls into one of three tiers.

### Tier 1 : Confident

The transaction clearly maps to one nominal code with no ambiguity. The counterparty, description, amount pattern, and context all point to the same account. A competent bookkeeper looking at the same data would reach the same conclusion without hesitation.

**Action:** Record the mapping and supporting source without unnecessary narration. Retain the audit trail and any tax/period issue even if the nominal code is clear.

### Tier 2 : Assumed

The transaction could reasonably map to two or more nominal codes. The data provides clues but not certainty. A competent bookkeeper would classify it but note the assumption.

**Action:** Use only a supported provisional mapping, flag the alternative and recognition/tax effect in the reviewer brief, and record it as Tier 2. Otherwise use Tier 3/unresolved rather than invent a default.

### Tier 3 : Needs Input

The transaction cannot be classified without information only the user possesses. The data provides insufficient clues for even a conservative assumption.

**Action:** Queue for user question in Step 5.5. Do not guess. A user answer supplies facts, not permission to override the applicable framework. "Don't know" preserves an unresolved item; it does not make an invented classification correct.

### Evidence-first treatment of uncertain classifications

Prudence is not a licence to force every uncertain item into an immediate expense or taxable revenue. Preserve the cash/source record and investigate the actual framework before final recognition:

- **Expense versus capital:** establish what was acquired, expected use and applicable recognition/materiality policy. An item meeting the applicable asset criteria is not expensed just because capitalisation is uncertain. Conversely, a tax cash-basis deduction can differ from financial-statement recognition. [IAS 16 recognition/cost overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/), [HMRC UK cash-basis equipment distinction](https://www.gov.uk/simpler-income-tax-cash-basis/income-and-expenses-under-cash-basis).
- **Business versus personal:** establish ownership/purpose. Exclude a proved personal amount from business P&L/deduction, but retain any business-bank movement and supported owner/related-party counterpart. Unknown purpose is unresolved, not proof that the transaction never occurred.
- **Current period versus prepaid/accrued:** establish the supplied/consumed period and actual accounting basis; do not expense a future-period service merely to lower profit. Keep an adjustment schedule and recognition evidence.
- **Revenue versus loan/capital/customer advance:** establish the counterparty, agreement and performance. A loan, capital contribution, inter-account transfer or unearned customer advance is not automatically revenue. For IFRS contracts apply the actual performance-obligation analysis. [IFRS 15](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/).
- **Inventory/cost of sales versus operating expense:** distinguish purchases, held stock and the period in which related revenue is recognised. Under IAS 2, sold inventory cost is expensed with the related revenue and remaining inventory has its own measurement test; calling all purchases operating expense can change profit, not just gross margin. [IAS 2 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/).
- **Current versus non-current liability:** establish contractual maturity, rights and the actual reporting-date framework; do not force all uncertainty to current classification. Refer unresolved covenant/refinancing questions to the reporting specialist.
- **Gross versus net tax:** keep original gross evidence and separately resolve actual tax status, recoverability and timing. A country skill's absence does not authorise a final gross P&L posting, and loading one does not prove a tax claim.

The country/entity method supplies actual codes, permitted policies and legal conditions. The uncertainty schedule identifies missing evidence, proposed counterpart, alternatives and whether the draft statements remain incomplete.

### Mixed-use transaction handling

When a transaction is partially business and partially personal:

- If the user has stated a business-use percentage, apply it.
- If the user has not stated a percentage and the item is commonly mixed-use (vehicle, phone, home office), ask in Step 5.5.
- If the user selects "don't know," keep the use allocation unresolved; do not fabricate zero business use, erase the bank movement or claim a tax deduction. Obtain a permitted allocation method and evidence from the country rule.
- Record the supported split and its source (records/user facts and applicable country rule); distinguish accounting allocation from tax allowability and flag unsupported percentages.

### Recurring vs. one-off treatment

- A recurring counterparty is a reusable mapping suggestion, not automatic recognition/tax proof. Check document, purpose, period and exceptions for each occurrence; flag changed facts and prevent duplicated invoice/payment postings.
- As an internal review heuristic, flag recurring amount changes above 20%, and any changed nature/currency/tax/period even below that. This percentage is not a legal materiality threshold or authority to keep a wrong classification.
- One-off large transactions (above the country skill's materiality threshold) always receive individual attention regardless of Tier.

### Revenue recognition timing

- **Cash-basis tax records:** recognise actual eligible receipts/payments under the applicable country scheme, including non-bank settlement where required. Keep unpaid invoice information as a control even when it does not enter that tax-basis profit; do not equate a tax record with statutory accrual financial statements.
- **Accrual basis:** establish the actual recognition/performance/consumption period, receivables/payables, inventory, assets, prepayments/accruals and any contract liability. Invoice date is a source field, not a universal recognition rule. [IFRS 15](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/), [IAS 2](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/).
- Confirm the actual legally permitted basis/election and purpose in Step 4. Never default every sole trader worldwide to cash basis. The UK tax scheme is one bounded example with entity exclusions and an alternative traditional method, not a worldwide accounting policy. [HMRC eligibility](https://www.gov.uk/simpler-income-tax-cash-basis/who-can-use-cash-basis).

---

## Section 3 : Output specification

For a full-period bookkeeping preparation engagement, deliver all five related outputs or explicitly mark which are incomplete and why. Preserve the numbered journals as part of the transaction-register delivery. A narrower reconciliation/diagnostic request may deliver its requested working papers without claiming a complete set of accounts.

### Output 1 : Trial balance

Tabular format with columns:

| Column | Content |
|---|---|
| Account code | The nominal code from the country skill's chart |
| Account name | The descriptive name |
| Debit balance | Positive number if the account has a debit balance |
| Credit balance | Positive number if the account has a credit balance |

Footer row: total debits, total credits (must be equal).

Grouped by category per the country skill's chart structure (assets, liabilities, equity, revenue, cost of sales, expenses).

### Output 2 : Profit & Loss statement

Format per the country skill's specification. Universal structure:

```
Revenue (grouped by category)
- Cost of goods sold (if applicable)
= Gross profit
- Operating expenses (grouped by category per country skill)
= Operating profit / Net profit before tax
- Tax (if the actual taxes apply and their rules are available)
= Net profit after tax
```

Each line item shows the nominal code, description, and amount. Categories are subtotalled. The country skill specifies whether single-step (all revenue minus all expenses) or multi-step (with gross profit intermediate).

### Output 3 : Balance sheet

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
    Tax liabilities (where actually applicable, whether or not a tax skill is loaded)
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

### Output 4 : Reviewer brief

A short narrative document for the human reviewer:

```markdown
# [Country] Bookkeeping : Reviewer Brief
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
[For each Tier 3 item: the question, the user's answer or "don't know :
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

### Output 5 : Transaction register

Every transaction with full classification detail:

| Column | Content |
|---|---|
| Date | Transaction date |
| Source | Bank/invoice/receipt reference |
| Counterparty | Name |
| Description | As provided in source data |
| Gross amount | Original amount |
| Net amount | Confirmed net amount under actual tax treatment; unresolved split identified |
| Tax amount | Confirmed tax amount and control/recoverability treatment, not inferred from skill presence |
| Debit account | Nominal code and name |
| Credit account | Nominal code and name |
| Confidence tier | 1, 2, or 3, internal workpaper status only, never a professional approval |
| Match/journal ID | Source line IDs, invoice/payment match, transfer pair, split lines and proposed import/journal reference |
| Resolution | Confirmed/provisional/unresolved and effect on readiness |
| Notes | Assumptions, user answers, flags |
| Excluded | Y/N with reason if Y |

---

## Section 4 : Detailed classification guidance

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
- Payments to retail stores without purpose evidence: unresolved/Tier 3 as necessary; a small amount does not prove personal use or justify dropping a business-bank line
- Consumer subscriptions/insurance: investigate actual purpose and contractual payer. Proven personal costs stay out of business P&L but a business-bank payment still needs its supported counterpart
- Mixed-use utilities (home office): Tier 3 : ask for business-use percentage

### Recurring vs. one-off treatment

- First occurrence of a new counterparty: classify on its merits
- Later similar-counterparty occurrences: reuse only a mapping suggestion after checking current source purpose, period/tax facts and invoice/payment match; do not re-recognise a settled invoice
- If a recurring pattern breaks (amount doubles, frequency changes, description changes): re-evaluate as if new, flag in reviewer brief

### Revenue recognition timing

**Cash basis recognition:**
- Sales: apply the actual permitted receipt convention; include relevant cash/card/cheque/in-kind channels, not bank deposits alone. [HMRC UK cash records](https://www.gov.uk/simpler-income-tax-cash-basis/income-and-expenses-under-cash-basis)
- Purchases: apply the actual eligible-payment convention and capital/private-use/tax rules, retaining non-bank payments and source evidence
- A tax cash-basis profit schedule is not necessarily a statutory balance sheet. Retain invoice/settlement controls and establish which statement basis is actually requested
- Prepayments and accruals may still exist depending on country GAAP

**Accrual basis recognition:**
- Sales: apply the actual recognition/performance condition, separately recording invoice, delivery, receipt and any unearned advance; do not default to invoice date. [IFRS 15](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/)
- Purchases: establish actual receipt/consumption, inventory/asset recognition, payable and period, including uninvoiced items; invoice date alone is insufficient
- Payment against invoice is a separate posting (debit bank, credit receivable / debit payable, credit bank)
- Period-end adjustments: accrue uninvoiced revenue/expenses, defer prepaid items

**Determination of basis:**
1. User states a basis: verify its permitted application, purpose and election/previous policy before use
2. User does not state → apply the country skill's default for the entity type
3. Country skill is silent: keep the basis unresolved and obtain the actual framework; no worldwide entity-based default
4. If transaction patterns or the actual legal framework conflict with the stated basis, reconcile and flag the conflict. An invoice before payment can exist under cash-basis tax records; it does not by itself prove accrual, and a user choice cannot override a mandatory reporting framework

---

## Section 5 : Self-checks (run before delivering output)

Run all twelve applicable checks. Fix and re-run failures before describing a pack as final-ready. An exception draft may be delivered with the exact unresolved/failing checks and missing evidence visible, as in Step 9.

### Structural integrity

**Check 1 : Trial balance balances.** Total debits on the trial balance exactly equal total credits. Not approximately : exactly. A full-precision posting difference is an unresolved error. Distinguish documented presentation rounding from ledger equality; retain any actual rounding adjustment and never conceal a difference with an unexplained plug.

**Check 2: Completeness.** Every source line has a disposition and retained reference. Distinguish source documents/lines, unique economic events and journal lines: split entries and an invoice plus its settlement can legitimately require more rows. Link duplicates to their retained event; match invoice/payment, bank transfers, fees, FX and owner movements. Reconcile source counts through the matching map, not a false requirement that raw line count equals journal count.

**Check 3 : Double-entry integrity.** Every journal entry in the transaction register has equal debits and credits. Sum all debit postings; sum all credit postings across the entire register; they must be equal.

**Check 4 : Bank reconciliation ties out.** The closing bank balance per ledger equals the closing bank balance per bank statement, after accounting for listed unmatched items. If unmatched items exist, the ledger balance ± unmatched items = bank statement balance.

### Cross-document consistency

**Check 5 : P&L matches trial balance.** Net profit on the P&L equals the sum of all revenue account balances minus the sum of all expense account balances on the trial balance. Reconcile any permitted display rounding explicitly to the full-precision ledger.

**Check 6 : Balance sheet balances.** Total assets on the balance sheet equal total liabilities plus total equity. The accounting equation must hold.

**Check 7 : Balance sheet matches trial balance.** Every asset, liability, and equity account balance on the balance sheet matches the corresponding balance on the trial balance.

**Check 8 : Tier 2/3 disclosure.** Every transaction marked as Tier 2 or Tier 3 in the transaction register has a corresponding entry in the reviewer brief (in "Assumptions made" for Tier 2, in "Questions asked" for Tier 3). Count on both sides; they must match.

### Logical consistency

**Check 9 : No personal transactions in business P&L.** No transaction classified as personal (excluded for personal reasons) appears in any revenue or expense account. Scan the P&L account codes; none should contain items flagged as personal in the register.

**Check 10: Revenue/cash bridge.** Reconcile recognised revenue to all cash/bank/processor channels through VAT/GST, fees, refunds/credit notes, opening/closing receivables, advances/deferred revenue, loans/capital/transfers, foreign exchange and other timing differences as applicable. A processor net settlement is not necessarily gross revenue. If the bridge cannot be supported, flag the exact difference.

**Check 11 : All nominal codes are valid.** Every nominal code used in the transaction register exists in the country skill's chart of accounts. No invented codes. No codes from a different country's chart.

**Check 12: VAT/GST control roll-forward.** Where registered/relevant, reconcile opening balance plus actual period output/reverse-charge tax minus allowable input/credits, adjustments, payments/refunds and documented timing/other-period items to closing balance and the actual return. A closing control balance need not equal a single return when prior periods/payment timing differ. Missing tax rules or registration facts are an unresolved check, not an automatic skip because no skill was loaded.

### Failure handling

If a check fails, fix the output and re-run all twelve. Do not represent an exception draft as a final-ready pack until all applicable checks pass. If a check fails twice on the same item, stop finalisation and report the exact failure, attempted fixes and evidence needed; never conceal it with a balancing plug. Preserve the exception draft for review.

---

## Section 6 : What this file is NOT

This file does NOT contain:

- **No chart of accounts.** The nominal codes, account names, and account groupings come from the country-specific bookkeeping skill.
- **No tax rates.** VAT, GST, income tax, corporation tax : all come from separate tax skills.
- **No jurisdiction-specific GAAP.** Local accounting standards, micro-entity exemptions, filing requirements : all from the country skill.
- **No P&L or balance sheet format.** Single-step vs. multi-step, horizontal vs. vertical, grouping conventions : all from the country skill.
- **No currency conventions.** Base currency, decimal separators, thousand separators, rounding rules : all from the country skill.
- **No bank format patterns.** CSV column layouts, date formats, description field parsing : all from the country skill.
- **No country rate/form examples.** The bounded mechanical worked cases below test source matching and recognition boundaries; country examples remain necessary for local tax/GAAP rules.
- **No filing requirements.** Deadlines, portals, statutory accounts formats : all from the country skill.

Without a country/entity companion or actual rules, keep missing-rule classifications/reports provisional. Safe evidence inventory and mechanical reconciliation can continue. Do not invent nominal codes, framework or tax treatment, and do not call a provisional pack compliant final accounts.

---

## Section 7 : Country skill contract

Every country-specific bookkeeping skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Chart of accounts** : complete list of nominal codes, account names, account types (asset/liability/equity/revenue/COGS/expense), and normal balance direction (debit/credit). The chart must fit the actual entity and reporting needs; historic minimum account counts were internal design suggestions, not legal requirements or proof of completeness.

2. **P&L format specification** : single-step or multi-step, category groupings (with the nominal codes that belong to each group), subtotal points, local terminology.

3. **Balance sheet format specification** : horizontal or vertical presentation, current vs. non-current classification thresholds (e.g., 12 months), groupings, local terminology.

4. **Local GAAP requirements for micro-entities/sole traders** : simplified reporting options, exemptions from full accounts, abbreviated balance sheet rules.

5. **Classification rules** : country-specific Tier 1 rules mapping common transaction types to nominal codes. Include supported rules covering: revenue types, common expense categories, owner transactions, payroll, statutory payments, bank charges, fixed asset thresholds.

6. **Supplier/payee pattern library** : lookup table mapping common counterparty patterns to their nominal code treatment. Similar to the VAT skill's supplier pattern library. Include verified patterns, used as suggestions rather than final recognition proof, covering: major banks, utilities, telecoms, tax authorities, pension/social security bodies, common SaaS providers.

7. **Exclusion patterns** : actual duplicate representations/non-financial items that may be excluded, with retained match references; bank transfers and personal bank movements remain postings rather than disappearing with the local-language patterns that identify them.

8. **Conservative defaults** : country-specific concrete defaults for each ambiguity type in Section 2. How to preserve an unresolved counterpart and obtain evidence without inventing final recognition or tax eligibility.

9. **Materiality threshold** : a documented applicable entity/framework review or aggregation policy, not permission to erase transactions, invent purpose or ignore legal/tax conditions.

10. **Bank statement format guide** : local CSV format conventions, common bank export column names, date formats (DD/MM/YYYY vs. MM/DD/YYYY vs. YYYY-MM-DD), description field structure, known bank quirks.

11. **Currency and number format** : base currency, ISO code, decimal separator (. or ,), thousand separator, rounding rules (bankers rounding, truncation, etc.).

12. **Entity type defaults** : for each entity type common in the country (sole trader, partnership, private limited company, etc.): default accounting basis, default chart complexity level, default reporting requirements.

### Optional slots

13. **Industry-specific chart extensions** : additional nominal codes for common industries (construction, hospitality, retail, professional services) beyond the base chart.

14. **Year-end adjustment guidance** : depreciation methods, accrual conventions, stock valuation methods common in the country.

15. **Integration notes** : how the bookkeeping skill interacts with the country's VAT/GST skill, payroll skill, or income tax skill if loaded simultaneously.

---

## Section 8 : Reference material

### Validation status

This file is v1.1 of `bookkeeping-workflow-base`, updated in November 2026 from the original draft as part of the Open Accountants skill architecture in May 2026. It follows the structural pattern established by `vat-workflow-base` v0.2.0 and extends it to general bookkeeping.

### Design decisions

1. **Three-tier vs. two-tier classification.** The VAT workflow uses two tiers (know vs. don't know). Bookkeeping uses three tiers because the "don't know" category splits into two meaningfully different cases: "I can make a conservative assumption" (Tier 2) and "I genuinely cannot classify without user input" (Tier 3). These are internal uncertainty states, not professional approval or evidence that accounting errors have lower risk; recognition/tax assumptions remain explicit and unresolved when unsupported.

2. **No mandatory Excel output.** Unlike the VAT workflow, bookkeeping outputs are specified format-agnostically. Country skills may specify Excel, CSV, or JSON output depending on local tooling conventions.

3. **Bank as control account.** The bank account is always the anchor. All bank statement transactions post through it. This makes reconciliation the primary integrity check, which aligns with practitioner workflows.

4. **Cash vs. accrual flexibility.** The workflow supports both bases because different entity types in different countries use different bases. The actual permitted country/entity policy and tax election govern; the user supplies facts and permitted choices, not an override of mandatory rules.

### Known gaps

1. Multi-currency bookkeeping is acknowledged but not deeply specified. A future `multi-currency-workflow-base` may extend this.
2. Fixed asset registers and depreciation schedules are referenced but not fully specified at the workflow level.
3. Payroll journal integration is stub-level : a payroll-workflow-base would need to specify the full interaction.
4. Stock/inventory is covered only at recognition/expense boundary level; actual valuation/counts and local policy still need the country/entity method.
5. The 12 self-checks are deterministic integrity checks, not substantive correctness checks. A line-by-line review pass (analogous to vat-workflow-base Step 7.5) may be added in a future version.

### Change log

- **v1.0 (May 2026):** Initial release. Establishes the universal bookkeeping workflow, three-tier classification system, five-output specification, 12 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## When to refuse or refer

Hold final accounts/import when the opening balances, source completeness, legal entity, accounting basis, recognition or material tax treatment is unresolved. Preserve the source inventory, exception schedule and draft journals. Suspected fabricated documents, fraud, prohibited access or a request to conceal transactions needs specialist review and no unauthorised posting. Do not present balanced debits/credits as proof that recognition, tax treatment or source completeness is correct.

## Worked cases

**Invoice, net processor settlement and owner movements.** Assume a confirmed sole-trader accrual framework, no VAT in these illustrative amounts, opening bank/equity 1,000, an earned sale invoiced for 1,000, a processor settlement of 970 plus separately evidenced fee 30, owner capital contribution 2,000 and private withdrawal 200. The invoice creates revenue/receivable once; settlement clears the receivable, not another sale. Capital and drawings stay in the cash/equity records rather than disappearing. Closing bank is 3,770 and profit 970; equity reconciles to 3,770. Every amount is an assumed case fact, not a country threshold/rate. The actual revenue-recognition framework still controls when the invoice is earned. [IFRS 15 boundary](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/).

```oa-check
name: Match an invoice and settlement without duplicating revenue or dropping owner bank entries
inputs:
  opening_bank_and_equity: 1000
  earned_invoice: 1000
  processor_fee: 30
  capital_contributed: 2000
  owner_withdrawal: 200
steps:
  - bank_settlement: earned_invoice - processor_fee
  - receivable_remaining: earned_invoice - bank_settlement - processor_fee
  - closing_bank: opening_bank_and_equity + bank_settlement + capital_contributed - owner_withdrawal
  - net_profit: earned_invoice - processor_fee
  - closing_equity: opening_bank_and_equity + capital_contributed + net_profit - owner_withdrawal
  - accounting_difference: closing_bank - closing_equity
expected:
  bank_settlement: 970
  receivable_remaining: 0
  closing_bank: 3770
  net_profit: 970
  closing_equity: 3770
  accounting_difference: 0
```

**Capitalisation is a recognition decision, not an expense default.** Assume IAS 16 applies, the item meets its asset recognition criteria, a machine costs 1,200 with directly attributable delivery 100 and installation 200, and a separate evidenced current-period expense is 50. Recognised initial machine cost is 1,500, not an automatic immediate 1,500 expense. Current expense from the separately identified service is 50 before depreciation. Determine available-for-use date, useful life, residual value and actual policy before any depreciation/final profit; no depreciation rate is supplied by this example. A UK cash-basis tax equipment deduction can differ and needs a separate bridge. [IAS 16 cost/recognition](https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/), [HMRC UK cash-basis distinction](https://www.gov.uk/simpler-income-tax-cash-basis/income-and-expenses-under-cash-basis).

```oa-check
name: Recognised asset cost is not a conservative immediate expense
inputs:
  machine_price: 1200
  attributable_delivery: 100
  attributable_installation: 200
  separate_current_expense: 50
steps:
  - recognised_asset_cost: machine_price + attributable_delivery + attributable_installation
  - total_cash_paid: recognised_asset_cost + separate_current_expense
  - current_expense_before_depreciation: total_cash_paid - recognised_asset_cost
  - erroneous_extra_expense_if_all_expensed: total_cash_paid - current_expense_before_depreciation
expected:
  recognised_asset_cost: 1500
  total_cash_paid: 1550
  current_expense_before_depreciation: 50
  erroneous_extra_expense_if_all_expensed: 1500
```

## Sources

| Official source | What was actually read | Read on |
|---|---|---|
| https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/ | Read for the About overview's performance-obligation, transfer/control and over-time principles, not every standard paragraph or special contract | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/ | Read for the About overview's asset recognition and directly attributable cost conditions; no useful life, depreciation method or local threshold certified | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/ | Read for the About overview's inventory cost/measurement and sale-related expense recognition; not a full local GAAP implementation | 2026-11-14 |
| https://www.gov.uk/simpler-income-tax-cash-basis | Read for current UK tax cash-basis scope and alternative traditional accounting; not worldwide statutory accounting | 2026-11-14 |
| https://www.gov.uk/simpler-income-tax-cash-basis/who-can-use-cash-basis | Read for sole-trader/partnership eligibility, entity/trade exclusions and permitted alternative; no worldwide default adopted | 2026-11-14 |
| https://www.gov.uk/simpler-income-tax-cash-basis/income-and-expenses-under-cash-basis | Read for receipt/payment channels, consistency, equipment/cars and VAT-inclusive/exclusive conditions; not every linked expense/vehicle rule | 2026-11-14 |

Not yet confirmed: every client's actual reporting framework, chart, prior/opening balances, financial-reporting versus tax basis/election, functional currency/FX rules, tax registration and recoverability, capitalisation/materiality policy, useful lives/leases/impairment, inventory measurement, payroll/owner balances and filing rules. The IFRS overview examples are conditional and do not establish that a country/entity must use IFRS. The original universal expense, personal-exclusion, current-period, revenue, cash-basis and current-liability defaults are not adopted. The recurring-change percentage is an internal review heuristic, not a legal figure. No country tax rate or depreciation life is certified here.
