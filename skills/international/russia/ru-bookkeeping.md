---
name: ru-bookkeeping
description: Use this skill whenever asked about record-keeping, bookkeeping, or accounting obligations for self-employed people and individual entrepreneurs (ИП) in Russia. Trigger phrases like "КУДиР", "bookkeeping Russia", "онлайн-касса", "ККТ", "what records ИП keep", "самозанятый records", "книга учёта доходов и расходов", "do I need a cash register in Russia", "Мой налог чеки", "ОФД", "сколько хранить документы", "first-aid documents акт накладная счёт", "does an ИП need full accounting", "НПД vs УСН vs ОСНО records". Distinguishes obligations by tax regime (НПД / самозанятый, УСН, ОСНО) and explains why ИП generally are NOT required to keep full бухгалтерский учёт.
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

# RU Bookkeeping

## Russia (RU) — Record-Keeping & Bookkeeping for the Self-Employed (2026)

This skill covers what records a self-employed person in Russia must keep, by tax regime. The reply language follows the user (English prose with native Russian tax terms kept verbatim, since these are the legal terms the user will see on the ФНС portal, in software, and on documents). Russian terms used: КУДиР (книга учёта доходов и расходов), ККТ / онлайн-касса, ОФД (оператор фискальных данных), самозанятый, НПД (налог на профессиональный доход), ФНС, личный кабинет, первичные документы, акт, накладная, счёт.

> YMYL note: tax rules change. Figures and form numbers below were verified against ФНС и reputable Russian accounting sources as of May 2026, but anything marked "verify current value" must be re-checked at point of use against nalog.gov.ru (and npd.nalog.ru for самозанятые).

## 1. Quick Reference + Conservative Defaults

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Russian Federation (RU) |
| Scope | Self-employed individuals: самозанятые (НПД) and individual entrepreneurs (ИП) on УСН or ОСНО. Excludes ООО / legal entities (they keep full бухгалтерский учёт). |
| Currency | Russian rouble (RUB, ₽) |
| Legislation | НК РФ (Tax Code); Law 54-ФЗ (ККТ / онлайн-касса); Law 422-ФЗ of 27.11.2018 (НПД / самозанятые); Law 402-ФЗ "О бухгалтерском учёте" (accounting); Приказ Минфина 86н/БГ-3-04/430 of 13.08.2002 (ИП ОСНО ledger); Приказ ФНС ЕА-7-3/816@ of 07.11.2023 (УСН КУДиР form) — verify current form |
| Authority | Федеральная налоговая служба (ФНС России) — nalog.gov.ru |
| Portal | Личный кабинет налогоплательщика (lkfl2.nalog.ru / lkip.nalog.ru); app «Мой налог» for самозанятые |
| Retention | Generally 5 years for tax records and primary documents (ст. 23 НК РФ, increased from 4 to 5 years by Law 6-ФЗ of 17.02.2021) |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a Russian accountant |
| Version | 1.0 |

### Conservative defaults (apply when facts are missing or ambiguous)

- **Assume records ARE required** unless the user clearly qualifies for an exemption. Default to keeping a ledger and primary documents.
- **Assume ККТ (онлайн-касса) IS required** for ИП taking payment from individuals for goods/works/services, unless a specific exemption is established. The general deferral for ИП without employees ended 01.07.2021 — verify no new exemption applies.
- **Самозанятые (НПД): no ledger, no ККТ** — but every taxable receipt MUST produce a чек in «Мой налог». Treat a missing чек as a compliance failure (penalty 20% of the amount, 100% on repeat within 6 months — verify current value).
- **Retention: keep everything ≥ 5 years.** When in doubt, keep longer.
- **Never invent form numbers, line numbers, rates, or thresholds.** If not verified, say "verify current value" and point the user to nalog.gov.ru.
- ИП do **not** keep full бухгалтерский учёт; do not advise an ИП to prepare financial statements (бухгалтерская отчётность) — that is an ООО obligation.

## 2. Records Required by Regime

**Records Required by Regime table**

