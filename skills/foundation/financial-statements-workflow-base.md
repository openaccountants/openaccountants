---
name: financial-statements-workflow-base
description: Universal financial statements preparation workflow base that defines the trial balance review, year-end adjustments, income statement and balance sheet preparation, notes to accounts, and filing runbook for all jurisdictions. Contains no jurisdiction-specific content — no local GAAP rules, no filing portals, no reporting thresholds, no specific account formats. This skill MUST be loaded alongside a country-specific financial statements skill that provides the reporting framework, format requirements, and local filing rules. This skill alone cannot produce any output.
version: 1.0
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-06-12
tier: 2
domain: financial-statements
---

# Financial Statements Workflow Base Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a financial statements preparation task: the order of operations, how to review a trial balance, how to post year-end adjustments, how to format an income statement and balance sheet, how to draft notes to accounts, what to check before delivering. It contains no local GAAP rules, no reporting thresholds, no specific account names, no filing portals, no audit exemption criteria, no depreciation rates.

**This file must always be loaded with a country-specific financial statements skill** that provides the reporting framework, P&L and balance sheet formats, notes requirements, and filing rules (e.g., `uk-financial-statements`, `au-financial-statements`, `de-financial-statements`). This file alone cannot produce a set of accounts. Loading it without a companion is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a country financial statements skill says it conforms to v1.0 of this base, it means: it fills the country slots specified in Section 5, it produces outputs in the format specified in Section 3, its outputs can be validated by the self-checks in Section 4, and it participates in the workflow in Section 1.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping a business owner or their accountant prepare a set of financial statements from a completed trial balance. The output will be reviewed by a qualified accountant before filing. Your job is to do the mechanical preparation work — reviewing the trial balance for completeness, posting year-end adjustments, formatting the statements per the applicable framework, and producing a reviewer brief that makes the professional's job fast and accurate.

Execute these eight steps in order. Do not skip. Do not reorder. Do not begin drafting statements before step 5. Do not build any output files before step 7.

### Step 1 — Confirm the companion skills are loaded

This workflow base requires a country-specific financial statements skill providing the reporting framework, statement formats, notes requirements, and filing rules.

If no country-specific skill is loaded, stop and tell the user: "I need a country-specific financial statements skill loaded alongside this workflow base. Which jurisdiction are these accounts for?" Do not proceed without it.

If a bookkeeping workflow skill is also loaded, note its presence — the trial balance from the bookkeeping skill is the input to this workflow. If a tax skill is loaded, note its presence — the tax provision computation in Step 4 can reference the tax skill's rates and rules.

### Step 2 — Determine the reporting framework

From the country skill and the client's details, establish:

- **Entity type.** The legal form determines which reporting framework and exemptions apply.
- **Entity size classification.** Apply the country skill's size thresholds (revenue, balance sheet total, employees) to classify as micro, small, medium, or large. This drives the level of detail required.
- **Applicable reporting framework.** Full local GAAP, simplified small-entity framework, micro-entity regime, or IFRS per the country skill. If the entity has a choice, present options and implications.
- **Reporting period.** Confirm financial year dates. Flag first accounting periods or changes of accounting date.
- **Comparative period.** Determine whether required (almost always above micro level) and whether available.
- **Going concern status.** Ask about indicators of going concern doubt. If present, this affects basis of preparation and requires specific disclosures.

Present the framework determination to the user:

> "Based on the entity details, here is the reporting framework I will apply:
>
> [Entity type, size classification, applicable framework, reporting period, comparative requirement, going concern assumption.]
>
> Is this correct? If anything needs adjusting, tell me before I begin reviewing the trial balance."

Wait for confirmation.

### Step 3 — Trial balance review

The user will provide a trial balance — either from the bookkeeping workflow output or as a separate document. Review it for completeness:

- **Balance check.** Total debits must equal total credits. If they do not, stop and tell the user the trial balance does not balance. Do not proceed with an unbalanced trial balance.
- **Account completeness.** Check that the trial balance contains accounts for all the categories expected by the country skill's chart of accounts: revenue, cost of sales (if applicable), operating expenses, fixed assets, current assets, current liabilities, long-term liabilities, equity. Flag any missing category.
- **Suspense accounts.** If any suspense account has a balance, flag it. Suspense accounts must be cleared before statements can be prepared.
- **Period consistency.** Verify that the trial balance period matches the reporting period established in Step 2. If the trial balance covers a different period, stop and clarify with the user.
- **Nominal code validity.** Every account code in the trial balance should exist in the country skill's chart of accounts. Flag any unrecognized codes.
- **Brought-forward balances.** If comparative figures are available, verify that the opening balances on the current trial balance match the closing balances from the prior period. Flag any discrepancies.
- **Obvious anomalies.** Credit balances on normally-debit accounts (e.g., a credit balance on a fixed asset account could indicate over-depreciation or disposal). Debit balances on normally-credit accounts (e.g., a debit balance on a creditor could indicate an overpayment). Unusually large or small balances relative to comparatives. Accounts with no movement in the period that previously had activity.

Produce a trial balance review summary listing any issues found. If no issues: "Trial balance reviewed — no issues found. Proceeding to year-end adjustments."

### Step 4 — Year-end adjustments

Review the trial balance and the user's supporting information for year-end adjustments that need to be posted. For each adjustment type, determine whether an adjustment is needed and compute the amount:

**Accrued expenses.** Expenses incurred before the year-end but not yet invoiced or paid. Common examples: utility bills covering the year-end, professional fees for year-end work, interest on loans, employee bonuses declared but not yet paid. For each: debit the expense account, credit accrued expenses (current liability).

**Accrued income.** Revenue earned before the year-end but not yet invoiced. For each: debit accrued income (current asset), credit the revenue account.

**Prepayments.** Expenses paid before the year-end that relate to periods after the year-end. Common examples: insurance premiums, rent paid in advance, subscription fees. For each: debit prepayments (current asset), credit the expense account. Compute the portion relating to the post-year-end period.

**Deferred income.** Revenue received before the year-end for services or goods to be delivered after the year-end. For each: debit the revenue account, credit deferred income (current liability).

**Depreciation.** For every fixed asset on the balance sheet, compute the depreciation charge for the period using the method specified by the country skill (straight-line, reducing balance, units of production). Apply the rates from the country skill's depreciation schedule. For assets acquired or disposed of during the period, pro-rate. Debit depreciation expense, credit accumulated depreciation.

**Amortization.** For intangible assets, compute amortization using the method and useful life specified by the country skill. Debit amortization expense, credit accumulated amortization.

**Provisions.** Review for items that require a provision:

- *Doubtful debts.* Review the trade debtors listing. Apply the country skill's provision policy (specific provision for known bad debts, general provision as a percentage of aged debtors). Debit bad debt expense, credit provision for doubtful debts.
- *Warranty provisions.* If the entity sells goods with warranties, estimate the provision based on historical claim rates. Debit warranty expense, credit warranty provision.
- *Legal provisions.* If the entity is party to legal proceedings with a probable adverse outcome and estimable cost, recognize a provision. Debit legal expense, credit legal provision.
- *Dilapidation provisions.* If the entity has lease obligations to restore premises, recognize a provision over the lease term.

**Inventory adjustments.** If the entity holds inventory: verify the closing inventory value per the count or valuation. Post any write-down from cost to net realizable value. Debit cost of sales, credit inventory.

**Foreign currency revaluation.** If the entity holds monetary assets or liabilities in a foreign currency, revalue to the year-end exchange rate per the country skill's rules. Post exchange gains or losses to the P&L.

**Tax provision.** Compute the current tax charge for the period:

- Apply the country skill's corporate tax rate to the taxable profit (which may differ from accounting profit due to disallowable expenses and capital allowances).
- If a tax skill is loaded, use its computation. If not, apply the country skill's headline rate to accounting profit as an approximation and flag for the reviewer.
- Post: debit tax expense (P&L), credit tax payable (current liability).
- If the country skill requires deferred tax: compute the deferred tax asset or liability arising from timing differences between accounting profit and taxable profit. Debit/credit deferred tax expense (P&L), credit/debit deferred tax liability/asset (balance sheet).

For every adjustment, record: the adjustment type, the accounts affected, the debit amount, the credit amount, and the rationale. Present the full list of adjustments to the user before proceeding:

