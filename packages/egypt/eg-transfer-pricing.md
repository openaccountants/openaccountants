---
name: eg-transfer-pricing
description: Use this skill whenever asked about Egyptian transfer pricing documentation, benchmarking, or related-party transaction review — for residents with cross-border or domestic related-party dealings. Trigger on "Egypt TP", "Egypt transfer pricing", "Master File Egypt", "CbCR Egypt", "ضريبة نفقات الشركات المرتبطة مصر". ALWAYS read this skill before touching any Egypt TP work.
version: 0.1
jurisdiction: EG
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt Transfer Pricing

## Egypt Transfer Pricing (تسعير المعاملات بين الشركات المرتبطة) Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Jurisdiction is required.** Set `jurisdiction: EG` in frontmatter even when the folder path implies it. Sync to openaccountants.com skips files without a resolvable jurisdiction.

This skill covers Egyptian **transfer pricing (TP)** compliance for resident companies, permanent establishments of non-residents, and Egyptian-parented MNE groups. Egypt was the first country in the Middle East to introduce TP legislation (Article 30, Income Tax Law No. 91 of 2005). The framework is OECD-aligned, following BEPS Action 13's three-tier documentation model. The AI must reply in the user's language (English or Arabic / Egyptian Arabic) and may use the native tax terms shown throughout.

> **Currency note:** all figures are in Egyptian Pounds (EGP / ج.م).
> **YMYL — verify before relying.** Egyptian TP guidelines, thresholds, and penalty rates are subject to amendment (most recently Laws 5, 6, 7 of 2025). Where this skill says "verify current value," re-confirm against the Egyptian Tax Authority (ETA — eta.gov.eg), PwC Worldwide Tax Summaries (taxsummaries.pwc.com/egypt), or a Big-4 alert before filing.

## What this file is

**This file is a content skill that loads on top of a workflow base** (here: `transfer-pricing-workflow-base`). It provides Egypt-specific TP rules, documentation thresholds, methods, filing deadlines, penalty regimes, and APA procedure.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Egypt (جمهورية مصر العربية) |
| Tax authority | Egyptian Tax Authority (ETA — مصلحة الضرائب المصرية, eta.gov.eg) |
| Primary TP legislation | Article 30, Income Tax Law No. 91 of 2005 (قانون الضريبة على الدخل) |
| Executive Regulations | Articles 38, 39, 40 of the Executive Regulations of Law 91/2005 |
| TP Guidelines | Egyptian Transfer Pricing Guidelines, Ministerial Decree No. 547 of 2018 (circulating as the ETA TP circulars) |
| Related-party definition | Article 1, Executive Regulations of Unified Tax Procedures Law No. 206 of 2020 (amended by Law No. 211 of 2020) |
| APA basis | Ministerial Decree No. 221 of 2018 (amended Art 30 ITL); bilateral/multilateral available |
| OECD member? | No |
| BEPS Inclusive Framework? | Yes (member) |
| OECD TPG adoption | Egyptian TPG modeled on OECD TPG (2017 ed., acknowledged as global standard) |
| Currency | EGP (ج.م) |
| Documentation language | Arabic; English accepted for MNE groups with non-Arabic parents |
| Skill version | 0.1 |

## Section 2 — Legal Foundation

### 2.1 Primary Articles

**Primary Articles**  _(Executive Regs Art 39; Law 91/2005; Ministerial Decrees 547/2018, 221/2018; Unified Tax Procedures Law 206/2020)_

