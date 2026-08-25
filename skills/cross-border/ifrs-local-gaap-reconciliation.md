---
name: ifrs-local-gaap-reconciliation
description: "Use this skill whenever a preparer or reviewer needs to reconcile financial statements between IFRS Accounting Standards and a local GAAP. Trigger on phrases like \"IFRS to US GAAP\", \"GAAP differences\", \"IFRS reconciliation\", \"first-time adoption IFRS 1\", \"ASC 842 vs IFRS 16\", \"ASC 606 vs IFRS 15\", \"ASC 326 CECL vs IFRS 9 ECL\", \"IAS 12 vs ASC 740\", \"Indian Ind AS\", \"Chinese ASBE\", \"Japanese J-GAAP\", \"Brazilian CPC\", \"Italian OIC\", \"German HGB\", \"UK FRS 102\", \"convergence\", \"EBIT vs operating profit\", or any request to identify, quantify, or document a difference between IFRS and a national accounting framework. Covers the major reconciliation differences between IFRS and: US GAAP (ASC), German HGB, UK FRS 102, Italian OIC, French PCG, Indian Ind AS, Chinese ASBE 2006/2014, Japanese J-GAAP, Brazilian CPC (pre/post full IFRS adoption), Canadian ASPE (private enterprises). Does NOT cover: tax accounting (only the IAS 12 / ASC 740 deferred-tax differences are flagged), audit opinion construction, or local statutory filing mechanics. ALWAYS read this skill before booking an IFRS-to-local-GAAP adjustment or producing comparative financial statements."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - financial-statements-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IFRS Local GAAP Reconciliation

## IFRS ↔ Local GAAP Reconciliation v0.1

## What this file is

**This file is a content skill that loads on top of `financial-statements-workflow-base`.** It maps the major recognition, measurement, and presentation differences between IFRS Accounting Standards (as issued by the IASB through 31 December 2024) and the principal national accounting frameworks.

**Tax year coverage.** Current for **annual periods beginning on or after 1 January 2025**, reflecting:
- IFRS 18 Presentation and Disclosure in Financial Statements (effective 1 January 2027 — early adoption permitted)
- IFRS 19 Subsidiaries without Public Accountability: Disclosures (effective 1 January 2027 — early adoption permitted)
- US ASU 2023-09 Improvements to Income Tax Disclosures (effective for public business entities annual periods beginning after 15 Dec 2024)
- US ASU 2023-07 Segment Reporting (effective annual periods beginning after 15 Dec 2023)
- IND AS amendments per Companies (Indian Accounting Standards) Amendment Rules 2024
- China MOF revisions to ASBE (2024 supplementary guidance)

**The reviewer is the customer of this output.** GAAP reconciliations have direct consequences for reported earnings, debt covenant compliance, and tax provisions. Every output must be reviewed by a credentialed practitioner (typically a CPA / CA with dual-GAAP experience) before any reconciliation is finalised.

## Section 1 — Scope statement

This skill covers reconciliation between **IFRS Accounting Standards** and:

- **US GAAP** (FASB Accounting Standards Codification)
- **German HGB** (Handelsgesetzbuch §238-342e plus DRS standards)
- **UK GAAP** (FRS 102 — the Financial Reporting Standard applicable in the UK and Republic of Ireland)
- **Italian OIC** (Organismo Italiano di Contabilità standards, codified Civil Code Art. 2423-2435 et seq.)
- **French PCG** (Plan Comptable Général; ANC Règlement 2014-03 consolidated)
- **Indian Ind AS** (Companies (Indian Accounting Standards) Rules 2015 — broadly IFRS-equivalent with carve-outs)
- **Chinese ASBE** (Accounting Standards for Business Enterprises 2006/2014 — substantively converged with IFRS but with material differences in application)
- **Japanese J-GAAP** (Japanese Generally Accepted Accounting Principles per ASBJ and Business Accounting Council)
- **Brazilian CPC** (Comitê de Pronunciamentos Contábeis — Brazil adopted full IFRS for listed entities from 2010; CPC standards mirror IFRS, but PJ-medium and small entities apply CPC-PME)
- **Canadian ASPE** (Accounting Standards for Private Enterprises — Part II of CPA Canada Handbook)