> "I have identified the following year-end adjustments:
>
> [Numbered list with one line per adjustment: type, amount, accounts affected.]
>
> Are there any additional adjustments I should include, or any of these you want to remove or modify?"

Wait for confirmation.

### Step 5 — Prepare the income statement (P&L)

From the adjusted trial balance (trial balance + year-end adjustments), prepare the income statement in the format specified by the country skill:

- Extract all revenue accounts and group per the country skill's format.
- Extract all cost of sales accounts (if the format uses gross profit).
- Compute gross profit (revenue − cost of sales) if applicable.
- Extract all operating expense accounts and group per the country skill's categories.
- Compute operating profit (gross profit − operating expenses).
- Include other income and expenses (interest, foreign exchange gains/losses, exceptional items) per the country skill's format.
- Compute profit before tax.
- Deduct the tax charge (from Step 4).
- Compute profit after tax.

If the country skill specifies a single-step format (all revenue minus all expenses in one step), follow that instead of the multi-step format above.

Apply the country skill's terminology (e.g., "turnover" vs. "revenue," "profit and loss account" vs. "income statement," "operating charges" vs. "operating expenses").

Include comparative figures if required and available.

### Step 6 — Prepare the balance sheet

From the adjusted trial balance, prepare the balance sheet in the format specified by the country skill:

**Assets:**
- Non-current assets (fixed assets at cost less accumulated depreciation, intangible assets, investments).
- Current assets (inventory, trade debtors/receivables, prepayments, accrued income, bank and cash).

**Liabilities:**
- Current liabilities (trade creditors/payables, tax payable, social security payable, accrued expenses, deferred income, short-term portion of long-term debt).
- Non-current liabilities (long-term loans, deferred tax liability, provisions with settlement dates beyond 12 months).

**Equity:**
- Share capital or owner's equity.
- Retained earnings (brought forward + current year profit − dividends/drawings).
- Other reserves per the country skill's requirements.

Verify the accounting equation: Total assets = Total liabilities + Total equity. If it does not balance, stop and find the error. Do not proceed with an unbalanced balance sheet.

Apply the country skill's format (vertical vs. horizontal presentation, the order of liquidity, local terminology, whether to show net current assets as a subtotal).

Include comparative figures if required and available.

### Step 7 — Prepare notes to accounts

Prepare the notes in the order and format specified by the country skill. Universal note categories that most frameworks require:

1. **Accounting policies.** Basis of preparation, going concern confirmation, revenue recognition policy, depreciation policy, inventory valuation policy, foreign currency policy, and any other significant policies. Use the policies appropriate to the framework identified in Step 2.

2. **Turnover / revenue.** Breakdown by activity or geographical market if material.

3. **Operating profit.** Disclosure of items charged in arriving at operating profit: depreciation, amortization, auditor remuneration, operating lease charges, staff costs, directors' remuneration.

4. **Tax.** Reconciliation of the tax charge to the expected charge at the headline rate. Deferred tax movements.

5. **Fixed assets / property, plant, and equipment.** Movement schedule: opening cost, additions, disposals, closing cost. Opening accumulated depreciation, charge for the year, disposals, closing accumulated depreciation. Net book value at start and end.

6. **Intangible assets.** Same movement schedule as fixed assets.

7. **Debtors / receivables.** Breakdown by type (trade debtors, prepayments, other debtors). Amounts falling due after more than one year disclosed separately.

8. **Creditors / payables.** Breakdown by type (trade creditors, tax, social security, accruals, other creditors). Split between amounts due within one year and amounts due after more than one year.

9. **Provisions.** Movement schedule: opening balance, charged in the period, utilized, released, closing balance.

10. **Share capital / equity.** Number and class of shares, movements in the period.

11. **Related party transactions.** Disclosure of transactions with directors, shareholders, group companies, and other related parties.

12. **Post-balance-sheet events.** Disclosure of significant events between the balance sheet date and the date of approval.

13. **Commitments and contingencies.** Capital commitments, operating lease commitments, contingent liabilities.

The country skill specifies which notes are mandatory for the entity's size classification, the exact format, and any additional jurisdiction-specific notes. Micro-entity regimes often require minimal or no notes — follow the country skill's guidance.

