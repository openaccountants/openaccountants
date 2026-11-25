---
name: canada-transfer-pricing
description: Use this skill whenever asked about Canada transfer pricing rules, documentation requirements, or CRA transfer pricing compliance. Trigger on phrases like "transfer pricing Canada", "Canadian TP documentation", "CRA transfer pricing", "master file Canada", "local file Canada", "CbCR Canada", "APA Canada", "Section 247", "Form T106", "contemporaneous documentation Canada", or any question about intercompany pricing for Canadian entities.
version: 1.1
jurisdiction: CA
tax_year: 2025
tax_year_notes: Historical 2025 workpaper with separately identified older and later year-beginning regimes; no single current-year or artificial cross-year period is certified.
last_updated: 2026-11-25
source_checked: 2026-11-21
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: transfer-pricing
---

# Canada Transfer Pricing

## Canada Transfer Pricing Skill v1.1

This corrects the historical 2025 workpaper. Select the actual taxation-year beginning before applying an older or amended regime; not every 2025 return uses the later rule. **HOLD** blocks final use of an affected scope, deadline, penalty or relief outcome until its operative source and case inputs are established. A filing threshold is not a documentation exemption or deductible allowance.

## Rates and thresholds

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
That historical attribution does not approve this proposed correction. Unresolved scope, source and operative conditions are explicitly held below.

### Transfer Pricing

