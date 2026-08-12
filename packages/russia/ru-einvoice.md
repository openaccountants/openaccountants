---
name: ru-einvoice
description: "Use this skill whenever asked about Russian electronic invoicing or digital tax reporting for a self-employed person or small business: the VAT invoice (счёт-фактура), the universal transfer document (УПД), electronic document exchange (ЭДО) and when e-invoices are mandatory, the goods traceability system (национальная система прослеживаемости товаров), online cash registers (ККТ / онлайн-касса) transmitting via ОФД to ФНС, product labelling («Честный знак» / маркировка), the electronically filed VAT return, and what a самозанятый (НПД), an ИП on УСН, and an ИП/ООО on ОСНО must each do. Trigger on phrases like \"счёт-фактура\", \"УПД\", \"ЭДО Russia\", \"online cash register Russia\", \"ККТ\", \"онлайн-касса\", \"ОФД\", \"прослеживаемость\", \"маркировка\", \"Честный знак\", \"e-invoicing Russia\", or any question about Russian digital invoicing or fiscal reporting. Always read this skill before advising on Russian e-invoicing or fiscal reporting."
version: 1.0
jurisdiction: RU
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# RU Einvoice

## Russia — Electronic Invoicing & Digital Reporting (ЭДО, ККТ, прослеживаемость)

> **Quality tier:** Research-verified — pending sign-off by a Russian accountant.
> **Tax year:** 2026. Verified against ФНС (nalog.gov.ru) and reputable Russian secondary sources in May 2026. Several rollouts are still phasing in — items marked **[verify]** must be re-checked against current ФНС guidance before use.
> Respond to the user in their own language (Russian or English). Russian native terms are kept inline so the skill works for both.

This skill describes the *plumbing* of Russian tax compliance — how documents are created, signed, exchanged, and reported electronically. It does **not** compute tax. For VAT classification and the НДС return itself, defer to the `russia-vat` skill; for income tax / regime selection, defer to `ru-income-tax`, `ru-usn`, and `ru-self-employed-npd`.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Russian Federation (RU) |
| Scope | Electronic invoicing & digital reporting — счёт-фактура / УПД, ЭДО, ККТ/ОФД, прослеживаемость, маркировка, e-filed VAT return |
| Currency | Russian rouble (RUB / ₽) |
| Systems | **ЭДО** (electronic document exchange via operators), **ОФД/ККТ** (online cash registers → fiscal data operators → ФНС), **прослеживаемость** (national goods traceability), **«Честный знак»** (mandatory labelling/маркировка) |
| Authority | Federal Tax Service — **ФНС** (nalog.gov.ru). Labelling operator: ЦРПТ / «Честный знак» (chestnyznak.ru) |
| Primary law | НК РФ Part Two, Ch. 21 (счёт-фактура, ст. 169); Federal Law No. 54-ФЗ (ККТ); Government Decree No. 1137 (invoice forms); Federal Law No. 371-ФЗ (traceability); Federal Law No. 487-ФЗ (labelling); Federal Law No. 425-ФЗ of 28 Nov 2025 (VAT rate 20%→22% and УСН VAT changes from 2026) |
| Quality tier | Research-verified — pending sign-off by a Russian accountant |
| Skill version | 1.0 |

### Conservative defaults

When facts are missing, assume the position that minimises ФНС penalty risk and flag for the reviewer:

- **Default to electronic, not paper.** If a counterparty deals in traceable (прослеживаемые) or labelled (маркированные) goods, assume the счёт-фактура / УПД **must** be electronic via an ЭДО operator. Do not advise paper.
- **Default to "ККТ required"** for any retail sale or service settlement with an individual, unless a specific 54-ФЗ exemption clearly applies.
- **Never assume the user is the simplest regime.** Confirm whether they are самозанятый (НПД), ИП on УСН, ИП on ОСНО, or ООО — obligations differ sharply.
- **Treat rollout dates as moving.** Labelling and traceability scope expand almost every quarter; mark scope claims **[verify]** against the current «Честный знак» calendar and the Government traceability list.
- **Do not guess document formats/versions.** Confirm the current ФНС-approved XML format (e.g. УПД version) before asserting it is mandatory.

## 2. Who Must Do What — by Regime

**Who Must Do What — by Regime**

