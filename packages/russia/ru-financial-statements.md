---
name: ru-financial-statements
description: Use this skill whenever asked about financial statements or formal accounting reporting obligations in Russia for self-employed people, individual entrepreneurs (ИП), or the organisations they might set up (ООО, АО). Trigger phrases like "Russia financial statements", "бухгалтерская отчётность", "РСБУ", "ФСБУ", "do I file accounts as ИП", "ГИР БО", "бухгалтерский баланс", "отчёт о финансовых результатах", "обязательный аудит", "упрощённая бухгалтерская отчётность", "МСФО / IFRS Russia", "consolidated financial statements Russia", "when does an ООО file accounts", "31 марта deadline accounts". Explains that an ИП and a самозанятый file NO financial statements (Federal Law 402-ФЗ), and what changes if they incorporate an organisation.
version: 1.0
jurisdiction: RU
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# RU Financial Statements

## Russia (RU) — Financial Statements & Accounting Reporting (2026)

This skill covers formal **бухгалтерская (финансовая) отчётность** (financial / accounting statements) in Russia: who must prepare and file them, under which standards, in what components, by when, and when a statutory audit is required.

The reply language follows the user (English prose, with native Russian legal terms kept verbatim because those are the exact terms the user will see on the ФНС portal, in accounting software, and on the statements themselves). Russian terms used: бухгалтерская (финансовая) отчётность, бухгалтерский учёт, бухгалтерский баланс, отчёт о финансовых результатах, РСБУ (российские стандарты бухгалтерского учёта), ФСБУ (федеральные стандарты бухгалтерского учёта), ПБУ, МСФО (международные стандарты финансовой отчётности / IFRS), ГИР БО (государственный информационный ресурс бухгалтерской отчётности), ФНС, ИП, ООО, АО, ПАО, СМП (субъекты малого предпринимательства), обязательный аудит, КУДиР.

**Core message for a self-employed reader:** As an **ИП** or a **самозанятый**, you file **none** of the financial statements described here. Formal бухгалтерская отчётность is an *organisation's* obligation (ООО, АО). This skill exists so you understand (a) why you are exempt, and (b) what changes the day you set up an ООО.

> YMYL note: tax and accounting rules change. Figures, thresholds and form numbers below were web-verified against ФНС (nalog.gov.ru), the Ministry of Finance (minfin.gov.ru) and reputable Russian accounting sources as of **May 2026**. Anything marked "verify current value" must be re-checked at point of use.

## 1. Quick Reference + Conservative Defaults

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Russia (RU) |
| Who prepares financial statements | Organisations — **ООО, АО, ПАО** (and other legal entities). **ИП and самозанятые are exempt** (402-ФЗ). |
| Standards | **РСБУ / ФСБУ** (federal accounting standards) for statutory statements; **МСФО (IFRS)** for consolidated statements of banks, insurers, NPFs and listed/public-interest groups (208-ФЗ). |
| Reporting currency | Russian rouble (**RUB / ₽**) |
| Primary legislation | Federal Law **402-ФЗ** "О бухгалтерском учёте"; **ФСБУ 4/2023** (statements); **208-ФЗ** (consolidated/IFRS); **307-ФЗ** (audit); **209-ФЗ** (СМП criteria). |
| Authority / register | **ФНС** — statements filed into the state register **ГИР БО** (государственный информационный ресурс бухгалтерской отчётности). |
| Annual filing deadline | **31 March** of the year following the reporting year (e.g. FY2025 → **31 March 2026**); shifts to the next business day if it falls on a weekend/holiday. |
| Filing format | **Electronic only**, via telecom channel to ФНС / ГИР БО; ФНС formats per приказ 15.11.2024 № ЕД-7-1/1041@ (verify current order). |
| Quality tier | **Research-verified — pending sign-off by a qualified Russian accountant.** |
| Skill version | 1.0 |

