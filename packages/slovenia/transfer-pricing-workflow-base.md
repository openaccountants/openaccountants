---
name: transfer-pricing-workflow-base
description: Universal transfer pricing documentation and analysis workflow base that defines the related-party transaction identification, method selection, arm's length analysis, and documentation preparation runbook for all jurisdictions. Contains no jurisdiction-specific content — no local TP thresholds, no penalty regimes, no specific documentation filing portals. This skill MUST be loaded alongside a country-specific transfer pricing skill that provides the local TP rules, documentation requirements, and filing deadlines. This skill alone cannot produce any output.
version: 1.0
category: foundation
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# Transfer Pricing Workflow Base Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a transfer pricing documentation task: the order of operations, how to identify related-party transactions, how to select and apply a transfer pricing method, how to structure documentation per the OECD three-tiered approach, what to check before delivering. It contains no local TP thresholds, no penalty rates, no documentation filing portals, no specific safe harbor rules, no country-specific materiality limits.

**This file must always be loaded with a country-specific transfer pricing skill** that provides the local TP rules, documentation requirements, filing deadlines, and penalty regimes (e.g., `uk-transfer-pricing`, `au-transfer-pricing`, `de-transfer-pricing`). This file alone cannot produce a TP documentation package. Loading it without a companion is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a country transfer pricing skill says it conforms to v1.0 of this base, it means: it fills the country slots specified in Section 6, it produces outputs in the format specified in Section 4, its analysis can be validated by the self-checks in Section 5, and it participates in the workflow in Section 1.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping a multinational group or its advisors prepare transfer pricing documentation for related-party transactions. The output will be reviewed by a qualified TP specialist or tax advisor before filing or use. Your job is to do the structured analytical work — identifying transactions, selecting methods, structuring the documentation — and produce a comprehensive documentation package plus a reviewer brief that makes the professional's job fast and accurate.

Execute these seven steps in order. Do not skip. Do not reorder. Do not begin method selection before step 3. Do not build any documentation files before step 6.

### Step 1 — Confirm the companion skills are loaded

This workflow base requires a country-specific transfer pricing skill providing the local TP rules, documentation thresholds, filing requirements, and penalty regime.

If no country-specific skill is loaded, stop and tell the user: "I need a country-specific transfer pricing skill loaded alongside this workflow base. Which jurisdiction is this TP documentation for?" Do not proceed without it.

If a financial statements skill or bookkeeping skill is also loaded, note their presence — the financial data from those skills feeds the functional analysis and benchmarking in this workflow.

### Step 2 — Identify related-party transactions

From the user's provided data (intercompany agreements, financial statements, management accounts, group structure charts, or narrative descriptions), identify and catalogue every related-party transaction:

**Transaction types to identify:**

- **Tangible goods.** Sales or purchases of physical goods between related entities. Note the product type, volume, and pricing mechanism (per-unit, cost-plus markup, resale minus margin).
- **Services.** Management fees, shared service charges, technical assistance, consulting, administrative support, IT services. Note the service description, the fee basis (cost-plus, fixed fee, percentage of revenue), and whether the service provides a benefit to the recipient.
- **Intangible property.** Royalty payments for trademarks, patents, know-how, software licenses, trade names. Note the intangible, the royalty rate or fee, and the contractual basis.
- **Financial transactions.** Intercompany loans (note principal, interest rate, currency, term), guarantees (note the guaranteed amount and any guarantee fee), cash pooling arrangements.
- **Cost contribution arrangements.** Shared R&D costs, shared marketing costs, or other arrangements where multiple entities contribute to and benefit from a joint activity.

For each transaction, record:

- The two related parties involved (entity name, jurisdiction, role in the group)
- The nature and description of the transaction
- The transaction value for the period
- The contractual terms (if an intercompany agreement exists)
- The direction of flow (which entity is the payer, which is the recipient)

Present the transaction catalogue to the user:

> "I have identified the following related-party transactions:
>
> [Numbered list: each transaction with parties, nature, and value.]
>
> Is this complete? Are there any additional intercompany transactions I should include?"

Wait for confirmation. If the user identifies additional transactions, add them to the catalogue.

### Step 3 — Determine the applicable TP method

For each related-party transaction (or group of similar transactions), select the most appropriate transfer pricing method from the five OECD-approved methods described in Section 2. The selection process:

1. **Characterize the transaction.** What is being transferred (goods, services, intangibles, money)? What functions does each party perform? What assets does each party employ? What risks does each party assume?

2. **Perform a functional analysis.** For each party to the transaction, document:
   - Functions performed (manufacturing, R&D, marketing, distribution, management, administration)
   - Assets employed (tangible assets, intangible assets, financial assets)
   - Risks assumed (market risk, credit risk, inventory risk, foreign exchange risk, product liability)
   - The economically significant characteristics that determine the allocation of profit between the parties

3. **Select the method.** Apply the OECD hierarchy:
   - The Comparable Uncontrolled Price (CUP) method is preferred when reliable comparable uncontrolled transactions exist.
   - If CUP is not reliably applicable, apply the method most appropriate to the transaction type and the available data: Resale Price Method for distributors, Cost Plus Method for service providers and contract manufacturers, TNMM for routine functions, Profit Split for highly integrated transactions involving unique intangibles on both sides.
   - Document why the selected method is the most appropriate and why the rejected methods are less appropriate.

4. **Identify comparability factors.** For the selected method, determine what comparable data is needed:
   - Characteristics of the goods, services, or intangibles
   - Functional profiles of the parties
   - Contractual terms
   - Economic circumstances (market conditions, geographic markets)
   - Business strategies (market penetration, capacity utilization)

Present the method selection to the user for each transaction:

> "For [transaction description], I recommend the [method name] because [one-sentence reason]. The key comparability factors are [list]. The rejected methods and reasons: [brief list]."

Wait for confirmation before proceeding to Step 4.

### Step 4 — Arm's length analysis

For each transaction with a confirmed method, perform the arm's length analysis:

**Benchmarking.** Describe the benchmarking approach: the database or source used (the user typically provides this — Claude cannot access commercial databases like Orbis or Capital IQ directly), the search strategy (SIC/NACE codes, geographic and independence filters), the comparable companies identified, the financial indicator used (gross margin for RPM, markup for CPM, net margin for TNMM, profit share for PSM), the arm's length range (interquartile range), and where the tested party's result falls.

If the user has not provided comparable data, explain what is needed and ask them to provide search results. Do not fabricate comparable data or financial ratios. If no benchmarking data is available, state this limitation explicitly and note the documentation will need completion before filing.

**Reasonableness check.** Even without formal benchmarking, assess whether the intercompany pricing is directionally reasonable:

- Is a cost-plus markup within a plausible range for the function performed? (A contract manufacturer at 50% markup is unusual; at 5-15% it is typical.)
- Is a royalty rate within a plausible range for the intangible type? (A trademark royalty of 25% of revenue is unusual for most industries; 1-5% is more common.)
- Is an intercompany loan rate within the range of what an unrelated lender would charge, given the borrower's creditworthiness and the loan terms?
- Does the profit allocation leave each entity with a return commensurate with its functions, assets, and risks?

Flag any pricing that appears outside plausible ranges as a high-priority item in the reviewer brief.

### Step 5 — Documentation preparation

Prepare the TP documentation following the OECD three-tiered structure described in Section 3. The country skill specifies which tiers are required and any local modifications to the OECD structure:

**Master File.** If the country skill requires a Master File (and the group exceeds the country skill's Master File threshold), prepare the group-level overview. If the user has not provided sufficient group-level information, list the specific information needed.

**Local File.** Prepare the entity-specific TP analysis for the jurisdiction in question. This is the core deliverable and is required in virtually all jurisdictions with TP documentation rules. Include:

- Entity description and functional profile
- Transaction-by-transaction analysis (or grouped if transactions are sufficiently similar)
- Method selection and justification
- Benchmarking results (or placeholder for benchmarking to be completed)
- Arm's length conclusion for each transaction
- Financial data supporting the analysis

**Country-by-Country Report (CbCR) assessment.** Determine whether the group is required to file a CbCR based on the country skill's consolidated revenue threshold. If required, note the filing obligation. Claude does not prepare the CbCR itself (it requires group-wide financial data that is typically assembled by the group's head office), but flags the obligation and deadline.

### Step 6 — Risk assessment and output delivery

Before delivering, assess the TP risk profile:

- **High risk.** Unique intangibles, low-tax jurisdiction counterparties, tested party losses, values exceeding materiality thresholds.
- **Medium risk.** Limited benchmarking data, results near arm's length range edges, new transaction types.
- **Low risk.** Robust benchmarking, safe harbors, low-value-adding services within exemptions.

Produce all outputs specified in Section 4. Run the self-checks in Section 5. Only deliver when all checks pass.

### Step 7 — Produce documentation package and deliver

Write a short closing chat response:

- The number of transactions documented and their total value
- The risk assessment summary (how many high, medium, low risk)
- The most important finding or concern
- Any incomplete items (benchmarking data not yet provided, group information needed for Master File)
- An invitation to revise: "If any transaction details change or you obtain benchmarking data, tell me and I'll update the documentation."

---

## Section 2 — The five OECD methods

This section describes the five OECD-approved transfer pricing methods. The country skill may specify additional locally accepted methods or preferences. The OECD methods are the universal baseline.

### Comparable Uncontrolled Price (CUP) method

Compares the price in the controlled transaction to the price in a comparable uncontrolled transaction. Preferred when reliable comparables exist — internal (same entity transacting with unrelated parties) or external (unrelated parties transacting with each other). Requires a high degree of comparability in goods/services, contractual terms, and economic circumstances. Adjustments for differences are permitted but must be reliable. **Financial indicator:** the transaction price itself.

### Resale Price Method (RPM)

Starts with the resale price to an unrelated party and subtracts the resale price margin that a comparable independent reseller would earn. The residual is the arm's length intercompany purchase price. Best suited for distributors who resell without significant further processing. Less sensitive to product comparability than CUP — the focus is on the distribution margin. **Financial indicator:** gross margin on resales.

### Cost Plus Method (CPM)

Starts with costs incurred by the supplier and adds an appropriate markup reflecting what an unrelated party would earn for similar functions, assets, and risks. Best suited for service providers, contract manufacturers, and toll manufacturers performing functions on behalf of a related party. Requires a consistent, clearly defined cost base. **Financial indicator:** markup on costs.

### Transactional Net Margin Method (TNMM)

Examines the net profit margin from a controlled transaction relative to an appropriate base (costs, revenue, or assets), compared to margins of comparable unrelated enterprises. The most commonly applied method in practice — less sensitive to transactional differences than CUP, RPM, or CPM. Appropriate when the tested party performs routine functions and one-sided analysis is sufficient. The tested party must be the less complex party whose functions can be reliably benchmarked. **Financial indicator:** net profit margin relative to an appropriate base.

### Profit Split Method (PSM)

Allocates combined profit from a controlled transaction between related parties based on each party's contributions. Two approaches: contribution analysis (allocates based on relative value of contributions) and residual analysis (first allocates routine returns, then splits residual profit based on unique intangible contributions). Appropriate for highly integrated transactions where both parties contribute unique and valuable intangibles. The most data-intensive and judgment-intensive method. **Financial indicator:** each party's share of combined profit.

### Method selection hierarchy

