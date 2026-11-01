---
name: sa-return-assembly
description: Use this skill whenever asked to assemble, finalize, or package a Saudi Arabian annual tax return or Zakat declaration. Trigger on phrases like "Saudi return assembly", "ZATCA submission", "Saudi annual filing", "120-day deadline Saudi", "Zakat declaration", "Saudi CIT return", "assemble Saudi return", "finalize KSA return", "Saudi working paper", or "ZATCA filing package". This is the capstone orchestrator that pulls together outputs from sa-zakat, sa-corporate-tax, sa-withholding-tax, sa-rett, sa-gosi-saudization, sa-excise-tax, sa-formation, saudi-arabia-vat, and saudi-einvoice into a single unified working paper plus payment and filing instructions. It does not recompute anything itself, it reconciles upstream outputs, builds the line-by-line ZATCA working paper, generates SADAD billing instructions for ZATCA portal payment, and produces a reviewer brief and taxpayer action list. ALWAYS read this skill last when finalizing a Saudi tax return or Zakat declaration.
jurisdiction: SA
version: 1.1
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SA Return Assembly

## Saudi Arabia: Return Assembly (Capstone): Skill v1.1

## Scope


Intake and the content Guides have already collected the facts for this working paper. Use what they captured, and ask the user again only where something is missing or contradicts itself.

Specifically:

- **Do NOT ask "do you want me to assemble the full package".** The user asked for the return. Produce it.
- **Do NOT re-interrogate the user about residency, CR number, TIN, or ownership structure**: intake already captured this; trust the upstream packages.
- **Do NOT pause between reconciliation steps to check in.** Run all cross-checks in sequence; flag failures in the reviewer brief and continue.
- **Self-checks are targets, not blockers.** If a check fails, note it under "Reviewer Attention Flags" and continue.
- **Do NOT submit anything to ZATCA.** This skill produces a working paper plus filing instructions. A credentialed reviewer (SOCPA member, or recognised ICAEW / ACCA / US CPA practising in KSA) must review, and the taxpayer (or authorised representative) submits via the ZATCA portal.

**If you feel the urge to ask "how should I proceed", pick the most defensible path, proceed, and flag the decision for the reviewer.**


The final capstone skill for Saudi Arabian annual tax filings. It consumes the outputs of every other Saudi skill and assembles a single unified working paper covering one of:

- **Zakat declaration**: Saudi-owned and GCC-owned entities under Royal Decree No. M/40 (1405 AH) and the Implementing Regulations for Zakat Collection issued by ZATCA
- **Corporate Income Tax return (Form 800 series)**: foreign-owned (non-Saudi / non-GCC) entities under the Income Tax Law (Royal Decree No. M/1 of 1425 AH) and its Implementing Regulations
- **Mixed-entity return**: joint Saudi / foreign ownership; Zakat applied to the Saudi/GCC share, CIT applied to the foreign share, on a single combined return

The output is a reviewer-ready package: line-by-line ZATCA working paper, cross-skill reconciliation table, payment instructions (ZATCA portal → SADAD billing ID → Saudi bank channel), filing instructions, reviewer checklist, taxpayer action list, WPS / Saudization compliance check, and 2027 planning notes.

## Ask the client first

Intake normally holds these. Ask only for what is missing: ownership split with nationality, fiscal year-end and its day count, revenue, whether audited accounts exist, and payments to non-residents.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Zakat, Hijri year | 2.5% of the Zakat base | 2026 | Regulations art. 15, https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf |
| Zakat, other fiscal year | 2.5% / Hijri days x fiscal days | 2026 | same |
| Income tax on the non-Saudi share | 20% | 2026 | ZATCA guideline, https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf |
| WHT management fees | 20% | 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf |
| WHT royalties; land transport; other payments | 15% | 2026 | same |
| WHT dividends, rent, loan charges, insurance, technical and consulting services, air tickets and freight, international telecoms | 5% | 2026 | same |
| VAT monthly filing | annual supplies over SAR 40 million | 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Submit-VAT-Return-for-Oct-andQ3-2026.aspx |
| E-invoicing Wave 25 | VAT-liable revenue over SAR 187,500 in any of 2022 to 2025; integrate by 1 February 2027 | 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx |
| VAT mandatory registration | SAR 375,000 | 2026 | unverified |
| VAT voluntary registration | SAR 187,500 | 2026 | unverified |

### Section 1: Quick reference

**Section 1: Quick reference table**

| Field | Detail |
| --- | --- |
| Country | Kingdom of Saudi Arabia |
| Tax authority | Zakat, Tax and Customs Authority (ZATCA): formerly GAZT and Saudi Customs, merged in 2021 |
| Filing portal | ZATCA portal: https://zatca.gov.sa |
| Currency | SAR (Saudi Riyal) |
| Tax year (default) | Gregorian calendar year (1 Jan - 31 Dec); some entities approved for Hijri year; financial year of taxpayer if different by approval |
| Current tax year | 2026 (filing window opens 1 January 2027) |
| Annual return deadline | **Within 120 days of fiscal year-end** (31 December 2026 year-end → 30 April 2027) |
| Zakat declaration | Annual; return and payment within 120 days of the end of the Zakat year; a deadline on an official holiday moves to the next working day (Regulations art. 102) |
| CIT return | Annual Form 800 series (Form 8 and variants); due within 120 days of FYE |
| Mixed-entity return | Zakat portion + CIT portion on the same combined annual return |
| VAT return | **Monthly** (annual supplies over SAR 40 million) or **quarterly** (SAR 40 million or less); due by the last day of the month after the period (ZATCA 2026 calendar) |
| WHT return | **Monthly**; due by the 10th of the following month, plus an annual statement within 120 days of fiscal year-end (ZATCA WHT Guideline) |
| Excise return | **Every two months**; due by the last day of the month after the period, for example January and February 2026 by 31 March 2026 (ZATCA 2026 calendar) |
| RETT (Real Estate Transaction Tax) | Transaction-by-transaction at notarisation; 5% on real estate disposals |
| Confirmation receipt | ZATCA portal acknowledgement with submission reference and timestamp |
| Payment channel | ZATCA portal generates **SADAD bill** (with billing ID) → pay via any Saudi bank, internet banking, mobile app, or SADAD-enabled ATM |
| Audited financial statements | Unverified: required above ZATCA thresholds (old text: SAR 40M+ revenue) |
| Governing law | Zakat: Royal Decree M/40 (1405 AH) + Implementing Regulations for Zakat Collection 1445 H (Decision 1007, amended by Decision 1248); CIT: Royal Decree M/1 (1425 AH) Income Tax Law + Implementing Regulations; VAT: Royal Decree M/113 (1438 AH); Excise: Royal Decree M/86 (1438 AH); RETT: Royal Decree M/84 (1442 AH) |
| Skill version | 1.1 |
| Validated by | Pending: requires sign-off by SOCPA member (Saudi Organization for Chartered Public Accountants) or recognised ICAEW / ACCA / US CPA practising in KSA |

#### 1.1 What this capstone produces

A single reviewer-ready package containing:

1. **Master working paper (Excel)**: ZATCA-aligned schedules, cross-skill reconciliation, SADAD billing register
2. **Reviewer brief (Markdown)**: executive summary, Zakat / CIT / mixed split walk-through, positions taken, attention flags
3. **Taxpayer action list (Markdown)**: payments to make (SADAD bills to settle), ZATCA portal submission steps, deadlines, WPS / Saudization confirmations, record retention
4. **2027 planning notes**: VAT periodicity check, WHT monthly cadence, advance Zakat / CIT planning, Saudization tier maintenance, working capital optimisation for Zakat

### Section 2: Required inputs from upstream SA skills

The assembly skill does not recompute anything. It expects structured outputs from the following upstream Saudi skills. If an upstream skill did not run, the assembly notes the gap and continues with available data.

#### 2.1 Entity-type matrix: which upstream skills feed which return

**Entity-type matrix table**

| Entity ownership | Annual filing | Upstream skills consumed |
| --- | --- | --- |
| 100% Saudi / GCC-owned | Zakat declaration only | sa-zakat, saudi-arabia-vat, sa-withholding-tax, sa-gosi-saudization, sa-formation, saudi-einvoice |
| 100% foreign-owned | CIT return (Form 800) | sa-corporate-tax, saudi-arabia-vat, sa-withholding-tax, sa-gosi-saudization, sa-formation, saudi-einvoice |
| Mixed (Saudi/GCC + foreign) | Combined Zakat + CIT return: proportional split by ownership | sa-zakat AND sa-corporate-tax, plus all others |
| Listed on Tadawul with mixed shareholders | Combined Zakat + CIT: proportional by free float | sa-zakat AND sa-corporate-tax, plus others |
| Real estate disposer in the year | + RETT computation | sa-rett |
| Excise-taxable goods (tobacco, sugary drinks, energy drinks, soft drinks, sweetened beverages, e-cigarettes, electronic devices for vaping) | + Excise return | sa-excise-tax |

#### 2.2 Zakat declaration: inputs

**Zakat declaration inputs table**

| Upstream skill | Output consumed | Where it lands on the Zakat declaration |
| --- | --- | --- |
| `sa-zakat` | Zakat base computation under the Regulations, including the art. 27 minimum base; 2.5% for a Hijri year, scaled by art. 15 for any other fiscal year (365 days against 354 gives about 2.5777%); working capital adjustments | Main Zakat base schedule; Zakat liability line |
| `saudi-arabia-vat` | VAT-registered turnover; output VAT and input VAT positions (cross-check only) | Cross-check vs. revenue in financial statements |
| `sa-withholding-tax` | WHT suffered (rare for Saudi/GCC entities other than payments from abroad) and WHT agent obligations on payments to non-residents (5%, 15% or 20% by category) | WHT credits schedule; agent compliance check |
| `sa-gosi-saudization` | GOSI contributions (employer + employee), Saudization tier (Nitaqat: Platinum / High Green / Medium Green / Low Green / Yellow / Red), WPS file submissions via Mudad | Salary & wage schedule; compliance attestation |
| `sa-rett` | Real estate transaction tax paid on disposals during the year (5% RETT) | Disclosure schedule; not Zakat-deductible |
| `sa-excise-tax` | Excise paid and collected on taxable goods | Cross-check only: separate return |
| `sa-formation` | Entity structure: Commercial Registration (CR) number, TIN, MoC registration, shareholders' nationality split, paid-up capital | Identification block; ownership split for mixed entities |
| `saudi-einvoice` | E-invoicing compliance status (Fatoorah Phase 1 generation + Phase 2 integration with ZATCA) | Compliance attestation |

#### 2.3 CIT return (foreign-owned entities): inputs

**CIT return inputs table**

| Upstream skill | Output consumed | Where it lands on the CIT return |
| --- | --- | --- |
| `sa-corporate-tax` | CIT computation: accounting profit → taxable income via tax adjustments; CIT at 20% (general rate); 85% rate for upstream oil & gas; 20% for natural gas investment (Income Tax Law art. 7(b), as amended from 1 January 2018); permanent establishment determination | Form 800: main computation; tax adjustments schedule; depreciation schedule (under SA Income Tax Law Implementing Regulations) |
| `sa-withholding-tax` | WHT suffered (rare) and WHT agent obligations on payments to non-residents (20% management fees / 15% royalties / 15% other / 5% dividends, rent, loan charges, insurance, technical and consulting services, air tickets and freight, international telecoms; 15% land transport in the Kingdom: ZATCA WHT Guideline) | Tax credits schedule; agent compliance check |
| `saudi-arabia-vat` | Output and input VAT; VAT return reconciliation | Cross-check vs. revenue |
| `sa-gosi-saudization` | Employee GOSI, salary expense, Saudization tier compliance | Salary schedule; compliance attestation |
| `sa-rett` | RETT paid on disposals (deductible or capitalised per accounting policy) | Disclosure schedule |
| `sa-excise-tax` | Excise tax paid / collected | Cross-check only |
| `sa-formation` | CR number, TIN, MoC registration, shareholders' nationality, paid-up capital | Identification block |
| `saudi-einvoice` | Fatoorah compliance status | Compliance attestation |

#### 2.4 Mixed-entity return: proportional split

**Mixed-entity proportional split table**

| Step | Treatment |
| --- | --- |
| 1. Compute the Zakat base (equity method) | Per sa-zakat |
| 2. Compute the CIT taxable income | Per sa-corporate-tax |
| 3. Determine ownership split | From sa-formation (cap table at year-end) |
| 4. Apply Zakat to Saudi/GCC share of Zakat base × 2.5% | Zakat portion |
| 5. Apply CIT to foreign share of CIT taxable income × 20% (or applicable rate) | CIT portion |
| 6. Add WHT agent obligations | Same for both portions |
| 7. Combined liability on a single return submitted via ZATCA portal | One submission |

#### 2.5 Intake-required identifiers

**Intake-required identifiers table**

| Identifier | Required for |
| --- | --- |
| Commercial Registration (CR) number: issued by Ministry of Commerce | All entities |
| Tax Identification Number (TIN): issued by ZATCA | All entities |
| VAT registration number: 15 digits ending in `03` | If VAT-registered |
| ZATCA portal credentials (username + password + nafath / IAM) | All electronic submissions |
| MoC commercial registration certificate | All entities |
| Shareholders' nationality split (Saudi / GCC / foreign) | Mixed-entity determination |
| Fiscal year-end date | Determines 120-day deadline |
| Audited financial statements (where threshold met) | All entities above the SAR 40M revenue threshold (or other ZATCA-specified thresholds) |
| GOSI employer registration | All entities with employees |
| Mudad subscription (WPS platform) | All entities with employees |
| Nitaqat tier (Saudization) | Entities with 5+ employees |
| Saudi Customs importer / exporter identifier | If applicable |

- **Missing identifier handling**: If any identifier is missing, the assembly skill flags it as "Needs Input" and produces the working paper with placeholders rather than halting.

### Section 3: Assembly workflow

The capstone runs in eight phases. Each phase reads upstream output, runs reconciliation, and writes a section of the master working paper.

