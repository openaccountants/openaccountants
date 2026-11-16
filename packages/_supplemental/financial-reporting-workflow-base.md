---
name: financial-reporting-workflow-base
description: Foundation workflow base for financial-reporting (US GAAP and IFRS) content skills. Contains the universal runbook, the two-layer output contract (reference layer + executable computation layer), the journal-entry format, the dual-standard convention, the AUDIT FLASH POINT marker convention, conservative-default principle, the structured question form, and the universal self-checks. This skill provides workflow architecture only  -  it contains no standard-specific recognition or measurement content. It MUST be loaded alongside a topic content skill (e.g. us-gaap-asc606-revenue, ifrs15-revenue) that provides the actual recognition, measurement, presentation, and disclosure rules. This base is the foundation every financial-reporting content skill loads on top of.
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
standard: US GAAP (ASC) and IFRS Accounting Standards routing and workflow
effective_date: 2026-11-14
source_checked: 2026-11-14
type: router
last_updated: 2026-11-16
category: financial-reporting
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-reporting
---

# Financial Reporting Workflow Base

## Scope

This is the shared runbook for the OpenAccountants US GAAP / IFRS content skills. Load it with the financial-reporting router and the applicable topic edition. It specifies working-paper structure, evidence intake, citation traces, journal format, judgement escalation and checks. It does not supply its own recognition/measurement rules or produce accounting without a supported topic.

The intended preparer is a controller, financial accountant, audit associate or other qualified preparer, with a credentialed reviewer responsible for the actual engagement. Outputs are draft working papers, entries and a reviewer brief. They are not filed financial statements, an audit/assurance opinion or sufficient audit evidence merely because this workflow was followed.

**Currency:** workflow version 0.2 is effective 14 November 2026; that is the frontmatter effective date for this revision, not an effective date shared by the standards. Topic content states its own governing standard, edition, amendment, transition and local adoption. Recheck those and the current library inventory for the reporting period; the former claim that the base "does not expire" is not a currency control.

### Quick reference

| Stage | Required outcome |
|---|---|
| Before computation | Evidenced reporting basis, scope, documents, period and material missing facts |
| Reference layer | Applicable rule and paragraph, with source/version/conditions |
| Executable layer | Supported conclusion and only the entries/disclosures actually required |
| Incomplete facts | Targeted intake, supported estimates where allowed, or explicit conditional scenarios; hold unsupported final conclusions |
| Dual reporting | Separate supported runs and reconciliation; missing edition is a gap |
| Delivery | Self-checks, reviewer brief and honest authorship/review status |

## Ask the client first

Use the router's framework/scope handoff and first read the supplied documents and existing material. Obtain unresolved facts in one structured block, grouped by the rule/decision they unlock: contract parties and substance; reporting entity/basis/period; dates; consideration and terms; estimates/valuation inputs; elections/transition; related parties and existing accounting; required deliverable. Avoid asking again for facts already evidenced.

For each missing item state its purpose, the decision affected and the document/evidence needed. Do not promise to replace an unknown decisive fact with a preferred accounting treatment. Topic-specific questions belong here, after the router's initial framework gate.

## The method, step by step

The following sections are internal output and evidence policy unless an accounting-standard paragraph is explicitly cited. The applicable standard controls recognition, measurement, presentation and disclosure; the template does not create an entry or disclosure requirement.

### Section 1 - The two-layer output contract

Produce both layers unless the user requests only one, while still making limitations and governing rules clear.

#### Layer A - Reference layer (the rules)

State the applicable topic's recognition, measurement, presentation and disclosure rules in your own words, with the governing paragraph, version, effective/transition conditions and primary source. A rule number alone is not evidence that its scope fits the facts. Examples of citation identifiers are ASC 606-10-25-1, IFRS 15.31, IAS 32.16 and ASC 842-10-15-3; these examples are not a statement that all four apply to a transaction. The reference layer answers what the applicable standard requires and where it is written.

Use the topic's supported decision path. IFRS scope interaction requires care: IFRS 15.5–7 coordinates other-standard separation/measurement, and IAS 32.2–4 distinguishes issuer presentation from measurement/disclosure and excludes specified arrangements. Sources: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html; https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html.

#### Layer B - Executable layer (the computation)

