---
name: cross-border-workflow-base
description: >
  Master orchestrator for multi-jurisdiction cases. Coordinates all 7 accounting domains
  (tax, bookkeeping, payroll, VAT/GST, e-invoicing, financial statements, transfer pricing)
  across multiple countries. Use when the user mentions two or more jurisdictions, foreign
  income, relocation, foreign subsidiaries, importing/exporting, or remote workers abroad.
  This skill activates BEFORE any single-country skill when a cross-border element is detected.
  It produces a consolidated compliance map across all involved jurisdictions.
version: 1.0
category: foundation
depends_on:
  - tax-residency-planning
  - permanent-establishment-risk
  - withholding-tax-matrix
  - eu-social-security-coordination
  - eu-directives-cross-border
  - oecd-model-treaty-defaults
jurisdiction: GLOBAL
last_updated: 2026-06-12
tier: 2
---

# Cross-Border Workflow Base — Master Multi-Jurisdiction Orchestrator

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

This is the **master orchestrator** for any case involving more than one jurisdiction. It coordinates all seven accounting domains across multiple countries and produces a unified compliance map. It does not contain country-specific rules — those come from the individual country skills loaded in Step 3. It contains the workflow, the coordination logic, and the output specification.

**This file activates when a cross-border element is detected.** It sits above individual country skills and below the global router. The global router hands off to this skill when it detects multi-jurisdiction signals; this skill then loads the relevant country skills and coordinates them.

---

## Section 1 — When this skill activates (detection triggers)

Activate this skill when ANY of the following signals are present in the user's message or context:

| Signal Category | Examples |
|----------------|----------|
| Two or more countries mentioned | "I live in Germany but have clients in the US and UK" |
| Foreign income or clients | "I invoice clients abroad", "I receive payments from overseas" |
| Relocation or moving | "I'm moving from the UK to Portugal", "I relocated last year" |
| Foreign company or subsidiary | "My company has a branch in Ireland", "I set up an LLC in the US" |
| Importing or exporting | "I sell goods to EU customers", "I import from China" |
| Remote workers abroad | "My developer works from Poland", "I have a remote team in India" |
| Cross-border payments | "Withholding tax was deducted", "I need to claim treaty relief" |
| Digital nomad signals | "I work from different countries", "I travel while working" |
| Intercompany transactions | "Transfer pricing", "management fees between entities" |
| Social security abroad | "Which country do I pay social security in", "A1 certificate" |

**If none of these signals are present, do NOT activate this skill.** Hand off to the single-country workflow instead.

---

## Section 2 — The cross-border intake workflow (10 steps)

Execute these ten steps in order. Do not skip. Do not reorder. Do not produce outputs before Step 10.

### Step 1 — Map all jurisdictions involved

Identify every country that has a role in the user's situation. Classify each:

| Role | Definition | Example |
|------|-----------|---------|
| **Resident country** | Where the individual/entity is tax-resident | Germany (where the founder lives) |
| **Source country** | Where income originates or is earned | US (where the client pays from) |
| **Company country** | Where a business entity is incorporated | Ireland (where the Ltd is registered) |
| **Employment country** | Where work is physically performed | Poland (where the remote worker sits) |
| **Supply country** | Where goods/services are delivered to | France (where the customer receives) |

A single country may have multiple roles. List all. If uncertain about a country's role, ask the user ONE clarifying question before proceeding.

### Step 2 — Classify the cross-border scenario type

Every cross-border case fits one or more of these types:

| Type | Description | Primary domains triggered |
|------|-------------|--------------------------|
| **Type A** | Freelancer/business with foreign clients | VAT place of supply + WHT + income tax |
| **Type B** | Relocated individual (mid-year or recent move) | Residency determination + split-year + exit tax |
| **Type C** | Company with foreign employees or remote workers | Payroll + social security coordination |
| **Type D** | Multi-entity group with cross-border transactions | Transfer pricing + PE risk + consolidated accounts |
| **Type E** | Digital nomad / no fixed base / perpetual traveller | Residency tie-breaker + PE risk + SS coordination |
| **Type F** | Foreign company formation | Formation + substance requirements + CFC rules |

