---
name: ua-bookkeeping
description: "Ukrainian sole-proprietor (ФОП) record-keeping and bookkeeping: the income ledger and income-and-expense ledger, software cash registers (ПРРО / PRRO), primary documents that support income and expenses, fiscalisation, and document retention. Records and process, not rate computation."
version: 1.0
jurisdiction: UA
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UA Bookkeeping

## Ukraine FOP Record-Keeping & Bookkeeping — Self-Employed Skill v1.0

This skill covers how a Ukrainian sole proprietor (ФОП / FOP — фізична особа-підприємець) keeps records: the income ledger and the income-and-expense ledger, software cash registers (ПРРО / PRRO), the primary documents that support income and expenses, and how long records must be kept. It is a **process** skill. For tax groups, rates, income limits, ЄСВ and the military levy, read **ua-single-tax**; for VAT records, read **ukraine-vat**.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Ukraine |
| Scope | FOP (фізична особа-підприємець) record-keeping & fiscalisation — single tax & general system |
| Currency | UAH (₴) |
| Primary legislation | Tax Code of Ukraine (Податковий кодекс — ПКУ): Art. 44 (record-keeping & retention), Art. 296 (single-tax records), Art. 177 (general-system records); Law №265/95-ВР "On the use of RRO"; MoF Order №261 of 13.05.2021 (typical ledger form & order) |
| Authority | Державна податкова служба (ДПС / State Tax Service) |
| Portal | Електронний кабінет платника (cabinet.tax.gov.ua) |
| Retention period | Generally **1095 days (3 years)** from the deadline/date of the related filing; longer in defined cases — see Section 6 |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Ukrainian accountant |
| Skill version | 1.0 |

**Wartime note:** Martial law suspends the running of statute-of-limitation periods for tax audits, which in practice **extends** how long documents should be kept (see Section 6). Treat all retention periods as *minimums*. Figures and form references are as of **May 2026**.

### Conservative defaults

- **Keep a ledger even if not registered** — Registration of ledgers was abolished from 01.01.2021, but the obligation to keep records was not. Default to maintaining one.
- **Keep records electronically and back them up** — Default to the Електронний кабінет ledger or a structured spreadsheet plus scanned primary documents.
- **Assume PRRO is required** — Assume PRRO is required for any cash or card-acquiring/payment-service sale unless a specific exemption clearly applies (Group 1; or genuinely IBAN-to-IBAN-only with no card/PSP).
- **Keep every primary document** — Keep every primary document, even where the single tax does not require expense proof — income must still be substantiated, and audits are open-ended where none has occurred.
- **Retain longer, not shorter** — When in doubt about the retention period, keep the document.
- **Flag, don't guess** — If the FOP group, payment channel, or activity type is unknown, ask; the answer changes the PRRO obligation entirely.

## Section 2 — Records by FOP group and system

The record-keeping obligation differs by **system** (single tax vs general system) and, for the single tax, by **VAT status**. Registration of any ledger with the ДПС is **no longer required** (abolished 01.01.2021) — but keeping records remains mandatory under Art. 44 ПКУ.

**Records by FOP type**

| FOP type | Ledger to keep | What is recorded | Form / format |
| --- | --- | --- | --- |
| **Group 1 single tax** (non-VAT) | Книга обліку доходів (income ledger) | Income only | Free form (paper or electronic); typical MoF form optional |
| **Group 2 single tax** (non-VAT) | Книга обліку доходів (income ledger) | Income only | Free form (paper or electronic) |
| **Group 3 single tax, non-VAT** | Книга обліку доходів (income ledger) | Income only | Free form (paper or electronic) |
| **Group 3 single tax, VAT-registered (3% path)** | Книга обліку доходів і витрат (income & expense ledger) | Income **and** expenses | Free form; VAT records additionally per ukraine-vat |
| **General system FOP** | Книга обліку доходів і витрат (income & expense ledger) | Income, expenses, supporting primary documents | Typical form per **MoF Order №261 (13.05.2021)**; paper or electronic |
| **Independent professional activity** (незалежна професійна діяльність — not a FOP, but same regime) | Книга обліку доходів і витрат | Income & expenses | Typical form per MoF Order №261 |

