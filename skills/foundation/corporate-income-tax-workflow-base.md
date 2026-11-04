---
name: corporate-income-tax-workflow-base
description: Tier 1 workflow base for corporate income tax skills serving small, medium, and large companies across jurisdictions. Contains the workflow runbook, conservative defaults principle, structured intake form, reviewer-oriented output spec, self-checks, global refusal catalogue, citation discipline, and content skill slot contract. Workflow architecture only — no tax content, no rates, no thresholds, no form line references, no year-specific figures. MUST be loaded alongside at least one content skill that provides actual corporate income tax rules and current-year figures for a specific jurisdiction. Assumes a human reviewer credentialed under the local equivalent of Circular 230 (CPA, CA, CTA, EA, Chartered Tax Advisor, Steuerberater, expert-comptable, commercialista, etc.) reviews and signs off on every output before it reaches the taxpayer or the tax authority.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
category: foundation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Corporate Income Tax Workflow Base

## Corporate Income Tax Workflow Base v0.1

## What this file is

This is the **Tier 1 workflow base** for any corporate income tax content skill. It does not contain country-specific tax rules. It contains:

- The standard runbook for preparing a corporate income tax computation, return, and reviewer brief
- The structured intake form for gathering inputs from a corporate client
- The output specification for a reviewer-ready working paper
- The global refusal catalogue — situations a content skill must escalate to a credentialed practitioner without computing
- The 18 self-checks
- The citation discipline
- The Pillar Two interaction protocol
- The slot contract that every country-level content skill must fill

**Every corporate income tax skill MUST be loaded alongside this base.**

## Section 1 — Audience and assumptions

This base assumes:

- The **taxpayer** is a **corporation** (incorporated entity) — not a partnership, trust, sole proprietorship, or individual
- The **filing currency** is the corporation's functional currency
- The corporation maintains accounting records under either local GAAP or IFRS (see `ifrs-local-gaap-reconciliation.md` for reconciliation)
- A **credentialed reviewer** (CPA / CA / CTA / Steuerberater / equivalent) reviews and signs off on every output before it is filed
- The corporation is in scope for the country's general corporate income tax — NOT a special regime (banking, insurance, REIT, fund, oil and gas, mining, shipping, aviation, charity — these require sector skills)

## Section 2 — The runbook

### Step 0 — Onboarding (always first)

0. **Onboarding intake** — Run the intake form (Section 4). Confirm: - Country of incorporation - Country of tax residence (place of effective management — POEM) - Filing year-end date - Corporate size and threshold tests (small / medium / large / MNE) - Accounting framework (local GAAP / IFRS / Ind AS / etc.) - Any consolidated / group tax filing status (Organschaft, intégration fiscale, group relief, etc.) - Any in-scope regime overlays (Pillar Two, CFC, BEAT, GILTI) If any of: cross-border activities; multiple shareholders with different tax residences; loss-making with restructuring; ongoing audit; M&A in the year → flag to reviewer before computation.

### Step 1 — Reconcile accounting profit to tax profit

0. **Reconciliation walk-through** — Start from the audited / approved profit-before-tax (PBT) per the corporation's accounting framework. Walk through the adjustment categories table.

**Adjustment categories**

| Adjustment category | Direction | Example |
| --- | --- | --- |
| Non-deductible expenses | Add back | Fines, penalties, certain entertainment |
| Tax-exempt income | Subtract | Inter-corporate dividends within participation exemption; certain investment income |
| Timing differences | ± | Depreciation (book vs tax), provisions, IFRS leases |
| Disallowed depreciation / interest | ± | Interest deduction limitations |
| Loss utilization | ± | Brought-forward losses; group relief |
| GAAR / anti-abuse override | If applicable | Refer to reviewer |

### Step 2 — Apply jurisdiction-specific rate

0. **Apply rate** — Apply the headline corporate income tax rate from the content skill. Where multiple rates apply (small-company rate, lower rate on first slice, surcharges), apply per the content skill's bracket schedule.

### Step 3 — Apply credits and offsets

0. **Credits and offsets** — - R&D credits (see `rd-tax-credits-matrix.md`) - Patent / IP box benefit (see `ip-patent-box-matrix.md`) - Foreign tax credits - Group relief utilisation - Withholding tax credits on receipts - Anti-double taxation relief

