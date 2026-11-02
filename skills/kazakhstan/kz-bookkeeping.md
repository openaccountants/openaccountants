---
name: kz-bookkeeping
description: >
  Use this skill whenever asked about record-keeping, bookkeeping, ledgers, or
  accounting obligations for self-employed people and individual entrepreneurs
  (ИП / жеке кәсіпкер) in Kazakhstan. Trigger phrases like "ЭСФ Казахстан",
  "ККМ Казахстан", "bookkeeping Kazakhstan ИП", "e-invoicing Kazakhstan",
  "электронные счета-фактуры", "онлайн-ККМ", "фискальный чек", "виртуальный склад",
  "СНТ", "first-aid documents Kazakhstan", "what records does an ИП keep",
  "do I need a cash register in Kazakhstan", "Form 910.00 records",
  "упрощённая декларация учёт", "общеустановленный режим учёт", "срок хранения
  документов Казахстан", "налоговый учёт ИП", "e-Salyq", "ИС ЭСФ".
  Distinguishes obligations by tax regime (simplified declaration / упрощённая
  декларация vs general / общеустановленный) and explains when ИП are NOT
  required to keep full бухгалтерский учёт.
version: 1.0
jurisdiction: KZ
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Kazakhstan (KZ) — Record-Keeping & Bookkeeping for the Self-Employed (2026)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers what records a self-employed person in Kazakhstan must keep, by
tax regime, under the **new Tax Code adopted 18 July 2025 and effective from
1 January 2026**. The reply follows the user's language (English prose with the
native Russian/Kazakh tax terms kept verbatim, because these are the legal terms the
user will see on KGD / e-Salyq portals, in 1C and other software, and on documents).

Terms used: ИП (индивидуальный предприниматель / жеке кәсіпкер), СНР (специальный
налоговый режим / special tax regime), упрощённая декларация (simplified
declaration), общеустановленный режим (general regime), налоговый учёт (tax
accounting), бухгалтерский учёт (full accounting), ЭСФ (электронный счёт-фактура /
e-invoice), ИС ЭСФ (information system for ЭСФ), ККМ (контрольно-кассовая машина),
онлайн-ККМ, фискальный чек, ОФД (оператор фискальных данных), Виртуальный склад
(Virtual Warehouse), СНТ (сопроводительная накладная на товары), первичные документы
(primary documents), МРП (месячный расчётный показатель / MCI), ЭЦП (электронная
цифровая подпись), КГД (Комитет государственных доходов).

> YMYL note: tax rules change and the 2026 Tax Code is new. Figures, form numbers,
> and thresholds below were researched against KGD, egov.kz, Big-4 and reputable
> Kazakhstan accounting sources as of May 2026. Anything marked **"verify"** must be
> re-checked at point of use against **kgd.gov.kz** and the e-Salyq / IS ESF portals.

---

## 1. Quick Reference + Conservative Defaults

| Field | Value |
|---|---|
| Country | Republic of Kazakhstan (KZ) |
| Scope | Self-employed individuals: ИП (индивидуальный предприниматель / жеке кәсіпкер) on the simplified declaration (упрощённая декларация) or general (общеустановленный) regime, and persons in private practice. Excludes ТОО / legal entities (full бухгалтерский учёт). |
| Currency | Kazakhstani tenge (KZT, ₸) |
| Authority | State Revenue Committee (Комитет государственных доходов, **КГД**), Ministry of Finance — kgd.gov.kz |
| Legislation | New Tax Code of the RK (adopted 18.07.2025, effective 01.01.2026); MoF orders on ЭСФ issuance rules (2026), ККМ application & receipt content (e.g. MoF Order on ККМ effective 01.01.2026), goods-traceability mechanism rules (effective 01.01.2026), and СНТ — **verify exact order numbers/dates** |
| Portals | ИС ЭСФ (esf.gov.kz / esf.kgd.gov.kz); e-Salyq / Кабинет налогоплательщика (cabinet.salyk.kz); egov.kz; e-Salyq Business / e-Salyq Azamat apps |
| Unit of account | МРП (MCI). For 2026, 1 МРП = **verify current value** (widely reported ~4,325 KZT — confirm against the 2026 budget law) |
| Retention | Generally **5 years** for tax records and primary documents — verify under the new Tax Code |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Kazakhstan accountant |
| Version | 1.0 |

