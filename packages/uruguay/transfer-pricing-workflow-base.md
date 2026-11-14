---
name: transfer-pricing-workflow-base
description: Universal transfer pricing documentation and analysis workflow base that defines the related-party transaction identification, method selection, arm's length analysis, and documentation preparation runbook for all jurisdictions. Uses official authority guidance for shared analytical concepts, not a claim of identical domestic law. No local TP thresholds, penalty regimes or documentation filing portals are supplied as usable rules. This skill MUST be loaded alongside a country-specific transfer pricing skill that provides the local TP rules, documentation requirements, and filing deadlines. This skill alone cannot certify a country TP result or a completed filing package; an explicitly incomplete inventory and evidence plan may still be useful.
version: 1.1
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-11-14
tax_year: 2026
type: cross-country-method
tier: 2
domain: transfer-pricing
---

# Transfer Pricing Workflow Base Skill v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### What this file is, and what it is not

**Scope:** this shared 2026 documentation method retains transaction identification, functional/comparability analysis, method selection, pricing arithmetic and the group/entity/CbCR workstreams. The official HMRC and IRAS sources below illustrate analytical controls; they do not make an authority's law, guideline edition, exemption or practice universal. Obtain each country's actual related-party scope, effective law/guideline version, thresholds, safe harbours, penalties and prepare/retain/file/notification duties before claiming country compliance.

**This file must always be loaded with a country-specific transfer pricing skill** that provides the local TP rules, documentation requirements, filing deadlines, and penalty regimes (e.g., `uk-transfer-pricing`, `au-transfer-pricing`, `de-transfer-pricing`). This file alone cannot produce a TP documentation package. Without a companion or equivalent current official country evidence, refuse a final country conclusion. Continue only a labelled inventory/gap plan, not a filing-ready package.

**This file is the contract.** When a country transfer pricing skill says it conforms to v1.1 of this base, it means: it fills the country slots specified in Section 6, it produces outputs in the format specified in Section 4, its analysis can be validated by the self-checks in Section 5, and it participates in the workflow in Section 1.

---

## The method, step by step

### Section 1: The workflow

You are helping a multinational group or its advisors prepare transfer pricing documentation for related-party transactions. The output will be reviewed by a qualified TP specialist or tax advisor before filing or use. Your job is to do the structured analytical work , identifying transactions, selecting methods, structuring the documentation , and produce a comprehensive documentation package plus a reviewer brief that makes the professional's job fast and accurate.

Execute these seven steps in order. Do not skip. Do not reorder. Do not begin method selection before step 3. Do not present final documentation before the transaction/method analysis. Step 5 prepares controlled drafts; Step 6 runs the evidence/risk checks before delivery.

### Step 1 , Confirm the companion skills are loaded

This workflow base requires a country-specific transfer pricing skill providing the local TP rules, documentation thresholds, filing requirements, and penalty regime.

Identify the country from the records and available catalogue first. If the actual country method/source is unavailable, state the precise gap and hold the country conclusion; do not repeatedly ask a fact already in the records. Confirm all affected counterparty countries and actual period, not just the payer's location. Preserve the skill name/version/date, actual approval label and source provenance; using a named accountant's method does not mean that accountant approved this new engagement output.

If a financial statements skill or bookkeeping skill is also loaded, note their presence , the financial data from those skills feeds the functional analysis and benchmarking in this workflow.

### Step 2 , Identify related-party transactions

From the user's provided data (intercompany agreements, financial statements, management accounts, group structure charts, or narrative descriptions), identify and catalogue every related-party transaction:

**Transaction types to identify:**

- **Tangible goods.** Sales or purchases of physical goods between related entities. Note the product type, volume, and pricing mechanism (per-unit, cost-plus markup, resale minus margin).
- **Services.** Retain management/shared/technical/consulting/administrative/IT services, fee basis and beneficiary. Establish the actual benefit and willingness of an independent recipient to pay or perform it in-house; distinguish shareholder activities, unnecessary duplication and incidental group benefits before pricing. A recorded cost is not proof of a chargeable service. [HMRC services](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm440060).
- **Intangible property.** Royalty payments for trademarks, patents, know-how, software licenses, trade names. Note the intangible, the royalty rate or fee, and the contractual basis.
- **Financial transactions.** Intercompany loans (note principal, interest rate, currency, term), guarantees (note the guaranteed amount and any guarantee fee), cash pooling arrangements.
- **Cost contribution arrangements.** Shared R&D costs, shared marketing costs, or other arrangements where multiple entities contribute to and benefit from a joint activity.

