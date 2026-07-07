---
name: ie-return-assembly
description: Use this skill whenever asked to assemble, finalize, or package an Irish annual tax return. Trigger on phrases like "Ireland tax return assembly", "Form 11 final", "CT1 final filing", "ROS submission Ireland", "preliminary tax Ireland", "31 October Ireland", "assemble Irish return", "prepare Form 11", "prepare Form 12", "finalize Irish self-assessment", or "Revenue Online Service pay and file". This is the capstone orchestrator that pulls together outputs from ie-income-tax-form11, ie-preliminary-tax, ie-prsi-class-s, ie-usc, ireland-vat-return, ie-corporation-tax, ie-paye, ie-payroll, ie-cgt, ie-cat, and ie-formation into a single Form 11 / Form 12 / CT1 working paper plus payment and filing instructions for the Revenue Online Service (ROS). It does not recompute anything itself — it reconciles upstream outputs, builds the line-by-line working paper, generates ROS payment instructions, and produces a reviewer brief and taxpayer action list. ALWAYS read this skill last when finalizing an Irish tax return.
jurisdiction: IE
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ie-return-assembly

## Ireland — Return Assembly (Capstone) — Skill v1.0

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

**When this skill is invoked, the user has already passed through intake and the relevant content skills. They want their finished Irish return working paper. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask "do you want me to assemble the full package".** The user asked for the return. Produce it.
- **Do NOT re-interrogate the user about residency, PPSN, tax registration, or business structure** — intake already captured this; trust the upstream packages.
- **Do NOT pause between reconciliation steps to check in.** Run all cross-checks in sequence; flag failures in the reviewer brief and continue.
- **Self-checks are targets, not blockers.** If a check fails, note it under "Reviewer Attention Flags" and continue.
- **Do NOT submit anything to ROS.** This skill produces a working paper plus filing instructions. A credentialed Irish reviewer (Chartered Accountants Ireland — CAI; ACCA-IE; or Irish Tax Institute — CTA) must review and the taxpayer (or their TAIN-registered agent) submits via ROS.

**If you feel the urge to ask "how should I proceed", pick the most defensible path, proceed, and flag the decision for the reviewer.**

## What this file is

The final capstone skill for Irish annual tax returns. It consumes the outputs of every other Ireland skill and assembles a single unified working paper covering one (or more) of the following Revenue forms:

- **Form 11 / 11S** — annual self-assessment income tax return for chargeable persons (self-employed sole traders, partners, proprietary directors, individuals with non-PAYE income above the small-amounts threshold)
- **Form 12** — annual return for PAYE taxpayers with limited non-PAYE income (below the Form 11 chargeable-person threshold)
- **CT1** — corporation tax return for Irish-resident companies
- **VAT3** — bi-monthly (or quarterly / annual where authorised) VAT return; the RTD (Return of Trading Details) annual VAT statement
- **CG1** — Capital Gains Tax return (for individuals not otherwise filing Form 11)
- **IT38** — Capital Acquisitions Tax (gifts and inheritances) return