### Conservative defaults (apply when facts are missing or ambiguous)

- **Assume records ARE required.** Default to keeping a налоговый учёт ledger and the
  primary documents that support every income and expense item.
- **Assume онлайн-ККМ IS required** for any ИП taking cash or bank-card payment from
  the public, unless a specific, current exemption is established. Do not assume
  exemption from "small business" or "no employees" alone — verify.
- **Assume ЭСФ may be required** even for a non-VAT ИП when selling goods on the
  **Виртуальный склад**, traceable goods, imported goods, on international transport,
  or commission/consignment supplies. Check the goods/activity, not just VAT status.
- **From 2026 a СНР cannot be combined with VAT-payer status** — this is a major change.
  If the user is VAT-registered, the simplified declaration is not available; verify.
- **Retention: keep everything ≥ 5 years.** When in doubt, keep longer.
- **Never invent МРП values, thresholds, rates, form numbers, or penalty amounts.**
  If not verified, write "verify" and point the user to kgd.gov.kz.
- ИП on a СНР who are not VAT-registered generally do **not** keep full бухгалтерский
  учёт; do not tell such an ИП to prepare financial statements.

---

## 2. Records Required by Regime

| Regime | Ledger / tax accounting | Primary documents | Tax return | ЭСФ | Онлайн-ККМ |
|---|---|---|---|---|---|
| **Simplified declaration (упрощённая декларация)** — ИП on СНР, not VAT-registered | **Simplified налоговый учёт** under the 2026 rules for ИП on СНР who do not keep бухучёт; a tax accounting policy (налоговая учётная политика) and income/turnover records are required — verify exact form | акт выполненных работ/услуг, накладная, счёт на оплату, фискальный чек, bank statements, СНТ where applicable | **Form 910.00**, filed semi-annually (per half-year) — verify; **Form 200.00** quarterly if there are employees | Generally **only if** selling Виртуальный склад / traceable / imported goods, on international transport, or other listed cases — verify | **Generally required** for cash/card sales to the public; narrow exemptions only |
| **General regime (общеустановленный режим)** — ИП | **Налоговый учёт** under the 2026 organisation-of-tax-accounting rules for ИП (simplified order for ИП who do not keep бухучёт); налоговая учётная политика required. Income and expense (deduction) records with supporting documents. | Full set: акт, накладная, счёт, фискальный чек, ЭСФ (issued/received), bank documents, СНТ | Annual ИПН (individual income tax) declaration (e.g. **Form 220.00** — verify); VAT (Form 300.00) if VAT-registered | **Required if VAT-registered**; otherwise per the goods/activity list above | **Generally required** for cash/card sales to the public |

**Key distinction.** Under the 2026 Tax Code, ИП on a СНР who are **not** VAT payers
and **not** classified as keeping mandatory бухучёт are generally **exempt from full
бухгалтерский учёт and from preparing financial statements** — they keep **налоговый
учёт** (tax accounting) instead. New 2026 rules set out the *simplified organisation
of tax accounting* for ИП who do not keep бухучёт, including a налоговая учётная
политика. Exemption from бухучёт does **NOT** exempt anyone from creating and keeping
**первичные документы**: primary documents must still support every transaction, be
drawn up in the state (Kazakh) and/or Russian language, and be retained. Only ТОО and
other legal entities keep full бухгалтерский учёт (out of scope here).

---

## 3. ЭСФ — Electronic Invoicing (Who, When, How)

**What it is.** ЭСФ (электронный счёт-фактура) is the mandatory electronic invoice
issued through the national **ИС ЭСФ** (Information System of Electronic Invoices),
signed with an **ЭЦП** (electronic digital signature). It is the e-invoice backbone of
Kazakhstan's tax system and the basis of input-VAT and goods-traceability control.

**Who must issue ЭСФ (2026).** The circle of obligated persons was **expanded from
1 January 2026** under the new Tax Code. Typically required:
- **All registered VAT payers** — must issue ЭСФ for their supplies.
- **Non-VAT payers (including ИП)** in specific cases, notably: sale of goods held on
  the **Виртуальный склад**; sale of **traceable** goods; sale of **imported** goods;
  **international transport** services; goods sold under **commission/consignment**;
  and other categories listed by the Tax Code / MoF — **verify the current list**.