- **Conservative default — assume ИП/самозанятый** — Assume the user is an ИП or самозанятый unless they say "ООО" / "АО" / "company". If self-employed, the answer to "do I file financial statements?" is no — point them to КУДиР / tax reporting instead (cross-ref ru-bookkeeping).  _(402-ФЗ)_
- **Conservative default — full РСБУ/ФСБУ assumption** — If they have incorporated, assume full РСБУ / ФСБУ applies until СМП small-enterprise status is confirmed; do not assume the simplified option without checking 209-ФЗ criteria.  _(209-ФЗ)_
- **Conservative default — audit requirement not assumed** — Do not assume an audit is or is not required — check the 307-ФЗ thresholds against the prior year's revenue and balance-sheet assets.  _(307-ФЗ)_
- **Conservative default — date-sensitive figures** — When a threshold or form number is date-sensitive, state the verified figure and add "verify current value at nalog.gov.ru / minfin.gov.ru."
- **Conservative default — never file/sign on user's behalf** — Never file or e-sign on the user's behalf; produce drafts/explanations for a qualified Russian accountant (бухгалтер / аудитор) to review and sign.

## 2. ИП / самозанятый vs Organisation — Who Files What

Russia separates **бухгалтерский учёт** (financial accounting → financial statements) from **налоговый учёт** (tax accounting → tax returns). The self-employed do the second, not the first.

- **Самозанятый (НПД) filing obligations** — No бухгалтерский учёт. No financial statements. No КУДиР. Income is recorded only by issuing receipts (чеки) in the «Мой налог» app; tax is computed automatically. Files nothing into ГИР БО.
- **ИП exemption from бухгалтерский учёт** — Under 402-ФЗ ст. 6, an ИП is exempt from keeping бухгалтерский учёт provided they keep tax accounting (typically КУДиР — книга учёта доходов и расходов, or the equivalent register for the regime). Applies under any tax regime — УСН, ОСНО, ПСН, ЕСХН, АУСН.  _(402-ФЗ ст. 6)_
- **ИП files nothing into ГИР БО** — An ИП files no бухгалтерский баланс, no отчёт о финансовых результатах, and nothing into ГИР БО — under any tax regime.  _(402-ФЗ ст. 6)_
- **ИП voluntary accounting** — An ИП may keep accounting voluntarily, but is never required to file statements. For what an ИП does keep (КУДиР, ККТ/онлайн-касса, primary documents), see ru-bookkeeping.
- **Organisation accounting obligation** — Organisations (ООО, АО, ПАО, etc.) must keep full бухгалтерский учёт and must prepare and file annual бухгалтерская (финансовая) отчётность — regardless of tax regime (yes, including an ООО on УСН). Files annual statements electronically into ГИР БО via ФНС by 31 March. May qualify for simplified accounting and simplified statements if it is a СМП (small enterprise) and not otherwise excluded (see §3).

The transition that matters for a self-employed reader: the moment you register an ООО, you acquire a full accounting obligation — chart of accounts, double entry, annual statements, ГИР БО filing, and potentially audit. This is the single biggest administrative difference between operating as an ИП and operating as a company, and it is usually why a one-person business stays an ИП.

## 3. Components of Financial Statements + the Simplified СМП Option

Statutory annual financial statements under ФСБУ 4/2023 (which replaced ПБУ 4/99 and the форм приказ № 66н, applied from the FY2025 statements filed in 2026) comprise the following.

- **Full set (standard organisations)** — 1. Бухгалтерский баланс — the balance sheet. 2. Отчёт о финансовых результатах — the statement of financial results (P&L). 3. Приложения (appendices), which include: Отчёт об изменениях капитала (statement of changes in equity); Отчёт о движении денежных средств (cash-flow statement); Пояснения (notes / explanatory disclosures). 4. For organisations subject to обязательный аудит, the аудиторское заключение (audit report) is filed into ГИР БО alongside the statements (within the deadline, or within 10 business days after the audit report date but no later than 31 December of the following year — verify current rule).  _(ФСБУ 4/2023)_
- **Simplified set for СМП** — A small enterprise that is eligible to use simplified accounting may prepare a reduced set: Бухгалтерский баланс and Отчёт о финансовых результатах in upbeat/aggregated (укрупнённые) line items, and it may omit the separate statements of changes in equity, cash flows, and detailed notes unless their absence would prevent a fair view.
- **СМП average headcount threshold** — up to 100 employees (small); up to 15 = micro employees  _(209-ФЗ ст. 4)_
- **СМП annual income threshold** — up to 800 million ₽ (small); up to 120 million ₽ = micro RUB  _(209-ФЗ ст. 4)_
- **СМП additional tests and category determination** — Plus structural/ownership tests (limits on foreign and large-company shareholding). Category is taken as the higher of the headcount and income tests.  _(209-ФЗ ст. 4)_
- **Exclusions from simplified accounting even if СМП** — 402-ФЗ excludes certain entities even if small — including those subject to обязательный аудит, plus listed/issuer entities, housing cooperatives, microfinance organisations, law-firm and notarial bar entities, NPOs performing the functions of a foreign agent, and others (verify current exclusion list). Practically: if an organisation triggers mandatory audit, it cannot use the simplified statements, even if it is otherwise small.  _(402-ФЗ)_

