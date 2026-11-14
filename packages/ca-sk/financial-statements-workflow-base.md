---
name: financial-statements-workflow-base
description: "Shared 2026 financial-statement preparation method: confirm the actual framework and period, review trial balance/source support, propose adjustments, prepare every required statement and note, reconcile comparatives/equity/cash, and hand off approval/filing tasks. Includes bounded IFRS and 2026-applicable Australian standard examples, not worldwide GAAP, tax rates, audit exemptions or filing dates."
version: 1.1
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-11-14
tax_year: 2026
type: cross-country-method
tier: 2
domain: financial-statements
---

# Financial Statements Workflow Base Skill v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a financial statements preparation task: the order of operations, how to review a trial balance, how to post year-end adjustments, how to format an income statement and balance sheet, how to draft notes to accounts, what to check before delivering. It supplies no worldwide local GAAP, reporting/audit thresholds, filing portal or depreciation rate. Bounded standard-based recognition/presentation examples below illustrate the method without establishing the entity's actual legal reporting framework.

**This file must always be loaded with a country-specific financial statements skill** that provides the reporting framework, P&L and balance sheet formats, notes requirements, and filing rules (e.g., `uk-financial-statements`, `au-financial-statements`, `de-financial-statements`). Without actual applicable country/entity/framework rules, Claude must not call an accounts pack complete or compliant. Evidence inventory, TB diagnostics and clearly provisional schedules can continue while the exact missing rules are identified; a missing catalogue companion does not justify invented policies or a refusal of all useful preparation.

**This file is the contract.** When a country financial statements skill says it conforms to v1.1 of this base, it means: it fills the country slots specified in Section 5, it produces outputs in the format specified in Section 3, its outputs can be validated by the self-checks in Section 4, and it participates in the workflow in Section 1.

---

## Ask the client first

Read the full existing client record, prior issued accounts, chart, TB and supporting schedules before asking again. Confirm legal entity/group and jurisdictions; reporting framework/version and period/early adoption; opening balances/comparatives; functional/presentation currency; going-concern and post-period facts/authorisation date; and requested approval/filing deliverables. Identify tax framework/elections separately from financial reporting. Unknown facts remain explicit and cannot be made true by a confirmation prompt.

## The method, step by step

You are helping a business owner or their accountant prepare a set of financial statements from a completed trial balance. The output will be reviewed by a qualified accountant before filing. Your job is to do the mechanical preparation work : reviewing the trial balance for completeness, posting year-end adjustments, formatting the statements per the applicable framework, and producing a reviewer brief that makes the professional's job fast and accurate.

Execute these eight steps in order. Do not skip. Do not reorder. Do not begin drafting statements before step 5. Draft adjustment schedules during Step 4 and statements during Steps 5 to 7, then finalise the required set at Step 8. Prepare numbered proposed journals/import files; do not change a ledger or file accounts merely because access is available.

### Step 1 : Confirm the companion skills are loaded

This workflow base requires a country-specific financial statements skill providing the reporting framework, statement formats, notes requirements, and filing rules.

If the companion is missing, search the current available catalogue using known jurisdiction/entity facts. Ask only for missing facts. Continue safe TB/evidence review but hold any framework-dependent final recognition/disclosure/filing claim. Carry the actual source skill/version/date/approval label into the handoff; professional approval does not spread to all other source methods.

If a bookkeeping workflow skill is also loaded, note its presence : the trial balance from the bookkeeping skill is the input to this workflow. If a tax skill is loaded, note its presence : the tax provision computation in Step 4 can reference the tax skill's rates and rules.

### Step 2 : Determine the reporting framework

From the country skill and the client's details, establish:

- **Entity type/group/activity.** Establish legal form, group membership, listing/regulated/public-interest status and actual local law; legal form alone does not determine all reporting or audit exemptions.
- **Entity size classification.** Apply actual current thresholds, effective year, measurement/group basis, prior-period/two-year tests and ineligible-entity overrides. Do not infer micro/small status or audit exemption from one revenue/employee number.
- **Applicable reporting framework.** Full local GAAP, simplified small-entity framework, micro-entity regime, or IFRS per the country skill. If the entity has a choice, present options and implications.
- **Reporting period.** Confirm financial year dates. Flag first accounting periods or changes of accounting date.
- **Comparative period.** Establish actual framework requirements, availability, restatements/reclassifications and any opening statement requirement. Entity size alone is not permission to omit comparatives.
- **Going concern.** Obtain management's actual assessment, forecasts/funding and relevant subsequent facts over the framework's required horizon. Assess basis and material uncertainties; a user's yes/no assurance is not evidence of ability to continue.

