---
name: sd-vat-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Sudan VAT return, or to advise on Sudanese VAT registration, filing, and input tax recovery. Trigger on phrases like "Sudan VAT", "Sudan value added tax", "ضريبة القيمة المضافة السودان", "Sudan VAT return", "Sudan VAT registration", "sales tax Sudan", or any Sudan VAT request. ALWAYS read this skill before touching any Sudan VAT work.
version: 0.1
jurisdiction: SD
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sudan VAT (ضريبة القيمة المضافة) Skill

## Sudan VAT (ضريبة القيمة المضافة) Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Currency note:** All figures are in Sudanese Pounds (SDG — ج.س).
> **YMYL — verify before relying.** Sudan's VAT Act was originally enacted in 1999/2001 (post-regime VAT replacing earlier sales tax); the task body references a 2021 VAT Act but the actual law in force is the **Value Added Tax Act 2001** with **2017 Regulations** and ongoing ministerial amendments. The standard 17% rate is confirmed by Sudanese sources, but special rates apply to telecommunications and cigarettes. Verify current rates and registration threshold with the Sudan Taxation Chamber before filing.

## Section 1 — Scope statement

This skill covers:

- VAT scope, taxable supplies, and exempt categories
- Standard and special VAT rates (17% general; 40% telecom; 30% cigarettes)
- Registration threshold and registration procedure
- Monthly return filing mechanics
- Input VAT recovery
- Reverse charge on imported services
- Refund claims for exporters
- Tax invoicing and bookkeeping requirements

This skill does NOT cover:

- Personal income tax — see `sd-income-tax`
- Corporate / Business Profits Tax — see `sd-corporate-income-tax`
- Payroll and social insurance — see `sd-payroll-social`
- Company formation — see `sd-company-formation`

## Section 2 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Sudan (جمهورية السودان) |
| Tax | Value Added Tax (ضريبة القيمة المضافة — VAT) |
| Currency | SDG (Sudanese Pound — ج.س) |
| Standard rate | **17%** |
| Telecom sales rate | **40%** |
| Cigarettes rate | **30%** |
| Reduced rate | **5%** (selected sectors — verify current list) |
| Zero rate | Exports of goods; services provided outside Sudan |
| Exempt | Financial services, insurance, educational services, unprocessed agricultural products, poultry products, capital equipment for qualifying investment |
| Registration threshold | **SDG 1,200,000** annual turnover (mandatory for traders, industrial producers, service providers above threshold; importers/exporters regardless of turnover) |
| Tax authority | Sudan Taxation Chamber (Diwan Al-Daraib) |
| Return form | VAT Return (Form 3) |
| Filing frequency | Monthly |
| Deadline | Within **15 days** of the end of the tax accounting month |
| Importer obligation | Tax collected at customs clearance, regardless of importer turnover |
| Administering authority | Sudan Taxation Chamber (VAT department / local VAT office) |

### Key return sections (Form 3)

**Key return sections (Form 3)**

| Section | Meaning |
| --- | --- |
| Output VAT — 17% sales | Taxable sales at 17% (net) |
| Output VAT — 40% telecom | Telecom sales at 40% (net) |
| Output VAT — 30% cigarettes | Cigarettes sales at 30% (net) |
| Output VAT — 5% reduced | Reduced-rate sales (net) |
| Zero-rated exports | Net zero-rated sales |
| Exempt supplies | Net exempt sales |
| Total Output VAT | Sum of all output tax |
| Input VAT — local purchases | Recoverable input on local 17% purchases |
| Input VAT — imports (paid at customs) | Recoverable input for import VAT |
| Input VAT — reverse-charge foreign services | Self-assessed input on imported services |
| Total Input VAT | Sum of all input tax |
| Net VAT payable | Output minus input; positive = pay |
| Excess credit c/f | Excess input carried forward to next month |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | **17% standard** until confirmed |
| Unknown whether special rate (40% telecom, 30% cig) | Apply **17% standard** and flag for verification |
| Unknown whether export is documented | Treat as domestic 17% |
| Unknown business-use % | 0% input credit (no credit without documentation) |
| Unknown whether registered | Tax due at customs regardless of importer turnover |
| Foreign services to non-registered buyer | 17% reverse-charge |

## Section 3 — Rates and thresholds

**Rates and thresholds**  _(VAT Act 2001; Britacom; PwC; Trading Economics; Sudan Tribune; tax.gov.sd)_

