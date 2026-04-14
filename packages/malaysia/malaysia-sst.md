---
name: malaysia-sst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Malaysia Sales and Service Tax (SST) return (SST-02) for any client. Trigger on phrases like "Malaysia SST", "Sales Tax Malaysia", "Service Tax Malaysia", "SST-02", "MySST", "RMCD", or any request involving Malaysia SST. This is NOT a VAT — there is NO input tax credit. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Malaysia SST work.
version: 2.0
---

# Malaysia SST Return Skill (SST-02) v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Malaysia |
| Tax type | Sales and Service Tax (SST) — NOT a VAT. No input tax credit. |
| Sales Tax rate | 10% (standard); 5% (specific goods); specific rates (petroleum) |
| Service Tax rate | 8% (standard, from 1 March 2024); 6% (retained: F&B, telecoms, parking, logistics) |
| Exempt goods | Basic foodstuffs, live animals, certain agriculture, medical devices |
| Return form | SST-02 (bimonthly for both Sales Tax and Service Tax) |
| Filing portal | https://mysst.customs.gov.my (MySST) |
| E-invoice portal | https://myinvois.hasil.gov.my (IRBM, from August 2024) |
| Authority | Royal Malaysian Customs Department (RMCD / JKDM) |
| Currency | MYR (Malaysian Ringgit) |
| Filing frequency | Bimonthly (Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct, Nov-Dec) |
| Deadline | Last day of month following the bimonthly period |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending — requires licensed Malaysian tax agent |

**Key SST-02 fields:**

| Part | Field | Meaning |
|---|---|---|
| A1/A2 | Sales Tax 10% | Taxable goods at standard rate |
| A3/A4 | Sales Tax 5% | Taxable goods at reduced rate |
| A7 | Exempt goods | Including exports |
| A9 | Total Sales Tax | A2 + A4 + A6 |
| B1/B2 | Service Tax 8% | Standard rate services |
| B3/B4 | Service Tax 6% | Retained rate services (F&B, telecoms, parking, logistics) |
| B6 | Total Service Tax | B2 + B4 |
| C5 | Net SST payable | A9 + B6 - adjustments |

**CRITICAL: NO INPUT TAX CREDIT under SST.** SST paid on inputs is a cost. Manufacturers use Schedule A/B exemptions on raw materials (exemption at purchase, not credit after payment).

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown Sales Tax rate | 10% |
| Unknown Service Tax rate | 8% |
| Unknown whether manufacturer or trader | Trader (no Sales Tax obligation on output) |
| Unknown service classification | Not prescribed (no Service Tax) |
| Unknown SST paid on inputs | Cost (no credit) |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | RM 50,000 |
| HIGH tax-delta on a single default | RM 2,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the bimonthly period. Acceptable from: Maybank, CIMB, Public Bank, RHB, Hong Leong, AmBank, Bank Islam, Bank Rakyat, OCBC Malaysia, UOB Malaysia, or any other.

**Recommended** — sales invoices, Schedule A/B approval letters, SST registration certificates (separate for Sales Tax and Service Tax).

### Malaysia-specific refusal catalogue

**R-MY-1 — Free Zone / Licensed Manufacturing Warehouse.** Trigger: client in Free Zone or LMW. Message: "Free Zone and LMW operations have special SST treatment. Please escalate to a licensed tax agent."

**R-MY-2 — Petroleum and crude oil taxation.** Trigger: client in petroleum sector with specific-rate Sales Tax. Message: "Petroleum-specific Sales Tax rates require specialist analysis. Please escalate."

**R-MY-3 — Foreign digital service provider registration.** Trigger: foreign entity providing digital services to Malaysian consumers under Section 56C. Message: "Foreign DSP registration under Section 56C has specific obligations. Please escalate."

**R-MY-4 — GST transitional claims.** Trigger: client has unclaimed GST input credits from pre-September 2018. Message: "GST transitional provisions have largely expired. Please escalate for assessment of any remaining claims."

---

## Section 3 — Supplier pattern library

### 3.1 Malaysian banks (fees — cost, no credit)