| Regime | Ledger / records | Primary documents | Tax return | ККТ / онлайн-касса |
| --- | --- | --- | --- | --- |
| **Самозанятый (НПД)** — individual or ИП on НПД | **No ledger.** Income is recorded by issuing a чек in «Мой налог» for each payment; the app auto-computes the tax. | чек from «Мой налог» is the primary income record. Contracts/акт optional but recommended for B2B. | **None** — no declaration filed; ФНС gets data from «Мой налог». | **Exempt** — «Мой налог» replaces the cash register. |
| **ИП on УСН** | **КУДиР** (книга учёта доходов и расходов). "Доходы" object: record income (and certain deductions). "Доходы минус расходы": record income and deductible expenses. | акт, накладная (ТОРГ-12 / УПД), счёт, банковские выписки, чеки/БСО. | Annual УСН declaration (verify current form — приказ ФНС ЕД-7-3/1017@ from 28.02.2026 introduced an updated form; verify). | **Generally required** for cash/card sales to individuals; exemptions are narrow — verify. |
| **ИП on ОСНО** | **Книга учёта доходов и расходов и хозяйственных операций** (Приказ Минфина 86н, 13.08.2002), cash method, positional, chronological. Plus VAT registers (книга покупок / книга продаж) if VAT-registered. | Full set: акт, накладная/УПД, счёт, счёт-фактура (for VAT), банк, кассовые документы. | НДФЛ (3-НДФЛ) annually; VAT returns quarterly if applicable. | **Generally required** for cash/card sales to individuals — verify. |

- **ИП not required to keep full бухгалтерский учёт** — ИП are NOT required to keep full бухгалтерский учёт (full double-entry accounting and financial statements) under Law 402-ФЗ, because they keep tax accounting (налоговый учёт) instead — the relevant ledger above. This holds on every regime. Only ООО and other legal entities must keep full бухгалтерский учёт. However, exemption from бухучёт does not exempt anyone from creating and keeping primary documents (первичные документы).  _(Law 402-ФЗ)_

## 3. КУДиР Details (книга учёта доходов и расходов)

**Who keeps it:** ИП on УСН (and the ОСНО analogue, the книга учёта доходов и расходов и хозяйственных операций). Самозанятые (НПД) do **not** keep a КУДиР.

- **What goes in it (УСН)** — All taxable income, recorded by the cash method (on the date money is received). For "Доходы минус расходы": deductible expenses, recorded when both paid and the underlying obligation is met, with the supporting первичный документ referenced. Entries are chronological, continuous, and complete; each entry references the primary document (number, date, description).
- **Electronic vs paper КУДиР** — The ИП may choose either. If paper, the book must be laced, page-numbered (прошита и пронумерована). If electronic, it is printed, laced and numbered at year-end and signed.
- **ФНС certification (заверение)** — No longer required. There is no obligation to take the КУДиР to the tax office to be certified — current Минфин/ФНС orders for the УСН, patent and ЕСХН books contain no certification requirement. The taxpayer may still ask the tax office to certify it voluntarily. The book is presented to ФНС only on request (during a check). (Verify current value — re-check the controlling order.)
- **Form to use (2026)** — For 2026 use the КУДиР form approved by Приказ ФНС ЕА-7-3/816@ of 07.11.2023 — verify this is still the current form, as КУДиР forms are reissued periodically.  _(Приказ ФНС ЕА-7-3/816@ of 07.11.2023)_
- **Penalty for absence / gross errors** — Absence or material defects in the КУДиР can attract a penalty under ст. 120 НК РФ (commonly cited as 10,000 ₽ for one period; some sources cite a 200 ₽ document-failure penalty under ст. 126 — verify current value and the applicable article before quoting a number to a user).  _(ст. 120 НК РФ; ст. 126)_

## 4. ККТ / Онлайн-касса — Who, Exemptions, OFD