#### 3.1 Phase 1: Read intake & confirm scope

0. **Phase 1**: Confirm entity type: Saudi/GCC-owned / foreign-owned / mixed; confirm fiscal year-end (Gregorian default; Hijri or custom by ZATCA approval); compute the 120-day deadline from FYE; confirm whether RETT, Excise apply; confirm VAT periodicity (monthly if annual supplies exceed SAR 40M; otherwise quarterly)

#### 3.2 Phase 2: Ownership split (for mixed entities)

0. **Phase 2**: Read cap table from sa-formation; classify each shareholder as Saudi / GCC / foreign; compute Saudi+GCC % and foreign %; carry to mixed-entity computation

#### 3.3 Phase 3: Zakat base or CIT taxable income

0. **Phase 3**: For Saudi/GCC-owned (Zakat only): Read Zakat base from sa-zakat (subject to the art. 27 minimum base); apply 2.5% for a Hijri year, or the art. 15 day-count percentage for a fiscal year that differs, about 2.5777% for 365 days against a 354-day Hijri year. For foreign-owned (CIT only): Read CIT taxable income from sa-corporate-tax; apply 20% general rate (or specialised rates: 85% upstream petroleum; 30% natural gas); apply interest deduction limitation: 50% of EBITDA per ITL Art. 12 / Implementing Regulations; apply carry-forward loss rules: 25% annual cap per year against current-year income, no time limit on the loss. For mixed: compute both bases independently; apply proportional ownership split

#### 3.4 Phase 4: Withholding tax compliance

0. **Phase 4**: Read WHT agent obligations from sa-withholding-tax; verify monthly WHT returns filed by the 10th of the following month for each month of the year; reconcile total WHT remitted vs. total payments to non-residents × applicable rate. Rates (ZATCA WHT Guideline, May 2026): management fees 20%; royalties 15%; dividends 5%; rent 5%; loan charges 5%; insurance and reinsurance 5%; technical and consulting services 5%; air tickets, air or sea freight 5%; international telecommunications 5%; land transport within the Kingdom 15%; any other payments 15%

#### 3.5 Phase 5: VAT reconciliation

0. **Phase 5**: Annual VAT-able revenue per saudi-arabia-vat should equal financial statement revenue (after standard reconciling items: zero-rated exports, exempt items, output adjustments); annual output VAT vs. sum of monthly/quarterly returns; annual input VAT vs. sum of returns; net VAT position: refundable or payable

#### 3.6 Phase 6: GOSI, Saudization, WPS

0. **Phase 6**: Read GOSI contributions from sa-gosi-saudization; confirm WPS files submitted via Mudad for every month of the year; confirm Nitaqat tier (Platinum / High Green / Medium Green / Low Green / Yellow / Red) for entities with 5+ employees; Yellow/Red tier flags consequences: visa restrictions, work permit renewal issues, ZATCA may flag the file

#### 3.7 Phase 7: RETT and Excise (if applicable)

0. **Phase 7**: RETT: per sa-rett: 5% of real estate disposal value, paid at notarisation; disclosure only on the annual return. Excise: per sa-excise-tax: two-monthly returns; annual reconciliation. Sweetened drinks moved from a flat 50% to sugar-based tiers on 1 January 2026; take all excise rates from sa-excise-tax (unverified here)

#### 3.8 Phase 8: Final assembly

0. **Phase 8**: Build master Excel workbook; write reviewer brief; write taxpayer action list; generate SADAD billing register; generate 2027 planning notes

### Section 4: Working paper structure (for credentialed reviewer)

The reviewer is a **SOCPA member** (Saudi Organization for Chartered Public Accountants) or a recognised foreign credential practising in KSA: **ICAEW (UK)**, **ACCA**, or **US CPA**. They sign off before ZATCA submission. SOCPA is the primary local credential; foreign credentials are accepted by ZATCA for international firms and joint ventures.

#### 4.1 Master workbook sheets

**Master workbook sheets table**

| Sheet | Contents |
| --- | --- |
| Cover | Entity name, CR number, TIN, VAT number, fiscal year, return type (Zakat / CIT / Mixed), reviewer name, sign-off block |
| Identification | CR, TIN, VAT, MoC, GOSI employer ID, addresses, principal activity, NACE/ISIC equivalent |
| Ownership Split | Cap table at FYE; Saudi/GCC% and foreign% |
| Computation: Zakat | Equity-method base build; working capital adjustments; 2.5% application |
| Computation: CIT | Accounting profit → taxable income; tax adjustments; depreciation; interest deduction limit; loss carry-forward |
| Mixed-Entity Apportionment | Saudi/GCC share × Zakat; foreign share × CIT |
| WHT Schedule | All monthly WHT returns with SADAD billing IDs, payments to non-residents by category and rate |
| VAT Reconciliation | Monthly / quarterly VAT returns vs. annual revenue |
| GOSI & Saudization | Monthly GOSI returns, Nitaqat tier, WPS attestation |
| RETT (if applicable) | Each real estate disposal with notarisation date and 5% RETT paid |
| Excise (if applicable) | Two-monthly excise returns; annual reconciliation |
| E-Invoicing (Fatoorah) | Phase 1 generation status; Phase 2 integration status |
| SADAD Billing Register | Every payment with tax head, period, amount, SADAD billing ID, payment date, bank receipt |
| Cross-Check Summary | Pass/fail for each reconciliation |
| 2027 Planning | VAT periodicity, WHT monthly cadence, Saudization plan |

#### 4.2 Cross-skill reconciliations

- **Reconciliation tolerance rule**: Each cross-check must pass within tolerance (SAR 100 default; SAR 1,000 for larger entities). Failures flagged, not silently absorbed.

**Cross-check 1: Revenue reconciliation**

| Source | Comes from | Rule |
| --- | --- | --- |
| Financial statements revenue | Top of P&L | Anchor |
| sa-zakat / sa-corporate-tax revenue | Per upstream | Should equal anchor |
| saudi-arabia-vat aggregate annual output base | Sum of monthly/quarterly returns | Reconciles ± zero-rated exports, exempt sales, output adjustments |
| Bank deposits (if available) | Cross-check | Reconciles ± timing |

**Cross-check 2: Salary, GOSI, WPS**

| Source | Comes from | Rule |
| --- | --- | --- |
| sa-gosi-saudization annual GOSI contributions | Sum of monthly returns | Anchor |
| sa-corporate-tax / financial statement salary expense | P&L salaries line | Reconciles to (gross salaries) |
| WPS file submissions via Mudad | 12 monthly files | All present: no gaps |
| Nitaqat tier per Saudization | Per upstream | Confirm not Yellow / Red |

**Cross-check 3: WHT agent obligations**

| Source | Comes from | Rule |
| --- | --- | --- |
| Total payments to non-residents (per accounting records) | Per upstream | Anchor |
| WHT rate by category × payment amount | Per ITL Art. 68 | Should equal WHT remitted |
| Sum of monthly WHT returns | sa-withholding-tax | Must equal WHT due |
| Late WHT payment risk | 1% of the unpaid tax for every 30 days (ITL art. 77(a), ZATCA WHT Guideline) | Flag for reviewer |