| Obligation | Самозанятый (НПД) | ИП on УСН | ИП/ООО on ОСНО |
| --- | --- | --- | --- |
| **Issue счёт-фактура (VAT invoice)** | No — not a VAT payer; issues a **чек** in «Мой налог» instead | Only if a VAT payer (2025 income > ₽20m) **or** voluntarily issues VAT invoices | **Yes** — VAT payer; счёт-фактура is mandatory for taxable supplies |
| **Use ЭДО (electronic exchange)** | Not required | Required if dealing in traceable/labelled goods; otherwise optional but common | Required for traceable/labelled goods; e-invoices and e-VAT-return effectively force ЭДО |
| **Online cash register (ККТ/ОФД)** | **No** — the «Мой налог» чек replaces ККТ | **Yes** for most retail/service sales to individuals (some exemptions) | **Yes** for most retail/service sales to individuals |
| **VAT return (НДС-декларация)** | No | Only if a VAT payer; electronic, quarterly | **Yes** — electronic, quarterly |
| **Traceability reporting (прослеживаемость)** | No | Yes if it handles traceable goods | Yes if it handles traceable goods |
| **Labelling («Честный знак»)** | Effectively no (NPD cannot resell most labelled categories for resale) | Yes if it produces/imports/sells labelled goods | Yes if it produces/imports/sells labelled goods |

### Key takeaways

- **Самозанятый (НПД):** the lightest regime. **No счёт-фактура, no ККТ, no VAT return.** The only document is the **чек** generated in the **«Мой налог»** app after each receipt of income; it is sent to the customer (link, QR, paper, or e-mail) and constitutes the income confirmation to ФНС. The app reports income to ФНС automatically — there is no separate filing. (See `ru-self-employed-npd`.)
- **ИП on УСН:** from 2026 a simplified-regime taxpayer **becomes a VAT payer if 2025 income exceeded ₽20,000,000** (threshold drops to ₽15m for 2027 and ₽10m from 2028) — Federal Law No. 425-ФЗ. A VAT-paying упрощенец must issue счета-фактуры, keep the книга продаж / книга покупок, and file the НДС-return electronically. Below the threshold, no VAT invoices and no VAT return — but ККТ and (if applicable) traceability/labelling obligations still apply.
- **ИП/ООО on ОСНО:** full VAT obligations — счёт-фактура mandatory, ledgers, quarterly e-filed VAT return, plus ККТ and any traceability/labelling duties.

## 3. счёт-фактура / УПД & When ЭДО Is Mandatory

### 3.1 The documents

- **счёт-фактура** — The VAT invoice under НК РФ ст. 169. It is the document that supports the buyer's input-VAT deduction (вычет НДС). Required from VAT payers on taxable supplies. Mandatory content includes the parties, the VAT rate (standard **22%** from 1 Jan 2026, or 10% / 0%), the amount, and — for special goods — traceability/labelling fields.  _(НК РФ ст. 169)_
- **УПД (универсальный передаточный документ)** — The "universal transfer document" that combines an invoice with a primary handover document (it can replace the ТОРГ-12 delivery note or an act of services). The УПД with status **«1»** doubles as a счёт-фактура (for VAT) **and** a primary document; status **«2»** is a primary document only (no VAT function). From 2026 the УПД is the expected replacement for separate delivery notes and acts in ЭДО. **[verify]**
- **Format/version** — ФНС publishes the approved XML format. For 2026 the УПД e-format moved to a new version (reported as **5.03**) reflecting the 22% rate and the traceability/labelling fields. Confirm the current mandatory version and effective date against ФНС before asserting it. **[verify]**

### 3.2 ЭДО — electronic document exchange

- **ЭДО (электронный документооборот)** — The exchange of legally significant documents in electronic form, usually through a certified **оператор ЭДО** (e.g. Контур.Диадок, СБИС, Такском). Documents are signed and transmitted over the operator's secured channel; ФНС can request them electronically.
- **Traceable goods (прослеживаемые товары)** — счёт-фактура and УПД for operations with traceable goods **must be electronic via an ЭДО operator** — paper is not permitted. The document must carry the **РНПТ** and the related fields (graphs 11, 12/12а, 13, 14 of the invoice).  _(НК РФ; Federal Law No. 371-ФЗ)_
- **Labelled goods (маркированные товары)** — Transfer of «Честный знак»–labelled goods between participants is documented through electronic УПД in the labelling system; e-document exchange is effectively required. **[verify scope by category]**
- **Practical compulsion for VAT payers** — The VAT return is filed electronically and includes invoice-level data from the книга продаж / книга покупок, so VAT payers run счета-фактуры through ЭДО or e-reporting software in practice even where paper is technically still allowed for non-traceable goods.
- **Signing** — Legally significant e-documents normally use a **qualified electronic signature (КЭП — квалифицированная электронная подпись)**. Note a 2026 development: for routine document flow ФНС accepts the operator's secured channel, so parties are not always required to apply КЭП for ordinary (non-mandatory-КЭП) documents — verify the exact document types this applies to. **[verify]**