| Source | Scope |
| --- | --- |
| **Law 91/2005 Art 30** | Arm's length principle applied to transactions between related parties — commercial, financial, goods, services, cost contributions, royalties, interest, other commercial/financial transactions |
| **Law 91/2005 Executive Regs Art 38** | Related-party scope; application of arm's length principle |
| **Law 91/2005 Executive Regs Art 39** | Recognised TP methods (CUP, RPM, CPM, TNMM, PSM); other appropriate methods permitted with supporting documentation |
| **Law 91/2005 Executive Regs Art 40** | Documentation requirements; comparability analysis; documentation retention |
| **Ministerial Decree 547/2018** | Egyptian Transfer Pricing Guidelines — a guide to the application of Art 30 of Law 91/2005 (modeled on OECD TPG 2017) |
| **Ministerial Decree 221/2018** | Amendments to Art 30 ITL — added TNMM and PSM as permissible methods; authorised APAs; authorised ETA guidance on documentation |
| **Unified Tax Procedures Law 206/2020 Art 1** | Related-party definition (replaces prior definitions in scattered regs) |
| **Law 91/2005 Arts 24, 52, 56** | Non-TP rules relevant to related-party transactions: interest deductibility (Art 24 — interest on loans exceeding 2× CBE rate non-deductible), thin-cap interaction, Art 56 WHT on payments to non-residents at 20% |

### 2.2 Arm's Length Principle

Article 30 of Law 91/2005 applies the arm's length principle: where a transaction between related parties is not at arm's length, the ETA may adjust taxable profit to reflect what independent parties would have agreed. The 2018 Decree expanded the scope to explicitly include commercial and financial transactions for goods, services, cost contribution allocations, royalties, interest, and other commercial/financial transactions.

### 2.3 Related Party Definition (Law 206/2020 Art 1)

Related parties exist where the relationship affects, directly or indirectly (through management, control, or ownership), the determination of the tax base. Two persons are related where one or both can make dispositions according to the directions, requests, proposals, or will of the other or a third party. Specifically:

1. Husband, wife, ascendants, descendants, or inter se
2. Partnerships, general partners, and limited partners therein
3. Companies and the person who owns, directly or indirectly, at least 50% of the voting rights, management, dividends, or capital rights
4. Two or more companies in which another person owns or acquired at least 50% of voting rights, management, or dividends/capital rights

> **Note.** Ownership attributed by a related party may not be reassigned to another. Employees/clients are not related parties solely by virtue of that relationship unless it affects the tax base.

## Section 3 — Documentation Requirements

Egypt follows the OECD BEPS Action 13 three-tier documentation model.

### 3.1 Documentation Threshold

**Documentation Threshold**

| Item | Detail |
| --- | --- |
| Master File + Local File required | Aggregated annual related-party transactions > **EGP 15 million** |
| Below threshold | Arm's length pricing must still be substantiated; TP policy/strategy recommended but documentation not mandatory |
| Individual transaction records | Maintain records of material controlled transactions (> EGP 1m individually as a practical benchmark; no statutory individual threshold) |

> **Threshold verification.** The EGP 15m threshold is the widely-cited figure in professional practice (Andersen 2025, ETA guidance). Earlier sources cited EGP 8m; verify current threshold against ETA before filing — the threshold may have been amended by Laws 5, 6, 7 of 2025.

### 3.2 Master File

**Master File**

| Item | Detail |
| --- | --- |
| Required? | Yes, where EGP 15m threshold met |
| Format | OECD-aligned per BEPS Action 13 |
| Content | Group organisational structure; description of business; intangibles ownership and strategy; intercompany financial activities; consolidated financial and tax positions |
| Filing | Filed with ETA — align with ultimate parent's Master File filing date in its home jurisdiction |
| Language | Arabic; English accepted for non-Arabic parent groups |
| Size | No statutory MB cap; ETA may set practical limits |

### 3.3 Local File

**Local File**

| Item | Detail |
| --- | --- |
| Required? | Yes, where EGP 15m threshold met |
| Format | OECD-aligned; entity-specific analysis of material transactions |
| Content | Local entity business description; FAR analysis (functions, assets, risks); controlled transaction descriptions; method selection; comparability analysis and benchmarking; financial data |
| Filing | Due **within two months** of filing the CIT return |
| Revised return interaction | If a revised CIT return is filed within 30 days, Local File deadline resets to two months from the new submission date |
| Comparables preference | Egyptian comparables searched first; then Middle Eastern/African regional; then global (per Egyptian TPG §5.7.3.1) |

### 3.4 Country-by-Country Report (CbCR)

**Country-by-Country Report (CbCR)**