A case may be multiple types simultaneously (e.g., a freelancer who relocated AND has foreign clients = Type A + Type B). Identify all applicable types.

### Step 3 — Load relevant country skills

For each jurisdiction identified in Step 1, determine which domain skills are needed:

1. **Tax** — income tax / corporate tax skill for the country
2. **Bookkeeping** — chart of accounts, transaction classification
3. **Payroll** — if employees or the user is employed there
4. **VAT/GST** — if supplies cross that border
5. **E-invoicing** — if the country mandates electronic invoicing
6. **Financial statements** — if filing obligations exist there
7. **Transfer pricing** — if related-party transactions cross that border

Load ONLY the skills that are relevant to the scenario type(s) identified in Step 2. Do not load all seven domains for every country — load what the case requires.

### Step 4 — Determine tax residency

For each individual involved, determine their tax residency:

1. Apply the domestic residency rules of each claiming country (load from country skill)
2. If TWO countries claim residency → apply the treaty tie-breaker (load `oecd-model-treaty-defaults.md`, Article 4 cascade):
   - Permanent home available → if only in one country, resident there
   - Centre of vital interests → personal and economic ties
   - Habitual abode → where time is spent over an extended period
   - Nationality → citizenship as final determinant
   - Mutual Agreement Procedure → if all above fail
3. Apply the 183-day test specific to each country (some use calendar year, some fiscal year, some rolling 12 months)
4. Document the conclusion with supporting facts

**If residency is genuinely ambiguous after applying the cascade, apply the conservative default: assume resident in BOTH countries.** This maximizes obligations; the reviewer can reduce.

### Step 5 — Assess PE risk in each non-resident country

For each country where the user or their entity is NOT tax-resident but has activity:

1. Load `permanent-establishment-risk.md`
2. Apply the three-part test: fixed place + permanence + business carried on
3. Check for agent PE (authority to conclude contracts)
4. Check for service PE if UN-model treaty applies (90-day or 183-day threshold)
5. Check the 2025 OECD update on remote work PE (< 50% working time from a location generally not a PE)
6. Classify risk: None / Low / Medium / High / Triggered

**If PE risk is Medium or higher, flag it prominently in the compliance map.** Do not attempt profit attribution — that is T3.

### Step 6 — Determine VAT/GST treatment for cross-border supplies

For each supply that crosses a border:

1. Classify the supply: goods vs services
2. For **goods**: determine origin country, destination country, whether intra-EU (zero-rated ICS) or export (zero-rated) or import (import VAT)
3. For **services**: determine place of supply using the B2B/B2C rules:
   - B2B services → generally taxable where customer is established (reverse charge)
   - B2C services → generally taxable where supplier is established (exceptions for digital services, real estate, transport)
4. Determine who accounts for VAT (supplier charges, customer reverse-charges, or import VAT at border)
5. Identify registration obligations (does the supplier need to register for VAT in the destination country?)

**Conservative default for place of supply when uncertain: assume destination principle (tax where customer is).** This maximizes the supplier's obligations.

### Step 7 — Determine withholding tax exposure

For each cross-border payment:

1. Load `withholding-tax-matrix.md`
2. Identify the source country (payer's country) and residence country (payee's country)
3. Classify the payment: services / royalties / interest / dividends
4. Look up domestic WHT rate in source country
5. Look up treaty rate (if treaty exists between the pair)
6. Determine whether treaty benefits can be claimed (CoR available? Forms filed?)
7. If EU → check whether Parent-Subsidiary Directive or Interest & Royalties Directive eliminates WHT

**Conservative default: assume domestic WHT rate applies.** Treaty relief is claimed separately and requires documentation.

### Step 8 — Determine social security obligations

For each individual working across borders:

1. If all countries are EU/EEA/Switzerland → load `eu-social-security-coordination.md`, apply Regulation 883/2004:
   - Single-state worker: lex loci laboris (country where work is performed)
   - Posted worker: home country continues (A1 certificate, max 24 months)
   - Multi-state worker: 25% substantial activity test → residence country if ≥ 25% there
2. If EU + UK → apply TCA Protocol on Social Security Coordination (similar rules)
3. If non-EU bilateral → check whether a totalization agreement exists between the pair
4. If no agreement → risk of double contribution (flag prominently)

