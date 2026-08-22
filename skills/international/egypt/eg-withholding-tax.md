---
name: eg-withholding-tax
description: Use this skill whenever asked about Egyptian withholding tax (WHT) on outbound payments to non-residents — dividends, interest, royalties, technical/management/consulting fees, and rental income. Trigger on phrases like "Egypt WHT", "Egypt withholding tax", "ضريبة الخصم تحت الحساب", "dividends to non-resident Egypt", "royalty WHT Egypt", "technical services fee Egypt", or any cross-border payment from an Egyptian payer. ALWAYS read this skill before touching any Egypt WHT work.
version: 0.1
jurisdiction: EG
tax_year: 2025
last_updated: 2026-07-22
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt Withholding Tax (ضريبة الخصم تحت الحساب) Skill v0.1

## Egypt Withholding Tax (ضريبة الخصم تحت الحساب) Skill v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Jurisdiction is required.** Set `jurisdiction: EG` in frontmatter even when the folder path implies it. Sync to openaccountants.com skips files without a resolvable jurisdiction.

This skill covers Egyptian **withholding tax (WHT)** obligations for **resident payers** making payments to **non-residents** (and in some cases, residents) on:
- Dividends
- Interest
- Royalties
- Technical, management, and consulting services
- Rental income (movable/immovable property)
- Capital gains on disposal of Egyptian assets

The AI must reply in the user's language (English or Arabic / Egyptian Arabic) and may use the native tax terms shown throughout.

> **Currency note:** all figures are in Egyptian Pounds (EGP / ج.م) unless otherwise stated.
> **YMYL — verify before relying.** Egyptian WHT rates and treaty benefits changed in 2024-2025. Where this skill says "verify current value," re-confirm against the Egyptian Tax Authority (ETA — eta.gov.eg), PwC Worldwide Tax Summaries (taxsummaries.pwc.com/egypt), or a Big-4 alert before filing.

## What this file is

**This file is a content skill that loads on top of a workflow base** (here: `income-tax-workflow-base`). It provides Egypt-specific WHT rates, treaty reduction mechanics, compliance steps, and filing mechanics.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

## Section 1 — Scope statement

This skill covers:

- **Domestic WHT rates** (non-treaty) for each payment category under Law 91/2005 Arts 56, 56 bis
- **Double Tax Treaty (DTT) reduction** mechanics — how to claim treaty rates with a Tax Residency Certificate (TRC)
- **Key DTT partners** for Egypt (UAE, KSA, UK, USA, Netherlands, France, Germany, Italy, Cyprus, Mauritius, Singapore, etc.)
- **Compliance timeline** — deduction, remittance (Form 41), annual reconciliation
- **Penalties** for late deduction/remittance (Art 110-111)
- **Exemptions** — participation exemption (dividends ≥10%/1yr), government bonds, Suez Canal, etc.

This skill does NOT cover:

- VAT reverse charge on imported services — see `egypt-vat`
- Personal income tax withholding on salaries (PAYE) — see `eg-payroll`
- Social insurance contributions — see `eg-social-insurance`
- Transfer pricing adjustments that recharacterise payments — see `eg-transfer-pricing` (planned)
- Free zone / special economic zone WHT holidays — escalate to licensed advisor

## Section 2 — Filing requirements

**Filing requirements**  _(Law 91/2005 Arts 56, 56 bis, 57; ETA Decree 2023; ETA Circular 2022)_

| Item | Rule | Source |
| --- | --- | --- |
| **Who must withhold** | Any **resident person** (company, branch, PE, individual) paying listed income to a **non-resident** | Law 91/2005 Art 56 |
| **When to deduct** | At the **earlier of**: (a) payment date, (b) credit to account, (c) invoice date | Law 91/2005 Art 56 |
| **Remittance form** | **Form 41** (نموذج 41) — monthly WHT return | ETA Decree 2023 |
| **Remittance deadline** | **15th of the month following** the month of deduction | Law 91/2005 Art 56 |
| **Annual reconciliation** | Annual WHT statement filed with CIT return (30 Apr) | Law 91/2005 Art 57 |
| **Tax Residency Certificate (TRC)** | Required to claim treaty rate — must be **original, apostilled/legalised, valid for the tax year** | ETA Circular 2022 |
| **No TRC = domestic rate** | If TRC not provided at time of payment, apply domestic rate; refund claim possible within 3 years if TRC obtained later | Law 91/2005 Art 56 bis |