## 4. РСБУ / ФСБУ vs IFRS (МСФО)

РСБУ (российские стандарты бухгалтерского учёта) is the national framework. It is being modernised standard-by-standard into ФСБУ (федеральные стандарты бухгалтерского учёта), which progressively replace the older ПБУ. Statutory statements filed into ГИР БО are prepared under РСБУ/ФСБУ. Key relevant standard: ФСБУ 4/2023 «Бухгалтерская (финансовая) отчётность», mandatory from the FY2025 statements (filed in 2026), incorporating amendments by приказ № 159н of 07.11.2025 (verify). Other ФСБУ govern fixed assets, inventories, leases, intangible assets, etc.

- **МСФО (IFRS) required entities** — МСФО (IFRS) is required for consolidated financial statements of specific public-interest entities under Federal Law 208-ФЗ, including: credit institutions / banks (and their groups/holdings); insurers and mutual insurance societies; негосударственные пенсионные фонды (NPFs); publicly traded companies (ПАО) and entities whose securities are admitted to organised trading; clearing organisations and certain other listed/specified groups.  _(208-ФЗ)_
- **Consolidated vs individual statements** — These entities prepare consolidated statements under МСФО in addition to their individual (separate) РСБУ/ФСБУ statements. ФСБУ 4/2023 does not govern the 208-ФЗ consolidated statements.  _(208-ФЗ; ФСБУ 4/2023)_

МСФО is effectively never relevant to an ИП or to a small ООО. A small ООО reports under РСБУ/ФСБУ only. IFRS comes into play only at the banking / insurance / listed-group scale.

## 5. Audit Requirements (Обязательный аудит) + Thresholds

- **Mandatory audit governing rule** — A statutory annual audit (обязательный аудит) is governed by 307-ФЗ ст. 5. It is required if either of the following financial thresholds was exceeded in the preceding year (verify current values — these were confirmed for FY2025 audited in 2026).  _(307-ФЗ ст. 5)_

**Audit threshold triggers**  _(307-ФЗ ст. 5)_

| Trigger (any one) | Threshold |
| --- | --- |
| **Доход (revenue)** for the preceding year, per Tax Code ch. 25 (line 2110 of the отчёт о финансовых результатах, **net of VAT**) | **> 800 million ₽** |
| **Сумма активов (total balance-sheet assets)** as at 31 December of the preceding year | **> 400 million ₽** |

- **FY2025 audit determination example** — For FY2025 statements (audited in 2026): audit is mandatory if 2025 revenue > 800 млн ₽ or assets at 31.12.2025 > 400 млн ₽.  _(307-ФЗ ст. 5)_
- **Status/sector audit triggers** — Audit required regardless of size for: Публичные акционерные общества (ПАО); non-public АО whose securities are admitted to organised trading; credit institutions / banks (and groups, holdings); insurers and mutual insurance societies; негосударственные пенсионные фонды (NPFs); professional participants of the securities market; entities that publish/file consolidated statements; and others named in 307-ФЗ or separate laws (verify current list).  _(307-ФЗ)_
- **Consequences and filing of audit report** — The аудиторское заключение is filed into ГИР БО with the statements. Absence of a required audit / failure to file the report exposes the organisation to administrative penalties (verify current КоАП amounts). ИП и самозанятые are never subject to обязательный аудит because they have no statutory financial statements to audit.

## 6. Worked Examples

### Example A — Самозанятый designer (НПД).

Question: "Do I need to file бухгалтерская отчётность or a balance sheet?"
Answer: No. A самозанятый keeps no бухгалтерский учёт, files nothing into ГИР БО, and has no balance sheet. Income is captured only via чеки in «Мой налог». Nothing in this skill applies — see ru-bookkeeping / ru-self-employed-npd.

### Example B — ИП on УСН, ~5 million ₽ turnover, no employees.

Question: "My friend with an ООО filed accounts by 31 March. Do I have to?"
Answer: No. Under 402-ФЗ ст. 6 an ИП is exempt from бухгалтерский учёт and files no financial statements under any regime — including УСН. The 31 March / ГИР БО obligation is an organisation's duty. The ИП keeps a КУДиР for tax purposes and files the УСН tax return on its own schedule (see ru-usn). No audit, ever.