**Conservative default: if SS coordination is unclear, assume obligation to contribute in BOTH countries.** The reviewer can reduce based on applicable agreement.

### Step 9 — Identify transfer pricing requirements

If related-party cross-border transactions exist (intercompany services, management fees, IP licensing, loans):

1. Determine whether the transaction exceeds documentation thresholds in either country
2. Identify the appropriate transfer pricing method (CUP, cost-plus, TNMM, profit split)
3. Check whether a Local File and/or Master File is required
4. Check Country-by-Country Reporting (CbCR) thresholds (€750M consolidated revenue)
5. Flag any transaction where the pricing appears non-arm's-length

**If the user has intercompany transactions but no transfer pricing documentation → flag as HIGH risk in the compliance map.**

### Step 10 — Produce consolidated cross-border compliance map

Assemble all findings from Steps 4–9 into a single, structured output (format specified in Section 3).

---

## Section 3 — The compliance map output

The cross-border compliance map is the primary deliverable of this skill. It consists of five components:

### Component 1 — Country-by-country obligation matrix

| Country | Tax Residency | Income Tax Filing | VAT/GST Filing | Payroll Obligation | SS Contributions | E-invoicing | Financial Statements |
|---------|--------------|-------------------|----------------|-------------------|-----------------|-------------|---------------------|
| [country] | Resident / Non-resident / Treaty tie-breaker needed | Yes (form) / No / Conditional | Yes (form) / No / Registration needed | Yes / No | Yes (rate) / No / Covered by other country | Required / Not required | Required / Not required |

One row per country. Every cell must be filled with a definitive answer or an explicit "NEEDS REVIEWER INPUT."

### Component 2 — Double taxation relief summary

For each income type that is taxed in more than one country:

| Income Type | Taxed In | Taxed In | Relief Method | Treaty Article | Action Required |
|-------------|----------|----------|---------------|---------------|-----------------|
| Consulting fees | DE (residence) | IN (source, 10% WHT) | Credit method (Art 23B) | India-Germany DTA Art 23 | Claim FTC in Germany; obtain Indian TRC |

### Component 3 — Unified filing calendar

| Obligation | Country | Form / Return | Period | Deadline | Frequency |
|-----------|---------|---------------|--------|----------|-----------|
| Income tax | DE | ESt | Annual | 31 July (with advisor: 28 Feb following year) | Annual |
| VAT return | DE | UStVA | Monthly/Quarterly | 10th of following month | Monthly |
| WHT refund claim | IN | Form 10F | Per payment | Within 5 years | As needed |

All deadlines in one place, sorted chronologically. Flag any deadlines within 30 days as URGENT.

### Component 4 — Risk flags

Categorize all identified risks:

| Priority | Risk | Country | Impact | Mitigation |
|----------|------|---------|--------|-----------|
| HIGH | PE risk — 4 months on-site at client | NL | Corporate tax filing + VAT registration | Limit days, remove dedicated desk |
| HIGH | No transfer pricing documentation | DE-IE | Adjustment risk on €200K intercompany fee | Prepare benchmarking study |
| MEDIUM | WHT not claimed via treaty | IN | 10% overclaim, €3,000 recoverable | File Form 10F with CoR |
| LOW | SS coordination unclear for 2-week trip | FR | Minimal contribution risk | Obtain A1 certificate |

### Component 5 — Reviewer brief for cross-border specialist

A narrative summary (similar to the VAT reviewer brief format) containing:

- One-paragraph situation summary
- Key determination made (residency, PE, applicable SS legislation)
- Highest-priority items requiring human verification
- Documents the reviewer should request from the client
- Conservative defaults applied and where the reviewer can reduce obligations
- Refusal triggers checked and cleared

---

## Section 4 — Coordination rules (how domains interact across borders)

### Bookkeeping coordination

- **Primary chart of accounts**: Use the chart of the tax-residence country (where the main entity files)
- **Multi-entity**: Each entity keeps its own books per local GAAP; consolidated at parent level
- **Intercompany eliminations**: Transactions between related entities in different countries must be eliminated on consolidation
- **Currency**: Each entity books in local functional currency; convert at transaction-date rate for P&L, closing rate for balance sheet
- **Cross-border transactions**: Book in the entity that bears the economic risk; ensure both sides record consistently

