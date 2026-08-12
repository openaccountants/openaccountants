---
name: pk-sales-tax-services
description: "Source-cited tax guide for PK: pk sales tax services. Unverified draft, pending local-accountant review."
jurisdiction: PK
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ibrar Ali
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PK Sales Tax Services

## Pakistan — Provincial Sales Tax on Services — Skill v1.0

ALWAYS READ THIS SKILL IN FULL before touching any Pakistan provincial sales tax on services work. Sales tax on services in Pakistan is NOT a single federal regime — it is administered by five separate revenue authorities under five separate statutes, each with its own portal, rate, return form, due date, and penalty regime. Federal FBR sales tax (Sales Tax Act 1990) covers GOODS only; services are provincial. Confusing the two is the single most common error.

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by Ibrar Ali on 2026-06-12. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.

### pk-sales-tax-services

- **Sindh (SRB)** — 0.15  _(Sindh Sales Tax on Services Act 2011)_
- **Punjab (PRA)** — 16%  _(Punjab Sales Tax on Services Act 2012)_
- **Khyber Pakhtunkhwa (KPRA)** — 15%  _(KP Finance Act 2013, Ch. VI)_
- **Balochistan (BRA)** — 15%  _(Balochistan Sales Tax on Services Act 2015)_
- **Islamabad ICT (FBR)** — 0.15  _(ICT (Tax on Services) Ordinance 2001)_
- **Return due (all authorities)** — 15th of the following month for payment; 18th for filing. (Note: PRA exception).  _(Provincial Acts)_
- **Registration** — Mandatory on commencement of taxable supplies (no general turnover threshold)  _(Provincial Acts)_
- **Late filing penalty (e.g. SRB)** — PKR 5,000 if filed within 15 days of the due date; PKR 10,000 if delayed beyond 15 days.  _(SRB Act §43 (and provincial equivalents))_
- **Default surcharge** — KIBOR + 3% per annum  _(SRB Act §44 (and equivalents))_
- **Records retention** — 5 years  _(Provincial Acts)_
- **Exported IT/ITeS services** — Exempt/zero-rated upon realization of foreign currency via banking channel (PRC).  _(Provincial Second Schedules)_
- **Educational & healthcare services** — Generally exempt (healthcare except cosmetic)  _(Provincial Schedules)_
- **Cross-province supply** — Major conflict: SRB (Sindh) favors the Origin principle, while PRA (Punjab) strictly applies the Destination principle.  _(Place-of-supply rules)_
- **Inbound digital services** — Reverse charge / 100% withholding applies across major authorities (SRB, PRA, ICT) for unregistered foreign suppliers.  _(Provincial Acts)_

## 1. Quick Reference Table

**Quick Reference Table**  _(Quick Reference Table)_

| Authority | Jurisdiction | Statute | Standard Rate | Portal | Return Due |
| --- | --- | --- | --- | --- | --- |
| **SRB** (Sindh Revenue Board) | Sindh | Sindh Sales Tax on Services Act 2011 | **15%** | e-SRB (e.srb.gos.pk) | 15th of following month (payment); 18th (return) |
| **PRA** (Punjab Revenue Authority) | Punjab | Punjab Sales Tax on Services Act 2012 | **16%** | e-PRA (e.pra.punjab.gov.pk) | 15th (payment); 18th (return) |
| **KPRA** (KP Revenue Authority) | Khyber Pakhtunkhwa | KP Finance Act 2013, Chapter VI | **15%** | e-KPRA (kpra.kp.gov.pk) | 15th (payment); 18th (return) |
| **BRA** (Balochistan Revenue Authority) | Balochistan | Balochistan Sales Tax on Services Act 2015 | **15%** | e-BRA (bra.gob.pk) | 15th (payment); 18th (return) |
| **ICT-IRS** (FBR) | Islamabad Capital Territory | Islamabad Capital Territory (Tax on Services) Ordinance 2001 | **15%** | FBR IRIS (iris.fbr.gov.pk) | 15th (payment); 18th (return) |

Special reduced rates exist within each regime (e.g. 5%, 8% for IT services in some PRAs subject to conditions). Always check the relevant Second Schedule of the governing Act for the year of supply.

## 2. Required Inputs + Refusal Catalogue

### 2.1 Required Inputs Before Computing Any Pakistan Services Tax