This skill does NOT cover:

- **Local statutory filing mechanics** (XBRL formats, regulator portals, audit thresholds — see country `*-financial-statements.md` skills).
- **Tax computations** beyond the deferred-tax recognition and measurement differences.
- **First-time adoption mechanics in jurisdiction-specific detail** (see IFRS 1 with jurisdiction overlays).
- **Audit opinion drafting** under local GAAS / ISAs.
- **Industry-specific GAAPs** for insurance (other than IFRS 17 vs ASC 944), banking (other than IFRS 9 vs ASC 326), or extractives.

## Section 2 — Reconciliation methodology

### Step 1 — Identify the framework pair

- **Confirm framework pair** — **[T1]** Confirm both frameworks in play. Document: - IFRS as issued by IASB? Or IFRS as adopted by EU? Or local IFRS-equivalent (Ind AS, ASBE)? - Specific local GAAP: US GAAP (public vs private)? FRS 102 (full vs Section 1A)? HGB (BilMoG era)?  _([T1])_

### Step 2 — Identify the reporting periods

Annual periods, comparative periods, restatement scope.

### Step 3 — Walk the difference catalogue (Section 3)

- **Walk difference catalogue** — For each line item or transaction, walk through: - The IFRS treatment with paragraph citation - The local GAAP treatment with paragraph citation - The difference in measurement, recognition, or presentation - The adjustment entry (debit/credit, balance sheet and income statement legs)  _(unsure)_

### Step 4 — Document the reconciliation

- **Document reconciliation outputs** — Produce: - A net income reconciliation: IFRS PAT → local GAAP PAT with line items - An equity reconciliation: IFRS equity → local GAAP equity with line items - A balance sheet reconciliation by major category - An operating-cash-flow reconciliation if a cash flow statement is in scope  _(unsure)_

## Section 3 — Material difference catalogue

### 3.1 Revenue recognition

**Revenue recognition — IFRS vs US GAAP vs Other GAAP**  _(IFRS 15 / ASC 606)_

| Topic | IFRS | US GAAP | Other GAAP |
| --- | --- | --- | --- |
| Standard | IFRS 15 | ASC 606 | HGB: realisation principle (§252(1)4 HGB) — narrower; FRS 102 §23 — IFRS-aligned; J-GAAP: substantively converged 2018 |
| Variable consideration | Estimated and constrained (expected value or most likely) | Same (ASC 606 was joint project) | HGB: realised only when claim is enforceable |
| Licences (right to use vs right to access) | Point in time vs over time | Same | HGB: revenue at delivery |
| Contract costs (commissions) | Capitalise if recoverable; amortise (IFRS 15 ¶91-94) | Same (ASC 340-40) | HGB: expense as incurred |
| Principal vs agent | Control of specified good/service before transfer | Same | Generally consistent |

**Typical adjustment:** none if both IFRS 15 and ASC 606 are properly applied; differences emerge in transition period adjustments (modified retrospective vs full retrospective).

### 3.2 Leases

**Leases — IFRS 16 vs ASC 842**  _(IFRS 16 / ASC 842)_

| Topic | IFRS 16 | ASC 842 |
| --- | --- | --- |
| Lessee model | Single model: capitalise all leases ≥ 12 months and > USD 5,000 with ROU asset and lease liability | Dual model: Finance leases (similar to IFRS 16) and Operating leases (ROU asset but straight-line P&L expense) |
| P&L pattern | Depreciation + interest (front-loaded total) | Operating: straight-line lease expense; Finance: depreciation + interest |
| Lessor model | Substantially converged with ASC 840/842 | Substantially converged with IFRS 16 |
| Sale-and-leaseback | Recognise gain only to extent of rights transferred | Subtle measurement difference where leaseback at off-market terms |

- **Recurring P&L difference** — **[T1] Recurring P&L difference:** under ASC 842 operating leases, lessees report straight-line rent; under IFRS 16 the same lease produces front-loaded expense. EBITDA differs.  _([T1])_