### Step 8 — Filing and approval

Produce a filing checklist:

- **Director / owner approval.** The statements must be approved by the directors (or owner for sole traders) before filing. Note the approval requirement.
- **Filing with the registrar.** If the jurisdiction requires filing accounts with a company registrar, list the filing requirements (which version of accounts: full, abbreviated, abridged), the filing portal, and the deadline.
- **Filing with the tax authority.** If the accounts accompany the tax return, note the tax filing deadline and any format requirements.
- **Audit requirement.** If the entity exceeds audit thresholds or is otherwise required to be audited, note this. If the entity qualifies for audit exemption, note the exemption and its conditions.
- **Publication requirements.** If the accounts must be published or made publicly available, note where and when.

Produce all outputs specified in Section 3. Run the self-checks in Section 4. Only deliver when all checks pass.

---

## Section 2 — Adjustment types (detailed reference)

This section provides the universal mechanics for each adjustment type. The country skill provides the specific rates, policies, and thresholds; this section provides the computational framework.

### Accrued expenses and accrued income

**Recognition test:** Has an expense been incurred (or income earned) before the year-end for which no invoice has been received (or issued)? Estimate the amount from the contract, prior period patterns, or the user's estimate. Flag estimates for the reviewer. Accruals are typically reversed in the following period — note this but do not post the reversal.

### Prepayments and deferred income

**Recognition test:** Has a payment been made (or received) before the year-end that relates wholly or partly to post-year-end periods? Time-apportion the payment over the service period.

### Depreciation and amortization

**Methods** (the country skill specifies which to use):

- *Straight-line:* (Cost − Residual value) ÷ Useful life = Annual charge. Pro-rate for part-year ownership.
- *Reducing balance:* Net book value at start of period × Rate = Annual charge. Pro-rate for part-year ownership.
- *Units of production:* (Cost − Residual value) × (Units produced this period ÷ Total estimated units) = Period charge.

**First-year and disposal-year treatment:** The country skill specifies whether assets acquired or disposed of during the year receive a full year's depreciation, a half-year charge, or a pro-rated charge based on months of ownership.

### Provisions

**Recognition test (per IAS 37 / local GAAP equivalent):**
1. Present obligation (legal or constructive) arising from a past event.
2. Probable outflow of economic resources to settle.
3. Reliable estimate of the amount.

All three conditions must be met. If condition 3 fails but 1 and 2 are met, disclose as a contingent liability in the notes rather than recognizing a provision.

### Inventory adjustments

**Valuation rule:** Lower of cost and net realizable value (NRV). Cost per the entity's costing method (FIFO, weighted average — the country skill specifies which methods are permitted). NRV is estimated selling price less costs to complete and sell.

**Write-down:** If NRV < cost, write down to NRV. Debit cost of sales, credit inventory.

### Foreign currency revaluation

**Monetary items** (cash, receivables, payables in foreign currency): Revalue at the year-end spot rate. Exchange differences go to the P&L.

**Non-monetary items** (fixed assets, inventory purchased in foreign currency): Remain at the historical rate unless impaired. No revaluation at year-end.

### Tax provision — current and deferred

**Current tax:** Taxable profit × Tax rate = Current tax charge. Taxable profit starts from accounting profit and is adjusted for: disallowable expenses (entertaining, fines, depreciation replaced by capital allowances), non-taxable income (exempt dividends, capital gains taxed separately), and timing differences that create deferred tax.

**Deferred tax:** Arises from timing differences between when items are recognized in accounting profit vs. taxable profit. The most common source is the difference between accounting depreciation and tax capital allowances. Compute using the country skill's approach (full provision method or partial provision, balance sheet liability method or income statement method).

---

## Section 3 — Output specification

Six outputs per financial statements engagement. All six are mandatory. Never produce one without the others.

### Output 1 — Income statement (P&L)

Format per the country skill's specification. See Step 5 for the universal structure. Include comparative figures if required. Show all subtotals and groupings per the country skill's format.

### Output 2 — Balance sheet

Format per the country skill's specification. See Step 6 for the universal structure. Include comparative figures if required. Show the accounting equation verification at the bottom.