| Item | Rate | Source |
| --- | --- | --- |
| **Standard VAT rate** | **17%** | VAT Act 2001; Britacom; PwC; Trading Economics; Sudan Tribune; tax.gov.sd |
| **Telecommunications services** | **40%** | VAT Act 2001 / Ministerial amendments; Britacom tax profile |
| **Cigarettes** | **30%** | VAT Act 2001 / Ministerial amendments; Britacom tax profile |
| **Reduced rate (some categories)** | **5%** | VAT Act 2001; sd-icalculator reference |
| **Zero rate (exports)** | **0%** | VAT Act 2001; Britacom — exporters enjoy zero VAT with input VAT refund entitlement |
| **Exempt** | **0%** (no input credit) | VAT Act 2001, Schedule — financial services, insurance, educational services, unprocessed agricultural products, poultry products |
| **VAT registration threshold** | **SDG 1,200,000** | VAT Act 2001; Britacom — for industrial producers, traders, service providers |
| **Importer registration** | Required regardless of turnover | VAT Regulations 2017 |

### Who must register

According to VAT Act 2001 and 2017 Regulations:

**Mandatory registration** for:
- **Industrial producers** with turnover at or above the registration threshold
- **Traders (importing or local)** with turnover at or above the threshold
- **Service providers** with turnover at or above the threshold
- **Importers and exporters** — **regardless of turnover** (every importer must register)

**Voluntary registration** is available for persons below the threshold.

### Registration procedure (Form 1, Form 2)

1. Submit registration application (Form 1) to the tax office within the jurisdiction of the taxpayer's main office
2. Office reviews application; if information is missing, registers provisionally and gives a period to complete
3. Completed applications are recorded in the register kept at the office
4. The Authority assigns a registration number to the taxpayer
5. Registration certificate (Form 2) is approved by the Secretary-General or their delegate and stamped with the Authority's seal
6. **Taxpayer must display the certificate in a visible place** at the main business location and a copy at each branch

### Registration cancellation

- **Registration cancellation** — Registered person may request cancellation in writing to the Secretary-General; cancellation effective from the last day of the tax period in which the decision was made (if approved); person must retain tax books, records, and invoice copies for **2 years** from cancellation date; every taxpayer ceasing activities or liquidating must notify the Authority within **30 days**  _(VAT Act 2001 and 2017 Regulations)_

### Changes to registration data

- **Changes to registration data** — Every registered taxpayer must notify the Authority in writing within **30 days** of any changes to: Name; Address; Main taxable activity; Other activities. If approved, a new certificate is issued with the same registration number reflecting the updates.  _(VAT Act 2001 and 2017 Regulations)_

### Filing and payment

**Filing and payment**  _(VAT Regulations 2017; tax.gov.sd; VAT Act 2001)_

| Item | Deadline | Source |
| --- | --- | --- |
| **Monthly return (Form 3)** | Within **15 days** of the end of the tax accounting month | VAT Regulations 2017; tax.gov.sd |
| **Payment** | At the same date as return submission | VAT Act 2001 |
| **Quarterly accounting** | Quarterly reconciliation per tax year | VAT Act 2001, Art 14 |
| **Extension** | The Secretary-General may extend the period for a similar duration if necessary | VAT Regulations 2017 |

### Filing and payment

A nil return is required even if no taxable sales, services, or works occurred during the accounting month.

### Books and records

- **Five mandatory registers** — 1. **Purchases register** — purchase invoices and customs documents for imports 2. **Sales register** — tax invoices for sales 3. **Returns register** — sales and purchase returns with adjustment notes 4. **Exports register** — export details, including customs certificates 5. **Stock register** — stock movements (FIFO method)  _(VAT Act 2001 and 2017 Regulations)_

### Step 1 — Compute output VAT

- **Output VAT** — Output VAT = (Standard-rate sales × 17%) + (Telecom sales × 40%) + (Cigarettes × 30%) + (Reduced-rate sales × 5%) + (Zero-rated exports × 0%) + (Exempt sales × 0%)  _(VAT Act 2001)_

### Step 2 — Compute input VAT (only recoverable if registered)

- **Input VAT** — Input VAT = (Standard-rate local purchases × 17%) -- recoverable + (Import VAT paid at customs × applicable rate) -- if registered, claimable + (Reverse-charge on imported services × 17%) -- self-assessed, same amount claimed as input **Import VAT is paid at customs** regardless of importer's registration status, but only registered taxpayers can claim it as input credit.  _(VAT Act 2001)_

### Step 3 — Net VAT payable

- **Net VAT payable** — Net VAT = Total Output VAT - Total Input VAT - Prior Excess Credit If positive: **pay** the Sudan Taxation Chamber If negative: **excess input—carry forward** to next month (or claim refund if eligible exporter)  _(VAT Act 2001)_