### Payroll coordination

- **Which country's payroll system**: The country where the employee is subject to social security (determined in Step 8)
- **EU workers**: Regulation 883/2004 determines the single applicable legislation; employer registers with that country's authority
- **Posted workers (EU)**: Home country payroll continues; A1 certificate proves exemption in host country (max 24 months)
- **Non-EU bilateral**: Check totalization agreement for which country gets contributions
- **No agreement**: Employee may need payroll in both countries; flag for specialist
- **Remote workers**: The country where work is physically performed generally claims payroll obligations

### E-invoicing coordination

- **Domestic supplies**: Use the format of the country where the supply is taxable
- **Intra-EU B2B services (reverse charge)**: Supplier issues invoice WITHOUT local VAT; no e-invoicing mandate applies to the reverse-charge invoice in most EU countries (but check Italy SDI for domestic supplies)
- **Cross-border goods (intra-EU)**: Invoice in supplier's format; buyer self-accounts in their system
- **Export to non-EU**: Use supplier's country format (or no mandate — exports are zero-rated)
- **Country-specific mandates override**: If a country mandates e-invoicing for ALL invoices (Italy, India, Saudi Arabia), comply with that mandate regardless of cross-border nature

### Transfer pricing coordination

- **When required**: Any transaction between related parties (≥ 25% ownership or effective control) that crosses a border
- **Documentation**: Prepare Local File in each country where a related entity exists; Master File at group level
- **Methods**: Apply the OECD Transfer Pricing Guidelines (2022); choose the most appropriate method per transaction
- **Advance Pricing Agreements (APAs)**: For recurring high-value intercompany transactions, consider bilateral APA to eliminate adjustment risk
- **Safe harbours**: Some countries offer safe harbour rules for low-value-adding services (mark-up of 5% on costs, per OECD simplified approach)

### Financial statements coordination

- **Standalone vs consolidated**: Each entity files standalone statements per local GAAP; parent files consolidated if group exceeds size thresholds
- **GAAP conflicts**: When entities in different countries use different GAAP (e.g., HGB in Germany, UK GAAP in UK), consolidated statements use the parent's GAAP or IFRS
- **Audit requirements**: Check each country's audit threshold independently; an entity may require audit in one country but not another
- **Related-party disclosures**: All intercompany transactions must be disclosed in standalone statements of both entities
- **Consolidation exemptions**: Small groups may be exempt from consolidation in their parent state; check the size thresholds (total assets, revenue, employees) per country
- **Currency translation**: Use the closing rate for balance sheet items and average rate for P&L; translation differences go to equity reserves

### VAT/GST coordination across borders

| Supply type | VAT treatment | Registration trigger |
|-------------|--------------|---------------------|
| B2B services (general rule) | Reverse charge — customer accounts for VAT in their country | No registration for supplier in customer's country |
| B2C services (digital) | Taxable where customer is established (OSS/IOSS in EU) | Supplier registers for OSS in one EU state OR registers in each customer state |
| Intra-EU goods | Zero-rated supply + acquisition tax in destination | Supplier needs VAT ID in origin state; buyer self-accounts |
| Export of goods (to non-EU) | Zero-rated in origin country | Customs export documentation required |
| Import of goods (into EU) | Import VAT at point of entry (or deferred accounting) | Importer registers for VAT in import state (or uses fiscal representative) |
| Triangulation (A→B→C, goods ship A→C) | Simplification available in EU (no registration in transit country) | All three parties need valid VAT IDs; specific invoicing requirements |

### Income tax coordination

- **Worldwide vs territorial**: Residence countries generally tax worldwide income; source countries tax only locally-sourced income
- **Credit vs exemption**: The treaty between the pair determines whether the residence country gives a credit for foreign tax or exempts the foreign income (see OECD Art 23A/23B)
- **Foreign tax credit limitations**: Credits are usually limited to the residence-country tax attributable to the foreign income — excess credits may carry forward (country-specific)
- **CFC rules**: If a controlled foreign subsidiary is in a low-tax jurisdiction, the parent's country may tax the subsidiary's undistributed profits (ATAD in EU; Subpart F/GILTI in US; § 7-14 AStG in Germany)
- **Treaty override hierarchy**: Domestic law → treaty → EU directive (in EU). If a treaty is more generous than domestic law, the treaty applies. If an EU directive mandates relief, it applies regardless of the treaty.