**IFRS 16 vs FRS 102**

| Topic | IFRS 16 vs FRS 102 |
| --- | --- |
| FRS 102 (UK private) | Section 20 retains the operating-vs-finance distinction; no ROU asset for operating leases. Material difference on transition from IFRS to FRS 102 (e.g., for groups moving to UK private status). |

**IFRS 16 vs HGB**

| Topic | IFRS 16 vs HGB |
| --- | --- |
| HGB | Lessee accounting follows economic ownership tests (BilMoG). Most operating leases remain off-balance-sheet — significant difference vs IFRS 16. |

### 3.3 Financial instruments — impairment

**Financial instruments impairment — IFRS 9 vs ASC 326**  _(IFRS 9 / ASC 326)_

| Topic | IFRS 9 | ASC 326 (CECL) |
| --- | --- | --- |
| Model | 3-stage Expected Credit Loss (ECL) — 12-month ECL → lifetime ECL on significant increase in credit risk → lifetime ECL on credit-impaired | Current Expected Credit Loss (CECL) — lifetime ECL from inception, no staging |
| Scope | Financial assets at amortised cost, FVOCI debt, lease receivables, loan commitments, financial guarantees | Same scope plus held-to-maturity debt securities |
| Available-for-sale securities | n/a (replaced by FVOCI debt) | OTTI replaced by available-for-sale credit loss model (allowance) |

- **Quantitative difference** — **[T1] Quantitative difference:** ASC 326 generally produces higher day-one allowances because lifetime ECL applies from origination. IFRS 9 day-one allowance is 12-month ECL only.  _([T1])_

### 3.4 Financial instruments — classification and measurement

**Financial instruments classification — IFRS 9 vs ASC 320/321/825**  _(IFRS 9 / ASC 320/321/825)_

| Topic | IFRS 9 | ASC 320/321/825 |
| --- | --- | --- |
| Classification | Business model + SPPI: amortised cost / FVOCI / FVPL | Trading / Available-for-sale / Held-to-maturity (debt); FV through earnings (equity) |
| Equity investments without significant influence | FVPL or FVOCI election (no recycling) | Generally FVPL unless practicable expedient (cost less impairment, less observable price changes) for non-marketable |

### 3.5 Goodwill

**Goodwill — IFRS vs US GAAP**  _(IAS 38 / IFRS 3 / ASC 350 / ASU 2014-02 / ASU 2017-04)_

| Topic | IFRS | US GAAP |
| --- | --- | --- |
| Amortisation | Not amortised (IAS 38 ¶107 / IFRS 3) | Not amortised by public BEs; private companies may elect 10-year amortisation under ASU 2014-02 |
| Impairment test | Annual + indicator-based; one-step (recoverable amount = higher of FV less costs to sell, value in use) | Annual + indicator; one-step quantitative for public BEs after ASU 2017-04 |
| CGU vs Reporting Unit | IAS 36 CGU | ASC 350 Reporting Unit (typically broader) |

**Goodwill — IFRS vs HGB**  _(HGB §253(3))_

| Topic | IFRS vs HGB |
| --- | --- |
| HGB §253(3) requires goodwill amortisation over useful life (default 5 years if not estimable) | Material recurring P&L difference |

**Goodwill — IFRS vs J-GAAP**

| Topic | IFRS vs J-GAAP |
| --- | --- |
| J-GAAP requires goodwill amortisation over up to 20 years (typically straight-line) | Material recurring P&L difference |

### 3.6 Inventory

**Inventory — IFRS (IAS 2) vs US GAAP (ASC 330)**  _(IAS 2 / ASC 330)_

| Topic | IFRS (IAS 2) | US GAAP (ASC 330) |
| --- | --- | --- |
| LIFO | Prohibited | Permitted (and common in US tax matching — LIFO conformity rule) |
| Lower of cost / NRV reversal | Permitted if NRV recovers | Reversal not permitted (one-way) |