### Step 4 — Compute and reconcile

0. **Compute and reconcile** — - Tax liability before payments - Less: provisional / advance payments made during the year - Less: foreign tax credit utilisation - Net tax payable / refundable Reconcile to the corporation's accounting tax provision (current + deferred). Document material variances.

### Step 5 — Pillar Two overlay (if applicable)

0. **Pillar Two overlay** — If the corporation is part of an MNE group with consolidated revenue ≥ EUR 750m (or local-equivalent threshold), apply the Pillar Two analysis from `pillar-two-globe-minimum-tax.md`: - Compute Adjusted Covered Taxes - Compute GloBE Income - Compute jurisdictional ETR - Apply SBIE and de minimis - Compute Top-up Tax (IIR / UTPR / QDMTT)

### Step 6 — Cross-border overlays

0. **Cross-border overlays** — If the corporation has cross-border activity: - **Permanent establishment risk** — see `permanent-establishment-risk.md` - **Withholding tax on outbound payments** — see `withholding-tax-matrix.md` - **CFC inclusion** — apply local CFC rules - **BEPS Action 5 IP regime nexus** — see `ip-patent-box-matrix.md` - **DAC6 / MDR reporting** — see `dac6-mdr-reportable-arrangements.md` - **CbCR / Action 13** — see CbCR skill (forthcoming) - **Transfer pricing documentation** — see `transfer-pricing-workflow-base.md`

### Step 7 — Deferred tax provision

0. **Deferred tax provision** — Compute the deferred tax position under local GAAP / IFRS: - Identify all timing differences (book-tax basis differences) - Apply applicable tax rate (typically substantively enacted future rate) - Recognise DTAs to the extent recoverable - Track 5-year DTL recapture risk for Pillar Two (DTLs that do not reverse within 5 years are added back)

### Step 8 — Filing assembly

0. **Filing assembly** — Produce: - The return / forms required by the jurisdiction - The reviewer brief (Section 5) - The tax provision schedule for the audit - The tax payment schedule - The supporting documentation index

## Section 3 — Conservative defaults principle

- **Conservative defaults principle** — When uncertain about any position, choose the treatment that costs more or imposes stricter compliance, never less. Your reviewer can correct an over-conservative position. They cannot easily recover from an aggressive one. Applied to corporate income tax: - Where a deduction is uncertain → flag, do not claim - Where income classification is uncertain → use the higher-taxed classification - Where a provision could be deductible OR non-deductible → exclude from claim, document the alternative - Where an exemption is uncertain → treat as taxable - Where treaty access is uncertain → withhold at domestic rate - Where loss carryforward is uncertain → defer recognition of the DTA

## Section 4 — Structured intake form

Every corporate income tax computation begins with:

```
[BASIC INFORMATION]
1. Corporation legal name and tax ID
2. Country of incorporation
3. Country of tax residence (and any conflict with incorporation country)
4. Tax year-end (calendar year, financial year, accounting period)
5. Accounting period if shorter than 12 months (specify reason — first year, change of accounting reference date, liquidation)
6. Audit status (audited, reviewed, compiled, none) and auditor name if audited
7. Accounting framework (IFRS-IASB, IFRS-EU, local GAAP, FRS 102, Ind AS, ASBE, etc.)

[SCOPE]
8. Industry / sector — confirm not in special regime (banking, insurance, REIT, fund, oil/gas, shipping, aviation)
9. Workforce — number of employees by jurisdiction
10. Activities by country — sales, services, manufacturing, R&D, IP, finance, holding
11. Consolidated group status — is this entity part of a wider group? Top parent identity and country
12. Group's consolidated revenue (for Pillar Two scope test)

[OWNERSHIP]
13. Shareholders — name, country of residence, % held, voting rights
14. Subsidiaries — name, jurisdiction, % held, activity
15. Major intra-group flows — IP licenses, services, finance, goods
16. Permanent establishments in other jurisdictions

[PRIOR YEAR]
17. Brought-forward losses (by category and country)
18. Brought-forward credits (R&D, FTC, etc.)
19. Capital allowances pools and depreciation schedules
20. Provisional payments made in current year

[CURRENT YEAR]
21. Material new positions taken (M&A, restructuring, asset disposal, new operations)
22. Tax authority interactions in the year (audit, ruling, MAP, APA)
23. Known controversies or open assessments
24. DAC6 / MDR / similar disclosures filed in the year

[CONFIRMATIONS]
25. The user confirms they will have the output reviewed by a credentialed practitioner before filing
26. The user confirms they have the authority to provide the data above
```