- A taxpayer on a СНР who is **not** a VAT payer may still be required to issue an
  **invoice/ЭСФ** when selling goods, works or services in the cases above — verify.

**Who does NOT issue ЭСФ.** ЭСФ is not issued on the **sale of personal property by an
individual** (including an individual who is an ИП) — i.e. private, non-business sales.

**Deadlines.** ЭСФ are generally issued within the statutory window (commonly cited as
within a set number of days of the supply) — **verify the current term** for the
supply type, as terms differ for goods, services, and Виртуальный склад items.

**2026 changes to note (verify before quoting specifics):**
- New ЭСФ **form and issuance rules** apply from 2026, including a **new mandatory
  field** added to the ЭСФ form.
- Expanded list of persons obliged to issue ЭСФ.
- New ИС ЭСФ functions tied to the 2026 VAT reform.
- Tighter integration with the **Национальный каталог товаров** (national goods
  catalogue) and goods traceability.

---

## 4. Online Cash Registers (онлайн-ККМ) & Fiscal Receipts

**What it is.** ККМ (контрольно-кассовая машина) — in modern form an **онлайн-ККМ** —
is a fiscal cash register that records each sale and transmits it in real time to the
**ОФД** (оператор фискальных данных) and on to КГД. Each sale produces a **фискальный
чек** for the buyer. Software ККМ (e.g. mobile/app registers) are permitted.

**Who must use it.** Broadly, **any ИП or company accepting cash or bank-card payment
from the public** must use an онлайн-ККМ and issue a фискальный чек. Since around 2020
the obligation has been general across activities; do not assume a "small business" or
"no employees" exemption — **verify the specific activity**.

**Registration (2026).** Registration of онлайн-ККМ is done **on the basis of data
from the ОФД, without visiting the tax office** — verify the current procedure on
egov.kz / e-Salyq.

**Exemptions (narrow — verify each against the current MoF rules):** historically
limited categories, e.g. certain sellers of newspapers/journals, transport ticket
sellers, certain agricultural producers, and a defined list of activities/locations.
Some remote/low-connectivity settlements have had special treatment — **verify**
whether any exemption applies to the user's exact activity and location before advising
"no ККМ".

**2026 changes to note (verify):**
- New **ККМ application rules** and **receipt-content requirements** take effect
  **1 January 2026** (MoF order; commonly cited Order No. 626 — verify number/date).
- Owners of stationary models (e.g. Mercury, Minika, Port) may need a service-centre
  update; software ККМ are updated automatically.
- Receipts must correctly reflect the product (linked to the goods catalogue) — verify.

**ОФД role & retention.** The онлайн-ККМ sends each фискальный чек to an accredited ОФД,
which validates and forwards it to КГД and stores fiscal data. The ОФД's storage does
**not** replace the taxpayer's own document-retention duty.

---

## 5. Виртуальный склад, Traceability, Primary Documents, Retention & Portals

### Виртуальный склад (Virtual Warehouse) & goods traceability

The **Виртуальный склад (ВС)** is a **module of ИС ЭСФ** that tracks the movement and
stock of specific goods and underpins Kazakhstan's **goods-traceability** mechanism
(implementing an EAEU international agreement). For goods on the ВС / traceable goods:
- supplies are documented through **СНТ** (сопроводительная накладная на товары —
  electronic consignment/shipping note) and **ЭСФ** via ИС ЭСФ;
- the list of goods covered by the ВS and by СНТ was **expanded for 2026** (MoF orders,
  e.g. lists approved in late 2025 effective 01.01.2026 — verify);
- on **technical failure**, documents may be issued on paper temporarily and entered
  into the system within the statutory window (commonly cited as 15 days — verify).

If the user does not trade in listed/traceable goods, the ВС and СНТ usually do not
apply — but **verify** the goods against the current catalogue, as the list grows.

### Primary documents (первичные документы)