### 3.3 What each regime does here

- **НПД:** none of this. No счёт-фактура, no УПД, no ЭДО. (If a customer demands a VAT invoice, the NPD person generally cannot/should not issue one — flag and refer to `ru-self-employed-npd`.)
- **УСН non-VAT-payer:** no счёт-фактура; may still need ЭДО + electronic УПД if it touches traceable or labelled goods.
- **УСН VAT-payer / ОСНО:** issue счета-фактуры (or УПД status 1); use ЭДО for traceable/labelled goods; data flows into the e-filed VAT return.

## 4. ККТ / Онлайн-касса & ОФД

### 4.1 How it works

- **ККТ/ОФД mechanism** — Under **Federal Law No. 54-ФЗ**, most businesses settling with individuals must use a **контрольно-кассовая техника (ККТ / онлайн-касса)** fitted with a **fiscal drive (фискальный накопитель)**. Each receipt (кассовый чек) is sent in real time through a **fiscal data operator (ОФД — оператор фискальных данных)** to **ФНС**. The customer gets a paper or electronic чек (with a QR code that lets the customer verify it via the ФНС checker). Cash-register receipt requisites tightened from 1 September 2025 (e.g. buyer phone/e-mail tags for online payment, time zone, non-cash amount, QR) and those requirements continue into 2026.  _(Federal Law No. 54-ФЗ)_

### 4.2 Who must use ККТ in 2026