## Section 5 — Output specification

Every corporate income tax skill must produce a reviewer brief containing:

```
1. Executive summary (1 page)
   - Tax position: total liability, refunds, balance due
   - Year-over-year movement and key drivers
   - Reviewer attention items (flagged [T2] or [T3])

2. Computation walk-through
   - Profit before tax (per audited financials)
   - Reconciliation to taxable profit (line-by-line adjustments with citations)
   - Tax at headline rate
   - Credits and offsets
   - Net tax liability

3. Cross-border / Pillar Two analysis (if applicable)
   - Permanent establishment risk
   - Transfer pricing position
   - Withholding tax on outbound payments
   - Pillar Two scope, ETR, Top-up Tax

4. Deferred tax provision
   - All timing differences with measurement
   - DTA recoverability assessment
   - 5-year recapture risk register

5. Supporting schedules
   - Capital allowances / depreciation
   - Brought-forward losses and credits
   - Foreign tax credit utilisation
   - Group relief flows
   - GAAR risk register

6. Reviewer questions
   - All [T2] items requiring reviewer judgement
   - All [T3] items requiring escalation

7. Filing assembly
   - Forms required
   - Supporting documentation index
   - Payment schedule
```

## Section 6 — Global refusal catalogue

Refuse to compute and escalate to a credentialed practitioner if:

- **R-CIT-1** — Corporation is a regulated financial institution (bank, insurer, asset manager, fund) — load sector skill
- **R-CIT-2** — Corporation is a REIT or property collective investment vehicle — load sector skill
- **R-CIT-3** — Corporation is in extractive industries with country-by-country reporting under EU CbCR Directive — load sector skill
- **R-CIT-4** — Corporation is in shipping / aviation tonnage tax regime — load sector skill
- **R-CIT-5** — Corporation is a charity / nonprofit — load nonprofit skill
- **R-CIT-6** — Tax authority is currently auditing or has issued a notice of deficiency — controversy strategy first
- **R-CIT-7** — The user is requesting an aggressive position (GAAR risk) — reviewer must approve
- **R-CIT-8** — M&A transaction with material tax-free reorganisation election — reviewer must approve
- **R-CIT-9** — The corporation's tax residence is in dispute (POEM, treaty tie-breaker) — escalate
- **R-CIT-10** — The corporation is in liquidation or insolvency — separate procedural rules
- **R-CIT-11** — The Pillar Two threshold is met but the country has not yet enacted Pillar Two — escalate, complex
- **R-CIT-12** — The corporation has dual-resident status or hybrid mismatches — escalate

**Global refusal catalogue table**

| Refusal | Trigger |
| --- | --- |
| **R-CIT-1** | Corporation is a regulated financial institution (bank, insurer, asset manager, fund) — load sector skill |
| **R-CIT-2** | Corporation is a REIT or property collective investment vehicle — load sector skill |
| **R-CIT-3** | Corporation is in extractive industries with country-by-country reporting under EU CbCR Directive — load sector skill |
| **R-CIT-4** | Corporation is in shipping / aviation tonnage tax regime — load sector skill |
| **R-CIT-5** | Corporation is a charity / nonprofit — load nonprofit skill |
| **R-CIT-6** | Tax authority is currently auditing or has issued a notice of deficiency — controversy strategy first |
| **R-CIT-7** | The user is requesting an aggressive position (GAAR risk) — reviewer must approve |
| **R-CIT-8** | M&A transaction with material tax-free reorganisation election — reviewer must approve |
| **R-CIT-9** | The corporation's tax residence is in dispute (POEM, treaty tie-breaker) — escalate |
| **R-CIT-10** | The corporation is in liquidation or insolvency — separate procedural rules |
| **R-CIT-11** | The Pillar Two threshold is met but the country has not yet enacted Pillar Two — escalate, complex |
| **R-CIT-12** | The corporation has dual-resident status or hybrid mismatches — escalate |