### Formation and substance coordination

- **Substance requirements**: A company formed in Country X must have genuine economic substance there (employees, office, decision-making) or risk:
  - Being treated as tax-resident elsewhere (where management and control actually exercised)
  - CFC rules in the parent's jurisdiction attributing income
  - Denial of treaty benefits under LOB/PPT clauses
- **Director residency**: Many jurisdictions require at least one locally-resident director for substance
- **Board meetings**: Hold and minute board meetings in the formation country to support management-and-control claims
- **Bank accounts**: Primary operating account should be in the formation country
- **Economic nexus**: Revenue, customers, contracts, or assets should exist in the formation country

---

## Section 5 — Conservative defaults for cross-border cases

When information is ambiguous or incomplete, apply these defaults. They ALWAYS maximize the user's obligations. The reviewer can reduce; the reviewer cannot easily recover from an unreported liability.

| Ambiguity | Conservative Default | Rationale |
|-----------|---------------------|-----------|
| Residency unclear — two countries could claim | Assume resident in BOTH | File in both; reviewer determines which treaty tie-breaker applies |
| PE risk unclear — borderline presence | Flag PE risk as HIGH | Better to flag and have reviewer dismiss than to miss |
| WHT rate uncertain — treaty may or may not apply | Apply domestic (higher) rate | Treaty relief claimed separately with documentation |
| VAT place of supply uncertain | Assume destination principle | Tax where customer is; higher obligation on supplier |
| Social security — unclear which country | Assume obligation in BOTH | Double contribution flagged; reviewer applies coordination rules |
| Transfer pricing — no documentation exists | Flag as HIGH risk | Absence of documentation is itself a compliance failure |
| Treaty existence uncertain | Assume NO treaty | Apply domestic law; if treaty exists, it only reduces obligations |
| Beneficial ownership challenged | Assume treaty benefits denied | Conservative; reviewer can confirm beneficial ownership |
| Split-year treatment available | Assume full-year resident in BOTH | Conservative; reviewer can apply split-year rules |
| Exit tax triggered by relocation | Assume full deemed disposal | Deferral/exemptions applied by reviewer after review |
| Foreign income classification uncertain | Classify as taxable in BOTH states | Double-tax relief removes the duplication; failing to declare creates liability |
| SS coordination — multi-state test borderline | Assume both countries may claim | Flag for A1 determination by competent institution |
| Entity substance questionable | Assume CFC rules apply in parent state | Flag for substance review; CFC inclusion is the conservative default |
| Intercompany pricing below market | Flag as non-arm's-length | Transfer pricing adjustment risk is HIGH if documentation absent |
| Treaty benefit eligibility uncertain | Assume NOT eligible | Benefits are claimed affirmatively; absence of proof = no benefit |

### The conservative defaults principle — worked example

**Situation:** A German freelancer has a US client who pays $50,000 for consulting services. The freelancer visited the US client's office for 2 weeks during the year.

| Question | Conservative default | Actual answer (for reviewer) |
|----------|---------------------|------------------------------|
| Is the income taxable in Germany? | YES — German tax resident, worldwide income | Correct |
| Is the income taxable in the US? | Assume YES (unknown whether treaty applies properly) | Treaty Art 7 + no PE = NOT taxable in US. Reviewer can confirm. |
| Does the US apply WHT? | Assume domestic rate (30%) | US does NOT impose WHT on service fees — rate is 0% regardless |
| Does the 2-week visit create PE? | Flag LOW PE risk | 2 weeks is clearly no PE — reviewer dismisses |
| Is VAT applicable? | B2B reverse charge — no German VAT on invoice | Correct |

The conservative default ALWAYS errs toward more obligations. The reviewer then reduces based on facts and documentation. This approach ensures nothing is missed; it never under-reports.

---

## Section 6 — Self-checks (run before delivering the compliance map)

### Structural checks

