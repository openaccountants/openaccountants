---
name: pk-return-assembly
description: Use this skill whenever asked to assemble, finalize, or package a Pakistani annual tax return. Trigger on phrases like "Pakistan tax return assembly", "FBR IRIS final filing", "year-end Pakistan", "ATL filing", "Section 114 return", "assemble Pakistan return", "finalize PK return", "Pakistan working paper", or "IRIS filing package". This is the capstone orchestrator that pulls together outputs from pk-income-tax, pk-corporate-tax, pk-withholding-tax, pk-sales-tax-federal, pk-sales-tax-services, pk-payroll-eobi, pk-cgt, and pk-formation into a single unified working paper plus payment and filing instructions. It does not recompute anything itself — it reconciles upstream outputs, builds the line-by-line IRIS working paper, generates PSID payment instructions for FBR e-payment via designated banks, and produces a reviewer brief and taxpayer action list. ALWAYS read this skill last when finalizing a Pakistani tax return.
version: 0.1
jurisdiction: PK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - pk-freelance-intake
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PK Return Assembly

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

**When this skill is invoked, the user has already passed through intake and the relevant content skills. They want their finished IRIS working paper. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask "do you want me to assemble the full package".** The user asked for the return. Produce it.
- **Do NOT re-interrogate the user about residency, NTN, CNIC, or business structure** — intake already captured this; trust the upstream packages.
- **Do NOT pause between reconciliation steps to check in.** Run all cross-checks in sequence; flag failures in the reviewer brief and continue.
- **Self-checks are targets, not blockers.** If a check fails, note it under "Reviewer Attention Flags" and continue.
- **Do NOT submit anything to FBR IRIS.** This skill produces a working paper plus filing instructions. A credentialed reviewer (ICAP CA, ICMAP, or ACCA-PK with Pakistan practising rights) must review, and the taxpayer (or authorised filer / e-intermediary) submits via IRIS.

**If you feel the urge to ask "how should I proceed", pick the most defensible path, proceed, and flag the decision for the reviewer.**

## What this file is

The final capstone skill for Pakistani annual tax returns. It consumes the outputs of every other Pakistan skill and assembles a single unified working paper covering either:

- **Individual / AOP Return** — annual return under section 114 of the Income Tax Ordinance 2001, including salaried persons, sole proprietors, and Association of Persons (AOP) members
- **Company Return** — annual return under section 114 for resident companies (Private Limited, Single Member Company, Public Listed Company)

The output is a reviewer-ready package: line-by-line IRIS working paper, cross-skill reconciliation table, payment instructions (PSID via IRIS → CPR via designated banks), filing instructions, reviewer checklist, taxpayer action list, ATL update note, and 2026-27 planning notes.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Islamic Republic of Pakistan |
| Tax authority | Federal Board of Revenue (FBR) |
| Filing portal | IRIS — https://iris.fbr.gov.pk |
| Currency | PKR (Pakistani Rupee / Rs) |
| Tax year (normal) | 1 July – 30 June (Tax Year 2026 = 1 Jul 2025 – 30 Jun 2026) |
| Current tax year | 2026 (TY 2025-26); filing window opens July 2026 |
| Individual / AOP return | Income Tax Return under section 114 (IRIS form 114(1)) |
| Salaried return (simplified) | IRIS salaried form (section 114) |
| Company return | Income Tax Return for Companies under section 114 (IRIS form 114(1)) |
| Wealth statement | Section 116 — mandatory for all resident individuals filing a return |
| Sales tax return | STR-7 (monthly) via IRIS / e.FBR |
| Confirmation receipt | IRIS acknowledgement with submission reference and timestamp |
| Active Taxpayer List (ATL) | Updated automatically on timely filing; affects withholding rates under Tenth Schedule |
| Governing law | Income Tax Ordinance 2001; Sales Tax Act 1990; Federal Excise Act 2005; Finance Act 2025 amendments |
| Skill version | 1.0 |
| Validated by | Pending — requires sign-off by ICAP CA, ICMAP, or ACCA-PK member with Pakistan practising rights |

### 1.1 What this capstone produces

A single reviewer-ready package containing:

1. **Master working paper (Excel)** — IRIS-aligned schedules, cross-skill reconciliation, PSID register
2. **Reviewer brief (Markdown)** — executive summary, computation walk-through, positions taken, attention flags
3. **Taxpayer action list (Markdown)** — payments to make, PSIDs to generate, IRIS submission steps, deadlines, ATL implications, record retention
4. **2026-27 planning notes** — quarterly advance tax (section 147), withholding-as-collector obligations, Finance Act 2025 transitional items

## Section 2 — Required inputs from upstream PK skills

The assembly skill does not recompute anything. It expects structured outputs from the following upstream skills. If an upstream skill did not run, the assembly notes the gap and continues with available data.

### 2.1 Individual / AOP return — inputs

**Individual / AOP return — inputs table**

| Upstream skill | Output consumed | Where it lands on the IRIS return |
| --- | --- | --- |
| `pk-income-tax` | Personal income tax computation: salary, business income, property, other sources; slab-based PIT applied; surcharge and super tax where applicable | IRIS form 114(1) — main computation; Annex A (Salary), Annex B (Business), Annex E (Property), Annex F (Other sources) |
| `pk-withholding-tax` | Withholding suffered by the taxpayer (sections 149–158, 231A, 231B, 233, 235, 236 series) with CPSR / CPR references | Adjustable tax schedule (Annex G / tax payments tab) |
| `pk-sales-tax-federal` | Sales tax registrations, output and input tax positions (cross-check only, does not flow to income tax return) | Cross-check vs. business turnover |
| `pk-sales-tax-services` | Provincial sales tax on services (PRA / SRB / KPRA / BRA) — cross-check vs. service revenue | Cross-check only |
| `pk-payroll-eobi` | EOBI contributions, salary tax withheld, monthly statements u/s 165 | Cross-check to Annex A (Salary) and to amounts withheld disclosure |
| `pk-cgt` | Capital gains on securities (section 37A), immovable property (section 37(1A)), other capital assets | Annex D (Capital gains) |
| `pk-formation` | Entity structure, NTN, CNIC, AOP partnership deed, partner share ratios | Identification block; AOP partner share allocation |