## Section 3 — Domestic WHT rates (non-treaty)

**Domestic WHT rates (non-treaty)**  _(Law 91/2005 Art 56(1)-(6))_

| Payment type | Rate | Legal basis | Notes |
| --- | --- | --- | --- |
| **Dividends** | **10%** | Law 91/2005 Art 56(1) | **Exempt** if recipient holds ≥10% for ≥1 year (participation exemption, Art 18 bis) |
| **Interest** | **20%** | Law 91/2005 Art 56(2) | Exempt: interest on Egyptian government bonds, Suez Canal Authority bonds, CBE bills |
| **Royalties** | **20%** | Law 91/2005 Art 56(3) | Includes patents, trademarks, designs, models, plans, secret formulas/processes, copyrights, software licences |
| **Technical / management / consulting fees** | **20%** | Law 91/2005 Art 56(4) | Broad definition — includes engineering, legal, accounting, marketing, administrative, financial advisory |
| **Rental — movable property** | **20%** | Law 91/2005 Art 56(5) | Equipment leasing, vehicle leasing |
| **Rental — immovable property** | **20%** | Law 91/2005 Art 56(5) | Real estate rent paid to non-resident |
| **Capital gains — disposal of Egyptian shares/real estate** | **20%** on gross proceeds (or 10% on net gain with documentation) | Law 91/2005 Art 56(6) | Applies to non-resident sellers of Egyptian assets |

## Section 4 — Treaty rates (key partners)

**Treaty rates (key partners)**  _(Egypt Double Tax Treaties; TRC per partner authority)_

| Treaty partner | Dividends | Interest | Royalties | Technical / consulting | TRC notes |
| --- | --- | --- | --- | --- | --- |
| **UAE** | **5%** (≥10% holding) / 10% | **10%** | **10%** | 10% | Most-used treaty; UAE TRC from MoF |
| **Saudi Arabia** | **5%** (≥10%) / 10% | **10%** | **10%** | 10% | KSA TRC from ZATCA |
| **United Kingdom** | **5%** (≥10%) / 15% | **10%** | **10%** | 10% | UK TRC from HMRC |
| **United States** | **5%** (≥10%) / 15% | **15%** | **15%** | 15% | US TRC from IRS (Form 6166) |
| **Netherlands** | **0%** (≥10%) / 10% | **10%** | **10%** | 10% | NL TRC from Belastingdienst |
| **France** | **5%** (≥10%) / 15% | **10%** | **10%** | 10% | FR TRC from DGFiP |
| **Germany** | **5%** (≥10%) / 15% | **10%** | **10%** | 10% | DE TRC from BZSt |
| **Italy** | **10%** | **10%** | **10%** | 10% | IT TRC from AdE |
| **Cyprus** | **5%** (≥10%) / 10% | **10%** | **10%** | 10% | CY TRC from Tax Dept |
| **Mauritius** | **5%** (≥10%) / 10% | **10%** | **12.5%** | 10% | MU TRC from MRA |
| **Singapore** | **5%** (≥10%) / 10% | **10%** | **10%** | 10% | SG TRC from IRAS |
| **China** | **5%** (≥25%) / 10% | **10%** | **10%** | 10% | CN TRC from STA |
| **No treaty / TRC not provided** | **10%** | **20%** | **20%** | **20%** | Domestic rates apply |

> **AUDIT FLASH POINT** — ETA audits WHT heavily. Common findings: (1) missing/invalid TRC, (2) misclassifying "technical services" vs "royalties", (3) late Form 41 filing, (4) interest on related-party loans recharacterised as dividends (thin cap + WHT interplay). Always verify TRC validity dates cover the payment period.

## Section 5 — Compliance mechanics

### Step 1 — Identify the payment