The output is a reviewer-ready package: line-by-line working paper, cross-skill reconciliation table, payment instructions for ROS (SEPA Direct Debit / EFT / debit card / myAccount), filing instructions, reviewer checklist, and taxpayer action list.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Ireland (Éire) |
| Tax authority | Revenue Commissioners (Na Coimisinéirí Ioncaim) |
| Filing portal | ROS — Revenue Online Service (https://www.ros.ie); myAccount for individuals not registered for ROS |
| Currency | EUR (€) |
| Tax year — individuals | Calendar year (1 January – 31 December) |
| Tax year — companies | Accounting period as defined by the company (max 12 months) |
| Current tax year | 2025 (Form 11 filing window 1 January – 31 October 2026; ROS pay & file extended date mid-November 2026, announced by Revenue) |
| Individual self-assessment return | Form 11 / Form 11S (short form for simpler cases) |
| PAYE return (non-chargeable persons) | Form 12 (via myAccount) |
| Corporate return | CT1 |
| VAT return | VAT3 (bi-monthly default); RTD annually |
| CGT return | CG1 (or via Form 11 Panel CGT) |
| CAT return | IT38 |
| Confirmation receipt | ROS Notice of Acknowledgement / receipt number |
| Governing law | Taxes Consolidation Act 1997 (TCA 1997, as amended); VAT Consolidation Act 2010; Capital Acquisitions Tax Consolidation Act 2003; Finance Act 2024; Finance (No. 2) Act 2023 |
| Skill version | 1.0 |
| Validated by | Pending — requires sign-off by a credentialed Irish reviewer: Chartered Accountants Ireland (CAI — the body that registered the "Chartered Accountant" designation in Ireland); ACCA-IE (Association of Chartered Certified Accountants — Ireland); or Irish Tax Institute (Chartered Tax Adviser — CTA) |

## Section 2 — Required inputs from upstream skills

The assembly skill does not recompute anything. It expects structured outputs from the following upstream skills. If an upstream skill did not run, the assembly notes the gap and continues with available data.

### 2.1 Individual return (Form 11) — inputs

**Form 11 inputs table**

| Upstream skill | Output consumed | Where it lands on the return |
| --- | --- | --- |
| `ie-income-tax-form11` | Schedule D Case I/II trading profit; case III foreign income; case IV miscellaneous; case V rental; standard rate cut-off point; tax credits | Form 11 Panel Self-Employed Income; Panel PAYE/BIK; Panel Foreign Income; Panel Rental |
| `ie-preliminary-tax` | Preliminary tax 2026 (100% prior-year / 90% current-year / 105% pre-preceding safe harbours under s959AN TCA 1997) | Form 11 Preliminary Tax Panel; payment instruction by 31 October 2026 |
| `ie-prsi-class-s` | PRSI Class S liability at 4.1% (rising to 4.2% from 1 October 2025) on relevant income; minimum €650 (2025) annual payment | Form 11 PRSI Panel |
| `ie-usc` | Universal Social Charge bands and rates; surcharge on non-PAYE income > €100,000 (3% additional USC under s531AN TCA 1997) | Form 11 USC Panel |
| `ireland-vat-return` | If VAT-registered: bi-monthly VAT3 history; RTD; cross-check turnover | Cross-check; nothing flows to Form 11 directly |
| `ie-paye` | Employment income from P60 / PAYE Modernisation (PMOD) Employment Detail Summary | Form 11 PAYE Panel |
| `ie-payroll` | Employer-side PAYE / USC / PRSI summaries (if proprietary director or employer themselves) | Form 11 Director / Employer panels |
| `ie-cgt` | CGT disposals during 2025: chargeable gains, annual exemption €1,270, 33% rate | Form 11 CGT Panel (or separate CG1) |
| `ie-cat` | Gifts / inheritances received in valuation date year | Separate IT38; cross-reference in Form 11 not required |
| `ie-formation` | Sole trader registration (TR1) / business name / start-of-trade adjustments | Identity panel |

### 2.2 PAYE / non-chargeable individual return (Form 12) — inputs

**Form 12 inputs table**

| Upstream skill | Output consumed | Where it lands on the return |
| --- | --- | --- |
| `ie-paye` | P60 / Employment Detail Summary; tax credits used | Form 12 employment income |
| `ie-income-tax-form11` | Only if non-PAYE income exists below chargeable-person threshold | Form 12 non-PAYE income panel |
| `ie-cgt` | Disposals (or routed to CG1) | Reference panel |

- **Threshold rule for chargeable person** — A taxpayer becomes a "chargeable person" if non-PAYE income (gross) exceeds €5,000 or net (after expenses) exceeds €5,000, requiring Form 11 instead of Form 12. The assembly skill checks this and routes accordingly.  _(s959B TCA 1997)_

### 2.3 Corporate return (CT1) — inputs

**CT1 inputs table**

| Upstream skill | Output consumed | Where it lands on the return |
| --- | --- | --- |
| `ie-corporation-tax` | Case I/II trading income at 12.5% trading rate (s21 TCA 1997); Case III/IV/V at 25% passive rate; close company surcharge (s440 TCA 1997) if applicable; R&D tax credit | CT1 Income Panel; Tax Computation Panel |
| `ie-payroll` | Payroll cost classification (P30 monthly returns reconciled) | CT1 Trading Account |
| `ireland-vat-return` | If VAT-registered: bi-monthly VAT3 history; RTD; cross-check turnover | Cross-check; PPN cost in P&L if irrecoverable |
| `ie-cgt` | Company chargeable gains (corporates pay CGT-equivalent via CT at 33% via re-grossing under s78 TCA 1997) | CT1 Chargeable Gains Panel |
| `ie-formation` | Company incorporation date, CRO number, accounting period dates | Identity panel |

### 2.4 Intake-required identifiers

**Intake identifiers table**

| Identifier | Required for |
| --- | --- |
| PPSN (Personal Public Service Number) | All individual returns |
| Tax Reference Number (TRN) | Sole traders, partnerships, employer registrations |
| CRO number + Tax Reference Number (CT1 TRN) | All companies |
| VAT number (IE + 7 digits + 1 or 2 letters) | If VAT-registered |
| Employer registration number (PREM) | If operating PAYE/PRSI |
| TAIN (Tax Adviser Identification Number) | If filing as agent |
| ROS Digital Certificate | Required for ROS submission |
| Marital / civil status & assessment basis (single / joint / separate assessment) | Form 11/12 tax credit and band determination |
| Dependants (qualifying children for Single Person Child Carer Credit, Incapacitated Child Credit, etc.) | Tax credits |

- **Missing identifier handling** — If any identifier is missing, the assembly skill flags it as "Needs Input" and produces the working paper with placeholders rather than halting.

## Section 3 — Tax computation reconciliation

The assembly skill verifies that numbers from the upstream skills are mutually consistent. If a cross-check fails by more than **€1**, the discrepancy is raised in the reviewer brief — never silently rounded.

### Cross-check 1 — Turnover / revenue reconciliation

**Turnover reconciliation table**

| Source | Figure | Rule |
| --- | --- | --- |
| `ie-income-tax-form11` or `ie-corporation-tax` trading account turnover | Schedule D Case I/II turnover | Anchor figure |
| `ireland-vat-return` RTD turnover (Box T1/T2 plus zero-rated boxes) | Annual VAT turnover from RTD | Must reconcile within ± timing differences (cash vs invoice basis), VAT-exempt activity, intra-Community supplies |
| Bookkeeping ledger gross sales | General ledger | Anchor for both above |

- **Mismatch causes** — **If mismatch:** Likely causes are (i) VAT-exempt activity not in VAT boxes, (ii) cash vs invoice basis timing, (iii) intra-Community supplies (Box E1/E2) excluded from T1, (iv) reverse-charge purchases that inflate Box T2 but are not turnover.

### Cross-check 2 — Income tax / USC / PRSI add up correctly (Form 11)

**Income tax / USC / PRSI table**

| Component | Source skill | Description |
| --- | --- | --- |
| Income tax at 20% within standard rate cut-off | ie-income-tax-form11 | Standard band charge |
| Income tax at 40% above cut-off | ie-income-tax-form11 | Higher band charge |
| Tax credits (Personal, PAYE, Earned Income, etc.) | ie-income-tax-form11 | Non-refundable credits against gross tax |
| USC | ie-usc | Computed on gross income subject to USC (different base from income tax) |
| PRSI Class S (self-employed) | ie-prsi-class-s | 4.1% (or 4.2% from 1 Oct 2025) on relevant income; minimum €650 |
| Preliminary tax paid (PT) | ie-preliminary-tax | Credit against final liability |
| PAYE / USC / PRSI withheld at source | ie-paye | Credit against final liability |
| Withholding tax (PSWT — Professional Services Withholding Tax 20% under s522 TCA 1997) | ie-income-tax-form11 | Credit against final liability |
| Foreign tax credit (DTR — Double Taxation Relief) | ie-income-tax-form11 | Credit, capped at Irish tax on that source |

- **Credits cap rule** — **Rule:** Total credits cannot exceed Irish tax liability for refund purposes unless the excess is PAYE / PSWT properly supported by Employment Detail Summary or F45 / F50 certificates.

### Cross-check 3 — Preliminary tax safe harbour (s959AN TCA 1997)

**Safe harbour table**

| Safe harbour | Source | Rule |
| --- | --- | --- |
| 100% of 2025 final liability | ie-preliminary-tax | Most common; standard prior-year rule |
| 90% of 2026 estimated liability | ie-preliminary-tax | Useful when 2026 income lower; risk if 2026 actual exceeds estimate |
| 105% of 2024 ("pre-preceding") liability paid via SEPA Direct Debit only | ie-preliminary-tax | Only if PT is paid monthly by SDD throughout the year |

- **Safe harbour failure interest** — **If safe harbour failed:** Interest at 0.0219% per day (≈ 8% p.a.) under s1080 TCA 1997 applies; flag for the reviewer.  _(s1080 TCA 1997)_

### Cross-check 4 — VAT reconciliation (annual RTD ↔ bi-monthly VAT3s)

**VAT reconciliation table**

| Item | Source | Rule |
| --- | --- | --- |
| Sum of six bi-monthly VAT3 Box T1 (Sales VAT) | ireland-vat-return | Must equal annual RTD Box T1 |
| Sum of six bi-monthly VAT3 Box T2 (Purchases VAT) | ireland-vat-return | Must equal annual RTD Box T2 |
| RTD filing | ireland-vat-return | Due same date as bi-monthly VAT3 for Nov/Dec period (19 January 2026 paper / 23 January 2026 ROS) |

- **Mismatch investigation** — **If mismatch:** Investigate VAT3 amendments (Form VAT3a) not reflected in RTD, intra-Community acquisitions / supplies (Boxes E1/E2/ES1/ES2), postponed accounting on imports (PA1/PA2).

### Cross-check 5 — PAYE / PMOD reconciliation

If the taxpayer (or company) operated PAYE for any employees, or is a proprietary director with PAYE income:

**PMOD reconciliation table**

| Item | Source | Rule |
| --- | --- | --- |
| Sum of monthly P30 returns under PMOD (PAYE Modernisation, effective 1 January 2019) | ie-payroll | Must equal annual Employment Detail Summary per employee |
| Employer's PRSI contribution rate | ie-payroll | Class A: 8.9% / 11.15% (rising to 11.25% from 1 Oct 2025) depending on band; Class S: 4.1% (proprietary director's own income) |
| Income tax / USC / PRSI withheld | ie-payroll → ie-paye | Reconciles to employee P60 / EDS |