1. Use CUP when reliable comparables exist.
2. If CUP is not applicable, choose from RPM, CPM, TNMM, or PSM based on the transaction type and functional profile.
3. RPM and CPM are preferred when the tested party's profile closely matches their assumptions (distributor for RPM, cost-based for CPM).
4. TNMM is the fallback for routine functions when RPM or CPM comparables are insufficient.
5. PSM is reserved for transactions where both parties contribute unique value.
6. The country skill may specify a local preference or override this hierarchy.

---

## Section 3 — Documentation tiers (OECD three-tiered approach)

The OECD BEPS Action 13 establishes a three-tiered documentation structure. The country skill specifies which tiers are required, the local thresholds, and any modifications.

### Master File

The Master File provides an overview of the multinational group, filed in each jurisdiction where the group has entities (subject to local thresholds). It covers five areas: (1) organizational structure (group chart, entities, jurisdictions, ownership), (2) business description (profit drivers, supply chains for the five largest products/services, service arrangements, geographic markets), (3) intangibles (strategy for development/ownership/exploitation, list of important intangibles and their owners, related-party IP agreements), (4) intercompany financial activities (group financing, central treasury functions, TP policies for financial transactions), and (5) financial and tax positions (consolidated financial statements, existing APAs and rulings).

### Local File

The Local File provides detailed TP analysis for the specific entity. It is the core compliance document. Contents:

1. **Entity description.** Management structure, local organization chart, reporting lines, individuals to whom local management reports.
2. **Business description.** Nature of the business, business strategy, key competitors.
3. **Controlled transactions.** For each material transaction or category:
   - Description and context
   - Amount
   - Counterparty entities involved
   - Intercompany agreements
   - Functional analysis (functions, assets, risks of each party)
   - Method selection and justification
   - Comparability analysis (search strategy, comparable selection, adjustments)
   - Benchmarking results and arm's length range
   - Conclusion on arm's length nature
4. **Financial information.** Financial statements for the fiscal year, reconciliation of financial data to the TP analysis, summary schedules of relevant financial data for comparables.

### Country-by-Country Report (CbCR)

The CbCR is filed by the ultimate parent entity of the group (or a surrogate parent) if the group's consolidated revenue exceeds the threshold (€750 million in OECD guidelines; the country skill provides the local implementation). Contents:

1. **Aggregate information** for each jurisdiction where the group operates: revenue (related and unrelated), profit/loss before tax, income tax paid (cash basis), income tax accrued, stated capital, accumulated earnings, number of employees, tangible assets other than cash.
2. **List of all constituent entities** of the group, their jurisdictions of incorporation and residence, and their main business activities.

Claude's role with respect to CbCR is limited: assess whether the filing obligation is triggered (based on the group's consolidated revenue versus the country skill's threshold), note the filing deadline, and flag the obligation. The CbCR itself is assembled from group-wide data that is beyond the scope of a single-entity TP documentation engagement.

---

## Section 4 — Output specification

Five outputs per TP documentation engagement. All five are mandatory. Never produce one without the others.

### Output 1 — Local File

The entity-specific TP analysis per Section 3's Local File structure. This is the primary deliverable. If benchmarking data has not been provided by the user, include the methodology and search strategy with placeholders clearly marked for completion.

### Output 2 — Master File (or Master File assessment)

If the country skill requires a Master File and sufficient group-level data is available, produce it per Section 3's Master File structure. If group-level data is insufficient, produce a Master File gap analysis listing the specific information needed from the group, organized by the Master File's five sections.

### Output 3 — Transaction matrix

A summary table of all related-party transactions:

| # | Transaction | Entity A | Entity B | Nature | Value | Method | Arm's Length? | Risk Level |
|---|---|---|---|---|---|---|---|---|
| 1 | [description] | [name, jurisdiction] | [name, jurisdiction] | [goods/services/IP/financial] | [amount] | [CUP/RPM/CPM/TNMM/PSM] | [Yes/Within range/Outside range/Pending benchmarking] | [High/Medium/Low] |
| ... | | | | | | | | |