**Check 1 — All jurisdictions covered.** Every country identified in Step 1 appears in the obligation matrix. No country silently dropped.

**Check 2 — No conflicting determinations.** If country A says "resident" and country B says "resident," the treaty tie-breaker is applied or both are flagged. Never deliver a map that says "resident in A" AND "non-resident in A" without explanation.

**Check 3 — Double taxation addressed.** Every income item taxed in two countries has an entry in the double-taxation relief summary. No double-taxed income is left without a relief mechanism identified.

**Check 4 — Filing calendar complete.** Every "Yes" in the obligation matrix has a corresponding entry in the filing calendar with a specific deadline.

**Check 5 — Risk flags populated.** At least one risk flag exists (if no risks found, the case probably does not need this skill — reconsider whether cross-border activation was correct).

### Domain interaction checks

**Check 6 — SS and payroll consistent.** The country identified for social security in Step 8 matches the country where payroll is processed. If they differ, document why.

**Check 7 — VAT and e-invoicing consistent.** If a supply is taxable in country X (per Step 6), the e-invoicing treatment uses country X's format requirements.

**Check 8 — Transfer pricing and bookkeeping consistent.** Intercompany transactions identified in Step 9 are recorded in both entities' books at the same arm's-length price.

**Check 9 — PE and income tax consistent.** If PE is flagged in country X, the obligation matrix shows an income tax filing requirement in country X.

**Check 10 — WHT and treaty relief consistent.** If WHT is applied at the domestic rate (conservative default), the double-taxation relief summary shows how the payee recovers via credit or refund.

### Conservative-default checks

**Check 11 — Every default disclosed.** Each conservative default applied is listed in the reviewer brief with the alternative treatment and its impact.

**Check 12 — No silent assumptions.** No cell in the obligation matrix says "No" without an explicit basis. If the basis is "no treaty, no filing obligation under domestic law," state it.

**Check 13 — Reviewer actions clear.** The reviewer brief contains specific actions (not vague "review this") — "verify A1 certificate obtained," "confirm days in NL < 183," "check India TRC validity."

### Refusal and escalation checks

**Check 14 — Complexity ceiling.** If the case involves more than 5 countries, more than 3 entities, or more than 2 scenario types simultaneously, flag for specialist escalation rather than attempting full resolution.

**Check 15 — No prohibited advice given.** Verify that no output contains treaty shopping suggestions, nominee arrangements, or structuring advice that lacks substance.

**Check 16 — Temporal consistency.** All tax rules, rates, and thresholds cited are current for the relevant tax year. If the user's situation spans multiple tax years (e.g., relocation mid-year), each year uses that year's rules.

**Check 17 — Document completeness.** The reviewer brief lists every document the user needs to obtain (CoR, A1 certificate, Form 10F, W-8BEN, etc.) with the issuing authority and approximate timeline.

**Check 18 — Cross-reference integrity.** Every reference to another skill (e.g., "see withholding-tax-matrix.md") corresponds to a real file that exists in the skill set. Do not reference non-existent skills.

---

## Section 7 — Refusals

This skill MUST refuse to proceed and escalate to a human specialist when any of the following are detected:

### Hard refusals (immediate stop)

| Code | Trigger | Refusal message |
|------|---------|-----------------|
| R-CB-1 | Treaty shopping / aggressive structuring | "This arrangement appears designed to access treaty benefits without genuine economic substance. I cannot advise on treaty shopping structures. Please consult a qualified international tax advisor." |
| R-CB-2 | Nominee arrangements without substance | "Nominee structures without genuine economic activity in the nominee jurisdiction are outside my scope. A qualified advisor must review substance requirements." |
| R-CB-3 | Tax evasion signals | "The described arrangement raises potential tax evasion concerns (unreported income, hidden accounts, deliberate non-filing). I cannot assist. Please consult a qualified advisor." |
| R-CB-4 | Sanctions-country transactions | "Transactions involving sanctioned jurisdictions (currently: Russia, Belarus, North Korea, Iran, Syria, and others per EU/US sanctions lists) require specialist legal review. I cannot advise." |
| R-CB-5 | CRS/FATCA avoidance | "Arrangements designed to circumvent Common Reporting Standard or FATCA obligations are illegal. I cannot advise." |
| R-CB-6 | Artificial profit shifting without substance | "Profit shifting to low-tax jurisdictions without corresponding economic activity and substance fails BEPS standards. I cannot advise on structures lacking substance." |
| R-CB-7 | DAC6 hallmark arrangement design | "I cannot help design arrangements that would trigger mandatory disclosure under DAC6. If an existing arrangement is reportable, I can flag the reporting obligation." |