- **Adjustment note** — **[T1] Adjustment:** LIFO-reserve reclassification; reversal restoration on inventory write-down recovery (rare but material when present).  _([T1])_

### 3.7 Property, plant and equipment

**PP&E — IFRS (IAS 16) vs US GAAP (ASC 360) vs HGB**  _(IAS 16 / ASC 360 / HGB §253)_

| Topic | IFRS (IAS 16) | US GAAP (ASC 360) | HGB |
| --- | --- | --- | --- |
| Revaluation model | Permitted | Not permitted | Not permitted (HGB §253 cost-based) |
| Component depreciation | Required (IAS 16 ¶43) | Permitted, less commonly applied | Not required |
| Impairment reversal | Required when indicators reverse | Not permitted (ASC 360-10-35-20) | Required for reversible impairment |

### 3.8 Intangible assets / development costs

**Development costs — IFRS (IAS 38) vs US GAAP (ASC 350, 730, 985-20)**  _(IAS 38 / ASC 350 / ASC 730 / ASC 985-20)_

| Topic | IFRS (IAS 38) | US GAAP (ASC 350, ASC 730, ASC 985-20) |
| --- | --- | --- |
| Internal development costs | Capitalise from development phase if 6 criteria met | Generally expensed (R&D) except for ASC 985-20 software (technological feasibility test) and certain web/internal-use software (ASC 350-40) |

- **Recurring difference note** — **[T1] Recurring difference:** IFRS-compliant tech companies often capitalise more development cost than under US GAAP. Reconciliation requires reversal.  _([T1])_

### 3.9 Borrowing costs

**Borrowing costs — IFRS (IAS 23) vs US GAAP (ASC 835-20)**  _(IAS 23 / ASC 835-20)_

| Topic | IFRS (IAS 23) | US GAAP (ASC 835-20) |
| --- | --- | --- |
| Qualifying assets | Capitalise on qualifying assets | Same |
| Inventories (long production cycle) | Capitalise unless routinely manufactured in large quantities | Generally expense routine inventory; capitalise for major construction inventory |

### 3.10 Provisions

**Provisions — IFRS (IAS 37) vs US GAAP (ASC 450)**  _(IAS 37 / ASC 450)_

| Topic | IFRS (IAS 37) | US GAAP (ASC 450) |
| --- | --- | --- |
| Recognition | "Probable" = more likely than not (>50%) | "Probable" = high likelihood (typically interpreted as ~70%-80%) |
| Measurement | Best estimate; discount if material | Best estimate of range; if range, low end if no point in range better; usually not discounted unless timing is fixed |

- **Quantitative difference** — **[T1] Quantitative difference:** IFRS recognises more provisions at smaller amounts; US GAAP recognises fewer provisions but at higher amounts.  _([T1])_

### 3.11 Employee benefits

**Employee benefits — IFRS (IAS 19) vs US GAAP (ASC 715)**  _(IAS 19 / ASC 715)_

| Topic | IFRS (IAS 19) | US GAAP (ASC 715) |
| --- | --- | --- |
| Pension actuarial gains/losses | Through OCI immediately (no recycling) | Through OCI with amortisation to P&L over expected remaining service life (corridor method abolished by ASC 715 amendments but amortisation remains) |
| Net interest on net defined benefit liability | Single rate (discount rate) on net liability | Separate expected return on plan assets and interest cost on PBO |

### 3.12 Income taxes

**Income taxes — IFRS (IAS 12) vs US GAAP (ASC 740)**  _(IAS 12 / ASC 740)_

| Topic | IFRS (IAS 12) | US GAAP (ASC 740) |
| --- | --- | --- |
| Uncertain tax positions | Single best estimate / expected value | Two-step: more-likely-than-not recognition, then measurement at cumulative-probability ≥ 50% |
| Intra-entity asset transfers | Recognise deferred tax effects immediately (post-2017 ASU eliminated US deferral but only for non-inventory; inventory still deferred) | Inventory deferred until external sale; non-inventory recognised |
| Tax base | Tax base concept | Same |

### 3.13 Foreign exchange