- **Mismatch cause** — **If mismatch:** Likely cause is mid-month corrections via PMOD, BIK (benefit-in-kind) adjustments not in original payroll runs, or year-end true-ups.

### Cross-check 6 — Close company surcharge (s440 / s441 TCA 1997) — corporates only

If the entity is a close company (Irish private company under control of 5 or fewer participators):

**Close company surcharge table**

| Item | Source | Rule |
| --- | --- | --- |
| Estate / investment income retained > 18 months | ie-corporation-tax | 20% surcharge on undistributed investment / estate income |
| Service company surcharge | ie-corporation-tax | 15% on undistributed trading income for service companies (s441) |
| Distributions made within 18 months of period end | ie-corporation-tax | Reduce surchargeable amount |

**Flag:** Close company status often missed; assembly must always check.

### Cross-check 7 — Tolerance discipline

- **Tolerance rule** — For every cross-check above, the threshold is **€1**. If a difference is between €1 and €100, document the variance and proceed with a reviewer flag. If above €100, raise as "Needs Input" — the reviewer should resolve before sign-off.

## Section 4 — Working paper template: individual Form 11

The working paper is built around the ROS Form 11 panel structure. Form 11S (short form) is for simpler cases meeting Revenue's published criteria; the assembly skill picks the correct form based on intake.

### 4.1 Form 11 — panel-by-panel

**Form 11 panels table**

| Panel | Field | Description | Source |
| --- | --- | --- | --- |
| **Personal Details** | PPSN, name, address, marital / civil status, basis of assessment, spouse PPSN if joint | All | Intake |
| **Self-Employed Income (Schedule D Case I/II)** | Trading profit per accounts | Bottom-line trading profit | ie-income-tax-form11 |
|  | Add-backs (depreciation, entertainment, private use) | Tax adjustments | ie-income-tax-form11 |
|  | Capital allowances (wear & tear, IBA, energy-efficient) | Per s284 / s291A TCA 1997 | ie-income-tax-form11 |
|  | Adjusted Case I/II profit | Computed | ie-income-tax-form11 |
|  | Losses brought forward (s382 TCA 1997) | Used against same-trade profit | ie-income-tax-form11 |
|  | Losses set sideways (s381 TCA 1997) | Set against other income — election required | ie-income-tax-form11 |
| **PAYE / BIK Income (Schedule E)** | Salary, BIK, share option gains | All employment-source | ie-paye |
| **Foreign Income (Schedule D Case III)** | Foreign trading / employment / rental / investment | Including FTC | ie-income-tax-form11 |
| **Rental Income (Schedule D Case V)** | Net rental income after allowable deductions; pre-letting expenses; PRTB registration check | s97 TCA 1997 framework | ie-income-tax-form11 |
| **Investment Income (Schedule D Case IV / F)** | Deposit interest (DIRT applied — final liability for most; PRSI / USC may still apply); dividends | All | ie-income-tax-form11 |
| **Capital Gains** | Disposals 2025; €1,270 annual exemption; 33% rate; entrepreneur relief (10% on lifetime €1m under s597AA) | All | ie-cgt |
| **USC** | Bands applied; surcharge on non-PAYE > €100,000 (3% under s531AN) | All | ie-usc |
| **PRSI Class S** | 4.1% (4.2% from 1 Oct 2025); €650 minimum | All | ie-prsi-class-s |
| **Tax Credits** | Personal (€2,000 / €4,000 married 2025); PAYE (€2,000); Earned Income (€2,000); Home Carer; SPCCC; Age Tax Credit; etc. | All | ie-income-tax-form11 |
| **Withholding / Credits** | PAYE withheld; PSWT (s522); DIRT (s257); foreign tax credit (DTR) | All | ie-income-tax-form11 + ie-paye |
| **Final Liability** | Income tax + USC + PRSI − credits − withholding | Computed | All |
| **Preliminary Tax 2026** | 100%/90%/105% safe harbour amount | s959AN TCA 1997 | ie-preliminary-tax |

### 4.2 Schedules / panels checklist

**Schedules checklist table**

| Schedule | Title | When used |
| --- | --- | --- |
| Trading accounts panel | Extracts of accounts (income, expenses, profit) | All self-employed |
| Capital allowances schedule | Wear & tear pools; balancing allowances / charges | If business assets |
| Rental computation | Per-property net rent | If Case V income |
| CGT computation | Disposal-by-disposal | If chargeable gains |
| Foreign income & DTR | Foreign source detail | If non-Irish income |
| EII / SCI / FII relief claim | Investment relief panels | If subscriptions made |
| Pension contributions panel | Age-related percentage cap (15% < 30 to 40% ≥ 60), €115,000 earnings cap | If pension paid for the year (deadline 31 Oct / mid-Nov for current-year relief) |

### 4.3 PAYE-vs-chargeable-person decision

- **Routing rule** — If non-PAYE income is below €5,000 gross / €5,000 net, the taxpayer can file **Form 12** instead of Form 11. The assembly skill checks this at intake and routes to the correct working paper template.

### 5.1 CT1 — panel-by-panel

**CT1 panels table**