### Soft escalations (proceed with flag)

| Code | Trigger | Action |
|------|---------|--------|
| R-CB-S1 | More than 5 jurisdictions | Proceed but flag: "This case involves [N] jurisdictions and exceeds typical complexity. Output is indicative only. Specialist review essential." |
| R-CB-S2 | Profit attribution to PE | Proceed but do NOT compute attribution. Flag: "PE profit attribution requires specialist analysis. Filing obligation flagged but quantum not computed." |
| R-CB-S3 | Exit tax computation | Flag the exit tax trigger but do NOT compute the tax liability. "Exit tax likely triggered by departure from [country]. Specialist computation required." |
| R-CB-S4 | Mutual Agreement Procedure needed | "Treaty tie-breaker cascade exhausted without resolution. MAP between competent authorities required (typically 24–36 months)." |

---

## Section 8 — How this skill interacts with other skills

### Loading hierarchy

```
global-router.md
  → (detects cross-border signal)
  → cross-border-workflow-base.md (THIS FILE)
      → country skills (loaded per Step 3)
      → cross-border specialist skills (loaded per scenario type):
          - tax-residency-planning.md (Type B, E)
          - permanent-establishment-risk.md (Type A, C, D, E)
          - withholding-tax-matrix.md (Type A, D)
          - eu-social-security-coordination.md (Type C, E — EU only)
          - eu-directives-cross-border.md (Type D — EU only)
          - oecd-model-treaty-defaults.md (all types — treaty interpretation)
```

### Scenario routing table

| Scenario Type | Skills loaded | Primary output |
|---------------|--------------|----------------|
| Type A (foreign clients) | Country tax skill(s) + WHT matrix + PE risk + OECD defaults | Obligation matrix + WHT relief map |
| Type B (relocation) | Residency planning + country tax skills (both countries) + OECD Art 4 | Residency determination + split-year filing plan |
| Type C (foreign employees) | EU SS coordination (if EU) + country payroll skills | SS determination + payroll registration guidance |
| Type D (multi-entity) | TP skills + EU directives + PE risk + country tax skills | TP documentation plan + PE risk map + consolidated compliance |
| Type E (digital nomad) | Residency planning + PE risk + SS coordination + OECD defaults | Residency establishment plan + PE avoidance guidance |
| Type F (foreign formation) | Country formation skill + EU directives (if EU) + OECD defaults | Formation checklist + substance requirements + CFC analysis |

### Conflict resolution

- **If two country skills conflict on the same fact**: the country whose domestic law governs that fact wins (e.g., source country determines domestic WHT rate)
- **If a country skill and a cross-border skill conflict**: the cross-border skill wins on treaty/coordination matters; the country skill wins on domestic implementation
- **If this orchestrator and a country skill specify different workflow steps**: follow this orchestrator's Steps 1–10 for the overall case; defer to the country skill's workflow for country-specific deliverables within each step

### Output ownership

- This skill owns: the compliance map (Section 3), the unified filing calendar, the risk flags, the cross-border reviewer brief
- Country skills own: individual country returns, country-specific workbooks, country-specific reviewer briefs
- Both produce outputs — this skill's output is the coordination layer that ties them together

---

## Section 9 — Reference material

### Validation status

This file is v1.0 of `cross-border-workflow-base`, drafted May 2026 as part of the OpenAccountants multi-jurisdiction orchestration layer. It has not yet been validated against real multi-country cases.

### Known gaps

1. The 10-step workflow has not been stress-tested against cases with more than 3 countries simultaneously.
2. Transfer pricing documentation thresholds vary significantly by country and are not fully captured here — they come from individual country skills.
3. The conservative defaults assume bilateral cases; multilateral cases (3+ countries claiming the same income) may need different treatment.
4. Social security coordination for non-EU cases relies on bilateral totalization agreements which this skill does not contain — it only flags the need and defers to country-specific bilateral agreement content.
5. The 2025 OECD update on remote work PE is in the Commentary, not the Model Articles themselves; many existing treaties have not been updated.