Must be drawn up in **Kazakh and/or Russian**, without reference to bookkeeping
accounts when prepared by an ИП who does not keep бухучёт. Core documents:
- **Акт** (акт выполненных работ / оказанных услуг) — confirms services/works; main
  document for service freelancers.
- **Накладная** / **СНТ** — confirms transfer of goods (СНТ for traceable goods).
- **Счёт на оплату** — payment request / pro-forma; basis for payment.
- **ЭСФ** — the electronic VAT/invoice document via ИС ЭСФ where required.
- **Фискальный чек** — the receipt from онлайн-ККМ for cash/card sales.
- **Bank statements** — evidence of receipts and payments.

### Retention

Generally **5 years** for tax records and supporting primary documents — verify the
exact term and start point under the 2026 Tax Code (some categories may run longer).

### Portals

- **ИС ЭСФ** — esf.gov.kz / esf.kgd.gov.kz (issue/receive ЭСФ, Виртуальный склад, СНТ).
- **e-Salyq / Кабинет налогоплательщика** — cabinet.salyk.kz (returns, reporting).
- **egov.kz** — ККМ registration and many state services.
- **e-Salyq Azamat / e-Salyq Business** — mobile services for individuals/business.
- **kgd.gov.kz** — КГД, the authority and primary reference.

---

## 6. Worked Examples

**Example 1 — ИП on simplified declaration, IT freelancer billing businesses.**
Aizhan is an ИП on the **упрощённая декларация**, not VAT-registered, paid by bank
transfer by company clients. She keeps **simplified налоговый учёт** (with a налоговая
учётная политика and turnover records), issues an **акт** and **счёт** for each
engagement, files **Form 910.00 semi-annually** (verify), and keeps no full
бухгалтерский учёт. She generally needs **no онлайн-ККМ** (no cash/card from the
public) and generally issues **no ЭСФ** — *unless* she sells listed/traceable/imported
goods or falls in another listed case. Retention: **5 years**. *Flag:* if she ever
registers for VAT she **loses** the СНР from 2026 — verify.

**Example 2 — ИП on simplified declaration, retail shop taking cash and cards.**
Bauyrzhan runs a kiosk on the **упрощённая декларация**, selling to the public. He
**must use an онлайн-ККМ** with an **ОФД** contract and issue a **фискальный чек** for
every sale. If his goods are on the **Виртуальный склад** / traceable list, he must
also handle **СНТ** and **ЭСФ** via ИС ЭСФ — *even though he is not a VAT payer* —
verify against the 2026 goods list. He keeps supplier накладные/СНТ, чеки, and bank
statements for **5 years**, and keeps **налоговый учёт**, not full бухучёт.

**Example 3 — ИП on general regime, VAT-registered, mixed B2B/B2C.**
Dana is an ИП on the **общеустановленный режим**, VAT-registered. She **must issue ЭСФ**
for her supplies through **ИС ЭСФ** (signed with ЭЦП), files **Form 300.00 (VAT)** and
the annual **ИПН** declaration (Form 220.00 — verify), and uses an **онлайн-ККМ** for
any cash/card sales to the public. She keeps **налоговый учёт** under the 2026 ИП
tax-accounting rules (she does not keep бухучёт as an ИП), retains all ЭСФ, чеки,
акты, накладные/СНТ and bank documents for **5 years**, and reflects products
correctly on receipts per the 2026 ККМ rules.

---

## 7. Tier 2 Notes + References + Checklist

### Tier 2 / ambiguity flags (escalate or verify, do not guess)
- **2026 МРП value** and any threshold expressed in МРП (simplified-declaration income
  limit, VAT-registration threshold) — sources conflict; **verify** before quoting.
- Exact **simplified-declaration income ceiling** (cited variously as ~600,000 МРП and
  ~2.36–2.6 bn KZT) and whether the user qualifies — verify.
- **VAT-registration threshold** for 2026 (cited variously, e.g. ~10,000 МРП or a fixed
  KZT figure) — verify; it determines whether ЭСФ becomes mandatory across all supplies.
- Whether the **СНР cannot be combined with VAT** affects the user's regime choice —
  verify and route to a regime-choice resource if needed.
- Exact **ЭСФ / ККМ / СНТ form numbers, fields, and issuance terms** for 2026 — verify.
- Whether specific **goods** are on the **Виртуальный склад / traceable / СНТ** list —
  verify against the current catalogue (it is expanding).