## Section 7 — 18 self-checks

Before delivering output, verify:

1. [ ] Country of tax residence confirmed against POEM and treaty tie-breaker
2. [ ] Functional currency identified per IAS 21 / ASC 830 / local GAAP
3. [ ] Audited financial statements available; opinion is unmodified or modifications documented
4. [ ] PBT starting point matches the audited financials
5. [ ] All material non-deductible items added back with citations
6. [ ] All tax-exempt income subtracted with citations
7. [ ] Depreciation reconciled: book vs tax with capital allowances schedule
8. [ ] Brought-forward losses validated against last filed return
9. [ ] Foreign tax credits supported by withholding certificates / receipts
10. [ ] Transfer pricing position documented or master / local file ready
11. [ ] Permanent establishment risk in any non-residence country assessed
12. [ ] Pillar Two scope tested if group revenue ≥ EUR 750m
13. [ ] Deferred tax: DTAs recoverable on more-likely-than-not / probable basis
14. [ ] DTL 5-year recapture register maintained for Pillar Two
15. [ ] GAAR risk identified contemporaneously, not retroactively
16. [ ] DAC6 / MDR / equivalent disclosure status confirmed for the year
17. [ ] Filing deadline, payment deadline, and instalment schedule plotted
18. [ ] Output flags every [T2]/[T3] item for reviewer judgement and includes the reviewer brief

## Section 8 — Citation discipline

- **Citation discipline** — Every figure in the reviewer brief must trace to: - A statutory section (e.g., IRC §163(j), CGI Article 209, KStG §8, ITA §247) - A regulatory citation (Treas. Reg., DGFiP BOI, HMRC manual, ATO PCG) - A judicial decision where positional - The corporation's accounting records line item (general ledger account, journal entry) No figure may rely on "general practice" or "common interpretation" without explicit reviewer escalation.

## Section 9 — Slot contract for country content skills

Every country-level corporate income tax content skill must populate:

```
[REGIME IDENTIFICATION]
- Jurisdiction code (ISO 3166-1 alpha-2 or jurisdiction-specific)
- Statutory framework (act name, sections)
- Tax authority name and portal
- Filing form numbers
- Filing deadline
- Payment / instalment schedule

[RATES]
- Headline corporate income tax rate
- Small company / reduced rate (if any)
- Surcharges (national / regional / sectoral)
- Reduced rates by activity (IP box, R&D, manufacturing zone)
- Branch profits tax rate

[ADJUSTMENTS]
- Statutory list of non-deductible expenses
- Statutory list of tax-exempt income (participation exemption, etc.)
- Depreciation rules (tax life vs accounting life)
- Interest deduction limitation (ATAD-equivalent, §163(j), thin cap)

[LOSSES]
- Carryforward period
- Carryforward cap (% of profit, currency cap)
- Carryback availability
- Change of ownership restrictions
- Group relief mechanism

[CREDITS]
- R&D credit (cross-ref to skill)
- Patent / IP box (cross-ref to skill)
- Foreign tax credit mechanism
- Investment credits
- Withholding tax credits

[FILING MECHANICS]
- Form numbers
- Submission portal / format
- Supporting schedules required
- Audit thresholds

[ANTI-AVOIDANCE]
- GAAR text and key tests
- CFC rules
- Hybrid mismatch rules
- BEAT / GILTI equivalent if applicable

[PILLAR TWO OVERLAY]
- QDMTT in force?
- IIR in force?
- UTPR in force?
- Domestic top-up mechanism

[CROSS-REFERENCES]
- Withholding tax matrix (this skill)
- Pillar Two (this skill)
- DAC6 / MDR (this skill if EU)
- IP box (this skill if regime exists)
- R&D credit (this skill if regime exists)
- Free zone overlay (this skill if applicable)
- Transfer pricing workflow base
```

## Section 10 — Disclaimer

This workflow base produces working papers for review by credentialed practitioners, not direct tax advice. Every output is subject to credentialed reviewer sign-off before filing or acting upon.

The most up-to-date, verified version of this workflow base is maintained at [openaccountants.com](https://openaccountants.com).
