---
name: financial-reporting-router
description: Entry point for the OpenAccountants financial-reporting (US GAAP / IFRS) skill library. ALWAYS load this skill first when a user asks how to account for, recognise, measure, classify, or disclose a transaction under US GAAP or IFRS  -  e.g. "how do I book this contract", "is this a lease", "debt or equity", "how do I account for this acquisition", "revenue recognition for...", "what's the journal entry for...". The router does not compute anything. It (1) establishes the entity's reporting framework, (2) identifies which accounting standard(s) the transaction touches, (3) gates out transactions whose governing standard the library does not yet cover, (4) sequences the topic skills when more than one applies, and (5) hands off to the financial-reporting-workflow-base plus the correct topic content skill(s). Every topic skill (revenue, leases, debt vs. equity, business combinations) assumes this routing step has happened first.
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
standard: US GAAP (ASC) and IFRS Accounting Standards routing and workflow
effective_date: 2026-11-14
source_checked: 2026-11-14
type: router
last_updated: 2026-11-14
category: financial-reporting
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-reporting
---

# Financial Reporting Router

## Scope

The entry point for the OpenAccountants financial-reporting library: establish the basis of the particular statements, identify candidate standards, check related scope gaps, coordinate dependencies and hand off to `financial-reporting-workflow-base` plus the applicable topic skills. This router computes no recognition, measurement or journal entry. Routing can happen in the background, but the framework, coverage limits and proposed sequence must be clear to the user.

This is workflow version 0.2, effective 14 November 2026. The frontmatter effective date is this workflow revision's date, **not** a common effective date for every accounting standard. Each topic's applicable edition, amendments, transition and local endorsement must be established for the actual reporting period. US GAAP here means the relevant nongovernmental FASB framework, not every US governmental reporting framework.

### Quick reference

| Situation | Action |
|---|---|
| Framework evidenced | Select the actual applicable edition and local overlay |
| Framework unclear | Resolve the basis of preparation before topic computation |
| Covered topic matched | Still pass the adjacent-standard gate and dependency sequencing |
| Missing framework/topic coverage | Preserve the covered portion, label the unsupported portion and refer |
| Dual basis confirmed | Separate runs and reconciliation; do not assume every topic has two editions |

## Ask the client first

Read the provided statements, basis-of-preparation note, contracts and existing case material before asking. Establish the entity/reporting unit, jurisdiction, reporting period, statutory/group purpose, actual framework and local adoption or early-application facts. If the framework remains unclear, ask once:

> "Which framework applies to these statements: US GAAP, IASB-issued IFRS, locally adopted IFRS, or another basis? If there are local and group reporting requirements, what basis applies to each?"

Do not start the topic computation until that gate is resolved. Detailed transaction intake belongs to the workflow base after routing, not a second piecemeal interview here.

## The method, step by step

### Step 0: Establish the reporting framework

Signals are prompts to inspect evidence, not a substitute for the basis of preparation.

| Signal | Original example retained | Evidence gate and route | Official source |
|---|---|---|---|
| Explicit statement | "we report under IFRS", "US GAAP filer" | Confirm exact framework, reporting set, edition and period; distinguish IASB-issued, locally adopted and other bases | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html; https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.4-01 |
| SEC registrant / US domestic filer | "10-K", "Form S-1", "SEC" | Determine domestic versus foreign private issuer and applicable filing basis. SEC alone does not prove US GAAP; foreign private issuers can use IASB-issued IFRS under the rule | https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.4-01 |
| Local framework / IFRS jurisdiction | EU-listed, UK, Australia, most of Asia/Africa | Do not infer full IFRS from geography. EU regulated-market consolidated-account rules use adopted standards with national options; UK FRS 102 and Australian simplified disclosures illustrate different bases. The broad Asia/Africa inference remains unconfirmed | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02002R1606-20080410; https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/; https://standards.aasb.gov.au/int-2-dec-2021 |
| US private company | "GAAP", "ASC", "FASB", US-based, no IFRS mention | Confirm the actual nongovernmental reporting basis; US location/private status alone does not establish it | https://storage.fasb.org/ASU%202021-08.pdf |
| Parent / subsidiary mismatch | "US sub of a German group", "we file local + group" | Confirm each required basis and whether separate statements, group conversion working papers or another deliverable is needed. Do not infer two full reporting sets solely from group geography | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02002R1606-20080410; https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.4-01 |