### Reverse-charge on imported services

- **Reverse-charge on imported services** — Every resident who contracts with a non-resident who does not have a legal entity registered in Sudan for taxable services **shall add the tax amount to the service value and deposit the same with the Chamber** (self-assess). **Step-by-step:** 1. Foreign supplier bills net amount (e.g., $10,000) 2. Resident computes VAT: net × 17/100 = VAT amount 3. Resident declares both output VAT AND input VAT for that amount — net zero for fully taxable businesses 4. Resident holds documentation (contract, foreign invoice, payment evidence)  _(VAT Regulations 2017; tax.gov.sd)_

### Tax invoice requirements

- **Tax invoice requirements** — A valid tax invoice must contain: 1. The words "Tax Invoice" or "Manifest" as a title 2. Date and tax identification number 3. Taxpayer's name, address, registration number, and TIN 4. Buyer's name, address, registration number, and TIN 5. Details of the good or service, **tax rate**, and total invoice value For sales to non-taxpayers: - Invoice showing total value (including tax) is acceptable - Issued in triplicate (original to buyer, copy kept by taxpayer) Computerized invoices are permitted provided they meet conditions in Article 9(1)(c) of the Regulations.  _(Article 20 of the VAT Act and 2017 Regulations)_

### Special-rate supplies

**Special-rate supplies**  _(Britacom tax profile; Investment Incentive Law 2021)_

| Supply | Rate | Notes |
| --- | --- | --- |
| Telecommunications services | 40% | Telecom companies' sales; Britacom tax profile |
| Cigarettes | 30% | Tobacco sales; Britacom tax profile |
| Selected goods (machinery, basic items) | 5% (reduced) | Verify current list against Ministerial schedule |
| Exports of goods / services | 0% (zero-rated) | Eligible for input VAT refund |
| Financial services | Exempt | No input credit |
| Insurance | Exempt | No input credit |
| Educational services | Exempt | No input credit |
| Unprocessed agricultural products | Exempt | No input credit |
| Poultry products | Exempt | No input credit |
| Capital equipment — investment projects | Exempt | Per Investment Incentive Law 2021; list approved by Ministry of Investment and International Cooperation |

### Voluntary registration

- **Voluntary registration** — - A person below the registration threshold may apply for voluntary registration using Form 1 - Once registered, subject to all VAT provisions; **cannot request cancellation before 2 years** from registration date  _(VAT Act 2001 and 2017 Regulations)_

### Sanctions for non-payment

- **Sanctions for non-payment** — Where tax due is not paid by the taxpayer within fixed dates, the Secretary-General may impose: - **Financial sanctions specified by regulations** for each month of delay - Sanctions collected along with the tax through the same procedure  _(VAT Act 2001 and 2017 Regulations)_

### Refunds for exporters

- **Refunds for exporters** — Exporters (zero-rated supplies) can claim **input VAT refund**. Refund claims require: - Customs certificates for exports - Valid input tax invoices - Filing of monthly returns **AUDIT FLASH POINT:** Refund processing for exporters historically requires extensive documentation and may be delayed. Many exporters operate cash-flow negative on VAT until refunds are processed. Conservative approach: assume refund will be claimed on next quarterly cycle, not received immediately.  _(VAT Act 2001; Britacom)_

### Imports

- **Imports** — Tax on imported goods is due at the **stage of customs clearance** upon the event that triggers the customs tax, and collected per customs procedure. **Applies to every importer regardless of turnover.** Customs cannot postpone the tax or subject it to installments. Final release of imported goods does not occur before full payment. For continuous services (e.g., subscriptions), the **issue of the invoice by the person rendering the service** is the event that gives rise to tax.  _(VAT Act 2001 and 2017 Regulations)_

### Example 1 — Standard domestic sale

**Scenario:** Khartoum-based electronics retailer sells a TV for SDG 117,000 (VAT-inclusive) to a consumer.

- VAT-inclusive price: SDG 117,000
- Net price (extract VAT): 117,000 / 1.17 = **SDG 100,000**
- Output VAT (17%): **SDG 17,000**
- Invoice must show VAT separately if buyer is registered; can show VAT-inclusive total for non-registered buyer

### Example 2 — Telecom sale (special rate)

**Scenario:** Mobile operator sells prepaid airtime worth SDG 100,000.

- VAT at 40% (telecom): 100,000 × 40% = **SDG 40,000**
- Output VAT line item on return: SDG 40,000
- (Note: this rate applies to telecommunications companies per the Britacom profile — verify directly with current Ministerial amendments)