**Foreign exchange — IFRS (IAS 21) vs US GAAP (ASC 830)**  _(IAS 21 / IAS 29 / ASC 830-10-45-12)_

| Topic | IFRS (IAS 21) | US GAAP (ASC 830) |
| --- | --- | --- |
| Functional currency determination | Primary indicators + secondary | Same with subtle differences for parent's currency in cumulative translation |
| Hyperinflationary economies | IAS 29 restatement when cumulative 3-yr inflation > 100% | ASC 830-10-45-12: same threshold; remeasure as if functional currency = reporting currency |

### 3.14 Consolidation

**Consolidation — IFRS (IFRS 10) vs US GAAP (ASC 810)**  _(IFRS 10 / ASC 810 / ASC 946)_

| Topic | IFRS (IFRS 10) | US GAAP (ASC 810) |
| --- | --- | --- |
| Control | Single model: power + variable returns + ability to use power | Two models: voting interest entities and Variable Interest Entities (VIE) |
| Investment entity exception | IFRS 10 exempts investment entities from consolidating non-investment subsidiaries | ASC 946 similar for investment companies |

### 3.15 Business combinations

**Business combinations — IFRS 3 vs ASC 805**  _(IFRS 3 / ASC 805 / IAS 32)_

| Topic | IFRS 3 | ASC 805 |
| --- | --- | --- |
| Non-controlling interest measurement | Choice on each business combination: FV (full goodwill) or proportionate share of identifiable net assets | Always FV (full goodwill) |
| Contingent consideration classification | Liability or equity per IAS 32 (most variable-amount = liability) | Same |
| Acquisition-related costs | Expense | Expense |

### 3.16 Cash flow statement

**Cash flow statement — IFRS (IAS 7) vs US GAAP (ASC 230)**  _(IAS 7 / ASC 230)_

| Topic | IFRS (IAS 7) | US GAAP (ASC 230) |
| --- | --- | --- |
| Interest paid | Choice: operating or financing | Operating only |
| Interest received | Choice: operating or investing | Operating only |
| Dividends paid | Choice: operating or financing | Financing only |
| Dividends received | Choice: operating or investing | Operating only |
| Income taxes | Operating unless specifically identifiable with investing/financing | Operating only |

### 3.17 Presentation (IFRS 18 effective 2027)

- **IFRS 18 presentation changes** — **[T1]** IFRS 18 introduces three required categories on the income statement: operating, investing, financing. Mandates new subtotals: operating profit, profit before financing and tax. Adds management-defined performance measures (MPMs) reconciliation. **No direct US GAAP equivalent** — material presentation difference begins 2027.  _([T1] IFRS 18)_

### 3.18 Subsidiaries without public accountability (IFRS 19 effective 2027)

- **IFRS 19 reduced disclosure** — Permits reduced disclosure for subsidiaries of IFRS parents that have no public accountability. No US GAAP equivalent (compare to ASC private-company alternatives).  _(IFRS 19)_

## Section 4 — German HGB-specific differences

**HGB vs IFRS differences**  _(HGB §252, §248(2), §253(2), §275(2)1, §249, §256a, §254)_

| Topic | HGB | IFRS |
| --- | --- | --- |
| Prudence principle | Strict imparity / realisation principles (§252) | Neutral / faithful representation |
| Internally generated intangibles | Optional capitalisation under §248(2) BilMoG (rare in practice) | Required IFRS 38 capitalisation if 6 criteria met |
| Goodwill | Amortise over useful life (default 5 years) | Not amortised |
| Pension provisions | Discount rate set by Bundesbank-published average (§253(2)) | Yield on AA corporate bonds in IAS 19 |
| Construction contracts | Completed contract method permitted (§275(2)1) | IFRS 15 percentage-of-completion (over time) when criteria met |
| Provisions | More extensive recognition (§249) including for omissions of own labour | IAS 37 narrower |
| Foreign currency receivables/payables ≤ 1 yr | Reported at lower of historical or closing rate (§256a) | IAS 21 closing rate |
| Derivatives | Designated hedges only at fair value; otherwise §254 hedge units with no gain recognition | IFRS 9 all derivatives at FV |