#### Dual reporters

For confirmed US GAAP and IFRS requirements, load the actual available applicable editions, run the topic workflow separately and show supported differences and reconciliation side by side. A subsidiary conversion schedule is not automatically a second complete set of financial statements. Check the topic's divergence section; where a required edition or comparison is missing, record it as unsupported coverage instead of fabricating a parallel answer. For another local basis, obtain its own supported skill/primary source before computing that leg.

### Step 1: Identify the standard(s) the transaction touches

This is a candidate navigation index, not clearance that a transaction is inside the named standard. Test the loaded topic's own scope and period first.

| Signal in the fact pattern | Candidate topic | Skill (US GAAP / IFRS) |
|---|---|---|
| Sale of goods/services, customer contract, performance obligations, variable consideration, licences, bundled deliverables, revenue timing | Revenue | `us-gaap-asc606-revenue` / `ifrs15-revenue` |
| Right to use an asset, rent/hire/charter, embedded lease, lessor/lessee, sale-and-leaseback | Leases | `us-gaap-asc842-leases` / `ifrs16-leases` |
| Preferred/redeemable shares, warrants, convertible notes, puttable instruments, debt or equity | Issuer classification, subject to scope | `us-gaap-debt-vs-equity` / `ias32-debt-vs-equity` |
| Obtaining control of a business, merger, purchase-price allocation, goodwill, bargain purchase, contingent consideration | Business combinations, after business/control/scope tests | `us-gaap-asc805-business-combinations` / `ifrs3-business-combinations` |

All matches proceed through **Step 2 and Step 3** before handoff. No match also proceeds to Step 2. A familiar word does not bypass adjacent-standard dependencies. Official scope anchors: IFRS 15.5–7 https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html, IFRS 16.3–12 https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html, IAS 32.2–4 https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html, IFRS 3.2–3 https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html. US topic scope must be checked in the applicable Codification/topic skill; the limited official amendments read here do not clear its full current text.

### Step 2: Scope gate - what this library does NOT cover yet

Read the actual available inventory at handoff. The following are non-exhaustive referral pointers, **not** independently verified recognition/measurement rules for those topics.

| If the user actually needs... | Candidate governing standard / coverage boundary | What to say |
|---|---|---|
| Goodwill / asset impairment | ASC 350 / ASC 360; IAS 36 | Initial acquisition goodwill is not subsequent impairment; name the missing impairment coverage |
| Income tax accounting / deferred tax | ASC 740; IAS 12 | Flag the tax leg even when the main transaction has a covered skill |
| Financial instrument measurement / impairment / hedging | IFRS 9; ASC 326 / ASC 815 address credit loss / derivatives and hedging, with other ASC topics potentially relevant | Issuer debt/equity classification is not a complete measurement or hedge answer |
| Share-based payment | ASC 718; IFRS 2 | Refer the uncovered arrangement; do not force it into the instrument classifier |
| Inventory, PP&E or standalone intangibles | ASC 330/360/350; IAS 2/16/38 | Acquisition coverage does not establish subsequent or standalone treatment |
| Provisions / contingencies | ASC 450; IAS 37 | Keep any dependency visible rather than inventing treatment |
| Consolidation, equity method or JVs | ASC 810/323; IFRS 10/11, IAS 28 | Acquisition accounting is not ongoing group accounting |
| Foreign currency translation | ASC 830; IAS 21 | Name the unsupported translation leg |
| Primary statement presentation / cash-flow classification | ASC 205/230; IAS 1/7 or applicable IFRS 18 | There are existing `ifrs18-presentation` and `ifrs18-presentation-worked-examples` skills. Route only after actual applicability/local endorsement. Other presentation/cash-flow coverage remains a separate gate |