For each transaction, record:

- The two related parties involved (entity name, jurisdiction, role in the group)
- The nature and description of the transaction
- The transaction value for the period
- The contractual terms and actual conduct, decision-makers, relevant records, recognition date, currency and any counterparty mismatch; no agreement is not proof that no transaction exists
- The direction of flow (payer/recipient), source-record identifiers, balances and non-cash/deemed transactions where the actual country scope includes them. Reconcile counterparties without counting both sides of the same transaction twice in a group total; do not add loan principal, annual interest and outstanding balances into one unexplained amount

Present the transaction catalogue to the user:

> "I have identified the following related-party transactions:
>
> [Numbered list: each transaction with parties, nature, and value.]
>
> Is this complete? Are there any additional intercompany transactions I should include?"

Reconcile the full available agreements, ledgers and disclosures before asking about genuinely missing transactions. Record confirmations and add identified omissions. Work on evidenced items while material completeness gaps remain visible; silence is not confirmation of completeness.

### Step 3 , Determine the applicable TP method

For each related-party transaction (or group of similar transactions), select the most appropriate reliable method under the applicable country rule. Section 2 retains the five familiar methods, without excluding another locally accepted reliable method. The selection process:

1. **Characterize the transaction.** What is being transferred (goods, services, intangibles, money)? What functions does each party perform? What assets does each party employ? What risks does each party assume?