## Section 5 — UK FRS 102-specific differences

**FRS 102 vs IFRS differences**  _(FRS 102)_

| Topic | FRS 102 | IFRS |
| --- | --- | --- |
| Goodwill | Amortise over finite useful life (max 10 years if not reliably estimable) | Not amortised |
| Investment property | FV through P&L if held to earn rentals AND FV can be measured reliably without undue cost or effort | Same option; FRS 102 has the "undue cost or effort" cap |
| Borrowing costs | Accounting policy choice: expense or capitalise | IAS 23 capitalise on qualifying assets (no choice) |
| Development costs | Policy choice: expense or capitalise | IAS 38 capitalise if 6 criteria met |
| Defined benefit plan accounting | Net interest model (similar to IAS 19) | Same |
| Lease accounting | Operating-vs-finance distinction (Section 20) — operating leases off-balance-sheet | IFRS 16 single model, ROU on balance sheet |

- **FRS 102 March 2024 amendments** — **[T1] FRS 102 March 2024 amendments** (effective 1 January 2026): bring lease accounting closer to IFRS 16 (ROU asset and lease liability for material operating leases). Until then, leases is the largest FRS 102 ↔ IFRS difference for UK private companies.  _([T1] FRS 102 March 2024 amendments)_

## Section 6 — Indian Ind AS-specific carve-outs

- **Ind AS broadly IFRS-equivalent** — **[T1]** Ind AS is broadly IFRS-equivalent (Companies Indian Accounting Standards Rules 2015) but contains carve-outs:  _([T1])_

**Ind AS vs IFRS differences**  _(Ind AS Para 46A, Ind AS 11 App C)_

| Topic | Ind AS | IFRS |
| --- | --- | --- |
| Foreign currency monetary items long-term | Para 46A option: amortise FX over remaining life of asset / liability | IAS 21 immediate P&L (with hedge accounting overlay) |
| Bargain purchase | Recognise in capital reserve through OCI | IFRS 3 recognise gain in P&L |
| Property, plant and equipment | Option to use previous GAAP carrying value as deemed cost (first-time adoption) | Choice but stricter rules |
| Service concession arrangements | Not yet fully adopted (App C to Ind AS 11 deferred); IFRIC 12 broader | Full IFRIC 12 |

## Section 7 — Chinese ASBE-specific differences

- **ASBE substantively converged note** — **[T1]** Substantively converged with IFRS, but:  _([T1])_

**ASBE vs IFRS differences**  _(ASBE / IAS 36 / IAS 20 / IFRS 3)_

| Topic | ASBE | IFRS |
| --- | --- | --- |
| Related-party transactions | Broader disclosure required including state-owned enterprises under common control | Generally narrower |
| Reversal of asset impairment | Goodwill, long-lived assets — NOT reversible | Long-lived assets reversible (IAS 36) |
| Government grants | Choice of gross vs net presentation | IAS 20 — option |
| Mergers under common control | Pooling-of-interests with carrying value | IFRS 3 excludes common control; in practice, pooling |
| Fixed assets — borrowing costs | Capitalise mandatorily | Same |

## Section 8 — Japanese J-GAAP-specific differences

**J-GAAP vs IFRS differences**  _(ASBJ Statement 29)_

| Topic | J-GAAP | IFRS |
| --- | --- | --- |
| Goodwill | Amortise over useful life (max 20 years) straight-line | Not amortised |
| Revenue | Substantively converged with IFRS 15 from FY2021 (ASBJ Statement 29) | IFRS 15 |
| Leases | Lessee: finance vs operating distinction; off-balance for operating | IFRS 16 single model |
| Development costs | Generally expensed (similar to old US GAAP); software for sale capitalised after technological feasibility | IFRS 38 capitalise if 6 criteria met |
| R&D | Expense as incurred | Same |
| Pension actuarial gains/losses | OCI immediately recognised under updated standards (post-2014 ASBJ); previously corridor allowed | IFRS 19 OCI immediately |

## Section 9 — Brazilian CPC-specific notes