IFRS 18 applies for annual periods beginning on or after 1 January 2027, with earlier application permitted and disclosed; local adoption must also be checked. Merely appearing in an issued edition does not make future consequential changes current for every 2026 entity. Source: IFRS 18.C1 and Appendix D https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html. These existing presentation files are routing targets, not changed or reattested by this revision.

#### Out-of-scope message template

> "The supported part is [topic/framework/period]. [Adjacent topic] needs [standard/source] coverage that is missing here. I can prepare the supported part as a clearly bounded working paper and list the missing part for review; a complete conclusion depends on resolving it."

Never fabricate an uncovered treatment. Missing facts within a covered topic also do not authorize an unsupported final answer; follow the base's neutral evidence and conditional-scenario procedure.

### Step 3: Sequence when multiple topics apply

| Combined fact pattern | Handoff order / dependency | Why and source |
|---|---|---|
| Business combination including contracts/leases/instruments | Establish combination scope/acquisition context, then coordinate relevant topics **at acquisition** and subsequently | Acquisition rules contain recognition/measurement exceptions. Do not reset every item to fair value or defer every topic until after acquisition. IFRS 3.15–28B https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html; ASC 805 amendments including contract assets/liabilities under Topic 606: https://storage.fasb.org/ASU%202021-08.pdf |
| Sale-and-leaseback | Load revenue **and** leases for the transfer assessment, then follow the supported sale/failed-sale route | Lease-specific conditions participate in the sale test; a revenue-only decision followed later by leases can miss them. IFRS 16.98–103 https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html; ASC 842-40-25-1–5 amendment text https://storage.fasb.org/ASU%202016-02_Section%20A.pdf |
| Convertible / hybrid issued to fund or settle a contract | Identify issuer/holder, transaction scope, required separation and measurement priorities, then coordinate instruments and customer/lease topics | No universal independent-classification-first shortcut. IFRS 15.7 https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html; IAS 32.2–4 scope exclusions and IFRS 9/7 relationship https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html; unsupported IFRS 2/measurement legs remain referrals |
| Divergence-sensitive dual reporter | Run the supported dependency sequence separately under each confirmed basis | A shared order does not imply a shared measurement answer; do not merge the runs |

State the sequence before topic computation: "This touches [A] and [B]. I will first resolve [scope/dependency], then run [supported sequence], with [missing coverage] held open."

### Step 4: Handoff

1. Load `financial-reporting-workflow-base` for the shared output, journal, judgement and self-check contract.
2. Load the actual topic edition(s) selected from the evidenced framework. US GAAP and IFRS runs remain separate; missing editions remain named gaps.
3. Pass the resolved scope, dependency sequence, reporting period/adoption evidence, available documents, source versions and unresolved questions. Load all supported multi-topic dependencies.

Tell the user: "Loaded the workflow base and [topic/edition]. I will produce the supported conclusion, applicable initial/subsequent entries, statement impact, disclosure checklist and reviewer brief, after resolving the required facts." Then hand off detailed intake to the base. A disclosure-only/no-entry task must not acquire fabricated entries merely because the template lists them.

### Router self-checks

- [ ] Framework and reporting set established; unresolved framework stops computation.
- [ ] Every candidate and adjacent topic identified; a match did not bypass the scope gate.
- [ ] Uncovered items named and kept open.
- [ ] Multi-topic dependencies and order stated, including acquisition exceptions and joint sale-test inputs.
- [ ] Correct available editions selected; both supported bases handled where required.
- [ ] Workflow base and topic skills loaded together; dates/adoption checked.

### Routing checks

**Acquisition plus deferred tax:** A business-acquisition question matches the combination skill. It must still pass Step 2, which flags the uncovered income-tax leg, then Step 3 to coordinate acquisition-date dependencies. Handoff records that the complete acquisition conclusion is held open for the tax leg; this router books nothing.