Apply the evidenced facts through Layer A and link each step to its rule. Deliver the supported recognition/measurement/classification conclusion; initial and subsequent entries where needed; amounts and captions affected in the primary statements; and the transaction's disclosure checklist. A classification-only or disclosure-only task may require no journal entry or subsequent schedule: say why rather than inventing one. No computation without a supported cited rule. Preserve uncertainty and identify which missing facts prevent a final result.

### Section 2 - The dual-standard convention

US GAAP and IFRS editions are separate skills where both actually exist. Confirm the current inventory; the earlier statement that every topic ships two files was incorrect. For example the IFRS presentation skill and its worked companion do not establish a US GAAP twin.

For confirmed local/group bases, run each supported applicable edition separately and show conclusions, entries, statement/disclosure effects and reconciliation side by side. Distinguish group conversion work from separate statutory statements. A divergence section is an editorial requirement for comparable supported editions, not a requirement imposed by an accounting standard. Where a comparison or edition is absent, state the missing coverage and obtain supported sources/review for that leg. Do not merge incompatible frameworks or infer a second full reporting set from a foreign parent.

### Section 3 - Journal entry format

Use this template for every entry actually required by the supported topic:

```text
[Date / period] - [Event description] - driving rule: [standard / paragraph]
Dr  [Account caption]   [amount]
Cr  [Account caption]   [amount]
Memo: [inputs, calculation and rule producing each amount]
Check: [total debits] = [total credits]
Statement mapping: [caption to asset, liability, equity, revenue, expense or OCI]
```

Include multiple debit/credit lines where the transaction requires them. Every entry must balance and state that check. Map the captions to actual statement lines; distinguish cash-flow presentation from recognition. For present values, allocations and estimates show the rate/term, standalone selling prices, fair values or other inputs, their source/date and the Layer A rule used.

Show applicable subsequent periods, including discount unwinding, amortisation, remeasurement and reclassification. If one is not applicable, say so. The template does not require all of these effects for every transaction, and it supplies no measurement assumptions of its own.

### Section 4 - AUDIT FLASH POINT convention

Use the marker as an **internal reviewer checklist**, with factual support for any specific external regulator/auditor assertion:

> **⚑ AUDIT FLASH POINT -** [judgement; why sensitive; applicable rule; evidence; alternatives; statement/disclosure effect; unresolved facts and reviewer decision]

Retain the original families: estimates/significant judgements; related-party and non-arm's-length terms; cut-off/period-end timing; principal versus agent and gross versus net; classification affecting EBITDA, leverage or current ratio; movements between profit/loss and OCI or between periods. These are prompts, not an assertion that every item is actively challenged by SEC, FRC or ESMA. Surface each triggered point in the reviewer brief.

Disclosure does not cure an incorrect treatment or missing evidence. For SEC filings, Regulation S-X 4-01(a)(1) expressly addresses non-GAAP statements despite disclosure; this does not make the base a substitute for engagement-specific SEC requirements. Source: https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.4-01.

### Section 5 - Conservative-default principle: evidence and neutral judgement

Preserve caution as a workflow control, replacing the former "harder to challenge / easier to unwind" accounting shortcut. If a decisive fact is missing, obtain evidence or stop the unsupported final conclusion. A permitted estimate can be prepared using the governing standard's required method and support; a conditional scenario must state its assumptions, effect and facts that would change it. Do not silently choose favourable or unfavourable accounting.

For IFRS, IAS 8.7–12 requires the applicable standard and, only where necessary, its policy hierarchy; neutrality/prudence is not deliberate overstatement or understatement. The Conceptual Framework 2.12–2.19 explains the principle and does not override a standard. Sources: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias8.html; https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/cf.html. These are scoped IFRS anchors; the actual US GAAP topic and authoritative Codification must govern the US leg.

An instruction to take an "aggressive" position and a named reviewer cannot authorize noncompliance. Where a standard permits an option or significant judgement, record the lawful alternatives, evidence, selected policy and responsible reviewer. Escalate an unsupported requested result; never treat client preference as the governing rule.

### Section 6 - Structured intake (the question form)

Ask unresolved material facts together, not piecemeal. Example:

> "To apply [topic] under [basis/period], I still need [fact/document], used in [step/rule]. If unavailable, [specific conclusion] remains open; I can show [clearly conditional scenario] if useful. Any estimate must meet [governing rule]."

Group by the Layer A decision. State evidence already read and avoid repeating it. The original proposed automatic conservative assumption is replaced by this transparent limitation/estimate route; no essential fact is guessed.

### Section 7 - Universal self-checks