### Output 3 — Notes to accounts

Format and content per Step 7 and the country skill's requirements. Each note numbered sequentially. Cross-referenced to the line items on the income statement and balance sheet.

### Output 4 — Year-end adjustment schedule

Every adjustment posted in Step 4, in tabular format:

| # | Adjustment Type | Description | Debit Account | Credit Account | Amount | Rationale |
|---|---|---|---|---|---|---|
| 1 | [type] | [description] | [account] | [account] | [amount] | [why] |
| ... | | | | | | |

Total debits must equal total credits across all adjustments.

### Output 5 — Filing checklist

Per Step 8. Includes director approval, registrar filing, tax authority filing, audit status, and publication requirements. Each item with a deadline and status (pending/complete).

### Output 6 — Reviewer brief

```markdown
# [Country] Financial Statements — Reviewer Brief
**Entity:** [name and type]
**Period:** [year-end date]
**Framework:** [applicable reporting framework]
**Size classification:** [micro/small/medium/large]
**Generated:** [date]

## Summary
- Revenue: [amount] [currency] ([change from prior year])
- Net profit / (loss): [amount] ([change from prior year])
- Total assets: [amount]
- Net assets: [amount]
- Year-end adjustments posted: [count]
- Total value of adjustments: [amount]

## High-priority items (review first)
[Numbered list: items with largest financial impact, unusual
adjustments, material estimates, going concern indicators. Each:
one sentence what, one sentence why it matters, one sentence
what the reviewer should do.]

## Year-end adjustments summary
[For each adjustment: one line with the type, amount, and whether
the amount is exact or estimated. Flag any adjustment that exceeds
materiality thresholds.]

## Assumptions made
[For each assumption: the assumption, what it affects, what changes
if the assumption is wrong, and the financial impact.]

## Accounting policies applied
[Summary of significant policies: depreciation method and rates,
inventory valuation method, revenue recognition, bad debt
provisioning approach.]

## Items the reviewer should verify
[Specific items: bank confirmation letters to obtain, debtor
circularizations, fixed asset physical verification, inventory
count reconciliation, post-year-end invoice checks for accruals.
Not generic "verify everything."]

## Filing deadlines
- Accounts filing with [registrar]: [deadline]
- Tax return filing: [deadline]
- Audit requirement: [yes/no — reason]
```

---

## Section 4 — Self-checks (run before delivering output)

Run these fourteen checks against all outputs. If any fails, fix and re-run. Do not deliver until all pass.

### Arithmetic integrity

**Check 1 — Trial balance balances after adjustments.** The adjusted trial balance (original TB + all year-end adjustments) has total debits exactly equal to total credits.

**Check 2 — Adjustment schedule balances.** Total debits across all year-end adjustments equal total credits. Every adjustment is a valid double entry.

**Check 3 — Income statement foots.** Revenue minus cost of sales equals gross profit (if multi-step). Gross profit minus operating expenses equals operating profit. All subtotals are arithmetically correct. The tax charge deducted matches the tax provision posted in Step 4.

**Check 4 — Balance sheet balances.** Total assets equal total liabilities plus total equity. Not approximately — exactly. A difference of even 0.01 means a posting error.

**Check 5 — Retained earnings reconciles.** Retained earnings on the balance sheet equals: opening retained earnings + net profit for the year − dividends declared. If it does not, the P&L and balance sheet are inconsistent.

### Cross-document consistency

**Check 6 — P&L matches adjusted trial balance.** Every revenue and expense balance on the income statement matches the corresponding account balance on the adjusted trial balance.

**Check 7 — Balance sheet matches adjusted trial balance.** Every asset, liability, and equity balance on the balance sheet matches the corresponding account balance on the adjusted trial balance.

**Check 8 — Notes cross-reference correctly.** Every note referenced from the income statement or balance sheet exists in the notes to accounts. Every note in the notes to accounts is referenced from the face of a statement (or is a disclosure note required by the framework regardless of reference).

**Check 9 — Comparative figures are consistent.** If comparative figures are presented: the prior year figures on the current year's income statement and balance sheet match the published figures from the prior year. If the user provided prior year accounts, verify. If not, flag as unverified in the reviewer brief.