| Item | Detail |
| --- | --- |
| Egyptian-parent threshold | MNE groups with consolidated group revenue ≥ **EGP 3 billion** (≈ EUR 750m; aligned with OECD CbCR threshold) |
| Non-Egyptian-parent threshold | OECD EUR 750m applies; Egyptian subsidiaries must file CbCR Notification in each tax year |
| Surrogate filing | Egyptian subsidiary may be required to file locally if the parent's jurisdiction does not require CbCR, does not have automatic exchange with Egypt, or fails to file |
| Filing deadline | **12 months** after the last day of the reporting fiscal year of the MNE group |
| Format | Per BEPS Action 13 / OECD CbC template (Annex III) |
| Notification | Required for each Egyptian subsidiary of an MNE group meeting the threshold |
| Effective | From fiscal years beginning on/after 1 January 2018 |

## Section 4 — Transfer Pricing Methods

### 4.1 Accepted Methods (Executive Regs Art 39)

**Accepted Methods**  _(Executive Regs Art 39)_

| Method | Accepted | Best suited for |
| --- | --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes | Commodities, standard goods with public prices; must be applied where reliable comparables available |
| Resale Price Method (RPM) | Yes | Distributors that add limited value to goods purchased from related parties |
| Cost Plus Method (CPM) | Yes | Manufacturers; service providers; routine back-office functions |
| Transactional Net Margin Method (TNMM) | Yes | Most common in practice; acceptable for a wide range of transactions |
| Profit Split Method (PSM) | Yes | Highly integrated operations; unique intangibles; both parties contribute significant value |
| Other appropriate methods | Yes | Per 2018 Decree — permitted with supporting documentation |

### 4.2 Method Selection

Egypt applies the **"most appropriate method"** criterion (Egyptian TPG §2.3.2) — not a strict hierarchy. The method most directly producing an arm's length result for the specific transaction must be selected, consistent with OECD TPG Chapter II.

### 4.3 Comparability Analysis

**Comparability Analysis**

| Requirement | Detail |
| --- | --- |
| OECD TPG Chapter III alignment | Yes, Egypt follows the OECD approach |
| Comparability adjustments | Required where differences between controlled and uncontrolled transactions affect price/margin (Egyptian TPG Chapter 4) |
| Arm's length range | Permitted; statistical measures (interquartile range) applied where sufficient comparables exist |
| Domestic vs foreign comparables | Egyptian comparables preferred; regional (Middle East/Africa) secondary; global tertiary (Egyptian TPG §5.7.3.1) |
| Secret comparables | **Not used** (confirmed in OECD TP Country Profile — Egypt, 2022) |
| Commodity transactions | Follows OECD TPG ¶¶2.18-2.22 (Egyptian TPG §4.4.1) |

### 4.4 Intra-Group Services

**Intra-Group Services**

| Field | Detail |
| --- | --- |
| Dedicated guidance in Egyptian TPG? | No (OECD TPG consulted for detail) |
| Low-value-adding services safe harbour? | No |
| Benefit test | Apply OECD TPG Chapters IV and VII principles — services must provide economic/commercial value; shareholder-type costs generally not chargeable |
| Charge-out vs cost-only | Both accepted in practice; charge-out (cost + markup) most common for routine shared services; cost-only acceptable where services are duplicative |
| WHT interaction | Payments to non-resident affiliates subject to Art 56 WHT at 20% (before treaty relief) |
| Documentation | FAR analysis; benefit test; cost allocation keys; benchmarking of charge-out rates |

### 4.5 Financial Transactions / Thin Capitalisation

**Financial Transactions / Thin Capitalisation**

| Field | Detail |
| --- | --- |
| Dedicated TP guidance for financial transactions? | No (OECD TPG consulted) |
| Thin-cap rule | Law 91/2005 Art 24 — interest on loans exceeding **2× the Central Bank of Egypt (CBE) credit/discount rate** at the start of the calendar year is non-deductible |
| BEPS Action 4 implementation | Not fully implemented; Egypt relies on the Art 24 interest cap |
| Other financial rules | Art 52 (no deduction of distributions to owners); Art 56 (20% WHT on payments to non-residents) |

## Section 5 — Filing Obligations and Deadlines

### 5.1 Filing Matrix

