---
name: sa-return-assembly
description: Use this Guide to assemble a Saudi Arabia annual tax and Zakat working paper for tax year 2026 from completed intake and upstream computations. Trigger on Saudi return assembly, ZATCA filing package, mixed ownership, Zakat declaration, corporate income tax return or SADAD payment instructions. It reconciles ownership, revenue, VAT, withholding, employment, real estate, excise and e-invoicing evidence, produces a master workbook, reviewer brief and taxpayer action list, and records missing inputs. Rates and tax positions require their cited conditions. Unconfirmed rules remain non-operative holds. It does not submit to ZATCA, replace specialist computations or certify a return as ready while a material hold remains.
jurisdiction: SA
version: 1.2
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SA Return Assembly v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Saudi Arabia: Return Assembly (Capstone): Skill v1.2

## Scope


Intake and the content Guides have already collected the facts for this working paper. Use what they captured, and ask the user again only where something is missing or contradicts itself.

Specifically:

- **Do NOT ask "do you want me to assemble the full package".** The user asked for the return. Produce it.
- **Do NOT re-interrogate the user about residency, CR number, TIN, or ownership structure**: intake already captured this; trust the upstream packages.
- **Do NOT pause between reconciliation steps to check in.** Run all cross-checks in sequence; flag failures in the reviewer brief and continue.
- **Holds prevent finalisation.** Continue independent reconciliation, but a failed legal/factual check leaves the affected amount unavailable and the package partial.
- **Do NOT submit anything to ZATCA.** Produce a working paper for a professional authorised for this work in Saudi Arabia. Confirm that authority separately; a professional membership alone is not filing authority.

Continue supported evidence work. Never resolve an unknown legal rule by choosing the most defensible-looking tax treatment.


The final capstone skill for Saudi Arabian annual tax filings. It consumes the outputs of every other Saudi skill and assembles a single unified working paper covering one of:

- **Zakat declaration**: Saudi-owned and GCC-owned entities under Royal Decree No. M/40 (1405 AH) and the Implementing Regulations for Zakat Collection issued by ZATCA
- **Corporate Income Tax return (portal-approved form; historical Form 800 label on HOLD)**: foreign-owned (non-Saudi / non-GCC) entities under the Income Tax Law (Royal Decree No. M/1 of 1425 AH) and its Implementing Regulations
- **Mixed-entity return**: joint Saudi / foreign ownership; Zakat applied to the Saudi/GCC share, CIT applied to the foreign share, with form presentation held until the taxpayer's portal evidence is checked

The output is a reviewer-ready package: line-by-line ZATCA working paper, cross-skill reconciliation table, payment instructions (ZATCA portal → SADAD billing ID → Saudi bank channel), filing instructions, reviewer checklist, taxpayer action list, WPS / Saudization compliance check, and 2027 planning notes.

## Ask the client first

Intake normally holds these. Ask only for what is missing: ownership split with nationality, fiscal year-end and its day count, revenue, whether audited accounts exist, and payments to non-residents.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Zakat, Hijri year | 2.5% of the applicable Zakat base for an ordinary full Hijri year | 2026 | Regulations art. 15, https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf |
| Zakat, other fiscal year | 2.5% / actual Hijri-year days x actual fiscal-year days; commencement, cessation and mergers require arts. 14 to 15 review | 2026 | same |
| General income tax | 20% on taxable income allocated to the non-Saudi share of a resident capital company, or the covered non-Saudi resident business / Saudi PE; special sectors excluded | 2026 | ZATCA Income Tax Guideline sections 1, 2 and 4, PDF pp. 4 to 5: https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf |
| WHT management fees, when the scope test below is met | 20% | 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf |
| WHT royalties; land transport within the Kingdom; residual other payments, after category/scope review | 15% | 2026 | same |
| WHT dividends, rent, loan charges, insurance/reinsurance, technical and consulting services, air tickets or air/sea freight, international telecoms, subject to definitions and exclusions below | 5% | 2026 | same |
| VAT monthly filing | annual supplies over SAR 40 million | 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Submit-VAT-Return-for-Oct-andQ3-2026.aspx |
| E-invoicing Wave 25 | VAT-liable revenue over SAR 187,500 in any of 2022 to 2025; integrate by 1 February 2027 | 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx |
| VAT registration decision | HOLD pending current threshold and scope verification; no numeric default | 2026 | unverified |
| VAT voluntary eligibility | HOLD; taxable expenses and non-resident rules also require review | 2026 | unverified |

Apply a domestic rate only after confirming a resident payer or Saudi PE, a payment to a non-resident, a Saudi income source, the precise payment category and any PE connection, exclusion, exemption or documented treaty claim. [ZATCA WHT Guideline, sections 2 to 5](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf). The table is not a rate-selection default. Unknown category means HOLD the calculation, never choose the highest rate. Natural-person payer rules cover activity-related payments, not personal consumption. Exclusions include relevant oil/gas investment dividends and specified telecom network/roaming payments. Interbank loan returns require the specific maximum-90-day and certified-statement conditions; freight definitions exclude inbound shipping to Saudi ports. Payments connected with a recipient's Saudi PE and capital gains need the separate income-tax treatment. Read the category definition and any treaty before the rate, not after.

### Section 1: Quick reference

**Section 1: Quick reference table**