- Is the payer **resident in Egypt**? (incorporated in Egypt, managed/controlled in Egypt, or PE in Egypt)
- Is the recipient **non-resident**? (no PE in Egypt, not tax-resident)
- Is the payment **listed in Art 56**? (dividends, interest, royalties, technical/management/consulting fees, rental, capital gains on Egyptian assets)

### Step 2 — Determine the rate

1. Check if a **DTT exists** between Egypt and recipient's country of residence
2. Obtain **valid TRC** from recipient (original, apostilled/legalised, covers the tax year)
3. Apply **treaty rate** if TRC in hand at payment date; otherwise apply **domestic rate**
4. Check **exemptions**: participation exemption (dividends ≥10%/1yr), government bonds, Suez Canal, etc.

### Step 3 — Deduct and remit

- Deduct at **earliest of payment/credit/invoice**
- Calculate: `WHT = Gross amount × applicable rate`
- Remit via **Form 41** by **15th of following month**
- Pay via ETA e-payment portal (eta.gov.eg) or authorised banks

### Step 4 — Record keeping

- Keep: invoice, contract, TRC copy, Form 41 receipt, bank payment proof
- Retain **5 years** from end of tax year of payment

### Step 5 — Annual reconciliation

- Include WHT summary in corporate tax return (30 Apr)
- Report: recipient name, country, TRC ref, payment type, gross, rate, WHT deducted, net paid
- Any over/under deduction adjusted via amended return or refund claim (3-year statute)

## Section 6 — Edge cases and special rules

**Edge cases and special rules**  _(Art 49; Art 56; Art 56 bis; Law 91/2005 Art 40 ter; Art 18 ter, Law 5/2025; Law 83/2002, Law 173/2018; ETA Practice Note 2023; OECD Commentary)_

| Situation | Rule | Source |
| --- | --- | --- |
| **Related-party interest** | Subject to **thin cap (4:1 debt:equity)** — excess interest non-deductible AND WHT applies on gross | Art 49 + Art 56 |
| **Royalty vs technical services** | Royalties = IP licences; Technical = human-delivered services. **Misclassification risk** — ETA often reclassifies technical as royalty (20% vs 20% same rate but different treaty articles) | Art 56(3)-(4), OECD Commentary |
| **Software payments** | Shrink-wrap/standard licence → **royalty (20%)**; Custom development/SaaS → **technical services (20%)**; Treaty may distinguish | ETA Practice Note 2023 |
| **Branch remittance tax** | **No branch profits tax** in Egypt — branch profits taxed at 22.5% CIT, remittance to head office not subject to WHT | Law 91/2005 Art 40 ter |
| **Capital gains on listed shares (EGX)** | Non-resident: **exempt if held ≥1 yr**; otherwise 10% on gain (with documentation) or 20% on gross | Art 18 ter, Law 5/2025 |
| **Free zone companies** | Payments to free zone entities — WHT applies unless specific holiday granted | Law 83/2002, Law 173/2018 |
| **Refund of over-deducted WHT** | File refund claim within **3 years** of payment; requires TRC obtained post-payment | Art 56 bis |

## Section 7 — Self-checks

Before delivering output, verify:

- [ ] Payer is Egyptian tax resident (company, branch, PE, or individual)
- [ ] Recipient is non-resident (no Egyptian PE, not tax-resident)
- [ ] Payment type falls under Art 56 (div, int, royalty, tech/consulting, rental, cap gains)
- [ ] Correct domestic rate applied (10% div, 20% int/royalty/tech/rental)
- [ ] If treaty claimed: valid TRC on file covering payment date, correct treaty article cited
- [ ] Participation exemption checked for dividends (≥10% holding, ≥1 year)
- [ ] Form 41 filed by 15th of following month
- [ ] Annual WHT reconciliation included in CIT return (30 Apr)
- [ ] Related-party interest tested for thin cap + arm's length rate
- [ ] Records retained for 5 years (invoice, contract, TRC, Form 41, bank proof)

## Section 8 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, Egyptian licensed tax accountant — محاسب قانوني, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