**UK company with FRS 102 basis:** "UK" does not load full IFRS automatically. The evidenced local basis is outside the full-IFRS/US-GAAP topic run here; obtain the FRS 102 overlay or refer, preserving any separately confirmed group-IFRS conversion requirement. Source for the distinct basis: https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/. These are navigation checks, not monetary computation examples.

## When to refuse or refer

The original PROHIBITIONS remain: never compute/classify/book in the router; never load a topic without the base; never guess the framework; never improvise an uncovered standard; never collapse confirmed dual bases into one answer; never run multi-topic work without resolving its governing scope/dependencies. "Business combination first" means establish acquisition context and exceptions, not a universal fair-value baseline. "Sale test before leaseback entries" includes the lease-specific constraints during that test.

Stop an unsupported final conclusion when framework, key scope or required topic coverage is unresolved. A professional reviewer cannot authorize departure from the governing standard merely by instructing a preferred result.

## Disclaimer


This skill routes between computational guidance skills for US GAAP and IFRS. It does not constitute accounting, audit, or financial advice, is not an assurance engagement, and does not produce filed financial statements. Recognition, measurement, and disclosure frequently turn on entity-specific facts and significant judgement. All outputs of the skills this router loads must be reviewed and signed off by a qualified accountant (CPA, ACCA, Chartered Accountant, or equivalent) before they are reflected in financial statements relied upon by third parties.

## Sources

The tables/index are routing policy; the following actual primary reads support the external framework and dependency boundaries. Read date is the operative scope read, not simply a server response.

| Official source | Actual read scope | Read date |
|---|---|---|
| https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.4-01 | Read for 17 CFR 210.4-01(a)(1)–(2) and neighboring display provisions; current domestic/foreign issuer distinction | 2026-11-14 |
| https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02002R1606-20080410 | Read for Regulation 1606/2002 Articles 3–5 and neighboring adoption provisions; regulated-market consolidated scope and national options | 2026-11-14 |
| https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/ | Read for FRS 102 applicability/current-edition overview; a distinct framework, no substantive FRS 102 treatment asserted | 2026-11-14 |
| https://standards.aasb.gov.au/int-2-dec-2021 | Read for Comparison with IFRIC 2, Tier 1/Tier 2 and neighboring rubric; no general Australia-equals-full-IFRS inference | 2026-11-14 |
| https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html | Read for paragraphs 2–3, 15–28B and neighboring recognition/measurement exceptions; no acquisition calculation here | 2026-11-14 |
| https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html | Read for paragraphs 5–8 and neighboring scope, especially separation/measurement precedence in 7 | 2026-11-14 |
| https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html | Read for paragraphs 3–12 and 98–103: scope/lease identification and joint sale-and-leaseback dependency | 2026-11-14 |
| https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias32.html | Read for paragraphs 2–4: issuer perspective, relation to IFRS 9/7 and exclusions including share-based arrangements | 2026-11-14 |
| https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html | Read for C1–C3, Appendix D effective-date condition and neighboring scope; protected skill contents not re-reviewed | 2026-11-14 |
| https://storage.fasb.org/ASU%202021-08.pdf | Read for ASU 2021-08 printed pages 6–10 and frontmatter: ASC 805 recognition/measurement exceptions, customer-contract amendments, transition. ASU communicates amendments; Codification is authoritative | 2026-11-14 |
| https://storage.fasb.org/ASU%202016-02_Section%20A.pdf | Read for ASC 842-40-25-1–5 and neighbors in official ASU 2016-02 Section A; scoped sale-test counterexample, not full current ASC review | 2026-11-14 |

Not yet confirmed: the original broad "most of Asia/Africa" full-IFRS inference; entity-specific local adoption and statement basis; complete current ASC text beyond the scoped official amendments; any uncovered topic's substantive treatment; and a second edition/divergence comparison where the inventory lacks it. These are outside usable accounting instructions. The current source set does not attest every linked topic skill.