**Cross-check 4: VAT reconciliation**

| Source | Comes from | Rule |
| --- | --- | --- |
| Annual output VAT | Sum of period returns | Anchor |
| 15% (standard rate from 1 July 2020) × VAT-able sales | Computed | Reconciles |
| Annual input VAT | Sum of period returns | Per saudi-arabia-vat |
| Zero-rated exports | Per saudi-arabia-vat | Disclosed separately |
| Exempt sales (financial services, residential rent etc.) | Per saudi-arabia-vat | Disclosed separately |

**Cross-check 5: RETT (if any disposals)**

| Source | Comes from | Rule |
| --- | --- | --- |
| Real estate disposals during the year | Per sa-rett | Anchor |
| 5% × disposal value | Should equal RETT paid at notarisation | RETT-1 form |
| VAT exemption confirmation | Real estate disposals are VAT-exempt (RETT replaces VAT on real estate from October 2020) | Disclosure check |

**Cross-check 6: Excise (if any)**

| Source | Comes from | Rule |
| --- | --- | --- |
| Two-monthly excise returns | Per sa-excise-tax | Anchor |
| Annual excise tax collected + paid | Sum of two-monthly returns | Reconcile |
| Excise-able goods register | Per sa-excise-tax | Rates per sa-excise-tax; sweetened drinks use sugar tiers from 1 January 2026 |

**Cross-check 7: E-Invoicing (Fatoorah)**

| Source | Comes from | Rule |
| --- | --- | --- |
| Phase 1 generation (since 4 December 2021) | All B2B and B2C invoices generated electronically | Compliance check |
| Phase 2 integration with ZATCA (rolled out in waves) | If wave is in scope, integration confirmed | Compliance check; if not yet in wave, note expected wave |
| QR code on each invoice | Mandatory | Spot-check sample |

**Cross-check 8: Working capital / Zakat adjustments**

| Source | Comes from | Rule |
| --- | --- | --- |
| Long-term liabilities (added to Zakat base) | Per sa-zakat | Anchor |
| Long-term assets (deducted from Zakat base) | Per sa-zakat | Anchor |
| Inventory financed by short-term borrowing | Per sa-zakat | Adjustment per Implementing Regulations |
| Provisions for doubtful debts | Per sa-zakat | Add-back rules per Implementing Regulations |

- **Cross-check 9: Tolerance discipline**: For Zakat / CIT base computation: SAR 100 default tolerance. For larger entities (> SAR 40M revenue): SAR 1,000 tolerance. Discrepancies between SAR 100 and SAR 10,000: flag and proceed. Above SAR 10,000: raise as "Needs Input" before sign-off.

### Section 5: Tax computation summary (Zakat / CIT / Mixed bottom line)

The bottom line of the return appears in the reviewer brief executive summary.

#### 5.1 Zakat declaration bottom line (Saudi/GCC-owned)

- **Zakat declaration bottom line formula**: Equity (capital + retained earnings + reserves)              SAR X Plus: Long-term liabilities                                  SAR X Plus: Provisions added back                                  SAR X Less: Long-term assets                                       SAR X Less: Other deductible items per Implementing Regulations    SAR X = Zakat base                                                 SAR X Apply art. 15 percentage           SAR X = Zakat liability                                            SAR X Less: Any advance Zakat paid                                 SAR X = Net Zakat payable                                          SAR X

#### 5.2 CIT return bottom line (foreign-owned)

- **CIT return bottom line formula**: Accounting profit before tax                                 SAR X Plus: Tax adjustments (non-deductible)                       SAR X Less: Tax adjustments (extra-deductible)                     SAR X = Taxable income                                             SAR X Interest deduction limit: 50% of EBITDA: apply if breached  SAR X Loss carry-forward (25% cap per year)                        SAR X = Final taxable income                                       SAR X CIT at 20% (general) / 85% (upstream petroleum) / 20% (natural gas) SAR X = CIT liability                                              SAR X Less: Foreign tax credit (treaty-based)                      SAR X Less: Any WHT credit (rare for resident filer)               SAR X Less: Any advance CIT paid                                   SAR X = Net CIT payable                                            SAR X

#### 5.3 Mixed-entity bottom line

- **Mixed-entity bottom line formula**: Zakat base × Saudi/GCC% × 2.5%                               SAR X (Zakat portion) Taxable income × foreign% × 20% (or applicable)              SAR X (CIT portion) Combined liability on single return                          SAR X

#### 5.4 Refund treatment

- **Refund treatment rule**: If net is refundable: claim is made on the ZATCA portal. Refunds are processed under the Tax Procedures Law; unverified processing time 30 to 60 days, longer if ZATCA selects for audit. If net is payable: must be settled via SADAD billing before the 120-day deadline (see Section 6).  _(Tax Procedures Law)_

### Section 8: WPS + Saudization compliance check

This section is critical because ZATCA increasingly cross-references labor compliance with tax filings, and Yellow/Red Nitaqat tier is flagged on the entity's file.

#### 8.1 WPS (Wage Protection System) via Mudad