- **TP provision** — Section 247, ITA  _(ITA s.247; CRA — Transfer pricing — canada.ca)_
- **Arm's length standard** — ITA s.247(2)  _(ITA s.247(2))_
- **Recharacterization power** — The older two-part structure applies to years beginning on or before 4 November 2025; its recharacterization test also has the bona-fide-purpose/tax-benefit limb. Later years use the amended adjustment/arm's-length-conditions structure, which can still involve a different or no transaction. HOLD actual transaction conditions and applicable version. [older 247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html); [current 247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html); [CRA year boundary](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html).
- **Documentation threshold** — CAD $1M aggregate with all non-arm's length non-residents combined is the T106 FILING threshold — it is not an exemption from contemporaneous documentation under s.247(4)  _([ITA s.247(4); CRA — Transfer pricing memorandum TPM-09](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf))_
- **Timing** — Person's documentation-due date follows its filing-due date; partnership actual/hypothetical information-return timing is a separate definition and is held until bound. Subsequent-year material changes must be assessed. [247 definitions/(4)(a)-(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html).
- **Provision to CRA on request** — Paragraph 247(4)(c), not (b): older three-month period, later 30-day period for taxation years beginning after 4 November 2025, from the specified service of written request. Paragraph (b) concerns subsequent-year material changes. [older (4)(c)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html); [amended (4)(c)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html); [enacted boundary](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html).
- **Form T106** — More than CAD 1 million aggregate relevant transactions with all relevant non-residents combined; exactly 1 million does not pass that gate. HOLD actual reporting-person/partnership and business-related reportable-transaction scope; not every cross-border payment. [233.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.1.html); [form instructions](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf).
- **Form T106 deadline** — Person/partnership timing is in 233.1(2)/(3); (4) is the 1-million exception. Ordinary corporate six months, trust 90 days, individual 30 April and applicable self-employment extension (including the spouse branch) must be matched to actual facts; partnership timing is held. [233.1(2)-(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.1.html); [page 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf).
- **CbCR (Form RC4649)** — Section 233.8 is in Part XV, not Part XVIII. Apply the EUR 750-million group boundary using the immediately preceding fiscal year's consolidated revenue and the actual UPE/conditional Canadian constituent-entity/surrogate-parent branches. HOLD actual filing obligation. [233.8](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.8.html); [CRA guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4651/guidance-on-country-country-reporting-canada.html).
- **CbCR deadline** — General timing is 233.8(6), not (3): 12 months after reporting fiscal year-end, with the statutory systemic-failure notice/later-30-day branch where applicable. HOLD actual notice and date; not a universal extension. [233.8(6)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.8.html); [CRA timing](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4651/guidance-on-country-country-reporting-canada.html).
- **TP penalty threshold** — Lesser of $10M or 10% of gross revenue for taxation years beginning after November 4, 2025 (Budget 2025); previously the lesser of $5M or 10% of gross revenue  _([ITA s.247(3); Finance Canada draft legislation Aug 2025](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html))_
- **Penalty rate** — Apply 10% to the statutory 247(3)(a) amount when the applicable (3)(b) gate is exceeded; do not subtract the gate. HOLD actual defined capital/income adjustments, reasonable-efforts/qualifying-arrangement exclusions, permitted setoffs and statutory revenue. Ordinary gross netting is not certified. [247 definitions/(3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html); [older version](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html).
- **Reasonable efforts defence** — Statutory reasonable-efforts protection and documentation deeming must be applied to the actual defined amounts/arrangement. Records alone do not prove sufficient efforts or blanket immunity. [247(3)-(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html).
- **Documentation failure** — Deeming is in 247(4); 247(3)(b) is the penalty gate. Bind applicable preparation/content/material-change and written-request conditions before a result. [247(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html); [older (4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html).
- **Late T106** — $25/day, min $100, max $2,500  _(ITA s.162(7); CRA)_
- **Types** — Unilateral, Bilateral, Multilateral  _(CRA — Advance pricing arrangement — canada.ca; IC 94-4R)_
- **Duration** — Ordinary prospective APA term usually five years; HOLD the old fixed five-prior-year rollback maximum, which was not substantiated. Rollback depends on open-year/treaty/factual criteria, and unilateral rollback is excluded. [IC94-4R2 paragraph 36](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic94-4/international-transfer-pricing-advance-pricing.html); [TPM-11](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing/11.html).
- **Application fee** — None set out in IC94-4R2; travel costs for CRA officials are borne by the CRA, and the taxpayer pays its own travel and any independent expert (IC94-4R2)  _([CRA — IC 94-4R](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic94-4/international-transfer-pricing-advance-pricing.html))_
- **Processing time** — The CRA index read on 21 November 2026 linked the 2024 report: 13 completed bilateral/multilateral cases, mean 40.8 months acceptance-to-completion. This historical cohort is not a service guarantee or a current pending-case estimate. [report index](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-services/advance-pricing-arrangements.html); [2024 table](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-services/advance-pricing-arrangements/2024-apa-program-report.html).
- **Formal safe harbour?** — HOLD the unqualified nationwide/no-exception assertion. No blanket entitlement was established; actual exclusions and 247(4.1) prescribed simplification need separate binding. [247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html).
- **Low-value services** — HOLD the unsupported 5% cost-plus/Canadian acceptance claim; OECD guidance alone is not Canadian operative authority. No final markup is authorized.
- **Form T106 de minimis** — ≤ $1M aggregate: no filing required  _(ITA s.233.1)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Tax authority | Canada Revenue Agency (CRA) |
| Key TP legislation | Section 247, Income Tax Act (ITA) |
| Documentation | Subsection 247(4) ITA -- contemporaneous documentation |
| CbCR | Form RC4649; section 233.8 in Part XV. [ITA placement and scope](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.8.html) |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Currency | CAD |
| Documentation language | English or French |
| Skill version | 1.1; [version in frontmatter](https://github.com/openaccountants/openaccountants/blob/9b64e41478873276d303288b5c64d55af24175b0/skills/canada/canada-transfer-pricing.md#L4) |

## Section 2 -- Documentation Requirements

### 2.1 Contemporaneous Documentation (Section 247(4))

**Contemporaneous Documentation (Section 247(4))**  _(https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf)_

| Item | Detail |
| --- | --- |
| Required? | Bind actual section 247 scope; T106 filing does not create or limit its documentation duty. HOLD actual taxpayer/partnership, transactions and exclusions. [247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |
| Threshold | T106 filing: aggregate transactions > CAD 1 million with all non-arm's length non-residents combined (the documentation duty is not exempted below it) |
| Timing | By the applicable documentation-due date; person and partnership definitions differ. HOLD actual partnership timing; assess subsequent-year material-change records. [247 definitions/(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |
| Content | Retain six headings, but HOLD completeness under the actual statutory version: property/services, terms, participants, functions, data/method and economic assumptions require the full applicable descriptions, actual conduct, wider group context and method analysis. [older (4)(a)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html); [amended (4)(a)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |
| Provision to CRA | Applicable older three months / later 30 days under paragraph (4)(c), following specified written-request service; actual version/date required. [older](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html); [amended](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |

### 2.2 Form T106 -- Information Return

**Form T106 -- Information Return**  _(https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf)_

| Item | Detail |
| --- | --- |
| Required? | Relevant aggregate exceeds CAD 1 million, subject to actual reporting-person/partnership and business-related reportable-transaction definitions. HOLD actual scope. [233.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.1.html); [instructions](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf) |
| Filing deadline | Ordinary corporation six months; trust 90 days; individual 30 April or applicable self-employment/spouse extension. HOLD actual exceptions and partnership actual/hypothetical section-229 timing. Deadline provisions are 233.1(2)/(3). [statute](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.1.html); [page 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf) |
| Content | Summary of all non-arm's length transactions by non-resident party |

### 2.3 Master File / Local File

HOLD any categorical separate Master/Local File filing exemption: it was not established merely by the six documentation headings. CRA confirms Bill C-15 Royal Assent on 26 March 2026 and the enhanced regime for taxation years beginning after 4 November 2025. Bind the actual new documentation content and any filing duty; no universal exemption or every-2025-return application. [CRA enactment notice](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html); [247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html).

### 2.4 Country-by-Country Report (Form RC4649)

**Country-by-Country Report (Form RC4649)**  _(https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4651/guidance-on-country-country-reporting-canada.html)_

| Item | Detail |
| --- | --- |
| Threshold | Use immediately preceding fiscal-year consolidated group revenue, with EUR 750-million boundary and actual MNE-group definitions. HOLD actual reporting population and currency/application details. [233.8](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.8.html); [guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4651/guidance-on-country-country-reporting-canada.html) |
| Filing deadline | Section 233.8(6): ordinary 12 months after reporting fiscal year; qualifying systemic-failure notice can create a later 30-day date. HOLD actual branch/notice/date. [(6)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.8.html); [guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4651/guidance-on-country-country-reporting-canada.html) |
| Applies to | Applicable Canadian UPE branch, conditional Canadian constituent-entity local filing, and Canadian surrogate-parent reporting must all be assessed. HOLD actual definitions, parent/jurisdiction/exchange/systemic-failure conditions and any qualifying surrogate filing; UPE status alone is not the complete rule. [233.8(3)-(5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.8.html); [secondary/surrogate guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4651/guidance-on-country-country-reporting-canada.html) |
| Notification | No advance notification required for a Canadian UPE or SPE; an SPE must notify the CRA at the time of filing |

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length standard definition** — Section 247(2) ITA: Where terms/conditions between a taxpayer and a non-arm's length non-resident differ from those that would have been made between arm's length parties, adjustments are made to reflect arm's length conditions.  _(Section 247(2) ITA)_

### 3.2 Accepted Methods

**Accepted Methods**

| Method | Accepted |
| --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes |
| Resale Price Method (RPM) | Yes |
| Cost Plus Method (CPM) | Yes |
| Transactional Net Margin Method (TNMM) | Yes |
| Profit Split Method (PSM) | Yes |

### 3.3 Preferred Method

Select the actual most appropriate method under amended 247(2.04). HOLD unqualified method interchangeability/no-preference advice: CRA TPM-14 includes equal-reliability preferences/natural hierarchy, so old IC87-2R alone is insufficient. [247(2.04)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html); [TPM-14](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing/14-2010-update-oecd-transfer-pricing-guidelines.html).

### 3.4 Recharacterization Power

- **Recharacterization Power** — Older years require the full former 247(2)(b) test, including its bona-fide-purpose/tax-benefit limb; not merely whether arm's-length parties would enter it. Years beginning after 4 November 2025 use the amended adjustment/conditions structure, which can still support a different or no transaction. HOLD actual version, purpose and arrangement; a “single rule” does not abolish those possibilities. [former 247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html); [amended 247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html); [year boundary](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html).

## Section 4 -- Filing Obligations

**Filing Obligations**  _(https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html)_

| Obligation | Detail |
| --- | --- |
| Contemporaneous documentation | Prepared by documentation-due date; provided within 3 months (30 days for taxation years beginning after 4 Nov 2025) of CRA request |
| Form T106 | Annual information return (if threshold met) |
| Form T1134 | HOLD actual foreign-affiliate scope, deadline and exceptions; this crosslink is not a completed filing instruction |
| Form RC4649 (CbCR) | Bind prior-year group revenue and UPE/local/surrogate branches, not group size alone; HOLD actual obligation. [233.8](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.8.html) |
| CbC notification | Not required in advance for a Canadian UPE or SPE; an SPE notifies the CRA at the time of filing |
| Corporate tax return (T2) | Annual self-assessment |

## Section 5 -- Deadlines

**Deadlines**  _(https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf)_

| Item | Deadline |
| --- | --- |
| Documentation preparation | Applicable statutory documentation-due date; person/partnership distinction and subsequent-year changes require actual inputs. [247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |
| Provision to CRA on request | Paragraph 247(4)(c): older three months / later 30 days following specified written-request service; bind year/branch/date. [older](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html); [amended](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |
| Form T106 | Ordinary corporation six months / trust 90 days / individual 30 April or applicable self-employment/spouse extension; HOLD partnership and actual exceptions. [233.1(2)/(3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.1.html); [instructions page 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf) |
| CbCR (RC4649) | Ordinary 12 months, with actual statutory systemic-failure notice branch under (6); HOLD exact date. [233.8(6)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.8.html) |
| T2 corporate tax return | 6 months after taxation year-end |
| T2 tax payment | Ordinary two months; three-month balance requires actual CCPC/SBD/prior-year business-limit and group conditions, not an entity label alone. HOLD eligibility; instalments separate. [CRA T4012](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-before-you-start.html) |

## Section 6 -- Penalties

### 6.1 Transfer Pricing Penalty (s.247(3))

**Transfer Pricing Penalty (s.247(3))**  _(https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html)_

| Item | Detail |
| --- | --- |
| Trigger threshold | Net TP adjustment exceeds lesser of: CAD 5 million OR 10% of gross revenue (for taxation years beginning on or before 4 Nov 2025); lesser of CAD 10 million OR 10% of gross revenue (for taxation years beginning after 4 Nov 2025) |
| Penalty rate | 10% of the applicable statutory (3)(a) amount once (3)(b) gate is exceeded; do not subtract the gate. HOLD definitions, capital/income adjustments, qualifying-arrangement/reasonable-efforts exclusions, offsets and revenue. [247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html); [older](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html) |
| Reasonable efforts defence | Apply actual statutory protection and documentation deeming; records alone are not a certificate of sufficient efforts or universal immunity. [247(3)-(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |
| Documentation impact | Subsection (4), not the penalty-gate paragraph (3)(b), governs deeming. Bind applicable content, due date, material changes and request-service compliance. [247(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |

### 6.2 Other Penalties

The stated T106 figures below are headline schedules from the form, not a complete assessment. HOLD actual failure/slip basis, knowledge/gross negligence, demand and non-compliance timing, offsets and section-162 conditions; multiple slip penalties may be assessed. Do not import every T1135 sanction wholesale.

**Other Penalties**  _(https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf)_

| Offence | Penalty |
| --- | --- |
| Late filing Form T106 | CAD 25/day, minimum CAD 100, maximum CAD 2,500 |
| Failure to file Form T106 | Knowingly or through gross negligence: CAD 500 per month up to CAD 12,000 (CAD 1,000 per month up to CAD 24,000 after a demand) |
| Late CbCR | HOLD quantified amount, operative conditions and actual failure; “standard administrative penalties” is not a usable assessment rule |

## Section 7 -- Advance Pricing Agreements (APA)

**Advance Pricing Agreements (APA)**  _(https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic94-4/international-transfer-pricing-advance-pricing.html)_

| Item | Detail |
| --- | --- |
| Availability | Yes (active program) |
| Types | Unilateral, Bilateral, Multilateral |
| Governing guidance | IC 94-4R2 (Information Circular, February 22, 2024) |
| Application | To CRA Competent Authority Division |
| Duration | Usually five years prospective; HOLD a fixed five-prior-year rollback maximum. Open-year/treaty/factual criteria and unilateral exclusion matter. [paragraph 36](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic94-4/international-transfer-pricing-advance-pricing.html); [TPM-11](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing/11.html) |
| Fees | None set out in IC 94-4R2; travel costs for CRA officials are borne by the CRA (taxpayer pays its own travel and any independent expert) |
| Processing time | Dated 2024 cohort: 13 completed bilateral/multilateral cases, mean 40.8 months acceptance-to-completion; index read 21 November 2026 linked this report. Not a service guarantee or prediction. [2024 report](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-services/advance-pricing-arrangements/2024-apa-program-report.html); [index](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-services/advance-pricing-arrangements.html) |
| Annual compliance report | Required |
| Key benefit | HOLD unconditional immunity. Protection depends on actual covered transactions, effective/complied-with APA and statutory conditions; not every administrative penalty. [IC94-4R2](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic94-4/international-transfer-pricing-advance-pricing.html); [247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |

## Section 8 -- Safe Harbours

HOLD the unqualified absence-of-safe-harbours claim. Actual statutory exclusions and prescribed simplification require separate binding; no blanket entitlement or universal no-exception rule is certified. [247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html).

## Section 8 -- Safe Harbours

**Safe Harbours**  _(https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html)_

| Area | Detail |
| --- | --- |
| Low-value services | HOLD unsupported 5% cost-plus/Canadian acceptance; OECD guidance alone does not establish operative Canadian authority |
| Interest rates | HOLD actual loan/guarantee exclusions, entity/transaction and other interest/thin-cap conditions; no universal benchmarking-only result. [247 scope](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |
| Simplified documentation (later years) | Enabling 247(4.1) requires prescribed conditions, documentation and manner. HOLD current operative prescription and actual eligibility; enactment alone does not qualify a case. [(4.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html); [year boundary](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html) |
| Small transactions | No CAD 1-million documentation exemption follows from T106, but HOLD any universal no-exception/no-safe-harbour conclusion. [247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html); [separate T106 gate](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.1.html) |
| Form T106 threshold | Aggregate transactions ≤ CAD 1 million: no Form T106 filing required |

### 8.1 Practical Risk Assessment

HOLD the following original risk-policy list: no read current primary statement established this exact prioritization. It is an investigation checklist, not proof of current CRA targeting:
- Large/complex transactions with high-risk jurisdictions
- Transactions involving intangibles and cost-sharing arrangements
- Financial transactions (intercompany loans, guarantees)
- Entities with thin capitalisation concerns
- Losses sustained over multiple years in Canada

### 8.2 2025 Simplified Documentation

Legislation enacted by Bill C-15 (Royal Assent March 26, 2026) for taxation years beginning after November 4, 2025 introduces:
- Simplified contemporaneous documentation for taxpayers meeting prescribed conditions
- HOLD current prescribed conditions, operational availability and consultation status; “still being finalized” was not established by the enabling rule alone
- Intended to reduce compliance burden for lower-risk transactions

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| August 2025 | Draft legislation: enhanced TP documentation requirements (OECD-aligned analytical framework) |
| November 2025 | New rules effective for taxation years beginning after 4 November 2025 |
| Nov 2025 | Penalty threshold increased to lesser of CAD 10 million or 10% of gross revenue (for taxation years beginning after 4 Nov 2025; lesser of CAD 5 million or 10% of gross revenue before that date) |
| Later year-beginning regime | Written-request response 30 days only for years beginning after 4 November 2025; older three-month rule retained. [enacted boundary](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html); [247(4)(c)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |
| 2024 | HOLD separate Pillar Two implementation/scope; not established by this TP review |
| Ongoing | HOLD current increased-audit activity claim; exact primary prioritization was not read |
| Later regime | Enabling 247(4.1) exists; HOLD actual prescription/operational status. [(4.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| canada-bookkeeping | TP documentation relies on Canadian accounting records |
| canada-corporate-tax | TP adjustments under s.247 directly affect taxable income |
| canada-gst-hst | HOLD operative customs/GST relationship; a crosslink does not substantiate an adjustment rule |
| Thin capitalisation | HOLD actual 18(4)/loan/guarantee scope and ratio; this is a crosslink, not a verified calculation |
| Form T106 | Annual information return; compliance gateway for TP |
| CbCR | HOLD exact permitted downstream use; do not treat CbCR as conclusive pricing evidence |

## Conditional arithmetic diagnostics

The baseline had no numeric client case. These examples assume the relevant statutory scope and definitions are already established; they do not determine a reporting or penalty outcome. The gate example assumes the stated amount is the correct statutory penalty base after all required exclusions/adjustments, and the stated revenue is the applicable defined revenue. Real amounts and reasonable-efforts/APA protection remain held.

```oa-check
name: T106 aggregate arithmetic does not determine scope
inputs:
  first_relevant_counterparty: 600000
  second_relevant_counterparty: 400000
  additional_relevant_amount: 1
steps:
  - initial_aggregate: first_relevant_counterparty + second_relevant_counterparty
  - revised_aggregate: initial_aggregate + additional_relevant_amount
expected:
  initial_aggregate: 1000000
  revised_aggregate: 1000001
```

Exactly one million does not exceed the T106 filing gate; the second assumed aggregate does. Neither result excuses documentation or proves the underlying transactions are reportable. [ITA 233.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.1.html).

```oa-check
name: Conditional older and later penalty gates are not deductions
inputs:
  assumed_statutory_revenue: 60000000
  assumed_statutory_penalty_base: 7000000
  older_fixed_gate: 5000000
  later_fixed_gate: 10000000
steps:
  - revenue_gate: assumed_statutory_revenue * 0.10
  - older_gate: min(older_fixed_gate, revenue_gate)
  - later_gate: min(later_fixed_gate, revenue_gate)
  - conditional_penalty_after_gate_exceeded: assumed_statutory_penalty_base * 0.10
expected:
  revenue_gate: 6000000
  older_gate: 5000000
  later_gate: 6000000
  conditional_penalty_after_gate_exceeded: 700000
```

The assumed seven-million base exceeds either gate; once the applicable gate is exceeded the conditional result is 700,000, not ten percent of only the excess. This is not an individual assessment or permission to use ordinary gross netting. [Older 247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html); [amended 247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html).

```oa-check
name: Historical 2024 APA completion-stage mean reconciliation
inputs:
  due_diligence_months: 18.9
  negotiation_months: 14.3
  post_negotiation_months: 7.6
steps:
  - reported_combined_mean: due_diligence_months + negotiation_months + post_negotiation_months
expected:
  reported_combined_mean: 40.8
```

The original source's stage labels and actual cohort must govern interpretation; the arithmetic above is a reconciliation of its three reported means, not a new processing standard. [CRA 2024 APA report](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-services/advance-pricing-arrangements/2024-apa-program-report.html).

## Sources

Completed 21 November 2026 reads are reused after confirming the baseline is unchanged. Older and amended statutory versions apply by actual year beginning; no complete Income Tax Act, every foreign-return penalty or current simplification prescription was read. A source citation alone is not proof the unresolved case conditions are met.

| Primary source | Completed read scope | Read date |
| --- | --- | --- |
| [CRA transfer-pricing amendment notice](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing.html) | Enactment on 26 March 2026, year-beginning boundary after 4 November 2025; single structure does not exclude a different/no transaction | 2026-11-21 |
| [Current ITA 247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247.html) | Relevant definitions, adjustment/method rules, complete penalty formula, documentation paragraphs (a)-(c) and enabling simplification; actual capital/income/revenue and case scope held | 2026-11-21 |
| [Older ITA 247](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-247-20210629.html) | Older penalty/documentation and recharacterization purpose/tax-benefit dependency; not applied indiscriminately to later years | 2026-11-21 |
| [Official 2025 T106](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t106/t106-25e.pdf) | Pages 7-9: five methods, reporting scope, aggregate boundary, filing instructions and penalty headlines; actual section-162 case dependencies remain held | 2026-11-21 |
| [ITA 233.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.1.html) | Reporting and de minimis clauses; filing timing in (2)/(3), amount exception in (4) | 2026-11-21 |
| [ITA 233.8](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-233.8.html) | Statutory Part XV placement, reporting branches, definitions and deadline (6); not Part XVIII or deadline (3) | 2026-11-21 |
| [CRA CbCR guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4651/guidance-on-country-country-reporting-canada.html) | Prior-year group revenue, secondary/surrogate branches, ordinary/systemic-failure timing and reporting-entity identification/notifications | 2026-11-21 |
| [IC94-4R2](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic94-4/international-transfer-pricing-advance-pricing.html) | Header and paragraphs 9-18, 23, 36, 64, 94-98; prospective term, process, costs and compliance; no unconditional penalty immunity | 2026-11-21 |
| [TPM-11](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing/11.html) | Conditional rollback with open-year/treaty/factual criteria; fixed five-year maximum not substantiated, unilateral exclusion retained | 2026-11-21 |
| [TPM-14](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/transfer-pricing/14-2010-update-oecd-transfer-pricing-guidelines.html) | Most-appropriate method and equal-reliability preferences/natural hierarchy; not universal interchangeability | 2026-11-21 |
| [CRA APA report index](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-services/advance-pricing-arrangements.html) | At the read date, linked 2024 as latest report; not a promise of current pending-case duration | 2026-11-21 |
| [CRA 2024 APA report](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-services/advance-pricing-arrangements/2024-apa-program-report.html) | Completed-case table: 13 bilateral/multilateral cases, 40.8-month mean; due diligence 18.9, negotiations 14.3, post-negotiations 7.6 months. Bounded 25 November re-read of completion paragraph/table resolves stage labels; historical cohort, not a guarantee | 2026-11-21; bounded follow-up 2026-11-25 |
| [CRA T4012](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-before-you-start.html) | Applicable completed return/balance-payment passages reused; three-month conditions not determined by entity label alone | 2026-11-21 |

**Not yet confirmed:** actual reportable-person/partnership and documentation scope, complete case-specific enhanced contents, subsequent material changes, partnership deadlines, Master/Local File separate-filing position, actual CbCR group/branch/notice/deadline, statutory penalty base/revenue/exclusions/setoffs and every administrative penalty assessment, fixed five-year rollback, unconditional APA immunity, unsupported 5% service markup, current simplification prescription/operational status, loan/guarantee/interest and thin-cap scope, T1134, Pillar Two, current audit-risk assertions, customs/GST relationship and downstream CbCR use. Holds block affected conclusions; six corrected citation/scope groups do not make every tax claim verified.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.