Present the framework determination to the user:

> "Based on the entity details, here is the reporting framework I will apply:
>
> [Entity type, size classification, applicable framework, reporting period, comparative requirement, going concern assumption.]
>
> Is this correct? If anything needs adjusting, tell me before I begin reviewing the trial balance."

Wait for confirmation.

### Step 3 : Trial balance review

The user will provide a trial balance : either from the bookkeeping workflow output or as a separate document. Review it for completeness:

- **Balance check.** Total debits must equal total credits. If they do not, stop and tell the user the trial balance does not balance. Do not proceed with an unbalanced trial balance.
- **Account completeness.** Check that the trial balance contains accounts for all the categories expected by the country skill's chart of accounts: revenue, cost of sales (if applicable), operating expenses, fixed assets, current assets, current liabilities, long-term liabilities, equity. Flag any missing category.
- **Suspense accounts.** Identify each unsupported counterpart, origin and evidence needed. Do not clear it by inventing income/expense or a balancing plug. Keep the exception draft; a material unresolved item prevents a compliant final pack.
- **Period consistency.** Verify that the trial balance period matches the reporting period established in Step 2. If the trial balance covers a different period, stop and clarify with the user.
- **Nominal code validity.** Every account code in the trial balance should exist in the country skill's chart of accounts. Flag any unrecognized codes.
- **Brought-forward balances.** If comparative figures are available, verify that the opening balances on the current trial balance match the closing balances from the prior period. Flag any discrepancies.
- **Obvious anomalies.** Credit balances on normally-debit accounts (e.g., a credit balance on a fixed asset account could indicate over-depreciation or disposal). Debit balances on normally-credit accounts (e.g., a debit balance on a creditor could indicate an overpayment). Unusually large or small balances relative to comparatives. Accounts with no movement in the period that previously had activity.

Produce a trial balance review summary listing any issues found. If no issues: "Trial balance reviewed : no issues found. Proceeding to year-end adjustments."

### Step 4 : Year-end adjustments

Review the trial balance and the user's supporting information for year-end adjustments that need to be posted. For each adjustment type, determine whether an adjustment is needed and compute the amount:

**Accrued expenses.** Establish an actual recognised obligation/consumed service before period end, its estimate, account and maturity; an invoice received later is evidence, not automatically a future expense. Utilities, professional work, interest and employee bonuses need their actual contracts/recognition rules. Use the supported expense/asset and payable/accrual accounts; do not accrue a planned future cost or assume every accrual is current.

**Accrued income.** Establish actual earned performance and receivable/contract-asset criteria, not merely the intention to invoice. Under IFRS contracts apply the satisfied-performance analysis and actual presentation; current classification is not automatic. [IFRS 15 overview](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/).

**Prepayments.** Expenses paid before the year-end that relate to periods after the year-end. Common examples: insurance premiums, rent paid in advance, subscription fees. For each: debit prepayments (current asset), credit the expense account. Compute the portion relating to the post-year-end period.

**Deferred income.** Identify a receipt/invoice that is not yet earned under the actual framework and its contract liability/presentation. If revenue was already credited incorrectly, propose its reversal to the appropriate liability; do not debit revenue twice when the receipt was correctly deferred from the start. [IFRS 15](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/).

**Depreciation.** Establish depreciable asset/components, cost/revaluation, residual value, useful life, available-for-use and cessation dates and consumption-based method. Do not substitute tax capital-allowance rates or months of ownership. Depending on actual use, the debit can be expense or another asset's cost. [AASB 116 paras 43 to 62A, 2026-applicable compilation](https://standards.aasb.gov.au/aasb-116-dec-2022).

**Amortisation.** Establish actual intangible recognition and finite/indefinite life. Under IAS 38 an indefinite-life intangible is not amortised but needs annual impairment testing; finite-life assets use their applicable life/method and impairment rules. Goodwill has a separate framework. [IAS 38 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/).

**Provisions.** Review for items that require a provision:

- *Doubtful debts.* Reconcile receivable exposure, actual credit/collection evidence and the applicable financial-instrument impairment model. Under IFRS, expected credit losses are a financial-instrument task, not a generic IAS 37 provision or invented aged-debtor percentage. [IFRS 9 overview/history](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/).
- *Warranty provisions.* Establish the actual warranty/contract type and present obligation, probability and measurement; historical claims are evidence, not automatic proof that every warranty is an IAS 37 provision. Use the actual warranty/revenue method. [IAS 37](https://www.ifrs.org/issued-standards/list-of-standards/ias-37-provisions-contingent-liabilities-and-contingent-assets/).
- *Legal provisions.* Obtain legal evidence and apply the actual present-obligation, probable-outflow and reliable-measurement conditions; distinguish recognised provision, disclosed contingency and remote case. Do not equate being sued with an automatically recognised loss. [IAS 37](https://www.ifrs.org/issued-standards/list-of-standards/ias-37-provisions-contingent-liabilities-and-contingent-assets/).
- *Restoration/dilapidation.* Establish when the present obligation arises, measurement/discounting and related asset/expense treatment. Do not spread every obligation evenly over a lease term; asset recognition may include restoration cost. [IAS 37](https://www.ifrs.org/issued-standards/list-of-standards/ias-37-provisions-contingent-liabilities-and-contingent-assets/), [IAS 16 cost overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/).

**Inventory adjustments.** If the entity holds inventory: verify the closing inventory value per the count or valuation. Post any write-down from cost to net realizable value. Debit cost of sales, credit inventory.

**Foreign currency.** Confirm functional/presentation currencies, monetary versus non-monetary measurement and actual exchangeability/rate. Apply the correct transaction, closing or fair-value-date rate and P&L/OCI treatment, including applicable foreign-operation/hedge exceptions; not every exchange effect belongs in P&L. [AASB 121 paras 20 to 34](https://standards.aasb.gov.au/aasb-121-oct-2023).

**Tax provision.** Compute the current tax charge for the period:

- Apply the country skill's corporate tax rate to the taxable profit (which may differ from accounting profit due to disallowable expenses and capital allowances).
- Obtain a complete actual current-tax computation, losses/credits and applicable enacted/substantively enacted rules. A missing tax method is an unresolved provision, not permission to post headline rate times accounting profit. Separate the tax charge from instalments/withholding/payment settlements and prior-period amounts. [IAS 12 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/).
- Determine actual tax recognition/allocation and settlement accounts from the relevant framework and tax working paper. Do not automatically put every tax movement in P&L or treat prepaid current tax as a new expense; establish the actual payable/receivable and presentation.
- If applicable, compute deferred tax from the actual temporary difference between carrying amount and tax base, losses/credits, recognition/recoverability conditions and exceptions. Timing differences alone are not the whole balance-sheet model. Obtain the actual P&L/OCI/equity allocation and relevant Pillar Two exception; no deferred-tax figure is invented here. [IAS 12 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/).

For every adjustment, record: the adjustment type, the accounts affected, the debit amount, the credit amount, and the rationale. Present the full list of adjustments to the user before proceeding:

> "I have identified the following year-end adjustments:
>
> [Numbered list with one line per adjustment: type, amount, accounts affected.]
>
> Are there any additional adjustments I should include, or any of these you want to remove or modify?"

Wait for factual confirmation and authorised journal approval. A request to remove a mandatory recognised liability or disclosure does not override the applicable framework; document the disagreement and hold finalisation where necessary.

### Step 5 : Prepare the income statement (P&L)

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

Include required comparative figures and any supported restatement/reclassification bridge. Missing required comparatives remain an explicit finalisation gap, not an optional omission.

### Step 6 : Prepare the balance sheet

From the adjusted trial balance, prepare the balance sheet in the format specified by the country skill:

**Assets:**
- Non-current assets (fixed assets at cost less accumulated depreciation, intangible assets, investments).
- Current assets (inventory, trade debtors/receivables, prepayments, accrued income, bank and cash).

**Liabilities:**
- Current liabilities (trade creditors/payables, tax payable, social security payable, accrued expenses, deferred income, short-term portion of long-term debt).
- Non-current liabilities as actually classified under the applicable framework, including relevant loans, deferred tax and provisions; maturity beyond a simple month count is not the only test.

**Equity:**
- Share capital or owner's equity.
- Retained earnings/owner equity with a full roll-forward: actual profit allocation, distributions/drawings under the correct legal form, restatements/transfers and other direct equity movements; do not mix company dividends with proprietor drawings.
- Other reserves per the country skill's requirements.

Verify the accounting equation: Total assets = Total liabilities + Total equity. If it does not balance, stop and find the error. Do not proceed with an unbalanced balance sheet.

Apply the country skill's format (vertical vs. horizontal presentation, the order of liquidity, local terminology, whether to show net current assets as a subtotal).

Include required comparative figures and any supported restatement/reclassification bridge. Missing required comparatives remain an explicit finalisation gap, not an optional omission.

### Step 7 : Prepare notes to accounts

Prepare the notes in the order and format specified by the country skill. Universal note categories that most frameworks require:

1. **Accounting policies.** Actual basis of preparation, going-concern assessment/material uncertainty, revenue recognition policy, depreciation policy, inventory valuation policy, foreign currency policy, and any other significant policies. Use the policies appropriate to the framework identified in Step 2.

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

12. **Post-period events.** Identify events through authorisation for issue, distinguish evidence of conditions already existing at period end from later conditions, adjust the former and assess material disclosure for the latter under the actual framework. [IAS 10 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-10-events-after-the-reporting-period/).

13. **Commitments and contingencies.** Capital commitments, operating lease commitments, contingent liabilities.

The country skill specifies which notes are mandatory for the entity's size classification, the exact format, and any additional jurisdiction-specific notes. Do not assume micro status means no notes; establish the actual statutory minimum disclosures and any ineligible-entity/group exceptions.

### Step 8 : Filing and approval

Produce a filing checklist:

- **Director / owner approval.** The statements must be approved by the directors (or owner for sole traders) before filing. Note the approval requirement.
- **Filing with the registrar.** If the jurisdiction requires filing accounts with a company registrar, list the filing requirements (which version of accounts: full, abbreviated, abridged), the filing portal, and the deadline.
- **Filing with the tax authority.** If the accounts accompany the tax return, note the tax filing deadline and any format requirements.
- **Audit requirement.** If the entity exceeds audit thresholds or is otherwise required to be audited, note this. If the entity qualifies for audit exemption, note the exemption and its conditions.
- **Publication requirements.** If the accounts must be published or made publicly available, note where and when.

Produce all outputs specified in Section 3. Run the self-checks in Section 4. Only label the set final-ready when all applicable checks pass; deliver an exception draft only with unresolved/failed items clearly visible, without filing or claiming compliance.

---

## Section 2 : Adjustment types (detailed reference)

This section provides shared adjustment questions and explicitly bounded standard applications, not universally mandatory accounting rules. The country skill provides the specific rates, policies, and thresholds; this section provides the computational framework.

### Accrued expenses and accrued income

**Recognition test:** Has an expense been incurred (or income earned) before the year-end for which no invoice has been received (or issued)? Estimate the amount from the contract, prior period patterns, or the user's estimate. Flag estimates for the reviewer. Accruals are typically reversed in the following period : note this but do not post the reversal.

### Prepayments and deferred income

**Recognition test:** establish the actual right/obligation and service/performance period before adjusting. Time apportionment is appropriate only when it represents the actual supplied/consumed pattern; a cash receipt or invoice alone does not make all revenue earned. Retain the original posting and proposed adjustment to avoid duplicate deferral. [IFRS 15](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/).

### Depreciation and amortization

**Methods** (the country skill specifies which to use):

- *Straight-line:* (Cost − Residual value) ÷ Useful life = Annual charge. Apply the actual depreciation period and method, not ownership alone.
- *Reducing balance:* apply the supported rate to the appropriate carrying amount for each actual availability period, including additions/disposals. Respect residual value, actual method and period; opening carrying amount alone cannot depreciate an asset first acquired during the year. The rate is an entity estimate/policy, not automatically a tax rate.
- *Units of production:* (Cost − Residual value) × (Units produced this period ÷ Total estimated units) = Period charge, within the actual depreciable amount and supported production estimate. Missing/zero estimated total units is unresolved, not a valid divisor.

**First/disposal year:** under the cited AASB 116 compilation, start when available for use and cease at the applicable held-for-sale/derecognition point. Determine actual dates/policy and significant components; tax half/full-year conventions are a separate tax matter. Residual value, life and method need review, not a universal country rate. [AASB 116 paras 48 to 62A](https://standards.aasb.gov.au/aasb-116-dec-2022).

### Provisions

**Recognition test (per IAS 37 / local GAAP equivalent):**
1. Present obligation (legal or constructive) arising from a past event.
2. Probable outflow of economic resources to settle.
3. Reliable estimate of the amount.

Within the applicable IAS 37 model, establish all recognition conditions and actual disclosure requirements. An unrecognised obligation/possible obligation may need contingency disclosure unless outflow is remote; future operating losses do not create a provision merely because forecast. Measurement includes actual risk/discounting conditions, not a flat smoothing amount. [IAS 37 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-37-provisions-contingent-liabilities-and-contingent-assets/).

### Inventory adjustments

**Valuation rule, IAS 2 application:** compare supported cost with NRV, meaning estimated selling price less completion and necessary selling costs. Determine actual inventory scope, permitted cost method, quantities/condition and allocation. The lower-of-cost/NRV rule is not an unqualified worldwide local-GAAP claim. [IAS 2 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/).

**Write-down:** If NRV < cost, write down to NRV. Debit cost of sales, credit inventory.

### Foreign currency revaluation

**Monetary items:** under the cited AASB 121 model, translate using the closing rate. Ordinary settlement/translation differences are in P&L subject to the actual foreign-operation/net-investment and hedge rules. Establish exchangeability and actual rate rather than an arbitrary provider quote. [AASB 121 paras 23, 27 to 34](https://standards.aasb.gov.au/aasb-121-oct-2023).

**Non-monetary items:** historical-cost items use the transaction-date rate; fair-value items use the rate at the actual valuation date. Test impairment/NRV using the relevant measurement-date amounts/rates. An exchange component follows the relevant underlying P&L/OCI treatment, not an automatic all-P&L rule. [AASB 121 paras 23 to 31](https://standards.aasb.gov.au/aasb-121-oct-2023).

### Tax provision : current and deferred

**Current tax:** reconcile accounting profit to actual taxable income, disallowances/deductions, exempt/separately taxed income, capital allowances, losses, surcharges and credit relief under the applicable country rules. Do not infer that every example expense is disallowed or every dividend exempt worldwide. Compute actual current tax and its payable/receivable separately from deferred tax and payments. [IAS 12 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/).

**Deferred tax:** under IAS 12 use actual carrying-amount/tax-base temporary differences and unused losses/credits with recognition conditions and exceptions. Depreciation versus capital allowances is one possible source, not the definition or the whole computation. Another local framework can have different rules; establish it rather than choosing a convenient full/partial method. [IAS 12 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/).

---

## Section 3 : Output specification

Retain all six workpaper groups below for a full financial-statements engagement, adding the actual framework's required statement components within the statement group. Never call a P&L and balance sheet with notes alone a complete IFRS set. A narrower diagnostic request may return the requested working paper without claiming full accounts.

### Output 1 : Income statement (P&L)

Format per the country skill's specification. See Step 5 for the universal structure. Include comparative figures if required. Show all subtotals and groupings per the country skill's format.

### Output 2 : Balance sheet

Format per the country skill's specification. See Step 6 for the universal structure. Include comparative figures if required. Show the accounting equation verification at the bottom.

### Required complete-set components within Outputs 1 and 2

When IAS 1 applies, include profit/loss **and OCI**, statement of financial position, changes in equity, cash flows, notes and required comparatives. Assess the required opening comparative statement for retrospective restatement/reclassification. Do not assert IFRS compliance with missing components. Determine actual local exemptions rather than applying this list to every country/entity. [IAS 1 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/).

For a 2026 reporting period, identify whether IAS 1 remains applicable or IFRS 18 is validly early adopted. IFRS 18 is ordinarily effective for annual periods beginning on or after **1 January 2027**, with early application permitted. Do not impose its new presentation subtotals on every 2026 entity simply because the current website describes them. Record adoption/transition and linked standard versions. [IFRS 18 effective date](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/).

### Output 3 : Notes to accounts

Format and content per Step 7 and the country skill's requirements. Each note numbered sequentially. Cross-referenced to the line items on the income statement and balance sheet.

### Output 4 : Year-end adjustment schedule

Every adjustment posted in Step 4, in tabular format:

| # | Adjustment Type | Description | Debit Account | Credit Account | Proposed debit/credit and evidence | Rationale |
|---|---|---|---|---|---|---|
| 1 | [type] | [description] | [account] | [account] | [amount] | [why] |
| ... | | | | | | |

Total debits must equal total credits across all adjustments.

### Output 5 : Filing checklist

Per Step 8. Includes director approval, registrar filing, tax authority filing, audit status, and publication requirements. Each item with a deadline and status (pending/complete).

### Output 6 : Reviewer brief

```markdown
# [Country] Financial Statements : Reviewer Brief
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
- Audit requirement: [yes/no : reason]
```

---

## Section 4 : Self-checks (run before delivering output)

Run all fourteen applicable checks. Fix failures before describing the set as final-ready; retain exact gaps in an exception draft without claiming compliance.

### Arithmetic integrity

**Check 1 : Trial balance balances after adjustments.** The adjusted trial balance (original TB + all year-end adjustments) has total debits exactly equal to total credits.

**Check 2 : Adjustment schedule balances.** Total debits across all year-end adjustments equal total credits. Every adjustment is a valid double entry.

**Check 3 : Income statement foots.** Revenue minus cost of sales equals gross profit (if multi-step). Gross profit minus operating expenses equals operating profit. All subtotals are arithmetically correct. The tax charge deducted matches the tax provision posted in Step 4.

**Check 4 : Balance sheet balances.** Total assets equal total liabilities plus total equity. Not approximately : exactly. A full-precision ledger difference is an unresolved error; reconcile any permitted presentation rounding explicitly rather than confusing display rounding with an unexplained posting plug.

**Check 5: Equity reconciles.** Reconcile opening equity/retained earnings, profit/OCI allocations, contributions, distributions, restatements and supported transfers to closing balances. Identify each movement and legal form; not every equity change goes through P&L or retained earnings.

### Cross-document consistency

**Check 6 : P&L matches adjusted trial balance.** Every revenue and expense balance on the income statement matches the corresponding account balance on the adjusted trial balance.

**Check 7 : Balance sheet matches adjusted trial balance.** Every asset, liability, and equity balance on the balance sheet matches the corresponding account balance on the adjusted trial balance.

**Check 8 : Notes cross-reference correctly.** Every note referenced from the income statement or balance sheet exists in the notes to accounts. Every note in the notes to accounts is referenced from the face of a statement (or is a disclosure note required by the framework regardless of reference).

**Check 9: Comparatives reconcile.** Tie to prior issued accounts, showing any required policy/error restatement or reclassification with its authority, bridge and disclosure. A correct restatement must not be forced back to the old published error. Distinguish prospective estimate changes from retrospective corrections. [IAS 8 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-8-basis-of-preparation-of-financial-statements/).

**Check 10: Depreciation allocation reconciles.** Tie the fixed-asset movement to the period charge and its actual allocation between P&L and amounts included in other assets, disposals/transfers and opening/closing accumulated balances. Not every period charge is immediately P&L expense. [AASB 116 paras 48 to 49](https://standards.aasb.gov.au/aasb-116-dec-2022).

### Completeness

**Check 11 : All mandatory notes present.** The country skill specifies the mandatory notes for the entity's size classification. Every mandatory note is present. No mandatory note is omitted.

**Check 12: Every balance/component accounted for.** Map every adjusted TB balance, including direct equity and OCI movements, to the applicable complete statement set/notes and supporting roll-forwards. Reconcile cash flows and equity to the balance sheet and required comparative/opening statements; do not omit components because the old output list contained only P&L and balance sheet.

**Check 13 : Filing checklist complete.** Every filing obligation from the country skill is listed in the filing checklist with a deadline. No obligation is silently omitted.

**Check 14 : Reviewer brief disclosure complete.** Every year-end adjustment, every assumption, and every estimate is disclosed in the reviewer brief. Count adjustments in the schedule; count entries in the brief; they must match.

### Failure handling

Fix and re-run all fourteen after a failure. If the same item fails twice, stop finalisation and report the exact failure, attempted fixes and missing evidence. Preserve an exception draft without filing or misrepresenting it as a complete compliant set.

---

## Section 5 : Country skill contract

Every country-specific financial statements skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Reporting framework specification** : which GAAP/standard applies per entity size (full local GAAP, small entity framework, micro-entity regime, IFRS) and the size thresholds (revenue, balance sheet total, employee count).
2. **Income statement format** : single-step or multi-step, category groupings, subtotal points, terminology, exceptional item presentation.
3. **Balance sheet format** : vertical or horizontal, order of liquidity, current/non-current split, net current assets subtotal, local terminology.
4. **Chart of accounts mapping** : how trial balance codes map to income statement and balance sheet line items and groupings.
5. **Notes requirements by size** : for each classification (micro, small, medium, large): mandatory notes, content/format, and exemptions.
6. **Depreciation schedule** : permitted methods under local GAAP, typical useful lives and rates, first-year and disposal-year treatment.
7. **Tax provision rules** : corporate tax rate, computation method (adjustments for disallowable items, capital allowances), deferred tax requirements and method.
8. **Filing requirements** : where to file (registrar, tax authority, both), deadline rules, form of accounts required, penalties for late filing.
9. **Audit thresholds** : criteria for mandatory audit and available exemptions.
10. **Directors' report requirements** : whether required, contents, size exemptions.
11. **Going concern disclosure requirements** : local GAAP requirements including the look-forward period.
12. **Currency and number format** : base currency, ISO code, separators, rounding rules for presentation.

### Optional slots

13. **Industry-specific formats** : modified formats for specific industries (financial institutions, insurance companies, charities) that differ from the standard commercial format.

14. **Consolidation requirements** : if the entity is part of a group, whether consolidated accounts are required and the thresholds for exemption.

15. **Integration notes** : how the financial statements skill interacts with the country's bookkeeping skill, tax skill, or audit skill if loaded simultaneously.

---

## Section 6 : Reference material

### Validation status

This file is v1.1 of `financial-statements-workflow-base`, updated in November 2026 from the original draft as part of the Open Accountants skill architecture in May 2026. It follows the structural pattern established by `bookkeeping-workflow-base` v1.0.

### Design decisions

1. **Trial balance as input, not raw transactions.** The bookkeeping-workflow-base handles transaction-to-TB. This separation keeps each workflow focused.

2. **Year-end adjustments as an interactive step.** Adjustments are presented for confirmation because many involve estimates only the user can confirm.

3. **Framework determination before any work.** The framework determines format, notes, disclosures, and filing requirements. Getting it wrong wastes all subsequent work.

4. **Fourteen self-checks matching the bookkeeping standard.** Deliberately aligned to establish a consistent quality bar across the skill set.

### Known gaps

1. Consolidated financial statements are not specified. A future `consolidation-workflow-base` may extend this.
2. Required cash flow statements must be included now in a claimed complete set; actual classification/IAS 7 or local-framework detail requires its applicable method, not silent omission.
3. Include a separate statement of changes in equity where required; a balance-sheet note does not automatically replace it.
4. Management accounts and interim reporting are not in scope : statutory year-end accounts only.
5. IFRS-specific requirements (IFRS 16, IFRS 9, etc.) are delegated to the country skill's framework specification.

### Change log

- **v1.0 (May 2026):** Initial release. Establishes the universal financial statements workflow, adjustment type reference, six-output specification, 14 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## When to refuse or refer

Hold final compliance/filing claims where the actual framework/adoption, material opening balance/recognition, mandatory statement/disclosure, tax provision or authorisation is unresolved. Keep the TB diagnostic, proposed journals and precise exception schedule usable. Consolidation, leases, credit loss, complex revenue, valuation, going concern and special/regulatory regimes require the relevant actual framework method; a short overview is not a full implementation. A user confirmation does not authorise a false statement of compliance or removal of a required liability/disclosure.

## Worked cases

**Depreciation starts at availability, not acquisition.** Assume the 2026-applicable AASB 116 model, cost 12,000, residual 2,000, confirmed five-year straight-line life, acquisition in January but first available for use in October, and three full months under the entity's supported monthly allocation policy. Annual charge is 2,000, current charge 500 and closing carrying amount 11,500 before any impairment/revaluation. A full ownership-year charge would overstate depreciation by 1,500. All cost/life/dates are assumed facts, not a country's tax allowance or statutory depreciation table. [AASB 116 paras 50 to 62A](https://standards.aasb.gov.au/aasb-116-dec-2022).

```oa-check
name: Depreciation availability boundary with a confirmed monthly policy
inputs:
  asset_cost: 12000
  residual: 2000
  life_years: 5
  months_available_this_period: 3
steps:
  - annual_charge: (asset_cost - residual) / life_years
  - current_charge: annual_charge * months_available_this_period / 12
  - carrying_amount: asset_cost - current_charge
  - overstatement_from_full_ownership_year: annual_charge - current_charge
expected:
  annual_charge: 2000
  current_charge: 500
  carrying_amount: 11500
  overstatement_from_full_ownership_year: 1500
```

**Inventory NRV includes completion and selling cost.** Assume IAS 2 applies, 100 identical units at cost 10 each, supported expected selling price 9 each, completion cost 0.5 and necessary selling cost 0.5 per unit. NRV is 8 each, total carrying amount 800 and write-down 200. Using selling price alone would leave carrying amount 900, overstated by 100. The write-down is the supported adjustment, not a second expense of all purchases. Currency amounts and quantities are assumed case facts. [IAS 2 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/).

```oa-check
name: Inventory lower-of-cost and complete net realisable value
inputs:
  units: 100
  cost_each: 10
  selling_price_each: 9
  completion_each: 0.5
  selling_cost_each: 0.5
steps:
  - total_cost: units * cost_each
  - nrv_each: selling_price_each - completion_each - selling_cost_each
  - carrying_amount: min(total_cost, units * nrv_each)
  - write_down: total_cost - carrying_amount
  - overstatement_if_only_selling_price_used: min(total_cost, units * selling_price_each) - carrying_amount
expected:
  total_cost: 1000
  nrv_each: 8
  carrying_amount: 800
  write_down: 200
  overstatement_if_only_selling_price_used: 100
```

## Sources

| Official standard-setter source | What was actually read for | Read on |
|---|---|---|
| https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/ | Read for About overview's complete-set components/comparatives and no compliance claim without all requirements; not the entire standard | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/ | Read for About overview's 2027 effective date, permitted early adoption and IAS 1 replacement; no automatic 2026 adoption | 2026-11-14 |
| https://standards.aasb.gov.au/aasb-116-dec-2022 | Read for operative-period header, IAS 16 comparison and paras 43 to 62A, including component/expense allocation, availability, residual/life/method reviews and cessation. This compilation applies to periods beginning January 2023 before January 2027; older 2021 compilation was excluded | 2026-11-14 |
| https://standards.aasb.gov.au/aasb-121-oct-2023 | Read for operative-period header and paras 20 to 34, initial/closing/fair-value-date measurement, P&L/OCI and net-investment/hedge exceptions; this compilation applies to periods beginning January 2025 before January 2027 | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ias-37-provisions-contingent-liabilities-and-contingent-assets/ | Read for About overview's obligation/provision/contingency, measurement and future-loss distinction; not all specialist application paragraphs | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/ | Read for About overview's recognition, research/development distinction and finite/indefinite-life amortisation/impairment | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/ | Read for About and impairment-history sections establishing the financial-instrument/expected-credit-loss task; no model, probability or allowance amount certified | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ias-8-basis-of-preparation-of-financial-statements/ | Read for About overview's policy/error retrospective versus estimate prospective distinction; actual adopted version and transitional rules still govern | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ias-10-events-after-the-reporting-period/ | Read for About overview's authorisation-for-issue window, adjusting conditions and material non-adjusting disclosure | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/ | Read for About overview's actual cost/NRV definition, measurement and sold-inventory expense recognition | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/ | Read for About overview's recognition and restoration/attributable cost categories, not a depreciation-rate table | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/ | Read for About overview's performance/control recognition boundary, not every contract-asset/warranty application | 2026-11-14 |
| https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/ | Read for About overview's actual current tax and temporary-difference/unused-loss-credit model; not all allocation, recognition-exception or Pillar Two detail | 2026-11-14 |

Not yet confirmed: each entity's actual local framework/version/early adoption, size/group/audit eligibility, nominal mapping, full notes and filing rules, functional/presentation currency, tax base/rates/loss-credit recoverability and P&L/OCI/equity tax allocation, Pillar Two exception detail, actual going-concern evidence, leases, impairment/credit-loss model and valuations. Full cash-flow classification, consolidation and specialist-standard implementation need their applicable methods. No blanket depreciation life/rate, impairment percentage, headline accounting-profit tax provision, ownership-date proration or exemption is certified here. All original adjustment families, six workpaper groups, fourteen checks, notes categories and country slots remain; missing required statements are no longer deferred to a hypothetical future version.