### Example 3 — Export of goods (zero-rated)

**Scenario:** Sudanese exporter sells sesame worth SDG 5,000,000 to a Saudi buyer. Documents: contract, customs export declaration, bank transfer evidence.

- Zero rate (0%): 5,000,000 × 0% = **SDG 0** output VAT
- Input VAT on local purchases (e.g., SDG 170,000 paid): **fully refundable** under export zero-rate rules
- Return entry: zero-rated sales = 5,000,000; input credit claim = 170,000 (or carry-forward per refund process)

### Example 4 — Reverse charge on foreign SaaS subscription

**Scenario:** Sudanese company pays $2,000/month (≈SDG 100,000 at illustrative rate) for Microsoft 365.

- Foreign digital service — reverse charge applies
- VAT = 100,000 × 17% = **SDG 17,000**
- Declare as **output VAT** AND claim as **input VAT** — net zero for fully taxable business
- Documentation: foreign invoice, bank SWIFT, contract

### Example 5 — Import of goods (customs VAT)

**Scenario:** Importer brings in machinery CIF value SDG 10,000,000, customs duty SDG 2,000,000.

- VAT base = 10,000,000 + 2,000,000 = **SDG 12,000,000**
- Import VAT at 17% = **SDG 2,040,000** — paid at customs clearance
- If registered, claim as input VAT in same month's return

### Example 6 — Monthly return summary

**Example 6 — Monthly return summary (Trading company — April 2025)**

| Item | Net (SDG) | Output VAT (SDG) |
| --- | --- | --- |
| Domestic sales at 17% | 10,000,000 | 1,700,000 |
| Export sales (0%) | 5,000,000 | 0 |
| Telecom sales (40%) | 500,000 | 200,000 |
| Total Output | 15,500,000 | 1,900,000 |
|  |  |  |
| Local input purchases at 17% | 6,000,000 | 1,020,000 |
| Import VAT (customs) | 4,000,000 | 680,000 |
| Reverse-charge foreign services | 200,000 | 34,000 |
| Total Input | 10,200,000 | 1,734,000 |
| **Net VAT payable** |  | **166,000** |

## Section 8 — Self-checks

Before delivering output, verify:

- [ ] Rate correctly assigned (17% standard, 40% telecom, 30% cigarettes, 5% reduced, 0% exports, exempt categories)
- [ ] Tax invoice contains all required fields (TIN, addresses, tax rate, date, amounts)
- [ ] Registration threshold (SDG 1,200,000) cross-checked for client status
- [ ] Monthly return submitted within 15 days of month-end
- [ ] Importer VAT at customs regardless of registration status
- [ ] Reverse-charge on imported services declared both as output and input
- [ ] Exempt supplies not generating input credit
- [ ] Export zero-rated requires valid customs certificates for refund claim
- [ ] All 5 mandatory registers maintained
- [ ] Voluntary registration cannot be cancelled within 2 years

## Section 9 — Reference material

**Reference material**

| Resource | Reference |
| --- | --- |
| Sudan Taxation Chamber — VAT | https://tax.gov.sd/en/value-added-tax-vat |
| VAT Act 2001 (PDF) | https://tax.gov.sd/wp-content/uploads/2025/02/The-Value-Add-tax.pdf |
| VAT Regulations 2017 (PDF) | https://tax.gov.sd/wp-content/uploads/2025/02/vat_list.pdf |
| Britacom tax profile — Sudan | https://www.britacom.org/zt/BRPolicies/Sudan/ |
| PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/sudan |
| Sudan Tribune (livestock export VAT) | https://sudantribune.com/article/309388 |

## PROHIBITIONS

- Do NOT confuse the 17% standard rate with the 40% telecom or 30% cigarettes special rates — different rules apply per Ministerial schedule.
- Do NOT claim input credit on exempt supplies (financial services, insurance, education, unprocessed agricultural products) — no credit available.
- Do NOT assume an unregistered buyer should receive a VAT-inclusive-only invoice for sale to a registered buyer — registered buyers require VAT-separated invoices with TIN.
- Do NOT claim import VAT as input credit without confirming the importer is VAT-registered.
- Do NOT cancel voluntary registration within 2 years — automatic bar.
- Do NOT present output as final without flagging "verify current rate" for special rates.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in Sudan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

**Sources:** VAT Act 2001 (Sudan); VAT Regulations 2017; tax.gov.sd; Britacom; PwC; Trading Economics; Sudan Tribune.

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