- [ ] Both requested layers produced; every executable step traces to an applicable reference rule.
- [ ] Every required journal entry balances, with total debits/credits shown.
- [ ] Every caption maps to a primary-statement line; no fabricated entry for a no-entry task.
- [ ] Applicable subsequent periods shown, or not-applicable reason stated.
- [ ] Every figure traces to an evidenced input or rule; no unsourced numbers.
- [ ] Standard edition, effective date/transition and local adoption match the reporting basis/period.
- [ ] Each confirmed dual basis has a separate supported run; divergence/reconciliation and missing coverage recorded.
- [ ] Every triggered AUDIT FLASH POINT appears in the reviewer brief.
- [ ] Missing facts, supported estimates and conditional assumptions are explicit; no unsupported conservative/aggressive accounting default.
- [ ] Transaction disclosure checklist produced with references, or not-applicable reason.
- [ ] Authorship/source-check/independent-review/attestation status described accurately; engagement reviewer sign-off remains separate.

### Section 8 - Output specification

Deliver in this order, marking a part not applicable where justified:

1. **Conclusion:** supported outcome, framework/period and driving rule; if incomplete, say which conclusion cannot yet be reached.
2. **Reference-layer trace:** decision path, conditions and citations.
3. **Journal entries:** Section 3 initial/subsequent entries and calculations where required.
4. **Statement impact:** balance sheet, profit/loss, OCI, cash flow and relevant metrics, without inventing effects.
5. **Disclosure checklist:** triggered requirements with paragraph references.
6. **Reviewer brief:** judgements, all triggered flash points, estimates/conditional assumptions, lawful options, missing facts/coverage and decisions the qualified reviewer must clear.
7. **Divergence note:** supported differences and reconciliation for relevant confirmed dual bases; otherwise state the limited comparison.

### Section 9 - Verification status and disclaimer

Describe who authored, which sources were checked, whether an independent source review occurred, and any actual accountant attestation separately. Neither the tier value nor an AI check proves human sign-off. This workflow is Not yet approved. Do not reuse the former two-label quality-tier definitions as evidence of professional review. A topic's own current verified status must be read from its actual published record, not inferred here.

These skills provide computational and interpretive reference material. They are not an audit, an assurance engagement or a substitute for professional judgement. Recognition, measurement and disclosure often turn on entity-specific facts and significant judgement. Have the actual output reviewed and signed by a qualified accountant before incorporating it into financial statements relied on by third parties; an independent source-reading record is not that engagement sign-off.

## When to refuse or refer

Refuse an unsupported final conclusion when the framework, governing scope, decisive facts or required source/edition is missing. Preserve a supported bounded portion and explicit conditional outcomes where useful. Refer uncovered standards, complex interactions or requested noncompliant treatments; neither cautious wording, disclosure nor reviewer instruction cures missing support. Do not compute from this base alone or fabricate entries, rates or cases for template completeness.

## Sources

Workflow format, intake, checklist and review markers are internal policy. The actual primary scopes below support the external accounting boundaries, with no full-standard review or complete topic approval implied.

| Official source | Actual read scope | Read date |
|---|---|---|
| https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias8.html | Read for paragraphs 7–12, applicable-standard/policy hierarchy, neutrality/prudence and guidance authority; future IFRS 18 consequential relocations are not presumed current | 2026-11-14 |
| https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/cf.html | Read for status/purpose and paragraphs 2.12–2.19, faithful representation, neutrality and prudence; Framework does not override standards | 2026-11-14 |
| https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html | Read for paragraphs 5–8, scope and other-standard separation/measurement priorities | 2026-11-14 |
| https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html | Read for paragraphs 2–4, issuer presentation versus IFRS 9/7 and scope exclusions | 2026-11-14 |
| https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.4-01 | Read for 17 CFR 210.4-01(a)(1)–(2) and neighboring display provisions; disclosure does not cure non-GAAP preparation | 2026-11-14 |
| https://storage.fasb.org/ASU%202021-08.pdf | Read for official ASU frontmatter and printed pages 6–10: authoritative Codification versus explanatory update and scope-specific amendments; no full current ASC treatment asserted | 2026-11-14 |

Not yet confirmed: entity-specific reporting basis, adoption/early application and transition; any actual transaction evidence not provided; uncovered topic rules/current live Codification text beyond the scoped amendments; the former broad claim that every listed flash point is actively challenged by SEC/FRC/ESMA; and a parallel edition or divergence conclusion where coverage is absent. Do not use these as accounting instructions.