| Panel | Field | Description | Source |
| --- | --- | --- | --- |
| **Company Details** | CRO number, TRN, name, registered office, accounting period | All | Intake |
| **Trading Income (Case I/II)** | Turnover, COGS, expenses, profit per accounts | All | ie-corporation-tax |
|  | Add-backs (depreciation, client entertainment, motor expenses, etc.) | All | ie-corporation-tax |
|  | Capital allowances (W&T at 12.5% straight line typical) | s284 TCA 1997 | ie-corporation-tax |
|  | Adjusted Case I/II profit | Computed | ie-corporation-tax |
|  | Losses forward (s396 TCA 1997) | Same-trade carry-forward | ie-corporation-tax |
|  | Group / consortium relief (s411/s420 TCA 1997) | If group exists | ie-corporation-tax |
| **Passive / Investment Income (Case III/IV/V)** | Rental, interest, foreign income | Charged at 25% (s21A) | ie-corporation-tax |
| **Chargeable Gains** | Disposals re-grossed under s78 to give effective 33% rate | All | ie-cgt |
| **R&D Tax Credit** | 25% (or 30% on first €75,000 from 2025 budget) of qualifying R&D expenditure (s766) | If R&D claim made | ie-corporation-tax |
| **Close Company Surcharges** | s440 (investment income) 20%; s441 (service company trading) 15% | If close company | ie-corporation-tax |
| **Tax Computation** | 12.5% trading + 25% passive + 33% gains + surcharges − credits | All | ie-corporation-tax |
| **Preliminary Tax** | "Large company" (CT > €200,000 prior year): two payments — 50% by month 6, balance to 90% by 31st of month 11; "Small company": single payment of 100% prior year or 90% current year by 31st of month 11 (s959AS TCA 1997) | ie-corporation-tax + ie-preliminary-tax |  |
| **Final Balance** | Final balance due 23 days after 9-month CT1 due date | Computed |  |

### 5.2 CT1 panels checklist

**CT1 panels checklist table**

| Panel | Title | When used |
| --- | --- | --- |
| Trading account / iXBRL accounts | Financial statements tagged in iXBRL | All companies (filing exemption for very small / qualifying micro entities — verify thresholds against Revenue eBrief 2024/25) |
| Capital allowances | Plant & machinery, IBA, energy-efficient | If capex |
| R&D | s766 / s766A / s766C panels | If R&D claim |
| Transfer pricing | Local file / master file references | If TP regime applies (turnover > €50m group threshold under s835D-G TCA 1997, post-Finance Act 2019) |
| CFC | Controlled Foreign Company rules (s835I et seq, transposing ATAD) | If CFC interest |
| Hybrid mismatches | s835AA et seq | If hybrid arrangements |
| Interest limitation (ILR) | s835AY et seq, transposing ATAD | If interest > €3m de minimis |
| Pillar Two (QDMTT / IIR / UTPR) | Top-up tax for in-scope groups (revenue ≥ €750m) under Part 4A TCA 1997 (Finance (No. 2) Act 2023) | If in scope |

### 5.3 Close company status verification (always)

- **Close company checks** — For every CT1, the assembly skill confirms close company status: - **Close company test:** Irish resident company under control of 5 or fewer participators OR controlled by participators who are directors (s430 TCA 1997) - If close: check s440 (20% surcharge on undistributed estate / investment income) and s441 (15% surcharge on undistributed service company trading income) - Distributions made within 18 months of period end reduce the surchargeable amount  _(s430 TCA 1997)_

## Section 6 — Payment instructions: ROS payment channels

Under Revenue's electronic-filing mandate, payments are settled via the Revenue Online Service (ROS) or via myAccount for non-ROS individuals.

### 6.1 Payment channels

**Payment channels table**

| Channel | Description | Best for |
| --- | --- | --- |
| **ROS Debit Instruction (RDI / SEPA Direct Debit)** | Bank account is debited on the due date; mandate set up in ROS | Preliminary tax monthly SDD (105% safe harbour); large companies' biannual CT preliminary |
| **ROS EFT (Electronic Funds Transfer)** | Pay via online banking using Revenue's bank details + reference number | Larger one-off payments |
| **Debit / credit card via ROS or myAccount** | Card payment (small surcharge may apply on credit) | One-off smaller balancing payments |
| **myAccount Payment** | For individuals not registered for ROS | Form 12 balancing amounts |
| **Cheque / bank giro** | Legacy channel; Revenue discourages — paper filings restricted | Rare; not for ROS-mandated filers |

### 6.2 Payment timing relative to filing — Individuals (Form 11)

**Individual payment timing table**

| Payment | Due date | Reference |
| --- | --- | --- |
| 2025 balance of income tax / USC / PRSI | **31 October 2026** paper / **mid-November 2026** via ROS pay & file (extended date announced each year — TBC; verify on revenue.ie before filing) | s959AN TCA 1997 |
| 2026 preliminary tax (income tax / USC / PRSI) | **31 October 2026** / mid-November 2026 via ROS | s959AN TCA 1997 |
| 2025 CGT — December disposals | **31 January 2026** | s959AN |
| 2025 CGT — January–November disposals | Paid by **15 December 2025** as "initial period" CGT | s959AN |

- **Filing and payment concurrency rule** — **Rule:** Filing and payment are concurrent — Form 11 cannot be marked complete on ROS without the payment instruction lodged.

### 6.3 Payment timing relative to filing — Companies (CT1)

**Company payment timing table**

| Payment | Due date | Reference |
| --- | --- | --- |
| CT1 filing | **9 months after period-end**, but no later than the **23rd of the 9th month** (e.g., year-end 31 Dec 2025 → CT1 due 23 Sep 2026) | s959AA TCA 1997 |
| Final balance of CT | Same as CT1 filing date | s959AA |
| Small-company preliminary tax | **Single payment**: by **23rd of month 11** of accounting period (e.g., year-end 31 Dec 2025 → 23 Nov 2025); 100% prior-year or 90% current-year | s959AS |
| Large-company preliminary tax (CT > €200,000 in prior period) | **First instalment** (45% of prior or 50% of current): 23rd of month 6; **Second instalment** (top to 90% of current year): 23rd of month 11 | s959AS / s959AT |

### 6.4 Payment timing — VAT, CGT, CAT, PAYE/PRSI

**VAT/CGT/CAT/PAYE timing table**