### Output 4 — CbCR assessment

A one-page assessment: whether the CbCR filing obligation is triggered, the threshold applied, the filing deadline, and the filing entity. If triggered, note the data requirements. If not triggered, state the reason (consolidated revenue below threshold).

### Output 5 — Reviewer brief

```markdown
# [Country] Transfer Pricing Documentation — Reviewer Brief
**Entity:** [name and jurisdiction]
**Group:** [ultimate parent name]
**Period:** [fiscal year]
**Generated:** [date]

## Summary
- Related-party transactions documented: [count]
- Total value of controlled transactions: [amount] [currency]
- Methods applied: [list of methods used]
- High risk transactions: [count]
- Medium risk transactions: [count]
- Low risk transactions: [count]
- CbCR filing required: [Yes/No]
- Master File required: [Yes/No]

## High-priority items (review first)
[Numbered list: transactions with the highest risk, pricing outside
plausible ranges, transactions involving unique intangibles, losses
in tested party, transactions with low-tax jurisdiction entities.
Each: one sentence what, one sentence why it matters, one sentence
what the reviewer should do.]

## Benchmarking status
[For each transaction: whether benchmarking is complete, pending,
or not applicable. If pending, what data is needed.]

## Method selection rationale
[For each transaction: one-sentence summary of why the method was
selected and the key rejected alternative.]

## Assumptions made
[For each assumption: the assumption, what it affects, and what
changes if the assumption is wrong.]

## Documentation gaps
[Specific items that must be completed before the documentation can
be filed: missing benchmarking data, missing intercompany agreements,
missing group-level information for the Master File.]

## Filing deadlines
- Local File due: [deadline per country skill]
- Master File due: [deadline per country skill]
- CbCR due: [deadline per country skill, if applicable]
- Penalty for late filing: [per country skill]
```

---

## Section 5 — Self-checks (run before delivering output)

Run these ten checks against all outputs. If any fails, fix and re-run. Do not deliver until all pass.

### Completeness

**Check 1 — All transactions documented.** Every related-party transaction identified in Step 2 and confirmed by the user appears in both the Local File and the transaction matrix. No transaction is silently omitted.

**Check 2 — Method selected for every transaction.** Every transaction in the transaction matrix has a TP method assigned. No transaction has a blank method column.

**Check 3 — Functional analysis for every transaction.** The Local File contains a functional analysis (functions, assets, risks) for both parties to every documented transaction. No transaction lacks a functional analysis.

**Check 4 — CbCR assessment present.** The CbCR assessment output exists and states whether the filing obligation is triggered, regardless of the answer.

### Consistency

**Check 5 — Transaction values reconcile.** The transaction values in the transaction matrix match the values in the Local File's transaction descriptions. If the user provided financial statements, the intercompany transaction values in the documentation are consistent with the related-party disclosures in those statements.

**Check 6 — Method justification consistent with functional analysis.** For every transaction, the selected method is consistent with the functional profile. A distributor is tested with RPM or TNMM, not Cost Plus. A contract manufacturer is tested with Cost Plus or TNMM, not RPM. A transaction involving unique intangibles on both sides uses Profit Split, not a one-sided method. If a method is inconsistent with the functional profile, either the method or the functional analysis is wrong.

