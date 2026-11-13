---
name: statutory-audit-workflow-base
description: "Tier 1 workflow base for statutory audit skills. Covers the audit lifecycle — engagement acceptance, risk assessment, audit planning, evidence gathering, fieldwork, opinion formulation, reporting — applied to the International Standards on Auditing (ISA) as issued by the IAASB plus country overlays (US GAAS for public co's, UK FRC ISA(UK), Germany IDW PS, France NEP, Italy ISA-Italia). Workflow architecture only — no engagement-specific procedures, materiality benchmarks, or audit programs. MUST be loaded alongside a content skill that provides the country-specific audit threshold rules, regulator inspection regime, statutory deadlines, and any non-ISA local standards. Assumes a qualified statutory auditor (RA, CPA, CA, Wirtschaftsprüfer, commissaire aux comptes, revisore legale, etc.) signs the audit report. Does NOT cover: internal audit, regulatory audit (banking, insurance prudential), tax audit by tax authority, IT general controls testing methodology, or forensic audit."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
category: foundation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: audit-assurance
---

# Statutory Audit Workflow Base

## What this file is

This is the **Tier 1 workflow base** for statutory audit content skills. It does not contain country-specific audit rules. It contains:

- The audit lifecycle runbook aligned to ISA (IAASB)
- The country audit threshold matrix (when an audit is required)
- The engagement acceptance and continuance protocol
- The ISA risk assessment and significance-determination framework
- The reviewer-oriented audit file structure
- The opinion formulation decision tree
- The 21 self-checks
- The global refusal catalogue
- The slot contract for country statutory audit skills

**Every statutory audit skill MUST be loaded alongside this base.**

## Section 1 — Audit lifecycle (ISA-aligned)

### Phase 1 — Engagement acceptance / continuance (ISA 220, 220R, 210)

**Before accepting or continuing tests**  _(ISA 220, 220R, 210)_

| Test | Reference |
| --- | --- |
| Independence (firm-level + engagement team) | IESBA Code Part 4A; PCAOB Rule 3520; FRC ES 1; IDW PS 220 |
| Competence to perform the audit | ISA 220 ¶15 |
| Acceptance approval by appropriate partner | Firm policy; ISA 220 ¶16 |
| Engagement letter signed | ISA 210 ¶10 |
| Predecessor auditor communication | ISA 510 (initial engagements); communication with predecessor required |
| Audit fee not impaired (no contingent fees on the audit opinion) | IESBA Code 410 |

### Phase 2 — Risk assessment (ISA 315 (Revised 2019))

**[T1] Required activities:**
- Understand the entity, its environment, and its system of internal control
- Identify and assess Risks of Material Misstatement (RMM) at financial statement and assertion levels
- Determine significant risks
- Identify controls relevant to the audit

**[T1] Significant risks** receive enhanced procedures and cannot be addressed with substantive analytical procedures alone.

### Phase 3 — Audit plan and materiality (ISA 320, 330)

- **Overall materiality** — Overall materiality — judgment based on benchmark and percentage (commonly 5% of PBT, 0.5-1% of revenue, 1-2% of equity, 1-2% of total assets, depending on user emphasis)  _(ISA 320, 330)_
- **Performance materiality** — Performance materiality — typically 50-75% of overall materiality  _(ISA 320, 330)_
- **Specific materiality** — Specific materiality — for particular classes of transactions / accounts / disclosures requiring lower threshold (e.g., related parties, executive compensation)  _(ISA 320, 330)_
- **Clearly trivial threshold** — Clearly trivial threshold — typically 5% of performance materiality  _(ISA 320, 330)_

### Phase 4 — Fieldwork / procedures (ISA 330, 500, 501-540)

- **Audit evidence requirement** — Audit evidence must be sufficient (quantity) and appropriate (relevance + reliability). Per assertion (existence, completeness, valuation, rights/obligations, classification, presentation/disclosure, accuracy, cut-off), select procedures from the procedures table.  _(ISA 330, 500, 501-540)_

**Procedures and Types**  _(ISA 330, 500, 501-540)_

| Procedure | Type |
| --- | --- |
| Inspection of records or documents | Substantive / control |
| Inspection of tangible assets | Substantive (existence) |
| Observation | Control |
| Inquiry of management / others | Substantive / control / inquiry |
| External confirmation | Substantive (existence/valuation) |
| Recalculation | Substantive |
| Reperformance | Control |
| Analytical procedures | Substantive (when designed appropriately) |

