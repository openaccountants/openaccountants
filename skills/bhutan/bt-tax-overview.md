---
name: bt-tax-overview
description: "Route a Bhutan 2026 tax question by income year, taxpayer, income source, GST, payroll and company obligations, preserving the historical filing boundary."
jurisdiction: BT
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: "2.1"
type: situation-rules
---

# Bhutan Tax Overview (2026) | v2.1

Use the 2026 Acts for 2026 income and transactions, and keep the 2025-2026 filing cycle separate. Choose the taxpayer, source and tax job before loading the detailed computation or filing skill. [ss.2-5](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.2-5,ScheduleI](https://www.drc.gov.bt/wp-content/uploads/2025/12/Consolidated-GST-Act-of-Bhutan-2020-and-amendment-thereof.pdf); [paragraphs 1-2](https://www.drc.gov.bt/wp-content/uploads/2025/12/Tax-Filing-Notification_IY-2025_final.pdf)

## Who this applies to

This is the ordinary Bhutan tax-system entry point, not a complete return or a special-zone opinion. DRC administers tax under the Ministry of Finance. Individual residence and business source matter: resident business income is worldwide, while the other income heads and non-resident business income follow the Bhutan-source boundary in ss.19-20. [ss.16-20](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [both image pages](https://www.drc.gov.bt/transition-to-the-bhutan-integrated-taxation-system-income-tax-module/)

## Rates, bands and thresholds

| Item | Rule for 2026 | Official source |
|---|---|---|
| Income year | Normally 1 January to 31 December, or another 12-month period approved by DRC. Do not silently substitute a company’s accounting period without checking approval. | [s.706(40)](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) |
| Currency | Bhutanese Ngultrum, Nu./BTN. RMA states that it is pegged at par to INR;1:1 is derived from “at par”, not a guarantee of bank fees or every transaction’s conversion result. | [monetary-policy peg paragraph](https://www.rma.org.bt/mpolicy/) |
| Reform boundary | Income Tax Act 2025 and GST commencement:1 January 2026, with non-retroactivity and prior-income-tax rights/liabilities/proceedings preserved under the new Act. | [ss.2-5](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.2-5,ScheduleI](https://www.drc.gov.bt/wp-content/uploads/2025/12/Consolidated-GST-Act-of-Bhutan-2020-and-amendment-thereof.pdf) |

## The base

For employment, rent, investment and other individual receipts, load [personal income tax](bt-income-tax.md): residence, current tax-free band and top progressive band, employment/education/home relief, exemptions and final withholding. The former high-income surcharge and old seven-band year label must not be reused as current law. [ss.16-20](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [PartIII 14 A](https://www.drc.gov.bt/wp-content/uploads/2024/11/Income-Tax-Act-of-the-Kingdom-of-Bhutan-2001_Fourth-Edition.pdf)

For an incorporated company or unincorporated business, load [corporate and business income tax](bt-corporate-income-tax.md): entity rates, ordinary versus presumptive individual business, withholding, losses, prepayment and annual return. The previous skill’s universal flat company/BIT treatment does not identify the 2026 taxpayer-specific result. [Schedule 1 paragraphs 2-6](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 2](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [PartI 45;PartII 12](https://www.drc.gov.bt/wp-content/uploads/2024/11/Income-Tax-Act-of-the-Kingdom-of-Bhutan-2001_Fourth-Edition.pdf)

For a supply, import, exemption, registration or input-credit question, load [GST](bt-vat-gst.md). Historical Sales Tax is not the current GST computation. Classify the specific 2026 amended goods schedule and distinguish exemption from zero-rating before giving a rate or credit result. The separate Excise Tax Act 2025 repeals the former GST excise-equalization provisions; it does not make every import excise-free. [ss.2-5,ScheduleI](https://www.drc.gov.bt/wp-content/uploads/2025/12/Consolidated-GST-Act-of-Bhutan-2020-and-amendment-thereof.pdf); [notification and replacementScheduleIV-C](https://www.drc.gov.bt/wp-content/uploads/2026/06/GST_Public_Notification_2026.pdf); [whole addendum](https://www.drc.gov.bt/wp-content/uploads/2026/06/Addendum_GST_Public_Notification-2026.pdf); [ss.1-7](https://www.drc.gov.bt/wp-content/uploads/2025/10/Excise-Tax-Act-of-Bhutan-2025-2.pdf)

For employees, load [payroll/social contributions](bt-payroll-social.md) and distinguish tax from pension/PF. For a new or converting entity, load [company formation](bt-company-formation.md) for Corporate Regulatory Authority, licences, foreign-investment gates, audit and registry filings. Tax registration and corporate registration are separate completion items. [r.153;AnnexureI,42401-42500 row](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf); [clauses 1.1-1.2](https://www.nppf.org.bt/downloads/?attachment_id=442); [ss.21-37](https://www.cra.gov.bt/wp-content/uploads/2026/04/The-Companies-Act-of-Bhutan-2016.pdf); [ss.296-300](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

Historical corrections are preserved in the specialist skills. The old Act distinguished state and non-state companies and used a different PIT surcharge condition; the DRC 2025 filing notice distinguished PIT from business/company deadlines. Do not use the 2026 personal bands or reform description to recalculate an earlier year without the applicable historical Act and rules. [PartI 45;PartII 12](https://www.drc.gov.bt/wp-content/uploads/2024/11/Income-Tax-Act-of-the-Kingdom-of-Bhutan-2001_Fourth-Edition.pdf); [PartIII 14 A](https://www.drc.gov.bt/wp-content/uploads/2024/11/Income-Tax-Act-of-the-Kingdom-of-Bhutan-2001_Fourth-Edition.pdf); [paragraphs 1-2](https://www.drc.gov.bt/wp-content/uploads/2025/12/Tax-Filing-Notification_IY-2025_final.pdf); [ss.2-5](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

## Deadlines and filing

Use the specialist calendar for each liability: annual income return and assessment payment, business prepayment, monthly withholding statement/deposit, approved GST period, PF remittance and company annual return. A date for one job is not a universal Bhutan deadline. Inactive businesses still have the s.291 declaration requirement. [ss.263,290-295](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.285-289](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.273-279](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.38-55,337(105)](https://www.drc.gov.bt/wp-content/uploads/2025/12/Consolidated-GST-Act-of-Bhutan-2020-and-amendment-thereof.pdf); [ss.251-255,267-268](https://www.cra.gov.bt/wp-content/uploads/2026/04/The-Companies-Act-of-Bhutan-2016.pdf)

The November notice announces BITS income-module implementation from 1 January 2027; RAMIS remains the current income-tax route through the announced transition or further notice. GST already has its own BITS route. Keep tax type, period, old/new TPN and acknowledgement together. Future portal screens and a GST number do not prove a completed income-tax registration. [both image pages](https://www.drc.gov.bt/transition-to-the-bhutan-integrated-taxation-system-income-tax-module/); [whole notification](https://www.drc.gov.bt/wp-content/uploads/2026/07/Notification-on-Prepayment-of-Tax-for-the-IY-2026.pdf); [registration and filing/payment sections](https://www.drc.gov.bt/easy-guide-for-businesses-and-consumers/)

## Penalties and interest

Identify which tax or registry obligation failed and the year before quoting a penalty. Current income-tax late filing/payment, GST late payment and NPPF late-deposit penalties have separate bases and conditions in their specialist skills. A historical notice’s penalty is not automatically the 2026 penalty for another tax. [ss.442-450,664-666](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.261-264;ScheduleVII-A](https://www.drc.gov.bt/wp-content/uploads/2025/12/Consolidated-GST-Act-of-Bhutan-2020-and-amendment-thereof.pdf); [contribution table and remittance paragraphs](https://www.nppf.org.bt/remittance-of-contribution/)

## Cross-border points

Determine residence, business source, PE/SEP, payment character, foreign ownership and the relevant indirect-tax import route. Apply foreign-loss restrictions and withholding finality separately. Refer a special-zone, treaty or sector-specific result until the actual regime and operative source are established; ordinary Bhutan company formation or a rupee peg does not establish those benefits. [ss.16-20](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.226-232](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.58-61,204-207,239-240](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.266-284;Schedule 1 paragraph 7](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [rr.1-16,58-85,108,138(22);SchedulesI-III](https://www.moice.gov.bt/wp-content/uploads/2025/08/FDI-Rules-Regulations-2025.docx.pdf); [monetary-policy peg paragraph](https://www.rma.org.bt/mpolicy/)

## Two worked examples that recompute

Year selection changes a company result. Holding taxable profit constant at Nu.2,000,000 and assuming ordinary full liability with no relief or credits, the historical non-state company rate gives Nu.500,000, historical state-enterprise rate Nu.600,000, and 2026 company rate Nu.440,000. These derived comparisons expose why “all companies previously 30%” was wrong; they are not permission to use the 2026 base for a 2025 return. [PartI 45;PartII 12](https://www.drc.gov.bt/wp-content/uploads/2024/11/Income-Tax-Act-of-the-Kingdom-of-Bhutan-2001_Fourth-Edition.pdf); [Schedule 1 paragraphs 2-6](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.2-5](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

```oa-check
name: Company year and entity classification
inputs:
  comparable_taxable_profit: 2000000
steps:
  historical_nonstate: comparable_taxable_profit * 0.25
  historical_state: comparable_taxable_profit * 0.30
  current_company: comparable_taxable_profit * 0.22
  nonstate_difference: historical_nonstate - current_company
expected:
  historical_nonstate: 500000
  historical_state: 600000
  current_company: 440000
  nonstate_difference: 60000
```

A company has Nu.2,000,000 Bhutan business profit and Nu.3,000,000 foreign business profit. In the resident-company branch, both enter the business base and tax is Nu.1,100,000. In a comparable non-resident ordinary-assessment branch with only the stated Bhutan profit within charge, tax is Nu.440,000; the derived difference is Nu.660,000. No final-withholding, exemption, foreign credit, SEP election or treaty adjustment is assumed. Establish residence/source first; do not choose a branch solely for a lower result. [ss.16-20](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.226-232](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 1 paragraphs 2-6](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

```oa-check
name: Residence changes business source base
inputs:
  bhutan_profit: 2000000
  foreign_profit: 3000000
steps:
  resident_base: bhutan_profit + foreign_profit
  resident_tax: resident_base * 0.22
  nonresident_tax: bhutan_profit * 0.22
  difference: resident_tax - nonresident_tax
expected:
  resident_base: 5000000
  resident_tax: 1100000
  nonresident_tax: 440000
  difference: 660000
```

## Ask the client first

- Income year, transaction date and approved accounting period?
- Entity class, residence, source and any PE/SEP or special-zone facts?
- Employment, business, investment, supplies/imports and foreign ownership?
- DRC/GST/Corporate Regulatory Authority/PF registrations and actual scheme membership?
- Accounts, receipts, withholding, payments, prior assessments and notices?
- Is the requested job a computation, registration, return or historical correction?

## Sources

| Source | Read for | Read date |
|---|---|---|
| [Income Tax Act of Bhutan 2025](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) | Read for ss.1-64,204-207,226-240,262-300,324-326,442-450,664-674,706(40); Schedules 1-3 and 6. | 2026-11-15 |
| [Rules on the Income Tax Act 2025](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf) | Read for rr.47-58,151-164; Annexures I-II and IV, relevant individual and company computation fields. | 2026-11-15 |
| [Historical Income Tax Act 2001, Fourth Edition](https://www.drc.gov.bt/wp-content/uploads/2024/11/Income-Tax-Act-of-the-Kingdom-of-Bhutan-2001_Fourth-Edition.pdf) | Read for Part I s.45; Part II s.12; Part III ss.4-5,7,12,14 A-15,17; historical provisions only. | 2026-11-15 |
| [DRC income-year 2025 filing notice,29 December 2025](https://www.drc.gov.bt/wp-content/uploads/2025/12/Tax-Filing-Notification_IY-2025_final.pdf) | Read for both pages: filing windows, inactive entities, RAMIS/BETA, completion status and payment voucher. | 2026-11-15 |
| [DRC prepayment notice,29 July 2026](https://www.drc.gov.bt/wp-content/uploads/2026/07/Notification-on-Prepayment-of-Tax-for-the-IY-2026.pdf) | Read for whole scanned page: 2026 prepayment, RAMIS registration and non-resident branches. | 2026-11-15 |
| [DRC income-module transition notice,10 November 2026](https://www.drc.gov.bt/transition-to-the-bhutan-integrated-taxation-system-income-tax-module/) | Read for both image pages: January transition, TPN notices and December application timing. | 2026-11-15 |
| [GST Act 2020,September 2025 consolidation](https://www.drc.gov.bt/wp-content/uploads/2025/12/Consolidated-GST-Act-of-Bhutan-2020-and-amendment-thereof.pdf) | Read for ss.1-62,209-212,261-264,337(105); Schedules I-II and VII-A; consolidation limitation. | 2026-11-15 |
| [DRC GST amendment notification,25 June 2026](https://www.drc.gov.bt/wp-content/uploads/2026/06/GST_Public_Notification_2026.pdf) | Read for all 6 pages including complete replacement Schedule IV-C and BTC descriptions. | 2026-11-15 |
| [DRC addendum,26 June 2026](https://www.drc.gov.bt/wp-content/uploads/2026/06/Addendum_GST_Public_Notification-2026.pdf) | Read for whole page: legal commencement versus collection date and credit adjustment. | 2026-11-15 |
| [Excise Tax Act 2025](https://www.drc.gov.bt/wp-content/uploads/2025/10/Excise-Tax-Act-of-Bhutan-2025-2.pdf) | Read for ss.1-7 only: commencement,savings and repeal of GST excise provisions. | 2026-11-15 |
| [Companies Act of Bhutan 2016,current Corporate Regulatory Authority copy](https://www.cra.gov.bt/wp-content/uploads/2026/04/The-Companies-Act-of-Bhutan-2016.pdf) | Read for ss.2-14,21-27,30-37,249-255,267-269; formation,liability,audit and annual return. | 2026-11-15 |
| [FDI Rules and Regulations 2025](https://www.moice.gov.bt/wp-content/uploads/2025/08/FDI-Rules-Regulations-2025.docx.pdf) | Read for rr.1-16,58-85,108,138(22) and Schedules I-III; classification,project-cost base,funding and approval gates. | 2026-11-15 |
| [NPPF remittance of contribution](https://www.nppf.org.bt/remittance-of-contribution/) | Read for complete contribution table,remittance instructions and late-deposit penalty paragraph. | 2026-11-15 |
| [NPPF current Private PF agreement](https://www.nppf.org.bt/downloads/?attachment_id=442) | Read for all 4 pages,especially clauses 1.1-1.2: member numbers,rate,base,deposit and recovery schedule. | 2026-11-15 |
| [RMA monetary policy](https://www.rma.org.bt/mpolicy/) | Read for all 3 operative paragraphs,including the at-par INR peg. | 2026-11-15 |
| [DRC GST Easy Guide](https://www.drc.gov.bt/easy-guide-for-businesses-and-consumers/) | Read for registration applications and Filing GST Returns/How to File/How to Pay sections; statutory precision checked against Act and Rules. | 2026-11-15 |

Not yet confirmed: unread treaty/special-zone/regulated-sector outcomes, the old draft’s unsupported 2025 personal-band label and deduction conditions, and final live 2027 income-module return/payment screens. Follow the relevant specialist skill’s unresolved boundary rather than filling it by analogy.
