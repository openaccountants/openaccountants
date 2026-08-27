---
name: ng-return-assembly
description: Use this skill whenever asked to assemble, finalize, or package a Nigerian annual tax return. Trigger on phrases like "assemble Nigerian return", "Nigeria SPT package", "final review Nigerian tax", "FIRS Tax Pro-Max submission", "year-end Nigeria", "prepare CIT return", "prepare PIT return", "Nigeria filing package", "Form A annual return", "Form H1 reconciliation", or "Nigerian working paper". This is the capstone orchestrator that pulls together outputs from ng-cit, ng-personal-income-tax, ng-paye, ng-statutory-deductions, ng-wht, ng-cgt, ng-vat, ng-payroll, and ng-formation into a single unified working paper plus payment and filing instructions. It does not recompute anything itself — it reconciles upstream outputs, builds the line-by-line return working paper, generates Tax Pro-Max / Remita payment instructions, and produces a reviewer brief and taxpayer action list. ALWAYS read this skill last — it's the capstone.
jurisdiction: NG
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Omolola Fasasi
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NG Return Assembly

## Nigeria — Return Assembly (Capstone) — Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

- **Review statement** — Reviewed against the cited tax authorities by Omolola Fasasi on 2026-06-21. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.

### ng-return-assembly

- **Individual PIT (Form A) filing deadline** — 31 March (90 days after year-end)  _(PITA Section 41)_
- **Employer Form H1 (annual PAYE reconciliation) filing deadline** — 46053  _(PITA Section 81)_
- **CIT Self-Assessment Return deadline (31 December 2025 year-end)** — 6 months after FYE; 30 June 2026 for 31 Dec 2025 year-end  _(CITA Section 55)_
- **VAT monthly return deadline** — 21st of the following month  _(VAT Act Section 14)_
- **Plc CIT rate** — 30% percent (typically falls in the large-company band under NTA 2025)  _(NTA 2025)_
- **CIT rate — medium companies** — 20%  _(CITA + Finance Acts)_
- **CIT rate — small companies** — 0%  _(CITA + Finance Acts)_
- **NTA 2025 CIT changes effective date** — 46023  _(Nigeria Tax Act 2025)_
- **Tertiary Education Tax (TET) rate** — Abolished  _(Nigeria Tax Act 2025)_
- **CGT rate - companies** — 0.3  _(NIGERIA TAX ACT 2025)_
- **Employee pension contribution rate** — 8% of monthly emoluments  _(Pension Reform Act 2014)_
- **Employer pension contribution rate** — 10% of monthly emoluments  _(Pension Reform Act 2014)_
- **Total combined pension contribution rate (employer + employee)** — 18% of monthly emoluments  _(Pension Reform Act 2014)_
- **Pension remittance deadline** — Within 7 working days of salary payment  _(PRA 2014 Section 11(3))_
- **NHF contribution rate** — 2.5% of basic salary
- **NHF contribution — minimum earnings threshold** — #70,000 per month
- **ITF levy rate** — 1% of total annual payroll
- **ITF levy applicability — employee threshold** — Employers with ≥ 5 employees
- **ITF levy applicability — turnover threshold** — ≥ ₦50,000,000 turnover
- **ITF levy payment due date (2025 payroll year)** — 1 April 2026
- **NSITF contribution rate** — 1% of total monthly payroll
- **ITF levy applicability — employee threshold** — Employers with ≥ 5 employees
- **WHT rate on professional fees** — 5%
- **WHT rate on rent / royalties / dividends / interest** — 10%
- **WHT on contract payments to individuals (State IRS)** — 5%
- **Late-filing penalty for Form H1 — company employer** — ₦500,000  _(PITA Section 81(3))_
- **Late-filing penalty for Form H1 — individual employer** — ₦50,000  _(PITA Section 81(3))_
- **WHT credit note shelf life under CITA** — 6 years  _(CITA Section 78A (Finance Act 2019))_
- **WHT credit note practical verification flag age** — 3 years (flag any credit note older than 3 years for confirmation)
- **TIN digit length** — 10 digits
- **Tax year for individuals** — Calendar year: 1 January – 31 December
- **Tax year for companies** — Accounting year-end (any 12-month period)
- **NTA 2025 assent date** — June 2025  _(Nigeria Tax Act 2025)_
- **NTA 2025 key provisions effective date** — 1 January 2026  _(Nigeria Tax Act 2025)_
- **Foreign tax credit cap — individual (PIT)** — Under the Nigeria Tax Act (NTA), the cap for the Foreign Tax Credit for resident individuals (Personal Income Tax - PIT) is limited to the lower of the tax actually paid in the foreign country or the Nigerian tax attributable to that foreign incom  _(Nigeria Tax Act 2025)_
- **Foreign tax credit cap — corporate (CIT)** — there is no flat, unilateral foreign tax credit cap for Companies Income Tax (CIT)  _(Nigeria Tax Act 2025)_

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

When this skill is invoked, the user has already passed through intake and the relevant content skills. They want their finished Nigerian return working paper. Execute all steps without pausing for permission.

Specifically:

- Do NOT ask "do you want me to assemble the full package". The user asked for the return. Produce it.
- Do NOT re-interrogate the user about residency, TIN, RC number, or business structure — intake already captured this; trust the upstream packages.
- Do NOT pause between reconciliation steps to check in. Run all cross-checks in sequence; flag failures in the reviewer brief and continue.
- Self-checks are targets, not blockers. If a check fails, note it under "Reviewer Attention Flags" and continue.
- Do NOT submit anything to FIRS Tax Pro-Max or any State IRS portal. This skill produces a working paper plus filing instructions. A Chartered Accountant in Nigeria (ICAN or ANAN member) must review, and the taxpayer (or authorised filer) submits via the relevant portal.

If you feel the urge to ask "how should I proceed", pick the most defensible path, proceed, and flag the decision for the reviewer.

## What this file is

The final capstone skill for Nigerian annual tax returns. It consumes the outputs of every other Nigeria skill and assembles a single unified working paper covering either:

- Personal Income Tax (PIT) Form A — annual return for resident individuals (including sole proprietors), filed with the relevant State Internal Revenue Service (SIRS / LIRS for Lagos, FCT-IRS for Abuja, etc.) under the Personal Income Tax Act (PITA) as amended
- Companies Income Tax (CIT) Self-Assessment Return — annual return for resident companies (RC), filed with the Federal Inland Revenue Service (FIRS) under the Companies Income Tax Act (CITA) as amended, supplemented by Tertiary Education Tax (TET) under the Tertiary Education Trust Fund Act, and where applicable the new Development Levy introduced by the Nigeria Tax Act 2025