### Example C — Small ООО on УСН, 2025 revenue 60 million ₽, assets 12 million ₽, 8 staff.

Question: "We just incorporated last year — what's the difference now, and do we need an auditor?"
Answer: The ООО must keep full бухгалтерский учёт and file annual бухгалтерская отчётность into ГИР БО via ФНС by 31 March 2026 for FY2025, even though it is on УСН. It meets the СМП criteria (revenue < 800 млн ₽, ≤ 100 staff), so it may use simplified accounting and the reduced statement set (aggregated баланс + отчёт о финансовых результатах, omitting the separate equity/cash-flow statements and detailed notes). No обязательный аудит — both 2025 revenue (60 млн < 800 млн) and assets (12 млн < 400 млн) are below the 307-ФЗ thresholds, and no sector trigger applies. The big change versus being an ИП: full accounting + annual ГИР БО filing now exist where they did not before. (Have a qualified бухгалтер confirm СМП eligibility and prepare the statements.)

## 7. Tier 2 Notes + References

Route to a qualified Russian accountant / auditor: Preparation of the actual баланс / отчёт о финансовых результатах line items, чёт of accounts, and ФСБУ measurement (fixed assets, leases, inventories, deferred tax). 208-ФЗ consolidated statements and full МСФО (IFRS) application. Conducting or selecting an обязательный аудит; audit-firm engagement. Reorganisation, liquidation, interim (промежуточная) statements, first-period and short-period statements after incorporation. КоАП/tax penalties for late or non-filing and their mitigation. Whether to incorporate an ООО at all (tax/structuring decision — separate analysis).

402-ФЗ "О бухгалтерском учёте" — esp. ст. 6 (ИП exemption; simplified accounting eligibility). ФСБУ 4/2023 "Бухгалтерская (финансовая) отчётность" (Минфин приказ № 157н of 04.10.2023; amendments приказ № 159н of 07.11.2025). 208-ФЗ "О консолидированной финансовой отчётности" (МСФО scope). 307-ФЗ "Об аудиторской деятельности" — ст. 5 (mandatory audit triggers/thresholds). 209-ФЗ — ст. 4 (СМП small/medium-enterprise criteria). ФНС / ГИР БО: nalog.gov.ru (state accounting-statements register; e-filing formats per приказ ЕД-7-1/1041@ of 15.11.2024). Минфин: minfin.gov.ru (ФСБУ / accounting standards). Cross-references: ru-bookkeeping (КУДиР, ККТ, what ИП keep), ru-usn, ru-income-tax, ru-self-employed-npd.

## PROHIBITIONS

Do NOT tell an ИП or самозанятый that they must file бухгалтерская отчётность, a баланс, or anything into ГИР БО. They are exempt under 402-ФЗ. This is the most common and most damaging error for this jurisdiction.
Do NOT prepare, sign, or e-file financial statements, audit reports, or ГИР БО submissions on the user's behalf. Produce drafts/explanations only.
Do NOT state audit, СМП, or filing-threshold figures as settled without flagging "verify current value" — these change by law and ministerial order.
Do NOT assume the tax regime removes the obligation for an organisation — an ООО on УСН still files annual statements.
Do NOT apply МСФО (IFRS) to an ordinary small ООО, ИП, or самозанятый.
Do NOT confuse налоговая отчётность (tax returns) with бухгалтерская отчётность (financial statements) — they are distinct obligations with distinct recipients and deadlines.
Do NOT give legal certainty on penalties, audit selection, or eligibility edge cases — route to a qualified Russian бухгалтер / аудитор.

## Disclaimer

This skill is research-verified against ФНС (nalog.gov.ru), the Russian Ministry of Finance (minfin.gov.ru), and reputable Russian accounting sources as of May 2026, but it is pending sign-off by a qualified Russian accountant (бухгалтер / аудитор). It is general information, not accounting, audit, tax, or legal advice, and does not create a professional engagement. Russian accounting law, ФСБУ, and the 307-ФЗ / 209-ФЗ thresholds change frequently; always re-verify current values and have all financial statements, audit determinations, and ГИР БО filings reviewed and signed by a credentialed Russian professional before submission. Part of the open-source tax skills at openaccountants.com.

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