**Filing Matrix**

| Obligation | File | Deadline |
| --- | --- | --- |
| CIT return | CITR | Within 30 April following the fiscal year-end (standard fiscal year 1 Jan – 31 Dec) unless an extension applies; ETA returns may be filed up to 30 days late with revised return (preserves Local File deadline) |
| Local File | TP documentation | **Within 2 months** of filing the CITR (or revised CITR) |
| Master File | TP documentation | Aligns with the ultimate parent's own Master File filing deadline in its home jurisdiction |
| CbCR | CbC report | **12 months** after the last day of the MNE group's reporting fiscal year |
| CbCR Notification | Notification from Egyptian subsidiaries | Due at the same time as the CIT return for the year in which the MNE group's fiscal year ends |

### 5.2 Retention and Language

**Retention and Language**

| Item | Detail |
| --- | --- |
| Documentation retention | Retain during the tax statute of limitations (5 years per Unified Tax Procedures Law; longer if audit open) |
| Language | Arabic; supplementary English accepted for MNE groups |
| Production on audit | Must be produced on ETA request; failure to produce is a basis for ETA estimation |

## Section 6 — Penalties

### 6.1 Percentage-Based TP Penalties

Egypt's TP penalty regime follows a percentage-of-transaction-value model, capped at **3% of total related-party transactions** per year (per Law 206/2020 and ETA practice):

**Percentage-Based TP Penalties**  _(per Law 206/2020 and ETA practice)_

| Violation | Penalty Rate |
| --- | --- |
| Failure to disclose related-party transactions in the tax return | **1%** of the transaction value |
| Failure to submit the Local File | **3%** of the transaction value |
| Failure to submit the Master File | **3%** of the transaction value |
| Failure to file CbCR or notification | **2%** of the transaction value |
| Aggregate cap | **3%** of total related-party transactions (per year), even if multiple violations occur |

### 6.2 General CIT Late Filing / Late Payment Penalties (Law 91/2005)

**General CIT Late Filing / Late Payment Penalties**  _(Law 91/2005 Arts 110-111)_

| Provision | Detail |
| --- | --- |
| Late filing penalty | Art 110 CIT Law — **2%/month** on tax due, from the day following the legal deadline |
| Late payment penalty | Art 111 CIT Law — **1.5%/month** from the deadline until full payment |
| TP audit-driven assessments | Adjusted tax follows general CIT penalty rules above, on top of TP percentage penalties in §6.1 |

### 6.3 Additional Risks

**Additional Risks**

| Risk | Detail |
| --- | --- |
| ETA estimation | Without sufficient documentation, the ETA may estimate arm's length prices — the burden shifts to the taxpayer to disprove the estimate |
| Reassessment window | 5 years from filing (or 6 years if fraud); extended by Unified Tax Procedures Law 206/2020 in certain cases |
| Criminal exposure | Introduced by Law 7/2025 — tax evasion including deliberate mis-statement of related-party prices may attract criminal liability; qualified professional review strongly advised |

## Section 7 — Advance Pricing Agreements (APA)

**Advance Pricing Agreements (APA)**

| Item | Detail |
| --- | --- |
| Availability | Yes — available under Ministerial Decree 221/2018 (amending Art 30 ITL) |
| Types | Unilateral, bilateral, and multilateral APAs |
| Administrator | Egyptian Tax Authority (ETA) — competent authority function |
| Bilateral / multilateral | Available through mutual agreement procedure (MAP) provisions in Egypt's tax treaties (~60 treaties) |
| Detailed administrative procedure? | No specific APA procedural regulations published; ETA discretion applies |
| Process in practice | Taxpayer files an APA request with ETA; ETA evaluates the proposed methodology and comparables; for bilateral/multilateral, ETA enters into MAP discussions with the other jurisdiction(s) |
| Duration | Typically 3-5 years (aligned with OECD practice) |
| Roll-back | Not explicitly provided for; may be negotiated with ETA on a case-by-case basis |
| Fees | No statutory fee structure; professional fees apply |
| Practical use | Limited uptake; advance tax rulings and bilateral negotiations more common in practice |