**[T1]** Listed companies must use CPC standards (Brazilian IFRS-equivalent). Closely held entities (PME) may apply CPC-PME — substantively the IFRS for SMEs. Differences from full IFRS for listed companies are minor and typically arise from:
- Timing of Brazilian-specific interpretations (ICPC, OCPC)
- Tax provisions interacting with the RTT/MEP regime now repealed
- Indexation of pre-IFRS opening balances under Law 11638/2007

## Section 10 — Canadian ASPE-specific differences

ASPE (Part II of CPA Canada Handbook) is the Canadian framework for private enterprises that elect not to apply IFRS. Substantive differences:

**ASPE vs IFRS differences**  _(ASPE Part II CPA Canada Handbook)_

| Topic | ASPE | IFRS |
| --- | --- | --- |
| Goodwill | Amortise over useful life (no max stated, typically ≤ 40 years) | Not amortised |
| Intangibles | Amortise over useful life | If finite, amortise; if indefinite, impairment-only |
| Leases | Operating-vs-finance distinction | IFRS 16 single model |
| Income taxes | Choice of taxes-payable method or future income taxes method (deferred) | IAS 12 deferred only |
| Investments in subsidiaries / associates | Choice of cost, equity, or consolidation | IFRS requires consolidation / equity method per applicable IFRS |
| Defined benefit plans | Choice of accrued benefit obligation valuation method | IAS 19 prescribed projected unit credit |

## Section 11 — Output specification

The reviewer brief must include:

1. **Framework pair** and reporting period scope.
2. **Difference catalogue** filled in for the entity, marking each as material / immaterial.
3. **Net income reconciliation** with each line item showing IFRS → local GAAP delta.
4. **Equity reconciliation** with each line item.
5. **Balance sheet reconciliation** by major category.
6. **Disclosure adjustments** — disclosures required under each framework that the other does not require.
7. **Transition-period adjustments** if IFRS 1, FRS 102 first-time adoption, or other transition rules apply.
8. **Future-effective standards** flagged: IFRS 18 (2027), IFRS 19 (2027), FRS 102 March 2024 amendments (2026), upcoming ASBJ amendments.
9. **Reviewer questions** — open items flagged as [T2] or [T3].

## Section 12 — Self-checks

- [ ] Both frameworks correctly identified (IFRS as issued by IASB vs EU-endorsed vs Ind AS).
- [ ] Each material difference walked sub-item by sub-item with paragraph citations.
- [ ] Goodwill amortisation difference quantified for HGB, J-GAAP, ASPE, FRS 102.
- [ ] Leases reconciliation completed for IFRS 16 vs ASC 842 / FRS 102 / HGB.
- [ ] ECL vs CECL difference quantified for financial institutions.
- [ ] LIFO reserve reclassified for US GAAP-to-IFRS movement (or vice versa).
- [ ] Deferred tax reconciliation includes uncertain tax position differences.
- [ ] Cash flow presentation differences identified.
- [ ] Future-effective IFRS 18 / IFRS 19 / FRS 102 amendments flagged.
- [ ] Output flags every [T2]/[T3] item for reviewer judgement.

## Section 13 — Prohibitions

- **Do not** treat IFRS-as-EU-endorsed and IFRS-as-issued-by-IASB as identical without checking the EU endorsement status of recent standards.
- **Do not** apply ASBE / Ind AS / CPC differences from training memory without confirming the current national standard text — Asian and Latin American frameworks update faster than the documentation tracks.
- **Do not** reverse impairments on goodwill or long-lived assets under US GAAP — both are one-way.
- **Do not** capitalise development costs under US GAAP outside the limited ASC 985-20 / ASC 350-40 software exceptions.
- **Do not** assume an ASPE or FRS 102 entity has "less" deferred tax — many ASPE entities elect the future-tax method and have full DTA/DTL.

## Section 14 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute accounting, audit, or financial advice. GAAP differences carry direct consequences for reported earnings, debt covenants, and tax provisions. Every output must be reviewed and signed off by a credentialed CPA / CA with dual-GAAP experience before any reconciliation is finalised.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