| Field | Detail |
| --- | --- |
| Country | Kingdom of Saudi Arabia |
| Tax authority | Zakat, Tax and Customs Authority (ZATCA): formerly GAZT and Saudi Customs, merged in 2021 |
| Filing portal | ZATCA portal: https://zatca.gov.sa |
| Currency | SAR (Saudi Riyal) |
| Fiscal period | Capture the taxpayer's registered dates and calendar basis; HOLD any calendar-eligibility conclusion or period change pending current law and approval evidence |
| Current tax year | 2026; use the registered fiscal period, not an assumed portal opening date |
| Annual return deadline | General annual period: 120 days after FYE. 31 December 2026 + 120 days = 30 April 2027 **before holiday/exception adjustment**; do not issue this as a final payment deadline until that adjustment is checked |
| Zakat declaration | Annual; return and payment within 120 days of the end of the Zakat year; a deadline on an official holiday moves to the next working day (Regulations art. 102) |
| CIT return | Approved portal form; general annual return within 120 days of FYE, subject to entity/cessation exceptions; historical Form 800/Form 8 labels on HOLD; [2026 calendar](https://zatca.gov.sa/en/MediaCenter/Publications/Documents/Zakat%20Declaration%20and%20Tax%20Returns%20Calendar%20(EN).pdf) |
| Mixed-entity return | Separate supported Zakat and income-tax components; HOLD the exact combined-return form/identifier until portal evidence |
| VAT return | **Monthly** (annual supplies over SAR 40 million) or **quarterly** (SAR 40 million or less); due by the last day of the month after the period (ZATCA 2026 calendar) |
| WHT return | Monthly statement/payment within the first 10 days of the following month **when withholding payments exist**; no nil monthly statement required. Annual summary normally within 120 days of FYE, partnerships within 60 days; [WHT Guideline section 5, PDF p. 30](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| Excise return | **Every two months**; due by the last day of the month after the period, for example January and February 2026 by 31 March 2026 (ZATCA 2026 calendar) |
| RETT (Real Estate Transaction Tax) | HOLD rate, exemptions, instrument and deadline; collect property transaction evidence and request specialist computation |
| Confirmation receipt | ZATCA portal acknowledgement with submission reference and timestamp |
| Payment channel | Supported income-tax invoice through SADAD; for Zakat, art. 102 permits SADAD bank transfer or another accepted means. HOLD exact bill format and other-tax/bank workflows until evidenced |
| Audited financial statements | HOLD any universal revenue threshold; obtain the actual entity-specific audit/attachment requirement |
| Governing law | Use the Sources table for provisions actually read. Historical RETT/Tax Procedures instruments below are non-operative holds |
| Skill version | 1.2 |
| Validated by | Pending independent review; professional authorisation and client-specific sign-off required before filing |

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
| 100% foreign-owned | CIT return (form identifier on HOLD) | sa-corporate-tax, saudi-arabia-vat, sa-withholding-tax, sa-gosi-saudization, sa-formation, saudi-einvoice |
| Mixed (Saudi/GCC + foreign) | Separate Zakat and income-tax bases and allocations; form presentation held until evidenced | sa-zakat AND sa-corporate-tax, plus other relevant workstreams |
| Listed on Tadawul with mixed shareholders | HOLD the special ownership allocation | Specialist review; no general free-float formula applied |
| Real estate disposer in the year | + RETT computation | sa-rett |
| Potential excise goods, including tobacco, drinks and vaping products | Collect goods and composition; HOLD product scope/registration/rates until sourced | sa-excise-tax for verification |

#### 2.2 Zakat declaration: inputs

**Zakat declaration inputs table**

| Upstream skill | Output consumed | Where it lands on the Zakat declaration |
| --- | --- | --- |
| `sa-zakat` | Zakat base computation under the Regulations, including the art. 27 minimum base; 2.5% for a Hijri year, scaled by art. 15 for any other fiscal year (365 days against 354 gives about 2.5777%); working capital adjustments | Main Zakat base schedule; Zakat liability line |
| `saudi-arabia-vat` | VAT-registered turnover; output VAT and input VAT positions (cross-check only) | Cross-check vs. revenue in financial statements |
| `sa-withholding-tax` | Separate supported credits from payer-agent obligations; use source/PE/category/treaty conditions before a rate. Resident/PE credits require the art. 68(g) test | Separate credit and agent schedules; [WHT Guideline section 5, PDF p. 31](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| `sa-gosi-saudization` | Actual contribution statements, payroll, Nitaqat result and WPS records; HOLD unverified rates, bands and legal compliance assertions | Salary reconciliation and open employment issues |
| `sa-rett` | Transaction facts and a separately sourced computation; HOLD rate, deadline, exemption, deductibility and capitalisation conclusions until verified | Property disclosure and reviewer issues |
| `sa-excise-tax` | Excise paid and collected on taxable goods | Cross-check only: separate return |
| `sa-formation` | Entity structure: Commercial Registration (CR) number, TIN, MoC registration, shareholders' nationality split, paid-up capital | Identification block; ownership split for mixed entities |
| `saudi-einvoice` | E-invoicing compliance status (Fatoorah Phase 1 generation + Phase 2 integration with ZATCA) | Compliance attestation |

#### 2.3 CIT return (foreign-owned entities): inputs

**CIT return inputs table**

| Upstream skill | Output consumed | Where it lands on the CIT return |
| --- | --- | --- |
| `sa-corporate-tax` | Accounting profit, supported taxable-income adjustments and general-rate allocation. HOLD interest, loss and specialised oil/gas computations until current-law review | Main computation and supporting schedules in the approved portal form |
| `sa-withholding-tax` | Separate supported credits from payer-agent obligations; use source/PE/category/treaty conditions before a rate. Resident/PE credits require the art. 68(g) test | Separate credit and agent schedules; [WHT Guideline section 5, PDF p. 31](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) |
| `saudi-arabia-vat` | Output and input VAT; VAT return reconciliation | Cross-check vs. revenue |
| `sa-gosi-saudization` | Actual contribution statements, payroll, Nitaqat result and WPS records; HOLD unverified rates, bands and legal compliance assertions | Salary reconciliation and open employment issues |
| `sa-rett` | Transaction facts and a separately sourced computation; HOLD rate, deadline, exemption, deductibility and capitalisation conclusions until verified | Property disclosure and reviewer issues |
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
| 4. Apply the applicable art. 15 percentage to the supported Saudi/GCC allocation | Zakat portion; do not apply a flat Hijri rate to a different fiscal period |
| 5. Apply CIT to foreign share of CIT taxable income × 20% (or applicable rate) | CIT portion |
| 6. Reconcile WHT agent obligations separately | Do not add monthly payer-agent WHT to annual taxpayer liability or treat it as a credit merely because it was remitted |
| 7. Present supported annual Zakat/CIT components | Confirm the actual approved portal form; combined-form identifier remains held |

#### 2.5 Intake-required identifiers

**Intake-required identifiers table**

| Identifier | Required for |
| --- | --- |
| Commercial Registration (CR) number: issued by Ministry of Commerce | All entities |
| Tax Identification Number (TIN): issued by ZATCA | All entities |
| VAT registration number: number copied from the certificate | If VAT-registered |
| Taxpayer portal access | Taxpayer/authorised representative uses their own account; record access readiness, never request their password |
| MoC commercial registration certificate | All entities |
| Shareholders' nationality split (Saudi / GCC / foreign) | Mixed-entity determination |
| Fiscal year-end date | Determines 120-day deadline |
| Audited financial statements (where required) | HOLD the old SAR 40M audit assertion; determine the actual entity-specific law and portal attachment requirement |
| GOSI employer registration | Capture employment evidence; HOLD the legal registration test if not separately verified |
| Mudad/WPS status | Capture employment evidence; HOLD legal scope/mandate pending current employer-specific review |
| Nitaqat tier (Saudization) | Capture actual status for employee workstreams; HOLD the old headcount trigger |
| Saudi Customs importer / exporter identifier | If applicable |

- **Missing identifier handling**: If any identifier is missing, the assembly skill flags it as "Needs Input" and produces the working paper with placeholders rather than halting.

### Section 3: Assembly workflow

The capstone runs in eight phases. Each phase reads upstream output, runs reconciliation, and writes a section of the master working paper.

#### 3.1 Phase 1: Read intake & confirm scope

0. **Phase 1**: Confirm entity/ownership evidence, registered fiscal period and actual days. HOLD calendar eligibility or a change until supported; do not impose a Gregorian default. Compute the unadjusted annual 120-day interval, check tax-specific holiday/exception rules, and record actual VAT periodicity from taxable supplies and portal evidence.

#### 3.2 Phase 2: Ownership split (for mixed entities)

0. **Phase 2**: Read cap table from sa-formation; classify each shareholder as Saudi / GCC / foreign; compute Saudi+GCC % and foreign %; carry to mixed-entity computation

#### 3.3 Phase 3: Zakat base or CIT taxable income

0. **Phase 3**: Obtain independently sourced Zakat and income-tax computations. For Zakat test art. 27 minimum and art. 28 maximum and apply art. 15 day scaling. Use 20% only for the ordinary income-tax scope in the rates table. **NON-OPERATIVE HOLD:** the inherited 50%-of-EBITDA instruction is withdrawn. The official Arabic regulations art. 9(2), PDF p. 10, describe a different loan-return formula with a bank exception; this compilation's later amendments require confirmation before computation. Loss carry-forward and specialised oil/gas rates are also held. No held figure enters taxable income. [Zakat Regulations](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf); [Income-tax regulations](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).

#### 3.4 Phase 4: Withholding tax compliance

0. **Phase 4**: Reconcile supported payments and WHT by category to statements and receipts. No-payment months do not require monthly nil statements. Follow the monthly and annual statement rules in the quick reference, including the partnership exception. Apply the rates table only with the scope/definition/exemption conditions; unknown category or treaty relief is a HOLD. [WHT Guideline sections 2 to 5](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

#### 3.5 Phase 5: VAT reconciliation

0. **Phase 5**: Annual VAT-able revenue per saudi-arabia-vat should equal financial statement revenue (after standard reconciling items: zero-rated exports, exempt items, output adjustments); annual output VAT vs. sum of monthly/quarterly returns; annual input VAT vs. sum of returns; net VAT position: refundable or payable

#### 3.6 Phase 6: GOSI, Saudization, WPS

0. **Phase 6**: Reconcile actual GOSI statements, payroll and WPS/Mudad records for the covered employment months and capture actual Nitaqat status. HOLD rates, headcount/band consequences, reporting deadlines and any assertion that ZATCA blocks a tax return for labour status.

#### 3.7 Phase 7: RETT and Excise (if applicable)

0. **Phase 7**: Collect RETT transaction support and excise period statements. **HOLD** any RETT rate, exemption, deadline or deductibility result until separately sourced. For excise reconcile the two-month periods in the [2026 calendar](https://zatca.gov.sa/en/MediaCenter/Publications/Documents/Zakat%20Declaration%20and%20Tax%20Returns%20Calendar%20(EN).pdf); sweetened-drink sugar-tier method changed from 1 January 2026 under the [Arabic announcement](https://zatca.gov.sa/en/MediaCenter/News/Pages/excise-tax-regulation-2026.aspx), but tier amounts and the final product calculation remain held.

#### 3.8 Phase 8: Final assembly

0. **Phase 8**: Build master Excel workbook; write reviewer brief; write taxpayer action list; generate SADAD billing register; generate 2027 planning notes

### Section 4: Working paper structure (for credentialed reviewer)

The reviewer must be professionally authorised for the engagement and submission in Saudi Arabia. Record their body, credential, authority and scope; **HOLD** the inherited assertion that SOCPA, ICAEW, ACCA or US CPA membership alone establishes Saudi filing authority.

#### 4.1 Master workbook sheets

**Master workbook sheets table**

| Sheet | Contents |
| --- | --- |
| Cover | Entity name, CR number, TIN, VAT number, fiscal year, return type (Zakat / CIT / Mixed), reviewer name, sign-off block |
| Identification | CR, TIN, VAT, MoC, GOSI employer ID, addresses, principal activity, NACE/ISIC equivalent |
| Ownership Split | Cap table at FYE; Saudi/GCC% and foreign% |
| Computation: Zakat | Supported base, minimum/maximum review and correct art. 15 period percentage |
| Computation: CIT | Accounting profit → taxable income; tax adjustments; depreciation; interest deduction limit; loss carry-forward |
| Mixed-Entity Apportionment | Saudi/GCC share × Zakat; foreign share × CIT |
| WHT Schedule | All monthly WHT returns with SADAD billing IDs, payments to non-residents by category and rate |
| VAT Reconciliation | Monthly / quarterly VAT returns vs. annual revenue |
| GOSI & Saudization | Monthly GOSI returns, Nitaqat tier, WPS attestation |
| RETT (if applicable) | Deed/transaction facts, separately verified computation/payment; otherwise HOLD |
| Excise (if applicable) | Two-monthly excise returns; annual reconciliation |
| E-Invoicing (Fatoorah) | Phase 1 generation status; Phase 2 integration status |
| SADAD Billing Register | Every payment with tax head, period, amount, SADAD billing ID, payment date, bank receipt |
| Cross-Check Summary | Pass/fail for each reconciliation |
| 2027 Planning | VAT periodicity, WHT monthly cadence, Saudization plan |

#### 4.2 Cross-skill reconciliations

- **Internal reconciliation convention, not a legal safe harbour**: SAR 100 comparison tolerance, or SAR 1,000 for a larger workbook, can prioritise flags. Every difference is documented. No tolerance authorises an incorrect return or overrides a material hold.

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
| WPS file submissions via Mudad | Actual records for covered payroll periods | Reconcile completeness; HOLD unverified legal deadlines |
| Nitaqat tier per Saudization | Actual upstream evidence | Capture result; HOLD band validity and consequences pending current-law check |

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
| Standard/zero/exempt classification and rate | Separately supported VAT calculation | HOLD any rate or exemption not verified for the transaction and period |
| Annual input VAT | Sum of period returns | Per saudi-arabia-vat |
| Zero-rated exports | Per saudi-arabia-vat | Disclosed separately |
| Exempt sales (financial services, residential rent etc.) | Per saudi-arabia-vat | Disclosed separately |

**Cross-check 5: RETT (if any disposals)**

| Source | Comes from | Rule |
| --- | --- | --- |
| Real estate disposals during the year | Per sa-rett | Anchor |
| Property tax computation and payment | Separately verified upstream computation | HOLD the old rate, notarisation timing and RETT-1 identifier |
| Property VAT treatment | Separately sourced current transaction treatment | HOLD the blanket assertion that RETT replaces VAT for every property disposal |

**Cross-check 6: Excise (if any)**

| Source | Comes from | Rule |
| --- | --- | --- |
| Two-monthly excise returns | Per sa-excise-tax | Anchor |
| Annual excise tax collected + paid | Sum of two-monthly returns | Reconcile |
| Excise-able goods register | Per sa-excise-tax | Rates per sa-excise-tax; sweetened drinks use sugar tiers from 1 January 2026 |

**Cross-check 7: E-Invoicing (Fatoorah)**

| Source | Comes from | Rule |
| --- | --- | --- |
| Phase 1 generation (4 December 2021) | Taxpayers subject to the regulation; take current technical scope from separately verified specifications | Compliance evidence; no universal invoice-type rule inferred |
| Phase 2 integration with ZATCA (rolled out in waves) | If wave is in scope, integration confirmed | Compliance check; if not yet in wave, note expected wave |
| Invoice-type technical requirements | Check the applicable current specifications | HOLD blanket QR/clearance/reporting assertions |

**Cross-check 8: Working capital / Zakat adjustments**

| Source | Comes from | Rule |
| --- | --- | --- |
| Liabilities in Zakat base | Source-supported upstream schedule | Do not assume all long-term liabilities are added without arts. 23 to 29 conditions |
| Assets deducted from Zakat base | Source-supported upstream schedule | Do not assume all long-term assets qualify for deduction |
| Inventory financed by short-term borrowing | Upstream documents and proposed adjustment | HOLD adjustment until exact current rule and conditions are supplied |
| Provisions for doubtful debts | Upstream documents and proposed add-back | HOLD treatment until exact current rule and conditions are supplied |

- **Cross-check 9: Internal tolerance discipline**: The inherited SAR 100 / SAR 1,000 bands and SAR 10,000 escalation point are workflow triage conventions, not statutory thresholds. Record every difference, escalate larger or legally material differences, and do not round away liability or finalise a held item.

### Section 5: Tax computation summary (Zakat / CIT / Mixed bottom line)

The bottom line of the return appears in the reviewer brief executive summary.

#### 5.1 Zakat declaration bottom line (Saudi/GCC-owned)

- **Zakat bottom line**: Use the supported upstream base after addition, deduction, minimum and maximum tests, then the applicable art. 15 percentage and ownership allocation. Subtract documented eligible advance payments once; do not treat an unexplained equity roll-forward as the statutory base. [Zakat Regulations arts. 15, 23 to 28](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf). Detailed adjustment and credit eligibility remains held if not sourced.

#### 5.2 CIT return bottom line (foreign-owned)

- **CIT bottom line**: Supported accounting profit + documented add-backs - documented deductions - legally supported loss relief = final taxable income; apply the covered general rate and foreign allocation once. **HOLD interest limitation, loss relief, foreign credits and specialised rates** until the exact current rule and conditions are checked. No 50%-of-EBITDA proxy is permitted. Credit/advance payments require evidence and must not duplicate the payer-agent WHT liability.

#### 5.3 Mixed-entity bottom line

- **Mixed-entity bottom line**: Supported Zakat base × relevant Saudi/GCC allocation × art. 15 period percentage; plus supported taxable income × relevant foreign allocation × applicable sourced income-tax rate. Confirm neither upstream base is already ownership-apportioned before multiplying again. Combined return presentation is verified against the taxpayer's portal.

#### 5.4 Refund treatment

- **Refund treatment HOLD**: Collect overpayment, return, assessment and payment evidence and request the tax-specific refund procedure. Do not promise the inherited 30 to 60 day processing range or cite an unverified common Tax Procedures Law. Payment obligations continue to follow their supported deadlines.

### Section 8: WPS + Saudization compliance check

This is an employment-evidence reconciliation. **HOLD** any claim that ZATCA cross-references labour status or that a particular Nitaqat band changes filing rights.

#### 8.1 WPS (Wage Protection System) via Mudad

- **WPS/Mudad HOLD**: Obtain payroll-period, employee and bank/submission records and reconcile completeness. The former universal monthly mandate, 3-day deadline and visa/work-permit/civil-penalty consequences are not operative here. Have the employment reviewer verify the employer category and current MHRSD rules before a compliance attestation.

#### 8.2 Saudization: Nitaqat tier

Capture the employer's actual Nitaqat classification. **HOLD:** the former tier-to-benefit/consequence table, including Yellow, until the current employer/sector rules are verified. The following is a data collection table, not a current legal band list.

**Nitaqat tier table**

| Tier | Status | Implications |
| --- | --- | --- |
| Platinum (legacy topic) | HOLD current status | Do not infer benefits, visa rights, permit rights or compliance |
| High Green (legacy topic) | HOLD current status | Do not infer benefits, visa rights, permit rights or compliance |
| Medium Green (legacy topic) | HOLD current status | Do not infer benefits, visa rights, permit rights or compliance |
| Low Green (legacy topic) | HOLD current status | Do not infer benefits, visa rights, permit rights or compliance |
| Yellow (legacy topic) | HOLD current status | Do not infer benefits, visa rights, permit rights or compliance |
| Red (legacy topic) | HOLD current status | Do not infer benefits, visa rights, permit rights or compliance |

- **Nitaqat check**: Record the actual documented result and refer unresolved labour issues. Do not require a named band as a tax-filing condition.

#### 8.3 GOSI confirmation

- **GOSI HOLD**: Reconcile actual statements and payments to employee records and payroll for covered months. No rate, wage cap, entrant phase-in or payment deadline is verified here; do not use the old percentages as an estimate.

#### 8.4 Attestation block

The reviewer brief must include:

```
[ ] Actual covered payroll periods and WPS evidence reconciled; legal compliance verified or held
[ ] GOSI statements and payments for covered employees/periods reconciled
[ ] Nitaqat tier confirmed as: ______________
[ ] No outstanding labor violations flagged with MHRSD
[ ] Employee count reconciles to financial statements
```

### Section 9: Year-end planning notes

#### 9.1 Zakat working capital optimisation (Saudi/GCC entities)

- **Zakat planning**: Identify proposed asset/debt/provision transactions and request a sourced before/after base calculation including arts. 25 to 28 placement/minimum/maximum tests. **HOLD** the old mechanical advice to accelerate assets, reclassify debt or time provisions merely to reduce the base. [Zakat Regulations](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

#### 9.2 CIT interest deduction limit (foreign entities)

- **Interest HOLD**: Do not plan or restructure using the withdrawn 50%-of-EBITDA assertion. Obtain the current loan-return rule, bank exception, actual finance costs/income and amendment history. Arabic regulations art. 9(2), PDF p. 10, use a different formula; no replacement calculation is applied until current applicability is resolved. [Official compilation](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf).

#### 9.3 WHT exemption certificates

- **Treaty planning**: Obtain residence, beneficial-owner, PE, payment and treaty evidence and verify the applicable relief procedure before applying a reduction. **HOLD** the old universal prepayment certificate/refund timing rule and treaty count. [WHT Guideline sections 4 to 5](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

#### 9.4 Saudization workforce planning

Collect the 2027 workforce plan and request employment review. **HOLD** legal quotas, tier consequences and subsidy eligibility until sourced; no hiring recommendation is made from an unverified band.

#### 9.5 VAT periodicity transition

Use actual annual taxable supplies, not total accounting turnover, for the SAR 40 million monthly/quarterly VAT test in the cited ZATCA notice. Plan the reconciliation cadence after confirming the actual period allocation. E-invoicing selection uses its own historical-year test.

#### 9.6 E-Invoicing Phase 2 waves

ZATCA continues to phase in Phase 2 integration in waves. Wave 25 requires revenue exceeding SAR 187,500 of VAT-liable revenue in any of 2022 to 2025, with integration by 1 February 2027. Confirm: Has the entity received the wave notification? Is integration with ZATCA infrastructure complete? Is the entity exchanging cryptographic stamps / UUIDs correctly?

#### 9.7 RETT planning

- **RETT planning HOLD**: Capture planned transaction, value, date and parties; obtain current law, exemption conditions and filing/payment dates before recommending timing or computing tax.

#### 9.8 Transfer pricing / BEPS

- **Transfer pricing HOLD**: Capture related-party/controlled transactions, group structure and consolidated revenue; refer for the current documentation, disclosure and CbCR tests. No inherited monetary threshold determines whether work is required.

### Section 10: Reviewer attestation block

The reviewer brief contains an attestation block:

```markdown
# Reviewer Attestation: [Entity Name]: FY 2026

Reviewer name: ____________________________________
Membership body and credential: __________________
Saudi professional/filing authority and engagement scope verified: __________________
Membership number: ____________________________________
Date of review: ____________________________________

I have reviewed:
[ ] Zakat base computation per sa-zakat (Saudi/GCC entities)
[ ] CIT computation per sa-corporate-tax (foreign-owned entities)
[ ] Mixed-entity apportionment (where applicable)
[ ] Withholding tax compliance per sa-withholding-tax with SADAD billing verification
[ ] VAT reconciliation per saudi-arabia-vat
[ ] GOSI & Saudization compliance per sa-gosi-saudization
[ ] WPS evidence for covered payroll periods reconciled
[ ] Actual Nitaqat result recorded; no unsupported legal consequence asserted
[ ] RETT disclosures per sa-rett (where applicable)
[ ] Excise reconciliation per sa-excise-tax (where applicable)
[ ] E-Invoicing (Fatoorah) Phase 1 + Phase 2 compliance per saudi-einvoice
[ ] Entity records per sa-formation
[ ] Cross-skill reconciliations within tolerance
[ ] All positions taken have legislative citations (ITL / Zakat IR / VAT IR / RETT)
[ ] Audited financial statements attached (where threshold met)

Sign-off: ____________________________________

Final status: [ ] Partial package with holds  [ ] Ready after all material holds resolved
I confirm the above status and that the taxpayer / authorised representative has the supported action list and payment register. Do not sign as ready while any material fact or legal position remains held.
```

### Section 11: Final taxpayer action list template

```markdown
# Action List: [Entity Name]: FY 2026 (Saudi Arabia)

## Immediate (before 120-day deadline: i.e. by [deadline date])

#### Annual return submission
1. Log into ZATCA portal with TIN + password / Nafath
2. Open "Annual Zakat/Tax Return" → select form (Zakat / CIT / Mixed)
3. Enter computation values from working paper
4. Upload the attachments actually required for the entity and return; HOLD an assumed audit threshold
5. Submit return → save acknowledgement with submission reference and timestamp
6. Generate SADAD bill for the payable amount
7. Pay via Saudi bank (internet banking, mobile app, SADAD ATM, or branch teller)
8. Save SADAD payment confirmation
9. Reconcile payment confirmation and portal status; HOLD any promised status-update time

#### Final WHT remittance (if year-end month outstanding)
1. Confirm statements/payment for months with withholding payments and the applicable annual summary; no nil-month statement assumed
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
| GOSI contribution | GOSI evidence | HOLD legal payment date pending current employer/entrant rules |
| WPS file via Mudad | Payroll evidence | HOLD reporting mandate/deadline pending employer-specific review |
| Excise two-monthly | Excise return | Last day of month after period |
| RETT | Property transaction workstream | HOLD rate, form and deadline |

#### Record retention

- **Record retention**: Keep Zakat return support within the Kingdom for at least 10 years under art. 110. WHT records last at least 10 years after payment and longer while the authority/competent body is considering the matter, under regulations art. 63(9)(c) and WHT Guideline section 5. Retain ledgers, invoices, contracts, receipts, returns, bank records and ownership support. **HOLD:** the old income-tax 6-year rule, blanket cross-tax retention rule and Arabic-translation assertion until separately sourced. [Zakat art. 110](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf); [WHT Guideline PDF p. 31](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

#### Compliance attestations to keep current

- [ ] CR status checked; HOLD any assumed annual renewal rule
- [ ] VAT registration active
- [ ] GOSI employer registration active
- [ ] Mudad subscription active
- [ ] Actual Nitaqat status recorded and employer-specific legal obligations verified or held
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
3. Audit/attachment requirement remains a HOLD until the actual entity-specific rule is sourced; this Guide does not produce an audit.
4. Transfer pricing Local File / Master File / CbCR content is referenced via sa-corporate-tax but not assembled here.
5. Treaty-based WHT reductions are referenced via sa-withholding-tax but specific DTA analysis is upstream.
6. Special regimes (Aramco upstream petroleum, natural gas investment, banking, insurance, SEZ, RHQ, NEOM, Red Sea Global, Qiddiya) are out of scope.
7. Sharia-board specific interpretations of Zakat base are out of scope; the capstone applies ZATCA Implementing Regulations as published.
8. Obtain the registered Hijri-period dates and checked conversion evidence; never accept an unsupported upstream calendar as final.
9. Local labor compliance beyond WPS / Nitaqat (e.g., specific MHRSD inspections) is out of scope.
10. Customs duty interactions on imports / exports are out of scope; ZATCA merged with Saudi Customs in 2021 but the Customs Schedule is administered separately.

## Worked cases

**Case 1: a mixed entity bottom line.** Saudi share 60%, Zakat base SAR 2,000,000, taxable income SAR 500,000, 365-day fiscal year against a 354-day Hijri year. Assume these are independently checked, unapportioned ordinary-company bases, with no short-period, merger or specialised rule, and that the stated day counts are established inputs. The combined arithmetic is SAR 70,932.20; no portal form or final liability is certified by this example.

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

**Case 2: file on time or exactly 30 days late?** Assume an ordinary company, no relief/waiver, revenue SAR 3,000,000, income tax SAR 100,000 wholly unpaid until filing/payment exactly 30 days after the deadline. The filing alternatives are min(1% × revenue, SAR 20,000) = SAR 20,000 and 5% × unpaid tax = SAR 5,000. Higher alternative: SAR 20,000. One 30-day late-payment period adds SAR 1,000, total SAR 21,000. Timely filing **and payment** incurs neither in these facts. This decision compares only these penalties, not fees or other defaults. [Income Tax Guideline sections 7.2 to 7.3](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf), and regulations arts. 67 to 68. No remainder-period assumption or exemption-initiative eligibility is used.

```oa-check
name: File and pay on time versus exactly 30 days late
inputs:
  revenue: 3000000
  unpaid: 100000
steps:
  - option_a: min(revenue * 0.01, 20000)
  - option_b: unpaid * 0.05
  - filing_penalty: max(option_a, option_b)
  - delay_penalty: unpaid * 0.01
  - timely_penalties: 0
  - late_total: filing_penalty + delay_penalty
  - saving: late_total - timely_penalties
expected:
  option_a: 20000
  option_b: 5000
  filing_penalty: 20000
  delay_penalty: 1000
  timely_penalties: 0
  late_total: 21000
  saving: 21000
```

## When to refuse or refer


- **R-SA-ASM-1**: Upstream skill did not run. Name the missing skill. Continue with available data; flag the gap; do not fabricate the missing computation.
- **R-SA-ASM-2**: Upstream self-check failed. Note the specific check; continue but flag.
- **R-SA-ASM-3**: Cross-skill reconciliation > SAR 10,000. Raise as "Needs Input"; do not silently round.
- **R-SA-ASM-4**: Specialist scope referral: petroleum, natural gas, banking, insurance, listed-company allocation/reporting, investment funds, REITs, special economic/logistics zones, RHQ, NEOM, Red Sea Global and Qiddiya. HOLD all specialised rates and arrangements; no rate is supplied by this workflow.
- **R-SA-ASM-5**: Out of scope: PE-only filings for non-resident contractors operating without local CR; pure-play offshore service permanent establishments under treaty-protected positions; transfer pricing assessments for MNEs above CbCR threshold (handled via sa-corporate-tax with specialist support); APA negotiations with ZATCA. Refer to a specialist.
- **R-SA-ASM-6**: Intake incomplete. Name the missing intake field (CR, TIN, VAT number, ownership split, fiscal year-end, audited FS, GOSI ID, Mudad subscription). Cannot finalise the return until provided.
- **R-SA-ASM-7**: Asked to submit to ZATCA. This skill produces a working paper. Submission is the taxpayer's (or their authorised representative's) action, after credentialed reviewer sign-off. Decline politely; provide the filing instructions instead.
- **R-SA-ASM-8**: An unverified rate, threshold, rule or upstream calculation remains a HOLD. Request current official source and facts; an upstream Guide is not legal verification, and this revision does not attest to the ten named-contributor Guides.
- **R-SA-ASM-9**: Asked to opine on Sharia compliance of Zakat base treatment. Decline: Sharia interpretation is the role of the entity's Sharia board or qualified scholar; the capstone applies ZATCA's Implementing Regulations as published, not independent Sharia analysis.

## Filing and payment

### Section 6: Payment instructions: ZATCA portal, SADAD billing

Use the payment procedure supported for the particular tax head and actual invoice. Do not assume every tax head or bank shares the same menu.

#### 6.1 The ZATCA → SADAD flow

- **Supported income-tax payment sequence**: Following submission of the checked approved return, pay the issued invoice through SADAD, as in [Income Tax Guideline section 6, PDF p. 7](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf). Copy the invoice reference exactly, verify taxpayer/period/amount and keep the receipt. **HOLD** the old 14-digit bill format, universal bank/ATM/teller availability, particular login route and automatic portal-status timing. For other tax heads obtain their actual invoice/workflow evidence before final instructions.

#### 6.2 Common tax heads / SADAD bill mapping

**Common tax heads / SADAD bill mapping table**

| Tax head | ZATCA portal section | Periodicity | Used for |
| --- | --- | --- | --- |
| Zakat | Annual Zakat declaration | Annual (120 days from FYE) | Saudi/GCC entities |
| Corporate Income Tax | Approved annual income-tax form; number on HOLD | General 120 days from FYE, exceptions checked | Covered income-tax scope |
| Mixed Zakat + CIT | Annual combined | Annual (120 days from FYE) | Mixed-ownership entities |
| VAT | Monthly or quarterly | Last day of following month | All VAT-registered |
| Withholding Tax | Monthly | 10th of following month | All WHT agents |
| Excise Tax | Two-monthly | Last day of month after period | Excise-able goods |
| RETT | Property transaction workstream | HOLD rate, form and deadline |

#### 6.3 Payment timing relative to filing

**Payment timing relative to filing table**

| Payment | Due date | Filing reference |
| --- | --- | --- |
| Annual Zakat / CIT balance | General 120-day period; 31 December 2026 gives 30 April 2027 before any applicable holiday/exception adjustment | Confirm actual return and payment deadline |
| Monthly VAT (turnover > SAR 40M) | Last day of following month | VAT return |
| Quarterly VAT (turnover ≤ SAR 40M) | Last day of month after quarter | VAT return |
| Monthly WHT | 10th of following month | WHT return |
| Two-monthly Excise | Last day of month after period | Excise return |
| RETT | Property transaction workstream | HOLD rate, form and deadline |

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
| Intentional evasion by fraud or false information, income tax and WHT | 25% of the tax difference | ZATCA Income Tax Guideline, https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf |
| Fines exemption initiative | Runs 1 July to 31 December 2026; excludes returns due after 30 June 2026, VAT Law art. 45 fines and evasion fines; not automatic: registration where required, outstanding/corrected returns and full principal payment or a compliant approved instalment plan by the initiative deadline; already-paid fines are excluded | ZATCA Simplified Guide, https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf |

### Section 7: Filing instructions: annual return within 120 days of FYE via ZATCA

#### 7.1 Filing channel

- **Income-tax filing channel**: ZATCA publishes the electronic portal route in [Income Tax Guideline section 6](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf). **HOLD** the old blanket no-paper assertion and any conclusion about every other tax head without its procedure.

#### 7.2 Submission steps

- **Submission steps**: For a resolved income-tax working paper, access the taxpayer's account at https://zatca.gov.sa, choose **Returns**, complete the approved form, check data and terms, submit, and pay the issued invoice through SADAD. These are the steps ZATCA actually publishes in [Income Tax Guideline section 6, PDF p. 7](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf). This Guide produces instructions only. Record the actual form/period, attachments and field labels shown in the taxpayer's portal; **HOLD** historical Form 800/Form 8 identifiers, exact box/menu labels, universal attachment requirements and Nafath/login assumptions until verified. Preserve acknowledgement, invoice and payment receipt; reconcile without assuming a status-update time. For Zakat and other taxes confirm their own portal workflow rather than treating the income-tax sequence as proof of every menu.

#### 7.3 Deadlines (illustrative: adjust to actual FYE)

**Deadlines table**

| Fiscal year-end | 120-day deadline | Notes |
| --- | --- | --- |
| 31 December 2025 | **30 April 2026** | Stated in the ZATCA 2026 calendar |
| 31 December 2026 | **30 April 2027 before adjustment** | Arithmetic only; check the actual official holiday/tax-specific extension before a final date |
| 31 March 2026 | **29 July 2026 before adjustment** | Arithmetic only; check actual holiday/exception rules |
| 30 June 2026 | **28 October 2026 before adjustment** | Arithmetic only; no Hijri eligibility conclusion |
| 30 September 2026 | **28 January 2027 before adjustment** | Arithmetic only; check actual holiday/exception rules |
| Custom year-end approved by ZATCA | FYE + 120 days | Per approval |

- **Hijri-period deadline**: Capture the actual year-end and calculate the elapsed days. **HOLD** calendar-conversion/eligibility assumptions until the registered period and applicable procedure are checked; do not use ownership nationality to reject a Hijri period.

#### 7.4 Extension of time

**Extension of time table**

| Item | Mechanism |
| --- | --- |
| Extension / payment relief | NON-OPERATIVE HOLD: no automatic extension, customary duration or penalty suspension is assumed; obtain current tax-specific procedure and written approval |



#### 7.5 Audit & assessment

For Zakat, art. 106 permits assessment/correction within 5 years in the ordinary stated cases, 10 years for late/incomplete/unpaid/missing returns, and without a time limit in its para. 3 cases (evasion, approved taxpayer request/consent, or unregistered payer); para. 4 separately covers arithmetic/clerical errors for 10 years. [Zakat Regulations arts. 105 to 107, PDF pp. 59 to 61](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf). **HOLD:** income-tax periods and the following legacy audit-trigger suggestions; they are information to collect, not verified selection rules:

- Significant book-to-tax adjustments
- Loss carry-forward usage
- Related-party transactions (transfer pricing: Saudi adopts OECD-aligned TP rules; Local File / Master File / CbCR thresholds apply)
- Refund claims
- Industry-specific risk profiling

## Completion checklist


All upstream skills required for the chosen return type have produced output, or the gap is flagged.

Ownership split traces to evidence; indirect/GCC corporate/listed treatment remains held unless independently verified.

Zakat base reconciles to source accounts with statutory additions/deductions and minimum/maximum controls; unsupported adjustments remain held.

CIT taxable income reconciles from accounting profit through documented tax adjustments with ITL section references.

Interest calculation remains a HOLD until the current applicable loan-return rule and amendments are verified; no EBITDA proxy enters the workbook.

All months with withholding payments reconcile to the required statement, invoice and receipt; no nil monthly filing requirement is assumed. Annual statement timing includes the partnership exception.

VAT reconciliation: annual revenue ties to sum of monthly/quarterly VAT returns ± documented reconciling items.

Covered payroll periods reconcile to WPS evidence; legal completeness remains held unless separately verified.

Actual Nitaqat result is recorded; any legal status or consequence remains held until employer-specific verification.

Audit/attachment requirements are established for the actual entity or explicitly held; no SAR 40M audit default is used.

RETT disclosures are present for any real estate disposals during the year.

Excise reconciliation is present if entity deals in excise-able goods.

Fatoorah notice and implementation evidence are recorded; exact technical compliance remains held until verified against applicable specifications.

The general 120-day interval, applicable tax-specific exceptions and actual holiday-adjusted deadline are separately recorded; an arithmetic illustration is not labelled a final deadline.

SADAD billing register lists every payable item with billing ID, amount, and payment status.

Record retention period (10 years for Zakat documents, art. 110) is stated in the action list.

Reviewer brief contains legislation citations (Royal Decree numbers, ITL articles, Zakat IR articles, VAT IR articles, RETT framework) for every position taken.

A professional authorised for the actual Saudi engagement reviews and signs; membership alone is not treated as authority.

For mixed entities, confirm bases are not already apportioned and apply the art. 15 period percentage, rather than a flat 2.5% for every calendar.

WHT rates applied per the ZATCA WHT Guideline (20% management fees / 15% royalties / 15% other / 5% dividends, rent, loan charges, technical services).

## Legal instruments named in this skill

The Sources table identifies the texts actually read. **NON-OPERATIVE HISTORICAL TOPICS:** the earlier instrument list also named Income Tax Law M/1 (1425H), its Resolution 1535 regulations, Zakat Royal Decree M/40, VAT Law M/113 and Royal Order A/638, Excise Law M/86, conflicting RETT A/84/M/84 instruments, Social Insurance Laws M/33/M/22, Companies Law M/132, Nitaqat/WPS decisions, GCC VAT Agreement, bilateral treaties and a common "Tax Procedures Law". No unverified title, date, article attribution or universal procedural rule in that list is authority in this revision. Their relevant rules remain held where used. Obtain the operative current text before relying on any held topic; old instrument labels are retained here solely so the prior scope is not lost.

## Change log

- **v1.0 (May 2026):** Initial release. Modelled on pk-return-assembly and us-ca-return-assembly, adapted for Saudi annual returns, ZATCA portal filing, SADAD billing payment flow, the Zakat / CIT / mixed-entity split, WPS + Saudization compliance integration, and Royal Decree-based statutory references. Coordinates nine upstream Saudi skills.

- **v1.1 (November 2026):** Moved to tax year 2026 and the method shape. Corrected the Zakat percentage and minimum base, withholding rates, VAT and excise due dates, penalties, record retention and e-invoicing wave.

- **v1.2 (1 November 2026):** Replaced operative assumptions with explicit local holds; corrected WHT nil-month and partnership exceptions, calendar scaling and the late-penalty example; recorded exact source scope and preserved earlier topics in the evidence ledger. Platform attribution and standard closing block preserved.

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Zakat Collection Regulations 1445H, Decision 1007 as amended by 1248; read in the original source: PDF pp. 2 to 9, 15 to 23, 58 to 63 (definitions, residence, period/rate, minimum/maximum and procedure/retention); no full-document claim | https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf | 2026-11-01 |
| ZATCA Income Tax Guideline, May 2026; read in the original source: all 11 PDF pages, including rate diagram on p. 5 and obligations diagram on p. 6; Arabic prevails | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf | 2026-11-01 |
| Income-tax Implementing Regulations, Arabic compilation; read in the original source: cover/amendment list and arts. 9(2), 67 to 68, PDF pp. 1 to 2, 10 to 11, 55 to 57; compilation states amendments through Decision 2568 of 1440H, so no claim to complete 2026 amendment coverage | https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf | 2026-11-01 |
| ZATCA WHT Guideline, May 2026; read in the original source: definitions and sections 1 to 5, PDF pp. 5 to 33: source/PE/category, exclusions, rates, nil months, annual partnership exception, retention and penalties | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf | 2026-11-01 |
| ZATCA 2026 calendar; read in the original source: complete two-page PDF, annual deadline and all monthly VAT/WHT/excise entries; 2027 illustrative dates are calculated, not published in this calendar | https://zatca.gov.sa/en/MediaCenter/Publications/Documents/Zakat%20Declaration%20and%20Tax%20Returns%20Calendar%20(EN).pdf | 2026-11-01 |
| ZATCA VAT penalties; read in the original source: complete offence/fine table and neighbouring repeat-offence note | https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/Penalties.aspx | 2026-11-01 |
| ZATCA September/Q3 2026 VAT notice; read in the original source: complete article and supplies split, not just title | https://zatca.gov.sa/en/MediaCenter/News/Pages/Submit-VAT-Return-for-Oct-andQ3-2026.aspx | 2026-11-01 |
| ZATCA Wave 25; read in the original source: complete article: qualifying years, strict threshold, notification, integration date and Phase 1 context | https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx | 2026-11-01 |
| ZATCA sweetened-drink amendment announcement, Arabic; read in the original source: complete article: 2026 effective date, sugar method and 100 ml unit; not a tier-rate schedule | https://zatca.gov.sa/en/MediaCenter/News/Pages/excise-tax-regulation-2026.aspx | 2026-11-01 |
| ZATCA cancellation initiative; read in the original source: PDF pp. 1 to 9 including conditions and exclusions; no automatic eligibility conclusion | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf | 2026-11-01 |
| MISA Investment Law; read in the original source: bilingual PDF pp. 1 to 4, including arts. 1, 7 to 8 and 14 to 16 and securities exception | https://misa.gov.sa/app/uploads/2024/08/Investment-Law.pdf | 2026-11-01 |
| MISA updated law page; read in the original source: law text and Q&A 2.2 to 2.5, including existing-investor answer, not merely the registration headline | https://misa.gov.sa/activities/laws-regulations-copy/ | 2026-11-01 |
| MISA Implementing Regulations; read in the original source: arts. 1 to 2 and 9 to 13, PDF pp. 1 to 2 and 5 to 7, applicant information and annual-update context | https://misa.gov.sa/app/uploads/2025/06/THE-INVESTMENT-LAW-IMPLEMENTING-REGULATIONS.pdf | 2026-11-01 |

| Bureau of Experts Income Tax Law, **archived 15 February 2026** after direct TLS and ordinary-browser failure; read in original Arabic arts. 1 to 13 and amendment notes, 21 to 23, 60 to 61, 68 to 71, 76 to 77; later amendments not established | https://web.archive.org/web/20260215020442/https://laws.boe.gov.sa/boelaws/laws/lawdetails/23576008-1ce4-4685-ac3e-a9a700f2cb02/1 | 2026-11-01 |

Not yet confirmed: live Income Tax Law and amendments after the 15 February 2026 archive capture (direct BOE TLS fetch and ordinary browser failed); complete later amendments to the Arabic income-tax regulation compilation; VAT registration thresholds, rate and all transaction-specific zero/exempt conditions; Hijri eligibility or changes for income tax; interest limitation and loss-relief computation; specialised oil/gas rates; indirect/GCC corporate and listed-company allocation; actual mixed-return form and box identifiers; audit thresholds and attachment law; tax-specific portal/login/bill identifiers or status-update timing beyond the published income-tax steps; general extensions/refund periods; non-Zakat/non-WHT retention; GOSI rates, caps, new-entrant rules and payment dates; Nitaqat current bands/headcount thresholds/benefits/consequences; WPS mandate/deadline; RETT rate, exemptions, first-home limit, instrument and filing/payment date; excise product rates/tier amounts and registration test; Phase 1 invoice-type technical/QR/clearance/reporting rules and earlier waves; Investment Law commencement/transition and exceptions outside the read clauses; professional credential recognition and filing authority; transfer-pricing/Master File/Local File/CbCR thresholds; common Tax Procedures Law assertion. These are NON-OPERATIVE HOLDS: do not compute, classify, refuse, backdate, declare overdue, promise a date or finalise the affected line from a held rule. Named-contributor Guides remain outside this review and do not resolve a hold by themselves.

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