| Pattern | Treatment | Notes |
|---|---|---|
| MAYBANK, MALAYAN BANKING | EXCLUDE for bank charges | No SST on exempt financial services |
| CIMB, CIMB BANK | EXCLUDE for bank charges | Same |
| PUBLIC BANK, PBB | EXCLUDE for bank charges | Same |
| RHB, HONG LEONG, AMBANK | EXCLUDE for bank charges | Same |
| BANK ISLAM, BANK RAKYAT | EXCLUDE for bank charges | Same |
| OCBC MY, UOB MY, STANDARD CHARTERED MY | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| RMCD, CUSTOMS, JKDM | EXCLUDE | Tax/duty payment |
| LHDN, IRBM, INLAND REVENUE | EXCLUDE | Income tax |
| SSM, COMPANIES COMMISSION | EXCLUDE | Registration fee |
| EPF, KWSP, SOCSO, PERKESO, EIS | EXCLUDE | Employee contributions |
| LEMBAGA HASIL | EXCLUDE | Tax authority |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| TENAGA NASIONAL, TNB | Cost (includes 6% Service Tax) | Electricity — SST embedded, no credit |
| SYABAS, AIR SELANGOR, SAJ | Cost | Water |
| TM, TELEKOM MALAYSIA, MAXIS, DIGI, CELCOM, U MOBILE | Cost (includes 6% Service Tax) | Telecoms — retained 6% rate |
| UNIFI, TIME INTERNET | Cost (includes 6% Service Tax) | Broadband |

### 3.4 Insurance

| Pattern | Treatment | Notes |
|---|---|---|
| GREAT EASTERN, AIA, PRUDENTIAL, ALLIANZ MY | Cost (Service Tax embedded) | Insurance services taxable at 8% |
| TAKAFUL, ETIQA | Cost | Same |

### 3.5 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, FACEBOOK | Self-account 8% via SST-02A | Imported service — Section 26 |
| AWS, AMAZON, ZOOM, SLACK | Self-account 8% via SST-02A | Same |
| CANVA, FIGMA, NOTION, OPENAI | Self-account 8% via SST-02A | Same |
| NETFLIX, SPOTIFY, DISNEY+ | Should be collected by provider (Section 56C) | Check if SST included |

### 3.6 E-commerce platforms

| Pattern | Treatment | Notes |
|---|---|---|
| SHOPEE, LAZADA, GRAB | Platform fees are cost | Service Tax embedded in platform commission |
| FOODPANDA, DELIVEREAT | Cost | Same |

### 3.7 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| AUDIT FIRM, ACCOUNTING, CONSULTANT | Cost (8% Service Tax embedded) | Group C prescribed service |
| LAW FIRM, LEGAL, PEGUAM | Cost (8% Service Tax embedded) | Same |
| ARCHITECT, ENGINEER, SURVEYOR | Cost (8% Service Tax embedded) | Same |

### 3.8 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, GAJI, WAGES | EXCLUDE | Outside SST scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Out of scope |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Manufacturer domestic sale at 10% Sales Tax

**Input line:** `05.04.2026 ; FURNITURE RETAILER SDN BHD ; CREDIT ; Invoice MY-041 ; RM 88,000`

**Reasoning:** Registered manufacturer sells taxable goods. Sales Tax at 10%. Net = RM 80,000, Sales Tax = RM 8,000. SST-02 Part A1/A2.

| Date | Counterparty | Gross | Net | Tax | Rate | SST-02 field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | FURNITURE RETAILER | +88,000 | +80,000 | 8,000 | 10% | A1/A2 | N | — |

### Example 2 — Professional service at 8% Service Tax

**Input line:** `10.04.2026 ; CONSULTANCY FEES ; CREDIT ; Advisory April ; RM 32,400`

**Reasoning:** Prescribed taxable service (Group C). Service Tax at 8%. Net = RM 30,000, Tax = RM 2,400. SST-02 Part B1/B2.

| Date | Counterparty | Gross | Net | Tax | Rate | SST-02 field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | CLIENT SDN BHD | +32,400 | +30,000 | 2,400 | 8% | B1/B2 | N | — |

### Example 3 — Restaurant at retained 6% Service Tax

**Input line:** `15.04.2026 ; FOOD SALES ; CREDIT ; F&B revenue ; RM 5,300`

**Reasoning:** F&B retains 6% rate. Net = RM 5,000, Tax = RM 300. SST-02 Part B3/B4.

| Date | Counterparty | Gross | Net | Tax | Rate | SST-02 field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | F&B REVENUE | +5,300 | +5,000 | 300 | 6% | B3/B4 | N | — |

### Example 4 — Imported cloud service (self-account)

**Input line:** `18.04.2026 ; AWS ; DEBIT ; Cloud hosting ; RM -2,350`

**Reasoning:** Imported service. Self-account 8% via SST-02A. Service Tax = RM 188. This is a COST — no credit.

| Date | Counterparty | Gross | Net | Tax | Rate | SST-02 field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | AWS | -2,350 | -2,350 | 188 | 8% | SST-02A | N | — |

### Example 5 — Export, exempt from Sales Tax

**Input line:** `22.04.2026 ; AUSTRALIAN BUYER PTY ; CREDIT ; Exported textiles ; RM 500,000`