- **WPS via Mudad requirements**: Every entity with employees must: Submit monthly WPS file via the **Mudad** platform (https://mudad.com.sa); Confirm all employees received salary via authorised bank channel; Submit no later than the salary disbursement deadline (typically 3 days after the salary date). **Capstone check:** Confirm 12 monthly WPS files were submitted for the year. If any gap, flag as a "Reviewer Attention" item: gaps in WPS are a compliance violation under Ministry of Human Resources and Social Development (MHRSD) regulations and can result in: - Visa block on the company - Suspension of work permit renewals - Civil penalties

#### 8.2 Saudization: Nitaqat tier

The Nitaqat program tracks Saudi national employment as a percentage of total workforce. Tiers (current framework):

**Nitaqat tier table**

| Tier | Status | Implications |
| --- | --- | --- |
| Platinum | Best | Maximum benefits; expedited services |
| High Green | High compliance | Normal services; favoured for govt contracts |
| Medium Green | Compliant | Normal services |
| Low Green | Compliant but marginal | Normal services; warning zone |
| Yellow | Non-compliant | Visa restrictions; cannot renew certain work permits |
| Red | Severely non-compliant | Severe visa/work permit restrictions; major risk for operations |

- **Capstone Nitaqat check**: **Capstone check:** Confirm Nitaqat tier per sa-gosi-saudization. If Yellow or Red, raise as a "Reviewer Attention" item: does not block the tax filing but is a major operational risk.

#### 8.3 GOSI confirmation

- **GOSI confirmation checks**: Confirm GOSI monthly contributions paid for all 12 months; Confirm employee numbers reconcile to financial statement salary expense; Unverified, take from sa-gosi-saudization: Saudi nationals employer 11.75% and employee 9.75%, both including SANED 0.75%; non-Saudi employer occupational hazards 2%. The old SANED 1%/1% conflicted with the GOSI FAQ

#### 8.4 Attestation block

The reviewer brief must include:

```
[ ] All 12 monthly WPS files submitted via Mudad
[ ] All 12 monthly GOSI returns filed and paid
[ ] Nitaqat tier confirmed as: ______________
[ ] No outstanding labor violations flagged with MHRSD
[ ] Employee count reconciles to financial statements
```

### Section 9: Year-end planning notes

#### 9.1 Zakat working capital optimisation (Saudi/GCC entities)

- **Zakat working capital planning**: The Zakat base under the equity method includes: Long-term liabilities (added); Long-term assets (deducted). Strategic planning at FYE: Accelerate qualifying long-term asset purchases before FYE to reduce Zakat base; Convert short-term debt to long-term (over 1 year) to add to Zakat base: but watch other consequences; Time inventory write-downs and provisions per Implementing Regulations; Test the art. 27 minimum Zakat base

#### 9.2 CIT interest deduction limit (foreign entities)

- **Interest deduction limit planning**: ITL Article 12 / Implementing Regulations cap interest deduction at 50% of EBITDA. Planning items: Forecast EBITDA and interest expense before FYE; Consider thin-cap restructuring if interest exceeds the cap; Carry-forward of denied interest: verify current rules in sa-corporate-tax  _(ITL Article 12)_

#### 9.3 WHT exemption certificates

- **WHT exemption certificate planning**: For payments to non-residents in treaty countries (Saudi Arabia has 50+ DTAs): Apply for WHT exemption / reduced rate certificate before payment; ZATCA processes certificate applications via the portal; Without certificate, full statutory WHT applies; refund claim possible but cash-tied-up for months

#### 9.4 Saudization workforce planning

Plan Nitaqat tier maintenance for 2027: hire Saudi nationals, train, retain; Use programs like HRDF / HADAF subsidies for Saudi training; Forecast Saudi national % by quarter to avoid tier drop

#### 9.5 VAT periodicity transition

If turnover crosses SAR 40M threshold, periodicity becomes mandatory monthly. Plan: Internal controls upgrade for monthly close; Reconciliation cadence; E-invoicing Phase 2 wave inclusion check

#### 9.6 E-Invoicing Phase 2 waves

ZATCA continues to phase in Phase 2 integration in waves. Wave 25 reaches SAR 187,500 of VAT-liable revenue in any of 2022 to 2025, with integration by 1 February 2027. Confirm: Has the entity received the wave notification? Is integration with ZATCA infrastructure complete? Is the entity exchanging cryptographic stamps / UUIDs correctly?

#### 9.7 RETT planning

- **RETT planning**: If real estate disposals are planned in 2027: RETT 5% on disposal value, paid at notarisation; RETT replaced VAT on real estate from 4 October 2020; Some exemptions (gifts between first-degree relatives, certain inheritance, etc.): verify per sa-rett

#### 9.8 Transfer pricing / BEPS

- **Transfer pricing / BEPS thresholds**: Saudi adopted OECD-aligned TP rules; entities meeting thresholds must prepare: Local File; Master File; Country-by-Country Report (CbCR): for MNEs above SAR 3.2 billion consolidated revenue. Not assembled here; reference via sa-corporate-tax.

### Section 10: Reviewer attestation block

The reviewer brief contains an attestation block:

```markdown
# Reviewer Attestation: [Entity Name]: FY 2026

Reviewer name: ____________________________________
Membership body: [ ] SOCPA   [ ] ICAEW   [ ] ACCA   [ ] US CPA practising in KSA
Membership number: ____________________________________
Date of review: ____________________________________

I have reviewed:
[ ] Zakat base computation per sa-zakat (Saudi/GCC entities)
[ ] CIT computation per sa-corporate-tax (foreign-owned entities)
[ ] Mixed-entity apportionment (where applicable)
[ ] Withholding tax compliance per sa-withholding-tax with SADAD billing verification
[ ] VAT reconciliation per saudi-arabia-vat
[ ] GOSI & Saudization compliance per sa-gosi-saudization
[ ] WPS file submissions via Mudad (12 monthly files confirmed)
[ ] Nitaqat tier confirmed (not Yellow / Red)
[ ] RETT disclosures per sa-rett (where applicable)
[ ] Excise reconciliation per sa-excise-tax (where applicable)
[ ] E-Invoicing (Fatoorah) Phase 1 + Phase 2 compliance per saudi-einvoice
[ ] Entity records per sa-formation
[ ] Cross-skill reconciliations within tolerance
[ ] All positions taken have legislative citations (ITL / Zakat IR / VAT IR / RETT)
[ ] Audited financial statements attached (where threshold met)

Sign-off: ____________________________________

I confirm the return is ready for ZATCA submission and that the taxpayer / authorised representative has been provided with the action list and SADAD billing register.
```

### Section 11: Final taxpayer action list template

```markdown
# Action List: [Entity Name]: FY 2026 (Saudi Arabia)

## Immediate (before 120-day deadline: i.e. by [deadline date])

#### Annual return submission
1. Log into ZATCA portal with TIN + password / Nafath
2. Open "Annual Zakat/Tax Return" → select form (Zakat / CIT / Mixed)
3. Enter computation values from working paper
4. Upload audited financial statements (SOCPA-signed) and supporting schedules
5. Submit return → save acknowledgement with submission reference and timestamp
6. Generate SADAD bill for the payable amount
7. Pay via Saudi bank (internet banking, mobile app, SADAD ATM, or branch teller)
8. Save SADAD payment confirmation
9. Verify "Paid" status in ZATCA portal within 1 to 2 business days

#### Final WHT remittance (if year-end month outstanding)
1. Confirm all 12 monthly WHT returns filed (by the 10th of the following month)
2. Confirm SADAD bills paid for each month

#### Final VAT remittance (if year-end period outstanding)
1. Confirm all VAT periods (monthly or quarterly) filed and paid
2. Verify "Paid" status for each period

#### Excise reconciliation (if applicable)
1. Confirm all two-monthly excise returns filed and paid
```

#### Monthly / periodic compliance through FY 2027

**Monthly / periodic compliance through FY 2027 table**

| Item | Tax head | Due |
| --- | --- | --- |
| WHT: payments to non-residents | Monthly WHT return | 10th of following month |
| VAT (monthly filer: turnover > SAR 40M) | VAT return | Last day of following month |
| VAT (quarterly filer) | VAT return | Last day of month after quarter |
| GOSI monthly contribution | GOSI portal | Around the 15th: verify |
| WPS file via Mudad | Mudad platform | After each salary disbursement (typically 3 days) |
| Excise two-monthly | Excise return | Last day of month after period |
| RETT | Per transaction | At notarisation |

#### Record retention

- **Record retention rule**: Per Tax Procedures Law and Zakat Implementing Regulations, records must be retained for **at least 10 years** kept in the Kingdom for Zakat Return documents (Zakat Regulations art. 110); the 6-year income tax period in the old text is unverified. Records include: Books of account (general ledger, sales register, purchase register); SADAD payment confirmations; ZATCA submission acknowledgements; VAT invoices (Fatoorah-compliant, with QR code); WHT certificates issued to non-residents; GOSI monthly returns and confirmations; WPS monthly files; Bank statements; Audited financial statements and auditor's reports; Cap table updates (mixed entities). Records must be retrievable in Arabic where ZATCA requests (some documents may be in English with Arabic translation on request).  _(Tax Procedures Law and Zakat Implementing Regulations)_

#### Compliance attestations to keep current

- [ ] CR renewal (annually, via MoC)
- [ ] VAT registration active
- [ ] GOSI employer registration active
- [ ] Mudad subscription active
- [ ] Saudization Nitaqat tier maintained at Medium Green or above
- [ ] E-Invoicing Phase 2 integration current

### Section 14: Output files

The final output is **three files**:

1. **`[entity_slug]_FY2026_sa_master.xlsx`**: Master workbook. Sheets per Section 4.1. Use live formulas where possible; verify no `#REF!` errors.

2. **`reviewer_brief.md`**: Markdown file with executive summary, computation walk-through, cross-check results, positions taken, attention flags, attestation block.

3. **`taxpayer_action_list.md`**: Markdown file with all Section 11 contents.

All three files are placed in `/mnt/user-data/outputs/` and presented to the user at the end.

If execution runs out of context mid-build, complete the computation work first and produce whichever formatted outputs are finished, then state clearly which deliverables are partial.

### Section 15: Known gaps

1. PDF form filling is not automated; the reviewer or taxpayer enters values into the ZATCA portal using the working paper.
2. ZATCA XML / API submission is not produced by this skill; integrations with ERP / e-invoicing solution providers handle that.
3. Auditor's report attachment is the taxpayer's responsibility; this skill flags audit requirement based on revenue threshold but does not produce the audit itself.
4. Transfer pricing Local File / Master File / CbCR content is referenced via sa-corporate-tax but not assembled here.
5. Treaty-based WHT reductions are referenced via sa-withholding-tax but specific DTA analysis is upstream.
6. Special regimes (Aramco upstream petroleum, natural gas investment, banking, insurance, SEZ, RHQ, NEOM, Red Sea Global, Qiddiya) are out of scope.
7. Sharia-board specific interpretations of Zakat base are out of scope; the capstone applies ZATCA Implementing Regulations as published.
8. Hijri-year conversions are handled by sa-zakat; the capstone uses the upstream output as-is.
9. Local labor compliance beyond WPS / Nitaqat (e.g., specific MHRSD inspections) is out of scope.
10. Customs duty interactions on imports / exports are out of scope; ZATCA merged with Saudi Customs in 2021 but the Customs Schedule is administered separately.

## Worked cases

**Case 1: a mixed entity bottom line.** Saudi share 60%, Zakat base SAR 2,000,000, taxable income SAR 500,000, 365-day fiscal year against a 354-day Hijri year. The combined figure on the return is SAR 70,932.20.

```oa-check
name: Combined Zakat and income tax
inputs:
  zakat_base: 2000000
  taxable_income: 500000
  saudi_share: 0.6
steps:
  - zakat: zakat_base * saudi_share * 0.025 / 354 * 365
  - income_tax: taxable_income * (1 - saudi_share) * 0.20
  - total: zakat + income_tax
expected:
  total: 70932.20
```

**Case 2: file on time or 40 days late?** A company with revenue of SAR 3,000,000 and unpaid income tax of SAR 100,000 files 40 days late. Option (a) gives the lesser of 1% of revenue and SAR 20,000, so SAR 20,000. Option (b), over 30 days, gives 10%, so SAR 10,000. The higher applies: SAR 20,000, plus the delay penalty of 1% for each full 30 days, SAR 1,000 for the one full 30-day period (treatment of the 10-day remainder is unverified). Filing on time costs neither.

```oa-check
name: Late income tax return, 40 days
inputs:
  revenue: 3000000
  unpaid: 100000
steps:
  - option_a: min(revenue * 0.01, 20000)
  - option_b: unpaid * 0.10
  - filing_penalty: max(option_a, option_b)
  - total: filing_penalty + unpaid * 0.01
expected:
  filing_penalty: 20000.00
  total: 21000.00
```

## When to refuse or refer


- **R-SA-ASM-1**: Upstream skill did not run. Name the missing skill. Continue with available data; flag the gap; do not fabricate the missing computation.
- **R-SA-ASM-2**: Upstream self-check failed. Note the specific check; continue but flag.
- **R-SA-ASM-3**: Cross-skill reconciliation > SAR 10,000. Raise as "Needs Input"; do not silently round.
- **R-SA-ASM-4**: Out of scope: upstream petroleum (Aramco-style 85% rate regime), natural gas investment (20% rate, specialist regime), banking under SAMA-regulated specialised regimes, insurance specialised regimes, listed Tadawul-specific reporting requirements beyond the standard ownership split, qualified investment funds (QIFs) under special regimes, Real Estate Investment Traded Funds (REITs) under specialised CMA rules, Special Economic Zones (Riyadh ITSEZ, Jazan, Ras Al-Khair, Cloud Computing Special Economic Zone, Special Integrated Logistics Zone), Regional Headquarters (RHQ) tax incentive regime, and entities in NEOM / Red Sea Global / Qiddiya with specialised arrangements. Flag for human specialist; do not attempt.
- **R-SA-ASM-5**: Out of scope: PE-only filings for non-resident contractors operating without local CR; pure-play offshore service permanent establishments under treaty-protected positions; transfer pricing assessments for MNEs above CbCR threshold (handled via sa-corporate-tax with specialist support); APA negotiations with ZATCA. Refer to a specialist.
- **R-SA-ASM-6**: Intake incomplete. Name the missing intake field (CR, TIN, VAT number, ownership split, fiscal year-end, audited FS, GOSI ID, Mudad subscription). Cannot finalise the return until provided.
- **R-SA-ASM-7**: Asked to submit to ZATCA. This skill produces a working paper. Submission is the taxpayer's (or their authorised representative's) action, after credentialed reviewer sign-off. Decline politely; provide the filing instructions instead.
- **R-SA-ASM-8**: Asked to confirm rates / thresholds without verification against current ZATCA regulations. Defer to sa-zakat / sa-corporate-tax / saudi-arabia-vat which carry the verified current-period figures. Flag any figure used here as "verify against current upstream skill output".
- **R-SA-ASM-9**: Asked to opine on Sharia compliance of Zakat base treatment. Decline: Sharia interpretation is the role of the entity's Sharia board or qualified scholar; the capstone applies ZATCA's Implementing Regulations as published, not independent Sharia analysis.