- **ISA-required specific procedures** — Specific ISA-required procedures: - ISA 240 — fraud: testing journal entries, related party transactions, management override - ISA 250 — laws and regulations: inquiries, document inspection, legal letters - ISA 501 — inventory observation, litigation legal letters, segment information - ISA 540 (Revised) — accounting estimates (including ECL, pensions, goodwill, fair value) - ISA 550 — related party transactions - ISA 560 — subsequent events review through report date - ISA 570 — going concern (12 months from balance sheet date in most jurisdictions; 12 from report sign-off in some) - ISA 600 — group audits and component auditor reliance  _(ISA 240, 250, 501, 540, 550, 560, 570, 600)_

### Phase 5 — Completion (ISA 700-720)

- **Completion checklist** — Completion checklist: - Going concern assessment (ISA 570) - Subsequent events review (ISA 560) - Written representations from management (ISA 580) - Quality control review (ISA 220, 220R) - Engagement Quality Review (EQR) for PIE / listed audits (ISA 220R, ISQM 1) - Key Audit Matters (KAM) selection (ISA 701 — listed entities) / equivalent for unlisted in some jurisdictions - Audit opinion formulation (ISA 700, 705, 706) - Annual report or other information reading (ISA 720)  _(ISA 700-720)_

### Phase 6 — Reporting (ISA 700/705/706/701/710)

- **Opinion options** — Opinion options: - **Unmodified** — financial statements give a true and fair view - **Qualified** — material but not pervasive misstatement OR scope limitation - **Adverse** — material and pervasive misstatement - **Disclaimer** — material and pervasive scope limitation - **Emphasis of matter** — adds emphasis without modifying opinion (e.g., subsequent event after issuance) - **Other matter** — additional matters not addressed in financial statements - **Key Audit Matters** — significant matters in current period audit (listed and certain unlisted) - **Going concern paragraph** — material uncertainty paragraph or going concern KAM  _(ISA 700/705/706/701/710)_

### Phase 7 — Post-issuance (ISA 220R, ISQM 1)

- **Post-issuance activities** — - Engagement quality reviews - Firm monitoring and remediation - Inspections by regulators (PCAOB, FRC, AOB, etc.) - Subsequent discovery of facts (ISA 560 ¶14-17)  _(ISA 220R, ISQM 1)_

## Section 2 — When is a statutory audit required?

Each country sets size thresholds (typically two-of-three test on balance sheet total, revenue, employees) above which an audit is mandatory.

**Illustrative thresholds (2025)**  _(Illustrative thresholds (2025))_

| Country | Total assets | Net revenue | Employees | Notes |
| --- | --- | --- | --- | --- |
| **UK** | GBP 5.1m | GBP 10.2m | 50 | Two-of-three; PIEs/PLCs always audited |
| **Germany (BilanzRichtlinie umgesetzt §267 HGB)** | EUR 6m | EUR 12m | 50 | "Mittelgroße" company audited; "Kleine" exempt |
| **France** | EUR 5m | EUR 10m | 50 | Loi PACTE 2019 raised thresholds |
| **Italy** | EUR 5m | EUR 10m | 50 | art. 2477 CC |
| **Spain** | EUR 4m | EUR 8m | 50 | Plus de minimis tests |
| **Netherlands** | EUR 7.5m | EUR 15m | 50 | "Middelgroot" |
| **EU general (Accounting Directive 2013/34/EU as amended 2023)** | EUR 7.5m | EUR 15m | 50 | Raised by 25% in 2023 indexation; MS may modify |
| **Ireland** | EUR 7.5m | EUR 15m | 50 | Aligned EU |
| **Australia** | AUD 12.5m or grand-fund > 50 | AUD 25m | 50 | Various tests; large proprietary or grandfathered |
| **Canada** | Provincial CPCA / OBCA — most private companies opt out via unanimous shareholder waiver | n/a | n/a | Subject to public-company status |
| **United States** | No federal statutory audit for private companies | n/a | n/a | SEC: all listed companies. State LLC / corporation audit by election. |
| **India** | INR 100 crore (sales) or INR 50 crore (net profit) → 2017 audit thresholds; private cos with paid-up capital | n/a | n/a | Companies Act 2013 |
| **Japan** | JPY 500m capital OR JPY 20bn liabilities | n/a | n/a | Financial Instruments and Exchange Act for listed; Companies Act for large |
| **Brazil** | BRL 78m total assets | BRL 300m gross revenue | n/a | Listed always |
| **Singapore** | SGD 10m total assets | SGD 10m revenue | 50 | Two-of-three; Small Company Concept since 2014 |