### Test suite

#### Test 1 — Type A: German freelancer with US and UK clients

**Input:** German tax resident freelancer invoices US clients ($80K) and UK clients (£30K). Works 100% from home in Berlin. No travel abroad.

**Expected output:**
- Residency: Germany only
- PE risk: None (pure remote, no travel)
- WHT: US 0% (no US WHT on service fees); UK 0% (no UK WHT on service fees)
- VAT: B2B reverse charge on all invoices (no German VAT charged; clients account in their countries under their rules)
- SS: Germany only (single-state worker, lex loci laboris)
- Filing: German income tax (ESt) on worldwide income; German VAT return (services reported in Kz 45)
- Risk flags: None

#### Test 2 — Type B: UK resident relocating to Portugal mid-year

**Input:** UK resident moves to Portugal on 1 July. Continues freelancing for UK clients. No return to UK planned.

**Expected output:**
- Residency: UK for Apr 6 – Jun 30 (split-year SRT Case 4); Portugal from Jul 1 (183+ days if stays)
- PE risk: None in UK (no fixed place, no agent)
- WHT: UK does not impose WHT on service fees; Portugal does not impose WHT on inbound services
- VAT: UK VAT deregistration if below threshold; Portuguese VAT registration if above PT threshold
- SS: UK NIC until departure; Portuguese SS from registration date
- Filing: UK SA (split-year treatment claimed); Portuguese IRS for Jul-Dec
- Exit tax: UK has no general exit tax on individuals (only certain trusts)
- Risk flags: MEDIUM — ensure UK SRT is properly met for split-year; obtain Portuguese NIF and register with SS

#### Test 3 — Type C: Dutch company with remote developer in Poland

**Input:** Dutch BV hires a full-time developer in Poland. Developer works from home in Warsaw. No Dutch travel.

**Expected output:**
- Residency: Not applicable (company scenario, individual is Polish resident)
- PE risk: Generally NO PE for Dutch BV in Poland (employee working from home does not usually create PE for employer — 2025 OECD Commentary)
- WHT: N/A (salary, not cross-border payment subject to WHT)
- VAT: N/A (employment, not supply of services)
- SS: Poland — lex loci laboris (Art 11(3)(a) of Reg 883/2004). Worker performs all activity in Poland → Polish ZUS applies
- Payroll: Dutch employer must register with Polish ZUS as foreign employer, or use payroll provider / employer-of-record
- Filing: Polish PIT for employee; Dutch BV reports employment costs in Dutch accounts
- Risk flags: MEDIUM — Dutch BV must register as employer in Poland or use EoR; failure to register = non-compliance

#### Test 4 — Type D: Irish subsidiary paying management fees to German parent

**Input:** German GmbH owns 100% of Irish Ltd. Irish Ltd pays €200K annual management fee to German GmbH.

**Expected output:**
- WHT: Ireland does not impose WHT on service fees; Interest & Royalties Directive N/A (services not covered by IRD)
- Transfer pricing: Required — related-party cross-border transaction exceeds documentation thresholds in both countries. Local File needed in Ireland and Germany. Arm's-length pricing must be documented.
- PE risk: LOW for German GmbH in Ireland (management services from Germany, no fixed place in Ireland)
- VAT: Reverse charge — Irish Ltd self-accounts for Irish VAT on management services received from German GmbH
- Filing: German CIT includes management fee income; Irish CT return deducts fee (subject to TP documentation)
- Risk flags: HIGH — no TP documentation = adjustment risk. Revenue (Ireland) and Finanzamt (Germany) may challenge pricing.

### Change log

- **v1.0 (May 2026):** Initial draft. Ten-step workflow, six scenario types, five-component compliance map output, eighteen self-checks, seven hard refusals plus four soft escalations. Four test cases.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. Cross-border tax matters are inherently complex and fact-specific. All outputs must be reviewed and signed off by a qualified international tax professional before filing or acting upon.