- **What ККТ is** — ККТ (контрольно-кассовая техника), in modern form an онлайн-касса — a fiscal cash register that transmits each sale electronically. Governed by Law 54-ФЗ.  _(Law 54-ФЗ)_
- **Who must use ККТ** — Broadly, anyone (ИП or company) who takes payment from individuals for goods, works, or services — whether cash or card. The general deferral that let ИП without employees selling their own goods/works/services skip ККТ ended on 01.07.2021. Since then most such ИП must apply ККТ. (Verify whether any later, narrower deferral applies to the user's activity.)  _(Law 54-ФЗ)_
- **Key exemptions** — **Самозанятые (НПД): exempt.** «Мой налог» issues the чек and transmits data to ФНС; no separate онлайн-касса is needed. This is the cleanest exemption. - **Payments received only from organisations / other ИП by bank transfer** (B2B non-cash to a current account) generally do not require ККТ. - Certain **patent (ПСН)** activities and a list of specific activities/locations in 54-ФЗ are exempt — verify the user's specific activity, as the list is narrow and changes.  _(Law 54-ФЗ (verify each exemption before relying))_
- **OFD (оператор фискальных данных)** — The licensed intermediary between the онлайн-касса and ФНС. The cash register sends each fiscal document (чек) to the OFD, which validates it and forwards it to ФНС (within 24 hours), and stores fiscal data for 5 years. Any business using ККТ must have a contract with an accredited OFD. The OFD's retention is separate from — and does not replace — the taxpayer's own document retention.
- **Penalties for non-application of ККТ** — Non-application of required ККТ is penalised under КоАП ст. 14.5 (a percentage of the unrecorded turnover, with minimums) — verify current amounts.  _(КоАП ст. 14.5)_

## 5. Primary Documents (первичные документы) + Retention

- **Core primary documents** — - **Акт** (акт выполненных работ / оказанных услуг) — confirms services/works were delivered and accepted; the main document for service freelancers. - **Накладная** (товарная накладная ТОРГ-12, or УПД — универсальный передаточный документ) — confirms transfer of goods. - **Счёт** (счёт на оплату) — an invoice/payment request; not itself a tax document but the standard basis for payment. - **Счёт-фактура** — the VAT document, relevant for ИП on ОСНО who charge VAT (and for the buyer's input-VAT deduction). Not used by НПД or by most УСН ИП. - **Чек** — the fiscal receipt from онлайн-касса (ИП) or from «Мой налог» (самозанятый). - **Bank statements (банковские выписки)** — evidence of receipts and payments under the cash method. Even самозанятые, who keep no ledger, should keep their чеки (auto-stored in «Мой налог») and any договор/акт with business clients.
- **Retention period for tax records/primary documents** — 5 years (generally 5 years for tax records and the documents supporting income, expenses, and tax paid; the 5 years run from the year following the year the document was last used for tax purposes. Some categories (e.g. records supporting loss carry-forward, fixed-asset records) must be kept longer — verify for the specific document.)  _(ст. 23 НК РФ; Law 6-ФЗ of 17.02.2021 (4→5 year change))_

## 6. Worked Examples

### Example 1 — Самозанятый designer (НПД), individual clients.

Anna is a самозанятая graphic designer. For each paid project she opens «Мой налог», enters the amount and client type (individual → 4%), and the app issues a чек and adds the tax to her monthly bill. She keeps **no КУДиР**, files **no declaration**, and needs **no онлайн-касса**. Records to retain: the чеки (kept in the app) and, ideally, simple contracts/акт for larger jobs. *Risk to flag:* failing to issue a чек for a payment is a penalty (20% of the amount; 100% on repeat within 6 months — verify current value).

### Example 2 — ИП on УСН "Доходы", retail to the public.

Boris is an ИП on УСН 6% selling phone accessories from a kiosk, taking cash and cards from individuals. He **must use an онлайн-касса** with an OFD contract (the without-employees deferral ended 01.07.2021). He records income in the **КУДиР** (current form per Приказ ФНС ЕА-7-3/816@ — verify), keeps it electronically, and prints/laces/numbers it at year-end. **No ФНС certification** of the book is required; he presents it only on request. He keeps накладные from suppliers, чеки, and bank statements for **5 years**. He does **not** keep full бухгалтерский учёт.

### Example 3 — ИП on ОСНО providing IT services to businesses, no cash.

Vera is an ИП on ОСНО, paid only by bank transfer from company clients. She keeps the **книга учёта доходов и расходов и хозяйственных операций** (Приказ Минфина 86н), issues an **акт** and **счёт** (and **счёт-фактура** with VAT) for each engagement, maintains книга покупок / книга продаж for VAT, and files **3-НДФЛ** annually plus VAT returns. Because she receives money only from organisations by bank transfer, an **онлайн-касса is generally not required** — verify against her exact payment flows. Retention: **5 years**.

### Example 4 — Switching самозанятый → ИП on УСН mid-activity.

A self-employed person whose income approaches the **НПД limit of 2,400,000 ₽/year** (verify current value) should plan to leave НПД and register a different regime. On НПД there is no ledger; once on УСН they must **start a КУДиР** from the date the УСН regime begins, and reassess **онлайн-касса** obligations (which НПД exempted them from).

## 7. Tier 2 Notes + References + Checklist

### Tier 2 / ambiguity flags (escalate or verify, do not guess)

- Exact **current КУДиР form** and any 2026 reissue.
- Whether a **specific activity** qualifies for a 54-ФЗ ККТ exemption (list is narrow, changes often).
- **Penalty amounts** under ст. 120 / ст. 126 НК РФ and КоАП ст. 14.5 — verify before quoting figures.
- **НПД income limit** (2,400,000 ₽; possible increase to 3,000,000 ₽ discussed but not confirmed as of May 2026 — verify current value).
- Patent (ПСН) regime specifics — out of primary scope here; route to a patent-specific resource.
- ООО / legal-entity бухгалтерский учёт — **out of scope** (this skill is self-employed only).

### References (verify at point of use)

- nalog.gov.ru — ФНС России (primary authority)
- npd.nalog.ru — официальный портал НПД / самозанятые; app «Мой налог»
- НК РФ ст. 23 (retention), ст. 120/126 (record-keeping penalties)
- Law 54-ФЗ (ККТ / онлайн-касса / OFD)
- Law 422-ФЗ of 27.11.2018 (НПД)
- Law 402-ФЗ (бухгалтерский учёт; ИП exemption)
- Приказ Минфина 86н/БГ-3-04/430, 13.08.2002 (ИП ОСНО ledger)
- Приказ ФНС ЕА-7-3/816@, 07.11.2023 (УСН КУДиР form — verify still current)
- lkfl2.nalog.ru / lkip.nalog.ru (личный кабинет)

### Checklist (run before concluding)

- [ ] Regime identified: НПД / УСН / ОСНО (or other → escalate)?
- [ ] Correct ledger named for that regime (or "no ledger" for НПД)?
- [ ] ККТ / онлайн-касса obligation assessed, including exemptions?
- [ ] OFD mentioned if онлайн-касса applies?
- [ ] Primary documents listed for the regime (акт / накладная / счёт / счёт-фактура / чек)?
- [ ] Retention stated as 5 years (with longer-period caveat)?
- [ ] Confirmed ИП do not keep full бухгалтерский учёт?
- [ ] All unverified figures/forms flagged "verify current value"?
- [ ] Reply in the user's language; Russian terms kept verbatim?

## PROHIBITIONS

- **Prohibitions list** — - Do not invent or guess КУДиР/declaration form numbers, line numbers, tax rates, thresholds, or penalty amounts. If not verified, write "verify current value" and cite nalog.gov.ru. - Do not tell an ИП they must keep full бухгалтерский учёт or file бухгалтерская отчётность — that is an ООО obligation, not an ИП obligation. - Do not tell a самозанятый (НПД) to keep a КУДиР or to install an онлайн-касса — «Мой налог» replaces both. Conversely, do not tell them they may skip issuing a чек. - Do not assert a ККТ exemption for an ИП based on "no employees" alone — that general deferral ended 01.07.2021. Verify a current, specific exemption before advising no касса. - Do not advise shorter retention than 5 years; do not claim 4 years (changed in 2021). - Do not handle ООО / legal entities, patent (ПСН) specifics, payroll, or non-self-employed scenarios under this skill — route elsewhere. - Do not present this output as filed/final advice without a qualified Russian accountant's sign-off.

## Disclaimer

This skill is research-verified content from the Open Accountants Community, current to the best available public sources as of May 2026, and is pending sign-off by a qualified Russian accountant. It is general information, not individualised tax advice. Russian tax law (НК РФ, 54-ФЗ, 422-ФЗ, ФНС orders) changes frequently; always verify forms, rates, thresholds, and exemptions against nalog.gov.ru (and npd.nalog.ru for самозанятые) at the point of use. A qualified Russian accountant or tax adviser must review any output before it is relied upon for filing. See openaccountants.com.

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