- **PIE definition and requirements** — PIEs (Public Interest Entities — listed, banks, insurers): always audited, with additional partner rotation, audit firm rotation, and enhanced reporting (KAMs).

## Section 3 — Engagement structure

### 3.1 Roles

**Roles and Responsibilities**

| Role | Responsibility |
| --- | --- |
| Audit engagement partner | Overall accountability; signs the report (ISA 220) |
| Engagement Quality Reviewer (EQR) | Independent objective evaluation (ISA 220R, ISQM 1) — required for PIEs, recommended for higher-risk |
| Manager | Day-to-day engagement leadership |
| Senior / In-charge | Field execution |
| Staff | Detailed testing |
| Specialists | Tax, IT, valuation, actuarial — internal or external (ISA 620) |
| Group auditor (parent) | Overall group opinion; relies on component auditors per ISA 600 |
| Component auditor | Component audit work for inclusion in group audit |

### 3.2 Independence (IESBA Code Part 4A)

- **Threats and prohibitions** — Self-interest, self-review, advocacy, familiarity, intimidation threats must be evaluated. Specific prohibitions for PIEs: - Bookkeeping / accounting services - Internal audit outsourcing - Valuations relevant to the financial statements - Tax services involving advocacy - Certain corporate finance / advisory engagements - Rotation of engagement partner (typically 5 years on / 5 off; PIE rotation rules vary) - Audit firm rotation (EU mandatory rotation cap typically 10-24 years for PIEs)  _(IESBA Code Part 4A)_

## Section 4 — Reviewer brief (audit working paper file)

Every audit produces a file containing:

```
1. Engagement acceptance / continuance file
   - Independence declarations
   - Risk acceptance
   - Engagement letter
   - Predecessor communications

2. Risk assessment file
   - Entity understanding documentation
   - Industry / regulatory environment
   - Internal control walkthroughs and testing
   - Risk identification and significance matrix
   - Significant risks and response plan

3. Planning file
   - Materiality determination (overall, performance, specific, trivial)
   - Audit plan with timing and resources
   - Component auditor instructions (group audits)
   - Internal control reliance plan

4. Fieldwork file
   - By assertion: procedures performed and conclusions
   - Confirmations sent and received
   - Inventory observation working papers
   - Going concern assessment
   - Estimates testing (ECL, pensions, goodwill, fair value)
   - Related party identification and testing
   - Litigation legal letters and management responses
   - Subsequent events review

5. Completion file
   - Final analytical procedures
   - Management representation letter
   - Going concern conclusion
   - Subsequent events through report sign-off
   - Engagement quality review (EQR) for PIE / listed

6. Reporting file
   - Final financial statements signed by management
   - Audit opinion (with KAMs for listed)
   - Letter to those charged with governance / management letter
   - Audit committee communications (ISA 260, 265)
```

## Section 5 — Opinion formulation decision tree

```
Misstatement detected?
  No → Material uncertainty / scope limitation?
    No → Unmodified opinion
    Yes → Pervasive?
      No → Qualified opinion (scope limitation)
      Yes → Disclaimer of opinion
  Yes → Corrected by management?
    Yes → Unmodified opinion
    No → Material?
      No → Unmodified (track for clearly trivial threshold)
      Yes → Pervasive?
        No → Qualified opinion (disagreement)
        Yes → Adverse opinion

Going concern material uncertainty?
  Yes + Adequate disclosure → Unmodified + going concern paragraph
  Yes + Inadequate disclosure → Qualified or adverse depending on materiality/pervasiveness
```

## Section 6 — 21 self-checks

Before signing the opinion, verify:

1. [ ] Engagement acceptance / continuance documented and approved
2. [ ] Engagement letter signed before fieldwork
3. [ ] Independence — firm and engagement team — declared and threats assessed
4. [ ] Risk assessment per ISA 315 (Revised) — entity understanding, RMM, significant risks
5. [ ] Materiality — overall, performance, specific, trivial — determined and documented
6. [ ] Audit plan responsive to identified risks
7. [ ] Significant risks addressed with substantive procedures (analytical not alone sufficient)
8. [ ] Going concern assessment for at least 12 months from report date
9. [ ] Subsequent events review through report sign-off
10. [ ] Written representation letter from management received before report sign-off
11. [ ] Fraud risk assessment per ISA 240 with required journal entry testing
12. [ ] Estimates tested per ISA 540 (Revised)
13. [ ] Related parties identified and tested per ISA 550
14. [ ] Litigation legal letters obtained per ISA 501
15. [ ] Group audit — component auditor reliance documented per ISA 600
16. [ ] EQR review completed and reviewer concur for PIEs / required engagements
17. [ ] Annual report read and other information consistent with audited financial statements (ISA 720)
18. [ ] Communications to TCWG / management letter prepared
19. [ ] Opinion type confirmed via decision tree (Section 5)
20. [ ] KAMs identified and documented for listed entities (ISA 701)
21. [ ] Audit file assembled and archived per ISQM 1 and country regulations (typically 5+ years)