## Filing and payment

### Section 6: Payment instructions: ZATCA portal, SADAD billing

All Saudi tax payments flow through the ZATCA portal → SADAD billing mechanism.

#### 6.1 The ZATCA → SADAD flow

- **ZATCA to SADAD flow steps**: 1. **Log into ZATCA portal** at https://zatca.gov.sa with TIN + password (or via Nafath / national IAM) 2. **Navigate to "Returns and Payments"** → select the relevant return (Zakat / CIT / VAT / WHT / Excise) 3. **Submit the return**: the portal computes the liability based on entries; verify against the working paper 4. **Generate SADAD bill**: ZATCA issues a **SADAD billing ID** (numeric, typically 14 digits or as currently formatted) 5. **Pay via Saudi bank channel**: present the SADAD billing ID via: **Internet banking**: every Saudi bank has a SADAD payment tab; select biller "ZATCA" / "Zakat, Tax and Customs Authority" → enter billing ID → pay; **Mobile banking app**: same flow; **SADAD-enabled ATM**: select SADAD payments → ZATCA → enter billing ID; **Bank branch teller**: present billing ID for over-the-counter payment 6. **Payment receipt**: bank issues a SADAD payment confirmation; the payment auto-feeds to ZATCA's records against the TIN 7. **Verify in ZATCA portal**: payment status updates from "Pending" to "Paid"