### 2.2 Company return — inputs

**Company return — inputs table**

| Upstream skill | Output consumed | Where it lands on the IRIS return |
| --- | --- | --- |
| `pk-corporate-tax` | Corporate income tax computation: accounting profit → taxable income via tax adjustments; CIT at 29% (or banking / SME / small company rates); super tax under section 4C; minimum tax under section 113; alternative corporate tax under section 113C | IRIS company return — main computation; Tax adjustments schedule |
| `pk-withholding-tax` | Withholding suffered (advance tax credits) and withholding agent obligations (sections 149–158, 231A series) | Tax credits schedule; cross-check to monthly statements u/s 165 |
| `pk-sales-tax-federal` | Output and input sales tax; sales tax return reconciliation | Cross-check vs. financial statements revenue |
| `pk-sales-tax-services` | Provincial sales tax on services across PRA / SRB / KPRA / BRA | Cross-check only |
| `pk-payroll-eobi` | Employee salary expense, salary tax withheld u/s 149, EOBI contributions, monthly statements u/s 165 | Schedule of employees; cross-check to financial statements salary expense |
| `pk-cgt` | Capital gains on disposals; treatment of listed securities (section 37A) vs. other assets (section 37) | Capital gains schedule |
| `pk-formation` | NTN, incorporation details, share capital, directors, registered address; SECP CUIN | Identification block; directors schedule |

### 2.3 Intake-required identifiers

**Intake-required identifiers table**

| Identifier | Required for |
| --- | --- |
| NTN (National Tax Number) — 7 digits + check digit, or 13-digit CNIC-as-NTN for individuals | All returns |
| CNIC (Computerized National Identity Card) — 13 digits | Individual returns; AOP partners; company directors |
| CUIN (Corporate Universal Identification Number) — SECP | Company returns |
| IRIS user ID and password | All electronic submissions |
| STRN (Sales Tax Registration Number) — 13 digits | Sales tax cross-checks |
| Provincial registrations: PRA / SRB / KPRA / BRA reference numbers | Provincial sales tax on services cross-checks |
| Tax year (normal 1 Jul – 30 Jun, or approved special year-end) | Determines deadline |
| Residency status (resident / non-resident under section 82) | All returns |
| Filing status (salaried / non-salaried individual / AOP / company) | Determines IRIS form and deadline |

- **Missing identifier handling** — If any identifier is missing, the assembly skill flags it as "Needs Input" and produces the working paper with placeholders rather than halting.

## Section 3 — Assembly workflow

The capstone runs in seven phases. Each phase reads upstream output, runs reconciliation, and writes a section of the master working paper.

### 3.1 Phase 1 — Read intake & confirm scope

0. **Phase 1 steps** — - Confirm taxpayer type: salaried individual / non-salaried individual / AOP / company - Confirm tax year (TY 2026 = 1 Jul 2025 – 30 Jun 2026 unless special year-end approved u/s 74) - Confirm residency (section 82): for individuals, 183-day rule; for companies, incorporation or control & management in Pakistan - Confirm Finance Act 2025 applies (the Act received Presidential assent on 29 June 2025 for TY 2026)

### 3.2 Phase 2 — Income reconciliation

**Individuals — head of income table**

| Head of income (section 11) | Source upstream skill | IRIS schedule |
| --- | --- | --- |
| Salary (section 12) | pk-payroll-eobi + pk-income-tax | Annex A |
| Income from business (section 18) | pk-income-tax | Annex B |
| Income from property (section 15) | pk-income-tax | Annex E |
| Capital gains (sections 37, 37A) | pk-cgt | Annex D |
| Income from other sources (section 39) | pk-income-tax | Annex F |
| Foreign source income (section 102) | pk-income-tax | Foreign income schedule |

**Companies — items table**

| Item | Source | IRIS schedule |
| --- | --- | --- |
| Revenue and cost of sales | pk-corporate-tax | Trading account / P&L schedule |
| Operating expenses | pk-corporate-tax | P&L schedule |
| Tax adjustments (admissible / inadmissible) | pk-corporate-tax | Tax computation worksheet |
| Depreciation under Third Schedule | pk-corporate-tax | Depreciation schedule |
| Initial allowance under section 23 | pk-corporate-tax | Initial allowance schedule |
| Carry-forward losses (section 57) | pk-corporate-tax | Loss adjustment schedule |
| Capital gains | pk-cgt | Capital gains schedule |

### 3.3 Phase 3 — Tax computation

0. **Phase 3 steps** — - Apply slab rates for individuals (TY 2026 brackets per Finance Act 2025 — see pk-income-tax for current figures) - Apply 29% corporate rate (or 20% small company rate u/s 2(59A) / banking 39% / SME rates) for companies - Compute super tax under section 4C (income > Rs 150 million bands per Finance Act 2025 transitional) - Compute minimum tax under section 113 (turnover-based) — applies if higher than normal tax - Compute alternative corporate tax under section 113C - Add applicable surcharge (Finance Act 2025 transitional may introduce surcharge thresholds — confirm at filing time)

### 3.4 Phase 4 — Adjust for credits and payments

**Credits and payments table**

| Credit / payment | Source | Treatment |
| --- | --- | --- |
| Tax deducted at source (sections 149–158, 231 series) | pk-withholding-tax | Adjustable against final liability |
| Advance tax paid under section 147 | pk-income-tax / pk-corporate-tax (quarterly instalments) | Adjustable |
| Tax credit on charitable donations (section 61) | pk-income-tax | Subject to limits |
| Investment tax credit / pension fund credit (section 63 historic — now largely repealed; verify) | pk-income-tax | TBC — verify under Finance Act 2025 |
| Foreign tax credit (section 103) | pk-income-tax | Capped at PK tax on foreign source income |