## Section 7 — Global refusal catalogue

**Global refusal catalogue**

| Refusal | Trigger |
| --- | --- |
| **R-AUDIT-1** | Independence cannot be established or threats cannot be reduced to acceptable level |
| **R-AUDIT-2** | Predecessor auditor will not communicate or hostile transition |
| **R-AUDIT-3** | Management refuses to provide written representations |
| **R-AUDIT-4** | Material misstatement detected and management refuses to correct |
| **R-AUDIT-5** | Limitation on scope imposed by management |
| **R-AUDIT-6** | Suspected fraud — escalate per firm fraud protocols and ISA 240 ¶42 |
| **R-AUDIT-7** | Suspected non-compliance with laws and regulations affecting financial statements — ISA 250 ¶27 escalation |
| **R-AUDIT-8** | Going concern material uncertainty with inadequate disclosure that management refuses to enhance |
| **R-AUDIT-9** | Component auditor refuses cooperation in group audit |
| **R-AUDIT-10** | Regulatory inspection finding against firm requires re-issuance of opinion |

- **R-AUDIT-1** — Independence cannot be established or threats cannot be reduced to acceptable level
- **R-AUDIT-2** — Predecessor auditor will not communicate or hostile transition
- **R-AUDIT-3** — Management refuses to provide written representations
- **R-AUDIT-4** — Material misstatement detected and management refuses to correct
- **R-AUDIT-5** — Limitation on scope imposed by management
- **R-AUDIT-6** — Suspected fraud — escalate per firm fraud protocols and ISA 240 ¶42
- **R-AUDIT-7** — Suspected non-compliance with laws and regulations affecting financial statements — ISA 250 ¶27 escalation
- **R-AUDIT-8** — Going concern material uncertainty with inadequate disclosure that management refuses to enhance
- **R-AUDIT-9** — Component auditor refuses cooperation in group audit
- **R-AUDIT-10** — Regulatory inspection finding against firm requires re-issuance of opinion

## Section 8 — Slot contract for country audit content skills

Every country statutory audit content skill must populate:

```
[REGULATOR]
- National audit regulator (FRC, PCAOB, AOB, H3C, etc.)
- Auditor qualification body (ICAEW, AICPA, etc.)
- Auditor licensing process

[STANDARDS]
- Auditing standards in force (ISA-IAASB, ISA(UK), GAAS-PCAOB, NEP, IDW PS, etc.)
- Reporting standards in force (IFRS-IASB, IFRS-EU, FRS 102, US GAAP, local)
- Required audit reporting language and structure

[THRESHOLDS]
- Statutory audit trigger thresholds (assets, revenue, employees)
- PIE definition and additional requirements
- Audit committee requirements
- Audit firm rotation requirements (PIEs)
- Engagement partner rotation requirements

[FILING]
- Filing deadline (annual return, financial statements, audit report)
- Public access to financial statements (Companies House, BR, RCS, BOE, etc.)
- Late filing penalties
- Format requirements (XBRL, Inline XBRL, ESEF for listed)

[OPINION]
- Required language and structure
- Local KAM / equivalents
- Director's responsibilities statement requirements
- Subsequent event treatment specifics

[ANCILLARY]
- Country-specific procedures (US §404 ICFR opinion; UK FRC ISA(UK) 240/700/701 specific paragraphs; France lettre d'affirmation specifics; etc.)
- Tax / payroll / VAT / pension auditor responsibilities (where audit-related)
- Related-party disclosure local rules

[CROSS-REFERENCES]
- IFRS / local GAAP reconciliation (this skill if dual reporting)
- Pillar Two — auditor responsibility for tax provision and disclosure
```

## Section 9 — Disclaimer

This workflow base produces working papers for audit engagement, not direct accounting or financial advice. Every audit opinion must be signed by a qualified statutory auditor in compliance with the local regulator's requirements.

The most up-to-date, verified version of this workflow base is maintained at [openaccountants.com](https://openaccountants.com).