| Payment | Due date | Reference |
| --- | --- | --- |
| VAT3 bi-monthly | **19th of month following period** (paper) / **23rd of month following period** (ROS) | s76 VATCA 2010 |
| RTD (annual VAT statement) | Same as final bi-monthly VAT3 for the year (typically Jan filing for Nov-Dec period) | Revenue eBrief |
| Monthly PAYE / USC / PRSI (P30) under PMOD | **14th of following month** (paper) / **23rd of following month** (ROS) | s989 TCA 1997 / PMOD regs |
| CGT — initial period (1 Jan – 30 Nov disposals) | **15 December** of same year | s959AN |
| CGT — later period (1 Dec – 31 Dec disposals) | **31 January** following year | s959AN |
| CAT (IT38) | **31 October** following valuation date (or mid-Nov via ROS pay & file) | s46 CATCA 2003 |

- **Late payment interest rule** — **Rule:** Late payment attracts interest under s1080 TCA 1997 (currently 0.0219% per day, ≈ 8% p.a. for income tax / CT / CGT; 0.0274% per day, ≈ 10% p.a. for VAT / PAYE / fiduciary taxes). Penalty regime under s1077E TCA 1997 may also apply.  _(s1080 TCA 1997; s1077E TCA 1997)_

### 7.1 Filing channels

- **Mandatory eFiling regime** — Under Revenue's mandatory eFiling regime (s917EA TCA 1997 and Revenue regulations), most filings must go through ROS. Channels:  _(s917EA TCA 1997)_

**Filing channels table**

| Channel | Description | Best for |
| --- | --- | --- |
| **ROS Online Form** | Fill the form directly in the ROS browser interface | Most Form 11 / CT1 / VAT3 filers |
| **ROS Offline Application** | Download form template, complete offline, upload signed file | Larger / complex filers needing review before submission |
| **ROS Web Services API** | Direct integration from accounting / tax software | Agents, larger firms with software integration |
| **myAccount** | For individuals not registered for ROS — Form 12, PAYE balancing statements, statement of liability | PAYE individuals only |

### 7.2 Submission steps — Form 11 / CT1

1. **Log in to ROS** using ROS Digital Certificate (.p12 file + password); agents use TAIN-linked certificate
2. Select **Complete a Form Online** → choose Form 11 / Form 11S (individuals) or CT1 (companies) → choose tax year / accounting period
3. Complete each panel — values from the working paper
4. Attach **iXBRL accounts** (mandatory for CT1 filers per s884 TCA 1997 and Revenue eBrief, with exemptions for qualifying micro / small entities — confirm thresholds at filing time)
5. Run **Form Pre-Submission Check** — ROS validates arithmetic, schema, mandatory fields
6. Submit and lodge payment instruction (RDI / EFT / card)
7. Receive **ROS Notice of Acknowledgement** with Receipt Number — retain as legal proof of filing

### 7.3 Submission steps — VAT3 / RTD

1. Log in to ROS
2. **My Services → File a Return → VAT3** (or RTD)
3. Enter Box T1, T2, T3, T4, E1, E2, ES1, ES2, PA1, PA2 amounts
4. Submit and lodge payment (if T1 − T2 > 0)
5. Retain ROS receipt

### 7.4 Deadlines (tax year 2025 / accounting periods ending 2025)

**Deadlines table**

| Filer | Form | Paper deadline | ROS pay & file extended date (TBC for 2026) |
| --- | --- | --- | --- |
| Individual (chargeable person) | Form 11 / 11S | **31 October 2026** | Mid-November 2026 (Revenue announces each year — TBC; verify on revenue.ie) |
| Individual (PAYE non-chargeable) | Form 12 / Statement of Liability | No statutory deadline but 4-year window for refund claims | n/a |
| Company | CT1 | **9 months after period-end**, no later than **23rd of 9th month** | Same — ROS-only filing |
| VAT-registered trader | VAT3 (bi-monthly) | 19th of month following period | 23rd of month following |
| VAT-registered trader | RTD (annual) | With final VAT3 of year | Same |
| Capital gains | CG1 (or Form 11 CGT panel) | 31 October following year | Mid-Nov via ROS |
| Capital acquisitions | IT38 | 31 October following valuation date | Mid-Nov via ROS |

### 7.5 Late filing surcharge (s1084 TCA 1997)

**Late filing surcharge table**  _(s1084 TCA 1997)_

| Lateness | Surcharge |
| --- | --- |
| Up to 2 months late | **5%** of tax liability, capped at **€12,695** |
| More than 2 months late | **10%** of tax liability, capped at **€63,485** |

- **Surcharge applicability** — Surcharge applies even if the tax is fully paid — it is for late **filing**, not late **payment**. Late payment attracts interest under s1080 (see Section 6).  _(s1080 TCA 1997)_

## Section 8 — Reviewer brief contents

The reviewer brief is a single markdown file the credentialed reviewer (CAI / ACCA-IE / CTA) reads before sign-off.