### 3.5 Phase 5 — Cross-skill reconciliation

0. **Phase 5 description** — Run all cross-checks in Section 4 below. Each check is pass / fail / flagged. The output table goes into the reviewer brief.

### 3.6 Phase 6 — Payment instructions

0. **Phase 6 description** — Generate the PSID register: for each amount due (income tax balance, super tax, surcharge, monthly sales tax, payroll tax u/s 149, EOBI), produce a row with payment head, tax year, period, amount, and which IRIS module the PSID is generated from. Section 6 below details the PSID-to-CPR flow.

### 3.7 Phase 7 — Final assembly

0. **Phase 7 steps** — - Build the master Excel workbook - Write the reviewer brief - Write the taxpayer action list - Note the ATL update implication - Generate 2026-27 planning notes

## Section 4 — Working paper structure (for credentialed reviewer)

The reviewer is an ICAP CA (Institute of Chartered Accountants of Pakistan), ICMAP (Institute of Cost and Management Accountants of Pakistan), or ACCA-PK member with Pakistan practising rights. They sign off before IRIS submission.

### 4.1 Master workbook sheets

**Master workbook sheets table**

| Sheet | Contents |
| --- | --- |
| Cover | Taxpayer name, NTN, CNIC, CUIN (if company), tax year, return type, reviewer name, sign-off block |
| Identification | NTN, STRN, provincial sales tax numbers, business address, principal activity, NIC of representative |
| Computation — Income | Head-by-head income with section references |
| Computation — Tax | Slab application, super tax, minimum tax, ACT (companies) |
| Adjustable Tax | All section 149–158 / 231 series withholdings with CPR references |
| Advance Tax (Section 147) | Quarterly instalments paid, CPR references |
| Tax Credits | Charitable donations (s.61), foreign tax credit (s.103), other |
| Wealth Statement (Individuals) | Assets, liabilities, reconciliation of net wealth — section 116 |
| Wealth Reconciliation | Opening net wealth + income + gifts received − expenses − gifts paid = closing net wealth |
| Capital Gains | Listed securities (s.37A), immovable property (s.37(1A)), other (s.37) |
| Depreciation (Companies) | Third Schedule rates, initial allowance, WDV roll-forward |
| Salary Schedule | Per-employee detail (companies / AOPs with employees) |
| Sales Tax Cross-check | Federal STR-7 turnover vs. financial statements revenue; provincial sales tax on services |
| PSID Register | Every payment with head, period, amount, PSID number, CPR number, payment date |
| Cross-Check Summary | Pass/fail for each reconciliation item |
| 2026-27 Planning | Quarterly advance tax forecast, ATL implications, withholding agent obligations |

### 4.2 Cross-skill reconciliations

Cross-checks must each pass within tolerance (PKR 100 default; PKR 1,000 for companies). Failures flagged, not silently absorbed.

**Cross-check 1 — Revenue reconciliation**

| Source | Figure | Rule |
| --- | --- | --- |
| pk-corporate-tax / pk-income-tax business revenue | Top of P&L | Anchor figure |
| pk-sales-tax-federal annual output | Sum of monthly STR-7 turnover | Reconciles to revenue ± timing |
| pk-sales-tax-services aggregate (PRA/SRB/KPRA/BRA) | Sum of provincial returns | Reconciles to service revenue portion |
| Bank statement deposits | (If available) | Cross-check for cash leakage |

**Cross-check 2 — Salary withholding & EOBI**

| Source | Figure | Rule |
| --- | --- | --- |
| pk-payroll-eobi annual salary withheld u/s 149 | Sum of monthly statements u/s 165 | Anchor |
| pk-corporate-tax salary expense | Salary line in P&L | Reconciles to total gross salary |
| EOBI annual contributions | Per pk-payroll-eobi | Confirms employer contribution paid |
| Annex A (Salary) on employee individual returns | Bukti potong equivalent — sum across employees | Should reconcile to employer schedule |

**Cross-check 3 — Withholding agent obligations**

| Source | Figure | Rule |
| --- | --- | --- |
| Withholding deducted by entity on payments (s.153 supplies/services, s.155 rent, s.156 prizes, etc.) | pk-withholding-tax | Cross-check to monthly statements u/s 165 |
| Sum of CPRs for deposited withholding | PSID / CPR register | Must equal withholding declared in statements |
| Late deposit risk | Default surcharge u/s 205 — 12% per annum (or KIBOR + 3% — verify Finance Act 2025) | Flag for reviewer |

**Cross-check 4 — Advance tax under section 147**