#### 6.2 Common tax heads / SADAD bill mapping

**Common tax heads / SADAD bill mapping table**

| Tax head | ZATCA portal section | Periodicity | Used for |
| --- | --- | --- | --- |
| Zakat | Annual Zakat declaration | Annual (120 days from FYE) | Saudi/GCC entities |
| Corporate Income Tax | Annual CIT (Form 800) | Annual (120 days from FYE) | Foreign-owned entities |
| Mixed Zakat + CIT | Annual combined | Annual (120 days from FYE) | Mixed-ownership entities |
| VAT | Monthly or quarterly | Last day of following month | All VAT-registered |
| Withholding Tax | Monthly | 10th of following month | All WHT agents |
| Excise Tax | Two-monthly | Last day of month after period | Excise-able goods |
| RETT | Transaction-by-transaction | At notarisation | Real estate disposers |

#### 6.3 Payment timing relative to filing

**Payment timing relative to filing table**

| Payment | Due date | Filing reference |
| --- | --- | --- |
| Annual Zakat / CIT balance | **Within 120 days of FYE** (for 31 Dec 2026 FYE → 30 April 2027) | Annual return |
| Monthly VAT (turnover > SAR 40M) | Last day of following month | VAT return |
| Quarterly VAT (turnover ≤ SAR 40M) | Last day of month after quarter | VAT return |
| Monthly WHT | 10th of following month | WHT return |
| Two-monthly Excise | Last day of month after period | Excise return |
| RETT | At notarisation | Transactional |

- **Payment settlement rule**: The SADAD billing payment must be settled by the deadline. The annual return submission and the payment can be done in the same session via the portal.

#### 6.4 Penalties for late payment / filing

**Penalties for late payment / filing table**

| Item | Penalty | Source |
| --- | --- | --- |
| Late payment of income tax, WHT and advance payments | 1% of the unpaid tax for every 30 days | ZATCA Income Tax Guideline, https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf |
| Late payment of VAT | 5% of the unpaid tax for each month or part of a month | ZATCA fines page, https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/Penalties.aspx |
| Late income tax return | Higher of (a) 1% of total revenue capped at SAR 20,000 and (b) 5% of unpaid tax up to 30 days, 10% over 30, 20% over 90, 25% over 365 | ZATCA Income Tax Guideline, https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf |
| Late VAT return | 5% to 25% of the tax that should have been declared | ZATCA fines page, https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/Penalties.aspx |
| Late income tax registration | SAR 1,000 natural person; SAR 10,000 joint stock company; SAR 5,000 other | ZATCA Income Tax Guideline, https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf |
| Lower amount declared in a VAT return | 50% of the difference | ZATCA fines page, https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/Penalties.aspx |
| Fraud or false information, income tax and WHT | 25% of the tax difference | ZATCA Income Tax Guideline, https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf |
| Fines exemption initiative | Runs 1 July to 31 December 2026; excludes returns due after 30 June 2026, VAT Law art. 45 fines and evasion fines | ZATCA Simplified Guide, https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf |

### Section 7: Filing instructions: annual return within 120 days of FYE via ZATCA

#### 7.1 Filing channel

- **Filing channel rule**: All Saudi annual tax filings are submitted electronically through the **ZATCA portal** at https://zatca.gov.sa. Paper filings are not accepted for normal taxpayers.

#### 7.2 Submission steps

- **Submission steps**: 1. **Confirm CR / TIN validity**: both must be active in MoC and ZATCA records 2. **Prepare audited financial statements** if required (entities above SAR 40M revenue typically must attach audited FS signed by a SOCPA-licensed auditor) 3. **Log into ZATCA portal** with TIN + password / Nafath 4. **Navigate to "Returns and Payments"** → select "Annual Zakat/Tax Return" 5. **Choose the form**: Zakat declaration form (for Saudi/GCC); CIT Form 800 series (for foreign-owned); Combined declaration (for mixed) 6. **Enter the computation** using the working paper as source 7. **Upload attachments**: Audited financial statements (SOCPA-signed); Auditor's report; Cap table at FYE (mixed entities); Supporting schedules as required 8. **Validate**: portal runs arithmetic and schema checks; resolve errors 9. **Submit**: receive ZATCA acknowledgement with submission reference and timestamp 10. **Generate SADAD bill** for payable amount 11. **Pay via Saudi bank channel** (per Section 6) 12. **Save acknowledgement and SADAD payment confirmation**: legal proof of filing and payment

#### 7.3 Deadlines (illustrative: adjust to actual FYE)

**Deadlines table**

| Fiscal year-end | 120-day deadline | Notes |
| --- | --- | --- |
| 31 December 2025 | **30 April 2026** | Stated in the ZATCA 2026 calendar |
| 31 December 2026 | **30 April 2027** | Most common Gregorian filers |
| 31 March 2026 | **29 July 2026** | Some entities |
| 30 June 2026 | **28 October 2026** | Hijri-aligned filers |
| 30 September 2026 | **28 January 2027** | Some entities |
| Custom year-end approved by ZATCA | FYE + 120 days | Per approval |

- **Hijri filer conversion**: For Hijri-year filers, the 120 days runs from the Hijri year-end and is converted to Gregorian for portal submission.

#### 7.4 Extension of time

**Extension of time table**

| Item | Mechanism |
| --- | --- |
| Extension request | Application to ZATCA before deadline, citing grounds (typically audit delay or major operational disruption) |
| Typical extension | Unverified: 30 days; rarely more |
| Penalty during extension | Late payment penalty (1% per month) still accrues unless ZATCA grants a payment moratorium |

#### 7.5 Audit & assessment

For Zakat, ZATCA may assess or correct within 5 years of the Return deadline, 10 years where the Return was late, incomplete, unpaid or missing, with no limit in the art. 106(3) cases. The income tax period is unverified. Triggers (unverified) include:

- Significant book-to-tax adjustments
- Loss carry-forward usage
- Related-party transactions (transfer pricing: Saudi adopts OECD-aligned TP rules; Local File / Master File / CbCR thresholds apply)
- Refund claims
- Industry-specific risk profiling

## Completion checklist


All upstream skills required for the chosen return type have produced output, or the gap is flagged.

Ownership split is correctly classified between Saudi/GCC and foreign for mixed entities, with cap table support.

Zakat base (equity method) reconciles to the financial statements equity section; long-term liabilities and long-term assets correctly identified.

CIT taxable income reconciles from accounting profit through documented tax adjustments with ITL section references.

Interest deduction limit (50% of EBITDA per ITL Art. 12) is tested and applied if breached.