```markdown
# Complete Return Package — [Taxpayer Name] — Tax Year 2025

## Executive Summary
- Filing entity: [Individual / Sole Trader / Company (Ltd / DAC / CLG)]
- PPSN / TRN / CRO: [identifiers]
- VAT number: [if applicable]
- Tax regime: [Form 11 / Form 11S / Form 12 / CT1]
- Accounting period (companies): [start - end]
- Final liability: €X
- Preliminary tax 2026 (individuals) / current-period preliminary CT (companies): €X
- Total credits: €X
- Balance due / refund: €X
- Filing deadline: [31 October 2026 / 23 [Month] 2026 / mid-November 2026 via ROS]

## Income Tax / Corporation Tax Computation
[From ie-income-tax-form11 or ie-corporation-tax]
- Panel-by-panel working paper
- Capital allowances schedule
- Losses tracker (s382 / s396)
- Foreign tax credit computation (DTR) if applicable
- R&D credit (s766) if applicable

## PRSI / USC (individuals)
[From ie-prsi-class-s + ie-usc]
- Class S liability with rate transition flag for 1 October 2025 (4.1% → 4.2%)
- USC band-by-band breakdown
- Self-employed surcharge (3% on non-PAYE > €100,000)

## Preliminary Tax
[From ie-preliminary-tax]
- Safe harbour chosen (100% prior / 90% current / 105% pre-preceding via SDD)
- Calculation working
- Payment instruction (SDD / EFT / card)

## VAT (if VAT-registered)
[From ireland-vat-return]
- Bi-monthly VAT3 summary
- Annual RTD reconciliation
- Cross-check to trading account turnover

## Payroll & PAYE (PMOD)
[From ie-payroll + ie-paye]
- P30 monthly returns reconciled
- Employment Detail Summary cross-check
- BIK adjustments
- Employer PRSI band (Class A / Class S for proprietary directors)

## Capital Gains
[From ie-cgt]
- Disposal-by-disposal schedule
- Annual exemption (€1,270) applied
- Entrepreneur relief (s597AA) if claimed
- Initial-period vs later-period payment split

## Capital Acquisitions (if applicable)
[From ie-cat]
- Gifts / inheritances in valuation date year
- Group A/B/C threshold check (s109 CATCA 2003)
- IT38 filing pathway

## Cross-Skill Reconciliation
- Turnover reconciliation: [pass/fail]
- Income tax / USC / PRSI total: [pass/fail]
- Preliminary tax safe harbour: [pass/fail]
- VAT3 ↔ RTD: [pass/fail]
- PMOD monthly ↔ EDS annual: [pass/fail]
- Close company surcharge check (corporates): [pass/fail]

## Reviewer Attention Flags
- Items requiring CAI / ACCA-IE / CTA judgement
- Mixed-use expenses; client entertainment (non-deductible — s840A)
- Related-party transactions (transfer pricing per s835D-G if in scope)
- Pension contributions on / before 31 October for current-year relief
- R&D claim documentation (TBC — confirm 30% rate on first €75,000 per latest Finance Act)
- EII / SCI subscription certificates (Form RICT)
- Close company surcharge exposure

## Positions Taken
[List with legislation citations]
- e.g., "12.5% trading rate applied — s21 TCA 1997"
- e.g., "Entrepreneur relief 10% applied on €X — s597AA TCA 1997"
- e.g., "Loss set sideways under s381 TCA 1997 election"
- e.g., "Earned Income Tax Credit €2,000 claimed — s472AB TCA 1997"
- e.g., "Pillar Two QDMTT not applicable — group revenue below €750m threshold"

## Planning Notes for 2026
- Monthly SDD for 2026 preliminary tax (105% safe harbour) — establish in ROS by January
- VAT thresholds (€42,500 services / €85,000 goods from 1 Jan 2025; verify if updated for 2026)
- Pension contribution headroom for 2026
- Capital allowances opening pools rolled forward
- Loss memorandum
- Legislative changes effective 1 January 2026 (Finance Act 2025 — TBC; review at year-end)
- USC band shifts (Budget 2026)
- PRSI rate transitions (4.2% Class S in force full-year 2026)
```

## Section 9 — Final taxpayer action list

```markdown
# Action List — [Taxpayer Name] — Tax Year 2025

## Immediate (before pay & file deadline)

### For individuals (Form 11) — deadline 31 October 2026 paper / mid-November 2026 ROS (TBC):
1. Confirm ROS Digital Certificate is current (renew every 2 years)
2. Confirm bank mandate is in place for SDD / EFT
3. Review the working paper against your records — especially trading account, capital allowances, pension
4. **By 31 October 2026:** Make any current-year pension contribution to obtain 2025 relief (s787 TCA 1997 deadline tied to pay & file)
5. **By 31 October 2026 / mid-Nov 2026:** Pay 2025 balance + 2026 preliminary tax via ROS
6. Submit Form 11 via ROS → save Notice of Acknowledgement (Receipt Number)
7. If filing CG1 separately for CGT, do so by the same date
8. If filing IT38 (CAT), do so by 31 October following valuation date

### For companies (CT1) — deadline 23rd of 9th month after year-end:
1. Confirm CT1 Digital Certificate is current
2. Prepare iXBRL-tagged accounts and attach (if required — verify micro/small entity exemption thresholds)
3. **By 23rd of month 6** (large companies only): Pay first preliminary CT instalment
4. **By 23rd of month 11**: Pay small-company preliminary CT in full OR large-company second instalment
5. **By 23rd of month 9 after year-end**: File CT1 + pay balance via ROS → save Receipt
6. File annual return (B1) with CRO separately — not a Revenue filing but commonly aligned

### Ongoing through 2026

| Item | Due |
|---|---|
| Bi-monthly VAT3 (if VAT-registered) | 19th paper / 23rd ROS of month following period |
| Monthly P30 (PAYE/USC/PRSI under PMOD) | 14th paper / 23rd ROS of following month |
| Annual RTD (VAT) | With final VAT3 of year |
| 2026 preliminary tax monthly SDD (if 105% safe harbour used) | Last working day of each month |
| Form 11 for 2026 | 31 October 2027 / mid-Nov 2027 ROS |
| Employer EDS confirmation under PMOD | Auto-generated; verify Dec |

## Record retention

Per s886 TCA 1997, accounting records must be retained for **6 years** from the end of the chargeable period (or 6 years after final settlement of any audit / appeal). This includes:
- Books of account and supporting invoices / receipts
- Bank statements
- VAT3, RTD, EDS, P30 acknowledgements
- ROS Receipt Numbers (filing proof)
- iXBRL accounts attachments

Records must be kept available in the State (Ireland), although electronic / cloud storage is acceptable provided Revenue can access them on demand.
```

## Section 9 — Final taxpayer action list

**Ongoing through 2026 table**

| Item | Due |
| --- | --- |
| Bi-monthly VAT3 (if VAT-registered) | 19th paper / 23rd ROS of month following period |
| Monthly P30 (PAYE/USC/PRSI under PMOD) | 14th paper / 23rd ROS of following month |
| Annual RTD (VAT) | With final VAT3 of year |
| 2026 preliminary tax monthly SDD (if 105% safe harbour used) | Last working day of each month |
| Form 11 for 2026 | 31 October 2027 / mid-Nov 2027 ROS |
| Employer EDS confirmation under PMOD | Auto-generated; verify Dec |

## Section 9 — Final taxpayer action list

- **Record retention rule** — Per s886 TCA 1997, accounting records must be retained for 6 years from the end of the chargeable period (or 6 years after final settlement of any audit / appeal). Records must be kept available in the State (Ireland), although electronic / cloud storage is acceptable provided Revenue can access them on demand.  _(s886 TCA 1997)_

## Section 10 — 2026 planning notes

The capstone produces a forward-looking section so the taxpayer arrives at next year's filing with no surprises.

### 10.1 Preliminary tax for 2026 (individuals)

- **Preliminary tax rules** — Computed in the upstream skill (`ie-preliminary-tax`). Rule: - **Default: 100% of 2025 liability** paid by 31 October 2026 (mid-Nov via ROS) - **90% of 2026 estimated liability** — useful if 2026 income lower; risky if estimate too low (interest under s1080 if shortfall) - **105% of 2024 ("pre-preceding") liability** — only available if paid monthly by SEPA Direct Debit; set up RDI mandate in ROS by January  _(s1080 TCA 1997)_

### 10.2 Pension contributions