## Section 8 — Safe Harbours and Simplified Approaches

**Safe Harbours and Simplified Approaches**

| Area | Detail |
| --- | --- |
| Low-value-adding services safe harbour | **No** — full arm's length analysis required; OECD TPG Chapter VII consulted |
| Interest rate safe harbour | **No** — thin-cap governed by Art 24 (2× CBE rate) and arm's length principle; no reduced-rate safe harbour |
| Thin cap | 2× CBE credit/discount rate (cost not deductible beyond this) — a deduction cap, not a TP method |
| CbCR safe harbour | **No** — full OECD template required |
| General position | All cross-border and domestic related-party transactions must meet the arm's length standard |

## Section 9 — Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| 2005 | Law 91/2005 Art 30 enacted — Egypt becomes the first ME country with TP legislation (CUP, RPM, CPM initially) |
| 2010 | First Egyptian TP Guidelines issued (closely follow OECD TPG) |
| May 2018 | Ministerial Decree 221/2018 — added TNMM and PSM; authorised APAs; broadened scope of related-party transactions |
| May 2018 | Ministerial Decree 547/2018 — Egyptian Transfer Pricing Guidelines re-issued (modeled on OECD TPG 2017 ed.) |
| 2020 | Unified Tax Procedures Law 206/2020 — provided a single definition of related parties, CbCR filing mechanism, TP documentation framework |
| 2022 | OECD TP Country Profile — Egypt updated (confirmed the 5 methods, most-appropriate-method rule, no secret comparables) |
| 2022 | OECD TPG (January 2022 ed.) — Egypt's TPG should be updated to reflect Actions 8-10 and the 2022 changes; preparation in progress |
| 2025 | Laws 5, 6, 7 of 2025 amended CIT — verify thresholds, rates, and penalty interactions before filing |
| Ongoing | ETA building TP audit capacity; increased audit focus on royalties, management fees, and IP |
| Ongoing | CbCR used for risk assessment and audit selection; exchange of CbC reports under MCAA |

## Section 10 — Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| eg-corporate-tax | TP adjustments directly affect taxable income and CIT liability; adjustments flow through the CITR |
| eg-withholding-tax | Art 56 WHT at 20% applies to payments to non-resident affiliates (before treaty relief); royalty/interest/fees in scope |
| eg-income-tax | Related-party transactions affect individual income tax for owners/partners |
| eg-tax-optimization | TP structuring and APA considerations feed tax planning; document benefits test |
| eg-financial-statements | TP documentation builds on IFRS / Egyptian Accounting Standards-compliant records |
| eg-formation | New entities must consider TP policy from formation; related-party agreements should be in place from day one |
| transfer-pricing-workflow-base | Workflow base for this content skill — controls documentation and formatting |
| Cross-border treaty skills | Egypt's ~60 tax treaties provide WHT relief and MAP/APA pathways for related-party cross-border transactions |

## Sources

- **Law 91/2005** (Income Tax Law) Arts 24, 30, 38-40, 52, 56, 110-111 — mof.gov.eg
- **Ministerial Decree 221 of 2018** — amendment to Art 30 ITL (TP methods, APAs)
- **Ministerial Decree 547 of 2018** — Egyptian Transfer Pricing Guidelines (ETA TP circulars)
- **Unified Tax Procedures Law No. 206 of 2020** Art 1 (related-party definition), Art 12-13 (TP procedures, CbCR)
- **Executive Regulations of Law 91/2005** Arts 38, 39, 40 — TP methods, documentation, comparability
- **OECD Transfer Pricing Country Profile: Egypt (June 2022)** — oecd.org
- **OECD Transfer Pricing Guidelines (January 2022 edition)** — acknowledged by ETA as a reference
- **Andersen in Egypt "Transfer Pricing Regulations in Egypt and India" (Dec 2025)** — eg.andersen.com
- **Thomson Reuters "Egypt Enhances Transfer Pricing Rules" (Jul 2018)** — tax.thomsonreuters.com
- **PwC Worldwide Tax Summaries — Egypt** — taxsummaries.pwc.com/egypt

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

> Contributed by Ahmed Hassan.

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