- **Who must use ККТ — required** — Most ИП and organisations on **ОСНО and УСН** that sell goods or services to individuals, online or offline, must use ККТ.  _(Federal Law No. 54-ФЗ)_
- **Exempt (selected, non-exhaustive)** — - **Самозанятые (НПД)** — fully exempt for NPD income; the **«Мой налог» чек** replaces the cash receipt. - Certain **ПСН (патент)** activities listed in 54-ФЗ. - Businesses in designated remote/hard-to-reach areas (паспортных условиях) — may issue paper БСО without transmitting through ОФД. - Specific personal services without hired staff (e.g. shoe repair, tutoring, renting out one's own dwelling, certain childcare) — verify the current list, it changes. **[verify]**  _(Federal Law No. 54-ФЗ)_
- **Penalties** — Penalties for ККТ violations are scheduled to **increase in 2026** — flag this as a real cost of non-compliance. **[verify exact amounts]**

### 4.3 By regime

**ККТ / ОФД by regime**

| Regime | ККТ / ОФД |
| --- | --- |
| Самозанятый (НПД) | **Not required** — чек in «Мой налог» |
| ИП on УСН | **Required** for most B2C sales (limited exemptions) |
| ИП/ООО on ОСНО | **Required** for most B2C sales |

### 4.3 By regime

Note: ККТ is for *settlement* receipts to customers; the счёт-фактура/УПД is a separate VAT/primary document. A VAT-paying retailer may need **both** a кассовый чек (for the sale) and a счёт-фактура/УПД (for the VAT/B2B leg).

## 5. Traceability (прослеживаемость) & Labelling (маркировка)

These are two **different** systems — do not conflate them.

### 5.1 National goods traceability — прослеживаемость

- **What is прослеживаемость** — The **национальная система прослеживаемости товаров** is a *document-based* (not physical-marking) system tracking certain **imported goods** by lot. There is **no physical code on the item** — tracking is by the **РНПТ (регистрационный номер партии товара)** carried through invoices.  _(Federal Law No. 371-ФЗ)_
- **Scope** — A Government-approved list (e.g. monitors and projectors, certain refrigeration/AC equipment, industrial vehicles, washing machines, certain children's items, etc.). The list is amended periodically — verify the current Government перечень before classifying. **[verify]**
- **РНПТ** — The importer registers each incoming lot with ФНС and obtains the РНПТ; for EAEU imports the participant requests it from ФНС.
- **Mandatory e-invoices** — Operations with traceable goods require **electronic** счёт-фактура / УПД via ЭДО, carrying the РНПТ and graphs 11–14.
- **Reporting** — Participants file a **quarterly report on operations with traceable goods (отчёт об операциях)** to ФНС, due by the **25th** of the month after the quarter. VAT payers reflect traceability data within the VAT return ecosystem; non-VAT-payers (e.g. УСН) file the separate operations report.
- **Liability** — Dedicated penalties for traceability violations are scheduled to take effect from **1 September 2026** — until then enforcement is lighter, but the documentary obligations already apply. **[verify]**

### 5.2 Product labelling — «Честный знак» / маркировка (brief)

- **What is «Честный знак»** — A *physical* marking system. Each unit carries a **Data Matrix** code registered in the **«Честный знак»** system (operator ЦРПТ) so the unit can be tracked from producer/importer to retail sale.
- **Categories (2026, expanding)** — Include footwear, clothing/light industry, dairy, bottled water, tobacco/nicotine, beer and low-alcohol drinks, pet food, veterinary preparations, dietary supplements (БАДы), antiseptics, and more. Scope and start dates change almost every quarter — verify against the «Честный знак» calendar. **[verify]**
- **At the till** — From 2026 a **разрешительный режим (permission/validation mode)** applies for many categories — the cash software queries «Честный знак» at sale to confirm the code is legal, unsold, not expired, etc. This links ККТ to labelling.
- **Documents** — Transfers of labelled goods between participants are documented via **electronic УПД** in the labelling system.
- **Relevance to the self-employed** — A **самозанятый (НПД) generally cannot resell labelled goods for resale** (NPD prohibits resale of others' goods), so labelling rarely applies to NPD producers of their own non-listed goods. ИП/ООО handling listed categories must register in «Честный знак» and mark units.

## 6. Worked Examples

### Example 1 — Freelance developer, самозанятый (НПД)

A developer on НПД invoices a Russian client ₽150,000 for a project. **Does she issue a счёт-фактура or use a cash register?** No. As an NPD payer she is **not a VAT payer** and is **exempt from ККТ**. She generates a **чек in «Мой налог»** after receiving payment and sends the чек link to the client. No счёт-фактура, no ЭДО, no VAT return. The app reports the income to ФНС automatically. If the client insists on a VAT invoice, that is a sign the client expects a VAT-paying counterparty — she cannot provide one; escalate to the reviewer / `ru-self-employed-npd`.

### Example 2 — ИП on УСН, retail shop, no traceable goods, 2025 income ₽8m

The shop sells ordinary (non-traceable, non-labelled) goods to walk-in customers. **Obligations:** Below the ₽20m VAT threshold, so **no счёт-фактура and no VAT return**. But it **must use an online cash register (ККТ)** transmitting кассовые чеки through an **ОФД** to ФНС for its retail sales. No ЭДО is mandatory unless it later starts handling traceable/labelled stock.

### Example 3 — ИП on УСН crossing the VAT threshold + traceable goods

An ИП on УСН had 2025 income of ₽26m (above ₽20m) and imports monitors (a traceable category). From 2026 it is a **VAT payer**: it must issue **счета-фактуры** (or УПД status 1), keep the книга продаж / книга покупок, and **file the НДС-return electronically**. Because monitors are traceable, those invoices/УПД **must be electronic via an ЭДО operator** and carry the **РНПТ**. It also files the **quarterly traceability operations report** and continues to use **ККТ** for any B2C sales. (VAT computation → `russia-vat`.)

### Example 4 — ООО on ОСНО selling labelled footwear at retail

Footwear is a «Честный знак» category. The ООО must register in «Честный знак», ensure each pair carries a **Data Matrix** code, and at the till the **ККТ** software validates the code under the разрешительный режим and transmits the чек via **ОФД**. As an ОСНО VAT payer it issues **счета-фактуры/УПД** and files the **electronic VAT return** quarterly (due the 25th of the month after the quarter, electronic only via an ЭДО/ТКС operator).

## 7. Tier 2 Issues, References & Checklist

### Tier 2 — escalate to a credentialed Russian accountant

- Whether a specific good is **traceable** or **labelled** in 2026, and the exact start date for a new category. **[verify]**
- The current **mandatory УПД / счёт-фактура XML format version** and its effective date. **[verify]**
- Exact **54-ФЗ ККТ exemptions** for a given activity, and 2026 penalty amounts. **[verify]**
- Cross-border / EAEU operations, **sanctions** impact on document exchange and foreign counterparties (international sanctions can affect ЭДО with non-RU parties).
- Whether a УСН taxpayer should take the special 5%/7% VAT rates (no input credit) vs standard rates — defer to `russia-vat`.
- The interaction of the **разрешительный режим** with a particular cash software / ОФД setup.

### Reference

- ФНС — nalog.gov.ru (счёт-фактура, ЭДО, traceability, ККТ, VAT return).
- НК РФ Part Two, Ch. 21 (ст. 169 счёт-фактура; e-filing of the VAT return).
- Federal Law No. 54-ФЗ — ККТ / online cash registers / ОФД.
- Federal Law No. 371-ФЗ — traceability (прослеживаемость), РНПТ, operations report.
- Federal Law No. 487-ФЗ — mandatory labelling (маркировка); «Честный знак» (chestnyznak.ru, operator ЦРПТ).
- Federal Law No. 425-ФЗ of 28 Nov 2025 — VAT 20%→22% and УСН VAT changes from 2026.
- Government Decree No. 1137 — invoice/УПД forms and ledger rules.

### Compliance checklist

- [ ] Identify the regime: самозанятый (НПД) / ИП УСН / ИП-ООО ОСНО.
- [ ] Is the taxpayer a **VAT payer**? (ОСНО = yes; УСН = yes only if 2025 income > ₽20m or voluntary.) → drives счёт-фактура + e-VAT-return.
- [ ] Does the taxpayer sell to individuals? → **ККТ via ОФД** required unless a 54-ФЗ exemption applies (NPD always exempt).
- [ ] Does any good appear on the **traceability** list? → **electronic** счёт-фактура/УПД via ЭДО with **РНПТ**, plus the quarterly operations report. **[verify list]**
- [ ] Does any good appear on the **labelling** list? → register in «Честный знак», Data Matrix codes, разрешительный режим at the till. **[verify list]**
- [ ] Confirm the **current ФНС-approved УПД/счёт-фактура format version**. **[verify]**
- [ ] VAT return: **electronic only**, quarterly, by the **25th** of the month after the quarter, through an ЭДО/ТКС operator.
- [ ] Confirm signing requirements (КЭП vs operator secured channel). **[verify]**

## PROHIBITIONS

- **Prohibitions list** — - Do NOT advise a самозанятый (НПД) to issue a счёт-фактура, register a ККТ, or file a VAT return — the «Мой налог» чек is the only document, and NPD is not a VAT payer. - Do NOT tell a taxpayer that paper счёт-фактура/УПД is acceptable for traceable goods — those documents must be electronic via an ЭДО operator. - Do NOT assert a specific good is (or is not) traceable or labelled, or state a category start date, without verifying the current Government / «Честный знак» list. Mark such claims [verify]. - Do NOT state a mandatory document format/version (e.g. УПД 5.03) as settled fact without confirming against current ФНС guidance. [verify] - Do NOT advise that a paper VAT return is acceptable for a VAT payer — the НДС-декларация is electronic only; a paper filing by an obligated payer is treated as not submitted. - Do NOT compute VAT amounts, choose УСН VAT rates, or determine regime eligibility here — defer to `russia-vat`, `ru-usn`, `ru-income-tax`, `ru-self-employed-npd`. - Do NOT ignore sanctions exposure on cross-border e-document exchange — flag it as Tier 2/Tier 3 for the reviewer. - Do NOT issue final advice without credentialed Russian-accountant sign-off.

## Disclaimer

This skill is **research-verified — pending sign-off by a qualified Russian accountant.** It was prepared from ФНС (nalog.gov.ru) and reputable Russian secondary sources as at **May 2026** for tax year **2026**. Russian e-invoicing, traceability, labelling, and ККТ rules change frequently and several rollouts are still phasing in; items marked **[verify]** must be re-checked against current official sources before reliance. Nothing here is a substitute for advice from a qualified Russian accountant or tax adviser, who must review and approve any output before it is acted upon or filed. Part of the open-source tax skills library at **openaccountants.com**.

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