- **Place of business / permanent establishment (PE)** — which province(s) does the service provider have a PE in?  _(n/a)_
- **Place of supply / place of consumption** — where is the recipient located? Where is the service performed?  _(n/a)_
- **Nature of service** — software development, IT-enabled services (ITeS), consulting, marketing, etc. (each authority's Second Schedule has its own classification codes).  _(n/a)_
- **PSEB registration status** — Pakistan Software Export Board registration unlocks export exemption for IT/ITeS services.  _(n/a)_
- **Annual turnover** — registration is generally mandatory regardless of turnover for taxable service providers, but small-supplier thresholds may apply in some PRAs.  _(n/a)_
- **Existing registrations** — NTN (National Tax Number), STRN (Sales Tax Registration Number), and any provincial registration numbers.  _(n/a)_
- **Client jurisdiction breakdown** — invoice-by-invoice province of recipient.  _(n/a)_
- **Foreign-currency receipts via banking channel** — required for export exemption.  _(n/a)_

### 2.2 Refusal Catalogue

- **Refund claims** — under any provincial Act (complex documentary evidence; authority-specific procedures). DO NOT proceed — escalate to a Pakistan-licensed tax practitioner.  _(2.2 Refusal Catalogue)_
- **Cross-province apportionment disputes** — where two or more PRAs have issued show-cause notices for the same supply. DO NOT proceed — escalate to a Pakistan-licensed tax practitioner.  _(2.2 Refusal Catalogue)_
- **Withholding agent obligations** — under any PRA's Withholding Rules where the client is a government department or large taxpayer. DO NOT proceed — escalate to a Pakistan-licensed tax practitioner.  _(2.2 Refusal Catalogue)_
- **Reverse-charge / self-billing** — scenarios on imported services where the recipient is in Pakistan. DO NOT proceed — escalate to a Pakistan-licensed tax practitioner.  _(2.2 Refusal Catalogue)_
- **Anti-money-laundering / suspicious transaction reporting** — triggered by sales tax inquiries. DO NOT proceed — escalate to a Pakistan-licensed tax practitioner.  _(2.2 Refusal Catalogue)_
- **Audit defence and tribunal appeals** — before the Appellate Tribunals of each PRA. DO NOT proceed — escalate to a Pakistan-licensed tax practitioner.  _(2.2 Refusal Catalogue)_
- **Sales tax on goods** — (federal FBR) — that is the Sales Tax Act 1990 regime, not in scope here.  _(2.2 Refusal Catalogue)_
- **Federal Excise Duty on services** — (rare residual cases under FED Act 2005) — out of scope.  _(2.2 Refusal Catalogue)_
- **Capital value tax, infrastructure development cess, professional tax** — different regimes.  _(2.2 Refusal Catalogue)_

## 3. Tier 1 — Per-Province Detail

### 3.1 SRB — Sindh

- **Standard rate** — 15% (general); reduced rates apply per Second Schedule.  _(Sindh Sales Tax on Services Act 2011)_
- **IT / IT-enabled services** — Generally taxable at standard rate UNLESS exported. Some categories enjoy reduced rates (e.g. call centres historically at 3% — verify current Schedule).  _(Sindh Sales Tax on Services Act 2011)_
- **Registration threshold** — No general turnover threshold for taxable service providers — registration is mandatory upon commencement of taxable supplies.  _(Sindh Sales Tax on Services Act 2011)_
- **Filing frequency** — Monthly.  _(Sindh Sales Tax on Services Act 2011)_
- **Return form** — SST-03 via e-SRB portal.  _(Sindh Sales Tax on Services Act 2011)_
- **Payment** — PSID generation on e-SRB → pay through any designated bank or ADC channel.  _(Sindh Sales Tax on Services Act 2011)_
- **Late filing penalty** — PKR 5,000 if filed within 15 days of the due date; PKR 10,000 if delayed beyond 15 days under §43; default surcharge under §44 (KIBOR + 3% per annum).  _(SRB Act §43, §44)_
- **Notable services subject to SST** — software/IT services, telecommunication, advertising, courier, banking, insurance, franchise, consulting, contractual execution of work.  _(Sindh Sales Tax on Services Act 2011)_

### 3.2 PRA — Punjab

- **Standard rate** — 16% (general); reduced rates per Second Schedule (e.g. certain IT services historically 5% subject to conditions — verify current Schedule).  _(Punjab Sales Tax on Services Act 2012)_
- **IT / IT-enabled services** — Reduced rate available where conditions are met (no input tax adjustment, services rendered to local clients in specified categories).  _(Punjab Sales Tax on Services Act 2012)_
- **Registration threshold** — Mandatory for taxable service providers; no general turnover threshold.  _(Punjab Sales Tax on Services Act 2012)_
- **Filing frequency** — Monthly.  _(Punjab Sales Tax on Services Act 2012)_
- **Return form** — PST return via e-PRA portal.  _(Punjab Sales Tax on Services Act 2012)_
- **Payment** — PSID via e-PRA → bank or 1Bill / ADC.  _(Punjab Sales Tax on Services Act 2012)_
- **Late filing penalty** — PKR 10,000 minimum under §48; default surcharge under §49 (KIBOR + 3%).  _(§48, §49)_
- **Notable services** — advertising, IT services, construction, franchise, courier, freight forwarding, professional consultancy.  _(Punjab Sales Tax on Services Act 2012)_

### 3.3 KPRA — Khyber Pakhtunkhwa

- **Statute** — KP Finance Act 2013, Chapter VI; Khyber Pakhtunkhwa Sales Tax on Services Regulation 2022 (operative regulations).  _(KP Finance Act 2013)_
- **Standard rate** — 15%.  _(KP Finance Act 2013, Ch. VI)_
- **IT / IT-enabled services** — Some reduced rates per Schedule; verify current notification.  _(KP Finance Act 2013)_
- **Registration** — Mandatory upon commencement of taxable supply.  _(KP Finance Act 2013)_
- **Filing frequency** — Monthly.  _(KP Finance Act 2013)_
- **Return form** — Filed via e-KPRA portal.  _(KP Finance Act 2013)_
- **Late filing penalty** — Per KPRA penalty schedule — PKR 5,000 to 10,000 minimum plus daily amount; default surcharge at prescribed rate.  _(KP Finance Act 2013)_
- **Notable services** — restaurants, hotels, telecommunication, advertising, construction services, professional services.  _(KP Finance Act 2013)_

### 3.4 BRA — Balochistan

- **Standard rate** — 15%.  _(Balochistan Sales Tax on Services Act 2015)_
- **Registration** — Mandatory for taxable service providers in Balochistan.  _(Balochistan Sales Tax on Services Act 2015)_
- **Filing frequency** — Monthly.  _(Balochistan Sales Tax on Services Act 2015)_
- **Return form** — BST-03 via e-BRA portal.  _(Balochistan Sales Tax on Services Act 2015)_
- **Late filing penalty** — Per Chapter VIII of the Act — minimum PKR 10,000 + default surcharge.  _(Chapter VIII, Balochistan Sales Tax on Services Act 2015)_
- **Notable services** — telecommunication, advertising, banking, construction, professional services, hotels, restaurants, IT services.  _(Balochistan Sales Tax on Services Act 2015)_

### 3.5 ICT-IRS — Islamabad Capital Territory

- **Statute** — Islamabad Capital Territory (Tax on Services) Ordinance 2001 — administered by FBR (NOT a separate provincial authority; sits within Inland Revenue Service of FBR).  _(ICT (Tax on Services) Ordinance 2001)_
- **Standard rate** — 15% (aligned with the Sales Tax Act 1990 rate by reference).  _(ICT (Tax on Services) Ordinance 2001)_
- **Registration** — Via FBR IRIS — same STRN as federal sales tax registration; service provider declares ICT services on the monthly federal sales tax return.  _(ICT (Tax on Services) Ordinance 2001)_
- **Filing frequency** — Monthly.  _(ICT (Tax on Services) Ordinance 2001)_
- **Return form** — Federal Sales Tax Return on IRIS — services section.  _(ICT (Tax on Services) Ordinance 2001)_
- **Late filing penalty** — Per Sales Tax Act 1990 §33 (applied by reference).  _(Sales Tax Act 1990 §33)_
- **Notable services** — services rendered, provided, initiated, received, or consumed within ICT — same Second Schedule classifications as adopted from FBR notifications.  _(ICT (Tax on Services) Ordinance 2001)_

## 4. Tier 2 — Cross-Province, Digital Services, Exemptions

### 4.1 Cross-Province Services — Which PRA Has Jurisdiction?

Each PRA's Act contains its own "place of supply" rules. Common principles:

- **Service rendered in Province X to a recipient in Province X** — that province's PRA has unambiguous jurisdiction.  _(n/a)_
- **Service rendered in Province X to a recipient in Province Y** — BOTH provinces may claim jurisdiction. In practice: SRB (Sindh) favors the Origin principle, while PRA (Punjab) strictly applies the Destination principle — a major source of conflict. Inter-provincial agreements / MOUs between SRB, PRA, KPRA, BRA, and FBR aim to reduce double taxation but disputes persist.  _(n/a)_
- **Service rendered remotely (online) by a Province X provider to a Province Y recipient** — generally treated as supplied at the place of business of the recipient if B2B, or at provider's PE if B2C. Verify against the specific PRA's place-of-supply rule.  _(n/a)_
- **Conservative default** — If the supplier has a PE only in Province X and bills a Province Y client for remotely-delivered services, register and remit in Province X. Maintain documentation evidencing place of rendering. If any PRA issues a notice, do not concede — request the matter be referred to the inter-provincial committee.  _(n/a)_

### 4.2 Digital / Cross-Border Services

- **Exports of services (IT/ITeS) with foreign-currency receipts via banking channel (PRC)** — Exempt or zero-rated under most PRAs (SRB, PRA, KPRA) for IT and IT-enabled services, subject to specific Schedule conditions (e.g. no input adjustment, formal export declaration, encashment certificate from bank).  _(n/a)_
- **Inbound digital services from foreign suppliers to Pakistani recipients** — Reverse charge / 100% withholding applies across major authorities (SRB, PRA, ICT) for unregistered foreign suppliers — the Pakistani recipient is required to withhold and pay PST. Verify before advising.  _(n/a)_
- **Marketplace facilitator rules** — Limited and evolving; not yet uniform across PRAs.  _(n/a)_

### 4.3 Common Exemptions

- **Exported IT/ITeS services** — (foreign-currency receipt via banking channel (PRC); encashment certificate) — exempt/zero-rated under SRB, PRA, KPRA.  _(n/a)_
- **Services rendered to diplomatic missions and certain international organizations** — exempt under each Act's Schedule.  _(n/a)_
- **Educational services (recognized institutions)** — exempt under most Schedules.  _(n/a)_
- **Healthcare services** — generally exempt except cosmetic/aesthetic.  _(n/a)_
- **Government-to-government services** — exempt by notification.  _(n/a)_

Exemption is NOT automatic — service provider must maintain documentary evidence (invoices marked "exempt," PSEB certificate, banking encashment certificate, recipient's exemption certificate).

## 5. Worked Example

Ali is a freelance software developer.
PE: Karachi (Sindh) — sole proprietorship, home office.
Clients:
- Client A: Karachi-based fintech (Sindh) — PKR 800,000/month for development services.
- Client B: Lahore-based marketing agency (Punjab) — PKR 400,000/month for development services.
- Client C: US-based SaaS company — USD 5,000/month received via banking channel into Ali's bank account in Karachi; Ali holds PSEB registration.
Ali is NOT registered with any PRA yet.

Federal: Ali must hold NTN (FBR) for income tax. Services are NOT federally taxable as sales tax (federal sales tax = goods only).

SRB (Sindh): Client A: service rendered from Sindh PE to Sindh recipient → unambiguous SRB jurisdiction. Taxable at 15% standard rate UNLESS the specific software development category qualifies for a reduced rate under the current Sindh Second Schedule (verify). Client C: service rendered from Sindh PE to foreign recipient with PSEB registration and foreign-currency receipt via banking channel → exempt/zero-rated. Encashment certificate required. Registration: Ali must register with SRB on commencement of taxable supplies (Client A).

PRA (Punjab): Client B: service rendered from Sindh PE to Punjab recipient → JURISDICTIONAL OVERLAP. SRB position (origin): taxable in Sindh. PRA position (destination): potentially taxable in Punjab. Conservative default: Register only in SRB; charge SRB rate on Client B invoices; document place of rendering (Sindh). Be prepared to defend if PRA issues a notice. If risk of PRA notice is high (Client B is a withholding agent under Punjab rules), seek pre-clearance under the inter-provincial MOU or consider voluntary PRA registration as a precaution — but this is a judgment call requiring practitioner sign-off.

Filing: Monthly SRB return (SST-03 via e-SRB) showing: Taxable supplies to Client A: PKR 800,000 × 15% = PKR 120,000 output tax. Taxable supplies to Client B: PKR 400,000 × 15% = PKR 60,000 output tax (treated as Sindh-originated). Exempt exports to Client C: USD 5,000 declared as exempt; PSEB certificate and banking encashment certificate held on file. Payment by 15th, return by 18th of following month.

Self-check: PSEB certificate valid and current? ✓ Foreign-currency receipt via banking channel for Client C (not cash, not crypto)? ✓ Place-of-rendering documentation for Client B (timesheets, IP logs showing work performed in Sindh)? ✓ Invoice template includes SRB registration number, taxable value, tax amount separately? ✓

## 6. Filing & Payment Per Authority

**Filing & Payment Per Authority**  _(Filing & Payment Per Authority)_

| Authority | Portal | Return Form | Payment Due | Return Due | Payment Mechanism |
| --- | --- | --- | --- | --- | --- |
| SRB | e.srb.gos.pk | SST-03 | 15th | 18th | PSID → designated bank / ADC |
| PRA | e.pra.punjab.gov.pk | PST return | 15th | 18th | PSID → bank / 1Bill / ADC |
| KPRA | kpra.kp.gov.pk | KP sales tax return | 15th | 18th | PSID → bank / ADC |
| BRA | bra.gob.pk | BST-03 | 15th | 18th | PSID → bank / ADC |
| ICT-IRS | iris.fbr.gov.pk | Federal Sales Tax Return (services section) | 15th | 18th | PSID via IRIS → bank / ADC |

Documentation to retain (minimum 5 years): Invoices (with registration number, taxable value, tax amount). Receipt vouchers / banking encashment certificates. PSEB certificate (for exports). Working papers reconciling return to books. Withholding tax certificates received (where applicable).

## 7. Conservative Defaults

When facts are ambiguous, default conservatively:

- **Default to registration** — if any taxable supply is made in a province, register. The cost of late registration penalties exceeds the cost of early registration.  _(n/a)_
- **Default to standard rate** — do not apply a reduced-rate or exempt classification without explicit Schedule evidence and confirmation of all conditions.  _(n/a)_
- **Default to origin-province in cross-province disputes** — register and remit in the PE province; document place of rendering meticulously.  _(n/a)_
- **Default to TAXABLE on exports without PSEB** — only treat as exempt if PSEB registration is current AND foreign-currency receipt via banking channel is documented.  _(n/a)_
- **Default to monthly filing** — there is no quarterly/annual option in any PRA's standard regime.  _(n/a)_
- **Default to separate invoice line for tax** — never embed tax in the gross amount; show taxable value and tax amount distinctly.  _(n/a)_
- **Default to in-province bank account** — for receipts where possible — strengthens place-of-rendering position.  _(n/a)_
- **Default to escalating to a Pakistan-licensed practitioner** — for any matter touching: refunds, cross-province disputes, withholding obligations, inbound reverse charge, audits, appeals.  _(n/a)_

## 8. Sources

Sindh Sales Tax on Services Act 2011 (with subsequent amendments through Sindh Finance Acts).
Punjab Sales Tax on Services Act 2012 (with subsequent amendments through Punjab Finance Acts).
Khyber Pakhtunkhwa Finance Act 2013 Chapter VI; KP Sales Tax on Services Regulation 2022.
Balochistan Sales Tax on Services Act 2015 (with subsequent Balochistan Finance Acts).
Islamabad Capital Territory (Tax on Services) Ordinance 2001.
Sales Tax Act 1990 (federal — goods only; referenced for ICT cross-application and penalty provisions).
SRB portal: e.srb.gos.pk
PRA portal: e.pra.punjab.gov.pk
KPRA portal: kpra.kp.gov.pk
BRA portal: bra.gob.pk
FBR IRIS: iris.fbr.gov.pk
Pakistan Software Export Board (PSEB): pseb.org.pk

Citation discipline: Each provincial Act has been amended multiple times by successive Finance Acts. Always cite the section number AND the year of the Finance Act version in force on the date of the relevant supply. Rates and Schedules in this skill reflect the position as of tax year 2025-26 and must be re-verified against the current Schedule before any filing.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