- **Penalty amounts** for missing ЭСФ, чеки, or records — verify; do not quote unverified.
- **Patent (патент)** regime and **retail tax** specifics, payroll, and ТОО / legal
  entities — out of primary scope; route elsewhere.

### References (verify at point of use)
- **kgd.gov.kz** — State Revenue Committee (КГД), primary authority
- **esf.gov.kz / esf.kgd.gov.kz** — ИС ЭСФ, Виртуальный склад, СНТ
- **cabinet.salyk.kz / e-Salyq** — Кабинет налогоплательщика, returns
- **egov.kz** — ККМ registration and state services
- New **Tax Code of the RK** (adopted 18.07.2025, effective 01.01.2026)
- MoF orders on **ЭСФ issuance rules (2026)**, **ККМ application & receipt content
  (effective 01.01.2026)**, **goods-traceability mechanism**, and **СНТ** — verify nos.
- PwC *Kazakhstan — Other taxes*; EY / Baker McKenzie / Moore / Dentons 2026 tax notes

### Checklist (run before concluding)
- [ ] Regime identified: simplified declaration / general (or patent/retail → escalate)?
- [ ] VAT status established (and SNR+VAT incompatibility from 2026 flagged)?
- [ ] Correct ledger named: налоговый учёт (not full бухучёт for an ИП on СНР)?
- [ ] ЭСФ obligation assessed by VAT status AND by goods/activity (Виртуальный склад,
      traceable, imported, international transport)?
- [ ] Онлайн-ККМ obligation assessed, including ОФД and narrow exemptions?
- [ ] Виртуальный склад / СНТ assessed for traceable goods?
- [ ] Primary documents listed (акт / накладная / СНТ / счёт / ЭСФ / фискальный чек)?
- [ ] Retention stated as 5 years (with longer-period caveat)?
- [ ] Confirmed ИП on СНР do not keep full бухгалтерский учёт?
- [ ] All unverified МРП values, thresholds, forms, terms flagged "verify"?
- [ ] Reply in the user's language; Russian/Kazakh terms kept verbatim?

---

## PROHIBITIONS

- Do **not** invent or guess **МРП values, thresholds, tax rates, form numbers, ЭСФ/ККМ
  issuance terms, or penalty amounts**. If not verified, write "verify" and cite
  kgd.gov.kz.
- Do **not** tell an ИП on a СНР (not VAT-registered) that they must keep full
  бухгалтерский учёт or file financial statements — that is a ТОО / legal-entity
  obligation. They keep налоговый учёт plus primary documents.
- Do **not** say an ИП may skip **ЭСФ** purely because they are not VAT-registered —
  ЭСФ can still be required for Виртуальный склад / traceable / imported goods,
  international transport, and other listed cases. Check the goods/activity.
- Do **not** assert an **онлайн-ККМ** exemption based on "small business" or "no
  employees" alone — verify a specific, current exemption for the exact activity/location.
- Do **not** tell a user they may combine a **СНР with VAT-payer status** in 2026 — this
  combination is removed under the new Tax Code; verify and advise a regime choice.
- Do **not** advise shorter retention than **5 years**.
- Do **not** handle ТОО / legal entities, patent or retail-tax specifics, payroll, or
  non-self-employed scenarios under this skill — route elsewhere.
- Do **not** present this output as filed/final advice without a qualified Kazakhstan
  accountant's sign-off.

## Disclaimer

This skill is **research-verified** content from the Open Accountants Community, current
to the best available public sources as of **May 2026**, and is **pending sign-off by a
qualified Kazakhstan accountant**. It is general information, not individualised tax
advice. The new Kazakhstan Tax Code (effective 1 January 2026) and its implementing MoF
orders on ЭСФ, ККМ, СНТ and goods traceability are recent and still settling; МРП
values, thresholds, forms, issuance terms, and exemptions change — always verify against
**kgd.gov.kz** and the **ИС ЭСФ / e-Salyq** portals at the point of use. A qualified
Kazakhstan accountant or tax adviser must review any output before it is relied upon for
filing. See **openaccountants.com**.