The output is a reviewer-ready package: line-by-line return working paper, cross-skill reconciliation table, payment instructions (Tax Pro-Max billing reference and Remita RRR), filing instructions for federal and state portals, reviewer checklist, and taxpayer action list.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Federal Republic of Nigeria |
| Federal tax authority | Federal Inland Revenue Service (FIRS) — soon transitioning to Nigeria Revenue Service (NRS) under NTA 2025 |
| State tax authorities | 36 State Internal Revenue Services + FCT-IRS (Lagos = LIRS, Rivers = RIRS, etc.) |
| Federal filing portal | FIRS Tax Pro-Max (https://taxpromax.firs.gov.ng) |
| Payment platform | Remita (https://www.remita.net) — Treasury Single Account (TSA) consolidation |
| Currency | NGN (Nigerian Naira / ₦) |
| Tax year | Calendar year for individuals (1 January – 31 December); accounting year-end for companies (commonly 31 December, but any 12-month period) |
| Current tax year | 2025 (filing window for Dec 2025 year-ends opens January 2026) |
| Individual return | PIT — Form A (annual income declaration), filed with State IRS |
| Corporate return | CIT Self-Assessment Return (Tax Pro-Max electronic form), filed with FIRS |
| Employer annual return | Form H1 (annual PAYE reconciliation), filed with State IRS |
| VAT return | FIRS VAT Form 002 (monthly) |
| Individual filing deadline | **31 March 2026** (PITA Section 41 — 90 days after year-end) |
| Employer Form H1 deadline | **31 January 2026** (PITA Section 81 — 31 January following year-end) |
| CIT deadline | **6 months after FYE** — for 31 December 2025 year-end, due **30 June 2026** (CITA Section 55) |
| VAT monthly deadline | **21st of following month** (VAT Act Section 14) |
| Confirmation receipt | Tax Pro-Max acknowledgement (Federal); SIRS portal acknowledgement (State); Remita RRR / e-receipt for payment |
| Governing law | Companies Income Tax Act (CITA, Cap C21 LFN 2004 as amended); Personal Income Tax Act (PITA, Cap P8 LFN 2004 as amended); Value Added Tax Act (Cap V1 LFN 2004 as amended); Capital Gains Tax Act (Cap C1 LFN 2004 as amended); Tertiary Education Trust Fund Act 2011; FIRS Establishment Act 2007; **Nigeria Tax Act 2025 (NTA 2025)** — assented June 2025, key provisions effective 1 January 2026 |
| Skill version | 1.0 |
| Validated by | Verified by Omolola Fasasi (MB058950) on 2026-06-21 |

## Section 2 — Required inputs from upstream skills

The assembly skill does not recompute anything. It expects structured outputs from the following upstream skills. If an upstream skill did not run, the assembly notes the gap and continues with available data.

### 2.1 Individual return (PIT Form A) — inputs

**Individual return (PIT Form A) — inputs table**

| Upstream skill | Output consumed | Where it lands on Form A |
| --- | --- | --- |
| `ng-personal-income-tax` | Chargeable income computation: gross income, allowable deductions, consolidated relief allowance (CRA), reliefs, PIT due at graduated rates | Form A Parts B, C, D |
| `ng-paye` | Employment income from employer Form H1; PAYE already deducted at source via monthly Form G | Form A Part B (employment income); credit for PAYE in Part D |
| `ng-statutory-deductions` | Pension (8% employee contribution), NHF (2.5%), NHIS, life assurance premium — all reducing chargeable income | Form A Part C (reliefs and allowances) |
| `ng-wht` | WHT credit notes received as a recipient (e.g., 5%/10% on professional fees, rent, royalties, dividends, interest) | Form A Part D (tax credits) |
| `ng-cgt` | Capital gains tax computation on chargeable assets disposed of in the year (10% rate under CGTA) | Filed separately on CGT return; cross-referenced in Form A net worth schedule |
| `ng-vat` | If sole proprietor is VAT-registered: monthly VAT return position; cross-check of turnover only | Cross-check, not on Form A directly |
| `ng-payroll` | Sole proprietor as employer: PAYE for staff, pension remittance, NHF — supports the H1 the proprietor files | Separate Form H1; supports Form A Part C if proprietor's own pension contribution exists |
| `ng-formation` | Business registration evidence: CAC BN number (sole proprietor) or RC number (if incorporated and individual is director); TIN | Identity section of Form A |

### 2.2 Corporate return (CIT Self-Assessment) — inputs

**Corporate return (CIT Self-Assessment) — inputs table**

| Upstream skill | Output consumed | Where it lands on the CIT return |
| --- | --- | --- |
| `ng-cit` | Adjusted profit, capital allowances claimed, taxable profit, CIT at applicable rate (30% large, 20% medium, 0% small under CITA + Finance Acts; NTA 2025 changes apply from FY 2026), Tertiary Education Tax at 3% of assessable profits, Development Levy where applicable | Tax Pro-Max CIT return Schedules |
| `ng-paye` | Employee payroll cost classification; PAYE remittance evidence | Operating expenses section; supports Form H1 filing |
| `ng-statutory-deductions` | Employer pension (10%), NHF, NHIS, ITF (1% of payroll), NSITF (1% of payroll) — all deductible business expenses | Operating expenses; ITF/NSITF compliance certificates required for CAC and tax clearance |
| `ng-wht` | WHT deducted from company on dividends/interest received and on contracts (credit notes); WHT the company remitted as a withholding agent (compliance only) | Schedule of WHT credits; reconciliation to monthly remittances |
| `ng-cgt` | CGT on chargeable assets disposed in the year (10% rate) | Separate CGT return; cross-referenced |
| `ng-vat` | Monthly VAT return position; VAT paid is not creditable against CIT; non-recoverable input VAT is a cost in the P&L | Cross-check; non-recoverable input VAT flows into P&L expenses |
| `ng-payroll` | Full payroll cost classification; supports Form H1 and monthly Form G | Operating expenses; supports H1 |
| `ng-formation` | CAC registration evidence (RC number); FIRS TIN; SCUML if applicable; ITF / NSITF compliance certificates | Identity section of CIT return; required for Tax Clearance Certificate |

### 2.3 Intake-required identifiers

**Intake-required identifiers table**

| Identifier | Required for |
| --- | --- |
| TIN (Tax Identification Number) — 10-digit, FIRS-issued for companies, JTB/State-issued for individuals (unified TIN under NTA 2025) | All returns |
| RC Number (Registration Number) — issued by Corporate Affairs Commission (CAC) for companies | CIT return |
| BN Number (Business Name) — issued by CAC for sole proprietors / partnerships | PIT return if trading under a business name |
| NIN (National Identity Number) — NIMC-issued, now linked to individual TIN | PIT return |
| Employer Code — issued by State IRS for PAYE / Form G filing | All payroll filings |
| State of Residence — determines which State IRS has jurisdiction for PIT (PITA First Schedule "place of residence" rule) | PIT return — critical, drives filing portal |
| LGA (Local Government Area) of residence | PIT return supplementary |
| Pension PIN (PenCom-issued RSA PIN) | Pension reliefs and remittance evidence |

If any identifier is missing, the assembly skill flags it as "Needs Input" and produces the working paper with placeholders rather than halting.

### 2.4 Federal vs State coordination

Nigeria has a bifurcated tax administration:

- Federal (FIRS): CIT, TET, VAT, WHT on companies, CGT on companies, Stamp Duties on certain instruments, Petroleum Profits Tax (out of scope), Development Levy (NTA 2025).
- State (SIRS): PIT including PAYE remittance, CGT on individuals, business premises levy, development levies (state), road tax, withholding tax on individuals (5% of contract payments to individuals).

The capstone produces separate filing packs for federal and state. A single individual sole proprietor may have BOTH a federal VAT obligation (FIRS) AND a PIT obligation (State IRS). The assembly cross-references both.

## Section 3 — Tax computation reconciliation

- **Reconciliation tolerance rule** — The assembly skill verifies that numbers from the upstream skills are mutually consistent. If a cross-check fails by more than ₦1,000, the discrepancy is raised in the reviewer brief — never silently rounded.

### Cross-check 1 — Revenue reconciliation (turnover ties across skills)

**Revenue reconciliation table**

| Source | Figure | Rule |
| --- | --- | --- |
| Bookkeeping / management accounts gross revenue | Total operating revenue | Anchor figure |
| `ng-vat` annual taxable supplies | Sum of monthly VAT 002 output Box | Must reconcile to bookkeeping revenue ± permitted timing differences and VAT-exempt revenue |
| `ng-cit` (corporates) / `ng-personal-income-tax` (individuals) gross income | Top line of fiscal computation | Must equal bookkeeping ± fiscal-vs-accounting adjustments |
| `ng-wht` (as recipient) — contract values from WHT credit notes received | Implicit gross from WHT credits ÷ WHT rate | Should reconcile to a subset of bookkeeping revenue |

If mismatch: Likely causes are (i) VAT-exempt or zero-rated supplies not in VAT output, (ii) cash vs accrual timing, (iii) intra-group eliminations, (iv) revenue subject to final WHT (rent, royalties to individuals) not in the same bucket.

### Cross-check 2 — Tax credits add up correctly

**Tax credits for individuals (Form A) table**

| Line | Source skill | Description |
| --- | --- | --- |
| PAYE deducted by employer(s) | ng-paye (Form H1 from employer) | Credit |
| WHT on professional fees / rent / royalties / dividends / interest received | ng-wht (credit notes) | Credit |
| Provisional tax paid (instalments under PITA Section 44) | ng-personal-income-tax | Credit |
| Foreign tax credit (where DTT exists or unilateral relief under PITA Section 38) | ng-personal-income-tax | Credit, capped at Nigerian PIT on same income |

### Cross-check 2 — Tax credits add up correctly

**Tax credits for corporates (CIT) table**

| Line | Source skill | Description |
| --- | --- | --- |
| WHT suffered on contracts, rent, dividends, interest (FIRS / SIRS credit notes) | ng-wht | Credit |
| Provisional tax / advance CIT paid | ng-cit | Credit |
| Foreign tax credit (CITA Section 44 — DTT or unilateral relief) | ng-cit | Credit, capped |
| Excess Dividend Tax (EDT) prior-year offset under CITA Section 19 | ng-cit | If applicable |

- **Credits cap and shelf-life rule** — Total credits cannot exceed tax payable for refund purposes unless excess is supported by valid FIRS/SIRS credit notes with verifiable serial numbers. WHT credit notes have a 6-year shelf life under Section 78A CITA (introduced by Finance Act 2019), but practical FIRS verification is shorter — flag any credit note older than 3 years for confirmation.  _(Section 78A CITA (Finance Act 2019))_

### Cross-check 3 — PAYE reconciliation between annual H1 and monthly Form G

**PAYE reconciliation table**

| Item | Source | Rule |
| --- | --- | --- |
| Sum of monthly Form G PAYE remitted (Jan–Dec 2025) | ng-paye / ng-payroll | Should equal total PAYE in Form H1 |
| Form H1 total PAYE | ng-paye | Annual reconciliation |
| Form H1 due date | Fixed | **31 January 2026** |
| Late-filing penalty | PITA Section 81(3) | ₦500,000 (company) or ₦50,000 (individual employer) per month |

If mismatch: Likely cause is mid-year joiners/leavers, bonus / 13th-month paid in December not captured in monthly remittance, or PAYE on benefits-in-kind only recognised at year-end.

### Cross-check 4 — Statutory deductions remittance compliance

**Statutory deductions remittance compliance table**

| Item | Source | Rule |
| --- | --- | --- |
| Pension — 18% combined (10% employer + 8% employee) of monthly emoluments | ng-statutory-deductions | Must be remitted to RSA PFA within 7 working days of salary payment (PRA 2014 Section 11(3)) |
| NHF — 2.5% of basic salary (employees earning ≥ ₦3,000/month) | ng-statutory-deductions | Remitted monthly to FMBN |
| NHIS — varies by scheme | ng-statutory-deductions | Monthly |
| ITF — 1% of total annual payroll (employers with ≥ 5 employees or ≥ ₦50M turnover) | ng-statutory-deductions | Due by **1 April 2026** |
| NSITF — 1% of total annual payroll (employers ≥ 5 employees) | ng-statutory-deductions | Monthly within 14 days; annual reconciliation |

Compliance certificates required for FIRS Tax Clearance Certificate (TCC):
- ITF Compliance Certificate
- NSITF Compliance Certificate
- PenCom Compliance Certificate
- NHF Compliance Certificate

Missing any of these blocks TCC issuance, which in turn blocks government contracts, visa applications, and bank loans. Flag any missing certificate in the reviewer brief.

### Cross-check 5 — WHT compliance as a withholding agent

**WHT compliance as withholding agent table**

| Item | Source | Rule |
| --- | --- | --- |
| WHT on contracts paid (5% companies, 5%/10% individuals) | ng-wht | Remitted monthly by 21st of following month (FIRS for companies; State IRS for individuals) |
| WHT on rent paid (10%) | ng-wht | Monthly |
| WHT on professional fees (10% individuals, 5% companies) | ng-wht | Monthly |
| WHT on dividends, interest, royalties (10%, sometimes final) | ng-wht | Monthly |
| WHT credit notes issued to suppliers | ng-wht | Must be issued promptly; failure exposes principal to disallowance of expense (Section 81 CITA / Section 73 PITA) |

- **Withholding failure penalty rule** — Withholding is the entity's obligation, not its own tax credit. Failure to withhold can result in (a) penalty of ₦500,000 (company) or ₦50,000 (individual) plus 10% of unremitted amount, and (b) disallowance of the underlying expense. Flag any apparent failure for the reviewer.  _(Section 81 CITA / Section 73 PITA)_

### Cross-check 6 — VAT-to-CIT/PIT consistency (for VAT-registered taxpayers)

**VAT-to-CIT/PIT consistency table**

| Item | Source | Rule |
| --- | --- | --- |
| Output VAT (7.5% on taxable supplies) | ng-vat | NOT income — held in trust for FIRS |
| Input VAT recoverable | ng-vat | NOT a cost in fiscal P&L — netted against output |
| Input VAT non-recoverable (e.g., on overhead before VAT Modification Order rules) | ng-vat | IS a cost in fiscal P&L |
| VAT on imported services (reverse charge per Finance Act 2020) | ng-vat | Self-account; reverse charge entries must reconcile |

If inconsistency: An expense net of VAT in the P&L while the VAT was also not claimed on the VAT return means the VAT is lost. Flag for reviewer.

### Cross-check 7 — Capital allowances (companies) and CGT (both)

**Capital allowances and CGT table**

| Item | Source | Rule |
| --- | --- | --- |
| Capital allowances claimed in CIT computation | ng-cit | Cannot exceed 66 2/3% of assessable profits for non-manufacturing companies (CITA Section 31 / Second Schedule); manufacturing companies have no cap |
| Tax Written Down Value (TWDV) roll-forward | ng-cit | Opening TWDV + additions − initial + annual allowances = closing TWDV |
| CGT on chargeable assets disposed | ng-cgt | 10% on net gain; CGTA Section 2; principal private residence and certain shares exempt |
| Roll-over relief claimed | ng-cgt | Confirm CGTA Section 32 conditions met |

Note: NTA 2025 introduces revised capital allowance rates and an updated definition of "qualifying capital expenditure" effective 1 January 2026 — this does NOT affect FY 2025 computations but must be flagged in 2026 planning.

### Cross-check 8 — Tolerance discipline

- **Tolerance discipline rule** — For every cross-check above, the threshold is ₦1,000. If a difference is between ₦1,000 and ₦100,000, document the variance and proceed with a reviewer flag. If above ₦100,000, raise as "Needs Input" — the reviewer should resolve before sign-off.

## Section 4 — Working paper template: individual PIT Form A

Form A is the annual income declaration filed with the relevant State Internal Revenue Service (the SIRS of the taxpayer's "place of residence" as defined in PITA First Schedule). For Lagos residents this is LIRS; FCT residents file with FCT-IRS; Rivers with RIRS, etc.

### 4.1 Form A — line-by-line

**Form A line-by-line table**

| Part | Line | Description | Source |
| --- | --- | --- | --- |
| **Identity** | TIN, NIN, name, BN (if applicable), address, state, LGA, marital status, dependants, employer details | All | Intake |
| **A. Gross Income** | 1 | Employment income (salary, wages, bonus, 13th-month, BIK) | ng-paye |
|  | 2 | Trade, business, profession (sole-proprietor net profit per accounts) | ng-personal-income-tax |
|  | 3 | Rental income (gross) | ng-personal-income-tax (rental subject to 10% WHT often final) |
|  | 4 | Dividends, interest, royalties (gross, before WHT) | ng-personal-income-tax |
|  | 5 | Pensions and annuities | ng-personal-income-tax |
|  | 6 | Other income | ng-personal-income-tax |
|  | 7 | **Total Gross Income** | Sum 1–6 |
| **B. Allowable Deductions** | 8 | Trade / business allowable expenses | ng-personal-income-tax |
|  | 9 | Capital allowances on business assets | ng-personal-income-tax |
|  | 10 | Other allowable deductions (interest on owner-occupied mortgage etc.) | ng-personal-income-tax |
|  | 11 | **Total Deductions** | Sum |
| **C. Reliefs & Allowances** | 12 | Consolidated Relief Allowance (CRA) — higher of ₦200,000 or 1% of gross income, plus 20% of gross income (PITA Sixth Schedule as amended by Finance Act 2020) | ng-personal-income-tax |
|  | 13 | Pension contribution (8% employee or self-employed equivalent) | ng-statutory-deductions |
|  | 14 | NHF (2.5%) | ng-statutory-deductions |
|  | 15 | Life assurance premium | ng-statutory-deductions |
|  | 16 | NHIS | ng-statutory-deductions |
|  | 17 | **Total Reliefs** | Sum |
| **D. Chargeable Income** | 18 | Line 7 − Line 11 − Line 17 | Computed |
| **E. Tax Computation** | 19 | Apply graduated PIT rates (7% / 11% / 15% / 19% / 21% / 24% — PITA Sixth Schedule) to Line 18 | ng-personal-income-tax |
| **F. Tax Credits** | 20 | PAYE deducted at source (per Form H1 from employer) | ng-paye |
|  | 21 | WHT suffered (per credit notes) | ng-wht |
|  | 22 | Provisional tax paid (instalments) | ng-personal-income-tax |
|  | 23 | Foreign tax credit (capped) | ng-personal-income-tax |
|  | 24 | **Total Credits** | Sum |
| **G. Tax Payable / Refundable** | 25 | Line 19 − Line 24 (positive = balance due; negative = refund / carry-forward) | Computed |

### 4.2 Supporting schedules

**Supporting schedules table**

| Schedule | Title | When used |
| --- | --- | --- |
| Schedule 1 | Statement of Assets & Liabilities (Net Worth Statement) | Mandatory for high-net-worth and discretionary for others — required by LIRS for income > ₦25M |
| Schedule 2 | Business income detailed P&L (sole-proprietor) | If business income on Line 2 |
| Schedule 3 | Capital allowances schedule (additions, disposals, TWDV) | If business assets |
| Schedule 4 | Rental income property-by-property breakdown | If rental income |
| Schedule 5 | WHT credit notes register (serial number, payer, date, amount) | If WHT credits claimed |
| Schedule 6 | Foreign income & foreign tax credit working | If foreign income |

### 4.3 NTA 2025 transitional note for individuals

The Nigeria Tax Act 2025 (assented June 2025) revises the PIT regime from 1 January 2026, including:
- New graduated PIT rates (0% / 15% / 18% / 21% / 23% / 25% per draft as published — confirm at FY 2026 filing time)
- New tax-free threshold of ₦800,000 annual chargeable income (replacing CRA structure)
- Rent relief of up to ₦200,000 per year
- Consolidation of the unified TIN regime
- None of these apply to the 2025 return. Flag in the 2026 planning section.

## Section 5 — Working paper template: corporate CIT Self-Assessment

Filed via FIRS Tax Pro-Max (https://taxpromax.firs.gov.ng). Tax Pro-Max generates an assessment notice, billing reference, and Remita RRR for payment.

### 5.1 CIT Self-Assessment — line-by-line

**CIT Self-Assessment line-by-line table**

| Section | Line | Description | Source |
| --- | --- | --- | --- |
| **Identity** | RC No., TIN, name, registered office, year of assessment, accounting period, principal activity | All | Intake |
| **A. Profit/Loss per Accounts** | 1 | Turnover (revenue) | Bookkeeping |
|  | 2 | Cost of sales | Bookkeeping |
|  | 3 | Gross profit | Computed |
|  | 4 | Operating expenses | Bookkeeping |
|  | 5 | Other income (non-operating) | Bookkeeping |
|  | 6 | Profit/(Loss) per accounts | Computed |
| **B. Tax Adjustments** | 7 | Add: depreciation per accounts | ng-cit (disallowed; replaced by capital allowances) |
|  | 8 | Add: disallowable expenses (donations not approved, entertainment, fines/penalties, general provisions, etc. per CITA Section 27) | ng-cit |
|  | 9 | Less: non-taxable income (dividends from Nigerian companies — franked, certain exempt) | ng-cit |
|  | 10 | Less: capital gains taxed separately under CGTA | ng-cgt |
|  | 11 | **Assessable Profit** | Computed |
| **C. Capital Allowances** | 12 | Initial allowances on qualifying capital expenditure | ng-cit |
|  | 13 | Annual allowances | ng-cit |
|  | 14 | Investment allowances (where applicable) | ng-cit |
|  | 15 | Balancing allowances / (charges) | ng-cit |
|  | 16 | **Total Capital Allowances** (capped at 66 2/3% of assessable profit for non-manufacturing; no cap for manufacturing per CITA Second Schedule) | Computed |
| **D. Loss Relief** | 17 | Brought-forward losses utilised (indefinite carry-forward under CITA Section 31, post-Finance Act 2019) | ng-cit |
| **E. Total Profit (Taxable Profit)** | 18 | Line 11 − Line 16 − Line 17 | Computed |
| **F. Tax Charge** | 19 | CIT rate applied: **0%** (small company — turnover ≤ ₦25M); **20%** (medium — ₦25M < turnover ≤ ₦100M); **30%** (large — turnover > ₦100M) per CITA Section 40 as amended by Finance Act 2019/2020 | ng-cit |
|  | 20 | CIT liability | Line 18 × rate |
|  | 21 | **Tertiary Education Tax (TET)** at **3%** of assessable profit (TET Act as amended by Finance Act 2023 — rate increased from 2.5% to 2.5% then to 3.0% under Finance Act 2023; confirm rate effective for FY 2025) | ng-cit |
|  | 22 | **Development Levy** (NTA 2025) — not applicable for FY 2025; effective FY 2026 onward at 4% of assessable profit consolidating TET, NITDA, NASENI levies | n/a for 2025 |
|  | 23 | NITDA Levy 1% (companies with turnover ≥ ₦100M, IT-related sectors) | ng-cit |
|  | 24 | NASENI Levy 0.25% (specified sectors) | ng-cit |
|  | 25 | Police Trust Fund Levy 0.005% of net profit | ng-cit |
|  | 26 | **Total Federal Tax Liability** | Sum 20–25 |
| **G. Tax Credits** | 27 | WHT suffered (credit notes) | ng-wht |
|  | 28 | Advance / provisional CIT paid | ng-cit |
|  | 29 | Foreign tax credit | ng-cit |
|  | 30 | **Total Credits** | Sum |
| **H. Net Tax Payable** | 31 | Line 26 − Line 30 | Computed |
| **I. Minimum Tax Check** | 32 | Minimum tax under CITA Section 33 (where company has no/insufficient tax payable): 0.5% of gross turnover less franked investment income, for non-exempt companies. NTA 2025 introduces **Minimum Effective Tax Rate (MEFR)** of 15% for large groups effective 2026 (out of scope for 2025) | ng-cit |

### 5.2 Supporting schedules (Tax Pro-Max attachments)

**Supporting schedules (Tax Pro-Max attachments) table**

| Schedule | Title | When used |
| --- | --- | --- |
| Schedule 1 | Audited Financial Statements (Statement of Profit or Loss, Statement of Financial Position, Statement of Cash Flows, Notes) — signed by directors + auditors (ICAN/ANAN) | Always (CITA Section 55 + CAMA 2020) |
| Schedule 2 | Detailed Tax Computation | Always |
| Schedule 3 | Capital Allowances Schedule (per asset class, with TWDV roll-forward) | Always if fixed assets |
| Schedule 4 | Loss Relief Schedule (YOA-by-YOA brought-forward losses) | If losses |
| Schedule 5 | WHT credit notes register | If WHT credits claimed |
| Schedule 6 | Related-party transactions / Transfer Pricing Declaration Form (FIRS TP Regulations 2018) | If related-party transactions exist |
| Schedule 7 | Country-by-Country Reporting notification (multinationals with consolidated revenue ≥ ₦160 billion) | If MNE |
| Schedule 8 | Donations schedule (specified Sixth Schedule beneficiaries only) | If charitable donations |
| Schedule 9 | Compliance certificates (ITF, NSITF, PenCom, NHF) | Always for TCC |

### 5.3 Tertiary Education Tax detail

- **TET detail rule** — TET is computed at 3% of assessable profit (Line 11 in 5.1), not total profit. It applies to all Nigerian-resident companies regardless of size (no small-company exemption — confirmed by Finance Act 2023). TET is administered by FIRS and paid alongside CIT through Tax Pro-Max.  _(Finance Act 2023)_

### 5.4 NTA 2025 transitional note for companies

The Nigeria Tax Act 2025 (effective 1 January 2026) introduces sweeping changes that do NOT apply to FY 2025 but must be flagged for FY 2026:

- Development Levy at 4% consolidating TET (3%), NITDA (1%), and NASENI (0.25%) into a single levy
- Small company threshold raised to ₦100M annual turnover (currently ₦25M)
- CIT rate reduced to 25% for large companies (down from 30%)
- Minimum Effective Tax Rate (MEFR) of 15% for multinational groups with ≥ €750M consolidated revenue (Pillar Two adoption)
- VAT rate to remain at 7.5% in 2026 (NTA 2025 left the rate untouched after political pushback on proposed increase)
- Nigeria Revenue Service (NRS) replaces FIRS as the federal tax authority
- Unified TIN regime
- Digital services tax updates

The 2026 planning section of the reviewer brief flags every NTA 2025 item materially affecting the taxpayer.

## Section 6 — Payment instructions: Tax Pro-Max, Remita, Treasury Single Account

Nigerian tax payments flow through the Treasury Single Account (TSA) via the Remita payment platform. The taxpayer logs into Tax Pro-Max, the system generates an assessment and an associated billing reference / Remita Retrieval Reference (RRR), the taxpayer pays the RRR via bank channel (any commercial bank, internet banking, mobile banking, USSD, or POS), and Remita issues a payment receipt that auto-feeds back to Tax Pro-Max as payment evidence.

### 6.1 Tax types and FIRS / State channels

**Tax types and FIRS / State channels table**

| Tax | Authority | Portal / Form | Payment channel |
| --- | --- | --- | --- |
| CIT | FIRS (federal) | Tax Pro-Max — CIT Self-Assessment | Remita RRR → bank → TSA |
| TET | FIRS | Tax Pro-Max — TET module | Same |
| VAT | FIRS | Tax Pro-Max — VAT Form 002 (monthly) | Same |
| WHT (companies) | FIRS | Tax Pro-Max — WHT module | Same |
| PAYE | State IRS (LIRS, FCT-IRS, RIRS, etc.) | State portal (e.g., eTax LIRS) — Form G monthly, Form H1 annual | State-specific Remita / portal payment |
| PIT (individual annual) | State IRS | State portal — Form A | Same |
| WHT (individuals) | State IRS | State portal | Same |
| CGT (companies) | FIRS | Tax Pro-Max | Same |
| CGT (individuals) | State IRS | State portal | Same |
| ITF Levy | ITF | ITF portal | Direct |
| NSITF | NSITF | NSITF portal | Direct |
| Pension | PenCom (regulator) → PFA (custodian) | RSA via PFA | Bank transfer to PFA custodian |
| NHF | FMBN | FMBN portal | Direct |

### 6.2 Tax Pro-Max → Remita → TSA flow

1. Log into Tax Pro-Max with TIN + password (or FIRS-issued digital certificate for high-volume filers)
2. Select tax type (CIT, TET, VAT, WHT) and period (year of assessment / month)
3. Enter computation OR upload XML / spreadsheet (Tax Pro-Max accepts bulk upload templates)
4. Submit — system generates Assessment Notice and Billing Reference Number (BRN)
5. Tax Pro-Max generates Remita RRR (15-digit) tied to the BRN
6. Pay the RRR via:
   - Any commercial bank teller (cash/cheque/bank transfer)
   - Internet banking (most Tier-1 banks integrate Remita)
   - Mobile banking app
   - USSD (Remita short code per bank)
   - POS at FIRS office
7. Bank confirms payment → Remita issues e-receipt with Remita Transaction Reference (RTR) + Tax Pro-Max payment evidence
8. Tax Pro-Max marks the assessment as settled; the corresponding return becomes filed (or filing is now actionable if payment was required first)

### 6.3 Tax Pro-Max payment timing relative to filing

**Payment timing relative to filing table**

| Payment | Due date | Filing reference |
| --- | --- | --- |
| CIT — FY ending 31 December 2025 | **30 June 2026** (CITA Section 55) | Self-Assessment Return |
| TET — FY ending 31 December 2025 | **30 June 2026** (paid with CIT) | Within CIT return |
| VAT monthly (December 2025) | **21 January 2026** | VAT 002 |
| WHT monthly (December 2025 deductions) | **21 January 2026** | WHT schedule |
| PAYE monthly (December 2025) | **10 January 2026** (PITA Section 81; 10th of following month) | Form G |
| PIT annual (individual) | **31 March 2026** (PITA Section 41 — 90 days after year-end) | Form A |
| Employer annual PAYE reconciliation | **31 January 2026** | Form H1 |
| ITF Levy (FY 2025) | **1 April 2026** | ITF annual return |
| NSITF (December 2025) | **14 January 2026**; annual reconciliation also due | Monthly |
| Pension (December 2025 salary) | Within 7 working days of salary payment | RSA contribution schedule |

- **Payment evidence upload rule** — For CIT, FIRS practice is to require payment evidence (RTR) to be uploaded before the Self-Assessment Return is treated as accepted. Plan to settle BEFORE the formal submission step — or in two instalments per CITA Section 77 (one with provisional return at 3 months, balance with final return).  _(CITA Section 77)_

### 6.4 Provisional / instalment CIT under CITA Section 77

- **Instalment options** — CITA Section 77 permits payment in instalments: - Option 1 (Single payment): Pay full CIT liability on filing date (or on or before due date if filing earlier) - Option 2 (Instalments): Up to 6 monthly instalments with FIRS approval; first instalment with the return, subsequent monthly. 2% interest applies on outstanding balance. For provisional tax (where statute requires), the company pays an estimate within 3 months of year-end and trues up at filing. FIRS practice is increasingly tolerant of single-payment-at-filing where the company is a "good standing" taxpayer.  _(CITA Section 77)_

### 6.5 Payment evidence to retain

**Payment evidence to retain table**

| Document | Issued by | Retain for |
| --- | --- | --- |
| Remita RRR | Tax Pro-Max | Until settled |
| Remita e-Receipt (RTR) | Remita | Indefinite — proof of payment |
| Tax Pro-Max Payment Confirmation | FIRS | Indefinite |
| Tax Clearance Certificate (TCC) | FIRS / State IRS | 12-month validity; renew annually |
| Compliance Certificates (ITF, NSITF, PenCom, NHF) | Respective agencies | 12-month validity each |

### 7.1 Federal (FIRS) filings via Tax Pro-Max

**Federal filing channels table**

| Channel | Description | Best for |
| --- | --- | --- |
| **Tax Pro-Max Web — Direct Entry** | Fill the return directly in browser | Small / medium taxpayers |
| **Tax Pro-Max Web — Bulk Upload** | Upload FIRS-template Excel / XML | Larger taxpayers, multi-line schedules |
| **Tax Pro-Max API** | Direct integration for ERP / accounting software | Big-4 / multinational filers |

Submission steps (CIT example):

1. Prepare — finalise audited accounts, sign-off by directors and external auditors (ICAN-registered)
2. Log into Tax Pro-Max (TIN + password)
3. Navigate to CIT → File Return → Year of Assessment 2026 (relating to FY 2025)
4. Enter / upload computation; attach audited financial statements (PDF), tax computation (PDF/XLSX), capital allowances schedule, and compliance certificates
5. Validate — Tax Pro-Max runs arithmetic checks; resolve errors
6. Submit return → system generates Assessment Notice + Remita RRR
7. Pay the RRR (or set up instalment plan if applicable)
8. After payment, retrieve filed-and-paid acknowledgement — this is proof of compliance and is the basis for Tax Clearance Certificate (TCC) application
9. Apply for TCC for the year (separate Tax Pro-Max workflow)

### 7.2 State (SIRS) filings — example: LIRS eTax

Each State IRS operates its own portal; LIRS is the largest. General pattern:

1. Log into State IRS portal (e.g., https://etax.lirs.net for Lagos)
2. Navigate to Annual Returns → Form A (Individuals) or Annual Returns → Form H1 (Employers)
3. Enter income, deductions, reliefs, credits
4. Upload supporting documents (payslips, WHT credit notes, business accounts for sole proprietors)
5. Submit → portal generates Assessment Notice + Remita RRR for any balance
6. Pay via Remita
7. Retrieve filing acknowledgement → basis for State TCC

### 7.3 Deadlines summary (tax year 2025 / year of assessment 2026)

**Deadlines summary table**

| Filer type | Return | Authority | Deadline |
| --- | --- | --- | --- |
| Individual (resident) | Form A (annual PIT) | State IRS | **31 March 2026** (PITA Section 41) |
| Employer | Form H1 (annual PAYE reconciliation) | State IRS | **31 January 2026** (PITA Section 81) |
| Employer | Form G (monthly PAYE) | State IRS | **10th of following month** |
| Company | CIT Self-Assessment (FY 31 Dec 2025) | FIRS | **30 June 2026** (CITA Section 55 — 6 months after FYE) |
| Company | TET (with CIT) | FIRS | **30 June 2026** |
| VAT-registered taxpayer | VAT Form 002 (monthly) | FIRS | **21st of following month** |
| Withholding agent | WHT monthly schedule | FIRS (companies) / State IRS (individuals) | **21st of following month** (FIRS) / **10th** (State) |
| Sole proprietor | Form A + Schedule 2 (business income) | State IRS | **31 March 2026** |
| ITF | Annual contribution | ITF | **1 April 2026** |
| NSITF | Annual reconciliation | NSITF | **31 March 2026** |

### 7.4 Late filing penalties

**Late filing penalties table**

| Filer | Tax | Penalty | Basis |
| --- | --- | --- | --- |
| Company | CIT late filing | ₦25,000 first month + ₦5,000 per additional month | CITA Section 55(3) |
| Company | CIT late payment | 10% of unpaid tax + interest at CBN MPR + 5% per annum | CITA Section 85 |
| Company | TET late | Same as CIT proportionally | TET Act |
| Employer | Form H1 late | ₦500,000 (corporate) / ₦50,000 (individual employer) | PITA Section 81(3) |
| Individual | Form A late | ₦5,000 + ₦100 per day of default | PITA Section 94 |
| VAT-registered | VAT late filing | ₦50,000 first month + ₦25,000 per additional month | VAT Act Section 19 (Finance Act 2020) |
| WHT | Failure to deduct/remit | 10% of unremitted amount + interest at CBN MPR + 5% | CITA Section 81 / PITA Section 73 |

### 7.5 Filing-versus-payment ordering

Unlike some jurisdictions, in Nigerian practice the assessment is generated FROM the filed return, then the Remita RRR is settled. There is no true "pay first, then file" — but for the return to be treated as substantively complete, the matching payment must be made before the deadline. Late payment penalties accrue independently of late filing penalties.

## Section 8 — Working paper structure for the credentialed reviewer

The reviewer is a Chartered Accountant in Nigeria — ICAN (Institute of Chartered Accountants of Nigeria) or ANAN (Association of National Accountants of Nigeria) member, and (for tax-specific opinions) potentially a CITN (Chartered Institute of Taxation of Nigeria) member. The reviewer brief is a single markdown file the reviewer reads before sign-off.

```markdown
# Complete Return Package — [Taxpayer Name] — Year of Assessment 2026 (FY 2025)

## Executive Summary
- Filing entity: [Individual / Sole Proprietor / Company (Small/Medium/Large per CITA)]
- TIN: [10-digit]
- RC No. / BN No.: [if applicable]
- State of Residence (individuals): [for SIRS jurisdiction]
- Tax regime: [PIT graduated rates / CIT 0% / CIT 20% / CIT 30%]
- VAT status: [Registered / Below threshold]
- Returns to be filed:
  - [ ] Form A (PIT) — State IRS — due 31 March 2026
  - [ ] Form H1 (PAYE annual) — State IRS — due 31 January 2026
  - [ ] CIT Self-Assessment — FIRS Tax Pro-Max — due 30 June 2026
  - [ ] TET — within CIT return
  - [ ] VAT 002 December — FIRS — due 21 January 2026
- Total federal tax liability: ₦X
- Total state tax liability: ₦X
- Total credits: ₦X
- Net payable / refundable: ₦X
- TCC application due: [date]

## Federal Tax Computation (CIT + TET + Levies)
[From ng-cit]
- Audited P&L reconciliation
- Tax adjustments schedule (disallowables, exempt income)
- Capital allowances schedule with TWDV roll-forward
- Loss relief schedule
- CIT at applicable rate (0% / 20% / 30%)
- TET at 3% of assessable profit
- NITDA, NASENI, Police Trust Fund Levy (where applicable)

## State Tax Computation (PIT / PAYE)
[From ng-personal-income-tax, ng-paye]
- Form A line-by-line
- Form H1 employer reconciliation
- State of residence determination (PITA First Schedule)

## Statutory Deductions Compliance
[From ng-statutory-deductions]
- Pension remittance log (PFA confirmations) — within 7 working days
- NHF monthly remittance
- ITF annual compliance certificate status
- NSITF annual compliance certificate status
- NHIS / NHIA scheme status
- PenCom compliance certificate status

## Withholding Tax (WHT)
[From ng-wht]
- As withholding agent: monthly remittance schedule, credit notes issued to suppliers
- As recipient: WHT credit notes received, serial number register, ageing analysis

## VAT
[From ng-vat]
- Monthly VAT 002 summary for 2025
- Output VAT, input VAT recoverable, net VAT remitted
- Cross-check to bookkeeping turnover

## Capital Gains Tax
[From ng-cgt]
- Disposals schedule
- Net chargeable gains at 10% CGT rate
- Roll-over relief claims

## Payroll
[From ng-payroll]
- Annual payroll summary
- BIK computation
- Payroll reconciliation to general ledger

## Formation / Compliance Identity
[From ng-formation]
- CAC RC / BN status
- TIN status (FIRS / JTB unified)
- ITF / NSITF / PenCom / NHF certificate status

## Cross-Skill Reconciliation
- Revenue reconciliation: [pass/fail]
- Tax credits add up: [pass/fail]
- PAYE annual H1 vs monthly G: [pass/fail]
- Statutory deductions remitted on time: [pass/fail]
- WHT agent compliance: [pass/fail]
- VAT-to-income consistency: [pass/fail]
- Capital allowances within Section 31 cap (non-manufacturing): [pass/fail]

## Reviewer Attention Flags
- Items requiring ICAN / CITN confirmation
- Disallowable expenses borderline (entertainment, donations not on Sixth Schedule, general provisions)
- Related-party transactions (TP Regulations 2018 — local file due with return)
- WHT credit notes older than 3 years (ageing risk)
- Missing compliance certificates blocking TCC
- Minimum tax check under CITA Section 33
- Excess Dividend Tax (EDT) risk under CITA Section 19
- State of residence ambiguity for PIT (multi-state employee)

## Positions Taken
[List with legislation citations]
- e.g., "Small company exemption applied — turnover ₦X ≤ ₦25M, CITA Section 40 as amended by Finance Act 2019"
- e.g., "TET at 3% of assessable profit per Finance Act 2023 amendment to TET Act"
- e.g., "Donations of ₦X to [Sixth Schedule beneficiary] — CITA Sixth Schedule, item Y"
- e.g., "Capital allowances claimed at full rate, no Section 31 cap (manufacturing exception)"

## Planning Notes for 2026 (NTA 2025 impact)
- Development Levy at 4% replaces TET/NITDA/NASENI from 1 Jan 2026
- Small company threshold rising to ₦100M turnover
- CIT large-company rate dropping to 25%
- MEFR of 15% for MNE groups (if applicable)
- New PIT rates and ₦800,000 tax-free threshold for individuals
- Rent relief up to ₦200,000 for individuals
- Unified TIN regime full rollout
- FIRS → Nigeria Revenue Service (NRS) rebrand
- Consolidated Nigeria Tax Account view in Tax Pro-Max from 1 Jan 2026
```

## Section 9 — Tax computation summary (PIT or CIT bottom line)

This section is the single "headline" block the reviewer and taxpayer read first.

### 9.1 Individual headline block

- **PIT 2025 headline template** — ```markdown # PIT 2025 — Headline (₦) Gross Income:                      X Less: Allowable deductions:        (X) Less: Reliefs (CRA + statutory):   (X) = Chargeable Income:               X PIT at graduated rates:            X Less: PAYE deducted:               (X) Less: WHT credits:                 (X) Less: Provisional tax:             (X) = Net PIT payable / (refundable):  X / (X) Filing: Form A, State IRS [name], due 31 March 2026 Payment: Remita RRR generated post-filing ```

### 9.2 Corporate headline block

- **CIT 2025 headline template** — ```markdown # CIT 2025 — Headline (₦) — Year of Assessment 2026 Turnover:                          X Profit per accounts:               X Add: Disallowables:                X Less: Exempt income:               (X) = Assessable Profit:               X Less: Capital allowances (capped): (X) Less: Loss relief:                 (X) = Total Profit (Taxable):          X CIT at [0% / 20% / 30%]:           X TET at 3% of assessable profit:    X NITDA / NASENI / PTF (if app):     X = Total federal tax liability:     X Less: WHT credits:                 (X) Less: Advance tax paid:            (X) Less: Foreign tax credit:          (X) = Net tax payable:                 X Minimum tax check (CITA s.33):     [pass/fail] Filing: CIT Self-Assessment, FIRS Tax Pro-Max, due 30 June 2026 Payment: Remita RRR via TSA; instalments under CITA s.77 available ```

## Section 10 — Payment instructions block (for the action list)

```markdown
# Payment Instructions

## Federal payments via Tax Pro-Max / Remita

1. Log into Tax Pro-Max → CIT module → File 2026 YOA return
2. After submission, Tax Pro-Max generates Assessment Notice + Remita RRR
3. Note the RRR (15-digit)
4. Pay via:
   - Bank teller (any commercial bank) — quote RRR
   - Bank internet banking — Remita Bills Payment menu
   - Bank mobile app — Remita section
   - USSD — bank-specific Remita short code
   - POS at FIRS office
5. Bank confirms → Remita issues e-Receipt (RTR)
6. Return to Tax Pro-Max; payment auto-reconciles; status changes to "Paid"
7. Save: Assessment Notice PDF, RRR slip, Remita e-Receipt, Tax Pro-Max Payment Confirmation

## State payments via State IRS portal / Remita

1. Log into State IRS portal (e.g., LIRS eTax for Lagos)
2. File Form A (PIT) or Form H1 (PAYE) as applicable
3. Portal generates Assessment + Remita RRR
4. Pay via Remita (same channels as federal)
5. Retrieve filing acknowledgement → basis for State TCC

## Statutory contributions (parallel — not via Tax Pro-Max)

- Pension: direct bank transfer to PFA custodian within 7 working days of salary payment
- NHF: FMBN portal
- ITF: ITF portal — annual return + payment by 1 April
- NSITF: NSITF portal — monthly + annual reconciliation
```

## Section 11 — Filing instructions block (federal and state, with deadlines)

```markdown
# Filing Instructions

## Federal (FIRS)
- CIT Self-Assessment: Tax Pro-Max, due 30 June 2026 (for 31 Dec 2025 FYE)
- TET: included in CIT return
- VAT 002 (December 2025): Tax Pro-Max, due 21 January 2026
- WHT (December 2025): Tax Pro-Max, due 21 January 2026
- Required attachments: Audited Financial Statements, Tax Computation, Capital Allowances Schedule, Compliance Certificates (ITF, NSITF, PenCom, NHF)

## State (State IRS — taxpayer's state of residence)
- Form A (Individual annual PIT): State IRS portal, due 31 March 2026
- Form H1 (Employer annual PAYE reconciliation): State IRS portal, due 31 January 2026
- Form G (Monthly PAYE): State IRS portal, due 10th of following month
- WHT (individuals): State IRS portal, due 10th of following month

## Statutory bodies (parallel filings)
- Pension contribution schedule: PFA, within 7 working days of salary payment (PenCom monitoring)
- NHF: FMBN, monthly
- ITF: ITF, annual by 1 April 2026
- NSITF: NSITF, monthly + annual reconciliation by 31 March 2026

## Post-filing
- Apply for FIRS TCC (Federal Tax Clearance Certificate) via Tax Pro-Max
- Apply for State TCC via State IRS portal
- Both TCCs are 12-month validity; renew annually
```

## Section 12 — Final taxpayer action list

```markdown
# Action List — [Taxpayer Name] — Tax Year 2025 / Year of Assessment 2026

## Immediate (before earliest deadline — 10 January 2026 for December PAYE)

### Individuals — deadlines:
1. **10 January 2026** — Confirm December 2025 PAYE (Form G) remitted by employer
2. **31 March 2026** — File Form A with State IRS; pay net PIT of ₦X via Remita RRR
3. Apply for State TCC after Form A acceptance

### Employers (PAYE):
1. **10 January 2026** — File December 2025 Form G; remit December PAYE
2. **31 January 2026** — File Form H1 (annual PAYE reconciliation) with State IRS
3. **31 March 2026** — NSITF annual reconciliation
4. **1 April 2026** — ITF annual contribution + return
5. Apply for compliance certificates: ITF, NSITF, PenCom, NHF (each ~12-month validity)

### Companies (CIT):
1. **21 January 2026** — File VAT 002 December; remit VAT
2. **21 January 2026** — File WHT December schedule; remit WHT
3. **31 January 2026** — File Form H1 with State IRS (employer reconciliation)
4. **31 March 2026** — NSITF annual; ensure compliance certificates current
5. **1 April 2026** — ITF annual return + payment
6. **30 June 2026** — File CIT Self-Assessment on Tax Pro-Max for FY ending 31 December 2025; remit CIT + TET via Remita
7. Apply for FIRS TCC after CIT acceptance
8. Generate transfer pricing local file (if related-party transactions); attach to CIT filing
```

## Monthly compliance through 2026

**Monthly compliance through 2026 table**

| Item | Authority | Due |
| --- | --- | --- |
| PAYE Form G | State IRS | 10th of following month |
| WHT (companies) | FIRS Tax Pro-Max | 21st of following month |
| WHT (individuals) | State IRS | 10th of following month |
| VAT 002 | FIRS Tax Pro-Max | 21st of following month |
| Pension (RSA) | PFA | 7 working days from salary |
| NHF | FMBN | Monthly |
| NSITF | NSITF | Monthly (14 days) |

## Record retention

- **Record retention requirement** — Per CITA Section 26 (companies) and PITA Section 53 (individuals), accounting records must be retained for 6 years after the year to which they relate (i.e., FY 2025 records must be kept until end of 2031). FIRS practice for VAT records under VAT Act Section 31: 6 years. Records may be kept in electronic form provided they are accessible to FIRS / State IRS on demand. Cross-border storage is permissible but reasonable on-demand access in Nigeria is expected. Retain at minimum: - Audited financial statements - General ledger and supporting source documents - WHT credit notes (received and issued) with serial numbers - VAT invoices and VAT credit notes - Remita e-Receipts (RTRs) and Tax Pro-Max payment evidence - Tax Pro-Max filing acknowledgements - State IRS filing acknowledgements - Form G monthly + Form H1 annual employer returns - Compliance certificates (ITF, NSITF, PenCom, NHF) - TCCs (federal and state)  _(CITA Section 26; PITA Section 53; VAT Act Section 31)_

## Section 2 — Required inputs from upstream skills

0. **Consume individual return inputs**
0. **Consume ng-personal-income-tax output** — Chargeable income computation feeding Form A Parts B, C, D

## Section 13 — 2026 planning notes (NTA 2025 transitional impact)

The capstone produces a forward-looking section so the taxpayer arrives at the next year's filing aware of the structural changes the **Nigeria Tax Act 2025** introduces.

### 13.1 NTA 2025 — what changes from 1 January 2026

**NTA 2025 transitional changes table**  _(Nigeria Tax Act 2025 (NTA 2025))_

| Area | FY 2025 (current) | FY 2026 (NTA 2025) | Action |
| --- | --- | --- | --- |
| CIT large-company rate | 30% | **25%** | Re-forecast tax in 2026 budget |
| Small company threshold | Turnover ≤ ₦25M | **Turnover ≤ ₦100M** | Many medium companies move into small-company exemption (0% CIT) |
| TET + NITDA + NASENI | 3% + 1% + 0.25% separate levies | Consolidated **Development Levy of 4%** | Single line in 2026 computation |
| Minimum tax (companies) | Section 33 CITA: 0.5% turnover | **MEFR 15%** for MNE groups ≥ €750M consolidated revenue (Pillar Two) | Pillar Two diagnostic for MNE clients |
| PIT structure | Graduated 7–24%, CRA, Sixth Schedule reliefs | New brackets 0–25%; ₦800K tax-free threshold; rent relief ₦200K | Update payroll PAYE calculations from 1 Jan 2026 |
| TIN | Separate FIRS TIN (companies) and JTB TIN (individuals) | **Unified TIN** — single identifier | Re-validate identifiers post 1 Jan 2026 |
| Tax authority | FIRS | **Nigeria Revenue Service (NRS)** | Portal rebrand; processes substantively unchanged in short term |
| VAT rate | 7.5% | **7.5%** (unchanged — proposed increase dropped) | No change |
| Digital services | Significant Economic Presence rules (FA 2019) | NTA 2025 codifies + expands; includes non-resident e-commerce | If MNE: review SEP exposure |
| Consolidated view | Separate modules in Tax Pro-Max | **Nigeria Tax Account** consolidates all obligations in one ledger from 1 Jan 2026 | Reconciliation should be easier post-rollout |

- **Plc CIT rate** — 30% percent (typically falls in the large-company band under NTA 2025)  _(NTA 2025)_
- **Small company threshold** — Turnover ≤ ₦25M  _(Many medium companies move into small-company exemption (0% CIT))_
- **TET + NITDA + NASENI** — 3% + 1% + 0.25% separate levies  _(Single line in 2026 computation)_
- **Minimum tax (companies)** — Section 33 CITA: 0.5% turnover  _(Pillar Two diagnostic for MNE clients)_
- **PIT structure** — Graduated 7–24%, CRA, Sixth Schedule reliefs  _(Update payroll PAYE calculations from 1 Jan 2026)_
- **TIN** — Separate FIRS TIN (companies) and JTB TIN (individuals)  _(Re-validate identifiers post 1 Jan 2026)_
- **Tax authority** — FIRS  _(Portal rebrand; processes substantively unchanged in short term)_
- **VAT rate** — 7.5%  _(No change)_
- **Digital services** — Significant Economic Presence rules (FA 2019)  _(If MNE: review SEP exposure)_
- **Consolidated view** — Separate modules in Tax Pro-Max  _(Reconciliation should be easier post-rollout)_

### 13.2 Provisional / advance tax for 2026

- **CIT provisional tax** — Plan provisional CIT under CITA Section 77 if the company will pay in instalments; first instalment due with provisional return (typically within 3 months of FY-end). Provisional return is filed on the basis of current-year forecast.  _(CITA Section 77)_
- **PIT provisional tax** — Self-employed individuals pay provisional PIT in 4 quarterly instalments under PITA Section 44 (15 April, 15 July, 15 October, 15 January). Compute on best estimate of FY 2026 chargeable income at NEW NTA 2025 rates.  _(PITA Section 44)_

### 13.3 Compliance certificate renewals

All four compliance certificates (ITF, NSITF, PenCom, NHF) renew annually. Plan applications **early Q1 2026** to ensure TCC is not blocked. Each can take 2–6 weeks.

### 13.4 Transfer pricing (companies)

If related-party transactions exist:

- **Local File** — Required for entities with related-party transactions ≥ ₦300M (FIRS TP Regulations 2018 Regulation 16). Due with CIT return (30 June 2026 for 31 Dec 2025 FYE).  _(FIRS TP Regulations 2018 Regulation 16)_
- **Master File** — Required for entities part of MNE groups ≥ ₦160B consolidated revenue. Same due date.  _(FIRS TP Regulations 2018)_
- **CbCR Notification** — Annual within 12 months of FY-end if MNE.  _(FIRS TP Regulations 2018)_
- **TP Declaration Form** — Submitted as schedule to Tax Pro-Max return.  _(FIRS TP Regulations 2018)_

### 13.5 Minimum tax monitoring

- **Minimum tax rule** — Under CITA Section 33, where a company has insufficient tax payable (e.g., due to large capital allowances or losses), minimum tax of **0.5% of gross turnover** applies (excluded: small companies under Section 40, companies in first 4 years of operation, manufacturing within first 4 years, agricultural). Flag in 2026 forecast if minimum tax is likely to bite.  _(CITA Section 33)_

### 13.6 Excess Dividend Tax (EDT)

- **Excess Dividend Tax** — Under CITA Section 19, if a company pays dividends in excess of its taxable profits for the year, the excess is taxable at the corporate rate. Plan dividend distributions to avoid EDT exposure. Finance Act 2020 narrowed but did not eliminate EDT.  _(CITA Section 19; Finance Act 2020)_

## Section 14 — Conservative defaults

When inputs from upstream skills are ambiguous or missing, apply the following defaults and flag for the reviewer:

**Conservative defaults table**

| Situation | Conservative default |
| --- | --- |
| Cross-skill reconciliation differs by > ₦1,000 | Flag as "Needs Input"; do not silently round |
| Tax Pro-Max billing reference / Remita RRR unknown | Use "TBC — generate via Tax Pro-Max" and DO NOT estimate the RRR |
| Company size classification borderline (turnover near ₦25M / ₦100M boundary) | Use HIGHER tax bracket as conservative; flag for reviewer |
| State of residence ambiguous (multi-state employee) | Default to state of principal employment per PITA First Schedule; flag |
| Capital allowances cap applicability unclear (non-manufacturing vs manufacturing) | Apply 66 2/3% cap; flag for reviewer |
| TIN missing or unverified | Cannot finalise return; flag as blocker |
| WHT credit notes claimed but not in hand | Exclude the credit; flag for taxpayer to obtain |
| Audit requirement unclear (small company exempted from audit by CAMA 2020 Section 402 — must be a small company per CAMA definition) | Recommend audit unless clearly exempt; conservative position |
| Donation deductibility uncertain (recipient not on CITA Sixth Schedule) | Disallow; flag for reviewer |
| December payroll true-up not booked | Treat year as incomplete; cannot finalise return until December payroll closed |
| Foreign tax credit certificate of payment missing | Disallow credit; flag for documentation |
| Related-party transactions undocumented | Flag transfer pricing risk; do not assume arm's-length |
| Compliance certificate missing or expired | Flag as TCC blocker |
| NTA 2025 rate or threshold assumed for FY 2025 | Reject; FY 2025 uses pre-NTA rules; NTA 2025 applies from 1 Jan 2026 only |
| Tax Pro-Max payment evidence missing | Mark assessment as "pending payment"; advise to settle before deadline |

- **Cross-skill reconciliation differs by > ₦1,000** — Flag as "Needs Input"; do not silently round
- **Tax Pro-Max billing reference / Remita RRR unknown** — Use "TBC — generate via Tax Pro-Max" and DO NOT estimate the RRR
- **Company size classification borderline (turnover near ₦25M / ₦100M boundary)** — Use HIGHER tax bracket as conservative; flag for reviewer
- **State of residence ambiguous (multi-state employee)** — Default to state of principal employment per PITA First Schedule; flag
- **Capital allowances cap applicability unclear (non-manufacturing vs manufacturing)** — Apply 66 2/3% cap; flag for reviewer
- **TIN missing or unverified** — Cannot finalise return; flag as blocker
- **WHT credit notes claimed but not in hand** — Exclude the credit; flag for taxpayer to obtain
- **Audit requirement unclear (small company exempted from audit by CAMA 2020 Section 402 — must be a small company per CAMA definition)** — Recommend audit unless clearly exempt; conservative position
- **Donation deductibility uncertain (recipient not on CITA Sixth Schedule)** — Disallow; flag for reviewer
- **December payroll true-up not booked** — Treat year as incomplete; cannot finalise return until December payroll closed
- **Foreign tax credit certificate of payment missing** — Disallow credit; flag for documentation
- **Related-party transactions undocumented** — Flag transfer pricing risk; do not assume arm's-length
- **Compliance certificate missing or expired** — Flag as TCC blocker
- **NTA 2025 rate or threshold assumed for FY 2025** — Reject; FY 2025 uses pre-NTA rules; NTA 2025 applies from 1 Jan 2026 only
- **Tax Pro-Max payment evidence missing** — Mark assessment as "pending payment"; advise to settle before deadline
- **Tolerance rule (repeated for emphasis)** — ₦1,000 reconciliation tolerance. Any larger discrepancy is escalated, not absorbed.

## Section 15 — Refusals

- **R-NG-ASM-1** — Upstream skill did not run. Name the missing skill. Continue with available data; flag the gap; do not fabricate the missing computation.  _(R-NG-ASM-1)_
- **R-NG-ASM-2** — Upstream self-check failed. Note the specific check; continue but flag.  _(R-NG-ASM-2)_
- **R-NG-ASM-3** — Cross-skill reconciliation > ₦1,000. Raise as "Needs Input"; do not silently round.  _(R-NG-ASM-3)_
- **R-NG-ASM-4** — Out of scope: Petroleum Profits Tax (PPTA), Hydrocarbon Tax under PIA 2021, mining royalties, telecommunications-specific levies, gaming tax, betting tax, freezone tax holidays (NEPZA / OGFZA pioneer status under Industrial Development Income Tax Relief Act). Flag for human specialist; do not attempt.  _(R-NG-ASM-4)_
- **R-NG-ASM-5** — Out of scope: non-resident companies / non-resident individuals, Permanent Establishment determination under DTT, mixed-residency years, expatriate Significant Economic Presence under FA 2019 / NTA 2025. Refer to a specialist; this skill assumes full-year Nigerian tax residency.  _(R-NG-ASM-5)_
- **R-NG-ASM-6** — Out of scope: combined federal-state tax disputes, Tax Appeal Tribunal (TAT) proceedings, FIRS audit defence, transfer pricing audit defence. Refer to a tax lawyer / CITN member with TAT practice.  _(R-NG-ASM-6)_
- **R-NG-ASM-7** — Intake incomplete. Name the missing intake field (TIN, RC/BN, NIN, State of Residence, etc.). Cannot finalise the return until provided.  _(R-NG-ASM-7)_
- **R-NG-ASM-8** — Asked to submit to Tax Pro-Max or State IRS portal directly. This skill produces a working paper. Submission is the taxpayer's (or their authorised filer's) action, after ICAN / CITN review and sign-off. Decline politely; provide the filing instructions instead.  _(R-NG-ASM-8)_
- **R-NG-ASM-9** — NTA 2025 retroactive application. NTA 2025 effective dates govern; do not back-apply 2026 rates / thresholds to 2025 returns. Decline politely; explain transitional rules.  _(R-NG-ASM-9)_
- **R-NG-ASM-10** — Out of scope: oil and gas sector (PIA 2021 Chapter 4 fiscal terms), pioneer status companies, free zone enterprises, NIPC-incentivised entities. Refer to specialist.  _(R-NG-ASM-10)_

## Section 16 — Self-checks

All upstream skills required for the chosen filing type have produced output, or the gap is flagged.

Revenue reconciles between bookkeeping, ng-vat, and the chosen income-tax skill (ng-cit / ng-personal-income-tax) within ₦1,000.

Tax credits sum correctly across PAYE, WHT, provisional tax, foreign tax credit; each WHT credit note backed by FIRS / State IRS serial number.

Form H1 sum equals Form G monthly totals within ₦1,000; December true-up is booked.

All four statutory deductions (Pension, NHF, NHIS, ITF/NSITF) remitted; compliance certificates current.

For companies: capital allowances within Section 31 cap (66 2/3% for non-manufacturing) unless manufacturing exemption applies; TWDV roll-forward ties.

Minimum tax check under CITA Section 33 performed; result documented.

CIT rate band (0% / 20% / 30%) correctly applied based on FY 2025 turnover (₦25M / ₦100M thresholds); company classified small/medium/large.

TET at 3% of assessable profit (NOT total profit); applied to ALL companies (no small-company exemption from TET per Finance Act 2023).

Filing deadlines explicitly stated in action list: 10 Jan (PAYE), 21 Jan (VAT/WHT), 31 Jan (H1), 31 Mar (Form A / NSITF), 1 Apr (ITF), 30 Jun (CIT).

Tax Pro-Max workflow described: file → Assessment → Remita RRR → Pay → e-Receipt → Reconciliation.

State IRS jurisdiction for PIT correctly identified per taxpayer's "place of residence" under PITA First Schedule.

Record retention period (6 years per CITA Section 26 / PITA Section 53 / VAT Act Section 31) is stated.

Reviewer brief contains legislation citations for every position taken (CITA, PITA, VAT Act, CGTA, TET Act, Finance Acts, NTA 2025 where prospective).

TCC application workflow noted in action list (FIRS TCC + State TCC).

ICAN / CITN reviewer sign-off requirement stated in executive summary and action list.

NTA 2025 transitional impacts flagged in 2026 planning section; rates/thresholds NOT back-applied to 2025.

## Section 17 — Reviewer attestation block

The final working paper carries an attestation block the credentialed reviewer signs:

```markdown
# Reviewer Attestation — Year of Assessment 2026 (FY 2025)

I, [Name], [ICAN/ANAN] member with ICAN/ANAN number [____], 
and [CITN member where applicable] number [____], 
acting for [Taxpayer name, TIN ________], 
have reviewed the working paper prepared by [preparer / OpenAccountants AI], 
verified the cross-skill reconciliations to my satisfaction, 
and confirm that:

  [ ] The audited financial statements (companies) or business accounts (sole 
       proprietors) on which this return is based are signed off
  [ ] Tax adjustments, capital allowances, and reliefs comply with CITA / PITA / 
       relevant Finance Acts
  [ ] Statutory compliance certificates (ITF, NSITF, PenCom, NHF) are in place 
       (or absence is flagged)
  [ ] WHT credit notes claimed have verifiable serial numbers
  [ ] VAT-to-income reconciliation is within ₦1,000 tolerance (or explained)
  [ ] PAYE Form H1 reconciles to monthly Form G remittances
  [ ] No NTA 2025 prospective rule has been back-applied to 2025
  [ ] Transfer pricing local file is prepared (where required) and attached
  [ ] Minimum tax check under CITA Section 33 (companies) is documented
  [ ] All payment due dates and Remita / Tax Pro-Max workflows are explained 
       to the taxpayer

Signed: ___________________  Date: ___________________
        [Reviewer name]
ICAN/ANAN no.: ___________________
CITN no. (if applicable): ___________________
Firm: ___________________  FRC no.: ___________________
```

**No filing without this signed attestation.**

## Section 18 — Output files

The final output is **three files**:

1. **`[taxpayer_slug]_2025_ng_master.xlsx`** — Master workbook. Sheets: Cover, Identity, Form A (or CIT Self-Assessment), Tax Computation, Capital Allowances, Loss Relief, WHT Credit Notes Register, Statutory Deductions Register, VAT Reconciliation, Form H1 / Form G Reconciliation, Cross-Check Summary, Tax Pro-Max / Remita Payment Schedule, Compliance Certificates Tracker. Use live formulas where possible; verify no `#REF!` errors.

2. **`reviewer_brief.md`** — Markdown file with all Section 8 contents, plus the headline blocks from Section 9 and the attestation block from Section 17.

3. **`taxpayer_action_list.md`** — Markdown file with all Section 12 contents, plus the payment instructions block from Section 10 and filing instructions block from Section 11.

All three files are placed in `/mnt/user-data/outputs/` and presented to the user at the end.

If execution runs out of context mid-build, complete the computation work first and produce whichever formatted outputs are finished, then state clearly which deliverables are partial.

## Section 19 — Known gaps

1. PDF form filling is not automated; the reviewer or taxpayer enters values into Tax Pro-Max / State IRS portals using the working paper.
2. Tax Pro-Max XML / bulk upload templates are not generated by this skill; integrations with ERP / accounting software handle that.
3. Audited financial statements attachment is the taxpayer's responsibility; this skill only flags when audit is required (CAMA 2020 Section 402 small-company exemption).
4. Transfer pricing local file / master file content is referenced but not assembled here (separate skill needed for full TP documentation).
5. Petroleum Profits Tax / Hydrocarbon Tax under PIA 2021 is out of scope.
6. Pioneer status (NIPC) / freezone (NEPZA / OGFZA) regime computations are out of scope.
7. Country-by-Country Reporting XML is not assembled here.
8. NTA 2025 implementing regulations may evolve through 2025–2026; every prospective rule in this skill should be re-verified against the gazetted NTA 2025 commencement notice and any FIRS / NRS implementation guidance.
9. State IRS portal mechanics vary by state; this skill describes the LIRS pattern as the most-developed example. Smaller states may require paper filings; flag in intake.
10. CGT on shares: NTA 2025 changes the CGT treatment of certain share disposals from 1 Jan 2026 — not relevant for 2025 returns but flagged in planning.

### Change log

- **v1.0 (May 2026):** Initial release. Modelled on mt-return-assembly, us-ca-return-assembly, and id-return-assembly. Adapted for Nigerian PIT Form A, CIT Self-Assessment via FIRS Tax Pro-Max, State IRS coordination, Remita / TSA payment, and NTA 2025 transitional impact. Coordinates nine upstream Nigeria skills.

## Section 20 — Sources

**Sources table**

| Source | Reference |
| --- | --- |
| Companies Income Tax Act (CITA), Cap C21 LFN 2004 (as amended) | CIT framework; Sections 31 (capital allowances cap), 33 (minimum tax), 40 (rates), 55 (filing deadline), 77 (instalments), 81 (WHT compliance), 85 (interest), Second Schedule (capital allowances), Sixth Schedule (donations) |
| Personal Income Tax Act (PITA), Cap P8 LFN 2004 (as amended) | PIT framework; Sections 41 (annual return), 44 (provisional tax), 73 (WHT compliance), 81 (PAYE), 94 (penalties), First Schedule (residence), Sixth Schedule (CRA & graduated rates) |
| Value Added Tax Act, Cap V1 LFN 2004 (as amended through Finance Act 2020) | VAT framework, 7.5% rate, monthly filing, reverse charge on imported services |
| Capital Gains Tax Act (CGTA), Cap C1 LFN 2004 (as amended) | CGT at 10%; Section 32 roll-over relief |
| Tertiary Education Trust Fund Act 2011 (as amended by Finance Act 2023) | TET at 3% of assessable profit; applies to all resident companies |
| Pension Reform Act 2014 | Pension framework; 8% employee + 10% employer; Section 11(3) seven-day remittance |
| National Housing Fund Act 1992 | 2.5% NHF contribution |
| Industrial Training Fund Act (as amended) | 1% of payroll; annual return |
| Employees Compensation Act 2010 | NSITF 1% of payroll |
| National Health Insurance Authority Act 2022 (replacing NHIS Act) | NHIA scheme rates |
| Companies and Allied Matters Act (CAMA) 2020 | Section 402 small-company audit exemption; CAC RC/BN issuance |
| FIRS Establishment Act 2007 | FIRS powers; transitioning to NRS under NTA 2025 |
| Federal Inland Revenue Service Transfer Pricing Regulations 2018 | Local file, master file, TP declaration, related-party thresholds |
| Finance Act 2019 | Small company exemption; WHT reforms; minimum tax narrowing |
| Finance Act 2020 | VAT reforms; SEP rules; EDT narrowing; CRA enhancement |
| Finance Act 2021 | Capital gains on shares; further VAT amendments |
| Finance Act 2023 | TET rate to 3%; further refinements |
| **Nigeria Tax Act 2025 (NTA 2025)** — assented June 2025, key provisions effective 1 January 2026 | New CIT rate (25% large), new small-company threshold (₦100M), Development Levy (4% consolidating TET/NITDA/NASENI), new PIT brackets and ₦800K threshold, unified TIN, NRS rebrand, MEFR 15% for MNEs (Pillar Two) — **prospective only; does NOT apply to FY 2025** |
| FIRS Tax Pro-Max | https://taxpromax.firs.gov.ng |
| Remita | https://www.remita.net |
| Lagos State Internal Revenue Service (LIRS) eTax | https://etax.lirs.net |
| FCT-IRS | https://fctirs.gov.ng |
| Institute of Chartered Accountants of Nigeria (ICAN) | https://icanig.org |
| Association of National Accountants of Nigeria (ANAN) | https://anan.org.ng |
| Chartered Institute of Taxation of Nigeria (CITN) | https://citn.org |
| Skill version | 1.0 |

- **CIT framework; Sections 31 (capital allowances cap), 33 (minimum tax), 40 (rates), 55 (filing deadline), 77 (instalments), 81 (WHT compliance), 85 (interest), Second Schedule (capital allowances), Sixth Schedule (donations)** — CIT framework; Sections 31 (capital allowances cap), 33 (minimum tax), 40 (rates), 55 (filing deadline), 77 (instalments), 81 (WHT compliance), 85 (interest), Second Schedule (capital allowances), Sixth Schedule (donations)  _(Companies Income Tax Act (CITA), Cap C21 LFN 2004 (as amended))_
- **PIT framework; Sections 41 (annual return), 44 (provisional tax), 73 (WHT compliance), 81 (PAYE), 94 (penalties), First Schedule (residence), Sixth Schedule (CRA & graduated rates)** — PIT framework; Sections 41 (annual return), 44 (provisional tax), 73 (WHT compliance), 81 (PAYE), 94 (penalties), First Schedule (residence), Sixth Schedule (CRA & graduated rates)  _(Personal Income Tax Act (PITA), Cap P8 LFN 2004 (as amended))_
- **Value Added Tax Act, Cap V1 LFN 2004 (as amended through Finance Act 2020)** — VAT framework, 7.5% rate, monthly filing, reverse charge on imported services
- **CGT at 10%; Section 32 roll-over relief** — CGT at 10%; Section 32 roll-over relief  _(Capital Gains Tax Act (CGTA), Cap C1 LFN 2004 (as amended))_
- **Tertiary Education Trust Fund Act 2011 (as amended by Finance Act 2023)** — TET at 3% of assessable profit; applies to all resident companies
- **Pension framework; 8% employee + 10% employer; Section 11(3) seven-day remittance** — Pension framework; 8% employee + 10% employer; Section 11(3) seven-day remittance  _(Pension Reform Act 2014)_
- **2.5% NHF contribution** — 2.5% NHF contribution  _(National Housing Fund Act 1992)_
- **1% of payroll; annual return** — 1% of payroll; annual return  _(Industrial Training Fund Act (as amended))_
- **NSITF 1% of payroll** — NSITF 1% of payroll  _(Employees Compensation Act 2010)_
- **NHIA scheme rates** — NHIA scheme rates  _(National Health Insurance Authority Act 2022 (replacing NHIS Act))_
- **Section 402 small-company audit exemption; CAC RC/BN issuance** — Section 402 small-company audit exemption; CAC RC/BN issuance  _(Companies and Allied Matters Act (CAMA) 2020)_
- **FIRS powers; transitioning to NRS under NTA 2025** — FIRS powers; transitioning to NRS under NTA 2025  _(FIRS Establishment Act 2007)_
- **Local file, master file, TP declaration, related-party thresholds** — Local file, master file, TP declaration, related-party thresholds  _(Federal Inland Revenue Service Transfer Pricing Regulations 2018)_
- **Small company exemption; WHT reforms; minimum tax narrowing** — Small company exemption; WHT reforms; minimum tax narrowing  _(Finance Act 2019)_
- **VAT reforms; SEP rules; EDT narrowing; CRA enhancement** — VAT reforms; SEP rules; EDT narrowing; CRA enhancement  _(Finance Act 2020)_
- **Capital gains on shares; further VAT amendments** — Capital gains on shares; further VAT amendments  _(Finance Act 2021)_
- **Finance Act 2023** — TET rate to 3%; further refinements
- **New CIT rate (25% large), new small-company threshold (₦100M), Development Levy (4% consolidating TET/NITDA/NASENI), new PIT brackets and ₦800K threshold, unified TIN, NRS rebrand, MEFR 15% for MNEs (Pillar Two) — **prospective only; does NOT apply to FY 2025**** — New CIT rate (25% large), new small-company threshold (₦100M), Development Levy (4% consolidating TET/NITDA/NASENI), new PIT brackets and ₦800K threshold, unified TIN, NRS rebrand, MEFR 15% for MNEs (Pillar Two) — **prospective only; does NOT apply to FY 2025**  _(**Nigeria Tax Act 2025 (NTA 2025)** — assented June 2025, key provisions effective 1 January 2026)_
- **https://taxpromax.firs.gov.ng** — https://taxpromax.firs.gov.ng  _(FIRS Tax Pro-Max)_
- **https://www.remita.net** — https://www.remita.net  _(Remita)_
- **https://etax.lirs.net** — https://etax.lirs.net  _(Lagos State Internal Revenue Service (LIRS) eTax)_
- **https://fctirs.gov.ng** — https://fctirs.gov.ng  _(FCT-IRS)_
- **https://icanig.org** — https://icanig.org  _(Institute of Chartered Accountants of Nigeria (ICAN))_
- **https://anan.org.ng** — https://anan.org.ng  _(Association of National Accountants of Nigeria (ANAN))_
- **https://citn.org** — https://citn.org  _(Chartered Institute of Taxation of Nigeria (CITN))_
- **1.0** — 1.0  _(Skill version)_

## OpenAccountants footer disclaimer

*OpenAccountants — open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed and signed off by a Chartered Accountant in Nigeria (ICAN or ANAN member, and where tax-specific opinions are required, also CITN-registered) before filing via FIRS Tax Pro-Max or the relevant State Internal Revenue Service portal.*

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