All 12 monthly WHT returns are confirmed filed; each has a SADAD billing ID and payment confirmation.

VAT reconciliation: annual revenue ties to sum of monthly/quarterly VAT returns ± documented reconciling items.

All 12 monthly WPS files via Mudad are confirmed submitted.

Nitaqat tier is identified; if Yellow or Red, raised as a Reviewer Attention item.

Audited financial statements are attached where threshold met (SAR 40M+ revenue or other ZATCA-specified threshold).

RETT disclosures are present for any real estate disposals during the year.

Excise reconciliation is present if entity deals in excise-able goods.

Fatoorah (e-invoicing) Phase 1 compliance confirmed; Phase 2 integration confirmed where wave applies.

120-day deadline is explicitly stated in the action list with the correct calendar date computed from FYE.

SADAD billing register lists every payable item with billing ID, amount, and payment status.

Record retention period (10 years for Zakat documents, art. 110) is stated in the action list.

Reviewer brief contains legislation citations (Royal Decree numbers, ITL articles, Zakat IR articles, VAT IR articles, RETT framework) for every position taken.

Credentialed reviewer (SOCPA / ICAEW / ACCA / US CPA) sign-off requirement is stated in the executive summary, attestation block, and action list.

For mixed entities, Saudi/GCC% × Zakat base × 2.5% PLUS foreign% × taxable income × applicable CIT rate equals the combined liability on the return.

WHT rates applied per the ZATCA WHT Guideline (20% management fees / 15% royalties / 15% other / 5% dividends, rent, loan charges, technical services).

## Legal instruments named in this skill


**Sources table**

| Source | Reference |
| --- | --- |
| Income Tax Law (ITL) | Royal Decree No. M/1 of 1425 AH (15 January 2004) and successive amendments; articles referenced throughout (Arts. 1 to 5, 12, 13, 27, 30, 68, 71, 72) |
| ITL Implementing Regulations | Issued by Ministerial Resolution; defines tax adjustments, depreciation, interest deduction limit, loss carry-forward, WHT mechanism |
| Zakat: Royal Decree | Royal Decree No. M/40 of 1405 AH and successor regulations |
| Implementing Regulations for Zakat Collection 1445 H | Minister of Finance Decision 1007, amended by Decision 1248 |
| VAT Law | Royal Decree No. M/113 of 1438 AH (4 November 2017); VAT Implementing Regulations issued by ZATCA |
| Excise Tax Law | Royal Decree No. M/86 of 1438 AH (29 May 2017); Excise Implementing Regulations |
| Real Estate Transaction Tax (RETT) | Royal Decree No. M/84 of 14/02/1442 AH (effective 4 October 2020); RETT Implementing Regulations |
| Tax Procedures Law | Common procedural framework for ZATCA-administered taxes; penalties, deadlines, assessment, appeals |
| E-Invoicing (Fatoorah) | ZATCA Resolution; Phase 1 effective 4 December 2021; Phase 2 phased waves from 2023 onward |
| GOSI: Social Insurance Law | Royal Decree No. M/22 of 1389 AH and amendments |
| Saudization (Nitaqat) | Ministry of Human Resources and Social Development decisions |
| WPS: Wage Protection System | MHRSD regulations via Mudad platform |
| Companies Law | Royal Decree No. M/132 of 1443 AH (effective 19 January 2023, replacing 1965 Companies Law): for entity structure, audit thresholds |
| ZATCA portal | zatca.gov.sa |
| Mudad portal | mudad.com.sa |
| GOSI portal | www.gosi.gov.sa |
| SOCPA: Saudi Organization for Chartered Public Accountants | socpa.org.sa |
| Ministry of Commerce (MoC): CR registry | mc.gov.sa |
| Ministry of Human Resources and Social Development (MHRSD) | hrsd.gov.sa |
| SADAD payment system | National bill-payment infrastructure operated by Saudi Central Bank (SAMA) |

## Change log

- **v1.0 (May 2026):** Initial release. Modelled on pk-return-assembly and us-ca-return-assembly, adapted for Saudi annual returns, ZATCA portal filing, SADAD billing payment flow, the Zakat / CIT / mixed-entity split, WPS + Saudization compliance integration, and Royal Decree-based statutory references. Coordinates nine upstream Saudi skills.

- **v1.1 (November 2026):** Moved to tax year 2026 and the method shape. Corrected the Zakat percentage and minimum base, withholding rates, VAT and excise due dates, penalties, record retention and e-invoicing wave.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read in full text: Implementing Regulations for Zakat Collection 1445 H, Minister of Finance Decision 1007, amended by Decision 1248: arts. 1, 3, 15, 27, 102, 106, 110 | https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf | 2026-11-01 |
| Read in full text: ZATCA, Taxpayers' Obligations: Zakat and Returns Calendar 2026 | https://zatca.gov.sa/en/MediaCenter/Publications/Documents/Zakat%20Declaration%20and%20Tax%20Returns%20Calendar%20(EN).pdf | 2026-11-01 |
| Read in full text: ZATCA, General Guideline for Withholding Tax, second version, May 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf | 2026-11-01 |
| Read in full text: ZATCA, Simplified Guideline for Income Tax, second version, May 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf | 2026-11-01 |
| Read in full text: ZATCA, Taxation Violation Fines (VAT) | https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/Penalties.aspx | 2026-11-01 |
| Read in full text: ZATCA, VAT returns for September and Q3 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Submit-VAT-Return-for-Oct-andQ3-2026.aspx | 2026-11-01 |
| Read in full text: ZATCA, Wave 25 e-invoicing criteria | https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx | 2026-11-01 |
| Read in full text: ZATCA, excise regulation amendments from 1 January 2026 (Arabic) | https://zatca.gov.sa/en/MediaCenter/News/Pages/excise-tax-regulation-2026.aspx | 2026-11-01 |
| Read in full text: ZATCA, Simplified Guide on cancellation of fines, as of 1 July 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf | 2026-11-01 |
| Read in full text: Ministry of Investment, updated Investment Law page | https://misa.gov.sa/activities/laws-regulations-copy/ | 2026-11-01 |

Not yet confirmed: the Income Tax Law and its Implementing Regulations were not opened directly (laws.boe.gov.sa did not connect), so articles are cited through the ZATCA guidelines above, and the English guidelines defer to the Arabic text. Also unconfirmed, and carried only where marked unverified: VAT thresholds of SAR 375,000 and SAR 187,500; Wave 24 criteria (seen in a search extract, page not opened); GOSI rates and the phase-in for new entrants; excise rates and sugar tier amounts; RETT rate, exemptions and the instrument number (the old text gave both Royal Order A/84 and Royal Decree M/84); interest limit, loss carry-forward and specialised oil and gas rates; audited accounts threshold; extension practice; refund timing; income tax record retention; Hijri year eligibility; treatment of GCC corporate owners and listed float; Nitaqat bands (the old skills disagree on Yellow); Investment Law in-force date; form names such as Form 800.


*OpenAccountants: open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed and signed off by a credentialed reviewer (SOCPA member, or recognised ICAEW / ACCA / US CPA practising in KSA) before filing via the ZATCA portal.*

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