- **Pension contribution rules** — - Pay before **31 October 2026** (paper) / mid-November 2026 (ROS pay & file) to claim 2025-year relief - Age-related % cap: <30: 15%; 30-39: 20%; 40-49: 25%; 50-54: 30%; 55-59: 35%; 60+: 40% — applied to net relevant earnings - Earnings cap: **€115,000** for relief purposes (s790A TCA 1997; verify current Finance Act for any change) - Standard Fund Threshold (€2m, with phased increase to €2.8m from 2026-2029 per Finance Act 2024 — TBC; verify current published schedule)  _(s790A TCA 1997)_

### 10.3 VAT planning

- **VAT threshold rules** — - Registration thresholds **from 1 January 2025**: **€85,000 goods** / **€42,500 services** (Finance (No. 2) Act 2023 s86) - If approaching threshold during 2026, register in advance — VAT becomes due from the first day of the period in which the threshold is breached  _(Finance (No. 2) Act 2023 s86)_

### 10.4 R&D tax credit (corporates)

- **R&D credit rules** — - Standard rate 25% on qualifying R&D expenditure (s766 TCA 1997) - **First €75,000** of qualifying expenditure attracts uplift to **30%** (Finance Act 2024 — TBC; verify current Finance Act language) - Three-year payable in cash refund (if no CT liability to offset) - Documentation: scientific narrative + financial schedule must be retained  _(s766 TCA 1997; Finance Act 2024)_

### 10.5 Pillar Two (in-scope groups only)

- **Pillar Two rules** — - QDMTT (Qualified Domestic Minimum Top-up Tax), IIR (Income Inclusion Rule), UTPR (Undertaxed Payments Rule) under Part 4A TCA 1997 (Finance (No. 2) Act 2023) - Applies to groups with consolidated revenue ≥ **€750m** in at least 2 of the last 4 fiscal years - GIR (GloBE Information Return) and DTT filing requirements per Revenue published guidance — TBC; verify on revenue.ie before filing  _(Part 4A TCA 1997; Finance (No. 2) Act 2023)_

### 10.6 Close company planning

- **Close company planning rules** — If the company is close: - Distribute investment / estate income within 18 months of period end to avoid 20% surcharge (s440) - Distribute service company trading income within 18 months to avoid 15% surcharge (s441) - Track participators and director-shareholdings  _(s440 / s441 TCA 1997)_

### 10.7 Legislative monitoring

- **Finance Act 2025** (typically enacted late December 2025) — review for 2026 changes
- **Budget 2026** (typically October 2025) — preview of Finance Act direction
- Monitor Revenue **eBriefs** through 2026 for procedural / interpretive updates

## Section 11 — Conservative defaults

**Conservative defaults table**

| Situation | Conservative default |
| --- | --- |
| Cross-skill reconciliation differs by > €1 | Flag as "Needs Input"; do not silently round |
| Preliminary tax safe harbour ambiguous | Default to **100% prior-year** rule; safest, most defensible |
| Chargeable-person status borderline (non-PAYE near €5,000) | Default to **Form 11** (chargeable person); over-files but never under-files |
| Close company status unclear (corporates) | Default to **close**; compute surcharges; flag for reviewer to confirm |
| Pension contribution claimed but no certificate | Exclude; flag for taxpayer to obtain |
| PSWT credit claimed but no F45 / F50 | Exclude; flag for taxpayer to obtain |
| EII / SCI relief claimed but no RICT certificate | Exclude; flag |
| BIK valuation method unclear | Default to **revenue-published OMV / cash equivalent**; flag |
| Capital allowances on mixed-use asset | Default to **business-use proportion 50%**; flag for evidence-based split |
| iXBRL accounts not yet tagged | Flag; cannot submit CT1 until tagged (unless qualifying micro/small entity) |
| ROS Digital Certificate expired | Flag; cannot submit until renewed |
| Foreign income with no DTR documentation | Disallow DTR credit; flag for certificate of residence / withholding statement |
| Related-party transactions undocumented | Flag transfer pricing risk; do not silently assume arm's-length |
| R&D claim documentation incomplete | Exclude credit; flag for narrative + schedule |
| Pillar Two scope unclear | Default to **not in scope** unless intake confirms ≥ €750m group revenue |

- **Tolerance rule (repeated for emphasis)** — €1 reconciliation tolerance. Any larger discrepancy is escalated, not absorbed.

## Section 12 — Refusals

- **R-IE-ASM-1** — Upstream skill did not run. Name the missing skill. Continue with available data; flag the gap; do not fabricate the missing computation.
- **R-IE-ASM-2** — Upstream self-check failed. Note the specific check; continue but flag.
- **R-IE-ASM-3** — Cross-skill reconciliation > €1. Raise as "Needs Input"; do not silently round.
- **R-IE-ASM-4** — Out of scope: stamp duty, customs / excise, VRT (Vehicle Registration Tax), DWT (Dividend Withholding Tax) reclaim procedures, LPT (Local Property Tax) assessment, PAYE Modernisation real-time interventions, complex transfer pricing dispute resolution, MAP / APA procedures. Flag for human specialist; do not attempt.
- **R-IE-ASM-5** — Out of scope: non-resident / non-domiciled remittance basis taxation, split-year residence, expatriate concession (SARP — Special Assignee Relief Programme), Foreign Earnings Deduction (FED). Refer to a specialist; this skill assumes full-year Irish tax residency and ordinary residence.
- **R-IE-ASM-6** — Out of scope: Section 110 SPV taxation, IREF (Irish Real Estate Fund) charge, qualifying investor AIF, REITs, ICAVs. Specialist regime; refer.
- **R-IE-ASM-7** — Out of scope: Pillar Two top-up tax detailed computation, GIR preparation, GloBE elections. Although flagged in scope check, detailed computation requires specialist Pillar Two skill (not yet built).
- **R-IE-ASM-8** — Intake incomplete. Name the missing intake field (PPSN, TRN, CRO, VAT number, marital status, dependants, ROS certificate). Cannot finalise the return until provided.
- **R-IE-ASM-9** — Asked to submit to ROS. This skill produces a working paper. Submission is the taxpayer's (or TAIN-registered agent's) action, after CAI / ACCA-IE / CTA review and sign-off. Decline politely; provide the filing instructions instead.

## Section 13 — Self-checks