**Reasoning:** Export of manufactured goods. Exempt from Sales Tax. SST-02 Part A7.

| Date | Counterparty | Gross | Net | Tax | Rate | SST-02 field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | AUSTRALIAN BUYER | +500,000 | +500,000 | 0 | Exempt | A7 | N | — |

### Example 6 — Bank charges, excluded

**Input line:** `30.04.2026 ; MAYBANK ; DEBIT ; Service charge ; RM -30`

| Date | Counterparty | Gross | Net | Tax | Rate | SST-02 field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | MAYBANK | -30 | — | — | — | — | N | "Exempt financial service" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Sales Tax — manufacturers only
Only registered manufacturers of taxable goods are liable. Retailers/wholesalers do NOT charge Sales Tax. 10% standard, 5% specific goods.

### 5.2 Service Tax — prescribed services only
Only services in First Schedule of Service Tax Regulations 2018. 8% standard (from 1 March 2024). 6% retained for F&B, telecoms, parking, logistics.

### 5.3 NO INPUT TAX CREDIT
SST is single-stage. No offset mechanism. Manufacturers use Schedule A/B/C exemptions on raw materials (applied at purchase, not as credit).

### 5.4 Imported services — self-account (Section 26)
All persons in Malaysia receiving prescribed taxable services from non-resident: self-account at 8% (or 6% retained rate) via SST-02A. Pay within 30 days. This is a COST.

### 5.5 Exports — exempt
Manufactured goods exported: exempt from Sales Tax. Report in SST-02 Part A7.

### 5.6 Registration thresholds
Sales Tax: RM 500,000 manufacturer turnover. Service Tax: RM 500,000 general; RM 1,500,000 F&B.

### 5.7 E-invoicing
Phase 1 (Aug 2024): > RM 100M. Phase 2 (Jan 2025): > RM 25M. Phase 3 (Jul 2025): all. IRBM MyInvois system.

### 5.8 Credit notes
Excess SST from returned goods/reduced consideration: deduct from next SST-02 Part C4. Within 6 years.

### 5.9 Bad debt relief
SST portion of debt outstanding > 6 months and written off: claim via Part C3. If recovered, repay.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Manufacturing vs service boundary
Pattern: subcontractor processing. Default: flag. Question: "Is the activity manufacturing (Sales Tax) or a service (Service Tax)?"

### 6.2 Mixed supply (goods + services)
Default: flag. Question: "Can goods and services be separately invoiced?"

### 6.3 SaaS billing entities
Default: self-account 8%. Question: "Check invoice entity — Malaysian or foreign?"

### 6.4 Schedule A/B exemption status
Default: no exemption. Question: "Do you have RMCD approval for Schedule A/B input exemption?"

### 6.5 Service scope expansion (July 2025)
Default: check if newly prescribed. Question: "Confirm service type against expanded First Schedule."

### 6.6 E-invoicing compliance
Default: required. Question: "What is annual turnover? Which phase applies?"

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Malaysia fields: Part A (Sales Tax 10%, 5%, specific, exempt), Part B (Service Tax 8%, 6%), Part C (totals, adjustments, net payable).

---

## Section 8 — Bank statement reading guide

Maybank, CIMB, Public Bank exports CSV/PDF with DD/MM/YYYY. MYR primary. Internal transfers between Maybank/CIMB/Public Bank: exclude. EPF/SOCSO/EIS deductions: exclude (payroll). Grab/Shopee settlements: separate platform fee from underlying revenue.

---

## Section 9 — Onboarding fallback

### 9.1 Registration type — "Are you registered for Sales Tax, Service Tax, or both?"
### 9.2 SST registration numbers — "Provide Sales Tax and/or Service Tax registration numbers."
### 9.3 Manufacturer status — "Are you a manufacturer of taxable goods?"
### 9.4 Prescribed services — "Which services do you provide from the First Schedule?"
### 9.5 Schedule A/B approval — "Do you hold RMCD exemption approvals?"
### 9.6 Filing period — Bimonthly. "Which period?"
### 9.7 E-invoicing phase — "What is your annual turnover?"

---

## Section 10 — Reference material

### Sources
1. Sales Tax Act 2018 (Act 806). 2. Service Tax Act 2018 (Act 807). 3. Sales Tax Regulations 2018. 4. Service Tax Regulations 2018 (and 2025 amendment). 5. RMCD MySST portal. 6. IRBM e-Invoice Guidelines v4.1.

### Known gaps
1. Free Zone/LMW refused. 2. Petroleum specific rates refused. 3. Supplier library covers major banks and utilities only. 4. Service scope expansion (July 2025) partially mapped.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure. Critical "no input credit" distinction emphasized throughout.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