2. **Perform a functional analysis.** For each party to the transaction, document:
   - Functions performed (manufacturing, R&D, marketing, distribution, management, administration)
   - Assets employed (tangible assets, intangible assets, financial assets)
   - Risks assumed (market risk, credit risk, inventory risk, foreign exchange risk, product liability)
   - The economically significant characteristics that determine the allocation of profit between the parties
   - Actual conduct versus agreements, control over each significant risk, financial capacity and options realistically available to both sides. Do not infer risk-bearing from a contract, entity label or legal ownership alone. Accurate delineation precedes the separate, exceptional question of disregarding a transaction. [HMRC delineation](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm440201).
   - For intangible transactions, record who actually develops, enhances, maintains, protects and exploits the intangible (DEMPE), relevant people/decisions, funding and risks, then obtain the country-specific remuneration analysis. Legal IP title alone is not a completed functional analysis. [HMRC risk/DEMPE evidence](https://www.gov.uk/government/publications/help-with-common-risks-in-transfer-pricing-approaches-gfc7/common-compliance-risks-part-2).

3. **Select the method.** Compare reliability, available data, functional fit and limitations rather than imposing a rigid ladder. CUP is preferred over another method when equally reliable; traditional transactional methods have the equivalent-reliability preference over profit methods, not automatic primacy despite worse evidence. RPM, cost plus, TNMM and profit split are candidates, not choices forced by an entity label. Document internal comparables and the best rejected alternative. [HMRC overview](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421010), [CUP](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421030).
   - Establish tested party, financial indicator and transaction segmentation for a one-sided method; assess both parties even when testing one.
   - Preserve distributor, service-provider/manufacturer, routine-function and integrated/unique-contribution profiles as investigation prompts. Highly integrated operations can justify evaluating profit split even without unique intangibles on both sides. [HMRC profit split](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421070).
   - Record why the chosen method is reliable for these actual facts and why alternatives are less reliable; no method wins merely because it produces less tax.
4. **Identify comparability factors.** For the selected method, determine what comparable data is needed:
   - Characteristics of the goods, services, or intangibles
   - Functional profiles of the parties
   - Contractual terms
   - Economic circumstances (market conditions, geographic markets)
   - Business strategies (market penetration, capacity utilization)

Present the method selection to the user for each transaction:

> "For [transaction description], I recommend the [method name] because [one-sentence reason]. The key comparability factors are [list]. The rejected methods and reasons: [brief list]."

Resolve material factual/method disagreements before a final analysis. Keep proposed methodology separate from a confirmed arm's-length conclusion; user agreement alone does not validate unreliable data.

### Step 4 , Arm's length analysis

For each transaction with a confirmed method, perform the arm's length analysis:

**Benchmarking.** Describe the benchmarking approach: the actual authorised database/source and version, access/search date and reproducible export (do not claim commercial access or a live search unless it actually occurred), the search strategy (SIC/NACE codes, geographic and independence filters), the comparable companies identified, the financial indicator used (gross margin for RPM, markup for CPM, net margin for TNMM, profit share for PSM), the supported arm's-length result/range, any adjustments and the tested result. An interquartile range is not compulsory everywhere and cannot repair non-comparable companies. Document why statistical narrowing is justified, the exact convention/software, years and observations; do not mechanically adjust every result to the median. Reconcile segment results, accounting classifications, pass-through costs, working capital, FX and loss/exceptional-item treatment with actual data. [HMRC range guidance](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm485120).

Search the provided records and available authorised official/public evidence first. If reliable comparable data remains absent, identify the specific export/evidence needed; do not request a database purchase or claim a search that was not run. Do not fabricate comparable data or financial ratios. If no benchmarking data is available, state this limitation explicitly and note the documentation will need completion before filing.

**Reasonableness check.** Even without formal benchmarking, assess whether the intercompany pricing is directionally reasonable:

- Is the proposed cost-plus result supported by the actual functions/risks, consistent cost definitions and reliable uncontrolled data? No generic manufacturer markup range is evidence of an arm's-length price. [HMRC cost plus](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421060).
- Does the royalty analysis establish what rights/services are actually supplied, the beneficiary, commercial value and reliable comparability? No generic trademark percentage is a safe range. Keep potential service/IP characterisation differences in the reviewer brief. [HMRC services and rights](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm440060).
- Is an intercompany loan rate within the range of what an unrelated lender would charge, given the borrower's creditworthiness and the loan terms?
- Does the profit allocation leave each entity with a return commensurate with its functions, assets, and risks?

Flag unsupported pricing, contradictory facts or results outside an actually reliable range as priority evidence issues. A directional observation is not a benchmark, a safe harbour or proof that a tax adjustment is due.

### Step 5 , Documentation preparation

Prepare the TP documentation following the OECD three-tiered structure described in Section 3. The country skill specifies which tiers are required and any local modifications to the OECD structure:

**Master File.** If the country skill requires a Master File (and the group exceeds the country skill's Master File threshold), prepare the group-level overview. If the user has not provided sufficient group-level information, list the specific information needed.

**Local File.** Prepare the entity-specific TP analysis for the jurisdiction in question. This is the entity-analysis workstream; determine whether the country requires a formal Local File, another record format, simplified documentation or an exemption. A package may include a non-required assessment, not a falsely mandatory filing. [HMRC specified-record scope](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm450010), [IRAS documentation](https://www.iras.gov.sg/taxes/international-tax/transfer-pricing). Include:

- Entity description and functional profile
- Transaction-by-transaction analysis (or grouped if transactions are sufficiently similar)
- Method selection and justification
- Benchmarking results (or placeholder for benchmarking to be completed)
- Arm's length conclusion for each transaction
- Financial data supporting the analysis

**Country-by-Country Report (CbCR) assessment.** Determine group/reporting-entity scope using the actual consolidated revenue period, threshold operator, currency/short-period rule and domestic implementation; assess UPE, surrogate/local filing, exchange arrangements and notifications separately. If required, note the filing obligation. Claude does not prepare the CbCR itself (it requires group-wide financial data that is typically assembled by the group's head office), but flags the obligation and deadline.

### Step 6 , Risk assessment and output delivery

Before delivering, assess the TP risk profile:

- **High-priority investigation candidates.** Unique intangibles, low-tax counterparties, losses, material values and contradictions can warrant scrutiny; none alone proves non-arm's-length pricing. Record their economic significance and evidence.
- **Medium-priority candidates.** Limited comparables, range-edge results and new transactions need evidence/context; a range-edge result is not automatically wrong.
- **Lower-priority candidates.** Reliable supported analysis or an actually applicable documented safe harbour can reduce a specific risk; a services label or documentation exemption does not automatically establish correct pricing. These are reviewer priorities, not statutory risk grades. [HMRC risk assessment](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm482170).

Produce all outputs specified in Section 4. Run the self-checks in Section 5. Deliver a completed conclusion only for checks supported by evidence. A separately labelled incomplete working package may be delivered with exact gaps; never relabel a failed required check as passed.

### Step 7 , Produce documentation package and deliver

Write a short closing chat response:

- The number of transactions documented and their total value
- The risk assessment summary (how many high, medium, low risk)
- The most important finding or concern
- Any incomplete items (benchmarking data not yet provided, group information needed for Master File)
- An invitation to revise: "If any transaction details change or you obtain benchmarking data, tell me and I'll update the documentation."

---

## Section 2 , The five OECD methods

The five methods are a shared reference shape, supported by the authority sources below. The country method establishes legal acceptance, applicable guidance edition, local preferences and any additional reliable method. No international guideline automatically overrides domestic law.

### Comparable Uncontrolled Price (CUP) method

Compares the price in the controlled transaction to the price in a comparable uncontrolled transaction. Preferred when reliable comparables exist , internal (same entity transacting with unrelated parties) or external (unrelated parties transacting with each other). Requires a high degree of comparability in goods/services, contractual terms, and economic circumstances. Adjustments for differences are permitted but must be reliable. **Financial indicator:** the transaction price itself. Prefer it at equivalent reliability, with justified adjustments rather than superficial product similarity. [HMRC CUP](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421030).

### Resale Price Method (RPM)

Starts with the resale price to an unrelated party and subtracts the resale price margin that a comparable independent reseller would earn. Adjust the residual for relevant purchase-associated costs before calling it the intercompany purchase price; customs duty, for example, may be outside the seller's amount. Best suited for distributors who resell without significant further processing. Less sensitive to product comparability than CUP , the focus is on the distribution margin. **Financial indicator:** gross margin on resales, after consistent classification and function/risk comparability. A resale gross margin is not a markup on purchase cost. [HMRC resale minus](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421050).

### Cost Plus Method (CPM)

Starts with costs incurred by the supplier and adds an appropriate markup reflecting what an unrelated party would earn for similar functions, assets, and risks. Best suited for service providers, contract manufacturers, and toll manufacturers performing functions on behalf of a related party. Requires a consistent, clearly defined cost base. **Financial indicator:** markup on the consistently defined relevant costs. Distinguish traditional gross cost plus from a net full-cost profit-level indicator under TNMM. A contractual guarantee or manufacturer label is not a substitute for analysing risk. [HMRC cost plus](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421060).

### Transactional Net Margin Method (TNMM)

Examines the net profit margin from a controlled transaction relative to an appropriate base (costs, revenue, or assets), compared to margins of comparable unrelated enterprises. Do not use the method's popularity or purported tolerance of differences as a substitute for comparability; net results can be affected by non-price factors. Appropriate when the tested party performs routine functions and one-sided analysis is sufficient. Normally choose the party for which a reliable one-sided analysis and data are available; explain complexity, assets/risks, segment selection and benchmark availability rather than choosing the local entity automatically. **Financial indicator:** relevant transaction-level net profit relative to the justified base, with a segment-to-accounts bridge. [HMRC TNMM](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421080).

### Profit Split Method (PSM)

Allocates combined profit from a controlled transaction between related parties based on each party's contributions. Two approaches: contribution analysis (allocates based on relative value of contributions) and residual analysis (first allocates routine returns, then splits residual profit based on unique intangible contributions). Evaluate highly integrated dealings and unique/valuable contributions based on actual functions and risk, not a mandatory intangible on each side. There must be reliable combined-profit and contribution data; absent one-sided comparables alone does not justify an arbitrary split. The most data-intensive and judgment-intensive method. **Financial indicator:** each party's supported share of transaction-specific combined profit or loss, on consistent accounting policies, without hindsight. [HMRC contribution/residual approaches](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421070).

### Method selection reliability review

1. Accurately delineate the transaction and compare available reliable internal/external data.
2. Evaluate CUP, RPM, cost plus, TNMM and profit split without making TNMM a last resort or requiring a particular method solely from a distributor/manufacturer label.
3. At equivalent reliability, apply the stated traditional-method/CUP preferences under the applicable rule.
4. Document the tested party, cost/base/financial indicator, adjustments and reasons the nearest alternative is less reliable.
5. For profit split, substantiate integration/contributions, combined profit or loss and allocation keys; do not infer the method only from missing comparables.
6. Check country acceptance/version/local methods and current law before concluding. [HMRC method overview](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421010).
---

## Section 3 , Documentation tiers (OECD three-tiered approach)

Preserve Master File, Local File and CbCR as distinct workstreams. Determine domestic legal scope and whether the task is preparation, retention, filing, producing on request or notification; these are different duties, with different exemptions, dates, language and responsible entities. The sources illustrate that formal specified files are not required for every entity. [HMRC records](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm450010), [IRAS](https://www.iras.gov.sg/taxes/international-tax/transfer-pricing).

### Master File

The Master File provides an overview of the multinational group, prepared, retained or provided according to each actual country requirement, not automatically filed everywhere. It covers five areas: (1) organizational structure (group chart, entities, jurisdictions, ownership), (2) business description (profit drivers, supply chains for the five largest products/services, service arrangements, geographic markets), (3) intangibles (strategy for development/ownership/exploitation, list of important intangibles and their owners, related-party IP agreements), (4) intercompany financial activities (group financing, central treasury functions, TP policies for financial transactions), and (5) financial and tax positions (consolidated financial statements, existing APAs and rulings).

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

The CbCR is filed by the ultimate parent entity of the group (or a surrogate parent) when the actual domestic scope, reference-period revenue test and filing-entity rules require it. No universal current-year amount/operator is supplied here. A parent filing elsewhere does not by itself settle local filing, exchange or notification duties. [HMRC reporting scope and responsible entities](https://www.gov.uk/guidance/check-if-you-must-send-a-country-by-country-report). Contents:

1. **Aggregate information** for each jurisdiction where the group operates: revenue (related and unrelated), profit/loss before tax, income tax paid (cash basis), income tax accrued, stated capital, accumulated earnings, number of employees, tangible assets other than cash.
2. **List of all constituent entities** of the group, their jurisdictions of incorporation and residence, and their main business activities.

Claude's role with respect to CbCR is limited: assess the actual group, period, domestic threshold, filing entity, exchange/local-filing and notification obligations, note the filing deadline, and flag the obligation. The CbCR itself is assembled from group-wide data that is beyond the scope of a single-entity TP documentation engagement.

---

## Section 4 , Output specification

Five outputs per TP documentation engagement. All five are mandatory. Never produce one without the others.

### Output 1 , Local File or entity-analysis scope assessment

The entity-specific TP analysis per Section 3's Local File structure. This is the primary analysis deliverable; if no formal Local File is legally required, state the actual exemption/scope and retain the required entity evidence instead of labelling it a mandatory filing. If benchmarking data has not been provided by the user, include the methodology and search strategy with placeholders clearly marked for completion.

### Output 2 , Master File (or Master File assessment)

If the country skill requires a Master File and sufficient group-level data is available, produce it per Section 3's Master File structure. If group-level data is insufficient, produce a Master File gap analysis listing the specific information needed from the group, organized by the Master File's five sections.

### Output 3 , Transaction matrix

A summary table of all related-party transactions:

| # | Transaction | Entity A | Entity B | Nature | Value | Method | Arm's Length? | Risk Level | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [description] | [name, jurisdiction] | [name, jurisdiction] | [goods/services/IP/financial] | [amount] | [CUP/RPM/CPM/TNMM/PSM] | [Yes/Within range/Outside range/Pending benchmarking] | [High/Medium/Low/Unresolved] | [Actual ledger/document IDs; the template itself contains no client amount. Method evidence control: HMRC](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm483030) |
| ... | | | | | | | | | [Continue source-record references; retain accounting/tax-adjustment evidence](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm483030) |

### Output 4 , CbCR assessment

A one-page assessment: whether the CbCR filing obligation is triggered, the threshold applied, the filing deadline, and the filing entity. If triggered, note the data requirements. If not triggered, state the actual evidenced reason, not automatically revenue below the threshold. Unknown group data or filing/exchange status means unresolved, not no obligation.

### Output 5 , Reviewer brief

```markdown
# [Country] Transfer Pricing Documentation , Reviewer Brief
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
- CbCR filing required: [Yes/No/Unresolved; responsible entity and notification assessed separately]
- Master File required: [Yes/No/Unresolved; actual prepare/retain/file duty]

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

## Section 5 , Self-checks (run before delivering output)

Run all ten checks against all outputs, recording pass/fail/unresolved/not applicable with evidence. Correct failures before a final package; an expressly incomplete draft retains each gap and its affected conclusion.

### Completeness

**Check 1 , All transactions documented.** Every related-party transaction identified in Step 2 and confirmed by the user appears in both the Local File and the transaction matrix. No transaction is silently omitted.

**Check 2 , Method selected for every transaction.** Every transaction in the transaction matrix has a TP method assigned. No transaction has a blank method column.

**Check 3 , Functional analysis for every transaction.** The Local File contains a functional analysis (functions, assets, risks) for both parties to every documented transaction. No transaction lacks a functional analysis.

**Check 4 , CbCR assessment present.** The CbCR assessment output exists and states whether the filing obligation is triggered, regardless of the answer.

### Consistency

**Check 5 , Transaction values reconcile.** The transaction values in the transaction matrix match the values in the Local File's transaction descriptions. If the user provided financial statements, the intercompany transaction values in the documentation are consistent with the related-party disclosures in those statements.

**Check 6: Method justification consistent with actual evidence.** Test functional profile, actual conduct, comparability and reliability together. Preserve distributor/manufacturer/intangible scenarios, but do not enforce RPM/TNMM/cost-plus/profit-split solely from a label or ban a reliable alternative by category. Verify the selected party, indicator and best rejected method, contribution/combined-result data where relevant and any actual local preference.

**Check 7 , Risk assessment consistent with analysis.** Transactions flagged as high risk in the reviewer brief have substantive reasons (pricing outside range, losses, low-tax jurisdiction, unique intangibles). Transactions flagged as low risk have supporting evidence (within arm's length range, safe harbor applicable, low-value-adding services). No transaction is flagged as low risk while having characteristics that should make it high risk.

### Accuracy

**Check 8: Country legal content separately established.** Thresholds, dates, penalties, exemptions, accepted methods/editions and filing/retention portals must come from current country evidence. Shared examples and foreign authority analytical guidance do not become local law merely by being in this base.

**Check 9 , OECD method descriptions accurate.** The method applied to each transaction aligns with the OECD description in Section 2. The financial indicator used matches the method (gross margin for RPM, markup on costs for CPM, net margin for TNMM, profit share for PSM, price for CUP).

**Check 10 , Reviewer brief disclosure complete.** Every assumption, every documentation gap, and every high-risk finding is documented in the reviewer brief. No material issue is buried in the Local File without being surfaced in the brief.

### Failure handling

If any check fails, correct and rerun it. A repeated required failure holds the affected final conclusion, not the whole evidenced inventory. Report the precise source/data/calculation gap, preserve all ten results and issue only a clearly incomplete working package while it remains unresolved. Do not silently omit a failed transaction or invent a benchmark to unblock delivery.

---

## Section 6 , Country skill contract

Every country-specific transfer pricing skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Local TP legislation** , statutory basis for transfer pricing rules, including the arm's length standard as codified in local law.
2. **Documentation requirements** , which tiers are required (Master File, Local File, CbCR), thresholds for each, content requirements (including deviations from OECD structure), and language requirements.
3. **Filing deadlines** , deadline rule for each tier (e.g., "due with annual tax return," "on request within 30 days"), and whether proactive filing or maintain-and-produce-on-request.
4. **Penalty regime** , penalties for failure to prepare, failure to file, and TP adjustments following audit. Percentage-based, fixed, or both.
5. **Materiality thresholds** , transaction value thresholds for simplified or no documentation. Safe harbor provisions for low-value-adding services or low-risk financial transactions.
6. **Accepted TP methods** , whether the five OECD methods are accepted, additional local methods, and local preferences or hierarchy.
7. **Benchmarking requirements** , local vs. pan-regional comparables, acceptable databases, refresh frequency.
8. **Advance Pricing Agreement (APA) availability** , unilateral, bilateral, multilateral; process and typical timeline.
9. **Related domestic rules** , thin capitalization rules, CFC rules, and domestic anti-avoidance provisions that overlap with TP.
10. **Currency and exchange rate conventions** , documentation currency, exchange rate basis (spot, average, year-end), official rate source.

### Optional slots

11. **Industry-specific guidance** , TP guidelines for specific industries (financial services, extractive industries, pharmaceuticals) issued by the local tax authority.
12. **Bilateral treaty positions** , key MAP provisions, corresponding adjustment mechanisms, and the jurisdiction's track record.
13. **Integration notes** , how the TP skill interacts with the country's corporate tax, financial statements, or bookkeeping skills.

---

## Worked cases

### RPM gross margin is not a purchase-cost markup

Assume a reliable, consistently defined comparable resale gross margin of 25% is supplied as a case fact, unrelated resale proceeds of 1,000 and separately borne purchase-associated duty of 20. The amount available for the intercompany goods price is 1,000 less 250 gross margin less 20 duty = 730. Dividing 1,000 by 1.25 instead confuses gross margin on sales with markup on cost and omits the duty adjustment. The illustrative margin is not an industry norm or a statutory safe harbour. [HMRC RPM mechanics](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421050).

```oa-check
name: Resale price margin and purchase associated cost reconciliation
inputs:
  unrelated_resale: 1000
  assumed_supported_resale_margin: 0.25
  purchase_duty: 20
steps:
  - reseller_gross_margin: unrelated_resale * assumed_supported_resale_margin
  - price_before_purchase_cost_adjustment: unrelated_resale - reseller_gross_margin
  - intercompany_goods_price: price_before_purchase_cost_adjustment - purchase_duty
expected:
  reseller_gross_margin: 250
  price_before_purchase_cost_adjustment: 750
  intercompany_goods_price: 730
```

### Residual split conserves combined profit

Assume a reliably delineated transaction has combined profit 300, supported basic returns of 40 and 60, and a residual allocation key of 60%/40% established from actual contributions. Residual profit is 200; final allocations are 160 and 140, summing to 300. These assumed returns/keys are not statutory rates, a benchmark or a conclusion that profit split is appropriate for a real business. Do not allocate routine returns twice or substitute uneliminated intercompany income for combined external profit. Loss cases need their actual contribution/risk analysis. [HMRC residual analysis](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421070).

```oa-check
name: Residual allocation includes basic returns once and preserves combined profit
inputs:
  combined_profit: 300
  basic_return_a: 40
  basic_return_b: 60
  assumed_residual_key_a: 0.60
steps:
  - residual_profit: combined_profit - basic_return_a - basic_return_b
  - final_a: basic_return_a + residual_profit * assumed_residual_key_a
  - final_b: basic_return_b + residual_profit * (1 - assumed_residual_key_a)
  - allocation_difference: final_a + final_b - combined_profit
expected:
  residual_profit: 200
  final_a: 160
  final_b: 140
  allocation_difference: 0
```

## When to refuse or refer

Hold a final country package without current country legal requirements, reliable functional facts or required financial/comparable data. Preserve every related-party transaction and incomplete method, rather than fabricating an arm's-length conclusion. Complex intangibles, financial transactions, disputed actual conduct, unsupported adjustments or double-tax/MAP issues go to the relevant specialist with an evidence list. CbCR preparation and MAP/competent-authority proceedings remain outside this documentation engagement; assessing their existence and deadlines remains in scope. Do not post a TP adjustment, backdate an agreement, submit a file or contact an authority merely because a draft has been prepared.

## Section 7 , Reference material

### Validation status

This file is v1.1 of `transfer-pricing-workflow-base`, updated as a shared 2026 method with bounded official-source reads and recomputing illustrative cases. It is not a completed country engagement or accountant approval. It follows the structural pattern established by `bookkeeping-workflow-base` v1.0 and `vat-workflow-base` v0.2.0.

### Design decisions

1. **Documentation focus, not advisory.** This workflow produces TP documentation (the compliance deliverable), not planning or optimization advice. The documentation describes and supports pricing as it exists.

2. **Benchmarking requires actual evidence/access.** Integrate provided exports or authorised accessible data, preserving reproducibility and rejection criteria; never pretend a commercial database search occurred. The method defines the evidence needed rather than inventing results.

3. **Shared shape, country law.** Retain all five methods and three documentation workstreams, applying actual domestic scope and acceptance instead of assuming universal filing requirements.

4. **Risk assessment as output, not gatekeeper.** The risk level affects reviewer attention priority, not whether documentation is produced.

### Known gaps

1. Benchmarking execution (database searches, rejection criteria, statistical ranges) cannot be performed without database access. By design.
2. Profit Split quantitative calculation requires judgment beyond automated documentation scope.
3. DEMPE evidence is explicitly collected during functional analysis; the complete country-specific IP valuation/remuneration analysis and any hard-to-value intangible rules still require specialist evidence.
4. Each run covers a specific fiscal year. Preserve prior documentation/data and identify current changes/refresh obligations; this method does not itself manage a multi-year statutory retention system.
5. Mutual Agreement Procedure (MAP) and competent authority cases are not in scope.

### Change log

- **v1.1 (14 November 2026):** Corrects rigid method/range shortcuts, actual-conduct analysis, transaction reconciliation and documentation/filing scope, while retaining seven workflow steps, five methods, five outputs, ten checks and thirteen country slots.

- **v1.0 (May 2026):** Initial release. Establishes the universal transfer pricing documentation workflow, five OECD methods reference, three-tiered documentation structure, five-output specification, 10 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| HMRC INTM421010. Read for method summary, other methods and equivalent-reliability preference; opening reform/version warning read, no 2026 UK statutory interpretation adopted | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421010 | 2026-11-14 |
| HMRC INTM421030. Read for complete CUP comparability/reliable-adjustment and preference discussion | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421030 | 2026-11-14 |
| HMRC INTM421050. Read for operative resale-minus mechanics, purchase-cost adjustment and functional comparability | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421050 | 2026-11-14 |
| HMRC INTM421060. Read for opening cost-plus explanation, cost-classification comparisons, manufacturing and contract-manufacturer label cautions; not the entire later share-option discussion | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421060 | 2026-11-14 |
| HMRC INTM421070. Read for complete operative contribution/residual split discussion, integration, economic function/risk and allocation evidence | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421070 | 2026-11-14 |
| HMRC INTM421080. Read for operative TNMM internal/external comparable discussion, non-price weaknesses and reliable-range limits | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm421080 | 2026-11-14 |
| HMRC INTM485120. Read for opening range reliability, interquartile-range non-mandatory rule, statistical conditions and initial narrowing factors; not every later adjustment example | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm485120 | 2026-11-14 |
| HMRC INTM440201. Read for accurate delineation/actual conduct and risk-control/capacity sections, separate disregard discussion; not every historical alternative | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm440201 | 2026-11-14 |
| HMRC INTM440060. Read for service benefit, provider/recipient perspectives, rights-versus-services, duplication/incidental group and shareholder-activity sections | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm440060 | 2026-11-14 |
| HMRC INTM450010. Read for specified-record scope, Master/Local files, retain/produce-on-request distinction, annual review and exemptions; not every linked scope provision | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm450010 | 2026-11-14 |
| HMRC INTM483030. Read for opening proportionality discussion and four classes of accounting/tax-adjustment/controlled-transaction/arm's-length evidence | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm483030 | 2026-11-14 |
| HMRC INTM482170. Read for operative qualitative risk assessment and profit-driver/function/risk mismatch discussion | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm482170 | 2026-11-14 |
| IRAS transfer pricing. Read for arm's-length introduction, method/tested-party workflow and documentation scope/content/prepare-retain-submit table; not the full linked e-Tax Guide | https://www.iras.gov.sg/taxes/international-tax/transfer-pricing | 2026-11-14 |
| HMRC current CbCR public guidance. Read for prior-period revenue and UPE/other-entity filing/exchange assessment; threshold equality is not certified from this page alone | https://www.gov.uk/guidance/check-if-you-must-send-a-country-by-country-report | 2026-11-14 |
| Current UK CbCR Regulations 2016 reg. 3. Read complete group/period/threshold, FX and period-scaling text via public legislative snippet | https://www.legislation.gov.uk/uksi/2016/237/regulation/3/data.xht?view=snippet&wrap=true | 2026-11-14 |
| Current UK CbCR reg. 3A. Read complete operative parent-filing duty and amendment notes; reg. 4 was separately read as omitted, so its original as-made wording is not current authority | https://www.legislation.gov.uk/uksi/2016/237/regulation/3A/data.xht?view=snippet&wrap=true | 2026-11-14 |
| HMRC common compliance risks, part two. Read for the end of risk-control analysis and section 2.2.6 intangible/DEMPE facts, historic contributions and specificity; not every section of the publication | https://www.gov.uk/government/publications/help-with-common-risks-in-transfer-pricing-approaches-gfc7/common-compliance-risks-part-2 | 2026-11-14 |

Not yet confirmed: every actual country's 2026 related-party definition, guideline edition, accepted method/local preference, safe harbour, documentation/materiality thresholds, current forms, language, deadline, penalty, APA process and currency rules; detailed current intangible/DEMPE remuneration, financial transaction/guarantee/cash-pool and cost-contribution analysis; actual comparable exports, statistical convention, profit-level indicator and segment bridge for any real case; actual CbCR threshold/equality/reference-year/currency/short-period, surrogate/local filing, exchange and notification requirements. The old global EUR 750-million/exceeds shortcut is not usable here: HMRC public guidance says more than, while current reg. 3 defines a threshold amount without that phrase; reg. 4's former wording was repealed. Both current sources were read and linked above, but a boundary-sensitive UK conclusion is held rather than guessed. Complete country legal resolution and filing evidence are needed; no review of a specific taxpayer is claimed.