- **Single tax (non-VAT) → income only** — Single-tax payers who are not VAT-registered record only income. They are not required to keep an expense ledger, because the single tax is charged on turnover, not profit. They must still hold primary documents proving the origin of goods where applicable and substantiating income.
- **VAT-registered single-tax payers (Group 3, 3% path) → income and expenses** — They keep the income-and-expense ledger and the VAT records described in ukraine-vat.
- **General system → full income and expenses** — Net taxable income (ПДФО base) is income minus documented business expenses, so the income-and-expense ledger and complete primary documents are essential. Undocumented expenses are simply disallowed.
- **Ledger registration abolished** — Registration of the ledger in the typical form with the ДПС was abolished from 1 January 2021 for all FOPs. There is no "register the book" step in 2026. The MoF №261 form still exists and is mandatory in structure for general-system FOPs, but it is self-maintained, not filed.

## Section 3 — The income ledger (Книга обліку доходів)

- **Who keeps the income ledger** — Single-tax FOPs (Groups 1–3) who are not VAT-registered.
- **What to record** — Date of the entry / day of the transaction. Amount of income received that day (cash and non-cash), in UAH. For returns/refunds — the amount returned (reduces income). Total daily and period income.  _(Art. 296 ПКУ and the historic №261 structure)_
- **Format and electronic form (2026 position)** — The ledger may be kept in paper or electronic form, in any convenient format. There is no longer a mandatory standard form and no registration with the ДПС. Electronic options in practice: (a) the Книга обліку facility inside the Електронний кабінет (cabinet.tax.gov.ua); or (b) a self-built spreadsheet (Excel/Sheets). Whichever format is chosen, entries must be reconstructable on demand for an audit.
- **When entries are made** — Income is recorded on the day it is received (cash basis — date funds hit the till or bank account). FOPs recognise income when received, not when invoiced. Foreign-currency income is converted to UAH at the NBU rate on the date of receipt (when funds are credited to the FOP's account). Keep the bank credit advice as evidence of the rate/date.

**Verify per case:** the exact line structure depends on the FOP's group and whether they sell goods (origin-of-goods documents) versus pure services. The obligation to record income daily and to keep it electronically-or-on-paper is settled; the layout is at the FOP's discretion.

## Section 4 — ПРРО / cash registers (RRO / PRRO)

- **ПРРО definition** — A ПРРО (програмний реєстратор розрахункових операцій / software RRO) is a free, software-based fiscal cash register that issues fiscal receipts and transmits data to the ДПС in real time. It is the modern alternative to a hardware RRO and is what almost all FOPs use. The state offers a free PRRO app; common third-party PRROs include Checkbox, Vchasno.Kasa, and others.

### Who must use RRO/PRRO in 2026

**RRO/PRRO obligation by FOP type (2026)**

| FOP type | RRO/PRRO obligation (2026) |
| --- | --- |
| **Group 1 single tax** | **Exempt** — may operate without RRO/PRRO, provided activity stays within "retail trade at markets / household (personal) services to the population." Online sales, delivery, or expanding channels can forfeit the exemption. |
| **Group 2 single tax** | **Mandatory** for settlement operations — cash, payment-card (POS), and payment services (NovaPay, LiqPay, WayForPay, Fondy, etc.). |
| **Group 3 single tax** | **Mandatory** when accepting cash, card or payment-service payments. |
| **General system FOP** | **Mandatory** — no group-based exemption. |

### The IBAN-to-IBAN (pure bank transfer) exemption

- **IBAN-to-IBAN exemption** — A settlement that the buyer makes directly from their account to the FOP's IBAN on the basis of an invoice or contract, without a payment card and without a payment service/intermediary, is not treated as a "settlement operation" requiring fiscalisation. Such IBAN→IBAN income needs no PRRO receipt. This is the standard reason a remote/online service FOP (e.g. an IT freelancer paid by SWIFT/IBAN) may legitimately operate with no PRRO. The moment a card, acquiring terminal, or payment service (LiqPay, WayForPay, Fondy, NovaPay, etc.) is introduced, the IBAN exemption is lost and PRRO becomes required (for Groups 2/3 and general system).

### Activities/goods requiring RRO/PRRO regardless of group

- **Goods/activities requiring RRO/PRRO regardless of group** — Certain sales require RRO/PRRO irrespective of single-tax group (i.e. even some Group 1/low-turnover arguments fail). Verify the current list against Art. 296.10 ПКУ and Law №265, but it generally includes: Technically complex household goods subject to warranty (технічно складні побутові товари). Medicines, medical products and medical devices. Jewellery and articles of precious metals / precious & semi-precious stones. Excisable goods (alcohol, tobacco, fuel) where sold by the FOP.  _(Art. 296.10 ПКУ and Law №265)_

### How a PRRO works (process)

- **PRRO process steps** — 1. FOP registers the PRRO (the cash register unit and its cashiers) in the Електронний кабінет. 2. At each cash/card/PSP sale, the FOP creates a fiscal receipt in the PRRO app. 3. The receipt is transmitted to the ДПС fiscal server in real time; offline mode is permitted for a limited time/number of receipts when connectivity fails, then synced. 4. A Z-report is generated at end of shift; the X-report shows current totals. 5. Fiscal receipts/Z-reports become part of the FOP's records and feed the income ledger.

**Penalties (verify amounts):** failure to issue a fiscal receipt where required is penalised at 100% of the value of the goods/service on first violation and 150% on subsequent ones (regime effective from mid-2025). Flag exposure but do not state penalty figures as certain without confirming the current law.

## Section 5 — Primary documents (первинні документи)

Primary documents substantiate every figure in the ledgers. Even single-tax (non-VAT) FOPs, who keep no expense ledger, must hold documents proving income and the origin of goods sold.

- **Income-side documents** — Invoice (рахунок-фактура / рахунок). Can serve as a primary document at the moment of payment if it carries the required requisites. Act of completed works/services (акт виконаних робіт / наданих послуг). Confirms that work was completed and accepted by the client — the core service-FOP document. Contract (договір) with the client (especially for IBAN-to-IBAN income, to evidence the basis of payment and support the no-PRRO position). Fiscal receipts / Z-reports from the PRRO (for cash/card/PSP sales). Bank statements (банківські виписки) showing funds received — the primary evidence of income date and amount for non-cash receipts.
- **Expense-side documents (general system, and VAT-registered Group 3)** — Supplier invoices, видаткові накладні (delivery notes), acts of works/services received. Cash documents, bank payment confirmations. Documents must show a direct link to obtaining business income to be deductible (Art. 177 ПКУ).  _(Art. 177 ПКУ)_
- **Cash vs bank receipts** — Cash sales → require a PRRO fiscal receipt (unless the FOP is a Group 1 exempt operator). Bank/non-cash receipts → evidenced by bank statements; PRRO required only if a card or payment service was involved (not pure IBAN→IBAN).
- **FX / foreign-currency conversion evidence** — Foreign income (common for IT freelancers) is converted to UAH at the NBU exchange rate on the date the funds are credited. Keep the bank credit advice / SWIFT confirmation and the bank statement showing the conversion and crediting date. These evidence both the income amount and the applied rate. Note Ukraine's currency-control rules require export-service proceeds to be repatriated within the prescribed period (verify current NBU term) — keep the contract and inbound-payment evidence to satisfy the bank/NBU as well as the ДПС.

## Section 6 — Retention & audit readiness

- **General retention rule** — Keep primary documents, ledgers, and related records for at least 1095 days (3 years), counted from the deadline for filing the related tax report (or from the date of actual filing if later) for which the documents were used.  _(Art. 44.3 ПКУ)_
- **Longer retention — payments to non-residents / simplified-system entities** — 1825 days (5 years) days (e.g. documents relating to payments to non-residents with Ukrainian-source income (and certain simplified-system legal-entity records) — verify the exact category)  _(Art. 44 ПКУ (see Section 6))_
- **Longer retention — transfer pricing / CFC documentation** — 2555 days (7 years) days (transfer-pricing and controlled-foreign-company documentation — verify the exact category)  _(Art. 44 ПКУ (see Section 6))_
- **The "no audit yet" trap** — If the ДПС has never conducted a documentary audit of the FOP, the taxpayer must, in practice, retain primary documents until such an audit takes place — even beyond 1095 days. Do not advise destroying documents merely because three years have elapsed.
- **Wartime extension** — Under martial law the running of audit limitation periods is suspended, so the effective retention horizon is longer than 1095 days for periods falling within the suspension. Default to keeping everything.

Ledger maintained and reconstructable (electronic copy + backup). Primary documents organised by period and matched to ledger entries. Bank statements reconciled to recorded income. PRRO Z-reports retained and tied to cash/card income. FX credit advices retained for foreign income. Origin-of-goods documents retained where goods are sold.

### Example A — Group 3 single-tax IT freelancer (non-VAT), paid by IBAN

**Facts:** Develops software for foreign clients, paid in USD/EUR to the FOP's foreign-currency account, no card/PSP, no cash. **Ledger:** Книга обліку доходів (income ledger only) — non-VAT single tax. **PRRO:** Not required — payments are IBAN→IBAN with no card or payment service. **Records:** Service contract; act of completed works (or equivalent); bank statement + SWIFT/credit advice showing the UAH-converted amount and crediting date (NBU rate on receipt date). **Entry timing:** Record income in UAH on the date funds are credited. **Retention:** ≥ 1095 days from each annual declaration deadline; keep longer (no audit yet / wartime suspension).

### Example B — Group 2 single-tax with cash sales (small café/services to individuals)

**Facts:** Accepts cash and POS-card payments from walk-in customers. **Ledger:** Книга обліку доходів (income ledger only) — non-VAT single tax. **PRRO:** Mandatory — cash and card settlement operations. Register a PRRO in the Електронний кабінет; issue a fiscal receipt for every sale; generate Z-reports per shift. **Records:** Daily Z-reports feed the income ledger; origin-of-goods documents for resold items; bank statements for card settlements. **Retention:** ≥ 1095 days; longer per Section 6.

### Example C — General-system FOP (consulting + resale of equipment)

**Facts:** On the general system; income taxed on net profit; mix of bank and card income. **Ledger:** Книга обліку доходів і витрат (income-and-expense ledger) in the MoF №261 typical form — paper or electronic; not registered with the ДПС. **PRRO:** Mandatory for cash/card/PSP sales; IBAN→IBAN-only receipts would be exempt. **Records:** Full expense documentation (supplier invoices, видаткові накладні, acts of services received), bank statements, PRRO receipts, contracts. Undocumented expenses are disallowed for ПДФО. **Retention:** ≥ 1095 days; resale/origin-of-goods and any non-resident-payment documents may need longer.

### Example D — Group 1 single-tax market trader

**Facts:** Retail trade at a market; sales to individuals only; within Group 1 limits. **Ledger:** Книга обліку доходів (income ledger only). **PRRO:** Exempt while activity stays within "retail at markets / household services." Selling online or via delivery, or selling listed goods (technically complex goods, jewellery, medicines, excisable goods), would trigger a PRRO obligation. **Records:** Daily income recorded in the ledger; origin-of-goods documents where required.

## Section 8 — Tier 2 Catalogue (reviewer judgement required)

Flag these to a credentialed Ukrainian accountant rather than deciding unilaterally: 1. Whether a payment channel is "IBAN-to-IBAN." Whether a specific PSP/marketplace flow counts as a card/payment-service settlement (PRRO required) or a pure bank transfer (exempt) is fact-specific; transfer codes (e.g. 2924, 2650, 2654) and intermediary involvement matter. 2. Group 1 "format" boundary. Whether a Group 1 trader's activity has strayed beyond "markets / household services" (e.g. social-media or delivery sales) and lost the PRRO exemption. 3. Listed-goods triggers. Whether goods sold fall within the technically-complex / jewellery / medicines / excisable categories that mandate PRRO regardless of group. 4. Origin-of-goods documentation sufficiency for goods-selling single-tax FOPs. 5. Expense deductibility on the general system — the "direct link to income" test under Art. 177. 6. Retention beyond 1095 days — non-resident payments, controlled transactions, depreciable assets, and the wartime suspension's effect on each period. 7. FX recognition date and NBU rate application where banking dates and value dates differ. 8. Single-tax limit breach consequences for records (re-classification, retroactive PRRO duty) — coordinate with ua-single-tax.

## Section 9 — Reference Material + checklist

Tax Code of Ukraine (ПКУ): Art. 44 (record-keeping, retention, 1095/1825/2555-day rules); Art. 296 (single-tax records, 296.10 RRO exemption); Art. 177 (general-system income/expense). Law №265/95-ВР "On the use of registrars of settlement operations" (RRO/PRRO). MoF Order №261 of 13.05.2021 — typical form & order for the income-and-expense ledger (general system / independent professional activity); abolition of mandatory standard single-tax book and of ledger registration from 01.01.2021. Державна податкова служба — tax.gov.ua / dps.gov.ua; Електронний кабінет cabinet.tax.gov.ua.

- [ ] Correct ledger for the system/group (income only vs income-and-expense). - [ ] Ledger kept (paper or electronic) — backed up; no registration needed. - [ ] Income recorded on the date of receipt; FX converted at NBU rate on credit date. - [ ] PRRO registered and used for all cash/card/PSP sales (unless Group 1 exempt or pure IBAN→IBAN). - [ ] Fiscal receipts issued; Z-reports retained. - [ ] Primary documents on file: contracts, invoices, acts of works, bank statements, credit advices. - [ ] Origin-of-goods documents where goods are sold. - [ ] Documents retained ≥ 1095 days (longer where rules or wartime suspension apply).

## PROHIBITIONS

- **Prohibitions list** — Do not state that ledgers must be registered with the ДПС — registration was abolished from 01.01.2021. Only assert the keeping obligation. Do not tell a FOP they need no PRRO without confirming the payment channel — only Group 1 (within format) and genuinely card-/PSP-free IBAN→IBAN flows are exempt. Do not advise destroying documents at 1095 days where no audit has occurred or where the wartime suspension or a longer category applies. Do not treat a single-tax (non-VAT) FOP as needing an expense ledger — income only — but never imply they can discard income/origin-of-goods evidence. Do not quote penalty amounts or specific NBU repatriation terms as settled without verifying current law. Do not compute tax, rates, ЄСВ, the military levy, or VAT here — defer to ua-single-tax and ukraine-vat. Do not advise on company (TOV) accounting — this skill is FOP-only.

## Disclaimer

This skill is research-verified against the State Tax Service of Ukraine (tax.gov.ua / dps.gov.ua), the Tax Code of Ukraine, Law №265, MoF Order №261, and reputable Ukrainian accounting sources, current to May 2026. It has not yet been signed off by a qualified Ukrainian accountant or auditor. Ukrainian record-keeping and PRRO rules change frequently and are affected by martial-law measures; verify the current position before relying on it. This is general information, not tax or legal advice — a credentialed Ukrainian professional must review any output before it is used for filing or compliance. Part of the open-source library at openaccountants.com. Contributions and corrections from qualified Ukrainian practitioners are welcome.

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