**Check 7 — Risk assessment consistent with analysis.** Transactions flagged as high risk in the reviewer brief have substantive reasons (pricing outside range, losses, low-tax jurisdiction, unique intangibles). Transactions flagged as low risk have supporting evidence (within arm's length range, safe harbor applicable, low-value-adding services). No transaction is flagged as low risk while having characteristics that should make it high risk.

### Accuracy

**Check 8 — No jurisdiction-specific content from this base.** Verify that all thresholds, deadlines, penalty amounts, and filing portal names come from the country skill. This base provides the framework; the country skill provides the jurisdiction-specific content.

**Check 9 — OECD method descriptions accurate.** The method applied to each transaction aligns with the OECD description in Section 2. The financial indicator used matches the method (gross margin for RPM, markup on costs for CPM, net margin for TNMM, profit share for PSM, price for CUP).

**Check 10 — Reviewer brief disclosure complete.** Every assumption, every documentation gap, and every high-risk finding is documented in the reviewer brief. No material issue is buried in the Local File without being surfaced in the brief.

### Failure handling

If any check fails, fix the output and re-run all ten. Do not deliver until all pass. If a check fails twice in a row on the same item, stop and report the failure to the user.

---

## Section 6 — Country skill contract

Every country-specific transfer pricing skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Local TP legislation** — statutory basis for transfer pricing rules, including the arm's length standard as codified in local law.
2. **Documentation requirements** — which tiers are required (Master File, Local File, CbCR), thresholds for each, content requirements (including deviations from OECD structure), and language requirements.
3. **Filing deadlines** — deadline rule for each tier (e.g., "due with annual tax return," "on request within 30 days"), and whether proactive filing or maintain-and-produce-on-request.
4. **Penalty regime** — penalties for failure to prepare, failure to file, and TP adjustments following audit. Percentage-based, fixed, or both.
5. **Materiality thresholds** — transaction value thresholds for simplified or no documentation. Safe harbor provisions for low-value-adding services or low-risk financial transactions.
6. **Accepted TP methods** — whether the five OECD methods are accepted, additional local methods, and local preferences or hierarchy.
7. **Benchmarking requirements** — local vs. pan-regional comparables, acceptable databases, refresh frequency.
8. **Advance Pricing Agreement (APA) availability** — unilateral, bilateral, multilateral; process and typical timeline.
9. **Related domestic rules** — thin capitalization rules, CFC rules, and domestic anti-avoidance provisions that overlap with TP.
10. **Currency and exchange rate conventions** — documentation currency, exchange rate basis (spot, average, year-end), official rate source.

### Optional slots

11. **Industry-specific guidance** — TP guidelines for specific industries (financial services, extractive industries, pharmaceuticals) issued by the local tax authority.
12. **Bilateral treaty positions** — key MAP provisions, corresponding adjustment mechanisms, and the jurisdiction's track record.
13. **Integration notes** — how the TP skill interacts with the country's corporate tax, financial statements, or bookkeeping skills.

---

## Section 7 — Reference material

### Validation status

This file is v1.0 of `transfer-pricing-workflow-base`, drafted as part of the Open Accountants skill architecture in May 2026. It follows the structural pattern established by `bookkeeping-workflow-base` v1.0 and `vat-workflow-base` v0.2.0.

### Design decisions

1. **Documentation focus, not advisory.** This workflow produces TP documentation (the compliance deliverable), not planning or optimization advice. The documentation describes and supports pricing as it exists.

2. **Benchmarking as a user-provided input.** Claude cannot access commercial TP databases. The workflow defines methodology and search criteria, integrating user-provided results.

3. **OECD as the universal baseline.** The five methods and three-tiered structure are universal. Country skills overlay local modifications.

4. **Risk assessment as output, not gatekeeper.** The risk level affects reviewer attention priority, not whether documentation is produced.

### Known gaps

1. Benchmarking execution (database searches, rejection criteria, statistical ranges) cannot be performed without database access. By design.
2. Profit Split quantitative calculation requires judgment beyond automated documentation scope.
3. DEMPE analysis is referenced but not specified as a separate step.
4. Multi-year documentation management is not covered — each run covers a single fiscal year.
5. Mutual Agreement Procedure (MAP) and competent authority cases are not in scope.

### Change log

- **v1.0 (May 2026):** Initial release. Establishes the universal transfer pricing documentation workflow, five OECD methods reference, three-tiered documentation structure, five-output specification, 10 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