- **Check IE-ASM-1** — All upstream skills required for the chosen form have produced output, or the gap is flagged.
- **Check IE-ASM-2** — Revenue / turnover reconciles between bookkeeping, ireland-vat-return RTD, and the chosen income / corporation tax skill within €1.
- **Check IE-ASM-3** — Total tax + USC + PRSI − credits − withholding ties to the final liability on the working paper.
- **Check IE-ASM-4** — Preliminary tax 2026 safe harbour chosen is explicitly named (100% prior / 90% current / 105% pre-preceding via SDD) with the supporting calculation.
- **Check IE-ASM-5** — VAT3 bi-monthly amounts sum to the annual RTD.
- **Check IE-ASM-6** — PMOD monthly P30 returns reconcile to annual Employment Detail Summary per employee.
- **Check IE-ASM-7** — For corporates: close company status confirmed; s440 / s441 surcharges considered.  _(s440 / s441 TCA 1997)_
- **Check IE-ASM-8** — For corporates: R&D claim (if any) has narrative + financial schedule referenced.
- **Check IE-ASM-9** — Pension contributions claimed: certificates / scheme references attached; deadline 31 Oct (paper) / mid-Nov (ROS) for current-year relief noted.
- **Check IE-ASM-10** — Filing deadline (31 October 2026 individuals / 23rd of 9th month after period-end for companies) explicitly stated in the action list with the correct date.
- **Check IE-ASM-11** — Record retention period (6 years per s886 TCA 1997) is stated.  _(s886 TCA 1997)_
- **Check IE-ASM-12** — Reviewer brief contains legislation citations (TCA 1997, VATCA 2010, CATCA 2003, Finance Acts) for every position taken.
- **Check IE-ASM-13** — ROS Notice of Acknowledgement (Receipt Number) retention is included in the action list.
- **Check IE-ASM-14** — Credentialed reviewer sign-off (CAI / ACCA-IE / CTA) is stated as a precondition in the executive summary and action list.
- **Check IE-ASM-15** — Late filing surcharge (s1084 — 5% capped €12,695 up to 2 months; 10% capped €63,485 beyond) and late payment interest (s1080) are explicitly flagged in the action list.  _(s1084 TCA 1997; s1080 TCA 1997)_

## Section 14 — Output files

The final output is **three files**:

1. **`[taxpayer_slug]_2025_ie_master.xlsx`** — Master workbook. Sheets: Cover, Identifiers, Form 11 (or CT1) Panels, Capital Allowances Schedule, Losses Tracker, PRSI/USC, Preliminary Tax, VAT Reconciliation, PMOD Reconciliation, CGT Schedule, Close Company Check (corporates), Cross-Check Summary, ROS Payment Schedule. Use live formulas where possible; verify no `#REF!` errors.

2. **`reviewer_brief.md`** — Markdown file with all Section 8 contents.

3. **`taxpayer_action_list.md`** — Markdown file with all Section 9 contents.

All three files are placed in `/mnt/user-data/outputs/` and presented to the user at the end.

If execution runs out of context mid-build, complete the computation work first and produce whichever formatted outputs are finished, then state clearly which deliverables are partial.

## Section 15 — Known gaps

1. iXBRL tagging of accounts is not produced by this skill; tagging must be done in an iXBRL-compliant tool (e.g., commercial tagging software) and the resulting file attached at ROS submission.
2. PDF form filling is not automated; values are entered into ROS using the working paper.
3. Audit attachment / iXBRL exemption thresholds for "qualifying micro" and "qualifying small" entities are subject to change — verify on revenue.ie before filing.
4. Transfer pricing local file / master file content is referenced but not assembled here (separate skill needed if in scope under s835D-G).
5. SARP, FED, remittance basis, and split-year residency are out of scope (Section 12).
6. Pillar Two QDMTT / IIR / UTPR detailed computation is out of scope (Section 12, R-IE-ASM-7).
7. Stamp duty, customs, VRT, LPT, DWT reclaim, MAP/APA all out of scope.
8. Some Finance Act 2024 / Finance Act 2025 figures (Standard Fund Threshold schedule, R&D 30% uplift, ROS pay & file extended date) are marked TBC — confirm against the latest published Finance Act and Revenue eBrief at filing time.
9. CRO annual return (Form B1) is referenced but is a CRO filing, not a Revenue filing — handled separately.

### Change log

**v1.0 (May 2026):** Initial release. Modelled on mt-return-assembly, us-ca-return-assembly, and id-return-assembly, adapted for Irish self-assessment regime, ROS filing, and PAYE Modernisation environment. Coordinates eleven upstream Ireland skills.

## Section 16 — Sources

**Sources table**

| Source | Reference |
| --- | --- |
| Taxes Consolidation Act 1997 (TCA 1997, as amended) | Income tax, corporation tax, capital gains tax, USC, PRSI Class S, preliminary tax, surcharges, interest, retention |
| Value-Added Tax Consolidation Act 2010 (VATCA 2010) | VAT framework, VAT3, RTD, registration thresholds |
| Capital Acquisitions Tax Consolidation Act 2003 (CATCA 2003) | CAT / IT38 |
| Finance Act 2024 | R&D 30% first €75,000 uplift; Standard Fund Threshold phased increase; other 2025 changes |
| Finance (No. 2) Act 2023 | VAT thresholds €85,000 / €42,500 (effective 1 Jan 2025); Pillar Two Part 4A TCA 1997 |
| s959AN / s959AS / s959AT TCA 1997 | Preliminary tax safe harbours (individuals + companies) |
| s1080 TCA 1997 | Interest on late payment |
| s1084 TCA 1997 | Late filing surcharge |
| s440 / s441 TCA 1997 | Close company surcharges |
| s382 / s396 TCA 1997 | Losses |
| s522 TCA 1997 | PSWT (Professional Services Withholding Tax) |
| s787 / s790A TCA 1997 | Pension contributions and earnings cap |
| s597AA TCA 1997 | Entrepreneur Relief CGT |
| s531AN TCA 1997 | USC self-employed surcharge 3% over €100,000 |
| s886 TCA 1997 | Record retention 6 years |
| s917EA TCA 1997 | Mandatory eFiling |
| s959B TCA 1997 | Chargeable person definition |
| s835D-G TCA 1997 | Transfer pricing |
| Part 4A TCA 1997 | Pillar Two |
| Revenue Commissioners | https://www.revenue.ie |
| ROS — Revenue Online Service | https://www.ros.ie |
| myAccount | https://www.ros.ie/myaccount-web/home.html |
| Companies Registration Office (CRO) | https://www.cro.ie (Form B1 annual return — separate filing) |
| Skill version | 1.0 |

## Footer disclaimer

*OpenAccountants — open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed and signed off by a credentialed Irish reviewer — Chartered Accountants Ireland (CAI), ACCA-IE, or a Chartered Tax Adviser (CTA, Irish Tax Institute) — before filing via the Revenue Online Service (ROS).*

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

## Section 2 — Required inputs from upstream skills

0. **Invoke ie-income-tax-form11** — Consume Schedule D Case I/II/III/IV/V income, standard rate cut-off, tax credits