**Check 10 — Depreciation in notes matches P&L.** The total depreciation charge disclosed in the fixed assets note equals the depreciation expense on the income statement.

### Completeness

**Check 11 — All mandatory notes present.** The country skill specifies the mandatory notes for the entity's size classification. Every mandatory note is present. No mandatory note is omitted.

**Check 12 — All accounts classified.** Every account on the adjusted trial balance appears on either the income statement or the balance sheet. No account is orphaned (present on the TB but absent from the statements).

**Check 13 — Filing checklist complete.** Every filing obligation from the country skill is listed in the filing checklist with a deadline. No obligation is silently omitted.

**Check 14 — Reviewer brief disclosure complete.** Every year-end adjustment, every assumption, and every estimate is disclosed in the reviewer brief. Count adjustments in the schedule; count entries in the brief; they must match.

### Failure handling

If any check fails, fix the output and re-run all fourteen. Do not deliver until all pass. If a check fails twice in a row on the same item, stop and report the failure to the user.

---

## Section 5 — Country skill contract

Every country-specific financial statements skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Reporting framework specification** — which GAAP/standard applies per entity size (full local GAAP, small entity framework, micro-entity regime, IFRS) and the size thresholds (revenue, balance sheet total, employee count).
2. **Income statement format** — single-step or multi-step, category groupings, subtotal points, terminology, exceptional item presentation.
3. **Balance sheet format** — vertical or horizontal, order of liquidity, current/non-current split, net current assets subtotal, local terminology.
4. **Chart of accounts mapping** — how trial balance codes map to income statement and balance sheet line items and groupings.
5. **Notes requirements by size** — for each classification (micro, small, medium, large): mandatory notes, content/format, and exemptions.
6. **Depreciation schedule** — permitted methods under local GAAP, typical useful lives and rates, first-year and disposal-year treatment.
7. **Tax provision rules** — corporate tax rate, computation method (adjustments for disallowable items, capital allowances), deferred tax requirements and method.
8. **Filing requirements** — where to file (registrar, tax authority, both), deadline rules, form of accounts required, penalties for late filing.
9. **Audit thresholds** — criteria for mandatory audit and available exemptions.
10. **Directors' report requirements** — whether required, contents, size exemptions.
11. **Going concern disclosure requirements** — local GAAP requirements including the look-forward period.
12. **Currency and number format** — base currency, ISO code, separators, rounding rules for presentation.

### Optional slots

13. **Industry-specific formats** — modified formats for specific industries (financial institutions, insurance companies, charities) that differ from the standard commercial format.

14. **Consolidation requirements** — if the entity is part of a group, whether consolidated accounts are required and the thresholds for exemption.

15. **Integration notes** — how the financial statements skill interacts with the country's bookkeeping skill, tax skill, or audit skill if loaded simultaneously.

---

## Section 6 — Reference material

### Validation status

This file is v1.0 of `financial-statements-workflow-base`, drafted as part of the Open Accountants skill architecture in May 2026. It follows the structural pattern established by `bookkeeping-workflow-base` v1.0.

### Design decisions

1. **Trial balance as input, not raw transactions.** The bookkeeping-workflow-base handles transaction-to-TB. This separation keeps each workflow focused.

2. **Year-end adjustments as an interactive step.** Adjustments are presented for confirmation because many involve estimates only the user can confirm.

3. **Framework determination before any work.** The framework determines format, notes, disclosures, and filing requirements. Getting it wrong wastes all subsequent work.

4. **Fourteen self-checks matching the bookkeeping standard.** Deliberately aligned to establish a consistent quality bar across the skill set.

### Known gaps

1. Consolidated financial statements are not specified. A future `consolidation-workflow-base` may extend this.
2. Cash flow statements are not included. A future version will add this for entities that require it.
3. Statement of changes in equity is covered in the balance sheet and notes, not as a separate output.
4. Management accounts and interim reporting are not in scope — statutory year-end accounts only.
5. IFRS-specific requirements (IFRS 16, IFRS 9, etc.) are delegated to the country skill's framework specification.

### Change log

- **v1.0 (May 2026):** Initial release. Establishes the universal financial statements workflow, adjustment type reference, six-output specification, 14 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