| Source | Figure | Rule |
| --- | --- | --- |
| Quarterly advance tax paid (15 Sep, 15 Dec, 15 Mar, 15 Jun) | pk-income-tax / pk-corporate-tax | Each instalment had a CPR |
| Sum of quarterly payments | Should approximate (last year's tax × current year turnover / last year turnover) ÷ 4 | Confirms reasonable estimate |
| Default surcharge on underpaid instalment | Section 205 | Flag for reviewer |

**Cross-check 5 — Capital gains**

| Source | Figure | Rule |
| --- | --- | --- |
| pk-cgt listed securities (s.37A) gains | Net of CDC/NCCPL statement | Withholding by NCCPL is final tax for some classes (verify Finance Act 2025) |
| pk-cgt immovable property (s.37(1A)) | Per holding period | Rate depends on holding period; flag if filer status uncertain |
| Total CGT on return | Annex D | Reconciles to sum of (5a) and (5b) |

Pakistan distinguishes between "adjustable" tax (creditable against final liability) and "final tax" / "minimum tax" regimes. Misclassification is a common error.

**Cross-check 6 — Adjustable vs. final tax classification**

| Source | Figure | Rule |
| --- | --- | --- |
| Final tax items (e.g., dividend u/s 5, profit on debt u/s 7B for certain classes, exports u/s 154) | pk-withholding-tax | Not added to taxable income; tax already final |
| Adjustable items (e.g., section 153 on supplies/services for company filers) | pk-withholding-tax | Income added to taxable income; tax credited |
| Minimum tax items (e.g., section 113 turnover tax) | pk-corporate-tax | Higher of normal tax or minimum tax |

Each item must be flagged in the right column. Reviewer to verify against Finance Act 2025 reclassifications.

**Cross-check 7 — Wealth statement reconciliation (individuals)**

| Source | Figure | Rule |
| --- | --- | --- |
| Opening net wealth (prior year closing) | Last year's wealth statement | Anchor |
| Add: declared income for TY 2026 | Income from return |  |
| Add: gifts received, inheritance | Intake | Document required |
| Less: personal expenses, gifts paid | Intake |  |
| = Closing net wealth | Wealth statement | Must reconcile |

- **Unexplained accretion to wealth** — Unexplained accretion to wealth is treated as income under section 111 (unexplained income & assets). Flag any unreconciled gap.  _(Section 111)_
- **Cross-check 8 — Tolerance discipline** — For individuals: PKR 100 default tolerance. For companies: PKR 1,000 default tolerance. Discrepancies between PKR 100 and PKR 10,000 — flag and proceed. Above PKR 10,000 — raise as "Needs Input" before sign-off.

## Section 5 — Tax computation summary (PIT or CIT bottom line)

The bottom line of the return appears in the reviewer brief executive summary.

### 5.1 Individual / AOP bottom line

- **Individual / AOP bottom line formula** — Total taxable income (after all adjustments)         PKR X Tax on taxable income per slab                       PKR X Plus: Super tax (s.4C, if income > threshold)        PKR X Plus: Surcharge (Finance Act 2025 transitional)      PKR X (TBC) Less: Tax credits (s.61 etc.)                        PKR X = Gross tax liability                                PKR X Less: Adjustable tax withheld (s.149–158, 231)       PKR X Less: Advance tax paid (s.147 — four quarters)       PKR X Less: Foreign tax credit (s.103)                     PKR X = Net tax payable / (refundable)                     PKR X

### 5.2 Company bottom line

- **Company bottom line formula** — Accounting profit before tax                         PKR X Plus / less: Tax adjustments                         PKR X = Taxable income                                     PKR X Tax at 29% (or applicable rate)                      PKR X Plus: Super tax (s.4C bands)                         PKR X Higher of: above vs. minimum tax (s.113) vs. ACT     PKR X Less: Tax credits                                    PKR X = Gross tax liability                                PKR X Less: Adjustable tax withheld                        PKR X Less: Advance tax paid (s.147)                       PKR X = Net tax payable / (refundable)                     PKR X

### 5.3 Refund treatment

If net is refundable: claim is made in the IRIS return; FBR typically processes via section 170. Refunds may take several months. Do not expect immediate disbursement.

If net is payable: must be paid via PSID before filing the return (see Section 6).

## Section 6 — Payment instructions — PSID via IRIS, CPR, e-payment

All tax payments in Pakistan flow through the PSID → CPR mechanism.

### 6.1 The PSID-to-CPR flow

1. **Log into IRIS** at https://iris.fbr.gov.pk with NTN + password
2. **Navigate to "Payments"** → "Create Payment" (some users see "e-Payments")
3. **Select tax head** — Income Tax (for annual settlement), Withholding (s.149/153/155/156 etc.), Sales Tax (STR-7), Federal Excise, etc.
4. **Select payment nature** — Admitted income tax (for return balance), advance tax (s.147), minimum tax adjustment, super tax, etc.
5. **Enter tax year, period, and amount**
6. **Generate PSID** — IRIS issues a Payment Slip ID (PSID), valid for a defined window (typically 7 days, varies by tax head)
7. **Pay via designated bank** — present PSID at any branch of a National Bank of Pakistan (NBP), State Bank of Pakistan (SBP) authorised branch, or any Scheduled Bank linked to FBR (1Link), via:
   - Bank teller (cash/cheque)
   - Internet banking (most major banks have an FBR tab)
   - Mobile banking
   - ATM (1Link enabled)
8. **Receive CPR** — Computerized Payment Receipt — this is the legal proof of payment
9. **CPR auto-feeds to IRIS** — appears against the taxpayer's NTN ledger; the PSID closes
10. **Reference the CPR in the return** — CPRs are auto-populated for many heads but verify before submission

### 6.2 Common tax heads / PSID nature mapping

> **TBC — verify current PSID dropdown options in IRIS at the time of payment.** The list below is the conventional 2024-25 mapping; Finance Act 2025 may have introduced reclassifications. Always confirm against the live IRIS dropdown.

**Tax head / PSID nature mapping table**

| Tax head | IRIS payment nature | Used for |
| --- | --- | --- |
| Income Tax — Annual | Admitted Income Tax on return / Tax demanded | Annual return balance for individuals, AOPs, companies |
| Income Tax — Advance | Advance Tax u/s 147 | Quarterly instalments |
| Income Tax — Super Tax | Super Tax u/s 4C | Income > threshold |
| Income Tax — Minimum Tax | Minimum Tax u/s 113 | Turnover-based |
| Withholding Tax | Section-specific (149 salary, 153 supplies/services, 155 rent, 156 prizes, 231A cash withdrawal, 236 various) | Monthly withholding by withholding agent |
| Sales Tax — Federal | STR-7 monthly | FBR sales tax |
| Sales Tax — Services PRA | PRA portal — separate from IRIS | Punjab services |
| Sales Tax — Services SRB | SRB portal — separate | Sindh services |
| Sales Tax — Services KPRA | KPRA portal — separate | KP services |
| Sales Tax — Services BRA | BRA portal — separate | Balochistan services |
| Federal Excise | FED on services / goods | Limited services (some banking, telecom) |
| Capital Value Tax (CVT) | Section 8 of Finance Act 1989 / Finance Act 2022 | Certain assets |

### 6.3 Payment timing relative to filing

**Payment timing table**

| Payment | Due date | Filing reference |
| --- | --- | --- |
| Annual income tax balance — individuals | **Before filing** the s.114 return | Adjustable against the return |
| Annual income tax balance — companies | **Before filing** the s.114 return | Adjustable against the return |
| Q1 advance tax (TY 2027) | 15 September 2026 | Section 147 |
| Q2 advance tax (TY 2027) | 15 December 2026 | Section 147 |
| Q3 advance tax (TY 2027) | 15 March 2027 | Section 147 |
| Q4 advance tax (TY 2027) | 15 June 2027 | Section 147 |
| Monthly withholding | 7th of following month (private sector) / 15th (government) — verify u/s 158 | Section 165 statement |
| Monthly sales tax | 18th of following month | STR-7 |

- **CPR before return submission rule** — The CPR must exist before the s.114 return is submitted, otherwise the credit cannot be applied against the demand on the return.

### 6.4 Default surcharge on late payment

**Default surcharge table**

| Item | Rate | Section |
| --- | --- | --- |
| Default surcharge on late tax payment | KIBOR + 3% per annum (or 12% as fixed — verify Finance Act 2025) | Section 205 |
| Penalty for non-payment of advance tax | Same surcharge | Section 205(1B) |
| Late filing of return | Penalty per section 182 (table) — minimum Rs 10,000 to Rs 50,000+ depending on filer category | Section 182 |
| Late statement u/s 165 | Penalty per section 182 — Rs 5,000 to Rs 50,000+ | Section 182 |

## Section 7 — Filing instructions — IRIS

### 7.1 Filing channel

- **Filing channel** — All Pakistani income tax returns are filed electronically through **IRIS** (https://iris.fbr.gov.pk). Manual paper returns are not accepted for normal taxpayers.

### 7.2 Filing channels by taxpayer type

**Filing channels by taxpayer type table**

| Taxpayer type | IRIS form | Notes |
| --- | --- | --- |
| Salaried individual (salary ≥ 75% of taxable income) | Salaried return (simplified) | Pre-populated from employer's s.165 statements where possible |
| Non-salaried individual (business income) | 114(1) full | Includes wealth statement (s.116) |
| AOP | 114(1) for AOP | Each partner separately files their individual share |
| Private Limited / SMC | Company return 114(1) | Includes financial statements upload |
| Public Listed Company | Company return 114(1) | Includes audit report upload |
| Non-profit organisation (s.2(36) approved) | Specific NPO return | Approval certificate required |

### 7.3 Submission steps

1. **Pay first** — all admitted tax must be settled (CPRs issued) before submission
2. **Log into IRIS** (NTN + password; companies may use a representative login)
3. **Navigate to "Declaration"** → "114(1) — Return of Income"
4. **Pre-fill check** — IRIS pre-populates certain fields from CPRs and s.165 statements; verify each against the working paper
5. **Upload supporting documents** as required:
   - Audited / unaudited financial statements (companies)
   - Auditor's report (where audit required under Companies Act 2017)
   - Wealth statement (individuals — section 116)
   - Wealth reconciliation
   - Schedule of foreign income and foreign assets (if applicable, sections 116A and 165B)
6. **Validate** — IRIS runs schema and arithmetic checks; resolve any errors
7. **Submit** — receive IRIS acknowledgement with submission reference and timestamp
8. **Save acknowledgement** — this is the legal proof of filing and must be retained

### 7.4 Deadlines (tax year 2026 = 1 Jul 2025 – 30 Jun 2026)

**Deadlines table**

| Filer type | Deadline | Statutory basis |
| --- | --- | --- |
| Salaried / non-salaried individual | **30 September 2026** | Section 118(2A) ITO 2001 |
| AOP | **30 September 2026** | Section 118(2A) |
| Company with year ended 30 June | **31 December 2026** | Section 118(2)(a) — six months after year-end (or 31 December, whichever earlier — verify Finance Act 2025) |
| Company with special year-end (e.g., December) | Six months after year-end | Section 118(2) |
| Sales tax — monthly | 18th of following month | Sales Tax Act 1990 |
| Withholding statement u/s 165 — quarterly | Within 30 days of quarter-end | Section 165 |
| Wealth statement (individuals) | Filed with the return | Section 116 |

### 7.5 Extension of time

**Extension of time table**

| Item | Mechanism |
| --- | --- |
| Extension request | Application under section 119 to Commissioner Inland Revenue (CIR) before deadline |
| Typical extension | 15–30 days; rarely more |
| Interest accrues | Default surcharge u/s 205 still applies on any underpayment |

### 7.6 Late filing penalties

**Late filing penalties table**

| Filer | Penalty | Basis |
| --- | --- | --- |
| Late filing of return | Per section 182 Sl. No. 1 — depending on tax payable; minimum Rs 10,000 to maximum Rs 50,000+ (verify Finance Act 2025 table) | Section 182 |
| Non-filer becomes "non-ATL" | Withholding rates increased per Tenth Schedule (often 2x) | Tenth Schedule |
| Late wealth statement | Per section 182 Sl. No. 6 — Rs 100 per day, max Rs 50,000 | Section 182 |
| Failure to file statement u/s 165 | Per section 182 Sl. No. 4 — Rs 5,000 to Rs 50,000+ | Section 182 |

### 8.1 What is ATL?

- **ATL definition** — The **Active Taxpayer List (ATL)** is published by FBR weekly. A person appears on the ATL if they have filed their s.114 return for the most recent tax year by the deadline (or by a stipulated grace cut-off).

### 8.2 ATL implications

- **On ATL:** Lower withholding rates apply (normal rates per Division & Part of First Schedule)
- **Not on ATL:** Increased withholding under the **Tenth Schedule** — frequently 2x the normal rate (some items 4x). Examples:
  - Cash withdrawal (s.231A): Filer 0.6% — non-filer rate per Tenth Schedule
  - Vehicle registration / token tax (s.231B / 234): Filer vs. non-filer differentials
  - Property transfer (s.236C / 236K): Filer vs. non-filer differentials
  - Banking transactions (various 236 series items)

### 8.3 How the return updates ATL

- File s.114 return by deadline → name appears in next ATL update (typically within 1–2 weeks)
- File late but within grace period → may still appear, possibly with surcharge for ATL late inclusion (Rs 1,000 individual / Rs 10,000 AOP / Rs 20,000 company — verify current schedule)
- ATL effective period: 1 March to 28/29 February of following year (e.g., ATL TY 2025 effective 1 March 2026 – 28/29 February 2027)

### 8.4 Action list item

Every return assembly package must include in the action list:

```
ATL implication:
- Filing on time (by [deadline date]) → ATL active for period [1 March 2027 – 28/29 February 2028]
- Late filing → withholding rates double under Tenth Schedule until ATL reactivation surcharge paid
- Surcharge for ATL late activation (TY 2026): Rs [TBC — verify current schedule] for [filer category]
```

### 9.1 Bracket changes

- **Bracket changes note** — The Finance Act 2025 amended Personal Income Tax slabs and corporate rates effective TY 2026. The pk-income-tax skill carries the current bracket table. The capstone references but does not duplicate it. **Confirm at time of computation** that pk-income-tax is on the Finance Act 2025 brackets, not the prior year's.

### 9.2 Super tax bands (Section 4C)

Section 4C super tax applies to high-income persons and certain sectors. Finance Act 2025 may have restructured the bands. The pk-corporate-tax and pk-income-tax skills hold the current rate table. Confirm at computation time. Typical bands historically:

**Super tax bands table**

| Income band | Super tax rate |
| --- | --- |
| Up to Rs 150 million | 0% |
| Rs 150–200 million | 1% |
| Rs 200–250 million | 2% |
| Rs 250–300 million | 3% |
| Rs 300–350 million | 4% |
| Rs 350–400 million | 6% |
| Rs 400–500 million | 8% |
| Above Rs 500 million | 10% |

**TBC — verify against Finance Act 2025 because bands and rates may have shifted.**

### 9.3 Surcharge thresholds

- **Surcharge thresholds note** — Finance Act 2025 introduced / revised surcharges on high-income individuals. The pk-income-tax skill carries the current surcharge mechanism. Confirm at computation time.

### 9.4 Quarterly advance tax plan for TY 2027

The capstone produces a quarterly schedule:

**Quarterly advance tax plan table**

| Quarter | Due date | Amount |
| --- | --- | --- |
| Q1 | 15 September 2026 | (1/4 of estimated tax) |
| Q2 | 15 December 2026 | (1/4 of estimated tax) |
| Q3 | 15 March 2027 | (1/4 of estimated tax) |
| Q4 | 15 June 2027 | (1/4 of estimated tax) |

- **Estimated tax formula** — Estimated tax for TY 2027 = (Last assessed tax × current year turnover / last year turnover), or any reasonable basis under section 147(4A).  _(Section 147(4A))_

### 9.5 Withholding agent obligations for TY 2027

If the taxpayer (especially a company) is a withholding agent under sections 153, 155, 156, etc.:

- File monthly statements u/s 165 (or quarterly under section 165(1) for some classes — verify Finance Act 2025)
- Deposit withholding by 7th of following month (private sector)
- Issue withholding certificates to deductees per section 164

### 9.6 Sales tax planning

- Federal STR-7 monthly: due by 18th
- Provincial sales tax on services: each province has its own portal and due date (typically 15th – 21st)
- Annual sales tax reconciliation: not a separate form, but auditor and reviewer should reconcile annual STR-7 totals to financial statements revenue

### 9.7 Sector-specific considerations

**Sector-specific considerations table**

| Sector | Note |
| --- | --- |
| Banking | 39% CIT (or higher); section 4 framework |
| Insurance | Fourth Schedule special regime |
| Petroleum exploration | Fifth Schedule special regime |
| Power generation | Profits exempt under certain regimes (verify) |
| Export sales | Section 154 — final tax regime (1% of export proceeds, verify Finance Act 2025) |
| IT / ITeS exports | Concessional regime under specific clauses (verify under Finance Act 2025 — partial taxability shifts have occurred) |

## Section 10 — Reviewer attestation block

The reviewer brief contains an attestation block:

```markdown
# Reviewer Attestation — [Taxpayer Name] — TY 2026

Reviewer name: ____________________________________
Membership body: [ ] ICAP CA   [ ] ICMAP   [ ] ACCA-PK with Pakistan practising rights
Membership number: ____________________________________
Date of review: ____________________________________

I have reviewed:
[ ] Income computation per pk-income-tax / pk-corporate-tax
[ ] Withholding schedule per pk-withholding-tax with CPR verification
[ ] Sales tax cross-check per pk-sales-tax-federal / pk-sales-tax-services
[ ] Payroll & EOBI per pk-payroll-eobi
[ ] Capital gains per pk-cgt
[ ] Entity records per pk-formation
[ ] Wealth statement (individuals)
[ ] Cross-skill reconciliations within tolerance
[ ] All positions taken have legislative citations
[ ] ATL implication noted

Sign-off: ____________________________________

I confirm the return is ready for IRIS submission and that the taxpayer / authorised filer has been provided with the action list and PSID register.
```

## Section 11 — Final taxpayer action list template

```markdown
# Action List — [Taxpayer Name] — TY 2026

## Immediate (before s.114 return filing)

### For individuals / AOPs — deadline 30 September 2026:
1. Generate PSID for income tax balance of PKR X (Tax head: Income Tax — Annual; Period: TY 2026) in IRIS
2. Pay via 1Link bank channel (internet/mobile banking) or NBP branch; obtain CPR
3. Verify all monthly withholdings (June 2026 final month) deposited and reflected in IRIS ledger
4. Verify all s.147 quarterly advance tax instalments (Sep 2025, Dec 2025, Mar 2026, Jun 2026) have valid CPRs
5. Upload financial statements (if required), wealth statement, wealth reconciliation
6. Submit s.114 return in IRIS → save acknowledgement
7. Confirm ATL appears in next FBR weekly update

### For companies — deadline 31 December 2026 (for 30 June year-end):
1. Generate PSID for company income tax balance of PKR X (Tax head: Income Tax — Annual; Period: TY 2026)
2. Pay via 1Link / NBP; obtain CPR
3. Generate PSID for super tax (s.4C) if applicable
4. Verify all monthly withholding deposits and s.165 statements filed
5. Verify s.147 quarterly advance tax instalments paid
6. Upload audited financial statements and auditor's report
7. Submit company s.114 return in IRIS → save acknowledgement
8. File annual EOBI return (typically by employer's pension fund process)

## Monthly compliance through TY 2027

| Item | Tax head | Due |
|---|---|---|
| Withholding (s.149 salary, s.153 supplies/services, s.155 rent, etc.) | Section-specific PSID | 7th of following month |
| Monthly sales tax (STR-7) | Sales Tax — Federal | 18th of following month |
| Provincial sales tax on services (PRA / SRB / KPRA / BRA) | Province portal | Each province's calendar |
| Quarterly s.165 statement | Statement upload in IRIS | Within 30 days of quarter-end |
| EOBI contributions | EOBI portal | 15th of following month |

## Quarterly advance tax (Section 147) — TY 2027

| Quarter | Due | Estimated amount |
|---|---|---|
| Q1 | 15 September 2026 | PKR X |
| Q2 | 15 December 2026 | PKR X |
| Q3 | 15 March 2027 | PKR X |
| Q4 | 15 June 2027 | PKR X |

## Record retention

Per section 174 ITO 2001, records must be retained for **6 years** from end of the tax year (longer if assessment under reassessment proceedings). Records include:
- Books of account (general ledger, cash book, sales register, purchase register)
- CPRs (Computerized Payment Receipts)
- IRIS submission acknowledgements
- Withholding certificates issued and received
- Sales tax invoices and STR-7 acknowledgements
- Bank statements
- Wealth statement supporting (individuals)
- Financial statements and auditor's reports (companies)

Records must be kept in Pakistan or in a manner accessible to the Commissioner. Electronic records permitted under section 174(2A).
```

## Monthly compliance through TY 2027

**Monthly compliance table**

| Item | Tax head | Due |
| --- | --- | --- |
| Withholding (s.149 salary, s.153 supplies/services, s.155 rent, etc.) | Section-specific PSID | 7th of following month |
| Monthly sales tax (STR-7) | Sales Tax — Federal | 18th of following month |
| Provincial sales tax on services (PRA / SRB / KPRA / BRA) | Province portal | Each province's calendar |
| Quarterly s.165 statement | Statement upload in IRIS | Within 30 days of quarter-end |
| EOBI contributions | EOBI portal | 15th of following month |

## Quarterly advance tax (Section 147) — TY 2027

**Quarterly advance tax table**

| Quarter | Due | Estimated amount |
| --- | --- | --- |
| Q1 | 15 September 2026 | PKR X |
| Q2 | 15 December 2026 | PKR X |
| Q3 | 15 March 2027 | PKR X |
| Q4 | 15 June 2027 | PKR X |

## Section 12 — Refusals

- **R-PK-ASM-1** — Upstream skill did not run. Name the missing skill. Continue with available data; flag the gap; do not fabricate the missing computation.
- **R-PK-ASM-2** — Upstream self-check failed. Note the specific check; continue but flag.
- **R-PK-ASM-3** — Cross-skill reconciliation > PKR 10,000. Raise as "Needs Input"; do not silently round.
- **R-PK-ASM-4** — Out of scope: petroleum exploration (Fifth Schedule), insurance (Fourth Schedule), banking (specialised rules), modarabas, mutual funds, oil & gas concession agreements, group taxation under section 59AA / 59B, controlled foreign company rules (section 109A), tax holidays under Second Schedule clauses, special zones (Gwadar Free Zone, Khyber Pakhtunkhwa Special Economic Zones), agricultural income (provincial), provincial taxes other than sales tax on services. Flag for human specialist; do not attempt.
- **R-PK-ASM-5** — Out of scope: non-resident individuals, mixed-residency years, expatriate package taxation under section 12(2), Pakistan-source income for non-residents requiring section 152 final tax analysis. Refer to a specialist; this skill assumes full-year Pakistani tax residency unless explicitly handled by pk-income-tax with non-resident schedules.
- **R-PK-ASM-6** — Intake incomplete. Name the missing intake field (NTN, CNIC, CUIN, STRN, IRIS credentials, residency status). Cannot finalise the return until provided.
- **R-PK-ASM-7** — Asked to submit to IRIS. This skill produces a working paper. Submission is the taxpayer's (or their authorised filer's / e-intermediary's) action, after credentialed reviewer sign-off. Decline politely; provide the filing instructions instead.
- **R-PK-ASM-8** — Asked to confirm rates / brackets / thresholds against Finance Act 2025 without verification. Defer to pk-income-tax / pk-corporate-tax which carry the verified Finance Act 2025 figures. Flag any figure used here as "verify against current upstream skill output".

## Section 13 — Self-checks

**Check PK-ASM-1** — All upstream skills required for the chosen form have produced output, or the gap is flagged.

**Check PK-ASM-2** — Revenue reconciles between pk-corporate-tax / pk-income-tax, pk-sales-tax-federal, and pk-sales-tax-services within tolerance.

**Check PK-ASM-3** — Withholding tax credits sum correctly across s.149/153/155/156/231A/231B/233/235/236 series, with each credit backed by a CPR visible in the IRIS ledger.

**Check PK-ASM-4** — Section 147 quarterly advance tax instalments are present and reconcile to CPRs.

**Check PK-ASM-5** — Salary withholding (s.149) and EOBI ties to pk-payroll-eobi monthly statements u/s 165.

**Check PK-ASM-6** — For companies: tax adjustments (book to tax) are itemised with legislative basis (admissible / inadmissible per ITO sections).

**Check PK-ASM-7** — Capital gains correctly split between s.37A (listed securities), s.37(1A) (immovable property), and s.37 (other).

**Check PK-ASM-8** — Adjustable vs. final vs. minimum tax classifications are correctly applied per Finance Act 2025.

**Check PK-ASM-9** — Wealth statement (individuals) reconciles within tolerance; any unexplained accretion flagged under s.111.

**Check PK-ASM-10** — Super tax (s.4C) and any applicable surcharge are computed using the figures from pk-income-tax / pk-corporate-tax (not duplicated here).

**Check PK-ASM-11** — Minimum tax (s.113) and alternative corporate tax (s.113C) considered for companies; higher of normal / minimum / ACT applied.

**Check PK-ASM-12** — ATL implication note included in the action list with exact ATL effective period.

**Check PK-ASM-13** — Filing deadline (30 September or 31 December 2026) is explicitly stated in the action list with the correct date.

**Check PK-ASM-14** — Record retention period (6 years per s.174) is stated.

**Check PK-ASM-15** — Reviewer brief contains legislation citations (ITO 2001 sections, Sales Tax Act 1990 sections, Finance Act 2025 for amendments) for every position taken.

**Check PK-ASM-16** — IRIS submission acknowledgement retention is included in the action list.

**Check PK-ASM-17** — Credentialed reviewer (ICAP CA / ICMAP / ACCA-PK) sign-off requirement is stated in the executive summary, attestation block, and action list.

**Check PK-ASM-18** — All PSID payment heads referenced are flagged "TBC — verify in IRIS" if not directly confirmed against the current IRIS payment dropdown.

## Section 14 — Output files

The final output is **three files**:

1. **`[taxpayer_slug]_TY2026_pk_master.xlsx`** — Master workbook. Sheets per Section 4.1. Use live formulas where possible; verify no `#REF!` errors.

2. **`reviewer_brief.md`** — Markdown file with executive summary, computation walk-through, cross-check results, positions taken, attention flags, attestation block.

3. **`taxpayer_action_list.md`** — Markdown file with all Section 11 contents.

All three files are placed in `/mnt/user-data/outputs/` and presented to the user at the end.

If execution runs out of context mid-build, complete the computation work first and produce whichever formatted outputs are finished, then state clearly which deliverables are partial.

## Section 15 — Known gaps

1. PDF form filling is not automated; the reviewer or taxpayer enters values into IRIS using the working paper.
2. IRIS XML generation is not produced by this skill; integrations with ERP / third-party software handle that.
3. Audit report attachment is the taxpayer's responsibility; this skill only flags when audit is required (Companies Act 2017 thresholds).
4. Transfer pricing local file / master file content is referenced via pk-corporate-tax but not assembled here.
5. Final tax regime items (exports u/s 154, dividends u/s 5, profit on debt u/s 7B) are referenced via pk-withholding-tax but the regime-vs-normal-tax decisioning is upstream.
6. Tax holidays, Special Economic Zones, Gwadar Free Zone, and clause-by-clause exemptions in the Second Schedule are out of scope.
7. Provincial sales tax on services portals (PRA, SRB, KPRA, BRA) are referenced but each province's nuances are in pk-sales-tax-services.
8. Finance Act 2025 figures must be re-verified against pk-income-tax / pk-corporate-tax at every computation — the capstone does not carry rates.
9. Agricultural income tax is a provincial matter and is out of scope for this federal capstone.
10. Capital Value Tax (CVT), Workers Welfare Fund (WWF), Workers Profit Participation Fund (WPPF) flagged but not fully scheduled.

### Change log

- **v1.0 (May 2026):** Initial release. Modelled on id-return-assembly and us-ca-return-assembly, adapted for Pakistani s.114 returns, IRIS filing, PSID-to-CPR payment flow, ATL implications, and Finance Act 2025 transitional considerations. Coordinates eight upstream Pakistan skills.

## Section 16 — Sources

**Sources table**

| Source | Reference |
| --- | --- |
| Income Tax Ordinance 2001 | Primary income tax legislation; sections referenced throughout (s.4C, 11, 12, 15, 18, 37, 37A, 39, 57, 61, 82, 103, 109A, 111, 113, 113C, 114, 116, 118, 119, 147, 149–158, 165, 170, 174, 182, 205, 231 series, 236 series, Tenth Schedule) |
| Sales Tax Act 1990 | Federal sales tax framework; STR-7 |
| Federal Excise Act 2005 | FED on services and limited goods |
| Finance Act 2025 | Annual amendments for TY 2026 — Presidential assent 29 June 2025; verify all rates, bands, brackets against this Act |
| Companies Act 2017 | Audit requirement thresholds; SECP CUIN |
| Punjab Sales Tax on Services Act 2012 | PRA framework |
| Sindh Sales Tax on Services Act 2011 | SRB framework |
| Khyber Pakhtunkhwa Finance Act 2013 | KPRA framework |
| Balochistan Sales Tax on Services Act 2015 | BRA framework |
| Employees' Old-Age Benefits Act 1976 | EOBI framework |
| Federal Board of Revenue | https://www.fbr.gov.pk |
| IRIS portal | https://iris.fbr.gov.pk |
| PRA portal | https://www.pra.punjab.gov.pk |
| SRB portal | https://www.srb.gos.pk |
| KPRA portal | https://kpra.kp.gov.pk |
| BRA portal | https://bra.gob.pk |
| ICAP — Institute of Chartered Accountants of Pakistan | https://www.icap.org.pk |
| ICMAP — Institute of Cost and Management Accountants of Pakistan | https://www.icmap.com.pk |
| ACCA Pakistan | https://www.accaglobal.com/pk |
| Skill version | 1.0 |

## Disclaimer footer

*OpenAccountants — open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed and signed off by a credentialed reviewer (ICAP CA, ICMAP, or ACCA-PK member with Pakistan practising rights) before filing via FBR IRIS.*

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
